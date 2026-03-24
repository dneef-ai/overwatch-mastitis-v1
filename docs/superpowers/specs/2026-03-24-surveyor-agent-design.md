# Surveyor Agent — Design Spec

## Summary

Surveyor is the sixth agent in the Overwatch drug discovery pipeline. It sits between Forge (Phase 3) and Reaper (Phase 4), computationally validating every candidate target before the red team attacks it. Its job is to answer: **"Is this target real, unique, conserved, and structurally plausible?"**

Surveyor does not make kill decisions. It provides genomic, structural, and annotation data so that Reaper's kill tests are grounded in evidence rather than literature extrapolation.

## Pipeline Position

```
Pathfinder → Sapper → Forge → Surveyor → Reaper → Anvil
(Phase 1)    (Phase 2) (Phase 3)  (3b)     (Phase 4)  (Phase 5)
```

Surveyor runs as part of the Phase 3 block in `run-program.sh`, after Forge and before external review. This avoids renumbering existing phases or output files. The `--phase` flag remains integer-based: `--phase 3` runs Forge + Surveyor + external review; `--phase 4` starts from Reaper (which now has Surveyor's output available).

- **Input:** `phase-3-candidates.md` (Forge's output)
- **Output:** `phase-3b-survey-report.md`
- **Reaper reads:** both `phase-3-candidates.md` and `phase-3b-survey-report.md`

## Step 0: Target Resolution

Forge's output uses natural-language target descriptions (e.g., "inhibit ClpP protease in S. aureus") without protein accession numbers. Before running any analysis, Surveyor's first step is to **resolve every candidate to specific identifiers**:

1. Parse each candidate's target/mechanism from `phase-3-candidates.md`
2. Query NCBI Entrez and UniProt to find the specific gene name, protein accession (UniProt ID or RefSeq), organism taxonomy ID, and amino acid sequence
3. If the target cannot be resolved to a specific protein (e.g., it targets a pathway or a non-protein mechanism), note this and skip BLAST/structure analyses — assess only what's computationally tractable
4. Write resolved identifiers into the per-candidate assessment so all downstream work references specific accessions

This resolution step also serves as a **sequence availability gate** — if the target protein doesn't exist in public databases, that's immediately informative and gets flagged.

## Tiered Analysis

### Category A/B Candidates (Known / Non-Obvious) — Reality Check

These candidates have literature support. Surveyor's job is to verify the biological claims computationally:

1. **Conservation analysis** — BLAST the target gene/protein across field-relevant pathogen isolates. Confirm the target is conserved across the strains that matter (e.g., CC97/CC151/CC479 for S. aureus mastitis; subsp. necrophorum vs funduliforme for F. necrophorum). Report % identity and coverage for each strain checked. Maps to Quality Standard 16 (strain heterogeneity). Thresholds: <80% identity = "divergent"; absent from >20% of field strains = "conservation concern."

2. **Host selectivity** — BLAST the target against the host proteome (bovine, salmon, etc.). Flag any homolog with >50% identity at >50% query coverage. Report the specific ortholog, its function, and the selectivity risk. Maps to Quality Standard 14 (host selectivity assessed).

3. **Annotation verification** — Query UniProt/NCBI Entrez to confirm or correct the candidate's claimed properties: localization (surface, secreted, intracellular, membrane), function, essentiality, and known post-translational modifications. If Forge claims a protein is surface-exposed, Surveyor checks it.

### Category C Candidates (Novel) — Full Workup

Novel proposals from first principles get everything above, plus:

4. **Structure prediction** — Two-tier approach:
   - **Tier 1 (automated):** Check the AlphaFold Protein Structure Database (alphafold.ebi.ac.uk) for pre-computed structures. Many bacterial proteins already have AF2 predictions available via API. If found, download and assess.
   - **Tier 2 (human-in-the-loop):** For targets without pre-computed structures, or where co-folding with metals/ligands/partners is needed, Surveyor writes an AF3 submission request: the exact sequence, job name, co-factor specifications, and rationale. It then **pauses and prompts Daniel** to submit the job at alphafoldserver.com and provide the results back. This mirrors the existing web review checkpoint pattern. Surveyor resumes analysis once the structure is available.
   - Assess: does the predicted structure have a druggable pocket or exposed functional site? Report pLDDT/pTM confidence scores.

5. **Operon / gene neighborhood analysis** — Query NCBI for the genomic context. Is this gene part of a virulence island? Pathogenicity island? Co-regulated with other virulence factors? In an operon with essential genes? This context determines whether the target is likely essential for pathogenesis or peripheral.

6. **Signal peptide / transmembrane prediction** — Confirm the protein's accessibility. A drug target inside the cytoplasm has different delivery requirements than one on the surface. Verify Forge's assumptions about accessibility. Use SignalP-style analysis via sequence features and UniProt annotations.

## Output Format

### Per-Candidate Assessment

For each candidate in `phase-3-candidates.md`, Surveyor writes:

```markdown
### [Candidate Name] — [Category A/B/C]

**Resolved Identity:**
- Gene: [gene name] | Protein: [UniProt/RefSeq accession]
- Organism: [species, taxonomy ID]
- Sequence length: [N aa]
- Resolution notes: [any issues finding the protein, or "N/A — non-protein target"]

**Conservation:**
- [Organism] field isolates checked: [list strains]
- Identity range: [X-Y%] across [N] strains
- Notable gaps: [any strains where gene is absent or <80% identity]
- Evidence: [COMPUTATIONAL — BLASTP against nr, date, e-value threshold, database]

**Host Selectivity:**
- Closest host ortholog: [protein name, UniProt ID]
- Identity: [X%] at [Y%] query coverage
- Risk: [LOW (<30%) / MODERATE (30-50%) / HIGH (>50%)]
- Evidence: [COMPUTATIONAL — BLASTP against host proteome]

**Annotation Check:**
- Claimed localization: [what Forge said] → Verified: [what UniProt/Entrez shows]
- Claimed function: [what Forge said] → Verified: [what annotation shows]
- Essentiality: [essential / conditionally essential / dispensable / unknown]
- Evidence: [UniProt ID, NCBI Gene ID]

**Structure (Category C only):**
- Source: [AlphaFold DB / AF3 submission / not available]
- Confidence: [pLDDT mean, pTM if AF3]
- Druggable pocket: [YES — location and approximate volume / NO / UNCLEAR]
- Notable features: [metal binding sites, disordered regions, domain architecture]
- Evidence: [COMPUTATIONAL — structure files in programs/<name>/bioinfo/structures/]
- [If AF3 needed: "AF3 SUBMISSION REQUESTED — see bioinfo/af3_requests/[target].md"]

**Operon Context (Category C only):**
- Gene neighborhood: [upstream and downstream genes, operon membership]
- Virulence island: [YES — which island / NO]
- Regulation: [known regulators, co-expression data if available]
- Evidence: [NCBI Gene ID, genome coordinates]

**Accessibility (Category C only):**
- Signal peptide: [YES — Sec/Tat pathway / NO]
- Transmembrane domains: [count and topology]
- Predicted localization: [cytoplasmic / membrane / surface / secreted]
- Evidence: [COMPUTATIONAL — UniProt annotation + sequence features]

**Verdict:** [CONFIRMED / CORRECTED / FLAGGED]
- [One-line summary of what was found]
- [If CORRECTED: what was wrong and what's true]
- [If FLAGGED: the specific problem]

**Wet-lab confirmation type:**
- [Type of experiment that would confirm or refute the key computational finding]
- [e.g., "Surface localization → flow cytometry with anti-[protein] antibody"]
- [Scope: experiment TYPE only. Full design, thresholds, and budgets are Anvil's job.]
```

### Summary Table

At the top of `phase-3b-survey-report.md`, a summary table:

| Candidate | Category | Accession | Conservation | Host Selectivity | Annotation | Structure | Verdict |
|-----------|----------|-----------|-------------|-----------------|------------|-----------|---------|
| [name] | A/B/C | [ID] | [X-Y% / N strains] | [risk level] | [confirmed/corrected] | [pocket Y/N or N/A] | CONFIRMED/CORRECTED/FLAGGED |

## Tool Stack

### Required (pre-installed or API-accessible)

| Tool | Purpose | Access Method |
|------|---------|---------------|
| NCBI BLAST | Conservation, host homology | BioPython `NCBIWWW` (remote API, requires NCBI API key) |
| UniProt | Protein annotation, function | REST API (api.uniprot.org) |
| NCBI Entrez | Gene info, operon context, genome neighborhood | BioPython `Entrez` (requires API key for >3 req/s) |
| AlphaFold DB | Pre-computed structure lookup | REST API (alphafold.ebi.ac.uk) |
| AlphaFold3 Server | De novo structure prediction (Cat C) | Human-in-the-loop (Daniel submits at alphafoldserver.com) |
| BioPython | Sequence/structure parsing | Python library (pip install) |

### NCBI API Key and Rate Limiting

NCBI enforces rate limits: 3 requests/second without an API key, 10/second with one. Surveyor MUST:
- Use an NCBI API key (set via `Entrez.api_key` in BioPython)
- Stagger BLAST submissions (remote BLAST can take 5-30 minutes per query)
- Cache all BLAST results in `bioinfo/cache/` keyed by query sequence hash — never re-run a query that's already cached
- For parallel subagents: coordinate via the shared cache directory; each subagent checks cache before submitting

### AlphaFold3 — Human-in-the-Loop Workflow

AF3 Server has no public API. For Category C targets needing structure prediction:

1. Surveyor writes a submission request to `bioinfo/af3_requests/[target].md` containing:
   - Protein sequence (FASTA)
   - Job name
   - Co-factors/ions to include (if any)
   - Rationale for why this target needs a structure
2. Surveyor completes all other analyses (BLAST, annotation, operon) while waiting
3. Surveyor's report marks the structure field as "AF3 SUBMISSION REQUESTED"
4. Overwatch prompts Daniel to submit the AF3 jobs (same pattern as the web review checkpoint)
5. When Daniel provides results, Overwatch can re-run Surveyor with `--resume-af3` to complete the structure assessment, or the results can be integrated manually before Reaper runs

This mirrors how Argus handled AF3 — see `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/` for the reference implementation.

### Not In Scope

| Tool | Why Not |
|------|---------|
| Smina/Meeko/RDKit docking | Premature — docking is for lead optimization after target selection |
| Virtual screening | Same — comes after Daniel selects a target to pursue |
| Molecular dynamics | Too expensive computationally for triage |
| ESMFold | Hosted API (esmatlas.com) shut down late 2024; local requires GPU. Use AlphaFold DB for pre-computed structures instead |

## Constraints

### Quality Standard 8: Computational Evidence Is Triage

All Surveyor output is tagged `[COMPUTATIONAL]`. Surveyor explicitly states what wet-lab experiment type would confirm or refute each finding. Computational evidence alone cannot promote or kill a target — it triages for experimental validation.

### No Kill Decisions

Surveyor provides data. Reaper makes kill decisions. If Surveyor finds a host homolog at 60% identity, it reports "FLAGGED — high host selectivity risk" but does NOT say "kill this candidate." Reaper takes that data and applies Kill Test 14 (host selectivity).

### No Literature Review

Surveyor does not search PubMed or review papers. That's Forge's job (proposing) and Reaper's job (attacking). Surveyor runs computational analyses against databases and structure prediction servers.

### Wet-Lab Scope Boundary

The "Wet-lab confirmation type" field proposes the *type* of experiment needed (e.g., "flow cytometry for surface localization," "Western blot for expression confirmation"). It does NOT design the full experiment, set GO/KILL thresholds, or estimate costs. Full experiment design with budgets and binary gates is Anvil's job (Phase 5).

### Subagent Usage

Surveyor has unlimited subagent budget. For a candidates list with 15 targets, it should launch parallel agents for independent analyses. However:

- **BLAST subagents** must check the shared `bioinfo/cache/` directory before submitting queries to avoid duplicate API calls
- **Rate limiting:** no more than 10 concurrent NCBI API requests (with API key). Subagents should stagger BLAST submissions
- **Consolidation:** each subagent writes its per-target results to `bioinfo/results/[target-name].md`. The main Surveyor process reads all result files and compiles the final `phase-3b-survey-report.md`
- **Expected scale:** ~2-4 subagents per candidate (BLAST conservation, BLAST host, annotation, operon). For 15 candidates, expect ~30-60 subagents total, staggered by API availability

## File Structure

Surveyor creates a `bioinfo/` directory in the program folder:

```
programs/<name>/
├── phase-3-candidates.md          (input from Forge)
├── phase-3b-survey-report.md      (Surveyor's output)
├── bioinfo/
│   ├── scripts/                   (Python scripts Surveyor writes and runs)
│   ├── sequences/                 (FASTA files, BLAST XML results)
│   ├── structures/                (AlphaFold DB PDB, AF3 CIF/PDB when available)
│   ├── af3_requests/              (AF3 submission requests for Daniel)
│   ├── results/                   (per-target analysis markdown)
│   └── cache/                     (BLAST result cache, keyed by sequence hash)
```

This directory persists for future use — if Daniel later wants to bring in docking for a selected target, the structures and sequences are already there. The Argus bioinfo directory at `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/` serves as a reference implementation for directory conventions and script patterns.

## Integration With Overwatch

### No Separate External Validation for Surveyor

External validation (cross-check.py + web review) happens after Phase 3 as it does now. Surveyor runs before external review, so the external models benefit from having computationally-grounded candidates. The survey report itself does not need separate external review — it's computational data, not scientific claims.

### Before Surveyor Runs
Overwatch checks Forge's output: does every disease stage have at least one candidate? If not, send Forge back before invoking Surveyor.

### After Surveyor Runs
Overwatch reads `phase-3b-survey-report.md` and checks:
- Did Surveyor assess every candidate? (no skips)
- Did it actually run BLAST or just describe what BLAST would show? Are BLAST parameters reported (database, e-value threshold)?
- If a Category C target has no structure prediction, is there a valid reason (e.g., AF3 submission pending)?
- Are there any FLAGGED verdicts that Forge should address before Reaper? (e.g., a novel target with no druggable pocket — Forge might want to propose an alternative mechanism)
- If AF3 submissions are pending, prompt Daniel for the AF3 checkpoint before proceeding to Reaper

### In the 70% Loop
If Anvil fails the 70% test and Forge proposes new candidates, those new candidates go through Surveyor before reaching Reaper. The loop becomes: Forge (gaps) → Surveyor → Reaper → Anvil (re-test).

## Changes to Existing Components

### CLAUDE.md

Add Surveyor to the agent table:

```markdown
| **Surveyor** | Computationally validate targets | Forge candidates | `phase-3b-survey-report.md` |
```

Update pipeline description and add to "After Each Agent" section:

```markdown
- For Surveyor: did every candidate get a verdict? Did it actually run BLAST or just describe what BLAST would show? Are BLAST parameters reported? If a Category C target has no structure, why not? Are there AF3 submissions pending?
```

Add to manual mode instructions:

```markdown
3b. "Run Surveyor" → launch Surveyor, review computational findings, discuss flagged items with Daniel. If AF3 submissions needed, pause for Daniel to submit and return results.
```

### workflow.md

Add Phase 3b between Phase 3 and Phase 4. Note that Surveyor runs within the Phase 3 block (after Forge, before external review) and does not change phase numbering.

### run-program.sh

In the Phase 3 block, add Surveyor invocation between Forge and external review:

```bash
# Phase 3: Propose Solutions (Forge) + Computational Validation (Surveyor)
if (( START_PHASE <= 3 )); then
  run_agent "forge" 3
  run_agent "surveyor" "3b"
  # AF3 checkpoint (if Category C targets need structure prediction)
  # ... prompt Daniel for AF3 submissions if af3_requests/ is non-empty ...
  run_external_review 3 "phase-3-candidates.md"
fi
```

In the 70% loop, add Surveyor between Forge and Reaper:

```bash
run_agent "forge" "5-revision-$LOOP"
run_agent "surveyor" "5-revision-$LOOP"
run_agent "reaper" "5-revision-$LOOP"
run_agent "anvil" "5-revision-$LOOP"
```

### agents/surveyor.md (NEW)

The agent prompt file. Written during implementation.

### agents/reaper.md

Add `phase-3b-survey-report.md` to the "Also read" list:

```markdown
Also read:
- `phase-1-disease-map.md` — to check if candidates actually address what they claim
- `phase-2-failure-analysis.md` — to check if candidates repeat known failure modes
- `phase-3b-survey-report.md` — computational validation of targets (conservation, host homology, structure, annotation). Use this data to ground Kill Tests 2 (species), 4 (strain), 5 (resistance), and the host selectivity check.
```

### agents/anvil.md

Add `phase-3b-survey-report.md` to the "Read ALL prior documents" list. Note that Surveyor's structure predictions, conservation data, and annotation corrections should inform de-risk experiment design and the evidence register.
