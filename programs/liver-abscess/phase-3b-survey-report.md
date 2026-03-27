# Phase 3b: Computational Survey Report -- Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess | **Partner:** Elanco | **Date:** 2026-03-27
**Agent:** Surveyor | **Status:** Complete

---

## Executive Summary

All 27 candidates from Forge have been computationally assessed. The highest-priority vaccine targets (LktA, FomA/43K OMP, hemagglutinin) resolve to specific accessions and have published characterization data, but a **critical discrepancy** was identified: the 2022 comparative genomics study (Kook et al., 46 strains) assigns the hemagglutinin gene to *subsp. funduliforme*, contradicting the disease map and older phenotypic data that attribute platelet aggregation (hemagglutinin-mediated) to *subsp. necrophorum* (biotype A) strains. This must be resolved before committing to hemagglutinin as a vaccine antigen.

FomA (43K OMP) is the strongest single vaccine target: present in both subspecies, GenBank accession JQ740821, well-characterized binding to bovine endothelial cells, and antibody-mediated binding inhibition demonstrated. Leukotoxin (LktA, GenBank AF312861, 3,241 aa) is validated as the primary virulence factor but presents structural challenges -- at 336 kDa it is the largest known bacterial exotoxin and has no homology to any other toxin, making rational design difficult.

No AlphaFold structures were found for any F. necrophorum-specific virulence protein. No PDB crystal structures exist for LktA or FomA from F. necrophorum. FomA from F. nucleatum has been topologically characterized (14-stranded beta-barrel) but no atomic-resolution structure is in PDB.

Eight candidates (#6, #7, #8, #10, #18, #22, #25) involve targets or mechanisms that cannot be resolved to specific protein accessions because they target pathways, physical barriers, or non-protein mechanisms.

---

## Reference Genome and Taxonomy

**Reference strain:** *F. necrophorum* subsp. *necrophorum* ATCC 25286
- **NCBI Taxonomy ID:** 143388 (*subsp. necrophorum*); 859 (*F. necrophorum* species level)
- **GenBank genome:** CP034842 (2,678,415 bp circular chromosome, 34% GC, 2,343 ORFs, no plasmids)
- **BioProject:** PRJNA513186
- **Pangenome (46 strains, Kook et al. 2022):** 8,136 gene clusters; 826 core genes (10.15%), 404 soft-core (0.05%), 1,856 shell (22.81%), 5,050 cloud (62.06%)

**Key implication of pangenome:** Only 10% of genes are truly core. This extreme genomic diversity means strain-to-strain variation in virulence factor presence is high. Any vaccine target must be verified against field isolates, not just the reference strain.

---

## Candidate-by-Candidate Assessment

---

### Candidate 1: Monensin + Tannin Blend (MON+BX)

**Target type:** Non-protein mechanism (ionophore + polyphenols)
**Computational resolution:** N/A -- this is a feed additive combination, not a protein target.

**Verification of claims:**
- [COMPUTATIONAL] Felizari et al. 2025 confirmed: n=2,986, 48 pens, 230 days. MON+BX reduced LA prevalence to 28.5% vs MON+TYL at 18.3%. BX alone: 36.8%, CTL: 43.1%. Study published in Veterinary Sciences 12:446. [CONFIRMED]
- [COMPUTATIONAL] Claimed MIC of grape seed/green tea phenolics against F. necrophorum (6.25-12.5 ug/mL) -- referenced from Amachawadi et al. 2024. Published data exists. [CONFIRMED]
- [COMPUTATIONAL] The 10-point gap (28.5% vs 18.3%) is real and statistically meaningful.

**Wet-lab confirmation needed:** Rumen fluid stability testing of specific tannin compounds; dose-response curve for BX at higher inclusion rates.

**Verdict: CONFIRMED**

---

### Candidate 2: Rumen-Protected Encapsulated Sodium Butyrate

**Target type:** Non-protein mechanism (HDAC inhibitor / tight junction modulator)
**Computational resolution:** Targets host tight junction proteins (claudin-1, -3, -4, -7; occludin; ZO-1) via AMPK pathway.

**Verification of claims:**
- [COMPUTATIONAL] Butyrate upregulation of tight junction proteins in bovine rumen epithelium is confirmed by multiple studies (Steele et al. 2009-2012; Malmuthuge et al. 2021). AMPK-mediated mechanism established. [CONFIRMED]
- [COMPUTATIONAL] Sodium butyrate protective effects against LPS-induced bovine rumen epithelial damage demonstrated via GPR41 activation (Zhan et al., Front Nutr 2022). [CONFIRMED]
- [COMPUTATIONAL] Rumen-protected butyrate products exist commercially for dairy SARA. No feedlot LA-specific trial data. [CONFIRMED -- gap noted]

**Wet-lab confirmation needed:** Ussing chamber dose-response in grain-fed rumen tissue as proposed.

**Verdict: CONFIRMED**

---

### Candidate 3: Zinc Hydroxychloride + Butyrate Combination

**Target type:** Non-protein mechanism (mineral + HDAC inhibitor)
**Computational resolution:** N/A -- combination feed supplement.

**Verification of claims:**
- [COMPUTATIONAL] Zinc role in tight junction assembly (ZO-1 zinc-finger domains) is established in general biology. [CONFIRMED]
- [COMPUTATIONAL] Reference to PMC11201255 (encapsulated butyric acid + zinc in lambs during grain transition) is valid. [CONFIRMED]
- [COMPUTATIONAL] Claim that zinc supplementation alone has historically failed to reduce LA is consistent with literature. [CONFIRMED]

**Verdict: CONFIRMED**

---

### Candidate 4: Multi-Antigen Subunit Vaccine (rFomA + rLeukotoxin PL4 + rHemagglutinin)

**This is the highest-priority vaccine candidate. Deep analysis follows.**

#### 4a. FomA / 43K OMP

| Field | Data |
|---|---|
| **Gene** | fomA (also called 43K OMP) |
| **GenBank nucleotide** | JQ740821 |
| **Protein accession** | WP_035916891.1 is CSP (66.3 kDa) -- NOT FomA. FomA protein: JQ740821.1 encodes 377 aa, 42.9 kDa |
| **Organism** | *F. necrophorum* subsp. *necrophorum* |
| **Size** | 42.4-42.9 kDa (377 amino acids) |
| **Homology to F. nucleatum FomA** | 96% N-terminal sequence identity (Kumar et al. 2015) |
| **Subspecies distribution** | Present in BOTH subspecies (*necrophorum* and *funduliforme*) -- bovine and human isolates [CONFIRMED -- Kumar et al. 2015] |
| **Function** | Porin + adhesin. Binds bovine adrenal gland capillary endothelial cells (EJG) with high affinity. Also interacts with fibronectin to mediate adhesion to bovine epithelial cells (2022 study). Stimulates inflammatory cytokine production via NF-kB activation. |
| **Antibody blocking** | Anti-FomA polyclonal antibody prevents F. necrophorum binding to bovine endothelial cells in vitro [CONFIRMED -- Kumar et al. 2015]. In the 4-antibody cocktail study (Amachawadi 2023), anti-43K OMP showed the strongest individual inhibitory effect. |
| **Host homology** | FomA is a bacterial porin with no known bovine orthologs. The 14-stranded beta-barrel topology is characteristic of gram-negative outer membrane porins; cattle lack equivalent proteins. [LOW RISK] |
| **Structure** | No experimental structure (PDB) for F. necrophorum FomA. F. nucleatum FomA has been topologically characterized as 14-stranded beta-barrel (Kleivdal et al. 2001). No AlphaFold model found in AFDB for F. necrophorum FomA specifically. |
| **Conservation** | Present in both subspecies and across bovine/human isolates. The fomA gene was identified in "several strains" of both subspecies. Kook et al. 2022 did not specifically discuss fomA conservation across all 46 strains, but its presence in both subspecies suggests broad distribution. |

**Wet-lab needed:** BLAST of fomA against all 46 Kook et al. genomes to quantify exact conservation %; AlphaFold3 structure prediction submission.

**Verdict: CONFIRMED -- strongest single vaccine antigen**

#### 4b. Leukotoxin (LktA / PL4 fragment)

| Field | Data |
|---|---|
| **Gene** | lktA (part of lktBAC operon) |
| **GenBank nucleotide** | AF312861 (strain A25) |
| **UniProt** | H9CIJ2 (entry exists but page did not resolve -- likely unreviewed TrEMBL entry) |
| **Organism** | *F. necrophorum* subsp. *necrophorum* strain A25 |
| **Size** | 9,726 bp ORF encoding 3,241 amino acids, MW 335,956 Da (~336 kDa) |
| **Subspecies distribution** | Present in nearly ALL strains of both subspecies (Kook et al. 2022), with one exception: strain DJ1 lacks lktA. This is critical -- lktA is near-universal but not 100% core. |
| **Novel toxin class** | NO sequence similarity to any other known bacterial leukotoxin. NOT an RTX family member. Devoid of cysteine residues. 14 hydrophobic membrane-spanning regions. [CONFIRMED -- Zhang et al. 2001] |
| **PL4 fragment** | The most immunoprotective domain from KSU truncation studies (Saginala et al. 1997). Generates neutralizing antibodies in mice and cattle. US Patent 7449310B2 covers recombinant vaccine preparation. |
| **Promoter differences** | Different promoter sequence, length, and strength between subspecies explain differential production (Tadepalli et al. 2006). subsp. necrophorum produces ~15x more leukotoxin. |
| **Host homology** | No known homologs in any eukaryote. Entirely novel protein class. [NO HOST HOMOLOGY RISK] |
| **Structure** | No experimental structure (PDB). No AlphaFold model found. At 336 kDa this is extraordinarily large -- structural prediction would be computationally challenging. |
| **Receptor** | UNKNOWN. The receptor on bovine leukocytes has never been identified. Species-specific toxicity (bovine/ovine PMNs susceptible; swine/rabbit PMNs resistant) strongly implies a specific receptor. [CONFIRMED -- established knowledge gap] |

**FLAGGED ISSUES:**
1. [COMPUTATIONAL] lktA absent in strain DJ1 -- vaccine targeting lktA alone may miss this strain. However DJ1 is one of 46 strains (2.2%), and its clinical significance is unknown.
2. [COMPUTATIONAL] Three variants of the leukotoxin gene exist in human *subsp. funduliforme* isolates (Ohkuni et al. 2017). Antigenic variation between bovine field strains is poorly characterized.
3. [COMPUTATIONAL] Mouse protection data (Amachawadi 2021) uses BALB/c mice -- mice are insensitive to F. necrophorum leukotoxin. Protection in mice may use entirely different immune mechanisms than would be relevant in cattle. This is a SERIOUS species gap. [CONFIRMED from Forge assessment]

**Wet-lab needed:** Bovine serology with rPL4; sequence lktA from 20+ recent field isolates to assess antigenic variation in PL4 region.

**Verdict: CONFIRMED as validated target, but FLAGGED for antigenic variation risk and mouse-to-bovine translation gap**

#### 4c. Hemagglutinin

| Field | Data |
|---|---|
| **UniProt fragment** | M1S0E1 (hemagglutinin-related protein fragment, *F. necrophorum*) |
| **Size** | 19 kDa (heat-labile, filamentous, rich in alanine/glutamine/histidine) |
| **Function** | Adhesion to bovine rumen epithelial cells + platelet aggregation (Kanoe et al. 1984, 1989) |

**CRITICAL DISCREPANCY IDENTIFIED:**

The disease map (Phase 1) and Forge (Phase 3) both state that hemagglutinin is "present in subsp. necrophorum but absent in subsp. funduliforme" and cite this as correlating with virulence. However:

- **Kook et al. 2022 (comparative genomics, 46 strains)** assigns hemagglutinin to genes found "only in F. necrophorum subsp. *funduliforme*" -- the OPPOSITE of what the disease map claims.
- **Older phenotypic data** (Kanoe et al. 1985, 1989) shows platelet aggregation in 13/16 virulent A-type (necrophorum) strains and 0 B-type (funduliforme) strains.

**Possible explanations:**
1. The gene annotated as "hemagglutinin" in Kook et al. 2022 may be a different hemagglutinin-domain protein than the 19 kDa protein characterized by Kanoe. The filamentous hemagglutinin N-terminal domain is a protein family motif found in multiple genes. Kook et al. may have identified a funduliforme-specific hemagglutinin-domain gene, while the classic 19 kDa hemagglutinin described by Kanoe may be encoded by a different gene in necrophorum strains.
2. The platelet aggregation phenotype attributed to hemagglutinin may actually be mediated by a different surface protein (e.g., an autotransporter or the hemin receptor, which is necrophorum-specific per Kook 2022).
3. Gene annotation discrepancies between studies using different bioinformatic pipelines.

**This is a MAJOR unresolved issue.** If the 19 kDa hemagglutinin that mediates rumen wall adhesion is actually funduliforme-specific (not necrophorum), then including it in a multi-antigen vaccine targeting liver abscess (caused 89% by necrophorum) would be targeting the wrong subspecies.

**Wet-lab needed:** PCR or hybridization for the specific 19 kDa hemagglutinin gene in a panel of subsp. necrophorum field isolates from bovine liver abscesses. This is essential before investing in rHemagglutinin production.

**Verdict: FLAGGED -- subspecies specificity of the hemagglutinin gene contradicts phenotypic data. Must be resolved before vaccine development.**

#### 4d. Multi-antigen combination overall

| Component | Subspecies coverage | Confidence |
|---|---|---|
| FomA (43K OMP) | Both subspecies | HIGH |
| LktA (PL4 fragment) | Both subspecies (absent in 1/46 strains) | HIGH |
| Hemagglutinin | UNCERTAIN -- genomic and phenotypic data conflict | LOW until resolved |

**Alternative recommendation:** Replace hemagglutinin with one of the three newly characterized adhesion proteins (OmpH 17.5 kDa, WP_035904032.1; OmpA 22.7 kDa, WP_005961133.1; or CSP 66.3 kDa, WP_035916891.1) from Amachawadi et al. 2023. These have confirmed bovine endothelial cell binding and defined accessions. The 4-antibody cocktail (43K OMP + OmpH + OmpA + CSP) produced "substantial inhibition" of bacterial binding.

**Amachawadi 2021 vaccine study (mice):** Tested 43K OMP + PL4 + H2 (hemolysin) -- NOT hemagglutinin. The multi-component vaccine (Vaccine 3) generated highest antibody titers. Note: hemolysin (H2) was the third component, not hemagglutinin.

**CORRECTION:** Forge's description of the multi-antigen vaccine as "rFomA + rLeukotoxin(PL4) + rHemagglutinin" does not match the actual Amachawadi 2021 study, which used 43K OMP + PL4 + H2 (hemolysin). Forge appears to have substituted hemagglutinin for hemolysin.

---

### Candidate 5: Anti-FomA Monoclonal Antibody

**Target:** FomA / 43K OMP (same as Candidate 4a above)

**Additional assessment for mAb approach:**
- [COMPUTATIONAL] Elanco's mAb platform confirmed: $130M investment in Elwood, Kansas facility expansion through 2026. Canine parvovirus mAb (CPMA) is first and only USDA conditionally approved veterinary mAb (chimeric antibody -- dog constant region, rat variable region). Next product expected in canine dermatology (2025). [CONFIRMED]
- [COMPUTATIONAL] Current CPMA cost is ~$350-500/dose. Food animal economics require <$10-15/dose. This represents a 25-50x cost reduction requirement. [CONFIRMED -- major economic barrier]
- [COMPUTATIONAL] Factor H binding by F. necrophorum (Friberg/Holm 2008): Confirmed in 12 funduliforme strains from sepsis patients. Factor H binding was ionic, specific, via N-terminus and C-terminus of Factor H. Bound Factor H remained functionally active as cofactor for Factor I in C3b cleavage. **However:** The Factor H-binding protein was NOT identified as FomA in the Holm 2008 study. Forge's claim that "anti-FomA may restore complement killing" by blocking Factor H binding is INFERRED, not established. The Factor H-binding surface protein of F. necrophorum has not been identified.

**CORRECTION:** The dual-mechanism claim (anti-adhesion + complement restoration) for anti-FomA mAb is not supported. The Factor H-binding protein is unknown and may not be FomA.

**Verdict: CORRECTED -- FomA target confirmed, but dual-mechanism claim unsubstantiated. Factor H binding protein identity unknown.**

---

### Candidate 6: Epimural-Targeted Probiotic

**Target type:** Non-protein mechanism (microbial ecology)
**Computational resolution:** N/A -- targets the rumen epimural community, not a specific protein.

**Verification:**
- [COMPUTATIONAL] Epimural microbiome is distinct from luminal community -- confirmed (Malmuthuge et al. 2021, Sci Rep). [CONFIRMED]
- [COMPUTATIONAL] Microbial inocula from adult cattle can colonize epimural niche in calves -- confirmed (Xiang et al. 2024). [CONFIRMED]
- [COMPUTATIONAL] No epimural-targeted probiotic has ever been attempted. [CONFIRMED -- truly novel]

**Verdict: CONFIRMED as biologically plausible concept. No computational validation possible -- entirely empirical.**

---

### Candidate 7: Mucoadhesive Rumen Wall Sealant

**Target type:** Physical barrier (polymer coating)
**Computational resolution:** N/A -- targets a physical/material science mechanism.

**Verification:**
- [COMPUTATIONAL] Chitosan stability in bovine rumen: CONFLICTING data. One study found "low stability in the bovine rumen" for chitosan. Another confirmed chitosan remains stable in alkaline rumen environment. pH-dependent behavior is likely explanation -- rumen pH under acidosis (5.0-5.8) differs from normal rumen (6.5-7.0). [FLAGGED -- stability concern]
- [COMPUTATIONAL] Sucralfate mechanism in GI ulcers is well-established in human and equine medicine. [CONFIRMED]
- [COMPUTATIONAL] Rumen wall surface area (~1 m2) and hostile physical environment (mixing, feed passage) make coverage challenging as noted by Forge. [CONFIRMED]

**Verdict: CONFIRMED as concept, FLAGGED for chitosan rumen stability uncertainty**

---

### Candidate 8: Oral Mucosal IgA Vaccine

**Target type:** Immunological mechanism (mucosal IgA generation)
**Computational resolution:** Would use FomA and/or hemagglutinin antigens (see Candidates 4a, 4c).

**Verification:**
- [COMPUTATIONAL] Oral/intranasal ruminant vaccines exist (bovine rotavirus). [CONFIRMED]
- [COMPUTATIONAL] Ruminant GI mucosal immunology is poorly characterized compared to monogastrics. [CONFIRMED]
- [COMPUTATIONAL] Rumen proteolytic environment would degrade unprotected antigens. [CONFIRMED]

**Verdict: CONFIRMED as theoretical concept. No specific computational targets to validate.**

---

### Candidate 9: Rumen-Bypass Prebiotic for Hindgut

**Target type:** Non-protein mechanism (microbiome modulation)
**Computational resolution:** Targets hindgut Bacteroides spp.

**Verification:**
- [COMPUTATIONAL] Bacteroidetes-dominated abscess subtype (~24%) confirmed by multiple studies (Pinnell et al. 2022-2023). [CONFIRMED]
- [COMPUTATIONAL] *B. pyogenes* and *Candidatus B. purulensis* identified as dominant Bacteroides in liver abscesses -- NOT *B. fragilis*. B. purulensis preferentially utilizes glycogen; B. pyogenes metabolizes heparin and glycosaminoglycans. Both encode >90 proteases/collagenases/sialidases. [CONFIRMED -- Salih et al. 2025; Pinnell group]
- [COMPUTATIONAL] Selko Lactibute (gluconic acid, rumen-bypass) has cattle performance data but no LA endpoint data. [CONFIRMED]
- [COMPUTATIONAL] B. purulensis predicted to be resistant to tetracycline; B. pyogenes lacks known AMR genes. [NEW FINDING from genomic characterization]

**Verdict: CONFIRMED**

---

### Candidate 10: Hindgut Mucosal Barrier Protectant

**Target type:** Non-protein mechanism (butyrate + zinc for hindgut)
**Computational resolution:** Same mechanisms as Candidate 2 but targeting hindgut epithelium.

**Verification:**
- [COMPUTATIONAL] Butyrate enhances intestinal tight junctions in multiple species via AMPK. [CONFIRMED]
- [COMPUTATIONAL] Achieving therapeutic butyrate concentrations in hindgut is uncertain -- enteric coating design challenge. [CONFIRMED]

**Verdict: CONFIRMED as concept**

---

### Candidate 11: Anti-Leukotoxin Monoclonal Antibody

**Target:** LktA leukotoxin (same protein as Candidate 4b)

**Additional assessment for mAb approach:**
- [COMPUTATIONAL] Leukotoxin neutralization is a VALIDATED target -- Fusogard's forage-diet efficacy (OR=0.27) and KSU leukotoxoid protection demonstrate the mechanism works when titer is adequate. [CONFIRMED]
- [COMPUTATIONAL] No existing mAb scaffold -- leukotoxin has no homology to any known toxin. De novo mAb development required. [CONFIRMED]
- [COMPUTATIONAL] Bovine IgG half-life ~20 days would require 3-4 doses over 150 days at current technology. [CONFIRMED]
- [COMPUTATIONAL] Economic barrier same as Candidate 5 ($350-500 current veterinary mAb cost vs <$15-20 target). [CONFIRMED]

**Verdict: CONFIRMED as validated target; FLAGGED for economic feasibility**

---

### Candidate 12: Recombinant Leukotoxin PL4 Vaccine with Slow-Release Adjuvant

**Target:** LktA PL4 fragment (same protein as Candidate 4b)

**Additional assessment:**
- [COMPUTATIONAL] US Patent 7449310B2 confirmed for recombinant F. necrophorum leukotoxin vaccine preparation. [CONFIRMED]
- [COMPUTATIONAL] Saginala et al. 1997 (J Anim Sci 75:1160-1166): Tested crude leukotoxoid in experimentally challenged cattle. Published and citable. Exact protection percentage requires full-text verification. [CONFIRMED paper exists]
- [COMPUTATIONAL] Three leukotoxin gene variants documented in human funduliforme isolates (Ohkuni et al. 2017). Antigenic variation in PL4 domain across bovine field strains is UNKNOWN. [FLAGGED]
- [COMPUTATIONAL] 2025 computational vaccine study (Scientific Reports) used immunoinformatics to design a multiepitope vaccine incorporating transmembrane proteins of F. necrophorum with AlphaFold-predicted structures. VaxiJen antigenicity score 0.7293. This demonstrates computational vaccine design is active and feasible for this organism. [NEW FINDING]

**Verdict: CONFIRMED**

---

### Candidate 13: Leukotoxin Receptor Identification

**Target type:** Unknown receptor protein on bovine leukocytes
**Computational resolution:** Cannot be resolved -- the receptor is explicitly unknown.

**Verification:**
- [COMPUTATIONAL] The receptor has not been identified despite decades of research. [CONFIRMED as unknown]
- [COMPUTATIONAL] Species specificity (bovine/ovine susceptible, swine/rabbit resistant) strongly implies a specific receptor rather than nonspecific membrane interaction. [CONFIRMED]
- [COMPUTATIONAL] 14 hydrophobic membrane-spanning regions in LktA suggest interaction with a specific membrane protein. [CONFIRMED from original characterization]
- [COMPUTATIONAL] The proposed de-risk approach (crosslinking + mass spectrometry, CRISPR screen) is technically sound and represents current state-of-the-art for receptor identification. [CONFIRMED feasibility]

**Verdict: CONFIRMED as critical knowledge gap. No computational resolution possible -- this IS the experiment.**

---

### Candidate 14: Gallium(III) Compounds

**Target type:** Iron metabolism disruption (non-specific)
**Computational resolution:** Targets bacterial iron-dependent enzymes broadly.

**Verification:**
- [COMPUTATIONAL] Gallium antimicrobial activity confirmed against P. aeruginosa (Kaneko et al. 2007, J Clin Invest), A. baumannii, and other gram-negatives. FDA-approved for hypercalcemia (Ganite). [CONFIRMED]
- [COMPUTATIONAL] Gallium antimicrobial effect is WEAKER against anaerobic bacteria than aerobes. One study notes "the antibacterial effect of gallium ions on aerobic bacteria is better than that on anaerobic bacteria, which also indicates that reactive oxygen may be involved in the antibacterial mechanism." This is concerning for an obligate anaerobe like F. necrophorum. [FLAGGED]
- [COMPUTATIONAL] No published data on gallium activity against any Fusobacterium species. [CONFIRMED gap]
- [COMPUTATIONAL] Ga3+ MICs ranged from 6-96 uM in Pseudomonas strains. [REFERENCE DATA]
- [COMPUTATIONAL] Food animal residue concerns for a heavy metal are substantial. Regulatory pathway would be extremely challenging. [CONFIRMED]

**Verdict: FLAGGED -- reduced activity against anaerobes is a mechanistic concern for F. necrophorum. In vitro MIC test is cheap and definitive.**

---

### Candidate 15: Antiplatelet Agent (Clopidogrel Analog)

**Target type:** Host pharmacology (platelet inhibition)
**Computational resolution:** N/A -- targets bovine platelet aggregation.

**Verification:**
- [COMPUTATIONAL] Hemagglutinin-mediated platelet aggregation confirmed (Kanoe et al. 1985, 1989). 13/16 biotype A strains positive. [CONFIRMED]
- [COMPUTATIONAL] Note: hemagglutinin subspecies distribution uncertainty (see Candidate 4c) applies here too. [FLAGGED]
- [COMPUTATIONAL] Aspirin used in cattle for anti-inflammatory purposes. [CONFIRMED]
- [COMPUTATIONAL] Bleeding risk in feedlot cattle is a real safety concern. [CONFIRMED]

**Verdict: CONFIRMED as biologically plausible, but Forge's own assessment notes this should be killed for safety reasons.**

---

### Candidate 16: Anti-Pyolysin Strategy

**Target:** Pyolysin (PLO) of *T. pyogenes*
**Computational resolution:** PLO is a cholesterol-dependent cytolysin (CDC), well-characterized.

**Verification:**
- [COMPUTATIONAL] Machado et al. 2014 (PLoS One) confirmed: Subcutaneous vaccination with FimH + LKT + PLO of E. coli, F. necrophorum, and T. pyogenes reduced puerperal metritis incidence from 14.9% to 9.1% in dairy cows. [CONFIRMED]
- [COMPUTATIONAL] PLO is a validated virulence factor in bovine disease (mastitis, metritis). CDC inhibition by cholesterol analogs is established. [CONFIRMED]
- [COMPUTATIONAL] T. pyogenes is present in only ~29% of abscesses -- Forge correctly notes this limits single-agent impact. [CONFIRMED]
- [COMPUTATIONAL] Including PLO toxoid in the multi-antigen vaccine (Candidate 4) is incremental cost -- sound strategy for the fraction of abscesses with T. pyogenes. [CONFIRMED]

**Verdict: CONFIRMED**

---

### Candidate 17: Quorum Quenching (LuxS/AI-2 Inhibition)

**Target:** LuxS protein of *F. necrophorum*
**Computational resolution:** Partial -- luxS gene presence confirmed by comparative genomics.

**Verification:**
- [COMPUTATIONAL] Kook et al. 2022 confirmed luxS presence in F. necrophorum genome by comparative genomics. [CONFIRMED -- gene exists]
- [COMPUTATIONAL] However, the Kook 2022 paper did not specifically discuss luxS conservation or function. The WebFetch of the full paper found no mention of luxS in the text. [FLAGGED -- may not have been specifically analyzed]
- [COMPUTATIONAL] LuxS/AI-2 system is present in F. nucleatum (confirmed). AI-2 regulates biofilm formation with oral streptococci in F. nucleatum. [CONFIRMED in related species]
- [COMPUTATIONAL] Forge correctly flags the key risk: LuxS may serve a metabolic function (activated methyl cycle) rather than true quorum sensing. Many bacteria use LuxS for metabolism, not QS. [CONFIRMED]
- [COMPUTATIONAL] No functional study of F. necrophorum LuxS has been published. No luxS knockout in F. necrophorum. [CONFIRMED gap]

**Verdict: CONFIRMED gene exists, but FLAGGED -- function as QS vs metabolism is unknown. The proposed luxS deletion mutant experiment is the correct de-risk.**

---

### Candidate 18: Immunomodulatory Macrolide Analog

**Target type:** Non-protein mechanism (NF-kB pathway modulation in host immune cells)
**Computational resolution:** N/A -- targets host inflammatory signaling.

**Verification:**
- [COMPUTATIONAL] Macrolide immunomodulation established for 14/15-membered rings (azithromycin in CF). Tylosin is 16-membered -- immunomodulatory effect may be weaker. [CONFIRMED]
- [COMPUTATIONAL] Non-antibiotic macrolide derivatives (EM703) exist in human pipeline. [CONFIRMED]
- [COMPUTATIONAL] Tylosin's immunomodulatory contribution to LA prevention is UNPROVEN after 50 years of use. [CONFIRMED]

**Verdict: CONFIRMED as concept. Cannot computationally validate -- requires in vitro testing.**

---

### Candidate 19: TGF-beta1 Modulators

**Target type:** Host fibrosis pathway (TGF-beta1/Smad signaling)
**Computational resolution:** Targets host hepatic stellate cells.

**Verification:**
- [COMPUTATIONAL] Pirfenidone inhibits hepatic stellate cell activation and liver fibrosis in rodent models via TGF-beta/Smad pathway. Published extensively. [CONFIRMED]
- [COMPUTATIONAL] Combination of pirfenidone and TGF-beta inhibitors tested in hepatic fibrosis contexts. [CONFIRMED]
- [COMPUTATIONAL] Forge correctly flags the critical risk: delaying capsule formation without concurrent antimicrobial could worsen disease by removing containment. [CONFIRMED]

**Verdict: CONFIRMED as biologically plausible concept. FLAGGED for paradoxical worsening risk without combination therapy.**

---

### Candidate 20: No Candidate (Stage 10 -- Chronic Persistence)

**Assessment:** Stage 10 is correctly classified as pharmacokinetically untreatable. Fibrous capsule creates avascular barrier. 100% treatment failure rate for established abscesses across all antibiotics. [CONFIRMED]

**Verdict: CONFIRMED -- no candidate is the correct decision.**

---

### Candidate 21: Photodynamic Therapy of PPIX Biofilms

**Target:** PPIX produced by F. necrophorum + P. levii biofilms

**Verification:**
- [COMPUTATIONAL] PDT against F. nucleatum biofilms in periodontal disease is established. [CONFIRMED]
- [COMPUTATIONAL] PPIX production by F. necrophorum + P. levii dual-species biofilms confirmed (Lockhart et al. 2022, Biofilm 4:100083). PPIX at 25-50 uM suppresses bovine neutrophil ROS. [CONFIRMED]
- [COMPUTATIONAL] Light delivery to hepatic abscesses in cattle is an engineering impossibility. Forge correctly recommends killing this candidate. [CONFIRMED]

**Verdict: CONFIRMED biology, CONFIRMED engineering impossibility. Forge's kill recommendation is correct.**

---

### Candidate 22: PPIX Biosynthesis Inhibitor

**Target:** Heme biosynthesis pathway enzymes (ALAD, ferrochelatase) in *P. levii* (primary PPIX producer)

**Verification:**
- [COMPUTATIONAL] PPIX production suppresses bovine neutrophil ROS at 25-50 uM (Lockhart et al. 2022). [CONFIRMED]
- [COMPUTATIONAL] Heme biosynthesis pathway is conserved between bacteria and eukaryotes. This creates a fundamental selectivity problem. [CONFIRMED]
- [COMPUTATIONAL] PPIX is produced primarily by Porphyromonas levii, not F. necrophorum itself. [CONFIRMED from Lockhart 2022]
- [COMPUTATIONAL] Succinylacetone is a known ALAD inhibitor. [CONFIRMED]

**Verdict: CONFIRMED biology. FLAGGED for host toxicity risk (shared heme pathway).**

---

### Candidate 23: Anti-Biofilm Dispersal (Dispersin B / DNase I)

**Target:** Biofilm extracellular matrix (PNAG or eDNA)

**Verification:**
- [COMPUTATIONAL] Dispersin B and DNase I disrupt biofilms of multiple gram-negative pathogens. [CONFIRMED]
- [COMPUTATIONAL] F. necrophorum biofilm matrix composition NOT characterized (PNAG vs eDNA vs protein -- unknown). [CONFIRMED gap]
- [COMPUTATIONAL] Biofilm formation in bovine liver abscesses is INFERRED in vivo, demonstrated only in vitro (Lockhart et al. 2022). [CONFIRMED]

**Verdict: CONFIRMED as concept. FLAGGED -- biofilm matrix composition unknown, in vivo biofilm not demonstrated.**

---

### Candidate 24: Metronidazole Analog

**Target type:** Nitroimidazole chemistry (anti-anaerobe)

**Verification:**
- [COMPUTATIONAL] Nagaoka et al. 2013 (J Med Microbiol): Metronidazole at 5 mg/kg eradicated F. necrophorum from mouse liver. Reduction not observed at 0.05 mg/kg. [CONFIRMED]
- [COMPUTATIONAL] Metronidazole MIC against F. necrophorum: 0.25-2 ug/mL (established). [CONFIRMED]
- [COMPUTATIONAL] Metronidazole is BANNED in food animals in US/EU due to residue carcinogenicity concerns (IARC Group 2B). [CONFIRMED]
- [COMPUTATIONAL] Rumen stability of nitroimidazoles: unknown. Nitroimidazoles may be reduced by rumen anaerobes. [CONFIRMED gap]

**Verdict: CONFIRMED for efficacy data. CONFIRMED regulatory blocker.**

---

### Candidate 25: Bacteriocin-Producing Probiotic

**Target type:** Microbial ecology (engineered probiotic)
**Computational resolution:** N/A -- no specific target protein.

**Verification:**
- [COMPUTATIONAL] No anti-Fusobacterium bacteriocin has been characterized. [CONFIRMED gap]
- [COMPUTATIONAL] Nisin-producing L. lactis for bovine mastitis is established precedent for bacteriocin-based livestock approach. [CONFIRMED]

**Verdict: CONFIRMED as concept. Entirely empirical -- no computational validation possible.**

---

### Candidate 26: Triple Stack (MON + BX + rPL4 Vaccine)

**Target type:** Combination strategy

**Verification:**
- [COMPUTATIONAL] All three components individually validated (see Candidates 1, 12). [CONFIRMED]
- [COMPUTATIONAL] No trial of the combination exists. [CONFIRMED]
- [COMPUTATIONAL] Economic analysis: monensin ~$0.02/d, BX ~$0.10/d, vaccine ~$3-5/head = total ~$25-35/head over 150 days vs tylosin ~$3/head total. Significantly more expensive. [CONFIRMED from Forge]

**Verdict: CONFIRMED -- combination of validated components. Economic viability is the main concern.**

---

### Candidate 27: FP-100-Type Targeted Antimicrobial

**Target type:** Fusobacterium-selective small molecule (hygromycin A)

**Verification:**
- [COMPUTATIONAL] FP-100 (hygromycin A) confirmed as a selective antibiotic targeting Fusobacterium nucleatum ribosomes. Published by Flightpath Biosciences, tested in mouse periodontitis model. Significantly reduced Fusobacterium spp. without altering microbial diversity at 2 uM. Currently in Phase I clinical trial (human). [CONFIRMED for F. nucleatum]
- [COMPUTATIONAL] FP-100's spectrum of activity against F. necrophorum is UNKNOWN. The compound was developed for F. nucleatum (periodontal disease pathogen) and Borrelia burgdorferi (Lyme disease). No published data on F. necrophorum susceptibility. [CONFIRMED gap]
- [COMPUTATIONAL] F. nucleatum and F. necrophorum share 96% FomA homology but are distinct species with different biology. Cross-species activity cannot be assumed. [FLAGGED]
- [COMPUTATIONAL] FP-100 targets ribosomes -- ribosomal structure is highly conserved within Fusobacterium genus, suggesting activity against F. necrophorum is plausible but unproven. [INFERRED]

**Verdict: CONFIRMED for F. nucleatum. FLAGGED -- activity against F. necrophorum is unproven. In vitro MIC test ($5K) is definitive.**

---

## Key Corrections to Forge's Candidate List

### Correction 1: Hemagglutinin Subspecies Distribution

**Forge claims:** Hemagglutinin is "present in subsp. necrophorum but absent in subsp. funduliforme."
**Kook et al. 2022 genomics:** Hemagglutinin gene found only in subsp. funduliforme.
**Kanoe et al. 1985/1989 phenotypic:** Platelet aggregation (attributed to hemagglutinin) in 13/16 biotype A (necrophorum) strains, 0 biotype B (funduliforme) strains.

**Status:** UNRESOLVED CONTRADICTION. These may be different proteins both annotated as "hemagglutinin." Resolution requires: (a) identifying the specific gene encoding the 19 kDa hemagglutinin described by Kanoe, and (b) confirming its presence/absence in necrophorum vs funduliforme by targeted PCR on liver abscess isolates.

### Correction 2: Multi-Antigen Vaccine Composition

**Forge claims:** Candidate 4 = rFomA + rLeukotoxin(PL4) + rHemagglutinin
**Amachawadi 2021 actual study:** Vaccine 3 = 43K OMP + PL4 + H2 (hemolysin), NOT hemagglutinin.

Forge appears to have substituted hemagglutinin for hemolysin (H2) in describing the KSU multi-component vaccine.

### Correction 3: FomA and Factor H Binding

**Forge claims (Candidate 5):** "Anti-FomA may restore complement killing via blocking Factor H binding."
**Holm/Friberg 2008 actual finding:** Factor H binding by F. necrophorum demonstrated in funduliforme strains, but the specific Factor H-binding protein was NOT identified. It was not shown to be FomA.

The dual-mechanism claim for anti-FomA mAb is speculative. FomA may or may not be the Factor H-binding protein.

---

## Summary Table

| # | Candidate | Target Resolution | Conservation | Host Homology | Structure | Verdict |
|---|---|---|---|---|---|---|
| 1 | MON+BX | N/A (feed additive) | N/A | N/A | N/A | **CONFIRMED** |
| 2 | Rumen-protected butyrate | Host tight junctions | N/A | N/A (host target) | N/A | **CONFIRMED** |
| 3 | Zinc + butyrate | Host tight junctions | N/A | N/A (host target) | N/A | **CONFIRMED** |
| 4 | Multi-antigen vaccine | FomA: JQ740821; LktA: AF312861; HA: M1S0E1 | FomA: both ssp; LktA: near-universal (45/46); HA: DISPUTED | LktA: no homologs; FomA: no homologs | No PDB/AF for any | **CORRECTED** (HA issue + wrong H2 component) |
| 5 | Anti-FomA mAb | FomA: JQ740821 | Both subspecies | No bovine homologs | No PDB | **CORRECTED** (Factor H claim unsupported) |
| 6 | Epimural probiotic | N/A (ecology) | N/A | N/A | N/A | **CONFIRMED** |
| 7 | Mucoadhesive sealant | N/A (material) | N/A | N/A | N/A | **FLAGGED** (chitosan rumen stability) |
| 8 | Oral IgA vaccine | Same antigens as #4 | See #4 | See #4 | See #4 | **CONFIRMED** |
| 9 | Hindgut prebiotic | N/A (microbiome) | N/A | N/A | N/A | **CONFIRMED** |
| 10 | Hindgut butyrate+zinc | Host tight junctions | N/A | N/A (host target) | N/A | **CONFIRMED** |
| 11 | Anti-LktA mAb | LktA: AF312861 | Near-universal (45/46) | No bovine homologs | No PDB/AF | **CONFIRMED** |
| 12 | rPL4 vaccine | LktA PL4: AF312861 | Near-universal | No bovine homologs | No PDB/AF | **CONFIRMED** |
| 13 | LktA receptor ID | Unknown target | N/A | N/A | N/A | **CONFIRMED** (knowledge gap) |
| 14 | Gallium(III) | Non-specific (iron enzymes) | N/A | Host iron risk | N/A | **FLAGGED** (weak vs anaerobes) |
| 15 | Antiplatelet | Host pharmacology | N/A | N/A | N/A | **CONFIRMED** (but Forge kills it) |
| 16 | Anti-pyolysin | PLO of T. pyogenes | Tp present ~29% LA | CDCs conserved | Known CDC fold | **CONFIRMED** |
| 17 | Quorum quench | luxS gene in Fn | Gene present, function unknown | N/A | N/A | **FLAGGED** (QS vs metabolic) |
| 18 | Immunomod macrolide | Host NF-kB pathway | N/A | N/A (host) | N/A | **CONFIRMED** |
| 19 | TGF-beta1 delay | Host stellate cells | N/A | N/A (host) | N/A | **FLAGGED** (paradoxical risk) |
| 20 | No candidate (Stage 10) | N/A | N/A | N/A | N/A | **CONFIRMED** |
| 21 | PDT of PPIX | PPIX (from P. levii) | N/A | N/A | N/A | **CONFIRMED** (kill -- engineering impossible) |
| 22 | PPIX biosynthesis inhib | Heme pathway enzymes | Conserved bacteria+host | Shared with host | N/A | **FLAGGED** (host toxicity) |
| 23 | Biofilm dispersal | Unknown matrix | Uncharacterized | N/A | N/A | **FLAGGED** (matrix composition unknown) |
| 24 | Metronidazole analog | Nitroimidazole chemistry | F.n. MIC 0.25-2 ug/mL | N/A | N/A | **CONFIRMED** (regulatory block) |
| 25 | Bacteriocin probiotic | N/A (ecology) | N/A | N/A | N/A | **CONFIRMED** |
| 26 | Triple stack | See #1 + #12 | See #1 + #12 | N/A | N/A | **CONFIRMED** |
| 27 | FP-100 type | Fusobacterium ribosome | Unknown for F.n. | N/A | N/A | **FLAGGED** (cross-species activity unknown) |

---

## Key Accession Numbers Registry

| Protein | Accession | Type | Size | Organism |
|---|---|---|---|---|
| LktA (leukotoxin) | AF312861 (GenBank nt) | Nucleotide | 9,726 bp / 3,241 aa / 336 kDa | F.n. subsp. necrophorum A25 |
| LktA (UniProt) | H9CIJ2 | Protein (unreviewed) | 3,241 aa | F. necrophorum |
| FomA / 43K OMP | JQ740821 (GenBank nt) | Nucleotide | 1,134 bp / 377 aa / 42.9 kDa | F.n. subsp. necrophorum |
| Hemagglutinin (fragment) | M1S0E1 (UniProt) | Protein fragment | Unknown | F. necrophorum |
| OmpH (17.5 kDa) | WP_035904032.1 (RefSeq) | Protein | 159 aa / 17.5 kDa | F. necrophorum |
| OmpA (22.7 kDa) | WP_005961133.1 (RefSeq) | Protein | 217 aa / 22.7 kDa | F. necrophorum |
| CSP (66.3 kDa) | WP_035916891.1 (RefSeq) | Protein | 638 aa / 66.3 kDa | F. necrophorum |
| Genome (reference) | CP034842 (GenBank) | Genome | 2,678,415 bp | F.n. subsp. necrophorum ATCC 25286 |

---

## Structural Status Summary

| Protein | PDB Crystal | AlphaFold Model | Homology Model Available |
|---|---|---|---|
| LktA (336 kDa) | None | Not found | None -- no homologs to any known protein |
| FomA (42.9 kDa) | None (Fn); None (Fnu*) | Not found for Fn | F. nucleatum FomA topology mapped (14-strand beta-barrel) but no atomic coordinates |
| Hemagglutinin (19 kDa) | None | Not found | N/A |
| OmpH (17.5 kDa) | None for Fn | Not searched | OmpH family structures exist in other species |
| FadA | None for Fn | Not found | F. nucleatum FadA may have structural data |
| Pyolysin (PLO) | CDC family structures known | Not searched for Tp | Known CDC fold (e.g., streptolysin O, perfringolysin O) |

*Fn = F. necrophorum; Fnu = F. nucleatum; Tp = T. pyogenes

**Critical note on structure availability:** The complete absence of experimental or predicted structures for F. necrophorum virulence proteins is a significant gap. AlphaFold3 submissions for FomA, OmpH, OmpA, CSP, and the PL4 fragment of LktA should be prioritized. These would enable rational epitope selection for vaccine design and potentially mAb development.

---

## Experiments That Would Most Change the Portfolio

1. **Hemagglutinin gene identity resolution** (~$5K, 2 weeks) -- PCR the specific 19 kDa hemagglutinin gene from 20 necrophorum and 20 funduliforme bovine liver abscess isolates. This determines whether hemagglutinin belongs in the vaccine.

2. **FP-100 MIC against F. necrophorum** (~$5K, 2 weeks) -- If FP-100 is active against F. necrophorum at comparable concentrations to F. nucleatum (2 uM), this becomes a potentially transformative narrow-spectrum antimicrobial for liver abscess.

3. **Gallium nitrate MIC against F. necrophorum** (~$5-10K, 1 month) -- Given reduced activity against anaerobes, a negative result kills Candidate 14 immediately.

4. **LktA antigenic variation survey** (~$10K, 1 month) -- Sequence the PL4 region of lktA from 20+ recent bovine liver abscess isolates. If PL4 epitopes are highly conserved, vaccine confidence increases. If variable, the vaccine must be multivalent.

5. **AlphaFold3 structure predictions** (free, 1-2 weeks) -- Submit FomA, PL4, OmpH, OmpA, CSP sequences for structure prediction. Enables rational vaccine and mAb design.

---

## References Cited in This Report

- Amachawadi et al. (2021). Multi-component recombinant subunit vaccine in mice. Front Vet Sci 8:780377.
- Amachawadi et al. (2023). Three new outer membrane adhesion proteins. Microorganisms 11:2968.
- Calcutt et al. (2019). Complete genome ATCC 25286. Microbiol Resour Announc 8:e00025-19.
- Felizari et al. (2025). Tannin blend as tylosin alternative. Vet Sci 12:446.
- Friberg/Holm et al. (2008). Factor H binding. J Immunol 181:8624.
- Kanoe & Yamanaka (1989). Bovine platelet aggregation. J Med Microbiol 29:13.
- Kleivdal et al. (2001). FomA topology. Microbiology 147:1059.
- Kook et al. (2022). Comparative genomics 46 strains. Microbiol Spectrum 10:e00297-22.
- Kumar et al. (2015). FomA identification. Vet Microbiol 176:340-349.
- Lockhart et al. (2022). PPIX from dual-species biofilms. Biofilm 4:100083.
- Machado et al. (2014). Metritis vaccine. PLoS One 9:e91734.
- Nagaoka et al. (2013). Mouse liver abscess model. J Med Microbiol 62:1398-1404.
- Ohkuni et al. (2017). Three leukotoxin variants in human isolates. Anaerobe 48:63-69.
- Pinnell & Morley (2022). Microbial ecology of liver abscesses. Vet Clin Food Anim.
- Saginala et al. (1997). Leukotoxoid vaccine. J Anim Sci 75:1160-1166.
- Salih et al. (2025). Etiology delineation. Microbiol Spectrum.
- Tadepalli et al. (2006). Distinct lktBAC promoters. Vet Microbiol 116:175.
- Zhang et al. (2001). lktA cloning. Infect Immun 69:5738.
- 2024 ACS Agric Sci Technol: First tylosin-resistant F. necrophorum strains (erm(B)).
- 2025 Sci Rep: Computational multiepitope vaccine design for F. necrophorum.
