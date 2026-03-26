# Phase 5: Coverage Map -- The 70% Pathology Reduction Test

**Program:** Mastitis | **Partner:** Zoetis
**Agent:** Anvil | **Date:** 2026-03-26 | **Revision:** R1 (target-level reframe)
**Primary pathogen:** *Staphylococcus aureus* (bovine mastitis)
**Inputs:** Phase 1 Disease Map (R1), Phase 2 Failure Analysis (R1), Phase 3 Candidates R2 (27 targets), Phase 3b Survey Reports (R0, R1), Phase 4 Kill Report R2
**Prior attempt:** R0 (compound-level) FAILED at 43.45%

---

## Methodology

The 70% test asks: **does this portfolio of validated biological targets cover at least 70% of *S. aureus* bovine mastitis pathology?**

### The Target-Level Reframe

R0 failed at 43.45% because compound-level kills eliminated coverage for entire disease stages. R2 reframed from compounds to **targets** -- biological intervention points where Zoetis can aim its chemistry, biologics, and diagnostics teams. Under this framing:

- A target with proven biology but no current drug-like compound is STILL A VALID TARGET (Zoetis has its own chemistry)
- A target where a specific compound failed but the biology is sound is STILL ALIVE
- Coverage credit is awarded for validated biology, discounted by evidence tier and Reaper verdict

### How This Analysis Works

1. Disease stage pathology weights are carried forward from R0 (unchanged -- same disease biology)
2. For each stage, I list targets from Forge R2 with their Reaper R2 verdicts
3. SURVIVED targets contribute at full biological potential, discounted by evidence tier
4. WOUNDED targets contribute at reduced value (50% of biological potential) -- Reaper wounded them for practical/commercial reasons, not because the biology is wrong. But the practical concerns are real and discount the probability that a drug emerges from the target.
5. KILLED targets contribute 0%
6. Stage coverage = stage weight x combined target coverage
7. Total coverage = sum of all stage coverages

**I am NOT inflating estimates to pass.** Reaper R2 was honest. I respect its verdicts.

---

## Disease Stage Pathology Weights

Unchanged from R0. These weights reflect the multi-barrier model from Phase 1.

| Stage | Description | Weight | Evidence Basis |
|-------|-------------|--------|----------------|
| **0** | Upstream systemic modifiers | **8%** | Subclinical ketosis, transition-period immunosuppression, gut-mammary axis. [MODERATE/INFERRED] |
| **1** | Entry and exposure | **7%** | Teat canal barrier; ITS reduces IMI ~40%. Well-managed herds partially address. [ESTABLISHED] |
| **2** | Adhesion and colonization | **8%** | MSCRAMM-mediated adhesion, FnBP-mediated internalization. Gateway step. [ESTABLISHED for mechanism; INFERRED for weight] |
| **3** | Immune evasion | **15%** | SpA, LukMF', capsule, AdsA, superantigens. Prevents immune clearance. [ESTABLISHED] |
| **4** | Acute pathology and tissue damage | **10%** | Hla pore formation, LukMF' neutrophil killing, Hlb, neutrophil collateral damage. [ESTABLISHED] |
| **5** | Chronic persistence | **25%** | Intracellular survival, SCVs, biofilm. The central disease stage. Sets cure rate ceiling. [ESTABLISHED] |
| **6** | Treatment resistance | **12%** | Five barriers to antibiotic cure. Current cure rates 20-35% lactation, 40-70% dry-off. [ESTABLISHED] |
| **7** | Reinfection and reseeding | **10%** | Contagious transmission, within-cow spread, SCV reversion/intracellular release. [ESTABLISHED/MODERATE] |
| **8** | Resolution and remodeling | **5%** | Post-cure SCC recovery, fibrosis, microbiome re-equilibration. [MODERATE] |
| | **TOTAL** | **100%** | |

---

## Coverage Analysis by Stage

### Stage 0: Upstream Systemic Modifiers (8%)

**Targets and Reaper verdicts:**
- T1 (Gut-mammary axis/SCFA): **WOUNDED** -- biology real but unquantified contribution; feed additive, not Zoetis drug
- T2 (BHBA-neutrophil axis): **WOUNDED** -- ESTABLISHED biology but management protocol, not product
- T3 (Host genetics TLR4/CXCR1/BoLA): **WOUNDED** -- small gene effects; genomics product, not drug

**Coverage analysis:**

All three targets are WOUNDED. The biology of each is real:
- BHBA-neutrophil dysfunction: ESTABLISHED (PMID 18411287, 41651367). Subclinical ketosis is a documented risk factor for mastitis.
- Gut-mammary axis: MODERATE (PMID 41130091 -- causal evidence in caprine/murine). The application to bovine mastitis prevention is genuinely new.
- Host genetics: MODERATE-ESTABLISHED (CXCR1, TLR4, BoLA-DRB3 associations replicated).

Reaper wounded all three for the SAME reason: these are not pharmaceutical targets. They are management (T2), feed additive (T1), and genomics (T3) opportunities. The biology is sound -- the Zoetis product fit is poor for pharma. However, Zoetis has a Genetics division and a Nutrition division. T2 and T3 could be Zoetis Genetics/diagnostic products. T1 is genuinely outside Zoetis's core.

Combined biological coverage of Stage 0 if all three targets yield interventions: 65% (Forge estimate, which I find reasonable -- these three targets together address most of the known upstream modifiers, but the unquantified "other" systemic factors cap coverage).

**Discount for all-WOUNDED status:** 50% (practical/commercial barriers are real). 65% x 50% = 32.5%.

**Stage 0 coverage contribution:** 8% x 32.5% = **2.6%** [MODERATE/INFERRED]

---

### Stage 1: Entry and Exposure (7%)

**Targets and Reaper verdicts:**
- T4 (Teat canal keratin barrier): **SURVIVED** -- cheap line extension to existing Zoetis Orbeseal product
- T5 (NAS colonization resistance): **WOUNDED** -- narrow safety margin, undefined regulatory path

**Coverage analysis:**

T4 is an incremental improvement to an existing commercial product. Fatty acid antimicrobial activity against *S. aureus* is ESTABLISHED (Hibbitt 1969, Capuco 1992). ITS efficacy is ESTABLISHED (PMID 32081124, OR 0.29 for new IMI). An antimicrobial-enhanced ITS is a formulation question ($30-50K de-risk, binary GO/KILL). Reaper correctly noted: 5-15% improvement over baseline ITS. Contribution: modest but real.

T5 (NAS competitive exclusion) -- biology is MODERATE (epidemiological association, in-vitro biofilm disruption). But the regulatory void, the narrow margin between "probiotic" and "pathogen" for NAS species, and the zero interventional evidence make this a high-uncertainty target. WOUNDED is correct.

T4 biological coverage of Stage 1: 20% (incremental improvement over existing ITS baseline -- ITS already provides 40% reduction, T4 adds 5-15% on top of that, net ~20% of remaining unaddressed Stage 1 pathology).

T5 biological coverage at 50% discount: 15% x 50% = 7.5%.

Combined: 27.5% (these are additive -- different mechanisms).

**Stage 1 coverage contribution:** 7% x 27.5% = **1.9%** [ESTABLISHED for T4; MODERATE for T5]

---

### Stage 2: Adhesion and Colonization (8%)

**Targets and Reaper verdicts:**
- T6 (SrtA): **SURVIVED** -- cleanest anti-virulence target; zero host homolog; 99.5-100% conservation
- T7 (FnBPA-integrin axis): **SURVIVED** -- strongest single-gene phenotype (>95% internalization reduction in MAC-T)
- T8 (Iron acquisition/Isd): **SURVIVED** -- bovine trial data (Petitclerc 2007, 45.5% cure with lactoferrin + penicillin)

**Coverage analysis:**

This is the strongest stage in the portfolio. All three targets SURVIVED Reaper R2 and address different aspects of adhesion/colonization:

- T6 (SrtA) inhibition prevents display of ALL MSCRAMMs (ClfA, ClfB, FnBPA, FnBPB, Cna) -- the master switch for surface protein display. 24 years of chemistry failure, but recent covalent inhibitors (PMID 40122408, 2024-2025) show progress. Zero bovine homolog (Surveyor R0 CONFIRMED). [ESTABLISHED for target biology; MODERATE for pharmacological evidence]
- T7 (FnBPA) is the gateway to intracellular persistence. >95% internalization reduction with FnBP-deficient mutant DU5883 in bovine MAC-T cells (PMID 10547450, 12654860). Multiple drug modalities available (decoy, vaccine component, small molecule). [ESTABLISHED for target biology]
- T8 (Iron/Isd) -- validated by bovine trial data. Petitclerc 2007 (PMID 17517718, VERIFIED by Surveyor R1). Iron is a survival bottleneck. [MODERATE; bovine in-vivo]

Combined biological coverage: these three targets address surface display (T6), internalization (T7), and metabolic survival (T8) -- three independent adhesion/colonization mechanisms. T6 partially overlaps with T7 (SrtA prevents FnBPA display), but T7 offers an independent intervention point (decoy, vaccine) that works even if SrtA chemistry fails. Estimated combined coverage: 65% of Stage 2 pathology.

**Stage 2 coverage contribution:** 8% x 65% = **5.2%** [ESTABLISHED/MODERATE]

---

### Stage 3: Immune Evasion (15%)

**Targets and Reaper verdicts:**
- T9 (SpA Fc-binding): **SURVIVED** -- Fc evasion ESTABLISHED in cattle; Fab unknown is cheaply testable ($20-30K)
- T10 (LukMF'/CCR1): **WOUNDED** -- excellent bovine-validated biology but lineage restriction (50-96% depending on market)
- T11 (AdsA/A2aR axis): **WOUNDED** -- largely redundant with SrtA (T6); mouse-only in-vivo data
- T12 (CP5/CP8 capsule): **WOUNDED** -- within-host evolution loses capsule in chronic infections; 25+ year vaccine history with failures
- T13 (Gamma-delta T cell evasion): **KILLED** -- no molecular target identified

**Coverage analysis:**

SpA (T9) is the anchor. SpA Fc-binding blocks opsonophagocytosis -- the primary antibody-mediated killing mechanism. Removing SpA could unlock the entire humoral immune response. 100% conservation, zero host homolog (Surveyor R0). The critical unknown -- whether SpA binds bovine BoVH1 Fab -- is answerable with a $20-30K binding assay. Even if only Fc-binding operates in cattle, the target has substantial value. [ESTABLISHED for Fc mechanism]

T9 biological coverage of Stage 3: 25-35% (SpA is the single most important immune evasion mechanism, but it is one of several -- capsule, AdsA, LukMF', superantigens operate independently). I estimate 30%.

T10 (LukMF') is bovine-validated (PMID 26045537 -- CCR1 interaction). But lineage restriction limits coverage to 50-96% depending on market. In the best case (Dutch herds, 96% lukM+), this is a powerful target. In the worst case (50% lukM+), it helps half the infections. At 50% discount for WOUNDED status: biological coverage 20% x 50% = 10%.

T11 (AdsA) is largely redundant with SrtA -- AdsA is sortase-anchored. If SrtA (T6) works, AdsA is addressed. Independent A2aR antagonism path exists (human-approved istradefylline) but is more speculative. At 50% discount: 10% x 50% = 5%.

T12 (CP5/CP8) -- the 25-year vaccine failure track record and within-host capsule loss during chronic infection are damning. But capsule IS active during acute/early infection. As a vaccine component (not standalone), it contributes to early immune clearance. At 50% discount: 15% x 50% = 7.5%.

T13: KILLED. 0%.

Combined Stage 3 coverage: 30% (T9) + 10% (T10) + 5% (T11) + 7.5% (T12) = 52.5%. Cap at 50% because these mechanisms partially overlap (all improve immune clearance) and diminishing returns apply.

**Stage 3 coverage contribution:** 15% x 50% = **7.5%** [ESTABLISHED for T9; MODERATE for T10-T12]

---

### Stage 4: Acute Pathology and Tissue Damage (10%)

**Targets and Reaper verdicts:**
- T14 (NLRP3 activation): **WOUNDED** -- therapeutic window (pyroptosis = tissue damage) is unproven
- T15 (Hla): **WOUNDED** -- one of several tissue-damaging toxins; insufficient alone

**Coverage analysis:**

Both targets are WOUNDED. Neither is a primary coverage driver.

T14 (NLRP3 activation) is mechanistically interesting -- overriding *S. aureus* PINK1/Parkin suppression to force expulsion of intracellular bacteria. NLRP3 KO mice show 50% mortality within 24h (PMID reference in Phase 1 4.2 and Forge R2). But the therapeutic window question is real: pyroptosis IS tissue damage. The $40-60K MAC-T experiment will answer whether controlled activation is achievable (intracellular CFU reduced >1-log with cell death <30%). At 50% discount: biological coverage 25% x 50% = 12.5%.

T15 (Hla) -- one of several toxins. Even perfect anti-Hla neutralization leaves LukMF', Hlb, PSMs, and neutrophil collateral damage intact. Reaper correctly positioned this as a vaccine component, not a standalone target. At 50% discount: biological coverage 20% x 50% = 10%.

Combined: 12.5% + 10% = 22.5%. Some overlap (both reduce tissue damage), but via different mechanisms (intracellular bacterial expulsion vs. toxin neutralization). Cap at 25%.

**Stage 4 coverage contribution:** 10% x 25% = **2.5%** [MODERATE/INFERRED]

---

### Stage 5: Chronic Persistence (25%)

**This is the most important stage. 25% of total pathology. R0 failed here because SCV dormancy had ZERO coverage.**

**Targets and Reaper verdicts:**
- T16 (ClpP activation): **SURVIVED** -- most important target in portfolio; addresses SCV/persister gap
- T17 (Autophagy subversion axis): **WOUNDED** -- bacteria may escape autophagosomes before flux restoration can act
- T18 (SCV ETC metabolic reversion): **KILLED** -- both pharmacological approaches killed; no replacement proposed
- T19 (Biofilm matrix): **SURVIVED** -- phage signal (81.3% cure) is the strongest in portfolio
- T20 (TA systems): **KILLED** -- no drug-like compounds; redundant systems

**Coverage analysis:**

Stage 5 has three co-equal persistence mechanisms: intracellular survival, SCVs, and biofilm. I assess each sub-barrier:

**Sub-barrier A: Intracellular survival (~40% of Stage 5)**

T16 (ClpP activation) addresses intracellular bacteria by killing them regardless of metabolic state. ADEP4 + rifampicin eradicated chronic biofilm infection in mice in one day (Conlon et al. 2013, Nature 503:365, PMID 24226776). ZG-series compounds (Wei et al. 2022, PMID 36376309; Zhang et al. 2024, PMID 39615486) solve the mammalian selectivity problem. Three independent selectivity mechanisms confirmed in bovine ClpP by Surveyor R1 (W142, reversed H/Y, C-terminal lid). 99.5-100% conservation. [ESTABLISHED for target; MODERATE for ZG scaffold]

CRITICAL CAVEATS: (1) No SCV-specific data for ZG compounds, (2) single-lab dependency (Yang CG lab), (3) ClpP-null resistance is biologically accessible. Despite these, this is the highest-impact single target -- it fills the SCV gap that killed R0.

ClpP coverage of intracellular sub-barrier: 60% (addresses SCVs AND actively growing intracellular bacteria; limited by no bovine data and resistance risk).

T17 (Autophagy flux restoration) -- bacteria may escape autophagosomes before the intervention acts. This is the key critique. At 50% WOUNDED discount: 20% x 50% = 10%.

Iron deprivation (T8, scored in Stage 2 but has secondary effect here) -- lactoferrin creates iron stress on intracellular bacteria. 45.5% cure in bovine trials validates the mechanism. Secondary contribution: 10%.

Combined intracellular coverage: 60% + 10% + 10% = 80%. Cap at 70% (diminishing returns). 70% of 40% of Stage 5 = 28% of Stage 5.

**Sub-barrier B: SCV dormancy (~30% of Stage 5)**

This was the ZERO-coverage gap in R0. Now:

T16 (ClpP) is the primary SCV target. ClpP activation degrades >400 intracellular proteins -- killing dormant bacteria because they cannot replace degraded proteins. This is the mechanistic principle from Conlon et al. 2013. ZG compounds have NOT been tested against SCVs (this is the #1 experimental gap). But the mechanism is scaffold-independent -- if ZG activates ClpP, the downstream persister-killing effect follows from the target biology.

T18 (SCV ETC): KILLED. Both menadione and apo-lactoferrin approaches failed.
T20 (TA systems): KILLED. No drug-like compounds.

ClpP coverage of SCV sub-barrier: 50% (strong mechanistic basis but ZERO experimental confirmation against SCVs; single-lab dependency; resistance risk from ClpP-null mutants).

50% of 30% of Stage 5 = 15% of Stage 5.

**Sub-barrier C: Biofilm (~30% of Stage 5)**

T19 (Biofilm matrix) SURVIVED. Kromker 2026 phage cocktail: 81.3% cure (CI 57-94%, n=16) -- the highest cure rate for any novel modality. Phage inherently penetrate biofilm and lyse bacteria within the matrix. The n=16 is small but this is DIRECT BOVINE EVIDENCE. [PRELIMINARY for phage trial; ESTABLISHED for biofilm biology]

DNase + antibiotic is a backup modality if phage fails.

Biofilm coverage: 55% (phage signal is strong but unreplicated; DNase/enzyme approaches have formulation challenges; biofilm composition varies by strain).

55% of 30% of Stage 5 = 16.5% of Stage 5.

**Combined Stage 5 coverage:** 28% + 15% + 16.5% = 59.5%. Round to 60%.

**THIS IS THE CRITICAL CHANGE FROM R0.** R0 had 55% Stage 5 coverage with zero SCV coverage. R1 adds ClpP (T16) which addresses the SCV gap, raising Stage 5 coverage to 60%.

**Stage 5 coverage contribution:** 25% x 60% = **15.0%** [MODERATE -- anchored by ClpP (survived but untested in bovine SCV) and phage (survived but unreplicated)]

---

### Stage 6: Treatment Resistance (12%)

**Targets and Reaper verdicts:**
- T21 (Phage sensitivity): **SURVIVED** -- only novel modality with positive bovine field trial; AMR-orthogonal
- T22 (Endolysin substrate): **WOUNDED** -- lysostaphin-PTD 0% cure; milk matrix variability

**Coverage analysis:**

T21 (Phage) is the primary target. Lytic phage kill regardless of AMR genotype. Kromker 2026 achieved 81.3% cure (n=16). AMR-orthogonal mechanism. EU regulatory tailwind (Regulation 2019/6). [PRELIMINARY; direct bovine evidence]

T21 coverage of Stage 6: 50% (addresses genetic AMR completely, but does not address phenotypic tolerance/persister cells; n=16 is unreplicated; phage resistance development is a long-term concern; phage titers drop in milk within 36-48h).

T22 (Endolysin) at 50% WOUNDED discount: peptidoglycan cross-bridge is universal and essential. But lysostaphin-PTD 0% cure is sobering bovine data. Endolysins cannot reach intracellular bacteria (27 kDa protein). Milk matrix variability documented. Biological coverage 25% x 50% = 12.5%.

Combined: 50% + 12.5% = 62.5%. Cap at 55% (overlap -- both target extracellular bacteria via AMR-orthogonal killing).

**Stage 6 coverage contribution:** 12% x 55% = **6.6%** [PRELIMINARY for T21; MODERATE-NEGATIVE for T22]

---

### Stage 7: Reinfection and Reseeding (10%)

**Targets and Reaper verdicts:**
- T23 (Intracellular reservoir = Stage 5): **SURVIVED** -- derivative; passes if Stage 5 passes
- T24 (Contagious transmission diagnostics): **SURVIVED** -- established biology; low-risk; Zoetis diagnostics fit

**Coverage analysis:**

Stage 7 has two components: internal reseeding (~40%) and contagious transmission (~60%).

T23 -- internal reseeding coverage derives from Stage 5 success. Stage 5 coverage = 60%. Internal reseeding reduction proportional to Stage 5 success: 60% of 40% of Stage 7 = 24% of Stage 7.

T24 -- diagnostic-guided segregation improves on the 5-point plan. 20% reduction in new *S. aureus* IMI is the GO threshold. Conservative estimate: 15% of contagious transmission component = 15% of 60% = 9% of Stage 7.

Combined: 24% + 9% = 33%.

**Stage 7 coverage contribution:** 10% x 33% = **3.3%** [MODERATE/INFERRED]

---

### Stage 8: Resolution and Remodeling (5%)

**Targets and Reaper verdicts:**
- T25 (TGF-beta1/Smad fibrosis): **WOUNDED** -- 5-8 day treatment window vs. weeks-to-months anti-fibrotic biology
- T26 (SPM pathway): **KILLED** -- five stacked problems; 40% citation fabrication
- T27 (Mammary microbiome restoration): **WOUNDED** -- deliberately infusing bacteria into cured quarters; regulatory void

**Coverage analysis:**

T26 is KILLED. 0%.

T25 (pirfenidone for fibrosis): the fundamental biology question is whether 5-8 days of anti-fibrotic treatment prevents meaningful new fibrosis during a treatment window. Every published anti-fibrotic study requires weeks to months. Generic API is available ($0.005-0.10/dose, Surveyor R1 confirmed), so COGS is not the barrier. At 50% WOUNDED discount: 25% x 50% = 12.5%.

T27 (microbiome restoration): the safety concern is real -- deliberately infusing bacteria into post-cure quarters risks SCC elevation. But the $40-60K pilot with hard SCC stop is well-designed. At 50% WOUNDED discount: 15% x 50% = 7.5%.

Combined: 12.5% + 7.5% = 20%.

**Stage 8 coverage contribution:** 5% x 20% = **1.0%** [INFERRED]

---

## Coverage Summary

| Stage | Weight | Targets (Survived/Wounded/Killed) | Coverage % | Contribution | Primary Drivers |
|-------|--------|----------------------------------|-----------|--------------|-----------------|
| 0. Upstream systemic | 8% | 0S / 3W / 0K | 32.5% | 2.6% | T2 (BHBA), T3 (genetics) |
| 1. Entry/exposure | 7% | 1S / 1W / 0K | 27.5% | 1.9% | T4 (keratin barrier) |
| 2. Adhesion/colonization | 8% | 3S / 0W / 0K | 65% | 5.2% | T6 (SrtA), T7 (FnBPA), T8 (Isd) |
| 3. Immune evasion | 15% | 1S / 3W / 1K | 50% | 7.5% | T9 (SpA), T10 (LukMF') |
| 4. Acute pathology | 10% | 0S / 2W / 0K | 25% | 2.5% | T14 (NLRP3), T15 (Hla) |
| 5. Chronic persistence | 25% | 2S / 1W / 2K | 60% | 15.0% | T16 (ClpP), T19 (biofilm/phage) |
| 6. Treatment resistance | 12% | 1S / 1W / 0K | 55% | 6.6% | T21 (phage) |
| 7. Reinfection/reseeding | 10% | 2S / 0W / 0K | 33% | 3.3% | T23 (=Stage 5), T24 (diagnostics) |
| 8. Resolution/remodeling | 5% | 0S / 2W / 1K | 20% | 1.0% | T25 (TGF-beta1), T27 (microbiome) |
| **TOTAL** | **100%** | **10S / 12W / 4K** | | **45.6%** | |

---

## VERDICT: FAIL (but with structured path to conditional pass)

**Total coverage: 45.6% -- BELOW the 70% threshold by 24.4 percentage points.**

This is an improvement over R0 (43.45%) by 2.15 percentage points. The improvement is driven by:
- ClpP (T16) addressing the SCV dormancy gap (+1.5% via Stage 5 SCV sub-barrier)
- Stage 1 now has coverage from T4 (survived) and T5 (wounded) (+1.9% vs. 0% in R0)
- Stage 8 now has two WOUNDED targets (+1.0% vs. 0% in R0)

The improvement is modest because the target-level reframe, while conceptually correct, does not change the fundamental math: most targets are WOUNDED, and WOUNDED targets contribute at 50% of their biological potential. The 12 WOUNDED targets collectively contribute about 15% of the 45.6% total -- if they were all SURVIVED, total coverage would be ~60%.

---

## Why 70% Remains Structurally Difficult

### The Coverage Ceiling Analysis

Even in the best case (all WOUNDED targets pass their de-risk experiments and convert to SURVIVED), the portfolio reaches approximately:

| Stage | Weight | Best-Case Coverage | Contribution |
|-------|--------|--------------------|--------------|
| 0 | 8% | 65% | 5.2% |
| 1 | 7% | 35% | 2.45% |
| 2 | 8% | 65% | 5.2% |
| 3 | 15% | 65% | 9.75% |
| 4 | 10% | 40% | 4.0% |
| 5 | 25% | 70% | 17.5% |
| 6 | 12% | 60% | 7.2% |
| 7 | 10% | 45% | 4.5% |
| 8 | 5% | 35% | 1.75% |
| **TOTAL** | **100%** | | **57.55%** |

**Best-case with all WOUNDED converted to SURVIVED: ~58%.** This is still below 70%.

### The Gap That Blocks 70%

The remaining 12 percentage points require one or more of:

1. **Combination synergies.** Architecture A ("Cure Protocol": SrtA + iron deprivation + ClpP + phage) is biologically synergistic -- simultaneous defense stripping, metabolic stress, dormant-cell killing, and biofilm disruption could yield coverage exceeding the sum of individual targets. If synergies add 5-8% coverage, the best case reaches 63-66%.

2. **De-risk experiments exceeding expectations.** If the phage cocktail replicates at >70% cure (vs. the 60% GO threshold), or if ClpP kills SCVs at >4-log (exceeding the GO threshold), these would boost Stage 5 and 6 coverage beyond current estimates.

3. **Stage 3 vaccine platform success.** A multi-antigen vaccine (SpA + LukMF' + FnBPA + CP5/CP8) that achieves meaningful severity reduction would boost Stage 3 from 50% toward 70%. This is credible but requires the SpA Fab question answered AND the LukMF' carriage survey to show high coverage in target markets.

4. **Stage 4 NLRP3 therapeutic window exists.** If controlled NLRP3 activation is achievable (the $40-60K MAC-T experiment), Stage 4 coverage jumps from 25% toward 45%.

**Realistic range after de-risk: 55-66%.** The 70% threshold is reachable only if combination synergies are real AND the top de-risk experiments pass.

---

## Gap Report

### Structural Gaps

**1. Stage 4 (Acute Pathology) -- No SURVIVED targets.**
Both T14 (NLRP3) and T15 (Hla) are WOUNDED. Stage 4 is 10% of pathology. If both fail de-risk, Stage 4 drops to 0% coverage, costing 2.5 percentage points.

**2. Stage 0 (Upstream Systemic) -- No SURVIVED targets, no pharmaceutical products.**
All three targets are management/genomics/nutrition. Biologically valid but not the pharmaceutical targets Zoetis is primarily looking for.

**3. Stage 8 (Resolution) -- No SURVIVED targets, weakest biology in portfolio.**
SPM pathway KILLED. Pirfenidone and microbiome restoration both WOUNDED with uncertain biology. Stage 8 is only 5% of pathology, but fibrosis also limits efficacy of Stage 5/6 targets by creating physical barriers to drug delivery.

**4. SCV dormancy -- entire case rests on ClpP (single target, single lab).**
If ClpP fails de-risk (ZG compounds do not kill SCVs, or bovine selectivity fails experimentally), the SCV gap reopens with no backup. T18 (SCV ETC) is KILLED. T20 (TA systems) is KILLED. There is no Plan B for SCV dormancy.

### What Must Happen Next

This gap report goes back to Overwatch. The portfolio FAILS at 45.6%.

**However, the failure is different from R0.** R0 failed because of structural completeness -- entire disease stages had zero coverage. R1 has coverage at every stage except that no stages have SURVIVED-only coverage anchoring them at high confidence.

**Recommendation: proceed to Phase 5 deliverables (evidence register, decision memo) WITH the 45.6% coverage honestly reported.** The rationale:

1. The 45.6% number is conservative. It discounts all 12 WOUNDED targets at 50%. Several of these (T2 BHBA, T10 LukMF', T15 Hla) have ESTABLISHED biology -- they are wounded for practical/commercial reasons, not biological ones. A partner with broader capabilities (Zoetis has pharma, genetics, nutrition, diagnostics) may convert wounded targets that a pure-pharma company could not.

2. The de-risk sequence ($500-700K over 18 months) is designed to convert the most impactful WOUNDED targets to SURVIVED (or KILLED, providing clarity). After the Month 1-3 in-vitro sprint, coverage will either climb toward 55-60% or the ceiling will be confirmed.

3. The target-level reframe is the correct framing for a Zoetis partnership. Zoetis does not need Agteria to deliver compounds. Zoetis needs validated targets with evidence packages and de-risk roadmaps. The 45.6% coverage with a structured path to 60%+ is more valuable than an inflated 70% claim built on wishful compound-level estimates.

4. Sending Forge back a third time is unlikely to yield new targets that were not already captured in the 27-target portfolio. The disease biology is comprehensively mapped (8 stages + 3 supplementary sections in Phase 1). The gaps are in target maturity and de-risk data, not in target identification.

---

## Sensitivity Analysis

### What happens if key targets fail de-risk?

| Scenario | Targets Lost | Coverage Impact | New Total |
|----------|-------------|----------------|-----------|
| ClpP fails (ZG no SCV kill) | T16 | Stage 5 drops from 60% to 42% (-4.5%) | 41.1% |
| Phage fails replication (<35% cure) | T21, T19 (phage component) | Stage 5 drops to 50%, Stage 6 drops to 25% (-5.4%) | 40.2% |
| SpA Fab question negative + OPK fails | T9 weakened | Stage 3 drops from 50% to 35% (-2.25%) | 43.35% |
| Both ClpP AND phage fail | T16, T21, T19 | Stage 5 drops to 35%, Stage 6 drops to 25% (-9.4%) | 36.2% |

**Worst case (both ClpP and phage fail): 36.2%.** This would be a catastrophic outcome requiring fundamental portfolio redesign.

**Best case (ClpP + phage + SpA + NLRP3 all pass): ~58-66%.** Still below 70% but commercially presentable with honest framing.

---

*This coverage map was built using pathology weights from Phase 1 Disease Map (R1), target biology from Forge R2, Reaper R2 verdicts, and computational evidence from Surveyor R0 and R1. WOUNDED targets discounted at 50%. KILLED targets at 0%. No combination synergies assumed. All evidence tiers per Quality Standard 1.*
