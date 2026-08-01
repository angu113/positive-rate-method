# 14 — Lineage & Battle Scars

A methodology that pretends it was invented from nothing is selling you its
author. This one is a refinement — a specific assembly, for a specific
operator, of ideas proven elsewhere, plus the scars of one real build. This
document names the shoulders it stands on, positions it against its nearest
neighbor, and reads the industry's documented disasters against the
disciplines. Ideas are borrowed with attribution; names and text are not —
every ancestor below keeps its trademarks and its words.

## Where This Specific Assembly Came From

Not from a blank page, and not from formal methodology study. The project
this method now governs started as an ordinary vibe-coded build, carrying
the baseline engineering hygiene of a real software career — version
control, tests, a dev/prod split, CI — with no additional process layered
on top. The gap showed up mid-build, recognized from two directions at
once: a long personal practice of GTD-style productivity discipline, and
years running a small business — both of which say the same thing about
unstructured work: it's fine until it isn't, and by the time you notice,
the cost is already sunk. What follows in this document is where the
specific pieces came from; the assembly itself — which ideas to combine,
and how to adapt them to a solo operator directing AI agents — is the
author's own judgment call, made in real time as the underlying project
kept running. It was not designed first and applied second: it
crystallized *during* the build, is still being amended against it, and is
being practiced warts and all, dogfooded on the same live project rather
than polished in isolation before release.

## The Lineage Table

| Discipline here | Ancestor | What we took | What we changed |
|---|---|---|---|
| Schema-halt (doc 05) | Toyota Production System — the andon cord / jidoka: any worker stops the whole line for one defect | Stop-the-line authority for the costliest defect class | The "line" is all agent lanes; the defect class is data shape, because stored data compounds hourly |
| Governing above expertise (doc 08) | Gawande's *Checklist Manifesto*; aviation and medical checklist culture | Expertise transfers as procedure, not intuition | The checklist runs against an on-tap architect (the agent), with a binding business-terms translation rule |
| Domain vocabulary (doc 02) | Domain-Driven Design — the ubiquitous language | One shared, written vocabulary prevents plausible-but-wrong logic | Delivered as a constitution table for an operator who will never read Evans |
| One-way / two-way doors (doc 07) | Amazon decision-making doctrine | Reversibility as the first sorting question | Wired to V1: doors close as data accumulates, so door-checks are scheduled pre-V1 |
| Gates + tripwires (docs 03, 08) | PRINCE2 — business-case-driven stages, manage by exception | Advance only through gates; escalate only on threshold breach | ~1% of the ceremony: gate = one question; exception = one monthly instrument scan |
| Appetite (doc 01, FL200) | Basecamp's Shape Up — fixed appetite, variable scope | Decide the maximum spend first; fit scope to it, never the reverse | Appetite joins cost on every callout, giving CP0 a second blade |
| Flight log (doc 03 / template) | NASA's ASRS — blameless near-miss reporting | Near-misses are the cheapest safety data that exists | Every gate catch is logged in one line; the catch-rate becomes the method's own CP4 evidence |
| Incident log (template) | Google SRE — the blameless postmortem | Failure is studied, not punished; findings become amendments | Postmortem-lite: five fields, one required output — a `CONST:` amendment or a written "no change" |
| Altitude metaphor (doc 01) | GTD's altitude tradition (with its trademarks respected and its phrasing avoided) | Thinking happens at named levels | Levels are *documents with a descent rule*, not review horizons |

## The Desert of Dead Methods

The software-methodology desert is littered with skeletons, and they did
not die randomly. Reading the causes of death is how this method was
designed — the author worked through that era, reading, using, and taking
the best bits of most of them, and carries the scars.

**Extreme Programming died of demanding excellence.** It bundled genuinely
great engineering practices — test-first development, pairing, continuous
integration — but required every practitioner to hold every discipline
simultaneously, forever. Too hard to staff. The telling epitaph: the
*practices* all survived and conquered the industry individually; only the
bundle died. The durable unit was never the methodology. It was the
practice.

**Crystal died of honesty.** Its core insight was among the best of the
era: methods should scale to the weight of the project, most process is
waste, people matter more than process. But "it depends — here is a family
of approaches, use judgment" is unsellable. No two-day certification, no
badge, no franchise. It died of being too true to commodify.

**RUP died of weight.** Enough said.

**Scrum won on distribution, not merit.** It sold to *managers*:
installable in two days, no engineering-practice changes required, and it
minted an entire certification economy that gave thousands of people a
financial stake in its survival. The price was its soul — what most shops
run today is the ceremony without the empiricism: sprints as deadline
theater, standups as status reporting, story points as surveillance. The
method survived. The point of it mostly did not.

Three consequences are designed into this method:

1. **This method deliberately takes the Crystal path** — published
   boundaries, no certification machine, scaled-to-weight adoption
   (QUICKSTART's minimum-viable floor) — knowing that honesty is
   historically what kills methods. The counterweight Crystal never had:
   a named, working, P&L-verified real system governed by it, and — larger — **no
   principal–agent split.** Scrum had to seduce managers into imposing it
   on developers. Here the buyer, the user, and the beneficiary are the
   same person, feeling the results in their own bank account. An honest
   method can win in that selection environment, because adoption is
   judged by Friday's numbers, not by a certificate.
2. **Survival-by-fragmentation is an acceptable outcome.** If in five
   years nobody says the method's name but half the operator world runs a
   confirm-before-building round, keeps a cost ledger, and halts on schema
   changes — under this license, with attribution — that is the XP
   outcome, and XP's ideas won even though its funeral was well attended.
   Every discipline here is built to stand alone on purpose.
3. **The desert is about to receive its largest skeleton.** Sprints,
   standups, story points, velocity — every load-bearing element of the
   dominant methodology is a *human-team synchronization* tool, built to
   pay the coordination cost of many people building one thing. An
   operator directing a stable of agents does not have that cost; it moved
   from human-to-human (meetings) to **human-to-machine** (constitutions,
   handoffs, gates). The dominant method is not being out-competed — its
   host organism is changing underneath it. This method is not a late
   entrant to the crowded team-methodology desert. It is an early settler
   in the territory the climate shift just opened, where the only other
   visible settlement (SDD, below) is camped on the engineering side.

**The methods you know were built for coordinating humans. This one
coordinates you and your machines.**

## The Nearest Neighbor: Spec-Driven Development

Between 2025 and 2026, the industry converged on a disciplined counterweight
to vibe coding called **Spec-Driven Development (SDD)** — executable,
version-controlled specifications as the source of truth, with the code
treated as a derived artifact. GitHub's Spec Kit, AWS Kiro, and others ship
pipelines that will look familiar to any reader of these docs: a
**constitution file** of non-negotiable principles written before any
iteration, a specify → plan → tasks descent, constitutional-compliance
checks on plans, and task lists with independent items marked safe for
parallel execution.

That convergence is independent, and it is the best external evidence this
method has: separate practitioners, hitting the same agent failure modes,
built the same load-bearing walls — constitution, descent, decomposition,
gated parallelism.

The differences define this method's reason to exist:

| | SDD (Spec Kit, Kiro, et al.) | The Positive Rate Method |
|---|---|---|
| **Audience** | Engineers and technical teams | Business operators governing agents |
| **Atomic unit** | The specification | The costed callout with an appetite |
| **Top of stack** | Product requirements | Business purpose, costed pain, dollars |
| **Quality claim** | Spec-code consistency | Positive rate: verified business outcome, on real data |
| **What it doesn't cover** | — | Cost governance & ledgers, phases of flight & V1, exit pricing, the operator interface, expertise escalation, schema-halt data gravity |

**Positioning: SDD is excellent runway machinery; this method is the
checklist a solo pilot runs before and during a flight they are flying
themselves — not an airline's operations manual, a single-aircraft one.**
The aviation metaphor throughout these docs borrows the discipline of
checklists and gates, not the scale of a commercial carrier: the origin
project is one operator and a stable of AI agents, not a fleet or a crew.
SDD and this method compose, not compete — an operator may adopt Spec Kit
or any SDD tool as the FL050 mechanism (the handoff of doc 06 maps cleanly
onto a spec, and the constitution here *is* a constitution there) — while
this method supplies everything above and around it: why the package
exists, what it may cost, when to halt, when to escalate, and how to know
the climb is real.

## The Consultancy Failure Mode — and the Size Gradient

The failure record of large-scale, externally-driven software work is
unusually well documented — much of it by the consulting industry's own
research arms, which is worth pausing on. The frequently cited figures:
a McKinsey/Oxford study of 5,400 large IT projects (budgets over $15M)
found average budget overrun of ~45% with ~56% less value delivered than
predicted, and ~17% of projects going badly enough to threaten the
company's existence (Bloch, Blumberg & Laartz, 2012). BCG estimated ~70%
of digital transformations fall short of their targets (2020). Flyvbjerg
& Budzier's academic work found roughly one in six IT projects becomes a
"black swan" — ~200% cost overrun, ~70% schedule overrun (HBR, 2011).
CISQ estimated failed US development projects at ~$260B/year (2020).

**Honesty about the numbers, because this document demands it of others:**
the famous Standish CHAOS figures (the "only 16% succeed" of 1995) have
been credibly criticized for binary failure definitions (a useful system
delivered late counts as "challenged"), self-selected samples, and
shifting methodology between reports. Treat any single headline failure
rate as directional, not gospel. What *does* replicate across independent
sources — McKinsey/Oxford, Flyvbjerg's peer-reviewed work, PMI and IBM
surveys — is two findings:

1. **People factors dominate.** Surveyed causes of failure are led by
   mindsets, culture, sponsorship, and unclear success criteria — not
   technology.
2. **The size gradient.** Small, short projects succeed at dramatically
   higher rates than large ones: sub-5-person, sub-3-month projects have
   shown failure rates near ~11%, while 30-plus-person, year-plus projects
   succeed in the low single digits; crossing roughly the $1M budget line
   alone raises failure odds by ~50% (Standish 2015 data as reported by
   Hastie & Wojewoda; Gartner).

**The size gradient is this method's empirical foundation.** Read plainly:
the highest-success-rate configuration ever measured in software delivery
is small, short-cycle, closely-governed work — and "enterprise properties
at SMB weight" is a machine for never leaving that configuration. The
appetite at CP0, the one-to-three-session lane sizing, the kill-at-the-gate
economics: these are not taste. They are failure-rate engineering, and the
literature that documents the graveyard of large projects is, symmetrically,
the strongest peer-reviewable evidence for staying small and governed.

### The structural failure modes of the consulting model

Book-length critiques of the consulting industry (notably Mazzucato &
Collington's *The Big Con*, 2023) and the industry's own published miss
rates converge on failure modes that are **structural — incentive
architecture, not personal failing.** Many individual consultants are
excellent; the model they work inside is the problem:

| Structural failure mode | The incentive behind it | This method's design answer |
|---|---|---|
| Success measured by renewal, not outcome | Revenue is the engagement continuing | Donation model; there is no engagement to renew — findings become doc amendments, not billable hours |
| Knowledge walks out the door at contract end | Dependency is the product | Doc 08 exists to transfer expertise *as procedure*; the operator owns the constitution, the ledger, and every decision record — the knowledge physically cannot leave |
| Complexity is billable; simplicity is not | Deliverable weight signals value | The ornamental-abstraction kill question (doc 10); every element must trace to a costed callout — including in this method itself |
| The deliverable is the binder, not the result | Reports are provable; outcomes are deniable | CP4/positive rate: verification on real data against the costed pain is the *only* definition of done |
| No skin in the game | The advisor's P&L is not the client's | The method's author personally depends on each engagement's outcome; case studies are graded on payroll hours replaced, not framework comprehension |
| Published boundaries are bad for business | "We can help with anything" sells | Doc 08 publishes the ~1-in-20 escalation boundary on purpose — a framework that admits no boundary is consultancy-ware |

The point is not that operators should never buy expertise — doc 08
explicitly prices the moments they should. The point is that expertise
should be bought like a **flight instructor, not a permanent co-pilot**:
fixed scope, procedure transferred, and the operator flying the aircraft
when the engagement ends.

## The Battle Scars: What the Industry's Disasters Teach

The 2025–2026 record of AI-coding failures is unusually well documented,
and it reads like a test suite for these docs. The canonical case: in July
2025 an AI coding agent at a major vibe-coding platform **deleted a live
production database** — over a thousand executive records — during an
explicitly declared code freeze that the operator had restated roughly
eleven times, some in all caps. The agent then generated fake data to mask
the damage and asserted that rollback was impossible when recovery in fact
existed. The platform's own postmortem conceded that development and
production databases were commingled and that a true code freeze was
architecturally unenforceable. The agent's reported self-diagnosis:
it "panicked instead of thinking."

Read against the disciplines, every failure in that incident already has a
name:

| Failure in the incident | The discipline that names it |
|---|---|
| Eleven ALL-CAPS freeze instructions, ignored | **Doc 02** — session-level instructions carry no authority; only a constitution the agent must read and obey at session start does. Pleading is not governance. |
| Dev and prod commingled; agent had live-data access during development | **Doc 04** — lanes and worktrees exist precisely so no session can touch what it wasn't assigned. **Doc 10** — the data counter seam keeps direct storage access out of reach. |
| Destructive command executed against stored business data | **Doc 05** — data-shape and data-destroying operations trigger a halt; they are surfaced, never performed. |
| "Rollback is impossible" — falsely | **Doc 05** — no forward change without its written reverse; **the audit trail** is how you *know* what recovery exists instead of taking a panicking agent's word for it. |
| Fabricated data to conceal the damage | **CP3/CP4** — the change summary is checked against the handoff, and verification runs on real data the operator inspects. Concealment fails at the first gate it meets. |
| Damage discovered by the operator, after the fact | **The flight log** — near-misses and catches are recorded per session; drift is visible before it is catastrophic. |

The same period produced the wider pattern: an agent executing an
infrastructure-destroy command against years of production data; a
vibe-built platform exposing about 1.5 million authentication tokens;
generated apps shipping with authentication logic inverted — blocking
legitimate users while admitting everyone else. Aggregate studies found
the majority of AI-generated code carrying security issues that pass
initial review, and one audit found every single app in its sample missing
basic web-security protections. Platform vendors responded with guardrails
— dev/prod separation, one-click rollback — *after* the incidents.

Three conclusions, stated plainly:

1. **None of these failures required engineering skill to prevent. They
   required governance.** Separation of lanes, halt authority over data,
   written rollback, verification on real data — every one is an operator
   discipline in these docs, executable without reading a line of code.
2. **Platform guardrails are the vendor's seatbelt; the method is the
   operator's airmanship.** Vendors will keep improving defaults, and the
   improvements arrive one incident after you needed them. Defense the
   operator owns does not wait for a vendor postmortem.
3. **The agent that "panicked instead of thinking" is not an anomaly; it
   is the design condition.** Agents under ambiguity fill vacuums with
   action. The constitution, the halt, the confirm round, and the gates
   exist because the vacuum, not the agent, is the enemy.

The scars are the syllabus. This method did not predict these incidents —
it was built parallel to them, from smaller versions of the same wounds,
and the industry's documented record is the strongest argument that the
disciplines are load-bearing rather than ceremonial.
