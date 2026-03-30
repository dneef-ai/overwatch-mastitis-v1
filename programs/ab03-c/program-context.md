# AB03-C Program Context — Drug Target Constraint

**Program:** AB03-C — Druggable Targets for Rumen H₂ Disposal
**Internal Agteria Program** (no partner)
**Date:** 2026-03-30

---

## The Problem

Same as AB03-A/B: when methanogenesis is inhibited in cattle, H₂ accumulates, shifting VFA profiles and reducing productivity. AB03 is an inhibitor-agnostic intervention.

## The Constraint

**This variant accepts ONLY druggable molecular targets.** Every candidate must be:

- A specific protein, enzyme, receptor, or nucleic acid target
- Modulable by a designed molecule: small molecule, peptide, peptidomimetic, antisense oligomer, morpholino, aptamer, or equivalent
- NOT a feed additive, supplement, electron acceptor, DFM, or material added in bulk

Acceptable modalities:
- Small molecule enzyme activators or inhibitors
- Allosteric modulators
- Peptide-based modulators (including stapled peptides, cyclic peptides)
- Antisense oligonucleotides, morpholinos, peptide-nucleic acids (PNA)
- Engineered enzymes delivered as protein therapeutics (cell-free)
- Small molecule transcription factor modulators
- Quorum sensing modulators

NOT acceptable:
- Feed additives (menadione, phloroglucinol, fumarate, nitrate)
- Bulk electron acceptors or redox mediators
- Direct-fed microbials (live organisms)
- Conductive materials (biochar, magnetite)
- Management interventions (dose optimization, diet changes)
- GMO organisms (engineered microbes released into rumen)

## Upstream Work (Already Complete)

This sprint builds on the disease maps, bottleneck consensus, and failure analyses from AB03-A and AB03-B. Both variants converged on:

- **Bottleneck:** NADH reoxidation at fermentation microsites, gated by dissolved H₂ partial pressure
- **Quantitative target:** Lower dissolved H₂ at microsites to <15 Pa
- **Three gates:** Population installation, H₂ threshold mismatch, spatial coupling
- **Key finding:** The biology works (electrons CAN be redirected) — failures are economic, toxicological, or ecological
- **Redox mediators confirmed experimentally:** Agteria independently chose Rhein (anthraquinone) and Menadione (naphthoquinone) for AB03, with in vivo Rhein trial upcoming. The pipeline converged on the same chemistry.

## Scoring: Likelihood of Success (Replaces 70% Test)

Every candidate must be scored on:

1. **Target Validation (0-25):** Is the target real, characterized, and causally linked to H₂ disposal or its consequences?
2. **Druggability (0-25):** Does the target have a binding pocket, known ligands, structural data, or precedent for modulation?
3. **Rumen Feasibility (0-25):** Can the drug survive rumen conditions (pH, proteases, anaerobic, 39°C, H₂S, 24-48h passage)?
4. **Magnitude of Effect (0-25):** If the drug works perfectly, what fraction of the H₂ problem does it address?

**Total: 0-100.** Scores >60 are development candidates. Scores 40-60 are research candidates. Scores <40 are conceptual only.

## Strategic Preference

Agteria is a drug discovery company. This is the modality where Agteria has the strongest IP position and the clearest differentiation from feed additive competitors. Novel molecular targets with clean patent claims are the goal.
