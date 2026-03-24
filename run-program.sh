#!/usr/bin/env bash
# run-program.sh — Run the full 6-agent, 5-phase drug discovery workflow for a program
#
# Usage: ./run-program.sh <program-name> [--phase N] [--skip-external]
#
# Example: ./run-program.sh mastitis
#          ./run-program.sh mastitis --phase 3    (start from phase 3)

set -euo pipefail

# ─── Paths ────────────────────────────────────────────────────────────────────
OVERWATCH_ROOT="$(cd "$(dirname "$0")" && pwd)"
AGENTS_DIR="$OVERWATCH_ROOT/agents"
TOOLS_DIR="$OVERWATCH_ROOT/tools"
DOCS_DIR="$OVERWATCH_ROOT/docs"

# ─── Parse Arguments ──────────────────────────────────────────────────────────
PROGRAM=""
START_PHASE=1
SKIP_EXTERNAL=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --phase) START_PHASE="$2"; shift 2 ;;
    --skip-external) SKIP_EXTERNAL=true; shift ;;
    -h|--help)
      echo "Usage: run-program.sh <program-name> [--phase N] [--skip-external]"
      echo "  <program-name>    Directory name under programs/ (e.g., mastitis)"
      echo "  --phase N         Start from phase N (default: 1)"
      echo "  --skip-external   Skip API external review (still prompts for web review)"
      exit 0
      ;;
    *)
      if [[ -z "$PROGRAM" ]]; then
        PROGRAM="$1"; shift
      else
        echo "Unknown argument: $1" >&2; exit 1
      fi
      ;;
  esac
done

if [[ -z "$PROGRAM" ]]; then
  echo "Error: program name required. Usage: ./run-program.sh <program-name>" >&2
  exit 1
fi

PROGRAM_DIR="$OVERWATCH_ROOT/programs/$PROGRAM"
mkdir -p "$PROGRAM_DIR/deliverables"

# ─── Argus Reference Paths (for prior work) ──────────────────────────────────
ARGUS_ROOT="/Users/danielneef/Projects/Argus"

# ─── Helper Functions ─────────────────────────────────────────────────────────

run_agent() {
  local agent_name=$1
  local phase_num=$2
  local agent_prompt="$AGENTS_DIR/${agent_name}.md"

  echo ""
  echo "══════════════════════════════════════════════════════════════"
  echo "  $agent_name — Phase $phase_num | Program: $PROGRAM"
  echo "══════════════════════════════════════════════════════════════"

  if [[ ! -f "$agent_prompt" ]]; then
    echo "FATAL: Agent prompt not found: $agent_prompt" >&2
    exit 1
  fi

  # Build the prompt: agent identity + program context
  local tmpfile
  tmpfile=$(mktemp)

  {
    cat "$agent_prompt"
    echo ""
    echo "---"
    echo ""
    echo "## Program Context"
    echo ""
    echo "**Program:** $PROGRAM"
    echo "**Program directory:** $PROGRAM_DIR"
    echo "**Argus prior work:** $ARGUS_ROOT"
    echo ""
    echo "## Quality Standards"
    echo ""
    echo "Read the full standards at: $DOCS_DIR/quality-standards.md"
    echo ""
    echo "## Principles"
    echo ""
    cat "$DOCS_DIR/principles.md"
  } > "$tmpfile"

  # Run as full Claude Code process with access to program dir, Argus, and tools
  (
    cd "$PROGRAM_DIR"
    claude -p \
      --model opus \
      --permission-mode bypassPermissions \
      --add-dir "$OVERWATCH_ROOT" "$ARGUS_ROOT" \
      < "$tmpfile" \
      2>&1
  ) | tee "$PROGRAM_DIR/${agent_name}-phase-${phase_num}.log"

  rm -f "$tmpfile"

  echo "$agent_name phase $phase_num complete."
}

run_external_review() {
  local phase_num=$1
  local document=$2

  echo ""
  echo "──────────────────────────────────────────────────────────────"
  echo "  EXTERNAL REVIEW — Phase $phase_num (GPT-5.4 + Gemini 3.1 Pro)"
  echo "──────────────────────────────────────────────────────────────"

  if [[ "$SKIP_EXTERNAL" == "true" ]]; then
    echo "Skipping API external review (--skip-external flag)"
  else
    if [[ -f "$PROGRAM_DIR/$document" ]]; then
      local review_output="$PROGRAM_DIR/external-review-phase-${phase_num}.md"
      python3 "$TOOLS_DIR/cross-check.py" \
        --adversarial "$PROGRAM_DIR/$document" \
        --tier premium \
        --system-prompt-file "$TOOLS_DIR/external-review-prompt.txt" \
        --output "$review_output" \
        2>&1 || echo "WARNING: API external review failed."
      echo "API review saved: $review_output"
    else
      echo "WARNING: Document not found: $PROGRAM_DIR/$document"
    fi
  fi

  # Always prompt for web review
  echo ""
  echo "╔══════════════════════════════════════════════════════════════╗"
  echo "║  WEB REVIEW CHECKPOINT                                      ║"
  echo "╠══════════════════════════════════════════════════════════════╣"
  echo "║  For best results, also submit to web versions:             ║"
  echo "║                                                              ║"
  echo "║  1. Claude Web    — best at fact-checking specific claims    ║"
  echo "║  2. GPT-5.4 Web   — best at nuanced judgment               ║"
  echo "║  3. Gemini Extended — most comprehensive technical review    ║"
  echo "║                                                              ║"
  echo "║  Document: $document"
  echo "║  Path: $PROGRAM_DIR/$document"
  echo "║                                                              ║"
  echo "║  Paste web model responses into:                             ║"
  echo "║  $PROGRAM_DIR/web-review-phase-${phase_num}.md"
  echo "║                                                              ║"
  echo "║  Press ENTER to continue (or wait if submitting to web)...   ║"
  echo "╚══════════════════════════════════════════════════════════════╝"
  read -r
}

check_70_percent() {
  echo ""
  echo "══════════════════════════════════════════════════════════════"
  echo "  70% PATHOLOGY COVERAGE TEST"
  echo "══════════════════════════════════════════════════════════════"

  if [[ ! -f "$PROGRAM_DIR/phase-5-coverage-map.md" ]]; then
    echo "FATAL: Coverage map not found. Anvil must write phase-5-coverage-map.md" >&2
    exit 1
  fi

  # Check if Anvil's coverage map indicates pass or fail
  if grep -qi "FAIL\|<70%\|below 70\|insufficient\|does not pass" "$PROGRAM_DIR/phase-5-coverage-map.md"; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║  70% TEST FAILED — Portfolio has insufficient coverage      ║"
    echo "╠══════════════════════════════════════════════════════════════╣"
    echo "║  Sending back to Forge for uncovered disease stages.        ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    return 1
  else
    echo "70% test: PASSED"
    return 0
  fi
}

check_af3_requests() {
  local af3_dir="$PROGRAM_DIR/bioinfo/af3_requests"
  if [[ -d "$af3_dir" ]] && [[ -n "$(ls -A "$af3_dir" 2>/dev/null)" ]]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║  AF3 SUBMISSION CHECKPOINT                                   ║"
    echo "╠══════════════════════════════════════════════════════════════╣"
    echo "║  Surveyor has requested AlphaFold3 structure predictions.    ║"
    echo "║                                                              ║"
    echo "║  Submission requests in: bioinfo/af3_requests/               ║"
    echo "║  Download results to:    bioinfo/structures/                 ║"
    echo "║                                                              ║"
    echo "║  For each request file:                                      ║"
    echo "║  1. Go to alphafoldserver.com                                ║"
    echo "║  2. Submit the sequence with specified co-factors            ║"
    echo "║  3. Download results                                         ║"
    echo "║                                                              ║"
    echo "║  Press ENTER when done (or to skip for now)...               ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    read -r
  fi
}

# ─── Main Workflow ────────────────────────────────────────────────────────────

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║       OVERWATCH — Drug Discovery Workflow                    ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║  Program: $PROGRAM"
echo "║  Starting phase: $START_PHASE"
echo "║  Program dir: $PROGRAM_DIR"
echo "╚══════════════════════════════════════════════════════════════╝"

# Phase 1: Disease Map (Pathfinder)
if (( START_PHASE <= 1 )); then
  run_agent "pathfinder" 1
fi

# Phase 2: Treatment Failure Analysis (Sapper)
if (( START_PHASE <= 2 )); then
  run_agent "sapper" 2
fi

# Phase 3: Propose Solutions (Forge) + Computational Validation (Surveyor)
if (( START_PHASE <= 3 )); then
  run_agent "forge" 3
  run_agent "surveyor" "3b"
  check_af3_requests
  run_external_review 3 "phase-3-candidates.md"
fi

# Phase 4: Red Team (Reaper)
if (( START_PHASE <= 4 )); then
  run_agent "reaper" 4
fi

# Phase 5: Portfolio + 70% Test + Deliverables (Anvil)
if (( START_PHASE <= 5 )); then
  run_agent "anvil" 5

  # 70% test loop
  MAX_LOOPS=3
  LOOP=0
  while ! check_70_percent; do
    LOOP=$((LOOP + 1))
    if (( LOOP >= MAX_LOOPS )); then
      echo "FATAL: 70% test failed after $MAX_LOOPS iterations. Stopping for human review." >&2
      exit 1
    fi
    echo "Loop $LOOP: Sending back to Forge for uncovered stages..."
    run_agent "forge" "5-revision-$LOOP"
    run_agent "surveyor" "5-revision-$LOOP"
    check_af3_requests
    run_agent "reaper" "5-revision-$LOOP"
    run_agent "anvil" "5-revision-$LOOP"
  done

  run_external_review 5 "phase-5-decision-memo.md"
fi

# ─── Complete ─────────────────────────────────────────────────────────────────

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    WORKFLOW COMPLETE                         ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║  Program: $PROGRAM"
echo "║  Deliverables in: $PROGRAM_DIR/deliverables/"
echo "║                                                              ║"
echo "║  Review the output before any partner presentation.          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
