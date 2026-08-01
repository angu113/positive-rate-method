# 07 — Platform Decisions: Foundation vs. Scaffolding

Every FL100 platform choice is one of two things, and the method requires you
to say which — **in writing, at decision time**:

- **Foundation** — chosen to carry the system for its life. Judged on limits,
  guarantees, and fit.
- **Scaffolding** — chosen deliberately for speed, with the full intention of
  tearing it down later. Judged on how fast it gets you to a validated
  callout, *and on the written cost of the exit.*

Scaffolding is not a mistake. Choosing it *without naming it* is the mistake —
because unnamed scaffolding quietly becomes foundation, and you discover which
one you built only when you hit its wall.

## The Decision Record

Every platform-level choice gets a one-page record with five fields:

**1. Classification.** Foundation or scaffolding. One word, dated, signed.

**2. Published limits.** The platform's *documented* hard limits and where
current growth puts you against them in 24 months. Platforms almost never
fail by surprise — they fail at limits that were published all along, watched
by no one.

**3. Role count.** How many architectural jobs is this one component doing?
Storage? API? Authentication? Identity? Workflow? **Exit cost scales with
role count**, roughly multiplicatively: leaving a component that plays one
role means replacing one thing; leaving a component that plays three means
replacing three, and untangling every place they assumed each other.

**4. The exit paragraph.** What leaving costs — in dollars and weeks, at
today's best estimate — and what the replacement would be. Scaffolding
without an exit paragraph is not scaffolding; it's foundation you're lying
to yourself about.

**5. Review triggers.** Thresholds *in business units the operator already
tracks* — documents/month, headcount, integration count, records stored —
at which this record must be re-opened. Not calendar dates: growth dates.

## The One-Way / Two-Way Door Test

Before classifying, ask: **if this choice is wrong, can we walk back through
the door?** Data platforms, identifier schemes, and anything that issues
documents customers keep are one-way doors (reversal cost grows with every
record written). UI frameworks, report generators, and internal tooling are
mostly two-way. One-way doors deserve foundation-grade scrutiny even when
you're moving fast; two-way doors are where deliberate scaffolding earns
its keep.

## Worked Example: The SharePoint Exit

The consulting engagement described in the case study chose SharePoint lists as its first data
platform. This was a *correct* scaffolding call: storage, API, and
authentication for free on day one meant callouts were validated in weeks,
not months.

What the decision record would have caught — because none existed yet:

- **Published limits:** the 5,000-item list view threshold was documented
  from the start. Nobody was watching document volume against it.
- **Role count: three.** SharePoint was simultaneously storage, API, and
  auth. The exit therefore meant standing up all three replacements at once
  (Azure SQL + an ASP.NET Core API + Entra-based auth), not swapping a
  database.
- **The unwritten exit paragraph:** because it was never priced, the exit was
  deferred past the point of cheapness. What would have been a migration
  became a re-architecture.
- **The un-named guarantee gap:** document numbers require true atomic
  uniqueness; a list platform with eventual-consistency behavior cannot
  promise that. This is a one-way-door property that scaffolding
  classification should have flagged for foundation-grade review.

The migration succeeded anyway — and *why* it succeeded is the method's own
disciplines: the append-only audit trail and the FL100 data-ownership table
meant every record's shape and history were known, which is the difference
between a migration and an excavation.

**The lesson is not "don't use SharePoint."** The lesson is: scaffold on
purpose, price the exit the day you build it, count the roles, and watch the
published limits like you watch your bank balance.

## Platform Choice and Agent Velocity

One modern input to the FL100 record: AI coding agents are not equally
strong everywhere. Mainstream web stacks are their home territory; niche or
older native frameworks work but run thinner. The method is
platform-agnostic — the governance is identical on any stack — but agent
velocity is a legitimate, recordable factor in the platform decision itself.
Write it in field 2 like any other limit.
