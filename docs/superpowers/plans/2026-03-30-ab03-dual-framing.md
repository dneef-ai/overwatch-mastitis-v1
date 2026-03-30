# AB03 Dual-Framing Pipeline Experiment — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run the H₂ sink problem (AB03) through the full 9-agent Overwatch pipeline twice — once with adapted biochemistry framing (Variant A) and once with disease framing (Variant B) — then produce a meta-analysis comparing both.

**Architecture:** Two independent program directories (`programs/ab03-a/`, `programs/ab03-b/`), each running the full Pathfinder → Tribunal → Sapper → Forge ∥ Vulcan → Surveyor → Reaper → Board → Anvil pipeline with 6-model external panel at every phase. Variants A and B can run in parallel. After both complete, Overwatch writes the comparison document.

**Tech Stack:** Claude Code subagents (agent prompts in `agents/`), `tools/cross-check.py` (OpenRouter API for 6-model panel), phase prompts in `tools/phase-prompts.txt`

**Spec:** `docs/superpowers/specs/2026-03-30-ab03-dual-framing-design.md`

---

## Task 0: Create Program Directories and Context Documents

**Files:**
- Create: `programs/ab03-a/program-context.md`
- Create: `programs/ab03-a/panel-context.md`
- Create: `programs/ab03-b/program-context.md`

### Variant A — Program Context

- [ ] **Step 1: Create `programs/ab03-a/` directory**

```bash
mkdir -p programs/ab03-a
```

- [ ] **Step 2: Write `programs/ab03-a/program-context.md`**

This document is prepended to every agent prompt when launching Variant A agents. It maps disease vocabulary to biochemistry vocabulary.

```markdown
# AB03 Program Context — Variant A (Biochemistry Mode)

**Program:** AB03 — Rumen H₂ Sink During Methanogenesis Inhibition
**Internal Agteria Program** (no partner)
**Date:** 2026-03-30

---

## The Problem

When methanogenesis is inhibited in cattle (by any inhibitor — 3-NOP, Asparagopsis, halogenated compounds, etc.), the primary ruminal H₂ sink is removed. H₂ accumulates, shifting the NADH/NAD⁺ ratio, altering VFA profiles toward acetate, reducing fiber degradation, and costing animal productivity.

AB03 is an inhibitor-agnostic intervention that simultaneously sinks accumulated H₂ and recovers or improves animal productivity during methanogenesis inhibition.

## Vocabulary Mapping

This is NOT a disease program. It is a rumen biochemistry optimization problem. The pipeline's disease vocabulary maps as follows:

| Pipeline Term | AB03 Meaning |
|--------------|-------------|
| Disease | Rumen H₂ accumulation during methanogenesis inhibition |
| Pathogen | Accumulated dissolved H₂ (not a living agent) |
| Disease stages | H₂ metabolism stages (see below) |
| Virulence factors | H₂-mediated disruption mechanisms (NADH/NAD⁺ shift, VFA profile change, fiber degradation loss) |
| Host immune response | Rumen's native compensatory mechanisms (partial propionogenesis upregulation, microbial community shifts) |
| Rate-limiting barrier | The bottleneck preventing alternative H₂ sinks from scaling |
| R0 / transmission | H₂ flux dynamics: steady-state dissolved H₂ partial pressure, accumulation rate, concentration thresholds |
| KE#1 | The single experiment that resolves the most important unknown about H₂ disposal |
| Treatment failures | Failed alternative H₂ sink interventions (fumarate, nitrate, acetogens, etc.) |
| Drug targets | Molecular/biological interventions for H₂ disposal |
| 70% coverage | 70% of tractable H₂ metabolism stages covered by surviving candidates |

## The Stages to Map (Pathfinder)

Instead of disease progression stages, map the H₂ metabolism system:

1. **H₂ Production** — fermentative H₂ generation during carbohydrate metabolism. Which organisms, which pathways, what flux rates?
2. **Interspecies H₂ Transfer** — how H₂ moves from producers to consumers. Dissolved H₂ concentrations, gradients, physical proximity requirements.
3. **Primary Sink (Now Inhibited)** — methanogenesis. 4H₂ + CO₂ → CH₄ + 2H₂O. Normally consumes 70-80% of metabolic H₂. ΔG°' = −131 kJ/mol. This is what's been removed.
4. **Alternative Sink: Propionogenesis** — fumarate reductase pathway. Consumes H₂, produces propionate (valuable VFA). Thermodynamics, enzyme kinetics, current capacity, scaling barriers.
5. **Alternative Sink: Reductive Acetogenesis** — Wood-Ljungdahl pathway. 4H₂ + 2CO₂ → CH₃COOH + 2H₂O. ΔG°' = −105 kJ/mol. Higher H₂ threshold required. Why acetogens lose to methanogens in the rumen but dominate in the hindgut.
6. **Alternative Sink: Nitrate/Sulfate Reduction** — inorganic electron acceptors. Effective H₂ sinks but toxic intermediates (nitrite, H₂S).
7. **Alternative Sink: Biohydrogenation** — saturation of unsaturated fatty acids. Limited by dietary fat content.
8. **Downstream Effects** — what happens when H₂ accumulates: NADH/NAD⁺ ratio shift, VFA profile change (acetate↑, propionate↓), reduced fiber degradation, productivity loss.
9. **Microbial Ecology** — community structure under inhibition. Which populations expand/contract? Is there a new equilibrium?

## Strategic Preference

Agteria is a drug discovery company. Novel molecular targets (enzymes, engineered microbes, novel electron acceptors) are preferred over feed additives. Apply the "why isn't the field doing this?" test to any feed-ingredient proposal.
```

- [ ] **Step 3: Write `programs/ab03-a/panel-context.md`**

This document provides adapted context for the 6-model external panel prompts when running Variant A.

```markdown
# AB03-A Panel Context

Prepend this to phase prompts when running cross-check.py for Variant A.

---

**Context for reviewers:** This is NOT a disease program. It is a rumen biochemistry optimization problem. The system being analyzed is rumen hydrogen (H₂) metabolism during methanogenesis inhibition in cattle. When methanogens are suppressed (by any inhibitor), H₂ accumulates because the primary sink is removed. The goal is to find interventions that redirect H₂ into productive pathways.

When the document references "disease stages," read these as "H₂ metabolism stages." When it references "treatments," read these as "interventions for H₂ disposal." When it references "the pathogen," this means accumulated dissolved H₂, not a living organism.

Apply your expertise to this biochemistry/microbial ecology problem as you would to a disease problem — with the same rigor around evidence, mechanisms, and failure analysis.
```

### Variant B — Program Context

- [ ] **Step 4: Create `programs/ab03-b/` directory**

```bash
mkdir -p programs/ab03-b
```

- [ ] **Step 5: Write `programs/ab03-b/program-context.md`**

```markdown
# AB03 Program Context — Variant B (Disease Mode)

**Program:** AB03 — Rumen Hydrogen Accumulation Syndrome (RHAS)
**Internal Agteria Program** (no partner)
**Date:** 2026-03-30

---

## The Disease

Rumen Hydrogen Accumulation Syndrome (RHAS) is an iatrogenic condition caused by the administration of methanogenesis inhibitors in cattle. When the primary ruminal H₂ sink (methanogenesis) is pharmacologically suppressed, dissolved H₂ accumulates, triggering a cascade of pathological effects on rumen fermentation and animal productivity.

RHAS is the universal side effect of methane mitigation in ruminants. AB03 is an inhibitor-agnostic treatment for RHAS — designed to pair with any methane inhibitor.

## Disease Progression

### Stage 1: Entry/Exposure
Administration of any methanogenesis inhibitor (3-NOP/Bovaer, Asparagopsis taxiformis, halogenated compounds, bromochloromethane, chloroform analogs). The inhibitor targets methyl-coenzyme M reductase (MCR) or other methanogenic enzymes, suppressing the dominant H₂ disposal pathway.

### Stage 2: Colonization (H₂ Accumulation)
With methanogens suppressed, dissolved H₂ partial pressure rises. The rumen normally maintains H₂ at ~1-10 Pa (nanomolar). Under inhibition, H₂ can rise 5-40x. The "colonization threshold" is the H₂ concentration at which alternative sinks can no longer compensate for the lost methanogenic capacity.

### Stage 3: Immune Evasion (Compensatory Failure)
The rumen's native compensatory mechanisms attempt to adapt:
- Partial upregulation of propionogenesis (fumarate reductase pathway)
- Microbial community shifts (increased Selenomonas, Succiniclasticum)
- Minor expansion of reductive acetogens
These "immune responses" are insufficient — they capture only a fraction of the H₂ that methanogenesis was disposing of. The "pathogen" (H₂) overwhelms the "immune system" (alternative sinks).

### Stage 4: Acute Pathology
- NADH/NAD⁺ ratio shift in fermentative bacteria (thermodynamic inhibition of H₂-producing reactions)
- VFA profile change: acetate↑, propionate↓ (reduced gluconeogenic substrate for the host)
- Reduced fiber degradation efficiency (cellulolytic bacteria are H₂ producers — thermodynamic product inhibition)
- Decreased feed efficiency and dry matter intake

### Stage 5: Chronic Persistence
- Sustained productivity loss for the duration of inhibitor administration
- Potential microbial dysbiosis (long-term community restructuring under chronic H₂ stress)
- Economic erosion of the value proposition of methane inhibition (the productivity cost partially offsets the environmental/carbon credit benefit)

### Stage 6: Treatment Resistance
Why every proposed "treatment" for RHAS has failed to achieve practical adoption:
- Fumarate supplementation: effective H₂ sink but requires high doses (~100 mg/g DM), cost-prohibitive at scale
- Nitrate supplementation: effective H₂ sink (NO₃⁻ → NH₃) but toxic intermediate (nitrite → methemoglobinemia)
- Acetogen inoculation (DFMs): thermodynamically outcompeted by even residual methanogens; colonization failure
- Sulfate reduction: H₂S is toxic to rumen epithelium
- Biohydrogenation (dietary oils): limited by fat tolerance (~5-6% DM), can reduce fiber digestibility

### Stage 7: Reinfection/Reseeding
Continuous. As long as the methanogenesis inhibitor is administered, H₂ is continuously generated by fermentation with no adequate sink. The "pathogen" cannot be eliminated — it must be redirected.

## R0 Estimate
Does RHAS self-amplify? Partially:
- High H₂ → thermodynamic inhibition of fermentation → reduced substrate turnover → reduced H₂ production (negative feedback)
- But also: high H₂ → shift from propionate to acetate → more H₂ per mole of VFA produced (positive feedback)
- Net effect: a new equilibrium at reduced productivity, not a runaway amplification
- R0 framing: the "reproduction number" of H₂ disruption is ~1.0 — self-sustaining but not exponentially amplifying. Small interventions that tip the balance could collapse the syndrome.

## Strategic Preference

Agteria is a drug discovery company. Novel molecular targets (enzymes, engineered microbes, novel electron acceptors) are preferred over feed additives. Apply the "why isn't the field doing this?" test to any feed-ingredient proposal.
```

- [ ] **Step 6: Commit setup files**

```bash
git add programs/ab03-a/program-context.md programs/ab03-a/panel-context.md programs/ab03-b/program-context.md
git commit -m "setup: AB03 program directories and context documents for dual-framing experiment"
```

---

## Task 1A: Run Pathfinder — Variant A

**Files:**
- Read: `agents/pathfinder.md` (agent prompt)
- Read: `programs/ab03-a/program-context.md` (context)
- Create: `programs/ab03-a/phase-1-disease-map.md` (output)
- Create: `programs/ab03-a/prediction-log.md` (predictions)

- [ ] **Step 1: Launch Pathfinder-A as a subagent**

Launch a Claude Code Agent with this prompt:

```
You are Pathfinder, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/pathfinder.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context and vocabulary mapping

IMPORTANT: This is NOT a disease. Follow the vocabulary mapping in program-context.md. Map the H₂ metabolism system, not a disease progression. Your "disease stages" are H₂ metabolism stages. Your "rate-limiting barrier" is the bottleneck preventing alternative sinks from scaling. Your "R0" is H₂ flux dynamics.

Write your output to programs/ab03-a/phase-1-disease-map.md
Write 3-5 initial predictions to programs/ab03-a/prediction-log.md

Use web search and literature databases to ground your analysis in real data. Include thermodynamic values (ΔG°'), enzyme kinetics, dissolved H₂ concentrations, and microbial population data where available.
```

- [ ] **Step 2: Overwatch quality check on Pathfinder-A output**

Read `programs/ab03-a/phase-1-disease-map.md` and verify:
- All 9 H₂ metabolism stages from program-context.md are covered
- Each stage has evidence tiers tagged
- H₂ flux dynamics section present (replaces R0)
- Rate-limiting barrier identified with reasoning
- KE#1 (portfolio-restructuring experiment) defined with cost/timeline
- Prediction log has 3-5 falsifiable predictions
- No disease vocabulary leaking in (should be biochemistry throughout)

If gaps: send Pathfinder-A back with specific instructions to fill them.

- [ ] **Step 3: Run 6-model panel on Pathfinder-A output**

Extract the `===PHASE_1_PATHFINDER===` prompt block from `tools/phase-prompts.txt`. Write it to a temp file, prepending the panel context from `programs/ab03-a/panel-context.md`.

```bash
# Prepend panel context to phase prompt, save as temp file
cat programs/ab03-a/panel-context.md > /tmp/ab03a-phase1-prompt.txt
echo -e "\n---\n" >> /tmp/ab03a-phase1-prompt.txt
# Extract PHASE_1_PATHFINDER block from phase-prompts.txt and append
sed -n '/===PHASE_1_PATHFINDER===/,/===PHASE_2/{ /===PHASE_2/d; /===PHASE_1/d; p; }' tools/phase-prompts.txt >> /tmp/ab03a-phase1-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-a/phase-1-disease-map.md \
  --tier full \
  --system-prompt-file /tmp/ab03a-phase1-prompt.txt \
  --output programs/ab03-a/external-input-phase-1.md
```

- [ ] **Step 4: Review panel output and decide if Pathfinder-A needs resend**

Read `programs/ab03-a/external-input-phase-1.md`. If any model identifies missing H₂ metabolism mechanisms or stages, send Pathfinder-A back with the specific gaps before proceeding.

- [ ] **Step 5: Commit Phase 1A**

```bash
git add programs/ab03-a/phase-1-disease-map.md programs/ab03-a/prediction-log.md programs/ab03-a/external-input-phase-1.md
git commit -m "AB03-A phase 1: Pathfinder H₂ metabolism map + 6-model panel"
```

---

## Task 1B: Run Pathfinder — Variant B

**Files:**
- Read: `agents/pathfinder.md` (agent prompt)
- Read: `programs/ab03-b/program-context.md` (context)
- Create: `programs/ab03-b/phase-1-disease-map.md` (output)
- Create: `programs/ab03-b/prediction-log.md` (predictions)

> **Note:** Task 1A and 1B can run in PARALLEL — they are independent.

- [ ] **Step 1: Launch Pathfinder-B as a subagent**

```
You are Pathfinder, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read these files in order:
1. agents/pathfinder.md — your base instructions
2. programs/ab03-b/program-context.md — the disease context

This IS framed as a disease: Rumen Hydrogen Accumulation Syndrome (RHAS). Use the disease stages defined in program-context.md. Map the full disease progression from inhibitor administration through chronic productivity loss. Apply your standard disease mapping methodology.

Write your output to programs/ab03-b/phase-1-disease-map.md
Write 3-5 initial predictions to programs/ab03-b/prediction-log.md

Use web search and literature databases to ground your analysis in real data.
```

- [ ] **Step 2: Overwatch quality check on Pathfinder-B output**

Read `programs/ab03-b/phase-1-disease-map.md` and verify:
- All 7 standard disease stages covered (entry → colonization → immune evasion → acute pathology → chronic persistence → treatment resistance → reinfection)
- Each stage has evidence tiers tagged
- R0 estimate present (even if reframed for non-infectious context)
- Rate-limiting barrier identified
- KE#1 defined with cost/timeline
- Prediction log has 3-5 falsifiable predictions
- Disease vocabulary used consistently (no breaking character)

If gaps: send Pathfinder-B back.

- [ ] **Step 3: Run 6-model panel on Pathfinder-B output**

Standard phase prompts — no panel context adaptation needed for Variant B.

```bash
sed -n '/===PHASE_1_PATHFINDER===/,/===PHASE_2/{ /===PHASE_2/d; /===PHASE_1/d; p; }' tools/phase-prompts.txt > /tmp/ab03b-phase1-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-b/phase-1-disease-map.md \
  --tier full \
  --system-prompt-file /tmp/ab03b-phase1-prompt.txt \
  --output programs/ab03-b/external-input-phase-1.md
```

- [ ] **Step 4: Review panel output and decide if Pathfinder-B needs resend**

- [ ] **Step 5: Commit Phase 1B**

```bash
git add programs/ab03-b/phase-1-disease-map.md programs/ab03-b/prediction-log.md programs/ab03-b/external-input-phase-1.md
git commit -m "AB03-B phase 1: Pathfinder RHAS disease map + 6-model panel"
```

---

## Task 2A: Run Tribunal — Variant A

**Files:**
- Read: `agents/tribunal.md`, `programs/ab03-a/program-context.md`
- Read: `programs/ab03-a/phase-1-disease-map.md`, `programs/ab03-a/external-input-phase-1.md`
- Create: `programs/ab03-a/phase-1b-bottleneck-consensus.md`

> **Depends on:** Task 1A complete

- [ ] **Step 1: Launch Tribunal-A as a subagent**

```
You are the Tribunal, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/tribunal.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context and vocabulary mapping
3. programs/ab03-a/phase-1-disease-map.md — the H₂ metabolism map
4. programs/ab03-a/external-input-phase-1.md — 6-model panel contributions

IMPORTANT: This is NOT a disease. Your "disease bottleneck" is the SYSTEM BOTTLENECK — what prevents alternative H₂ sinks from replacing methanogenesis? Your four frames should be:
- Frame A (Unframed Analyst): where is the highest-leverage intervention point in the H₂ metabolism system?
- Frame B (Microbial Ecologist): which organisms could fill the methanogen niche? What prevents them?
- Frame C (Host/Environment): what rumen conditions enable or prevent alternative sinks from scaling?
- Frame D (Martian/Quantitative): thermodynamic free energies, H₂ thresholds, kinetic rate constants — what do the numbers say?

Write output to programs/ab03-a/phase-1b-bottleneck-consensus.md
```

- [ ] **Step 2: Overwatch quality check**

Verify: all 4 frames produced independent analyses, evaluator mapped convergence AND disagreement, bottleneck determination supported by 3+/4 agents, Martian contributed something domain agents missed.

- [ ] **Step 3: Commit**

```bash
git add programs/ab03-a/phase-1b-bottleneck-consensus.md
git commit -m "AB03-A phase 1b: Tribunal bottleneck consensus on H₂ metabolism"
```

---

## Task 2B: Run Tribunal — Variant B

**Files:**
- Read: `agents/tribunal.md`, `programs/ab03-b/program-context.md`
- Read: `programs/ab03-b/phase-1-disease-map.md`, `programs/ab03-b/external-input-phase-1.md`
- Create: `programs/ab03-b/phase-1b-bottleneck-consensus.md`

> **Depends on:** Task 1B complete. Can run in PARALLEL with Task 2A.

- [ ] **Step 1: Launch Tribunal-B as a subagent**

```
You are the Tribunal, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read these files in order:
1. agents/tribunal.md — your base instructions
2. programs/ab03-b/program-context.md — the disease context
3. programs/ab03-b/phase-1-disease-map.md — the RHAS disease map
4. programs/ab03-b/external-input-phase-1.md — 6-model panel contributions

This is framed as a disease (RHAS). Use your standard 4-frame methodology:
- Frame A: Unframed Analyst
- Frame B: Pathogen Specialist (the "pathogen" is accumulated H₂)
- Frame C: Host/Environment Analyst
- Frame D: Martian (quantitative first principles)

Write output to programs/ab03-b/phase-1b-bottleneck-consensus.md
```

- [ ] **Step 2: Overwatch quality check**

Same criteria as Task 2A.

- [ ] **Step 3: Commit**

```bash
git add programs/ab03-b/phase-1b-bottleneck-consensus.md
git commit -m "AB03-B phase 1b: Tribunal bottleneck consensus on RHAS"
```

---

## Task 3A: Run Sapper — Variant A

**Files:**
- Read: `agents/sapper.md`, `programs/ab03-a/program-context.md`
- Read: `programs/ab03-a/phase-1-disease-map.md`, `programs/ab03-a/phase-1b-bottleneck-consensus.md`
- Create: `programs/ab03-a/phase-2-failure-analysis.md`
- Create: `programs/ab03-a/external-input-phase-2.md`

> **Depends on:** Task 2A complete

- [ ] **Step 1: Launch Sapper-A as a subagent**

```
You are Sapper, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/sapper.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context
3. programs/ab03-a/phase-1-disease-map.md — the H₂ metabolism map
4. programs/ab03-a/phase-1b-bottleneck-consensus.md — the bottleneck consensus

IMPORTANT: Your "treatments" are alternative H₂ sink interventions that have been tried and failed to achieve practical adoption. Analyze AT LEAST these:
1. Fumarate/malate supplementation
2. Nitrate supplementation
3. Sulfate supplementation
4. Acetogen inoculation (direct-fed microbials)
5. Dietary oils (biohydrogenation)
6. 3-NOP + fumarate combinations
7. 3-NOP + vitamin B₁₂ combinations
8. Asparagopsis + fumarate combinations

For each: what was tried, specific results (doses, VFA changes, H₂ reduction %), WHY it failed at the mechanism level (target failure vs implementation failure), and what constraint it imposes on future approaches.

Write output to programs/ab03-a/phase-2-failure-analysis.md
```

- [ ] **Step 2: Overwatch quality check**

Verify: every intervention has a specific failure mechanism (not just "didn't work"), gap map produced, target-vs-implementation distinction made for each.

- [ ] **Step 3: Run 6-model panel**

```bash
cat programs/ab03-a/panel-context.md > /tmp/ab03a-phase2-prompt.txt
echo -e "\n---\n" >> /tmp/ab03a-phase2-prompt.txt
sed -n '/===PHASE_2_SAPPER===/,/===PHASE_3/{ /===PHASE_3/d; /===PHASE_2/d; p; }' tools/phase-prompts.txt >> /tmp/ab03a-phase2-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-a/phase-2-failure-analysis.md \
  --tier full \
  --system-prompt-file /tmp/ab03a-phase2-prompt.txt \
  --output programs/ab03-a/external-input-phase-2.md
```

- [ ] **Step 4: Commit**

```bash
git add programs/ab03-a/phase-2-failure-analysis.md programs/ab03-a/external-input-phase-2.md
git commit -m "AB03-A phase 2: Sapper failure analysis + 6-model panel"
```

---

## Task 3B: Run Sapper — Variant B

> **Depends on:** Task 2B complete. Can run in PARALLEL with Task 3A.

- [ ] **Step 1: Launch Sapper-B as a subagent**

```
You are Sapper, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read these files in order:
1. agents/sapper.md — your base instructions
2. programs/ab03-b/program-context.md — the disease context
3. programs/ab03-b/phase-1-disease-map.md — the RHAS disease map
4. programs/ab03-b/phase-1b-bottleneck-consensus.md — the bottleneck consensus

This is framed as a disease. Analyze failed "treatments" for RHAS using your standard methodology. Find at least 8 current or historical treatment approaches and explain WHY each failed at the biological/pharmacological mechanism level.

Write output to programs/ab03-b/phase-2-failure-analysis.md
```

- [ ] **Step 2: Overwatch quality check**

Same criteria as Task 3A.

- [ ] **Step 3: Run 6-model panel (standard prompts, no panel-context adaptation)**

```bash
sed -n '/===PHASE_2_SAPPER===/,/===PHASE_3/{ /===PHASE_3/d; /===PHASE_2/d; p; }' tools/phase-prompts.txt > /tmp/ab03b-phase2-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-b/phase-2-failure-analysis.md \
  --tier full \
  --system-prompt-file /tmp/ab03b-phase2-prompt.txt \
  --output programs/ab03-b/external-input-phase-2.md
```

- [ ] **Step 4: Commit**

```bash
git add programs/ab03-b/phase-2-failure-analysis.md programs/ab03-b/external-input-phase-2.md
git commit -m "AB03-B phase 2: Sapper RHAS treatment failure analysis + 6-model panel"
```

---

## Task 4A: Run Forge + Vulcan — Variant A (Parallel)

**Files:**
- Create: `programs/ab03-a/phase-3-candidates.md` (Forge)
- Create: `programs/ab03-a/phase-3-vulcan.md` (Vulcan)
- Create: `programs/ab03-a/external-input-phase-3.md` (panel on Forge)

> **Depends on:** Task 3A complete

- [ ] **Step 1: Launch Forge-A and Vulcan-A as PARALLEL subagents**

**Forge-A prompt:**
```
You are Forge, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/forge.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context
3. programs/ab03-a/phase-1-disease-map.md — the H₂ metabolism map
4. programs/ab03-a/phase-1b-bottleneck-consensus.md — the bottleneck consensus
5. programs/ab03-a/phase-2-failure-analysis.md — why interventions failed
6. programs/ab03-a/external-input-phase-2.md — 6-model panel on failures

IMPORTANT: Your "disease stages" are H₂ metabolism stages. Propose candidates for EVERY stage. Novel molecular targets (enzymes, engineered microbes, novel electron acceptors, pathway engineering) are preferred over feed additives.

For the primary intervention target, decompose ALL molecular intervention points — not just "add fumarate" but every step in the pathway that could be enhanced or engineered.

Search for what has ACTUALLY WORKED in vivo in cattle, not just what should work based on mechanism.

Write candidates to programs/ab03-a/phase-3-candidates.md
Append 5 falsifiable predictions to programs/ab03-a/prediction-log.md
```

**Vulcan-A prompt:**
```
You are Vulcan, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files ONLY:
1. agents/vulcan.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context (vocabulary mapping only)
3. programs/ab03-a/phase-1-disease-map.md — the H₂ metabolism map

QUARANTINE: Do NOT read the failure analysis, the external panel input, or any other files. You work from the H₂ metabolism map ONLY.

Your job: first-principles thermodynamic and kinetic analysis of H₂ disposal in the rumen. Given the chemistry (free energies, enzyme kinetics, H₂ thresholds, microbial niche theory), what SHOULD work? Decompose every promising intervention point into ALL molecular steps.

Think about:
- Thermodynamic coupling (can you make an unfavorable reaction favorable by coupling it?)
- Enzyme engineering (can you lower the H₂ threshold for acetogenesis?)
- Niche creation (can you create conditions where acetogens outcompete residual methanogens?)
- Novel electron acceptors (what chemistry is available beyond the known sinks?)
- Synthetic biology (can you engineer a rumen microbe with enhanced H₂ disposal?)

Write output to programs/ab03-a/phase-3-vulcan.md
```

- [ ] **Step 2: Overwatch quality check on Forge-A**

Verify: every H₂ metabolism stage has at least one candidate, novel targets preferred over feed additives, primary target fully decomposed into molecular intervention points, prediction log updated with 5 predictions.

- [ ] **Step 3: Overwatch quality check on Vulcan-A**

Verify: quarantine maintained (no references to failure analysis or panel), found intervention points from first principles, decomposed into molecular steps.

- [ ] **Step 4: Run 6-model panel on Forge-A output**

```bash
cat programs/ab03-a/panel-context.md > /tmp/ab03a-phase3-prompt.txt
echo -e "\n---\n" >> /tmp/ab03a-phase3-prompt.txt
sed -n '/===PHASE_3_FORGE===/,/===PHASE_4/{ /===PHASE_4/d; /===PHASE_3/d; p; }' tools/phase-prompts.txt >> /tmp/ab03a-phase3-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-a/phase-3-candidates.md \
  --tier full \
  --system-prompt-file /tmp/ab03a-phase3-prompt.txt \
  --output programs/ab03-a/external-input-phase-3.md
```

- [ ] **Step 5: Commit**

```bash
git add programs/ab03-a/phase-3-candidates.md programs/ab03-a/phase-3-vulcan.md programs/ab03-a/prediction-log.md programs/ab03-a/external-input-phase-3.md
git commit -m "AB03-A phase 3: Forge candidates + Vulcan first-principles + 6-model panel"
```

---

## Task 4B: Run Forge + Vulcan — Variant B (Parallel)

> **Depends on:** Task 3B complete. Can run in PARALLEL with Task 4A.

- [ ] **Step 1: Launch Forge-B and Vulcan-B as PARALLEL subagents**

**Forge-B prompt:**
```
You are Forge, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read these files in order:
1. agents/forge.md — your base instructions
2. programs/ab03-b/program-context.md — the disease context
3. programs/ab03-b/phase-1-disease-map.md — the RHAS disease map
4. programs/ab03-b/phase-1b-bottleneck-consensus.md — the bottleneck consensus
5. programs/ab03-b/phase-2-failure-analysis.md — why treatments failed
6. programs/ab03-b/external-input-phase-2.md — 6-model panel on failures

This is framed as a disease. Propose drug targets for EVERY disease stage of RHAS. Novel molecular targets preferred. Decompose the primary target into ALL molecular intervention points.

Write candidates to programs/ab03-b/phase-3-candidates.md
Append 5 falsifiable predictions to programs/ab03-b/prediction-log.md
```

**Vulcan-B prompt:**
```
You are Vulcan, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read these files ONLY:
1. agents/vulcan.md — your base instructions
2. programs/ab03-b/program-context.md — the disease context (for framing only)
3. programs/ab03-b/phase-1-disease-map.md — the RHAS disease map

QUARANTINE: Do NOT read the failure analysis, the external panel input, or any other files.

This is framed as a disease. Find intervention points using first-principles analysis of the disease biology. Decompose every virulence mechanism of the "pathogen" (H₂) into molecular intervention points.

Write output to programs/ab03-b/phase-3-vulcan.md
```

- [ ] **Step 2: Quality checks on Forge-B and Vulcan-B**

Same criteria as Task 4A.

- [ ] **Step 3: Run 6-model panel on Forge-B (standard prompts)**

```bash
sed -n '/===PHASE_3_FORGE===/,/===PHASE_4/{ /===PHASE_4/d; /===PHASE_3/d; p; }' tools/phase-prompts.txt > /tmp/ab03b-phase3-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-b/phase-3-candidates.md \
  --tier full \
  --system-prompt-file /tmp/ab03b-phase3-prompt.txt \
  --output programs/ab03-b/external-input-phase-3.md
```

- [ ] **Step 4: Commit**

```bash
git add programs/ab03-b/phase-3-candidates.md programs/ab03-b/phase-3-vulcan.md programs/ab03-b/prediction-log.md programs/ab03-b/external-input-phase-3.md
git commit -m "AB03-B phase 3: Forge RHAS candidates + Vulcan first-principles + 6-model panel"
```

---

## Task 5A: Run Surveyor — Variant A

**Files:**
- Read: `programs/ab03-a/phase-3-candidates.md`, `programs/ab03-a/phase-3-vulcan.md`, `programs/ab03-a/phase-1-disease-map.md`
- Create: `programs/ab03-a/phase-3b-survey-report.md`

> **Depends on:** Task 4A complete

- [ ] **Step 1: Launch Surveyor-A as a subagent**

```
You are Surveyor, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/surveyor.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context
3. programs/ab03-a/phase-3-candidates.md — Forge's candidates
4. programs/ab03-a/phase-3-vulcan.md — Vulcan's first-principles intervention points
5. programs/ab03-a/phase-1-disease-map.md — the H₂ metabolism map

IMPORTANT: This is a biochemistry problem, not a pathogen. Your target resolution may involve:
- Rumen microbial enzymes (fumarate reductase, CODH/ACS complex, hydrogenases)
- Host enzymes (if any host-side targets proposed)
- Engineered or synthetic proteins

Merge Forge and Vulcan candidates. For every candidate: resolve to specific protein/enzyme identifiers where possible, run BLAST for conservation across rumen microbial populations, check UniProt annotations, predict structures for top targets (AF3 where applicable).

Write output to programs/ab03-a/phase-3b-survey-report.md
```

- [ ] **Step 2: Overwatch quality check**

Verify: every candidate assessed, Forge-Vulcan overlap mapped (independent convergence noted), structure predictions attempted for top targets.

- [ ] **Step 3: Commit**

```bash
git add programs/ab03-a/phase-3b-survey-report.md
git commit -m "AB03-A phase 3b: Surveyor computational validation"
```

---

## Task 5B: Run Surveyor — Variant B

> **Depends on:** Task 4B complete. Can run in PARALLEL with Task 5A.

- [ ] **Step 1: Launch Surveyor-B**

Same structure as Task 5A but reading from `programs/ab03-b/` and using disease framing.

```
You are Surveyor, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read these files in order:
1. agents/surveyor.md — your base instructions
2. programs/ab03-b/program-context.md — the disease context
3. programs/ab03-b/phase-3-candidates.md — Forge's candidates
4. programs/ab03-b/phase-3-vulcan.md — Vulcan's first-principles intervention points
5. programs/ab03-b/phase-1-disease-map.md — the RHAS disease map

Merge Forge and Vulcan candidates. Assess every candidate computationally.

Write output to programs/ab03-b/phase-3b-survey-report.md
```

- [ ] **Step 2: Quality check and commit**

```bash
git add programs/ab03-b/phase-3b-survey-report.md
git commit -m "AB03-B phase 3b: Surveyor computational validation"
```

---

## Task 6A: Run Reaper — Variant A

**Files:**
- Read: All prior Variant A phase outputs + `agents/reaper.md`
- Create: `programs/ab03-a/phase-4-kill-report.md`
- Create: `programs/ab03-a/external-input-phase-4.md`

> **Depends on:** Task 5A complete

- [ ] **Step 1: Launch Reaper-A as a subagent**

```
You are Reaper, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/reaper.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context
3. programs/ab03-a/phase-3-candidates.md — all candidates
4. programs/ab03-a/phase-3-vulcan.md — Vulcan candidates
5. programs/ab03-a/phase-1-disease-map.md — the H₂ metabolism map
6. programs/ab03-a/phase-2-failure-analysis.md — failure analysis
7. programs/ab03-a/phase-3b-survey-report.md — Surveyor's computational validation

Kill everything that's weak. Apply ALL kill tests. Pay special attention to:
- Kill Test 1 (20-Year Test): fumarate, nitrate, acetogens have decades of research — why no product?
- Kill Test 3 (Matrix Test): rumen fluid, not broth
- Kill Test 7 (Stoichiometric Test): H₂ flux vs proposed sink capacity — does the math work?
- Extra scrutiny on feed additives: "why isn't the field doing this?"

Write output to programs/ab03-a/phase-4-kill-report.md
```

- [ ] **Step 2: Overwatch quality check**

Verify: kills are evidence-based not just skepticism, Surveyor data used, single-lab dependencies tagged, clinical endpoints included. Were the kills mechanism-level, not category-level?

- [ ] **Step 3: Run 6-model panel**

```bash
cat programs/ab03-a/panel-context.md > /tmp/ab03a-phase4-prompt.txt
echo -e "\n---\n" >> /tmp/ab03a-phase4-prompt.txt
sed -n '/===PHASE_4_REAPER===/,/===PHASE_5/{ /===PHASE_5/d; /===PHASE_4/d; p; }' tools/phase-prompts.txt >> /tmp/ab03a-phase4-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-a/phase-4-kill-report.md \
  --tier full \
  --system-prompt-file /tmp/ab03a-phase4-prompt.txt \
  --output programs/ab03-a/external-input-phase-4.md
```

- [ ] **Step 4: Commit**

```bash
git add programs/ab03-a/phase-4-kill-report.md programs/ab03-a/external-input-phase-4.md
git commit -m "AB03-A phase 4: Reaper kill report + 6-model panel"
```

---

## Task 6B: Run Reaper — Variant B

> **Depends on:** Task 5B complete. Can run in PARALLEL with Task 6A.

- [ ] **Step 1: Launch Reaper-B**

Same structure, reading from `programs/ab03-b/`, disease framing.

```
You are Reaper, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read these files in order:
1. agents/reaper.md — your base instructions
2. programs/ab03-b/program-context.md — the disease context
3. programs/ab03-b/phase-3-candidates.md — all candidates
4. programs/ab03-b/phase-3-vulcan.md — Vulcan candidates
5. programs/ab03-b/phase-1-disease-map.md — the RHAS disease map
6. programs/ab03-b/phase-2-failure-analysis.md — failure analysis
7. programs/ab03-b/phase-3b-survey-report.md — Surveyor validation

Apply all kill tests. This is framed as a disease — use your standard adversarial methodology.

Write output to programs/ab03-b/phase-4-kill-report.md
```

- [ ] **Step 2: Quality check, run panel (standard prompts), commit**

```bash
sed -n '/===PHASE_4_REAPER===/,/===PHASE_5/{ /===PHASE_5/d; /===PHASE_4/d; p; }' tools/phase-prompts.txt > /tmp/ab03b-phase4-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-b/phase-4-kill-report.md \
  --tier full \
  --system-prompt-file /tmp/ab03b-phase4-prompt.txt \
  --output programs/ab03-b/external-input-phase-4.md

git add programs/ab03-b/phase-4-kill-report.md programs/ab03-b/external-input-phase-4.md
git commit -m "AB03-B phase 4: Reaper RHAS kill report + 6-model panel"
```

---

## Task 7A: Run Board — Variant A

**Files:**
- Read: All prior Variant A outputs + `agents/board.md`
- Create: `programs/ab03-a/phase-4b-board-decision.md`

> **Depends on:** Task 6A complete

- [ ] **Step 1: Launch Board-A as a subagent**

```
You are the Board, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/board.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context
3. programs/ab03-a/phase-1-disease-map.md
4. programs/ab03-a/phase-2-failure-analysis.md
5. programs/ab03-a/phase-3-candidates.md
6. programs/ab03-a/phase-3b-survey-report.md
7. programs/ab03-a/phase-4-kill-report.md
8. programs/ab03-a/external-input-phase-4.md — 6-model panel challenges

This is an internal Agteria program (no partner). Force-rank by: leverage on H₂ disposal, information value of de-risk experiment, IP position, combination potential with existing methane inhibitors.

Run the external review panel as described in your instructions, then synthesize and force-rank.

Write output to programs/ab03-a/phase-4b-board-decision.md
```

- [ ] **Step 2: Overwatch quality check**

Verify: external feedback synthesized, devil's advocate inversion for each survived target, genuine force-ranking (not all-equal), novel drug targets ranked above feed additives at equivalent evidence.

- [ ] **Step 3: Prompt Daniel for web review (if warranted)**

At this checkpoint, ask Daniel if he wants to submit the Board output to web-based models (Claude Web, GPT-5.4 Web, Gemini Extended Thinking) for human-in-the-loop review.

- [ ] **Step 4: Commit**

```bash
git add programs/ab03-a/phase-4b-board-decision.md
git commit -m "AB03-A phase 4b: Board strategic force-ranking"
```

---

## Task 7B: Run Board — Variant B

> **Depends on:** Task 6B complete. Can run in PARALLEL with Task 7A.

- [ ] **Step 1: Launch Board-B**

Same structure, reading from `programs/ab03-b/`, disease framing.

```
You are the Board, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read all prior phase outputs from programs/ab03-b/ plus agents/board.md.
This is an internal Agteria program. Use standard Board methodology with disease framing.

Write output to programs/ab03-b/phase-4b-board-decision.md
```

- [ ] **Step 2: Quality check, web review prompt, commit**

```bash
git add programs/ab03-b/phase-4b-board-decision.md
git commit -m "AB03-B phase 4b: Board RHAS strategic force-ranking"
```

---

## Task 8A: Run Anvil — Variant A

**Files:**
- Read: All prior Variant A outputs + `agents/anvil.md`
- Create: `programs/ab03-a/phase-5-coverage-map.md`
- Create: `programs/ab03-a/phase-5-evidence-register.md`
- Create: `programs/ab03-a/phase-5-decision-memo.md`
- Create: `programs/ab03-a/external-input-phase-5.md`

> **Depends on:** Task 7A complete

- [ ] **Step 1: Launch Anvil-A as a subagent**

```
You are Anvil, running for program AB03-A (Rumen H₂ Sink — Biochemistry Mode).

Read these files in order:
1. agents/anvil.md — your base instructions
2. programs/ab03-a/program-context.md — the problem context
3. All prior phase outputs from programs/ab03-a/
4. programs/ab03-a/phase-4b-board-decision.md — the Board's force-ranking

IMPORTANT: This is an internal Agteria program (no partner). The "disease stages" are H₂ metabolism stages. For the 70% test:
- "Tractable" = amenable to a molecular/biological intervention (enzyme, microbe, electron acceptor)
- "Non-tractable" = management-only (feed rate, timing) — not a drug target
- Coverage is calculated against tractable H₂ metabolism stages only

Use the Board's force-ranking for prioritisation. Flag KE#1 if not yet run. Complete the prediction log.

Write to:
- programs/ab03-a/phase-5-coverage-map.md
- programs/ab03-a/phase-5-evidence-register.md
- programs/ab03-a/phase-5-decision-memo.md
```

- [ ] **Step 2: Overwatch quality check — THE 70% ENFORCEMENT**

This is the most important check. Read `programs/ab03-a/phase-5-coverage-map.md`:
1. Is every H₂ metabolism stage covered?
2. Are coverage estimates honest (not inflated)?
3. Does total coverage hit 70% of tractable stages?

If it fails: send Forge-A back for uncovered stages → Surveyor-A → Reaper-A → Anvil-A. Maximum 3 loops.

- [ ] **Step 3: Run 6-model panel on Anvil-A output**

```bash
cat programs/ab03-a/panel-context.md > /tmp/ab03a-phase5-prompt.txt
echo -e "\n---\n" >> /tmp/ab03a-phase5-prompt.txt
sed -n '/===PHASE_5_ANVIL===/,/^$/p' tools/phase-prompts.txt >> /tmp/ab03a-phase5-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-a/phase-5-decision-memo.md \
  --tier full \
  --system-prompt-file /tmp/ab03a-phase5-prompt.txt \
  --output programs/ab03-a/external-input-phase-5.md
```

- [ ] **Step 4: Commit**

```bash
git add programs/ab03-a/phase-5-coverage-map.md programs/ab03-a/phase-5-evidence-register.md programs/ab03-a/phase-5-decision-memo.md programs/ab03-a/prediction-log.md programs/ab03-a/external-input-phase-5.md
git commit -m "AB03-A phase 5: Anvil portfolio + 70% test + 6-model panel"
```

---

## Task 8B: Run Anvil — Variant B

> **Depends on:** Task 7B complete. Can run in PARALLEL with Task 8A.

- [ ] **Step 1: Launch Anvil-B**

```
You are Anvil, running for program AB03-B (Rumen Hydrogen Accumulation Syndrome — Disease Mode).

Read all prior phase outputs from programs/ab03-b/ plus agents/anvil.md.
This is an internal Agteria program. Use standard Anvil methodology with disease framing.
Run the 70% test against RHAS disease stages.

Write to:
- programs/ab03-b/phase-5-coverage-map.md
- programs/ab03-b/phase-5-evidence-register.md
- programs/ab03-b/phase-5-decision-memo.md
```

- [ ] **Step 2: 70% enforcement loop (same as Task 8A)**

- [ ] **Step 3: Run 6-model panel (standard prompts), commit**

```bash
sed -n '/===PHASE_5_ANVIL===/,/^$/p' tools/phase-prompts.txt > /tmp/ab03b-phase5-prompt.txt

python3 tools/cross-check.py --adversarial programs/ab03-b/phase-5-decision-memo.md \
  --tier full \
  --system-prompt-file /tmp/ab03b-phase5-prompt.txt \
  --output programs/ab03-b/external-input-phase-5.md

git add programs/ab03-b/phase-5-coverage-map.md programs/ab03-b/phase-5-evidence-register.md programs/ab03-b/phase-5-decision-memo.md programs/ab03-b/prediction-log.md programs/ab03-b/external-input-phase-5.md
git commit -m "AB03-B phase 5: Anvil RHAS portfolio + 70% test + 6-model panel"
```

---

## Task 9: Meta-Analysis — Compare A vs B

**Files:**
- Read: All outputs from `programs/ab03-a/` and `programs/ab03-b/`
- Create: `programs/ab03-comparison.md`

> **Depends on:** Tasks 8A AND 8B both complete

- [ ] **Step 1: Overwatch reads all phase outputs from both variants**

Read side-by-side:
- Both Pathfinder maps
- Both Tribunal consensuses
- Both Sapper failure analyses
- Both Forge candidate lists + both Vulcan outputs
- Both Surveyor reports
- Both Reaper kill reports
- Both Board decisions
- Both Anvil portfolios (coverage maps, evidence registers, decision memos)

- [ ] **Step 2: Write `programs/ab03-comparison.md`**

Structure per the spec's Meta-Analysis section:

```markdown
# AB03 — Dual-Framing Comparison: Biochemistry Mode vs Disease Mode

**Date:** 2026-03-30
**Experiment:** Same problem (rumen H₂ sink during methanogenesis inhibition) run through the full Overwatch pipeline with two different framings

---

## 1. Problem Map Comparison
[Side-by-side analysis of Pathfinder-A vs Pathfinder-B outputs]

## 2. Bottleneck Consensus Comparison
[Tribunal-A vs Tribunal-B: same bottleneck? Different frame diversity?]

## 3. Failure Analysis Comparison
[Sapper-A vs Sapper-B: depth, mechanism-level rigor]

## 4. Candidate Novelty Comparison
[Total unique, novel, and Vulcan-only candidates per variant]

## 5. Kill Resistance Comparison
[What survived in each? Same targets or different?]

## 6. Portfolio Coverage Comparison
[70% test results, coverage quality]

## 7. Framing Artifact Analysis
[Where did framing help or hurt? Forced structure, vocabulary mismatch, anchoring, creative freedom, panel quality]

## 8. Recommendation
[For future non-disease problems: adapted framing, disease framing, or both?]
```

Populate every section with specific evidence from the outputs. Quote directly from phase documents. Use tables for side-by-side comparisons. This is the primary deliverable of the meta-experiment.

- [ ] **Step 3: Commit**

```bash
git add programs/ab03-comparison.md
git commit -m "AB03: dual-framing meta-analysis comparing biochemistry vs disease mode"
```

---

## Task Dependency Graph

```
Task 0 (setup)
├── Task 1A (Pathfinder-A) ─── Task 2A (Tribunal-A) ─── Task 3A (Sapper-A) ─── Task 4A (Forge+Vulcan-A) ─── Task 5A (Surveyor-A) ─── Task 6A (Reaper-A) ─── Task 7A (Board-A) ─── Task 8A (Anvil-A) ──┐
│                                                                                                                                                                                                          ├── Task 9 (Comparison)
└── Task 1B (Pathfinder-B) ─── Task 2B (Tribunal-B) ─── Task 3B (Sapper-B) ─── Task 4B (Forge+Vulcan-B) ─── Task 5B (Surveyor-B) ─── Task 6B (Reaper-B) ─── Task 7B (Board-B) ─── Task 8B (Anvil-B) ──┘
```

**Maximum parallelism:** A and B variants run simultaneously. Within each variant, Forge and Vulcan run in parallel. All other agents are sequential within their variant.

**Estimated panel cost:** ~$0.10-0.30 per phase × 5 panel phases × 2 variants = ~$1-3 total.
