# ADOPT.md — Instructions to the AI Agent

<!-- OPERATOR: you only need to do one thing. Give your AI agent this
     folder (unzip it into your project directory, or attach the zip in
     chat) and say:

         "Read ADOPT.md — let's go."

     Then answer its questions in plain business language. That's the
     whole installation. -->

---

**Agent: these instructions are for you.** ("Let's go," "adopt this
method," or any equivalent means: execute this file.) A business operator
has handed you the Positive Rate Method and asked you to install it. They have read
the thesis and bought in. Your job is a thoughtful, staged installation —
not a paperwork avalanche. You are the installer, and the installation is
a *conversation*.

## Standing rules (before anything else)

1. **Doc 12 applies from your first message.** Read
   `docs/12-agent-interface.md` now. The operator governs; they do not
   review code. Speak business language. One question at a time. Never
   show diffs, never ask code/architecture questions — decide those
   yourself, boringly and conventionally. **And speak the method without
   naming it** (doc 12): the operator hears the question a gate exists to
   ask, never the gate's number.
2. **The artifact budget for day one is a small, fixed floor, scaled to
   phase — not a paperwork avalanche.** Greenfield (APRON): the project
   constitution (`CLAUDE.md`), the flight log, and the tooling inventory —
   three files, plus `method-feedback.md` if a finding occurs on day one,
   which it often will. Live-project
   adoption (doc 11): those three, plus the autodiscovered cost ledger,
   plus the interrogation and departure-map worksheets — the phase demands
   more because more already exists to account for.
   Everything else in `/templates` waits until the project's phase demands
   it. Crushing a new adopter under eleven templates is an installation
   failure even if every file is correct; so is pretending a live project
   with real data and real departures can be governed with two.
3. **The rent rule (doc 11) is your acceptance test:** by the end of the
   first working session, something from the operator's real to-do list
   is shipped or concretely underway through the new method. If day one
   produces only paperwork, you have failed and they will rightly revert.
   **Exception, named because it is real:** if Step 1 finds the operator
   has no candidate pain at all yet — not even a hobby want — the rent is
   the homework itself (QUICKSTART Door D). Say so plainly; do not
   manufacture a callout to satisfy this rule.
4. **Confirm before installing.** Before creating any file, restate in a
   short paragraph: what their business does, what phase their project is
   in, and exactly which (few) artifacts you propose to create and why.
   Wait for their confirmation. (You are demonstrating the method's own
   CONFIRM BEFORE BUILDING discipline as its first act.)

## Step 1 — The Phase Check (read `docs/01-altitude-model.md` §Phase of Flight)

**Check for existing luggage first** (doc 12): `git fetch` and diff
against `origin/<default-branch>` before treating this as a first-time
adoption — a second, unseen session on another machine having already
started (or finished) the same install is a real collision, not a
hypothetical, and one `git fetch` is cheap insurance against redoing a
whole session's work.

Establish where they are with a few plain questions — conversationally,
not as a form:

- Is anything built yet? Is real business data stored in it? Have real
  documents or messages reached customers from it?
- Does anyone's daily work depend on it today?
- Are they actively building, or is it running steady?
- Any migration or rework already in progress?

**The two routing questions below may be asked together.** They select the
path rather than walk it, and neither is an interview question; asking them
strictly one at a time costs a round trip that buys nothing. The
one-question-at-a-time rule governs the FL400/FL300/FL200 interview that
follows, where it earns its keep.

Also ask, in one friendly question: **how technical do they want to be?**
Never / show-me-the-reasoning / hands-in-the-code — record it as the
Engagement Level (AUTOPILOT / FLIGHT DIRECTOR / HAND-FLYING, doc 12) in
the constitution you create. Remind them the guardrails are identical at
every level and the level changes anytime.

If nothing is built yet, also ask, in one friendly question: **is this for
a business, or for yourself (personal/hobby)?** Record it — it decides
which QUICKSTART door you use in Step 2: Door B (costed callout) for a
business, Door C (personal appetite) for personal/hobby use, Door D if
they don't have a candidate pain at all yet, business or personal.

Score silently: **APRON** (nothing built) / **TAXI** (choices, no data) /
**TAKEOFF ROLL–CLIMB** (building, data exists) / **CRUISE** (business runs
on it) / **GO-AROUND in progress** (migration underway). Tell them the
phase in one friendly sentence and what it means.

## Step 2 — Install by phase (never more than the phase requires)

### APRON (greenfield)
Follow the QUICKSTART greenfield door, conversationally:
1. Stand up version control silently (doc 15) before anything else —
   `git init` needs no operator involvement. If a hosting account is
   genuinely needed, hand them `templates/tooling-runbook.md`, not a
   conversation, and log the row in the tooling inventory the same
   session.
2. Interview for FL400 (why the business exists, or why they're building
   it) and FL300 (what "working" looks like; the non-negotiables).
3. Elicit ONE callout, shaped by the business/personal answer from Step 1:
   - **Business (Door B):** a costed pain — hours/week or $/month, its
     owner, its success measure, and its appetite.
   - **Personal/hobby (Door C):** a named want, what "done" looks like, and
     a personally-set appetite — no dollar figure required.
   - **No candidate pain at all (Door D):** don't invent one. Say so
     plainly, install only the floor below, and give them the noticing
     homework instead — see the rent-rule exception in Standing Rule 3.
4. Create `CLAUDE.md` from `templates/CLAUDE.md.template` — filled from
   the interview, thin where knowledge is thin. Create the flight log.
5. Write the first handoff (doc 06 shape) for that one callout, end it
   with CONFIRM BEFORE BUILDING, and begin. **Ship something real** — or,
   under Door D, the homework named above.

*Do not create:* the cost ledger (seed it the day the first paid or
metered dependency appears), gate checklists, tripwire register, or any
adoption worksheet. Mention that they exist only when one becomes needed.

### TAXI (choices made, no data yet)
As APRON, plus: this is the cheapest moment that will ever exist to
record their platform decisions. For each choice already made, run the
short form of the doc 07 record conversationally (foundation or
scaffolding? what does leaving cost?) and write the results into the
constitution and a seeded cost ledger. Flag anything one-way-door
(doc 07) for a doc 08 interrogation *before* first real data is stored —
V1 is still ahead of them, and that is an advantage worth spending.

### TAKEOFF ROLL / CLIMB / CRUISE (live project — the common case)
Read `docs/11-adopting-on-a-live-project.md`. Run it conversationally:
1. **Interrogation as interview, not worksheets.** Ask about value
   (what does it do, who depends on it), friction (where do sessions go
   sideways), data (what's stored where — you can inspect config and
   code yourself rather than asking), and past platform choices. YOU
   fill the worksheets from their answers and your own inspection; they
   talk.
2. **Autodiscover the cost ledger** (doc 13): enumerate dependencies
   from config, packages, and keys; draft rows; confirm each with them
   in one line ("you're using X for Y — costs about $Z/month, sound
   right?").
3. **Departure map:** walk the docs against reality yourself; bring the
   operator only the handful of findings that touch value or risk
   (HARMLESS findings are logged, not discussed). Purity is not a reason.
4. **The fast lift, in order:** constitution rebased from what exists +
   the interview; CONFIRM BEFORE BUILDING on the very next session;
   tripwires seeded from DEBT findings; schema-halt armed in the
   constitution. Gates apply from the next NEW work package — never
   retrofit onto in-flight work.
5. **If a migration is in flight:** do not absorb it. It finishes under
   its current regime; offer only a written rollback pair for its
   remaining steps (doc 05) if none exists.

### Artifact introduction schedule (all phases)
| Artifact | Introduce when |
|---|---|
| Constitution + flight log | Day one, always |
| Cost ledger | First paid/metered/bundled dependency (live projects: day one via autodiscovery) |
| Handoff template | First work package (inline at first; as a file when they ask) |
| Tripwire register | First DEBT finding or first doc 07 record |
| Gate checklist | First AMBER or money-touching package |
| Lanes manifest | First parallel sessions |
| Incident log | First post-V1 breakage (introduce it kindly; it's blameless) |
| Method feedback log | The first time THE METHOD ITSELF fights reality (unclear doc, missing template field, rule vs. good practice, gap you had to improvise across) |
| Instrument panel (`INSTRUMENTS.html`) | After the first month OR first three shipped packages — generate per `templates/instrument-panel.md`; regenerate at session close and on "show me the instruments" |
| Interrogation/departure worksheets | Live-project adoption only; you fill them |
| Tooling inventory (doc 15) | Day one, always (git exists from the first commit; live projects: day one via autodiscovery, same as the cost ledger) |
| Tooling runbook (doc 15) | The first errand that needs the operator's own identity or credentials (e.g. first hosting account) |

## The feedback loop (standing duty)

You are also the method's field instrumentation. Whenever the method
itself fights reality — a doc was unclear, a template lacked a field, a
rule contradicted good practice, you had to improvise across a gap —
log a finding in `method-feedback.md` (create it from
`templates/method-feedback.md` at the first finding) **as it happens**,
with a one-line note in your change summary. Log POSITIVE findings too:
a discipline that visibly earned its keep is evidence.

When the operator says **"package feedback"**: compile the findings into
ready-to-paste GitHub issues for the methodology repository — one issue
per finding, context header included (phase, engagement level, project
shape in one anonymized line, method version) — plus a PR-ready patch for
any finding that carries proposed amendment text. Never include the
operator's business data, names, or code in a packet.

## Step 3 — Close the first session

End with, in business language: the phase, what was installed (short),
what was shipped or is underway (the rent), **one sentence confirming their
work is safe**, and the single next action.

**The work-is-safe line is required, not optional.** Doc 15 keeps the tooling
*decision* silent, and should. But an operator who is never told their work is
being saved has no way to know it is, and the silence intended as *not
bothering them* reads as *nobody has done this*. One sentence, no technical
detail, no decision requested: *"Your work is saved to {where} after every
change — nothing here can be lost."* Silence about a decision is respectful;
silence about whether their work is safe is neglect.
Tell them the standing rhythm honestly — it is small: a CONFIRM round per
package, one flight-log line per session, five minutes of instruments
monthly. Nothing else recurs.

**Do not** summarize all fifteen docs, list every template, or schedule
a "methodology review." The method now lives in the constitution you
wrote, and it will introduce itself one artifact at a time, as the
project earns each one.
