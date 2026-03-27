# Phase 5: Decision Memo — Liver Abscess Prevention Portfolio

**To:** Senior R&D Leadership, Elanco Animal Health
**From:** Agteria Discovery Platform (Overwatch)
**Date:** 2026-03-27
**Re:** Tylosin Replacement Portfolio for Feedlot Liver Abscess Prevention

---

> **CRITICAL: KE#1 has not been run. The $15-20K paired abscess typing experiment described in Section 6 should run BEFORE committing to any de-risk investment. Its result restructures the entire portfolio.**

---

## 1. Executive Summary

We ran a 7-agent, 6-model drug discovery pipeline against feedlot liver abscess prevention. Twenty-seven candidate interventions were proposed, computationally validated, adversarially challenged, externally reviewed by six frontier AI models, force-ranked, and portfolio-tested. Ten were killed. Four survived with conditions. Thirteen remain wounded (viable but requiring specific data).

**The portfolio's recommendation:** A three-component prevention strategy combining burden reduction (monensin + tannin blend), immune support (recombinant leukotoxin vaccine with modern adjuvant), and hindgut protection (pending KE#1), validated through a gated $330-440K de-risk sequence over 14-16 months.

**The bottom line for Elanco:**
- The first $15-20K experiment (KE#1, paired abscess typing) restructures the entire strategy and should run immediately
- The combination of MON+BX burden reduction with an improved leukotoxin vaccine is the highest-probability path to a non-antibiotic tylosin replacement
- No single intervention will match tylosin. The replacement must be multi-dimensional, matching tylosin's multi-mechanism action
- Total investment through the definitive combination trial decision gate: $330-440K over 14-16 months
- If the combination works, commercial positioning options range from a feed additive stack ($25-35/head) to a premium prevention platform

---

## 2. The Problem

### Why This Is Urgent

Liver abscess costs the US beef industry **$256 million annually**. Prevalence has **doubled since 2010** to 21.3% -- and no one knows why. The only effective prevention, continuous tylosin feeding, faces three converging threats:

1. **Regulatory pressure.** The EU September 2026 antimicrobial restriction deadline directly impacts US beef exports. Prophylactic antibiotic use in livestock is under escalating scrutiny from FDA-CVM, USDA, and international regulators.

2. **Resistance.** The first tylosin-resistant *F. necrophorum* strains (erm(B)-positive) were isolated from abscessed livers in 2024. This was considered impossible for decades. Whether this is isolated or emerging is unknown, but 86% of commensal enterococci in tylosin-fed cattle already carry macrolide resistance genes -- the reservoir exists.

3. **Consumer and retail pressure.** Major retailers are implementing "raised without antibiotics" programs. Any feedlot selling into these markets cannot use tylosin, creating a growing population of unprotected cattle.

### Why This Is Hard

Fifty years of research and thirteen distinct intervention approaches have failed to replace tylosin. Our failure analysis reveals why:

- **pH is not the bottleneck.** Saccharomyces cerevisiae fermentation product improved rumen pH in a definitive trial (n=4,689) and had **zero** effect on liver abscess. This eliminates all pH-focused approaches as standalone solutions.

- **Broad-spectrum approaches are worse than tylosin, not better.** Chlortetracycline (broader spectrum) was significantly inferior. Essential oils **doubled** the risk. Selectivity for *F. necrophorum* at the rumen wall matters more than total antimicrobial breadth.

- **Vaccines work in principle but fail under continuous challenge.** Fusogard achieves 73% reduction on forage diets (OR=0.27) but fails on grain diets. The target (leukotoxin neutralization) is correct. The failure is dose overwhelm: antibody-mediated protection cannot keep up with 150+ days of continuous bacterial translocation from a chronically damaged rumen wall.

- **~24% of abscesses originate from the hindgut, not the rumen.** Recent 16S sequencing reveals a second abscess subtype dominated by *Bacteroides* species translocating from the cecum/colon. No intervention has ever targeted this pathway. This caps any rumen-only strategy at ~76% maximum efficacy.

- **Established abscesses are untreatable.** The fibrous capsule (>1 cm collagen) creates an avascular, anaerobic, low-pH environment that no systemic drug can penetrate. The portfolio must be 100% prevention-focused.

### The Implication

Tylosin works because it attacks the disease on at least three dimensions simultaneously: direct antimicrobial activity against *F. necrophorum* at the rumen wall, microbiome restructuring, and possibly immunomodulation. **No single-dimension intervention has ever matched it.** Any replacement must be multi-dimensional.

---

## 3. What We Did

### The Pipeline

| Phase | Agent | What it does | Output |
|---|---|---|---|
| 1 | Pathfinder | Maps the disease completely (11 stages, R0, KE#1) | Disease map with 2 translocation routes, rate-limiting barrier identification |
| 2 | Sapper | Explains why every treatment failed | 13 failures analyzed; 5 core lessons extracted |
| 3a | Forge | Proposes 27 candidates across all 11 stages | 4 categories: empirical hits, known approaches, cross-disease analogies, novel proposals |
| 3b | Surveyor | Computationally validates targets | BLAST, structure analysis, literature cross-checks; 3 critical corrections to Forge |
| 4 | Reaper | Red-team kill testing (12 kill tests per candidate) | 10 killed, 12 wounded, 7 survived |
| 4b | Board | 6-model external review + force-ranking + devil's advocate | 2 resurrections, 2 downgrades, strict force-ranking, 4 mandatory prerequisites |
| 5 | Anvil | Portfolio construction, 70% test, partner deliverables | This memo |

### External Panel

At every phase, six frontier AI models (Gemini 3.1 Pro, GPT-5.4, Grok 4, Claude Opus, DeepSeek R1, Qwen 2.5) independently reviewed the output. This is not a rubber stamp -- the panel identified three critical Surveyor corrections, argued for two Board resurrections, contested the portfolio backbone (4/6 models argued for killing MON+BX), and identified three missing kill tests that were incorporated into the de-risk sequence.

---

## 4. The Portfolio

### Force-Ranked Surviving Targets

| Rank | Candidate | Disease stage | Evidence level | Status |
|---|---|---|---|---|
| **1** | **MON+BX (monensin + tannin blend)** | Stages 1, 3 (burden reduction) | Cattle data, n=2,986, single study | SURVIVED -- conditional on independent replication |
| **2** | **rPL4 vaccine (recombinant leukotoxin + slow-release adjuvant)** | Stage 6 (immune evasion defeat) | Cattle challenge model (80% protection); zero grain-diet field data | SURVIVED -- conditional on PL4 sequence conservation + rumen fluid IgG access |
| **3** | **Hindgut intervention** | Stage 5 (hindgut translocation) | Conceptual; no LA endpoint data | SURVIVED -- contingent on KE#1 result |
| **4** | **Triple Stack (MON+BX + rPL4 vaccine)** | Stages 1, 3, 6 combined | No combination data exists | SURVIVED -- deprioritized below component validation |

### Key Wounded Candidates (Second Tranche)

| Rank | Candidate | Why it matters |
|---|---|---|
| 5 | Multi-antigen vaccine (rFomA + rPL4 + OMP adhesin) | Best long-term vaccine concept -- but must be reformulated (hemagglutinin data disputed) and requires cattle data |
| 6 | Anti-FomA mAb (reframed as mechanistic validation tool) | Not a commercial product; fastest way to validate whether blocking FomA adhesion prevents LA in cattle |
| 7 | Rumen-protected butyrate | Addresses the wide-open barrier integrity gap (Stage 2); VFA paradox unresolved |

### What Was Killed and Why

| Candidate | Kill reason |
|---|---|
| Anti-FomA mAb (commercial) | $120/head, 8 injections; economics impossible |
| Anti-leukotoxin mAb | Same economics; redundant with cheaper vaccine |
| Mucoadhesive rumen sealant | Physics -- rumen destroys polymer coatings |
| Gallium compounds | Heavy metal in food animals -- regulatory impossibility |
| TGF-beta1 modulators | Capsule CONTAINS infection; removing it spreads disease |
| PPIX biosynthesis inhibitor | Shared heme pathway causes host porphyria |
| Biofilm dispersal (in abscess) | Unproven target + delivery impossible + dispersal = bacteremia |
| Metronidazole analog | FDA class-wide ban on nitroimidazoles in food animals |
| Antiplatelet agent | Bleeding risk unacceptable |
| PDT of biofilms | Light delivery to bovine liver impossible |

---

## 5. The Decision Tree

### What Happens at Each Gate

```
GATE 0: KE#1 (Paired Abscess Typing)
  Cost: $15-20K | Timeline: 4-6 weeks
  |
  |-- If hindgut fraction >40% under tylosin:
  |     Portfolio pivots to barrier integrity + systemic approaches
  |     Hindgut intervention elevated to Rank #1
  |     Rumen-only strategies have lower ceiling than assumed
  |
  |-- If hindgut fraction <15% under tylosin:
  |     Rumen-focused strategies validated
  |     Hindgut candidates deprioritized
  |     MON+BX + vaccine combination has clear path
  |
  |-- If erm(B) resistance prevalence >5%:
  |     Urgency for non-antibiotic alternative increases
  |     Product that is 5-10 points inferior to tylosin becomes
  |     commercially attractive if tylosin is failing
  |
GATE 1: MON+BX Independent Replication
  Cost: $80-100K | Timeline: 8-10 months
  |
  |-- If MON+BX replicates (LA prevalence 25-32%):
  |     Burden reduction backbone validated
  |     Proceed to Triple Stack trial
  |
  |-- If MON+BX fails to replicate:
  |     Portfolio backbone collapses
  |     Program restructures around vaccine-only
  |     or novel antimicrobial strategies
  |
GATE 2: Vaccine Foundation Package
  Cost: $35-50K | Timeline: 8-12 weeks (parallel with Gate 1)
  |
  |-- PL4 sequence conserved + rumen IgG detectable:
  |     Vaccine strategy lives
  |     Proceed to adjuvant titer study ($50-70K)
  |
  |-- PL4 varies significantly across field strains:
  |     Single-variant PL4 vaccine is dead
  |     Must develop polyvalent or conserved-epitope approach
  |     Timeline extends 12-18 months
  |
  |-- Rumen IgG undetectable:
  |     All systemic vaccination strategies are dead for
  |     colonization prevention
  |     Vaccines can only address Stage 6 (hepatic, post-translocation)
  |     Mucosal vaccination (intranasal) gains priority
  |
GATE 3: Triple Stack Field Trial
  Cost: $150-200K | Timeline: 10-12 months
  (ONLY if Gates 1 and 2 pass)
  |
  |-- Triple Stack matches or beats MON+TYL:
  |     Commercial development candidate identified
  |     Proceed to pivotal multi-site trial
  |
  |-- Triple Stack inferior but within 5 points:
  |     Commercially viable ONLY if tylosin restricted
  |     Position as "non-antibiotic alternative"
  |
  |-- Triple Stack fails to improve over MON+BX alone:
  |     Vaccine contribution is zero on grain diets
  |     30-year pattern confirmed
  |     Program must pursue novel mechanisms
```

---

## 6. De-Risk Experiments

### Experiment 1: KE#1 -- Paired Abscess Typing (RUN FIRST)

| Parameter | Detail |
|---|---|
| **Question** | What fraction of liver abscesses under tylosin are hindgut-origin? Does tylosin selectively prevent rumen-origin LA? |
| **Design** | n=100 abscesses from tylosin-treated cattle + n=100 from untreated cattle (same feedlot, same diet, same slaughter day). 16S rRNA amplicon sequencing + culture-based quantification. |
| **Primary endpoint** | Proportion of Fusobacterium-dominated vs Bacteroidetes-dominated abscesses in each group |
| **Secondary endpoints** | F. necrophorum subspecies ratio; erm(B) resistance gene prevalence; T. pyogenes co-occurrence; abscess severity vs subtype |
| **Cost** | $15-20K (sequencing ~$50-75/sample x 200 + culture + analysis) |
| **Timeline** | 4-6 weeks (single slaughter day collection; 2-3 week sequencing; 1-2 week analysis) |
| **Practical requirement** | Access to a packing plant processing both tylosin-treated and untreated cattle from the same feedlot on the same day. Elanco's Benchmark database (68,000+ feedlots) can identify suitable sites. Abscess collection is free -- done at normal slaughter inspection. |
| **GO** | Proceed with portfolio as designed. Hindgut fraction informs candidate prioritization. |
| **KILL** | N/A -- this is pure information. All outcomes inform the portfolio; none kill the program. |

### Experiment 2: MON+BX Independent Replication

| Parameter | Detail |
|---|---|
| **Question** | Does MON+BX reduce LA prevalence vs MON+TYL in a second feedlot with an independent BX formulation? |
| **Design** | n=500, 3-arm: MON+TYL (positive control), MON+BX (test), MON-only (negative control). Randomized, pen-level assignment, blinded liver scoring. |
| **Primary endpoint** | Liver abscess prevalence at slaughter (Elanco Liver Check scoring: 0, A-, A, A+) |
| **Secondary endpoints** | Abscess 16S typing (leverages KE#1 methodology); BX anti-Fn activity in presence of feedlot-concentration dietary protein; feed efficiency; carcass merit |
| **Cost** | $80-100K |
| **Timeline** | 8-10 months (one full feeding cycle) |
| **GO threshold** | MON+BX achieves LA prevalence within 8 percentage points of MON+TYL (i.e., <27% if MON+TYL is ~19%). Liver abscess score at slaughter is the commercial endpoint. |
| **KILL threshold** | MON+BX prevalence >32% (no meaningful improvement over untreated historical controls). |

### Experiment 3: Vaccine Foundation Package

Two studies running in parallel:

#### 3A: PL4 Sequence Conservation Survey

| Parameter | Detail |
|---|---|
| **Question** | Is the PL4 leukotoxin epitope region conserved across bovine field strains? |
| **Design** | Collect >=50 F. necrophorum isolates from liver abscesses at >=3 feedlots (geographically diverse). PCR amplify PL4 region. Sequence and align. Assess epitope conservation. |
| **Cost** | $15-20K |
| **Timeline** | 6-8 weeks |
| **GO** | PL4 epitope region shows >95% sequence conservation across isolates. |
| **KILL** | Significant antigenic variation (>3 epitope variants at >10% frequency each). Single-variant vaccine cannot provide broad coverage. |

#### 3B: Rumen Fluid IgG Access Study

| Parameter | Detail |
|---|---|
| **Question** | Does systemic vaccination generate detectable anti-PL4 IgG at the rumen wall mucosal surface? |
| **Design** | Vaccinate 10 steers with existing PL4 immunogen + adjuvant. Collect paired serum and rumen fluid samples at 2, 4, 8 weeks post-vaccination. Quantify anti-PL4 IgG in both compartments by ELISA. |
| **Cost** | $20-30K |
| **Timeline** | 8-12 weeks |
| **GO** | Rumen fluid anti-PL4 IgG detectable at >=1% of serum titer. |
| **KILL** | Rumen fluid IgG undetectable or <0.1% of serum. Systemic vaccination cannot provide mucosal protection. All parenteral vaccine strategies are dead for colonization prevention. |

### Experiment 4: Adjuvant Titer Duration Study (runs only if Experiment 3 passes)

| Parameter | Detail |
|---|---|
| **Question** | Can a modern adjuvant sustain protective anti-PL4 neutralizing titers for 150+ days from 2-3 doses? |
| **Design** | 40 steers, 4 adjuvants x 10 animals, all receiving rPL4 antigen. Measure neutralizing Ab titers at 0, 30, 60, 90, 120, 150 days. |
| **Cost** | $50-70K |
| **Timeline** | 6-9 months |
| **GO** | At least one adjuvant maintains neutralizing titer above 10x the in vitro leukotoxin neutralization threshold at day 150. |
| **KILL** | No adjuvant maintains protective titers beyond day 90. The dose-overwhelm problem is unsolvable by adjuvant engineering. |

### Experiment 5: Triple Stack Field Trial (runs only if Experiments 2 and 4 pass)

| Parameter | Detail |
|---|---|
| **Question** | Does MON+BX + rPL4 vaccine match or beat MON+TYL for liver abscess prevention? |
| **Design** | n=800, 4-arm: (a) MON+TYL (positive control), (b) MON+BX (burden reduction only), (c) MON+BX + rPL4 vaccine (Triple Stack), (d) MON + rPL4 vaccine only (detects monensin-vaccine antagonism). |
| **Primary endpoint** | Liver abscess prevalence at slaughter |
| **Secondary endpoints** | Abscess severity scoring; 16S typing; feed efficiency; carcass merit; serum neutralizing Ab titer at slaughter |
| **Cost** | $150-200K |
| **Timeline** | 10-12 months |
| **GO** | Triple Stack LA prevalence within 5 percentage points of MON+TYL AND statistically superior to MON+BX alone. |
| **KILL** | Triple Stack not superior to MON+BX alone (vaccine adds nothing on grain diet). Or: vaccine-only arm (#d) shows antagonism with monensin. |

### Total De-Risk Investment

| Experiment | Cost | Timeline | Dependency |
|---|---|---|---|
| KE#1 (abscess typing) | $15-20K | 4-6 weeks | None -- runs first |
| MON+BX replication | $80-100K | 8-10 months | After KE#1 |
| PL4 sequence survey | $15-20K | 6-8 weeks | Parallel with replication |
| Rumen fluid IgG access | $20-30K | 8-12 weeks | Parallel with replication |
| Adjuvant titer study | $50-70K | 6-9 months | After Exp 3 passes |
| Triple Stack field trial | $150-200K | 10-12 months | After Exp 2 + 4 pass |
| **Total through Triple Stack gate** | **$330-440K** | **14-16 months** | Gated, not parallel |

---

## 7. Commercial Positioning

Three options depending on Elanco's strategic priority and which experiments succeed:

### Option 1: Tylosin Successor (Feed Additive Stack)

**Product:** Rumensin + optimized tannin blend (proprietary formulation)
**Route:** Oral (in-feed), continuous administration
**Target price:** $0.12-0.15/head/day = $18-23/head total (vs tylosin $0.02-0.05/day = $3-8/head)
**Positioning:** Direct replacement for tylosin in the same feed-additive channel. Non-antibiotic. Zero withdrawal period. Compatible with "raised without antibiotics" programs.
**Regulatory:** Feed additive (FDA-CVM). Tannin blends are generally recognized as safe (GRAS) or have existing feed additive approvals. Fastest regulatory path.
**Who buys:** Feedlot nutritionist prescribes; purchased through feed mill. Existing distribution channel.
**Key advantage for Elanco:** Builds on Rumensin franchise. Same customer, same channel, same call point. Elanco already has the monensin relationship.
**Key limitation:** 10-point efficacy gap vs tylosin (28.5% vs 18.3%). If gap cannot be closed below 5 points, positioning as a "replacement" is commercially awkward. Best positioned for markets where tylosin is restricted or unavailable.
**Timeline to market:** 18-24 months (if replication succeeds and formulation optimization closes the gap).

### Option 2: Premium Prevention Stack (Feed Additive + Vaccine)

**Product:** Rumensin + tannin blend (feed) + rPL4 slow-release vaccine (injectable at arrival + boost)
**Route:** Combination oral + injectable
**Target price:** $25-35/head total over feeding period
**Positioning:** Premium prevention platform. First non-antibiotic approach that addresses BOTH burden reduction AND immune evasion. Higher price justified by superior efficacy (if Triple Stack matches tylosin) and non-antibiotic status.
**Regulatory:** Feed additive component (FDA-CVM) + vaccine component (USDA-CVB). Dual regulatory pathway, but Elanco has both capabilities.
**Who buys:** Feedlot veterinarian prescribes vaccine; nutritionist prescribes feed components. Both existing Elanco call points.
**Key advantage for Elanco:** Multi-product bundle increases revenue per head. Creates competitive moat vs generic tylosin alternatives. Leverages both Rumensin franchise AND vaccine manufacturing infrastructure (Fusogard heritage, production facilities).
**Key limitation:** $25-35/head vs $3-8/head for tylosin. At 10,000 head, incremental cost = $220K-$320K/year. Only justified if tylosin is restricted, if resistance spreads, or if the premium efficacy claim is compelling.
**Timeline to market:** 3-4 years (requires vaccine development, adjuvant selection, field trials, USDA-CVB approval).

### Option 3: Next-Generation Platform (Novel Biologic)

**Product:** Fc-engineered anti-FomA monoclonal antibody (single injection, 60-90 day half-life)
**Route:** Injectable at feedlot arrival (single dose)
**Target price:** $15-25/head (aspirational; requires 20-30x cost reduction from current veterinary mAb manufacturing)
**Positioning:** First-in-class livestock monoclonal antibody for infection prevention. Technology platform applicable to multiple diseases.
**Regulatory:** USDA conditional approval pathway (precedent: Elanco's canine parvovirus mAb, 2023).
**Key advantage for Elanco:** Leverages $130M Elwood mAb manufacturing investment. Differentiates from all competitors. Creates a platform technology for livestock biologics.
**Key limitation:** Food-animal mAb manufacturing at <$25/dose has no precedent. Elwood expansion is companion-animal focused. Internal commercial assessment of food-animal mAbs appears currently negative. Cost reduction timeline is uncertain.
**Timeline to market:** 5-7 years minimum.

### Elanco-Specific Strategic Considerations

- **Elanco owns Tylan (tylosin), Rumensin (monensin), AND Fusogard.** All three are relevant to this portfolio. A non-antibiotic replacement strategy that builds on Rumensin and improves on Fusogard uses existing Elanco assets.
- **Elanco is #1 in US beef.** This is their franchise to defend.
- **The first-mover advantage is significant.** If tylosin faces regulatory restriction, the first company with a validated non-antibiotic alternative captures the entire market transition.
- **Elanco's Benchmark database (68,000+ feedlots)** is a unique asset for KE#1 site selection and for identifying high-risk populations where premium products are justified.

---

## 8. What We Are NOT Promising

### Scope Boundaries

- This portfolio addresses **prevention** of new liver abscess formation. Treatment of established abscesses is pharmacokinetically impossible and is not included.
- All efficacy estimates are for **feedlot finishing cattle on high-grain (80-95% concentrate) diets**. Results may differ for backgrounding, forage-based, or dairy cattle operations.
- The portfolio does not address the underlying cause of liver abscess (high-grain feeding). The economic model of feedlot finishing is taken as a fixed constraint.

### Key Unknowns

1. **KE#1 has not been run.** The 76/24 rumen/hindgut split comes from a single lab's 16S data. If the actual ratio is 60/40, the portfolio underweights hindgut interventions. If it is 90/10, the hindgut candidates are irrelevant. This $15-20K experiment is the single highest-value investment in the program.

2. **No vaccine has ever worked on grain diets.** The rPL4 vaccine strategy is based on the hypothesis that combining burden reduction (MON+BX) with improved vaccination can overcome the dose-overwhelm problem. This is logical but unproven. It is the central bet of the portfolio.

3. **MON+BX has one study.** The entire burden reduction backbone depends on a single trial (Felizari 2025, n=2,986). Independent replication is a mandatory prerequisite, not an optional validation.

4. **The 10-point efficacy gap may be a ceiling, not a dose issue.** If tannins' mechanism of action is primarily slowing starch fermentation (not direct anti-Fn activity at the rumen wall), no dose increase will close the gap between MON+BX and MON+TYL. The replication trial should include protein-binding saturation testing to evaluate this.

5. **Why has prevalence doubled since 2010?** No one knows. If the driver is genetic change in cattle populations (more beef-dairy crossbreds), management practices, or F. necrophorum evolution, it changes the target profile for prevention products.

6. **The leukotoxin receptor is unknown.** This is the largest basic science gap. If identified, it could enable a receptor-blocking approach that bypasses the dose-overwhelm problem entirely. But receptor identification has failed for decades, and the timeline to a commercial product from receptor ID is 5-10 years.

### What Could Go Wrong

| Risk | Impact | Mitigation |
|---|---|---|
| MON+BX does not replicate | Portfolio backbone collapses | Replication trial is the first gated investment |
| PL4 varies across field strains | Single-variant vaccine fails | PL4 sequence survey ($15-20K) runs before adjuvant investment |
| Rumen IgG is undetectable at mucosal surface | All systemic vaccines fail for colonization prevention | IgG access study ($20-30K) runs before adjuvant investment |
| Adjuvant cannot sustain titers for 150 days | Vaccine repeats Fusogard failure | Titer study ($50-70K) runs before $150-200K field trial |
| Triple Stack fails (components subadditive) | No combination matches tylosin | 4-arm trial design detects antagonism |
| erm(B) resistance spreads rapidly | Tylosin loses efficacy faster than replacement arrives | KE#1 secondary endpoint includes erm(B) prevalence screening |

### The Honest Assessment

This portfolio passes the 70% tractable pathology test only in the best-case scenario where the Triple Stack works AND a hindgut intervention is effective. The realistic case (MON+BX alone + partial vaccine contribution) covers 44-61% of tractable pathology -- below the 70% threshold.

We are not inflating these numbers. The evidence base for a non-antibiotic tylosin replacement is thinner than the field acknowledges. Fifty years of research and thirteen distinct approaches have failed to match a $3/head feed additive. The path forward is a gated investment sequence where each cheap experiment ($15-50K) either validates or kills the next expensive one ($80-200K), and where every dollar spent produces information that changes decisions.

The $330-440K total investment is not a bet on one candidate. It is a decision tree that prunes failing branches early and commits resources only when evidence justifies it. At each gate, Elanco knows whether to continue, pivot, or stop.

---

## Target Product Profiles

### TPP 1: MON+BX Feed Additive (Option 1 product)

| Parameter | Specification |
|---|---|
| **Indication** | Prevention of liver abscess in feedlot cattle on high-grain finishing diets |
| **Active ingredients** | Monensin sodium (30-33 mg/kg DM) + proprietary condensed tannin blend (dose TBD, currently 7.95 g/animal/day) |
| **Route** | Oral, continuous in-feed administration |
| **Duration** | Entire finishing period (120-180 days) |
| **Target efficacy** | LA prevalence <25% (within 7 points of MON+TYL benchmark of ~18%) |
| **Withdrawal period** | Zero (monensin: 0 days; tannins: expected 0 days as GRAS/natural product) |
| **Target price** | $0.12-0.15/head/day ($18-23/head total) |
| **Regulatory pathway** | FDA-CVM (feed additive) |
| **Stability** | Stable in TMR for 48 hours at ambient temperature |
| **Contraindications** | Not for use in horses (monensin toxicity) |
| **Competition** | Tylosin ($3-8/head, 40-70% reduction); virginiamycin (29% reduction) |

### TPP 2: rPL4 Vaccine (Component of Option 2)

| Parameter | Specification |
|---|---|
| **Indication** | Aid in prevention of liver abscess caused by F. necrophorum in feedlot cattle |
| **Active ingredient** | Recombinant PL4 leukotoxin fragment in slow-release adjuvant |
| **Route** | Subcutaneous, 2 doses: arrival + 21 days |
| **Duration of immunity** | Target: >=150 days from second dose |
| **Target efficacy** | When combined with MON+BX: LA prevalence within 5 points of MON+TYL |
| **Withdrawal period** | Standard for biologics (21 days typical) |
| **Target price** | $3-5/head (2-dose regimen) |
| **Regulatory pathway** | USDA-CVB (veterinary biological product) |
| **Storage** | 2-8C; 12-month shelf life |
| **Competition** | Fusogard (same target, failed on grain diets); no other vaccine on market |

---

*Prepared by the Agteria Overwatch discovery platform. 7-agent pipeline, 6-model external panel at every phase. All evidence claims are referenced in the accompanying Evidence Register (phase-5-evidence-register.md). Full disease map, failure analysis, candidate proposals, computational validation, kill report, and Board decision available in the program directory.*
