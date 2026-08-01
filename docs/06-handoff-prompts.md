# 06 — Structured Handoffs & CONFIRM BEFORE BUILDING

A handoff prompt is the CP2 artifact: the complete, written transfer of one
work package from operator to agent. It is not conversation — it is a work
order, and it has a fixed shape so that writing one takes minutes and
reviewing the agent's response takes seconds.

## The Handoff Shape

Seven sections, always in this order (template in `/templates/handoff-prompt.md`):

1. **CALLOUT** — the FL200 callout this serves, verbatim, with its success
   measure. The agent should be able to argue *from* the callout when it hits
   an ambiguity.
2. **LANE** — the CP1 classification and declared locks. The agent is told
   what it may not touch as explicitly as what it may.
3. **CURRENT STATE** — what exists now, where, and what's known-good about
   it. Pointers into the constitution rather than repetition of it.
4. **REQUIRED CHANGE** — the change, in business terms first, technical
   terms second. Business terms first is deliberate: it lets the agent catch
   the operator's technical misconceptions instead of faithfully implementing them.
5. **NON-GOALS** — explicitly out of scope. This section does more work than
   any other. Agents fill vacuums; non-goals remove the vacuum.
6. **ACCEPTANCE** — how CP4 will be tested, stated concretely enough that
   the agent can self-check at CP3.
7. **CONFIRM BEFORE BUILDING** — the closing instruction, always verbatim:

   > Before writing any code: restate the task in your own words, list every
   > assumption you are making, list every file you expect to touch, and flag
   > anything that looks like a data-shape change or a decision above your
   > altitude. Estimate the effort to done as a range (sessions/hours) and
   > state the run-cost delta: any new or changed recurring cost this
   > package introduces, with advertised pricing — or the word "none"
   > (doc 13). Wait for my confirmation.

## Why the Confirmation Round Matters

The confirmation reply is where the method earns its keep. The operator is
not reviewing code (can't, reliably) — they are reviewing **restated intent
and assumptions**, which any competent operator can judge. In practice the
confirmation round catches, in order of frequency:

1. Vocabulary mismatches (the agent means something different by a domain term)
2. Undeclared file touches that would violate a lock
3. Scope inflation ("I'll also refactor...")
4. Hidden shape changes ("I'll add a column to track...") → halt, doc 05
5. Genuine ambiguities in the operator's own thinking

Item 5 is the quiet one: the confirmation round is where the *operator*
discovers their FL200 callout was underspecified — an ascent, caught before
it cost a build.

## Rules of Engagement Mid-Session

- **New requirements discovered mid-build do not enter the session.** They
  become new FL050 packages. The current package finishes to its CP2 spec or
  returns to CP2 amended — never mutates silently.
- **The agent's questions are answered in writing in the session,** and any
  answer that states a durable fact gets promoted to the constitution at CP5.
- **A session that stops confirming and starts assuming is ended,** and the
  package restarts at CP2 with a tightened handoff. Sessions are cheap;
  drift is not.

## The Compounding Effect

Handoffs get shorter over the life of a project — not because discipline
relaxes, but because sections 2, 3, and 5 increasingly reduce to constitution
pointers. A mature project's handoff is often half a page. This is the
measurable form of the method's economic claim: the marginal cost of a
feature converges on the cost of writing its CALLOUT and NON-GOALS.
