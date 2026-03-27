# Phase 4b: Board Decision -- Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess | **Partner:** Elanco | **Date:** 2026-03-27
**Agent:** Board | **Status:** Complete

---

## Executive Summary

The Board reviewed Reaper's kill report (8 killed, 12 wounded, 7 survived) and the 6-model external panel's challenges. After independent analysis, the Board makes four verdict changes (two resurrections, two downgrades), delivers a strict force-ranking of all surviving and resurrected targets, and recommends a three-experiment de-risk sequence with KE#1 running first.

The portfolio's central tension is clear: **the only candidate with real cattle data (MON+BX) is 10 points worse than tylosin, and the only candidate that addresses the validated mechanism (rPL4 vaccine) faces a 30-year history of grain-diet failure.** The combination hypothesis (Triple Stack #26) is the strategic bet -- but it is untested, expensive, and depends on two individually uncertain components reinforcing each other. The Board accepts this bet with conditions.

The hardest call: **MON+BX (#1) survives as the portfolio backbone despite legitimate single-study risk and a persistent efficacy gap.** Three of six external models argued for killing it. The Board disagrees -- not because the criticisms are wrong, but because killing the only candidate with commercial-scale cattle data in a prevention-focused portfolio is strategically reckless. The correct response is replication, not abandonment.

---

## Step 1: External Panel Synthesis

### 1.1 Verdict Changes from External Feedback

#### RESURRECTION: Candidate 5 (Anti-FomA mAb) -- KILLED to WOUNDED (severe, reframed)

**Panel support:** 3/6 models (Gemini, Grok, DeepSeek) argued the kill was wrong.

**The Board agrees, partially.** Reaper killed this candidate on economics ($120/head, 8 injections). The external panel makes two arguments that survive scrutiny:

1. **Proof-of-concept tool, not commercial product.** DeepSeek is right: an anti-FomA mAb is the fastest way to validate whether blocking FomA adhesion *in vivo* in cattle actually prevents liver abscesses. This is the single most important mechanistic question for the entire vaccine strategy (Candidates 4, 12, 26). If anti-FomA mAb prevents LA in a challenge model, FomA goes into every vaccine formulation. If it fails, the vaccine strategy is fundamentally wrong and we save $200K+ on adjuvant studies.

2. **Half-life engineering changes the math.** Gemini and Grok are right that assuming native 20-day IgG half-life is naive. Fc engineering (PASylation, FcRn-binding variants) routinely extends mAb half-life to 60-90 days in other species. A single injection at arrival providing 60-90 days of protection covers the highest-risk grain-transition period.

**What the Board does NOT accept:** Gemini's "high-risk animal targeting" use case is speculative -- there is no validated biomarker for LA risk at feedlot arrival. And the companion animal mAb cost trajectory is irrelevant without food-animal regulatory precedent.

**New verdict: WOUNDED (severe, reframed).** Not as a commercial product. As a mechanistic validation tool for the FomA target. Elanco's mAb platform can generate this antibody. A single challenge study ($80-120K) would resolve whether FomA blocking prevents LA. This experiment should run BEFORE committing $200K to the vaccine field trial (#26).

#### RESURRECTION: Candidate 23 (Anti-Biofilm Dispersal) -- KILLED to WOUNDED (reframed)

**Panel support:** 2/6 models (GPT-5.4, Claude Opus) argued the kill was wrong.

**The Board agrees on reframing.** Reaper killed this candidate for three reasons: biofilm unproven in vivo, delivery to abscess interior impossible, dispersal equals bacteremia. All three criticisms target the wrong use case. Claude Opus identifies the correct reframing: the relevant biofilm target is **Stage 3 (rumen wall colonization)**, not Stage 11 (abscess interior). If F. necrophorum forms biofilm on damaged rumen epithelium (Lockhart 2022 demonstrates the organism CAN form biofilms), then anti-biofilm agents delivered via feed additive to the rumen wall could disrupt colonization upstream of translocation. Delivery IS feasible in the rumen (unlike abscess interiors).

**New verdict: WOUNDED (reframed to Stage 3).** The $10K biofilm matrix characterization experiment should proceed, but with the explicit goal of understanding rumen wall biofilm, not abscess interior biofilm. This is low-priority but not dead.

#### NO RESURRECTION: Candidates 14 (Gallium), 24 (Metronidazole Analog)

**Panel support for gallium resurrection:** 4/6 models (GPT-5.4, Grok, DeepSeek, Qwen) argued the kill was wrong.

Despite 4/6 model support, the Board upholds the kill. The models argue that gallium's iron-mimicry mechanism works independently of ROS and that regulatory precedent exists for metals in feed (zinc, copper). Both points have merit technically, but miss the commercial reality: (a) the food-animal regulatory path for a novel heavy metal compound with no veterinary precedent is 7-10 years minimum, (b) Elanco needs a solution within 2-3 years for the EU September 2026 deadline, and (c) even if the $5K MIC test is positive, the next 15 steps are each individually uncertain. The Board's job is portfolio prioritization, not scientific completeness. Gallium stays dead as a program candidate. The $5K MIC test can run as unfunded academic curiosity.

**Panel support for metronidazole analog resurrection:** 1/6 models (Claude Opus) argued the kill was wrong.

Claude Opus makes a fair regulatory distinction -- a novel scaffold inspired by nitroimidazole chemistry is not automatically subject to a class-wide ban. This is technically correct but commercially irrelevant within Elanco's planning horizon. The regulatory path is 10-15 years. Upheld as KILLED.

### 1.2 Challenges to Survivals

#### MON+BX (#1): The Portfolio's Most Contested Candidate

**Models arguing for kill:** 4/6 (GPT-5.4, Grok, Qwen, DeepSeek argued single-study dependency and/or commercial non-viability as a tylosin "replacement")

**The Board's ruling: SURVIVES, with mandatory replication.**

The criticism is legitimate. Four models and Reaper itself flag the single-study dependency and the 10-point efficacy gap. The Board takes this seriously. But the alternative -- killing the only candidate with commercial-scale feedlot cattle data -- leaves the portfolio with nothing but mouse models, in vitro assays, and theoretical combinations. That is worse.

**The Board's logic:**

1. MON+BX is not being positioned as a standalone tylosin replacement. It is the burden-reduction component of a multi-dimensional strategy. Its job is not to match tylosin alone -- it is to reduce translocation volume enough that the vaccine component (#12) can work where Fusogard failed.

2. The 10-point gap (28.5% vs 18.3%) at current BX dose does not preclude closing at higher doses or with mucoadhesive formulation targeting the rumen wall. Dose optimization has not been attempted.

3. BX alone failing (36.8% vs 43.1% control) is consistent with the Sapper lesson: no single-mechanism intervention works. This is expected, not damning. The combination with monensin (which provides intake stabilization, not direct LA prevention) is where the mechanism operates.

4. The single-study risk is real and addressable. The Board mandates: **no investment in the Triple Stack field trial (#26) until MON+BX efficacy is independently replicated in a second feedlot with a different BX formulation.** Cost of replication trial: ~$80K (n=500, 2-arm: MON+BX vs MON+TYL). This is a prerequisite, not a nice-to-have.

**Condition: MON+BX survives ONLY if an independent replication trial is funded as the first investment.** If replication fails, the portfolio backbone collapses and the program must be restructured around vaccine-only or novel antimicrobial strategies.

#### rPL4 Vaccine (#12): The 30-Year Problem

**Models arguing for kill:** 3/6 (Gemini, GPT-5.4, Grok) argued this repeats Fusogard's failure mode.

**The Board's ruling: SURVIVES, downgraded from Reaper's clean survival to SURVIVED (conditional).**

The criticisms are strong. Gemini is right that "modern adjuvants are better" is hand-waving without specific data showing 150-day titer maintenance under continuous challenge. GPT-5.4 is right that 30 years of failure at the same target endpoint is not "a high burden of proof" -- it is a pattern. Claude Opus identifies the most dangerous missing kill test: **immune exhaustion from continuous antigen exposure**, which the proposed adjuvant comparison study would not detect.

However, Reaper's survival logic also holds: the target IS validated (Fusogard works on forage, Saginala shows 80% protection in challenge), the failure mode IS identified (dose overwhelm, not wrong target), and modern adjuvant technology IS meaningfully better than 1990s formulations.

**The Board adds two prerequisites before the adjuvant study proceeds:**

1. **PL4 sequence survey** across >=50 bovine field isolates from at least 3 feedlots. If PL4 epitopes vary significantly, no adjuvant saves this vaccine. Cost: ~$15-20K. Timeline: 6-8 weeks. DeepSeek and Claude Opus both identify this as critical.

2. **Rumen fluid IgG access study.** Claude Opus identifies the most important unknown in the vaccine strategy: does serum IgG reach the rumen wall at functional concentrations? Vaccinate 10 cattle, measure anti-PL4 IgG in rumen fluid vs serum at 2, 4, 8 weeks. If rumen fluid IgG is <1% of serum, the entire systemic vaccine strategy is dead regardless of adjuvant. Cost: ~$20-30K. This experiment should precede or run concurrently with the adjuvant study.

**Condition: #12 survives ONLY if PL4 sequence conservation is confirmed AND rumen fluid IgG is detectable.** Without both, this is Fusogard 3.0.

#### Triple Stack (#26): The Untested Combination Bet

**Models arguing for kill:** 3/6 (GPT-5.4, Grok, Qwen) argued stacking two uncertain components assumes synergy without evidence.

**The Board's ruling: SURVIVES, but deprioritized below its component validation experiments.**

GPT-5.4 is correct that "combining two suboptimal mechanisms often yields additive disappointment, not breakthrough efficacy." Grok's point about cost ($220K-$320K incremental per 10,000 head) is commercially severe. But Qwen and GPT-5.4 also correctly identify that no alternative combination exists in the portfolio.

The Board's condition: the Triple Stack field trial ($150-200K) does NOT run until BOTH components are individually validated:
- MON+BX must replicate in an independent trial
- rPL4 vaccine must pass the PL4 sequence survey AND the adjuvant titer duration study must show protective titers at day 120+
- The rumen fluid IgG study must show detectable anti-PL4 at the mucosal surface

Only after all three prerequisites are met does the $150-200K combination trial proceed. The Board will not spend $200K testing a combination of two unvalidated components.

#### FP-100 (#27): Cheap Experiment, Dead Product

**Models arguing for kill:** 3/6 (GPT-5.4, DeepSeek, Claude Opus) argued cheapness of the MIC test is not a survival criterion.

**The Board's ruling: DOWNGRADED from SURVIVED to KILLED as a program candidate. MIC test authorized as a $5K information-gathering experiment only.**

Claude Opus and DeepSeek are right. Three independent extrapolations (different species, different organ, different host), plus an asset owned by a human pharma startup with zero food-animal interest, plus the fact that FP-100 IS an antibiotic (narrow-spectrum ribosomal inhibitor) facing the same regulatory headwinds as tylosin -- this is not a viable drug development candidate. The Board agrees with GPT-5.4: "Worth screening is not the same as survives."

The $5K MIC test should run because information is cheap. But it exits the portfolio as a ranked candidate. If the MIC result is surprisingly potent, it re-enters as a future-generation lead compound, not a near-term Elanco product.

#### Hindgut Prebiotic (#9): Valid but Contingent

**Models arguing for kill:** 1/6 (GPT-5.4) argued cheapness of experiment is not survival.

**The Board's ruling: SURVIVES.** GPT-5.4's criticism (cheap experiment does not justify survival) applies to FP-100 but not here. The hindgut-origin subtype is a genuine biological discovery (Pinnell 2022-2023), and the question of whether tylosin preferentially prevents rumen-origin vs hindgut-origin abscesses is the single most portfolio-restructuring question in the program (KE#1). The candidate is not contingent on a cheap experiment -- it is contingent on a fundamental biological question that changes the entire portfolio strategy.

The Pinnell single-lab dependency is real and concerning. The Board notes this as a risk but does not kill for it because the KE#1 experiment itself provides independent validation or refutation of the 24% estimate.

### 1.3 Single-Lab Dependencies -- Board Assessment

| Candidate | Lab Dependency | Board Action |
|-----------|---------------|-------------|
| #1 (MON+BX) | Felizari 2025 -- single trial, single feedlot, single BX formulation | **CRITICAL.** Independent replication mandated as prerequisite for any further investment. |
| #9 (Hindgut) | Pinnell 2022-2023 -- single lab's 16S estimate of 24% hindgut fraction | **SIGNIFICANT.** KE#1 provides independent check. If KE#1 data contradicts Pinnell estimate, hindgut candidates are immediately killed. |
| #4/#12 (Vaccines) | Amachawadi/KSU lab -- all multi-antigen data, FomA blocking, genomics | **MODERATE.** Kumar 2015 (FomA) and Saginala 1997 (PL4) are from different eras and partially different groups. Not a single-investigator dependency. But ALL bovine grain-diet field trial data is absent from ANY lab. |
| #27 (FP-100) | Flightpath Biosciences -- single company, human pharma focus | **FATAL for commercialization.** Contributes to FP-100 downgrade from SURVIVED to information-only. |

### 1.4 Missing Kill Tests Accepted from External Panel

The Board accepts three missing kill tests identified by the external panel and incorporates them into the de-risk sequence:

1. **Rumen wall IgG access** (Claude Opus): The most important unknown in the vaccine strategy. Must be tested before adjuvant optimization. Incorporated into prerequisites for #12.

2. **PL4 antigenic variation** (DeepSeek, Claude Opus): If PL4 epitopes vary across bovine field strains, no adjuvant fixes this. Incorporated as prerequisite for #12.

3. **Tannin protein-binding saturation** (Claude Opus): Does dietary protein neutralize BX's anti-Fn activity? A simple in vitro experiment (BX activity in the presence of feedlot-concentration protein) would resolve whether dose optimization can close the gap or if BX faces a mechanistic ceiling. Incorporated into MON+BX replication trial design.

---

## Step 2: Devil's Advocate Inversion

For each surviving target, the Board argues the opposite case.

### #1 -- MON+BX (Burden Reduction Backbone)

**Availability bias check:** YES, this is in the portfolio primarily because it exists and has data, not because independent biological reasoning points to "monensin + tannins" as the optimal burden reduction strategy. The biology points to selective anti-Fn activity at the rumen wall (Sapper Lesson 2). MON+BX provides partial anti-Fn activity in broth (MIC 6.25-12.5 ug/mL) but likely achieves near-zero concentration at the wall after protein binding consumes 70-90% of the tannin. The real active ingredient may be monensin's intake stabilization, not tannin's antimicrobial effect -- in which case BX adds cost without adding mechanism.

**Alternative explanation:** Monensin alone + better dietary management (3-inch chop length roughage, which reduced LA from 12.5% to 0%) could provide equivalent burden reduction without BX. The chop-length finding is the most underexploited result in the field.

**"Elanco already knows this" test:** Elanco manufactures Rumensin (monensin). They have certainly evaluated monensin combinations internally. If MON+BX were obviously promising, Elanco would already have an agreement with the BX manufacturer. The absence of such a deal after the Felizari 2025 publication is notable.

**Board conclusion:** Availability bias is HIGH. But the bias is acknowledged, not disqualifying. MON+BX survives because killing it leaves nothing with cattle data, and the alternative (dietary management) is economically impossible. The replication trial will determine if the bias misled us.

### #9 -- Hindgut Prebiotic (The Unaddressed 24%)

**Availability bias check:** LOW. This is in the portfolio because biology independently points here. The Pinnell 2022-2023 discovery of two abscess subtypes is a genuine advance. No existing product targets this pathway.

**Alternative explanation:** The 24% Bacteroidetes-dominated subtype may not require hindgut-specific intervention. If these bacteria translocate via the same damaged rumen wall vasculature (just originating from a different GI source), then rumen barrier integrity (#2) and hepatic immune support (#12) would address them without hindgut-specific products.

**"Elanco already knows this" test:** Unlikely. The Pinnell data is very recent (2022-2023), and Elanco's internal pipeline has historically focused on rumen-targeted approaches. However, Elanco's Benchmark database (68,000+ feedlots) would let them validate the 24% estimate retrospectively through abscess typing if they chose to.

**Board conclusion:** Low availability bias. The alternative explanation (barrier integrity addresses hindgut abscesses too) is plausible and would be tested by the KE#1 experiment.

### #12 -- rPL4 Vaccine with Slow-Release Adjuvant

**Availability bias check:** HIGH. This is in the portfolio because leukotoxin vaccination has a 30-year academic literature, a US patent exists, Elanco has vaccine infrastructure, and Kansas State has spent decades on this target. The portfolio gravitates toward this candidate because the scientific ecosystem supports it, not because independent analysis points to "yet another leukotoxin vaccine" as the highest-probability approach.

**Alternative explanation:** The dose-overwhelm problem may be fundamentally unsolvable by any adjuvant. The correct approach to leukotoxin neutralization may not be vaccination at all but rather (a) reducing translocation volume so much that even modest titers suffice (MON+BX's role), or (b) a single-dose long-acting mAb at arrival covering the grain-transition risk window, or (c) receptor blocking (Candidate #13) which bypasses the titer problem entirely.

**"Elanco already knows this" test:** DEFINITELY. Elanco owns Fusogard. They have internal data on its failure on grain diets. They have almost certainly evaluated next-generation adjuvants internally. If a slow-release adjuvant formulation were obviously promising, they would have tested it. The fact that Fusogard has not been reformulated with modern adjuvants despite being on the market suggests Elanco's internal assessment may be pessimistic.

**Board conclusion:** Availability bias is HIGH and the "Elanco already knows this" signal is concerning. The Board does NOT kill the candidate on this basis -- Elanco's internal assessment may have been done with 2010s adjuvants, and the field has advanced. But this reinforces the need for the two prerequisites (PL4 sequence survey, rumen IgG access) before committing to the expensive adjuvant study.

### #26 -- Triple Stack (MON+BX + rPL4 Vaccine)

**Availability bias check:** MODERATE. The combination is proposed because the individual components exist, not because a biological model predicts synergy. However, the Sapper lesson (multi-dimensional attack required) independently justifies combining burden reduction with immune support.

**Alternative explanation:** The combination may be subadditive rather than synergistic. If monensin suppresses immune responses (documented in vitro at higher doses -- Claude Opus's missing kill test), the ionophore could ANTAGONIZE the vaccine. The combination could perform worse than the vaccine alone on a non-monensin background.

**"Elanco already knows this" test:** Elanco owns both Rumensin and Fusogard. They have certainly considered combining them. The absence of a published Rumensin + Fusogard combination trial is notable. This could mean they tested it and it failed, or that they never tested it because Fusogard's standalone failure on grain diets made the combination moot. Either way, this is a warning signal.

**Board conclusion:** The monensin-vaccine interaction risk (Claude Opus) is a genuine concern that the 4-arm trial design would detect. The Board adds an explicit requirement: the Triple Stack trial MUST include a vaccine-only arm (no monensin) to detect antagonism.

### #5 (Resurrected) -- Anti-FomA mAb (Mechanistic Validation Tool)

**Availability bias check:** MODERATE. This is in the portfolio partly because Elanco has a mAb platform, creating a solution-in-search-of-a-problem dynamic. However, FomA is independently validated as the strongest adhesion target (Kumar 2015, Amachawadi 2023).

**Alternative explanation:** The FomA target can be validated more cheaply via vaccination than via mAb. A bovine serology study ($40-60K) measuring anti-FomA antibodies' ability to block adhesion in vitro provides target validation without the cost of mAb development.

**"Elanco already knows this" test:** Elanco's mAb platform is companion-animal focused. They have not publicly pursued food-animal mAbs. The $130M Elwood expansion is for canine products. Internal advocates for livestock mAbs may exist but have not won budget allocation. This suggests Elanco's commercial assessment of food-animal mAbs is currently negative.

**Board conclusion:** The alternative (vaccination-based target validation) is cheaper but slower and less definitive. A mAb challenge study provides clean, dose-controlled proof. The Board ranks this as a potential de-risk experiment, not a product candidate.

---

## Step 3: Force-Ranking

All surviving and resurrected targets, force-ranked with NO TIES. Ranking criteria: leverage (rate-limiting barrier), information value, concentration risk, replication status, clinical endpoint completeness, and partner fit.

| Rank | Candidate | Verdict | Why This Rank |
|------|-----------|---------|---------------|
| **1** | **#1 -- MON+BX** | SURVIVED (conditional on replication) | Only candidate with commercial-scale cattle LA data. Addresses the rate-limiting barrier (Stages 1+3). Highest partner fit (feed additive, Elanco's Rumensin). Highest clinical endpoint completeness (LA prevalence at slaughter). Single-study risk is the critical vulnerability -- but it is addressable. If this falls, nothing replaces it in the near term. |
| **2** | **#12 -- rPL4 Vaccine** | SURVIVED (conditional on PL4 survey + IgG access) | Addresses the most validated virulence mechanism (leukotoxin, Stage 6). Highest information value: the adjuvant titer study answers whether ANY vaccine can work on grain diets. Elanco has vaccine infrastructure. But 30-year failure history, zero grain-diet cattle data, and two unresolved prerequisites (PL4 conservation, rumen IgG access) prevent rank #1. |
| **3** | **#9 -- Hindgut Prebiotic** | SURVIVED (contingent on KE#1) | Addresses the only completely unaddressed disease pathway (Stage 5, hindgut-origin 24%). Highest concentration risk: if hindgut abscesses ARE the residual fraction under tylosin, this is the most important candidate in the portfolio. But the entire rationale depends on one lab's 16S estimate. KE#1 determines whether this is rank #1 or irrelevant. |
| **4** | **#26 -- Triple Stack** | SURVIVED (deprioritized below component validation) | The only combination strategy and the portfolio's ultimate bet. But it inherits ALL risks from #1 and #12, plus untested synergy, plus 8-12x tylosin cost. Cannot be tested until both components individually validate. Ranked #4 because it is derivative, not independent. |
| **5** | **#4 -- Multi-Antigen Vaccine (reformulated)** | WOUNDED (severe) | Best long-term vaccine concept (multi-antigen, multi-stage targeting). But formulation must be corrected (replace hemagglutinin with validated OMP adhesin per Surveyor), zero cattle data, mouse model is misleading due to leukotoxin insensitivity. Ranked below #12 because #12 is simpler and tests the core question (can any leukotoxin vaccine work on grain diets?) that #4 also depends on. |
| **6** | **#5 -- Anti-FomA mAb (reframed as validation tool)** | WOUNDED (severe, resurrected) | Highest information value per dollar IF framed as a mechanistic validation experiment: does blocking FomA prevent LA in cattle? Answers the question that the entire vaccine adhesion-blocking strategy depends on. But not a commercial product. Ranked #6 because it is a tool, not a portfolio asset. |
| **7** | **#2 -- Rumen-Protected Butyrate** | WOUNDED | Addresses the wide-open Stage 2 gap (barrier integrity). The Ussing chamber experiment ($15-20K) is cheap and resolves the VFA paradox. But zero feedlot cattle data and a genuine biological concern (adding VFA to VFA-damaged epithelium). Ranked here because barrier integrity is critical but this candidate's biology is uncertain. |
| **8** | **#8 -- Mucosal IgA Vaccine (intranasal route only)** | WOUNDED | Addresses the systemic-vs-mucosal immunity gap that undermines all parenteral vaccines. Intranasal delivery bypasses the rumen degradation problem. But ruminant mucosal immunology is poorly characterized, and no evidence exists that intranasal priming generates rumen wall IgA. Long-shot but addresses a real gap. |
| **9** | **#16 -- Anti-Pyolysin** | WOUNDED | Valid add-on to vaccine candidates (incremental $15-20K). But 29% ceiling (T. pyogenes prevalence) makes this a minor contributor. Ranked low because it cannot stand alone and adds marginal value to already-uncertain vaccine candidates. |
| **10** | **#6 -- Epimural-Targeted Probiotic** | WOUNDED | Addresses the right niche (rumen wall, not lumen) -- the key Sapper lesson. But 5+ year basic research timeline. The 16S comparison of LA-resistant vs LA-susceptible epimural communities ($30K) is the right first experiment. Long-horizon, low near-term value. |
| **11** | **#13 -- Leukotoxin Receptor ID** | WOUNDED | If the receptor is identified, it restructures the entire anti-leukotoxin strategy. Paradigm-shifting potential. But decades of failed attempts, 5-10 year path to product, and basic research nature. The crosslinking/mass spec experiment ($30-50K) is high-risk/high-reward. Not a near-term portfolio asset. |
| **12** | **#3 -- Zinc + Butyrate Combo** | WOUNDED | Combines two individually failed approaches with a coherent mechanistic rationale (zinc for structural assembly + butyrate for transcriptional activation). But zinc alone has failed for LA, and the "two wrongs make a right" logic requires proof. Low incremental cost ($20K) to add to an existing trial, but low independent confidence. |
| **13** | **#10 -- Hindgut Butyrate + Zinc** | WOUNDED | Same concerns as #2 and #3 but for the hindgut, with even less evidence. Entirely dependent on KE#1 confirming hindgut significance. If KE#1 is negative, this is irrelevant. If positive, still faces the VFA paradox and delivery uncertainty. |
| **14** | **#18 -- Immunomodulatory Macrolide Analog** | WOUNDED | The in vitro experiment ($20-30K) resolving whether tylosin's immunomodulatory effect matters for LA is genuinely worth doing -- it answers a 50-year question. But the path from "yes, immunomodulation matters" to a commercial non-antibiotic macrolide derivative is 7-10 years and $10-50M. Information value is high; product probability is near-zero. |
| **15** | **#17 -- Quorum Quenching** | WOUNDED | Genuinely novel mechanism. But zero functional studies of LuxS in F. necrophorum, high risk that LuxS is metabolic (not QS), and AI-2 inhibition could disrupt the entire rumen ecosystem. The luxS deletion experiment ($40-60K) is the right binary test, but it is expensive for a low-probability outcome. |
| **16** | **#25 -- Bacteriocin-Producing Probiotic** | WOUNDED | Four sequential research challenges (find bacteriocin, find producer, achieve wall colonization, demonstrate persistence) each at <50% probability. Cumulative success probability <5%. The $15K screening experiment could yield a hit but the path to product is 5+ years of basic research. Ranked last among active candidates. |
| **17** | **#23 -- Anti-Biofilm Dispersal (reframed)** | WOUNDED (resurrected) | Reframed from abscess interior (impossible) to rumen wall biofilm (feasible). But biofilm at the rumen wall is unproven, matrix composition is unknown, and even if proven, this would be an adjunct to other interventions. Ranked last because it addresses a hypothetical mechanism at a hypothetical site. |

---

## Step 4: Board Decision

### A. Priority De-Risk Sequence (Top 3 Experiments)

If Elanco can fund only three experiments, these three, in this order:

#### Experiment 1: KE#1 -- Paired 16S Typing of Abscesses from Tylosin vs Untreated Cattle
- **Cost:** $15-20K
- **Timeline:** 4-6 weeks
- **What it answers:** What fraction of liver abscesses under tylosin are hindgut-origin? Does tylosin selectively prevent rumen-origin LA?
- **Why first:** This restructures the entire portfolio. If hindgut abscesses are >40% of residual LA under tylosin, the portfolio pivots hard toward barrier integrity and systemic approaches. If <15%, rumen-focused strategies gain confidence and hindgut candidates are deprioritized. Every other experiment's priority depends on this answer.
- **Design:** n=100 abscesses from tylosin-treated cattle + n=100 from untreated cattle at the same feedlot. 16S rRNA amplicon sequencing + culture. Primary endpoint: Fusobacterium-dominated vs Bacteroidetes-dominated proportion in each group. Secondary: erm(B) resistance gene prevalence, subspecies ratios.
- **Who benefits:** Every candidate in the portfolio. This is pure information, not candidate-specific.

#### Experiment 2: MON+BX Independent Replication Trial
- **Cost:** $80-100K
- **Timeline:** 8-10 months (one feeding cycle)
- **What it answers:** Does MON+BX reduce LA prevalence vs MON+TYL in a second feedlot with an independent BX formulation? Is the Felizari 2025 result replicable?
- **Why second:** The portfolio backbone depends on this result. If MON+BX fails to replicate, the combination strategy (#26) is dead and the program must restructure.
- **Design:** n=500, 3-arm: MON+TYL (positive control), MON+BX (test), MON-only (negative control). Primary endpoint: LA prevalence at slaughter. Include: (a) abscess 16S typing (leverages KE#1 methodology), (b) BX anti-Fn activity in the presence of feedlot-concentration dietary protein (tests the tannin protein-binding saturation concern from Claude Opus).
- **Who benefits:** Candidates #1 and #26 directly. The entire portfolio's near-term strategy indirectly.

#### Experiment 3: Vaccine Foundation Package (PL4 Sequence Survey + Rumen Fluid IgG Access)
- **Cost:** $35-50K total ($15-20K for PL4 survey + $20-30K for IgG access study)
- **Timeline:** 8-12 weeks (can run in parallel)
- **What it answers:** (a) Is the PL4 epitope region conserved across >=50 bovine field isolates from >=3 feedlots? (b) Does systemic vaccination generate detectable anti-PL4 IgG at the rumen wall mucosal surface?
- **Why third:** These are binary prerequisites for the entire vaccine strategy. If PL4 varies significantly across field strains, no vaccine based on a single PL4 variant will work. If serum IgG does not reach the rumen wall, no systemic vaccine will prevent colonization -- and the entire rationale for combining vaccines with burden reduction collapses.
- **Design:** (a) Collect >=50 F. necrophorum isolates from liver abscesses at >=3 feedlots; PCR amplify and sequence the PL4 region; assess epitope conservation. (b) Vaccinate 10 steers with existing PL4 immunogen; collect paired serum and rumen fluid samples at 2, 4, 8 weeks; quantify anti-PL4 IgG in both compartments by ELISA.
- **Who benefits:** Candidates #4, #5 (as validation tool), #12, #26. If either result is negative, the vaccine branch of the portfolio is pruned and resources redirect to non-immunological approaches.

**Total cost of top 3 experiments: $130-170K**
**Total timeline: 3-10 months (KE#1 is 4-6 weeks; replication trial is 8-10 months; vaccine package is 8-12 weeks in parallel with replication trial)**

### B. KE#1 Recommendation

**YES -- KE#1 should run BEFORE the de-risk sequence, not concurrently.**

The Board recommends KE#1 (Experiment 1 above) as the absolute first investment, running before anything else. At $15-20K and 4-6 weeks, it is the cheapest, fastest, highest-information-value experiment in the portfolio. Its result changes the priority of every other experiment:

- **If hindgut fraction under tylosin is >40%:** Rumen-focused burden reduction (MON+BX) has a lower ceiling than assumed. Barrier integrity and hepatic immune approaches gain priority. The MON+BX replication trial (Experiment 2) still runs but the Triple Stack (#26) may need a hindgut component.
- **If hindgut fraction under tylosin is <15%:** Rumen-focused strategies are validated. MON+BX + rPL4 vaccine combination has a realistic path to matching tylosin. Hindgut candidates (#9, #10) are deprioritized to Tier 3.
- **If erm(B) resistance prevalence is high (>5%):** The urgency for a tylosin replacement accelerates. This changes the commercial calculus for Elanco -- a product that is 5-10 points inferior but non-antibiotic becomes more attractive if tylosin resistance is spreading.

**Practical note:** KE#1 requires access to a packing plant where tylosin-treated and untreated cattle from the same feedlot are slaughtered on the same day. Elanco's Benchmark database (68,000+ feedlots) can identify suitable feedlots. Abscess collection is free -- done at normal slaughter inspection. The only cost is sequencing and culture.

### C. Targets Requiring Deferral

The following targets are valid but should wait for first-tranche results before investment:

| Candidate | Wait For | Why |
|-----------|----------|-----|
| **#26 (Triple Stack)** | MON+BX replication + vaccine foundation package | Do not spend $150-200K on a combination trial until both components individually validate |
| **#4 (Multi-Antigen Vaccine)** | Vaccine foundation package (#12 prerequisites) + reformulation | Must replace hemagglutinin with validated OMP; must confirm PL4 conservation and rumen IgG access first |
| **#5 (Anti-FomA mAb, reframed)** | Vaccine foundation package | If rumen IgG access study shows systemic antibodies reach the rumen wall, mAb validation may be unnecessary -- vaccination provides the answer |
| **#2 (Butyrate)** | KE#1 result | If hindgut fraction is high, barrier integrity at both rumen AND hindgut becomes higher priority, potentially elevating this candidate |
| **#8 (Intranasal IgA vaccine)** | Rumen fluid IgG access study | If systemic IgG reaches the rumen wall adequately, mucosal vaccination is unnecessary. If not, intranasal IgA gains priority dramatically |
| **#13 (Leukotoxin receptor ID)** | Vaccine adjuvant titer study | If adjuvant technology solves the titer duration problem, receptor blocking is less urgent. If not, receptor ID becomes the only viable anti-leukotoxin strategy |
| **#6, #10, #16, #17, #18, #25** | All first-tranche results | Long-horizon candidates. None should receive investment until the portfolio's core strategy (burden reduction + immune support) is validated or refuted |

---

## Summary Scorecard

| Metric | Before Board | After Board |
|--------|-------------|-------------|
| **KILLED (total)** | 10 | 10 (same candidates; #14, #24 upheld; #27 killed as program candidate but MIC test authorized) |
| **SURVIVED** | 6 (#1, 9, 12, 20, 26, 27) | 4 (#1, 9, 12, 26) -- all conditional |
| **WOUNDED** | 12 | 14 (#5 and #23 resurrected to wounded; #27 downgraded from survived to information-only) |
| **Resurrections** | -- | 2 (#5 reframed, #23 reframed) |
| **Downgrades** | -- | 2 (#12 to conditional, #27 to killed-as-candidate) |
| **Mandatory prerequisites added** | 0 | 4 (MON+BX replication, PL4 survey, rumen IgG access, KE#1 first) |

### Portfolio Composition After Board

**Near-term actionable (conditional):**
1. MON+BX (#1) -- burden reduction backbone
2. rPL4 vaccine (#12) -- immune evasion, if prerequisites pass
3. Hindgut prebiotic (#9) -- unaddressed 24%, contingent on KE#1

**Second tranche (after first-tranche validation):**
4. Triple Stack (#26) -- combination bet
5. Multi-antigen vaccine (#4) -- reformulated
6. Anti-FomA mAb (#5) -- as mechanistic validation tool

**Long-horizon (deferred):**
7-17. All wounded candidates, prioritized by which first-tranche results change their status.

### Critical Path

```
Week 0-6:    KE#1 (abscess typing, $15-20K)
Week 0-12:   Vaccine foundation package (PL4 survey + IgG access, $35-50K, parallel)
Week 6-46:   MON+BX replication trial ($80-100K, depends on feedlot cycle)
Week 12-24:  Adjuvant titer study ($50-70K, IF prerequisites pass)
Week 46-58:  Triple Stack field trial ($150-200K, IF components validate)
```

**Total portfolio cost through Triple Stack decision gate: ~$330-440K**
**Timeline to first definitive combination data: ~14-16 months**

---

## Final Note to Overwatch

This portfolio is honest about its vulnerability. The near-term backbone (MON+BX) has a single-study dependency and a 10-point efficacy gap. The long-term backbone (rPL4 vaccine) faces a 30-year failure history at its target endpoint. The combination (Triple Stack) is untested, expensive, and inherits both vulnerabilities.

What makes this portfolio defensible despite these weaknesses is the de-risk sequence. Every major investment is gated behind a cheap, fast, binary experiment. KE#1 ($15-20K, 6 weeks) restructures the portfolio. The PL4 survey + IgG access study ($35-50K, 12 weeks) either validates or kills the vaccine strategy. MON+BX replication ($80-100K, 10 months) either confirms or kills the burden reduction backbone. At each gate, the Board recommends the cheapest experiment that could change the most decisions.

The EU September 2026 antimicrobial restriction deadline creates urgency, but urgency must not override evidence. Spending $200K on a Triple Stack field trial before validating its components is not urgency -- it is waste. The Board's de-risk sequence costs $130-170K and produces three portfolio-restructuring answers within 12 months. That is the correct first investment.
