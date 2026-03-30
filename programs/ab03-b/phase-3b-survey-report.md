# Phase 3b — Survey Report: Rumen Hydrogen Accumulation Syndrome (RHAS)

**Program:** AB03-B | **Internal Agteria Program** (no partner) | **Version:** v1
**Agent:** Surveyor | **Date:** 2026-03-30

---

## Preamble: Adapted Validation Framework

RHAS is a thermodynamic syndrome, not an infectious disease. The "pathogen" is dissolved H2. Most candidates in this portfolio are **non-protein interventions** -- small-molecule redox mediators, conductive materials, mineral electron acceptors, abiotic catalysts, and engineered organisms. The standard Surveyor workflow (BLAST conservation, host selectivity, UniProt annotation, AlphaFold structure) applies to only a subset of candidates.

For non-protein targets, I substitute the following computationally tractable assessments:

| Standard Analysis | Non-Protein Equivalent |
|---|---|
| Conservation (BLAST across strains) | **Thermodynamic universality** -- does the mechanism work regardless of microbiome composition? |
| Host selectivity (BLAST vs bovine) | **Toxicity profile** -- LD50, known adverse effects in cattle, GRAS/FDA status |
| Annotation verification | **Chemical feasibility** -- redox potential compatibility, rumen stability (pH 5.5-7.0, 39C, anaerobic), degradation kinetics |
| Structure prediction | **Reaction thermodynamics** -- delta-G calculations, dose-response modeling |
| Operon context | **Supply chain feasibility** -- cost-of-goods at production scale, sourcing |

For the 3 protein enzyme targets in the portfolio (phloroglucinol reductase, fumarate reductase, PEPCK), I perform standard protein-level validation.

---

## Forge-Vulcan Candidate Merge

### Mapping Overlaps (Independent Convergence)

| Forge Candidate | Vulcan Intervention Point | Convergence Signal |
|---|---|---|
| **1.1: Redox Mediators (Riboflavin/FMN/Quinone shuttles)** | **V1.1: Quinone-based electron acceptor for NADH** | **STRONG** -- Both independently identified quinone/flavin electron shuttles as the #1 novel target. Forge emphasized riboflavin/FMN; Vulcan emphasized naphthoquinone derivatives. SAME mechanism class. |
| **2.1: Conductive Biochar (DIET)** | **S4.1: Conductive particle-mediated DIET** | **STRONG** -- Independent convergence on DIET as a bypass of H2-dependent thermodynamic ceiling. Both propose biochar/magnetite. |
| **2.2: Magnetite Nanoparticles (DIET)** | **S4.1: Conductive particle-mediated DIET** | **STRONG** -- Same as above; magnetite is one of Vulcan's conductive particle candidates. |
| **1.2: Engineered NADH Oxidase (noxE)** | **V1.2: Extracellular NADH oxidase + V3.2: Engineered bacteria with NADH:acceptor oxidoreductase** | **MODERATE** -- Forge proposes intracellular noxE; Vulcan independently identifies the intracellular access problem and proposes V3.2 as the solution. Vulcan's analysis is more granular. |
| **6.1: Engineered Fumarate Reductase M. elsdenii** | **V1.3: PEPCK/PEPC activator (same pathway, different enzyme)** | **PARTIAL** -- Both target the propionogenesis pathway. Forge targets fumarate reductase (downstream); Vulcan targets PEPCK (upstream committed step). Complementary, not overlapping. |
| **3.2: Iron(III) Oxide** | No Vulcan equivalent | Forge-only |
| **7.1: Formate-to-Propionate Routing** | **S2.1: Formate trap (FDH enhancement)** | **STRONG** -- Both independently identify formate as a key intermediate in the hydrogen recovery gap. Vulcan's framing (NADH -> formate via FDH as thermodynamically favorable under RHAS) adds mechanistic depth. |

### Vulcan-Only Candidates (New Entries for Reaper)

| Vulcan ID | Intervention | Why Forge Missed It |
|---|---|---|
| **S3.1: Abiotic Pd/Pt Nanoparticle Catalyst** | Heterogeneous catalyst in rumen for direct H2 oxidation | Outside biological frame -- chemistry/materials science approach |
| **V1.3: PEPCK/PEPC Activator** | Small molecule activator of propionogenesis committed step | Specific enzyme target requiring enzymology knowledge |
| **V2.1: Rumen-Protected Propionate (Bypass)** | Post-ruminal propionate delivery to host | Symptom-level treatment; Forge focused on rumen-level fixes |
| **V2.2: Lactate-to-Propionate (Acrylate Pathway Activator)** | Enhance M. elsdenii acrylate pathway | Niche enzymatic target |
| **V3.1: Rnf Complex Engineering in Cellulolytic Bacteria** | Decouple NADH recycling from H2 in R. albus | Deep acetogen biochemistry |
| **V3.2: Engineered Bacteria with NADH:Acceptor Oxidoreductase** | Synthetic electron disposal pathway in engineered commensal | Combines engineered biology with quinone chemistry |
| **V4.1: Hepatic Gluconeogenesis Cofactor Supplementation** | Biotin/B12 for liver enzyme support | Host-level; low priority per Vulcan's own assessment |
| **S5: H2-Sensor Antagonist** | Block bacterial sensing of high H2 to prevent metabolic shift | Regulatory biology target, not metabolic |

**Total merged candidate count: 30** (22 Forge + 13 Vulcan - 5 overlaps = 30 unique)

---

## Summary Table

| # | Candidate | Source | Category | Chemical/Protein ID | Thermo/Conservation | Toxicity/Host Select. | Rumen Stability/Annotation | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Redox Mediators (Riboflavin/FMN) | Forge+Vulcan | NOVEL | Riboflavin CID 493570; FMN CID 643976 | E0' = -210 mV (ox/red), compatible | GRAS, vitamin B2, no toxicity at proposed doses | 99.3% rumen degradation = ACTIVE | **CONFIRMED** |
| 1.1b | Redox Mediators (Lawsone/Naphthoquinone) | Forge+Vulcan | NOVEL | Lawsone CID 6755; E0' ~ -145 mV | Redox compatible with NADH | LD50 300 mg/kg oral rat; hemolytic risk | Rumen-stable quinone | **FLAGGED** |
| 1.1c | Redox Mediators (Menadione/VitK3) | Forge+Vulcan | NOVEL | Menadione CID 4055; E0' ~ -203 mV | Redox compatible | FDA-approved feed additive; 1000x safety margin | Rumen-degraded to menaquinol; increased propionate | **CONFIRMED** |
| 1.1d | Redox Mediators (AQDS) | Forge+Vulcan | NOVEL | AQDS CID 15572; E0' ~ -184 mV | Proven electron shuttle in anaerobic systems | Limited cattle data; AQ reduced DMI 16% | Water-soluble, rumen-stable | **FLAGGED** |
| 1.2 | Engineered NADH Oxidase (noxE) | Forge+Vulcan | NOVEL | noxE UniProt A2RIB7; EC 1.6.3.4 | O2-dependent -- inactive in anaerobic rumen | N/A (biologic) | Requires O2 traces -- insufficient in rumen | **FLAGGED** |
| 2.1 | Conductive Biochar (DIET) | Forge+Vulcan | NON-OBVIOUS | Material: pyrolyzed biomass >600C | EC increases above 600C; DIET established in AD | Non-toxic feed additive; GRAS-equivalent | Stable at rumen pH/temp; not degraded | **CONFIRMED** |
| 2.2 | Magnetite Nanoparticles (DIET) | Forge+Vulcan | NOVEL | Fe3O4 CID 16211978 | Conductive; proven DIET mediator | Generally low toxicity; nanoparticle-specific concerns at high doses | Stable in anaerobic rumen conditions | **CORRECTED** |
| 3.1 | Bio-Based Succinic Acid | Forge | NON-OBVIOUS | Succinic acid CID 1110 | Endogenous rumen metabolite | Non-toxic; natural intermediate | Rapidly metabolized to propionate | **CONFIRMED** |
| 3.2 | Iron(III) Oxide / Fe(OH)3 | Forge | NOVEL | Fe(OH)3 CID 73964 | delta-G'0 = -228 kJ/mol H2 (vs -131 for CH4) | Fe(OH)3 non-toxic; Fe2+ accumulation risk at high doses | pH-sensitive: dissolves below pH 3.5, stable at rumen pH | **CONFIRMED** |
| 3.3 | Encapsulated Nitrate + Scavenger | Forge | NON-OBVIOUS | NaNO3 + Mo/W cofactors | 8 electrons/molecule; most thermodynamically favorable biological sink | Nitrite intermediate causes methemoglobinemia; Mo supplementation did NOT prevent toxicity in sheep | Encapsulation slows release; 18.5% CH4 reduction demonstrated | **FLAGGED** |
| 4.1 | Phloroglucinol | Forge | EMPIRICAL HIT A | Phloroglucinol CID 359; PGR EC 1.3.1.57 | Enzyme in Coprococcus/Eubacterium; NADPH-dependent | Non-toxic; GRAS food additive | Conflicting in vivo data: positive (Martinez-Fernandez 2017) vs negative (Maigaard 2024) | **FLAGGED** |
| 5.1 | Selective Hydrogenosome Inhibitor | Forge | NOVEL | Target: [FeFe]-hydrogenase in protozoal hydrogenosomes | Hydrogenosomes absent from Entodinium; present in Epidinium/Isotricha/Dasytricha | Selectivity crisis: [FeFe]-hydrogenases widespread in rumen bacteria | No known selective protozoal inhibitor exists | **FLAGGED** |
| 5.2 | Saponin Partial Defaunation | Forge | KNOWN | Yucca/Quillaja saponins | Reduces protozoa 30-60% | Transient effect (2-4 weeks); adaptation | Non-specific antimicrobial at higher doses | **CONFIRMED** |
| 6.1 | Engineered Fumarate Reductase M. elsdenii | Forge | NOVEL | frdABCD operon; EC 1.3.5.4 | FRD characterized in S. ruminantium membrane fraction | N/A (biologic); GMO regulatory path | M. elsdenii proven rumen colonizer (Lactipro) | **CONFIRMED** |
| 6.2 | Fumarate + Acrylate Combination | Forge | EMPIRICAL HIT A | Fumaric acid CID 444972; Acrylic acid CID 6581 | Both validated H2 sinks; in vivo propionate increase confirmed | Acrylate reduced DMI (Maigaard 2024); fumarate safe | Stoichiometric cost trap remains | **CONFIRMED** |
| 7.1 | Formate-to-Propionate Routing | Forge+Vulcan | NOVEL | FDH EC 1.17.1.9; Prevotella engineering | CO2 + NADH -> formate thermodynamically favorable under RHAS | N/A (biologic) | Formate dynamics under RHAS unmeasured | **CORRECTED** |
| 8.1 | Propylene Glycol Bridge | Forge | NON-OBVIOUS | PG CID 1030 | PG -> propionate in rumen; established physiology | FDA-approved; widely used for ketosis | Bridge only (14-21 days); not standalone RHAS treatment | **CONFIRMED** |
| S1.1 | Dose Escalation Protocol | Forge | MANAGEMENT | N/A | N/A | N/A | N/A | **CONFIRMED** |
| S1.2 | Diet Optimization | Forge | MANAGEMENT | N/A | N/A | N/A | N/A | **CONFIRMED** |
| S5.1 | Intraruminal Bolus Delivery | Forge | PLATFORM | N/A | Monensin CRC validated platform | Depends on payload | 90-120 day continuous release demonstrated | **CONFIRMED** |
| V1.3 | PEPCK/PEPC Activator | Vulcan | NOVEL | PEPCK: UniProt P22259 (S. ruminantium); EC 4.1.1.49 | 538 aa, 59.6 kDa monomer; ADP-dependent; crystal structure motifs known | No host selectivity issue (target is bacterial PEPCK) | Transcriptionally regulated by energy status; 12x higher on lactate vs glucose | **CONFIRMED** |
| V2.1 | Rumen-Protected Propionate | Vulcan | NOVEL | Calcium propionate; rumen-bypass coating | Established gluconeogenesis physiology | Non-toxic; calcium propionate FDA-approved | Requires 100-200 g/day propionate salt; large bolus | **CONFIRMED** |
| V2.2 | Lactate-to-Propionate Activator | Vulcan | NOVEL | Acrylate pathway in M. elsdenii; lactoyl-CoA dehydratase | Requires lactate substrate; RHAS =/= acidosis | N/A | Substrate (lactate) may not accumulate under RHAS | **FLAGGED** |
| V3.1 | Rnf Complex Engineering | Vulcan | NOVEL | Rnf complex from A. woodii; target: R. albus | Rnf well-characterized in acetogens | N/A (biologic) | R. albus/R. flavefaciens genetically intractable | **FLAGGED** |
| V3.2 | Engineered NADH:Acceptor Oxidoreductase + Quinone | Vulcan | NOVEL | NADH:menaquinone oxidoreductase + menadione | Selective advantage under RHAS = colonization driver | N/A (biologic + small molecule combo) | Colonization challenge mitigated by fitness advantage | **CONFIRMED** |
| V4.1 | Hepatic Gluconeogenesis Cofactors | Vulcan | NOVEL | Biotin + B12 supplementation | Problem is substrate-limited, not enzyme-limited | Safe; routine supplementation | Minimal expected impact (<5% per Vulcan) | **FLAGGED** |
| S2.1 | Formate Trap (FDH Enhancement) | Vulcan | NOVEL | FDH EC 1.17.1.9; from Cupriavidus necator | CO2 + NADH -> formate: thermodynamically favorable at high NADH | N/A | Formate accumulation under RHAS unconfirmed | **CORRECTED** |
| S3.1 | Abiotic Pd/Pt Nanoparticle Catalyst | Vulcan | NOVEL | Pd nanoparticles on alumina support | H2 + fumarate -> succinate: delta-G = -86 kJ/mol; Pd catalyzes at ambient temp | **H2S POISONING** -- rumen H2S 1000-6000 ppm; Pd is sulfide-poisoned | Catalyst deactivation in rumen is near-certain | **FLAGGED** |
| S4.1 | Synthetic IET via Conductive Particles | Vulcan | NOVEL | Magnetite/biochar/activated carbon | Same mechanism as 2.1/2.2; Vulcan adds theoretical depth | Same as 2.1/2.2 | Merged with Forge 2.1/2.2 | Merged |
| S5 | H2-Sensor Antagonist | Vulcan | NOVEL | Target: putative sensory [FeFe]-hydrogenase hyd3 in R. albus | Target identified but NOT characterized | No known ligand or binding site | Fundamental research stage; no druggable target yet | **FLAGGED** |

---

## Per-Candidate Assessments

### Candidate 1.1: Redox Mediators — Riboflavin/FMN — NOVEL [Forge+Vulcan Convergence]

**Resolved Identity:**
- Compound: Riboflavin (vitamin B2) / Flavin mononucleotide (FMN)
- PubChem CID: 493570 (riboflavin) / 643976 (FMN)
- Molecular formula: C17H20N4O6 (riboflavin); C17H21N4O9P (FMN)
- MW: 376.4 (riboflavin); 456.3 (FMN)
- Resolution notes: Non-protein small molecule. No BLAST/conservation analysis applicable. Validated as redox shuttle.

**Thermodynamic Compatibility (replaces Conservation):**
- FMN midpoint reduction potential: E0' = -210 mV (two-electron, oxidized/hydroquinone)
- One-electron potentials: E0'(ox/SQ) = -314 mV; E0'(SQ/HQ) = -124 mV
- NADH/NAD+ couple: E0' = -320 mV
- H+/H2 couple: E0' = -414 mV
- **Assessment:** FMN sits between NADH (-320 mV) and H+/H2 (-414 mV) in its one-electron ox/SQ couple (-314 mV). This means NADH can reduce FMN to semiquinone. However, the SQ/HQ couple at -124 mV is much more positive than NADH, meaning the full two-electron reduction is thermodynamically favorable from NADH. The two-electron midpoint (-210 mV) is more positive than NADH (-320 mV), so electron transfer from NADH to riboflavin/FMN is thermodynamically favorable (delta-E = +110 mV, delta-G = -21 kJ/mol per pair of electrons transferred).
- **Critical insight:** Rumen bacteria possess NADH dehydrogenases (including Na+-NQR in some species) that naturally use FMN as a cofactor. Riboflavin shuttling via non-specific NADH dehydrogenases is thermodynamically feasible.
- Evidence: [COMPUTATIONAL -- redox potential values from published electrochemistry]

**Rumen Stability (replaces Annotation):**
- 99.3% of supplemented riboflavin disappeared before the duodenal cannula in dairy cows
- This is NOT instability -- it represents ACTIVE UTILIZATION by rumen microbes. Riboflavin is rapidly taken up and metabolized, which is the desired mechanism of action.
- Rumen microbial riboflavin synthesis is associated with dietary carbohydrate availability
- **Assessment:** Riboflavin's rapid rumen uptake is a FEATURE, not a bug. It means rumen bacteria actively import and use it. The question is whether exogenous riboflavin at supra-physiological doses (10-50 mg/cow/day vs. ~5-15 mg/day endogenous synthesis) can act as an electron shuttle rather than being sequestered into normal vitamin metabolism.
- Evidence: [COMPUTATIONAL/LITERATURE -- Castagnino et al. 2017, J. Dairy Sci.]

**Toxicity Profile (replaces Host Selectivity):**
- Riboflavin: GRAS (Generally Recognized As Safe); water-soluble vitamin; essentially non-toxic at any practical dose
- FMN: Endogenous cofactor in all organisms; no toxicity concern
- Cost: Riboflavin ~$15/kg; at 10-50 mg/cow/day = $0.0002-0.001/day (essentially free)
- Risk: LOW
- Evidence: [ESTABLISHED -- FDA GRAS status; NAS Vitamin Tolerance of Animals]

**Dose-Response Modeling:**
- At 10-50 mg/cow/day riboflavin: rumen concentration ~0.5-2.5 uM (in ~100L rumen volume)
- Comparable to effective shuttle concentrations in anaerobic bioreactors (1-100 uM)
- Catalytic turnover means each molecule shuttles many electrons before degradation
- **Assessment:** Dose range is plausible. Whether micromolar riboflavin can outcompete normal vitamin sequestration pathways for the electron shuttle function is the KE#1 question.

**Verdict: CONFIRMED**
- Thermodynamics support electron shuttle function from NADH. Safety is beyond question (it's a vitamin). Cost is negligible. The key unknown is whether exogenous riboflavin at achievable rumen concentrations will preferentially act as a redox shuttle rather than being channeled into normal vitamin metabolism. This is testable in RUSITEC.
- **Wet-lab confirmation type:** RUSITEC with graded riboflavin/FMN concentrations (0, 5, 25, 100, 500 uM) under 50% methanogenesis inhibition. Primary endpoint: dissolved H2, total VFA. Secondary: NADH/NAD+ ratio in rumen fluid.

---

### Candidate 1.1b: Redox Mediators — Lawsone (2-Hydroxy-1,4-Naphthoquinone) — NOVEL [Forge+Vulcan Convergence]

**Resolved Identity:**
- Compound: Lawsone (2-hydroxy-1,4-naphthoquinone)
- PubChem CID: 6755
- Molecular formula: C10H6O3
- MW: 174.2
- EC number: N/A (substrate, not enzyme)
- Resolution notes: Non-protein small molecule. Natural product from henna (Lawsonia inermis).

**Thermodynamic Compatibility:**
- Naphthoquinone midpoint potential: E0' ~ -145 mV (estimated from quinone/hydroquinone couple)
- Menaquinone (structural analog): Em(Q/Q.-) = -260 mV
- **Assessment:** Lawsone's redox potential sits well positive of NADH (-320 mV), making NADH -> lawsone reduction thermodynamically favorable (delta-E ~ +175 mV). As a quinone, it can accept two electrons in a two-step reduction. Rumen bacteria possess broad-substrate NADH dehydrogenases capable of reducing exogenous quinones (proven by anthraquinone data).
- Evidence: [COMPUTATIONAL -- redox potential estimates from published quinone electrochemistry]

**Toxicity Profile:**
- **CONCERN:** LD50 = 300 mg/kg oral in rats. More toxic in vivo than menadione.
- Causes hemolytic anemia of oxidative nature at high doses (redox cycling generates ROS)
- Produces mitochondrial dysfunction in yeast (Saccharomyces cerevisiae)
- Renal damage reported in 13-week rat studies
- At proposed micromolar doses (10-50 uM in rumen fluid): total mass ~0.2-1.0 mg/cow/day. This is 5-6 orders of magnitude below the LD50 dose for a 600 kg cow. However, hemolytic potential at chronic low doses is unknown.
- **Assessment:** Toxicity risk is real at pharmacological doses but the proposed doses are extremely low (micromolar). The safety margin may be sufficient, but the hemolytic anemia signal requires explicit dose-finding toxicity study in cattle.
- Risk: MODERATE
- Evidence: [COMPUTATIONAL -- PubChem toxicity data; EU SCCP opinion on lawsone]

**Rumen Stability:**
- Quinones are generally stable under anaerobic conditions (not oxidized by O2)
- Lawsone is a natural product in plant materials; rumen bacteria can reduce it
- **Assessment:** Stable in rumen environment; actively reduced by microbial enzymes = desired mechanism

**Verdict: FLAGGED**
- Thermodynamics are excellent. Electron shuttling function is supported by anthraquinone analogy. But the hemolytic anemia potential is a material safety concern that must be resolved before in vivo testing. Recommend in vitro hemolysis assay with bovine red blood cells at proposed rumen concentrations before advancing.
- **Wet-lab confirmation type:** In vitro hemolysis assay (bovine RBC + lawsone at 1, 10, 50, 100 uM) AND RUSITEC dose-response under methanogenesis inhibition.

---

### Candidate 1.1c: Redox Mediators — Menadione (Vitamin K3) — NOVEL [Forge+Vulcan Convergence]

**Resolved Identity:**
- Compound: Menadione (2-methyl-1,4-naphthoquinone; vitamin K3)
- PubChem CID: 4055
- Molecular formula: C11H8O2
- MW: 172.2

**Thermodynamic Compatibility:**
- Menaquinone Em(Q/Q.-) = -260 mV (one-electron); two-electron midpoint ~ -203 mV
- NADH (-320 mV) -> menadione (-203 mV): thermodynamically favorable (delta-E = +117 mV)
- **Assessment:** Excellent redox potential match. Menadione is the endogenous quinone in many rumen bacteria's electron transport chains (as menaquinone/MK). Bacteria possess NQO1-type two-electron quinone reductases that detoxify menadione via safe two-electron reduction to menaquinol.

**Toxicity Profile:**
- FDA-approved as animal feed additive (menadione sodium bisulphite, MSB)
- EFSA safety assessment: acute toxicity reached at levels exceeding dietary requirement by factor of at least 1,000
- In dairy cows: 200 mg/day menadione increased propionate molar ratio -- directly relevant to RHAS
- No reported cases of toxicity from menadione in livestock at supplemental levels
- Risk: LOW at feed-additive doses
- Evidence: [ESTABLISHED -- EFSA 2014 safety opinion; FDA vitamin K substances guidance]

**Rumen Stability:**
- Menadione is reduced to menaquinol by rumen bacteria (NQO1-type reductases)
- This reduction IS the electron shuttle mechanism. Menaquinol can then donate electrons to alternative acceptors.
- **Critical finding:** 200 mg/day VK3 INCREASED PROPIONATE MOLAR RATIO in dairy cows. This is direct evidence of enhanced propionogenesis via menaquinone-mediated electron shuttling.

**Verdict: CONFIRMED**
- Menadione is the strongest candidate in the redox mediator class. It has: (1) correct redox potential, (2) FDA/EFSA safety approval as a feed additive, (3) existing cattle data showing propionate increase at 200 mg/day, (4) bacterial enzymes (NQO1) for safe two-electron reduction, (5) commodity pricing. The propionate-increasing effect in dairy cows is already partial proof-of-concept for the electron shuttle mechanism under normal rumen conditions. Testing under RHAS conditions (with methanogenesis inhibition) is the clear next step.
- **Wet-lab confirmation type:** RUSITEC with menadione (0, 50, 200, 600 mg/day equivalent) under 50% methanogenesis inhibition. Primary endpoint: dissolved H2, propionate, total VFA.

---

### Candidate 1.1d: Redox Mediators — AQDS (Anthraquinone-2,6-Disulfonate) — NOVEL [Forge+Vulcan Convergence]

**Resolved Identity:**
- Compound: Anthraquinone-2,6-disulfonate (AQDS)
- PubChem CID: 15572
- Molecular formula: C14H6Na2O8S2
- MW: 412.3

**Thermodynamic Compatibility:**
- AQDS midpoint potential: E0' ~ -184 mV (AQDSox/AQDSred couple)
- NADH (-320 mV) -> AQDS (-184 mV): thermodynamically favorable (delta-E = +136 mV)
- Proven electron shuttle in anaerobic digestion systems; triggers mediated interspecies electron transfer (MIET)
- **Assessment:** Strong thermodynamic match. AQDS is the model compound for humic acid electron shuttling.

**Toxicity Profile:**
- Parent compound anthraquinone (AQ): reduced DMI by 16% in cattle (Mohammed et al. 2004)
- AQ also reduced methane 59% in beef heifers but with significant DMI depression
- AQDS is more water-soluble than AQ (sulfonate groups), which may reduce non-specific membrane disruption
- **Assessment:** The DMI reduction with AQ is a serious concern. AQDS may have different toxicity profile due to water solubility, but no cattle-specific data exists.
- Risk: MODERATE-HIGH (DMI depression precedent)

**Rumen Stability:**
- Water-soluble, stable under anaerobic conditions
- Not adsorbed to feed particles (unlike AQ, which is hydrophobic)
- Remains in aqueous phase -- may improve bioavailability vs AQ

**Verdict: FLAGGED**
- Excellent thermodynamics and proven electron shuttle function. But the DMI depression seen with parent compound anthraquinone in cattle is a material concern. AQDS should be tested alongside riboflavin and menadione in RUSITEC, but with explicit DMI proxy monitoring (substrate disappearance). If it shows DMI suppression even in vitro, deprioritize.
- **Wet-lab confirmation type:** RUSITEC dose-response with substrate disappearance monitoring as DMI proxy.

---

### Candidate 1.2: Engineered NADH Oxidase (noxE from L. lactis) — NOVEL [Forge+Vulcan]

**Resolved Identity:**
- Gene: noxE | Protein: UniProt A2RIB7 (NADH oxidase, L. lactis subsp. cremoris)
- EC: 1.6.3.4 (NADH oxidase, H2O-forming)
- Organism: Lactococcus lactis subsp. cremoris
- Sequence length: 451 aa
- Resolution notes: Well-characterized protein. Structural and functional data available.

**Critical Feasibility Assessment:**
- noxE is a water-forming NADH oxidase: NADH + H+ + 1/2 O2 -> NAD+ + H2O
- **The rumen is anaerobic.** O2 concentration in rumen fluid is essentially zero except for trace amounts entering via saliva and feed.
- noxE activity was confirmed as inactive in the absence of oxygen in L. lactis
- Vulcan independently identified this as "the intracellular access problem" and rated extracellular enzyme delivery as LOW magnitude (<10%)
- The alternative (couple noxE to fumarate reductase intracellularly) requires engineering two enzyme systems in a rumen commensal -- feasible in principle but complex

**Annotation Check:**
- Claimed function: Direct NADH -> NAD+ oxidation -> Verified: Yes, but O2-dependent
- Claimed applicability in rumen: -> **CORRECTED: noxE requires O2 as terminal electron acceptor; not functional in anaerobic rumen**
- An O2-independent NADH oxidase with alternative electron acceptor would be needed
- Evidence: [COMPUTATIONAL -- UniProt A2RIB7; Tachon et al. 2010, Appl. Environ. Microbiol.]

**Verdict: FLAGGED**
- The core mechanism (NADH oxidation) is valid, but noxE specifically is O2-dependent and therefore non-functional in the anaerobic rumen. The concept should be redirected toward: (a) NADH:acceptor oxidoreductases that use quinones or other non-O2 acceptors (see V3.2), or (b) expressing fumarate reductase alongside NADH oxidase for an intracellular electron disposal pathway. Vulcan's V3.2 is the corrected version of this concept.
- **Wet-lab confirmation type:** If pursuing, test alternative NADH:acceptor oxidoreductases (not noxE) in anaerobic batch culture.

---

### Candidate 2.1: Conductive Biochar (DIET Mechanism) — NON-OBVIOUS [Forge+Vulcan Convergence]

**Resolved Identity:**
- Material: Pyrolyzed biomass (pine, hardwood, or agricultural waste)
- Pyrolysis temperature: 500-700C (conductivity increases significantly above 600C)
- Particle size: target 0.5-2 mm (fiber mat retention)
- Not a single chemical entity -- a material with defined physical properties

**Thermodynamic/Physical Feasibility:**
- DIET mechanism: electrons flow from fermentative bacteria through conductive biochar surface to electron-accepting partners (propionate producers, acetogens)
- Biochar electrical conductivity: increases dramatically with pyrolysis temperature above 600C; mechanism is "discontinuous electron hopping"
- DIET has been established in anaerobic digester systems with biochar: shortened lag time for propionate degradation by 20.5% and butyrate by 9.1%
- Genera capable of extracellular electron transfer (Geobacter, Sphaerochaeta, Sporanaerobacter) enriched in presence of biochar in anaerobic digesters
- **Critical unknown:** Whether rumen bacteria (Selenomonas, Prevotella, Ruminococcus) can perform DIET. These are NOT Geobacter. No rumen-specific DIET data exists.
- Evidence: [COMPUTATIONAL/LITERATURE -- multiple anaerobic digestion studies reviewed]

**Toxicity Profile:**
- Biochar is recognized as a safe feed additive in cattle; multiple feeding studies with no adverse effects
- No effect on silage quality or in vitro rumen fermentation parameters
- Rumen-stable; not degraded in rumen fluid
- Risk: LOW
- Evidence: [ESTABLISHED -- Schmidt et al. 2019, Anim. Feed Sci. Technol.; multiple feeding trials]

**Rumen Stability:**
- Biochar is chemically inert at rumen pH (5.5-7.0) and temperature (39C)
- Particles sized >0.5 mm retained in fiber mat; not washed out with liquid phase
- Not metabolized by rumen microbes
- **Assessment:** Stable platform. Physical retention in rumen is achievable with particle sizing.

**Cost Assessment:**
- Biochar: $0.30-1.00/kg
- At 50-200 g/cow/day: $0.02-0.20/day
- Commercially viable if effective

**Verdict: CONFIRMED**
- Physical and chemical properties are suitable. Non-toxic, rumen-stable, cheap. The ONLY question is whether DIET operates in the rumen with rumen-specific bacteria. This is the KE#1 question for this candidate. The control experiment (conductive vs. non-conductive biochar at same particle size) is the critical test.
- **Wet-lab confirmation type:** RUSITEC with conductive biochar (>600C pyrolysis) vs. non-conductive biochar (<400C pyrolysis) at same loading under methanogenesis inhibition. Measure dissolved H2, VFA profile, propionate. Conductivity-dependent H2 reduction = DIET evidence.

---

### Candidate 2.2: Magnetite (Fe3O4) Nanoparticles (DIET) — NOVEL [Forge+Vulcan Convergence]

**Resolved Identity:**
- Compound: Magnetite (Fe3O4)
- PubChem CID: 16211978
- MW: 231.5
- Crystal structure: Inverse spinel

**Thermodynamic/Physical Feasibility:**
- Magnetite is conductive (band gap ~0.1 eV) and facilitates DIET in anaerobic digesters (Kato et al. 2012, Science)
- Acts as a conduit: fermentative bacteria donate electrons to magnetite surface; accepting partners (propionogenesis bacteria) receive electrons from the other side
- Catalytic -- not consumed in the process
- **Assessment:** Same DIET mechanism as biochar but with defined and consistent conductivity. Higher conductivity than biochar per unit mass.

**Toxicity Profile:**
- Magnetite nanoparticles: "generally low toxicity to humans and ecosystem" per multiple reviews
- Nanoparticle-specific concerns exist: oxidative stress, inflammatory responses reported in rats at 1-5 mg/kg doses
- However, these are for systemic (intravenous) exposure. Oral exposure in the rumen is different -- rumen is an external compartment; particles >20 nm are not absorbed across rumen epithelium
- Nano-mineral supplements (including iron oxide) have been used in cattle at low doses for nutritional supplementation
- **Assessment:** At proposed doses (5-50 g/L rumen fluid = substantial mass), the nanoparticle safety profile needs explicit evaluation. Particle size >50 nm recommended to minimize absorption risk.
- Risk: MODERATE (nanoparticle-specific; dose-dependent)
- Evidence: [COMPUTATIONAL -- review of nanoparticle toxicology literature]

**Rumen Stability:**
- Fe3O4 is stable at rumen pH (5.5-7.0) -- does not dissolve
- Stable under anaerobic conditions
- High density (5.2 g/cm3) -- particles will settle in ventral rumen; may need to be size-optimized for fiber mat retention or continuous resuspension

**Verdict: CORRECTED**
- Forge claimed Fe3O4 acts "catalytically" and is "not consumed." This is correct for the DIET mechanism but understates the practical challenge: at 5 g/L rumen fluid (Vulcan's proposed concentration), that's ~500 g of magnetite per cow. At rumen turnover of 48h, continuous re-dosing is needed. The mass/cost may be manageable if delivered via slow-release bolus.
- Correction: the dose proposed by Vulcan (5 g/L) may be excessive. Start screening at 0.1-1 g/L and establish minimum effective concentration.
- **Wet-lab confirmation type:** Batch culture dose-response (0.1, 0.5, 1, 5 g/L magnetite) under methanogenesis inhibition. Compare to biochar. Include non-conductive SiO2 nanoparticles as surface-area control.

---

### Candidate 3.1: Bio-Based Succinic Acid — NON-OBVIOUS [Forge]

**Resolved Identity:**
- Compound: Succinic acid (butanedioic acid)
- PubChem CID: 1110
- MW: 118.1
- pKa: 4.21, 5.64

**Thermodynamic Feasibility:**
- Succinate enters propionate pathway directly: succinate -> succinyl-CoA -> methylmalonyl-CoA -> propionyl-CoA -> propionate
- Succinic acid is a natural rumen intermediate (endogenous concentrations ~1-5 mM)
- Each succinate molecule accepts 0 additional electrons (unlike fumarate which accepts 2[H] in fumarate -> succinate); succinate is DOWNSTREAM of the electron-accepting step
- **CORRECTION:** Forge claims succinate "serves as both an electron acceptor (when produced from fumarate reduction)." This is imprecise. Succinate itself does NOT accept electrons -- it is the PRODUCT of fumarate reduction. Supplementing succinate provides a propionate precursor but NOT an H2 sink. The electron acceptance occurs at the fumarate -> succinate step, which requires fumarate, not succinate.
- **Assessment:** Succinic acid is a propionate precursor, not an electron acceptor. It addresses the VFA profile (propionate deficit) but NOT the H2 accumulation problem directly. It bypasses the fumarate reductase step entirely.

**Toxicity Profile:**
- Non-toxic; natural metabolite; GRAS
- Risk: LOW

**Cost Assessment:**
- Bio-based succinic acid: approaching $0.50-1.00/kg
- At 50-100 g/cow/day: $0.03-0.10/day
- Borderline economically viable

**Verdict: CONFIRMED (but mechanism corrected)**
- Succinic acid is a valid propionate precursor that addresses the VFA profile shift (Stage 4) but does NOT directly sink H2 (contra Forge's claim). It is a symptomatic treatment for propionate deficit, not a causal treatment for H2 accumulation. Still useful in the portfolio as a propionate booster, but should not be counted as an H2 disposal candidate.
- **Wet-lab confirmation type:** RUSITEC with graded succinate + 3-NOP. Measure propionate (should increase) AND dissolved H2 (should NOT decrease if mechanism correction is right).

---

### Candidate 3.2: Iron(III) Oxide / Fe(OH)3 — NOVEL [Forge]

**Resolved Identity:**
- Compound: Ferric hydroxide / iron(III) oxide-hydroxide
- Formula: Fe(OH)3 / FeOOH
- MW: 106.9 (Fe(OH)3)
- PubChem CID: 73964

**Thermodynamic Feasibility:**
- Fe(OH)3 + 1/2 H2 -> Fe(OH)2 + H2O
- delta-G'0 = -228 kJ/mol H2 for iron(III) reduction (per search results from anaerobic digestion literature)
- This is MORE favorable than methanogenesis (-131 kJ/mol) by nearly 2x
- Iron-reducing bacteria (Geobacter, Shewanella) can use Fe(III) as terminal electron acceptor
- Iron-reducing bacteria ARE present in the rumen, though at low abundance
- **Assessment:** Thermodynamics are extremely favorable -- Fe(III) reduction is one of the most exergonic H2 disposal reactions available. The question is whether rumen iron-reducing bacteria can be activated sufficiently.

**Mass/Dose Calculation (Forge's Analysis Verified):**
- 1 electron per Fe3+ reduced to Fe2+
- Fumarate accepts 2 electrons per molecule (MW 116); equivalent Fe(OH)3 dose for same electron acceptance: ~3x mass
- To replace 100g fumarate's electron-accepting capacity: ~300-550g Fe(OH)3/day
- At $0.10-0.50/kg: $0.03-0.28/day
- **Assessment:** High mass dose but potentially affordable. Palatability and physical handling are concerns.

**Toxicity Profile:**
- Fe(OH)3: insoluble, non-toxic at moderate doses
- Fe2+ product: soluble; can be toxic at high concentrations (oxidative stress)
- Normal rumen iron: 50-100 ppm; adding 300-550g Fe(OH)3 to 100L rumen = ~50-100 g Fe / 100L = 500-1000 ppm total Fe (if fully dissolved after reduction)
- This is 5-10x normal rumen iron levels
- **Assessment:** Fe2+ accumulation is a real concern at the mass doses needed. Need to monitor Fe2+ in rumen fluid and systemic iron status.
- Risk: MODERATE
- Evidence: [COMPUTATIONAL -- stoichiometric calculation + iron toxicity literature]

**Rumen Stability:**
- Fe(OH)3 is insoluble at rumen pH (5.5-7.0); does not dissolve
- Stable under anaerobic conditions (anaerobic = Fe(III) persists until biologically reduced)
- High density: will settle; may need suspension strategy

**Verdict: CONFIRMED**
- Thermodynamics are the strongest of any candidate in the portfolio. The challenge is mass dose and Fe2+ accumulation. Worth testing in batch culture at graded doses to establish the dose-response for H2 reduction and Fe2+ accumulation kinetics.
- **Wet-lab confirmation type:** Batch culture with rumen fluid + 3-NOP + graded Fe(OH)3 (1, 5, 10, 50 g/L). Measure dissolved H2, Fe2+ concentration, total VFA, microbial viability.

---

### Candidate 3.3: Encapsulated Nitrate + Nitrite Scavenger — NON-OBVIOUS [Forge]

**Resolved Identity:**
- Active: Sodium nitrate (NaNO3) in slow-release encapsulation
- Co-factor: Molybdenum/tungsten cofactor precursors (nitrite reductase cofactors)
- Encapsulation: Ethylcellulose or similar rumen-stable polymer

**Thermodynamic Feasibility:**
- NO3- -> NO2- -> NH3: accepts 8 electrons total
- Most electron-dense biological H2 sink known
- Confirmed to DECREASE dissolved H2 by 30% while reducing methane 75% (Martinez-Fernandez et al. 2017)
- Encapsulated nitrate demonstrated 18.5% methane reduction in grazing steers (Front. Microbiol. 2019)

**Toxicity Profile:**
- **CRITICAL SAFETY CONCERN:** Nitrite (NO2-) intermediate causes methemoglobinemia
- MetHb > 30% is clinically dangerous; > 70% is lethal
- Encapsulation mitigates but does NOT eliminate risk -- variable intake patterns create unpredictable nitrite spikes
- **Molybdenum co-factor strategy:** "Manipulating the rumen environment by sulfur and molybdenum balance did NOT control methemoglobin formation in sheep" -- the Forge-proposed nitrite scavenger strategy has been tested and FAILED in sheep
- Risk: HIGH
- Evidence: [ESTABLISHED -- van Zijderveld et al. 2010; Hegarty et al. 2016; Mo/S balance study in sheep]

**Verdict: FLAGGED**
- The biology is excellent (most efficient biological H2 sink), but the nitrite safety concern is fundamentally unresolved. The specific Mo/W cofactor co-formulation strategy proposed by Forge has been tested as Mo supplementation in sheep and failed to prevent methemoglobinemia. This candidate carries irreducible safety risk. Even slow-release formulations cannot guarantee safety in all feeding scenarios (variable intake, gorge feeding, etc.).
- **Wet-lab confirmation type:** If pursued, would require continuous blood MetHb monitoring in cattle with worst-case intake simulation. High regulatory burden.

---

### Candidate 4.1: Phloroglucinol — EMPIRICAL HIT A [Forge]

**Resolved Identity:**
- Compound: Phloroglucinol (1,3,5-trihydroxybenzene)
- PubChem CID: 359
- MW: 126.1
- Target enzyme: Phloroglucinol reductase (EC 1.3.1.57)
  - Gene: phlB (in Coprococcus/Eubacterium)
  - Known accessions: UniProt P57793 (E. oxidoreducens), U2C7W9 (Clostridium sp.)
  - Enzyme MW: 78-130 kDa depending on organism (homodimer or homotetramer)
  - Cofactor: NADPH (not NADH)
  - Km for phloroglucinol: 0.00003-0.8 mM (highly variable by organism)
  - pH optimum: 7.4-7.8 (compatible with rumen pH)
  - Temp optimum: 40C (compatible with rumen temperature 39C)

**Conservation of Target Enzyme:**
- Phloroglucinol reductase identified in: Coprococcus sp. Pe15, Eubacterium oxidoreducens, Clostridium sp., Desulfosporosinus orientis
- These are rumen-associated organisms; Coprococcus is present in cattle rumen microbiome
- **Key concern:** Coprococcus abundance varies with diet and animal. The Maigaard (2024) negative result may reflect insufficient Coprococcus populations in the test animals.
- Evidence: [COMPUTATIONAL -- BRENDA enzyme database; Krumholz & Bryant 1986, Appl. Environ. Microbiol.]

**Mechanism Assessment:**
- Phloroglucinol is reduced to dihydrophloroglucinol by NADPH-dependent PGR
- Dihydrophloroglucinol is cleaved to 3-hydroxy-5-oxohexanoic acid, then oxidized to triacetic acid
- End products: 2 acetate + 2 CO2 per phloroglucinol
- H2 is consumed indirectly: the NADPH used to reduce phloroglucinol must be regenerated, and H2 can serve as the electron donor for NADP+ reduction via hydrogenase
- **Critical note:** The H2 capture mechanism requires a coupled hydrogenase that regenerates NADPH from H2. This coupling may explain the variable results -- it depends on the H2/NADPH-coupled hydrogenase activity in the specific microbial community.

**Conflicting Evidence:**
- POSITIVE: Martinez-Fernandez et al. (2017): 8 Brahman steers, chloroform + phloroglucinol = decreased H2, shifted fermentation
- POSITIVE: Romero et al. (2024): Asparagopsis + phloroglucinol in goats = 68.1% H2 emission decrease
- POSITIVE: Huang et al. (2023): in vitro, phloroglucinol + BES = 72% H2 decrease after 3 sequential incubations
- **NEGATIVE:** Maigaard et al. (2024): in vivo pulse-dosing in dairy cows on 3-NOP = NO effect; "phloroglucinol seemed not to be metabolized in the rumen"
- **Discrepancy analysis:** Maigaard used 7-day periods with pulse-dosing through fistula. Martinez-Fernandez used 16 days + 21 days chloroform adaptation (37 total days). Huang used 3 sequential incubations showing progressive improvement. This pattern suggests ADAPTATION TIME is critical -- the Coprococcus population needs to expand in response to phloroglucinol availability. 7-day periods with pulse dosing may be insufficient.

**Toxicity Profile:**
- GRAS as food additive (antispasmodic use in humans at 250 mg/dose)
- Non-toxic in cattle at tested doses
- Risk: LOW

**Verdict: FLAGGED**
- The mechanism is sound and the enzyme biochemistry is favorable (pH, temperature optima match rumen conditions). But the Maigaard (2024) negative in vivo result creates material uncertainty. The adaptation time hypothesis is the most parsimonious explanation for the discrepancy, but it is UNTESTED. Resolution of this discrepancy is one of the most important experiments in the entire portfolio.
- **Wet-lab confirmation type:** Continuous dietary phloroglucinol supplementation (not pulse-dosing) for 21+ days in RUSITEC under methanogenesis inhibition. Monitor Coprococcus/phloroglucinol-degrading bacteria abundance over time (qPCR for phlB gene).

---

### Candidate 5.1: Selective Hydrogenosome Inhibitor — NOVEL [Forge]

**Resolved Identity:**
- Target: [FeFe]-hydrogenase and/or PFOR in protozoal hydrogenosomes
- Organisms: Epidinium, Isotricha, Dasytricha (hydrogenosome-containing rumen protozoa)
- **NOTE:** Hydrogenosomes are ABSENT from Entodinium (the most abundant rumen ciliate) and Diploplastron
- This means the target is limited to a subset of rumen protozoa

**Selectivity Assessment:**
- [FeFe]-hydrogenases are present in BOTH protozoa and bacteria in the rumen
- Epidinium dominated [FeFe]-hydrogenase gene reads in rumen metagenomes, suggesting protozoa are major H2 producers via this enzyme
- PFOR (pyruvate:ferredoxin oxidoreductase) is also widespread in rumen bacteria
- **Assessment:** No selectivity window exists between protozoal and bacterial [FeFe]-hydrogenases or PFOR based on available sequence data. Any inhibitor targeting these enzymes would affect bacterial fermentation (which would WORSEN RHAS by reducing fermentation capacity).
- Nitroimidazoles (the known hydrogenosome inhibitors) are BANNED in food-producing animals (carcinogenicity)

**Verdict: FLAGGED**
- The target (protozoal H2 source reduction) is valid in concept, but the selectivity challenge is effectively insurmountable with current knowledge. [FeFe]-hydrogenases and PFOR are too conserved between protozoa and bacteria. Additionally, the most abundant rumen protozoa (Entodinium) lack hydrogenosomes entirely, limiting the impact even if selectivity were achieved. Low priority.
- **Wet-lab confirmation type:** Comparative genomics of protozoal vs. bacterial [FeFe]-hydrogenase sequences to identify selectivity windows. This is a bioinformatics-first project.

---

### Candidate 5.2: Saponin Partial Defaunation — KNOWN [Forge]

**Resolved Identity:**
- Compounds: Steroidal and triterpenoid saponins from Yucca schidigera / Quillaja saponaria
- Mechanism: Membrane disruption of protozoa (cholesterol-dependent lysis)

**Assessment:**
- Reduces protozoa 30-60% at 0.5-1% DM in meta-analyses
- Effect is transient: 2-4 weeks in most studies due to microbial/protozoal adaptation
- Non-specific antimicrobial activity at higher doses
- Never tested specifically under RHAS conditions as H2 source reduction strategy

**Verdict: CONFIRMED**
- Known mechanism, known limitations (transient effect). Useful as a complementary/combination approach with primary candidates. Not a standalone RHAS treatment. Low regulatory risk.
- **Wet-lab confirmation type:** RUSITEC with 3-NOP + low-dose saponin. Measure protozoal counts, H2, VFA over 14+ days to confirm transient vs. sustained effect under RHAS.

---

### Candidate 6.1: Engineered Fumarate Reductase in M. elsdenii — NOVEL [Forge]

**Resolved Identity:**
- Target enzyme: Fumarate reductase (EC 1.3.5.4; frdABCD operon)
- Host organism: Megasphaera elsdenii
- FRD in rumen bacteria: characterized in S. ruminantium membrane fraction (Asanuma et al. 2002)
  - FRD exists in membrane fraction of fumarate-reducing bacteria
  - S. ruminantium subspecies reduce fumarate using H2 as electron donor
  - frdABCD operon structure in S. ruminantium NOT fully characterized in public databases
- M. elsdenii: proven rumen colonizer (Lactipro commercial DFM); acid-tolerant strain H6F32 exists

**Annotation Check:**
- Forge claims: "Overexpression has been done in E. coli" -- Verified: frdABCD overexpression is well-established in E. coli metabolic engineering
- Forge claims: "M. elsdenii has been engineered for acid tolerance" -- Verified: H6F32 strain documented
- Forge claims: "No exogenous fumarate supplementation needed" because the organism uses endogenous rumen fumarate/malate -- **PARTIALLY CORRECTED:** Endogenous rumen fumarate/malate concentrations are low (transient intermediates, typically <1 mM). Overexpressing FRD increases the kinetic capacity but the SUBSTRATE (fumarate/malate) may be limiting. The organism would need to also upregulate the upstream PEP -> oxaloacetate -> malate -> fumarate pathway to provide substrate, or be co-administered with low-dose fumarate.

**Feasibility:**
- M. elsdenii is genetically tractable (transformation protocols exist)
- Rumen colonization is proven (Lactipro)
- GMO regulatory pathway is the main non-technical barrier
- Selective advantage under RHAS conditions: yes -- an organism with enhanced H2 disposal grows faster when H2 is elevated

**Verdict: CONFIRMED (with substrate correction)**
- Technically feasible and biologically sound. The correction is that FRD overexpression alone may not increase H2 disposal if substrate (fumarate) is limiting. The engineered organism should ideally also overexpress the upstream carboxylation step (PEPCK/PEPC -- see V1.3) to pull carbon into the pathway. This is a pathway engineering project, not just a single-gene overexpression.
- **Wet-lab confirmation type:** Express frdABCD in M. elsdenii; test in batch culture with rumen fluid + 3-NOP. Measure propionate production, dissolved H2.

---

### Candidate 6.2: Fumarate + Acrylate Combination — EMPIRICAL HIT A [Forge]

**Resolved Identity:**
- Fumaric acid: PubChem CID 444972; MW 116.1
- Acrylic acid: PubChem CID 6581; MW 72.1

**Assessment:**
- In vivo validated in dairy cows (Maigaard 2024): both fumaric acid and acrylic acid increased rumen propionate within hours of dosing
- Acrylic acid REDUCED DMI in the Maigaard study -- a significant concern
- Stoichiometric cost trap: $0.20-0.80/day at effective doses
- **Assessment:** The biology is validated. The economics and the acrylate DMI reduction are the barriers.

**Verdict: CONFIRMED**
- Useful as positive control in KE#1 RUSITEC experiments. Not a development candidate due to stoichiometric cost. The DMI reduction with acrylate requires monitoring.
- **Wet-lab confirmation type:** Include as positive control in KE#1 RUSITEC alongside novel candidates.

---

### Candidate 7.1 / S2.1: Formate Trap — Formate-to-Propionate Routing / FDH Enhancement — NOVEL [Forge+Vulcan Convergence]

**Resolved Identity:**
- Enzyme target: Formate dehydrogenase (FDH, EC 1.17.1.9)
- Reaction: CO2 + NADH + H+ -> HCOO- + NAD+ (formate synthesis direction)
- Under RHAS: high NADH/NAD+ ratio FAVORS CO2 reduction to formate (consuming NADH, regenerating NAD+)
- This is distinct from the classic FDH direction (formate -> CO2 + NADH)

**Thermodynamic Assessment:**
- CO2 + NADH -> formate + NAD+: delta-G depends on concentrations
  - At standard conditions: delta-G'0 = -3.5 kJ/mol (barely favorable)
  - Under RHAS conditions (high NADH/NAD+ ratio, high CO2): delta-G becomes more negative (thermodynamically more favorable)
- **Assessment:** The reaction is thermodynamically favorable SPECIFICALLY under RHAS conditions, which is elegant -- the disease creates the conditions that make the treatment work.

**Critical Unknown:**
- Whether formate actually accumulates under RHAS conditions is UNMEASURED
- Martinez-Fernandez (2017) observed increased formate under chloroform treatment -- this is the only data point
- If formate does NOT accumulate (rapidly interconverted to H2 by formate hydrogen lyase), the formate trap strategy fails
- **Assessment:** This candidate's viability depends entirely on KE#1 formate measurement. Zero cost to add this measurement to existing experiments.

**Verdict: CORRECTED**
- Forge frames this as "Formate-to-Propionate Routing via Engineered Prevotella" -- a complex genetic engineering project. Vulcan frames it as "FDH enhancement" -- a simpler enzymatic/small-molecule approach. Both converge on the same biology but Vulcan's framing is more practical. Correction: the first step is NOT engineering Prevotella but simply MEASURING formate dynamics under RHAS in KE#1 RUSITEC. If formate accumulates, multiple intervention approaches (FDH supplementation, acetogen stimulation, simple formate capture) become available.
- **Wet-lab confirmation type:** Add formate measurement to KE#1 RUSITEC at all time points. If formate > 2x controls under methanogenesis inhibition, the formate trap is viable.

---

### Candidate 8.1: Propylene Glycol Bridge Therapy — NON-OBVIOUS [Forge]

**Resolved Identity:**
- Compound: Propylene glycol (1,2-propanediol)
- PubChem CID: 1030
- MW: 76.1
- FDA-approved for ketosis prevention in dairy cattle

**Assessment:**
- PG is metabolized to propionate in the rumen and to glucose in the liver
- Widely used, well-understood, commercially available
- Bridge therapy concept (14-21 days during inhibitor initiation) is novel application
- Cost: $0.50-1.50/day x 14-21 days = $7-30 total per introduction cycle
- **Assessment:** Low-risk, near-term clinical utility. Not a standalone RHAS solution.

**Verdict: CONFIRMED**
- Can proceed immediately as clinical bridge therapy during inhibitor introduction. No computational validation needed -- this is a known drug in a novel application.
- **Wet-lab confirmation type:** Pilot study: 3-NOP initiation with vs. without 14-day PG bridge. Measure blood BHB, glucose, NEFA, milk yield, DMI.

---

### Candidate V1.3: PEPCK/PEPC Activator — NOVEL [Vulcan-Only]

**Resolved Identity:**
- Enzyme: Phosphoenolpyruvate carboxykinase (ATP) (PEPCK; EC 4.1.1.49)
- Gene: pckA
- UniProt: P22259 (Selenomonas ruminantium)
- Sequence length: 538 aa; MW: 59.6 kDa; monomer
- Cofactors: ADP (not GDP/IDP), Mg2+, Mn2+
- Also characterized in: Ruminococcus flavefaciens (purified and characterized; Hou et al. 1997)

**Conservation:**
- PEPCK is universally present in propionogenic rumen bacteria (Selenomonas, Prevotella, Veillonella, Propionibacterium)
- The propionate pathway is conserved across all rumen environments, regardless of microbiome composition
- **Assessment:** Target is universally conserved in the rumen.

**Host Selectivity:**
- Bovine PEPCK (hepatic gluconeogenesis enzyme) is structurally different from bacterial PEPCK: bovine uses GTP, bacterial S. ruminantium uses ADP
- Different cofactor specificity provides inherent selectivity
- Risk: LOW
- Evidence: [COMPUTATIONAL -- cofactor specificity difference]

**Annotation Check:**
- Vulcan claims: "PEPCK is the committed step of propionogenesis" -- Verified: PEP carboxylation to oxaloacetate is the entry point to the succinate-propionate pathway
- Vulcan claims: "Transcriptionally regulated by energy status" -- Verified: pck mRNA was 12-fold higher when grown on lactate than glucose, inversely related to energy sufficiency
- Vulcan proposes bicarbonate supplementation as CO2 source for PEPC -- this is a testable, low-cost intervention
- **Crystal structure information:** Three consensus kinase motifs (kinase-1a, kinase-2, kinase-3a) identified by crystal structure + sequence alignment. Substrate-binding and catalytic residues characterized.

**Druggability Assessment:**
- Active site is well-characterized (ADP binding pocket, PEP binding site, CO2/bicarbonate binding)
- Small-molecule allosteric activator would need to increase Vmax or decrease Km for PEP/ADP
- No known allosteric activators of bacterial PEPCK exist -- this is a genuine drug discovery target
- The bicarbonate variant (simple supplementation) is immediately testable at zero risk

**Verdict: CONFIRMED**
- This is a genuine and novel drug target. The enzyme is well-characterized, crystal structure information exists, and the cofactor specificity (ADP vs GTP) provides inherent selectivity over host PEPCK. The bicarbonate supplementation experiment (Vulcan's V1.3 simple variant) costs essentially nothing and could demonstrate the principle. The small-molecule activator is a longer-term drug discovery project.
- **Wet-lab confirmation type:** Two-stage: (1) RUSITEC with 50 mM NaHCO3 + 3-NOP to test CO2 supplementation effect on propionate; (2) If positive, initiate PEPCK allosteric activator screen.

---

### Candidate V2.1: Rumen-Protected Propionate — NOVEL [Vulcan-Only]

**Resolved Identity:**
- Compound: Calcium propionate in rumen-bypass coating (pH-sensitive polymer)
- Mechanism: Symptom-level treatment -- delivers propionate post-ruminally

**Assessment:**
- Rumen-bypass technology is mature (Evonik, Adisseo products for amino acids)
- Addresses propionate deficit at host level, NOT H2 accumulation
- Requires 100-200 g/day propionate salt -- feasible but bulky
- **Assessment:** Valid clinical bridge but does not treat the underlying syndrome. Similar to PG bridge (8.1) but post-ruminal delivery.

**Verdict: CONFIRMED**
- Technically feasible with existing technology. Low development risk. Addresses symptom, not cause.
- **Wet-lab confirmation type:** In vivo trial with rumen-protected calcium propionate + Bovaer. Measure milk yield, blood glucose, propionate absorption.

---

### Candidate V2.2: Lactate-to-Propionate Activator (Acrylate Pathway) — NOVEL [Vulcan-Only]

**Resolved Identity:**
- Target: Lactoyl-CoA dehydratase and acryloyl-CoA reductase in M. elsdenii acrylate pathway
- Mechanism: Lactate -> acrylyl-CoA -> propionyl-CoA -> propionate (consumes [2H])

**Critical Assessment:**
- Vulcan identifies the key weakness: "lactate accumulation is not a consistent feature of RHAS"
- RHAS is NOT acidosis -- lactate typically does not accumulate in a functional rumen under RHAS conditions
- Without lactate substrate, this pathway has nothing to convert
- **Assessment:** Substrate-limited; not applicable to RHAS unless lactate accumulation is confirmed

**Verdict: FLAGGED**
- The pathway exists and is well-characterized in M. elsdenii, but the substrate (lactate) is unlikely to be available under typical RHAS conditions. Low priority unless RHAS is combined with acidosis (a different clinical scenario).
- **Wet-lab confirmation type:** Measure rumen lactate under graded methanogenesis inhibition in RUSITEC. If lactate > 5 mM, revisit.

---

### Candidate V3.1: Rnf Complex Engineering in Cellulolytic Bacteria — NOVEL [Vulcan-Only]

**Resolved Identity:**
- Target: Rnf complex (ferredoxin:NAD+ oxidoreductase) from Acetobacterium woodii
- Host: Ruminococcus albus / R. flavefaciens (cellulolytic rumen bacteria)
- Mechanism: Decouple NADH recycling from H2 production; generate membrane potential from ferredoxin oxidation

**Critical Assessment:**
- Vulcan correctly identifies the weakest link: "genetic engineering of obligate anaerobic rumen bacteria is extremely challenging"
- R. albus and R. flavefaciens are poorly tractable for genetic manipulation -- no established transformation protocols
- The Rnf complex is a multi-subunit membrane complex (6 subunits: RnfA-E, RnfG) -- expressing and correctly assembling this in a heterologous host is a major molecular biology challenge
- No published examples of Rnf complex transfer between anaerobes
- **Assessment:** Scientifically elegant but technically at the limits of current capability. High risk, long timeline.

**Verdict: FLAGGED**
- The intervention concept is sound (decouple NADH recycling from H2 production in cellulolytics), but the technical barriers are currently insurmountable for Ruminococcus. Would require fundamental advances in genetic tools for obligate anaerobic rumen bacteria. Long-term research project.
- **Wet-lab confirmation type:** As a first step, test whether A. woodii Rnf complex can be expressed in a more tractable anaerobe (Clostridium acetobutylicum or similar).

---

### Candidate V3.2: Engineered Bacteria with NADH:Acceptor Oxidoreductase + Quinone — NOVEL [Vulcan-Only]

**Resolved Identity:**
- Concept: Engineer rumen bacterium to overexpress NADH:menaquinone oxidoreductase; co-administer menadione as the exogenous quinone electron acceptor
- Creates synthetic electron disposal pathway: NADH -> [enzyme] -> quinone -> reduced quinone
- The engineered bacterium has a SELECTIVE ADVANTAGE under RHAS: faster NADH recycling = faster growth when H2 is high

**Assessment:**
- This is the corrected and improved version of Forge's 1.2 (NADH oxidase)
- Solves the O2 problem (uses quinone instead of O2 as terminal acceptor)
- Solves the intracellular access problem (enzyme is expressed intracellularly)
- The selective advantage under RHAS conditions is a crucial insight -- addresses the colonization challenge that defeats all DFM approaches
- **Assessment:** Technically more feasible than V3.1 because the host organism can be M. elsdenii or another genetically tractable rumen bacterium

**Verdict: CONFIRMED**
- This is one of the most sophisticated and well-reasoned candidates in the entire portfolio. It combines two validated concepts (quinone electron shuttling + engineered intracellular enzyme) with a natural selection mechanism (fitness advantage under RHAS). Medium-term development timeline (requires molecular biology + in vitro validation).
- **Wet-lab confirmation type:** Express NADH:menaquinone oxidoreductase in M. elsdenii; test with menadione supplementation in batch culture under methanogenesis inhibition. Measure growth rate vs. wild-type to confirm selective advantage.

---

### Candidate V4.1: Hepatic Gluconeogenesis Cofactor Supplementation — NOVEL [Vulcan-Only]

**Resolved Identity:**
- Supplements: Biotin (cofactor for propionyl-CoA carboxylase) + B12/adenosylcobalamin (cofactor for methylmalonyl-CoA mutase)
- Target: Liver gluconeogenesis efficiency from propionate

**Assessment:**
- Vulcan self-assesses: "the problem is almost certainly substrate supply, not enzyme capacity. The liver has enormous reserve gluconeogenic capacity."
- Magnitude estimate: <5% of RHAS pathology
- **Assessment:** Agree with Vulcan's own low-priority assessment. The bottleneck is propionate supply to the liver, not hepatic enzyme capacity. Cofactor supplementation will have negligible effect unless hepatic enzyme deficiency is demonstrated under RHAS (Vulcan predicts it will not be).

**Verdict: FLAGGED**
- Lowest priority candidate in the portfolio. Vulcan correctly identifies this as a low-magnitude, substrate-limited intervention. Include in portfolio for completeness but do not invest resources.
- **Wet-lab confirmation type:** Measure hepatic PCC and methylmalonyl-CoA mutase activity in cows on Bovaer vs. controls. If no difference (Vulcan's prediction), archive.

---

### Candidate S3.1: Abiotic Pd/Pt Nanoparticle Catalyst — NOVEL [Vulcan-Only, Highest Novelty]

**Resolved Identity:**
- Material: Palladium nanoparticles (5 nm) on alumina support
- Mechanism: Abiotic catalytic hydrogenation of rumen metabolic intermediates (fumarate -> succinate, CO2 -> formate, crotonate -> butyrate) using dissolved H2

**Thermodynamic Feasibility:**
- H2 + fumarate -> succinate: delta-G'0 = -86 kJ/mol (highly favorable)
- Pd catalyzes hydrogenation at ambient temperature in aqueous solution (confirmed in industrial chemistry)
- Turnover frequencies of Pd nanoparticles for H2-mediated reactions: extremely high (thousands per hour)
- **Assessment:** The chemistry is thermodynamically sound. Pd is one of the most active H2 oxidation catalysts known.

**CRITICAL PROBLEM: H2S Poisoning**
- Rumen H2S concentration: 1,639-6,005 ppm (depending on dietary sulfur)
- Even "low sulfur" diets produce ~1,600 ppm H2S in rumen gas
- **Palladium is IRREVERSIBLY POISONED by H2S.** Sulfides chemisorb to Pd surface, forming PdS, which is catalytically dead
- "Hydrogen sulfide is produced by many anaerobic bacteria and can irreversibly damage the palladium catalyst"
- Recovery requires reduction treatment under H2 atmosphere at elevated temperature -- not possible in a rumen
- One adsorbed RS group inhibits adsorption of one hydrogen atom
- A study specifically investigated "evaluation of potential hydrogen sulfide adsorbents for the protection of palladium catalyst in anaerobic culture systems" -- the fact that this paper exists confirms H2S poisoning is a known, critical problem for Pd in anaerobic systems
- **Assessment:** Pd nanoparticles will be DEACTIVATED within minutes to hours in the rumen due to H2S poisoning. This is a near-certain failure mode.

**Potential Mitigation:**
- H2S adsorbent layer (iron oxide coating on alumina support before Pd) -- could scavenge H2S before it reaches catalyst surface
- Sulfide-tolerant catalysts (MoS2, WS2) -- but these have much lower H2 oxidation activity
- **Assessment:** Mitigation is theoretically possible but adds significant complexity and uncertainty. The rumen H2S environment is fundamentally hostile to Pd catalysis.

**Verdict: FLAGGED**
- This is the most novel and intellectually bold candidate in the entire portfolio. The thermodynamics are excellent. But the H2S poisoning problem in the rumen is a near-certain deactivation mechanism that Vulcan did not consider. Vulcan identified rumen stability as the "weakest link" but focused on biofilm coating and mechanical abrasion -- H2S poisoning is the actual show-stopper. If H2S poisoning can be mitigated (iron oxide pre-layer, sulfide-tolerant catalyst alternative), this could still be viable. But the risk is VERY HIGH.
- **Wet-lab confirmation type:** Before any rumen testing, test Pd nanoparticles in sealed bottles with: (a) H2 + buffer (positive control), (b) H2 + buffer + H2S at rumen concentrations (poisoning test), (c) H2 + buffer + H2S + iron oxide pre-layer. This is a simple chemistry experiment. Cost: <$1K.

---

### Candidate S5: H2-Sensor Antagonist — NOVEL [Vulcan-Only]

**Resolved Identity:**
- Target: Putative sensory [FeFe]-hydrogenase hyd3 in R. albus (Zheng et al. 2014, J. Bacteriol.)
- Mechanism: Block H2 sensing to prevent metabolic shift to acetate production

**Assessment:**
- The sensory hydrogenase is "identified but its regulatory role is not confirmed" (Vulcan's own assessment)
- No ligand, no binding site, no crystal structure, no screening assay available
- This is a fundamental research target, not a drug discovery target
- **Assessment:** Pre-discovery stage. Cannot be computationally validated because the target is not characterized.

**Verdict: FLAGGED**
- Interesting concept but currently at the fundamental research stage. Would require: (1) confirm hyd3 is actually a sensor, (2) characterize its signaling mechanism, (3) identify a binding site, (4) design a screening assay. This is 3-5 years of basic research before drug discovery begins. Very low priority for the current portfolio.
- **Wet-lab confirmation type:** R. albus hyd3 knockout/knockdown to test whether the metabolic shift under high H2 is regulatory (altered in mutant) vs. purely thermodynamic (unchanged in mutant).

---

### Management and Platform Candidates (Brief Assessments)

**S1.1: Dose Escalation Protocol** -- CONFIRMED. Management tool; no computational validation needed.

**S1.2: Diet Optimization (Fiber:Starch Ratio)** -- CONFIRMED. Based on established meta-analysis data (Kebreab et al. 2023).

**S5.1: Intraruminal Bolus Delivery** -- CONFIRMED. Platform technology; validated by monensin CRC (335 mg/day for 100 days). Applicable to any lead compound that emerges.

---

## Structure Prediction and Binder Design Assessment

### Applicability to RHAS Portfolio

Unlike infectious disease programs where structure prediction enables vaccine antigen/antibody design, the RHAS portfolio is dominated by small-molecule and material interventions. Structure prediction is applicable to only 3 candidates:

| Target | Structure Available? | AF3 Needed? |
|---|---|---|
| Phloroglucinol reductase (EC 1.3.1.57) | Not in AlphaFold DB for rumen Coprococcus | YES -- would inform substrate pocket analysis |
| PEPCK (P22259, S. ruminantium) | Homology models available from E. coli PEPCK crystal structures | OPTIONAL -- allosteric site identification |
| Fumarate reductase (frdABCD) | Well-characterized in E. coli; homology modeling feasible | NO -- sufficient structural information exists |

### Binder Design

Not applicable to this program. There are no antibody/vaccine targets -- RHAS is not an infectious disease. No binder design requests needed.

### AF3 Submission Request: Phloroglucinol Reductase

A structure prediction for Coprococcus phloroglucinol reductase would inform understanding of the substrate binding pocket and potentially guide the design of synthetic phloroglucinol analogs with improved H2-capture kinetics. However, given that phloroglucinol itself is cheap and available, and the primary question is biological (does the adaptation time hypothesis explain the Maigaard discrepancy?), structure prediction is LOW PRIORITY for this candidate.

**Decision: No AF3 submissions requested at this stage.** The key unknowns in this portfolio are biological and thermodynamic, not structural. AF3 submissions should be reconsidered if PEPCK allosteric activator screening is initiated (Phase 2 of V1.3 development).

---

## Key Corrections and Discoveries

### Corrections to Forge

1. **Candidate 1.2 (NADH Oxidase / noxE):** noxE is O2-DEPENDENT and therefore non-functional in the anaerobic rumen. Vulcan's V3.2 (NADH:acceptor oxidoreductase + quinone) is the corrected version.

2. **Candidate 3.1 (Succinic Acid):** Succinate is NOT an electron acceptor -- it is the product of fumarate reduction. Supplementing succinate provides propionate precursor but does NOT sink H2. Forge's claim that it "serves as both an electron acceptor" is incorrect.

3. **Candidate 6.1 (Engineered Fumarate Reductase):** Overexpressing FRD alone may be substrate-limited (endogenous fumarate is low). The upstream carboxylation step (PEPCK/PEPC) should be co-engineered to increase fumarate supply.

### Corrections to Vulcan

4. **Candidate S3.1 (Pd Nanoparticle Catalyst):** Vulcan identified "rumen stability" as the weakest link but focused on biofilm coating and mechanical abrasion. The actual show-stopper is **H2S poisoning** -- Pd is irreversibly deactivated by the 1,600-6,000 ppm H2S naturally present in the rumen.

### Key Discovery: Menadione (Vitamin K3) as Lead Redox Mediator

The most significant finding of this survey is the existing cattle data showing that menadione (200 mg/day) INCREASES PROPIONATE MOLAR RATIO in dairy cows. This is direct evidence for the electron shuttle mechanism under normal rumen conditions. Combined with:
- FDA/EFSA safety approval as feed additive
- 1,000x safety margin above requirement
- Correct redox potential for NADH electron acceptance
- Bacterial enzymes (NQO1) for safe two-electron reduction

Menadione may be the lead compound for the redox mediator class, potentially displacing riboflavin as the #1 candidate due to stronger existing evidence of propionate-shifting activity.

---

## Surveyor Force-Ranking (Computational Confidence)

Based on computational validation, ranked by confidence that the mechanism will work in the rumen:

| Rank | Candidate | Computational Confidence | Key Strength | Key Risk |
|---|---|---|---|---|
| 1 | **1.1c: Menadione (VitK3)** | **HIGH** | Existing cattle propionate data; FDA-approved; correct redox | Whether effect size is sufficient under RHAS |
| 2 | **1.1: Riboflavin/FMN** | **HIGH** | Thermodynamically sound; GRAS; dirt cheap | Rapid rumen degradation may limit shuttle function |
| 3 | **3.2: Iron(III) Oxide** | **HIGH** | Best thermodynamics of any candidate (-228 kJ/mol) | Mass dose; Fe2+ accumulation |
| 4 | **2.1: Biochar (DIET)** | **MODERATE-HIGH** | Non-toxic, cheap, rumen-stable | DIET unproven in rumen |
| 5 | **4.1: Phloroglucinol** | **MODERATE** | In vivo cattle data exists | Conflicting results (Maigaard 2024) |
| 6 | **V1.3: PEPCK/PEPC (bicarbonate)** | **MODERATE** | Enzyme well-characterized; test is trivial | CO2 may not be limiting in inhibited rumen |
| 7 | **6.2: Fumarate + Acrylate** | **MODERATE** | In vivo validated | Stoichiometric cost; acrylate DMI depression |
| 8 | **V3.2: Engineered NADH:acceptor + quinone** | **MODERATE** | Elegant combination; fitness advantage | Engineering + colonization challenge |
| 9 | **6.1: Engineered FRD M. elsdenii** | **MODERATE** | Proven host organism | Substrate limitation; GMO regulatory |
| 10 | **7.1/S2.1: Formate Trap** | **LOW-MODERATE** | Thermodynamically elegant under RHAS | Formate accumulation unconfirmed |
| 11 | **2.2: Magnetite (DIET)** | **LOW-MODERATE** | Defined conductivity | Nanoparticle safety; dose uncertainty |
| 12 | **S3.1: Pd Nanoparticle Catalyst** | **LOW** | Highest thermodynamic potential | H2S poisoning near-certain |
| 13 | **3.3: Encapsulated Nitrate** | **LOW** | Most efficient H2 sink known | Nitrite toxicity unmitigable |
| 14 | **5.1: Hydrogenosome Inhibitor** | **LOW** | Valid target concept | No selectivity window exists |
| 15 | **S5: H2-Sensor Antagonist** | **VERY LOW** | Novel concept | Target not characterized |

---

## Predictions for Prediction Log

### Prediction S-1: Menadione Propionate Effect Under RHAS
- **Prediction:** Menadione (vitamin K3) at 200 mg/day equivalent in RUSITEC under 50% methanogenesis inhibition will increase propionate molar percentage by >3 points and decrease dissolved H2 by >15% relative to 3-NOP-only controls.
- **Test:** RUSITEC dose-response with menadione (0, 50, 200, 600 mg/day equiv.) at fixed 3-NOP.
- **If TRUE:** Menadione is validated as an RHAS treatment via electron shuttle mechanism. Advance to in vivo.
- **If FALSE:** The propionate increase seen in normal cows does not scale under RHAS conditions. Deprioritize menadione; focus on riboflavin or Fe(III) oxide.

### Prediction S-2: Pd Catalyst H2S Deactivation
- **Prediction:** Pd nanoparticles (5 nm, alumina-supported) exposed to H2S at 2,000 ppm (rumen-relevant concentration) will lose >90% of H2 oxidation activity within 1 hour at 39C.
- **Test:** Sealed bottle assay: Pd NPs + H2 + buffer at t=0; measure H2 consumption rate. Then add H2S to 2,000 ppm; measure H2 consumption rate at 1, 4, 24 hours.
- **If TRUE:** Pd catalysis in rumen is not viable without H2S mitigation. Consider sulfide-tolerant alternatives (MoS2) or pre-layer protection.
- **If FALSE:** H2S poisoning is slower than expected at rumen temperatures. Pd catalyst remains viable.

### Prediction S-3: Succinic Acid Does Not Reduce H2
- **Prediction:** Succinic acid supplementation (100 mM) in RUSITEC under 50% methanogenesis inhibition will increase propionate production by >10% but will NOT decrease dissolved H2 concentration relative to 3-NOP-only controls.
- **Test:** RUSITEC with succinic acid + 3-NOP. Measure both propionate and dissolved H2.
- **If TRUE:** Confirms Surveyor's correction that succinate is a propionate precursor, not an H2 sink. Reclassify candidate as "VFA modifier" not "H2 disposal."
- **If FALSE:** Some indirect H2 disposal occurs via metabolic coupling. Candidate is more valuable than assessed.

### Prediction S-4: DIET in Rumen (Biochar Conductivity Test)
- **Prediction:** Conductive biochar (pyrolyzed >600C, EC > 1 S/m) under 50% methanogenesis inhibition will reduce dissolved H2 by >15% relative to non-conductive biochar (<400C, same mass loading) controls, demonstrating that the effect is conductivity-dependent (DIET) rather than surface-area-dependent (adsorption).
- **Test:** RUSITEC with conductive vs. non-conductive biochar at 1% DM + 3-NOP. Measure dissolved H2, VFA profile.
- **If TRUE:** DIET is operational in the rumen. This is transformative.
- **If FALSE:** Rumen bacteria cannot perform DIET. Biochar effects (if any) are adsorption-based. Deprioritize DIET mechanism; focus on soluble electron shuttles.

---

## Summary for Reaper

**Candidates with high computational confidence (proceed to kill/survive assessment):**
- 1.1c Menadione, 1.1 Riboflavin/FMN, 3.2 Iron(III) Oxide, 2.1 Biochar DIET, 4.1 Phloroglucinol, V1.3 PEPCK/bicarbonate, 6.2 Fumarate+Acrylate (positive control)

**Candidates with corrections (mechanism updated, still viable):**
- 3.1 Succinic Acid (propionate precursor, not H2 sink), 7.1/S2.1 Formate Trap (measure first, engineer later), 6.1 Engineered FRD (needs pathway co-engineering), V3.2 Engineered NADH:acceptor (corrected version of 1.2)

**Candidates flagged for material risk:**
- 1.1b Lawsone (hemolytic risk), 1.1d AQDS (DMI depression precedent), 3.3 Encapsulated Nitrate (nitrite toxicity unmitigable; Mo strategy failed), S3.1 Pd Catalyst (H2S poisoning), 1.2 noxE (O2-dependent), 5.1 Hydrogenosome Inhibitor (no selectivity), V2.2 Acrylate Activator (no substrate under RHAS), V3.1 Rnf Engineering (genetically intractable hosts), V4.1 Hepatic Cofactors (<5% magnitude), S5 H2-Sensor (target uncharacterized)

**Reaper should pay special attention to:**
1. Whether the menadione propionate data under normal conditions extrapolates to RHAS conditions
2. Whether riboflavin's rapid rumen degradation is a feature (active uptake for shuttling) or a bug (vitamin sequestration, no shuttle function)
3. Whether any candidate can pass the "why isn't the field doing this?" test -- specifically, why hasn't menadione been tested for RHAS given the existing propionate data?
4. The practical mass dose challenge for iron(III) oxide (300-550 g/day)
