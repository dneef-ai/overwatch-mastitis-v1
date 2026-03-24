# Argus Drug Discovery Workflow

This document defines the 5-phase workflow for Argus drug discovery programs.
Follow these phases in order. Do not skip phases. Do not start proposing
treatments before you understand why current ones fail.

---

## Phase 1: Disease Map

### Goal
Understand the full pathology. Map every stage from initial infection/exposure to chronic persistence/treatment failure.

### What to Do
1. Read all existing program files (v8, v9 if they exist) as starting context
2. Map the complete disease progression:
   - Entry/exposure mechanism
   - Colonization and establishment
   - Immune evasion strategies
   - Acute pathology drivers
   - Chronic persistence mechanisms
   - Treatment resistance mechanisms
   - Reinfection/reseeding pathways
3. For each stage: what's driving it? What's the evidence? What's unknown?
4. Identify the RATE-LIMITING BARRIER — which stage most determines outcome?

### Output
`phase-1-disease-map.md` — annotated disease model with every stage, evidence tiers, and identified rate-limiting barrier.

### Completion Criteria
- Every stage from entry to chronic persistence is mapped
- External models reviewed the disease map (cross-check.py --adversarial) and identified no missing major stages
- At least one published review article cross-checked for completeness
- Rate-limiting barrier explicitly named with evidence

### Common Failure Modes
- Stopping at "infection → immune response → resolution or persistence" without mapping the persistence mechanisms in detail
- Treating the disease as a single event rather than a multi-stage process
- Ignoring stages where current treatments fail

---

## Phase 2: Treatment Failure Analysis

### Goal
For every current/historical treatment approach: why doesn't it work? What specifically defeats it?

### What to Do
1. List at least 8 current or historical treatment approaches
2. For each: what is the specific failure mechanism?
   - Not just "didn't work in trials" — WHY didn't it work?
   - What biological mechanism defeats the treatment?
   - What pharmacological barrier prevents efficacy?
3. Map failures back to the disease stages from Phase 1
4. Identify which disease stages have NO effective treatment

### Output
`phase-2-failure-analysis.md` — failure map with specific failure mechanisms for each approach and identified treatment gaps by disease stage.

### Completion Criteria
- At least 8 approaches analyzed
- Each has a specific failure mechanism (not just "insufficient efficacy")
- Treatment gaps mapped to disease stages
- Rate-limiting barrier to cure explicitly named

### Common Failure Modes
- Listing treatments without explaining WHY they fail
- Accepting "this approach doesn't work" without investigating the mechanism
- Not connecting treatment failures to specific disease stages

---

## Phase 3: Propose Solutions

### Goal
Propose treatment candidates for EVERY disease stage — including stages where nothing currently exists.

### What to Do
1. For each disease stage from Phase 1:
   a. Known approaches — literature-supported targets with evidence
   b. Non-obvious approaches — cross-disease analogies, emerging biology, repurposed mechanisms from other fields
   c. Novel proposals — if nothing exists for this stage, DESIGN something from first principles. Use the biology from Phase 1 to identify intervention points. Be creative, then be rigorous.
2. Apply Standards 1-9 (evidence) to all proposals
3. Apply Standards 10-17 (target evaluation) to all proposals
4. Run external validation:
   ```
   python3 tools/cross-check.py --adversarial phase-3-candidates.md \
     --tier premium --system-prompt-file tools/external-review-prompt.txt \
     --output phase-3-external-review.md
   ```
5. Address ALL external feedback
6. Incorporate promising alternatives suggested by external models (apply same evidence standards before adopting)

### Output
`phase-3-candidates.md` — candidate table covering ALL disease stages. For each candidate: mechanism, evidence tier, species data, key risk, proposed de-risk experiment.

### Completion Criteria
- Every disease stage has at least one candidate
- Both obvious AND non-obvious approaches included
- External models reviewed and feedback addressed
- Novel proposals included for stages with no existing approaches

### Common Failure Modes
- Only proposing well-known targets with existing compounds
- Scoping out hard disease stages as "intractable"
- Treating external model suggestions as automatically inferior
- Failing to propose anything for stages where literature is silent

---

## Phase 4: The 70% Test

### Goal
Verify that the portfolio, if everything works, would reduce total pathology by ≥70%.

### What to Do
1. List every disease stage from Phase 1 with its contribution to overall pathology (rough % estimate with evidence tier)
2. For each stage, list which portfolio candidate addresses it
3. For each candidate, estimate maximum pathology reduction if it works perfectly (with evidence tier and reasoning)
4. Sum coverage across all stages
5. If total < 70%:
   - Identify the uncovered stage(s)
   - Return to Phase 3 for those stages
   - You may need to propose something genuinely novel
6. Repeat until coverage ≥ 70%

### Output
`phase-4-coverage-map.md` — portfolio coverage analysis with stage-by-stage breakdown, honest gap assessment, and evidence for coverage estimates.

### Completion Criteria
- Coverage map shows ≥70% total pathology addressed
- Every major disease stage has at least one candidate
- Coverage estimates have evidence tiers (not just assertions)
- External models reviewed the coverage assessment

### How to Estimate Pathology Contribution
Use published data where available:
- Clinical outcome attribution studies
- Knockout/mutant phenotype data (how much does removing this factor change the disease?)
- Epidemiological data (what fraction of cases involve this mechanism?)
Where data is insufficient, state your reasoning and tag as [INFERRED].

### Common Failure Modes
- Inflating coverage estimates to pass the test
- Double-counting (one candidate doesn't address two stages at 100% each)
- Accepting 70% without checking that coverage estimates are honest
- Treating the 70% threshold as a formality rather than a real constraint

---

## Phase 5: De-Risk & Deliver

### Goal
Design binary GO/KILL experiments for each candidate and produce partner-grade deliverables.

### What to Do
1. For each portfolio candidate:
   - Binary GO/KILL gate with specific thresholds
   - Experiment design (prefer in vitro screening gates)
   - Realistic budget estimate (Standard 31)
   - Embarrassment pass (Standard 24)
   - Target Product Profile (Standard 10)
2. Run external validation on the complete portfolio:
   ```
   python3 tools/cross-check.py --adversarial phase-5-decision-memo.md \
     --tier premium --system-prompt-file tools/external-review-prompt.txt \
     --output phase-5-external-review.md
   ```
3. Address ALL external feedback
4. Produce partner-grade deliverables:
   - `phase-5-evidence-register.md` — structured evidence by target with PMIDs, tiers, species tags, replication status
   - `phase-5-decision-memo.md` — partner-facing recommendation with portfolio, de-risk experiments, budgets, commercial framing

### Output
Evidence register + decision memo. Partner-grade — a senior R&D scientist at the target partner should be able to read it, verify citations, and make an investment decision.

### Completion Criteria
- Every candidate has GO/KILL gate, experiment, budget, TPP
- External models reviewed the final output
- All citation PMIDs verified (Standard 4 + Standard 14)
- A reviewer checking any 3 citations at random would find them correct
- The embarrassment pass is honest and specific for each target

### Common Failure Modes
- Fantasy budget estimates ($5K for a screening cascade)
- GO/KILL gates that are too easy (always pass) or too hard (always fail)
- Missing TPPs
- Unverified citations in partner-facing material

---

## Output Directory Convention

Enhanced workflow outputs go in a new version directory:
- `zoetis-mastitis-v10/` for mastitis
- `elanco-liver-abscess-v10/` for liver abscess
- Each phase produces its named artifact in this directory.
