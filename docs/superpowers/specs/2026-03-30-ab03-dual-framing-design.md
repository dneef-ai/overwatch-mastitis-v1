# AB03 — Dual-Framing Pipeline Experiment

**Date:** 2026-03-30
**Program:** AB03 (internal Agteria)
**Partner:** None — internal R&D
**Status:** Design

---

## Problem Statement

When methanogenesis is inhibited in cattle (by any inhibitor — 3-NOP, Asparagopsis, halogenated compounds, etc.), the primary ruminal H₂ sink is removed. H₂ accumulates, shifting the NADH/NAD⁺ ratio, altering VFA profiles toward acetate, reducing fiber degradation, and costing animal productivity. This is the universal side effect of methane mitigation in ruminants.

AB03 is an **inhibitor-agnostic intervention** that simultaneously sinks accumulated H₂ and recovers or improves animal productivity during methanogenesis inhibition. It is designed to pair with any methane inhibitor as a combination product.

## Experiment: What Are We Testing?

This is a **meta-experiment on the Overwatch pipeline itself**. We run the same problem through the full 9-agent pipeline twice, with different problem framings:

- **Variant A ("Biochemistry Mode")** — agents receive adapted vocabulary that treats this as a rumen biochemistry optimization problem
- **Variant B ("Disease Mode")** — agents receive the problem framed as a disease (H₂ accumulation syndrome) using the standard Overwatch disease vocabulary

The independent variable is **framing only**. Same agents, same 6-model external panel, same Reaper adversarial pressure, same Anvil 70% test. The comparison reveals how problem framing affects pipeline output quality across multiple dimensions.

### Comparison Dimensions

After both pipelines complete, a meta-analysis scores both variants across:

1. **Problem map completeness** — did Pathfinder miss anything?
2. **Bottleneck consensus quality** — did Tribunal converge on something defensible?
3. **Failure analysis depth** — did Sapper find mechanism-level reasons, not just "didn't work"?
4. **Candidate novelty** — how many non-obvious targets did Forge + Vulcan produce?
5. **Vulcan independence** — did the quarantined variant find things the literature-aware variant missed?
6. **Kill resistance** — what survived Reaper, and was it the same across variants?
7. **Portfolio coverage** — did either hit 70% of the tractable problem space?
8. **Framing artifacts** — where did the framing help or hurt the agents' reasoning?

---

## Variant A: Adapted Framing ("Biochemistry Mode")

### Core Principle

Agents receive their standard prompts unmodified. Overwatch provides a **program context document** (`programs/ab03-a/program-context.md`) that translates the pipeline's disease vocabulary into biochemistry vocabulary. Each agent is launched with this context plus the standard prompt.

### Agent Reframing

| Agent | Standard Concept | AB03-A Reframing |
|-------|-----------------|------------------|
| **Pathfinder** | Disease stages (entry → colonization → immune evasion → acute pathology → chronic persistence → treatment resistance → reinfection) | H₂ metabolism stages: fermentation H₂ production → interspecies H₂ transfer → methanogenic consumption (now inhibited) → alternative sink pathways (propionogenesis, reductive acetogenesis, nitrate/sulfate reduction, biohydrogenation) → thermodynamic constraints → microbial ecology → downstream effects on VFA profile and animal productivity |
| **Pathfinder** | Rate-limiting barrier | The thermodynamic, kinetic, or ecological bottleneck preventing alternative H₂ sinks from scaling when methanogens are suppressed |
| **Pathfinder** | R0 / transmission dynamics | Not applicable as infection metric. Instead: **H₂ flux dynamics** — what is the steady-state dissolved H₂ partial pressure under inhibition? How fast does it accumulate? What concentration threshold triggers VFA profile shift and fiber degradation loss? |
| **Pathfinder** | KE#1 (portfolio-restructuring experiment) | The single experiment that would resolve the most important unknown about H₂ disposal in the inhibited rumen |
| **Tribunal** | Disease bottleneck (4 frames) | System bottleneck: what prevents alternative H₂ sinks from replacing methanogenesis? Frame A (unframed), Frame B (microbial ecology — which organisms could fill the niche?), Frame C (host/environment — what rumen conditions enable or prevent alternative sinks?), Frame D (Martian/quantitative — thermodynamic free energies, H₂ thresholds, kinetic parameters) |
| **Sapper** | Treatment failures | Intervention failures: why has every proposed alternative H₂ sink failed to achieve practical adoption? Fumarate (cost, dose, in vivo translation), nitrate (toxicity, nitrite accumulation), acetogens (thermodynamic disadvantage vs methanogens), sulfate (H₂S toxicity), DFMs (colonization failure), Asparagopsis + fumarate combos (in vitro only). Each failure analyzed at mechanism level: target failure vs implementation failure. |
| **Forge** | Drug targets for disease stages | Interventions for H₂ disposal: novel electron acceptors, engineered microorganisms, enzyme systems, pathway enhancement (propionogenesis cofactors), synthetic biology approaches, combination strategies. Novel molecular targets preferred over feed additives per Agteria strategy. Decompose the primary target into ALL intervention points. |
| **Vulcan** | First-principles vulnerability analysis (quarantined) | First-principles thermodynamic analysis of H₂ disposal. Quarantined: sees ONLY the H₂ metabolism map, NOT the failure analysis, NOT the external panel. Works from thermodynamic free energies, enzyme kinetics, and microbial niche theory. What SHOULD work based purely on chemistry and physics? |
| **Surveyor** | Computational validation + structure prediction | Validate proposed targets: are the enzymes real? Are they conserved across rumen microbial populations? Structure prediction for novel protein targets. Binder design where applicable (e.g., if proposing enzyme engineering). |
| **Reaper** | Kill tests against candidates | All 12 kill tests apply. Adapted where needed: Kill Test 3 (Matrix) = rumen fluid, not broth. Kill Test 1 (20-Year Test) = especially relevant for fumarate, nitrate, acetogens — decades of research with no adoption. Kill Test 7 (Stoichiometric) = H₂ flux vs sink capacity at proposed dose. |
| **Board** | Strategic force-ranking + external review | Same structure. Force-rank by: leverage on H₂ disposal, information value of de-risk experiment, IP position, combination potential with existing inhibitors. |
| **Anvil** | 70% coverage test + deliverables | Coverage test against the H₂ metabolism map stages. "Tractable" = amenable to a molecular/biological intervention. Non-tractable = management-only (e.g., feed rate management). 70% of tractable H₂ disposal problem must be covered. |

### 6-Model External Panel

Phase prompts from `tools/phase-prompts.txt` are used with minor wording adaptations in the system prompt context. The adaptations are documented in `programs/ab03-a/panel-context.md` so Overwatch can prepend them when running `cross-check.py`.

Adaptations are minimal — replace "disease" with "system," "pathogen" with "accumulated H₂," "treatment" with "intervention," etc. The panel models are smart enough to work with either vocabulary given adequate context.

---

## Variant B: Disease Framing ("H₂ Toxicity as Pathology")

### Core Principle

The problem is framed as a disease using the existing Overwatch vocabulary with minimal modification. Agents receive their standard prompts. Overwatch provides a **program context document** (`programs/ab03-b/program-context.md`) that frames H₂ accumulation as a disease.

### The Disease Frame

| Disease Concept | H₂ Accumulation Mapping |
|----------------|------------------------|
| **Disease name** | Rumen Hydrogen Accumulation Syndrome (RHAS) — iatrogenic, caused by methanogenesis inhibition |
| **Pathogen** | Accumulated dissolved H₂ (the "agent" causing pathology) |
| **Entry/exposure** | Administration of any methanogenesis inhibitor |
| **Colonization** | H₂ accumulation in the rumen — dissolved H₂ partial pressure rises above the threshold where alternative sinks can compensate |
| **Immune evasion** | The rumen's native compensatory mechanisms (partial propionogenesis upregulation, microbial community shifts) are insufficient — the "pathogen" overwhelms the "immune system" |
| **Acute pathology** | VFA profile shift (acetate↑, propionate↓), NADH/NAD⁺ ratio change, reduced fiber degradation, decreased feed efficiency |
| **Chronic persistence** | Sustained productivity loss, potential microbial dysbiosis, reduced economic value of methane inhibition |
| **Treatment resistance** | Why alternative sinks fail: thermodynamic disadvantage of acetogenesis, toxicity of nitrate pathway, cost/dose issues with fumarate, colonization failure of DFMs |
| **Reinfection/reseeding** | Continuous — as long as the inhibitor is administered, the "pathogen" (H₂) is continuously generated |
| **R0** | Reframed as: does the H₂ accumulation problem self-amplify? (Yes — high H₂ inhibits fermentation → less substrate turnover → but also less H₂ production. There may be a negative feedback equilibrium.) |

### Agent Behavior

Agents use their standard prompts with no modifications. The disease frame in the program context document provides enough mapping for the agents to operate within their normal vocabulary. This is the key test: **can the standard disease-oriented pipeline handle a non-disease problem when the problem is framed in disease terms?**

### 6-Model External Panel

Standard phase prompts from `tools/phase-prompts.txt` used as-is. The disease framing should be sufficient for the panel models to engage.

---

## Execution Architecture

### Program Directories

```
programs/
├── ab03-a/                          # Variant A (adapted framing)
│   ├── program-context.md           # Biochemistry vocabulary mapping
│   ├── panel-context.md             # Panel prompt adaptations
│   ├── phase-1-disease-map.md       # (named for pipeline consistency)
│   ├── phase-1b-bottleneck-consensus.md
│   ├── phase-2-failure-analysis.md
│   ├── phase-3-candidates.md
│   ├── phase-3-vulcan.md
│   ├── phase-3b-survey-report.md
│   ├── phase-4-kill-report.md
│   ├── phase-4b-board-decision.md
│   ├── phase-5-coverage-map.md
│   ├── phase-5-evidence-register.md
│   ├── phase-5-decision-memo.md
│   ├── prediction-log.md
│   ├── external-input-phase-1.md
│   ├── external-input-phase-2.md
│   ├── external-input-phase-3.md
│   ├── external-input-phase-4.md
│   └── external-input-phase-5.md
├── ab03-b/                          # Variant B (disease framing)
│   ├── program-context.md           # Disease vocabulary mapping
│   ├── phase-1-disease-map.md
│   ├── ... (same file structure)
│   └── external-input-phase-5.md
└── ab03-comparison.md               # Meta-analysis comparing A vs B
```

### Execution Order

Both variants run the full pipeline. Within each variant, the order follows standard Overwatch workflow:

```
Phase 1:   Pathfinder → 6-model panel → (gap check, resend if needed)
Phase 1b:  Tribunal (4-frame consensus)
Phase 2:   Sapper → 6-model panel
Phase 3:   Forge ∥ Vulcan (parallel) → 6-model panel on Forge output
Phase 3b:  Surveyor (merges Forge + Vulcan)
Phase 4:   Reaper → 6-model panel
Phase 4b:  Board (external review + force-ranking)
Phase 5:   Anvil (70% test + deliverables) → 6-model panel
```

Forge and Vulcan run in parallel within each variant. The two variants (A and B) also run in parallel where possible — they are completely independent.

### Parallelism Strategy

**Maximum parallelism:** Run Variant A and Variant B simultaneously from the start. Each variant's internal pipeline is sequential (except Forge ∥ Vulcan). This means at any given time, up to 4 agents could be running (Forge-A ∥ Vulcan-A ∥ Forge-B ∥ Vulcan-B).

**Practical constraint:** External panel calls via `cross-check.py` hit OpenRouter. Running both variants' panels simultaneously doubles the API calls per phase. This is fine given the low cost (~$0.10-0.30 per phase × 2 variants = under $4 total for both full runs).

### Overwatch Quality Checks

All standard Overwatch quality checks apply to both variants. Overwatch reads every phase output before passing to the next agent and applies the checks defined in CLAUDE.md:

- Pathfinder: complete map? R0/flux estimate? KE#1?
- Tribunal: all 4 frames independent? 3+/4 convergence?
- Sapper: mechanism-level failure reasons for every intervention?
- Forge: every stage covered? novel targets preferred? prediction log updated?
- Vulcan: quarantine verified? found things Forge missed?
- Surveyor: every candidate assessed? structure predictions for top targets?
- Reaper: evidence-based kills? Surveyor data used? extra scrutiny on feed additives?
- Board: external feedback synthesized? devil's advocate inversion? genuine force-ranking?
- Anvil: 70% test honest? KE#1 flagged? prediction log complete?

### The 70% Enforcement Loop

Both variants get the standard 70% enforcement:
1. Anvil reports coverage map
2. Overwatch verifies: is every stage covered? Are estimates honest?
3. If it fails: Forge gets sent back for uncovered stages → Surveyor → Reaper → Anvil again
4. Maximum 3 loops per variant. If still failing, escalate to Daniel.

For Variant A, "tractable stages" are H₂ metabolism stages amenable to molecular/biological intervention.
For Variant B, "tractable stages" are disease stages amenable to pharmaceutical intervention.

---

## Meta-Analysis: Comparing A vs B

After both pipelines complete, Overwatch (the orchestrator — not a subagent) produces `programs/ab03-comparison.md` containing:

### 1. Problem Map Comparison
- Side-by-side: what did each Pathfinder identify?
- Did one framing produce a more complete or more nuanced map?
- Did the disease frame force Pathfinder to find "stages" that don't naturally exist?
- Did the biochemistry frame miss anything the disease frame caught (or vice versa)?

### 2. Bottleneck Consensus Comparison
- Did the two Tribunals converge on the same bottleneck?
- Did the 4 frames produce more diverse perspectives under one framing?
- Which Tribunal's determination is more defensible?

### 3. Failure Analysis Comparison
- Did Sapper go deeper under one framing?
- Did the "treatment failure" frame produce more forensic analysis than "intervention failure"?
- Were the same failure mechanisms identified?

### 4. Candidate Novelty Comparison
- Total unique candidates per variant
- Novel candidates (not in published literature) per variant
- Vulcan-only candidates (not in Forge) per variant — this tests whether quarantine works differently under different framings

### 5. Kill Resistance Comparison
- What survived Reaper in each variant?
- Same targets, or different?
- Were kills more evidence-based under one framing?
- Did one framing's Reaper have an easier or harder time?

### 6. Portfolio Coverage Comparison
- Did either hit 70%?
- Which stages were hardest to cover?
- Was coverage quality (evidence depth per stage) different?

### 7. Framing Artifact Analysis
The most important section. Where did framing help or hurt?
- **Forced structure:** Did the disease frame force agents to find stages/mechanisms they wouldn't have otherwise?
- **Vocabulary mismatch:** Did agents struggle with adapted vocabulary?
- **Agent anchoring:** Did disease-trained agents perform better with disease vocabulary?
- **Creative freedom:** Did the biochemistry frame give Forge/Vulcan more room to propose non-standard interventions?
- **Panel quality:** Did the 6-model panel produce better contributions under one framing?

### 8. Recommendation
Based on the comparison: for future non-disease problems, should Overwatch use adapted framing, disease framing, or both? Under what conditions?

---

## Prior Art / Literature Context

From initial literature search (pre-pipeline):

**The core problem:** Methanogenesis consumes ~70-80% of rumen metabolic H₂. When inhibited (e.g., by 3-NOP), H₂ accumulates because alternative sinks cannot scale to replace methanogenic capacity. The thermodynamic hierarchy: methanogenesis (ΔG°' = −131 kJ/mol) >> propionogenesis >> reductive acetogenesis (ΔG°' = −105 kJ/mol but higher H₂ threshold required).

**Key references identified:**
- Ungerfeld 2020 (Frontiers in Microbiology, 294 citations) — landmark review of metabolic H₂ flows and intervention possibilities
- Wang et al. 2022 (Applied and Environmental Microbiology) — 3-NOP + fumarate synergy: reduced CH₄ by 11.48%, increased propionate, alleviated H₂ accumulation in vitro
- Wang et al. 2022 (Journal of Dairy Science) — 3-NOP + vitamin B₁₂: reduced CH₄ by 12%, enhanced propionate via B₁₂-dependent propionogenesis pathway
- Zhang et al. 2021 (Journal of Animal Science) — 3-NOP + canola oil: 51% CH₄ reduction, oil partially absorbed H₂ via biohydrogenation
- Microbiome 2025 — reductive acetogenesis is dominant in the ruminant hindgut (cecum), 12× more acetogens than rumen. Suggests the ecology, not thermodynamics, is the primary barrier in the rumen.

**Known alternative H₂ sinks (all with limitations):**
1. Propionogenesis (fumarate/malate → succinate → propionate) — consumes H₂, produces valuable VFA, but requires high dose and cost
2. Reductive acetogenesis (CO₂ + H₂ → acetate) — thermodynamically unfavorable vs methanogenesis at rumen H₂ concentrations
3. Nitrate reduction (NO₃⁻ → NH₃) — effective H₂ sink but nitrite intermediate is toxic
4. Sulfate reduction (SO₄²⁻ → H₂S) — H₂S is toxic
5. Biohydrogenation of unsaturated fatty acids — limited by dietary fat content
6. Direct-fed microbials (acetogens) — colonization failure in the rumen

This context is provided for reference. The pipeline agents will conduct their own independent analysis.

---

## Success Criteria

The experiment succeeds if it produces:

1. **For AB03:** At least one novel, high-confidence intervention target for H₂ disposal during methanogenesis inhibition that survives Reaper and could enter Agteria's development pipeline
2. **For the Overwatch product:** Clear evidence about whether adapted framing or disease framing produces better results for non-disease problems, with specific recommendations for future programs
3. **For the comparison:** A defensible meta-analysis that identifies framing artifacts and informs pipeline methodology

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Disease framing forces agents into artificial stages | Variant B produces lower-quality analysis | This IS the experiment — if it happens, it's a finding |
| Adapted framing confuses agents trained on disease vocabulary | Variant A produces incoherent output | Program context document provides explicit vocabulary mapping |
| Both variants converge on the same obvious answers (fumarate, nitrate) | No novel insights | Vulcan quarantine + Forge Principle 5 ("if nothing exists, propose something new") push for novelty |
| 6-model panel struggles with non-disease framing | Lower quality external input for Variant A | Panel context document provides explicit framing; panel models are capable of domain adaptation |
| Pipeline is overkill for a biochemistry problem | Wasted compute/time | Low cost (~$4 total), and the meta-experiment on framing justifies the run regardless of AB03 outcome |
