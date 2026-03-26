# Phase 5: Coverage Map -- The 70% Pathology Reduction Test

**Program:** Mastitis | **Partner:** Zoetis
**Agent:** Anvil | **Date:** 2026-03-26 | **Revision:** R0
**Primary pathogen:** *Staphylococcus aureus* (bovine mastitis)
**Inputs:** Phase 1 Disease Map (R1), Phase 2 Failure Analysis (R1), Phase 3 Candidates (R0), Phase 3b Survey Report (R0), Phase 4 Kill Report (R0), External Review Corrected Scorecard (6 reviewers)

---

## Methodology

The 70% test asks: if every surviving candidate works perfectly, does total pathology drop by at least 70%?

To answer this honestly:
1. Each disease stage is assigned a **pathology weight** -- its contribution to the overall burden of *S. aureus* mastitis pathology. Weights are based on clinical outcome attribution, knockout/mutant phenotype data, epidemiological data, and expert inference. Where data are insufficient, the reasoning is stated and the estimate tagged [INFERRED].
2. For each stage, surviving candidates are mapped with a **maximum coverage estimate** -- the maximum fraction of that stage's pathology that the candidate could address if it works perfectly.
3. Stage coverage = stage weight x maximum coverage estimate.
4. Total coverage = sum of all stage coverages.

**Critical constraint:** The disease map describes a **multi-barrier model**, not a single rate-limiting barrier. Pathology contributions are not independent -- barriers interact. A candidate that addresses Stage 5 (chronic persistence) also addresses Stage 7 (reseeding) indirectly. These dependencies are noted but not double-counted.

---

## Surviving Candidates (Post-External Review)

| # | Candidate | Verdict | Disease Stages |
|---|-----------|---------|----------------|
| 0B | Ca/BHBA management protocol | SURVIVED | Stage 0 |
| 3B | LukMF' toxoid vaccine | SURVIVED (precision component) | Stage 3, Stage 4 |
| 3C | Mucosal IgA vaccination | SURVIVED (upgraded from WOUNDED) | Stage 3, Stage 2 |
| 5A | Lactoferrin + pirlimycin | SURVIVED | Stage 5, Stage 6 |
| 6A | Phage cocktail | SURVIVED | Stage 6, Stage 5 |
| 6B | Endolysin + pirlimycin | SURVIVED (upgraded from WOUNDED) | Stage 6, Stage 5 |
| 7A | Solve Stage 5 = Solve Stage 7 | SURVIVED (strategic principle) | Stage 7 |
| 7C | Herd management tool | SURVIVED | Stage 7 |

**Note on non-product survivors:** 0B (management protocol), 7A (strategic principle), and 7C (diagnostic-guided management) are biologically valid but are not therapeutic products. They contribute to the coverage map because they reduce pathology, but they are not portfolio assets for de-risk investment.

---

## Disease Stage Pathology Weights

### How Weights Were Derived

The multi-barrier model (Phase 1) identifies five co-equal barriers to cure: (A) intracellular persistence and phenotypic switching, (B) fibrosis and microabscess compartmentalization, (C) biofilm, (D) host factors, and (E) AMR selection dynamics. These map across the nine disease stages. Pathology weights reflect clinical and epidemiological evidence for each stage's contribution to the overall burden of *S. aureus* mastitis (new infection incidence + treatment failure + recurrence + production loss).

| Stage | Description | Weight | Evidence Basis |
|-------|-------------|--------|----------------|
| **0** | Upstream systemic modifiers | **8%** | Subclinical ketosis (BHBA >1.2 mmol/L) is a significant risk factor for clinical mastitis. Transition-period immunosuppression compounds all downstream barriers. Gut-mammary axis contribution unquantified. [MODERATE for BHBA/Ca; INFERRED for gut-mammary] |
| **1** | Entry and exposure | **7%** | Teat canal is the first barrier; ITS reduces new IMI by ~40% (OR 0.29). Milking hygiene and teat-end condition are established risk factors. Well-managed herds already address most of this stage. [ESTABLISHED] |
| **2** | Adhesion and colonization | **8%** | MSCRAMM-mediated adhesion and FnBP-mediated internalization are prerequisites for chronic infection. FnBP-deficient mutants show >95% reduction in internalization. But adhesion is a gateway step, not a direct pathology contributor -- its weight derives from enabling downstream stages. [ESTABLISHED for mechanism; INFERRED for weight] |
| **3** | Immune evasion | **15%** | SpA (Fc + Fab binding), LukMF' (neutrophil killing via CCR1), capsule (anti-phagocytic), AdsA (adenosine-mediated suppression), superantigens (polyclonal T-cell waste). These mechanisms collectively prevent immune clearance, which is why 65-80% of untreated infections become chronic. NLRP3 inflammasome modulation now understood as protective (KO mice: 50% mortality within 24h). [ESTABLISHED for immune evasion; MODERATE for quantitative contribution] |
| **4** | Acute pathology and tissue damage | **10%** | Hla pore formation, LukMF'-mediated neutrophil killing, Hlb sphingomyelinase activity, neutrophil-mediated collateral damage. Fibrosis and microabscess formation begin here and progress through Stage 5. Direct tissue damage reduces milk production (~1.44 kg/day per log SCC unit). [ESTABLISHED] |
| **5** | Chronic persistence | **25%** | The central disease stage. Intracellular survival, SCVs, biofilm -- three co-equal persistence mechanisms. Extended pirlimycin data (13% to 86% cure rate over 2 to 8 days) prove that most treatment failure is pharmacokinetic, but the residual ~15% failure rate represents a biological barrier no antibiotic can breach. This stage sets the cure rate ceiling. [ESTABLISHED] |
| **6** | Treatment resistance | **12%** | The five barriers to antibiotic cure (intracellular inaccessibility, biofilm tolerance, fibrosis compartmentalization, milk matrix interference, phenotypic tolerance). Current cure rates 20-35% during lactation, 40-70% at dry-off. AMR dynamics further reduce cure probability over time. [ESTABLISHED] |
| **7** | Reinfection and reseeding | **10%** | Contagious transmission at milking, within-cow quarter-to-quarter spread, SCV reversion and intracellular release. Even after bacteriological cure, intracellular reservoirs can reseed infection. The 5-point plan reduces but does not eliminate transmission. [ESTABLISHED for transmission; MODERATE for SCV reseeding] |
| **8** | Resolution and remodeling | **5%** | Post-cure SCC recovery, tissue remodeling (reversible vs. permanent fibrosis), microbiome re-equilibration. Fibrotic tissue is largely irreversible. This stage determines the ceiling on production recovery even after successful cure. [MODERATE] |
| | **TOTAL** | **100%** | |

---

## Coverage Analysis by Stage

### Stage 0: Upstream Systemic Modifiers (8%)

**Surviving candidates:**
- **0B Ca/BHBA management protocol** -- biologically sound management intervention targeting BHBA-mediated neutrophil dysfunction and hypocalcemia-mediated phagocytosis impairment.

**Coverage estimate:** The BHBA-neutrophil link is ESTABLISHED (PMID 18411287). Subclinical ketosis is a significant risk factor. However, this is a management practice, not a product. Well-managed herds already implement transition management. The incremental benefit for such herds is small; for poorly managed herds (majority globally), it could reduce mastitis incidence by an estimated 15-25%.

**Maximum pathology reduction from Stage 0:** 0B addresses metabolic predisposition directly. If it works perfectly in a poorly managed herd: 50% of Stage 0 pathology addressed.

**Stage 0 coverage contribution:** 8% x 50% = **4.0%** [MODERATE/INFERRED]

---

### Stage 1: Entry and Exposure (7%)

**Surviving candidates:** None directly.

**Indirect coverage:** ITS (existing product, not a novel candidate) already reduces new IMI by ~40%. No surviving candidate adds to Stage 1 coverage beyond what is already commercially available.

**Stage 1 coverage contribution:** **0%** (no novel coverage -- existing ITS is baseline)

**GAP IDENTIFIED:** No surviving candidate addresses entry and exposure. The wounded candidates (1A antimicrobial sealant, 1B NAS teat dip) were not upgraded in external review.

---

### Stage 2: Adhesion and Colonization (8%)

**Surviving candidates:**
- **3C Mucosal IgA vaccination** (secondary mechanism -- anti-adhesion via sIgA against ClfA/FnBP).

**Coverage estimate:** Mucosal IgA vaccination was UPGRADED from WOUNDED. Cattle studies show mammary IgA induction via nasal immunization. *S. aureus*-specific IgA in milk demonstrated. sIgA does not bind SpA (bypasses the central immune evasion mechanism). However: (a) bovine mammary MALT-like structures exist but functional sIgA generation from intramammary delivery is still unconfirmed, (b) IgA primarily prevents adhesion, not intracellular clearance.

If mucosal IgA works perfectly: could prevent 30-50% of new adhesion/colonization events by blocking MSCRAMM binding before it starts.

**Stage 2 coverage contribution:** 8% x 40% = **3.2%** [INFERRED -- sIgA anti-adhesion mechanism extrapolated from human mucosal immunology]

---

### Stage 3: Immune Evasion (15%)

**Surviving candidates:**
- **3B LukMF' toxoid vaccine** -- neutralizes the most potent bovine neutrophil-killing toxin. Dutch isolates: 96% lukM/lukF' positive. Market segmentation approach -- pair with strain diagnostics.
- **3C Mucosal IgA vaccination** -- sIgA bypasses SpA entirely (SpA does not bind IgA). Could restore functional antibody-mediated opsonization in the mammary gland.

**Coverage estimate:**

*3B LukMF' toxoid:* Preserving neutrophil function by neutralizing LukMF' is mechanistically direct. LukMF' is the most potent anti-neutrophil weapon in bovine-adapted strains. However, coverage is strain-dependent: CC151 carries lukM at high frequency; CC97 at ~30%. In the Dutch market (96% lukM-positive), coverage is near-complete. In other markets, coverage may be 50-70%. Assume target market average of 70% strain coverage. If neutralizing LukMF' restores neutrophil function, it addresses ~40% of immune evasion pathology (LukMF' is one of several evasion mechanisms -- SpA, capsule, AdsA, superantigens operate independently).

*3C Mucosal IgA:* If functional mammary sIgA against *S. aureus* surface antigens is achievable, it circumvents SpA completely. SpA accounts for roughly 30-40% of immune evasion (both Fc-binding and Fab-mediated B-cell effects). sIgA that can opsonize without SpA interference could restore phagocytic clearance. Maximum: 30% of immune evasion addressed if sIgA response is robust.

Combined (3B + 3C): Partial overlap (both improve immune clearance) but different mechanisms (toxin neutralization vs. antibody-mediated opsonization). Combined maximum: 50% of Stage 3.

**Stage 3 coverage contribution:** 15% x 50% = **7.5%** [MODERATE for LukMF'; INFERRED for mucosal IgA]

---

### Stage 4: Acute Pathology and Tissue Damage (10%)

**Surviving candidates:**
- **3B LukMF' toxoid vaccine** (secondary mechanism -- reduces neutrophil killing, which reduces collateral immune-mediated tissue damage).

**Coverage estimate:** LukMF' neutralization protects neutrophils from killing. Surviving neutrophils clear bacteria more effectively AND cause less collateral tissue damage (fewer dying neutrophils releasing ROS and proteases). This is an indirect benefit. Hla and Hlb still cause direct epithelial damage -- no surviving candidate addresses these. Maximum: 25% of Stage 4 (neutrophil survival reduces collateral damage but does not address direct toxin-mediated epithelial damage).

**Stage 4 coverage contribution:** 10% x 25% = **2.5%** [INFERRED]

---

### Stage 5: Chronic Persistence (25%)

**Surviving candidates:**
- **5A Lactoferrin + pirlimycin** -- iron chelation, beta-lactamase suppression, pirlimycin intracellular accumulation. Multi-mechanism. Real bovine data (45.5% cure in experimentally induced resistant infection; 33.3% in naturally acquired chronic). Natively stable in milk matrix.
- **6A Phage cocktail** (secondary mechanism -- phage can penetrate biofilm and lyse bacteria within biofilm matrix, including some activity against metabolically dormant cells).
- **6B Endolysin + pirlimycin** (secondary mechanism -- endolysin kills extracellular/biofilm bacteria, pirlimycin handles intracellular fraction).

**Coverage estimate:**

*5A Lactoferrin + pirlimycin:* This is the strongest surviving candidate for Stage 5. Lactoferrin creates iron stress (forcing metabolic changes in intracellular bacteria), suppresses beta-lactamase transcription (restoring antibiotic susceptibility), and pirlimycin accumulates intracellularly. The combination addresses intracellular persistence and partial biofilm disruption (pirlimycin at sub-MIC reduces biofilm). Corrected cure rates: 33-45.5% (below what Forge implied, per Reaper's citation verification). Maximum stage coverage if working perfectly: 40% of Stage 5 (addresses intracellular + partial biofilm, but does NOT address SCVs or fibrosis/microabscess compartmentalization).

*6A Phage cocktail (secondary):* Phage can penetrate biofilm matrix and lyse bacteria. Kromker 2026 achieved 81.3% cure (CI 57-94%, n=16). Phage primarily kills extracellular and biofilm bacteria -- limited intracellular access. Secondary contribution to Stage 5: 15% (biofilm component only).

*6B Endolysin + pirlimycin (secondary):* Endolysin kills extracellular/biofilm bacteria via cell wall hydrolysis (AMR-orthogonal). Variable milk matrix activity (Phase 2 Section 7). Secondary contribution: 10% (extracellular/biofilm, limited by milk matrix variability).

Combined (5A + 6A + 6B): These candidates address different sub-barriers within Stage 5 (intracellular, biofilm, extracellular). Some overlap in biofilm targeting. Combined maximum: 55% of Stage 5.

**CRITICAL GAP:** No surviving candidate addresses **SCV dormancy** directly. The SCV wake-and-kill candidate (5E, menadione) was KILLED in external review because menadione at SCV-reverting concentrations (0-10 uM) causes oxidative damage to MAC-T cells -- no therapeutic window. ADEP/ClpP (5B) was also KILLED unless pivoted to ZG-series non-ADEP selective ClpP activators (noted as future opportunity, not current asset). This means the deepest persistence mechanism -- the SCV phenotypic switch -- has **ZERO coverage** in the surviving portfolio.

**Stage 5 coverage contribution:** 25% x 55% = **13.75%** [MODERATE for 5A; PRELIMINARY for 6A secondary; PRELIMINARY for 6B secondary]

---

### Stage 6: Treatment Resistance (12%)

**Surviving candidates:**
- **6A Phage cocktail** -- AMR-orthogonal killing mechanism. Lytic phage kill bacteria regardless of antibiotic resistance genotype.
- **6B Endolysin + pirlimycin** -- endolysin is AMR-orthogonal (cell wall hydrolysis, not antibiotic target). Pirlimycin provides intracellular component.
- **5A Lactoferrin + pirlimycin** (secondary -- lactoferrin suppresses beta-lactamase transcription, restoring susceptibility to beta-lactams).

**Coverage estimate:**

*6A Phage cocktail:* Completely bypasses genetic AMR. The 81.3% cure rate (if replicated) would exceed all antibiotic regimens for *S. aureus* mastitis. Maximum: 60% of Stage 6 (addresses genetic resistance completely, but does not address phenotypic tolerance/persister cells).

*6B Endolysin + pirlimycin:* Endolysin bypasses AMR. Combined with pirlimycin intracellular activity. Maximum: 40% of Stage 6.

*5A Lactoferrin (secondary):* Beta-lactamase suppression specifically restores susceptibility of blaZ-positive strains. Maximum secondary contribution: 15%.

Combined: Some overlap (all address AMR bypass). Combined maximum: 65% of Stage 6.

**Stage 6 coverage contribution:** 12% x 65% = **7.8%** [PRELIMINARY for phage; MODERATE for lactoferrin beta-lactamase suppression]

---

### Stage 7: Reinfection and Reseeding (10%)

**Surviving candidates:**
- **7A Solve Stage 5 = Solve Stage 7** -- correct strategic principle. If Stage 5 candidates eliminate the intracellular reservoir, endogenous reseeding becomes impossible.
- **7C Herd management tool** -- diagnostic-guided segregation/culling interrupts contagious transmission.

**Coverage estimate:**

*7A Strategic principle:* Stage 5 coverage is 55% (see above). Therefore, the reseeding component attributable to intracellular reservoir elimination is 55% of the internal reseeding fraction. Internal reseeding (SCV reversion, intracellular release) accounts for approximately 40% of Stage 7 pathology; contagious transmission (milking, fomites) accounts for the remaining 60%. Maximum contribution: 55% x 40% = 22% of Stage 7 via internal reseeding prevention.

*7C Herd management:* Diagnostic-guided segregation and milking order interrupts contagious transmission. The 5-point plan is already ESTABLISHED but imperfect. Adding rapid strain-typing diagnostics could improve segregation effectiveness by 20-30%. Maximum contribution: 25% of Stage 7 (contagious transmission component).

Combined: 22% + 25% = 47% of Stage 7. These address different reinfection routes (endogenous vs. exogenous) with minimal overlap.

**Stage 7 coverage contribution:** 10% x 47% = **4.7%** [INFERRED]

---

### Stage 8: Resolution and Remodeling (5%)

**Surviving candidates:** None.

**Coverage:** APT (8A) was KILLED in external review because ALL published studies are manufacturer-funded with COI (lead author = CMO of Armenta). Zero independent replication. Pirfenidone (8B) was killed on biology (treatment window too short). Post-treatment probiotic (8C) was REVIVED from KILLED as WOUNDED (intramammary *Lactococcus lactis* field trials exist), but it is not a primary portfolio asset.

**Stage 8 coverage contribution:** **0%**

**GAP IDENTIFIED:** No surviving candidate addresses resolution and tissue remodeling. Fibrosis is a co-equal barrier to cure (Phase 1 multi-barrier model), and no intervention prevents or reverses it.

---

## Coverage Summary

| Stage | Weight | Coverage % | Contribution | Primary Candidates |
|-------|--------|-----------|--------------|-------------------|
| 0. Upstream systemic | 8% | 50% | 4.0% | 0B (Ca/BHBA management) |
| 1. Entry/exposure | 7% | 0% | 0.0% | NONE |
| 2. Adhesion/colonization | 8% | 40% | 3.2% | 3C (mucosal IgA) |
| 3. Immune evasion | 15% | 50% | 7.5% | 3B (LukMF' toxoid), 3C (mucosal IgA) |
| 4. Acute pathology | 10% | 25% | 2.5% | 3B (LukMF' -- secondary) |
| 5. Chronic persistence | 25% | 55% | 13.75% | 5A (lactoferrin + pirlimycin), 6A (phage -- secondary), 6B (endolysin -- secondary) |
| 6. Treatment resistance | 12% | 65% | 7.8% | 6A (phage), 6B (endolysin), 5A (lactoferrin -- secondary) |
| 7. Reinfection/reseeding | 10% | 47% | 4.7% | 7A (strategic), 7C (management tool) |
| 8. Resolution/remodeling | 5% | 0% | 0.0% | NONE |
| **TOTAL** | **100%** | | **43.45%** | |

---

## VERDICT: FAIL

**Total coverage: 43.45% -- BELOW the 70% threshold.**

The portfolio fails the 70% test by a substantial margin (26.55 percentage points short). This is not a borderline failure -- the portfolio is structurally incomplete.

---

## Gap Analysis

### Critical Gaps (stages with zero or near-zero coverage from surviving candidates)

**1. Stage 1: Entry and Exposure (7% weight, 0% coverage)**
No surviving candidate addresses pathogen entry. Existing ITS is the baseline -- the portfolio adds nothing above current commercial products.

**Impact:** Moderate. Stage 1 is a prevention stage. Existing products (ITS, teat dips) partially address it. The gap is real but not the primary driver of the 70% failure.

**2. Stage 5: SCV Dormancy Sub-barrier (within the 25% Stage 5 weight)**
The surviving candidates address intracellular persistence (lactoferrin + pirlimycin) and biofilm (phage, endolysin) but NOT SCV dormancy. The SCV wake-and-kill candidate (5E) was KILLED. ADEP/ClpP (5B) was KILLED. No surviving candidate can kill or reactivate dormant SCV populations.

**Impact:** CRITICAL. SCVs are the deepest persistence mechanism. They are invisible to diagnostics, immune to antibiotics, and capable of reseeding infection indefinitely. Without SCV coverage, Stage 5 coverage is capped at ~55% and the residual 45% represents an irreducible treatment failure rate driven by SCV dormancy.

**3. Stage 8: Resolution and Remodeling (5% weight, 0% coverage)**
APT (the only candidate addressing tissue repair) was KILLED for COI. Pirfenidone was KILLED on biology. No surviving candidate addresses fibrosis, which is a co-equal barrier to cure.

**Impact:** Moderate individually (5% weight), but fibrosis also limits the effectiveness of Stage 5 and Stage 6 candidates by creating physical barriers to drug delivery.

### Structural Gaps

**4. No persister-killing mechanism in the portfolio.**
The portfolio has no mechanism to kill metabolically dormant cells (SCVs, biofilm persisters). All surviving candidates work on metabolically active bacteria. The ~15% residual failure rate of 8-day pirlimycin (the best current therapy) is likely driven by dormant cells, and nothing in the surviving portfolio addresses this population.

**5. SrtA inhibitor was DOWNGRADED from SURVIVED to WOUNDED.**
SrtA (2A) was the only multi-barrier small-molecule target (adhesion + immune evasion + internalization prevention). Its downgrade to WOUNDED (22+ years, no drug-quality compound, PAINS-dominated field, discovery-stage only) removes the most versatile target from the portfolio.

---

## What Must Happen to Pass

The portfolio needs approximately **27 additional percentage points** of coverage. The most efficient routes:

### Route 1: Rehabilitate Wounded Candidates
The external review created 14 WOUNDED candidates. Several have defined questions that, if answered, would significantly increase coverage:

1. **SrtA inhibitor (2A, WOUNDED):** If a drug-quality SrtA inhibitor can be identified, it addresses Stages 2, 3, and 5 simultaneously. Potential coverage gain: +8-12%.
2. **NLRP3 activator (4B, WOUNDED -- REVIVED):** External review corrected Reaper's kill. NLRP3 ACTIVATION (not inhibition) is the correct therapeutic direction -- overriding *S. aureus* PINK1/Parkin suppression. NLRP3 is protective (KO mice: 50% mortality). Compound tested in bovine mastitis model (Thacker et al. 2012). Potential coverage gain: +3-5% (Stage 4 + partial Stage 3).
3. **A2aR antagonism pathway (3D, WOUNDED -- REVIVED and RESCOPED):** AdsA inhibition alone may be redundant with SrtA, but host-target A2aR antagonism is independently druggable. A2aR antagonism enhanced *S. aureus*-specific Th17 responses in mice. Potential coverage gain: +2-3% (Stage 3).
4. **Post-treatment probiotic (8C, WOUNDED -- REVIVED):** Intramammary *Lactococcus lactis* field trials exist. Potential coverage gain: +2-3% (Stage 8).

### Route 2: Return to Forge for Gap Stages
Forge must be asked to propose new candidates specifically for:
- **SCV dormancy:** The wake-and-kill concept (5E) and ADEP/ClpP (5B) were both killed. A new mechanism for killing or reactivating dormant cells is needed. The ZG-series non-ADEP selective ClpP activators noted in the 5B kill were flagged as a future opportunity -- this should become a current opportunity.
- **Stage 8 fibrosis:** Need a commercially viable anti-fibrotic approach, not pirfenidone.
- **Stage 1 entry:** Novel teat-level prevention beyond existing ITS.

### Route 3: Accept Realistic Ceiling
If the above routes do not yield sufficient additional coverage, the portfolio coverage ceiling should be honestly reported as ~55-60% maximum with full rehabilitation of wounded candidates + Forge re-run for gap stages. The 70% test may require an additional iteration cycle.

---

## Recommendation to Overwatch

**STOP. Do not proceed to full portfolio construction.**

The surviving portfolio covers 43.45% of *S. aureus* mastitis pathology. This is below the 70% threshold by 26.55 percentage points. Proceeding to partner-grade deliverables with this coverage would violate Principle 9 and Quality Standard 19.

**Recommended actions:**

1. **Immediate:** Incorporate the 4 WOUNDED candidates with corrected verdicts from external review (NLRP3 activator, A2aR pathway, post-treatment probiotic, SrtA inhibitor as discovery-stage target) into the coverage analysis. This could add 15-23% coverage if the de-risk questions are answered.

2. **If coverage with rehabilitated wounded candidates reaches 60-65%:** Proceed with portfolio construction using a tiered approach -- Tier 1 (survived, de-risked) and Tier 2 (wounded, conditional on de-risk gates). Present to partner with honest coverage estimate and identified gaps.

3. **If coverage remains below 60%:** Send Forge back for SCV dormancy, Stage 8 fibrosis, and Stage 1 entry.

---

## REVISED ANALYSIS: Including Conditionally Rehabilitated Wounded Candidates

Given that the external review upgraded several candidates and the Overwatch instructions specify using the corrected scorecard, I will re-run the coverage analysis including wounded candidates that have defined, achievable de-risk gates, presented as **conditional coverage** -- coverage that is unlocked IF the de-risk experiment passes.

### Additional Candidates (Conditional -- Wounded with Defined Gates)

| # | Candidate | Status | De-Risk Gate | Stages |
|---|-----------|--------|--------------|--------|
| 2A | SrtA inhibitor | WOUNDED | Identify drug-quality compound from recent covalent inhibitor literature | 2, 3, 5 |
| 4B | NLRP3 activator | WOUNDED (REVIVED) | Bovine mammary cell model confirming NLRP3 activation protects against *S. aureus* | 4, 3 |
| 3D | A2aR antagonism | WOUNDED (REVIVED, RESCOPED) | A2aR antagonist enhances Th17 response against bovine *S. aureus* isolates | 3 |
| 0A | Protected butyrate | WOUNDED | Gut-mammary axis contribution to bovine mastitis quantified at >10% | 0 |
| 8C | Post-treatment probiotic | WOUNDED (REVIVED) | Intramammary *L. lactis* does not cause SCC elevation above 200K | 8 |
| 5B | ZG-series ClpP activator | NOTED (future, from 5B kill) | Non-ADEP scaffold selective for bacterial over mammalian ClpP | 5 |

### Revised Coverage with Conditional Candidates

| Stage | Weight | Base Coverage | Conditional Addition | Total | Key Conditional Candidates |
|-------|--------|--------------|---------------------|-------|---------------------------|
| 0 | 8% | 4.0% | +1.6% | 5.6% | 0A (butyrate, conditional) |
| 1 | 7% | 0.0% | 0.0% | 0.0% | NONE |
| 2 | 8% | 3.2% | +2.4% | 5.6% | 2A (SrtA, conditional) |
| 3 | 15% | 7.5% | +4.5% | 12.0% | 2A (SrtA blocks SpA), 4B (NLRP3 activation), 3D (A2aR) |
| 4 | 10% | 2.5% | +2.0% | 4.5% | 4B (NLRP3 activation reduces tissue damage) |
| 5 | 25% | 13.75% | +5.0% | 18.75% | 2A (SrtA prevents new internalization), 5B/ZG (ClpP if selective scaffold found) |
| 6 | 12% | 7.8% | 0.0% | 7.8% | (already well-covered) |
| 7 | 10% | 4.7% | +1.5% | 6.2% | (indirect from Stage 5 improvement) |
| 8 | 5% | 0.0% | +1.5% | 1.5% | 8C (post-treatment probiotic, conditional) |
| **TOTAL** | **100%** | **43.45%** | **+18.5%** | **~62%** | |

### Revised Verdict: CONDITIONAL PASS POSSIBLE BUT NOT ACHIEVED

With full rehabilitation of all wounded candidates with favorable external review corrections, total coverage reaches approximately **62%** -- still below the 70% threshold but much closer.

**The remaining 8% gap** is driven by:
- Stage 1 (7% weight, 0% coverage) -- no novel entry-prevention candidate
- Stage 5 SCV sub-barrier -- even with ZG-series ClpP activators, SCV coverage is uncertain
- Stage 8 (5% weight, 1.5% coverage) -- minimal resolution/remodeling capability

---

## FINAL RECOMMENDATION

**To Overwatch: The portfolio in its current form (8 survivors post-external review) covers 43.45% of pathology and FAILS the 70% test.**

**With conditional rehabilitation of wounded candidates that received favorable external review corrections, coverage reaches ~62% -- still short of 70%.**

**Decision required:**

**Option A:** Send Forge back for the following gap stages with specific briefs:
- SCV dormancy: Need a new mechanism (ZG-series ClpP is the best lead)
- Stage 1: Novel teat-level prevention
- Stage 8: Commercially viable anti-fibrotic or tissue recovery approach

**Option B:** Accept a ~62% conditional coverage portfolio and proceed to partner deliverables with honest gap disclosure. This requires Daniel's approval to proceed below the 70% threshold.

**Option C:** Hybrid -- proceed with portfolio construction for the ~62% conditional portfolio while Forge works on the gap stages in parallel. Present to Zoetis with identified gaps and a plan to fill them.

---

*This coverage map was compiled using corrected verdicts from six external reviewers (Gemini Pro, GPT-5.4, Gemini Extended Thinking, Claude Web, Edison/PaperQA3, GPT-5.4 Web). Pathology weights are based on the Phase 1 disease map multi-barrier model. Coverage estimates use corrected cure rate data from Reaper's primary source verification (lactoferrin: 33-45.5%, not higher; phage: CI 57-94%, n=16). All estimates tagged with evidence tiers per Quality Standard 1.*
