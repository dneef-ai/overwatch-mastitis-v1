# Phase 5 -- Coverage Map: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Agent:** Anvil (Portfolio Architect)
**Date:** 2026-03-27
**Partner:** Elanco
**Status:** Complete

---

## Step 0: Portfolio-Restructuring Experiment (KE#1)

**CRITICAL: The portfolio-restructuring experiment (KE#1) has not been run. KE#1 is a quantitative comparison of rumen wall vs. hindgut (colonic epithelium) as the primary source of hepatic F. necrophorum, using matched qPCR on rumen epithelium, colonic epithelium, and liver abscess material from the same animals. Cost: $15-25K. Timeline: 4-8 weeks.**

**If hindgut contribution exceeds 20%:** All rumen-focused Gate 1 interventions (phage cocktail) have an intrinsic ceiling. The vaccine would need Bacteroides-targeting antigens currently absent from the portfolio. Coverage estimates below would require downward revision for Gate 1 components.

**If hindgut contribution is <5%:** Current portfolio architecture is correct. Coverage estimates below hold.

**Board decision:** KE#1 runs in parallel with Priority De-Risk experiments. Results expected alongside de-risk data in 16-20 weeks.

The following coverage estimates assume rumen-dominant translocation (hindgut <20%), consistent with the current literature balance. All estimates are tagged with sensitivity to KE#1 outcome.

---

## Step 1: Strategic Prioritisation (Force-Ranked from Board)

**If you can fund only 3 experiments, which 3 and why?**

| Rank | Experiment | Cost | Why |
|------|-----------|------|-----|
| 1 | **V2/LktC acyltransferase assay** | $5-10K | Highest information/dollar. Binary: opens a first-in-class drug target nobody else is pursuing, or dies permanently. Novel = Agteria's strategic differentiator. Addresses the rate-limiting bottleneck (Gate 2) at the molecular level. |
| 2 | **G2-3 + G2-8: Multi-antigen vaccine immunogenicity trial** | $30-50K | Resolves two critical risks to the lead product: (a) can modern adjuvant + epitope focusing beat Fusogard's titer? (b) does FomA complement sensitization translate from human Lemierre's to bovine liver abscess? One trial, two answers. Run at an INDEPENDENT lab to address the portfolio-level single-lab dependency on KSU. |
| 3 | **G1-2: Phage rumen stability trial** | $15-25K | Resolves the strongest external challenge (rumen pharmacokinetics). If phage survives and suppresses F. necrophorum, the portfolio gains a non-antibiotic Gate 1 component -- the tylosin replacement Elanco needs for EU September 2026. If it fails, vaccine-only strategy proceeds. |

**Priority De-Risk Sequence total: $50-85K, 16-20 weeks**
**+ KE#1 in parallel: $15-25K**
**First-tranche total: $65-110K**

**Extended Portfolio** (not in first tranche, await de-risk results or triggers):

| Target | Status | Trigger to Fund |
|--------|--------|----------------|
| G2-1: Anti-LktA mAb | Deferred | Vaccine titer insufficient at 16 weeks; mAb needed as bridging |
| G2-2: mRNA vaccine | Deferred | Elanco-Medgene H5N1 data shows >=4x titer advantage over subunit |
| G2-10: DNase assay | Gated | $2-5K binary experiment; positive = resurrect NET preservation |
| G1-1: Hemagglutinin gene ID | Gated | Mass spec gene identification; positive = new vaccine component |
| G1-8: Biofilm confirmation | Gated | $5-8K confocal; positive = opens anti-biofilm targeting |
| PG-4: Blood biomarker | Parallel research tool | Fund alongside vaccine trial for trial monitoring |

---

## Step 2: The 70% Test

### 2A: Disease Stage Classification

| # | Disease Stage | Gate | Tractable for Elanco? | Rationale |
|---|--------------|------|----------------------|-----------|
| 1 | Acidosis / rumenitis | Gate 0 | **NON-TRACTABLE** (management/nutrition) | Diet-driven. Elanco sells monensin (Rumensin) as a feed efficiency product, not as an abscess preventive. Monensin alone = 0% abscess reduction. pH management is a management practice, not a pharmaceutical target. Reported for completeness. |
| 2 | Rumen wall colonization by F. necrophorum | Gate 1 | **TRACTABLE** | Phage (biologic), anti-adhesion vaccine, antimicrobial -- all pharmaceutical/biologic modalities Elanco can develop and sell. |
| 3 | Portal transit / complement evasion | Gate 1-2 transition | **TRACTABLE** | Vaccine-mediated complement sensitization (anti-FomA), opsonizing antibodies. Biologic modality within Elanco's capability. |
| 4 | Hepatic immune evasion (BOTTLENECK) | Gate 2 | **TRACTABLE** | Vaccine (anti-LktA), small molecule anti-virulence (LktC inhibitor if confirmed), mAb. Drug/biologic targets. This is the core of the portfolio. |
| 5 | Abscess formation (pre-encapsulation, 3-10 day window) | Post-Gate 2 | **NON-TRACTABLE** (current state) | No diagnostic exists to identify animals in this window. Treatment would require prophylactic systemic administration to all cattle. TGF-beta pathway inhibition is immunosuppressive. Board killed PG-1 (anti-stellate cell). Potentially tractable with a blood biomarker (PG-4), but PG-4 is a research tool, not a product. |
| 6 | Chronic persistence (encapsulated abscess) | Irreversible | **NON-TRACTABLE** (physics barrier) | Fibrous capsule prevents antibiotic penetration. Board and Reaper concur: pharmacokinetically impossible. Forge, Reaper, and Board all agree. |
| 7 | Continuous reseeding from rumen | Recurring Gate 1 | **TRACTABLE** | Ongoing suppression via phage (in-feed continuous), vaccine-mediated immune surveillance. Pharmaceutical/biologic approaches exist. |
| 8 | Polymicrobial synergy (T. pyogenes, Bacteroides) | Cross-stage | **PARTIALLY TRACTABLE** | T. pyogenes component addressable by adding antigens to multi-antigen vaccine (near-zero marginal cost). Bacteroides component poorly characterized. |
| 9 | Hindgut translocation pathway | Alt Gate 1 | **CONDITIONALLY TRACTABLE** | Depends on KE#1. If hindgut >20%, this becomes a real tractable stage. Colonic drug delivery is undeveloped but not physically impossible. |

**Tractable stages for coverage calculation:** Stages 2, 3, 4, 7, and 8 (partially).
**Non-tractable stages excluded:** Stages 1 (management), 5 (no diagnostic), 6 (physics barrier).
**Conditional stage:** Stage 9 (hindgut) -- included at reduced weight pending KE#1.

### 2B: Pathology Weight Estimation

The Tribunal's sequential gate model provides the framework for estimating each stage's contribution to disease incidence.

| Tractable Stage | Pathology Contribution | Basis | Evidence Tier |
|----------------|----------------------|-------|---------------|
| Stage 2: Rumen wall colonization | **15-20%** | Modulating Gate 1 throughput reduces the inoculum arriving at Gate 2. Tylosin achieves 40-70% reduction primarily via this mechanism, but tylosin also has immunomodulatory effects. Pure inoculum reduction (without immunomodulation) likely accounts for 15-20% of disease prevention. Key data: monensin alone = 0% (targets wrong organisms); tannins alone = 0% (P>0.05); tylosin's antimicrobial component alone (estimated via CTC comparison) ~40%. Phage would target F. necrophorum specifically. | [INFERRED from comparative failure analysis] |
| Stage 3: Portal transit / complement evasion | **10-15%** | Factor H binding varies 5-42% across strains (Friberg 2008). Strains with strongest binding cause most severe disease. Restoring complement killing during portal transit reduces the viable inoculum arriving at sinusoids. Effect is additive with Stage 2 (inoculum reduction) and Stage 4 (immune evasion). Neisseria fHbp vaccine (Bexsero) achieves significant reduction in meningococcal disease via this mechanism. Estimated contribution to abscess prevention: moderate, because portal transit time (~30 seconds) limits MAC formation, but opsonization for downstream Kupffer cell uptake is rapid. | [INFERRED from Friberg 2008 + Neisseria analogy] |
| Stage 4: Hepatic immune evasion (BOTTLENECK) | **50-60%** | This is the rate-limiting step. Tribunal 4/4 convergence. Leukotoxin production correlates with severity at P < 0.0001 (Pillai 2021). Leukotoxoid vaccine achieved 80% protection in controlled challenge (Saginala 1997). If leukotoxin is fully neutralized, the liver's Kupffer cell defense (>99% bacterial clearance capacity) handles the inoculum. The 50-60% estimate reflects that even with perfect neutralization, chronic high-volume translocation on high-grain diets may periodically overwhelm the defense (the firehose problem -- Fusogard's failure on grain diets). Perfect neutralization in challenge models = 80-100% protection; field adjustment for continuous exposure and strain variation = 50-60%. | [MODERATE -- challenge data + field adjustment] |
| Stage 7: Continuous reseeding | **10-15%** | Continuous translocation sustains the disease across the 120-400 day feeding period. Sustained immune surveillance (vaccine-maintained titers) and sustained pathogen suppression (continuous phage feeding) address this. The contribution is inherently captured in Stages 2+3+4 if those interventions are sustained throughout the feeding period. Reported separately to reflect the TIME dimension: interventions that wane (e.g., mAb after 21 days) fail here. | [INFERRED -- dimensional overlap with Stages 2-4] |
| Stage 8: Polymicrobial synergy | **5-10%** | T. pyogenes present in 29% of abscesses. When present, it increases severity. Addressing T. pyogenes (via multi-antigen vaccine component) reduces severe (A+) abscesses in the TP-positive subset. Population impact: ~29% x 30-50% severity reduction = 9-15% reduction in severe abscesses. Bacteroides contribution poorly characterized but estimated at ~20-33% of abscesses (16S data); currently unaddressed by portfolio. | [INFERRED from Abbasi 2025, Fuerniss 2022] |

**NOTE ON DOUBLE-COUNTING:** Stages 2, 3, 4, and 7 form a sequential cascade. Their pathology contributions are not strictly additive -- addressing Stage 4 (the bottleneck) captures the largest share, and Stages 2, 3, and 7 provide additive benefit by reducing the load the Stage 4 intervention must handle. The coverage calculation below uses a CASCADE MODEL: each intervention independently reduces the probability of abscess formation, and combined effects are multiplicative (1 - product of residual risks), not additive.

### 2C: Coverage Calculation

**Portfolio candidates mapped to tractable stages:**

| Tractable Stage | Surviving Candidate(s) | Max Pathology Reduction (if works perfectly) | Confidence |
|----------------|----------------------|-------------------------------------------|-----------|
| Stage 2: Rumen wall colonization | G1-2: Phage cocktail | 25-40% reduction in rumen F.n. load, translating to 15-25% reduction in translocation events | PRELIMINARY (phage exist, rumen efficacy untested) |
| Stage 3: Portal transit | G2-8: Anti-FomA (complement sensitization) | 15-30% reduction in viable bacteria reaching sinusoids via restored complement killing + opsonization | MODERATE (Friberg 2008; Neisseria precedent; bovine confirmation needed) |
| Stage 4: Hepatic immune evasion | G2-3: Epitope subunit vaccine (LktA PL1+PL3+PL4) | 40-60% reduction in abscess incidence via leukotoxin neutralization | MODERATE (Saginala 80% in challenge; field estimate 40-60% with improved adjuvant) |
| Stage 4: Hepatic immune evasion (novel) | V2/LktC: Acyltransferase inhibitor (if confirmed) | 40-60% reduction (equivalent to leukotoxin neutralization if acylation is required for activity) | INFERRED (acyltransferase function untested) |
| Stage 7: Continuous reseeding | G1-2 + G2-3 sustained | Captured in Stages 2+4 if sustained across feeding period | -- |
| Stage 8: Polymicrobial synergy | FomA component (anti-adhesion effect on T. pyogenes colonization, indirect); future T. pyogenes antigen addition | 5-10% reduction in severe abscesses | INFERRED |

**Cascade model -- combined portfolio if all interventions work perfectly:**

The product concept is: multi-antigen vaccine (LktA epitopes + FomA, ISCOMATRIX) + phage cocktail (in-feed).

For a given animal on high-grain diet:
- Probability of abscess without intervention: ~21% (baseline US prevalence)
- After phage (Stage 2): inoculum reduction of 25-40% --> residual risk = 0.79-0.85 x baseline
- After FomA complement sensitization (Stage 3): viable inoculum further reduced by 15-30% --> residual = 0.70-0.85 x previous
- After LktA vaccine (Stage 4): leukotoxin neutralized, clearance threshold raised --> residual = 0.40-0.60 x previous
- Combined residual risk: 0.79 x 0.70 x 0.40 = 0.22 (best case) to 0.85 x 0.85 x 0.60 = 0.43 (worst case)

**Estimated combined reduction in abscess incidence:**
- **Best case:** 1 - 0.22 = **78% reduction** (21% prevalence --> ~4.6%)
- **Worst case:** 1 - 0.43 = **57% reduction** (21% prevalence --> ~9.0%)
- **Central estimate:** ~**65-70% reduction** (21% prevalence --> ~6-7%)

This compares to tylosin alone at 40-70% reduction. The portfolio's central estimate MATCHES or EXCEEDS tylosin at the top end.

**If LktC acyltransferase confirms (V2):** A small-molecule LktC inhibitor would provide a second, independent mechanism at Gate 2 (preventing LktA activation rather than neutralizing it after secretion). Used in combination with the vaccine, it would raise the ceiling: estimated additional 15-25% absolute reduction in the vaccine-only scenario's residual risk.

### 2D: 70% Test Verdict

**Tractable pathology stages:** Stages 2, 3, 4, 7, 8

**Coverage by the surviving portfolio:**

| Tractable Stage | Covered? | By Which Candidate? |
|----------------|----------|-------------------|
| Stage 2: Rumen wall colonization | YES | G1-2 (phage cocktail) |
| Stage 3: Portal transit / complement evasion | YES | G2-8 (anti-FomA) |
| Stage 4: Hepatic immune evasion (BOTTLENECK) | YES | G2-3 (epitope subunit vaccine) + V2/LktC (if confirmed) |
| Stage 7: Continuous reseeding | YES | Sustained by vaccine (duration) + phage (continuous in-feed) |
| Stage 8: Polymicrobial synergy | PARTIAL | FomA indirect effect; T. pyogenes antigens deferred to second-generation vaccine |

**Coverage fraction: 4.5 / 5 tractable stages covered = 90%**

**Estimated incidence reduction: 57-78% (central ~65-70%)**

**VERDICT: PASS. Tractable coverage exceeds 70%.**

**Honesty check on estimates:**
- The phage component (G1-2) is PRELIMINARY -- rumen stability untested. If phage fails, coverage drops to 3.5/5 tractable stages and estimated reduction drops to 45-60%, which is BELOW the 70% incidence reduction target but still above 70% of tractable STAGES. The test measures stage coverage, not incidence reduction: the portfolio still covers 70% of tractable stages even without phage (Stages 3, 4, 7, 8 partially = 3.5/5 = 70%). However, the incidence reduction estimate becomes more dependent on the vaccine alone overcoming the firehose problem -- which is the exact failure mode of Fusogard.
- The FomA component (G2-8) requires bovine Factor H binding confirmation. If it fails, Stage 3 is uncovered. Coverage drops to 3/5 tractable stages = 60%. This would be BELOW the 70% threshold and would trigger a gap report.
- The LktC acyltransferase (V2) is a gating experiment. If it fails, Stage 4 relies solely on the vaccine. The coverage count does not change (Stage 4 is still covered by G2-3), but the depth of coverage at the bottleneck is reduced.

**Risk matrix:**

| Scenario | Stages Covered | Coverage % | Incidence Reduction | Pass? |
|----------|---------------|------------|--------------------|----|
| All succeed (vaccine + FomA + phage + LktC) | 5/5 | 100% | 70-85% | YES |
| Vaccine + FomA + phage (LktC fails) | 4.5/5 | 90% | 57-78% | YES |
| Vaccine + FomA (phage fails) | 3.5/5 | 70% | 45-65% | MARGINAL |
| Vaccine only (FomA fails, phage fails) | 2/5 | 40% | 35-55% | NO -- gap report |
| Gate 2 approach fails entirely | 1/5 | 20% | <20% | NO -- portfolio restructure |

**The 70% test passes in the central scenario and both primary scenarios (all succeed, vaccine + FomA + phage). It becomes marginal if phage fails and sub-threshold if FomA also fails. This validates the Board's priority de-risk sequence: the experiments are designed to resolve exactly the scenarios that determine whether the portfolio passes or fails.**

---

## Stage 9: Hindgut Pathway (Conditional)

If KE#1 shows hindgut contribution >20%:
- The ~25% Bacteroidetes fraction of abscesses is PARTIALLY addressable by the FomA complement sensitization mechanism (if anti-FomA opsonizing antibodies also target hindgut-origin bacteria -- possible if Bacteroides isolates from abscesses share surface antigens with F. necrophorum).
- The phage cocktail (targeting F. necrophorum specifically) would NOT address Bacteroides-dominated abscesses.
- A dedicated hindgut component (G1-5) would be needed. This is currently DEFERRED, gated on KE#1.
- Coverage estimate with hindgut >20%: portfolio loses ~10-20% of its ceiling unless Bacteroides-targeting is added.

---

## Summary

| Metric | Value |
|--------|-------|
| Tractable disease stages | 5 (Stages 2, 3, 4, 7, 8) |
| Non-tractable stages | 3 (Stages 1, 5, 6) + 1 conditional (Stage 9) |
| Stages covered by surviving candidates | 4.5 / 5 (90%) |
| Estimated combined incidence reduction (central) | 65-70% |
| 70% tractable coverage test | **PASS** |
| Conditional on | Phage rumen stability (G1-2), bovine Factor H binding (G2-8), independent epitope replication (G2-3) |
| KE#1 sensitivity | If hindgut >20%, coverage ceiling drops ~10-20% unless Bacteroides component added |
| First-tranche budget to resolve key uncertainties | $65-110K |
