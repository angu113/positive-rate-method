# TOOLING RUNBOOK — {tool/service name}
<!-- Doc 15. One filled instance per errand — a setup step only the
     operator can perform (their identity, their credentials, their
     payment method). Plain language, numbered, executable steps. No
     step assumes prior knowledge. The agent verifies the result
     programmatically before marking this complete — see Verification
     below. -->

**Why this exists:** {one plain sentence — what pain this removes, why
it's needed for the project}
**Time required:** {honest estimate, e.g. "10 minutes, one sitting"}
**What you need before starting:** {e.g. an email address; a payment
method if a paid tier is chosen; nothing else}

## Steps
| # | Do this | You should see | Done? |
|---|---------|-----------------|-------|
| 1 | {exact action — click path or exact command, no unexplained jargon} | {exact expected result — screen, message, output} | [ ] |
| 2 | … | … | [ ] |

## Security checklist (agent-verified, not operator-verified)
| Check | Expectation | Verified how | Result |
|-------|------------|---------------|--------|
| Scope/permissions | Narrowest scope that does the job — never owner/admin by default | {CLI/API call used} | {pass/fail} |
| Visibility | Private/restricted by default unless a business reason requires public | {CLI/API call used} | {pass/fail} |
| Secrets handling | Nothing that authenticates appears in chat, commits, or runbook output | {scan used} | {pass/fail} |
| Functional check | The thing actually works as intended (not just "exists") | {concrete test performed} | {pass/fail} |

**If any check fails:** stop here. Name the finding in plain language,
propose the fix, and do not mark this runbook complete until every row
reads pass.

## Sign-off
Completed: {date} · Verified by agent: {yes/no} · Logged to tooling
inventory: {row #}

---

## Worked example — Git + GitHub (the first errand almost every project needs)

**Why this exists:** every session needs a place to save your work so
nothing is lost between sessions, and so the agent can track changes
safely. Git is the tool; GitHub is where your copy lives online.
**Time required:** about 10 minutes, one sitting.
**What you need before starting:** an email address. A free GitHub
account is enough — no paid plan required for a private repo.

| # | Do this | You should see | Done? |
|---|---------|-----------------|-------|
| 1 | Go to github.com and click "Sign up." Use the email you check most. | A welcome screen asking you to verify your email. | [ ] |
| 2 | Verify your email from the link GitHub sends you. | Your GitHub account dashboard. | [ ] |
| 3 | Click the "+" in the top right → "New repository." Name it after your project. **Set visibility to Private.** Leave every other box unchecked. Click "Create repository." | A page showing an empty repository with a URL like `github.com/you/project-name`. | [ ] |
| 4 | Paste that repository's URL to the agent in chat — nothing else needed from you. | The agent confirms it can see the repository. | [ ] |

(Everything past step 4 — connecting the local project, first commit, first
push — is a boring conventional decision under doc 12; the agent does it
silently and reports only the result.)

**Security checklist (agent-verified):**
| Check | Expectation | Verified how | Result |
|---|---|---|---|
| Scope/permissions | Repo access uses the operator's own login — no separate token created unless a later step needs one, and if so, scoped to that repo only | ownership/scope check via API or CLI | pass |
| Visibility | Repository is Private | visibility check via API or CLI | pass |
| Secrets handling | No credentials appear in the chat transcript or in any committed file | scan of first commits for common secret patterns | pass |
| Functional check | Agent can push to and pull from the repository | test push of an initial commit | pass |

This worked example is what "verify programmatically" looks like end to
end — not a promise, an actual command run and its actual output checked.
