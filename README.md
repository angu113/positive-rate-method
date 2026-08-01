# The Positive Rate Method

*After liftoff, before anything is committed, the crew confirms "positive
rate" — the climb is real, read off the instruments, not felt in the seat.
Only then: gear up. This method is that call, applied to software: verified
on real data, in business numbers, before you commit. Confirmed on the
instruments, not felt in the seat.*

**Instrumented AI-assisted development — for anyone governing an AI coding agent by dollars, by time, or both.**

This did not start as a methodology. It started as an ordinary vibe-coded build, carried on the baseline
engineering hygiene its author already had from a real software career — version control, tests, a
dev/prod split, CI — with no formal process layered on top. The gap showed up mid-build, recognized from
two directions at once: a long personal practice of GTD-style productivity discipline, and years running a
small business — both of which say the same thing about unstructured work: it's fine until it isn't, and
by the time you notice, the cost is already sunk. The Positive Rate Method is that recognition, made
specific to a solo operator directing AI agents — assembled from existing, proven ideas (see
[doc 14](docs/14-lineage-and-battle-scars.md) for the specific lineage), not invented from a blank page,
and crystallized *during* the build it now governs, not before it. **The method itself, and the judgment
of how/why/what to apply it, is the author's own work as a software engineer and architect. The specific
software it was first applied to is a separate question with its own considerations, addressed in the
case study, not asserted here.**

It is now being run, warts and all, on that same project — a live, CRUISE-phase system with real users and
real production history — amended in the open as the dogfooding turns up gaps. See the
[case study](case-study/consulting-engagement.md) for the honest, unvarnished account, and
[CONTRIBUTING](CONTRIBUTING.md) for how findings become amendments.

> **The realistic pitch: this is for anyone who wants their AI-assisted build instrumented — measured and
> governed against dollars if you run a small business, or against your own time and attention if you're
> building for yourself — plus a set of guardrails solid enough that someone else can safely work on the
> same project alongside you or the agent. It is not a promise of enterprise polish, proven savings, or a
> substitute for judgment; it is a way to see what a project actually costs and catches, as you go.**

> **Status:** v0.13, amended continuously against real use on a live project — not a finished, theory-first
> spec. See the [case study](case-study/consulting-engagement.md) for exactly what real use has and hasn't
> proven so far.

---

## The Problem

Every "learn AI coding" resource is bottom-up: prompts, tricks, snippets. That
teaches you to generate code. It does not teach you to *govern* a software project —
to know what to build, when to stop the machine, and how to keep a codebase
coherent over 18 months when you are not a software engineer and your day job is
running a business.

The Positive Rate Method is top-down. It starts where a business owner actually starts:
purpose. It ends at running code. Every layer in between is a deliberate descent
with a defined checkpoint.

## The Altitude Model

```
  FL400  PURPOSE          Why does this business exist?
  FL300  VISION / VALUES  What does "working" look like? What won't we compromise?
  FL200  BUSINESS CALLOUTS The named, costed problems worth solving
  FL100  SYSTEM DESIGN    Modules, data ownership, boundaries
  FL050  WORK PACKAGES    Lane-classified, gate-controlled units of work
  RUNWAY CODE             Shipped, versioned, audited
```

Altitude is one axis — *abstraction*. The model's second axis is **phase of
flight** — *maturity*: apron (nothing built), taxi (choices, no data),
takeoff roll (watch for **V1** — the first stored business data, past which
you fly the airplane), climb, cruise, and the go-around (a governed
migration). The Phase Check (doc 11) autodiscovers where you are, and every
method activity scales to it.

**The rule:** you may only descend one level at a time, and you may not descend
until the level above is written down. Most AI-assisted projects fail because the
operator starts at the runway ("build me an app that...") with nothing above it.
The agent will happily comply, and you will get confident, coherent, wrong software.

**Adopting takes one step:** hand this folder to your AI agent and say
*"Read ADOPT.md — let's go."* The agent checks
your project's phase, installs only what that phase requires, and ships
something real in the first session. Details: [ADOPT.md](ADOPT.md) and the
[QUICKSTART](QUICKSTART.md). Already six weeks into a project that's
starting to fight you? That's the normal arrival — the installer routes
you through [doc 11](docs/11-adopting-on-a-live-project.md).

## The Five Disciplines

| # | Discipline | What it prevents |
|---|-----------|------------------|
| 1 | **Altitude descent** — write each level before descending | Building the wrong thing well |
| 2 | **Context discipline** — a maintained `CLAUDE.md` as the project's constitution | The agent forgetting who you are and what the rules are |
| 3 | **Checkpoint gates (CP0–CP6)** — no work package advances without passing its gate | Silent scope drift and unreviewed merges |
| 4 | **Lane classification & parallel worktrees** — isolate work by risk class | One risky change contaminating three safe ones |
| 5 | **Schema-halt protocol** — any data-shape change stops all lanes | The single most expensive class of AI-agent mistake |

Full write-ups in [`/docs`](./docs). Reusable artifacts in [`/templates`](./templates).

## Who This Is For

Two overlapping audiences, both real:

- **Small-business owners and operators (5–50 people)** who have real domain
  knowledge and real operational pain, are already talking to an AI about
  the problem — conversational tech-savvy is assumed; engineering skill is
  not — are willing to write, review, and decide but not to become
  engineers, and want internal software that replaces payroll hours, priced
  in hours and dollars as they go.
- **Hobbyists and solo builders** with no business case to cost, but a real
  appetite for their own time and attention, who want the same discipline
  without inventing a dollar figure to justify it (QUICKSTART Door C).

Either way, the same guardrails do a second job worth naming directly:
they're what lets **someone else — a hired hand, a business partner, a
second AI session, a future version of you** — work on the same project
without silently corrupting what's there. Governance for a solo operator
and safety for a second pair of hands turn out to be the same set of gates.

## Proof

This methodology was applied by its author, working independently, to a consulting engagement with an
existing small business — a shop-management platform (quoting, customer messaging, document generation,
check printing, cut optimization, a flat-pattern drawing pipeline, audit trail) built as a sidebar/helper
app alongside the business's existing ERP, not a replacement for it. The real outcome is velocity and a
calmer front office, not a proven dollar figure; front-office capacity equivalent to one full-time
position opened up as a byproduct, not the headline. See
[`/case-study`](./case-study) for the honest version, including what this one engagement does and doesn't
prove.

## Repo Map

```
docs/
  01-altitude-model.md        The descent model in full
  02-context-discipline.md    CLAUDE.md as constitution
  03-checkpoint-gates.md      CP0–CP6 definitions
  04-lanes-and-worktrees.md   Lane classes, parallel worktrees, manifest/locks
  05-schema-halt.md           The halt protocol
  06-handoff-prompts.md       CONFIRM BEFORE BUILDING and structured handoffs
  07-platform-decisions.md    Foundation vs. scaffolding, exit-cost accounting
  08-governing-above-your-expertise.md  Tripwires, interrogation, red flags
  09-build-time-vs-run-time.md   Compile intelligence into code; contract descent
  10-seams.md                 Reception desk, swappable policy, data counter
  11-adopting-on-a-live-project.md  The front door: interrogation, departure map, fast lift
  12-agent-interface.md       Keeping the conversation at altitude; hard-path routing
  13-cost-governance.md       The cost ledger, marginal estimates, runaway tripwires, the Cray rule
  14-lineage-and-battle-scars.md  Standing on shoulders; SDD positioning; the industry's disasters, read against the disciplines
  15-standing-up-infrastructure.md  The errand pattern, tooling runbooks, and mandatory security verification
templates/
  CLAUDE.md.template          Starting constitution for a new project
  handoff-prompt.md           Work-package handoff skeleton
  checkpoint-checklist.md     Printable CP0–CP6 gate checklist
  tripwire-register.md        The operator's instrument panel (doc 07/08)
  architects-interrogation.md Standing platform-review prompt (doc 08)
  adoption-interrogation.md   Live-project adoption, Phase 1 worksheet (doc 11)
  departure-map.md            Live-project adoption, Phase 2 worksheet (doc 11)
  cost-ledger.md              Technical inventory with price tags (doc 13)
  flight-log.md               One line per session: estimates, actuals, catches (doc 03)
  incident-log.md             Blameless postmortem-lite for post-V1 breakage (doc 14)
  method-feedback.md          Findings about the method itself; "package feedback" exports issues/PRs
  instrument-panel.md         Spec: the six-pack flight instruments as one offline HTML file
  tooling-runbook.md          Lay-person setup runbook for an infra errand, worked Git+GitHub example (doc 15)
  tooling-inventory.md        Standing log of every tool/service stood up, why, and its security verification (doc 15)
case-study/
  consulting-engagement.md    A real engagement — honest gaps, and a merged independent critical review
ADOPT.md                      The installer: agent-facing instructions for one-step adoption
QUICKSTART.md                 Day one, both doors (greenfield and live project)
CONTRIBUTING.md               How amendments are validated; contributor agreement
LICENSE                       CC BY-SA 4.0
```

## License, Support & Donations

Copyright © 2026 Angus Wathen. Created and maintained independently by the
author, and validated through an independent consulting engagement with a
metal service center — see the [case study](case-study/consulting-engagement.md).


This methodology is **free and open** under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) — share it,
adapt it, teach it, with attribution and share-alike.

It was built running a real business, and it continues whether or not
anyone else finds it useful — that's not a marketing line, it's just true.
If it saves you time or money, a coffee via **[donations](https://ko-fi.com/anguswathen)**
is genuinely appreciated. It isn't what keeps this going, though — the
method gets maintained because it's in daily use, not because it's funded.

Support happens in **Discussions**, on a weekly rhythm, with no obligation
attached in either direction. Hard-path problems that outgrow the docs —
platform migrations, scaling walls, one-way-door decisions — are exactly
what doc 08 tells you to stop and get real expert technical help for.
This repo doesn't broker or sell that help; naming the boundary honestly,
and telling you when you've hit it, is the whole obligation here. In case
of emergency, release the controls and let a real pilot fly.

No warranty, no professional advice — see [LICENSE](LICENSE). Your project,
your data, your decisions.
