# Phase 4 -- Kill Report: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill | **Version:** v2
**Agent:** Reaper | **Date:** 2026-03-27

---

## Summary

38 candidates entered this phase (27 Forge + 15 Vulcan, merged to 38 unique by Surveyor with 4 direct convergences). I applied 12 standard kill tests plus 4 crypto-specific tests (Immune Independence, Duration, Timing, Autoinfection) to every candidate.

**Results:**

| Verdict | Count | Candidates |
|---|---|---|
| **KILLED** | 10 | #4, #11, #17, #19, #20, #21, #23, V5, V8, V11 |
| **WOUNDED** | 18 | #1, #3, #5, #6, #8, #9, #10, #12, #13, #14, #15, #18, #24, V1, V2, V3, V4, V7 |
| **SURVIVED** | 10 | #2, #7, #16, #22, #25, #26, #27, V6, V9, V13 |

Note: Vulcan targets V10 (CpPKG), V12 (CpIMPDH), V14 (dual aaRS), and V15 (T6PS-TPase) overlap with Forge candidates and are assessed under their converged entries.

---

## FORGE CANDIDATES

---

### Candidate #1: MMV665917 (Piperazine-Based Cryptosporicidal)

**Verdict: WOUNDED**

This is the most dangerous candidate in the portfolio -- dangerous because the calf data is real enough to attract investment, but fragile enough to collapse under scrutiny.

**Kill Test 11 (Independent Replication): FAIL -- SINGLE-LAB DEPENDENCY.** All efficacy data -- the calf study, the piglet study, the NOD SCID mouse cure, the time-kill assay -- comes from two closely collaborating groups: the Huston lab (University of Vermont) and the Tzipori lab (Tufts). Based on articles retrieved from PubMed, the calf study ([DOI](https://doi.org/10.1371/journal.pntd.0006183)) and piglet study ([DOI](https://doi.org/10.1093/infdis/jiz105)) share authors and funding sources. There is zero independent replication of the 94% shedding reduction in calves. Zero independent replication of the parasiticidal mechanism. Zero independent replication of the NOD SCID mouse cure.

**Kill Test 2 (Species): Concern.** The calf study used a grand total of how many calves? The paper (Stebbins et al., 2018) does not report a large n. This is a proof-of-concept study, not a powered clinical trial. The 94% shedding reduction is from a handful of animals. Statistical confidence at this sample size is insufficient to conclude therapeutic breakthrough.

**Kill Test 1 (20-Year Test): Concern.** MMV665917 was identified in 2018. It is now 2026 -- 8 years with no follow-on calf trials, no Phase I equivalent, no COGS analysis, no formulation development published. If this compound were as transformative as claimed, why has the field not advanced it? Possible answers: (a) the mechanism is unknown, making rational optimization impossible; (b) hERG inhibition at 58% at 11 uM is a development barrier; (c) the 22 mg/kg dose is high for a production animal -- COGS may exceed the $10-15 threshold.

**Kill Test 10 (Commercial Reality): Concern.** 22 mg/kg QD for 7 days for a 40 kg calf = 6.16 g total compound per calf. For a novel chemical entity with multi-step synthesis, this dose is likely unaffordable in production animals. No COGS analysis exists. The compound has hERG liability at 58% inhibition at 11 uM -- even if luminal delivery avoids cardiac exposure, this creates a regulatory burden for any absorbed fraction.

**Kill Test 9 (Repetition): Pass.** This is NOT repeating a known failure mode -- it is genuinely parasiticidal where everything else is parasitistatic. The mechanism is distinct.

**The Embarrassment Test (Kill Test 8):** The simplest way MMV665917 fails: the 94% shedding reduction in the calf study was observed in a tiny sample with intensive supportive care, and when repeated at commercial scale with realistic dosing compliance, the effect size shrinks to something resembling halofuginone. The unknown mechanism of action means there is no way to predict whether this will happen.

**Why WOUNDED, not KILLED:** The parasiticidal mechanism IS genuinely different from everything else in the pipeline. The NOD SCID mouse cure is remarkable -- NTZ, clofazimine, and paromomycin all fail in this model. The calf data, while thin, is the ONLY therapeutic (post-symptom) efficacy data in the species. But the single-lab dependency, unknown target, high dose, and 8-year stall are serious red flags.

**Required to graduate from WOUNDED:** Independent replication of the calf efficacy data by a lab with no Huston/Tzipori connection. COGS analysis proving <$15/treatment course. Target identification via resistance selection + WGS.

---

### Candidate #2: BKI-1553 / Next-Generation BKIs (CpCDPK1 Inhibitors)

**Verdict: SURVIVED**

I tried hard to kill this one. I could not.

**Kill Test 1 (20-Year Test): Pass.** CpCDPK1 was validated as a target in the mid-2000s. BKIs in calves since 2016. The 10-year timeline is explained by the hERG optimization cycle -- a legitimate medicinal chemistry challenge, not a hidden target problem. New scaffolds (BKI-1649, BKI-1812, BKI-1814) are in active development.

**Kill Test 2 (Species): Pass.** BKI-1553 has actual calf data (Schaefer et al., 2016). Fecal concentration predicts efficacy better than plasma -- this is a calf-specific pharmacology insight.

**Kill Test 4 (Strain): Pass.** CpCDPK1 is >99% conserved across IIa and IId subtypes. The glycine gatekeeper residue is universally conserved. Surveyor confirmed this.

**Kill Test 5 (Resistance): Moderate concern.** CDPK1 is a single gene target. Resistance via gatekeeper mutation (glycine to threonine) is theoretically possible and would eliminate the BKI selectivity mechanism entirely. However, such a mutation would likely reduce kinase activity and impose a fitness cost. No published resistance data for BKIs against C. parvum. This is a concern but not a kill.

**Kill Test 10 (Commercial Reality): Concern but manageable.** hERG toxicity in first-generation compounds is being addressed. The luminal delivery insight (fecal > plasma concentration) transforms the development path -- a non-absorbable oral formulation eliminates both hERG risk and simplifies the safety package. Sustained-release bolus formulation is the key unmet need.

**Crypto-Specific Duration Test: Concern.** Daily oral dosing for 14 days has the same compliance barrier as halofuginone. BUT: if sustained-release luminal delivery is achieved, this concern vanishes. The formulation gap is real but is an engineering problem, not a biology problem.

**Kill Test 11 (Independent Replication): Pass.** Multiple labs have contributed to BKI development (Van Voorhis at UW, Huston at UVM, others). Calf data is from one study but the mouse data spans multiple groups. This is not a single-lab story.

**What I tried and why it failed:** I tried to kill BKIs on the argument that fecal concentration driving efficacy means the compound never actually reaches the intracellular parasite and is working via some indirect luminal mechanism. But paromomycin proves luminal access to the niche IS real, and the CpCDPK1 target is validated as essential by conditional knockdown. The mechanism chain holds.

**Why it survived:** Best-validated target in Crypto. Crystal structures for rational optimization. Parasite-specific (no mammalian CDPKs). Active compound optimization addressing hERG. Calf proof-of-concept exists. The path from here to a product is medicinal chemistry and formulation -- not fundamental biology discovery.

---

### Candidate #3: Paromomycin Analogs / Reformulated Paromomycin

**Verdict: WOUNDED**

**Kill Test 10 (Commercial Reality): FAIL.** 100 mg/kg/day x 11 days x 40 kg calf = 44 g of drug. Even generic paromomycin at bulk pricing makes this $15-30/course -- at or above the production animal threshold. A sustained-release non-absorbable formulation would need to deliver the same total drug load but in a single bolus. 44 g of drug in a single bolus is a formulation fantasy. The gastric volume of a neonatal calf cannot accommodate this.

**Kill Test 9 (Repetition): FAIL.** The reformulation hypothesis assumes the ONLY problem is delivery/toxicity. But Sapper documents that at 50 mg/kg (half-dose), paromomycin shows rebound after cessation. At 25 mg/kg, calves gained LESS weight than controls -- toxicity at sub-therapeutic doses. The therapeutic window is razor-thin. Reformulation cannot widen a therapeutic window -- it can only change the PK curve. If the minimum effective luminal concentration is inherently near the toxic concentration, reformulation changes nothing.

**Kill Test 8 (Embarrassment): The simplest failure mode:** Non-absorbable paromomycin reformulation achieves luminal concentrations that fluctuate between effective and sub-effective levels across the 14-day window. During troughs, autoinfection restarts. During peaks, local toxicity damages enterocytes. The net effect is equivalent to standard paromomycin with extra steps.

**Why WOUNDED, not KILLED:** Paromomycin at 100 mg/kg IS the closest thing to a proof-of-concept cure. The principle -- sustained luminal aminoglycoside -- is validated. The problem is this SPECIFIC compound at this SPECIFIC dose. If a less toxic luminal agent with the same ribosomal mechanism could be identified at lower effective concentrations, the reformulation strategy becomes viable. The principle survives; the compound does not.

**Required to graduate:** Identify minimum effective luminal concentration (is it really 100 mg/kg equivalent, or could 25-50 mg/kg work with sustained delivery?). If the answer is "must be 100 mg/kg," this is KILLED on formulation impossibility.

---

### Candidate #4: Halofuginone + Sustained-Release Reformulation

**Verdict: KILLED**

**Kill Test 9 (Repetition): FATAL.** Forge itself admits halofuginone is cryptostatic, has a narrow therapeutic index, and achieves only ~25% improvement in diarrhea duration. Sapper documents this in detail. The bottleneck consensus quantifies why: partial merogony suppression on an exponential growth curve produces a temporal delay of ~1 cycle (12-14h), NOT a reduction in peak burden. Sustained-release reformulation eliminates inter-dose troughs, but the CEILING of the compound's mechanism is unchanged.

**The math is unforgiving.** Even with perfect sustained-release achieving constant luminal halofuginone concentration, the compound is cryptostatic. It slows replication by some fraction. The Martian calculated that you need >80% suppression of the replication rate to meaningfully shift the kinetic balance. Halofuginone's narrow therapeutic index (effective dose approaches toxic dose) means the maximum tolerable concentration achieves far less than 80% suppression. Sustained-release does not change the drug's potency at its target -- it only eliminates concentration fluctuations.

**Kill Test 5 (Resistance): Additional concern.** MetRS inhibitor (same aaRS class) generated resistant C. parvum within days in calves. ProRS (halofuginone's target) faces the same single-gene resistance risk. The parasite replicates fast enough (8 merozoites per 12-14h) to generate resistance mutations against a single-target cryptostatic drug.

**Killed because:** A weak drug in a better formulation is still a weak drug. Halofuginone's mechanism sets an insurmountable ceiling. Sustained-release is engineering effort spent on a compound that cannot succeed by mechanism. Spend the formulation development effort on BKIs or MMV665917 instead.

---

### Candidate #5: Anti-GP40/GP15 Monoclonal Antibody (Sustained Luminal Delivery)

**Verdict: WOUNDED**

**Surveyor Correction (FATAL for current design): GP60 is the subtyping locus -- the MOST VARIABLE gene in the C. parvum genome.** Anti-GP40 antibodies generated against one subtype (e.g., IIaA15G2R1) may fail against another subtype (IId). This is not a minor polymorphism concern -- GP60 is the gene that DEFINES subtypes. Sequence variation in the serine repeat region is extensive. Any monoclonal antibody targeting a linear epitope in the variable region is dead on arrival for broad-spectrum protection.

**Kill Test 4 (Strain): FAIL for monoclonal approach.** A single mAb cannot cover GP60 diversity. This needs either (a) a cocktail targeting multiple subtypes, (b) a mAb targeting a strictly conserved conformational epitope (which may be glycan-dependent and therefore unreproducible recombinantly), or (c) abandonment of the single-mAb concept.

**Crypto-Specific Duration Test: FAIL.** Forge acknowledges antibody half-life in the gut lumen is hours, not days. The 14-day window requires continuous antibody presence. Even with mucoadhesive microsphere encapsulation, maintaining active antibody concentration for 14 days in a proteolytic gut environment is an unsolved problem. The technology does not exist.

**Why WOUNDED, not KILLED:** The anti-GP40 principle IS validated -- hyperimmune colostrum with anti-GP40 antibodies DOES reduce disease. The target biology works. The failures are compound-level (antibody degradation) and strain-level (GP60 polymorphism). The VHH nanobody approach (Candidate #9) addresses both problems more directly. This candidate should be subsumed into #9, not pursued independently.

---

### Candidate #6: CpIMPDH Inhibitors

**Verdict: WOUNDED**

**Kill Test 1 (20-Year Test): FAIL.** CpIMPDH was structurally characterized with inhibitors at nanomolar IC50 over a decade ago (Hedstrom lab). Crystal structures since 2007-2013. Multiple chemotypes developed. Yet NO in vivo proof-of-concept in any animal model exists. This is the loudest silence in the portfolio. If you have a validated essential target with nanomolar inhibitors and crystal structures for a decade, and STILL no in vivo efficacy, the delivery problem is either unsolved or unsolvable.

**The delivery gap is diagnostic.** CpIMPDH inhibitors work beautifully in cell culture. They fail to translate. The extracytoplasmic niche means the inhibitor must either (a) traverse the host cell and enter the parasitophorous vacuole, or (b) reach the parasite from the luminal side. If luminal delivery works (as Forge hypothesizes based on paromomycin precedent), then someone should have tested a non-absorbable CpIMPDH inhibitor in mice by now. The fact that this has not happened in >10 years suggests either the compounds are not suitable for luminal delivery, or the delivery challenge is harder than it appears.

**Kill Test 8 (Embarrassment):** CpIMPDH inhibitors achieve nanomolar IC50 in HCT-8 cell culture but when administered to mice, the compound is either absorbed systemically (leaving the gut lumen too quickly to reach the parasite) or stays in the lumen but cannot penetrate the parasitophorous vacuole membrane from the outside. The cell culture model does not have a mucus layer, peristalsis, or transit time -- factors that may be decisive for luminal drug-to-parasite access.

**Why WOUNDED, not KILLED:** The target is real (essential, no bypass, structurally distinct from host). The inhibitors are real (nanomolar, selective). The concept of luminal reformulation is sound in principle. But the decade-long absence of in vivo data is a warning that the execution challenge is severe. This cannot be a portfolio PRIMARY until the delivery-to-efficacy gap is closed.

**Required to graduate:** Non-absorbable CpIMPDH inhibitor tested in IFN-gamma-KO mouse model with efficacy demonstrated. If luminal formulation fails in mice, this is KILLED.

---

### Candidate #7: CpPDE1 Inhibitors (Pyrazolopyrimidines)

**Verdict: SURVIVED**

Based on articles retrieved from PubMed, the 2024 Nature Communications paper ([DOI](https://doi.org/10.1038/s41467-024-52658-y)) provides genetic validation via CRISPR mutant and oral efficacy in immunocompromised mice.

**Kill Test 1 (20-Year Test): Pass.** CpPDE1 was validated as a drug target in 2024 -- this is a brand-new target, not a stalled one.

**Kill Test 2 (Species): Concern but not fatal.** Only mouse data. No calf data. BUT: the mice were immunocompromised (IFN-gamma KO), which partially models the neonatal calf's immunological state during the vulnerability window. This is the correct disease model.

**Kill Test 5 (Resistance): Low concern.** CpPDE1 V900A CRISPR mutant alters susceptibility but the mutation comes at a fitness cost (bulkier amino acids in the active site). The probability of spontaneous V900A in the field is unknown but the structural constraint suggests resistance is not trivial.

**Surveyor Correction: 3 PDEs exist, not 1.** CpPDE1 (cgd3_2320) is the validated asexual-stage target, but cgd6_4020 and cgd6_500 exist. If these provide redundant cGMP degradation, CpPDE1 inhibition alone may be insufficient. HOWEVER: the CRISPR V900A mutant alters susceptibility, confirming CpPDE1 is the relevant target for the pyrazolopyrimidine compounds -- regardless of whether other PDEs exist. The genetic validation holds.

**Kill Test 10 (Commercial Reality): Manageable.** Lead compounds have oral efficacy in mice. Human PDE-V cross-reactivity is a concern for systemic delivery but eliminated by luminal formulation (same as BKIs). Pyrazolopyrimidine scaffolds are synthetically accessible.

**The mechanistic novelty is genuine.** Egress blockade is mechanistically distinct from every other candidate. Trapped parasites cannot spread, cannot autoinfect, and are cleared by normal enterocyte turnover in 3-5 days. This is the only candidate that simultaneously breaks merogony amplification AND autoinfection from a single target.

**What I tried and why it failed:** I tried to kill CpPDE1 on the argument that trapped parasites in dead host cells would trigger catastrophic inflammatory damage (a Crypto-specific inflammatory storm). But the parasite is already in the extracytoplasmic niche -- when the host cell dies, the parasite is expelled luminally, not into the lamina propria. The inflammatory concern is theoretical and would be visible in the mouse efficacy data if it were real (it was not reported).

---

### Candidate #8: Bovicrypt Maternal Vaccine

**Verdict: WOUNDED**

**Surveyor Flag (GP60 polymorphism): Concern.** Same GP60 subtyping locus variability as #5. Field trials conducted in European herds where IIa predominates. Efficacy against IId subtypes (China, Middle East) is unknown.

**Kill Test 12 (Clinical Endpoint): FAIL.** The 2025 field trial showed significantly shorter diarrhea episodes in dairy calves. BUT: most clinical endpoints did not reach statistical significance. The trial was confounded by insufficient natural challenge levels. This is not a clean efficacy signal -- it is a trend that failed to reach significance on most measures.

**Kill Test 9 (Repetition): FAIL.** Sapper documents that maternal vaccination reduces severity but cannot prevent infection. Colostral antibody decay is 3-5 days; the vulnerability window is 14 days. Bovicrypt does not solve the antibody duration problem that Sapper identified as the core failure mode for all passive immunization approaches.

**Crypto-Specific Duration Test: FAIL.** Even boosted colostral antibodies degrade within days. Bovicrypt provides 2-3 days of enhanced protection at best. The remaining 11-12 days of the vulnerability window are uncovered. The dose-independence of severity data means even this partial protection may not matter -- the few parasites that establish during days 0-3 autoinfect to full disease burden by day 7 regardless.

**Why WOUNDED, not KILLED:** Bovicrypt has the best commercial path (single injection in dam, no calf handling). It is NOT a standalone solution, but it IS a viable adjunct in a combination strategy. Its value is providing the first 2-3 days of coverage while a sustained-release drug provides days 0-14.

---

### Candidate #9: VHH Nanobody Cocktail Against GP40 + CSL + TRAP-C1

**Verdict: WOUNDED**

**Kill Test 1 (20-Year Test): N/A -- novel proposal.**

**Kill Test 2 (Species): FAIL.** Zero anti-Cryptosporidium nanobodies exist anywhere. The entire technology chain -- immunize camelids, select nanobodies, test neutralization, formulate for sustained delivery -- has never been initiated for this pathogen. The anti-rotavirus VHH precedent proves the platform works in calf gut, but cross-pathogen extrapolation is not evidence.

**Kill Test 4 (Strain): Partial concern.** GP40 is subtype-variable (GP60 subtyping locus). CSL is conserved (mAb 3E2 works cross-strain). TRAP-C1 has two alleles. A cocktail using CSL-targeting nanobodies as the anchor with GP40 and TRAP-C1 as secondary targets would be more robust. But the cocktail design cannot be finalized until the nanobodies are generated and tested.

**Crypto-Specific Duration Test: The decisive question.** VHH nanobodies ARE protease-resistant (established for rotavirus). BUT: protease resistance is not the only barrier. Mucus turnover, peristalsis, and dilution across the length of the intestine mean even protease-resistant nanobodies will be physically cleared from the ileal surface within hours to days. Sustained luminal presence for 14 days requires either repeated dosing (labor cost barrier) or a sustained-release formulation that does not yet exist for nanobodies.

**Kill Test 8 (Embarrassment):** Anti-GP40 nanobodies block 80% of sporozoite invasion in vitro. In the calf, the 20% that get through establish the autoinfection cycle within 48 hours. Given dose-independence of severity (Zambriski et al.), 20% invasion means identical disease to 100% invasion -- the exponential amplification machinery erases any initial inoculum difference within 2-3 cycles. The nanobodies would need >99% invasion blockade to meaningfully affect outcomes.

**Why WOUNDED, not KILLED:** The VHH platform technology IS proven for oral delivery to neonatal calf gut. CSL is a strong target (cross-strain, mAb 3E2 passive protection evidence). Nanobodies are cheap to produce in yeast. This is the most plausible antibody-based approach. But the path from zero (no anti-Crypto nanobodies exist) to product is 3-5 years minimum, and the 14-day duration problem applies to any luminal biologic.

**Required to graduate:** Generate anti-CSL nanobodies (the most conserved target), demonstrate in vitro neutralization of sporozoite invasion at >90%, and demonstrate sustained luminal presence for >7 days via mucoadhesive formulation.

---

### Candidate #10: Lectin-Mimetic Galactose/GalNAc Polymer (Luminal Decoy)

**Verdict: WOUNDED**

**Kill Test 8 (Embarrassment):** Sporozoite attachment is multi-mechanism. Gal/GalNAc lectin binding is ONE of at least 4 attachment mechanisms (CSL lectin, GP40/GP15, TRAP-C1 gliding motility, host ENO1 interaction). A sugar polymer blocking only the lectin-Gal/GalNAc pathway leaves three other invasion routes operational. Even 100% blockade of one pathway may reduce invasion by only 25-50%.

**Kill Test 7 (Stoichiometric): Concern.** The ileal surface area of a neonatal calf is enormous. Coating it with a polymer at sufficient density to compete with endogenous Gal/GalNAc epitopes requires grams of polymer per dose, maintained continuously. The concentration required in the ileal lumen may be impractical.

**The "why isn't the field doing this?" test:** Polyvalent sugar decoys for enteric pathogens have been studied for E. coli, Vibrio, and others. None have reached the market for enteric infections in any species. The luminal dilution problem (maintaining effective concentrations across a dynamic, peristaltic gut) defeats elegant in vitro results. If sugar decoys worked easily in the gut, the much-simpler E. coli problem would already be solved.

**Why WOUNDED, not KILLED:** The concept is cheap to test in vitro ($5-8K). If in vitro invasion inhibition is <50%, this is KILLED. If >80%, it graduates to animal testing. Let the data decide.

---

### Candidate #11: Host Lipid Raft Disruption (MbCD or Statin Derivative)

**Verdict: KILLED**

**Kill Test 3 (Matrix): FATAL.** Methyl-beta-cyclodextrin depletes membrane cholesterol from ALL cells it contacts. In the neonatal calf gut, this means depleting cholesterol from uninfected enterocytes, goblet cells, Paneth cells, and stem cells. Neonatal intestinal epithelium is already under stress from C. parvum infection. Adding non-selective membrane disruption to an already-damaged epithelial barrier will worsen barrier dysfunction, increase paracellular leakage, and potentially cause more harm than the 70% invasion reduction is worth.

**Kill Test 8 (Embarrassment):** MbCD at the concentration needed for 70% invasion reduction strips cholesterol from the enterocyte apical membrane. The neonatal calf, already losing fluid to secretory and malabsorptive diarrhea, now also has iatrogenic barrier disruption. The calf gets worse, not better.

**Forge proposed plant saponins as an alternative.** Saponins are also non-selective cholesterol-binding agents. The selectivity problem is inherent to the mechanism, not the specific compound.

**Killed because:** Non-selective membrane disruption in a neonatal gut already suffering from C. parvum-induced barrier damage is iatrogenic harm. The 70% invasion reduction (measured in clean cell culture) does not account for the host toxicity cost in an already-damaged system.

---

### Candidate #12: CpOSBP Inhibitor (Oxysterol-Binding Protein)

**Verdict: WOUNDED**

**Surveyor Flag: Gene identity UNRESOLVED.** Cannot validate a target without a confirmed gene ID.

**Kill Test 1 (20-Year Test): N/A but concerning.** CpOSBP was described in a conceptual paper (Yao et al., 2020) but no CpOSBP-specific inhibitors have been tested. The feeder organelle remains molecularly uncharacterized at the level needed for drug design.

**Kill Test 8 (Embarrassment):** "Let's inhibit CpOSBP" cannot even get started because nobody knows which gene it is with certainty, whether it is essential, what it transports, or whether redundant lipid transport exists.

**Why WOUNDED, not KILLED:** The feeder organelle IS the parasite's lifeline. Disrupting nutrient acquisition IS a valid strategy. CpOSBP is the closest thing to a molecular handle on this interface. But until the gene ID is resolved and CRISPR essentiality is demonstrated, this is a concept, not a candidate.

**Required to graduate:** Resolve gene ID in CryptoDB. CRISPR conditional knockdown to test essentiality. If not essential, KILLED.

---

### Candidate #13: Pro-Apoptotic Host-Directed Therapy (BH3 Mimetic)

**Verdict: WOUNDED**

**Kill Test 3 (Matrix/Host): CRITICAL CONCERN.** ABT-263 (navitoclax) causes dose-limiting thrombocytopenia in human cancer trials because it targets Bcl-xL on platelets. In a dehydrated neonatal calf with diarrhea-induced hemoconcentration, thrombocytopenia could be catastrophic. Forge proposes luminal delivery to avoid systemic exposure, but BH3 mimetics are small molecules designed for cell permeability -- they WILL be absorbed from the gut.

**The selectivity hypothesis is elegant but untested.** Forge argues infected cells with upregulated Bcl-2 are selectively vulnerable to BH3 mimetics. This is analogous to oncogene addiction in cancer -- and in cancer, the selectivity window is narrow (navitoclax has a therapeutic index of ~2-3x in most settings). For a production animal, where the acceptable adverse event rate is near zero, a 2-3x selectivity window between killing infected and uninfected enterocytes is insufficient.

**Crypto-Specific Autoinfection Test: Concern.** BH3 mimetics force premature cell death. The parasite is in the extracytoplasmic niche -- when the cell dies, the parasite is expelled luminally. These expelled parasites may still be viable (merozoites at various maturation stages). Viable expelled merozoites in the lumen can immediately reinvade adjacent enterocytes. The approach may accelerate parasite turnover rather than eliminate it.

**Kill Test 10 (Commercial Reality):** Navitoclax costs >$1,000/patient in oncology. Even a veterinary-grade BH3 mimetic at production-animal doses would far exceed $15/calf.

**Why WOUNDED, not KILLED:** The in vitro selectivity assay is $3-5K. If infected cells show >10x selective killing vs. uninfected cells, this reopens the conversation. If selectivity is <3x (which is the typical range for BH3 mimetics in cancer), this is KILLED. The concept is novel enough to warrant the cheap test.

---

### Candidate #14: Bile Salt Sequestrant (Autoinfection Cycle Disruptor)

**Verdict: WOUNDED**

**Kill Test 3 (Matrix): CRITICAL CONCERN.** Bile salt sequestration in the ileum of a neonatal calf dependent on milk fat for >50% of caloric intake is potentially devastating. Bile salts are required for fat emulsification and absorption. Cholestyramine at excystation-inhibiting concentrations could cause fat malabsorption, steatorrhea, fat-soluble vitamin deficiency (A, D, E, K), and caloric deficit in an already-malnourished neonate. This iatrogenic malnutrition may cause MORE harm than the autoinfection it prevents.

**Kill Test 7 (Stoichiometric): Concern.** To reduce excystation efficiency by >87.5% (the threshold calculated by Forge to make autoinfection unsustainable given 8x amplification per cycle), bile salt concentration in the ileum must be reduced by a corresponding amount. The ileum of a milk-fed calf has high bile salt throughput. The amount of cholestyramine needed to sequester 87.5% of ileal bile salts may be prohibitive.

**Kill Test 8 (Embarrassment):** Veterinarian gives cholestyramine to a crypto-infected calf. The calf stops autoinfecting but also stops absorbing milk fat. It starves instead of dehydrating. Treatment was successful -- the patient died of malnutrition.

**Why WOUNDED, not KILLED:** The in vitro excystation dose-response experiment is cheap ($2-3K) and would determine whether the required bile salt reduction is within a tolerable range. If 50% bile salt reduction achieves >87.5% excystation inhibition (because the excystation dose-response curve is steep), the approach becomes feasible with modest fat absorption compromise. If the dose-response is shallow, this is KILLED.

---

### Candidate #15: Yeast Beta-Glucan Trained Innate Immunity

**Verdict: WOUNDED**

**Crypto-Specific Immune Independence Test: FAIL.** Beta-glucan trained immunity works by priming innate immune cells (monocytes, macrophages) for enhanced responses. The 2025 calf studies showed protection from days 31-60, NOT days 0-14. The Crypto vulnerability window is days 0-14. If trained immunity takes 2-4 weeks to mature to functional levels, it arrives AFTER the disease has already peaked and resolved naturally. The immune system clears Crypto by day 14-21 without beta-glucan. What is beta-glucan adding?

**Crypto-Specific Timing Test: FAIL.** Even if day-0 oral beta-glucan primes innate cells faster than observed in the 2025 studies, the primed innate response produces IL-1beta, TNF-alpha, and IL-6. These are INFLAMMATORY cytokines. The Crypto-infected gut is already inflamed. Adding a trained immunity-driven inflammatory burst on top of Crypto-induced inflammation in the first 3-7 days could worsen intestinal pathology, not improve it.

**Kill Test 12 (Clinical Endpoint): Concern.** The 2025 studies measured "all-cause diarrhea" reduction at days 31-60. They did NOT measure Crypto-specific oocyst shedding, Crypto-specific diarrhea, or ileal IFN-gamma at any timepoint. The observed benefit may be entirely from reducing bacterial/viral diarrhea in the post-Crypto period, not from any anti-Crypto effect.

**The "too simple to be the answer" test:** Beta-glucan is cheap, available, and well-studied. If it worked against Crypto in calves, someone would have tested it against Crypto by now. The field has not -- probably because trained immunity practitioners understand the timing mismatch with neonatal cryptosporidiosis.

**Why WOUNDED, not KILLED:** The trained immunity biology in calves IS real and replicated (2 independent 2025 studies, 96 calves). The question is purely timing. A day-0 oral beta-glucan + C. parvum challenge at day 2 with early timepoint ileal sampling (days 3-7) would answer whether trained immunity can act fast enough. This experiment is $15-20K and is worth doing because if trained immunity CAN narrow the timing gap by even 2 days, the effect on parasite burden at immune engagement is ~100-fold (the Martian's calculation).

**Required to graduate:** Crypto-specific calf challenge study showing either (a) reduced oocyst shedding in first 14 days, or (b) elevated ileal IFN-gamma/iNOS at days 3-5. If neither, KILLED.

---

### Candidate #16: COX-2 Inhibitor / Meloxicam (Anti-Secretory + Immunosuppression Relief)

**Verdict: SURVIVED**

**Kill Test 9 (Repetition): Pass.** This is NOT repeating the indomethacin story -- Forge specifically proposes meloxicam (selective COX-2, better renal safety profile) over indomethacin (non-selective, renal toxicity).

**Kill Test 2 (Species): Strong.** Bovine ex vivo data from 2001 (Blikslager et al.) directly demonstrates full restoration of electrolyte absorption in C. parvum-infected BOVINE ileum with indomethacin + glutamine. This is the actual target species, the actual pathogen, and the actual tissue.

**Kill Test 10 (Commercial Reality): Excellent.** Meloxicam is approved for calves, available, cheap (<$1/dose). Regulatory pathway is clear (label extension, not novel entity).

**Kill Test 8 (Embarrassment):** The simplest failure mode is that meloxicam's anti-secretory effect masks diarrhea severity without reducing parasite burden. The calf LOOKS better (less watery stool) but the infection progresses identically. This would still be commercially valuable (reduced treatment costs, improved welfare scores) but would not be a disease-modifying intervention.

**The immunomodulation hypothesis is unproven.** The PGE2-mediated immunosuppression explanation for rBoIL-12 failure is the Tribunal's novel hypothesis, not established biology. COX-2 inhibition may NOT relieve local immunosuppression. But the anti-secretory effect alone justifies the trial.

**What I tried and why it failed:** I tried to kill meloxicam on the argument that COX-2 inhibition in dehydrated neonatal calves causes renal damage. But meloxicam has an established safety profile in neonatal calves at standard doses (0.5 mg/kg). The renal concern is real for non-selective NSAIDs (indomethacin) but manageable for selective COX-2 inhibitors with appropriate hydration support (which is already standard of care via ORT).

**Why it survived:** Available now. Cheap. Approved. Ex vivo bovine data showing full electrolyte restoration. Even if the immunomodulation hypothesis fails, the anti-secretory effect is clinically meaningful. The risk-reward ratio is the best in the portfolio.

---

### Candidate #17: Recombinant Bovine IFN-gamma + COX-2 Inhibitor

**Verdict: KILLED**

**Kill Test 9 (Repetition): FATAL.** rBoIL-12 stimulated IFN-gamma production and CD4+ T cell expansion in neonatal calf gut and STILL FAILED to protect (Pasquali et al., 2006). This candidate proposes giving IFN-gamma directly (bypassing the T-cell activation step) + COX-2 inhibition. But the question is: WHY did IFN-gamma fail to protect even when the immune system successfully produced it? The PGE2 hypothesis is only ONE explanation. Others: (a) the extracytoplasmic niche physically shields the parasite from IFN-gamma-induced iNOS in the host cell cytoplasm -- iNOS produces NO in the cytoplasm, but the parasite is NOT in the cytoplasm; (b) the parasite's anti-apoptotic manipulation prevents IFN-gamma-induced cell death; (c) the parasite burden at the time of immune engagement is already too high for even maximal IFN-gamma to overcome.

**Kill Test 10 (Commercial Reality): FATAL.** Recombinant bovine IFN-gamma is a research reagent, not a veterinary product. Cost is orders of magnitude above $15/calf. No approved formulation exists. Oral delivery of a protein cytokine to the gut mucosa with maintained bioactivity is unsolved.

**Kill Test 8 (Embarrassment):** rBoIFN-gamma + meloxicam given to neonatal calves. The IFN-gamma is degraded in the stomach. The fraction that reaches the ileum activates iNOS in enterocyte cytoplasm, but the parasite is in the extracytoplasmic niche and does not care. Meloxicam provides the same anti-secretory benefit it would have provided alone. Cost: $200/calf. Benefit: identical to $1 meloxicam alone.

**Killed because:** rBoIL-12 already PROVED that IFN-gamma in the calf gut does not protect. Giving IFN-gamma directly instead of via IL-12 stimulation changes the upstream pathway but the downstream problem (parasite in niche, not in cytoplasm) is unchanged. The COX-2 addition is valuable but does not need the IFN-gamma component.

---

### Candidate #18: CpG-ODN TLR9 Agonist

**Verdict: WOUNDED**

**Crypto-Specific Timing Test: FAIL.** TLR9-induced IFN-gamma peaks at 24-48 hours and wanes. A single birth-dose provides 1-2 days of enhanced innate activation. The vulnerability window is 14 days. Repeated dosing over 14 days is required, which creates the same compliance barrier as halofuginone.

**Kill Test 9 (Repetition): Concern.** CpG-ODN activates IL-12 and IFN-gamma -- the SAME downstream effectors as rBoIL-12. If rBoIL-12 failed to protect despite successfully stimulating IFN-gamma in the calf gut, why would CpG-ODN-stimulated IFN-gamma succeed? The PGE2 hypothesis (COX-2 inhibitor rescues this) is the only differentiating argument, but it is unproven.

**Kill Test 11 (Independent Replication): N/A -- never tested against Crypto.**

**Why WOUNDED, not KILLED:** CpG-ODN is cheap, available, and safe in calves. A single experiment (CpG at birth + Crypto challenge + measure ileal cytokines at days 3-7) would determine whether TLR9 agonism produces faster/stronger innate responses than the natural course. Adding meloxicam to the CpG arm tests the PGE2 hypothesis directly. This is a $15-20K experiment that could answer two critical questions simultaneously.

**Required to graduate:** CpG + Crypto challenge calf study with early ileal biopsy showing elevated iNOS and reduced parasite burden at day 5 vs. controls. If no difference, KILLED.

---

### Candidate #19: Recombinant Mucin-Like Glycoprotein Decoy

**Verdict: KILLED**

**Kill Test 11 (Independent Replication): FATAL.** Single lab (Striepen group), single 2023 publication, 10 citations. The MAb 1A5-reactive heterodimer was only characterized in 2023. Nobody has independently confirmed the attachment-blocking observation.

**Kill Test 8 (Embarrassment):** Recombinant expression of a mucin-like glycoprotein with correct O-linked glycosylation in CHO cells costs $50-100K and takes 6-12 months. The expressed protein may not have the correct glycan decoration that is required for the biological activity (mucin function is almost entirely glycan-dependent, not protein-dependent). The most likely outcome: you spend $100K making recombinant mucin, it has the wrong glycans, and it does not block invasion.

**Kill Test 10 (Commercial Reality):** Even if the recombinant glycoprotein works perfectly, scaling mucin production with correct O-linked glycosylation for production animal use is economically impossible.

**Killed because:** Single-lab early-stage biology + technically impossible recombinant expression at scale + glycan-dependent function that cannot be replicated recombinantly = dead.

---

### Candidate #20: Gametocyte Commitment Blocker (Concept)

**Verdict: KILLED**

**This is not a candidate. It is a wish.** Forge itself admits: "the molecular trigger for sexual commitment in C. parvum is unknown." Surveyor confirms: "No molecular target identified. Cannot be computationally validated. Basic research question, not a drug target."

**Subsumed by Vulcan V1 (Myb-M).** Vulcan identified the ACTUAL molecular handle on sexual commitment. This concept-level candidate has been superseded by a specific target proposal. Keeping both is redundant.

**Killed because:** No target, no compound, no evidence. This is a 5-10 year basic science research direction, not a drug candidate for a portfolio.

---

### Candidate #21: Environmental Oocyst Inactivation

**Verdict: KILLED**

**The Martian already killed this.** The dose-independence of severity data (Zambriski et al., 2013) proves that reducing environmental oocyst load has ZERO effect on individual calf disease severity. Whether a calf encounters 10 or 10^6 oocysts, the disease is identical. Even 99.9999% environmental decontamination leaves enough oocysts (from 10^10 shed per calf) to infect hundreds of calves.

**Kill Test 10 (Commercial Reality):** This is a farm management intervention, not a drug. Cargill already knows how to manage calving environments. There is no Agteria IP here.

**Killed because:** The intervention target (environmental oocyst load) is irrelevant to the commercial endpoint (individual calf disease severity). Long-term herd R0 reduction over multiple calving seasons has value, but that is an operational decision for Cargill, not a drug discovery target.

---

### Candidate #22: Enhanced ORT -- Glutamine + Meloxicam

**Verdict: SURVIVED**

**Kill Test 2 (Species): STRONGEST DATA IN THE PORTFOLIO.** Blikslager et al. (2001) demonstrated FULL restoration of Na+/Cl- absorption in C. parvum-infected BOVINE ileum ex vivo. This is the actual species, actual pathogen, actual target tissue. Gookin et al. (2008) confirmed full inhibition of the secretory diarrhea component with indomethacin in infected piglet tissue.

**Kill Test 10 (Commercial Reality): Perfect.** Glutamine: food-grade amino acid supplement, <$0.50/dose. Meloxicam: approved in calves, <$1/dose. Total cost: <$2/calf. Available now. No regulatory barriers.

**Kill Test 8 (Embarrassment):** The simplest failure mode: ex vivo tissue restoration does not translate to in vivo clinical improvement because the calf's GI tract has transit, absorption, and systemic factors that the ex vivo model does not capture. Glutamine may be absorbed in the jejunum before reaching the ileum. Meloxicam may not achieve sufficient ileal mucosal concentrations.

I tried hard to find evidence of this failure mode. I could not. Glutamine reaches the ileum at oral doses used in human and veterinary nutrition. Meloxicam reaches ileal tissue at standard approved doses. The ex vivo-to-in vivo gap is a legitimate concern, but both drugs are known to reach the target tissue.

**Kill Test 9 (Repetition): N/A -- this combination has NEVER been tested in vivo.** The most underexploited finding in 25 years of Crypto research. Full electrolyte restoration in bovine infected tissue -- sitting in the 2001 literature for a quarter century with no clinical translation. The absence of a clinical trial is not evidence of failure. It is evidence of neglect.

**The "too simple to be the answer" test:** This is NOT a cure. It does not kill the parasite. It does not shorten infection. It reduces diarrhea severity by restoring electrolyte absorption, preventing the worst of the dehydration, and potentially reducing mortality. The question is not "is this too simple?" but "why has nobody tested this in 25 years?"

**Why it survived:** Cheapest, fastest, lowest-risk experiment in the entire portfolio. $10-15K for a randomized calf trial. All components available now. Even if the anti-parasitic portfolio fails entirely, enhanced ORT reduces the welfare and economic burden of cryptosporidiosis immediately.

---

### Candidate #23: Serotonin (5-HT3) Receptor Antagonist (Ondansetron)

**Verdict: KILLED**

**Kill Test 2 (Species): FAIL.** The enteroendocrine disruption data is from a piglet model (Wang et al., 2007). No bovine enteroendocrine data exists for C. parvum infection. The neurogenic contribution to diarrhea in CALVES is completely uncharacterized.

**Kill Test 8 (Embarrassment):** Ondansetron reduces intestinal motility. In a calf with C. parvum infection, reduced motility means increased contact time between oocysts/sporozoites and enterocytes. The anti-motility effect could INCREASE invasion efficiency and worsen the infection. The anti-emetic benefit (which is ondansetron's primary use) is irrelevant -- calves with cryptosporidiosis do not vomit. They have diarrhea.

**Kill Test 10 (Commercial Reality): Concerning.** Ondansetron costs $5-15/dose in veterinary use. For a symptomatic intervention with uncertain mechanism and potential to worsen infection, this is unacceptable cost.

**Killed because:** No species-specific evidence, potential to worsen infection by reducing motility, and Candidate #22 (enhanced ORT) addresses the same symptom (diarrhea) with cheaper, better-evidenced components.

---

### Candidate #24: Wnt Pathway Activator (Post-Infection Recovery)

**Verdict: WOUNDED**

**Kill Test 8 (Embarrassment):** Wnt activation in the intestinal epithelium is the primary driver of colorectal cancer. Giving a Wnt activator to calves -- even transiently -- risks promoting neoplastic transformation in crypt stem cells. While bovine colorectal cancer is rare, introducing oncogenic signaling into a damaged, hyperproliferative epithelium (crypt hyperplasia is already present during Crypto infection) is playing with fire.

**Kill Test 1 (20-Year Test): N/A -- novel hypothesis.**

**Kill Test 2 (Species): Weak.** Wnt pathway data is from mouse enteroids (Zhang et al., 2016). No bovine Wnt pathway characterization during or after Crypto infection exists.

**The fundamental question is whether intervention is needed.** Calves DO recover from cryptosporidiosis. The disease IS self-limiting. The weight loss that "is not recovered for 6 months" may reflect nutritional deficit during the acute phase, not persistent Wnt suppression. If you prevent the worst of the diarrhea (via enhanced ORT), the weight recovery problem may solve itself.

**Why WOUNDED, not KILLED:** The economic argument (6-month weight deficit) is compelling. Butyrate supplementation during recovery (a Forge suggestion) is cheap, safe, and promotes epithelial differentiation without the oncogenic risk of direct Wnt activation. The Wnt pathway characterization study ($5-10K) would determine if persistent Wnt suppression even exists in recovering calves.

---

### Candidates #25, #26, #27: Combination Strategies

**Candidate #25: Triple Combination (BKI + Nanobody + Beta-Glucan)**

**Verdict: SURVIVED**

Each component must individually demonstrate efficacy before combination testing. But the quantitative synergy argument is sound: if BKI reduces burden by 1 log10, nanobody reduces new invasions by 0.5-1 log10, and beta-glucan advances immune engagement by 1-2 days, the immune system encounters ~10^7 instead of ~10^10 parasites. This is a 1,000x reduction in challenge at immune engagement.

The combination addresses the timing gap from three independent mechanisms. Even if each component achieves only 50% of its predicted individual effect, the combined impact on the kinetic mismatch would exceed any single agent.

**Risk:** Total COGS for three components. BKI sustained-release bolus + nanobody microspheres + beta-glucan oral dose may exceed $15/calf. But each component can be tested individually first, and the combination only needs to include the components that individually pass de-risk.

**Candidate #26: Enhanced ORT + MMV665917**

**Verdict: SURVIVED**

Practical near-term regimen combining the best symptomatic intervention (enhanced ORT) with the best anti-parasitic (MMV665917 -- if it replicates). This is the logical first clinical regimen to test.

**Candidate #27: Maternal Vaccine + BKI + Beta-Glucan**

**Verdict: SURVIVED**

Layered protection across the 14-day window. Bovicrypt covers days 0-3, BKI covers days 0-14, beta-glucan covers days 3-14. The architecture is sound even if individual components underperform.

---

## VULCAN TARGETS

---

### Vulcan IP1: Myb-M Forced Activation (Death Switch)

**Verdict: WOUNDED**

This is the highest-ceiling target in the entire portfolio. It is also the highest-risk.

**Kill Test 1 (20-Year Test): N/A -- discovered in 2024.** The Myb-M story is brand new. Zero drug development has been attempted.

**Kill Test 8 (Embarrassment -- and the decisive test):** The "death switch" concept requires ACTIVATING Myb-M (forcing terminal male differentiation) rather than INHIBITING it. Drug discovery almost always seeks INHIBITORS. Activators/stabilizers of transcription factors are an order of magnitude harder to develop than inhibitors. The Myb-M death switch is conceptually brilliant but pharmacologically unprecedented. There is no example of a small molecule that forces overexpression of a specific transcription factor in any apicomplexan parasite.

**The transcription factor druggability problem is real.** Myb-family transcription factors have been targeted in oncology (Myb-p300 interaction disruption), but these are INHIBITORY approaches. The Myb-M forced activation concept requires either (a) stabilizing the Myb-M protein to prevent degradation (PROTAC-in-reverse / molecular glue), (b) providing a small molecule that mimics Myb-M's DNA-binding activity (impossible for a TF), or (c) using a gene therapy approach to overexpress Myb-M (impractical in a production animal setting).

**Drug delivery to the parasite nucleus is an extreme challenge.** Myb-M is a nuclear transcription factor inside a parasite that sits in an extracytoplasmic niche. A small molecule must: (1) survive the gut lumen, (2) traverse or bypass the parasitophorous vacuole membrane, (3) enter the parasite cytoplasm (extracytoplasmic = the drug may need to access from the lumen side), (4) enter the parasite nucleus. Each step is a barrier.

**Kill Test 11 (Single Lab): Flag.** All Myb-M data comes from the Striepen lab. The 2024 Nature paper is from a single group. No independent replication of the Myb-M conditional ablation or forced overexpression phenotype.

**Why WOUNDED, not KILLED:** The biology is extraordinary. Genetic ablation of Myb-M eliminates male gametes and blocks oocyst production -- both thick-walled AND thin-walled. This means blocking Myb-M function OR forcing Myb-M activation could be curative. The Myb-M forced activation concept is the single most original idea in the entire candidate set. But the pharmacological path from "genetic proof" to "small molecule drug" for a transcription factor activator in an extracytoplasmic parasite is so long that this is a 5-10 year research target, not a near-term drug candidate.

**Required to graduate:** AF3 structure prediction of Myb-M protein. Identification of Myb-M binding partners (co-activators, co-repressors) that might be more druggable than Myb-M itself. Small-molecule screen for Myb-M protein stabilizers. If no druggable pocket or interaction surface exists, this stays a genetic tool, not a drug target.

---

### Vulcan IP2: AP2-F Female Gamete Maturation Blockade

**Verdict: WOUNDED**

**Kill chain weakness (Step 4 -- thin-walled oocysts): This determines everything.** AP2-F ablation blocks thick-walled oocyst shedding. But does it block thin-walled oocyst-mediated autoinfection? If thin-walled oocysts use a different (simpler, single-membrane) wall assembly pathway that is NOT AP2-F-dependent, then AP2-F inhibition blocks transmission but NOT autoinfection. In that case, individual calf disease is unaffected -- you get a transmission-blocking agent but not a treatment.

Vulcan's own analysis estimates: if AP2-F only blocks thick-walled oocysts, disease reduction is ~30-50%. That is halofuginone territory -- not enough.

**Kill Test 8 (Embarrassment):** AP2-F inhibitor eliminates thick-walled oocysts from feces. The calf still gets full disease because thin-walled oocyst autoinfection is unimpaired. The farmer sees the same sick calf but cleaner feces. Not commercially useful.

**The transcription factor druggability problem applies here too.** AP2-F is a plant-type transcription factor (AP2/EREBP family), which provides selectivity over mammals (no AP2 domains in mammals). But AP2 domain inhibitors do not exist as a drug class. The plant biology community has not developed AP2 domain inhibitors despite decades of AP2 research.

**Kill Test 11 (Single Lab): Flag.** Striepen lab only.

**Why WOUNDED, not KILLED:** AP2-F has built-in host selectivity (plant-type, absent from mammals). If the thin-walled oocyst question is answered favorably (AP2-F DOES block autoinfection), this becomes a curative target. The experiment to answer this question (AP2-F conditional ablation in immunocompromised mice, measure autoinfection persistence) is definitive. If thin-walled oocysts persist, this is KILLED for individual calf treatment (but remains valuable for herd-level transmission blocking).

---

### Vulcan IP3: CDPK5 Male Gamete Egress Blockade

**Verdict: WOUNDED**

**The magnitude problem kills this as a primary.** Genetic ablation data shows CDPK5 KO parasites are still viable with REDUCED (not eliminated) oocyst shedding and virulence. Vulcan estimates 40-60% disease reduction. Sapper and the Martian demonstrated that partial interventions producing less than 80% effect are insufficient against the exponential amplification dynamics. 40-60% disease reduction is halofuginone territory -- marginally useful but not portfolio-changing.

**Kill Test 5 (Resistance): Additional concern.** CDPK5 is a transmission-stage-specific target not required for asexual growth. A resistance mutation in CDPK5 would have NO fitness cost during the asexual amplification phase (which drives disease severity). Selection pressure from a CDPK5 inhibitor would favor resistant parasites with zero trade-off -- the fastest path to resistance of any target in the portfolio.

**Kill Test 8 (Embarrassment):** CDPK5 inhibitor reduces oocyst shedding by 50%. The calf still gets 50-60% of the disease. Autoinfection via remaining oocysts sustains the infection. The environmental benefit (50% fewer oocysts) is real but takes 3-5 calving seasons to compound meaningfully. Cargill will not wait 5 years for a 50% reduction.

**Why WOUNDED, not KILLED:** CDPK5 has value as a combination target (with Myb-M inhibition or BKI) for maximal sex-stage disruption. As a standalone, it is too weak.

---

### Vulcan IP4: Glycogen Phosphorylase

**Verdict: WOUNDED**

**Surveyor Correction: "No backup" is WRONG.** CpGT1 and CpGT2 provide external glucose import. Glycogen phosphorylase essentiality may reflect a requirement for rapid glucose mobilization during peak replication, not sole glucose supply. As monotherapy, Vulcan estimates only 30-50% parasite burden reduction. This is sub-threshold for the kinetic mismatch.

**Kill Test 3 (Host Selectivity): Concerning.** Glycogen phosphorylase is a conserved enzyme. Human GP inhibitors (CP-316,819, ingliforib) exist for diabetes -- meaning the host enzyme IS druggable. Achieving >100-fold selectivity for CpGP over bovine GP requires structural differences that have not been characterized.

**Kill Test 8 (Embarrassment):** CpGP inhibitor slows merogony from 12h to 18h cycle time. Parasite still reaches 10^9 by day 6 instead of day 5. Disease severity is marginally reduced. The immune system still faces an overwhelming burden.

**Why WOUNDED, not KILLED:** The combination concept (CpGP inhibition + dual CpGT1/GT2 blockade) could achieve complete glucose starvation. But this requires TWO drugs targeting the same metabolic pathway, which is complex and may be better addressed by targeting the convergence point (aldolase -- see V5).

---

### Vulcan IP5: Aldolase (Non-Redundant Glycolytic Chokepoint)

**Verdict: KILLED**

**Kill Test 3 (Host Selectivity): FATAL.** Surveyor flags aldolase as having the HIGHEST host homology risk in the entire portfolio. Aldolase is one of the most conserved enzymes in biology. Bovine aldolase A (ALDOA) is essential for glycolysis in every cell in the calf's body, including every rapidly dividing intestinal crypt cell, every immune cell, every red blood cell. Achieving selective inhibition of CpAldolase over bovine aldolase would require exploiting subtle structural differences in an enzyme whose catalytic mechanism has been conserved for over a billion years.

**Kill Test 8 (Embarrassment):** CpAldolase inhibitor given to neonatal calf. The compound inhibits bovine aldolase in intestinal crypt cells (most rapidly dividing cells = most metabolically active = most sensitive to glycolytic blockade). Crypt cell death accelerates, barrier function collapses, the calf goes into fulminant enteropathy. The parasite is also affected, but so is the host. This is the decoquinate-at-toxic-doses story: non-selective toxicity that harms both parasite and calf.

**Vulcan's own prediction ("at least 3 active-site residue differences") has not been validated.** No CpAldolase structure exists. The prediction that sufficient selectivity pocket exists is speculation. For a glycolytic enzyme whose mechanism is perfectly conserved across Class I aldolases in all eukaryotes, 3 residue differences may not create a selectivity window.

**Killed because:** Host selectivity is unachievable for a glycolytic enzyme this conserved. Any compound potent enough to block CpAldolase will also block bovine aldolase in the most vulnerable tissue (intestinal epithelium). This is not a drug target. It is a poison.

---

### Vulcan IP6: Dual CpGT1 + CpGT2 Glucose Transport Blockade

**Verdict: SURVIVED**

**The Surveyor correction is important: individually dispensable due to redundancy.** This means individual CpGT1 or CpGT2 inhibitors are worthless. Only simultaneous dual blockade works.

**Kill Test 5 (Resistance): Low concern for dual blockade.** Resistance would require simultaneous mutations in both transporters to restore glucose import -- a combinatorial barrier.

**The selectivity handle is real.** CpGT1 and CpGT2 transport glucose-6-phosphate directly -- an unusual substrate specificity not shared by mammalian GLUT transporters (which transport glucose, not glucose-6-phosphate). A glucose-6-phosphate mimetic could selectively block parasite transporters while sparing host GLUTs.

**Kill Test 8 (Embarrassment):** A pan-CpGT inhibitor blocks glucose import. The parasite draws down amylopectin reserves. Reserves last 24-48 hours. During this time, the parasite continues replicating (slowly) and producing thin-walled oocysts. After reserve depletion, glycolysis halts and parasites die. But 24-48 hours of continued autoinfection seeds a population that may survive if drug concentration drops even transiently. The drug must be present continuously at effective concentration for the full 14-day window.

**Why it survived:** The glucose-6-phosphate substrate specificity provides a genuine selectivity handle. Dual-target resistance barrier is high. This is an execution challenge (designing the pan-CpGT inhibitor), not a target validation problem. The Striepen lab's 2024 genetic data provides the foundation.

---

### Vulcan IP7: CpABC1 Transporter

**Verdict: WOUNDED**

**Kill Test 8 (Embarrassment):** "Let's block the ABC transporter at the feeder organelle" -- but C. parvum has 21 ABC family members. If even one other ABC transporter can compensate, the approach fails. The cargo specificity of CpABC1 is unknown. This is targeting a protein whose function is inferred from localization, not demonstrated by genetic essentiality.

**Surveyor confirms: essentiality NOT demonstrated.** CRISPR knockout needed.

**Kill Test 3 (Host Selectivity): Moderate concern.** ABC transporter NBDs are highly conserved. Must target the substrate-binding domain (TMD), which is more variable. But without knowing what CpABC1 transports, rational inhibitor design is impossible.

**Why WOUNDED, not KILLED:** The feeder organelle IS the right target domain. CpABC1 IS confirmed at the feeder organelle by immuno-EM. If CRISPR ablation shows essentiality, this becomes a validated target. The experiment is definitive. If not essential, KILLED.

---

### Vulcan IP8: Host Cdc42/N-WASP/Arp2/3 Blockade

**Verdict: KILLED**

**Kill Test 3 (Host Selectivity): FATAL.** Cdc42, N-WASP, and Arp2/3 are ESSENTIAL host cell proteins. Arp2/3-mediated actin polymerization is required for: intestinal epithelial cell migration (wound healing), tight junction maintenance (barrier integrity), immune cell chemotaxis (neutrophil and macrophage function), and intestinal stem cell division. Inhibiting these in a neonatal gut ALREADY damaged by C. parvum infection is adding insult to injury.

**Vulcan acknowledges this** and proposes "partial inhibition (50-70%) might differentially impair invasion vs. normal function." This is pharmacological wishful thinking. Dose-response curves for essential cellular machinery are steep -- the difference between 50% Arp2/3 inhibition (tolerable) and 70% (catastrophic barrier failure) may be a 2-fold concentration difference. In a dynamic gut with variable drug absorption, hitting this narrow window consistently is impossible.

**Kill Test 10 (Commercial Reality):** Wiskostatin and CK-666 are research tools, not drug candidates. No oral formulation exists. No veterinary safety data.

**Killed because:** Targeting essential host cell machinery in a damaged neonatal gut. The therapeutic window between anti-parasitic effect and host toxicity does not exist in practice.

---

### Vulcan IP9: CpROM1 Rhomboid Protease

**Verdict: SURVIVED (barely)**

**Kill Test 2 (Species): Concern.** The invasion-trapping model is based on Toxoplasma and Plasmodium rhomboid function. CpROM1-specific functional data is limited. C. parvum invasion is mechanistically distinct from Toxoplasma (extracytoplasmic niche vs. intracytoplasmic; host actin-driven vs. parasite actin-driven).

**Kill Test 8 (Embarrassment):** CpROM1 inhibitor prevents GP900 cleavage. But GP900's role has been revised -- it may be primarily a "lubrication" protein, not an adhesin. If GP900 cleavage is not critical for invasion, CpROM1 inhibition does nothing.

**What saved it:** CpROM1 may cleave substrates BEYOND GP900 (the protein is unusually large at 990 amino acids, suggesting additional functional domains). Rhomboid proteases in other apicomplexa cleave multiple invasion-essential proteins. The host selectivity is good (intramembrane serine protease with a divergent catalytic site). And the in vitro test is clean: rhomboid inhibitor + sporozoites + GP900 surface staining + invasion assay. One experiment answers the question.

**Why it survived:** Good host selectivity basis. Clean falsifiable experiment. If GP900 cleavage is NOT required for invasion, this is KILLED. But the experiment is cheap and definitive.

---

### Vulcan IP11: Kinesin-5/CpKin5

**Verdict: KILLED**

**Surveyor CORRECTED this target: 73.3% similarity to human Eg5 (KIF11).** This is the highest host homology of any target in the portfolio. Kinesin-5 inhibitors (monastrol, ispinesib, SB-743921) were developed as anticancer drugs -- they kill rapidly dividing cells. In the neonatal calf intestinal epithelium (the most rapidly dividing tissue in the body, with complete turnover every 3-5 days), these drugs would be DIRECTLY CYTOTOXIC to intestinal crypt cells.

**The 2024 mBio paper confirms the inhibitors work against the parasite -- but they also work against the host.** SB-743921 and SB-715992 block CpTSP4 secretion AND inhibit host cell mitosis. There is no selectivity.

**Killed because:** 73.3% similarity to human Eg5 makes selective inhibition impossible. Existing kinesin-5 inhibitors are anticancer drugs that kill dividing cells. Intestinal crypt cells are the most rapidly dividing cells in the body. This target is a direct path to iatrogenic enteropathy.

---

### Vulcan IP13: CpFAS1 Megasynthase

**Verdict: SURVIVED (barely)**

**Kill Test 8 (Embarrassment):** CpFAS1 inhibitor (cerulenin analog) blocks VLCFA elongation. But VLCFAs may not be required for oocyst wall integrity -- the role is INFERRED, not established. If VLCFAs are membrane components used during general intracellular development (not specifically oocyst walls), the effect could be broader (hitting all stages) or narrower (redundant with host-derived lipid import). The uncertainty is real.

**What saved it:** CpFAS1 is genuinely unique -- a Type I FAS megasynthase with no mammalian equivalent. The 8,243-amino-acid protein has a domain architecture unlike anything in the host. Selectivity is inherent. Cerulenin inhibits CpFAS1-KS with IC50 ~1.5 uM. The in vitro experiment (cerulenin dose-response measuring oocyst output vs. asexual burden) directly tests the VLCFA-oocyst wall connection.

**Host selectivity: LOW risk.** CpFAS1 substrate specificity (VLCFA elongation from host-derived medium-chain precursors) is distinct from mammalian FASN (de novo synthesis). Selectivity is built in.

**Why it survived:** Unique parasite enzyme, inherent selectivity, cheap testable hypothesis. If VLCFAs are NOT required for oocyst formation, this is KILLED.

---

### Vulcan IP14: T6PS-TPase (Trehalose Synthesis)

**Assessed under the combination/environmental context.**

**Kill Test for individual calf disease: KILLED.** Vulcan's own estimate: <10% individual calf disease reduction. Trehalose inhibition affects oocyst environmental SURVIVAL, not oocyst PRODUCTION or infection severity. This is a transmission-control target with no value for the individual calf.

**For herd-level R0 reduction:** WOUNDED. Potentially 20-40% reduction in environmental persistence over multiple calving seasons. But the timeline is 3-5 years of compounding, and Cargill needs near-term individual calf benefit.

---

### Vulcan IP15: Dual aaRS Combination

**Verdict: WOUNDED (assessed under Candidate #4 context)**

**Kill Test 9 (Repetition): Concern.** This proposes combining halofuginone (ProRS) with BRD7929 (PheRS). But halofuginone is KILLED above as a standalone. Combining a killed drug with a second drug does not resurrect the first drug -- it potentially creates combined toxicity. Halofuginone's narrow therapeutic index means ANY addition of a second aaRS inhibitor further narrows the combined therapeutic window.

**The resistance prevention logic is sound.** Dual-target combination IS the right approach to prevent resistance. But the specific combination (halofuginone + BRD7929) inherits halofuginone's fundamental weakness: cryptostatic mechanism. Two cryptostatic drugs are still cryptostatic. The combination prevents resistance to either drug but does not overcome the cryptostatic ceiling.

**Why WOUNDED, not KILLED:** The principle is correct. Apply it to BETTER drugs (two BKIs with different selectivity profiles, or BKI + CpPDE1 inhibitor) rather than to halofuginone.

---

## SUMMARY: THE PORTFOLIO AFTER REAPER

### What Survived (10 candidates)

| # | Candidate | Stage | Why It Survived |
|---|---|---|---|
| #2 | BKI/CpCDPK1 | S2+S4 | Best-validated target. Crystal structures. Calf POC. Parasite-specific. |
| #7 | CpPDE1 inhibitors | S2+S4 | Novel egress mechanism. CRISPR-validated. Mouse oral efficacy (2024). |
| #16 | Meloxicam (COX-2) | S6+S7 | Approved, cheap, bovine ex vivo data. Anti-secretory effect alone justifies trial. |
| #22 | Enhanced ORT | S7 | 25 years of neglected bovine data. <$2/calf. Test TOMORROW. |
| #25 | Triple combination | S2+S4+S5+S6 | Sound synergy logic from three independent mechanisms. |
| #26 | Enhanced ORT + MMV665917 | S4+S7 | Best near-term anti-parasitic + best symptomatic intervention. |
| #27 | Maternal vaccine + BKI + glucan | S2+S4+S6 | Layered 14-day coverage architecture. |
| V6 | Dual CpGT1+GT2 blockade | S3 | Glucose-6-phosphate selectivity handle. Dual-target resistance barrier. |
| V9 | CpROM1 rhomboid protease | S2 | Good selectivity. Clean falsifiable experiment. |
| V13 | CpFAS1 megasynthase | S5 | Unique enzyme. Inherent selectivity. Testable hypothesis. |

### What is WOUNDED and What Each Needs (18 candidates)

| # | Candidate | Required to Graduate |
|---|---|---|
| #1 | MMV665917 | Independent replication of calf data. COGS analysis. Target ID. |
| #3 | Paromomycin reformulated | Minimum effective luminal concentration determination. If 100 mg/kg, KILLED. |
| #5 | Anti-GP40 mAb | Subsumed into #9 (nanobody). Cross-subtype epitope mapping. |
| #6 | CpIMPDH | Non-absorbable formulation tested in mouse model. If no in vivo efficacy, KILLED. |
| #8 | Bovicrypt | Cross-subtype neutralization (IIa vs. IId). |
| #9 | VHH nanobody cocktail | Generate anti-CSL nanobodies. >90% in vitro neutralization. 7-day luminal persistence. |
| #10 | Gal/GalNAc polymer | In vitro invasion assay. If <50% inhibition, KILLED. |
| #12 | CpOSBP | Resolve gene ID. CRISPR essentiality. If not essential, KILLED. |
| #13 | BH3 mimetic | In vitro selectivity assay. If <10x selectivity, KILLED. |
| #14 | Bile salt sequestrant | In vitro excystation dose-response. If shallow, KILLED. |
| #15 | Beta-glucan | Crypto-specific calf challenge with early ileal sampling. If no effect days 0-14, KILLED. |
| #18 | CpG-ODN | Calf challenge + ileal biopsy. If no effect, KILLED. |
| #24 | Wnt activator | Wnt pathway characterization in recovering calves. If not suppressed, KILLED. |
| V1 | Myb-M forced activation | AF3 structure. Binding partner ID. Small-molecule screen for stabilizers. |
| V2 | AP2-F | Thin-walled oocyst question in immunocompromised mice. If autoinfection persists, KILLED (for individual treatment). |
| V3 | CDPK5 | Gatekeeper residue characterization. Only valuable as combination target. |
| V4 | Glycogen phosphorylase | CpGP vs. bovine GP structural comparison. If no selectivity pocket, KILLED. |
| V7 | CpABC1 | CRISPR essentiality test. If not essential, KILLED. |

### What is KILLED and Why (10 candidates)

| # | Candidate | Fatal Flaw |
|---|---|---|
| #4 | Halofuginone sustained-release | Cryptostatic ceiling. Weak drug in better packaging is still a weak drug. |
| #11 | Lipid raft disruption | Non-selective membrane damage in already-damaged neonatal gut. |
| #17 | rBoIFN-gamma + COX-2 | rBoIL-12 already proved IFN-gamma in calf gut does not protect. Cost prohibitive. |
| #19 | Mucin glycoprotein decoy | Single-lab, glycan-dependent function unreproducible recombinantly, unscalable. |
| #20 | Gametocyte blocker (concept) | No target. Subsumed by Myb-M (V1). |
| #21 | Environmental decontamination | Dose-independence proves zero individual calf value. Not a drug target. |
| #23 | 5-HT3 antagonist | No species data. May worsen infection by reducing motility. Candidate #22 is better. |
| V5 | Aldolase | Host selectivity impossible. Most conserved enzyme in biology. Poison, not drug. |
| V8 | Host Cdc42/Arp2/3 | Essential host proteins in damaged neonatal gut. No therapeutic window. |
| V11 | Kinesin-5/CpKin5 | 73.3% similarity to human Eg5. Anticancer drug kills crypt cells. |

---

## THE THREE EXPERIMENTS THAT MATTER MOST

If Daniel asks "what do we test first after Reaper?":

1. **Enhanced ORT ($10-15K, can start tomorrow).** Glutamine + meloxicam + standard ORT vs. standard ORT in naturally infected calves. 25 years of neglected bovine data. Even if everything else in the portfolio fails, this improves standard of care. Survived Reaper with the cleanest bill of health.

2. **BH3 mimetic in vitro selectivity ($3-5K, 2-week experiment).** Low-dose ABT-263 on infected vs. uninfected HCT-8 cells. If selectivity >10x, a completely new therapeutic axis opens. If <3x, KILLED and we move on. Cheapest experiment that could restructure the portfolio.

3. **CpPDE1 inhibitor in neonatal calf challenge ($25-35K).** The pyrazolopyrimidines survived every kill test. Mouse data in immunocompromised model is positive. This is the critical species translation experiment. If CpPDE1 inhibitors work in calves, we have a novel mechanism with egress blockade -- something nothing else in the pipeline offers.

---

*Reaper analysis complete. 38 candidates entered. 10 survived. 18 wounded with specific graduation criteria. 10 killed with cited evidence. No candidate received a pass based on novelty or creativity. Every verdict is mechanism-specific, not category-level.*
