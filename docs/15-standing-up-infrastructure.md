# 15 — Standing Up Infrastructure Safely

Every project needs some infrastructure to exist at all — version control, a
place to host it, maybe a package manager or a cloud account. Doc 12's
self-gate already settles who decides this: these are code-shaped choices
("boring conventional option, decide, don't ask"). But doc 12 doesn't cover
one specific moment — where an account or identity can only be created *by
the operator*, because it's tied to their name, their email, their payment
method. That moment is not a decision, it's an **errand** — and it needs its
own procedure, because "figure it out yourself" is exactly where a lay
operator loses confidence and closes the laptop.

## The Errand Pattern

An **errand** is any setup step that requires the operator's own identity,
credentials, or consent, and cannot be performed by the agent on their
behalf — creating a hosting account, provisioning a cloud subscription,
installing software that needs admin rights on their machine. This is
distinct from ordinary tooling decisions (`git init`, `.gitignore`, branch
naming), which stay fully silent under doc 12's self-gate and never reach
the operator at all.

When, and only when, an errand is required, the agent:

1. **Names it in one plain sentence** — what it is, why it's needed, roughly
   how long it takes.
2. **Hands the operator a runbook**, not a conversation.
3. **Never asks the operator to make a technical choice inside the errand** —
   the agent has already decided the boring/conventional option ("GitHub,"
   not "pick a git host"); the errand is pure execution.

## The Runbook

Every errand ships as a filled instance of `templates/tooling-runbook.md`:
plain language, numbered, executable steps, each with an expected result the
operator can literally see and check off. No step assumes prior knowledge.
The runbook is a worksheet to complete in one sitting, not documentation to
browse.

Template: [`/templates/tooling-runbook.md`](../templates/tooling-runbook.md)

## The Tooling Inventory

Every tool or service the project depends on — however it was chosen — gets
one row in a standing, interrogatable log: what it is, why it was chosen,
who decided (agent-silent under doc 12, or an operator errand under this
doc), its foundation/scaffolding classification (doc 07, if it plays a
one-way-door role), and its security-verification status. This is the
aggregated record doc 12's per-session "record it in a comment and the
change summary" was always missing — those entries are ephemeral and
scattered across sessions; this is where they accumulate into something the
operator, or a future session, can actually query.

Template: [`/templates/tooling-inventory.md`](../templates/tooling-inventory.md)

Introduced day one at APRON (git exists from the first commit) and via
autodiscovery for live-project adoption (doc 11) — same cadence as the cost
ledger.

## Security Verification — Mandatory, Not Optional

An operator handed a runbook and told "click here, sign up there" cannot be
expected to spot a misconfigured service. That responsibility does not
transfer to them just because they clicked the buttons — it stays with the
agent, discharged programmatically, every time:

1. **Least privilege by default.** Any scoped token, key, or permission
   grant is requested at the narrowest scope that does the job — never
   "owner" or "admin" because it was easier to click. If the setup flow
   defaults to a broad scope, the runbook explicitly narrows it before
   finishing.
2. **Private by default.** Any new repository, storage bucket, or service
   defaults to private/restricted visibility. Public is an explicit, named
   decision with a business reason — never an accident of accepting
   defaults.
3. **No secrets in the clear.** Nothing that authenticates (tokens,
   passwords, connection strings) is ever pasted into chat, written into a
   committed file, or left in a runbook's output. The agent watches for this
   the same way it watches for schema drift — a standing check, not a
   one-off reminder.
4. **The agent verifies the result programmatically — never takes "done" on
   faith.** After the operator completes a runbook step, the agent checks
   the actual outcome via CLI/API (repo visibility, token scope, whether a
   test push succeeds, whether the expected files/config exist) before
   marking the errand complete. "I clicked through it" is not verification.
5. **Verification failure is a blocker, not a silent fix.** If a check comes
   back wrong — public when it should be private, wider scope than
   requested, a secret found somewhere it shouldn't be — the agent stops,
   names the specific finding in plain language, and proposes the fix. It
   does not quietly patch it and move on (that would hide a mistake that
   might recur), and it does not ask the operator to diagnose it (that
   violates doc 12's self-gate).

Every verification outcome — pass or fail, and what was done about a
failure — is recorded in the tooling inventory row for that tool.

## Where This Sits

This document does not replace doc 07 (platform decisions) or doc 12 (agent
interface) — it is the connective tissue between them for the specific,
recurring moment of *standing something up for the first time*. A tool that
later grows into a one-way-door platform choice graduates into a full doc 07
decision record; the tooling inventory row simply gains a link to it, the
same way a cost ledger row does.
