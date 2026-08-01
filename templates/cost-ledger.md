# COST LEDGER — {project name}
<!-- Doc 13. The technical inventory with its price tags. One row per
     product/service/subscription/API the system depends on. Reviewed
     monthly alongside the tripwire register. Agent reads this every
     session; agent updates rows in change summaries when usage moves. -->

**Phase of flight:** {APRON / TAXI / TAKEOFF ROLL / CLIMB / CRUISE} · **V1 crossed:** {no / yes, {date}}
<!-- APRON = this ledger is empty and that is correct. TAXI = rows exist,
     none has data-gravity yet: cheapest moment to record everything. -->

## Autodiscovery sweep (agent-run, seeds the rows below)
<!-- The agent enumerates what the project ACTUALLY depends on — from
     config files, connection strings, SDK/package references, API keys in
     the vault, provider dashboards — and drafts a ledger row per finding.
     The operator confirms each row where session flow allows. At AUTOPILOT
     engagement level, or when live confirmation of every row would break a
     rent-first adoption session, draft the row instead with its dollar
     figure marked "estimate pending — confirm at first monthly review" —
     never silently, never entered as if confirmed when it wasn't. -->
| Found where | Dependency discovered | Drafted as row? | Confirmed? |
|-------------|----------------------|-----------------|------------|
| {app config} | {storage connection string → blob account} | {#2} | {yes / estimate pending — confirm at first monthly review} |
| {package refs} | {maps SDK} | {#3} | {yes / estimate pending — confirm at first monthly review} |
| {vault} | {AI provider key} | {#4} | {yes / estimate pending — confirm at first monthly review} |

## Inventory & running costs
| Product / service | Role(s) it plays | Tier / plan | Upfront | $/month now | Free-tier / band cliff | $/month at 5× volume | RUNAWAY-CAPABLE? | Cap/alert set? | Tripwire | Decision record |
|---|---|---|---|---|---|---|---|---|---|---|
| {M365 subscription} | {SharePoint storage, Entra auth} | {Business Std, already owned} | {$0 marginal} | {$0 marginal} | {5,000-item list threshold} | {$0 — but see exit} | no | n/a | {items > 3,000} | {doc-07 record link} |
| {Azure Blob Storage} | {document storage} | {Hot LRS} | {$0} | {<$1} | {pricing band at 50 GB} | {~$4} | no | n/a | {40 GB} | {link} |
| {Maps/routing API} | {delivery routing} | {free tier} | {$0} | {$0} | {N calls/month} | {$?} | **yes** (per-call) | {quota cap ON} | {80% of free calls} | {link} |
| {AI runtime component} | {judgment step in workflow X} | {model: {tier} — cheapest passing CP4} | {$0} | {$…} | {n/a — metered} | {$…} | **yes** (per-run, loop risk) | {per-run budget in code + provider cap} | {$…/month} | {link} |
| {SMS provider} | {customer messaging} | {campaign plan} | {$…} | {$…} | {n/a — per message} | {$…} | **yes** (per-message) | {alert at $…} | {msgs/month > …} | {link} |

## Bundled / already-owned assets in play
<!-- Subscriptions the business already pays for whose spare capacity the
     system rides. Marginal cost near zero is recorded honestly — and so is
     the exit paragraph. Both numbers, side by side. -->
| Asset | Spare capacity used | Marginal cost | Exit cost (from doc 07 record) |
|---|---|---|---|
| | | | |

## Cost events log
<!-- Newest first. Every change-summary cost announcement lands here. -->
| Date | Package | What moved | Before → after $/mo | Cliff distance |
|---|---|---|---|---|
| | | | | |

## Monthly review (with tripwire register)
- [ ] Read each row's actual spend vs. ledger figure — investigate any gap
- [ ] Check volume against each cliff and tripwire
- [ ] Verify every RUNAWAY-CAPABLE row still has its cap/alert live
- [ ] Total $/month: {sum} — vs. value of callouts served: {sum from FL200}
