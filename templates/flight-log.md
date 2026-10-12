# FLIGHT LOG — {project name}
<!-- One row per unit of WORK (a work item or PR), not per session: with
     parallel agents and a fleet, a session is not a unit (doc 17). Row cap:
     about 600 characters. Detail goes in the PR or the change summary, and the
     row links to it. Blameless by charter (lineage: NASA ASRS —
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
· `above-altitude` · `estimate-miss` · `cost-surprise` · `falsified-hypothesis` · `none`

`falsified-hypothesis` covers a result that surprised the agent without
breaking anything — "we expected X, observed Y," corrected before it
shipped. Not a catch of a mistake in progress and not an incident (that's
`incident-log.md`'s job); just a wrong expectation, worth a line for the
same reason a catch is: a pattern across several is data the method can
act on, and it evaporates the moment it's silently corrected in-session.

## Monthly rollup (five minutes, with the tripwire/ledger scan)
- Rows this month: {n} · Halts: {n} · Catches: {n} ({top type})
- Catches by type: {type: n, ...} <!-- COUNT them. Three of one type = an
  amendment (charter 3), and nothing triggers that unless someone counts. -->
- Engagement level still right? {from the kind of work in the rows} (doc 12)
- Estimate accuracy: {median actual/estimate} — trending {tighter/looser}
- Marginal cost of a feature this month: {median hours CP0→CP6}
  vs. three months ago: {hours} <!-- the compounding claim, measured -->

## Charter
1. The log is blameless — it records what happened, never whose fault.
2. A catch is a SUCCESS of the method, not an embarrassment. A month of
   `none` means either flawless handoffs or a log nobody is filling.
3. Three catches of the same type = a doc or constitution amendment, filed.
   The monthly rollup counts them, because nothing else will.
4. Est. says a number and a reason, or says "not estimated" and why. A column
   filled with "~1 session" or "not estimated" measures nothing, and the
   doc 13 marginal-cost claim then rests on nothing.
5. Keep the table together. Append rows directly under the header row, above
   the rollup. Rows appended below the rollup are orphaned from the header.
6. Measured on one project (152 rows): median row 2,028 characters, 39 over
   3,000. A log nobody can scan is a log nobody reads, so the cap is part of
   the charter, not a style note.
