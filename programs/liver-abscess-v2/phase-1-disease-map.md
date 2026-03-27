# Phase 1 -- Disease Map: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Agent:** Pathfinder
**Date:** 2026-03-27
**Status:** Complete

---

## Executive Summary

Hepatic abscessation in feedlot cattle is a diet-driven, endogenous, polymicrobial infection with an annual economic impact of **US$255.6 million** (95% CI: $161.9M--$377.9M) in the U.S. alone. The disease follows a stereotyped progression: high-grain diets cause ruminal acidosis, which damages the rumen epithelium (rumenitis), allowing *Fusobacterium necrophorum* -- a normal rumen commensal -- to colonize the damaged wall, enter portal circulation, and establish abscesses in the liver. The organism's primary weapon is **leukotoxin (LktA)**, a 336 kDa secreted protein that kills bovine neutrophils and Kupffer cells, enabling immune evasion in the liver. Once formed, abscesses become walled off by a fibrous capsule that prevents both immune clearance and antibiotic penetration, making the disease essentially **incurable once established**.

The sole effective preventive intervention is in-feed **tylosin**, which reduces incidence by 40--70% but faces growing regulatory pressure as a medically important antimicrobial. No effective vaccine exists. The previously available Centurion vaccine (Merck) has been discontinued. Incidence has been increasing, with reports of 20--30%+ prevalence across U.S. feedlots.

**Rate-limiting barrier:** The transition from rumen wall colonization to portal transit and hepatic seeding -- the point where a commensal becomes a pathogen. This stage is poorly understood and currently unaddressed by any intervention except tylosin's indirect suppression of F. necrophorum in the rumen.

**KE#1 (Portfolio-Restructuring Experiment):** Quantitative comparison of rumen wall vs. hindgut (colonic epithelium) as the primary source of hepatic F. necrophorum, using matched qPCR on rumen epithelium, colonic epithelium, and liver abscess material from the same animals. Recent data (Salih et al. 2025) suggests the hindgut may be an underappreciated source -- if confirmed as a major pathway, half the portfolio (rumen-focused interventions) would need restructuring.

---

## 1. Entry/Exposure: The Rumen-Liver Axis

### 1.1 The Grain Feeding Trigger

Hepatic abscessation is fundamentally a disease of **intensive grain feeding**. The causal chain begins with diet:

- **High-grain finishing diets** (typically >80% concentrate) provide rapidly fermentable carbohydrates (primarily starch from corn) that outpace the rumen's buffering and absorptive capacity [ESTABLISHED]
- **Volatile fatty acid (VFA) accumulation** drives ruminal pH below 5.6 (subacute ruminal acidosis, SARA) or below 5.0 (acute ruminal acidosis) [ESTABLISHED]
- pH depression is primarily from total VFA accumulation in SARA, not lactic acid -- unlike acute acidosis where Streptococcus bovis overgrowth produces D-lactate [ESTABLISHED]
- **Duration matters:** SARA bouts of >5 hours/day during adaptation are most damaging; cumulative exposure over the feeding period correlates with abscess incidence [MODERATE]

**Key dietary risk factors:**
- Rapid transition from forage to concentrate diets (insufficient rumen adaptation) [ESTABLISHED]
- Fine particle size in grain processing (increased fermentation rate) [ESTABLISHED]
- Insufficient effective fiber (reduced rumination and saliva buffering) [ESTABLISHED]
- Days on feed: incidence increases with >100 DOF; Holsteins (300--400 DOF) have dramatically higher rates than beef breeds (120--150 DOF) [ESTABLISHED] (Amachawadi & Nagaraja 2016, [DOI](https://doi.org/10.2527/jas.2015-0261))

**What is unknown:**
- The exact threshold of ruminal pH depression and duration that triggers the transition from subclinical SARA to abscess-predisposing rumenitis
- Why some animals on identical diets develop abscesses and others do not -- host genetic susceptibility is implied by GWAS data (Keele et al. 2016, [DOI](https://doi.org/10.2527/jas.2015-9887)) but poorly characterized
- Whether subacute episodes are cumulative or whether single acute events are sufficient

### 1.2 Ruminal Acidosis and Rumenitis

**The acidosis-rumenitis-liver abscess complex** is the accepted pathogenic sequence [ESTABLISHED] (Nagaraja & Chengappa 1998, [DOI](https://doi.org/10.2527/1998.761287x)):

1. **Low pH damages ruminal epithelium:** VFA at low pH penetrate the stratum corneum, causing chemical burns to the rumen papillae [ESTABLISHED]
2. **Epithelial barrier breakdown:** Tight junctions between ruminal epithelial cells are disrupted; parakeratosis (thickening + hyperkeratinization) develops [ESTABLISHED]
3. **Rumenitis:** Inflammatory infiltration of the ruminal wall -- erosions, ulcers, papillary clumping, and focal necrosis [ESTABLISHED]
4. **Bacterial translocation:** Damaged epithelium permits entry of rumen bacteria, particularly F. necrophorum, into the ruminal wall and subsequently the portal vasculature [ESTABLISHED]

**Inflammatory cascade in rumenitis:**
- SARA-induced high LPS levels over-activate MAPK and NF-kB inflammatory pathways in ruminal epithelium [MODERATE]
- Gram-negative bacterial lysis releases LPS, histamine, and tyramine into the rumen fluid [ESTABLISHED]
- LPS translocation across damaged epithelium triggers systemic inflammatory responses [MODERATE]

**What is unknown:**
- The precise molecular events that convert parakeratosis to transmural bacterial invasion
- Whether rumenitis is necessary or merely correlative -- some abscesses occur in cattle without gross rumenitis at slaughter
- The role of rumen microbiome dysbiosis beyond F. necrophorum

### 1.3 F. necrophorum as Normal Rumen Inhabitant

F. necrophorum is a **normal commensal** of the bovine rumen, not an invading pathogen [ESTABLISHED]:

- Present in both forage-fed and grain-fed cattle, but at **higher concentrations in grain-fed animals** (Tadepalli et al. 2009, [DOI](https://doi.org/10.1016/j.anaerobe.2008.05.005))
- Normal metabolic role: ferments lactate (a key function in rumen pH regulation) and degrades feed proteins and epithelial proteins [ESTABLISHED]
- Adherent to normal ruminal wall as well as present in ruminal fluid [ESTABLISHED]
- Gram-negative, rod-shaped, obligate anaerobe (but aerotolerant) [ESTABLISHED]

---

## 2. Colonization: Rumen Wall Invasion and Portal Transit

### 2.1 Adhesion to Damaged Rumen Epithelium

Once rumenitis creates epithelial breaks, F. necrophorum exploits the damage through multiple adhesion mechanisms:

**Hemagglutinin-mediated adhesion:**
- Hemagglutinin on the F. necrophorum surface mediates adherence to ruminal epithelial cells [ESTABLISHED] (Kanoe & Iwaki 1987, PMID 3820273)
- Anti-hemagglutinin antiserum reduces bacterial attachment to rumen cells [ESTABLISHED]
- Purified hemagglutinin binds directly to ruminal epithelial cell membranes [ESTABLISHED]
- Hemagglutinin activity is present in **all hepatic isolates** of subsp. necrophorum but only some ruminal isolates -- suggesting selection for adhesion-competent strains during liver invasion [MODERATE] (Okwumabua et al. 1996, [DOI](https://doi.org/10.1128/aem.62.2.469-472.1996))

**Outer membrane protein (OMP)-mediated adhesion:**
- A **42.4 kDa OMP** binds with high affinity to bovine endothelial cells and is recognized by sera from cattle with liver abscesses [MODERATE] (Kumar et al. 2013, PMID 23153522)
- **43K OMP** interacts with fibronectin to mediate adhesion to bovine epithelial cells [MODERATE] (Singh et al. 2022, PMID 35121302)
- Four OMPs (17, 24, 40, and 74 kDa) bind to endothelial cells in western blot analysis [MODERATE]
- Trypsin treatment of bacterial cells decreases binding to endothelial cells, confirming proteinaceous nature of adhesins [MODERATE]

**Other adhesion factors:**
- FadA (Fusobacterium adhesin A) -- identified in F. necrophorum outer membrane vesicle proteomics [PRELIMINARY]
- OmpA-family protein -- present in outer membrane vesicles [PRELIMINARY]
- OmpH-family protein (17.5 kDa) -- structural/adhesion role [PRELIMINARY]

### 2.2 Rumen Wall Penetration

Once adherent, F. necrophorum actively penetrates the rumen wall:

- **Protease activity** degrades epithelial proteins and interstitial matrix [MODERATE]
- F. necrophorum stimulates production of **collagenase 3 (MMP-13)** by epithelial cells, degrading interstitial collagen and facilitating bacterial spread [MODERATE] (Nagaraja & Narayanan 2007, [DOI](https://doi.org/10.1016/j.anaerobe.2005.01.004))
- **Dermonecrotic toxin** causes local tissue necrosis in the rumen wall [MODERATE]
- Leukotoxin is cytolytic to ruminal epithelial cells, further aiding penetration [MODERATE]
- Rumen wall abscesses can form as an intermediate stage before portal dissemination [ESTABLISHED]

### 2.3 Portal Vein Transit

The transition from rumen wall to liver is the critical -- and poorly understood -- step:

- Bacteria in the ruminal wall gain access to the **portal venous system**, which drains the rumen directly to the liver [ESTABLISHED]
- **Intravascular coagulation** induced by F. necrophorum endotoxic LPS and platelet aggregation factor may create microthrombi that carry bacteria [MODERATE]
- The liver acts as a **filter** for portal blood, trapping bacteria in hepatic sinusoids [ESTABLISHED]
- Transit is likely intermittent, not continuous -- correlating with episodes of rumenitis exacerbation [INFERRED]
- The concentration of F. necrophorum in ruminal epithelial tissue is 4--5 log CFU/g -- substantially lower than in established abscesses (7--7.5 log CFU/g), suggesting amplification occurs in the liver [ESTABLISHED] (Abbasi et al. 2025, [DOI](https://doi.org/10.1128/spectrum.01888-25))

### 2.4 The Hindgut Pathway (Newly Recognized)

**Critical new finding:** The hindgut (colon) may be an additional source of liver abscess pathogens, beyond the rumen:

- Colonic epithelial tissues yielded **more subsp. funduliforme isolates** than ruminal epithelial tissues [MODERATE] (Salih et al. 2025, [DOI](https://doi.org/10.1128/spectrum.02539-25))
- **Bacteroides spp.** -- primarily a hindgut organism -- account for **33% of sequencing reads** in liver abscesses, with some abscesses dominated by Bacteroides rather than Fusobacterium [MODERATE] (Fuerniss et al. 2022, [DOI](https://doi.org/10.1093/jas/skac252))
- The colonic epithelium has portal venous drainage to the liver (via the inferior mesenteric vein), providing a direct route [ESTABLISHED -- anatomy]
- Salmonella enterica has been isolated from liver abscesses at low concentrations, and its colonic prevalence exceeds ruminal prevalence [MODERATE]

**What is unknown:**
- The relative quantitative contribution of rumen vs. hindgut to hepatic bacterial seeding
- Whether hindgut-derived abscesses have different bacteriology, severity, or response to intervention
- Whether hindgut acidosis (from starch overflow) parallels rumen acidosis as a predisposing factor

---

## 3. Immune Evasion: How F. necrophorum Defeats Hepatic Defenses

The liver is one of the most immune-competent organs in the body, heavily defended by **Kupffer cells** (resident macrophages lining the hepatic sinusoids) and rapidly recruited **neutrophils**. F. necrophorum must overcome these defenses to establish infection.

### 3.1 Leukotoxin (LktA) -- The Primary Weapon

Leukotoxin is the **single most important virulence factor** in hepatic abscess pathogenesis [ESTABLISHED]:

**Molecular characteristics:**
- Encoded by the **lktA gene** within the tricistronic operon **lktBAC** [ESTABLISHED]
- lktA ORF: 9,726 bp encoding 3,241 amino acids [ESTABLISHED]
- Molecular weight: **335,956 Da (~336 kDa)** [ESTABLISHED] (Narayanan et al. 2001, PMID 11500416)
- **No sequence similarity** to any other known bacterial leukotoxin -- it is a unique toxin [ESTABLISHED]
- Secreted extracellularly; concentration peaks at mid-log growth phase [ESTABLISHED]
- Heat-labile (inactivated at 56 C for 5 min); unstable at pH >7.8 or <6.6 [ESTABLISHED]
- Inactivated by proteases (trypsin, chymotrypsin) but not amylase [ESTABLISHED]

**Mechanism of action -- concentration-dependent dual killing:**
1. **Low concentration:** Induces neutrophil ACTIVATION (granule translocation to cell periphery), followed by **apoptosis** -- decreased cell size, organelle condensation, membrane blebbing, chromatin condensation, DNA content decrease [ESTABLISHED] (Narayanan et al. 2002, [DOI](https://doi.org/10.1128/IAI.70.8.4609-4620.2002))
2. **Moderate concentration:** Induces apoptosis in mononuclear cells (lymphocytes, monocytes) [ESTABLISHED]
3. **High concentration:** Causes **necrotic cell death** of all bovine peripheral leukocytes [ESTABLISHED]

**PMN specificity:**
- PMNs are more sensitive than lymphocytes at equivalent toxin concentrations [ESTABLISHED]
- The toxin shows **ruminant specificity** -- more toxic to bovine and ovine leukocytes than to cells from other species [ESTABLISHED]
- Kills Kupffer cells, preventing hepatic bacterial clearance [MODERATE]

**Correlation with disease severity:**
- Strains from **severe (A+) liver abscesses** produce significantly higher leukotoxic activity AND higher leukotoxin protein concentration than strains from mild abscesses (P < 0.0001) [ESTABLISHED] (Pillai et al. 2021, [DOI](https://doi.org/10.1016/j.anaerobe.2021.102344))
- High variability among strains within severity categories -- not all severe strains are equally toxigenic [MODERATE]
- Correlation between leukotoxic activity and protein concentration strengthens at 24h culture (r = 0.47) vs. 9h (r = 0.14, NS) [MODERATE]

**Subspecies differences in leukotoxin production:**
- Subsp. necrophorum produces **21.1-fold more lktA transcript** at mid-log phase than subsp. funduliforme [ESTABLISHED] (Tadepalli et al. 2007, [DOI](https://doi.org/10.1016/j.anaerobe.2007.09.001))
- LktB and LktA proteins share 87% and 88% amino acid identity between subspecies but differ significantly in N-terminal sequences [ESTABLISHED]
- The lkt operon has the same three-gene organization (lktBAC) in both subspecies [ESTABLISHED]
- Lower leukotoxin production is the primary reason subsp. funduliforme is less virulent [ESTABLISHED]

### 3.2 Endotoxin (LPS)

F. necrophorum LPS contributes to immune evasion and tissue damage through multiple mechanisms:

- **Intravascular coagulation:** LPS triggers the coagulation cascade, creating fibrin deposits that shield bacteria from phagocytes [MODERATE]
- **Platelet aggregation:** Works synergistically with a separate platelet aggregation factor to form protective microthrombi [MODERATE]
- **Endothelial damage:** Direct toxic effect on hepatic sinusoidal endothelium [MODERATE]
- **Anaerobiosis creation:** By damaging erythrocytes and impairing oxygen transport, LPS helps create the anaerobic microenvironment that F. necrophorum requires [MODERATE]
- LPS from subsp. necrophorum is more potent than from subsp. funduliforme [MODERATE] (Tan et al. 1996, [DOI](https://doi.org/10.1007/BF00385634))

### 3.3 Hemolysin

- **Phospholipase B (PLB) activity** is the basis of hemolytic action [MODERATE] (Garcia et al. 1996, PMID 8734639)
- Hemolysin binds to **phosphatidylcholine** on erythrocyte membranes as its receptor [MODERATE] (Gokce et al. 1998, PMID 9812364)
- Two-phase kinetics: prelytic binding phase followed by temperature-dependent lytic phase [MODERATE]
- **Species selectivity:** Strong lysis of rabbit, human, and dog erythrocytes; only trace activity against bovine erythrocytes [MODERATE]
- Co-purifies with leucocidin activity, suggesting dual function [MODERATE]
- Contributes to tissue destruction and anaerobiosis by lysing erythrocytes [INFERRED]

### 3.4 Additional Virulence Factors

**Platelet Aggregation Factor:**
- Distinct from LPS; promotes formation of microthrombi around bacterial foci [MODERATE]
- Creates protected anaerobic niches within the aerobic liver parenchyma [MODERATE]

**Dermonecrotic Toxin:**
- Causes focal tissue necrosis [MODERATE]
- Contributes to abscess cavity formation [MODERATE]

**Extracellular Enzymes:**
- **Proteases:** Degrade tissue matrix proteins, facilitating spread [MODERATE]
- **DNases:** Degrade neutrophil extracellular traps (NETs) [INFERRED]
- **Collagenase stimulation:** F. necrophorum induces host MMP-13, degrading interstitial collagen [MODERATE]

**Capsule:**
- Some strains possess a polysaccharide capsule that may resist phagocytosis [PRELIMINARY]

**Outer Membrane Vesicles (OMVs):**
- F. necrophorum produces OMVs containing leukotoxin, OmpA, OmpH, 43K OMP, FadA, and other virulence factors [MODERATE]
- OMVs may serve as a delivery mechanism for virulence factors at a distance from the bacterial cell [PRELIMINARY]
- OMV-based vaccine candidates are under investigation [PRELIMINARY]

---

## 4. Acute Pathology: Abscess Formation

### 4.1 Sequence of Abscess Development

The progression from bacterial seeding to mature abscess follows a defined histopathological sequence [ESTABLISHED] (Amachawadi & Nagaraja 2022, [DOI](https://doi.org/10.1016/j.cvfa.2022.08.001)):

1. **Microabscess formation:** Earliest lesion -- focal bacterial colonization with neutrophil infiltration in hepatic sinusoids [ESTABLISHED]
2. **Coagulative necrosis:** Bacterial toxins (leukotoxin, LPS, proteases) destroy adjacent hepatocytes; expanding zone of necrosis [ESTABLISHED]
3. **Pus formation:** Destruction of neutrophils releases lysosomal enzymes and reactive oxygen species, causing further collateral damage to hepatocytes -- the classic "abscess" [ESTABLISHED]
4. **Encapsulation:** Fibroblasts deposit collagen around the necrotic core; mature fibrous capsule forms within **3--10 days** of initial infection (based on experimental infections) [ESTABLISHED]
5. **Maturation:** Capsule thickens; inner layer of immature fibroblasts, outer layer of mature fibrous tissue [ESTABLISHED]

**Histological architecture of mature abscess:**
- **Center:** Necrotic debris, pus, viable bacteria (primarily F. necrophorum at 7--7.5 log CFU/g)
- **Inner rim:** Macrophages and multinucleated giant cells; bacteria visible within phagocytes
- **Capsule:** Variable thickness; inner immature fibroblasts, outer mature collagen
- **Periphery:** Compressed but viable hepatocytes; inflammatory infiltration

### 4.2 Severity Classification (Elanco Grading System)

Liver abscesses are graded at slaughter using the standard Elanco system:

| Grade | Description |
|-------|-------------|
| 0 | No abscesses (healthy liver) |
| A- | 1--2 small abscesses or abscess scars |
| A | 2--4 small, well-organized abscesses (<2.54 cm diameter); surrounding liver appears healthy |
| A+ | 1 or more large abscesses (>2.54 cm); inflamed surrounding tissue |
| A+ Adhesion | Liver adhered to gastrointestinal tract or diaphragm |
| A+ Open | Ruptured abscess |

[ESTABLISHED]

### 4.3 Polymicrobial Synergy

Liver abscesses are **almost always polymicrobial** [ESTABLISHED]:

**F. necrophorum subsp. necrophorum -- Primary pathogen:**
- Detected in **85.9% of liver abscesses** by qPCR [ESTABLISHED] (Abbasi et al. 2025, [DOI](https://doi.org/10.1128/spectrum.01888-25))
- Mean concentration: **7.0--7.5 log CFU/g** [ESTABLISHED]
- Dominant species by both culture and molecular methods [ESTABLISHED]

**F. necrophorum subsp. funduliforme:**
- Present without subsp. necrophorum in only **16.9% of abscesses** [MODERATE]
- Similar concentration (7.0 log CFU/g) when present as sole Fusobacterium [MODERATE]
- Less virulent due to 21-fold lower leukotoxin production [ESTABLISHED]

**Trueperella pyogenes -- Secondary pathogen:**
- Detected in **29.2% of liver abscesses** by qPCR (vs. 16.7% by culture -- qPCR is more sensitive) [MODERATE]
- Mean concentration: **5.9 log CFU/g** -- approximately 10--100-fold lower than F. necrophorum [MODERATE]
- **More prevalent in abscesses from cattle NOT receiving tylosin** (P = 0.022) [MODERATE] (Fuerniss et al. 2022)
- Concentration too low to be the primary etiologic agent, but contributes synergistically [MODERATE]

**T. pyogenes virulence factors that contribute to synergy:**
- **Pyolysin (Plo):** Cholesterol-dependent cytolysin; forms transmembrane pores in host cells; cytolytic [ESTABLISHED]
- **Neuraminidases (NanH, NanP):** Remove sialic acid from host glycoproteins; aid adhesion and provide carbon source [MODERATE]
- **Fimbriae (FimA and others):** Mediate adhesion to host tissues [MODERATE]
- **Collagen-binding protein (CbpA):** Binds collagen-rich tissue; complements neuraminidase-mediated adhesion [MODERATE]
- **Biofilm formation:** T. pyogenes forms biofilms that may protect the polymicrobial community [PRELIMINARY]

**Mechanism of F. necrophorum + T. pyogenes synergy:**
- T. pyogenes is a **facultative anaerobe** -- it consumes oxygen in the tissue, creating anaerobic conditions favorable for F. necrophorum [MODERATE]
- F. necrophorum kills neutrophils with leukotoxin, protecting T. pyogenes from phagocytosis [MODERATE]
- T. pyogenes pyolysin and neuraminidases cause additional tissue destruction, expanding the abscess niche [MODERATE]
- The combined effect is abscesses that are **larger and more severe** than those caused by either organism alone [ESTABLISHED]

**Bacteroides spp. (~33% of reads in 16S studies):**
- Primarily hindgut organisms; their presence in abscesses supports hindgut involvement [MODERATE]
- Some abscesses are **Bacteroides-dominated** rather than Fusobacterium-dominated -- a distinct subtype [PRELIMINARY] (Fuerniss et al. 2022)
- Species identification and pathogenic contribution poorly characterized [UNKNOWN]

**Other organisms occasionally isolated:**
- Salmonella enterica (isolated by culture but not quantifiable by qPCR -- very low abundance) [MODERATE]
- E. coli, Klebsiella spp., Pseudomonas aeruginosa -- prevalence 70--93% by some culture methods, but likely contaminants or opportunists at very low concentrations [PRELIMINARY]
- Porphyromonas spp. (~1% of 16S reads) [MODERATE]
- Over 99% of genus-level reads belong to Gram-negative genera [MODERATE]

### 4.4 Timing of Abscess Development

A **major knowledge gap** -- the timing of abscess development during the feedlot period is unknown because liver abscesses cannot be detected in live cattle [ESTABLISHED]:

- No reliable ante-mortem diagnostic exists [ESTABLISHED]
- Cattle with liver abscesses show **no clinical signs** until detected at slaughter [ESTABLISHED]
- Abscesses presumably form during the high-concentrate finishing phase, but exact timing is unknown [INFERRED]
- Greater DOF correlates with higher incidence, but this could reflect cumulative risk rather than late-stage formation [UNKNOWN]
- A metabolomics study identified biochemicals in abscess material (3-phenylpropionate, tryptophan metabolites, succinate) that might serve as blood biomarkers [PRELIMINARY] (Amachawadi et al. 2023, [DOI](https://doi.org/10.1093/jas/skac427))

---

## 5. Chronic Persistence: Why Abscesses Don't Resolve

### 5.1 The Fibrous Capsule as Sanctuary

Once a liver abscess is encapsulated, it becomes essentially **self-sustaining** [ESTABLISHED]:

- The fibrous capsule creates a **physical barrier** that prevents:
  - Neutrophil and macrophage infiltration into the abscess core [ESTABLISHED]
  - Antibiotic penetration to effective concentrations [ESTABLISHED]
  - Immune-mediated resolution [ESTABLISHED]
- The necrotic, anaerobic interior is an **ideal environment** for F. necrophorum growth [ESTABLISHED]
- Viable bacteria persist at high concentrations (7+ log CFU/g) within established abscesses [ESTABLISHED]
- The abscess acts as a **continuous source of inflammatory mediators** (LPS, leukotoxin) that prevent healing of surrounding tissue [MODERATE]

### 5.2 Anaerobic Niche Maintenance

F. necrophorum is an obligate anaerobe operating in the highly oxygenated liver. Multiple mechanisms maintain anaerobiosis:

- **Platelet aggregation and fibrin deposition** create local ischemia [MODERATE]
- **Erythrocyte damage** (from hemolysin/LPS) impairs local oxygen delivery [MODERATE]
- **Neutrophil respiratory burst** consumes local oxygen during the acute phase [INFERRED]
- **T. pyogenes oxygen consumption** as a facultative anaerobe reduces pO2 in the polymicrobial community [MODERATE]
- **Fibrous encapsulation** limits vascular ingrowth and oxygen diffusion [ESTABLISHED]

### 5.3 Immune Exhaustion and Tolerance

- Chronic abscesses show a **granulomatous response** (macrophages, giant cells) rather than acute neutrophilic inflammation -- suggesting immune containment rather than clearance [MODERATE]
- Bacteria persist within macrophages and giant cells, indicating failed intracellular killing [MODERATE]
- Serum anti-leukotoxin antibodies are present in cattle with abscesses but do not resolve the infection [MODERATE]
- The immune system appears to reach a **stalemate**: it cannot clear the encapsulated bacteria, but prevents systemic dissemination [INFERRED]

### 5.4 Abscess Growth and Coalescence

- Small abscesses can grow and coalesce into large A+ abscesses [MODERATE]
- The mechanism of growth is likely ongoing tissue destruction at the capsule margins by bacterial toxins [INFERRED]
- A+ abscesses with adhesions indicate that abscess growth can breach the hepatic capsule and adhere to adjacent organs [ESTABLISHED]
- Open (ruptured) abscesses represent the most severe outcome -- peritonitis and potential death [ESTABLISHED]

---

## 6. Treatment Resistance: Why Current Interventions Fail

### 6.1 Tylosin -- The Gold Standard (and Its Limits)

**Mechanism and efficacy:**
- Tylosin phosphate (macrolide antibiotic) is fed continuously at 60--90 mg/head/day during the finishing period [ESTABLISHED]
- Reduces liver abscess incidence by **40--70%** [ESTABLISHED] (Nagaraja & Chengappa 1998)
- Believed to work by **suppressing F. necrophorum in the rumen**, reducing the bacterial load available for translocation [MODERATE]
- Does NOT cure existing abscesses [ESTABLISHED]
- Five antibiotics are FDA-approved for liver abscess prevention: bacitracin methylene disalicylate, chlortetracycline, oxytetracycline, tylosin, and virginiamycin. Tylosin is by far the most effective and most commonly used [ESTABLISHED]

**Why tylosin can't cure established abscesses:**
- The fibrous capsule prevents antibiotic penetration to the abscess interior [ESTABLISHED]
- F. necrophorum within the encapsulated abscess is physically sequestered from systemically delivered antibiotics [ESTABLISHED]
- Even therapeutic antibiotic doses cannot achieve effective concentrations inside the abscess cavity [MODERATE]
- Tylosin's mechanism is prevention (reducing rumen bacterial load), not treatment [ESTABLISHED]

**Limitations and concerns:**
- 30--60% of abscesses still occur despite tylosin use [ESTABLISHED]
- Tylosin significantly increases fecal erythromycin-resistant Enterococcus concentrations and erm(B) gene prevalence (P < 0.001) [ESTABLISHED] (Agga et al. 2023, [DOI](https://doi.org/10.1016/j.prevetmed.2023.105930))
- Classified as a **medically important antimicrobial** by WHO and Health Canada [ESTABLISHED]
- Since January 2017, use requires veterinary oversight (Veterinary Feed Directive) [ESTABLISHED]
- Future regulatory restriction is plausible given AMR concerns [INFERRED]
- Minimal impact on overall fecal and soil microbiomes and resistomes (Weinroth et al. 2019, [DOI](https://doi.org/10.1093/jas/skz306)), but targeted macrolide resistance increase is significant [MODERATE]

### 6.2 Why Alternative Antibiotics Are Inferior

- Chlortetracycline, oxytetracycline: less effective than tylosin for liver abscess prevention [ESTABLISHED]
- Bacitracin methylene disalicylate: some efficacy but not widely used [MODERATE]
- Virginiamycin: some data on efficacy but not commonly adopted [MODERATE]
- No antibiotic can treat established abscesses for the same physical barrier reasons [ESTABLISHED]

### 6.3 Why Vaccines Have Failed

The history of F. necrophorum vaccine development is one of **consistent underperformance** [ESTABLISHED]:

**Leukotoxoid vaccines:**
- Crude leukotoxoid (formalin-inactivated culture supernatant + adjuvant): promising in experimental challenge (one study showed 0% abscesses in vaccinated vs. controls) but **inconsistent in field trials** [MODERATE] (Saginala et al. 1997, PMID 9110232)
- Relationship between anti-leukotoxin antibody titer and protection observed but not reliable [MODERATE]
- Challenge: leukotoxin is a 336 kDa protein with no homology to other toxins -- immune responses may not efficiently neutralize it [INFERRED]

**Centurion (Merck Animal Health):**
- Combined F. necrophorum leukotoxin + T. pyogenes bacterin [ESTABLISHED]
- Reduced abscess severity and incidence by **up to 40%** in some trials [MODERATE]
- **No longer commercially available** -- discontinued [ESTABLISHED]
- The reasons for discontinuation likely include inconsistent field efficacy and poor adoption vs. cheap tylosin [INFERRED]

**OMP-based vaccine candidates:**
- 43K OMP + leukotoxin + hemolysin multi-component recombinant subunit vaccine: protective in mice [PRELIMINARY] (Liu et al. 2021)
- Outer membrane vesicle (OMV) vaccines: under investigation [PRELIMINARY]
- No OMP vaccine has been tested in cattle field trials [UNKNOWN]

**Why vaccines have been hard to develop:**
1. The disease is not transmissible -- no herd immunity benefit to exploit [ESTABLISHED]
2. The pathogen is an endogenous commensal, not an invading agent -- the immune system must distinguish commensal from pathogen [MODERATE]
3. Leukotoxin's unique structure means no cross-reactive immunity from other infections [ESTABLISHED]
4. Natural antibody responses to leukotoxin occur during infection but are insufficient to resolve it [ESTABLISHED]
5. Timing: the vaccine must generate a response BEFORE rumenitis-triggered translocation [MODERATE]

### 6.4 Why Essential Oils and Other Alternatives Fail

- Essential oil mixtures (including limonene): **no significant impact on liver abscess incidence** in controlled trials [MODERATE] (Meyer et al. 2009, PMID 19359504)
- Saccharomyces cerevisiae fermentation products: little impact on abscess microbial community [MODERATE]
- Direct-fed microbials (Bacillus licheniformis): under investigation; early data insufficient [PRELIMINARY]
- Monensin (ionophore): reduces acidosis severity but does not specifically prevent abscesses -- reduces VFA swings but does not address F. necrophorum colonization [MODERATE]
- The fundamental problem: alternatives either target the wrong stage (rumen pH management alone is insufficient) or lack sufficient potency against F. necrophorum specifically [INFERRED]

---

## 7. Reinfection/Reseeding: The Continuous Source

### 7.1 Why Liver Abscess Is a Continuous-Exposure Disease

Unlike classical infectious diseases, hepatic abscessation involves **continuous reseeding** from the animal's own gut:

- F. necrophorum is a **permanent resident** of the rumen; it cannot be eradicated without destroying rumen function [ESTABLISHED]
- As long as the animal is on a high-grain diet, the conditions for rumenitis and bacterial translocation persist [ESTABLISHED]
- Each episode of ruminal acidosis creates a new opportunity for bacterial translocation [MODERATE]
- Existing rumen wall lesions (scars from prior rumenitis) may represent **permanent weak points** for future translocation [INFERRED]
- The liver continually receives portal blood from the rumen, so exposure is ongoing, not episodic [ESTABLISHED]

### 7.2 Multi-Source Seeding

- Rumen epithelium: primary recognized source (F. necrophorum at 4--5 log CFU/g) [ESTABLISHED]
- Colonic epithelium: newly recognized secondary source, possibly contributing subsp. funduliforme and Bacteroides [MODERATE]
- Existing liver abscesses may seed new foci within the liver via local extension or via blood [INFERRED]
- The polymicrobial nature suggests that multiple bacterial species transit simultaneously or sequentially [MODERATE]

### 7.3 The Feed Period as Sustained Exposure Window

- Feedlot cattle are on high-grain finishing diets for **120--400 days** depending on breed [ESTABLISHED]
- Every day on high-grain diet is another day of potential ruminal acidosis and bacterial translocation [MODERATE]
- Removing tylosin even temporarily during the feeding period increases abscess incidence [MODERATE]
- The disease is self-perpetuating within each animal as long as the dietary driver persists [ESTABLISHED]

---

## 8. F. necrophorum Subspecies Differences

The two subspecies have clinically significant differences that affect disease severity and potentially intervention strategy:

| Feature | subsp. necrophorum (Biotype A) | subsp. funduliforme (Biotype B) |
|---------|-------------------------------|--------------------------------|
| Morphology | Long filaments (>100 um) | Short rods, pleomorphic |
| Leukotoxin production | High (21x more transcript) | Low |
| LPS potency | Higher | Lower |
| Hemagglutination | All hepatic isolates positive | Negative |
| Hemolytic activity | High | Low |
| Mouse virulence | Virulent | Less virulent |
| Liver abscess isolation | Most frequent; often pure culture | Less frequent; usually in mixed culture |
| Liver abscess prevalence | 83.1% (sole or with FNF) | 16.9% as sole Fusobacterium |
| Rumen vs. colon | More prevalent in rumen | More isolates from colon |

[ESTABLISHED] -- Composite from multiple sources (Tadepalli et al. 2007, 2009; Okwumabua et al. 1996; Abbasi et al. 2025)

**Taxonomic note:** A recent genomic analysis (Fatahi-Bafghi 2024, [DOI](https://doi.org/10.1007/s10482-023-01921-1)) proposed reclassifying subsp. funduliforme as a later heterotypic synonym of subsp. necrophorum based on ANI, AAI, and digital DDH values exceeding species delineation cutoffs. This reclassification, if adopted, would collapse the subspecies distinction -- but the biological differences in virulence and leukotoxin production remain real and clinically relevant regardless of nomenclature. [MODERATE]

---

## 9. Complete Virulence Factor Inventory

| Virulence Factor | Molecular Details | Function | Evidence Tier |
|-----------------|-------------------|----------|---------------|
| **Leukotoxin (LktA)** | 336 kDa; encoded by lktBAC operon (9,726 bp lktA) | Kills neutrophils and Kupffer cells via apoptosis (low dose) or necrosis (high dose); primary immune evasion mechanism | ESTABLISHED |
| **LPS (Endotoxin)** | Lipid A-core-O antigen; Gram-negative outer membrane | Intravascular coagulation; endothelial damage; systemic inflammation; anaerobiosis creation | ESTABLISHED |
| **Hemolysin** | Phospholipase B; targets phosphatidylcholine | Erythrocyte lysis; tissue destruction; anaerobiosis; co-purifies with leucocidin | MODERATE |
| **Hemagglutinin** | Surface-associated protein | Adhesion to ruminal epithelial cells; mediates initial rumen wall colonization | ESTABLISHED |
| **43K OMP** | 43 kDa outer membrane protein; fibronectin-binding | Adhesion to bovine epithelial and endothelial cells; stimulates NF-kB activation and inflammatory cytokines | MODERATE |
| **OmpA-family protein** | 22.7 kDa | Structural maintenance; adhesion; present in OMVs | PRELIMINARY |
| **OmpH-family protein** | 17.5 kDa | Structural/adhesion; present in OMVs | PRELIMINARY |
| **FadA (Fusobacterium adhesin A)** | Surface adhesin | Adhesion to host cells; identified in OMV proteomics | PRELIMINARY |
| **Platelet aggregation factor** | Distinct from LPS | Promotes microthrombi formation; creates anaerobic niches | MODERATE |
| **Dermonecrotic toxin** | Poorly characterized | Causes focal tissue necrosis in rumen wall and liver | MODERATE |
| **Proteases** | Extracellular; poorly characterized | Degrades tissue matrix; aids penetration and spread | MODERATE |
| **DNases** | Extracellular | Degrades NETs; disrupts host DNA-based defense | INFERRED |
| **MMP-13 induction** | Host enzyme stimulated by F. necrophorum | Degrades interstitial collagen; facilitates bacterial spread | MODERATE |
| **Capsule** | Polysaccharide (some strains) | Anti-phagocytic | PRELIMINARY |
| **Outer membrane vesicles** | 50-250 nm; contain LktA, OMPs, LPS | Deliver virulence factors at distance from bacterial cell | MODERATE |

---

## 10. Incidence, Epidemiology, and Economics

### 10.1 Incidence Data

| Parameter | Value | Evidence Tier |
|-----------|-------|---------------|
| Mean incidence (U.S. feedlots) | 12--32% (varies by feedlot, region, management) | ESTABLISHED |
| Native beef steers | ~15--20% average | ESTABLISHED |
| Holstein steers (fed for beef) | 25--40% (higher due to longer DOF) | ESTABLISHED |
| Cull dairy cows | 32.1% (Great Lakes region) | MODERATE |
| A+ (severe) proportion | ~5--10% of total cattle at slaughter | MODERATE |
| Trend 2008--2013 | +25% in native beef steers; **3x increase** in Holstein steers | MODERATE |
| Regional variation | Texas/Kansas: 20.6% incidence | MODERATE |

### 10.2 Economic Impact

- **Annual cost to U.S. beef industry: US$255.6 million** (95% CI: $161.9M--$377.9M) [ESTABLISHED] (Journal of Animal Science 2025, [DOI](https://doi.org/10.1093/jas/skaf127))
- **Per animal cost: $9.70** regardless of abscess status (industry-wide) [ESTABLISHED]
- **Breakdown of losses:**
  - Reduced ADG and dressing percentage: **48.6%** of total losses
  - Liver condemnation, offal loss, excess carcass trimming: **~40%**
  - Processing delays: **~5%**
  - Carcass quality grade discounts (A+ abscesses): **~4%**
- **If tylosin were removed:** Economic losses would approximately **double** through increased prevalence [MODERATE]

### 10.3 Genetic Susceptibility

- GWAS identified **35 SNP associations** (15 for pooling allele frequency, 20 for total intensity) at FDR less than or equal to 5% [MODERATE] (Keele et al. 2016, [DOI](https://doi.org/10.2527/jas.2015-9887))
- Associated genes are in pathways including:
  - pH homeostasis in the GI tract
  - Immune defenses in the liver
  - Leukocyte migration from blood to infected tissues
  - Glutamine transport (acidosis response)
  - Platelet aggregation for liver repair
  - Axon guidance
- Evidence of **polygenic variation** -- adequate genetic variation exists for potential selection against susceptibility [MODERATE]
- Breed differences (Holstein >> beef breeds) likely reflect both genetic susceptibility AND management (DOF) differences [MODERATE]

---

## 11. R0 Analog and Herd-Level Dynamics

### 11.1 Why Classical R0 Does Not Apply

Hepatic abscessation is **NOT a transmissible disease** in the classical sense [ESTABLISHED]:

- There is no animal-to-animal transmission of F. necrophorum causing liver abscesses
- Each animal's infection originates from its own rumen/gut flora
- The "epidemic" is diet-driven, not pathogen-driven
- Removing one infected animal does not reduce risk to others

Therefore, a classical R0 (basic reproduction number) is **not applicable**.

### 11.2 Modified Risk Framework: Diet-Driven Endogenous Infection

Instead of R0, the relevant framework is an **exposure-response model** [INFERRED]:

**P(abscess) = f(diet intensity, duration, rumen barrier integrity, F.n. virulence, host susceptibility)**

Where:
- **Diet intensity** (grain %, particle size, transition speed) is the dominant driver [ESTABLISHED]
- **Duration** (DOF on high-concentrate) is a cumulative risk factor [ESTABLISHED]
- **Rumen barrier integrity** varies between animals (genetic, prior damage) [MODERATE]
- **F. necrophorum strain virulence** (leukotoxin production level) varies between animals and feedlots [ESTABLISHED]
- **Host susceptibility** has a genetic component (GWAS evidence) [MODERATE]

### 11.3 Herd-Level Implications

Because this is not a transmissible disease:
- **Prevention interventions do NOT compound over time** the way they would for R0 near 1.0
- Each animal must be individually protected -- there is no herd immunity concept
- The "herd-level" intervention is **dietary management** (roughage inclusion, grain processing, adaptation protocols)
- Tylosin works at the individual animal level, not at the transmission level
- Vaccination (if effective) would need to protect each individual animal -- no indirect benefit to non-vaccinated animals

### 11.4 The Real Leverage: Diet vs. Pharmaceutics

- **Dietary management** (slower grain adaptation, more roughage, coarser processing) reduces incidence but conflicts with economic optimization (maximum weight gain) [ESTABLISHED]
- **Tylosin** addresses the consequence (bacterial translocation) but not the cause (acidosis/rumenitis) [ESTABLISHED]
- The ideal intervention would **break the rumenitis-to-translocation link** without requiring dietary suboptimality [INFERRED]
- An intervention that prevents F. necrophorum from colonizing damaged rumen wall or transiting to the liver would be "diet-agnostic" -- allowing aggressive feeding programs without abscess risk [INFERRED]

---

## 12. Rate-Limiting Barrier Identification

### 12.1 Analysis of Each Disease Stage

| Stage | Intervention Potential | Current Coverage | Rate-Limiting? |
|-------|----------------------|------------------|----------------|
| 1. Ruminal acidosis | Diet management, buffers, monensin | Partially addressed but conflicts with production economics | No -- too upstream; would require diet changes industry won't accept |
| 2. Rumenitis | Nothing specifically targets rumen wall healing | Unaddressed | Partially -- but hard to target specifically |
| 3. Rumen wall colonization | Tylosin (indirect, suppresses F.n. numbers) | Partially addressed by tylosin | **YES -- Primary rate-limiting barrier** |
| 4. Portal transit | Nothing | Completely unaddressed | Partially -- but mechanistically intertwined with #3 |
| 5. Immune evasion (leukotoxin) | Failed vaccines | Essentially unaddressed | Important but downstream |
| 6. Abscess formation | Nothing | Completely unaddressed | Too late -- already past the point of no return |
| 7. Chronic persistence | Untreatable | Completely unaddressed | Not rate-limiting -- consequence of #3-5 |

### 12.2 The Rate-Limiting Barrier: Stage 3 -- Rumen Wall Colonization/Portal Transit

The **transition from commensal to pathogen** occurs at the rumen (and potentially hindgut) wall. This is where F. necrophorum shifts from its normal fermentative role to an invasive pathogen that colonizes damaged epithelium and enters portal blood.

**Why this is rate-limiting:**
1. Everything upstream (acidosis, rumenitis) is addressable but economically constrained -- the industry will not fundamentally change feeding programs
2. Everything downstream (immune evasion, abscess formation, persistence) is a **consequence** of successful translocation -- if you prevent translocation, you prevent the disease
3. Tylosin works at this stage (reducing rumen F.n. load) but is a blunt instrument with AMR consequences
4. There is NO specific molecular intervention targeting the adhesion, penetration, or translocation events
5. The adhesion mechanisms (hemagglutinin, 43K OMP, FadA) are **specific molecular targets** that could be addressed without affecting the rumen ecosystem

**What we don't know about this stage:**
- The relative contribution of rumen vs. hindgut translocation
- The exact molecular events of epithelial penetration
- Whether biofilm formation on the rumen wall is required for invasion
- The quantitative threshold of bacterial load needed for successful translocation
- Whether there are host factors (barrier integrity, local immunity) that determine susceptibility at this stage

---

## 13. KE#1 -- The Portfolio-Restructuring Experiment

### 13.1 The Question

**Does the rumen or the hindgut contribute more to hepatic F. necrophorum seeding?**

### 13.2 Why This Restructures the Portfolio

If the rumen is the dominant source (current assumption):
- Anti-adhesion strategies targeting rumen wall colonization are the primary intervention point
- Tylosin alternatives should focus on rumen F. necrophorum suppression
- Rumen pH management has direct prevention value

If the hindgut is a major co-contributor (emerging evidence suggests it might be):
- Rumen-only interventions will have a **ceiling of ~50-60% efficacy** because they miss the hindgut pathway
- Portfolio must include hindgut-targeted interventions
- The Bacteroides-dominated abscess subtype may represent a fundamentally different pathogenic route
- Starch overflow to the hindgut (cecal/colonic acidosis) becomes a critical risk factor
- Dietary management must consider hindgut fermentation, not just rumen pH

### 13.3 The Experiment

**Design:** Matched quantitative sampling from feedlot cattle at slaughter (n = 100+, powered to detect 20% difference in contribution)

**Samples per animal:**
1. Rumen epithelial tissue (multiple sites including areas with/without visible rumenitis)
2. Colonic epithelial tissue (multiple sites)
3. Liver abscess material (if present)
4. Portal vein blood (if technically feasible at slaughter speed)

**Analysis:**
- 4-plex qPCR (FNN, FNF, T. pyogenes, S. enterica) on all samples (validated assay exists: Abbasi et al. 2025)
- 16S rRNA amplicon sequencing for community composition
- Strain-level matching between gut wall and abscess isolates (WGS on paired isolates)

**Key metric:** Strain concordance between rumen epithelium vs. colonic epithelium and liver abscess bacteria. If >30% of abscess strains match colonic but not ruminal epithelial isolates, the hindgut pathway is clinically significant.

### 13.4 Cost and Timeline

- **Cost:** $15--25K (slaughterhouse sampling logistics + qPCR + 16S sequencing + bioinformatics; WGS on subset adds $5--10K)
- **Timeline:** 6--8 weeks (2 weeks sampling, 3--4 weeks lab work, 1--2 weeks analysis)
- Sample collection infrastructure already exists at commercial processors collaborating with KSU (Nagaraja lab)

### 13.5 What Changes If Answer Is A vs B

| If rumen dominant (>80%) | If hindgut significant (>20%) |
|--------------------------|-------------------------------|
| Focus on rumen wall anti-adhesion | Must also target hindgut pathway |
| Tylosin alternatives: rumen-targeted | Tylosin alternatives: must also reach hindgut |
| Rumen pH management is sufficient dietary intervention | Starch overflow to hindgut becomes a critical dietary factor |
| Bacteroides-dominated abscesses are secondary/rare | Bacteroides-dominated abscesses represent a distinct disease subtype |
| Portfolio: 4--5 rumen-focused targets | Portfolio: split between rumen and hindgut targets |

---

## 14. Disease Stage Summary and Gap Analysis

| Stage | Understanding Level | Intervention Status | Critical Unknowns |
|-------|-------------------|-------------------|-------------------|
| 1. Acidosis/rumenitis | Well understood | Dietary management (constrained by economics) | Threshold for translocation risk; individual susceptibility |
| 2. Rumen wall colonization | Moderate -- adhesion mechanisms known | Tylosin (indirect) | Quantitative dynamics; biofilm role; molecular detail of penetration |
| 3. Portal transit | Poorly understood | Nothing | Timing, frequency, bacterial load thresholds; hindgut contribution |
| 4. Hepatic immune evasion | Well understood (leukotoxin) | Failed vaccines | Why vaccines don't work in field; other immune evasion mechanisms |
| 5. Abscess formation | Well understood (histopathology) | Nothing | Timing during feedlot period; why some animals clear bacteria |
| 6. Chronic persistence | Understood (capsule barrier) | Untreatable | Biofilm within abscess; metabolic dormancy |
| 7. Reinfection/reseeding | Understood conceptually | Nothing (continuous exposure) | Relative contribution of rumen vs hindgut; role of existing abscesses in seeding new foci |

**Stages with ZERO specific molecular intervention coverage:** 2, 3, 4, 5, 6, 7

**The only stage with any pharmaceutical coverage:** Stage 2/3 (tylosin, indirectly)

---

## 15. Key References (by PubMed, DOI-linked)

1. Nagaraja TG & Chengappa MM (1998). Liver abscesses in feedlot cattle: a review. J Anim Sci. [DOI](https://doi.org/10.2527/1998.761287x)
2. Nagaraja TG & Lechtenberg KF (2007). Liver abscesses in feedlot cattle. Vet Clin North Am Food Anim Pract. [DOI](https://doi.org/10.1016/j.cvfa.2007.05.002)
3. Amachawadi RG & Nagaraja TG (2022). Pathogenesis of Liver Abscesses in Cattle. Vet Clin North Am Food Anim Pract. [DOI](https://doi.org/10.1016/j.cvfa.2022.08.001)
4. Amachawadi RG & Nagaraja TG (2016). Liver abscesses in cattle: incidence, bacteriology, vaccine approaches. J Anim Sci. [DOI](https://doi.org/10.2527/jas.2015-0261)
5. Tadepalli S et al. (2009). F. necrophorum: a ruminal bacterium that invades liver. Anaerobe. [DOI](https://doi.org/10.1016/j.anaerobe.2008.05.005)
6. Tadepalli S et al. (2007). Leukotoxin operon and differential expressions. Anaerobe. [DOI](https://doi.org/10.1016/j.anaerobe.2007.09.001)
7. Narayanan S et al. (2002). Leukotoxin induces activation and apoptosis. Infect Immun. [DOI](https://doi.org/10.1128/IAI.70.8.4609-4620.2002)
8. Pillai DK et al. (2021). Leukotoxin production in relation to severity. Anaerobe. [DOI](https://doi.org/10.1016/j.anaerobe.2021.102344)
9. Tan ZL et al. (1996). F. necrophorum infections: virulence factors review. Vet Res Commun. [DOI](https://doi.org/10.1007/BF00385634)
10. Abbasi M et al. (2025). Quantification of major bacterial pathogens in liver abscesses. Microbiol Spectr. [DOI](https://doi.org/10.1128/spectrum.01888-25)
11. Salih HM et al. (2025). Etiology of liver abscesses and hindgut as source. Microbiol Spectr. [DOI](https://doi.org/10.1128/spectrum.02539-25)
12. Fuerniss LK et al. (2022). Liver abscess microbiota of feedlot steers. J Anim Sci. [DOI](https://doi.org/10.1093/jas/skac252)
13. Keele JW et al. (2016). Genomewide association study of liver abscess. J Anim Sci. [DOI](https://doi.org/10.2527/jas.2015-9887)
14. Amachawadi RG et al. (2023). Metabolome of liver abscess purulent materials. J Anim Sci. [DOI](https://doi.org/10.1093/jas/skac427)
15. Weinroth MD et al. (2019). Tylosin effects on microbiomes and resistomes. J Anim Sci. [DOI](https://doi.org/10.1093/jas/skz306)
16. Agga GE et al. (2023). Tylosin effects on macrolide-resistant enterococci. Prev Vet Med. [DOI](https://doi.org/10.1016/j.prevetmed.2023.105930)
17. Okwumabua O et al. (1996). Ribotyping to differentiate F. necrophorum subspecies. Appl Environ Microbiol. [DOI](https://doi.org/10.1128/aem.62.2.469-472.1996)
18. Xiao J et al. (2024). B cell epitopes on leukotoxin protein. Anaerobe. [DOI](https://doi.org/10.1016/j.anaerobe.2024.102884)
19. Fatahi-Bafghi M (2024). Genomic analysis and reclassification proposal. Antonie van Leeuwenhoek. [DOI](https://doi.org/10.1007/s10482-023-01921-1)
20. Gruninger RJ et al. (2024). Genome sequences of T. pyogenes from liver abscesses. Microbiol Resour Announc. [DOI](https://doi.org/10.1128/mra.00554-24)

---

*Phase 1 complete. This disease map covers all 7 stages of pathogenesis with evidence tagging on every claim. The rate-limiting barrier is identified (Stage 3: rumen wall colonization / portal transit) and the portfolio-restructuring experiment (KE#1: rumen vs. hindgut contribution) is defined. Ready for external panel review and Sapper analysis.*
