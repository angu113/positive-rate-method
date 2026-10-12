# 17 — Running Agents at Scale: Topology, Authority and Usage Gates

> **Status: proposed for v0.16.** Drafted 2026-10-12 from one live project that
> grew from one operator and one agent to several machines running dispatched
> agents. Evidence grades as in doc 12. Single-project evidence.

The method's default picture is one operator and one agent. Doc 04 covers
parallel lanes and worktrees. It does not cover what happens when agents
dispatch other agents, when several machines share one usage allowance, or when
an agent that was told to do one small thing goes on to do the next ten.

## 1. Roles

Two session roles worked, and mixing them did not:

| Role | Does | Never does |
|---|---|---|
| **Daily-work session** | Research, planning, batch creation, the operator's conversation. Enqueues work. | Registers as a worker. Runs the batch itself. |
| **Governor** | Dispatch only. Claims queued work, spawns one worker per item, reports. Safe to clear and restart. | Enqueue, edit code, ask the operator questions. If the operator speaks to it, it forwards the words verbatim. |

Reason (OBSERVED): a single session that ran a whole batch's
claim, dispatch, verify and complete loop inline grew its own context by the
batch's full history. The split keeps the long-lived session thin and
disposable.

Inside a dispatched item, **Maker/Checker**: a Maker builds on its own branch; a
separate Checker verifies and merges. The orchestrator does not do the work
itself except for a single-file, no-logic tweak; it dispatches, verifies,
merges, confirms the shared remote, and reports.

## 2. The authority boundary

Orchestrator-not-executor says a worker's output must be verified. It does not
say **what class of action a worker may take unsupervised.** Two incidents in
one session showed the gap (OBSERVED):

1. A worktree agent told to "self-rebase onto fresh master as your last step"
   merged and pushed its own work before review.
2. A *fork* of the orchestrator, which inherits full context and judgment, was
   dispatched to relay one message. It chained through the rest of the workflow
   and ran a **production release** end to end. Nothing broke. The safety
   property, that a person sees a hard-to-reverse action before it ships, was
   not in effect.

Rule: **anything outward-facing or hard to reverse executes in the
orchestrator's own foreground turn, never in a dispatched worker, whatever its
scope or type.** That covers a production release, a push to a shared or
customer-facing system, an irreversible delete, and spending beyond a granted
limit. Brief wording ("leave your branch unpushed") is a per-task fix. The
boundary has to be a hook or a standing rule every brief cites.

A fork is a worker with the orchestrator's judgment, which makes it *more*
dangerous than a fresh agent, not less.

## 3. One versioned rules file for dispatched agents

Do not re-paste process rules into every brief. They go stale in the briefs and
nobody notices. Keep one `agent-rules.md` with a version in its own header. A
brief cites "the current version of that file" rather than a number, and the
completion report records the version the agent read. Our rule count grew past
thirty-five, and the cost of the single file was that the numbers drifted in
every document that pinned one.

A stuck agent **reports at completion with a NOT-OBSERVED line**: what it could
not verify. It does not hand off mid-task, and it does not assume a background
notification will wake it. A subagent does not wake itself from a background
process (OBSERVED four times in one session). It polls inside its own turn or
says plainly that it is stuck.

## 4. Spend: usage windows and who may lift a stop

Doc 13 governs subscriptions and per-run budgets. Agent work has a second
meter: **usage windows** (a short rolling window and a weekly one) that are
shared by every machine on the same account. Observed: three machines hit 90%
of the weekly window at once and all parked.

What worked:

- A **dispatch gate**: a PreToolUse hook on the dispatch tool that reads the
  usage gauge and refuses new work above a headroom threshold (we use 80% and
  90%, with an override above those).
- A **soft limit is a person's grant**, not a dollar spend. Overage credit is
  counted only past 100%.
- **Only a person lifts a stop.** A stop that the agent can lift is not a
  stop. A person may grant a dollar-capped allowance for a defined period.
- The gate **reports itself inert** (doc 16, section 6) if the gauge is
  missing or stale, since a dead gate looks like free headroom.
- The prepaid balance, not the gauge, is the real hard stop. The gate should
  park cleanly before zero.

Burst sizing (REPORTED, one rate-limit event): about three concurrent agents
was comfortable; about ten triggered a real limit.

## 5. The flight log at fleet scale

"One line per session" assumes a session is a unit of work. With parallel
agents it is not. See `templates/flight-log.md` for the revised unit (a work
item or PR), the row cap, and the rule that the rollup counts catch types.

## Constitution fragment

```
- Daily-work sessions plan and enqueue; Governor sessions dispatch only.
  A Governor never edits, never enqueues, never asks the operator.
- Outward-facing or hard-to-reverse actions (production release, push to a
  shared system, irreversible delete, spend beyond a grant) run only in the
  orchestrator's own foreground turn. No dispatched worker or fork does them.
- Dispatched agents follow the versioned agent-rules file; briefs cite its
  current version from its own header.
- New agent dispatch is refused under tight usage headroom. Only a person
  lifts a usage stop or sets a dollar-capped grant.
```
