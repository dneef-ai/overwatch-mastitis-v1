# Surveyor Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Surveyor as the sixth agent in the Overwatch pipeline, align workflow.md phase numbering with run-program.sh, and ensure the 70% test loop includes Surveyor.

**Architecture:** Surveyor sits between Forge (Phase 3) and Reaper (Phase 4) as a computational target validation agent. It runs within the Phase 3 block of run-program.sh. The 70% enforcement loop (Anvil→Forge→Surveyor→Reaper→Anvil) is the critical path.

**Tech Stack:** Markdown agent prompts, Bash shell script, BioPython/NCBI/UniProt APIs (referenced in prompts, not implemented here)

**Spec:** `docs/superpowers/specs/2026-03-24-surveyor-agent-design.md`

---

### Task 1: Create the Surveyor Agent Prompt

**Files:**
- Create: `agents/surveyor.md`

This is the core deliverable. The agent prompt defines Surveyor's identity, inputs, outputs, analysis tiers, tool usage, and constraints. It must match the design spec exactly while following the voice and structure of the existing agent prompts (direct, imperative, focused on ONE job).

Reference the existing agent prompts for style: `agents/pathfinder.md`, `agents/forge.md`, `agents/reaper.md`. Each starts with identity + ONE job, then output, then methodology, then "How to Work", then "What NOT to Do."

Reference the spec for content: `docs/superpowers/specs/2026-03-24-surveyor-agent-design.md` — especially Step 0 (target resolution), tiered analysis (A/B vs C), output format, tool stack, and constraints.

- [ ] **Step 1: Write `agents/surveyor.md`**

The prompt must include these sections in order:

1. **Identity and ONE job** — "You are Surveyor, a computational biologist. Your ONE job is to computationally validate every candidate target from Forge before Reaper attacks it."

2. **Your Output** — Write `phase-3b-survey-report.md` in the program directory. Read `phase-3-candidates.md` first. Also read `phase-1-disease-map.md` for disease context and species/strain information.

3. **Step 0: Target Resolution** — First step: resolve every candidate's natural-language target description to specific identifiers (gene name, protein accession, organism taxonomy ID, amino acid sequence). Query NCBI Entrez and UniProt. If a target can't be resolved to a specific protein (pathway targets, non-protein mechanisms), note it and skip BLAST/structure — assess only what's computationally tractable. This is also a sequence availability gate.

4. **Category A/B Analysis (Reality Check)** — For known/non-obvious candidates:
   - Conservation: BLAST across field-relevant isolates. Report % identity per strain. Thresholds: <80% = "divergent", absent from >20% of strains = "conservation concern". Maps to Quality Standard 16.
   - Host selectivity: BLAST against host proteome. Flag >50% identity at >50% query coverage. Maps to Quality Standard 14.
   - Annotation verification: UniProt/Entrez to confirm localization, function, essentiality. If Forge claims surface-exposed, verify it.

5. **Category C Analysis (Full Workup)** — Everything above, plus:
   - Structure: First check AlphaFold DB (alphafold.ebi.ac.uk API) for pre-computed structures. If not found and structure is needed (co-folding, novel fold), write an AF3 submission request to `bioinfo/af3_requests/[target].md` with sequence (FASTA), job name, co-factors, and rationale. Mark structure field as "AF3 SUBMISSION REQUESTED". Complete all other analyses while waiting.
   - Operon/gene neighborhood: Query NCBI for genomic context — virulence island membership, co-regulation, essential gene neighbors.
   - Signal peptide/transmembrane: Confirm accessibility via UniProt annotations and sequence features.

6. **Output Format** — Include the exact per-candidate assessment template from the spec (Resolved Identity, Conservation, Host Selectivity, Annotation Check, Structure, Operon Context, Accessibility, Verdict, Wet-lab confirmation type). Include the summary table format at the top of the report.

7. **NCBI API Key and Rate Limiting** — Must use an NCBI API key via `Entrez.api_key`. Cache all BLAST results in `bioinfo/cache/` keyed by sequence hash. Stagger BLAST submissions (5-30 min per query). Max 10 concurrent NCBI requests with API key.

8. **How to Work** — Unlimited subagent budget. Launch parallel agents per candidate for independent analyses. Each subagent checks cache before submitting BLAST. Each writes to `bioinfo/results/[target-name].md`. Main process compiles final report. Reference Argus bioinfo at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/` as a reference implementation.

9. **File Structure** — Create `bioinfo/` directory with subdirs: `scripts/`, `sequences/`, `structures/`, `af3_requests/`, `results/`, `cache/`.

10. **What NOT to Do:**
    - Don't make kill decisions — provide data, not verdicts on viability. CONFIRMED/CORRECTED/FLAGGED, not KILLED.
    - Don't search PubMed or review papers — that's Forge and Reaper's job
    - Don't design experiments with budgets or GO/KILL thresholds — that's Anvil's job. Only suggest the TYPE of wet-lab confirmation.
    - Don't promote or kill targets based on computational evidence alone (Quality Standard 8)
    - Don't describe what BLAST would show — actually run it. Write Python scripts, execute them, report real results.
    - Don't skip candidates — every candidate in Forge's output gets assessed

- [ ] **Step 2: Verify the file exists and reads correctly**

Run: `wc -l agents/surveyor.md && head -5 agents/surveyor.md`

- [ ] **Step 3: Commit**

```bash
git add agents/surveyor.md
git commit -m "feat: add Surveyor agent prompt — computational target validation between Forge and Reaper"
```

---

### Task 2: Align and Rewrite workflow.md

**Files:**
- Modify: `docs/workflow.md` (full rewrite)

The current `workflow.md` has phase numbers misaligned with `CLAUDE.md` and `run-program.sh`. Specifically:
- workflow.md Phase 4 = "The 70% Test" (standalone phase)
- workflow.md Phase 5 = "De-Risk & Deliver"
- But run-program.sh Phase 4 = Reaper, Phase 5 = Anvil (which does BOTH 70% test AND deliverables)

The aligned structure must be:
- Phase 1: Disease Map (Pathfinder) — unchanged
- Phase 2: Treatment Failure Analysis (Sapper) — unchanged
- Phase 3: Propose Solutions (Forge) + Computational Validation (Surveyor) — add Surveyor
- Phase 4: Red Team (Reaper) — was "The 70% Test" in old workflow.md
- Phase 5: Portfolio + 70% Test + Deliverables (Anvil) — merge old phases 4+5

**CRITICAL: The 70% test content must NOT be lost.** It moves from being a standalone Phase 4 into Phase 5 as Anvil's gatekeeper step. All 70% test details (estimation method, common failure modes, the loop logic) must be preserved.

- [ ] **Step 1: Rewrite `docs/workflow.md`**

New structure:

```markdown
# Overwatch Drug Discovery Workflow

This document defines the 6-agent, 5-phase workflow for Overwatch drug discovery programs.
Follow these phases in order. Do not skip phases.

---

## Phase 1: Disease Map (Pathfinder)
[Keep existing Phase 1 content unchanged — lines 9-40 of current file]

---

## Phase 2: Treatment Failure Analysis (Sapper)
[Keep existing Phase 2 content unchanged — lines 43-70 of current file]

---

## Phase 3: Propose Solutions (Forge) + Computational Validation (Surveyor)

### Phase 3a: Propose Solutions (Forge)

#### Goal
[Keep existing Phase 3 Goal/What to Do/Output/Completion Criteria/Common Failure Modes — lines 73-108]

### Phase 3b: Computational Target Validation (Surveyor)

#### Goal
Computationally validate every candidate target before the red team attacks it. Answer: is this target real, unique, conserved, and structurally plausible?

#### What to Do
1. Resolve each candidate to specific identifiers (gene name, protein accession, taxonomy ID, sequence)
2. For Category A/B (known/non-obvious) candidates — reality check:
   - BLAST across field-relevant pathogen isolates for conservation (Standard 16)
   - BLAST against host proteome for selectivity risk (Standard 14)
   - Verify claimed localization, function, essentiality via UniProt/Entrez
3. For Category C (novel) candidates — full workup (all of the above plus):
   - Check AlphaFold DB for pre-computed structures; if not available, write AF3 submission request for Daniel
   - Operon/gene neighborhood analysis for virulence context
   - Signal peptide/transmembrane prediction for accessibility
4. Run external validation on candidates (after Surveyor enrichment):
   ```
   python3 tools/cross-check.py --adversarial phase-3-candidates.md \
     --tier premium --system-prompt-file tools/external-review-prompt.txt \
     --output phase-3-external-review.md
   ```
5. If AF3 submissions are pending, pause for Daniel to submit and return results

#### Output
`phase-3b-survey-report.md` — per-candidate computational assessment with verdicts (CONFIRMED/CORRECTED/FLAGGED), summary table, and suggested wet-lab confirmation types.

#### Completion Criteria
- Every candidate has a verdict
- BLAST was actually run (parameters reported), not just described
- Category C targets have structure predictions or documented AF3 submission requests
- All flagged items reviewed before passing to Reaper

#### Common Failure Modes
- Describing what BLAST would show instead of running it
- Skipping candidates because they're "well-known"
- Making kill decisions (that's Reaper's job — Surveyor provides data)
- Promoting targets based on computational evidence alone (Standard 8)

---

## Phase 4: Red Team (Reaper)

### Goal
Find the fatal flaw in every proposal and kill it with evidence. Reaper reads both `phase-3-candidates.md` and `phase-3b-survey-report.md`.

### What to Do
[Keep existing Phase 4 Red Team content — this maps to what Reaper actually does. Note: the OLD workflow.md had "The 70% Test" as Phase 4, but that was misaligned. The 70% test is part of Phase 5 (Anvil). Phase 4 is Reaper's kill tests.]

Apply 10 kill tests to every candidate:
1. The 20-Year Test — known >5 years with no product? Why?
2. The Species Test — evidence from target species or extrapolated? Use Surveyor's host homology data.
3. The Matrix Test — tested in real biological matrix?
4. The Strain Test — tested across relevant pathogen lineages? Use Surveyor's conservation data.
5. The Resistance Test — how fast would resistance develop?
6. The Citation Test — verify key PMIDs
7. The Stoichiometric Test — molecules per cell calculation
8. The Embarrassment Test — simplest plausible failure
9. The Repetition Test — repeating a known failure mode?
10. The Commercial Reality Test — route, cost, regulatory, withdrawal

### Output
`phase-4-kill-report.md` — verdict for each candidate: KILLED / WOUNDED / SURVIVED

### Completion Criteria
- Every candidate attacked
- Kills are evidence-based, not just skepticism
- Surveyor's computational data used where relevant (species, strain, host selectivity tests)

---

## Phase 5: Portfolio + 70% Test + Deliverables (Anvil)

### Goal
Build surviving candidates into a partner-grade program. The 70% pathology coverage test is MANDATORY and comes first.

### Step 1: The 70% Test (MANDATORY — Cannot Skip)

This is the gatekeeper. Before building anything:

1. List every disease stage from Phase 1 with its contribution to overall pathology (rough % with evidence tier)
2. For each stage, list which surviving candidate addresses it
3. For each candidate, estimate maximum pathology reduction if it works perfectly (with evidence tier and reasoning)
4. Sum coverage across all stages
5. **If total < 70%: STOP.** Write a gap report. This goes back to Overwatch, who sends Forge back for the uncovered stages, then Surveyor, then Reaper, then back to Anvil. Maximum 3 loops.
6. **If total ≥ 70%: Proceed.**

#### How to Estimate Pathology Contribution
Use published data where available:
- Clinical outcome attribution studies
- Knockout/mutant phenotype data (removing this factor changes disease by X%)
- Epidemiological data (what fraction of cases involve this mechanism?)
Where data is insufficient, state reasoning and tag as [INFERRED].
Do NOT inflate estimates to pass the test.

#### Common 70% Test Failure Modes
- Inflating coverage estimates to pass the test
- Double-counting (one candidate doesn't address two stages at 100% each)
- Accepting 70% without checking that coverage estimates are honest
- Treating the 70% threshold as a formality rather than a real constraint

### Step 2: De-Risk & Deliver
[Keep existing Phase 5 De-Risk & Deliver content — TPPs, GO/KILL gates, experiment design, evidence register, decision memo, external review, completion criteria]

### Output
- `phase-5-coverage-map.md` — the 70% test result
- `phase-5-evidence-register.md` — structured evidence by target
- `phase-5-decision-memo.md` — partner-facing recommendation

### Completion Criteria
- 70% test PASSED (coverage ≥70% with honest estimates)
- Every candidate has GO/KILL gate, experiment, budget, TPP
- External models reviewed the final output
- All citation PMIDs verified
- Embarrassment pass honest and specific for each target

---

## Output Directory Convention

Program outputs go in the program directory:
- `programs/mastitis/` for mastitis
- `programs/liver-abscess/` for liver abscess
- Each phase produces its named artifact in this directory.
```

- [ ] **Step 2: Verify the 70% test content is preserved**

Grep for "70%" in the new file — should appear in Phase 5, the common failure modes, and the loop description. The 70% test must NOT have been lost in the rewrite.

Run: `grep -c "70%" docs/workflow.md` — should be ≥5 occurrences.

- [ ] **Step 3: Commit**

```bash
git add docs/workflow.md
git commit -m "fix: align workflow.md phases with agent pipeline, add Surveyor (Phase 3b), move 70% test into Phase 5"
```

---

### Task 3: Update run-program.sh

**Files:**
- Modify: `run-program.sh`

Three changes:
1. Add Surveyor invocation in Phase 3 block (between Forge and external review)
2. Add AF3 checkpoint after Surveyor
3. Add Surveyor to the 70% enforcement loop
4. Update header comments to reflect 6-agent pipeline

- [ ] **Step 1: Update script header**

Change line 2 from:
```bash
# run-program.sh — Run the full 5-phase drug discovery workflow for a program
```
to:
```bash
# run-program.sh — Run the full 6-agent, 5-phase drug discovery workflow for a program
```

- [ ] **Step 2: Add AF3 checkpoint helper function**

Insert between the `check_70_percent()` closing brace and the `# ─── Main Workflow` comment. Use the old_string `echo "70% test: PASSED"\n    return 0\n  fi\n}` and append the new function after it, before the Main Workflow section. The exact insertion point is after line 183 (end of `check_70_percent`), before line 185 (`# ─── Main Workflow`).

```bash
check_af3_requests() {
  local af3_dir="$PROGRAM_DIR/bioinfo/af3_requests"
  if [[ -d "$af3_dir" ]] && [[ -n "$(ls -A "$af3_dir" 2>/dev/null)" ]]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║  AF3 SUBMISSION CHECKPOINT                                   ║"
    echo "╠══════════════════════════════════════════════════════════════╣"
    echo "║  Surveyor has requested AlphaFold3 structure predictions.    ║"
    echo "║                                                              ║"
    echo "║  Submission requests are in:                                 ║"
    echo "║  $af3_dir/"
    echo "║                                                              ║"
    echo "║  For each request:                                           ║"
    echo "║  1. Go to alphafoldserver.com                                ║"
    echo "║  2. Submit the sequence with specified co-factors            ║"
    echo "║  3. Download results to programs/$PROGRAM/bioinfo/structures/ ║"
    echo "║                                                              ║"
    echo "║  Press ENTER when done (or to skip for now)...               ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    read -r
  fi
}
```

- [ ] **Step 3: Update Phase 3 block to include Surveyor**

Replace lines 206-210:
```bash
# Phase 3: Propose Solutions (Forge)
if (( START_PHASE <= 3 )); then
  run_agent "forge" 3
  run_external_review 3 "phase-3-candidates.md"
fi
```

with:
```bash
# Phase 3: Propose Solutions (Forge) + Computational Validation (Surveyor)
if (( START_PHASE <= 3 )); then
  run_agent "forge" 3
  run_agent "surveyor" "3b"
  check_af3_requests
  run_external_review 3 "phase-3-candidates.md"
fi
```

- [ ] **Step 4: Add Surveyor to the 70% enforcement loop**

Replace lines 230-233:
```bash
    echo "Loop $LOOP: Sending back to Forge for uncovered stages..."
    run_agent "forge" "5-revision-$LOOP"
    run_agent "reaper" "5-revision-$LOOP"
    run_agent "anvil" "5-revision-$LOOP"
```

with:
```bash
    echo "Loop $LOOP: Sending back to Forge for uncovered stages..."
    run_agent "forge" "5-revision-$LOOP"
    run_agent "surveyor" "5-revision-$LOOP"
    check_af3_requests
    run_agent "reaper" "5-revision-$LOOP"
    run_agent "anvil" "5-revision-$LOOP"
```

- [ ] **Step 5: Verify the script is syntactically valid**

Run: `bash -n run-program.sh` — should produce no output (no syntax errors).

- [ ] **Step 6: Verify Surveyor appears in the right places**

Run: `grep -n "surveyor" run-program.sh` — should show invocations in both the Phase 3 block and the 70% loop.

- [ ] **Step 7: Commit**

```bash
git add run-program.sh
git commit -m "feat: add Surveyor to pipeline — Phase 3b invocation + AF3 checkpoint + 70% loop integration"
```

---

### Task 4: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

Six changes to the orchestrator instructions:
1. Agent count and table
2. Agent prompts list
3. Workflow reference
4. Manual mode instructions
5. After Each Agent quality checks
6. 70% enforcement loop (add Surveyor)

- [ ] **Step 1: Update agent count and table**

Replace lines 5-17:
```markdown
Five specialist agents, each a full Claude Code process that can deploy its own subagents:

| Agent | Job | Input | Output |
|-------|-----|-------|--------|
| **Pathfinder** | Map the disease completely | Disease name + prior work | `phase-1-disease-map.md` |
| **Sapper** | Explain why every treatment failed | Disease map | `phase-2-failure-analysis.md` |
| **Forge** | Propose solutions for EVERY disease stage | Disease map + failure analysis | `phase-3-candidates.md` |
| **Reaper** | Kill everything that's weak | Candidates | `phase-4-kill-report.md` |
| **Anvil** | Build portfolio, run 70% test, deliver | Everything above | Coverage map + evidence register + decision memo |

Agent prompts: `agents/pathfinder.md`, `agents/sapper.md`, `agents/forge.md`, `agents/reaper.md`, `agents/anvil.md`
```

with:
```markdown
Six specialist agents, each a full Claude Code process that can deploy its own subagents:

| Agent | Job | Input | Output |
|-------|-----|-------|--------|
| **Pathfinder** | Map the disease completely | Disease name + prior work | `phase-1-disease-map.md` |
| **Sapper** | Explain why every treatment failed | Disease map | `phase-2-failure-analysis.md` |
| **Forge** | Propose solutions for EVERY disease stage | Disease map + failure analysis | `phase-3-candidates.md` |
| **Surveyor** | Computationally validate targets | Forge candidates + disease map | `phase-3b-survey-report.md` |
| **Reaper** | Kill everything that's weak | Candidates + survey report | `phase-4-kill-report.md` |
| **Anvil** | Build portfolio, run 70% test, deliver | Everything above | Coverage map + evidence register + decision memo |

Agent prompts: `agents/pathfinder.md`, `agents/sapper.md`, `agents/forge.md`, `agents/surveyor.md`, `agents/reaper.md`, `agents/anvil.md`
```

- [ ] **Step 2: Update automated workflow examples**

Replace lines 49-54:
```markdown
### Automated (full workflow)
```bash
./run-program.sh mastitis                    # Run all 5 phases
./run-program.sh mastitis --phase 3          # Start from phase 3
./run-program.sh mastitis --skip-external    # Skip API review (still prompts for web)
```
```

with:
```markdown
### Automated (full workflow)
```bash
./run-program.sh mastitis                    # Run all 6 agents across 5 phases
./run-program.sh mastitis --phase 3          # Start from phase 3 (Forge + Surveyor + external review)
./run-program.sh mastitis --skip-external    # Skip API review (still prompts for web)
```
```

- [ ] **Step 3: Update manual mode instructions**

Replace lines 56-65:
```markdown
### Manual (interactive — you control each step)
Daniel tells you what to run. You launch agents one at a time:

1. "Run Pathfinder on mastitis" → launch Pathfinder, review output, discuss with Daniel
2. "Run Sapper" → launch Sapper, review output
3. "Run Forge" → launch Forge, run external review, discuss alternatives with Daniel
4. "Run Reaper" → launch Reaper, review kills with Daniel
5. "Run Anvil" → launch Anvil, check 70% test, iterate if needed

Manual mode is better for the first run of a new disease. Automated mode is for re-runs.
```

with:
```markdown
### Manual (interactive — you control each step)
Daniel tells you what to run. You launch agents one at a time:

1. "Run Pathfinder on mastitis" → launch Pathfinder, review output, discuss with Daniel
2. "Run Sapper" → launch Sapper, review output
3. "Run Forge" → launch Forge, discuss alternatives with Daniel
3b. "Run Surveyor" → launch Surveyor, review computational findings, discuss flagged items with Daniel. If AF3 submissions needed, pause for Daniel to submit and return results.
4. "Run Reaper" → launch Reaper (now has Surveyor's data), review kills with Daniel
5. "Run Anvil" → launch Anvil, check 70% test, iterate if needed

After Forge and Surveyor: run external review, discuss alternatives with Daniel.

Manual mode is better for the first run of a new disease. Automated mode is for re-runs.
```

- [ ] **Step 4: Update "Before Each Agent" section**

Replace lines 71-74:
```markdown
### Before Each Agent
- Set context: what prior agents found, what to pay attention to
- For Forge: explicitly list the gap stages from Sapper's analysis — "these stages need novel proposals"
- For Reaper: no guidance — let it be pure adversary
```

with:
```markdown
### Before Each Agent
- Set context: what prior agents found, what to pay attention to
- For Forge: explicitly list the gap stages from Sapper's analysis — "these stages need novel proposals"
- For Surveyor: pass through Forge's candidates without filtering — Surveyor assesses everything
- For Reaper: no guidance — let it be pure adversary. But make sure it has the survey report.
```

- [ ] **Step 5: Update "After Each Agent" section**

Replace lines 76-83:
```markdown
### After Each Agent
- Read the output before passing it to the next agent
- Check: did the agent follow its instructions? Did it cut corners?
- For Pathfinder: is the disease map complete? Any stages missing?
- For Sapper: does EVERY treatment have a specific failure mechanism (not just "didn't work")?
- For Forge: does EVERY disease stage have at least one candidate? If not, SEND IT BACK.
- For Reaper: were the kills evidence-based or just skepticism?
- For Anvil: did the 70% test actually pass honestly? Check the math.
```

with:
```markdown
### After Each Agent
- Read the output before passing it to the next agent
- Check: did the agent follow its instructions? Did it cut corners?
- For Pathfinder: is the disease map complete? Any stages missing?
- For Sapper: does EVERY treatment have a specific failure mechanism (not just "didn't work")?
- For Forge: does EVERY disease stage have at least one candidate? If not, SEND IT BACK.
- For Surveyor: did every candidate get a verdict? Did it actually run BLAST or just describe what BLAST would show? Are BLAST parameters reported (database, e-value threshold)? If a Category C target has no structure prediction, is there a valid reason (e.g., AF3 submission pending)? Are there AF3 submissions pending that need Daniel's action?
- For Reaper: were the kills evidence-based or just skepticism? Did it use Surveyor's data?
- For Anvil: did the 70% test actually pass honestly? Check the math.
```

- [ ] **Step 6: Update the 70% enforcement loop**

Replace lines 85-91:
```markdown
### The 70% Enforcement Loop
This is your most important function. When Anvil reports the coverage map:
1. Read it yourself
2. Check: is every disease stage covered?
3. Check: are the coverage estimates honest (not inflated)?
4. If it fails: send Forge back for the uncovered stages, then Reaper, then Anvil again
5. Maximum 3 loops. If it still fails after 3, escalate to Daniel.
```

with:
```markdown
### The 70% Enforcement Loop
This is your most important function. When Anvil reports the coverage map:
1. Read it yourself
2. Check: is every disease stage covered?
3. Check: are the coverage estimates honest (not inflated)?
4. If it fails: send Forge back for the uncovered stages, then Surveyor, then Reaper, then Anvil again
5. Maximum 3 loops. If it still fails after 3, escalate to Daniel.
```

- [ ] **Step 7: Update "Key Paths" workflow reference**

Replace line 104:
```markdown
- Workflow: `docs/workflow.md` (5 phases)
```

with:
```markdown
- Workflow: `docs/workflow.md` (6 agents, 5 phases)
```

- [ ] **Step 8: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add Surveyor to orchestrator — agent table, manual mode, quality checks, 70% loop"
```

---

### Task 5: Update Reaper Agent Prompt

**Files:**
- Modify: `agents/reaper.md:9-13`

Add `phase-3b-survey-report.md` to Reaper's input documents and note which kill tests benefit from computational data.

- [ ] **Step 1: Update the "Also read" list**

Replace lines 9-13:
```markdown
Write `phase-4-kill-report.md` in the program directory. Read the candidates document (`phase-3-candidates.md`) and attack every single candidate.

Also read:
- `phase-1-disease-map.md` — to check if candidates actually address what they claim
- `phase-2-failure-analysis.md` — to check if candidates repeat known failure modes
```

with:
```markdown
Write `phase-4-kill-report.md` in the program directory. Read the candidates document (`phase-3-candidates.md`) and attack every single candidate.

Also read:
- `phase-1-disease-map.md` — to check if candidates actually address what they claim
- `phase-2-failure-analysis.md` — to check if candidates repeat known failure modes
- `phase-3b-survey-report.md` — Surveyor's computational validation of targets (conservation across field isolates, host homology, protein annotation, structure predictions). Use this data to ground your kill tests — especially Kill Test 2 (species), Kill Test 4 (strain), Kill Test 5 (resistance), and host selectivity. If Surveyor flagged a target, that's your starting point.
```

- [ ] **Step 2: Commit**

```bash
git add agents/reaper.md
git commit -m "feat: add Surveyor report to Reaper inputs — computational data grounds kill tests"
```

---

### Task 6: Update Anvil Agent Prompt

**Files:**
- Modify: `agents/anvil.md:15-19`

Add `phase-3b-survey-report.md` to Anvil's input documents and note how computational data informs de-risk experiments and the evidence register.

- [ ] **Step 1: Update the "Read ALL prior documents" list**

Replace lines 15-19:
```markdown
Read ALL prior documents first:
- `phase-1-disease-map.md` — the disease stages
- `phase-2-failure-analysis.md` — why treatments fail
- `phase-3-candidates.md` — the proposals
- `phase-4-kill-report.md` — what survived and what didn't
```

with:
```markdown
Read ALL prior documents first:
- `phase-1-disease-map.md` — the disease stages
- `phase-2-failure-analysis.md` — why treatments fail
- `phase-3-candidates.md` — the proposals
- `phase-3b-survey-report.md` — Surveyor's computational validation (conservation, host homology, structure predictions, annotation). Use this data when designing de-risk experiments — Surveyor's structure predictions inform assay design, conservation data confirms strain coverage, and host selectivity flags inform safety assessment. Include computational evidence in the evidence register tagged as [COMPUTATIONAL].
- `phase-4-kill-report.md` — what survived and what didn't
```

- [ ] **Step 2: Commit**

```bash
git add agents/anvil.md
git commit -m "feat: add Surveyor report to Anvil inputs — computational data informs de-risk experiments"
```

---

### Task 7: Final Verification

- [ ] **Step 1: Verify all 6 agent prompts exist**

Run: `ls -la agents/*.md | wc -l` — should be 6.

- [ ] **Step 2: Verify Surveyor appears in all critical locations**

Run: `grep -rl "surveyor\|Surveyor\|survey-report\|phase-3b" agents/ CLAUDE.md run-program.sh docs/workflow.md` — should list at least: `agents/surveyor.md`, `agents/reaper.md`, `agents/anvil.md`, `CLAUDE.md`, `run-program.sh`, `docs/workflow.md`.

- [ ] **Step 3: Verify the 70% test is preserved and active**

Run: `grep -c "70%" docs/workflow.md` — should be ≥5.
Run: `grep -c "70%" CLAUDE.md` — should be ≥2.
Run: `grep -c "70%" run-program.sh` — should be ≥3.
Run: `grep -c "70%" agents/anvil.md` — should be ≥3.

- [ ] **Step 4: Verify run-program.sh has no syntax errors**

Run: `bash -n run-program.sh` — should produce no output.

- [ ] **Step 5: Verify Surveyor is in the 70% loop in run-program.sh**

Run: `grep -A2 "revision-\$LOOP" run-program.sh` — should show `surveyor` between `forge` and `reaper` in the loop.

- [ ] **Step 6: Verify phase alignment across documents**

Confirm these match:
- `CLAUDE.md` agent table has 6 agents with Surveyor between Forge and Reaper
- `workflow.md` has Phase 3b (Surveyor) between Phase 3 (Forge) and Phase 4 (Reaper)
- `run-program.sh` runs Surveyor after Forge and before external review in Phase 3 block
- `run-program.sh` 70% loop runs Forge → Surveyor → Reaper → Anvil
