# ADOPTION INTERROGATION — {project name}
<!-- Doc 11, Phase 1. The OPERATOR is never asked to read code — every
     question you put to them stays in business language, one evening.
     The AGENT inspects code and config directly to fill these rows in;
     that inspection is how a real finding (like a config value nothing
     actually reads) gets caught instead of missed. -->

## 0. Phase Check (doc 01 — Phase of Flight)
| Question | Answer |
|----------|--------|
| Real business data stored? (records / months) | {n records, m months / none} |
| Real documents/outputs reached customers? | {yes since {date} / no} |
| Whose daily workflow depends on it? | {roles / nobody} |
| Platform choices WITH data behind them | {n} |
| Actively building or steady state? | {building / steady} |

**Phase:** {APRON / TAXI / TAKEOFF ROLL / CLIMB / CRUISE (+GO-AROUND?)}
**V1 crossed:** {no / yes — back-dated to {date}, logged}

<!-- APRON → stop here; use the QUICKSTART greenfield door instead. -->

## 1a. Value Inventory — what we protect
| Capability | Who uses it | What it replaced | If it dies tomorrow |
|-----------|------------|------------------|---------------------|
| {e.g. Quote generation} | {front office} | {retyping into 3 systems} | {back to 6 hrs/wk manual} |

## 1b. Friction Log — where time disappears
| What I asked for | What happened instead | What it cost |
|-----------------|----------------------|--------------|
| {feature X} | {agent asked me to review a refactor; session spiraled} | {2 evenings} |

## 1c. Data Reality — what we own and where it lives
| Data | Stored where | Owned by | Can we get it out? |
|------|-------------|----------|--------------------|
| {customers} | {platform/table} | {module} | {yes — export path / NO / unknown ⚠} |

<!-- Every "unknown" in the last column is already a finding. -->

## 1d. Decision Archaeology — doors already walked through
<!-- One row per platform-level choice already made. Classify NOW per doc 07. -->
| Decision | Foundation / Scaffolding | Roles it plays | Published limits & where we sit | Exit paragraph (dollars + weeks) |
|----------|--------------------------|----------------|--------------------------------|----------------------------------|
| {storage on X} | {scaffolding} | {storage, auth = 2} | {limit Y; we're at 60%} | {$ / wks / replacement} |

## Hard-path problems surfaced (if any)
<!-- Anything here is NOT part of the adoption lift — it is its own RED
     project. See doc 11, "When Adoption Surfaces a Hard-Path Problem." -->
- {e.g. platform at 90% of published limit; migration overdue}
