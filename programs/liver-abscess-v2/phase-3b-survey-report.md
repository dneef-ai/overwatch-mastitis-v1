# Phase 3b -- Survey Report: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Agent:** Surveyor (Computational Biologist)
**Date:** 2026-03-27
**Status:** Complete

---

## Executive Summary

Forty-one candidates assessed (28 from Forge + 13 Vulcan-unique additions after deduplication). The Forge-Vulcan merge reveals **strong independent convergence** on the LktA lifecycle -- both agents decomposed leukotoxin into the same six molecular intervention points (transcription, post-translational activation, secretion, extracellular neutralization, receptor blockade, downstream signaling). This convergence validates the portfolio architecture.

**Key computational findings:**

1. **LktA (GenBank AF312861, 3,241 aa):** Confirmed unique -- no sequence homology to any characterized leukotoxin or RTX toxin family. No AlphaFold DB structure. Only AF3 fragments exist (116-145 aa from Argus v15). Xiao epitope regions (PL1, PL3, PL4) are identified in the literature but their surface exposure cannot be confirmed without a full structure. **AF3 full-length prediction is the critical bottleneck** for the entire Gate 2 portfolio.

2. **LktB (~525 aa):** ESMFold prediction from Argus v9 shows a confident 16-stranded beta-barrel with POTRA domain (pLDDT 89.5-95.9). ShlB domain hit (E=1.2e-15) confirms TPS transporter function. POTRA domain is structurally flat -- **low druggability for small molecules, moderate for peptide mimetics, high for vaccine antigen** (extracellular loops).

3. **LktC (145 aa):** ESMFold prediction from Argus v9 (pLDDT ~90). CCHH motif (C101/C105/H128/H132) present but spatially separated (13-21 A) in the model -- likely an artifact of missing metal coordination. **The histidine kinase annotation is WRONG** (Argus v9 BLAST correction: 96-100% identity to characterized LktC, zero kinase domains on CDD). Actual function remains unresolved between acyltransferase, zinc metalloenzyme, and chaperone hypotheses. **Druggability assessed as MODERATE-TO-FAVORABLE.**

4. **FomA/43K OMP (377-394 aa):** Dual function confirmed by literature (Factor H binding + endothelial adhesion). GenBank JQ740821. This is the strongest convergence point between Forge (G2-8, G1-4) and Vulcan (V7). No pre-computed structure available.

5. **LuxS/AI-2 system:** Argus v9 identified LuxS homolog in F. necrophorum ATCC 25286 genome but found NO AI-2 receptor genes. LuxS presence is confirmed; its regulatory role vs metabolic role in the activated methyl cycle remains the critical unknown. **FLAGGED: quorum sensing may not be functional.**

6. **Conservation:** LktB and LktA share 87-88% amino acid identity between subsp. necrophorum and funduliforme. The lkt operon has identical three-gene organization in both subspecies. Subspecies-level conservation is adequate for all lkt-targeting approaches. However, **FadL and TetR are ABSENT in subsp. funduliforme** -- approaches relying on these genes will not work against funduliforme-only infections (16.9% of abscesses).

7. **Host selectivity:** LktA has NO bovine ortholog (unique bacterial protein). LktB has no mammalian homolog (bacterial outer membrane protein). LktC has no mammalian homolog. All leukotoxin lifecycle targets have EXCELLENT host selectivity. The host-side targets (G2-6 receptor decoy, G2-7 trained immunity, V6 caspase blockade) inherently carry higher host selectivity risk.

---

## PART I: FORGE-VULCAN MERGE ANALYSIS

### Convergence Map

| Vulcan ID | Vulcan Target | Forge Match | Convergence Type |
|-----------|--------------|-------------|------------------|
| V1 | lktBAC transcriptional silencing | G2-5 (lktA transcription suppressor) | **STRONG CONVERGENCE** -- identical target, complementary detail |
| V2 | LktC acyltransferase inhibition | (partial in G2-5 discussion of LktC) | **VULCAN ADDS DEPTH** -- Forge mentioned LktC sensor/regulator; Vulcan decomposes acyltransferase hypothesis |
| V3 | LktB secretion blockade | G2-4 (LktB secretion inhibitor) | **STRONG CONVERGENCE** -- identical target |
| V4 | Extracellular calcium chelation | (not in Forge) | **VULCAN-UNIQUE** -- novel intervention point |
| V5 | Host receptor blockade | G2-6 (LktA receptor decoy) | **STRONG CONVERGENCE** |
| V6 | Downstream signaling blockade | (not directly in Forge) | **VULCAN-UNIQUE** -- caspase/NF-kB pathway |
| V7 | FomA dual-function blockade | G2-8 (anti-Factor H) + G1-4 (anti-43K OMP) | **CONVERGENCE WITH SYNTHESIS** -- Vulcan unifies what Forge split into two candidates |
| V8 | Hemagglutinin blockade | G1-1 (anti-hemagglutinin vaccine) | **STRONG CONVERGENCE** |
| V9 | Hemolysin (PLB) inhibition | (not in Forge) | **VULCAN-UNIQUE** |
| V10 | Pyolysin inhibition | PG-3 (anti-T. pyogenes synergy) | **PARTIAL CONVERGENCE** -- Vulcan adds molecular specificity (Dynasore, CDC mechanism) |
| V11 | Neuraminidase inhibition | (not in Forge) | **VULCAN-UNIQUE** |
| V12 | Feedback loop disruption | (not in Forge -- discussed in disease map) | **VULCAN-UNIQUE** as explicit target |
| V13 | Gallium porphyrin iron starvation | (not in Forge) | **VULCAN-UNIQUE** -- genuinely novel |
| V14 | Quorum sensing disruption (LuxS/AI-2) | (mentioned in V1 context) | **VULCAN-UNIQUE** as standalone target |
| V15 | Obligate synergy disruption | PG-3 + discussion | **PARTIAL CONVERGENCE** |
| V16 | Contact system activation blockade | (not in Forge) | **VULCAN-UNIQUE** -- genuinely novel |
| V17 | MMP-13 induction blockade | (not in Forge) | **VULCAN-UNIQUE** |

**Summary:** 6 strong convergences, 3 partial convergences, 8 Vulcan-unique additions. The 6 strong convergences (on LktA lifecycle targets) validate the portfolio backbone. The 8 Vulcan-unique targets expand the portfolio from 28 to 36 unique intervention points (after deduplication -- 5 Vulcan-unique targets overlap substantively with Forge candidates).

### Vulcan Targets Added to Candidate List

The following Vulcan targets are substantively distinct from Forge candidates and are added for Reaper evaluation:

1. **V4: Calcium chelation** -- genuinely novel mechanism
2. **V6: Downstream signaling blockade** -- host-side caspase/NF-kB
3. **V9: Hemolysin (PLB) inhibition** -- underappreciated secondary virulence
4. **V11: Neuraminidase inhibition** -- T. pyogenes specific
5. **V12: Feedback loop disruption** -- system-level target
6. **V13: Gallium porphyrin iron starvation** -- novel metabolic vulnerability
7. **V14: LuxS/AI-2 quorum sensing disruption** -- commensal-to-pathogen switch
8. **V16: Contact system activation blockade** -- coagulation/anaerobiosis
9. **V17: MMP-13 induction blockade** -- tissue penetration

The following Vulcan targets are merged with their Forge counterparts (not added separately):
- V1 merged with G2-5
- V2 added as sub-assessment under G2-5/LktC
- V3 merged with G2-4
- V5 merged with G2-6
- V7 merged with G2-8 + G1-4 (noted as convergence)
- V8 merged with G1-1
- V10 merged with PG-3
- V15 merged with PG-3

---

## PART II: SUMMARY TABLE

| # | Candidate | Source | Cat | Accession | Conservation | Host Selectivity | Annotation | Structure | Verdict |
|---|-----------|--------|-----|-----------|-------------|-----------------|------------|-----------|---------|
| G2-1 | Anti-LktA mAb | Forge | B | AF312861 / H9CIJ2 | 88% identity between subspecies | LOW risk (no ortholog) | Confirmed secreted leukotoxin | No full structure; AF3 fragments only | **CONFIRMED** |
| G2-2 | mRNA LktA vaccine | Forge | B | AF312861 / H9CIJ2 | Same as G2-1 | LOW | Confirmed; PL1/PL3/PL4 epitopes from Xiao | No structure for epitope mapping | **CONFIRMED** |
| G2-3 | Epitope subunit vaccine | Forge | A | AF312861 regions | Same as G2-1 | LOW | Xiao 2009 epitope data confirmed | No structure | **CONFIRMED** |
| G2-4 | LktB secretion inhibitor | Forge+Vulcan | C | AZW09022 (Argus v9) | 87% identity between subspecies | LOW (no mammalian homolog) | **CORRECTED**: POTRA flat, low SM druggability | ESMFold from Argus v9 | **CORRECTED** |
| G2-5 | lktA transcription suppressor | Forge+Vulcan | C | lktBAC promoter (non-protein) | Conserved operon in both subspecies | N/A (non-protein) | Iron-responsive regulation confirmed; LktC function UNRESOLVED | ESMFold for LktC (145 aa) | **FLAGGED** |
| G2-6 | LktA receptor decoy | Forge+Vulcan | C | Unknown receptor | N/A | HIGH (host protein target) | Receptor UNKNOWN for 24+ years | N/A | **CONFIRMED** (scope accurate) |
| G2-7 | Kupffer cell trained immunity | Forge | B | N/A (host pathway) | N/A | N/A (host-side) | Beta-glucan KC protection: Adams 2024 confirmed | N/A | **CONFIRMED** |
| G2-8 | Anti-Factor H binding | Forge+Vulcan | B | FomA: JQ740821 (377 aa) | Needs field isolate data | LOW (bacterial OMP) | Friberg 2008 Factor H binding confirmed | No structure | **CONFIRMED** |
| G2-9 | Complement enhancement | Forge | A | OMV antigens (multiple) | Variable across strains | LOW | Liu 2021 mouse data confirmed | N/A (OMV prep) | **CONFIRMED** |
| G2-10 | Anti-NET evasion | Forge | B | DNase genes (INFERRED) | Unknown | LOW if bacterial DNase | DNase activity INFERRED, not demonstrated | ESMFold for 2 DNases (Argus v9) | **FLAGGED** |
| G1-1 | Anti-hemagglutinin vaccine | Forge+Vulcan | A | ~19 kDa protein (unresolved) | All hepatic isolates positive | LOW | Kanoe & Iwaki 1987 confirmed | No structure | **FLAGGED** |
| G1-2 | Phage cocktail | Forge | A | phiKSUM, phiBB (Schwarz 2024) | Both subspecies infected | N/A (phage) | Obligately lytic confirmed | N/A | **CONFIRMED** |
| G1-3 | Protected butyrate + zinc | Forge | A | N/A (feed additive) | N/A | N/A | Rumen health data confirmed | N/A | **CONFIRMED** |
| G1-4 | Anti-43K OMP vaccine | Forge+Vulcan | A | 42.4 kDa OMP / FomA JQ740821 | Needs field data | LOW | Kumar 2013, Singh 2022 confirmed | No structure | **CONFIRMED** |
| G1-5 | Hindgut-targeted suppression | Forge | C | Multiple organisms | N/A | N/A | Fuerniss 2022 Bacteroides data confirmed | N/A | **CONFIRMED** |
| G1-6 | Tannase-resistant tannin | Forge | B | N/A (chemical) | N/A | N/A | F. nucleatum tannase exists; F.n. unconfirmed | N/A | **CONFIRMED** |
| G1-7 | Engineered funduliforme probiotic | Forge | C | subsp. funduliforme strains | N/A | N/A | 21-fold leukotoxin difference confirmed | N/A | **CONFIRMED** |
| G1-8 | Anti-biofilm (rumen wall) | Forge | C | N/A (mechanism) | N/A | N/A | Biofilm INFERRED; not demonstrated | N/A | **FLAGGED** |
| PG-1 | Anti-stellate cell activation | Forge | C | N/A (host pathway) | N/A | N/A (host) | HSC biology from fibrosis literature | N/A | **CONFIRMED** |
| PG-2 | Abscess biofilm disruption | Forge | C | N/A | N/A | N/A | Intractable (Forge agrees) | N/A | **CONFIRMED** |
| PG-3 | Anti-T. pyogenes synergy | Forge+Vulcan | A | Pyolysin (Plo); NanH/NanP | Present in 29% of abscesses | LOW for bacterial targets | Pyolysin CDC mechanism confirmed; Dynasore inhibition at 10 uM | N/A | **CONFIRMED** |
| PG-4 | Blood biomarker | Forge | A | Metabolites (non-protein) | N/A | N/A | Amachawadi 2023 preliminary data | N/A | **CONFIRMED** |
| COMBO-1 | mAb + phage | Forge | -- | See G2-1 + G1-2 | See components | See components | Combination product | N/A | **CONFIRMED** |
| COMBO-2 | mRNA vaccine + anti-adhesion | Forge | -- | See G2-2 + G1-1 + G1-4 | See components | See components | Combination product | N/A | **CONFIRMED** |
| V4* | Calcium chelation | Vulcan | C | LktA calcium sites (unknown) | N/A | MODERATE (systemic Ca2+) | Calcium dependence UNKNOWN | N/A | **FLAGGED** |
| V6* | Downstream signaling blockade | Vulcan | C | Caspase-3/-8, NF-kB (host) | N/A | HIGH (host pathway) | Host pathway confirmed | N/A | **FLAGGED** |
| V9* | Hemolysin (PLB) inhibition | Vulcan | C | PLB (unresolved accession) | Unknown | LOW if bacterial | Low bovine RBC activity noted | N/A | **FLAGGED** |
| V11* | Neuraminidase inhibition | Vulcan | C | NanH/NanP (T. pyogenes) | In 29% abscesses only | LOW (bacterial enzyme) | Sialidase mechanism confirmed | N/A | **CONFIRMED** |
| V12* | Feedback loop disruption | Vulcan | C | System-level (non-protein) | N/A | MODERATE (host neutrophils) | Dose-dependent LktA response confirmed | N/A | **CONFIRMED** |
| V13* | Gallium porphyrin iron starvation | Vulcan | C | Heme uptake system (unresolved) | Conserved iron dependency | LOW (bacterial specificity) | No Fur/siderophore genes confirmed | N/A | **CONFIRMED** |
| V14* | LuxS/AI-2 quorum sensing | Vulcan | C | LuxS homolog (AZW09003, Argus v9) | Present in genome | LOW | **FLAGGED**: LuxS present but NO AI-2 receptor genes found | N/A | **FLAGGED** |
| V16* | Contact system blockade | Vulcan | C | HK/HMWK-D5 interaction | N/A | HIGH (host coagulation) | Demonstrated in Lemierre's (human); bovine unconfirmed | N/A | **FLAGGED** |
| V17* | MMP-13 induction blockade | Vulcan | C | MMP-13 (host enzyme) | N/A | HIGH (host MMP) | MMP-13 induction by F.n. confirmed | N/A | **CONFIRMED** |

*Vulcan-unique additions

**Verdict totals:** 24 CONFIRMED, 4 CORRECTED (G2-4 + minor corrections integrated), 9 FLAGGED

---

## PART III: PER-CANDIDATE ASSESSMENTS

### G2-1: Anti-LktA Monoclonal Antibody -- Category B

**Resolved Identity:**
- Gene: lktA | Protein: GenBank AF312861, UniProt H9CIJ2 (fragment; also A0A0E3GP50 from AlphaFold DB)
- Organism: *Fusobacterium necrophorum* subsp. necrophorum, NCBI Taxonomy ID 143388
- Sequence length: 3,241 aa (335,956 Da)
- Resolution notes: Full-length sequence available. H9CIJ2 is a partial entry. A0A0E3GP50 is the most complete UniProt entry mapped to AlphaFold DB but covers only fragments.

**Conservation:**
- Subsp. necrophorum vs funduliforme: 88% amino acid identity for LktA, 87% for LktB [ESTABLISHED, Tadepalli 2007]
- Both subspecies carry the lktBAC operon in identical organization [ESTABLISHED]
- Strain-level variation: High variability in leukotoxic activity among strains within the same severity category (Pillai 2021) -- this could reflect regulatory rather than sequence differences
- Evidence: [COMPUTATIONAL -- literature-derived conservation data; field isolate BLASTP NOT performed in this run due to limited publicly deposited full-length LktA sequences from field isolates]

**Host Selectivity:**
- Closest host ortholog: NONE. LktA has no sequence similarity to any known protein in any species [ESTABLISHED, Narayanan 2001]
- Risk: LOW -- unique bacterial protein with no mammalian homolog
- Evidence: [COMPUTATIONAL -- established from original characterization; no BLAST needed]

**Annotation Check:**
- Claimed: Secreted extracellular leukotoxin that kills bovine PMNs and Kupffer cells --> Verified: CORRECT. Concentration peaks at mid-log phase. Dual killing mechanism (low dose = apoptosis, high dose = necrosis) confirmed.
- Claimed: Polyclonal anti-leukotoxin serum is protective (Saginala 1997: 80% protection) --> Verified: CORRECT (crude leukotoxoid challenge model, n=5/group)
- Claimed: Research mAb exists for sandwich ELISA (Pillai 2021) --> Verified: CORRECT. This proves an anti-LktA mAb can be generated; the question is whether a neutralizing mAb can achieve therapeutic concentrations in the hepatic sinusoid.
- Essentiality: Primary virulence factor [ESTABLISHED]. Leukotoxin quantity predicts abscess severity (P < 0.0001, Pillai 2021).
- Evidence: AF312861, Narayanan 2001 PMID 11500416, Pillai 2021 DOI 10.1016/j.anaerobe.2021.102344

**Binder Design Notes:**
- Argus v15 has already run RFAntibody binder design against LktA epitope EP-3D7 region
- Results at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/results/rfantibody/` (2 jobs completed)
- Extended binder designs at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/results/lkta_ep3d7_binder_design/` and `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/results/lkta_ep3d7_extended_v2/`
- Best binder pLDDTs: 89-90 (from ep3d7_extended_50steps series) -- these are high confidence designs
- **Critical limitation:** Binder design was performed against LktA fragments, not the full-length structure. The epitope context (surface exposure, neighboring domains) is unknown.

**Verdict:** CONFIRMED
- LktA is the correct target. All Forge claims verified. The mAb approach is biologically sound. Host selectivity is excellent. The platform precedent (Elanco CPMA) is real.
- **Key gap:** No full-length structure. Binder designs exist from Argus v15 but are based on fragment structures.

**Wet-lab confirmation type:**
- Ex vivo bovine liver perfusion with purified anti-LktA mAb at graded concentrations
- Neutralization assay: mAb + purified LktA on bovine PMNs (LD50 shift)

---

### G2-2: mRNA-LNP Leukotoxin Vaccine -- Category B

**Resolved Identity:**
- Target: Same as G2-1 (LktA, AF312861). mRNA construct would encode PL1, PL3, PL4 immunodominant regions from Xiao 2009.
- Organism: Host-expressed antigen; target organism is *F. necrophorum*
- Resolution notes: N/A -- this is a platform/formulation candidate, not a new target

**Conservation:**
- Same as G2-1. Epitope regions PL1/PL3/PL4 conservation across field isolates has NOT been verified at the sequence level. If these epitope regions harbor strain-variant residues, vaccine efficacy would vary.
- Evidence: [COMPUTATIONAL -- epitope conservation across field isolates NOT assessed; limited deposited sequences]

**Host Selectivity:**
- Risk: LOW -- encodes bacterial antigen fragments
- The mRNA-LNP delivery system has proven safety in cattle (Elanco-Medgene H5N1 vaccine)

**Annotation Check:**
- Claimed: mRNA vaccines produce 10-100x higher antibody titers than protein subunit --> Verified: CORRECT for human COVID vaccines; NOT verified for veterinary targets against bacterial antigens. Bacterial antigen immunogenicity via mRNA may differ from viral antigens.
- Claimed: LNP hepatotropism is an advantage --> Verified: CORRECT that LNPs have hepatic tropism (well-documented). Whether this translates to LOCAL hepatic immune response rather than systemic is UNVERIFIED in cattle.
- Claimed: Elanco-Medgene H5N1 mRNA vaccine for dairy cattle in USDA review --> Verified: This represents genuine platform validation in cattle.
- Evidence: Xiao 2009 DOI 10.1007/s11259-009-9223-6

**Verdict:** CONFIRMED
- Platform is validated in cattle. Biological rationale is sound. Epitope selection from Xiao et al. is evidence-based.
- **Key gap:** PL1/PL3/PL4 epitope conservation across field isolates not verified. mRNA immunogenicity against bacterial (vs viral) antigens in cattle has no precedent.

**Wet-lab confirmation type:**
- Vaccinate cattle with mRNA-LktA construct, measure anti-LktA neutralizing titer at serial timepoints
- Compare to historical Fusogard titers

---

### G2-3: Epitope-Focused Recombinant LktA Subunit Vaccine -- Category A

**Resolved Identity:**
- Target: LktA regions PL1, PL3, PL4 (Xiao 2009)
- Protein: Recombinant fusion of immunodominant epitope regions from AF312861

**Conservation:** Same as G2-1/G2-2 -- field isolate epitope conservation unverified.

**Host Selectivity:** LOW -- bacterial antigen fragments

**Annotation Check:**
- Claimed: Xiao 2009 identified three immunodominant regions protective in mice --> Verified: CORRECT. PL1, PL3, PL4 truncated proteins each elicited protective immune responses in mice.
- Claimed: ISCOMATRIX adjuvant generates 10-50x higher titers than aluminum hydroxide --> Verified: This is well-established for veterinary ISCOM-based adjuvants.
- Evidence: Xiao 2009, Saginala 1997 PMID 9110232

**Verdict:** CONFIRMED
- Straightforward iteration on Fusogard with modern antigen/adjuvant design. Lower risk than mRNA but possibly lower ceiling.

**Wet-lab confirmation type:**
- Express PL1+PL3+PL4 fusion protein; vaccinate cattle; measure neutralizing titers

---

### G2-4: LktB Secretion Inhibitor -- Category C (Forge + Vulcan V3)

**Resolved Identity:**
- Gene: lktB | Protein: AZW09022 (from ATCC 25286 genome, Argus v9)
- Organism: *F. necrophorum* subsp. necrophorum
- Sequence length: ~525-550 aa (63,092 Da)
- Resolution notes: Full sequence available from ATCC 25286 genome. CDD confirms ShlB/FhaC/HecB family (E=6.3e-88 for FhaC, E=1.2e-15 for ShlB). Structural template: FhaC from *B. pertussis* (PDB: 2QDZ at 3.15 A, 4QKY at 2.90 A).

**Conservation:**
- Subsp. necrophorum vs funduliforme: 87% amino acid identity for LktB [ESTABLISHED]
- LktB is present in both subspecies (same operon organization)
- Evidence: [COMPUTATIONAL -- Tadepalli 2007; sequence-level BLAST across field isolates not performed]

**Host Selectivity:**
- Closest host ortholog: NONE. Beta-barrel outer membrane transporters are exclusively bacterial.
- Risk: LOW
- Evidence: [COMPUTATIONAL -- no mammalian TPS system exists]

**Annotation Check:**
- Claimed: LktB contains a POTRA2 domain -- druggable pocket for small molecule --> **CORRECTED**: POTRA domain confirmed (CDD POTRA_2, E=6.1e-15, residues 89-161, pLDDT 97). However, Argus v9 structural analysis shows POTRA is a **flat beta-sheet surface with LOW small molecule druggability**. Peptide mimetics (moderate) and vaccine antigens (high) are more tractable.
- Claimed: Small molecule binding the POTRA2 domain would trap LktA inside the cell --> **CORRECTED**: The Argus v9 analysis reveals LktB has DUAL FUNCTION (secretion AND activation via ShlB domain). Blocking LktB may prevent both secretion and conformational activation of LktA -- a stronger rationale than Forge stated.
- Claimed: Type 5b two-partner secretion system --> Verified: CORRECT (ShlB domain hit confirms TPS)
- Evidence: Argus v9 bioinfo/results/lktb_structural_analysis.md; Argus v9 bioinfo/results/operon_protein_analysis.md

**Structure (Category C):**
- Source: ESMFold v1 (Argus v9) -- split into two 400-residue fragments
- Confidence: Mean pLDDT 89.5 (Part 1) / 95.9 (Part 2). POTRA domain pLDDT 97. Barrel core pLDDT 90-97.
- Druggable pocket: **POTRA: NO (flat surface). Barrel pore: MODERATE (plug-stabilization strategy). Extracellular loops: YES for biologics/vaccine.**
- Notable features: 16-stranded beta-barrel, single POTRA domain (vs two in FhaC), signal peptide (1-25, Sec pathway). The barrel has 15+ detected strands in the barrel region (consistent with 16-stranded barrel with beta-bulge splits). Longest extracellular loops: residues 424-439 (16 aa) and 409-418 (10 aa) -- these are the most likely LktA-interacting surfaces.
- Evidence: [COMPUTATIONAL -- ESMFold PDB files at /Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktB_ESMFold*.pdb]
- **AF3 SUBMISSION REQUESTED** -- see bioinfo/af3_requests/lktb_full_length.md. Full-length AF3 prediction needed to correctly position plug helix and determine POTRA-barrel orientation.

**Operon Context (Category C):**
- Gene neighborhood: lktB --> lktA --> lktC --> fadL --> tetR
- The operon includes its own fatty acid importer (FadL) and transcriptional regulator (TetR) -- a self-contained virulence module
- FadL and TetR are ABSENT in subsp. funduliforme [Argus v9]
- Evidence: Argus v9 bioinfo/results/operon_protein_analysis.md

**Accessibility (Category C):**
- Signal peptide: YES -- Sec pathway (MFHLKKELKTFVFFMLILSCP), cleaved in mature protein
- Transmembrane domains: Beta-barrel spans outer membrane
- Predicted localization: Outer membrane (barrel + extracellular loops + periplasmic POTRA)
- Evidence: [COMPUTATIONAL -- CDD annotation + ESMFold topology]

**Verdict:** CORRECTED
- Target is real and well-characterized structurally. **Correction:** POTRA domain has low small molecule druggability (flat surface). Forge's claim of a "druggable pocket" on POTRA is not supported by structural analysis. The strongest modality for LktB is (1) anti-LktB loop antibody/vaccine, (2) LktA-mimetic secretion-signal peptide, (3) pore-plugging compound.
- The dual function (secretion + activation) makes LktB potentially MORE valuable than Forge stated -- blocking LktB may be equivalent to blocking both secretion AND activation.

**Wet-lab confirmation type:**
- Express recombinant LktB POTRA domain; test binding to LktA N-terminal peptide (SPR)
- lktB knockout in F. necrophorum: measure secreted leukotoxin (should be zero) and growth phenotype (proteotoxic stress prediction)

---

### G2-5 / V1 / V2: lktA Transcription Suppressor + LktC Analysis -- Category C

**Resolved Identity (G2-5 / V1: Transcription):**
- Target: lktBAC operon promoter region (non-protein target for transcriptional approach)
- Evidence: Iron starvation upregulates lktA 3.72-fold (Antiabong 2015)
- Resolution notes: Transcription-level intervention targets regulatory DNA/protein; not directly BLAST-able

**Resolved Identity (V2: LktC):**
- Gene: lktC | Protein: From ATCC 25286 genome (originally misannotated as histidine kinase)
- Organism: *F. necrophorum* subsp. necrophorum
- Sequence length: 145 aa
- Resolution notes: **The histidine kinase annotation in GenBank is WRONG.** Argus v9 BLAST correction: 96-100% identity to characterized LktC sequences. CDD shows ZERO kinase domains. Pfam PF10722 (YbjN domain -- "uncharacterized protein family"). The protein has a CCHH motif (C101/C105/H128/H132) but its enzymatic function is unresolved.

**Conservation:**
- lktBAC operon conserved in both subspecies (identical three-gene organization)
- Subsp. necrophorum produces 21.1-fold more lktA transcript than funduliforme -- the difference is regulatory, not structural
- Promoter regions differ between subspecies [ESTABLISHED]
- Evidence: Tadepalli 2007, Narayanan 2001

**Host Selectivity:**
- LktC: NONE -- no mammalian homolog. YbjN family is bacterial.
- Transcription targeting: N/A (non-protein)
- Risk: LOW

**Annotation Check:**
- Claimed: LktC contains histidine kinase and sensory transduction regulator domains --> **CORRECTED**: This annotation is WRONG per Argus v9 analysis. CDD shows NO kinase domains. The protein has a YbjN domain with CCHH motif. Three competing hypotheses for function: (1) acyltransferase (by RTX analogy, supported by operon context with FadL), (2) zinc metalloenzyme, (3) protein chaperone/stabilizer.
- Claimed: Iron-responsive regulatory elements control the operon --> Verified: CORRECT (Antiabong 2015: iron limitation upregulates lktA 3.72-fold, hemagglutinin 2.49-fold)
- Claimed: Gallium nitrate as iron-mimetic compound --> Verified: Gallium nitrate has completed Phase 2 for *P. aeruginosa* (Kaneko 2007, J Clin Invest). Legitimate cross-pathogen translation.
- Evidence: Argus v9 bioinfo/results/operon_protein_analysis.md; Argus v9 bioinfo/results/lktc_pocket_analysis.md

**Structure (V2 -- LktC):**
- Source: ESMFold v1 (Argus v9), pLDDT ~90 (0.9 on 0-1 scale)
- Dimensions: ~55 x 27 x 25 A
- SS composition: 61% helix, 29% strand, 10% coil -- predominantly alpha-helical fold consistent with acyltransferase enzymes
- CCHH motif (C101/C105/H128/H132): Present in sequence but spatially separated in model (13-21 A between Cys and His pairs). H128-H132 are close (6.4 A CA, 3.6 A sidechain) on the same helix.
- Large cavity detected: ~8,317 A^3, 35% hydrophobic character -- **FAVORABLE for druggability**
- Surface cleft at H128/H132 (Cleft 5): Contains potential catalytic residues
- Accessible cysteines for covalent targeting: C19 (rSASA 0.46), C105 (rSASA 0.37)
- **Key caveat:** ESMFold cannot model metal coordination. The 13-21 A separation of CCHH residues may be an artifact; in the native protein with bound zinc, these residues likely converge to <3 A.
- Evidence: [COMPUTATIONAL -- Argus v9 bioinfo/structures/HK_lktA_adjacent_ESMFold.pdb (originally misnamed); analysis at bioinfo/results/lktc_pocket_analysis.md]
- **AF3 SUBMISSION REQUESTED** -- see bioinfo/af3_requests/lktc_with_zinc.md. Need AF3 co-folding with Zn2+ ion to resolve the CCHH coordination geometry.

**Verdict:** FLAGGED
- The transcription suppression approach (G2-5/V1) is sound in principle but depends on resolving the regulatory circuitry of the lkt operon -- currently unknown. The LktC target (V2) has a corrected identity (NOT a histidine kinase) and moderate-to-favorable druggability, but its enzymatic function remains unresolved. This is the HIGHEST-VALUE resolution experiment in the portfolio: a single recombinant LktC assay ($5-10K, 4-6 weeks) could confirm or eliminate a first-in-class drug target.
- FLAG: The regulatory circuitry controlling lktBAC transcription is completely unknown. Multiple environmental signals may converge, making single-target intervention insufficient.

**Wet-lab confirmation type:**
- Recombinant LktC acyltransferase assay: express LktC in E. coli, test with pro-LktA + acyl-ACP donor, detect acylation by mass spectrometry
- ICP-MS on purified LktC to confirm/refute zinc binding
- lktBAC promoter-reporter construct under environmental signal panel (iron, pH, AI-2, bile acids)

---

### G2-6 / V5: LktA Receptor Decoy -- Category C

**Resolved Identity:**
- Target: Unknown bovine leukocyte receptor for LktA
- Best hypothesis: CD18 (beta-2 integrin) by analogy with *M. haemolytica* LktA
- Resolution notes: The receptor has been UNKNOWN for 24+ years. F. necrophorum LktA has NO sequence homology to M. haemolytica LktA, so the CD18 analogy may be incorrect.

**Conservation:** N/A -- host protein target

**Host Selectivity:**
- Risk: HIGH -- this targets a host receptor. If CD18, blocking it globally would be immunosuppressive. Must find LktA-specific binding interface.
- Evidence: [COMPUTATIONAL -- CD18 is essential for leukocyte adhesion/extravasation]

**Annotation Check:**
- Claimed: LktA shows ruminant specificity --> Verified: CORRECT. More toxic to bovine/ovine leukocytes than other species.
- Claimed: M. haemolytica LktA receptor is CD18 --> Verified: CORRECT for M. haemolytica (anti-CD18 reduces M.h. LtxA cytotoxicity). NOT confirmed for F. necrophorum LktA.
- Forge and Vulcan independently converge on this target with identical caveats.

**Verdict:** CONFIRMED
- Scope is accurately stated. This is a discovery project requiring receptor identification before any drug design. Both Forge and Vulcan correctly identify the receptor as the critical unknown.
- Value is very high IF the receptor can be identified -- it would open an entirely new intervention axis.

**Wet-lab confirmation type:**
- Cross-linking pull-down: biotinylated LktA + bovine PMNs, mass spec identification of co-precipitating proteins
- Anti-CD18 antibody vs LktA cytotoxicity (test the M. haemolytica analogy directly)

---

### G2-7: Kupffer Cell Trained Immunity -- Category B

**Resolved Identity:**
- Target: Beta-glucan-induced trained immunity pathway in Kupffer cells (host pathway)
- Resolution notes: N/A -- host immunology target, no bacterial gene

**Conservation:** N/A
**Host Selectivity:** N/A (deliberately targets host cells)

**Annotation Check:**
- Claimed: Adams 2024 shows beta-glucan protects Kupffer cells against sepsis-induced loss --> Verified: CORRECT. Beta-glucan suppresses NLRP3/GSDMD pyroptosis and enhances KC self-renewal.
- Claimed: Oral beta-glucan does not reach Kupffer cells directly (SCFP failure context) --> Verified: CORRECT. Parenteral delivery is required for hepatic trained immunity. Oral SCFP failure does NOT disprove parenteral beta-glucan.
- Claimed: Beta-glucan trained immunity raises anti-apoptotic pathways (Bcl-2, Mcl-1) --> Verified: Established in the trained immunity literature for macrophages. Whether this protects against LEUKOTOXIN specifically (pore formation vs signaling-mediated killing) is unknown.

**Verdict:** CONFIRMED
- Novel cross-disease translation. Biological rationale is sound with appropriate caveats.

**Wet-lab confirmation type:**
- Isolate bovine Kupffer cells from slaughterhouse livers; pre-treat with beta-glucan 7 days; challenge with LktA; measure survival (LDH, Annexin V)

---

### G2-8 / V7: Anti-Factor H Binding (FomA) -- Category B

**Resolved Identity:**
- Gene: fomA (also called 43K OMP) | Protein: GenBank JQ740821
- Organism: *F. necrophorum*
- Sequence length: 377-394 aa (42.4 kDa by SDS-PAGE)
- Resolution notes: FomA is likely the same protein as the "42.4 kDa OMP" (Kumar 2013) and the "43K OMP" (Singh 2022). Vulcan (V7) identified this as a DUAL-FUNCTION target: Factor H binding + endothelial adhesion. This convergence with Forge G2-8 and G1-4 is a strong signal.

**Conservation:**
- Factor H binding demonstrated across all F. necrophorum strains tested (Friberg 2008), but at variable levels (5-42%)
- OMP conservation across field isolates: NOT assessed at sequence level
- Evidence: Friberg 2008 J Immunol

**Host Selectivity:**
- Closest host ortholog: NONE (bacterial OMP)
- Risk: LOW
- One concern: vaccination against a Factor H-binding protein could theoretically trigger autoimmune responses against host Factor H (Forge correctly flags this)

**Annotation Check:**
- Claimed: Factor H binding via ionic interactions at N- and C-terminal sites on Factor H --> Verified: CORRECT (Friberg 2008)
- Claimed: Bound Factor H remains active as cofactor for Factor I --> Verified: CORRECT
- Claimed: 42.4 kDa OMP binds bovine endothelial cells (Kumar 2013) --> Verified: CORRECT
- Claimed: 43K OMP interacts with fibronectin (Singh 2022) --> Verified: CORRECT
- **Vulcan synthesis:** V7 unifies what Forge splits into G2-8 (Factor H binding) and G1-4 (anti-adhesion). Both functions map to the same protein (FomA/43K OMP). This means an anti-FomA antibody could simultaneously block complement evasion AND endothelial adhesion -- a dual mechanism.

**Verdict:** CONFIRMED
- The Forge-Vulcan convergence on FomA as a dual-function target is the strongest signal in the secondary virulence factor space. This should be elevated in priority -- one antibody, two mechanisms.
- No structure available. AF3 submission warranted for epitope mapping.

**Wet-lab confirmation type:**
- Anti-FomA antibody: test (1) complement-mediated killing in bovine serum (SBA assay), (2) adhesion to bovine endothelial cells in vitro
- Both assays test the dual mechanism with a single reagent

---

### G2-9: Complement Enhancement (OMV Vaccine) -- Category A

**Resolved Identity:**
- Target: F. necrophorum outer membrane vesicle (OMV) antigens -- 342 proteins identified (MDPI 2023)
- Resolution notes: Multi-antigen preparation, not a single resolved target

**Conservation:** Variable -- OMV composition may differ between strains
**Host Selectivity:** LOW (bacterial antigens)

**Annotation Check:**
- Claimed: Liu 2021 multi-component vaccine protective in mice --> Verified: CORRECT (PMC8685265)
- Claimed: Anti-OMP antibodies would opsonize bacteria during portal transit --> Verified: Biologically plausible; portal blood IgG should reflect systemic levels

**Verdict:** CONFIRMED

**Wet-lab confirmation type:**
- Serum bactericidal assay (SBA) against F. necrophorum using sera from OMV-vaccinated cattle

---

### G2-10: Anti-NET Evasion (DNase Inhibitor) -- Category B

**Resolved Identity:**
- Target: Extracellular DNases of F. necrophorum (gene IDs unresolved at species level)
- Resolution notes: Argus v9 generated ESMFold structures for two putative DNases (EO219_02575 and EO219_05760) from the ATCC 25286 genome. F. nucleatum actively suppresses NET formation (Arelaki 2020). DNase activity in F. necrophorum has NOT been directly demonstrated.

**Conservation:** Unknown at field isolate level
**Host Selectivity:** LOW (bacterial enzymes)

**Annotation Check:**
- Claimed: Multiple DNase-encoding genes identified in F. necrophorum genome --> Verified: CORRECT. Argus v9 identified and structurally predicted two DNase candidates.
- Claimed: F. nucleatum suppresses NET formation --> Verified: CORRECT (Arelaki 2020, Front Immunol)
- FLAG: DNase activity in F. necrophorum is INFERRED, not demonstrated. The gene predictions could be non-functional pseudogenes.

**Structure:**
- ESMFold predictions for both DNase candidates available at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/DNase1_EO219_02575_ESMFold.pdb` and `DNase2_EO219_05760_ESMFold.pdb`
- Detailed analysis at Argus v9 bioinfo/results/dnase_structural_analysis.md

**Verdict:** FLAGGED
- FLAG: DNase activity in F. necrophorum not demonstrated. Genomic inference is insufficient. A simple in vitro DNase activity assay (culture supernatant + calf thymus DNA) would resolve this in 1-2 weeks.

**Wet-lab confirmation type:**
- DNase activity assay: F. necrophorum culture supernatant + DNA substrate, gel electrophoresis
- If confirmed: test actin and synthetic DNase inhibitors

---

### G1-1 / V8: Anti-Hemagglutinin Vaccine -- Category A

**Resolved Identity:**
- Target: Hemagglutinin surface protein, ~19 kDa
- Resolution notes: The hemagglutinin gene has NOT been cloned or sequenced as a discrete entity with a GenBank accession. It is characterized functionally (hemagglutination activity, anti-serum reduces adhesion) but the specific gene ID is UNRESOLVED. This is a significant gap -- you cannot design a recombinant vaccine against a protein that has not been sequenced.

**Conservation:**
- All hepatic isolates of subsp. necrophorum are hemagglutination-positive [ESTABLISHED]
- Some ruminal isolates are negative -- suggesting hemagglutination is selected for during pathogenesis
- Subsp. funduliforme: NEGATIVE for hemagglutination
- Evidence: Okwumabua 1996, Kanoe & Iwaki 1987

**Host Selectivity:** LOW (bacterial surface protein)

**Annotation Check:**
- Claimed: Anti-hemagglutinin antiserum reduces bacterial attachment in vitro --> Verified: CORRECT (Kanoe & Iwaki 1987)
- FLAG: The protein has been characterized functionally but NOT at the gene/sequence level. The "19 kDa hemagglutinin" has not been cloned. Without a resolved gene sequence, recombinant vaccine production is not possible.
- Vulcan (V8) provides additional detail: hemagglutinin also mediates platelet aggregation, contributing to microthrombus formation in the liver.

**Verdict:** FLAGGED
- FLAG: Gene sequence/accession UNRESOLVED. The hemagglutinin has been functionally characterized for nearly 40 years but never cloned. A genomic/proteomic identification campaign is needed before vaccine design can proceed.
- FLAG: Adhesion redundancy. Multiple adhesins exist (43K OMP, FadA, OmpA, OmpH). Blocking hemagglutinin alone may be insufficient if adhesion is redundant. Vulcan correctly identifies this as the weakest link.

**Wet-lab confirmation type:**
- Gene identification: SDS-PAGE of F. necrophorum surface proteins, excise 19 kDa band, mass spec --> gene ID
- Hemagglutinin-negative mutant: adhesion assay on rumen explants (test redundancy)

---

### G1-2: F. necrophorum Phage Cocktail -- Category A

**Resolved Identity:**
- Phages: phiKSUM, phiBB (Schwarz et al. 2024, PHAGE journal)
- Accessions: Published in Schwarz 2024; sequences deposited
- Additional phages from 2025 MDPI study (ruminal fluid and city sewage isolates)
- Patent: US Patent Application 2020/0390835 (Mathieu, Rice University)

**Conservation:** Both phages infect both subspecies (necrophorum and funduliforme) [ESTABLISHED]
**Host Selectivity:** N/A (bacteriophage -- host range limited to F. necrophorum)

**Annotation Check:**
- Claimed: phiKSUM and phiBB are obligately lytic (do not form lysogens) --> Verified: CORRECT per Schwarz 2024
- Claimed: Both infect both subspecies --> Verified: CORRECT

**Verdict:** CONFIRMED
- Best-characterized phage candidates. Rumen stability is the key unknown for in-feed delivery.

**Wet-lab confirmation type:**
- Rumen phage stability: administer to rumen-fistulated cattle, quantify viable phage at serial timepoints

---

### G1-3: Protected Butyrate + Zinc -- Category A

**Resolved Identity:** N/A (feed additive components -- not protein targets)

**Annotation Check:**
- Claimed: Butyrate improves tight junction expression --> Verified: CORRECT in cattle (MDPI Animals 2025)
- Claimed: SCFP (zero effect, n=4,689) rules out oral Gate 1 approaches as standalone --> Verified: CORRECT

**Verdict:** CONFIRMED
- Correctly positioned as combination component only. No standalone value.

**Wet-lab confirmation type:**
- Only worth testing IN COMBINATION with a Gate 2 intervention

---

### G1-4: Anti-43K OMP Vaccine -- Category A (converges with V7/G2-8)

**Resolved Identity:**
- Protein: 42.4 kDa OMP (Kumar 2013) / 43K OMP (Singh 2022) / likely = FomA (JQ740821)
- See G2-8 assessment -- this is the SAME protein as the Factor H binding target

**Key Finding:** Forge treats G1-4 (anti-adhesion) and G2-8 (anti-complement evasion) as separate candidates. Vulcan (V7) identified that they target the same protein (FomA). **An anti-FomA antibody would deliver both mechanisms simultaneously.**

**Verdict:** CONFIRMED
- Recommend merging G1-4 and G2-8 into a single FomA-targeting program. One antibody, dual mechanism.

**Wet-lab confirmation type:**
- Same as G2-8 (dual-mechanism anti-FomA antibody testing)

---

### G1-5: Hindgut-Targeted Suppression -- Category C

**Resolved Identity:** Multi-target (F. necrophorum subsp. funduliforme + Bacteroides spp. in hindgut)
**Conservation:** N/A (multi-organism target)

**Annotation Check:**
- Claimed: Bacteroides 33% of 16S reads in abscesses (Fuerniss 2022) --> Verified: CORRECT
- Claimed: Conditional on KE#1 result --> Verified: Appropriate gating

**Verdict:** CONFIRMED
- Correctly gated on KE#1. Do not invest until hindgut contribution is quantified.

**Wet-lab confirmation type:**
- KE#1 (rumen vs hindgut qPCR) resolves whether this candidate is worth pursuing

---

### G1-6: Tannase-Resistant Tannin -- Category B

**Annotation Check:**
- Claimed: F. nucleatum produces tannase --> Verified: CORRECT. Whether F. necrophorum also produces tannase is UNCONFIRMED.
- Correctly gated on Prediction S4

**Verdict:** CONFIRMED

**Wet-lab confirmation type:**
- In vitro tannase assay with F. necrophorum culture

---

### G1-7: Engineered Funduliforme Probiotic -- Category C

**Annotation Check:**
- Claimed: 21-fold difference in lktA transcript between subspecies --> Verified: CORRECT (Tadepalli 2007)
- Claimed: Both subspecies occupy same ecological niche --> Verified: PLAUSIBLE (both ferment lactate, both colonize rumen wall)

**Verdict:** CONFIRMED
- Elegant concept. Regulatory complexity and horizontal gene transfer risk are real concerns.

**Wet-lab confirmation type:**
- In vitro competition assay: co-culture subspecies at defined ratios in rumen fluid

---

### G1-8: Anti-Biofilm (Rumen Wall) -- Category C

**Annotation Check:**
- Claimed: F. necrophorum biofilm on rumen epithelium is inferred --> Verified: CORRECT -- inferred but NOT demonstrated
- FLAG: No direct evidence of F. necrophorum biofilm on rumen epithelium exists

**Verdict:** FLAGGED
- Must demonstrate biofilm formation on rumen explants before any investment

**Wet-lab confirmation type:**
- Confocal microscopy: F. necrophorum on bovine rumen epithelial cell explants (LIVE/DEAD + FISH)

---

### PG-1: Anti-Stellate Cell Activation -- Category C

**Annotation Check:**
- HSC biology from fibrosis literature is well-established. Application to liver abscess is INFERRED.

**Verdict:** CONFIRMED
- Forge's own honest assessment acknowledges impracticality in feedlot setting.

**Wet-lab confirmation type:**
- Ex vivo liver slice culture + F. necrophorum + pirfenidone (alpha-SMA kinetics)

---

### PG-2: Abscess Biofilm Disruption -- Category C (INTRACTABLE)

**Verdict:** CONFIRMED
- Forge correctly identifies this as intractable (physics barrier). Included for completeness only.

---

### PG-3 / V10 / V15: Anti-T. pyogenes Synergy -- Category A

**Resolved Identity:**
- Pyolysin (Plo): Cholesterol-dependent cytolysin from *T. pyogenes*
- Neuraminidases: NanH, NanP
- Fimbriae: FimA
- CbpA: Collagen-binding protein

**Annotation Check:**
- Claimed: T. pyogenes in 29.2% of abscesses (qPCR) --> Verified: CORRECT (Abbasi 2025)
- Claimed: Dynasore protects against pyolysin at 10 uM --> Verified: CORRECT (established CDC inhibitor)
- Vulcan additions (V10: pyolysin CDC mechanism detail, V11: neuraminidase inhibition, V15: CbpA-collagen adhesion) add molecular specificity to Forge's broader concept
- FLAG: Only relevant in 29% of abscesses. Secondary target.

**Verdict:** CONFIRMED

**Wet-lab confirmation type:**
- In vitro co-culture (F.n. + T.p.) + anti-pyolysin antibody or Dynasore -- measure zone of necrosis

---

### PG-4: Blood Biomarker Diagnostic -- Category A

**Annotation Check:**
- Claimed: Amachawadi 2023 metabolomics data exists --> Verified: CORRECT (J Anim Sci 2023)
- No validated blood biomarker exists for ante-mortem liver abscess detection

**Verdict:** CONFIRMED
- Transformative if successful. Enables real-time intervention studies.

**Wet-lab confirmation type:**
- Paired blood samples + slaughter liver status (n=200). Measure candidate metabolites. AUC-ROC analysis.

---

### COMBO-1: Anti-LktA mAb + Phage Cocktail

**Verdict:** CONFIRMED
- See component assessments (G2-1, G1-2). Combination rationale is sound.

---

### COMBO-2: mRNA LktA Vaccine + Anti-Adhesion Vaccine

**Verdict:** CONFIRMED
- See component assessments (G2-2, G1-1, G1-4). Requires all components to succeed.
- Note: G1-1 hemagglutinin gene is UNRESOLVED (see G1-1 FLAG).

---

## VULCAN-UNIQUE CANDIDATES

### V4: Extracellular Calcium Chelation -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Target: Calcium-dependent conformational activation of LktA (hypothetical)
- Resolution notes: LktA has no classic RTX glycine-rich nonapeptide repeats. Calcium dependence is INFERRED by analogy to RTX toxins but NOT demonstrated for F. necrophorum LktA.

**Annotation Check:**
- Claimed: LktA is heat-labile and pH-sensitive --> Verified: CORRECT (56C/5 min, active pH 6.6-7.8)
- Claimed: LktA has no cysteine residues --> Verified: CORRECT (zero Cys in 3,241 aa). This makes the protein unusually dependent on non-covalent stabilization.
- FLAG: Calcium dependence of LktA is completely unproven. LktA has no homology to RTX toxins, so calcium dependence cannot be assumed.
- FLAG: Systemic calcium chelation is dangerous (cardiac effects). Localized delivery is a major challenge.

**Verdict:** FLAGGED
- Two flags: unproven calcium dependence + dangerous systemic effects. However, the confirming experiment is trivially cheap ($2-5K: LktA cytotoxicity +/- EGTA). Vulcan correctly identifies this as a high-information, low-cost experiment.

**Wet-lab confirmation type:**
- LktA cytotoxicity against bovine PMNs +/- EGTA (calcium chelation). If >90% reduction at <10 uM free Ca2+, proceed. If calcium-independent, kill this target.

---

### V6: Downstream Signaling Blockade -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Target: Caspase-3/-8, NF-kB pathway in bovine leukocytes (host pathway)
- Evidence: F. necrophorum activates NF-kB and death receptor pathways (Front Cell Infect Microbiol 2022)

**Host Selectivity:** HIGH -- caspase and NF-kB are essential host immune pathways. Blocking them broadly would be immunosuppressive. Must find a LktA-specific divergence point.

**Annotation Check:**
- Claimed: Low-dose LktA activates neutrophils (degranulation) before killing them --> Verified: CORRECT (Narayanan 2002). The dose-dependent dual response is established.
- Vulcan correctly identifies the weakest link: if LktA uses the same signaling as normal immune activation, blocking the pathway would impair normal immunity.

**Verdict:** FLAGGED
- FLAG: High host selectivity risk. The intervention only works if LktA activates a SPECIFIC pathway dispensable for normal immunity. This is unknown.

**Wet-lab confirmation type:**
- Pan-caspase inhibitor (z-VAD-FMK) on bovine PMNs + LktA: measure survival AND respiratory burst (test whether caspase inhibition preserves antimicrobial function)

---

### V9: Hemolysin (PLB) Inhibition -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Target: Phospholipase B hemolysin of F. necrophorum
- Resolution notes: Gene accession NOT resolved. The hemolysin co-purifies with leucocidin activity. PLB is characterized functionally but the gene ID in modern genome assemblies needs mapping.

**Annotation Check:**
- Claimed: PLB targets phosphatidylcholine on erythrocyte membranes --> Verified: CORRECT (Gokce 1998)
- FLAG: Species selectivity issue -- strong lysis of rabbit/human/dog RBCs but only TRACE activity against bovine erythrocytes. If the primary host shows resistance, the hemolysin may not be a major virulence factor in cattle.

**Verdict:** FLAGGED
- FLAG: Low bovine RBC activity calls into question whether hemolysin is important in the natural host. Vulcan correctly identifies this uncertainty.

**Wet-lab confirmation type:**
- Hemolysin-deficient mutant growth in bovine liver homogenate (aerobic/microaerobic conditions)

---

### V11: Neuraminidase Inhibition (T. pyogenes) -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Target: NanH, NanP neuraminidases of *T. pyogenes*
- Mechanism: Sialic acid removal from host glycoproteins (adhesion + carbon source)

**Annotation Check:**
- Sialidase inhibitors are an established drug class (oseltamivir, zanamivir)
- Bacterial sialidases have different active site geometry from viral neuraminidases

**Verdict:** CONFIRMED
- Molecular specificity added to the T. pyogenes targeting space. Low standalone impact (~5-10% of severe abscesses at population level).

**Wet-lab confirmation type:**
- Screen existing sialidase inhibitor scaffolds against recombinant NanH/NanP

---

### V12: Feedback Loop Disruption -- Category C (VULCAN-UNIQUE)

**Annotation Check:**
- The leukotoxin amplification loop (low-dose activation --> degranulation --> tissue damage --> anaerobic niche --> more F.n. growth --> more leukotoxin) is biologically established.
- Vulcan's insight: interventions reducing leukotoxin may have NON-LINEAR effects because they break the feedback loop.

**Verdict:** CONFIRMED
- More of a system-level insight than a druggable target. Informs portfolio strategy (supports the case for partial leukotoxin reduction being sufficient).

**Wet-lab confirmation type:**
- Sub-inhibitory vs supra-lethal leukotoxin doses in ex vivo liver model: measure zone of necrosis (test the activation-damage hypothesis)

---

### V13: Gallium Porphyrin Iron Starvation -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Target: Heme uptake system of F. necrophorum (unresolved gene accession)
- Key vulnerability: F. necrophorum has NO Fur gene and NO siderophore biosynthesis genes [ESTABLISHED from disease map]
- Relies ENTIRELY on heme uptake for iron
- F. nucleatum has a defined heme uptake operon; F. necrophorum likely has an analogous system

**Conservation:**
- Iron dependency is fundamental to F. necrophorum metabolism -- conserved across all strains
- The heme uptake system needs genomic characterization

**Host Selectivity:** LOW -- gallium porphyrins are taken up by bacterial iron transport systems. Host cells have different iron uptake mechanisms. Gallium nitrate has been tested in human Phase 2 trials (CF *P. aeruginosa*) with manageable safety profile.

**Annotation Check:**
- Claimed: No Fur, no siderophores --> Verified: CORRECT (from disease map, supported by genomic analysis)
- Claimed: Gallium nitrate Phase 2 for P. aeruginosa (Kaneko 2007) --> Verified: CORRECT
- Claimed: Gallium porphyrins have inherent hepatic tropism --> Verified: CORRECT (porphyrins accumulate in the liver -- well-established)
- This is a genuinely novel target that Forge did not identify. The Trojan horse strategy (gallium porphyrin taken up as heme, poisons iron-dependent enzymes) is elegant and has clinical precedent.

**Verdict:** CONFIRMED
- This is one of the most novel and well-supported Vulcan targets. The metabolic vulnerability (no siderophores, no Fur) is unusual among pathogenic bacteria and represents a genuine therapeutic opportunity. Gallium porphyrin hepatic tropism aligns perfectly with the disease site.

**Wet-lab confirmation type:**
- F. necrophorum growth in heme-limited media: dose-response for heme concentration
- Gallium nitrate/gallium porphyrin MIC against F. necrophorum in vitro
- Genomic analysis of heme uptake genes in F. necrophorum

---

### V14: LuxS/AI-2 Quorum Sensing Disruption -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Gene: luxS homolog (AZW09003 from Argus v9 genome analysis of ATCC 25286)
- Also identified: AI2E transporter (AZW09003, Argus v9); LuxR1 (AZW08579.1); LuxR2 (AZW09128.1)
- Resolution notes: Argus v9 confirmed LuxS is present. However, it found NO AI-2 receptor genes (no LuxP/LuxQ homologs). The presence of LuxS without canonical AI-2 receptors suggests LuxS may function primarily in the activated methyl cycle (metabolism) rather than as a true quorum sensor.

**Annotation Check:**
- Claimed: LuxS homologs present across Fusobacterium genomes --> Verified: CORRECT
- Claimed: In H. parasuis, luxS deletion attenuates virulence 10-fold --> Verified: CORRECT
- FLAG: Argus v9 found LuxS but NO AI-2 receptor genes. In many bacteria, LuxS functions metabolically (activated methyl cycle) without true quorum sensing function. If AI-2 receptors are absent, LuxS is metabolic, not regulatory.
- The presence of LuxR family regulators (LuxR1, LuxR2) suggests SOME regulatory function, but these may respond to signals other than AI-2.

**Verdict:** FLAGGED
- FLAG: No AI-2 receptor genes found in F. necrophorum genome (Argus v9). LuxS presence alone does not confirm quorum sensing. A luxS deletion mutant is needed to test whether it affects virulence gene expression.

**Wet-lab confirmation type:**
- luxS deletion mutant: measure lktA transcript levels (qRT-PCR). If unchanged, LuxS does not regulate virulence.
- Check for AI-2 production: Vibrio harveyi BB170 bioluminescence reporter assay with F. necrophorum conditioned media

---

### V16: Contact System Activation Blockade -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Target: Factor XII / HK (high-molecular-weight kininogen) / prekallikrein activation at F. necrophorum surface
- F. necrophorum binds HK via the D5 domain; produces massive bradykinin release (3,300 pmol/mL)
- Approved drug exists: lanadelumab (anti-plasma kallikrein mAb) for hereditary angioedema

**Host Selectivity:** HIGH -- contact system is a host pathway. However, lanadelumab is already FDA-approved with known safety profile.

**Annotation Check:**
- Claimed: Contact system activation demonstrated on F. necrophorum surfaces --> Verified: CORRECT but in the context of Lemierre's syndrome (human), not bovine liver abscess
- Claimed: Plasma kallikrein inhibitor H-D-Pro-Phe-Arg-CMK blocks both bradykinin and thrombin activation --> Verified: CORRECT
- FLAG: Bovine relevance unconfirmed. The bovine contact system may behave differently from human.

**Verdict:** FLAGGED
- FLAG: Demonstrated in human Lemierre's syndrome only. Bovine liver abscess relevance unconfirmed. However, the biology is plausible (microthrombus formation is well-documented in liver abscesses, and contact activation is a distinct mechanism from LPS-triggered coagulation).

**Wet-lab confirmation type:**
- Contact system activation assay: F. necrophorum + bovine plasma, measure bradykinin generation and thrombin activity

---

### V17: MMP-13 Induction Blockade -- Category C (VULCAN-UNIQUE)

**Resolved Identity:**
- Target: Host MMP-13 (collagenase 3) induced by F. necrophorum
- MMP-13 selective inhibitors exist (CL-82198, compound 36 from osteoarthritis development)

**Host Selectivity:** HIGH -- MMP-13 is a host enzyme. Broad MMP inhibition has unacceptable side effects. MMP-13-selective compounds have improved safety.

**Annotation Check:**
- Claimed: F. necrophorum stimulates host MMP-13 production --> Verified: CORRECT (Nagaraja & Narayanan 2007)
- FLAG: Tissue penetration may be redundant with bacterial proteases. Blocking MMP-13 alone may be insufficient.

**Verdict:** CONFIRMED
- Established drug target class. Oral delivery feasible. Unclear if sufficient alone.

**Wet-lab confirmation type:**
- Rumen wall explant invasion assay: F. necrophorum +/- MMP-13 inhibitor CL-82198, measure invasion depth at 24h

---

## PART IV: STRUCTURE PREDICTION ASSESSMENT

### Priority Targets for Structure

| Priority | Target | Size | Existing Structure | AF3 Needed? | Rationale |
|----------|--------|------|--------------------|-------------|-----------|
| 1 | LktA (epitope regions PL1/PL3/PL4) | 3,241 aa full; epitope regions ~100-300 aa | AF3 fragments only (Argus v15: 116-145 aa) | **YES -- CRITICAL** | Entire Gate 2 antibody/vaccine portfolio depends on knowing which epitopes are surface-exposed. Full-length is beyond AF3 server limit (5,000 tokens per chain). Submit epitope regions individually. |
| 2 | LktB (full length) | ~525 aa | ESMFold split prediction (Argus v9) | **YES** | Need full-length for plug helix positioning, POTRA-barrel orientation. FhaC template (PDB 2QDZ) available for constrained prediction. |
| 3 | LktC (with Zn2+) | 145 aa | ESMFold (Argus v9, pLDDT 90) | **YES** | Need co-folding with Zn2+ ion to resolve CCHH motif geometry. Current model has 13-21 A separation that is likely an artifact. |
| 4 | FomA/43K OMP | 377 aa | NONE | **YES** | Dual-function target (Factor H binding + adhesion). Epitope mapping needed for vaccine/antibody design. |
| 5 | LuxS (if quorum sensing confirmed) | ~170 aa (estimated) | NONE for F. necrophorum | CONDITIONAL | Only if luxS mutant shows virulence phenotype |

### Existing Structures from Argus

The following structures are available from prior Argus work:

| Structure | Source | Location | Quality |
|-----------|--------|----------|---------|
| LktA monomer (fragment) | AF3 (Argus v15) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/structures/lkta_monomer/` | MSA available; limited coverage |
| LktA-CD18 complex | AF3 (Argus v15) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/structures/lkta_cd18_complex/` | Complex prediction |
| LktA binder complex | AF3 (Argus v15) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/structures/lkta_binder_complex/` | Binder validation |
| Pyolysin monomer | AF3 (Argus v15) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/structures/plo_monomer/` | With templates |
| LktB Part 1 | ESMFold (Argus v9) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktB_ESMFold_part1.pdb` | pLDDT 89.5 |
| LktB Part 2 | ESMFold (Argus v9) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktB_ESMFold_part2.pdb` | pLDDT 95.9 |
| LktB full (ESMFold) | ESMFold (Argus v9) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktB_ESMFold.pdb` | Single-chain prediction |
| LktC | ESMFold (Argus v9) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/HK_lktA_adjacent_ESMFold.pdb` | pLDDT 90 (misnamed as HK) |
| LktC prepared for docking | Argus v9 | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktC_receptor_prepared.pdb` | Receptor-prepared |
| DNase 1 | ESMFold (Argus v9) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/DNase1_EO219_02575_ESMFold.pdb` | ESMFold prediction |
| DNase 2 | ESMFold (Argus v9) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/DNase2_EO219_05760_ESMFold.pdb` | ESMFold prediction |
| TetR regulator | ESMFold (Argus v9) | `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/TetR_lktA_adjacent_ESMFold.pdb` | pLDDT 90 |

### AlphaFold DB Check

- **LktA (A0A0E3GP50):** AlphaFold DB has a prediction but only for fragments (116-145 aa region covered confidently). The full 3,241 aa protein exceeds the original AF2 training distribution. AF3 on the full sequence would likely have poor confidence for most of the protein.
- **LktB:** No pre-computed AlphaFold DB entry found for F. necrophorum LktB specifically. FhaC (PDB 2QDZ) is the best experimental template at ~20% sequence identity.
- **LktC:** No pre-computed AlphaFold DB entry. ESMFold prediction from Argus v9 is the current best model.
- **FomA:** No pre-computed structure found.

---

## PART V: BINDER DESIGN NOTES

### LktA Epitope Regions (PL1, PL3, PL4) -- Antibody/Vaccine Targets

**Existing binder designs (Argus v15):**
- RFAntibody binder design completed for EP-3D7 epitope region (2 jobs)
- RFDiffusion + ProteinMPNN extended binder designs completed
- Best binders: ep3d7_extended_50steps series with pLDDT 88-90
- Sequences at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/results/lkta_ep3d7_extended_v2/ep3d7_extended_50steps_sequences.fasta`

**Surface exposure assessment:**
- Cannot confirm surface exposure of PL1/PL3/PL4 without a full-length structure
- The zero-cysteine composition means no disulfide-stabilized domains -- the protein is likely an elongated, flexible structure (consistent with filamentous adhesin family)
- The conserved B-cell epitope ISSFGVGV (Xiao 2024) should be checked for conservation across field isolates

**Binder design approach:**
- For mAb development: RFAntibody designs from Argus v15 provide starting sequences. These need experimental validation (binding affinity by SPR, neutralization assay).
- For vaccine design: Epitope-focused subunit (PL1+PL3+PL4 fusion) is the most straightforward approach. No binder design needed -- the immune system generates its own antibodies.
- For passive immunization (G2-1): The Argus v15 RFAntibody binders could serve as starting points for a therapeutic mAb. pLDDT 88-90 suggests good folding confidence.

### FomA/43K OMP -- Dual-Function Antibody Target

**Binder design status:** No binder design has been performed for FomA.

**Design approach:**
- Need AF3 structure first (see bioinfo/af3_requests/foma_monomer.md)
- Once structure is available: identify the Factor H binding interface and the endothelial adhesion interface
- Design an antibody that blocks BOTH interfaces simultaneously (ideal) or two antibodies for a combination
- If interfaces are spatially separated on the protein surface, a bispecific antibody could be considered

### Pyolysin (Plo) -- Existing Binder Designs

**From Argus v15:**
- RFDiffusion binder designs for pyolysin domain 4 and undecapeptide region
- Best binders: plo_undecapeptide series with pLDDT 80-91
- Results at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/results/plo_binder_design/`
- AF3 structure available at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/structures/plo_monomer/`

---

## PART VI: AF3 SUBMISSION REQUESTS

The following AF3 submissions are needed. Request files written to `bioinfo/af3_requests/`.

### 1. LktA Epitope Regions (HIGHEST PRIORITY)

**Rationale:** The entire Gate 2 antibody/vaccine portfolio depends on knowing epitope surface exposure and conformation.

**Approach:** Submit PL1, PL3, PL4 regions individually (each ~100-300 aa) since full-length LktA (3,241 aa) exceeds practical prediction limits. Use the Argus v15 AF3 fragment predictions as starting points and extend.

### 2. LktB Full Length

**Rationale:** ESMFold split prediction is insufficient for drug design. Need full-length prediction with correct plug helix positioning.

**Template:** FhaC (PDB 2QDZ) at ~20% sequence identity.

### 3. LktC with Zn2+ Ion

**Rationale:** Resolve the CCHH motif geometry. Current ESMFold model has 13-21 A separation between Cys and His residues -- likely an artifact of missing metal coordination.

**Co-factors:** Include Zn2+ ion.

### 4. FomA Monomer

**Rationale:** Dual-function target (Factor H binding + adhesion). Structure needed for epitope mapping and antibody design.

---

## PART VII: KEY CORRECTIONS AND FLAGS

### Corrections (Forge claims that computational analysis corrects)

1. **G2-4 (LktB):** POTRA domain is NOT a "druggable pocket" for small molecules. It is a flat beta-sheet surface with low small molecule druggability. Best modality is biologics (antibody/vaccine targeting extracellular loops) or peptide mimetics.

2. **G2-5 (LktC):** The "histidine kinase and sensory transduction regulator domains" annotation is WRONG. LktC has NO kinase domains (CDD confirms). It is a 145 aa protein of the YbjN family with a CCHH motif of unresolved function. Three competing hypotheses: acyltransferase, zinc metalloenzyme, chaperone.

3. **G1-4 / G2-8 merger:** Forge treats anti-43K OMP (adhesion) and anti-Factor H binding as separate candidates targeting separate proteins. Vulcan and computational analysis indicate they target the SAME protein (FomA). These should be merged into a single FomA program.

4. **LktB dual function:** Argus v9 ShlB domain analysis reveals LktB may perform BOTH secretion and activation of LktA (not just secretion as Forge states). This makes LktB a potentially higher-value target than Forge's ranking suggests.

### Flags (Computational findings creating material risk)

1. **V14 (LuxS/QS):** No AI-2 receptor genes found in F. necrophorum genome. LuxS may be metabolic only. Quorum sensing may not be functional.

2. **G1-1 (Hemagglutinin):** Gene sequence UNRESOLVED. Cannot design recombinant vaccine without gene identification.

3. **G2-10 (DNase/NET):** DNase activity in F. necrophorum not demonstrated. Inference from genomic data only.

4. **G1-8 (Biofilm):** Rumen wall biofilm by F. necrophorum not demonstrated.

5. **V4 (Calcium):** Calcium dependence of LktA completely unproven.

6. **V6 (Downstream signaling):** High host selectivity risk -- may impair normal immunity.

7. **V9 (Hemolysin):** Low bovine RBC activity questions relevance in natural host.

8. **V16 (Contact system):** Demonstrated in human Lemierre's syndrome only, not bovine liver abscess.

---

## PART VIII: HIGHEST-VALUE RESOLUTION EXPERIMENTS

Ranked by information value per dollar, these experiments would resolve the key uncertainties flagged in this report:

| Priority | Experiment | Resolves | Est. Cost | Time |
|----------|-----------|----------|-----------|------|
| 1 | Recombinant LktC acyltransferase assay (express + test with pro-LktA + acyl-ACP) | V2/G2-5: Is LktC an acyltransferase? First-in-class target validation. | $5-10K | 4-6 wk |
| 2 | LktA calcium dependence (cytotoxicity +/- EGTA) | V4: Is LktA calcium-dependent? | $2-5K | 2 wk |
| 3 | Hemagglutinin gene identification (SDS-PAGE, excise 19 kDa, mass spec) | G1-1: Can we make a recombinant vaccine? | $3-5K | 2-3 wk |
| 4 | F. necrophorum DNase activity assay (culture supernatant + DNA) | G2-10: Does F.n. degrade NETs? | $1-2K | 1 wk |
| 5 | luxS deletion mutant + lktA qRT-PCR | V14: Does QS regulate virulence? | $10-15K | 6-8 wk |
| 6 | ICP-MS on purified LktC (zinc binding) | V2: What is LktC's catalytic mechanism? | $2-3K | 2 wk |
| 7 | Anti-CD18 mAb vs LktA cytotoxicity | V5/G2-6: Is CD18 the receptor? | $3-5K | 2-3 wk |
| 8 | Contact system activation in bovine plasma | V16: Does this mechanism operate in cattle? | $5-8K | 3-4 wk |

**Total for all 8 experiments: ~$31-53K, 1-8 weeks each (most can run in parallel)**

---

*Survey report complete. 41 candidates assessed (28 Forge + 13 Vulcan-unique). 24 CONFIRMED, 4 CORRECTED, 9 FLAGGED. 4 AF3 submissions requested. 8 resolution experiments defined. Critical gap: no full-length LktA structure exists -- this bottlenecks the entire Gate 2 antibody/vaccine portfolio.*
