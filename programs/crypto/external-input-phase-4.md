# Adversarial Review — phase-4-kill-report.md

Generated: 2026-03-27 13:24

Document: `programs/crypto/phase-4-kill-report.md`

---

### OpenRouter (gemini-2.5-pro)

Excellent. The Reaper agent's analysis is thorough, but it exhibits a predictable bias towards academically interesting mechanisms and underestimates practical, on-farm failure modes. My independent review follows.

---

## WRONG KILLS (Targets killed that should survive)

I have reviewed the agent's 12 primary kills and find them to be robustly defended. The reasoning for killing targets based on definitive CRISPR data (CpAOX, CpIMPDH, CpDHFR), fundamental biological mismatches (NTZ), insurmountable PK/PD barriers (Racecadotril, Gal-GalNAc), or clear commercial non-viability (Bovilis Cryptium enhancement) is sound.

I find no fault with the agent's kills. This review will therefore focus on its survivals and blind spots.

## WRONG SURVIVALS (Targets that survived but should be killed)

The agent allowed several candidates to survive based on theoretical elegance while downplaying fatal, unresolved questions.

**1. Crofelemer (B11)**

*   **Fatal Flaw:** The entire rationale for crofelemer rests on the unproven and unquantified assumption that secretory diarrhea is a major driver of pathology in neonatal calf cryptosporidiosis. The agent's own "Embarrassment Test" correctly identifies the kill shot: *"We test crofelemer in crypto calves and discover the primary diarrhea mechanism in neonatal crypto is malabsorptive (villous atrophy), not secretory (chloride channels). Blocking chloride secretion reduces stool volume by <15%."*
*   **Evidence:** The pathophysiology of cryptosporidiosis is dominated by villous blunting and epithelial cell destruction, leading to a profound malabsorptive and maldigestive state. While a secretory component may exist, its contribution relative to the massive loss of absorptive surface area is unknown. A drug that only addresses a minor component of the pathology is not a viable adjunct. The agent's decision to let this survive without any data on the relative contribution of the target mechanism is a failure of rigor.
*   **Verdict should be:** **KILLED**. The burden of proof is on the proposal to demonstrate the target mechanism is clinically relevant. Without data quantifying the secretory vs. malabsorptive components of diarrhea in this specific disease model, the target is speculative and should be killed.

**2. EGF Supplementation for Mucosal Repair (D5)**

*   **Fatal Flaw:** The proposal fails to consider that the parasite may hijack host growth factor signaling for its own benefit. Promoting epithelial proliferation in the presence of an active infection could simply provide more healthy, new host cells for the parasite to invade, potentially worsening or prolonging the infection.
*   **Evidence:** It is a known strategy for intracellular pathogens to manipulate host cell signaling, including growth factor pathways, to create a favorable replicative niche. For example, *Toxoplasma gondii* (a related apicomplexan) is known to manipulate host EGFR signaling. The agent's analysis only considers the host benefit (repair) and ignores the potential parasite benefit (more targets). This is a critical oversight.
*   **Verdict should be:** **KILLED**. The risk of exacerbating the primary infection by providing fresh target cells is too high. The "dump the infected cell" strategy of the IL-22 inducers (D1) is biologically superior as it simultaneously removes parasites and promotes renewal. EGF promotes renewal without removing the parasite threat.

## SINGLE-LAB DEPENDENCIES

The agent correctly identified several single-lab dependencies. I will consolidate and emphasize them here as they represent a systemic portfolio risk. ALL of the most promising non-Novartis/ANL candidates rely on data that has not been independently replicated.

*   **Anti-P23 IgY (A6):** All neonatal calf efficacy data originates from a single 2025 study by **Cho et al.** The entire viability of this candidate rests on one paper from one group.
*   **NOD2 Agonism / MDP (C1):** All supporting data comes from a single 2025 neonatal mouse study from an **unnamed lab**. This is a single paper, in a single species, from a single group.
*   **EDI048 (A1) Calf Data:** While mouse data is broader, the critical neonatal calf efficacy data comes primarily from the **Novartis/Hulverson group**.
*   **AN7973 (A2) Calf Data:** Similarly, the critical neonatal calf efficacy data originates from the **research group associated with the Jumani et al. and Swale et al. publications**.

## MISSING KILL TESTS

The agent's 12 kill tests are comprehensive but miss several critical, practical failure modes relevant to the neonatal calf and modern farm environment.

**1. Target: EDI048 (A1), AN7973 (A2), and all other oral candidates.**

*   **Missing Test: The "Anorexic Calf" Test.**
*   **Failure Mode:** The entire delivery model assumes the drug is consumed orally in milk replacer. Sick calves, particularly those with severe cryptosporidiosis, are anorexic and often refuse to drink. A drug is useless if the calf won't ingest it. Efficacy in a controlled trial where intake is forced or guaranteed does not reflect field conditions where a farmer may not have time to tube-feed every sick animal.
*   **Likelihood:** High. Anorexia is a primary clinical sign of severe calf scours. Any oral drug's business case depends on voluntary intake,

---

### OpenRouter (grok-4-07-09)

## WRONG KILLS (Targets killed that should survive)
- **B14 — NTZ Reformulation (Gut-Restricted Nitazoxanide)**: The kill reasoning is wrong because it overemphasizes immune dependence as an absolute barrier, ignoring evidence that NTZ has direct antiparasitic effects (e.g., interference with pyruvate:ferredoxin oxidoreductase) that could be amplified by gut-restricted reformulation to achieve higher luminal concentrations without systemic reliance. Evidence supporting the target includes in vitro studies showing NTZ's cidal activity against Crypto independent of host immunity (e.g., Gargala et al., 2000, Antimicrob Agents Chemother), and neonatal calf trials where NTZ reduced oocyst shedding even in immature hosts (e.g., Ollivett et al., 2012, J Vet Intern Med). While immune cooperation enhances efficacy, it's not strictly required, and reformulation could mitigate PK issues in diarrheic calves. Verdict should be WOUNDED (needs calf-specific reformulation testing, but not killed outright).
- **C5 — Atovaquone-Like Compounds (Ubiquinone Pathway/CpAOX)**: The kill is wrong because it relies too heavily on a single 2025 FASEB Journal CRISPR KO study claiming CpAOX non-essentiality, but that study used in vitro/in vivo models that may not fully replicate the metabolic stress in neonatal calf infections; earlier data (e.g., Vanaerschot et al., 2014, PLoS Pathog) suggests Crypto's mitosome retains some redox functions under hypoxic gut conditions, making AOX inhibition potentially disruptive. Supporting evidence includes atovaquone's modest but consistent in vitro activity against Crypto (e.g., Woods et al., 1996, Antimicrob Agents Chemother) and synergies with other inhibitors in related apicomplexans. The decoquinate failure was dosing-related, not target invalidation. Verdict should be WOUNDED (needs better in vivo validation in calves, but CRISPR data isn't conclusive enough for a kill).
- **EXT-1 — CpIMPDH Inhibition (Purine Salvage)**: The kill is wrong because the Pawlowic 2019 PNAS CRISPR KO showed viability under lab conditions but noted fitness costs in vivo (e.g., reduced virulence in mice), suggesting IMPDH is conditionally essential in high-burden infections like neonatal calves where host purine availability may be limited. Evidence includes mycophenolic acid's in vitro inhibition of Crypto growth (e.g., Umejiego et al., 2008, Chem Biol) and structural divergence allowing selective inhibitors (e.g., Gorla et al., 2013, J Med Chem). The "bypass" via host import isn't absolute in stressed environments. Verdict should be WOUNDED (needs calf-specific fitness testing of KO mutants).

## WRONG SURVIVALS (Targets that survived but should be killed)
- **A1 — EDI048 (CpPI4K Inhibitor)**: Fatal flaw is the unresolved cidal-vs-static mechanism, which Reaper downplayed as a "development question" but is actually a biological kill; if static (as suggested by Forge notes on unclear sexual stage effects and echoes of halofuginone's cryptostatic failure), it won't clear infections in high-burden calf settings, leading to rapid recrudescence. Evidence: Manjunatha et al. 2017 (Nature) shows arrest but not killing in time-kill assays, and no long-term clearance data beyond 7 days in calves (Hulverson et al. 2024, Nature Microbiol). This repeats Sapper's core failure mode.
- **D1 — IL-22-Inducing Oral Innate Immune Activator (I3C/AhR)**: Fatal flaw is the species-specific immaturity of bovine neonatal ILC3 cells, which lack robust AhR responsiveness compared to mice/piglets; I3C induction may fail entirely in calves due to underdeveloped innate pathways. Evidence: Piglet data (2024, Journal of Virology) is not directly translatable, and bovine studies show delayed ILC3 maturation until week 4 (e.g., Hoek et al., 2019, Front Immunol), making timely IL-22 induction unlikely during the 0-14 day infection window. This is a translation failure, not just a cheap test.
- **EXT-9 — MCFAs (Lauric Acid/Coconut Oil)**: Fatal flaw is the limited exposure to intracellular parasites; MCFAs disrupt membranes of extracellular stages only, but Crypto spends most of its cycle epicellularly/intracellularly, rendering the approach ineffective against established infections. Evidence: In vitro sporozoite killing (cited by Claude) doesn't translate to in vivo calf models, where mixed results show no significant oocyst clearance (e.g., Shahiduzzaman et al., 2009, Parasitol Res), and the brief extracellular phase (minutes) provides insufficient window for meaningful impact.

## SINGLE-LAB DEPENDENCIES
- **A2 — AN7973 (CPSF3 Inhibitor)**: All calf efficacy data comes from the Jumani/Swale group (e.g., Jumani et al. 2019, Nature Communications; Swale et al. 2019, Science Translational Medicine). Mouse data is broader, but the critical neonatal calf validation is single-lab dependent, risking overestimation of efficacy if not replicated independently.
- **B11 — Crofelemer (CFTR/CaCC Chloride Channel Blocker)**: All relevant mechanistic data for diarrhea (though not Crypto-specific) stems from the Curran/Barrett lab at UCSF (e.g., Tradtrantip et al., 2010, J Clin Invest), with no independent replication in veterinary models; this dependency heightens uncertainty about its luminal efficacy in calves.
- **D5 — EGF Supplementation for Mucosal Repair**: Supporting data for neonatal intestinal repair is predominantly from the Buret lab (e.g., Buret et al., 1998, Infect Immun), with limited cross-lab confirmation in bovine models; the crypto-specific application relies entirely on this group's extrapolations.

## MISSING KILL TESTS
- **A2 — AN7973 (CPSF3 Inhibitor)**: Failure mode not considered is boron toxicity accumulation in repeated dosing; benzoxaboroles can form stable complexes with host enzymes (e.g., off-target inhibition of mammalian PDE4 as seen in related compounds), potentially causing neurotoxicity in neonates over a 7-day course. Likelihood: Moderate (30-50%), based on class effects in oncology benzoxaboroles (e.g., bortezomib analogs showing peripheral neuropathy).
- **B15 — Combination: EDI048 + AN7973**: Failure mode not considered is pharmacokinetic antagonism in the gut lumen; the ester moiety of EDI048 could hydrolyze prematurely in the presence of AN7973's boron, reducing bioavailability of both. Likelihood: High (50-70%), as no co-formulation stability data exists, and gut chemistry interactions are common in oral combos (e.g., similar issues with kinase inhibitors and boronic acids in pharma pipelines).
- **D8 — Lactose-Reduced Milk Replacer**: Failure mode not considered is nutritional deficiency leading to stunted growth; reducing lactose (a primary energy source for neonates) without adequate caloric replacement could exacerbate weight loss in already-compromised calves. Likelihood: High (60-80%), supported by calf nutrition studies showing lactose as 40-50% of energy needs (e.g., Drackley, 2008, J Dairy Sci), with no crypto-specific caloric balance data.

---

### OpenRouter (gpt-5.4-20260305)

## WRONG KILLS (Targets killed that should survive)

### B7. Bovilis Cryptium enhancement / gp40-gp60 vaccination
**Why the kill is wrong:**  
The report kills this on the basis of modest effect size in the first approved product and antigen polymorphism. That is not a fatal flaw for the *target class*. It is evidence the first-generation product is weak, not that maternal vaccination/passive antibody boosting against Crypto is biologically capped at irrelevance. In food-animal prophylaxis, modest reductions in diarrhea incidence/severity can still be commercially meaningful if cheap and integrated into herd programs.

**What evidence supports the target:**  
- There is already a licensed bovine product, which is stronger validation than most of the “survivors” have.  
- Field efficacy, even if modest, proves the modality can move a real endpoint in calves.  
- Crypto control in calves is inherently partial; an intervention that reduces disease burden rather than sterilizes infection can still survive as an adjunct/prevention-layer product.

**What the agent got wrong conceptually:**  
It conflates “first product underperforms” with “enhancement cannot work.” That is too strong. GP60 polymorphism is a real wound, but polyvalent or non-GP60 antigen additions are exactly what an enhancement program would try to solve.

**Correct verdict:**  
**WOUNDED**, not killed.

---

### D6. Engineered *L. reuteri* secreting anti-P23 VHH
**Why the kill is wrong:**  
The report treats EU/global GMO regulatory difficulty as an absolute commercial impossibility. That is overstated. Regulatory difficulty is not the same as a fatal flaw, especially for an early concept. Geographic segmentation alone breaks the “cannot be sold” logic.

**What evidence supports the target:**  
- *L. reuteri* is a plausible gut chassis in neonates.  
- VHH secretion by microbes is a technically active field; oral biologic delivery by live biotherapeutics is not science fiction.  
- P23 itself has supporting biology as a reinvasion-associated antigen.

**Why this matters:**  
This should be deprioritized, not killed. If the proposal had been “primary global commercial product,” kill would be fair. But as a biologically coherent platform concept, the proper objection is translational/regulatory uncertainty.

**Correct verdict:**  
**WOUNDED**, not killed.

---

### B9. Gal-GalNAc competitive blockade
**Why the kill is wrong:**  
The report kills the concept as a stoichiometric impossibility, but it only analyzes free-sugar competition in bulk lumen. That is a narrow implementation, not the target principle. Competitive blockade can be delivered via multivalent glycoconjugates, mucoadhesive polymers, or high-avidity decoys localized at the epithelial surface. The kill overreaches from one formulation logic to the whole mechanism.

**What evidence supports the target:**  
- Gal/GalNAc-mediated attachment has longstanding biological support in *Cryptosporidium* invasion literature.  
- Blocking attachment is a valid extracellular-stage strategy, especially as an adjunct reducing initial seeding/reinvasion.

**What verdict should be:**  
Killing “free sugar as feed additive” may be justified. Killing the broader **Gal-GalNAc blockade target concept** is not.

**Correct verdict:**  
**WOUNDED** for practical delivery issues.

---

## WRONG SURVIVALS (Targets that survived but should be killed)

### D1. IL-22-inducing oral innate immune activator (I3C/AhR)
**Fatal flaw:**  
This survival is much too generous. The evidence chain is almost entirely indirect: mouse immunology, piglet PEDV data, generalized AhR/IL-22 biology, then a leap to neonatal calf crypto. That is a mechanistic stack of assumptions, not target validation. Worse, I3C is a promiscuous dietary signaling molecule with pleiotropic host effects and no demonstrated crypto efficacy in calves, mice, or even a crypto model.

**Evidence/problem:**  
- No bovine neonatal crypto efficacy data.  
- No demonstrated bovine ileal ILC3/AhR responsiveness in this disease context.  
- PEDV piglet data is a different virus, different tropism, different pathology.  
- IL-22 can be protective or pathological depending on timing/intensity; the report ignores the risk of pushing epithelial/inflammatory remodeling in an already damaged neonatal gut.

**Why this is fatal:**  
This is basic hypothesis-generation masquerading as a surviving product concept. Cheapness of a de-risk experiment is not evidence. If “no species data + no disease-model efficacy + indirect cross-species immunology” survives, the bar has collapsed.

**Correct verdict:**  
**KILLED** as a target/product proposal; retain only as exploratory biology.

---

### B11. Crofelemer
**Fatal flaw:**  
This survives despite zero cryptosporidiosis-specific efficacy evidence and no calf data. The mechanism mismatch risk is not a caveat; it is central. Crypto diarrhea in calves is heavily driven by villus injury/malabsorption, not just secretory chloride flux. The report itself states the key uncertainty is the proportion of secretory vs malabsorptive diarrhea, yet still lets it survive.

**Evidence/problem:**  
- Approved for HIV noninfectious-secretory diarrhea, not protozoal enteropathy in calves.  
- No calf PK/PD or efficacy data.  
- Botanical mixture with batch-complexity and veterinary formulation questions.  
- If diarrhea mechanism is mostly malabsorptive, the target is nearly irrelevant.

**Why this is fatal:**  
Adjunct status should not exempt a target from evidentiary standards. By the report’s own rules, this fails species and endpoint relevance.

**Correct verdict:**  
**KILLED**.

---

### C3. Beta-glucan trained immunity
**Fatal flaw:**  
This survives mostly because Cargill already has a product and testing is cheap. That is not scientific survival. There is no controlled crypto efficacy evidence. “Trained immunity” in neonatal calves over the infection timescale is speculative, and the report itself articulates the obvious null scenario.

**Evidence/problem:**  
- No crypto-specific controlled trial.  
- Neonatal immune immaturity may limit the effect.  
- Historical experience with nonspecific immune/nutritional modulation in crypto is weak.  
- Clinical endpoint data absent.

**Why this is fatal:**  
The agent replaced biology with portfolio convenience. Existing product status is not evidence of anti-crypto value.

**Correct verdict:**  
**KILLED** as a crypto target; maybe retain as a low-cost exploratory test outside the main portfolio.

---

### C4. Ondansetron
**Fatal flaw:**  
This survives on price and safety, not on relevance. Ondansetron is an antiemetic/5-HT3 antagonist; the report assumes a “plausible neurogenic secretory component” without showing this component matters in neonatal bovine crypto diarrhea.

**Evidence/problem:**  
- No crypto-specific calf data.  
- Calves are not using this for vomiting control in a disease where vomiting is not the major issue.  
- No evidence that serotonergic secretory signaling is a meaningful driver of stool losses in calf cryptosporidiosis.

**Why this is fatal:**  
This is mechanism speculation plus convenience. Cheap to test is not enough to survive if the target could easily be irrelevant.

**Correct verdict:**  
**KILLED**.

---

### D5. EGF supplementation
**Fatal flaw:**  
This is being advanced for a recovery-phase benefit with no crypto-specific evidence and major delivery/cost doubts. Oral peptide/protein delivery in calves is nontrivial; abomasal/protease degradation is an obvious fatal practical issue, not a minor caveat.

**Evidence/problem:**  
- No demonstrated preservation of EGFR signaling in infected calf ileum.  
- No crypto-specific efficacy data.  
- Protein stability and cost are serious barriers for livestock use.  
- “Addresses the 34 kg growth deficit” is aspirational, not evidence-based.

**Why this is fatal:**  
The report rewards an unmet need rather than evidence. This is a hypothesis, not a surviving candidate.

**Correct verdict:**  
**KILLED**.

---

### D8. Lactose-reduced milk replacer
**Fatal flaw:**  
This survived because it is easy for Cargill to make. That is not a target defense. Secondary lactase deficiency is plausible, but there is no crypto-specific efficacy evidence, and reducing lactose in neonatal calves risks compromising energy delivery exactly when sick calves need calories.

**Evidence/problem:**  
- No crypto calf trial.  
- Lactose is a major energy substrate in milk replacer.  
- Reformulation may worsen intake/growth if not carefully balanced.  
- Symptom plausibility is not evidence of disease benefit.

**Why this is fatal:**  
This is husbandry speculation, not a validated intervention.

**Correct verdict:**  
**KILLED** from a drug-target portfolio, or at minimum demoted to non-portfolio management experiment.

---

### EXT-7. Zinc supplementation
**Fatal flaw:**  
Again, survival is based on being cheap and WHO-endorsed for human childhood diarrhea, not on calf crypto data. Extrapolation from human pediatric diarrhea to neonatal calf cryptosporidiosis is weak.

**Evidence/problem:**  
- No crypto-specific efficacy in calves.  
- Zinc can help generalized diarrhea/gut integrity without touching parasite burden or meaningful outcomes in this setting.  
- Species and disease-context extrapolation is doing all the work.

**Correct verdict:**  
**KILLED** as a crypto-specific target.

---

### EXT-9. MCFAs
**Fatal flaw:**  
This survives despite the report admitting the likely effect is limited to the very brief extracellular window. That is basically a mechanistic self-kill. If the active window is minutes and in vivo exposure control is poor, the modality is almost certainly too weak.

**Evidence/problem:**  
- Mostly in vitro/extracellular-stage rationale.  
- Mixed calf results.  
- Intracellular/epicellular stages dominate pathogenesis after establishment.

**Correct verdict:**  
**KILLED**.

---

### D4. Mucoadhesive nanoparticle drug delivery
**Fatal flaw:**  
The report exempts this because it is a “platform,” but that is exactly where a kill test should bite. In crypto calves, diarrhea and mucus disruption can defeat retention; manufacturing and cost are nontrivial; and no payload-specific efficacy exists. Platform status should not create immunity from evidence standards.

**Evidence/problem:**  
- No crypto-specific in vivo validation of retention/benefit.  
- Mucus depletion during infection may undermine the core mechanism.  
- Depends entirely on a payload that itself must work.

**Correct verdict:**  
**KILLED as an independent survivor**; can be reconsidered only paired with a proven drug.

---

## SINGLE-LAB DEPENDENCIES

### A1. EDI048
**Lab/group:** Novartis/Hulverson-associated group  
**Dependency:** All calf efficacy support appears to come from this development-associated group; independent neonatal calf replication is absent.

### A2. AN7973
**Lab/group:** Primarily the Van Voorhis/Swale/Jumani-linked antiparasitic development network  
**Dependency:** Calf efficacy is not independently reproduced by an unrelated lab.

### D1. IL-22 inducer / I3C-AhR
**Lab/group:** Support appears assembled from disparate immunology papers rather than direct crypto efficacy, but the livestock-neonatal translational support leans heavily on a small number of piglet AhR/ILC3 studies.  
**Dependency:** Not one lab for all data, but effectively one narrow literature pocket supports the livestock translation.

If strict “all supporting data from one lab” is required, A1 and A2 are the clearest surviving examples.

---

## MISSING KILL TESTS

### A1. EDI048
**Failure mode:** Overreliance on challenge-strain efficacy with insufficient field-isolate heterogeneity and coinfection context.  
**Why it matters:** Field calves often have mixed pathogens and variable inoculum; clean challenge efficacy may overpredict real-world benefit.  
**Likelihood:** Moderate.

### A1 / A2 / B15
**Failure mode:** Food-animal residue/withdrawal fatality.  
**Why it matters:** For neonatal calves entering food chains, residue depletion and milk/meat withdrawal can kill commercial feasibility even if efficacy is excellent. The report mentions commercial complexity but not residue toxicology as a hard gate.  
**Likelihood:** Moderate to high.

### A2. AN7973
**Failure mode:** Calf efficacy may be dose-impractical once scaled across farm conditions.  
**Why it matters:** 25 mg/kg may be biologically active yet economically or formulation-wise nonviable for routine use.  
**Likelihood:** Moderate.

### B11. Crofelemer
**Failure mode:** Wrong pathophysiology target; chloride secretion may be minor relative to malabsorption.  
**Why it matters:** This is the primary kill and should have been treated as likely, not hypothetical.  
**Likelihood:** High.

### C3. Beta-glucan
**Failure mode:** Existing-product bias mistaken for efficacy rationale.  
**Why it matters:** Cheap, available products can clutter portfolios with near-certain nulls.  
**Likelihood:** High.

### C4. Ondansetron
**Failure mode:** Adjuncts with no demonstrated disease-mechanism relevance are being allowed through because they are inexpensive.  
**Why it matters:** This lowers the survival bar and produces false-positive portfolio breadth.  
**Likelihood:** High.

### D1. I3C/AhR
**Failure mode:** Immunopathology or pathogen-agnostic epithelial remodeling harms nutrient absorption or worsens inflammation.  
**Why it matters:** Host-directed immune activators can worsen disease despite elegant mechanism diagrams.  
**Likelihood:** Moderate.

### D5. EGF
**Failure mode:** Growth-repair biology uncoupled from active infection control.  
**Why it matters:** Promoting repair during ongoing infection may feed epithelial turnover without improving outcomes, or even provide more target cells.  
**Likelihood:** Moderate.

### D8. Lactose-reduced milk replacer
**Failure mode:** Caloric dilution/poorer growth offsets any osmotic diarrhea benefit.  
**Why it matters:** In neonatal production animals, growth penalty can negate symptom gains.  
**Likelihood:** Moderate to high.

### EXT-7. Zinc
**Failure mode:** Human diarrhea generalization does not translate to calf crypto.  
**Why it matters:** The report repeatedly imports low-quality cross-context evidence into survivals.  
**Likelihood:** High.

### Portfolio-wide
**Failure mode:** “Adjunct inflation” — too many low-evidence supportive-care concepts survive because they are cheap, safe, or Cargill-compatible.  
**Why it matters:** This creates the illusion of a diversified portfolio while only 2 real antiparasitic assets exist.  
**Likelihood:** Very high.

---

### OpenRouter (claude-4.6-opus-20260205)

# Independent Challenge of Kill Report

## WRONG KILLS (Targets killed that should survive)

### B7 — Bovilis Cryptium Enhancement
The kill reasoning conflates the current product's modest efficacy with the theoretical ceiling of all vaccination approaches. The 0.4-day reduction was achieved with a SINGLE antigen (killed whole parasite) delivered via maternal vaccination — a suboptimal approach by design. The kill report dismisses "enhancement" as if it means tweaking the same product, but multi-antigen subunit vaccines targeting conserved (non-GP60) antigens delivered directly to neonates via oral mucosal immunization represent a fundamentally different approach. The report's own data shows rC7-targeted hyperimmune colostrum achieved 99.8% oocyst reduction (A5), proving that antigen selection matters enormously. A vaccine incorporating rC7 + P23 + conserved antigens could dramatically outperform Bovilis Cryptium. The GP60 polymorphism argument is valid against GP60-based vaccines but irrelevant if enhancement means switching to conserved antigens. The "40 years without success" argument is a 20-Year Test failure applied to the entire modality rather than to the specific enhancement concept. **Verdict should be: WOUNDED** (ceiling unknown for next-generation antigen combinations; worth exploring if conserved antigens are used).

### B14 — NTZ Reformulation
The kill is based on NTZ being "immune-dependent," citing failure in HIV patients and SCID mice. However, this oversimplifies the mechanism. NTZ's primary target is PFOR/NTR-mediated oxidative damage to the parasite — a DIRECT antiparasitic mechanism. The immune dependence may reflect that NTZ is cryptostatic at achievable systemic concentrations, and immune clearance is needed to finish the job. A gut-restricted formulation achieving 10-100x higher LUMINAL concentrations could push the drug from static to cidal territory, potentially eliminating the immune dependence. The report assumes immune dependence is binary and mechanism-intrinsic, but it may be concentration-dependent. The SCID mouse failure occurred at standard systemic doses. No one has tested gut-restricted NTZ at high luminal concentrations in immunocompromised models. **Verdict should be: WOUNDED** (immune dependence may be dose-dependent; gut-restricted high-concentration NTZ in immunocompromised mouse model is a cheap de-risk experiment before killing).

### C7 — Pro-Apoptotic Agents
The kill assumes BH3 mimetics are the only approach and that any pro-apoptotic intervention will cause catastrophic villous atrophy. But the concept includes TARGETED approaches — e.g., compounds that reverse Crypto's specific anti-apoptotic manipulation (survivin upregulation, NF-κB activation) without broadly inducing apoptosis in uninfected cells. A survivin-specific inhibitor would preferentially affect infected cells (which have upregulated survivin) over uninfected cells. The report correctly notes C1/D1 is strategically superior, but that doesn't make C7 fatally flawed — it makes it lower priority. **Verdict should be: WOUNDED** (targeted anti-survivin approach avoids the broad apoptosis concern; low priority but not dead).

---

## WRONG SURVIVALS (Targets that survived but should be killed)

### D1 — IL-22 Inducer (I3C/AhR)
The survival reasoning has a critical gap: **I3C is rapidly absorbed in the proximal small intestine and metabolized to DIM and other condensation products in the stomach's acidic environment.** The active AhR ligands from dietary I3C are acid-condensation products (DIM, ICZ) that are systemically absorbed, not luminally active in the distal ileum where *C. parvum* resides. To activate ILC3 cells in the ileal lamina propria, you need either (a) systemic delivery of AhR ligands (which means systemic immune effects, not the targeted innate activation claimed) or (b) a formulation that delivers I3C/DIM specifically to the ileum (which is a drug delivery problem equivalent to D7's bile acid conjugate). The piglet PEDV data cited involves a RESPIRATORY/PROXIMAL GI virus, not a distal ileal parasite. The $5-8K de-risk experiment (IHC + ex vivo stimulation) tests whether bovine ILC3 cells CAN respond to AhR ligands, not whether dietary I3C REACHES them at relevant concentrations in the ileum. This is a matrix test failure that the report missed. **Should be WOUNDED at minimum, with the ileal delivery problem flagged as potentially fatal.**

### D5 — EGF Supplementation
Oral EGF is a protein that will be degraded by pepsin in the abomasum of neonatal calves. The report's own embarrassment test mentions this but then survives the candidate anyway. Human neonatal EGF studies use EGF naturally present in breast milk, which is protected by milk's buffering capacity and other milk proteins. Supplemental recombinant EGF in milk replacer has no such protection. The cost issue is also unaddressed — recombinant bovine EGF at therapeutic doses for a 40 kg calf would likely cost $50-200/dose. This fails the commercial reality test for a recovery-phase adjunct. **Should be WOUNDED** with abomasal degradation and cost flagged as likely fatal.

### B11 — Crofelemer
The survival reasoning relies on the luminal mechanism avoiding the PK paradox. But crofelemer's mechanism requires binding to CFTR and CaCC on the APICAL surface of enterocytes. In crypto-infected calves, the apical surface of infected enterocytes is occupied by the parasitophorous vacuole, and surrounding enterocytes undergo massive villous atrophy with loss of normal apical architecture. The drug's target surface may be physically destroyed. Additionally, the report acknowledges the key uncertainty — what proportion of crypto diarrhea is secretory vs malabsorptive — but then survives the candidate without resolving it. Published pathology of neonatal calf cryptosporidiosis consistently emphasizes VILLOUS ATROPHY (malabsorptive) as the dominant mechanism, with secretory components being secondary. If malabsorption dominates, crofelemer addresses <20% of diarrhea volume. **Should be WOUNDED** with the malabsorptive-dominant pathology as a serious concern.

### C3 — Beta-Glucan Trained Immunity
The survival reasoning is essentially "it's free to test." But trained immunity requires epigenetic reprogramming of monocytes/macrophages, which takes 5-7 days to establish. Crypto infection in neonatal calves causes clinical disease within 3-5 days of exposure, often before trained immunity could be established. Prophylactic administration starting at birth might work, but calves are exposed to oocysts within hours of birth on endemic farms. The timing mismatch is fundamental, not just a "modest expectations" issue. More importantly, the report's own Sapper Treatment 17 analysis states probiotics/nutritional interventions fail because "the scale and speed of the infection overwhelm any microbiome-based defense." Trained immunity faces the same scale problem — even fully trained innate immune cells cannot clear 10^10 oocysts. This should have been killed by the repetition test. **Should be KILLED** — timing mismatch + scale mismatch make this biologically implausible against crypto specifically, regardless of cost.

---

## SINGLE-LAB DEPENDENCIES

### EDI048 (A1) — Calf efficacy data
All neonatal calf efficacy data comes from the Novartis/Hulverson group. The report correctly flags this as SINGLE-LAB DEPENDENCY but still gives a clean SURVIVED verdict. The KDU731 predecessor calf data is from the same collaborative network. **Lab: Novartis Global Health Institute / Hulverson / University of Washington collaboration.**

### AN7973 (A2) — Calf efficacy data
All neonatal calf efficacy data comes from the Bhatt/Bhatt/Jumani group (Huston lab, University of Vermont). Mouse data is broader but the critical calf data is single-source. **Lab: Christopher Huston lab, University of Vermont.**

### CpPDE1 (B5) — All data
The 2024 Nature Communications paper from Ajiboye et al. appears to be the sole source for CpPDE1 as a drug target. CRISPR validation, inhibitor screening, and mouse efficacy all from one publication/group. **Lab: Ajiboye/Bhatt group (likely overlapping with Huston lab network).**

### IL-22/I3C (D1) — Crypto-specific rationale
The NOD2/IL-22 connection to crypto clearance comes from the single 2025 mouse study (C1). The broader AhR/ILC3 biology is multi-lab, but the specific application to cryptosporidiosis rests on one study. **Lab: Unclear from report, but the 2025 NOD2/crypto mouse study is single-source.**

### Anti-P23 IgY (A6) — Already flagged
**Lab: Cho et al. 2025 — single study, single lab.** Report correctly identified this.

---

## MISSING KILL TESTS

### EDI048 (A1) — Cidal vs. static is not just a "development question"
The report treats the cidal-vs-static question as a minor development issue. But if EDI048 is static (which the report itself flags as plausible given "unclear on sexual stages"), then it REPEATS halofuginone's failure mode — the #1 Sapper constraint. A static PI4K inhibitor at $15-30/treatment that requires 7+ days of dosing and shows recrudescence after cessation is commercially dead. The report should have applied the Repetition Test more aggressively here. **Likelihood: moderate (30-40%).** The absence of published time-kill data for EDI048 is a red flag, not a footnote.

### AN7973 (A2) — Benzoxaborole boron-mediated drug-drug interactions
The report doesn't consider that benzoxaboroles form reversible covalent bonds with cis-diols. In a combination protocol (B15), AN7973 could interact with sugar-containing compounds in milk replacer, ORS formulations, or co-administered drugs. Boron-sugar interactions could sequester the active drug. This is particularly relevant because the proposed combination protocol includes lactose-reduced milk replacer, ORS, and potentially other sugar-containing adjuncts. **Likelihood: moderate.** Should be tested in simulated GI fluid with milk replacer components.

### AN7973 (A2) — 25 mg/kg dose commercial viability
The report mentions the 25 mg/kg dose but doesn't fully interrogate it. For a 40 kg calf over 7 days, that's 7 grams of API per treatment course. Benzoxaborole synthesis involves boron chemistry that is expensive at scale. At even $500/kg API cost (optimistic for boron-containing compounds), that's $3.50 in API alone before formulation, distribution, and margin. This may be viable but is at the edge. **Likelihood of commercial failure: moderate-high.**

### D8 — Lactose-Reduced Milk Replacer — Caloric deficit
The report's embarrassment test mentions this but doesn't kill or wound the candidate. Lactose provides ~40% of calories in milk replacer. A 50% lactose reduction without caloric replacement means a 20% caloric deficit in a neonatal calf that is already losing weight from diarrhea. The replacement carbohydrate/fat source matters enormously — some alternatives (e.g., glucose polymers) may cause osmotic diarrhea themselves. This is not trivial product reformulation; it requires careful nutritional balancing. **Likelihood of worsening outcomes: moderate.**

### B15 — EDI048 + AN7973 Combination — Regulatory impossibility
The report flags "commercial complexity" but understates the regulatory barrier. FDA-CVM's combination product requirements (VICH GL52, not just "Quality Standard 23") require demonstration that each component contributes to efficacy AND that the combination is superior to each component alone. For two novel APIs with no individual veterinary approvals, this means: (1) approve EDI048 alone, (2) approve AN7973 alone, (3) THEN prove combination superiority. This is a 10-15 year, $10M+ regulatory path. **Likelihood of never reaching market as a combination: high (>60%).**

### Crofelemer (B11) — Botanical standardization for veterinary use
Crofelemer is a complex botanical extract (proanthocyanidin polymer mixture from *Croton lechleri*). FDA-CVM has no precedent for approving a complex botanical extract for food-producing animals. The human FDA approval required extensive characterization that may not transfer to veterinary regulatory frameworks. Withdrawal period determination for a complex mixture in milk/meat is a regulatory nightmare. **Likelihood of regulatory failure: high for prescription product; moderate if positioned as feed additive (different regulatory path).**

### All surviving adjuncts — Combination interaction testing never mentioned
The report survives ~8 adjuncts (zinc, MCFAs, beta-glucan, ondansetron, crofelemer, ORS, lactose reduction, colostrum) without considering interactions between them. Zinc chelates with many compounds. MCFAs alter membrane permeability (could affect drug absorption). Beta-glucan binds small molecules. Cholestyramine (wounded but considered) binds everything. A protocol combining 5+ adjuncts has unpredictable interaction effects. **No interaction testing framework is proposed.**

---

### OpenRouter (deepseek-r1)

## WRONG KILLS (Targets killed that should survive)
None. All killed candidates appear to have fatal flaws as described. The kill reasoning is sound and evidence-based.

## WRONG SURVIVALS (Targets that survived but should be killed)
**D1 — IL-22 inducer (I3C/AhR)**  
*Fatal flaw:* No evidence that IL-22 induction protects against Cryptosporidium in any species. The supporting piglet data (Journal of Virology, 2024) is for protection against PEDV (a viral diarrhea), not a protozoan infection. Cryptosporidium causes distinct pathology (epicellular niche, villous atrophy) and may suppress ILC3 function or AhR signaling. The mechanism—epithelial renewal—is likely too slow to outpace Crypto’s rapid replication (R0 5–15). Without any Crypto-specific data, this candidate is purely speculative and should be killed.

**B11 — Crofelemer (CFTR/CaCC blocker)**  
*Fatal flaw:* No calf or Cryptosporidium-specific efficacy data. Crofelemer’s mechanism targets secretory diarrhea, but Cryptosporidium-induced diarrhea in neonates is predominantly malabsorptive due to villous atrophy. Human HIV‑associated diarrhea (the approval basis) is mechanistically different. The agent’s “embarrassment test” acknowledges this uncertainty, yet the candidate survived. Without evidence that secretory mechanisms contribute meaningfully to crypto diarrhea, crofelemer has no rationale for inclusion—even as an adjunct.

## SINGLE-LAB DEPENDENCIES
**EDI048 (A1)** – All calf efficacy data comes from the Novartis/Hulverson group (single lab).  
**AN7973 (A2)** – Calf efficacy data primarily from one research group (single lab).  
*Note: The agent tagged these as “wounded” for independent replication but still gave a SURVIVED verdict. These dependencies represent critical vulnerabilities for the portfolio backbone.*

## MISSING KILL TESTS
**D1 — IL-22 inducer (I3C/AhR)**  
*Failure mode:* Cryptosporidium infection may directly inhibit ILC3 function or AhR signaling in neonatal calves, rendering the inducer ineffective.  
*Likelihood:* Moderate—neonatal immune responses are immature and pathogen-specific modulation is common.

**A1/A2 — EDI048 and AN7973**  
*Failure mode:* Both compounds may have poor stability or bioavailability in milk replacer or under variable GI conditions (e.g., pH, enzyme activity) in neonatal calves. Formulation challenges could drastically reduce efficacy in field settings.  
*Likelihood:* Moderate—veterinary formulations must withstand farm handling and calf GI variability.

**B11 — Crofelemer**  
*Failure mode:* By reducing fluid secretion, crofelemer might impair the natural flushing of parasites from the gut lumen, potentially prolonging infection or increasing parasite burden.  
*Likelihood:* Low but plausible—fluid secretion may help mechanically clear parasites.

---

### OpenRouter (qwen-2.5-72b-instruct)

## WRONG KILLS (Targets killed that should survive)
### A7. Halofuginone (Halocur) — Existing Standard
**Why the kill is wrong:** While halofuginone is cryptostatic and not curative, it remains a valuable benchmark and can serve as a control in clinical trials. It has a well-established safety profile and is already in use, which provides a baseline for comparing the efficacy of new candidates.
**Evidence supporting the target:** Halofuginone has been used for over 30 years and has a well-documented safety and efficacy profile in treating cryptosporidiosis. It is the only approved treatment for cryptosporidiosis in calves, making it a critical comparator.
**Verdict should be:** **WOUNDED** (as a benchmark and control, not as a development candidate)

### B10. Racecadotril
**Why the kill is wrong:** While the PK data in diarrheic calves is a significant concern, racecadotril has shown promise in reducing secretory diarrhea in other contexts. The PK issues may be addressable with formulation improvements or in combination with other treatments.
**Evidence supporting the target:** Racecadotril has been used in humans and other animals to reduce secretory diarrhea. It has a well-established safety profile and has shown efficacy in reducing stool volume in other diarrheal diseases.
**Verdict should be:** **WOUNDED** (requires further PK optimization and combination studies)

## WRONG SURVIVALS (Targets that survived but should be killed)
### A3. MMV665917 — Piperazine-Based Compound (Unknown Target)
**What the flaw is:** The unknown target and the lack of follow-up publications since 2019 are significant red flags. The hERG liability of the original compound is a neonatal safety concern, and the silence since 2021 suggests the program may have been abandoned.
**Cite evidence:** The lack of recent publications and the hERG liability concern are significant. The unknown target makes it difficult to assess resistance, strain coverage, and rational combination design.
**Verdict should be:** **KILLED** (unknown target, safety concerns, and lack of recent development)

### B3. CpLDH + CpPyK Dual Glycolytic Inhibition
**What the flaw is:** The high EC50 values and the lack of calf data are significant concerns. Achieving sustained micromolar drug levels in the ileal lumen of a diarrheic calf may require very high oral doses, which is impractical and potentially toxic.
**Cite evidence:** The EC50 values for CpLDH (14.88 uM) and CpPyK (10-86 uM) are high, and achieving these concentrations in the ileal lumen of a diarrheic calf is challenging. The lack of calf data further limits the confidence in this approach.
**Verdict should be:** **KILLED** (high EC50, no calf data, and practical dosing concerns)

### D3. BSO/Gut-Restricted GSH Depletion
**What the flaw is:** The therapeutic window between "enough GSH depletion to kill the parasite" and "too much GSH depletion that damages enterocytes" may not exist. Neonatal calves already under oxidative stress from infection could be severely harmed by additional GSH depletion.
**Cite evidence:** The therapeutic window for GSH depletion is narrow, and the potential for host cell damage is high. The lack of data on the safety and efficacy of GSH depletion in neonatal calves is a significant concern.
**Verdict should be:** **KILLED** (narrow therapeutic window and potential for host cell damage)

## SINGLE-LAB DEPENDENCIES
### A6. Anti-P23 IgY (Egg Yolk Antibodies)
**Lab:** Cho et al. 2025
**Dependency:** All calf data comes from a single study by Cho et al. 2025. There is no independent replication of the calf trial.

### C1. NOD2 Agonism — MDP
**Lab:** Single study (2025)
**Dependency:** All neonatal mouse data comes from a single study. No independent replication in calves or other species.

## MISSING KILL TESTS
### A1. EDI048 — CpPI4K Inhibitor
**Failure mode:** **Long-term resistance development**
**Likelihood:** Moderate
**Explanation:** While the current data shows no resistance emergence during a 7-day treatment course, the long-term resistance potential is unknown. Continuous use in a field setting could lead to the emergence of resistant strains over time.

### A2. AN7973 — CPSF3 Inhibitor (Benzoxaborole)
**Failure mode:** **GI stability in acidic environments**
**Likelihood:** High
**Explanation:** The stability of AN7973 in the acidic abomasum of neonatal calves is a significant concern. If the compound degrades before reaching the small intestine, the in vivo efficacy observed in calves may not be reproducible in a field setting.

### B15. Combination: EDI048 + AN7973
**Failure mode:** **Antagonistic interactions**
**Likelihood:** Moderate
**Explanation:** The potential for antagonistic interactions between EDI048 and AN7973 in the gut lumen is a significant concern. The combination of two novel compounds from different chemical classes could lead to unexpected interactions that reduce the efficacy of both drugs.

### D1. IL-22-Inducing Oral Innate Immune Activator (I3C/AhR)
**Failure mode:** **Species-specific differences in AhR responsiveness**
**Likelihood:** High
**Explanation:** The responsiveness of bovine neonatal ILC3 cells to AhR ligands may differ significantly from that of piglets and mice. The lack of bovine neonatal data for AhR responsiveness is a critical gap that needs to be addressed before advancing this candidate.

---

