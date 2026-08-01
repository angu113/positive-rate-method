# FLIGHT LOG — {project name}
<!-- One line per agent session. Blameless by charter (lineage: NASA ASRS —
     near-misses are the cheapest safety data that exists). Two jobs:
     (1) calibrate estimates so the doc 13 marginal-cost claim is MEASURED,
     not asserted; (2) record what the gates caught — the method's own
     positive-rate evidence. Filling a line takes under a minute; the agent
     drafts it in the change summary, the operator confirms. -->

| Date | Package | Lane | Gate reached | Est. (from CONFIRM) | Actual | Caught this session | Halt? |
|------|---------|------|--------------|---------------------|--------|---------------------|-------|
| {date} | {name} | {G/A/R} | {CP3} | {2–4 hrs} | {3 hrs} | {CONFIRM flagged undeclared file touch} | {—} |
| {date} | {name} | {G} | {CP6} | {1 session} | {2 sessions} | {vocabulary mismatch: "quote" vs "estimate"} | {—} |

**"Caught this session" vocabulary** (use the shortest true one):
`scope-inflation` · `vocab-mismatch` · `undeclared-touch` · `shape-change-flagged`
· `above-altitude` · `estimate-miss` · `cost-surprise` · `none`

## Monthly rollup (five minutes, with the tripwire/ledger scan)
- Sessions this month: {n} · Halts: {n} · Catches: {n} ({top type})
- Estimate accuracy: {median actual/estimate} — trending {tighter/looser}
- Marginal cost of a feature this month: {median hours CP0→CP6}
  vs. three months ago: {hours} <!-- the compounding claim, measured -->

## Charter
1. The log is blameless — it records what happened, never whose fault.
2. A catch is a SUCCESS of the method, not an embarrassment. A month of
   `none` means either flawless handoffs or a log nobody is filling.
3. Three catches of the same type = a doc or constitution amendment, filed.
