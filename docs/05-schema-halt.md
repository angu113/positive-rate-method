# 05 — The Schema-Halt Protocol

The most expensive class of mistake in AI-assisted development is a **silent
data-shape change**: the agent adds a column, renames a field, "improves" a
stored JSON structure, or migrates data as a side effect of an unrelated task.
Code mistakes are cheap — revert the branch. Data mistakes propagate into
stored records, documents already issued, and integrations already consuming
the old shape. They compound hourly.

The schema-halt protocol treats data shape the way a shop treats lockout/tagout:
a formal stop with a formal restart.

## Halt Triggers

The protocol activates when **any** of the following occurs:

1. A package is classified RED at CP1 (planned halt).
2. Any session, in any lane, *proposes* a data-shape change — even as a
   suggestion (unplanned halt).
3. A CP3 change summary reveals a data-shape change that wasn't declared
   (emergency halt — this is also a gate violation).
4. The operator discovers stored data whose shape doesn't match the FL100
   data-ownership table (forensic halt).

"Data shape" is defined broadly on purpose: database schema, stored file
formats, document templates whose output is retained, identifier formats,
and any serialized structure another module reads.

## The Halt Sequence

1. **STOP all lanes.** Every active session is ended or instructed to stand
   down at its current gate. The manifest is marked `HALT` at the top.
2. **State the change in writing** — one paragraph, in business terms, in the
   FL100 data-ownership table's vocabulary: what shape, owned by whom,
   changing how, read by which modules.
3. **Enumerate the blast radius.** Every module that reads the shape, every
   document type generated from it, every stored record already in the old
   shape, every integration consuming it.
4. **Write the migration + rollback pair.** No forward migration is approved
   without its reverse written at the same time. If the reverse is impossible
   (destructive change), that fact is stated explicitly and the operator
   signs off on it specifically. **Lighter tier for purely-additive
   changes:** a migration that is provably additive only — a new nullable
   or safely-defaulted column/table, zero changes to any existing row,
   column, or consumer — satisfies this step by stating explicitly "no
   rollback needed — additive only, default is a no-op" instead of writing
   a formal reverse script. Any migration that also backfills or mutates
   existing rows, even "just" setting a flag on rows that already exist,
   still needs the full reverse-pair treatment.
5. **Execute solo, as a RED lane,** through the full gate sequence. CP4
   verification includes checking *old* records still read correctly, not
   just new ones.
6. **Amend the constitution and FL100 table** (`CONST:` commit) so every
   future session knows the new shape.
7. **Lift the halt.** Manifest cleared, lanes re-open — each surviving lane
   re-verifies at its current gate against the new shape before proceeding.

## When the Migration Runner Auto-Applies Fleet-Wide

The sequence above assumes an implicit ordering: surface the note, get
sign-off, *then* it touches the database. That ordering doesn't hold when
the schema-application mechanism auto-applies on next deploy or boot with
no code-level approval gate — the common case for migration-runner tooling
(DbUp, Flyway, EF Migrations and similar). In a fleet or multi-node
architecture, any node that pulls the new build can apply the migration
the moment it boots against the shared database, regardless of whether
sign-off has actually been given. In that shape, step 2's sign-off must
complete **before the migration file merges to the main branch** — not
before "the next ship," which may already be too late once more than one
node can boot the new build. Where a true pre-apply code gate is wanted
(blocking apply until an explicit approval flag is set), that is a
separate, heavier build — a CI check or a startup marker check — not
something the written note provides for free.

## Why So Heavy

Because the asymmetry is extreme. In practice the full sequence costs an
evening. The failure it prevents — three parallel lanes each half-adapted to
a schema that changed under them, plus a week of production documents issued
against the wrong shape — costs weeks, and some of it (documents already in
customers' hands, audit records already written) can't be repaired at all.

An append-only audit trail (part of the reference architecture) is the halt
protocol's insurance policy: when a forensic halt happens, the audit table is
how you reconstruct which records were written under which shape.

## The Cultural Point

The protocol also disciplines the *agent*. A constitution that states "any
data-shape proposal triggers a halt — surface it, do not implement it"
converts the agent's most dangerous habit (helpfully migrating your data)
into its most useful one (flagging shape pressure early, while it's still a
one-paragraph decision).
