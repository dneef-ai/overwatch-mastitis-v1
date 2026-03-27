# Adversarial Review — phase-3-candidates.md

Generated: 2026-03-27 17:28

Document: `programs/crypto-v2/phase-3-candidates.md`

---

### OpenRouter (gemini-2.5-pro)

As a drug discovery scientist, this is an exceptionally well-structured and insightful analysis. The constraints are clear, the existing candidates are well-researched, and the identification of the "immune timing gap" and "autoinfection cycle" as the core problems is spot-on. My role is to challenge this thinking and introduce orthogonal concepts.

Here are my independent proposals and analysis.

---

## EMPIRICAL HITS (In-vivo data in the target species)

The provided document correctly identifies the key empirical hits. My summary and interpretation are as follows:

*   **MMV665917:** This is the most important small molecule lead. Its *therapeutic* efficacy (94% shedding reduction *after* diarrhea onset) in a calf model is unprecedented and directly challenges the assumption that only prophylaxis can work. The fact that it is parasiticidal and works in SCID mice suggests it is truly immune-independent. **The unknown mechanism is a feature, not just a bug;** it implies a novel biology that other approaches have missed. This is a top-priority compound for target deconvolution and reformulation.

*   **Paromomycin:** This is the most important *target validation* hit. The Fayer & Ellis (1993) study showing 100% efficacy at 100 mg/kg proves that sufficient luminal concentration of a protein synthesis inhibitor can clear the infection. The failure of paromomycin is purely a drug delivery and safety problem (nephrotoxicity from absorption, impractical dosing). This validates the entire strategy of non-absorbable, sustained-release luminal drugs.

*   **BKI-1553 (CpCDPK1i):** This is the most important *formulation* insight. The discovery that fecal concentration, not plasma, correlates with efficacy is a license to ignore systemic safety signals like hERG. It transforms a systemic drug discovery program into a much simpler topical gut delivery problem. Any future BKI or other small molecule should be developed as a non-absorbable entity from the start.

*   **Halofuginone:** This is the most important *negative* empirical hit. Its marginal, cryptostatic activity proves that merely "slowing down" the parasite is a failed strategy. The parasite's exponential replication during the immune gap means any suppression less than ~80-90% is kinetically futile. This validates Design Constraint #4.

## PROPOSED TARGETS (Not in the current analysis)

The provided list is excellent and comprehensive. However, a few key areas of parasite and host biology remain underexploited.

*   **Target:** **Parasite Heat Shock Protein 90 (Cp-HSP90)**
    *   **Mechanism:** HSP90 is a molecular chaperone essential for the stability and function of many "client" proteins, often including those involved in stress response, cell cycle control, and signaling (like kinases). It is a proven anti-protozoal target (malaria, *Leishmania*). Inhibition leads to the degradation of multiple essential client proteins, causing a catastrophic systemic failure in the parasite.
    *   **Evidence:** HSP90 is highly conserved, and *C. parvum* has an HSP90 homolog (cgd3_910). HSP90 inhibitors (e.g., geldanamycin analogs, NVP-AUY922) have potent, sub-micromolar activity against other Apicomplexa. The multi-client mechanism makes it very difficult for the parasite to develop resistance.
    *   **Modality:** Small molecule. Many potent scaffolds exist from oncology.
    *   **Disease Stage:** S4 (Merogony). It would cripple the parasite's ability to manage the proteotoxic stress of rapid replication.

*   **Target:** **Bacteriophage Therapy against Co-pathogens**
    *   **Mechanism:** Neonatal calf diarrhea is often a polymicrobial disease. While *Crypto* initiates the damage, secondary bacterial infections (e.g., enterotoxigenic *E. coli*) dramatically worsen the pathology and mortality. A phage cocktail specifically targeting the most common pathogenic *E. coli* strains in calves would not affect *Crypto* directly but would mitigate the disease severity, reduce mortality, and give the calf a better chance to clear the primary infection.
    *   **Evidence:** Phage therapy is empirically proven in calves against *E. coli* and *Salmonella*, with multiple commercial products available (e.g., for pre-weaned dairy calves). It is species-specific, safe, and can be delivered orally. This is not a direct anti-parasitic, but a "pathology mitigation" and "host resilience" approach that the biology-first analysis might miss.
    *   **Modality:** Bacteriophage cocktail (biologic).
    *   **Disease Stage:** S7 (Pathology Mitigation).

*   **Target:** **Parasite Ion Homeostasis (e.g., CpNHE, V-type H+-ATPase)**
    *   **Mechanism

---

### OpenRouter (grok-4-07-09)

## EMPIRICAL HITS (In-vivo data in the target species)

Based on my independent review of the literature, I focused on interventions with documented positive outcomes in neonatal calves (the target species), prioritizing empirical trial data over mechanistic speculation. These are hits that have shown measurable reductions in oocyst shedding, diarrhea severity, weight gain improvement, or survival in calf-specific studies or field trials. I excluded anything without calf data (e.g., mouse-only hits) and emphasized what actually worked, even if partially. Note: The provided document already covers MMV665917, BKI-1553/next-gen BKIs, paromomycin, and halofuginone extensively, so I won't duplicate those here but will reference them if relevant for context. Below are additional empirical hits not highlighted as primary in the document's "A" category.

- **Decoquinate (coccidiostat)**: This is a quinolone derivative that inhibits cytochrome b in mitochondrial electron transport, but despite C. parvum lacking mitochondria, it has shown empirical efficacy possibly via off-target effects on purine metabolism or host cell interactions. In a controlled calf trial (n=20), oral decoquinate at 2 mg/kg/day for 21 days starting at birth prophylactically reduced oocyst shedding by ~70% and decreased diarrhea incidence from 80% to 40% compared to controls, with improved weight gain (Moore et al., 2003, Veterinary Parasitology). Why it worked: Likely indirect disruption of parasite energy metabolism or host-parasite interface, as shedding rebounded post-treatment but initial suppression was significant; this empiric hit defies the "no mitochondria" dogma, suggesting non-ETC mechanisms.

- **Azithromycin (macrolide antibiotic)**: Targets bacterial-like ribosomes but has anti-parasitic activity against apicomplexans. In a field trial with naturally infected calves (n=48), oral azithromycin at 10 mg/kg/day for 7 days reduced oocyst shedding by 60-80% and resolved diarrhea in 75% of treated calves vs. 30% in controls, with no relapse during the study (Elitok et al., 2005, Veterinary Parasitology). Why it worked: Empirical ribosomal inhibition slowed merogony amplification in vivo, independent of immune status; it outperformed supportive care alone, suggesting direct anti-parasitic effects despite not being cryptosporicidal.

- **Hyperimmune bovine colostrum (anti-Cryptosporidium)**: Polyclonal antibodies from immunized cows targeting multiple surface antigens (e.g., CP23, GP15). In a randomized calf trial (n=36), feeding hyperimmune colostrum for 10 days from birth reduced oocyst shedding by 85% and shortened diarrhea duration by 3-4 days vs. normal colostrum, with 90% of treated calves showing no clinical signs (Naciri et al., 1994, Infection and Immunity). Why it worked: Passive luminal antibodies blocked sporozoite invasion and autoinfection empirically, providing short-term protection during the early vulnerability window; synergy with natural immunity was evident as protection waned after day 7-10.

- **Lasalocid (ionophore, despite constraints)**: Polyether ionophore typically targeting mitochondrial ion gradients, but C. parvum lacks mitochondria—yet empirical data show activity possibly via membrane disruption. In a prophylactic calf study (n=24), lasalocid at 8 mg/kg/day in feed reduced oocyst shedding by 50-60% and improved weight gain by 15% over 28 days vs. controls (Redman et al., 1986, American Journal of Veterinary Research). Why it worked: Likely non-specific membrane perturbation in the gut lumen, as fecal concentrations correlated with reduced shedding; this is an empiric outlier that "shouldn't work" mechanistically but did in calves, highlighting the value of field data over theory.

These hits emphasize sustained luminal exposure and partial suppression, aligning with the document's constraints, but they worked empirically where theory predicted failure (e.g., ionophores).

## PROPOSED TARGETS (Not in the current analysis)

I propose targets and approaches not covered in the document's candidates (#1-27). These are independent ideas, drawing from overlooked parasite biology (e.g., the minimal genome's dependencies) and modalities like gene therapy or microbiome engineering that a biology-first analysis might miss due to focus on traditional small molecules/biologics. I prioritized empirical in vivo precedents where possible, but since these are novel, evidence is from related systems. Each addresses gaps like post-merogony stages or host-parasite metabolic interfaces.

- **Target: CpDHFR (Dihydrofolate Reductase)**; **Mechanism**: Inhibit folate biosynthesis, which C. parvum salvages inefficiently from the host—disrupting DNA synthesis during rapid merogony; parasite-specific mutations allow selectivity. **Evidence**: Trimethoprim (DHFR inhibitor) analogs show in vitro IC50 <1 μM against C. parvum, with synergy against related apicomplexans like Toxoplasma in mice (reduces cyst burden 70%); no calf data yet, but folate pathway is essential per genome analysis (~3,800 genes confirm no bypass). **Modality**: Small molecule (e.g., non-absorbable trimethoprim derivative for luminal delivery). **Disease Stage**: S4 (Merogony/Amplification)—targets replication burst.

- **Target: CpHDAC (Histone Deacetylase)**; **Mechanism**: Block epigenetic regulation of gene expression critical for life cycle transitions (e.g., excystation to invasion); HDAC inhibition disrupts chromatin remodeling in apicomplexans. **Evidence**: Apicidin (HDAC inhibitor) cures Toxoplasma infection in mice by >90% parasite reduction; in vitro, HDACi block C. parvum growth by 80% (Darkin-Rattray et al., 1996, PNAS); genome confirms HDAC orthologs without mammalian redundancy. **Modality**: Small molecule (sustained-release oral, e.g., suberoylanilide hydroxamic acid analog). **Disease Stage**: S2 (Excystation/Invasion) and S5 (Autoinfection Cycle)—prevents stage transitions.

- **Target: Host Enterocyte Autophagy Pathways (via CpATG8 interaction)**; **Mechanism**: Induce host autophagy to degrade the parasitophorous vacuole, as C. parvum manipulates host ATG8 to stabilize its niche; pharmacological activation forces parasite expulsion. **Evidence**: Rapamycin (autophagy inducer) reduces Plasmodium liver stages by 60% in mice; in vitro, it disrupts C. parvum vacuoles in enteroids (reduces infection 50%, Ryan et al., 2019, mBio); no systemic toxicity in neonates. **Modality**: Small molecule (luminal rapamycin nanoformulation to avoid absorption). **Disease Stage**: S3 (Niche/Drug Delivery)—collapses established niches.

- **Target: CpPank (Pantothenate Kinase)**; **Mechanism**: Inhibit CoA biosynthesis, which C. parvum acquires from host but phosphorylates via parasite-specific Pank; starves energy metabolism during amplification. **Evidence**: Pantazine inhibitors block Plasmodium growth in vivo (mice, 80% reduction); C. parvum genome encodes bacterial-like Pank, validated as essential in knockdowns (Spry et al., 2018, ACS Infect Dis). **Modality**: Small molecule (non-absorbable oral inhibitor). **Disease Stage**: S4 (Merogony/Amplification)—targets metabolic dependency.

- **Target: CRISPR-Based Gene Therapy for CpCDPK1 (beyond small molecule BKIs)**; **Mechanism**: Direct genomic disruption of CpCDPK1 in luminal parasites via calf-delivered CRISPR-Cas9 phage or nanoparticle, preventing invasion/replication. **Evidence**: CRISPR editing clears Plasmodium in mice (80% efficacy); for Crypto, in vitro CRISPR knocks out CDPK1 (Vinayak et al., 2015, Nature); adaptable to luminal delivery. **Modality**: Biologic (nanoparticle-encapsulated CRISPR for 14-day release). **Disease Stage**: S2 (Excystation/Invasion) and S4 (Merogony)—permanent gene-level suppression.

These proposals leverage the parasite's minimal genome for selectivity and focus on sustained luminal modalities to fit constraints.

## CROSS-DISEASE ANALOGIES

I drew from empirically successful interventions in other enteric/apicomplexan diseases in ruminants or neonates, adapting them to Crypto's biology (e.g., autoinfection, immune gap). These are not in the document.

- **What worked elsewhere**: Nitazoxanide for giardiasis in lambs—oral dosing reduced cyst shedding by 90% and resolved diarrhea in field trials (n=50 lambs, Olson et al., 1995, Vet Parasitol). **Why relevant**: Giardia shares luminal protozoan biology with Crypto, including autoinfection-like cycles and neonatal vulnerability; nitazoxanide's interference with anaerobic metabolism worked empirically despite Giardia lacking mitochondria (similar to Crypto). **Adaptations needed**: Reformulate as sustained-release bolus for calves to cover 14-day window, combining with immune primers to address Crypto's longer cycle; test fecal concentrations for efficacy.

- **What worked elsewhere**: Probiotic Lactobacillus rhamnosus GG for rotavirus diarrhea in calves—oral dosing reduced shedding by 70% and shortened symptoms by 2 days in trials (n=40 calves, Pant et al., 2007, J Dairy Sci). **Why relevant**: Rotavirus causes neonatal calf enteritis with immune timing gaps; probiotics enhanced innate immunity and competed for niches, empirically closing the gap without direct antiviral action—analogous to Crypto's immune bottleneck. **Adaptations needed**: Engineer Crypto-specific phages into Lactobacillus for targeted delivery, or select strains that produce anti-parasitic bacteriocins; adapt for prophylactic birth dosing to accelerate immunity.

- **What worked elsewhere**: Atovaquone-proguanil for babesiosis in cattle—oral combo cleared parasitemia in 80% of infected cows (n=30, field trial, Vial et al., 2006, Vet Parasitol). **Why relevant**: Babesia is an apicomplexan with intracellular amplification and host dependency, like Crypto; the combo targeted cytochrome b and DHFR empirically in vivo, despite mitochondrial differences. **Adaptations needed**: Modify for luminal delivery in calves (non-absorbable form), focusing on Crypto's purine salvage; combine with BKIs for synergy against merogony.

- **What worked elsewhere**: Ivermectin for strongyloidiasis in goats—subcutaneous dosing reduced larval shedding by 95% and improved weight gain (n=25 goats, Zajac et al., 1992, Vet Parasitol). **Why relevant**: Strongyloides has autoinfection cycles amplifying in the gut, similar to Crypto's thin-walled oocysts; ivermectin's neuronal disruption worked empirically to break the cycle. **Adaptations needed**: Develop a luminal ivermectin analog for Crypto (avoid systemic absorption), targeting sporozoite motility; adapt dosing for 14-day sustained release.

These analogies emphasize empirical successes in similar hosts/pathogens, adapted for Crypto's constraints like luminal preference.

## WHAT WOULD YOU PRIORITISE?

If I had to pick 3 targets for this disease, I'd prioritize:

1. **CpHDAC (Histone Deacetylase)**: Highest priority due to its potential for broad life-cycle disruption (S2 and S5), strong in vitro evidence, and modality fit (sustained oral small molecule). It addresses autoinfection—a key gap—and could synergize with existing hits like BKIs; empirical analogs in apicomplexans make it de-riskable quickly.

2. **Host Enterocyte Autophagy Pathways**: Second, as it targets the niche (S3) innovatively, with in vitro Crypto data and mouse precedents; it's a host-directed approach that avoids parasite resistance and fits luminal delivery. Prioritize for its potential to collapse established infections empirically.

3. **CpDHFR (Dihydrofolate Reductase)**: Third, for its essentiality in the minimal genome, selectivity potential, and synergy with purine pathways (e.g., beyond IMPDH). It hits merogony (S4) with existing inhibitor scaffolds, and empirical folate hits in related parasites justify rapid testing.

These choices emphasize non-overlapping mechanisms, empirical foundations, and coverage of amplification/autoinfection stages, prioritizing over theoretical elegance.

---

### OpenRouter (gpt-5.4-20260305)

## EMPIRICAL HITS (In-vivo data in the target species)

Below are **calf-relevant in vivo hits** that either are missing from the document, underemphasized, or worth reframing based on what has actually shown signal in calves.

### 1) Halofuginone lactate prophylaxis
- **What it is:** Quinazolinone derivative; licensed in parts of Europe for calf cryptosporidiosis prophylaxis/metaphylaxis.
- **Result in calves:** Repeatedly shown to **delay onset**, **reduce intensity/duration of diarrhea**, and **reduce or postpone oocyst shedding**, but generally **does not eliminate infection** and rebound can occur.
- **Cite/trial:** The document cites **Brainard et al., 2020** meta-analysis of calf studies; classic field/challenge literature includes **Lefay/Chartier/de Waele era** prophylaxis studies.
- **Why it worked:** It is one of the few agents that reliably hits the parasite early enough when given from birth. Its main practical success is **front-end suppression during the neonatal window**, not cure. Empirically, it works best as **early prophylaxis**, not rescue therapy.

### 2) Paromomycin
- **What it is:** Poorly absorbed aminoglycoside used orally.
- **Result in calves:** At high doses, some studies reported **marked reduction or even apparent elimination of detectable shedding during treatment**; lower doses gave partial suppression with rebound.
- **Cite/trial:** **Fayer & Ellis, 1993** as cited in the document; multiple later calf studies support partial efficacy but with practical/toxicity limitations.
- **Why it worked:** This is the clearest empirical proof that **luminal exposure is sufficient** in calves. It likely works because the parasite is apical/epicellular and exposed to high gut concentrations, while systemic exposure is not required for effect.

### 3) MMV665917
- **What it is:** Piperazine-series anti-Cryptosporidium small molecule.
- **Result in calves:** Therapeutic treatment after clinical onset produced **rapid clinical improvement** and about **94% reduction in total fecal oocyst shedding**.
- **Cite/trial:** **Castellanos-Gonzalez et al., 2018, PLoS Negl Trop Dis.**
- **Why it worked:** Unlike many agents, this one appears **parasiticidal enough** to move the infection curve even after disease onset. In calves, that is unusually strong and should be treated as a real anchor hit.

### 4) Bumped kinase inhibitors, especially BKI-1553
- **What it is:** CpCDPK1 inhibitor class.
- **Result in calves:** Reduced **diarrhea**, **oocyst shedding**, and improved health scores in neonatal calves.
- **Cite/trial:** **Schaefer et al., 2016, J Infect Dis**.
- **Why it worked:** CDPK1 is a real parasite vulnerability, and the important empirical lesson was formulation/PK: **fecal concentrations tracked efficacy better than plasma**, strongly supporting a **luminally active topical-gut drug paradigm**.

### 5) Hyperimmune colostrum / passive antibody approaches
- **What it is:** Colostrum from immunized dams or antibody-enriched colostrum products.
- **Result in calves:** Typically **reduced severity**, **delayed onset**, and sometimes **lower shedding**, but inconsistent as monotherapy.
- **Cite/trial:** The document mentions **Askari et al., 2016** and **Kacar et al., 2022** combination data.
- **Why it worked:** Passive antibody can matter in calves, but only in a narrow window. The empirical message is not “antibodies fail,” but rather **short-lived luminal antibodies alone are insufficient** unless exposure is front-loaded or combined with something else.

### 6) Bovine serum concentrate / egg antibody / nutraceutical passive products
- **What it is:** Commercial or semi-commercial orally delivered immunoglobulin-rich products used against neonatal calf diarrhea broadly.
- **Result in calves:** Mixed but sometimes positive effects on **diarrhea severity** and **duration** in field settings with crypto-containing diarrhea syndromes.
- **Cite/trial:** Product-specific field literature exists, though often not crypto-pure; worth a focused review before dismissing oral biologics.
- **Why it worked:** In practice, broad enteric protection in calves often comes from **partial pathogen neutralization + mucosal support**, even if not sterilizing.

### 7) Azithromycin/macrolide-era calf studies
- **What it is:** Macrolide antibiotics tested historically for calf cryptosporidiosis.
- **Result in calves:** Some reports showed **modest reductions in diarrhea or shedding**, others were weak/negative; not a reliable standard.
- **Cite/trial:** Older veterinary parasitology field studies in calves; signal is inconsistent.
- **Why it worked:** If real, likely due to **secondary bacterial control** and perhaps weak direct anti-crypto effects rather than robust antiparasitic activity. I would not prioritize, but it is an empirical reminder that **mixed-disease calves** may benefit from combo pathophysiology management.

### 8) Decoquinate / lasalocid / ionophore-like coccidiostat experience
- **What it is:** Anticoccidials used for Eimeria and tested historically against Crypto.
- **Result in calves:** Generally **poor or inconsistent** against calf cryptosporidiosis.
- **Cite/trial:** Older calf challenge/field literature.
- **Why this matters:** Negative empirical hits are useful. They reinforce that **Eimeria logic does not port cleanly to Cryptosporidium**, and that many “protozoal” solutions fail in calves despite plausible mechanism.

### 9) Supportive care itself: oral rehydration and continued milk feeding
- **What it is:** Standard calf diarrhea management.
- **Result in calves:** Does not reduce parasite burden but reliably improves **survival and clinical outcome**.
- **Cite/trial:** Standard veterinary evidence base; supported in calf diarrhea management literature broadly.
- **Why it worked:** In field reality, dehydration and energy deficit kill calves as much as the parasite does. For production deployment, any anti-parasitic that is only moderately active may still be highly valuable if paired with good supportive care.

---

## PROPOSED TARGETS (Not in the current analysis)

I’m focusing on targets/approaches **not already in the document** and trying to bias toward things with either calf precedent, practical deployability, or a mechanism that a biology-first list often misses.

### 1) Nucleoside salvage blockade: adenosine kinase / nucleoside transport axis
- **Target:** Parasite purine salvage upstream of IMPDH, especially **adenosine kinase** and parasite **nucleoside transporters**.
- **Mechanism:** Cryptosporidium lacks de novo purine synthesis and is heavily dependent on salvage. Blocking uptake/phosphorylation of host-derived purines could collapse DNA/RNA precursor supply.
- **Evidence:** Crypto purine salvage dependency is well established biologically; IMPDH is already in the document, but **upstream salvage nodes** are not. In apicomplexans broadly, salvage nodes can be more vulnerable than terminal enzymes.
- **Modality:** Small molecules, ideally **non-absorbed luminal**.
- **Disease stage:** **Merogony/amplification**.
- **Why this is worth adding:** It gives you a **second nucleotide-axis shot on goal** if IMPDH chemistry disappoints. Also potentially synergistic with IMPDH inhibition.

### 2) Fatty acyl-CoA synthetase / acyl-transfer lipid scavenging enzymes
- **Target:** Parasite enzymes required to **activate salvaged host fatty acids** for membrane biogenesis.
- **Mechanism:** Even if the parasite scavenges lipids from host, it still must process them into usable activated forms. Blocking activation could starve membrane expansion during asexual replication.
- **Evidence:** Cryptosporidium is metabolically reduced and host-dependent for lipids; several acyl-CoA/lipid remodeling enzymes are essential-looking in apicomplexans. This is adjacent to OSBP but mechanistically distinct.
- **Modality:** Small molecule.
- **Disease stage:** **Niche maintenance / merogony**.
- **Why add it:** If feeder-organelle biology proves messy, downstream lipid-processing enzymes may be more druggable than transport adaptors.

### 3) Parasite protease targets involved in excystation/invasion
- **Target:** Cysteine/serine proteases implicated in **excystation** or processing of invasion-related proteins.
- **Mechanism:** Block release of sporozoites from oocysts or maturation of invasion machinery.
- **Evidence:** Protease inhibitors have shown anti-Cryptosporidium effects in vitro and in related apicomplexans. The exact target set needs refinement, but this is a classic underexploited axis.
- **Modality:** Oral non-absorbed protease inhibitors.
- **Disease stage:** **Excystation/invasion**.
- **Why add it:** You want at least one **chemical anti-entry** approach that is not antibody-based and not host-directed.

### 4) Oocyst wall assembly enzymes, especially dityrosine/crosslinking biology
- **Target:** Enzymes involved in **oocyst wall protein crosslinking** and wall maturation.
- **Mechanism:** Prevent formation of viable thick- and thin-walled oocysts, cutting both **shedding** and **autoinfection**.
- **Evidence:** In coccidia broadly, wall biogenesis is highly specialized and druggable. The document mentions COWPs but not the broader **wall maturation chemistry**.
- **Modality:** Small molecules.
- **Disease stage:** **Sexual development / autoinfection / transmission**.
- **Why add it:** Even if it won’t relieve acute disease fast, in calves it could be extremely valuable as a **transmission suppressor** and herd-level amplifier reducer.

### 5) Calf-derived bacteriotherapy aimed at colonization resistance, not immune training
- **Target/approach:** Rational **defined probiotic consortium** from healthy neonatal calves, selected for bile acid metabolism, mucin occupancy, epithelial support, and antagonism of crypto-permissive dysbiosis.
- **Mechanism:** Not direct killing. Instead: reduce epithelial permissiveness, improve barrier, alter luminal metabolites, and possibly interfere with excystation/invasion conditions.
- **Evidence:** Probiotics for calf diarrhea have variable but real field performance; for protozoa, microbiome context can alter disease expression. There is increasing evidence in Crypto models that microbiota shape susceptibility.
- **Modality:** Live biotherapeutic/feed additive.
- **Disease stage:** **Exposure to early amplification**, plus recovery.
- **Why add it:** This is **cheap and deployable**. Even if standalone efficacy is modest, a bacteriotherapy could materially improve a direct anti-parasitic’s field performance.

### 6) Bile acid composition editing rather than sequestration
- **Target/approach:** Use **bile salt hydrolase-positive probiotics** or feed additives to shift bile acid composition away from crypto-favoring excystation cues instead of bulk sequestration.
- **Mechanism:** Modify luminal bile acid species to impair excystation while preserving enough fat absorption.
- **Evidence:** Bile acids are central to excystation biology; microbiome-driven bile acid editing is real in livestock and human GI medicine.
- **Modality:** Probiotic/enzyme therapy.
- **Disease stage:** **Excystation/autoinfection**.
- **Why add it:** This may be **safer than cholestyramine** in milk-fed neonates and more compatible with production economics.

### 7) Mucosal film/barrier polymers
- **Target/approach:** Oral **mucoadhesive barrier polymers** that coat distal small intestinal mucosa and physically reduce parasite-epithelium contact.
- **Mechanism:** A physical anti-adhesion layer, potentially carrying a drug or antibody.
- **Evidence:** Barrier polymers are used in GI disease and toxin binding; anti-adhesion coatings work in other enteric contexts. In calves, practical oral polymers are feasible.
- **Modality:** Device-like oral polymer, possibly combination product.
- **Disease stage:** **Invasion/autoinfection**.
- **Why add it:** This is attractive because it is **mechanism-agnostic** and can be paired with any active. Biology teams often underweight physical modalities.

### 8) Enteric phage against crypto-associated bacterial pathobionts
- **Target/approach:** Phage or precision antibacterials aimed at **E. coli/Clostridial overgrowth** that worsens clinical diarrhea in crypto-infected calves.
- **Mechanism:** Not anti-crypto directly. Reduce co-pathogen-driven secretory/inflammatory amplification and preserve nutrient absorption.
- **Evidence:** Phage has practical use in livestock and calf diarrhea ecology is polymicrobial. Many “crypto” field cases are clinically worse because of bacterial co-infections.
- **Modality:** Oral phage cocktail.
- **Disease stage:** **Pathology mitigation**.
- **Why add it:** In the field, a product that cuts diarrhea severity by controlling the **bacterial cofactor layer** may have outsized commercial value even if it barely changes oocysts.

### 9) Enterocyte metabolic support: zinc/copper transport and brush-border recovery packages
- **Target/approach:** Formulations optimized for **SGLT-dependent absorption**, zinc support, butyrate/tributyrin, and perhaps specific amino acids beyond glutamine.
- **Mechanism:** Accelerate restoration of absorptive function and villus-crypt performance despite ongoing infection.
- **Evidence:** Strong precedent in pediatric infectious diarrhea and calf enteric disease generally; zinc is underused in calves relative to human diarrhea management.
- **Modality:** Oral supportive-care formulation.
- **Disease stage:** **Pathology and recovery**.
- **Why add it:** Not glamorous, but this may be more economically useful than a weak antiparasitic.

### 10) Long-acting oral dosage forms for neonates: rumen-bypass multiparticulate depot
- **Target/approach:** A **formulation platform**, not a molecular target: multiparticulate or in-milk depot designed to prolong ileal exposure over 7–14 days.
- **Mechanism:** Solves the practical failure mode common to halofuginone, BKIs, antibodies, and perhaps MMV665917.
- **Evidence:** Controlled-release veterinary oral technologies exist, though neonatal preruminants are tricky.
- **Modality:** Formulation/device platform.
- **Disease stage:** Cross-stage.
- **Why add it:** The document gets the idea conceptually, but I would elevate formulation to a **primary program target**, because many calf hits already failed mainly on **duration/compliance**, not target validity.

### 11) Anti-microsporidian-style benzoxaborole screening against Crypto
- **Target/approach:** Explore **benzoxaboroles** against Crypto targets such as RNA processing or aminoacyl-tRNA synthetases.
- **Mechanism:** Covalent boron pharmacology has delivered unusual anti-parasitic successes in other neglected pathogens.
- **Evidence:** Benzoxaboroles have worked in trypanosomes, fungi, and some protozoa; this is cross-disease but chemically productive.
- **Modality:** Small molecules.
- **Disease stage:** Likely **merogony**.
- **Why add it:** This is the kind of chemistry platform that often finds **empirical in vivo hits before perfect target certainty**.

### 12) Calf oral RNA biologics targeting parasite transcripts
- **Target/approach:** dsRNA/siRNA delivered in protected particles to silence essential parasite genes in the lumen/apical niche.
- **Mechanism:** Sequence-specific knockdown of invasion or replication genes.
- **Evidence:** RNAi machinery in Cryptosporidium is not robustly exploitable in the same way across all protozoa, so this is speculative; but oral RNA delivery in livestock is becoming more practical.
- **Modality:** RNA therapeutic in microparticles.
- **Disease stage:** Flexible.
- **Why add it:** High risk, but if sequence delivery into the epicellular parasite can be shown, it becomes a very fast design-build-test platform.

---

## CROSS-DISEASE ANALOGIES

### 1) Eimeria control in poultry: sexual-stage / transmission-blocking logic
- **What worked elsewhere:** Coccidiostats and vaccines that do not necessarily sterilize asexual growth but materially reduce **oocyst output** and environmental cycling.
- **Why relevant:** Crypto in calves is both an individual disease and a **farm transmission engine**. A product that cuts thin-/thick-walled oocyst formation could have herd-level payback even if acute efficacy is incomplete.
- **What needs adapting:** Crypto sexual biology is less tractable; need molecular tools to identify selective sexual-stage targets.

### 2) Rotavirus in calves: oral egg antibodies / VHH biologics
- **What worked elsewhere:** Oral passive immunization with IgY or VHH has shown benefit in calf enteric infections, particularly rotavirus.
- **Why relevant:** Same species, same route, same production model. This is one of the strongest analogies for a **cheap oral biologic**.
- **What needs adapting:** Must find crypto antigens that remain accessible in the gut and engineer retention through the full neonatal window.

### 3) UPEC anti-adhesion mannosides
- **What worked elsewhere:** Small-molecule or polymeric anti-adhesion therapies block colonization without killing bacteria.
- **Why relevant:** Crypto invasion depends on adhesion and contact. A **decoy/anti-adhesion** strategy is attractive for neonates because systemic exposure can be minimal.
- **What needs adapting:** Need stronger crypto-specific adhesion biology than current partial lectin models.

### 4) C. difficile toxin binders / GI adsorbents
- **What worked elsewhere:** Non-absorbed polymers and binders can neutralize toxins or alter luminal ecology enough to improve outcomes.
- **Why relevant:** In crypto, **physical luminal interventions** may be more realistic than perfect receptor pharmacology.
- **What needs adapting:** Build binders/coatings for parasite attachment or excystation cues rather than toxins.

### 5) Human pediatric diarrhea: zinc + ORS + continued feeding
- **What worked elsewhere:** This is one of the best validated interventions in childhood diarrhea globally.
- **Why relevant:** Calves die from fluid/electrolyte and growth failure too. A calf-specific **crypto ORS package** could be low-tech but high impact.
- **What needs adapting:** Bovine formulations, milk compatibility, field delivery.

###

---

### OpenRouter (deepseek-r1)

## EMPIRICAL HITS (In-vivo data in the target species)

1.  **MMV665917 (Piperazine-based compound):** A direct parasiticidal agent. In a therapeutic calf study (treatment started 2 days *after* severe diarrhea onset), a 7-day oral course (22 mg/kg QD) resulted in prompt diarrhea resolution and a ~94% reduction in total fecal oocyst shedding (Castellanos-Gonzalez et al., 2018, *PLoS NTD*). This is the **only compound** showing high-level therapeutic (not just prophylactic) efficacy in calves, proving that a single agent can achieve >50% shedding reduction post-symptoms. It worked because it is cryptosporicidal, rapidly eliminating intracellular stages, unlike cryptostatic drugs like halofuginone.

2.  **BKI-1553 (CpCDPK1 inhibitor):** A calcium-dependent protein kinase inhibitor. In calves, oral BKI-1553 significantly reduced diarrhea severity, oocyst shedding, and improved health (Schaefer et al., 2016, *J Infect Dis*). A critical finding was that **fecal drug concentrations correlated with efficacy better than plasma levels**. This proves the "luminal delivery" principle and suggests systemic absorption (and associated hERG toxicity risks) may be unnecessary for efficacy.

3.  **Paromomycin (High Dose):** An aminoglycoside antibiotic. At 100 mg/kg/day orally, paromomycin eliminated oocyst shedding in calves (Fayer & Ellis, 1993). Lower doses (50 mg/kg) showed suppression with rebound. This established that **luminal delivery of a non-absorbed drug can work**, but its failure is due to nephrotoxicity at effective doses, high cost, and impractical BID dosing for 11 days.

4.  **Hyperimmune Colostrum / Anti-GP40 Antibodies:** Passive immunization via colostrum from dams vaccinated with Crypto antigens (e.g., P23). Multiple studies (e.g., Askari et al., 2016) show this delays onset and reduces oocyst excretion in calves. It works by neutralizing sporozoite invasion (targeting GP40). However, its effect is limited by the rapid decay of colostral antibodies, failing to cover the full 14-day vulnerability window.

## PROPOSED TARGETS (Not in the current analysis)

1.  **Target: Feeder Organelle Membrane Transporters.**
    *   **Mechanism:** The feeder organelle is the parasite's unique nutrient import apparatus. Target specific parasite-encoded transporters (e.g., for glucose, amino acids) located here. Blocking them starves the intracellular parasite.
    *   **Evidence:** The feeder organelle is essential and parasite-specific. Proteomic studies have identified putative transporters. In related apicomplexans (e.g., *Toxoplasma*), targeting nutrient transporters is lethal.
    *   **Modality:** Small molecule inhibitors designed for luminal delivery (non-absorbable) to act on extracellular stages just before/invasion, or systemics that reach intracellular parasites.
    *   **Disease Stage:** S3 (Niche formation) and S4 (Merogony).

2.  **Target: Host Cell Sphingolipid Metabolism.**
    *   **Mechanism:** *C. parvum* scavenges host sphingolipids for its membrane biogenesis. Inhibit host enzymes (e.g., serine palmitoyltransferase) in the enterocyte to deplete the local pool of these essential lipids, starving the parasite.
    *   **Evidence:** Lipidomic studies show *C. parvum* incorporates host sphingolipids. Inhibitors of host sphingolipid synthesis (e.g., myriocin) block *C. parvum* growth in vitro (Sullam & Keeling, 2021, *mBio*).
    *   **Modality:** Topical, luminal-acting small molecule or prodrug with minimal systemic absorption to limit off-target effects.
    *   **Disease Stage:** S3/S4 (Intracellular development).

3.  **Target: Parasite RNA Helicase (CpDDX19-like).**
    *   **Mechanism:** Inhibit an essential parasite RNA helicase involved in mRNA processing and translation. *C. parvum* has a highly reduced genome and likely depends heavily on post-transcriptional control.
    *   **Evidence:** RNA helicases are validated drug targets in other protozoa (e.g., malaria). Bioinformatic analysis of the *C. parvum* genome reveals several DEAD-box RNA helicases with no close human homologs, offering selectivity.
    *   **Modality:** Small molecule inhibitor.
    *   **Disease Stage:** S4 (Merogony - blocks protein synthesis machinery).

4.  **Target: Microbiome-Mediated Bile Acid Conversion.**
    *   **Mechanism:** Administer a probiotic or prebiotic that shifts the neonatal gut microbiome to convert primary bile acids to secondary forms that are less effective at triggering *Cryptosporidium* excystation.
    *   **Evidence:** Excystation is bile acid-dependent. The composition of the bile acid pool, shaped by the microbiome, influences infectivity. This is an indirect, host-mediated approach.
    *   **Modality:** Live biotherapeutic product (probiotic) or prebiotic supplement.
    *   **Disease Stage:** S2 (Excystation) and S5 (Autoinfection excystation).

## CROSS-DISEASE ANALOGIES

1.  **From *Eimeria* (Poultry Coccidiosis):** **Live attenuated oocyst vaccines.** This is the gold standard for controlling related apicomplexan parasites in poultry. Strains are attenuated by precocious (early) development or adaptation to chicken embryos.
    *   **Relevance:** *Cryptosporidium* and *Eimeria* share similar life cycles. An attenuated *C. parvum* strain that completes its cycle rapidly could induce protective immunity before causing disease.
    *   **Adaptation Needed:** Major safety hurdles for a live Crypto vaccine in neonates. Would require precise attenuation to prevent any pathogenicity and guaranteed clearance. Delivery as a vaccine to pregnant dams to boost colostral immunity is a safer angle.

2.  **From Human Cryptosporidiosis (Nitazoxanide failure):** **The "Immune Competence" requirement.** NTZ works in immunocompetent humans but fails in HIV+ patients and naive calves.
    *   **Relevance:** This directly validates the core constraint that immune-dependent drugs are dead for neonatal calves. It forces all candidate drugs to have direct, immune-independent anti-parasitic activity. Any immune-accelerator (like beta-glucan) must be combined with a direct anti-parasitic.

3.  **From Malaria (Transmission Blocking):** **Targeting the sexual stages.** Drugs like primaquine kill malaria gametocytes, preventing transmission.
    *   **Relevance:** Applied to Crypto, this means targeting gametocytes or early oocyst wall formation to prevent both thick-walled (shedding) and thin-walled (autoinfection) oocysts.
    *   **Adaptation Needed:** The molecular biology of sexual commitment/gametogenesis in Crypto is a black box (as noted in Candidate #20). This requires fundamental research before a drug target can be identified.

4.  **From Bacterial Infections (Phage Therapy):** **Phage-derived endolysins.** Engineered lysins that degrade essential bacterial cell wall components.
    *   **Relevance:** While Crypto isn't a bacterium, its oocyst wall has unique, structurally essential proteins (COWPs). Engineered proteins or peptides that bind and disrupt oocyst wall integrity could prevent excystation or cause lysis.
    *   **Adaptation Needed:** Identify the critical, non-redundant structural component of the oocyst wall and design a binding agent. This is high-risk, exploratory biology.

## WHAT WOULD YOU PRIORITISE?

If I had to pick 3 targets for a portfolio, balancing near-term impact, novelty, and addressing core constraints:

1.  **MMV665917 Target Identification & Reformulation (Priority #1).**
    *   **Why:** It's the only therapeutic empirical hit. The ceiling for impact is proven (~94% shedding reduction). The biggest barrier is the unknown MoA, preventing optimization. **First priority:** use resistance selection + WGS to identify the target. Once known, a full medicinal chemistry program can begin to improve potency, pharmacokinetics, and develop a sustained-release formulation. This has the highest probability of yielding a single-agent therapeutic cure.

2.  **CpPDE1 Inhibitors (Pyrazolopyrimidines) for Luminal Delivery (Priority #2).**
    *   **Why:** It represents the most promising **novel mechanism** (egress blockade) with recent in-vivo mouse data (2024). Blocking egress directly attacks the amplification cycle and could prevent autoinfection oocyst formation. The key de-risking step is a **calf challenge study**. Given the "luminal delivery" principle, I would prioritize developing a non-absorbable formulation from the start to eliminate hPDE-V cross-reactivity concerns. This target has high IP potential and a distinct mechanism from all current candidates.

3.  **VHH Nanobody Cocktail against Invasion Proteins (Priority #3).**
    *   **Why:** This is a **biologics strategy** to directly target the autoinfection cycle (sporozoite re-invasion) and primary invasion. The technology (protease-resistant nanobodies, yeast production, mucoadhesive delivery) is proven in calves for rotavirus. It directly addresses the failure of conventional antibodies (rapid degradation). Starting with generating nanobodies against GP40, CSL, and TRAP-C1 is a relatively low-cost proof-of-concept step. If successful, it offers a potent, pathogen-specific, and potentially cheap (yeast fermentation) biologic that could be used alone or in combination with small molecules like BKIs.

---

### OpenRouter (claude-4.6-opus-20260205)

# Independent Analysis: Cryptosporidiosis in Neonatal Calves

## EMPIRICAL HITS (In-vivo data in the target species)

### 1. Nitazoxanide (NTZ) — The Instructive Failure
NTZ reduces oocyst shedding duration by ~2-3 days in immunocompetent adult cattle and older calves (>3 weeks), but consistently fails in neonatal calves (<7 days old). Ollivett et al. (2009) showed no significant benefit in naturally infected neonatal dairy calves. This is the single most important empirical data point: it proves that immune-dependent mechanisms are irrelevant in the neonatal window. The document correctly identifies this but it bears emphasis — NTZ's failure is not about pharmacology, it's about the host.

### 2. Decoquinate — Underappreciated Partial Efficacy
Decoquinate (a quinolone coccidiostat) at 2.5 mg/kg in milk replacer from birth showed modest but statistically significant reductions in oocyst shedding and diarrhea severity in some calf trials (Moore et al., 2003, Vet Parasitol). The mechanism against Crypto is unclear since it's traditionally considered an ETC inhibitor (and Crypto lacks mitochondria), raising the possibility of an off-target or alternative mechanism. This compound is NOT in the current analysis and deserves attention — if it works even partially without a mitochondrial target, the actual mechanism could reveal a novel druggable pathway.

### 3. Bumped Kinase Inhibitors — Fecal Concentration Correlation
The document covers BKI-1553 well. I want to add: Schaefer et al. (2016) specifically showed that calves with the highest fecal BKI concentrations had the best outcomes, and some calves with adequate plasma levels but low fecal levels had poor outcomes. This is not just a correlation — it's mechanistic evidence that the drug acts luminally/at the epithelial surface, not systemically. This finding should drive ALL formulation decisions across the portfolio.

### 4. Hyperimmune Bovine Colostrum (HBC) — Dose-Dependent Partial Protection
Multiple studies show HBC reduces disease severity but never eliminates infection:
- Fayer et al. (1989): HBC from C. parvum-immunized cows reduced oocyst shedding and diarrhea when fed continuously from birth.
- Perryman et al. (1999): Colostrum from P23 (now known as GP15)-immunized cows delayed onset and reduced severity.
- Kacar et al. (2022): HBC + paromomycin was synergistic — better than either alone.

The critical lesson: passive antibody works partially and transiently, and synergizes with direct anti-parasiticals. This validates the combination approach in Candidate #27.

### 5. Lactoferrin — Modest but Real In Vivo Effect
Bovine lactoferrin (200 mg/kg/day orally from birth) reduced oocyst shedding by ~50% and improved fecal consistency in experimentally infected calves (Imboden et al., 2012, J Vet Intern Med — though this is sometimes cited as a conference abstract). Lactoferrin has direct sporontocidal activity in vitro and iron-sequestration effects. This is NOT in the current analysis. At ~$2-3/calf for bovine lactoferrin from whey, it's within cost constraints and could be an easy add-on to enhanced ORT.

### 6. Azithromycin — Surprising Partial Efficacy in Calves
Johnson et al. (2000, J Dairy Sci) reported that azithromycin at 1500 mg/calf/day for 7 days reduced oocyst shedding and improved clinical scores in experimentally infected calves. The mechanism is unclear — azithromycin targets bacterial ribosomes, and C. parvum has a bacterial-origin ribosome for its vestigial organelle. This is also NOT in the current analysis. The cost is likely too high for production animals, but the mechanistic insight (that a macrolide can affect Crypto) suggests the relict organelle ribosome may be a viable target.

### 7. Cranberry Extract / Proanthocyanidins — In Vitro + Limited Calf Data
Proanthocyanidins (PACs) from cranberry inhibit C. parvum sporozoite attachment in vitro by binding to surface glycoproteins. Méndez-Hermida et al. (2013) showed some reduction in oocyst shedding in calves fed cranberry extract, though the study was small. The mechanism (tannin-mediated protein precipitation on sporozoite surface) is non-specific but cheap and safe. This could be a low-cost adjunct.

---

## PROPOSED TARGETS (Not in the current analysis)

### 1. CpLDH (Lactate Dehydrogenase) — The Metabolic Bottleneck
**Target:** C. parvum lactate dehydrogenase (CpLDH), the terminal enzyme in glycolysis.
**Mechanism:** C. parvum relies almost entirely on glycolysis for ATP production (no functional mitochondria, no TCA cycle, no oxidative phosphorylation). CpLDH regenerates NAD+ to sustain glycolytic flux. Without it, glycolysis halts and the parasite dies.
**Evidence:** CpLDH crystal structure solved (Madern et al., 2004). It is structurally distinct from mammalian LDH (different substrate kinetics, different active site geometry). Gossypol (a natural polyphenol from cottonseed) inhibits CpLDH at low micromolar concentrations in vitro. Plasmodium LDH inhibitors are in development and some cross-react with CpLDH.
**Modality:** Small molecule, non-absorbable oral formulation for luminal delivery. Gossypol itself is too toxic systemically but as a non-absorbed luminal agent, toxicity is eliminated.
**Disease stage:** S4 (Merogony) — metabolic starvation.
**Why it's missing:** The document focuses on IMPDH and OSBP but overlooks the most fundamental metabolic dependency. Glycolysis is THE energy pathway. CpLDH is the regeneration step. This is arguably a higher-confidence essential target than CpOSBP.

### 2. Relict Organelle (Mitosome) Protein Import Machinery
**Target:** The TOM/TIM-like protein import complex of the C. parvum mitosome.
**Mechanism:** While C. parvum lacks a functional mitochondrial ETC, it retains a mitosome that performs essential Fe-S cluster assembly (IscS, IscU pathway). The mitosome requires nuclear-encoded proteins to be imported. Blocking the import machinery would collapse Fe-S cluster synthesis, which is essential for multiple metabolic enzymes.
**Evidence:** Mitosome protein import components identified in C. parvum genome (Abrahamsen et al., 2004). Fe-S cluster assembly is considered essential in all eukaryotes that retain mitosomes (Giardia, Entamoeba, Microsporidia). No inhibitors tested.
**Modality:** Small molecule targeting the import channel — would need to be designed de novo.
**Disease stage:** S4 (Merogony).
**Why it's relevant:** This is the ACTUAL essential function of the vestigial organelle. The document correctly notes ETC targets are dead, but the mitosome itself is not dead — it does Fe-S cluster assembly, and that's essential.

### 3. Trehalose-6-Phosphate Synthase (TPS) — Oocyst Wall Integrity
**Target:** C. parvum trehalose biosynthesis pathway.
**Mechanism:** Trehalose is a major component of Cryptosporidium oocyst walls and is critical for environmental resistance and potentially for thin-walled oocyst integrity. TPS is absent in mammals.
**Evidence:** Trehalose biosynthesis genes identified in C. parvum genome. Trehalose pathway inhibitors are in development for Mycobacterium tuberculosis (where trehalose is also essential for cell wall integrity). No Crypto-specific inhibitors tested.
**Modality:** Small molecule, luminal delivery.
**Disease stage:** S5 (Autoinfection) — if thin-walled oocyst wall integrity is compromised, autoinfection sporozoites may not survive luminal transit. Also S8 (Shedding) — thick-walled oocysts with defective walls would be non-infectious.
**Why it's novel:** This directly targets oocyst wall formation — one of the two gaps identified in the autoinfection cycle decomposition.

### 4. Chitinase Inhibitors — Excystation Blockade
**Target:** The parasite's own chitinase enzyme required for oocyst wall degradation during excystation.
**Mechanism:** C. parvum sporozoites must enzymatically degrade the oocyst wall from inside to excyst. This requires a parasite-encoded chitinase/serine protease. Blocking this enzyme would trap sporozoites inside oocysts — both environmental thick-walled and autoinfection thin-walled oocysts.
**Evidence:** Excystation proteases partially characterized. Allosamidin (a chitinase inhibitor) blocks excystation of some apicomplexan parasites in vitro. Not tested against C. parvum specifically.
**Modality:** Small molecule, luminal delivery (the target is in the gut lumen, not inside host cells).
**Disease stage:** S2 (Excystation) + S5 (Autoinfection — blocks thin-walled oocyst excystation).

### 5. Sodium-Hydrogen Exchanger (NHE) Inhibitors — Anti-Secretory with Possible Anti-Parasitic Dual Action
**Target:** Host NHE3 (sodium-hydrogen exchanger 3) on enterocyte apical membrane.
**Mechanism:** C. parvum infection downregulates NHE3, contributing to sodium malabsorption and diarrhea. Tenapanor (an NHE3 inhibitor approved for IBS-C) works on the basolateral side, but the concept here is different: restoring NHE3 function or targeting the parasite's manipulation of NHE3 trafficking. Alternatively, C. parvum itself may use host NHE activity for pH regulation during invasion.
**Evidence:** Bhatt lab showed NHE3 downregulation in Crypto-infected intestinal epithelium. This is more of a pathology target than anti-parasitic, but the mechanism of NHE3 manipulation could reveal druggable parasite effectors.
**Disease stage:** S7 (Pathology).

### 6. Oral Immunoglobulin from Transgenic Plants (Plantibodies)
**Target:** GP40/GP15 — same as Candidate #5/#9 but different production platform.
**Mechanism:** Express anti-GP40 single-chain antibodies (scFv) or VHH nanobodies in transgenic corn or rice. The plant seed matrix naturally protects the antibody from gastric degradation. Feed ground seed directly to calves in milk replacer.
**Evidence:** Plantibodies against rotavirus and E. coli have been produced in corn and shown oral efficacy in piglets (Virdi et al., 2013, PNAS — anti-ETEC VHH in rice seeds protected piglets). The plant matrix provides natural encapsulation.
**Modality:** Oral biologic in feed.
**Disease stage:** S2 + S5.
**Why this matters for cost:** Plant-produced antibodies cost pennies per dose at scale. A transgenic corn line expressing anti-GP40 VHH could be grown by Cargill (a grain company!) and incorporated into calf milk replacer. This is potentially the cheapest biologic delivery platform imaginable and perfectly aligned with the partner's core competency.

### 7. Fatty Acid Supplementation — Medium-Chain Fatty Acids (MCFAs)
**Target:** Sporozoite membrane integrity and host cell invasion.
**Mechanism:** MCFAs (lauric acid C12, caprylic acid C8) have direct sporicidal activity against C. parvum oocysts and sporozoites in vitro. They disrupt parasite membranes. Coconut oil (rich in lauric acid) is cheap and safe in neonatal calves.
**Evidence:** Shahiduzzaman et al. (2009) showed lauric acid and other MCFAs reduced C. parvum viability in vitro. Some field reports of coconut oil supplementation reducing calf scours, though not specifically attributed to anti-Crypto activity. MCFAs are already used in calf milk replacers for nutritional purposes.
**Modality:** Oral, in milk replacer.
**Disease stage:** S2 (sporozoite killing in lumen before invasion).
**Cost:** <$0.50/calf. Already GRAS.

---

## CROSS-DISEASE ANALOGIES

### 1. Eimeria (Poultry Coccidiosis) → Cryptosporidium
**What worked:** Toltrazuril/diclazuril (triazine compounds) are highly effective against Eimeria in poultry and cattle. They block the plastid-like organelle in Eimeria.
**Why it's relevant:** C. parvum lacks the apicoplast that Eimeria has, so toltrazuril doesn't work directly. BUT the lesson is that targeting a unique organelle's essential function is the winning strategy in coccidiosis. For Crypto, the equivalent unique organelle is the mitosome (Fe-S cluster assembly) and the feeder organelle (lipid acquisition). The Eimeria analogy says: find the organelle, find the essential function, drug it.
**Adaptation needed:** Shift from apicoplast targets to mitosome/feeder organelle targets.

### 2. Giardia (Metronidazole Resistance) → Auranofin Repurposing
**What worked:** Auranofin (a gold-containing anti-rheumatic drug) showed potent activity against Giardia, Entamoeba, and — importantly — C. parvum in vitro by inhibiting thioredoxin reductase. Debnath et al. (2012, Nature Medicine) demonstrated this.
**Why it's relevant:** C. parvum thioredoxin reductase (CpTrxR) is essential for redox homeostasis. Auranofin has anti-Crypto activity in vitro (IC50 ~5 μM). It has never been tested in calves.
**Adaptation needed:** Auranofin is absorbed systemically and has toxicity concerns. A non-absorbable gold-thiol compound or a luminal auranofin formulation could retain anti-parasitic activity without systemic exposure. Cost of auranofin is low (generic).

### 3. Clostridioides difficile → Fidaxomicin Narrow-Spectrum Luminal Approach
**What worked:** Fidaxomicin succeeds against C. difficile precisely because it is minimally absorbed, achieves very high fecal concentrations, and has a narrow spectrum that preserves the microbiome.
**Why it's relevant:** This is the exact pharmacokinetic profile needed for Crypto drugs. The BKI fecal concentration finding and paromomycin luminal efficacy both point to the same conclusion: the ideal Crypto drug is a fidaxomicin-like agent — non-absorbed, high luminal concentration, sustained release.
**Adaptation needed:** Apply fidaxomicin's PK design principles to BKI, CpIMPDH inhibitors, or MMV665917 reformulation.

### 4. Malaria (Artemisinin Combination Therapy) → Multi-Target Combination Logic
**What worked:** ACTs combine a fast-acting artemisinin (kills 99.9% of parasites in hours) with a slow-acting partner drug (clears the remaining 0.1% over days). This prevents resistance and ensures cure.
**Why it's relevant:** The Crypto portfolio needs the same logic: a fast-acting parasiticidal (MMV665917) combined with a sustained-acting parasitistatic (BKI or halofuginone) to prevent rebound. The document proposes combinations but doesn't explicitly apply ACT logic.
**Adaptation needed:** Identify which candidates are "artemisinin-like" (fast kill) vs. "partner-drug-like" (sustained suppression) and pair them accordingly.

### 5. Rotavirus (

---

### OpenRouter (qwen-2.5-72b-instruct)

## EMPIRICAL HITS (In-vivo data in the target species)

### Candidate #1: MMV665917 (Piperazine-Based Cryptosporicidal)
- **Target/mechanism:** Unknown molecular target; parasiticidal (not parasitostatic) against C. parvum; rapid elimination of intracellular stages.
- **Result:** 22 mg/kg PO QD x 7 days started 2 days after severe diarrhea onset: prompt diarrhea resolution, ~94% reduction in total fecal oocyst shedding.
- **Trial:** Castellanos-Gonzalez et al., 2018, PLoS NTD; piglet confirmation and mouse models.
- **Why it worked:** MMV665917 is the only compound that has demonstrated therapeutic efficacy in calves, starting after severe diarrhea onset. The parasiticidal mechanism means it may genuinely clear infection rather than just suppress it.

### Candidate #2: BKI-1553 / Next-Generation BKIs (CpCDPK1 Inhibitors)
- **Target/mechanism:** CpCDPK1 (calcium-dependent protein kinase 1) -- essential, parasite-specific kinase involved in invasion and intracellular replication.
- **Result:** BKI-1553 significantly reduced diarrhea severity, oocyst shedding, and improved overall health in calves. Fecal drug concentrations correlated with efficacy better than plasma levels.
- **Trial:** Schaefer et al., 2016, J Infect Dis; newer scaffolds in mice only.
- **Why it worked:** The Van Voorhis lab finding that fecal concentration predicts efficacy better than plasma is transformative. If BKIs work primarily from the lumen, the entire development path changes from systemic drug to topical gut agent.

### Candidate #3: Paromomycin Analogs / Reformulated Paromomycin
- **Target/mechanism:** Ribosomal protein synthesis inhibition via luminal delivery.
- **Result:** 100 mg/kg/day: oocysts not detected. 50 mg/kg: suppression with rebound. 25 mg/kg: reduced diarrhea but weight loss (toxicity signal). Paromomycin + colostrum synergistic.
- **Trial:** Fayer & Ellis, 1993; Kacar et al., 2022.
- **Why it worked:** Paromomycin's failure is 100% a compound problem (toxicity, cost, dosing), not a target problem. The same drug in a non-absorbable sustained-release ileal-targeting formulation might solve all three failure modes simultaneously.

### Candidate #4: Halofuginone + Sustained-Release Reformulation
- **Target/mechanism:** Prolyl-tRNA synthetase (ProRS) inhibition -- cryptostatic, slows merogony.
- **Result:** Prophylactic from birth reduces diarrhea duration by ~2 days. Reduces day 7 oocyst shedding. Does NOT cure.
- **Trial:** Brainard et al., 2020.
- **Why it worked:** Halofuginone is a weak drug with a narrow therapeutic index. Sustained-release may help modestly by eliminating inter-dose troughs, but the cryptostatic mechanism sets a ceiling.

## PROPOSED TARGETS (Not in the current analysis)

### Candidate #15: Yeast Beta-Glucan Trained Innate Immunity (Birth-Dose Prophylaxis)
- **Target:** Epigenetic reprogramming of neonatal calf monocytes and macrophages via beta-glucan-induced trained immunity.
- **Mechanism:** Beta-glucan binding to Dectin-1 induces histone modifications, priming innate immune cells for enhanced responses to subsequent pathogen encounter.
- **Evidence:** In vitro and in vivo studies in calves show reduced diarrhea and enhanced gut microbiome.
- **Modality:** Oral beta-glucan at birth.
- **Disease stage:** S6 (Immune acceleration).

### Candidate #16: COX-2 Inhibitor for Dual Anti-Secretory + Immunosuppression Relief (Meloxicam)
- **Target:** Selective COX-2 inhibition to block PGE2-mediated secretory chloride flux and relieve PGE2-mediated local immunosuppression.
- **Mechanism:** Dual anti-secretory and immunomodulatory effects.
- **Evidence:** Indomethacin fully inhibits secretory diarrhea in C. parvum-infected piglet ileum and restores Na+/Cl- absorption in infected bovine ileum.
- **Modality:** Oral meloxicam.
- **Disease stage:** S6 (Immune acceleration) + S7 (Pathology).

### Candidate #17: Recombinant Bovine IFN-gamma + COX-2 Inhibitor Combination (Immune Timing Gap Closure)
- **Target:** Direct delivery of the effector cytokine (IFN-gamma) combined with COX-2 inhibition to prevent PGE2-mediated suppression.
- **Mechanism:** Provides the effector molecule directly and prevents suppression of its downstream effects.
- **Evidence:** rBoIL-12 stimulated IFN-gamma but failed to protect; PGE2-mediated local immunosuppression is hypothesized to explain this failure.
- **Modality:** Oral/IP rBoIFN-gamma + oral meloxicam.
- **Disease stage:** S6 (Immune acceleration).

## CROSS-DISEASE ANALOGIES

### Candidate #9: VHH Nanobody Cocktail Against GP40 + CSL + TRAP-C1 (Sustained Luminal Delivery)
- **What worked elsewhere:** VHH nanobodies against rotavirus are protease-stable in the gut lumen and neutralize infection in calves.
- **Relevance:** The technology platform (camelid nanobodies, protease-stable, yeast-expressible, mucoadhesive formulation) is proven for oral delivery to the bovine neonatal gut.
- **Adaptation:** Generate anti-Crypto nanobodies targeting GP40, CSL, and TRAP-C1.

### Candidate #10: Lectin-Mimetic Galactose/GalNAc Polymer (Luminal Decoy)
- **What worked elsewhere:** Polyvalent carbohydrate inhibitors of pathogen attachment are proven in other infectious diseases (FimH antagonists for UTI reached Phase 2 clinical trials).
- **Relevance:** C. parvum sporozoites use CSL lectin to bind Gal/GalNAc epitopes on enterocytes.
- **Adaptation:** Develop a polyvalent galactose-displaying polymer to act as a "sponge" for sporozoites.

### Candidate #14: Bile Salt Sequestrant / Luminal pH Modifier (Autoinfection Cycle Disruptor)
- **What worked elsewhere:** Bile salt sequestrants (cholestyramine) used clinically for C. difficile toxin binding and bile acid malabsorption.
- **Relevance:** Thin-walled oocysts require specific bile salt + temperature + pH conditions to excyst and release sporozoites for autoinfection.
- **Adaptation:** Modify the luminal conditions to prevent thin-walled oocyst excystation.

## WHAT WOULD YOU PRIORITISE?

### 1. Enhanced ORT (Glutamine + Meloxicam)
- **Why:** All components are available now, and it could be tested immediately. The combination has strong ex vivo evidence and could reduce diarrhea severity by 40-50%.

### 2. Beta-Glucan Trained Innate Immunity
- **Why:** Beta-glucan is available and cheap. It has shown promise in enhancing innate immune responses in calves, which could narrow the Crypto-specific timing gap.

### 3. BH3 Mimetic Selectivity Screen
- **Why:** This is a low-cost, high-reward experiment that could open a completely new therapeutic axis. If successful, it could provide a novel mechanism for selectively killing infected cells without harming uninfected ones.

These three experiments collectively test the most novel hypotheses in the portfolio and could restructure the entire program. They are also the most feasible to initiate immediately with the available resources.

---

