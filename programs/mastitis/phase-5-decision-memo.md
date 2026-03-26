# Phase 5: Decision Memo -- Bovine *S. aureus* Mastitis Drug Discovery Portfolio

**Program:** Mastitis | **Partner:** Zoetis
**Agent:** Anvil | **Date:** 2026-03-26 | **Revision:** R0
**Prepared for:** Senior R&D leadership, Zoetis
**Prepared by:** Agteria drug discovery pipeline (6-agent system with 6 external reviewers)

---

## Executive Summary

We mapped *S. aureus* bovine mastitis across 9 disease stages, analyzed 16 failed treatment approaches, proposed 32 novel intervention candidates, subjected them to adversarial kill review and 6-model external validation, and distilled the survivors into a portfolio.

**The honest answer:** The surviving portfolio, if every candidate works perfectly, covers approximately 62% of *S. aureus* mastitis pathology. This is below our 70% internal threshold and reflects a genuine gap -- no surviving candidate can kill dormant small-colony variants (SCVs), the deepest persistence mechanism. We are not hiding this gap. We are presenting what we found, what it costs to test, and what happens if it works.

**The portfolio has three primary assets:**

| Priority | Candidate | What It Does | De-Risk Cost | Timeline | Key Gate |
|----------|-----------|-------------|-------------|----------|----------|
| **1** | Phage cocktail | AMR-orthogonal killing; 81.3% cure in pilot (n=16) | $150-200K | 12 months | Independent replication: cure rate >60% at n=80 |
| **2** | Lactoferrin + pirlimycin | Multi-mechanism cure: iron chelation + intracellular antibiotic | $150-200K | 12 months | Combination exceeds pirlimycin alone by >15 points at n=100 |
| **3** | Endolysin + pirlimycin | AMR-orthogonal enzymatic kill + intracellular antibiotic | $80-120K | 9 months | Consistent activity (>2-log kill) in milk from 20+ cows |

**Two vaccine assets provide immune protection:**

| Priority | Candidate | What It Does | De-Risk Cost | Timeline | Key Gate |
|----------|-----------|-------------|-------------|----------|----------|
| **4** | LukMF' toxoid vaccine | Protects bovine neutrophils from the most potent leukocidin | $70-100K | 12 months | Bovine anti-LukM serum protects neutrophils in bovine whole milk |
| **5** | Mucosal IgA vaccination | Generates SpA-invisible sIgA in milk | $80-120K | 12 months | sIgA/IgG ratio >2 in milk after nasal immunization |

**Total de-risk investment for the 5 primary assets: $530K-740K**

If the phage cocktail replicates at 65%+ and lactoferrin + pirlimycin achieves 50%+ cure, Zoetis would have the first non-antibiotic and the first combination therapeutic to exceed current cure rates for *S. aureus* mastitis during lactation. Either result alone would be commercially significant under EU Regulation 2019/6.

---

## The Problem: Why *S. aureus* Mastitis Is Hard

*S. aureus* bovine mastitis costs the global dairy industry USD 19.7-32 billion annually. Current treatments achieve bacteriological cure rates of only 20-35% during lactation. This is because *S. aureus* deploys at least five co-equal barriers to cure:

1. **Intracellular persistence:** Bacteria invade mammary epithelial cells and hide from antibiotics and immune surveillance.
2. **Biofilm:** 10-1000x antibiotic tolerance for biofilm-embedded bacteria.
3. **Fibrosis/microabscesses:** Physical barriers exclude drugs from reaching bacteria.
4. **Immune evasion:** SpA (subverts IgG), LukMF' (kills neutrophils), capsule (blocks phagocytosis), AdsA (suppresses immune response via adenosine).
5. **Small colony variants (SCVs):** Metabolically dormant phenotypic switch invisible to diagnostics and immune to all antibiotics.

No single treatment addresses more than two of these five barriers. This is why previous portfolio approaches (Argus v8, v9) achieved ~45% pathology coverage and stalled.

---

## What We Did

### Process

| Phase | Agent | What Happened | Output |
|-------|-------|--------------|--------|
| 1. Disease mapping | Pathfinder | Complete 9-stage disease map with multi-barrier model | 930 lines, revised post-external review |
| 2. Failure forensics | Sapper | 16 treatment approaches analyzed for specific failure mechanisms | 1,012 lines, revised post-external review |
| 3. Candidate design | Forge | 32 candidates across all 9 stages (13 Known, 10 Non-Obvious, 9 Novel) | 680 lines |
| 3b. Computational validation | Surveyor | 8 protein targets resolved, conserved, host-selectivity checked | 848 lines |
| 4. Adversarial kill review | Reaper | 8 killed, 16 wounded, 8 survived | 581 lines |
| 5. External validation | 6 independent AI models | Corrected verdicts: 10 killed, 8 survived, 14 wounded | See corrected scorecard |
| 5. Portfolio construction | Anvil | 70% test, evidence register, this memo | Current document |

### Quality Controls

- 35 quality standards enforced (evidence tiers, citation verification, embarrassment passes, realistic cost estimates)
- 6 external reviewers: Gemini Pro, GPT-5.4, Gemini Extended Thinking, Claude Web, Edison/PaperQA3, GPT-5.4 Web
- Primary source verification for all strategic claims (Reaper retrieved and re-read key papers)
- Known corrections logged (lactoferrin cure rates adjusted downward; NLRP3 direction corrected; APT killed for COI; menadione killed for host cell toxicity)

---

## The Portfolio

### Tier 1: De-Risk Now (Survived External Review)

#### 1. Phage Cocktail (Candidate 6A)

**What:** Multi-phage cocktail targeting CC97/CC151/CC479, administered intramammarily at 12-hour intervals (5 doses). Replicates and independently validates the Kromker 2026 protocol.

**Why it matters:** If the 81.3% cure rate replicates at even 65%, this becomes the first non-antibiotic approach to exceed the current standard of care for *S. aureus* mastitis. Under EU Regulation 2019/6 (blanket prophylactic antibiotic ban), non-antibiotic alternatives have regulatory tailwind.

**Evidence:**
- Kromker 2026 pilot RCT: 81.3% cure (13/16), p=0.026 [PRELIMINARY; bovine in-vivo; PMID 41594069]
- Gill 2006 single-phage precedent: 16.7% cure [ESTABLISHED; bovine in-vivo]
- Rational improvement from single phage to cocktail and q24h to q12h dosing
- COI flag: co-author affiliated with Phage Technology Center

**Target Product Profile:**

| Parameter | Specification |
|-----------|--------------|
| Indication | Treatment of *S. aureus* intramammary infection during lactation |
| Route | Intramammary infusion, 5 doses at 12-hour intervals |
| Target population | Lactating dairy cows with confirmed *S. aureus* IMI |
| Target cure rate | >60% bacteriological cure at 21 days post-treatment |
| Target price | $50-100 per treatment course (5 infusions) |
| Withdrawal period | Minimal expected (phage are biological agents, not chemical residues). Must be validated. |
| Regulatory pathway | Novel -- no established FDA-CVM pathway for phage. EU may be more permissive under Regulation 2019/6. USDA-CVB biologics pathway possible. |
| Who buys | Veterinarian administers (5-dose protocol requires compliance management). Sold through veterinary distributors. |

**De-Risk Experiment:**

| Parameter | Detail |
|-----------|--------|
| Design | Multi-farm RCT: phage cocktail (minimum 3 phages covering CC97/CC151/CC479), 5 doses q12h vs. untreated controls |
| Sample size | n=40 treated, n=40 control (per Reaper's recommendation; sufficient to detect 25-point difference at 80% power) |
| Primary endpoint | Bacteriological cure at 21 and 42 days (culture-negative milk, 2 consecutive samples) |
| Secondary endpoints | SCC trajectory, clinical score, relapse rate at 90 days, phage resistance emergence |
| GO gate | Cure rate >60% (lower bound of Kromker CI) |
| KILL gate | Cure rate <40% (not significantly different from extended pirlimycin comparator) |
| Budget | $150,000-200,000 (multi-farm enrollment, phage production, culture costs, statistical analysis) |
| Timeline | 12 months (3 months enrollment, 3 months treatment, 6 months follow-up) |
| What PASS means | First non-antibiotic therapy to exceed current SOC for *S. aureus* mastitis. Zoetis has a novel biological therapeutic with EU regulatory tailwind. |
| What FAIL means | The Kromker result was a statistical artifact. Phage therapy for bovine mastitis requires fundamental redesign. |

**Embarrassment pass:** We replicate Kromker and get 55% cure. It is positive but not transformative. Alternatively, the cocktail shows high efficacy against CC151 but fails against CC97, revealing strain-specific phage susceptibility. The cocktail works but only in herds with the right strain profile.

**Kill criteria (defined before experiment):**
- Cure rate <40% at 21 days: KILL
- Phage resistance in >30% of treated quarters by 42 days: KILL
- Severe adverse reactions (acute inflammatory flare) in >10% of treated quarters: KILL

---

#### 2. Lactoferrin + Pirlimycin Combination (Candidate 5A)

**What:** Bovine lactoferrin (iron chelation, beta-lactamase suppression) combined with pirlimycin (intracellular accumulation). Multi-mechanism approach addressing iron-dependent persistence, antibiotic resistance, and intracellular bacteria simultaneously.

**Why it matters:** The only combination therapeutic with real bovine clinical data showing synergy. Lactoferrin is natively stable in milk (unique among all protein candidates). The beta-lactamase suppression mechanism restores susceptibility to beta-lactams -- a separate value proposition from the iron chelation mechanism.

**Evidence:**
- Trial 1 (experimental, resistant strain): 45.5% cure vs. 9.1% pirlimycin alone [MODERATE; bovine in-vivo; PMID 17517718]
- Trial 2 (natural chronic): 33.3% cure vs. 12.5% pirlimycin alone [MODERATE; bovine in-vivo; PMID 17565052]
- Lactoferrin suppresses blaZ transcription [MODERATE; bovine in-vivo/in-vitro]
- Pirlimycin achieves intracellular accumulation and reduces biofilm at sub-MIC [ESTABLISHED; pharmacokinetics; MODERATE; bovine isolates; PMC5609010]

**Target Product Profile:**

| Parameter | Specification |
|-----------|--------------|
| Indication | Treatment of *S. aureus* IMI during lactation, including beta-lactam-resistant infections |
| Route | Intramammary infusion, 5-day course (combining lactoferrin with pirlimycin in each infusion) |
| Target population | Lactating dairy cows with confirmed *S. aureus* IMI, particularly beta-lactam-resistant strains |
| Target cure rate | >50% bacteriological cure (representing >15-point improvement over pirlimycin alone) |
| Target price | $20-40 per treatment course. Lactoferrin COGS: $12.50-50/dose at current pricing ($50-200/g, 250 mg-1 g/dose). Scale manufacturing could reduce to <$10/dose. Pirlimycin (Pirsue) is already priced. Combined: must remain under $40 total. |
| Withdrawal period | Pirlimycin withdrawal period applies (36 hours milk, 9 days meat). Lactoferrin is a natural milk protein -- minimal additional withdrawal expected. |
| Regulatory pathway | FDA-CVM NADA for combination product (pirlimycin is already approved; lactoferrin is GRAS as food ingredient, but intramammary therapeutic use would require NADA). 2-API combination = 3 trial arms (manageable). |
| Who buys | Veterinarian prescribes; farmer administers (same as current pirlimycin). Sold through veterinary distributor. |

**De-Risk Experiment:**

| Parameter | Detail |
|-----------|--------|
| Design | 3-arm bovine RCT: (a) pirlimycin 5-day, (b) lactoferrin + pirlimycin 5-day, (c) lactoferrin alone 5-day |
| Sample size | n=50 per arm (per Reaper's correction from Forge's n=20; sufficient for 15-point difference at 80% power) |
| Primary endpoint | Bacteriological cure at 21 and 42 days |
| Secondary endpoints | SCC trajectory, relapse at 90 days, beta-lactamase status of surviving isolates |
| GO gate | Combination exceeds pirlimycin alone by >15 percentage points (p<0.05) |
| KILL gate | Combination does not exceed pirlimycin alone by >10 points (p>0.1) |
| Budget | $150,000-200,000 (3-arm trial, CRO costs, culture, statistics) |
| Timeline | 12 months |
| What PASS means | First combination therapeutic with proven synergy for *S. aureus* mastitis. Lactoferrin component restores susceptibility of resistant strains -- a novel mechanism with commercial differentiation. |
| What FAIL means | Lactoferrin synergy is not sufficient to improve outcomes beyond pirlimycin alone. The iron chelation mechanism is real but clinically insufficient. |

**Embarrassment pass:** We run the 3-arm trial and the combination achieves 38% cure vs. 30% pirlimycin alone. The trend is positive but not statistically significant. We have spent $150K to generate an underpowered positive trend.

**Kill criteria:**
- Combination cure rate <35% (absolute): KILL
- Lactoferrin causes adverse mammary reactions (acute SCC flare >5x baseline) in >10% of treated cows: KILL
- Lactoferrin COGS cannot be reduced below $20/dose at commercial scale: KILL (commercial, not biological)

---

#### 3. Endolysin + Pirlimycin Combination (Candidate 6B)

**What:** Engineered endolysin (cell wall hydrolysis, AMR-orthogonal) combined with pirlimycin (intracellular accumulation). Endolysin kills extracellular/biofilm bacteria; pirlimycin handles the intracellular fraction.

**Why it matters:** AMR-orthogonal enzymatic kill mechanism. Exebacase (lysin CF-301) in Phase 3 human trials reduces platform risk for the endolysin class. Trx-SA1 endolysin has demonstrated bovine intramammary efficacy.

**Target Product Profile:**

| Parameter | Specification |
|-----------|--------------|
| Indication | Treatment of *S. aureus* IMI during lactation |
| Route | Intramammary infusion, intensive dosing (q12h for 5 doses, per phage dosing evidence) |
| Target cure rate | >55% bacteriological cure |
| Target price | $30-60 per treatment course. Endolysin manufacturing is protein production -- COGS must be validated. |
| Withdrawal period | Endolysin is a protein enzyme (no chemical residue). Pirlimycin withdrawal applies. Combined withdrawal TBD. |
| Regulatory pathway | FDA-CVM NADA for combination (endolysin + antibiotic). Complex but precedent being established by human exebacase program. |
| Who buys | Veterinarian prescribes; farmer administers. |

**De-Risk Experiment:**

| Parameter | Detail |
|-----------|--------|
| Design | Lead endolysin activity test across milk from 20 different cows (capturing normal inter-cow variation in fat, protein, pH, SCC) |
| Primary endpoint | MBC consistency: >2-log killing in >80% of milk samples |
| GO gate | >2-log kill in >16/20 milk samples |
| KILL gate | >2-log kill in <10/20 milk samples (inconsistent -- commercially unreliable) |
| Budget | $80,000-120,000 |
| Timeline | 9 months |

**Embarrassment pass:** The endolysin kills beautifully in lab-grade skim milk but fails in 60% of field milk samples because fat content, pH, and protein composition vary wildly between cows. The product works in the lab but not in the field.

**Kill criteria:**
- Inconsistent activity (<80% of milk samples): KILL
- Endolysin degrades to <50% activity within 4 hours in milk at 37 degrees C: KILL (insufficient contact time)

---

#### 4. LukMF' Toxoid Vaccine (Candidate 3B)

**What:** Vaccination with detoxified LukM/LukF' toxoid to generate neutralizing antibodies that protect bovine neutrophils from the most potent leukocidin.

**Why it matters:** LukMF' is bovine-specific (targets CCR1). Neutralization preserves neutrophil function, improving bacterial clearance and reducing collateral tissue damage. In the Dutch market (96% lukM-positive), coverage is near-complete. This is a precision vaccine -- paired with strain diagnostics for market segmentation.

**Target Product Profile:**

| Parameter | Specification |
|-----------|--------------|
| Indication | Prevention of *S. aureus* mastitis severity and treatment resistance in lukM-positive herds |
| Route | Subcutaneous injection, pre-calving vaccination series (2-3 doses) |
| Target population | Dairy cattle in herds with confirmed lukM-positive *S. aureus* strains |
| Target efficacy | >50% reduction in treatment failure rate for lukM-positive infections; reduced severity of clinical episodes |
| Target price | $5-15 per dose (in line with existing bovine vaccines) |
| Withdrawal period | None (biologics) |
| Regulatory pathway | USDA-CVB (biologics). Fits Zoetis vaccine portfolio exactly. |
| Who buys | Veterinarian recommends, farmer purchases. Sold through veterinary distributors. |

**De-Risk Experiment:**

| Parameter | Detail |
|-----------|--------|
| Design | (1) Confirm lukM carriage in target market by screening 100+ bovine *S. aureus* isolates. (2) Generate bovine anti-LukM serum via vaccination with toxoid. (3) Test neutrophil survival in presence of anti-LukM serum + live CC151 in bovine whole milk. |
| GO gate | Anti-LukM serum protects >70% of bovine neutrophils from LukMF'-mediated killing (vs. <30% with pre-immune serum) |
| KILL gate | Anti-LukM serum protects <40% of neutrophils (insufficient neutralization) |
| Budget | $70,000-100,000 |
| Timeline | 12 months |

**Embarrassment pass:** We develop the vaccine, demonstrate neutrophil protection in vitro, test it in a field trial, and it works in CC151-dominant herds but has zero impact in CC97-dominant herds (where lukM carriage is ~30%). The product gets mixed reviews because farmers do not know their herd's strain profile.

**Pairing requirement:** This vaccine MUST be paired with strain diagnostics (Candidate 7C) to identify herds where lukM carriage is high enough to justify vaccination.

---

#### 5. Mucosal IgA Vaccination (Candidate 3C)

**What:** Nasal immunization to generate mammary-associated sIgA that opsonizes *S. aureus* without SpA interference. SpA binds IgG but NOT IgA -- this circumvents the central immune evasion mechanism.

**Target Product Profile:**

| Parameter | Specification |
|-----------|--------------|
| Indication | Prevention of *S. aureus* IMI via mucosal immunity |
| Route | Intranasal or intramammary immunization (dry period) |
| Target efficacy | Detectable *S. aureus*-specific sIgA in milk; >30% reduction in new IMI incidence |
| Target price | $10-25 per vaccination course |
| Regulatory pathway | USDA-CVB (biologics). Novel delivery route but established antigen targets. |

**De-Risk Experiment:**

| Parameter | Detail |
|-----------|--------|
| Design | Intranasal delivery of *S. aureus* multi-antigen formulation (ClfA + FnBP fragments + CP5/CP8 conjugate) + mucosal adjuvant in 20 dry cows. Measure sIgA in milk at calving vs. 20 systemic-vaccination controls. |
| GO gate | sIgA/IgG ratio >2 in milk and detectable *S. aureus*-specific sIgA in >70% of vaccinated cows |
| KILL gate | No detectable *S. aureus*-specific sIgA in milk (<30% of vaccinated cows) |
| Budget | $80,000-120,000 |
| Timeline | 12 months (vaccination during dry period, sampling at calving) |

---

### Tier 2: Discovery Stage (Wounded -- Conditional)

#### 6. SrtA Inhibitor (Candidate 2A)

**Status:** WOUNDED. Discovery-stage target with zero host homolog and multi-barrier mechanism (adhesion + immune evasion + internalization prevention). 22+ years with no drug-quality compound. Recent covalent inhibitor chemistry (2024-2025) shows progress.

**Why it stays in portfolio:** SrtA is the cleanest pharmacological target in the entire portfolio (zero bovine homolog, 7 PDB structures, universal conservation, multi-barrier mechanism). The 22-year development history reflects medicinal chemistry difficulty, not biological invalidity.

**De-risk:** Screen 2024-2025 covalent SrtA inhibitor scaffolds against bovine CC97/CC151/CC479 in surface protein display assay. Budget: $60,000-80,000.

**GO:** IC50 <10 uM against bovine isolates with >50% reduction in surface SpA/ClfA display and no PAINS alerts.
**KILL:** All available scaffolds are PAINS or IC50 >50 uM.

#### 7. NLRP3 Activator (Candidate 4B)

**Status:** WOUNDED (REVIVED). NLRP3 is PROTECTIVE against *S. aureus* (KO mice: 50% mortality). Activation (not inhibition) is the correct therapeutic direction. Compound tested in bovine mastitis model (Thacker et al. 2012).

**De-risk:** Test NLRP3-activating compound in bovine MAC-T infection model. Budget: $50,000-70,000.

#### 8. A2aR Antagonism (Candidate 3D, rescoped)

**Status:** WOUNDED (REVIVED, RESCOPED). Host-target A2aR antagonism is independently druggable. Enhanced *S. aureus*-specific Th17 responses in mice. A2aR antagonists in human immuno-oncology Phase 1/2 trials.

**De-risk:** A2aR antagonist in bovine whole blood *S. aureus* killing assay. Budget: $40,000-60,000.

---

### Companion Diagnostics and Management

#### 9. Herd Management Tool (Candidate 7C)

**What:** Rapid on-farm PCR diagnostics for *S. aureus* strain typing (CC97/CC151/CC479) + SCC-based prognostic scoring to stratify cows into treat/segregate/monitor pathways.

**Why Zoetis should care:** This is NOT a therapeutic -- it is the platform that makes every therapeutic more effective. Strain typing enables precision deployment of the LukMF' vaccine (herds with high lukM carriage) and phage cocktail (strain-matched phage selection). Prognostic scoring identifies cows where treatment is economically justified vs. those where segregation/culling is the rational choice.

**Zoetis fit:** Zoetis has a diagnostics division. Rapid isothermal PCR for CC-typing is technically feasible. This is a companion diagnostic opportunity.

**Budget:** $100,000-150,000 for pilot development and validation in 5 herds.

#### 10. Ca/BHBA Management Protocol (Candidate 0B)

**What:** Targeted peripartum calcium and propylene glycol supplementation to prevent BHBA-mediated neutrophil dysfunction and hypocalcemia-mediated phagocytosis impairment.

**Zoetis fit:** Not a product opportunity for Zoetis. But it is the biological baseline that makes all other interventions work better. Recommended as standard management guidance to accompany any Zoetis mastitis product.

---

## Portfolio Economics

### De-Risk Budget Summary

| Priority | Candidate | Budget | Key Gate |
|----------|-----------|--------|----------|
| 1 | Phage cocktail replication | $150-200K | Cure rate >60% at n=80 |
| 2 | Lactoferrin + pirlimycin RCT | $150-200K | Combination exceeds pirlimycin by >15 points |
| 3 | Endolysin milk variability | $80-120K | >2-log kill in >80% of milk samples |
| 4 | LukMF' toxoid proof-of-concept | $70-100K | Neutrophil protection >70% in bovine whole milk |
| 5 | Mucosal IgA proof-of-concept | $80-120K | sIgA/IgG >2 in milk, *S. aureus*-specific |
| 6 | SrtA inhibitor screen | $60-80K | IC50 <10 uM, no PAINS |
| 7 | NLRP3 activator MAC-T test | $50-70K | >1-log CFU reduction, <20% LDH increase |
| 8 | A2aR antagonist blood assay | $40-60K | >50% improvement in phagocytic killing |
| 9 | Herd management tool pilot | $100-150K | Diagnostic accuracy + economic model validation |
| | **TOTAL** | **$780K-1.1M** | |

**Tier 1 only (candidates 1-5):** $530K-740K
**Full portfolio (all 9):** $780K-1.1M

These are CRO-grade cost estimates, not fantasy budgets. Per Quality Standard 31: screening cascades, recombinant protein expression, enzyme assays, and cell-based assays cost $50-100K minimum per target. Multi-farm RCTs cost $150-200K.

### Commercial Potential

**If phage cocktail passes (>60% cure):**
- First non-antibiotic cure for *S. aureus* mastitis
- EU market advantage under Regulation 2019/6
- Global dairy market for mastitis therapeutics: ~$1.5-2B annually
- A 65% cure rate phage product would be commercially revolutionary -- no existing non-antibiotic approach achieves this

**If lactoferrin + pirlimycin passes (>50% cure):**
- First synergistic combination specifically restoring antibiotic susceptibility in resistant *S. aureus*
- Pirlimycin is already a Zoetis product (Pirsue) -- this is a product line extension, not a new platform
- Lactoferrin COGS at scale: $5-15/dose (achievable with dedicated manufacturing)
- The beta-lactamase suppression mechanism is novel intellectual property

**If LukMF' vaccine passes:**
- First precision bovine *S. aureus* vaccine targeting the species-specific toxin
- Companion diagnostic (CC-typing) creates a platform play
- Fits Zoetis vaccine manufacturing and distribution capabilities
- Potential synergy with Librela/Cytopoint biologics manufacturing expertise

---

## Decision Tree

```
PHAGE COCKTAIL REPLICATION (Priority 1, $150-200K, 12 months)
    |
    |-- PASS (cure >60%) --> Phase 2 development: dose optimization,
    |                         strain panel expansion, regulatory strategy
    |
    |-- FAIL (cure <40%) --> KILL phage approach.
                             Remaining portfolio: lactoferrin + endolysin + vaccines

LACTOFERRIN + PIRLIMYCIN RCT (Priority 2, $150-200K, 12 months, parallel with #1)
    |
    |-- PASS (>15 points over pirlimycin) --> Combination development.
    |                                          Pirsue line extension.
    |                                          Lactoferrin sourcing + scale manufacturing.
    |
    |-- FAIL (no significant difference) --> Lactoferrin synergy insufficient.
                                             KILL lactoferrin combination.
                                             Pirlimycin optimization separate.

ENDOLYSIN MILK VARIABILITY (Priority 3, $80-120K, 9 months, parallel)
    |
    |-- PASS (>80% samples, >2-log kill) --> Combination with pirlimycin
    |                                         in bovine RCT. Budget: additional $150K.
    |
    |-- FAIL (inconsistent activity) --> KILL endolysin intramammary approach.
                                         Milk matrix too variable.

LukMF' TOXOID (Priority 4, $70-100K, 12 months, parallel)
    |
    |-- PASS (neutrophil protection >70%) --> Multi-antigen vaccine development.
    |                                          Combine with SpAKKAA and/or IgA components.
    |                                          Companion diagnostic (CC-typing).
    |
    |-- FAIL (protection <40%) --> KILL LukMF' toxoid approach.
                                   Toxoid does not generate sufficient neutralization.

MUCOSAL IgA (Priority 5, $80-120K, 12 months, parallel)
    |
    |-- PASS (sIgA in milk, S. aureus-specific) --> Multi-antigen mucosal vaccine
    |                                                development. Novel delivery route IP.
    |
    |-- FAIL (no sIgA in milk) --> KILL mucosal IgA approach.
                                   Bovine mammary gland does not generate sIgA
                                   to nasal immunization.
```

**Portfolio resilience:** If any 2 of the 5 primary assets pass their gates, Zoetis has a differentiated mastitis program. If all 5 fail, the disease biology is harder than we modeled and the program should be reconsidered.

---

## Commercial Positioning

Three options depending on Zoetis strategic priority:

### Option A: "Next-Gen Cure" (Cure-Side Focus)
Lead with phage cocktail (if replicates) + lactoferrin/pirlimycin combination. Position as the first non-antibiotic + first synergistic combination for *S. aureus* mastitis. Target: EU market first (Regulation 2019/6 demand), then global.

**Zoetis advantage:** Already owns Pirsue (pirlimycin) -- lactoferrin combination is a line extension. Phage is a new platform but builds on Zoetis biologics manufacturing (Librela, Cytopoint).

### Option B: "Precision Prevention" (Vaccine + Diagnostics)
Lead with LukMF' toxoid + mucosal IgA + companion CC-typing diagnostic. Position as the first precision mastitis prevention platform. Target: herds with identified *S. aureus* strain profiles.

**Zoetis advantage:** Vaccine manufacturing capability is core competency. Companion diagnostics create a platform (test + treat model). Higher margin than therapeutics.

### Option C: "Full Stack" (Prevention + Cure + Management)
Combine Options A and B. Position as the only complete *S. aureus* mastitis management platform. Diagnostic identifies strain, vaccine prevents, therapeutic cures, management tool guides decisions.

**Zoetis advantage:** No competitor offers all three. The diagnostic ties the entire platform together and creates lock-in.

**Recommendation for Daniel:** Let the de-risk data guide the choice. Run all 5 priority de-risk experiments in parallel ($530-740K, 12 months). The results will tell you which option is real.

---

## What We Are NOT Promising

1. **We are not promising 70% pathology coverage.** The honest coverage estimate is ~62% with all conditional candidates included. The SCV dormancy gap is real and unaddressed. This means a fraction of chronically infected cows (those with deep SCV reservoirs) will not be cured by any candidate in this portfolio.

2. **We are not promising the phage result will replicate.** The Kromker data are n=16 with a wide confidence interval (57-94%). The replication trial is the experiment, not the foregone conclusion.

3. **We are not promising lactoferrin COGS are viable.** At current pricing ($50-200/g), lactoferrin may or may not be commercially feasible. Scale manufacturing economics must be validated.

4. **We are not promising regulatory pathways exist.** Phage has no established FDA-CVM pathway. Mucosal vaccination is a novel delivery route. These regulatory questions are real and could add 2-5 years to development timelines.

5. **We are not promising any single candidate solves the disease.** *S. aureus* mastitis is a multi-barrier problem. No single mechanism addresses all five barriers. The value of this portfolio is the combination of complementary mechanisms across disease stages.

6. **We are not presenting the killed candidates as "what could have been."** Gallium was a food safety non-starter. ADEP kills mammalian cells. Menadione damages host tissue at therapeutic concentrations. APT's data are manufacturer-funded without independent replication. Pirfenidone's economics are incompatible with dairy. These candidates were killed for specific, evidence-based reasons that cannot be engineered around.

---

## Unresolved Questions

These are the questions we identified but could not answer within this program. They are flagged for future work:

1. **SCV field prevalence.** How common are SCVs in natural bovine *S. aureus* mastitis? If they are rare, the SCV coverage gap matters less. If they are common (which we suspect), the gap is critical. A field prevalence survey ($30-50K) would directly inform portfolio prioritization.

2. **ZG-series selective ClpP activators.** The ADEP scaffold was killed for mammalian ClpP activation. Non-ADEP ClpP activators (ZG-series) may have selectivity for bacterial over mammalian ClpP. This is a future discovery opportunity, not a current asset.

3. **agr expression in vivo.** Nearly all agr regulatory data are from in-vitro models. There are essentially zero studies measuring agr dynamics during bovine mastitis in vivo. This gap affects all anti-virulence strategies.

4. **Bovine-specific complement evasion.** Bovine-adapted *S. aureus* lacks SCIN/CHIPS (which are human-specific). Whether bovine strains have evolved alternative complement inhibitors is unknown.

5. **Within-host evolution endpoint.** The sigB-deficient, capsule-negative, biofilm-enhanced pathotype may be the inevitable evolutionary destination of chronic mastitis. If so, all therapies must be designed against this phenotype, not the infecting strain.

---

## Conclusion

This portfolio represents the output of the most rigorous analytical process we can run: complete disease mapping, forensic failure analysis, creative candidate design, adversarial kill review, 6-model external validation, and honest coverage assessment.

The result is a portfolio that covers ~62% of *S. aureus* mastitis pathology, short of the 70% threshold due to the SCV dormancy gap. But it contains three candidates (phage cocktail, lactoferrin/pirlimycin, endolysin/pirlimycin) that, if validated, would each independently represent a meaningful advance over current therapy -- and two vaccine candidates (LukMF' toxoid, mucosal IgA) that address immune evasion mechanisms no current product touches.

The total de-risk investment for all 5 primary assets is $530-740K over 12 months. All experiments have binary GO/KILL gates with specific thresholds defined before the work begins. The decision tree is explicit: if candidates pass, here is what happens next. If they fail, here is what dies.

The honest framing: this is hard biology. *S. aureus* has evolved to persist in the bovine mammary gland across millions of years of co-evolution. A portfolio that addresses 62% of this pathology is more complete than any previous effort (Argus v8/v9 achieved ~45%), but it is not complete. The SCV gap must be filled in a future iteration.

---

*This decision memo was prepared using data from all five prior phases, corrected verdicts from six external reviewers, and honest coverage assessment. All claims are traceable to the evidence register. Budget estimates are CRO-grade. Kill criteria are defined before experiments. What we are NOT promising is stated explicitly.*
