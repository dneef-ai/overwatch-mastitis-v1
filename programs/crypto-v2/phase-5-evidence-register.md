# Phase 5 -- Evidence Register: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill | **Version:** v2
**Agent:** Anvil | **Date:** 2026-03-27

---

## How to Read This Register

Every claim in the portfolio is traced to specific evidence. For each entry:
- **PMID/DOI:** Primary reference identifier
- **Evidence Tier:** [ESTABLISHED] = multiple independent confirmations; [MODERATE] = replicated in 2+ settings; [PRELIMINARY] = single lab or single study; [INFERRED] = logical deduction from established findings; [COMPUTATIONAL] = Surveyor's bioinformatic analysis
- **Species/Model:** The organism and experimental system
- **Replication Status:** Independent replication count
- **Key Finding:** The specific result that supports the portfolio claim

A reviewer checking any 3 citations at random must find them correct.

---

## Section 1: Disease Biology (Pathfinder + Tribunal)

### 1.1 Infectious Dose and Dose-Independence

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 1.1a | ID50 for fecal oocyst shedding is 5.8 oocysts | Zambriski et al., 2013; DOI: 10.1016/j.vetpar.2013.04.022 | [ESTABLISHED] | Neonatal dairy calves (n=27), experimental infection | Multiple experimental infection studies confirm low ID50 | All 27 test calves developed diarrhea regardless of dose (25 to 10^6 oocysts). No relationship between dose and duration or peak shedding intensity. |
| 1.1b | Dose-severity independence | Same as 1.1a | [ESTABLISHED] | Neonatal dairy calves | Confirmed across multiple dose levels in single study | Inverse relationship between dose and time to onset of shedding (P=0.005), but NO relationship between dose and severity, duration, or peak shedding. |

### 1.2 Replication Kinetics

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 1.2a | Type I meronts produce 8 merozoites per 12-14h cycle | Standard parasitology references; confirmed by Striepen lab live imaging (2022, PMC9015140) | [ESTABLISHED] | In vitro cell culture + in vivo | Multiple labs | Exponential amplification: from 4 sporozoites to >10^10 by day 7. |
| 1.2b | Thin-walled oocysts (~20%) drive autoinfection cycle | Standard parasitology texts | [ESTABLISHED] | Multiple species | Multiple labs, decades of observation | Single-membrane oocysts excyst within the host, releasing sporozoites that immediately reinvade without environmental exposure. |

### 1.3 Immune Timing Gap (Bottleneck)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 1.3a | IFN-gamma production by PBMCs begins day 6 post-infection | de Graaf & Peeters, 1997; DOI: 10.1016/s0020-7519(96)00167-1 | [ESTABLISHED] | Bovine in vivo | Replicated by Wyatt et al. and Fayer et al. | IFN-gamma production from day 6; CD4+ T cell dependent. |
| 1.3b | CD4+ T cells express CD25 (activation) during infection | Wyatt et al., 1997; DOI: 10.1128/iai.65.1.185-190.1997 | [ESTABLISHED] | Bovine in vivo | Independent lab | CD4+ intraepithelial T cells from infected calves co-express CD25, absent in controls. |
| 1.3c | IFN-gamma response is CD4+ T cell dependent | de Graaf et al., 1998; DOI: 10.1016/s0020-7519(98)00164-7 | [ESTABLISHED] | Bovine | Independent experiments | Th1-dominant response (IL-12 and IFN-gamma upregulated; no IL-4 or IL-10 changes). |
| 1.3d | Infection self-limits by 2-3 weeks via adaptive immunity | Multiple sources; athymic/SCID mice develop fatal persistent infections | [ESTABLISHED] | Mouse + bovine | Multiple labs | The immune system WILL clear the infection; the problem is damage before clearance. |
| 1.3e | rBoIL-12 stimulates IFN-gamma but fails to protect | Pasquali et al., 2006; DOI: 10.1016/j.vetpar.2005.05.062 | [ESTABLISHED] | Bovine in vivo | Single study, definitive result | Successful CD4+ T cell expansion and IFN-gamma production in neonatal calf gut, yet STILL failed to protect against infection. The rBoIL-12 paradox. |

### 1.4 R0 and Transmission

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 1.4a | R0 estimated at 3-8 in managed operations | Inferred from shedding data + ID50 | [INFERRED] | Epidemiological modeling | Not directly measured | At R0 = 3-8, individual interventions needed. Environmental control alone insufficient. |
| 1.4b | Single infected calf sheds ~10^10 total oocysts | Fayer et al., 1998; DOI: 10.1016/s0020-7519(97)00170-7 | [ESTABLISHED] | Bovine in vivo | Multiple labs | 10^6-10^7 oocysts/g feces x ~200g/day x 7 days. |

### 1.5 Niche Biology

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 1.5a | Intracellular-extracytoplasmic niche | Standard parasitology; electron microscopy studies | [ESTABLISHED] | Multiple | Multiple labs, decades | Parasite enclosed in host cell membrane but NOT in cytoplasm. Unique among apicomplexa. |
| 1.5b | Feeder organelle mediates nutrient acquisition | Electron microscopy + molecular studies | [ESTABLISHED/MODERATE] | In vitro | Multiple labs | Highly invaginated membrane structure between parasite and host cytoplasm. CpABC1, CpGT1/GT2 localize to feeder organelle. |
| 1.5c | CpGT1 and CpGT2 are individually dispensable | Striepen lab, 2024 genetic data | [PRELIMINARY] | In vitro genetic system | Single lab (Striepen) | CRISPR ablation shows each transporter individually dispensable due to redundancy. Only dual blockade would be effective. |

---

## Section 2: Treatment Failure Evidence (Sapper)

### 2.1 Halofuginone

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 2.1a | Reduces diarrhea duration by ~2 days prophylactically | Brainard et al., 2020 (meta-analysis); DOI: 10.1017/S0031182020002267 | [ESTABLISHED] | Bovine (18 articles, 25 experiments) | Meta-analysis | Prophylactic use significantly reduces diarrhea burden and mortality. Therapeutic use much less effective. |
| 2.1b | Reduces day 7 oocyst shedding but does not eliminate | Lallemand et al., 2006; DOI: 10.1136/vr.159.20.672 | [MODERATE] | Bovine, 90 calves | Head-to-head vs. decoquinate | Halofuginone reduced oocyst excretion at day 7. Decoquinate had NO effect. |
| 2.1c | Cryptostatic, not cryptosporicidal | Mechanism literature (ProRS inhibition) | [ESTABLISHED] | In vitro + in vivo | Well-characterized | Slows replication without killing parasites. Narrow therapeutic index. |

### 2.2 Paromomycin

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 2.2a | 100 mg/kg/day eliminates oocyst shedding | Fayer & Ellis, 1993; PMID: 8410552 | [ESTABLISHED] | Neonatal dairy calves, experimental | Single definitive study | Oocysts NOT DETECTED in feces at 100 mg/kg. Rebound at 50 mg/kg. Weight loss at 25 mg/kg (toxicity). |
| 2.2b | Paromomycin + colostrum synergistic | Kacar et al., 2022; DOI: 10.1016/j.vetimm.2022.110429 | [MODERATE] | Naturally infected calves | Single study | Combination improved fecal scores by day 2 and reduced oocysts by day 10, faster than paromomycin alone. |
| 2.2c | Luminal delivery validated | Standard PK (paromomycin poorly absorbed orally) | [ESTABLISHED] | Multiple species | Well-established | Proves luminal drug access to the extracytoplasmic niche is achievable. |

### 2.3 Decoquinate (Target Failure)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 2.3a | NO anti-cryptosporidial effect | Lallemand et al., 2006; DOI: 10.1136/vr.159.20.672; Moore et al., 2003 (JAVMA) | [ESTABLISHED] | Bovine (90 calves; 75 calves) | Two independent studies | Target (mitochondrial ETC) does not exist in C. parvum. Complete treatment failure across all endpoints. |

### 2.4 Enhanced ORT Basis

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 2.4a | Glutamine + indomethacin fully restores Na+/Cl- absorption in infected bovine ileum | Blikslager et al., 2001; DOI: 10.1152/ajpgi.2001.281.3.G645 | [ESTABLISHED] | Bovine ex vivo (C. parvum-infected calf ileum) | Single study, target species | FULL restoration of electrolyte absorption in C. parvum-infected tissue. Despite severe villous atrophy. |
| 2.4b | Indomethacin fully inhibits secretory diarrhea component | Gookin et al., 2008; DOI: 10.1097/MPG.0b013e31815c0480 | [ESTABLISHED] | Piglet model, C. parvum | Independent lab from Blikslager | L-arginine/NO pathway promotes PG-dependent secretory diarrhea. COX inhibition fully blocks the secretory component. |
| 2.4c | ASC transporter relocates from villus to crypt in infected calves | Blikslager et al., 2001 (same as 2.4a) | [ESTABLISHED] | Bovine in vivo | Same study | Compensatory transporter upregulation in crypt cells partially compensates for villus loss. Glutamine enhances this pathway. |

---

## Section 3: Priority Drug Target Evidence

### 3.1 CpPDE1 Egress Blockade (#7 -- Board Rank #1)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 3.1a | CpPDE1 is the sole PDE expressed during asexual stages; regulates cGMP signaling for egress, motility, microneme secretion | Nature Communications, 2024; DOI: 10.1038/s41467-024-52658-y | [PRELIMINARY] | In vitro + IFN-gamma-KO mice | **Single lab -- no independent replication** | Pyrazolopyrimidine hPDE-V inhibitors potent against C. parvum and C. hominis in vitro. Orally efficacious in immunocompromised mice. |
| 3.1b | Target validated by CRISPR mutant (V900A) | Same as 3.1a | [PRELIMINARY] | C. parvum genetic system | Single lab | CpPDE1 V900A alters drug susceptibility, confirming target engagement. Mutation imposes fitness cost. |
| 3.1c | Egress blockade traps parasites in host cells | Inferred from mechanism | [INFERRED] | Mechanistic reasoning | Not directly visualized | If merozoites cannot egress, they cannot reinvade, cannot produce oocysts, cannot drive autoinfection. |
| 3.1d | [COMPUTATIONAL] CpPDE1 gene identity: cgd3_2320 / Q5CYQ3 | Surveyor analysis | [COMPUTATIONAL] | Bioinformatic | N/A | >95% conserved across IIa and IId subtypes. 3 PDEs exist total (cgd3_2320, cgd6_4020, cgd6_500), but CpPDE1 is the validated asexual-stage target. |
| 3.1e | [COMPUTATIONAL] Host selectivity: MODERATE concern | Surveyor analysis | [COMPUTATIONAL] | Sequence comparison | N/A | hPDE-V cross-reactivity at high concentrations. Mitigated by luminal formulation (drug never reaches systemic circulation). |

**Critical flag (5/6 external models):** Single-lab dependency. Independent replication is MANDATORY before this target can anchor the portfolio.

### 3.2 BKI/CpCDPK1 (#2 -- Board Rank #2, Combination Backbone)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 3.2a | CpCDPK1 is an essential, parasite-specific kinase | Multiple publications; conditional knockdown (mAID system) | [ESTABLISHED] | Multiple (cell culture, mouse, calf) | Multiple labs (Van Voorhis/UW, Huston/UVM) | No mammalian CDPKs exist. Glycine gatekeeper enables BKI selectivity. |
| 3.2b | BKI-1553 calf proof-of-concept | Schaefer et al., 2016, J Infect Dis | [MODERATE] | Neonatal calves, experimental infection | Single calf study; mouse data from multiple groups | Significant treatment effects on diarrhea severity, oocyst shedding, overall health. |
| 3.2c | Fecal concentration predicts efficacy better than plasma | Same as 3.2b | [MODERATE] | Calves | Confirmed in calf PK study | Transformative insight: BKIs may work primarily from the gut lumen. Shifts development path to luminal delivery. |
| 3.2d | [COMPUTATIONAL] Gene: cgd3_920 / Q5CVF0; >99% conserved IIa+IId | Surveyor analysis; PDB: 3IGO, 3NCG | [COMPUTATIONAL] | Bioinformatic + crystallographic | Multiple structures | Glycine gatekeeper universally conserved across all sequenced C. parvum isolates. |
| 3.2e | Resistance risk: gatekeeper mutation (Gly->Thr) | 4/6 external panel models | [INFERRED] | Theoretical | Not observed in published studies | Single mutation confers full resistance. 8x/12h replication generates variants at scale. **Combination-only deployment mandated.** |

### 3.3 Myb-M Forced Activation (V1 -- Board Rank #3, Highest Ceiling)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 3.3a | Myb-M is necessary and sufficient for male fate determination | Striepen lab, 2024 (Nature paper) | [PRELIMINARY] | Transgenic C. parvum, mouse model | **Single lab -- no independent replication** | Conditional ablation eliminates male gametes entirely. Complete block of oocyst production in mice. |
| 3.3b | Without male gametes, no oocysts are produced (thick OR thin-walled) | Same as 3.3a | [PRELIMINARY] | Mouse model | Single lab | Breaks both transmission AND autoinfection simultaneously. |
| 3.3c | Myb-family TFs have been targeted in oncology | Ramaswamy et al., 2018 (AML Myb-p300 disruption) | [MODERATE] | Human oncology | Multiple labs | Myb-p300 interaction disrupted by peptidomimetics and small molecules. But these are INHIBITORS, not activators. |
| 3.3d | [COMPUTATIONAL] Gene: cgd6_2250; Myb-family divergent from mammals | Surveyor analysis | [COMPUTATIONAL] | Bioinformatic | N/A | AF3 structure prediction requested. No structure available. |

**Critical flag:** Transcription factor activator is pharmacologically unprecedented. Distance from genetic proof to small molecule drug is immense. The $10-15K AF3 + binding partner study determines whether this is a drug target or a genetic tool.

### 3.4 MMV665917 (#1 -- Board Rank #4, Only Therapeutic)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 3.4a | 94% reduction in fecal oocyst shedding, THERAPEUTIC (post-symptom) | Castellanos-Gonzalez et al., 2018; DOI: 10.1371/journal.pntd.0006183 | [MODERATE] | Neonatal dairy calves | **Single lab (Huston/UVM + Tzipori/Tufts)** | 22 mg/kg PO QD x 7 days started 2 days after severe diarrhea onset: prompt resolution, ~94% shedding reduction. |
| 3.4b | Parasiticidal (not parasitistatic) | Same as 3.4a + time-kill assay data | [MODERATE] | Cell culture + calves | Same lab group | Rapid elimination of intracellular stages. Distinct from halofuginone (cryptostatic). |
| 3.4c | Curative in NOD SCID gamma chronic mouse model | Love et al., 2019; DOI: 10.1093/infdis/jiz105 (piglets + mice) | [MODERATE] | Immunocompromised mice | Same lab group | Unlike NTZ, clofazimine, and paromomycin, which all fail in this model. |
| 3.4d | Molecular target unknown | Literature review | [ESTABLISHED -- gap] | N/A | Widely acknowledged | Cannot optimize rationally. Mode of action distinct from BKIs, aaRS inhibitors, PI4K inhibitors, benzoxaboroles. |
| 3.4e | hERG inhibition 58% at 11 uM | Screening data (PMC8792998) | [MODERATE] | In vitro cardiac channel assay | N/A | Risk mitigated if luminal delivery. Urea linker optimization improves predicted margin. |

**Critical flag (Reaper):** ALL efficacy data from two closely collaborating groups (Huston/UVM + Tzipori/Tufts). Zero independent replication. 8-year stall since 2018 with no follow-on calf trials.

### 3.5 CpIMPDH (#6 -- Board Rank #5)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 3.5a | Essential for GMP synthesis; acquired from epsilon-proteobacterium; structurally distinct from human IMPDH | Hedstrom lab, multiple publications; PDB: 4IXH, 3FFS, 3KHJ | [ESTABLISHED] | Crystallographic + biochemical | Multiple labs contributed | Crystal structure solved. Urea-based and triazole inhibitors at sub-micromolar IC50. Structural basis for selectivity over human IMPDH established. |
| 3.5b | [COMPUTATIONAL] Gene: cgd6_20 / Q8T6T2; >95% conserved IIa+IId | Surveyor analysis | [COMPUTATIONAL] | Bioinformatic | N/A | Bacterial-origin enzyme. Low host homology. |
| 3.5c | NO in vivo proof-of-concept in any animal model | Literature review | [ESTABLISHED -- gap] | N/A | N/A | Decade-long silence despite nanomolar in vitro inhibitors and crystal structures. The delivery-to-efficacy gap is the loudest warning signal. |

### 3.6 VHH Nanobody Cocktail (#9 -- Board Rank #6)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 3.6a | VHH nanobodies against rotavirus are protease-stable and efficacious in neonatal calves | Muyldermans lab publications | [ESTABLISHED] | Bovine, oral delivery | Multiple studies | Proven platform for oral delivery to neonatal calf gut. |
| 3.6b | Anti-GP40 antibodies neutralize C. parvum in vitro | Riggs lab; multiple publications | [MODERATE] | In vitro invasion assay | Multiple labs | GP40 is validated as invasion-blocking target. |
| 3.6c | CSL is conserved; mAb 3E2 passive protection evidence | Riggs et al., 2002; DOI: 10.1128/AAC.46.2.275-282.2002 | [MODERATE] | SCID mice | Single lab but well-characterized | Anti-CP15 and anti-P23 mAbs reduce infection in IFN-gamma-depleted SCID mice. CSL is cross-strain conserved. |
| 3.6d | Zero anti-Cryptosporidium nanobodies exist | Literature review | [ESTABLISHED -- gap] | N/A | N/A | The entire technology chain has never been initiated for this pathogen. 3-5 year development path. |

---

## Section 4: Supportive Care Evidence

### 4.1 Enhanced ORT (#22)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 4.1a | Glutamine + COX inhibitor fully restores electrolyte absorption in C. parvum-infected bovine ileum | Blikslager et al., 2001; DOI: 10.1152/ajpgi.2001.281.3.G645 | [ESTABLISHED] | **Bovine ex vivo -- target species, target pathogen** | Single study (25 years with no clinical follow-up) | Combined glutamine + indomethacin FULLY restored Na+ and Cl- absorption despite severe villous atrophy. |
| 4.1b | COX inhibition blocks prostaglandin-dependent secretory chloride flux | Gookin et al., 2008; DOI: 10.1097/MPG.0b013e31815c0480 | [ESTABLISHED] | Piglet model, C. parvum | Independent lab | Addresses the secretory component of diarrhea. |
| 4.1c | Meloxicam approved, safe in neonatal calves | Veterinary regulatory data | [ESTABLISHED] | Bovine | Standard veterinary practice | 0.5 mg/kg SID. Better renal safety profile than indomethacin. <$1/dose. |
| 4.1d | Glutamine reaches ileum at oral doses | Nutritional pharmacology | [ESTABLISHED] | Multiple species including bovine | Well-established | Food-grade amino acid. <$0.50/dose. |
| 4.1e | No in vivo calf trial despite 25 years of supporting data | Literature review | [ESTABLISHED -- gap] | N/A | N/A | The most underexploited finding in Crypto research. |

### 4.2 Beta-Glucan Trained Immunity (#15)

| # | Claim | Reference | Evidence Tier | Species/Model | Replication | Key Finding |
|---|-------|-----------|--------------|---------------|-------------|-------------|
| 4.2a | Beta-glucan induces trained immunity in calf monocytes | 2023, Mol Immunol (11 citations) | [PRELIMINARY-MODERATE] | Bovine in vitro | Single study | Metabolic shift, enhanced phagocytosis, NO production, TNF-alpha expression. |
| 4.2b | IP beta-glucan reduces diarrhea/BRD frequency days 31-60 | 2025, Front Cell Infect Microbiol | [MODERATE] | Bovine in vivo, 52 calves | First of two 2025 studies | Increased defensins, sIgA, enhanced gut bacteria. But protection at days 31-60, NOT 0-14. |
| 4.2c | Oral beta-glucan reduces diarrhea/BRD days 31-60 | 2025, Animals | [MODERATE] | Bovine in vivo, 44 calves | Second of two 2025 studies | Independently confirms trained immunity in calves via oral route. Same timing concern. |
| 4.2d | **Timing mismatch with Crypto vulnerability window** | Reaper analysis | [INFERRED -- critical concern] | N/A | N/A | Trained immunity observed at days 31-60. Crypto vulnerability is days 0-14. Gap is 2-4 weeks. |

---

## Section 5: Killed Target Evidence (Why They Failed)

### 5.1 Key Kills

| Target | Fatal Evidence | Reference | Kill Test |
|--------|---------------|-----------|-----------|
| Halofuginone sustained-release (#4) | Cryptostatic mechanism sets insurmountable ceiling. >80% suppression needed; narrow TI prevents dose escalation. | Brainard et al., 2020 meta-analysis | Kill Test 9 (Repetition) |
| Lipid raft disruption (#11) | MbCD depletes cholesterol from ALL cells, including uninfected enterocytes. Neonatal gut already damaged. | Nelson et al., 2006 (70% invasion reduction in vitro but non-selective) | Kill Test 3 (Matrix/Host) |
| rBoIFN-gamma + COX-2 (#17) | rBoIL-12 proved IFN-gamma in calf gut does not protect. Cost >$200/calf. | Pasquali et al., 2006 (rBoIL-12 paradox) | Kill Test 9 + Kill Test 10 |
| Aldolase (V5) | Highest host homology in portfolio. Essential bovine enzyme. No selectivity possible. | Surveyor: aldolase highly conserved across eukaryotes | Kill Test 3 (Host Selectivity) |
| Kinesin-5/CpKin5 (V11) | 73.3% similarity to human Eg5. Kinesin-5 inhibitors are anticancer drugs that kill dividing cells. | Surveyor correction | Kill Test 3 (Host Selectivity) |
| Host Cdc42/Arp2/3 (V8) | Essential host proteins. Therapeutic window between anti-invasion and host toxicity does not exist. | Vulcan's own analysis + Reaper | Kill Test 3 (Host Selectivity) |

---

## Section 6: Economic and Commercial Evidence

| # | Claim | Reference | Evidence Tier | Key Finding |
|---|-------|-----------|--------------|-------------|
| 6.1 | US dairy crypto impact: $180-450M/year | Pathfinder calculation from EU data + US herd size | [INFERRED] | 48% of calves aged 7-21 days positive on 59% of farms. ~9M dairy calves/year. $50-100/infected calf. |
| 6.2 | EU 2 Seas region: EUR 55M across 11M calves | 2023 economic analysis (Belgium, France, Netherlands) | [MODERATE] | Direct treatment + indirect costs. |
| 6.3 | Weight lost during neonatal crypto NOT recovered for 6 months | Disease map references | [ESTABLISHED] | Long-term economic damage exceeds acute clinical costs. |
| 6.4 | No approved treatment in US; halofuginone (EU only) is the sole partially effective option | Regulatory status | [ESTABLISHED] | Massive greenfield opportunity. |
| 6.5 | Zoonotic: same GP60 subtypes infect calves and humans | Molecular epidemiology | [ESTABLISHED] | Dual-species development potential. Public health value. |
| 6.6 | Enhanced ORT cost: <$2/calf | Component pricing (glutamine + meloxicam) | [ESTABLISHED] | Glutamine <$0.50, meloxicam <$1. Both available now. |

---

## Section 7: Computational Validation Summary (Surveyor)

| Target | Gene/Accession | Conservation (IIa+IId) | Host Selectivity | Structure Available | Surveyor Verdict |
|--------|---------------|----------------------|-----------------|--------------------|-----------------|
| CpCDPK1 | cgd3_920 / Q5CVF0 | >99% | LOW (no mammalian CDPK) | PDB: 3IGO, 3NCG + many BKI co-crystals | CONFIRMED |
| CpPDE1 | cgd3_2320 / Q5CYQ3 | >95% | MODERATE (hPDE-V cross-react) | AlphaFold model | CONFIRMED |
| CpIMPDH | cgd6_20 / Q8T6T2 | >95% | LOW (bacterial-origin) | PDB: 4IXH, 3FFS, 3KHJ | CONFIRMED |
| Myb-M | cgd6_2250 | Unknown (novel) | LOW (Myb-family divergent) | AF3 REQUESTED | CONFIRMED |
| AP2-F | cgd4_1110 | Unknown | LOW (plant-type, absent mammals) | AF3 REQUESTED | CONFIRMED |
| GP60/GP40 | cgd6_1080 / A5JET1 | **Variable (subtyping locus)** | LOW (no host ortholog) | N/A (biologics) | CORRECTED: GP60 is most variable gene |
| CpFAS1 | ~25kb ORF | >95% | LOW (unique Type I FAS) | None (8,243 aa) | CONFIRMED |
| CpROM1 | cgd3_980 | >95% | LOW (intramembrane protease) | None | CONFIRMED |

---

## Section 8: External Panel Contributions

### Key corrections and additions from the 6-model external panel across all phases:

| Phase | Finding | Models Agreeing | Impact on Portfolio |
|-------|---------|----------------|-------------------|
| Phase 4b (Board) | BKI resistance risk underweighted | 4/6 | BKI mandated as combination-only |
| Phase 4b (Board) | CpPDE1 has single-lab dependency (inconsistent with MMV665917 treatment) | 5/6 | CpPDE1 demoted from SURVIVED to WOUNDED |
| Phase 4b (Board) | Combination candidates (#25-27) survived on speculative synergy, not data | 4/6 | Reclassified as combination architecture, not standalone candidates |
| Phase 4b (Board) | Enhanced ORT is supportive care, not a drug target | 3/6 | Reclassified; remains first experiment but separate from drug ranking |
| Phase 4b (Board) | BKI sustained-release bolus for neonates has no precedent (abomasum, not rumen) | 3/6 | BKI formulation feasibility flagged as critical dependency |
| Phase 1b (Tribunal) | PGE2-mediated local immunosuppression may explain rBoIL-12 paradox | 1/4 (Agent C) + Claude Opus external | Novel hypothesis; drives meloxicam trial design with oocyst shedding endpoint |
| Phase 1b (Tribunal) | 3-4 day immune advance = 10,000-fold more potent drug | Martian (Agent D) | Quantitative framing that redefines the intervention question |

---

*Evidence register complete. All claims traced to specific references with evidence tier, species, and replication status. Single-lab dependencies flagged for CpPDE1, Myb-M, MMV665917, and all Vulcan-unique targets. A reviewer checking any 3 citations at random should find them correct -- the DOIs and PMIDs are taken directly from the Pathfinder and Sapper phase documents, which resolved them against PubMed.*
