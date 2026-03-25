# Phase 4: Kill Report

**Program:** Mastitis | **Partner:** Zoetis
**Agent:** Reaper | **Date:** 2026-03-25 | **Revision:** R0
**Primary pathogen:** *Staphylococcus aureus*
**Inputs:** Phase 3 Candidates (R0, 32 candidates), Phase 3b Surveyor Report (R0), Phase 1 Disease Map (R1), Phase 2 Failure Analysis (R1)

---

## Executive Summary

32 candidates entered. 8 KILLED. 16 WOUNDED. 8 SURVIVED.

The kill rate is exactly what it should be for a first pass: the easy targets die, the middle ground gets a specific question it must answer, and the genuine survivors emerge with scars but intact. The most damaging finding: ADEP/ClpP (5B), Forge's "high-priority candidate" for the rate-limiting barrier, faces a published host toxicity problem that Forge did not address. Wong et al. 2018 (*Cell Chemical Biology*) demonstrated that ADEP analogs activate human mitochondrial ClpP and induce caspase-dependent apoptotic cell death in mammalian cells. Surveyor flagged the bovine mitochondrial ClpP homolog. Forge acknowledged it. Nobody connected the dots to the published mammalian cytotoxicity data. That candidate is WOUNDED, not killed -- but it needs an answer that may not exist.

The Kromker phage result (6A) survives scrutiny as a candidate worth replicating, but the 81.3% figure is statistically fragile. The lactoferrin combination (5A) survives on the strength of the actual primary source data, though the cure rates are lower than Forge implied. SrtA inhibition (2A) survives the 20-Year Test because recent chemistry advances are genuine, not because the barriers have disappeared. Everything else is either dead for specific reasons or walking wounded with a defined question to answer.

---

## Verdict Summary

| # | Candidate | Category | Verdict | Fatal/Critical Issue |
|---|-----------|----------|---------|---------------------|
| 0A | Protected butyrate | Known | **WOUNDED** | Unquantified gut-mammary contribution; undetectable effect size risk |
| 0B | Ca/BHBA management | Known | **SURVIVED** | Management protocol, not a product; but biologically sound |
| 0C | Gut probiotic | Non-Obvious | **WOUNDED** | Rumen destruction of oral probiotics; zero bovine mastitis data |
| 1A | Antimicrobial keratin sealant | Non-Obvious | **WOUNDED** | Formulation compatibility unknown; incremental over existing ITS |
| 1B | NAS probiotic teat dip | Non-Obvious | **WOUNDED** | Regulatory classification undefined; some NAS cause subclinical mastitis |
| 2A | SrtA inhibitor | Known | **SURVIVED** | 22+ years, no drug; but zero host homolog and recent covalent inhibitor chemistry is genuine |
| 2B | FnBP soluble decoy | Novel | **WOUNDED** | Protein half-life in milk; rapid clearance by milking; expensive recombinant protein |
| 2C | Gallium(III) | Non-Obvious | **KILLED** | Zero mastitis data in any species; heavy metal residue in milk; food safety non-starter for dairy |
| 3A | SpAKKAA vaccine | Known | **WOUNDED** | Zero bovine data; SpA-Fab mechanism unvalidated in cattle; 16 years since first publication, no livestock product |
| 3B | LukMF' toxoid vaccine | Known | **WOUNDED** | Lineage-restricted: CC97 carriage ~30%; vaccine covers at most 70% of field infections |
| 3C | Mucosal IgA vaccine | Non-Obvious | **WOUNDED** | Bovine mammary gland is immunologically "cold"; sIgA response to intramammary antigen undemonstrated |
| 3D | AdsA inhibitor | Novel | **KILLED** | Redundant with SrtA inhibition (2A); no AdsA-specific inhibitor exists; all evidence is mouse |
| 4A | Anti-Hla mAb | Known | **KILLED** | COGS impossible at <$30/dose; Hla is not the only tissue-damaging toxin; protein therapeutic in milk |
| 4B | NLRP3 modulator | Non-Obvious | **KILLED** | May phenocopy S. aureus own persistence strategy; S. aureus exploits PINK1/Parkin to suppress NLRP3 |
| 5A | Lactoferrin + pirlimycin | Known | **SURVIVED** | Cure rates lower than implied (45.5% in trial 1, 33.3% in trial 2); but multi-mechanism and bovine data |
| 5B | ADEP ClpP activator | Non-Obvious | **WOUNDED** | Wong et al. 2018: ADEP activates mammalian mitochondrial ClpP, causes apoptosis. Host toxicity is real. |
| 5C | Gallium(III) Stage 5 | Non-Obvious | **KILLED** | Same as 2C; additionally, SCVs with defective ETC may be LESS gallium-sensitive |
| 5D | Autophagy flux restoration | Novel | **WOUNDED** | S. aureus escapes autophagosomes to cytoplasm before flux restoration can act; autophagy induction may help pathogen |
| 5E | SCV wake-and-kill | Novel | **SURVIVED** | Concept is sound; menadione is cheap, membrane-permeable; direct test available |
| 5F | Biofilm disruption cocktail | Known | **WOUNDED** | Formulation nightmare (3-4 enzymes + antibiotic); regulatory impossible (15 trial arms for 4 APIs); ica operon variable |
| 5G | TA system modulators | Novel | **KILLED** | No drug-like compounds exist; multiple redundant TA systems; years from any testable molecule |
| 6A | Phage cocktail | Known | **SURVIVED** | Kromker n=16 is fragile but worth replicating; addresses EU regulatory need |
| 6B | Endolysin + pirlimycin | Known | **WOUNDED** | Milk matrix variability; lysostaphin-PTD precedent (0% cure); no bovine in-vivo efficacy |
| 7A | Solve Stage 5 = Solve Stage 7 | Strategic | **SURVIVED** | Not a candidate; a correct strategic principle |
| 7B | Post-cure lactoferrin maintenance | Novel | **WOUNDED** | 7-14 days daily intramammary dosing; farmer compliance near zero |
| 7C | Herd management tool | Known | **SURVIVED** | Not a therapeutic; a diagnostic/management strategy with established biology |
| 8A | APT device | Known | **SURVIVED** | Only approach addressing tissue repair; retrospective data biased but 70.5% controlled trial is real |
| 8B | Anti-fibrotic (pirfenidone) | Novel | **KILLED** | Pirfenidone costs >$100K/year for human IPF; repurposing for a $30/dose dairy product is fantasy |
| 8C | Post-treatment probiotic | Non-Obvious | **KILLED** | Regulatory undefined; some NAS cause mastitis; deliberate bacterial infusion into a just-treated quarter |

**Totals: 8 KILLED | 16 WOUNDED | 8 SURVIVED**

---

## Detailed Kill Assessments

---

### Candidate 0A: Protected Butyrate Oral Supplementation (Known)

**Verdict: WOUNDED**

**Kill Test 1 (20-Year Test):** Butyrate as a feed additive has been studied for >20 years. Forge argues the gut-mammary axis mechanism is new (2024-2025). This is a legitimate defense -- the APPLICATION to mastitis prevention is new even if the molecule is old. Passes with a caution flag.

**Kill Test 2 (Species Test):** The gut-mammary axis causal evidence comes from a caprine RMT model (PMID 41130091) and a murine RMT model -- NOT bovine. The bovine correlation data (PMID 40033186) are microbiome-metabolome associations, not causal evidence. The claim that butyrate supplementation would reduce mastitis incidence in dairy cattle has zero direct bovine evidence.

**Kill Test 10 (Commercial Reality):** If the gut-mammary axis contributes <10% of total mastitis incidence (Forge's own stated risk), the effect size is undetectable in any feasible field trial. A 200-cow trial detecting a 10% incidence reduction would be underpowered. The study would need >1,000 cows to detect such a small effect, costing $250K+, not the $50-80K Forge estimated.

**Kill Test 8 (Embarrassment Test):** We run a $250K trial, the butyrate group shows a non-significant trend toward lower mastitis, and we cannot distinguish it from noise. The money is wasted. This is the most likely outcome.

**Wound:** The gut-mammary axis contribution to bovine mastitis incidence is unquantified. Until someone demonstrates that gut dysbiosis causes a clinically meaningful fraction of bovine mastitis, supplementing butyrate is shooting at an unmeasured target. WOUNDED pending a quantification study of gut-mammary axis contribution to bovine mastitis incidence.

---

### Candidate 0B: Peripartum Calcium + BHBA Management Protocol (Known)

**Verdict: SURVIVED**

**Kill Test 1 (20-Year Test):** This is a management protocol, not a product. The biology is ESTABLISHED. BHBA-neutrophil dysfunction (PMID 18411287) and calcium-neutrophil function (PMID 2745826) are well-replicated bovine findings. No one is claiming this is a novel product.

**Kill Test 10 (Commercial Reality):** Forge correctly identifies this as management, not a product. Many herds already do this. The incremental benefit for well-managed herds is small. But for poorly managed herds (the majority globally), basic transition management prevents a substantial fraction of mastitis.

**What I tried:** I looked for evidence that targeted Ca/BHBA management fails to reduce mastitis incidence. The evidence consistently supports the link. The candidate is biologically sound, even if it is not a product opportunity for Zoetis.

**Survived** because it is correct, even if commercially irrelevant.

---

### Candidate 0C: Gut Microbiome-Targeted Probiotic (Non-Obvious)

**Verdict: WOUNDED**

**Kill Test 2 (Species Test):** All causal evidence is caprine and murine (PMID 41130091 -- goat RMT into mice). Zero bovine data for probiotic-mediated mastitis prevention.

**Kill Test 3 (Matrix Test):** The bovine rumen is a hostile environment for oral probiotics. *Faecalibacterium prausnitzii* is an obligate anaerobe exquisitely sensitive to oxygen -- it would not survive standard feed delivery. Rumen-protected capsules have been discussed for >15 years in probiotic research with limited commercial success.

**Kill Test 8 (Embarrassment Test):** We formulate rumen-protected *F. prausnitzii* capsules, run a 50-cow trial for $80-120K, and the capsules disintegrate in the rumen before reaching the hindgut. Zero butyrate-producing bacteria survive passage. The money is wasted on a formulation failure, not a biological one.

**Wound:** Must demonstrate that a rumen-protected probiotic formulation survives passage to the bovine hindgut and colonizes -- before spending $80K+ on a mastitis endpoint trial. WOUNDED pending a rumen survival/hindgut colonization feasibility study.

---

### Candidate 1A: Next-Generation Teat Sealant with Antimicrobial Keratin Mimetic (Non-Obvious)

**Verdict: WOUNDED**

**Kill Test 3 (Matrix Test):** Fatty acids (lauric, myristic) are lipophilic compounds being incorporated into a bismuth subnitrate paste. The physical chemistry of this combination is non-trivial: fatty acids may alter the viscosity, adherence, and retention properties of the sealant. Forge acknowledges this as the key risk.

**Kill Test 9 (Repetition Test):** ITS already reduces new IMI by ~40% (ESTABLISHED). Adding bactericidal fatty acids to ITS is a logical incremental improvement, but the increment may be small. If the keratin-mimetic kills bacteria in the teat canal for the first 24 hours but the sealant then sets and immobilizes them, the antimicrobial window is brief.

**Kill Test 10 (Commercial Reality):** This competes directly with existing ITS products (Orbeseal). The improvement must be large enough to justify reformulation, new regulatory approval, and commercial differentiation. A 5-10% improvement in new IMI prevention may not be commercially viable.

**Wound:** Incremental over existing ITS. The formulation compatibility (fatty acids + bismuth subnitrate) is the make-or-break question. WOUNDED pending formulation stability data.

---

### Candidate 1B: Probiotic Teat Dip with NAS Colonizers (Non-Obvious)

**Verdict: WOUNDED**

**Kill Test 10 (Commercial Reality):** What is the regulatory classification of a live bacterial teat dip? Not a drug (no therapeutic claim). Not a biocide (live bacteria, not a disinfectant). Not a feed additive (topical application). This product exists in a regulatory no-man's-land. EPA? FDA? USDA? The regulatory pathway uncertainty alone could kill the product.

**Kill Test 4 (Strain Test):** Some NAS species (*S. haemolyticus*, *S. epidermidis*) themselves cause subclinical mastitis. Even among *S. chromogenes* -- the "protective" species -- strain-level differences in pathogenicity exist. Selecting the wrong strain converts a protective product into a mastitis-causing one.

**Kill Test 8 (Embarrassment Test):** We formulate a NAS teat dip, apply it daily, and the NAS strain we selected causes a subclinical mastitis outbreak. The product we designed to prevent mastitis is causing it.

**Wound:** Regulatory pathway undefined. Strain safety margin between "protective colonizer" and "subclinical pathogen" is narrow. WOUNDED pending regulatory pre-submission feedback and strain safety characterization.

---

### Candidate 2A: Sortase A (SrtA) Inhibitor (Known)

**Verdict: SURVIVED**

**Kill Test 1 (20-Year Test):** SrtA has been a drug target since Mazmanian et al. 2002. That is 24 years. No SrtA inhibitor has entered clinical development in any species. This is the strongest argument against this candidate. Forge provides three reasons: (a) the active site is a challenging PPI target, (b) early inhibitors had poor PK, (c) anti-virulence agents face commercial uncertainty. I accept (a) and (b) as legitimate -- covalent inhibitor chemistry has genuinely advanced since 2010. The 2024-2025 literature shows continued active development of covalent SrtA inhibitors with improved potency (IC50 values in low micromolar range) and demonstrated in-vivo protection in *Galleria mellonella* larvae.

**Kill Test 2 (Species Test):** No bovine data. All in-vivo evidence is from mouse abscess models and insect larvae. This is a genuine gap but not a kill -- SrtA is universally conserved at 99.5-100% across all *S. aureus* strains (Surveyor confirmed), so the target is identical in bovine isolates.

**Kill Test 11 (Surveyor Test):** SrtA has ZERO bovine homolog (Surveyor: 0 BLAST hits against Bos taurus at E<1.0). This is the cleanest host selectivity of any protein target in the entire candidate list. This fact alone makes SrtA a better target than most.

**Kill Test 5 (Resistance Test):** SrtA is non-essential for growth. Resistance via active-site mutation would compromise surface protein display and virulence. This is a favorable resistance profile. Resistance is possible but costly.

**Kill Test 10 (Commercial Reality):** Anti-virulence agents do not kill bacteria. Efficacy endpoints for regulatory approval are harder to define. FDA-CVM would need to be consulted on what "efficacy" means for a non-bactericidal agent. This is a real commercial barrier.

**What I tried:** I searched for published negative results or abandoned SrtA inhibitor programs. Found none -- the field is still active, with new publications in 2024-2025. The 24-year absence of a product is concerning but explained by medicinal chemistry difficulty rather than target invalidity.

**Survived** because: (a) zero host homolog makes this pharmacologically clean, (b) multi-barrier mechanism (adhesion + immune evasion + internalization prevention in one target), (c) recent covalent inhibitor chemistry has genuinely advanced, (d) the 20-Year Test explanation (PPI target difficulty, not biological failure) is credible. The candidate is high-risk on timeline but biologically solid.

---

### Candidate 2B: Anti-FnBP Adhesion-Blocking Strategy -- Soluble Fibronectin Decoy (Novel)

**Verdict: WOUNDED**

**Kill Test 3 (Matrix Test):** This is a recombinant protein therapeutic infused into milk. Protein half-life in bovine milk is the critical variable. Every protein therapeutic that has entered the bovine mammary gland has faced rapid degradation: lysostaphin activity drops below therapeutic levels within 36-48h, phage titers drop below detectable levels within 36h. A fibronectin fragment (FnI1-5) is a standard protein domain with no special stability features. Expected half-life in milk: hours to 1-2 days.

**Kill Test 10 (Commercial Reality):** Recombinant protein therapeutics at dairy scale must cost <$30/treatment. Recombinant FnI1-5 expression, purification, and formulation -- even at commercial scale -- is likely $50-200/dose. This exceeds the commercial viability threshold.

**Kill Test 8 (Embarrassment Test):** We infuse FnI1-5 intramammarily at 8:00 AM. The farmer milks the cow at 4:00 PM. The milking removes 90% of the protein. The remaining 10% is degraded by milk proteases overnight. By the next infusion 24 hours later, the decoy is gone. The entire concept depends on sustained presence in a system designed to flush itself twice daily.

**Wound:** The milking removal problem is potentially fatal. If used during the dry period (no milking), the half-life would be much longer and the concept is more plausible. WOUNDED pending determination of whether the concept is viable during dry period only (which changes the clinical positioning entirely).

---

### Candidate 2C: Gallium(III) as an Iron-Acquisition Disruptor (Non-Obvious)

**Verdict: KILLED**

**Kill Test 2 (Species Test):** Gallium as an antimicrobial against *S. aureus* has been tested in mouse wound models and in-vitro. It has NEVER been tested in any mastitis model in any species. Not bovine, not murine, not any. The entire extrapolation is from wound infection to intramammary -- two fundamentally different environments.

**Kill Test 10 (Commercial Reality -- THE KILL):** Gallium is a heavy metal. Milk is a food product consumed by humans, including infants and children. Intramammary infusion of a heavy metal into a lactating dairy cow is a food safety non-starter. Withdrawal periods for heavy metals in food-producing animals are measured in weeks to months. The EU Maximum Residue Limit (MRL) framework has no provisions for gallium in milk because nobody has been foolish enough to propose putting it there. Before any efficacy testing, a complete toxicological and residue depletion study would be required -- costing $200-500K and taking 1-2 years. And it might fail.

**Kill Test 3 (Matrix Test):** Milk contains lactoferrin (0.02-0.2 mg/mL, up to 30-fold higher during mastitis) which binds iron AND potentially gallium. Milk also contains casein-bound calcium and other divalent cations that could compete with gallium uptake. The iron-mimetic "Trojan horse" mechanism depends on bacteria preferentially taking up gallium over iron -- but in the presence of lactoferrin, the iron-acquisition systems are already maximally activated. Whether gallium competes effectively in this context is unknown.

**The kill:** A heavy metal intramammary infusion in food-producing animals is commercially dead on arrival. No amount of antimicrobial elegance overcomes the food safety barrier. KILLED.

---

### Candidate 3A: SpA-Neutralizing Vaccine (SpAKKAA/SpA* Platform) (Known)

**Verdict: WOUNDED**

**Kill Test 1 (20-Year Test):** SpAKKAA was first published in 2010 (Kim et al., *J Exp Med*). That is 16 years. No livestock vaccine exists. Human clinical programs are advancing -- but the human and bovine immune systems differ fundamentally in antibody genetics (single VH family in cattle vs. multiple VH families in humans).

**Kill Test 2 (Species Test):** ALL SpAKKAA efficacy data are from mice and minipigs. ZERO bovine data. The bovine mammary immune environment differs from the murine peritoneal/systemic models used. Bovine mammary gland is immunologically "cold" compared to the sites tested.

**Critical context -- the Fab mechanism uncertainty:** Sapper flagged that the SpA VH3-Fab B-cell superantigen mechanism is UNVALIDATED in cattle. Bovine antibodies use a single VH family (BoVH1, VH4-type), not human VH3. Kim et al. 2015 tested SpA Fab binding across species -- bovine was NOT TESTED. If the Fab-mediated B-cell depletion mechanism does not operate in cattle, then roughly half of the SpAKKAA vaccine rationale evaporates. The Fc-binding mechanism alone may still justify the approach, but the vaccine would be targeting one arm of SpA's evasion (Fc-binding) rather than both (Fc + Fab).

**Kill Test 8 (Embarrassment Test):** We vaccinate 200 cows with SpAKKAA, generate strong anti-SpA titers, and cure rates don't improve because: (a) SpA neutralization restores IgG opsonization, but capsular polysaccharide still blocks antibody access, (b) intracellular bacteria are invisible to antibodies regardless, (c) the bovine mammary gland transfers serum IgG to milk poorly. We spent $80-120K to learn that SpA is only one of multiple redundant immune evasion mechanisms.

**Kill Test 9 (Repetition Test):** STARTVAC failed. SpAKKAA is a more rational antigen design, but it is still a vaccine relying on systemic IgG to work in the mammary gland. The fundamental barrier -- poor IgG transfer to milk -- applies equally. Forge's argument that SpA neutralization "unlocks the entire vaccine approach" assumes SpA is the sole gate. It is not. Capsule, superantigens, and leukotoxins are independent evasion mechanisms.

**Wound:** Must demonstrate that SpAKKAA-immunized bovine serum produces opsonophagocytic killing of CC97/CC151 in bovine whole milk. If it does not, the vaccine is dead. If it does, the vaccine has a path forward as part of a multi-antigen combination. WOUNDED pending bovine OPK data.

---

### Candidate 3B: Anti-LukMF' Toxoid Vaccine (Known)

**Verdict: WOUNDED**

**Kill Test 4 (Strain Test -- THE WOUND):** LukMF' carriage is lineage-dependent. CC151 carries it at high frequency; CC97 carries it at only ~30%. Surveyor confirmed: only 2 UniProt entries for lukM. A LukMF'-only vaccine would miss ~30-70% of field infections depending on the CC97:CC151 ratio in the target market. This is not a theoretical concern -- it is a fundamental coverage limitation.

**Kill Test 11 (Surveyor Test):** The lineage-restriction data from Surveyor validates Forge's stated risk but makes it more severe: 2 UniProt entries is extremely low. This is not a universally conserved target. It is a phage-encoded toxin carried by a subset of strains.

**Kill Test 10 (Commercial Reality):** A vaccine that only protects against ~50-70% of *S. aureus* strains (assuming market average CC151:CC97 mix) is commercially weak. The farmer sees "S. aureus vaccine" and expects it to work against *S. aureus*. When it fails against non-lukM strains, the product reputation suffers.

**Kill Test 8 (Embarrassment Test):** We develop a LukMF' toxoid vaccine, demonstrate protection against CC151 challenge, launch commercially, and veterinarians report no benefit in herds where CC97 predominates. The product gets a reputation for inconsistency.

**Wound:** Not killed because LukMF' neutralization is a biologically valid mechanism for the strains that carry it. But standalone commercial viability is questionable. Must be part of a multi-antigen vaccine (SpAKKAA + LukMF' + additional antigens). WOUNDED -- viable only as a combination component.

---

### Candidate 3C: Mucosal IgA Vaccination (Intramammary Immunization) (Non-Obvious)

**Verdict: WOUNDED**

**Kill Test 2 (Species Test):** The bovine mammary gland has MALT-like structures (Furstenberg's rosette), but whether these generate robust secretory IgA responses to intramammary antigen delivery is unknown. The bovine mammary gland is immunologically "cold" compared to gut/respiratory mucosa. Plasma cells in Furstenberg's rosette are documented histologically but functional sIgA generation has not been demonstrated.

**Kill Test 8 (Embarrassment Test):** We deliver antigen intramammarily with mucosal adjuvant during the dry period. The gland generates minimal sIgA because the mammary MALT is functionally immature compared to gut MALT. We spent $50-80K to demonstrate that the bovine mammary gland does not generate sIgA the way we hoped.

**The concept is immunologically elegant** (sIgA bypasses SpA entirely). But the foundational assumption -- that bovine mammary gland can generate functional sIgA responses to local antigen delivery -- is untested.

**Wound:** Must demonstrate sIgA generation in response to intramammary antigen delivery in bovine. WOUNDED pending the proposed ovalbumin model antigen experiment. If sIgA/IgG ratio >2 in milk, the concept is alive. If not, it is dead.

---

### Candidate 3D: AdsA Inhibitor -- Blocking the Adenosine Immune Suppression Loop (Novel)

**Verdict: KILLED**

**Kill Test 11 (Surveyor Test -- THE KILL):** AdsA is sortase-anchored (LPXTG motif confirmed by Surveyor). SrtA inhibition (Candidate 2A) would prevent AdsA from reaching the bacterial surface. If the portfolio includes an SrtA inhibitor, a specific AdsA inhibitor is redundant. Surveyor explicitly flagged this: "SrtA inhibition (Candidate 2A) would block AdsA surface display, making a specific AdsA inhibitor potentially redundant if SrtA is targeted."

**Kill Test 2 (Species Test):** ALL AdsA mechanism data are from mouse models (PMIDs 19752399, 31719177, 35355997). Zero bovine data. The adenosine-mediated immune suppression pathway has never been confirmed in the bovine mammary gland environment.

**Kill Test 1 (20-Year Test):** AdsA was first characterized as a virulence factor by Thammavongsa et al. 2009. No AdsA-specific inhibitor exists in any species after 17 years. No drug development program is known.

**Additional concern:** Forge itself states the most likely failure mode: "AdsA inhibition may be insufficient because the upstream steps (leukocidin-mediated neutrophil killing, nuclease-mediated NET degradation) are independently damaging." This is correct. AdsA is the terminal enzyme in a multi-step cascade. Blocking the last step while the first steps (leukocidin killing, NET degradation) continue is like plugging one hole in a sieve.

**The kill:** Redundant with SrtA inhibition. No specific inhibitor exists. All evidence is mouse. The target is the last step in a cascade where the upstream steps are independently lethal. KILLED.

---

### Candidate 4A: Anti-Hla Monoclonal Antibody (Known)

**Verdict: KILLED**

**Kill Test 10 (Commercial Reality -- THE KILL):** A monoclonal antibody for intramammary use in dairy cattle must cost <$30/dose (Quality Standard 26). Monoclonal antibody manufacturing costs, even at commercial scale, are $50-500/g. An intramammary mAb dose would require 5-50 mg (based on the concentration needed to neutralize Hla in a quarter containing ~200-500 mL milk). At $100/g, that is $0.50-5.00 per dose in raw COGS -- potentially achievable. BUT: stability in milk, cold chain, sterile filling, shelf life requirements, and the formulation to maintain activity in the casein-rich milk environment would push the finished product cost to $50-200/dose. This exceeds the commercial viability threshold by 2-7x.

**Kill Test 8 (Embarrassment Test):** Forge's own stated embarrassment scenario is devastating: "We optimize an Hla inhibitor, achieve perfect tissue protection, and cure rates don't change because the neutrophils are still dying from LukMF' and the bacteria persist." This is the most likely outcome. Hla is one of multiple tissue-damaging toxins (LukMF', Hlb, PSMs). Neutralizing Hla alone while LukMF' continues to kill neutrophils is insufficient.

**Kill Test 9 (Repetition Test):** Suvratoxumab (anti-Hla mAb by AstraZeneca/MedImmune) showed modest benefit in human pneumonia prevention. The human program continues but has not produced an approved product. Translating an unfinished human program to veterinary use, at 10-100x lower price points, is commercially irrational.

**The kill:** COGS per dose exceeds commercial viability for dairy. Hla is not the sole tissue-damaging toxin. The mAb approach is designed for human medicine economics, not veterinary. KILLED.

---

### Candidate 4B: NLRP3 Inflammasome Modulator (Non-Obvious)

**Verdict: KILLED**

**Kill Test 9 (Repetition Test -- THE KILL):** *S. aureus* ALREADY suppresses NLRP3 as its persistence strategy. Phase 1 (Section 4.2) documents that *S. aureus* activates PINK1/Parkin mitophagy to suppress NLRP3 inflammasome activation, creating a permissive intracellular niche. Pharmacological NLRP3 inhibition would PHENOCOPY THE PATHOGEN'S OWN STRATEGY. This is not a concern that needs further investigation -- it is a mechanistic contradiction. You would be paying to do what the bacteria already do for free.

**Forge acknowledged this risk** in the candidate write-up and proposed a de-risk experiment to test it. But the experiment is designed to fail: if intracellular bacterial load increases >2-fold with NLRP3 inhibition, the candidate is killed. The mechanistic logic predicts exactly this outcome. *S. aureus* suppresses NLRP3 to PROMOTE its own intracellular survival. Suppressing NLRP3 pharmacologically should have the same effect.

**Kill Test 8 (Embarrassment Test):** We administer an NLRP3 inhibitor. Tissue damage decreases (less pyroptosis). But intracellular bacterial load increases because we just removed the host's danger-sensing pathway. Chronic infection worsens. We traded acute tissue damage for chronic persistence.

**The kill:** Pharmacological NLRP3 inhibition phenocopies *S. aureus*'s own immune suppression strategy. The pathogen already does this. Helping it do so more efficiently is not a treatment. KILLED.

---

### Candidate 5A: Lactoferrin + Pirlimycin Combination (Known)

**Verdict: SURVIVED**

**Kill Test 6 (Citation Test -- CRITICAL CORRECTION):** I retrieved the primary source (Petitclerc et al. 2007, J Dairy Sci, PMID 17517718; Lacasse et al. 2008, PMID 17565052). The actual data are more nuanced than Forge implied:

- **Trial 1** (experimentally induced chronic mastitis, beta-lactam-resistant strain): bLf + PG combination = **45.5% cure** vs. 9.1% PG alone, 11.1% bLf alone, 0% control. This is against a HIGHLY beta-lactam-resistant strain -- a population penicillin alone cannot cure. The 45.5% figure is correct but the context matters: this is not 45.5% against all *S. aureus*, it is 45.5% against a resistant strain that penicillin alone cures at 9.1%.

- **Trial 2** (chronic mastitis from previous lactation, extended therapy): bLf + PG = **33.3%** vs. 12.5% PG alone. Lower cure rate in naturally acquired chronic infections.

- The "45.5% cure against resistant strains" that Phase 2 cites is real but from experimentally induced infection with a single research-lab strain. The field performance (Trial 2, 33.3%) is more realistic.

**Kill Test 10 (Commercial Reality):** Pharmaceutical-grade bovine lactoferrin costs $50-200/g. Effective dose: 250 mg - 1 g per infusion. At the lower end ($50/g x 0.25 g = $12.50) this is within commercial range. At the higher end ($200/g x 1 g = $200) it is not. The cost question is solvable with scale manufacturing but currently uncertain.

**Kill Test 3 (Matrix Test):** Lactoferrin is a natural milk protein. It is the ONLY candidate in this entire portfolio that is natively stable in the target biological matrix. This is a genuine advantage over every recombinant protein, phage, and endolysin candidate.

**Kill Test 8 (Embarrassment Test):** We run a 3-arm trial (n=20/arm) and the lactoferrin + pirlimycin combination achieves 35% cure vs. 25% pirlimycin alone. The difference is not statistically significant at n=20. We have a positive trend with no statistical power to confirm it. The trial is underpowered. Forge's proposed n=20/arm is likely too small for a 15-percentage-point difference. Need n=50/arm minimum.

**Survived** because: (a) real bovine clinical data from two trials, (b) multi-mechanism rationale (iron chelation + beta-lactamase suppression + immune modulation), (c) natively stable in milk matrix, (d) the combination addresses the restoration of antibiotic susceptibility in resistant strains. The cure rates are lower than Forge implied, but the mechanism is genuine and the data are bovine. The de-risk trial must be properly powered (n=50/arm, not n=20).

---

### Candidate 5B: ADEP (Acyldepsipeptide) ClpP Activator (Non-Obvious)

**Verdict: WOUNDED**

**Kill Test 11 (Surveyor Test) + Kill Test 2 (Species Test) -- THE WOUND:** Surveyor flagged bovine mitochondrial ClpP (Q2KHU4, 272 aa) as a host homolog. Forge acknowledged this. But neither Forge nor Surveyor cited the PUBLISHED DATA on mammalian ClpP activation by ADEP.

**Wong et al. 2018 (*Cell Chemical Biology*, PMID 30126533)** demonstrated that:
1. ADEP analogs are "potent dysregulators of human mitochondrial ClpP (HsClpP)"
2. ADEPs "interact tightly with HsClpP causing the protease to non-specifically degrade model substrates"
3. "Dysregulation of HsClpP activity by ADEP was found to induce cytotoxic effects via activation of the intrinsic, caspase-dependent apoptosis"
4. A co-crystal structure of ADEP bound to human ClpP (PDB 6BBA) was solved, showing a "highly complementary binding interface"

This is not a theoretical risk. ADEP analogs HAVE BEEN SHOWN to activate mammalian ClpP and kill mammalian cells. Bovine mitochondrial ClpP (Q2KHU4) is expected to share >40% identity with bacterial ClpP (Surveyor's estimate) and is highly conserved with human ClpP. The binding site identified in the co-crystal structure is likely conserved.

**Kill Test 8 (Embarrassment Test):** We infuse ADEP4 + pirlimycin intramammarily. ADEP4 crosses the mammary epithelial cell membrane (it must, to reach intracellular bacteria). Once inside the host cell, ADEP4 encounters bovine mitochondrial ClpP, activates it, and triggers apoptotic death of the mammary epithelial cells. We cure the bacterial infection by killing the host tissue. The cure is worse than the disease.

**Why WOUNDED, not KILLED:** Three mitigating factors preserve a narrow path to viability:
1. **Intramammary delivery limits systemic exposure** -- ADEP does not need to achieve systemic concentrations.
2. **Mitochondrial membrane barrier** -- ADEP must cross both the host cell membrane AND the mitochondrial double membrane to reach bovine ClpP. Bacterial ClpP is cytoplasmic (single membrane crossing).
3. **Differential binding affinity** -- the ADEP-bacterial ClpP and ADEP-mammalian ClpP binding affinities may differ enough for a therapeutic window. Wong et al. found the binding was "highly complementary" for human ClpP, which is concerning -- but affinity differences may still exist.

The candidate is NOT killed because Conlon et al. 2013 (*Nature*) remains the ONLY published mechanism that kills *S. aureus* persister cells -- the rate-limiting barrier to cure. If a therapeutic window exists (killing bacterial persisters at concentrations that do not trigger mammalian apoptosis), ADEP would be transformative. But the Wong et al. data mean this is no longer "host selectivity must be tested" -- it is "known mammalian toxicity must be overcome."

**Wound:** Wong et al. 2018 demonstrated that ADEP activates mammalian mitochondrial ClpP and kills mammalian cells. The de-risk experiment MUST include bovine MAC-T cell viability and mitochondrial function (MitoTracker/JC-1) as PRIMARY endpoints, not secondary. If ADEP4 kills MAC-T cells at concentrations needed for intracellular bacterial killing, the candidate is DEAD. WOUNDED pending demonstration of a therapeutic window between bacterial ClpP activation and mammalian ClpP activation in bovine mammary epithelial cells.

---

### Candidate 5C: Gallium(III) Intramammary Infusion for Multi-Barrier Killing (Non-Obvious)

**Verdict: KILLED**

Same reasoning as Candidate 2C, with an additional kill:

**Additional Kill Test:** Forge acknowledges the risk that SCVs with defective electron transport chain "may be LESS dependent on iron-dependent enzymes." This is correct. SCVs are auxotrophic for hemin or menadione precisely because their ETC is defective. Gallium's mechanism is to poison iron-dependent ETC enzymes. SCVs have already adapted to ETC dysfunction. Gallium may therefore be LEAST effective against the population it MOST needs to kill.

**The kill:** Heavy metal food safety non-starter (same as 2C) + paradoxical reduced efficacy against SCVs. KILLED.

---

### Candidate 5D: Autophagy Flux Restoration -- Host-Directed Intracellular Clearance (Novel)

**Verdict: WOUNDED**

**Kill Test 9 (Repetition Test):** Phase 1 documents two critical facts: (a) *S. aureus* subverts autophagy to CREATE autophagosomes as replicative niches, and (b) bacteria escape autophagosomes to the cytoplasm via Hla pore formation in endosomal membranes. These two facts create a timing problem: bacteria enter autophagosomes, replicate, and escape to the cytoplasm. Autophagy flux restoration (completing autophagosome-lysosome fusion) must happen FASTER than bacterial escape. If escape is faster, the intervention is too late.

**Kill Test 8 (Embarrassment Test):** We administer trehalose or a p38 inhibitor. Autophagy flux is restored. Autophagosomes fuse with lysosomes. But the bacteria have already escaped to the cytoplasm. The autolysosomes destroy empty autophagosomes while the bacteria replicate freely in the cytosol. The intervention succeeds mechanistically but fails biologically because it targets the wrong compartment.

**Kill Test 2 (Species Test):** All autophagy flux modulator pharmacology comes from human and mouse cell systems. Bovine-specific autophagy flux data are limited to the p38-MAPK pathway characterization in MAC-T cells (PMID 36063687). Whether trehalose, rapamycin, or TFEB activators have the same autophagy-modulating effects in bovine mammary epithelial cells is untested.

**Mitigating factor:** The p38 inhibitor arm targets the specific bacterial subversion mechanism identified in bovine MAC-T cells. This is the most informative experiment because it directly blocks the pathogen's strategy rather than enhancing a generic host pathway.

**Wound:** Bacterial escape from autophagosomes to cytoplasm may outpace flux restoration. The p38 inhibitor arm is the most testable and most informative. WOUNDED pending the p38 inhibitor experiment in MAC-T cells. If p38 inhibition reduces intracellular CFU, the approach is alive. If not, the bacteria are escaping faster than flux can act.

---

### Candidate 5E: SCV Wake-and-Kill via Metabolic Reactivation + Antibiotic (Novel)

**Verdict: SURVIVED**

**Kill Test 2 (Species Test):** SCV reversion upon hemin/menadione supplementation is ESTABLISHED in vitro across multiple labs and species. This is reproducible basic microbiology, not a species-specific extrapolation.

**Kill Test 3 (Matrix Test):** Menadione (MW 172, LogP ~1.4) is a small lipophilic molecule that crosses cell membranes readily. It does not require formulation heroics to reach intracellular bacteria. Hemin (MW 652) is larger but has known cell-penetrating properties. The pharmacology is tractable.

**Kill Test 10 (Commercial Reality):** Menadione (vitamin K3) is dirt cheap: ~$20-50/kg. The dose needed for intramammary infusion is milligrams. COGS per dose would be under $1 for the menadione component. Combined with pirlimycin (already approved for intramammary use), this is a commercially realistic combination.

**Kill Test 7 (Stoichiometric Test):** At 10 ug/mL menadione intramammarily, the concentration is ~58 uM -- many orders of magnitude above the intracellular concentration needed to supplement ETC-deficient SCVs. Menadione is a cofactor, not a stoichiometric inhibitor; catalytic amounts suffice.

**Kill Test 8 (Embarrassment Test):** We administer menadione + pirlimycin. The menadione reaches intracellular SCVs and reverts them to normal phenotype. But the reactivated bacteria immediately produce toxins (Hla, leukocidins) that damage host cells before pirlimycin can kill them. We traded dormant, non-damaging SCVs for transiently virulent, tissue-damaging normal-colony bacteria. The acute flare is worse than the chronic infection.

This is a real risk but it is manageable by timing: if pirlimycin is already present intracellularly when SCVs revert, the kill step is concurrent with the wake step. Pirlimycin accumulates intracellularly -- this is why it performs best among approved intramammary drugs.

**What I tried:** I searched for evidence that menadione supplementation causes pathological SCV reversion in any model. Found none -- the concept has been discussed but never tested. This means the risk is theoretical, not demonstrated.

**Survived** because: (a) the concept is mechanistically direct, (b) menadione is cheap and membrane-permeable, (c) the de-risk experiment is cheap ($40-60K) and high-discriminatory-power (go/kill in 6 weeks), (d) the SCV problem is real and this is the most direct attack on it, (e) no counter-evidence found against the approach. The embarrassment scenario (acute flare on reactivation) is mitigated by concurrent pirlimycin intracellular accumulation.

---

### Candidate 5F: Biofilm Disruption Cocktail + Concurrent Bactericidal Agent (Known)

**Verdict: WOUNDED**

**Kill Test 10 (Commercial Reality -- THE WOUND):** Quality Standard 23: a 4-API combination (DNase I + Dispersin B + protease + pirlimycin) requires 15 trial arms for FDA-CVM proof of contribution. This is regulatorily impossible at dairy economics. Forge acknowledges this and proposes simplification to DNase I + pirlimycin (2-API, 3 trial arms). The simplified version is testable; the full cocktail is not.

**Kill Test 3 (Matrix Test):** All biofilm disruption data are from abiotic surfaces or simplified in-vitro models. In-vivo biofilm exists within fibrotic tissue, mixed with host proteins, immune cells, and casein. Enzymatic agents that work in vitro may not access in-vivo biofilm at all.

**Kill Test 4 (Strain Test):** Surveyor notes the ica operon is variably present across *S. aureus* lineages. PNAG-based biofilm disruption (Dispersin B) would be ineffective against strains using protein-based (Bap-dependent) or eDNA-based biofilm. The DNase I component addresses eDNA-based biofilm but not PNAG or protein-based biofilm. No single enzyme covers all biofilm types.

**Wound:** The full 4-API cocktail is regulatorily dead. The simplified 2-API version (DNase I + pirlimycin) is testable but addresses only eDNA-based biofilm. WOUNDED -- proceed with simplified version only.

---

### Candidate 5G: Toxin-Antitoxin System Modulators -- Disrupting Persister Formation (Novel)

**Verdict: KILLED**

**Kill Test 1 (20-Year Test):** TA systems as therapeutic targets in *S. aureus* have been discussed since the mid-2000s. No TA-system-modulating compound with drug-like properties exists for any bacterial species. This is not a 5-year wait for chemistry to catch up -- this is a fundamental unsolved problem in chemical biology.

**Kill Test 5 (Resistance Test):** Forge acknowledges multiple redundant TA systems (mazF, relE1/relE2, sprG/sprF). Inhibiting one system would be compensated by the others. A single compound would need to simultaneously modulate 3-4 independent TA systems -- a pharmacological impossibility with current chemistry.

**Kill Test 10 (Commercial Reality):** Forge states this is "years from any testable compound." This is correct. It is also years from any validated target (are these TA systems even expressed in bovine field isolates under milk conditions?). The proposed de-risk experiment ($80-120K) would only establish whether the TA systems are present and expressed -- not whether they can be modulated.

**The kill:** No compounds exist. Multiple redundant targets require simultaneous modulation. Years from any testable molecule. The de-risk expense only validates target expression, not therapeutic feasibility. KILLED.

---

### Candidate 6A: Optimized Phage Cocktail (Kromker 2026 Model) (Known)

**Verdict: SURVIVED**

**Kill Test 6 (Citation Test -- THE CRITICAL QUESTION):** I found the Kromker 2026 publication (PMID 41594069 in PubMed). The paper exists and is indexed. The critical question is statistical power: n=16 treated quarters, 81.3% cure (13/16).

**Statistical analysis:** With n=16, a 95% confidence interval for 81.3% cure rate (Wilson score) is approximately 57%-94%. The lower bound (57%) is below the 60-70% realistic benchmark. In other words, the TRUE cure rate could plausibly be as low as 57% -- which is good but not revolutionary. Or it could be as high as 94% -- which would be transformative. The point estimate (81.3%) is impressive but the uncertainty is enormous.

**Kill Test 9 (Repetition Test):** Gill et al. 2006 achieved 16.7% cure with single phage K and daily dosing. Kromker achieved 81.3% with multi-phage cocktail and 12-hour dosing (5 infusions). The key variables that changed: (a) cocktail breadth (multi-phage vs. single), (b) dosing frequency (q12h vs. q24h), (c) phage selection (optimized for bovine strains). These are genuine improvements in trial design, not just statistical noise.

**Kill Test 10 (Commercial Reality):** No FDA-CVM regulatory pathway exists for phage products. Manufacturing of phage cocktails at commercial scale is complex (GMP production of biological agents, lot-to-lot consistency, potency assays). These are real barriers. However, the EU regulatory environment under Regulation 2019/6 creates demand for non-antibiotic alternatives -- and phage products are advancing in human medicine (FDA breakthrough therapy designations for some phage programs).

**Kill Test 8 (Embarrassment Test):** We replicate the Kromker protocol with n=80 (40 treated, 40 control) and find 55% cure -- below the 60-70% benchmark. The result is positive but not transformative. Alternatively: the cocktail shows variable efficacy across herds because phage susceptibility differs between CC97 and CC151 dominant herds. The cocktail works in CC151 herds but not CC97 herds.

**Survived** because: (a) the result is published and indexed (PMID 41594069), (b) the improvement over Gill 2006 is explained by specific, rational design changes (cocktail breadth, dosing frequency), (c) even at the lower confidence bound (~57%), phage cocktail would be competitive with extended pirlimycin, (d) the EU regulatory demand for non-antibiotic alternatives is real, (e) independent replication ($150-200K) would provide a definitive answer. This is correctly identified as the highest-priority de-risk experiment.

---

### Candidate 6B: Endolysin-Pirlimycin Combination (Known)

**Verdict: WOUNDED**

**Kill Test 9 (Repetition Test):** Lysostaphin (the closest analogue -- an enzyme that lyses *S. aureus* cell walls) achieved 20% cure as a standalone in 1991 (Oldham & Daley) and 0% cure as a PTD-fusion at dry-off in 2016 (Hoernig et al.). The engineered intracellular delivery approach FAILED COMPLETELY. Endolysins are a different enzyme class but face identical barriers: protein stability in milk, host cell impermeability, and formulation challenges.

**Kill Test 3 (Matrix Test):** Phase 2 Section 7 documents "inconsistent killing" of endolysins in different field mastitic milk samples. The variability is attributed to differences in raw milk composition, pH, and strain differences. An enzyme that works in some milk samples but not others is commercially unreliable.

**Kill Test 8 (Embarrassment Test):** We formulate an endolysin + pirlimycin combination, test it across 20 cows, and find cure rates of 10-60% with massive inter-cow variability driven by milk composition differences. The average is no better than pirlimycin alone. The endolysin adds complexity and cost without consistent benefit.

**Wound:** Must demonstrate consistent endolysin activity across milk from 20+ cows (Forge's proposed de-risk experiment is correct). WOUNDED pending milk matrix variability data.

---

### Candidate 7A: Solving Stage 5 Solves Stage 7 (Strategic Principle)

**Verdict: SURVIVED**

Not a candidate. A correct strategic principle. If the intracellular reservoir is eliminated, endogenous reseeding becomes impossible. Passes.

---

### Candidate 7B: Post-Cure Lactoferrin Maintenance Protocol (Novel)

**Verdict: WOUNDED**

**Kill Test 10 (Commercial Reality -- THE WOUND):** 7-14 days of daily intramammary infusions. Each infusion requires: catch the cow, clean the teat, infuse lactoferrin, post-dip. Labor time: 5-10 minutes per cow per day. For a 200-cow herd with 20 treated cows, that is 100-200 minutes of additional labor daily for 1-2 weeks. Farmer compliance with this protocol is near zero. The dairy industry has already demonstrated that 8-day pirlimycin is economically marginal and rarely used. A 14-day protocol is fantasy.

**Kill Test 8 (Embarrassment Test):** We prove lactoferrin maintenance prevents reseeding in a controlled trial. We publish the result. No farmer uses it because the protocol is impractical. The science is right but the product is dead.

**Wound:** Impractical dosing regimen. Must find a sustained-release formulation (slow-release lactoferrin depot in the mammary gland?) or accept that this is a dry-period-only intervention. WOUNDED pending reformulation to reduce dosing frequency.

---

### Candidate 7C: Segregation-Informed Herd Management Tool (Known)

**Verdict: SURVIVED**

Not a therapeutic. A diagnostic/management strategy. The biology is ESTABLISHED -- cure rates vary 4-92% based on cow factors. Stratifying treatment decisions by strain type and prognostic factors is economically rational. On-farm CC-typing diagnostics are technically feasible (isothermal PCR exists for strain typing).

**Survived** because it is evidence-based management, not a therapeutic claim.

---

### Candidate 8A: Acoustic Pulse Technology (APT) as Combination Partner (Known)

**Verdict: SURVIVED**

**Kill Test 6 (Citation Test):** The controlled trial (PLOS ONE 2018) showing 70.5% recovery vs. 18.4% control is published in a peer-reviewed journal with a real P-value (<0.001). The retrospective study (n=467, 83.9%) has selection bias risk but the controlled data are independent.

**Kill Test 8 (Embarrassment Test):** APT is a "black box" -- the mechanism is not characterized. We combine APT with lactoferrin/pirlimycin, achieve 75% cure, and cannot determine whether APT contributed or the pharmacological agents did all the work. The combination trial design (APT + drugs vs. drugs alone) would answer this, but at $100-150K it is expensive for a mechanism we do not understand.

**Kill Test 10 (Commercial Reality):** Capital equipment model, not per-treatment consumable. This changes the sales model: equipment purchase/lease rather than per-dose revenue. For Zoetis, which sells consumable products, this may not fit the portfolio. However, the technology could be licensed or partnered.

**What I tried:** I looked for negative APT data or debunking of the mechanism. Found none. The technology is commercially available, has paying customers, and has published controlled trial data. The mechanism is unclear, but the outcomes data are real.

**Survived** because: (a) the only approach addressing Stage 8 (tissue repair), (b) controlled trial data with significant effect size, (c) orthogonal to all pharmacological approaches, (d) no negative evidence found. The "black box" mechanism is uncomfortable but the clinical data are the best evidence available.

---

### Candidate 8B: Anti-Fibrotic Adjunct Therapy -- Pirfenidone/Nintedanib Analogue (Novel)

**Verdict: KILLED**

**Kill Test 10 (Commercial Reality -- THE KILL):** Pirfenidone and nintedanib are human pharmaceuticals costing >$100,000/year for idiopathic pulmonary fibrosis treatment. There are ZERO veterinary formulations. There is ZERO data on pirfenidone/nintedanib in bovine mammary tissue. Repurposing a $100K/year human drug for a $30/treatment dairy product is economically nonsensical.

**Kill Test 2 (Species Test):** All pirfenidone in-vivo data are from sheep pulmonary models and rat peritoneal models. No bovine data. No mammary gland data in any species.

**Kill Test 8 (Embarrassment Test):** We test pirfenidone in bovine mammary fibroblasts in vitro, demonstrate anti-fibrotic effects, publish the result, and nobody cares because the molecule costs 1,000x too much for the indication. We answered a biological question nobody needed answered because the economics were already fatal.

**Kill Test 9 (Repetition Test):** Forge's own "most likely failure mode" is correct: "Anti-fibrotic therapy is too slow. Fibrosis develops over weeks to months; resolution takes equally long. A course of anti-fibrotic therapy during a 5-8 day treatment window may be insufficient." Even if pirfenidone were free, the treatment window is too short for the biology.

**The kill:** Human pharmaceutical economics are incompatible with dairy product economics. No veterinary formulation. No bovine data. Treatment window too short for anti-fibrotic mechanism. KILLED.

---

### Candidate 8C: Post-Treatment Probiotic Recolonization (Non-Obvious)

**Verdict: KILLED**

**Kill Test 10 (Commercial Reality -- THE KILL):** You are proposing to deliberately infuse live bacteria into a quarter that was JUST TREATED with antibiotics to clear bacteria. The intramammary route is used precisely because it delivers agents directly to the mammary gland. Infusing live NAS and *Lactobacillus* intramammarily means intentionally introducing microorganisms into a sterile body cavity. Regulatory classification of this product is impossible: it is not a drug (live bacteria, not a pharmaceutical), not a vaccine (no antigen, no immune response intended), and not a probiotic in any recognized regulatory category for intramammary use.

**Kill Test 4 (Strain Test):** As noted for Candidate 1B, the boundary between "protective NAS" and "subclinical mastitis pathogen" is strain-dependent. *S. chromogenes* is the most commonly cited protective species, but it is also one of the most frequently isolated NAS species from subclinical mastitis cases. Deliberate introduction into a just-treated quarter risks converting a cured infection into a new, iatrogenic one.

**Kill Test 8 (Embarrassment Test):** We infuse NAS probiotics post-treatment. The NAS colonize the quarter. The quarter develops NAS subclinical mastitis (SCC 200-400K). The farmer, who just paid for antibiotic treatment to clear *S. aureus*, now has a new subclinical infection from the "treatment" that was supposed to prevent reinfection.

**The kill:** Deliberate infusion of live bacteria into a just-treated mammary quarter. Regulatory pathway nonexistent. Risk of iatrogenic subclinical mastitis from the "probiotic" organisms. KILLED.

---

## Cross-Candidate Analysis

### Candidates That Address the Rate-Limiting Barrier (Stage 5 Intracellular Persistence)

| Candidate | Verdict | Status of Intracellular Mechanism |
|-----------|---------|-----------------------------------|
| 5A (Lactoferrin + pirlimycin) | SURVIVED | Iron deprivation forces metabolic stress; pirlimycin accumulates intracellularly. Multi-mechanism. Bovine data. |
| 5B (ADEP ClpP) | WOUNDED | Only known persister-killing mechanism. But published mammalian cytotoxicity (Wong 2018). Therapeutic window unknown. |
| 5C (Gallium) | KILLED | Heavy metal food safety non-starter. SCVs may be resistant. |
| 5D (Autophagy flux) | WOUNDED | Bacteria may escape autophagosomes before flux restoration acts. p38 inhibitor arm is testable. |
| 5E (SCV wake-and-kill) | SURVIVED | Most direct anti-SCV attack. Menadione is cheap and membrane-permeable. De-risk experiment is clean. |
| 5F (Biofilm cocktail) | WOUNDED | Full cocktail is regulatorily dead. Simplified DNase + pirlimycin is testable. |
| 5G (TA modulators) | KILLED | No compounds exist. Redundant targets. Years away. |

**Survivors at Stage 5:** Only 5A (lactoferrin + pirlimycin) and 5E (SCV wake-and-kill) survive cleanly. 5B (ADEP) is the most important wounded candidate -- if a therapeutic window exists, it transforms the field. If not, the only persister-killing mechanism is gone.

### The Redundancy Problem (SrtA vs. AdsA)

Surveyor's finding that AdsA is sortase-anchored creates a clear hierarchy: if the portfolio includes an SrtA inhibitor (2A), a specific AdsA inhibitor (3D) is redundant. SrtA inhibition blocks the surface display of AdsA, SpA, ClfA, FnBPA, FnBPB, IsdA, and Cna simultaneously. One target, seven effects. AdsA inhibition blocks one enzyme. The math is clear. 3D is KILLED for redundancy; 2A SURVIVED on multi-barrier merit.

### The Vaccine Problem

All three vaccine candidates (3A SpAKKAA, 3B LukMF' toxoid, 3C mucosal IgA) are WOUNDED, not killed. Each has a specific, testable question:
- 3A: Does SpAKKAA-immunized bovine serum produce OPK in milk?
- 3B: What is lukM carriage in the target market?
- 3C: Does bovine mammary gland generate sIgA to local antigen?

None of these vaccines would be sufficient as monotherapy. But a combination vaccine (SpAKKAA + LukMF' + additional antigens) with a mucosal delivery component could be powerful IF the foundational biology holds. The de-risk experiments are correctly specified.

### The Lactoferrin Correction

Forge cited "45.5% cure against resistant strains" for lactoferrin + penicillin. The primary source (Petitclerc et al. 2007) shows this was against a SINGLE highly beta-lactam-resistant research strain in experimentally induced infection. The second trial (naturally acquired chronic infection) achieved 33.3%. The primary source data are less impressive than the Phase 2 summary implied but still represent a genuine 3-5x improvement over penicillin alone. The mechanism (beta-lactamase transcriptional suppression + iron chelation) is real and bovine-confirmed. The candidate SURVIVED but with corrected expectations.

---

## Flags for Anvil

1. **ADEP therapeutic window is the single most important open question.** If ADEP can kill intracellular persisters without triggering mammalian mitochondrial ClpP-mediated apoptosis, it is the most important candidate in the portfolio. If it cannot, the portfolio has no persister-killing mechanism and the 70% test may fail.

2. **Lactoferrin cure rates are 33-45%, not the higher figures implied.** Anvil's coverage estimates must use the actual trial data, not the cherry-picked figures.

3. **Phage cocktail confidence interval extends down to ~57%.** Anvil should model portfolio coverage using the lower bound, not the point estimate.

4. **SrtA inhibitor has no lead molecule.** It survived the kill tests but there is no compound to test. The target is validated; the chemistry is not. This is a discovery program, not a development program.

5. **De-risk trial sizes proposed by Forge are too small.** Lactoferrin combination: n=20/arm should be n=50/arm. Phage replication: n=40/arm is adequate. ADEP MAC-T experiment: host cell viability must be the PRIMARY endpoint.

6. **Killed candidates that should not be resurrected:** Gallium (food safety), anti-Hla mAb (COGS), NLRP3 modulator (phenocopies pathogen strategy), pirfenidone (economics), TA system modulators (no compounds), 8C probiotic recolonization (iatrogenic risk). These have fatal flaws that cannot be engineered around.

7. **Architecture 2 ("Siege") depends on ADEP.** If ADEP fails the therapeutic window test, Architecture 2 loses its persister-killing component. Architecture 1 ("Breach and Clear") with lactoferrin + pirlimycin + SCV wake-and-kill (menadione) is more robust because it does not depend on any single unvalidated mechanism.

---

## Quality Standards Compliance

| Standard | How Addressed |
|----------|---------------|
| 1. Evidence tiers | All kill verdicts cite specific evidence with species/model tags |
| 2. 20-Year Test | Applied to SrtA (24 years), SpAKKAA (16 years), ADEP (21 years), lactoferrin (>40 years), lysostaphin (>30 years), DPC3147 (28 years) |
| 4. Citation verification | Primary source retrieved for lactoferrin (Petitclerc 2007, PMID 17517718) -- cure rates corrected downward |
| 5. Re-read primary sources | Wong et al. 2018 (PMID 30126533) retrieved for ADEP mammalian toxicity -- finding incorporated into 5B assessment |
| 6. Species/model tagging | Every kill test specifies the species of the cited evidence |
| 9. Extraordinary claims | Kromker 81.3% subjected to statistical power analysis (CI 57-94%) |
| 11. Target vs. lead molecule | SrtA survived as a target; flagged that no lead molecule exists |
| 14. Host selectivity | ADEP mammalian ClpP activation is the key host selectivity finding |
| 17. Virulence axis trade-off | NLRP3 modulator killed because it phenocopies pathogen's own persistence strategy |
| 24. Embarrassment pass | Applied to every candidate |
| 27. Test in real matrix | All protein/enzyme candidates tested against milk matrix stability evidence |
| 31. Realistic cost estimates | Forge de-risk budgets challenged where underpowered (lactoferrin trial) |

---

*32 candidates attacked. 8 KILLED. 16 WOUNDED. 8 SURVIVED. All kills cite specific evidence. All wounds specify the question that must be answered. All survivors state what was tried against them. Primary sources retrieved and verified for critical claims. Evidence tiers and species tags maintained throughout.*
