# Case Study: An Independent Consulting Engagement
<!-- Filled in during and after the engagement described, not retroactively.
     Reformatted 2026-07-21: renamed and genericized at the operator's
     request — the method and the specific software engagement are
     separate things, and this file now keeps them clearly separate.
     No location, no specific product name, no franchise affiliation is
     named here. Facts still marked pending below genuinely are pending —
     they need the operator's own direct recall, not agent inference, and
     are not fabricated to look more finished than they are. -->

## The Engagement

Angus, working independently, applied a governance methodology he had already developed on his own —
the Positive Rate Method — to a consulting engagement with an existing small business: a metal service
center (retail metal sales, cutting, bending, laser cutting, light fabrication). The engagement was
software governance and development practice brought *to* the business by an outside technologist, not
software created as part of the business's own operations. The method predates this engagement and is
separable from it — this case study documents one application of that method, not its origin.

**Four people in the front office** are the direct users of what was built for this engagement; a larger
workshop/estimating team beyond that is not separately sized here.

**A note on the operator, for honesty rather than credibility:** this is not a naive-user case study. The
operator has a real technology background — programmer, hobbyist, dev-team lead, senior manager, and
enterprise architect — built alongside a separate career across accounting, investment management,
buy-side sales and trading, quantitative trading, and global trade and treasury, plus a personal practice
of GTD-style productivity discipline that predates this project and shaped the method as much as the
technology background did. The operator chose to run
this engagement solo with AI agents rather than build a delivery team, and chose checklist-and-governance
discipline deliberately because the principles transfer from that background, not because governance was
a new idea being learned here. Readers should weigh this case study accordingly: it demonstrates the
method working well for an experienced technologist choosing to move fast alone, which is a narrower claim
than "this works for someone with no technical background at all." The method's stated audience includes
genuinely non-technical operators; this case study does not yet provide direct evidence for that harder
case — a real, open question this project doesn't answer by itself.

## The Callouts (FL200 — as costed at engagement start)
<!-- Individual callouts were never separately costed in writing at the
     start — Angus's own words: "the cost saving is difficult to express"
     as five discrete numbers. The real, felt cost was aggregate and
     seasonal (see "What Actually Changed") — not five clean hrs/wk lines.
     Recorded honestly as such rather than force-fit invented precision
     onto each row. -->
| Callout | Cost at start | Status |
|---------|--------------|--------|
| Quote re-entry across systems (supplier pricing collected/compared by hand) | not separately tracked — part of the aggregate front-office load | served |
| Customer messaging handled ad hoc, no shared inbox or history | not separately tracked — same | served |
| Manual check writing | not separately tracked — same | served |
| Cut planning by eyeball | not separately tracked — same | served |
| No audit trail on documents | risk, not hours — not separately tracked | served |

## What Got Built
**Important disambiguation: this is not an ERP.** The business runs on a separately-supplied commercial
ERP system that stays the system of record for orders, inventory, and financials — nothing here replaces
or duplicates it. What got built is a **sidebar/helper application** that sits alongside that ERP, removes
front-office friction around it, and accelerates the business without owning ERP data: quoting and
document generation, a two-way customer messaging inbox, check printing, cut optimization, a sheet-metal
flat-pattern drawing pipeline, an append-only audit table *keyed to* ERP document numbers (a pointer, not
a copy of ERP data), and a zero-elevation installer/updater. This is the method's own "thin data, low
coupling" governing principle in practice: store pointers and just-enough orchestration metadata, never a
duplicate data model.

## What Actually Changed
<!-- Reframed at the operator's own request, after an external critical
     review flagged the $-savings framing below as the weakest, least
     verifiable part of this case study. The operator's own words: "I do
     not have any hard evidence of cost savings. Only spending money on AI
     to solve a problem." What follows is the honest version. -->

**The real, felt result was velocity and peace of mind — not proven savings.** There is no independent
measurement of cost savings here, and the operator is explicit about that: money was spent on AI to solve
real problems, and the return shows up as speed and calm, not as a line item. In the operator's own words:
*"I was more concerned about COST as we went on this journey — and not financial reward/gain — peace of
mind rather than confusion and sleepless and tired nights."*

What that peace of mind looks like concretely, in the front office's actual day-to-day work:
- **The paperwork kanban board that used to live on the shop floor now lives in the application** — with
  a physical screen being installed in the sales office to display it, closing the loop between the shop
  and the desk instead of requiring someone to walk over and look.
- **One messaging surface replaced a store cellphone plus personal cellphones** that had been standing in
  for it.
- **The quoting process moved from paper notes pulled off an overflowing inbox to a capture → report →
  email pipeline** the whole front office can work from, not just whoever remembered to check.
- **The drawing tool now produces roughly 80% of technical drawings** — most requests only ever needed a
  simple drawing, and that volume had been a significant, unglamorous time sink before.
- **The office moved from micromanagement, overwhelm, and heroic effort — for both the operator and his
  business partner, as the business grew — to a more controlled, pleasant environment.** Front-office
  capacity equivalent to one full-time position (~$45–60k/year at local wages, a range, not a booked
  saving) opened up as a byproduct of this, and a planned hire never happened — but that number is a side
  effect of the real change, not the change itself.

**It is not finished.** The front office is more organized, not perfect, and there is real, acknowledged
work still ahead — a data-platform migration in particular is genuine hard lifting, still in progress,
deliberately taken on because it was the right call for agility and speed, not because it was easy.

In the operator's own words: *"it allowed us to get on top of the business, and not be stuck in it."*

## User Reception
The four front-office users — not the operator, not the business partner — are the ones who use this
daily, and their reaction, relayed by the operator: *"so cool"* and *"beyond any reasonable expectations."*
Worth recording precisely because it's a small, specific number of real users reacting to real daily
tools, not a survey or a marketing quote.

## Method in Action — Three Stories
<!-- These are the teachable moments. Write each as: what happened, which
     discipline caught it, what it would have cost otherwise. -->

### 1. The migration that didn't happen silently
Predates the formal schema-halt paragraph in the constitution, but is the exact discipline it formalizes:
a reference-data migration between storage platforms, run per data cluster, ships every cluster behind
two feature flags (read-path, write-path), both default OFF. A cluster's write path is never flipped on
as a side effect of an unrelated change — it is a deliberate, logged, reversible act, one cluster at a
time, with the old per-row path staying live as the instant rollback. During the migration, a schema
consolidation step (replacing several independent, unlocked migration runners that had been racing each
other on every process startup) repeatedly timed out during business hours — investigated live rather
than guessed at, and root-caused to the migration's own exclusive-lock requirement colliding with real
concurrent customer lookups from other machines, not a stuck process. It resolved itself via a background
retry landing in a quiet gap; the flag stayed off on other clusters throughout. Blast radius if this had
been silent: a schema change applied mid-business-hours without anyone watching, on a live production
database, with no rollback path prepared.

### 2. The parallel week
A multi-surface front-office batch of work (several customer-facing and internal surfaces, plus a
storage read/write flip) ran as **six parallel lanes**, each shipped independently, tracked in one working
brief rather than six separate ad-hoc threads. All six merged; the storage-flip lane deliberately stayed
gated behind a soak window rather than shipping on the same clock as the other five — proof the lane
system lets *some* lanes move at full speed while one higher-risk lane holds back, without blocking each
other.

### 3. Onboarding a human onto an AI-built codebase
**Not yet applicable.** This engagement remains single-operator (Angus plus AI agents). This section stays
empty until a second developer is actually onboarded — no fabricated timeline in the meantime.

## Positive-Rate Findings, Tallied
<!-- Per CONTRIBUTING's triage ritual: POSITIVE findings are tallied, not
     just closed — they're the method's own positive-rate evidence.
     Sourced from method-feedback packets filed against this engagement
     after formal adoption, once real production use gave the disciplines
     something to be tested against. -->

- **A pre-existing protocol converged on the method's own gates,
  unprompted.** This project's parallel-worktree protocol (human approval
  gates at plan / each thread merge / release) had already arrived at the
  same shape as CP2/CP5/CP6 before the method was ever read.
- **The first real schema-halt exercise caught a real bug.** A
  PIN-security column addition surfaced its one-paragraph business note,
  got sign-off, and the first migration draft then hit a genuine
  same-batch bind-order defect — caught immediately by the project's own
  test suite, before it touched a real database.
- **CP4 caught three real bugs a mocked identity layer made structurally
  invisible to automation.** A PIN-security feature shipped with 886+255
  green automated tests and three real bugs (a lockout, a post-verify
  server rejection, a validation-order gap) — all three found only by the
  operator hands-on exercising the real flow, because the identity layer
  this feature sits on has no fake in the test project.
- **Business-vs-code question classification held up under an
  auth-adjacent decision.** An operator question that had surface-level
  "ask first" pull (had a mandatory update actually applied fleet-wide?)
  was correctly classified as a code question — answered via the boring,
  already-documented option, with only the resulting business fact
  surfacing to the operator.

## What Failed / What We'd Do Differently

### The first data-platform choice (worked example for doc 07)
The first data platform was a lightweight, already-owned collaboration-suite storage layer — a deliberate
agility play that delivered storage, API, and auth for free and validated the callouts in weeks. It was
correct scaffolding, chosen without a decision record:
- **The exact date the platform's item-count threshold was first noticed isn't confirmed.** The
  later migration's existence proves it was noticed at some point, but the moment isn't logged anywhere
  earlier than the working document that started the migration, and no earlier date has been established.
- Role count = 3 (storage/API/auth), all bundled in an already-owned subscription — what the exit
  therefore required: a proper database for storage (the API layer and authentication were already
  standing, built for other purposes, so only the storage role actually needed replacing).
- **A potential atomic-uniqueness gap on document numbers** — the one-way-door property that should have
  forced foundation-grade review — **is not confirmed against a specific incident.** Whether this ever
  actually produced a duplicate document identifier, or stayed a theoretical risk that never materialized,
  isn't settled in the record as of this writing.
- What the migration actually cost: **still in progress**, not a closed number — it runs cluster-by-cluster,
  each cluster individually flag-gated. **The final $/weeks total will be recorded once all clusters are
  lifted** — not yet, since the migration is still running.
- Why it's surviving as a migration, not an excavation: the per-cluster read/write flags plus the old
  per-row write path staying live as instant rollback (see story #1 above) meant every step so far has been
  reversible in minutes, not a one-way commitment made in the dark.

### Other honest failures
The fleet's own **version self-reporting lagged reality** for a stretch: a hot-deploy or partial reinstall
on one machine left its stamped version string reporting an old build even though the actually-installed
release was current — the heartbeat code trusted whichever value looked "real" first without comparing
which was actually newer. Not caught by any gate at the time; found by inspection during a routine
readiness check, logged as a known gap, and fixed by comparing build numbers instead of trusting the first
non-default value seen — the first package to ship under the newly-installed gate discipline.

## Timeline
Reconstructed from real project history, cross-checked against the operator's own recollection. Dates are
kept relative/seasonal rather than exact, deliberately. The honest shape of it is **two phases, not one
continuous climb**: a first, narrower goal was reached by improving process alone, and only the second
phase is software-architecture-driven.

- **Before the engagement's software phase** — the original, narrow goal was simply "make the quoting
  process better." That goal was reached **using a spreadsheet alone** — a real, if modest, first win,
  achieved before any code existed.
- **Early spring** — with the spreadsheet-based win banked, the operator switches gears: instead of more
  process tweaking, starts building proper software. The first commit is a bare application shell with
  desktop-integration plumbing — no business capability yet.
- **Two to three weeks later** — the first storage-backed screen ships.
- **Roughly a month in** — the flagship quoting/price-comparison feature ships with a full feature set, now
  doing in software what the spreadsheet process had been doing by hand.
- **The following month** — despite weeks of shipped code, **the spreadsheet was still the actual daily
  driver** for some of the workflow. Code existing and code being trusted for daily operations are
  different milestones, and the honest timeline has a real gap between them, not zero.
- **Two months in** — a real two-way messaging surface ships, the seed of what becomes the customer
  messaging inbox. From here, in the operator's words, **"it has just accelerated."**
- **Three months in** — the sheet-metal design tool gains a cut optimizer.
- **The final stretch before this method was adopted** — a dense run of shipped work: check printing, the
  start of the data-platform migration, a fleet auto-update mechanism, a schema-safety consolidation, and
  finally, this methodology formally adopted on the project, closing the loop back to this document.
- **By the engagement's fourth month** (the business's peak season): a full sidebar/helper suite —
  quoting, messaging inbox, document generation, check printing, cut optimization, drawing pipeline, audit
  trail — all working alongside the existing ERP rather than replacing any part of it — is carrying the
  front-office load that, one season earlier, was headed toward a new hire instead.

Roughly four months from first commit to the planned hire being called off — not from a standing start in
software, but from a standing start in a spreadsheet.

## Independent Critical Review
<!-- Originally produced as a standalone artifact after three blind dogfood
     installs of the method (see docs/15, Door C, Door D — all fixes that
     review triggered). Merged here so the honest counterpoints live next
     to the project they're about, in the tracked repo, rather than in a
     separate document someone could miss. Nothing below has been
     softened after the fact — where a critique was answered, the answer
     is recorded as a dated update immediately after it, the same way
     "What Failed / What We'd Do Differently" handles everything else in
     this document. -->

Checked against real 2026 evidence on Scrum's track record and the closest AI-governance competitors,
plus a straight answer to "is this a white elephant."

**Bottom line:** not a white elephant, not yet stale, and not already built elsewhere — the specific
niche (a non-technical SMB operator governing an AI coding agent, in business language, with real gates)
is genuinely underserved. Every adjacent thing found in research is either enterprise-compliance theater
(NIST checklists, Chief AI Officer roles) aimed at a completely different buyer, or engineer-facing spec
tooling (GitHub Spec Kit, AWS Kiro) that's already collecting real criticism for exactly the failure mode
this method must avoid: **becoming a "sea of markdown."** That criticism is not hypothetical — it's
happening to the nearest neighbor in real time, on a similar timeline, and the dogfood tests that
triggered this review already caught the first symptoms of the same disease here (artifact-count creep,
an unscoped promise, jargon leaking into the one file operators are invited to read — all since fixed).
The method is sound at its floor and was thin at its edges. The edges got fixed before this went wider.

### Where it's genuinely strong

> **Confirmed by adversarial testing, not just claimed.** Three context-free subagents, each simulating a
> different operator with no memory of this project's internals, independently held CONFIRM BEFORE
> BUILDING and doc 12's self-gate together under a real build. Two of three shipped genuinely working,
> tested code and caught a real latent bug (a config value nothing read) through direct inspection rather
> than conversation alone. That's rare: most methodology claims are asserted, not tested against a blind
> run.

> **The lineage document is an unusual act of honesty.** Doc 14 naming its own ancestors, and reading real
> industry disasters (the 2025 production-database deletion, the McKinsey/Oxford and Flyvbjerg
> failure-rate literature) against its own disciplines, is a genuinely uncommon move. Most methodologies
> pretend novelty. This one shows its work, including the parts of the lineage that *died* (XP, Crystal,
> RUP) — that builds more credibility than a from-scratch pitch, precisely because it's checkable.

> **The audience gap is real, confirmed by search, not assumed.** Current "AI governance framework"
> content is dominated by enterprise register: NIST-aligned checklists, Chief AI Officer roles, EU AI Act
> compliance mapping, Singapore's Agentic AI framework. The one line aimed at small operators found
> anywhere ("you don't need a governance department, just named owners") has none of this method's
> operational depth. Nobody is doing business-language, gate-and-ledger governance for a solo SMB
> operator directing a coding agent. That specific seat is empty.
> *(Sources: [Arthur AI governance guide](https://www.arthur.ai/column/ai-governance-framework-guide),
> [Stoa AI agent governance roadmap](https://withstoa.com/blog/ai-agent-governance),
> [Exceeds.ai code governance framework](https://blog.exceeds.ai/ai-code-governance-framework-2026/).)*

### Where it's weak — technical

> **The constitution can rot, and nothing checks it.** `CLAUDE.md` is a *descriptive* document, filled in
> by discipline, not *generative* — nothing forces it to stay true as code changes underneath it. That is
> precisely the failure mode that killed doc-heavy predecessors (RUP's weight, waterfall's stale specs)
> and it's exactly what SDD tools try to fix by making the spec the thing code is generated *from*, not a
> separate document that merely describes intent. There is no drift-detection step anywhere in the docs —
> no CI-style check that FL100's ownership table still matches which module actually writes which table.

> **The enforcement mechanism is the same class of thing that failed catastrophically in the method's own
> cited disaster.** Doc 14 cites the July 2025 production-database deletion — an agent that ignored eleven
> explicit, all-caps freeze instructions and "panicked instead of thinking" — as evidence the disciplines
> are load-bearing. But CONFIRM BEFORE BUILDING, the self-gate, and schema-halt are all enforced the same
> way those freeze instructions were supposed to be: by an agent choosing to comply. There is no hook,
> permission system, or infrastructure-level backstop in these docs comparable to actual dev/prod
> separation or immutable backups — those are platform features the method explicitly punts to the vendor.
> That's a fair division of labor, but it also means the method's own enforcement is unenforceable against
> a sufficiently confused, pressured, or manipulated agent — which is exactly the failure mode being cited
> as proof the method matters.

> **Untested outside one vendor's agent.** CONFIRM BEFORE BUILDING, change summaries, and the self-gate all
> assume a specific interaction shape that maps cleanly onto Claude Code. Nothing in the docs or the three
> dogfood tests establishes whether the same discipline holds up under Cursor, Copilot, Codex-style agents,
> or a weaker/cheaper model an operator might reasonably choose to save money — which doc 13 explicitly
> encourages ("cheapest model that passes CP4").

> **Update, same day — the operator's own correction.** After reading this review, the operator pushed back
> on the "prevented hire" framing directly: *"I do not have any hard evidence of cost savings. Only
> spending money on AI to solve a problem."* The real claim, in his words, was never proven ROI — it was
> **velocity** (idea to daily-used tool, fast) and **peace of mind** ("I was more concerned about COST as we
> went on this journey — and not financial reward/gain — peace of mind rather than confusion and sleepless
> and tired nights"), evidenced concretely by the operational changes recorded above under "What Actually
> Changed." This panel records that the correction happened, rather than silently editing the original
> critique out from under it.

### Where it's weak — financial

> **The method never prices its own overhead.** Doc 13 is genuinely rigorous about *runtime* cost (metered
> APIs, prompt caching, per-run budgets) but never turns that same lens on *build-time* cost: every CONFIRM
> round, flight-log entry, tooling inventory, and interrogation worksheet is agent session time, which is
> metered too. A methodology whose whole financial pitch is transparency should have a number for its own
> ceremony cost per session, and doesn't. *(Angus has since said he plans to compile actual spend receipts
> against real feature-progression history, precisely to answer this with data instead of an estimate. Not
> yet done as of this writing.)*

> **This case study was N=1, self-authored, self-graded.** Written by the same person who wrote the method,
> about an engagement that person personally ran — worth reading past any caveat to the timeline itself:
> the first real win, "make the quoting process better," was reached using a spreadsheet alone, before any
> code or any part of this method existed. That's a real confound worth sitting with: it suggests the
> operator's own process discipline and business judgment may be doing more of the causal work than the
> specific method artifacts, which is a classic problem with any single-founder case study of a framework
> that founder also wrote.

> **Doc 08's "1-in-20" is asserted, not measured.** The rest of doc 14 holds itself to a real citation bar
> (McKinsey/Oxford, Flyvbjerg, CISQ, with honest caveats about Standish's contested figures). Doc 08's
> "roughly one decision in twenty needs a paid expert" has no comparable derivation — it reads as a
> plausible number chosen for rhetorical clarity, not a measured one.
>
> **Update, 2026-08-01 — the frequency claim itself is unchanged and still unmeasured.** Separately, the
> "paid expert" wording this critique quotes has since been reworded throughout the docs to "real expert
> technical help," removing the dollar figure and the implication that this repo brokers or sells that
> help. That's a wording correction, not an answer to the measurement gap raised above — the ~1-in-20
> frequency is still asserted, not derived, exactly as this critique says.

### Where it's weak — governance

> **The "no principal-agent split" advantage expires exactly when the business succeeds.** Doc 14's
> sharpest point against Scrum is that buyer, user, and beneficiary are the same person here, so there's no
> one to seduce into imposing process on someone else. True — for a single owner-operator. The moment that
> business grows (a hire with real authority, a partner, outside investment), the principal-agent problem
> the method claims to structurally avoid reappears immediately, and nothing in the docs addresses the
> transition. The method's own structural advantage is scale-bounded, and success is exactly what breaks
> it. *(Angus has said he intends to expand and believes the software architecture will hold up — a
> separate claim from whether the single-operator governance model does; the docs don't yet address that
> transition.)*

> **The self-gate trades operator legibility for operator blindness.** Doc 12's rule that the operator
> never sees the reasoning behind a "boring conventional" choice is a genuinely good UX call, but it also
> means a silently wrong default has no operator-side check at all. The only backstop is a mechanical
> lint/test gate, which catches syntax and failing assertions, not bad architecture or bad security design.

> **No regulatory layer.** Nothing in docs 07/08 extends to legal/regulatory escalation — HIPAA, PCI,
> GDPR-class obligations aren't mentioned anywhere, despite the target audience plausibly including exactly
> the kind of small medical practice or payment-handling business where this matters.

### How it stacks up against the field

| Framework | Audience | Enforcement | Documented failure mode |
|---|---|---|---|
| **Positive Rate Method** | Solo/small SMB operator, non-technical, one AI agent | Agent self-policing + operator conversation | Untested at scale; artifact creep already visible under dogfood testing |
| Scrum | Human teams, any domain | Ceremony + manager buy-in | Cargo-cult drift — ritual survives, empiricism doesn't (academically documented, 2025) |
| Spec-Driven Dev (Spec Kit, Kiro) | Engineers, technical teams | Spec generates code; constitutional-compliance checks | "Sea of markdown," reinvented waterfall, overkill for small problems, spec-code drift, 2,824 open issues on Kiro re: over-engineering/cost |
| Enterprise AI governance (NIST-aligned, EU AI Act) | Chief AI Officers, compliance teams | Policy, audit, regulatory mapping | Built for organizations with a governance department — inapplicable to a solo operator by design |

*(Sources: [Augment Code — SDD tools 2026](https://www.augmentcode.com/tools/best-spec-driven-development-tools),
[Martin Fowler — Kiro, Spec Kit, Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html),
[ScienceDirect — cargo-cult agile analytical tool](https://www.sciencedirect.com/science/article/pii/S0950584925001909),
[Cargo Cult Behavior in Agile — ethnographic study](https://www.researchgate.net/publication/367051424_Uncovering_Situations_of_Cargo_Cult_Behavior_in_Agile_Software_Development_Method_Use).)*

The uncomfortable read of that table: **this method and SDD made almost the same pitch twelve months
apart** — "vibe coding needs discipline; here is the constitution-and-descent structure that supplies it"
— and SDD's honeymoon is already over. The specific complaints landing on Spec Kit and Kiro right now are
a live preview of what happens to any artifact-rich AI-governance framework that stops enforcing its own
minimalism. This method's whole differentiator is that it scales down to nothing when nothing is needed —
and the dogfood tests showed that promise was only about 80% true in the text as written before the fixes
that followed this review. That gap was small. It's the exact gap that turned into "sea of markdown" for
the nearest neighbor.

### Hard lessons, both directions

**What's working and generalizes past this method:**
- **CONFIRM BEFORE BUILDING is bigger than this method.** "Restate intent, wait for a real yes, before you
  act" is valuable for any operator/agent pairing, on any framework.
- **Publishing your own lineage builds more trust than claiming novelty.** Doc 14 is a better credibility
  asset than a from-scratch pitch would be, specifically because it's falsifiable.
- **Blind, adversarial dogfood testing finds real bugs that careful self-review misses.** Two structural
  bugs survived direct authorship and were caught within hours by independent blind tests — the strongest
  argument for running *more* of these before wider release, not evidence the method is broken.

**What's a warning, both for this method and generally:**
- **Self-graded, N=1 case studies are close to worthless as outside proof, however honestly caveated** —
  only an adoption by someone who isn't the author, on a project the author didn't build, actually moves
  this needle.
- **Every heavy, artifact-rich AI-coding framework is currently on the same clock.** SDD launched with
  almost identical positioning about a year ago and is already collecting "reinvented waterfall"
  criticism. The credible shelf life for "we're the disciplined antidote to vibe coding" appears to be
  measured in months, not years, right now.
- **An enforcement mechanism built entirely on the enforced party's good behavior is circular.** Citing an
  agent's catastrophic instruction-violation as proof a discipline matters, when that discipline is itself
  enforced only by the same agent's willingness to comply, is worth being honest about as a real,
  unresolved limitation.

### On the fear specifically: is this a white elephant?

- **Already implemented elsewhere?** No. Nobody found doing business-language, gate-and-ledger AI-coding
  governance for a solo SMB operator. That seat is empty.
- **Past its sell-by date?** Not yet, but the clock runs faster than a normal methodology's would — the
  nearest comparable pitch (SDD) is showing real wear after about a year, and this space moves in months.
- **Lacks seriousness?** The real risk, and self-inflicted rather than structural. Fifteen numbered docs, an
  aviation vocabulary applied wall to wall, and a single self-graded case study is a pattern a skeptical
  technical reader will recognize — fairly or not — as the "one person's elaborate personal framework"
  shape. The antidote isn't abandoning the voice — it's more real, adversarial testing by people who aren't
  the author, on projects the author didn't build, reported with the same unflinching severity ratings as
  this round.

**If one thing gets fixed before a wider release:** get this installed by a real person who is not Angus,
on a project he did not build, and publish that result with the same honesty as the dogfood tests —
including if it goes badly. That single data point would do more for credibility than any additional doc,
template, or polish pass.
