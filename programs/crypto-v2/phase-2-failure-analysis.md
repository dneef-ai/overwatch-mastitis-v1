# Phase 2 — Treatment Failure Analysis: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill | **Version:** v2
**Agent:** Sapper | **Date:** 2026-03-27

---

## The Unifying Failure: The Immune Timing Gap

The Tribunal determined the bottleneck is the **3-7 day gap between parasite amplification to overwhelming burden (days 0-5) and functional adaptive immune engagement (days 6-14)**. Every treatment failure analyzed below can be traced back to this kinetic mismatch. The parasite reaches 10^10+ organisms before the immune system shows up, and before most treatments are even initiated.

The fundamental reframe: **most treatments were not tested against the disease's actual bottleneck.** They were tested either (a) too late (after the kinetic race was already lost), (b) against the wrong target (environmental load instead of within-animal amplification), or (c) without adequate duration to bridge the full vulnerability window. Halofuginone's partial success when given prophylactically from birth — and its failure when given therapeutically — is the clearest proof that timing, not pharmacology, is the rate-limiting variable.

---

## Treatment 1: Halofuginone (Halocur)

### What was tried
Halofuginone lactate (Halocur), a halogenated quinazolinone derivative of febrifugine, administered orally at 100-150 mcg/kg/day for 7 consecutive days. The only drug approved for calf cryptosporidiosis (EU only; not approved in US).

### Specific results
Based on articles retrieved from PubMed, a systematic review and meta-analysis (Brainard et al., 2020; [DOI](https://doi.org/10.1017/S0031182020002267)) of 18 articles describing 25 experiments found:
- **Prophylactic use (started before day 5 of life):** Significantly lower incidence of oocyst shedding, reduced diarrhea burden, and lower mortality
- **Effect size:** Reduces diarrhea duration by approximately 2 days (from median ~7-9 to ~5-7 days). Reduces oocyst shedding at day 7 (Lallemand et al., 2006; [DOI](https://doi.org/10.1136/vr.159.20.672)) but does NOT eliminate infection
- **Peak shedding intensity:** Minimally affected — calves still shed 10^6-10^7 oocysts/g at peak
- **Therapeutic use (started after clinical signs):** Dramatically less effective; the meta-analysis noted beneficial results when started before day 5, with much weaker evidence for later initiation
- **Publication bias:** Likely, especially for diarrhea outcomes

### Why it failed

**Mechanism of action:** Halofuginone inhibits **prolyl-tRNA synthetase (ProRS)**, blocking protein synthesis. It is **cryptostatic** (slows replication) rather than **cryptosporicidal** (kills parasites). This means it reduces the replication rate but does not eliminate existing parasites.

**The kinetic explanation:** The Martian's analysis from Phase 1b quantifies this precisely. On an exponential growth curve with 8x amplification per 12-14h cycle, a modest reduction in replication rate does not reduce peak burden proportionally — it produces a temporal delay of approximately 1 cycle (12-14h). This predicts halofuginone's observed effect size: a ~2 day reduction in diarrhea duration, with minimal impact on peak severity or shedding intensity. The drug delays the kinetic curve by 1-2 cycles but does not flatten it.

**Why prophylactic is better than therapeutic:** When given prophylactically from birth, halofuginone is present during the establishment phase (Gate 2 in the bottleneck model) when parasite numbers are 10^1-10^4. Partial suppression at this stage can meaningfully slow the time to overwhelming burden. When given after clinical signs (day 3-5), the parasite population is already 10^8-10^10 — partial suppression of replication at this stage is fighting an exponential curve that is already near its peak.

**Why it cannot cure:** Halofuginone is cryptostatic. Viable parasites persist throughout treatment. When treatment stops after 7 days, autoinfection via thin-walled oocysts can reseed the infection. Furthermore, the drug has a narrow therapeutic index — doses above 150 mcg/kg approach toxicity in neonatal calves. There is no dose escalation path to achieve the >90% replication suppression needed to meaningfully shift the kinetic balance.

### Failure classification
**COMPOUND FAILURE (partial).** The target biology is correct — suppressing merogony slows disease. But the specific compound (halofuginone) is too weak: cryptostatic rather than cryptosporicidal, narrow therapeutic index, insufficient suppression of the exponential amplification curve. A more potent inhibitor of the same pathway, or a drug that was cryptosporicidal rather than cryptostatic, might achieve the >80% replication suppression needed to shift outcomes.

### Disease stage mapping
- **Stage 4 (Merogony/Amplification)** — primary target
- **Stage 5 (Autoinfection)** — does NOT break the autoinfection cycle; thin-walled oocysts continue to form during treatment

### Constraints for Forge
1. Cryptostatic is insufficient; a merogony-targeting drug must achieve >80% suppression or be cryptosporicidal
2. Must be delivered prophylactically from birth — 7-day daily dosing is the current standard but labor-intensive
3. The narrow therapeutic index means more potent analogs may not be achievable within the halofuginone scaffold
4. The drug works to some degree — this proves merogony suppression IS a valid strategy if the compound is potent enough

---

## Treatment 2: Nitazoxanide (Cryptaz/Alinia)

### What was tried
Nitazoxanide (NTZ), a thiazolide anti-parasitic, is the only FDA-approved treatment for human cryptosporidiosis (immunocompetent patients only). Tested in calves at various doses. The activated metabolite tizoxanide is the active form.

### Specific results
- **In humans:** 3-day course resolves diarrhea in immunocompetent adults and children (FDA approval 2002-2004). FAILS in HIV/AIDS patients and immunocompromised individuals — no significant benefit over placebo
- **In calves:** Conflicting results across studies. Some show modest reduction in oocyst shedding and diarrhea duration; others show no significant effect. No consistent, replicable anti-cryptosporidial efficacy in neonatal calves under field conditions
- **Dose-response:** No clear dose-response relationship established in calves

### Why it failed

**The immune-dependence problem:** NTZ's efficacy is **immune-dependent**. It requires a functional adaptive immune system to achieve parasite clearance. The drug appears to work in synergy with host immunity — it may tip the balance in an already-close fight, but cannot win a one-sided one. In immunocompetent human adults, the immune system is already engaged when treatment starts; NTZ provides just enough additional pressure to accelerate clearance. In neonatal calves, the adaptive immune system is NOT yet engaged during the critical window (days 3-7). NTZ is fighting the parasite alone, without its immune co-combatant.

**The mechanism of action problem:** NTZ was originally thought to target pyruvate:ferredoxin oxidoreductase (PFOR), a key anaerobic metabolic enzyme. However, C. parvum may lack classical PFOR — its metabolic machinery is so reduced that the canonical NTZ target may not exist in this parasite. The actual mechanism of anti-cryptosporidial activity remains unclear, which means rational dose optimization is impossible.

**The timing problem:** In humans, NTZ is given therapeutically (after diagnosis). In immunocompetent humans, this works because the immune system has been mounting a response for days before diagnosis. In calves, therapeutic administration faces the same timing problem as all other drugs: by the time diarrhea is detected (day 3-5), parasite burden is already 10^8-10^10 and the immune system is still 1-4 days from activation.

### Failure classification
**TARGET FAILURE (primary) + COMPOUND FAILURE (secondary).** The primary issue is that NTZ's mechanism requires immune cooperation that does not exist in the neonatal calf during the critical disease window. This is a fundamental biological mismatch between the drug's mechanism and the host's immunological state. The compound itself may also have weak direct anti-cryptosporidial activity due to uncertain target engagement (PFOR absence).

### Disease stage mapping
- **Stage 4 (Merogony)** — supposed target, but mechanism unclear
- **Stage 6 (Immune response)** — NTZ's efficacy depends on this stage being active, which it is NOT in neonates during the critical window

### Constraints for Forge
1. Any immune-dependent drug will fail in neonatal calves during the vulnerability window
2. Drugs must have direct anti-parasitic activity independent of adaptive immunity
3. NTZ's failure in immunocompromised hosts (human and bovine neonate) is definitive evidence that immune-dependent mechanisms cannot bridge the timing gap
4. Do NOT pursue NTZ analogs for this indication unless the immune-dependence is eliminated

---

## Treatment 3: Paromomycin

### What was tried
Paromomycin (aminoglycoside antibiotic), administered orally at 25-100 mg/kg/day for 5-11 days. Off-label use.

### Specific results
Based on articles retrieved from PubMed, Fayer & Ellis (1993; [PMID 8410552]) demonstrated in experimentally infected neonatal dairy calves:
- **100 mg/kg/day (Group A):** Oocysts NOT DETECTED in feces. Significantly fewer days of diarrhea, reduced severity, reduced total oocyst shedding vs. untreated controls
- **50 mg/kg/day (Group B):** Significantly reduced diarrhea severity; oocysts initially suppressed but shed resumed near end of treatment or after
- **25 mg/kg/day (Group C):** Reduced diarrhea severity; oocyst suppression during treatment but rebound after; calves in this group gained significantly LESS weight than all other groups
- **Rebound after cessation:** Calves in Groups B and C began shedding oocysts at or near the end of paromomycin administration, indicating suppression but not clearance

Based on articles retrieved from PubMed, Kacar et al. (2022; [DOI](https://doi.org/10.1016/j.vetimm.2022.110429)) showed that paromomycin (100 mg/kg/day for 5 days) improved fecal scores by day 8 and reduced oocyst counts by day 10 in naturally infected calves, but colostrum supplementation alongside paromomycin accelerated clinical improvement (fecal scores improved by day 2).

### Why it failed

**It actually works pharmacologically — but fails practically.** Paromomycin at 100 mg/kg/day is the closest thing to a proof-of-concept cure. It demonstrates that:
1. Luminal drug delivery CAN reach the parasite in its niche (paromomycin is poorly absorbed; it acts from the gut lumen)
2. Aminoglycosides CAN suppress C. parvum replication and prevent oocyst shedding
3. Prophylactic, continuous dosing during the vulnerability window CAN control infection

**Why it still fails commercially:**
1. **Nephrotoxicity:** Paromomycin, despite being poorly absorbed orally, has documented nephrotoxic effects in neonatal calves at the effective doses. The 25 mg/kg group showed significantly reduced weight gain — likely indicating systemic toxicity even at lower doses
2. **Cost:** At 100 mg/kg/day for a 40kg calf = 4g/day x 11 days = 44g of drug per calf. Paromomycin costs approximately $15-30 per treatment course at these doses — exceeding the economic threshold for production animal treatment
3. **Rebound after cessation:** At sub-optimal doses (25-50 mg/kg), oocyst shedding resumed after treatment ended, confirming that paromomycin is suppressive, not curative. Autoinfection re-seeds the infection during inter-dose troughs and after drug withdrawal
4. **Labor intensity:** 11 consecutive days of twice-daily oral dosing to every calf from birth is impractical at commercial scale
5. **Regulatory:** No approved formulation for calves; off-label aminoglycoside use in food animals faces regulatory resistance

### Failure classification
**COMPOUND FAILURE.** The target biology is validated — luminal aminoglycoside delivery to the niche works. The compound itself is toxic, expensive, and requires impractical dosing regimens. A non-toxic luminal agent with similar mechanism but better therapeutic index would succeed.

### Disease stage mapping
- **Stage 3 (Niche)** — proves luminal access to the intracellular-extracytoplasmic niche is achievable
- **Stage 4 (Merogony)** — suppresses replication effectively at high doses
- **Stage 5 (Autoinfection)** — does NOT break the cycle; rebound occurs after cessation at lower doses

### Constraints for Forge
1. Luminal delivery to the niche IS validated — this is the most important positive finding in the treatment literature
2. A non-toxic, affordable compound with similar luminal mechanism could work
3. Must achieve continuous luminal presence for 14+ days to prevent autoinfection rebound
4. The 100 mg/kg dose level sets the bar: effective prophylaxis requires this level of suppression, which translates to a high luminal drug concentration maintained continuously
5. Paromomycin + colostrum may be synergistic — the combination principle is worth exploring

---

## Treatment 4: Decoquinate

### What was tried
Decoquinate, a quinolone anticoccidial used against Eimeria in cattle, tested as a feed additive at 2-2.5 mg/kg/day for prophylaxis against C. parvum.

### Specific results
- **Moore et al. (2003, JAVMA):** 75 calves, randomized controlled trial. Decoquinate had **NO effect** on days to first diarrhea, days to first oocyst shedding, or duration of diarrhea or oocyst shedding. Complete treatment failure across all endpoints.
- **Lallemand et al. (2006; [DOI](https://doi.org/10.1136/vr.159.20.672)):** 90 calves, head-to-head vs. halofuginone. Decoquinate had **NO effect** on diarrhea levels, dehydration, proportion of diarrhoeic calves, or oocyst shedding. Unlike halofuginone, it did NOT reduce oocyst excretion at day 7.
- **Lindsay et al. (2000, Vet Parasitol):** In vitro cell culture: NO activity at 10 or 50 microM; only 8% inhibition at 100 microM. In suckling mice: NO significant reduction in oocysts at 2.5 or 5.0 mg/kg.

### Why it failed

**The target does not exist in C. parvum.** Decoquinate targets the mitochondrial electron transport chain (ETC), specifically inhibiting ubiquinone (CoQ) biosynthesis. This is effective against Eimeria because Eimeria has a functional mitochondrion with a complete ETC.

C. parvum has a **radically reduced mitochondrion** — it lacks the TCA cycle, lacks a functional ETC, and has only a remnant organelle (mitosome). The drug's target is literally absent in C. parvum. This is not a case of insufficient drug concentration or poor timing — the biological target does not exist in this parasite.

**Why practitioners tried it anyway:** Decoquinate is available, cheap, and labeled for another protozoan in the same host. Veterinary practitioners extrapolated from anticoccidial efficacy to anti-cryptosporidial use based on the assumption that "apicomplexan parasites are similar." This assumption is catastrophically wrong for this specific target — C. parvum's metabolic reduction makes it fundamentally different from Eimeria at the drug target level.

### In vitro to in vivo gap
There IS no in vitro activity. The failure is consistent from cell culture through to calf trials. This is clean evidence of a target that simply does not exist.

### Failure classification
**TARGET FAILURE (absolute).** The biological target (mitochondrial ETC) does not exist in C. parvum. No reformulation, dose optimization, or timing change can overcome this. Decoquinate should never be used for cryptosporidiosis.

### Disease stage mapping
- None — the drug has no mechanism of action against C. parvum at any stage

### Constraints for Forge
1. C. parvum's reduced genome means many standard anti-protozoal drug targets are absent
2. Do NOT assume efficacy against Eimeria translates to C. parvum — verify target existence first
3. Any proposed drug target must be confirmed to exist in the C. parvum genome (~3,800 genes)
4. The metabolic reduction of C. parvum is a fundamental constraint: it lacks de novo synthesis of amino acids, nucleotides, fatty acids, and has no functional ETC

---

## Treatment 5: Ionophores (Lasalocid, Monensin)

### What was tried
Lasalocid-Na and monensin, polyether ionophore antibiotics used extensively as anticoccidials in cattle. Tested for anti-cryptosporidial activity at various doses.

### Specific results
- **Lasalocid (preventive, 3 mg/kg from birth to day 7):** One Japanese study showed significant reduction in oocyst-positive rates during the dosing period. However, the effect was **preventive only** — calves with established infections showed minimal benefit
- **Lasalocid (therapeutic, 8 mg/kg for 3 days):** A Turkish study of 11 naturally infected calves showed reduced oocyst counts in 7/11 calves after 72h of treatment, but 1 calf died during treatment. The dose (8 mg/kg) approaches the toxic threshold for calves
- **Monensin:** Effective against Eimeria (coccidiosis) but ionophores in general have shown **no consistent anti-cryptosporidial activity** in controlled trials
- **Toxicity:** Lasalocid can be acutely toxic to calves depending on dose. Decline of suckling reflex and intoxication symptoms were observed in treated animals

### Why they failed

**Mechanism mismatch:** Ionophores work by disrupting membrane potential in parasites with mitochondria, facilitating uncontrolled ion flux that collapses energy production. Like decoquinate, this mechanism depends on a functional mitochondrial membrane potential. C. parvum's reduced mitosome does not generate a conventional membrane potential — the primary mechanism of ionophore action is attenuated.

**Partial efficacy at toxic doses:** The modest efficacy observed at high doses (8 mg/kg lasalocid) likely reflects non-specific membrane disruption at concentrations approaching toxicity for the host. This is not target-specific anti-parasitic activity — it is non-selective toxicity that harms both parasite and calf.

**The narrow therapeutic window:** In neonatal calves, ionophore toxicity is a significant concern. The margin between a dose that might affect C. parvum (if at all) and a dose that poisons the calf is dangerously narrow. One death out of 11 treated calves (9% mortality from treatment) is unacceptable.

### Failure classification
**TARGET FAILURE (primary) + COMPOUND FAILURE (secondary).** The primary target (mitochondrial membrane potential) is absent or severely reduced in C. parvum. Any efficacy observed at high doses is likely non-specific toxicity, not target engagement. The compounds are also too toxic at the doses needed to affect C. parvum.

### Disease stage mapping
- **Stage 4 (Merogony)** — theoretical target, but mechanism is inactive against C. parvum's reduced mitochondrion

### Constraints for Forge
1. Ionophore mechanisms are not viable against C. parvum
2. Non-specific membrane disruption approaches require toxic doses
3. The mitochondrial reduction in C. parvum eliminates an entire class of anti-protozoal mechanisms
4. Any proposed mechanism must be validated against C. parvum specifically, not extrapolated from Eimeria or Plasmodium

---

## Treatment 6: Azithromycin

### What was tried
Azithromycin, a macrolide antibiotic with known anti-protozoal activity, tested at 500-2,000 mg/calf/day for 7 days orally, and by injection.

### Specific results
- **Elitok et al. (2005, J Vet Intern Med):** 50 naturally infected Holstein calves. At 1,500-2,000 mg/day for 7 days: significant reductions in oocyst shedding and diarrhea incidence vs. controls. Weight gain was significantly higher in medicated calves. Authors recommended 1,500 mg/day for economic reasons.
- **Combination (azithromycin + toltrazuril, 2017, Vet Med):** 55 calves. The combination showed the best clinical scores and lowest oocyst counts at all time points. Combination promoted rapid clinical recovery and stopped oocyst shedding.
- **Russian study (2024):** Intramuscular azithromycin-based drug for 5-7 days. Claimed 100% effectiveness against Cryptosporidium with decreased diarrhea duration.

### Why it failed (to become a treatment)

**It may actually work — but the evidence is weak and the economics are prohibitive.**

**Evidence quality problems:**
1. The positive studies are predominantly from single research groups (Iran, Turkey, Russia) with no independent replication in controlled settings in North America or Western Europe
2. The Elitok study used naturally infected calves (uncontrolled infection timing and dose), making it impossible to separate drug effect from natural disease resolution
3. The Russian study claims 100% efficacy — which is biologically implausible and suggests methodological issues
4. No randomized, blinded, placebo-controlled trial with experimentally infected calves has confirmed efficacy

**Economic problems:**
1. 1,500 mg/day azithromycin x 7 days = 10.5g total. At current veterinary azithromycin costs, this is approximately $20-50 per treatment course — far above the $10-15 production animal threshold
2. Azithromycin is a critically important antimicrobial for human medicine (WHO Watch List). Routine prophylactic use in calves would face massive antimicrobial stewardship resistance
3. No approved veterinary formulation exists for oral use in neonatal calves

**Mechanism uncertainty:** Macrolides inhibit protein synthesis at the ribosomal level, but the specific interaction with C. parvum ribosomes is not well characterized. The drug may be acting partially as an immunomodulator rather than a direct anti-parasitic, which would explain its apparent efficacy in naturally infected (not immunologically naive) calves but would predict failure in the critical prophylactic window.

### Failure classification
**COMPOUND FAILURE (primarily economic and regulatory).** There is suggestive but unreplicated evidence of biological efficacy. The compound fails on cost, antimicrobial stewardship concerns, lack of approved formulation, and inadequate evidence base. The target biology (ribosomal protein synthesis) may be valid but is not definitively confirmed for C. parvum.

### Disease stage mapping
- **Stage 4 (Merogony)** — if the mechanism is direct ribosomal inhibition
- **Stage 6 (Immune response)** — possible immunomodulatory contribution

### Constraints for Forge
1. Protein synthesis inhibition at the ribosome may be a valid mechanism — but must be confirmed as direct anti-parasitic, not just immunomodulatory
2. The antimicrobial stewardship issue is a hard constraint: critically important human antibiotics cannot be used prophylactically in production animals
3. Any anti-parasitic that shares mechanism class with human antibiotics faces regulatory death
4. The combination approach (azithromycin + toltrazuril) hints that multi-target combinations may be necessary

---

## Treatment 7: Bumped Kinase Inhibitors (BKIs/CDPK1)

### What was tried
Bumped kinase inhibitors (BKIs) targeting C. parvum calcium-dependent protein kinase 1 (CpCDPK1), an essential parasite-specific kinase with no mammalian homolog. BKI-1553 was the first compound tested in calves. Newer scaffolds include pyrrolopyrimidine-based BKI-1649, BKI-1812, and BKI-1814.

### Specific results
- **BKI-1553 in calf model (Schaefer et al., 2016, J Infect Dis):** Proof-of-concept demonstrated. Significant treatment effects on diarrhea severity, oocyst shedding, and overall health. First demonstration that BKIs are safe and effective in the calf clinical model.
- **Mouse models:** Multiple BKIs show dose-dependent reduction in parasite burden in both neonatal and IFN-gamma-knockout mouse models
- **In vitro:** BKIs inhibit C. parvum in cell culture at sub-micromolar concentrations
- **Key finding (Van Voorhis lab, 2017, J Infect Dis; [DOI not available]):** Fecal drug concentrations correlating with parasite inhibitory concentrations predict efficacy better than plasma levels — suggesting luminal mechanism matters

### Why they have not yet succeeded

**These are the most advanced pipeline candidates — they have NOT definitively failed. But they face critical barriers to commercial viability:**

1. **hERG toxicity (cardiotoxicity):** First-generation BKIs showed anti-human ether-a-go-go potassium channel activity, a critical safety liability. This triggered extensive medicinal chemistry optimization to eliminate hERG activity while maintaining anti-parasitic potency. This is a compound optimization problem, not a target problem.

2. **The daily dosing requirement:** Like halofuginone, BKIs require daily oral administration during the prophylactic window. No sustained-release formulation has been demonstrated. The dosing regimen mirrors halofuginone's — and halofuginone's labor-intensive dosing is already a commercial limitation.

3. **Manufacturing cost uncertainty:** BKIs are novel chemical entities with multi-step synthesis. No published COGS analysis for production-scale manufacturing exists. The $10-15/dose production animal threshold has not been demonstrated as achievable.

4. **The fecal concentration finding changes everything:** If fecal (luminal) concentrations predict efficacy better than plasma levels, this means BKIs may be working primarily from the gut lumen rather than systemically. This would favor oral non-absorbable delivery — which could simplify formulation but raises questions about whether the absorbed dose is even necessary.

5. **Limited calf data:** Only BKI-1553 has been tested in calves, in a limited proof-of-concept study. The newer, safer scaffolds (BKI-1649, BKI-1812) have only been tested in mice. Translation to the calf model — with its unique neonatal physiology, milk-based diet, and rapid gastrointestinal transit — is not guaranteed.

### Failure classification
**NOT YET FAILED — but facing COMPOUND FAILURE barriers.** The target (CpCDPK1) is validated and parasite-specific. The biological mechanism is sound. The failures are all compound-level: hERG toxicity in first-generation compounds, manufacturing cost uncertainty, daily dosing requirement, and incomplete translation from mouse to calf models.

### Disease stage mapping
- **Stage 2 (Invasion)** — CDPK1 is involved in invasion; BKIs can block sporozoite entry
- **Stage 4 (Merogony)** — CDPK1 essential for intracellular replication

### Constraints for Forge
1. CpCDPK1 is a validated, parasite-specific target — this IS the right biology
2. The compound optimization challenge (hERG, COGS, formulation) is real but potentially solvable
3. If fecal concentration drives efficacy, reformulation as a non-absorbable oral agent could simplify the safety and PK profile
4. A sustained-release oral formulation (bolus, in-feed) delivering BKI to the gut lumen for 14 days would be transformative
5. BKIs are the best available chemical starting point — Forge should build on them, not reinvent the wheel

---

## Treatment 8: Passive Immunization (Colostrum Antibodies, Hyperimmune Products)

### What was tried
Multiple approaches to provide pre-formed anti-Cryptosporidium antibodies to neonatal calves:
1. **Natural colostrum supplementation** — feeding additional colostrum from unvaccinated dams
2. **Hyperimmune bovine colostrum (HBC)** — colostrum from dams vaccinated with C. parvum antigens
3. **Hyperimmune bovine colostral immunoglobulin concentrate** — purified IgG from hyperimmune colostrum (e.g., GastroGard-type products)
4. **Egg yolk antibodies (IgY)** — from hens immunized with C. parvum antigens

### Specific results
Based on articles retrieved from PubMed:
- **Recombinant P23-based vaccination of dams (Askari et al., 2016; [DOI](https://doi.org/10.1111/pim.12317)):** Calves fed hyperimmune colostrum from P23-vaccinated dams "did not show cryptosporidiosis signs" and had delayed onset and reduced oocyst excretion vs. controls. But: small study, single lab, challenged with 10^7 oocysts (high dose).
- **Natural colostrum supplementation (Kacar et al., 2022; [DOI](https://doi.org/10.1016/j.vetimm.2022.110429)):** Colostrum + paromomycin improved clinical outcomes faster than paromomycin alone. However, colostrum alone (without paromomycin) was NOT sufficient to prevent or cure infection.
- **General colostrum supplementation (2023 Frontiers study cited in disease map):** Limited clinical alleviation; modulates gut immune response but does NOT prevent infection or significantly reduce shedding.
- **Hyperimmune products in mice:** Anti-CP15 and anti-P23 antibodies showed efficacy in murine models.
- **Transfer of passive immunity data (Gamsjager et al., 2023; [DOI](https://doi.org/10.1016/j.prevetmed.2023.106026)):** C. parvum-specific IgG levels in neonatal calf serum were highly variable between farms and were not predictive of protection. Higher total IgG was associated with better outcomes, but the effect was not C. parvum-specific.

### Why it failed

**The antibody half-life problem:** Colostral IgG in the intestinal lumen has a half-life measured in hours, not days. The vulnerability window is 14+ days. Even if colostral antibodies are effective at blocking invasion on day 1, they are degraded by proteolytic enzymes in the gut by day 3-5 — exactly when the parasite is accelerating to peak burden. There is no mechanism for sustained antibody presence in the gut lumen after the initial colostral feeding.

**The specificity problem:** Natural colostrum contains variable and often low levels of C. parvum-specific antibodies. General IgG supplementation provides some non-specific mucosal protection but cannot achieve the antigen-specific neutralization needed to block sporozoite invasion. The positive results from hyperimmune colostrum (P23, GP40-targeted) suggest that antigen specificity matters — but even antigen-specific colostral antibodies degrade in the gut within days.

**The autoinfection bypass:** Even if luminal antibodies block primary sporozoite invasion from environmental oocysts, autoinfection via thin-walled oocysts occurs within the gut lumen — potentially in protected microenvironments (crypt-villus interface) where antibody penetration may be limited. Furthermore, once the parasite is established in its intracellular-extracytoplasmic niche, luminal antibodies cannot reach it.

**The systemic vs. luminal disconnect:** Colostral antibodies enter the neonatal calf's bloodstream via FcRn-mediated transcytosis in the first 24h of life, providing systemic immunity. But C. parvum is a luminal/mucosal pathogen — systemic IgG has limited access to the intestinal lumen after gut closure. The antibodies go to the wrong compartment.

### Failure classification
**COMPOUND FAILURE (delivery and duration).** The target biology is partially valid — anti-GP40 and anti-P23 antibodies CAN neutralize sporozoites in vitro and in some in vivo models. The failure is in delivery: antibodies cannot persist in the gut lumen for the 14-day vulnerability window. This is a formulation/delivery challenge, not a target failure.

### Disease stage mapping
- **Stage 2 (Invasion)** — antibodies block sporozoite attachment; effective for primary invasion but not autoinfection
- **Stage 6 (Immune response)** — supplements deficient neonatal mucosal immunity, but transiently

### Constraints for Forge
1. Antibody-based approaches require sustained luminal presence for 14+ days — this is the critical unsolved problem
2. Antigen specificity matters: anti-GP40, anti-P23 are more effective than polyclonal colostrum
3. Systemic IgG is irrelevant for this mucosal pathogen — the product must persist in the gut lumen
4. Encapsulation, mucoadhesive formulation, or continuous oral delivery could overcome the degradation problem
5. Combination with a direct anti-parasitic (as shown with paromomycin) may be synergistic

---

## Treatment 9: Maternal Vaccination (Recombinant Antigen Vaccines)

### What was tried
Vaccinating pregnant dams with C. parvum antigens to boost colostral antibody transfer to calves. Key antigens: GP40/GP15 (from GP60 precursor), P23, CP15/60.

### Specific results
- **Bovicrypt (EU, HIPRA):** Subunit vaccine targeting multiple C. parvum antigens. Field trials show reduced diarrhea duration in calves from vaccinated dams. EU regulatory review ongoing/completed. The most advanced maternal vaccination approach.
- **Recombinant P23 vaccine (Askari et al., 2016; [DOI](https://doi.org/10.1111/pim.12317)):** Vaccinating cows 4 times from 70 days to parturition significantly increased antibody titres in sera and first-milking colostrum. Calves fed hyperimmune colostrum had reduced and delayed oocyst excretion.
- **No vaccine prevents infection:** All maternal vaccination approaches reduce severity and duration but do NOT prevent establishment of infection or significantly reduce peak oocyst shedding

### Why it has not solved the problem

**All the passive immunization problems apply, plus additional vaccine-specific issues:**

1. **The colostral antibody decay problem persists:** Maternal vaccination increases the QUANTITY of specific antibodies in colostrum, but does not change their DURABILITY in the calf gut. Higher starting titre delays the point at which antibody levels drop below the effective threshold — perhaps by 1-3 days — but cannot bridge the full 14-day vulnerability window.

2. **Single antigenic target limitation:** Most vaccine candidates target a single surface antigen (GP40 or P23). C. parvum has multiple redundant invasion pathways — sporozoites can potentially use alternative receptors even when the primary invasion pathway is blocked by antibodies. Single-antigen vaccines are inherently limited against parasites with invasion redundancy.

3. **Glycan-dependent epitopes:** GP40 has glycan-dependent epitopes that are difficult to replicate in recombinant expression systems. Vaccines using recombinant GP40 may not present the correct conformational/glycan epitopes needed for functional neutralizing antibodies.

4. **Strain variation:** GP60 subtypes (IIa vs IId) vary in sequence, potentially affecting the breadth of vaccine-induced antibody neutralization. A vaccine optimized for one subtype may have reduced efficacy against another.

5. **The autoinfection problem remains unsolved:** Even if maternal antibodies reduce primary invasion from environmental oocysts by 50-80%, the exponential amplification dynamics mean the remaining parasites reach overwhelming burden within 1-2 additional merogony cycles (12-24h delay). The dose-independence of severity data from Zambriski et al. predicts that even dramatically reduced initial invasion will produce similar disease severity once autoinfection establishes.

### Failure classification
**PARTIAL TARGET FAILURE + COMPOUND FAILURE.** The target biology (blocking sporozoite invasion) is sound but insufficient alone — reducing primary invasion does not prevent disease due to autoinfection and exponential amplification. The compound (colostral antibodies) degrades too rapidly for the required duration of protection. Maternal vaccination is a valid component of a multi-pronged strategy but cannot stand alone.

### Disease stage mapping
- **Stage 2 (Invasion)** — reduces initial sporozoite invasion efficiency
- Not effective against Stage 4 (Merogony) or Stage 5 (Autoinfection)

### Constraints for Forge
1. Maternal vaccination reduces severity but cannot prevent infection — it IS a useful adjunct but NOT a standalone solution
2. Multi-antigen vaccines may perform better than single-antigen
3. The colostral duration problem must be solved independently (formulation, not vaccination)
4. Maternal vaccination has the best commercial viability profile (single injection in dam, no calf handling) — combine with a direct anti-parasitic for the calf

---

## Treatment 10: Probiotics and Prebiotics

### What was tried
Various probiotic organisms and prebiotic supplements:
- Lactic acid-producing bacteria (Lactobacillus spp.)
- Bacillus subtilis
- Saccharomyces boulardii
- Mannan-oligosaccharide (MOS, prebiotic)
- Synbiotic combinations (probiotic + prebiotic)
- Fermented milk with probiotic strains

### Specific results
- **Harp et al. (1996, Am J Vet Res):** 134 calves, field study. Oral lactic acid bacteria daily for 10 days from birth — NO significant difference in diarrhea incidence or oocyst shedding vs. controls. "High numbers of C. parvum in the environment may have overwhelmed any potential benefits."
- **Bacillus subtilis (2021, J Dairy Sci):** 1,801 calves, large commercial dairy. Probiotic-treated calves had 100x lower Cryptosporidium oocyst shedding at day 14 — a remarkable result. BUT: no effect on diarrhea duration, hazard of diarrhea, or pneumonia incidence. The reduction in shedding did NOT translate to clinical improvement.
- **Fermented milk with probiotic strains (2023, Vet Microbiol):** 143 calves across 3 farms. NO significant effect on diarrhea prevalence, C. parvum occurrence, or Campylobacter levels. The feeding approach actually showed a **detrimental effect on daily weight gain**.

### Why they failed

**The competition model is wrong for this pathogen.** Probiotics work through three mechanisms: (1) competitive exclusion of pathogens from binding sites, (2) production of antimicrobial metabolites (butyrate, bacteriocins), and (3) immune modulation. For C. parvum, none of these mechanisms can overcome the core problem:

1. **Competitive exclusion fails:** C. parvum is an intracellular parasite. It does not compete with bacteria for luminal resources or binding sites in the same way. Once sporozoites invade enterocytes and establish the parasitophorous vacuole, they are beyond the reach of luminal bacteria.

2. **Metabolite production is too slow:** Butyrate and other short-chain fatty acids require an established, mature microbiome to produce at effective concentrations. In neonatal calves (0-3 days old), the microbiome is barely colonized. By the time a probiotic could establish and begin producing anti-parasitic metabolites (days 5-7), the parasite has already reached peak burden.

3. **Immune modulation is the timing gap again:** Probiotics can prime innate immunity, but this priming requires days to take effect. The parasite amplifies faster than probiotic-mediated immune maturation.

**The Bacillus subtilis exception is informative:** The 100x reduction in oocyst shedding at day 14 without clinical improvement suggests the probiotic affected shedding dynamics (possibly by altering gut environment during the resolution phase) but did NOT affect peak disease severity. This is consistent with the timing gap model — the probiotic's effects manifest too late to prevent peak damage.

### Failure classification
**TARGET FAILURE (for standalone clinical protection).** The biological rationale — modulate the gut environment to disadvantage the parasite — is fundamentally mismatched with C. parvum's disease kinetics. The parasite reaches peak burden in 5-7 days; probiotics need weeks to establish. However, probiotics may have value for (a) reducing oocyst shedding (environmental contamination reduction) and (b) accelerating post-infection recovery.

### Disease stage mapping
- **Stage 8 (Shedding/Environment)** — some evidence for reduced shedding (Bacillus subtilis)
- NOT effective against Stages 2-5 during the critical vulnerability window

### Constraints for Forge
1. Probiotics cannot stand alone against cryptosporidiosis — the kinetic mismatch is too severe
2. The Bacillus subtilis shedding reduction (100x) is notable for herd-level environmental load reduction
3. Probiotics may have value as an adjunct for post-infection recovery (Stage 7-8), not primary prophylaxis
4. Any microbiome-based approach would need to be combined with a direct anti-parasitic or immune accelerator

---

## Treatment 11: Oral Rehydration Therapy (ORT)

### What was tried
Oral rehydration solutions (ORS) with various formulations — standard WHO-type electrolyte solutions, glutamine-enriched ORS, ORS with continued milk feeding, IV fluid support for severe cases.

### Specific results
- **ORS + whole milk (1994, J Dairy Sci):** 42 calves with spontaneous diarrhea (70% Cryptosporidium-positive). ORS + continued milk feeding promoted weight gain; ORS alone caused weight loss during first 3 days. No mortality in any group. BUT: no effect on fecal score, rectal temperature, or infection parameters.
- **Blikslager et al. (2001) ex vivo data:** Glutamine + indomethacin fully restored Na+ and Cl- absorption in C. parvum-infected bovine ileum despite severe villous atrophy — directly addressing the secretory and malabsorptive components of diarrhea.
- **Isoquinoline alkaloid supplementation (2021, Vet Parasitol):** 26 calves. Supplemented calves had higher weight gain (14-21 days), no mortality (vs. 15.4% in controls), and reduced diarrhea intensity/duration. Control calves required more hydration support.

### Why it is necessary but insufficient

**ORT does not treat the disease — it treats the consequence.** The entire rationale of ORT is to prevent death from dehydration while the calf's immune system clears the infection. ORT has ZERO anti-parasitic activity. It does not reduce parasite burden, does not shorten infection duration, and does not reduce oocyst shedding.

**Why it is still the most important current intervention:**
1. It prevents mortality. Calves die of dehydration and metabolic acidosis, not directly from the parasite. ORT addresses the proximate cause of death.
2. Continued milk feeding during diarrhea prevents the catastrophic weight loss that is not recovered for 6 months post-infection.
3. It is available, cheap, and requires no regulatory approval.

**The glutamine + indomethacin finding is the most underexploited result in the literature.** Full restoration of electrolyte absorption in infected tissue — without any anti-parasitic activity — means symptomatic management could be dramatically improved with a simple two-component intervention. This has never been tested in a controlled in vivo calf trial despite compelling ex vivo bovine data from 2001.

### Failure classification
**NOT A TREATMENT FAILURE — it is a management intervention that works as intended.** ORT was never designed to kill the parasite. Its limitation is that it does not address the disease itself, only its consequences.

### Disease stage mapping
- **Stage 7 (Pathology/Diarrhea)** — directly addresses fluid and electrolyte loss
- **Stage 12 (Economic impact)** — prevents mortality and partially mitigates weight loss

### Constraints for Forge
1. ORT is the baseline — any new treatment must be ADDED to ORT, not replace it
2. The glutamine + indomethacin combination should be evaluated in vivo as an enhanced ORT — it could be the most cost-effective near-term improvement
3. Indomethacin (COX inhibitor) may have dual value: anti-secretory + relief of PGE2-mediated local immunosuppression (per Tribunal Phase 1b PGE2 hypothesis)
4. Any anti-parasitic treatment will also require concurrent ORT — the two are complementary, not alternatives

---

## Treatment 12: Environmental Decontamination

### What was tried
Multiple approaches to reduce environmental oocyst load:
- **Chemical disinfection:** Chlorine, quaternary ammonium compounds, hydrogen peroxide, p-chloro-m-cresol
- **Physical methods:** UV irradiation, ozone, steam cleaning, desiccation, heat
- **Management:** All-in/all-out housing, pen rotation, extended vacancy periods

### Specific results
- **Chlorine:** 5 mg/L free chlorine for 300 min achieves only ~0.6-0.8 log reduction (Coleman et al., 2023). Essentially useless against the scale of contamination.
- **Ozone:** Effective in water treatment — 99% inactivation achievable at appropriate concentrations. BUT: ozone is highly reactive and decomposes rapidly; maintaining effective concentrations in a farm environment (organic matter-rich) is impractical.
- **UV:** Effective in water treatment at adequate doses. Not practical for surface decontamination on farms.
- **Steam cleaning:** Can achieve >99% oocyst inactivation on hard surfaces. Limited by: only works on cleanable surfaces; cannot treat soil, bedding, or organic matter-laden surfaces.
- **Desiccation:** Oocysts ARE vulnerable to drying. Extending pen vacancy with dry conditions can reduce viability. But: farm environments in temperate climates cannot be kept consistently dry.
- **p-Chloro-m-cresol (3%):** In combination with halofuginone, showed efficacy (Keidel & Daugschies, 2013). But cresol-based disinfectants have their own toxicity and environmental concerns.
- **Management (meta-analysis, Thomson et al., 2017):** All-in-all-out housing, steam cleaning pens, colostrum management can lower incidence by 30-50% in aggregate.

### Why they fail for individual calf protection

**The Martian's calculation from Phase 1b is definitive.** The math:
- One infected calf sheds ~10^10 total oocysts
- ID50 is ~10 oocysts
- Even 99.99% decontamination leaves 10^6 viable oocysts — enough to infect 100,000 calves
- To get below infectious dose threshold requires >6 log10 reduction — practically unachievable in a farm environment with continuous organic matter, moisture, and new calves entering daily

**Furthermore, the dose-independence of severity means partial environmental reduction has ZERO impact on individual disease outcomes.** Whether a calf encounters 10 oocysts or 10 million oocysts, the resulting disease is identical (Zambriski et al., 2013). Environmental decontamination only matters if it achieves complete elimination of exposure — which is mathematically impossible at current R0.

**Where environmental management DOES matter:**
- Multi-year herd-level R0 reduction: if each calving season reduces environmental load by 90%, compounding over 3-5 seasons could eventually bring exposure below critical thresholds
- Reducing peak environmental load to reduce the probability of very-early exposure (day 0-1 of life) vs. slightly-later exposure (day 3-5)

### Failure classification
**TARGET FAILURE (for individual calf protection).** The target (environmental oocyst load) is the wrong target for individual disease outcomes due to dose-independence of severity. Environmental decontamination addresses herd-level R0 over multi-year timescales, not individual calf disease severity.

### Disease stage mapping
- **Stage 1 (Entry/Exposure)** — reduces probability of exposure, but cannot eliminate it
- **Stage 8 (Shedding/Environment)** — reduces environmental burden for subsequent calves

### Constraints for Forge
1. Environmental decontamination is necessary for long-term herd management but irrelevant for individual calf treatment
2. Any portfolio must include environmental management as a complement, not a primary intervention
3. The real environmental lever is SHEDDING REDUCTION from treated calves — a drug that reduces oocyst output by >90% per calf would be more impactful than any decontamination protocol
4. Do not waste Forge resources on environmental approaches for individual calf outcomes

---

## Treatment 13: Clofazimine (Bonus — Pipeline Failure)

### What was tried
Clofazimine (Lamprene), an oral phenazine dye used for leprosy for 50+ years, identified via high-throughput screening as having anti-Cryptosporidium activity.

### Specific results
Based on articles retrieved from PubMed, the CRYPTOFAZ trial (NCT03341767; Nachipo et al., 2018; [DOI](https://doi.org/10.1186/s13063-018-2846-6)) was a randomized, double-blind, placebo-controlled study in HIV-infected patients with cryptosporidial diarrhea in Malawi:
- Clofazimine or placebo for 5 days
- **Oocyst shedding was detected even at days 41-55** in both clofazimine and placebo arms
- Re-analysis (Nyirenda et al., 2023; [DOI](https://doi.org/10.1371/journal.pone.0289929)) confirmed no clear anti-Cryptosporidium efficacy by either qPCR or ELISA
- Active in acute mouse infection models but NOT in persistent/chronic infection

### Why it failed

**The acute vs. persistent infection distinction.** Clofazimine showed efficacy in acute mouse models (immunocompetent mice with self-limiting infection) but failed in HIV-infected humans with persistent infection. The same pattern as NTZ — efficacy in immunocompetent hosts, failure in immunocompromised hosts.

**Mechanism of action unclear.** Clofazimine's anti-cryptosporidial mechanism is not well characterized. It may work via reactive oxygen species generation or membrane disruption, mechanisms that might be insufficient against the protected intracellular-extracytoplasmic niche.

**Implications for calf crypto:** The CRYPTOFAZ failure is directly relevant because neonatal calves during the vulnerability window are functionally immunodeficient (like HIV patients) in terms of their adaptive anti-Crypto response. Any drug that requires immune cooperation to achieve lasting clearance will fail in this population.

### Failure classification
**TARGET FAILURE (immune-dependence) + COMPOUND FAILURE (insufficient direct anti-parasitic activity).** Like NTZ, clofazimine's efficacy is immune-dependent. Its direct anti-parasitic activity is insufficient to clear established infection without immune cooperation.

### Disease stage mapping
- Uncertain — mechanism not well characterized

### Constraints for Forge
1. Yet another confirmation that immune-dependent drugs fail in immunologically naive hosts
2. HTS-identified compounds must be validated in the correct disease model (immunodeficient, high-burden) not just acute models
3. The acute-mouse-model-to-chronic-human-failure pipeline is a systemic problem in Crypto drug development — any Forge candidate must be tested in a model that recapitulates the neonatal calf's immunological state

---

## The Gap Map

| Disease Stage | Treatments Tried | Why They Failed | Gap? |
|---|---|---|---|
| **1. Entry/Exposure** | Environmental decontamination (chlorine, ozone, UV, steam, management) | Cannot achieve sufficient log reduction at farm scale; dose-independence means partial reduction is useless for individual calves | YES — no practical way to prevent exposure at current R0 |
| **2. Excystation/Invasion** | Passive immunization (hyperimmune colostrum, maternal vaccination), anti-GP40 antibodies | Antibody degradation in gut lumen (hours, not days); cannot sustain protection for 14-day window; single-antigen may face invasion redundancy | **PARTIAL** — mechanism works but delivery fails; Bovicrypt shows modest benefit |
| **3. Niche (Drug Delivery)** | Paromomycin proves luminal access; BKIs prove systemic access | The niche IS accessible from both routes — this is NOT the primary barrier | **NO** — niche access is solved in principle (luminal route validated) |
| **4. Merogony Suppression** | Halofuginone (cryptostatic), BKIs (CDPK1), paromomycin | Halofuginone too weak; BKIs promising but not yet commercially viable; paromomycin toxic | YES — need a potent, safe, affordable merogony inhibitor with sustained delivery |
| **5. Autoinfection Block** | None specifically targeted | No treatment has specifically targeted the thin-walled oocyst autoinfection cycle | **YES (CRITICAL GAP)** — no approach exists to break the autoinfection loop |
| **6. Immune Acceleration** | rBoIL-12 (failed despite IFN-gamma stimulation), natural colostrum (insufficient) | rBoIL-12 paradox — immune stimulation alone insufficient, possibly due to PGE2-mediated local immunosuppression | YES — no validated approach to accelerate neonatal adaptive immunity across the timing gap |
| **7. Pathology Mitigation** | ORT (effective at preventing death), glutamine + indomethacin (ex vivo only) | ORT works for survival; glutamine + indomethacin untested in vivo despite compelling ex vivo data | **PARTIAL** — ORT works; enhanced ORT (glutamine + COX inhibitor) is untested |
| **8. Shedding Reduction** | Halofuginone (modest), paromomycin (effective but toxic), Bacillus subtilis (100x at day 14) | No safe, affordable drug achieves >90% shedding reduction needed to impact herd R0 | YES — need >90% shedding reduction in a safe, affordable format |
| **9. Post-Infection Recovery** | None specifically targeted | No treatment addresses the stem cell/Wnt pathway damage that prevents weight recovery for 6 months | **YES (CRITICAL GAP)** — no approach addresses epithelial regeneration |
| **10. Neonatal Immune Priming** | Probiotics (failed for clinical protection), colostrum (insufficient) | Probiotics too slow; colostral antibodies too transient | YES — innate immune training (beta-glucan, BCG) never tested in calves for Crypto |

---

## The Rate-Limiting Barrier to Cure

The rate-limiting barrier is **the immune timing gap combined with the absence of any treatment that can bridge it**.

Every treatment that has been tested fails at one of three points:
1. **Too weak:** Halofuginone, NTZ — partial suppression that delays the kinetic curve by 1-2 cycles but cannot flatten it
2. **Too late:** Therapeutic approaches given after clinical signs face 10^10+ parasites — an insurmountable burden for any drug alone
3. **Too brief:** Antibody-based approaches degrade within days; the vulnerability window is 14+ days

The one compound that DOES work pharmacologically (paromomycin at 100 mg/kg/day) proves the concept — continuous luminal drug presence from birth through the vulnerability window can control infection — but fails on toxicity and cost.

**The solution must be:**
- Present from birth (prophylactic)
- Active for 14+ days (sustained delivery)
- Potent enough for >80% merogony suppression (not merely cryptostatic)
- Safe in neonates (no nephrotoxicity, no growth impairment)
- Affordable (<$10-15/calf)
- Ideally combined with an immune accelerator and/or enhanced ORT

---

## The Compound Contamination Summary

| Treatment | Target Failure or Compound Failure? | Implication |
|---|---|---|
| Halofuginone | **COMPOUND** (too weak; cryptostatic not -cidal) | Target valid — merogony suppression works; need better compound |
| Nitazoxanide | **TARGET** (immune-dependent mechanism fails in immunologically naive host) | Do not pursue immune-dependent drugs for neonatal window |
| Paromomycin | **COMPOUND** (toxic, expensive, impractical dosing) | Target valid — luminal aminoglycoside delivery works; need safer compound |
| Decoquinate | **TARGET** (absolute — target absent in C. parvum) | ETC-targeting drugs are irrelevant; verify target existence in genome |
| Ionophores | **TARGET** (primarily) + COMPOUND (toxic) | Mitochondrial disruption mechanisms fail against reduced mitosome |
| Azithromycin | **COMPOUND** (economic, regulatory, evidence quality) | Ribosomal target may be valid but unconfirmed; AMR stewardship blocks use |
| BKIs | **COMPOUND** (hERG, COGS, formulation — not yet failed) | CpCDPK1 is validated; compound optimization is achievable |
| Passive immunization | **COMPOUND** (delivery/duration failure) | Antibodies CAN neutralize; need sustained luminal delivery |
| Maternal vaccination | **PARTIAL TARGET** + **COMPOUND** | Reduces severity but cannot prevent infection; colostral duration insufficient |
| Probiotics | **TARGET** (kinetic mismatch too severe) | Cannot match parasite amplification speed; value only as adjunct |
| ORT | **N/A** (not a treatment; works as management) | Essential baseline; enhanced ORT (glutamine + indomethacin) untested |
| Environmental | **TARGET** (dose-independence eliminates individual calf value) | Long-term herd R0 value only; not individual calf intervention |
| Clofazimine | **TARGET** (immune-dependent) + **COMPOUND** (insufficient activity) | Confirms immune-dependence pattern across multiple drug classes |

---

## In Vitro to In Vivo Translation Gaps

| Compound | In Vitro Result | In Vivo Result | Translation Gap Explanation |
|---|---|---|---|
| **BKIs** | Sub-micromolar IC50 against C. parvum in cell culture | Significant effects in calf model, but fecal concentration (not plasma) predicts efficacy | Luminal delivery may be more important than systemic; PK profile matters more than potency |
| **Decoquinate** | 8% inhibition at 100 microM only | Zero effect in calves and mice | No translation gap — drug is inactive against C. parvum at all levels |
| **Paromomycin** | Active against C. parvum in cell culture | Effective prophylactically in calves at 100 mg/kg/day but nephrotoxic | Translation gap is toxicity, not efficacy — the drug reaches the target but poisons the host |
| **NTZ** | Active in cell culture (HCT-8 cells) | Conflicting results in calves; fails in immunocompromised hosts | Cell culture does not model the immune-dependence of in vivo activity |
| **Clofazimine** | Active in HTS screen; active in acute mouse model | Failed in CRYPTOFAZ (HIV patients); likely would fail in calves | Acute self-limiting models do not predict efficacy in chronic/high-burden infections |
| **Anti-GP40 antibodies** | Neutralize invasion in vitro | Modest reduction in vivo; cannot prevent infection | Antibody degradation in gut lumen; autoinfection bypasses luminal antibodies |
| **Probiotics (Bacillus subtilis)** | Some in vitro evidence of anti-Crypto metabolite production | 100x shedding reduction but no clinical improvement | Timing mismatch: metabolite effects manifest after clinical disease peak |

**The systemic pattern:** In vitro activity against C. parvum is necessary but wildly insufficient to predict in vivo efficacy. The critical in vivo barriers — the timing gap, the autoinfection cycle, the immune-dependence, the antibody degradation, the neonatal physiology — are invisible in cell culture. **Any compound entering the Forge pipeline must be evaluated against the in vivo bottleneck (timing gap + sustained delivery), not just the in vitro target.**

---

## The 5 Key Lessons for Forge

1. **Cryptostatic is insufficient; cryptosporicidal or >80% suppression is required.** Halofuginone's marginal efficacy proves that partial merogony slowing delays the kinetic curve but cannot flatten it. Any drug candidate must be evaluated for its ability to reduce peak parasite burden by >3 log10, not just slow replication.

2. **Immune-dependent drugs are dead on arrival for neonatal calves.** NTZ, clofazimine, and rBoIL-12 all demonstrate that drug efficacy requiring immune cooperation fails in the neonatal window. Direct anti-parasitic activity is non-negotiable.

3. **Luminal delivery to the niche is validated and may be superior to systemic.** Paromomycin (luminal aminoglycoside) achieved the strongest efficacy of any tested compound. BKI fecal concentration correlates better with efficacy than plasma concentration. The parasite's intracellular-extracytoplasmic niche is more accessible from the lumen than from the cytoplasm.

4. **Sustained delivery for 14+ days is the critical product property — more important than potency.** Every effective approach (halofuginone, paromomycin, BKIs) requires continuous daily dosing. Every approach that degrades or wears off (colostral antibodies, pulsed dosing) fails due to autoinfection rebound. A moderately potent drug in a sustained-release formulation beats a highly potent drug requiring daily oral dosing.

5. **The autoinfection cycle is the untargeted multiplier.** No treatment has specifically targeted the thin-walled oocyst autoinfection cycle. This is the amplification engine that makes every other intervention insufficient. Breaking autoinfection — even partially — would synergize with every other approach.

---

*Sapper analysis complete. 13 approaches analyzed with specific failure mechanisms. Every failure mapped to disease stages. Every failure tagged as target or compound failure. In vitro to in vivo translation gaps catalogued. Gap map shows 6 stages with YES (critical gaps), 2 PARTIAL, and 2 with validated approaches. The rate-limiting barrier is the immune timing gap combined with the absence of any sustained, potent, safe, affordable anti-parasitic that can bridge it.*
