# METHOD FEEDBACK — Positive Rate Method (this repo)
<!-- Findings about THE METHOD ITSELF, not about your project. (Project
     sessions → flight log; project breakage → incident log; this file →
     moments the method fought reality.) Agent-maintained: created at the
     first finding, one entry per finding, drafted by the agent and
     confirmed by the operator in a sentence.

     Export anytime: tell the agent "package feedback" — it compiles this
     file into ready-to-paste GitHub issues (and PR-ready patches where a
     proposed amendment exists) for the methodology repo. -->

**Context header (include in every packet, anonymized):**
Phase: N/A — finding raised against the methodology repo itself, not an
adopting project · Engagement level: N/A · Project shape: the methodology
repo dogfooding its own feedback loop · Method version: v0.13

## Findings
| # | Doc/Template | What happened | Class | Proposed amendment (text or "—") |
|---|---|---|---|---|
| 1 | QUICKSTART.md / docs/01-altitude-model.md (FL200) | Operator asked whether the method supports hobbyists building for personal use. The FL200 gate requires a costed callout (hours/week or $/month) to justify descent; docs/01 states plainly "if you cannot cost the callout, you are building a hobby, and you should know that before descending" — but offers no path forward for that case beyond the warning. The floor three artifacts (constitution, CONFIRM BEFORE BUILDING, CP4) are not actually business-specific and would protect a hobby project just as well, but nothing routes a hobbyist to them. | GAP | **Applied.** Added "Door C — Personal / Hobby Use" to QUICKSTART.md (keeps the three-artifact floor; replaces the costed callout with a personal appetite as the FL200 substitute; no free pass on FL100/schema-halt; excludes the doc 11 paid-consulting product since there's no business ROI to price). Added a one-line cross-reference from docs/01's FL200 paragraph pointing to Door C. |
| 2 | QUICKSTART.md / ADOPT.md / docs/12-agent-interface.md | Operator asked what happens when a new project has no version control or any other tooling standing yet, and flagged that a non-technical operator might balk at the tech-setup steps involved. Doc 12's self-gate already implies tooling choices are made silently by the agent, but nothing in QUICKSTART's greenfield door or ADOPT.md's APRON step ever mentions that a git repo (and possibly a hosting account) is about to be stood up — it would have surfaced as a surprise mid-session, not a stated expectation. There was also no standing, interrogatable record of *which* tools got stood up and why (doc 12's "record it in a comment and the change summary" is per-session and ephemeral), no lay-friendly executable runbook pattern for the one case where the operator's own identity/credentials are required, and no explicit discipline requiring the agent to verify a stood-up service is actually configured safely (private by default, least-privilege scopes, no leaked secrets) rather than taking the operator's word that they "did it." | GAP | **Applied.** New `docs/15-standing-up-infrastructure.md`: the "errand" pattern (silent by default; surfaces only when the operator's own identity is required), the runbook requirement, the tooling-inventory artifact, and a mandatory security-verification checklist (least privilege, private-by-default, no secrets in the clear, programmatic verification, verification failure = blocker not silent fix). New templates `templates/tooling-runbook.md` (with a worked Git+GitHub example) and `templates/tooling-inventory.md`. Cross-references added to ADOPT.md's APRON step + Artifact Introduction Schedule, QUICKSTART's "minimum viable method" section, and docs/12's self-gate section. |
| 3 | ADOPT.md (Step 1, APRON Step 2) | Three blind dogfood installs (context-free subagents following ADOPT.md against a hobby idea, a live ungoverned project, and an empty folder) independently surfaced that ADOPT.md never actually routes to QUICKSTART's Door C: the Phase Check never asks business-vs-personal, and APRON's callout step uses Door B's costed-callout language verbatim with no branch. One test noticed the mismatch only because it had separately read the whole QUICKSTART file; a literal-minded install would not have. | GAP | **Applied.** Step 1 now asks "is this for a business, or for yourself?" when nothing is built yet, and records which door it selects. APRON's callout step now branches explicitly across Door B / Door C / Door D instead of hard-coding Door B's language. |
| 4 | ADOPT.md (Standing Rule 2), QUICKSTART.md (Door B / Door C) | Independently surfaced by two of the three dogfood tests: Standing Rule 2 states "the artifact budget for day one is TWO files," but the Artifact Introduction Schedule (and doc 15) require the tooling inventory day one always, and doc 11 live-project adoption realistically produces 6-9 files day one (constitution, flight log, cost ledger, tooling inventory, interrogation, departure map) — "two files" is only true for a bare-minimum greenfield install and was stated with no such scope. Also: neither Door B nor Door C had a path for an operator who cannot name *any* candidate pain yet (not even a hobby want) — the rent rule's "day one ships something real or the install failed" wording has no exception for that honest case, meaning the method's own acceptance test would call a legitimate "I don't know yet" session a failure. | GAP | **Applied.** Rule 2 rescoped explicitly by phase (two files greenfield; more for live-project adoption, named as expected rather than a violation). New QUICKSTART "Door D — No Idea Yet" (install only the phase-agnostic floor, hand the operator noticing-homework instead of a shipped feature). Rent rule (Standing Rule 3) now names this exception explicitly rather than treating it as an unconditional failure. |
| 5 | templates/adoption-interrogation.md, docs/11-adopting-on-a-live-project.md, QUICKSTART.md (Door A) | A dogfood test on a live ungoverned project found a config value (`followup_days`) that looked wired up but was never actually read by the code — a real latent bug, caught only because the agent inspected the code/config directly instead of relying on the operator's description. The template's own header comment ("Business language only. No code reading.") and doc 11's matching prose read as an instruction to the *agent* not to read code, which contradicts doc 11's actual intent (and ADOPT.md's own instruction elsewhere) that the agent inspect code/config itself. A literal reading would have missed this bug. | GAP | **Applied.** Reworded the template header, doc 11's Phase 1 intro, and QUICKSTART's Door A line to say plainly: the *operator* is never asked to read code (business language only, to them); the *agent* inspects code/config directly, and that inspection is what catches findings like this one. |

**Classes:** `DOC-BUG` (practice beat the doc — amend) · `GAP` (method was
silent; agent improvised — fence it) · `FRICTION` (correct but unclear or
heavy — fix wording/weight) · `POSITIVE` (discipline earned its keep —
these matter too; they're the method's positive-rate evidence).

## Charter
1. Blameless toward the method too — findings describe what happened,
   not who wrote a bad doc.
2. The agent drafts findings AS THEY OCCUR (a one-line note in the
   change summary: "logged a method finding"), never in a batch
   reconstruction at the end.
3. Three findings of the same class against the same doc = package and
   send now; don't wait for more.
