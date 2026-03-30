# Cross-Model AI Review: Setup & Integration Guide

**For the Agteria team — how our 6-model external review panel works, why it matters, and how to set it up yourself.**

*Daniel Neef, March 2026*

---

## Why Cross-Model Review?

No single AI model should fact-check itself. Every frontier model has blind spots — different training data, different reasoning patterns, different failure modes. We discovered this firsthand during the mastitis v12 review:

- **GPT-5.4** caught that our FnBP conservation analysis was answering the wrong question (sequence conservation ≠ prevalence in bovine mastitis) — a blind spot Claude completely missed
- **Gemini 3.1 Pro** identified Specialized Pro-resolving Mediators (SPMs) as a missed tissue repair target that no other model surfaced
- **Grok 4** caught metabolic pathway errors in the liver abscess analysis that appeared in no other review

When we ran the FnBP gate analysis, GPT-5.4's challenge led us to kill a target **in one day** instead of spending months and money on it. The gate process worked because we didn't trust a single model's assessment.

**Bottom line:** Cross-model review consistently finds 3-5 decision-changing findings per document that the authoring model missed entirely.

---

## The System at a Glance

### What It Does

Takes any scientific document (review, analysis, pipeline output) and sends it to multiple frontier AI models simultaneously. Each model independently evaluates the work using a structured prompt. Results are compiled into a single markdown file with model-by-model sections.

### The 6-Model Panel

| Model | Via | Strengths |
|-------|-----|-----------|
| **Gemini 3.1 Pro** | OpenRouter | Deep biological mechanism, commercially provocative |
| **GPT-5.4** | OpenRouter | Best experimental design critique, sharp target-vs-molecule distinction |
| **Grok 4** | OpenRouter | Metabolic pathway errors, contrarian perspectives |
| **Claude Opus 4.6** | OpenRouter | Rigorous fact-checking, catches citation drift and claim compression |
| **DeepSeek R1** | OpenRouter | Reasoning chains, mechanistic logic verification |
| **Qwen 2.5** | OpenRouter | Broad coverage, different training distribution |

### Cost

~$0.10-0.30 per review. A full Overwatch program run (6 phases × 6 models) costs under $2.

---

## Setup (5 minutes)

### Step 1: Get an OpenRouter API Key

1. Go to [openrouter.ai](https://openrouter.ai) and create an account
2. You get **$5 free credits** on signup — enough for hundreds of reviews
3. Go to Keys → Create Key → copy it

### Step 2: Set Environment Variables

Add to your `~/.zshrc` (or `~/.bashrc`):

```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# Optional — for free-tier models (not needed if using OpenRouter):
export GOOGLE_API_KEY="your-google-ai-key"    # Free Gemini Flash
export GROQ_API_KEY="your-groq-key"           # Free Llama 3.3 70B
```

Then reload: `source ~/.zshrc`

### Step 3: Get the Script

The script lives at `tools/cross-check.py` in the Overwatch repo. It's a single Python file with no dependencies beyond `requests` (and optionally `edison-client` for PaperQA3).

```bash
# From the overwatch repo root:
python3 tools/cross-check.py --help
```

### Step 4: Verify

```bash
# Quick test — check a single claim:
python3 tools/cross-check.py "Tomatidine has >2000x selectivity for SCV S. aureus over wild-type" --tier standard
```

You should see responses from 2-3 models with VERDICT / CONFIDENCE / REASONING.

---

## How to Use It

### Four Modes

#### 1. Single Claim Check

Check one scientific claim against multiple models:

```bash
python3 tools/cross-check.py "ClpP inhibition suppresses >14 virulence factors in S. aureus" --tier full
```

#### 2. Batch Claim File

Check a list of claims (one per line in a text file):

```bash
python3 tools/cross-check.py --file claims.txt --tier standard
```

#### 3. Auto-Extract + Verify

Give it a full document — it extracts 15-20 key claims automatically, then checks each against the panel:

```bash
python3 tools/cross-check.py --review my-analysis.md --tier premium
```

#### 4. Full Adversarial Review (most powerful)

Send an entire document to each model for independent structured review:

```bash
python3 tools/cross-check.py --adversarial my-analysis.md \
  --tier full \
  --output my-analysis-external-review.md
```

This is the mode used in the Overwatch pipeline. Each model returns:
1. **FACTUAL ERRORS** — would change a recommendation
2. **CRITICAL MISSING EVIDENCE** — would add or kill a target
3. **LOGIC ERRORS** — conclusion doesn't follow from evidence
4. **OVERLOOKED ALTERNATIVES** — approaches with real evidence not in the analysis
5. **WHAT THE ANALYSIS GETS RIGHT** — 3-5 strongest claims
6. **VERDICT** — reliable enough to act on?

Every finding must pass the **"so what?" test** — it must name the specific decision that would change.

### Model Tiers

| Tier | Models | Cost | When to Use |
|------|--------|------|-------------|
| `free` | Gemini Flash + Llama 3.3 + OpenRouter free | $0 | Quick sanity checks |
| `standard` | Gemini Pro + GPT-5.4 + Llama | ~$0.05 | Routine review |
| `premium` | Gemini Pro + GPT-5.4 + Edison (PaperQA3) | ~$0.15 | Key documents |
| `full` | All 6 frontier models | ~$0.20 | Pipeline phases, critical decisions |
| `board` | All 6 + Edison (PaperQA3) | ~$0.30 | Board-level strategic decisions |

**Default recommendation:** Use `--tier standard` for routine work, `--tier full` for anything that drives a target selection or kill decision.

### Custom Prompts

You can override the default adversarial prompt with a domain-specific one:

```bash
python3 tools/cross-check.py --adversarial document.md \
  --tier full \
  --system-prompt-file my-custom-prompt.txt
```

The repo includes two built-in prompts:
- `tools/external-review-prompt.txt` — general scientific review (adds "Overlooked Alternatives" section)
- `tools/phase-prompts.txt` — phase-specific generative prompts for the Overwatch pipeline (Pathfinder, Sapper, Forge, Reaper, Anvil)

---

## How It's Used in Overwatch

In the Overwatch pipeline, the 6-model panel runs at **every phase** — not as a final check, but as a generative contributor throughout:

```
Pathfinder (disease map)
    └── 6 models contribute: missing mechanisms, R0, rate-limiting step
Tribunal (bottleneck consensus)
    └── informed by panel's disease insights
Sapper (failure analysis)
    └── 6 models contribute: missed failures, target-vs-compound distinction
Forge (candidates) + Vulcan (quarantined first-principles)
    └── 6 models contribute: empirical hits, proposed targets, analogies
Surveyor (computational validation)
    └── no panel (computational only)
Reaper (adversarial kill)
    └── 6 models challenge: wrong kills, wrong survivals, single-lab flags
Board (strategic decision)
    └── 6 models contribute: coverage honesty, top-3 experiments, commercial reality
Anvil (portfolio + 70% test)
    └── 6 models validate: coverage estimates, portfolio gaps
```

**Key principle:** Each agent receives BOTH the previous phase output AND the 6-model panel responses. The panel contributions are fed forward, not discarded.

### The Pattern

After each agent completes:

```bash
# 1. Run the panel with phase-specific generative prompt
python3 tools/cross-check.py --adversarial programs/<name>/phase-N-output.md \
  --tier full \
  --system-prompt-file tools/phase-prompts.txt \
  --output programs/<name>/external-input-phase-N.md

# 2. Feed both the phase output AND panel responses to the next agent
```

### Interpreting Panel Results

When synthesizing panel output (as the Board agent does):

- **2+ models agree on a finding** → signal worth investigating
- **4+ models agree** → near-certain, must address
- **1 model flags something unique** → may be noise, but check if it's from that model's known strength area (e.g., GPT-5.4 on experimental design)
- **All models miss something** → not evidence of absence; they share training data biases

### Real Examples of Panel Impact

**Crypto v2 (Cargill):** After Phase 4, the panel:
- Flagged CpPDE1 as single-lab dependent (5/6 models) → downgraded from SURVIVED to WOUNDED
- Challenged oocyst inactivation kill as using wrong evaluation lens (individual calf vs transmission control)
- Identified 4 wrong kills where the Reaper agent was too aggressive

**Mastitis (Zoetis):** After the Board phase:
- GPT-5.4 identified that our "zero bovine homolog for SrtA" claim was overstated
- Gemini identified SPMs/resolvins as a completely missed tissue repair target class
- The FnBP conservation analysis was challenged → led to target being killed in <24 hours

**Liver Abscess v2 (Elanco):** Tribunal bottleneck consensus (4/4 agents + panel) confirmed Gate 2 (leukotoxin immune evasion) as the bottleneck, shifting the entire portfolio from feed-additive-centered to drug-target-centered.

---

## How to Integrate Into Your Workflow

### For Jarvis (Martin / Rafey)

The simplest integration point: after each Jarvis pipeline step, run the adversarial review on the output before proceeding.

```bash
# After Jarvis produces a step output:
python3 tools/cross-check.py --adversarial jarvis-step-output.md \
  --tier full \
  --output jarvis-step-external-review.md
```

Feed `jarvis-step-external-review.md` into the next Jarvis step alongside the original output.

**Martin's vision:** Jarvis → Argus → OpenRouter Board. The cross-check script IS the board — it runs the same 6 models that sit on Overwatch's Board agent panel.

### For Argus Reviews (Daniel)

Already integrated. The `--adversarial` mode with `--tier full` is how every Argus review gets cross-checked. The zoetis-mastitis-v12 review used this at every stage.

### For Any Scientific Document

The script works on any markdown document. Use cases beyond the pipeline:

- **Grant applications** — check claims before submission
- **Partner presentations** — verify all numbers and citations
- **Experiment designs** — have 6 models critique your protocol
- **Literature reviews** — check for missed papers and alternative interpretations

```bash
# Example: review a partner presentation
python3 tools/cross-check.py --adversarial elanco-presentation.md \
  --tier standard \
  --output elanco-presentation-review.md
```

### For Claude Code Users

If you're using Claude Code (as most of the team does), you can call the script directly from within a session:

```bash
# Inside Claude Code:
! python3 ~/Projects/Agteria/overwatch/tools/cross-check.py \
  --adversarial my-document.md --tier full
```

Or have Claude Code read the output and incorporate the findings into its next response.

---

## Quality Standards

The cross-model review enforces several of Overwatch's 40 quality standards:

- **QS #4 — Citation verification:** Every PMID must be checked against the actual paper
- **QS #6 — Species and model tagging:** Mouse evidence ≠ bovine evidence
- **QS #9 — Extraordinary claims require extraordinary scrutiny:** Stoichiometric test for implausible efficacy claims
- **QS #16 — Strain heterogeneity:** Must test across major lineages
- **QS #36 — Independent replication:** Single-lab data flagged for mandatory replication
- **QS #40 — Mechanism-level evaluation:** Don't kill a category when the specific mechanism is viable

---

## Troubleshooting

**"No API key found"** — Check `echo $OPENROUTER_API_KEY` in terminal. If empty, re-source your shell config.

**Timeout errors** — Some models (especially DeepSeek R1 with long reasoning chains) can take 3-5 minutes. The script has a 300s timeout for OpenRouter calls. If you're consistently timing out, try `--tier standard` first.

**Empty responses** — Usually means the model's context window was exceeded. Split very long documents (>50KB) into sections and review each separately.

**Edison errors** — Edison (PaperQA3) requires the `edison-client` pip package and an `EDISON_API_KEY`. It's optional — `premium` tier without Edison just uses Gemini Pro + GPT-5.4.

**Rate limits** — OpenRouter has generous limits for paid accounts. If you hit them, the script will show HTTP 429 errors. Wait 30 seconds and retry, or reduce parallelism by splitting into smaller batches.

---

## Architecture Summary

```
┌─────────────────────────────────────────────┐
│              cross-check.py                  │
│                                              │
│  Input: any .md document                     │
│  Output: structured multi-model review .md   │
│                                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
│  │Gemini   │  │GPT-5.4  │  │Grok 4   │     │
│  │3.1 Pro  │  │         │  │         │     │
│  └────┬────┘  └────┬────┘  └────┬────┘     │
│       │            │            │            │
│  ┌────┴────┐  ┌────┴────┐  ┌────┴────┐     │
│  │Claude   │  │DeepSeek │  │Qwen 2.5 │     │
│  │Opus 4.6 │  │R1       │  │         │     │
│  └────┬────┘  └────┬────┘  └────┬────┘     │
│       │            │            │            │
│       └────────────┼────────────┘            │
│                    │                         │
│         ┌──────────┴──────────┐              │
│         │  Compiled Output    │              │
│         │  (model-by-model)   │              │
│         └─────────────────────┘              │
│                                              │
│  All calls via OpenRouter API (~$0.20/run)   │
│  Parallel execution (ThreadPoolExecutor)     │
│  Phase-specific or custom prompts            │
└─────────────────────────────────────────────┘
```

---

## Quick Reference

```bash
# Single claim check
python3 tools/cross-check.py "your claim here" --tier standard

# Full adversarial review (recommended)
python3 tools/cross-check.py --adversarial document.md --tier full

# With custom prompt
python3 tools/cross-check.py --adversarial document.md --tier full \
  --system-prompt-file tools/external-review-prompt.txt \
  --output document-review.md

# Auto-extract and verify claims
python3 tools/cross-check.py --review document.md --tier premium
```

**Start here:** Get an OpenRouter key, set the env var, run `--adversarial` on your next analysis with `--tier standard`. You'll see the value immediately.
