# Phase 3 -- Treatment Candidates: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Agent:** Forge (The Inventor)
**Date:** 2026-03-27
**Status:** Complete

---

## Executive Summary

Twenty-eight candidates across all disease stages, organized around the Tribunal's Gate 2 bottleneck determination. The portfolio center is leukotoxin (LktA) -- decomposed into six molecular intervention points from transcription to downstream signaling. Fusogard proves the TARGET is right; every Gate 2 candidate below is designed to solve the APPROACH failures (insufficient titer, wrong localization, no durability) that Fusogard exposed.

**Portfolio architecture:**
- **Gate 2 core (14 candidates):** LktA lifecycle interventions (transcription, secretion, extracellular neutralization, receptor blockade, downstream protection, complement evasion) -- these are the portfolio backbone
- **Gate 1 supporting (8 candidates):** Inoculum reduction approaches that lower the bacterial load arriving at the liver, designed as COMBINATION PARTNERS for Gate 2 targets, not standalone products
- **Post-Gate 2 / polymicrobial (4 candidates):** Early abscess disruption, anti-synergy, and diagnostic
- **Combination products (2 candidates):** Integrated Gate 1 + Gate 2 systems

**Key constraint from failure analysis:** No Gate 1-only intervention has EVER reduced liver abscess incidence as a standalone. Every candidate below that acts at Gate 1 is positioned as a combination component with a Gate 2 partner. The portfolio passes the 70% test ONLY through Gate 2 coverage.

---

## Disease Stage Coverage Map

| Disease Stage | Gate | # Candidates | Primary Candidates |
|---|---|---|---|
| Stage 1: Acidosis/rumenitis | Gate 0 | 2 | Butyrate zinc (G1-3), Monensin companion (existing) |
| Stage 2: Rumen wall colonization | Gate 1 | 4 | Anti-hemagglutinin vaccine (G1-1), phage cocktail (G1-2), anti-43K OMP (G1-4) |
| Stage 3: Portal transit / complement evasion | Gate 1-2 | 2 | Anti-Factor H binding (G2-8), complement enhancement (G2-9) |
| Stage 4: Hepatic immune evasion (BOTTLENECK) | Gate 2 | 8 | mAb anti-LktA (G2-1), mRNA LktA vaccine (G2-2), epitope-focused subunit (G2-3), LktB secretion inhibitor (G2-4), lktA transcription suppressor (G2-5), receptor decoy (G2-6), Kupffer cell trained immunity (G2-7), anti-NET evasion (G2-10) |
| Stage 5: Abscess formation (pre-encapsulation) | Post-G2 | 2 | Anti-stellate cell activation (PG-1), early detection biomarker (PG-4) |
| Stage 6: Chronic persistence | Irreversible | 1 | Biofilm disruption (PG-2) -- low priority |
| Stage 7: Continuous reseeding / polymicrobial | Recurring | 2 | Anti-T. pyogenes synergy (PG-3), hindgut-targeted intervention (G1-5) |
| Hindgut pathway | Alt Gate 1 | 1 | Hindgut-targeted Bacteroides/FNF suppression (G1-5) |
| **Combination products** | G1+G2 | 2 | mAb + phage (COMBO-1), mRNA vaccine + anti-adhesion (COMBO-2) |

---

## GATE 2 CANDIDATES: The Portfolio Core

### Leukotoxin Lifecycle -- Six Molecular Intervention Points

```
lktBAC operon transcription --> LktA translation --> LktC post-translational modification(?)
    --> LktB-mediated secretion --> Extracellular LktA --> Receptor binding on bovine PMN/Kupffer
        --> Downstream intracellular cascade (apoptosis/necrosis)

Each step = a separate intervention target.
```

---

### G2-1: Anti-LktA Monoclonal Antibody (Passive Immunization)

**Target/mechanism:** Extracellular neutralization of secreted LktA protein in the hepatic sinusoidal space. Antibody binds LktA and prevents receptor engagement on Kupffer cells and neutrophils.

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2

**Category:** Non-obvious (cross-species translation: veterinary mAb platform)

**Evidence tier:** MODERATE

**Species data:** No anti-LktA mAb has been tested in cattle for passive protection. However: (1) Elanco's canine parvovirus monoclonal antibody (CPMA) is the first commercially approved veterinary mAb, proving the platform works in production animals. (2) Elanco is investing $130M to expand mAb manufacturing in Elwood, Kansas, with 10+ mAb pipeline projects. (3) Polyclonal anti-leukotoxin serum is protective in challenge models (Saginala 1997: 80% protection). (4) A leukotoxin-specific monoclonal antibody already exists as a research tool (used in sandwich ELISA for LktA quantification -- Pillai 2021).

**Biological rationale:** The Fusogard failure analysis shows the target is right but the vaccine approach generates insufficient sinusoidal antibody titers on high-grain diets. A monoclonal antibody bypasses the vaccine problem entirely -- you DELIVER the neutralizing antibody directly rather than relying on the host immune system to produce it. This guarantees titer, controls dosing, and eliminates the immunogenicity variable. The Elanco CPMA precedent shows single-injection mAb delivery achieves therapeutic concentrations for 2-3 weeks in dogs. The question is whether a single mAb injection (or periodic dosing) can maintain neutralizing concentrations in the hepatic sinusoid for the 120-400 day feeding period.

**Key risk:** Duration of protection. A single mAb injection provides 2-4 weeks of circulating antibody. The feeding period is 120-400 days. Options: (a) long-acting formulation (PEGylation, Fc engineering for extended half-life -- FcRn recycling extends bovine IgG1 half-life to ~21 days), (b) repeated injections (2-3 doses during feeding period), (c) combination with a vaccine (mAb for immediate protection during high-risk adaptation, vaccine for sustained immunity thereafter).

**Proposed de-risk:** $15-18K. Ex vivo bovine liver perfusion (Prediction T2 design): perfuse slaughterhouse livers with F. necrophorum +/- anti-LktA monoclonal antibody at defined concentrations. Measure clearance threshold shift. If mAb raises clearance threshold by >=1 log, proceed to in vivo.

**Why this beats Fusogard:** Guaranteed titer. No dependence on host immunogenicity. Dose-controllable. Leverages Elanco's $130M mAb platform directly.

**Elanco fit:** Direct alignment with their mAb manufacturing expansion. CPMA demonstrates regulatory pathway. Benchmark database (68,000 feedlots) enables rapid field trial design.

---

### G2-2: mRNA-LNP Leukotoxin Vaccine (Next-Generation Active Immunization)

**Target/mechanism:** Endogenous production of LktA antigen fragments by host cells, generating high-titer neutralizing anti-LktA antibodies AND T-cell responses. mRNA encoding immunodominant LktA epitopes (identified by Xiao et al.) delivered in lipid nanoparticles (LNPs).

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2

**Category:** Non-obvious (platform translation from human/H5N1 to liver abscess)

**Evidence tier:** PRELIMINARY (platform validated in cattle for H5N1; not tested for LktA)

**Species data:** Elanco-Medgene H5N1 mRNA vaccine for dairy cattle is in USDA final review for conditional licensing (2025). This proves: (a) mRNA-LNP vaccines generate robust immune responses in cattle, (b) the manufacturing and regulatory pathway exists for veterinary mRNA, (c) Elanco already has a partnership with Medgene for this exact platform.

**Biological rationale:** Fusogard (inactivated toxoid) failed because it generated insufficient titer. mRNA vaccines produce 10-100x higher antibody titers than protein subunit vaccines in human trials (Moderna/Pfizer COVID data). LNPs naturally traffic to the liver (hepatotropism of LNPs is well-documented -- this is usually a liability in human mRNA vaccines but would be an ADVANTAGE for liver abscess prevention because it concentrates antigen presentation in hepatic APCs, generating a LOCAL immune response where it matters most). Encode the three immunodominant LktA regions identified by Xiao et al. (PL1, PL3, PL4 -- protective in mice) as a polyvalent mRNA construct.

**Key risk:** (1) Duration -- mRNA vaccines typically require boosters. Can a 2-dose regimen at feedlot arrival + 4 weeks provide 150+ days of protection? (2) Cost -- current veterinary mRNA vaccines are more expensive than traditional vaccines, though costs are dropping rapidly. (3) Cold chain requirements for feedlot distribution.

**Proposed de-risk:** $25-40K. Vaccinate 10 cattle with mRNA-LktA construct (Medgene collaboration). Measure systemic AND hepatic venous anti-LktA IgG titers at 2, 4, 8, 12, and 20 weeks post-vaccination. Compare titers to those achieved by historical Fusogard vaccination. If mRNA achieves >=4x higher peak titer and detectable titer at 20 weeks, proceed to challenge trial.

**Why this beats Fusogard:** Higher titer, hepatic LNP tropism concentrates immune response at the sinusoid, T-cell responses provide broader protection, rapid antigen redesign if strain variation emerges.

**Elanco fit:** Existing Medgene partnership for mRNA platform. Manufacturing infrastructure being built for H5N1. Regulatory pathway established.

---

### G2-3: Epitope-Focused Recombinant LktA Subunit Vaccine

**Target/mechanism:** Recombinant protein vaccine presenting only the immunodominant neutralizing epitopes of LktA (PL1, PL3, PL4 regions), formulated with a potent depot adjuvant for sustained high-titer neutralizing antibodies.

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2

**Category:** Known approach (iterating on Fusogard with modern antigen/adjuvant design)

**Evidence tier:** MODERATE

**Species data:** Xiao et al. (2009, Vet Res Commun) identified three immunodominant regions on LktA. Truncated recombinant proteins PL1, PL3, PL4 elicited protective effects in mice against F. necrophorum infection. Liu et al. (2021) showed multi-component vaccine (43K OMP + LktA + hemolysin) was protective in mice. Saginala 1997 crude leukotoxoid: 80% protection in challenge.

**Biological rationale:** Fusogard used a crude formalin-inactivated toxoid. Modern rational vaccine design starts from the identified B-cell epitopes and engineers a focused immunogen. Key innovations over Fusogard: (1) concentrate immune response on neutralizing epitopes rather than diluting it across the entire 336 kDa protein, (2) use ISCOMATRIX or saponin-based adjuvant (proven in veterinary vaccines to generate 10-50x higher titers than aluminum hydroxide), (3) include a prime-boost schedule calibrated to the feedlot timeline (dose 1 at arrival processing, dose 2 at reimplant ~60 days later).

**Key risk:** Same firehose problem as Fusogard -- will even improved titers be sufficient on high-grain diets with continuous translocation? This candidate is strongest when COMBINED with a Gate 1 inoculum reducer (see COMBO-2).

**Proposed de-risk:** $30-50K. Express PL1+PL3+PL4 as fusion protein in E. coli. Formulate with ISCOMATRIX adjuvant. Vaccinate 20 cattle (10 vaccine, 10 control). Measure anti-LktA neutralizing titer at 2, 4, 8, 16 weeks. Primary endpoint: neutralizing titer >=1:256 at 16 weeks (4x the estimated protective threshold). If met, proceed to challenge.

---

### G2-4: LktB Secretion Inhibitor (Small Molecule Anti-Virulence)

**Target/mechanism:** Block the LktB transporter that secretes LktA from the bacterial cell. LktB contains a POTRA2 (polypeptide transport-associated) domain -- the substrate-binding pocket through which LktA is exported via the Type 5b two-partner secretion system. A small molecule binding the POTRA2 domain would trap LktA inside the cell, rendering the bacteria unable to kill Kupffer cells even though it produces the toxin.

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2

**Category:** Novel (first-principles design; no precedent for LktB inhibition)

**Evidence tier:** INFERRED

**Species data:** None -- this is a novel target. However: (1) The LktBAC operon structure is established (Narayanan 2001). (2) POTRA domains in related two-partner secretion systems have been structurally characterized in E. coli and other Gram-negatives. (3) Small molecule inhibitors of bacterial Type I secretion systems (which export RTX toxins in other pathogens) are an active area of research.

**Biological rationale:** LktA has no homology to any other known leukotoxin. This means there is no human therapeutic value to F. necrophorum's secretion machinery -- making it a clean veterinary target with no risk of cross-resistance to human medicine. Inhibiting secretion rather than neutralizing the toxin extracellularly has the advantage of acting at the bacterial surface (higher effective concentration vs the diffuse sinusoidal space). Anti-virulence approaches avoid resistance selection pressure because they don't kill the bacteria.

**Key risk:** (1) No structure of LktB exists -- would require AlphaFold prediction or crystallography. (2) Delivery: a small molecule must reach the rumen (if targeting rumen wall F.n.) or the liver (if targeting hepatic F.n.) at effective concentrations. (3) Unknown whether blocking secretion is lethal or merely attenuating.

**Proposed de-risk:** $15-20K. (1) AlphaFold3 structure prediction of LktB POTRA2 domain. (2) Virtual screen of 10M compound library against POTRA2 binding pocket. (3) Top 20 hits tested in vitro: incubate F. necrophorum with compound, measure supernatant leukotoxic activity (if secretion is blocked, activity should drop). Timeline: 12-16 weeks.

**Closest analogy:** Anti-virulence approaches against Type III secretion systems in Pseudomonas and Salmonella (multiple compounds in preclinical development).

**Most likely failure mode:** No druggable pocket on LktB; the POTRA2 domain may be too flat or too dynamic for small molecule binding.

---

### G2-5: lktA Transcription Suppressor (Anti-Virulence -- Gene Regulation)

**Target/mechanism:** Suppress transcription of the lktBAC operon, reducing leukotoxin production at the source. LktC contains histidine kinase and sensory transduction regulator domains, suggesting it functions as a sensor/regulator of leukotoxin expression. Additionally, iron starvation at low cell density upregulates lktA expression 3.72-fold -- implying iron-responsive regulatory elements control the operon. Intervention: either (a) a small molecule agonist of the putative LktC repressor activity, or (b) an iron-mimetic compound that signals iron sufficiency and suppresses lktA transcription.

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2

**Category:** Novel

**Evidence tier:** INFERRED

**Species data:** (1) Iron starvation upregulates lktA 3.72-fold and hemagglutinin 2.49-fold (Antiabong et al. 2015, ScienceDirect). (2) LktC contains sensory transduction domains (Narayanan 2001). (3) No compound has been tested against lktA transcription.

**Biological rationale:** The Pillai 2021 data shows that leukotoxin QUANTITY predicts abscess severity (P < 0.0001, r=0.47 at 24h). Reducing production per cell by 5-10x would effectively convert virulent subsp. necrophorum into something resembling the less-virulent subsp. funduliforme (21-fold lower lktA transcript). You don't need to kill the bacteria -- just silence its weapon.

**Key risk:** (1) The regulatory circuitry of the lkt operon is poorly characterized. (2) Iron-responsive regulation may involve multiple overlapping systems (Fur, DtxR homologs). (3) In vivo delivery to F. necrophorum in the rumen/liver at effective concentrations.

**Proposed de-risk:** $10-15K. (1) RNA-seq of F. necrophorum under iron-replete vs iron-depleted conditions to map the full lktA regulatory network. (2) Test iron-mimetic compounds (e.g., gallium nitrate, which substitutes for iron in bacterial systems and suppresses iron-responsive virulence genes) against F. necrophorum in vitro -- measure lktA transcript by qRT-PCR and leukotoxic activity.

**Closest analogy:** Gallium nitrate as an anti-virulence agent against Pseudomonas aeruginosa (Kaneko 2007, J Clin Invest; Phase II clinical trial for CF lung infections).

---

### G2-6: LktA Receptor Decoy / Receptor Blockade

**Target/mechanism:** Block the unidentified bovine leukocyte receptor for LktA, preventing toxin binding and cell killing. Two approaches: (a) Identify the receptor, then develop a small molecule or antibody blocker. (b) Deploy soluble receptor fragments as "decoys" that bind LktA in the sinusoidal space before it reaches cell-surface receptors.

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2

**Category:** Novel

**Evidence tier:** INFERRED

**Species data:** The bovine LktA receptor is UNIDENTIFIED (Key Unknown #4 in Argus v15; flagged by Tribunal Agent B). LktA shows ruminant specificity (more toxic to bovine/ovine leukocytes than other species), strongly implying a specific receptor interaction rather than non-specific membrane disruption. For comparison: Mannheimia haemolytica leukotoxin (LktA -- confusingly the same gene name) binds bovine CD18 (beta-2 integrin). However, F. necrophorum LktA has NO sequence homology to M. haemolytica LktA, so the receptor may be entirely different.

**Biological rationale:** This is the "other half" of the leukotoxin equation. While G2-1 through G2-5 target the toxin side, this targets the host side. A receptor-blocking antibody would protect ALL Kupffer cells and neutrophils from leukotoxin regardless of toxin quantity, strain variation, or timing. It would be the most durable intervention because the host receptor doesn't change.

**Key risk:** The receptor is unknown. Without knowing the target, you cannot design the blocker. This is a discovery project, not a development project.

**Proposed de-risk:** $30-50K. Receptor identification screen: (1) Treat bovine PMNs with biotinylated purified LktA at low (activating) concentration. (2) Cross-link toxin-receptor complex. (3) Pull down with streptavidin beads. (4) Mass spectrometry identification of co-precipitating bovine proteins. (5) Validate top hits by CRISPR knockout in a bovine cell line (if the knockout cell is resistant to LktA, the receptor is confirmed). Timeline: 4-6 months.

**What changes if successful:** Opens an entirely new intervention axis. A receptor-blocking antibody could be the most durable single intervention in the portfolio -- possibly better than anti-LktA because it is resistant to toxin strain variation.

---

### G2-7: Kupffer Cell Trained Immunity (Beta-Glucan Hepatic Priming)

**Target/mechanism:** Pre-activate Kupffer cells via beta-glucan-induced "trained immunity" so they survive leukotoxin exposure at higher concentrations and clear bacteria more effectively. Beta-glucan (from yeast cell walls) reprograms macrophages epigenetically via histone modifications (H3K4me1, H3K27ac), enhancing their metabolic and antimicrobial capacity for weeks-months after exposure.

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2 host-side

**Category:** Non-obvious (cross-disease translation from sepsis/oncology immunology)

**Evidence tier:** MODERATE (for beta-glucan trained immunity in macrophages); PRELIMINARY (for application to Kupffer cells against leukotoxin)

**Species data:** Adams et al. (2024, Immunology): "Beta-glucan protects against sepsis-induced Kupffer cell loss by inhibiting pyroptosis and promoting self-renewal." Beta-glucan suppresses NLRP3/GSDMD-mediated pyroptosis and enhances KC self-renewal via c-Maf/MafB downregulation. This is directly relevant: LktA kills Kupffer cells, and beta-glucan protects them from a different killing mechanism. The question is whether trained immunity makes Kupffer cells resistant to LEUKOTOXIN-mediated killing specifically.

**Biological rationale:** The Sapper analysis noted that "an activated Kupffer cell killed by leukotoxin is just as dead as a resting one" -- and this is true for non-specific activation. BUT trained immunity is not just activation; it is metabolic and epigenetic reprogramming that changes the cell's survival capacity. If beta-glucan-trained Kupffer cells upregulate anti-apoptotic pathways (Bcl-2, Mcl-1) and enhanced phagocytic capacity, they might survive leukotoxin exposure at concentrations that kill naive Kupffer cells. This would raise the Gate 2 clearance threshold without requiring antibodies.

**Key risk:** (1) LktA may kill Kupffer cells via a mechanism that trained immunity cannot counter (e.g., direct pore formation rather than apoptotic signaling). (2) Delivery: intravenous beta-glucan particles are needed for hepatic trained immunity (oral beta-glucan from SCFP did not work -- but oral delivery does not reach Kupffer cells directly). (3) Duration of trained immunity effect (weeks-months, not the full feeding period).

**Proposed de-risk:** $8-12K. In vitro: isolate bovine Kupffer cells (from slaughterhouse livers). Pre-treat with particulate beta-glucan for 7 days. Then challenge with purified LktA at graded concentrations. Measure survival (LDH release, Annexin V), phagocytic capacity (fluorescent bead uptake), and pro-inflammatory cytokine production. Compare trained vs naive Kupffer cells. If trained cells show >=2-fold higher LD50 for LktA, proceed to in vivo.

**Important distinction from SCFP failure:** SCFP delivers beta-glucan ORALLY, where it acts in the rumen (Gate 1). This candidate delivers beta-glucan INTRAVENOUSLY (or via injectable particulate formulation), where it reaches Kupffer cells directly. The failure analysis rules out oral beta-glucan for liver abscess prevention but does NOT rule out parenteral beta-glucan for hepatic immune priming. Different route, different target.

---

### G2-8: Anti-Factor H Binding (Complement Sensitization During Portal Transit)

**Target/mechanism:** Block F. necrophorum's ability to bind Factor H, a host complement regulator, on its surface. F. necrophorum evades complement-mediated killing during portal transit by binding Factor H via ionic interactions at both N-terminal and C-terminal sites (Friberg et al. 2008, J Immunol). Bound Factor H remains active as a cofactor for Factor I-mediated C3b cleavage, effectively coating the bacterium in a "don't attack me" signal. Blocking this binding would expose F. necrophorum to full complement attack during portal transit, killing bacteria BEFORE they reach the hepatic sinusoid.

**Disease stage:** Stage 3 (portal transit) -- Gate 1-2 transition

**Category:** Non-obvious (human Neisseria meningitidis vaccine precedent)

**Evidence tier:** MODERATE (Factor H binding is established; intervention is novel)

**Species data:** Friberg et al. (2008): All F. necrophorum strains tested were serum-resistant and bound Factor H at variable levels (5-42%). Strains with strongest Factor H binding caused most severe disease in humans (Lemierre's syndrome). Increased C3b deposition and MAC formation on weakly-binding strains impaired survival in serum at 3.5 hours.

**Biological rationale:** This is an underappreciated intervention point. The Tribunal focused on leukotoxin at the liver, but complement evasion during portal transit determines HOW MANY bacteria arrive at the liver alive. If you remove Factor H binding, complement kills bacteria in portal blood. This reduces the effective inoculum at Gate 2 -- working synergistically with leukotoxin neutralization. The precedent: Neisseria meningitidis binds Factor H via fHbp (Factor H binding protein), and the licensed vaccine Trumenba/Bexsero targets fHbp to restore complement-mediated killing.

**Key risk:** (1) The F. necrophorum outer membrane protein(s) that bind Factor H are not fully characterized. (2) Vaccination against a Factor H-binding protein could theoretically trigger autoimmune responses against the host's own Factor H. (3) Complement killing in portal blood may be too slow to clear bacteria before they reach the sinusoid (~30 seconds transit time).

**Proposed de-risk:** $20-30K. (1) Identify the F. necrophorum Factor H-binding protein by affinity chromatography (bovine Factor H as bait, pull down from F.n. outer membrane extracts, mass spec ID). (2) Test whether anti-fHBP antibodies restore serum killing of F. necrophorum in an ex vivo bovine serum bactericidal assay.

---

### G2-9: Systemic Complement Enhancement (Portal Blood Bactericidal Activity)

**Target/mechanism:** Enhance complement-mediated killing of F. necrophorum during portal transit by vaccinating with F. necrophorum outer membrane antigens that are targets of complement deposition (LPS O-antigen, OMPs). This generates opsonizing antibodies that promote C3b deposition and MAC formation on the bacterial surface even in the presence of Factor H binding.

**Disease stage:** Stage 3 (portal transit) -- Gate 1-2 transition

**Category:** Known approach (outer membrane vaccine component)

**Evidence tier:** MODERATE

**Species data:** Liu et al. (2021) multi-component vaccine (43K OMP + LktA + hemolysin) was protective in mice. OMV vaccine candidates are under investigation (MDPI 2023: 342 proteins identified in F. necrophorum OMVs). Anti-OMP antibodies would opsonize bacteria for complement-mediated killing during portal transit.

**Biological rationale:** This is distinct from G2-3 (which targets leukotoxin neutralization). Here, the goal is to kill the bacteria during transit, before they reach the sinusoid. Opsonizing anti-OMP antibodies + complement = bactericidal activity in portal blood. This reduces the viable inoculum arriving at the liver. Works at the Gate 1-2 transition.

**Key risk:** Same as for all vaccine approaches: sufficient titer, durability, and the systemic-to-portal-blood IgG localization question. However, IgG in portal blood should be similar to systemic IgG (portal blood is not a privileged compartment like CSF or the eye).

**Proposed de-risk:** $15-25K. Formulate OMV-based vaccine from F. necrophorum subsp. necrophorum. Vaccinate 10 cattle. Measure serum bactericidal activity against F. necrophorum at 2, 4, 8, 16 weeks post-vaccination using standard SBA assay.

---

### G2-10: Anti-NET Evasion (DNase Inhibitor to Restore Neutrophil Trapping)

**Target/mechanism:** Inhibit F. necrophorum extracellular DNases to preserve neutrophil extracellular traps (NETs) in the hepatic sinusoid. Multiple external panel models identified NET evasion via DNases as a critical but underappreciated immune evasion mechanism that operates BEFORE leukotoxin kills neutrophils. If NETs remain intact, they physically trap bacteria and expose them to antimicrobial histones and granule proteins, buying time for Kupffer cell phagocytosis.

**Disease stage:** Stage 4 (hepatic immune evasion) -- Gate 2 supplementary

**Category:** Non-obvious (cross-pathogen translation from S. aureus/S. pyogenes NET evasion)

**Evidence tier:** INFERRED (DNase activity in F. necrophorum is inferred from genomic data and the F. nucleatum analogy)

**Species data:** Multiple DNase-encoding genes identified in F. necrophorum genome (Grok and Gemini external panels). F. nucleatum (closest well-studied relative) actively suppresses NET formation (Arelaki 2020, Front Immunol). S. aureus DNase (nucA) is a validated virulence factor where inhibitors are in development.

**Key risk:** (1) F. necrophorum DNase activity has not been directly demonstrated in bovine infections. (2) Multiple redundant DNases may exist. (3) Delivery of a DNase inhibitor to the hepatic sinusoidal space.

**Proposed de-risk:** $5-8K. (1) Confirm DNase activity: incubate F. necrophorum culture supernatant with calf thymus DNA, measure degradation by gel electrophoresis. (2) Test actin (a natural DNase inhibitor that stabilizes NETs) and known synthetic DNase inhibitors against F. necrophorum DNase activity in vitro.

---

## GATE 1 CANDIDATES: Combination Components

These reduce the bacterial inoculum arriving at the liver. None is proposed as a standalone liver abscess intervention. Each is designed as a COMBINATION PARTNER with a Gate 2 target.

---

### G1-1: Anti-Hemagglutinin Vaccine (Anti-Adhesion at Rumen Wall)

**Target/mechanism:** Block hemagglutinin-mediated adhesion of F. necrophorum to damaged ruminal epithelium. Generate anti-hemagglutinin antibodies that prevent the initial "handshake" between bacterium and rumen wall. Reduces the number of bacteria that colonize the rumen wall and subsequently enter portal blood.

**Disease stage:** Stage 2 (rumen wall colonization) -- Gate 1

**Category:** Known approach

**Evidence tier:** MODERATE

**Species data:** Anti-hemagglutinin antiserum reduces bacterial attachment to rumen cells in vitro (Kanoe & Iwaki 1987). All hepatic isolates of subsp. necrophorum are hemagglutination-positive; some ruminal isolates are negative -- suggesting hemagglutination is required for invasive disease. Prediction P4 tests whether hemagglutinin blockade reduces rumen wall colonization by >50%.

**Key risk:** (1) Antibody delivery to the rumen surface. Systemic IgG from parenteral vaccination reaches the rumen epithelial surface at low concentrations. Mucosal IgA might be better. (2) Adhesion redundancy -- 43K OMP, FadA, and other adhesins may compensate.

**Proposed de-risk:** $20-40K. Ex vivo rumen tissue explant assay (Prediction P4 design). If anti-hemagglutinin reduces adhesion by >=50%, proceed. If <25%, adhesion machinery is too redundant for single-target blockade.

---

### G1-2: F. necrophorum-Specific Phage Cocktail (Rumen Biocontrol)

**Target/mechanism:** Lytic bacteriophages that specifically kill F. necrophorum subsp. necrophorum in the rumen, reducing the inoculum available for translocation. A "living antibiotic" with narrow-spectrum specificity.

**Disease stage:** Stage 2 (rumen wall colonization) -- Gate 1

**Category:** A -- Empirical data exists

**Evidence tier:** PRELIMINARY

**Species data:** Schwarz et al. (2024, PHAGE journal): Isolated six novel F. necrophorum phages (phiFN37, phiRTG5, phiKSUM, phiHugo, phiPaco, phiBB) from rumen fluid and ruminal F. necrophorum isolates. Two phages (phiKSUM, phiBB) did NOT form lysogens and infected BOTH subspecies -- these are the candidates for therapy. A 2025 MDPI study isolated additional lytic phages from ruminal fluid and city sewage, with higher frequency in sewage. Patent filed: US Patent Application 2020/0390835 (Mathieu, Rice University) -- "Composition and method for inhibiting the growth of pathogens causing bovine liver abscesses."

**Biological rationale:** Phage therapy targets F. necrophorum specifically without AMR concerns and without disrupting the broader rumen microbiome. The obligately lytic phages phiKSUM and phiBB are ideal candidates because they cannot lysogenize (avoiding phage resistance via superinfection immunity). The Gemini external panel flagged phage therapy as commercially dead due to rumen pharmacokinetics (dilution, washout, protozoal grazing). HOWEVER: in-feed continuous delivery (like tylosin) could maintain effective phage concentrations. The bacteria are also concentrated in rumen wall biofilms where phage can accumulate at higher local concentrations.

**Key risk:** (1) Rumen stability: phage particles may be degraded by rumen proteases or consumed by protozoa. (2) Resistance emergence: bacteria evolve phage resistance rapidly; a cocktail of 3+ phages with different receptor specificities mitigates this. (3) Efficacy ceiling: even if phage reduces rumen F.n. by 1-2 logs, this may be insufficient without a Gate 2 partner.

**Proposed de-risk:** $15-25K. In vivo rumen phage stability: administer phiKSUM and phiBB to rumen-fistulated cattle (n=4). Sample rumen fluid at 0, 1, 4, 8, 24h. Quantify viable phage (plaque assay) and F. necrophorum concentration (qPCR). Primary endpoint: does phage survive in the rumen for >=8h at detectable titers? Does F.n. concentration decrease by >=0.5 log?

---

### G1-3: Protected Butyrate + Zinc Complex (Barrier Support -- Combination Component ONLY)

**Target/mechanism:** Dual barrier support: butyrate provides energy for ruminal epithelial cells, upregulates tight junction proteins (claudin-1, ZO-1, occludin), and suppresses NF-kB inflammatory signaling. Zinc enhances metallothionein-mediated antioxidant defense and epithelial cell proliferation. Together, they reduce the severity of rumenitis and the frequency of barrier failure events.

**Disease stage:** Stage 1-2 (acidosis/rumenitis, barrier integrity) -- Gate 0/1

**Category:** A -- Empirical hits exist

**Evidence tier:** MODERATE for individual components; PRELIMINARY for combination

**Species data:** Butyrate: 2025 study (MDPI Animals 15:3380) showed protected butyrate supplementation improved rumen papillae development and reduced inflammatory pathway expression (IL-17, NF-kB) in beef cattle. Grok external panel notes butyrate reduced liver abscess incidence in at least one trial (though non-significant in most). Zinc methionine: improved zinc status and reduced inflammatory markers but no standalone abscess reduction. The combination has not been tested.

**CRITICAL FRAMING:** This is NOT a standalone liver abscess intervention. The failure analysis definitively rules out Gate 1-only approaches. This is positioned as a COMBINATION COMPONENT with a Gate 2 target -- reducing the "firehose" volume of translocation so that the Gate 2 intervention (mAb, vaccine) has an easier job. SCFP (zero effect on abscesses, n=4,689) proves that Gate 1 improvement alone is insufficient. Protected butyrate + zinc is proposed only as the "monensin companion" layer in a multi-component product.

**Key risk:** Same as SCFP -- may have zero incremental effect on abscesses even as a combination component. However, prediction S3 (SCFP + Gate 2 vaccine) tests whether Gate 1 support adds value when Gate 2 is addressed.

**Proposed de-risk:** Already partially de-risked by existing butyrate and zinc cattle data showing rumen health benefits. The remaining de-risk is testing the combination WITH a Gate 2 vaccine (per prediction S3 design).

---

### G1-4: Anti-43K OMP Vaccine (Anti-Adhesion -- Complementary to G1-1)

**Target/mechanism:** Generate antibodies against the 43K outer membrane protein of F. necrophorum that mediates fibronectin-dependent adhesion to bovine epithelial and endothelial cells. Complements anti-hemagglutinin (G1-1) to cover multiple adhesion pathways.

**Disease stage:** Stage 2 (rumen wall colonization) -- Gate 1

**Category:** Known approach

**Evidence tier:** MODERATE

**Species data:** Kumar et al. (2013): 42.4 kDa OMP binds with high affinity to bovine endothelial cells and is recognized by sera from cattle with liver abscesses. Singh et al. (2022): 43K OMP interacts with fibronectin. Liu et al. (2021): multi-component vaccine including 43K OMP was protective in mice.

**Key risk:** Same antibody delivery problem as G1-1. Systemic anti-OMP IgG may not reach the rumen wall surface at sufficient concentration to block adhesion. However, anti-OMP antibodies in portal blood could opsonize bacteria during transit (dual function: anti-adhesion at the rumen wall + opsonization during portal transit).

**Proposed de-risk:** $15-25K. Test whether anti-43K OMP serum reduces F. necrophorum adhesion to bovine endothelial cells in vitro (adhesion assay). If >=50% reduction, test in the ex vivo rumen tissue explant assay alongside G1-1. The combination of anti-hemagglutinin + anti-43K OMP should exceed either alone.

---

### G1-5: Hindgut-Targeted F. necrophorum / Bacteroides Suppression

**Target/mechanism:** Address the hindgut translocation pathway (estimated 20-33% of liver abscesses based on Bacteroides dominance in 16S data). Deliver an antimicrobial or anti-adhesion agent that reaches the colon intact. Options: (a) colon-targeted encapsulated antimicrobial (pH-responsive release at pH 6.5-7.0 of the hindgut), (b) anti-Bacteroides bacteriophage, (c) hindgut-specific competitive exclusion organism.

**Disease stage:** Stage 7 / Hindgut pathway -- Alt Gate 1

**Category:** Novel

**Evidence tier:** INFERRED

**Species data:** Fuerniss et al. (2022): Bacteroides account for 33% of 16S reads in liver abscesses, with some abscesses Bacteroides-dominated. Salih et al. (2025): colonic epithelium yields more subsp. funduliforme isolates than rumen. Zero interventions have ever targeted the hindgut pathway.

**Biological rationale:** If KE#1 confirms that >20% of liver abscess F. necrophorum originates from the hindgut (Prediction P1), then all rumen-focused interventions have an intrinsic 20-33% efficacy ceiling. This candidate fills that gap.

**Key risk:** (1) KE#1 may show the hindgut is a negligible contributor (<5%). (2) Colonic drug delivery in cattle is poorly developed. (3) Bacteroides species identification in liver abscesses is incomplete.

**Proposed de-risk:** $5K. Wait for KE#1 results. If hindgut >20%, invest in colonic delivery platform development. If <5%, deprioritize.

---

### G1-6: Tannin-Resistant Anti-F. necrophorum Compound (Addressing the Tannase Problem)

**Target/mechanism:** A tannin derivative or synthetic analog that retains antimicrobial activity against F. necrophorum but is resistant to degradation by bacterial tannase. Addresses the Sapper-identified hypothesis (Prediction S4) that F. necrophorum produces tannase that degrades quebracho/chestnut tannins at the rumen wall.

**Disease stage:** Stage 2 (rumen wall colonization) -- Gate 1

**Category:** Non-obvious

**Evidence tier:** INFERRED

**Species data:** Silvafeed BX + monensin: 28.5% abscess incidence vs 43.1% control (Felizari 2025, n=2,986) -- partial effect but inferior to MON+TYL (18.3%). F. nucleatum (closely related to F. necrophorum) produces highly active tannase. If Prediction S4 is confirmed, the 10-point gap between MON+BX and MON+TYL may be partly due to F. necrophorum tannase degrading tannins at the rumen wall colonization site.

**Key risk:** (1) Prediction S4 may be falsified (F. necrophorum may lack meaningful tannase). (2) Synthesizing tannase-resistant tannin analogs may be chemically challenging.

**Proposed de-risk:** $5-10K. Run Prediction S4 first (in vitro tannase assay). If F. necrophorum degrades tannins by >50% at 4h, screen a library of synthetic polyphenol derivatives for tannase resistance + retained anti-F.n. MIC.

---

### G1-7: Engineered Funduliforme Probiotic (Competitive Exclusion with Attenuated Leukotoxin)

**Target/mechanism:** Introduce an engineered or selected strain of F. necrophorum subsp. funduliforme (which produces 21-fold less leukotoxin) into the rumen to competitively displace virulent subsp. necrophorum strains. Both subspecies occupy the same ecological niche (lactate fermentation, epithelial adhesion). The funduliforme strain would maintain normal rumen function while eliminating the high-leukotoxin strains responsible for severe abscesses.

**Disease stage:** Stage 2 / pen-level strain ecology -- Gate 1

**Category:** Novel

**Evidence tier:** INFERRED

**Species data:** The Tribunal's Martian analysis identified that 75% of pen-level variance in abscess prevalence is driven by pen microbiome composition, likely reflecting F. necrophorum strain virulence ecology. Subsp. funduliforme is naturally less virulent (21x less lktA transcript). Prediction P3 predicts funduliforme-only abscesses are predominantly A- or A grade (mild).

**Biological rationale:** Traditional DFMs fail because they occupy a DIFFERENT niche from F. necrophorum (Bacillus is aerobic; F.n. is an obligate anaerobe using lactate). A funduliforme-based probiotic occupies the SAME niche -- it can genuinely compete for attachment sites, lactate substrate, and epithelial colonization. If it displaces necrophorum, the leukotoxin production of the pen's F. necrophorum population drops 21-fold, converting a high-risk pen into a low-risk pen.

**Key risk:** (1) Funduliforme may not competitively displace established necrophorum populations. (2) Regulatory pathway for a live attenuated bacterium in feed is complex. (3) Funduliforme still causes SOME disease (16.9% of abscesses). (4) Risk of horizontal gene transfer of virulence genes between subspecies.

**Proposed de-risk:** $15-30K. In vitro competition assay: co-culture subsp. necrophorum and subsp. funduliforme at varying ratios in rumen fluid simulant. Measure changes in subspecies ratio over 7 days. If funduliforme can maintain >50% of the population when inoculated at 1:1, competitive exclusion is plausible. Then test in rumen-fistulated cattle.

---

### G1-8: Anti-Biofilm Agent (Rumen Wall Biofilm Disruption)

**Target/mechanism:** Disrupt F. necrophorum biofilms on the rumen wall to expose bacteria to host immune defenses and phage/antimicrobial agents. F. nucleatum (closest relative) forms extensive biofilms via FadA-mediated co-aggregation (Brennan & Garrett 2019, Nat Rev Microbiol). F. necrophorum rumen wall concentrations (4-5 log CFU/g -- consistent with biofilm densities) and the requirement for continuous tylosin feeding both suggest biofilm involvement.

**Disease stage:** Stage 2 (rumen wall colonization) -- Gate 1

**Category:** Non-obvious

**Evidence tier:** INFERRED

**Species data:** No direct evidence of F. necrophorum biofilm on rumen epithelium. However: (1) F. nucleatum biofilm is extensively characterized. (2) Rumen wall F.n. concentrations suggest sessile (biofilm) growth. (3) Continuous tylosin requirement is consistent with biofilm dynamics (biofilm reforms after treatment cessation).

**Key risk:** F. necrophorum biofilm on rumen epithelium has not been demonstrated. This is speculative.

**Proposed de-risk:** $5-8K. (1) Demonstrate biofilm: culture F. necrophorum on bovine rumen epithelial cell explants for 48h, then visualize with confocal microscopy (LIVE/DEAD staining, FISH probe). (2) If biofilm confirmed, test dispersal agents (DNase I, dispersin B, D-amino acids) for ability to disrupt the biofilm and release planktonic cells.

---

## POST-GATE 2 CANDIDATES

---

### PG-1: Anti-Stellate Cell Activation (Encapsulation Delay)

**Target/mechanism:** Inhibit hepatic stellate cell (HSC) activation in the first 24-72 hours after bacterial seeding to delay encapsulation. HSCs are activated by TGF-beta, PDGF, and inflammatory cytokines, transitioning from quiescent vitamin A-storing cells to activated myofibroblasts that deposit collagen I/III (Friedman 2008, Physiol Rev). Delaying encapsulation extends the therapeutic window during which host immune cells and systemic antibiotics can reach and clear the bacterial focus.

**Disease stage:** Stage 5 (abscess formation, pre-encapsulation) -- Post-Gate 2

**Category:** Non-obvious (cross-disease from hepatic fibrosis/cirrhosis)

**Evidence tier:** INFERRED

**Species data:** No data in the liver abscess context. However, HSC biology is extensively studied in liver fibrosis. TGF-beta signaling inhibitors (pirfenidone, galunisertib) are in clinical trials for human liver fibrosis. The question is whether short-term HSC inhibition during the adaptation/early feeding period could extend the window for immune clearance of early microabscesses.

**Key risk:** (1) Timing -- you would need to administer this during the high-risk period before you know whether seeding has occurred (since abscesses are subclinical). (2) Systemic TGF-beta inhibition has immunosuppressive side effects. (3) Cost and impracticality of systemic anti-fibrotic therapy in feedlot cattle.

**Proposed de-risk:** $10-15K. Ex vivo liver slice culture: inoculate fresh bovine liver slices with F. necrophorum. Measure stellate cell activation (alpha-SMA expression) at 6, 12, 24, 48h. Test pirfenidone at graded concentrations -- does it delay alpha-SMA expression by >=24h without impairing Kupffer cell viability?

---

### PG-2: Abscess Biofilm Disruption (Post-Establishment -- Low Priority)

**Target/mechanism:** Disrupt the polymicrobial biofilm within established abscesses using enzymatic degradation of the extracellular polymeric substance (EPS) matrix. Combined with antimicrobial delivery, this could theoretically sterilize established abscesses.

**Disease stage:** Stage 6 (chronic persistence) -- Irreversible (INTRACTABLE)

**Category:** Novel

**Evidence tier:** INFERRED

**Species data:** Biofilm within liver abscesses is inferred (Costerton 1999, Science; GPT-5.4 and Gemini external panels). No direct evidence of EPS matrix characterization in bovine liver abscesses.

**HONEST ASSESSMENT:** This is included for coverage completeness but is the lowest priority candidate. The fibrous capsule prevents delivery of any agent to the abscess interior. Even if you could deliver a biofilm-disrupting enzyme, the anaerobic, acidic, nutrient-depleted microenvironment would impair most antimicrobials. And cattle show no clinical signs that would trigger treatment. This candidate exists to acknowledge the gap, not to seriously propose a path forward.

**Key risk:** Pharmacokinetically impossible under current technology. The capsule barrier is a physics problem, not a biology problem.

**Proposed de-risk:** Do not invest. Focus all resources on prevention (Gates 1-2).

---

### PG-3: Anti-T. pyogenes Synergy Disruption

**Target/mechanism:** Break the F. necrophorum / T. pyogenes synergy that makes mixed infections more severe. T. pyogenes consumes oxygen (creating anaerobiosis for F. necrophorum) and produces pyolysin (additional cytotoxin). Anti-pyolysin antibodies or T. pyogenes-specific bacteriophage would reduce the severity of polymicrobial abscesses without targeting F. necrophorum directly.

**Disease stage:** Stage 4-5 (polymicrobial synergy) -- Post-Gate 2

**Category:** Known approach (building on Centurion's T. pyogenes bacterin component)

**Evidence tier:** MODERATE

**Species data:** Centurion vaccine included T. pyogenes bacterin alongside F. necrophorum leukotoxoid. T. pyogenes detected in 29.2% of liver abscesses (Abbasi 2025). More prevalent in cattle NOT receiving tylosin (P=0.022, Fuerniss 2022). Pyolysin (cholesterol-dependent cytolysin) is the primary virulence factor.

**Key risk:** T. pyogenes is secondary, not primary. Targeting it alone would have minimal impact on overall abscess incidence. Only valuable as a combination component.

**Proposed de-risk:** $10-15K. Test anti-pyolysin antibodies in an in vitro polymicrobial abscess model: co-culture F. necrophorum + T. pyogenes with bovine immune cells +/- anti-pyolysin serum. Measure whether disrupting the synergy reduces abscess-like aggregate formation.

---

### PG-4: Blood Biomarker for Ante-Mortem Liver Abscess Detection

**Target/mechanism:** Develop a blood-based diagnostic for liver abscess in live cattle, enabling early detection during the feeding period. Amachawadi et al. (2023) identified candidate metabolites (3-phenylpropionate, tryptophan metabolites, succinate) in abscess material that might be detectable in peripheral blood.

**Disease stage:** Stage 4-5 (early detection) -- Diagnostic

**Category:** Known approach

**Evidence tier:** PRELIMINARY

**Species data:** Amachawadi et al. (2023, J Anim Sci): metabolomics of liver abscess purulent material identified biochemicals distinct from normal liver tissue. No validated blood biomarker exists.

**Biological rationale:** A blood biomarker would transform the field: (1) Enable early intervention during the feeding period. (2) Allow epidemiological studies with real-time abscess tracking (resolving the "when do abscesses form?" question). (3) Enable individual animal treatment decisions. (4) Validate other interventions in real-time rather than waiting for slaughter data.

**Key risk:** (1) Abscesses are walled off by capsules that may prevent metabolite leakage into blood. (2) Background hepatic inflammation from SARA may create false positives. (3) Sensitivity at the early microabscess stage (when intervention could help) may be too low.

**Proposed de-risk:** $10-15K. Collect paired blood samples and liver abscess status from 200 cattle at slaughter. Measure 3-phenylpropionate, tryptophan metabolites, succinate, and haptoglobin in serum. Test sensitivity/specificity for abscess detection. If AUC-ROC >0.75, develop into a rapid point-of-care test.

---

## COMBINATION PRODUCTS

The failure analysis demands simultaneous Gate 1 + Gate 2 targeting. These are the integrated product concepts.

---

### COMBO-1: Anti-LktA mAb + Phage Cocktail ("Shield + Sword")

**Components:** G2-1 (anti-LktA monoclonal antibody, injectable) + G1-2 (F. necrophorum phage cocktail, in-feed continuous)

**Rationale:** The mAb raises the hepatic clearance threshold (Gate 2). The phage reduces the bacterial inoculum arriving at the liver (Gate 1). Together, the reduced inoculum is far below the elevated threshold. This is the combination that the failure analysis says has never been tried but is demanded by the data. Prediction S2 predicts >80% reduction.

**Elanco fit:** mAb leverages their $130M manufacturing platform. Phage leverages their feed additive distribution infrastructure (feed mills, premix contracts). Both are non-antibiotic.

**Cost estimate:** mAb injection at feedlot arrival + booster at reimplant (~$5-8/head). Phage in-feed continuous (~$1-2/head). Total ~$6-10/head. Competitive with tylosin ($2-3/head) only if abscess reduction exceeds 70%. Justified by the $9.70/head industry-wide loss from abscesses.

---

### COMBO-2: mRNA LktA Vaccine + Anti-Adhesion Vaccine ("Prime + Block")

**Components:** G2-2 (mRNA-LNP leukotoxin vaccine, injectable) + G1-1/G1-4 (anti-hemagglutinin + anti-43K OMP vaccine antigens, co-formulated)

**Rationale:** A single-injection, multi-component vaccine that simultaneously generates: (1) anti-LktA neutralizing antibodies (Gate 2), (2) anti-hemagglutinin antibodies (Gate 1 -- reduces rumen wall colonization), (3) anti-43K OMP antibodies (Gate 1 -- reduces adhesion + Gate 1.5 -- opsonizes bacteria during portal transit). The mRNA component generates high titers against leukotoxin. The protein components generate anti-adhesion antibodies. This is the rational evolution of the Liu et al. (2021) multi-component concept, translated to cattle.

**Elanco fit:** Leverages Medgene mRNA partnership + traditional vaccine manufacturing. Single injection at processing = minimal labor cost.

**Cost estimate:** $3-5/head for a single-injection product. Competitive with tylosin. If a booster is needed at reimplant, ~$5-8/head total.

---

## CATEGORY A: WHAT HAS ACTUALLY WORKED IN VIVO

The following have positive in-vivo data in cattle or relevant models. Listed separately per Forge instructions.

| # | Intervention | Species | In-Vivo Result | PMID/DOI | Relevance |
|---|---|---|---|---|---|
| A1 | Tylosin (60-90 mg/hd/d in feed) | Cattle | 40-70% abscess reduction | Multiple; Meyer 2013 n=3,632 | Gold standard. AMR concerns. Sets efficacy floor. |
| A2 | Fusogard leukotoxoid vaccine | Cattle | 80% reduction in challenge model (1/5 vs 5/5); forage-fed field efficacy; inconsistent on grain | Saginala 1997, PMID 9110232 | Proves Gate 2 target. Fails on high-grain = formulation problem, not target problem. |
| A3 | Crude leukotoxoid (KSU) | Cattle | 100% protection in challenge (0/5 vaccinated vs 5/5 controls) | Saginala 1997 | Small n but strongest single-intervention result in the literature. |
| A4 | Silvafeed BX + monensin | Cattle | 28.5% incidence vs 43.1% control (P<0.001) | Felizari 2025, n=2,986 | Partial. Unknown mechanism. Inferior to MON+TYL (18.3%). |
| A5 | Multi-antigen subunit vaccine (43K OMP + LktA + hemolysin) | Mice | Protective in mouse challenge | Liu 2021, PMC8685265 | First dual-gate (G1+G2) approach. No cattle data. |
| A6 | Protected butyrate (calcium butyrate 2g/kg DM) | Cattle | Improved rumen papillae, reduced IL-17/NF-kB; some reduction in abscess incidence (non-significant) | MDPI Animals 2025, 15:3380 | Gate 1 only. Value as combination component. |
| A7 | F. necrophorum phage (phiKSUM, phiBB) | In vitro | Lytic, obligately lytic, infects both subspecies | Schwarz 2024, PHAGE journal | No in vivo cattle data yet. Most promising phage candidates. |

---

## CANDIDATE RANKING

Ranked by: evidence strength x bottleneck relevance x Elanco fit x IP position. Novel drug/vaccine targets ranked above feed additives at equivalent evidence per Agteria strategic preference.

### Tier 1: Portfolio Center (Invest Now)

| Rank | Candidate | Gate | Rationale |
|---|---|---|---|
| 1 | **G2-1: Anti-LktA mAb** | Gate 2 | Guaranteed titer. Elanco mAb platform. Solves the Fusogard problem directly. De-risk with Prediction T2 ex vivo liver perfusion. |
| 2 | **G2-2: mRNA LktA vaccine** | Gate 2 | 10-100x higher titers than Fusogard. Hepatic LNP tropism. Elanco-Medgene partnership exists. Fastest path to cattle POC. |
| 3 | **COMBO-1: mAb + phage** | G1+G2 | Tests the core portfolio thesis (S2). Non-antibiotic tylosin replacement. Both components have Elanco manufacturing alignment. |
| 4 | **G2-3: Epitope-focused subunit vaccine** | Gate 2 | Lower-risk iteration on Fusogard. Xiao epitope data enables rational design. Lower cost per dose than mAb or mRNA. |
| 5 | **G1-2: F.n. phage cocktail** | Gate 1 | Specific, non-antibiotic F.n. suppression. Schwarz 2024 phages exist. In-feed delivery mirrors tylosin. Essential combination partner. |

### Tier 2: High Value, Needs Discovery (Invest After Tier 1 De-Risk)

| Rank | Candidate | Gate | Rationale |
|---|---|---|---|
| 6 | **G2-6: LktA receptor decoy** | Gate 2 | The "other half" of leukotoxin. Would be best single target if receptor identified. Requires discovery investment. |
| 7 | **G2-8: Anti-Factor H binding** | G1-2 | Elegant complement restoration. Neisseria vaccine precedent. Requires F.n. fHBP identification. |
| 8 | **G2-5: lktA transcription suppressor** | Gate 2 | Anti-virulence: silence the weapon without killing the commensal. Gallium nitrate analog. Needs regulatory circuitry mapping. |
| 9 | **G2-4: LktB secretion inhibitor** | Gate 2 | Novel small molecule target. No structure exists. High IP value if druggable. AF3 structure prediction first. |
| 10 | **COMBO-2: mRNA vaccine + anti-adhesion** | G1+G2 | All-in-one injectable. Most elegant product concept but requires both vaccine components to succeed. |

### Tier 3: Supporting / Conditional

| Rank | Candidate | Gate | Rationale |
|---|---|---|---|
| 11 | G2-7: Kupffer cell trained immunity | Gate 2 | Novel host-side approach. Beta-glucan KC protection data is strong. Needs bovine LktA-specific validation. |
| 12 | G1-1: Anti-hemagglutinin vaccine | Gate 1 | Combination component. Adhesion redundancy risk. |
| 13 | G2-9: Complement enhancement (OMV vaccine) | G1-2 | Kills bacteria during transit. Component of multi-antigen vaccine. |
| 14 | G1-4: Anti-43K OMP vaccine | Gate 1 | Dual function (anti-adhesion + opsonization). Component of COMBO-2. |
| 15 | G2-10: Anti-NET evasion (DNase inhibitor) | Gate 2 | Supplementary. Must confirm F.n. DNase activity first. |
| 16 | PG-4: Blood biomarker diagnostic | Diagnostic | Transforms field trial design. Enables real-time intervention studies. |
| 17 | G1-5: Hindgut-targeted suppression | Alt G1 | Conditional on KE#1 result. |
| 18 | G1-7: Engineered funduliforme probiotic | Gate 1 | Elegant concept. Regulatory complexity. Long development. |

### Tier 4: Background / Low Priority

| Rank | Candidate | Gate | Rationale |
|---|---|---|---|
| 19 | G1-3: Protected butyrate + zinc | Gate 0/1 | Combination component only. No standalone value. Feed additive -- low IP. |
| 20 | G1-6: Tannase-resistant tannin | Gate 1 | Conditional on Prediction S4. Feed additive adjacent. |
| 21 | G1-8: Anti-biofilm (rumen wall) | Gate 1 | Must confirm biofilm first. Speculative. |
| 22 | PG-1: Anti-stellate cell activation | Post-G2 | Novel but impractical in feedlot setting. |
| 23 | PG-3: Anti-T. pyogenes synergy | Post-G2 | Secondary target. Only relevant if primary targets succeed. |
| 24 | PG-2: Abscess biofilm disruption | Irreversible | Included for completeness. Do not invest. Physics barrier. |

---

## THE "WHY ISN'T THE FIELD DOING THIS?" TEST

Applied to each feed additive / nutraceutical candidate per Forge instructions:

| Feed Additive | Why isn't it standard of care? | Honest answer |
|---|---|---|
| Protected butyrate | Improves rumen health markers. Zero proven abscess reduction as standalone. | Gate 1 target. The field tried SCFP (n=4,689) and got zero. No feed additive targeting Gate 1 alone has ever worked. |
| Tannin blends | Partial effect with monensin (28.5% vs 43.1%). Unknown mechanism. | 10-point gap to MON+TYL. Unknown mechanism makes optimization impossible. Possible tannase degradation by target pathogen. |
| Zinc supplementation | Improves zinc status and reduces inflammation. Zero abscess reduction. | Gate 1 only. Same lesson as SCFP. |
| Beta-glucan (oral) | SCFP contains beta-glucan. SCFP = zero effect (n=4,689). | Oral beta-glucan does not reach Kupffer cells. Gate 1 immune stimulation is non-specific and insufficient against leukotoxin. |
| Essential oils | ZERO effect. Possible 107% INCREASED risk. | Potentially harmful. Disrupts rumen ecology in favor of F. necrophorum. |

**Conclusion:** No feed additive is ranked in Tier 1. Protected butyrate + zinc (G1-3) is Tier 4, positioned only as a combination component. The portfolio backbone is drug targets (mAb, small molecules) and next-generation vaccines (mRNA, epitope-focused subunit).

---

## COVERAGE CHECK

| Disease Stage | Covered? | By Which Candidate(s)? |
|---|---|---|
| Stage 1: Acidosis/rumenitis | YES | G1-3 (butyrate+zinc -- combination), monensin (existing) |
| Stage 2: Rumen wall colonization | YES | G1-1, G1-2, G1-4, G1-7, G1-8 |
| Stage 3: Portal transit | YES | G2-8, G2-9 |
| Stage 4: Hepatic immune evasion (BOTTLENECK) | YES (8 candidates) | G2-1, G2-2, G2-3, G2-4, G2-5, G2-6, G2-7, G2-10 |
| Stage 5: Abscess formation | YES | PG-1, PG-4 (diagnostic) |
| Stage 6: Chronic persistence | YES (intractable) | PG-2 (acknowledged, not pursued) |
| Stage 7: Continuous reseeding / polymicrobial | YES | PG-3, G1-2 (continuous phage in feed) |
| Hindgut pathway | YES (conditional) | G1-5 |

**All disease stages covered.** 8/28 candidates target the bottleneck (Gate 2). The portfolio center is leukotoxin neutralization at the hepatic sinusoid, decomposed into six molecular intervention points.

---

## KEY REFERENCES

1. Saginala S et al. (1997). Effect of F. necrophorum leukotoxoid vaccine on experimentally induced liver abscesses in cattle. J Anim Sci. PMID 9110232.
2. Pillai DK et al. (2021). Leukotoxin production in relation to severity. Anaerobe. DOI: 10.1016/j.anaerobe.2021.102344
3. Schwarz C et al. (2024). Isolation and characterization of six novel F. necrophorum phages. PHAGE. DOI: 10.1089/phage.2023.0028
4. Liu X et al. (2021). Multi-component recombinant subunit vaccine in mice. Front Vet Sci. PMC8685265
5. Xiao J et al. (2009). Immunodominant regions on leukotoxin protein. Vet Res Commun. DOI: 10.1007/s11259-009-9223-6
6. Friberg N et al. (2008). Factor H binding as complement evasion mechanism. J Immunol. DOI: 10.4049/jimmunol.181.12.8624
7. Antiabong JF et al. (2015). Iron limitation and cell density effects on F. necrophorum gene expression. ScienceDirect.
8. Adams et al. (2024). Beta-glucan protects against sepsis-induced Kupffer cell loss. Immunology. DOI: 10.1111/imm.70043
9. Felizari LD et al. (2025). Tannin blend + monensin trial. n=2,986. J Anim Sci.
10. Narayanan S et al. (2001). Cloning, sequencing, expression of leukotoxin gene. Infect Immun. PMID 11500416
11. Kumar A et al. (2013). 42.4 kDa OMP binding to bovine endothelial cells. PMID 23153522
12. Singh K et al. (2022). 43K OMP fibronectin interaction. PMID 35121302
13. Fuerniss LK et al. (2022). Liver abscess microbiota. J Anim Sci. DOI: 10.1093/jas/skac252
14. Salih HM et al. (2025). Hindgut as source of hepatic pathogens. Microbiol Spectr. DOI: 10.1128/spectrum.02539-25
15. Friedman SL (2008). Hepatic stellate cells. Physiol Rev. DOI: 10.1152/physrev.00013.2007
16. Nature (2025). Computational multi-epitope vaccine design for F. necrophorum transmembrane proteins. Sci Rep. DOI: 10.1038/s41598-025-00166-4
17. Elanco press release (2025). $130M mAb manufacturing expansion, Elwood, Kansas.
18. Elanco-Medgene (2025). H5N1 mRNA vaccine for dairy cattle, USDA conditional licensing review.

---

*28 candidates proposed. All disease stages covered. 8 candidates at the bottleneck (Gate 2). Portfolio center: leukotoxin lifecycle interventions. Feed additives relegated to combination components. 5 predictions appended separately to prediction-log.md.*
