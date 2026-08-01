# HANDOFF — {package-name}
<!-- CP2 artifact. One package, one lane, one handoff. -->

## 1. CALLOUT
{Paste the FL200 callout verbatim, including cost and success measure.}

## 2. LANE
- Class: {GREEN | AMBER | RED}
- Worktree: {../wt/package-name}
- Locks declared: {files/artifacts, or "-"}
- You may NOT touch: {explicit exclusions}

## 3. CURRENT STATE
{What exists now and where. Point into the constitution — don't repeat it.}

## 4. REQUIRED CHANGE
**In business terms:** {what the operator will be able to do that they can't now}

**In technical terms:** {the operator's best understanding — the agent should
correct this in its confirmation if it's wrong}

## 5. NON-GOALS
- {Explicitly out of scope}
- {No refactors beyond the files listed}
- {No dependency additions without surfacing first}

## 6. ACCEPTANCE (CP4 test)
{Concrete steps the operator will perform with real data, and what they
expect to see. The agent self-checks against this at CP3.}

## 7. CONFIRM BEFORE BUILDING
<!-- Interface reminder (doc 12): the confirmation below is answered in
     business terms. No diffs, no code questions to the operator — code
     decisions are made in-session per constitution rule 7. -->
Before writing any code: restate the task in your own words, list every
assumption you are making, list every file you expect to touch, and flag
anything that looks like a data-shape change or a decision above your
altitude. Estimate the effort to done as a range (sessions/hours) and
state the run-cost delta: any new or changed recurring cost this package
introduces, with advertised pricing — or the word "none". Wait for my
confirmation.
