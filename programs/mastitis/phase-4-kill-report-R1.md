# Phase 4: Kill Report -- Revision 1 (Gap-Fill Candidates)

**Program:** Mastitis | **Partner:** Zoetis
**Agent:** Reaper | **Date:** 2026-03-26 | **Revision:** R1
**Primary pathogen:** *Staphylococcus aureus*
**Inputs:** Phase 3 Candidates R1 (6 new candidates + 4 combination architectures), Phase 3b Survey Report R1, Phase 1 Disease Map R1, Phase 2 Failure Analysis R1, Phase 4 Kill Report R0
**Scope:** Only the 6 new R1 candidates and 4 combination architectures. The original 32 candidates were assessed in R0 and are not re-attacked here.

---

## Executive Summary

6 new candidates entered. 1 KILLED. 4 WOUNDED. 1 SURVIVED.
4 combination architectures entered. 1 KILLED. 3 WOUNDED. 0 SURVIVED.

The R1 round is weaker than R0. It has to be -- these candidates exist because R0 left a gaping hole at SCV dormancy that nothing in the original 32 could fill. Forge went hunting in thinner evidence territory and it shows. The single standout is **R1-1 (ZG-series ClpP activators)**, which survives on the strength of genuine structural biology, co-crystal structures, and a credible selectivity mechanism -- but it has never touched an SCV, never touched a cow, and never touched milk. Everything else ranges from "might work if the universe cooperates" to "dead on arrival."

The most damaging finding: **R1-3 (apo-lactoferrin for SCV killing)** is built on a hypothesis that is contradicted by the published literature. Batko et al. 2021 (*J Bacteriol*, PMID 34606375, [DOI](https://doi.org/10.1128/JB.00458-21)) demonstrated that hemB SCV mutants are *already defective* at siderophore-mediated iron acquisition and rely on heme, not free iron, as their primary iron source. Lactoferrin chelates free iron. It does not chelate heme. The entire "iron-starve-the-SCV" premise collapses when you read the actual SCV iron metabolism literature.

The combination architectures are where the real damage is. Architecture 4 ("Full Spectrum") claims 71.6% coverage -- barely passing the 70% test. But this number is built on at least four layers of optimism: (1) it requires *every* wounded candidate to rehabilitate, (2) it requires *every* new R1 candidate to pass de-risk, (3) it double-counts lactoferrin's contribution across multiple barriers, and (4) it treats management protocols (0B, 7C) as equivalent to therapeutic products. Honest math puts the achievable coverage at 55-62%, well below 70%.

**R1-4 (SPMs)** arrived with 40% of its evidence base fabricated (2 of 5 citations are fake PMIDs) and has no veterinary precedent, no commercial-scale synthesis route, and a half-life measured in minutes. **R1-2 (Oritavancin)** would be the strongest SCV-killing candidate if it were not a Critically Important Antimicrobial protected by patents until 2029-2035 with zero bovine data. **R1-6 (Pirfenidone)** correctly rebuts the R0 cost kill but has zero evidence that 5-8 days of anti-fibrotic therapy does anything meaningful in any tissue.

---

## Verdict Summary

| # | Candidate | Category | Verdict | Fatal/Critical Issue |
|---|-----------|----------|---------|---------------------|
| R1-1 | ZG-series ClpP activators | Non-Obvious | **SURVIVED** | No SCV-specific data; no bovine data; no milk matrix data. But structural biology and selectivity mechanism are genuine. |
| R1-2 | Oritavancin | Non-Obvious | **WOUNDED** | Patent-protected until 2029-2035; Critically Important Antimicrobial; zero bovine data; EU market impossible |
| R1-3 | Apo-lactoferrin dry period | Non-Obvious | **KILLED** | SCV iron metabolism contradicts premise: hemB SCVs are siderophore-defective and rely on heme, not free iron |
| R1-4 | SPM adjunct | Non-Obvious | **WOUNDED** | 40% citation fabrication rate; minutes-scale half-life; no commercial synthesis route; no veterinary SPM product exists |
| R1-5 | Antimicrobial keratin ITS | Non-Obvious | **WOUNDED** | Incremental at best (5-15% improvement); no evidence this is meaningfully different from existing ITS |
| R1-6 | Pirfenidone | Known | **WOUNDED** | Zero evidence for short-course anti-fibrotic benefit in any tissue; every clinical study requires weeks to months |
| Arch 1 | "Breach and Clear" | Combination | **WOUNDED** | Depends entirely on R1-1 (unproven); $37-85/treatment may exceed cull economics for moderate-value cows |
| Arch 2 | "Shield and Spear" | Combination | **WOUNDED** | Mucosal IgA vaccination is the foundational assumption and is completely untested in bovine mammary gland |
| Arch 3 | "Siege" | Combination | **KILLED** | Contains NLRP3 activator (killed in R0) + ZG-series (unproven) = two unknowns; 26.5% coverage is useless |
| Arch 4 | "Full Spectrum" | Combination | **WOUNDED** | 71.6% is inflated; honest math is 55-62%; requires every conditional to pass simultaneously |

**Totals: 2 KILLED | 7 WOUNDED | 1 SURVIVED**

---

## Detailed Kill Assessments -- Individual Candidates

---

### Candidate R1-1: ZG-Series Selective ClpP Activators (Non-Obvious)

**Verdict: SURVIVED**

This is the strongest candidate in R1, and it survives because I cannot find published evidence that kills it. But make no mistake: it survives on the strength of structural biology and selectivity data, not on any demonstration of SCV killing, bovine efficacy, or milk stability. It is the best candidate for the worst-characterized gap.

**Kill Test 1 (20-Year Test):** ClpP as a drug target: published since Brotz-Oesterhelt et al. 2005, >20 years. ADEP-based activators: studied since ~2005, no product. The ZG-series scaffold: first published 2022 (Wei et al., *Nature Communications*, PMID 36376309, [DOI](https://doi.org/10.1038/s41467-022-34753-0)). The defense that ZG is a 4-year-old scaffold for a 20-year-old target is legitimate. The target has been validated by multiple groups; the failure was in the scaffold (ADEP's mammalian toxicity), not the target. ZG solves the scaffold problem. **PASS -- but the clock is ticking.** If no one has a clinical candidate from the ZG scaffold by 2030, the same 20-year question will apply to it.

**Kill Test 2 (Species Test):** All in vivo data are from zebrafish (Wei et al. 2022), *Galleria mellonella* larvae, murine skin infection, and murine thigh infection (Zhang et al. 2024, *Cell Reports Medicine*, PMID 39615486, [DOI](https://doi.org/10.1016/j.xcrm.2024.101837)). Zhang et al. 2025 (*J Med Chem*, PMID 39760203, [DOI](https://doi.org/10.1021/acs.jmedchem.4c02562)) added murine peritonitis. **Zero bovine data of any kind.** Zero intramammary data. The species gap is total, but this is expected for a novel scaffold at this stage. What matters: Surveyor confirmed that bovine mitochondrial ClpP retains all three selectivity barriers (W142, reversed H/Y, C-terminal lid). The computational prediction is strong but requires experimental confirmation.

**Kill Test 3 (Matrix Test):** ZG compounds have never been tested in milk. Based on molecular weight (estimated 300-500 Da) and the fact that they are small molecules (not proteins/peptides), milk matrix interference should be less severe than for lysostaphin, endolysins, or phage. Casein binding is a risk for any compound with aromatic/hydrophobic character, which ZG compounds almost certainly have given their binding to a hydrophobic cleft. Unquantified risk, not a kill.

**Kill Test 4 (Strain Test):** Surveyor data: ClpP is 99.5-100% conserved across 100 *S. aureus* BLASTP hits, including bovine lineages CC97, CC151, CC479. This is among the most conserved targets in the entire portfolio. **PASS.** Strain coverage is not a concern for this target.

**Kill Test 5 (Resistance Test):** This is the most interesting test. ClpP is non-essential for *S. aureus* growth under standard conditions, which means ClpP-null mutants can survive. Mellergaard et al. 2023 (*mBio*, PMID 37796131, [DOI](https://doi.org/10.1128/mbio.01349-23)) demonstrated that clinical *S. aureus* isolates with ClpP mutations exist and use them for immune evasion (PD-1 interaction). This means resistance is biologically accessible -- *S. aureus* can mutate ClpP and survive. The fitness cost is real (impaired stress response, reduced virulence), but in the intramammary environment where persistence matters more than virulence, a ClpP-mutant that survives ZG treatment could have a selective advantage. This is a WOUND, not a kill: resistance is theoretically possible but costly, and ZG compounds could be combined with conventional antibiotics to prevent resistant mutant selection. Monotherapy resistance risk is moderate.

**Kill Test 6 (Citation Test):** Wei et al. 2022 (PMID 36376309): VERIFIED. Zhang et al. 2024 (PMID 39615486): VERIFIED. Zhang et al. 2025 (PMID 39760203): VERIFIED. All from the same research group (Yang CG lab, Shanghai Institute of Materia Medica). Single-group dependency is a concern -- no independent replication by other labs. But the co-crystal structures (PDB 9IRP) are deposited and verifiable. **PASS with flag:** single-lab dependency.

**Kill Test 7 (Stoichiometric Test):** N/A -- this is a small-molecule activator, not an intracellular signaling molecule. At uM concentrations achievable by intramammary infusion, the molecule count per bacterial cell would be in the millions. Not a concern.

**Kill Test 8 (Embarrassment Test):** The simplest plausible failure: ZG297 at effective bactericidal concentrations (say 10-50 uM) causes unexpected toxicity to bovine mammary epithelial cells. The computational selectivity prediction is strong (all 3 mechanisms conserved), but computational predictions of protein-ligand interaction are not guarantees. If ZG297 has off-target activity against any bovine protease or if bovine ClpP has a conformational state not captured by sequence alignment that allows ZG binding, the entire premise collapses. This is exactly what the MAC-T viability assay will test.

**Kill Test 9 (Repetition Test):** This is NOT a resurrection of killed candidate 5B. ADEP was killed for activating mammalian mitochondrial ClpP (Wong et al. 2018). ZG compounds use a structurally distinct binding mode that exploits the W146 selectivity determinant absent in ADEP's mechanism. The kill rationale for 5B explicitly does not apply. **PASS.**

**Kill Test 10 (Commercial Reality Test):** Small molecule, synthetic, estimated $10-30/dose at scale. Intramammary route. No regulatory precedent for a ClpP activator in any species, but the FDA-CVM pathway for novel small-molecule antimicrobials is established. Withdrawal period would need determination. Commercially viable if efficacy is demonstrated. **PASS.**

**Kill Test 11 (Surveyor Test):** Surveyor CONFIRMED all three bovine ClpP selectivity mechanisms. This is the strongest computational result in R1. Conservation data: 99.5-100% across field isolates. Co-crystal structures available. **PASS.**

**The critical gap I cannot fill from published literature:** No one has tested ZG-series compounds against SCV populations. The Forge brief cites Conlon et al. 2013 (*Nature*) for the concept that ClpP activation kills persisters, but that paper used ADEP4, not ZG compounds. ADEP4 kills persisters by activating ClpP, and ZG compounds activate ClpP by a different binding mode. The mechanistic inference (ZG activates SaClpP -> uncontrolled proteolysis -> persister death) is sound in principle, but the actual demonstration against hemB/menB SCV mutants with ZG-series compounds does not exist in the published literature. This is the single most important experiment in the entire R1 de-risk sequence.

**Summary:** ZG-series survives because the structural biology is real, the selectivity mechanism is computationally confirmed for cattle, the target is universally conserved, and I cannot find published evidence that kills it. But it has never been tested against an SCV, in a cow, or in milk. It survives on potential, not on data.

---

### Candidate R1-2: Oritavancin-Class Lipoglycopeptide (Non-Obvious)

**Verdict: WOUNDED**

Oritavancin has the best published SCV-killing data of any candidate in R1. Garcia et al. 2012 (PMID 22564838, [DOI](https://doi.org/10.1128/AAC.00285-12)): >3-log CFU reduction against intracellular hemB and menD SCV mutants in THP-1 monocytes. Nguyen et al. 2009 (PMID 19188397, [DOI](https://doi.org/10.1128/AAC.01146-08)): synergy with rifampin against intracellular SCVs. This is published, peer-reviewed, species-tagged (human THP-1) SCV-killing data. No other R1 candidate has this.

But the wounds are deep and may be fatal.

**Kill Test 1 (20-Year Test):** Oritavancin was FDA-approved for human ABSSSI in 2014. It has been available for 12 years and never been tested in veterinary medicine. Not because it does not work, but because nobody looked -- the human market was more lucrative. The 20-year absence is commercial, not biological. **PASS with explanation.**

**Kill Test 2 (Species Test):** All SCV-killing data are from human THP-1 monocytes infected with lab-constructed hemB/menD mutants of COL MRSA. Zero bovine data. Zero bovine MAC-T data. Zero data against bovine *S. aureus* lineages CC97/CC151/CC479. The THP-1 monocyte model uses human cells with human phagocytic machinery -- bovine macrophages may handle oritavancin differently (different lysosomal pH, different accumulation kinetics). The species gap is complete.

**Kill Test 3 (Matrix Test):** Oritavancin is a large molecule (MW 1793 Da) with a lipophilic 4'-chlorobiphenyl side chain. In bovine whole milk, casein binding is almost certain. No published MIC data for oritavancin in milk exist. For comparison: vancomycin (MW 1449 Da, structurally related) shows reduced activity in serum due to protein binding (~55%). Oritavancin's protein binding in human serum is approximately 85%. In whole bovine milk (3.2% casein = 32 g/L protein), protein binding could push effective MIC to 5-10x broth values. If broth MIC is 0.06-0.25 ug/mL (typical for *S. aureus*), milk MIC might be 0.3-2.5 ug/mL. Achievable by intramammary infusion at mg doses? Probably, but untested.

**Kill Test 4 (Strain Test):** Oritavancin targets cell wall synthesis and membrane integrity -- universal bacterial features. MIC against bovine lineages is unpublished but expected to be comparable to human isolates given the target mechanism. Low concern.

**Kill Test 5 (Resistance Test):** Oritavancin has a dual mechanism (cell wall synthesis inhibition + membrane disruption). Vancomycin resistance (VanA) confers reduced oritavancin susceptibility but not complete resistance (oritavancin retains activity against many VanA strains via membrane disruption). VanA in bovine *S. aureus* is extremely rare. Resistance risk is low. **PASS.**

**Kill Test 6 (Citation Test):** Garcia et al. 2012 (PMID 22564838): VERIFIED by Surveyor. Nguyen et al. 2009 (PMID 19188397): VERIFIED by Surveyor. **PASS.**

**Kill Test 8 (Embarrassment Test):** The simplest failure: MIC in whole bovine milk is 100x broth MIC due to casein binding, making the effective dose unachievable by intramammary infusion. This is testable for <$10K.

**Kill Test 9 (Repetition Test):** Does this repeat a known failure mode? Oritavancin is a glycopeptide, and glycopeptides have never been used in bovine mastitis. This is not a repetition of any Sapper failure -- it is a genuinely untested approach. **PASS.**

**Kill Test 10 (Commercial Reality Test):** This is where oritavancin bleeds out.

(a) **Patent status:** Forge claimed oritavancin is "off-patent in some markets." Surveyor CORRECTED this: oritavancin remains patent-protected. Orbactiv earliest generic entry: August 2029. Kimyrsa patent protection: July 2035. There is no generic oritavancin available anywhere in the world as of March 2026. Synthesizing oritavancin de novo for veterinary use is technically possible but commercially complex -- the molecule is a semi-synthetic lipoglycopeptide requiring chemical modification of a fermentation-derived glycopeptide core.

(b) **Critically Important Antimicrobial (CIA) status:** Glycopeptides are classified as "Highest Priority Critically Important Antimicrobials" by WHO. The EU banned avoparcin (a glycopeptide) from food animal use in 1997 specifically because glycopeptide use in animals drives vancomycin-resistant enterococcus (VRE) selection. EU Regulation 2019/6 explicitly restricts use of CIAs in food-producing animals. Deploying a glycopeptide intramammarily in dairy cattle -- a food-producing species -- would face regulatory opposition in the EU that borders on impossibility. The US market is more permissive, but Zoetis operates globally. A product that cannot be sold in the EU loses ~30% of the addressable market.

(c) **COGS:** Forge estimated intramammary doses in milligrams, not grams, making raw API cost manageable. But oritavancin API from current sources costs $100-300/g (not generic). At 50-200 mg per intramammary dose, API cost alone is $5-60/dose before formulation. Upper end is commercially marginal.

**Kill Test 11 (Surveyor Test):** Surveyor confirmed the SCV-killing data (Garcia et al. 2012, Nguyen et al. 2009) and corrected the patent status. No computational analysis applicable (small molecule, not a protein target).

**Wounds (3, all potentially fatal):**
1. Patent-protected until 2029-2035. No generic available. Veterinary licensing or de novo synthesis required.
2. Highest Priority CIA. EU market is functionally closed for a glycopeptide in food animals.
3. Zero bovine data -- MIC, milk matrix, intramammary PK, MAC-T intracellular killing, all unpublished.

**Any ONE of wounds 1 or 2 could be independently fatal for commercial viability.** The biology is strong -- oritavancin may be the best SCV-killing molecule that exists. But "best molecule that you cannot sell" is not a product.

---

### Candidate R1-3: Apo-Lactoferrin High-Dose Dry Period for SCV Killing (Non-Obvious)

**Verdict: KILLED**

**The kill is based on published SCV iron metabolism that directly contradicts the premise.**

The Forge brief states: "severe iron deprivation forces SCV metabolic crisis -- SCVs with defective ETC are already iron-stressed; further depletion pushes them toward either metabolic reactivation (to scavenge iron) or death."

This hypothesis assumes that iron deprivation will kill or revert SCVs. According to PubMed, Batko et al. 2021 (*J Bacteriol* 203:e00458-21, PMID 34606375, [DOI](https://doi.org/10.1128/JB.00458-21)) tested exactly this question and found the opposite:

1. **hemB SCV mutants are already defective at siderophore-mediated iron acquisition.** The hemB mutant demonstrated "limited utilization of endogenous staphyloferrin B or exogenously provided staphyloferrin A, deferoxamine mesylate, and epinephrine." Wild-type *S. aureus* can overcome iron limitation via siderophores; hemB SCVs cannot.

2. **hemB SCVs rely on heme, not free iron.** "Increased hemin availability enables hemB bacteria to utilize siderophores for growth when iron availability is restricted." The SCV's primary iron source is heme (acquired via the Isd system from hemoglobin/haptoglobin), not free iron.

3. **Lactoferrin chelates free iron (Fe3+). It does not chelate heme.** Lactoferrin has 16 Fe3+ binding sites (confirmed by Surveyor via UniProt P24627). It sequesters transferrin-type iron. Heme iron is bound in a porphyrin ring and is not accessible to lactoferrin.

4. **The SCV iron crisis already exists naturally.** hemB SCVs are already iron-stressed because they cannot efficiently use siderophores. Adding more lactoferrin to deprive them of free iron is targeting an iron acquisition pathway they are already defective in. It is like taking away someone's bicycle when they already cannot ride one.

5. **In vivo confirmation:** Batko et al. showed that deferoxamine (an iron chelator analogous to lactoferrin's function) "failed to promote hemB bacterial growth in every organ analyzed except for the kidneys" -- but this means SCVs were not killed by iron chelation either. They simply remained in their heme-dependent state, unaffected by free-iron deprivation.

**Kill Test 1 (20-Year Test):** Lactoferrin has been studied for bovine mastitis for >20 years (Petitclerc 2007 is the landmark trial). No lactoferrin product specifically targeting SCVs has been developed because the SCV-specific mechanism was never validated.

**Kill Test 2 (Species Test):** Petitclerc 2007 (PMID 17517718) provides bovine in vivo data for lactoferrin + penicillin (45.5% cure). This is real. But this cure rate is against the general *S. aureus* population, not against SCVs specifically. The SCV-targeting hypothesis is layered on top of lactoferrin's known general activity.

**Kill Test 3 (Matrix Test):** Lactoferrin IS the matrix (it is an endogenous milk protein). No matrix interference concern. **PASS.**

**Kill Test 6 (Citation Test):** Petitclerc 2007 (PMID 17517718): VERIFIED by Surveyor. The 91.7% dry-period cure rate (n=12): unverified and statistically meaningless at n=12. With 12 treated cows, the 95% confidence interval for 91.7% (11/12) is 61.5-99.8%. This could easily be 62% instead of 92%. Forge correctly flagged this as "statistically fragile" but then built a candidate around it.

**Kill Test 8 (Embarrassment Test):** We expose hemB SCV mutants to 20 mg/mL apo-lactoferrin in iron-depleted media for 72 hours. The SCVs shrug, switch to heme-dependent iron acquisition via the Isd system, and show zero viability change. The de-risk experiment fails at step one. This is the most likely outcome based on Batko et al. 2021.

**Kill Test 9 (Repetition Test):** This candidate is an extension of survived candidate 5A (lactoferrin + pirlimycin). The general lactoferrin mechanism (iron deprivation + antibiotic synergy) remains valid for non-SCV bacteria. The SPECIFIC SCV-targeting hypothesis fails, but the general candidate (5A) is not affected by this kill. The kill is narrow: it destroys the SCV-specific claim, not lactoferrin's general utility.

**Kill Evidence:** Batko et al. 2021, *J Bacteriol* 203:e00458-21 (PMID 34606375, [DOI](https://doi.org/10.1128/JB.00458-21)). hemB SCV mutants of *S. aureus* USA300 are defective for siderophore-mediated iron acquisition and rely on heme as their primary iron source. Iron chelation (the mechanism of lactoferrin) targets the wrong iron acquisition pathway. The hypothesis that extreme iron deprivation would force SCV metabolic crisis is contradicted by published data showing SCVs are already adapted to iron limitation through heme dependency.

---

### Candidate R1-4: SPM Intramammary Adjunct (Non-Obvious)

**Verdict: WOUNDED**

This candidate arrived with its credibility already compromised. Surveyor caught two fabricated citations out of five (40% fabrication rate). The remaining three verified citations support the general biology of SPMs and bovine mammary inflammation, but none of them demonstrate SPM therapeutic efficacy in bovine mastitis.

**Kill Test 1 (20-Year Test):** SPMs (resolvins, protectins, maresins) were first characterized by Serhan's group around 2002-2004. After 22+ years of research, there is no SPM product in any veterinary indication. In human medicine, SPMs have entered clinical trials only for skin inflammation and ocular disease -- neither of which involves the challenges of the bovine mammary environment (milk matrix, continuous removal by milking, bacterial infection). The absence is notable.

**Kill Test 2 (Species Test):** Sordillo 2018 (PMID 29397182, [DOI](https://doi.org/10.3168/jds.2017-13855)): bovine mammary review of oxylipids. Confirms SPM biology is relevant to bovine mastitis. But this is a REVIEW -- it does not demonstrate therapeutic SPM administration in cattle. Lutaty et al. 2018 (PMID 29643857, [DOI](https://doi.org/10.3389/fimmu.2018.00644)): lactoferrin fragments promote resolution-phase macrophage conversion. Model systems: murine peritonitis and bovine mastitis MILK SAMPLES (ex vivo observation, not therapeutic intervention). Filor et al. 2025 (PMID 40836686): PCBUS model with zymosan. This validates the experimental MODEL, not SPM therapy. **No publication demonstrates therapeutic SPM administration reducing mastitis severity or promoting resolution in any animal model.**

**Kill Test 3 (Matrix Test):** SPMs are lipid mediators with half-lives of MINUTES in vivo. In the bovine mammary gland, enzymatic degradation by 15-hydroxyprostaglandin dehydrogenase (15-PGDH) and other lipid-metabolizing enzymes would destroy unformulated SPMs within minutes of intramammary infusion. Any SPM product would require a sustained-release formulation that does not currently exist for lipid mediators in an aqueous biological environment.

**Kill Test 6 (Citation Test):** Three verified, two FABRICATED. The fabricated citations are:
- "Bannerman 2021 PMID 33881479" -- actually a JAMA COVID-19 erratum. Has nothing to do with bovine mastitis or SPMs.
- "Prunty 2019 PMID 30686737" -- actually a plant biology paper about DOF2.1 in *Arabidopsis*. Has nothing to do with animals.

A 40% fabrication rate in the evidence base is not merely an annotation error. It means Forge's AI-assisted literature search hallucinated references and nobody caught it before submission. If 40% of the citations are fake, how much confidence should we place in the remaining inferential chain? The verified citations support SPM biology in general; they do not support SPM therapy for bovine mastitis specifically.

**Kill Test 8 (Embarrassment Test):** We synthesize RvD2 at research-grade pricing ($5,000/mg), infuse it intramammarily, and it is enzymatically destroyed within 10 minutes before reaching any meaningful concentration at the tissue level. The $60-80K de-risk experiment produces a flat line.

**Kill Test 10 (Commercial Reality Test):** SPM synthesis costs are extreme. Research-grade RvD2 costs $1,000-10,000/mg. Even with commercial-scale synthesis, SPMs are structurally complex lipids requiring multi-step total synthesis or enzymatic conversion. Forge acknowledges the cost concern but waves it away with "biosynthetic production routes." No commercial biosynthetic SPM production route exists. No SPM product in any indication has been commercialized at any price point.

Additionally: no regulatory pathway exists for a lipid mediator intramammary product. The FDA-CVM has no precedent for this class. The regulatory timeline is measured in years before a submission template is even defined.

**Kill Test 11 (Surveyor Test):** Surveyor rated R1-4 as CORRECTED due to citation fabrication and noted the reduced evidence base. Surveyor cannot computationally validate a lipid mediator formulation concept.

**Wounds (5):**
1. 40% citation fabrication rate undermines the entire evidence chain.
2. SPM half-life is minutes; no sustained-release formulation exists.
3. Synthesis cost is $1,000-10,000/mg with no commercial production route.
4. Zero published data on therapeutic SPM administration in any mastitis model.
5. No regulatory precedent for lipid mediator intramammary products.

**Why not KILLED:** The underlying biology -- that resolution-phase lipid mediators promote tissue healing -- is real and well-established (Serhan's body of work spanning >20 years). The three verified citations confirm SPM relevance to bovine mammary inflammation. If someone solves the formulation, synthesis, and delivery problems, this class could work. But those are three unsolved problems stacked on top of each other, and the evidence base arrived pre-damaged by fabrication.

---

### Candidate R1-5: Antimicrobial Keratin-Enhanced Internal Teat Sealant (Non-Obvious)

**Verdict: WOUNDED**

**Kill Test 1 (20-Year Test):** Internal teat sealants have been commercially available for >20 years (Orbeseal approved 2003). The bacteriostatic activity of teat canal keratin fatty acids (C12:0 lauric acid, C14:0 myristic acid) against *S. aureus* has been known since Hibbitt et al. 1969 -- over 55 years. Nobody has combined them in a commercial product. The proposed microencapsulation technology is the only novel element.

**Kill Test 2 (Species Test):** ITS efficacy: bovine in vivo, extensively demonstrated. Keratin fatty acid bacteriostatic activity: bovine in vitro. This is entirely bovine data. **PASS.**

**Kill Test 3 (Matrix Test):** The "matrix" here is the sealant itself plus teat canal fluid. The critical question is whether microencapsulated fatty acids remain stable in the bismuth subnitrate matrix for 6-8 weeks (dry period duration), then release upon contact with teat canal moisture. No formulation data exists. Fatty acids are chemically stable but microencapsulation integrity over weeks in a biological environment is untested.

**Kill Test 8 (Embarrassment Test):** We make the prototype sealant, put it in a dry cow, and after 8 weeks the microencapsulation has degraded in the alkaline environment of involuting mammary secretion, the fatty acids have been released and metabolized long before the vulnerable pre-calving window, and the sealant provides no incremental benefit over standard Orbeseal. We have spent $30-50K on a slightly fancier version of an existing product.

**Kill Test 9 (Repetition Test):** The original 1A candidate was WOUNDED in R0 for "formulation compatibility unknown; incremental over existing ITS." This R1 version proposes microencapsulation to solve the formulation compatibility question. The repetition concern is not formulation compatibility -- it is incrementality. ITS already reduces new IMI by ~40%. If the antimicrobial keratin enhancement adds 5-15% improvement (Forge's own estimate), the absolute new IMI reduction goes from ~40% to ~45-55%. This is not transformative. At Stage 1's 7% pathology weight, the maximum contribution to the coverage map is 0.35-1.05 percentage points.

**Kill Test 10 (Commercial Reality Test):** Adding microencapsulated fatty acids to a bismuth subnitrate sealant increases manufacturing complexity and cost. The existing ITS market is mature and competitive (Orbeseal, Shutout, etc.). A slightly better ITS must compete on thin margins. The development cost ($30-50K de-risk + full regulatory dossier for a novel formulation) may not be justified for an incremental improvement at a low-weight disease stage.

**Wounds (2):**
1. Incrementality: 5-15% improvement over existing ITS translates to <1 percentage point in the coverage map.
2. No formulation prototype exists; microencapsulation stability in bismuth subnitrate matrix over 6-8 weeks is untested.

**Why not KILLED:** It is not biologically wrong. The fatty acids are bacteriostatic against *S. aureus*. The concept is plausible. It is just small. At 7% stage weight and 20% estimated coverage, this adds 1.4% to the portfolio. It is a product improvement, not a breakthrough.

---

### Candidate R1-6: Pirfenidone Intramammary at Generic API Pricing (Known)

**Verdict: WOUNDED**

Forge correctly rebutted the R0 cost kill. I acknowledge this: my R0 kill of 8B used human formulation pricing ($100K/year), not generic API pricing ($50-200/kg). At 100-500 mg intramammary doses, API cost is negligible ($0.005-0.10/dose). Surveyor confirmed: off-patent since ~2021, 21+ generic API suppliers, MW 185.22 Da, passes all Lipinski/Veber rules. **The cost kill is retracted.**

But the biology kill stands, and gets worse on closer examination.

**Kill Test 1 (20-Year Test):** Pirfenidone has been FDA-approved for human IPF since 2014 (12 years). It has been used as an anti-fibrotic for >25 years in research settings. It has NEVER been tested in any veterinary species. It has NEVER been tested in mammary gland tissue. It has NEVER been tested in any acute/short-course anti-fibrotic protocol that showed benefit within 5-8 days.

**Kill Test 2 (Species Test):** Human in vivo (IPF -- chronic, months of treatment). Ovine pulmonary models (chronic). Rat peritoneal models (chronic). In lung transplantation, pirfenidone reduced primary graft dysfunction and acute cellular rejection within 30 days -- but this is still 30 days, not 5-8 days. **Zero data in any species showing anti-fibrotic benefit within a 5-8 day treatment window.**

The fundamental biology: fibrosis involves TGF-beta-mediated fibroblast activation, collagen synthesis, cross-linking, and extracellular matrix deposition. This is a process that takes weeks to establish. Pirfenidone inhibits new collagen deposition. Even if pirfenidone completely blocked TGF-beta signaling from day 1 of intramammary treatment, the existing fibrotic tissue would remain (pirfenidone does not dissolve existing collagen). The question is whether preventing 5-8 days of new fibrosis deposition during an antimicrobial treatment course is clinically meaningful in an organ that has been fibrotic for weeks to months.

**Kill Test 3 (Matrix Test):** Pirfenidone is a small, moderately lipophilic molecule (XLogP 1.9, TPSA 20.3). It should penetrate mammary tissue well and have minimal milk matrix binding issues. **PASS.**

**Kill Test 8 (Embarrassment Test):** We infuse pirfenidone intramammarily for 8 days alongside antibiotic therapy. At the end of treatment, we measure collagen content in mammary biopsies. The pirfenidone-treated quarters show no difference from untreated controls because: (a) 8 days is too short for measurable collagen reduction, (b) the existing fibrotic scar tissue is unaffected, and (c) the small amount of new collagen that would have been deposited in 8 days is clinically insignificant compared to the months of accumulated fibrosis. The experiment is negative, and we cannot tell whether the drug reached the tissue, whether it inhibited TGF-beta, or whether it simply did not matter.

**Kill Test 9 (Repetition Test):** Forge argues this is "prevention of new fibrosis, not reversal of existing." This is a valid reframing. But Sapper's analysis established that fibrosis is a BARRIER to drug access -- meaning existing fibrosis is the problem, not future fibrosis during a treatment course. Preventing 5-8 days of new collagen deposition while leaving the existing fibrotic barrier intact does not solve the problem that fibrosis creates (drug inaccessibility to bacteria in microabscesses).

**Kill Test 10 (Commercial Reality Test):** API cost: negligible. Formulation: simple (small molecule in aqueous/oil vehicle). But: pirfenidone has no established MRL for milk. Withdrawal period determination is required. No veterinary pirfenidone precedent exists in any species for any indication. The regulatory pathway would require a full safety/efficacy dossier from scratch.

**Wounds (3):**
1. Zero evidence for short-course anti-fibrotic benefit (5-8 days) in any tissue, any species.
2. The biological mechanism (preventing new collagen deposition) does not address the clinical problem (existing fibrotic barriers to drug access).
3. No veterinary precedent; full regulatory dossier required from scratch including MRL determination.

**Why not KILLED:** The cost rebuttal is valid. The anti-inflammatory effects (TNF-alpha, IL-6 reduction within hours) are independent of the anti-fibrotic mechanism and could provide some benefit as an adjunct. The de-risk experiment (bovine fibroblast TGF-beta assay) is cheap ($40-60K) and definitive. If it works at 7 days in vitro, the hypothesis has a basis. If it does not, the candidate dies cleanly.

---

## Detailed Kill Assessments -- Combination Architectures

---

### Architecture 1: "Breach and Clear" (Cure-Side Intensive, Lactation)

**Verdict: WOUNDED**

Components: 5A (lactoferrin + pirlimycin) + 6A (phage cocktail) + R1-1 (ZG-series ClpP activator)

**Attack on coverage estimate (33.7%):**

Forge estimates 33.7% coverage for this cure-side triple. The number is internally consistent given the stage-by-stage breakdown, but it makes this architecture useless as a standalone portfolio. At 33.7%, it cannot pass the 70% test alone and requires the prevention arm (Architecture 2 or 4) to function.

**Attack on the component dependencies:**

The entire architecture depends on R1-1 (ZG-series) for SCV coverage. R1-1 has zero SCV-specific data. If the ZG MAC-T viability assay fails (bovine ClpP shows unexpected activation), the SCV component disappears and the architecture collapses to 5A + 6A = approximately 22% coverage, addressing only the non-SCV fractions of Stages 5 and 6.

**Attack on the treatment protocol framing:**

Forge proposes administering 3 separate products sequentially over 5-8 days to avoid the 15-arm combination product trial. This is clever regulatory maneuvering, but commercially problematic:

1. **Farmer compliance:** A protocol requiring 3 different intramammary products administered on different schedules over 8 days is complex. Dairy farmers already struggle with compliance on single-product extended therapy (the reason 8-day pirlimycin is not widely adopted).

2. **Multiple products = multiple purchase decisions.** Zoetis would need to market, distribute, and support 3 separate SKUs that only work together. This is not how veterinary products are sold -- practitioners prefer single-product solutions.

3. **COGS: $37-85/treatment course.** For cows with chronic *S. aureus* mastitis (SCC >500K, multiple failed treatments), cull economics become relevant. A replacement heifer costs $1,500-3,000 in the US. A treatment protocol costing $60-85 that achieves 60-70% cure is economically justified for high-genetic-merit cows but not for average cows in the bottom third of the herd. Market size shrinks.

**Wounds:**
1. Entirely dependent on R1-1 (zero SCV data) for the critical barrier.
2. 3-product sequential protocol has farmer compliance and commercial viability concerns.
3. Cannot stand alone -- requires prevention arm to reach 70%.

---

### Architecture 2: "Shield and Spear" (Prevention + Cure)

**Verdict: WOUNDED**

Components: 3C (mucosal IgA vaccine) + 3B (LukMF' toxoid) + 5A (lactoferrin + pirlimycin) + 6A (phage cocktail)

**Attack on coverage estimate (41.3%):**

The prevention arm (3C + 3B) contributes approximately 12 percentage points at Stages 2-4. This estimate depends on two wounded candidates:

1. **3C mucosal IgA vaccination** was WOUNDED in R0 for: "Bovine mammary gland is immunologically 'cold'; sIgA response to intramammary antigen undemonstrated." The foundational assumption -- that intramammary vaccination can generate functional secretory IgA in bovine milk -- has NEVER been demonstrated. Not once. Not in any cow. This is a $50-80K experiment (the IgA ovalbumin model) that has not been done. If it fails, the prevention arm loses its largest component and Stages 2-3 coverage drops from ~10% to ~4% (LukMF' alone, strain-limited to ~70% of isolates).

2. **3B LukMF' toxoid** was WOUNDED for lineage-restricted coverage: LukMF' is carried by CC151 (high), CC479 (variable), and only ~30% of CC97. In herds where CC97 predominates, the vaccine misses 70% of the target population.

**Attack on the cure side:**

The cure side (5A + 6A) covers approximately 22% -- the same as Architecture 1 without ZG-series. Without an SCV-targeting component, this architecture cannot touch the deepest persistence mechanism.

**Attack on the 41.3% total:**

41.3% is an honest number for this architecture, but it is 29 points below the 70% threshold. Even if every component works perfectly, this architecture does not pass the 70% test. It is presented as a building block, not a solution, and should be evaluated accordingly.

**Wounds:**
1. IgA vaccination foundational assumption is untested.
2. Cure side has zero SCV coverage.
3. 41.3% -- cannot pass 70% test under any scenario.

---

### Architecture 3: "Siege" (Cure-Side Maximum with Wounded Candidates)

**Verdict: KILLED**

Components: 5A (lactoferrin + pirlimycin) + R1-1 (ZG-series) + 4B (NLRP3 activator)

**The kill:** 4B (NLRP3 activator) was KILLED in R0. Forge's R1 brief labels it "WOUNDED (REVIVED)" without explaining what new evidence reverses the R0 kill. The R0 kill rationale: "*S. aureus* exploits PINK1/Parkin to suppress NLRP3; activating NLRP3 may phenocopy the pathogen's own persistence strategy." The external review corrected the DIRECTION (activate, not inhibit), but the fundamental concern remains: forcing pyroptosis in mammary epithelial cells destroys the tissue you are trying to save. Pyroptosis is inflammatory by definition -- it releases IL-1beta, damages epithelial integrity, and could worsen the fibrotic response.

Forge acknowledges this: "pyroptosis itself causes tissue damage -- net effect uncertain." When the proposer says the net effect is uncertain, the candidate is not ready for a combination architecture. It is a research question, not a component.

**Coverage math:** 26.5% -- the lowest of all four architectures. Even Forge does not pretend this reaches 70%.

**Kill evidence:** Architecture 3 combines two unknowns (R1-1: zero SCV data; 4B: killed in R0) with one survivor (5A) and achieves 26.5% coverage. This is a thought experiment, not a portfolio. One unknown component per architecture is acceptable. Two is speculation.

---

### Architecture 4: "Full Spectrum" (Maximum Coverage Protocol)

**Verdict: WOUNDED**

This is the architecture that matters. Forge claims 71.6% conditional coverage. Let me disassemble this number.

**Attack 1: The conditional stack.**

The 71.6% requires ALL of the following to be true simultaneously:
- ZG-series demonstrates selective SCV killing in bovine models (R1-1)
- SrtA inhibitor lead compound is identified (2A -- WOUNDED, 22+ years with no drug)
- NLRP3 activator confirmed as protective in bovine (4B -- KILLED in R0)
- SPM + pirfenidone provide measurable Stage 8 benefit (R1-4 WOUNDED + R1-6 WOUNDED)
- Mucosal IgA vaccination generates functional sIgA (3C -- WOUNDED, untested assumption)

Forge itself acknowledges: "If any two of the five conditionals fail, the portfolio drops below 70%." The probability that ALL FIVE pass is the product of their individual probabilities. Being generous:
- ZG-series SCV killing: 40% (strong structural biology but zero SCV data)
- SrtA inhibitor: 25% (22 years, no drug; recent chemistry is genuine but the hit rate from in vitro to in vivo is ~10-20%)
- NLRP3 activator: 10% (KILLED in R0; inclusion here contradicts the R0 verdict)
- SPM + pirfenidone Stage 8 benefit: 15% (two WOUNDED candidates with minutes-scale half-life and zero short-course anti-fibrotic data)
- Mucosal IgA in bovine: 30% (novel concept, plausible biology, but zero bovine data)

P(all five pass) = 0.40 x 0.25 x 0.10 x 0.15 x 0.30 = 0.045% -- essentially zero.

P(at least four pass) -- still below 70% threshold -- is only slightly better.

**Attack 2: Double-counting lactoferrin.**

Lactoferrin appears in the coverage math at Stage 3 (immunomodulation, 10%), Stage 5 (intracellular iron deprivation, 40%), Stage 6 (beta-lactamase suppression, 15%), and Stage 7 (indirect from Stage 5 improvement). A single molecule providing coverage at four stages is not additive -- it is the same mechanism viewed from different angles. If lactoferrin's actual effect is "45.5% cure rate in a bovine trial" (Petitclerc 2007), then its total contribution is captured by that number, not by splitting it across four stages.

**Attack 3: Management protocols inflating coverage.**

0B (Ca/BHBA management) contributes 4.0% and 7C (herd management) contributes 5.0%. Together: 9.0% of the 71.6% total. These are not Zoetis products. These are management practices that well-run dairies already implement. Including them in the coverage math inflates the product portfolio's coverage by 9 percentage points. Without management protocols: 71.6% - 9.0% = 62.6%. Below 70%.

**Attack 4: The 70% Stage 5 estimate.**

Forge estimates 70% coverage at Stage 5 (25% weight = 17.5% contribution) by combining: 5A (intracellular 40%) + 6A (biofilm 15%) + R1-1 (SCV 25%) = 70%. But these sub-barrier coverages are not additive if the barriers interact:

- Lactoferrin's 40% intracellular coverage assumes iron deprivation enhances pirlimycin's intracellular kill. The 45.5% TRIAL cure rate (Petitclerc 2007) includes whatever intracellular effect lactoferrin provides. It is not 40% of a 100% possible -- it is 40% of whatever pirlimycin can reach, which in turn depends on fibrosis (Barrier B), biofilm (Barrier C), and immune evasion (Barrier D).

- Phage's 15% biofilm coverage: the Kromker trial (81.3%, n=16) used phage WITHOUT lactoferrin or ZG-series. The cure rate INCLUDES whatever biofilm disruption the phage achieved. You cannot extract a "15% biofilm-specific contribution" and add it to a separate calculation -- the phage result is a composite outcome.

- ZG-series 25% SCV coverage: this is entirely hypothetical (zero SCV data). But even granting it: adding 25% SCV coverage on top of 40% intracellular + 15% biofilm assumes the barriers are independent. They are not. An SCV living inside a fibrotic microabscess is protected by both the SCV dormancy barrier AND the fibrosis barrier. Killing the SCV phenotype does not help if the ZG compound cannot reach the SCV through the fibrotic tissue.

**Honest estimate:** Stage 5 combined coverage is more likely 45-55% (reflecting the empirical observation that the best mono-agent cure rate for *S. aureus* chronic mastitis is ~86% for 8-day pirlimycin, meaning multi-barrier coverage at Stage 5 is capped at roughly 70% under ideal conditions -- and this is with an approved drug using extended treatment, not a 3-component experimental protocol).

**Attack 5: Combination synergies are hypothetical.**

Forge states: "lactoferrin iron deprivation + ZG ClpP activation may be synergistic against SCVs -- iron-starved bacteria may be more susceptible to proteolytic kill." This is speculation. There is no published evidence that iron deprivation enhances ClpP activator efficacy. The words "may be synergistic" are not evidence.

**Attack 6: Farmer adoption.**

Even if the science works, the "Full Spectrum" protocol requires a farmer to:
1. Manage Ca/BHBA at transition
2. Vaccinate with a combined IgA/LukMF' vaccine (2-3 doses/cow/year)
3. Apply antimicrobial ITS at dry-off
4. Upon infection: administer lactoferrin + pirlimycin (8 days)
5. Administer phage cocktail (5 doses over 2.5 days)
6. Administer ZG-series compound (6 days)
7. Administer SPM adjunct (post-treatment)
8. Administer pirfenidone (concurrent with treatment)
9. Implement diagnostic-guided segregation

This is 9 interventions from 6-8 separate products. The total per-infection cost: $85-205 (Forge's estimate). The complexity is appropriate for a referral veterinary hospital treating high-value cattle. It is not realistic for a 2,000-cow commercial dairy operating on thin margins with minimal veterinary oversight between scheduled visits.

**Revised honest coverage estimate:**

| Stage | Weight | Achievable Coverage | Contribution |
|-------|--------|-------------------|-------------|
| 0 | 8% | 30% (management, already practiced) | 2.4% |
| 1 | 7% | 10% (standard ITS, negligible R1-5 increment) | 0.7% |
| 2 | 8% | 20% (IgA conditional, 30% chance it works; SrtA conditional, 25% chance) | 1.6% |
| 3 | 15% | 25% (LukMF' strain-limited; IgA conditional) | 3.75% |
| 4 | 10% | 15% (LukMF' neutrophil preservation) | 1.5% |
| 5 | 25% | 50% (5A proven at ~45%; 6A promising at ~81% but unreplicated; R1-1 conditional) | 12.5% |
| 6 | 12% | 55% (6A AMR-orthogonal + 5A beta-lactamase suppression) | 6.6% |
| 7 | 10% | 35% (indirect from Stage 5 + management) | 3.5% |
| 8 | 5% | 10% (SPM + pirfenidone both WOUNDED, low probability) | 0.5% |
| **TOTAL** | **100%** | | **33.0% base; ~55% optimistic; ~62% best case** |

**Honest assessment: 55-62% achievable coverage under optimistic but not fantastical assumptions. Below 70%.**

**Wounds (4):**
1. 71.6% is inflated by management protocols (9%), double-counted lactoferrin contributions, and non-additive sub-barrier estimates.
2. Requires all 5 conditionals to pass simultaneously (joint probability <0.05%).
3. Farmer adoption of a 9-intervention, 6-8 product protocol is unrealistic for commercial dairy.
4. Honest achievable coverage: 55-62%, below 70%.

**Why not KILLED:** The architecture is not biologically wrong. The component selection is rational -- it addresses the right stages with the right modalities. The APPROACH (disease management protocol with separately approved products) is commercially sound and mirrors human oncology. What is wrong is the MATH. The numbers are optimistic to the point of misleading. If the ZG-series and IgA experiments both succeed (total probability ~12%), the coverage could reach 62-67%. That is close to 70% but not there. The 70% test may be mathematically impossible for *S. aureus* chronic bovine mastitis with currently available knowledge.

---

## Cross-Cutting Findings

### 1. The SCV gap remains the fatal gap.

R1-1 (ZG-series) is the only candidate with a credible mechanism for SCV killing, and it has zero SCV-specific data. R1-2 (oritavancin) has actual SCV-killing data but faces patent and CIA barriers that may be commercially fatal. R1-3 (apo-lactoferrin SCV hypothesis) is KILLED by published iron metabolism data. After R1, the SCV gap is narrowed from "zero candidates" to "one candidate with zero SCV data" (or "two candidates, one commercially impossible"). This is progress, but it is fragile progress.

### 2. The 70% test may be structurally impossible.

Forge's honest recalculation (lines 296-298 of the R1 candidates document) reaches 66.65% maximum conditional coverage -- and that is Forge's own number, not mine. My recalculation reaches 55-62%. The gap between 62% and 70% cannot be closed by adding more candidates. It can only be closed by: (a) one of the existing candidates performing better than estimated, (b) genuine synergies between combination components, or (c) lowering the bar. Option (c) requires Overwatch's decision, not mine.

### 3. Citation fabrication is a systemic risk.

Two fabricated PMIDs in R1-4 were caught by Surveyor. This is not the first time AI-assisted literature search has generated plausible but nonexistent references. The risk is not limited to R1-4 -- any candidate whose evidence base was assembled by an AI system should be verified citation by citation. Surveyor is doing this, but the R1-4 fabrication rate (40%) should trigger a full audit of all previously cited PMIDs across the portfolio.

### 4. The "treatment protocol" regulatory framing is clever but commercially untested.

Forge's proposal to market 3-4 separate products as a combined treatment protocol avoids the 15-arm combination trial matrix. This mirrors human oncology (combination chemotherapy from separately approved drugs). But veterinary medicine does not have a precedent for this model. Zoetis has never marketed a multi-product treatment protocol for mastitis. The commercial infrastructure (sales training, practitioner education, protocol compliance monitoring) does not exist and would need to be built.

---

## What Survives R1

After R0 + R1, the strongest candidates for the final portfolio are:

| # | Candidate | Verdict | Key Strength |
|---|-----------|---------|-------------|
| 5A | Lactoferrin + pirlimycin | SURVIVED (R0) | Bovine in vivo data, 45.5% cure, multi-mechanism |
| 6A | Phage cocktail | SURVIVED (R0) | 81.3% pilot RCT, AMR-orthogonal, EU-friendly |
| R1-1 | ZG-series ClpP activators | SURVIVED (R1) | Structural selectivity confirmed, universally conserved target |
| 2A | SrtA inhibitor | SURVIVED (R0) | Zero host homolog, recent covalent chemistry |
| 0B | Ca/BHBA management | SURVIVED (R0) | Biologically sound management protocol |
| 7C | Herd management | SURVIVED (R0) | Diagnostic/management strategy |

Everything else is either KILLED or WOUNDED with specific questions that must be answered before inclusion in a portfolio.

---

*This kill report assessed 6 new candidates and 4 combination architectures from Forge R1. The strongest new candidate (R1-1, ZG-series ClpP activators) survived on structural biology but has zero SCV-specific data. The most critical finding: R1-3 (apo-lactoferrin SCV hypothesis) is killed by Batko et al. 2021, which demonstrated that hemB SCVs are siderophore-defective and rely on heme, not free iron -- directly contradicting the iron-starvation premise. The 71.6% conditional coverage estimate is inflated; honest math yields 55-62%. The 70% test remains unmet and may be structurally impossible for S. aureus chronic bovine mastitis.*
