# Phase 4b -- Board Decision: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Agent:** Board (Strategic Decision-Maker)
**Date:** 2026-03-27
**Partner:** Elanco
**Status:** Complete

---

## Executive Summary

Six external frontier models challenged Reaper's kill report. The Board synthesized their challenges, conducted devil's advocate analysis on every survivor, and produced a force-ranked portfolio with a priority de-risk sequence.

**The verdict:** The Gate 2 bottleneck (leukotoxin-mediated immune evasion) stands. The portfolio center is correct. But the external panel exposed a critical weakness that Reaper underweighted: **every surviving candidate has single-lab dependency on the KSU/Nagaraja research lineage.** This is not a flaw in any individual candidate -- it is a structural risk for the entire portfolio. The first dollar should go to independent replication of the foundational claims, not to advancing any single candidate.

**Three decisions:**

1. **LktC acyltransferase assay ($5-10K)** -- the single highest-information experiment in the portfolio. Binary: if LktC is an acyltransferase, a first-in-class drug target opens. If not, that branch dies permanently. This is Agteria's strategic differentiator.

2. **Epitope subunit vaccine (G2-3) + FomA (G2-8) as a combined multi-antigen vaccine candidate** -- the lead product concept. Protein subunit, ISCOMATRIX adjuvant, single injection at processing. But GATED on independent replication of KSU epitope data and bovine Factor H binding confirmation.

3. **KE#1 abscess typing study ($15-25K) runs in parallel** -- determines whether the hindgut pathway reshapes the portfolio before committing to full development.

---

## Step 1: External Panel Synthesis on Kill Report

### Synthesized Feedback Table

| # | Finding | Models Agreeing | Verdict Change? | Action Required |
|---|---------|----------------|-----------------|-----------------|
| 1 | **G2-4 (LktB) kill too harsh** -- POTRA is flat for small molecules but barrel pore and biologic approaches survive | Grok 4, GPT-5.4, Qwen 2.5, DeepSeek R1 (4/6) | YES -- KILLED should be WOUNDED | Re-evaluate as biologic/vaccine target only, not small molecule. Board concurs: the kill of the small-molecule POTRA approach is correct, but the kill of LktB as a target entirely is overbroad. Reclassify as WOUNDED. |
| 2 | **G2-10 (DNase/NET) kill too harsh** -- undemonstrated is not disproven; cheap assay should gate, not kill | GPT-5.4, DeepSeek R1, Opus (3/6) | YES -- KILLED should be WOUNDED | Board concurs: the $2-5K DNase assay should be a gating experiment. Reclassify as WOUNDED, gated on assay. |
| 3 | **G1-1 (hemagglutinin) kill too harsh** -- unsequenced is not invalid; modern proteomics can resolve | Gemini Pro, GPT-5.4, Opus (3/6) | PARTIAL -- KILLED to WOUNDED | Board concurs with nuance: the VACCINE approach is correctly killed (you cannot make a recombinant vaccine without a sequence), but the TARGET is not dead. Gene identification via mass spec is a gating experiment. Reclassify as WOUNDED, gated on gene ID. |
| 4 | **G2-3 (epitope subunit) survival challenged** -- single-lab dependency, mouse-only epitope data, semi-purified Saginala result warns against focusing | Gemini Pro, GPT-5.4, Qwen 2.5, DeepSeek R1, Opus (5/6) | YES -- requires independent replication as mandatory gate | **Critical signal.** 5 of 6 models flag this. Board agrees: G2-3 survives but MUST be gated on independent replication of the Xiao epitope data in cattle. The Saginala semi-purification result (less protective than crude) is a genuine warning that epitope focusing could fail. This does NOT kill the candidate, but it makes independent bovine validation a hard requirement before investment exceeds $50K. |
| 5 | **G1-2 (phage) survival challenged** -- natural rumen phage-bacteria equilibrium proves phages cannot eliminate host; rumen pharmacokinetics hostile | Gemini Pro, GPT-5.4, DeepSeek R1 (3/6) | NO -- but downgraded | Board partially concurs. The ecological equilibrium argument is strong but not fatal. Super-physiological dosing has worked in other systems. The rumen stability experiment ($15-25K) is the correct gate. Board retains SURVIVED but notes this is the weakest survivor. |
| 6 | **G2-8 (FomA) survival challenged** -- all Factor H data is from human Lemierre's isolates, not bovine; species-specific complement interaction unconfirmed | GPT-5.4, Qwen 2.5, DeepSeek R1, Opus (4/6) | YES -- from SURVIVED to SURVIVED with mandatory bovine gate | 4 of 6 models flag the human-to-bovine extrapolation. Board agrees: bovine Factor H binding confirmation is a MANDATORY gate before G2-8 advances beyond the $20-30K de-risk experiment. |
| 7 | **PG-4 (biomarker) survival challenged** -- capsule prevents metabolite leakage; temporal dynamics make early detection impossible; PPV too low | Gemini Pro, GPT-5.4, DeepSeek R1, Opus (4/6) | PARTIAL | Board is split. The capsule-cuts-both-ways argument (Gemini) is strong. However, the biomarker's value is primarily as a RESEARCH TOOL for trial monitoring, not as a clinical diagnostic. Even a mediocre biomarker (AUC-ROC 0.65-0.75) that detects large abscesses at slaughter with 80%+ sensitivity would enable better clinical trial design. Board retains SURVIVED but recategorizes as research infrastructure, not product candidate. |
| 8 | **COMBO-2 survival is a bait-and-switch** -- Reaper reformulated it into COMBO-2b, which is just G2-3 + G2-8 | GPT-5.4, Opus (2/6) | YES -- COMBO-2 as originally proposed should be KILLED | Board concurs fully. COMBO-2 (mRNA + anti-adhesion) is KILLED. COMBO-2b (protein subunit LktA epitopes + FomA + ISCOMATRIX) is the actual product concept, and it IS just G2-3 + G2-8 combined. Board formalizes this: the lead product concept is a multi-antigen protein subunit vaccine combining LktA epitopes and recombinant FomA in ISCOMATRIX adjuvant. It does not need a separate COMBO designation. |
| 9 | **V14 (LuxS/AI-2) kill challenged** -- LuxS may have noncanonical signaling roles | Grok 4, GPT-5.4, Qwen 2.5 (3/6) | NO | Board disagrees with the models. The Surveyor found NO AI-2 receptor genes in the F. necrophorum genome. While noncanonical LuxS roles exist in some bacteria, three models offering this as a possibility is not evidence. The kill stands. Functional assays could theoretically rescue this, but the probability is low enough that the $5-10K is better spent on LktC or DNase assays. |
| 10 | **V2 (LktC acyltransferase) underweighted by Reaper** -- Vulcan's Tier 1 ranking, genuinely novel first-in-class target | Not explicitly flagged by panel (covered under G2-5 WOUNDED) | N/A -- Board elevates independently | Board independently elevates V2/LktC. Reaper wounded this under the combined G2-5/V2 umbrella, which diluted the LktC acyltransferase hypothesis by linking it to the intractable transcriptional silencing approach. The LktC acyltransferase assay is a standalone, binary, $5-10K experiment that either opens a first-in-class drug target (8,317 A^3 cavity, moderate-to-favorable druggability per Surveyor) or dies permanently. This is the highest-information-per-dollar experiment in the portfolio. |
| 11 | **Portfolio-level risk: what if Gate 2 is not the bottleneck?** | Opus (1/6) | LOW probability, HIGH consequence | Board notes this. The Tribunal's 4/4 agent convergence and the quantitative evidence (Magrin r=0 for rumenitis-abscess correlation; Pillai P<0.0001 for leukotoxin-severity) make this unlikely. But the portfolio hedges naturally: phage (Gate 1) + vaccine (Gate 2) covers both scenarios. No additional action needed. |
| 12 | **G1-3 (butyrate+zinc) kill challenged** -- SCFP is not a valid proxy for targeted butyrate+zinc | Grok 4, DeepSeek R1 (2/6) | NO | Only 2 models. Board upholds the kill. The logic is: SCFP's comprehensive rumen improvement produced zero abscess effect (n=4,689). Butyrate+zinc targets the same gate. The "it's different because it's targeted" argument is the same argument every failed Gate 1 intervention makes. Kill stands. |
| 13 | **Single-lab dependency is PORTFOLIO-LEVEL, not candidate-level** | GPT-5.4, DeepSeek R1, Opus (3/6) | STRUCTURAL RISK | **This is the most important finding from the external panel.** Every surviving candidate traces its core F. necrophorum-specific evidence to the KSU/Nagaraja lab (G2-3 epitopes from Xiao/Nagaraja; G2-8 FomA from Kumar/Nagaraja; phage from Schwarz at KSU). The external panel is right: this is not a candidate-level concern to be flagged and moved past. It is a structural portfolio risk. If KSU's foundational claims do not replicate independently, the entire portfolio collapses. Board mandates: the first tranche of investment must include independent replication of the two most critical claims. |

### Board Verdicts After External Panel

| # | Candidate | Reaper Verdict | Board Verdict | Change Reason |
|---|-----------|---------------|---------------|---------------|
| G2-1 | Anti-LktA mAb | WOUNDED | WOUNDED (defer) | Agree with Reaper. Duration problem is real. Repositioned as bridging strategy only. |
| G2-2 | mRNA LktA vaccine | WOUNDED | WOUNDED (defer) | Agree. No bacterial mRNA precedent in cattle. Wait for H5N1 platform data. |
| G2-3 | Epitope subunit vaccine | SURVIVED | **SURVIVED -- LEAD, gated on independent replication** | 5/6 models flag single-lab dependency. Gate: independent lab must replicate Xiao epitope immunogenicity in cattle. |
| G2-4 | LktB secretion inhibitor | KILLED | **WOUNDED** (biologic/vaccine only) | 4/6 models challenge. Small molecule kill is correct. LktB extracellular loops as vaccine antigen survive. Low priority. |
| G2-5/V2 | lktA transcription + LktC acyltransferase | WOUNDED | **SPLIT: V2 ELEVATED (Tier 1 experiment); G2-5 transcription DEFERRED** | LktC acyltransferase assay is highest-information experiment. Transcription approach deferred (10+ year timeline). |
| G2-6 | LktA receptor decoy | WOUNDED | WOUNDED (defer) | Agree. Discovery project. Park as KE#2. |
| G2-7 | Kupffer cell trained immunity | WOUNDED | WOUNDED (defer) | Agree. Pore-formation kill mechanism may bypass trained immunity. Single-lab. |
| G2-8 | Anti-FomA (Factor H + adhesion) | SURVIVED | **SURVIVED -- LEAD component, gated on bovine Factor H binding** | 4/6 models flag human-to-bovine extrapolation. Mandatory gate: demonstrate bovine Factor H binding by bovine liver abscess isolates. |
| G2-9 | Complement enhancement (OMV) | WOUNDED | WOUNDED (defer) | Agree. Research tool, not product. Use to identify defined antigens. |
| G2-10 | Anti-NET evasion (DNase) | KILLED | **WOUNDED** (gated on $2-5K assay) | 3/6 models challenge. Board concurs: cheap assay should gate, not kill preemptively. |
| G1-1 | Anti-hemagglutinin vaccine | KILLED | **WOUNDED** (gated on gene identification) | 3/6 models challenge. Gene ID by mass spec is feasible. Target is not dead, only the current approach. |
| G1-2 | Phage cocktail | SURVIVED | **SURVIVED -- supporting product component** | Weakened by ecological equilibrium argument. Retained because rumen stability is cheaply testable and the product form (in-feed, no AMR) is ideal. |
| G1-3 | Protected butyrate + zinc | KILLED | KILLED | Upheld. Only 2/6 models challenged. |
| G1-4 | Anti-43K OMP vaccine | WOUNDED | Merged with G2-8 (FomA) | Same protein. Evaluate as one program. |
| G1-5 | Hindgut-targeted suppression | WOUNDED | WOUNDED (gated on KE#1) | Agree. Wait for hindgut contribution data. |
| G1-6 | Tannase-resistant tannin | KILLED | KILLED | Upheld. |
| G1-7 | Funduliforme probiotic | WOUNDED | WOUNDED (defer) | Agree. Regulatory barrier. |
| G1-8 | Anti-biofilm (rumen wall) | KILLED | **WOUNDED** (gated on confocal demo) | Opus flags inconsistency: same standard as G2-10. Board concurs. |
| PG-1 | Anti-stellate cell | KILLED | KILLED | Upheld. |
| PG-2 | Abscess biofilm disruption | KILLED | KILLED | Upheld. Physics barrier. |
| PG-3 | Anti-T. pyogenes synergy | WOUNDED | WOUNDED (defer) | Agree. Secondary. Value only as multi-antigen vaccine component. |
| PG-4 | Blood biomarker | SURVIVED | **SURVIVED -- research infrastructure** | Recategorized. Not a product candidate. Value is trial monitoring. |
| COMBO-1 | mAb + phage | WOUNDED | KILLED | mAb duration problem kills this combination. |
| COMBO-2 | mRNA vaccine + anti-adhesion | SURVIVED (conditional) | **KILLED** as originally proposed | Bait-and-switch acknowledged. The real product concept is G2-3 + G2-8 combined. |
| V4 | Calcium chelation | KILLED | KILLED | Upheld. |
| V6 | Downstream signaling blockade | KILLED | KILLED | Upheld. |
| V9 | Hemolysin (PLB) inhibition | WOUNDED | WOUNDED (defer) | Agree. Low bovine activity. |
| V11 | Neuraminidase inhibition | WOUNDED | WOUNDED (defer) | Agree. Marginal impact. |
| V12 | Feedback loop disruption | WOUNDED | WOUNDED -- portfolio insight, not target | Agree. Valuable for predicting non-linear vaccine effects. |
| V13 | Gallium porphyrin | WOUNDED | WOUNDED (10-year defer) | Agree. Elegant biology, no regulatory path. |
| V14 | LuxS/AI-2 quorum sensing | KILLED | KILLED | Upheld despite 3/6 challenge. No AI-2 receptors. |
| V16 | Contact system blockade | WOUNDED | WOUNDED (defer) | Agree. Human data only. No bovine validation. |
| V17 | MMP-13 induction blockade | WOUNDED | WOUNDED (defer) | Agree. Gate 1 target, MMP inhibitor failure history. |

---

## Step 2: Devil's Advocate on Every Survivor

### G2-3: Epitope-Focused Recombinant LktA Subunit Vaccine

**Availability bias check:** This candidate exists because Xiao mapped LktA epitopes in 2009 and recombinant vaccine technology is mature. If Xiao had never published, would anyone independently arrive at this approach? YES -- the Fusogard efficacy data (80% protection in challenge) combined with its field failure (insufficient titer) logically points to "same target, better formulation." This is not compound contamination; it is rational iteration on validated biology. PASSES.

**Alternative explanation:** Could the same disease stage (hepatic immune evasion) be addressed by a completely different approach? YES. An anti-LktA monoclonal antibody (G2-1) addresses the same biology. But the mAb has a fatal duration problem. A small molecule anti-virulence agent (LktC inhibitor, if the acyltransferase hypothesis confirms) would address it differently. The vaccine is not the only approach -- but it is the most commercially mature. PASSES with note: LktC assay could open a superior path.

**"Elanco already knows this" test:** Elanco owned Centurion (which included a leukotoxoid component). They know the target intimately. They discontinued the product because it didn't work well enough on high-grain diets. The question is: would Elanco's internal team believe that ISCOMATRIX adjuvant + epitope focusing solves the firehose problem they already encountered? **This is the hard question.** Elanco's scientists would immediately ask: "What is quantitatively different about this formulation versus what we already tried?" The answer must be: (1) ISCOMATRIX delivers 10-50x higher titers than aluminum hydroxide (Centurion's likely adjuvant), (2) epitope focusing concentrates the immune response on neutralizing regions rather than diluting it across the entire 336 kDa protein, (3) the combination with FomA adds complement sensitization that Centurion lacked. If those three points hold, this is genuinely different from what Elanco tried. CONDITIONAL PASS -- the titer comparison to Centurion/Fusogard is the critical data point.

**Board assessment:** SURVIVES devil's advocate. The strongest challenger is the "Elanco already knows this" test, which demands head-to-head titer comparison against historical Fusogard data. This must be an explicit endpoint in the de-risk experiment.

---

### G2-8: Anti-FomA (Factor H Binding + Adhesion)

**Availability bias check:** FomA exists in the portfolio because Kumar (2013) and Friberg (2008) published on it. Without their work, would biology point here? PARTIALLY. The Tribunal identified complement evasion (Factor H binding) as a secondary virulence mechanism. A target screen would have identified FomA as the Factor H-binding protein. But the dual-mechanism claim (adhesion + complement) is a product of the literature, not first principles. The adhesion function may be redundant with other adhesins. **WARNING: the dual-mechanism narrative may overstate the target's value.** If the adhesion component is redundant (as Reaper argues for G1-1), FomA's value is primarily complement sensitization -- a single mechanism, not two.

**Alternative explanation:** Could complement sensitization be achieved differently? YES. An anti-LPS vaccine or OMV vaccine (G2-9) could opsonize bacteria for complement killing. But FomA has the Neisseria vaccine precedent (Bexsero/Trumenba) -- the regulatory and scientific analogy is stronger than any alternative. PASSES.

**"Elanco already knows this" test:** Factor H binding by F. necrophorum is a relatively niche finding from the Lemierre's syndrome literature. It is unlikely Elanco's livestock vaccine team has evaluated this. The Neisseria-to-Fusobacterium translation is the kind of cross-pathogen insight that specialist companies miss. PASSES -- this is novel to the partner.

**Board assessment:** SURVIVES with a downgrade. The dual-mechanism claim is likely overstated (adhesion is probably redundant). The primary value is complement sensitization via Factor H binding disruption. The Neisseria precedent is real and novel to the partner. But the HUMAN-to-BOVINE extrapolation is unresolved and must be gated.

---

### G1-2: F. necrophorum Phage Cocktail

**Availability bias check:** This candidate exists because Schwarz published obligately lytic F. necrophorum phages in 2024. It is a recently available compound, not an old idea. PASSES.

**Alternative explanation:** Could Gate 1 inoculum reduction be achieved differently? YES. Tylosin already does this (40-70% reduction). Any tylosin replacement that reduces rumen F. necrophorum achieves the same goal. Phage has the advantage of being non-antibiotic and narrow-spectrum. But a tannin-resistant antimicrobial compound, if it worked, could also fill this niche. PASSES with note: phage is the best non-antibiotic Gate 1 approach available today.

**"Elanco already knows this" test:** Elanco OWNS Tylan. They need a tylosin REPLACEMENT, not a competitor. Phage therapy for rumen pathogens is a novel concept that Elanco's feed additive division would not have evaluated seriously. The EU September 2026 antimicrobial deadline creates urgency for non-antibiotic alternatives. PASSES -- this is strategically aligned with Elanco's replacement need.

**Devil's advocate -- the ecological equilibrium problem:** Gemini and GPT-5.4 made a strong argument: these phages were isolated FROM the rumen, proving they already coexist with F. necrophorum at equilibrium. Therapeutic dosing above equilibrium has worked in controlled phage therapy settings, but the rumen is a 60-100L continuous fermentation vat with protozoal predation and rapid bacterial turnover. The probability that phage therapy achieves meaningful and sustained F. necrophorum suppression in this environment is genuinely uncertain. **This is the weakest survivor in the portfolio.** The $15-25K rumen stability experiment is the critical gate, and the bar should be high: >=1 log F. necrophorum reduction sustained for >=48 hours, or this candidate dies.

**Board assessment:** SURVIVES, but as the weakest survivor. The ecological argument is strong. The EU deadline creates urgency for non-antibiotic alternatives that may justify the risk. Gate: rumen stability experiment with a high bar.

---

### PG-4: Blood Biomarker

**Availability bias check:** This exists because Amachawadi (2023) published metabolomic data from abscess material. The concept is obvious. But "obvious" does not mean "easy." PASSES trivially -- any diagnostician would propose this.

**Alternative explanation:** Could trial monitoring be achieved differently? YES. Slaughter-only endpoints are the current standard. Ultrasound has been attempted but is unreliable. A biomarker would be superior if it works, but slaughter data, while delayed, is definitive. The question is whether the time and cost savings from real-time monitoring justify the $10-15K investment and the risk of misleading data from a poor biomarker. PASSES -- even imperfect real-time data is better than waiting 120+ days for slaughter results.

**"Elanco already knows this" test:** Elanco processes data from their Benchmark database (68,000 feedlots). They have extensive slaughter-based abscess grading data. A blood biomarker would be novel to their portfolio and would enhance their Benchmark platform. PASSES.

**Board assessment:** SURVIVES as research infrastructure. The external panel's challenges (capsule prevents leakage, PPV too low, inflammation confounders) are serious and may ultimately kill this. But at $10-15K, the downside is trivial relative to the portfolio. Recategorized: not a product, not a candidate -- a research tool.

---

### V2/LktC: Acyltransferase Assay (elevated from WOUNDED)

**Availability bias check:** This is NOT here because a compound exists. It is here because Vulcan's first-principles decomposition of the LktA lifecycle identified a mechanistic step that has never been tested. The disease map describes LktC's conflicting annotations (histidine kinase vs. acyltransferase). No published study has directly tested LktC's enzymatic function. This is a genuinely novel hypothesis. PASSES strongly -- this is the opposite of compound contamination.

**Alternative explanation:** If LktC is NOT an acyltransferase, does it matter? NO -- the LktC target dies immediately and resources redirect to other Gate 2 approaches. If LktC IS an acyltransferase, this opens a first-in-class drug target with favorable druggability (8,317 A^3 cavity) that has no human medicine competition (LktA is unique to F. necrophorum) and no AMR risk (anti-virulence, not antimicrobial). PASSES.

**"Elanco already knows this" test:** Elanco almost certainly does NOT know this. The acyltransferase hypothesis comes from Vulcan's quarantined analysis of the operon structure, cross-referenced with RTX toxin biology. This is the kind of first-principles molecular biology that a commercial livestock company does not do. This is Agteria's strategic value-add. PASSES strongly.

**Board assessment:** ELEVATED. This is the Board's highest-priority experiment. Binary outcome. Low cost. High information value. Agteria's differentiator.

---

## Step 3: Force-Ranked Portfolio

All surviving + resurrected targets, force-ranked. NO TIES.

| Rank | Target | Type | Why This Rank | Critical Dependency | If This Fails... |
|------|--------|------|---------------|--------------------|--------------------|
| 1 | **V2: LktC acyltransferase assay** | Novel drug target (gating experiment) | Highest information value per dollar ($5-10K). Binary: opens first-in-class anti-virulence drug target or dies. Novel = Agteria's strategic priority. No one else is testing this. | Recombinant LktC must have acyltransferase activity. ONE experiment. | Kill V2 permanently. Redirect to vaccine-only strategy. Nothing else in the portfolio changes. |
| 2 | **G2-3: Epitope subunit vaccine (LktA PL1+PL3+PL4, ISCOMATRIX)** | Lead product (vaccine component 1) | Most technically mature Gate 2 candidate. Cheapest product form ($1-3/dose). Compatible with feedlot processing. Proven adjuvant platform. Addresses the bottleneck directly. | (a) Independent lab replicates Xiao epitope immunogenicity in cattle, (b) neutralizing titers >=4x historical Fusogard at 16 weeks, (c) epitope conservation across 50+ field isolates. | Portfolio loses its primary Gate 2 component. Fall back to mAb bridging (G2-1) or mRNA (G2-2) -- both have higher risk/cost. Or wait for LktC acyltransferase result. |
| 3 | **G2-8: Anti-FomA (complement sensitization)** | Lead product (vaccine component 2) | Dual-mechanism target with clinical vaccine precedent (Bexsero). Combines with G2-3 into a multi-antigen vaccine. Novel to partner. Cross-pathogen translation is Agteria's specialty. | (a) Bovine liver abscess isolates bind bovine Factor H, (b) anti-FomA antibodies restore bovine serum bactericidal activity, (c) no autoimmune cross-reactivity with host porins. | Multi-antigen vaccine becomes single-antigen (LktA only). Fusogard-like efficacy ceiling remains. Portfolio loses the complement sensitization mechanism. |
| 4 | **G1-2: Phage cocktail** | Supporting product (in-feed) | Best non-antibiotic Gate 1 approach. EU deadline creates urgency. Compatible with monensin. Product form is ideal (in-feed, no withdrawal). Fills the tylosin replacement gap that Elanco needs. | (a) Phage survives in rumen >=8h at detectable titers, (b) achieves >=1 log F. necrophorum reduction sustained >=48h, (c) resistance emergence manageable with cocktail rotation. | Portfolio has no Gate 1 component. Vaccine-only strategy depends entirely on titer overcoming the firehose problem -- the exact failure mode of Fusogard. |
| 5 | **PG-4: Blood biomarker** | Research infrastructure | Cheap ($10-15K). Enables better trial design for all other candidates. Transforms a field that relies on slaughter-only endpoints. Low downside. | (a) At least one candidate analyte achieves AUC-ROC >=0.75 for abscess detection, (b) specificity adequate to distinguish from BRD/rumenitis inflammation. | Clinical trials for all other candidates proceed with slaughter-only endpoints (slower, less informative, but not fatal). |
| 6 | **G2-10: Anti-NET evasion (DNase inhibitor)** | Gated experiment | Resurrected from KILLED. $2-5K binary experiment: does F. necrophorum produce extracellular DNase? If yes, NET preservation becomes a supplementary Gate 2 mechanism. | F. necrophorum must have measurable extracellular DNase activity in vitro. | Kill permanently. No further investment. |
| 7 | **G2-4: LktB secretion (biologic/vaccine target)** | Deferred (biologic approach only) | Small molecule approach correctly killed. LktB extracellular loops could serve as vaccine antigen in a future multi-antigen formulation. Low priority because anti-LktA + anti-FomA vaccine already covers Gate 2. | AF3 structure of LktB extracellular loops must reveal immunogenic epitopes. | No loss. G2-3 + G2-8 vaccine proceeds without LktB component. |
| 8 | **G1-1: Anti-hemagglutinin (gene identification)** | Gated experiment | Resurrected from KILLED. Modern proteomics (SDS-PAGE, mass spec) can identify the gene in weeks. If identified, adds a Gate 1 anti-adhesion component to the multi-antigen vaccine. | Mass spec identifies a single protein responsible for hemagglutination activity. | Kill permanently. Rely on FomA for anti-adhesion (which may be redundant anyway). |
| 9 | **G1-8: Anti-biofilm (rumen wall confirmation)** | Gated experiment | Resurrected from KILLED. $5-8K confocal microscopy to confirm or refute rumen wall biofilm. If confirmed, opens anti-biofilm targeting as a Gate 1 component. | Confocal demonstrates structured F. necrophorum community on rumen epithelial explants. | Kill permanently. F. necrophorum rumen wall colonization is planktonic, not biofilm. |
| 10 | **G2-1: Anti-LktA mAb** | Deferred (research tool / bridging only) | Duration problem (21-day half-life vs 120-400 day feeding) kills standalone use. Repositioned as: (a) bridging strategy (mAb at arrival, vaccine builds immunity), or (b) research tool for ex vivo liver perfusion studies to calibrate the neutralizing titer threshold. | Extended-release formulation achieving >=90-day effective concentration, OR confirmed utility as a bridging tool alongside vaccine. | No commercial product impact. Vaccine strategy proceeds independently. Lose the research tool for titer calibration. |
| 11 | **G2-5: lktA transcription suppressor** | Deferred (long-term) | 10+ year research timeline. Five stacked unknowns in series. The regulatory circuitry is completely unmapped after 25 years of research. Correctly deferred to academic collaboration. | Complete regulatory circuit must be mapped before any drug design. | No near-term impact. This is a moonshot that may yield insights in 5-10 years. |
| 12 | **G2-6: LktA receptor decoy** | Deferred (KE#2 discovery project) | Receptor unknown for 24+ years. High payoff if solved (receptor blockade = durable protection independent of toxin strain variation). But 2-5 year timeline minimum. | Receptor must be identified by pull-down + mass spec, and must be specifically blockable without global immunosuppression. | No near-term impact. Vaccine strategy proceeds. |
| 13 | **V13: Gallium porphyrin** | Deferred (10-year moonshot) | Elegant biology (no Fur, no siderophores = unique iron vulnerability). But no veterinary regulatory pathway and no approved gallium antimicrobial in any species after 15+ years of development. | Gallium antimicrobial achieves human regulatory approval (ABATE trial 2027). | No impact. Revisit if regulatory landscape changes. |

---

## Step 4: Board Decision

### A. Priority De-Risk Sequence ("If you can fund only 3 experiments")

**Experiment 1: LktC Acyltransferase Assay ($5-10K, 4-6 weeks)**

- Express recombinant LktC in E. coli
- Incubate with pro-LktA substrate + acyl-ACP donor
- Detect acylated LktA by mass spectrometry (mass shift ~250 Da per acylation site)
- **GO:** Mass shift detected. LktC is an acyltransferase. Immediately commission AlphaFold3 structure prediction and virtual screen against the active site. Elevate to Tier 1 drug target.
- **KILL:** No mass shift. LktC is not an acyltransferase. Kill V2 permanently. The function (chaperone? zinc metalloenzyme?) may be interesting but is not a druggable anti-virulence target.
- **Why first:** This is the highest-information experiment in the portfolio. It resolves whether Agteria has a first-in-class drug target -- the kind of novel discovery that differentiates Agteria from "another vaccine company." It must come first because a positive result would restructure the portfolio: a small-molecule LktC inhibitor + vaccine combination is a more defensible IP position than a vaccine alone.

**Experiment 2: Multi-Antigen Vaccine Immunogenicity Trial ($30-50K, 16-20 weeks)**

- Express PL1+PL3+PL4 fusion protein + recombinant FomA
- Formulate with ISCOMATRIX adjuvant
- Vaccinate 20 cattle (10 vaccine, 10 control) at an independent lab (NOT KSU)
- Measure at 2, 4, 8, 16 weeks:
  - Anti-LktA neutralizing titer (primary endpoint: >=1:256 at 16 weeks)
  - Anti-FomA titer
  - Serum bactericidal activity against F. necrophorum (bovine serum)
  - Bovine Factor H binding by F. necrophorum field isolates (bovine serum, n=20 isolates)
- **GO criteria:**
  - Anti-LktA neutralizing titer >=4x historical Fusogard at 16 weeks
  - Anti-FomA antibodies restore serum bactericidal activity by >=3-fold
  - Bovine isolates bind bovine Factor H (confirming the mechanism translates from human)
- **KILL criteria:**
  - Anti-LktA titers <=Fusogard equivalent (adjuvant improvement not sufficient)
  - Zero bovine Factor H binding by field isolates (FomA mechanism doesn't translate)
- **Why second:** This resolves the two biggest risks to the lead product concept: (1) Can we beat Fusogard's titer with modern antigen/adjuvant design? (2) Does the FomA complement sensitization mechanism work in cattle? Both questions answered in one trial. The requirement for an independent lab addresses the single-lab dependency risk flagged by 5/6 external models.

**Experiment 3: Phage Rumen Stability Trial ($15-25K, 4-6 weeks)**

- Administer phiKSUM + phiBB (obligately lytic, both subspecies) to rumen-fistulated cattle (n=4)
- Continuous in-feed delivery (mimicking commercial use)
- Sample rumen fluid at 0, 1, 4, 8, 24, 48h
- Quantify: (a) viable phage (plaque assay), (b) F. necrophorum concentration (qPCR), (c) rumen microbiome composition (16S)
- **GO:** Phage detectable at >=10^4 PFU/mL at 8h; F. necrophorum >=1 log reduction at 48h
- **KILL:** Phage undetectable by 4h (protease destruction) OR F. necrophorum <0.3 log reduction at 48h (ecological equilibrium maintained)
- **Why third:** This resolves the strongest external challenge to the phage candidate (rumen pharmacokinetics). The bar is deliberately high (1 log reduction at 48h). If phage fails, the portfolio proceeds as vaccine-only. If phage succeeds, the product concept becomes vaccine (injection) + phage (in-feed) -- a genuinely novel combination that addresses both gates.

**Total Priority De-Risk Budget: $50-85K**
**Timeline: 16-20 weeks to all three results**

---

### B. KE#1 Recommendation

**YES. The abscess typing study ($15-25K) should run IN PARALLEL with the Priority De-Risk Sequence.**

**Design:** Collect matched samples (rumen epithelium, colonic epithelium, liver abscess material) from 50 cattle at slaughter. Run qPCR for F. necrophorum subsp. necrophorum, subsp. funduliforme, and Bacteroides spp. on all three tissue types from each animal. Calculate the quantitative contribution of rumen vs. hindgut to hepatic bacterial seeding.

**Why parallel, not sequential:**
- KE#1 does NOT affect the priority experiments. Whether the hindgut contributes 5% or 50%, the LktC assay, vaccine trial, and phage trial proceed the same way.
- But KE#1 DOES affect the second tranche of investment. If hindgut >20%, the vaccine may need Bacteroides antigens (currently absent). If hindgut >40%, the entire rumen-focused Gate 1 strategy (phage) has an intrinsic ceiling.
- Running KE#1 in parallel means the results arrive alongside the priority de-risk results, enabling a fully informed second-tranche decision.

**GO/KILL from KE#1:**
- Hindgut <5%: Deprioritize G1-5 (hindgut suppression). Rumen-focused approach is correct.
- Hindgut 5-20%: Note as a portfolio ceiling. Rumen-focused approach is still primary.
- Hindgut >20%: Flag. The vaccine must consider Bacteroides antigens. Phage cocktail needs hindgut-active phages. G1-5 becomes a real candidate.
- Hindgut >40%: Restructure the portfolio. Rumen-focused Gate 1 approaches (phage) have a hard ceiling. Vaccine must be multi-pathogen.

**Total parallel budget: $15-25K**
**Total first-tranche investment: $65-110K**

---

### C. Targets Requiring Deferral

The following targets are explicitly DEFERRED -- not killed, but not funded in the first tranche. They wait for Priority De-Risk and KE#1 results.

| Target | Deferral Reason | Trigger to Reactivate |
|--------|----------------|----------------------|
| G2-1: Anti-LktA mAb | Duration problem. Only viable as bridging or research tool. | Vaccine trial (Exp 2) shows insufficient titer at 16 weeks. Then mAb bridging becomes necessary. |
| G2-2: mRNA vaccine | No bacterial antigen precedent in cattle. Cold chain. Cost premium. | Elanco-Medgene H5N1 mRNA vaccine data becomes available, showing >=4x titer advantage over protein subunit for cattle. |
| G2-5: lktA transcription | 10+ year research timeline. Unmapped regulatory circuit. | Academic collaboration identifies the regulatory circuit (opportunistic -- do not fund directly). |
| G2-6: Receptor decoy | 2-5 year discovery project. Receptor unknown for 24+ years. | Academic lab identifies the LktA receptor (opportunistic -- consider funding the pull-down/mass-spec experiment for $30-50K if the vaccine trial shows the titer problem is unsolvable). |
| G2-7: Kupffer trained immunity | Single-lab (Adams 2024). Pore-formation kill mechanism may bypass trained immunity. | Adams data replicated independently AND bovine KC + LktA in vitro shows >=2-fold LD50 shift in trained cells. |
| G2-9: Complement OMV vaccine | Undefined 342-protein antigen. Research tool. | FomA (G2-8) vaccine trial fails. Then OMV proteomic screen identifies better complement-targeting antigens. |
| G1-5: Hindgut suppression | Gated on KE#1. Colonic delivery undeveloped. | KE#1 shows >20% hindgut contribution. |
| G1-7: Funduliforme probiotic | No regulatory precedent. HGT risk. | Synthetic biology advances enable safe lktA-deleted funduliforme with clear regulatory path. |
| PG-3: Anti-T. pyogenes synergy | Secondary pathogen (29% of abscesses). | Multi-antigen vaccine trial succeeds. T. pyogenes antigens added to second-generation formulation at near-zero marginal cost. |
| V13: Gallium porphyrin | No veterinary regulatory pathway. 10+ year timeline. | Gallium antimicrobial achieves human regulatory approval. |
| V16: Contact system blockade | Human data only. No bovine validation. Expensive biologic. | Academic collaboration demonstrates contact activation in bovine liver abscess model. |
| V17: MMP-13 blockade | Gate 1 target. MMP inhibitor clinical failure history. | All Gate 2 approaches fail and portfolio must revisit Gate 1 strategies. |

---

## The Product Concept (if Priority De-Risk succeeds)

```
PRODUCT: Multi-antigen protein subunit vaccine
  Components:
    - LktA epitopes PL1+PL3+PL4 (Gate 2 -- leukotoxin neutralization)
    - Recombinant FomA (Gate 2 -- complement sensitization; Gate 1 -- anti-adhesion)
    - ISCOMATRIX adjuvant
  Delivery: Single injection at feedlot arrival processing
  Booster: Optional at reimplant (~60 days)
  Cost target: $2-4/head (competitive with tylosin)

COMBINATION (if phage succeeds):
  + Phage cocktail (phiKSUM + phiBB) in-feed continuous
  Cost: +$1-2/head
  Total: $3-6/head

NOVEL DRUG TARGET (if LktC confirms):
  + LktC acyltransferase inhibitor (oral, daily, in-feed or bolus)
  Timeline: 3-5 years to candidate; 7-10 years to market
  Value: First-in-class anti-virulence agent. Patentable. No AMR.

RESEARCH TOOLS:
  - Blood biomarker (enables real-time trial monitoring)
  - Ex vivo liver perfusion model (calibrates neutralizing titer threshold)
```

**Elanco alignment:**
- Vaccine leverages their biologics manufacturing
- Phage leverages their feed additive distribution (feed mills, premix)
- LktC inhibitor leverages their small molecule R&D capability (if confirmed)
- mAb manufacturing ($130M facility) is ready if the bridging concept is needed
- Non-antibiotic portfolio addresses EU September 2026 deadline
- Replaces Tylan (their own product) with a non-antimicrobial alternative -- self-cannibalization that preempts regulatory disruption

**What Elanco gets that they cannot build internally:**
1. The Gate 2 bottleneck insight (Tribunal-derived) -- reframes their entire liver abscess strategy
2. FomA complement sensitization (cross-pathogen translation from Neisseria) -- their livestock vaccine team would not find this
3. LktC acyltransferase hypothesis (first-principles Vulcan analysis) -- a novel drug target no one has tested
4. The phage cocktail (Schwarz 2024) -- recently published, not yet in any commercial pipeline

---

## Board's Closing Assessment

The portfolio is sound. The target is correct. The product concept is commercially viable. The risks are well-characterized and cheaply de-riskable.

The single biggest risk is NOT any individual candidate failing. It is the **single-lab dependency across the portfolio**. If KSU's foundational F. necrophorum data does not replicate, the entire program is in jeopardy. The Board's most important decision is requiring the vaccine immunogenicity trial (Experiment 2) to be run at an INDEPENDENT lab. This is not just a scientific standard -- it is portfolio-level risk management.

The second biggest risk is the **firehose problem**. Fusogard proved the target is right and the approach can fail. The portfolio's defense against this is three-layered: (1) better adjuvant (ISCOMATRIX), (2) epitope focusing (Xiao epitopes), (3) combination with Gate 1 reduction (phage or FomA anti-adhesion). If all three layers fail to overcome the firehose, the vaccine approach is dead and the portfolio pivots to the LktC inhibitor (if confirmed) or the mAb bridging strategy.

The third biggest risk is timeline. The first tylosin-resistant F. necrophorum was reported in 2024. The EU antimicrobial deadline is September 2026. The feedlot industry needs a tylosin replacement in 2-3 years, not 10. The vaccine and phage combination can potentially reach conditional licensure in 2-3 years. The LktC inhibitor is 7-10 years. The portfolio must lead with the vaccine/phage product while developing LktC as the long-term IP play.

**Recommendation to Daniel:** Fund the Priority De-Risk Sequence ($50-85K) and KE#1 ($15-25K) in parallel. Total first-tranche: $65-110K. Results in 16-20 weeks. Then convene the Board for a second-tranche decision with real data.

---

*Portfolio evaluated. 13 targets ranked. No ties. Three priority experiments defined. KE#1 runs in parallel. The dead are dead. The deferred await triggers. The leads are gated on independent replication. Fund it.*
