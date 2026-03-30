# Prediction Log — AB03-C: Druggable Targets for Rumen H2 Disposal

---

## Phase 3: Forge

### Prediction F1: Fumarate Reductase Activator In Vitro Proof of Concept

- **Prediction:** A small molecule allosteric activator screen against purified Wolinella succinogenes QFR (using the 2.2A crystal structure, PDB: 1QLB/1E7P) will identify at least one hit compound that increases fumarate reduction Vmax by >50% at 10 uM compound concentration, without increasing Km for fumarate.
- **Test:** High-throughput enzymatic screen (NADH oxidation-linked fumarate reduction assay) of 10,000-compound diversity library against purified QFR. Counter-screen against bovine succinate dehydrogenase (host Complex II) for selectivity.
- **If TRUE:** Fumarate reductase is a druggable activatable target. Proceed to testing in rumen fluid microcosms under 3-NOP. This validates the entire "catalytic vs. stoichiometric" thesis — a small molecule activator achieving the effect of fumarate supplementation without the substrate cost.
- **If FALSE (no hits):** The QFR active site/allosteric architecture does not accommodate small molecule activators. Pivot to Rnf complex or PEPCK as primary propionogenesis targets, or to enzyme engineering approaches (deliver engineered QFR with higher intrinsic Vmax as a protein therapeutic).

### Prediction F2: Rex Antagonist Derepresses Alternative Electron Disposal in Rumen Firmicutes

- **Prediction:** In Ruminococcus albus or Clostridium-type rumen isolates, a Rex knockout mutant (or a Rex DNA-binding-domain peptide competitor) will show >3-fold upregulation of lactate dehydrogenase, alcohol dehydrogenase, and/or formate-hydrogen lyase genes compared to wild type, and will produce >30% less H2 per mole glucose fermented in anaerobic batch culture.
- **Test:** Rex gene deletion in a culturable rumen Firmicute (R. albus or Clostridium sp.) using allelic exchange. Measure transcript levels of Rex regulon genes by RT-qPCR and H2 production per mole hexose in batch culture.
- **If TRUE:** Rex is a genuine drug target for RHAS — constitutive derepression of alternative electron disposal reduces H2 production. Proceed to Rex DNA-binding domain fragment screen for small molecule antagonists.
- **If FALSE (no change in H2 production):** Rex regulon in rumen Firmicutes does not control the relevant electron disposal pathways, or compensatory mechanisms exist. Deprioritize Rex as a target.

### Prediction F3: Rnf Activator Increases Propionate Output from Prevotella Under Elevated H2

- **Prediction:** In P. ruminicola cultures under 40 uM dissolved H2 (simulating RHAS), addition of a Rnf complex modulator (Na+ ionophore at sub-growth-inhibitory concentrations, as a proxy for enhanced Na+ cycling) will increase propionate:acetate ratio by >25% compared to control, by accelerating the Rnf-dependent redox balancing step.
- **Test:** Prevotella batch cultures under controlled H2 headspace (RHAS conditions). Compare VFA output with and without sub-inhibitory monensin (Na+/H+ antiporter — alters Na+ gradient) or valinomycin (K+ ionophore — indirectly affects Na+ gradient). Measure propionate, acetate, succinate, and redox state (NADH/NAD+ ratio).
- **If TRUE:** Rnf activity is genuinely rate-limiting for propionogenesis under RHAS conditions, and modulating the Na+ gradient (which drives Rnf) shifts VFA output toward propionate. This validates the Rnf activator approach and informs the mechanism for small molecule design.
- **If FALSE:** Rnf is not rate-limiting — the bottleneck is upstream (PEPCK) or downstream (succinate decarboxylase). Reprioritize the propionogenesis enzyme cascade.

### Prediction F4: Protozoal [FeFe]-Hydrogenase Inhibition Reduces Total H2 by >10% Without Affecting Bacterial Fermentation

- **Prediction:** In mixed rumen fluid under 3-NOP, selective delivery of a [FeFe]-hydrogenase inhibitor (formaldehyde at sub-bactericidal concentrations, or NO donor) to the protozoal fraction (via size-based filtration or density separation followed by treatment and re-mixing) will reduce total H2 production by >10% without decreasing total VFA production or substrate degradation.
- **Test:** Rumen fluid batch culture fractionation experiment. Separate protozoa by filtration (100 um mesh). Treat protozoal fraction with [FeFe]-hydrogenase inhibitor. Reconstitute with bacterial fraction. Measure H2, VFA, substrate disappearance. Compare to untreated control.
- **If TRUE:** Protozoal H2 production under RHAS is a meaningful and targetable fraction, and inhibition does not cascade to bacterial fermentation. This validates the protozoal [FeFe]-hydrogenase target and the source-reduction strategy.
- **If FALSE (<5% H2 reduction or VFA production decreases):** Either protozoal H2 is a smaller fraction than estimated, or bacterial hydrogenases are also affected. Deprioritize the protozoal hydrogenase target.

### Prediction F5: The NADH Reoxidation Zone Contains the Most Impactful Drug Target for RHAS

- **Prediction:** Among the three target zones tested in RUSITEC under 3-NOP (Zone 1: NADH-directed intervention using PFL-AE activator analog oxamate; Zone 2: propionogenesis enhancement using sub-stoichiometric fumarate at 10% of dose used in prior studies; Zone 3: acetogenesis enhancement using tungsten supplementation for HDCR), Zone 1 will produce the largest improvement in total VFA production and the greatest reduction in dissolved H2, because it directly addresses the rate-limiting gate identified by Tribunal.
- **Test:** RUSITEC experiment with 3-NOP at 50% CH4 inhibition. Four arms: (a) control, (b) oxamate at 1 mM (PFL-AE activator proxy), (c) fumarate at 5 mg/g DM (sub-stoichiometric), (d) sodium tungstate at 50 uM (HDCR metalation enhancer). Primary endpoint: total VFA production. Secondary: dissolved H2, VFA profile, hydrogen recovery.
- **If TRUE:** NADH reoxidation is confirmed as the highest-leverage drug target zone, validating the portfolio's primary strategy. All three Zone 1 targets (Rnf, Rex, PFL-AE) move to lead optimization.
- **If FALSE (Zone 2 or 3 wins):** The bottleneck is downstream of NADH reoxidation, and the propionogenesis or acetogenesis zones should be reprioritized. This would contradict the Tribunal's bottleneck determination and require revisiting the mechanistic model.

---

## Phase 3b: Surveyor

### Prediction S-1: Fumarate Reductase Activator Screens Will Fail

- **Prediction:** High-throughput screening of a diverse compound library (>10,000 compounds) against purified W. succinogenes FrdABCD will identify zero allosteric activators (compounds that increase Vmax >1.5x) despite the enzyme having excellent structural coverage (2.2 A crystal structures, multiple crystal forms).
- **Test:** Run HTS with Vmax readout for fumarate reduction; counter-screen for selectivity vs bovine SDH.
- **If TRUE:** Confirms that enzyme activators for this target class are not achievable with conventional screening. Redirects effort to fumarate supply (PEPC activation) or pathway engineering. ChEMBL data showing only inhibitors (nafuredin IC50 2.4 nM, pyrvinium 500 nM) supports this prediction — the binding site architecture favors inhibition.
- **If FALSE:** Opens the most direct route to RHAS treatment. Fumarate reductase activation becomes the lead program. This would be surprising and transformative.

### Prediction S-2: Phosphomycin Increases Propionate in Rumen Fluid

- **Prediction:** Phosphomycin (50-500 uM) added to rumen fluid in vitro under 3-NOP-mediated methanogenesis inhibition will increase propionate production by >20% and decrease dissolved H2 by >15%, validating PEPC as a druggable upstream bottleneck for propionogenesis.
- **Test:** In vitro rumen incubation with phosphomycin dose-response curve + 3-NOP at 50% methane inhibition. Primary endpoint: propionate concentration. Secondary: dissolved H2, total VFA, acetate:propionate ratio.
- **If TRUE:** PEPC activation via phosphomycin scaffold is the fastest path to a lead candidate. No host selectivity concern (mammals lack PEPC). Immediate lead optimization of phosphomycin analogs for rumen stability.
- **If FALSE:** PEPC is not rate-limiting for propionogenesis under RHAS; fumarate reductase Vmax or population size is the actual bottleneck. Computational finding of phosphomycin as activator is correct but target is not rate-limiting.

### Prediction S-3: Oxythiamine Shifts Electron Carrier from H2 to Formate

- **Prediction:** Oxythiamine (100 uM, PFOR inhibitor via TPP competition) added to rumen fluid under 3-NOP will increase formate concentration >5-fold and decrease dissolved H2 by >25%, with total VFA production maintained within 10% of control.
- **Test:** In vitro rumen incubation with oxythiamine + 3-NOP. Measure dissolved H2, formate, total VFA, individual VFA profiles.
- **If TRUE:** PFOR inhibition successfully redirects electron flow from H2 to formate without fermentation penalty. The TPP-[4Fe-4S] selectivity handle (unique to PFOR, absent from bovine PDH) enables selective drug design. Vulcan's V11 moves to development.
- **If FALSE:** PFOR inhibition causes unacceptable fermentation disruption (oxythiamine hits other TPP enzymes), or formate is rapidly consumed without benefiting H2 disposal.

### Prediction S-4: N-Oxide Antiprotozoals Reduce H2 While Maintaining VFA

- **Prediction:** The top N-oxide antiprotozoal compound (from the MDPI Metabolites 2019 screen) at its effective antiprotozoal concentration will reduce protozoal counts by >80%, decrease H2 production by >15%, and total VFA production will not decrease (may increase due to bacterial expansion filling the niche).
- **Test:** Rumen simulation (RUSITEC or batch) with N-oxide lead compound vs. monensin positive control vs. untreated control. Measure protozoal counts, H2, CH4, total VFA, individual VFA, microbial protein.
- **If TRUE:** Selective defaunation is a viable standalone RHAS intervention. The most immediately actionable target in the portfolio.
- **If FALSE:** Protozoal contribution to VFA/fiber degradation is more important than the H2 production benefit, or N-oxide selectivity is insufficient.

### Prediction S-5: Rex Regulon in Rumen Firmicutes Includes Propionogenesis Genes

- **Prediction:** Rex-regulated genes in R. albus or C. ruminicola include fumarate reductase (frdABCD) operon or other propionogenesis-related genes, meaning Rex antagonism would simultaneously derepress NADH disposal AND propionogenesis.
- **Test:** ChIP-seq or RNA-seq of rex-knockout vs. wild-type rumen Firmicute under elevated NADH/NAD+. Map all derepressed genes.
- **If TRUE:** Rex antagonism becomes a dual-mechanism target (derepresses both NADH disposal AND propionogenesis). Adjusted score increases to 75+. One of the most important findings for the portfolio.
- **If FALSE:** Rex regulon is limited to ethanol/lactate pathways. Derepression may produce undesirable fermentation products. Rex score remains at 68 but utility is narrower.

---

## Phase 4: Reaper

### Prediction R-1: Fumarate Reductase HTS Will Yield Zero Activators

- **Prediction:** A screen of >10,000 diverse compounds against purified W. succinogenes FrdABCD will identify zero allosteric activators (Vmax increase >1.5x).
- **Test:** Run HTS with Vmax readout.
- **If TRUE:** FrdABCD activator is dead. Redirects portfolio to PEPC/upstream substrate supply.
- **If FALSE:** FrdABCD activator becomes the #1 target in the portfolio.

### Prediction R-2: PFOR Inhibition Will Reduce H2 Less Than Predicted

- **Prediction:** Oxythiamine (100 uM) in rumen fluid under 3-NOP will reduce dissolved H2 by <15% (not the 25% predicted by Surveyor S-3), because many rumen bacteria either lack functional PFL or have limited PFL capacity.
- **Test:** In vitro rumen incubation with oxythiamine + 3-NOP. Measure H2, formate, VFA.
- **If TRUE:** PFOR inhibition is a supporting strategy, not a primary one. Need combination.
- **If FALSE:** PFOR inhibition is transformative. V11 becomes lead program.

### Prediction R-3: N-Oxide Antiprotozoals Will Impair Fiber Digestion

- **Prediction:** An N-oxide compound that reduces protozoal counts by >80% will also reduce NDF digestibility by >10%, offsetting the H2 reduction benefit.
- **Test:** Rumen simulation with N-oxide vs. control. Measure NDF digestibility alongside H2 and VFA.
- **If TRUE:** Partial defaunation (50-70% reduction) becomes the strategy. Full defaunation is off the table.
- **If FALSE:** Full defaunation is viable. V12 becomes lead monotherapy candidate.

### Prediction R-4: Phosphomycin Will Kill Rumen Bacteria Before Activating PEPC

- **Prediction:** In rumen fluid, phosphomycin at concentrations needed for PEPC activation (50-500 uM) will reduce bacterial viability by >50% via MurA inhibition, negating any propionogenesis benefit.
- **Test:** Phosphomycin dose-response in rumen fluid: measure bacterial CFU and propionate simultaneously.
- **If TRUE:** Phosphomycin scaffold must be modified to remove MurA activity. PEPC-selective analog is mandatory.
- **If FALSE:** Phosphomycin has a therapeutic window for PEPC activation in the rumen. Fast-track to in vivo.

### Prediction R-5: Rex Regulon in Rumen Firmicutes Does NOT Include frdABCD

- **Prediction:** The Rex regulon in R. albus or C. ruminicola does NOT include fumarate reductase genes. It is dominated by ethanol dehydrogenase and lactate dehydrogenase genes.
- **Test:** RNA-seq of rex-knockout vs. wild-type rumen Firmicute under elevated NADH/NAD+.
- **If TRUE:** Rex antagonism would primarily increase ethanol and lactate -- potentially causing ruminal acidosis. Rex is KILLED.
- **If FALSE:** Rex antagonism derepresses propionogenesis. Rex advances to development candidate.

---

## Phase 4b: Board

### Prediction B-1: PFOR Inhibition Will Be the Highest-Information Experiment in the Portfolio

- **Prediction:** The PFOR branch-point validation (Experiment 1) will produce the largest portfolio-restructuring decision of any single experiment. Either it validates the entire source-reduction strategy (GO) or it kills the highest-ranked target and forces a pivot to sink-enhancement (KILL).
- **Test:** Compare the number of portfolio decisions changed by Experiment 1 vs. Experiments 2 and 3.
- **If TRUE:** The Board's prioritization was correct.
- **If FALSE:** One of the other experiments produced a bigger surprise -- likely the Rex regulon (Experiment 3) being unexpectedly favorable.

### Prediction B-2: Ecological Compensation Will Reduce All In Vitro Effect Sizes by 15-30%

- **Prediction:** When any AB03-C intervention (PFOR inhibitor, N-oxide, PEPC activator) is tested in mixed rumen fluid (not pure culture), the observed H2 reduction will be 15-30% smaller than predicted from mechanism alone, due to community-level compensatory shifts in H2-producing populations.
- **Test:** Compare H2 reduction in pure-culture vs. mixed-rumen-fluid for oxythiamine and N-oxide compounds.
- **If TRUE:** The 20% ecological discount applied by the Board was appropriate. All single-target effect magnitude estimates should be further reduced.
- **If FALSE:** The rumen community does not compensate as rapidly as expected. Effect sizes are closer to mechanism-level predictions. This would be optimistic for the portfolio.

### Prediction B-3: The Rex Regulon Will Be Dominated by LDH, Not Propionogenesis Genes

- **Prediction:** RNA-seq of rex-knockout in R. albus will show >3-fold upregulation of ldh (lactate dehydrogenase) and adhE (alcohol dehydrogenase), but <1.5-fold change in frdABCD, fum, or mdh (propionogenesis genes). Rex antagonism would increase lactate production, not propionate.
- **Test:** Experiment 3 (Rex regulon characterization).
- **If TRUE:** Rex is killed. The most druggable target in the portfolio is biologically useless for RHAS.
- **If FALSE (regulon includes propionogenesis):** Rex immediately becomes the #1 drug target in the portfolio -- a druggable transcription factor that upregulates the most valuable H2 sink. This would be the most portfolio-transforming outcome of any single experiment.

### Prediction B-4: Phloroglucinol Reductase Will Be the Best Drug Target in AB03-C v2

- **Prediction:** When the phloroglucinol reductase is identified and characterized from rumen bacteria, it will score >70/100 on the AB03-C rubric because it combines (a) the strongest empirical validation of any target (50.6% H2 reduction in vivo), (b) a likely inhibitor/activator pocket on a soluble reductase, and (c) a direct mechanism for both H2 and formate disposal.
- **Test:** Formal Forge proposal for phloroglucinol reductase in AB03-C v2.
- **If TRUE:** The entire AB03-C pipeline should have started with reverse-engineering phloroglucinol.
- **If FALSE:** The phloroglucinol mechanism is too distributed or the reductase is not druggable.
