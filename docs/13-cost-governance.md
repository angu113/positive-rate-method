# 13 — Cost Governance: The Ledger, the Estimate, and the Cray Rule

Every other discipline in this method governs *risk*. This one governs
*money*, and for a business operator it is not a technical concern — it is
the lever they already know how to pull. Development costs money whether it
looks like it or not: hours of the operator's time, subscriptions,
per-use API pricing, storage that accretes. A method that hides those costs
behind "the agent handles it" has taken away the one instrument every owner
reads fluently. **The method's rule: cost is surfaced continuously, in the
units the operator already budgets in — dollars per month and hours per
feature.**

Two standing artifacts and three behaviors.

## Artifact 1 — The Cost Ledger (the Technical Inventory)

One running document — the financial twin of the FL100 data-ownership
table. Every product, service, subscription, and API the system depends on
gets a row: what it is, what role it plays, what tier/plan it's on, what it
costs upfront and monthly, **where the free-tier cliff sits**, what it
would cost at 5× current volume, and the tripwire threshold at which the
row must be re-opened.

Template: [`/templates/cost-ledger.md`](../templates/cost-ledger.md)

The ledger serves three readers:
- **The operator, monthly** — read alongside the tripwire register (doc 08).
  Same ritual, same five minutes: numbers you already know against
  thresholds already written.
- **The agent, every session** — the ledger is constitutional context. An
  agent that knows the ledger doesn't propose a $200/month service to serve
  a $50/month callout.
- **The platform decision record (doc 07)** — every ledger row links to its
  decision record; the exit paragraph and the running cost live one click
  apart, which is exactly how "should we leave?" gets answered honestly.

At AUTOPILOT engagement level, or whenever confirming every row live would
break a rent-first adoption session's flow (stopping mid-session to get
five or more back-to-back dollar confirmations from the operator), draft
rows with their dollar figures explicitly marked **"estimate pending —
confirm at first monthly review"** instead of blocking on live
confirmation. Resolved at the first monthly review — never silently, and
never left unmarked as if it had been confirmed.

## Artifact 2 — The Marginal Cost Estimate

Every handoff's CONFIRM BEFORE BUILDING round now returns an estimate with
the restatement:

- **Effort:** sessions/hours to CP6, honestly ranged ("2–4 evenings").
- **Run-cost delta:** any new or changed recurring cost this package
  introduces — new service, new SKU, changed usage pattern — with the
  advertised pricing, or the word **"none."**

This is what makes the method's economics *visible* instead of merely
claimed. The compounding effect (doc 06) — marginal feature cost converging
on the cost of writing its callout — becomes something the operator watches
happen in their own ledger, package by package. And a package whose
estimate exceeds its callout's costed value gets killed at CP0, which is
the estimate doing its real job: **the cost estimate is a business gate,
not paperwork.**

## Behavior 1 — Surface Costs As They Accrue, Not As They Surprise

The agent's constitutional duty: **any change in usage pattern that moves a
cost — up, down, or toward a cliff — is announced in the change summary in
plain dollars.**

> "This package stores generated PDFs in blob storage. At your current
> volume (~400 documents/month, ~200 KB each) that's under $1/month. The
> tripwire is 50 GB, where you'd cross into the next pricing band — at
> current growth, roughly six years away. Ledger row updated."

The tone matters as much as the number. The purpose is to **take the
anxiety out**: most cloud costs at SMB scale are boringly small, and saying
so — with the number — is what lets the operator stop worrying about the
meter and govern the few rows where the meter actually matters.

## Behavior 2 — Bundled Assets and Free Tiers Are Strategy, Not Cheating

An SMB rarely starts from zero. The business likely already owns
subscriptions with unused capacity — a Microsoft 365 tenant with SharePoint
and Entra in the box, an Azure subscription bolted on when the company
formed, a Google Workspace with API quotas going spare. **Riding what you
already pay for is a first-class platform driver**, recorded in the doc 07
decision record like any other.

The case-study engagement is the worked example, and it cuts both ways:

- **The win:** SharePoint-as-scaffolding was partly a *cost* decision — the
  M365 subscription was already paid, so storage, API, and auth arrived at
  a marginal cost of zero, with pricing that was predictable and low.
  That lift was real and correct. Later, genuinely heavyweight
  capabilities (mapping and routing) landed inside a provider's free tier —
  enterprise-grade function at SMB volume for $0. At SMB scale this happens
  constantly, and the ledger is where you notice it.
- **The catch:** a bundled asset is still a platform, with the same
  published limits and the same role-count arithmetic. "Free" storage that
  is also your API and your auth is still playing three roles, and its exit
  still costs what doc 07 says it costs. The ledger row for a bundled asset
  records the *marginal* cost honestly (near zero) **and** the exit
  paragraph honestly (not zero) — both numbers, side by side, is the whole
  discipline.

## Behavior 3 — Runaway-Cost Tripwires

Most SMB tech costs are flat or gently linear. A few are **runaway-shaped**
— they scale with usage in ways that can 100× without anyone changing a
line of code. These rows get flagged `RUNAWAY-CAPABLE` in the ledger,
each with a hard monthly cap or alert configured at the provider **on the
day the row is created**, not after the first surprise invoice.

The headline runaway of this era is **AI at run time** (doc 09). An agent
call inside your production workflow is a metered expense on every
execution, and the failure modes are specific and avoidable:

- **Wrong model for the job.** The most capable model is rarely required
  for extraction, classification, or formatting. The ledger row states
  which model tier the component uses and why; "cheapest model that passes
  CP4 acceptance" is the default, upgraded only on evidence.
- **No prompt caching / no reuse.** Re-sending the same instructions and
  context on every call multiplies cost for nothing. Caching is an
  acceptance criterion for any runtime-AI package, not an optimization.
- **Unbounded agentic loops.** A component that can retry, reflect, and
  tool-call in a loop has an unbounded per-run cost. Every runtime-AI
  component gets a **written per-run budget** (calls, tokens, dollars) in
  its handoff, enforced in code.
- **Building a chatbot by accident.** The doc 09 question, now with a price
  tag: is judgment genuinely a component here, or did an API-shaped problem
  get an agent-shaped (and meter-shaped) solution? Per-run intelligence is
  rented forever; compiled intelligence is bought once.

Same flag applies to per-message SMS, per-lookup geocoding, egress-priced
storage, and per-seat licenses that multiply on hiring — anything where
volume, not decisions, moves the bill.

## The Cray Rule

Cost transparency is not cost minimization. Sometimes the honest answer to
a callout is expensive — the compliance-grade service, the paid tier, the
real database. The method's obligation is to put the true number next to
the callout's costed value and let the operator make the call they are
uniquely qualified to make:

> **If the solution must be "buy a Cray," then that is the solution — and
> the operator hears it straight, priced, at CP0, not discovered at CP6.**

What the method forbids is not expense; it's *surprise*. A $400/month
answer to a $2,000/month problem is a great trade. The same $400 answer to
a $100 problem is a kill decision. Both are one subtraction — **if the
numbers are on the table.** Keeping them there is what this document is for.
