# TOOLING INVENTORY — {project name}
<!-- Doc 15. One row per tool/service the project depends on for its
     existence as a project — version control, hosting, package manager,
     CI, cloud accounts. Distinct from the cost ledger (doc 13, money)
     and the tripwire register (doc 08, growth limits): this is the
     record of WHAT was stood up, WHY, WHO decided, and whether it was
     verified safe. Introduced day one at APRON (git always exists from
     the first commit); autodiscovered for live-project adoption
     (doc 11), same cadence as the cost ledger. -->

**Phase of flight:** {APRON / TAXI / TAKEOFF ROLL / CLIMB / CRUISE}

## Inventory
| # | Tool/service | Role it plays | Chosen because (one line) | Decided by | Foundation/scaffolding (doc 07 link) | Runbook | Security verification | Date added |
|---|---|---|---|---|---|---|---|---|
| 1 | {Git} | version control | {every project needs a saved history; boring/conventional default} | agent (silent, doc 12) | n/a — two-way, internal tooling | n/a | n/a | {date} |
| 2 | {GitHub, private repo} | hosting the repo | {free, ubiquitous; operator's own account} | operator errand (doc 15) | scaffolding — two-way, swappable host | {templates/tooling-runbook.md — Git+GitHub} | {pass, date} | {date} |
| 3 | {…} | | | | | | | |

**Decided by** values: `agent (silent, doc 12)` — a boring/conventional
choice that never reached the operator · `operator errand (doc 15)` — a
setup step only the operator could perform · `operator decision` — a
genuine business-facing choice they made directly.

## Monthly review (fold into the same ritual as the cost ledger and tripwire register)
- [ ] Any row still showing an unverified or failed security check?
      Resolve before moving on.
- [ ] Any row whose role has grown (doing more than it was chosen for)?
      Flag for a doc 07 record if it doesn't have one yet.
