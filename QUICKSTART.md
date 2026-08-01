# Quickstart — Day One

## The whole journey, honestly

1. **Get an agentic AI** with coding access — typically a paid plan,
   around $20/month. (That subscription is also the first row of your
   cost ledger. The method eats its own cooking.)
2. **Point it at your project** — code, docs, a data export, or nothing
   at all. Not having code yet is a phase, not a problem.
3. **Drop in this zip.** Unzip it into your project folder, or attach it
   in chat.
4. **Say: "Read ADOPT.md — let's go."**

Then answer its questions in plain business language. The agent runs the
phase check, installs only what your project's phase requires (two files
on day one, not eleven), and ships something real from your to-do list in
the first session. That is the entire installation. [ADOPT.md](ADOPT.md)
is the installer; the doors below are the manual for those who prefer to
drive.

---

Four doors. Pick yours.

## Door A — You already have a project

An AI-built (or half-built) system with business value in it, and sessions
that have started to fight you. **Most people arrive here.**

→ Go straight to [doc 11 — Adopting on a Live Project](docs/11-adopting-on-a-live-project.md).

Your day one: run the interrogation
([template](templates/adoption-interrogation.md)) — one evening, in
business language with you; the agent inspects code and config itself
rather than only asking. Day two: the departure map and the fast lift.
Your first governed session ships a real item from your to-do list, or
the lift failed.

## Door B — Greenfield

Nothing built yet. Resist the urge to open a coding session.

1. **Write FL400 and FL300** (doc 01) — purpose, one paragraph; vision and
   values, one page. An hour, honestly spent.
2. **Write one FL200 callout** (doc 01) — a named, costed pain:
   *"{who} loses {hours/week} to {what}; done means {measure}."*
   If you can't cost it, stop — you're about to build a hobby.
3. **Copy the constitution template**
   ([templates/CLAUDE.md.template](templates/CLAUDE.md.template)) into your
   new repo as `CLAUDE.md` and fill what you know. It will be thin. That's
   correct — it thickens by amendment, not by prophecy.
4. **Sketch the FL100 table** — modules × owned data × shared identifiers.
   Three rows is a fine start. This single table is what makes the
   schema-halt protocol enforceable later.
5. **Write your first handoff**
   ([templates/handoff-prompt.md](templates/handoff-prompt.md)), ending in
   CONFIRM BEFORE BUILDING. Open the session. Read the agent's restatement
   *carefully* — the first confirmation round nearly always catches a
   misunderstanding, and catching it now is the method paying rent on day one.

## Door C — Personal / Hobby Use

Building for yourself, not a business — no one's hours, no dollar figure. The
altitude model still protects you; only FL200 changes shape.

1. **Write FL400 and FL300** exactly as in Door B — purpose (why you're
   building it) and vision (what "working" looks like), one paragraph and
   one page.
2. **Replace the costed FL200 callout with a personal appetite:** name the
   want, name what "done" looks like, and set the appetite yourself — the
   time and money you're willing to spend, decided before you start. No
   hours/week or $/month figure is required; the appetite is the whole
   justification.
3. **Keep the floor.** The constitution (`CLAUDE.md`), CONFIRM BEFORE
   BUILDING, and CP4 (verify on real data) are not business-specific — they
   stop the agent from inventing decisions and catch mistakes before
   they're baked in, which you need exactly as much building alone as an
   operator does running a shop. Install all three, same as any other door.
4. **What's different from Door B:** if a hard-path problem comes up (doc
   08's boundary), the advice is the same — get real expert technical
   help for that one decision — but there's no business ROI here to weigh
   it against, so the appetite you set in step 2 is what decides whether
   it's worth it. And there is no free pass on FL100 or the schema-halt
   paragraph: data you'd hate to lose is luggage regardless of whether a
   business depends on it.

This door exists so "I can't cost it" answers a question instead of ending
the conversation.

## Door D — No Idea Yet

Nothing built, and no idea yet either — not even a hobby want. This is an
honest starting point, not a failure to have skipped.

1. **Say so plainly.** Don't invent a purpose or a pain to satisfy the
   installer; a manufactured callout is worse than no callout, because it
   sends real effort after a made-up problem.
2. **Install only the phase-agnostic mechanics:** version control (silent,
   doc 15), a constitution left explicitly thin with the gap named in
   writing ("no callout yet — FL400/FL300 pending"), and the flight log.
   Nothing else.
3. **The rent rule is waived for this session, by name.** The agent should
   say so directly: day one ships homework, not software — a short,
   concrete prompt to go *notice* one recurring annoyance over the next
   week or two, at work or at home, worth writing down the moment it's
   felt.
4. **The next session is Door B or Door C**, whichever the noticed pain
   turns out to be. Nothing above this floor gets built until then.

## The minimum viable method

At small scale you do not need all of it. The floor is three artifacts:

| Artifact | Doc | Why it's in the floor |
|----------|-----|----------------------|
| The constitution (`CLAUDE.md`) | 02 | Every session starts amnesiac without it |
| CONFIRM BEFORE BUILDING | 06 | Catches wrong builds before they exist |
| CP4 — verify with real data | 03 | The one gate no machine can run for you |

Add lanes/worktrees (doc 04) when you first run parallel sessions. Add the
full gate sheet when a package first touches money or shared data. The
schema-halt paragraph (doc 05) goes in the constitution on day one
regardless — it costs nothing until the day it saves everything.

Version control isn't on this list because it isn't optional — it exists
from your first commit, standing up silently (doc 15) under the same rule
that keeps every other tooling choice out of your way. You'll only hear
about it if a step needs your own identity or credentials (a hosting
account, say), and then it arrives as a plain runbook to work through, not
a technical decision to make.

## The one rule that outranks the rest

You govern. The agent builds. The moment a session asks you a code question
or shows you a diff, point it at the constitution (doc 12). The moment *you*
catch yourself making a business rule up mid-session, climb — that decision
belongs at FL200, in writing, before the descent resumes.
