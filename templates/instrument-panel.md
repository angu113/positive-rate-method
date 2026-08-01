# THE INSTRUMENT PANEL — generation spec (agent-facing)
<!-- The operator's flight instruments: a visual, business-language view
     of progress, generated from the project's logs. The operator says
     "show me the instruments" (or you regenerate at session close once
     it exists). This file is the SPEC — you build the panel fresh each
     time. Introduce it after the first month OR first three shipped
     packages, whichever comes first; an empty cockpit teaches nothing. -->

## Hard rules

1. **One self-contained file: `INSTRUMENTS.html`** at the project root.
   Everything inline — styles, any charting drawn as inline SVG. **Zero
   external dependencies, zero network requests, zero scripts that call
   out.** It must open from a double-click, offline, forever. No operator
   data may leave the machine.
2. **The logs are the only source of truth.** Read the flight log, cost
   ledger, tripwire register, LANES.manifest, gate checklists, FL200
   callouts, and constitution. The panel is a disposable VIEW — never a
   second data store, never hand-edited, always safe to delete.
3. **Business language only.** "Pain removed," "cost to run," "features
   this month," "hours per feature." Never: velocity, burn-down, sprint,
   KPI, or any term the operator didn't use first.
4. **Honest gauges.** No vanity framing. If hours-per-feature trended up
   this month, the needle shows it. If a tripwire is amber, it is amber
   at the top of the page. The panel exists to be trusted, and one
   flattering lie ends that.

## The six-pack (in this layout order)

1. **POSITIVE RATE (vertical speed) — the centerpiece, top and largest.**
   Value delivered vs. cost to run: total $/month (or hrs/week) of served
   callout pain, against total $/month from the ledger. One big
   climbing/level/descending needle and one sentence:
   *"Removing ~$X/month of pain for $Y/month of running cost."*
2. **AIRSPEED** — median hours per shipped feature, this month vs. prior
   months, as a small trend line. Caption when true: *"Features are
   getting cheaper to add."* (The compounding claim, drawn.)
3. **ATTITUDE** — packages currently in flight: name, lane color, gate
   position CP0→CP6 as a horizontal progress strip. Level = advancing;
   a HALT banks the display and says why in one line.
4. **HEADING** — the current callout, quoted in the operator's own words
   from FL200, with its success measure and appetite remaining.
5. **FUEL** — $/month burn from the ledger, the nearest cliff and its
   distance in the operator's units (*"next storage price band: ~6 years
   away at current growth"*), and any RUNAWAY-CAPABLE row's cap status.
6. **ANNUNCIATOR ROW** — small lights: tripwires (green/amber per row),
   halts this month, catches this month (from the flight log — shown as
   the good news it is: *"the gates caught 3 things before they cost
   anything"*), incidents open.

Footer, small print: phase of flight, V1 date, method version, generated
timestamp, and *"Generated from your project's logs — safe to delete,
regenerates on request."*

## Style

Clean, calm, print-friendly. Dark-panel cockpit aesthetic is welcome but
legibility outranks theme. Large type for the six headline numbers — the
operator should absorb the whole panel in ten seconds from across a shop
counter. Degrade gracefully: a gauge with no data yet says *"no data yet
— first entries appear after {trigger}"* rather than showing zeros.

## What this is not

Not a task manager, not an editor, not interactive beyond viewing (links
into the underlying .md files are fine). Interaction stays in
conversation with the agent; the panel is for SEEING. If the operator
asks for controls, the answer is: "tell me, and I'll do it — the panel
will show it done."
