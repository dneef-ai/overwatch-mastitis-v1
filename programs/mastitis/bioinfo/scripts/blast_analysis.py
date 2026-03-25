#!/usr/bin/env python3
"""
BLAST Analysis Script for Surveyor Phase 3b
Runs BLASTP queries for conservation (S. aureus) and host selectivity (Bos taurus).
Uses NCBI BLAST REST API via BioPython.
Caches results.
"""

import json
import os
import sys
import time
import hashlib
from pathlib import Path
from io import StringIO

BASE_DIR = Path("/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo")
CACHE_DIR = BASE_DIR / "cache"
RESULTS_DIR = BASE_DIR / "results"
SEQ_DIR = BASE_DIR / "sequences"

from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
Entrez.email = "daniel@agteria.bio"

import requests as req

def cache_key(query_type, query_params):
    raw = f"{query_type}:{json.dumps(query_params, sort_keys=True)}"
    return hashlib.md5(raw.encode()).hexdigest()

def get_cached(key):
    path = CACHE_DIR / f"{key}.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None

def set_cache(key, data):
    path = CACHE_DIR / f"{key}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)

# Load resolution results
with open(RESULTS_DIR / "target_resolution_results.json") as f:
    resolution = json.load(f)


def run_blast_ncbi(sequence, database="nr", entrez_query="", expect=1e-5, hitlist_size=50, max_retries=3):
    """Run BLASTP against NCBI and return parsed results."""
    ck = cache_key("blast", {
        "seq_hash": hashlib.md5(sequence.encode()).hexdigest()[:12],
        "db": database,
        "entrez_query": entrez_query,
        "expect": expect
    })
    cached = get_cached(ck)
    if cached:
        print(f"    [CACHE HIT] BLAST ({entrez_query[:40]}...)")
        return cached

    for attempt in range(max_retries):
        try:
            print(f"    [BLAST] Submitting to NCBI (attempt {attempt+1})...")
            print(f"    Query: {entrez_query[:60]}...")
            print(f"    Sequence length: {len(sequence)} aa")

            result_handle = NCBIWWW.qblast(
                "blastp",
                database,
                sequence,
                entrez_query=entrez_query,
                expect=expect,
                hitlist_size=hitlist_size,
                format_type="XML"
            )

            blast_records = NCBIXML.parse(result_handle)
            blast_record = next(blast_records)

            hits = []
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    identity_pct = (hsp.identities / hsp.align_length) * 100
                    coverage_pct = (hsp.align_length / len(sequence)) * 100
                    hits.append({
                        "title": alignment.title[:200],
                        "accession": alignment.accession,
                        "length": alignment.length,
                        "identities": hsp.identities,
                        "align_length": hsp.align_length,
                        "identity_pct": round(identity_pct, 1),
                        "coverage_pct": round(coverage_pct, 1),
                        "e_value": hsp.expect,
                        "score": hsp.score,
                        "gaps": hsp.gaps,
                    })

            result = {
                "query_length": len(sequence),
                "database": database,
                "entrez_query": entrez_query,
                "expect": expect,
                "num_hits": len(hits),
                "hits": hits[:20],  # keep top 20
                "date": "2026-03-25",
            }
            set_cache(ck, result)
            print(f"    [BLAST] {len(hits)} hits found")
            return result

        except Exception as e:
            print(f"    [ERROR] BLAST attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                wait_time = 30 * (attempt + 1)
                print(f"    Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            else:
                print(f"    [FAILED] All BLAST attempts failed for this query")
                return {"error": str(e), "num_hits": 0, "hits": []}


def analyze_conservation(candidate_id, gene_name, sequence):
    """BLAST against S. aureus to check conservation across CCs."""
    print(f"\n  --- Conservation BLAST for {gene_name} ---")
    # BLAST against S. aureus (taxid 1280)
    result = run_blast_ncbi(
        sequence,
        database="nr",
        entrez_query="Staphylococcus aureus[Organism]",
        expect=1e-10,
        hitlist_size=100
    )
    return result


def analyze_host_selectivity(candidate_id, gene_name, sequence):
    """BLAST against Bos taurus proteome to check host homology."""
    print(f"\n  --- Host Selectivity BLAST for {gene_name} ---")
    result = run_blast_ncbi(
        sequence,
        database="nr",
        entrez_query="Bos taurus[Organism]",
        expect=0.01,  # more permissive to catch weak homologs
        hitlist_size=10
    )
    return result


def main():
    print("=" * 80)
    print("SURVEYOR BLAST ANALYSIS — Phase 3b")
    print("Date: 2026-03-25")
    print("=" * 80)

    all_blast_results = {}

    for cand_id, res in resolution.items():
        target = res["target"]
        up = res.get("uniprot")

        if not up or not up.get("sequence"):
            print(f"\n  SKIP {cand_id} — no sequence available")
            continue

        gene_name = target["gene"]
        sequence = up["sequence"]

        print(f"\n{'='*60}")
        print(f"BLAST Analysis: {cand_id} — {target['name']}")
        print(f"Accession: {up['accession']} | Length: {up['length']} aa")
        print(f"{'='*60}")

        # Conservation BLAST (S. aureus)
        conservation = analyze_conservation(cand_id, gene_name, sequence)

        # Host selectivity BLAST (Bos taurus)
        time.sleep(5)  # Rate limit between BLAST submissions
        host_select = analyze_host_selectivity(cand_id, gene_name, sequence)

        all_blast_results[cand_id] = {
            "gene": gene_name,
            "accession": up["accession"],
            "length": up["length"],
            "conservation": conservation,
            "host_selectivity": host_select,
        }

        time.sleep(5)  # Rate limit between targets

    # Save results
    output_path = RESULTS_DIR / "blast_results.json"
    with open(output_path, "w") as f:
        json.dump(all_blast_results, f, indent=2, default=str)

    print(f"\n\nAll BLAST results saved to: {output_path}")

    # Print summary
    print("\n" + "=" * 80)
    print("BLAST SUMMARY")
    print("=" * 80)
    for cand_id, res in all_blast_results.items():
        cons = res["conservation"]
        host = res["host_selectivity"]

        # Conservation summary
        cons_hits = cons.get("num_hits", 0)
        if cons.get("hits"):
            identities = [h["identity_pct"] for h in cons["hits"]]
            cons_range = f"{min(identities):.0f}-{max(identities):.0f}%"
        else:
            cons_range = "NO HITS"

        # Host selectivity
        host_hits = host.get("num_hits", 0)
        if host.get("hits"):
            best_host = host["hits"][0]
            host_risk = f"{best_host['identity_pct']:.0f}% id, {best_host['coverage_pct']:.0f}% cov"
            if best_host['identity_pct'] > 50 and best_host['coverage_pct'] > 50:
                risk_level = "HIGH"
            elif best_host['identity_pct'] > 30:
                risk_level = "MODERATE"
            else:
                risk_level = "LOW"
        else:
            host_risk = "No bovine homolog"
            risk_level = "LOW"

        print(f"  {cand_id} ({res['gene']}): Conservation={cons_range} ({cons_hits} SA hits) | Host={host_risk} ({risk_level})")


if __name__ == "__main__":
    main()
