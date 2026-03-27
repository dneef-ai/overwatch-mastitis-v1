# Phase 1 — Disease Map: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill | **Version:** v2
**Agent:** Pathfinder | **Date:** 2026-03-27

---

## Executive Summary

Cryptosporidiosis in neonatal calves is caused primarily by *Cryptosporidium parvum*, an obligate intracellular apicomplexan parasite that occupies a unique **intracellular-but-extracytoplasmic** niche in the intestinal epithelium. It is the leading cause of neonatal calf diarrhea worldwide, with prevalence of 20-50% in preweaned calves and near-universal herd exposure. There is **no effective cure**, no approved treatment in the US, and only one partially effective drug (halofuginone/Halocur) approved in the EU. The disease is self-limiting in immunocompetent animals (resolves in 1-2 weeks) but causes severe watery diarrhea, dehydration, weight loss, and can be fatal. Critically, weight lost during infection is **not regained** in the six months following — the long-term economic damage exceeds the acute clinical costs.

The fundamental barrier to solving this disease is the **unique parasitophorous vacuole niche** — C. parvum sits inside the host cell membrane but outside the cytoplasm, protected from both extracellular immune clearance and intracellular drug delivery. This niche, combined with the extremely low infectious dose (ID50 ~ 5-17 oocysts), massive oocyst amplification (10^6-10^7 per gram feces), environmental persistence (months in soil/water, resistant to chlorine), and thin-walled oocyst autoinfection cycle, creates a disease that is extraordinarily difficult to control with conventional pharmacological approaches.

**R0 estimate: 3-8 in managed calf operations** [INFERRED] — this is NOT a disease near the tipping point. Small prevention effects will not collapse prevalence. Effective control requires either dramatic reduction in environmental contamination, effective prophylaxis during the 1-3 week vulnerability window, or direct anti-parasitic intervention.

---

## Stage 1: Entry and Exposure

### 1.1 Infectious Dose and Dose-Response

**The infectious dose is extraordinarily low.**

Based on articles retrieved from PubMed, Zambriski et al. (2013) experimentally challenged 27 dairy calves within 24h of birth with doses ranging from 25 to 10^6 oocysts ([DOI](https://doi.org/10.1016/j.vetpar.2013.04.022)):
- **All 27 test calves developed diarrhea** regardless of dose
- ID50 for fecal oocyst shedding: **5.8 oocysts**
- ID50 for diarrhea: **9.7 oocysts**
- ID50 for oocyst shedding with diarrhea: **16.6 oocysts**
- Inverse relationship between dose and time to onset of shedding (P=0.005)
- No relationship between dose and duration or peak shedding intensity
- **Implication:** Even minimal environmental contamination is sufficient to infect every exposed calf

**Evidence tier:** [ESTABLISHED] — multiple experimental infection studies confirm extremely low infectious dose in neonatal calves.

### 1.2 Transmission Route

Fecal-oral is the dominant route. Oocysts are fully sporulated and immediately infectious when shed.

**Sources of oocyst exposure to neonatal calves:**
- **Contaminated calving environment** — oocysts persist for months in bedding, pens, soil [ESTABLISHED]
- **Other infected calves** — a single infected calf can shed 10^6-10^7 oocysts per gram of feces for 6-13 days (Fayer et al., 1998; [DOI](https://doi.org/10.1016/s0020-7519(97)00170-7)) [ESTABLISHED]
- **Adult cattle** — the role of periparturient cows as direct sources is **disputed**. Studies using sensitive detection found that adult cattle shed multiple distinct genotypes, while calves within a herd converge on a predominant genotype, suggesting **calf-to-calf** transmission is the dominant amplification route rather than dam-to-calf [MODERATE]
- **Contaminated water/feed** — oocysts in water sources persist and resist chlorination [ESTABLISHED]
- **Fomites** — boots, equipment, bedding from contaminated environments [MODERATE]

### 1.3 Environmental Persistence of Oocysts

Oocysts are **extraordinarily resistant** to environmental degradation and standard disinfection:

- Survive **months** in moist environments at 4-20degC [ESTABLISHED]
- **Resistant to standard chlorination** — free chlorine at 5 mg/L for 300 min achieves only ~0.6-0.8 log reduction (Coleman et al., 2023; [DOI](https://doi.org/10.1021/acs.est.3c00536)) [ESTABLISHED]
- Resistant to most commercial disinfectants including quaternary ammonium compounds [ESTABLISHED]
- Only reliably inactivated by **heat** (>65degC), **UV irradiation**, **ozone**, **ammonia** (at high concentration), or specific cresol-based products (p-chloro-m-cresol at 3% showed efficacy in combination with halofuginone; Keidel & Daugschies, 2013; [DOI](https://doi.org/10.1016/j.vetpar.2013.03.003)) [ESTABLISHED]
- **Desiccation** is effective — oocysts are vulnerable to drying [MODERATE]
- Triple oocyst wall (outer glycocalyx, middle rigid layer, inner lipid layer) provides mechanical and chemical resistance [ESTABLISHED]

### 1.4 What Is Unknown

- Precise quantification of environmental oocyst load required to sustain transmission in a typical calf-rearing facility
- Contribution of wildlife reservoirs (rodents, birds) to farm contamination
- Relative contribution of dam shedding vs. environmental carryover between calving seasons

---

## Stage 2: Excystation and Invasion

### 2.1 Excystation

Upon ingestion, oocysts excyst in the gastrointestinal tract in response to:
- **Temperature shift** (body temperature ~38.5degC) [ESTABLISHED]
- **Bile salts** and **CO2** [ESTABLISHED]
- **pH changes** — sequential exposure to acidic then alkaline/neutral conditions mimics gastric-to-intestinal transit [ESTABLISHED]
- **Trypsin and other pancreatic enzymes** facilitate the process [MODERATE]

Each oocyst releases **4 sporozoites**, which are the invasive form. [ESTABLISHED]

### 2.2 Sporozoite Attachment and Invasion

Attachment and invasion of intestinal epithelial cells is a multi-step process involving specific parasite ligands and host receptors.

**Parasite invasion proteins:**

| Protein | Location | Function | Evidence |
|---------|----------|----------|----------|
| **CSL** (~1,300 kDa glycoprotein) | Apical complex micronemes + dense granules + surface | Sporozoite lectin; contains ligand for intestinal epithelial cells; translocated posteriorly along pellicle via cytoskeleton-dependent process | [ESTABLISHED] — Riggs lab, multiple studies |
| **GP900** (mucin-like glycoprotein) | Micronemes + surface | Initially thought adhesive; now evidence suggests primarily a **lubrication** role; cleaved in secretory pathway | [MODERATE] — revised understanding |
| **GP40/GP15** (proteolytically cleaved from GP60 precursor) | Surface | Major surface antigen; GP40 mediates attachment; anti-GP40 antibodies neutralize infection in vitro; GP15 anchored to membrane via GPI anchor | [ESTABLISHED] — key vaccine target |
| **TRAP-C1** (thrombospondin-related adhesive protein) | Apical complex | Essential for gliding motility and host cell attachment; ~76 kDa; contains peptide motifs binding sulfated glycoconjugates | [MODERATE] |
| **CpGP40 (Cpgp40)** | Surface | Interacts with host ENO1 (alpha-enolase) on cell surface; functional role in invasion confirmed by antibody neutralization and siRNA knockdown (2024 study) | [PRELIMINARY] — single lab, 2024 |
| **P23** | Surface + parasitophorous vacuole | Surface antigen targeted by neutralizing antibodies | [MODERATE] |

**Host cell receptors and factors:**
- **Gal/GalNAc epitopes** on enterocyte surface — sporozoite lectins bind these sugar moieties [ESTABLISHED]
- **ENO1 (alpha-enolase)** — host cell surface protein interacting with CpGP40; involved in cytoskeletal regulation during invasion [PRELIMINARY]
- **CD46/CD59** — GPI-anchored host proteins may serve as attachment points [INFERRED]
- Host **PI3-kinase** activation is required for invasion — cytoskeletal remodeling drives membrane protrusion around the invading sporozoite [MODERATE]
- Host **actin** accumulates at the host-parasite interface during invasion [ESTABLISHED]

**Invasion mechanism model:**
1. Sporozoite glides along intestinal epithelium via TRAP-C1 mediated motility
2. Initial attachment via lectin-Gal/GalNAc interactions with glycocalyx
3. Specific attachment via CSL and GP40/GP15 to enterocyte membrane receptors
4. Sporozoite triggers host cell actin polymerization and membrane protrusion
5. Host cell membrane envelops the parasite, forming the **parasitophorous vacuole**
6. Parasite settles into its unique **intracellular-but-extracytoplasmic** niche

**Primary target tissue:** Ileum (posterior small intestine), with extension to jejunum and, in heavy infections, cecum and colon. [ESTABLISHED]

### 2.3 What Is Unknown

- Complete molecular details of the receptor-ligand interactions mediating invasion
- Whether there is receptor redundancy (multiple parallel invasion pathways)
- Whether specific enterocyte maturation states affect susceptibility to invasion
- Role of intestinal stem cell niches in parasite tropism

---

## Stage 3: The Intracellular-Extracytoplasmic Niche

### 3.1 The Parasitophorous Vacuole — A Unique Niche

This is the **single most important biological feature** of C. parvum for drug development. Unlike all other apicomplexan parasites (Toxoplasma, Plasmodium, Eimeria), which reside fully within the host cytoplasm, C. parvum occupies a position that is:

- **Intracellular** — enclosed within the host cell membrane [ESTABLISHED]
- **Extracytoplasmic** — NOT immersed in host cytoplasm [ESTABLISHED]
- The parasitophorous vacuole membrane (PVM) extends over the **apical** (luminal-facing) domain of the parasite only [ESTABLISHED]
- The **basal** domain contacts the host cell through a fused parasite-host membrane called the **feeder organelle membrane** [ESTABLISHED]

**Structural detail of the niche:**
- The PVM is derived from the host cell membrane during invasion [ESTABLISHED]
- A highly invaginated membrane structure — the **feeder organelle** — forms between the parasite and host cytoplasm [ESTABLISHED]
- The feeder organelle is composed of stacked flat bursiform, ring-shaped, and reticulated tubular membranes that increase surface area for nutrient transport [MODERATE]
- An electron-dense band separates the parasite from the host cytoplasm [ESTABLISHED]
- The parasite exports proteins into the host cytosol through this interface, modifying host cell function [PRELIMINARY — 2021 eLife study]

### 3.2 The Feeder Organelle — Nutrient Acquisition

C. parvum has a **radically reduced genome** (~3.6 Mb, ~3,800 genes) and has lost most metabolic pathways:
- No mitochondrial genome, no TCA cycle, no functional electron transport chain [ESTABLISHED]
- No de novo synthesis of amino acids, nucleotides, or fatty acids [ESTABLISHED]
- Relies entirely on salvage pathways and import from host [ESTABLISHED]

**Nutrient transport through the feeder organelle:**
- **CpABC1** (ATP-binding cassette transporter) — localizes to the feeder organelle; likely mediates selective transport between host and parasite [MODERATE]
- **CpGT1 and CpGT2** (glucose transporters) — localize to the feeder organelle; can directly transport glucose phosphate from host cell [MODERATE]
- **CpIMPDH** (inosine monophosphate dehydrogenase) — acquired via lateral gene transfer from epsilon-proteobacterium; essential for guanine nucleotide synthesis from salvaged adenosine [ESTABLISHED]
- **CpLDH** (lactate dehydrogenase) — associated with the PVM; potential drug target [MODERATE]

### 3.3 Functional Consequences of the Niche

This unique niche has profound implications:

1. **Immune evasion:** Parasite antigens have limited direct exposure to immune cells; protected from phagocytosis; not targeted by guanylate-binding proteins [ESTABLISHED]
2. **Drug delivery challenge:** Many intracellular-acting drugs (e.g., those requiring cytoplasmic accumulation) cannot reach the parasite because it is NOT in the cytoplasm [ESTABLISHED]
3. **Paromomycin paradox:** Paromomycin and geneticin can inhibit C. parvum growth WITHOUT trafficking through the host cell cytoplasm — they can reach the parasite from the luminal side through the PVM [MODERATE]
4. **Vulnerability:** The parasite IS accessible from the intestinal lumen — oral/luminal-acting drugs can potentially reach it without requiring intracellular delivery [MODERATE]

### 3.4 What Is Unknown

- Complete molecular composition of the feeder organelle membrane
- Full set of transported nutrients and their specific transporters
- Whether the feeder organelle is a viable drug target (disrupting nutrient acquisition)
- Detailed mechanism of protein export from parasite to host cytosol
- Whether Cryptosporidium uses multiple distinct secretory organelles (2023 Cell Host & Microbe study suggests yes, including a novel secretory organelle)

---

## Stage 4: Intracellular Development (Merogony)

### 4.1 Asexual Reproduction — Type I Meronts

After invasion, the sporozoite develops into a **trophozoite**, then into a **Type I meront** (also called schizont):

- Each Type I meront produces **8 merozoites** [ESTABLISHED]
- Merozoites rupture from the host cell and invade adjacent enterocytes [ESTABLISHED]
- Type I merozoites can form **another Type I meront**, creating an exponential amplification cycle [ESTABLISHED]
- This amplification cycle drives the massive parasite burden seen in acute infection [ESTABLISHED]
- Each merozoite can infect a new cell within minutes, and a full asexual cycle completes in ~12-14 hours [MODERATE]

### 4.2 Type II Meronts (Revised Understanding)

The traditional view was:
- Type I merozoites eventually form **Type II meronts** containing **4 merozoites** [TRADITIONAL VIEW]
- Type II merozoites do not recycle but proceed to sexual development [TRADITIONAL VIEW]

**However, live imaging studies have revised this** (Striepen lab, 2022; PMC9015140):
- No morphologically distinct Type II meront intermediate stage was observed [PRELIMINARY]
- Male and female gametes develop **directly from Type I meronts** (8N stage) [PRELIMINARY]
- This challenges the traditional two-meront model and suggests the life cycle may be simpler than previously thought

**Evidence tier for revised model:** [PRELIMINARY] — single lab, live imaging in cell culture. The traditional model remains the textbook description.

### 4.3 Amplification Dynamics

The key clinical consequence: from a single ingested oocyst (4 sporozoites), the parasite can amplify to **billions** of parasites through:
1. Each sporozoite invades a cell and produces 8 merozoites (8x amplification per cycle)
2. Each merozoite can reinitiate the cycle (8x per cycle, ~12-14h per cycle)
3. After 3 cycles: 4 x 8^3 = 2,048 parasites from 1 oocyst
4. After 5 cycles: 4 x 8^5 = 131,072 parasites from 1 oocyst

This exponential amplification, combined with autoinfection (see Stage 5), explains how infection from <20 oocysts produces shedding of 10^6-10^7 oocysts per gram of feces.

### 4.4 What Is Unknown

- What signals determine whether a Type I merozoite recycles (more Type I meronts) vs. commits to sexual development?
- Is this decision stochastic or density-dependent?
- Is the revised life cycle model (direct gamete formation from Type I meronts) correct, or an artifact of in vitro conditions?
- Can the merogony cycle be specifically disrupted without host toxicity?

---

## Stage 5: Sexual Reproduction and Oocyst Formation

### 5.1 Gametogony

After several rounds of asexual amplification, parasites commit to sexual development:

- **Macrogamonts** (female) — develop from merozoites; enlarge and accumulate wall-forming bodies [ESTABLISHED]
- **Microgamonts** (male) — produce **16 non-flagellated microgametes** that are released to fertilize macrogamonts [ESTABLISHED]
- Fertilization produces a **zygote** that develops into an oocyst [ESTABLISHED]

### 5.2 Two Types of Oocysts

This is the second critically important biological feature for understanding persistence:

| Feature | Thick-walled oocysts (~80%) | Thin-walled oocysts (~20%) |
|---------|---------------------------|--------------------------|
| Wall structure | Triple-layered, robust | Single membrane, fragile |
| Fate | Excreted in feces | Excyst **within the host** |
| Function | Environmental transmission | **Autoinfection** |
| Infectivity | Immediately infectious when shed | Immediately releases sporozoites in gut |

[ESTABLISHED] — well-documented in multiple studies

### 5.3 Autoinfection Cycle

The thin-walled oocysts drive **autoinfection** — they excyst within the intestinal lumen and release sporozoites that immediately invade new enterocytes without ever leaving the host. [ESTABLISHED]

**Consequences:**
1. **Escalation of infection intensity** without additional oocyst ingestion from the environment
2. **Self-sustaining infection** even in a clean environment — once infected, the calf continues to amplify parasites internally
3. **Therapeutic window is narrow** — by the time clinical signs appear (diarrhea at day 3-5 post-infection), autoinfection is already established
4. **Any drug must eliminate both intracellular stages AND thin-walled oocysts** to prevent rebound

### 5.4 What Is Unknown

- What determines the ratio of thick-walled to thin-walled oocysts? Is it host immune status, parasite density, or both?
- Can the autoinfection cycle be specifically disrupted?
- Is gametocyte commitment a therapeutic target (as it is in malaria)?

---

## Stage 6: Immune Response and Evasion

### 6.1 Innate Immunity

**Epithelial cell defenses:**
- **iNOS** (inducible nitric oxide synthase) — expression is upregulated in infected epithelium via NF-kappaB; NO production mediates partial enterocyte defense against parasites; selective iNOS inhibition INCREASES parasitism (Gookin et al., 2005; [DOI](https://doi.org/10.1152/ajpgi.00460.2004)) [ESTABLISHED — neonatal piglet model]
- **Prostaglandin** production — PGE2 drives secretory chloride flux (contributes to diarrhea) but does not appear to control parasitism [MODERATE]
- **Toll-like receptors** — TLR4 and TLR2 recognize parasite components; activate NF-kappaB signaling [MODERATE]
- **Antimicrobial peptides** — defensins and cathelicidins are induced but efficacy against C. parvum is unclear [PRELIMINARY]

**Neutrophil response:**
- Rapid neutrophil infiltration into infected mucosa is a hallmark [ESTABLISHED]
- Proteomic analysis shows inflammatory effectors including reactive oxygen species and myeloperoxidases drive an **ulcerative neutrophilic ileitis** pattern [MODERATE — 2023 study]
- Neutrophils may cause collateral tissue damage but their role in parasite clearance is uncertain [MODERATE]

### 6.2 Adaptive Immunity

**The critical role of IFN-gamma and CD4+ T cells:**

Based on articles retrieved from PubMed:

- Infection induces IFN-gamma production by PBMCs from day 6 post-infection onward (de Graaf & Peeters, 1997; [DOI](https://doi.org/10.1016/s0020-7519(96)00167-1)) [ESTABLISHED — bovine in vivo]
- Substantial increases in **CD4+ and CD8+ T cells** in ileal intraepithelial lymphocyte populations during acute infection (Fayer et al., 1998; [DOI](https://doi.org/10.1016/s0020-7519(97)00170-7)) [ESTABLISHED — bovine in vivo]
- CD4+ intraepithelial T cells from infected calves co-express **CD25** (activation marker) — absent in controls (Wyatt et al., 1997; [DOI](https://doi.org/10.1128/iai.65.1.185-190.1997)) [ESTABLISHED — bovine in vivo]
- IFN-gamma response is **CD4+ T-cell dependent** (de Graaf et al., 1998; [DOI](https://doi.org/10.1016/s0020-7519(98)00164-7)) [ESTABLISHED — bovine]
- RT-PCR shows increased IL-12 and IFN-gamma mRNA in ileal intraepithelial and lamina propria lymphocytes; **no changes** in IL-2, IL-4, or IL-10 — consistent with a **Th1-dominant** response [ESTABLISHED]
- **IL-15 mRNA** is DECREASED in infected calves — possible impairment of NK/T cell maintenance [PRELIMINARY]

**Antibody response:**
- Local IgA and IgM responses develop from day 6 post-infection, peak at day 10 [ESTABLISHED — bovine]
- Specific serum IgG develops but its protective role is uncertain [MODERATE]
- Passive immunization with colostral antibodies provides **partial** but not complete protection [MODERATE]

### 6.3 Why Neonates Are Particularly Susceptible

This is a critical question. Neonatal calves are overwhelmingly the most affected age group (peak infection 1-3 weeks of age). Several factors converge:

1. **Immature mucosal immune system** — neonatal calves have underdeveloped gut-associated lymphoid tissue (GALT); CD4+ T cells are naive and slow to mount antigen-specific responses [ESTABLISHED]
2. **Inadequate colostral immunity** — natural colostrum has variable and often insufficient C. parvum-specific antibodies; antibodies decline rapidly in the gut lumen [MODERATE]
3. **rBoIL-12 paradox** — recombinant bovine IL-12 stimulates strong CD4+ T cell expansion and IFN-gamma production in the gut, yet STILL fails to protect against infection (Pasquali et al., 2006; [DOI](https://doi.org/10.1016/j.vetpar.2005.05.062)) [ESTABLISHED — bovine in vivo]
4. **Parasite replication outpaces immune response** — given the extremely rapid asexual amplification (12-14h cycles) and autoinfection, the parasite establishes massive burden BEFORE adaptive immunity activates (~day 6-7) [INFERRED]
5. **Immature intestinal barrier** — neonatal enterocytes may have higher expression of receptors used for parasite attachment [INFERRED]
6. **Microbiome immaturity** — the neonatal gut microbiome is undeveloped; specific microbiome pathways (isoprenoid, haem, purine biosynthesis) may supply metabolites the parasite scavenges (2023 Animal Microbiome study) [PRELIMINARY]

### 6.4 Immune Evasion Mechanisms

1. **The extracytoplasmic niche itself** — by sitting outside the cytoplasm, C. parvum avoids:
   - MHC-I presentation of parasite antigens (requires cytoplasmic processing) [INFERRED]
   - Targeting by intracellular GTPases and guanylate-binding proteins [MODERATE]
   - Autophagy-mediated clearance (no cytoplasmic presence to target) [INFERRED]

2. **Minimal surface antigen exposure** — the luminal face of the PVM shields most parasite antigens [MODERATE]

3. **Disruption of host cell junctions** — proteomics show C. parvum infection disrupts tight junction and adherens junction proteins, potentially impairing organized immune signaling [PRELIMINARY — 2023 proteomics]

4. **Modulation of host gene expression** — RNA-seq reveals downregulation of macrophage chemotaxis markers and cytosolic pattern recognition pathways, with upregulation of specific inflammatory pathways (2024 Frontiers in Immunology) [PRELIMINARY]

5. **Speed** — the parasite completes its life cycle faster than the adaptive immune system can respond effectively; the infection is largely self-limiting because immunity eventually catches up, not because the parasite is cleared quickly [ESTABLISHED]

### 6.5 Recovery and Protective Immunity

- Infection is **self-limiting** in immunocompetent calves — resolution typically occurs by 2-3 weeks post-infection [ESTABLISHED]
- **Cleared by adaptive immunity** — athymic (nude) mice and SCID mice develop persistent, fatal infections [ESTABLISHED]
- IFN-gamma-depleted SCID mice develop persistent infection that can be partially controlled by passive monoclonal antibody therapy (Riggs et al., 2002; [DOI](https://doi.org/10.1128/AAC.46.2.275-282.2002)) [ESTABLISHED — mouse model]
- **Partial protective immunity** develops after primary infection — reduced severity on re-exposure but not sterilizing immunity [MODERATE]

### 6.6 What Is Unknown

- Exact mechanisms by which C. parvum suppresses host immune responses at the molecular level
- Whether the parasite actively modulates the ratio of Th1/Th2 response
- Why rBoIL-12 administration enhances IFN-gamma but fails to protect — is the issue drug timing, tissue penetration, or a fundamental limitation of the immune axis?
- Role of gamma-delta T cells (WC1+) in neonatal defense — these cells are prominent in bovine mucosa

---

## Stage 7: Pathology and Disease Mechanisms

### 7.1 Tissue Distribution

- **Primary site:** Ileum (distal small intestine) — most severely affected [ESTABLISHED]
- **Secondary extension:** Jejunum, and in heavy infections, cecum and colon [ESTABLISHED]
- Infection shifts caudally (from small intestine to large intestine) over the course of infection [ESTABLISHED — piglet model, Vitovec & Koudela, 1992; [DOI](https://doi.org/10.1016/0304-4017(92)90045-b)]
- Parasites found in heterotopic glandular epithelium in submucosa of cecum/colon by days 9-10 [MODERATE]

### 7.2 Histopathology

- **Villous atrophy** — shortened, blunted villi with fusion of adjacent villi [ESTABLISHED]
- **Crypt hyperplasia** — compensatory proliferation of crypt cells [ESTABLISHED]
- **Inflammatory infiltration** — neutrophils, lymphocytes, and macrophages in lamina propria [ESTABLISHED]
- **Goblet cell depletion** — mucin barrier is depleted with incompletely filled goblet cells [MODERATE — 2023 study]
- Scanning electron microscopy shows infected absorptive cells have thicker and longer microvilli; neighboring non-infected cells become hypertrophic with minute microvilli [MODERATE — piglet model]

**Impact on intestinal stem cells:**
- C. parvum infection INHIBITS enteroid propagation ex vivo (Zhang et al., 2016; [DOI](https://doi.org/10.14814/phy2.13060)) [MODERATE — mouse model]
- Decreased expression of intestinal stem cell markers (Lgr5) in infected enteroids [MODERATE]
- **Wnt pathway disruption** — increased DKK1 (Wnt antagonist), decreased Wnt5a, downregulated LRP5 (Wnt co-receptor) [PRELIMINARY]
- This suggests C. parvum may impair epithelial regeneration, not just destroy existing villi

### 7.3 Mechanism of Diarrhea

The diarrhea has **multiple contributing mechanisms** — this is NOT purely osmotic:

1. **Malabsorptive component** (primary):
   - Villous atrophy reduces absorptive surface area [ESTABLISHED]
   - Reduced brush-border enzyme activity (disaccharidases, peptidases) [ESTABLISHED]
   - Impaired trans- and paracellular permeability [MODERATE — rat model]
   - Reduced leucine and glutamate absorption [MODERATE — rat model]
   (Barbot et al., 2001; [DOI](https://doi.org/10.1016/S0003-4509(01)80004-3))

2. **Secretory component**:
   - Prostaglandin-mediated epithelial chloride secretion contributes significantly [ESTABLISHED — piglet model]
   - L-arginine/NO pathway promotes PG-dependent secretory diarrhea (Gookin et al., 2008; [DOI](https://doi.org/10.1097/MPG.0b013e31815c0480)) [ESTABLISHED — piglet model]
   - Indomethacin (COX inhibitor) fully inhibits secretory component in infected tissue [ESTABLISHED]

3. **Inflammatory component**:
   - Neutrophilic infiltration and inflammatory cytokines contribute to tissue damage [MODERATE]
   - Reactive oxygen species from neutrophils may exacerbate epithelial injury [MODERATE]

4. **Barrier dysfunction**:
   - Decreased transepithelial resistance [MODERATE]
   - Tight junction disruption allows paracellular leakage [PRELIMINARY]

**Compensatory mechanisms:**
- Crypt cells upregulate nutrient transporters — the ASC (neutral amino acid transport system) relocates from villus to crypt apical border in infected calves, partially compensating for villus loss (Blikslager et al., 2001; [DOI](https://doi.org/10.1152/ajpgi.2001.281.3.G645)) [ESTABLISHED — bovine in vivo]
- Combined glutamine + indomethacin fully restores Na+ and Cl- absorption in infected ileum despite severe villous atrophy [ESTABLISHED — bovine ex vivo]

### 7.4 Clinical Course in Calves

- **Incubation period:** 3-6 days post-infection [ESTABLISHED]
- **Diarrhea onset:** Day 3-5 post-infection; intermittent to persistent watery diarrhea [ESTABLISHED]
- **Duration:** 4-16 days, highly variable between individual calves [ESTABLISHED]
- **Peak oocyst shedding:** Days 6-8 post-infection [ESTABLISHED]
- **Shedding duration:** Mean 7-9 days (range 1-13 days) [ESTABLISHED]
- **Shedding intensity:** Up to 10^6-4x10^7 oocysts per gram of feces [ESTABLISHED]
- **Resolution:** Self-limiting in immunocompetent calves by 2-3 weeks [ESTABLISHED]

**Severity determinants:**
- Dose has minimal effect on severity once threshold is exceeded [ESTABLISHED]
- Co-infection with rotavirus, coronavirus, E. coli, or Salmonella dramatically worsens outcomes (Almawly et al., 2013; [DOI](https://doi.org/10.1016/j.vetpar.2013.04.029)) [ESTABLISHED]
- Colostrum quality/passive transfer status affects severity [MODERATE]
- C. parvum subtype influences pathogenicity — IId subtypes show higher oocyst shedding peaks (4.3x10^7/g) [PRELIMINARY]

### 7.5 What Is Unknown

- Relative contribution of each diarrhea mechanism (malabsorptive vs. secretory vs. inflammatory) in calves specifically (most mechanistic work is in piglets/rodents)
- Why there is such high individual variability in clinical severity among calves receiving identical inocula
- Role of Wnt pathway disruption in delayed mucosal recovery
- Whether the intestinal stem cell damage has long-term consequences for gut function

---

## Stage 8: Persistence, Shedding, and Environmental Burden

### 8.1 Oocyst Shedding Dynamics

- Calves begin shedding oocysts 3-6 days post-infection [ESTABLISHED]
- Peak shedding at days 6-8, with counts up to 10^7 per gram [ESTABLISHED]
- Average shedding duration: 7-9 days [ESTABLISHED]
- A single infected calf can shed **billions** of oocysts during a single infection episode [ESTABLISHED]
- **All oocysts are immediately infectious** — no environmental maturation needed [ESTABLISHED]

### 8.2 Environmental Accumulation Cycle

This is the core transmission problem. In a typical calf-rearing operation:

1. Calf A is infected (possibly from minimal environmental residuum or dam exposure)
2. Calf A sheds billions of oocysts into the environment over 7-9 days
3. **These oocysts persist for months** in bedding, pens, soil, water
4. Calf B enters the contaminated environment and requires only ~10 oocysts to become infected
5. Calf B amplifies the environmental burden further
6. Environmental contamination ratchets upward with each calving cycle

**The math is devastating:**
- 1 infected calf sheds ~10^7 oocysts/g x ~200g feces/day x 7 days = ~1.4 x 10^10 total oocysts
- ID50 for the next calf: ~10 oocysts
- Even if 99.99% of oocysts are removed/inactivated, the remaining 1.4 x 10^6 oocysts can infect ~140,000 more calves

### 8.3 Between-Season Persistence

- Oocysts survive in soil for **at least 2-6 months** at temperate conditions [ESTABLISHED]
- Can survive through winter at 4degC [MODERATE]
- Facilities that housed infected calves remain contaminated even after extended vacancy [MODERATE]
- This creates a **ratchet effect** — each calving season adds to the environmental burden, with incomplete clearance between seasons [INFERRED]

### 8.4 Adult Cattle Shedding

- Adult cattle can shed C. parvum but at **much lower levels** and intermittently [MODERATE]
- Periparturient cows rarely shed detectable oocysts by standard methods [MODERATE]
- Adult cattle show different genotype diversity than calves in the same herd, suggesting calves are not primarily infected by their dams but rather by the contaminated environment or other calves [MODERATE]
- Adults more commonly shed C. bovis, C. ryanae, and C. andersoni — species that are generally **not pathogenic** in neonates [ESTABLISHED]

### 8.5 What Is Unknown

- Quantitative environmental oocyst survival curves under typical farm conditions
- Contribution of biofilm-associated oocysts in water systems
- Whether oocyst viability declines gradually or catastrophically
- Role of invertebrate vectors (flies, beetles) in oocyst dispersal

---

## Stage 9: Species and Genotype Variation

### 9.1 Cryptosporidium Species in Cattle

| Species | Age group | Pathogenicity in calves | Zoonotic | Prevalence |
|---------|-----------|------------------------|----------|------------|
| **C. parvum** | Preweaned calves (1-3 weeks) | **HIGH** — primary pathogen | YES | Dominant in preweaned calves (~70-80% of infections) |
| **C. bovis** | Post-weaned, juveniles | LOW — generally subclinical | No (rare in humans) | Common in older calves |
| **C. ryanae** | Post-weaned, juveniles | LOW — subclinical | No | Common in older calves |
| **C. andersoni** | Adults | LOW — abomasal, not intestinal | No (rare) | Common in adult cattle |

[ESTABLISHED]

### 9.2 C. parvum Subtype Variation (GP60 Gene)

- Two major subtype families dominate in cattle: **IIa** and **IId** [ESTABLISHED]
- IIaA15G2R1 is the most common zoonotic subtype in dairy calves globally [ESTABLISHED]
- IId subtypes may cause more severe disease with higher oocyst shedding [PRELIMINARY]
- Subtype distribution is geographically variable [ESTABLISHED]
- **Same subtypes infect humans and calves** — direct zoonotic transmission confirmed [ESTABLISHED]

### 9.3 What Is Unknown

- Whether virulence differences between subtypes affect treatment efficacy
- Whether subtype-specific interventions (e.g., subtype-specific antibodies) would be needed
- Full diversity of C. parvum subtypes in US beef and dairy operations

---

## Stage 10: Treatment Resistance — Why Nothing Works

### 10.1 Current Treatment Landscape

**There is no effective cure for cryptosporidiosis in calves.** The treatment landscape is defined by failure:

| Treatment | Status | Efficacy | Why it fails |
|-----------|--------|----------|-------------|
| **Halofuginone (Halocur)** | Approved EU, NOT US | Partial — reduces oocyst shedding and diarrhea severity when given prophylactically from birth, but no cure; delayed infection, not prevented | Cryptostatic, not cryptosporicidal; mechanism unclear; must start within 24-48h of birth for best effect; post-infection treatment much less effective |
| **Nitazoxanide** | Approved for human crypto (immunocompetent only) | Conflicting results in calves; some studies show benefit, others no effect | May require functional immune system; mechanism unclear; NTZ activates pyruvate:ferredoxin oxidoreductase (PFOR) but C. parvum may lack classical PFOR |
| **Paromomycin** | Off-label | Effective prophylactically in some studies (eliminates shedding at 100 mg/kg/day); nephrotoxic, expensive | Nephrotoxicity limits use; cost prohibitive for production animals; aminoglycoside — detrimental growth effects in young animals |
| **Decoquinate** | Available as feed additive | No significant anti-cryptosporidial effect in calves (Lallemand et al., 2006; [DOI](https://doi.org/10.1136/vr.159.20.672)) | Targets mitochondrial electron transport — C. parvum has a reduced/absent ETC |
| **Colostrum supplementation** | Management practice | Limited clinical alleviation; modulates gut immune response but does NOT prevent infection or significantly reduce shedding (2023 Frontiers study) | Non-specific antibodies; variable Crypto-specific Ab levels; antibodies degraded in gut |

### 10.2 Why Drugs Fail — Biological Barriers

1. **The niche problem:** The intracellular-extracytoplasmic location means drugs must either:
   - Cross the host cell membrane AND navigate the parasitophorous vacuole architecture, OR
   - Reach the parasite from the luminal side through the PVM
   - Most systemic drugs cannot accumulate sufficiently at the parasite [ESTABLISHED]

2. **Reduced genome = fewer drug targets:** With only ~3,800 genes and minimal metabolic capacity, C. parvum presents far fewer druggable targets than bacteria or fungi [ESTABLISHED]

3. **Speed of replication vs. therapeutic window:** By the time clinical signs appear (day 3-5), billions of parasites and autoinfection are established; the therapeutic window for intervention is already closing [INFERRED]

4. **Autoinfection sustains infection:** Even if a drug reduces the intracellular parasite burden, thin-walled oocysts continuously seed new infection cycles from within the gut lumen [ESTABLISHED]

5. **Host age problem:** The target population (1-3 week old calves) limits the pharmacological options — nephrotoxic, hepatotoxic, or growth-impairing compounds are unacceptable [ESTABLISHED]

6. **Cost constraint:** Production animal economics require treatment costs <$10-15 per calf; most advanced therapeutics far exceed this [ESTABLISHED]

### 10.3 Emerging Drug Targets and Pipeline

| Target/Approach | Mechanism | Stage | Evidence |
|----------------|-----------|-------|----------|
| **CDPK1 (calcium-dependent protein kinase 1)** | Essential kinase; no mammalian homolog; bumped kinase inhibitors (BKIs) block invasion | Preclinical — efficacy in calf model (BKI-1553); newer pyrrolopyrimidine scaffolds (BKI-1649, BKI-1812) more potent | [MODERATE] — multiple labs, calf and mouse models |
| **CpIMPDH (inosine monophosphate dehydrogenase)** | Essential for GMP synthesis; acquired from bacteria; structurally distinct from human IMPDH | Preclinical — triazole and adenosine-derived inhibitors identified | [MODERATE] — screening pipeline established |
| **CpPDE1 (phosphodiesterase)** | Parasite-specific PDE; pyrazolopyrimidine inhibitors rapidly eliminate parasites in vitro | Preclinical — orally efficacious in immunocompromised mouse model (2024 Nature Comms) | [PRELIMINARY] — promising but mouse model only |
| **PI(4)K (phosphatidylinositol 4-kinase)** | Essential lipid kinase; MMV390048 shows efficacy | Preclinical — but PI4K is highly conserved and selectivity is challenging | [PRELIMINARY] |
| **Clofazimine** | Identified by HTS screen; oral phenazine dye | Failed in human HIV-crypto trial (CRYPTOFAZ); active in acute models but NOT persistent infection | [ESTABLISHED — FAILED] |
| **Passive immunization (maternal vaccine)** | Vaccinate dams to boost colostral anti-GP40 antibodies transferred to calves | Bovicrypt (EU approval); novel subunit vaccine targeting GP40 glycopeptide epitope; reduced diarrhea duration in field trials | [MODERATE] — field trials, EU regulatory review |

### 10.4 The 20-Year Test

**Why has no effective treatment emerged despite decades of research?**

1. **Reduced target space** — C. parvum has dramatically fewer druggable targets than other pathogens. The streamlined genome means there are fewer essential enzymes to inhibit.
2. **In vitro culture limitations** — until recently, C. parvum could not be cultured through complete life cycles in vitro, severely hampering drug screening. The HCT-8 cell line supports partial development but not continuous propagation.
3. **Animal model limitations** — immunocompetent mouse models don't replicate disease well; IFN-gamma-knockout or SCID mice are used but don't represent neonatal calf biology.
4. **Market economics** — pharmaceutical investment in neonatal calf diarrhea is limited by per-treatment cost constraints; human Crypto is a neglected tropical disease with limited pharma interest.
5. **The niche problem** compounds everything — even when active compounds are identified in vitro, achieving adequate drug concentrations at the parasite in vivo is extremely difficult.

### 10.5 What Is Unknown

- Whether CDPK1 BKIs will prove safe and economically viable for neonatal calves
- Whether CpPDE1 inhibitors will work in immunocompetent neonatal calves (tested only in immunocompromised mice)
- Whether combination approaches (e.g., prophylactic BKI + maternal vaccination) could achieve clinically meaningful protection
- Whether disrupting the feeder organelle nutrient transport is a viable strategy

---

## Stage 11: Zoonotic Risk

### 11.1 Public Health Significance

- **C. parvum is the dominant zoonotic Cryptosporidium species worldwide** [ESTABLISHED]
- The same GP60 subtypes (especially IIaA15G2R1) infect both calves and humans [ESTABLISHED]
- **Leading cause of waterborne disease outbreaks** — the 1993 Milwaukee outbreak infected ~403,000 people from contaminated municipal water supply [ESTABLISHED]
- Cryptosporidium is the leading cause of outbreaks linked to recreational water and third leading cause linked to animal contact in the US [ESTABLISHED]
- During 2009-2017, 444 cryptosporidiosis outbreaks (7,465 cases) were reported by 40 US states [ESTABLISHED]
- **Direct zoonotic risk to farmworkers** — contact with infected calves is a recognized transmission route; multiple case reports and outbreak investigations [ESTABLISHED]

### 11.2 Cargill-Specific Relevance

- Cargill's calf operations represent a significant public health nexus — large-scale calf-rearing facilities with high environmental contamination can contribute to:
  - Occupational risk for farmworkers
  - Contamination of surface water via runoff
  - Community risk through water supply contamination
- An effective intervention for calf cryptosporidiosis would have dual value: animal health AND public health impact
- Regulatory/reputational risk for Cargill if linked to human outbreaks

### 11.3 What Is Unknown

- Quantitative risk of human infection from specific farm management practices
- Whether subtype variation affects human virulence
- Contribution of US calf operations to human cryptosporidiosis burden vs. other sources

---

## Stage 12: Economic Impact

### 12.1 Direct Costs Per Infected Calf

- Treatment costs, veterinary care, rehydration therapy: **EUR 40-60 per calf** (Western European data; Belgium EUR 60.62, France EUR 43.83, Netherlands EUR 58.24) [MODERATE]
- Estimates range up to **EUR 100-150 per calf** for severe cases requiring intensive care [MODERATE]
- Mortality: variable but can reach 50%+ in scouring calves without intervention [MODERATE]

### 12.2 Indirect and Long-Term Costs

- **Calf body weight lost during neonatal diarrhea is NOT regained in the six months following infection** [ESTABLISHED] — this is the most important economic finding
- Reduced average daily gain persists beyond clinical recovery [MODERATE]
- Increased susceptibility to secondary infections (respiratory disease, other enteric pathogens) [MODERATE]
- Labor costs for intensive monitoring and treatment of sick calves [MODERATE]

### 12.3 Scale of the Problem

- Prevalence of C. parvum in preweaned calves: 20-50% globally [ESTABLISHED]
- In the US, 48% of calves aged 7-21 days on 59% of farms test positive [ESTABLISHED]
- In the EU 2 Seas region (Belgium, France, Netherlands), cryptosporidiosis costs **EUR 55 million** across 11 million calves [MODERATE]
- Extrapolated US impact: with ~9 million dairy calves born annually and ~40-50% infection rate, at $50-100/infected calf, the **US dairy industry alone faces $180-450 million/year** in crypto-related losses [INFERRED]

### 12.4 What Is Unknown

- Precise economic quantification for US beef and dairy operations (most data is European)
- Long-term milk production impact in heifers that had neonatal crypto infection
- True mortality burden in US calf ranching operations where management is less intensive

---

## Transmission Dynamics and R0

### R0 Estimate

**No published R0 value exists specifically for C. parvum in managed calf herds.** This must be inferred from epidemiological data.

**Parameters for inference:**
- Prevalence: 40-50% of calves infected by 3 weeks of age [ESTABLISHED]
- Infectious period: 7-9 days of oocyst shedding [ESTABLISHED]
- Generation time: ~7-10 days (time from infection to peak infectiousness) [ESTABLISHED]
- Environmental persistence: months [ESTABLISHED]
- Infectious dose: ~10 oocysts; single calf sheds ~10^10 total oocysts [ESTABLISHED]
- Attack rate in naive herds: approaches 100% [MODERATE]

**Inferred R0: 3-8 in typical managed calf operations** [INFERRED]

**Reasoning:**
- With an ID50 of ~10 oocysts and shedding of 10^10 oocysts per infected calf, the theoretical R0 in the absence of any control would be astronomically high
- Practical R0 is constrained by: pen separation, cleaning between calves, limited contact window (calves age out of susceptibility by 4-6 weeks)
- That prevalence stabilizes at 40-50% (not 100%) suggests some management barriers and age-related immunity prevent universal infection, but R0 is clearly well above 1.0
- The Brookhart et al. (2002) mathematical model of the Milwaukee human outbreak ([DOI](https://doi.org/10.1002/sim.1258)) estimated secondary transmission parameters but these apply to waterborne human transmission, not calf-to-calf dynamics
- A 2023 deterministic model found that shedding rate and environmental acquisition rate are the most sensitive parameters for persistence

### R0 Fragility Assessment

**R0 is NOT near 1.0.** This is critical for target prioritization.

- At R0 = 3-8, **small prevention effects will NOT collapse herd prevalence**
- Even a 30-40% reduction in new infections would still leave R0 well above 1.0
- **Implications for portfolio:**
  - Pure prevention approaches (vaccines, environmental control) must be dramatically effective to make a dent
  - Treatment/reduction of shedding in infected calves could reduce environmental burden but requires >90% efficacy to meaningfully reduce R0
  - The most impactful interventions would be those that either:
    (a) Prevent or dramatically shorten the clinical disease window (reducing individual calf suffering and economic loss)
    (b) Reduce oocyst output per infected calf by >90% (cutting environmental amplification)
  - Combined approaches (partial prevention + partial treatment) may be needed

### Prevention vs. Treatment Leverage

At this R0, **treatment leverage is likely higher than prevention leverage** for individual calf outcomes, but **environmental contamination reduction** (via reduced shedding) has long-term herd benefits.

A 90% reduction in oocyst shedding per infected calf would reduce environmental burden by ~10x, potentially bringing effective R0 below 1.0 over 2-3 calving cycles.

**Tag: [INFERRED] — no published R0 for managed calf herds; inference from epidemiological parameters**

---

## The Rate-Limiting Barrier

### Identification

The single most important barrier to solving cryptosporidiosis in neonatal calves is:

**The intracellular-extracytoplasmic parasitophorous vacuole niche combined with autoinfection via thin-walled oocysts.**

This is not a single-stage problem — it is an architectural barrier that defeats interventions at multiple stages simultaneously:

1. **Drug delivery failure:** The niche is accessible neither from the systemic circulation (parasite is not in the cytoplasm) nor straightforwardly from the intestinal lumen (parasite is membrane-enclosed). This eliminates most standard drug delivery approaches.

2. **Autoinfection sustains infection:** Even if an intervention reduces the intracellular burden, thin-walled oocysts (~20% of production) continuously seed new infection cycles from within the gut. Any intervention that is not continuously present during the entire infection period will fail due to rebound.

3. **Speed vs. immune kinetics:** The parasite amplifies exponentially with a ~12-14h doubling time while adaptive immunity requires 6-7 days to activate. The race is over before the immune system starts running.

4. **Reduced target space:** The streamlined genome (~3,800 genes) means there are far fewer essential, druggable, parasite-specific targets than for any bacterial or fungal pathogen.

### Why This Is the Barrier (Not Something Else)

- It is NOT the environmental persistence alone — if drugs worked, treated calves would recover regardless of environmental burden
- It is NOT the immune deficiency alone — immunocompetent calves DO clear infection; the problem is damage before clearance
- It is NOT the low infectious dose alone — many other pathogens have low infectious doses but are treatable
- It IS the combination of the unique niche + autoinfection + rapid replication + minimal drug targets that makes this disease intractable to conventional approaches

---

## KE#1: Portfolio-Restructuring Experiment

### The Question

**Does luminal-acting drug delivery (reaching the parasite from the intestinal lumen through the PVM) achieve equivalent or superior parasite killing compared to systemically absorbed drugs that must traverse host cell membranes?**

This question determines whether the portfolio should prioritize:
- (A) Luminal/topical approaches (oral non-absorbable compounds, large molecules, colostral antibodies) that access the PVM from the lumen, OR
- (B) Systemic small molecules that must cross into the host cell and navigate the feeder organelle interface, OR
- (C) Whether both routes are needed simultaneously

### The Experiment

**Ex vivo Ussing chamber drug access study with C. parvum-infected neonatal calf ileum**

1. Obtain ileal tissue from C. parvum-infected calves at day 5-7 post-infection (peak parasitism) — source from slaughterhouse or terminal experiment
2. Mount in Ussing chambers with separate mucosal (luminal) and serosal (systemic) reservoirs
3. Apply known anti-Cryptosporidium compounds (paromomycin, BKI-1553, nitazoxanide) to EITHER:
   - Mucosal side only (simulating oral/luminal delivery)
   - Serosal side only (simulating systemic delivery)
   - Both sides simultaneously
4. Measure parasite viability/infectivity after 4-8 hours using RT-qPCR for parasite RNA, excystation assays, and/or immunofluorescence
5. Quantify drug penetration to the parasite niche from each route

### Cost and Timeline

- **Cost:** $10-15K (tissue procurement, Ussing chamber time, drug compounds, quantification assays)
- **Timeline:** 4-6 weeks
- **Location:** Any veterinary parasitology lab with Ussing chamber capability and access to infected calf tissue (e.g., NC State, Cornell, Moredun Institute)

### What Changes

- **If luminal delivery is superior:** Portfolio prioritizes oral non-absorbable compounds, antibody-based approaches, and large-molecule therapeutics. Systemic BKIs are deprioritized. Maternal vaccination (colostral antibodies) becomes the lead platform.
- **If systemic delivery is superior:** Portfolio prioritizes cell-permeable small molecules (BKIs, PDE inhibitors, IMPDH inhibitors). Antibody approaches are deprioritized.
- **If both routes achieve similar access:** Combination approaches become the priority — oral prophylaxis + systemic treatment.

This experiment resolves ~40-50% of the downstream portfolio structure.

---

## Species and Genotype Context

### Age-Related Species Distribution in Cattle

| Age | Dominant species | Clinical significance |
|-----|-----------------|----------------------|
| 0-4 weeks | C. parvum | HIGH — primary cause of neonatal diarrhea |
| 1-6 months | C. bovis, C. ryanae | LOW — subclinical |
| >6 months | C. andersoni | LOW — abomasal, mild |
| Adults | Mixed (C. andersoni dominant) | MINIMAL — intermittent low-level shedding |

[ESTABLISHED]

### Key Implication

The therapeutic target is **exclusively C. parvum in 1-3 week old calves**. Any intervention must be safe for neonates, effective against C. parvum specifically, and deliverable within the first 1-2 weeks of life. The narrow age window is both a challenge (immature immunity) and an opportunity (defined prophylaxis window).

---

## Summary Disease Map

| Stage | Key Mechanism | Therapeutic Relevance | Evidence Tier |
|-------|--------------|----------------------|---------------|
| **1. Entry** | Fecal-oral; ID50 ~10 oocysts; environmental persistence months | Prevention: reduce oocyst exposure | ESTABLISHED |
| **2. Excystation/Invasion** | Sporozoite attachment via CSL/GP40/TRAP; host actin remodeling | Block invasion: anti-GP40 antibodies, invasion inhibitors | ESTABLISHED |
| **3. Unique Niche** | Intracellular-extracytoplasmic PVM; feeder organelle for nutrients | Drug delivery challenge; luminal vs systemic access | ESTABLISHED |
| **4. Asexual Amplification** | Type I meronts; 8 merozoites per cycle; ~12-14h; exponential | Target merogony: BKIs, IMPDH inhibitors, PDE inhibitors | ESTABLISHED |
| **5. Oocyst Formation** | Thick-walled (transmission) + thin-walled (autoinfection) | Block autoinfection; reduce shedding | ESTABLISHED |
| **6. Immune Evasion** | Niche shields antigens; replication outpaces neonatal immunity | Boost neonatal immunity; passive immunization | ESTABLISHED |
| **7. Pathology** | Villous atrophy; secretory + malabsorptive diarrhea; barrier loss | Supportive care; anti-secretory (indomethacin + glutamine) | ESTABLISHED |
| **8. Shedding/Environment** | 10^7/g for 7-9 days; oocyst environmental persistence | Reduce shedding intensity; environmental decontamination | ESTABLISHED |
| **9. Species Variation** | C. parvum only pathogen in neonates; IIa/IId subtypes | Target specificity to C. parvum | ESTABLISHED |
| **10. Treatment Failure** | Unique niche + reduced genome + autoinfection + speed | Need new approaches: BKIs, PDEi, IMPDH, antibodies | ESTABLISHED |
| **11. Zoonotic Risk** | Same subtypes infect humans; waterborne outbreaks | Dual value: animal + public health | ESTABLISHED |
| **12. Economic Impact** | $50-150/calf; weight loss not recovered; $180-450M/yr US | Strong commercial case for intervention | MODERATE |

---

## Disease Stages Requiring Portfolio Coverage

For Forge to propose solutions, every stage below must have at least one candidate:

1. **Prevention of initial infection** (reducing oocyst ingestion / blocking invasion)
2. **Killing/inhibiting intracellular parasites** (targeting merogony within the niche)
3. **Blocking autoinfection** (preventing thin-walled oocyst recycling)
4. **Reducing oocyst shedding** (cutting environmental contamination)
5. **Mitigating pathology** (reducing diarrhea severity and duration)
6. **Accelerating recovery** (restoring mucosal function, weight gain)
7. **Environmental decontamination** (reducing oocyst burden between calves)
8. **Boosting neonatal immunity** (passive or active immunization)

---

*Disease map complete. 12 stages mapped with evidence tiers. R0 estimated at 3-8 [INFERRED]. Rate-limiting barrier identified: intracellular-extracytoplasmic niche + autoinfection cycle. KE#1 defined: Ussing chamber luminal vs. systemic drug access study ($10-15K, 4-6 weeks). Ready for external panel review and Sapper analysis.*
