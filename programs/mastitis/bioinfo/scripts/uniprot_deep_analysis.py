#!/usr/bin/env python3
"""
Deep UniProt Analysis for Surveyor Phase 3b
Uses UniProt REST API for:
1. Conservation check - search for orthologs across S. aureus strains
2. Host selectivity - search for bovine homologs
3. Detailed annotation verification
"""

import json
import hashlib
import time
import requests
from pathlib import Path

BASE_DIR = Path("/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo")
CACHE_DIR = BASE_DIR / "cache"
RESULTS_DIR = BASE_DIR / "results"

UNIPROT_BASE = "https://rest.uniprot.org"

with open(RESULTS_DIR / "target_resolution_results.json") as f:
    resolution = json.load(f)


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


def uniprot_search(query, fields, size=50):
    """Generic UniProt search."""
    ck = cache_key("uniprot_search", {"query": query, "fields": fields, "size": size})
    cached = get_cached(ck)
    if cached is not None:
        return cached

    url = f"{UNIPROT_BASE}/uniprotkb/search"
    params = {
        "query": query,
        "format": "json",
        "size": size,
        "fields": fields,
    }

    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
        set_cache(ck, results)
        return results
    except Exception as e:
        print(f"  [ERROR] UniProt search: {e}")
        return []


def check_conservation_uniprot(gene_name, reference_length):
    """Check conservation across S. aureus strains using UniProt search."""
    print(f"\n  --- Conservation (UniProt) for {gene_name} ---")

    # Search for the gene across S. aureus
    query = f'gene:{gene_name} AND organism_id:1280'
    fields = "accession,organism_name,organism_id,length,gene_names"

    results = uniprot_search(query, fields, size=100)

    if not results:
        print(f"    No S. aureus entries found")
        return {"num_entries": 0, "entries": []}

    entries = []
    for r in results:
        org = r.get("organism", {})
        genes = r.get("genes", [])
        gene_list = []
        for g in genes:
            if "geneName" in g:
                gene_list.append(g["geneName"].get("value", ""))

        entries.append({
            "accession": r.get("primaryAccession", ""),
            "organism": org.get("scientificName", ""),
            "strain": org.get("commonName", ""),
            "length": r.get("sequence", {}).get("length", 0),
            "genes": gene_list,
        })

    print(f"    Found {len(entries)} S. aureus entries for {gene_name}")

    # Check length variation (proxy for conservation)
    lengths = [e["length"] for e in entries if e["length"] > 0]
    if lengths:
        avg_len = sum(lengths) / len(lengths)
        length_variation = max(lengths) - min(lengths)
        print(f"    Length range: {min(lengths)}-{max(lengths)} aa (variation: {length_variation})")

    return {
        "num_entries": len(entries),
        "entries": entries[:20],  # keep top 20
        "length_range": f"{min(lengths)}-{max(lengths)}" if lengths else "N/A",
        "reference_length": reference_length,
    }


def check_host_homology_uniprot(gene_name, protein_name):
    """Check for bovine homologs using UniProt search."""
    print(f"\n  --- Host Selectivity (UniProt) for {gene_name} ---")

    # Search for similar proteins in Bos taurus
    # Try by gene name first, then by protein name
    queries = [
        f'gene:{gene_name} AND organism_id:9913',
        f'protein_name:"{protein_name}" AND organism_id:9913',
    ]

    all_results = []
    for q in queries:
        fields = "accession,organism_name,length,protein_name,gene_names,cc_function"
        results = uniprot_search(q, fields, size=10)
        for r in results:
            acc = r.get("primaryAccession", "")
            if not any(e["accession"] == acc for e in all_results):
                pn = r.get("proteinDescription", {})
                rec_name = pn.get("recommendedName", {})
                full_name = ""
                if rec_name:
                    fn = rec_name.get("fullName", {})
                    full_name = fn.get("value", "") if isinstance(fn, dict) else str(fn)

                genes = r.get("genes", [])
                gene_list = []
                for g in genes:
                    if "geneName" in g:
                        gene_list.append(g["geneName"].get("value", ""))

                func = ""
                for c in r.get("comments", []):
                    if c.get("commentType") == "FUNCTION":
                        texts = c.get("texts", [])
                        if texts:
                            func = texts[0].get("value", "")

                all_results.append({
                    "accession": acc,
                    "protein_name": full_name,
                    "genes": gene_list,
                    "length": r.get("sequence", {}).get("length", 0),
                    "function": func[:200],
                })

    if all_results:
        print(f"    Found {len(all_results)} Bos taurus entries")
        for r in all_results[:3]:
            print(f"      {r['accession']}: {r['protein_name']} ({r['genes']})")
    else:
        print(f"    No Bos taurus homologs found by gene/protein name search")

    return {
        "num_bovine_hits": len(all_results),
        "hits": all_results[:5],
        "note": "Name-based search only; BLASTP needed for sequence-level homology" if all_results else "No bovine homolog found by name search"
    }


def get_detailed_annotation(accession):
    """Get detailed UniProt annotation for a specific accession."""
    ck = cache_key("uniprot_detail", {"accession": accession})
    cached = get_cached(ck)
    if cached is not None:
        return cached

    url = f"{UNIPROT_BASE}/uniprotkb/{accession}"
    params = {
        "format": "json",
        "fields": "accession,protein_name,gene_names,organism_name,cc_subcellular_location,cc_function,cc_catalytic_activity,cc_pathway,cc_tissue_specificity,ft_signal,ft_transmem,ft_topo_dom,ft_domain,ft_binding,ft_act_site,ft_metal,ft_motif,keyword,xref_pdb,xref_alphafolddb,cc_interaction"
    }

    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        set_cache(ck, data)
        return data
    except Exception as e:
        print(f"  [ERROR] UniProt detail for {accession}: {e}")
        return None


def parse_annotation(data):
    """Parse detailed UniProt annotation."""
    if not data:
        return {}

    result = {
        "localization": [],
        "function": "",
        "catalytic_activity": [],
        "pathway": [],
        "signal_peptide": False,
        "transmembrane_count": 0,
        "transmembrane_details": [],
        "active_site": [],
        "metal_binding": [],
        "domains": [],
        "keywords": [],
        "pdb_structures": [],
    }

    # Comments
    for c in data.get("comments", []):
        ct = c.get("commentType", "")
        if ct == "SUBCELLULAR LOCATION":
            for sl in c.get("subcellularLocations", []):
                loc = sl.get("location", {})
                result["localization"].append(loc.get("value", ""))
        elif ct == "FUNCTION":
            texts = c.get("texts", [])
            if texts:
                result["function"] = texts[0].get("value", "")
        elif ct == "CATALYTIC ACTIVITY":
            reaction = c.get("reaction", {})
            if reaction:
                result["catalytic_activity"].append(reaction.get("name", ""))
        elif ct == "PATHWAY":
            texts = c.get("texts", [])
            for t in texts:
                result["pathway"].append(t.get("value", ""))

    # Features
    for ft in data.get("features", []):
        ft_type = ft.get("type", "")
        if ft_type == "Signal":
            result["signal_peptide"] = True
        elif ft_type == "Transmembrane":
            result["transmembrane_count"] += 1
            loc = ft.get("location", {})
            start = loc.get("start", {}).get("value", "?")
            end = loc.get("end", {}).get("value", "?")
            result["transmembrane_details"].append(f"{start}-{end}")
        elif ft_type == "Active site":
            loc = ft.get("location", {})
            pos = loc.get("start", {}).get("value", "?")
            desc = ft.get("description", "")
            result["active_site"].append(f"Pos {pos}: {desc}")
        elif ft_type == "Metal binding":
            loc = ft.get("location", {})
            pos = loc.get("start", {}).get("value", "?")
            desc = ft.get("description", "")
            result["metal_binding"].append(f"Pos {pos}: {desc}")
        elif ft_type == "Domain":
            loc = ft.get("location", {})
            start = loc.get("start", {}).get("value", "?")
            end = loc.get("end", {}).get("value", "?")
            desc = ft.get("description", "")
            result["domains"].append(f"{desc} ({start}-{end})")

    # Keywords
    for kw in data.get("keywords", []):
        result["keywords"].append(kw.get("name", ""))

    # PDB cross-refs
    for xr in data.get("uniProtKBCrossReferences", []):
        if xr.get("database") == "PDB":
            result["pdb_structures"].append(xr.get("id", ""))

    return result


def main():
    print("=" * 80)
    print("SURVEYOR DEEP ANNOTATION ANALYSIS — Phase 3b")
    print("Date: 2026-03-25")
    print("=" * 80)

    all_results = {}

    for cand_id, res in resolution.items():
        target = res["target"]
        up = res.get("uniprot")

        if not up:
            continue

        accession = up["accession"]
        gene_name = target["gene"]

        print(f"\n{'='*60}")
        print(f"Deep Analysis: {cand_id} — {target['name']} ({accession})")
        print(f"{'='*60}")

        # 1. Conservation check
        conservation = check_conservation_uniprot(gene_name, up.get("length", 0))
        time.sleep(0.5)

        # 2. Host selectivity
        protein_name = up.get("protein_name", target["name"])
        host = check_host_homology_uniprot(gene_name, protein_name)
        time.sleep(0.5)

        # 3. Detailed annotation
        print(f"\n  --- Detailed Annotation for {accession} ---")
        detail = get_detailed_annotation(accession)
        annotation = parse_annotation(detail)
        if annotation:
            print(f"    Localization: {annotation['localization']}")
            print(f"    Signal peptide: {annotation['signal_peptide']}")
            print(f"    TM domains: {annotation['transmembrane_count']}")
            print(f"    Active sites: {annotation['active_site']}")
            print(f"    PDB structures: {annotation['pdb_structures']}")
        time.sleep(0.5)

        all_results[cand_id] = {
            "gene": gene_name,
            "accession": accession,
            "conservation": conservation,
            "host_selectivity": host,
            "annotation": annotation,
            "claimed_localization": target.get("claimed_localization", ""),
            "claimed_function": target.get("claimed_function", ""),
            "claimed_essentiality": target.get("claimed_essentiality", ""),
        }

    # Save
    output_path = RESULTS_DIR / "deep_annotation_results.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n\nResults saved to: {output_path}")

    # Summary
    print("\n" + "=" * 80)
    print("ANNOTATION VERIFICATION SUMMARY")
    print("=" * 80)
    for cand_id, res in all_results.items():
        ann = res.get("annotation", {})
        cons = res.get("conservation", {})
        host = res.get("host_selectivity", {})

        loc_match = "MATCH" if any(
            cl.lower() in " ".join(ann.get("localization", [])).lower()
            for cl in res.get("claimed_localization", "").lower().split(",")
            if cl.strip()
        ) else "CHECK"

        print(f"  {cand_id} ({res['gene']}):")
        print(f"    Conservation: {cons.get('num_entries', 0)} SA entries, length {cons.get('length_range', 'N/A')}")
        print(f"    Host homologs: {host.get('num_bovine_hits', 0)} bovine hits")
        print(f"    Localization: {ann.get('localization', [])} (claimed: {res.get('claimed_localization', '')})")
        print(f"    Signal peptide: {ann.get('signal_peptide')}, TM: {ann.get('transmembrane_count')}")
        print(f"    PDB structures: {len(ann.get('pdb_structures', []))}")
        print()


if __name__ == "__main__":
    main()
