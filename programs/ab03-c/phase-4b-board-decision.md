# Phase 4b -- Board Decision: Druggable Targets for Rumen H2 Disposal

**Program:** AB03-C -- Druggable Targets for Rumen H2 Disposal | **Internal Agteria Program** | **Version:** v1
**Agent:** Board | **Date:** 2026-03-30

---

## Executive Summary

Six targets survived or were conditionally approved by Reaper from an initial 24. The external panel (6 frontier models) has now independently reviewed the kill report, and their feedback fundamentally changes the portfolio calculus for three of those six. The panel converged on two critical findings: (1) all three survivors face serious ecosystem-level failure modes that Reaper underweighted, and (2) the hardest problem in this portfolio is not biological -- it is the gap between what the biology demands (enzyme activation) and what medicinal chemistry can deliver (enzyme inhibition).

After integrating external feedback, performing devil's advocate inversions, and force-ranking against the AB03-C scoring rubric, I am left with a portfolio that is honest about its fragility. Every target carries a specific, testable vulnerability. The Board's job is to sequence the de-risk experiments so the portfolio fails fast or validates fast -- not to pretend these are strong development candidates.

**Board outcome:** 3 targets advance to Priority De-Risk. 2 targets deferred pending gate experiments. 1 target killed by the Board (overriding Reaper's survival).

---

## Step 1: External Panel Synthesis

### Panel Composition
- **Gemini 3.1 Pro** -- killed PEPC, PFL-AE, and Rex; found all Reaper kills justified
- **GPT-5.4** -- flagged ecosystem-level failure modes for all three survivors; identified missing kill tests for community compensation and flux-control misassignment
- **Grok 4** -- challenged N-oxide and PFOR survivals; raised thiamine antagonism toxicity for PFOR; argued CODH/ACS and protozoal [FeFe]-Hase were killed too aggressively
- **Claude Opus** -- identified PEPC downstream bottleneck inconsistency with PEPCK; proposed 20-30% ecological compensation discount; flagged resistance evolution for PFOR
- **DeepSeek R1** -- proposed killing all three survivors on various grounds; flagged formate recycling via FHL as a missing kill test for PFOR
- **Qwen 2.5** -- confirmed Reaper's analysis; no novel challenges

### Synthesized Findings

| Finding | Models Agreeing | Verdict Change? | Action Required |
|---------|----------------|-----------------|-----------------|
| **PEPC activator: phosphomycin/MurA separation may be impossible** | Gemini, GPT-5.4, Opus, DeepSeek (4/6) | YES -- PEPC survival is weakened | Reassess as conditional; requires non-antibiotic chemotype demonstration |
| **N-oxide antiprotozoal: refaunation + fiber digestion = commercially fatal** | GPT-5.4, Grok, Opus, DeepSeek (4/6) | PARTIAL -- survival maintained but magnitude downgraded | Refaunation kinetics must be tested in vivo; partial defaunation is the realistic strategy |
| **PFOR inhibitor: broad TPP inhibition risks fermentation collapse + resistance** | GPT-5.4, Grok, Opus, DeepSeek (4/6) | PARTIAL -- survival maintained but risk elevated | PFL backup capacity across key rumen taxa must be validated; resistance evolution test needed |
| **All survivors need 20-30% ecological compensation discount** | Opus (1/6, but logically compelling) | YES -- all magnitude estimates reduced | Applied to all final scores |
| **CODH/ACS kill was premature -- cofactor delivery modality distinct from activation** | GPT-5.4, Grok, Opus, DeepSeek (3-4/6) | NO -- remains killed for rate-limitation uncertainty | Note for future research queue |
| **Missing kill test: community ecological compensation** | GPT-5.4, Opus (2/6) | YES -- applied as systematic discount | 20-30% haircut on all predicted H2 disposal magnitudes |
| **Missing kill test: resistance evolution for inhibitor targets** | Grok, Opus (2/6) | YES -- PFOR inhibitor specifically affected | Added to de-risk requirements |
| **Missing kill test: combination antagonism with 3-NOP** | Opus (1/6) | YES -- all targets must be tested under 3-NOP conditions | Incorporated into de-risk experiment design |
| **Missing kill test: feed interaction / matrix binding** | Opus (1/6) | YES -- especially for TPP analogs and N-oxides | Added to in vivo testing requirements |
| **Phloroglucinol reductase was never proposed as a drug target** | Opus (1/6), GPT-5.4 (Phase 3 panel) | N/A -- Board cannot add targets | Flagged as a gap for Overwatch |
| **Rex regulon likely dominated by LDH/ethanol genes** | Gemini, Grok (2/6) | NO -- Rex was already WOUNDED by Reaper | Confirms Rex should not advance without regulon data |
| **PFL-AE: formate variability across animals = population-level safety risk** | Gemini (1/6) | PARTIAL -- strengthens wound | PFL-AE remains deferred |

### Key Panel Disagreements

The panel split sharply on the three Reaper survivors:

- **N-oxide antiprotozoal:** Gemini and Qwen confirmed survival. GPT-5.4, Grok, and DeepSeek argued it should be killed on commercial/ecological grounds. Opus called it appropriately survived but overranked. **Split: 3 survive / 3 kill or downgrade.**
- **PFOR inhibitor:** Gemini and Qwen confirmed. GPT-5.4, Grok, and DeepSeek raised serious concerns (fermentation collapse, thiamine toxicity, resistance). Opus confirmed but flagged resistance. **Split: 3 survive / 3 wound or kill.**
- **PEPC activator:** Gemini, GPT-5.4, Opus, and DeepSeek argued it should be killed (phosphomycin separation impossible, downstream bottleneck). Grok and Qwen confirmed survival. **Split: 4 kill / 2 survive.**

**Board interpretation:** The PEPC activator's survival is the most challenged by the panel. Four of six models independently concluded the phosphomycin/MurA separation problem is likely fatal. I take this seriously. I am not killing PEPC outright, but I am downgrading its status from "survived" to "conditionally survived -- requires non-antibiotic chemotype before any investment."

---

## Step 2: Devil's Advocate Inversions

### Target 1: N-Oxide Selective Antiprotozoal (V12) -- Reaper Score 63

**The case FOR (Reaper's position):**
Protozoa become net H2 liabilities under RHAS. 19 N-oxide compounds tested in rumen simulation. Cytotoxic modality (not activation). Eukaryote-prokaryote selectivity basis exists. At R0 = 1.0, even 10-15% H2 reduction could collapse RHAS.

**The case AGAINST (devil's advocate):**
- **Availability bias:** This target is in the portfolio because a specific chemical class (N-oxides) was tested in one paper. Without that paper, would anyone independently propose "kill protozoa" as a drug target for H2 disposal? Defaunation has been studied for 40+ years with inconsistent results. The N-oxide dataset creates the illusion of novelty around an old idea.
- **Alternative explanation:** The same H2 reduction goal (eliminate protozoal contribution) could be achieved by disrupting the protozoa-methanogen endosymbiosis rather than killing the protozoa themselves. Monensin already partially defaunates and is commercially available. A fresh team might propose a hydrogenosome-targeted intervention rather than a blunt antiprotozoal.
- **The "why isn't the field doing this?" test:** The defaunation literature goes back decades. Multiple chemical defaunation agents have been tried (detergents, saponins, ionophores). None have become standard of care. The reasons are well-documented: fiber digestion impairment, rapid refaunation, inconsistent productivity outcomes. The N-oxide chemotype may or may not be different. Single-lab data.
- **Compound contamination:** The portfolio's #1-ranked target exists because one MDPI 2019 paper tested 19 compounds. Remove that paper and the target vanishes. This is the definition of compound contamination -- the target is ranked high because a compound exists, not because the biology independently points here.

**Board assessment:** The compound contamination concern is real but mitigated by the fact that defaunation biology is well-established independently of the N-oxide paper. The N-oxide data provides a lead scaffold, not the entire biological rationale. Survival is maintained but magnitude estimates are discounted for ecological compensation (refaunation, bacterial expansion into freed niche). **The target's true value is as a rapid, low-cost in vitro validation of the source-reduction strategy, not as a near-term development candidate.**

---

### Target 2: PFOR Inhibitor (V11) -- Reaper Score 62

**The case FOR:**
Inhibitor modality (tractable). Known lead compound (oxythiamine). TPP-[4Fe-4S] selectivity handle. Redirects electron flow from H2 to formate at the fundamental pyruvate branch point. Vulcan-original -- quarantined reasoning produced this independently of the literature.

**The case AGAINST:**
- **Availability bias:** Oxythiamine exists as a commercially available TPP analog. Is PFOR in the portfolio because the biology points to the pyruvate branch point, or because oxythiamine happens to be purchasable? Vulcan's analysis was first-principles, which argues against compound contamination. But the tractability of the proposal is entirely dependent on the oxythiamine scaffold. Without it, PFOR inhibition is a theoretical concept with no medicinal chemistry starting point.
- **Alternative explanation:** The same electron-flow redirection could be achieved by activating PFL (Forge's approach, Target T3/PFL-AE) rather than inhibiting PFOR. The Reaper wounded PFL-AE but did not kill it. A fresh team might prefer the "enhance the alternative" approach over "block the primary pathway," especially given the fermentation-collapse risk of PFOR inhibition.
- **The "Zoetis already knows this" test:** N/A -- internal program, no partner. But: would any experienced rumen biochemist independently propose inhibiting PFOR in the rumen? The answer is "probably not" -- PFOR is a core central metabolic enzyme in almost all rumen anaerobes. Inhibiting it is analogous to inhibiting glycolysis. The boldness of this proposal is either its greatest strength (genuine novelty) or its greatest weakness (obviously dangerous and therefore never attempted).
- **Grok's thiamine antagonism flag:** Oxythiamine depletes host thiamine, causing polioencephalomalacia in cattle. This is a documented veterinary toxicity. If the PFOR inhibitor is a TPP analog with any systemic absorption, host thiamine antagonism is a real risk. This was not in Reaper's analysis.

**Board assessment:** The Grok thiamine antagonism flag is a material new finding. Oxythiamine specifically, and TPP analogs generally, are known to cause thiamine-deficiency syndromes when absorbed systemically. The PFOR inhibitor must be rumen-restricted (no systemic absorption) or use a chemotype that does not antagonize host thiamine. This elevates the delivery/formulation challenge but does not kill the target. The biological logic remains the strongest in the portfolio -- redirecting electron flow at the pyruvate branch point is the most mechanistically elegant solution to H2 overproduction.

**Survival confirmed, but with an elevated delivery/formulation constraint.**

---

### Target 3: PEPC Activator (V5) -- Reaper Score 58

**The case FOR:**
Demonstrated activator (phosphomycin). No mammalian ortholog. Addresses the upstream rate-limiting step of propionogenesis. Bacterial-specific enzyme.

**The case AGAINST:**
- **Availability bias:** This target is entirely dependent on the phosphomycin precedent. Remove phosphomycin from the analysis, and PEPC activation has no lead, no chemical matter, and no more evidence than any of the other "activator needed" targets that Reaper killed. The target's survival is 100% dependent on one molecule -- and that molecule is an antibiotic that cannot be used as-is.
- **Alternative explanation:** The same propionogenesis enhancement could be achieved by PEPCK activation (which has a mapped allosteric site) or by fumarate reductase enhancement. PEPC was elevated over PEPCK by Reaper because phosphomycin exists -- but phosphomycin's antibiotic activity makes it unusable, which undermines the very advantage that elevated PEPC over PEPCK.
- **Opus's downstream bottleneck point:** Reaper killed PEPCK for "downstream bottleneck shift" risk -- the same logic applies identically to PEPC. Activating the carboxylation step only helps if malate dehydrogenase, fumarase, and fumarate reductase can handle the increased flux. Reaper did not apply this logic consistently.
- **Four of six external models recommended killing PEPC.** This is the strongest external signal against any surviving target.

**Board assessment:** The Opus point about downstream bottleneck inconsistency between PEPCK and PEPC is a genuine logical error in Reaper's analysis. PEPC and PEPCK occupy the same pathway node. If the downstream bottleneck concern kills PEPCK, it should equally wound PEPC. Combined with 4/6 models recommending a kill, I am downgrading PEPC from "survived" to "deferred -- requires demonstration of a non-antibiotic PEPC activator chemotype AND evidence that downstream pathway capacity is not limiting." This is effectively a kill unless new chemical matter emerges.

**PEPC downgraded to DEFERRED.**

---

### Target 4: PFL-AE Activator (T3) -- Reaper Score 55

**The case FOR:**
Demonstrated 3.7x activation by oxamate. Novel application. NADH-bypass mechanism (reduces NADH production rather than increasing disposal).

**The case AGAINST:**
- **Gemini's population-level safety point:** The formate-consuming capacity of the rumen varies between animals and diets. A drug that produces a formate flood in some animals (causing toxicity) and works perfectly in others is not a viable livestock therapeutic.
- **Single-lab dependency:** The oxamate activation data is from one PNAS 2023 publication.
- **The phloroglucinol data:** Phloroglucinol achieved 93% formate reduction in vivo -- suggesting the rumen CAN process formate. But phloroglucinol itself was the electron acceptor for formate reduction. Without a parallel formate sink, PFL-AE activation produces formate that may simply accumulate.

**Board assessment:** The formate-accumulation risk is real but testable. The 3.7x activation precedent is genuine and valuable -- this is one of only two targets in the portfolio where a synthetic small molecule activator has been demonstrated. The population-level safety concern (variable formate-consuming capacity across animals) is a commercial risk, not a biological impossibility.

**PFL-AE remains WOUNDED/DEFERRED. Advances only if formate accumulation is shown to be manageable in vitro.**

---

### Target 5: Rex Antagonist (T2) -- Reaper Score 52

**The case FOR:**
Most druggable non-GPCR target. Crystal structures. Defined conformational switch. Bacteria-specific.

**The case AGAINST:**
- **Gemini's prior probability argument:** The most likely Rex regulon composition in rumen Firmicutes is LDH + alcohol dehydrogenase genes, not propionogenesis genes. The biological prior probability of the desired regulon composition is low (~20-30%).
- **Grok's resistance concern:** Rex is a global regulator. Antagonism imposes strong selection for mutations in the Rex binding site. Resistance could emerge within weeks in the rumen's massive, rapidly dividing population.

**Board assessment:** Rex is the most structurally druggable target in the portfolio but addresses a biological question that is fundamentally unanswered. The regulon characterization experiment (RNA-seq of rex-knockout) is a $15-25K experiment that takes 3-6 months. It must precede any medicinal chemistry investment.

**Rex remains DEFERRED. Advances only with favorable regulon characterization.**

---

### Target 6: A1AO-ATP Synthase Inhibitor (T13) -- Reaper Score 52

**The case FOR:**
Most drug-discovery-advanced target (validated HTS, lead compounds). Archaea-specific selectivity.

**The case AGAINST:**
- **This is not an H2 disposal target.** It deepens methanogenesis inhibition. Under the AB03-C constraint, this target only has value as a combination component with proven H2 disposal agents.
- **Reaper correctly identified:** deeper methanogenesis inhibition = more H2 accumulation. This target makes the core problem worse unless paired with H2 disposal.

**Board assessment:** The A1AO inhibitor has the best drug-discovery infrastructure in the portfolio but solves the wrong problem. It is a methane-reduction tool, not an H2-disposal tool. In the AB03-C context, it is strictly a combination partner for the H2-disposal targets. It should not consume any de-risk budget until H2 disposal targets are validated.

**A1AO inhibitor: KILLED by Board for AB03-C scope. Transferred to the methane-inhibition program as a standalone candidate.**

---

## Step 3: Final Likelihood of Success Scores

Scores are adjusted from Reaper's values to incorporate:
- External panel feedback (4-component breakdown recalibrated)
- 20% ecological compensation discount on all magnitude estimates (Opus recommendation)
- Devil's advocate findings
- Thiamine antagonism risk for PFOR (Grok finding)
- Downstream bottleneck consistency correction for PEPC (Opus finding)

### 1. PFOR Inhibitor (V11)

| Component | Score | Rationale |
|-----------|-------|-----------|
| Target Validation | 17/25 | PFOR is central to H2-producing pyruvate metabolism. Branch point to PFL is real. But species-variable PFL backup is unresolved. |
| Druggability | 16/25 | TPP-binding site validated. Oxythiamine is a known lead. TPP-[4Fe-4S] interface provides selectivity over host. |
| Rumen Feasibility | 12/25 | Down from 15 -- thiamine antagonism risk (Grok) means rumen-restricted formulation is mandatory. Feed matrix binding of TPP analogs is untested. |
| Magnitude of Effect | 10/25 | Down from 13 -- 20% ecological compensation discount applied. Realistic range: 10-25% H2 reduction (down from 20-40%). |
| **TOTAL** | **55/100** | **Development candidate -- conditional** |

**De-risk cost:** $50-80K (in vitro rumen incubation with oxythiamine under 3-NOP; PFL expression survey across 10 key rumen taxa; 14-day continuous culture resistance test)
**Timeline:** 6-9 months
**IP assessment:** Novel application of TPP analog pharmacology to rumen H2 metabolism. Patentable as method-of-use. Freedom to operate is clear -- oxythiamine is a tool compound, not a commercial product. A novel TPP analog with PFOR selectivity and rumen restriction would have strong patent claims. The TPP-[4Fe-4S] selectivity interface is a genuine structural novelty.
**Synergy with Rhein/Menadione:** PFOR inhibition is mechanistically complementary to redox mediators. Rhein/Menadione provide an electron sink (accepting electrons from NADH/ferredoxin); PFOR inhibition reduces electron generation at source. Combined, they attack the H2 problem from both ends. A PFOR inhibitor could reduce the required Rhein/Menadione dose, improving the economics of the feed additive approach.

---

### 2. N-Oxide Selective Antiprotozoal (V12)

| Component | Score | Rationale |
|-----------|-------|-----------|
| Target Validation | 16/25 | Down from 18 -- defaunation effects are real but commercially inconsistent over 40 years. Compound contamination concern partially mitigated. |
| Druggability | 17/25 | Down from 18 -- single-lab N-oxide data. Cytotoxic modality is tractable. 19 compounds provide SAR starting point. |
| Rumen Feasibility | 15/25 | Down from 18 -- chronic dosing required due to refaunation. Therapeutic window for partial defaunation is narrow and untested. |
| Magnitude of Effect | 7/25 | Down from 9 -- 20% ecological compensation + refaunation discount. Realistic range: 5-15% H2 reduction (down from 9-25%). At R0=1.0, even 5-15% may be meaningful, but the lower bound is marginal. |
| **TOTAL** | **55/100** | **Development candidate -- conditional** |

**De-risk cost:** $30-50K (replicate N-oxide rumen simulation with fiber digestion endpoint; test refaunation kinetics over 28 days in continuous culture)
**Timeline:** 4-6 months
**IP assessment:** N-oxide antiprotozoals for rumen H2 management are novel. Method-of-use patents are strong. Composition-of-matter patents depend on structural novelty of the lead compound vs. published N-oxides. Freedom to operate requires confirming the MDPI 2019 compounds are not already patented.
**Synergy with Rhein/Menadione:** Antiprotozoal activity is mechanistically independent of redox mediation. An N-oxide antiprotozoal eliminates a H2 source that Rhein/Menadione cannot address (protozoal H2 is produced intracellularly, inaccessible to dissolved redox mediators). The combination directly addresses the "protected channel" problem. Protozoa also prey on bacteria -- partial defaunation may increase the bacterial population available for Rhein/Menadione to act on.

---

### 3. PFL-AE Activator (T3) -- DEFERRED

| Component | Score | Rationale |
|-----------|-------|-----------|
| Target Validation | 16/25 | Down from 17 -- single-lab activation data (PNAS 2023). Application to rumen is novel and unvalidated. |
| Druggability | 16/25 | Down from 17 -- oxamate is a real activator but rapidly metabolized in rumen. Need stable analog. |
| Rumen Feasibility | 8/25 | Down from 10 -- population-level formate safety concern (Gemini). Lead compound instability. |
| Magnitude of Effect | 8/25 | Down from 11 -- 20% ecological discount + formate bottleneck uncertainty. |
| **TOTAL** | **48/100** | **Research candidate -- deferred** |

**Gate experiment:** In vitro rumen incubation with stable oxamate analog under 3-NOP. If formate accumulates >15 mM and persists >6 hours, target is killed. Cost: $15-25K. Timeline: 3-4 months.
**IP assessment:** Novel application. Strong composition-of-matter potential for rumen-stable PFL-AE activator analogs.
**Synergy with Rhein/Menadione:** PFL-AE activation and redox mediation address different branches of the same problem. PFL-AE reduces NADH generation (source reduction); Rhein/Menadione provides an electron acceptor for NADH that IS generated (sink enhancement). Mechanistically orthogonal and potentially synergistic.

---

### 4. PEPC Activator (V5) -- DEFERRED

| Component | Score | Rationale |
|-----------|-------|-----------|
| Target Validation | 18/25 | PEPC is the gateway to propionogenesis. Well-characterized. No mammalian ortholog. |
| Druggability | 10/25 | Down from 15 -- phosphomycin is unusable as-is (antibiotic activity). 4/6 external models deemed the MurA separation challenge likely fatal. No non-antibiotic PEPC activator exists. |
| Rumen Feasibility | 8/25 | Down from 10 -- phosphomycin scaffold faces antibiotic confound + rapid bacterial uptake via GlpT/UhpT transporters. |
| Magnitude of Effect | 8/25 | Down from 13 -- downstream bottleneck correction (Opus); 20% ecological discount. |
| **TOTAL** | **44/100** | **Research candidate -- deferred** |

**Gate experiment:** Two-stage: (1) Phosphomycin dose-response for PEPC activation vs. bacterial viability in rumen fluid ($10-15K, 2 months). (2) If therapeutic window exists, design PEPC-selective analog lacking MurA activity -- this is a $200-400K medicinal chemistry campaign requiring PEPC crystal structure from a rumen organism.
**IP assessment:** Strong if a PEPC-selective chemotype can be developed. No mammalian PEPC means clean selectivity IP story. But the medicinal chemistry risk is high -- 4/6 models doubt feasibility.
**Synergy with Rhein/Menadione:** PEPC activation increases the propionogenesis H2 sink. Rhein/Menadione provides electrons to drive fumarate reduction. These are directly synergistic -- Rhein/Menadione acts as an electron shuttle feeding into the pathway that PEPC activation expands. This is the tightest mechanistic fit of any combination.

---

### 5. Rex Antagonist (T2) -- DEFERRED

| Component | Score | Rationale |
|-----------|-------|-----------|
| Target Validation | 10/25 | Down from 12 -- regulon composition in rumen Firmicutes is completely unknown. Biological prior probability of favorable composition is ~20-30%. |
| Druggability | 20/25 | Unchanged -- structurally the most druggable target in the portfolio. |
| Rumen Feasibility | 12/25 | Down from 14 -- broad-spectrum Rex antagonism across all Firmicutes; resistance evolution risk. |
| Magnitude of Effect | 4/25 | Down from 6 -- if regulon is dominated by LDH/ethanol genes (most likely), effect is zero or negative. |
| **TOTAL** | **46/100** | **Research candidate -- deferred** |

**Gate experiment:** RNA-seq of rex-knockout vs. wild-type in R. albus or a rumen Clostridium under elevated NADH/NAD+. Cost: $15-25K. Timeline: 4-6 months. This is a binary gate: if the regulon includes propionogenesis genes, Rex becomes a top-3 target. If it is dominated by LDH/ethanol, Rex is killed.
**IP assessment:** Excellent if regulon is favorable. Rex antagonists are a novel target class with no prior art. Clean bacteria-specific selectivity.
**Synergy with Rhein/Menadione:** If Rex derepresses propionogenesis genes, it amplifies the pathway that Rhein/Menadione feeds into. The combination would be: Rhein/Menadione provides electrons + Rex antagonist upregulates the enzymes that use those electrons.

---

## Step 4: Strategic Force-Ranking

| Rank | Target | Board Score | Why This Rank | Critical Dependency | If This Fails... |
|------|--------|-------------|---------------|--------------------|--------------------|
| **1** | **PFOR Inhibitor (V11)** | 55 | Highest-leverage mechanism (redirects electron flow at the pyruvate branch point). Inhibitor modality (not activation). Known lead compound. Vulcan-original -- novel insight from quarantined reasoning. | PFL backup capacity must be present in >50% of rumen taxa. Rumen-restricted formulation required to avoid thiamine antagonism. | Source-reduction strategy loses its primary target. N-oxide antiprotozoal becomes the sole source-reduction approach. Sink-enhancement targets must carry the entire portfolio. |
| **2** | **N-Oxide Antiprotozoal (V12)** | 55 | Independent mechanism (H2 source elimination). Rumen simulation data provides an immediate starting point. Addresses the "protected channel" problem (protozoal H2 inaccessible to dissolved interventions). | N-oxide data must replicate with fiber digestion endpoint. Refaunation must be manageable with continuous dosing at sub-toxic levels. | The protozoal H2 "leak" remains unaddressed. Portfolio loses 5-15% potential H2 reduction. Acceptable if PFOR inhibition compensates. |
| **3** | **PFL-AE Activator (T3)** | 48 | Demonstrated activator precedent (3.7x by oxamate). Novel NADH-bypass mechanism. Mechanistically complementary to PFOR inhibition (both shift pyruvate metabolism away from H2). | Formate accumulation must be manageable in vitro. Rumen-stable oxamate analog must be designable. | Loss of the only validated enzyme activator in the portfolio. The "NADH bypass" concept survives conceptually even if PFL-AE is killed. |
| **4** | **PEPC Activator (V5)** | 44 | Best host-selectivity profile (no mammalian PEPC). Addresses the upstream rate-limiting step of propionogenesis. Tightest mechanistic synergy with Rhein/Menadione. | Non-antibiotic PEPC activator chemotype must exist. Downstream pathway capacity must not be limiting. 4/6 models doubt feasibility. | Loss of the propionogenesis-amplification approach via enzyme activation. Feed additive fumarate supplementation becomes the only way to increase propionogenesis throughput. |
| **5** | **Rex Antagonist (T2)** | 46 | Most druggable target in the portfolio (crystal structures, conformational switch, fold-class precedent). Binary gate experiment is cheap ($15-25K) and decisive. | Rex regulon must include propionogenesis genes in rumen Firmicutes (~20-30% prior probability). | Loss of the only transcription-factor-based approach. The only target where druggability exceeds biology. Not a major portfolio loss unless the regulon proves favorable. |

**Rationale for PFOR over N-oxide at #1:**

Both score 55/100. I rank PFOR higher because:
1. **Mechanism quality:** PFOR inhibition addresses the fundamental electron-flow branch point. N-oxide antiprotozoals address a secondary H2 source (9-37% of total).
2. **Novelty and IP:** PFOR inhibition for rumen H2 management is genuinely novel (Vulcan-original). Defaunation is a 40-year-old concept with a new chemotype.
3. **Combination logic:** PFOR inhibition directly synergizes with Rhein/Menadione (reduces electron generation + provides electron acceptor). N-oxide synergy is additive but not mechanistically linked.
4. **Failure consequences:** If PFOR fails, we lose the highest-leverage single mechanism. If N-oxide fails, we lose a modest supplementary approach.

---

## Step 5: Board Decision

### A. The Priority De-Risk Sequence

**If Agteria can fund only 3 experiments, these 3 and in this order:**

**Experiment 1: PFOR Branch-Point Validation** ($25-35K, 3-4 months)
- In vitro rumen incubation with oxythiamine (50, 100, 200 uM) under 3-NOP (50% CH4 inhibition).
- Measure: dissolved H2, formate, total VFA, individual VFA (acetate, propionate, butyrate), NDF digestibility, bacterial viability.
- Include 14-day continuous culture arm to assess resistance emergence.
- **GO if:** >10% H2 reduction AND total VFA maintained within 90% of control AND no resistance emergence in 14 days.
- **KILL if:** Total VFA drops >15% OR resistance emerges within 14 days OR H2 reduction <5%.
- **Information value:** Resolves three critical uncertainties simultaneously (H2 reduction magnitude, fermentation safety, resistance risk). Most information per dollar of any experiment in the portfolio.

**Experiment 2: N-Oxide Antiprotozoal Replication + Fiber Endpoint** ($20-30K, 3-4 months)
- Replicate the MDPI 2019 N-oxide rumen simulation with top 3 compounds.
- Add: NDF digestibility, VFA production, bacterial counts, protozoal counts over 28 days.
- Include partial defaunation arm (target 50-70% protozoal reduction, not elimination).
- **GO if:** >10% H2 reduction at 50-70% defaunation AND NDF digestibility maintained within 90% of control AND protozoal counts remain suppressed through day 28 (no refaunation in closed system).
- **KILL if:** NDF digestibility drops >15% OR protozoal H2 contribution at partial defaunation is <5% OR protozoal counts recover within 14 days.
- **Information value:** Addresses the single-lab dependency (most critical portfolio fragility) and resolves the fiber digestion vs. H2 reduction trade-off.

**Experiment 3: Rex Regulon Characterization** ($15-25K, 4-6 months)
- RNA-seq of rex-knockout vs. wild-type in R. albus 7 (or Clostridium ruminicola if genetic tools are available) under elevated NADH/NAD+ conditions.
- Characterize full regulon: which genes are derepressed, and what metabolic pathways they belong to.
- **GO if:** Regulon includes frdABCD (fumarate reductase), fum (fumarase), mdh (malate dehydrogenase), or other propionogenesis/alternative-electron-disposal genes.
- **KILL if:** Regulon is dominated by ldh (lactate dehydrogenase) and adhE/adhB (ethanol dehydrogenase) genes.
- **Information value:** Binary gate for the most druggable non-GPCR target in the portfolio. At $15-25K, this is the cheapest experiment with the largest potential portfolio restructuring impact. If positive, Rex jumps from #5 to #1 in the force ranking.

**Total Priority De-Risk Budget:** $60-90K
**Total Timeline:** 4-6 months (experiments 1 and 2 can run in parallel; experiment 3 is independent)

### B. The KE#1 Recommendation

AB03-A/B identified a KE#1 RUSITEC experiment to resolve fundamental unknowns about H2 metabolism. For AB03-C specifically:

**The PFOR branch-point validation (Experiment 1) IS the KE#1 for the drug-target layer.** It tests the single most transformative hypothesis in the portfolio: can electron flow be redirected from H2 to formate by inhibiting PFOR? If yes, the drug-target layer has a viable lead mechanism. If no, the portfolio must rely on sink-enhancement targets (PEPC, FrdABCD) where the activation modality challenge is severe.

**Recommendation:** Run Experiment 1 BEFORE committing to Experiments 2 and 3. If PFOR inhibition fails catastrophically (VFA collapse, rapid resistance), the portfolio's strategic logic changes: source-reduction approaches are weakened, and the priority shifts to sink-enhancement -- which means investing in the wounded activator targets (FrdABCD HTS, Rnf AF3 prediction) despite their known challenges.

However, Experiments 2 and 3 are cheap enough ($35-55K combined) that they should run in parallel with Experiment 1 unless budget is severely constrained. The information value of all three is high and they are independent.

### C. Targets Requiring Deferral

| Target | Status | Gate to Re-entry | Gate Cost | Gate Timeline |
|--------|--------|------------------|-----------|---------------|
| **PFL-AE activator (T3)** | DEFERRED | In vitro formate accumulation test under 3-NOP + stable oxamate analog | $15-25K | 3-4 months |
| **PEPC activator (V5)** | DEFERRED | (1) Phosphomycin dose-response for PEPC vs. MurA, (2) Non-antibiotic PEPC activator chemotype | $10-15K for gate 1; $200-400K for gate 2 | 2 months for gate 1; 12-18 months for gate 2 |
| **Rex antagonist (T2)** | DEFERRED (but in Priority De-Risk as Experiment 3) | Rex regulon RNA-seq | $15-25K | 4-6 months |
| **A1AO-ATP synthase inhibitor (T13)** | KILLED (for AB03-C) | N/A -- transferred to methane-inhibition program | -- | -- |
| **Fumarate reductase activator (T4/V4)** | DEFERRED (WOUNDED) | HTS of >10K compounds against purified QFR for activator hits | $80-120K | 6-9 months |
| **Rnf complex activator (T1/V10)** | DEFERRED (WOUNDED) | AF3 structure prediction of P. ruminicola RnfC; druggable pocket identification | $5-10K computational; $50-80K if wet lab follows | 2-3 months computational |

---

## The Phloroglucinol Gap

Multiple external panel models (Claude Opus, GPT-5.4) flagged that phloroglucinol -- the most empirically validated small molecule for H2 disposal (50.6% H2 reduction, 93% formate reduction in vivo) -- was never reverse-engineered to identify its target reductase as a druggable candidate. The Board notes this as the most significant gap in the AB03-C pipeline. The phloroglucinol reductase is a real enzyme in rumen bacteria that demonstrably reduces both H2 and formate. If this reductase could be identified, characterized, and targeted for activation (or if the rumen organisms harboring it could be selectively enriched), it would be the most evidence-backed drug target in the entire program.

**Board recommendation to Overwatch:** Commission Forge to formally propose the phloroglucinol reductase as a drug target for AB03-C v2, with full molecular identification, structural characterization, and druggability assessment.

---

## Portfolio Logic Summary

The AB03-C drug-target portfolio sits alongside and behind the Rhein/Menadione feed additive approach. The relationship is:

1. **Rhein/Menadione (AB03 feed additive layer):** Provides a near-term, stoichiometric electron sink. Works NOW. Limited by dose economics and the gap between stoichiometric H2 acceptance and the total H2 burden.

2. **PFOR inhibitor + N-oxide antiprotozoal (AB03-C drug-target layer):** Reduces H2 GENERATION at source. Works on the OTHER side of the equation -- instead of adding more electron acceptors, it reduces the electron flux that needs accepting. Mechanistically complementary to Rhein/Menadione.

3. **PEPC/PFL-AE/Rex (deferred AB03-C targets):** Increases the enzymatic THROUGHPUT of H2-consuming pathways. If validated, these amplify the effect of Rhein/Menadione by increasing the rate at which donated electrons are processed.

The drug-target layer does NOT replace the feed additive layer. It extends it. The strategic vision is a combination product: Rhein/Menadione (electron sink) + PFOR inhibitor (source reduction) + antiprotozoal (source reduction) -- addressing H2 accumulation from both directions simultaneously.

---

## Predictions for the Prediction Log

### Prediction B-1: PFOR Inhibition Will Be the Highest-Information Experiment in the Portfolio
**Prediction:** The PFOR branch-point validation (Experiment 1) will produce the largest portfolio-restructuring decision of any single experiment. Either it validates the entire source-reduction strategy (GO) or it kills the highest-ranked target and forces a pivot to sink-enhancement (KILL).
**Test:** Compare the number of portfolio decisions changed by Experiment 1 vs. Experiments 2 and 3.
**If TRUE:** The Board's prioritization was correct.
**If FALSE:** One of the other experiments produced a bigger surprise -- likely the Rex regulon (Experiment 3) being unexpectedly favorable.

### Prediction B-2: Ecological Compensation Will Reduce All In Vitro Effect Sizes by 15-30%
**Prediction:** When any AB03-C intervention (PFOR inhibitor, N-oxide, PEPC activator) is tested in mixed rumen fluid (not pure culture), the observed H2 reduction will be 15-30% smaller than predicted from mechanism alone, due to community-level compensatory shifts in H2-producing populations.
**Test:** Compare H2 reduction in pure-culture vs. mixed-rumen-fluid for oxythiamine and N-oxide compounds.
**If TRUE:** The 20% ecological discount applied by the Board was appropriate. All single-target effect magnitude estimates should be further reduced.
**If FALSE:** The rumen community does not compensate as rapidly as expected. Effect sizes are closer to mechanism-level predictions. This would be optimistic for the portfolio.

### Prediction B-3: The Rex Regulon Will Be Dominated by LDH, Not Propionogenesis Genes
**Prediction:** RNA-seq of rex-knockout in R. albus will show >3-fold upregulation of ldh (lactate dehydrogenase) and adhE (alcohol dehydrogenase), but <1.5-fold change in frdABCD, fum, or mdh (propionogenesis genes). Rex antagonism would increase lactate production, not propionate.
**Test:** Experiment 3 (Rex regulon characterization).
**If TRUE:** Rex is killed. The most druggable target in the portfolio is biologically useless for RHAS.
**If FALSE (regulon includes propionogenesis):** Rex immediately becomes the #1 drug target in the portfolio -- a druggable transcription factor that upregulates the most valuable H2 sink. This would be the most portfolio-transforming outcome of any single experiment.

### Prediction B-4: Phloroglucinol Reductase Will Be the Best Drug Target in AB03-C v2
**Prediction:** When the phloroglucinol reductase is identified and characterized from rumen bacteria, it will score >70/100 on the AB03-C rubric because it combines (a) the strongest empirical validation of any target (50.6% H2 reduction in vivo), (b) a likely inhibitor/activator pocket on a soluble reductase, and (c) a direct mechanism for both H2 and formate disposal.
**Test:** Formal Forge proposal for phloroglucinol reductase in AB03-C v2.
**If TRUE:** The entire AB03-C pipeline should have started with reverse-engineering phloroglucinol.
**If FALSE:** The phloroglucinol mechanism is too distributed or the reductase is not druggable.

---

## For Anvil

The Board delivers to Anvil:

1. **Force-ranked target list** with final scores and 4-component breakdowns
2. **Three Priority De-Risk Experiments** with GO/KILL criteria and budgets
3. **Three deferred targets** with gate experiments and re-entry conditions
4. **One Board kill** (A1AO-ATP synthase inhibitor removed from AB03-C scope)
5. **One gap flag** (phloroglucinol reductase) for Overwatch to action

Anvil should note: this is a fragile portfolio. Every target has a testable fatal flaw. The Priority De-Risk Experiments are designed to fail fast. The 70% coverage test does NOT apply to AB03-C (replaced by Likelihood of Success scoring per program-context.md). Anvil's job is to build the de-risk cascade, not to inflate coverage estimates.

---

## Web Review Prompt

Daniel: the Board recommends submitting the kill report + this Board decision to web-based models for deeper analysis. Specific questions for web models:

**For Claude Web:** Fact-check the phloroglucinol reductase claim -- is there a characterized enzyme responsible for phloroglucinol reduction in rumen bacteria? What is it? Is it druggable?

**For GPT-5.4 Web:** Review the PFOR inhibitor thesis. Is there published evidence on PFL expression or activity in R. albus, R. flavefaciens, and Fibrobacter succinogenes? What fraction of major rumen cellulolytic bacteria have functional PFL as a backup pathway?

**For Gemini Extended Thinking:** Model the community-level ecological compensation for PFOR inhibition. If 50% of rumen PFOR activity is inhibited, what happens to the remaining community? Does PFL activity increase? Does a different H2-producing guild expand? What is the steady-state H2 reduction after community re-equilibration?
