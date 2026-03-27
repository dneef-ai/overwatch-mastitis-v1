# Phase 4 -- Kill Report: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Agent:** Reaper (Red Team)
**Date:** 2026-03-27
**Status:** Complete

---

## Executive Summary

Forty-one candidates attacked. Every candidate subjected to all 12 kill tests. Twenty verdicts rendered.

**Kill count:**
- **KILLED:** 10 candidates (fatal flaws found)
- **WOUNDED:** 16 candidates (serious concerns requiring specific answers)
- **SURVIVED:** 5 candidates (withstood all attacks; proceed with caution)

The portfolio's center -- leukotoxin neutralization at Gate 2 -- withstands attack. The TARGET is correct. But the APPROACHES are far more fragile than Forge admits. The anti-LktA mAb has a fatal duration-of-protection problem that Forge handwaves. The mRNA vaccine has no precedent for bacterial antigens in cattle. Every novel small-molecule target (LktB, LktC, lktA transcription) has multiple unknowns stacked in series. The feed additives are dead on arrival -- the field already tried them and they failed.

The five survivors are: the epitope subunit vaccine (G2-3), the phage cocktail (G1-2), the anti-Factor H/FomA approach (G2-8), the blood biomarker (PG-4), and the combination concept COMBO-2 (conditionally). Everything else needs answers before it can proceed.

---

## VERDICT TABLE

| # | Candidate | Verdict | Fatal/Key Issue |
|---|-----------|---------|-----------------|
| G2-1 | Anti-LktA mAb | **WOUNDED** | Duration: 21-day half-life vs 120-400 day feeding period. Cost-prohibitive at required dosing frequency. |
| G2-2 | mRNA LktA vaccine | **WOUNDED** | Zero precedent for mRNA against bacterial antigens in cattle. Viral antigen immunogenicity may not translate. |
| G2-3 | Epitope subunit vaccine | **SURVIVED** | Straightforward iteration on Fusogard. Xiao epitope data is real. ISCOMATRIX adjuvant is proven. Risk is well-characterized. |
| G2-4 | LktB secretion inhibitor | **KILLED** | Surveyor confirms POTRA domain is a flat beta-sheet surface -- NOT druggable by small molecules. No path to a drug. |
| G2-5 | lktA transcription suppressor | **WOUNDED** | Regulatory circuitry completely unknown. Multiple stacked unknowns before a drug is possible. |
| G2-6 | LktA receptor decoy | **WOUNDED** | Receptor unknown for 24+ years. This is a research project, not a drug program. |
| G2-7 | Kupffer cell trained immunity | **WOUNDED** | LktA may kill via pore formation, not signaling. Trained immunity cannot protect against physical membrane destruction. SINGLE-LAB DEPENDENCY (Adams 2024). |
| G2-8 | Anti-Factor H (FomA) | **SURVIVED** | Dual mechanism confirmed. Neisseria vaccine precedent is real (Bexsero/Trumenba). Target is validated in a related system. |
| G2-9 | Complement enhancement (OMV) | **WOUNDED** | 342 OMV proteins = undefined antigen. Strain variability in OMV composition. Mouse-only data. |
| G2-10 | Anti-NET evasion | **KILLED** | DNase activity in F. necrophorum is INFERRED, not demonstrated. Target may not exist. |
| G1-1 | Anti-hemagglutinin vaccine | **KILLED** | Hemagglutinin gene has NEVER been cloned or sequenced (40 years). Cannot make a recombinant vaccine against an unsequenced protein. Adhesion is redundant. |
| G1-2 | Phage cocktail | **SURVIVED** | Obligately lytic phages exist (Schwarz 2024). Both subspecies susceptible. Rumen stability is testable. Honest about limitations. |
| G1-3 | Protected butyrate + zinc | **KILLED** | SCFP (n=4,689) proves Gate 1 feed additives have zero standalone abscess effect. Butyrate is a Gate 1 feed additive. "Combination component" framing does not rescue a zero-effect mechanism. |
| G1-4 | Anti-43K OMP vaccine | **WOUNDED** | Merged with G2-8 (same protein = FomA). Adhesion function may be redundant. |
| G1-5 | Hindgut-targeted suppression | **WOUNDED** | Conditional on KE#1. Correctly gated, but colonic drug delivery in cattle is undeveloped. |
| G1-6 | Tannase-resistant tannin | **KILLED** | Tannin blends alone (without monensin) showed NO significant abscess reduction (Felizari 2025: BX alone P>0.05 vs control). Engineering tannase resistance into a compound that doesn't work alone is pointless. |
| G1-7 | Engineered funduliforme probiotic | **WOUNDED** | Funduliforme still causes 16.9% of abscesses. Introducing a live obligate anaerobe as a feed additive has no regulatory precedent. Horizontal gene transfer risk is real. |
| G1-8 | Anti-biofilm (rumen wall) | **KILLED** | F. necrophorum biofilm on rumen epithelium has NEVER been demonstrated. Target is speculative. |
| PG-1 | Anti-stellate cell activation | **KILLED** | Systemic TGF-beta inhibition is immunosuppressive. Must treat all cattle prophylactically because abscesses are subclinical. Cost and side effects are prohibitive in feedlot. Forge itself calls this impractical. |
| PG-2 | Abscess biofilm disruption | **KILLED** | Forge itself says "do not invest." The fibrous capsule is a physics barrier. Pharmacokinetically impossible. Included for completeness by Forge; killed for completeness by Reaper. |
| PG-3 | Anti-T. pyogenes synergy | **WOUNDED** | Only relevant in 29% of abscesses. Secondary pathogen. Dynasore at 10 uM in vitro does not predict in vivo efficacy. |
| PG-4 | Blood biomarker | **SURVIVED** | Not a treatment -- a diagnostic tool. Transformative if it works. Cheap to de-risk ($10-15K). Low downside. |
| COMBO-1 | mAb + phage | **WOUNDED** | Inherits the mAb duration problem. At $6-10/head with questionable mAb duration, the economics collapse. |
| COMBO-2 | mRNA vaccine + anti-adhesion | **SURVIVED** (conditional) | Best product concept IF the mRNA bacterial antigen immunogenicity question is answered AND hemagglutinin is sequenced. Both are testable. |
| V4 | Calcium chelation | **KILLED** | Calcium dependence of LktA is UNPROVEN. LktA has NO homology to RTX toxins. Systemic calcium chelation causes cardiac arrest. Even localized delivery is too dangerous for a feedlot product. |
| V6 | Downstream signaling blockade | **KILLED** | Caspase-3/NF-kB are essential host immune pathways. Blocking them globally is immunosuppressive. No evidence of a LktA-specific divergence point. |
| V9 | Hemolysin (PLB) inhibition | **WOUNDED** | Only TRACE activity against bovine erythrocytes. If the hemolysin barely works against the natural host's RBCs, why would inhibiting it matter? |
| V11 | Neuraminidase inhibition | **WOUNDED** | Population-level impact: ~5-10% of severe abscesses. Not worth pursuing as a standalone or even a secondary target. |
| V12 | Feedback loop disruption | **WOUNDED** | More of a conceptual insight than a druggable target. Separating neutrophil degranulation from phagocytosis is pharmacologically intractable. |
| V13 | Gallium porphyrin iron starvation | **WOUNDED** | Gallium was killed in v1 on regulatory grounds. Gallium nitrate remains IV-only in human medicine (NCT04294043 recruiting for CF/NTM is Phase 1b, still no approved antimicrobial product after 15+ years). No veterinary regulatory pathway exists. |
| V14 | LuxS/AI-2 quorum sensing | **KILLED** | Surveyor found NO AI-2 receptor genes in the F. necrophorum genome. LuxS is metabolic (activated methyl cycle), not a quorum sensor. The target does not exist. |
| V16 | Contact system blockade | **WOUNDED** | Demonstrated in Lemierre's syndrome (human). NEVER validated in any anaerobic abscess model in cattle. Bovine contact system may behave differently. Host-targeting approach with high selectivity risk. |
| V17 | MMP-13 induction blockade | **WOUNDED** | MMP inhibitors have failed repeatedly in human clinical trials (musculoskeletal side effects). MMP-13 may be redundant with bacterial proteases. Gate 1 target with all the Gate 1 limitations. |

---

## DETAILED KILL ANALYSES

---

### G2-1: Anti-LktA Monoclonal Antibody -- **WOUNDED**

**Kill Test 1 (20-Year Test):** Polyclonal anti-leukotoxin serum showed protection in 1997 (Saginala). That is 29 years ago. No monoclonal antibody against LktA has been developed for cattle in three decades. Why? Because the pharmacokinetic problem (duration of protection vs feeding period) has been recognized as fatal since the beginning. Elanco's CPMA (canine parvovirus mAb) provides 2-3 weeks of protection for a disease with a 1-2 week window. Liver abscess requires 120-400 days of continuous protection. These are different by an order of magnitude.

**Kill Test 3 (Matrix Test):** The mAb must reach effective concentrations in the hepatic sinusoidal space. Systemic IgG does equilibrate with the hepatic compartment (portal blood is not a privileged site), but the CONCENTRATION needed to neutralize leukotoxin from continuous translocation events over months is unknown. The Forge proposal cites "ex vivo liver perfusion" as a de-risk experiment, but a perfusion lasting hours cannot model the chronic, repeated challenge of a 4-8 month feeding period.

**Kill Test 10 (Commercial Reality):** Forge estimates $5-8/head for mAb injection. Bovine IgG1 half-life is approximately 21 days (similar to human IgG1). For a 200-day feeding period, you need approximately 10 injections (every 21 days). At $5-8 per injection, that is $50-80/head. The industry-wide loss from liver abscesses is $9.70/head. The economics are off by a factor of 5-8. Even with Fc engineering for extended half-life (FcRn recycling), you might achieve 30-42 day half-life at best, still requiring 5-7 injections. Repeated chute handling of feedlot cattle costs $1-3/head per event in labor alone, adding $5-21 in handling costs. A mAb-only approach is economically dead unless you can achieve single-injection, full-feeding-period protection -- which current mAb technology cannot do.

**Kill Test 11 (Independent Replication):** The Saginala 1997 challenge data (n=5/group) is the core evidence for leukotoxin neutralization efficacy. This data comes from a single research group (KSU/Nagaraja lab). The Saginala 1996 paper from the SAME lab showed that semi-purified leukotoxoid REDUCED protection vs crude supernatant -- which actually undermines the mAb concept (if purified antigen is less protective, a monospecific mAb targeting a single epitope may be even less protective). SINGLE-LAB DEPENDENCY for the core efficacy claim.

**Kill Test 12 (SCC/Clinical Endpoint Test):** Adapted for liver abscess: the relevant endpoint is abscess grading at slaughter (A-/A/A+), not just "abscess present/absent." A mAb that reduces A+ to A but does not eliminate abscesses has limited commercial value (all abscessed livers are condemned regardless of grade). The endpoint must be "clean liver at slaughter" to have economic impact.

**The embarrassment test (Kill Test 8):** A feedlot manager injects 5,000 cattle with an expensive mAb at arrival. Three weeks later, the mAb has washed out. The remaining 170 days of feeding occur without protection. Abscess rates are unchanged. Elanco writes off $150K in lost product. The simplest failure mode is that the protection window is too short relative to the risk period.

**Verdict: WOUNDED.** The target is correct. The mAb platform is real. But the pharmacokinetic mismatch (21-day half-life vs 120-400 day risk period) is a potentially fatal commercial flaw. The candidate can SURVIVE if: (1) a single-dose, extended-release formulation achieving >90 day half-life is demonstrated, OR (2) the mAb is repositioned as a 2-dose bridging strategy (mAb at arrival for immediate protection + vaccine at arrival for delayed but sustained protection -- i.e., mAb buys time for the vaccine to kick in).

---

### G2-2: mRNA-LNP Leukotoxin Vaccine -- **WOUNDED**

**Kill Test 1 (20-Year Test):** mRNA vaccines have existed for over a decade. Veterinary mRNA vaccines have been in development for 5+ years. The Elanco-Medgene H5N1 vaccine is the first cattle mRNA vaccine approaching approval. But that is for a VIRAL antigen. No mRNA vaccine has ever been tested against a BACTERIAL antigen in any livestock species. The Forge claim of "10-100x higher titers" is from human COVID vaccines (viral spike protein). Bacterial protein antigens have different immunogenicity profiles, folding requirements, and post-translational modifications. The extrapolation from viral to bacterial antigen immunogenicity is a leap, not a fact.

**Kill Test 2 (Species Test):** All titer superiority claims (mRNA vs protein subunit) come from human COVID-19 data. No cattle-specific comparison exists. Bovine immune responses to mRNA-encoded antigens may differ substantially from human responses. The one data point we have (H5N1 in cattle) is for a viral glycoprotein, not a 336 kDa bacterial protein. LktA is one of the largest known bacterial toxins. Encoding it (or its epitopes) in mRNA requires confirming that the bovine cellular machinery can correctly fold and present these unusual epitope regions.

**Kill Test 9 (Repetition Test):** This is Fusogard v2 with a different delivery platform. The failure mode of Fusogard was insufficient titer at the hepatic sinusoid on high-grain diets (the "firehose problem"). The mRNA vaccine claims to solve this with higher titers. But HOW MUCH higher is needed? Forge cites "4x higher peak titer" as the de-risk threshold. This is arbitrary. The Saginala 1997 data shows protection at controlled single-dose challenge. Field failure occurred with continuous chronic challenge. The titer needed to handle continuous challenge for 200 days may be 100-1000x higher than for a single challenge -- and even 10-100x higher titers from mRNA may not be sufficient.

**Kill Test 10 (Commercial Reality):** mRNA vaccines require cold chain storage (-20C to -80C for LNP formulations). Feedlot processing facilities in Kansas, Texas, and Nebraska operate outdoors in extreme temperatures (40C+ in summer, -20C in winter). The cold chain infrastructure does not exist at most feedlots. Forge mentions "costs are dropping rapidly" without quantification. Current veterinary mRNA vaccine cost estimates are $5-15/dose vs $0.50-2.00/dose for traditional protein subunit vaccines. At the required 2-dose schedule, that is $10-30/head vs $1-4/head for the subunit alternative.

**Kill Test 3 (Matrix Test):** LNP hepatotropism is claimed as an advantage. But LNP hepatotropism delivers the mRNA to HEPATOCYTES, not to antigen-presenting cells in the hepatic sinusoid specifically. Whether hepatocyte expression of LktA fragments leads to LOCAL sinusoidal immunity (vs systemic immunity that may be equivalent to any other injection site) is an assumption, not a demonstrated mechanism.

**Verdict: WOUNDED.** The platform is real (Elanco-Medgene exists). But three critical unknowns are stacked: (1) mRNA immunogenicity for bacterial vs viral antigens in cattle, (2) whether even 10-100x higher titers overcome the firehose problem, (3) cold chain and cost feasibility for feedlot deployment. The candidate survives if: a direct head-to-head comparison of mRNA vs protein subunit anti-LktA titers in cattle shows the claimed advantage. This is testable for $25-40K.

---

### G2-3: Epitope-Focused Recombinant LktA Subunit Vaccine -- **SURVIVED**

**Kill Test 1 (20-Year Test):** Xiao epitope mapping was published in 2009 (17 years). However, recombinant subunit vaccine technology with ISCOMATRIX adjuvants has advanced substantially since Fusogard. The reason the field hasn't done this is because Fusogard was on the market (then discontinued) and cheap tylosin filled the gap. The absence of a next-generation vaccine reflects market dynamics, not biological impossibility.

**Kill Test 2 (Species Test):** The Xiao epitope data is from mice, not cattle. Mouse protection does not guarantee bovine protection. However, the Saginala 1997 crude leukotoxoid data shows that anti-LktA antibodies ARE protective in cattle. The question is whether epitope-focused immunogens generate BETTER neutralizing responses than crude toxoid. This is testable.

**Kill Test 4 (Strain Test):** Epitope conservation across field isolates has not been verified. The 88% amino acid identity between subspecies means 12% of residues differ. If any PL1/PL3/PL4 epitope residues fall in the divergent regions, the vaccine could fail against some strains. This is a WOUNDED-level concern but is cheaply resolvable by sequencing epitope regions across 20-50 field isolates.

**Kill Test 9 (Repetition Test):** This IS an iteration on Fusogard. The firehose problem may persist. But the approach is honest about this: Forge positions it as strongest in combination with Gate 1 reduction. The ISCOMATRIX adjuvant genuinely produces 10-50x higher titers than aluminum hydroxide in veterinary vaccines -- this is well-documented, not aspirational.

**Kill Test 10 (Commercial Reality):** A recombinant subunit vaccine is the cheapest and most familiar product form for feedlot use. $1-3/dose, no cold chain, standard injection at processing. Compatible with existing chute-side protocols. Monensin-compatible. The commercial path is clear.

**Kill Test 11 (Independent Replication):** The Xiao 2009 epitope data is from the KSU/Nagaraja lab. The Saginala challenge data is also from KSU. This IS single-lab dependency for F. necrophorum-specific data. However, ISCOMATRIX adjuvant performance is validated across many independent labs for many antigens. The platform risk is low even if the target-specific risk has single-lab dependency. FLAGGED: first de-risk experiment must include an independent lab.

**Kill Test 8 (Embarrassment Test):** The simplest failure mode is that even with improved adjuvant, the titer still isn't high enough on high-grain diets. This is the same Fusogard failure mode. But it is testable for $30-50K before committing to a field trial.

**What I tried and failed to kill it with:** I looked for evidence that epitope-focused vaccines generate WORSE protection than whole-protein vaccines (which would undermine the approach). The Saginala 1996 data showing semi-purified leukotoxoid was LESS protective than crude supernatant initially seemed damaging. But this was semi-purification (partial removal of other antigens), not epitope-focused design (rational selection of best epitopes). These are different approaches. The failure of semi-purification does not predict the success or failure of epitope focusing.

**Verdict: SURVIVED.** Lowest risk, most technically straightforward Gate 2 candidate. Well-characterized failure modes. Cheapest de-risk path. Commercial form factor is ideal. Single-lab dependency flagged.

---

### G2-4: LktB Secretion Inhibitor -- **KILLED**

**Kill Test 1 (20-Year Test):** The TPS secretion system was characterized by Narayanan in 2001 (25 years ago). No inhibitor of ANY TPS system has ever entered clinical development for any pathogen. POTRA domain inhibitors for the related BamA system have been in preclinical research for over a decade with no clinical candidate. The field has been unable to drug these targets.

**Surveyor Correction (fatal):** The Surveyor's structural analysis is unambiguous: the POTRA domain is a FLAT BETA-SHEET SURFACE with LOW small molecule druggability. Forge's claim of a "druggable pocket" is directly contradicted by the Argus v9 ESMFold analysis (pLDDT 97 -- high confidence). The POTRA domain is not a cavity; it is a flat protein-protein interaction surface. Flat PPI surfaces are among the most difficult targets in all of drug discovery. Even large pharmaceutical companies with billion-dollar budgets struggle to drug flat PPI surfaces.

**Kill Test 10 (Commercial Reality):** Even if a peptide mimetic could be designed (moderate druggability per Surveyor), peptide drugs require parenteral administration and have short half-lives. A peptide drug targeting a bacterial outer membrane protein in the rumen wall or liver, requiring daily dosing by injection in feedlot cattle, is commercially nonsensical.

**The specific evidence that kills this:** Surveyor says "POTRA: NO (flat surface). Barrel pore: MODERATE (plug-stabilization strategy). Extracellular loops: YES for biologics/vaccine." If the small molecule approach is dead (and it is), the remaining path is a biologic targeting extracellular loops. But an anti-LktB antibody would need to reach F. necrophorum cells in the rumen wall or liver at sufficient concentration to block secretion -- the same delivery challenge as every other antibody approach, without the proven target validation that anti-LktA has. You would be developing a novel biologic against a novel target with no precedent.

**Verdict: KILLED.** Fatal flaw: the proposed druggable pocket does not exist. The POTRA domain is structurally flat. Forge overclaimed the druggability based on analogy rather than structure. Surveyor's correction is definitive. No viable path to a small molecule. The biologic alternative (anti-LktB loop antibody) is a longer development path than anti-LktA with no additional benefit.

---

### G2-5 / V1 / V2: lktA Transcription Suppressor + LktC Acyltransferase -- **WOUNDED**

**This candidate contains two hypotheses. I evaluate each separately.**

#### G2-5/V1: lktA Transcriptional Silencing

**Kill Test 1 (20-Year Test):** The lktBAC operon was characterized in 2001. The regulatory circuitry controlling its expression is STILL completely unknown 25 years later. This is not for lack of interest -- Nagaraja's group has been studying F. necrophorum virulence for 30+ years. The fact that the regulatory circuit remains unmapped suggests it is technically difficult (obligate anaerobe, poor genetic tools, complex regulation).

**The stacked unknowns:** To reach a drug from here requires resolving IN SERIES: (1) the environmental signals that upregulate lkt transcription, (2) the transcription factors that respond to those signals, (3) the druggable interface on those transcription factors, (4) a small molecule that fits that interface, (5) delivery to F. necrophorum in the rumen/liver. Each unknown has maybe a 30-50% probability of yielding a druggable result. Stacked in series: 0.3^5 = 0.2% probability of reaching a drug. This is a 10+ year research program, not a near-term portfolio candidate.

#### V2: LktC Acyltransferase Inhibition

**Kill Test (Critical Flaw -- RTX Analogy is Wrong):** This is the single most important kill test in the report. The ENTIRE premise of V2 rests on the analogy to RTX toxin acyltransferases. But F. necrophorum leukotoxin is NOT an RTX toxin. The 2001 Narayanan paper, the 2002 Narayanan review, and the 2004 Tadepalli review all state explicitly: LktA "does not have sequence similarity with any other bacterial leukotoxin." This is not a caveat -- it is the central fact about this toxin.

The RTX analogy fails on multiple levels:
1. **LktA has no RTX repeats.** RTX toxins are defined by glycine-rich nonapeptide repeats. LktA has none.
2. **LktA has no sequence homology to ANY other leukotoxin.** It is not a divergent RTX toxin; it is an entirely different protein.
3. **LktC's function is UNRESOLVED.** Surveyor confirms the histidine kinase annotation is WRONG, but the actual function is disputed between acyltransferase, zinc metalloenzyme, and chaperone. Three competing hypotheses with zero direct evidence for any of them.
4. **The acylation requirement is INFERRED, not demonstrated.** No one has ever shown that LktA requires post-translational acylation for activity. The inference comes entirely from operon organization (lktBAC resembles RTX operons in gene order). But gene order homology does not prove functional homology when the proteins themselves share no sequence similarity.

**Surveyor Correction:** The histidine kinase annotation is WRONG (Argus v9 BLAST: zero kinase domains). The protein has a YbjN domain with CCHH motif. This further undermines the RTX analogy -- if LktC is a zinc metalloenzyme or chaperone rather than an acyltransferase, the entire V2 hypothesis collapses.

**What survives:** The recombinant LktC acyltransferase assay ($5-10K, 4-6 weeks) would definitively resolve whether LktC IS an acyltransferase. This is a high-information, low-cost experiment. If it confirms acyltransferase activity, LktC becomes a legitimate first-in-class target with moderate-to-favorable druggability (8,317 A^3 cavity). If it refutes acylation, both V2 and part of G2-5 die immediately.

**Verdict: WOUNDED (combined).** The transcription approach has too many stacked unknowns for near-term investment. The LktC acyltransferase approach rests on an analogy that the primary literature contradicts. BUT both can be resolved cheaply: (1) lktBAC promoter-reporter construct under environmental signals ($5-10K), (2) recombinant LktC acyltransferase assay ($5-10K). Do these experiments. If LktC IS an acyltransferase, elevate V2 to Tier 1. If it is NOT, kill V2 permanently. Do not invest further without these data.

---

### G2-6: LktA Receptor Decoy / Receptor Blockade -- **WOUNDED**

**Kill Test 1 (20-Year Test):** The LktA receptor has been unknown for 24+ years. Multiple groups have presumably looked for it. The receptor for the closely related M. haemolytica leukotoxin (CD18) was identified decades ago. The fact that F. necrophorum LktA receptor remains unidentified despite active research suggests one of: (a) the receptor is an unusual protein not detected by standard methods, (b) the mechanism is not receptor-mediated (direct membrane insertion, like cholesterol-dependent cytolysins), or (c) the research community is too small and under-resourced.

**Kill Test 8 (Embarrassment Test):** You spend $30-50K on a receptor identification screen. The pull-down identifies CD18 (the obvious candidate from the M. haemolytica analogy). You then discover that blocking CD18 is globally immunosuppressive (CD18 is beta-2 integrin, essential for ALL leukocyte adhesion and extravasation). You cannot block CD18 without destroying the host immune system. $50K wasted, program back to zero.

**Alternative embarrassment:** The pull-down identifies nothing specific. LktA acts by non-specific membrane disruption (like a detergent) at high concentrations and receptor-mediated signaling at low concentrations. There is no single receptor to block. $50K wasted.

**Verdict: WOUNDED.** This is a legitimate discovery project with high payoff IF the receptor is identifiable and specifically blockable. But it is a 2-5 year research program with at least three branching failure points. Not a near-term portfolio candidate. Park it as a KE#2 experiment -- if it succeeds, it transforms the portfolio; if it fails, the portfolio is not dependent on it.

---

### G2-7: Kupffer Cell Trained Immunity (Beta-Glucan) -- **WOUNDED**

**Kill Test 2 (Species Test):** The Adams 2024 data showing beta-glucan protects Kupffer cells against sepsis-induced loss is in a mouse model. Not bovine. Bovine Kupffer cell biology may differ from murine.

**Kill Test 3 (Matrix Test):** LktA kills cells via a CONCENTRATION-DEPENDENT dual mechanism: low dose = apoptosis via caspase signaling; high dose = NECROSIS (likely membrane disruption). Trained immunity (epigenetic reprogramming via H3K4me1/H3K27ac) can plausibly enhance survival against signaling-mediated apoptosis. But necrosis caused by direct membrane destruction (pore formation or membrane solubilization) cannot be prevented by intracellular epigenetic changes. If the bacteria in the hepatic sinusoid produce LktA at moderate-to-high concentrations (which they likely do, given 7+ log CFU/g in established abscesses), necrosis will dominate. Trained immunity may protect against the LOW-DOSE activation but not the HIGH-DOSE killing that actually matters.

**Kill Test 9 (Repetition Test):** The failure analysis explicitly addresses this: "An activated Kupffer cell killed by leukotoxin is just as dead as a resting one." Forge argues that trained immunity is different from activation. This is partially true (trained immunity involves metabolic reprogramming, not just activation). But the killing mechanism matters. If LktA kills by physical pore formation at therapeutic concentrations, no amount of metabolic reprogramming prevents a hole in the membrane.

**Kill Test 10 (Commercial Reality):** IV beta-glucan injection in feedlot cattle is required (oral beta-glucan does not reach Kupffer cells -- proven by SCFP failure). IV injection at processing is feasible but adds cost and complexity. Duration of trained immunity: weeks to months. May need repeat dosing.

**Kill Test 11 (Independent Replication):** Adams 2024 (beta-glucan KC protection) is a SINGLE PUBLICATION from a SINGLE LAB. The application to F. necrophorum leukotoxin is entirely hypothetical. SINGLE-LAB DEPENDENCY for the core biological premise.

**Verdict: WOUNDED.** The concept is novel and intellectually interesting. But three concerns are serious: (1) LktA may kill by pore formation, not signaling -- trained immunity cannot block physical membrane destruction, (2) the Adams 2024 data is from ONE lab in a mouse sepsis model, not bovine leukotoxin exposure, (3) IV delivery adds cost and complexity. The candidate survives if: the in vitro bovine KC + LktA experiment ($8-12K) shows trained KCs have >=2-fold higher LD50. If they don't, kill it.

---

### G2-8: Anti-Factor H Binding (FomA) -- **SURVIVED**

**Kill Test 1 (20-Year Test):** Factor H binding by F. necrophorum was published by Friberg in 2008 (18 years ago). No intervention has been developed. HOWEVER: the Neisseria meningitidis fHbp vaccine (Bexsero, Trumenba) was approved in 2014-2015 and represents proof that targeting Factor H binding proteins is a clinically validated strategy. The veterinary field simply has not applied this approach to F. necrophorum -- which is exactly the kind of cross-pathogen translation Agteria should exploit.

**Kill Test 2 (Species Test):** The Friberg 2008 data is from human Lemierre's syndrome isolates, not bovine liver abscess isolates. Factor H binding was demonstrated in human serum. Bovine Factor H is a different protein with different binding characteristics. The binding must be confirmed in bovine serum. This is testable.

**Kill Test 4 (Strain Test):** Factor H binding varies from 5-42% across strains (Friberg 2008). This is substantial strain-level variation. If only high-binding strains cause severe disease (as Friberg reports for Lemierre's), then the intervention targets the right strains. If low-binding strains can also cause abscesses through other complement evasion mechanisms, the intervention has a ceiling.

**Kill Test 10 (Commercial Reality):** An anti-FomA vaccine is a standard parenteral vaccine candidate. FomA is a confirmed outer membrane protein. Anti-FomA antibodies would simultaneously block Factor H binding AND endothelial adhesion (Surveyor-confirmed dual mechanism). This is a two-for-one: one antibody, two mechanisms. The product concept is a multi-component vaccine (anti-LktA epitopes + anti-FomA) -- which is essentially what Liu 2021 tested in mice with success.

**Kill Test 5 (Resistance Test):** Resistance to anti-FomA antibodies would require mutation of the FomA surface. FomA mutations that abolish Factor H binding would simultaneously increase complement susceptibility, creating a fitness cost. This makes resistance unlikely to emerge -- the bacterium cannot easily escape without making itself more vulnerable.

**What I tried and failed to kill it with:** I looked for evidence that complement-mediated killing in portal blood is too slow to matter (transit time ~30 seconds from rumen to liver). Friberg 2008 showed increased killing at 3.5 hours, not seconds. However: (1) opsonization is rapid (seconds to minutes), (2) opsonized bacteria are MORE susceptible to phagocytosis by Kupffer cells even if complement MAC formation is slow, (3) the combination of anti-FomA + anti-LktA in a multi-component vaccine addresses both complement evasion and leukotoxin. The transit time objection is real but does not kill the candidate because opsonization assists Kupffer cell clearance downstream.

**Verdict: SURVIVED.** Dual-mechanism target with clinical vaccine precedent (Bexsero). Needs bovine Factor H binding confirmation. A strong component for a multi-antigen vaccine alongside LktA epitopes. The Surveyor's identification that G2-8 and G1-4 target the SAME protein (FomA) elevates this target -- you get anti-adhesion and anti-complement-evasion from one antigen.

---

### G2-9: Complement Enhancement (OMV Vaccine) -- **WOUNDED**

**Kill Test 4 (Strain Test):** OMV composition varies between bacterial strains. The 342 proteins identified in F. necrophorum OMVs (MDPI 2023) represent a MIXTURE from a SINGLE reference strain. Field isolate OMVs may have different compositions. A vaccine based on undefined OMV antigens from one strain may not cross-protect against heterologous field isolates.

**Kill Test 2 (Species Test):** The only in vivo data is from mice (Liu 2021). Mouse complement, antibody responses, and hepatic immune architecture differ from cattle. Mouse data cannot predict bovine field efficacy.

**Kill Test 10 (Commercial Reality):** OMV vaccines are difficult to standardize for regulatory approval. Each batch must be characterized for protein composition. Regulatory agencies (USDA-CVB) require defined antigens for veterinary biologics -- a 342-protein mixture is the opposite of defined.

**Verdict: WOUNDED.** An OMV vaccine is more of a research tool than a product candidate. Use OMVs to identify the BEST antigens for a defined subunit vaccine (combine the top hits with LktA epitopes and FomA). Do not try to commercialize the OMV mixture itself.

---

### G2-10: Anti-NET Evasion (DNase Inhibitor) -- **KILLED**

**Kill Test (Fatal Flaw):** F. necrophorum DNase activity has NOT been directly demonstrated. The evidence chain is: (1) F. nucleatum (a different species) suppresses NET formation, (2) DNase genes exist in the F. necrophorum genome, (3) therefore F. necrophorum probably has DNase activity. This is an inference chain, not evidence. Genomic gene predictions include pseudogenes, non-expressed genes, and genes with different substrate specificities.

Surveyor explicitly flags this: "DNase activity in F. necrophorum is INFERRED, not demonstrated. The gene predictions could be non-functional pseudogenes."

**Kill Test 8 (Embarrassment Test):** You develop a DNase inhibitor for F. necrophorum. You test it. F. necrophorum does not produce extracellular DNase. The target never existed.

**The cheap resolution:** A simple in vitro DNase activity assay ($2-5K, 1-2 weeks) would confirm or kill this target. But until that experiment is done, this candidate should not be in the portfolio. You cannot list a target that may not exist as a candidate.

**Verdict: KILLED.** Target existence is undemonstrated. Do the DNase activity assay. If positive, resurrect. If negative, permanently dead.

---

### G1-1: Anti-Hemagglutinin Vaccine -- **KILLED**

**Kill Test (Fatal Flaw):** Surveyor flagged this with devastating clarity: "The protein has been characterized functionally but NOT at the gene/sequence level. The '19 kDa hemagglutinin' has not been cloned. Without a resolved gene sequence, recombinant vaccine production is not possible."

The hemagglutinin was described by Kanoe & Iwaki in 1987 -- 39 years ago. In four decades, nobody has cloned this gene. This is not a trivial gap -- it means that despite active research on F. necrophorum virulence, the hemagglutinin has resisted molecular characterization. Possible reasons: the functional activity (hemagglutination) may be caused by multiple surface proteins, not a single gene product. Or the protein is difficult to purify away from other surface components. Or it is a modification of another protein rather than a standalone gene product.

**Kill Test 4 (Strain Test):** Some ruminal isolates are hemagglutination-NEGATIVE yet F. necrophorum thrives in the rumen. This means hemagglutination is not required for rumen colonization. If not required for rumen colonization, is it required for rumen wall penetration? Unknown.

**Kill Test 5 (Resistance Test):** Multiple adhesins exist (43K OMP, FadA, OmpA, OmpH). Even if hemagglutinin is blocked, other adhesins may compensate. Adhesion redundancy makes single-adhesin targeting unreliable.

**Verdict: KILLED.** You cannot make a recombinant vaccine against a protein that has never been cloned or sequenced in 39 years. The gene is unresolved. The adhesion function is likely redundant. This candidate is dead until the gene is identified. If Forge wants to rescue this, the FIRST experiment is gene identification (SDS-PAGE, excise 19 kDa band, mass spec), not vaccine development.

---

### G1-2: F. necrophorum Phage Cocktail -- **SURVIVED**

**Kill Test 1 (20-Year Test):** Phage therapy for rumen pathogens is relatively new. The Schwarz 2024 paper is the first comprehensive isolation and characterization of F. necrophorum-specific phages. This is not a 20-year-old idea that nobody acted on -- it is a genuinely recent development.

**Kill Test 3 (Matrix Test):** Rumen stability is the critical unknown. The rumen environment (pH 5.0-6.5 during SARA, proteases, protozoa, 60-100L volume) is hostile to phage particles. However: (1) phages naturally exist in the rumen -- the Schwarz 2024 phages were ISOLATED from rumen fluid, proving they survive in this environment, (2) continuous in-feed delivery (like tylosin) could maintain effective phage concentrations even with degradation, (3) phage accumulation in biofilms on the rumen wall would concentrate them where F. necrophorum resides.

**Kill Test 5 (Resistance Test):** Phage resistance emerges rapidly (single receptor mutations). A cocktail of 3+ phages with different receptor specificities mitigates this, but does not eliminate it. Continuous in-feed delivery with a rotating cocktail is the standard phage therapy approach. This is a legitimate concern but is well-recognized in the phage therapy field and has established mitigation strategies.

**Kill Test 10 (Commercial Reality):** In-feed continuous delivery mirrors tylosin's route. Feed additive regulatory pathway is established. No withdrawal period (phage are not antibiotics). Cost estimate of $1-2/head for continuous feeding is within the competitive range. Compatible with monensin.

**Kill Test 8 (Embarrassment Test):** The simplest failure: phage are destroyed by rumen proteases within minutes, never reaching effective concentrations. But this is testable in a $15-25K rumen-fistulated cattle study before any commercial investment. The de-risk is honest and appropriately designed.

**Kill Test 11 (Independent Replication):** Schwarz 2024 is a single publication from one lab. The 2025 MDPI study isolated additional phages independently, providing partial independent confirmation that F. necrophorum phages exist and can be isolated. Not full replication of efficacy, but independent confirmation of the biological premise.

**What I tried and failed to kill it with:** I looked for evidence that rumen phage populations are ineffective at controlling their bacterial hosts (the observation that F. necrophorum persists despite naturally occurring phage predation). This is a valid concern -- naturally occurring phage-bacteria dynamics maintain equilibrium rather than eliminating the host. Therapeutic phage cocktails aim to tip this balance by delivering phage at orders of magnitude above natural levels. Whether this works in the rumen is genuinely unknown, but the principle (super-physiological phage dosing) has been demonstrated in other systems.

**Verdict: SURVIVED.** The phages exist, are obligately lytic, and infect both subspecies. The rumen stability question is testable for $15-25K before any major investment. The commercial form factor is ideal (in-feed, continuous, no withdrawal). This is a honest, well-bounded candidate with identifiable failure modes and cheap de-risk experiments. Best Gate 1 candidate in the portfolio.

---

### G1-3: Protected Butyrate + Zinc -- **KILLED**

**Kill Test 9 (Repetition Test -- FATAL):** SCFP (Saccharomyces cerevisiae fermentation product) was tested across n=4,689 cattle and produced ZERO liver abscess reduction despite measurably improving rumen health markers. SCFP contains beta-glucans, mannan-oligosaccharides, and fermentation metabolites -- including butyrate-promoting components. If SCFP's comprehensive rumen health improvement produced zero abscess reduction, why would protected butyrate + zinc produce any?

Forge's defense: "This is a combination component, not standalone." But a combination component with zero standalone efficacy adds zero to the combination. If the Gate 2 partner (vaccine, mAb) works, it works with or without butyrate. If the Gate 2 partner fails, butyrate cannot rescue it. The combination framing is a rescue narrative for a dead compound.

**"Why isn't the field doing this?" test:** Butyrate supplementation has been available for cattle for over a decade. Zinc supplementation is standard feedlot practice. If the combination worked, it would be standard of care. It isn't because it doesn't work for liver abscess.

**Kill Test 10 (Commercial Reality):** Protected butyrate is a commodity feed additive with no IP protection. Even if it contributed marginal abscess reduction in combination, Agteria/Elanco would capture zero value from the butyrate component. There is no commercial rationale for including a commodity ingredient with no demonstrated efficacy in an IP-protected portfolio.

**Verdict: KILLED.** SCFP (n=4,689) is the definitive control experiment. Gate 1 feed additives do not reduce liver abscesses. Butyrate + zinc is a Gate 1 feed additive. "Combination component" framing cannot rescue a zero-effect mechanism. The portfolio is better served by focusing resources on Gate 2 candidates.

---

### G1-4: Anti-43K OMP Vaccine -- **WOUNDED**

Surveyor merged G1-4 with G2-8 -- they target the SAME protein (FomA/43K OMP). This means G1-4 is not a separate candidate; it is a component of the FomA-targeting program.

**As a standalone anti-adhesion candidate: WOUNDED.** Multiple adhesins exist. Single-adhesin blockade may be insufficient. Same redundancy concern as G1-1.

**As part of the FomA dual-mechanism program (merged with G2-8): see G2-8 assessment.** The dual mechanism (anti-adhesion + anti-complement-evasion) from one antigen is the strongest argument. An anti-FomA antibody in a multi-component vaccine alongside LktA epitopes is the rational evolution of the Liu 2021 concept.

**Verdict: WOUNDED as standalone. Evaluate as part of the G2-8/FomA program.**

---

### G1-5: Hindgut-Targeted Suppression -- **WOUNDED**

**Kill Test 1 (20-Year Test):** The hindgut pathway was only recognized in 2022 (Fuerniss) and 2025 (Salih). This is a genuinely new finding. The 20-year test does not apply.

**Kill Test 10 (Commercial Reality):** Colonic drug delivery in cattle is undeveloped. No colonic-targeted feed additive or pharmaceutical exists for cattle. Developing a pH-responsive encapsulated antimicrobial for the bovine colon is a formulation challenge that adds years to the development timeline.

**Verdict: WOUNDED.** Correctly gated on KE#1. Do not invest until hindgut contribution is quantified. If KE#1 shows >20% hindgut origin, this becomes a real gap that must be addressed. But the colonic delivery technology does not currently exist.

---

### G1-6: Tannase-Resistant Tannin -- **KILLED**

**Kill Test 9 (Repetition Test -- FATAL):** Felizari 2025 (n=2,986) showed that tannin blend ALONE (BX without monensin) did NOT significantly reduce liver abscess incidence (P>0.05 vs control). Tannins alone are a zero-effect intervention. Engineering tannase resistance into a compound class that produces zero standalone effect is optimizing a failed approach. Making tannins more resistant to degradation does not fix the fact that tannins don't work for liver abscess prevention.

**The consensus data confirms this:** The 2019 Argentine study (n=495) showed tannins reduced macroscopic abscesses (3/258 vs 14/237), but microscopic lesions were identical between groups -- suggesting tannins affected abscess PROGRESSION but not liver COLONIZATION by bacteria. This is a Gate 1 effect on abscess size, not on the Gate 2 bottleneck. It confirms tannins cannot address the disease mechanism.

**Verdict: KILLED.** Tannins alone do not prevent liver abscesses (Felizari 2025, P>0.05). Improving tannin stability does not fix the fundamental problem -- the mechanism of action (Gate 1 rumen ecology) is wrong.

---

### G1-7: Engineered Funduliforme Probiotic -- **WOUNDED**

**Kill Test 5 (Resistance/Ecology Test):** F. necrophorum subsp. funduliforme causes 16.9% of liver abscesses on its own. Introducing funduliforme into the rumen does not eliminate the disease -- it replaces severe abscesses with milder abscesses. This is a harm reduction strategy, not a cure.

**Kill Test 10 (Commercial Reality):** Regulatory pathway for a live obligate anaerobe feed additive in cattle does not exist. The closest precedent is DFMs (Bacillus, Lactobacillus), which are GRAS organisms with decades of safety data. Introducing a KNOWN PATHOGEN (even an attenuated subspecies) as a feed additive would face extraordinary regulatory scrutiny. The horizontal gene transfer risk (virulence gene acquisition from necrophorum to funduliforme) would be a major regulatory concern.

**Kill Test 8 (Embarrassment Test):** You introduce funduliforme into feedlot pens. Horizontal gene transfer occurs (documented in Fusobacterium). Funduliforme acquires the high-leukotoxin promoter from necrophorum. You have now created a more virulent strain and distributed it across the feedlot.

**Verdict: WOUNDED.** Elegant concept undermined by: (1) funduliforme itself causes disease, (2) no regulatory pathway for a pathogenic species as a feed additive, (3) horizontal gene transfer risk. Would require a synthetic biology approach (deletion of lktA from funduliforme) that adds complexity and regulatory burden.

---

### G1-8: Anti-Biofilm (Rumen Wall) -- **KILLED**

**Kill Test (Fatal Flaw):** F. necrophorum biofilm on rumen epithelium has NEVER been demonstrated. Surveyor flagged this: "No direct evidence of F. necrophorum biofilm on rumen epithelium exists." The entire candidate is based on inference from F. nucleatum (a different species in a different environment). The rumen wall concentrations (4-5 log CFU/g) are cited as "consistent with biofilm densities," but planktonic bacteria at the tissue surface can also achieve these densities.

**Verdict: KILLED.** Target is speculative. Demonstrate biofilm first ($5-8K confocal microscopy experiment). If biofilm is confirmed, resurrect. If not, permanently dead. Same logic as G2-10 (DNase): do not list undemonstrated targets as portfolio candidates.

---

### PG-1: Anti-Stellate Cell Activation -- **KILLED**

**Kill Test 10 (Commercial Reality -- FATAL):** This requires systemic TGF-beta pathway inhibition in feedlot cattle. TGF-beta is a master regulator of immune tolerance, wound healing, and fibrosis across all tissues. Systemic inhibition causes immunosuppression, delayed wound healing, and potentially autoimmune responses. Feedlot cattle experience routine injuries, respiratory infections, and immune challenges. Immunosuppressing them is directly harmful.

Furthermore, abscesses are subclinical -- no diagnostic exists to identify which cattle have early-stage seeding events. You would need to treat ALL cattle prophylactically with an immunosuppressive drug for weeks during the adaptation period. This is ethically and commercially untenable.

**Forge agrees:** "HONEST ASSESSMENT: impractical in feedlot setting." If Forge itself calls the candidate impractical, Reaper concurs.

**Verdict: KILLED.** Impractical, immunosuppressive, and requires prophylactic treatment of all cattle. Forge's own assessment is accurate.

---

### PG-2: Abscess Biofilm Disruption -- **KILLED**

**Forge said:** "Do not invest. Physics barrier. Focus all resources on prevention."

**Reaper says:** Agreed. The fibrous capsule is avascular. Drug penetration is <10%. The microenvironment is anaerobic and acidic. Even if you could deliver an agent, F. necrophorum at 7+ log CFU/g would overwhelm any realistic drug concentration.

**Verdict: KILLED.** Physics barrier. Pharmacokinetically impossible. Forge and Reaper agree.

---

### PG-3: Anti-T. pyogenes Synergy -- **WOUNDED**

**Kill Test 4 (Strain Test):** T. pyogenes is present in only 29% of abscesses. The 71% of abscesses without T. pyogenes demonstrate that F. necrophorum does NOT need T. pyogenes to form abscesses. Targeting T. pyogenes addresses a minority of abscesses and a secondary pathogen.

**Kill Test 10 (Commercial Reality):** The population-level impact is ~10-15% reduction in SEVERE abscesses (affecting only the 29% T. pyogenes-positive subset). This is commercially marginal. No feedlot would adopt a product that addresses 10% of the problem.

**Kill Test 8 (Embarrassment Test):** You develop an anti-pyolysin treatment. You test it in a field trial. Only 29% of abscesses have T. pyogenes. Your treatment has no detectable effect on overall abscess incidence because 71% of abscesses are unaffected.

**Verdict: WOUNDED.** Secondary target. Only value is as a component in a multi-antigen vaccine (where adding T. pyogenes antigens is nearly free). Not worth standalone investment.

---

### PG-4: Blood Biomarker -- **SURVIVED**

**Kill Test 3 (Matrix Test):** The capsule barrier that prevents drug penetration into abscesses also prevents metabolite leakage OUT of abscesses. Sensitivity may be very low at the critical early stage when intervention could help.

**Kill Test 8 (Embarrassment Test):** You develop a biomarker panel. Sensitivity is 60% and specificity is 70%. In a 20% prevalence population, the positive predictive value is ~33%. Two out of three positive tests are false positives. Feedlot managers treat based on false positives, wasting resources.

**Why it survives despite these concerns:** This is a DIAGNOSTIC, not a treatment. The downside of failure is $10-15K wasted, not a failed drug program. The upside of success is transformative: real-time abscess tracking enables vastly better clinical trials for all other candidates in the portfolio. Even a moderate-performance biomarker (AUC-ROC 0.75) would be revolutionary for the field.

**Verdict: SURVIVED.** Low-cost de-risk. Transformative upside. Acceptable downside. Not a therapeutic candidate -- a research tool that enables better evaluation of everything else.

---

### COMBO-1: Anti-LktA mAb + Phage -- **WOUNDED**

Inherits the mAb duration problem from G2-1. If the mAb provides only 21 days of protection, the combination product provides 21 days of dual protection followed by months of phage-only protection. Phage-only is a Gate 1-only approach. The combination does not solve the mAb pharmacokinetic limitation -- it just adds a Gate 1 component during the brief window when the mAb is active.

**Kill Test 10 (Commercial Reality):** At $6-10/head ($5-8 mAb + $1-2 phage), the product costs more than tylosin ($2-3/head) for potentially similar efficacy. The economic case collapses unless the mAb duration problem is solved.

**Verdict: WOUNDED.** The phage component is strong (see G1-2 SURVIVED). The mAb component is the weak link. Reposition as phage + vaccine (COMBO-2 architecture) rather than phage + mAb.

---

### COMBO-2: mRNA Vaccine + Anti-Adhesion Vaccine -- **SURVIVED (conditional)**

**This is the best PRODUCT CONCEPT in the portfolio** despite individual component concerns:

1. Multi-component vaccine (LktA epitopes + FomA + hemagglutinin?) addresses Gate 2 + Gate 1 simultaneously
2. Single injection at processing = minimal labor
3. Vaccine provides duration of protection that mAb cannot
4. The Liu 2021 mouse data validates the multi-antigen approach

**Conditional on:** (1) mRNA immunogenicity for bacterial antigens in cattle is confirmed, (2) hemagglutinin is sequenced (or replaced with FomA as the anti-adhesion component), (3) cost is competitive with tylosin.

**Better version:** Drop the mRNA platform (unproven for bacterial antigens, cold chain problem). Use a PROTEIN SUBUNIT approach: epitope-focused LktA (PL1+PL3+PL4) + recombinant FomA + ISCOMATRIX adjuvant. This eliminates the mRNA bacterial antigen uncertainty, the cold chain requirement, and the cost premium. It is essentially G2-3 + G2-8 in one injection. Call it COMBO-2b.

**Verdict: SURVIVED (conditional).** Best product architecture. Should be reformulated as a protein subunit combination (COMBO-2b: LktA epitopes + FomA, ISCOMATRIX adjuvant) to eliminate unnecessary mRNA platform risk.

---

## VULCAN QUARANTINED TARGETS

---

### V4: Calcium Chelation -- **KILLED**

**Kill Test (Fatal Flaw #1):** LktA calcium dependence is completely unproven. LktA has NO homology to RTX toxins. The inference of calcium dependence comes entirely from RTX analogy, but LktA is NOT an RTX toxin (no glycine-rich repeats, no sequence homology). Assuming calcium dependence because "other toxins need calcium" is not evidence.

**Kill Test (Fatal Flaw #2):** Systemic calcium chelation causes cardiac arrest (calcium is essential for cardiac muscle contraction, neurotransmission, and blood clotting). Even localized hepatic calcium chelation would disrupt hepatocyte function. The safety margin is zero.

**Verdict: KILLED.** Two fatal flaws: unproven target biology AND lethal safety profile. The confirming experiment (LktA + EGTA in vitro) costs $2-5K. If calcium dependence is confirmed, the biology is interesting but the delivery/safety problem remains fatal for a feedlot product.

---

### V6: Downstream Signaling Blockade -- **KILLED**

**Kill Test (Fatal Flaw):** Caspase-3, caspase-8, and NF-kB are ESSENTIAL host immune pathways. Blocking them globally causes immunosuppression. Emricasan (pan-caspase inhibitor) was in human clinical trials for NASH -- it FAILED and was abandoned partly due to immune consequences. If pan-caspase inhibition fails in controlled human clinical settings with careful dose management, applying it to feedlot cattle as prophylaxis is fantasy.

The approach requires finding a LktA-SPECIFIC signaling pathway that diverges from normal immune signaling. Vulcan correctly identifies this as the weakest link but has no evidence that such a divergence point exists. Without this, the approach is just "block the immune system and hope for the best."

**Verdict: KILLED.** The target (host immune signaling) cannot be safely blocked. No evidence for a LktA-specific divergence point. Pharmacologically intractable.

---

### V9: Hemolysin (PLB) Inhibition -- **WOUNDED**

**Kill Test 2 (Species Test):** The disease map states: "Strong lysis of rabbit, human, and dog erythrocytes; only TRACE activity against bovine erythrocytes." If the hemolysin barely affects bovine RBCs, its contribution to bovine liver abscess pathogenesis is questionable. A virulence factor that doesn't work against the host species is not a useful drug target.

**Possible rescue:** The hemolysin may have non-RBC targets (leukocyte membranes, hepatocyte membranes) that are more susceptible than bovine RBCs. Or the "trace" activity may be sufficient in the confined abscess microenvironment. But these are hypotheses, not data.

**Verdict: WOUNDED.** Low priority. The bovine RBC resistance data is a strong negative signal. Do not invest unless a hemolysin-deficient mutant shows reduced virulence in a bovine system.

---

### V11: Neuraminidase Inhibition -- **WOUNDED**

**Kill Test 10 (Commercial Reality):** Population-level impact: ~5-10% of severe abscesses. This is too small to justify development as a standalone product or even a significant combination component. The entire T. pyogenes space (V10, V11, V15) addresses only 29% of abscesses and only the secondary pathogen. Neuraminidase is one of several T. pyogenes virulence factors, making its individual contribution even smaller.

**Verdict: WOUNDED.** Marginal population-level impact. Not worth standalone or even combination investment at current evidence levels.

---

### V12: Feedback Loop Disruption -- **WOUNDED**

This is a conceptual insight, not a druggable target. The insight (leukotoxin reduction may have non-linear effects because the feedback loop breaks) is valuable for portfolio STRATEGY but does not translate to a specific intervention. Separating neutrophil degranulation from phagocytosis pharmacologically is one of the hardest challenges in immunopharmacology.

**Verdict: WOUNDED.** Retain as a portfolio-level insight. Do not invest as a drug target.

---

### V13: Gallium Porphyrin Iron Starvation -- **WOUNDED**

**Kill Test 1 (20-Year Test):** Gallium as an antimicrobial has been in development for over 15 years (Kaneko 2007). In human medicine: gallium nitrate (Ganite) is FDA-approved only for cancer-related hypercalcemia, NOT as an antimicrobial. The ABATE trial (NCT04294043) for gallium nitrate in CF patients with NTM infections is Phase 1b, RECRUITING since 2021, not expected to complete until 2027. AR-501 (inhaled gallium citrate) for CF Pseudomonas (NCT03669614) has UNKNOWN status after 7+ years. No gallium antimicrobial product has EVER received regulatory approval in any country for any infection.

**Kill Test 10 (Commercial Reality):** Gallium compounds are IV or inhaled in human medicine. No oral formulation exists. Feedlot cattle cannot receive IV gallium. Even gallium porphyrins with hepatic tropism would require parenteral administration. The regulatory pathway for a novel metal-based antimicrobial in food-producing animals is UNDEFINED. Withdrawal periods would be extended (heavy metal residue concerns). The USDA/FDA would require extensive tissue residue studies.

**v1 Kill:** This was previously killed on regulatory grounds. Nothing has changed. Gallium antimicrobials remain 10+ years from human regulatory approval and have NO veterinary regulatory pathway.

**What saves it from complete kill:** The BIOLOGY is elegant. F. necrophorum's lack of Fur and siderophores makes it uniquely vulnerable to iron mimetics. The gallium porphyrin Trojan horse concept is mechanistically sound. If regulatory barriers were removed, this would be a top-3 target.

**Verdict: WOUNDED (not killed, because the biology is real; but the regulatory barrier is currently insurmountable).** Park as a 10-year moonshot. If gallium antimicrobials achieve human approval (ABATE trial success by 2027), revisit for veterinary translation. Until then, do not invest.

---

### V14: LuxS/AI-2 Quorum Sensing -- **KILLED**

**Kill Test (Fatal Flaw):** Surveyor found NO AI-2 receptor genes in the F. necrophorum genome. LuxS is present but AI-2 receptor genes (lsrB, lsrACDB transport system, or LuxP/LuxQ homologs) are ABSENT. Without a receptor, there is no quorum sensing circuit. LuxS in the absence of AI-2 receptors functions in the activated methyl cycle (SAM recycling), which is a core metabolic pathway, not a virulence regulator.

This is not a wound -- it is a kill. The target does not exist. LuxS/AI-2 quorum sensing in F. necrophorum is a myth. LuxS is metabolic.

**Verdict: KILLED.** No AI-2 receptor genes. LuxS is metabolic, not regulatory. The quorum sensing hypothesis for F. necrophorum is falsified by genomic evidence.

---

### V16: Contact System Activation Blockade -- **WOUNDED**

**Kill Test 2 (Species Test -- CRITICAL):** Contact system activation by F. necrophorum was demonstrated in the context of Lemierre's syndrome (HUMAN jugular vein thrombophlebitis). The bovine hepatic sinusoidal environment is different: (1) bovine contact factors may have different sensitivity, (2) the hepatic sinusoid has unique hemodynamics (low shear, fenestrated endothelium) that differ from the jugular vein, (3) the bovine coagulation system differs from human (cattle have lower Factor XII levels and different contact activation kinetics).

**Kill Test 1 (20-Year Test):** Contact system activation in bacterial infections has been studied for >20 years (review: 2010, J Mol Med). Contact system inhibitors (lanadelumab) are FDA-approved for hereditary angioedema. Despite this, NO contact system-based antimicrobial strategy has been developed for ANY infection. If contact system blockade were an effective antimicrobial strategy, it would have been tried in human sepsis (where contact system activation is well-documented). It has not succeeded.

**Kill Test 10 (Commercial Reality):** Lanadelumab costs approximately $40,000/year in humans. A bovine-adapted contact system inhibitor would be a novel biologic targeting a host pathway -- expensive, complex, and with high risk of immune-related side effects (coagulopathy, bleeding risk).

**Verdict: WOUNDED.** The biology is interesting but entirely unvalidated in cattle. Contact system activation may contribute to the disease but has never been shown to be necessary or sufficient for abscess formation. The 20-year absence of contact system-based antimicrobials in human medicine, despite extensive research, is a strong negative signal. Do not invest without bovine-specific validation.

---

### V17: MMP-13 Induction Blockade -- **WOUNDED**

**Kill Test 1 (20-Year Test):** MMP inhibitors have been in pharmaceutical development for 30+ years. They have FAILED repeatedly in human clinical trials -- the marimastat/batimastat era of broad-spectrum MMP inhibitors ended in failure due to musculoskeletal syndrome (joint pain, stiffness, tendonitis). MMP-13-selective inhibitors have better safety profiles but NONE has been approved for any indication.

**Kill Test 5 (Resistance/Redundancy Test):** F. necrophorum produces its own proteases (disease map: "Proteases degrade tissue matrix proteins, facilitating spread"). MMP-13 is one of potentially multiple tissue-degradation mechanisms. If bacterial proteases provide sufficient tissue penetration independent of MMP-13, blocking MMP-13 alone will fail.

**Kill Test 10 (Commercial Reality):** This is a Gate 1 target (rumen wall penetration). Gate 1 targets have a ceiling because Gate 2 is the bottleneck. Even if MMP-13 blockade reduces rumen wall penetration by 50%, this only reduces the inoculum arriving at the liver. It does not address leukotoxin. Same limitation as every other Gate 1-only approach.

**Verdict: WOUNDED.** 30+ years of MMP inhibitor clinical failures. Bacterial protease redundancy. Gate 1 target with Gate 1 limitations. Low priority.

---

## KILL SUMMARY AND PORTFOLIO IMPLICATIONS

### What SURVIVED (5 candidates)

1. **G2-3: Epitope subunit vaccine** -- Lowest risk Gate 2 candidate. Proven adjuvant. Known failure modes. Testable.
2. **G1-2: Phage cocktail** -- Best Gate 1 candidate. Phages exist. Both subspecies susceptible. Honest about limitations.
3. **G2-8: Anti-FomA (Factor H + adhesion)** -- Dual mechanism. Vaccine precedent. One antigen, two benefits.
4. **PG-4: Blood biomarker** -- Not a therapy. Transformative research tool. Cheap to de-risk.
5. **COMBO-2 (reformulated as COMBO-2b)** -- Best product concept: LktA epitopes + FomA, protein subunit, ISCOMATRIX adjuvant. Single injection. Gate 1 + Gate 2.

### What is WOUNDED but Worth Saving (6 candidates)

1. **G2-1: Anti-LktA mAb** -- Reposition as BRIDGING strategy (immediate protection while vaccine builds) or as a research tool (ex vivo liver perfusion). Not a standalone product.
2. **G2-2: mRNA vaccine** -- Test bacterial antigen immunogenicity in cattle. If confirmed, revisit. If not, use protein subunit platform instead.
3. **G2-5/V2: LktC acyltransferase** -- Do the $5-10K recombinant LktC assay. Binary outcome: if acyltransferase, elevate to Tier 1; if not, kill permanently.
4. **G2-6: LktA receptor decoy** -- Park as KE#2 discovery project. High payoff if successful. Not portfolio-critical.
5. **V13: Gallium porphyrin** -- Park as 10-year moonshot. Elegant biology, insurmountable regulatory barrier today.
6. **G1-7: Funduliforme probiotic** -- Interesting but regulatory and safety concerns need resolution.

### What is DEAD (10 candidates)

G2-4 (LktB -- flat POTRA), G2-10 (DNase -- undemonstrated), G1-1 (hemagglutinin -- unsequenced), G1-3 (butyrate -- SCFP kills it), G1-6 (tannin -- BX alone P>0.05), G1-8 (biofilm -- undemonstrated), PG-1 (stellate cell -- impractical), PG-2 (abscess disruption -- physics), V4 (calcium -- unsafe), V6 (caspase -- immunosuppressive), V14 (LuxS -- no receptor genes).

### The Surviving Portfolio Architecture

```
PRODUCT CONCEPT (single-injection, multi-antigen vaccine):
  - LktA epitopes PL1+PL3+PL4 (Gate 2 -- leukotoxin neutralization)
  - Recombinant FomA (Gate 2 -- complement sensitization + Gate 1 -- anti-adhesion)
  - ISCOMATRIX adjuvant (proven 10-50x titer enhancement)

COMBINATION PARTNER (in-feed, continuous):
  - Phage cocktail (phiKSUM + phiBB) (Gate 1 -- F.n. suppression)

RESEARCH TOOLS:
  - Blood biomarker (enables real-time trial monitoring)
  - LktC acyltransferase assay (resolves first-in-class drug target)
  - LktA receptor identification (opens new intervention axis)
```

This is a 3-component portfolio: vaccine (injectable) + phage (in-feed) + diagnostics. It addresses Gate 2 (leukotoxin + complement) and Gate 1 (phage + anti-adhesion) simultaneously -- the combination that the failure analysis says has never been tried. Estimated cost: $3-5/head for the vaccine + $1-2/head for phage = $4-7/head total, competitive with tylosin.

---

## REAPER'S FINAL NOTE

The target is right. Leukotoxin neutralization at Gate 2 is the correct strategy. The bottleneck determination is correct. The portfolio architecture (Gate 1 + Gate 2 combination) is correct.

But Forge overbuilt the portfolio with speculative targets (unsequenced proteins, undemonstrated activities, analogy-based inferences) and defensive candidates (feed additives positioned as "combination components" to avoid being killed). The 28-candidate list looked comprehensive but included 10 candidates that should never have been proposed.

The surviving portfolio is smaller, cheaper, and more honest. Five candidates. Three product components. One product concept. Test it.

---

*41 candidates attacked. 10 killed. 16 wounded. 5 survived. The dead are dead. The wounded need specific answers. The survivors are ready for Board evaluation.*
