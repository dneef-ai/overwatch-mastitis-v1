#!/usr/bin/env python3
"""
Run all BLAST queries sequentially for conservation and host selectivity.
"""

import json
import hashlib
import time
import sys
from pathlib import Path
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import Entrez
Entrez.email = "daniel@agteria.bio"

CACHE_DIR = Path("/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo/cache")
RESULTS_DIR = Path("/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo/results")

with open(RESULTS_DIR / "target_resolution_results.json") as f:
    resolution = json.load(f)


def run_blast(sequence, entrez_query, label, expect=1e-10, hitlist_size=50):
    """Run a single BLAST and return parsed hits."""
    ck = hashlib.md5(f"blast_{label}".encode()).hexdigest()
    cache_path = CACHE_DIR / f"{ck}.json"
    if cache_path.exists():
        print(f"  [CACHE HIT] {label}")
        with open(cache_path) as f:
            return json.load(f)

    print(f"  [BLAST] Submitting: {label} ({len(sequence)} aa)...")
    sys.stdout.flush()

    try:
        result_handle = NCBIWWW.qblast(
            "blastp", "nr", sequence,
            entrez_query=entrez_query,
            expect=expect,
            hitlist_size=hitlist_size,
            format_type="XML"
        )
        blast_records = NCBIXML.parse(result_handle)
        record = next(blast_records)

        hits = []
        for alignment in record.alignments:
            hsp = alignment.hsps[0]
            identity_pct = (hsp.identities / hsp.align_length) * 100
            coverage_pct = (hsp.align_length / len(sequence)) * 100
            hits.append({
                "title": alignment.title[:200],
                "accession": alignment.accession,
                "length": alignment.length,
                "identity_pct": round(identity_pct, 1),
                "coverage_pct": round(coverage_pct, 1),
                "e_value": float(hsp.expect),
                "gaps": hsp.gaps,
            })

        result = {
            "label": label,
            "query_length": len(sequence),
            "entrez_query": entrez_query,
            "num_hits": len(hits),
            "hits": hits,
            "date": "2026-03-25",
        }

        with open(cache_path, "w") as f:
            json.dump(result, f, indent=2, default=str)

        print(f"  [DONE] {len(hits)} hits")
        return result

    except Exception as e:
        print(f"  [ERROR] {label}: {e}")
        error_result = {"label": label, "error": str(e), "num_hits": 0, "hits": []}
        with open(cache_path, "w") as f:
            json.dump(error_result, f, indent=2)
        return error_result


def main():
    all_results = {}

    targets = [
        ("2A", "srtA"),
        ("2B", "fnbA"),
        ("3A", "spa"),
        ("3B", "lukM"),
        ("3D", "adsA"),
        ("4A", "hla"),
        ("5B", "clpP"),
        ("5F", "icaA"),
    ]

    for cand_id, gene in targets:
        res = resolution[cand_id]
        seq = res["uniprot"]["sequence"]

        print(f"\n{'='*60}")
        print(f"{cand_id} — {gene} ({len(seq)} aa)")
        print(f"{'='*60}")

        # Conservation: BLAST against S. aureus
        cons = run_blast(
            seq,
            "Staphylococcus aureus[Organism]",
            f"sa_{gene}",
            expect=1e-10,
            hitlist_size=50
        )

        time.sleep(3)

        # Host selectivity: BLAST against Bos taurus
        host = run_blast(
            seq,
            "Bos taurus[Organism]",
            f"bt_{gene}",
            expect=1.0,  # very permissive to catch any weak homology
            hitlist_size=10
        )

        all_results[cand_id] = {
            "gene": gene,
            "conservation": cons,
            "host_selectivity": host,
        }

        time.sleep(3)

    # Save combined results
    output_path = RESULTS_DIR / "all_blast_results.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n\n{'='*80}")
    print("BLAST RESULTS SUMMARY")
    print(f"{'='*80}")
    for cand_id, r in all_results.items():
        cons = r["conservation"]
        host = r["host_selectivity"]

        # Conservation
        if cons.get("hits"):
            ids = [h["identity_pct"] for h in cons["hits"]]
            print(f"  {cand_id} ({r['gene']}): Conservation {min(ids):.0f}-{max(ids):.0f}% ({cons['num_hits']} hits)")
        else:
            print(f"  {cand_id} ({r['gene']}): Conservation: {cons.get('error', 'NO HITS')}")

        # Host
        if host.get("hits"):
            best = host["hits"][0]
            risk = "HIGH" if best["identity_pct"] > 50 and best["coverage_pct"] > 50 else (
                "MODERATE" if best["identity_pct"] > 30 else "LOW"
            )
            print(f"    Host: best={best['identity_pct']:.0f}% id / {best['coverage_pct']:.0f}% cov ({risk}) - {best['title'][:60]}")
        else:
            print(f"    Host: No bovine homolog (LOW risk)")


if __name__ == "__main__":
    main()
