# Adversarial Review — phase-3-candidates.md

Generated: 2026-03-27 13:02

Document: `programs/crypto/phase-3-candidates.md`

---

### OpenRouter (gemini-2.5-pro)

Excellent analysis. The provided document is a comprehensive and well-structured overview of the current state of R&D for bovine cryptosporidiosis. It correctly identifies the leading small molecule candidates and astutely incorporates novel host-directed and nutritional approaches.

My role is to provide an independent perspective, drawing on cross-disciplinary experience to identify targets or modalities that may have been overlooked. I will focus on approaches that sidestep common failure modes and leverage empirical success from other fields.

---

## EMPIRICAL HITS (In-vivo data in the target species)

The provided document's "Category A" is an excellent summary of the state-of-the-art. I will not repeat it, but instead offer my drug hunter's interpretation of the three most important hits:

1.  **AN7973 (CPSF3 Inhibitor):** This is the most promising direct-acting antiparasitic profile described. The combination of **rapidly cidal** activity, efficacy against **asexual and sexual stages**, and validation in **immunosuppressed models** makes it theoretically capable of achieving a sterilizing cure. It satisfies the most critical Sapper constraints that Halofuginone and PI4K inhibitors may not. The key unknown is the genetic barrier to resistance. The history of tRNA synthetase inhibitors (e.g., halofuginone, BRD7929) shows that single-target agents can be vulnerable. If the benzoxaborole's mechanism of trapping the enzyme offers a higher resistance barrier, this is the lead target class.

2.  **MMV665917 (Unknown Target):** The importance of this compound cannot be overstated. Its documented **therapeutic efficacy** (started *after* severe diarrhea onset) in calves is a rare and precious empirical result. In drug discovery, a "dirty" compound that works in the target species is often more valuable than a "clean" compound that only works in a petri dish. The unknown target is a risk but also an opportunity. It may represent a completely novel vulnerability. The lack of follow-up since 2018 is a red flag suggesting a potential development dead-end (e.g., toxicity, synthesis issues, or target already known to be problematic), but it remains a critical piece of evidence. **Why it worked:** It achieved sufficient exposure at the site of infection to kill parasites even in a compromised, diarrheic gut. This is a PK/PD success story that must be reverse-engineered.

3.  **Anti-P23 IgY (Egg Yolk Antibodies):** This represents the most pragmatic and scalable anti-reinvasion approach. While hyperimmune colostrum works, its production is logistically complex. IgY production in hens is cheap, scalable, and easily standardized. The Cho et al. (2025) study is crucial because it demonstrated **survival of functional IgY through the GI tract**, a key failure point for many oral biologics. **Why it worked:** It provided a continuous, luminal blockade of the autoinfection cycle by neutralizing merozoites before they could reinvade. It cannot cure, but it can turn an explosive, multi-cycle infection into a single-cycle, self-limiting one, allowing the calf's own immunity to catch up.

## PROPOSED TARGETS (Not in the current analysis)

The provided analysis is exceptionally thorough. However, a few modalities and target classes are under-represented.

1.  **Target:** Microbiome competition (indirect)
    **Mechanism:** Bacteriophage-mediated microbiome editing. *Cryptosporidium* relies on the gut microbiota for key nutrients (e.g., purines, specific amino acids). Furthermore, co-infecting or dysbiotic bacteria can exacerbate pathology. Instead of adding "good" bacteria (probiotics), this approach uses bacteriophages to specifically *remove* "bad" or "pro-parasitic" bacteria. A phage cocktail could be designed to target bacterial species known to produce metabolites scavenged by *Crypto* or those associated with worse clinical outcomes.
    **Evidence:** Phage therapy is well-established in veterinary medicine (e.g., against *Salmonella*, *E. coli*). The technology to isolate and cocktail phages is mature. The link between specific microbial functions and crypto susceptibility (Hares et al. 2023) provides a rational basis for selecting bacterial targets.
    **Modality:** Oral bacteriophage cocktail (liquid or lyophilized).
    **Disease Stage:** Stage 0 (Upstream Susceptibility) and Stage 5 (Intestinal Pathology).

2.  **Target:** Parasite mRNA (e.g., CpPI4K, CPSF3, or other essential genes)
    **Mechanism:** Gene silencing via Antisense Oligonucleotides (ASOs). ASOs are short, synthetic strings of nucleic acids that bind to a specific mRNA, leading to its degradation via RNase H and preventing protein translation. A chemically-modified ASO targeting an essential parasite gene could be delivered orally.
    **Evidence:** ASO technology is now FDA-approved for multiple human diseases. Oral delivery to the gut is a major area of development, with new chemical modifications (e.g., constrained-ethyl/LNA) improving stability in the GI tract. This approach bypasses the need to find a druggable pocket on a protein; if the gene is essential, it's a target.
    **Modality:** Chemically-modified antisense oligonucleotide. Could be formulated for ileal release.
    **Disease Stage:** Stage 3 (Intracellular Development).

3.  **Target:** The Parasitophorous Vacuole Membrane (PVM)
    **Mechanism:** Disruption of PVM integrity or transport. The PVM is a unique non-fusogenic compartment that is the parasite's interface with the host cell cytoplasm. It is studded with parasite-exported proteins that act as pores and transporters to acquire host nutrients. Targeting these PVM transporters (e.g., with pore-blocking small molecules) or the lipid composition of the PVM itself could starve the parasite or cause the vacuole to collapse.
    **Evidence:** This is a validated target concept for *Plasmodium* (which also resides in a PVM), where exported protein function is essential. Proteomic studies of the *Crypto* PVM have identified unique parasite proteins that are absent in the host. These represent a panel of highly selective potential targets.
    **Modality:** Small molecule.
    **Disease Stage:** Stage 3 (Intracellular Development).

4.  **Target:** Oocyst wall (environmental)
    **Mechanism:** Enzym

---

### OpenRouter (grok-4-07-09)

## EMPIRICAL HITS (In-vivo data in the target species)

Based on my knowledge of veterinary literature and clinical trials in neonatal calves (Bos taurus, 0-30 days old), I focused on interventions with documented positive outcomes in controlled trials or field studies specifically for cryptosporidiosis caused by Cryptosporidium parvum. I prioritized empirical efficacy (e.g., reduced oocyst shedding, diarrhea resolution, improved survival or weight gain) over mechanistic hypotheses. Only those with in-vivo calf data are included—excluding mouse-only or in-vitro data. These are drawn from peer-reviewed sources and meta-analyses up to my last training data (2023), cross-referenced with the provided document for independence.

- **Halofuginone (Halocur)**: A synthetic quinazolinone derivative that inhibits prolyl-tRNA synthetase, acting as a cryptostatic agent (arrests parasite development without killing). In a meta-analysis of 14 randomized controlled trials in neonatal calves (e.g., Silverlås et al., 2010, Prev Vet Med; Keidel and Daugschies, 2013, Vet Parasitol), prophylactic dosing (100-120 μg/kg/day for 7 days) reduced oocyst shedding by 50-80% and decreased diarrhea severity/mortality in high-challenge herds. No significant weight gain benefit, and rebound occurred post-treatment. It worked empirically by slowing parasite proliferation during peak vulnerability, allowing immature calf immunity to catch up, though it's not curative and has a narrow safety margin (toxicity at 2x dose).

- **Paromomycin**: An aminoglycoside antibiotic that interferes with parasite protein synthesis. In multiple calf trials (e.g., Fayer and Ellis, 1993, Vet Parasitol; Grinberg et al., 2002, Vet Parasitol), oral dosing (100 mg/kg/day for 11 days) prophylactically reduced oocyst shedding by 70-90% and shortened diarrhea duration by 2-4 days compared to controls. Therapeutic use showed partial suppression but rebound. It worked by directly inhibiting intracellular parasite stages from the luminal side, exploiting the epicellular niche's accessibility, though it's static rather than cidal and causes microbiome disruption.

- **Nitazoxanide (NTZ)**: A thiazolide antiparasitic with unclear mechanism (possibly PFOR inhibition or host-mediated). In a randomized controlled trial in neonatal calves (Ollivett et al., 2012, J Vet Intern Med), oral NTZ (500 mg twice daily for 3 days) reduced oocyst shedding by ~60% and improved fecal scores in naturally infected dairy calves, with no adverse effects. However, results are inconsistent across studies (e.g., Schnyder et al., 2009, Vet Parasitol showed no benefit). It worked in positive trials by partial parasite clearance, likely requiring some host immune cooperation, but efficacy varies with infection intensity and calf age.

- **Hyperimmune Bovine Colostrum**: Polyclonal antibodies from immunized dams targeting C. parvum antigens (e.g., rC7 or gp15/40). In a controlled trial (Perryman et al., 1999, Infect Immun), supplementation reduced oocyst shedding by 80-99% and eliminated clinical diarrhea in challenged neonatal calves. Field studies (e.g., Meganck et al., 2015, Prev Vet Med) confirmed shorter diarrhea (2-3 days vs 5-7 in controls). It worked by neutralizing extracellular sporozoites/merozoites during transit, preventing reinvasion, and providing passive immunity without relying on the calf's immature system.

- **Decoquinate**: A quinolone coccidiostat targeting mitochondrial function. In a field trial in beef calves (Redman et al., 1989, Vet Rec), continuous feed supplementation (0.5 mg/kg/day) reduced oocyst prevalence by 50% and improved weight gain in crypto-endemic herds. However, a later study (Moore et al., 2003, Vet Parasitol) showed only marginal benefits. It worked empirically in some settings by inhibiting early parasite stages, but inconsistent due to C. parvum's vestigial mitochondria.

- **Lasalocid**: An ionophore antibiotic disrupting parasite ion gradients. In a controlled calf challenge study (Sréter et al., 1995, Int J Parasitol), oral dosing (8 mg/kg/day) reduced oocyst output by 60-70% and mitigated diarrhea. It worked by direct antiparasitic effects on membrane integrity, similar to other ionophores, but with variable efficacy and safety concerns in neonates.

These hits emphasize that no single agent achieves sterilizing cure; successes are often prophylactic or adjunctive, highlighting the need for combinations.

## PROPOSED TARGETS (Not in the current analysis)

I independently scanned for targets and approaches missing from the document's 42 candidates. The document is biology-heavy (e.g., focused on parasite kinases, tRNA synthetases, host immunity), so I prioritized chemistry-first or non-traditional modalities like phage therapy, peptide mimetics, or repurposed drugs from veterinary use, emphasizing empirical precedents in related species/pathogens. Only those not covered (e.g., no overlap with EDI048, AN7973, IgY, etc.). Evidence is tiered: ESTABLISHED (in-vivo data in related models), MODERATE (in-vitro + mechanistic), PRELIMINARY (hypothetical but grounded).

- **CpIMP Dehydrogenase (IMPDH) Inhibition via Repurposed Mycophenolic Acid Derivatives**: Target is C. parvum inosine monophosphate dehydrogenase (CpIMPDH), essential for purine salvage (parasite lacks de novo synthesis). Mechanism: Blocks guanine nucleotide production, halting replication. Evidence: ESTABLISHED—mycophenolic acid (MPA) reduced parasite burden in immunocompromised mice (Yarlett et al., 2014, Antimicrob Agents Chemother), with synergy against related apicomplexans; no calf data but veterinary MPA analogs exist for immunosuppression. Modality: Small molecule, oral gut-restricted derivative (e.g., ester prodrug for ileal release). Addresses Stage 3 (Intracellular Development) by starving established parasites. Missed in document: Document has tRNA synthetases but not this purine pathway node, which has higher empirical hits in vivo.

- **Bacteriophage Therapy Targeting Crypto-Associated Dysbiosis**: Target is secondary bacterial overgrowth (e.g., E. coli, Clostridium) exacerbating crypto diarrhea via toxin production. Mechanism: Lytic phages selectively kill dysbiotic bacteria, restoring microbiome balance without antibiotics. Evidence: MODERATE—phage cocktails reduced E. coli diarrhea in calves (Smith et al., 1987, J Gen Microbiol); analogous to phage success in calf scours (not crypto-specific but relevant for co-infection). Modality: Oral phage cocktail (e.g., T4-like phages), stable in abomasum. Addresses Stage 5 (Intestinal Pathology) by reducing bacterial contributions to secretion/malabsorption. Missed: Document has microbiome engineering (C9) but not phage-based, which has stronger empirical calf data.

- **CpDHFR Inhibition with Trimethoprim-Sulfamethoxazole (TMP-SMX) Repurposing**: Target is C. parvum dihydrofolate reductase (CpDHFR), critical for folate metabolism and DNA synthesis. Mechanism: Synergistic inhibition blocks thymidylate production, cidal against replicating stages. Evidence: ESTABLISHED—TMP-SMX reduced oocyst shedding and improved survival in piglet cryptosporidiosis models (Moon et al., 1982, Vet Pathol), with anecdotal calf use; folate pathway validated across apicomplexans. Modality: Small molecule combination, oral suspension. Addresses Stage 3 (Intracellular Development) for therapeutic kill. Missed: Document covers glycolysis (B3) but not folate, despite veterinary repurposing potential.

- **Host CXCR3 Chemokine Receptor Agonism with IP-10 Mimetic Peptides**: Target is host CXCR3 on innate immune cells (e.g., NK cells, gamma-delta T cells). Mechanism: Enhances recruitment of IFN-gamma-producing cells to ileum, accelerating epithelial clearance without adaptive immunity. Evidence: PRELIMINARY—IP-10 (CXCL10) analogs boosted mucosal immunity in neonatal lamb crypto models (Suraud et al., 2009, Vet Immunol Immunopathol); peptide mimetics stable orally. Modality: Synthetic peptide, oral enteric-coated. Addresses Stage 4 (Host Immune Response) for neonates. Missed: Document has IFN-lambda (C2) but not CXCR3, which has direct calf-analog data.

- **CpProteasome Inhibition with Bortezomib Analogs**: Target is the parasite's 26S proteasome, essential for protein degradation and stress response. Mechanism: Blocks ubiquitin-proteasome pathway, leading to toxic protein accumulation and death. Evidence: MODERATE—proteasome inhibitors killed C. parvum in vitro (Ndao et al., 2013, Antimicrob Agents Chemother); bortezomib effective in Toxoplasma mouse models with gut restriction possible. Modality: Small molecule, gut-restricted analog. Addresses Stage 3 (Intracellular Development) across stages. Missed: Document has HDAC (B4) but not proteasome, a high-hit target in parasite drug screens.

## CROSS-DISEASE ANALOGIES

I drew analogies from diseases with similar pathophysiology (e.g., intracellular mucosal parasites, neonatal enteric infections) where interventions have empirical in-vivo success in target or related species. Adaptations focus on calf-specific needs (e.g., oral delivery, neonatal safety).

- **From Toxoplasmosis (Toxoplasma gondii in cats/lambs)**: Spiramycin (macrolide) reduced tissue cysts and shedding in pregnant ewes (Buxton et al., 1988, Vet Rec). Relevant because both are apicomplexans with epicellular niches and autoinfection; spiramycin's placental/ mucosal penetration could adapt to crypto by formulating as a gut-restricted macrolide to block C. parvum invasion (Stage 2). Adaptation: Veterinary oral suspension, combined with ionophores for synergy, tested in calf challenge models—empirical lamb data suggests >70% shedding reduction possible.

- **From Coccidiosis (Eimeria in poultry/calves)**: Amprolium (thiamine analog) prophylactically reduced oocyst output by 80% in calf Eimeria trials (Joyner et al., 1978, Vet Parasitol). Relevant for shared purine/thiamine dependencies in apicomplexans; crypto's purine salvage makes it analogous. Adaptation: Repurpose as crypto prophylactic in milk replacer, but add gut-restriction to avoid systemic thiamine depletion in neonates—could address Stage 3, with poultry data showing high resistance barrier via multi-pathway disruption.

- **From Neonatal Rotavirus Diarrhea in Calves**: Zinc supplementation (as zinc sulfate) reduced diarrhea duration by 2 days and improved weight gain in rotavirus-infected calves (Graham et al., 2013, J Dairy Sci). Relevant for crypto's secretory diarrhea and mucosal damage; zinc stabilizes tight junctions and reduces secretion. Adaptation: High-dose oral zinc in ORS for Stage 5, adapted from rotavirus empirics—add to crypto protocols to enhance repair, as zinc has no parasite resistance risk and fits feed-additive modality.

- **From Giardiasis (Giardia in dogs/calves)**: Fenbendazole (benzimidazole) cleared Giardia cysts with 90% efficacy in puppies (Zajac et al., 1998, Vet Parasitol). Relevant for shared luminal protozoan lifecycle and microtubule disruption mechanism; crypto's cytoskeleton is benzimidazole-sensitive in vitro. Adaptation: Veterinary oral fenbendazole for Stage 6 (shedding), combined with anti-reinvasion agents—calf Giardia data suggests adaptation could reduce crypto oocysts by targeting egress.

- **From Babesiosis (Babesia in cattle)**: Imidocarb dipropionate reduced parasitemia by 95% in bovine trials (Kuttler et al., 1972, Am J Vet Res). Relevant as another apicomplexan with purine dependencies; imidocarb's broad-spectrum activity. Adaptation: Gut-restricted imidocarb analog for oral use in crypto Stage 3, leveraging cattle safety data—empirical hits in Babesia indicate potential for multi-stage coverage without immunity dependence.

## WHAT WOULD YOU PRIORITISE?

If I had to pick 3 targets for cryptosporidiosis in neonatal calves, I'd prioritize based on empirical in-vivo hits in calves or close analogs, potential for rapid veterinary development, and addressing key gaps (e.g., cidal activity, immunity independence, transmission reduction). These emphasize combinations over monotherapies, as no single agent cures.

1. **CpIMPDH Inhibition (e.g., mycophenolic acid derivatives)**: Top priority because it's cidal, immunity-independent (works in immunosuppressed models), and has strong analogies from apicomplexans with in-vivo data. It targets a validated metabolic chokepoint missed in the analysis, with repurposing potential for quick calf trials—prioritize for Stage 3 to provide the direct-kill backbone.

2. **Bacteriophage Therapy for Dysbiosis**: Second, as an adjunct for Stage 5, with empirical calf data in bacterial diarrhea and high safety/neonatal fit. It addresses microbiome contributions empirically overlooked in the document, adaptable as a low-cost oral cocktail to enhance antiparasitic efficacy without resistance risks.

3. **CpDHFR Inhibition (TMP-SMX repurposing)**: Third for its established veterinary use, synergistic cidal mechanism, and piglet data translatable to calves. It fills the folate pathway gap, prioritizing therapeutic use in Stage 3 with a high resistance barrier via combination—empirical hits make it de-risked for fast prioritization.

---

### OpenRouter (gpt-5.4-20260305)

## EMPIRICAL HITS (In-vivo data in the target species)

Below I focus on **what has actually shown benefit in calves**, including some items that are under-emphasized or interpreted too narrowly in the review.

### 1. Halofuginone lactate (Halocur)  
**What it is:** Licensed oral quinazolinone derivative used in calves; generally regarded as **cryptosporidiostatic**, not curative.  
**Result in calves:** Repeated calf studies and meta-analyses show **reduced oocyst shedding** and some reduction in clinical severity when given early/prophylactically; benefit is inconsistent for therapeutic use after diarrhea is established.  
**Key citations:**  
- Lefay et al., systematic review/meta-analysis of halofuginone in calves, *Prev Vet Med* (approx. 2021/2022 era literature)  
- Earlier field studies supporting registration in Europe under Halocur  
**Why it worked:** It lowers parasite expansion during the early epithelial amplification phase. Empirically, its value is not “cure” but **blunting peak burden** if started early enough.  
**Take-home:** Important as a **benchmark**, but not a portfolio anchor.

---

### 2. Paromomycin  
**What it is:** Poorly absorbed aminoglycoside used off-label in some studies.  
**Result in calves:** Multiple calf studies reported **reduced oocyst shedding and clinical signs during dosing**, but often with **rebound after cessation** and concerns about antimicrobial stewardship/residue/regulatory fit.  
**Key citations:**  
- Grinberg et al., calf cryptosporidiosis treatment studies, early 2000s  
- Viu et al. / other European calf studies comparing paromomycin vs halofuginone  
**Why it worked:** This is a very important empirical point: paromomycin shows the parasite is **pharmacologically reachable from the gut lumen/apical side** in calves. Even if the class is imperfect, the modality is validated.  
**What the review may miss:** Paromomycin is not just a mediocre legacy agent; it is a strong **delivery proof-of-concept** for luminally retained chemotypes.

---

### 3. Azithromycin  
**What it is:** Macrolide antibiotic with reported anti-cryptosporidial activity in some veterinary studies.  
**Result in calves:** Some calf trials reported **reduced diarrhea severity/duration and lower shedding**, though results were variable and generally not transformational.  
**Key citations:**  
- Nasir et al. / Abubakar et al. era veterinary studies in calves  
**Why it worked:** Likely a mix of modest direct anti-parasitic effect plus impact on secondary bacterial overgrowth/inflammation.  
**Why it matters:** Even if not development-worthy, it suggests **combination benefit with enteropathogen-control and cryptosporidial suppression** can look better in field calves than clean mechanistic models predict.

---

### 4. Nitazoxanide  
**What it is:** Broad antiparasitic approved in humans for cryptosporidiosis.  
**Result in calves:** **Mixed/weak calf efficacy** overall; some studies show partial clinical or shedding benefit, others little value.  
**Key citations:**  
- Multiple calf studies from the 2000s; generally inconsistent field efficacy  
**Why it sometimes worked:** Probably context-dependent: inoculum, timing, immune status, co-infections, formulation.  
**Why it still matters:** As a **negative-to-marginal empirical comparator**, not a lead. It reminds us that **human crypto efficacy does not port cleanly into neonatal calves**.

---

### 5. Hyperimmune colostrum / immune colostral whey  
**What it is:** Colostrum from dams immunized with *C. parvum* antigens or enriched anti-Crypto antibodies.  
**Result in calves:** Some studies showed **marked reduction in diarrhea and oocyst shedding**, especially when high-titer material was used early and repeatedly.  
**Key citations:**  
- Fayer, Jenkins, Perryman-associated calf passive immunization literature  
- Trials using hyperimmune bovine colostrum or colostral concentrates against calf crypto  
**Why it worked:** It intercepts the **short extracellular transit stages**—sporozoites/merozoites—reducing reinvasion and effective amplification.  
**Important nuance:** The review is right that it is not sterilizing, but the empirical signal in calves is real enough that this should be treated as a **viable adjunct class**, not just a mechanistic curiosity.

---

### 6. Specific anti-*Cryptosporidium* egg-yolk antibodies (IgY; anti-P23 and related surface antigens)  
**What it is:** Orally delivered chicken IgY raised to Crypto antigens.  
**Result in calves:** Recent calf work reported **reduced diarrhea duration and lower oocyst shedding**; antigen-specific IgY remained detectable in feces.  
**Key citation:**  
- Cho et al., 2025 calf study  
**Why it worked:** Same logic as hyperimmune colostrum, but with a cheaper/manufacturable passive oral biologic format.  
**Why it matters:** This is one of the few **Cargill-compatible, species-positive** adjuncts.

---

### 7. BKI-class CDPK1 inhibitors, including BKI-1708  
**What it is:** Bumped kinase inhibitor targeting parasite CDPK1.  
**Result in calves:** Calf studies reported **improved clinical signs and faster diarrhea resolution**; parasite reductions have been seen across rodent and calf systems.  
**Key citations:**  
- Hulverson / Arnold / McDonald group calf studies on BKIs including BKI-1708  
**Why it worked:** It effectively blocks **invasion/egress cycling**, which matters a lot in the self-amplifying gut infection of calves.  
**Important nuance:** Not ideal monotherapy, but clearly an **in-vivo active class in calves**.

---

### 8. MMV665917  
**What it is:** Phenotypic-screen hit with unknown target.  
**Result in calves:** Therapeutic administration after diarrhea onset gave **substantial shedding reduction and clinical improvement**.  
**Key citation:**  
- Stebbins et al., 2018, *PLoS Negl Trop Dis*  
**Why it worked:** Unknown mechanism, but the phenotype is exactly what matters in the field: it works **after disease is evident**, not just prophylactically.  
**Why it matters:** This is one of the strongest reasons to keep **phenotypic discovery** alive rather than overcommitting to known targets.

---

### 9. Benzoxaborole CPSF3 inhibitor AN7973  
**What it is:** mRNA processing inhibitor.  
**Result in calves:** Reported **>99% reduction in fecal parasite output** and elimination of diarrhea in experimental calf infection.  
**Key citation:**  
- Love et al. / Lunde et al. benzoxaborole anti-Crypto studies; calf efficacy paper around 2021–2023  
**Why it worked:** CPSF3 is a high-value parasite vulnerability with broad lifecycle impact.  
**Take-home:** One of the best empirical calf hits in the entire space.

---

### 10. PI4K inhibitor series culminating in gut-restricted candidates like EDI048  
**What it is:** Parasite PI4K inhibitor optimized for gut exposure and low systemic burden.  
**Result in calves:** Rapid clinical improvement and strong reduction in shedding, with durable suppression after treatment.  
**Key citations:**  
- Manjunatha et al. foundational PI4K work  
- Recent Novartis/EDI gut-restricted candidate reports including calf efficacy  
**Why it worked:** Excellent match of **target biology + site-of-action pharmacology**.  
**Take-home:** Probably the cleanest modern example of “design to species/pathophysiology.”

---

### 11. Supportive oral rehydration / nutritional support  
**What it is:** ORS, good colostrum management, feeding support.  
**Result in calves:** Not anti-parasitic, but consistently improves survival/supportive outcomes in diarrheic calves, including crypto-positive animals.  
**Key citations:** standard calf diarrhea management literature  
**Why it worked:** Crypto mortality in calves is often driven by **dehydration, acidosis, energy deficit**, not parasite burden alone.  
**Why it matters here:** Adjunctive products that improve hydration/energy may produce larger real-world gains than elegant immunology.

---

## PROPOSED TARGETS (Not in the current analysis)

I’m excluding targets already covered in the review and focusing on additional, biology-first or modality-first ideas with either empirical support elsewhere or a strong translational case.

### 1. **Cryptosporidium N-myristoyltransferase (NMT)**
- **Target:** Parasite NMT
- **Mechanism:** Blocks co-translational myristoylation needed for membrane targeting/signaling of multiple essential proteins.
- **Evidence:** NMT is drugged successfully in other protozoa, especially *Trypanosoma* and *Plasmodium* programs. Apicomplexans are often vulnerable to lipidation pathway disruption.
- **Modality:** Small-molecule, gut-restricted oral inhibitor.
- **Stage addressed:** Stage 3 primarily; possibly invasion/egress too.
- **Why propose it:** This is a **poly-effector essentiality node** with potential for rapid kill and less single-pathway bypass than many tRNA synthetases. It’s not in the current map and is exactly the kind of target medicinal chemists can optimize for gut restriction.

---

### 2. **Parasite signal peptide peptidase / secretory pathway proteases**
- **Target:** Crypto intramembrane or processing proteases involved in maturation/export of secreted invasion proteins.
- **Mechanism:** Blocks proper maturation/trafficking of apical or surface proteins required for invasion and reinvasion.
- **Evidence:** Secretory protease dependencies are exploitable across apicomplexa; plasmepsin-like and processing protease pathways are validated elsewhere.
- **Modality:** Small-molecule protease inhibitor, ideally luminally retained.
- **Stage addressed:** Stage 2 and Stage 3 cycling.
- **Why propose it:** Crypto relies on a compact but highly specialized secretory/invasion apparatus. Protease pathway inhibitors can create **multistage disruption** without directly targeting host kinases.

---

### 3. **Host ASBT/IBAT modulation as a delivery and disease-modifying lever**
- **Target:** Apical sodium-dependent bile acid transporter pathway
- **Mechanism:** Not to inhibit parasite directly, but to **reshape bile acid flux** and possibly reduce bile-acid-driven secretory diarrhea; also can be used to target drug conjugates.
- **Evidence:** IBAT inhibitors are active in veterinary and human GI disease spaces; bile acid signaling strongly affects intestinal secretion and epithelial physiology.
- **Modality:** Small molecule, or prodrug strategy.
- **Stage addressed:** Stage 5 primarily.
- **Why propose it:** The review mentions cholestyramine and bile-acid conjugates, but not the broader **bile acid transporter pharmacology**. In calves, symptom control that is mechanistically specific to ileal injury could have field value.

---

### 4. **Host chloride secretory axis beyond CFTR: CaCC/TMEM16A-selective blockade**
- **Target:** TMEM16A / CaCC on enterocytes
- **Mechanism:** Reduce secretory water loss without slowing gut motility.
- **Evidence:** CaCC is a validated secretory diarrhea node in infectious diarrhea and overlaps with crofelemer biology, but pure-selective blockers may be cleaner than a botanical mixture.
- **Modality:** Non-absorbed small molecule.
- **Stage addressed:** Stage 5.
- **Why propose it:** A **fully luminal, non-antimicrobial, prescription-light adjunct** could be commercially useful even if it doesn’t hit the parasite.

---

### 5. **PAR-2 / enteric neuroimmune secretion axis**
- **Target:** Protease-activated receptor-2 on enteric epithelium/neurons
- **Mechanism:** Dampens neurogenic secretion, epithelial leak, and visceral inflammatory signaling.
- **Evidence:** PAR-2 is implicated in infectious and inflammatory diarrhea across species.
- **Modality:** Antagonist peptide or small molecule; likely adjunctive.
- **Stage addressed:** Stage 5.
- **Why propose it:** If serotonin/secretory reflexes are only part of crypto diarrhea, PAR-2 may be a broader anti-secretory / barrier-protective node than ondansetron alone.

---

### 6. **Host epithelial ferroptosis/redox protection**
- **Target:** GPX4-lipid peroxidation axis in host enterocytes
- **Mechanism:** Prevents collateral epithelial death and barrier collapse during infection.
- **Evidence:** Ferroptosis is increasingly implicated in inflammatory epithelial injury; neonatal gut is redox-sensitive.
- **Modality:** Nutritional-pharma hybrid: selenium optimization, lipophilic radical traps, GPX4-supportive formulations.
- **Stage addressed:** Stage 5 and 7.
- **Why propose it:** Even with a good antiparasitic, calves may still lose performance from mucosal injury. A **repair/protection layer** that preserves villus function could matter economically.

---

### 7. **Enterocyte proliferation axis via GLP-2 analog biology**
- **Target:** GLP-2 receptor axis
- **Mechanism:** Increases intestinal growth, absorptive area, barrier repair, and nutrient uptake.
- **Evidence:** GLP-2 analogs are highly effective in short bowel and mucosal injury settings in humans; strong translational GI biology.
- **Modality:** Peptide or long-acting analog; potentially expensive, but a short-course veterinary analog or nutritional secretagogue could be explored.
- **Stage addressed:** Stage 7, possibly late Stage 5.
- **Why propose it:** The review mentions EGF but not GLP-2. For the long-term **34 kg deficit problem**, GLP-2 biology may be more powerful than EGF.

---

### 8. **Oocyst excystation inhibitors**
- **Target:** Oocyst wall opening/excystation triggers
- **Mechanism:** Prevent ingested oocysts from releasing infective sporozoites in the calf gut.
- **Evidence:** Excystation is chemically triggerable and therefore probably chemically disruptable; similar concepts exist in coccidial control.
- **Modality:** Feed additive or orally delivered excystation blocker.
- **Stage addressed:** Stage 1 to 2.
- **Why propose it:** This is different from oocyst wall formation inhibitors. It could function as a **metaphylactic “challenge dampener”** in outbreak settings.

---

### 9. **Environmental biological control of oocysts using lytic enzymes/spore-wall degrading preparations**
- **Target:** Oocyst wall in the environment, not in the calf
- **Mechanism:** Enzymatic degradation of wall integrity on bedding/calving areas.
- **Evidence:** Enzymatic and oxidative approaches can reduce viability of hardy parasite stages in other systems; fungal enzymes and protease blends are used against resilient biostructures.
- **Modality:** Barn-applied biological disinfectant adjunct.
- **Stage addressed:** Stage 1 exposure.
- **Why propose it:** The current review stays drug-centric. But in calf crypto, **environmental load is a therapeutic target**. If a feed/nutrition company can bundle calf products with environmental control, that may outperform another weak immunomodulator.

---

### 10. **Phage-inspired bacterial ecosystem editing for co-pathogen suppression**
- **Target:** Secondary bacterial contributors in crypto diarrhea
- **Mechanism:** Reduce severity by selectively suppressing ETEC/other enteropathogens that worsen fluid loss and growth failure.
- **Evidence:** Field calves often have mixed infections. Bacteriophages and precision bacteriocins are effective in other livestock enteric settings.
- **Modality:** Phage cocktail or bacteriocin-producing probiotic.
- **Stage addressed:** Stage 5 supportive/field management.
- **Why propose it:** It does not hit Crypto directly, but real-world efficacy in calf diarrhea often depends on controlling the **polymicrobial reality**, not the pure mono-infection model.

---

### 11. **Long-acting oral adsorbent/toxin-binding mucosal protectant**
- **Target:** Luminal inflammatory mediators, bile acids, proteases, water flux
- **Mechanism:** Protect the epithelial surface and reduce stool water loss while preserving nutrient delivery.
- **Evidence:** Dioctahedral smectite and related adsorbents work in pediatric infectious diarrhea; widely used in veterinary GI disease.
- **Modality:** Clay/polymer adsorbent blend.
- **Stage addressed:** Stage 5.
- **Why propose it:** Low-tech, cheap, field-compatible. May outperform sophisticated molecules in farms if it tangibly reduces dehydration.

---

## CROSS-DISEASE ANALOGIES

### 1. **Eimeria/coccidiosis control in poultry and ruminants**
- **What worked elsewhere:** Ionophores, triazines, and management-integrated prophylaxis dramatically reduced apicomplexan burden in production animals.
- **Why relevant:** *Cryptosporidium* is also an apicomplexan with intense epithelial cycling and environmental persistence.
- **What to adapt:** Crypto differs in niche and mitochondrial biology, so classic coccidiostats may fail mechanistically, but the **program design logic** is relevant: combine direct anti-parasitic, environmental control, and nutrition rather than seek one magic bullet.

---

### 2. **Human pediatric rotavirus/norovirus diarrhea management**
- **What worked elsewhere:** ORS optimization, zinc, anti-secretory agents, and rapid supportive care can massively cut morbidity.
- **Why relevant:** In neonatal calves, mortality and growth loss come from physiology, not just pathogen counts.
- **What to adapt:** Calf-specific ORS, gut-protective additives, timing around milk feeding, and products that still work during malabsorption.

---

### 3. **Human HIV-associated cryptosporidiosis**
- **What worked elsewhere:** The biggest gains came from **immune restoration plus supportive care**; direct drugs alone were often insufficient historically.
- **Why relevant:** Neonatal calves resemble a transiently immunologically immature host.
- **What to adapt:** Not HAART, obviously—but the analogy supports combining **parasite kill + immune bridge + hydration**.

---

### 4. **Plasmodium/Toxoplasma kinase and CPSF3 programs**
- **What worked elsewhere:** PI4K and CPSF3 emerged as elite antiparasitic targets with in vivo efficacy.
- **Why relevant:** Crypto already validates both in calves.
- **What to adapt:** Resistance management from malaria—pairing, cycling, and using **non-overlapping

---

### OpenRouter (claude-4.6-opus-20260205)

# Independent Drug Discovery Analysis: Cryptosporidiosis in Neonatal Calves

## EMPIRICAL HITS (In-vivo data in the target species)

The document captures the major hits well, but there are several important omissions and under-explored results from actual calf trials:

### 1. Bumped Kinase Inhibitor 1294 (BKI-1294) — Original CDPK1 Inhibitor
**What it is:** The predecessor to BKI-1708, a pyrazolopyrimidine-scaffold CDPK1 inhibitor.
**Result:** In neonatal calves (Schaefer et al., 2016, *Int J Parasitol*), BKI-1294 at 20 mg/kg reduced oocyst shedding and improved clinical scores when given prophylactically. However, it showed hERG channel liability and skeletal toxicity concerns at higher doses.
**Why it matters:** The document mentions BKI-1708 as the improved version but doesn't adequately capture that BKI-1294 was the first kinase inhibitor to show calf efficacy. The entire BKI class has now been tested across multiple scaffolds (PP, AC, imidazopyridazine) in calves — this is the deepest in-vivo SAR dataset for any anti-crypto target in the target species. The lesson: CDPK1 is a validated calf target, but the therapeutic window for kinase inhibitors in neonates is genuinely narrow.

### 2. Decoquinate (Deccox) — Quinolone Coccidiostat
**What it is:** A feed-additive coccidiostat targeting the mitochondrial electron transport chain, widely used for *Eimeria* in poultry and cattle.
**Result:** Multiple calf trials show NO meaningful efficacy against *C. parvum* despite in-vitro activity. Lallemond et al. (2006) and others found no significant reduction in oocyst shedding or diarrhea.
**Why it matters as a NEGATIVE result:** This is the strongest evidence that mitochondrial/mitosome-targeted approaches are dead for Crypto. The document mentions this in passing under C5 but doesn't give it the weight it deserves. Decoquinate's failure, combined with CpAOX CRISPR knockout data, should be treated as a HARD KILL for any ETC-targeting strategy. This eliminates an entire class of compounds (ionophores, quinolones, atovaquone analogs) from consideration.

### 3. Azithromycin in Calves
**What it is:** Macrolide antibiotic with known anti-cryptosporidial activity in immunocompromised humans.
**Result:** Johnson et al. (2000) tested azithromycin in neonatal calves — modest reduction in oocyst shedding but no significant clinical improvement. Inconsistent results across studies.
**Why it matters:** Azithromycin's partial activity suggests the apicoplast-like ribosomal target may have some relevance, but the effect is too weak for clinical utility. More importantly, it demonstrates that drugs with human crypto efficacy don't automatically translate to calves — the neonatal bovine GI tract is pharmacologically distinct (abomasal pH, transit time, volume of ingesta).

### 4. Lasalocid and Monensin — Ionophore Coccidiostats
**What they are:** Polyether ionophores used as feed additives for *Eimeria* control.
**Result:** Multiple calf trials show no efficacy against *C. parvum*. This is consistent with the mitosome biology — ionophores disrupt mitochondrial membrane potential, which is irrelevant to Crypto's vestigial mitosome.
**Why it matters:** Another HARD KILL for the mitochondrial targeting class. Also demonstrates that "what works for Eimeria doesn't work for Crypto" — a critical lesson given that many veterinary practitioners still try coccidiostats empirically.

### 5. Oral Bovine Lactoferrin
**What it is:** Iron-binding glycoprotein from bovine milk with antimicrobial and immunomodulatory properties.
**Result:** Patel et al. (2014, *J Pediatr Gastroenterol Nutr*) and others have shown modest effects in animal models. In calves, lactoferrin supplementation has shown inconsistent results — some studies report reduced diarrhea severity, others show no effect on oocyst shedding. Importantly, lactoferrin's mechanism may involve iron sequestration (Crypto requires iron for ribonucleotide reductase) and direct sporozoite membrane disruption.
**Why it matters:** Lactoferrin is cheap, GRAS, orally stable, and within Cargill's manufacturing capability. Even a modest adjunctive effect combined with its safety profile makes it worth a properly controlled trial. The document completely omits this.

### 6. Lauric Acid / Medium-Chain Fatty Acids (MCFAs)
**What they are:** Coconut oil-derived fatty acids (C12:0 lauric acid, C8:0 caprylic acid) with direct anti-protozoal membrane-disrupting activity.
**Result:** In vitro, lauric acid and monolaurin show sporozoite killing at achievable luminal concentrations. Calf studies with coconut oil supplementation have shown mixed results — some reduction in diarrhea severity but not consistently significant oocyst reduction. A 2019 study (Vélez et al.) showed MCFA supplementation reduced *Cryptosporidium* infection intensity in calves.
**Why it matters:** MCFAs are dirt cheap, GRAS, feed-additive compatible, and directly within Cargill's palm/coconut oil supply chain. The mechanism (membrane disruption of extracellular sporozoites/merozoites) is resistance-proof. Even if the effect is modest, the cost-benefit ratio may be favorable as part of a combination protocol.

### 7. Nitazoxanide in Calves — The Full Picture
**What the document says:** "Conflicting calf data."
**What actually happened:** Schnyder et al. (2009) tested NTZ in naturally infected calves and found NO significant effect on oocyst shedding or diarrhea compared to placebo. Ollivett et al. (2009) similarly found no benefit. This is not "conflicting" — it is consistently negative in immunologically naive neonatal calves, which is entirely consistent with the immune-dependence hypothesis. NTZ works in immunocompetent human adults and older children but fails in neonates (human and bovine). This should be treated as a HARD KILL for NTZ and NTZ derivatives in neonatal calves, not as "conflicting data requiring reformulation."

---

## PROPOSED TARGETS (Not in the current analysis)

### Target 1: CpIMPDH (Inosine Monophosphate Dehydrogenase) — Purine Salvage Bottleneck
**Target:** *C. parvum* inosine-5'-monophosphate dehydrogenase, the sole enzyme converting IMP to XMP in the purine salvage pathway.
**Mechanism:** Crypto has lost de novo purine synthesis entirely and depends on salvage. CpIMPDH has significant structural divergence from human IMPDH (bacterial-like insert domain). Selective inhibitors have been developed (Mandapati et al., 2017, *Bioorg Med Chem*; Gorla et al., 2012).
**Evidence:** EC50 values in the low micromolar range in vitro. Structural basis for selectivity established by X-ray crystallography. However — and this is critical — the document's CRISPR screen data (Cell, 2025) identified nucleotide import pathways, suggesting the parasite may bypass IMPDH via direct nucleotide scavenging. This is the key risk.
**Modality:** Small molecule oral inhibitor. Several lead compounds exist.
**Disease stage:** Stage 3 (intracellular development).
**Why it's missing from the analysis:** Likely because of the bypass concern. But the bypass may be partial — IMPDH inhibition combined with nucleotide transporter blockade could be synergistic.
**De-risk:** CRISPR knockout of CpIMPDH to determine whether it's essential in the presence of host nucleotides (the relevant in vivo condition).

### Target 2: Cryptosporidium Fatty Acyl-CoA Binding Protein (CpACBP) / Fatty Acid Metabolism
**Target:** *C. parvum* has retained a Type I fatty acid synthase (CpFAS1) — unusual for an apicomplexan — and depends on both de novo synthesis and host fatty acid scavenging. CpACBP is essential for intracellular lipid trafficking.
**Mechanism:** Inhibiting fatty acid metabolism would disrupt membrane biogenesis during schizogony. Triclosan (FAS-II inhibitor) has shown anti-crypto activity in vitro, but CpFAS1 is a Type I enzyme (different from bacterial FAS-II). The real opportunity is in the lipid trafficking machinery.
**Evidence:** Zhu et al. (2004) characterized CpFAS1. In vitro activity of fatty acid synthesis inhibitors demonstrated. No calf data.
**Modality:** Small molecule.
**Disease stage:** Stage 3.
**Why it's relevant:** The document focuses heavily on tRNA synthetases, kinases, and redox metabolism but completely ignores lipid metabolism — one of Crypto's most unusual metabolic features.

### Target 3: Cryptosporidium Thymidine Kinase (CpTK) — Pyrimidine Salvage
**Target:** Like purines, Crypto depends on salvage for pyrimidines. CpTK is a key enzyme in the pyrimidine salvage pathway and has been structurally characterized.
**Mechanism:** Nucleoside analog prodrugs activated by CpTK but not host TK could achieve selective toxicity — the same strategy used in antiviral therapy (acyclovir/HSV-TK).
**Evidence:** Structural data available. Concept validated in antiviral field. Not tested for Crypto.
**Modality:** Nucleoside analog prodrug.
**Disease stage:** Stage 3.
**Why it's novel:** This "Trojan horse" approach — using the parasite's own salvage enzyme to activate a toxic nucleoside — has never been proposed for Crypto but is one of the most successful strategies in antiviral drug discovery.

### Target 4: Parasite Extracellular Vesicle (EV) Blockade
**Target:** *C. parvum*-infected cells release extracellular vesicles that modulate neighboring uninfected cells, suppressing antimicrobial peptide expression and promoting a permissive environment for parasite spread.
**Mechanism:** Block EV release (e.g., with GW4869, a neutral sphingomyelinase inhibitor) or block EV uptake by neighboring cells.
**Evidence:** Ming et al. (2018, *Parasites & Vectors*) and others have characterized Crypto-induced EV release. Host-derived EVs from infected cells suppress innate immune responses in neighboring cells.
**Modality:** Small molecule (sphingomyelinase inhibitor) or antibody-based EV capture.
**Disease stage:** Stage 3/4 (disrupts paracrine immune suppression).
**Why it's relevant:** This addresses a mechanism the document doesn't cover — the parasite's active suppression of local immunity via hijacking host EV machinery. Blocking this could restore local innate immune function without requiring systemic immunomodulation.

### Target 5: Intestinal Alkaline Phosphatase (IAP) Supplementation
**Target:** Host intestinal alkaline phosphatase — an endogenous enzyme that detoxifies LPS, maintains barrier integrity, and modulates gut inflammation.
**Mechanism:** Crypto infection damages the brush border where IAP is concentrated. Exogenous IAP supplementation could reduce secondary bacterial translocation (a major contributor to sepsis and mortality in crypto calves), maintain barrier function, and reduce inflammatory damage.
**Evidence:** IAP supplementation reduces NEC in premature infants (Biesterveld et al., 2019). Bovine IAP is commercially available. Not tested for crypto.
**Modality:** Oral enzyme supplement in milk/ORS.
**Disease stage:** Stage 5 (intestinal pathology) and Stage 7 (resolution).
**Cargill fit:** HIGH — enzyme supplementation in feed is existing Cargill capability.

### Target 6: Fecal Microbiota Transplant (FMT) from Crypto-Resistant Calves
**Target:** The gut microbiome composition that confers relative resistance to severe cryptosporidiosis.
**Mechanism:** Hares et al. (2023) showed pre-infection microbiome profiles predict susceptibility. Rather than engineering a defined consortium (C9 in the document), use FMT from calves that experienced mild/no disease despite exposure.
**Evidence:** FMT has shown efficacy in *C. difficile* (human) and various enteric infections in livestock. Not tested for crypto in calves.
**Modality:** Oral FMT capsule or suspension.
**Disease stage:** Stage 0 (upstream susceptibility).
**Why it's different from C9:** FMT transfers the entire functional community, including unknown protective species and metabolites, rather than requiring identification of specific organisms. It's empirical rather than rational — and empirical approaches often outperform rational ones in microbiome interventions.

### Target 7: Zinc Supplementation — Direct Anti-Protozoal + Mucosal Repair
**Target:** Zinc has dual mechanisms: (1) direct anti-protozoal activity (zinc disrupts parasite metalloenzymes and membrane integrity), and (2) mucosal repair (zinc promotes enterocyte proliferation and tight junction integrity).
**Mechanism:** WHO recommends zinc supplementation for all childhood diarrhea. Zinc-deficient calves have worse crypto outcomes. Zinc methionine or zinc sulfate supplementation.
**Evidence:** Multiple human pediatric studies show zinc reduces diarrhea duration and severity in cryptosporidiosis. Calf studies show zinc supplementation improves gut integrity markers. Zinc is cheap, GRAS, and feed-additive compatible.
**Modality:** Oral zinc supplement (zinc methionine for better bioavailability).
**Disease stage:** Stage 5 (pathology reduction) + Stage 7 (mucosal repair).
**Cargill fit:** VERY HIGH — mineral supplementation is core Cargill capability.
**Why it's missing:** Possibly considered too "obvious" or too modest in effect size. But the combination of direct anti-protozoal activity + mucosal repair + immune support + near-zero cost makes zinc one of the highest-value adjuncts available.

---

## CROSS-DISEASE ANALOGIES

### 1. Clostridioides difficile → Cryptosporidium: Toxin-Binding/Neutralization Strategy
**What worked:** Bezlotoxumab (anti-toxin B monoclonal antibody) reduces *C. difficile* recurrence by 40% — not by killing the organism but by neutralizing its pathogenic effector.
**Why it's relevant:** *C. parvum* secretes effector proteins into host cells during invasion and intracellular development. If key secreted effectors could be identified and neutralized (by antibodies or small molecules), this could reduce pathology without requiring parasite killing. The parasite's secretome during infection is increasingly characterized.
**What would need to be adapted:** Identification of the dominant secreted pathogenic effectors in Crypto (analogous to toxin B). Development of neutralizing agents. This is a pathology-reduction strategy, not a cure — similar to bezlotoxumab's profile.

### 2. Giardia → Cryptosporidium: Auranofin (Thioredoxin Reductase Inhibition)
**What worked:** Auranofin (gold-containing anti-rheumatic drug) kills *Giardia lamblia* by inhibiting thioredoxin-glutathione reductase, disrupting redox homeostasis. FDA-approved, cheap, oral.
**Why it's relevant:** *C. parvum* has a highly reduced redox system (lost glutathione synthesis, depends on host GSH import). Its thioredoxin system may be the primary remaining endogenous redox defense. Auranofin has shown in vitro activity against multiple protozoa. If CpTrxR is essential and structurally divergent from bovine TrxR, auranofin or analogs could exploit the same vulnerability.
**

---

### OpenRouter (qwen-2.5-72b-instruct)

## EMPIRICAL HITS (In-vivo data in the target species)

### A1. EDI048 — Gut-Restricted CpPI4K Inhibitor
- **What it is:** ATP-competitive inhibitor of *Cryptosporidium parvum* phosphatidylinositol 4-kinase (CpPI4K). Engineered as a "soft drug" with ester moiety for rapid hepatic metabolism to inactive carboxylic acid — gut-restricted activity.
- **Result:** Rapid diarrhea resolution by 48h, significant oocyst reduction, no recrudescence 7 days post-treatment, no adverse effects.
- **Trial:** Neonatal calves.
- **Why it worked:** Blocks membrane trafficking required for parasitophorous vacuole maintenance, segmentation, and egress.

### A2. AN7973 — CPSF3 Inhibitor (Benzoxaborole)
- **What it is:** Inhibitor of Cleavage and Polyadenylation Specific Factor 3 (CPSF3), an essential endonuclease in mRNA processing.
- **Result:** >99% reduction in total parasite fecal excretion, complete diarrhea elimination, no adverse effects.
- **Trial:** Neonatal calves.
- **Why it worked:** Rapidly cidal, traps enzyme in a dead-end complex, broad-stage activity (asexual + sexual stages).

### A3. MMV665917 — Piperazine-Based Compound (Unknown Target)
- **What it is:** Piperazine-based compound from Medicines for Malaria Venture (MMV) open-access collection.
- **Result:** 94% reduction in total parasite fecal excretion, prompt diarrhea resolution, improved general health, appetite, and hydration.
- **Trial:** Neonatal calves.
- **Why it worked:** Kills intracellular parasites, demonstrated therapeutic efficacy when given after severe diarrhea onset.

### A4. BKI-1708 — 5-Aminopyrazole-4-Carboxamide CpCDPK1 Inhibitor
- **What it is:** Inhibitor of *C. parvum* calcium-dependent protein kinase 1 (CpCDPK1).
- **Result:** Rapidly resolved diarrhea and improved clinical outcomes.
- **Trial:** Neonatal calves.
- **Why it worked:** Blocks invasion and egress, lower hERG liability than other BKIs.

### A5. Hyperimmune Bovine Colostrum (rC7 Antigen)
- **What it is:** Passive antibody transfer targeting sporozoite surface antigens.
- **Result:** 99.8% reduction in oocyst excretion and elimination of clinical diarrhea.
- **Trial:** Neonatal calves.
- **Why it worked:** IgG1/IgA in colostrum neutralize sporozoites during the brief extracellular transit between cells, reducing reinvasion events.

### A6. Anti-P23 IgY (Egg Yolk Antibodies)
- **What it is:** Chicken IgY antibodies against *C. parvum* P23 surface antigen.
- **Result:** Significantly reduced diarrhea duration and oocyst shedding.
- **Trial:** Neonatal calves.
- **Why it worked:** Targets sporozoite surface to block reinvasion, survived GI transit.

### A7. Halofuginone (Halocur) — Existing Standard
- **What it is:** Prolyl-tRNA synthetase (PRS) inhibitor.
- **Result:** Reduces oocyst shedding, some mortality benefit, but does NOT cure.
- **Trial:** Neonatal calves.
- **Why it worked:** Cryptostatic, activates amino acid response via integrated stress response.

## PROPOSED TARGETS (Not in the current analysis)

### D1. IL-22-Inducing Oral Innate Immune Activator
- **Target:** IL-22 production from intestinal ILC3 cells.
- **Mechanism:** Oral administration of AhR ligands (e.g., indole-3-carbinol) to induce IL-22 production.
- **Evidence:** Neonatal calves have abundant gamma-delta T cells and ILC3 cells. IL-22 drives epithelial cell renewal and upregulates antimicrobial peptides.
- **Modality:** Oral feed additive.
- **Disease Stage:** Stage 4 (Host Immune Response — innate-lymphoid-cell-mediated epithelial defense).

### D2. Lipid Raft Disruption — Methyl-Beta-Cyclodextrin or Dietary Phytosterols
- **Target:** Lipid rafts in enterocyte membranes.
- **Mechanism:** Disrupt lipid raft integrity using methyl-beta-cyclodextrin or dietary phytosterols.
- **Evidence:** Lipid rafts are essential for *C. parvum* invasion. Disruption reduces invasion efficiency.
- **Modality:** Dietary supplementation.
- **Disease Stage:** Stage 2 (Invasion — disrupts host membrane organization required for parasite entry).

### D3. Gut-Restricted Glutathione Depletion — N-Acetylcysteine Withholding + BSO
- **Target:** Reduced glutathione (GSH) in infected enterocytes.
- **Mechanism:** Use buthionine sulfoximine (BSO) to inhibit GSH synthesis, creating oxidative stress in the parasite.
- **Evidence:** *C. parvum* cannot synthesize GSH and is entirely dependent on importing it from host enterocytes.
- **Modality:** Enteric-coated formulation.
- **Disease Stage:** Stage 3 (Intracellular Development — metabolic starvation).

## CROSS-DISEASE ANALOGIES

### C1. NOD2 Agonism — MDP (Muramyl Dipeptide) or Derivatives
- **What worked elsewhere:** NOD2 receptor stimulation via MDP reduces *C. parvum* parasite burden in neonatal mice by increasing pro-inflammatory cytokine and antimicrobial peptide gene expression, rapid neutrophil influx, and epithelial renewal.
- **Why it's relevant:** The IL-22-mediated epithelial renewal mechanism is particularly interesting for neonatal calves, as it eliminates infected cells without requiring adaptive immunity.
- **What would need to be adapted:** Identify orally bioavailable NOD2 agonists and test in neonatal calves.

### C2. IFN-lambda (Type III Interferon) Supplementation
- **What worked elsewhere:** IFN-lambda acts primarily on epithelial cells, reducing *C. parvum* infection in human intestinal ALI cultures and mouse models.
- **Why it's relevant:** IFN-lambda has fewer systemic inflammatory side effects than IFN-gamma and is the dominant epithelial antiviral/antiparasitic interferon at mucosal surfaces.
- **What would need to be adapted:** Confirm bovine IFN-lambda receptor expression in neonatal calf ileal epithelium and test recombinant bovine IFN-lambda in bovine enteroid models.

### C3. Beta-Glucan Trained Immunity — Yeast Cell Wall Supplementation
- **What worked elsewhere:** Beta-1,3/1,6-glucans from yeast cell walls induce "trained immunity" in innate immune cells, enhancing responsiveness to subsequent infections.
- **Why it's relevant:** May accelerate the neonatal innate immune response to *C. parvum*.
- **What would need to be adapted:** Test beta-glucan supplementation in neonatal calves with *C. parvum* challenge to assess oocyst shedding, diarrhea severity, and immune parameters.

## WHAT WOULD YOU PRIORITISE?

### 1. **A1 — EDI048 (CpPI4K)**
- **Why:** Most advanced, gut-restricted, calf-validated. Key question: cidal or static? If cidal, it addresses the critical constraints of cidal, immunity-independent, and luminal delivery.

### 2. **A2 — AN7973 (CPSF3)**
- **Why:** Cidal, multi-stage, calf-validated. Key question: resistance barrier? If the resistance barrier is high, it could be the better target than PI4K.

### 3. **C1 — NOD2/MDP (IL-22 pathway)**
- **Why:** Novel innate immune approach, neonatal mice data. Key question: translates to calves? If it does, it could bridge the neonatal immune gap via innate (not adaptive) immunity, which is critical for neonatal calves.

These three targets address the most critical stages of the disease and have the highest potential to satisfy the Sapper constraints, particularly the need for a cidal, immunity-independent, and luminal delivery mechanism.

---

### OpenRouter (deepseek-r1)

## EMPIRICAL HITS (In-vivo data in the target species)
The following have demonstrated positive efficacy in neonatal calves or highly relevant immunocompromised mouse models (which predict immunity-independent activity in calves). Those with direct calf data are most compelling.

1. **EDI048 (CpPI4K inhibitor) – Novartis**  
   *What it is:* Gut-restricted small molecule inhibitor of *C. parvum* phosphatidylinositol 4-kinase, engineered for minimal systemic exposure.  
   *Result in calves:* Rapid diarrhea resolution within 48 hours, significant oocyst reduction, no recrudescence 7 days post-treatment, no adverse effects.  
   *Trial:* Novartis Phase 1 complete, Phase 2 recruiting in humans (NCT07249463); calf data from internal studies (not fully published).  
   *Why it worked:* Direct inhibition of an essential parasite kinase; gut-restriction maximizes luminal concentration at the infection site while minimizing systemic toxicity. Works in immunocompromised mice, confirming immunity-independent action.  
   *Caveat:* Unclear if it is parasiticidal or static; may not achieve sterilizing cure alone.

2. **AN7973 (CPSF3 inhibitor) – benzoxaborole**  
   *What it is:* Small molecule inhibitor of cleavage and polyadenylation specific factor 3, an essential mRNA processing enzyme.  
   *Result in calves:* >99% reduction in oocyst shedding, complete elimination of diarrhea, no adverse effects at 25 mg/kg.  
   *Trial:* Calf study by University of Vermont (Buckner et al., AAC 2019); also efficacious in immunocompromised mice.  
   *Why it worked:* Rapidly cidal against multiple lifecycle stages (asexual and sexual); works in absence of adaptive immunity.  
   *Caveat:* Resistance barrier not yet characterized; benzoxaborole chemistry may present stability challenges.

3. **MMV665917 (piperazine-based, unknown target)**  
   *What it is:* Phenotypic hit from MMV open-access library; target unknown.  
   *Result in calves:* 94% oocyst reduction and clinical improvement when administered therapeutically (2 days after severe diarrhea onset).  
   *Trial:* Stebbins et al. 2018, PLoS NTD.  
   *Why it worked:* Demonstrated therapeutic (not just prophylactic) efficacy; likely cidal given magnitude of oocyst reduction.  
   *Caveat:* Target unknown, so resistance risk and mechanism unclear; no follow-up development since 2018.

4. **Hyperimmune bovine colostrum (rC7 antigen)**  
   *What it is:* Colostrum from dams immunized with recombinant C7 sporozoite surface antigen.  
   *Result in calves:* 99.8% reduction in oocyst excretion and elimination of clinical diarrhea.  
   *Trial:* Multiple studies, e.g., Perryman et al., Infect. Immun. 1999.  
   *Why it worked:* High-titer IgG1 and IgA in colostrum neutralize sporozoites, blocking invasion. Passive immunity bridges the neonatal immune gap.  
   *Caveat:* Does not cure established infection; protection wanes as colostral antibodies clear.

5. **Anti-P23 IgY (egg yolk antibodies)**  
   *What it is:* Chicken IgY antibodies against P23 sporozoite surface protein, spray-dried for oral delivery.  
   *Result in calves:* Significantly reduced diarrhea duration and oocyst shedding; IgY survived GI transit.  
   *Trial:* Cho et al. 2025 (single study).  
   *Why it worked:* P23 is essential for gliding motility and reinvasion; oral IgY binds sporozoites in the lumen, blocking autoinfection.  
   *Caveat:* Single study; does not kill intracellular parasites.

6. **Halofuginone (Halocur)**  
   *What it is:* Prolyl-tRNA synthetase inhibitor; only licensed treatment in EU for calf cryptosporidiosis.  
   *Result in calves:* Meta-analysis shows oocyst reduction and some mortality benefit when used prophylactically; does not cure and has narrow therapeutic index.  
   *Trial:* Multiple field studies.  
   *Why it worked:* Cryptostatic inhibition of parasite protein synthesis.  
   *Caveat:* Static, not cidal; toxicity limits use; rebound after withdrawal.

## PROPOSED TARGETS (Not in the current analysis)
These are not covered in the 42-candidate list and address gaps or leverage under-explored biology.

1. **Cryptosporidium dihydroorotate dehydrogenase (CpDHODH)**  
   *Target & Mechanism:* CpDHODH is a key enzyme in the de novo pyrimidine biosynthesis pathway, which is essential in Cryptosporidium (unlike purine salvage). Inhibiting DHODH depletes UMP, blocking RNA/DNA synthesis.  
   *Evidence:* DHODH inhibitors (e.g., brequinar, DSM265) are effective against other apicomplexans (malaria, toxoplasmosis). Cryptosporidium has a functional pyrimidine pathway, and DHODH is conserved and likely essential (inferred from genome). In vitro studies show activity of brequinar against C. parvum.  
   *Modality:* Small molecule, oral. Could be gut-restricted to improve safety.  
   *Disease Stage:* Stage 3 (intracellular development) – blocks replication.  
   *Why it’s missed:* Most focus has been on purine salvage (IMPDH) which is absent; pyrimidine biosynthesis is intact but under-explored. DHODH inhibitors are advanced in malaria, offering repurposing potential.

2. **Host kynurenine pathway modulation via indoleamine 2,3-dioxygenase (IDO) inhibition**  
   *Target & Mechanism:* Cryptosporidium infection upregulates host IDO, depleting tryptophan and producing immunosuppressive kynurenines. Inhibition of IDO could (a) restore tryptophan levels (parasite is auxotrophic for tryptophan, so host depletion may limit parasite growth) and (b) reduce immunosuppressive kynurenines, allowing better local immune response.  
   *Evidence:* In other intracellular infections (e.g., Chlamydia, Toxoplasma), IDO induction limits pathogen growth by tryptophan starvation, but Cryptosporidium may be more sensitive due to auxotrophy. IDO inhibitors (e.g., epacadostat) are in cancer trials. In calf intestinal explants, IDO is upregulated during Crypto infection.  
   *Modality:* Small molecule IDO inhibitor, oral.  
   *Disease Stage:* Stage 3 (metabolic starvation) and Stage 4 (immune modulation).  
   *Why it’s missed:* Dual host-directed mechanism (starve parasite and boost immunity) is counterintuitive; most host-directed approaches focus on single pathways.

3. **Parasite proteasome inhibition**  
   *Target & Mechanism:* Cryptosporidium proteasome is essential for protein turnover and lifecycle progression. The parasite proteasome has distinct substrate specificity and sensitivity compared to host proteasome. Selective inhibitors (e.g., vinyl sulfones) could be parasiticidal.  
   *Evidence:* Proteasome inhibitors are effective against other apicomplexans (e.g., malaria, toxoplasmosis). Cryptosporidium proteasome subunits are divergent; screening of proteasome inhibitors showed activity in vitro. Carfilzomib (FDA-approved for myeloma) has shown activity against Cryptosporidium in high-throughput screens.  
   *Modality:* Small molecule, possibly peptide-based. Could be engineered for gut restriction.  
   *Disease Stage:* Stage 3 (intracellular development) – rapid killing via protein homeostasis disruption.  
   *Why it’s missed:* Toxicity concerns for host proteasome inhibition, but parasite-specific inhibitors are feasible due to sequence divergence. This is a high-risk/high-reward target.

## CROSS-DISEASE ANALOGIES
Approaches from other pathogens that could be adapted to Cryptosporidium.

1. **Artemisinin-based combination therapy (ACT) from malaria**  
   *What worked elsewhere:* Artemisinin derivatives (fast-acting, short half-life) combined with longer-acting partner drugs (e.g., lumefantrine) prevent resistance and improve cure rates in malaria.  
   *Relevance to Crypto:* Crypto has high R0 (5-15) and resistance risk is high. A combination of a fast-killing agent (e.g., AN7973) with a longer-acting agent (e.g., EDI048) could suppress both acute infection and prevent recrudescence.  
   *Adaptation needed:* Identify pairs with complementary pharmacokinetics and distinct mechanisms. Ensure both are gut-restricted and safe in neonates.

2. **Fecal microbiota transplantation (FMT) from C. difficile infection**  
   *What worked elsewhere:* FMT restores healthy gut microbiota and clears C. difficile infection by colonization resistance and metabolic competition.  
   *Relevance to Crypto:* Dysbiosis precedes Crypto infection; microbiome engineering (Category C9) is analogous. A defined consortium of bacteria that consume metabolites essential for Crypto (e.g., purines, isoprenoids) could reduce parasite growth.  
   *Adaptation needed:* Identify keystone species that confer colonization resistance in calves. Develop a standardized, safe consortium for neonatal calves (may be challenging due to immature gut).

3. **Monoclonal antibody (mAb) cocktails from viral infections (e.g., SARS-CoV-2)**  
   *What worked elsewhere:* Combinations of mAbs targeting distinct epitopes on viral spike protein prevent escape mutants and enhance neutralization.  
   *Relevance to Crypto:* Passive antibodies (IgY, colostrum) are effective but limited to sporozoite surface antigens. A cocktail of nanobodies or mAbs against multiple sporozoite/merozoite antigens (e.g., gp900, Cp-P34, P23) could block invasion more completely and reduce escape.  
   *Adaptation needed:* Develop orally stable nanobodies or mAb fragments that resist GI degradation. Ensure low-cost production for veterinary use.

## WHAT WOULD YOU PRIORITISE?
If I had to pick 3 targets for this disease, based on empirical evidence, feasibility, and alignment with constraints:

1. **AN7973 (CPSF3 inhibitor) – as the backbone cidal agent**  
   *Why:* It is the only compound with demonstrated cidal activity, multi-stage coverage, and efficacy in immunocompromised models and calves. It directly addresses Stage 3, the core of pathology. The benzoxaborole scaffold is amenable to oral formulation. Priority should be on characterizing its resistance barrier and optimizing veterinary formulation.

2. **Anti-P23 IgY – as an anti-reinvasion adjunct**  
   *Why:* It has positive calf data, is orally deliverable, and fits Cargill’s manufacturing capabilities (egg-based production). It blocks autoinfection, which is critical given the high R0. When combined with a cidal agent, it can reduce oocyst shedding and environmental contamination. Rapid development path as a feed additive.

3. **Host squalene synthase inhibition (lapaquistat derivative) – as a host-directed, high-resistance-barrier partner**  
   *Why:* The host-directed approach has an unparalleled resistance barrier (parasite cannot mutate around host enzyme). The CRISPR screen validation (Cell 2025) is strong. Despite lapaquistat’s hepatotoxicity, a gut-restricted derivative could limit systemic exposure while acting on enterocytes. This targets the parasite’s absolute dependency on host glutathione, a metabolic vulnerability. It complements direct antiparasitics by attacking a different aspect of parasite survival.

**Rationale:** This combination covers multiple stages: AN7973 kills intracellular parasites, IgY blocks reinvasion, and host squalene inhibition starves the parasite of essential metabolites. It balances direct parasiticidal action, transmission reduction, and a novel host-directed mechanism with high resistance barrier. All three have some empirical support and are compatible with oral/feed-additive delivery.

---

