# 08 — Governing Above Your Expertise

An honest limitation, stated plainly: parts of this method were developed by
an operator who is also a trained developer and enterprise architect. Some
FL100 calls — when a platform needs to pivot, when "agile now" becomes
"trapped later" — drew on that training. **A methodology that only works if
you secretly have twenty years of architecture experience is not a
methodology; it's a biography.**

This document is the answer. The claim is *not* that a playbook can install
architectural judgment. It can't. The claim is the one every safety-critical
field has already proven: **expertise transfers as procedure, not as
intuition.** Aviation didn't make pilots into aeronautical engineers — it
gave them checklists and instrument thresholds. Medicine didn't make triage
nurses into diagnosticians — it gave them protocols that define *when to
escalate.* The lay operator does not make architecture calls. **They govern
them** — the way a good board member governs a CTO: written decisions,
watched numbers, known escalation points.

Three mechanisms.

## 1. The Tripwire Register

Every platform decision record (doc 07) feeds a single running register —
the operator's instrument panel. Each row: the decision, its published
limits, its role count, its review triggers *in business units the operator
already tracks* (documents/month, headcount, integrations, stored records).

The operator's entire recurring duty is: **once a month, read the numbers
they already know against the triggers, and re-open any record that trips.**
No technology evaluation. No architecture opinion. The expert's skill of
"knowing when to worry" is exactly what the register proceduralizes.

Template: [`/templates/tripwire-register.md`](../templates/tripwire-register.md)

## 2. The Architect's Interrogation

The leverage that changed everything: **the operator has an architect on
tap — the agent itself.** What the layperson lacks is not access to
expertise; it's knowing *which questions to ask.* So the questions are
codified into a standing ritual, run against any proposed platform choice or
any tripped register row:

1. What are this platform's **published hard limits**, and where does our
   current growth put us against each one in 24 months?
2. How many **architectural roles** would this component play? Name each.
3. What does **exiting** cost — in dollars and weeks — and what would
   replace it?
4. What in this design **must never be inconsistent or duplicated** (money,
   document numbers, identity), and what *specifically* guarantees that?
5. If we grow 5×, **what breaks first?**
6. Is this a **one-way or two-way door**, and why?
7. What does this **cost** — upfront, per month at today's volume, and at
   5× — where are the **free-tier cliffs**, and is any part of it
   **runaway-capable** (metered per use, unbounded by decisions)? (Doc 13.)

**The binding rule: every answer must be given in business terms, or the
answer is rejected and re-asked.** The operator cannot judge "eventual
consistency." The operator can absolutely judge *"there is a small chance
two customers receive the same invoice number."* Forcing the translation is
the entire trick — it converts an architecture review into a business-risk
review, which is a thing operators already do every day.

Run it against more than one agent session (or one agent and one human) for
anything classified as a one-way door. Disagreement between answers is
itself a finding.

Template: [`/templates/architects-interrogation.md`](../templates/architects-interrogation.md)

## 3. The Red-Flag Glossary

A short list of phrases that mean **escalate to a human expert now**,
regardless of how confident the source sounds. The operator doesn't need to
understand them — only to recognize them, the way a shop hand recognizes the
smell of an overheating motor without being an electrician:

- *"We can migrate that later."* (Later is a price. Demand the number today.)
- *"We'll denormalize for now."* / *"We'll keep a copy in both places."*
  (Two copies of one fact is a standing bet that they'll never disagree.)
- *"This component can also handle X."* (Role count just went up. Re-run doc 07.)
- *"That limit is theoretical."* (Limits are published because someone hit them.)
- *"It's eventually consistent, which is fine here."* (Fine is a business
  judgment. Whose?)
- *"We'll enforce uniqueness in the application."* (Uniqueness enforced
  anywhere except the data layer is a suggestion, not a guarantee.)
- *"The agent will just handle that step."* (If it's mechanical and
  recurring, "the agent handles it" means nobody designed it. Which
  contract? What happens when it's wrong? See doc 09.)
- *"I've made this extensible for future flexibility."* (Flexibility no
  written callout demanded is scope inflation wearing a suit. See doc 10.)
- *"Let's just try it and see."* — **when the agent proposes it.** That is the
  agent spending your time to run its experiment. Ask what it expects to
  happen and why; if the answer is a guess, the next step is reading the
  documentation, not another attempt. (Doc 12; doc 03 halt conditions.)

Any red-flag hit on a **one-way door** decision is an automatic escalation.

## The Honest Boundary

Procedure covers most of the distance. It does not cover all of it. There is
a residue of genuine judgment calls — perhaps one decision in twenty — where
the register has tripped, the interrogation answers conflict, and the door
is one-way. **The method's instruction for that case is not "apply the
framework harder." It is: hand the controls to a real human expert for that
one decision.** Weighed against a five-figure exit cost, bringing in real
expert technical help for the one decision that actually needs it is the
best trade in the whole method.

A framework that pretends it has no boundary is consultancy-ware. This one
publishes its boundary, and that is precisely why the other 95% can be
trusted.

## Procedure Isn't Only for the Inexperienced

This document is written for an operator who lacks the expertise to make
architecture calls alone — but an operator who *does* bring real technical
judgment should not read that as license to skip the register. The two
things do different jobs (doc 01, "Two Ways to Fail"): personal expertise
is the faster, cheaper catch for the slow kind of failure — drift, scope
creep, a decision that quietly stopped being the right one. It is a poor
defense against the other kind: the single catastrophic action that
doesn't feel wrong in the moment, because those don't discriminate by
skill level. The disaster earlier in this document was built by
engineers, not amateurs.

An experienced operator running this method should expect the tripwire
register and the interrogation to catch less, more rarely, than a novice
would need them to — that's real, earned reduction in procedural load, not
a reason to skip them. What they still catch, expertise or not, is the
one-way door that looked fine in the moment it was walked through. **No
track record of avoided incidents proves the guardrails were unnecessary;
it proves the combination hasn't yet met its worst day.**
