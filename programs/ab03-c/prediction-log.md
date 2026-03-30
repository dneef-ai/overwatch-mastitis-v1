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
