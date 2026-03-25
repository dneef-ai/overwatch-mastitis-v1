#!/usr/bin/env python3
"""
AlphaFold Structure Analysis for Surveyor Phase 3b
Downloads pre-computed structures from AlphaFold DB for Category C targets.
Analyzes confidence scores and druggability features.
"""

import json
import os
import requests
from pathlib import Path

BASE_DIR = Path("/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo")
STRUCT_DIR = BASE_DIR / "structures"
RESULTS_DIR = BASE_DIR / "results"
CACHE_DIR = BASE_DIR / "cache"

STRUCT_DIR.mkdir(parents=True, exist_ok=True)

# Load resolution results
with open(RESULTS_DIR / "target_resolution_results.json") as f:
    resolution = json.load(f)

# Category C targets (Novel) that need full workup including structure
CATEGORY_C_TARGETS = ["2B", "3D", "5B"]  # FnBP decoy, AdsA inhibitor, ClpP/ADEP
# Also check all other resolved targets for completeness

def download_alphafold_structure(uniprot_id, gene_name):
    """Download AlphaFold PDB and confidence data."""
    pdb_url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"
    pdb_path = STRUCT_DIR / f"AF-{uniprot_id}-{gene_name}.pdb"

    if pdb_path.exists():
        print(f"  [CACHED] {pdb_path.name}")
        return str(pdb_path)

    try:
        resp = requests.get(pdb_url, timeout=30)
        if resp.status_code == 200:
            with open(pdb_path, "w") as f:
                f.write(resp.text)
            print(f"  [DOWNLOADED] {pdb_path.name}")
            return str(pdb_path)
        else:
            print(f"  [FAILED] Could not download {pdb_url} (status {resp.status_code})")
            return None
    except Exception as e:
        print(f"  [ERROR] {e}")
        return None


def analyze_pdb_confidence(pdb_path):
    """Parse a PDB file and extract pLDDT (B-factor) statistics."""
    if not pdb_path or not os.path.exists(pdb_path):
        return None

    bfactors = []
    residues_seen = set()

    with open(pdb_path) as f:
        for line in f:
            if line.startswith("ATOM") and line[12:16].strip() == "CA":  # alpha carbons only
                res_num = line[22:26].strip()
                if res_num not in residues_seen:
                    residues_seen.add(res_num)
                    try:
                        bfactor = float(line[60:66].strip())
                        bfactors.append(bfactor)
                    except ValueError:
                        pass

    if not bfactors:
        return None

    n = len(bfactors)
    mean_plddt = sum(bfactors) / n
    very_high = sum(1 for b in bfactors if b > 90) / n * 100
    confident = sum(1 for b in bfactors if b > 70) / n * 100
    low = sum(1 for b in bfactors if b < 50) / n * 100

    return {
        "num_residues": n,
        "mean_plddt": round(mean_plddt, 1),
        "pct_very_high_confidence": round(very_high, 1),  # >90
        "pct_confident": round(confident, 1),  # >70
        "pct_low_confidence": round(low, 1),   # <50
        "min_plddt": round(min(bfactors), 1),
        "max_plddt": round(max(bfactors), 1),
    }


def main():
    print("=" * 80)
    print("SURVEYOR ALPHAFOLD STRUCTURE ANALYSIS — Phase 3b")
    print("Date: 2026-03-25")
    print("=" * 80)

    structure_results = {}

    for cand_id, res in resolution.items():
        target = res["target"]
        up = res.get("uniprot")
        af = res.get("alphafold")

        if not up or not af or not af.get("available"):
            print(f"\n  SKIP {cand_id} — no AlphaFold structure available")
            continue

        uniprot_id = up["accession"]
        gene_name = target["gene"]

        print(f"\n{'='*60}")
        print(f"Structure: {cand_id} — {target['name']} ({uniprot_id})")
        print(f"{'='*60}")

        # Download PDB
        pdb_path = download_alphafold_structure(uniprot_id, gene_name)

        # Analyze confidence
        confidence = analyze_pdb_confidence(pdb_path)

        is_category_c = cand_id in CATEGORY_C_TARGETS

        structure_results[cand_id] = {
            "gene": gene_name,
            "accession": uniprot_id,
            "category_c": is_category_c,
            "pdb_path": pdb_path,
            "confidence": confidence,
            "alphafold_version": af.get("version", "unknown"),
        }

        if confidence:
            print(f"  pLDDT: mean={confidence['mean_plddt']}, "
                  f">{90}: {confidence['pct_very_high_confidence']}%, "
                  f"<{50}: {confidence['pct_low_confidence']}%")

    # Save
    output_path = RESULTS_DIR / "alphafold_structure_results.json"
    with open(output_path, "w") as f:
        json.dump(structure_results, f, indent=2)

    print(f"\n\nResults saved to: {output_path}")

    # Summary
    print("\n" + "=" * 80)
    print("STRUCTURE SUMMARY")
    print("=" * 80)
    for cand_id, res in structure_results.items():
        conf = res.get("confidence")
        cat_c = " [CATEGORY C]" if res.get("category_c") else ""
        if conf:
            print(f"  {cand_id} ({res['gene']}){cat_c}: pLDDT mean={conf['mean_plddt']}, "
                  f"residues={conf['num_residues']}, "
                  f"very_high={conf['pct_very_high_confidence']}%, "
                  f"low={conf['pct_low_confidence']}%")
        else:
            print(f"  {cand_id} ({res['gene']}){cat_c}: No confidence data")


if __name__ == "__main__":
    main()
