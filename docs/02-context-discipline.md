# 02 — Context Discipline: The Project Constitution

Every AI-agent session starts amnesiac. Context discipline is the practice of
maintaining one authoritative file — by convention `CLAUDE.md` at the repo
root — that reconstitutes the project's identity at the start of every session.

Call it the **constitution**: it constrains every session, it is amended
deliberately, and it outranks anything said inside a session.

## What Belongs in the Constitution

Ordered by how expensive it is when the agent doesn't know it:

1. **Standing constraints (from FL300 values).**
   *"All secrets come from Key Vault — never hardcode, never .env."*
   *"Installer must never require elevation."*
   *"Every ERP document number is immutable once issued."*
2. **Domain vocabulary.** The terms of your trade, defined once. In a metal
   shop: what T&C means, what an HSK# is, what a heat number is. The agent
   writing plausible-but-wrong domain logic is the most common failure in
   operator-built software, and vocabulary is the cheapest prevention.
3. **Architecture facts.** Stack, module map (from FL100), data ownership
   table, identifier schemes, naming conventions.
4. **Process rules.** The gate system, the schema-halt protocol, the handoff
   format — stated as binding instructions to the agent.
5. **Environment facts.** Where things run, what the agent may and may not
   touch, how to build and test.

## What Does NOT Belong

- Session-specific instructions (those go in the handoff prompt)
- Aspirations ("we should eventually...") — constitutions are law, not roadmap
- Anything you aren't willing to enforce at a gate

## Amendment Protocol

The constitution changes by **explicit amendment, never by drift**:

1. A session may *propose* an amendment when it hits a contradiction.
2. The operator reviews and commits the amendment as its own commit,
   message prefixed `CONST:`.
3. All active lanes are notified (in practice: the manifest is touched and
   parallel sessions re-read the constitution — see doc 04).

The `CONST:` commit history becomes the project's legislative record. When
onboarding a human developer months later, this history answers "why is it
like this?" better than any wiki.

## The Onboarding Dividend

A maintained constitution is also your human onboarding document. In practice:
a new developer joining a constitution-disciplined project is productive in
days, because the same file that governs the agent explains the project to a
person. You are not writing documentation *and* prompts — they are the same
artifact.

## Smells

- **The constitution hasn't changed in a month of active work.** Either the
  project learned nothing (unlikely) or learning is leaking into session
  memory and dying there.
- **The constitution is over ~3 pages of prose.** Move detail into linked
  docs; the constitution holds rules and pointers, not essays.
- **You're re-explaining the same fact in handoff prompts.** That fact is
  constitutional. Amend.
