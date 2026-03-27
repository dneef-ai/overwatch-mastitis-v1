# Phase 5: Coverage Map — The 70% Tractable Pathology Test

**Program:** Liver Abscess | **Partner:** Elanco | **Date:** 2026-03-27
**Agent:** Anvil | **Status:** Complete

---

> **CRITICAL: KE#1 has not been run. Coverage estimates for hindgut-origin pathology (Stages 5, 8) and the overall portfolio balance may change fundamentally based on its outcome. All coverage numbers below for hindgut-related pathology are provisional.**

---

## Step 1: Disease Stage Classification

### Tractable vs Non-Tractable

| # | Disease Stage | Classification | Rationale |
|---|---------------|---------------|-----------|
| 1 | Ruminal acidosis | **NON-TRACTABLE** | This is fundamentally a diet problem. The acidosis itself is non-tractable without changing the 80-95% concentrate finishing diet, which is economically impossible. Feed additives that address downstream consequences (barrier damage, colonization) are classified under those downstream stages. Monensin's intake stabilization role is a management-adjacent contribution, not a direct pharmaceutical intervention against acidosis per se. |
| 2 | Rumen epithelial damage / barrier breakdown | **TRACTABLE** | Tight junction upregulation, barrier repair, and anti-inflammatory interventions are pharmaceutical approaches. |
| 3 | Rumen wall colonization by F. necrophorum | **TRACTABLE** | Anti-adhesion (FomA, OMP vaccines), selective antimicrobials, and competitive exclusion are all pharmaceutical/biological interventions. This is the rate-limiting barrier. |
| 4 | Portal translocation (rumen origin, ~76%) | **TRACTABLE** | Barrier integrity enhancement and mucosal immunity reduce translocation. Partially addressed by interventions at Stages 2-3. |
| 5 | Portal translocation (hindgut origin, ~24%) | **TRACTABLE (provisional)** | Hindgut barrier integrity and microbiome management are pharmaceutical approaches. But the biology is poorly understood and KE#1 has not been run. Tractable classification is provisional. |
| 6 | Hepatic immune evasion (leukotoxin) | **TRACTABLE** | Vaccines, anti-toxin antibodies, and receptor blockers are biological/pharmaceutical interventions. Most validated virulence target. |
| 7 | Anaerobic niche creation | **NON-TRACTABLE (post-kills)** | All candidates for this stage were killed (gallium: regulatory impossible; antiplatelet: bleeding risk). No surviving or wounded candidate addresses this stage. Niche creation is also a multi-mechanism process (LPS coagulation + hemolysin + platelet aggregation) with no single intervention point. Preventing upstream colonization/translocation (Stages 2-4) makes this stage moot. |
| 8 | Polymicrobial synergy (Fn + Tp + Bacteroides) | **TRACTABLE** | Anti-pyolysin strategies and quorum sensing disruption are pharmaceutical approaches. However, all candidates are wounded. |
| 9 | Abscess formation / acute pathology | **TRACTABLE** | Immunomodulation to break the recruit-kill-recruit cycle is a pharmaceutical approach. However, only one wounded candidate remains (#18). |
| 10 | Chronic persistence (fibrous capsule) | **NON-TRACTABLE** | Established abscesses are pharmacokinetically untreatable. Prevention only. Correctly excluded from the 70% test. |
| 11 | Biofilm immune evasion (PPIX) | **NON-TRACTABLE (post-kills)** | All candidates killed (PDT: light delivery impossible; PPIX inhibitor: host toxicity; biofilm dispersal: delivery impossible + dissemination risk). Board resurrected #23 reframed to Stage 3 (rumen wall biofilm), not Stage 11. Evidence for in vivo biofilm in abscesses is PRELIMINARY only. |

### Summary

| Classification | Stages | Count |
|---|---|---|
| **TRACTABLE** | 2, 3, 4, 5, 6, 8, 9 | 7 |
| **NON-TRACTABLE** | 1, 7, 10, 11 | 4 |

The 70% test is assessed against the 7 tractable stages.

---

## Step 2: Pathology Contribution Estimates

To calculate coverage, we need to estimate what fraction of total liver abscess incidence each tractable stage contributes to. This is not a simple additive model -- liver abscess is a sequential cascade where ALL stages must be traversed for an abscess to form. Blocking ANY stage in the cascade blocks the downstream outcome.

### The Cascade Logic

An abscess forms only if: Acidosis (Stage 1) -> Barrier damage (Stage 2) -> Colonization (Stage 3) -> Translocation (Stage 4 or 5) -> Immune evasion (Stage 6) -> Niche creation (Stage 7) -> Synergy (Stage 8) -> Abscess (Stage 9) -> Persistence (Stage 10).

Because this is a sequential cascade, interventions at ANY tractable stage reduce the final incidence. The key question is: **what fraction of the remaining disease pathway does each intervention block?**

### Two Translocation Routes

| Route | Estimated contribution | Evidence |
|---|---|---|
| Rumen origin (Stages 2-4-6) | ~76% of all abscesses | [MODERATE -- Pinnell et al. 2022-2023] |
| Hindgut origin (Stage 5-6) | ~24% of all abscesses | [MODERATE -- Pinnell et al. 2022-2023] |

**KE#1 dependency:** The 76/24 split is from a single lab's 16S data. If KE#1 shows a different ratio (especially under tylosin), all coverage estimates below change.

### Reference Benchmarks

| Intervention | Observed incidence reduction | Evidence |
|---|---|---|
| Tylosin (continuous) | 40-70% reduction (Stage 3 primarily) | [ESTABLISHED -- Amachawadi et al. 2025, 32 trials] |
| MON+BX (combination) | ~34% reduction vs untreated control (28.5% vs 43.1%) | [ESTABLISHED -- single study, Felizari 2025] |
| Fusogard on forage diets | OR=0.27 (~73% reduction, Stage 6) | [ESTABLISHED -- Fox et al. 2009] |
| Fusogard on grain diets | No significant effect | [ESTABLISHED -- Checkley et al. 2009] |
| High roughage (45% corn silage) | Reduction from 29% to 12.4% (~57%) | [ESTABLISHED] |

---

## Step 3: Coverage by Tractable Stage

### Stage 2: Rumen Epithelial Damage / Barrier Breakdown

| Candidate | Status | Max pathology reduction if works perfectly | Evidence tier | Notes |
|---|---|---|---|---|
| #2 Rumen-protected butyrate | WOUNDED | 15-25% of rumen-origin abscesses (by reducing translocation volume) | [MODERATE for mechanism; INFERRED for LA efficacy] | VFA paradox unresolved. Ussing chamber experiment needed. No feedlot LA data. |
| #3 Zinc + butyrate combo | WOUNDED | Incremental over #2, possibly 5-10% additional | [INFERRED] | Zinc alone has failed. Combination synergy unproven. |

**Stage 2 coverage estimate: 15-25% of rumen-origin abscesses = 11-19% of total incidence**
**Confidence: LOW.** No feedlot LA data for any barrier integrity intervention. The butyrate VFA paradox could make this zero.

### Stage 3: Rumen Wall Colonization by F. necrophorum

| Candidate | Status | Max pathology reduction if works perfectly | Evidence tier | Notes |
|---|---|---|---|---|
| #1 MON+BX | SURVIVED (conditional) | ~34% total incidence reduction (observed) | [ESTABLISHED -- single study] | Board requires independent replication. 10-point gap vs tylosin persists. |
| #4 Multi-antigen vaccine (reformulated) | WOUNDED (severe) | 30-50% of rumen-origin abscesses via anti-adhesion | [MODERATE for individual antigens; INFERRED for combination in cattle] | Must be reformulated. Zero cattle grain-diet data. Mouse model misleading. |
| #6 Epimural probiotic | WOUNDED | Unknown -- concept stage | [INFERRED] | 5+ year timeline. Basic research. |
| #25 Bacteriocin probiotic | WOUNDED | Unknown -- concept stage | [INFERRED] | <5% cumulative probability of success. |
| #23 Biofilm dispersal (reframed) | WOUNDED (resurrected) | Unknown -- reframed to rumen wall | [INFERRED] | Biofilm at rumen wall unproven. |

**Stage 3 coverage estimate: 25-40% of total incidence** (anchored by MON+BX observed 34% reduction)
**Confidence: MODERATE** for MON+BX (single study, cattle data). LOW for all others.

### Stage 4: Portal Translocation (Rumen Origin)

| Candidate | Status | Max pathology reduction if works perfectly | Evidence tier | Notes |
|---|---|---|---|---|
| #8 Mucosal IgA vaccine (intranasal only) | WOUNDED | 20-40% of rumen-origin translocation if IgA reaches rumen wall | [INFERRED] | Ruminant mucosal immunology poorly characterized. No evidence intranasal -> rumen wall IgA. |

**Stage 4 coverage estimate: 0-15% of rumen-origin abscesses = 0-11% of total incidence**
**Confidence: VERY LOW.** Single wounded candidate with no data.

### Stage 5: Portal Translocation (Hindgut Origin)

| Candidate | Status | Max pathology reduction if works perfectly | Evidence tier | Notes |
|---|---|---|---|---|
| #9 Hindgut prebiotic | SURVIVED (contingent on KE#1) | Up to 50-80% of hindgut-origin abscesses = 12-19% of total incidence | [PRELIMINARY] | Entirely contingent on KE#1. No LA endpoint data. |
| #10 Hindgut butyrate + zinc | WOUNDED | Incremental over #9 | [INFERRED] | Same VFA paradox as #2. Less evidence. |

**Stage 5 coverage estimate: 12-19% of total incidence** (if hindgut abscesses are ~24% of total AND intervention is highly effective)
**Confidence: LOW.** Single lab's 16S estimate. KE#1 not run. No LA endpoint data for any hindgut intervention.

### Stage 6: Hepatic Immune Evasion (Leukotoxin)

| Candidate | Status | Max pathology reduction if works perfectly | Evidence tier | Notes |
|---|---|---|---|---|
| #12 rPL4 vaccine + slow-release adjuvant | SURVIVED (conditional) | 40-70% of rumen-origin abscesses if titer sustained for 150 days (matching Fusogard's forage-diet efficacy under reduced burden) | [MODERATE for target; INFERRED for grain-diet efficacy] | 30-year failure history on grain diets. Requires sustained titers that no adjuvant has demonstrated. Conditional on PL4 survey + rumen IgG access. |
| #5 Anti-FomA mAb (reframed as validation tool) | WOUNDED (severe, resurrected) | N/A -- mechanistic validation, not portfolio coverage | -- | Not counted toward coverage. |
| #13 Leukotoxin receptor ID | WOUNDED | Unknown -- basic research, 5-10 year path | [INFERRED] | Not counted toward near-term coverage. |

**Stage 6 coverage estimate: 40-70% of rumen-origin abscesses = 30-53% of total incidence** (if vaccine works as well on grain diets as Fusogard does on forage diets, which requires burden reduction from MON+BX)
**Confidence: LOW-MODERATE.** Target is validated. But no grain-diet cattle data for any modern vaccine formulation. Adjuvant performance over 150 days is the critical unknown.

### Stage 8: Polymicrobial Synergy

| Candidate | Status | Max pathology reduction if works perfectly | Evidence tier | Notes |
|---|---|---|---|---|
| #16 Anti-pyolysin | WOUNDED | ~29% reduction in abscess severity (not incidence), limited to the 29% of abscesses containing T. pyogenes | [MODERATE for target; INFERRED for LA efficacy] | Only as add-on to vaccine. |
| #17 Quorum quenching | WOUNDED | Unknown | [INFERRED] | Zero functional studies in F. necrophorum. LuxS may be metabolic. |

**Stage 8 coverage estimate: 5-10% incremental reduction in abscess severity**
**Confidence: VERY LOW.** Both candidates wounded. T. pyogenes is co-pathogen in only 29% of cases.

### Stage 9: Abscess Formation / Acute Pathology

| Candidate | Status | Max pathology reduction if works perfectly | Evidence tier | Notes |
|---|---|---|---|---|
| #18 Immunomodulatory macrolide analog | WOUNDED | Unknown -- depends on unresolved 50-year question | [INFERRED] | 7-10 year development path. In vitro experiment ($20-30K) needed first. |

**Stage 9 coverage estimate: 0% near-term**
**Confidence: N/A.** This is a basic research question, not a portfolio asset.

---

## Step 4: The 70% Test — Portfolio Coverage Calculation

### Portfolio: Board's Force-Ranked Surviving Candidates

The active portfolio consists of the Board's top 4 surviving candidates plus key wounded candidates:

**Core portfolio (survived/conditional):**
1. MON+BX (#1) -- Stages 1/3
2. rPL4 vaccine (#12) -- Stage 6
3. Hindgut prebiotic (#9) -- Stage 5
4. Triple Stack (#26) -- Stages 1/3/6 combined

**Key wounded (contributing to coverage):**
5. Rumen-protected butyrate (#2) -- Stage 2
6. Multi-antigen vaccine (#4, reformulated) -- Stage 3

### Coverage Calculation: Scenario Analysis

Because the cascade is sequential, interventions at different stages compound. An animal whose rumen wall is protected (Stage 2) AND whose colonization is reduced (Stage 3) AND whose leukotoxin is neutralized (Stage 6) gets triple protection.

#### Scenario A: Triple Stack Works (MON+BX + rPL4 vaccine, best case)

| Component | Mechanism | Estimated incidence reduction | Evidence |
|---|---|---|---|
| MON+BX | Reduced acidosis bouts + partial anti-Fn at rumen wall | 34% reduction vs untreated (28.5% vs 43.1%) | [ESTABLISHED -- single study] |
| rPL4 vaccine | Leukotoxin neutralization of bacteria that DO translocate | Under reduced burden from MON+BX: 40-60% reduction of remaining rumen-origin abscesses | [INFERRED -- extrapolating Fusogard forage-diet efficacy to reduced-burden context] |
| Combined (multiplicative) | MON+BX blocks 34%; of remaining 66%, vaccine blocks 40-60% of rumen-origin (76% of that 66%) | 34% + (66% x 76% x 50%) = 34% + 25% = **~59% total reduction** | [INFERRED] |
| + Hindgut intervention (#9) | If effective against hindgut-origin 24% | Additional 12-19% of total = total **~71-78%** | [PRELIMINARY -- contingent on KE#1] |

**Scenario A coverage: ~59-78% of total incidence prevented**
- Without hindgut component: ~59% -- **FAILS 70% test**
- With effective hindgut component: ~71-78% -- **PASSES 70% test (barely)**

#### Scenario B: Vaccine Fails on Grain Diet (MON+BX alone + hindgut)

| Component | Estimated reduction | Evidence |
|---|---|---|
| MON+BX | 34% | [ESTABLISHED -- single study] |
| Barrier integrity (#2 butyrate) | 5-15% additional | [INFERRED] |
| Hindgut prebiotic (#9) | 5-12% additional | [PRELIMINARY] |
| Total | **~44-61%** | -- |

**Scenario B coverage: ~44-61% -- FAILS 70% test**

#### Scenario C: MON+BX Fails to Replicate (vaccine + hindgut only)

| Component | Estimated reduction | Evidence |
|---|---|---|
| rPL4 vaccine (without burden reduction) | 0-20% on grain diet (Fusogard historical performance) | [ESTABLISHED -- Fusogard fails on grain] |
| Hindgut prebiotic (#9) | 5-12% | [PRELIMINARY] |
| Total | **~5-32%** | -- |

**Scenario C coverage: ~5-32% -- FAILS 70% test catastrophically**

---

## Step 5: 70% Test Verdict

### RESULT: CONDITIONAL PASS

The portfolio passes the 70% tractable pathology test ONLY under Scenario A (Triple Stack works AND hindgut intervention is effective). This requires:

1. MON+BX replicates in an independent trial (Board prerequisite)
2. rPL4 vaccine sustains protective titers for 150+ days on grain diets (unprecedented)
3. The burden reduction from MON+BX is sufficient to bring translocation volume into the range where the vaccine works (the Fusogard-on-forage logic applied to a reduced-challenge grain-diet context)
4. KE#1 confirms hindgut-origin abscesses are a significant fraction (~24%)
5. A hindgut intervention effectively reduces hindgut-origin abscesses

**If ANY of conditions 1-3 fails, coverage drops below 70%.**

### Gap Analysis

| Gap | Impact | Candidate needed |
|---|---|---|
| **Hindgut pathway has no validated intervention** | 24% of abscesses cannot be prevented by rumen-focused strategies | KE#1 must determine if this gap is real and whether it is even larger under tylosin |
| **No surviving candidate for Stage 4 (rumen translocation) beyond barrier overlap** | The rate-limiting barrier (colonization -> translocation) has limited direct coverage | Stage 4 is partially addressed by Stages 2-3 interventions reducing upstream colonization |
| **Stages 7 and 11 have zero candidates (non-tractable post-kills)** | Accepted gap -- upstream prevention makes downstream stages moot | No action unless upstream interventions fail |
| **Stage 9 has only basic research candidates** | The self-reinforcing immune destruction cycle is not pharmacologically interrupted | The $20-30K in vitro experiment on tylosin immunomodulation could open this stage |

### Honest Assessment

This portfolio is at the boundary of the 70% test. The conditional pass depends on the Triple Stack combination working as hypothesized, which is unproven. The Board is correct that the de-risk sequence (KE#1 -> MON+BX replication -> vaccine foundation) must run before committing to the combination trial.

**The hardest truth:** The only interventions with cattle data in the portfolio -- MON+BX (~34% reduction) and Fusogard on forage (~73% reduction) -- suggest that even the best non-antibiotic combination may plateau at 50-60% reduction. Reaching 70%+ likely requires the hindgut intervention to work AND the vaccine to overcome 30 years of grain-diet failure. This is possible but not probable.

---

## Coverage Map Summary Table

| Tractable Stage | Surviving/Wounded Candidates | Best-case coverage | Confidence | Key dependency |
|---|---|---|---|---|
| 2. Barrier damage | #2 (wounded), #3 (wounded) | 11-19% of total | LOW | Ussing chamber experiment |
| 3. Colonization | #1 (survived), #4 (wounded-severe), #6, #25, #23 (wounded) | 25-40% of total | MODERATE | MON+BX replication |
| 4. Translocation (rumen) | #8 (wounded) | 0-11% of total | VERY LOW | Intranasal IgA feasibility |
| 5. Translocation (hindgut) | #9 (survived), #10 (wounded) | 12-19% of total | LOW | KE#1 |
| 6. Immune evasion | #12 (survived), #13 (wounded) | 30-53% of total | LOW-MODERATE | Adjuvant titer duration; PL4 conservation; rumen IgG access |
| 8. Polymicrobial synergy | #16, #17 (wounded) | 5-10% severity | VERY LOW | T. pyogenes in only 29% of cases |
| 9. Abscess formation | #18 (wounded) | 0% near-term | N/A | Basic research |

**Combination coverage (Triple Stack + hindgut): ~71-78% best case, ~44-61% likely case**

**70% Test: CONDITIONAL PASS (best case) / LIKELY FAIL (realistic case)**

---

## Recommendation to Overwatch

The 70% test yields a conditional pass that depends on multiple unvalidated assumptions. I am flagging this honestly rather than inflating estimates. The portfolio's path to 70% is:

1. Run KE#1 immediately ($15-20K) -- determines hindgut contribution
2. Replicate MON+BX ($80-100K) -- validates the burden reduction backbone
3. Run vaccine foundation package ($35-50K) -- validates or kills the vaccine strategy
4. If all three pass: run the Triple Stack trial ($150-200K)

If the Triple Stack fails, the portfolio does not reach 70% with current candidates. In that scenario, Forge should be sent back to propose additional candidates for Stages 3-4 (rumen wall colonization and translocation) with a specific mandate: **find interventions that directly reduce F. necrophorum load at the rumen wall, not just modify fermentation patterns**. The failure analysis's clearest lesson -- that selectivity at the wall matters more than anything else -- has not been fully exploited by the current portfolio.
