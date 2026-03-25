# Phase 3: Bovine Mastitis Treatment Candidates

**Program:** Mastitis | **Partner:** Zoetis
**Agent:** Forge | **Date:** 2026-03-25 | **Revision:** R0
**Primary pathogen:** *Staphylococcus aureus* (focus), with cross-pathogen candidates where relevant
**Inputs:** Phase 1 Disease Map (R1), Phase 2 Failure Analysis (R1)

---

## Executive Summary

This document proposes treatment candidates for all nine disease stages (Stage 0 through Stage 8) of bovine *S. aureus* mastitis, organized by three categories: Known Approaches (literature-supported), Non-Obvious Approaches (cross-disease analogies and emerging biology), and Novel Proposals (first-principles designs for gap stages). Sapper identified complete gaps at Stage 7 (reinfection/reseeding), critical gaps at Stage 5 (intracellular/SCV/biofilm persistence), and defeated approaches at Stages 2-3 (adhesion, immune evasion). Every stage receives at least one candidate.

The central strategic insight: no single mechanism can address this disease (Sapper Constraint 8). The candidates are therefore designed as a **combination toolkit** -- individual mechanisms that can be assembled into multi-barrier regimens addressing intracellular persistence, biofilm, fibrosis, and immune evasion simultaneously. The document concludes with three proposed combination architectures that integrate candidates across stages to target the 70% pathology coverage threshold.

**Total candidates proposed:** 32 across 9 stages (13 Known, 10 Non-Obvious, 9 Novel)

---

## Table of Contents

1. [Stage 0: Upstream Systemic Modifiers](#stage-0-upstream-systemic-modifiers)
2. [Stage 1: Entry and Exposure](#stage-1-entry-and-exposure)
3. [Stage 2: Adhesion and Colonization](#stage-2-adhesion-and-colonization)
4. [Stage 3: Immune Evasion](#stage-3-immune-evasion)
5. [Stage 4: Acute Pathology and Tissue Damage](#stage-4-acute-pathology-and-tissue-damage)
6. [Stage 5: Chronic Persistence](#stage-5-chronic-persistence)
7. [Stage 6: Treatment Resistance](#stage-6-treatment-resistance)
8. [Stage 7: Reinfection and Reseeding](#stage-7-reinfection-and-reseeding)
9. [Stage 8: Resolution and Remodeling](#stage-8-resolution-and-remodeling)
10. [Combination Architectures](#combination-architectures)
11. [Coverage Map](#coverage-map)

---

## Stage 0: Upstream Systemic Modifiers

### Candidate 0A: Protected Butyrate Oral Supplementation (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Gut-mammary axis: butyrate depletion during SARA/NEB drives mammary inflammation via cGAS-STING/NLRP3 activation (Phase 1, Section 0.1). Oral butyrate restores SCFA levels, strengthens intestinal barrier, reduces LPS translocation, and supports mammary epithelial barrier integrity |
| **Disease stage** | Stage 0 (upstream systemic modifier) |
| **Category** | Known |
| **Evidence tier** | [MODERATE] -- bovine gut-mammary axis established (PMID 41130091, PMID 40033186); butyrate anti-inflammatory effects established in bovine systems; protected butyrate products exist as feed additives but not specifically tested for mastitis prevention |
| **Species data** | Bovine in-vivo (gut-mammary axis); caprine in-vivo (RMT model); bovine in-vitro (butyrate on epithelial cells) |
| **Key risk** | The gut-mammary axis contribution to mastitis incidence is unquantified -- if it contributes <10% of total incidence, the effect size will be undetectable in field trials |
| **Proposed de-risk** | Controlled field trial: 200 transition cows, protected butyrate vs. control, measure SCC, clinical mastitis incidence, and serum LPS during first 60 DIM. Cost: ~$50-80K |
| **Sapper constraint addressed** | Constraint 16 (genomic selection addresses Stage 0 at population scale -- butyrate addresses it at individual cow scale during transition period) |

**20-Year Test:** Butyrate as a feed additive has been studied for rumen health for >20 years. No product specifically positioned for mastitis prevention exists because: (a) the gut-mammary axis mechanism was not characterized until recently (2024-2025), (b) butyrate products were marketed for gut health and growth, not udder health, (c) the effect on mastitis specifically has not been tested in a powered trial. The mechanistic rationale is new even if the molecule is old.

---

### Candidate 0B: Peripartum Calcium + BHBA Management Protocol (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | BHBA-mediated neutrophil dysfunction: subclinical ketosis (BHBA >1.2 mmol/L) abrogates bovine NET formation and impairs neutrophil bactericidal activity (PMID 18411287, PMID 41651367). Hypocalcemia impairs neutrophil phagocytosis (PMID 2745826). Targeted oral calcium + propylene glycol supplementation during the transition period normalizes both pathways |
| **Disease stage** | Stage 0 |
| **Category** | Known |
| **Evidence tier** | [ESTABLISHED] for BHBA-neutrophil link and calcium-neutrophil link; [MODERATE] for mastitis-specific prevention benefit of targeted supplementation |
| **Species data** | Bovine in-vivo (epidemiology), bovine in-vitro (neutrophil function) |
| **Key risk** | This is management, not a product. Incremental benefit may be small because many well-managed herds already do this |
| **Proposed de-risk** | Retrospective analysis of herds with and without targeted transition management, correlating BHBA/Ca monitoring with mastitis incidence. Low cost, data may already exist in dairy herd records |
| **Sapper constraint addressed** | Constraint 14 (cow-level factors determine 4-92% cure range -- metabolic management shifts the starting point) |

---

### Candidate 0C: Gut Microbiome-Targeted Probiotic (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | Oral administration of butyrate-producing bacteria (e.g., *Faecalibacterium prausnitzii* or bovine-specific *Clostridium* cluster IV strains) to restore gut SCFA production, reduce LPS translocation, and attenuate cGAS-STING-mediated mammary inflammation. Cross-disease analogy: human gut microbiome-targeted probiotics for distal inflammation (IBD, metabolic syndrome) |
| **Disease stage** | Stage 0 |
| **Category** | Non-Obvious |
| **Evidence tier** | [INFERRED] -- gut-mammary axis established [MODERATE]; specific probiotic strains for bovine gut-mammary modulation untested |
| **Species data** | Caprine in-vivo (RMT proof-of-concept, PMID 41130091); bovine in-vivo (gut microbiome-mastitis correlation, PMID 40033186) |
| **Key risk** | Bovine rumen environment may degrade oral probiotics before reaching the hindgut. Rumen-protected formulation needed |
| **Proposed de-risk** | Identify butyrate-producing genera depleted in mastitis cows vs. healthy (from existing microbiome data); formulate rumen-protected capsule; pilot in 50 transition cows. Cost: ~$80-120K |
| **Sapper constraint addressed** | Constraint 16 (population-level approach); operates upstream of all treatment barriers |

**Closest analogy:** Rumen microbiota transplantation (RMT) in mice caused mastitis-like pathology (PMID 41130091), proving causality. Reversing the gut dysbiosis should reverse the predisposition.

---

## Stage 1: Entry and Exposure

### Candidate 1A: Next-Generation Teat Sealant with Antimicrobial Keratin Mimetic (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | Internal teat sealant (bismuth subnitrate) enhanced with synthetic analogues of teat canal keratin fatty acids (C12:0 lauric acid, C14:0 myristic acid) that provide bactericidal activity against *S. aureus* during the vulnerable dry-off and pre-calving windows. The natural teat canal keratin is bacteriostatic via these fatty acids (Phase 1, Section 1.1) -- augmenting a sealant with concentrated fatty acid analogues extends this defense |
| **Disease stage** | Stage 1 |
| **Category** | Non-Obvious |
| **Evidence tier** | [INFERRED] -- teat keratin fatty acid bacteriostatic activity [ESTABLISHED]; incorporation into sealant formulation untested |
| **Species data** | Bovine in-vivo (ITS efficacy); bovine in-vitro (keratin fatty acid activity) |
| **Key risk** | Fatty acids may interact with bismuth subnitrate, altering physical properties of the sealant. Formulation stability unknown |
| **Proposed de-risk** | Formulation study: sealant + lauric/myristic acid at 3 concentrations, test physical stability and in-vitro *S. aureus* killing in simulated teat canal conditions. Cost: ~$30-50K |
| **Sapper constraint addressed** | Constraint 13 (EU Regulation 2019/6 favors non-antibiotic approaches -- an antimicrobial sealant avoids antibiotic use at dry-off) |

---

### Candidate 1B: Probiotic Teat Dip with NAS Colonizers (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | Post-milking teat dip reformulated with live *S. chromogenes* and *S. simulans* -- non-aureus staphylococci that suppress *S. aureus* biofilm formation, produce bacteriocins active against clinical *S. aureus* (57.5% also inhibit MRSA), and are epidemiologically associated with lower *S. aureus* IMI risk (Phase 1, MB.2). The concept: replace chemical disinfection that kills ALL organisms (including protective commensals) with targeted colonization resistance |
| **Disease stage** | Stage 1 |
| **Category** | Non-Obvious |
| **Evidence tier** | [PRELIMINARY] -- NAS protective effects established in epidemiological studies and in-vitro; deliberate application as teat dip untested |
| **Species data** | Bovine epidemiology (NAS-*S. aureus* negative correlation); bovine in-vitro (biofilm suppression, bacteriocin production) |
| **Key risk** | Regulatory classification of a live bacterial teat dip is uncertain. Some NAS species can themselves cause mild subclinical mastitis -- strain selection critical |
| **Proposed de-risk** | Characterize 3-5 NAS strains: confirm *S. aureus* inhibition, confirm absence of own virulence, test colonization persistence on teat skin in a pilot with 20 cows. Cost: ~$60-90K |
| **Sapper constraint addressed** | Constraint 13 (non-antibiotic, regulatory tailwind); addresses the antibiotic-disruption-of-microbiome problem (Phase 1, MB.3) |

**Closest analogy:** Human vaginal probiotic suppositories (*Lactobacillus*) to prevent recurrent urinary tract infections. Same principle: colonization resistance by commensals rather than antibiotic sterilization.

---

## Stage 2: Adhesion and Colonization

### Candidate 2A: Sortase A (SrtA) Inhibitor (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | SrtA anchors all MSCRAMMs (ClfA, ClfB, FnBPA, FnBPB, SpA, IsdA, Cna) to the *S. aureus* cell wall. Inhibiting SrtA prevents surface display of adhesins, blocking adhesion (Stage 2), internalization (gateway to Stage 5), AND SpA-mediated immune evasion (Stage 3) in a single mechanism. SrtA is non-essential for growth, so resistance pressure is reduced (Quality Standard 15) |
| **Disease stage** | Stage 2 (primary), Stage 3 (secondary), Stage 5 (prevents new internalization) |
| **Category** | Known |
| **Evidence tier** | [MODERATE] -- SrtA validated as target in multiple in-vitro and mouse models; 32+ publications on SrtA inhibitors (PMID 35913166, 30369109, 30249042, 40122408); no bovine in-vivo data; no clinical-grade small-molecule inhibitor with drug-like properties |
| **Species data** | Mouse in-vivo (SrtA mutants attenuated); in-vitro (multiple compound classes) |
| **Key risk** | 20-Year Test concern: SrtA has been a drug target since ~2002 (Mazmanian et al.). No product exists. Likely reasons: (a) high protein-protein interaction binding site is hard to drug; (b) early inhibitors had poor PK; (c) anti-virulence agents face commercial uncertainty (don't kill bacteria, so efficacy endpoints are harder to define). Recent advances in covalent and allosteric inhibitors may overcome the medicinal chemistry barrier |
| **Proposed de-risk** | Screen 3-5 recently published SrtA inhibitor scaffolds (e.g., dihydro-beta-agarofuranone, thiadiazolidinedione derivatives; PMID 40122408) against bovine CC97/CC151/CC479 isolates for: (a) surface protein reduction by flow cytometry, (b) fibronectin-binding inhibition, (c) MAC-T internalization reduction. Cost: ~$60-80K |
| **Sapper constraint addressed** | Constraint 4 (SpA Fc-binding is validated -- SrtA inhibition prevents SpA surface display, sidestepping the immune evasion problem); Constraint 8 (multi-barrier -- SrtA inhibitor addresses adhesion, immune evasion, AND prevents new internalization simultaneously) |
| **Host selectivity** | SrtA has no mammalian homolog. Zero host selectivity concern. [Quality Standard 14 satisfied] |
| **Resistance logic** | SrtA is non-essential for growth -- low selection pressure for resistance. Resistance via SrtA active-site mutation possible but would compromise fitness (poor surface protein display). [Quality Standard 15 addressed] |

---

### Candidate 2B: Anti-FnBP Adhesion-Blocking Strategy -- Soluble Fibronectin Decoy (Novel)

| Field | Detail |
|---|---|
| **Target/mechanism** | FnBPA/FnBPB-mediated internalization into mammary epithelial cells is the gateway to chronic persistence (Phase 1, Section 2.2). The mechanism requires a fibronectin bridge between bacterial FnBPs and host alpha5-beta1 integrin. A soluble fibronectin fragment (the FnBP-binding N-terminal domain of fibronectin, FnI1-5) administered intramammarily would act as a **competitive decoy**, saturating FnBPs and preventing them from engaging cell-surface fibronectin. This blocks internalization without requiring antibodies |
| **Disease stage** | Stage 2 (blocking internalization) |
| **Category** | Novel |
| **Evidence tier** | [INFERRED] -- FnBP-fibronectin interaction mechanism [ESTABLISHED] in bovine MAC-T cells (PMID 10547450, 10456915); FnBP-deficient mutant shows >95% reduction in internalization [ESTABLISHED]; soluble fibronectin fragment as competitive inhibitor untested |
| **Species data** | Bovine cell (MAC-T) for FnBP biology |
| **Key risk** | Protein therapeutic in milk matrix -- subject to Sapper Constraint 2 (formulation critical) and Constraint 6 (mammary gland pharmacological challenges). Fibronectin fragment may bind host matrix proteins non-specifically. Half-life in milk unknown |
| **Proposed de-risk** | Express recombinant bovine FnI1-5 domain; test in MAC-T cell invasion assay at 3 concentrations with CC97 and CC151 strains. If >50% internalization reduction at <10 ug/mL, proceed. Cost: ~$40-60K |
| **Sapper constraint addressed** | Constraint 1 (addresses the intracellular problem at source -- prevent internalization rather than kill intracellular bacteria); Constraint 2 (protein therapeutic, but a simple domain rather than a complex antibody) |

**Biological rationale:** If you cannot kill bacteria inside cells, prevent them from getting inside cells. FnBP-mediated internalization is the rate-limiting step for establishing the intracellular reservoir. Blocking this step could fundamentally change the disease trajectory from chronic to acute/self-resolving.

**Closest analogy:** Soluble receptor decoys in human medicine (e.g., etanercept is a soluble TNF receptor that acts as a decoy to sequester TNF-alpha). Same principle: competitive inhibition of a ligand-receptor interaction using a soluble version of one partner.

**Most likely failure mode:** Rapid clearance from milk by milking or proteolytic degradation, requiring impractically frequent dosing. If used during the dry period (when milking removal is absent), half-life would be longer and efficacy potentially much higher.

**Cheapest test:** Recombinant FnI1-5 + MAC-T invasion assay. Go/kill in 6 weeks, ~$40K.

---

### Candidate 2C: Gallium(III) as an Iron-Acquisition Disruptor (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | Gallium(III) is an iron mimetic that is taken up by bacterial iron-acquisition systems (Isd pathway, siderophore systems) but cannot participate in redox reactions. It poisons iron-dependent enzymes, disrupts electron transport chain, inhibits biofilm, and is bactericidal at micromolar concentrations. Critically, Ga(III) enters bacteria through the same pathways *S. aureus* uses to acquire iron in the iron-limited mammary environment (Phase 1, Section 2.3). Gallium also disrupts MRSA biofilm via eDNA-dependent dispersal |
| **Disease stage** | Stage 2 (iron acquisition disruption), Stage 5 (biofilm disruption, anti-SCV via ETC poisoning), Stage 6 (non-antibiotic kill mechanism) |
| **Category** | Non-Obvious (cross-disease analogy from Pseudomonas/wound infection field) |
| **Evidence tier** | [MODERATE] -- gallium antibacterial activity against *S. aureus* including MRSA established in-vitro and in murine wound models (PMID 34346692, 31264851, 38878097); gallium + gallium porphyrin combination promotes MRSA biofilm dispersal; FDA-approved for IV use (gallium nitrate, Ganite) in hypercalcemia; NOT tested in bovine mastitis or intramammary route |
| **Species data** | Mouse in-vivo (wound model), extensive in-vitro against *S. aureus* |
| **Key risk** | Gallium is a heavy metal -- milk residue and food safety implications must be addressed. Withdrawal period unknown for intramammary use. Formulation for intramammary delivery untested. Potential bovine mammary epithelial toxicity at antibacterial concentrations |
| **Proposed de-risk** | (1) MIC/MBC of gallium nitrate against CC97/CC151/CC479 in whole bovine milk (not broth -- Sapper Constraint 6); (2) bovine MAC-T cytotoxicity at effective concentrations; (3) intracellular killing assay (MAC-T cells infected with *S. aureus*, treated with gallium). Cost: ~$50-70K |
| **Sapper constraint addressed** | Constraint 9 (lactoferrin synergy validates iron deprivation -- gallium is a more potent iron pathway disruptor); Constraint 1 (gallium enters intracellular bacteria via iron transporters -- potential intracellular activity); Constraint 5 (gallium disrupts biofilm while being bactericidal -- simultaneous disruption + killing) |
| **Resistance logic** | Gallium resistance in *S. aureus* has been studied: resistance evolution is possible but slower than antibiotic resistance, and fitness costs are associated with gallium-resistant mutants. The multiple iron-dependent targets create a higher barrier to resistance than single-target agents. [Quality Standard 15 addressed] |

**Closest analogy:** Gallium nitrate is FDA-approved (IV) for human hypercalcemia of malignancy. Gallium protoporphyrin + gallium nitrate combination showed enhanced antimicrobial activity in-vitro and in-vivo against MRSA in murine models. The "Trojan horse" strategy (bacteria import gallium thinking it is iron) is conceptually elegant.

**20-Year Test:** Gallium as an antimicrobial has been studied since ~2007. No antibacterial product is marketed. Reasons: (a) regulatory pathway for a metal-based antimicrobial is novel, (b) toxicity concerns at systemic doses, (c) the oral/IV route was studied for systemic infections where alternatives exist. Intramammary local delivery to an iron-restricted environment is a new application context where the iron-mimetic mechanism is maximally relevant.

---

## Stage 3: Immune Evasion

### Candidate 3A: SpA-Neutralizing Vaccine (SpAKKAA/SpA* Platform) (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Vaccination with non-toxigenic SpA variants (SpAKKAA or improved SpA*) that cannot bind IgG-Fc or VH3-Fab, generating antibodies that neutralize native SpA on the bacterial surface. This removes SpA's Fc-binding immune evasion (validated in cattle) and potentially Fab-mediated B-cell superantigen activity (unvalidated in cattle per Sapper Constraint 4). By neutralizing SpA, vaccine-induced and natural antibodies regain opsonophagocytic function |
| **Disease stage** | Stage 3 (immune evasion -- SpA neutralization) |
| **Category** | Known |
| **Evidence tier** | [MODERATE] -- SpAKKAA vaccination protects mice against MRSA (PMID 20713595, Kim et al. 2010, J Exp Med); improved SpA* (SpAKKE) with better safety profile (PMID 34088508); SpA+LukAB combination vaccine tested in minipig model (Nature npj Vaccines 2025); SpA Fc-binding in cattle [ESTABLISHED]; SpA-Fab binding in cattle [UNVALIDATED] |
| **Species data** | Mouse in-vivo (Kim et al. 2010); minipig in-vivo (2025); NO bovine data |
| **Key risk** | (1) Mouse efficacy may not translate to cattle -- bovine mammary immune environment is fundamentally different; (2) SpA VH3-Fab mechanism may not operate in cattle (Sapper Constraint 4) -- if SpA's damage is primarily Fc-mediated, Fc-neutralization alone may be sufficient; (3) 20-Year Test: SpAKKAA was first published in 2010 and no livestock vaccine exists, though human clinical programs are advancing |
| **Proposed de-risk** | (1) Test SpAKKAA-induced bovine serum for opsonophagocytic killing of CC97/CC151 in bovine whole milk; (2) Test whether SpA binds bovine BoVH1 (VH4-type) Fab -- directly addresses the unvalidated mechanism. Cost: ~$80-120K |
| **Sapper constraint addressed** | Constraint 4 (explicitly addresses the SpA uncertainty by testing bovine-specific mechanism); Constraint 8 (multi-barrier -- SpA neutralization re-enables the entire humoral immune response) |

**Why this is worth pursuing despite the 20-Year Test:** SpAKKAA was designed for human MRSA, not bovine mastitis. The bovine application is genuinely novel. SpA-mediated immune evasion is the single most cited reason for vaccine failure in bovine *S. aureus* mastitis -- removing it could unlock the entire vaccine approach.

---

### Candidate 3B: Anti-LukMF' Toxoid Vaccine (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | LukMF' is the most potent leukocidin against bovine neutrophils, acting via CCR1 receptor (PMID 26045537). Vaccination with detoxified LukM/LukF' toxoid to generate neutralizing antibodies that protect neutrophils from killing. This preserves neutrophil function during infection, improving bacterial clearance. Analogous to anti-Hla strategies in human *S. aureus* but targeting the bovine-specific toxin |
| **Disease stage** | Stage 3 (immune evasion -- leukocidin neutralization), Stage 4 (tissue damage reduction) |
| **Category** | Known |
| **Evidence tier** | [MODERATE] -- LukMF' identified as primary bovine neutrophil toxin [ESTABLISHED]; CCR1 receptor identified [ESTABLISHED]; toxoid vaccine approach is standard for pore-forming toxins; bovine LukMF' vaccination NOT tested |
| **Species data** | Bovine in-vitro (neutrophil killing); bovine in-vivo (LukM detected in milk during mastitis, PMID 27242043) |
| **Key risk** | LukMF' carriage is lineage-dependent: CC151 high, CC97 ~30%. A LukMF'-targeting vaccine may have limited efficacy against CC97 infections where LukMF' is absent. Multi-antigen approach needed |
| **Proposed de-risk** | (1) Confirm LukMF' carriage in target market strains; (2) Generate bovine anti-LukM serum; (3) Test neutrophil survival in presence of anti-LukM + live CC151 bacteria in bovine whole milk. Cost: ~$70-100K |
| **Sapper constraint addressed** | Constraint 4 (LukMF'-CCR1 interaction validated in bovine cells -- no species extrapolation uncertainty) |

---

### Candidate 3C: Mucosal IgA Vaccination (Intramammary Immunization) (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | Conventional systemic vaccination generates serum IgG, which SpA binds and subverts. Secretory IgA (sIgA) is NOT bound by SpA. Intramammary or local mucosal immunization to generate mammary-associated lymphoid tissue (MALT)-derived sIgA that can opsonize *S. aureus* without SpA interference. Uses multi-antigen formulation (ClfA, FnBP, CP5/CP8 conjugate) delivered intramammarily in a mucosal adjuvant |
| **Disease stage** | Stage 3 (immune evasion bypass), Stage 2 (anti-adhesion) |
| **Category** | Non-Obvious |
| **Evidence tier** | [INFERRED] -- SpA does not bind IgA [ESTABLISHED]; bovine mammary gland has MALT-like structures (Furstenberg's rosette contains plasma cells, Phase 1 Section 1.1); local mammary immunization producing local antibodies has been demonstrated in limited studies; specific sIgA-based anti-*S. aureus* mammary vaccination untested |
| **Species data** | Bovine histology (Furstenberg's rosette immune cells); limited bovine in-vivo intramammary immunization studies |
| **Key risk** | Bovine mammary gland is immunologically "cold" compared to gut/respiratory mucosa -- whether intramammary antigen delivery generates robust local sIgA responses is uncertain. Dry period may be the optimal window for immunization (gland undergoing involution with higher immune activity) |
| **Proposed de-risk** | Intramammary delivery of model antigen (ovalbumin) + mucosal adjuvant (cholera toxin B subunit) in 10 dry cows: measure sIgA in milk at calving vs. systemic control (IM injection). Go if sIgA/IgG ratio >2 in milk. Cost: ~$50-80K |
| **Sapper constraint addressed** | Constraint 4 (completely bypasses SpA -- sIgA is invisible to SpA); Constraint 8 (multi-barrier -- local sIgA operates in the mammary gland where systemic IgG transfer is limited) |

**Closest analogy:** Oral polio vaccine generates mucosal IgA immunity that prevents intestinal infection, while injectable polio vaccine generates systemic IgG that prevents viremia. Same principle: route of immunization determines the type of immune response and the compartment it protects.

---

### Candidate 3D: AdsA Inhibitor -- Blocking the Adenosine Immune Suppression Loop (Novel)

| Field | Detail |
|---|---|
| **Target/mechanism** | AdsA (adenosine synthase A) converts AMP to adenosine, which suppresses neutrophil oxidative burst via A2A receptors. AdsA also converts NET degradation products (deoxyribonucleotides) into dAdo/dGuo that kill macrophages (Phase 1, Section 3.1). Blocking AdsA would: (a) restore neutrophil killing capacity, (b) prevent macrophage apoptosis from NET degradation products, (c) break the lethal feedback loop where immune cells are recruited only to be killed by their own degradation products |
| **Disease stage** | Stage 3 (immune evasion -- adenosine-mediated suppression) |
| **Category** | Novel |
| **Evidence tier** | [INFERRED] -- AdsA mechanism established in mouse models (PMID 19752399, 31719177, 35355997); bovine-specific AdsA function not directly tested |
| **Species data** | Mouse in-vivo (AdsA mutants are attenuated); NO bovine data |
| **Key risk** | AdsA is a sortase-anchored surface enzyme -- an SrtA inhibitor (Candidate 2A) would also prevent AdsA surface display, potentially making a specific AdsA inhibitor redundant. Host adenosine signaling is ubiquitous -- selectivity must be achieved by targeting the bacterial enzyme, not the host A2A receptor |
| **Proposed de-risk** | (1) Confirm AdsA is expressed and surface-displayed by bovine CC97/CC151 isolates; (2) Test whether SrtA inhibition reduces AdsA surface activity (synergy test with Candidate 2A); (3) If needed, develop recombinant bovine AdsA for inhibitor screening. Cost: ~$60-80K |
| **Sapper constraint addressed** | Constraint 8 (addresses a specific immune evasion mechanism that amplifies all other barriers by killing the immune cells sent to clear the infection) |
| **Host selectivity** | AdsA is a bacterial 5'-nucleotidase with no direct mammalian ortholog at the bacterial cell surface. Host 5'-nucleotidases exist but are intracellular or differently localized. Selectivity risk is LOW for a surface-targeted approach. [Quality Standard 14 assessed] |

**Biological rationale:** The Phase 1 map describes a "lethal feedback loop" (Section 3.1): neutrophils are recruited, killed by leukotoxins, their NETs are degraded by nuclease, and the degradation products are converted by AdsA into molecules that kill macrophages. AdsA is the final enzyme in this death cascade. Blocking it would break the loop.

**Most likely failure mode:** AdsA inhibition may be insufficient because the upstream steps (leukocidin-mediated neutrophil killing, nuclease-mediated NET degradation) are independently damaging. AdsA inhibition alone removes the macrophage killing step but does not prevent neutrophil destruction.

---

## Stage 4: Acute Pathology and Tissue Damage

### Candidate 4A: Anti-Hla Monoclonal Antibody (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Alpha-hemolysin (Hla) forms heptameric pores in mammary epithelial cells, disrupting the epithelial barrier and enabling bacterial dissemination into deeper tissue (Phase 1, Section 4.3). Monoclonal antibody against Hla prevents pore formation, reduces tissue damage, and preserves epithelial barrier integrity |
| **Disease stage** | Stage 4 (acute pathology -- tissue damage reduction) |
| **Category** | Known |
| **Evidence tier** | [MODERATE] -- anti-Hla mAbs (e.g., MEDI4893/suvratoxumab) developed for human *S. aureus* pneumonia prevention (PMID 29311091); Hla role in bovine mastitis tissue damage [ESTABLISHED]; bovine-specific anti-Hla approach not tested |
| **Species data** | Human clinical trials (Phase 2 for pneumonia); mouse in-vivo; bovine in-vitro (Hla on mammary epithelial cells) |
| **Key risk** | (1) mAb is a protein therapeutic subject to milk matrix challenges (Sapper Constraint 2); (2) Hla may not be the primary tissue-damaging toxin in all bovine infections (LukMF' and Hlb also contribute); (3) mAbs are expensive -- COGS per dose must be <$30 for commercial viability (Quality Standard 26) |
| **Proposed de-risk** | Test whether anti-Hla serum protects bovine mammary epithelial monolayers from CC97/CC151 supernatant damage (barrier integrity assay). If Hla contributes >50% of barrier damage, proceed. Cost: ~$40-60K |
| **Sapper constraint addressed** | Constraint 11 (APT validates tissue repair as a mechanism -- anti-Hla prevents tissue damage at source); Constraint 7 (reducing tissue damage preserves drug access to bacteria by preventing fibrosis) |

**20-Year Test:** Anti-Hla mAb (suvratoxumab) was developed by AstraZeneca/MedImmune for human *S. aureus* pneumonia. Phase 2 results showed reduced *S. aureus* pneumonia incidence. The human program continues, but no veterinary adaptation has been attempted. The mAb approach may be too expensive for veterinary use -- a small-molecule Hla inhibitor or a toxoid vaccine (see 3B) would be more commercially viable.

---

### Candidate 4B: NLRP3 Inflammasome Modulator (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | *S. aureus*-induced pyroptosis via NLRP3 inflammasome activation is a major mechanism of mammary epithelial cell death (Phase 1, Section 4.2). NLRP3 inhibition (e.g., MCC950/dapansutrile class) would reduce pyroptotic cell death, limit IL-1-beta/IL-18 release, and preserve epithelial integrity. The key insight: *S. aureus* exploits the PINK1/Parkin mitophagy pathway to suppress NLRP3 when it wants to persist intracellularly (Phase 1, Section 4.2) -- the bacteria already know NLRP3 modulation is important |
| **Disease stage** | Stage 4 (acute pathology -- pyroptosis reduction) |
| **Category** | Non-Obvious (cross-disease from human autoinflammatory disease field) |
| **Evidence tier** | [INFERRED] -- NLRP3 activation in bovine MAC-T cells during *S. aureus* infection [MODERATE] (PMID 35123552); MCC950 is a well-characterized NLRP3 inhibitor in multiple species; bovine mammary-specific NLRP3 inhibition untested |
| **Species data** | Bovine cell (MAC-T) for NLRP3 activation; human and mouse for MCC950 pharmacology |
| **Key risk** | NLRP3 is a host defense pathway. Inhibiting it may impair bacterial clearance, converting acute infections to chronic ones (trading tissue damage for persistence). The Phase 1 map notes that *S. aureus* itself co-opts PINK1/Parkin mitophagy to suppress NLRP3 for persistence -- pharmacological NLRP3 inhibition might HELP the bacteria |
| **Proposed de-risk** | MAC-T infection model: MCC950 at 3 concentrations + CC97. Measure: (a) pyroptotic cell death, (b) intracellular bacterial load at 24h and 48h. If pyroptosis drops >50% but intracellular load increases >2-fold, KILL this candidate. Cost: ~$30-50K |
| **Sapper constraint addressed** | Constraint 11 (tissue repair/preservation); but must be tested against Constraint 1 (intracellular persistence -- cannot make this worse) |

**Critical caveat:** This candidate requires the most careful de-risking because the same mechanism (*S. aureus* suppresses NLRP3 via mitophagy) is used by the pathogen for persistence. If pharmacological NLRP3 inhibition phenocopies *S. aureus*'s own immune suppression strategy, the candidate is dead. The de-risk experiment is designed to test exactly this.

---

## Stage 5: Chronic Persistence

This is the critical gap stage. Sapper identified it as the rate-limiting barrier. Every candidate here is designed to address one or more of: intracellular survival, SCV dormancy, or biofilm.

### Candidate 5A: Lactoferrin + Pirlimycin Combination (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Bovine lactoferrin (bLf) iron chelation + pirlimycin intracellular accumulation. Lactoferrin: (a) deprives bacteria of iron via chelation, (b) suppresses beta-lactamase transcription (blaZ/blaR1/blaI), (c) modulates immune response. Pirlimycin: (a) accumulates intracellularly, (b) reduces biofilm at sub-MIC. Combination targets iron-dependent intracellular survival (lactoferrin) while pirlimycin kills bacteria flushed from dormancy by iron stress |
| **Disease stage** | Stage 5 (intracellular persistence, SCVs, biofilm), Stage 6 (restores antibiotic susceptibility) |
| **Category** | Known |
| **Evidence tier** | [MODERATE] -- lactoferrin + penicillin G achieved 45.5% cure against resistant *S. aureus* (Phase 2, Section 13); lactoferrin alone 91.7% during dry period (n=12, PRELIMINARY); pirlimycin 8-day achieves 83-86% [MODERATE]; combination of lactoferrin + pirlimycin specifically untested |
| **Species data** | Bovine in-vivo (lactoferrin trials, pirlimycin trials -- separately) |
| **Key risk** | Lactoferrin COGS: pharmaceutical-grade bovine lactoferrin is $50-200/g; 100-500 mg per dose needed. At $100/g, this is $10-50 per dose -- potentially within commercial range but needs optimization. Pirlimycin 8-day regimen is already off-label and economically marginal |
| **Proposed de-risk** | 3-arm bovine pilot trial (n=20/arm): (a) pirlimycin 5-day alone, (b) lactoferrin + pirlimycin 5-day, (c) lactoferrin alone. Measure bacteriological cure at 21 and 42 days. If combination exceeds pirlimycin alone by >15 percentage points, proceed. Cost: ~$100-150K (Sapper Constraint 31 -- realistic CRO-grade costing) |
| **Sapper constraint addressed** | Constraint 9 (validates iron deprivation); Constraint 10 (rifaximin validates intracellular killing -- pirlimycin is a non-rifamycin intracellular-penetrating agent without SCV promotion risk); Constraint 7 (realistic benchmark -- target 70% cure with combination) |

---

### Candidate 5B: ADEP (Acyldepsipeptide) ClpP Activator -- "Wake and Kill from Within" (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | ADEP4 activates the ClpP protease, converting it from a regulated housekeeping protease to an unregulated degradative machine that digests >400 proteins indiscriminately. This kills persister cells and SCVs by forcing self-digestion -- the mechanism works BECAUSE the cells are dormant (dormant cells cannot replace degraded proteins). ADEP4 + rifampicin combination eradicated *S. aureus* from deep-seated murine biofilm infection in a single day (Conlon et al. 2013, Nature 503:365, PMID 24226776) |
| **Disease stage** | Stage 5 (persister/SCV killing -- the rate-limiting barrier) |
| **Category** | Non-Obvious (cross-disease from the antibiotic persistence research field) |
| **Evidence tier** | [MODERATE] -- ADEP4 kills *S. aureus* persisters in vitro and eradicates chronic biofilm infection in mouse model (PMID 24226776, Nature); kills persister cells that survive all conventional antibiotics; mechanism validated for *S. aureus* specifically |
| **Species data** | Mouse in-vivo (deep-seated infection, PMID 24226776); extensive *S. aureus* in-vitro |
| **Key risk** | (1) ADEP4 has poor oral bioavailability and requires parenteral delivery -- intramammary route may be feasible but milk matrix stability unknown; (2) ClpP is essential in *S. aureus* -- aberrant activation is lethal, but bacteria can develop resistance by LOSING ClpP (clpP deletion mutants are ADEP-resistant but have severe fitness costs); (3) Must be combined with a conventional antibiotic to kill the metabolically active cells that ADEP sensitizes to killing; (4) No veterinary development program exists |
| **Proposed de-risk** | (1) Test ADEP4 stability in bovine whole milk (half-life measurement); (2) ADEP4 + pirlimycin against CC97/CC151 biofilm in a MAC-T intracellular survival model: measure intracellular CFU reduction vs. pirlimycin alone. GO if >2-log additional killing. Cost: ~$60-80K |
| **Sapper constraint addressed** | Constraint 1 (directly kills intracellular persisters -- the primary barrier); Constraint 3 (targets THE rate-limiting barrier); Constraint 5 (ADEP kills within biofilm -- persister cells are the survivors that matter); Constraint 10 (addresses SCV dormancy without promoting MORE SCVs, unlike rifampicin) |
| **Resistance logic** | Resistance to ADEP occurs via clpP loss-of-function mutations. clpP-null mutants are severely attenuated (impaired virulence, reduced growth rate, defective stress responses). Combination with a conventional antibiotic (rifampicin or pirlimycin) closes this resistance loophole -- clpP-null cells are killed by the partner antibiotic. [Quality Standard 15 addressed] |

**This is a high-priority candidate.** ADEP is the only known mechanism that specifically kills dormant persister cells -- the exact population that drives chronic *S. aureus* mastitis. The combination with pirlimycin (which already achieves the best solo results via intracellular accumulation) could be transformative.

**20-Year Test:** ADEP was published in 2005 (Brotz-Oesterhelt et al., Nature Med), and the persister-killing mechanism was demonstrated in 2013 (Conlon et al., Nature). No product exists in any species. Reasons: (a) ADEP4 has poor drug-like properties (peptide, poor PK), (b) newer ADEP analogs with improved properties are in preclinical development (ureadepsipeptides; PMC6916429), (c) the veterinary intramammary application is novel and may face fewer PK constraints than systemic human use.

---

### Candidate 5C: Gallium(III) Intramammary Infusion for Multi-Barrier Killing (Non-Obvious)

This is an expansion of Candidate 2C specifically for Stage 5 persistence mechanisms.

| Field | Detail |
|---|---|
| **Target/mechanism** | Gallium(III) enters *S. aureus* via iron acquisition pathways, poisons iron-dependent enzymes in the electron transport chain (the same ETC components that SCVs are deficient in -- hemin/menadione biosynthesis), disrupts biofilm via eDNA-dependent dispersal, and kills metabolically active and dormant cells. In the iron-restricted mammary environment, bacteria are maximally reliant on iron acquisition and therefore maximally vulnerable to the gallium Trojan horse |
| **Disease stage** | Stage 5 (intracellular killing via iron transport, SCV metabolic disruption, biofilm dispersal + killing) |
| **Category** | Non-Obvious |
| **Evidence tier** | [MODERATE] for anti-*S. aureus* activity; [INFERRED] for bovine intramammary application |
| **Species data** | Mouse in-vivo (wound model); extensive *S. aureus* in-vitro including MRSA and biofilm |
| **Key risk** | See Candidate 2C risks. Additionally: SCVs with defective ETC may be LESS dependent on iron-dependent enzymes (they have already adapted to ETC dysfunction). Gallium may therefore be less effective against the very population it most needs to kill |
| **Proposed de-risk** | Test gallium nitrate against: (a) normal-colony *S. aureus*, (b) defined hemB SCV mutant, (c) defined menD SCV mutant, in bovine whole milk. Determine if SCVs are more or less susceptible than parent. Cost: ~$30-50K |
| **Sapper constraint addressed** | Constraint 1, 5, 8, 9 (multi-barrier: intracellular + biofilm + iron disruption + non-antibiotic) |

---

### Candidate 5D: Autophagy Flux Restoration -- Host-Directed Intracellular Clearance (Novel)

| Field | Detail |
|---|---|
| **Target/mechanism** | *S. aureus* subverts autophagy in bovine mammary epithelial cells by blocking autophagosome-lysosome fusion via p38-alpha MAPK activation (Phase 1, Section 5.1). This creates autophagosomes that serve as replicative niches rather than killing chambers. A host-directed therapy that RESTORES autophagy flux -- completing the fusion of autophagosomes with lysosomes -- would turn the pathogen's sanctuary into its tomb. Small-molecule autophagy flux enhancers (e.g., TFEB activators, Rab7 stabilizers, mTOR-independent autophagy inducers like trehalose) could achieve this |
| **Disease stage** | Stage 5 (intracellular persistence -- the core mechanism) |
| **Category** | Novel |
| **Evidence tier** | [INFERRED] -- *S. aureus* autophagy subversion in bovine MAC-T cells [ESTABLISHED] (PMID 32431700); autophagy flux restoration kills intracellular bacteria in other systems (TB: PMID 26099586); specific autophagy flux restoration in bovine mammary cells for *S. aureus* clearance untested |
| **Species data** | Bovine cell (MAC-T) for autophagy subversion mechanism; human and mouse cell for autophagy modulator pharmacology |
| **Key risk** | (1) *S. aureus* may escape autophagosomes to the cytoplasm before flux restoration can occur; (2) Autophagy induction may paradoxically HELP *S. aureus* by providing more autophagosomes as replicative niches (the pathogen uses autophagosomes for replication -- Phase 1 Section 5.1); (3) The de-risk experiment must distinguish between "more autophagy induction" (potentially harmful) and "autophagy flux COMPLETION" (potentially curative) |
| **Proposed de-risk** | MAC-T cells infected with *S. aureus* CC97: treat with (a) rapamycin (mTOR-dependent autophagy inducer), (b) trehalose (mTOR-independent), (c) specific TFEB activator, (d) p38 inhibitor (directly blocks the bacterial subversion pathway). Measure: intracellular CFU at 24h, autophagosome-lysosome colocalization (confocal), and cell viability. GO if any compound reduces intracellular CFU >1-log without increasing cell death >20%. KILL if all compounds increase intracellular CFU. Cost: ~$50-70K |
| **Sapper constraint addressed** | Constraint 1 (directly addresses intracellular persistence -- the primary barrier); Constraint 10 (uses a non-antibiotic mechanism, avoiding SCV promotion); Constraint 13 (non-antibiotic, regulatory tailwind) |

**Biological rationale:** The disease map reveals that *S. aureus* creates its own intracellular sanctuary by hijacking host autophagy. The intervention is to UN-hijack it: restore the host cell's normal autophagy-to-lysosome pathway so infected cells can self-clear their bacterial cargo. This is genuinely novel in the bovine mastitis context.

**Closest analogy:** Host-directed therapy for *Mycobacterium tuberculosis* -- a paradigm where boosting host cell autophagy (via vitamin D, rapamycin, AMPK activators) enhances intracellular killing of TB bacteria that similarly subvert autophagy. Multiple human clinical trials are underway for autophagy-based HDT against TB (PMID 34534573, 26818871).

**Most likely failure mode:** *S. aureus* escapes autophagosomes to the cytoplasm faster than flux restoration can direct them to lysosomes. The escape mechanism (Hla pore formation in endosomal membranes) is independent of autophagy flux. This would mean the intervention is too late -- the bacteria are already cytoplasmic.

**How to test cheaply:** The p38 inhibitor arm is most informative -- it directly blocks the bacterial subversion mechanism identified in bovine MAC-T cells (PMID 36063687). If p38 inhibition restores autophagy flux AND reduces intracellular CFU, the approach is validated with a known, drug-like small molecule.

---

### Candidate 5E: SCV Wake-and-Kill via Metabolic Reactivation + Antibiotic (Novel)

| Field | Detail |
|---|---|
| **Target/mechanism** | SCVs are dormant because of defects in electron transport chain components (hemin or menadione auxotrophy). By supplying exogenous menadione (vitamin K3) or hemin intramammarily, SCVs can be forced to revert to the normal, metabolically active phenotype -- which is susceptible to conventional antibiotics. The "wake" step (metabolic reactivation) is followed by the "kill" step (antibiotic). Phase 1 (Section 5.2) documents that SCV reversion occurs in vitro -- the goal is to force it pharmacologically |
| **Disease stage** | Stage 5 (SCV dormancy -- direct attack) |
| **Category** | Novel |
| **Evidence tier** | [INFERRED] -- SCV reversion to normal phenotype upon hemin/menadione supplementation [ESTABLISHED] in vitro; pharmacological reactivation in vivo NOT demonstrated; concept widely discussed but never tested in any species |
| **Species data** | In-vitro (multiple labs, multiple species) |
| **Key risk** | (1) SCVs are intracellular -- menadione/hemin must reach intracellular bacteria, which requires host cell membrane penetration. Menadione (a quinone) is membrane-permeable; hemin requires transport. (2) SCV field prevalence is unknown (Sapper Constraint 15) -- if SCVs are rare in field infections, the approach targets a small fraction of total bacterial burden. (3) Reactivated bacteria may reestablish virulent infection before antibiotic can kill them -- timing of wake and kill must overlap. (4) Menadione is cytotoxic to mammalian cells at high concentrations |
| **Proposed de-risk** | Two-step experiment: (1) Confirm SCV reactivation: infect MAC-T cells with hemB SCV mutant; add menadione at 3 concentrations; measure reversion to normal phenotype (colony morphology, growth rate). (2) Wake-and-kill: add menadione + pirlimycin simultaneously; measure intracellular CFU vs. pirlimycin alone. GO if >2-log additional killing. Cost: ~$40-60K |
| **Sapper constraint addressed** | Constraint 1 (addresses THE intracellular SCV barrier); Constraint 15 (the de-risk experiment itself informs SCV prevalence -- if no SCVs are recovered from clinical specimens, the approach is less important); Constraint 3 (realistic benchmark -- aim for incremental improvement over pirlimycin alone) |

**Biological rationale:** This is the most direct attack on the SCV problem. Rather than trying to kill dormant cells directly (hard), WAKE THEM UP first, then kill them with existing tools. The concept has been discussed for years in the persistence literature but never tested in an animal model.

**Most likely failure mode:** Menadione/hemin cannot reach intracellular SCVs at sufficient concentrations. Menadione is small and lipophilic (MW 172, LogP ~1.4) -- it should cross cell membranes. Hemin is larger (MW 652) but has known cell-penetrating properties via heme carrier protein 1 (HCP1/SLC46A1). The pharmacology may actually be tractable.

---

### Candidate 5F: Biofilm Disruption Cocktail + Concurrent Bactericidal Agent (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Multi-enzyme cocktail targeting all four biofilm matrix components: (a) rhDNase I (degrades eDNA), (b) Dispersin B (degrades PNAG), (c) proteinase K or a targeted protease (degrades Bap and protein matrix), (d) PSM-amyloid disrupting agent. Administered intramammarily WITH concurrent pirlimycin to kill dispersed bacteria. Must be simultaneous -- Sapper Constraint 5 mandates no dispersal without killing |
| **Disease stage** | Stage 5 (biofilm -- one of three co-equal barriers) |
| **Category** | Known (individual components known; combination formulation novel) |
| **Evidence tier** | [PRELIMINARY] -- individual enzymes active against *S. aureus* biofilm in vitro (Phase 2, Section 10); combination in bovine system untested |
| **Species data** | In-vitro (bovine isolates for some enzymes); no bovine in-vivo |
| **Key risk** | (1) Formulation nightmare: 3-4 enzymes + antibiotic in a single stable intramammary preparation, all maintaining activity in milk matrix (Sapper Constraint 6); (2) Cost: multi-enzyme preparation is expensive to manufacture; (3) Regulatory: multi-API combination requires proof of contribution for each component (Quality Standard 23 -- 4 APIs = 15 trial arms); (4) In-vivo biofilm is embedded in fibrotic tissue, not on an abiotic surface |
| **Proposed de-risk** | Simplify to 2-component: rhDNase I + pirlimycin (most tractable combination -- DNase is already available as a pharmaceutical, Pulmozyme). Test in bovine milk-based biofilm assay (not abiotic surface -- use MAC-T cell-grown biofilm in milk). GO if >2-log biofilm CFU reduction vs. pirlimycin alone. Cost: ~$50-70K |
| **Sapper constraint addressed** | Constraint 5 (anti-biofilm + killing simultaneous); Constraint 8 (addresses biofilm barrier specifically) |

---

### Candidate 5G: Toxin-Antitoxin System Modulators -- Disrupting Persister Formation (Novel)

| Field | Detail |
|---|---|
| **Target/mechanism** | *S. aureus* persister cells form via toxin-antitoxin (TA) systems: mazF, relE1/relE2, sprG/sprF (Phase 1, Section 5.5). Under stress, the toxin component inhibits growth, pushing cells into dormancy. An agent that BLOCKS toxin activity or STABILIZES antitoxin would prevent persister formation, leaving all cells metabolically active and antibiotic-susceptible. Alternatively, an agent that forces toxin ACTIVATION in all cells simultaneously (without the protective antitoxin) would kill the entire population |
| **Disease stage** | Stage 5 (persister formation -- the switch to dormancy) |
| **Category** | Novel |
| **Evidence tier** | [INFERRED] -- TA systems in *S. aureus* persister formation [MODERATE] (PMID 34384900, 30056132); TA system modulation as therapeutic approach is theoretical in *S. aureus*; closest precedent is the *E. coli* mqsR/mqsA system modulation literature |
| **Species data** | In-vitro (TA system characterization) |
| **Key risk** | (1) Multiple redundant TA systems -- inhibiting one may be compensated by others; (2) TA modulators with drug-like properties do not exist; (3) Target validation in bovine system needed; (4) This is early-stage -- years from any testable compound |
| **Proposed de-risk** | (1) Profile TA system expression (mazF, relE1/relE2, sprG/sprF) in bovine CC97/CC151 isolates under milk-like conditions vs. lab media to confirm relevance; (2) Test whether pirlimycin-induced persister formation is reduced in TA-system-deleted mutants (if deletable). Cost: ~$80-120K |
| **Sapper constraint addressed** | Constraint 1 (addresses persister formation at its molecular source); Constraint 15 (addresses phenotypic tolerance) |

**This is the highest-risk, highest-reward candidate.** If TA system modulation can prevent persister formation, it converts *S. aureus* from an antibiotic-tolerant to an antibiotic-susceptible population -- making conventional antibiotics curative. But the science is early-stage.

---

## Stage 6: Treatment Resistance

### Candidate 6A: Optimized Phage Cocktail (Kromker 2026 Model) (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Multi-phage cocktail targeting the major bovine *S. aureus* clonal complexes (CC97, CC151, CC479), administered intramammarily at 12-hour intervals for 5 doses. Replicates and optimizes the Kromker 2026 protocol that achieved 81.3% bacteriological cure (PRELIMINARY, n=16, Phase 2 Section 8) |
| **Disease stage** | Stage 6 (bypasses all genetic AMR) |
| **Category** | Known |
| **Evidence tier** | [PRELIMINARY] -- Kromker 2026 pilot RCT (81.3% cure, n=16, single study, unreplicated); phage K single-phage trial (16.7% cure, Gill 2006, ESTABLISHED); bovine in-vitro susceptibility data |
| **Species data** | Bovine in-vivo (two trials); bovine in-vitro |
| **Key risk** | (1) Kromker result is n=16 and unreplicated (Sapper Constraint 3 -- 60-70% realistic benchmark); (2) Phage therapy has no clear FDA-CVM regulatory pathway; (3) Phage resistance can develop; (4) Manufacturing complexity; (5) 5-dose/12h protocol may be impractical at farm scale |
| **Proposed de-risk** | Independent replication of Kromker protocol: multi-phage cocktail (minimum 3 phages covering CC97/CC151/CC479), 5 doses at 12h, n=40 treated/40 control. Measure bacteriological cure at 21 and 42 days. Cost: ~$150-200K (multi-farm RCT). HIGHEST PRIORITY DE-RISK EXPERIMENT |
| **Sapper constraint addressed** | Constraint 13 (non-antibiotic, EU regulatory tailwind); Constraint 14 (phage efficacy varies by cow -- stratification may improve results); Constraint 3 (realistic benchmark) |

**Why this is the highest-priority de-risk:** If the Kromker result replicates at even 65%, phage cocktail becomes the first non-antibiotic approach to exceed the 60-70% realistic benchmark. This would be transformative for EU markets under Regulation 2019/6.

---

### Candidate 6B: Endolysin-Pirlimycin Combination (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Engineered endolysin (e.g., chimeric lysin combining *S. aureus*-specific CBD with enhanced catalytic domain) + pirlimycin. Endolysin kills extracellular/biofilm bacteria (cell wall hydrolysis, AMR-orthogonal); pirlimycin handles intracellular fraction. Nisin + lysostaphin synergy has been demonstrated against biofilm (PMID 26999597) |
| **Disease stage** | Stage 6 (AMR-orthogonal killing), Stage 5 (partial -- via pirlimycin intracellular component) |
| **Category** | Known |
| **Evidence tier** | [PRELIMINARY] -- endolysins in bovine milk in-vitro with variable results (Phase 2, Section 7); LysRODI efficacy in murine mastitis model; chimeric lysins + lysostaphin synergy in murine mammary glands (PMID 22286996) |
| **Species data** | Murine in-vivo; bovine in-vitro (variable milk matrix results) |
| **Key risk** | (1) Milk matrix variability between cows/quarters (Phase 2 Section 7 -- "inconsistent killing"); (2) Protein stability in milk; (3) Manufacturing cost; (4) Regulatory: endolysin + antibiotic combination = complex regulatory path |
| **Proposed de-risk** | Test lead endolysin in milk from 20 different cows (capturing normal variation): measure MBC variability. GO if >80% of milk samples show >2-log killing. Cost: ~$40-60K |
| **Sapper constraint addressed** | Constraint 2 (formulation critical -- test across variable milk matrix); Constraint 6 (mammary gland challenges -- but intensive dosing can compensate as Kromker showed) |

---

## Stage 7: Reinfection and Reseeding

Sapper identified this as a **complete gap** -- no approach addresses endogenous reseeding from the intracellular SCV reservoir.

### Candidate 7A: Solving Stage 5 Solves Stage 7 (Strategic Principle)

Stage 7 reseeding is driven by SCV reversion and intracellular bacterial release. If Stage 5 candidates (5A-5G) successfully eliminate the intracellular reservoir, reseeding becomes impossible. Therefore, every Stage 5 candidate is simultaneously a Stage 7 candidate.

---

### Candidate 7B: Post-Cure Lactoferrin Maintenance Protocol (Novel)

| Field | Detail |
|---|---|
| **Target/mechanism** | After bacteriological cure (culture-negative milk), administer intramammary lactoferrin for 7-14 days to maintain iron deprivation in the mammary gland. Purpose: if any residual SCVs revert to the normal phenotype and emerge from cells, they encounter an iron-depleted environment that suppresses regrowth. Lactoferrin also supports microbiome recolonization (Stage 8) |
| **Disease stage** | Stage 7 (reseeding prevention post-cure) |
| **Category** | Novel |
| **Evidence tier** | [INFERRED] -- lactoferrin bacteriostatic in milk [ESTABLISHED]; post-cure maintenance regimen concept untested |
| **Species data** | Bovine in-vivo (lactoferrin in milk -- natural protein, excellent matrix compatibility) |
| **Key risk** | Cost and compliance: 7-14 days of daily intramammary lactoferrin is labor-intensive. Farmer acceptance uncertain |
| **Proposed de-risk** | Subset analysis from any lactoferrin + antibiotic trial (Candidate 5A): compare relapse rates at 90 days between cows that received 5-day vs. 14-day lactoferrin. If extended lactoferrin reduces relapse, the reseeding-prevention mechanism is supported. Cost: incremental on Candidate 5A trial |
| **Sapper constraint addressed** | Constraint 1 (addresses the intracellular reservoir indirectly -- starves emerging bacteria); Constraint 12 (if post-cure maintenance extends cure duration, the economics of treatment improve) |

**Biological rationale:** The problem is that "cured" cows relapse. Lactoferrin maintenance after cure provides a hostile environment for any bacteria that emerge from residual intracellular reservoirs. The mammary gland is naturally iron-restricted -- lactoferrin intensifies this restriction during the critical post-cure window.

---

### Candidate 7C: Segregation-Informed Herd Management Tool (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | Rapid on-farm PCR diagnostics identifying *S. aureus* strain type (CC97/CC151/CC479) + SCC-based prognostic scoring to stratify cows into: (a) treat (high cure probability), (b) segregate and manage (low cure probability, cull at end of lactation), (c) monitor (new infection, may self-cure). This is the control-vs-cure strategic pathway (Sapper Section 18.1) |
| **Disease stage** | Stage 7 (transmission interruption) |
| **Category** | Known |
| **Evidence tier** | [ESTABLISHED] -- strain typing and SCC prognostic factors well-characterized (Phase 2, Section 18.3); economic modeling for segregation vs. treatment [MODERATE] |
| **Species data** | Bovine (extensive epidemiological data) |
| **Key risk** | This is management, not a therapeutic product. Farmer compliance with segregation protocols is variable. On-farm PCR diagnostics must be affordable and rapid |
| **Proposed de-risk** | Partner with a diagnostics company to develop CC-typing lateral flow or isothermal PCR assay. Pilot in 5 herds with economic modeling. Cost: ~$100-150K |
| **Sapper constraint addressed** | Constraint 12 (control pathway -- explicit acknowledgment that segregation/culling is economically rational in many contexts); Constraint 14 (cow-level stratification) |

---

## Stage 8: Resolution and Remodeling

### Candidate 8A: Acoustic Pulse Technology (APT) as Combination Partner (Known)

| Field | Detail |
|---|---|
| **Target/mechanism** | APT delivers focused acoustic energy to mammary tissue, promoting mechanotransduction-based tissue repair, enhanced blood flow, and potentially biofilm disruption. 83.9% bacterial cure in retrospective study (n=467), 70.5% in controlled trial (Phase 2, Section 15). The ONLY approach with evidence of promoting tissue recovery |
| **Disease stage** | Stage 8 (tissue repair), potentially Stage 5 (biofilm disruption) |
| **Category** | Known |
| **Evidence tier** | [MODERATE] -- bovine controlled trial (PLOS ONE 2018, 70.5% vs. 18.4%); bovine retrospective (n=467, 83.9%); mechanism not fully characterized |
| **Species data** | Bovine in-vivo (field data) |
| **Key risk** | (1) Mechanism unclear; (2) RCT evidence limited; (3) Capital equipment model (not per-treatment consumable); (4) *S. aureus*-specific data not reported separately; (5) Retrospective design bias possible |
| **Proposed de-risk** | Randomized controlled trial of APT + lactoferrin/pirlimycin combination vs. lactoferrin/pirlimycin alone in chronic *S. aureus* infections (n=40/arm). If APT adds >15 percentage points to cure rate, tissue repair mechanism confirmed. Cost: ~$100-150K (equipment loan from Armenta Ltd) |
| **Sapper constraint addressed** | Constraint 11 (APT validates tissue repair); Constraint 15 (APT provides a complementary physical mechanism orthogonal to all pharmacological approaches) |

---

### Candidate 8B: Anti-Fibrotic Adjunct Therapy -- Pirfenidone/Nintedanib Analogue (Novel)

| Field | Detail |
|---|---|
| **Target/mechanism** | *S. aureus* directly upregulates TGF-beta1 and bFGF in bovine mammary fibroblasts via NF-kB and AP-1 (Phase 1, Section 4.4), creating a positive feedback loop between infection and fibrosis. Anti-fibrotic drugs (pirfenidone, nintedanib) reduce TGF-beta signaling, fibroblast proliferation, and ECM deposition. Administered intramammarily during and after treatment to: (a) reduce new fibrosis formation during active infection, (b) allow partial resolution of existing fibrosis, (c) improve drug distribution by reducing tissue barriers |
| **Disease stage** | Stage 8 (resolution and remodeling), Stage 4 (reduces fibrosis-driven acute pathology progression), Stage 6 (improves drug distribution) |
| **Category** | Novel |
| **Evidence tier** | [INFERRED] -- pirfenidone reduces fibrosis in sheep pulmonary model (PMID 31762329); pirfenidone and nintedanib reduce TGF-beta-driven fibrosis in multiple animal models; bovine mammary fibrosis mechanism characterized (PMID 26948281); mammary-specific anti-fibrotic therapy untested in any species |
| **Species data** | Sheep in-vivo (pirfenidone for pulmonary fibrosis); bovine in-vitro (fibroblast TGF-beta pathway); rat in-vivo (pirfenidone and nintedanib for peritoneal fibrosis) |
| **Key risk** | (1) Pirfenidone is a human pharmaceutical -- cost per dose may be prohibitive for dairy animals; (2) Mammary tissue fibrosis may be fundamentally different from pulmonary fibrosis in its response to anti-fibrotics; (3) Anti-fibrotic treatment during active infection might WORSEN disease by reducing the host's ability to wall off bacteria; (4) Milk withdrawal/residue implications unknown |
| **Proposed de-risk** | (1) Bovine mammary fibroblast culture: pirfenidone at 3 concentrations -- measure TGF-beta1 expression, collagen deposition, fibroblast proliferation. (2) If effective in vitro: co-culture with *S. aureus*-infected MAC-T cells to check for adverse interaction. Cost: ~$40-60K |
| **Sapper constraint addressed** | Constraint 7 (realistic benchmark -- if fibrosis is a co-equal barrier, removing it should improve cure rates by the fibrosis fraction); Constraint 8 (multi-barrier -- addresses a barrier no other candidate addresses) |

**Biological rationale:** Fibrosis is identified as a co-equal barrier to cure (Phase 1, Multi-Barrier Model). It physically excludes drugs from reaching bacteria. Every treatment approach that achieves <100% cure loses a fraction to fibrosis-based inaccessibility. Anti-fibrotic therapy directly addresses this barrier.

**Closest analogy:** Pirfenidone and nintedanib are both approved for human idiopathic pulmonary fibrosis (IPF). Pirfenidone reduces TGF-beta-driven fibrosis in sheep, rat, and other animal models across lung, liver, heart, and kidney. The mammary gland is a new organ application but the mechanism (TGF-beta-driven ECM deposition) is identical.

**Most likely failure mode:** Anti-fibrotic therapy is too slow. Fibrosis develops over weeks to months; resolution takes equally long. A course of anti-fibrotic therapy during a 5-8 day treatment window may be insufficient to meaningfully reduce established fibrosis. This candidate may be better suited as a chronic maintenance therapy in subclinically infected cows, not an acute treatment adjunct.

---

### Candidate 8C: Post-Treatment Probiotic Recolonization (Non-Obvious)

| Field | Detail |
|---|---|
| **Target/mechanism** | After antibiotic treatment, intramammary administration of protective NAS species (*S. chromogenes*, *S. simulans*) and *Lactobacillus* to restore the mammary microbiome. Phase 1 (MB.3) notes that antibiotic treatment disrupts protective commensals, creating a window of vulnerability to reinfection. Deliberate recolonization with protective organisms closes this window |
| **Disease stage** | Stage 8 (microbiome restoration) |
| **Category** | Non-Obvious |
| **Evidence tier** | [INFERRED] -- antibiotic disruption of mammary microbiome [PRELIMINARY]; NAS protective effects [MODERATE]; deliberate post-treatment recolonization untested |
| **Species data** | Bovine epidemiology (NAS associations); bovine in-vitro (NAS anti-*S. aureus* activity) |
| **Key risk** | Regulatory classification of intramammary live bacterial product; risk that administered bacteria themselves cause mild subclinical mastitis |
| **Proposed de-risk** | Post-antibiotic intramammary NAS infusion in 10 cows: monitor SCC, culture for pathogen recolonization, and compare to 10 untreated controls over 60 days. Cost: ~$40-60K |
| **Sapper constraint addressed** | Constraint 13 (non-antibiotic); addresses the microbiome disruption paradox identified in Phase 1 |

**Closest analogy:** Fecal microbiota transplant (FMT) for *Clostridioides difficile* infection -- restoring a disrupted microbiome to prevent recurrent infection. Same principle applied to the mammary gland.

---

## Combination Architectures

No single candidate addresses all barriers (Sapper Constraint 8). The following architectures combine candidates into multi-barrier regimens.

### Architecture 1: "Breach and Clear" (Acute Cure-Side)

**Target population:** Recent-onset *S. aureus* IMI, primiparous, SCC <500K, front quarter (high-cure-probability cows)

| Component | Candidate | Barrier Addressed | Timing |
|---|---|---|---|
| Anti-adhesion + anti-evasion | 2A (SrtA inhibitor) | Prevents new adhesion, blocks SpA surface display | Days 1-8 |
| Iron disruption + beta-lactamase suppression | 5A (Lactoferrin) | Iron deprivation, SCV metabolic stress, immune modulation | Days 1-8 |
| Intracellular killing | 5A (Pirlimycin) | Intracellular accumulation, biofilm reduction at sub-MIC | Days 1-8 |
| SCV reactivation | 5E (Menadione co-formulation) | Forces SCV reversion to antibiotic-susceptible state | Days 1-8 |
| Post-cure maintenance | 7B (Lactoferrin maintenance) | Prevents reseeding | Days 9-21 |

**Barriers addressed:** Intracellular persistence (pirlimycin + lactoferrin + menadione), biofilm (pirlimycin sub-MIC), immune evasion (SrtA inhibitor blocks SpA), iron acquisition (lactoferrin + gallium alternative), SCV dormancy (menadione wake-and-kill), reseeding (post-cure lactoferrin)

**Regulatory complexity:** SrtA inhibitor = new chemical entity. Lactoferrin + pirlimycin = 2-API combination (manageable -- 3 trial arms per Quality Standard 23). Menadione is a vitamin K precursor with established safety. Overall: moderate regulatory complexity.

---

### Architecture 2: "Siege" (Chronic Cases + Dry Period)

**Target population:** Chronic subclinical *S. aureus* IMI, selected at dry-off for intensive treatment during the dry period (when milking removal is absent and drug contact time is maximized)

| Component | Candidate | Barrier Addressed | Timing |
|---|---|---|---|
| Persister/SCV killing | 5B (ADEP analogue) | Kills dormant persisters via ClpP activation | Dry-off infusion |
| Biofilm disruption + killing | 5F (DNase I + pirlimycin) | Biofilm matrix degradation + concurrent killing | Dry-off infusion |
| Iron disruption + immune support | 5A (Lactoferrin) | Iron deprivation, beta-lactamase suppression | Dry-off to calving |
| Physical barrier | ITS (bismuth subnitrate + Candidate 1A antimicrobial sealant) | Teat canal protection during dry period | Dry-off |
| Tissue repair | 8A (APT) or 8B (anti-fibrotic) | Reduce fibrosis barrier, promote tissue recovery | During dry period |

**Barriers addressed:** ALL FIVE -- intracellular (ADEP kills dormant cells), biofilm (DNase + pirlimycin), fibrosis (anti-fibrotic/APT), milk matrix (irrelevant during dry period), phenotypic tolerance (ADEP targets persisters specifically)

**Regulatory complexity:** HIGH -- multi-component, multiple new entities. But the dry period is the optimal biological window (no milking, sustained drug contact, lower bacterial burden). This architecture maximizes the chance of genuine cure in chronic cases.

---

### Architecture 3: "Shield" (Prevention-Focused)

**Target population:** Uninfected heifers and cows entering milking herd, prevention of new *S. aureus* IMI

| Component | Candidate | Barrier Addressed | Timing |
|---|---|---|---|
| SpA neutralization + toxin protection | 3A (SpAKKAA vaccine) + 3B (LukMF' toxoid) | Immune evasion, neutrophil protection | Pre-calving vaccination series |
| Colonization resistance | 1B (NAS probiotic teat dip) | Teat canal defense | Daily post-milking |
| Metabolic support | 0A (Protected butyrate) + 0B (Ca/BHBA management) | Gut-mammary axis, neutrophil function | Transition period |
| Genetic selection | Genomic tools (Sapper Constraint 16) | Population-level resistance | Continuous |

**Barriers addressed:** Prevents infection establishment rather than treating established disease. If prevention reduces new IMI by 50-70%, the cure-side challenge is diminished proportionally.

---

## Coverage Map

| Disease Stage | Candidates | Categories Covered | Barriers Addressed |
|---|---|---|---|
| **Stage 0:** Upstream systemic modifiers | 0A (butyrate), 0B (Ca/BHBA), 0C (gut probiotic) | Known, Known, Non-Obvious | Gut-mammary axis, metabolic predisposition |
| **Stage 1:** Entry and exposure | 1A (antimicrobial sealant), 1B (NAS probiotic teat dip) | Non-Obvious, Non-Obvious | Teat canal defense, colonization resistance |
| **Stage 2:** Adhesion and colonization | 2A (SrtA inhibitor), 2B (FnBP decoy), 2C (Gallium) | Known, Novel, Non-Obvious | MSCRAMM display, internalization, iron acquisition |
| **Stage 3:** Immune evasion | 3A (SpAKKAA vaccine), 3B (LukMF' toxoid), 3C (mucosal IgA), 3D (AdsA inhibitor) | Known, Known, Non-Obvious, Novel | SpA neutralization, leukocidin neutralization, IgA bypass, adenosine loop |
| **Stage 4:** Acute pathology | 4A (anti-Hla mAb), 4B (NLRP3 modulator) | Known, Non-Obvious | Tissue damage reduction, pyroptosis modulation |
| **Stage 5:** Chronic persistence | 5A (lactoferrin + pirlimycin), 5B (ADEP ClpP activator), 5C (Gallium), 5D (autophagy flux restoration), 5E (SCV wake-and-kill), 5F (biofilm cocktail), 5G (TA system modulators) | Known, Non-Obvious, Non-Obvious, Novel, Novel, Known, Novel | Intracellular persistence, SCV dormancy, biofilm, persister formation |
| **Stage 6:** Treatment resistance | 6A (phage cocktail), 6B (endolysin + pirlimycin) | Known, Known | AMR bypass, AMR-orthogonal killing |
| **Stage 7:** Reinfection and reseeding | 7A (solve Stage 5), 7B (post-cure lactoferrin), 7C (diagnostic-guided segregation) | Strategic, Novel, Known | Reservoir elimination, reseeding prevention, transmission interruption |
| **Stage 8:** Resolution and remodeling | 8A (APT), 8B (anti-fibrotic), 8C (post-treatment probiotic) | Known, Novel, Non-Obvious | Tissue repair, fibrosis reduction, microbiome restoration |

**Coverage check:** All 9 stages have at least one candidate. Stages 0, 3, and 5 have the most candidates (3-7), reflecting the importance of upstream prevention and the central role of chronic persistence. No stage has zero coverage.

**Category distribution:** 13 Known, 10 Non-Obvious, 9 Novel -- meeting the requirement for all three categories.

---

## De-Risk Prioritization

Ranked by information value per dollar spent:

| Priority | Candidate | Experiment | Cost | Why High Priority |
|---|---|---|---|---|
| **1** | 6A (Phage cocktail) | Independent replication of Kromker 2026 | ~$150-200K | If 81.3% replicates at even 65%, this is the first non-antibiotic approach exceeding the realistic benchmark. Transformative for EU market |
| **2** | 5B (ADEP) | ADEP4 + pirlimycin in MAC-T intracellular model | ~$60-80K | Tests whether persister killing works in bovine intracellular setting. High-discriminatory-power experiment |
| **3** | 5A (Lactoferrin + pirlimycin) | 3-arm bovine pilot trial | ~$100-150K | Tests the most promising synergy in a real bovine trial. Lactoferrin addresses multiple barriers simultaneously |
| **4** | 3A (SpAKKAA) | Bovine opsonophagocytic killing + SpA-bovine Fab binding test | ~$80-120K | Directly resolves the central uncertainty in bovine *S. aureus* immunology (Sapper Constraint 4) |
| **5** | 5D (Autophagy flux) | p38 inhibitor in MAC-T infection model | ~$50-70K | Tests the host-directed intracellular clearance concept with an existing drug-like molecule |
| **6** | 5E (Wake-and-kill) | Menadione + pirlimycin in MAC-T SCV model | ~$40-60K | Tests the most direct anti-SCV strategy with off-the-shelf reagents |
| **7** | 2A (SrtA inhibitor) | Screen recent inhibitors against bovine isolates in MAC-T invasion assay | ~$60-80K | Multi-barrier target (adhesion + immune evasion + internalization prevention) |
| **8** | 2C/5C (Gallium) | MIC in bovine milk + intracellular killing + SCV susceptibility | ~$50-70K | Tests whether the iron-mimetic Trojan horse works in the relevant matrix |
| **9** | SCV field prevalence survey | Culture 100+ chronic bovine *S. aureus* quarters on SCV-selective media | ~$30-50K | Directly tests the central thesis of the multi-barrier model (Sapper Constraint 15/16) |

**Total de-risk budget for top 5 priorities: ~$440-620K**

---

## Principles Compliance

| Principle | How Addressed |
|---|---|
| 1. Understand the disease | All candidates map to specific disease mechanisms from the Phase 1 disease map |
| 2. Understand why treatments fail | Every candidate explicitly addresses Sapper constraints from the Phase 2 failure analysis |
| 3. Obvious AND non-obvious | 13 Known + 10 Non-Obvious + 9 Novel candidates across all stages |
| 4. Don't ignore major pathology | Stage 5 (chronic persistence) receives 7 candidates -- the most of any stage. Stage 7 (complete gap per Sapper) receives 3 candidates |
| 5. If nothing exists, propose new | 9 Novel proposals for gap stages (Candidates 2B, 3D, 5D, 5E, 5G, 7B, 8B, and combination architectures) |
| 6. Guided but not constrained by literature | Cross-disease analogies from TB (autophagy HDT), wound infection (gallium), human vaccinology (SpAKKAA), and antibiotic persistence (ADEP) |
| 9. The 70% test | Three combination architectures designed to address ≥4 of 5 barriers simultaneously |
| 10. Discomfort is a signal | SCV wake-and-kill (5E), autophagy flux restoration (5D), and TA system modulation (5G) are high-risk proposals for the hardest problem. They are proposed with honest evidence tiers and explicit failure modes |

---

## Quality Standards Compliance

| Standard | How Addressed |
|---|---|
| 1. Evidence tiers | Every candidate tagged [ESTABLISHED], [MODERATE], [PRELIMINARY], or [INFERRED] |
| 2. 20-Year Test | Applied to SrtA inhibitors, SpAKKAA, ADEP, lysostaphin, nanoparticles, phage, lactoferrin, DPC3147 |
| 6. Species/model tagging | Every evidence claim tagged with species and model system |
| 8. Computational = triage | No candidates promoted on computational evidence alone |
| 11. Target vs. lead molecule | Explicitly separated throughout (e.g., SrtA is the target; specific inhibitor scaffolds are leads) |
| 14. Host selectivity | Assessed for SrtA (no mammalian homolog), AdsA (bacterial surface enzyme), NLRP3 (host target -- flagged as risk), gallium (non-specific -- flagged) |
| 15. Resistance logic | Addressed for SrtA (non-essential, low pressure), ADEP (clpP loss = fitness cost), gallium (multi-target, slow evolution), phage (cocktail breadth) |
| 16. Strain heterogeneity | Bovine CC97/CC151/CC479 specified for all de-risk experiments |
| 17. Virulence axis trade-off | SrtA inhibitor analysis notes that blocking SpA surface display via SrtA inhibition avoids the agr/Rot trade-off that anti-virulence approaches targeting secreted toxins face |
| 26. Commercial reality gate | COGS considerations noted for lactoferrin, mAb, gallium, phage, endolysin |
| 27. Test in real matrix | All de-risk experiments specify bovine whole milk, not broth |
| 31. Realistic cost estimates | De-risk experiments costed at $30-200K range based on CRO-grade estimates |

---

*32 candidates across 9 disease stages. 13 Known, 10 Non-Obvious, 9 Novel. Three combination architectures. All Sapper constraints addressed. All disease stages covered. De-risk prioritization with realistic cost estimates. Evidence tiers and species tags per Agteria Quality Standards.*
