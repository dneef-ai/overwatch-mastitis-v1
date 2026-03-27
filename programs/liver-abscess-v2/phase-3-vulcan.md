# Phase 3 -- Vulcan First-Principles Vulnerability Analysis: Hepatic Abscessation

**Program:** Liver Abscess v2
**Agent:** Vulcan (quarantined -- disease map only, no failure analysis, no external panel)
**Date:** 2026-03-27
**Status:** Complete

---

## Quarantine Declaration

This analysis derives ONLY from `phase-1-disease-map.md`. I have not read the failure analysis, candidate list, external panel contributions, or any prior Argus program files. Every intervention point below comes from first-principles decomposition of the biology.

---

## PART I: LEUKOTOXIN (LktA) -- COMPLETE LIFECYCLE DECOMPOSITION

LktA is the primary virulence factor. It is a 336 kDa protein with no sequence homology to any other known bacterial leukotoxin, encoded by the tricistronic lktBAC operon. The disease map establishes that strains from severe (A+) abscesses produce significantly more leukotoxin (P < 0.0001). This is the master target. Below, I decompose every molecular step in its lifecycle into a separate intervention point.

---

### V1: Transcriptional Silencing of the lktBAC Operon

**Target/mechanism:** The lktBAC operon promoter region. Subsp. necrophorum produces 21.1-fold more lktA transcript than subsp. funduliforme, and the two subspecies have distinct promoter regions. Whatever regulatory elements drive this differential expression are druggable.

**Disease stage:** Stage 3 (immune evasion) -- prevents leukotoxin production before it starts.

**Key biology:**
- The lktBAC operon is the sole source of leukotoxin. No redundant pathway exists.
- Promoter differences between subspecies indicate that transcriptional regulation is a major control point for virulence.
- Environmental signals likely regulate expression: F. necrophorum transitions from commensal (low leukotoxin) to pathogen (high leukotoxin). What triggers upregulation? Candidates include: (a) LuxS/AI-2 quorum sensing (LuxS homologs are present across Fusobacterium genomes), (b) iron limitation (F. necrophorum lacks Fur and siderophore genes -- it relies on heme uptake; iron-limited growth alters metabolism), (c) anaerobic stress signals upon entering the liver, (d) host-derived signals (bile acids in portal blood, complement fragments).
- LktC has been annotated with histidine kinase and sensory transduction regulator domains -- if LktC is a two-component sensor regulator, it may directly control lktA transcription in response to environmental signals.

**Kill-chain:**
1. Identify the environmental signal(s) that upregulate lktBAC transcription [UNKNOWN -- weakest link]
2. Confirm LktC's role as a sensor/regulator (vs. acyltransferase -- see V2) [UNKNOWN]
3. Design a small molecule that blocks the sensor domain or mimics the "commensal" signal
4. Deliver to the rumen/portal system at sufficient concentration
5. F. necrophorum remains in "commensal mode" -- produces leukotoxin at 21-fold lower levels (funduliforme baseline)
6. Kupffer cells clear translocated bacteria because leukotoxin is below the killing threshold

**Weakest link:** Step 1 -- the environmental trigger for lkt upregulation is completely unknown. If multiple signals converge, blocking one may be insufficient.

**Magnitude estimate:** If transcription is reduced to funduliforme levels (21-fold), this would effectively convert all subsp. necrophorum to the virulence profile of funduliforme. Since funduliforme-only abscesses are associated with lower severity, this could reduce severe (A+) abscesses by 60-80% and overall incidence by 30-50%.

**Falsifiable prediction:** A reporter construct driven by the lktBAC promoter, exposed to panel of environmental conditions (varying iron, O2, pH, bile acids, AI-2), will identify at least one condition that upregulates expression >5-fold. If no single condition achieves this, the regulation is more complex than a single environmental switch.

**Closest analogy:** LuxS/AI-2 quorum sensing inhibitors have been shown to reduce virulence 10-fold in Haemophilus parasuis in vivo. Quorum sensing inhibition is an active drug development field with multiple compounds in preclinical stages.

---

### V2: LktC Acyltransferase Inhibition (Post-Translational Activation Blockade)

**Target/mechanism:** LktC as an acyltransferase that activates pro-LktA. In canonical RTX toxin systems, the C gene product is an acyltransferase that attaches acyl-linked fatty acids to internal lysine residues of the pro-toxin. Without acylation, RTX toxins are inactive -- they cannot form pores or interact productively with host cell membranes.

**Disease stage:** Stage 3 (immune evasion) -- produces an inactive toxin.

**Key biology:**
- The lktBAC operon has the same gene order as RTX operons (BDCA in canonical systems). In RTX systems, the activating acyltransferase is ALWAYS required.
- LktC has been annotated with BOTH histidine kinase/sensor domains AND potential acyltransferase function. These annotations are conflicting. This ambiguity is itself a critical unknown.
- If LktC IS an acyltransferase: inhibiting it would cause F. necrophorum to produce a full-length but INACTIVE 336 kDa pro-LktA. The bacterium expends all the biosynthetic energy but gets no immune evasion benefit. This is exquisitely specific -- it does not kill the bacterium, does not affect rumen ecology, and has no AMR implications.
- RTX acyltransferases use acyl-ACP as the fatty acid donor. The catalytic mechanism involves a conserved histidine residue. The active site is structurally distinct from host acyltransferases.
- LktA has NO cysteine residues -- highly unusual. This means the protein cannot form disulfide bonds. Its folding and activity are therefore entirely dependent on post-translational modifications (acylation) and calcium binding for structural stabilization.

**Kill-chain:**
1. Confirm LktC has acyltransferase activity (express recombinant LktC, test with pro-LktA substrate + acyl-ACP donor) [CRITICAL -- weakest link]
2. If confirmed, solve LktC crystal structure or generate AlphaFold3 model
3. Identify the acyl-ACP binding pocket and catalytic residues
4. Screen fragment library against the active site (SPR or thermal shift assay)
5. Optimize hit to cell-penetrant inhibitor
6. Deliver: oral dosing targeting rumen/portal system
7. F. necrophorum produces pro-LktA that is secreted but non-functional
8. Neutrophils and Kupffer cells survive, clear bacteria normally

**Weakest link:** Step 1 -- if LktC is NOT an acyltransferase (if it is purely a sensor/regulator), this entire target collapses. The dual annotation (histidine kinase vs. acyltransferase) must be resolved experimentally.

**Magnitude estimate:** If LktA requires acylation for activity (as all characterized RTX toxins do), complete LktC inhibition would produce 100% inactive leukotoxin. Effect on disease: equivalent to complete leukotoxin neutralization -- estimated 40-60% reduction in abscess incidence, >80% reduction in severe (A+) abscesses.

**Falsifiable prediction:** Recombinant LktC expressed in E. coli, when incubated with pro-LktA and acyl-ACP, will produce acylated LktA detectable by mass spectrometry (mass shift of ~250 Da per acylation site). If no mass shift is detected, LktC is not an acyltransferase.

**Closest analogy:** HlyC (E. coli hemolysin acyltransferase) has been biochemically characterized and its catalytic mechanism is well understood. No inhibitor has been developed clinically, making this a first-in-class opportunity. RTX acyltransferase inhibitors would be a novel drug class with potential across multiple RTX-producing pathogens.

---

### V3: LktB Secretion Blockade (Transport Arrest)

**Target/mechanism:** LktB, the outer membrane transporter with a POTRA2 (polypeptide transport-associated) domain. LktA is secreted via the Type 5b two-partner secretion (TPS) system. In TPS systems, the TpsB protein (here LktB) forms a beta-barrel pore in the outer membrane through which the TpsA protein (here LktA) is translocated. Blocking the LktB substrate-binding pocket would trap pro-LktA in the periplasm.

**Disease stage:** Stage 3 (immune evasion) -- prevents leukotoxin from reaching the extracellular environment.

**Key biology:**
- LktA has an N-terminal signal peptide that routes it through the Sec pathway across the inner membrane into the periplasm. From there, LktB mediates transport across the outer membrane.
- The POTRA2 domain in LktB is the substrate recognition domain -- it binds the N-terminal secretion signal of LktA.
- A 336 kDa protein trapped in the periplasm would cause PROTEOTOXIC STRESS. The periplasm is a confined space with limited proteolytic capacity. Accumulation of a massive unfolded protein could: (a) activate the sigma-E/Cpx stress response, (b) disrupt outer membrane integrity, (c) be directly bactericidal. This makes secretion blockade potentially bactericidal in addition to neutralizing the toxin.
- TPS system beta-barrels have conserved structural features. The POTRA domain has a defined binding groove that could accommodate a small molecule.

**Kill-chain:**
1. Express and purify recombinant LktB POTRA2 domain [FEASIBLE]
2. Determine crystal structure or AF3 model [FEASIBLE]
3. Map the LktA N-terminal recognition peptide binding surface [MODERATE DIFFICULTY]
4. Design a competitive inhibitor of the POTRA2-LktA interaction [MODERATE DIFFICULTY]
5. Deliver orally; compound must survive rumen environment and reach F. necrophorum in the rumen wall or liver [WEAKEST LINK]
6. LktA accumulates in periplasm -> proteotoxic stress + no extracellular leukotoxin
7. Bacteria either die from stress or survive but cannot evade immune system

**Weakest link:** Step 5 -- delivery. An inhibitor must reach F. necrophorum cells in the rumen wall (anaerobic, low pH) or in the liver (post-translocation). Oral delivery to the rumen is feasible; reaching bacteria inside rumen wall tissue is harder.

**Magnitude estimate:** Complete secretion blockade = zero extracellular leukotoxin + potential direct bactericidal effect. If achieved: 50-70% reduction in abscess incidence. Proteotoxic stress adds value beyond toxin neutralization alone.

**Falsifiable prediction:** In a periplasmic accumulation assay, LktB-deficient F. necrophorum mutants (lktB knockout) will show: (a) no extracellular leukotoxin, (b) detectable intracellular/periplasmic LktA accumulation, and (c) reduced growth rate compared to wild-type. If growth rate is unaffected, the proteotoxic stress hypothesis is wrong.

**Closest analogy:** POTRA domain inhibitors have been explored for BamA (the essential beta-barrel assembly machinery) in Gram-negative bacteria. The structural biology is well established. No clinical inhibitors yet exist for any TPS system, making this first-in-class.

---

### V4: Extracellular Calcium Chelation (Conformational Arrest)

**Target/mechanism:** Calcium-dependent conformational activation of LktA. Although LktA lacks classic RTX glycine-rich nonapeptide repeats (it has no sequence homology to other leukotoxins), it is heat-labile (56 C/5 min) and pH-sensitive (inactivated at >7.8 or <6.6), suggesting a conformational activation step. If calcium binding is required for LktA to adopt its active conformation (as in all characterized RTX toxins), then local calcium chelation in the hepatic microenvironment could prevent toxin activation.

**Disease stage:** Stage 3 (immune evasion) -- prevents already-secreted leukotoxin from becoming active.

**Key biology:**
- LktA stability window: pH 6.6-7.8. Hepatic sinusoidal blood is pH ~7.4 (within the active range). Rumen fluid is pH 5.0-6.5 (partially outside the active range, which may explain why leukotoxin is not maximally active in the rumen).
- Calcium concentration in portal blood is ~1.2 mM (ionized). If LktA requires Ca2+ for folding (as RTX toxins do), reducing local Ca2+ could prevent activation.
- LktA has NO cysteine residues, so the protein cannot use disulfide bonds for structural stabilization. This makes it MORE dependent on non-covalent stabilization mechanisms (calcium binding, hydrophobic packing).

**Kill-chain:**
1. Determine whether LktA activity is calcium-dependent (test cytotoxicity in calcium-depleted vs. calcium-replete media) [FEASIBLE -- weakest link]
2. If calcium-dependent, identify the calcium-binding sites on LktA (mutagenesis + structural analysis)
3. Design a locally acting calcium chelator or a peptide that competes for the calcium-binding domain
4. Deliver to the liver via portal circulation (conjugate to a liver-targeting moiety)
5. LktA is secreted but remains conformationally inactive
6. Neutrophils and Kupffer cells survive

**Weakest link:** Step 1 -- LktA has no sequence homology to other leukotoxins, so calcium dependence cannot be assumed. It must be tested directly.

**Magnitude estimate:** If confirmed and achievable, equivalent to leukotoxin neutralization: 40-60% abscess reduction. However, systemic calcium chelation is dangerous (cardiac effects), so this would require highly localized delivery -- reducing practical feasibility.

**Falsifiable prediction:** LktA cytotoxicity against bovine PMNs in vitro will be reduced by >90% when free Ca2+ is chelated to <10 uM (using EGTA), compared to standard media (~1 mM Ca2+). If activity is calcium-independent, this target is invalid.

**Closest analogy:** Calcium chelation has been used to inhibit RTX toxins in research settings. Clinically, EDTA-based wound treatments exploit metal chelation. No clinical product uses localized calcium chelation as an anti-virulence strategy.

---

### V5: Host Receptor Blockade (Receptor-Side Neutralization)

**Target/mechanism:** The host cell receptor for LktA on bovine neutrophils and Kupffer cells. The receptor is UNKNOWN -- this has been an open question for 24+ years. By analogy with Mannheimia haemolytica leukotoxin (LtxA), the receptor is likely CD18 (beta-2 integrin), since: (a) anti-CD18 antibodies reduce M. haemolytica LtxA cytotoxicity, (b) LktA shows ruminant specificity matching CD18 species-specific sequences, (c) the integrin-EGF-3 domain of bovine CD18 is critical for M. haemolytica LtxA species-specific susceptibility.

**Disease stage:** Stage 3 (immune evasion) -- blocks leukotoxin at the point of target cell engagement.

**Key biology:**
- If CD18 is the receptor, the binding site is likely in the integrin-EGF-3 domain (by analogy with M. haemolytica).
- Blocking CD18 globally would be immunosuppressive (CD18 is essential for leukocyte adhesion and extravasation). Therefore, the approach must be: (a) identify the SPECIFIC binding interface between LktA and its receptor, (b) design a blocker that interferes with LktA binding WITHOUT blocking normal integrin function, or (c) develop a decoy receptor (soluble CD18 fragment that acts as a toxin "sponge").
- A soluble decoy receptor would be a biologic (protein therapeutic), not a small molecule. But if the binding site is identified, a peptide or small molecule mimetic could be developed.

**Kill-chain:**
1. Identify the LktA receptor on bovine PMNs (pull-down with LktA as bait + mass spectrometry) [CRITICAL -- weakest link]
2. Confirm binding (co-IP, surface plasmon resonance, flow cytometry competition)
3. Map the binding interface (truncation mutants of both LktA and receptor)
4. Design a competitive inhibitor or decoy
5. Deliver systemically (IV or SC -- this targets the liver, not the rumen)
6. LktA binds decoy instead of neutrophils/Kupffer cells
7. Immune cells survive, clear bacteria

**Weakest link:** Step 1 -- receptor identification. If the receptor is NOT CD18 (if the analogy to M. haemolytica is wrong), the entire strategy must be rebuilt from scratch. The 24-year gap in knowledge suggests this is technically difficult.

**Magnitude estimate:** Complete receptor blockade = complete neutralization of leukotoxin at the target. 40-60% abscess reduction, >80% reduction in severe abscesses.

**Falsifiable prediction:** Anti-bovine CD18 monoclonal antibody (clone BAQ153A or equivalent) will reduce LktA-mediated cytotoxicity of bovine PMNs in vitro by >50% in a dose-dependent manner. If <20% reduction, CD18 is not the receptor and the M. haemolytica analogy is wrong.

**Closest analogy:** Anti-CD11a (efalizumab) was an approved human biologic for psoriasis (subsequently withdrawn for PML risk). Anti-integrin biologics are a validated drug class. Raxibacumab (anti-protective antigen of B. anthracis) is an FDA-approved toxin-targeting biologic.

---

### V6: Downstream Signaling Blockade (Caspase/NF-kB Pathway Interruption)

**Target/mechanism:** The intracellular signaling cascades activated by LktA in host leukocytes. Recent work (Frontiers in Cellular and Infection Microbiology, 2022) shows that F. necrophorum activates both the NF-kB signaling pathway and the death receptor signaling pathway in neutrophils. Specifically:
- Upregulates pro-apoptotic genes: Bax, cytochrome c, caspase-3
- Downregulates anti-apoptotic gene: Bcl-2
- Activates TNF-alpha/TNFR1/NF-kB axis
- At low dose: neutrophil activation -> degranulation -> tissue damage
- At moderate dose: apoptosis via caspase cascade
- At high dose: necrotic cell death

**Disease stage:** Stage 3-4 (immune evasion + tissue damage) -- allows leukotoxin to bind but blocks the killing signal.

**Key biology:**
- The LOW-DOSE response is arguably more damaging than the HIGH-DOSE response. Low-dose leukotoxin activates neutrophils to degranulate, producing reactive oxygen species and lysosomal enzymes that destroy surrounding hepatocytes. This creates the necrotic zone that becomes the abscess cavity. Blocking the activation signal at low dose would prevent this tissue-damage amplification loop.
- Caspase-8 is upstream in the death receptor pathway. Caspase-3 is the executioner. Either could be targeted.
- NF-kB activation drives inflammatory cytokine production (IL-1beta, TNF-alpha, IL-6) which recruits more neutrophils to be killed by more leukotoxin -- a positive feedback loop.

**Kill-chain:**
1. Map the LktA signaling cascade in bovine PMNs (kinase/phosphatase inhibitor panel + flow cytometry) [MODERATE DIFFICULTY]
2. Identify the earliest divergence point (where LktA signaling diverges from normal immune signaling) [WEAKEST LINK]
3. Design an inhibitor of the divergence point
4. Deliver systemically
5. Neutrophils survive leukotoxin exposure, do not degranulate inappropriately, clear bacteria normally
6. Tissue damage loop is broken

**Weakest link:** Step 2 -- if LktA uses the same signaling pathways as normal immune activation (e.g., if it simply activates CD18 in an exaggerated way), then blocking the signaling would also block normal immune function. The intervention only works if there is a SPECIFIC pathway activated by LktA that is dispensable for normal immunity.

**Magnitude estimate:** If a specific pathway can be identified and blocked: 30-50% reduction in abscess formation (primarily by reducing tissue damage and breaking the amplification loop). Less effective than preventing leukotoxin production entirely, but addresses the tissue-damage component.

**Falsifiable prediction:** Bovine PMNs pre-treated with a pan-caspase inhibitor (z-VAD-FMK) will show >80% survival when exposed to moderate-dose LktA (a dose that kills >80% of untreated PMNs), but will still mount a normal respiratory burst in response to opsonized bacteria. If caspase inhibition also blocks normal antimicrobial function, this target has unacceptable collateral damage.

**Closest analogy:** Emricasan (pan-caspase inhibitor) was in human clinical trials for liver disease (NASH). Caspase inhibition in the liver is a validated concept. NF-kB inhibitors are an active pharmaceutical development area.

---

## PART II: SECONDARY VIRULENCE FACTORS -- DECOMPOSITION

---

### V7: FomA-Mediated Complement Evasion -- Factor H Decoy

**Target/mechanism:** FomA (42.4 kDa OMP) binds Factor H, the host complement inhibitor. This is a confirmed complement evasion mechanism: F. necrophorum captures Factor H on its surface, which acts as a cofactor for Factor I to cleave C3b, preventing complement-mediated killing. In Lemierre's syndrome patients, strains with the strongest Factor H binding had the most severe symptoms.

**Disease stage:** Stage 3 (immune evasion) -- a leukotoxin-independent immune evasion mechanism.

**Key biology:**
- Factor H binding is ionic and specific, occurring via both N-terminal and C-terminal sites on Factor H.
- Bound Factor H remains FUNCTIONALLY ACTIVE as a cofactor for Factor I.
- FomA also mediates adhesion to bovine endothelial cells. Anti-FomA antibodies prevent bacterial attachment.
- This is a DUAL-FUNCTION target: blocking FomA simultaneously removes complement evasion AND endothelial adhesion.

**Kill-chain:**
1. Solve FomA structure (or AF3 model) [FEASIBLE]
2. Map the Factor H binding interface on FomA [MODERATE DIFFICULTY]
3. Design a competitive inhibitor that occupies the Factor H binding pocket on FomA
4. Alternatively: develop anti-FomA antibody that blocks both Factor H binding and endothelial adhesion [FEASIBLE -- weakest link is delivery/durability]
5. F. necrophorum loses complement protection -> complement-mediated killing in hepatic sinusoids
6. Simultaneously loses endothelial adhesion -> reduced colonization of portal vasculature

**Weakest link:** Determining whether complement evasion via Factor H binding is quantitatively important in the liver microenvironment. This was demonstrated in Lemierre's syndrome (human bloodstream infection) but has not been confirmed in bovine liver abscesses.

**Magnitude estimate:** If Factor H binding is important for hepatic survival: 20-40% reduction in abscess incidence (additive with leukotoxin-targeting approaches). The dual adhesion/complement function makes this more attractive than a single-mechanism target.

**Falsifiable prediction:** F. necrophorum pre-incubated with anti-FomA antibody (or FomA-binding peptide) will show >3-fold increased susceptibility to complement-mediated killing in bovine serum compared to untreated bacteria. If <1.5-fold, complement evasion via Factor H is not the dominant complement resistance mechanism.

**Closest analogy:** Factor H binding is used by Neisseria meningitidis (fHbp), and fHbp is the target of the licensed MenB vaccines (Bexsero, Trumenba). This is a validated vaccine strategy with clinical precedent.

---

### V8: Hemagglutinin-Mediated Adhesion Blockade

**Target/mechanism:** The 19 kDa hemagglutinin surface protein that mediates F. necrophorum adhesion to ruminal epithelial cells. Critical observation from the disease map: hemagglutinin activity is present in ALL hepatic isolates of subsp. necrophorum but only SOME ruminal isolates. This means hemagglutinin is selected for during the commensal-to-pathogen transition -- it is a virulence gatekeeper.

**Disease stage:** Stage 2 (colonization) -- prevents rumen wall adhesion.

**Key biology:**
- Anti-hemagglutinin antiserum reduces bacterial attachment in vitro.
- The hemagglutinin also mediates platelet aggregation, contributing to microthrombus formation in the liver.
- The protein is only 19 kDa -- small enough for straightforward recombinant expression and structural characterization.
- If all liver-origin strains are hemagglutinin-positive, then hemagglutinin is a NECESSARY (not just contributing) factor for pathogenicity.

**Kill-chain:**
1. Purify recombinant hemagglutinin [FEASIBLE]
2. Identify the epithelial cell binding domain [MODERATE]
3. Design a competitive inhibitor (peptide or small molecule that mimics the epithelial receptor) [MODERATE]
4. Deliver to the rumen (oral, rumen-stable formulation) [FEASIBLE -- weakest link is rumen stability]
5. F. necrophorum cannot adhere to damaged rumen epithelium
6. Without adhesion, no rumen wall penetration, no portal transit
7. Disease is blocked at Stage 2 -- upstream of all other virulence factors

**Weakest link:** Adhesion redundancy. The disease map lists multiple adhesins: hemagglutinin, 43K OMP (fibronectin binding), FadA, OmpA, OmpH. If adhesion is redundant (any one of these is sufficient), blocking hemagglutinin alone will not work.

**Magnitude estimate:** If hemagglutinin is the dominant (non-redundant) adhesin for rumen wall colonization: 50-70% reduction in rumen wall F. necrophorum load, translating to 30-50% reduction in abscess incidence. If adhesion is redundant: <10% effect.

**Falsifiable prediction:** A hemagglutinin-negative mutant of F. necrophorum subsp. necrophorum (generated by gene deletion) will show >80% reduced adhesion to bovine rumen epithelial explants compared to wild-type. If reduction is <30%, other adhesins compensate and hemagglutinin is not the dominant adhesin.

**Closest analogy:** FimH adhesin inhibitors (mannosides) for uropathogenic E. coli have entered clinical trials. Anti-adhesion therapy is a validated therapeutic strategy.

---

### V9: Hemolysin (Phospholipase B) Inhibition -- Oxygen Deprivation Blockade

**Target/mechanism:** The hemolysin of F. necrophorum, which functions as a phospholipase B (PLB) targeting phosphatidylcholine on erythrocyte membranes. By lysing erythrocytes, hemolysin serves two critical functions: (a) liberates heme/iron for the pathogen (F. necrophorum lacks siderophores -- heme is its primary iron source), (b) creates local anaerobiosis by removing oxygen-carrying erythrocytes.

**Disease stage:** Stage 4 (abscess formation) -- maintains the anaerobic niche.

**Key biology:**
- Phospholipase B has defined catalytic mechanism amenable to inhibitor design.
- The hemolysin co-purifies with leucocidin activity -- it may be a secondary leukotoxin.
- Species selectivity: strong lysis of rabbit/human/dog erythrocytes but only TRACE activity against bovine erythrocytes. This is counterintuitive -- if the bovine is the natural host, why low activity against bovine RBCs? Possible explanations: (a) bovine erythrocytes have different phosphatidylcholine composition, (b) the hemolysin's primary function is not RBC lysis but something else (phospholipid metabolism, membrane disruption of non-erythrocyte cells).
- The low bovine erythrocyte activity suggests hemolysin may be less important for bovine liver abscess than for other Fusobacterium infections.

**Kill-chain:**
1. Confirm hemolysin is a phospholipase B with defined substrate specificity [ESTABLISHED]
2. Determine whether hemolysin is essential for anaerobic niche maintenance in the bovine liver [WEAKEST LINK -- unclear given low bovine RBC lysis]
3. Identify the catalytic residues of the PLB [FEASIBLE]
4. Screen phospholipase inhibitors (e.g., MAFP, bromoenol lactone) for activity against F. necrophorum hemolysin
5. Deliver to the liver
6. Without hemolysin: reduced iron acquisition + compromised anaerobic niche
7. F. necrophorum growth rate in the aerobic liver is reduced; immune clearance succeeds

**Weakest link:** Step 2 -- the low activity against bovine erythrocytes calls into question whether hemolysin is important in cattle. It may be a vestigial virulence factor or primarily active against non-erythrocyte targets.

**Magnitude estimate:** Uncertain. If hemolysin is critical for anaerobic niche maintenance: 20-30% reduction in abscess persistence. If it is not important in cattle: <5% effect.

**Falsifiable prediction:** A hemolysin-deficient mutant of F. necrophorum will show reduced growth in aerobic or microaerobic bovine liver homogenate (>1 log reduction at 24h) compared to wild-type. If growth is equivalent, hemolysin is not essential for hepatic survival.

**Closest analogy:** Phospholipase A2 inhibitors (varespladib) are in clinical development for snakebite. Phospholipase inhibition is a validated drug target class.

---

### V10: Pyolysin (T. pyogenes) -- Cholesterol-Dependent Cytolysin Inhibition

**Target/mechanism:** Pyolysin (Plo), the cholesterol-dependent cytolysin (CDC) from Trueperella pyogenes, the primary synergistic pathogen. Pyolysin forms transmembrane pores in host cell membranes by binding cholesterol. It does NOT require thiol activation (unlike most CDCs), making it constitutively active.

**Disease stage:** Stage 4 (abscess formation) -- breaks the polymicrobial synergy.

**Key biology:**
- T. pyogenes is present in 29% of liver abscesses. Abscesses with T. pyogenes are larger and more severe.
- T. pyogenes is a facultative anaerobe -- it consumes oxygen, creating conditions for F. necrophorum. Without T. pyogenes, the anaerobic niche is harder to establish.
- Pyolysin induces pyroptosis via NLRP3/caspase-1/gasdermin D pathway -- additional inflammatory damage.
- ESTABLISHED INHIBITOR: Dynasore (a dynamin GTPase inhibitor) protects cells against pyolysin at 10 uM by reducing cellular cholesterol and disrupting lipid rafts. Methyl-beta-cyclodextrin (cholesterol chelator) is a specific inhibitor.
- Isoprenoids (mevalonate pathway intermediates) increase cellular tolerance to pyolysin by altering membrane composition.

**Kill-chain:**
1. T. pyogenes is present in the polymicrobial community [ESTABLISHED in 29% of abscesses]
2. Pyolysin creates additional tissue destruction and inflammatory damage [ESTABLISHED]
3. A CDC inhibitor (small molecule targeting pyolysin pore formation or membrane cholesterol) reduces T. pyogenes contribution [FEASIBLE -- proof of concept with Dynasore]
4. Without pyolysin: T. pyogenes loses its cytolytic capability, oxygen consumption alone is insufficient for synergy
5. Reduced abscess severity (not necessarily incidence -- F. necrophorum can still initiate abscess)

**Weakest link:** T. pyogenes is only present in 29% of abscesses. Targeting it only helps in that subset. Also, the synergy mechanism involves multiple T. pyogenes factors (pyolysin, neuraminidases, fimbriae, biofilm) -- pyolysin alone may be insufficient.

**Magnitude estimate:** In the 29% of abscesses with T. pyogenes: 30-50% reduction in abscess severity (A+ to A). Population-level: ~10-15% reduction in severe abscesses. Modest standalone, but valuable as part of a combination.

**Falsifiable prediction:** In an in vitro co-culture system (F. necrophorum + T. pyogenes in bovine liver explants), addition of Dynasore (10 uM) will reduce the zone of necrosis by >40% compared to untreated controls. If <10% reduction, pyolysin is not the dominant synergy factor.

**Closest analogy:** CDC inhibitors are in development for Clostridium perfringens (epsilon toxin inhibitors for MS). Cholesterol-dependent mechanisms are a well-characterized drug target class.

---

### V11: T. pyogenes Neuraminidase Inhibition -- Breaking the Carbon Source

**Target/mechanism:** NanH and NanP neuraminidases of T. pyogenes. These enzymes remove sialic acid from host glycoproteins, serving dual functions: (a) expose underlying adhesion receptors, and (b) provide sialic acid as a carbon/nitrogen source for bacterial growth. Sialidase inhibitors are an established drug class (oseltamivir, zanamivir for influenza).

**Disease stage:** Stage 4 (abscess formation + polymicrobial synergy).

**Key biology:**
- Bacterial sialidases have different active site geometry than viral neuraminidases, but the catalytic mechanism is conserved (oxocarbenium ion intermediate).
- Selective inhibitors against bacterial sialidases have been explored for antibacterial action.
- Removing the sialic acid carbon source would starve T. pyogenes of an energy source, reducing its growth within the abscess.
- Removing the adhesion-enhancing function would reduce T. pyogenes colonization of the abscess cavity.

**Kill-chain:**
1. Confirm NanH/NanP are essential for T. pyogenes contribution to abscess severity [WEAKEST LINK]
2. Screen existing sialidase inhibitor scaffolds against recombinant NanH/NanP
3. Identify selective bacterial sialidase inhibitors that spare host sialidases
4. Deliver to the liver
5. T. pyogenes loses adhesion enhancement and carbon source
6. Reduced polymicrobial synergy

**Weakest link:** Step 1 -- neuraminidases may be dispensable if T. pyogenes has alternative adhesion and nutrition mechanisms.

**Magnitude estimate:** Population-level: ~5-10% reduction in severe abscesses (affects only the T. pyogenes-positive subset, and only the neuraminidase-dependent component). Low standalone value.

**Falsifiable prediction:** A nanH/nanP double mutant of T. pyogenes will show >50% reduced co-colonization with F. necrophorum in an ex vivo liver abscess model compared to wild-type T. pyogenes.

**Closest analogy:** Oseltamivir/zanamivir (influenza sialidase inhibitors) are multi-billion-dollar drugs. Bacterial sialidase inhibitors are in preclinical development.

---

## PART III: SYSTEM-LEVEL VULNERABILITIES

---

### V12: The Leukotoxin Amplification Loop -- Breaking the Positive Feedback

**Target/mechanism:** The self-amplifying feedback loop that drives abscess expansion:

```
Leukotoxin (low dose) -> Neutrophil ACTIVATION -> Degranulation ->
  Tissue damage -> Hepatocyte necrosis -> Anaerobic niche expansion ->
  F. necrophorum growth -> MORE leukotoxin -> More neutrophil recruitment ->
  More activation/killing -> More tissue damage -> Loop continues
```

This is the fundamental reason abscesses grow. Breaking ANY link in this loop could halt progression.

**Disease stage:** Stage 4-5 (abscess formation and growth).

**Key biology:**
- The loop has a dose-dependent switch: at low leukotoxin, neutrophils ACTIVATE (degranulate, produce ROS, cause tissue damage). At high leukotoxin, neutrophils DIE. Both outcomes benefit the pathogen -- activation causes collateral tissue damage, death removes immune cells.
- The most vulnerable link is the INITIAL ACTIVATION step, because this is where a small amount of leukotoxin produces a disproportionate amount of tissue damage.
- Blocking neutrophil degranulation specifically (without blocking phagocytosis) would break the loop.
- The loop predicts that interventions reducing leukotoxin will have NON-LINEAR effects: a 50% reduction in leukotoxin may produce >50% reduction in abscess severity because the feedback loop is broken.

**Kill-chain:**
1. Quantify the feedback loop dynamics (leukotoxin dose-response for activation vs. killing vs. degranulation) [FEASIBLE]
2. Identify a selective inhibitor of neutrophil degranulation that preserves phagocytic killing [WEAKEST LINK]
3. Deliver to the liver (systemic)
4. Neutrophils encounter leukotoxin but do not degranulate -> no tissue damage
5. Neutrophils either survive (if leukotoxin is sub-lethal) or die cleanly (apoptosis without degranulation)
6. Without tissue damage, the anaerobic niche does not expand, F. necrophorum growth is limited
7. Immune containment succeeds

**Weakest link:** Step 2 -- separating degranulation from phagocytosis pharmacologically is very difficult. They share signaling pathways. This is a system-level vulnerability that is easy to identify but hard to exploit.

**Magnitude estimate:** If the feedback loop is the primary driver of abscess expansion (vs. initial establishment): breaking it would have minimal effect on whether an abscess forms but major effect on whether it stays small (A-) vs. becomes large (A+). Estimated: 50-70% reduction in A+ abscesses with minimal effect on overall incidence.

**Falsifiable prediction:** In a mouse or ex vivo liver abscess model, sub-inhibitory doses of leukotoxin (concentrations that activate but do not kill neutrophils) will produce LARGER zones of necrosis than supra-lethal doses (which kill neutrophils quickly). If supra-lethal doses produce larger zones, the activation-damage model is wrong.

**Closest analogy:** Neutrophil elastase inhibitors (sivelestat, approved in Japan for ALI) target the destructive component of neutrophil activation while preserving other immune functions.

---

### V13: Iron/Heme Starvation -- Exploiting the Missing Siderophore

**Target/mechanism:** F. necrophorum has NO Fur (ferric uptake regulator) gene and NO siderophore biosynthesis genes. This is extraordinary -- nearly all pathogenic bacteria have iron acquisition systems. F. necrophorum appears to rely ENTIRELY on heme uptake for iron. This is a profound metabolic dependency.

**Disease stage:** Stage 3-5 (from hepatic establishment through chronic persistence).

**Key biology:**
- Iron limitation reduces F. necrophorum growth in a dose-dependent manner.
- The liver is the body's primary iron storage organ (ferritin, hemosiderin). The hepatic microenvironment is relatively iron-rich, which may be WHY F. necrophorum targets the liver.
- Without siderophores, F. necrophorum cannot scavenge free iron. It MUST acquire heme from lysed erythrocytes or damaged hepatocytes.
- F. nucleatum (closely related) has a defined heme uptake operon. F. necrophorum likely has an analogous system.
- Blocking heme uptake would starve F. necrophorum of its SOLE iron source in the liver.

**Kill-chain:**
1. Identify the F. necrophorum heme uptake system (genome analysis + transcriptomics under iron limitation) [FEASIBLE -- weakest link is whether it is a single system or redundant]
2. Characterize the outer membrane heme receptor [MODERATE DIFFICULTY]
3. Design a heme analog that binds the receptor but cannot be utilized (competitive inhibitor) or blocks the transporter
4. Alternatively: design a non-utilizable gallium-porphyrin that is taken up but poisons iron-dependent enzymes (Trojan horse strategy)
5. Deliver to the liver (gallium porphyrins have inherent hepatic tropism)
6. F. necrophorum starves for iron -> growth arrest
7. Without growth, leukotoxin production drops (it peaks at mid-log phase) -> immune clearance succeeds

**Weakest link:** Step 1 -- the specific heme uptake machinery in F. necrophorum has not been characterized. If it uses multiple redundant pathways, blocking one may be insufficient.

**Magnitude estimate:** If heme is truly the SOLE iron source (no siderophores, no Fur-independent uptake): this could be bacteriostatic or bactericidal. Estimated 40-60% reduction in abscess establishment and progression. The Trojan horse approach (gallium porphyrin) could be directly bactericidal.

**Falsifiable prediction:** F. necrophorum grown in iron-depleted media supplemented with defined heme concentrations will show a strict dose-response between heme availability and (a) growth rate and (b) leukotoxin production. If heme depletion reduces leukotoxin production by >80%, this confirms the iron-leukotoxin-virulence axis.

**Closest analogy:** Gallium-based antimicrobials (gallium maltolate, gallium nitrate) exploit iron dependency and have completed Phase 2 clinical trials for Pseudomonas aeruginosa lung infections in CF patients. Gallium porphyrins are in preclinical development.

---

### V14: Quorum Sensing Disruption -- Locking the Commensal-to-Pathogen Switch

**Target/mechanism:** F. necrophorum exists as a commensal in the rumen of ALL cattle. The disease occurs when it transitions to a pathogenic state. Something triggers this transition. The most likely candidate is quorum sensing via the LuxS/AI-2 system, which is widespread in Fusobacterium genomes and regulates virulence in related organisms.

**Disease stage:** Stage 2 (colonization) -- prevents the virulence switch.

**Key biology:**
- LuxS/AI-2 quorum sensing regulates biofilm formation, toxin production, and virulence across multiple bacterial species.
- In Haemophilus parasuis, luxS deletion attenuates virulence 10-fold.
- F. necrophorum density increases in the rumen of grain-fed cattle. Higher density = more AI-2 = potential trigger for virulence gene activation.
- If LuxS/AI-2 controls lktBAC operon expression, then quorum sensing disruption would simultaneously reduce leukotoxin production, adhesin expression, and other virulence factors.
- AI-2 inhibitors (DPD analogs, AI-2 antagonists) are in preclinical development.

**Kill-chain:**
1. Confirm LuxS is present in F. necrophorum subsp. necrophorum genome [FEASIBLE -- genomic analysis]
2. Generate luxS deletion mutant; test leukotoxin production and virulence [CRITICAL -- weakest link]
3. If luxS mutant has reduced virulence: screen AI-2 analog library for antagonist activity
4. Deliver to the rumen (oral, daily dosing during finishing period -- similar to tylosin delivery)
5. F. necrophorum remains at "low-density" signaling state despite high actual density
6. Virulence genes not upregulated; leukotoxin production stays at commensal baseline
7. Immune system clears translocated bacteria normally

**Weakest link:** Step 2 -- LuxS may NOT regulate leukotoxin in F. necrophorum. In many bacteria, LuxS functions primarily in the activated methyl cycle (metabolism) rather than as a true quorum sensor. If AI-2 receptors are absent, LuxS is metabolic, not regulatory.

**Magnitude estimate:** If LuxS controls the virulence switch: 40-70% reduction in abscess incidence (comparable to tylosin but via a completely different mechanism). If LuxS is metabolic only: 0% effect.

**Falsifiable prediction:** A luxS deletion mutant of F. necrophorum subsp. necrophorum will produce <20% of wild-type leukotoxin levels in vitro (measured by cytotoxicity assay and ELISA). If leukotoxin production is unchanged, LuxS does not regulate virulence in this organism.

**Closest analogy:** Anti-quorum sensing compounds (furanones, DPD analogs) have shown efficacy in multiple animal models. No QS inhibitor has reached clinical approval, but the field is active with multiple companies (e.g., Quorum Innovations).

---

### V15: Obligate Synergy Disruption -- Severing the F. necrophorum / T. pyogenes Partnership

**Target/mechanism:** The polymicrobial synergy between F. necrophorum and T. pyogenes is obligate in a specific sense: T. pyogenes consumes oxygen (as a facultative anaerobe), creating the anaerobic microenvironment that F. necrophorum requires in the aerobic liver. Without T. pyogenes (or another oxygen consumer), F. necrophorum must rely solely on its own mechanisms (platelet aggregation, fibrin deposition, hemolysin) to create anaerobiosis.

**Disease stage:** Stage 4 (abscess formation).

**Key biology:**
- T. pyogenes fimbriae (FimA) and collagen-binding protein (CbpA) mediate adhesion to the abscess environment. These are specific, druggable targets.
- CbpA binds collagen -- the fibrous capsule is collagen-rich. T. pyogenes literally anchors to the abscess wall.
- If T. pyogenes is excluded from the abscess, F. necrophorum must establish anaerobiosis alone. The liver's oxygen tension may be too high for F. necrophorum alone (it is an obligate anaerobe, though aerotolerant).
- This strategy does NOT require killing T. pyogenes -- just preventing it from co-localizing with F. necrophorum in the liver.

**Kill-chain:**
1. Confirm T. pyogenes oxygen consumption is essential for F. necrophorum survival in the liver microenvironment [WEAKEST LINK]
2. If essential: target CbpA (collagen binding) to prevent T. pyogenes from persisting in the abscess niche
3. Anti-CbpA antibody or competitive peptide
4. Deliver systemically
5. T. pyogenes cannot anchor to the fibrous capsule -> washed out of abscess by immune activity
6. Oxygen tension in the abscess rises -> F. necrophorum growth arrested or killed
7. Abscess resolves (or at least stops growing)

**Weakest link:** Step 1 -- 71% of abscesses do NOT contain detectable T. pyogenes. F. necrophorum clearly can establish abscesses without T. pyogenes. The synergy makes abscesses worse (larger, more severe) but is not obligate for establishment.

**Magnitude estimate:** Modest -- would reduce severity in the 29% of abscesses where T. pyogenes is present. Estimated 10-20% reduction in A+ abscesses at the population level.

**Falsifiable prediction:** In an in vitro system, F. necrophorum cultured at 2% O2 (typical hepatic sinusoidal oxygen) will not grow. Co-culture with T. pyogenes at the same O2 will permit F. necrophorum growth (T. pyogenes consumes O2 to create a local anaerobic zone). If F. necrophorum grows at 2% O2 alone, the oxygen-consumption synergy is not essential.

**Closest analogy:** Anti-biofilm strategies targeting specific adhesins in polymicrobial infections (e.g., dental plaque, wound infections). Synergy disruption is a recognized therapeutic approach.

---

### V16: Contact System Activation Blockade -- Anti-Coagulation at the Bacterial Surface

**Target/mechanism:** F. necrophorum activates the contact system (Factor XII, high-molecular-weight kininogen/HK, prekallikrein) at its surface. This produces bradykinin (vasodilation, inflammation) and activates the intrinsic coagulation pathway (thrombin generation, fibrin deposition). The result: microthrombi around bacterial foci that create anaerobic niches and physical barriers to immune cell access.

**Disease stage:** Stage 3-4 (hepatic immune evasion + abscess formation).

**Key biology:**
- F. necrophorum binds HK specifically via the D5 domain.
- Bradykinin release is massive (3,300 pmol/mL) -- this is a potent inflammatory stimulus.
- Contact system activation produces thrombin via the intrinsic pathway, driving local coagulation independent of tissue factor.
- The plasma kallikrein inhibitor H-D-Pro-Phe-Arg-CMK blocks both bradykinin release and thrombin activation at the bacterial surface.
- This is INDEPENDENT of LPS-triggered coagulation -- it is a distinct, contact-mediated mechanism.

**Kill-chain:**
1. Confirm contact system activation occurs on F. necrophorum in the bovine liver (not just in vitro/Lemierre's syndrome) [WEAKEST LINK]
2. Identify the F. necrophorum surface molecule that binds HK [MODERATE DIFFICULTY]
3. Block the binding (anti-HK-D5 peptide, or anti-bacterial surface molecule antibody)
4. Alternatively: use a plasma kallikrein inhibitor (lanadelumab-type) to block downstream activation
5. Without contact activation: no local bradykinin, no local thrombin, no protective microthrombi
6. F. necrophorum is exposed to aerobic conditions and phagocytes without physical barrier
7. Immune clearance succeeds

**Weakest link:** Step 1 -- contact system activation was demonstrated in the context of Lemierre's syndrome (human), not bovine liver abscess. The bovine contact system may behave differently.

**Magnitude estimate:** If contact activation is critical for anaerobic niche creation in the liver: 20-40% reduction in abscess formation. The mechanism is elegant because it targets the pathogen's environmental manipulation rather than the pathogen itself.

**Falsifiable prediction:** In an ex vivo bovine liver perfusion model, addition of a plasma kallikrein inhibitor to the perfusate will reduce the number of viable F. necrophorum foci at 24h by >50% compared to untreated controls. If <10% reduction, contact system activation is not critical for hepatic colonization.

**Closest analogy:** Lanadelumab (anti-plasma kallikrein monoclonal antibody) is FDA-approved for hereditary angioedema. Plasma kallikrein inhibition is a validated drug target with approved products.

---

### V17: MMP-13 Induction Blockade -- Stopping Bacterial-Directed Tissue Remodeling

**Target/mechanism:** F. necrophorum induces host MMP-13 (collagenase 3) production by epithelial cells. This is a hijacking strategy -- the bacterium uses the host's own enzymes to degrade interstitial collagen and facilitate bacterial spread through tissue. MMP-13 is an established drug target with multiple inhibitors in development.

**Disease stage:** Stage 2 (rumen wall penetration) and Stage 4 (abscess expansion in liver).

**Key biology:**
- MMP-13 degrades type II collagen (the primary collagen of interstitial tissue).
- F. necrophorum actively stimulates MMP-13 expression -- this is not passive tissue damage.
- MMP-13 selective inhibitors exist and have been developed for osteoarthritis (e.g., CL-82198, compound 36).
- Blocking MMP-13 would prevent F. necrophorum from penetrating the rumen wall AND from expanding in the liver.

**Kill-chain:**
1. Confirm MMP-13 induction is required for rumen wall penetration (test invasion in MMP-13 inhibitor-treated tissue) [WEAKEST LINK]
2. Select or develop an MMP-13 selective inhibitor suitable for oral delivery to cattle
3. Deliver during the finishing period (daily oral dosing)
4. F. necrophorum cannot degrade interstitial collagen -> cannot penetrate rumen wall
5. Even if some bacteria reach the liver, they cannot expand the abscess through surrounding tissue
6. Disease is blocked at the tissue penetration step

**Weakest link:** Step 1 -- F. necrophorum also produces its own proteases and stimulates DNase activity. MMP-13 may be one of many tissue degradation mechanisms, and blocking it alone may be insufficient.

**Magnitude estimate:** If MMP-13 is essential for penetration: 30-50% reduction in abscess incidence. If redundant with bacterial proteases: <10%.

**Falsifiable prediction:** In a rumen wall explant invasion assay, F. necrophorum invasion depth at 24h will be reduced by >60% in the presence of MMP-13 inhibitor CL-82198 (10 uM) compared to untreated controls. If <20% reduction, bacterial proteases provide sufficient tissue degradation independent of host MMP-13.

**Closest analogy:** MMP inhibitors have been in clinical development for decades (cancer, arthritis). Selectivity has been the challenge (broad-spectrum MMP inhibitors have unacceptable side effects), but MMP-13-selective compounds have improved safety profiles.

---

## PART IV: INTERVENTION POINT PRIORITIZATION

### Tier 1: Highest-Value Novel Targets (First-in-Class Potential)

| Rank | Target | ID | Rationale |
|------|--------|----|-----------|
| 1 | **LktC acyltransferase inhibition** | V2 | If LktC is an acyltransferase, inhibiting it produces inactive leukotoxin. Exquisitely specific. No AMR. First-in-class RTX activator inhibitor. ONE critical experiment (recombinant LktC acyltransferase assay) resolves whether this is real. |
| 2 | **Iron/heme starvation (gallium porphyrin)** | V13 | No siderophores, no Fur -- F. necrophorum has a uniquely vulnerable iron metabolism. Gallium porphyrins have clinical precedent. Could be directly bactericidal. |
| 3 | **LktB secretion blockade** | V3 | POTRA2 domain is structurally tractable. Secretion arrest = no leukotoxin + proteotoxic stress. Dual mechanism. |
| 4 | **FomA dual-function blockade** | V7 | Factor H binding + endothelial adhesion in one target. Vaccine precedent (MenB fHbp). |

### Tier 2: High-Value Targets with Greater Uncertainty

| Rank | Target | ID | Rationale |
|------|--------|----|-----------|
| 5 | **Quorum sensing disruption (LuxS/AI-2)** | V14 | Could silence the entire virulence program. But LuxS may be metabolic, not regulatory, in F. necrophorum. |
| 6 | **Transcriptional silencing of lktBAC** | V1 | Requires understanding the regulatory circuit -- high payoff but high research burden. |
| 7 | **Contact system blockade** | V16 | Targets the anaerobic niche creation mechanism. Approved drugs exist (lanadelumab). But bovine relevance unconfirmed. |
| 8 | **Host receptor blockade** | V5 | Receptor unknown for 24 years. High payoff if solved. |

### Tier 3: Supporting Targets (Combination Components)

| Rank | Target | ID | Rationale |
|------|--------|----|-----------|
| 9 | **Feedback loop disruption** | V12 | Addresses severity more than incidence. Hard to drug selectively. |
| 10 | **Hemagglutinin blockade** | V8 | Likely redundant with other adhesins. Valuable only if it is the dominant adhesin. |
| 11 | **MMP-13 inhibition** | V17 | Established drug target class. Unclear if sufficient alone. |
| 12 | **Pyolysin inhibition** | V10 | Only relevant in 29% of abscesses. Severity modifier. |
| 13 | **Calcium chelation** | V4 | Requires confirming calcium dependence. Delivery is challenging. |
| 14 | **Neuraminidase inhibition** | V11 | Low population-level impact. |
| 15 | **Hemolysin inhibition** | V9 | Low bovine RBC activity questions relevance. |
| 16 | **Synergy disruption** | V15 | 71% of abscesses lack T. pyogenes. Modest standalone value. |

---

## PART V: THE THREE MOST NOVEL TARGETS

These are the targets most likely to be missed by a literature-based analysis:

### 1. LktC Acyltransferase Inhibition (V2)
**Why novel:** The dual annotation of LktC (histidine kinase vs. acyltransferase) has prevented either function from being targeted. In RTX systems, the acyltransferase is ALWAYS required for toxin activity, but no one has tested whether F. necrophorum's LktC follows this pattern. A single recombinant enzyme assay could unlock a first-in-class drug target.

### 2. Iron/Heme Starvation via Gallium Porphyrin (V13)
**Why novel:** The absence of siderophores and Fur in F. necrophorum has been noted in the literature but never exploited therapeutically. Gallium-based antimicrobials are in clinical development for other pathogens but have never been applied to Fusobacterium. The hepatic tropism of porphyrins aligns perfectly with the disease site.

### 3. Contact System Activation Blockade (V16)
**Why novel:** Contact system activation on F. necrophorum surfaces was described in a 2011 paper in the context of Lemierre's syndrome and has apparently never been connected to bovine liver abscess pathogenesis. The bradykinin release and intrinsic coagulation activation would directly explain the microthrombus formation and anaerobic niche creation described in the disease map -- yet the disease map attributes these to LPS and the platelet aggregation factor, without mentioning the contact system.

---

## PART VI: CRITICAL EXPERIMENTS (Ranked by Information Value per Dollar)

| Priority | Experiment | Resolves | Cost | Time |
|----------|-----------|----------|------|------|
| 1 | Recombinant LktC acyltransferase assay (express LktC, test acylation of pro-LktA) | V2: Is LktC an acyltransferase? | $5-10K | 4-6 weeks |
| 2 | LktA calcium dependence (cytotoxicity +/- EGTA) | V4: Is LktA calcium-dependent? | $2-5K | 2 weeks |
| 3 | F. necrophorum heme uptake characterization (genomic analysis + heme-limited growth curves) | V13: Can iron starvation work? | $5-10K | 4-6 weeks |
| 4 | lktBAC promoter-reporter screen (environmental signal panel) | V1 + V14: What triggers virulence? | $10-15K | 6-8 weeks |
| 5 | Anti-CD18 antibody vs. LktA cytotoxicity | V5: Is CD18 the receptor? | $3-5K | 2-3 weeks |
| 6 | LktB knockout growth phenotype | V3: Does secretion blockade cause proteotoxic stress? | $10-15K | 6-8 weeks |
| 7 | Contact system activation on F. necrophorum in bovine plasma | V16: Does contact activation occur in cattle? | $5-8K | 3-4 weeks |

**Total for the 7 de-risk experiments: ~$40-68K, 2-8 weeks each (most can run in parallel).**

---

*Vulcan analysis complete. 17 molecular intervention points identified across the leukotoxin lifecycle (6), secondary virulence factors (5), and system-level vulnerabilities (6). 3 genuinely novel targets proposed. 7 critical de-risk experiments defined.*
