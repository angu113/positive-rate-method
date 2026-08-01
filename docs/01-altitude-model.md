# 01 — The Altitude Model

The core claim of the method: **software quality is determined above the code,
and AI has made this more true, not less.** An AI agent removes the cost of
writing code. It does not remove the cost of deciding what code to write. If
you don't supply the decisions, the agent will invent them — plausibly and
silently.

The model borrows aviation flight levels because operators intuitively get the
metaphor: you don't descend through an altitude you haven't been cleared for.

## The Levels

### FL400 — Purpose
One paragraph. Why the business exists. This is not decoration: it is the
tiebreaker for every downstream disagreement. When two designs are both
"fine," the one that serves the purpose wins.

*Written once. Revised almost never.*

### FL300 — Vision & Values
- **Vision:** what the operation looks like when the software is fully working.
  Written as a day-in-the-life narrative, not a feature list.
- **Values:** the non-negotiables. Examples from practice: *every document
  gets an immutable audit record*, *no employee needs admin rights to run our
  software*, *the customer's phone number is a first-class identity*.

Values become **standing constraints** that live in the project constitution
(see doc 02) and are enforced at every gate.

### FL200 — Business Callouts
The named, costed problems. Each callout gets:
- A name ("Front office retypes every quote into three systems")
- A cost estimate in hours/week or dollars/month
- An owner (who feels this pain)
- A success measure ("quote-to-invoice with zero re-entry")
- An **appetite** — the most this pain is worth spending to fix, in time
  and dollars, decided *before* descent. Scope varies to fit the appetite,
  never the reverse (lineage: Shape Up — see doc 14).

**This is the level that justifies the project.** If you cannot cost the
callout, you are building a hobby, and you should know that before
descending. (That's not a dead end — see QUICKSTART Door C, where the
appetite substitutes for the cost.)

### FL100 — System Design
Modules, boundaries, and — critically — **data ownership**. For each module:
what data does it own, what does it merely read, what identifiers cross its
boundary. This level exists mostly to make the schema-halt protocol (doc 05)
enforceable: you cannot detect a dangerous schema change if nobody wrote down
who owns the schema.

The operator does not need to produce UML. A table of modules × owned data ×
shared identifiers is sufficient and is the single highest-leverage document
in the whole method.

### FL050 — Work Packages
Units of work sized for one AI-agent session or one worktree lane. Each
package is lane-classified (doc 04), gets a handoff prompt (doc 06), and moves
through the CP0–CP6 gates (doc 03).

### RUNWAY — Code
Shipped, versioned, audited. Code that hasn't passed CP6 is at altitude, not
on the runway, no matter how finished it looks in a demo.

## The Descent Rule

> **You may only descend one level at a time, and only when the level above
> exists in writing.**

Corollaries:
1. **Ascent is always permitted.** Discovering mid-build that a callout was
   mis-costed is a success of the method, not a failure. Climb, fix, descend again.
2. **The agent never descends for you.** If an AI session starts making FL200
   decisions (inventing business rules) while working an FL050 package, that
   is a halt condition.
3. **Levels are documents, not meetings.** Each level is a file in the repo.
   If it isn't written down, it doesn't exist.

## The Second Axis: Phase of Flight

Altitude is *abstraction* — where a decision lives. **Phase of flight is
*maturity*** — how far down the runway the project already is, and how much
decision luggage it has accumulated. Every method activity scales with
phase, so the phase is established before anything else (the Phase Check,
doc 11).

| Phase | The project | Luggage | What the method weighs here |
|-------|------------|---------|------------------------------|
| **APRON** | Nothing built. Idea, pain, maybe a chat log with an AI. | None | Almost nothing: FL400/FL300 in an hour, one callout, thin constitution. Ledger has zero rows. |
| **TAXI** | First choices being made — stack, storage, platform trials. No production data. | Light, all reversible | Doc 07 records at decision time (cheapest they will ever be), first ledger rows, constitution thickening. |
| **TAKEOFF ROLL** | Actively building the first real capability. Committed, accelerating. | Accumulating fast | Full handoff + gate discipline. **Watch for V1.** |
| **CLIMB** | First callouts served; real use beginning; capabilities stacking. | Real | Lanes and parallelism start paying; tripwire register goes live; schema-halt armed for real. |
| **CRUISE** | Steady state. The business runs on it. New packages are increments. | Full hold | Monthly instrument scan (tripwires + ledger); marginal features converge on handoff-cost; adoption archaeology (doc 11) if governance arrived late. |
| **GO-AROUND** | A component's approach abandoned — migration, platform pivot, rework. | Repacking mid-air | A RED project with doc 07's exit paragraph as its flight plan. Not a failure: a go-around is the *procedure for* not landing badly. |

### V1 — Decision Speed

On the takeoff roll there is a speed, **V1**, past which aborting is more
dangerous than continuing: whatever happens next, you fly. A software
project has an exact equivalent:

> **V1 is the first moment real business data is stored, or a real document
> reaches a customer.**

(And just past V1 comes the moment the method's vocabulary keeps for the
joy of it: **rotate** — the deliberate input that produces flight. The
method is named for the call that comes *after*: positive rate, the climb
confirmed on instruments, the reading that authorizes commitment.)

Before V1, everything is cheap: platforms are trials, schemas are
sketches, aborting costs a weekend. After V1, data has gravity — records
accumulate, documents are in customers' hands, and every one-way door (doc
07) begins swinging shut. The method's V1 rules:

1. **Know when you cross it.** Crossing V1 is announced, dated, and logged
   — never discovered later.
2. **Pre-V1 is when foundation decisions are cheapest.** Anything doc 07
   would classify one-way (data platform, identifier scheme, document
   numbering) gets its interrogation *before* the roll, at the holding
   point, while aborting still costs nothing.
3. **Post-V1, you fly the airplane.** Problems are handled by procedure —
   gates, halts, go-arounds — not by starting over. "Let's just rebuild it"
   after V1 is a go-around decision with a priced exit, not a fresh apron.

### Building the Plane While Flying It

Every operator who reaches CLIMB with the business already using the system
knows the feeling: **you are building and fixing the plane while flying
it.** There is no hangar. No maintenance window. No "ship when it's done" —
customers are being quoted on the system that is mid-change. This is not a
temporary embarrassment to be engineered away; post-V1, it is the permanent
operating condition of operator-built software.

Aviation's answer to working on an aircraft you cannot land is the method's
answer: **not skill and nerve — procedure.** You never touch the wing spar
in flight without stopping everything else (schema-halt, doc 05). You
change one system at a time while the others hold the plane up (lanes, doc
04). Every change is checked before, during, and after (gates, doc 03).
A failing approach is abandoned by written procedure, not ridden down
(go-around, doc 07). The meme version of building-the-plane-in-flight is
chaos and duct tape. The method's claim is that it is a *governable
condition* — and every discipline in these docs is one item on that
flight's checklist.

## Two Ways to Fail

Aviation distinguishes two failure modes that feel nothing alike and are
prevented by nothing alike. So does this method.

**Explode** — a single catastrophic action, all at once, usually
irreversible: the destructive command, the schema change applied live, the
wrong action against the wrong environment. It rarely announces itself as
a bad idea in the moment, even to someone skilled — the disaster doc 14
cites was built by engineers, not amateurs. This is what schema-halt (doc
05), the gates (doc 03), and the tripwire register (doc 08) exist to
catch: procedure that holds regardless of who's flying, because the
moment before an explosion looks exactly like every other moment.

**Stall** — no single bad moment, just a slow loss of lift: scope creep
nobody named, a cost that crept up unwatched, a callout that quietly
stopped being the real priority, a project that keeps "succeeding" session
after session while the actual business result drifts away from what was
asked. This is what the phase-of-flight model, the appetite (FL200), and
the cost ledger (doc 13) are watching for — not a crash, a loss of climb.
It is also why the method is named for a positive-rate check and not a
collision-avoidance system: the everyday risk is quietly not climbing, not
a dramatic hit.

**Neither personal skill nor guardrails is sufficient alone against both.**
An operator's own technical judgment is usually the faster, cheaper defense
against stall — an experienced eye feels "this doesn't sit right" long
before any written gate would trip. That same judgment is a weak defense
against explode, precisely because catastrophic single actions don't feel
wrong in the moment even to someone skilled. Guardrails are the reverse:
built to catch explode regardless of who's flying, but a clumsy, slow tool
against the kind of drift a skilled operator would simply notice first.

> **The honest claim is not "the method prevents failure." It is: bring
> real technical discipline for the failures that announce themselves
> gradually, and install real procedure for the ones that don't announce
> themselves at all — because neither substitutes for the other, and a
> track record with no incidents yet proves the combination hasn't been
> tested by its worst day, not that either ingredient alone would have
> been enough.**

## Why This Beats Bottom-Up Prompting

A prompt is copyable. The written stack of FL400→FL050 documents for *your*
business is not — and it compounds. Every new work package is cheaper than the
last because the constitution, callouts, and design already exist. The
methodology's economic claim: **the marginal cost of feature N approaches the
cost of writing its handoff prompt.** That's how a one-person side effort
replaces a full-time role.
