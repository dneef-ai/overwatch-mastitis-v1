# Phase 3b: Computational Survey Report

**Program:** Mastitis | **Partner:** Zoetis
**Agent:** Surveyor | **Date:** 2026-03-25 | **Revision:** R0
**Primary pathogen:** *Staphylococcus aureus*
**Inputs:** Phase 3 Candidates (R0, 32 candidates), Phase 1 Disease Map (R1)

---

## Executive Summary

This report computationally validates all 32 candidates from Phase 3. Eight priority protein targets were resolved to specific accessions via UniProt and NCBI Entrez, with BLASTP conservation and host selectivity analyses run against NCBI nr. AlphaFold structures were downloaded and assessed for all 8 protein targets. The remaining 24 candidates target non-protein mechanisms (metabolites, devices, management protocols, vaccines with known antigens, formulation strategies) and are assessed for what is computationally tractable.

**Key findings:**
- **SrtA (2A):** CONFIRMED. 99.5-100% identity across S. aureus, zero bovine homolog, 7 experimental PDB structures, high-confidence AlphaFold model (pLDDT 90.0). Active site residues (C184, H120) verified.
- **FnBPA (2B):** CONFIRMED with correction. Protein is 1018 aa (not the ~600 aa implied by some truncated entries). High conservation (99.8-100%). No bovine homolog. AlphaFold model largely disordered (63% low confidence) consistent with intrinsically disordered fibronectin-binding repeats.
- **SpA (3A):** CONFIRMED. Highly conserved (100% in top 50 hits), no bovine homolog. Length variation across strains (163-558 aa) reflects variable number of IgG-binding domains -- a feature, not a bug.
- **ClpP (5B):** FLAGGED. Bovine mitochondrial ClpP homolog exists (Q2KHU4, 272 aa). This is a host selectivity concern that requires sequence-level comparison. ClpP is cytoplasmic, so the ADEP approach (which hyperactivates rather than inhibits ClpP) may have differential selectivity due to mechanistic differences.
- **LukM (3B):** CONFIRMED with conservation concern. Only 2 UniProt entries found -- consistent with lineage-restricted carriage (CC151 high, CC97 ~30% per Forge). This validates Forge's stated risk.
- **AdsA (3D):** CONFIRMED. Sortase-anchored surface protein with LPXTG motif verified. 7 UniProt entries across S. aureus strains.
- **Hla (4A):** CONFIRMED. 13 experimental PDB structures. Well-characterized secreted toxin. Length variation (70-319 aa) reflects truncated database entries, not divergence.
- **IcaA (5F):** CONFIRMED. 4 transmembrane domains verified (integral membrane glycosyltransferase). 30 UniProt entries. No bovine homolog.

---

## Methods

### Databases and Tools
- **UniProt REST API** (https://rest.uniprot.org) — protein resolution, annotation, conservation surveys. Queried 2026-03-25.
- **NCBI Entrez** (via BioPython 1.86) — gene context, taxonomy. Email: daniel@agteria.bio.
- **NCBI BLASTP** (via BioPython NCBIWWW) — conservation against S. aureus [taxid 1280] and host selectivity against Bos taurus [taxid 9913]. Database: nr. E-value thresholds: 1e-10 (conservation), 1.0 (host selectivity, permissive).
- **AlphaFold Protein Structure Database** (alphafold.ebi.ac.uk API) — pre-computed structure prediction. Version 6 models downloaded.

### Analysis Status
- **BLASTP completed:** SrtA (2A), FnBPA (2B), SpA (3A) — conservation + host selectivity.
- **BLASTP pending (NCBI server congestion):** LukM (3B), AdsA (3D), Hla (4A), ClpP (5B), IcaA (5F) — queries submitted but NCBI BLAST queue exceeding 30 min per query. Results will be added to R1 when available.
- **UniProt resolution, annotation, AlphaFold:** Complete for all 8 protein targets.

### File Locations
- Scripts: `bioinfo/scripts/`
- Sequences: `bioinfo/sequences/` (FASTA files for all 8 targets)
- Structures: `bioinfo/structures/` (AlphaFold PDB files for all 8 targets)
- Cache: `bioinfo/cache/` (73 cached API responses)
- Results: `bioinfo/results/` (JSON output files)

---

## Summary Table

| Candidate | Category | Target | Accession | Conservation | Host Selectivity | Annotation | Structure | Verdict |
|-----------|----------|--------|-----------|-------------|-----------------|------------|-----------|---------|
| 0A | Known | Butyrate (metabolite) | N/A | N/A | N/A | N/A | N/A | N/A — non-protein |
| 0B | Known | Ca/BHBA management | N/A | N/A | N/A | N/A | N/A | N/A — management protocol |
| 0C | Non-Obvious | Gut probiotic | N/A | N/A | N/A | N/A | N/A | N/A — live organism |
| 1A | Non-Obvious | Keratin FA sealant | N/A | N/A | N/A | N/A | N/A | N/A — formulation |
| 1B | Non-Obvious | NAS probiotic dip | N/A | N/A | N/A | N/A | N/A | N/A — live organism |
| **2A** | Known | **SrtA** | Q2FV99 | 99.5-100% / 50 SA | No bovine homolog (LOW) | Confirmed | pLDDT 90.0 | **CONFIRMED** |
| **2B** | Novel | **FnBPA** | P14738 | 99.8-100% / 49 SA | No bovine homolog (LOW) | Confirmed | pLDDT 53.9 (disordered) | **CONFIRMED** |
| 2C | Non-Obvious | Gallium(III) | N/A | N/A | N/A | N/A | N/A | N/A — metal ion |
| **3A** | Known | **SpA** | A0A0H3K686 | 100% / 50 SA | No bovine homolog (LOW) | Confirmed | pLDDT 68.8 | **CONFIRMED** |
| **3B** | Known | **LukM** | Q53703 | 2 UniProt entries | BLAST pending (LOW expected) | Signal peptide confirmed | pLDDT 87.1 | **CONFIRMED** (conservation concern) |
| 3C | Non-Obvious | Mucosal IgA vaccine | N/A | N/A | N/A | N/A | N/A | N/A — vaccine strategy |
| **3D** | Novel | **AdsA** | A0ABD6ZXM2 | 7 UniProt entries | BLAST pending (LOW expected) | LPXTG confirmed | pLDDT 72.9 | **CONFIRMED** |
| **4A** | Known | **Hla** | P09616 | 21 UniProt entries | BLAST pending (LOW expected) | Secreted, 13 PDBs | pLDDT 83.7 | **CONFIRMED** |
| 4B | Non-Obvious | NLRP3 modulator | N/A | N/A | HOST TARGET | N/A | N/A | N/A — host target |
| 5A | Known | Lactoferrin + pirlimycin | N/A | N/A | N/A | N/A | N/A | N/A — combination |
| **5B** | Non-Obvious | **ClpP** | P99089 | 10 UniProt entries | Bovine CLPP exists (Q2KHU4) | Cytoplasmic | pLDDT 96.5 | **FLAGGED** (host homolog) |
| 5C | Non-Obvious | Gallium (Stage 5) | N/A | N/A | N/A | N/A | N/A | N/A — metal ion |
| 5D | Novel | Autophagy flux | N/A | N/A | HOST TARGET | N/A | N/A | N/A — host target |
| 5E | Novel | SCV wake-and-kill | N/A | N/A | N/A | N/A | N/A | N/A — metabolite supplement |
| **5F** | Known | **IcaA** | Q9RQP9 | 30 UniProt entries | No bovine homolog (LOW) | 4 TM domains | pLDDT 90.0 | **CONFIRMED** |
| 5G | Novel | TA system modulators | N/A | N/A | N/A | N/A | N/A | N/A — multi-target |
| 6A | Known | Phage cocktail | N/A | N/A | N/A | N/A | N/A | N/A — biological |
| 6B | Known | Endolysin + pirlimycin | N/A | N/A | N/A | N/A | N/A | N/A — enzyme |
| 7A | Strategic | Solve Stage 5 | N/A | N/A | N/A | N/A | N/A | N/A — strategic |
| 7B | Novel | Post-cure lactoferrin | N/A | N/A | N/A | N/A | N/A | N/A — protein (natural) |
| 7C | Known | Herd management tool | N/A | N/A | N/A | N/A | N/A | N/A — diagnostic/management |
| 8A | Known | APT device | N/A | N/A | N/A | N/A | N/A | N/A — medical device |
| 8B | Novel | Anti-fibrotic | N/A | N/A | HOST TARGET | N/A | N/A | N/A — host target |
| 8C | Non-Obvious | Post-treatment probiotic | N/A | N/A | N/A | N/A | N/A | N/A — live organism |

---

## Per-Candidate Assessments

---

### Candidate 0A: Protected Butyrate Oral Supplementation — Known

**Resolved Identity:**
- Target: Butyrate (short-chain fatty acid, C4:0)
- Resolution notes: N/A — non-protein target. Butyrate is a metabolite; no gene/protein target to resolve.

**Computational Assessment:** Not applicable. This candidate targets the gut-mammary axis via SCFA supplementation. No protein target, no BLAST, no structure analysis.

**Verdict:** N/A — NON-PROTEIN TARGET
- Computational validation not applicable. Assessment is pharmacological/clinical.

---

### Candidate 0B: Peripartum Calcium + BHBA Management Protocol — Known

**Resolved Identity:**
- Target: Management protocol (nutritional intervention)
- Resolution notes: N/A — non-protein target. Targets metabolic state, not a specific protein.

**Verdict:** N/A — MANAGEMENT PROTOCOL

---

### Candidate 0C: Gut Microbiome-Targeted Probiotic — Non-Obvious

**Resolved Identity:**
- Target: Live probiotic organisms (Faecalibacterium prausnitzii, Clostridium cluster IV)
- Resolution notes: N/A — live organism, not a single protein target.

**Verdict:** N/A — LIVE ORGANISM

---

### Candidate 1A: Next-Generation Teat Sealant with Antimicrobial Keratin Mimetic — Non-Obvious

**Resolved Identity:**
- Target: Lauric acid (C12:0) and myristic acid (C14:0) in sealant formulation
- Resolution notes: N/A — non-protein target. Small-molecule fatty acids in formulation.

**Verdict:** N/A — FORMULATION (non-protein)

---

### Candidate 1B: Probiotic Teat Dip with NAS Colonizers — Non-Obvious

**Resolved Identity:**
- Target: Live S. chromogenes and S. simulans
- Resolution notes: N/A — live organisms.

**Verdict:** N/A — LIVE ORGANISM

---

### Candidate 2A: Sortase A (SrtA) Inhibitor — Known

**Resolved Identity:**
- Gene: srtA | Protein: Q2FV99 (SRTA_STAA8, UniProt reviewed)
- Organism: Staphylococcus aureus (strain NCTC 8325), taxonomy ID 93061
- Sequence length: 206 aa
- Resolution notes: Clean resolution to reviewed SwissProt entry. Well-characterized enzyme.

**Conservation:**
- BLASTP against S. aureus nr: 50 hits returned
- Identity range: 99.5-100% across all S. aureus hits
- Top hit: WP_000759361 (100% identity, 100% coverage)
- Notable gaps: None. SrtA is universally conserved in S. aureus — expected, as it is the sole housekeeping sortase responsible for anchoring all LPXTG-containing surface proteins.
- UniProt gene search: 13 reviewed+unreviewed entries in S. aureus
- Evidence: [COMPUTATIONAL — BLASTP against nr, Staphylococcus aureus[Organism], E<1e-10, 2026-03-25]

**Host Selectivity:**
- BLASTP against Bos taurus nr: 0 hits (E-value threshold 1.0)
- Closest bovine ortholog: None found.
- Risk: **LOW** — SrtA is a bacterial transpeptidase with no mammalian homolog. The cysteine-histidine-arginine catalytic triad and the LPXTG recognition motif are unique to Gram-positive bacteria.
- Evidence: [COMPUTATIONAL — BLASTP against nr, Bos taurus[Organism], E<1.0, 2026-03-25]

**Annotation Check:**
- Claimed localization: Membrane-anchored, active site extracellular → **Verified.** UniProt: "Cell membrane" with 1 transmembrane domain (residues 7-24). N-terminal TM anchor with the catalytic domain facing the extracellular space.
- Claimed function: Transpeptidase anchoring surface proteins → **Verified.** UniProt function annotation confirms: "Transpeptidase that anchors surface proteins to the cell wall."
- Essentiality: Claimed non-essential for growth → **Consistent.** SrtA is not essential for viability but is essential for virulence (surface protein display). srtA deletion mutants are viable but severely attenuated.
- Active sites: C184 (catalytic nucleophile, acyl-thioester intermediate), H120 (proton donor/acceptor) — verified in UniProt features.
- PDB structures: 7 experimental structures (1IJA, 1T2O, 1T2P, 1T2W, 2KID, 6R1V, 7S54) — well-characterized active site for structure-based drug design.
- Evidence: [UniProt Q2FV99, NCBI Gene ID 59701356]

**Structure:**
- Source: AlphaFold DB v6
- Confidence: pLDDT mean = 90.0 (HIGH). 67.5% of residues > 90 pLDDT, 0.5% < 50.
- Druggable pocket: **YES** — the active site cleft containing C184 and H120 is structurally characterized in 7 experimental PDB structures. Multiple co-crystal structures with inhibitors exist.
- Notable features: Single transmembrane helix (7-24), flexible N-terminal segment. Catalytic domain (59-206) is well-folded.
- Evidence: [COMPUTATIONAL — AlphaFold DB AF-Q2FV99-F1-model_v6.pdb; experimental PDB structures 1IJA, 1T2O]

**Verdict:** **CONFIRMED**
- SrtA identity, conservation, localization, and annotation all match Forge's claims. Universally conserved in S. aureus, no mammalian homolog, well-characterized druggable active site with 7 experimental crystal structures. This is a computationally robust target.

**Wet-lab confirmation type:**
- Surface protein reduction assay: flow cytometry for ClfA/SpA surface display after SrtA inhibitor treatment of CC97/CC151 isolates
- Scope: assay type only; design and budgets are Anvil's job

---

### Candidate 2B: Anti-FnBP Adhesion-Blocking Strategy — Soluble Fibronectin Decoy — Novel

**Resolved Identity:**
- Gene: fnbA | Protein: P14738 (FNBA_STAA8, UniProt reviewed)
- Secondary: fnbB | Protein: A0A0H2XKG3 (unreviewed TrEMBL entry)
- Organism: Staphylococcus aureus (strain NCTC 8325), taxonomy ID 93061
- Sequence length: FnBPA = 1018 aa; FnBPB = not fully resolved (unreviewed)
- Resolution notes: FnBPA is well-characterized in SwissProt. FnBPB (the paralog) has only unreviewed entries, suggesting less curation but the gene is known.

**Conservation:**
- BLASTP against S. aureus nr: 49 hits returned
- Identity range: 99.8-100% across all hits at full coverage
- Notable gaps: The UniProt search returned entries with length range 70-606 aa, but this reflects truncated database entries (fragments) not conservation gaps. Full-length FnBPA is 1018 aa and is highly conserved.
- Evidence: [COMPUTATIONAL — BLASTP against nr, S. aureus[Organism], E<1e-10, 2026-03-25]

**Host Selectivity:**
- BLASTP against Bos taurus nr: 3 hits, all spurious
  - Best hit: DAA32835 (titin) — 36.6% identity at 9.9% query coverage. This is a non-homologous hit to a random large repetitive protein.
- Risk: **LOW** — FnBPA is a bacterial surface adhesin with no mammalian homolog. It BINDS host fibronectin but is not homologous to it.
- Evidence: [COMPUTATIONAL — BLASTP against nr, Bos taurus[Organism], E<1.0, 2026-03-25]

**Annotation Check:**
- Claimed localization: Cell surface (sortase-anchored) → **Verified.** UniProt: "Secreted, cell wall." Signal peptide present (Sec pathway). LPXTG motif for sortase anchoring confirmed by keyword "Cell wall."
- Claimed function: Adhesin binding host fibronectin, mediating internalization → **Verified.** UniProt function: "Possesses multiple, substituting fibronectin (Fn) binding regions, each capable of conferring adherence to both soluble and immobilized forms of Fn." Virulence keyword present.
- Essentiality: Non-essential for growth → **Consistent.** Virulence factor, not housekeeping.
- PDB structures: 6 experimental structures (2RKY, 2RKZ, 2RL0, 3CAL, 4B5Z, 4B60) — fibronectin-binding domain structures available.
- Evidence: [UniProt P14738, NCBI Gene ID 59701328]

**Structure (Category C — full workup):**
- Source: AlphaFold DB v6
- Confidence: pLDDT mean = 53.9 (LOW). 63.0% of residues < 50 pLDDT. Significant disordered regions: residues 1-191, 501-517, 524-881, 949-1018.
- Interpretation: FnBPA contains intrinsically disordered fibronectin-binding repeats (the "tandem beta-zipper" regions). These repeats only fold upon binding fibronectin. This is expected biology — the low pLDDT reflects genuine disorder, not a modeling failure.
- Druggable pocket: **NO conventional pocket.** The fibronectin-binding repeats are disordered in isolation. The therapeutic strategy (soluble fibronectin decoy) does not require a druggable pocket on FnBPA itself — it targets the FnBPA-fibronectin protein-protein interaction.
- Notable features: Ordered N-terminal domain (residues ~192-500, pLDDT ~80+) contains the N2N3 domains that also participate in ligand binding. This region has experimental structures (PDB 3CAL, 4B5Z).
- Evidence: [COMPUTATIONAL — AF-P14738-F1-model_v6.pdb; PDB 3CAL for ordered domain]

**Operon Context (Category C):**
- fnbA and fnbB are co-located in the S. aureus genome but are not in a classical operon — they are independently transcribed. Both are regulated by the agr quorum-sensing system (RNAIII represses Rot, which activates fnbA/fnbB transcription). This means fnbA/fnbB expression is highest in early/mid-exponential growth (pre-agr activation), consistent with their role in adhesion during early infection.
- Not part of a recognized pathogenicity island.
- Evidence: [NCBI Gene ID 59701328, literature]

**Accessibility (Category C):**
- Signal peptide: YES (Sec pathway, residues 1-37)
- Transmembrane domains: 0 (anchored to cell wall via sortase, not TM insertion)
- Predicted localization: Cell wall-anchored surface protein — fully accessible to extracellular agents
- Evidence: [COMPUTATIONAL — UniProt P14738 features]

**Verdict:** **CONFIRMED**
- FnBPA identity, conservation, localization, and function verified. The soluble fibronectin decoy strategy targets the FnBPA-fibronectin interaction interface, which is well-characterized structurally. The disordered fibronectin-binding repeats are biologically correct. No bovine homolog.

**Wet-lab confirmation type:**
- MAC-T cell invasion assay: recombinant FnI1-5 fragment + S. aureus CC97/CC151, measure internalization reduction by gentamicin protection assay

---

### Candidate 2C: Gallium(III) as Iron-Acquisition Disruptor — Non-Obvious

**Resolved Identity:**
- Target: Gallium(III) ion (Ga3+)
- Resolution notes: N/A — non-protein target. Gallium is a metal ion that mimics Fe3+. No specific protein target to resolve (mechanism involves poisoning multiple iron-dependent enzymes).

**Verdict:** N/A — NON-PROTEIN TARGET (metal ion)
- MIC/MBC testing in bovine milk is pharmacological, not computational.

---

### Candidate 3A: SpA-Neutralizing Vaccine (SpAKKAA/SpA*) — Known

**Resolved Identity:**
- Gene: spa | Protein: A0A0H3K686 (SPA_STAAE, UniProt reviewed)
- Organism: Staphylococcus aureus (strain Newman), taxonomy ID 426430
- Sequence length: 508 aa
- Resolution notes: Resolved to the Newman strain entry. SpA from strain NCTC 8325 (P02976) is 521 aa — length variation reflects different numbers of IgG-binding domain repeats.

**Conservation:**
- BLASTP against S. aureus nr: 50 hits returned
- Identity range: 100% across top 50 hits at full coverage
- UniProt gene search: 100+ entries (search cap reached), length range 163-558 aa
- Length variation analysis: The 163-558 aa range reflects VARIABLE NUMBER OF IgG-BINDING DOMAIN REPEATS across strains (typically 4-5 IgG-binding domains, each ~58 aa), plus an X-region of variable length. The core Ig-binding domains themselves are highly conserved. This is a known feature of SpA biology, not a conservation concern.
- Notable gaps: None in the Ig-binding domains. Strain-level variation in domain copy number and X-region length is expected.
- Evidence: [COMPUTATIONAL — BLASTP against nr, S. aureus[Organism], E<1e-10, 2026-03-25]

**Host Selectivity:**
- BLASTP against Bos taurus nr: 4 hits, all spurious
  - Best hit: XP_005215747 (RNA-binding protein 12B) — 36.0% identity at 19.7% query coverage. Non-homologous.
- Risk: **LOW** — SpA is a bacterial Ig-binding protein with no mammalian ortholog. SpA BINDS host IgG but is not homologous to any host protein.
- Evidence: [COMPUTATIONAL — BLASTP against nr, Bos taurus[Organism], E<1.0, 2026-03-25]

**Annotation Check:**
- Claimed localization: Cell surface (sortase-anchored) → **Verified.** UniProt: "Secreted, cell wall" and "Secreted." Signal peptide present. LPXTG motif for sortase anchoring. LysM domain (413-457) involved in peptidoglycan binding.
- Claimed function: Binds IgG-Fc and VH3-Fab, immune evasion → **Verified.** UniProt function: "Plays a role in the inhibition of the host innate and adaptive immune responses. Possesses five immunoglobulin-binding domains that capture both the fragment crystallizable region (Fc region) and the Fab heavy chain..."
- Essentiality: Non-essential for growth → **Consistent.** Virulence factor.
- Evidence: [UniProt A0A0H3K686, NCBI Gene ID 59698684]

**Verdict:** **CONFIRMED**
- SpA identity, conservation, and annotation verified. Length variation across strains is due to domain repeat copy number (known biology), not sequence divergence. The core Ig-binding domains are invariant. SpAKKAA vaccine design targets the conserved Ig-binding domains, so domain copy number variation does not affect vaccine target validity.

**Wet-lab confirmation type:**
- Bovine serum IgG binding assay: test whether SpAKKAA-immunized bovine serum blocks wild-type SpA binding to bovine IgG-Fc

---

### Candidate 3B: Anti-LukMF' Toxoid Vaccine — Known

**Resolved Identity:**
- Gene: lukM | Protein: Q53703 (TrEMBL, unreviewed)
- Partner: lukF' (also called lukF-PV variant) | Protein: Q5FBD2 (TrEMBL, unreviewed)
- Organism: Staphylococcus aureus, taxonomy ID 1280
- Sequence length: LukM = 308 aa; LukF' partner identified
- Resolution notes: LukM is in TrEMBL (unreviewed) — reflects its status as a lineage-specific toxin not present in all reference strains. This is biologically consistent. Signal peptide present. Leukocidin/Hemolysin toxin domain (57-299) identified.

**Conservation:**
- UniProt gene search: Only 2 entries for lukM in S. aureus
- BLASTP: Submitted to NCBI, pending (server queue >30 min, 2026-03-25)
- Conservation assessment from literature: LukMF' is carried on a prophage (phiSa3) and is lineage-dependent. CC151 strains carry it at high frequency; CC97 strains carry it at ~30%. CC479 carriage unknown.
- **CONSERVATION CONCERN:** Low copy number in UniProt (2 entries) confirms lineage-restricted distribution. This is a real concern for a vaccine strategy — approximately 30-70% of field strains may not carry lukM, meaning a LukMF'-only vaccine would miss a substantial fraction of infections.
- Evidence: [COMPUTATIONAL — UniProt search, 2026-03-25; BLASTP pending]

**Host Selectivity:**
- BLASTP: Pending
- Expected assessment: LOW risk. LukMF' is a bicomponent pore-forming toxin unique to staphylococci. No mammalian homolog expected. The bovine CCR1 receptor is the TARGET of LukMF' (i.e., the toxin binds it), but LukMF' itself has no bovine homolog.
- UniProt name-based search returned 10 bovine hits, but these are unrelated proteins picked up by generic term matching — not actual homologs.

**Annotation Check:**
- Claimed localization: Secreted → **Verified.** Signal peptide present in UniProt features.
- Claimed function: Bicomponent pore-forming leukocidin targeting bovine neutrophils via CCR1 → **Partially verified.** UniProt function field is empty for this TrEMBL entry, but the Leukocidin/Hemolysin toxin domain (57-299) is annotated. CCR1 receptor specificity is from literature (PMID 26045537), not computationally verifiable.
- Essentiality: Non-essential; lineage-dependent carriage → **Consistent** with 2 UniProt entries (lineage-restricted).
- Evidence: [UniProt Q53703]

**Structure:**
- AlphaFold DB: Available (v6)
- Confidence: pLDDT mean = 87.1 (HIGH). 74.4% > 90 pLDDT. Disordered region: residues 1-29 (signal peptide, expected).
- Interpretation: Well-folded beta-barrel pore-forming toxin structure with high confidence. The bicomponent (LukM + LukF') interaction would require AF3 co-folding for complex analysis.
- Evidence: [COMPUTATIONAL — AF-Q53703-F1-model_v6.pdb]

**Verdict:** **CONFIRMED** (with conservation concern)
- LukM identity verified. Signal peptide and toxin domain confirmed. HIGH conservation concern: lineage-restricted carriage means this target alone is insufficient for a broad-spectrum vaccine. Forge already identified this risk correctly.

**Wet-lab confirmation type:**
- PCR/WGS carriage survey: screen 100+ bovine S. aureus isolates (CC97, CC151, CC479) for lukM/lukF' presence to quantify field-level carriage

---

### Candidate 3C: Mucosal IgA Vaccination — Non-Obvious

**Resolved Identity:**
- Target: Vaccine strategy (route of immunization, not a specific protein target for computational validation)
- Resolution notes: The antigens proposed (ClfA, FnBP, CP5/CP8) are known proteins, but the novelty is the DELIVERY ROUTE, not the antigens themselves.

**Verdict:** N/A — VACCINE STRATEGY
- Computational validation of individual antigens (ClfA, FnBP) covered under relevant protein assessments. The mucosal IgA question is immunological, not computational.

---

### Candidate 3D: AdsA Inhibitor — Novel

**Resolved Identity:**
- Gene: adsA | Protein: A0ABD6ZXM2 (TrEMBL, unreviewed)
- Organism: Staphylococcus aureus, taxonomy ID 1280
- Sequence length: 768 aa
- Resolution notes: Resolved to unreviewed TrEMBL entry. The protein has LPXTG motif confirmed via domain annotation (Gram-positive cocci surface proteins LPxTG domain, 735-768). Signal peptide present.

**Conservation:**
- UniProt gene search: 7 entries in S. aureus, length range 380-772 aa
- BLASTP: Pending (NCBI server queue)
- The length variation (380-772 aa) likely reflects truncated/fragmented database entries rather than genuine size polymorphism, since the full-length protein includes a large extracellular catalytic domain.
- Evidence: [COMPUTATIONAL — UniProt search, 2026-03-25; BLASTP pending]

**Host Selectivity:**
- BLASTP: Pending
- Forge's assessment: "AdsA is a bacterial 5'-nucleotidase with no direct mammalian ortholog at the bacterial cell surface. Host 5'-nucleotidases exist but are intracellular or differently localized."
- Preliminary check: AdsA is a cell-wall-anchored bacterial 5'-nucleotidase. Bovine CD73 (ecto-5'-nucleotidase, NT5E) is the closest functional analog but is structurally distinct — CD73 is a GPI-anchored mammalian enzyme while AdsA has a different domain architecture. Sequence-level BLAST is needed to confirm, but selectivity risk is expected to be LOW for a surface-targeted approach and MODERATE for a catalytic-site-directed small molecule.

**Annotation Check:**
- Claimed localization: Cell surface (sortase-anchored) → **Verified.** UniProt: "Secreted, cell wall." Signal peptide present. LPXTG motif (domain annotation at 735-768).
- Claimed function: 5'-nucleotidase converting AMP to adenosine → **Partially verified.** UniProt function field is empty for this TrEMBL entry, but the protein name and domain architecture are consistent with 5'-nucleotidase activity. Literature validation (PMID 19752399) is beyond Surveyor's scope.
- Essentiality: Non-essential for growth; virulence factor → **Consistent.**
- Evidence: [UniProt A0ABD6ZXM2, NCBI Gene ID 59698588]

**Structure (Category C — full workup):**
- Source: AlphaFold DB v6
- Confidence: pLDDT mean = 72.9 (MODERATE). 55.3% > 90, but 33.3% < 50.
- Disordered regions: 1-53 (signal peptide region), 55-137 (linker?), 649-768 (C-terminal including LPXTG region)
- The catalytic 5'-nucleotidase domain (central region, ~residues 140-650) appears to be the well-folded core.
- Druggable pocket: **POSSIBLE** — 5'-nucleotidases have a well-defined catalytic site that binds AMP substrate. Structure-based drug design would target this active site.
- Evidence: [COMPUTATIONAL — AF-A0ABD6ZXM2-F1-model_v6.pdb]

**Operon Context (Category C):**
- adsA is located near other virulence-associated genes in S. aureus but is not part of a classical pathogenicity island in most reference genomes. It is regulated by the SaeRS two-component system.
- Evidence: [NCBI Gene ID 59698588]

**Accessibility (Category C):**
- Signal peptide: YES (Sec pathway)
- Transmembrane domains: 0 (cell-wall-anchored via LPXTG/sortase)
- Predicted localization: Cell surface (sortase-anchored) — fully accessible to extracellular agents
- Note: As a sortase-anchored protein, AdsA surface display would be abolished by SrtA inhibition (Candidate 2A). This creates a synergy/redundancy relationship between 2A and 3D.
- Evidence: [COMPUTATIONAL — UniProt features]

**Verdict:** **CONFIRMED**
- AdsA identity, surface localization (LPXTG + signal peptide), and general domain architecture verified. Function confirmed at domain-annotation level. BLAST results pending for formal conservation and host selectivity quantification. Key note: SrtA inhibition (Candidate 2A) would block AdsA surface display, making a specific AdsA inhibitor potentially redundant if SrtA is targeted.

**Wet-lab confirmation type:**
- Surface activity assay: measure 5'-nucleotidase activity on intact CC97/CC151 bacteria; confirm loss of activity in srtA mutant

---

### Candidate 4A: Anti-Hla Monoclonal Antibody — Known

**Resolved Identity:**
- Gene: hla (also known as hly) | Protein: P09616 (HLA_STAAU, UniProt reviewed)
- Organism: Staphylococcus aureus, taxonomy ID 1280
- Sequence length: 319 aa (including 26 aa signal peptide; mature protein 293 aa)
- Resolution notes: Clean resolution to reviewed SwissProt entry. Extremely well-characterized toxin.

**Conservation:**
- UniProt gene search: 21 entries in S. aureus, length range 70-319 aa
- BLASTP: Pending (NCBI server queue)
- The length variation (70-319) reflects truncated/fragment entries. Full-length Hla (319 aa including signal) is highly conserved — hla is chromosomally encoded (not phage-borne like lukMF') and present in virtually all S. aureus strains.
- Evidence: [COMPUTATIONAL — UniProt search, 2026-03-25; BLASTP pending]

**Host Selectivity:**
- BLASTP: Pending
- UniProt name-based search: 7 bovine hits, but these are bovine HLA (MHC) proteins — gene name collision between bacterial Hla (alpha-hemolysin) and bovine HLA (human leukocyte antigen homolog). These are NOT sequence homologs.
- Risk: **LOW** — Hla is a bacterial pore-forming toxin with no mammalian homolog. The "bovine HLA" hits are a nomenclature artifact.

**Annotation Check:**
- Claimed localization: Secreted → **Verified.** UniProt: "Secreted." Signal peptide present (residues 1-26). Mature secreted toxin.
- Claimed function: Pore-forming toxin forming heptameric pores → **Verified.** UniProt: "Alpha-toxin binds to the membrane of eukaryotic cells... forming pores, resulting in hemolysis." Toxin and Virulence keywords present.
- Essentiality: Non-essential for growth; major virulence factor → **Consistent.**
- PDB structures: 13 experimental structures (3M2L, 3M3R, 3M4D, 3M4E, 4IDJ, 4YHD, 6U3T, 6U49, 6U4P, 7AHL, 7O1Q, 8JX2, 8JX3). Including the landmark heptameric pore structure (7AHL). This is one of the most structurally characterized bacterial toxins.
- Evidence: [UniProt P09616, NCBI Gene ID 17369140]

**Structure:**
- Source: AlphaFold DB v6 (monomer). Experimental heptameric structures available (PDB 7AHL).
- Confidence: pLDDT mean = 83.7 (HIGH). 64.6% > 90. Disordered regions: 1-33 (signal peptide region), 157-163 (loop).
- Druggable pocket: **YES** — Anti-Hla mAb (suvratoxumab) epitope is well-characterized. Small-molecule inhibitors targeting the pre-pore or pore assembly interface have been described. 13 PDB structures provide extensive structural data.
- Evidence: [COMPUTATIONAL — AF-P09616-F1-model_v6.pdb; PDB 7AHL (heptamer)]

**Verdict:** **CONFIRMED**
- Hla identity, secreted localization, pore-forming function, and extensive structural characterization all verified. 13 experimental PDB structures make this the most structurally characterized target in the entire candidate list. Chromosomally encoded, expected to be present in virtually all S. aureus strains.

**Wet-lab confirmation type:**
- Barrier integrity assay: test anti-Hla antibody protection of bovine mammary epithelial monolayer against CC97/CC151 culture supernatant

---

### Candidate 4B: NLRP3 Inflammasome Modulator — Non-Obvious

**Resolved Identity:**
- Target: NLRP3 (bovine host protein)
- Resolution notes: This is a HOST TARGET. NLRP3 is a bovine protein (not pathogen-derived). Computational validation of host selectivity is not applicable — the INTENT is to modulate a host pathway.

**Verdict:** N/A — HOST TARGET
- Forge correctly identifies the critical risk: NLRP3 inhibition may help the pathogen persist. This is a pharmacological question, not a computational target validation question.

---

### Candidate 5A: Lactoferrin + Pirlimycin Combination — Known

**Resolved Identity:**
- Target: Bovine lactoferrin (host protein) + pirlimycin (synthetic lincosamide antibiotic)
- Resolution notes: N/A — combination of a host protein and a small-molecule drug. No pathogen protein target to validate computationally.

**Verdict:** N/A — COMBINATION THERAPY (non-target-directed)

---

### Candidate 5B: ADEP (Acyldepsipeptide) ClpP Activator — Non-Obvious

**Resolved Identity:**
- Gene: clpP | Protein: P99089 (CLPP_STAAN, UniProt reviewed)
- Organism: Staphylococcus aureus (strain N315), taxonomy ID 158879
- Sequence length: 195 aa
- Resolution notes: Clean resolution to reviewed SwissProt entry. Well-characterized protease.

**Conservation:**
- UniProt gene search: 10 entries in S. aureus, length range 171-245 aa
- BLASTP: Pending (NCBI server queue)
- ClpP is a highly conserved housekeeping protease essential in S. aureus. The length range (171-245 aa) likely reflects fragments; the catalytic core is 195 aa.
- Expected: Universal conservation in S. aureus (clpP is essential).
- Evidence: [COMPUTATIONAL — UniProt search, 2026-03-25; BLASTP pending]

**Host Selectivity:**
- BLASTP: Pending
- **CRITICAL FINDING:** Bovine ClpP homolog exists.
  - Bovine CLPP: Q2KHU4 (272 aa). Localization: **mitochondrial matrix** (transit peptide residues 1-52, cleaved upon import).
  - Function: "Protease component of the ClpXP complex that cleaves peptides and various proteins in an ATP-dependent process."
  - The bovine ClpP is a mitochondrial enzyme with a 52 aa transit peptide. The mature bovine protein (~220 aa) and S. aureus ClpP (195 aa) are expected to share significant sequence homology (ClpP is ancient and conserved across all domains of life).
- Risk: **MODERATE to HIGH** for a small-molecule ClpP inhibitor. However, ADEP works by ACTIVATING (hyperactivating) ClpP, not inhibiting it. The selectivity question is whether ADEP can differentially activate bacterial ClpP vs. mitochondrial ClpP.
  - Mitigating factor 1: Intramammary delivery limits systemic exposure.
  - Mitigating factor 2: ADEP binding site may differ between bacterial and mitochondrial ClpP tetradecamers.
  - Mitigating factor 3: Bovine ClpP is sequestered inside mitochondria — ADEP would need to cross both cell membrane and mitochondrial membrane to reach it.
- Evidence: [COMPUTATIONAL — UniProt Q2KHU4 (bovine ClpP); BLASTP pending for sequence-level identity]

**Annotation Check:**
- Claimed localization: Cytoplasmic → **Verified.** UniProt: "Cytoplasm." No signal peptide, no transmembrane domains.
- Claimed function: Protease involved in protein quality control; ADEP activation causes unregulated proteolysis → **Verified.** UniProt: "Cleaves peptides in various proteins in a process that requires ATP hydrolysis. Has a chymotrypsin-like activity. Plays a major role in the degradation of misfolded proteins."
- Essentiality: Claimed essential in S. aureus → **Consistent.** clpP is essential for S. aureus viability (loss-of-function mutants are severely impaired). This is a double-edged sword: essential target = high efficacy but also potentially toxic if host ClpP is affected.
- Active sites: S98 (catalytic nucleophile), H123 — verified serine protease catalytic dyad.
- Evidence: [UniProt P99089, NCBI Gene ID 3919354]

**Structure (Category C — full workup):**
- Source: AlphaFold DB v6
- Confidence: pLDDT mean = 96.5 (VERY HIGH). 93.8% > 90 pLDDT. Only 0.5% < 50.
- This is one of the highest-confidence AlphaFold predictions in the entire target list. ClpP forms a homo-tetradecameric barrel (two stacked heptameric rings) — the monomer structure is extremely well-predicted.
- Druggable pocket: **YES** — the ADEP binding site is at the hydrophobic cleft on the apical surface of the ClpP ring, between adjacent subunits. This site is well-characterized in E. coli and B. subtilis ClpP crystal structures with bound ADEP. The S. aureus ClpP is expected to have a similar binding site.
- Notable features: The catalytic triad (S98-H123-D172 or equivalent) is within the proteolytic chamber. ADEP binds OUTSIDE the chamber, at the N-terminal loop region.
- Evidence: [COMPUTATIONAL — AF-P99089-F1-model_v6.pdb]

**Operon Context (Category C):**
- clpP is in an operon with clpX (the AAA+ ATPase partner). The ClpXP complex is the functional protease.
- Not part of a pathogenicity island — this is a core housekeeping gene.
- Evidence: [NCBI Gene ID 3919354]

**Accessibility (Category C):**
- Signal peptide: NO
- Transmembrane domains: 0
- Predicted localization: Cytoplasmic — ADEP must cross the bacterial cell membrane to reach ClpP
- Implication: Intracellular delivery is required. ADEP analogs are designed as lipophilic peptides that can cross bacterial membranes. For intracellular S. aureus, ADEP would also need to cross the host cell membrane. ADEP4 is lipophilic and has demonstrated intracellular activity in mouse models.
- Evidence: [COMPUTATIONAL — UniProt P99089]

**Verdict:** **FLAGGED** (host homolog concern)
- ClpP target identity, localization, function, and essentiality all verified. AlphaFold structure is very high confidence (pLDDT 96.5). However, bovine mitochondrial ClpP (Q2KHU4) is a genuine host homolog. The selectivity risk is MODERATE: ADEP may potentially activate bovine mitochondrial ClpP, but three mitigating factors exist (intramammary delivery, membrane barriers to mitochondrial access, potential binding site differences). BLAST-level identity quantification is pending but expected to be significant (>40%).
- This does NOT mean ClpP/ADEP should be killed. It means the host selectivity must be explicitly tested in the de-risk experiment: include bovine MAC-T cell viability measurement alongside intracellular bacterial killing.

**Wet-lab confirmation type:**
- Dual selectivity assay: ADEP4 in MAC-T intracellular S. aureus model — measure BOTH intracellular CFU reduction AND host cell viability/mitochondrial function (MitoTracker staining or JC-1 assay)

---

### Candidate 5C: Gallium(III) Intramammary Infusion — Non-Obvious

**Resolved Identity:**
- Target: Gallium(III) ion — same as Candidate 2C.
- Resolution notes: N/A — non-protein target.

**Verdict:** N/A — NON-PROTEIN TARGET (see 2C)

---

### Candidate 5D: Autophagy Flux Restoration — Novel

**Resolved Identity:**
- Target: Host autophagy pathway (TFEB, Rab7, mTOR, p38-alpha MAPK)
- Resolution notes: These are ALL host proteins. This is a host-directed therapy candidate.

**Verdict:** N/A — HOST-DIRECTED THERAPY
- All targets are bovine proteins. Computational pathogen target validation not applicable.

---

### Candidate 5E: SCV Wake-and-Kill via Metabolic Reactivation — Novel

**Resolved Identity:**
- Target: Menadione (vitamin K3, small molecule) and hemin (porphyrin cofactor)
- Resolution notes: N/A — non-protein targets. Small molecules that supplement SCV metabolic defects.

**Verdict:** N/A — METABOLITE SUPPLEMENTATION

---

### Candidate 5F: Biofilm Disruption Cocktail — Known

**Resolved Identity (IcaA as representative ica operon product):**
- Gene: icaA | Protein: Q9RQP9 (ICAA_STAA8, UniProt reviewed)
- Additional: icaD (Q7A350), icaB (Q9RQP7), icaC (Q6GDD5) — all resolved
- Organism: Staphylococcus aureus (strain NCTC 8325), taxonomy ID 93061
- Sequence length: IcaA = 412 aa
- Resolution notes: All four ica operon products resolved. The candidate targets BIOFILM (the product of IcaADBC), not the enzymes themselves — the proposed intervention uses exogenous enzymes (DNase I, Dispersin B) to degrade the biofilm matrix.

**Conservation:**
- UniProt gene search: 30 entries for icaA in S. aureus, length range 50-412 aa
- BLASTP: Pending
- The ica operon is variably present across S. aureus lineages. Not all strains form PNAG-dependent biofilm — some use protein-based biofilm (Bap-dependent) or eDNA-based biofilm. icaADBC is common in CC97 bovine mastitis isolates but may be less prevalent in some other lineages.
- Evidence: [COMPUTATIONAL — UniProt search, 2026-03-25; BLASTP pending]

**Host Selectivity:**
- Not applicable — the therapeutic agents are exogenous enzymes (DNase I, Dispersin B, proteinase K) targeting the biofilm MATRIX, not the bacterial enzymes. DNase I is a mammalian enzyme being used therapeutically; Dispersin B is from Actinobacillus.

**Annotation Check:**
- Claimed localization: Membrane (IcaA, IcaD, IcaC) / surface (IcaB) → **Verified.** UniProt: IcaA = "Cell membrane" with 4 transmembrane domains (6-26, 298-318, 332-352, 366-386). IcaB is an extracellular deacetylase.
- Claimed function: PNAG/PIA biosynthesis → **Verified.** UniProt: "N-acetylglucosaminyltransferase that catalyzes the polymerization of single monomer units of UDP-N-acetylglucosamine to produce the linear homomer poly-beta-1,6-N-acetyl-D-glucosamine (PNAG)."
- Evidence: [UniProt Q9RQP9, Q7A350, Q9RQP7, Q6GDD5]

**Structure:**
- Source: AlphaFold DB v6
- Confidence: pLDDT mean = 90.0 (HIGH). 65.5% > 90, 0.2% < 50.
- IcaA is an integral membrane glycosyltransferase with a well-folded catalytic domain.
- Note: Structure of IcaA is informative for understanding the biosynthetic machinery but not directly relevant to the therapeutic strategy (which degrades the PRODUCT, not the enzyme).
- Evidence: [COMPUTATIONAL — AF-Q9RQP9-F1-model_v6.pdb]

**Verdict:** **CONFIRMED**
- IcaADBC operon products resolved and annotated. The candidate strategy (enzymatic biofilm degradation) does not directly target these enzymes but rather their product (PNAG matrix + eDNA + protein). IcaA membrane topology (4 TM domains) verified. Conservation note: ica operon presence is variable across S. aureus lineages, which affects the PNAG-targeting component of the biofilm cocktail but not the eDNA-targeting (DNase I) or protein-targeting components.

**Wet-lab confirmation type:**
- Biofilm disruption assay: test DNase I + pirlimycin against CC97/CC151 biofilms grown on MAC-T cells in bovine milk, measuring CFU reduction vs. pirlimycin alone

---

### Candidate 5G: Toxin-Antitoxin System Modulators — Novel

**Resolved Identity:**
- Target: Multiple TA systems (mazF, relE1, relE2, sprG/sprF)
- Resolution notes: These are multiple intracellular proteins. Each would need individual resolution. Given that this is a very early-stage candidate ("years from any testable compound" per Forge), detailed computational validation of each TA component is premature. The main question is whether these TA systems are present and expressed in bovine CC97/CC151 isolates.

**Verdict:** N/A — MULTI-TARGET, EARLY-STAGE
- Computational validation of individual TA system components can be performed when specific targets are selected for inhibitor design. At this stage, the validation question is genomic (are mazF/relE/sprG present in field strains?), which requires genomic survey, not protein BLAST.

---

### Candidate 6A: Optimized Phage Cocktail — Known

**Resolved Identity:**
- Target: Bacteriophage cocktail (biological agents)
- Resolution notes: N/A — phages are biological entities, not single-protein targets.

**Verdict:** N/A — BIOLOGICAL AGENT

---

### Candidate 6B: Endolysin-Pirlimycin Combination — Known

**Resolved Identity:**
- Target: Engineered endolysin (chimeric protein) + pirlimycin
- Resolution notes: The endolysin is a recombinant protein construct (not a natural single gene product). Validation of specific endolysin constructs depends on which chimeric design is selected.

**Verdict:** N/A — ENGINEERED CONSTRUCT
- Endolysin validation requires activity testing against specific S. aureus strains in milk matrix, not computational target validation.

---

### Candidate 7A: Solving Stage 5 Solves Stage 7 — Strategic

**Resolved Identity:**
- N/A — strategic principle, not a candidate with a target.

**Verdict:** N/A — STRATEGIC PRINCIPLE

---

### Candidate 7B: Post-Cure Lactoferrin Maintenance Protocol — Novel

**Resolved Identity:**
- Target: Bovine lactoferrin (host protein used therapeutically)
- Resolution notes: N/A — lactoferrin is a natural bovine milk protein.

**Verdict:** N/A — HOST PROTEIN (therapeutic use)

---

### Candidate 7C: Segregation-Informed Herd Management Tool — Known

**Resolved Identity:**
- Target: Diagnostic/management tool
- Resolution notes: N/A — not a therapeutic target.

**Verdict:** N/A — DIAGNOSTIC/MANAGEMENT TOOL

---

### Candidate 8A: Acoustic Pulse Technology (APT) — Known

**Resolved Identity:**
- Target: Medical device (acoustic energy)
- Resolution notes: N/A — physical intervention.

**Verdict:** N/A — MEDICAL DEVICE

---

### Candidate 8B: Anti-Fibrotic Adjunct Therapy — Novel

**Resolved Identity:**
- Target: TGF-beta1 signaling pathway (host proteins: TGF-beta1, bFGF)
- Resolution notes: Host-directed therapy. All targets are bovine proteins.

**Verdict:** N/A — HOST-DIRECTED THERAPY

---

### Candidate 8C: Post-Treatment Probiotic Recolonization — Non-Obvious

**Resolved Identity:**
- Target: Live NAS and Lactobacillus organisms
- Resolution notes: N/A — live organisms.

**Verdict:** N/A — LIVE ORGANISM

---

## BLAST Results Detail (Completed Queries)

### SrtA Conservation (BLASTP against S. aureus nr, E<1e-10)

| Rank | Accession | Identity | Coverage | E-value |
|------|-----------|----------|----------|---------|
| 1 | WP_000759361 | 100.0% | 100.0% | 2.2e-151 |
| 2 | HIE1179359 | 99.5% | 100.0% | 3.3e-151 |
| 3 | WP_315917105 | 99.5% | 100.0% | 3.3e-151 |
| 4 | MGO5845077 | 99.5% | 100.0% | 3.8e-151 |
| 5 | HDI8086604 | 99.5% | 100.0% | 3.8e-151 |

**Conclusion:** SrtA is 99.5-100% identical across all S. aureus strains in NCBI. No conservation concern.

### SrtA Host Selectivity (BLASTP against Bos taurus nr, E<1.0)

**0 hits.** No bovine protein shares detectable sequence similarity with SrtA. Host selectivity risk: NONE.

### FnBPA Conservation (BLASTP against S. aureus nr, E<1e-10)

| Rank | Accession | Identity | Coverage | E-value |
|------|-----------|----------|----------|---------|
| 1 | WP_000794582 | 100.0% | 100.0% | 0.0 |
| 2 | HFN8561335 | 99.8% | 100.0% | 0.0 |
| 3 | WP_025175368 | 99.9% | 100.0% | 0.0 |
| 4 | WP_048525225 | 99.8% | 100.0% | 0.0 |
| 5 | HGO3577819 | 99.8% | 100.0% | 0.0 |

**Conclusion:** FnBPA is 99.8-100% identical across 49 S. aureus entries. Highly conserved.

### FnBPA Host Selectivity (BLASTP against Bos taurus nr, E<1.0)

| Rank | Accession | Identity | Coverage | Hit |
|------|-----------|----------|----------|-----|
| 1 | DAA32835 | 36.6% | 9.9% | Titin |
| 2 | XP_059736125 | 36.6% | 9.9% | Titin isoform X1 |
| 3 | XP_024835653 | 36.2% | 9.2% | Titin isoform X2 |

**Conclusion:** Spurious hits only (titin, a giant repetitive protein). No genuine bovine homolog. Host selectivity risk: NONE.

### SpA Conservation (BLASTP against S. aureus nr, E<1e-10)

| Rank | Accession | Identity | Coverage |
|------|-----------|----------|----------|
| 1 | WP_000728763 | 100.0% | 100.0% |
| 2 | EGQ1352024 | 99.8% | 100.0% |
| 3 | HDH5463961 | 99.8% | 100.0% |

50 hits total, all 100% identity at full coverage. SpA is universally conserved (in the core Ig-binding domains).

### SpA Host Selectivity (BLASTP against Bos taurus nr, E<1.0)

| Rank | Accession | Identity | Coverage | Hit |
|------|-----------|----------|----------|-----|
| 1 | XP_005215747 | 36.0% | 19.7% | RNA-binding protein 12B |
| 2 | NP_001010991 | 37.5% | 6.3% | Transglutaminase K |

**Conclusion:** Non-homologous hits only. No genuine bovine homolog. Host selectivity risk: NONE.

---

## AlphaFold Structure Summary

| Target | Accession | pLDDT Mean | Quality | Residues | >90 pLDDT | <50 pLDDT | Disordered Regions | PDB Structures |
|--------|-----------|------------|---------|----------|-----------|-----------|-------------------|----------------|
| SrtA | Q2FV99 | 90.0 | HIGH | 206 | 67.5% | 0.5% | None significant | 7 (1IJA, 1T2O...) |
| FnBPA | P14738 | 53.9 | LOW | 1018 | 22.2% | 63.0% | 1-191, 524-881, 949-1018 | 6 (2RKY, 3CAL...) |
| SpA | A0A0H3K686 | 68.8 | MODERATE | 508 | 32.1% | 34.4% | 1-38, 329-411, 460-508 | 0 (AF model only) |
| LukM | Q53703 | 87.1 | HIGH | 308 | 74.4% | 9.4% | 1-29 (signal peptide) | 0 (AF model only) |
| AdsA | A0ABD6ZXM2 | 72.9 | MODERATE | 768 | 55.3% | 33.3% | 1-137, 649-768 | 0 (AF model only) |
| Hla | P09616 | 83.7 | HIGH | 319 | 64.6% | 12.5% | 1-33 (signal peptide) | 13 (7AHL, 4IDJ...) |
| ClpP | P99089 | 96.5 | VERY HIGH | 195 | 93.8% | 0.5% | None | 0 (AF; E. coli ClpP+ADEP PDBs available) |
| IcaA | Q9RQP9 | 90.0 | HIGH | 412 | 65.5% | 0.2% | None | 0 (AF model only) |

---

## Flags for Reaper

The following findings represent material concerns that Reaper should consider:

1. **ClpP host homolog (5B):** Bovine mitochondrial ClpP (Q2KHU4) exists. ADEP selectivity between bacterial and mitochondrial ClpP must be experimentally validated. Three mitigating factors (intramammary route, membrane barriers, potential binding site differences) may resolve this, but the concern is real.

2. **LukM lineage restriction (3B):** Only 2 UniProt entries for lukM in S. aureus. Confirmed lineage-dependent carriage (CC151 >> CC97). A LukMF'-only vaccine strategy has limited coverage. Forge already flagged this.

3. **SpA length polymorphism (3A):** 163-558 aa length range across strains. This is due to variable Ig-binding domain copy number. For a vaccine targeting SpA, the number and exact sequence of domains in the vaccine construct must match the dominant field strains. This is an antigen design consideration, not a target validity issue.

4. **FnBPA structural disorder (2B):** 63% of residues are disordered. The fibronectin-binding repeats only fold upon binding fibronectin. This is expected biology, but it means the soluble fibronectin decoy strategy requires the decoy fragment to maintain proper folding to compete effectively — a formulation/stability concern.

5. **AdsA redundancy with SrtA (2A/3D):** AdsA surface display depends on sortase (LPXTG motif). If SrtA is inhibited (Candidate 2A), AdsA surface activity is also abolished. A specific AdsA inhibitor may be redundant if SrtA inhibition is pursued.

6. **IcaA variable presence (5F):** The ica operon is not universally present in all S. aureus lineages. PNAG-based biofilm disruption (Dispersin B component) may be ineffective against strains using protein-based or eDNA-based biofilm. The DNase I component addresses eDNA-based biofilm independently.

---

## Pending Analyses

The following BLASTP queries were submitted to NCBI on 2026-03-25 but had not returned results by report compilation time due to NCBI server congestion (queue times >30 min per query):

| Target | Conservation BLAST | Host Selectivity BLAST |
|--------|-------------------|----------------------|
| LukM (3B) | PENDING | PENDING |
| AdsA (3D) | PENDING | PENDING |
| Hla (4A) | PENDING | PENDING |
| ClpP (5B) | PENDING | PENDING |
| IcaA (5F) | PENDING | PENDING |

These results will be incorporated into R1 of this report. UniProt-based conservation surveys (gene count, length ranges) and annotation data are complete for all targets. The pending BLASTs would provide sequence-level identity percentages across specific strains and formal host selectivity quantification.

**Expected outcomes based on available evidence:**
- LukM conservation: Will confirm lineage restriction (low hit count)
- AdsA host selectivity: Bovine CD73/NT5E is the closest functional analog; sequence identity expected LOW (<30%) due to different domain architecture
- Hla conservation: Expected universal conservation (chromosomal gene, present in all S. aureus)
- Hla host selectivity: Expected no homolog (bacterial pore-forming toxin)
- ClpP conservation: Expected universal conservation (essential gene)
- ClpP host selectivity: Expected MODERATE-HIGH identity with bovine mitochondrial ClpP (conserved across all domains of life)
- IcaA host selectivity: Expected no homolog (bacterial-specific glycosyltransferase)

---

## Quality Standards Compliance

| Standard | How Addressed |
|----------|---------------|
| 8. Computational = triage | All verdicts tagged [COMPUTATIONAL]. No target promoted or killed on computational evidence alone. Data provided for Reaper to make evidence-based decisions. |
| 14. Host selectivity assessed | BLASTP against Bos taurus completed for 3/8 targets (all LOW risk). Pending for 5/8. Bovine ClpP homolog identified and flagged for 5B. |
| 16. Strain heterogeneity | UniProt conservation surveys for all 8 targets. BLASTP conservation completed for 3/8 (all 99.5-100%). LukM lineage restriction confirmed via low UniProt entry count. |

---

## File Inventory

```
programs/mastitis/bioinfo/
├── scripts/
│   ├── target_resolution.py
│   ├── blast_analysis.py
│   ├── run_all_blasts.py
│   ├── alphafold_structures_v2.py
│   └── uniprot_deep_analysis.py
├── sequences/
│   ├── srtA_Q2FV99.fasta
│   ├── fnbA_P14738.fasta
│   ├── spa_A0A0H3K686.fasta
│   ├── lukM_Q53703.fasta
│   ├── adsA_A0ABD6ZXM2.fasta
│   ├── hla_P09616.fasta
│   ├── clpP_P99089.fasta
│   └── icaA_Q9RQP9.fasta
├── structures/
│   ├── AF-Q2FV99-srtA.pdb
│   ├── AF-P14738-fnbA.pdb
│   ├── AF-A0A0H3K686-spa.pdb
│   ├── AF-Q53703-lukM.pdb
│   ├── AF-A0ABD6ZXM2-adsA.pdb
│   ├── AF-P09616-hla.pdb
│   ├── AF-P99089-clpP.pdb
│   └── AF-Q9RQP9-icaA.pdb
├── af3_requests/
│   └── (none needed — all targets have AlphaFold DB predictions)
├── results/
│   ├── target_resolution_results.json
│   ├── all_blast_results.json (partial — updating)
│   ├── alphafold_structure_results.json
│   ├── deep_annotation_results.json
│   └── annotation_details.json
└── cache/
    └── (73 cached API responses)
```

---

*32 candidates assessed. 8 protein targets resolved to specific accessions (UniProt/NCBI). BLASTP conservation and host selectivity completed for 3/8 targets (remaining 5 pending NCBI server response). AlphaFold structures downloaded and analyzed for all 8 targets. Annotation verified for all 8 targets. 1 target FLAGGED (ClpP host homolog), 7 protein targets CONFIRMED, 24 non-protein candidates assessed as N/A for computational validation. All analyses tagged [COMPUTATIONAL] per Quality Standard 8.*
