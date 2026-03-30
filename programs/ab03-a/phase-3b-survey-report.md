# Phase 3b — Survey Report: Computational Validation of H₂ Sink Candidates

**Program:** AB03-A — Rumen H₂ Sink (Biochemistry Mode) | **Internal Agteria** | **Version:** v1
**Agent:** Surveyor | **Date:** 2026-03-30

---

## Methodology Note

This is a biochemistry/microbial engineering program, not a pathogen program. Standard Surveyor protocols (BLAST conservation across pathogenic strains, host selectivity against bovine proteome) apply differently here:

- **"Conservation"** means: Is the target enzyme/pathway present and conserved across relevant rumen microbial populations?
- **"Host selectivity"** means: Does the intervention target a microbial enzyme/pathway that has no bovine ortholog of concern?
- **"Target resolution"** includes: enzyme identifiers, organism genomes, PDB structures, and chemical compound identifiers where applicable.
- **Many targets are non-protein** (redox mediators, conductive particles, iron chelates) or **whole-organism interventions** (DFMs, consortia). These receive chemical/biological feasibility assessments rather than protein-level validation.

All evidence tagged [COMPUTATIONAL] unless otherwise noted. No kills — data only. Reaper decides.

---

## Forge-Vulcan Merge: Convergence Map

Independent convergence between Forge (informed by failure analysis + external panel) and Vulcan (quarantined, first-principles only) is a strong validation signal.

| Forge Candidate | Vulcan Intervention Point | Convergence | Signal Strength |
|---|---|---|---|
| **2.1** Engineered adhesin display | **V2** Adhesin-mediated niche hijacking | **FULL CONVERGENCE** — identical target (Mru_1499), identical logic (co-opt methanogen spatial strategy) | VERY STRONG |
| **5.2** HDCR transplant (low-threshold acetogen) | **V1** Engineered high-throughput low-threshold acetogen | **FULL CONVERGENCE** — both identify HDCR from *T. kivui* as entry-point enzyme; Vulcan adds Rnf/Ech/Nfn multi-route energy conservation | VERY STRONG |
| **4.1** PEP carboxylase engineering | **V5** Supercharged propionogenesis / **V9** Reductive TCA fragment | **STRONG CONVERGENCE** — both identify endogenous fumarate generation via CO₂ fixation as the key to removing exogenous substrate dependency | STRONG |
| **8.1** Quinone/flavin redox shuttle | **V6** Redox mediator-assisted electron shuttling | **FULL CONVERGENCE** — both identify quinone-based mediators (AQDS, DHNA, riboflavin) for decoupling H₂ transfer from physical proximity | VERY STRONG |
| **5.1** *Ca.* Faecousia cultivation | **V1** (chassis option) | **PARTIAL** — Vulcan lists *Ca.* Faecousia as a chassis option but focuses on *E. limosum* and *S. ovata* as more tractable starting points | MODERATE |
| **1.1** Selective endosymbiont disruption | **V8** Protozoa-targeted selective endosymbiont disruption | **FULL CONVERGENCE** — identical concept; Vulcan adds molecular decomposition (lipophilic MCR prodrug, archaeal membrane targeting) | STRONG |
| **2.3** Conductive materials (GAC) | **V6** (partial overlap) | **WEAK** — Vulcan's redox mediators are soluble shuttles, not conductive particles; different mechanism | WEAK |
| **X.2** Phloroglucinol + *Coprococcus* | **V7** Engineered phloroglucinol-H₂ sink pathway | **PARTIAL** — Forge proposes co-administration of organism + substrate; Vulcan proposes engineering the enzyme pathway into a different chassis | MODERATE |
| **X.3** Formate targeting | **V4** Formate-H₂ interconversion buffer (FHL engineering) | **STRONG CONVERGENCE** — both identify formate as an underexploited electron carrier; Vulcan provides specific molecular target (FHL complex engineering) | STRONG |

### Vulcan-Only Candidates (New Entries for Reaper)

| Vulcan # | Intervention | Status |
|---|---|---|
| **V3** | Ferric iron chelate electron acceptor | NEW — not proposed by Forge |
| **V9** | Reductive TCA fragment (autotrophic propionogenesis from CO₂ + H₂) | NEW — extends Forge 4.1 concept to full autotrophic pathway |

### Total Merged Candidate Count: 25

(Forge's 23 original candidates + 2 Vulcan-only additions. Overlapping candidates are assessed once with both sources noted.)

---

## Summary Table

| # | Candidate | Source | Category | Key Identifier(s) | Target Type | Conservation / Feasibility | Key Risk | Verdict |
|---|---|---|---|---|---|---|---|---|
| 2.1/V2 | Engineered adhesin display (Mru_1499) | Forge+Vulcan | Novel | Mru_1499 (D3E0X3, *M. ruminantium* M1); PDB: none; Big_1 domains + TG domain | Protein (surface display) | Adhesin characterized; heterologous expression in bacteria untested | Archaeal protein folding in bacterial host | CONFIRMED with CAVEATS |
| 2.2 | Biofilm scaffold particles | Forge | Novel | N/A — physical scaffolds | Non-protein (material) | GAC/biochar feasibility established in AD | Scale and rumen passage survival | CONFIRMED |
| 2.3 | Conductive materials (DIET) | Forge | Non-obvious | N/A — GAC/biochar | Non-protein (material) | DIET demonstrated in AD systems | Cytochrome/pili requirement absent in rumen H₂ consumers | FLAGGED |
| 4.1/V5 | PEP carboxylase engineering | Forge+Vulcan | Novel | *ppc* gene (various); PEP carboxylase EC 4.1.1.31 | Protein (enzyme overexpression) | ppc well-characterized in *E. coli*, *A. succinogenes*; *Prevotella* homolog present | *Prevotella* genetic tools severely limited | CONFIRMED with CAVEATS |
| 4.2 | Fumarate bridge (low-dose) | Forge | Known (Cat A) | Fumaric acid (PubChem CID 444972) | Small molecule supplement | Established chemistry; in vitro efficacy moderate | In vivo cattle translation gap | CONFIRMED |
| 4.3/V5 | QFR overexpression | Forge+Vulcan | Novel | frdABCD operon; *W. succinogenes* QFR structure PDB 1QLA (2.2 A) | Protein (membrane complex) | Crystal structure solved; well-characterized enzyme | Membrane protein overexpression toxicity | CONFIRMED |
| 5.1 | *Ca.* Faecousia cultivation | Forge | Known (Cat A) | Uncultivated — MAG only (Pope et al., PNAS 2025) | Whole organism | Metagenomic evidence strong; WLP genes identified | Never cultivated; may be obligate syntrophic | CONFIRMED with CAVEATS |
| 5.2/V1 | HDCR transplant (low-threshold acetogen) | Forge+Vulcan | Novel | *T. kivui* HDCR: FdhF (743 aa), HydA2 (461 aa), HycB3 (184 aa), HycB4 (210 aa); PDB 7QV7 (3.4 A cryo-EM) | Protein (multi-subunit metalloenzyme) | Structure solved; kcat 2,654 s⁻¹ confirmed; [Fe-S] clusters characterized | Thermophilic enzyme at mesophilic temp; heterologous expression of multi-subunit complex | CONFIRMED |
| 5.3 | *A. woodii* rumen adaptation | Forge | Non-obvious | *A. woodii* DSM 1030; genome well-characterized; Rnf (rnfABCDEF) characterized | Whole organism | Lab model acetogen; genetic tools available; Rnf well-characterized | pH optimum 7.0-7.5 vs rumen 5.5-7.0; no rumen data | FLAGGED |
| 5.4 | Acetogen consortium DFM | Forge | Non-obvious | Multiple species | Multi-organism formulation | Individual organisms partially characterized | DFM persistence in rumen; consortium stability | CONFIRMED with CAVEATS |
| 5.5 | CRISPR-edited methanogens | Forge | Novel | MCR (*mcr*) — methyl-coenzyme M reductase; *M. ruminantium* genome CP001719 | Protein (gene knockout) | MCR is essential; genome sequenced | Archaea editing tools immature; organism may die without methanogenesis | FLAGGED |
| 6.1 | Encapsulated nitrate (safe dose) | Forge | Known (Cat A) | Calcium-ammonium nitrate | Small molecule supplement | Safety demonstrated at 200-400 mg Fe/kg DM analog; efficacy moderate | Individual animal variability in nitrite reductase capacity | CONFIRMED |
| 6.2 | Coupled nitrate/nitrite reductase | Forge | Novel | *S. ruminantium* narGHJI + nrfA (UniProt I0GSU1); genome AP012049 | Protein (enzyme co-expression) | Nitrate/nitrite reductases characterized; nar operon sequenced | Genetic tools for *S. ruminantium* limited | CONFIRMED with CAVEATS |
| 8.1/V6 | Quinone/flavin redox shuttle | Forge+Vulcan | Novel | AQDS (PubChem CID 66534, E°' = −184 mV); DHNA; Riboflavin (vitamin B2) | Small molecule (catalytic shuttle) | EET demonstrated in *L. plantarum*; AQDS well-characterized in AD | AQDS toxic to bacteria at >10 mM; rumen-specific stability unknown | CORRECTED |
| 8.2 | NADH oxidase (heterologous) | Forge | Novel | nox gene (various LAB); water-forming NADH oxidase EC 1.6.3.4 | Protein (heterologous enzyme) | Enzyme well-characterized | Requires O₂ — rumen is anaerobic; oxygen-independent variants need electrochemical regeneration | FLAGGED |
| 9.1 | Pre-adaptation protocol | Forge | Non-obvious | N/A — protocol, not molecular target | Protocol | Individual components have partial evidence | Sequential approach untested; populations may not persist through transition | CONFIRMED |
| 9.2 | Phage + sink installation | Forge | Non-obvious | Methanogen-targeting phage (Gilbert et al., 2020) | Biological (phage) | Phage identified from rumen samples | Strain-specific; rapid resistance; does not solve H₂ disposal | FLAGGED |
| 9.3 | Early-life rumen programming | Forge | Non-obvious | N/A — developmental window | Protocol | Pope et al. 2025 demonstrated calf rumen remodeling | Adult rumen may overwrite calf-established populations | CONFIRMED with CAVEATS |
| X.1 | Integrated AB03 product | Forge | Novel | N/A — combination formulation | Multi-component product | Individual components partially validated | Premature as a unit; interactions unknown | CONFIRMED (as concept) |
| X.2/V7 | Phloroglucinol + *Coprococcus* | Forge+Vulcan | Non-obvious | Phloroglucinol (PubChem CID 359); phloroglucinol reductase (EC 1.3.1.57, *E. oxidoreducens* G-41, 78 kDa homodimer) | Small molecule + organism | 50.6% H₂ reduction in steers (n=8); enzyme purified and characterized | Requires *Coprococcus* pre-establishment; high dose (450 g/day); n=4 for weight gain | CORRECTED |
| X.3/V4 | Formate targeting / FHL engineering | Forge+Vulcan | Non-obvious/Novel | *E. coli* FHL complex: PDB 7Z0S (2.6 A cryo-EM); 7 subunits (fdhF, hycBCDEFG) | Protein (enzyme complex engineering) | FHL structure solved at high resolution; reversibility demonstrated | Forward reaction 10x faster than reverse; directional engineering undemonstrated | CONFIRMED |
| 1.1/V8 | Selective endosymbiont disruption | Forge+Vulcan | Non-obvious/Novel | MCR as target; protozoal membrane permeability as barrier | Drug target (prodrug design) | MCR mechanism established; lipophilic drug delivery precedented | Protozoa-methanogen symbiosis may be obligate | CONFIRMED with CAVEATS |
| V3 | Ferric iron chelate electron acceptor | Vulcan only | Non-obvious | Ferric citrate (PubChem CID 3659987); Fe³⁺/Fe²⁺ E°' = +0.77 V | Small molecule (electron acceptor) | Fed to cattle at 200-750 mg Fe/kg DM safely; 72-81% H₂S reduction | Stoichiometry requires impractical doses for meaningful H₂ sinking | CORRECTED |
| V9 | Reductive TCA fragment (autotrophic propionogenesis) | Vulcan only | Novel | pyc + ppc + mdh + fumB + frdABCD + scpABC + hydABC + rnfABCDEF (synthetic pathway, ~15-20 genes) | Synthetic biology (multi-gene pathway) | Individual enzymes well-characterized; CO₂ fixation + fumarate reduction established | ~20-gene synthetic pathway; net ATP balance uncertain | FLAGGED |
| 4.2 (bridge) | Fumarate bridge | Forge | Known (Cat A) | — | — | — | — | CONFIRMED |

---

## Per-Candidate Assessments

### Candidate 2.1/V2: Engineered Adhesin Display (Mru_1499) — Novel [FORGE + VULCAN CONVERGENCE]

**Resolved Identity:**
- Gene: *mru_1499* | Protein: D3E0X3 (UniProt, *M. ruminantium* M1; inferred from genome project CP001719)
- Organism: *Methanobrevibacter ruminantium* M1, Taxonomy ID 634498
- Sequence length: ~1,000 aa (full-length adhesin with signal peptide aa 1-18, four Big_1 domains, transglutaminase domain)
- Resolution notes: Protein identified via phage display (Ng et al., 2016). Domain architecture well-characterized: Big_1 domains at positions 102-197, 195-283, 286-390, 577-665; TG domain at 878-981. First Big_1 domain (aa 19-198, AdLP-D1) is sufficient for protozoa binding. Epitope mapping completed (Subharat et al., 2022). No pre-computed AlphaFold structure found for full-length protein.

**Conservation:**
- The adhesin binds a "broad range of hydrogen-producing microorganisms" including *Butyrivibrio proteoclasticus*, *Ruminococcus* spp., and ciliate protozoa (multiple genera). This broad binding spectrum is advantageous — it does not require specificity engineering.
- Conservation within *M. ruminantium* strains: The genome is from the type strain M1 (ATCC 35063, DSM 1093). Adhesin-like proteins with Big_1 domains are found across Methanobrevibacteriales, including *M. smithii* and *Methanosphaera stadtmanae* (PMC11532034), suggesting the domain architecture is evolutionarily conserved.
- Evidence: [COMPUTATIONAL — genome analysis, domain annotation]

**Host Selectivity:**
- Big_1 domains are bacterial immunoglobulin-like domains. No bovine ortholog with binding function identified. The transglutaminase domain has mammalian homologs (blood coagulation factor XIII, tissue transglutaminase), but the overall protein architecture is unique to archaeal adhesins.
- Risk: LOW — this is an archaeal surface protein with no functional bovine counterpart.

**Annotation Check:**
- Claimed function: Adhesin binding H₂-producing rumen microbes → VERIFIED (Ng et al., 2016; phage display + co-culture binding assays)
- Claimed localization: Surface-exposed → VERIFIED (signal peptide residues 1-18; surface display confirmed by immunofluorescence)
- Essentiality: Not essential for *M. ruminantium* survival, but essential for its competitive H₂-scavenging strategy

**Structure:**
- No pre-computed AlphaFold structure for full-length Mru_1499.
- The AdLP-D1 domain (aa 19-198) has been recombinantly expressed in *E. coli* for epitope mapping studies, demonstrating bacterial expression is feasible for at least the binding domain.
- **AF3 submission warranted** for: (a) full AdLP-D1 domain structure to identify binding interface, (b) sortase-anchored display model on gram-positive cell wall context.
- Evidence: [COMPUTATIONAL — database search; no structure available]

**Key Computational Finding — Heterologous Expression Feasibility:**
- The protein is archaeal. Archaea have unique post-translational modifications (N-glycosylation at different sequons than bacteria/eukaryotes). Whether the binding function requires archaeal-specific glycosylation is UNKNOWN.
- However, the AdLP-D1 domain was successfully expressed in *E. coli* (Subharat et al., 2022), suggesting that at minimum the binding domain folds correctly in a bacterial host.
- For display on *E. limosum* (gram-positive): sortase-mediated cell wall anchoring is the appropriate system. Sortase-based display is well-established in *Lactobacillus* species.

**Verdict:** CONFIRMED with CAVEATS
- The adhesin is real, its binding function is demonstrated, and its domain architecture is characterized. The independent convergence between Forge and Vulcan on this target is the strongest signal in the program.
- Caveat 1: Functional expression of the full adhesin (not just AdLP-D1) on a bacterial surface has NOT been demonstrated.
- Caveat 2: Rumen protease resistance of the surface-displayed adhesin is unknown.
- Caveat 3: Even with adhesin-mediated attachment, per-cell H₂ consumption rate of the displaying organism must be sufficient to outcompete residual methanogens.

**Wet-lab confirmation type:**
- Co-culture binding assay: adhesin-displaying *E. limosum* + *R. albus*; quantify physical attachment by microscopy and co-sedimentation
- H₂ consumption rate comparison: adhesin+ vs adhesin- *E. limosum* in co-culture with H₂ producer; GC for headspace H₂

---

### Candidate 2.2: Biofilm Scaffold Particles — Novel

**Resolved Identity:**
- N/A — non-protein target. Physical scaffolds (cellulose microbeads, lignocellulose particles, granular activated carbon).
- Resolution notes: This is a materials science / biofilm engineering intervention, not a molecular target.

**Chemical/Biological Feasibility:**
- GAC promotes biofilm formation and close physical association in anaerobic digestion systems [ESTABLISHED]
- Cellulose-based scaffolds are biodegradable and compatible with rumen environment [ESTABLISHED]
- Key parameter: scaffold must survive rumen passage (mastication, pH 5.5-7.0, protease activity) and not interfere with normal fiber digestion
- Pre-colonization with acetogens before ruminal introduction is technically feasible (anaerobic culture on scaffold surface)

**Rumen Stability:**
- GAC particles of 0.5-2 mm diameter should survive rumen passage for multiple hours before passing to the omasum
- Lignocellulose scaffolds mimic feed particles and would integrate naturally into the rumen mat
- Scale estimate: If each cow receives 50 g scaffold/day with 10⁸ CFU acetogens/g, total dose is 5x10⁹ CFU — reasonable for a DFM

**Toxicity:**
- GAC: GRAS status in multiple applications; no reported toxicity at feed-relevant doses
- Biochar: Used as a feed additive in some livestock systems; generally recognized as safe

**Verdict:** CONFIRMED
- The concept is physically sound and draws on established anaerobic digestion engineering. The Tribunal's Martian insight about supersaturation-driven concentration gradients provides the theoretical basis.
- No protein-level validation needed. Assessment is at the materials/feasibility level.

**Wet-lab confirmation type:**
- Scaffold colonization assay: pre-colonize GAC/cellulose beads with *E. limosum* → introduce to rumen fluid + 3-NOP → quantify acetogen persistence on scaffold vs planktonic by 16S qPCR

---

### Candidate 2.3: Conductive Material-Mediated Electron Transfer (DIET) — Non-obvious

**Resolved Identity:**
- N/A — GAC/biochar as conductive material
- DIET requires specific outer-membrane multiheme cytochromes (e.g., OmcS in *Geobacter*) or conductive type IV pili

**Chemical/Biological Feasibility:**
- DIET is well-demonstrated between *Geobacter metallireducens* and *Methanosarcina barkeri* via GAC [ESTABLISHED]
- **Critical problem:** DIET requires specific electron transfer proteins (multiheme cytochromes, conductive pili) on the surfaces of BOTH the electron-donating and electron-accepting organisms. Typical rumen H₂ consumers (*Prevotella*, *Selenomonas*, acetogens) are NOT known to possess these surface electron transfer components.
- *Geobacter*-like organisms may be present in the rumen at very low abundance, but the dominant H₂ consumers do not have the molecular machinery for DIET.

**Verdict:** FLAGGED
- The DIET mechanism requires specific surface electron transfer proteins that are absent from the major rumen H₂-consuming populations. GAC may still promote biofilm formation and close physical proximity (overlapping with Candidate 2.2's mechanism), but the specific DIET pathway is unlikely to operate in the rumen context.
- This is a mechanism mismatch, not a materials problem. The conductive material is fine; the biology does not support the claimed electron transfer mode.

**Wet-lab confirmation type:**
- Metatranscriptomic survey of GAC-attached rumen microbial community under 3-NOP: look for multiheme cytochrome and pilA gene expression on GAC surfaces

---

### Candidate 4.1/V5: PEP Carboxylase Engineering (Endogenous Fumarate Overproduction) — Novel [FORGE + VULCAN CONVERGENCE]

**Resolved Identity:**
- Gene: *ppc* (phosphoenolpyruvate carboxylase) EC 4.1.1.31 | Also *pyc* (pyruvate carboxylase) EC 6.4.1.1
- PEP carboxylase is ubiquitous in rumen *Prevotella* — present in *P. ruminicola* 23 (type strain) and *P. brevis* genomes
- *Prevotella ruminicola* 23: NCBI Taxonomy ID 264731; genome draft available
- *Selenomonas ruminantium* subsp. *lactilytica*: Complete genome AP012049 (NCBI); Taxonomy ID 927704

**Conservation:**
- PEP carboxylase is a core metabolic enzyme present in essentially all *Prevotella* and *Selenomonas* species in the rumen [ESTABLISHED]
- Fumarate reductase (frdABCD): present in all propionate-producing rumen bacteria via the succinate pathway [ESTABLISHED]
- This is not a conservation concern — the target enzymes are universal in the relevant organisms

**Host Selectivity:**
- PEP carboxylase has a bovine ortholog (PEPCK / PEP carboxykinase functions in gluconeogenesis). However, this is an overexpression strategy in microbial cells, not an inhibition target. No host selectivity concern.
- Risk: NOT APPLICABLE — intervention is enzyme overexpression in rumen microbes, not a drug targeting the host

**Annotation Check:**
- Claimed mechanism: PEP carboxylase overexpression increases intracellular fumarate flux → more H₂ consumed by fumarate reductase → CONSISTENT with *E. coli* metabolic engineering data showing 3.5x succinate titer increase from ppc overexpression (PMC3754722)
- **Important correction:** PPC overexpression beyond an optimal range DECREASES growth and succinate production in *E. coli* (positive correlation only within a certain activity range). This is a known metabolic engineering pitfall — the relationship between ppc expression level and product formation is NOT linear.
- Claimed organism: *Prevotella ruminicola* → genetic tools are SEVERELY LIMITED. No established transformation protocol, limited shuttle vectors. *Selenomonas ruminantium* has narGHJI operon characterized but also limited tools. The most tractable alternative chassis is *E. limosum* (CRISPR/Cas9 established, shuttle vectors available).

**Vulcan's Extension (V5 — Supercharged Propionogenesis):**
- Vulcan identifies the COMPLETE pathway: pyc + mdh + fumB + frdABCD + scpABC + rnfABCDEF
- This is a more ambitious version of Forge's 4.1 — not just ppc overexpression, but engineering the entire reductive arm from CO₂ to propionate
- The magnitude estimate (10-15 mol [2H]/day, 17-26% of displaced H₂) is significant

**Verdict:** CONFIRMED with CAVEATS
- The biochemistry is sound. PEP carboxylase overexpression for enhanced succinate/propionate production is a mature metabolic engineering strategy with strong precedent in *E. coli* and *A. succinogenes*.
- Caveat 1: *Prevotella* genetic tools are insufficient for the proposed engineering. Realistic chassis is *S. ruminantium* or *E. limosum* (with the full propionate pathway added).
- Caveat 2: Expression level must be optimized — excessive ppc activity is counterproductive.
- Caveat 3: Vulcan's full autotrophic propionogenesis (V9) requires ~20 genes and uncertain net ATP balance. The intermediate version (ppc + frdABCD overexpression in a native propionate producer) is more tractable.

**Wet-lab confirmation type:**
- Metabolic flux analysis: ppc-overexpressing *S. ruminantium* vs wild-type under 50 μM dissolved H₂; measure propionate yield per cell by GC

---

### Candidate 4.2: Fumarate Supplementation as Short-Term Bridge — Known (Category A)

**Resolved Identity:**
- Fumaric acid: PubChem CID 444972, MW 116.07 g/mol, pKa₁ 3.03, pKa₂ 4.44
- At rumen pH 5.5-7.0, fumarate is predominantly in dibasic form (fully dissociated)

**Feasibility:**
- 44% H₂ capture in vitro [MODERATE — Ungerfeld & Forster, 2011]
- 3-NOP + fumarate: 11.5% additional CH₄ reduction in vitro (Zhang et al., AEM, 2022) [MODERATE]
- In vivo cattle: inconsistent; often non-significant [MODERATE]
- Cost at therapeutic dose: $3-7/head/day (CONSTRAINT C1 VIOLATION at full dose)
- Cost at bridge dose (2% DM): ~$0.50-1.00/head/day (marginal)

**Verdict:** CONFIRMED
- Chemistry and mechanism are straightforward. The bridge concept (limited-duration use for population pre-adaptation) is reasonable.
- Applies the "why isn't the field doing this?" test: at full dose, fumarate is too expensive and inconsistent in cattle. As a temporary bridge, the economics may work.

**Wet-lab confirmation type:**
- Pre-adaptation crossover: fumarate for 3 weeks → add 3-NOP → withdraw fumarate → track *Prevotella*/*Selenomonas* persistence by 16S

---

### Candidate 4.3/V5: Quinol:Fumarate Reductase (QFR) Overexpression — Novel

**Resolved Identity:**
- Gene: *frdABCD* operon | Protein: Quinol:fumarate reductase (QFR)
- *Wolinella succinogenes* QFR: Structure solved at 2.2 A (PDB 1QLA; Lancaster et al., Nature, 1999)
  - FrdA: 656 aa, contains covalently bound FAD prosthetic group, fumarate reduction site
  - FrdB: 238 aa, contains three iron-sulfur centres ([2Fe-2S], [4Fe-4S], [3Fe-4S])
  - FrdC: membrane anchor, five transmembrane helices, two haem b molecules
- *Prevotella* QFR: Identified in proteomics (Trautmann et al., 2023); originated mainly from *Prevotella* species in monensin-treated communities
- UniProt: FrdB from *W. succinogenes* ATCC 29543 = P17596

**Conservation:**
- Fumarate reductase is present in all succinate-pathway propionate producers in the rumen (*Prevotella*, *Selenomonas*, *Wolinella*, *Veillonella*) [ESTABLISHED]
- The *W. succinogenes* enzyme is the best-characterized structural model

**Structure Assessment:**
- PDB 1QLA provides a high-resolution template for understanding the active site, cofactor binding, and membrane integration
- The enzyme is a membrane-bound complex with three subunits — overexpression of membrane protein complexes is technically challenging and often results in inclusion bodies or membrane stress
- The Trautmann proteomics data confirm that rumen *Prevotella* naturally upregulates QFR under propionogenesis-promoting conditions (monensin treatment), suggesting the native regulatory machinery can be leveraged

**Verdict:** CONFIRMED
- The target is real, well-characterized structurally, and functionally validated. The *W. succinogenes* crystal structure provides atomic-level detail for rational engineering.
- The main technical challenge is membrane protein overexpression, which is a known difficulty but not a fundamental barrier.

**Wet-lab confirmation type:**
- Heterologous expression of *W. succinogenes* frdCAB in *E. coli* or *S. ruminantium*; measure fumarate reduction rate vs. native background; if >3x improvement, proceed to rumen organism chassis

---

### Candidate 5.1: *Candidatus* Faecousia Cultivation — Known (Category A)

**Resolved Identity:**
- Organism: *Candidatus* Faecousia sp. (uncultivated)
- Taxonomy: Novel lineage within Eubacteriaceae; assigned based on metagenome-assembled genomes (MAGs) from Pope et al., PNAS 2025
- Genome: MAG only — no pure culture, no type strain, no NCBI genome assembly with accession
- Key genomic features: Full Wood-Ljungdahl pathway genes (15 genes identified in MAG); dose-dependent WLP upregulation under 3-NOP
- Study: 51 dairy calves, 27,884 genome catalogue from rumen metagenomes

**Conservation:**
- This organism expanded dramatically and specifically in response to 3-NOP treatment in dairy calves [PRELIMINARY — single study, 2025]
- Whether it is present across breeds, diets, and geographies is UNKNOWN — the Pope et al. study used a single herd
- It belongs to Eubacteriaceae, suggesting phylogenetic relationship to *Eubacterium limosum* (also Eubacteriaceae)

**Annotation Check:**
- Claimed function: Reductive acetogenesis via Wood-Ljungdahl pathway → VERIFIED by metatranscriptomic evidence showing dose-dependent WLP gene upregulation under 3-NOP
- Claimed localization: Rumen-native → VERIFIED (reconstructed from rumen metagenome)
- Cultivability: NOT VERIFIED — organism has never been grown in pure culture. Many rumen organisms resist cultivation due to syntrophic dependencies, unknown growth factor requirements, or strict anaerobe sensitivity.

**Key Computational Finding:**
- The MAG provides a genome-guided cultivation strategy: predict amino acid auxotrophies, cofactor requirements, and potential syntrophic dependencies from the genome annotation.
- If the organism encodes a truncated amino acid biosynthesis pathway (common in rumen syntrophs), specific amino acid supplementation in culture medium may enable growth.
- The Eubacteriaceae affiliation is encouraging — *E. limosum* (same family) is readily cultivable. But *Candidatus* designation explicitly means uncultivated.

**Verdict:** CONFIRMED with CAVEATS
- The organism is real and its in vivo response is the strongest biological signal in the program (dramatic expansion with dose-dependent WLP upregulation under the exact condition AB03 addresses).
- Caveat 1: Cultivation is the critical enabling step and has never been achieved. This is a genuine technical risk.
- Caveat 2: Even if cultivated, its H₂ threshold is UNKNOWN — it may have the same high threshold as other rumen acetogens.
- Caveat 3: Single-study dependency (Pope et al., 2025). No independent replication yet.

**Wet-lab confirmation type:**
- Genome-guided cultivation: MAG-predicted nutritional requirements → dilution-to-extinction in supplemented rumen fluid media under elevated H₂ + 3-NOP
- If pure culture fails: defined consortium isolation (identify syntrophic partners from co-occurrence network)

---

### Candidate 5.2/V1: HDCR Transplant (Low-H₂-Threshold Acetogen Engineering) — Novel [FORGE + VULCAN CONVERGENCE]

**Resolved Identity:**
- Gene cluster: *T. kivui* HDCR — *fdhF1* (743 aa), *hydA2* (461 aa), *hycB3* (184 aa), *hycB4* (210 aa), plus maturation factor *fdhD*
- Structure: PDB 7QV7 — cryo-EM at 3.4 A resolution (Schwarz et al., Nature 2022)
- Architecture: Hexameric repeating unit (FdhF₂:HydA₂₆:HycB3₂:HycB4₆); forms filaments
- Catalytic activity: kcat = 2,654 s⁻¹ for CO₂ reduction (vs 28 s⁻¹ for *A. woodii* HDCR — 95x improvement)
- Metal cofactors: 34 [4Fe-4S] clusters across the complex; 6 iron-sulfur cluster complexes in hydrogenase active sites
- Organism of origin: *Thermoanaerobacter kivui* (thermophilic, optimal 66°C)
- Proposed host: *Eubacterium limosum* (rumen-native acetogen; genome 4.15 Mb, 3,805 genes; CRISPR/Cas9 and CRISPRi tools available)

**Conservation:**
- HDCR is the entry-point enzyme of the Wood-Ljungdahl pathway. All acetogens have SOME version of this enzyme.
- The *T. kivui* variant is exceptional in its catalytic rate (2,654 s⁻¹) — this is a specific variant, not a conserved enzyme.
- *E. limosum* SA11 (rumen isolate) has its own HDCR with lower activity. The transplant replaces native with *T. kivui* high-performance variant.

**Host Selectivity:**
- HDCR has no bovine ortholog. The Wood-Ljungdahl pathway is exclusively prokaryotic.
- Risk: NOT APPLICABLE

**Structure Assessment:**
- PDB 7QV7 at 3.4 A provides atomic detail of the complex architecture, including the iron-sulfur cluster relay connecting formate dehydrogenase and hydrogenase active sites.
- The filament architecture is notable — HDCR forms extended nanowire-like structures anchored to the membrane (Schwarz et al., Nature 2022: "Membrane-anchored HDCR nanowires drive hydrogen-powered CO₂ fixation").
- **Temperature concern:** *T. kivui* is thermophilic (optimal 66°C). The enzyme has "remarkable thermostability" (described as the highest-activity biological CO₂ catalyst). However, activity at rumen temperature (39°C) is not reported. Thermophilic enzymes typically retain SOME activity at mesophilic temperatures but at reduced rates.
- The Nature Communications 2024 paper reports engineered FdhF variants (truncated subunit) with retained activity — this demonstrates the enzyme is amenable to engineering.

**Genetic Tools for Host (*E. limosum*):**
- CRISPR/Cas9 system with 100% gene targeting efficiency (Shin et al., ACS Synth Biol, 2019)
- CRISPRi for transcriptional repression (genome-wide screen with 41,939 guide RNAs; Jang et al., PNAS 2023)
- Recombineering tools available
- Characterized genetic bioparts: promoters, 5' UTRs, terminators (Shin et al., 2022)
- Multiple shuttle vectors and selectable markers
- **This is the most genetically tractable rumen acetogen available.**

**Key Computational Finding:**
- The HDCR complex requires assembly of multiple iron-sulfur clusters ([4Fe-4S]). Heterologous expression of [Fe-S] cluster proteins requires co-expression of the ISC or SUF iron-sulfur cluster assembly machinery from the donor organism.
- *E. limosum* has native iron-sulfur cluster assembly systems (as all acetogens do), but the *T. kivui* HDCR may require specific maturation factors (FdhD is annotated as a maturation factor in the gene cluster).
- The kcat of 2,654 s⁻¹ was measured at the thermophilic optimum. Activity at 39°C must be experimentally determined. Even if reduced by 50-70%, it would still be 8-25x faster than native *A. woodii* HDCR.

**Verdict:** CONFIRMED
- This is the best-characterized molecular target in the program. Structure solved at atomic resolution, catalytic rate quantified, genetic tools in the host available, and engineering precedent exists (truncated variants, heterologous expression in *E. coli*).
- The Forge-Vulcan convergence is complete: both independently identified this as the highest-priority enzymatic target.
- The temperature concern is real but addressable (directed evolution for mesophilic activity, or using activity at 39°C which may still be sufficient given the 95x headroom).

**Wet-lab confirmation type:**
- Express *T. kivui* HDCR (fdhF1 + hydA2 + hycB3 + hycB4 + fdhD) in *E. limosum*; measure CO₂ reduction activity at 39°C; compare kcat to native *E. limosum* HDCR

---

### Candidate 5.3: *Acetobacterium woodii* Rumen Adaptation — Non-obvious

**Resolved Identity:**
- Organism: *Acetobacterium woodii* DSM 1030 (type strain)
- Genome: Well-characterized; Rnf complex (rnfABCDEF) is the best-studied energy conservation system in any acetogen
- Rnf complex: Na⁺-translocating ferredoxin:NAD⁺ oxidoreductase; requires Na⁺; reversibly coupled to membrane potential (Biegel & Muller, J Bacteriol 2018; PMC3814746)
- Genetic tools: Electrocompetent cells can be prepared (protocol published 2025, PMC12345282); gene deletion systems available

**Conservation:**
- *A. woodii* is NOT a rumen organism. It was isolated from pond sediment.
- Its Rnf complex is Na⁺-coupled (vs H⁺-coupled in some rumen acetogens), which provides more efficient energy conservation at near-equilibrium conditions.
- The organism does not survive in rumen conditions without adaptation.

**Key Risk Assessment:**
- pH: *A. woodii* optimal pH is 7.0-7.5. Rumen pH ranges 5.5-7.0. At pH 5.5, the organism would likely be non-viable.
- Competition: No precedent for establishing a non-native anaerobe in the rumen long-term
- Historical precedent: ALL non-native DFMs in the rumen show washout within 48-72 hours

**Verdict:** FLAGGED
- The organism has excellent biochemistry (best-characterized Rnf system) and developing genetic tools, but the rumen survival challenge is substantial. pH sensitivity is the primary concern.
- The directed evolution approach (serial passage in rumen fluid) is sound in principle but will require 3-6+ months and may not succeed.
- Alternative strategy: Use *A. woodii* as a GENE DONOR for Rnf complex components, rather than trying to install the whole organism in the rumen. Transfer the Na⁺-coupled Rnf to *E. limosum* (rumen-native).

**Wet-lab confirmation type:**
- pH tolerance assay: *A. woodii* viability (CFU) over 72h at pH 5.5, 6.0, 6.5, 7.0 in rumen fluid vs defined medium

---

### Candidate 5.4: Acetogen Consortium DFM — Non-obvious

**Resolved Identity:**
- Multi-species formulation: proposed members include *E. limosum* (tractable), *Blautia producta* (rumen-native), adapted *A. woodii* (if 5.3 succeeds), *Ca.* Faecousia relatives (if cultivated)
- N/A for single protein target — this is a formulation-level assessment

**Feasibility:**
- Defined consortia outperform monocultures 2.5-2.9x for H₂ production in anaerobic systems [cited by Forge from ScienceDirect 2020]
- Commercial precedent: Multi-strain DFMs are marketed for livestock (e.g., various *Lactobacillus* + *Propionibacterium* formulations). Manufacturing complexity is manageable.
- DFM persistence remains the fundamental challenge regardless of formulation.

**Verdict:** CONFIRMED with CAVEATS
- The consortium approach is sound for covering the range of rumen conditions (pH, H₂ concentration, spatial context).
- Caveat: Assembly requires at least 2-3 of the consortium members to be available in culture. Currently only *E. limosum* and *Blautia* spp. are available.

**Wet-lab confirmation type:**
- Defined co-culture stability: 2-3 acetogen species in continuous culture under rumen-like conditions for 30 days; monitor relative abundance by species-specific qPCR

---

### Candidate 5.5: CRISPR-Edited Methanogens — Novel

**Resolved Identity:**
- Target gene: *mcrA* (methyl-coenzyme M reductase alpha subunit) — the terminal enzyme of methanogenesis
- Organism: *Methanobrevibacter ruminantium* M1 (genome CP001719, 2.93 Mb, ~2,217 genes)
- Berkeley/Davis program: BIOME (Berkeley Initiative for Optimized Microbiome Editing), $70M from TED Audacious Project; led by Jill Banfield and Jennifer Doudna
- Strategy: Edit *mcrA*/*mtr* genes to eliminate methanogenesis while preserving H₂-consuming hydrogenases and adhesins

**Key Risk Assessment:**
- **Fundamental biological problem:** Methanogenesis is the SOLE energy conservation pathway for hydrogenotrophic *Methanobrevibacter*. Deleting *mcr* does not convert a methanogen into an acetogen — it kills it. The organism has no Wood-Ljungdahl pathway genes.
- Converting a methanogen to an acetogen would require INSERTING an entire WLP pathway (~15 genes) — massive genetic engineering in an archaeal host
- Archaeal genetic tools are far less developed than bacterial tools. CRISPR delivery to *Methanobrevibacter* has not been reported.
- The Berkeley/Davis program has been funded since ~2023 and is a 7-year project. Progress reports are not yet public.
- GMO regulatory pathway: 5-10+ years for livestock applications

**Verdict:** FLAGGED
- The concept is transformative but the technical barriers are enormous. The fundamental biology (methanogenesis = sole energy source for *Methanobrevibacter*) means gene deletion alone does not create a functional organism.
- Forge's recommendation to "monitor and license" rather than duplicate is appropriate.
- This is a 7-10 year horizon target at best.

**Wet-lab confirmation type:**
- N/A — monitor Berkeley/Davis program publications. Key milestone: demonstration of *Methanobrevibacter* gene editing with organism survival.

---

### Candidate 6.1: Encapsulated Slow-Release Nitrate — Known (Category A)

**Resolved Identity:**
- Active ingredient: Calcium-ammonium nitrate (Ca(NO₃)₂ or NH₄NO₃); encapsulated form
- Safety data: Blood methemoglobin below detection limit at tested doses (Lee et al., 2019; Duthie et al., 2018)
- EFSA BMDL₁₀: ~38 g NaNO₃/day for 600 kg cow; proposed dose 20-30 g/day (well below threshold)

**Efficacy Assessment:**
- 18.5% CH₄ reduction (encapsulated nitrate in grazing steers) [MODERATE]
- Captures ~10-15% of displaced H₂ at safe doses — INSUFFICIENT as primary sink, valid as supporting component
- NPN (non-protein nitrogen) value: ammonia produced is usable for microbial protein synthesis

**Verdict:** CONFIRMED
- Safety profile established. Efficacy is modest but real. Appropriate as a supporting component in a multi-intervention strategy, not as a standalone approach.

**Wet-lab confirmation type:**
- Add to existing 3-NOP trial: encapsulated nitrate at 20 g/day + 3-NOP → measure incremental H₂ reduction and blood methemoglobin over 4 weeks

---

### Candidate 6.2: Engineered Tightly-Coupled Nitrate/Nitrite Reductase — Novel

**Resolved Identity:**
- Target: Nitrate reductase (*narGHJI*) and nitrite reductase (*nrfA* or *nirBD*) — balance kinetics to prevent nitrite accumulation
- *S. ruminantium*: narGHJI operon characterized (Asanuma et al., 2004); nar transcription enhanced by nitrate
- *S. ruminantium* NrfA: UniProt I0GSU1 (cytochrome c nitrite reductase, ammonia-forming); from strain NBRC 103574/TAM6421
- *W. succinogenes*: Well-characterized nitrate/nitrite reduction; Km for fumarate/H₂ established

**Conservation:**
- narGHJI present in *S. ruminantium*, *W. succinogenes*, *Veillonella parvula* — all rumen-native [ESTABLISHED]
- NirBD (cytoplasmic nitrite reductase) present in *E. coli* and many Enterobacteriaceae; NrfAB (periplasmic) in *W. succinogenes*

**Annotation Check:**
- The kinetic mismatch (nitrate → nitrite is faster than nitrite → ammonia) is well-documented as the cause of nitrite toxicity [ESTABLISHED]
- Overexpressing nirBD or nrfA to match narGHJI kinetics is a sound engineering strategy

**Verdict:** CONFIRMED with CAVEATS
- The molecular targets are well-characterized. The concept of kinetically matching the two reductases is mechanistically sound.
- Caveat: Genetic tools for *S. ruminantium* are limited. Characterization of nar operon is at the sequencing/transcription level, not at the transformation/overexpression level.

**Wet-lab confirmation type:**
- Measure nitrite accumulation kinetics in rumen fluid with and without nrfA-overexpressing *S. ruminantium* (or *E. coli* as proof-of-concept host)

---

### Candidate 8.1/V6: Catalytic Redox Mediator Shuttle (Quinone/Flavin) — Novel [FORGE + VULCAN CONVERGENCE]

**Resolved Identity:**
- AQDS: Anthraquinone-2,6-disulfonate, PubChem CID 66534, MW 368.34 g/mol, E°' = −184 mV, water-soluble
- DHNA: 1,4-dihydroxy-2-naphthoic acid, E°' approx −145 mV, used by *L. plantarum* for EET
- Riboflavin: Vitamin B2, E°' = −208 mV, well-established electron shuttle in biological systems

**Chemical Feasibility:**
- AQDS is stable in anaerobic conditions and cycles between oxidized/reduced forms [ESTABLISHED in AD systems]
- DHNA is used by *Lactiplantibacillus plantarum* for extracellular electron transfer — increases NAD⁺/NADH ratio, accelerates fermentation, generates more ATP (eLife 2022; mBio 2023) [ESTABLISHED]
- Riboflavin-mediated EET demonstrated; *L. plantarum* uses flavin-dependent and DHNA-dependent routes through distinct pathways (Ndh2 + EetA for flavin; Ndh2 + PplA for DHNA) [ESTABLISHED]

**CRITICAL CORRECTION — AQDS Toxicity:**
- AQDS is TOXIC to bacteria at concentrations >10 mM — enters cells and causes cell death if accumulated past critical concentration (Shyu et al., J Bacteriol 2002)
- At 20 mM, AQDS was toxic for methanogenic activity for the entire experimental period
- Bacteria with *tolC* efflux pumps are protected; those without are vulnerable
- **The Forge/Vulcan proposed concentration of 0.5-5 mM is within the potentially toxic range for some organisms, particularly methanogens (which is actually beneficial here) but possibly also for sensitive rumen bacteria.**

**Rumen-Specific Assessment:**
- NO rumen-specific data exists for any quinone mediator. All evidence is from laboratory anaerobic digestion, *L. plantarum* cultures, or sediment environments.
- Whether rumen bacteria (cellulolytic *Ruminococcus*, *Fibrobacter*) can interact with quinone mediators via their NADH dehydrogenases (Ndh2 homologs) is UNKNOWN.
- DHNA and riboflavin are less toxic alternatives to AQDS and are more biologically relevant (riboflavin is vitamin B2, already present in rumen at trace levels).

**Magnitude Estimate Correction:**
- Vulcan estimates 100 mmol AQDS/day (~26 g/day) for a 200 L rumen at 0.5 mM. This is reasonable if the mediator is truly catalytic (recycled, not consumed). But if AQDS is partially degraded or irreversibly reduced by some rumen organisms, consumption would increase the dose requirement.

**Verdict:** CORRECTED
- The mediator concept is sound (Forge-Vulcan convergence is strong). BUT:
- (a) AQDS toxicity at >10 mM limits the working range. DHNA or riboflavin are safer alternatives.
- (b) No rumen-specific data exists for ANY quinone mediator.
- (c) The terminal electron acceptor problem remains: in EET systems, electrons must ultimately go somewhere. In the rumen (anaerobic), the acceptor is likely fumarate (propionate producers) or CO₂ (acetogens). The mediator does not create new sinks — it improves electron TRANSFER to existing sinks.
- The original assessment should prioritize DHNA and riboflavin over AQDS for rumen applications.

**Wet-lab confirmation type:**
- Batch rumen fluid + 3-NOP: add DHNA (1 μM, 10 μM, 100 μM) or riboflavin (same range); measure NAD⁺/NADH ratio, dissolved H₂, VFA profiles over 24h; UV-Vis monitoring of mediator redox cycling

---

### Candidate 8.2: Heterologous Water-Forming NADH Oxidase — Novel

**Resolved Identity:**
- Enzyme: Water-forming NADH oxidase (Nox), EC 1.6.3.4
- Sources: *Lactobacillus pentosus*, *Streptococcus mutans*, *Thermus thermophilus*
- Reaction: NADH + H⁺ + 0.5O₂ → NAD⁺ + H₂O

**Fundamental Problem:**
- The enzyme requires molecular oxygen (O₂) as terminal electron acceptor.
- The rumen is ANAEROBIC. Dissolved O₂ in the rumen is essentially zero (maintained by facultative anaerobe oxygen scavenging at the rumen wall).
- Oxygen-independent variants exist (JACS Au, 2024) but require electrochemical FAD regeneration — not available in vivo.

**Verdict:** FLAGGED
- The oxygen dependency is a FUNDAMENTAL barrier, not a technical challenge. This enzyme cannot function in the anaerobic rumen without an alternative electron acceptor.
- The only viable path is coupling with quinone mediators (Candidate 8.1): NADH → Nox → FAD → quinone → terminal acceptor. But this creates a multi-component system of cascading complexity.
- Forge correctly identified this as "most speculative" and "low priority unless 8.1 works."

**Wet-lab confirmation type:**
- Proof-of-concept ONLY: In vitro NADH → Nox → quinone → Fe³⁺ electron transfer chain in defined buffer. If the complete chain functions, then test in rumen fluid.

---

### Candidate 9.1: Pre-Adaptation Protocol — Non-obvious

**Resolved Identity:**
- N/A — protocol-level intervention, not a molecular target
- Components: (1) Low-dose fumarate for 3-4 weeks, (2) Acetogen DFM, (3) Then introduce 3-NOP

**Feasibility:**
- Fumarate expands *Prevotella* and *Succiniclasticum* in vitro (Zhang et al., 2022) [MODERATE]
- 3-NOP stimulates *Ca.* Faecousia acetogens (Pope et al., 2025) [PRELIMINARY]
- Sequential protocol: each component has partial evidence; the combination is untested
- Commercially: 3-4 week lead time before inhibitor use is inconvenient but not prohibitive for feedlot programs (animals are typically in feedlots for 100-180 days)

**Verdict:** CONFIRMED
- The protocol is the most immediately actionable intervention — no engineering required, components are available.
- Validates Gate 1 (population installation) as binding constraint.

**Wet-lab confirmation type:**
- Crossover trial: simultaneous vs. sequential 3-NOP + fumarate + DFM introduction; measure H₂ accumulation and microbial community composition at weeks 2, 4, 6

---

### Candidate 9.2: Phage-Mediated Methanogen Suppression — Non-obvious

**Resolved Identity:**
- *Methanobrevibacter*-targeting phage identified from rumen samples (Gilbert et al., 2020)
- Phage are obligately lytic or temperate; strain-specific

**Key Risk Assessment:**
- Phage are strain-specific → rumen *Methanobrevibacter* diversity allows escape mutants
- Phage resistance develops rapidly (CRISPR-Cas defense in archaea is highly efficient)
- Phage does NOT solve H₂ disposal — it creates the problem (by suppressing methanogens without providing alternative sinks)
- Sapper's failure analysis explicitly flagged this limitation

**Verdict:** FLAGGED
- Phage as a sole intervention creates the H₂ accumulation problem without solving it. Only viable as an adjunct to a validated sink intervention.
- Rapid resistance development in archaea (which have sophisticated CRISPR-Cas systems) further limits utility.

**Wet-lab confirmation type:**
- Only pursue if combined with validated sink. Phage cocktail + acetogen DFM + 3-NOP in RUSITEC; measure H₂ dynamics and methanogen resistance emergence over 4 weeks.

---

### Candidate 9.3: Early-Life Rumen Programming — Non-obvious

**Resolved Identity:**
- N/A — developmental window intervention
- Based on Pope et al. (2025): 51 dairy calves showed "remodeling" of fermentative communities under 3-NOP
- Berkeley/Davis "once-at-birth probiotic capsule" concept

**Feasibility:**
- Early-life microbial colonization window is established in rumen development biology [MODERATE]
- 3-NOP in pre-ruminant calves may not create sufficient H₂ pressure to select for acetogens (methanogenesis is minimal before weaning)
- Long-term persistence of early-established populations into adulthood: variable evidence

**Verdict:** CONFIRMED with CAVEATS
- Potentially transformative if early-life programming creates lasting microbiome shifts.
- Caveat: Long development timeline (need to track animals for 12-24 months). Not a near-term product path.

**Wet-lab confirmation type:**
- Longitudinal study: acetogen consortium at 1-2 weeks of age + low-dose 3-NOP at week 4; track acetogen persistence by 16S at weeks 4, 8, 16, 24

---

### Candidate X.1: Integrated AB03 Product — Novel (Combination)

**Resolved Identity:**
- Multi-component formulation combining: acetogen DFM, adhesin display, low-dose nitrate, redox mediator, short-term fumarate
- This is the eventual PRODUCT form — premature to test as a unit before individual components are validated

**Verdict:** CONFIRMED (as concept)
- Factorial design in RUSITEC (test components individually and in combinations) is the correct de-risk approach.
- Individual component validation should precede combination testing.

**Wet-lab confirmation type:**
- Factorial RUSITEC: 2^k design with k = 4-5 components; identify minimum effective combination

---

### Candidate X.2/V7: Phloroglucinol + *Coprococcus* — Non-obvious [FORGE + VULCAN PARTIAL CONVERGENCE]

**Resolved Identity:**
- Phloroglucinol: 1,3,5-trihydroxybenzene, PubChem CID 359, MW 126.11 g/mol
- Phloroglucinol reductase: EC 1.3.1.57, purified from *Eubacterium oxidoreducens* G-41 (Krumholz & Bryant, 1986)
  - Native MW: 78 kDa (homodimer, 33 kDa subunits)
  - Specific for phloroglucinol and NADPH
  - Temperature optimum: 40°C (near rumen temperature)
  - pH optimum: 7.8
- *Coprococcus* sp. Pe15: rumen isolate that degrades phloroglucinol to 2 acetate + 2 CO₂ per molecule
- In vivo data: 50.6% H₂ reduction + 93% formate reduction in Brahman steers (Martinez-Fernandez et al., 2017; n=8 steers, 16-day trial)

**CRITICAL CORRECTION — In Vivo Data Quality:**
- The 50.6% H₂ reduction result comes from n=8 steers in a SHORT 16-day trial
- The "205% weight gain improvement" cited by Forge is from the SAME trial with n=4 per group — this is almost certainly overstated due to small sample size and short duration
- Dairy cows (2024 study) showed NO metabolism of phloroglucinol — the effect is *Coprococcus*-dependent and this organism is not universally present
- The 450 g/day intraruminal delivery required is technically demanding; oral dosing not validated

**Vulcan Extension (V7):**
- Vulcan proposes engineering the phloroglucinol reductase pathway into a rumen acetogen (*E. limosum*) to create a dual-sink organism consuming H₂ via both WLP and phloroglucinol reduction
- This converts a "supplement + organism co-administration" approach into an engineered biology approach
- The enzyme is amenable to heterologous expression (small, cytoplasmic, NADPH-dependent)

**Verdict:** CORRECTED
- The dual H₂ + formate capture mechanism is genuinely unique and valuable. The 93% formate reduction is particularly significant.
- Corrections: (a) The weight gain data is unreliable (n=4, 16 days). (b) Effect is completely dependent on *Coprococcus* abundance, which varies across animals and breeds. (c) Requires high intraruminal dose.
- The Vulcan engineering approach (express PhlR in *E. limosum*) is more tractable than co-administration.

**Wet-lab confirmation type:**
- Two-track: (a) In vitro rumen fluid ± *Coprococcus* pre-establishment ± phloroglucinol under 3-NOP; measure H₂ + formate. (b) Express phloroglucinol reductase in *E. limosum*; measure phloroglucinol reduction under H₂/CO₂.

---

### Candidate X.3/V4: Formate Targeting / FHL Engineering — Non-obvious/Novel [FORGE + VULCAN CONVERGENCE]

**Resolved Identity:**
- *E. coli* formate hydrogen lyase (FHL): Structure solved by cryo-EM at 2.6 A (PDB 7Z0S; Steinhilper et al., Nature Comm, 2022)
  - 7 subunits: FdhF (formate dehydrogenase), HycE ([NiFe] hydrogenase), HycB/F/G (iron-sulfur relay), HycC/D (membrane anchor)
  - Iron-sulfur cluster relay connecting active sites at <14 A spacing
  - Reversible: can operate in both formate → H₂ + CO₂ and H₂ + CO₂ → formate directions
- Reversibility demonstrated in intact *E. coli* cells (Pinske, 2016, MicrobiologyOpen)
- At 54 μM dissolved H₂ (inhibited rumen): ΔG for CO₂ + H₂ → formate ≈ −13 kJ/mol (thermodynamically feasible)

**Structure Assessment:**
- PDB 7Z0S at 2.6 A provides exceptional structural detail
- An unpredicted metal-binding site near the FdhF-HycF interface may play a role in preventing reverse activity in vivo — this is the engineering target for biasing the reaction toward formate production
- The forward reaction (formate → H₂) is ~10x faster than reverse — overcoming this kinetic asymmetry is the key challenge

**Key Computational Finding:**
- The structural data provides a specific molecular target for directional engineering: the metal-binding site near FdhF-HycF interface
- Rational engineering of this site (mutagenesis to remove the kinetic bias) is now structurally informed
- However, expressing a 7-subunit membrane-anchored complex in a rumen organism is a major engineering challenge

**Verdict:** CONFIRMED
- The molecular target is exceptionally well-characterized (2.6 A cryo-EM structure, reversibility demonstrated, kinetic parameters known).
- The concept (convert H₂ to the more diffusible formate near production sites, then consume formate at distant locations) is mechanistically elegant and addresses the mass transfer bottleneck.
- Main challenge: heterologous expression of a complex 7-subunit membrane enzyme in a rumen organism. A simpler approach would be to overexpress just FdhF (formate dehydrogenase) with its electron transfer partner HycB, rather than the complete FHL complex.

**Wet-lab confirmation type:**
- In vitro proof-of-concept: add purified FHL (or *E. coli* overexpressing FHL) to rumen fluid with 3-NOP; measure formate accumulation and H₂ decrease over 6h

---

### Candidate 1.1/V8: Selective Endosymbiont Disruption — Non-obvious/Novel [FORGE + VULCAN CONVERGENCE]

**Resolved Identity:**
- Target: Endosymbiotic methanogens within ciliate protozoa hydrogenosomes
- Primary drug target: MCR (methyl-coenzyme M reductase) — same target as 3-NOP, but delivered intracellularly
- Vulcan's molecular decomposition: (a) lipophilic 3-NOP prodrug, (b) archaeal membrane-targeting peptides, (c) nanoparticle delivery

**Key Risk Assessment:**
- The protozoa-methanogen symbiosis may be OBLIGATE — protozoa may need their endosymbionts for H₂ removal from hydrogenosomes. Killing the endosymbiont may kill or impair the protozoan.
- Lipophilic prodrug approach is precedented (intracellular pathogen drug delivery, e.g., TB inside macrophages)
- Archaeal membrane targeting (ether-linked lipids) is theoretically feasible but no selective agents have been developed

**Verdict:** CONFIRMED with CAVEATS
- The concept is sound: endosymbiotic methanogens represent 9-37% of methanogenic H₂ flux and may be partially shielded from extracellular 3-NOP.
- Caveat 1: Obligate symbiosis risk — protozoa may die if endosymbionts are killed.
- Caveat 2: Novel medicinal chemistry required — no existing compounds are designed for this application.
- Caveat 3: The additional H₂ redirected (4-11 mol/day) is ADDITIVE to the H₂ accumulation problem, not a solution.

**Wet-lab confirmation type:**
- First test V8's Prediction V5: Does 3-NOP at standard doses penetrate protozoa and suppress endosymbiotic methanogenesis? Separate protozoa from free-living bacteria; measure per-fraction methanogenesis under 3-NOP.

---

### Candidate V3: Ferric Iron Chelate Electron Acceptor — Non-obvious [VULCAN ONLY — NEW]

**Resolved Identity:**
- Ferric citrate: PubChem CID 3659987; FDA-approved (Auryxia) for hyperphosphatemia in humans
- Fe³⁺/Fe²⁺ standard reduction potential: +0.77 V (vs SHE) — more favorable than CO₂/CH₄ (+0.17 V) and SO₄²⁻/H₂S (−0.22 V)
- Cattle safety: Tested at 200, 300, 400 mg Fe/kg DM in feedlot cattle (Drouillard et al., 2013; Ruiz-Moreno et al., 2016)

**CRITICAL CORRECTION — Stoichiometry:**
- Vulcan correctly identifies the magnitude problem: sinking 30% of displaced H₂ at 80% inhibition requires ~34 mol Fe³⁺/day = ~9.5 kg ferric citrate/day. **IMPRACTICAL.**
- At the highest tested dose (750 mg Fe/kg DM, 25 kg DMI): total iron = 18.75 g/day = 0.34 mol Fe³⁺ = 0.17 mol H₂ consumed. This is **<1% of displaced H₂ at 80% inhibition.**
- As a stoichiometric electron acceptor, ferric citrate is INSUFFICIENT.
- Vulcan acknowledges this: "the mechanism of action, if any, must be catalytic (community restructuring) rather than stoichiometric."

**Actual Demonstrated Effect:**
- 72-81% reduction in H₂S (hydrogen sulfide) in rumen fluid [MODERATE — Drouillard et al., 2013]
- Fe³⁺ outcompetes sulfate-reducing bacteria for electrons, shifting community away from H₂S producers [MODERATE]
- No demonstrated effect on H₂ accumulation or VFA profiles [NOT TESTED]

**Verdict:** CORRECTED
- The stoichiometry does not support ferric citrate as an H₂ sink. It is a SULFIDE REDUCER, not an H₂ sink.
- Possible secondary value: by suppressing sulfate-reducing bacteria, it may redirect their H₂ consumption capacity to other pathways. But this is speculative.
- Reclassify from "H₂ sink electron acceptor" to "community ecology modifier / H₂S suppressor."

**Wet-lab confirmation type:**
- In vitro rumen fluid + 3-NOP + ferric citrate (400 mg Fe/kg DM): measure dissolved H₂, H₂S, VFA profiles, iron-reducing bacteria abundance. Look for community restructuring effects, not direct H₂ sinking.

---

### Candidate V9: Reductive TCA Fragment (Autotrophic Propionogenesis from CO₂ + H₂) — Novel [VULCAN ONLY — NEW]

**Resolved Identity:**
- Synthetic pathway: pyc + ppc + mdh + fumB + frdABCD + scpABC + mmdA + hydABC + rnfABCDEF
- ~15-20 genes across 4 functional modules
- Net reaction: 3CO₂ + 7H₂ → propionate + 4H₂O (approximate)
- Individual enzymes well-characterized; combined autotrophic pathway has never been assembled

**Feasibility Assessment:**
- **ATP balance concern:** The pathway consumes 1 ATP at the CO₂ fixation step (pyruvate carboxylase). The fumarate reductase step generates ion gradient (via Rnf) for ATP synthesis. Whether the net ATP balance is positive depends on exact stoichiometry and coupling efficiency.
- **Engineering complexity:** ~20 genes in a single organism is at the upper limit of current synthetic biology in non-model organisms. This has been achieved in *E. coli* (e.g., synthetic carbon fixation cycles, Schwander et al., Science 2016) but not in rumen bacteria.
- **This is an extension of Forge Candidate 4.1** — the same logic (endogenous fumarate from CO₂ fixation) taken to its full autotrophic conclusion.

**Verdict:** FLAGGED
- The concept is thermodynamically sound and scientifically elegant. Individual enzymes are well-characterized.
- The engineering complexity (~20 genes) and uncertain ATP balance make this the highest-risk candidate in the portfolio.
- A staged approach is more tractable: start with 4.1 (ppc + frdABCD overexpression in a native propionate producer), then incrementally add modules.

**Wet-lab confirmation type:**
- First test in *E. coli* as proof-of-concept host: assemble complete pathway; grow under H₂/CO₂; measure propionate production and growth (indicating positive ATP balance)

---

## Structure Prediction Summary

### Pre-Computed Structures Available

| Target | PDB ID | Resolution | Method | Key Features |
|---|---|---|---|---|
| *T. kivui* HDCR complex | **7QV7** | 3.4 A | Cryo-EM | Hexameric filament; FdhF + HydA2 + HycB3/B4; 34 [4Fe-4S] clusters; membrane-anchored nanowire |
| *W. succinogenes* fumarate reductase | **1QLA** | 2.2 A | X-ray | FrdA (FAD), FrdB ([Fe-S] centers), FrdC (membrane anchor, 2 haem b) |
| *E. coli* FHL complex | **7Z0S** | 2.6 A | Cryo-EM | 7-subunit membrane complex; [NiFe] hydrogenase + FdhF; reversible; metal-binding site at FdhF-HycF interface |
| CODH/ACS (*M. thermoacetica*) | **1MJG** | 2.2 A | X-ray | 310 kDa bifunctional; NiFe4S4 A-cluster; gas tunnel connecting C-cluster to A-cluster |
| CODH/ACS (*M. thermophila*) hexamer | **9C0T** | varies | Cryo-EM | Methanogenic hexameric form |
| CODH/ACS (*C. autoethanogenum*) | **6YTT** | 3.0 A | X-ray | Clostridial variant |

### AF3 Submissions Requested

| Target | Rationale | Priority |
|---|---|---|
| Mru_1499 AdLP-D1 domain (aa 19-198) | Binding interface for H₂ producer attachment; needed for rational adhesin engineering | HIGH |
| *T. kivui* HDCR FdhF monomer at 39°C | Assess stability of thermophilic enzyme at rumen temperature; identify residues for mesophilic adaptation | HIGH |
| *E. limosum* Rnf complex (rnfABCDEF) | No experimental structure; needed to assess druggable/engineerable sites | MEDIUM |

**AF3 request files** should be prepared for Daniel's submission at alphafoldserver.com. I have not created these files because the sequences require extraction from genome databases — the specific FASTA sequences should be pulled from UniProt/NCBI for the exact strains above.

---

## Key Corrections and Flags for Reaper

### Corrections (Forge/Vulcan Claims That Need Updating)

1. **AQDS toxicity (8.1/V6):** AQDS is toxic to bacteria at >10 mM and to methanogens at 20 mM. Working range must stay below 5 mM. DHNA and riboflavin are safer alternatives for rumen application. The mediator concept is valid; the specific compound choice needs revision.

2. **Ferric citrate as H₂ sink (V3):** The stoichiometry makes this impractical as an H₂ sink (<1% of displaced H₂ at the highest safe dose). It is a H₂S suppressor and community modifier, not an H₂ sink. Reclassify.

3. **Phloroglucinol weight gain data (X.2):** The "205% weight gain improvement" is from n=4, 16-day trial. This is almost certainly overstated. The H₂ reduction (50.6%) and formate capture (93%) data are from n=8 and more reliable.

4. **PEP carboxylase expression level (4.1/V5):** Excessive ppc overexpression DECREASES growth and product formation in *E. coli*. Expression must be tuned, not maximized. This is a known metabolic engineering pitfall.

5. **CRISPR-edited methanogens (5.5):** Deleting *mcr* does not convert a methanogen to an acetogen — it kills it. The organism's sole energy source is methanogenesis. Converting to acetogenesis requires INSERTING an entire WLP (~15 genes), not just deleting mcr. The Berkeley/Davis program's framing as "editing" understates the engineering challenge.

### Flags (Material Risks for Reaper to Evaluate)

1. **DIET mechanism (2.3):** Rumen H₂ consumers lack the surface electron transfer proteins required for direct interspecies electron transfer. GAC may help via physical proximity (overlapping with 2.2), but the specific DIET claim is unsupported.

2. **NADH oxidase oxygen requirement (8.2):** Fundamentally incompatible with the anaerobic rumen. Only viable if coupled with quinone mediators (8.1), creating cascading complexity.

3. **Phage resistance (9.2):** Archaea have highly efficient CRISPR-Cas defense systems. Phage resistance will develop rapidly. Phage also does not solve H₂ disposal.

4. **A. woodii pH sensitivity (5.3):** pH optimum 7.0-7.5 vs rumen 5.5-7.0. Consider using *A. woodii* as a gene donor rather than trying to install it in the rumen.

5. **Ca. Faecousia cultivation (5.1):** Single-study dependency (Pope et al., 2025). No independent replication. H₂ threshold unknown.

6. **V9 ATP balance:** The full autotrophic propionogenesis pathway (~20 genes) has uncertain net ATP yield. May require heterotrophic supplementation, making it mixotrophic rather than truly autotrophic.

---

## Predictions for the Prediction Log

### Prediction S1: HDCR Activity at Rumen Temperature
- **Prediction:** *T. kivui* HDCR expressed in *E. limosum* will retain >30% of its thermophilic kcat (>800 s⁻¹) at 39°C, still providing >25x improvement over native *A. woodii* HDCR.
- **Test:** Express HDCR in *E. limosum*; measure CO₂ reduction kcat at 39°C vs 66°C.
- **If TRUE:** Thermophilic HDCR is directly usable without mesophilic adaptation.
- **If FALSE:** Directed evolution at 39°C is required, adding 3-6 months to the engineering timeline.

### Prediction S2: Adhesin Functional Expression in Bacteria
- **Prediction:** The Mru_1499 AdLP-D1 domain (aa 19-198), when displayed on *E. limosum* via sortase-mediated anchoring, will retain binding to *R. albus* (measurable by co-sedimentation assay) at >50% of the binding efficiency observed with the domain expressed as a soluble protein in *E. coli*.
- **Test:** Express AdLP-D1-sortase construct in *E. limosum*; co-culture with *R. albus*; quantify co-sedimentation.
- **If TRUE:** Bacterial surface display of the archaeal adhesin is functionally feasible — proceed to co-culture H₂ consumption assays.
- **If FALSE:** The adhesin requires archaeal-specific post-translational modifications for function. Alternative approach: synthetic adhesins (engineered binding peptides) rather than native archaeal protein.

### Prediction S3: DHNA as Rumen Electron Shuttle
- **Prediction:** DHNA at 10 μM in rumen fluid under 3-NOP will be cycled between oxidized and reduced forms by rumen bacteria (detectable by UV-Vis spectroscopy) and will increase total VFA production by >5% relative to 3-NOP alone within 24h in batch culture.
- **Test:** Batch rumen fluid incubation; spectrophotometric monitoring of DHNA redox state; GC for H₂ and VFA.
- **If TRUE:** The EET mechanism demonstrated in *L. plantarum* transfers to rumen mixed cultures — quinone-based electron shuttling is viable.
- **If FALSE:** Rumen bacteria lack the Ndh2/PplA-type NADH dehydrogenases required for quinone interaction, or DHNA is degraded/sequestered in rumen fluid. The mediator concept does not transfer from pure culture to complex community.

### Prediction S4: Prevotella Genetic Tools Availability
- **Prediction:** Within 24 months, at least one research group will publish a functional gene insertion/deletion system for *Prevotella ruminicola* or *P. brevis*, enabling the ppc/frdABCD overexpression proposed in Candidates 4.1/4.3.
- **Test:** Literature monitoring; preprint servers.
- **If TRUE:** Direct engineering of the most abundant rumen propionate producer becomes possible.
- **If FALSE:** All propionogenesis engineering must use surrogate chassis (*S. ruminantium*, *E. limosum* with heterologous pathway), which are ecologically less competitive in the rumen.

---

## Overall Assessment

### Strongest Candidates (Computationally Validated)

1. **5.2/V1 — HDCR Transplant:** Best-characterized molecular target. Structure at 3.4 A. 95x catalytic improvement. Genetic tools in host (*E. limosum*) are excellent. Temperature concern is addressable. **CONVERGENCE: VERY STRONG.**

2. **2.1/V2 — Adhesin Display:** Adhesin characterized, binding demonstrated, domain architecture known. First Big_1 domain expressed in *E. coli*. The spatial coupling logic is mechanistically sound. **CONVERGENCE: VERY STRONG.**

3. **8.1/V6 — Redox Mediator Shuttle (revised to DHNA/riboflavin):** EET mechanism established in *L. plantarum*. DHNA and riboflavin are non-toxic, biologically relevant. Cheapest to test of all candidates. **CONVERGENCE: VERY STRONG.** (AQDS replaced with safer alternatives.)

4. **5.1 — Ca. Faecousia Cultivation:** The organism that ACTUALLY responds in vivo. Genome available for guided cultivation. Single-study risk acceptable given strength of metagenomic/metatranscriptomic signal.

5. **4.1/V5 — PEP Carboxylase Engineering (staged approach):** Sound biochemistry with *E. coli* precedent. Realistic if targeted to *S. ruminantium* rather than *Prevotella*. Expression level optimization is critical.

### Weakest Candidates (Flags for Reaper)

1. **2.3 — DIET via conductive materials:** Mechanism mismatch — rumen H₂ consumers lack surface electron transfer proteins.
2. **8.2 — NADH oxidase:** Oxygen dependency is a fundamental barrier in the anaerobic rumen.
3. **9.2 — Phage + sink:** Rapid resistance; does not solve H₂ disposal.
4. **V3 — Ferric citrate as H₂ sink:** Stoichiometry makes it impractical (<1% of displaced H₂ at safe dose).
5. **V9 — Full autotrophic propionogenesis:** ~20-gene synthetic pathway with uncertain ATP balance.

---

*Survey complete. 25 merged candidates assessed. 6 pre-computed structures identified. 3 AF3 submissions requested. 5 corrections issued. 6 flags raised. 4 falsifiable predictions logged. All evidence tagged [COMPUTATIONAL].*
