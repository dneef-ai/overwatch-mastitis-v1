# Phase 5 — Decision Memo: AB03-B Rumen Hydrogen Accumulation Syndrome (RHAS)

**Program:** AB03-B | **Internal Agteria Program** (no partner) | **Version:** v1
**Agent:** Anvil | **Date:** 2026-03-30

---

## Executive Summary

RHAS is an iatrogenic metabolic syndrome caused by every methanogenesis inhibitor on the market or in development. When the primary hydrogen sink in the rumen (methanogenesis) is pharmacologically suppressed, dissolved H2 accumulates, stalling fermentation and eroding productivity. With Bovaer approved in 70+ countries and Denmark mandating its use, RHAS is transitioning from a research curiosity to a real-world clinical problem affecting potentially millions of cattle.

The Overwatch pipeline identified the NADH reoxidation bottleneck as the rate-limiting gate, mapped 10 failed treatment approaches across 20+ years, proposed 30 candidates from 2 independent analysis streams (Forge + Vulcan), killed 8 on evidence, wounded 13 with specific de-risk experiments, and produced a force-ranked portfolio of 5 priority candidates.

**No candidate in this portfolio has been tested for RHAS.** This is the honest starting state for a novel disease with zero prior treatments. The portfolio is not a set of validated targets — it is a set of testable hypotheses organized by information value and commercial potential.

**The investment ask:** $37-47K over 10-12 weeks to run 3 RUSITEC experiments (plus a $2K batch culture pre-screen) that will validate or kill the top 4 candidates and resolve the central mechanistic question (catalytic vs stoichiometric electron shuttling). This is the cheapest path to a data-backed portfolio decision.

**If it works:** Agteria has identified a novel mechanism (redox-mediated NADH reoxidation restoration) for treating a side effect that will affect every farm using methane inhibitors worldwide. The lead compound (menadione) is FDA-approved, costs $0.01/cow/day, and could be formulated and deployed within 12-18 months of in vivo validation.

**If it fails:** The RUSITEC data will tell us exactly why. The portfolio restructures toward the next-ranked candidates (phloroglucinol, biochar DIET, iron reduction), each with its own binary de-risk experiment. Total information value of the $37-47K investment is high regardless of outcome.

---

## The Problem: Why RHAS Is Hard

### Why This Disease Exists

Every methanogenesis inhibitor (3-NOP/Bovaer, Asparagopsis/bromoform, halogenated compounds) suppresses the dominant hydrogen disposal pathway in the rumen. Methanogenesis normally consumes 70-80% of all metabolic hydrogen. When suppressed, the displaced hydrogen has nowhere productive to go.

### Why Nothing Has Worked

Ten approaches have been tried over 20+ years. All failed:

| Approach | Why It Failed | Lesson |
|----------|--------------|--------|
| Fumarate/malate | Biology works; cost prohibitive ($0.20-0.80/cow/day) | Stoichiometric electron acceptors are economically dead |
| Nitrate | Most effective H2 sink; toxic intermediate (nitrite, methemoglobinemia) | Safety must be absolute at farm scale |
| Acetogens (DFMs) | Thermodynamic ceiling: cannot draw H2 low enough | Biology alone cannot solve a thermodynamic problem |
| Sulfate | Best thermodynamics; toxic product (H2S, PEM) | Even favorable thermodynamics fail if the product is toxic |
| Dietary fat | Limited by fat tolerance (5-6% DM); insufficient sink capacity | Minor sinks cannot compensate for a major pathway |
| Propionate DFMs | In vitro only; colonization failure | The rumen is not a batch culture |
| Defaunation | Impractical, temporary, incomplete | Source reduction is complementary, not primary |
| Dose optimization | Concedes methane reduction efficacy | Avoidance, not treatment |
| Yeast | Indirect; insufficient H2 disposal | Stimulating acetogens doesn't overcome thermodynamic ceiling |

**The common thread:** Every approach that has the right biology lacks the right economics or safety, and every approach with the right economics lacks the right biology. No treatment has ever satisfied all four requirements simultaneously: thermodynamically favorable + safe + cheap + spatially targeted.

### Why RHAS Is Uniquely Tractable

Despite 20 years of failure, RHAS has one property that makes it the most intervention-sensitive syndrome possible: **R0 ~ 1.0**. The disruption is self-sustaining but not amplifying. The FT curve for NADH oxidation is steep in the critical H2 range (10-100 Pa). This means:

- A 20-30% improvement in local H2 disposal is sufficient to restore NADH kinetics
- Small interventions produce disproportionate effects (the FT curve's nonlinearity)
- The bar for "clinically meaningful" is lower than for any infectious disease

RHAS is not a disease where you need 90% pathogen reduction. It is a disease where you need a marginal thermodynamic nudge.

---

## What We Did

### The Process

1. **Pathfinder** mapped RHAS as a 7-stage disease with quantitative thermodynamic analysis, R0 estimation, and identification of KE#1
2. **Tribunal** (4-frame consensus) determined the NADH reoxidation bottleneck with 4/4 agent agreement, adding the spatial heterogeneity insight (mat-localized H2 is 5-10x bulk)
3. **Sapper** analyzed 10 failed treatments, distinguishing compound failures (fumarate: cost, nitrate: toxicity) from target failures (acetogens: thermodynamic ceiling)
4. **Forge** proposed 22 candidates across 8 molecular intervention points, with full decomposition of the NADH cascade
5. **Vulcan** (quarantined, first-principles) independently converged on 3 of Forge's top candidates (redox mediators, DIET, formate trap) and added 8 unique candidates
6. **Surveyor** computationally validated all 30 merged candidates: thermodynamic compatibility, toxicity profiles, rumen stability, dose-response modeling
7. **Reaper** killed 7 candidates on evidence (noxE: O2-dependent in anaerobic rumen; encapsulated nitrate: Mo/W scavenger already failed in sheep; hydrogenosome inhibitor: no selectivity window; Pd catalyst: H2S poisoning; Rnf engineering: host intractable; hepatic cofactors: irrelevant bottleneck; H2-sensor: undiscovered target)
8. **Board** conducted devil's advocate inversion on all strategic candidates, synthesized 12 external model reviews, and produced the definitive force-ranking
9. **External panel** (6 frontier models x 2 rounds = 12 reviews) contributed throughout: identified rumen epithelial dysfunction (5/6), formate as electron carrier (3/6), and the redox mediator re-oxidation gap (9/12)

### Quality Controls

- **6-model external panel at every phase** (Gemini 3.1 Pro, GPT-5.4, Grok 4, Claude Opus, DeepSeek R1, Qwen 2.5)
- **Compound contamination check** on all candidates (Sapper: target vs compound failure; Reaper: repetition test)
- **"Why isn't the field doing this?" test** on all feed-additive proposals
- **Single-lab dependency tagging** on all key evidence
- **Devil's advocate inversion** on all Board-ranked candidates

---

## The Portfolio

### Force-Ranked Candidates (Board Decision)

| Rank | Candidate | Mechanism | Cost/Day | Evidence State | Key Risk |
|------|-----------|-----------|----------|----------------|----------|
| **1** | **Menadione (VK3)** | Menaquinone pool augmentation in propionogenic bacteria; potential catalytic electron shuttle from NADH to fumarate reductase | $0.01 | Single-lab propionate increase (Bai 2022, 8 cows); FDA-approved | Catalytic vs stoichiometric unresolved; milk yield decrease signal; single-lab dependency |
| **2** | **Phloroglucinol** | H2 capture by Coprococcus spp. via NADPH-dependent reductase | $0.03-0.30 | In vivo cattle positive (CSIRO, chloroform); in vivo cattle negative (Aarhus, 3-NOP) | Conflicting data; inhibitor mismatch; microbiome-dependent |
| **3** | **Riboflavin/FMN** | Extracellular NADH electron shuttle (water-soluble flavin) | $0.0002-0.001 | Correct thermodynamics; zero rumen data | Likely absorbed as vitamin, not shuttled; <20% Board probability |
| **4** | **Conductive biochar (DIET)** | Direct interspecies electron transfer bypassing H2 pool | $0.02-0.20 | DIET proven in anaerobic digesters; zero rumen DIET data | 14 years without rumen confirmation; rumen bacteria may lack EET machinery |
| **5** | **Iron(III) oxide** | Thermodynamically superior electron acceptor (delta-G = -228 kJ/mol) | $0.03-0.28 | Zero rumen-specific data | Mass dose (300-550 g/day); spatial mismatch; H2S interaction |

### Symptomatic/Supportive Candidates (Not RHAS Treatments)

| Candidate | Role | Status |
|-----------|------|--------|
| PG Bridge (8.1) | Propionate bridge during 14-21 day inhibitor initiation | Deployable now; FDA-approved |
| Rumen-Protected Propionate (V2.1) | Post-ruminal propionate for host gluconeogenesis | Wounded; mass dose at ongoing use |
| Fumarate + Acrylate (6.2) | Positive control for RUSITEC experiments | Not a development candidate |

### Deferred Candidates (Medium-Term)

| Candidate | Trigger for Reactivation |
|-----------|-------------------------|
| V3.2: Engineered NADH:Acceptor + Quinone | If menadione shuttle mechanism confirmed |
| 6.1: Engineered FRD M. elsdenii | If PEPCK co-engineering solves substrate limitation |
| 7.1/S2.1: Formate Trap | If formate accumulates >2x under RHAS in RUSITEC |

---

## Target Product Profiles

### TPP 1: AB03-B Lead — Redox Mediator for RHAS (Menadione-Based)

| Parameter | Specification |
|-----------|--------------|
| **Indication** | Prevention/treatment of RHAS in cattle receiving methanogenesis inhibitors |
| **Active ingredient** | Menadione sodium bisulphite (MSB) or menadione dimethylpyrimidinol bisulphite (MPB) |
| **Route** | Oral; mixed in TMR or delivered via intraruminal bolus |
| **Dose** | 200-2000 mg/cow/day (pending RUSITEC dose-response) |
| **Price** | Target: <$0.05/cow/day. At commodity menadione ($5-15/kg) and 200-2000 mg/day, COGS = $0.001-0.03/day. Substantial margin available. |
| **Withdrawal** | None expected (menadione is a vitamin; existing FDA approval as feed additive) |
| **Regulatory pathway** | Feed additive (21 CFR Part 573 if US). Menadione compounds already have FDA GRAS or approved status. New indication labeling may require NADA or minor use permit. EU: existing EFSA opinion covers safety; new efficacy claim requires dossier. |
| **Buyer** | Dairy/beef operations using methane inhibitors; Bovaer users; agri-cooperatives under regulatory mandates (Denmark, EU) |
| **Key claims** | "Restores rumen fermentation efficiency under methane inhibition"; "Maintains milk yield and feed efficiency during Bovaer/3-NOP use" |
| **Minimum viable product** | Menadione premix at defined dose, co-administered with 3-NOP in TMR. Labeled for RHAS prevention. |
| **IP position** | Menadione itself is not patentable (commodity chemical). IP resides in: (a) method-of-use patent for RHAS indication, (b) formulation patent (menadione + methane inhibitor co-formulation), (c) intraruminal bolus with menadione payload. |

### TPP 2: AB03-B Empirical Hit — Phloroglucinol for RHAS

| Parameter | Specification |
|-----------|--------------|
| **Indication** | H2 capture adjunct for cattle on methanogenesis inhibitors |
| **Active ingredient** | Phloroglucinol (1,3,5-trihydroxybenzene) |
| **Route** | Oral; dietary supplementation in TMR (continuous, 21+ day loading) |
| **Dose** | 5-20 g/cow/day (pending RUSITEC optimization) |
| **Price** | $5-15/kg synthetic; at 5-20 g/day = $0.03-0.30/day |
| **Withdrawal** | None expected (GRAS food additive) |
| **Regulatory pathway** | Feed additive with RHAS indication claim |
| **Buyer** | Same as TPP 1 |
| **Key claims** | "Reduces hydrogen emissions and restores fermentation under methane inhibition" |
| **IP position** | Phloroglucinol is generic. IP in: (a) method-of-use for RHAS, (b) formulation with methane inhibitor, (c) dosing protocol (continuous, 21-day loading). Weaker IP than menadione due to existing published cattle data. |

### TPP 3: AB03-B Platform — Conductive Biochar for Rumen DIET

| Parameter | Specification |
|-----------|--------------|
| **Indication** | Rumen fermentation enhancement under methane inhibition |
| **Active ingredient** | High-temperature pyrolyzed biochar (>600C, particle size 0.5-2 mm) |
| **Route** | Oral; dietary supplementation in TMR |
| **Dose** | 50-200 g/cow/day (pending validation) |
| **Price** | $0.30-1.00/kg biochar; at 50-200 g/day = $0.02-0.20/day |
| **Withdrawal** | None (inert material) |
| **Regulatory pathway** | Feed ingredient (not a drug). Low regulatory burden. |
| **Buyer** | Same as TPP 1 |
| **IP position** | Strong if DIET mechanism is confirmed (novel mechanism patent for "conductive material for facilitating interspecies electron transfer in the rumen"). If DIET fails, no IP value. Binary. |

---

## De-Risk Experiments

### Pre-KE#1 Gate: Batch Culture Menadione Replication ($2K, 1 Week)

| Parameter | Detail |
|-----------|--------|
| **Design** | Batch culture: rumen fluid from 3-NOP-treated donor cattle + menadione at 200 mg equivalent. 48-hour incubation. 3 replicates + 3-NOP-only control. |
| **GO threshold** | Propionate molar % increases >3 percentage points vs control |
| **KILL threshold** | No propionate shift; OR substrate disappearance decreases >10% (AQ-pattern toxicity) |
| **If GO:** Proceed to full RUSITEC Priority De-Risk Sequence |
| **If KILL:** Reassess menadione priority. Riboflavin and lawsone screened in batch culture as backup. If all quinones/flavins fail in batch, the redox mediator class is dead. Portfolio restructures to phloroglucinol, biochar, and iron oxide. |

### Priority Experiment 1: Menadione RUSITEC ($15-20K, 6-8 Weeks)

| Parameter | Detail |
|-----------|--------|
| **Design** | RUSITEC with 3-NOP at 50% methanogenesis inhibition. Menadione at 0, 20, 200, 2000 mg/day equivalent. 21-day duration. Fumarate positive control. Optional: riboflavin 100 uM arm. |
| **Primary endpoints** | Dissolved H2 (continuous or 4x daily), propionate (absolute and molar %), total VFA, substrate disappearance |
| **Secondary endpoints** | Methane output, menadione/menaquinol by HPLC (oxidized + reduced forms, liquid + pellet), formate concentration |
| **GO threshold (catalytic shuttle confirmed)** | Arm 1 (20 mg, ~0.1% of H2 gap stoichiometry) reduces dissolved H2 by >10% AND propionate increases; menadione persists in oxidized form (turnover evidence) |
| **GO threshold (respiratory chain amplification)** | Arm 2-3 shows dose-dependent propionate increase with >80% menadione in microbial pellet (intracellular action) |
| **KILL threshold** | All arms: H2 unchanged; OR substrate disappearance decreases (AQ-pattern disruption) |
| **If GO:** In vivo dairy cow trial with 3-NOP + menadione. Primary endpoint: milk yield, DMI, blood metabolites (BHB, glucose, NEFA) |
| **If KILL:** Menadione is not an RHAS treatment. If propionate increases without H2 decrease, reclassify as symptomatic propionate booster. If substrate disappearance decreases, the redox mediator class is toxic. |

### Priority Experiment 2: Phloroglucinol Adaptation ($10-15K, 4-6 Weeks)

| Parameter | Detail |
|-----------|--------|
| **Design** | RUSITEC with 3-NOP. Continuous phloroglucinol 6 mM for 21 days. Time-course sampling at days 0, 3, 7, 10, 14, 17, 21. |
| **Primary endpoints** | Dissolved H2, VFA profile, Coprococcus/phlB gene abundance (qPCR) |
| **GO threshold** | H2 reduction emerges after day 7-14, correlating with phlB enrichment |
| **KILL threshold** | No H2 reduction at day 21 regardless of Coprococcus status |
| **If GO:** In vivo dairy cow trial: 3-NOP + continuous dietary phloroglucinol for 28+ days |
| **If KILL:** Phloroglucinol does not work under 3-NOP. The chloroform-specific hypothesis is confirmed. Kill permanently. |

### Priority Experiment 3: Biochar DIET Binary Test ($8-10K, 3-4 Weeks)

| Parameter | Detail |
|-----------|--------|
| **Design** | RUSITEC with 3-NOP. High-temp biochar (>600C, conductive) vs low-temp biochar (<400C, non-conductive) at same mass (1-2% DM). SiO2 nanoparticles as surface-area control. 14 days. |
| **Primary endpoints** | Dissolved H2, propionate, total VFA, methane (to detect 3-NOP adsorption by biochar) |
| **GO threshold** | Conductive biochar reduces H2 and/or increases propionate significantly more than non-conductive biochar |
| **KILL threshold** | No difference between conductive and non-conductive biochar |
| **If GO:** First demonstration of rumen DIET. Publishable. Optimize particle properties and test in vivo. |
| **If KILL:** DIET does not operate in the rumen. Kill 2.1, 2.2, S4.1 permanently. |

### Budget Summary

| Experiment | Cost | Timeline | Parallel? |
|-----------|------|----------|-----------|
| Pre-KE#1: Batch culture menadione | $2K | 1 week | First gate |
| Priority 1: Menadione RUSITEC | $15-20K | 6-8 weeks | Yes (with 2) |
| Priority 2: Phloroglucinol RUSITEC | $10-15K | 4-6 weeks | Yes (with 1) |
| Priority 3: Biochar DIET RUSITEC | $8-10K | 3-4 weeks | Yes (with 1+2) |
| Bonus: Iron oxide batch culture | $3K | 1 week | Independent |
| **TOTAL** | **$38-50K** | **10-12 weeks** | |

---

## Decision Tree

```
Start: Run batch culture menadione pre-screen ($2K, 1 week)
  |
  |-- Propionate shifts >3 pts? --YES--> Run RUSITEC Priority Sequence ($35-45K, 8-10 weeks)
  |                                         |
  |                                         |-- Menadione: H2 decreases at low dose?
  |                                         |     YES --> Catalytic shuttle CONFIRMED
  |                                         |             GO to in vivo (3-NOP + menadione)
  |                                         |             Timeline to product: 12-18 months
  |                                         |
  |                                         |     NO, but propionate increases --> Respiratory chain amplifier
  |                                         |             May still be useful. Test in vivo for milk yield.
  |                                         |
  |                                         |     NO, and substrate disappearance drops --> AQ-pattern. KILL class.
  |                                         |
  |                                         |-- Phloroglucinol: H2 drops after day 14?
  |                                         |     YES --> Adaptation confirmed. GO to in vivo.
  |                                         |     NO at day 21 --> KILL permanently
  |                                         |
  |                                         |-- Biochar: conductive > non-conductive?
  |                                               YES --> DIET confirmed. Paradigm shift. GO to in vivo.
  |                                               NO --> DIET absent. KILL 2.1, 2.2, S4.1.
  |
  |-- Propionate does NOT shift? --NO--> Screen riboflavin + lawsone in batch ($2K, 1 week)
                                           |
                                           |-- Any quinone/flavin shifts propionate?
                                           |     YES --> Substitute for menadione in RUSITEC
                                           |     NO --> Redox mediator class is dead
                                           |           Run RUSITEC with phloroglucinol + biochar only
                                           |           Consider iron oxide, engineered biology as fallbacks
```

---

## Commercial Positioning

### Option A: "The Methane Inhibitor Companion Product"

AB03-B is sold alongside Bovaer/3-NOP as a complementary feed additive. Positioning: "Unlock the full benefit of methane reduction by preventing the productivity side effects." Target buyer is Bovaer distributors (DSM-Firmenich) and dairy cooperatives under regulatory mandates.

**Advantage:** Largest market (every Bovaer user is an AB03-B customer). Clear value proposition.
**Risk:** Depends on Bovaer's commercial success. If Bovaer fails commercially, AB03-B market disappears.

### Option B: "The RHAS Treatment for Regulatory Compliance"

AB03-B is positioned specifically for markets with methane mandates (Denmark, future EU-wide regulation). Positioning: "Comply with methane regulations without sacrificing productivity." Target buyer is farmers forced to use methane inhibitors.

**Advantage:** Regulatory mandate creates inelastic demand. Farmers will pay for anything that restores lost productivity.
**Risk:** Narrow market (mandate-only regions). Mandates may be relaxed if RHAS concerns grow.

### Option C: "The Rumen Fermentation Optimizer"

AB03-B is positioned broadly as a rumen efficiency product, with RHAS prevention as the lead indication but with claims extending to general rumen health. If menadione's respiratory chain amplification mechanism is confirmed, it may improve propionate production even without RHAS.

**Advantage:** Broader market. Not dependent on methane inhibitor adoption.
**Risk:** Weaker initial value proposition. Harder to differentiate from existing rumen modifiers.

**Recommendation:** Start with Option A. The AB03-B value story is strongest when tied to methane inhibition — the problem is clear, the mechanism is understood, and the regulatory tailwind is building. As data matures, expand to Option C if the mechanism supports broader claims.

---

## What We Are NOT Promising

1. **We are not promising a validated RHAS treatment.** No candidate has RHAS-specific data. We are promising a rigorous hypothesis-testing program that will produce a validated lead or a definitive negative within 12 weeks.

2. **We are not promising menadione works.** The single-lab data is promising but unreplicated, and the catalytic shuttle mechanism is untested. We are promising a $2K experiment that will determine whether to invest $15-20K, and a $15-20K experiment that will determine whether to invest in in vivo trials.

3. **We are not promising the 70% coverage test passes today.** It does not. Coverage is 17% expected / 45% best-case against tractable pathology. We are promising that the Priority De-Risk Sequence will resolve the coverage question within 10-12 weeks.

4. **We are not promising IP.** Menadione and phloroglucinol are commodity chemicals. IP resides in method-of-use, formulation, and co-administration claims. These are defensible but not fortress-grade. If biochar DIET validates, the mechanism patent is stronger.

5. **We are not claiming to have solved RHAS.** No one has. The field is 20+ years into this problem with zero commercial solutions. We are claiming to have identified novel intervention points (NADH reoxidation, DIET, redox mediation) that the field has not previously considered, and to have designed the cheapest possible experiments to test them.

---

## Prediction Log Summary

The program carries 15 falsifiable predictions from Pathfinder (5), Tribunal (5), Sapper (5), Forge (5), Reaper (5), Board (5), and Anvil (5). The most portfolio-critical predictions:

| Prediction | Source | Test | If TRUE | If FALSE |
|-----------|--------|------|---------|----------|
| Hydrogen recovery gap is thermodynamic | Pathfinder P1 | KE#1 RUSITEC | Chemical approaches correct | Pivot to biological |
| NADH FT threshold drives VFA decline | Tribunal T1 | KE#1 RUSITEC | Quantitative H2 target confirmed | Multiple rate-limiting steps |
| Menadione is intracellular respiratory chain amplifier | Board B-1 | RUSITEC HPLC | Lipophilic quinones are the class; riboflavin fails | Extracellular shuttle; broader compound space |
| Phloroglucinol requires >14 days adaptation | Board B-3 | RUSITEC time-course | Product needs loading phase | Phloroglucinol fails under 3-NOP; kill |
| DIET is absent from the rumen | Board B-4 | RUSITEC conductivity control | Kill DIET class | First rumen DIET demo; paradigm shift |
| 30% H2 disposal improvement collapses RHAS | Pathfinder P5 | In vivo after RUSITEC | Low bar for product; partial solutions viable | High bar; fewer candidates qualify |

The prediction log is the program's scientific backbone. Each RUSITEC experiment tests 3-5 predictions simultaneously. The total information value of the $38-50K investment is extraordinary relative to cost.
