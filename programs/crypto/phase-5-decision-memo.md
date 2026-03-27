# Phase 5 Decision Memo: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill (Animal Nutrition & Health)
**Agent:** Anvil | **Date:** 2026-03-27 | **Version:** 1.0

---

## Executive Summary

Cryptosporidiosis caused by *Cryptosporidium parvum* is the leading infectious cause of neonatal calf diarrhea worldwide, affecting 22-34% of calves and costing the dairy industry EUR 44-61 per infected calf, plus 34 kg of lost growth at 6 months. **No effective treatment exists.** Halofuginone, the only licensed product in some EU markets, does not cure, does not improve weight gain, and has a razor-thin therapeutic index.

We evaluated 42 mechanism-level candidates across all 8 disease stages, subjected them to computational validation, 12 kill tests, and adversarial review by 6 frontier AI models. Two antiparasitic compounds emerged as the clear portfolio backbone:

1. **AN7973 (CPSF3 inhibitor):** The only compound in the world with demonstrated *cidal*, multi-stage, immunity-independent activity in neonatal calves. >99% oocyst reduction. Complete diarrhea elimination.
2. **EDI048 (CpPI4K inhibitor):** The most advanced compound (Novartis Phase 2 for humans). Gut-restricted by design. 70-fold safety margin. Rapid diarrhea resolution in calves. Cidal-vs-static mechanism unresolved.

Cargill's proprietary opportunity is **anti-P23 egg yolk antibodies (IgY)** --- targeting a CRISPR-validated essential surface protein, manufactured as a spray-dried oral supplement squarely within Cargill's capabilities.

**The investment ask:** $108-142K for three sequenced de-risk experiments over 14-18 weeks that resolve the three biggest unknowns: (1) whether EDI048 kills or merely arrests parasites, (2) whether AN7973's unprecedented calf efficacy replicates independently, and (3) whether anti-P23 IgY is a real product.

**The honest number:** The portfolio achieves an estimated 46% coverage of tractable pathology (realistic) to 68% (optimistic). It does not pass the 70% threshold. This reflects the frontier of global science against a disease that has defeated 18 treatment approaches over 40 years. The de-risk experiments determine whether the portfolio can reach the threshold.

---

## The Problem: Why Cryptosporidiosis Is Unsolved

### The Disease

*Cryptosporidium parvum* is the dominant cause of neonatal calf diarrhea worldwide. It infects calves in a 2-3 week window of maximum vulnerability (days 3-21 of life), when the immune system is profoundly immature and passive colostral immunity is waning. A single infected calf sheds 39 billion oocysts --- each one immediately infectious, resistant to chlorine and virtually all common disinfectants, and requiring only 10-30 oocysts to establish a new infection. The basic reproduction number (R0) is estimated at 5-15 in managed facilities.

### Why Every Treatment Has Failed

We forensically analyzed 18 treatment approaches. Every failure maps to one of three biological barriers:

1. **The epicellular niche blocks drug access.** *C. parvum* occupies a unique position --- intracellular but extracytoplasmic --- at the apical surface of intestinal epithelial cells. It is shielded from both luminal and systemic drugs by the parasitophorous vacuole, electron-dense band, and feeder organelle complex.

2. **Drug efficacy depends on immune cooperation that neonatal calves cannot provide.** The CD4+ T cell / IFN-gamma response required for parasite clearance does not mature until 2-3 weeks of age. Every drug tested to date shows dramatically reduced efficacy in immunocompromised hosts (nitazoxanide in HIV patients, clofazimine in the CRYPTOFAZ trial).

3. **The autoinfection cycle restarts infection from intracellular reservoirs.** Approximately 20% of oocysts produced are thin-walled, excysting within the host and reinfecting new enterocytes. This internal amplification loop defeats any cryptostatic drug upon withdrawal.

These three barriers are synergistic. No single-agent, single-mechanism approach has overcome their convergence.

### The Economic Impact

- **Per-calf cost (Europe):** EUR 44-61 per infected calf (Belgium, France, Netherlands)
- **Growth loss:** 34 kg at 6 months in severely affected calves (P=0.034), with no catch-up growth
- **Mortality:** 7-35% depending on management and co-infection
- **Labor:** EUR 1,478-2,874 per farm in additional labor costs
- **Zoonotic risk:** Calves are the only major animal reservoir for *C. parvum* infections in humans (Milwaukee 1993: 403,000 cases)

---

## What We Did

### Process

This program was run through Agteria's 7-agent drug discovery pipeline with 6-model adversarial review at every phase:

| Phase | Agent | Output |
|-------|-------|--------|
| 1 | Pathfinder | Complete disease map (8 stages, R0 estimation, KE#1 identification) |
| 2 | Sapper | Failure analysis of 18 treatments with specific biological mechanisms |
| 3 | Forge | 42 mechanism-level candidates across all 8 disease stages |
| 3b | Surveyor | Computational validation (conservation, host homology, structure, annotation) |
| 4 | Reaper | 12 kill tests per candidate: 11 survived, 19 wounded, 12 killed |
| 4b | Board | External review integration, devil's advocate, force-ranking, priority de-risk |
| 5 | Anvil | Portfolio assembly, 70% test, evidence register, decision memo |

### Quality Controls

- **6-model external adversarial review** at Phases 1, 3, and 4 (Claude, GPT-5.4, Gemini, Grok, DeepSeek, Claude Opus)
- **40 quality standards** applied throughout, including citation verification, evidence tiering, species tagging, and commercial reality gates
- **10 operating principles** enforced, with explicit attention to the 70% pathology coverage test and the "discomfort is a signal" principle
- **14 Sapper constraints** derived from failure analysis, applied to every candidate

---

## The Portfolio

### Board Force-Ranking

| Rank | Target | Why | Cargill Role |
|------|--------|-----|-------------|
| **#1** | **AN7973 (CPSF3 inhibitor)** | Only CIDAL + multi-stage + immunity-independent compound in the world with calf efficacy. >99% oocyst reduction. Complete diarrhea elimination. | License from academic/global health developer. Veterinary clinical development + market access. |
| **#2** | **EDI048 (CpPI4K inhibitor)** | Most advanced compound (Novartis Phase 2 human). Gut-restricted. 70-fold safety margin. Calf efficacy demonstrated. | License veterinary rights from Novartis. Clinical development + market access. |
| **#3** | **Anti-P23 IgY** | CRISPR-validated essential target. Egg-based IgY, spray-dried, oral supplement. Cargill can own, manufacture, and sell without a pharma partner. | **100% Cargill-owned.** Development, manufacturing, distribution. |

### Target Product Profiles

#### AN7973 --- Oral Calf Anti-Crypto Treatment

| Parameter | Specification |
|-----------|---------------|
| **Indication** | Treatment of clinical cryptosporidiosis in neonatal dairy and beef calves (3-21 days of age) |
| **Route** | Oral drench or paste (compatible with milk/milk replacer delivery) |
| **Dose** | 25 mg/kg once daily for 7 days (dose optimization needed --- may reduce to 10-15 mg/kg) |
| **Target price** | <$20-30/treatment course |
| **Withdrawal** | TBD --- requires FDA-CVM NADA or equivalent |
| **Regulatory** | FDA-CVM New Animal Drug Application (NADA) --- novel active ingredient |
| **Who buys** | Veterinarian prescribes; producer administers |
| **GO threshold** | >90% oocyst reduction vs vehicle AND diarrhea days reduced by >50% vs halofuginone AND weight gain at day 30 within 2 kg of uninfected controls |
| **KILL threshold** | <50% oocyst reduction in independent trial OR resistance mutations within 5 in vitro passages OR neonatal safety signal |

**Embarrassment pass:** "We license AN7973, reformulate for calves, and discover the benzoxaborole degrades in the abomasum to <10% active drug. The 25 mg/kg dose worked because it was massively over-dosed. At COGS-viable doses, it doesn't work."

**Kill criteria (pre-defined):** (1) Independent calf trial shows <50% oocyst reduction. (2) In vitro resistance emerges in <10 passages at sub-IC50 concentration. (3) Benzoxaborole stability in simulated abomasal fluid <20% after 30 minutes.

#### EDI048 --- Oral Calf Anti-Crypto Treatment (Gut-Restricted)

| Parameter | Specification |
|-----------|---------------|
| **Indication** | Treatment of clinical cryptosporidiosis in neonatal dairy and beef calves (3-21 days of age) |
| **Route** | Oral (gut-restricted by design --- engineered for rapid hepatic inactivation) |
| **Dose** | 10 mg/kg BID for 7 days |
| **Target price** | <$20-30/treatment course |
| **Withdrawal** | TBD --- requires FDA-CVM NADA |
| **Regulatory** | FDA-CVM NADA --- novel active ingredient |
| **Who buys** | Veterinarian prescribes; producer administers |
| **GO threshold** | CIDAL in time-kill assay (>2 log reduction, no recrudescence) AND >90% oocyst reduction in independent calf trial AND weight gain at day 30 within 2 kg of uninfected controls |
| **KILL threshold** | Static mechanism (recrudescence within 3 days of washout) converts EDI048 from standalone to combination-partner only. Not a complete kill, but changes the TPP to a combination ingredient. |

**Embarrassment pass:** "We license EDI048 from Novartis for veterinary use, spend $500K on calf trials, and discover PI4K inhibition is static. We've built a more expensive halofuginone."

**Kill criteria (pre-defined):** (1) Time-kill assay shows <1 log reduction at 48h + rapid recrudescence = STATIC. Drops to combination-partner. (2) Novartis declines veterinary license = commercially dead regardless of biology.

#### Anti-P23 IgY --- Oral Supplement / Feed Additive

| Parameter | Specification |
|-----------|---------------|
| **Indication** | Reduction of clinical signs and oocyst shedding from cryptosporidiosis in neonatal calves, used as adjunct to antiparasitic treatment |
| **Route** | Oral --- spray-dried powder in milk replacer, colostrum supplement, or standalone oral paste |
| **Dose** | TBD (Cho et al. 2025 protocol --- requires independent replication and dose optimization) |
| **Target price** | <$5-10/treatment course |
| **Withdrawal** | None expected --- IgY is a food-grade protein. Regulatory pathway: feed additive (21 CFR, AAFCO) or USDA-CVB biologic |
| **Regulatory** | Feed additive (simplest) or USDA-CVB conditional license |
| **Who buys** | Producer purchases directly; no veterinary prescription required |
| **GO threshold** | Significant diarrhea reduction + oocyst reduction confirmed independently AND IgY binds IIa and IId P23 with <5-fold affinity difference AND COGS <$5/dose |
| **KILL threshold** | No significant effect in independent trial OR IgY binding to IId P23 >10-fold weaker (geographic limitation) OR COGS >$15/dose |

**Embarrassment pass:** "We develop anti-P23 IgY, sell it on US dairy farms (IIa-dominant), and it works. We expand to Middle Eastern/European markets (IId-dominant) and it fails --- the P23 repeat epitope is different."

**Kill criteria (pre-defined):** (1) Independent replication fails. (2) Subtype cross-reactivity fails (>10-fold affinity drop for IId). (3) COGS analysis shows >$15/dose at scale.

---

## De-Risk Experiments

### Board's Priority De-Risk Sequence

Three experiments, sequenced to maximize information value per dollar. Each result changes what happens next.

#### Experiment 1: EDI048 Cidal-vs-Static Determination

| Parameter | Detail |
|-----------|--------|
| **Design** | Time-kill curve assay of EDI048 against *C. parvum* in bovine ALI intestinal organoids. Multiple concentrations (0.1x, 1x, 10x EC50). Measure parasite viability at 6h, 12h, 24h, 48h, 72h. Washout at 48h, measure recrudescence at 7 days. |
| **Cost** | **$8,000-12,000** |
| **Timeline** | **4-6 weeks** |
| **GO** | >2 log reduction in viable parasites at 48h; no recrudescence at 7 days post-washout |
| **KILL** | <1 log reduction at 48h + rapid recrudescence = STATIC. EDI048 drops to combination-partner. AN7973 becomes sole backbone. Full drug-vs-IFN-gamma trial (KE#1 Phase B) becomes urgent. |
| **What you learn if it PASSES** | EDI048 is cidal. It is unambiguously the #1 compound. The de-risk sequence accelerates. Cargill's Novartis licensing discussion strengthens. |
| **What you learn if it FAILS** | EDI048 is a more expensive halofuginone. AN7973 becomes the sole cidal agent. The portfolio depends on a single compound. Combination strategy becomes mandatory. |

**Why first:** This is the single cheapest experiment that restructures the entire portfolio. Every dollar spent on EDI048 before knowing cidal-vs-static is a dollar risked on the halofuginone failure mode.

#### Experiment 2: AN7973 Independent Calf Replication + Resistance Selection

| Parameter | Detail |
|-----------|--------|
| **Design** | Two parallel studies: (a) Independent neonatal calf efficacy trial (n=8-10 per group: vehicle, AN7973 at 15 and 25 mg/kg, halofuginone comparator). Challenge with field isolate (IIa subtype). Endpoints: oocyst clearance (qPCR), diarrhea days, weight at day 30. (b) In vitro resistance selection in ALI organoid system for serial passages at sub-inhibitory AN7973. Sequence CPSF3 at each passage. |
| **Cost** | **$60,000-80,000** |
| **Timeline** | **10-14 weeks** (calf trial + resistance selection in parallel) |
| **GO** | >90% oocyst reduction confirmed independently; no resistance mutations in 10+ passages |
| **KILL** | Efficacy <50% in independent lab OR resistance mutations within 5 passages |
| **What you learn if it PASSES** | AN7973's unprecedented efficacy is real. Resistance barrier is high. Cargill has a validated lead compound to seek licensing for. |
| **What you learn if it FAILS** | The sole confirmed cidal agent may be artifactual (replication failure) or vulnerable to rapid resistance. Catastrophic for the portfolio --- triggers re-evaluation of deferred candidates (B1/BRD7929, B5/CpPDE1). |

**Why second:** Six independent AI models unanimously flagged single-lab dependency as a portfolio-level systemic risk. Independent replication is mandatory before committing >$100K.

#### Experiment 3: Anti-P23 IgY Independent Replication + Subtype Cross-Reactivity

| Parameter | Detail |
|-----------|--------|
| **Design** | (a) Independent neonatal calf trial reproducing Cho et al. 2025 protocol (n=8-10 per group). (b) ELISA/SPR binding assay of anti-P23 IgY against recombinant P23 from IIa and IId subtypes. |
| **Cost** | **$40,000-50,000** |
| **Timeline** | **10-14 weeks** |
| **GO** | Significant diarrhea + oocyst reduction confirmed independently; IgY binds IIa and IId P23 with <5-fold affinity difference |
| **KILL** | No significant effect in independent trial OR IgY binding to IId >10-fold weaker |
| **What you learn if it PASSES** | Cargill has a proprietary anti-crypto product it can develop, manufacture, and sell without a pharma partner. |
| **What you learn if it FAILS** | Cargill has no proprietary product. The company is entirely dependent on pharma licensing for any crypto intervention. |

### Total Investment and Timeline

| | Cost | Timeline |
|---|------|---------|
| Experiment 1 | $8-12K | Weeks 0-6 |
| Experiment 2 | $60-80K | Weeks 0-14 (parallel) |
| Experiment 3 | $40-50K | Weeks 0-14 (parallel) |
| **Total** | **$108-142K** | **14-18 weeks** |

### Decision Tree

```
Week 0:  Start all 3 experiments in parallel
         Begin Novartis licensing discussions (critical path, takes months)

Week 6:  Experiment 1 results
         |
         EDI048 CIDAL -----> EDI048 = backbone #1
         |                   Novartis license = highest priority
         |
         EDI048 STATIC ----> AN7973 = sole backbone
                             Combination (EDI048+AN7973) becomes mandatory
                             Run KE#1 Phase B (drug + IFN-gamma trial, $15-20K)

Week 14: Experiments 2 + 3 results
         |
         AN7973 replicates -----> Validated lead compound. Seek licensing.
         AN7973 fails ----------> CATASTROPHIC. Reactivate deferred candidates.
         |
         IgY replicates --------> Cargill proprietary product. Proceed to scale-up.
         IgY fails -------------> Cargill has no proprietary crypto product.

Week 18: Integration. Final portfolio composition known.
         Decide: which compounds to license, what Cargill builds in-house,
         what the combination protocol looks like.
```

---

## Commercial Positioning for Cargill

### What Cargill Brings to This Program

Cargill is not a pharmaceutical company. Its value in this program is NOT compound development. It is:

1. **Veterinary clinical trial infrastructure** --- the ability to run large-scale, GLP-compliant calf trials on commercial dairy operations
2. **Market access** --- feed and nutrition distribution channels reaching >80% of US dairy operations
3. **Manufacturing capability** for oral supplements, feed additives, colostrum products, milk replacers
4. **The commercial relationship** with dairy producers who need solutions

### Three Positioning Options

**Option 1: Crypto Management System (Bundle)**

Cargill develops a comprehensive crypto management protocol combining:
- Licensed antiparasitic (EDI048 or AN7973) as the backbone treatment
- Proprietary anti-P23 IgY as a co-administration supplement
- Crypto-optimized milk replacer (lactose-reduced, caloric-balanced)
- Enhanced ORS (glycine/glutamine formulation)
- Colostrum quality standards

This positions Cargill as the one-stop solution provider, not just a drug distributor. The bundle creates lock-in and allows margin capture across multiple product categories.

**Option 2: Licensing Play**

Cargill licenses veterinary rights to EDI048 (from Novartis) and/or AN7973 (from academic/global health partners) and develops them as standalone veterinary products. Anti-P23 IgY is developed as a complementary product. This is the highest-value play if licensing succeeds, but it depends entirely on pharma partners granting veterinary rights.

**Option 3: Proprietary-Only (Fallback)**

If licensing fails for both antiparasitic compounds, Cargill develops its own product layer:
- Anti-P23 IgY oral supplement (if replication succeeds)
- Crypto-optimized nutrition products (milk replacer, ORS, colostrum)
- This is a supportive care package, not a treatment. Coverage ~15-25%. Honest but commercially limited.

**Recommendation:** Pursue Option 1. Begin Novartis discussions immediately (parallel with science). The commercial access question is on the critical path.

### The Novartis Licensing Question

**This must be flagged prominently.** Cargill's path to the antiparasitic backbone --- the essential component without which the portfolio fails --- almost certainly runs through licensing.

- **EDI048:** Owned by Novartis. Phase 2 recruiting for human paediatric use (NCT07249463). Novartis has NO veterinary development program. Cargill's pitch: "We provide the veterinary development path and market access you don't have. You focus on human paediatrics. We develop the calf formulation. Shared upside in the largest unmet need in calf health."

- **AN7973:** Developed by academic groups funded by global health organizations (MMV, DNDi). No commercial owner in the veterinary space. Licensing or co-development agreement with the academic developers.

**The risk:** Novartis may decline (40-50% probability per Board estimate). If both compounds are inaccessible, the portfolio collapses to supportive care + IgY. Begin discussions NOW. Do not wait for experiment results.

---

## What We Are NOT Promising

1. **We are not promising a cure.** No compound in the world achieves sterilizing cure of neonatal calf cryptosporidiosis. AN7973's >99% oocyst reduction is extraordinary but not 100%. Recovery depends on the calf's own immune maturation at 2-3 weeks of age.

2. **We are not promising 70% pathology coverage.** The honest number is 46% (realistic) to 68% (optimistic). The disease biology --- epicellular niche, autoinfection, neonatal immune incompetence --- creates barriers that current science has not fully overcome.

3. **We are not promising that Cargill can develop the antiparasitic backbone alone.** EDI048 and AN7973 require pharma licensing. Cargill's independent capabilities cover the IgY product and the nutrition layer, not the drug backbone.

4. **We are not promising timelines.** Veterinary approval of a novel antiparasitic is a 3-5 year process (FDA-CVM NADA). The full combination product is a 5-10 year horizon.

5. **We are not promising the de-risk experiments will succeed.** There is a 15-20% probability that AN7973 fails independent replication (catastrophic), a 30-40% probability that EDI048 is static (portfolio restructuring), and a 25-30% probability that anti-P23 IgY fails replication (loss of Cargill proprietary product).

---

## The Honest Number

**Coverage of tractable pathology:** 46.3% (realistic), 68% (optimistic).

**What this means:** If every candidate in the portfolio works as well as current evidence suggests, approximately half of the disease burden addressable by pharmaceutical intervention would be covered. The remaining half is driven by the autoinfection cycle, the neonatal immune gap, and the impossibility of achieving sterilizing cure with any available compound.

**Why this is still worth pursuing:** Halofuginone --- the only licensed product --- provides approximately 15-20% coverage and does not cure. Moving from 15-20% to 46-68% would be the largest advance in calf cryptosporidiosis treatment in 40 years. It would mean the difference between a disease with no effective treatment and a disease with a treatment that resolves diarrhea, reduces shedding by >99%, and protects weight gain.

**The $108-142K investment buys answers, not promises.** In 14-18 weeks, Cargill will know:
- Whether the best compound in the world is cidal or static
- Whether the unprecedented calf efficacy data is real
- Whether Cargill has a proprietary product

Those answers are worth the investment regardless of the outcomes.

---

## SCC Equivalent for Cryptosporidiosis

For mastitis, the commercially relevant clinical endpoint is somatic cell count (SCC). For cryptosporidiosis, the equivalent composite endpoint is:

**GO threshold for any candidate must include ALL THREE:**
1. **Oocyst shedding reduction** (quantified by qPCR) --- >=90% reduction vs vehicle
2. **Diarrhea score improvement** --- >=50% reduction in diarrhea days vs halofuginone comparator
3. **Weight gain** --- body weight at day 30 within 2 kg of age-matched uninfected controls

Oocyst reduction without clinical improvement is not a commercial product. Diarrhea improvement without weight recovery is not a cure. All three must be satisfied.

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| EDI048 is static | 30-40% | HIGH | Experiment 1 ($8-12K, 4-6 weeks) |
| AN7973 fails independent replication | 15-20% | CATASTROPHIC | Experiment 2 ($60-80K, 10-14 weeks) |
| Anti-P23 IgY fails replication | 25-30% | MODERATE | Experiment 3 ($40-50K, 10-14 weeks) |
| Novartis declines EDI048 veterinary license | 40-50% | HIGH | Begin discussions immediately. Parallel-track. |
| AN7973 dose commercially unviable (25 mg/kg) | 30-40% | MODERATE | Dose optimization post-replication |
| Both antiparasitics inaccessible to Cargill | 20-30% | CATASTROPHIC | IgY becomes only asset. Explore deferred candidates. |
| P23 subtype polymorphism limits IgY | 25-35% | MODERATE | Experiment 3b (binding assays) |
| Rapid AN7973 resistance under selection | 10-15% | HIGH | Experiment 2b (resistance selection) |
| Anorexic calves refuse oral treatment | 20-30% | MODERATE | Paste/drench formulation alongside milk-replacer delivery |

---

## Appendix: Fallback Logic

**If the lead thesis (antiparasitic backbone + IgY + nutrition) fails:**

| Scenario | Trigger | Fallback |
|----------|---------|----------|
| AN7973 fails replication | Experiment 2 KILL | Reactivate BRD7929/PheRS (cured immunosuppressed mice, combination-only). Reactivate CpPDE1 (CRISPR-validated, new target). Reactivate lapaquistat/GSH axis (host-directed, resistance-proof). |
| EDI048 static + AN7973 fails | Both backbone compounds compromised | Emergency pivot to MMV665917 (target ID first). BKI-1708 as combination partner. Host-directed approaches (lapaquistat, NOD2/IL-22) as exploratory. |
| Anti-P23 IgY fails | Experiment 3 KILL | Reactivate hyperimmune colostrum (rC7 antigen --- backup passive antibody). Evaluate VHH nanobodies against Cp-P34 (alternative surface target). |
| All three fail | Experiments 1-3 all KILL | The portfolio collapses to supportive care. Escalate to Daniel. Consider whether the disease is addressable with current science. |
| Novartis declines license | Business failure, not science | Pursue AN7973 licensing aggressively. Explore BKI-1708 (CDPK target, pharma development groups at multiple institutions). Consider host-directed approaches that Cargill can own. |

---

*Phase 5 Decision Memo v1.0 --- Cryptosporidiosis in Neonatal Calves*
*Cargill (Animal Nutrition & Health)*
*Portfolio: 3 assets (AN7973, EDI048, anti-P23 IgY) + nutrition layer*
*Investment: $108-142K for 3 de-risk experiments over 14-18 weeks*
*Coverage: 46% realistic, 68% optimistic (does not pass 70% test)*
*Critical path: Novartis licensing discussion (begin immediately)*
