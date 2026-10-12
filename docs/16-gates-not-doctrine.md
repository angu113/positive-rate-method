# 16 — Gates, Not Doctrine: Making the Constitution Enforce Itself

> **Status: proposed for v0.16.** Drafted 2026-10-12 from three months of
> running this method on a live, multi-agent project (the case study).
> Evidence is graded OBSERVED / INFERRED / REPORTED as in doc 12. Nothing here
> is accepted until it passes the validation rule in CONTRIBUTING.md.

Docs 02 and 12 tell you to write a constitution. They do not tell you what
happens to it. This doc is about what happened to ours, and what we built so
that the rules that matter stop depending on the agent remembering them.

## 1. The failure: a constitution is prose, and prose decays

A constitution is read at session start and then competes with everything else
in the context for the rest of the session. The longer the session, and the
longer the constitution, the less any one rule weighs. Nobody has to decide to
ignore a rule for it to stop being followed.

What we observed (OBSERVED, project adherence audit, September 2026):

- The constitution had grown to **520 lines** of rules, rationale and incident
  stories.
- An audit of **51 rules** found **41 leave no trace when they are followed.**
  You cannot tell a session that obeyed from one that did not. The only
  evidence of adherence was the absence of a visible failure.
- Classified by whether a check could be written: **34 instrumentable, 4
  human-only, 3 unprovable.** Most rules *could* have been checked and were
  not.
- The "drift" hypothesis, that old claims in the constitution had gone stale,
  was tested on 20 claims and **failed: 0 of 20 had drifted.** The problem was
  not that the rules were wrong. It was that they were not enforced.
- The fix was a **cut from 520 to about 90 lines**, with each remaining rule
  carrying a pointer to the thing that enforces it, and a CI check on the file.

The lesson is blunt: **a rule with no gate is a wish.** The more rules you add
to the document, the weaker each one becomes, so the way to make a rule
stronger is usually to take words out of the constitution and put a check
somewhere else.

## 2. The ladder

Every rule in the constitution carries one of three modes, written in the same
line as the rule:

| Mode | Meaning | What enforces it |
|---|---|---|
| **BLOCKING** | The action is refused. | A hook that denies the tool call, or a CI check that fails the build. |
| **CONVENTION** | The action is allowed, but it leaves a trace someone can check. | A log line, a required field, a report that names the thing, a check that flags after the fact. |
| **STATED GUIDANCE** | Intent only. | Nothing. The line says so. |

Two rules about the ladder:

1. **STATED GUIDANCE is the default.** A new rule starts there. A rule with no
   stated mode is read as STATED GUIDANCE, so nothing sounds more binding than
   it is.
2. **Promotion is a logged decision.** Moving a rule up is a `CONST:` commit
   that cites the evidence (see section 4). There is no fourth mode called
   "important".

The point of naming the mode is honesty. A reader, or an agent, can see
at a glance which rules will stop them and which depend on their own
discipline.

## 3. Prefer a gate to a reminder

State this once, in the constitution's philosophy section:

> Prefer a deterministic, externally-checkable gate over a prose reminder.
> Where a rule cannot be made mechanical, tie it to the most concrete,
> frequent trigger available, not to a cadence.

The second sentence matters. "Check X every few sessions" never fires. "Check
X when the tool call contains `git merge`" fires every time it is relevant.
When a rule cannot be a hook, find the concrete event it belongs to and attach
it to that event.

### Classifying a rule

For each rule ask, in order:

1. **Can a program decide whether it was followed?** If yes, it is
   *instrumentable*. Write the check. Prefer blocking; accept flagging.
2. **If not, can a human decide, from something the session leaves behind?**
   It is *human-only*. Put the trace in a log the operator reads.
3. **If neither, is the rule about judgment inside the agent's head?** It is
   *unprovable*. Leave it as STATED GUIDANCE and say so. Do not dress it up.

Most rules turn out to be instrumentable. That was the surprise.

### What a gate looks like

Gates are small. Ours are a few dozen lines each. Four shapes cover most
needs:

- **PreToolUse hook** that reads the tool call and denies it: no commit to the
  default branch from the main checkout, no worktree removal while another
  worktree is nested under it, no issue close with an unchecked acceptance
  criterion, no launching the app from the agent's shell.
- **PostToolUse hook** that flags after the fact: a `git merge` ran and
  `origin/<branch>..<branch>` is non-empty, so say so now.
- **CI check** on the repository itself: no bare SQL `DELETE`, a named test
  that pins a business invariant, and the constitution validator (section 5).
- **Dispatch gate** for agent spend (doc 17).

A gate that blocks should print what it blocked and what to do instead.

## 4. Incident first, hook second, rule last

Every mechanically enforced rule on our project began as a breakage, and the
order was always the same: something went wrong, a hook was written, and only
then was the rule worded. Rules written *before* an incident were the ones that
decayed.

So the incident log (`templates/incident-log.md`) is the source of gates. The
log needs one column the postmortem-lite template did not have:

> **How detected** — `mechanism` (a check flagged it) or `luck` (a person or a
> different session happened to notice).

Our back-filled log had nine incidents. **Five ended in a hook, and four of
those five were found by luck first.** Four more still have no real gate. The
`luck` rows with no gate built are the to-do list. Reading the column tells
you how much of your safety is design and how much is chance.

Back-fill your own the same way: search the changelog, commit messages and any
note written after something went wrong.

## 5. Gate the constitution itself

Two properties of the constitution can be checked mechanically, and both
should be, in CI:

- **Size.** A token cap (we use `chars/4 <= 1500`). It stops the regrowth that
  caused the original problem. Without it the file grew back in weeks.
- **Cited paths resolve.** Every backtick-quoted repo path must exist. A rule
  that points to a hook that was renamed is a rule with no gate and no
  warning.

`templates/validate_constitution.py` is a stdlib-only version of ours. Two
lessons from running it:

- Judge exclusions on the path **relative to the repo root**. Ours excluded
  `.claude/worktrees` using absolute path parts, so it passed in CI and failed
  inside every agent worktree. That is the typical failure of a gate that was
  only ever tested in one environment.
- A check that only runs in CI is invisible during the session. Run it from
  the session-start check as well.

## 6. A silent gate looks exactly like a working one

A hook that is not wired into settings, or whose interpreter is missing from
the path, blocks nothing and says nothing. The first symptom is the incident
it was supposed to stop.

So every gate reports its own state. Ours prints one line at session start,
`USAGE GATE INERT on this box`, when the dispatch gate is not enforcing. Make
the session-start check list each hook and whether it is live, and treat an
inert gate as louder than a missing one.

Test a new gate by **deliberately breaking the rule once** and watching it
fire. A gate you have never seen fire is an assumption.

## 7. The gate ledger

`templates/gate-ledger.md` is one table: every rule in the constitution, its
mode, its gate or trace, and the gap. It is the working list for "what should
we instrument next", and it shares its rows with the incident log: the
incident is the reason, the ledger is the status.

Keep two kinds of rows. Constitution rules, and process rules that live outside
the constitution (the "last synced" pointer to this method, a cost-ledger
"confirmed" status). The second kind fails silently most often, because
nobody thinks of it as a rule.

## 8. Limits of the idea

- **A gate enforces what it checks, not what you meant.** A hook that blocks
  `git commit` on the default branch does not stop a merge to it. Write the
  gate, then try to get around it.
- **The agent can disable a gate it can edit.** Keep hook files and settings
  under review, and let only a person change a limit (doc 17).
- **Gates cost attention.** Every blocked action is friction. Prefer flagging
  to blocking until the incident has actually recurred.
- **The cut can lose information.** We moved rationale to docs the
  constitution points at. The constitution must say where, and the validator
  must check the pointer.
- **Single project.** This is OBSERVED on one project, with one operator. Treat
  the numbers as one data point.

## Constitution fragment

```
- Prefer a deterministic, externally-checkable gate over a prose reminder.
  Where a rule can't be made mechanical, tie it to the most concrete,
  frequent trigger available, not a cadence.
- Every non-negotiable names its mode and its gate in the same line:
  BLOCKING (hook/CI refuses) · CONVENTION (leaves a checkable trace) ·
  STATED GUIDANCE (intent only; the default when unstated).
- Promoting a rule up the ladder is a logged CONST: decision citing an
  incident-log row. New rules are STATED GUIDANCE.
- The constitution has a size cap and cited-path check in CI. A rule that
  needs a paragraph belongs in a doc it points to.
```
