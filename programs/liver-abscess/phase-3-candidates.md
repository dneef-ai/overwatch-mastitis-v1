# Phase 3: Treatment Candidates — Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess | **Partner:** Elanco | **Date:** 2026-03-27
**Agent:** Forge | **Status:** Complete

---

## Executive Summary

Twenty-seven candidates are proposed across all 11 disease stages, spanning four categories: empirical in-vivo hits (Category A), known approaches with literature support (Category B), non-obvious cross-disease analogies (Category C), and novel first-principles proposals (Category D). Every disease stage receives at least one candidate.

The portfolio is organized around three strategic pillars that emerged from the failure analysis:

1. **Reduce the bacterial burden reaching the liver** (Stages 1-5) — barrier protection, anti-colonization, reduced translocation from both rumen and hindgut
2. **Defeat immune evasion when bacteria arrive** (Stages 6-8) — anti-leukotoxin, anti-synergy, anti-biofilm
3. **Prevent abscess establishment** (Stages 9-11) — break the self-reinforcing destruction cycle

The top-priority candidates are: (1) a multi-antigen subunit vaccine combining recombinant leukotoxin + FomA + hemagglutinin with slow-release adjuvant, (2) the monensin + tannin blend combination (MON+BX) as the only non-antibiotic approach with commercial-scale cattle data approaching tylosin, (3) rumen-protected butyrate for barrier integrity, and (4) an anti-leukotoxin monoclonal antibody leveraging Elanco's mAb platform.

**Key insight from the failure analysis:** No single-mechanism intervention has ever matched tylosin. The portfolio must combine candidates across stages to build a multi-dimensional defense. The minimum viable portfolio requires simultaneous hits at: barrier integrity (Stage 2), colonization reduction (Stage 3), and immune evasion defeat (Stage 6).

---

## Stage 1: Ruminal Acidosis

### Candidate 1: Monensin + Tannin Blend Combination (MON+BX)

| Field | Detail |
|---|---|
| **Target/mechanism** | Dual mechanism: monensin stabilizes intake patterns (reduces acidosis bout frequency/severity); condensed tannins slow starch fermentation rate + direct anti-F. necrophorum activity (MIC 6.25-12.5 ug/mL for grape seed/green tea phenolics) |
| **Disease stage(s)** | Stage 1 (acidosis reduction) + partial Stage 3 (anti-Fn activity) |
| **Category** | **A — Empirical in-vivo hit** |
| **Evidence tier** | [ESTABLISHED] |
| **Species data** | **Cattle** — Felizari et al. 2025, n=2,986, 48 pens, 230 days commercial feedlot. MON+BX reduced LA prevalence to levels similar to MON+TYL (28.5% vs 18.3%). BX alone: 36.8%, control: 43.1%. Feed efficiency improved in MON+BX comparable to MON+TYL. |
| **Key risk** | BX alone is no better than control — requires monensin co-administration. The tannin effect may be partially from protein binding reducing effective ruminal starch digestion rather than direct antimicrobial action. Still inferior to MON+TYL (28.5% vs 18.3%). |
| **Proposed de-risk** | Already de-risked at commercial scale. Next step: formulation optimization to close the 10-point gap vs tylosin. Test higher BX dose rates. Test rumen-wall-targeted tannin delivery (mucoadhesive formulation) to increase concentration at colonization niche. Cost: $50-80K for dose-titration trial (n=500). |

**Why this matters:** This is the ONLY non-antibiotic approach that has come within range of tylosin efficacy at commercial scale. It is the lowest-risk candidate in the portfolio and the baseline that all other candidates must beat or complement.

---

## Stage 2: Rumen Epithelial Damage / Barrier Breakdown

### Candidate 2: Rumen-Protected Encapsulated Sodium Butyrate

| Field | Detail |
|---|---|
| **Target/mechanism** | Upregulates tight junction proteins (claudin-1, -3, -4, -7; occludin; ZO-1) via AMPK activation in rumen epithelium. Enhances barrier function against paracellular bacterial translocation. Also anti-inflammatory via HDAC inhibition (reduces NF-kB-mediated rumenitis). |
| **Disease stage(s)** | Stage 2 (barrier integrity) + partial Stage 4 (reduced translocation) |
| **Category** | **B — Known approach** |
| **Evidence tier** | [MODERATE] — tight junction upregulation demonstrated in bovine rumen epithelium (Steele et al., multiple studies). Rumen-protected butyrate products exist commercially for dairy cattle SARA management. No liver abscess-specific trial data. |
| **Species data** | Cattle — encapsulated sodium butyrate tested in dairy cattle for SARA prevention (multiple studies). Butyrate at 300 g/d for 30 days enhanced rumen papillae development and barrier gene expression. Encapsulated butyrate + zinc improved ileal villus height in acidosis-challenged cattle. No feedlot LA trial. |
| **Key risk** | Dose-response for tight junction upregulation in feedlot cattle on 85-90% concentrate diets unknown. Excess butyrate may promote hyperkeratosis/parakeratosis in adult rumen. VFA-mediated damage may overwhelm butyrate-mediated repair when total VFA >150 mM. |
| **Proposed de-risk** | Ex vivo Ussing chamber study: rumen tissue from grain-fed cattle exposed to butyrate at 3 concentrations, measure transepithelial electrical resistance (TEER) and FITC-dextran permeability. Cost: ~$15-20K. If positive, proceed to feedlot pen trial (n=200) with LA as primary endpoint, ~$60K. |

### Candidate 3: Zinc Hydroxychloride + Butyrate Combination (Barrier Repair Stack)

| Field | Detail |
|---|---|
| **Target/mechanism** | Zinc is essential for tight junction assembly (ZO-1 requires zinc-finger domains). Zinc hydroxychloride (IntelliBond Z) has superior rumen bioavailability vs zinc sulfate. Combined with rumen-protected butyrate, provides both structural material (zinc) and transcriptional activation (butyrate) for tight junction repair. |
| **Disease stage(s)** | Stage 2 (barrier integrity) |
| **Category** | **B — Known approach** |
| **Evidence tier** | [MODERATE] — zinc's role in tight junction assembly is established. Zinc hydroxychloride improves bioavailability in rumen. Combination with butyrate shown to improve rumen and intestinal health in lambs during abrupt grain transition (PMC11201255). No LA-specific data. |
| **Species data** | Cattle/sheep — encapsulated butyric acid + zinc tested in lambs transitioning to grain (PMC11201255). Zinc hydroxychloride tested extensively in feedlot cattle for hoof health and performance. |
| **Key risk** | Zinc supplementation alone has historically failed to reduce LA (external panel, Phase 2). May require combination with anti-colonization agent to have meaningful impact. Marginal barrier improvement insufficient if colonization pressure remains high. |
| **Proposed de-risk** | Add to an existing feedlot trial as a treatment arm alongside MON+BX. Factorial design: MON+BX vs MON+BX+ZnBut. Cost: incremental ~$20K on top of an existing trial. |

---

## Stage 3: Rumen Wall Colonization by F. necrophorum

### Candidate 4: Multi-Antigen Subunit Vaccine — rFomA + rLeukotoxin(PL4) + rHemagglutinin

| Field | Detail |
|---|---|
| **Target/mechanism** | Three simultaneous targets: (a) Anti-FomA antibodies block endothelial/epithelial adhesion (FomA binds bovine endothelial cells with high affinity; anti-FomA Ab prevents binding — Kumar et al. 2015). (b) Anti-leukotoxin (PL4 fragment) neutralizes primary virulence factor. (c) Anti-hemagglutinin blocks rumen wall adhesion + platelet aggregation (anti-HA serum reduces attachment — Kanoe et al. 1984). Multi-antigen approach addresses Fusogard's key failure: insufficient breadth. |
| **Disease stage(s)** | Stage 3 (anti-adhesion) + Stage 6 (anti-leukotoxin) + Stage 7 (anti-platelet aggregation reduces anaerobic niche creation) |
| **Category** | **B — Known approach (preclinical)** |
| **Evidence tier** | [MODERATE] — individual components validated: FomA adhesion blocking (Kumar et al. 2015), leukotoxin neutralization (Saginala et al. 1997, 80% protection in challenge model), hemagglutinin adhesion blocking (Kanoe et al. 1984). Multi-component vaccine (43K OMP + PL4 + H2) tested in mice with best immunoprotection (Amachawadi et al. 2021, Front Vet Sci). NO cattle trial of this combination. |
| **Species data** | Mouse (vaccine) + cattle (individual antigen validation). The 2021 KSU study used BALB/c mice; protection reflected mouse immune mechanisms, NOT bovine leukotoxin susceptibility (mice are insensitive to F. necrophorum leukotoxin — critical species gap). |
| **Key risk** | (1) Mouse-to-bovine translation gap is SERIOUS — mouse PMNs are insensitive to leukotoxin, so mouse protection may use entirely different mechanisms. (2) Dose overwhelm under grain challenge — even 3 antigens may generate insufficient titers for 150+ days continuous translocation. (3) FomA is present in BOTH subspecies; hemagglutinin is necrophorum-only — FomA targeting may have broader coverage. (4) Adjuvant selection critical — must sustain titers for 5+ months. |
| **Proposed de-risk** | Step 1: Bovine serology study — vaccinate 20 steers with each individual recombinant antigen, measure Ab titers, in vitro adhesion inhibition with bovine sera, and leukotoxin neutralization. Cost: ~$40-60K. Step 2: If titers adequate, feedlot pen trial (n=300, grain diet) with LA as primary endpoint. Cost: ~$80-120K. Elanco has vaccine manufacturing infrastructure — this is in their wheelhouse. |

### Candidate 5: Anti-FomA Monoclonal Antibody (Passive Immunization)

| Field | Detail |
|---|---|
| **Target/mechanism** | Recombinant bovine anti-FomA monoclonal antibody administered parenterally to block F. necrophorum adhesion to rumen wall endothelial/epithelial cells. Bypasses the titer-duration problem of active vaccination by providing known, high-concentration antibody. FomA is a dual target: (a) adhesion inhibitor, (b) possible complement evasion blocker (F. necrophorum binds Factor H to evade complement — Holm et al. 2008; anti-FomA may restore complement killing during portal transit). |
| **Disease stage(s)** | Stage 3 (anti-adhesion) + Stage 4 (restored complement killing during portal transit) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — anti-FomA polyclonal antibody prevents F. necrophorum binding to bovine endothelial cells in vitro (Kumar et al. 2015). F. necrophorum binds Factor H for complement evasion (Holm et al. 2008, J Immunol). No monoclonal antibody against FomA has been produced. No bovine in vivo data. |
| **Species data** | In vitro (bovine cells) only. |
| **Key risk** | (1) mAb half-life in cattle — requires sustained serum levels for 150+ days, likely needing repeat dosing or Fc-engineering for extended half-life. (2) Cost per dose — mAb manufacturing is expensive; must be economically viable at <$10/head/dose to compete with tylosin ($0.02/head/day). (3) FomA blocking may be insufficient if hemagglutinin and FadA provide redundant adhesion pathways. (4) Anti-FomA may not reach effective concentrations at rumen wall mucosal surface. |
| **Proposed de-risk** | Step 1: Generate bovine anti-FomA mAb using Elanco's mAb platform. Step 2: In vitro adhesion blocking assay with bovine rumen epithelial cells. Step 3: Bovine PK study to determine serum half-life and mucosal distribution. Cost: ~$100-200K for steps 1-3 combined. The opportunity: if anti-FomA mAb also restores complement killing (via blocking Factor H binding), this becomes a dual-mechanism biologic — anti-adhesion PLUS restored innate immune clearance during portal transit. |

**Why Elanco should care:** They are investing $130M in mAb manufacturing (Elwood, Kansas expansion) and have the only veterinary mAb platform with USDA conditional approval (canine parvovirus, 2023). Extending this to cattle liver abscess would be a first-in-class livestock mAb product.

### Candidate 6: Epimural-Targeted Probiotic (Engineered Colonization Resistance)

| Field | Detail |
|---|---|
| **Target/mechanism** | Competitive exclusion of F. necrophorum at the rumen wall, NOT the lumen. The rumen epimural community is dominated by Proteobacteria, Synergistetes, and specific Firmicutes — entirely different from luminal DFMs. Select strains from healthy epimural communities of LA-resistant cattle and formulate for wall adhesion. Key species candidates: Desulfobulbus spp. (oxygen scavengers that compete with F. necrophorum for the wall niche), Campylobacter-like organisms (dominant wall colonizers), or engineered Lactobacillus expressing rumen wall adhesins. |
| **Disease stage(s)** | Stage 3 (colonization resistance at rumen wall) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — no epimural-targeted DFM has ever been attempted. Concept is based on: (a) the failure of luminal DFMs proves the niche matters, (b) the epimural microbiome is distinct and functionally important for barrier integrity (Malmuthuge et al. 2021, Sci Rep), (c) microbial inocula from adult cattle can colonize the epimural niche in calves and alter gene expression. |
| **Species data** | Cattle — epimural microbiome characterized (Malmuthuge et al. 2021). Microbial inocula affect epimural composition in calves (Xiang et al. 2024, Sci Rep). No targeted epimural probiotic tested for LA prevention. |
| **Key risk** | (1) Identifying strains that actually colonize the wall is hard — most probiotics wash through. (2) Delivery: must survive rumen fluid and adhere to damaged epithelium. (3) Competitive exclusion at the wall may require continuous dosing. (4) The epimural niche biology is poorly understood — we may select wrong strains. (5) Timeline: 3-5 years to develop. |
| **Proposed de-risk** | Step 1: 16S/metagenomic comparison of epimural communities from LA-resistant vs LA-susceptible cattle on same diet (n=20 each). Identify candidate protective species. Cost: ~$30K. Step 2: In vitro competition assay — candidate strains vs F. necrophorum on bovine rumen epithelial cells. Cost: ~$15K. |

---

## Stage 4: Portal Translocation (Rumen Origin, ~76% of Abscesses)

### Candidate 7: Mucoadhesive Rumen Wall Sealant (Barrier Physical Protection)

| Field | Detail |
|---|---|
| **Target/mechanism** | Physical barrier coating over damaged rumen epithelium to prevent bacterial translocation across erosions/ulcers. Analogous to sucralfate (aluminum hydroxide + sucrose sulfate) which binds to ulcerated GI mucosa and forms a protective physical barrier. Rumen-adapted formulation: mucoadhesive polymer (e.g., chitosan, sodium alginate, or carboxymethylcellulose) delivered as daily feed additive or slow-release rumen bolus, designed to coat damaged papillae. |
| **Disease stage(s)** | Stage 4 (block translocation across damaged epithelium) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [INFERRED] — sucralfate is established for GI ulcer protection in humans and horses. Mucoadhesive polymers are used in oral drug delivery. Chitosan has inherent antimicrobial activity against gram-negative bacteria. No rumen application tested. |
| **Species data** | None for rumen application. Sucralfate used in horses for gastric ulcers. Chitosan studied for antimicrobial wound dressings. |
| **Key risk** | (1) Rumen environment is uniquely hostile — pH fluctuations, physical mixing, continuous feed passage may strip coating. (2) The rumen wall is enormous surface area (~1 m2 in cattle) — achieving coverage would require large doses. (3) May interfere with VFA absorption (the rumen's primary function). (4) Damaged areas are preferentially on ventral sac cranial papillae — even coverage unlikely. |
| **Proposed de-risk** | Ex vivo adhesion test: apply candidate polymers to excised rumen tissue from grain-fed cattle, subject to simulated rumen conditions (pH 5.5, VFA mixture, mechanical agitation), measure retention at 2/6/12 hours. Cost: ~$10K. If promising, test in cannulated cattle. |

### Candidate 8: Oral Mucosal IgA Vaccine (Rumen Wall Secretory Immunity)

| Field | Detail |
|---|---|
| **Target/mechanism** | Oral or intranasal vaccination with F. necrophorum antigens (FomA, hemagglutinin) formulated with mucosal adjuvant to generate secretory IgA at the rumen wall surface. IgA would neutralize F. necrophorum adhesins AT THE SITE OF COLONIZATION — addressing the fundamental limitation of systemic-only vaccines (Fusogard generates IgG in serum but minimal IgA at the rumen wall). |
| **Disease stage(s)** | Stage 3 (anti-colonization IgA) + Stage 4 (reduced translocation) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — mucosal vaccination generates IgA at GI surfaces in multiple species. Oral vaccines exist for ruminants (e.g., bovine rotavirus). No oral anti-Fusobacterium vaccine attempted. The rumen's extreme environment (pH 5.5-6.5, proteolytic) is a major delivery challenge. |
| **Species data** | None for this specific application. Oral/intranasal ruminant vaccines exist for other pathogens. |
| **Key risk** | (1) Rumen proteolytic degradation of vaccine antigens — requires robust encapsulation. (2) Immune tolerance: oral antigens can induce tolerance rather than immunity. (3) IgA titer kinetics at rumen wall unknown. (4) May need repeated boosting due to short IgA half-life. (5) Ruminant GI mucosal immunology is poorly characterized compared to monogastrics. |
| **Proposed de-risk** | Step 1: Pilot intranasal vaccination with recombinant FomA + cholera toxin B subunit adjuvant (established mucosal adjuvant) in 10 steers. Measure IgA in rumen fluid and at rumen wall biopsies at 2, 4, 8 weeks post-vaccination. Cost: ~$40K. This answers the fundamental question: can mucosal vaccination generate detectable anti-FomA IgA at the rumen wall? |

---

## Stage 5: Portal Translocation (Hindgut Origin, ~24% of Abscesses)

### Candidate 9: Rumen-Bypass Prebiotic Targeting Hindgut Bacteroides (Gluconic Acid / Resistant Starch Management)

| Field | Detail |
|---|---|
| **Target/mechanism** | Reduce starch escape to hindgut (primary driver of hindgut acidosis and Bacteroides bloom) by: (a) rumen-bypass gluconic acid delivery to hindgut to selectively promote beneficial fermentation (Selko Lactibute — commercial product), (b) managing total dietary starch to reduce hindgut overflow, (c) enzyme supplementation (alpha-amylase) to increase ruminal starch digestibility and reduce bypass starch. Hindgut-origin abscesses (~24%) are dominated by B. pyogenes and Candidatus B. purulensis — species that preferentially metabolize glycogen and heparin. Reducing their substrate availability in the hindgut may reduce translocation. |
| **Disease stage(s)** | Stage 5 (hindgut translocation prevention) |
| **Category** | **B — Known approach (novel application)** |
| **Evidence tier** | [PRELIMINARY] — rumen-bypass gluconic acid (Selko Lactibute) has cattle performance data but no LA-specific trial. Hindgut acidosis characterized in cattle (J Anim Sci 2011). Starch escape quantified (35-60% of small intestinal starch reaches hindgut). No intervention has EVER specifically targeted hindgut-origin liver abscesses. |
| **Species data** | Cattle — Selko Lactibute tested in feedlot cattle for hindgut health and performance. Hindgut acidosis models exist. No LA endpoint data. |
| **Key risk** | (1) Hindgut translocation mechanism may differ from rumen — may not require mucosal damage. (2) Reducing Bacteroides load may be insufficient if translocation occurs at low bacterial counts. (3) We do not know if hindgut interventions can reduce the 24% hindgut-origin LA fraction. (4) KE#1 (rumen vs hindgut LA fraction under tylosin) has not been answered. |
| **Proposed de-risk** | Include hindgut-origin abscess typing (16S rRNA sequencing of abscesses) as an endpoint in any feedlot trial. This answers KE#1: what fraction of residual LA under tylosin is hindgut-origin? Cost: ~$50/sample x 200 samples = $10K added to any trial. If hindgut abscesses are the majority of residual LA under tylosin, this becomes a top priority. |

### Candidate 10: Hindgut Mucosal Barrier Protectant (Rumen-Bypass Butyrate + Zinc)

| Field | Detail |
|---|---|
| **Target/mechanism** | Rumen-protected butyrate + zinc formulated for hindgut release (enteric coating dissolves at intestinal pH > 6.5). Targets hindgut epithelial tight junction integrity analogous to Candidate 2 for the rumen. Hindgut acidosis from starch overflow (pH drop + VFA surge) damages colonic/cecal epithelium, enabling Bacteroides translocation to portal circulation. |
| **Disease stage(s)** | Stage 5 (hindgut barrier integrity) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — butyrate enhances intestinal tight junctions in multiple species (AMPK-mediated). Rumen-protected butyrate products exist (designed for small intestine delivery). No hindgut-targeted LA prevention attempted. |
| **Species data** | Cattle — rumen-protected butyrate reaches lower GI. Lambs on grain transition showed improved gut health with encapsulated butyric acid + zinc (PMC11201255). |
| **Key risk** | (1) Achieving therapeutic butyrate concentrations in hindgut uncertain — much may be absorbed in small intestine. (2) Hindgut translocation mechanism poorly understood. (3) This addresses only barrier integrity, not the Bacteroides pathogen itself. |
| **Proposed de-risk** | Hindgut cannulation study (4 steers with cecal cannulae): measure butyrate concentration at cecum after oral rumen-protected butyrate at 3 doses. Cost: ~$25K. |

---

## Stage 6: Hepatic Immune Evasion (Leukotoxin Kills Kupffer Cells / Neutrophils)

### Candidate 11: Anti-Leukotoxin Monoclonal Antibody (Passive Immunization)

| Field | Detail |
|---|---|
| **Target/mechanism** | Bovine-engineered anti-leukotoxin monoclonal antibody administered at feedlot arrival and boosted at 60 days. Provides immediate, high-concentration neutralizing antibody that cannot be overwhelmed the way vaccine-induced titers are. Bypasses the core Fusogard failure: insufficient antibody production by the animal's own immune system under chronic challenge. |
| **Disease stage(s)** | Stage 6 (leukotoxin neutralization) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — leukotoxin neutralization is a VALIDATED target: (a) Fusogard works on forage (OR=0.27), (b) KSU leukotoxoid vaccine protects 80% in challenge model, (c) anti-leukotoxin titer correlates with protection (P<0.05, Saginala et al. 1997). Monoclonal antibodies against leukotoxin exist for ELISA quantification — never tested for passive protection. Elanco's mAb platform could manufacture this. |
| **Species data** | Cattle — polyclonal anti-leukotoxin antibodies are protective in challenge models. No monoclonal antibody passive immunization tested. |
| **Key risk** | (1) Cost: mAb must be <$15-20/dose to be economically viable at feedlot scale. Current veterinary mAb (canine parvo) is ~$350-500/dose — needs massive cost reduction for food animal economics. (2) Duration: bovine IgG half-life is ~20 days — would need 3-4 doses over 150 days. (3) Leukotoxin's unique structure (no homology to any known toxin) means no existing mAb scaffold — must develop de novo. (4) If leukotoxin receptor is unknown, rational mAb design targeting the receptor-binding domain is impossible. |
| **Proposed de-risk** | Step 1: Generate anti-leukotoxin mAbs from hybridomas or phage display using PL4 fragment (the most immunoprotective leukotoxin fragment from KSU data). Step 2: In vitro bovine neutrophil protection assay — can mAb neutralize leukotoxin-induced apoptosis? Step 3: Bovine PK study. Cost: ~$150-250K for steps 1-3. This is expensive but directly leverages Elanco's mAb infrastructure. |

### Candidate 12: Recombinant Leukotoxin Subunit Vaccine with Slow-Release Adjuvant

| Field | Detail |
|---|---|
| **Target/mechanism** | Purified recombinant leukotoxin fragment PL4 (the most immunoprotective domain from KSU truncation studies) formulated with modern slow-release adjuvant (ISCO-MATRIX, Montanide ISA 201, or aluminum hydroxide + CpG ODN) designed to sustain high neutralizing antibody titers for 150+ days. Addresses Fusogard's TWO key failures: (a) crude antigen dilution → purified recombinant eliminates irrelevant antigens, (b) insufficient titer duration → slow-release adjuvant sustains protective titers across the entire feeding period. |
| **Disease stage(s)** | Stage 6 (anti-leukotoxin) |
| **Category** | **B — Known approach (next-generation)** |
| **Evidence tier** | [MODERATE] — PL4 fragment generates neutralizing antibodies in mice and cattle (Saginala et al. 1997; Amachawadi et al. 2021). US Patent 7449310B2 covers recombinant F. necrophorum leukotoxin vaccine preparation. Slow-release adjuvant technology is established for veterinary vaccines. |
| **Species data** | Cattle — KSU leukotoxoid vaccine: 80% protection in challenge model (Saginala et al. 1997). Mouse — multi-component vaccine including PL4 showed best immunoprotection (Amachawadi et al. 2021). No grain-diet feedlot field trial of purified recombinant vaccine. |
| **Key risk** | (1) Dose overwhelm: even high-titer anti-leukotoxin antibodies may be consumed faster than they can neutralize under chronic high-volume translocation. (2) Leukotoxin is 336 kDa — PL4 is a fragment; may miss critical neutralizing epitopes. (3) The KSU challenge model used single bolus inoculation — does not replicate chronic translocation. (4) Need to achieve 5-10x higher titers than Fusogard for 5+ months. |
| **Proposed de-risk** | Step 1: Adjuvant comparison study in 40 steers (4 adjuvants x 10 animals) with rPL4 antigen. Measure neutralizing Ab titers at 0, 30, 60, 90, 120, 150 days. Goal: identify adjuvant that maintains protective titers at day 150. Cost: ~$50-70K. Step 2: If titer sustained, feedlot field trial on grain diet (n=500). Cost: ~$120K. |

### Candidate 13: Leukotoxin Receptor Identification + Receptor-Blocking Small Molecule

| Field | Detail |
|---|---|
| **Target/mechanism** | The leukotoxin receptor on bovine leukocytes is UNKNOWN — this is identified as the single most important knowledge gap in F. necrophorum biology (Phase 1, Section 3.6). If identified, a receptor-blocking compound could prevent leukotoxin binding to PMNs/Kupffer cells, rendering the toxin harmless regardless of concentration. This would solve the dose-overwhelm problem that kills all vaccine approaches — you only need to block the receptor, not neutralize every toxin molecule. |
| **Disease stage(s)** | Stage 6 (block leukotoxin action at the host cell level) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — receptor-blocking approaches are validated for other toxins (e.g., anti-TNF receptor antibodies, botulinum toxin receptor blockers). Leukotoxin is species-specific (bovine/ovine PMNs susceptible, swine/rabbit PMNs not) — suggesting a specific receptor that could be targetable. 14 hydrophobic membrane-spanning regions suggest interaction with a specific membrane protein. |
| **Species data** | None — the receptor has never been identified. |
| **Key risk** | (1) Receptor identification may take 2-5 years and $500K+. (2) The receptor may be a ubiquitous membrane component (lipid raft, ganglioside) rather than a specific protein — making blocking impractical. (3) Even if identified, developing a small molecule blocker is a multi-year program. |
| **Proposed de-risk** | Step 1: Crosslink leukotoxin to bovine PMN surface proteins using photo-reactive crosslinker, pull down and identify by mass spectrometry. Cost: ~$30-50K. Step 2: CRISPR screen in bovine PMN cell line — knock out candidate receptors and test for leukotoxin resistance. Cost: ~$50-80K. This is a KE#1-level experiment: if the receptor is identified, it restructures the entire anti-leukotoxin strategy. |

---

## Stage 7: Anaerobic Niche Creation in Liver

### Candidate 14: Gallium (III) Compounds as Iron Metabolism Disruptors

| Field | Detail |
|---|---|
| **Target/mechanism** | Gallium(III) is a ferric iron mimetic that bacteria take up via iron acquisition systems but cannot reduce (redox-inactive). Disrupts iron-dependent metabolic enzymes essential for anaerobic growth. F. necrophorum is an obligate anaerobe that requires iron/heme for growth — its hemolysins and heme-acquisition systems are critical for establishing the hepatic niche. Gallium incorporation into iron-dependent enzymes would impair metabolic fitness and biofilm formation. |
| **Disease stage(s)** | Stage 7 (disrupt anaerobic niche establishment) + Stage 8 (anti-biofilm via iron deprivation) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [PRELIMINARY] — gallium nitrate disrupts iron metabolism and has antimicrobial + antibiofilm activity in Pseudomonas aeruginosa (Kaneko et al. 2007, J Clin Invest). FDA-approved drug for hypercalcemia (Ganite). Active against multiple gram-negative pathogens including A. baumannii. NO data in Fusobacterium species. |
| **Species data** | Mouse/human — gallium nitrate tested in Pseudomonas lung infection model. In vitro activity against multiple gram-negative biofilm-formers. No bovine data. No Fusobacterium data. |
| **Key risk** | (1) Unknown activity against F. necrophorum specifically. (2) Oral bioavailability and hepatic distribution in cattle unknown. (3) Food animal residue concerns — gallium is a heavy metal. (4) May impair host iron metabolism at therapeutic doses. (5) Regulatory pathway for a heavy metal in food animals is extremely challenging. |
| **Proposed de-risk** | In vitro: test gallium nitrate MIC against F. necrophorum, T. pyogenes, and B. pyogenes under anaerobic conditions. Also test effect on biofilm formation in the F. necrophorum + P. levii dual-species model. Cost: ~$5-10K. This is the cheapest possible de-risk — if no in vitro activity, kill immediately. |

### Candidate 15: Antiplatelet Agent (Clopidogrel Analog) to Prevent Microthrombus-Mediated Ischemia

| Field | Detail |
|---|---|
| **Target/mechanism** | F. necrophorum hemagglutinin causes platelet aggregation (13/16 virulent A-type strains positive). Combined with LPS-induced coagulation cascade activation, this creates fibrin microthrombi that produce the localized ischemia necessary for anaerobic niche formation. Antiplatelet agents (clopidogrel, aspirin) could prevent this. Aspirin is already used in some cattle fever management protocols. |
| **Disease stage(s)** | Stage 7 (prevent microthrombus formation → prevent ischemic niche) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [INFERRED] — hemagglutinin-mediated platelet aggregation is established (F. necrophorum). Antiplatelet therapy for infectious thrombosis is an active research area in human medicine (septic portal vein thrombosis). Aspirin has been used in cattle for anti-inflammatory purposes. No LA-specific antiplatelet data. |
| **Species data** | Cattle — aspirin used for fever/inflammation. No LA prevention data. |
| **Key risk** | (1) Anticoagulant/antiplatelet use in feedlot cattle raises bleeding risk. (2) Continuous dosing needed for 150+ days. (3) Regulatory pathway for aspirin/clopidogrel as feed additive unclear. (4) May interfere with normal wound healing. (5) Hemagglutinin is only one of multiple mechanisms creating anaerobic niche (LPS, hemolysin also contribute). |
| **Proposed de-risk** | Proof of concept in mouse liver abscess model: F. necrophorum challenge +/- low-dose aspirin. Measure abscess size, severity, and microthrombus formation histologically. Cost: ~$15-20K. |

---

## Stage 8: Polymicrobial Synergy (F. necrophorum + T. pyogenes + Bacteroides)

### Candidate 16: Anti-Pyolysin Strategy (T. pyogenes Virulence Disruption)

| Field | Detail |
|---|---|
| **Target/mechanism** | T. pyogenes pyolysin (PLO) is a cholesterol-dependent cytolysin (CDC) that lyses hepatocytes, expanding the abscess niche. It also provides metabolic cross-feeding (lactic acid for F. necrophorum) and O2 scavenging. CDCs are inhibited by cholesterol-sequestering agents (e.g., cholesterol-loaded liposomes, beta-cyclodextrin, statins). Anti-PLO antibody could neutralize the cytolysin. Combination anti-Fn + anti-Tp vaccine (leukotoxin + pyolysin) addresses both synergistic partners. |
| **Disease stage(s)** | Stage 8 (disrupt polymicrobial synergy) + Stage 9 (reduce tissue destruction) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [MODERATE] — pyolysin is a validated virulence factor in bovine disease (mastitis, metritis). CDC inhibition by cholesterol analogs is established. A vaccine containing E. coli + F. necrophorum + T. pyogenes antigens reduced puerperal metritis in dairy cows (Machado et al. 2014, PLoS One; vaccine: 9.1% vs 14.9% incidence). Anti-PLO antibodies neutralize cytolysin in vitro. |
| **Species data** | Cattle — T. pyogenes metritis vaccine with LA-relevant antigens tested in dairy heifers (Machado et al. 2014). Reduced metritis by ~39%. Contains F. necrophorum leukotoxin + T. pyogenes pyolysin components. |
| **Key risk** | (1) T. pyogenes is present in only ~29% of abscesses — anti-PLO may have limited impact alone. (2) F. necrophorum alone can cause abscesses without T. pyogenes. (3) Cholesterol-targeting agents may have off-target effects on host cell membranes. |
| **Proposed de-risk** | Include pyolysin toxoid as additional antigen in the multi-antigen subunit vaccine (Candidate 4). Incremental cost to add one more recombinant antigen: ~$15-20K. |

### Candidate 17: Quorum Quenching — LuxS/AI-2 Inhibition

| Field | Detail |
|---|---|
| **Target/mechanism** | F. necrophorum likely uses the LuxS/AI-2 quorum sensing system (universal interspecies signaling system present in most gram-negative anaerobes) to coordinate virulence factor expression and the commensal-to-pathogen transition during rumen wall colonization. AI-2 inhibitors (e.g., D-ribose analogs, synthetic DPD analogs) could prevent the virulence switch that occurs when F. necrophorum population density reaches threshold levels at the rumen wall. In F. nucleatum (96% FomA homology), AI-2 regulates biofilm formation with oral streptococci. In Haemophilus parasuis, luxS deletion attenuated virulence 10-fold. |
| **Disease stage(s)** | Stage 3 (prevent virulence switch during wall colonization) + Stage 8 (disrupt polymicrobial coordination) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — LuxS/AI-2 is present in most Fusobacterium species (F. nucleatum confirmed). AI-2 quorum quenching reduces virulence in multiple gram-negative pathogens. F. necrophorum genome contains luxS (confirmed by comparative genomics, Kook et al. 2022). No direct functional studies of F. necrophorum QS system. |
| **Species data** | None for F. necrophorum. In vitro in multiple other anaerobes. Mouse models for LuxS mutants of related pathogens. |
| **Key risk** | (1) F. necrophorum's LuxS may have metabolic function (activated methyl cycle) rather than true quorum sensing — BMC Microbiol study suggests many bacteria use LuxS for metabolism, not QS. (2) AI-2 is a universal signal — inhibiting it may disrupt beneficial rumen microbial communities. (3) Delivering QQ agents to the rumen wall niche at effective concentrations. (4) Even if QS is disrupted, constitutive virulence expression may still produce enough leukotoxin. |
| **Proposed de-risk** | Step 1: Construct F. necrophorum luxS deletion mutant. Test: (a) leukotoxin production, (b) biofilm formation, (c) adhesion to bovine cells, (d) virulence in mouse model. Cost: ~$40-60K (requires anaerobic genetic manipulation capability). If luxS deletion reduces virulence >5-fold, proceed to AI-2 analog screening. |

---

## Stage 9: Abscess Formation / Acute Pathology

### Candidate 18: Immunomodulatory Macrolide Analog (Non-Antibiotic Tylosin Mimic)

| Field | Detail |
|---|---|
| **Target/mechanism** | Tylosin's immunomodulatory effect (NF-kB suppression in hepatic immune cells) may contribute to its superiority over CTC. Design a non-antibiotic macrolide derivative that retains the immunomodulatory properties (NF-kB suppression, reduced inflammatory cytokine cascade) WITHOUT antimicrobial activity. This would break the recruit-kill-recruit cycle (Stage 4.2 in disease map) where leukotoxin-killed immune cells release cytokines that recruit more immune cells to be killed. Analogous to low-dose azithromycin in cystic fibrosis (anti-inflammatory, not antimicrobial). |
| **Disease stage(s)** | Stage 9 (break self-reinforcing immune destruction cycle) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [PRELIMINARY] — macrolide immunomodulation is established for 14/15-membered rings (azithromycin in CF, diffuse panbronchiolitis). Tylosin is 16-membered — immunomodulatory effect may be weaker. Non-antibiotic macrolide derivatives (e.g., EM703, solithromycin analogs) exist in the human pharmaceutical pipeline. No bovine LA application. |
| **Species data** | Human — azithromycin immunomodulation in CF and COPD. No cattle immunomodulatory macrolide studies. |
| **Key risk** | (1) Tylosin's immunomodulatory contribution is unproven for LA — may be minor. (2) 16-membered macrolides have weaker anti-inflammatory effects than 14/15-membered. (3) Non-antibiotic macrolide derivatives would need full regulatory approval — long timeline. (4) Immunosuppression at the liver could theoretically worsen infection clearance. |
| **Proposed de-risk** | In vitro: treat bovine Kupffer cells and PMNs with tylosin and measure NF-kB activity, cytokine production (TNF-alpha, IL-1beta, IL-6), and phagocytic capacity. If tylosin significantly reduces inflammatory signaling, test azithromycin and EM703 at sub-MIC doses. Cost: ~$20-30K. This resolves the 50-year question of whether tylosin's immunomodulatory effect matters for LA. |

### Candidate 19: TGF-beta1 Modulators (Delay Capsule Formation)

| Field | Detail |
|---|---|
| **Target/mechanism** | Hepatic stellate cells drive fibrosis via TGF-beta1 signaling, creating the collagen capsule that makes established abscesses untreatable. TGF-beta1 upregulation documented in fibrotic zones around chronic bovine liver abscesses (Lechtenberg et al. 1988). If capsule formation could be DELAYED during the early abscess window (days 3-10 post-establishment), innate immunity and/or antibiotics might clear the nascent infection before encapsulation renders it pharmacokinetically inaccessible. TGF-beta1 pathway inhibitors (pirfenidone, nintedanib, galunisertib) exist in human medicine for pulmonary and hepatic fibrosis. |
| **Disease stage(s)** | Stage 9 (delay encapsulation → extend therapeutic window) + Stage 10 (prevent chronic persistence) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — TGF-beta1 drives hepatic fibrosis in all species studied. Pirfenidone reduces hepatic fibrosis in rodent models. TGF-beta1 upregulation in bovine LA capsule reported. No anti-fibrotic approach attempted for bovine LA. |
| **Species data** | Mouse/rat — pirfenidone and galunisertib in hepatic fibrosis models. TGF-beta1 expression documented in bovine LA. |
| **Key risk** | (1) Delaying encapsulation could allow abscess EXPANSION rather than clearance — the capsule also CONTAINS the infection. Without a concurrent antibacterial agent, delayed encapsulation could worsen outcomes. (2) TGF-beta1 is pleiotropic — systemic inhibition causes immunosuppression and impaired wound healing. (3) Must be combined with an anti-F. necrophorum agent. (4) Timing is critical — must act within the 3-10 day window before capsule matures. |
| **Proposed de-risk** | Mouse LA model (Fusobacterium IV challenge model — Kayo et al. 2013): challenge mice, treat half with pirfenidone starting day 1, measure abscess size, bacterial load, capsule thickness at day 7 and 14. One group: pirfenidone alone. One group: pirfenidone + metronidazole. Cost: ~$20-30K. CRITICAL: pirfenidone alone may worsen disease. Must test combination. |

---

## Stage 10: Chronic Persistence (Fibrous Capsule)

### Candidate 20: Accept Prevention-Only Strategy (No Treatment Candidates)

| Field | Detail |
|---|---|
| **Target/mechanism** | N/A — this stage is pharmacokinetically untreatable. The fibrous capsule (>1 cm collagen) creates an avascular, anaerobic, low-pH, protein-rich environment. No systemic drug can achieve therapeutic concentrations. No novel approach changes this fundamental physical reality. |
| **Disease stage(s)** | Stage 10 |
| **Category** | N/A |
| **Evidence tier** | [ESTABLISHED] — 100% treatment failure rate for established abscesses across all antibiotics tested. |
| **Key risk** | N/A |
| **Proposed de-risk** | No de-risk — redirect all resources to prevention (Stages 1-9). The only way to address Stage 10 is to prevent Stage 9 from progressing to Stage 10. Candidate 19 (TGF-beta1 modulation) is the closest to a Stage 10 intervention — by delaying capsule formation, it extends the window in which Stages 6-9 interventions can work. |

**Overwatch note:** This is a deliberate "no candidate" entry. The failure analysis proves treatment is impossible. Spending resources here is waste. The 70% test will evaluate coverage against TRACTABLE stages only.

---

## Stage 11: Biofilm Immune Evasion (PPIX-Mediated Neutrophil Suppression)

### Candidate 21: Photodynamic Therapy (PDT) of PPIX-Producing Biofilms

| Field | Detail |
|---|---|
| **Target/mechanism** | Protoporphyrin IX (PPIX) is a photosensitizer — it generates cytotoxic reactive oxygen species when exposed to light at specific wavelengths (~410 nm, ~635 nm). The same PPIX that F. necrophorum + P. levii biofilms produce to suppress neutrophils can be turned against them via photodynamic therapy. Light activation converts PPIX from an immune suppressant into a bacterial killer. PDT is established for treating oral Fusobacterium nucleatum biofilms in periodontal disease. |
| **Disease stage(s)** | Stage 11 (destroy biofilm via its own PPIX) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [PRELIMINARY] — PDT against F. nucleatum biofilms in periodontal disease is well-established. PPIX production by F. necrophorum + P. levii dual-species biofilms confirmed (Lockhart et al. 2022). PDT concept in hepatic abscesses never attempted. |
| **Species data** | Human (periodontal) — PDT against Fusobacterium biofilms. No bovine data. |
| **Key risk** | (1) Light delivery to hepatic abscesses is impractical in cattle — this is a fundamental feasibility barrier. No fiber optic liver illumination in feedlot settings. (2) Abscesses are deep in the liver parenchyma. (3) This is conceptually interesting but practically unworkable for feedlot use. |
| **Proposed de-risk** | Kill this candidate before spending money — the light delivery problem is an engineering impossibility in feedlot cattle. However, the PPIX biology remains actionable: see Candidate 22. |

### Candidate 22: PPIX Biosynthesis Inhibitor (Anti-Biofilm via Heme Pathway Disruption)

| Field | Detail |
|---|---|
| **Target/mechanism** | If PPIX is the key molecule suppressing neutrophil oxidative burst in biofilms, inhibiting PPIX biosynthesis would restore neutrophil killing capacity. The heme biosynthetic pathway (delta-aminolevulinic acid → porphobilinogen → ... → PPIX → heme) is essential for anaerobes. Inhibitors of delta-aminolevulinic acid dehydratase (ALAD), ferrochelatase, or porphobilinogen deaminase could reduce PPIX accumulation in biofilm extracellular fluid. Succinylacetone is a known ALAD inhibitor. However, heme pathway inhibition would also affect host cells — selectivity is the challenge. |
| **Disease stage(s)** | Stage 11 (block PPIX-mediated immune evasion) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — PPIX suppresses bovine neutrophil ROS at 25-50 uM (Lockhart et al. 2022). Heme biosynthesis pathway is conserved across bacteria and eukaryotes. No PPIX biosynthesis inhibitor tested against F. necrophorum biofilms. |
| **Species data** | None. |
| **Key risk** | (1) Host heme pathway is the same — systemic inhibition would cause porphyria-like toxicity. (2) PPIX is produced by Porphyromonas levii, not F. necrophorum itself — need to target the right organism. (3) Biofilm-specific delivery is impossible. |
| **Proposed de-risk** | In vitro screen: test succinylacetone (ALAD inhibitor) and 5 other heme pathway inhibitors against F. necrophorum + P. levii dual biofilm. Measure PPIX in supernatant and test whether treated-biofilm supernatant restores bovine neutrophil ROS response. Cost: ~$10-15K. |

### Candidate 23: Anti-Biofilm Disruption via Dispersin B or DNase I

| Field | Detail |
|---|---|
| **Target/mechanism** | Enzymatic biofilm dispersal: (a) Dispersin B (DspB) — glycosyl hydrolase that cleaves poly-N-acetylglucosamine (PNAG), a common biofilm matrix component. (b) DNase I — degrades extracellular DNA (eDNA) that forms the structural backbone of many polymicrobial biofilms. Both convert biofilm bacteria to planktonic form, restoring antibiotic susceptibility and immune accessibility. Used in combination with antimicrobials in human medicine for chronic biofilm infections (P. aeruginosa, MRSA). |
| **Disease stage(s)** | Stage 11 (biofilm disruption) + Stage 8 (disrupt polymicrobial matrix) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [PRELIMINARY] — DspB and DNase I disrupt biofilms of multiple gram-negative pathogens. F. necrophorum biofilm matrix composition not fully characterized (PNAG vs eDNA vs protein — unknown). No Fusobacterium-specific biofilm dispersal data. |
| **Species data** | In vitro — multiple bacterial species. No bovine or Fusobacterium data. |
| **Key risk** | (1) Biofilm formation in bovine liver abscesses is INFERRED, not directly demonstrated. (2) Unknown whether F. necrophorum biofilm uses PNAG or eDNA as structural matrix. (3) Enzyme stability and delivery to hepatic abscess site is problematic. (4) Biofilm disruption without concurrent killing may cause bacterial dissemination. |
| **Proposed de-risk** | Step 1: Characterize F. necrophorum + P. levii dual-species biofilm matrix composition (PNAG, eDNA, protein). Cost: ~$10K. Step 2: If PNAG or eDNA dominant, test DspB or DNase I for dispersal efficacy + concurrent metronidazole. Cost: ~$10K. |

---

## Cross-Stage Combination Candidates

### Candidate 24: Metronidazole Analog (Narrow-Spectrum Anti-Anaerobe, Rumen-Stable)

| Field | Detail |
|---|---|
| **Target/mechanism** | Metronidazole is the gold standard anti-anaerobe drug: potent against F. necrophorum (MIC 0.25-2 ug/mL), selective for anaerobes (spares aerobes/facultative anaerobes), and proven to eradicate F. necrophorum from liver in mouse model (Kayo et al. 2013, 5 mg/kg for 3 days cleared infection). A rumen-stable metronidazole analog (or nitroimidazole derivative) designed for oral delivery to cattle could provide tylosin-like selective anti-Fn activity without the macrolide resistance concern. |
| **Disease stage(s)** | Stage 3 (reduce Fn at rumen wall) + Stage 6 (reduce bacterial load reaching liver) |
| **Category** | **B — Known approach (repositioned)** |
| **Evidence tier** | [ESTABLISHED for activity, NOT for cattle use] — metronidazole eradicates F. necrophorum in mouse LA model (Kayo et al. 2013, J Med Microbiol). Potent anti-anaerobe activity established across species. NOT approved for food animals in US/EU (carcinogenicity concerns — classified as possible human carcinogen, IARC Group 2B). |
| **Species data** | Mouse — metronidazole at 5 mg/kg eradicated F. necrophorum from liver (Kayo et al. 2013). Used extensively in human Fusobacterium infections (Lemierre's syndrome). NOT approved for food-producing animals. |
| **Key risk** | (1) REGULATORY BLOCKER: Metronidazole is banned in food animals in the US and EU due to residue carcinogenicity concerns. (2) A novel nitroimidazole derivative would need to clear FDA/FSIS residue and safety reviews — 5-10 year regulatory path. (3) Even if safe, public perception of "antibiotic replacement" may face resistance. (4) Rumen stability unknown — nitroimidazoles may be reduced by rumen microbes. |
| **Proposed de-risk** | In vitro: test rumen stability of 5 nitroimidazole analogs (ronidazole, dimetridazole, tinidazole, secnidazole, ornidazole) in bovine rumen fluid. Test MIC against F. necrophorum for rumen-stable candidates. Cost: ~$10-15K. If a non-carcinogenic, rumen-stable analog is identified, proceed to regulatory pre-consultation. |

### Candidate 25: Bacteriocin-Producing Probiotic (Narrow-Spectrum Anti-Fn at Rumen Wall)

| Field | Detail |
|---|---|
| **Target/mechanism** | Engineer or select a probiotic strain that: (a) colonizes the rumen epimural community (wall-adherent), and (b) produces bacteriocins specifically active against F. necrophorum. Bacteriocins are ribosomally synthesized antimicrobial peptides — narrow-spectrum by nature. This combines the epimural colonization concept (Candidate 6) with targeted anti-Fn activity. Closest analog: nisin-producing Lactococcus lactis for mastitis prevention. |
| **Disease stage(s)** | Stage 3 (reduce Fn colonization) + Stage 2 (barrier protection via epimural community) |
| **Category** | **D — Novel proposal** |
| **Evidence tier** | [INFERRED] — bacteriocins active against gram-negative anaerobes exist (e.g., colicins, microcins). No anti-Fusobacterium bacteriocin characterized. Nisin-producing probiotics tested for bovine mastitis. No rumen wall-colonizing bacteriocin producer designed. |
| **Species data** | Cattle — nisin-producing L. lactis for mastitis. No rumen application. |
| **Key risk** | (1) Identifying bacteriocin active against F. necrophorum is itself a discovery program. (2) Rumen wall colonization by a probiotic never demonstrated. (3) Bacteriocin production in anaerobic rumen wall environment may differ from laboratory conditions. (4) Timeline: 5+ years to develop. |
| **Proposed de-risk** | Step 1: Screen culture supernatants of 50 rumen epimural isolates for anti-F. necrophorum activity in zone-of-inhibition assays. Cost: ~$15K. Step 2: If hits found, characterize the bacteriocin and the producing strain's wall-adhesion capacity. |

### Candidate 26: Combination Strategy — MON + BX + rPL4 Vaccine (Triple Stack)

| Field | Detail |
|---|---|
| **Target/mechanism** | Combine the three highest-evidence interventions: (a) Monensin (intake stabilization, Stage 1), (b) Tannin blend BX (Stage 1-3, anti-Fn activity), (c) Recombinant PL4 leukotoxin vaccine with slow-release adjuvant (Stage 6). Rationale: MON+BX reduces the translocation burden (making the bacterial challenge more manageable), while rPL4 vaccine neutralizes leukotoxin when bacteria do reach the liver. Together, they replicate tylosin's multi-dimensional mechanism: burden reduction + immune support. |
| **Disease stage(s)** | Stages 1 + 3 + 6 (multi-stage stack) |
| **Category** | **B — Known approach (combination)** |
| **Evidence tier** | [MODERATE for components individually; INFERRED for combination] — MON+BX tested at commercial scale (Felizari et al. 2025). rPL4 vaccine shows protection in challenge models (Saginala et al. 1997). No trial of MON+BX+vaccine. |
| **Species data** | Cattle — MON+BX (n=2,986). Cattle — KSU leukotoxoid (challenge model). Combination: no data. |
| **Key risk** | (1) Three products means three costs — must be economically viable (monensin: $0.02/d, BX: ~$0.10/d, vaccine: ~$3-5/head = total ~$25-35/head over 150 days vs tylosin ~$3/head total). Significantly more expensive. (2) Vaccine may still be overwhelmed even with reduced burden. (3) Three regulatory approvals/labels to coordinate. |
| **Proposed de-risk** | The individual components are already de-risked. The combination trial is the critical next step: 4-arm feedlot trial (n=200/arm): (a) MON+TYL (control), (b) MON+BX, (c) MON+BX+vaccine, (d) MON+vaccine. Cost: ~$150-200K. This is the definitive test of whether burden reduction + immune support can match tylosin. |

### Candidate 27: FP-100-Type Targeted Antimicrobial (Fusobacterium-Specific Small Molecule)

| Field | Detail |
|---|---|
| **Target/mechanism** | FP-100 is a targeted antimicrobial that specifically eliminates Fusobacterium species from the oral microbiota without altering overall microbial diversity (2 uM concentration). Originally developed for F. nucleatum in periodontal disease, it significantly reduced Fusobacterium spp. and alveolar bone loss in a mouse periodontitis model. A Fusobacterium-selective antimicrobial would address the core lesson from the failure analysis: selectivity matters more than breadth (tylosin > CTC despite narrower spectrum). |
| **Disease stage(s)** | Stage 3 (selective Fn elimination at rumen wall) |
| **Category** | **C — Non-obvious / cross-disease analogy** |
| **Evidence tier** | [PRELIMINARY] — FP-100 tested in mouse periodontitis model with F. nucleatum (He et al. 2024, J Dent Res). Reduced Fusobacterium without affecting diversity. No data in F. necrophorum or cattle. FP-100 is a research tool compound, not a drug. |
| **Species data** | Mouse (oral) — FP-100 reduced Fusobacterium spp. in oral microbiota. No bovine data. |
| **Key risk** | (1) F. necrophorum and F. nucleatum are related but distinct species — FP-100 selectivity may not cross over. (2) Rumen environment completely different from oral cavity (pH, anaerobiosis, volume). (3) Compound is research-stage — no PK, safety, or formulation data for cattle. (4) Specificity mechanism unclear — may not work against wall-colonizing bacteria. |
| **Proposed de-risk** | In vitro: test FP-100 MIC against F. necrophorum subsp. necrophorum (biotype A) vs F. varium vs T. pyogenes vs 5 beneficial rumen species. Cost: ~$5K. If selective for Fn over commensal species, proceed to rumen fluid stability testing. |

---

## Coverage Map Summary

| Disease Stage | Candidates | Categories |
|---|---|---|
| 1. Ruminal acidosis | #1 (MON+BX) | A |
| 2. Rumen epithelial damage | #2 (rumen-protected butyrate), #3 (zinc+butyrate stack) | B, B |
| 3. Rumen wall colonization | #4 (multi-antigen vaccine), #5 (anti-FomA mAb), #6 (epimural probiotic), #25 (bacteriocin probiotic), #27 (FP-100 type) | B, D, D, D, C |
| 4. Portal translocation (rumen) | #7 (mucoadhesive sealant), #8 (oral IgA vaccine) | C, D |
| 5. Portal translocation (hindgut) | #9 (hindgut prebiotic), #10 (hindgut butyrate+zinc) | B, D |
| 6. Hepatic immune evasion | #11 (anti-LktA mAb), #12 (rPL4 vaccine), #13 (receptor ID) | D, B, D |
| 7. Anaerobic niche creation | #14 (gallium), #15 (antiplatelet) | C, C |
| 8. Polymicrobial synergy | #16 (anti-pyolysin), #17 (quorum quench) | C, D |
| 9. Abscess formation | #18 (immunomodulatory macrolide), #19 (TGF-beta1 delay) | C, D |
| 10. Chronic persistence | #20 (no candidate — prevention only) | N/A |
| 11. Biofilm immune evasion | #21 (PDT — kill), #22 (PPIX inhibitor), #23 (biofilm dispersal) | C, D, C |
| **Cross-stage** | #24 (metronidazole analog), #26 (triple stack), #27 (FP-100) | B, B, C |

**Total candidates: 27 (across 11 stages)**
- Category A (empirical in-vivo): 1
- Category B (known approach): 8
- Category C (non-obvious): 8
- Category D (novel): 10

---

## Priority Ranking for De-Risk Investment

### Tier 1 — Highest confidence, shortest path to data (invest immediately)

| # | Candidate | De-risk cost | Timeline | Rationale |
|---|---|---|---|---|
| 1 | MON+BX (#1) | $50-80K (dose optimization) | 6 months | Only non-antibiotic with commercial cattle data approaching tylosin. Already partially de-risked. |
| 12 | rPL4 vaccine (#12) | $50-70K (adjuvant comparison) | 6-9 months | Validated target, US patent exists, Elanco has vaccine infrastructure. |
| 4 | Multi-antigen vaccine (#4) | $40-60K (bovine serology) | 6-9 months | Addresses Fusogard's key failure with modern antigen design. |
| 26 | Triple stack (#26) | $150-200K (field trial) | 12 months | Tests the hypothesis that burden reduction + immune support matches tylosin. |

### Tier 2 — Strong rationale, needs key data before commitment

| # | Candidate | De-risk cost | Timeline | Rationale |
|---|---|---|---|---|
| 2 | Rumen-protected butyrate (#2) | $15-20K (Ussing chamber) | 3 months | If barrier integrity can be pharmaceutically enhanced, this is a game-changer. |
| 5 | Anti-FomA mAb (#5) | $100-200K | 12-18 months | Leverages Elanco's mAb platform. Dual mechanism if Factor H binding is confirmed. |
| 11 | Anti-LktA mAb (#11) | $150-250K | 12-18 months | Most direct path to dose-overwhelm-proof leukotoxin neutralization. |
| 9 | Hindgut prebiotic (#9) | $10K (abscess typing) | 3 months | KE#1 must be answered first — if hindgut abscesses are residual LA under tylosin, this becomes Tier 1. |

### Tier 3 — Speculative but high upside if validated

| # | Candidate | De-risk cost | Timeline | Rationale |
|---|---|---|---|---|
| 13 | Leukotoxin receptor ID (#13) | $80-130K | 12-24 months | Paradigm-shifting if receptor found. |
| 17 | Quorum quenching (#17) | $40-60K | 12 months | Novel mechanism, but LuxS function in Fn unknown. |
| 24 | Metronidazole analog (#24) | $10-15K (screen) | 3 months | Cheap screen, but regulatory pathway is a decade-long barrier. |
| 14 | Gallium (#14) | $5-10K | 1 month | Cheapest de-risk in the portfolio — in vitro MIC test. |
| 27 | FP-100 type (#27) | $5K | 1 month | Cheap cross-reactivity screen. |

### Kill List (Do Not Pursue)

| # | Candidate | Reason |
|---|---|---|
| 21 | PDT of PPIX biofilms | Light delivery to bovine liver is an engineering impossibility. |
| 15 | Antiplatelet agent | Bleeding risk in feedlot cattle is unacceptable for a prevention product. Hemagglutinin is only one niche-creation mechanism. |

---

## Key Dependencies and Open Questions

1. **KE#1 (from Pathfinder):** What fraction of residual LA under tylosin is hindgut-origin? This determines whether hindgut candidates (#9, #10) are Tier 1 or Tier 3. Must be answered by abscess typing in any upcoming trial.

2. **Leukotoxin receptor identity:** If the receptor is identified (Candidate #13), the entire anti-leukotoxin strategy shifts from antibody neutralization to receptor blocking — potentially solving the dose-overwhelm problem permanently.

3. **Elanco's mAb platform readiness for livestock:** Current platform is companion animal focused. Extension to food animals requires cost reduction (from ~$350/dose to <$15/dose) and regulatory pathway for meat/milk residue clearance. Timeline: unknown.

4. **Adjuvant technology:** The success of vaccine candidates (#4, #12) hinges on sustaining protective titers for 150+ days from 2-3 doses. This is an adjuvant engineering problem, not an antigen problem.

5. **MON+BX gap closure:** The 10-point gap between MON+BX (28.5%) and MON+TYL (18.3%) must be closed. Whether this comes from higher BX dose, better formulation, or addition of a third component (vaccine) determines the portfolio's backbone.

---

## References

- Amachawadi et al. (2021). Multi-component recombinant subunit vaccine. Front Vet Sci 8:780377.
- Amachawadi et al. (2023). Novel OMP adhesion proteins. Microorganisms 11:2082.
- Amachawadi et al. (2024). Plant phenolic extracts vs liver abscess pathogens. Microorganisms.
- Felizari et al. (2025). Tannin blend as alternative to tylosin. Vet Sci 12:446.
- Fox et al. (2009). Fusogard efficacy. Can Vet J 46:1060-1067.
- Holm et al. (2008). Factor H binding in F. necrophorum. J Immunol 181:8624.
- Kanoe et al. (1984). Hemagglutinin-mediated adhesion. Jpn J Vet Sci.
- Kayo et al. (2013). Mouse liver abscess model with metronidazole. J Med Microbiol 62:1398-1404.
- Kook et al. (2022). Comparative genomics of F. necrophorum. Microorganisms 10:2486.
- Kumar et al. (2015). FomA identification and characterization. Vet Microbiol 176:340-349.
- Lockhart et al. (2022). PPIX from dual-species biofilms. Biofilm 4:100083.
- Machado et al. (2014). Recombinant vaccine prevents puerperal metritis. PLoS One 9:e91734.
- Malmuthuge et al. (2021). Bovine epimural microbiota. Microorganisms 9:342.
- Saginala et al. (1997). KSU leukotoxoid vaccine. J Anim Sci 75:1160-1166.
- Steele et al. (2009-2012). Rumen epithelial butyrate response. Multiple publications.
- Xiang et al. (2024). Microbial inoculum effects on rumen epimural. Sci Rep 14:14686.
- Zhang et al. (2001). Leukotoxin gene sequencing. Infect Immun 69:5738.
- US Patent 7449310B2. Recombinant F. necrophorum leukotoxin vaccine.
