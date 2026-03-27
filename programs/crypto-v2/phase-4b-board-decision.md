# Phase 4b -- Board Decision: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill | **Version:** v2
**Agent:** Board | **Date:** 2026-03-27

---

## Step 1: External Panel Synthesis

Six frontier models (GPT-5.4, Grok 4, Gemini 3.1 Pro, Claude Opus, DeepSeek R1, Qwen 2.5) independently challenged Reaper's kill report. I synthesized their findings below, weighted by corroboration count.

### 1.1 Synthesized Feedback Table

| Finding | Models Agreeing | Verdict Change? | Action Required |
|---------|----------------|-----------------|-----------------|
| **BKI/CpCDPK1 (#2) resistance risk is underweighted.** Single gatekeeper mutation confers full resistance; 8x/12h replication generates variants at scale. Sustained-release creates perfect sub-lethal selection pressure at tail end. | 4/6 (GPT-5.4, Grok 4, Gemini, Qwen) | NO -- but demotes from unconstrained #1. **BKI must be mandated as combination-only, never monotherapy.** | Add resistance constraint to BKI ranking. BKI's value is as a combination backbone, not a standalone. |
| **CpPDE1 (#7) has single-lab dependency.** All genetic validation, compound efficacy, and mouse data from one 2024 publication. Reaper flagged this for MMV665917 but gave CpPDE1 a pass. Inconsistent standard. | 5/6 (GPT-5.4, Grok 4, Claude, DeepSeek, Qwen) | YES -- **demote from SURVIVED to WOUNDED.** | CpPDE1 must demonstrate independent replication of mouse efficacy before it can anchor a de-risk sequence. Still high-ceiling, but not first-dollar material without replication. |
| **Combination candidates (#25, #26, #27) survived on speculative synergy, not data.** Combining wounded components does not create evidence. Operational complexity in neonatal calves is a real barrier. | 4/6 (GPT-5.4, DeepSeek, Claude partial, Grok partial) | YES -- **#25, #26, #27 are portfolio architecture, not standalone candidates.** | Remove from force-ranked individual targets. Retain as strategic combination frameworks to be assembled from individually validated components. |
| **Enhanced ORT (#22) is supportive care, not a drug target.** Strong ex vivo data but no in vivo calf trial. Agent framing as "#1 priority experiment" is inappropriate for a drug discovery portfolio. | 3/6 (GPT-5.4, Claude, Qwen) | PARTIAL -- correctly categorized as supportive care, but the trial remains the highest-value near-term experiment. | Reclassify as supportive care optimization. Keep as first experiment but separate from drug target ranking. |
| **Meloxicam (#16) may mask symptoms without modifying disease.** NSAID renal risk in dehydrated calves under field conditions is high. | 4/6 (GPT-5.4, Grok, Claude, DeepSeek) | NO -- renal risk is manageable with hydration support (already standard of care). But the symptom-masking concern is valid. | Require oocyst shedding endpoint in any meloxicam trial. If shedding is unchanged, meloxicam is supportive care only (still valuable, but not disease-modifying). |
| **V6 (Dual CpGT1+GT2) lacks any compound, any structure, any in vitro data.** Surviving on an elegant genetic argument and a selectivity hypothesis. No medicinal chemistry path exists. | 4/6 (GPT-5.4, Claude, DeepSeek, Grok) | YES -- **demote from SURVIVED to WOUNDED.** | This is a 5-10 year target. No first-dollar allocation until a pan-CpGT inhibitor or structural data exists. |
| **V9 (CpROM1) is too speculative.** GP900 may be lubrication, not adhesion. The Crypto-specific functional data is thin. Inference from Toxoplasma is unreliable for invasion biology. | 3/6 (GPT-5.4, Claude, DeepSeek) | YES -- **demote from SURVIVED to WOUNDED.** | One falsifiable experiment (rhomboid inhibitor + invasion assay) decides this. Cheap, but not yet done. |
| **V13 (CpFAS1) VLCFA-oocyst wall connection is inferred, not established.** Host lipid scavenging may compensate. Cerulenin is a dirty tool compound. | 4/6 (GPT-5.4, Claude, DeepSeek, Grok partial) | YES -- **demote from SURVIVED to WOUNDED (stricter criteria).** | Requires demonstration that CpFAS1 products are incorporated into oocyst walls before this can be a portfolio asset. |
| **Candidate #17 (rBoIFN-gamma + COX-2) kill reasoning is biologically flawed** -- agent conflated "IL-12-stimulated IFN-gamma failed" with "IFN-gamma is irrelevant." IFN-gamma IS essential (KO mice are highly susceptible). Kill stands on commercial grounds ($200/calf), not biology. | 4/6 (Grok, Gemini, Claude, Qwen) | NO -- kill stands, but biological reasoning corrected. | Correct the narrative: IFN-gamma is essential for clearance. The rBoIL-12 failure does NOT prove IFN-gamma is irrelevant. This matters for beta-glucan and CpG-ODN strategies that work partly through IFN-gamma. |
| **Candidate #21 (Environmental decontamination) kill is too absolute.** Dose-independence applies to severity once infected, but environmental interventions can reduce probability of infection, age at first infection, and cohort attack rate. | 2/6 (GPT-5.4, Grok partial) | NO -- kill stands for Agteria's portfolio (not a drug target, no IP). But Cargill should pursue this operationally in parallel. | Note for Cargill: environmental management is complementary but outside Agteria's scope. |
| **BKI sustained-release bolus formulation for neonatal calves has no precedent.** Neonates have abomasum, not functional rumen. Standard cattle boluses are for adult rumen. This is a major engineering unknown. | 3/6 (Claude, DeepSeek, Grok) | NO verdict change, but adds a critical dependency. | BKI formulation feasibility becomes a KE#1-adjacent question. Must be addressed before committing to BKI as portfolio anchor. |
| **Niche access illusion: HCT-8 and mouse efficacy may overstate access in neonatal calf ileum** with mucus, milk, transit, and epithelial turnover. Applies across all anti-parasitic targets. | 2/6 (GPT-5.4, Claude) | NO individual verdict change. Portfolio-level risk. | This is the argument for KE#1 (luminal vs. systemic drug access study). Resolves the access question for the entire portfolio simultaneously. |

### 1.2 Verdict Adjustments from External Panel

| Candidate | Reaper Verdict | Board Verdict | Reason |
|-----------|---------------|---------------|--------|
| #7 CpPDE1 | SURVIVED | **WOUNDED** | 5/6 models flag single-lab dependency. Inconsistent standard vs. MMV665917. |
| #25 Triple combo | SURVIVED | **Reclassified as combination architecture** | Not an independent candidate. Value emerges only after components validate individually. |
| #26 ORT + MMV665917 | SURVIVED | **Reclassified as combination architecture** | Same logic. MMV665917 is itself wounded. |
| #27 Vaccine + BKI + glucan | SURVIVED | **Reclassified as combination architecture** | Same logic. Each component has unresolved dependencies. |
| V6 Dual CpGT1+GT2 | SURVIVED | **WOUNDED** | No compound, no structure, no in vitro data. 5-10 year target. |
| V9 CpROM1 | SURVIVED (barely) | **WOUNDED** | GP900 role uncertain. One experiment needed. |
| V13 CpFAS1 | SURVIVED (barely) | **WOUNDED** | VLCFA-wall connection inferred. Needs biochemical proof. |
| #2 BKI/CpCDPK1 | SURVIVED | **SURVIVED -- but constrained: combination-only** | Resistance risk from 4/6 models. Never deploy as monotherapy. |
| #16 Meloxicam | SURVIVED | **SURVIVED -- reclassified as supportive care** | Not disease-modifying unless oocyst shedding endpoint met. |
| #22 Enhanced ORT | SURVIVED | **SURVIVED -- reclassified as supportive care** | Highest-value near-term experiment, but not a drug target. |

---

## Step 2: Devil's Advocate Inversion

For every candidate that survived Reaper (original 10) plus those I am retaining after adjustment, I argue the opposite position.

### #2 BKI/CpCDPK1 -- Compound Contamination Test

**The case against:** BKI is in this portfolio because BKI compounds happen to exist, not because CpCDPK1 is independently the best target. The entire BKI program exists because of a structural accident -- CpCDPK1 has a glycine gatekeeper that no mammalian kinase shares, making it uniquely targetable by "bumped" kinase inhibitors. Remove the compound and ask: "Is CpCDPK1 the highest-leverage kinase in C. parvum?" The answer is ambiguous. CDPK1 is involved in invasion AND replication, but it is not the sole essential kinase. The conditional knockdown shows essentiality, but essentiality does not equal highest leverage. CpPDE1 (egress blockade, breaking the amplification cycle) and Myb-M (sexual commitment, breaking autoinfection) both address the disease at higher-leverage points.

**The "Cargill already knows this" test:** BKI development has been publicly discussed in the veterinary parasitology literature since 2016. The Van Voorhis lab has presented at conferences. Zoetis and Elanco have had a decade to evaluate CpCDPK1 as a target. If they have not pursued it, the likely reason is the hERG problem and COGS uncertainty -- barriers Agteria also faces. The IP landscape is cluttered.

**Board assessment:** BKI is correctly in the portfolio but should NOT be ranked #1. It is the safest bet (most data) but not the highest-ceiling bet. The glycine gatekeeper that makes it druggable also makes resistance trivially achievable via a single mutation. It is a backbone for combinations, not a standalone anchor.

### #7 CpPDE1 -- Compound Contamination Test

**The case against:** CpPDE1 is in this portfolio because pyrazolopyrimidine hPDE-V inhibitors happened to cross-react with the parasite enzyme. The discovery was serendipitous. The "egress blockade" narrative is elegant but inferred -- the 2024 paper shows reduced parasite burden in mice, not direct visualization of egress blockade. The compound could be working through off-target effects or host PDE inhibition. The CRISPR V900A mutant confirms target engagement but not the downstream mechanism.

**The "fresh team" test:** Would a team starting from scratch, with no knowledge of pyrazolopyrimidines, independently identify CpPDE1 as a priority target? Possibly -- PDE1 is the sole PDE expressed during asexual stages, and cGMP signaling is essential for egress in related apicomplexa. But the "sole PDE" claim is wrong: Surveyor identified 3 PDEs, creating redundancy risk. A fresh team might prioritize CpPKG (the downstream effector) over CpPDE1 (one of multiple cGMP modulators).

**Board assessment:** CpPDE1 has the highest mechanistic novelty in the portfolio. Egress blockade simultaneously stops amplification, autoinfection, and transmission from a single target. But single-lab dependency is real and disqualifying for first-dollar allocation. Demote to second-tier pending independent replication.

### #16 Meloxicam (COX-2 inhibitor)

**The case against:** Meloxicam is in this portfolio because it is available, approved, and cheap -- not because the biology points to COX-2 as a critical node in cryptosporidiosis. The anti-secretory effect is real (ex vivo) but may simply mask symptoms. A calf that looks less sick but sheds the same number of oocysts, recovers at the same rate, and gains the same (or less) weight is not a treatment success. The immunomodulation hypothesis (PGE2 explains rBoIL-12 failure) is entirely unproven. If the anti-secretory effect masks clinical signs, farmers may delay supportive care interventions, paradoxically worsening outcomes.

**The "Cargill already knows this" test:** Every large-animal veterinarian knows about meloxicam for pain and inflammation in calves. If COX-2 inhibition meaningfully improved crypto outcomes, it would have been tested by now. The absence of a single published randomized controlled trial of meloxicam in crypto-infected calves, despite decades of availability, suggests the veterinary community does not expect meaningful benefit.

**Board assessment:** The absence of existing data is diagnostic -- either nobody thought to test it (plausible, given the neglected Blikslager data) or practitioners tested it informally and saw no benefit (unknowable). The trial is cheap enough ($10-15K) that the information value exceeds the cost regardless. Retain, but reclassify as supportive care.

### #22 Enhanced ORT (Glutamine + Meloxicam)

**The case against:** This is not a drug. It is a supportive care protocol. Including it in a drug discovery portfolio alongside novel molecular targets conflates two entirely different activities. Glutamine is a food-grade amino acid. Meloxicam is an approved NSAID. Neither has any anti-parasitic activity. Neither generates IP. Neither is licensable. If Agteria presents this to Cargill as a portfolio outcome, Cargill's response will be: "You spent $50K to tell us to add glutamine to ORT?"

**The "fresh team" test:** A fresh team would immediately identify the Blikslager 2001 data as a missed clinical translation opportunity. They would also immediately recognize it as a veterinary clinical trial, not a drug discovery program. The right entity to run this trial is a veterinary school or Cargill's own clinical team, not Agteria.

**Board assessment:** The trial should absolutely happen -- it is the highest expected-value experiment in the portfolio per dollar spent. But it should be framed as "baseline improvement to standard of care" that Agteria recommends Cargill test, not as an Agteria drug target. If meloxicam shows disease-modifying activity (reduced shedding, not just reduced diarrhea), the PGE2 immunomodulation hypothesis is confirmed and that DOES generate strategic value for the portfolio.

### V1 Myb-M (Forced Activation / Death Switch)

**The case against:** This is a genetic discovery, not a drug target. The distance from "conditional genetic ablation in a lab strain" to "small molecule that forces terminal differentiation in field isolates" is approximately the distance from the Moon to Mars. Transcription factor activators are the hardest class of drug to develop. Delivery to a nuclear target inside a parasite inside an extracytoplasmic niche requires traversing four biological barriers. The entire Myb-M story rests on one lab (Striepen). If forced activation proves pharmacologically impossible (the most likely outcome), the entire investment is lost.

**The "fresh team" test:** A fresh team with access to the 2024 Myb-M paper would be electrified by the biology. They would also immediately recognize that "genetic proof in a lab" and "druggable target" are separated by a chasm that most academic discoveries never cross. A pharmaceutical company would file this under "interesting biology, watch the space" and move on.

**Board assessment:** Myb-M is the highest-ceiling target in the entire portfolio. If druggable, it is curative. But "if druggable" is doing enormous work in that sentence. The AF3 structure prediction and binding partner identification are the minimum investment to determine if a druggable pocket exists. This is worth $10-15K to answer. It is NOT worth building a program around until that answer exists.

---

## Step 3: Adjusted Survivor List After Board Review

After external panel synthesis and devil's advocate, the surviving portfolio is:

**SURVIVED as drug targets (4):**
1. BKI/CpCDPK1 (#2) -- combination-only constraint
2. CpPDE1 (#7) -- demoted to wounded by panel; retains highest mechanistic novelty
3. MMV665917 (#1) -- wounded by Reaper, but unique therapeutic efficacy; single-lab risk
4. Myb-M/V1 -- wounded by Reaper, but highest ceiling if druggable

**SURVIVED as supportive care (2):**
5. Enhanced ORT (#22) -- highest near-term value, not a drug target
6. Meloxicam (#16) -- included in ORT trial, not independent drug target

**WOUNDED with clear graduation criteria (12):**
- CpPDE1 (#7), CpIMPDH (#6), VHH nanobody (#9), beta-glucan (#15), CpG-ODN (#18), Bovicrypt (#8), paromomycin reformulated (#3), bile salt sequestrant (#14), BH3 mimetic (#13), Myb-M (V1), AP2-F (V2), CpFAS1 (V13)

**Reclassified as combination architecture (3):**
- #25, #26, #27 -- frameworks, not candidates

**Demoted from SURVIVED to WOUNDED (4):**
- CpPDE1 (#7), V6, V9, V13

---

## Step 4: Strategic Force-Ranking

I am force-ranking ALL candidates that survived or are wounded with realistic graduation paths. No ties. The ranking reflects Agteria's strategic position: a drug discovery company proposing novel targets to Cargill for licensing. Supportive care recommendations are ranked separately.

### 4.1 Drug Target Force-Ranking

| Rank | Target | Why This Rank | Critical Dependency | If This Fails... |
|------|--------|---------------|--------------------|--------------------|
| **1** | **CpPDE1 egress blockade (#7)** | Highest-leverage mechanism in the portfolio. Egress blockade simultaneously stops amplification, autoinfection, and transmission from a single parasite-specific target. 2024 genetic validation + mouse efficacy. Novel mechanism = clean IP. If the single-lab dependency resolves, this is the portfolio anchor. | Independent replication of 2024 mouse data. Calf proof-of-concept. Luminal formulation to eliminate hPDE-V cross-reactivity. | Lose the only candidate that simultaneously addresses amplification + autoinfection + transmission. Portfolio falls back to BKI combinations (weaker). |
| **2** | **BKI/CpCDPK1 (#2) -- combination backbone** | Best-validated target in Crypto. Crystal structures enable rational optimization. Parasite-specific (no mammalian CDPKs). Calf POC exists (BKI-1553). The fecal-concentration-drives-efficacy insight transforms the development path to luminal delivery. **But: combination-only.** Monotherapy resistance is near-certain. Best paired with CpPDE1 or a future sex-stage inhibitor. | Sustained-release luminal formulation for neonatal calves (no precedent). hERG resolution via non-absorbable formulation. COGS < $10/calf. | Lose the most mature target. Portfolio is left with less-validated options. But BKI failure would not be catastrophic if CpPDE1 or Myb-M succeed. |
| **3** | **Myb-M forced activation / death switch (V1)** | Highest-ceiling target. If druggable, it is curative -- breaks autoinfection, blocks transmission, renders existing parasites terminally differentiated. No analog in the Crypto literature. Biology is extraordinary (2024 Striepen lab). **But: highest-risk.** Transcription factor activator in an extracytoplasmic parasite is pharmacologically unprecedented. Worth the AF3 structure prediction to determine if a druggable pocket exists. | AF3 structure. Binding partner identification. Evidence of a druggable interaction surface. | Lose the only potentially curative single-target approach. But portfolio retains BKI + CpPDE1 combinations which are adequate (not curative, but disease-modifying). |
| **4** | **MMV665917 (#1)** | Only compound with THERAPEUTIC (post-symptom) calf efficacy. Parasiticidal, not parasitistatic. 94% shedding reduction is unprecedented. **But: single-lab dependency, unknown target, 8-year stall, high dose (22 mg/kg), hERG concern.** The unknown target prevents rational optimization. If the calf data replicates independently, this jumps to #1. If it does not, it is dead. | Independent replication of calf efficacy (non-Huston/Tzipori lab). Target identification via resistance selection + WGS. COGS analysis. | Lose the only therapeutic option. Portfolio is entirely prophylactic. Not catastrophic (prophylaxis is the right strategy per bottleneck analysis), but therapeutic rescue capacity is gone. |
| **5** | **CpIMPDH inhibitors (#6)** | Cleanest target validation in the portfolio: crystal structure, nanomolar selective inhibitors, bacterial-origin enzyme (inherent selectivity). Independently identified by both Forge and Vulcan. **But: decade-long silence on in vivo efficacy is a loud warning.** The delivery-to-efficacy gap has not been closed despite having everything else in place. | Non-absorbable luminal formulation tested in mouse model with demonstrated efficacy. If luminal delivery fails in mice, KILLED. | Lose a clean, patentable target with established selectivity. Painful but portfolio has alternatives (BKI, CpPDE1). |
| **6** | **VHH nanobody cocktail (#9)** | Most promising biologic approach. Protease-resistant (unlike mAbs). Cheap to produce (yeast-expressible). Multi-target (GP40 + CSL + TRAP-C1) addresses invasion redundancy. Proven platform for oral delivery to neonatal calf gut (anti-rotavirus precedent). **But: zero anti-Crypto nanobodies exist.** The path from zero to product is 3-5 years minimum. | Generate anti-CSL nanobodies (most conserved target). Demonstrate >90% in vitro sporozoite neutralization. Demonstrate >7-day luminal persistence via mucoadhesive formulation. | Lose the best passive immunization approach. Bovicrypt (2-3 day coverage only) is the fallback, which is inadequate for the 14-day window. |
| **7** | **Beta-glucan trained immunity (#15)** | Cheapest immune acceleration candidate. Real 2025 calf data (96 calves, 2 studies). Addresses the timing gap from the immune side. **But: observed protection was days 31-60, NOT days 0-14.** The timing mismatch with the crypto vulnerability window is the critical question. Even partial acceleration (2-day advance in innate engagement) would reduce parasite burden at immune contact by ~100-fold. | Crypto-specific calf challenge: beta-glucan at birth, C. parvum challenge day 2, measure oocyst shedding + ileal IFN-gamma days 3-14. | Lose the cheapest path to immune timing gap closure. Fall back on CpG-ODN (#18) or accept that immune acceleration is not feasible in the neonatal window. |
| **8** | **AP2-F female gamete blockade (V2)** | Plant-type transcription factor absent from mammals = built-in selectivity. Blocks oocyst wall assembly. If it blocks BOTH thick- and thin-walled oocysts, it is curative. **But: thin-walled oocyst question is unanswered. Single lab (Striepen). Transcription factor druggability problem.** | Conditional ablation in immunocompromised mice to determine if autoinfection persists. If thin-walled oocysts are unaffected, demote to transmission-blocking only. | Lose a potentially curative target with inherent selectivity. But Myb-M (V1) addresses the same domain (sexual reproduction) from a different angle. |
| **9** | **CpG-ODN TLR9 agonist (#18)** | Cheap, available, safe in calves. Produces IFN-gamma within hours (faster than beta-glucan's trained immunity). **But: rBoIL-12 proved that IFN-gamma production alone does not protect.** The PGE2 hypothesis is the only differentiating argument. Transient effect (24-48h) requires repeated dosing. | Calf challenge: CpG at birth + crypto challenge + meloxicam arm. Measure ileal cytokines days 3-5. | Lose a fast-acting innate stimulant. Not catastrophic if beta-glucan (#15) works. |
| **10** | **CpFAS1 megasynthase (V13)** | Unique 8,243-aa Type I FAS with inherent selectivity (substrate specificity differs from mammalian FASN). If VLCFAs are essential for oocyst wall, this blocks both transmission and autoinfection. **But: VLCFA role is inferred. Single lab. Cerulenin is a dirty tool.** | Demonstrate CpFAS1 product incorporation into oocyst walls. Identify selective inhibitor (not cerulenin). | Lose a unique target with inherent selectivity. Portfolio retains Myb-M and AP2-F for the sexual reproduction / oocyst domain. |
| **11** | **Bovicrypt maternal vaccine (#8)** | Best commercial path (single injection in dam). Provides 2-3 days of colostral anti-GP40 antibody coverage. **But: GP60 subtype variability, 2-3 day duration vs. 14-day window, field trial significance was marginal.** Only valuable as Day 0-3 layer in a combination strategy. | Cross-subtype neutralization data (IIa vs. IId). US regulatory pathway. | Lose the passive immunization layer for days 0-3. Not catastrophic -- VHH nanobodies (#9) can fill this role if developed. |
| **12** | **Dual CpGT1+GT2 glucose transport blockade (V6)** | Elegant genetics (glucose-6-phosphate selectivity handle, dual-target resistance barrier). **But: no compound, no structure, no in vitro data.** This is a 5-10 year target identification and medicinal chemistry program. | Structural characterization of at least one CpGT. Demonstration that a G6P mimetic blocks transport in vitro. CRISPR double-KO confirming dual-blockade lethality. | Lose a target with an interesting selectivity handle. Not catastrophic given alternatives. |

### 4.2 Supportive Care Ranking (Separate Track)

| Rank | Intervention | Action | Cost |
|------|-------------|--------|------|
| **S1** | Enhanced ORT: glutamine + meloxicam (#22) | Randomized calf trial. 4-arm factorial. Endpoints: diarrhea severity, weight day 21, mortality, oocyst shedding. | $10-15K |
| **S2** | Meloxicam alone (#16) | Included as arm in ORT trial above. If shedding changes, promotes to disease-modifying. | Included in S1 |

---

## Step 5: Board Decision

### A. Priority De-Risk Sequence (Top 3 Experiments)

If Agteria can fund only 3 experiments, these are the 3 that generate the most strategic information per dollar:

**Experiment 1: Enhanced ORT Calf Trial ($10-15K)**
- **Design:** Randomized controlled, naturally infected calves. 4 arms: (A) Standard ORT, (B) ORT + glutamine 0.5g/kg/day, (C) ORT + meloxicam 0.5 mg/kg SID, (D) ORT + glutamine + meloxicam. N=10/arm (40 calves total).
- **Endpoints:** Diarrhea severity score (primary), weight at day 21, mortality, oocyst shedding (critical secondary -- if shedding changes, the PGE2 immunomodulation hypothesis is confirmed).
- **Why first:** Cheapest experiment. All components available now. No regulatory barriers. Even if the rest of the portfolio fails, this improves standard of care. Oocyst shedding endpoint also tests Prediction 7 (PGE2 explains rBoIL-12 paradox), which has implications for beta-glucan, CpG-ODN, and the entire immune acceleration arm of the portfolio.
- **Timeline:** Can begin immediately. Results in 8-12 weeks.
- **GO signal:** >40% reduction in diarrhea severity in the glutamine + meloxicam arm vs. standard ORT. ANY significant oocyst shedding reduction elevates meloxicam from supportive care to disease-modifying.
- **KILL signal:** No significant difference in any arm.

**Experiment 2: CpPDE1 Independent Replication + Calf Bridge ($30-40K)**
- **Design:** Two parts. Part A: Contract an independent lab (not the 2024 Nat Comms authors) to replicate pyrazolopyrimidine efficacy in IFN-gamma-KO mice. Part B (contingent on Part A): Test lead compound in neonatal calf challenge model (prophylactic, from birth).
- **Endpoints:** Part A: Oocyst reduction in mice (must replicate >1 log10 reduction). Part B: Oocyst shedding, diarrhea severity, weight in calves.
- **Why second:** CpPDE1 is the highest-leverage single target in the portfolio (egress blockade = amplification + autoinfection + transmission disruption). But the single-lab dependency is disqualifying for first-dollar allocation per 5/6 external models. Independent replication resolves this. If replicated, CpPDE1 immediately becomes the portfolio anchor.
- **Timeline:** Part A: 12-16 weeks. Part B: additional 12-16 weeks.
- **GO signal:** Independent replication of >1 log10 oocyst reduction in mice. Calf efficacy with >50% shedding reduction.
- **KILL signal:** Independent lab cannot replicate mouse efficacy. KILLED.

**Experiment 3: Myb-M Structure + Druggability Assessment ($10-15K)**
- **Design:** AF3 structure prediction of Myb-M protein. Identification of binding partners via co-immunoprecipitation from transgenic parasites (collaborate with Striepen lab). Computational assessment of druggable pockets on Myb-M and its interaction surfaces.
- **Endpoints:** Is there a druggable pocket on Myb-M or an interaction surface that can be disrupted by a small molecule? Are there binding partners more druggable than Myb-M itself?
- **Why third:** Highest-ceiling target in the portfolio. If druggable, it is curative. The AF3 + binding partner study is the minimum investment to determine whether "if druggable" is plausible or fantasy. At $10-15K, the information value is enormous relative to cost.
- **Timeline:** AF3 structure: 2-4 weeks. Binding partner identification: 8-12 weeks (requires collaboration).
- **GO signal:** Identifiable binding pocket with <500 Da fragment-like molecule docking scores. OR: a binding partner (co-activator, co-repressor) with an enzymatic activity or defined binding pocket.
- **KILL signal:** Myb-M is a structurally disordered protein with no identifiable pocket or interaction surface. Or: binding partners are equally undruggable. Myb-M becomes a genetic tool, not a drug target.

**Total cost for top 3 experiments: $50-70K. Timeline: 6-8 months for full de-risk data.**

### B. KE#1 Recommendation

**KE#1: Luminal vs. Systemic Drug Access to the Extracytoplasmic Niche ($10-15K)**

This experiment should run IN PARALLEL with the Priority De-Risk Sequence, not before it.

**Rationale:** The entire anti-parasitic portfolio -- BKIs, CpPDE1, CpIMPDH, MMV665917 -- depends on one unanswered question: does the drug reach the parasite primarily from the gut lumen (through the parasitophorous vacuole membrane) or from the systemic circulation (through the host cell)? The answer restructures every formulation decision in the portfolio.

**Design:** Administer a model compound (e.g., BKI-1553, which has both fecal and plasma PK data in calves) to C. parvum-infected neonatal calves in two formulations: (A) absorbable oral (systemic + fecal levels), (B) non-absorbable oral (fecal only, zero systemic). Compare oocyst shedding and diarrhea endpoints.

**Predicted outcomes and portfolio consequences:**
- If non-absorbable formulation is equally or more effective: **Luminal access confirmed.** The entire portfolio shifts to luminal-delivery formulation. hERG, systemic toxicity, and host selectivity concerns are eliminated for BKIs, CpPDE1, and CpIMPDH. Formulation becomes the rate-limiting step.
- If absorbable formulation is significantly more effective: **Systemic access required.** hERG optimization for BKIs becomes mandatory. CpIMPDH luminal-delivery hypothesis is KILLED. Portfolio shifts toward compounds with systemic bioavailability and acceptable safety.
- If neither works well: **Niche access is the fundamental barrier.** The entire small-molecule portfolio is in trouble. Pivot toward biologics (nanobodies, which can bind from the luminal side to surface proteins) and host-directed approaches (immune acceleration).

**Why parallel, not preceding:** The Priority De-Risk experiments (#1-3 above) generate critical information regardless of KE#1's outcome. Enhanced ORT does not depend on drug access. CpPDE1 replication in mice uses the same formulation as the original study. Myb-M druggability is structural, not PK-dependent. But KE#1's result will determine HOW to formulate the drug targets that graduate from de-risk.

### C. Targets Requiring Deferral

The following targets are explicitly DEFERRED -- not killed, but not funded in the first tranche. They wait until the Priority De-Risk experiments and KE#1 produce GO/KILL signals.

| Target | Deferral Reason | Reactivation Trigger |
|--------|----------------|---------------------|
| **CpIMPDH (#6)** | Decade-long in vivo silence despite excellent in vitro data. Wait for KE#1 (luminal access) result. | KE#1 confirms luminal access. Non-absorbable formulation tested in mice. |
| **VHH nanobody cocktail (#9)** | 3-5 year development timeline. No anti-Crypto nanobodies exist. High ceiling but long path. | CpPDE1 or BKI calf trials show the small-molecule approach has limits, increasing value of biologics. |
| **Beta-glucan (#15)** | Timing mismatch (days 31-60 protection, not days 0-14) is the critical unknown. Cheap to test but lower priority than anti-parasitic de-risk. | Enhanced ORT trial confirms PGE2 immunomodulation (oocyst shedding changes with meloxicam). This validates the immune acceleration hypothesis and makes beta-glucan timing more urgent to resolve. |
| **CpG-ODN (#18)** | Same logic as beta-glucan. Transient IFN-gamma (24-48h) may not bridge the 14-day window. | Beta-glucan trial shows immune acceleration is feasible in the neonatal window. |
| **AP2-F (V2)** | Thin-walled oocyst question must be answered before AP2-F is worth pursuing as a treatment target. Single lab. | Myb-M GO signal (druggable pocket found) activates the sexual reproduction target domain, making AP2-F worth parallel investigation. |
| **Dual CpGT1+GT2 (V6)** | No compound, no structure. Pure target identification stage. | Structural characterization of either transporter. |
| **CpFAS1 (V13)** | VLCFA role inferred. Single lab. | Biochemical demonstration that CpFAS1 products are in oocyst walls. |
| **CpROM1 (V9)** | GP900 role uncertain. | Rhomboid inhibitor + invasion assay shows >70% invasion reduction. |
| **Bovicrypt (#8)** | Marginal field data. GP60 subtype variability. Only useful as combination adjunct. | BKI sustained-release formulation exists and needs a Day 0-3 immunological complement. |
| **Paromomycin reformulated (#3)** | Therapeutic window may be insurmountable. | Minimum effective luminal concentration determined at <50 mg/kg (allowing practical bolus). |
| **Bile salt sequestrant (#14)** | Fat malabsorption risk. | In vitro excystation dose-response shows steep curve (50% bile salt reduction achieves >87% excystation inhibition). |
| **BH3 mimetic (#13)** | Novel but high host toxicity risk. | In vitro selectivity assay shows >10x infected vs. uninfected cell killing. |
| **CDPK5 (V3)** | Too weak as standalone (40-60% effect). Only valuable in combination. | Myb-M or AP2-F GO signal activates the sexual reproduction combination strategy. |
| **Glycogen phosphorylase (V4)** | Host selectivity uncertain. Monotherapy is sub-threshold. | CpGP vs. bovine GP structural comparison reveals exploitable selectivity pocket. |
| **CpABC1 (V7)** | Essentiality not demonstrated. Cargo unknown. | CRISPR ablation shows essentiality. |
| **CpOSBP (#12)** | Gene ID unresolved. Not validated. | Gene ID resolved + CRISPR essentiality demonstrated. |
| **Wnt activator (#24)** | Post-infection recovery. Lower priority than acute disease intervention. | Enhanced ORT trial shows persistent weight deficit despite diarrhea improvement, motivating recovery-phase intervention. |
| **Anti-GP40 mAb (#5)** | Subsumed into VHH nanobody program (#9). | N/A -- pursued through #9 only. |
| **Gal/GalNAc polymer (#10)** | Low-ceiling due to multi-mechanism invasion. | In vitro shows >80% invasion inhibition (unlikely but possible). |

---

## Step 6: Portfolio Summary and Recommendation to Anvil

### What Anvil Receives

**Tier 1 -- Immediate Action (first $70K, first 6 months):**
1. Enhanced ORT calf trial ($10-15K) -- supportive care baseline
2. CpPDE1 independent replication + calf bridge ($30-40K) -- highest-leverage drug target
3. Myb-M structure + druggability assessment ($10-15K) -- highest-ceiling target
4. KE#1: luminal vs. systemic access study ($10-15K) -- portfolio-restructuring experiment

**Tier 2 -- Conditional on Tier 1 Results (next $50-100K):**
- If CpPDE1 replicates: calf efficacy trial + luminal formulation development
- If Myb-M has a druggable pocket: small-molecule screen for Myb-M stabilizers
- If KE#1 confirms luminal access: BKI sustained-release formulation development + CpIMPDH luminal formulation test
- If enhanced ORT shows oocyst shedding change: beta-glucan crypto-specific calf challenge

**Tier 3 -- Long-Horizon Investments (12-36 months):**
- VHH nanobody generation (anti-CSL as anchor target)
- AP2-F thin-walled oocyst question
- CpFAS1 oocyst wall incorporation study
- BKI + CpPDE1 combination design

### Force-Ranking for 70% Test (Anvil Input)

For Anvil's coverage assessment, the targets that should be counted toward the 70% tractable pathology threshold are:

| Disease Stage | Primary Target | Backup | Coverage Confidence |
|--------------|---------------|--------|-------------------|
| S2. Invasion | BKI/CpCDPK1 (calf POC) | VHH nanobody (deferred) | MODERATE |
| S3. Niche/Drug Delivery | KE#1 resolves this | CpIMPDH (deferred) | LOW (depends on KE#1) |
| S4. Merogony | BKI/CpCDPK1 + CpPDE1 | MMV665917 (if replicates) | MODERATE-HIGH |
| S5. Autoinfection | CpPDE1 (egress blocks oocyst production) | Myb-M (if druggable) | LOW-MODERATE |
| S6. Immune Acceleration | Meloxicam (PGE2 hypothesis) | Beta-glucan (deferred) | LOW |
| S7. Pathology Mitigation | Enhanced ORT | -- | HIGH (if trial confirms) |
| S8. Shedding Reduction | All anti-parasitic candidates (secondary effect) | Myb-M (if druggable) | MODERATE |
| S9. Post-Infection Recovery | Deferred (Wnt activator) | Butyrate supplementation | LOW |

**Honest assessment for Anvil:** The portfolio is STRONGER than v1 (which failed at 46.3%) because CpPDE1 and Myb-M add genuinely novel mechanisms that v1 lacked. But the 70% test against tractable pathology will be tight. Stage S5 (autoinfection) remains the weakest link -- no validated approach directly breaks the thin-walled oocyst cycle. CpPDE1's egress blockade is the best indirect approach (trapped parasites cannot produce oocysts), but it is single-lab and unproven in calves. If CpPDE1 fails to replicate, the autoinfection stage has no credible coverage, and the 70% test will fail again.

**The critical path to 70%:** CpPDE1 replication + BKI as combination backbone + Myb-M as high-ceiling moonshot + Enhanced ORT as baseline improvement. If CpPDE1 replicates AND BKI formulation is feasible, the combination addresses S2 + S4 + S5 simultaneously. Add enhanced ORT for S7, and the portfolio reaches 70% of tractable pathology.

### Strategic Note for Cargill

Cargill is a nutrition company, not a pharma company. Agteria's value proposition is identifying novel drug targets with clean IP for licensing to pharma partners or for Cargill's own development. The portfolio hierarchy should be presented to Cargill as:

1. **Novel drug targets for licensing (Agteria's core value):** CpPDE1, Myb-M, BKI formulation innovation, VHH nanobody platform
2. **Near-term operational improvement (Cargill's internal action):** Enhanced ORT protocol, environmental management
3. **Combination strategy (joint development):** BKI + CpPDE1 combination as the anchor product concept, with Myb-M as the long-horizon curative moonshot

The zoonotic dimension (C. parvum infects humans, no effective treatment for immunocompromised patients) adds public health value and potential for dual-species development, which increases the licensing value of any novel target.

---

*Board decision complete. 6-model external panel synthesized. Devil's advocate applied to all survivors. Force-ranking delivered with no ties. Priority De-Risk Sequence: 3 experiments at $50-70K total. KE#1 runs in parallel. 18 targets deferred with explicit reactivation triggers.*
