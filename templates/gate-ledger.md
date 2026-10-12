# GATE LEDGER — {project name}
<!-- Doc 16. One table: every binding rule, its mode, what enforces or
     traces it, and the gap. Working list for "what do we instrument next".
     A rule with no gate says so here. There is no mode called "important". -->

## Rules
1. A rule that matters names its gate in the same line. BLOCKING = a hook or
   CI check refuses. CONVENTION = leaves a checkable trace. STATED GUIDANCE =
   intent only, and says so (the default).
2. Promotion up the ladder is a logged `CONST:` decision citing an
   incident-log row.
3. A silently inert gate is worse than none. Each hook self-reports at
   session start.
4. Test a new gate by breaking the rule once and watching it fire.

## Constitution rules
| Rule | Mode today | Gate / trace | Gap and proposed instrumentation |
|------|-----------|--------------|----------------------------------|
| {no commit to default branch from the main checkout} | BLOCKING | {hook path} | {none known} |
| {push after merge} | CONVENTION | {post-merge hook flags} | {could block next call while unpushed} |
| {verify the user's own factual claims} | STATED GUIDANCE | none | {unprovable; leave as guidance} |

## Process rules outside the constitution
| Rule | Mode today | Gap and proposed instrumentation |
|------|-----------|----------------------------------|
| {sync pointer to the method repo resolves} | prose | {script: git cat-file -e <pointer>} |
| {cost-ledger "confirmed" rows foot to an itemised total} | prose | {evidence column} |

## Classification (doc 16 section 3)
Instrumentable: {n} · Human-only: {n} · Unprovable: {n} · Instrumented so far: {n}
