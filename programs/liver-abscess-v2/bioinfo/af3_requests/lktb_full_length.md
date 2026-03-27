# AF3 Submission Request: LktB Full-Length Structure

**Target:** LktB -- TPS outer membrane transporter for leukotoxin (LktA)
**Organism:** *Fusobacterium necrophorum* subsp. necrophorum
**Priority:** HIGH (2 of 4)

## Rationale

LktB is the outer membrane pore through which the 336 kDa leukotoxin (LktA) is secreted. Argus v9 generated an ESMFold prediction split into two 400-residue fragments (due to ESMFold's length limit), with mean pLDDT 89.5-95.9. However, the split prediction cannot correctly position the plug helix relative to the beta-barrel or determine the precise POTRA-barrel domain orientation. A full-length AF3 prediction would resolve:

1. Plug helix position inside the barrel lumen (critical for pore-blocking drug design)
2. POTRA-barrel interdomain angle (critical for understanding substrate recognition)
3. Extracellular loop conformations (critical for vaccine antigen/antibody design)

## Sequence

Source: ATCC 25286 genome, accession AZW09022 (from Argus v9 bioinfo analysis)
Length: ~525-550 aa

FASTA file available at: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/proteins/LktB_AZW09022.fasta`

## Job Parameters

- **Job name:** fold_lktb_fnecrophorum_full_length
- **Mode:** Monomer
- **Co-factors:** None
- **Template:** FhaC from *B. pertussis* (PDB: 2QDZ at 3.15 A, 4QKY at 2.90 A) -- ~20% sequence identity, should serve as a structural template

## Questions This Structure Answers

1. Is there a druggable pocket at the plug-barrel interface (for plug-stabilizing compounds)?
2. What is the geometry of the POTRA substrate-binding groove (for competitive peptide inhibitor design)?
3. Which extracellular loops are longest/most exposed (for antibody/vaccine epitope selection)?

## Existing Data

- ESMFold Part 1: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktB_ESMFold_part1.pdb`
- ESMFold Part 2: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktB_ESMFold_part2.pdb`
- ESMFold Full: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/LktB_ESMFold.pdb`
- Structural analysis: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/results/lktb_structural_analysis.md`
