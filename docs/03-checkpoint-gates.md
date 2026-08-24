# 03 — Checkpoint Gates (CP0–CP6)

Gates are the operator's control surface. The agent produces; the gates decide
what advances. A work package occupies exactly one gate state at a time, and
**no gate may be skipped** — including for "trivial" changes, because triviality
is precisely the judgment AI-assisted work gets wrong most often.

## The Gates

### CP0 — Callout Confirmed
The package traces to a written FL200 callout with a cost and a success
measure. *Kills:* pet features, agent-suggested scope, "while we're in there."

**Gatekeeper question:** which callout, and what does done cost/save?

### CP1 — Design Slotted
The package is placed in the FL100 module map: which module owns it, what
data it touches, whether it crosses a boundary. **Lane classification happens
here** (see doc 04) — and this is where a package touching schema gets flagged
before it can do damage.

**Gatekeeper question:** whose data is this, and what lane is it?

### CP2 — Handoff Written
The structured handoff prompt exists (doc 06), ending in **CONFIRM BEFORE
BUILDING**. The agent has restated the task, surfaced its assumptions, and the
operator has corrected them. No code exists yet.

**Gatekeeper question:** did the agent's restatement match my intent?

### CP3 — Build Complete (In-Lane)
The agent reports done inside its worktree. Code compiles, agent-run tests
pass, the agent has produced a change summary. Nothing has left the lane.

**Gatekeeper question:** does the change summary describe only what CP2 authorized?

### CP4 — Operator Verification (the "Positive Rate" check)
The operator exercises the change against the callout's success measure —
real data, real workflow, not the agent's demo path. This is the gate that
cannot be delegated to the machine, because it tests the *business claim*,
not the code.

**Gatekeeper question:** does this actually remove the pain we costed at CP0?

*The aviation name is exact: after liftoff, the crew confirms "positive
rate" — actual climb, read off the instruments, not felt in the seat —
before committing the configuration ("gear up"). CP4 is that call: real
data, real workflow, the instrument reading that authorizes commitment.*

Verification at this gate runs in both directions. An operator's flat
factual assertion about the codebase, architecture, or a prior decision —
stated as settled memory, not asked as a question — is a claim like any
other, and gets checked against a code path, config value, or live data
point before a plan, fix, or doc is built on top of it (see doc 12's
evidence-grading discipline). Both sides of a solo-operator-plus-agent
pairing have incomplete memory of a fast-moving codebase; the check has
to run both ways to be worth anything.

### CP5 — Integration
Merge to mainline per the lane rules (doc 04): locks respected, manifest
updated, constitution amendments (if any) committed with `CONST:` prefix.

**Gatekeeper question:** is any other lane touching what I'm about to merge?

### CP6 — Shipped & Audited
Deployed through the standard release path; the change appears in the audit
record; rollback path known. Only now is the callout marked served.

**Gatekeeper question:** if this breaks Monday morning, do I know how to get back?

## Authorization Precondition (CP5–CP6)

Both gates assume the environment is already authorized to perform their
own actions — commit identity configured, push credentials live, deploy
rights granted. Confirm that *before* work reaches the gate, not when it's
discovered at the gate with otherwise-shippable work sitting behind it. An
intentionally un-authorized environment (an isolated dev box, a read-only
replica) is a valid, even desirable configuration — not a defect to route
around. When it's found for the first time at CP5/CP6, it's a business
question ("whose name goes on this work, and should this environment even
be authorized to push?"), escalated per doc 12, never defaulted by
inventing an author.

## Halt Conditions (any gate)

Immediate stop, package returns to CP1:
- The agent proposes or performs a **data-shape change** not declared at CP1
  → this escalates to the schema-halt protocol (doc 05), stopping *all* lanes.
- The agent makes an FL200-level decision (invents a business rule).
- The change summary at CP3 includes work not in the CP2 handoff.
- **Two failed attempts at the same problem.** Not a third guess: stop, go to
  the source of truth — documentation, reference implementation, actual source
  — and return with an answer that is observed rather than inferred. Each
  guessed fix handed to the operator to test spends their time running the
  agent's experiment, and looks like progress while producing none (doc 12).

## Why Seven Gates Isn't Bureaucracy

For a one-person operation, each gate is a question that takes between ten
seconds (CP0, CP1 for a routine package) and an hour (CP4 for a money-touching
one). The gates don't slow the work — they replace the *rework*, which in
ungated AI-assisted projects routinely consumes more time than the original
build. The gates are also what make **parallel** work safe at all: without
CP1 lane classification and CP5 lock discipline, running three agent sessions
at once is just three ways to corrupt one codebase.

## The Flight Log

Every session writes one line — package, lane, gate reached, estimate vs.
actual, what the gates caught (template:
[`/templates/flight-log.md`](../templates/flight-log.md)). Blameless by
charter: a catch is the method succeeding, and near-misses are the cheapest
safety data that exists (doc 14). The monthly rollup does two jobs no other
artifact can: it **measures** the compounding claim (median hours per
feature, trending down) instead of asserting it, and it turns the gates'
catch-rate into the method's own positive-rate evidence. Three catches of
the same type in a month is an amendment, filed.
