# Phase 3 Candidate Proposals: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill (Animal Nutrition & Health)
**Pathogen:** *Cryptosporidium parvum* | **Host:** Neonatal dairy and beef calves (0-30 days)
**Agent:** Forge | **Date:** 2026-03-27 | **Version:** 1.0

---

## Executive Summary

This document proposes **42 individual mechanism-level candidates** across **all 8 disease stages** for cryptosporidiosis in neonatal calves. Candidates are organized into four categories:

- **Category A (In Vivo Validated):** 7 compounds/approaches with positive calf or closely related in-vivo data
- **Category B (Known Approaches):** 15 literature-supported targets with mechanistic evidence
- **Category C (Non-Obvious Approaches):** 11 cross-disease analogies and repurposed mechanisms
- **Category D (Novel Proposals):** 9 first-principles designs for gap stages

Every candidate is evaluated against Sapper's 14 constraints. Every disease stage has at least one candidate. Candidates are tagged with evidence tiers per Quality Standard 1 and flagged for Cargill fit where applicable.

**Critical framing:** R0 = 5-15. This is NOT a fragile epidemic. Treatment that reduces shedding has dual benefit (individual cure + transmission reduction), but prevention alone cannot break the cycle. The portfolio must include direct-kill antiparasitics as the backbone, with host-directed and adjunctive approaches as combination partners.

---

## Table of Contents

1. [Category A: What Has Actually Worked In Vivo](#category-a-what-has-actually-worked-in-vivo)
2. [Category B: Known Approaches](#category-b-known-approaches)
3. [Category C: Non-Obvious Approaches](#category-c-non-obvious-approaches)
4. [Category D: Novel Proposals](#category-d-novel-proposals)
5. [Coverage Map by Disease Stage](#coverage-map-by-disease-stage)
6. [Cargill Fit Assessment](#cargill-fit-assessment)
7. [Constraint Compliance Summary](#constraint-compliance-summary)
8. [Priority Ranking for Surveyor](#priority-ranking-for-surveyor)

---

## Category A: What Has Actually Worked In Vivo

These are compounds/approaches with documented positive efficacy data in neonatal calves or closely related in-vivo models. This is the most important category because it represents empirical validation, not theoretical promise.

---

### A1. EDI048 — Gut-Restricted CpPI4K Inhibitor

| Field | Detail |
|---|---|
| **Target/mechanism** | *Cryptosporidium parvum* phosphatidylinositol 4-kinase (CpPI4K). ATP-competitive inhibitor. Blocks membrane trafficking required for parasitophorous vacuole maintenance, segmentation, and egress. Engineered as a "soft drug" with ester moiety for rapid hepatic metabolism to inactive carboxylic acid — gut-restricted activity. |
| **Disease stage** | Stage 3 (Intracellular Development) — primary. Also affects Stage 6 (Shedding) via oocyst reduction. |
| **Category** | A — In vivo validated |
| **Evidence tier** | [ESTABLISHED] — bovine in vivo, immunocompromised mouse, Phase 1 complete, Phase 2 recruiting (human CHIM, NCT07249463) |
| **Species data** | Neonatal calves: rapid diarrhea resolution by 48h, significant oocyst reduction, no recrudescence 7 days post-treatment, no adverse effects. Immunocompromised mice: ~3 log oocyst reduction at 10 mg/kg. 70-fold AUC safety margin. |
| **Key risk** | No veterinary development program exists. Novartis is developing for human paediatric use only. COGS at veterinary price points ($5-30/treatment) unproven. Incomplete parasitological cure — does not achieve sterilizing kill. May be inherently static (PI4K inhibition may arrest rather than kill). |
| **Proposed de-risk** | (1) Time-kill curve assay in bovine ALI organoids to determine whether PI4K inhibition is cidal or static. (2) Negotiate veterinary rights/license with Novartis. (3) If cidal: pursue veterinary formulation. If static: pursue combination with a cidal agent (e.g., CPSF3 inhibitor). |
| **Sapper constraint compliance** | Cidal: UNCERTAIN. Immunity-independent: YES (works in immunosuppressed mice). Luminal/apical: YES (gut-restricted by design). Multi-stage: PARTIAL (blocks segmentation/egress; unclear on sexual stages). Resistance barrier: MODERATE (ATP-competitive binding to conserved site). Neonatal safety: YES (70-fold safety margin). |
| **Cargill fit** | MODERATE — oral formulation possible, but novel kinase inhibitor synthesis may not match Cargill's manufacturing capabilities. Likely requires pharma partnership or license. |
| **20-Year Test** | N/A — first reported 2017 (KDU731), gut-restricted version (EDI048) 2024. Still in active human development. |

---

### A2. AN7973 — CPSF3 Inhibitor (Benzoxaborole)

| Field | Detail |
|---|---|
| **Target/mechanism** | Cleavage and Polyadenylation Specific Factor 3 (CPSF3), an essential endonuclease in mRNA processing. 6-carboxamide benzoxaborole. Rapidly cidal — traps enzyme in a dead-end complex. Broad-stage activity (asexual + sexual stages). |
| **Disease stage** | Stage 3 (Intracellular Development) — kills established parasites across multiple lifecycle stages. |
| **Category** | A — In vivo validated |
| **Evidence tier** | [MODERATE] — bovine in vivo (>99% oocyst reduction at 25 mg/kg, complete diarrhea elimination, no adverse effects); [ESTABLISHED] in immunocompromised mice |
| **Species data** | Neonatal calves: >99% reduction in total parasite fecal excretion. Complete diarrhea elimination. No adverse effects. Immunosuppressed mice: efficacious in both acute and established infection. |
| **Key risk** | Early development stage — AN7973 is a tool compound, not a clinical candidate. Benzoxaborole chemistry challenges (boron stability in GI tract). Resistance landscape not characterized. No veterinary development sponsor. |
| **Proposed de-risk** | (1) In vitro resistance selection experiment to characterize genetic barrier to resistance (critical — Compound 2093 precedent demands this before advancement). (2) GI stability testing of benzoxaborole in simulated abomasal and intestinal fluid. (3) If resistance barrier is high: pursue veterinary formulation optimization. |
| **Sapper constraint compliance** | Cidal: YES (demonstrated time-kill curves show complete elimination). Immunity-independent: YES (works in immunosuppressed mice). Multi-stage: YES (asexual + sexual). Resistance barrier: UNKNOWN (critical gap). Luminal/apical: PROBABLE (oral efficacy demonstrated, but gut-restriction not engineered). Neonatal safety: YES (no adverse effects in calf trial). |
| **Cargill fit** | LOW — novel boron-containing chemistry, requires pharma development capabilities. |
| **20-Year Test** | N/A — first reported 2019. Active development by global health organizations. |

**Strategic note:** AN7973's cidal + multi-stage profile is theoretically superior to EDI048's potentially static mechanism. If resistance barrier proves high, CPSF3 may be the better target than PI4K.

---

### A3. MMV665917 — Piperazine-Based Compound (Unknown Target)

| Field | Detail |
|---|---|
| **Target/mechanism** | Molecular target UNKNOWN. Piperazine-based compound from Medicines for Malaria Venture (MMV) open-access collection. Anti-cryptosporidial activity discovered through phenotypic screening. |
| **Disease stage** | Stage 3 (Intracellular Development) — kills intracellular parasites. |
| **Category** | A — In vivo validated |
| **Evidence tier** | [MODERATE] — bovine in vivo (94% oocyst reduction, prompt diarrhea resolution, safe and effective as THERAPEUTIC — started 2 days after severe diarrhea onset) |
| **Species data** | Neonatal calves (Stebbins et al. 2018, PLoS NTD): 22 mg/kg once daily for 7 days. Started therapeutically (2 days after severe diarrhea). 94% oocyst reduction. Prompt diarrhea resolution. Improved general health, appetite, dehydration. Safe. |
| **Key risk** | Unknown target = unknown resistance landscape, unknown mechanism of action. Single study. No follow-up publications since 2018. Development status unclear. |
| **Proposed de-risk** | (1) Target identification via CRISPR resistance selection or chemical proteomics. (2) Independent replication of calf efficacy. (3) If target is identified: assess resistance barrier and host homology. |
| **Sapper constraint compliance** | Cidal: PROBABLE (therapeutic efficacy with 94% oocyst reduction suggests killing, not stasis). Immunity-independent: UNKNOWN (calf data, not immunosuppressed model). Multi-stage: UNKNOWN. Resistance barrier: UNKNOWN. Neonatal safety: YES. |
| **Cargill fit** | UNKNOWN — depends on chemistry and manufacturing complexity once target is identified. |
| **20-Year Test** | N/A — first reported 2018. Absence of follow-up since 2018 is concerning — investigate whether development was abandoned. |

**Strategic note:** MMV665917 is notable because it demonstrated THERAPEUTIC efficacy (not just prophylactic) — one of very few compounds that worked when given after established infection. This is critical for field use where calves present with diarrhea.

---

### A4. BKI-1708 — 5-Aminopyrazole-4-Carboxamide CpCDPK1 Inhibitor

| Field | Detail |
|---|---|
| **Target/mechanism** | *C. parvum* calcium-dependent protein kinase 1 (CpCDPK1). Essential for invasion and egress (CRISPR-validated). BKI-1708 uses the 5-aminopyrazole-4-carboxamide (AC) scaffold with lower hERG liability than pyrazolopyrimidine-scaffold BKIs. |
| **Disease stage** | Stage 2 (Invasion) and Stage 3 (Intracellular Development — egress block). |
| **Category** | A — In vivo validated |
| **Evidence tier** | [MODERATE] — bovine in vivo (rapidly resolves diarrhea, improved clinical outcomes, lower hERG than PP-scaffold) |
| **Species data** | Neonatal calves: rapidly resolved diarrhea and improved clinical outcomes. Lower hERG liability than BKI-1294. |
| **Key risk** | CDPK1 is a stage-limited target (invasion/egress, not intracellular replication). Cannot achieve sterilizing cure as monotherapy. Long-term neonatal safety of AC scaffold not fully established. Host kinase cross-reactivity in neonates remains a concern (skeletal toxicity observed with other BKI scaffolds). |
| **Proposed de-risk** | (1) 14-day neonatal calf safety study with AC scaffold at 3x efficacious dose. (2) If safe: evaluate as combination partner with a cidal intracellular agent (e.g., AN7973 or EDI048). (3) Host kinase selectivity panel against developing calf kinome. |
| **Sapper constraint compliance** | Cidal: NO (blocks invasion/egress but does not kill established parasites). Immunity-independent: PARTIAL (blocks invasion regardless of immunity, but cannot eliminate intracellular burden). Multi-stage: NO (invasion/egress only). Resistance barrier: MODERATE. Neonatal safety: UNCERTAIN (AC scaffold better than PP, but not fully proven in neonates). |
| **Cargill fit** | LOW — novel kinase inhibitor chemistry, pharma development capabilities required. |

**Strategic note:** BKI-1708 is a COMBINATION PARTNER, not a standalone candidate. Its value is blocking reinvasion/autoinfection while a cidal agent kills intracellular parasites.

---

### A5. Hyperimmune Bovine Colostrum (rC7 Antigen)

| Field | Detail |
|---|---|
| **Target/mechanism** | Passive antibody transfer targeting sporozoite surface antigens. rC7-immunized dam colostrum achieved highest efficacy. Mechanism: IgG1/IgA in colostrum neutralize sporozoites during the brief extracellular transit between cells, reducing reinvasion events. |
| **Disease stage** | Stage 0 (Upstream Susceptibility) and Stage 2 (Invasion — blocks sporozoite attachment). |
| **Category** | A — In vivo validated |
| **Evidence tier** | [MODERATE] — bovine in vivo (rC7 antigen: 99.8% oocyst reduction, clinical diarrhea elimination; general hyperimmune colostrum: diarrhea 2.3 vs 5.0 days) |
| **Species data** | rC7-immunized colostrum: 99.8% reduction in oocyst excretion and elimination of clinical diarrhea. General hyperimmune colostrum: diarrhea 2.3 days vs 5.0 days in controls. Mouse model: purified IgG1, IgG2, IgA, IgM all showed significant reduction (P < 0.0001). |
| **Key risk** | Does NOT prevent infection — modulates severity. Cannot reach epicellular niche. Production scalability (requires immunizing individual pregnant cows). Waning at 16-28 days. Not a CURE — an adjunct. |
| **Proposed de-risk** | (1) Evaluate whether Cargill can produce a standardized hyperimmune colostrum product via large-scale dam immunization. (2) Test in combination with an antiparasitic (e.g., EDI048) to determine whether colostral antibodies + drug achieve sterilizing cure. |
| **Sapper constraint compliance** | Cidal: NO (prevents reinvasion, does not kill intracellular parasites). Immunity-independent: YES (passive antibodies work without endogenous immunity). Multi-stage: NO (extracellular stages only). |
| **Cargill fit** | HIGH — colostrum products, dam immunization protocols, and oral supplementation are directly within Cargill's animal nutrition capabilities. Could be developed as a colostrum supplement product. |

---

### A6. Anti-P23 IgY (Egg Yolk Antibodies)

| Field | Detail |
|---|---|
| **Target/mechanism** | Chicken IgY antibodies against *C. parvum* P23 (Cp23) surface antigen. P23 is CRISPR-validated as essential for gliding motility and reinfection (Watson et al. 2025, Nature Communications). IgY targets sporozoite surface to block reinvasion. Spray-dried for oral delivery. |
| **Disease stage** | Stage 2 (Invasion — blocks reinvasion by targeting P23-dependent gliding motility). |
| **Category** | A — In vivo validated |
| **Evidence tier** | [PRELIMINARY] — single study, bovine in vivo (Cho et al. 2025). Reduced diarrhea duration and oocyst shedding. IgY survived GI transit. |
| **Species data** | Neonatal calves: significantly reduced diarrhea duration and oocyst shedding. Functional P23-specific IgY detected in fecal samples throughout treatment (confirms GI survival). |
| **Key risk** | Single study, no independent replication. Cannot cure established infection (P23 KO parasites replicate and egress normally — P23 only needed for reinvasion). Manufacturing scalability at dairy farm economics (<$5-10/treatment). Stability in abomasum. |
| **Proposed de-risk** | (1) Independent replication of calf trial with larger n and oocyst quantification. (2) Cost-of-goods analysis for egg-based IgY production at dairy scale. (3) Enteric encapsulation to improve abomasal survival. |
| **Sapper constraint compliance** | Cidal: NO (blocks reinvasion only). Immunity-independent: YES (passive antibodies). Multi-stage: NO (extracellular sporozoite/merozoite transit only). |
| **Cargill fit** | HIGH — egg-based products, oral supplementation, feed-additive compatible. Spray-dried IgY can be formulated as a feed additive or oral supplement. This is squarely within Cargill's manufacturing and distribution capabilities. |

---

### A7. Halofuginone (Halocur) — Existing Standard

| Field | Detail |
|---|---|
| **Target/mechanism** | Prolyl-tRNA synthetase (PRS) inhibitor. Cryptostatic — activates amino acid response via integrated stress response. Licensed in EU at 100 mcg/kg/day for 7 days. |
| **Disease stage** | Stage 3 (Intracellular Development) — slows parasite proliferation. |
| **Category** | A — In vivo validated |
| **Evidence tier** | [ESTABLISHED] — meta-analysis of 14 studies. Reduces oocyst shedding, some mortality benefit, but does NOT cure. Diarrhea reduction NOT significant in low-bias studies. |
| **Species data** | Neonatal calves: meta-analysis confirms prophylactic benefit when started <5 days. Razor-thin therapeutic index. No weight gain benefit. |
| **Key risk** | Cryptostatic, not cidal. Narrow therapeutic index. Host PRS homology causes toxicity. Does not cure. Autoinfection rebound after withdrawal. |
| **Proposed de-risk** | None — this is the existing benchmark, not a development candidate. Include as comparator only. |
| **Sapper constraint compliance** | FAILS on: cidal (NO — cryptostatic), safety margin (MINIMAL — narrow TI), therapeutic use (NO — prophylactic only). |
| **Cargill fit** | MODERATE — oral, licensed product. But not owned by Cargill and patent/commercial landscape unclear. |

**Strategic note:** Halofuginone is the benchmark, not the goal. Any new candidate must demonstrate superiority to halofuginone on at least one axis (cidal vs static, therapeutic vs prophylactic, safety margin).

---

## Category B: Known Approaches

Literature-supported targets with evidence but requiring additional development. Each represents a specific mechanism, not a category.

---

### B1. CpPheRS Inhibition — BRD7929 (Bicyclic Azetidine)

| Field | Detail |
|---|---|
| **Target/mechanism** | *C. parvum* phenylalanyl-tRNA synthetase (CpPheRS). Blocks nuclear replication — treated cultures show only trophozoites, preventing meront progression. EC50 62 nM. CRISPR target validation. |
| **Disease stage** | Stage 3 (Intracellular Development) |
| **Category** | B — Known approach |
| **Evidence tier** | [ESTABLISHED] — cured immunosuppressed NOD SCID Gamma mice (10 mg/kg, 4 days, no relapse at 14 days). [MODERATE] — no calf data published. |
| **Species data** | Mouse only. Cured infection in highly immunosuppressed mice — one of very few compounds achieving this. |
| **Key risk** | 23-fold resistance from single CRISPR mutation (L482V). No calf data. Single tRNA synthetase target (MetRS precedent for rapid resistance). |
| **Proposed de-risk** | (1) In vitro resistance selection frequency determination at clinically relevant concentrations. (2) Neonatal calf efficacy trial (n=8-12). (3) If resistance barrier acceptable: develop as combination partner only (never monotherapy). |
| **Sapper constraint compliance** | Cidal: YES (cured immunosuppressed mice). Immunity-independent: YES (NSG mice). Multi-stage: PARTIAL (blocks meront progression). Resistance barrier: MODERATE-LOW (23-fold from single mutation). |
| **Cargill fit** | LOW — novel chemistry, pharma development. |

---

### B2. CpKRS Inhibition — DDD01510706 (Lysyl-tRNA Synthetase)

| Field | Detail |
|---|---|
| **Target/mechanism** | *C. parvum* lysyl-tRNA synthetase (CpKRS). EC50 1.3 uM. CRISPR-validated as essential. Third aminoacyl-tRNA synthetase target after MetRS and PheRS. |
| **Disease stage** | Stage 3 (Intracellular Development) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — CRISPR essential, in vitro activity confirmed |
| **Species data** | In vitro only. No mouse or calf data published. |
| **Key risk** | No in-vivo data. Single-mutation resistance risk (precedent from MetRS, PheRS). EC50 of 1.3 uM is higher than BRD7929 (62 nM) — may need dose optimization. |
| **Proposed de-risk** | (1) In vitro resistance selection. (2) Immunosuppressed mouse efficacy. (3) Only advance if resistance barrier is demonstrably higher than MetRS/PheRS. |
| **Sapper constraint compliance** | All: UNKNOWN — insufficient data. |
| **Cargill fit** | LOW |

---

### B3. CpLDH + CpPyK Dual Glycolytic Inhibition

| Field | Detail |
|---|---|
| **Target/mechanism** | Simultaneous inhibition of *C. parvum* lactate dehydrogenase (CpLDH, NSC158011, IC50 14.88 uM) and pyruvate kinase (CpPyK, NSC252172, EC50 10-86 uM). Exploits the parasite's near-complete dependence on glycolysis (no functional TCA cycle or oxidative phosphorylation). SYNERGISTIC combination — dual inhibition addresses metabolic flexibility concern. |
| **Disease stage** | Stage 3 (Intracellular Development) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — in vitro synergy demonstrated (Khan et al. 2023, AAC). Mouse efficacy for individual compounds. Oocyst reduction in mice. |
| **Species data** | Mouse in vivo for individual compounds. In vitro synergy. No calf data. |
| **Key risk** | Relatively high EC50 values (micromolar range — may require high oral doses). Host glycolytic enzyme homology (must confirm selectivity). No calf data. |
| **Proposed de-risk** | (1) Host selectivity assessment (bovine LDH and PK homology analysis + selectivity assay). (2) Combination synergy validation in ALI organoid model. (3) If selective: neonatal calf dose-finding. |
| **Sapper constraint compliance** | Cidal: UNKNOWN. Immunity-independent: UNKNOWN (mouse model, not immunosuppressed). Multi-stage: PROBABLE (glycolysis required by all stages). Resistance barrier: HIGHER (dual-target combination). |
| **Cargill fit** | MODERATE — if compounds are simple small molecules with acceptable COGS, oral delivery as feed additive is feasible. |

**Strategic note:** The dual-target combination design directly addresses Sapper Constraint 5 (high resistance barrier). Two simultaneous mutations in essential glycolytic enzymes would be required for resistance — significantly higher barrier than single-target approaches.

---

### B4. CpHDAC3 Inhibition — Vorinostat (SAHA)

| Field | Detail |
|---|---|
| **Target/mechanism** | *C. parvum* histone deacetylase 3 (CpHDAC3). Vorinostat (SAHA) is an FDA-approved HDAC inhibitor (for cutaneous T-cell lymphoma). EC50 0.203 uM against *C. parvum*. Disrupts parasite epigenetic regulation and gene expression. |
| **Disease stage** | Stage 3 (Intracellular Development) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — in vitro potent (EC50 0.203 uM), oocyst reduction in immunocompromised mice |
| **Species data** | Immunocompromised mouse in vivo. No calf data. |
| **Key risk** | Host HDAC homology — vorinostat inhibits human/bovine HDACs (known side effects in oncology patients: thrombocytopenia, fatigue, nausea). Neonatal safety is a major concern. Need CpHDAC3-selective inhibitor. |
| **Proposed de-risk** | (1) CpHDAC3 vs bovine HDAC3 structural comparison and selectivity modeling. (2) If sufficient divergence: design Crypto-selective HDAC inhibitors. (3) Screen existing HDAC inhibitor libraries for Crypto selectivity. |
| **Sapper constraint compliance** | Cidal: UNKNOWN. Immunity-independent: PROBABLY (mouse model was immunocompromised). Multi-stage: PROBABLE (epigenetic regulation required across lifecycle). Resistance barrier: UNKNOWN. Neonatal safety: HIGH RISK without selectivity. |
| **Cargill fit** | LOW — requires selective inhibitor development, pharma chemistry. |

---

### B5. CpPDE1 Inhibition — Pyrazolopyrimidine Phosphodiesterase Inhibitors

| Field | Detail |
|---|---|
| **Target/mechanism** | *C. parvum* phosphodiesterase 1 (CpPDE1). Novel target discovered 2024 (Ajiboye et al., Nature Communications). Pyrazolopyrimidine human PDE-V inhibitors repurposed. CpPDE1 is continuously expressed during asexual growth. CRISPR-validated: V900A mutation alters susceptibility, confirming target. Affects parasite host cell egress. Inhibits both *C. parvum* and *C. hominis*. |
| **Disease stage** | Stage 3 (Intracellular Development — egress) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — orally efficacious in immunocompromised mice. CRISPR target validation. Minimal off-target effects in safety panel. 2024 discovery. |
| **Species data** | Immunocompromised mouse in vivo. No calf data. |
| **Key risk** | No calf data. Egress-blocking mechanism may be static (arrests parasites without killing). Host PDE cross-reactivity (sildenafil does NOT affect Crypto — structural basis identified). Early discovery stage. |
| **Proposed de-risk** | (1) Time-kill assay to determine cidal vs static mechanism. (2) Neonatal calf safety/efficacy trial. (3) Selectivity profiling against bovine PDEs (especially PDE5, PDE3 — cardiovascular relevant). |
| **Sapper constraint compliance** | Cidal: UNKNOWN (affects egress — may be static). Immunity-independent: YES (immunocompromised mice). Multi-stage: PARTIAL (egress across asexual stages). Resistance barrier: UNKNOWN. |
| **Cargill fit** | LOW-MODERATE — depends on compound chemistry. |

**Strategic note:** The structural divergence between CpPDE1 and human PDE-V (Val900 and His884 replace alanines, blocking sildenafil binding) suggests the Crypto active site can be selectively targeted. This is one of the few targets where parasite selectivity is structurally demonstrated.

---

### B6. Host Squalene Synthase Inhibition — Lapaquistat (FDFT1 Pathway)

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED. Inhibits host squalene synthase (FDFT1), reducing squalene accumulation in enterocytes. Squalene buildup creates a reducing environment that makes more reduced glutathione (GSH) available for parasite uptake. *C. parvum* has LOST glutathione synthesis — entirely dependent on host GSH import. Lapaquistat shifts host redox environment against the parasite. Discovery via genome-wide CRISPR-Cas9 KO screen (Cell, 2025). |
| **Disease stage** | Stage 3 (Intracellular Development — disrupts parasite metabolic dependency). |
| **Category** | B — Known approach (abandoned drug repurposed) |
| **Evidence tier** | [ESTABLISHED] — genome-wide CRISPR screen discovery (Cell, 2025). In vitro and in vivo (mouse) efficacy demonstrated. |
| **Species data** | Mouse in vivo. No calf data. |
| **Key risk** | HOST-DIRECTED = host cell effects. Lapaquistat was abandoned in human cholesterol trials due to hepatotoxicity (elevated transaminases). Neonatal calf liver is immature — hepatotoxicity risk may be higher. Oral bioavailability and gut-restricted delivery not characterized. |
| **Proposed de-risk** | (1) Assess whether gut-restricted formulation is possible (lapaquistat acting only on enterocytes, not systemically). (2) Neonatal calf safety study with hepatic monitoring. (3) Evaluate alternative squalene synthase inhibitors with better safety profiles. |
| **Sapper constraint compliance** | Cidal: PROBABLY NOT (shifts metabolic environment, likely static). Immunity-independent: YES (acts on host cell, not immune system). Multi-stage: YES (all intracellular stages require host GSH). Resistance barrier: VERY HIGH (parasite cannot evolve around host enzyme). Neonatal safety: HIGH RISK (abandoned for hepatotoxicity). |
| **Cargill fit** | MODERATE — if a safe gut-restricted formulation is achievable, could be oral feed additive. But drug repurposing requires regulatory expertise. |

**Strategic note:** The resistance barrier advantage is enormous — the parasite cannot mutate around a host-directed mechanism. This makes squalene pathway intervention strategically important even if lapaquistat itself is not the final molecule.

---

### B7. Bovilis Cryptium Enhancement — gp40/gp60 Maternal Vaccination + Boosted Formulation

| Field | Detail |
|---|---|
| **Target/mechanism** | Maternal vaccination with gp40 antigen (processed from gp60, major sporozoite attachment glycoprotein). Bovilis Cryptium is EU-approved (November 2023) but shows clinically marginal effect (0.4-day diarrhea reduction). The question is whether enhancement (adjuvant optimization, multi-antigen formulation, or combination with oral calf treatment) can reach clinically meaningful benefit. |
| **Disease stage** | Stage 0 (Upstream Susceptibility) + Stage 2 (Invasion) |
| **Category** | B — Known approach (approved product) |
| **Evidence tier** | [ESTABLISHED] — EU-approved. Significantly elevated colostral antibody titers. But clinically marginal effect. |
| **Species data** | 283 dairy calves: 1.8 vs 2.2 days diarrhea (p=0.03 but clinically marginal). NO significant reduction in moderate-to-severe diarrhea. |
| **Key risk** | The fundamental limitation is modality, not antigen: passive antibodies cannot achieve sufficient occupancy in distal ileum, wane during peak vulnerability, and cannot reach the epicellular niche. Enhancement is ceiling-bounded. |
| **Proposed de-risk** | (1) Test Bovilis Cryptium in COMBINATION with an oral antiparasitic in calves on problem farms with high infection pressure (the missing trial). (2) Evaluate multi-antigen vaccine (gp40 + P23 + Cp-P34). |
| **Sapper constraint compliance** | Cannot satisfy constraints as standalone. Value only as adjunct in combination. |
| **Cargill fit** | LOW — vaccine development is MSD's domain, not Cargill's. Cargill role would be as the oral treatment partner. |

---

### B8. Paromomycin Derivative — Gut-Restricted Aminoglycoside

| Field | Detail |
|---|---|
| **Target/mechanism** | Paromomycin validates that the epicellular niche IS accessible from the luminal/apical side. The concept: a next-generation aminoglycoside or aminoglycoside-like compound engineered to be non-absorbed, non-nephrotoxic, and cidal rather than static. |
| **Disease stage** | Stage 3 (Intracellular Development) |
| **Category** | B — Known approach (modality validated by paromomycin) |
| **Evidence tier** | [MODERATE] — paromomycin bovine data validates the apical access concept. No improved derivative exists. |
| **Species data** | Paromomycin in calves: prophylactic use suppresses oocyst shedding during treatment, but rebound after withdrawal (cryptostatic). |
| **Key risk** | No improved aminoglycoside derivative exists for Crypto. Aminoglycosides are inherently nephrotoxic. The class may be intrinsically static against Crypto. |
| **Proposed de-risk** | This is a medicinal chemistry concept, not a development candidate. Propose only if a specific non-nephrotoxic, cidal aminoglycoside analog is identified. |
| **Sapper constraint compliance** | Concept only — depends on the specific molecule. |
| **Cargill fit** | MODERATE — if a gut-restricted oral formulation is developed, fits oral/feed-additive delivery. |

---

### B9. Anti-Sporozoite Adhesion — Competitive Carbohydrate Blockade (Gal-GalNAc)

| Field | Detail |
|---|---|
| **Target/mechanism** | Sporozoites attach to intestinal epithelial cells via lectin-carbohydrate interactions, with Gal-GalNAc (galactose-N-acetylgalactosamine) on host cells as primary receptors. Competitive blockade with free Gal-GalNAc or mucin-like decoys could reduce attachment efficiency. |
| **Disease stage** | Stage 2 (Invasion — blocks sporozoite attachment) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — attachment specificity established. In vitro data showing lectin competition reduces attachment. No in vivo data in calves. |
| **Species data** | In vitro only. |
| **Key risk** | Achieving sufficient luminal concentration of free sugars in the distal ileum to outcompete host surface glycoconjugates is pharmacologically daunting. Sugar dilution in 8-12 meters of calf intestine. Continuous re-exposure to oocysts may overwhelm competitive blockade. |
| **Proposed de-risk** | (1) In vitro dose-response: what concentration of free Gal-GalNAc reduces attachment by >90%? (2) Feasibility calculation: can this concentration be achieved in the distal ileum via oral delivery? |
| **Sapper constraint compliance** | Cidal: NO. Multi-stage: NO (attachment only). Resistance barrier: MODERATE (pathogen could evolve alternative attachment). |
| **Cargill fit** | HIGH — simple sugars/oligosaccharides as feed additives are core Cargill capability. If biologically feasible, this is the most Cargill-aligned candidate. |

**Embarrassment scenario:** "We spent $200K developing a Gal-GalNAc feed additive and it reduced attachment by 5% because the sugar was diluted to irrelevant concentrations in the ileum."

---

### B10. Anti-Secretory Therapy — Racecadotril (Enkephalinase Inhibitor)

| Field | Detail |
|---|---|
| **Target/mechanism** | Racecadotril inhibits enkephalinase (neutral endopeptidase), which potentiates endogenous enkephalins that reduce intestinal hypersecretion via delta-opioid receptors. Does NOT reduce motility (unlike loperamide). Anti-secretory without anti-motility = preserves normal transit while reducing fluid loss. Approved for human pediatric diarrhea in many countries. |
| **Disease stage** | Stage 5 (Intestinal Pathology — reduces secretory component of diarrhea) |
| **Category** | B — Known approach |
| **Evidence tier** | [PRELIMINARY] — racecadotril PK characterized in neonatal calves (healthy and diarrheic, 2022 study). NOT tested for anti-crypto efficacy. Established anti-secretory efficacy in human pediatric diarrhea. |
| **Species data** | PK in healthy neonatal calves: t1/2 4.70h, Cmax 377 ng/mL. CRITICAL FINDING: In diarrheic calves (including Crypto), racecadotril and thiorphan were only detected at 0.25-1.5h — very rapid elimination, likely due to malabsorption. |
| **Key risk** | PK data shows diarrhea dramatically reduces racecadotril absorption — the same pharmacokinetic paradox that killed clofazimine. If it requires systemic absorption, it will fail in sick calves. NOT a cure — symptomatic only. Does not address parasite. |
| **Proposed de-risk** | (1) Evaluate whether racecadotril's anti-secretory effect is achievable via luminal (non-absorbed) action. (2) If yes: test as adjunct to ORS in crypto-positive calves for reduction of dehydration severity. (3) If PK problem is insurmountable: consider alternative anti-secretory agents. |
| **Sapper constraint compliance** | Does NOT address parasite — symptomatic support only. Value only as ADJUNCT to reduce dehydration severity and improve supportive care outcomes. |
| **Cargill fit** | MODERATE — oral drug, but may require prescription status. |

---

### B11. Anti-Secretory Therapy — Crofelemer (CFTR Chloride Channel Blocker)

| Field | Detail |
|---|---|
| **Target/mechanism** | Crofelemer (Mytesi) is an FDA-approved anti-secretory agent that inhibits both CFTR (cystic fibrosis transmembrane conductance regulator) chloride channels and calcium-activated chloride channels (CaCC) at the luminal surface of enterocytes. Acts LOCALLY in the gut lumen — not systemically absorbed. Reduces chloride and water secretion. Approved for HIV-associated diarrhea. |
| **Disease stage** | Stage 5 (Intestinal Pathology — reduces secretory diarrhea) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — FDA-approved for secretory diarrhea in HIV patients. NOT tested against cryptosporidiosis specifically. Derived from *Croton lechleri* (dragon's blood tree) — a botanical extract. |
| **Species data** | Human (HIV-associated diarrhea). No calf data. |
| **Key risk** | Not tested in calves. Not tested specifically for crypto diarrhea. Botanical extract with complex composition. Regulatory pathway for veterinary use unclear. |
| **Proposed de-risk** | (1) In vitro: test crofelemer effect on chloride secretion in *C. parvum*-infected bovine enteroid monolayers. (2) If effective: pilot calf trial as adjunct to ORS. |
| **Sapper constraint compliance** | Does NOT address parasite — anti-secretory adjunct only. Key advantage: LUMINAL action, not absorbed. |
| **Cargill fit** | MODERATE — botanical extract, oral delivery. Natural product sourcing may align with Cargill nutrition capabilities if active principle can be standardized. |

**Strategic note:** Crofelemer's advantage over racecadotril is that it acts luminally (at the CFTR/CaCC on the apical membrane) without requiring systemic absorption. This avoids the PK paradox that plagues systemically absorbed drugs in diarrheic calves.

---

### B12. Colostrum Supplementation — Standardized High-Quality Bovine Colostrum Product

| Field | Detail |
|---|---|
| **Target/mechanism** | Not hyperimmune — standard high-quality colostrum supplementation. Provides passive IgG1/IgA, immunomodulatory cells (macrophages, lymphocytes, neutrophils), cytokines (IFN-gamma), and promotes resilient microbiome development with protective Bifidobacterium species. |
| **Disease stage** | Stage 0 (Upstream Susceptibility — improves passive immunity and microbiome resilience) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — bovine in vivo: colostrum supplementation mitigated some clinical signs, modulated gut immune response and microbiota to pattern more similar to healthy calves (2023 study). |
| **Species data** | Neonatal calves: limited diarrhea mitigation but modulated host gut immune responses and concomitant microbiota. |
| **Key risk** | Does not prevent infection. Effect is modest. Colostral quality varies enormously by source. |
| **Proposed de-risk** | None needed — this is a baseline management improvement, not a drug candidate. Include in portfolio as standard-of-care recommendation. |
| **Sapper constraint compliance** | Does NOT address parasite directly. Adjunct only. |
| **Cargill fit** | VERY HIGH — colostrum supplementation products are core Cargill capability. Standardization and quality control of colostrum products is a direct commercial opportunity. |

---

### B13. Oral Rehydration Optimization — Improved ORS with Glycine/Glutamine

| Field | Detail |
|---|---|
| **Target/mechanism** | Enhanced ORS formulations incorporating glycine (co-transported with sodium independently of SGLT1) and L-glutamine (primary fuel for enterocytes, promotes mucosal repair). Standard ORS relies on sodium-glucose co-transport via SGLT1, which is downregulated during crypto infection due to villous atrophy. Glycine-based ORS may improve absorption when SGLT1 is compromised. |
| **Disease stage** | Stage 5 (Intestinal Pathology — improves rehydration and mucosal support during active infection) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — glycine-based ORS established in human pediatric diarrhea. Glutamine supplementation reduces mucosal permeability in intestinal injury models. Not tested specifically for bovine cryptosporidiosis. |
| **Species data** | Human and animal models for glycine/glutamine. Bovine ORS is standard practice but formulations not optimized for crypto-specific pathophysiology. |
| **Key risk** | Symptomatic support only — does not address parasite. Incremental improvement, not transformative. |
| **Proposed de-risk** | Controlled trial in crypto-positive calves: standard ORS vs glycine/glutamine-enhanced ORS. Primary endpoint: days to clinical recovery. Secondary: weight at 30 days. |
| **Cargill fit** | VERY HIGH — oral rehydration products, nutritional supplements are core Cargill capability. |

---

### B14. Nitazoxanide Veterinary Reformulation — Gut-Restricted Derivative

| Field | Detail |
|---|---|
| **Target/mechanism** | The NTZ mechanism against Crypto remains uncertain (may involve unique PFOR with fused CYP domain, or host-mediated mechanisms). The concept: reformulate NTZ or tizoxanide as a gut-restricted compound (EDI048 strategy applied to NTZ scaffold) to maximize luminal concentration while minimizing systemic exposure. |
| **Disease stage** | Stage 3 (Intracellular Development) |
| **Category** | B — Known approach |
| **Evidence tier** | [MODERATE] — NTZ has conflicting calf data. Immune dependence is the primary concern. Gut-restricted reformulation addresses the PK problem but NOT the immune dependence. |
| **Key risk** | FUNDAMENTAL: NTZ appears to require immune cooperation. Gut-restricted formulation solves PK but if the drug needs immunity to work, it will still fail in neonates. This is a TARGET question, not a formulation question. |
| **Proposed de-risk** | (1) Test NTZ/tizoxanide in immunosuppressed mouse model to definitively resolve whether activity is immune-dependent or direct. If immune-dependent: KILL this candidate. If direct: proceed to gut-restricted formulation. |
| **Sapper constraint compliance** | Immunity-independent: LIKELY NO — this is the fundamental risk. |
| **Cargill fit** | MODERATE — simple small molecule, oral delivery. |

---

### B15. Combination: EDI048 + AN7973 (PI4K + CPSF3 Dual Therapy)

| Field | Detail |
|---|---|
| **Target/mechanism** | Rational combination of the two most promising compound classes. EDI048 blocks segmentation/egress (potentially static) while AN7973 achieves cidal killing across lifecycle stages. Dual-target combination addresses resistance barrier (two simultaneous mutations required). Covers the autoinfection cycle from both ends. |
| **Disease stage** | Stage 3 (Intracellular Development — comprehensive) |
| **Category** | B — Known approach (combination of established leads) |
| **Evidence tier** | [INFERRED] — both compounds individually validated in calves; combination not tested |
| **Key risk** | Neither compound is veterinary-approved. Cost of dual therapy. Drug-drug interactions in the gut lumen. Regulatory complexity of combination product (Quality Standard 23: FDA-CVM requires proof of contribution for each API). |
| **Proposed de-risk** | (1) In vitro combination synergy/antagonism testing in ALI organoid. (2) If synergistic or additive: calf efficacy trial of combination vs each agent alone. (3) Regulatory strategy: develop as co-packaged products rather than fixed-dose combination to simplify regulatory path. |
| **Sapper constraint compliance** | Cidal: YES (AN7973 component). Immunity-independent: YES (both work in immunosuppressed mice). Multi-stage: YES (complementary mechanisms). Resistance barrier: HIGH (dual-target). Luminal: YES (EDI048 gut-restricted; AN7973 oral). |
| **Cargill fit** | LOW — requires pharma partnership for both compounds. |

**Strategic note:** This combination is the theoretical optimum against the constraint set. It is also the most commercially challenging to develop. Include as the aspirational target; pursue individual components in parallel.

---

## Category C: Non-Obvious Approaches

Cross-disease analogies, emerging biology, and repurposed mechanisms.

---

### C1. NOD2 Agonism — MDP (Muramyl Dipeptide) or Derivatives

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED. NOD2 receptor stimulation via MDP reduces *C. parvum* parasite burden in neonatal mice by: (1) increasing pro-inflammatory cytokine and antimicrobial peptide gene expression, (2) rapid neutrophil influx to infection site, (3) increasing intestinal epithelium renewal (shedding infected cells), (4) IFN-gamma and IL-22 involvement. Mechanism does NOT require microbiota participation. Published 2025 (European Journal of Immunology). |
| **Disease stage** | Stage 4 (Host Immune Response — innate immune acceleration) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [PRELIMINARY] — neonatal mouse in vivo (2025). Rapid parasite burden reduction. Single study. |
| **Species data** | Neonatal mice only. No calf data. |
| **Key risk** | Mouse-to-calf translation gap. MDP itself has known pyrogenicity and rapid elimination. Need orally bioavailable, non-pyrogenic NOD2 agonist. IP injection route used in mice is not practical for calves. Neonatal safety of innate immune stimulation unknown. |
| **Proposed de-risk** | (1) Identify orally bioavailable NOD2 agonists from published SAR studies (reviewed 2024, European Journal of Medicinal Chemistry). (2) Test oral NOD2 agonist in neonatal calf crypto model. (3) Safety: monitor for excessive inflammatory response and fever in neonates. |
| **Sapper constraint compliance** | Immunity-independent: PARTIALLY — activates INNATE immunity (not adaptive CD4+/IFN-gamma), which may be more mature in neonates. Multi-stage: YES (epithelial renewal sheds infected cells regardless of parasite stage). |
| **Cargill fit** | HIGH — if an oral NOD2 agonist is identified, it could be formulated as a feed additive. MDP itself is a bacterial cell wall component — structurally related to compounds already in feed additive space. Beta-glucan and other innate immune stimulants are within Cargill's portfolio. |

**Strategic note:** This is one of the most important new findings. The IL-22-mediated epithelial renewal mechanism is particularly interesting — it eliminates infected cells (a "dump the cell" strategy) rather than trying to kill the parasite within its niche. This bypasses the drug access barrier entirely.

---

### C2. IFN-lambda (Type III Interferon) Supplementation

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED. IFN-lambda acts primarily on epithelial cells (restricted receptor expression) with fewer systemic inflammatory side effects than IFN-gamma. *C. parvum* infection of human intestinal ALI cultures induces strong type III IFN secretion (2024 study, Gut Microbes). IFN-lambda is the dominant epithelial antiviral/antiparasitic interferon at mucosal surfaces. |
| **Disease stage** | Stage 4 (Host Immune Response — epithelial-restricted immune potentiation) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [PRELIMINARY] — human ALI organoid data shows *C. parvum* induces type III IFN (2024). Mouse studies support IFN-lambda in mucosal crypto defense. No bovine data. |
| **Species data** | Human organoid and mouse. No bovine data. |
| **Key risk** | Recombinant bovine IFN-lambda not commercially available. Protein half-life issues (short). Oral delivery of cytokines is challenging (degradation in GI tract). Neonatal calf IFN-lambda receptor maturity unknown. |
| **Proposed de-risk** | (1) Confirm bovine IFN-lambda receptor expression in neonatal calf ileal epithelium (immunohistochemistry). (2) If receptors present: test recombinant bovine IFN-lambda in bovine enteroid model + *C. parvum*. (3) Explore IFN-lambda-inducing oral agents as alternative to recombinant protein (e.g., TLR3 agonists like poly(I:C)). |
| **Sapper constraint compliance** | Immunity-independent: PARTIALLY — IFN-lambda activates epithelial cell-intrinsic defense, not adaptive immunity. May be functional in neonates if epithelial receptor is expressed. |
| **Cargill fit** | LOW (recombinant protein) to MODERATE (IFN-lambda-inducing oral agents). |

**Strategic note:** The external panel flagged IFN-lambda as a better neonatal immune target than IFN-gamma because it acts on epithelium (the site of infection) without systemic inflammatory risk. This is an important conceptual shift from systemic immunomodulation to mucosal-restricted immunomodulation.

---

### C3. Beta-Glucan Trained Immunity — Yeast Cell Wall Supplementation

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED. Beta-1,3/1,6-glucans from yeast cell walls (*Saccharomyces cerevisiae*) induce "trained immunity" in innate immune cells — epigenetic reprogramming of monocytes/macrophages that persists for weeks and enhances responsiveness to subsequent infections. Does NOT require adaptive immune memory. May accelerate the neonatal innate immune response to crypto. |
| **Disease stage** | Stage 0 (Upstream Susceptibility) + Stage 4 (Host Immune Response — innate immune priming) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [PRELIMINARY] for crypto specifically. [ESTABLISHED] for trained immunity concept (Netea et al., extensive human and animal data). [MODERATE] for beta-glucan immune effects in calves (multiple studies, but NOT specifically for crypto). |
| **Species data** | Beta-glucan supplementation in calves: improved immune parameters in multiple studies. NOT specifically tested against cryptosporidiosis in controlled trials. |
| **Key risk** | Trained immunity operates through monocytes/macrophages and NK cells — all of which are present but potentially functionally immature in neonatal calves. The scale of crypto infection (10^10 oocysts) may overwhelm any innate immune enhancement. Mouse probiotic failures are the cautionary tale. |
| **Proposed de-risk** | (1) Neonatal calf trial: beta-glucan supplementation from day 1 + experimental *C. parvum* challenge. Primary endpoints: oocyst shedding, diarrhea severity, NK cell IFN-gamma production. (2) If positive: combine with antiparasitic. |
| **Sapper constraint compliance** | Cidal: NO (supports immunity, does not directly kill). Immunity-independent: NO (enhances immune function). Multi-stage: INDIRECT. |
| **Cargill fit** | VERY HIGH — yeast cell wall beta-glucan products are existing Cargill products. This requires zero new manufacturing capability. Oral, feed-additive compatible. If efficacious, fastest path to market of any candidate. |

**Embarrassment scenario:** "We ran a controlled trial of beta-glucan against crypto in calves and it reduced oocyst shedding by <10% because neonatal innate immunity is too immature to be 'trained' in 3 days."

---

### C4. Ondansetron — 5-HT3 Receptor Antagonist (Anti-Emetic/Anti-Secretory)

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED. 5-HT3 receptor antagonist. Blocks serotonin-mediated secretory reflexes in the enteric nervous system. Crypto infection activates enterochromaffin cells, releasing serotonin that drives neurogenic chloride/water secretion via 5-HT3 receptors on enteric neurons. Ondansetron is cheap, safe, and widely available as a veterinary anti-emetic. |
| **Disease stage** | Stage 5 (Intestinal Pathology — reduces neurogenic secretory component of diarrhea) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [INFERRED] for crypto specifically. [ESTABLISHED] for ondansetron anti-secretory mechanism in enteric infections generally (piglet/human models of secretory diarrhea). |
| **Species data** | No calf data for crypto specifically. Ondansetron used in calves as anti-emetic. |
| **Key risk** | Symptomatic only — does not address parasite. May reduce fluid loss but NOT infection. If the secretory component is a minority of total diarrhea (malabsorptive may dominate), benefit will be small. |
| **Proposed de-risk** | (1) Controlled trial: ondansetron as adjunct to ORS in crypto-positive calves. Endpoints: fecal output volume, dehydration score, weight gain. Low cost (~$2-5/treatment). |
| **Sapper constraint compliance** | Does NOT address parasite. Symptomatic adjunct only. |
| **Cargill fit** | HIGH — cheap, oral, existing veterinary product (off-label use). Could be included in a Cargill crypto management protocol. |

---

### C5. Apicomplexan Cross-Class: Atovaquone-Like Compounds — Targeting Ubiquinone Pathway

| Field | Detail |
|---|---|
| **Target/mechanism** | Atovaquone targets the cytochrome bc1 complex in *Plasmodium*, *Toxoplasma*, and *Babesia*. While *C. parvum* lacks a conventional ETC, it RETAINS ubiquinone biosynthesis in its mitosome. The question: is there a functional target in the ubiquinone pathway distinct from CpAOX (which was CRISPR-invalidated)? |
| **Disease stage** | Stage 3 (Intracellular Development) |
| **Category** | C — Non-obvious (cross-Apicomplexa analogy) |
| **Evidence tier** | [INFERRED] — ubiquinone biosynthesis retained, but functional significance unknown. CpAOX non-essential. |
| **Key risk** | CpAOX knockout result strongly suggests the electron transport chain is vestigial. Targeting ubiquinone biosynthesis may fail for the same reason decoquinate failed. The mitosome may only need ubiquinone for iron-sulfur cluster assembly, not energy metabolism. |
| **Proposed de-risk** | (1) CRISPR knockout of ubiquinone biosynthesis genes to test essentiality. If non-essential: KILL. |
| **Sapper constraint compliance** | All UNKNOWN. HIGH RISK of target failure based on CpAOX precedent. |
| **Cargill fit** | LOW |

**Honest assessment:** This is included for completeness but is likely dead based on the mitosome biology. Decoquinate, ionophores, and CpAOX KO all point to vestigial mitochondrial function. Do not prioritize.

---

### C6. Bile Acid Sequestrant — Cholestyramine for Secondary Bile Acid Diarrhea

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED / SYMPTOMATIC. *C. parvum* destroys the terminal ileum — the exclusive site of active bile acid reabsorption (via ASBT). Ileal damage leads to bile acid malabsorption and spillover into the colon, where bile acids act as potent secretagogues (stimulate colonic chloride/water secretion via TGR5 and detergent effects). Cholestyramine sequesters bile acids in the intestinal lumen, preventing their secretory effects. |
| **Disease stage** | Stage 5 (Intestinal Pathology — addresses bile acid-mediated colonic secretory diarrhea) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [INFERRED] for crypto. [ESTABLISHED] for bile acid sequestrant mechanism in bile acid malabsorption diarrhea. Used empirically in some calf diarrhea protocols but never formally tested for crypto-specific effect. |
| **Species data** | No calf data specifically for crypto-associated bile acid diarrhea. |
| **Key risk** | Cholestyramine is unpalatable and may reduce absorption of other oral drugs and nutrients. Binding capacity may be overwhelmed if bile acid malabsorption is massive. Symptomatic only. |
| **Proposed de-risk** | (1) Measure fecal bile acid concentrations in crypto-positive vs crypto-negative diarrheic calves to quantify the bile acid malabsorption component. If elevated: trial cholestyramine as ORS adjunct. |
| **Cargill fit** | MODERATE — oral, feed-additive compatible, but palatability issues. |

---

### C7. Anti-Apoptosis Reversal — Pro-Apoptotic Agents to Eject Infected Cells

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED. *C. parvum* actively INHIBITS host cell apoptosis early in infection (upregulates Bcl-2, activates NF-kB/PI3K/Akt survival signaling) to maintain its intracellular niche. Reversing this — promoting apoptosis of infected cells — would eject the parasite from its niche, exposing it to luminal drugs and immune effectors. This is the "dump the cell" strategy. |
| **Disease stage** | Stage 3 (Intracellular Development — disrupts niche maintenance) + Stage 4 (Host Immune Response — activates cell-intrinsic defense) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [MODERATE] — parasite anti-apoptotic manipulation well-documented (Laurent 1998, Chen 2001, McCole 2000). Pro-apoptotic drug concept is [INFERRED]. |
| **Key risk** | CRITICAL DILEMMA: accelerating apoptosis of infected enterocytes would worsen villous atrophy and malabsorption. In neonates with already limited regenerative capacity, this could be more harmful than helpful. The trade-off between ejecting parasites and losing absorptive surface may be unfavorable. |
| **Proposed de-risk** | (1) Bovine enteroid model: test whether BH3 mimetics (e.g., ABT-199/venetoclax at low doses) selectively increase apoptosis of infected cells without destroying uninfected neighbors. (2) Quantify: does infected cell ejection reduce parasite burden more than it worsens pathology? |
| **Sapper constraint compliance** | Neonatal safety: HIGH RISK (worsens epithelial damage in already compromised gut). |
| **Cargill fit** | LOW — requires pharma-level drug development. |

**Honest assessment:** The dilemma is real. The NOD2/MDP approach (C1) achieves the same "cell ejection" strategy but via epithelial RENEWAL rather than targeted apoptosis, which may be safer. Prefer C1 over C7.

---

### C8. Nanobody (VHH) Oral Delivery Against Sporozoite Surface Antigens

| Field | Detail |
|---|---|
| **Target/mechanism** | Camelid-derived single-domain antibodies (VHHs/nanobodies, ~12-15 kDa) targeting sporozoite surface antigens (gp900, Cp-P34). VHHs are ~10x smaller than conventional IgG, more acid-stable, and can be produced cheaply in yeast or bacteria. Cp-P34 is a novel surface protein unique to Cryptosporidium, identified via VHH selection (2021 study). VHHs against gp900 and Cp-P34 have been generated. |
| **Disease stage** | Stage 2 (Invasion — blocks sporozoite attachment/gliding) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [PRELIMINARY] — VHHs against Crypto surface antigens identified. Cp-P34 characterized. No in vivo efficacy data. |
| **Species data** | In vitro binding demonstrated. No animal efficacy data. |
| **Key risk** | Same fundamental limitation as all antibody approaches: cannot reach epicellular niche. But nanobodies' acid stability and small size improve luminal survival and mucosal penetration compared to conventional IgG/IgY. Anti-reinvasion only, not curative. Production scalability at dairy economics. |
| **Proposed de-risk** | (1) In vitro neutralization assay: do anti-Cp-P34 and anti-gp900 VHHs block sporozoite attachment? (2) Oral delivery stability: measure functional VHH in calf ileal contents after oral dosing. (3) If stable and neutralizing: calf efficacy trial as adjunct to antiparasitic. |
| **Sapper constraint compliance** | Cidal: NO. Multi-stage: NO. Value as reinvasion blocker only, in combination. |
| **Cargill fit** | MODERATE-HIGH — VHHs can be produced in yeast (*Pichia*) at scale. If production economics work, oral VHH supplement is aligned with Cargill capabilities. |

---

### C9. Microbiome Engineering — Defined Consortium for Colonization Resistance

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED. Rather than generic probiotics, design a defined microbial consortium that specifically DEPLETES the metabolites *C. parvum* scavenges from the gut environment. Hares et al. (2023) showed that pre-infection microbiome functional profiles predicting susceptibility had elevated isoprenoid precursor, haem, and purine biosynthesis — metabolites the parasite cannot synthesize. A consortium that consumes these metabolites competitively could create a nutrient-poor niche for the parasite. |
| **Disease stage** | Stage 0 (Upstream Susceptibility — microbiome-mediated resistance) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [INFERRED] — based on Hares et al. 2023 metabolomic association data. Causation not established. |
| **Key risk** | Association is not causation. The metabolite-scavenging hypothesis is unproven. Neonatal microbiome colonization dynamics are complex and unpredictable. Previous generic probiotic failures (Lactobacillus in field calves: no effect). |
| **Proposed de-risk** | (1) In vitro: test whether depleting purine/haem/isoprenoid precursors from culture medium reduces *C. parvum* growth. If YES: supports the scavenging hypothesis. (2) If validated: design defined consortium and test in neonatal calf challenge model. |
| **Sapper constraint compliance** | Cidal: NO. Multi-stage: INDIRECT. Scale adequacy: QUESTIONABLE (probiotics failed at the 10^10 oocyst scale). |
| **Cargill fit** | VERY HIGH — defined microbial consortia, probiotics, and gut health products are core Cargill capability. If the biology works, commercialization is straightforward. |

---

### C10. Quorum Sensing Disruption — Blocking Parasite Developmental Coordination

| Field | Detail |
|---|---|
| **Target/mechanism** | PARASITE-DIRECTED. The external panel (Gemini) flagged that *C. parvum* executes an intrinsic program of 3 asexual generations before committing to sexual development. If this commitment is influenced by parasite density through quorum sensing-like mechanisms (extracellular vesicles, secreted signals — demonstrated in *Toxoplasma gondii*), disrupting this signaling could: (a) prevent sexual development and oocyst production, (b) lock parasites in non-replicative states, or (c) desynchronize the lifecycle to impair autoinfection. |
| **Disease stage** | Stage 3 (Intracellular Development — blocks sexual commitment) + Stage 6 (Shedding — prevents oocyst formation) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [INFERRED] — quorum sensing not yet demonstrated in Cryptosporidium. Concept from Toxoplasma EV biology (Bhatia et al. 2022). Speculative. |
| **Key risk** | No evidence that Crypto uses quorum sensing. The asexual-to-sexual switch may be purely intrinsic (cell-autonomous). Even if quorum sensing exists, the molecular identity of the signal is unknown. |
| **Proposed de-risk** | (1) Test whether conditioned media from heavily infected cultures affects sexual commitment rates in fresh infections. If YES: quorum sensing is operating. (2) Proteomic analysis of *C. parvum* extracellular vesicles to identify candidate signaling molecules. |
| **Cargill fit** | LOW — early-stage basic research, no near-term product. |

---

### C11. Oocyst Wall Formation Inhibitors — Targeting Gametogony/Sporulation

| Field | Detail |
|---|---|
| **Target/mechanism** | PARASITE-DIRECTED. The oocyst wall is assembled from specialized wall-forming bodies in macrogametes, using cysteine-rich wall proteins with robust cross-linking chemistry. RNA-Seq confirms oocyst wall protein genes are expressed in gametocytes and stockpiled (Lippuner et al. 2018). Inhibiting wall formation would produce non-viable or fragile oocysts that cannot survive environmental transmission or autoinfection. Target: wall-forming body biogenesis or cross-linking enzymes. |
| **Disease stage** | Stage 6 (Shedding/Transmission — prevents viable oocyst formation) |
| **Category** | C — Non-obvious approach |
| **Evidence tier** | [INFERRED] — target concept from oocyst biology. No inhibitors characterized. Wall-forming body proteins identified by RNA-Seq. |
| **Key risk** | Would NOT immediately cure individual calves (asexual stages and existing intracellular burden continue). Would reduce TRANSMISSION by producing defective oocysts. Timeline to clinical benefit is slow (requires reducing environmental contamination over calving seasons). Unknown druggability of wall proteins. |
| **Proposed de-risk** | (1) Identify the specific enzymes involved in oocyst wall cross-linking (tyrosinase-like? transglutaminase?). (2) Test inhibitors of these enzyme classes in ALI organoid model for effect on oocyst viability. |
| **Sapper constraint compliance** | Cidal for OOCYSTS (not parasites). Multi-stage: NO (gametocyte stage only). Not curative — transmission-reduction product profile. |
| **Cargill fit** | MODERATE — if a simple oral inhibitor is found, feed-additive delivery is possible. The product profile (transmission reduction, not cure) aligns with Cargill's preventive/management approach. |

**Strategic note:** This is a TRANSMISSION TARGET, not a CURE TARGET. Product profile: feed additive that reduces oocyst viability, lowering environmental contamination over time. Useful at herd level even without individual-animal cure. At R0 = 5-15, would need >90% oocyst viability reduction to meaningfully impact herd transmission — a very high bar.

---

## Category D: Novel Proposals

First-principles designs for gap stages where no existing approach has been tested.

---

### D1. IL-22-Inducing Oral Innate Immune Activator

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED / NOVEL. The NOD2/MDP data (C1) shows that IL-22 drives intestinal epithelial cell renewal in neonatal mice, which clears *C. parvum* by replacing infected cells. IL-22 is produced by ILC3 (innate lymphoid cells type 3), gamma-delta T cells, and NK cells — all present in neonatal calves. The proposal: an oral agent that specifically induces IL-22 production from intestinal ILC3 cells. This bypasses the CD4+ T cell requirement entirely. |
| **Disease stage** | Stage 4 (Host Immune Response — innate-lymphoid-cell-mediated epithelial defense) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [INFERRED] — based on IL-22's role in MDP-mediated crypto clearance (2025), ILC3 biology, and neonatal gamma-delta T cell abundance in calves. |
| **Biological rationale** | Neonatal calves have abundant gamma-delta T cells (25% of lymphocytes in week 1) and these cells produce IFN-gamma and potentially IL-22 in response to microbial stimulation. ILC3 cells are mucosal-resident and functional in neonates. IL-22 acts on epithelial cells to: (a) accelerate cell turnover (ejecting infected cells), (b) upregulate antimicrobial peptides (beta-defensins, REG3gamma), (c) strengthen barrier integrity. |
| **Intervention** | Oral administration of AhR (aryl hydrocarbon receptor) ligands — dietary compounds like indole-3-carbinol (I3C, from cruciferous vegetables) or FICZ that activate AhR in ILC3 cells, driving IL-22 production. AhR ligands are natural dietary compounds. |
| **Closest analogy** | AhR-mediated IL-22 induction protects against *Citrobacter rodentium* (attaching-effacing enteropathogen) in mouse models — a well-established mucosal defense paradigm. |
| **Most likely failure mode** | Neonatal ILC3 cells may not respond to AhR stimulation due to developmental immaturity. Or IL-22-driven epithelial renewal may be too slow (days) to outpace *C. parvum* replication (hours). |
| **Cheapest test** | (1) Measure ILC3 cell frequency and AhR responsiveness in neonatal calf ileal tissue (immunohistochemistry + ex vivo stimulation, ~$5K). (2) If responsive: feed I3C to neonatal calves and measure ileal IL-22 protein by ELISA (~$8K). |
| **Cargill fit** | VERY HIGH — I3C is a natural dietary compound. Feed-additive formulation. Zero novel chemistry. |

---

### D2. Lipid Raft Disruption — Methyl-Beta-Cyclodextrin or Dietary Phytosterols

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED / NOVEL. *C. parvum* sporozoites cluster host lipid rafts (cholesterol-rich membrane domains) at invasion sites to facilitate parasitophorous vacuole formation. Disrupting lipid raft integrity reduces invasion. Methyl-beta-cyclodextrin depletes cholesterol from membranes; dietary phytosterols (plant sterols) compete with cholesterol for membrane incorporation. |
| **Disease stage** | Stage 2 (Invasion — disrupts host membrane organization required for parasite entry) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [MODERATE] — Nelson et al. (2006, Eukaryotic Cell) demonstrated MbCD blocks invasion in vitro. Harrison et al. (2008) with calf enterocyte cultures. [INFERRED] for dietary phytosterol approach. |
| **Biological rationale** | If lipid raft composition in neonatal enterocytes (which are processing milk-derived cholesterol) influences invasion efficiency, dietary manipulation of membrane lipid composition could reduce susceptibility. Calves on milk replacer vs whole milk may have different enterocyte membrane compositions. |
| **Intervention** | Dietary supplementation with phytosterols (sitosterol, campesterol) in milk replacer to alter enterocyte membrane cholesterol content and disrupt lipid raft formation at invasion sites. |
| **Closest analogy** | Phytosterol-mediated membrane disruption reduces *Plasmodium* erythrocyte invasion in vitro (shared apicomplexan biology). |
| **Most likely failure mode** | (a) Dietary phytosterols may not reach ileal enterocyte membranes in sufficient concentrations. (b) Cholesterol depletion in neonatal enterocyte membranes may impair normal gut development. (c) The invasion process may be too rapid (minutes) for a modest membrane composition change to block. |
| **Cheapest test** | (1) In vitro: treat bovine enteroids with physiologically achievable phytosterol concentrations and measure *C. parvum* invasion rate. (~$5K). |
| **Cargill fit** | VERY HIGH — phytosterols are existing Cargill nutrition products. Feed-additive delivery in milk replacer. |

---

### D3. Gut-Restricted Glutathione Depletion — N-Acetylcysteine Withholding + BSO

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED / NOVEL. Building on the FDFT1/squalene/glutathione discovery (Cell, 2025): *C. parvum* cannot synthesize glutathione and is entirely dependent on importing reduced GSH from host enterocytes. Rather than inhibiting squalene synthase (lapaquistat — hepatotoxic), directly deplete reduced glutathione in the microenvironment of infected enterocytes. Buthionine sulfoximine (BSO) inhibits gamma-glutamylcysteine synthetase, the rate-limiting enzyme in GSH synthesis. A gut-restricted BSO formulation could starve the parasite of its essential redox buffer. |
| **Disease stage** | Stage 3 (Intracellular Development — metabolic starvation) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [INFERRED] — based on the CRISPR screen discovery that GSH import is essential. BSO is a well-characterized GSH synthesis inhibitor. Not tested against Crypto. |
| **Biological rationale** | The parasite has lost GSH synthesis capacity — this is an absolute metabolic dependency with no bypass pathway (unlike IMPDH, which was bypassed by nucleotide import). Disrupting GSH supply is predicted to cause oxidative stress and death in the parasite. |
| **Intervention** | Enteric-coated BSO formulated for ileal release. Must be gut-restricted to avoid systemic GSH depletion (which would harm liver, immune cells, etc.). |
| **Closest analogy** | BSO enhances chemotherapy efficacy in cancer by depleting tumor GSH — the same principle of exploiting metabolic dependency. |
| **Most likely failure mode** | (a) Gut-restricted BSO may deplete GSH in uninfected enterocytes, causing oxidative damage and worsening pathology. (b) Host cells have rapid GSH regeneration — may need sustained high-level inhibition. (c) Enterocyte GSH depletion may impair barrier function. |
| **Cheapest test** | (1) In vitro: treat *C. parvum*-infected enteroid monolayers with BSO. Measure parasite growth, host cell viability, and GSH levels simultaneously. Determine therapeutic window (parasite killing without enterocyte death). (~$8K). |
| **Cargill fit** | LOW — requires pharmaceutical formulation development. |

**Honest assessment:** The therapeutic window between "enough GSH depletion to kill the parasite" and "too much GSH depletion that damages enterocytes" may not exist. The parasite is INSIDE the host cell, sharing its redox environment. This is the fundamental challenge of all host-directed metabolic approaches.

---

### D4. Mucoadhesive Nanoparticle Drug Delivery for Ileal Targeting

| Field | Detail |
|---|---|
| **Target/mechanism** | DELIVERY PLATFORM. The rate-limiting barrier for many drug candidates is insufficient concentration at the infected ileal epithelial surface. Mucoadhesive nanoparticles (chitosan-based, thiolated polymers, or lectin-functionalized particles) can adhere to the intestinal mucus layer, concentrate drug at the epithelial surface, and release payload over hours rather than the minutes of transit in a diarrheic gut. |
| **Disease stage** | Stage 3 (Intracellular Development — improves drug delivery to infection site) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [INFERRED] for crypto. [ESTABLISHED] for mucoadhesive nanoparticle drug delivery in other intestinal applications. |
| **Biological rationale** | Crypto-induced diarrhea accelerates intestinal transit, reducing drug contact time with infected epithelium. Mucoadhesive particles resist washout and maintain drug concentration at the mucosal surface. Chitosan nanoparticles are biocompatible, GRAS, and can encapsulate both hydrophilic (paromomycin) and hydrophobic (PI4K inhibitors) compounds. |
| **Intervention** | Encapsulate the most promising drug candidate (EDI048 or AN7973) in chitosan-coated PLGA nanoparticles with ileal-release coating (pH-sensitive, releasing at pH 7.0-7.4 of distal small intestine). |
| **Closest analogy** | Mucoadhesive nanoparticle delivery of amphotericin B for intestinal leishmaniasis (another intracellular parasite at a mucosal surface). |
| **Most likely failure mode** | (a) Crypto-induced mucus depletion (documented in colonic infection) may reduce mucoadhesive particle retention. (b) Diarrheal fluid volumes may still overwhelm nanoparticle capacity. (c) Manufacturing complexity and COGS. |
| **Cheapest test** | (1) Formulate paromomycin in chitosan nanoparticles. (2) Test in bovine enteroid model: does nanoparticle delivery increase efficacy vs free drug? (~$15K). |
| **Cargill fit** | LOW-MODERATE — nanoparticle formulation requires specialized capabilities, but Cargill has encapsulation technology for feed additives. |

---

### D5. Epidermal Growth Factor (EGF) Supplementation for Mucosal Repair

| Field | Detail |
|---|---|
| **Target/mechanism** | HOST-DIRECTED / REPAIR. Bovine colostrum naturally contains EGF, which promotes intestinal epithelial cell proliferation, migration, and maturation. Crypto-infected calves have massive villous atrophy and growth deficits (34 kg at 6 months — Shaw et al. 2020) that persist long after parasitological clearance. Exogenous EGF could accelerate mucosal regeneration. |
| **Disease stage** | Stage 5 (Intestinal Pathology — mucosal repair) + Stage 7 (Resolution — accelerate recovery and reduce long-term growth impact) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [MODERATE] for EGF in intestinal repair generally (extensive neonatal animal and human data). [INFERRED] for crypto-specific application. |
| **Biological rationale** | The 34 kg growth deficit at 6 months indicates prolonged mucosal damage. Standard supportive care (ORS, NSAIDs) does not address this. EGF targets the stem cell niche and proliferating crypt epithelium to accelerate villous regeneration. |
| **Intervention** | Oral recombinant bovine EGF in milk replacer during and after acute infection (days 7-30). Alternatively: EGF-enriched colostrum fraction. |
| **Closest analogy** | EGF supplementation reduces necrotizing enterocolitis in premature human infants — another neonatal intestinal injury requiring mucosal repair. |
| **Most likely failure mode** | (a) EGF degradation in the abomasum/intestinal lumen. (b) Crypto infection may damage EGF receptors on epithelial cells. (c) Cost of recombinant EGF at dairy scale. |
| **Cheapest test** | (1) Measure EGF receptor expression in crypto-infected vs uninfected neonatal calf ileum (immunohistochemistry, ~$3K). (2) If receptors intact: pilot calf trial of oral EGF during recovery phase. |
| **Cargill fit** | MODERATE — milk replacer supplementation is within Cargill's capabilities. Recombinant EGF production requires biotechnology partnership. Natural EGF from colostrum fractionation may be more accessible. |

---

### D6. Targeted Probiotic: Engineered *L. reuteri* Secreting Anti-P23 Nanobody

| Field | Detail |
|---|---|
| **Target/mechanism** | COMBINATION: Engineered probiotic + nanobody. *Lactobacillus reuteri* (a natural calf gut colonizer) engineered to constitutively secrete an anti-P23 VHH nanobody in the intestinal lumen. Provides continuous, self-renewing source of anti-sporozoite antibodies directly at the infection site, bypassing the abomasal degradation and waning problems of passive antibody approaches. |
| **Disease stage** | Stage 0 (Upstream Susceptibility — continuous colonization resistance) + Stage 2 (Invasion — continuous anti-P23 blockade) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [INFERRED] — each component exists (L. reuteri probiotics, anti-P23 VHHs) but the combination has not been built. Engineered probiotics secreting therapeutic proteins are in development for other indications. |
| **Biological rationale** | Anti-P23 IgY works but wanes. An engineered probiotic that colonizes the calf gut and continuously produces anti-P23 VHH would provide sustained protection throughout the vulnerability window. L. reuteri DSM 17938 has been tested in combination with NTZ for crypto (NCT04103216). |
| **Intervention** | Oral administration of engineered *L. reuteri* secreting anti-P23 VHH at birth. Single dose colonizes gut and provides continuous antibody production. |
| **Closest analogy** | Engineered *L. lactis* secreting anti-TNF nanobodies for IBD (ActoBio Therapeutics — Phase 2 human clinical trials). Proven that engineered lactic acid bacteria can secrete functional VHHs in vivo. |
| **Most likely failure mode** | (a) Engineered L. reuteri may not colonize neonatal calf gut reliably. (b) VHH secretion levels may be insufficient. (c) Regulatory pathway for GMO probiotic in food animals is complex/impossible in some markets. (d) Even continuous anti-P23 cannot cure established infection (P23-independent intracellular stages). |
| **Cheapest test** | (1) Construct anti-P23 VHH-secreting *L. reuteri* strain in lab (~$15K). (2) Test secreted VHH functionality against sporozoites in vitro. (3) If functional: colonization trial in neonatal calves. |
| **Cargill fit** | MODERATE — Cargill has fermentation and probiotic capabilities. GMO regulatory barriers may limit market access. |

---

### D7. Enterocyte-Targeted Drug Conjugate — Ileal-Homing Small Molecule

| Field | Detail |
|---|---|
| **Target/mechanism** | DELIVERY PLATFORM. Conjugate an antiparasitic compound to bile acid (which is actively reabsorbed in the ileum via ASBT — the apical sodium-dependent bile acid transporter). The bile acid moiety targets the conjugate specifically to ileal enterocytes (the primary site of *C. parvum* infection). Once inside the enterocyte, the drug is released to act on the epicellular parasite at the apical surface. |
| **Disease stage** | Stage 3 (Intracellular Development — precision delivery to infection site) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [INFERRED] — bile acid drug conjugates used in other intestinal diseases. ASBT-mediated ileal targeting established. Not tested for crypto. |
| **Biological rationale** | ASBT is highly expressed in ileal enterocytes — the same cells *C. parvum* infects. A bile acid-drug conjugate would be preferentially taken up by the infected cell population. This addresses the drug dilution problem (drug is concentrated at the infection site rather than distributed across the entire GI tract). |
| **Intervention** | Conjugate EDI048 or AN7973 to a bile acid (e.g., chenodeoxycholic acid) via a cleavable linker. |
| **Most likely failure mode** | (a) ASBT expression may be downregulated in crypto-damaged ileal epithelium (the very cells you need to target are damaged). (b) Drug release from conjugate may be too slow. (c) Bile acid conjugation may inactivate the drug. |
| **Cheapest test** | (1) Measure ASBT expression in crypto-infected vs healthy neonatal calf ileum (IHC, ~$3K). (2) If ASBT persists in infected cells: synthesize bile acid-paromomycin conjugate as proof of concept (~$10K). |
| **Cargill fit** | LOW — requires medicinal chemistry and conjugation expertise. |

---

### D8. Dietary Lactose Reduction During Acute Infection

| Field | Detail |
|---|---|
| **Target/mechanism** | MANAGEMENT / NUTRITIONAL. Crypto destroys mature villous enterocytes that express lactase. Undigested lactose reaching the colon is fermented, producing osmotic diarrhea that compounds the secretory component. Temporarily reducing lactose intake during acute infection (partial substitution with lactose-free formula or glucose-polymer-based supplement) could reduce the osmotic component of diarrhea. |
| **Disease stage** | Stage 5 (Intestinal Pathology — reduces osmotic diarrhea component) + Stage 7 (Resolution — supports nutritional recovery) |
| **Category** | D — Novel proposal |
| **Evidence tier** | [INFERRED] for crypto-specific application. [ESTABLISHED] for secondary lactase deficiency in neonatal enteric infections generally. |
| **Intervention** | Partial lactose-reduced milk replacer formulation for calves with confirmed cryptosporidiosis. 50% reduction in lactose content, substituted with glucose polymers. |
| **Most likely failure mode** | (a) Lactose-reduced feeding may reduce total caloric intake, worsening growth. (b) The malabsorptive and secretory components may dominate over osmotic, making lactose reduction marginal. (c) Practical farm implementation challenges. |
| **Cheapest test** | Controlled trial: standard milk replacer vs lactose-reduced formulation in crypto-positive calves. Endpoints: fecal output, hydration, weight gain at 14 and 30 days. (~$8K). |
| **Cargill fit** | VERY HIGH — milk replacer formulation is core Cargill capability. Can be implemented immediately in existing product lines. |

---

### D9. Combination Protocol: Antiparasitic + Anti-Secretory + Immune Support + Nutritional

| Field | Detail |
|---|---|
| **Target/mechanism** | MULTI-MODAL / NOVEL. No single agent satisfies all 14 Sapper constraints. Propose a PROTOCOL rather than a single product: (1) Direct-kill antiparasitic (EDI048 or AN7973 — best available) targeting Stage 3. (2) Anti-reinvasion agent (IgY or VHH) targeting Stage 2/autoinfection. (3) Anti-secretory adjunct (crofelemer or ondansetron) targeting Stage 5. (4) Innate immune support (beta-glucan or NOD2 agonist) targeting Stage 4. (5) Nutritional support (glutamine-enhanced ORS, lactose-reduced milk replacer, EGF) targeting Stage 5/7. |
| **Disease stage** | ALL STAGES — comprehensive multi-stage protocol |
| **Category** | D — Novel proposal |
| **Evidence tier** | [INFERRED] — each component has individual evidence. Combination protocol untested. |
| **Biological rationale** | The disease map identifies 8 stages and every one has a gap. The constraint set requires simultaneous satisfaction of 14 criteria. No single compound can do this. A protocol that combines mechanism-complementary interventions across stages may achieve what monotherapy cannot. |
| **Key risk** | Complexity. Multiple products = multiple regulatory pathways. Drug-drug interactions. Farm compliance with multi-product protocol. Cost. |
| **Proposed de-risk** | (1) Develop a simplified 3-component protocol: (a) best antiparasitic + (b) IgY/VHH + (c) optimized ORS. Test as bundle. (2) If 3-component bundle shows >70% improvement over ORS alone: iterate with additional components. |
| **Cargill fit** | MODERATE-HIGH — Cargill could bundle multiple oral products (antiparasitic license + proprietary IgY + optimized ORS/feed additive) as a "crypto management system." The protocol approach aligns with Cargill's nutritional consulting and management advisory role with dairy operations. |

---

## Coverage Map by Disease Stage

| Disease Stage | Candidates | Count | Coverage Assessment |
|---|---|---|---|
| **Stage 0: Upstream Susceptibility** | A5 (hyperimmune colostrum), B7 (Bovilis enhancement), B12 (colostrum supplement), C3 (beta-glucan trained immunity), C9 (microbiome engineering), D1 (IL-22 inducer), D6 (engineered probiotic) | 7 | COVERED — multiple approaches to bridge neonatal immune gap. But none individually sufficient. |
| **Stage 1: Exposure/Ingestion** | C11 (oocyst wall inhibitors — reduces environmental load over time) | 1 | MINIMALLY COVERED. Management interventions are necessary but not drug targets. Oocyst wall targeting is the only pharmacological option and it operates at herd level, not individual. |
| **Stage 2: Invasion** | A4 (BKI-1708), A5 (hyperimmune colostrum), A6 (anti-P23 IgY), B7 (Bovilis), B9 (Gal-GalNAc), C8 (nanobodies), D2 (lipid raft disruption), D6 (engineered probiotic) | 8 | WELL COVERED — but all are anti-reinvasion adjuncts, none curative alone. Best value as combination partners with Stage 3 drugs. |
| **Stage 3: Intracellular Development** | A1 (EDI048), A2 (AN7973), A3 (MMV665917), A7 (halofuginone), B1 (BRD7929/PheRS), B2 (DDD01510706/KRS), B3 (LDH+PK), B4 (HDAC3), B5 (PDE1), B6 (lapaquistat/GSH), B8 (aminoglycoside derivative), B14 (NTZ reformulation), B15 (EDI048+AN7973 combo), D3 (BSO/GSH depletion), D4 (nanoparticle delivery), D7 (bile acid conjugate) | 16 | HEAVILY COVERED — this is where the most validated targets exist. EDI048 and AN7973 lead. |
| **Stage 4: Host Immune Response** | C1 (NOD2/MDP), C2 (IFN-lambda), C3 (beta-glucan), D1 (IL-22 inducer) | 4 | COVERED — first time this stage has pharmacological candidates. NOD2/MDP and IL-22 approaches are most promising. |
| **Stage 5: Intestinal Pathology** | B10 (racecadotril), B11 (crofelemer), B13 (glycine/glutamine ORS), C4 (ondansetron), C6 (cholestyramine), D5 (EGF), D8 (lactose reduction) | 7 | WELL COVERED — multiple anti-secretory and repair approaches. None curative, all adjunctive. |
| **Stage 6: Shedding/Transmission** | A1 (EDI048 — oocyst reduction), A2 (AN7973), C11 (oocyst wall inhibitors) | 3 | PARTIALLY COVERED — best addressed indirectly by Stage 3 drugs that reduce parasite burden. Direct transmission targets limited. |
| **Stage 7: Resolution/Chronicity** | D5 (EGF for mucosal repair), D8 (lactose reduction), B13 (glutamine ORS) | 3 | MINIMALLY COVERED — the 34 kg growth deficit is a major unmet need. EGF supplementation is the most specific candidate. |

**TOTAL COVERAGE: All 8 stages have at least one candidate. Stage 3 is the most heavily addressed. Stages 1 and 7 have the fewest candidates and remain the weakest.**

---

## Cargill Fit Assessment

### Tier 1: Directly Within Cargill Capabilities (oral, feed-additive, nutritional)

| Candidate | Product Format | Cargill Capability Match |
|---|---|---|
| C3 — Beta-glucan trained immunity | Yeast cell wall feed additive | Existing product — reformulate with crypto indication data |
| B12 — Colostrum supplementation | Colostrum-based supplement | Existing capability — standardization opportunity |
| A6 — Anti-P23 IgY | Spray-dried egg yolk antibody supplement | Feed additive manufacturing, oral delivery |
| B13 — Glutamine/glycine ORS | Enhanced oral rehydration | Nutritional formulation |
| D8 — Lactose-reduced milk replacer | Modified milk replacer | Core milk replacer manufacturing |
| D1 — IL-22 inducer (I3C) | Dietary supplement (indole-3-carbinol) | Natural compound, feed additive |
| D2 — Phytosterols | Dietary supplement in milk replacer | Existing nutrition products |
| B9 — Gal-GalNAc blockade | Oligosaccharide feed additive | If biologically feasible |
| C4 — Ondansetron | Oral anti-secretory (off-label) | Distribution, not manufacturing |

### Tier 2: Possible With Partnership (requires pharma or biotech collaboration)

| Candidate | Required Partner | Cargill Role |
|---|---|---|
| A1 — EDI048 | Novartis (license veterinary rights) | Formulation, distribution |
| A2 — AN7973 | MMV/DNDi or pharma licensee | Formulation, distribution |
| A5 — Hyperimmune colostrum | Dam immunization protocol developer | Colostrum processing, distribution |
| C8 — Nanobodies | VHH discovery lab | Production (yeast fermentation), oral formulation |
| D6 — Engineered probiotic | Synthetic biology company | Fermentation, distribution |

### Tier 3: Pharma-Led (Cargill not well-positioned)

B1, B2, B3, B4, B5, B6, B8, B14, B15, D3, D4, D7, C5, C7, C10, A3, A4

---

## Constraint Compliance Summary

| Constraint (from Sapper) | Best-Compliant Candidates |
|---|---|
| 1. Parasiticidal (not static) | A2 (AN7973 — cidal), B1 (BRD7929 — cidal in mice) |
| 2. Immunity-independent | A1 (EDI048), A2 (AN7973), B1 (BRD7929) — all work in immunosuppressed mice |
| 3. Luminal/apical access | A1 (EDI048 — gut-restricted by design), B11 (crofelemer — luminal) |
| 4. Multi-stage coverage | A2 (AN7973 — asexual + sexual), B15 (combination) |
| 5. High resistance barrier | B3 (LDH+PK dual target), B6 (host-directed/lapaquistat), B15 (combination), D3 (host GSH) |
| 6. Outlasts autoinfection | A1 (EDI048 — no recrudescence at 7 days), B15 (combination) |
| 7. Gut-restricted | A1 (EDI048 — engineered), B11 (crofelemer), C4 (ondansetron) |
| 8. Neonatal safe | A1 (EDI048 — 70-fold margin), A2 (AN7973 — no adverse effects), A6 (IgY — food-based) |
| 9. Therapeutic (post-onset) | A3 (MMV665917 — started after severe diarrhea), A1 (EDI048), A2 (AN7973) |
| 10. Survives abomasal pH | A6 (IgY — detected in feces), D4 (enteric-coated nanoparticles) |
| 11. Oral/feed additive | ALL Category A and most others |
| 12. Affordable (<$20-30/calf) | A6 (IgY — egg-based production), C3 (beta-glucan — existing product), B12 (colostrum — existing) |
| 13. Viable regulatory path | A7 (halofuginone — already approved EU), B12 (colostrum — supplement), C3 (beta-glucan — GRAS feed additive) |
| 14. ORS-compatible | Most oral candidates — needs specific testing for each |

**No single candidate satisfies ALL 14 constraints. The combination approach (D9) is the only strategy that can simultaneously address all constraints.**

---

## Priority Ranking for Surveyor

### Highest Priority (validate or kill first)

1. **A1 — EDI048 (CpPI4K)** — Most advanced, gut-restricted, calf-validated. Key question: cidal or static?
2. **A2 — AN7973 (CPSF3)** — Cidal, multi-stage, calf-validated. Key question: resistance barrier?
3. **A3 — MMV665917** — Therapeutic efficacy in calves. Key question: what is the target?
4. **C1 — NOD2/MDP (IL-22 pathway)** — Novel innate immune approach, neonatal mice data. Key question: translates to calves?
5. **B6 — Lapaquistat (host squalene/GSH)** — Novel host-directed, high resistance barrier. Key question: neonatal safety?

### High Priority (Cargill-aligned, rapid deployment potential)

6. **C3 — Beta-glucan trained immunity** — Existing Cargill product, needs crypto-specific efficacy data
7. **A6 — Anti-P23 IgY** — Cargill-manufacturable, calf data, needs replication
8. **D1 — IL-22 inducer (I3C/AhR agonist)** — Natural compound, feed-additive, needs mechanistic validation
9. **B12 — Colostrum supplementation** — Standard-of-care optimization, minimal risk

### Medium Priority (combination partners)

10. **B11 — Crofelemer** — Best anti-secretory candidate (luminal action)
11. **A4 — BKI-1708** — Combination partner for anti-reinvasion
12. **B3 — LDH+PK dual inhibition** — High resistance barrier, needs calf data
13. **B5 — CpPDE1 inhibitors** — New target, validated, needs calf data
14. **D5 — EGF for mucosal repair** — Addresses 34 kg growth deficit gap

### Lower Priority (longer development timeline or higher risk)

15-42. Remaining candidates in order of evidence strength and constraint compliance.

---

## Summary for Overwatch

**What I proposed:** 42 mechanism-level candidates across all 8 disease stages.

**What I believe the core portfolio should center on:**
1. **Direct antiparasitic backbone:** EDI048 or AN7973 (or combination) — the only candidates that can satisfy the critical constraints of cidal + immunity-independent + luminal delivery
2. **Innate immune acceleration:** NOD2/MDP pathway or IL-22/AhR induction — the first approaches that could bridge the neonatal immune gap via INNATE (not adaptive) immunity
3. **Anti-reinvasion adjunct:** Anti-P23 IgY or nanobodies — continuous blockade of the autoinfection cycle
4. **Nutritional/supportive platform:** Beta-glucan + optimized ORS + lactose management — Cargill's core capability, deployable immediately

**What I am NOT confident about:**
- Whether EDI048 is cidal or static (this determines whether it can cure or only suppress)
- Whether AN7973's resistance barrier is acceptable for monotherapy
- Whether NOD2/IL-22 innate immune activation translates from neonatal mice to neonatal calves
- Whether any host-directed approach has an acceptable therapeutic window in neonatal enterocytes

**What the 70% test requires:**
Stage 3 (intracellular development) is the rate-limiting stage, responsible for >50% of pathology. A cidal antiparasitic that works in neonates is REQUIRED for the portfolio to pass. Adjuncts alone — even excellent ones — cannot reach 70% without solving Stage 3. EDI048 or AN7973 (or their combination) is the indispensable backbone.

---

*Forge v1.0 — Cryptosporidiosis in Neonatal Calves*
*42 mechanism-level candidates across 8 disease stages, 4 categories.*
*All claims evidence-tiered per Quality Standard 1.*
*Ready for Surveyor (Phase 3b: Computational Validation).*
