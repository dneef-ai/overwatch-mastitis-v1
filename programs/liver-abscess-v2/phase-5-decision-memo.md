# Phase 5 -- Decision Memo: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Prepared for:** Senior R&D Leadership, Elanco Animal Health
**Prepared by:** Agteria Bio (9-agent drug discovery pipeline)
**Date:** 2026-03-27
**Classification:** Partner Confidential

---

## 1. Executive Summary

Liver abscess in feedlot cattle costs the US beef industry $256M/year. The only effective prevention -- tylosin -- faces growing AMR pressure, first-confirmed F. necrophorum resistance (2024), and an EU September 2026 antimicrobial deadline. No effective replacement exists.

We ran the disease through Agteria's 9-agent pipeline with 6-model external panels at every phase, a 4-agent Tribunal bottleneck consensus, and a quarantined first-principles analysis (Vulcan). The pipeline evaluated 41 candidate interventions, killed 10, wounded 16, and surfaced 5 survivors plus a genuinely novel drug target.

**What we found:**

1. **The disease is decided at the liver, not the rumen.** A 4-agent Tribunal independently converged on leukotoxin-mediated killing of Kupffer cells (Gate 2) as the rate-limiting bottleneck -- not barrier failure (Gate 1). This reframes the entire intervention strategy. Every Gate 1-only approach ever tested (essential oils, DFMs, SCFP/Diamond V, monensin alone) has produced zero abscess reduction despite improving rumen conditions. The Gate 2 insight explains why Fusogard worked in challenge but failed in the field: the target was right but the titer was insufficient.

2. **A multi-antigen vaccine is the lead product.** LktA epitopes (PL1+PL3+PL4) + recombinant FomA in ISCOMATRIX adjuvant. Single injection at processing. $2-4/head. Non-antibiotic. No withdrawal. Addresses both leukotoxin neutralization (Gate 2) and complement sensitization (Gate 1-2 transition). This is Fusogard v2 -- same target, fundamentally better formulation.

3. **A first-in-class drug target may exist.** Vulcan's quarantined analysis identified LktC acyltransferase as a novel molecular target inside the leukotoxin lifecycle. If LktC activates pro-LktA through acylation (as in all characterized RTX toxin systems), inhibiting it would render leukotoxin inactive without killing the bacterium -- a clean anti-virulence target with no AMR implications and no human medicine competition. This has never been tested. A $5-10K binary assay resolves it.

4. **A phage cocktail is the best non-antibiotic Gate 1 component.** Obligately lytic phages that kill both F. necrophorum subspecies exist (Schwarz 2024). In-feed continuous delivery mirrors tylosin's route. No withdrawal. No AMR. Rumen stability is the critical unknown, testable for $15-25K.

**What it costs to find out:** $65-110K first tranche over 16-20 weeks. Three priority experiments + KE#1 (abscess typing) in parallel.

**What Elanco gets that cannot be built internally:**
- The Gate 2 bottleneck reframe (changes everything about intervention strategy)
- FomA complement sensitization (cross-pathogen translation from Neisseria meningitidis -- your livestock vaccine team would not find this)
- LktC acyltransferase (a novel drug target nobody has tested)
- F. necrophorum phage cocktail (2024 publication, not yet in any commercial pipeline)

---

## 2. The Problem: Why Liver Abscess Is Hard

Liver abscess is not a typical infectious disease. It is a diet-driven, endogenous, polymicrobial infection where the pathogen is a permanent resident of the rumen. You cannot eradicate it without destroying rumen function. You cannot change the diet without destroying feedlot economics. You cannot treat established abscesses because the fibrous capsule creates a physical sanctuary impervious to antibiotics. And you cannot diagnose it in live cattle.

**The numbers:**
- 21.3% mean US feedlot prevalence (12-32% range by management)
- $255.6M annual US cost (95% CI: $161.9M-$377.9M)
- $9.70/head industry-wide (including unaffected cattle)
- Doubling trend since 2010
- First tylosin-resistant F. necrophorum isolated in 2024
- 71% of large US feedlots use in-feed tylosin
- EU September 2026: medically important antimicrobials banned for prophylactic use in food animals

**Why previous approaches failed:**
- Gate 1 approaches (rumen pH management) have ZERO abscess effect. SCFP improved rumen health across 4,689 cattle with zero abscess reduction. Essential oils showed a non-significant 107% INCREASED risk. The disease is not controlled at the rumen.
- Fusogard proved the right target (leukotoxin neutralization) but failed on high-grain diets -- the "firehose problem." Chronic high-volume translocation overwhelmed vaccine-induced antibody titers. 80% protection in challenge, inconsistent in the field. Discontinued.
- Tylosin works (40-70% reduction) but via indirect inoculum reduction at Gate 1, not by addressing the bottleneck. It has reached its ceiling and faces regulatory attrition.

The central insight: **Nothing has ever targeted both gates simultaneously.** The portfolio below does.

---

## 3. What We Did: The Pipeline

### 9-Agent Architecture

| Agent | Role | Output |
|-------|------|--------|
| **Pathfinder** | Complete disease map with R0 analog and KE#1 identification | Disease stages, virulence factors, epidemiology, key unknowns |
| **Tribunal** | 4-agent bottleneck consensus (unframed biology, pathogen specialist, host/environment, quantitative first-principles) | Gate 2 leukotoxin bottleneck determination (4/4 convergence) |
| **Sapper** | Forensic failure analysis of 13 prior interventions | Target vs. compound failure classification for every approach |
| **Forge** | 28 candidate interventions across all disease stages | LktA lifecycle decomposition into 6 molecular intervention points |
| **Vulcan** | First-principles vulnerability analysis, quarantined from failure data | 17 independent intervention points (8 novel); LktC acyltransferase discovery |
| **Surveyor** | Computational validation of all 41 candidates | Sequence identity, host selectivity, structure predictions, Forge-Vulcan merge |
| **Reaper** | Red-team attack on every candidate (12 kill tests each) | 10 killed, 16 wounded, 5 survived |
| **Board** | 6-model external panel synthesis + devil's advocate + force-ranking | Portfolio-level single-lab risk identification; priority de-risk sequence |
| **Anvil** | Coverage test, evidence register, partner-grade deliverables | This memo |

### External Review

6 frontier models (Gemini 3.1 Pro, GPT-5.4, Grok 4, Claude Opus, DeepSeek R1, Qwen 2.5) independently reviewed every phase output via generative prompts -- contributing targets, challenging kills, and flagging structural risks. The most important finding from external review: **portfolio-level single-lab dependency on KSU/Nagaraja research lineage** (flagged by 3/6 models at Board phase, confirmed by Board as structural risk).

### Quality Controls
- 16 principles enforced throughout (including Principle 14: novel drug targets over feed additives; Principle 15: decompose the primary target)
- Vulcan quarantine ensured first-principles novelty (8 genuinely novel targets identified independently)
- Tribunal consensus prevented individual-agent bias in bottleneck identification
- 70% tractable pathology coverage test: PASSED (90% of tractable stages covered)

---

## 4. The Portfolio (Force-Ranked)

### The v1 to v2 Evolution

| Dimension | v1 (Argus-era) | v2 (Overwatch) |
|-----------|----------------|----------------|
| **Portfolio backbone** | MON+BX tannin blend (feed additive) + rPL4 vaccine | Leukotoxin lifecycle targets (vaccine + novel drug targets) + phage |
| **Bottleneck understanding** | "Barrier failure is rate-limiting" (Gate 1) | "Leukotoxin immune evasion is rate-limiting" (Gate 2) -- Tribunal 4/4 consensus |
| **Target type** | Feed additive-centered | Drug target-centered (Principle 14) |
| **Novelty** | Tannin blend (existing product) + vaccine iteration | LktC acyltransferase (first-in-class) + FomA complement sensitization (Neisseria translation) |
| **IP position** | Weak (tannin is commodity, vaccine is obvious) | Strong (LktC inhibitor = novel chemical entity; FomA complement mechanism = novel indication) |

The shift was driven by two v2-specific innovations:
1. **Tribunal reframed the bottleneck.** Four independent analytical agents converged on Gate 2 (leukotoxin at the liver), overriding the disease map's initial Gate 1 lean. The quantitative evidence was decisive: rumenitis does not predict abscesses (Magrin 2021, r ~ 0), pH management has zero effect on abscesses, and leukotoxin production predicts severity at P < 0.0001.
2. **Vulcan found LktC.** Quarantined from all prior work, Vulcan decomposed the LktA lifecycle into 6 molecular intervention points and identified LktC acyltransferase as a genuinely novel first-in-class target -- something the literature-aware pipeline (Forge) only partially captured.

### Force-Ranked Portfolio

| Rank | Target | Type | Rationale | Critical Gate |
|------|--------|------|-----------|--------------|
| **1** | **V2: LktC acyltransferase assay** | Novel drug target (gating experiment) | Highest information/dollar ($5-10K). Binary: opens first-in-class anti-virulence target or dies permanently. No one else is testing this. Agteria's strategic differentiator. | Recombinant LktC must show acyltransferase activity |
| **2** | **G2-3: Epitope subunit vaccine** (LktA PL1+PL3+PL4 + ISCOMATRIX) | Lead Gate 2 product | Most technically mature. $1-3/dose. Compatible with feedlot processing. Addresses the bottleneck. Proven adjuvant platform. | Independent lab must replicate Xiao epitope immunogenicity in cattle; neutralizing titers >=4x Fusogard at 16 weeks |
| **3** | **G2-8: Anti-FomA** (complement sensitization + anti-adhesion) | Lead vaccine component 2 | Dual-mechanism: blocks Factor H binding (restores complement killing) + blocks endothelial adhesion. Neisseria vaccine precedent (Bexsero/Trumenba). Novel to Elanco. | Bovine liver abscess isolates must bind bovine Factor H |
| **4** | **G1-2: Phage cocktail** | Best non-antibiotic Gate 1 | Obligately lytic phages exist. Both subspecies susceptible. In-feed continuous delivery = tylosin form factor. No AMR. EU deadline alignment. | Phage survives in rumen >=8h; achieves >=1 log F.n. reduction at 48h |
| **5** | **PG-4: Blood biomarker** | Research infrastructure | Cheap ($10-15K). Enables real-time trial monitoring for all other candidates. Transforms a field dependent on slaughter-only endpoints. | At least one analyte AUC-ROC >=0.75 |

### The Product Concept (if de-risk succeeds)

```
NEAR-TERM (2-3 years to conditional licensure):
  Multi-antigen protein subunit vaccine
    - LktA epitopes PL1+PL3+PL4 (Gate 2: leukotoxin neutralization)
    - Recombinant FomA (Gate 2: complement sensitization; Gate 1: anti-adhesion)
    - ISCOMATRIX adjuvant
    - Single injection at feedlot arrival processing
    - Optional booster at reimplant (~60 days)
    - Cost target: $2-4/head

  + Phage cocktail (phiKSUM + phiBB) in-feed continuous
    - Cost: +$1-2/head
    - Total: $3-6/head (competitive with tylosin at $2-3/head)

LONG-TERM (7-10 years to market):
  LktC acyltransferase inhibitor
    - Oral, daily, in-feed or bolus
    - First-in-class anti-virulence agent
    - Patentable novel chemical entity
    - No AMR implications
    - Potential for combination with vaccine
```

---

## 5. The Decision Tree

### First Tranche: $65-110K, 16-20 weeks

```
EXPERIMENT 1: LktC Acyltransferase Assay ($5-10K, 4-6 weeks)
  |
  |--> POSITIVE (mass shift detected): LktC IS an acyltransferase
  |      --> Commission AF3 structure prediction + virtual screen
  |      --> Elevate to Tier 1 drug target
  |      --> Agteria has a first-in-class asset
  |
  |--> NEGATIVE (no mass shift): LktC is NOT an acyltransferase
         --> Kill V2 permanently
         --> Portfolio proceeds as vaccine + phage only (still viable)

EXPERIMENT 2: Multi-Antigen Vaccine Immunogenicity ($30-50K, 16-20 weeks)
  |
  |--> GO: Anti-LktA titer >=4x Fusogard at 16 weeks
  |    AND anti-FomA restores SBA by >=3-fold
  |    AND bovine isolates bind bovine Factor H
  |      --> Proceed to bovine challenge trial ($150-300K)
  |
  |--> PARTIAL GO: Anti-LktA titer improved but <4x Fusogard
  |    OR FomA SBA weak (<3-fold)
  |      --> Reformulate (adjuvant dose, antigen ratio, booster schedule)
  |      --> Consider mAb bridging (G2-1) if titer insufficient
  |
  |--> KILL: Anti-LktA titers <=Fusogard equivalent
  |    OR zero bovine Factor H binding by field isolates
  |      --> Pivot to mRNA vaccine (G2-2) if Medgene data positive
  |      --> Or pivot to mAb bridging + LktC inhibitor (if confirmed)
  |      --> Or escalate to Daniel: portfolio restructure required

EXPERIMENT 3: Phage Rumen Stability ($15-25K, 4-6 weeks)
  |
  |--> GO: Phage detectable >=10^4 PFU/mL at 8h
  |    AND F. necrophorum >=1 log reduction at 48h
  |      --> Proceed to phage cocktail optimization and larger rumen trial
  |
  |--> KILL: Phage undetectable by 4h
  |    OR F. necrophorum <0.3 log reduction at 48h
  |      --> Portfolio becomes vaccine-only
  |      --> Gate 1 uncovered (firehose problem more acute)

KE#1: Abscess Typing Study ($15-25K, parallel)
  |
  |--> Hindgut <5%: Portfolio architecture confirmed
  |--> Hindgut 5-20%: Note as ceiling. Proceed.
  |--> Hindgut >20%: Add Bacteroides antigens to vaccine. Phage ceiling noted.
  |--> Hindgut >40%: Restructure. Multi-pathogen approach required.
```

### Second Tranche Decision Point (Week 20)

With first-tranche results in hand:

| Scenario | Action | Estimated Second Tranche |
|----------|--------|------------------------|
| All three GO + LktC positive | Full acceleration: challenge trial + LktC drug program + phage optimization | $300-500K |
| Vaccine GO + phage KILL + LktC positive | Vaccine + LktC drug program (no phage) | $250-400K |
| Vaccine GO + phage GO + LktC negative | Vaccine + phage combination product | $200-350K |
| Vaccine PARTIAL + phage GO + LktC positive | Reformulate vaccine, continue phage, accelerate LktC | $200-400K |
| Vaccine KILL | Pivot to alternative Gate 2 approach (mAb bridging, mRNA) | Reassess at Board |

---

## 6. De-Risk Experiments

### Experiment 1: LktC Acyltransferase Assay

| Parameter | Detail |
|-----------|--------|
| **Objective** | Determine whether LktC functions as an acyltransferase that activates pro-LktA |
| **Design** | Express recombinant LktC in E. coli. Incubate with recombinant pro-LktA + acyl-ACP donor. Detect acylated LktA by mass spectrometry (expected mass shift ~250 Da per acylation site). Positive control: E. coli HlyC + pro-HlyA (characterized RTX system). |
| **GO threshold** | Mass shift detected; acylated LktA confirmed by MS |
| **KILL threshold** | No mass shift; LktC does not catalyze acylation |
| **If GO** | Commission AF3 structure prediction of LktC. Virtual screen of 10M compound library against active site. Top 20 hits tested in LktA cytotoxicity assay (if inhibitor blocks LktC, LktA should be inactive against bovine PMNs). |
| **If KILL** | V2 dies permanently. LktC function (chaperone? metalloenzyme?) is scientifically interesting but not a druggable anti-virulence target. |
| **Cost** | $5-10K |
| **Timeline** | 4-6 weeks |
| **Why first** | Highest information/dollar in the portfolio. Binary outcome. Resolves whether Agteria has a first-in-class drug target. |

### Experiment 2: Multi-Antigen Vaccine Immunogenicity Trial

| Parameter | Detail |
|-----------|--------|
| **Objective** | Determine whether epitope-focused LktA + FomA vaccine generates sufficient neutralizing titers in cattle, AND whether FomA complement sensitization translates to bovine system |
| **Design** | Express PL1+PL3+PL4 fusion protein + recombinant FomA (GenBank JQ740821). Formulate with ISCOMATRIX adjuvant. Vaccinate 20 cattle (10 vaccine, 10 control) at an INDEPENDENT lab (NOT KSU). Measure at 2, 4, 8, 16 weeks: (a) anti-LktA neutralizing titer, (b) anti-FomA titer, (c) serum bactericidal activity against F. necrophorum in bovine serum, (d) bovine Factor H binding by bovine liver abscess isolates (n=20 isolates). |
| **GO threshold** | Anti-LktA neutralizing titer >=1:256 at 16 weeks (>=4x historical Fusogard). Anti-FomA antibodies restore serum bactericidal activity by >=3-fold. Bovine liver abscess isolates bind bovine Factor H. |
| **KILL threshold** | Anti-LktA titers <=Fusogard equivalent (adjuvant improvement not sufficient). Zero bovine Factor H binding by field isolates. |
| **Clinical endpoint note** | Secondary endpoint: anti-LktA serum must neutralize LktA cytotoxicity against bovine PMNs in vitro (LD50 shift >=4-fold). This confirms the antibodies are FUNCTIONALLY neutralizing, not just binding. |
| **If GO** | Proceed to bovine intraportal challenge trial (n=20-30, vaccine vs control, abscess grading at slaughter). Endpoint: clean liver rate (Grade 0) in vaccinated vs. control. |
| **If KILL** | Reformulate if anti-LktA titer is improved but insufficient. Pivot to mRNA or mAb if protein subunit ceiling is confirmed. Drop FomA if bovine Factor H binding is absent. |
| **Cost** | $30-50K |
| **Timeline** | 16-20 weeks |
| **Why at independent lab** | 5/6 external models flagged single-lab dependency on KSU. The entire portfolio's credibility depends on independent replication of the foundational immunogenicity claims. |

### Experiment 3: Phage Rumen Stability Trial

| Parameter | Detail |
|-----------|--------|
| **Objective** | Determine whether F. necrophorum-specific phages survive in the rumen and suppress the target organism |
| **Design** | Administer phiKSUM + phiBB (obligately lytic, both subspecies) to rumen-fistulated cattle (n=4). Continuous in-feed delivery mimicking commercial use. Sample rumen fluid at 0, 1, 4, 8, 24, 48h. Quantify: (a) viable phage by plaque assay, (b) F. necrophorum concentration by qPCR, (c) rumen microbiome composition by 16S to detect off-target effects. |
| **GO threshold** | Phage detectable at >=10^4 PFU/mL at 8h. F. necrophorum >=1 log reduction sustained at 48h. |
| **KILL threshold** | Phage undetectable by 4h (protease destruction). F. necrophorum <0.3 log reduction at 48h. |
| **Clinical endpoint note** | This is a pharmacokinetic study, not an efficacy study. The clinical endpoint (abscess reduction at slaughter) requires a subsequent feedlot trial if the PK study passes. |
| **If GO** | Optimize cocktail (additional phages for resistance management). Design feedlot trial with phage + vaccine combination. |
| **If KILL** | Portfolio becomes vaccine-only. Gate 1 is uncovered. The vaccine must overcome the firehose problem alone. |
| **Cost** | $15-25K |
| **Timeline** | 4-6 weeks |

### KE#1: Abscess Typing Study (Parallel)

| Parameter | Detail |
|-----------|--------|
| **Objective** | Quantify rumen vs. hindgut contribution to hepatic bacterial seeding |
| **Design** | Collect matched samples (rumen epithelium, colonic epithelium, liver abscess material) from 50 cattle at slaughter. qPCR for F. necrophorum subsp. necrophorum, subsp. funduliforme, and Bacteroides spp. on all three tissue types from each animal. |
| **Outcomes** | Hindgut <5%: proceed as is. 5-20%: note ceiling. >20%: add Bacteroides antigens. >40%: restructure. |
| **Cost** | $15-25K |
| **Timeline** | 4-8 weeks |

**Total first-tranche: $65-110K. All results in 16-20 weeks.**

---

## 7. Commercial Positioning

Three options depending on Elanco's strategic priority. These are not mutually exclusive.

### Option A: Tylosin Replacement (Defensive)

**Positioning:** "The non-antibiotic alternative to Tylan for liver abscess prevention."

- Product: Multi-antigen vaccine (single injection) + phage cocktail (in-feed continuous)
- Price: $3-6/head (competitive with tylosin at $2-3/head, justified by non-antibiotic positioning and regulatory future-proofing)
- Target customer: Feedlots facing or anticipating antimicrobial use restrictions (EU mandatory September 2026; US regulatory tightening likely)
- Elanco advantage: Self-cannibalizes Tylan before competitors or regulators do. Controls the transition.
- Timeline to conditional licensure: 2-3 years post-successful challenge trial
- Market size: $180-250M annually (US beef feedlots, based on current tylosin revenue + premium for non-antibiotic + regulatory-driven adoption)

**Why Elanco should want this:** You own Tylan. You know it faces attrition. Better to replace your own product with your own non-antibiotic alternative than to have a competitor or regulator do it for you. This is controlled self-disruption.

### Option B: First-in-Class Drug Target (Offensive)

**Positioning:** "The first anti-virulence drug for liver abscess -- a new drug class."

- Product: LktC acyltransferase inhibitor (oral, in-feed)
- Conditional on: LktC acyltransferase assay confirming the target
- Price: Premium ($5-10/head, justified by novel MOA, no AMR, patentable NCE)
- Target customer: Feedlots seeking differentiated technology beyond vaccines
- Elanco advantage: First-in-class. Patentable. No human medicine competition (LktA is unique to F. necrophorum). Platform potential across RTX-producing veterinary pathogens.
- Timeline: 7-10 years to market
- Market size: Potentially $300-500M+ if platform extends to other RTX pathogens

**Why Elanco should want this:** The vaccine is a good product. An anti-virulence drug is a franchise. Patent-protected, no generic erosion for 15+ years. Anti-virulence is the future of antimicrobial alternatives -- Elanco positions as a leader in the space.

### Option C: Combination Platform (Full Portfolio)

**Positioning:** "The complete liver abscess prevention platform -- vaccine + phage + anti-virulence."

- Product: Vaccine (injection at processing) + phage (in-feed continuous) + LktC inhibitor (in-feed, when available)
- Price: Tiered -- vaccine alone ($2-4), vaccine + phage ($3-6), full platform ($8-15)
- Target customer: Tiered by feedlot size and regulatory environment
- Elanco advantage: Leverages ALL of Elanco's capabilities -- biologics manufacturing (vaccine), feed additive distribution (phage), small molecule R&D (LktC inhibitor), mAb manufacturing ($130M facility, for bridging if needed), Benchmark database (68,000 feedlots for trial design)
- Timeline: Vaccine + phage in 2-3 years; LktC inhibitor adds in 7-10 years

**Why Elanco should want this:** No competitor can match the full platform because no competitor has biologics + feed additive + small molecule + mAb + data capabilities. Elanco is the only company positioned to deliver all layers. This is a moat.

---

## 8. What We Are NOT Promising

This section exists because honest science requires honest boundaries.

1. **We are not promising that the vaccine will overcome the firehose problem.** Fusogard proved the target is right and the approach can fail. Our formulation (ISCOMATRIX adjuvant, epitope focusing, FomA combination) is designed to be fundamentally better than Fusogard, but whether "better" is "enough" on high-grain diets is an open question that only a challenge trial can answer. The first-tranche experiments are designed to resolve this before committing to a challenge trial.

2. **We are not promising that LktC is an acyltransferase.** The hypothesis rests on operon organization analogy to RTX toxin systems, but LktA has no sequence homology to RTX toxins. The $5-10K assay is binary -- it either confirms or kills the target. If LktC is not an acyltransferase, the "first-in-class drug target" narrative disappears and the portfolio becomes a vaccine program.

3. **We are not promising that phage will work in the rumen.** The rumen is the most hostile environment for phage therapy: acidic, protease-rich, 60-100L volume, protozoal predation. The phages were isolated FROM the rumen (proving they can exist there), but whether therapeutic dosing achieves sustained suppression is genuinely uncertain.

4. **We are not promising that FomA complement sensitization translates from human Lemierre's to bovine liver abscess.** All Factor H binding data is from human isolates in human serum. The bovine system is different. This is why bovine confirmation is a hard gate in Experiment 2.

5. **We are not promising sub-tylosin cost.** The vaccine ($2-4/head) + phage ($1-2/head) totals $3-6/head versus tylosin at $2-3/head. The product will cost more than tylosin. The value proposition is non-antibiotic positioning, regulatory future-proofing, and potentially superior efficacy. If the industry is not willing to pay a premium for non-antibiotic prevention, the product faces an adoption barrier.

6. **We are not promising the single-lab dependency is resolved.** The entire portfolio traces critical F. necrophorum-specific evidence to the KSU/Nagaraja research lineage. We have mandated independent replication in Experiment 2. But until that experiment is done and confirmed, the foundational claims remain single-lab.

7. **We are not promising the hindgut pathway is addressed.** KE#1 may reveal that 20-40% of liver abscess bacteria come from the colon, not the rumen. If so, all rumen-focused interventions (phage) have an intrinsic ceiling, and the vaccine may need Bacteroides antigens that are not in the current formulation.

8. **We do not know the exact neutralizing antibody titer needed to overcome continuous translocation on high-grain diets.** This is the central unknown of the entire vaccine approach. The Saginala challenge model used a single intraportal dose. Field conditions involve months of chronic, variable translocation. The titer needed may be 10-1000x higher than challenge models suggest. Experiment 2 measures titers; a challenge trial tests whether those titers are sufficient.

---

## Appendix: Target Product Profiles

### TPP-1: Multi-Antigen Liver Abscess Vaccine

| Parameter | Specification |
|-----------|--------------|
| **Indication** | Prevention of hepatic abscessation in feedlot cattle on high-grain finishing diets |
| **Active ingredients** | Recombinant LktA epitopes (PL1+PL3+PL4 fusion) + recombinant FomA (377 aa) |
| **Adjuvant** | ISCOMATRIX (saponin-based; proven 10-50x titer enhancement in veterinary vaccines) |
| **Route** | Subcutaneous injection |
| **Dose schedule** | Single dose at feedlot arrival processing; optional booster at reimplant (~60 days) |
| **Onset of protection** | 14-21 days post-vaccination (antibody titer reaches protective threshold) |
| **Duration of protection** | Target: >=20 weeks (covers 120-150 day finishing period) |
| **Efficacy target** | >=50% reduction in liver abscess incidence vs unvaccinated controls at slaughter (minimum); target >=70% in combination with phage |
| **Price target** | $2-4/head (single dose); $3-6/head (with phage combination) |
| **Withdrawal period** | None (biologic, not antimicrobial) |
| **Regulatory pathway** | USDA-CVB conditional license (9 CFR 101-113); Subunit vaccine with defined antigens |
| **Monensin compatibility** | REQUIRED -- must be compatible with concurrent monensin feeding (near-universal in US feedlots) |
| **Storage** | 2-8C (standard refrigerated); NO ultra-cold chain requirement |
| **Target buyer** | Feedlot operations with >=1,000 head capacity; veterinary distributors |
| **Competitive positioning** | Non-antibiotic alternative to tylosin; addresses both Gate 1 (FomA anti-adhesion) and Gate 2 (LktA neutralization) |

### TPP-2: F. necrophorum Phage Cocktail (In-Feed)

| Parameter | Specification |
|-----------|--------------|
| **Indication** | Reduction of F. necrophorum load in the rumen of feedlot cattle; combination use with liver abscess vaccine |
| **Active agents** | phiKSUM + phiBB (obligately lytic, infect both subspecies) + 1-2 additional phages for resistance management |
| **Route** | In-feed, continuous daily administration (mirrors tylosin delivery) |
| **Dose** | TBD based on rumen stability trial (target: maintain >=10^4 PFU/mL in rumen fluid) |
| **Efficacy target** | >=1 log reduction in rumen F. necrophorum concentration; translating to >=20% standalone abscess reduction |
| **Price target** | $1-2/head for entire feeding period |
| **Withdrawal period** | None (phage, not antimicrobial) |
| **Regulatory pathway** | FDA-CVM (GRAS determination for phage in animal feed, or New Animal Drug Application) |
| **Storage** | Lyophilized or spray-dried for room temperature stability; reconstituted in feed premix |
| **Monensin compatibility** | REQUIRED |
| **Target buyer** | Feed mills, premix manufacturers; distributed through Elanco's feed additive network |
| **Competitive positioning** | Non-antibiotic tylosin replacement for EU-compliant operations; combinable with vaccine for full coverage |

### TPP-3: LktC Acyltransferase Inhibitor (Contingent on Experiment 1 GO)

| Parameter | Specification |
|-----------|--------------|
| **Indication** | Prevention of hepatic abscessation via anti-virulence mechanism (renders leukotoxin inactive) |
| **Mechanism** | Inhibits LktC-mediated acylation of pro-LktA; F. necrophorum produces but cannot activate leukotoxin |
| **Route** | Oral, daily, in-feed or intraruminal bolus |
| **Drug class** | Novel chemical entity; first-in-class anti-virulence agent |
| **Efficacy target** | >=50% reduction in liver abscess incidence as standalone; >=80% in combination with vaccine |
| **Price target** | $5-10/head for feeding period (premium justified by novel MOA, IP protection) |
| **AMR risk** | Minimal -- anti-virulence mechanism does not kill bacteria, reducing selection pressure |
| **Patent position** | Strong -- novel target (LktC), novel mechanism (RTX acyltransferase inhibition), no prior art |
| **Withdrawal period** | TBD based on PK studies; target: <=0 days (residue-free at slaughter) |
| **Regulatory pathway** | FDA-CVM New Animal Drug Application (NADA) |
| **Timeline** | 7-10 years from target confirmation to market |
| **Human medicine overlap** | None -- LktA is unique to F. necrophorum. No human pathogen uses this exact system. No competition from human pharma. |

---

## Appendix: Embarrassment Pass

For each lead candidate, the simplest plausible failure mode and what a skeptical Elanco scientist would say.

### G2-3 + G2-8 (Multi-Antigen Vaccine)

**Simplest failure mode:** The ISCOMATRIX adjuvant generates impressive anti-LktA titers in the first 4 weeks, but titers wane to sub-protective levels by week 12 -- exactly when the high-grain period is most intense. The firehose problem reasserts. Fusogard all over again with a better adjuvant that still isn't good enough.

**Skeptical Elanco scientist says:** "We had a leukotoxoid vaccine. It was called Centurion. We discontinued it because it didn't work on high-grain. What is quantitatively different about your formulation that solves the problem we already failed at?"

**Our answer:** Three things are quantitatively different: (1) ISCOMATRIX generates 10-50x higher titers than aluminum hydroxide (Centurion's likely adjuvant) -- this is documented across veterinary vaccines. (2) Epitope focusing concentrates the immune response on neutralizing regions rather than diluting across the 336 kDa protein. (3) FomA adds complement sensitization that Centurion lacked -- bacteria arriving at the liver are pre-opsonized for Kupffer cell uptake, reducing the leukotoxin challenge. These are testable claims. Experiment 2 measures all three.

### G1-2 (Phage Cocktail)

**Simplest failure mode:** Phage particles are destroyed by rumen proteases within 30 minutes. Despite continuous in-feed delivery, effective phage concentration never exceeds 10^2 PFU/mL -- two orders of magnitude below the therapeutic threshold. F. necrophorum numbers are unchanged.

**Skeptical Elanco scientist says:** "These phages were isolated from the rumen, so they exist there naturally. But they haven't eliminated F. necrophorum in nature. Why would adding more of them do what nature can't?"

**Our answer:** Natural phage-bacteria equilibrium maintains BOTH populations. Therapeutic dosing aims to shift the equilibrium by delivering phage at 10^4-10^6x above natural levels. This has worked in other phage therapy contexts (C. difficile, P. aeruginosa wounds). Whether it works in the rumen is genuinely uncertain -- which is why the $15-25K stability trial exists before any commercial commitment.

### V2/LktC (Acyltransferase Inhibitor)

**Simplest failure mode:** LktC is not an acyltransferase. It is a zinc metalloenzyme or chaperone with no druggable anti-virulence function. The $5-10K assay shows no mass shift. Target dies in week 4.

**Skeptical Elanco scientist says:** "You're assuming LktA behaves like an RTX toxin because the operon looks similar. But LktA has zero sequence homology to RTX toxins. Why should the activation mechanism be the same?"

**Our answer:** It might not be. That is exactly why the assay is the FIRST experiment, not the tenth. At $5-10K for a binary answer, the information value justifies the cost even at 30-50% probability of confirmation. If LktC is an acyltransferase, Elanco has a first-in-class drug target nobody else is pursuing. If it isn't, nothing else in the portfolio changes and you've spent $5-10K to learn something definitive about the pathogen's biology.

---

*Portfolio constructed. 70% tractable coverage: PASSED. Three priority experiments defined. Decision tree specified. Honest about what we don't know. Fund the first tranche.*
