# Phase 5 — Coverage Map: 70% Test for AB03-A Rumen H₂ Sink

**Program:** AB03-A — Rumen H₂ Sink (Biochemistry Mode) | **Internal Agteria** | **Version:** v1
**Agent:** Anvil | **Date:** 2026-03-30

---

## CRITICAL: The Portfolio-Restructuring Experiment (KE#1) Has Not Been Run

**The KE#1 — 13C-CO₂ pulse experiment in cannulated cattle under escalating 3-NOP doses — has not been run.** This experiment determines what fraction of displaced H₂ naturally routes to acetogenesis vs. propionogenesis vs. loss pathways. The following coverage estimates and target priorities may change fundamentally based on its outcome.

**Board recommendation:** Run KE#1 in parallel with the Priority De-Risk Sequence (~$25-30K, 8-12 weeks).

**Impact if KE#1 shows acetogenesis is dominant natural compensation (>20% of displaced H₂):** Validates 5.2 (HDCR transplant) as amplifying the right pathway; coverage estimates for Stage 5 may increase.

**Impact if KE#1 shows acetogenesis is minimal (<10%):** Validates 5.2 as installing a needed pathway the rumen cannot build itself; shifts strategic emphasis toward engineering over amplification. Coverage estimates for Stage 5 remain at current conservative levels.

---

## Step 0: KE#1 Status

**KE#1: 13C-CO₂ pulse experiment — NOT RUN**
**Estimated cost:** $25-30K | **Timeline:** 8-12 weeks
**Why it matters:** Without this data, we do not know whether the rumen's natural response to methanogenesis inhibition is primarily acetogenesis, propionogenesis, distributed minor sinks, or loss (rumen wall absorption). This determines whether AB03 amplifies what the rumen is already doing or installs something new.

**Recommendation: Run KE#1 BEFORE committing to the full de-risk sequence. All coverage estimates below are provisional pending KE#1 results.**

---

## Step 1: Strategic Prioritisation — Priority De-Risk Sequence

Using Board's force-ranking. The question: **If you can fund only 3 experiments, which 3 and why?**

### Priority De-Risk Sequence (Board-defined)

| Priority | Experiment | Target | Cost | Timeline | Leverage | Information Value | Concentration Risk |
|----------|-----------|--------|------|----------|----------|-------------------|-------------------|
| **1** | HDCR expression + activity at 39C in *E. limosum* | 5.2/V1 | $15-20K | 3-4 months | HIGH — addresses Gate 2 (H₂ threshold) directly; if enzyme works, the program has a validated molecular target | CRITICAL — resolves 3 unknowns in 1 experiment (temperature, direction, host compatibility) | HIGH — if this fails AND *Ca.* Faecousia cultivation fails, the acetogenesis engineering path stalls; pivot to *S. ovata* or *M. elsdenii* |
| **2** | DHNA/riboflavin redox cycling in rumen fluid | 8.1/V6 | $5-8K | 2-4 weeks | HIGH — addresses the NADH/NAD⁺ bottleneck upstream of H₂; if catalytic cycling works, a non-GMO feed additive pathway opens | CRITICAL — cheapest test of the most novel mechanism; binary GO/KILL in 2-4 weeks | LOW — failure eliminates 8.1 but other candidates unaffected |
| **3** | *Ca.* Faecousia cultivation attempt | 5.1 | $30-50K | 6-12 months | VERY HIGH — if cultivated, it becomes the foundation (DFM, gene donor, novel hydrogenase source); the organism that actually responds in vivo | HIGHEST — asymmetric upside; even failure is informative (confirms engineering path is the only option) | MODERATE — single-study dependency (Pope 2025); if cultivation fails, *E. limosum* remains the chassis |

### Extended Portfolio (not first-dollar investments but tracked)

| Rank | Target | Status | Role |
|------|--------|--------|------|
| 4 | 4.1/V5 — PEP carboxylase engineering | Wounded | Propionogenesis enhancement; endogenous fumarate generation |
| 5 | 2.1/V2 — Engineered adhesin display | Wounded (Board downgrade) | Gate 3 (spatial coupling) — concept correct, execution speculative |
| 6 | 6.1 — Encapsulated nitrate | Wounded | Supporting sink (5-7% H₂ capture); most immediately deployable |
| 7 | X.2/V7 — Phloroglucinol + *Coprococcus* | Wounded | Unique formate capture; engineering route preferred over co-administration |
| 8 | 4.2 — Fumarate bridge | Wounded | Pre-adaptation; failed in cattle meta-analysis |
| 9-16 | Remaining wounded candidates | Wounded/Deferred | Various supporting roles |

---

## Step 2: The 70% Test

### Stage Classification: Tractable vs. Non-Tractable

| # | H₂ Metabolism Stage | Classification | Rationale |
|---|---------------------|----------------|-----------|
| 1 | H₂ Production (fermentative) | **NON-TRACTABLE** | H₂ production is an inherent consequence of rumen carbohydrate fermentation. Reducing it means reducing fermentation, which harms the animal. Not a drug target. |
| 2 | Interspecies H₂ Transfer | **TRACTABLE** | Spatial coupling engineering (adhesins, scaffolds) and redox mediator shuttles can modify H₂ transfer architecture |
| 3 | Methanogenesis (inhibited) | **INPUT CONDITION** | This is the problem being solved, not a stage to cover. Excluded from calculation. |
| 4 | Propionogenesis | **TRACTABLE** | Enzyme engineering (PEP carboxylase, QFR), fumarate supplementation — molecular interventions are plausible |
| 5 | Reductive Acetogenesis | **TRACTABLE** | HDCR transplant, acetogen DFMs, *Ca.* Faecousia — primary target pathway with multiple molecular interventions |
| 6 | Nitrate/Sulfate Reduction | **TRACTABLE (limited)** | Safe-dose encapsulated nitrate; engineered matched-kinetic organisms. Hard safety ceiling limits scope, but molecular interventions exist |
| 7 | Biohydrogenation | **NON-TRACTABLE** | Capacity-capped at <5% of metabolic H₂ by dietary fat tolerance. No molecular intervention can overcome the substrate limitation. Correctly excluded by Forge. |
| 8 | Downstream Effects (NADH/NAD⁺ ratio, VFA shift, fiber degradation) | **TRACTABLE** | Quinone/flavin redox mediators, potentially NADH-related interventions target the NADH reoxidation bottleneck directly |
| 9 | Microbial Ecology (community restructuring) | **TRACTABLE** | Pre-adaptation protocols, DFM dosing, early-life programming — biological interventions to shape community composition |

**Summary:** 7 tractable stages (Stages 2, 4, 5, 6, 8, 9 + Stage 6 with safety ceiling). 2 non-tractable (Stages 1, 7). 1 input condition (Stage 3). The 70% threshold applies to the 7 tractable stages.

---

### Coverage by Tractable Stage

**Design target (Board):** Complement Bovaer (3-NOP) at commercial dose (20-35% CH₄ reduction, displacing ~15-22 mol [2H]/day). Multi-sink approach capturing 30-50% of displaced H₂.

| # | Tractable Stage | Surviving/Wounded Candidates | Best-Case Pathology Reduction | Evidence Basis | Confidence |
|---|----------------|------------------------------|-------------------------------|----------------|------------|
| **2** | Interspecies H₂ Transfer | **2.1/V2** (adhesin — WOUNDED), **8.1/V6** (redox mediator — WOUNDED, elevated priority) | **15-25%** of displaced H₂ redirected via improved spatial coupling or upstream electron interception | Adhesin binding demonstrated (Ng 2016); EET via quinones demonstrated in *L. plantarum* (eLife 2022); Tribunal Prediction 9 (>3x rate with attachment) untested | [INFERRED] — no rumen-specific data for either intervention |
| **4** | Propionogenesis | **4.1/V5** (PEP carboxylase — WOUNDED), **4.2** (fumarate bridge — WOUNDED), **4.3/V5** (QFR — WOUNDED) | **10-20%** of displaced H₂ routed to propionate via enhanced fumarate reduction | At 30% inhibition, propionogenesis captures ~7.5% of displaced H₂ naturally (Ungerfeld 2015); engineering or substrate supplementation could 2-3x this. Fumarate captures 44% in vitro but fails in cattle in vivo. Board-corrected stoichiometry: engineered *Prevotella* at realistic rumen abundance (~5-10% of community) could add 5-13% | [INFERRED] — PEP carboxylase overexpression proven in *E. coli* but never in rumen organisms |
| **5** | Reductive Acetogenesis | **5.2/V1** (HDCR transplant — SURVIVED with caveats), **5.1** (*Ca.* Faecousia — WOUNDED, elevated priority), **5.4** (consortium — WOUNDED), **5.3** (*A. woodii* genes — WOUNDED) | **15-25%** of displaced H₂ routed to acetate via enhanced Wood-Ljungdahl pathway | Vulcan estimate: engineered acetogen at realistic 0.5-1% biomass (Board-corrected from 5%) captures ~2.5-5% at 30% inhibition. But: *Ca.* Faecousia expanded dramatically in vivo (Pope 2025), and natural adaptation may contribute 10-20% (Prediction 7/KE#1). Combined engineered + natural: 15-25%. | [INFERRED] — HDCR activity at 39C unknown; *Ca.* Faecousia uncultivated; DFM persistence uncertain |
| **6** | Nitrate/Sulfate Reduction | **6.1** (encapsulated nitrate — WOUNDED) | **5-7%** of displaced H₂ at safe dose | Encapsulated nitrate: 18.5% CH₄ reduction with no methemoglobinemia (Lee 2019). At safe dose (20-30 g NaNO₃/day), captures ~5-7% of displaced H₂ at 30% inhibition (Board-corrected from Reaper's 10-15%). | [MODERATE] — dosing data exists; stoichiometry straightforward; safety demonstrated at tested doses |
| **8** | Downstream Effects | **8.1/V6** (redox mediator — WOUNDED, elevated priority) | **10-20%** improvement in fermentation efficiency if catalytic cycling works (i.e., H₂ not sunk directly but NADH reoxidation maintained, preserving glycolytic flux) | EET demonstrated in *L. plantarum* (eLife 2022); rumen-specific data: zero. If catalytic cycling works, it does not sink H₂ directly — it prevents the NADH/NAD⁺ ratio shift that impairs fermentation, allowing the animal to tolerate higher H₂ without productivity loss. Effect is on PRODUCTIVITY, not on H₂ disposal. | [INFERRED] — mechanism entirely unvalidated in rumen context |
| **9** | Microbial Ecology | **9.1** (pre-adaptation — WOUNDED by Board), **9.3** (early-life — DEFERRED) | **10-15%** acceleration of natural community adaptation via DFM dosing under 3-NOP | Pope 2025 showed community remodeling under 3-NOP in calves with no productivity loss at 62% inhibition. Board redesigned 9.1 as direct DFM + 3-NOP rather than fumarate pre-adaptation. Natural adaptation contributes but takes days-weeks. Pre-adapted populations may reduce the critical gap window. | [INFERRED] — sequential protocol untested; population expansion in vivo undemonstrated |

---

### Coverage Calculation

**Method:** For each tractable stage, the coverage estimate represents the fraction of the total H₂ disposal problem that surviving/wounded candidates could address if they work as proposed. These are NOT additive across stages in a simple sum because (a) some candidates address the same pool of displaced H₂, (b) Stage 8 addresses productivity rather than H₂ disposal directly, and (c) the "missing hydrogen" distributed across minor pathways means not all H₂ needs active sinking.

**Honest coverage assessment at design target (30% CH₄ inhibition, ~21 mol H₂/day displaced):**

| Stage | H₂ Capture / Mitigation | Status |
|-------|------------------------|--------|
| Stage 5 — Acetogenesis (primary) | 15-25% of displaced H₂ | Covered (5.2 + 5.1 + natural adaptation) |
| Stage 4 — Propionogenesis | 10-20% of displaced H₂ | Covered (4.1 + natural increase) |
| Stage 2 — Transfer architecture | 0-15% improvement in H₂ delivery to sinks | Covered (2.1/8.1 enable other sinks; effect is multiplicative, not additive) |
| Stage 6 — Nitrate (supporting) | 5-7% of displaced H₂ | Covered (6.1) |
| Stage 8 — NADH reoxidation | 10-20% fermentation efficiency improvement | Covered by concept (8.1); entirely unvalidated |
| Stage 9 — Community ecology | 10-15% acceleration of adaptation | Covered (9.1 redesigned) |

**Total H₂ capture (Stages 5 + 4 + 6, direct sinking):** 30-52% of displaced H₂ at 30% inhibition

**Note on missing hydrogen:** At 30% inhibition, 37-72% of displaced H₂ is naturally "missing" (routed to formate, rumen wall absorption, ethanol, chain elongation, biomass). This means the rumen's native compensation already handles a substantial fraction. AB03 needs to capture enough of the REMAINING H₂ to prevent the dissolved H₂ from reaching damaging concentrations (>20-40 uM threshold, Prediction 3).

**Combined portfolio effect (Board design target):** At 30% CH₄ inhibition, the multi-sink portfolio plus natural compensation could capture 60-80% of displaced H₂, keeping dissolved H₂ below the threshold that impairs fermentation.

---

### 70% Test Result

| Metric | Value | Status |
|--------|-------|--------|
| Total tractable stages | 7 (Stages 2, 4, 5, 6, 8, 9) | — |
| Stages with surviving/wounded candidates | **6/7** (all except Stage 6 which has only a minor supporting candidate) | — |
| Stages with at least one candidate in Board top-5 | **4/7** (Stages 2, 4, 5, 8) | — |
| Estimated tractable pathology coverage | **~75-85%** of tractable stages have at least one plausible intervention | — |
| Estimated H₂ capture at 30% inhibition | **30-52%** direct sinking + natural compensation | — |
| 70% threshold | **CONDITIONAL PASS** | See caveats |

### Caveats on the 70% PASS

**This is a conditional pass, not a clean pass.** The caveats are severe:

1. **Every coverage estimate except Stage 6 (nitrate) is tagged [INFERRED].** No candidate has been validated in the rumen for H₂ disposal. The highest-ranked candidate (5.2 HDCR transplant) has not been expressed in the host organism, let alone tested in rumen fluid.

2. **The Board corrected the biomass assumption** from 5% to 0.5-1% for engineered DFMs, which reduces the stoichiometric case for 5.2 from "25% capture" to "2.5-5% capture" from the engineered organism alone. The gap is filled by natural adaptation (which Pope 2025 supports but KE#1 has not quantified).

3. **KE#1 has not been run.** If KE#1 shows that reductive acetogenesis accounts for <10% of displaced H₂ even after 4 weeks of adaptation (Prediction 7), the Stage 5 coverage estimate drops, and the portfolio may fall below 70%.

4. **Stage 8 (downstream effects) coverage is entirely conceptual.** The redox mediator shuttle (8.1) has zero rumen data. If it fails (Prediction B2 negative), Stage 8 loses its only candidate.

5. **No single candidate addresses >25% of the problem alone.** This is a multi-sink portfolio by necessity, which means partial failure of any one candidate may not be compensated by others.

**Honest assessment: The portfolio provides broad coverage of tractable H₂ metabolism stages, but with shallow depth of evidence at every stage. The 70% pass is architectural (every stage has a plausible candidate) rather than evidential (every stage has a validated candidate).**

---

## Coverage Gap Report

| Gap | Severity | Action |
|-----|----------|--------|
| Stage 5 depth — engineered acetogenesis not yet validated | **HIGH** | Priority Experiment 1 (HDCR at 39C) resolves the gating question |
| Stage 8 depth — redox mediator entirely unvalidated | **MODERATE** | Priority Experiment 2 (DHNA cycling) is cheap and fast; binary GO/KILL |
| Stage 9 depth — pre-adaptation protocol redesigned but untested; early-life deferred | **LOW** | Board correctly deferred; revisit after DFM persistence data available |
| KE#1 not run — strategic direction uncertain | **HIGH** | Run in parallel with Priority De-Risk Sequence |
| Stage 6 — nitrate is minor (5-7%) and has individual variability risk | **LOW** | Acceptable as supporting sink; not worth additional investment |

---

## Summary

The AB03-A portfolio passes the 70% test conditionally. Six of seven tractable H₂ metabolism stages have at least one plausible intervention from the surviving/wounded candidate list. The portfolio is designed as a multi-sink approach at the Board's design target of 30% CH₄ inhibition (Bovaer commercial dose), where natural rumen compensation plus engineered interventions could capture 60-80% of displaced H₂.

The conditional nature of the pass reflects the reality that the program is at a very early stage: no candidate has been validated in the rumen, and the gating experiments (HDCR at 39C, redox mediator cycling, *Ca.* Faecousia cultivation, KE#1) will determine whether the coverage estimates hold.

**If Priority Experiments 1 and 2 both fail (HDCR <100 s⁻¹ at 39C AND no redox mediator cycling), the portfolio drops below 70% and must be restructured.** Contingency: pivot to *Sporomusa ovata* as chassis (verified low H₂ threshold at 6 Pa, Schuchmann & Muller 2014) or *Megasphaera elsdenii* (commercial DFM precedent, Board Finding #10).
