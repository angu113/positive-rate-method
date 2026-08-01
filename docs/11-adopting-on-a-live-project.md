# 11 — Adopting the Method on a Live Project

Almost nobody arrives at this method greenfield. The realistic arrival is an
operator six weeks into an AI-built project: delighted at first, business
value already on the table, and now in the arm-wrestle phase — sessions that
spiral, questions they can't answer, an agent that has quietly started making
decisions above its altitude. **This document is the front door for that
operator.** It is also, deliberately, the procedure this method's own author used when applying an
already-developed version of this method to a real, live consulting engagement — adoption must
round-trip onto real practice, not just theory, or the abstraction leaked.

Adoption is not a rewrite. A live project with business value is a working
shop floor; you do not halt it to repaint the lines. Adoption is three
phases: **interrogate what exists, map the departures, install the minimum
that protects value.**

## Phase 0 — The Phase Check

**Check for existing luggage first** (doc 12): `git fetch` and diff
against `origin/<default-branch>` before assuming this repo has no
in-flight adoption already — a second session on another machine can
otherwise run the same Phase 0 in parallel, unaware, and only find out at
a rejected push.

Before interrogating anything, establish **where the aircraft is** (doc 01,
Phase of Flight) — because every later step scales with the answer. This is
autodiscoverable: the agent runs it against the project in minutes, from
observable facts, no opinions required:

1. **Is real business data stored?** How many records, how many months
   deep? → *Any yes means V1 is behind you.*
2. **Have real documents/outputs reached customers?** Invoices issued,
   messages sent, files delivered? → *Also V1-crossed.*
3. **Does anyone's daily workflow depend on it?** Who stops working if it
   dies tomorrow?
4. **How many platform choices have data behind them?** (Choices without
   stored data are still TAXI-reversible; choices with data are luggage.)
5. **Is it still being actively built, or running steady?**

Score it plainly: no to everything → **APRON** (skip doc 11 entirely — take
the greenfield door in QUICKSTART). Choices but no data → **TAXI** (the
lift is trivial: record the decisions now, at their cheapest). Data and
users but still building → **TAKEOFF ROLL / CLIMB** (full doc 11, and the
V1 crossing gets back-dated and logged). Business runs on it → **CRUISE**
(full doc 11; the archaeology in 1d is the bulk of the work). Migration
already in flight → there's also a **GO-AROUND** in progress; govern it as
its own RED project per doc 07.

The phase stamps every artifact that follows — interrogation, departure
map, and cost ledger all carry it, because a DEBT rating at TAXI and the
same finding at CRUISE are different animals with different prices.

## Phase 1 — The Interrogation

Before touching a single prompt, inventory what exists. **The operator is
never asked to read code — every question you put to them stays in
business language.** The agent inspects code and config directly rather
than only asking; that inspection is what catches a real finding (a
config value nothing actually reads, say) that a conversation-only pass
would miss. Four artifacts, one evening:

### 1a. Value inventory — *what we protect*
Capability by capability: what does this system do for the business today,
who uses it, what did it replace, what breaks if it dies tomorrow. This list
anchors every later decision — departures are judged against it, not against
methodological purity.

### 1b. Friction log — *where time disappears*
Where does the AI go sideways? The questions you couldn't answer, the
sessions that spiraled, the "it keeps asking me about code" moments, the
features that took three attempts. Each entry: what you asked for, what
happened instead, what it cost. This log becomes the operator-interface
rules in your new constitution (doc 12) and, aggregated across adopters, the
method's own amendment queue.

### 1c. Data reality — *what we own and where it lives*
The FL100 data-ownership table, filled retroactively: what data exists,
where it's stored, who (which module, which platform) owns it, and — the
question most vibe-coded projects cannot answer — *can you get it out?* If
any answer is "I don't know," that row is already a finding.

### 1d. Decision archaeology — *what doors we already walked through*
Every platform-level choice already made (storage, auth, hosting, identifier
scheme, document generation), classified **now** as foundation or
scaffolding per doc 07, with a priced exit paragraph — the classification
nobody did at the time. The case-study engagement's SharePoint choice is the worked
example: a *correct* scaffolding call, unclassified, exit unpriced,
discovered at the 5,000-item threshold. Right decision, wrong bookkeeping,
expensive discovery.

Template: [`/templates/adoption-interrogation.md`](../templates/adoption-interrogation.md)

## Phase 2 — The Departure Map

Two columns: **business value at stake** vs. **methodology departure.**
Walk docs 01–10 against the interrogation output and log every place the
live project diverges. Each departure gets exactly one rating:

| Rating | Meaning | Disposition |
|--------|---------|-------------|
| **HARMLESS** | Departure exists, touches no value and no risk | Leave it alone. Forever, if it stays harmless. |
| **DEBT** | Will hurt at a known, nameable threshold | Register a tripwire (doc 08). Move on. |
| **ACTIVE BLEED** | Costing time or risking value *right now* | Fix in the lift (Phase 3). |

**The governing rule, in bold because it is the whole discipline:**

> **Departures are only fixed where they touch value or risk. Purity is not
> a reason.**

This rule is what separates adoption from a compliance audit. A consultant's
incentive is to find the maximum number of departures; the operator's job is
to find the three that matter. Expect the map to show mostly HARMLESS, a
handful of DEBT, and one or two ACTIVE BLEED — if everything looks like
bleed, re-check the value inventory, because the project that reached this
document alive is doing more right than wrong.

A special third finding class appears when the method is adopted by its own
author or another expert: departures where the docs and the practice
*disagree and the practice wins* — the thing works only because expertise is
silently filling a gap. Those are not departures to fix; they are **doc
amendments to make** and, for lay adopters, the exact holes to fence with a
procedure or a red flag. Log them separately.

Template: [`/templates/departure-map.md`](../templates/departure-map.md)

## Phase 3 — The Fast Lift

Minimum viable install, strictly ordered by protection-per-hour:

1. **Constitution first.** Write `CLAUDE.md` directly from the interrogation
   output: the value inventory becomes the purpose and standing constraints;
   the friction log becomes the operator-interface rules (doc 12); the data
   reality becomes the ownership table. One evening. The single biggest
   lever in the whole lift.
2. **CONFIRM BEFORE BUILDING installed on the very next session.** This
   kills the arm-wrestle immediately — which is the pain that brought the
   operator here. Instant, felt relief buys patience for the rest.
3. **Tripwire register seeded** from every DEBT row in the departure map.
   The operator now watches the thresholds instead of discovering them.
4. **Schema-halt armed.** The one protocol worth installing before it is
   needed. It costs a paragraph in the constitution and saves the class of
   mistake that cannot be reverted.
5. **Gates on new work only.** CP0–CP6 apply from the *next work package
   opened.* Never retrofit gates onto in-flight work — half-gated work is
   worse than ungated, because it looks governed and isn't. In-flight
   packages finish under the old regime; the first gated package is the
   project's true adoption date.

### The rent rule

> **The first session under the method must ship a real business item.**

Not setup. Not cleanup. Not "reorganizing the repo." Something from the
operator's actual to-do list, delivered through the new handoff format. If
adoption day one produces paperwork instead of business value, the lift has
failed and the operator will — correctly — revert. The method pays rent
immediately or it doesn't move in.

## When Adoption Surfaces a Hard-Path Problem

Phase 1 sometimes reveals a problem bigger than a lift: a platform at its
published limit, a migration already overdue, a data shape that cannot
support the next callout. **Do not fold that problem into the adoption.**
It is its own RED-lane project with its own gates, and it is exactly the
class of decision doc 08's escalation boundary exists for — interrogate it,
price it, and if the register has tripped and the door is one-way, bring in
real expert technical help for that one decision. Adoption installs the
governance; it does not perform the surgery.

## Running Phase 1 Self-Serve

Phase 1 is designed to be run straight from the templates, unaccompanied —
that is the complete path, not a stripped-down one. If a live project's
interrogation surfaces a hard-path problem beyond this document's scope
(doc 08's boundary), the answer is the same one doc 08 always gives: bring
in real expert technical help for that specific decision. The templates
and procedure are the whole of what this document offers; there is no
separate edition behind them.
