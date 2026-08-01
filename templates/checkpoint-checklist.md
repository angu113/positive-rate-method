# CP0–CP6 GATE CHECKLIST — {package-name}
<!-- One sheet per package. Date each gate as it passes. -->

| Gate | Question | Pass criteria | Date |
|------|----------|--------------|------|
| CP0 | Which callout? | Written FL200 callout with cost + success measure | |
| CP1 | Whose data, what lane? | Module owner identified; lane classified; locks declared if AMBER; halt scheduled if RED | |
| CP2 | Does the restatement match intent? | Handoff written; agent confirmed; assumptions corrected | |
| CP3 | Did it build only what CP2 authorized? | Compiles; agent tests pass; change summary matches handoff | |
| CP4 | Positive rate? (does it remove the costed pain?) | Operator verified with REAL data against acceptance steps | |
| CP5 | Is any other lane touching this? | Manifest checked; merge order respected; locks released; CONST: amendments committed | |
| CP6 | Can I get back if it breaks Monday? | Deployed via standard path; audit record present; rollback known | |

## Constitution non-negotiables (checked at CP3)
<!-- One row per non-negotiable that names a producible artifact (doc 12
     rule 9) — a test, a written note, a required field, an admin gate.
     "Agent tests pass" only proves the suite didn't regress; this table
     proves each specific non-negotiable was actually honored by THIS
     package. Status from a closed set only: Yes / No — miss, reason / N/A / Partial. -->
| Non-negotiable | Status |
|---|---|
| {e.g. bug fix ships its own regression test} | |

## Halt log
{Any halt triggered by this package: trigger, date, resolution.}

## Notes
{Anything learned worth promoting to the constitution.}
