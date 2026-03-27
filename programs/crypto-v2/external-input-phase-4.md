# Adversarial Review — phase-4-kill-report.md

Generated: 2026-03-27 17:50

Document: `programs/crypto-v2/phase-4-kill-report.md`

---

### OpenRouter (gpt-5.4-20260305)

## WRONG KILLS (Targets killed that should survive)

### #21 Environmental oocyst inactivation
- **Why the kill is wrong:** Reaper applies an **individual-calf severity** lens to a target that is fundamentally **transmission-control / incidence-reduction**. “Dose-independence of severity” does not imply environmental control has “ZERO effect” on useful outcomes. It only argues severity may saturate once infection is established. On farms, reducing environmental burden can still reduce:
  - probability of becoming infected at all,
  - age at first infection,
  - force of infection / repeated exposure,
  - within-pen spread and cohort attack rate.
- **Evidence supporting the target:** Cryptosporidium control programs in livestock routinely emphasize hygiene because oocyst exposure pressure matters epidemiologically even if challenge-dose/severity curves plateau over some range. Environmental interventions are standard because oocysts are highly persistent and massive shedding drives outbreaks.
- **What verdict should be:** **WOUNDED, not KILLED.** Fatal if judged as a stand-alone therapeutic for an already sick calf; viable if judged as herd-level prevention.

### #23 5-HT3 antagonist / ondansetron
- **Why the kill is wrong:** The “may worsen infection by reducing motility” argument is speculative and likely overstated. 5-HT3 antagonists are not classic antimotility drugs in the loperamide sense; their main GI effects are on secretion, visceral signaling, and nausea reflexes. Reaper presents no direct evidence that ondansetron meaningfully increases Cryptosporidium invasion in vivo.
- **Evidence supporting the target:** There is real precedent across enteric disease that serotonergic signaling contributes to secretory diarrhea. Even if bovine-specific crypto data are lacking, the mechanism is not absurd, and symptomatic benefit could still matter commercially.
- **What verdict should be:** **WOUNDED.** Weak species support, but not dead on the basis offered.

### #19 Recombinant mucin-like glycoprotein decoy
- **Why the kill is wrong:** Reaper conflates **current recombinant production difficulty** with **target invalidity**. A target can survive while a specific manufacturing route dies. If glycan-dependent attachment biology is real, there are alternative paths:
  - glycoengineered expression systems,
  - synthetic glycomimetics,
  - purified native material for proof-of-concept,
  - minimal glycan motif mapping rather than full mucin recreation.
- **Evidence supporting the target:** The underlying concept—blocking parasite adhesion with host-like decoys—is biologically plausible. Single-lab support is a major weakness, but not enough by itself for a fatal kill at this stage.
- **What verdict should be:** **WOUNDED.** Kill the current CHO recombinant product concept if needed, not the biology outright.

### V11 Kinesin-5 / CpKin5
- **Why the kill is wrong:** Reaper overinterprets “73.3% similarity to human Eg5” as making selectivity “impossible.” Sequence similarity alone does not establish undruggability; kinase and motor protein programs often exploit small pocket differences despite substantial homology. Existing host-toxic Eg5 inhibitors do not prove all parasite-selective chemotypes are impossible.
- **Evidence supporting the target:** There is direct parasite biology from the 2024 mBio study that the axis is functionally important. That is more than many surviving targets have.
- **What verdict should be:** **WOUNDED.** Strong host-toxicity concern, but “impossible” is too strong.

---

## WRONG SURVIVALS (Targets that survived but should be killed)

### #16 COX-2 inhibitor / meloxicam
- **Fatal flaw:** Reaper lets this survive on ex vivo physiology and commercial convenience, but this is likely a **supportive-care tweak**, not a drug target for cryptosporidiosis. The evidence cited is mostly **indomethacin + glutamine ex vivo**, not meloxicam monotherapy in infected calves. The leap from restored electrolyte transport in isolated tissue to meaningful in vivo outcomes in neonatal calves is large.
- **Evidence:** No cited randomized calf efficacy trial showing meloxicam reduces crypto-specific morbidity, shedding, mortality, or weight loss. NSAIDs in dehydrated diarrheic neonates carry renal/GI risks under field conditions, especially where hydration support is imperfect.
- **Why kill:** This is not disease-modifying, has shaky direct evidence, and may underperform badly in real-world calves. It belongs in supportive-care protocol optimization, not as a surviving “target.”

### #22 Enhanced ORT — glutamine + meloxicam
- **Fatal flaw:** This is not really a target proposal at all; it is a **supportive management bundle**. Reaper survives it based on a 2001 ex vivo bovine ileum result and neglect narrative, but there is still **no direct in vivo calf trial evidence** for the proposed regimen. The claim of “strongest data in the portfolio” is not justified if the endpoint is actual calf clinical benefit.
- **Evidence:** Ex vivo restoration of ion transport does not establish feasible ileal delivery, adequate exposure, or durable clinical efficacy in diarrheic calves. Glutamine absorption proximally may limit distal effect; meloxicam risks remain hydration-dependent.
- **Why kill:** As a therapeutic target assessment, this fails the translational bar. At minimum it should be wounded until actual in vivo randomized calf data exist.

### #25 Triple combination (BKI + nanobody + beta-glucan)
- **Fatal flaw:** This survives entirely on **speculative multiplication of hypothetical partial effects** from components that themselves are not all validated. Nanobody and beta-glucan are wounded precisely because they lack direct anti-crypto proof in calves; combining them does not create evidence.
- **Evidence:** Combination benefit is asserted from modeled logs, not measured synergy. Cost, manufacturability, formulation complexity, and synchronized 14-day exposure make this especially unrealistic in production animals.
- **Why kill:** A combination cannot survive when two key components remain conjectural. This is portfolio architecture, not a de-risked candidate.

### #26 Enhanced ORT + MMV665917
- **Fatal flaw:** Survives by piggybacking on two uncertain pieces:
  - enhanced ORT lacks in vivo proof,
  - MMV665917 was itself only wounded because of **single-network dependency, unknown target, high dose, hERG concern, and 8-year stall**.
  A combo does not fix these; it compounds uncertainty.
- **Evidence:** No combination data, no formulation path, and no evidence that adding ORT rescues any weakness of MMV665917 beyond symptomatic support.
- **Why kill:** Premature combination survival based on one shaky anti-parasitic plus one unproven supportive bundle.

### #27 Maternal vaccine + BKI + beta-glucan
- **Fatal flaw:** This is even weaker than #25. It combines:
  - a maternal vaccine with marginal/mostly non-significant field data and duration mismatch,
  - BKI needing formulation resolution,
  - beta-glucan with likely timing mismatch and no crypto-specific efficacy.
- **Evidence:** Every component has a major unresolved failure mode; no pairwise or triple-combination data are presented.
- **Why kill:** This should not survive. It is a conceptual stack of wounded parts.

### V6 Dual CpGT1 + CpGT2 blockade
- **Fatal flaw:** Reaper treats the glucose-6-phosphate specificity as a “real selectivity handle,” but that does not solve the biggest issue: **cell entry and transporter-face accessibility**. If the parasite transporters are not accessible from the luminal side with a charged G6P mimetic, the chemistry becomes nearly impossible. Phosphate-containing molecules are notoriously permeability-poor and formulation-challenging.
- **Evidence:** No compounds, no structural validation, no proof that a dual inhibitor can reach both transporters in the parasite membrane at effective concentrations in vivo. Also, redundancy means partial inhibition is likely useless.
- **Why kill:** This is elegant genetics with no practical medicinal chemistry path yet.

### V9 CpROM1 rhomboid protease
- **Fatal flaw:** Survives “barely” despite the central mechanism being highly uncertain. If GP900 is not the relevant substrate, the whole proposal collapses, and Reaper admits Crypto-specific functional data are limited. This is effectively a one-experiment hypothesis, not a validated target.
- **Evidence:** Extrapolation from Toxoplasma/Plasmodium rhomboids to Cryptosporidium is dangerous because invasion biology differs materially. No calf or even convincing parasite-stage functional package is cited.
- **Why kill:** Too speculative for survival; should be wounded pending direct substrate-function proof.

### V13 CpFAS1 megasynthase
- **Fatal flaw:** Reaper lets this survive on uniqueness/selectivity, but the actual disease-relevant biology is still unclear. The proposed role in oocyst wall / VLCFA biology is **inferred**, not shown. If host lipid scavenging compensates, target vulnerability may be low.
- **Evidence:** Cerulenin is a dirty tool compound; inhibition of a KS domain in vitro is not proof that the intact megasynthase is a tractable in vivo target. No animal efficacy, no direct essentiality package tied to the proposed vulnerable stage.
- **Why kill:** Unique ≠ validated. This looks like a biochemical curiosity more than a de-risked target.

---

## SINGLE-LAB DEPENDENCIES

### #7 CpPDE1 inhibitors
- **Lab:** Likely Striepen-associated 2024 Nature Communications effort.
- **Dependency:** The key package—genetic validation, resistance mutant, and in vivo mouse efficacy—appears to come from essentially one research program/publication stream. Reaper says it survived on that paper; that is near single-lab dependence.

### V6 Dual CpGT1 + CpGT2 blockade
- **Lab:** Striepen lab.
- **Dependency:** Surviving rationale relies on the 2024 genetic redundancy/essentiality story from one lab.

### V9 CpROM1
- **Lab:** Likely essentially one small body of Crypto-specific work.
- **Dependency:** The survival case depends on inferred apicomplexan homology rather than broad independent Crypto replication; any direct Crypto support seems thin and non-replicated.

### V13 CpFAS1
- **Lab:** Likely one main group/source for Crypto FAS1 biochemistry.
- **Dependency:** Survives on limited biochemical observations without broad independent confirmation.

### #16 / #22 meloxicam, enhanced ORT
- **Dependency note:** Not single-lab in the strictest sense because pieces come from Blikslager/Gookin and standard veterinary use, but the **crypto-specific mechanistic support** is surprisingly narrow and old. Not a pure single-lab dependency, but close to “single-study dependency” for the central translational claim.

---

## MISSING KILL TESTS

### #2 BKI / CpCDPK1
- **Failure mode:** **Kinase target vulnerability may not translate under field-stage timing.** If CDPK1 inhibition mainly affects invasion and early development, treatment after peak epithelial colonization may underperform in naturally infected calves.
- **Likelihood:** Moderate.

### #2 BKI / CpCDPK1
- **Failure mode:** **Resistance via non-gatekeeper mechanisms** such as efflux, altered uptake, or compensatory signaling. Reaper focused mostly on gatekeeper mutation.
- **Likelihood:** Moderate.

### #7 CpPDE1
- **Failure mode:** **Severe stage- or host-context dependence.** Egress blockade shown in immunocompromised mice may not map to calves if drug exposure or stage distribution differs.
- **Likelihood:** Moderate.

### #7 CpPDE1
- **Failure mode:** **Host PDE cross-reactivity in gut tissue** causing secretory or motility side effects even without systemic exposure.
- **Likelihood:** Moderate.

### #16 / #22 meloxicam-containing regimens
- **Failure mode:** **Field hydration dependence.** NSAID safety and benefit may collapse when calves are not aggressively rehydrated, which is common in commercial settings.
- **Likelihood:** High.

### #16 / #22
- **Failure mode:** **Symptom masking without outcome improvement.** Reduced diarrhea scores may not improve weight gain, mortality, or shedding and could delay escalation of care.
- **Likelihood:** High.

### #25 / #26 / #27 combinations
- **Failure mode:** **Operational non-implementability.** Even if biologically rational, the complexity of combined biologic + small molecule + supplement regimens in neonatal calves can be fatal commercially.
- **Likelihood:** High.

### V6 Dual CpGT1+GT2
- **Failure mode:** **Charged inhibitor chemistry trap.** Selective G6P-mimetic inhibitors may be too polar to access the transporter binding site in vivo or too unstable in the gut.
- **Likelihood:** High.

### V9 CpROM1
- **Failure mode:** **Wrong substrate biology.** Rhomboid cleavage may be dispensable or compensated in Crypto despite being important in related apicomplexa.
- **Likelihood:** High.

### V13 CpFAS1
- **Failure mode:** **Metabolic bypass through host lipid scavenging.** Unique enzyme may be non-vulnerable because the parasite can salvage enough lipid under in vivo conditions.
- **Likelihood:** Moderate to high.

### #1 MMV665917
- **Failure mode Reaper underweighted:** **Unknown mechanism may imply polypharmacology / host-directed toxicity**, making optimization impossible even if efficacy replicates.
- **Likelihood:** Moderate.

### #8 Bovicrypt and #5/#9 antibody approaches
- **Failure mode:** **Antigen shedding / decoy binding.** Soluble or shed parasite glycoproteins could soak up antibodies/nanobodies before they reach functional targets.
- **Likelihood:** Moderate.

### All intracellular/extracytoplasmic parasite targets
- **Failure mode:** **Niche access illusion.** HCT-8 and even mouse efficacy can overstate access to the parasite in the neonatal calf ileum with mucus, milk components, transit, and epithelial turnover.
- **Likelihood:** High across the portfolio.

---

### OpenRouter (grok-4-07-09)

## WRONG KILLS (Targets killed that should survive)
- **Candidate #4: Halofuginone + Sustained-Release Reformulation**. The agent's kill reasoning relies on an overly rigid interpretation of the cryptostatic mechanism and the Martian's 80% suppression threshold, assuming sustained-release can't meaningfully alter the replication kinetics. This is wrong because the agent's math ignores potential for sustained higher trough concentrations to push suppression beyond 80%—halofuginone's dose-response curve in vitro shows near-complete replication halt at peak levels, and sustained delivery could maintain that without toxicity spikes. Evidence supporting the target includes replicated calf studies (e.g., Schaefer et al., 2012, showing 70-90% shedding reduction) and the fact that halofuginone is already approved and used commercially, proving real-world tolerability. Verdict should be WOUNDED, requiring a PK study of sustained-release formulation to confirm >80% sustained suppression.

- **Candidate #17: Recombinant Bovine IFN-gamma + COX-2 Inhibitor**. The kill is based on repetition of rBoIL-12 failure and assuming IFN-gamma can't access the extracytoplasmic niche, but this overlooks the combination's novelty: COX-2 inhibition could relieve PGE2-mediated suppression, enabling IFN-gamma to induce iNOS effectively, as suggested by in vitro models where PGE2 blockade restores IFN-gamma efficacy (e.g., Gookin et al., 2008). Evidence includes bovine ileal data showing IFN-gamma reduces parasite burden ex vivo (Blikslager et al., 2001), and the agent's dismissal of oral protein delivery ignores mucoadhesive formulations proven for cytokines in calves. Verdict should be WOUNDED, pending a low-cost ex vivo combination test in bovine tissue.

- **Vulcan IP5: Aldolase (Non-Redundant Glycolytic Chokepoint)**. The fatal flaw cited is host selectivity due to high conservation, but this underestimates structural differences: Vulcan noted at least 3 active-site residues differ, and AF3 predictions could reveal exploitable pockets for selective inhibition, similar to selective glycolytic inhibitors in other parasites (e.g., Plasmodium enolase inhibitors). Evidence includes CpAldolase's essentiality via CRISPR (no bypass in glycolysis), and no actual cross-inhibition data exists yet—killing on speculation is premature. Verdict should be WOUNDED, requiring CpAldolase crystal structure and bovine aldolase inhibition assays to assess real selectivity.

## WRONG SURVIVALS (Targets that survived but should be killed)
- **Candidate #2: BKI-1553 / Next-Generation BKIs (CpCDPK1 Inhibitors)**. Fatal flaw is the unaddressed resistance risk: the agent downplayed gatekeeper mutations, but in related apicomplexans (Toxoplasma, Plasmodium), CDPK1 gatekeeper mutations confer full resistance with minimal fitness cost (e.g., Donald et al., 2006, showing rapid selection in vivo). C. parvum's high replication rate (8x per cycle) amplifies this, and no BKI resistance studies exist for Crypto—field resistance could emerge in one season. Cite: Surveyor's confirmation of conserved gatekeeper, but agent's "theoretical" dismissal ignores empirical evidence from analogs.

- **Candidate #7: CpPDE1 Inhibitors (Pyrazolopyrimidines)**. Fatal flaw is the incomplete validation of the target: the agent accepted CRISPR V900A as proof, but the 2024 paper shows the mutant only partially alters susceptibility, and with 3 PDEs in the genome, redundancy could allow bypass (e.g., cgd6_4020 compensating for cGMP degradation). Mouse efficacy is from one study, and no data on autoinfection persistence—trapped parasites might still autoinfect via alternative egress. Cite: Surveyor noted 3 PDEs, and agent's dismissal ignores functional redundancy evidence in apicomplexans (e.g., Plasmodium PDE-beta compensation).

- **Vulcan IP6: Dual CpGT1 + CpGT2 Glucose Transport Blockade**. Fatal flaw is the delivery barrier in the extracytoplasmic niche: even with glucose-6-phosphate mimics, the compound must access the parasite from the lumen without host absorption, but peristalsis and mucus dilute luminal concentrations, and no in vivo proof exists for dual blockade efficacy. Vulcan's estimate assumes complete starvation, but parasites can switch to amylopectin reserves for 48+ hours, sustaining autoinfection. Cite: Striepen lab's 2024 data shows reserves last multiple cycles, and agent's survival ignores this metabolic adaptation seen in Toxoplasma (Blume et al., 2009).

## SINGLE-LAB DEPENDENCIES
- **Candidate #7: CpPDE1 Inhibitors (Pyrazolopyrimidines)**. All supporting data (CRISPR validation, mouse efficacy, mutant analysis) comes from the Striepen lab at University of Pennsylvania (2024 Nature Communications paper and related works). Dependency: No independent replication of egress blockade or oral efficacy; if the lab's immunocompromised mouse model overstates translation, the target collapses.

- **Vulcan IP9: CpROM1 Rhomboid Protease**. All functional data on CpROM1 (GP900 cleavage, invasion role) derives from the Striepen lab (e.g., 2024 mBio and prior papers). Dependency: No external confirmation of rhomboid's essentiality or substrate breadth; reliance on one group's immuno-EM and in vitro assays risks overinterpretation of GP900's importance.

- **Vulcan IP13: CpFAS1 Megasynthase**. Validation (VLCFA role inference, cerulenin IC50) is solely from the Striepen lab (2024 publications). Dependency: No independent oocyst wall integrity assays or CpFAS1 knockout data; if VLCFAs prove non-essential for walls (as in some apicomplexans), the target's foundation fails.

## MISSING KILL TESTS
- **Candidate #16: COX-2 Inhibitor / Meloxicam**. Failure mode: Long-term renal impact in dehydrated calves under field conditions—agent considered acute safety but not chronic effects like NSAID-induced nephropathy, which could worsen mortality in herds with variable hydration support. Likelihood: High (30-50%), as veterinary literature shows meloxicam exacerbates renal stress in dehydrated neonates (e.g., studies in lambs, analogous to calves).

- **Candidate #22: Enhanced ORT -- Glutamine + Meloxicam**. Failure mode: Glutamine overload causing osmotic diarrhea—agent ignored that excess glutamine in malabsorptive states can draw water into the lumen, potentially counteracting anti-secretory benefits. Likelihood: Medium (20-40%), based on human pediatric trials where high-dose glutamine worsened diarrhea in infectious enteritis.

- **Candidate #25: Triple Combination (BKI + Nanobody + Beta-Glucan)**. Failure mode: Immunological interference between components—beta-glucan primes innate immunity, but nanobodies could trigger anti-VHH responses that neutralize the cocktail, and BKI's luminal action might alter gut microbiota affecting glucan efficacy. Likelihood: High (40-60%), as combinations in neonatal guts often show unexpected antagonisms (e.g., vaccine-adjuvant interactions in calves).

- **Vulcan IP13: CpFAS1 Megasynthase**. Failure mode: Compensatory lipid import from host—agent didn't consider that inhibiting CpFAS1 might upregulate feeder organelle transporters to bypass VLCFA synthesis, sustaining oocyst walls. Likelihood: Medium (25-50%), inferred from apicomplexan metabolic plasticity (e.g., Toxoplasma scavenges host lipids under FAS stress).

---

### OpenRouter (gemini-2.5-pro)

## WRONG KILLS (Targets killed that should survive)

**Candidate #17: Recombinant Bovine IFN-gamma + COX-2 Inhibitor**

*   **Why the Kill is Wrong:** The agent's kill reasoning is based on a fallacious equivalence. It argues that because rBoIL-12 (which stimulates IFN-gamma) failed, giving IFN-gamma directly will also fail. This is a failure of imagination. The 2006 Pasquali study is not the final word on apicomplexan immunology; it is a single data point. The agent's own analysis of Candidate #16 (Meloxicam) correctly identifies that PGE2-mediated immunosuppression is a critical, un-tested variable. The failure of rBoIL-12 could be because the induced IFN-gamma was immediately suppressed by PGE2. The proposed combination directly tests this hypothesis: provide the effector cytokine (IFN-gamma) while simultaneously removing the brake (COX-2 inhibitor). This is a fundamentally different experiment than the one that failed in 2006.
*   **Evidence for Survival:** The core biology is sound: IFN-gamma is the primary cytokine responsible for controlling *Cryptosporidium*. The agent's own analysis of #16 and #22 validates the anti-secretory and potential immunomodulatory role of COX-2 inhibition. The combination is a rational, hypothesis-driven attempt to make the calf's own primary defense mechanism work in the face of parasite-induced suppression.
*   **What the Verdict Should Be:** **WOUNDED**. The kill based on "repetition" is premature. The cost and delivery of rBoIFN-gamma are legitimate and severe commercial hurdles, but they are *development* problems, not fatal *biology* problems. The core biological hypothesis—that removing the PGE2 brake will allow IFN-gamma to function—has never been tested and remains valid. The candidate should be wounded, with the graduation requirement being a small-scale ex vivo or organoid study showing that IFN-gamma + meloxicam is more effective at controlling parasite replication in bovine cells than either agent alone.

## WRONG SURVIVALS (Targets that survived but should be killed)

**Candidate #2: BKI-1553 / Next-Generation BKIs (CpCDPK1 Inhibitors)**

*   **The Flaw:** The agent dramatically underestimates the resistance risk. It is flagged as a "moderate concern" but it is a fatal, time-bound flaw. The mechanism of resistance is a single point mutation in the gatekeeper residue. In a disease characterized by exponential replication (8x every 12-14h) and autoinfection, the parasite population generates billions of variants per day in a single calf. The selection pressure for a gatekeeper mutant under BKI treatment will be immense. The first calf treated with a BKI monotherapy will be a resistance-generation factory. The idea that a "fitness cost" will prevent this is wishful thinking; the fitness cost is irrelevant when the alternative is death by drug.
*   **Evidence:** The agent itself cites the rapid emergence of resistance to a MetRS inhibitor in calves. CpCDPK1 is no different—a single-gene target for a fast-replicating parasite. The entire BKI strategy, which relies on selectivity via that same gatekeeper residue, is built on a foundation that will inevitably crumble. A sustained-release bolus only makes it worse, ensuring constant, sub-lethal drug concentrations at the tail end of release, which is the perfect environment for selecting for resistance. This target should be **KILLED** as a monotherapy. It is only viable in a combination from day one, which the portfolio does not mandate.

**Candidate #7: CpPDE1 Inhibitors (Pyrazolopyrimidines)**

*   **The Flaw:** The agent dismisses the risk

---

### OpenRouter (qwen-2.5-72b-instruct)

## WRONG KILLS (Targets killed that should survive)
### Candidate #4: Halofuginone + Sustained-Release Reformulation
**Why the kill is wrong:** While halofuginone is indeed cryptostatic, the sustained-release reformulation addresses the primary weakness of the drug: its short half-life and the resulting inter-dose troughs. By maintaining a constant luminal concentration, the reformulation can potentially overcome the cryptostatic ceiling and provide a more consistent therapeutic effect. The agent's argument that sustained-release does not change the drug's potency is overly simplistic. Continuous exposure can have a cumulative effect that is not achievable with intermittent dosing.
**Evidence supporting the target:** Sustained-release formulations have shown success in other areas of veterinary medicine, such as the use of long-acting antibiotics and anti-parasitics. The pharmacokinetic profile of halofuginone in calves has been well-characterized, and sustained-release formulations have been developed for other drugs with similar properties.
**Verdict should be:** WOUNDED. The sustained-release reformulation should be tested in a calf model to determine if it can overcome the cryptostatic ceiling.

### Candidate #17: Recombinant Bovine IFN-gamma + COX-2 Inhibitor
**Why the kill is wrong:** The combination of rBoIFN-gamma and a COX-2 inhibitor addresses two key issues: the immunosuppressive environment created by PGE2 and the need for a strong innate immune response. While rBoIL-12 failed, it did not directly provide IFN-gamma, and the combination with a COX-2 inhibitor could potentially overcome the limitations of the previous approach.
**Evidence supporting the target:** The PGE2-mediated immunosuppression hypothesis is well-supported by the literature. COX-2 inhibitors have been shown to enhance immune responses in other contexts, and the combination of IFN-gamma and COX-2 inhibition has shown promise in preclinical models.
**Verdict should be:** WOUNDED. The combination should be tested in a calf model to determine if it can overcome the limitations of rBoIL-12.

### Candidate #23: Serotonin (5-HT3) Receptor Antagonist (Ondansetron)
**Why the kill is wrong:** Ondansetron has a well-established safety profile in veterinary use and has been shown to reduce intestinal motility, which could potentially reduce the contact time between oocysts and enterocytes. While the agent is concerned about the potential to worsen infection, this is a hypothesis that can be tested.
**Evidence supporting the target:** Ondansetron has been used in veterinary medicine for anti-emetic purposes and has a well-characterized pharmacokinetic profile. The reduction in motility could potentially reduce the severity of diarrhea and the spread of infection.
**Verdict should be:** WOUNDED. The effect of ondansetron on C. parvum infection in calves should be tested in a controlled study.

## WRONG SURVIVALS (Targets that survived but should be killed)
### Candidate #2: BKI-1553 / Next-Generation BKIs (CpCDPK1 Inhibitors)
**What the flaw is:** While BKIs have shown promise in vitro and in mouse models, the lack of in vivo efficacy in calves is a significant concern. The agent's argument that the hERG optimization cycle explains the 10-year timeline is not sufficient. The failure to translate to in vivo efficacy in the target species is a critical flaw.
**Evidence:** Despite over a decade of research, no in vivo proof-of-concept in calves has been demonstrated. The lack of progress in advancing BKIs to a clinical stage in calves is a red flag.
**Verdict should be:** KILLED. The lack of in vivo efficacy in calves is a fatal flaw that cannot be ignored.

### Candidate #7: CpPDE1 Inhibitors (Pyrazolopyrimidines)
**What the flaw is:** While the genetic validation and mouse efficacy data are promising, the lack of calf data is a significant concern. The agent's argument that the IFN-gamma KO mouse model partially models the neonatal calf's immunological state is not sufficient. The species-specific differences in the immune response and the gut environment are critical.
**Evidence:** The 2024 Nature Communications paper provides genetic validation and mouse efficacy data, but no calf data. The lack of in vivo efficacy in the target species is a critical flaw.
**Verdict should be:** KILLED. The lack of calf data is a fatal flaw that cannot be ignored.

### Candidate #16: COX-2 Inhibitor / Meloxicam (Anti-Secretory + Immunosuppression Relief)
**What the flaw is:** While meloxicam has a strong safety profile and ex vivo data showing electrolyte absorption restoration, the agent's concern about the anti-secretory effect masking diarrhea severity without reducing parasite burden is valid. The immunomodulation hypothesis is unproven, and the anti-secretory effect alone may not be sufficient to justify the clinical trial.
**Evidence:** The ex vivo data from Blikslager et al. (2001) and Gookin et al. (2008) are strong, but the lack of in vivo calf data and the potential for the anti-secretory effect to mask disease severity are significant concerns.
**Verdict should be:** WOUNDED. The combination should be tested in a calf model to determine if it can reduce parasite burden and not just mask symptoms.

## SINGLE-LAB DEPENDENCIES
### Candidate #1: MMV665917 (Piperazine-Based Cryptosporicidal)
**Lab Dependency:** All efficacy data comes from the Huston lab (University of Vermont) and the Tzipori lab (Tufts). There is zero independent replication of the 94% shedding reduction in calves, the parasiticidal mechanism, or the NOD SCID mouse cure.

### Candidate #19: Recombinant Mucin-Like Glycoprotein Decoy
**Lab Dependency:** All data comes from the Striepen group. The MAb 1A5-reactive heterodimer was only characterized in 2023, and nobody has independently confirmed the attachment-blocking observation.

### Candidate #24: Wnt Pathway Activator (Post-Infection Recovery)
**Lab Dependency:** All Wnt pathway data is from mouse enteroids (Zhang et al., 2016). No bovine Wnt pathway characterization during or after Crypto infection exists.

## MISSING KILL TESTS
### Candidate #2: BKI-1553 / Next-Generation BKIs (CpCDPK1 Inhibitors)
**Failure Mode:** Species-specific pharmacokinetics and pharmacodynamics. The agent did not consider the potential differences in drug metabolism and distribution between mice and calves, which could significantly impact the efficacy of BKIs in the target species.
**Likelihood:** High. The differences in gut physiology and immune response between mice and calves are well-documented and could be a critical barrier to translation.

### Candidate #7: CpPDE1 Inhibitors (Pyrazolopyrimidines)
**Failure Mode:** Species-specific target expression and function. The agent did not consider the potential differences in CpPDE1 expression and function between mice and calves, which could impact the efficacy of the inhibitors in the target species.
**Likelihood:** High. The differences in gene expression and function between species are well-documented and could be a critical barrier to translation.

### Candidate #16: COX-2 Inhibitor / Meloxicam (Anti-Secretory + Immunosuppression Relief)
**Failure Mode:** Species-specific immune response. The agent did not consider the potential differences in the immune response to COX-2 inhibition between calves and other species, which could impact the efficacy of the drug in reducing parasite burden.
**Likelihood:** Moderate. The differences in immune response between species are well-documented and could be a significant barrier to translation.

---

### OpenRouter (claude-4.6-opus-20260205)

# Independent Challenge of Kill Report

## WRONG KILLS (Targets killed that should survive)

### Candidate #4: Halofuginone Sustained-Release

The kill reasoning overstates the case. The agent claims halofuginone's cryptostatic ceiling is "insurmountable" and cites the Martian's >80% suppression threshold. But this threshold is a model output, not empirical data, and the model's assumptions about replication rate, immune engagement timing, and dose-response shape are all uncertain. More critically, the agent dismisses sustained-release by saying it "only eliminates concentration fluctuations" — but this is precisely the problem with halofuginone in practice. The current failure mode is inter-dose troughs allowing parasite rebound. Eliminating troughs could shift the effective suppression from the current ~25% improvement (with fluctuating levels) to something substantially higher at constant near-maximum tolerable concentration.

The resistance argument (MetRS resistance in days) is also misleading. MetRS and ProRS are different enzymes with different structural constraints. Halofuginone resistance in Plasmodium requires specific ProRS mutations that substantially reduce catalytic efficiency. The cross-class extrapolation is not rigorous.

**However**, I ultimately agree the kill is defensible — not because of the "cryptostatic ceiling" argument, but because the therapeutic index is genuinely razor-thin (LD50/ED50 ratio ~2-3x in calves), and sustained-release at near-maximum tolerable concentration for 14 days amplifies the cumulative toxicity risk. The kill stands, but for the wrong primary reason. The agent should have led with the therapeutic index problem, not the cryptostatic ceiling model.

**Verdict: Kill stands, but reasoning is partially flawed.**

### Candidate #17: rBoIFN-gamma + COX-2 Inhibitor

The kill reasoning contains a logical error. The agent states "rBoIL-12 already PROVED that IFN-gamma in calf gut does not protect." This is wrong. The Pasquali et al. (2006) study showed rBoIL-12 stimulated IFN-gamma production AND CD4+ T cell expansion but failed to reduce disease. The agent then argues this proves IFN-gamma itself is ineffective. But IFN-gamma knockout mice are HIGHLY susceptible to Cryptosporidium — IFN-gamma is demonstrably essential for clearance. The rBoIL-12 failure could mean: (a) the IFN-gamma produced was insufficient in magnitude, (b) the timing was wrong, (c) PGE2-mediated counter-regulation suppressed the downstream effectors, or (d) the extracytoplasmic niche shields the parasite. The agent conflates "IFN-gamma stimulation via IL-12 failed" with "IFN-gamma is irrelevant," which is not the same claim.

The cost argument ($200/calf for rBoIFN-gamma) IS fatal and sufficient to kill this as a standalone product. But the biological reasoning is sloppy and could mislead the team about the role of IFN-gamma in their broader portfolio strategy (e.g., beta-glucan and CpG-ODN both work partly through IFN-gamma).

**Verdict: Kill stands on commercial grounds, but the biological reasoning is wrong and should be corrected to avoid downstream errors.**

### Candidate #19: Mucin Glycoprotein Decoy

The kill is reasonable but the "single-lab" argument is overstated. The MAb 1A5-reactive heterodimer characterization may be from the Striepen group, but the broader biology of mucin-sporozoite interactions has been studied by multiple groups (Cevallos, Riggs, Widmer labs over decades). The agent treats this as if the entire concept rests on one 2023 paper, when the underlying biology of mucin-mediated attachment has a 20+ year literature base.

**Verdict: Kill stands on scalability/glycan grounds. The single-lab argument is overstated.**

---

## WRONG SURVIVALS (Targets that survived but should be killed)

### Candidate #7: CpPDE1 Inhibitors

The agent gave this a remarkably easy pass. Several critical issues were underweighted:

**Single-lab dependency.** The 2024 Nature Communications paper establishing CpPDE1 as a drug target comes from one research group (Bhatt/Bhatt-Bhargava or similar). The CRISPR validation, the pyrazolopyrimidine efficacy, and the mouse data are all from the same publication. The agent flagged single-lab dependency as a kill criterion for MMV665917 (#1) and Myb-M (V1) but did NOT apply the same standard to CpPDE1. This is inconsistent.

**The "egress blockade" mechanism is theoretical.** The agent states "trapped parasites cannot spread, cannot autoinfect, and are cleared by normal enterocyte turnover in 3-5 days." This is an elegant model, but the actual paper demonstrates reduced parasite burden in mice — it does not directly demonstrate egress blockade as the mechanism. The compound could be working through off-target effects, host PDE inhibition (pyrazolopyrimidines are a known human PDE scaffold), or other mechanisms. The CRISPR mutant alters susceptibility, confirming target engagement, but the downstream mechanism (egress blockade → clearance by enterocyte turnover) is inferred, not demonstrated.

**Human PDE cross-reactivity is dismissed too casually.** The agent says "eliminated by luminal formulation." But pyrazolopyrimidines are small lipophilic molecules — they WILL be absorbed. The same argument the agent used to dismiss luminal delivery of BH3 mimetics (#13: "BH3 mimetics are small molecules designed for cell permeability — they WILL be absorbed") applies equally to pyrazolopyrimidines. The inconsistency is glaring.

**No calf data whatsoever.** The agent accepted mouse-only data for CpPDE1 while wounding MMV665917 partly for thin calf data. MMV665917 at least HAS calf data showing 94% shedding reduction.

**Verdict: Should be WOUNDED, not SURVIVED.** Required: independent replication of the mouse efficacy, and demonstration that the mechanism is genuinely egress blockade (not off-target PDE inhibition). The single-lab standard must be applied consistently.

### Candidate V6: Dual CpGT1+CpGT2 Glucose Transport Blockade

The agent let this survive on the strength of the glucose-6-phosphate selectivity handle. But several problems were missed:

**No inhibitor exists.** There is no known small molecule that blocks CpGT1 or CpGT2. The "glucose-6-phosphate mimetic" is a concept, not a compound. The agent killed Candidate #20 (gametocyte blocker) for being "a wish, not a candidate" — the same logic applies here. There is no compound, no in vitro data, no structure for rational design.

**The dual-target requirement is a development nightmare.** You need ONE compound that hits BOTH transporters, or TWO compounds co-formulated. The agent acknowledges individual inhibitors are "worthless" due to redundancy. Designing a single pan-CpGT inhibitor requires structural knowledge of both transporters — which does not exist. This is a 5-10 year target identification and medicinal chemistry program before you even reach a lead compound.

**The 24-48 hour amylopectin reserve window.** The agent noted this but did not follow through. If the parasite can survive 24-48 hours on reserves, any transient drop in drug concentration (missed dose, formulation failure, transit variation) allows recovery. For a 14-day treatment window, this creates an extremely demanding PK requirement.

**Verdict: Should be WOUNDED at minimum.** Required: structural characterization of at least one CpGT, demonstration that a glucose-6-phosphate mimetic can block transport in vitro, and CRISPR double-knockout confirming lethality of dual blockade.

### Candidate V13: CpFAS1 Megasynthase

The agent let this survive "barely" but should have wounded it more seriously:

**The VLCFA-oocyst wall connection is entirely inferred.** No experiment has demonstrated that CpFAS1 products are incorporated into oocyst walls. The agent acknowledges this ("the role is INFERRED, not established") but then lets it survive anyway. If VLCFAs are used for general membrane biogenesis during intracellular development, CpFAS1 inhibition might affect all stages — or might be compensated by host-derived lipid import through the feeder organelle (the very lipid scavenging pathway that makes Crypto unusual).

**Cerulenin is not a drug.** It is a reactive natural product (epoxide) that covalently modifies KS domains non-selectively. It inhibits mammalian FASN, fungal FAS, and bacterial FabB/FabF. The "inherent selectivity" claim is overstated — cerulenin's selectivity for CpFAS1 over host FASN has not been demonstrated at pharmacologically relevant concentrations.

**Verdict: Should remain WOUNDED with stricter graduation criteria.** Required: demonstrate CpFAS1 product incorporation into oocyst walls, and identify a selective inhibitor (not cerulenin).

### Candidate #22: Enhanced ORT (Glutamine + Meloxicam)

The agent's enthusiasm here borders on advocacy rather than skepticism. Several issues:

**The Blikslager 2001 data is ex vivo.** The agent acknowledges this but then dismisses the ex vivo-to-in vivo gap by saying "I tried hard to find evidence of this failure mode. I could not." Absence of evidence is not evidence of absence. The ex vivo system uses Ussing chambers with controlled drug concentrations bathing both sides of the tissue. In vivo, glutamine must survive gastric acid, compete with jejunal absorption, and reach the ileum at therapeutic concentrations. Meloxicam must achieve sufficient mucosal concentration in inflamed, edematous tissue with altered blood flow. These are not trivial pharmacokinetic challenges.

**This is symptomatic treatment, not disease modification.** The agent correctly notes this but then argues it "survived Reaper with the cleanest bill of health." A symptomatic intervention that does not reduce parasite burden, does not shorten infection, and does not reduce transmission should not be in the same survival category as disease-modifying targets. It should be a supportive care recommendation, not a portfolio candidate competing for resources.

**Verdict: Survival is defensible as a low-risk adjunct, but the agent's framing as the #1 priority experiment is inappropriate for a drug discovery portfolio.** It should be clearly categorized as supportive care optimization, not a drug target.

---

## SINGLE-LAB DEPENDENCIES

| Target | Lab | Dependency |
|---|---|---|
| **#7 CpPDE1** | Single group (2024 Nat Comms paper) | ALL genetic validation, ALL compound efficacy data, ALL mouse in vivo data from one publication |
| **V1 Myb-M** | Striepen lab (UGA) | ALL conditional ablation data, ALL forced overexpression phenotype data |
| **V2 AP2-F** | Striepen lab (UGA) | ALL transcription factor characterization, ALL genetic ablation data |
| **V6 Dual CpGT** | Striepen lab (UGA) | ALL genetic redundancy data, ALL transporter characterization |
| **V9 CpROM1** | Limited groups | Functional data largely inferred from Toxoplasma/Plasmodium rhomboid biology, not CpROM1-specific experiments |
| **V13 CpFAS1** | Zhu lab (originally) | Biochemical characterization of the megasynthase; VLCFA role inferred |

**Critical note:** The Striepen lab dependency across V1, V2, V3, V6, and partially V9 means that a significant fraction of the surviving/wounded Vulcan targets rest on one laboratory's CRISPR platform and genetic tools. If there are systematic issues with the C. parvum genetic system (e.g., incomplete knockdowns being interpreted as essentiality, or compensatory mutations confounding phenotypes), multiple targets could fail simultaneously.

---

## MISSING KILL TESTS

### Candidate #2 (BKI/CpCDPK1) — Intracellular Niche Access
**Failure mode:** BKIs are kinase inhibitors optimized for cell permeability. The extracytoplasmic niche means the parasite is technically OUTSIDE the host cell cytoplasm. If BKIs achieve efficacy primarily through fecal/luminal contact (as the agent notes — "fecal concentration predicts efficacy better than plasma"), then the compound may never actually reach the intracellular CDPK1 enzyme at sufficient concentration. The efficacy could be driven by an off-target luminal mechanism (e.g., direct sporozoite/merozoite toxicity independent of CDPK1). This would mean the entire CDPK1 target validation is irrelevant to the actual mechanism of action in vivo.
**Likelihood:** Low-moderate. The CDPK1 crystal structure with BKI bound is solid, and the glycine gatekeeper selectivity mechanism is well-characterized. But the disconnect between fecal concentration driving efficacy and an intracellular kinase target has not been mechanistically resolved.

### Candidate #2 (BKI/CpCDPK1) — Formulation Feasibility for Sustained-Release Bolus
**Failure mode:** The agent identifies sustained-release bolus as the key unmet need and calls it "an engineering problem, not a biology problem." But sustained-release ruminal boluses for neonatal calves do not exist as a commercial product class. Neonatal calves have a functional abomasum (not rumen) — the reticulorumen is undeveloped. Standard cattle boluses are designed for the adult rumen. A sustained-release device for the neonatal abomasum/small intestine is an entirely different engineering challenge with no precedent.
**Likelihood:** Moderate-high. This is not a trivial engineering problem and could be a program-killing formulation barrier.

### Candidate #16 (Meloxicam) — Prostaglandin-Dependent Mucosal Defense
**Failure mode:** COX-2-derived prostaglandins (especially PGE2) are not only pro-secretory — they are also critical for mucosal defense, including mucus secretion, bicarbonate production, and mucosal blood flow. In a C. parvum-damaged ileum, COX-2 inhibition could impair the remaining mucosal defense mechanisms, slow epithelial repair, and worsen barrier dysfunction. The Blikslager ex vivo data shows electrolyte absorption restoration but does NOT measure mucosal integrity, barrier function (transepithelial resistance), or repair capacity over time.
**Likelihood:** Moderate. NSAID-induced intestinal injury is well-documented in multiple species. The agent dismissed this for meloxicam based on its safety profile at standard doses, but standard dosing studies were not conducted in actively C. parvum-infected neonates with compromised mucosal barriers.

### Candidate #7 (CpPDE1) — Redundancy with Other PDEs
**Failure mode:** The agent notes 3 PDEs exist but dismisses redundancy because the CRISPR V900A mutant confirms CpPDE1 as the pyrazolopyrimidine target. This misses the point. The question is not "which PDE does the drug hit?" but "can the parasite compensate for CpPDE1 inhibition by upregulating cgd6_4020 or cgd6_500?" Genetic point mutation (V900A) and pharmacological inhibition are different — a V900A mutant has an altered protein, while drug-treated parasites have a blocked protein. Compensatory upregulation of other PDEs could rescue cGMP signaling under drug pressure but would not rescue a structurally altered CpPDE1.
**Likelihood:** Low-moderate. Depends on whether the other PDEs have overlapping substrate specificity and expression timing.

### All Surviving Anti-Parasitic Targets — The Autoinfection Escape Problem
**Failure mode not systematically tested:** Every anti-parasitic candidate assumes that reducing the replication rate or blocking a specific lifecycle stage will reduce disease burden. But the autoinfection cycle (thin-walled oocysts → immediate re-invasion) means that even brief interruptions in drug coverage allow exponential recovery. The agent applied this test to some candidates (bile salt sequestrant, beta-glucan) but did NOT systematically apply it to BKIs, CpPDE1, or the glucose transport blockade. For BKIs specifically

---

### OpenRouter (deepseek-r1)

## WRONG KILLS (Targets killed that should survive)
None. The agent's kill decisions are well-justified based on the evidence provided. Each killed candidate has a clear, mechanistic fatal flaw that aligns with the kill tests.

## WRONG SURVIVALS (Targets that survived but should be killed)
**Candidate #7: CpPDE1 Inhibitors (Pyrazolopyrimidines)**  
**Fatal Flaw:** All supporting data come from a single lab (Striepen lab, 2024 Nature Communications paper). There is no independent replication of the CRISPR validation or mouse efficacy. Additionally, the mouse model used immunocompromised IFN-gamma KO mice, which may not fully recapitulate the neonatal calf immune context. The agent overlooked the single-lab dependency risk and the possibility of PDE redundancy (three PDEs exist in C. parvum). Without independent validation, this target is too early to "survive"; it should be wounded pending replication.

**Candidate #25: Triple Combination (BKI + Nanobody + Beta-Glucan)**  
**Fatal Flaw:** This is not a specific drug target but a combination strategy. Each component is individually unproven (BKI needs formulation, nanobodies don't exist for Crypto, beta-glucan timing is mismatched). Combining three high-risk candidates does not mitigate their individual flaws; it multiplies regulatory, development, and cost barriers. The agent should have killed this as a non-candidate or relegated it to a conceptual strategy.

**Candidate #26: Enhanced ORT + MMV665917**  
**Fatal Flaw:** This combination inherits the fatal flaws of MMV665917 (single-lab dependency, unknown target, high dose). MMV665917 is wounded and may not graduate. Combining it with a symptomatic treatment does not rescue its fundamental risks. This is not a standalone target and should be killed as a candidate.

**Candidate #27: Maternal Vaccine + BKI + Beta-Glucan**  
**Fatal Flaw:** Similar to #25, this is a combination of unvalidated components. The maternal vaccine (Bovicrypt) has not demonstrated cross-subtype efficacy and provides only 2–3 days of coverage. BKI requires sustained-release formulation not yet achieved. Beta-glucan's immune priming is mismatched to the 14-day vulnerability window. The "layered protection" architecture is speculative and does not qualify as a drug candidate.

**V6: Dual CpGT1 + CpGT2 Glucose Transport Blockade**  
**Fatal Flaw:** All genetic data come from the Striepen lab (single-lab dependency). The requirement for continuous dual inhibition for 14 days poses a formidable formulation challenge: maintaining effective luminal concentrations of a glucose-6-phosphate mimetic across the entire ileum for two weeks is likely commercially unviable. The agent underestimated the delivery hurdle.

**V9: CpROM1 Rhomboid Protease**  
**Fatal Flaw:** The target is supported by a single lab (Striepen), and the key substrate GP900 may not be essential for invasion (its role may be lubrication rather than adhesion). The agent's "clean falsifiable experiment" is still pending; until it is performed, the target remains high-risk and should be wounded, not survived.

**V13: CpFAS1 Megasynthase**  
**Fatal Flaw:** All data are from a single lab (Striepen). The role of VLCFAs in oocyst wall integrity is inferred, not proven. If VLCFAs are not required for oocyst formation, the target fails. This is a high-risk, early-stage hypothesis that should be wounded, not survived.

## SINGLE-LAB DEPENDENCIES
- **Candidate #7: CpPDE1 inhibitors** – All data from Striepen lab (2024 Nature Communications).
- **V6: Dual CpGT1+GT2 blockade** – All genetic data from Striepen lab.
- **V9: CpROM1 rhomboid protease** – All data from Striepen lab.
- **V13: CpFAS1 megasynthase** – All data from Striepen lab.
- **Candidate #1: MMV665917** (wounded) – All efficacy data from Huston/Tzipori labs (closely collaborating).

## MISSING KILL TESTS
**Candidate #7: CpPDE1 inhibitors**  
**Failure mode:** Off-target effects on host PDEs. Even with luminal delivery, some systemic absorption is likely, and host PDE inhibition (especially PDE5) could cause cardiovascular or other side effects in neonates.  
**Likelihood:** Moderate; PDE inhibitors are known to have systemic effects.

**Candidate #2: BKI-1553 / Next-Generation BKIs**  
**Failure mode:** Sustained-release bolus formulation is not feasible for neonatal calves due to rumen development and gut size. Neonatal calves have a small abomasum and variable gut transit; a bolus that releases drug over 14 days may not be reliably retained or may cause obstruction.  
**Likelihood:** High; this is a major engineering hurdle not addressed by the agent.

**V6: Dual CpGT1+GT2 blockade**  
**Failure mode:** Continuous luminal concentration for 14 days is unachievable. The neonatal calf gut has high fluid turnover and peristalsis; maintaining effective inhibitor concentration across the entire ileum without repeated dosing is likely impossible.  
**Likelihood:** High; no existing veterinary drug achieves this.

**Candidate #16/22: Meloxicam/Enhanced ORT**  
**Failure mode:** NSAID-induced renal toxicity in dehydrated calves. Even selective COX-2 inhibitors can impair renal perfusion in hypovolemic animals. In field conditions, calves with cryptosporidiosis are often dehydrated, and meloxicam could precipitate acute kidney injury.  
**Likelihood:** Moderate; requires careful hydration management, which may not be feasible on all farms.

**Candidate #9: VHH Nanobody Cocktail**  
**Failure mode:** Immunogenicity of camelid-derived nanobodies in calves. Repeated dosing over 14 days could induce anti-nanobody antibodies, leading to clearance or hypersensitivity.  
**Likelihood:** Moderate; nanobodies are foreign proteins and may trigger an immune response.

---

