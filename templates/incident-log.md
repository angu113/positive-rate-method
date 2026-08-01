# INCIDENT LOG — {project name}
<!-- Post-V1 breakage record. Blameless by charter (lineage: SRE postmortem
     culture — failure is studied, not punished). Postmortem-LITE: five
     fields per incident, one required output. If it takes more than half a
     page, it's a go-around plan, not a log entry. -->

## Incident {n} — {short name}, {date}
| Field | Entry |
|-------|-------|
| **What broke, in business terms** | {e.g. quotes issued Tue AM carried the wrong tax rate} |
| **Blast radius** | {n documents / customers / records touched; from the audit trail, not memory} |
| **Recovery** | {what was done, how long to restored service, rollback used?} |
| **Which discipline would have caught it** | {e.g. CP4 skipped on a "trivial" change — doc 03's exact warning} |
| **Amendment made** | {CONST: commit ref / doc issue filed / written "no change because…"} |

## Charter
1. Blameless. The log records conditions and procedures, never fault —
   the operator following a bad procedure is a procedure problem.
2. Every incident produces exactly one of: a constitution amendment, a
   methodology issue, or a *written* decision that no change is warranted.
   Silence is the only prohibited outcome.
3. "Which discipline would have caught it" is answered honestly even when
   the answer is "none" — that's a finding against the method itself, and
   it gets filed upstream (CONTRIBUTING.md).
4. Recovery drills: once a quarter, pick a past incident and re-verify the
   rollback path still works. CP6 asked "can I get back?" — this is the
   only proof the answer stayed yes.
