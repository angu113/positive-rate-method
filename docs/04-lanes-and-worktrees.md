# 04 — Lane Classification & Parallel Worktrees

The productivity claim of this method rests on parallelism: multiple AI-agent
sessions working simultaneously, each in its own **git worktree**, without
stepping on each other. Parallelism is only safe when work is classified by
risk *before* it starts.

## Lane Classes

Every work package is classified at CP1 into exactly one lane class:

| Lane | Definition | Parallelism rule |
|------|-----------|------------------|
| **GREEN** | Touches only its module's own code; no schema, no shared identifiers, no cross-module contracts | Unlimited parallel lanes |
| **AMBER** | Touches a shared contract (API surface, shared component, document template, identifier format) but not stored data shape | Parallel with GREEN; exclusive lock on the shared artifact |
| **RED** | Touches data shape: tables, columns, stored file formats, migration of any kind | **Solo. No other lane runs.** Triggers schema-halt entry conditions (doc 05) |

Classification is a judgment call the operator makes with a one-question test:
*if this package is wrong, what else breaks?* Only its own screen → GREEN.
Another module's behavior → AMBER. Data already stored → RED.

**Misclassification bias:** when unsure, classify up. A GREEN treated as AMBER
costs a lock. An AMBER treated as GREEN costs a weekend.

## Worktree Mechanics

- One worktree per active lane, named for the package
  (`../wt/chip-email-templates`), branched from mainline.
- Each session is opened *inside its worktree* and reads the constitution
  first — the constitution is the same file in every worktree by design.
- Sessions never touch files outside their worktree. The agent is told this
  in the constitution's process rules; the operator enforces it at CP3 by
  reading the change summary.

## The Manifest and Locks

Two small files at mainline root coordinate the lanes:

**`LANES.manifest`** — the flight board. One line per active lane:
```
chip-email-templates   AMBER  CP3  locks: EmailChipControl.xaml
audit-table-viewer     GREEN  CP4  locks: -
```

**Lock rules:**
1. An AMBER lane declares its locked artifacts in the manifest *before* CP2.
2. No lane may enter CP2 if its declared files intersect an existing lock.
3. Locks release at CP5 (merge), never earlier — "I'm basically done" is not CP5.
4. A RED lane's lock is the whole repository. The manifest shows only the RED
   line while it runs.

The manifest is committed like any file, which gives you a historical record
of what ran in parallel with what — invaluable when diagnosing an integration
bug weeks later.

## Merge Order at CP5

When multiple lanes reach CP5 in the same window: **RED first (there should
be nothing else running anyway), then AMBER in lock-declaration order, then
GREEN in any order.** After each AMBER merge, still-active lanes that read
the merged artifact re-verify at CP3 before proceeding.

## Sizing Lanes

A lane should complete in **one to three sessions**. Longer-running lanes go
stale against mainline and turn cheap merges into archaeology. If a package
can't fit, it was mis-scoped at FL050 — split it, and let the pieces be
GREEN wherever possible. The art of the whole method is decomposing work so
that RED is rare, AMBER is small, and GREEN is everything else.
