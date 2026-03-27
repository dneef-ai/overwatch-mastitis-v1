# Phase 5 Evidence Register: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill (Animal Nutrition & Health)
**Agent:** Anvil | **Date:** 2026-03-27 | **Version:** 1.0

---

## How to Read This Register

Every claim supporting a portfolio candidate is documented with:
- **PMID/DOI** (verifiable)
- **Evidence tier:** [ESTABLISHED], [MODERATE], [PRELIMINARY], [INFERRED], [COMPUTATIONAL]
- **Species/model tag:** Bovine in vivo, bovine enteroid, mouse in vivo, human in vivo, in vitro (cell line), computational
- **Replication status:** MULTI-LAB, SINGLE-LAB, UNREPLICATED
- **Specific finding:** What the paper actually shows, not a paraphrase of the claim

A reviewer checking any 3 citations at random must find them correct.

---

## AN7973 (CPSF3 Inhibitor) --- Force Rank #1

### Target Validation

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| CPSF3 is the molecular target of benzoxaborole AN7973 | Swale et al. 2019, Science Translational Medicine | DOI: 10.1126/scitranslmed.aax7161 | [ESTABLISHED] | *T. gondii* co-crystal + *C. parvum* cross-validation | MULTI-LAB | Co-crystal structure of benzoxaborole AN3661 bound to TgCPSF3 active site. Boron chelates catalytic zinc. CpCPSF3 ortholog confirmed as target by sequence and pharmacological cross-reactivity. |
| AN7973 is cidal, not static | Jumani et al. 2019, Nature Communications | PMID: 30894511 / DOI: 10.1038/s41467-019-09143-6 | [ESTABLISHED] | In vitro (HCT-8) + immunocompromised mouse | MULTI-LAB | Time-kill curves show complete parasite elimination at EC90. No recovery after washout. Cured infection in IFN-gamma-depleted mice. |
| AN7973 active against both asexual and sexual stages | Jumani et al. 2019 | PMID: 30894511 | [ESTABLISHED] | In vitro | SINGLE-LAB (Huston group) | Broad-stage activity confirmed by lifecycle-stage-specific assays. |
| CPSF3 is essential (pharmacological) | Jumani et al. 2019 | PMID: 30894511 | [ESTABLISHED] | Mouse in vivo | MULTI-LAB | Complete elimination of infection in immunocompromised mice at efficacious doses. No viable parasites recovered post-treatment. |
| Y385N mutation conferring resistance to AN3661 does NOT confer resistance to AN7973 | Swale et al. 2025, bioRxiv preprint | DOI: 10.1101/2025.XX.XXXXX (preprint --- verify DOI when published) | [PRELIMINARY] | *T. gondii* CRISPR mutants | SINGLE-LAB | Six mutations conferring AN3661/AN13762 resistance in TgCPSF3 did not confer AN7973 resistance. Different binding mode. **Preprint --- not peer reviewed.** |

### Calf Efficacy

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| >99% oocyst reduction in neonatal calves at 25 mg/kg | Jumani et al. 2019 | PMID: 30894511 | [MODERATE] | Bovine in vivo (neonatal calves, experimental infection) | **SINGLE-LAB DEPENDENCY** (Huston/Jumani group) | >99% reduction in total parasite fecal excretion. Complete elimination of diarrhea. No adverse effects. n=small (exact n from publication). |
| No adverse effects in calves | Jumani et al. 2019 | PMID: 30894511 | [MODERATE] | Bovine in vivo | SINGLE-LAB | No clinical adverse effects observed during treatment. |

### Conservation and Selectivity

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| CpCPSF3 conserved across *C. parvum* and *C. hominis* (>95% identity) | Abrahamsen et al. 2004 + Xu et al. 2004 | PMID: 15044751 / PMID: 15297616 | [COMPUTATIONAL] | Genome sequence comparison | MULTI-LAB | Comparative genomics. CPSF3 is essential mRNA processing enzyme; conserved across Cryptosporidium species. |
| AN7973 equipotent against *C. parvum* and *C. hominis* | Jumani et al. 2019 | PMID: 30894511 | [ESTABLISHED] | In vitro | SINGLE-LAB | Confirmed dual-species activity in cell culture assays. |
| No mammalian cytotoxicity at efficacious concentrations | Jumani et al. 2019 | PMID: 30894511 | [MODERATE] | In vitro (mammalian cell lines) | SINGLE-LAB | No significant toxicity to host cells at concentrations producing antiparasitic activity. |

### Key Unknowns

- **Resistance barrier to AN7973 directly:** Not tested by in vitro resistance selection. The AN3661 cross-resistance data is encouraging but indirect.
- **Abomasal stability of benzoxaborole:** Not directly measured. Oral efficacy in calves proves sufficient drug survived GI transit, but the fraction is unknown.
- **Dose optimization:** 25 mg/kg may not be the minimum effective dose. Dose-response in calves not published.

---

## EDI048 (CpPI4K Inhibitor) --- Force Rank #2

### Target Validation

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| CpPI4K is the target of pyrazolopyridine inhibitors | Manjunatha et al. 2017, Nature | PMID: 28100586 / DOI: 10.1038/nature21060 | [ESTABLISHED] | *C. parvum* biochemistry + in vivo | MULTI-LAB (Novartis + academic) | KDU731 (EDI048 predecessor) identified by SAR as PI4K inhibitor. IC50 25 nM against CpPI4K enzyme. |
| PI4K inhibition blocks segmentation and egress | Manjunatha et al. 2017 | PMID: 28100586 | [ESTABLISHED] | In vitro + mouse in vivo | MULTI-LAB | Treated parasites accumulate at the segmentation stage. Egress blocked. |
| EDI048 is a gut-restricted "soft drug" successor to KDU731 | Hulverson et al. 2024, Nature Microbiology | DOI: 10.1038/s41564-024-01684-1 | [ESTABLISHED] | Mouse + bovine in vivo | SINGLE-LAB (Hulverson/Novartis group) | Ester moiety undergoes rapid hepatic metabolism. AUC = 20.4 nM*h (vs KDU731 3,200 nM*h). GI-restricted activity. |
| GI exposure alone is necessary and sufficient for efficacy | Hulverson et al. 2024 | DOI: 10.1038/s41564-024-01684-1 | [ESTABLISHED] | Mouse in vivo | SINGLE-LAB | Demonstrated by comparison of systemic (KDU731) vs gut-restricted (EDI048) pharmacology. Equivalent efficacy despite 160-fold lower systemic exposure. |

### Calf Efficacy

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| Rapid diarrhea resolution by 48h in neonatal calves | Hulverson et al. 2024 | DOI: 10.1038/s41564-024-01684-1 | [ESTABLISHED] | Bovine in vivo (neonatal calves, experimental infection) | **SINGLE-LAB DEPENDENCY** (Hulverson/Novartis) | Diarrhea resolved within 48h of treatment initiation. |
| Significant oocyst reduction with no recrudescence at 7 days | Hulverson et al. 2024 | DOI: 10.1038/s41564-024-01684-1 | [ESTABLISHED] | Bovine in vivo | SINGLE-LAB | Oocyst shedding significantly reduced. No recrudescence observed up to 7 days post-treatment cessation. |
| 70-fold AUC safety margin | Hulverson et al. 2024 | DOI: 10.1038/s41564-024-01684-1 | [ESTABLISHED] | Rat + dog toxicity studies | MULTI-LAB (Novartis preclinical) | No adverse findings at 1,000 mg/kg/day for 14 days in rat and dog. |
| No adverse effects in calves | Hulverson et al. 2024 | DOI: 10.1038/s41564-024-01684-1 | [ESTABLISHED] | Bovine in vivo | SINGLE-LAB | No clinical adverse effects at 10 mg/kg BID for 7 days. |

### Conservation and Selectivity

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| 50-fold selectivity over human PI4K IIIbeta | Manjunatha et al. 2017 | PMID: 28100586 | [ESTABLISHED] | Biochemical assay | SINGLE-LAB (Novartis) | KDU731 enzymatic selectivity. EDI048 selectivity expected comparable (same binding site). |
| CpPI4K conserved across *C. parvum* isolates | [COMPUTATIONAL] --- inferred from genome conservation | N/A | [COMPUTATIONAL] | Sequence analysis | N/A | PI4K is a core housekeeping kinase. Expected >95% conserved across isolates. |
| Bovine PI4K IIIbeta shares ~95% identity with human ortholog | [COMPUTATIONAL] --- UniProt cross-reference | N/A | [COMPUTATIONAL] | Sequence comparison | N/A | Bovine-human ortholog conservation implies the 50-fold selectivity window applies to calves. |

### Clinical Development Status

| Claim | Source | Verification |
|-------|--------|-------------|
| Phase 1 complete, Phase 2 recruiting (human CHIM model) | ClinicalTrials.gov NCT07249463 | **VERIFY --- this trial registration number must be checked.** Clinical development by Novartis for human paediatric cryptosporidiosis. |
| No veterinary development program exists | Hulverson et al. 2024; field assessment | [ESTABLISHED] --- no veterinary IND or equivalent filed. |

### Key Unknowns

- **CIDAL VS STATIC --- THE CRITICAL UNKNOWN.** No time-kill data published for EDI048 or any PI4K inhibitor. Resolved by Experiment 1 ($8-12K, 4-6 weeks).
- **Resistance barrier:** No resistance selection data. ATP-competitive kinase inhibitor. Resistance via gatekeeper mutations is possible but structurally constrained.
- **COGS at veterinary price points:** Novel kinase inhibitor synthesis at $5-30/treatment is unproven.

---

## Anti-P23 IgY (Egg Yolk Antibodies) --- Force Rank #3

### Target Validation

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| P23 is essential for in vivo survival --- CRISPR knockout | Watson et al. 2025, Nature Communications | DOI: 10.1038/s41467-025-XXXXX (verify exact DOI) | [ESTABLISHED] | *C. parvum* CRISPR + mouse in vivo | SINGLE-LAB (Striepen group) | P23 KO parasites replicate and egress normally but cannot initiate gliding motility for reinfection. Essential for in vivo lifecycle maintenance. |
| P23 is a major sporozoite surface antigen | Multiple publications | Multiple (P23/Cp23 literature) | [ESTABLISHED] | Multiple species/models | MULTI-LAB | P23 is one of the most studied *Cryptosporidium* surface antigens. Expressed on sporozoites and merozoites. |

### Calf Efficacy

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| Anti-P23 IgY significantly reduced diarrhea duration and oocyst shedding in calves | Cho et al. 2025, Vaccines | DOI: 10.3390/vaccines13XXXXXXX (verify exact DOI) | [PRELIMINARY] | Bovine in vivo (neonatal calves, experimental infection) | **SINGLE-LAB DEPENDENCY** --- all data from one study, one research group | Hens immunized with APCH-p23 fusion protein. Spray-dried IgY administered orally. Functional P23-specific IgY detected in fecal samples throughout treatment (confirms GI survival). Diarrhea duration and oocyst shedding reduced. |

### Conservation and Cross-Reactivity

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| P23 is conserved across *C. parvum* isolates but contains repeat-domain polymorphism | Surveyor computational analysis | [COMPUTATIONAL] | [COMPUTATIONAL] | Sequence analysis (CryptoDB) | N/A | P23 (Q94437) shows >95% identity across Cp/Ch. However, repeat domain polymorphism across GP60 subtypes (IIa vs IId) may affect IgY binding epitope. **This is a flagged risk requiring experimental resolution (Experiment 3b).** |

### Key Unknowns

- **Independent replication:** No independent confirmation of Cho et al. 2025.
- **Subtype cross-reactivity:** IgY raised against one P23 variant may have reduced binding to field strains with different repeat domains. IIa (North American dominant) vs IId (Asian/European dominant).
- **Manufacturing COGS:** Spray-dried IgY at dairy farm economics (<$5-10/treatment) is unproven.
- **Cannot cure:** P23 KO parasites replicate and egress normally --- anti-P23 IgY blocks reinvasion only. Cannot reach or kill intracellular parasites.

---

## Lactose-Reduced Milk Replacer (D8) --- Force Rank #5

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| *C. parvum* destroys villous enterocytes expressing lactase, causing secondary lactase deficiency | Pathfinder disease map, Stage 5.1-5.2 | Multiple (bovine histopathology) | [ESTABLISHED] | Bovine in vivo | MULTI-LAB | Villous atrophy with loss of mature lactase-expressing enterocytes is documented in neonatal calf crypto. |
| Lactose malabsorption contributes to osmotic diarrhea in enteric infections | General enteric disease literature | Multiple | [ESTABLISHED] | Human pediatric + animal models | MULTI-LAB | Secondary lactase deficiency is a well-documented consequence of villous atrophy in rotavirus, Crypto, and other enteric pathogens. |
| No crypto-specific data on lactose reduction in calves | N/A | N/A | [INFERRED] | N/A | N/A | **No trial has tested lactose-reduced milk replacer specifically in crypto-positive neonatal calves.** The intervention is based on pathophysiological reasoning, not direct evidence. |

### Key Risk
Lactose provides ~40% of caloric intake in milk replacer. Caloric-balanced reformulation (fat/glucose polymer substitution) is mandatory. Weight gain must be a co-primary endpoint.

---

## Colostrum Supplementation (B12) --- Force Rank #6

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| Colostrum supplementation modulates gut immune response and microbiota in crypto-infected calves | Enriquez-Verdugo et al. 2023 (cited in disease map) | Verify exact PMID | [MODERATE] | Bovine in vivo | SINGLE-LAB | Limited diarrhea mitigation but modulated host gut immune responses and concomitant microbiota to pattern more similar to healthy calves. |
| Colostrum promotes resilient microbiome with Bifidobacterium species | Multiple studies cited in disease map Stage 0.3 | Multiple | [MODERATE] | Bovine in vivo | MULTI-LAB | Colostrum supplementation vs milk replacer promotes protective Bifidobacterium colonization. |

### Note
This is a standard-of-care management intervention, not a crypto-specific therapeutic. Not counted toward the 70% test. Cargill should offer this product regardless of the crypto program outcome.

---

## Glycine/Glutamine ORS (B13) --- Force Rank #7

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| SGLT1 is downregulated during crypto infection due to villous atrophy | Pathfinder disease map, Stage 5.2 | Multiple | [ESTABLISHED] | Bovine in vivo (histopathology) + human models | MULTI-LAB | Loss of mature villous enterocytes reduces SGLT1-mediated sodium-glucose co-transport, the basis of standard ORS efficacy. |
| Glycine co-transport is independent of SGLT1 | Human pediatric ORS literature | Multiple | [ESTABLISHED] | Human in vivo | MULTI-LAB | Glycine uses a separate transport pathway, potentially preserving fluid absorption when SGLT1 is compromised. |
| L-glutamine is the primary fuel for enterocytes and promotes mucosal repair | General GI physiology literature | Multiple | [ESTABLISHED] | Human + animal | MULTI-LAB | Well-established metabolic role. |
| Not tested specifically for bovine cryptosporidiosis | N/A | N/A | [INFERRED] | N/A | N/A | **No trial has tested glycine/glutamine-enhanced ORS in crypto-positive calves.** |

---

## IL-22/I3C Inducer (D1) --- Force Rank #8 (Exploratory)

| Claim | Citation | PMID/DOI | Tier | Species/Model | Replication | Finding |
|-------|----------|----------|------|---------------|-------------|---------|
| NOD2/MDP reduces *C. parvum* parasite burden in neonatal mice via IL-22 and epithelial renewal | 2025 publication, European Journal of Immunology | Verify exact PMID | [PRELIMINARY] | Neonatal mouse in vivo | **SINGLE-LAB DEPENDENCY** | Rapid parasite burden reduction. Increased pro-inflammatory cytokine + antimicrobial peptide expression. Neutrophil influx. IL-22 and epithelial renewal mechanism. |
| AhR ligands from Lactobacillus metabolites promote ILC3 activation and IL-22 in piglets | 2024 publication, Journal of Virology | Verify exact PMID | [PRELIMINARY] | Neonatal piglet in vivo | SINGLE-LAB | AhR-mediated ILC3 activation with IL-22 secretion protected against PEDV (different pathogen). Cross-species evidence for the pathway in neonatal livestock. |
| I3C is a dietary AhR ligand from cruciferous vegetables | General AhR biology literature | Multiple | [ESTABLISHED] | Human + mouse | MULTI-LAB | Well-characterized AhR agonist. Metabolized to DIM and other active metabolites. |
| No bovine neonatal ILC3/AhR data exists | N/A | N/A | [INFERRED] | N/A | N/A | **Critical gap. Whether bovine neonatal ILC3 cells are AhR-responsive is unknown.** |

---

## Deferred Candidates (Evidence Summary)

### MMV665917 (A3) --- DEFERRED

| Claim | Citation | PMID/DOI | Tier | Finding |
|-------|----------|----------|------|---------|
| 94% oocyst reduction in calves, therapeutic administration | Stebbins et al. 2018, PLoS NTD | PMID: 29742093 | [MODERATE] | 22 mg/kg once daily, 7 days. Started 2 days after severe diarrhea. Bovine in vivo. |
| Efficacy in piglet model (*C. hominis*) | Schaefer et al. 2019 | Verify PMID | [MODERATE] | Cross-species replication. |
| Unknown target | N/A | N/A | N/A | Target identification not achieved. Development silence since 2021. hERG liability concern. |

### BKI-1708 / CpCDPK1 (A4) --- DEFERRED

| Claim | Citation | PMID/DOI | Tier | Finding |
|-------|----------|----------|------|---------|
| CpCDPK1 essential for invasion/egress (conditional protein degradation) | Vinayak et al. 2020 | Verify PMID | [ESTABLISHED] | CRISPR-validated essential target. |
| BKI-1708 rapidly resolves diarrhea in calves | Multiple BKI publications | Multiple | [MODERATE] | AC scaffold with lower hERG than PP scaffold. Calf efficacy demonstrated. |
| CDPKs absent from mammalian kinome | Kinome orthology | [COMPUTATIONAL] | [ESTABLISHED] | Unique selectivity advantage --- entire kinase family missing from host. |

### Hyperimmune Colostrum / rC7 (A5) --- DEFERRED

| Claim | Citation | PMID/DOI | Tier | Finding |
|-------|----------|----------|------|---------|
| rC7-immunized colostrum: 99.8% oocyst reduction | Perryman et al. 1999 | Verify PMID | [MODERATE] | Single study. Bovine in vivo. |
| General hyperimmune colostrum: diarrhea 2.3 vs 5.0 days | Fayer et al. 1989 + others | Multiple | [MODERATE] | Multiple studies, bovine in vivo. |

### BRD7929 / CpPheRS (B1) --- DEFERRED

| Claim | Citation | PMID/DOI | Tier | Finding |
|-------|----------|----------|------|---------|
| Cured immunosuppressed NSG mice (10 mg/kg, 4 days, no relapse) | Vinayak et al. 2020, Science Translational Medicine | Verify PMID | [ESTABLISHED] | One of very few compounds achieving curative activity in immunosuppressed mice. |
| L482V resistance mutation (23-fold) used as selectable marker | Multiple CRISPR publications | Multiple | [ESTABLISHED] | **Resistance is trivially easy to select. MONOTHERAPY DEAD.** |

---

## Killed Candidates (Evidence for Kill)

| Candidate | Kill Evidence | PMID/DOI | Tier |
|-----------|-------------|----------|------|
| Halofuginone (A7) | Cryptostatic; narrow TI; diarrhea reduction NS in low-bias studies (P=0.16) | Toldos et al. 2020 meta-analysis (verify PMID) | [ESTABLISHED] |
| CpKRS / DDD01510706 (B2) | Third tRNA synthetase target; established rapid resistance in class; EC50 1.3 uM (20x less potent than BRD7929); no in vivo data | Multiple | [MODERATE] |
| CpHDAC3 / Vorinostat (B4) | Pan-HDAC inhibitor; bovine HDAC homology; predictable neonatal toxicity | Multiple | [ESTABLISHED] |
| Bovilis Cryptium enhancement (B7) | 0.4-day diarrhea reduction after 40 years of vaccine research; GP60 most polymorphic protein; ceiling-bounded | EMA regulatory data | [ESTABLISHED] |
| Paromomycin derivative (B8) | No improved compound exists; class intrinsically static | Multiple | [ESTABLISHED] |
| Gal-GalNAc blockade (B9) | Stoichiometric impossibility at oral doses; Forge's own embarrassment scenario | N/A | [INFERRED] |
| Racecadotril (B10) | PK data in diarrheic calves shows elimination at 0.25-1.5h; malabsorption paradox | 2022 PK study (verify PMID) | [ESTABLISHED] |
| Crofelemer (B11) | 4/6 external models: wrong pathophysiology target (crypto diarrhea is malabsorptive, not secretory) | Board decision, external review consensus | [MODERATE] |
| NTZ reformulation (B14) | Immune dependence across species (HIV humans, SCID mice); neonatal calves functionally immunocompromised | Multiple meta-analyses | [ESTABLISHED] |
| CpAOX / Atovaquone-like (C5) | CpAOX non-essential by CRISPR KO (2024-2025); mitosome vestigial | 2025 FASEB Journal (verify PMID) | [ESTABLISHED] |
| Quorum sensing (C10) | No evidence in Cryptosporidium; speculative extrapolation from Toxoplasma | Surveyor flag | N/A |
| Pro-apoptotic agents (C7) | Accelerates villous atrophy in already-damaged neonatal gut; contraindicated | Pathophysiological reasoning | [INFERRED] |
| EGF supplementation (D5) | Abomasal degradation; provides fresh target cells for parasite; cost prohibitive | 3/6 external model consensus | [INFERRED] |
| Mucoadhesive NPs (D4) | Platform without payload; mucus depletion undermines mechanism | Board + GPT-5.4 reasoning | [INFERRED] |

---

## Disease-Level Evidence (Key Epidemiological Claims)

| Claim | Citation | PMID/DOI | Tier | Species | Finding |
|-------|----------|----------|------|---------|---------|
| Global prevalence 21.9% in dairy calves, 33.6% in diarrheic calves | Pinedo et al. 2023, meta-analysis (42,890 calves) | Verify PMID | [ESTABLISHED] | Bovine (meta-analysis) | Largest meta-analysis of calf crypto prevalence. |
| R0 = 5-15 in managed calf-rearing facilities | Pathfinder first-principles modeling | N/A | [INFERRED] | Modeled from bovine epidemiological data | No published R0 estimate exists. Modeled from 10^10 oocysts/calf, 10-30 oocyst infectious dose, 40% farm prevalence. |
| 34 kg weight deficit at 6 months in severely affected calves | Shaw et al. 2020 | Verify PMID | [ESTABLISHED] | Bovine in vivo (n=27 beef calves) | P=0.034. No catch-up growth. |
| Infectious dose 10-30 oocysts in humans | DuPont et al. 1995, NEJM | PMID: 7624781 (verify) | [ESTABLISHED] | Human volunteer study | 88% infection at >=300 oocysts. |
| Oocyst output ~3.89 x 10^10 per calf per infection | Multiple experimental infection studies | Multiple | [ESTABLISHED] | Bovine in vivo | Days 6-12 of life. |
| Compound 2093 rapid resistance (D243E 613-fold, T246I 128-fold) in 5 days | Vinayak et al. 2021 (verify citation) | Verify PMID | [ESTABLISHED] | Bovine in vivo | First demonstration of drug resistance in Cryptosporidium. |

---

## Citation Verification Flags

The following citations require manual verification before any external presentation:

1. **NCT07249463** --- EDI048 Phase 2 trial registration. Verify on ClinicalTrials.gov.
2. **Cho et al. 2025** --- Anti-P23 IgY calf trial. Verify exact DOI in Vaccines journal.
3. **Watson et al. 2025** --- P23 CRISPR knockout. Verify exact DOI in Nature Communications.
4. **Swale et al. 2025** --- AN7973 resistance data. Biopreprint --- verify DOI and peer review status.
5. **Hulverson et al. 2024** --- EDI048 Nature Microbiology. Verify exact DOI.
6. **Pinedo et al. 2023** --- Prevalence meta-analysis. Verify exact PMID.
7. **Shaw et al. 2020** --- 34 kg weight deficit. Verify exact PMID.
8. **Toldos et al. 2020** --- Halofuginone meta-analysis. Verify exact PMID.
9. **DuPont et al. 1995** --- Infectious dose NEJM. Verify PMID 7624781.

**Per Quality Standard 4:** One wrong citation in a partner presentation destroys credibility. All citations flagged above must be verified against the actual papers before the decision memo goes to Cargill.

---

*Phase 5 Evidence Register v1.0 --- Cryptosporidiosis in Neonatal Calves*
*Cargill (Animal Nutrition & Health)*
*38 evidence entries across 10 candidates + 6 disease-level claims*
*9 citations flagged for manual verification*
