# 09 — Agents at Build Time vs. Run Time

The current wave of agentic tools puts the AI at **run time**: every
execution, the agent re-reads a screen or tool surface, re-decides, and
re-clicks. Every execution is therefore probabilistic, costs tokens, takes
seconds to minutes, and inherits whatever the UI feels like doing today. A
moved dialog or renamed button breaks the run — silently if you're unlucky.

This method puts the AI at **build time**: the agent writes deterministic
code against a stable contract (an API) once. Execution is then a compiled,
versioned, testable artifact that costs nothing per run and behaves
identically at 10 operations a day or 10,000.

> **You are compiling intelligence into code. Runtime-agent tools are
> renting intelligence per execution.**

That single distinction explains the scaling gap operators feel with
personal automation tools — and why a compiled contract keeps working
long after "I automated my inbox with an agent" demos tend to quietly stop
working: a moved button doesn't break code that never looked at the
button in the first place.

## The Contract-Descent Rule

For any integration, descend to the **lowest stable contract available**:

1. **Published API** (Graph, REST, SQL) — foundation. Build here whenever
   it exists.
2. **Protocol/gateway adapter** (e.g. an EWS gateway when the ideal API is
   unavailable to you) — acceptable foundation with a tripwire-register
   entry.
3. **File/format contract** (drop folders, DXF, CSV, locked tool defaults) —
   workable; record the format's stability assumptions.
4. **Driving a GUI** (agent or automation framework clicking an app) —
   **contract of last resort.** Scaffolding by definition. Register entry
   mandatory, status WATCH, with an exit paragraph naming what you're
   waiting for (an API, a vendor change, a replacement tool).

## When Runtime Agents Are Legitimate

This is not a sneer at agentic tools. Runtime agent-driving is
**scaffolding**, and scaffolding has honest uses:

- **Validation.** Let an agent drive the tool for a week to prove the FL200
  callout is real and the workflow is right — cheapest validation there is —
  *then* build the API version of what the week taught you.
- **No contract exists.** Legacy apps, vendor portals with no API,
  undocumented formats. The only door is the UI. Use it, register it,
  watch it.
- **Genuine judgment steps.** Where a task truly needs per-execution
  reasoning (triage this ambiguous email, summarize this dispute), the
  agent belongs at run time — but as a **component with a contract**:
  structured input in, structured output out, wrapped like any other
  external dependency (doc 10). Never as the workflow's chauffeur.

## The Decision Rule (operator-judgeable)

Build against the API when **two or more** are true:

- Runs more than ~20 times a month
- Touches anything one-way-door: sending, filing, money, issued documents
- A published API exists

Frequency and consequence — no technology judgment required.

## The Role-Count Trap, Agent Edition

"The agent is the integration" is a doc-07 role-count violation: one
runtime agent acting as reader, decider, *and* actor across three tools is
one component playing every role — the SharePoint pattern again, with the
added feature of being non-deterministic. Split it: deterministic code for
reading and acting, agent-as-component for the judgment step only.

## Red Flag (added to doc 08 glossary)

> *"The agent will just handle that step."*

If the step is mechanical and recurring, "the agent will handle it" means
"nobody has designed it." Ask: which contract, what happens when it's
wrong, and who notices?

## The Meter

Run-time intelligence is also *metered* intelligence — a recurring expense
on every execution, runaway-capable by construction. Every runtime-AI
component gets a cost-ledger row, a model-tier justification ("cheapest
model that passes CP4"), prompt caching as an acceptance criterion, and a
written per-run budget enforced in code. Full treatment: doc 13.
