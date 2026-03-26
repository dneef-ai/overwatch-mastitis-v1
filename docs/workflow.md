# Overwatch Drug Discovery Workflow

This document defines the 6-agent, 5-phase workflow for Overwatch drug discovery programs.
Follow these phases in order. Do not skip phases. Do not start proposing
treatments before you understand why current ones fail.

---

## Phase 1: Disease Map (Pathfinder)

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
`phase-1-disease-map.md` — annotated disease model with every stage, evidence tiers, identified rate-limiting barrier, R0 estimate, and portfolio-restructuring experiment (KE#1).

### Completion Criteria
- Every stage from entry to chronic persistence is mapped
- External models reviewed the disease map (cross-check.py --adversarial) and identified no missing major stages
- At least one published review article cross-checked for completeness
- Rate-limiting barrier explicitly named with evidence
- R0 estimated with evidence tier (or modeled from incidence/duration data)
- Prevention vs treatment leverage assessed based on R0
- Portfolio-restructuring experiment (KE#1) identified — the single cheapest experiment that would restructure the downstream portfolio

### Common Failure Modes
- Stopping at "infection → immune response → resolution or persistence" without mapping the persistence mechanisms in detail
- Treating the disease as a single event rather than a multi-stage process
- Ignoring stages where current treatments fail

---

## Phase 2: Treatment Failure Analysis (Sapper)

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

## Phase 3: Propose Solutions (Forge) + Computational Validation (Surveyor)

Phase 3 runs as two sequential steps: Forge proposes candidates, then Surveyor computationally validates every target before external review. External review then sees computationally-grounded candidates.

### Phase 3a: Propose Solutions (Forge)

#### Goal
Propose treatment candidates for EVERY disease stage — including stages where nothing currently exists.

#### What to Do
1. **First: search for what has actually worked in vivo in the target species.** Launch agents to find any compound/approach with positive trial data, regardless of mechanism. This catches modality-first discoveries that biology-first thinking misses.
2. For each disease stage from Phase 1:
   a. Empirical hits — approaches with positive in-vivo data in the target species (Category A)
   b. Known approaches — literature-supported targets with evidence (Category B)
   c. Non-obvious approaches — cross-disease analogies, emerging biology, repurposed mechanisms from other fields (Category C)
   d. Novel proposals — if nothing exists for this stage, DESIGN something from first principles. Use the biology from Phase 1 to identify intervention points. Be creative, then be rigorous. (Category D)
3. Propose at mechanism-level granularity, not category-level (Standard 40). Each specific mechanism gets its own entry.
4. Apply Standards 1-9 (evidence) to all proposals
5. Apply Standards 10-17 (target evaluation) to all proposals

#### Output
`phase-3-candidates.md` — candidate table covering ALL disease stages. For each candidate: mechanism, evidence tier, species data, key risk, proposed de-risk experiment.

#### Completion Criteria
- Every disease stage has at least one candidate
- Both obvious AND non-obvious approaches included
- Novel proposals included for stages with no existing approaches

#### Common Failure Modes
- Only proposing well-known targets with existing compounds
- Scoping out hard disease stages as "intractable"
- Failing to propose anything for stages where literature is silent

---

### Phase 3b: Computational Target Validation (Surveyor)

#### Goal
Computationally validate every candidate from Forge: confirm identity, assess conservation across field-relevant strains, check host selectivity, verify annotation claims, and predict structure for novel targets. Answer: "Is this target real, unique, conserved, and structurally plausible?"

Surveyor does not make kill decisions. It provides genomic, structural, and annotation data so that Reaper's kill tests are grounded in evidence rather than literature extrapolation.

#### What to Do

**Step 0: Target Resolution**
Parse each candidate's target/mechanism from `phase-3-candidates.md` and resolve every candidate to specific identifiers: gene name, protein accession (UniProt ID or RefSeq), organism taxonomy ID, and amino acid sequence via NCBI Entrez and UniProt. If the target cannot be resolved to a specific protein (e.g., it targets a pathway or a non-protein mechanism), note this and skip BLAST/structure analyses. Write resolved identifiers into the per-candidate assessment so all downstream work references specific accessions.

**Category A/B Candidates (Known / Non-Obvious) — Reality Check**
1. **Conservation analysis** — BLAST the target gene/protein across field-relevant pathogen isolates. Confirm the target is conserved across the strains that matter. Report % identity and coverage for each strain checked. Thresholds: <80% identity = "divergent"; absent from >20% of field strains = "conservation concern."
2. **Host selectivity** — BLAST the target against the host proteome (bovine, salmon, etc.). Flag any homolog with >50% identity at >50% query coverage. Report the specific ortholog, its function, and the selectivity risk.
3. **Annotation verification** — Query UniProt/NCBI Entrez to confirm or correct the candidate's claimed properties: localization, function, essentiality, and known post-translational modifications.

**Category C Candidates (Novel) — Full Workup**

Everything above, plus:

4. **Structure prediction** — Two-tier approach:
   - **Tier 1 (automated):** Check the AlphaFold Protein Structure Database for pre-computed structures. If found, download and assess for druggable pockets (pLDDT/pTM confidence scores).
   - **Tier 2 (human-in-the-loop):** For targets without pre-computed structures, or where co-folding with metals/ligands/partners is needed, Surveyor writes an AF3 submission request to `bioinfo/af3_requests/[target].md` and pauses to prompt Daniel to submit the job at alphafoldserver.com. Surveyor resumes once Daniel provides results.
5. **Operon / gene neighborhood analysis** — Query NCBI for genomic context. Is this gene part of a virulence island? Co-regulated with other virulence factors? In an operon with essential genes?
6. **Signal peptide / transmembrane prediction** — Confirm the protein's accessibility (cytoplasmic, membrane, surface, secreted). Verify Forge's assumptions about accessibility using UniProt annotations and sequence features.

**External Validation (after Surveyor)**
After Surveyor completes, run external validation on the candidates:
```
python3 tools/cross-check.py --adversarial phase-3-candidates.md \
  --tier premium --system-prompt-file tools/external-review-prompt.txt \
  --output phase-3-external-review.md
```
Address ALL external feedback. Incorporate promising alternatives suggested by external models (apply same evidence standards before adopting).

#### Output
`phase-3b-survey-report.md` — per-candidate assessments plus a summary table covering: accession, conservation (% identity / N strains), host selectivity risk, annotation verification, structure availability, and verdict (CONFIRMED / CORRECTED / FLAGGED).

Surveyor also creates a `bioinfo/` directory in the program folder:
```
programs/<name>/
├── phase-3-candidates.md
├── phase-3b-survey-report.md
└── bioinfo/
    ├── scripts/
    ├── sequences/
    ├── structures/
    ├── af3_requests/
    ├── results/
    └── cache/
```

#### Completion Criteria
- Every candidate in `phase-3-candidates.md` has a Surveyor assessment (no skips)
- BLAST parameters reported for all computational analyses (database, e-value threshold, date)
- All results tagged `[COMPUTATIONAL]` with the specific wet-lab experiment type that would confirm or refute each finding
- Category C targets either have a structure assessment or an AF3 submission request with valid reason
- External models reviewed `phase-3-candidates.md` and feedback addressed

#### Common Failure Modes
- Describing what BLAST would show instead of actually running it
- Skipping candidates because they seem straightforward
- Making kill recommendations — Surveyor provides data, Reaper makes kill decisions
- Forgetting to check the `bioinfo/cache/` directory before submitting duplicate BLAST queries
- Treating the AF3 human-in-the-loop checkpoint as optional for Category C targets with no pre-computed structure

---

## Phase 4: Red Team (Reaper)

### Goal
Destroy every candidate with evidence. Find the fatal flaw in each proposal before it wastes $500K in a cow trial.

Reaper is not constructive, not balanced, and not trying to help. Its ONE job is to find the single piece of evidence or logic that kills each candidate. Candidates that survive Reaper might actually work.

### What to Do

Reaper reads:
- `phase-3-candidates.md` — all candidates from Forge
- `phase-3b-survey-report.md` — computational validation data (conservation, host homology, structure, annotation). Use this to ground Kill Tests 2, 4, 5, and the host selectivity check.
- `phase-1-disease-map.md` — to verify candidates actually address what they claim
- `phase-2-failure-analysis.md` — to check if candidates repeat known failure modes

Apply these 10 kill tests to every candidate. Any single FAIL can kill a candidate:

1. **The 20-Year Test** — Has this target/mechanism been known for >5 years with no commercial product? If yes, explain why. If there's no good reason for the absence, the target is probably harder than claimed.

(Plus Kill Tests 11-12: Independent Replication Test and SCC/Clinical Endpoint Test — see `agents/reaper.md`)

2. **The Species Test** — Is the evidence from the target species, or extrapolated? Mouse mastitis is not bovine mastitis. Tag every piece of evidence with its actual species/model.

3. **The Matrix Test** — Has the compound/approach been tested in the real biological matrix (milk, rumen fluid, seawater — not broth)? If not, calculate what matrix effects would do (protein binding, pH, enzyme degradation).

4. **The Strain Test** — Has this been tested across relevant pathogen lineages? If only tested in lab strains, flag it. Field isolates may behave completely differently.

5. **The Resistance Test** — How fast would resistance develop? Single-point mutation (fast, fatal for monotherapy)? Multi-gene (slow, manageable)? Is there published resistance data?

6. **The Citation Test** — Verify the key PMIDs. Does the paper actually say what's claimed? Is the species/model correctly reported? Dispatch fresh subagents with zero context to verify — they can't inherit bias.

7. **The Stoichiometric Test** — For any intracellular mechanism: calculate molecules per cell at the proposed concentration. If <1, the mechanism is physically impossible.

8. **The Embarrassment Test** — State the simplest plausible way this candidate would fail in the real system. If you can't articulate it, the candidate hasn't been thought through.

9. **The Repetition Test** — Does this candidate repeat a known failure mode from Sapper's analysis? If yes, what's different this time? "This time it's different" needs evidence, not hope.

10. **The Commercial Reality Test** — Route of administration? Cost per dose? Regulatory pathway? Withdrawal period? If any of these are deal-breakers, flag them.

### Verdict System

For each candidate, deliver one of:
- **KILLED** — fatal flaw found. Cite the specific evidence. State exactly what kills it.
- **WOUNDED** — serious concern that must be addressed. The candidate might survive but needs a specific answer to a specific question.
- **SURVIVED** — you couldn't kill it. State what you tried and why it withstood the attack. This is the highest praise Reaper gives.

### Output
`phase-4-kill-report.md` — verdict for every candidate with evidence citations, specific failure mechanisms for KILLED verdicts, and unanswered questions for WOUNDED verdicts.

### Completion Criteria
- Every candidate has a verdict
- All KILLED verdicts cite specific evidence (not just skepticism)
- All WOUNDED verdicts specify the exact experiment needed to resolve the concern
- Surveyor's computational data was used to ground species, strain, and selectivity assessments

### Common Failure Modes
- Nihilistic kills based on absence of evidence rather than evidence of absence (flag as WOUNDED with specific experiment needed)
- Being constructive — suggestions go to Forge, not Reaper
- Grading novel proposals on a curve — they get the same scrutiny as known approaches
- Accepting "promising" as evidence

---

## Phase 5: Portfolio + 70% Test + Deliverables (Anvil)

Phase 5 runs as two sequential steps: first the 70% test (gatekeeper), then de-risk and deliver (output). Anvil does both.

### Step 0: Portfolio-Restructuring Experiment Check

Before running the 70% test, check: has Pathfinder's KE#1 been run? If not, flag it. The coverage estimates and target priorities that follow may change fundamentally based on its outcome.

### Step 0.5: Strategic Prioritisation

Force-rank the portfolio: "If you can fund only 3 experiments, which 3 and why?" Use R0 analysis, rate-limiting barrier identification, and information value. Present the top 3-5 as the Priority De-Risk Sequence. This prevents equal billing for load-bearing and marginal experiments.

### Step 1: The 70% Test (Gatekeeper)

#### Goal
Verify that the portfolio, if everything works, would reduce total TRACTABLE pathology by ≥70%.

#### What to Do
1. List every disease stage from Phase 1. Classify each as TRACTABLE (pharma/biologic/device intervention plausible for this partner) or NON-TRACTABLE (management, genomics, nutrition). Non-tractable stages are reported but do not count toward the 70% threshold.
2. For each tractable stage, list which portfolio candidate addresses it
3. For each candidate, estimate maximum pathology reduction if it works perfectly (with evidence tier and reasoning)
4. Use R0/herd dynamics (from Pathfinder) to weight prevention vs treatment targets
5. Sum coverage across tractable stages
6. If total < 70%:
   - Identify the uncovered stage(s)
   - Return to Phase 3 for those stages (Forge → Surveyor → Reaper → Anvil loop — maximum 3 loops)
   - Novel proposals will be required for stages with no existing approaches
7. Repeat until coverage ≥ 70%

#### How to Estimate Pathology Contribution
Use published data where available:
- Clinical outcome attribution studies
- Knockout/mutant phenotype data (how much does removing this factor change the disease?)
- Epidemiological data (what fraction of cases involve this mechanism?)
Where data is insufficient, state your reasoning and tag as [INFERRED].

#### Common Failure Modes (70% Test)
- Inflating coverage estimates to pass the test
- Double-counting (one candidate doesn't address two stages at 100% each)
- Accepting 70% without checking that coverage estimates are honest
- Treating the 70% threshold as a formality rather than a real constraint

---

### Step 2: De-Risk & Deliver

#### Goal
Design binary GO/KILL experiments for each candidate and produce partner-grade deliverables.

#### What to Do
1. For each portfolio candidate:
   - Binary GO/KILL gate with specific thresholds
   - Experiment design (prefer in vitro screening gates)
   - Realistic budget estimate (Standard 31)
   - Embarrassment pass (Standard 24)
   - Target Product Profile (Standard 10)
   - Incorporate Surveyor's structure predictions, conservation data, and annotation corrections into de-risk experiment design and the evidence register
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

#### Output
Coverage map + evidence register + decision memo. Partner-grade — a senior R&D scientist at the target partner should be able to read it, verify citations, and make an investment decision.

#### Completion Criteria
- Coverage map shows ≥70% total pathology addressed (Step 1 passed)
- Every candidate has GO/KILL gate, experiment, budget, TPP
- External models reviewed the final output
- All citation PMIDs verified (Standard 4 + Standard 14)
- A reviewer checking any 3 citations at random would find them correct
- The embarrassment pass is honest and specific for each target
- Coverage estimates have evidence tiers (not just assertions)
- External models reviewed the coverage assessment

#### Common Failure Modes
- Fantasy budget estimates ($5K for a screening cascade)
- GO/KILL gates that are too easy (always pass) or too hard (always fail)
- Missing TPPs
- Unverified citations in partner-facing material
- Coverage estimates with no evidence tiers

---

## The 70% Enforcement Loop

If Anvil fails the 70% test, Overwatch runs additional loops before accepting failure:

```
Forge (gap stages) → Surveyor → Reaper → Anvil (re-test)
```

Maximum 3 loops. If coverage still fails after 3 loops, escalate to Daniel.

Overwatch enforces this loop — Anvil does not self-certify. Overwatch reads the coverage map, checks the math, and verifies coverage estimates are honest before accepting a PASS.

---

## Output Directory Convention

Program outputs go in the program directory:
- `programs/mastitis/` for mastitis
- `programs/liver-abscess/` for liver abscess
- Each phase produces its named artifact in this directory.

Phase artifacts by name:
- `phase-1-disease-map.md`
- `phase-2-failure-analysis.md`
- `phase-3-candidates.md`
- `phase-3b-survey-report.md`
- `phase-4-kill-report.md`
- `phase-5-coverage-map.md`
- `phase-5-evidence-register.md`
- `phase-5-decision-memo.md`
