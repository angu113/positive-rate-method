# 10 — Seams: Enterprise Structure Without the Vocabulary

The software this method produces is not scripting. It is **enterprise
software at SMB weight**: built from the first line with the properties
that make enterprise systems survive — swappable vendors, migratable data,
priced exits — without the ceremony enterprises need to coordinate hundreds
of humans.

Those properties come from *seams*: deliberate boundaries where one part of
the system can change without the rest noticing. Software engineering has a
whole literature of these (the "design patterns" lineage). The operator
does not need to learn it. **The agent already knows the entire book.**
The operator's job is to *mandate the seams* — in business terms — and let
the agent implement them. Same division of labor as doc 08: judgment
doesn't transfer; procedure does.

## The Constitutional Rule

> **Nothing we don't own touches our code directly. Every outside thing —
> vendor API, platform, tool, AI service — talks to our system through one
> reception desk that we own. Vendors don't get keys to the shop floor.**

The shop-floor version: whatever truck shows up, whatever the supplier's
paperwork looks like, it becomes *your* format at the receiving dock, and
everything inside the building only ever sees your format. Swap suppliers —
the dock changes, the shop doesn't.

## The Three Seams (90% of the value)

**1. The Reception Desk** — *mandatory for every external dependency, from
day one, no exceptions.* One thin, owned module per outside thing; nothing
else in the codebase may import or call the vendor directly. Externals are
where the one-way doors live, so this seam is where exit insurance matters
most. (Engineers call this an adapter/facade. You don't have to.)

**2. The Swappable Policy** — for business rules you *know* will vary:
pricing schemes, optimization approaches, document formats, tax rules. Each
variant is a plug-in behind one socket; adding variant three doesn't touch
variants one and two. (Strategy pattern.) **Trigger condition: the second
variant exists or sits in a written FL200 callout.** Not before.

**3. The Data Counter** — all reads and writes of stored business data go
through one owned surface per module (which is doc 01's FL100 ownership
table made physical). This is precisely what turns a platform exit into a
migration instead of an excavation. (Repository pattern.)

## The Economics

A seam is **doc 07's exit paragraph made executable**. A one-way door with
a reception desk in front of it behaves like a two-way door: the exit cost
collapses from "rewrite everything that touched the vendor" to "rebuild the
desk." The premium is one thin file per dependency — minutes of agent work
when mandated at CP2, agonizing to retrofit at year two. That asymmetry is
the entire argument.

## The Opposite Failure: Ornamental Abstraction

Agents told "use good design patterns" over-abstract with enthusiasm:
interfaces for things that will only ever have one implementation, layers
for the sake of layers. Speculative generality is the consultant's disease
in code form, and it is caught at CP2 by a layperson with one question:

> **"Which written callout needs the second one?"**

No answer → it's out. Reception desks always justify themselves (externals
are inherently swappable); everything fancier must name its callout.

## Red Flag (added to doc 08 glossary)

> *"I've made this extensible for future flexibility."*

Flexibility that no callout demanded is scope inflation wearing a suit.

## Standing Constraints (add to the constitution)

- Every external dependency is wrapped in one owned reception-desk module;
  direct vendor calls anywhere else fail review at CP3.
- All stored-data access goes through the owning module's data counter.
- New abstractions beyond these require a named FL200 callout for the
  second use case, surfaced at CONFIRM BEFORE BUILDING.
