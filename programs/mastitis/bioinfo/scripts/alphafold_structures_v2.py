#!/usr/bin/env python3
"""
AlphaFold Structure Analysis v2 for Surveyor Phase 3b
Uses API-provided URLs (v6) instead of hardcoded v4.
"""

import json
import os
import requests
from pathlib import Path

BASE_DIR = Path("/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo")
STRUCT_DIR = BASE_DIR / "structures"
RESULTS_DIR = BASE_DIR / "results"

STRUCT_DIR.mkdir(parents=True, exist_ok=True)

# Load resolution results
with open(RESULTS_DIR / "target_resolution_results.json") as f:
    resolution = json.load(f)

CATEGORY_C_TARGETS = ["2B", "3D", "5B"]

def get_alphafold_urls(uniprot_id):
    """Get actual download URLs from AlphaFold API."""
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list) and data:
                entry = data[0]
                return {
                    "pdb_url": entry.get("pdbUrl", ""),
                    "cif_url": entry.get("cifUrl", ""),
                    "version": entry.get("latestVersion", ""),
                }
    except Exception as e:
        print(f"  [ERROR] API: {e}")
    return None


def download_structure(url, output_path):
    """Download a file from URL."""
    if os.path.exists(output_path):
        print(f"  [CACHED] {os.path.basename(output_path)}")
        return True
    try:
        resp = requests.get(url, timeout=60)
        if resp.status_code == 200:
            with open(output_path, "w") as f:
                f.write(resp.text)
            print(f"  [DOWNLOADED] {os.path.basename(output_path)}")
            return True
        else:
            print(f"  [FAILED] HTTP {resp.status_code}: {url}")
            return False
    except Exception as e:
        print(f"  [ERROR] {e}")
        return False


def analyze_pdb_confidence(pdb_path):
    """Parse PDB for pLDDT (B-factor) statistics."""
    if not pdb_path or not os.path.exists(pdb_path):
        return None

    bfactors = []
    residues_seen = set()

    with open(pdb_path) as f:
        for line in f:
            if line.startswith("ATOM") and len(line) > 66:
                atom_name = line[12:16].strip()
                if atom_name == "CA":
                    res_key = line[17:26]  # residue name + chain + number
                    if res_key not in residues_seen:
                        residues_seen.add(res_key)
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

    # Identify low-confidence regions (potential disordered regions)
    disordered_regions = []
    in_disorder = False
    start = 0
    for i, b in enumerate(bfactors):
        if b < 50 and not in_disorder:
            in_disorder = True
            start = i + 1  # 1-indexed
        elif b >= 50 and in_disorder:
            in_disorder = False
            if (i - start + 1) >= 5:  # only report stretches >= 5 residues
                disordered_regions.append(f"{start}-{i}")
    if in_disorder and (n - start + 1) >= 5:
        disordered_regions.append(f"{start}-{n}")

    return {
        "num_residues": n,
        "mean_plddt": round(mean_plddt, 1),
        "pct_very_high_confidence": round(very_high, 1),
        "pct_confident": round(confident, 1),
        "pct_low_confidence": round(low, 1),
        "min_plddt": round(min(bfactors), 1),
        "max_plddt": round(max(bfactors), 1),
        "disordered_regions": disordered_regions if disordered_regions else ["None detected"],
    }


def main():
    print("=" * 80)
    print("SURVEYOR ALPHAFOLD STRUCTURE ANALYSIS v2 — Phase 3b")
    print("Date: 2026-03-25")
    print("=" * 80)

    structure_results = {}

    for cand_id, res in resolution.items():
        target = res["target"]
        up = res.get("uniprot")

        if not up:
            continue

        uniprot_id = up["accession"]
        gene_name = target["gene"]

        print(f"\n{'='*60}")
        print(f"Structure: {cand_id} — {target['name']} ({uniprot_id})")
        print(f"{'='*60}")

        # Get URLs from API
        urls = get_alphafold_urls(uniprot_id)
        if not urls or not urls.get("pdb_url"):
            print(f"  No AlphaFold structure available")
            structure_results[cand_id] = {
                "gene": gene_name,
                "accession": uniprot_id,
                "available": False,
            }
            continue

        # Download PDB
        pdb_path = str(STRUCT_DIR / f"AF-{uniprot_id}-{gene_name}.pdb")
        success = download_structure(urls["pdb_url"], pdb_path)

        if not success:
            structure_results[cand_id] = {
                "gene": gene_name,
                "accession": uniprot_id,
                "available": False,
            }
            continue

        # Analyze confidence
        confidence = analyze_pdb_confidence(pdb_path)

        is_category_c = cand_id in CATEGORY_C_TARGETS

        structure_results[cand_id] = {
            "gene": gene_name,
            "accession": uniprot_id,
            "available": True,
            "category_c": is_category_c,
            "pdb_path": pdb_path,
            "confidence": confidence,
            "alphafold_version": urls.get("version", "unknown"),
        }

        if confidence:
            print(f"  pLDDT: mean={confidence['mean_plddt']}, "
                  f"very_high(>90)={confidence['pct_very_high_confidence']}%, "
                  f"low(<50)={confidence['pct_low_confidence']}%")
            if confidence['disordered_regions'] != ["None detected"]:
                print(f"  Disordered regions: {', '.join(confidence['disordered_regions'])}")

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
        available = res.get("available", False)
        if available and conf:
            quality = "HIGH" if conf["mean_plddt"] > 80 else ("MODERATE" if conf["mean_plddt"] > 60 else "LOW")
            print(f"  {cand_id} ({res['gene']}){cat_c}: AVAILABLE, pLDDT={conf['mean_plddt']} ({quality}), "
                  f"{conf['num_residues']} residues")
        else:
            print(f"  {cand_id} ({res['gene']}){cat_c}: NOT AVAILABLE")


if __name__ == "__main__":
    main()
