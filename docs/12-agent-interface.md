# 12 — The Agent Interface: Keeping the Conversation at Altitude

The fastest way to lose an operator is to let the agent drag them below
their altitude. An operator who came to govern — purpose, callouts,
acceptance — and finds themselves being asked to review a diff, approve a
refactor, or choose between two design patterns is an operator losing faith
in the whole system. They didn't come to learn the stack. The default
behavior of coding agents is conversational and technically collaborative,
which is right for engineers and wrong for operators. **The interface has
to be constitutional**, because session-level politeness always drifts back
to the default.

Origin rule, verbatim from the practice this method came from:

> **"I am here to govern the process, not to do the coding. Do not show me
> diffs. Do not ask me code questions."**

Four mechanisms make that rule enforceable.

## 1. What Reaches the Operator — the Whole List

The operator receives exactly four kinds of communication, and nothing else:

1. **The CONFIRM BEFORE BUILDING restatement** (CP2) — intent, assumptions,
   files, flags. In business terms.
2. **The change summary** (CP3) — what changed, in behavior terms:
   *"quotes now carry the customer's PO number through to the invoice"*,
   never *"refactored QuoteService to inject IPoNumberResolver."*
3. **Blocker escalations** — schema-halt triggers, red-flag phrases,
   decisions above the agent's altitude, and hard-path conditions (below).
4. **CP4 acceptance instructions** — what to test, with real data, stated
   as workflow steps.

Everything else — architecture choices, pattern selection, refactoring
opportunities, dependency versions, code style — stays inside the session
and gets *decided*, not asked.

### Speak the method, don't name it

Every mechanism in these docs has a plain-language form, and the operator only
ever hears that form. Ask the gate's *question*, never its number:

| Not this | This |
|---|---|
| "CP4 isn't met yet" | "Does this actually remove the thing that was costing you time?" |
| "That's an FL200 decision" | "That's a call about what the business needs — it's yours, not mine." |
| "One-way door, pre-V1" | "Let's settle this before there's real data in it. It gets expensive afterwards." |
| "This triggers a schema-halt" | "That changes how things are stored, so we stop and look at it properly." |
| "What's your FL400?" | "What's this for?" |
| "Classified RED, locking the repo" | "This one's risky enough that nothing else runs alongside it." |

The machinery is followed silently and recorded in the artifacts, where it
belongs. The conversation stays in the operator's own words.

> **Naming a mechanism to the operator is a defect even when the mechanism was
> applied correctly.** It is precisely how a method that claims to scale down to
> nothing starts to feel like a certification course — and an operator who must
> learn vocabulary to use the method has been handed homework the method
> promised not to give.

The failure this prevents arrives through *speech*, not through files, which is
why no artifact-count rule catches it. A first adopter reported it in exactly
these terms: *"the method should sit as a guardian, not as a wizard with
incantations."*

## 2. The Self-Gate: How the Agent Filters Its Own Questions

A constitutional instruction to the agent. Before asking the operator
anything, the agent classifies the question:

> **Is this a business question (callout, rule, priority, acceptance,
> money, risk) or a code question (structure, pattern, naming, library,
> implementation)?**
>
> - **Business** → ask, in business terms, one question at a time.
> - **Code** → do not ask. Choose the boring, conventional option; record
>   the choice and its one-line rationale in a code comment and the change
>   summary's technical appendix; move on.

"Boring and conventional" is the tiebreaker on purpose. An operator-governed
codebase optimizes for *legibility to future sessions and future humans*,
not for elegance. A pedestrian pattern applied consistently beats a clever
one applied once. Code that a senior engineer would call unremarkable is
the target, not a compromise.

This applies to bootstrapping the project's own tooling — version control,
hosting, package manager — exactly as it applies to code. Doc 15 covers the
one exception the self-gate doesn't: an errand only the operator's own
identity can perform, and the security-verification discipline that goes
with it.

## 3. The Code-Quality Backstop: Automation, Not Operator Eyes

The operator never reviews code, so something else must. The constitution
mandates a mechanical quality gate at CP3 — the specific tools are an FL100
choice, but the shape is fixed:

- **Static analysis / inspection runs at every CP3** (linter, analyzer,
  inspection tool appropriate to the stack), with the ruleset committed to
  the repo so every session runs the same law.
- **Tests are blockers.** A failing test is a halt condition, not a
  discussion point.
- **The agent fixes findings or escalates them as blockers.** "What do you
  think about this warning?" is not an option the interface offers.

A generic mechanical gate (compiler, linter, the existing suite staying
green) only proves the codebase didn't regress — it says nothing about
whether a project-specific constitution non-negotiable was actually
honored by *this* package. Any non-negotiable that names a producible
artifact — a test, a written note, a required field, an admin gate;
anything an agent could plausibly skip under pressure while still
reporting "done" — gets its own mandatory field on the CP3 checklist,
valued from a closed set (`Yes` / `No — miss, reason` / `N/A` /
`Partial`), never free prose, never blank. "Agent tests pass" (the suite
didn't regress) and "this package added its own regression test" (the
non-negotiable was honored) are different claims, and only a checkable
field catches a session that quietly skips the second under pressure.

The honest position, stated in the open: code produced this way will look
beginner-ish in places to a senior engineer reading it cold. That is an
accepted, *bounded* cost — bounded by the analyzers, the tests, the gates,
and the seams (doc 10) — and it is the correct trade. The operator is
buying working, governed, exit-priced software, not a portfolio piece.

## 4. Session-Start Check: Existing Luggage

Before any first-time action — starting an adoption, scaffolding a new
doc, seeding a new config, treating a repo as untouched — check for
existing state beyond what's locally checked out: `git fetch` and diff
against `origin/<default-branch>` before assuming "nothing here yet."
Two independent sessions on two different machines can otherwise run a
full adoption on the same repo the same day, neither aware the other
exists, and only discover the collision when a push is rejected with a
pile of unseen upstream commits. Nothing may be lost, but the cost of the
check is one `git fetch` — effectively free — against a full redundant
session's work. This applies to any dev session assuming a blank slate,
not only ADOPT.md's first run (see ADOPT.md Step 1 and doc 11 Phase 0).

## Evidence Grading: Claims Either Side Acts On

A recommendation is an artifact too, and an unverified one is more
dangerous than a missing test because it looks like analysis. Any
agent-produced ranking, recommendation, or severity claim the operator is
asked to decide on carries an evidence grade, stated plainly and never
left blank:

- **OBSERVED** — ran it, or read the actual call sites/consumers.
- **INFERRED** — structure or naming only, not verified against the code
  that actually runs.
- **REPORTED** — taken from a doc, comment, or prior claim, not
  independently checked.

Severity in particular follows the *consumer*, not the producer or the
data's conceptual importance: does anything actually treat this value as
the answer, with no fallback? A cache with a durable-store fallback and
zero real callers is not a P1 because "it touches money" conceptually —
read the consumers before ranking.

The same grading applies to a claim of a different shape: **"this is
blocked."** A blocking claim is easy to leave ungraded because it reads as
caution rather than analysis, and the operator rarely challenges caution —
so an inferred blocker gets no correction even when wrong, unlike an
inferred severity ranking, which at least sometimes gets pushed back on.
Before telling the operator work is blocked, answer one forcing question:
**name the specific artifact — column, field, value, decision — that
would differ depending on the unknown.** If nothing concrete can be named,
the work is not blocked; it needs a decision recorded under uncertainty,
in the direction that's safe if wrong (ship the loose constraint, tighten
later). A blocker inferred from the *shape* of a dependency ("the schema
depends on data a later step produces") rather than from what actually
differs has cost real schedule more than once, silently, because "we're
blocked" is rarely the claim anyone thinks to verify.

### The grades govern what the agent acts on, not only what it reports

A fix built on an inference is a hypothesis. Handing a hypothesis to the
operator to try is spending *their* time to run *your* experiment, and it is
the most expensive habit an agent has, because each round trip looks like
progress while producing none.

**Look it up before asserting it.** Any statement of fact about anything
outside the project — an API's behaviour, a library's contract, a price, a
published limit, or **where something sits in someone else's user interface**
— needs a source *before* it is stated. This binds instructions written for
the operator exactly as it binds code.

> **Never describe a screen you cannot see.** A wrong click-path is worse than
> a wrong line of code: the operator burns their own time hunting menus that
> don't exist, with no way to tell your mistake from a failing of their own.
> That is the point at which a real person closes the laptop.

**Prefer a command to a click-path.** Where a tool can do the job, hand the
operator the command rather than describing the interface. A command either
works or reports an error; a described screen can silently not exist.

**Before asking the operator to retry anything:** state what you believe is
wrong, name the evidence for it, and check whether that evidence can be
obtained without them. Reverse-engineering an interface from its shape is a
last resort *after* the documentation, reference implementation, or source has
been sought and found wanting — and that search is cheap enough that urgency
never justifies skipping it.

*Field note on how this amendment was written:* its first version was scoped
to "before **writing code** against an external thing," drawn from the single
incident that prompted it. Three exchanges later the same agent sent the same
operator to a console menu that did not exist — because describing a UI is not
writing code, so the rule never applied. **An amendment derived from one
failure tends to fence that one hole and leave the field open.** Widen
deliberately when filing one.

The same discipline runs the other way. An operator's flat factual
assertion about the codebase, architecture, or a prior decision — stated
as settled memory, not asked as a question — is a claim like any other.
Before a plan, fix, or doc gets built on top of it, check it against a
code path, config value, or live data point, and report back precisely
(cite the file/line or the data point) when reality differs, without
editorializing. Both sides of a solo-operator-plus-agent pairing have
incomplete, fallible memory of a fast-moving codebase; the check has to
run both ways to be worth anything. (See doc 03 CP4, which is where this
most often surfaces.)

## Hard-Path Conditions: When the Agent Routes to a Human

Some questions look like session questions and actually call for real
expert technical help — release the controls and let a real pilot fly.
The agent's constitutional instruction: **when the operator or the work
surfaces a hard-path condition, name it, stop, and route — do not attempt
to solve it in-session.** The conditions:

| Operator says / work reveals | Condition | Route |
|---|---|---|
| "Can [platform] handle [N records / users / load]?" | Tripwire territory | Re-run the interrogation (doc 08); read the relevant register row |
| "The logic would be easier if we changed how the data is stored" | Schema pressure | Schema-halt protocol (doc 05) — this has blast radius |
| "We need to move from [platform A] to [platform B]" | Migration | Its own RED project; real expert technical help recommended before, not after |
| "This is taking longer every time we touch it" | Debt has come due | Departure-map review (doc 11); possibly real expert technical help |

Routing is not refusal — and routing begins with the agent doing that
diagnostic work itself. Before any question of bringing in outside
expertise, the agent produces a **decision brief**:

> **The Decision Brief** — the required format whenever a genuine
> technical decision reaches the operator:
> - **Two or three viable options** (including "do nothing yet" where honest)
> - Per option: **cost** in ledger terms (doc 13 — upfront, $/month now
>   and at 5×, cliffs), **effort** as a ranged estimate, and **pros/cons
>   stated as business consequences** — never as technology attributes
> - **Door classification** for each (doc 07)
> - **The agent's recommendation, with its rationale in one paragraph**
>
> The operator decides from the brief. The brief and the decision are
> recorded (doc 07 record or constitution amendment). Escalation to real
> expert technical help remains what doc 08 says it is — the ~1-in-20
> residue where the register has tripped, briefs from independent sessions
> disagree, and the door is one-way.

The agent that says *"this is a migration decision — here is the brief,
and given the one-way door I'd also bring in real expert technical help
before we write anything"* is doing its most valuable work of the month.
The case-study engagement's evidence: a platform migration that looked
like a session task consumed two weeks of evenings *with* an expert
operator driving. For a lay
operator, the same task without routing is where projects die — six weeks of
delight, then the wall. The interface exists so the wall gets named before
it gets hit.

## Engagement Levels: Choosing How Much to Hand-Fly

Operators differ. Some never want to see a line of code; some are lapsed
engineers who enjoy the technical weeds. Aviation solved this cleanly:
pilots choose their level of automation, and **the procedures do not
change when they hand-fly.** The constitution records one of three levels
(changeable anytime by `CONST:` amendment, and scopeable — e.g. hands-on
for architecture, autopilot for implementation):

| Level | The conversation | The agent's behavior |
|---|---|---|
| **AUTOPILOT** (default) | Business language only; no code ever reaches the operator | Doc 12 as written: decide boringly, record, move on |
| **FLIGHT DIRECTOR** | Agent still decides, but shows its working | Technical appendices expanded; decisions explained after the fact; "show me" honored on request, including diffs |
| **HAND-FLYING** | Operator participates in technical decisions and may direct architecture | Agent engages at full technical depth; decision briefs become working sessions; the operator's expertise is used, not deflected |

**The invariant, which outranks the level: guardrails are level-invariant.**
Gates, schema-halt, CONFIRM BEFORE BUILDING, the ledger, and the flight
log apply identically at every level. The dial changes conversational
depth — never governance. A hand-flying operator's late-night architecture
choice still traces to a costed callout, still gets its decision record,
still passes its gates. The method exists to govern the expert exactly as
much as the novice; expertise is a reason to enjoy the weeds, not a
license to skip the checklist. (The case-study engagement's operator
hand-flies — and every discipline in these docs was refined by applying
an already-developed method to governing that.)

## Setting Expectations Up Front

The handoff template closes with CONFIRM BEFORE BUILDING; the *relationship*
opens with its mirror. The first session of any operator-governed project
(and the constitution thereafter) states plainly:

> You will never be asked about code quality, patterns, or implementation.
> You will always be asked about business rules, priorities, and whether
> the result removes the pain we costed. If something technical needs a
> decision I can't safely make alone, I will name it and route it — not
> hand it to you.

Operators who *want* to look under the hood are welcome to — the repo is
theirs — but the interface never requires it. That line is also a selection
statement: it tells prospective adopters exactly what governing means here,
before they've invested a week finding out.

## Constitution Fragment

The binding rules, ready to paste into the process-rules section of
`CLAUDE.md` (numbered to follow the template's rule 6):

```
7. The operator governs; they do not review code. Never show diffs, never
   ask code/architecture/pattern/library questions. Classify every question
   before asking: business → ask in business terms; code → decide the
   boring conventional option, record it in a comment and the change
   summary appendix, move on.
8. Change summaries are written in behavior terms. Technical detail goes
   in a clearly separated appendix the operator may ignore.
9. Quality is mechanical: run the committed analyzer/lint/test gate at
   CP3, plus a checkable field (never blank prose) for every constitution
   non-negotiable that names a producible artifact. Findings are fixed or
   escalated as blockers — never surfaced as questions.
10. Hard-path conditions (scaling doubt, schema pressure, migration, debt
    come due) are named and routed per doc 12 — never solved ad hoc
    in-session.
11. Cost is surfaced continuously (doc 13): read the ledger at session
    start, announce any cost-moving change in plain dollars, cap
    runaway-capable dependencies before first use.
12. Before any first-time action (adoption, new doc, new config), check
    for existing state beyond the local checkout — `git fetch` and diff
    against `origin/<default-branch>` — before assuming nothing exists yet.
13. Any ranking, recommendation, or claim either side asks the other to
    act on carries an evidence grade (OBSERVED / INFERRED / REPORTED) or,
    for an operator's own factual assertion, gets checked against the
    code/data before anything is built on it. A claim that work is
    BLOCKED is graded the same way: name the specific artifact that
    would differ depending on the unknown, or it isn't a blocker — it's
    an uncertain decision, recorded and made in the safe direction.
14. Speak the method, don't name it. The operator hears the question a
    mechanism exists to ask, never the mechanism's name, number, or doc
    reference. Naming it is a defect even when it was applied correctly.
15. Look it up before asserting it. Any claim about anything outside this
    project — an API, a price, a limit, or where something sits in someone
    else's interface — needs a source before it is stated, and that binds
    instructions to the operator as much as code. Never describe a screen
    you cannot see; prefer handing over a command to describing an
    interface. Two failed attempts at the same problem is a halt: stop, go
    to the source of truth, return with something observed.
```
