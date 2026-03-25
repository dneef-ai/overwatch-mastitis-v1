#!/usr/bin/env python3
"""
Target Resolution Script for Surveyor Phase 3b
Resolves each protein target to specific identifiers via UniProt REST API and NCBI Entrez.
Caches results in bioinfo/cache/
"""

import json
import os
import sys
import time
import hashlib
import requests
from pathlib import Path

# Paths
BASE_DIR = Path("/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo")
CACHE_DIR = BASE_DIR / "cache"
SEQ_DIR = BASE_DIR / "sequences"
RESULTS_DIR = BASE_DIR / "results"

CACHE_DIR.mkdir(parents=True, exist_ok=True)
SEQ_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# BioPython setup
from Bio import Entrez, SeqIO
Entrez.email = "daniel@agteria.bio"

UNIPROT_BASE = "https://rest.uniprot.org"

# S. aureus taxonomy IDs
SA_TAXID = 1280  # Staphylococcus aureus (species level)

# Bovine taxonomy ID
BOVINE_TAXID = 9913  # Bos taurus

# Priority protein targets from phase-3-candidates.md
TARGETS = [
    {
        "candidate": "2A",
        "name": "SrtA (Sortase A)",
        "gene": "srtA",
        "organism": "Staphylococcus aureus",
        "category": "Known",
        "claimed_localization": "membrane-anchored, active site extracellular",
        "claimed_function": "Transpeptidase that anchors surface proteins (MSCRAMMs) to cell wall",
        "claimed_essentiality": "Non-essential for growth",
    },
    {
        "candidate": "2B",
        "name": "FnBPA/FnBPB (Fibronectin-binding proteins)",
        "gene": "fnbA",  # primary; fnbB is paralog
        "gene2": "fnbB",
        "organism": "Staphylococcus aureus",
        "category": "Novel",
        "claimed_localization": "Cell surface (sortase-anchored)",
        "claimed_function": "Adhesin binding host fibronectin, mediating internalization into epithelial cells",
        "claimed_essentiality": "Non-essential for growth",
    },
    {
        "candidate": "3A",
        "name": "SpA (Protein A)",
        "gene": "spa",
        "organism": "Staphylococcus aureus",
        "category": "Known",
        "claimed_localization": "Cell surface (sortase-anchored)",
        "claimed_function": "Binds IgG-Fc and VH3-Fab, immune evasion",
        "claimed_essentiality": "Non-essential for growth",
    },
    {
        "candidate": "3B",
        "name": "LukM/LukF' (Bicomponent leukocidin)",
        "gene": "lukM",
        "gene2": "lukF-PV",  # lukF' is the partner
        "organism": "Staphylococcus aureus",
        "category": "Known",
        "claimed_localization": "Secreted",
        "claimed_function": "Bicomponent pore-forming leukocidin targeting bovine neutrophils via CCR1",
        "claimed_essentiality": "Non-essential; lineage-dependent carriage (CC151 high, CC97 ~30%)",
    },
    {
        "candidate": "3D",
        "name": "AdsA (Adenosine synthase A)",
        "gene": "adsA",
        "organism": "Staphylococcus aureus",
        "category": "Novel",
        "claimed_localization": "Cell surface (sortase-anchored)",
        "claimed_function": "5'-nucleotidase converting AMP to adenosine, suppressing neutrophil oxidative burst",
        "claimed_essentiality": "Non-essential for growth; virulence factor",
    },
    {
        "candidate": "4A",
        "name": "Hla (Alpha-hemolysin)",
        "gene": "hla",
        "organism": "Staphylococcus aureus",
        "category": "Known",
        "claimed_localization": "Secreted",
        "claimed_function": "Pore-forming toxin targeting epithelial cells, forms heptameric pores",
        "claimed_essentiality": "Non-essential for growth; major virulence factor",
    },
    {
        "candidate": "5B",
        "name": "ClpP (Caseinolytic protease proteolytic subunit)",
        "gene": "clpP",
        "organism": "Staphylococcus aureus",
        "category": "Non-Obvious",
        "claimed_localization": "Cytoplasmic",
        "claimed_function": "Protease involved in protein quality control; ADEP activation causes unregulated proteolysis",
        "claimed_essentiality": "Essential in S. aureus",
    },
    {
        "candidate": "5F",
        "name": "IcaA (Biofilm PIA/PNAG synthesis)",
        "gene": "icaA",
        "gene2": "icaD",
        "gene3": "icaB",
        "gene4": "icaC",
        "organism": "Staphylococcus aureus",
        "category": "Known",
        "claimed_localization": "Membrane (IcaA, IcaD, IcaC) / surface (IcaB)",
        "claimed_function": "PNAG/PIA biosynthesis for biofilm matrix",
        "claimed_essentiality": "Non-essential for growth; biofilm-associated",
    },
]


def cache_key(query_type, query_params):
    """Generate a cache key from query parameters."""
    raw = f"{query_type}:{json.dumps(query_params, sort_keys=True)}"
    return hashlib.md5(raw.encode()).hexdigest()


def get_cached(key):
    """Return cached result if available."""
    path = CACHE_DIR / f"{key}.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None


def set_cache(key, data):
    """Cache a result."""
    path = CACHE_DIR / f"{key}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def query_uniprot(gene_name, organism="Staphylococcus aureus", reviewed=True):
    """Query UniProt for a protein by gene name and organism."""
    ck = cache_key("uniprot", {"gene": gene_name, "organism": organism, "reviewed": reviewed})
    cached = get_cached(ck)
    if cached:
        print(f"  [CACHE HIT] UniProt {gene_name}")
        return cached

    reviewed_str = "true" if reviewed else "false"
    query = f"gene:{gene_name} AND organism_name:\"{organism}\""
    if reviewed:
        query += " AND reviewed:true"

    url = f"{UNIPROT_BASE}/uniprotkb/search"
    params = {
        "query": query,
        "format": "json",
        "size": 5,
        "fields": "accession,id,gene_names,organism_name,organism_id,length,protein_name,cc_subcellular_location,cc_function,ft_signal,ft_transmem,ft_topo_dom,sequence,xref_alphafolddb"
    }

    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
        if results:
            result = results[0]  # best match
            out = {
                "accession": result.get("primaryAccession", ""),
                "entry_name": result.get("uniProtkbId", ""),
                "protein_name": "",
                "gene_names": [],
                "organism": "",
                "organism_id": "",
                "length": 0,
                "sequence": "",
                "subcellular_location": [],
                "function": "",
                "signal_peptide": False,
                "transmembrane_domains": 0,
                "alphafold_id": "",
            }

            # Protein name
            pn = result.get("proteinDescription", {})
            rec_name = pn.get("recommendedName", {})
            if rec_name:
                full_name = rec_name.get("fullName", {})
                out["protein_name"] = full_name.get("value", "") if isinstance(full_name, dict) else str(full_name)

            # Gene names
            genes = result.get("genes", [])
            for g in genes:
                if "geneName" in g:
                    out["gene_names"].append(g["geneName"].get("value", ""))
                for syn in g.get("synonyms", []):
                    out["gene_names"].append(syn.get("value", ""))

            # Organism
            org = result.get("organism", {})
            out["organism"] = org.get("scientificName", "")
            out["organism_id"] = org.get("taxonId", "")

            # Length and sequence
            seq_info = result.get("sequence", {})
            out["length"] = seq_info.get("length", 0)
            out["sequence"] = seq_info.get("value", "")

            # Subcellular location
            comments = result.get("comments", [])
            for c in comments:
                if c.get("commentType") == "SUBCELLULAR LOCATION":
                    for sl in c.get("subcellularLocations", []):
                        loc = sl.get("location", {})
                        out["subcellular_location"].append(loc.get("value", ""))
                elif c.get("commentType") == "FUNCTION":
                    texts = c.get("texts", [])
                    if texts:
                        out["function"] = texts[0].get("value", "")

            # Features: signal peptide, transmembrane
            features = result.get("features", [])
            for ft in features:
                if ft.get("type") == "Signal":
                    out["signal_peptide"] = True
                elif ft.get("type") == "Transmembrane":
                    out["transmembrane_domains"] += 1

            # AlphaFold cross-reference
            xrefs = result.get("uniProtKBCrossReferences", [])
            for xr in xrefs:
                if xr.get("database") == "AlphaFoldDB":
                    out["alphafold_id"] = xr.get("id", "")

            set_cache(ck, out)
            print(f"  [API] UniProt {gene_name} -> {out['accession']} ({out['protein_name']})")
            return out
        else:
            print(f"  [API] UniProt {gene_name} -> NO RESULTS (reviewed={reviewed})")
            if reviewed:
                # Try unreviewed
                return query_uniprot(gene_name, organism, reviewed=False)
            set_cache(ck, None)
            return None
    except Exception as e:
        print(f"  [ERROR] UniProt query for {gene_name}: {e}")
        return None


def save_fasta(accession, gene_name, sequence, organism):
    """Save a FASTA file for a protein."""
    fasta_path = SEQ_DIR / f"{gene_name}_{accession}.fasta"
    with open(fasta_path, "w") as f:
        f.write(f">{accession}|{gene_name}|{organism}\n")
        # Write sequence in 60-char lines
        for i in range(0, len(sequence), 60):
            f.write(sequence[i:i+60] + "\n")
    return fasta_path


def check_alphafold(uniprot_id):
    """Check AlphaFold DB for a pre-computed structure."""
    ck = cache_key("alphafold", {"uniprot_id": uniprot_id})
    cached = get_cached(ck)
    if cached is not None:
        print(f"  [CACHE HIT] AlphaFold {uniprot_id}")
        return cached

    url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list) and len(data) > 0:
                entry = data[0]
                out = {
                    "available": True,
                    "model_url": entry.get("pdbUrl", ""),
                    "cif_url": entry.get("cifUrl", ""),
                    "pae_url": entry.get("paeImageUrl", ""),
                    "confidence_url": entry.get("confidenceImageUrl", ""),
                    "version": entry.get("latestVersion", ""),
                    "model_created": entry.get("modelCreatedDate", ""),
                }
                set_cache(ck, out)
                print(f"  [API] AlphaFold {uniprot_id} -> AVAILABLE (v{out['version']})")
                return out
        out = {"available": False}
        set_cache(ck, out)
        print(f"  [API] AlphaFold {uniprot_id} -> NOT AVAILABLE")
        return out
    except Exception as e:
        print(f"  [ERROR] AlphaFold query for {uniprot_id}: {e}")
        return {"available": False, "error": str(e)}


def query_ncbi_gene(gene_name, organism="Staphylococcus aureus"):
    """Query NCBI Gene for genomic context."""
    ck = cache_key("ncbi_gene", {"gene": gene_name, "organism": organism})
    cached = get_cached(ck)
    if cached:
        print(f"  [CACHE HIT] NCBI Gene {gene_name}")
        return cached

    try:
        search = Entrez.esearch(db="gene", term=f"{gene_name}[Gene Name] AND {organism}[Organism]", retmax=3)
        result = Entrez.read(search)
        search.close()
        time.sleep(0.35)  # rate limit

        ids = result.get("IdList", [])
        if not ids:
            print(f"  [API] NCBI Gene {gene_name} -> NO RESULTS")
            set_cache(ck, None)
            return None

        gene_id = ids[0]
        fetch = Entrez.efetch(db="gene", id=gene_id, rettype="gene_table", retmode="text")
        gene_data = fetch.read()
        fetch.close()
        time.sleep(0.35)

        out = {
            "gene_id": gene_id,
            "raw_data": gene_data[:3000] if isinstance(gene_data, str) else gene_data.decode()[:3000],
        }
        set_cache(ck, out)
        print(f"  [API] NCBI Gene {gene_name} -> Gene ID {gene_id}")
        return out
    except Exception as e:
        print(f"  [ERROR] NCBI Gene query for {gene_name}: {e}")
        return None


def main():
    print("=" * 80)
    print("SURVEYOR TARGET RESOLUTION — Phase 3b")
    print(f"Date: 2026-03-25")
    print(f"Targets: {len(TARGETS)} protein targets")
    print("=" * 80)

    all_results = {}

    for target in TARGETS:
        print(f"\n{'='*60}")
        print(f"Processing: {target['candidate']} — {target['name']}")
        print(f"{'='*60}")

        result = {"target": target, "uniprot": None, "alphafold": None, "ncbi_gene": None, "fasta_paths": []}

        # 1. UniProt query
        print("\n--- UniProt Resolution ---")
        up = query_uniprot(target["gene"], target["organism"])
        result["uniprot"] = up

        if up and up.get("sequence"):
            fasta = save_fasta(up["accession"], target["gene"], up["sequence"], up["organism"])
            result["fasta_paths"].append(str(fasta))
            print(f"  Saved FASTA: {fasta}")

        # If there's a second gene (e.g., fnbB, lukF', icaD)
        for extra_gene_key in ["gene2", "gene3", "gene4"]:
            if extra_gene_key in target:
                extra_gene = target[extra_gene_key]
                print(f"\n--- UniProt Resolution ({extra_gene}) ---")
                up2 = query_uniprot(extra_gene, target["organism"])
                result[f"uniprot_{extra_gene}"] = up2
                if up2 and up2.get("sequence"):
                    fasta2 = save_fasta(up2["accession"], extra_gene, up2["sequence"], up2["organism"])
                    result["fasta_paths"].append(str(fasta2))

        # 2. AlphaFold check
        if up and up.get("accession"):
            print("\n--- AlphaFold DB Check ---")
            af = check_alphafold(up["accession"])
            result["alphafold"] = af

        # 3. NCBI Gene (for genomic context)
        print("\n--- NCBI Gene Context ---")
        ncbi = query_ncbi_gene(target["gene"], target["organism"])
        result["ncbi_gene"] = ncbi

        all_results[target["candidate"]] = result
        time.sleep(0.5)  # gentle rate limiting between targets

    # Save all results
    output_path = RESULTS_DIR / "target_resolution_results.json"

    # Make serializable
    serializable = {}
    for k, v in all_results.items():
        serializable[k] = json.loads(json.dumps(v, default=str))

    with open(output_path, "w") as f:
        json.dump(serializable, f, indent=2)

    print(f"\n\nAll results saved to: {output_path}")

    # Print summary
    print("\n" + "=" * 80)
    print("RESOLUTION SUMMARY")
    print("=" * 80)
    for cand_id, res in all_results.items():
        up = res.get("uniprot")
        if up:
            print(f"  {cand_id}: {up.get('accession', 'N/A')} | {up.get('protein_name', 'N/A')} | {up.get('length', 'N/A')} aa | AF: {'YES' if res.get('alphafold', {}).get('available') else 'NO'}")
        else:
            print(f"  {cand_id}: RESOLUTION FAILED")


if __name__ == "__main__":
    main()
