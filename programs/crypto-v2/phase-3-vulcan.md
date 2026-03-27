# Phase 3 — Vulcan: First-Principles Vulnerability Analysis

**Program:** Cryptosporidiosis | **Partner:** [QUARANTINED] | **Version:** v2
**Agent:** Vulcan | **Date:** 2026-03-27

**Quarantine status:** CLEAN. This analysis is derived ONLY from the Phase 1 disease map and molecular biology research. No failure analysis, no candidate list, no external panel, no partner context was consulted.

---

## Method

I decomposed every molecular system described in the disease map into its constituent intervention points. For each, I wrote a kill-chain (the sequence of assumptions required for the intervention to work), identified the weakest link, estimated magnitude of effect, and specified a falsifiable prediction.

The biology reveals **four major vulnerability domains:**

1. **The sexual reproduction checkpoint** — the parasite's Achilles' heel
2. **The feeder organelle nutrient interface** — the lifeline
3. **The invasion and egress machinery** — the moving parts
4. **The reduced-genome metabolic bottlenecks** — what it cannot live without

---

## DOMAIN 1: THE SEXUAL REPRODUCTION CHECKPOINT

This is the single most promising vulnerability domain. C. parvum must complete sexual reproduction to produce oocysts (both thick-walled for transmission AND thin-walled for autoinfection). Blocking sex blocks BOTH transmission AND autoinfection simultaneously. Recent molecular discoveries (2024) reveal the transcription factors controlling this commitment, making this domain newly druggable.

---

### Intervention Point 1: Myb-M — Male Fate Determination Blockade

**Target/mechanism:** Myb-M transcription factor (master regulator of male sexual commitment in C. parvum). Myb-M is necessary and sufficient to drive male fate in an organism that lacks genetic sex determination. Conditional ablation of Myb-M leads to complete loss of male gametes, a complete block of oocyst production in mice, and therefore a complete block of both transmission and autoinfection.

**Disease stage:** Stage 5 (Sexual Reproduction and Oocyst Formation)

**Kill-chain:**
1. A small molecule or biologic inhibits Myb-M DNA-binding or protein-protein interactions [ASSUMPTION — Myb-family transcription factors have been targeted in oncology; the Myb DNA-binding domain is a known pharmacological target class]
2. Inhibition of Myb-M prevents transcription of male-specific gene programs [ESTABLISHED — genetic ablation demonstrates this]
3. Without male gametes, no microgametes are produced [ESTABLISHED — conditional ablation eliminates males while females/asexuals persist]
4. Without microgametes, macrogamonts cannot be fertilized [ESTABLISHED — obligate sexual reproduction]
5. Without fertilization, no zygotes form, no oocysts are produced [ESTABLISHED — confirmed in mouse model]
6. Without oocyst production: (a) no thin-walled oocysts = autoinfection cycle is broken, (b) no thick-walled oocysts = transmission is blocked [ESTABLISHED]
7. With autoinfection broken, the existing asexual parasite population is finite and will be cleared by the developing immune system within 7-14 days [INFERRED — established that adaptive immunity clears infection; without autoinfection renewal, the kinetic race shifts decisively to the immune system]

**Weakest link:** Step 1 — Can Myb-M be pharmacologically inhibited? Transcription factors are historically difficult drug targets ("undruggable"). However: (a) Myb-family TFs have been targeted via disruption of protein-protein interactions (Myb-p300 in AML), (b) the parasite's reduced proteome may make Myb-M's interacting partners limited and targetable, (c) PROTACs or molecular glue degraders could target Myb-M for destruction. The key question is whether the Myb-M protein has accessible binding pockets or obligate cofactors that can be disrupted by a small molecule.

**Magnitude estimate:** If Myb-M inhibition achieves complete block of oocyst production (as genetic ablation does): >95% reduction in disease severity (autoinfection loop broken), >99% reduction in environmental oocyst shedding. This is potentially a CURATIVE intervention.

**Falsifiable prediction:** A cell-permeable Myb-M inhibitor (or a compound that degrades Myb-M protein) will eliminate oocyst production in C. parvum cell culture within 24 hours of treatment, even when applied after asexual stages are established. Test: treat HCT-8 cultures at 24h post-infection (asexual stages established) with Myb-M inhibitor vs. DMSO; quantify oocyst production at 72h by immunofluorescence.

**Closest analogy:** c-Myb inhibition in acute myeloid leukemia. The Myb-p300 interaction has been disrupted by peptidomimetics and small molecules (Ramaswamy et al., 2018). Myb-M in C. parvum is structurally related, suggesting similar pharmacological approaches may be applicable.

---

### Intervention Point 2: AP2-F — Female Gamete Maturation Blockade (Oocyst Wall Assembly)

**Target/mechanism:** AP2-F transcription factor (female-specific Apetala 2-domain protein, cgd4_1110). AP2-F controls transcription of genes encoding crystalloid body proteins and oocyst wall proteins (COWPs) exclusively expressed in female gametes. Genetic ablation blocks oocyst shedding in vivo. Unlike Myb-M (which blocks one sex), AP2-F blocks the OUTPUT — oocyst wall assembly.

**Disease stage:** Stage 5 (Sexual Reproduction and Oocyst Formation)

**Kill-chain:**
1. A compound inhibits AP2-F DNA-binding activity or promotes its degradation [ASSUMPTION — AP2 domains are plant-type transcription factors absent from mammals, potentially offering selectivity]
2. Without AP2-F, COWP genes and crystalloid body genes are not transcribed [ESTABLISHED — genetic ablation data]
3. Without COWPs and crystalloid body proteins, oocyst wall assembly fails [ESTABLISHED — AP2-F ablation blocks oocyst shedding]
4. Without intact oocyst walls, (a) thick-walled oocysts cannot be produced = no environmental transmission, (b) thin-walled oocysts are likely malformed and non-functional = autoinfection disrupted [INFERRED — if wall formation genes are broadly affected, thin-walled oocyst function should also be impaired]
5. Without functional oocysts, infection becomes self-limiting and immune clearance completes [INFERRED]

**Weakest link:** Step 4 — the relationship between AP2-F and thin-walled oocyst production. AP2-F ablation blocks oocyst SHEDDING (thick-walled), but it is not established whether thin-walled oocyst formation is equally dependent on AP2-F-regulated genes. If thin-walled oocysts use a different wall assembly pathway (they are single-membrane, not triple-layered), AP2-F inhibition might block transmission without blocking autoinfection. This would still be valuable but not curative.

**Magnitude estimate:** If AP2-F inhibition blocks both oocyst types: >90% disease reduction (same logic as Myb-M). If it only blocks thick-walled oocysts: ~30-50% disease reduction (blocks transmission but not autoinfection; still valuable for herd-level R0 reduction).

**Falsifiable prediction:** AP2-F inhibition will block thick-walled oocyst production completely but will have a measurable but smaller effect on thin-walled oocyst-mediated autoinfection. Test: AP2-F-ablated parasites in immunocompromised mice should show zero fecal oocyst shedding but may still sustain intracellular infection (via autoinfection with malformed thin-walled oocysts) for longer than wild-type parasites cleared by immune-competent hosts.

**Closest analogy:** AP2 transcription factor targeting in Plasmodium. AP2-G in malaria controls gametocyte commitment and has been studied as a transmission-blocking target. The Cryptosporidium AP2-F is the output-side equivalent.

---

### Intervention Point 3: CDPK5 — Male Gamete Egress Blockade

**Target/mechanism:** Calcium-dependent protein kinase 5 (CDPK5). CDPK5 is expressed during male gamete development and is required for egress of mature microgametes from the host cell. CDPK5 deletion reduces virulence, disease severity, and oocyst shedding. Unlike CDPK1 (which has a glycine gatekeeper enabling bumped kinase inhibitors), CDPK5 would require its own inhibitor design. However, CDPK5 is NOT essential for asexual growth, making it a transmission-stage-specific target.

**Disease stage:** Stage 5 (Sexual Reproduction — specifically, male gamete release)

**Kill-chain:**
1. A kinase inhibitor blocks CDPK5 catalytic activity [ASSUMPTION — CDPKs are established druggable kinases; the question is selectivity over host kinases and over CpCDPK1]
2. Blocked CDPK5 prevents phosphorylation of substrates required for microgamete egress [ESTABLISHED — phosphoproteomics identifies putative substrates]
3. Microgametes fail to egress from the host cell [ESTABLISHED — CDPK5 deletion phenotype]
4. Trapped microgametes cannot reach macrogamonts for fertilization [INFERRED]
5. No fertilization = no oocyst production = no autoinfection + no transmission [INFERRED]

**Weakest link:** Step 1 — CDPK5 gatekeeper residue is unknown to me. If it has a bulky gatekeeper (unlike CDPK1's glycine), bumped kinase inhibitors will not work, and standard kinase inhibitor selectivity challenges apply. Additionally, CDPK5 genetic ablation shows parasites are still VIABLE — they just have reduced virulence. This means the block is partial, not absolute.

**Magnitude estimate:** Based on genetic ablation data (reduced but not eliminated virulence): 40-60% disease reduction. Less potent than complete sex block (Myb-M) because CDPK5 deletion reduces but does not eliminate oocyst shedding.

**Falsifiable prediction:** A selective CDPK5 inhibitor will reduce oocyst shedding in infected mice proportionally to its effect on microgamete egress, without affecting asexual replication rates. Test: measure asexual parasite burden (qPCR at 24h intervals) and oocyst output simultaneously in CDPK5 inhibitor-treated vs. untreated mice. Prediction: asexual burden will be identical, but oocyst output will be reduced by >50%.

**Closest analogy:** CDPK5 targeting in Toxoplasma gondii for transmission blocking. TgCDPK5 has been investigated in similar context.

---

## DOMAIN 2: THE FEEDER ORGANELLE — THE LIFELINE

The feeder organelle is the parasite's sole interface for nutrient acquisition from the host cell. C. parvum has the most reduced genome of any apicomplexan — it cannot synthesize amino acids, nucleotides, or fatty acids de novo. Everything must come through the feeder organelle. Disrupting this interface should starve the parasite.

However, recent genetic data (2024) reveals REDUNDANCY in glucose transport. This domain requires careful target selection.

---

### Intervention Point 4: Glycogen Phosphorylase — The Essential Internal Energy Reserve

**Target/mechanism:** C. parvum glycogen phosphorylase. This enzyme releases glucose-1-phosphate from the parasite's amylopectin (glycogen-like) stores. Genetic ablation demonstrates it is ESSENTIAL for parasite growth — unlike CpGT1 and CpGT2 (which are individually dispensable due to redundancy), glycogen phosphorylase has no backup. The parasite stores amylopectin as an energy reserve and uses glycogen phosphorylase to mobilize it. Without this enzyme, the parasite cannot access its internal energy reserves and cannot compensate for fluctuations in host glucose supply.

**Disease stage:** Stage 3 (Intracellular-Extracytoplasmic Niche) and Stage 4 (Merogony)

**Kill-chain:**
1. A glycogen phosphorylase inhibitor reaches the parasitophorous vacuole niche [ASSUMPTION — the compound must be accessible from the luminal side through the PVM, or must penetrate the host cell membrane. Given the extracytoplasmic niche, luminal access is plausible for small molecules]
2. Inhibitor blocks CpGP catalytic activity [ASSUMPTION — glycogen phosphorylase is a well-characterized enzyme class with known inhibitors in mammalian systems; selectivity for the parasite enzyme over host glycogen phosphorylase requires structural differences]
3. Without glycogen phosphorylase, the parasite cannot mobilize amylopectin stores [ESTABLISHED — genetic essentiality demonstrated]
4. Without internal glucose-1-phosphate supply, the parasite is entirely dependent on glucose transport through CpGT1/CpGT2 [INFERRED]
5. Because glucose transport through CpGT1/CpGT2 is ALSO individually dispensable (redundant), loss of internal reserves creates a metabolic crisis only if external supply is also intermittent or insufficient [INFERRED — the parasite may survive on external glucose alone if host glucose levels are adequate]
6. During merogony (rapid replication producing 8 merozoites per 12-14h), energy demand peaks and exceeds what external glucose transport alone can supply [INFERRED — this is the critical assumption]
7. Metabolic crisis during replication = incomplete merogony, reduced merozoite production, slower amplification [INFERRED]

**Weakest link:** Step 6 — whether glycogen phosphorylase inhibition alone creates sufficient metabolic stress. The 2024 genetic data shows that the parasite has MULTIPLE redundant glucose pathways. Glycogen phosphorylase is essential, but this may be because it provides glucose-1-phosphate (which enters glycolysis via phosphoglucomutase) AND because it maintains amylopectin homeostasis (the parasite needs to both store and mobilize). The real vulnerability may be the COMBINATION of glycogen phosphorylase inhibition + glucose transporter inhibition — eliminating both external and internal glucose sources simultaneously.

**Magnitude estimate:** As monotherapy: 30-50% reduction in parasite burden (metabolic stress but not starvation, due to redundant transport). In combination with glucose transport blockade: potentially >80% (complete glucose starvation).

**Falsifiable prediction:** Glycogen phosphorylase inhibition will slow merogony cycle time (from ~12-14h to >20h) without killing established parasites, reducing peak parasite burden by ~50%. The effect will be MORE pronounced during the exponential growth phase (days 2-5) than during the established infection phase (days 6-10). Test: quantitative time-course comparison of parasite burden (qPCR) in GP-inhibitor-treated vs. untreated cell cultures, with sampling every 6 hours for 72 hours.

**Closest analogy:** Human glycogen phosphorylase inhibitors for type 2 diabetes (CP-316,819, ingliforib). These compounds demonstrate that glycogen phosphorylase is a druggable enzyme class. The challenge is achieving selectivity for the parasite enzyme.

---

### Intervention Point 5: Aldolase — The Non-Redundant Glycolytic Chokepoint

**Target/mechanism:** Fructose-bisphosphate aldolase. The 2024 genetic ablation study (Striepen lab) demonstrated that while CpGT1, CpGT2, and hexokinase are all individually dispensable (redundant), aldolase is ESSENTIAL. Aldolase sits downstream of all glucose entry points — whether glucose comes from CpGT1/GT2, from hexokinase-mediated phosphorylation, or from glycogen phosphorylase-mediated amylopectin mobilization, it ALL converges at aldolase for glycolysis. Aldolase is the non-redundant chokepoint.

**Disease stage:** Stage 3 and Stage 4 (all intracellular stages)

**Kill-chain:**
1. An aldolase inhibitor reaches the parasite in the extracytoplasmic niche [ASSUMPTION — same delivery challenge as all feeder organelle targets]
2. Inhibitor selectively blocks CpAldolase without inhibiting host aldolase [ASSUMPTION — this is the major challenge; aldolase is highly conserved. However, C. parvum aldolase may have structural differences exploitable for selectivity, given the parasite's evolutionary divergence]
3. With aldolase blocked, glycolysis halts at the fructose-1,6-bisphosphate step [ESTABLISHED — standard biochemistry]
4. Without glycolysis, the parasite cannot generate ATP (C. parvum has no functional mitochondria, no TCA cycle, no electron transport chain — glycolysis is the SOLE ATP source) [ESTABLISHED — reduced genome, glycolysis-only energy metabolism]
5. Without ATP, all energy-dependent processes halt: replication, protein synthesis, transport [ESTABLISHED — bioenergetic collapse]
6. Parasite death [INFERRED — but rapid, given complete energy dependence on glycolysis]

**Weakest link:** Step 2 — selectivity. Aldolase is a conserved enzyme. Human aldolase B (liver) and aldolase A (muscle) are essential host enzymes. Achieving >100-fold selectivity for CpAldolase may be difficult. However, C. parvum's extreme evolutionary divergence (~1 billion years from mammals) suggests that active-site or allosteric differences exist. Structural comparison of CpAldolase vs. human aldolase is required.

**Magnitude estimate:** If selective inhibition is achievable: >90% parasite killing within 24 hours. This is a KILL target, not a SLOW target. Complete glycolytic blockade in an organism with no alternative energy source is lethal.

**Falsifiable prediction:** CpAldolase will have at least 3 active-site residue differences from human aldolase A/B that create a selectivity pocket for parasite-specific inhibitors. Test: comparative structural analysis (homology modeling or crystal structure) of CpAldolase vs. human aldolase; identify divergent residues within 5 angstroms of the active site.

**Closest analogy:** Trypanosoma brucei aldolase inhibitors in sleeping sickness research. T. brucei also depends on glycolysis, and aldolase inhibitors have been explored as antiparasitic agents.

---

### Intervention Point 6: Dual Glucose Transport Blockade (CpGT1 + CpGT2 Simultaneous Inhibition)

**Target/mechanism:** Simultaneous inhibition of BOTH CpGT1 and CpGT2 glucose transporters at the feeder organelle. Individually, each is dispensable due to redundancy. But the 2024 genetic data shows that the parasite requires SOME glucose import — the redundancy means single-knockout is tolerated, not that glucose import is unnecessary. A compound that blocks BOTH transporters (or that blocks the shared transport mechanism) would eliminate external glucose supply entirely.

**Disease stage:** Stage 3 (Feeder Organelle Nutrient Interface)

**Kill-chain:**
1. A compound inhibits both CpGT1 and CpGT2 glucose/glucose-6-phosphate transport [ASSUMPTION — requires a pan-CpGT inhibitor or a compound targeting a shared structural feature of both transporters]
2. Without external glucose import, the parasite relies entirely on internal amylopectin reserves [ESTABLISHED — logical consequence given the metabolic map]
3. Amylopectin reserves are finite [ESTABLISHED — stored granules are limited]
4. Once reserves are depleted, glycolysis halts [INFERRED]
5. Without glycolysis, ATP production stops, parasite dies [ESTABLISHED]

**Weakest link:** Step 1 — designing a single compound that inhibits both CpGT1 and CpGT2 selectively over host GLUT transporters. CpGT1 and CpGT2 transport glucose-6-phosphate directly (unusual — mammalian GLUTs transport glucose, not glucose-6-phosphate), which provides a potential selectivity handle: a glucose-6-phosphate mimetic might preferentially bind the parasite transporters.

**Magnitude estimate:** If both transporters fully blocked: parasite death within 24-48 hours (time to deplete amylopectin). But given the likelihood of incomplete inhibition: 50-70% parasite burden reduction.

**Falsifiable prediction:** CpGT1 and CpGT2 will share a conserved glucose-6-phosphate binding motif that differs from the glucose binding site of human GLUT1-4, enabling design of a selective dual inhibitor. Test: sequence alignment and homology modeling of CpGT1/GT2 substrate-binding domains vs. human GLUT family.

**Closest analogy:** Dual SGLT1/SGLT2 inhibitors in diabetes (sotagliflozin). Targeting two related transporters with a single molecule is pharmacologically precedented.

---

### Intervention Point 7: CpABC1 — The Multi-Cargo Transporter

**Target/mechanism:** CpABC1, an ATP-binding cassette transporter localized to the feeder organelle. ABC transporters move diverse substrates (lipids, amino acids, drugs, metabolites). CpABC1 is positioned at the host-parasite interface and likely mediates transport of multiple essential nutrients that the parasite cannot synthesize. Unlike the glucose transporters (redundant), CpABC1 appears to be a SINGLE transporter responsible for non-glucose cargo.

**Disease stage:** Stage 3 (Feeder Organelle)

**Kill-chain:**
1. A CpABC1 inhibitor blocks the transporter's substrate-binding pocket (NOT the ATP-binding site, which is conserved across all ABCs) [ASSUMPTION — substrate-binding domain specificity is required for selectivity over host ABCs]
2. Without CpABC1 function, the parasite cannot import essential non-glucose nutrients (lipids, amino acids, nucleoside precursors) from the host [INFERRED — the precise cargo set is not fully defined]
3. Nutrient starvation halts replication [INFERRED — the parasite has no de novo synthesis of these molecules]
4. Starvation during the rapid merogony phase (8 merozoites per 12-14h) is particularly damaging [INFERRED]

**Weakest link:** Step 2 — the cargo specificity of CpABC1 is not established. If CpABC1 transports only lipids (and amino acids come through other mechanisms), then inhibition would be less lethal. The complete molecular composition of the feeder organelle membrane is unknown.

**Magnitude estimate:** Highly uncertain. If CpABC1 is the sole non-glucose transporter: >80% efficacy. If alternative nutrient import pathways exist: <30%.

**Falsifiable prediction:** CpABC1 genetic ablation will be LETHAL (unlike CpGT1/GT2 ablation which is tolerated), because CpABC1 has no paralog in the C. parvum genome. Test: CRISPR-Cas9 ablation of CpABC1 in the Striepen lab's genetic system; assess whether knockout parasites can replicate in cell culture.

**Closest analogy:** Targeting P-glycoprotein (ABCB1) in cancer MDR reversal. ABC transporters are an established druggable family, though selectivity is the challenge.

---

## DOMAIN 3: THE INVASION AND EGRESS MACHINERY

C. parvum must invade new host cells continuously during merogony (every 12-14h). Each invasion event requires coordinated deployment of apical secretory organelles (micronemes, rhoptries, dense granules), gliding motility, host cell signaling hijack, and actin remodeling. Each component is a potential intervention point.

---

### Intervention Point 8: Host-Side Cdc42/N-WASP/Arp2/3 Actin Remodeling Blockade

**Target/mechanism:** The host cell Cdc42 -> N-WASP -> Arp2/3 -> actin polymerization cascade that C. parvum HIJACKS to drive membrane protrusion around the invading sporozoite/merozoite. This is a HOST-DIRECTED target: instead of hitting the parasite, hit the host cell signaling that the parasite exploits.

**Disease stage:** Stage 2 (Invasion) — applies to EVERY invasion event (primary sporozoite invasion, merozoite reinvasion, autoinfection reinvasion)

**Kill-chain:**
1. An N-WASP inhibitor (e.g., wiskostatin) or Arp2/3 inhibitor (e.g., CK-666) is delivered to the intestinal epithelium [ASSUMPTION — these compounds exist and have been used experimentally; the challenge is intestinal delivery without systemic toxicity]
2. Inhibitor blocks host cell actin branching and membrane protrusion at the invasion interface [ESTABLISHED — Cdc42/N-WASP/Arp2/3 is required for C. parvum invasion in cell culture]
3. Without membrane protrusion, sporozoites/merozoites cannot form the parasitophorous vacuole [ESTABLISHED — actin polymerization inhibition blocks invasion in vitro]
4. Blocked invasion means: (a) newly released merozoites from merogony cannot invade fresh enterocytes, (b) sporozoites from thin-walled oocyst autoinfection cannot invade, (c) environmental sporozoites from ingested oocysts cannot invade
5. Existing intracellular parasites complete their current merogony cycle but released merozoites die extracellularly [INFERRED]
6. Infection burns out within 1-2 merogony cycles (12-28 hours) [INFERRED]

**Weakest link:** Step 1 — Cdc42/N-WASP/Arp2/3 are ESSENTIAL host cell proteins involved in normal intestinal cell functions (cell migration, wound healing, barrier integrity). Systemic or even mucosal inhibition could cause severe enteropathy. The therapeutic window between blocking parasite invasion and impairing host cell function may be very narrow. HOWEVER: the parasite requires ACUTE, HIGH-INTENSITY actin remodeling (dense branched networks), while normal enterocyte function uses lower-level actin dynamics. A partial inhibitor (reducing Arp2/3 activity by 50-70% rather than fully blocking it) might differentially impair the intense invasion-associated remodeling while preserving baseline cell functions.

**Magnitude estimate:** If invasion is fully blocked: >95% reduction in disease (all amplification stops). But host toxicity limits practical efficacy to probably 30-60% invasion reduction with acceptable safety.

**Falsifiable prediction:** A dose-response curve for CK-666 (Arp2/3 inhibitor) applied luminally to C. parvum-infected intestinal organoids will show a concentration at which parasite reinvasion is reduced by >80% while organoid viability and barrier function (TEER) remain >70% of untreated controls. Test: concentration-response study in infected intestinal organoids with simultaneous measurement of parasite burden and organoid health.

**Closest analogy:** This approach has no direct precedent as an anti-infective strategy. The closest conceptual analog is CCR5 receptor blockers (maraviroc) for HIV — host-directed therapy that blocks pathogen cell entry.

---

### Intervention Point 9: CpROM1 Rhomboid Protease Inhibition — Locking the Invasion Machinery

**Target/mechanism:** CpROM1, a rhomboid intramembrane serine protease. CpROM1 cleaves microneme surface proteins (including GP900) during invasion. Rhomboid proteases are essential in apicomplexan parasites for "shedding" adhesins after they have been used for attachment — this cleavage allows the parasite to detach from the initial binding site and complete invasion. Without rhomboid cleavage, the parasite gets STUCK — it attaches but cannot complete entry.

**Disease stage:** Stage 2 (Invasion) — every invasion event

**Kill-chain:**
1. A rhomboid protease inhibitor reaches the intestinal epithelium and specifically inhibits CpROM1 [ASSUMPTION — rhomboid proteases have unusual active sites (catalytic dyad within the membrane); isocoumarin and beta-lactam-based inhibitors have been developed for rhomboid proteases]
2. CpROM1 inhibition prevents cleavage of GP900 and other microneme adhesins at the parasite surface [ESTABLISHED — CpROM1 cleaves GP900]
3. Uncleaved adhesins remain anchored to the host cell surface — the parasite cannot detach from initial attachment points and cannot complete invasion [INFERRED — based on rhomboid function in Toxoplasma and Plasmodium, where rhomboid inhibition traps parasites at the cell surface]
4. Trapped sporozoites/merozoites are exposed to luminal immune factors (antibodies, complement, antimicrobial peptides) [INFERRED]
5. Merozoites released from merogony cannot reinvade = amplification stops [INFERRED]

**Weakest link:** Step 3 — the assumption that CpROM1 inhibition traps parasites is based on the Toxoplasma/Plasmodium rhomboid model. C. parvum invasion is mechanistically distinct (extracytoplasmic niche, host actin-driven rather than parasite actin-driven). CpROM1 may have additional substrates or may not be absolutely required for invasion completion. CpROM1 is also the LARGEST rhomboid described (990 amino acids), suggesting additional domains with unknown functions.

**Magnitude estimate:** If CpROM1 is essential for invasion completion: 70-90% disease reduction. If redundant proteases exist: <30%.

**Falsifiable prediction:** CpROM1 inhibition will cause accumulation of uncleaved GP900 on the sporozoite surface (detectable by GP900-specific antibody staining showing increased surface signal) and will reduce invasion of HCT-8 cells by >70% without affecting excystation or motility. Test: treat sporozoites with rhomboid inhibitor (DCI or isocoumarin), then quantify surface GP900 by flow cytometry and invasion efficiency by immunofluorescence.

**Closest analogy:** Rhomboid protease inhibitors in malaria (PfROM4). PfROM4 is being pursued as an antimalarial target. CpROM1 is the Cryptosporidium equivalent.

---

### Intervention Point 10: PKG (cGMP-Dependent Protein Kinase) — Merozoite Egress Blockade

**Target/mechanism:** C. parvum protein kinase G (CpPKG). PKG mediates merozoite egress from host cells. Silencing PKG significantly inhibits egress and leads to retention of intracellular parasites within host cells. If merozoites cannot egress, the 12-14h amplification cycle is broken — parasites complete replication but cannot spread.

**Disease stage:** Stage 4 (Merogony — specifically, the egress step between cycles)

**Kill-chain:**
1. A PKG inhibitor reaches the parasite niche [ASSUMPTION — PKG inhibitors exist for Plasmodium and Toxoplasma; compound 1/compound 2 from the Merck series. CpPKG may be targetable by similar scaffolds]
2. CpPKG inhibition prevents phosphorylation of egress-associated substrates [ESTABLISHED — PKG silencing retains merozoites intracellularly]
3. Merozoites remain trapped within host cells [ESTABLISHED]
4. Trapped merozoites cannot invade new host cells = amplification stops [INFERRED]
5. Existing infected cells eventually die (normal enterocyte turnover ~3-5 days) and parasites are lost [INFERRED — enterocyte turnover at villus tips is rapid]
6. Without new invasion, autoinfection-derived sporozoites also fail to amplify [INFERRED]

**Weakest link:** Steps 1-2 — whether existing apicomplexan PKG inhibitors have adequate potency against CpPKG. PKG is highly conserved across apicomplexa, which means existing Plasmodium PKG inhibitors may cross-react, but the extracytoplasmic niche creates a drug delivery challenge that Plasmodium (fully intracellular) does not face.

**Magnitude estimate:** If egress fully blocked: >90% disease reduction (amplification halts). Combined with normal enterocyte turnover, parasites would be physically shed from villus tips within 3-5 days even without immune clearance.

**Falsifiable prediction:** A Plasmodium PKG inhibitor (compound 2 / ML10) will show cross-activity against CpPKG in an in vitro kinase assay with IC50 <1 micromolar, and will reduce merozoite egress in C. parvum-infected HCT-8 cells by >70% at 10 micromolar. Test: standard kinase assay with recombinant CpPKG + cell-based egress assay.

**Closest analogy:** Plasmodium PKG inhibitors. ML10 and related compounds block PfPKG-mediated merozoite egress in blood-stage malaria. CpPKG is the direct homolog.

---

### Intervention Point 11: Kinesin-5/Eg5 Inhibition — Microtubule-Dependent Secretion Blockade

**Target/mechanism:** Kinesin-5/Eg5 motor protein. A 2024 study showed that micronemal protein CpTSP4 secretion depends on intracellular trafficking through Cryptosporidium-unique microtubules that can be blocked by kinesin-5/Eg5 inhibitors. Microneme secretion is essential for invasion — without it, the parasite cannot deploy adhesins needed for host cell attachment and entry.

**Disease stage:** Stage 2 (Invasion — secretory organelle deployment)

**Kill-chain:**
1. A kinesin-5/Eg5 inhibitor (e.g., monastrol, ispinesib) reaches the parasite niche [ASSUMPTION — these compounds exist as anticancer drugs; selectivity for parasite kinesin over host kinesin is the question]
2. Inhibitor blocks microtubule-dependent trafficking of microneme proteins to the parasite surface [ESTABLISHED — demonstrated for CpTSP4]
3. Without microneme secretion, sporozoites/merozoites cannot deploy adhesins (CSL, GP40/GP15, TRAP-C1, CpTSP4) [INFERRED — microneme deployment is required for invasion in all apicomplexa]
4. Without adhesin deployment, invasion cannot proceed [ESTABLISHED — anti-adhesin antibodies block invasion]
5. Amplification cycle stops at each invasion step [INFERRED]

**Weakest link:** Step 1 — Kinesin-5 is a host cell protein also involved in mitosis. Inhibiting host Eg5 in rapidly dividing intestinal crypt cells would be toxic. The key question is whether C. parvum uses a PARASITE kinesin (not host) for microneme trafficking. The 2024 study mentions "Cryptosporidium-unique microtubules," suggesting parasite-derived structures, but whether the kinesin motors are parasite-encoded or co-opted from the host is unclear. If the kinesin is parasite-encoded, there may be structural differences enabling selectivity.

**Magnitude estimate:** If parasite-specific kinesin is selectively targetable: 60-80% disease reduction. If host kinesin must be inhibited: unacceptable toxicity.

**Falsifiable prediction:** C. parvum encodes at least one kinesin-5 homolog (distinct from human KIF11/Eg5) that localizes to the apical complex microtubules and is required for microneme secretion. Test: bioinformatic search of C. parvum genome for kinesin-5 family members; localization by epitope tagging.

**Closest analogy:** Kinesin inhibitors in cancer (ispinesib, filanesib). The question is whether parasite-selective kinesins exist.

---

## DOMAIN 4: REDUCED-GENOME METABOLIC BOTTLENECKS

C. parvum has ~3,800 genes — the most reduced genome of any apicomplexan. It has LOST nearly all biosynthetic capacity. The few essential enzymes that remain are obligate bottlenecks with no alternative pathway.

---

### Intervention Point 12: CpIMPDH — The Bacterial-Origin Nucleotide Bottleneck

**Target/mechanism:** Inosine monophosphate dehydrogenase (CpIMPDH), acquired by lateral gene transfer from an epsilon-proteobacterium. CpIMPDH is essential for guanine nucleotide synthesis via the salvage pathway (IMP -> XMP -> GMP). Without GMP, the parasite cannot synthesize DNA, RNA, or GTP-dependent signaling molecules. CpIMPDH is structurally distinct from human IMPDH (it resembles bacterial IMPDH), enabling selective inhibition.

**Disease stage:** Stage 4 (Merogony — DNA replication for merozoite production)

**Kill-chain:**
1. A CpIMPDH-selective inhibitor reaches the parasite [ASSUMPTION — multiple selective inhibitors exist: benzimidazoles, benzoxazoles, triazoles, urea-based compounds. Delivery to the extracytoplasmic niche requires luminal or transcellular access]
2. CpIMPDH inhibition blocks conversion of IMP to XMP [ESTABLISHED — crystal structures show inhibitor binding; IC50 values in nanomolar range]
3. Without XMP, GMP synthesis halts [ESTABLISHED — no alternative pathway in C. parvum; no de novo purine synthesis exists]
4. Without GMP, the parasite cannot replicate DNA for merogony [ESTABLISHED — GTP is required for DNA synthesis, translation (as GTP), and signaling]
5. Merogony halts — merozoite production stops [INFERRED]
6. Amplification cycle broken [INFERRED]

**Weakest link:** Step 1 — delivery. CpIMPDH inhibitors have been developed and characterized in vitro, but in vivo efficacy in animal models has been limited. The question is whether sufficient drug concentrations reach the parasite in the extracytoplasmic niche. The selective inhibitors developed by Hedstrom's lab are potent in vitro but have not demonstrated breakthrough efficacy in vivo.

**Magnitude estimate:** If drug delivery challenge is solved: >80% parasite burden reduction. The target is validated, the selectivity is established, the bottleneck is real. This is an execution problem (delivery), not a target validation problem.

**Falsifiable prediction:** A CpIMPDH inhibitor formulated as a non-absorbable oral suspension (reaching the parasite via luminal access through the PVM) will achieve >10x better in vivo efficacy than the same compound formulated for systemic absorption. Test: compare oral non-absorbable vs. oral absorbable formulations of the same CpIMPDH inhibitor in infected mice; measure oocyst output reduction.

**Closest analogy:** Mycophenolic acid (human IMPDH inhibitor) as an immunosuppressant. Same enzyme family, but selectivity is in the opposite direction — CpIMPDH inhibitors must spare human IMPDH.

---

### Intervention Point 13: CpFAS1 Megasynthase — Very Long Chain Fatty Acid Supply for Oocyst Walls

**Target/mechanism:** CpFAS1, a giant Type I fatty acid synthase (8,243 amino acids, 21 enzymatic domains). CpFAS1 does NOT synthesize fatty acids de novo — it ELONGATES host-derived medium/long-chain fatty acids to very long chain fatty acids (C20-C26+). These VLCFAs are likely structural components of the oocyst wall. CpFAS1 is structurally distinct from human Type I FAS and has substrate specificity for very long chain acyl-CoAs.

**Disease stage:** Stage 5 (Oocyst Formation — wall biosynthesis)

**Kill-chain:**
1. A CpFAS1 ketosynthase (KS) domain inhibitor blocks VLCFA elongation [ASSUMPTION — cerulenin inhibits CpFAS1-KS with IC50 ~1.5 micromolar; improved selective inhibitors could be designed]
2. Without VLCFAs, oocyst wall lipid composition is deficient [INFERRED — VLCFAs are proposed structural components of the wall's inner lipid layer]
3. Deficient oocyst walls fail to properly assemble [INFERRED]
4. Thin-walled oocysts (already single-membrane) may be more vulnerable than thick-walled oocysts to CpFAS1 inhibition [SPECULATION — if VLCFAs contribute to even the minimal thin-walled oocyst membrane]
5. Malformed oocysts = reduced autoinfection + reduced transmission [INFERRED]

**Weakest link:** Step 2 — the exact role of VLCFAs in oocyst wall structure is INFERRED, not established. If VLCFAs are not actually oocyst wall components (but rather membrane components used during intracellular development), then the effect would be different — potentially more broadly lethal to all stages, or potentially tolerated if the parasite can import VLCFAs from the host.

**Magnitude estimate:** Highly uncertain. If VLCFAs are essential for oocyst wall integrity: 40-70% disease reduction (blocks autoinfection and transmission). If VLCFAs are essential for all membrane functions: potentially >80% (broader effect on parasite viability).

**Falsifiable prediction:** CpFAS1-KS inhibition (by cerulenin or improved compound) will cause dose-dependent reduction in OOCYST output without proportional reduction in asexual parasite burden, because VLCFAs are primarily needed for wall formation, not for asexual membrane biogenesis. Test: cerulenin dose-response in C. parvum cell culture measuring both parasite DNA (qPCR, all stages) and oocyst-specific markers (immunofluorescence for COWP) at 72 hours.

**Closest analogy:** Fatty acid synthase inhibitors in cancer (TVB-2640 / denifanstat). Same enzyme family, different substrate specificity, but the inhibitor design principles are directly transferable.

---

### Intervention Point 14: Trehalose-6-Phosphate Synthase — The Stress Protectant Pathway

**Target/mechanism:** Trehalose-6-phosphate synthase/phosphatase (T6PS-TPase), a bifunctional enzyme that synthesizes trehalose. Trehalose is a stress protectant found in C. parvum oocysts. T6PS-TPase expression is highly elevated in late intracellular development (prior to or during oocyst production), implying trehalose is critical for oocyst environmental survival. This is a plant-type pathway ABSENT from mammals.

**Disease stage:** Stage 5 (Oocyst Formation) and Stage 1 (Environmental Persistence)

**Kill-chain:**
1. A T6PS inhibitor blocks trehalose synthesis in the parasite [ASSUMPTION — T6PS inhibitors have been developed for fungal pathogens; the plant-type enzyme in C. parvum may be targetable by similar scaffolds]
2. Without trehalose, oocysts lack stress protectant [INFERRED — trehalose protects against desiccation, heat, and oxidative stress in other organisms]
3. Thick-walled oocysts shed into the environment have reduced survival [INFERRED — environmental persistence may decrease from months to days/hours]
4. Thin-walled oocysts within the host may also be affected — if trehalose stabilizes sporozoites during autoinfection excystation [SPECULATION]
5. Reduced environmental oocyst survival = reduced R0 over multiple calving cycles [INFERRED]

**Weakest link:** Step 2-3 — whether trehalose is truly essential for oocyst survival. Oocyst walls also have mechanical protection (COWPs, lipid layers). Trehalose may provide only marginal additional stress protection, and its loss might not meaningfully reduce environmental persistence. Additionally, this pathway affects oocyst QUALITY, not oocyst QUANTITY — disease in the individual calf might be unaffected.

**Magnitude estimate:** For individual calf disease: <10% (trehalose inhibition doesn't stop infection or reduce parasite burden). For herd-level R0 over multiple seasons: potentially 20-40% reduction (if oocyst environmental half-life decreases from months to weeks). This is a TRANSMISSION CONTROL target, not a TREATMENT target.

**Falsifiable prediction:** Oocysts produced by T6PS-inhibited parasites will show >10-fold reduced viability after 7 days at 20 degrees C compared to normal oocysts, while their infectivity immediately after shedding will be equivalent. Test: produce oocysts from T6PS-inhibitor-treated vs. untreated cultures; compare immediate infectivity vs. 7-day environmental survival.

**Closest analogy:** Trehalose-6-phosphate synthase inhibitors in Mycobacterium tuberculosis (OtsA/OtsB). The TB field has pursued trehalose synthesis as a drug target for similar reasons.

---

### Intervention Point 15: Dual aminoacyl-tRNA Synthetase Inhibition — Overcoming Resistance by Combination

**Target/mechanism:** Simultaneous inhibition of TWO aminoacyl-tRNA synthetases (aaRS). C. parvum has multiple aaRS validated as drug targets: prolyl-tRNA synthetase (CpProRS, target of halofuginone), phenylalanyl-tRNA synthetase (CpPheRS, target of bicyclic azetidines), lysyl-tRNA synthetase (CpKRS), and methionyl-tRNA synthetase (CpMetRS). A critical finding from the disease map: a methionyl-tRNA synthetase inhibitor FAILED in a dairy calf trial because resistant C. parvum with target gene mutations emerged within DAYS. This reveals that single-aaRS inhibitors face a resistance catastrophe — the parasite's rapid replication (8 merozoites per 12-14h cycle) generates mutations fast enough to escape single-target pressure.

The intervention: combine TWO aaRS inhibitors (e.g., halofuginone/ProRS + BRD7929/PheRS) to require simultaneous resistance mutations in two unlinked genes. The probability of dual resistance is the product of individual probabilities — if single resistance frequency is ~10^-6, dual resistance is ~10^-12, which exceeds the total parasite population in a single calf.

**Disease stage:** Stage 4 (Merogony — protein synthesis during replication)

**Kill-chain:**
1. Two aaRS inhibitors with non-overlapping targets are co-administered [ASSUMPTION — drug-drug interactions and combined toxicity must be acceptable]
2. Each inhibitor independently blocks charging of its cognate amino acid [ESTABLISHED — ProRS inhibition by halofuginone is established; PheRS inhibition by BRD7929 is established]
3. Without charged tRNAs, translation halts [ESTABLISHED — standard biochemistry]
4. Without protein synthesis, merogony fails — merozoites cannot be produced [INFERRED]
5. Dual-target requirement prevents resistance emergence [ESTABLISHED — combinatorial barrier to resistance is a fundamental principle of antimicrobial therapy]

**Weakest link:** Step 1 — combined toxicity. Halofuginone at effective doses causes gastrointestinal side effects. Adding a second aaRS inhibitor may compound toxicity. However, the combination could enable lower doses of each agent (sub-MIC monotherapy doses that are synergistic in combination), reducing individual toxicity.

**Magnitude estimate:** If resistance is the primary reason for single-aaRS failure: >80% efficacy improvement over monotherapy. If the primary failure mode is delivery/pharmacokinetics rather than resistance: <20% improvement.

**Falsifiable prediction:** Halofuginone + BRD7929 at 50% monotherapy MIC each will achieve >90% parasite reduction in cell culture AND will NOT generate resistant parasites in serial passage (through 20 passages), while each compound at monotherapy MIC alone will generate resistance within 5-10 passages. Test: serial passage resistance generation assay comparing monotherapy vs. combination at equi-effective doses.

**Closest analogy:** TB multi-drug therapy. The principle that combination therapy prevents resistance is the foundation of all mycobacterial treatment. Applying it to C. parvum aaRS inhibitors is directly analogous.

---

## SYSTEM-LEVEL VULNERABILITIES

### System Vulnerability 1: The Autoinfection Positive Feedback Loop

**Description:** The thin-walled oocyst autoinfection cycle is a positive feedback loop: infection -> merogony -> gametogony -> thin-walled oocysts (20%) -> excystation in gut -> reinvasion -> MORE infection. This loop means that infection intensity increases over time EVEN WITHOUT new environmental exposure. Breaking this loop at ANY point collapses the feedback.

**Interventions that break the loop:**
- Myb-M inhibition (no oocysts produced at all) = loop broken at gametogony
- AP2-F inhibition (no functional oocyst walls) = loop broken at oocyst formation
- COWP disulfide bond disruption (malformed oocyst walls) = loop broken at oocyst integrity
- Continuous luminal anti-invasion agent (prevent autoinfection sporozoite reinvasion) = loop broken at reinvasion

**Key insight:** Breaking autoinfection does NOT require killing the parasite. It only requires disrupting ONE step in the oocyst formation/excystation/reinvasion sequence. Once autoinfection stops, the existing intracellular parasite population is finite and will be cleared by the developing adaptive immune response (which the disease map confirms is effective — just slow).

### System Vulnerability 2: The Asexual-to-Sexual Commitment Decision

**Description:** The parasite undergoes approximately 3 asexual cycles before committing to sexual development. This commitment is controlled by a transcription factor cascade (Myb-M for males, AP2-F for females). The decision point is a one-way gate — once committed to sexual development, the parasites are terminally differentiated and cannot revert to asexual amplification.

**The strategic implication:** If the commitment decision could be FORCED prematurely (driving all parasites into terminal sexual differentiation before sufficient amplification), the parasite population would self-limit. The 2024 finding that forced Myb-M overexpression drives ALL parasites into terminally differentiated males (ablating further replication and growth) demonstrates this is biologically possible.

**Intervention:** A compound that activates Myb-M expression or stabilizes Myb-M protein would force premature male commitment, creating a "death switch" — the parasite terminally differentiates and cannot sustain asexual amplification.

---

## INTERVENTION POINT RANKING (by estimated impact and druggability)

| Rank | Intervention Point | Domain | Impact | Druggability | Priority |
|------|-------------------|--------|--------|-------------|----------|
| 1 | **Myb-M inhibition** (or forced activation) | Sexual checkpoint | >95% | MEDIUM (TF targeting is hard but precedented) | HIGH |
| 2 | **PKG egress blockade** | Invasion/Egress | >90% | HIGH (kinase, existing inhibitors) | HIGH |
| 3 | **Aldolase inhibition** | Feeder organelle | >90% | MEDIUM (selectivity challenge) | HIGH |
| 4 | **CpIMPDH inhibition** (luminal formulation) | Metabolic bottleneck | >80% | HIGH (validated, selective inhibitors exist) | HIGH |
| 5 | **AP2-F inhibition** | Sexual checkpoint | 50-90% | MEDIUM (plant-type TF, absent in mammals) | MEDIUM-HIGH |
| 6 | **Dual aaRS combination** | Metabolic bottleneck | >80% | HIGH (compounds exist) | MEDIUM-HIGH |
| 7 | **Glycogen phosphorylase** | Feeder organelle | 30-50% mono | HIGH (druggable enzyme class) | MEDIUM |
| 8 | **CpROM1 rhomboid protease** | Invasion | 70-90% | MEDIUM (intramembrane protease) | MEDIUM |
| 9 | **Host Cdc42/Arp2/3 blockade** | Invasion | 30-60% | LOW (host toxicity) | LOW-MEDIUM |
| 10 | **CpFAS1 megasynthase** | Metabolic | 40-70% | MEDIUM (unique enzyme) | MEDIUM |
| 11 | **Dual CpGT1+GT2 blockade** | Feeder organelle | 50-70% | LOW (selectivity over host GLUTs) | LOW-MEDIUM |
| 12 | **CDPK5 kinase** | Sexual checkpoint | 40-60% | MEDIUM (kinase) | LOW-MEDIUM |
| 13 | **Kinesin-5/Eg5 blockade** | Invasion | 60-80% | LOW (host toxicity concern) | LOW |
| 14 | **CpABC1 transporter** | Feeder organelle | 30-80% | LOW (cargo unknown) | LOW |
| 15 | **T6PS-TPase** | Oocyst survival | <10% individual | MEDIUM (plant-type) | LOW |

---

## NOVEL CONTRIBUTIONS (what first-principles adds beyond standard literature)

1. **Myb-M as a drug target** — while the 2024 genetic discovery is published, the DRUG TARGET framing (small molecule inhibitor or forced activator creating a parasitic "death switch") is a first-principles inference, not a published therapeutic strategy. The forced activation concept (driving premature terminal male differentiation via Myb-M stabilization) is completely novel.

2. **Aldolase as the non-redundant glycolytic chokepoint** — the 2024 genetic data shows CpGT1, CpGT2, and hexokinase are all individually dispensable. The standard literature focuses on glucose transporters as feeder organelle targets. First-principles analysis identifies aldolase as the convergence point that CANNOT be bypassed.

3. **Glycogen phosphorylase as a genetically validated essential target** — the 2024 data proving essentiality is recent. The therapeutic framing (targeting internal energy reserves rather than external nutrient import) has not been explored.

4. **PKG inhibitor repurposing from malaria** — CpPKG as an egress blocker has been demonstrated by silencing, but the specific proposal to test existing Plasmodium PKG inhibitors for cross-activity is a direct actionable step.

5. **Host-side Cdc42/Arp2/3 partial inhibition** — the dose-response concept (partial inhibition differentially impairing intense invasion-associated remodeling while preserving baseline cell function) is a novel therapeutic framework.

6. **Dual aaRS combination to overcome rapid resistance** — the explicit framing of single-aaRS resistance as a combinatorial barrier problem, and the specific two-drug combination proposal, addresses the methionyl-tRNA synthetase calf trial failure through a first-principles resistance-genetics lens.

---

## WHAT VULCAN SEES THAT LITERATURE-ANCHORED ANALYSIS MIGHT MISS

1. **The sexual reproduction checkpoint is underexploited.** The 2024 Myb-M and AP2-F discoveries create a completely new target space. Literature-anchored analysis would focus on CDPK1, IMPDH, and PDE1 (the existing pipeline). First-principles analysis identifies sexual commitment as the highest-impact intervention point because it simultaneously breaks autoinfection AND transmission.

2. **The feeder organelle is more redundant than expected.** Literature from before 2024 presented CpGT1/GT2 as promising feeder organelle drug targets. The 2024 genetic ablation data reveals they are individually dispensable. First-principles analysis redirects toward the non-redundant downstream enzymes (aldolase, glycogen phosphorylase).

3. **The autoinfection loop is the key amplifier, and it can be broken without killing the parasite.** Most drug development focuses on KILLING parasites. First-principles analysis shows that breaking the autoinfection cycle (by disrupting oocyst formation, not parasite viability) converts the infection from an amplifying to a self-limiting one, allowing natural immunity to clear it.

4. **Resistance will defeat single-target approaches.** The methionyl-tRNA synthetase resistance data, combined with C. parvum's extremely rapid replication rate, predicts that any single-target drug will face resistance within days of clinical use. First-principles analysis demands combination strategies from the outset.

---

*Vulcan analysis complete. 15 intervention points across 4 domains. 5 predictions appended to prediction log. Quarantine maintained throughout.*
