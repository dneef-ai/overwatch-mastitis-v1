# Phase 5 — Evidence Register: AB03-A Rumen H₂ Sink

**Program:** AB03-A — Rumen H₂ Sink (Biochemistry Mode) | **Internal Agteria** | **Version:** v1
**Agent:** Anvil | **Date:** 2026-03-30

---

## Evidence Standards

Every claim is tagged with:
- **Evidence tier:** ESTABLISHED (textbook/multiple studies) | MODERATE (2-3 studies, consistent) | PRELIMINARY (single study or limited data) | INFERRED (logical extrapolation, no direct data) | COMPUTATIONAL (bioinformatic/structural analysis)
- **Species/model:** In vitro | RUSITEC | Sheep/goat | Cattle (beef/dairy) | Human gut | Other
- **Replication:** Independent replication status
- **Key reference:** PMID/DOI where available

---

## Target 1 (Board Rank #1): HDCR Transplant into *E. limosum* — Candidate 5.2/V1

### The Enzyme: *T. kivui* HDCR

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| HDCR catalyzes H₂ + CO₂ → formate as entry point of Wood-Ljungdahl pathway | Cryo-EM structure at 3.4 A; hexameric filamentous complex; membrane-anchored nanowires | ESTABLISHED | *T. kivui* (thermophilic acetogen) | Multiple labs have characterized HDCR; structure from Schwarz/Mueller lab | PMID 35859174 (Schwarz et al., Nature 2022); PDB 7QV7 |
| kcat = 2,654 s⁻¹ | **CAUTION: This may be for formate OXIDATION (favorable direction), not CO₂ REDUCTION (needed direction).** Board flagged (7/12 external models agreed). The thermodynamic favorability of formate oxidation vs. CO₂ reduction differs. Must measure CO₂ reduction specifically at 39C. | PRELIMINARY — direction of measurement uncertain | In vitro enzyme assay at thermophilic optimum (66C) | Single lab (Schwarz/Mueller) | PMID 35859174 |
| 95x improvement over *A. woodii* HDCR (kcat 28 s⁻¹) | Comparison based on two different labs' measurements under different conditions | MODERATE | In vitro | Different labs — Mueller lab (*T. kivui*) vs. earlier characterization of *A. woodii* | PMID 35859174; *A. woodii* HDCR from earlier work |
| HDCR complex: FdhF (743 aa) + HydA2 (461 aa) + HycB3 (184 aa) + HycB4 (210 aa) + maturation factor FdhD | Structural characterization of subunit composition | ESTABLISHED | *T. kivui* | — | PMID 35859174 |
| HDCR requires 34 [4Fe-4S] clusters across the complex | Structural analysis; iron-sulfur cluster assembly is the major technical challenge for heterologous expression | ESTABLISHED | Structural/biochemical | — | PMID 35859174 |
| Engineered FdhF variants (truncated subunit) retain activity | Demonstrates enzyme is amenable to engineering | PRELIMINARY | In vitro | Single lab | Nature Communications 2024 (Surveyor citation) |
| Activity at 39C is UNKNOWN — no published data | Gap acknowledged by all pipeline agents and external panel | GAP | — | — | — |

### The Host: *E. limosum*

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| CRISPR/Cas9 system with 100% gene targeting efficiency | Genome editing demonstrated | ESTABLISHED | *E. limosum* | Single lab (Shin/Cho, Korea) but multiple published papers | Shin et al., ACS Synth Biol, 2019 |
| CRISPRi genome-wide screen with 41,939 guide RNAs | Comprehensive genetic toolbox | ESTABLISHED | *E. limosum* | — | Jang et al., PNAS 2023 |
| Shuttle vectors, selectable markers, recombineering available | Standard genetic tools | ESTABLISHED | *E. limosum* | Multiple publications | Shin et al., 2022 |
| Genome: 4.15 Mb, 3,805 genes | Reference genome | ESTABLISHED | *E. limosum* SA11 | — | GenBank |
| Full Wood-Ljungdahl pathway; metabolically versatile (sugars, methanol, formate, H₂/CO₂) | Genome annotation + functional studies | ESTABLISHED | *E. limosum* | Multiple studies | Multiple |
| *E. limosum* "is unlikely to be a suitable candidate to take the place of hydrogenotrophic methanogens" (autotrophic growth unlikely in substrate-rich rumen) | Genome-based conclusion: organism defaults to heterotrophy | MODERATE | Computational/in vitro | — | Genome study (Sapper citation) |
| *E. limosum* is NOT truly "rumen-native" — isolated from sludge/human gut | Board finding: calling it rumen-native overstates persistence advantage (3/12 external models) | MODERATE | — | — | Board external panel |
| Rumen persistence: no published data for *E. limosum* specifically | Gap | GAP | — | — | — |
| All non-native DFMs in the rumen show washout within 48-72 hours | Historical pattern from multiple studies | ESTABLISHED | Cattle (various) | Multiple independent studies | Sapper review |

---

## Target 2 (Board Rank #2): *Ca.* Faecousia Cultivation — Candidate 5.1

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| *Ca.* Faecousia dramatically expanded under 3-NOP treatment in dairy calves | Metagenome-assembled genome (MAG) evidence; dose-dependent WLP gene upregulation | PRELIMINARY | Cattle (51 dairy calves) | **SINGLE STUDY — Pope et al., PNAS 2025** | PMID 41052332 |
| Full Wood-Ljungdahl pathway genes identified in MAG (15 genes) | Genome annotation from metagenomic assembly | PRELIMINARY [COMPUTATIONAL] | MAG reconstruction | Single study | PMID 41052332 |
| 62% CH₄ reduction with 3-NOP in calves; "strong reduction of methanogens and stimulation of reductive acetogens" | Primary outcome of Pope et al. | ESTABLISHED (for CH₄ reduction) / PRELIMINARY (for acetogen response) | Cattle (dairy calves) | Single study, but n=51 | PMID 41052332 |
| "No effect on dietary intake or animal performance" at 62% CH₄ reduction | Calf performance data | ESTABLISHED | Cattle (dairy calves) | Single study, n=51 | PMID 41052332 |
| Organism has NEVER been cultivated in pure culture | Gap | GAP | — | — | — |
| H₂ threshold for autotrophic growth is UNKNOWN | Gap — may have same high threshold as other rumen acetogens | GAP | — | — | — |
| Whether organism is present across breeds, diets, and geographies is UNKNOWN | Gap — Pope study used single herd | GAP | — | — | — |
| Belongs to Eubacteriaceae (same family as *E. limosum*) | Phylogenetic assignment from MAG | PRELIMINARY [COMPUTATIONAL] | MAG | — | PMID 41052332 |

---

## Target 3 (Board Rank #3): Quinone/Flavin Redox Mediator Shuttle — Candidate 8.1/V6

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| *L. plantarum* performs extracellular electron transfer (EET) via riboflavin and quinones, increasing NAD⁺/NADH ratio | Demonstrated in lactic acid bacteria | PRELIMINARY | *L. plantarum* (not rumen) | 2-3 studies | eLife 2022; mBio 2023 |
| DHNA (1,4-dihydroxy-2-naphthoic acid) acts as quinone shuttle for EET | Mechanism characterized in LAB | PRELIMINARY | *L. plantarum* | — | mBio 2023 |
| AQDS (anthraquinone-2,6-disulfonate) E°' = −184 mV; well-characterized electron shuttle in anaerobic digestion | Electrochemistry established | ESTABLISHED | Anaerobic digestion systems | Multiple labs | Various |
| AQDS is TOXIC to bacteria at >10 mM; toxic to methanogens at 20 mM | Surveyor correction; narrows working range to <10 mM | MODERATE | In vitro (AD systems) | Multiple studies | Surveyor citation |
| No rumen-specific data exists for ANY quinone mediator | Critical gap — mechanism entirely unvalidated in rumen bacteria | GAP | — | — | — |
| Whether rumen cellulolytic bacteria can interact with quinone mediators is UNKNOWN | Gap — EET demonstrated only in LAB, not in *Ruminococcus*, *Fibrobacter*, or *Prevotella* | GAP | — | — | — |
| DHNA and riboflavin are safer alternatives to AQDS | DHNA is a bacterial metabolite; riboflavin is vitamin B₂ | ESTABLISHED (safety) | General | — | — |

---

## Target 4 (Board Rank #4): PEP Carboxylase Engineering — Candidate 4.1/V5

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| PEP carboxylase overexpression increases succinate/propionate in *E. coli* | Standard metabolic engineering strategy; 3.5x succinate titer increase | ESTABLISHED | *E. coli* | Multiple labs | PMC3754722 and others |
| PPC overexpression beyond optimal range DECREASES growth and product formation | Surveyor correction; expression must be tuned, not maximized | ESTABLISHED | *E. coli* | Multiple studies | PMC3754722 |
| *Prevotella ruminicola* possesses PEP carboxylase and fumarate reductase | Genome annotation | ESTABLISHED [COMPUTATIONAL] | *P. ruminicola* 23 (type strain) | — | NCBI genome |
| *Prevotella* genetic tools are SEVERELY LIMITED — no established transformation protocol | Gap; limits engineering in the most relevant organism | GAP | — | — | — |
| *Selenomonas ruminantium* is a partial alternative (narGHJI operon characterized; genome AP012049) | Genome available but tools also limited | MODERATE [COMPUTATIONAL] | *S. ruminantium* | — | NCBI AP012049 |
| Vulcan extension: full reductive arm (pyc + mdh + fumB + frdABCD + scpABC) could capture 10-15 mol [2H]/day (17-26% of displaced H₂) | Stoichiometric estimate | INFERRED | Theoretical | — | Vulcan analysis |

---

## Target 5 (Board Rank #5): Engineered Adhesin Display (Mru_1499) — Candidate 2.1/V2

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| Mru_1499 adhesin from *M. ruminantium* M1 binds broad range of H₂-producing microorganisms | Phage display + co-culture binding assays | ESTABLISHED | *M. ruminantium* + rumen organisms | **SINGLE LAB — AgResearch/Massey (Ng/Leahy/Attwood)** | PMID 26643468 (Ng et al., Environ Microbiol, 2016) |
| Domain architecture: signal peptide (aa 1-18), four Big_1 domains, transglutaminase domain | Protein characterization | ESTABLISHED | *M. ruminantium* M1 | — | PMID 26643468; genome CP001719 |
| AdLP-D1 domain (aa 19-198) is sufficient for protozoa binding | Truncation analysis | MODERATE | Recombinant protein | Single lab | Subharat et al., 2022 |
| AdLP-D1 was expressed in *E. coli* and retained immunological reactivity | Epitope mapping study — but this is for IMMUNOLOGICAL reactivity, not FUNCTIONAL adhesion from a bacterial surface | MODERATE (expression) / GAP (functional display) | *E. coli* recombinant | Single lab (same group — AgResearch/Massey) | Subharat et al., 2022 |
| Functional heterologous display on a bacterial surface has NOT been demonstrated | Critical gap — no evidence that the adhesin works when displayed on a non-archaeal surface | GAP | — | — | — |
| Protozoal predation risk: adhesin binds protozoa, potentially making the DFM a target for predation | Board finding (5/12 external models flagged) | INFERRED | Theoretical | — | Board external panel |
| Mru_1499 is immunogenic (vaccine antigen) — mucosal IgA clearance may occur if cattle have pre-existing anti-Mru_1499 immunity | Board finding | INFERRED | Theoretical | — | Board external panel; Subharat 2022 was vaccine development |
| Archaeal glycosylation may be required for binding function — absent in bacterial hosts | 8/12 external models flagged concern | INFERRED | Theoretical | — | Board external panel |

---

## Target 6 (Board Rank #6): Encapsulated Nitrate at Safe Dose — Candidate 6.1

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| Encapsulated nitrate reduced CH₄ by 18.5% (g CH₄/kg forage DMI) in grazing steers | In vivo efficacy with safety | MODERATE | Cattle (beef, grazing) | 2-3 studies (Lee et al., 2019; Duthie et al., 2018) | Lee et al., 2019; Duthie et al., 2018 |
| Blood methemoglobin below detection limit at tested doses | Safety data | MODERATE | Cattle | 2-3 studies | Lee et al., 2019 |
| At safe dose (20-30 g NaNO₃/day), captures 5-7% of displaced H₂ at 30% inhibition | Board-corrected stoichiometric estimate (down from Reaper's 10-15%) | INFERRED (stoichiometry) | — | — | Board calculation |
| EFSA BMDL₁₀ = 64 mg nitrate/kg BW/day (~38 g NaNO₃/day for 600 kg cow) | Regulatory safety limit | ESTABLISHED | Cattle | EFSA evaluation | EFSA opinion |
| Individual animal variability in nitrite reductase capacity creates safety liability | Acknowledged gap; "variable and poorly understood" | MODERATE | Cattle | Multiple observations | Multiple (Sapper review) |
| Cost: ~$0.05-0.15/head/day at proposed doses | Economic estimate | MODERATE | — | — | Reaper analysis |

---

## Target 7 (Board Rank #7): Phloroglucinol + *Coprococcus* — Candidate X.2/V7

| Claim | Evidence | Tier | Species/Model | Replication | Reference |
|-------|----------|------|---------------|-------------|-----------|
| 50.6% H₂ reduction in Brahman steers with phloroglucinol | In vivo H₂ reduction (n=8, short trial, chloroform as inhibitor) | PRELIMINARY | Cattle (beef, Brahman, n=8) | **SINGLE LAB — Martinez-Fernandez/CSIRO, Australia** | PMID 29051749 (Martinez-Fernandez et al., Front Microbiol, 2017) |
| 93% formate reduction — unique dual H₂ + formate capture | Only candidate capturing formate | PRELIMINARY | Cattle (as above) | Single study | PMID 29051749 |
| "205% weight gain improvement" | **UNRELIABLE — n=4 per group, 16-day trial** | PRELIMINARY (overstated) | Cattle (n=4) | Single study, very small n | PMID 29051749 |
| Dairy cow trial (2024) showed NO phloroglucinol metabolism in rumen | Failure to replicate in different breed | PRELIMINARY (negative) | Cattle (dairy) | Different group from Martinez-Fernandez | 2024 study (Reaper citation) |
| *Coprococcus* significantly increased in responding animals (Brahman) | Microbial correlate | PRELIMINARY | Cattle (Brahman) | Single study | PMID 29051749 |
| Phloroglucinol reductase characterized (EC 1.3.1.57, 78 kDa homodimer, *E. oxidoreducens* G-41) | Enzyme known | ESTABLISHED | In vitro | — | Surveyor report |
| Intraruminal delivery at 450 g/day required — oral dosing not validated | Delivery limitation | PRELIMINARY | Cattle | Single study | PMID 29051749 |
| Cost at effective dose: $2.40-13.50/head/day | Exceeds C1 constraint ($0.50/head/day threshold) | INFERRED | — | — | Reaper stoichiometric analysis |

---

## Foundational Evidence (System-Level)

### Rumen H₂ Metabolism Under Methanogenesis Inhibition

| Claim | Evidence | Tier | Reference |
|-------|----------|------|-----------|
| Methanogenesis consumes ~48% of total metabolic hydrogen (batch) / 70-80% of gaseous H₂ | Quantitative H₂ balance | ESTABLISHED | Ungerfeld, Front Microbiol, 2015 (meta-analysis) |
| Dissolved H₂ rises from 0.2-15 uM to 40-54 uM under 3-NOP | Direct measurement in cannulated cattle | ESTABLISHED | Wang et al., 2016; Ungerfeld 2020 |
| 37-72% of displaced H₂ is "missing" — neither accumulates as gas nor redirects to known sinks | Meta-analysis finding | ESTABLISHED | Ungerfeld, 2015 |
| H₂ pool turnover: 0.2-0.9 seconds | Tribunal Martian calculation from measured parameters | INFERRED (calculation) | Tribunal Phase 1b |
| Fumarate reducers at 40 uM H₂ operate at ~89% of Vmax | Km-based calculation (Km ~5 uM) | INFERRED (calculation) | Tribunal Phase 1b |
| Dissolved H₂ supersaturated 38-43x relative to headspace | Direct measurement (Tibetan sheep) | ESTABLISHED | Wang et al., Front Microbiol, 2016 |
| At 100% inhibition, acetogenesis DG' = -50 kJ/mol — strongly thermodynamically favorable | Thermodynamic calculation | ESTABLISHED | Ungerfeld, 2015 |
| Fumaric acid supplementation offers "no measurable impact on methane emissions in beef and dairy cattle" | 2025 meta-analysis | ESTABLISHED | J Anim Sci, 2025 meta-analysis |
| *Sporomusa ovata* H₂ threshold = 6 Pa (Km(H₂) = 3 ± 1 uM) | Verified by Board panel (DeepSeek) | MODERATE | PMID 25281745 (Schuchmann & Muller, 2014, J Biol Chem) |

---

## Citation Verification Status

All PMIDs listed above should be independently verified before external communication. The following are confirmed by multiple pipeline agents and external panel:

- PMID 35859174 — Schwarz et al., Nature 2022 (*T. kivui* HDCR structure) — CONFIRMED
- PMID 41052332 — Pope et al., PNAS 2025 (*Ca.* Faecousia under 3-NOP) — CONFIRMED
- PMID 26643468 — Ng et al., Environ Microbiol, 2016 (Mru_1499 adhesin) — CONFIRMED
- PMID 29051749 — Martinez-Fernandez et al., Front Microbiol, 2017 (phloroglucinol) — CONFIRMED
- PMID 25281745 — Schuchmann & Muller, J Biol Chem, 2014 (*S. ovata* H₂ threshold) — CONFIRMED by DeepSeek (Board panel)
- PDB 7QV7 — HDCR cryo-EM structure — CONFIRMED
- PDB 1QLA — *W. succinogenes* QFR structure — CONFIRMED (Lancaster et al., Nature, 1999)
- PDB 7Z0S — *E. coli* FHL complex cryo-EM — CONFIRMED

**Unverified or uncertain citations:**
- *A. woodii* electrocompetent cell protocol (PMC12345282) — Surveyor citation, PMID appears potentially fabricated (sequential digits); must verify
- 2024 dairy cow phloroglucinol trial — no PMID provided; must locate
