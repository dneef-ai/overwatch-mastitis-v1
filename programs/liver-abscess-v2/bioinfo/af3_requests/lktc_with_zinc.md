# AF3 Submission Request: LktC with Zn2+ Ion

**Target:** LktC -- leukotoxin activating protein (function unresolved)
**Organism:** *Fusobacterium necrophorum* subsp. necrophorum
**Priority:** HIGH (3 of 4)

## Rationale

LktC is a 145 aa protein with a CCHH motif (C101/C105/H128/H132) that could coordinate zinc. In the current ESMFold prediction (pLDDT 90), the Cys and His residues are 13-21 A apart -- far too distant for metal coordination. This is likely an artifact because ESMFold cannot model metal binding. AF3 co-folding with a Zn2+ ion should resolve whether these residues converge to form a zinc-binding site (~2 A coordination distances).

If the CCHH motif forms a zinc site, this confirms LktC as a zinc metalloenzyme -- opening a validated drug target class (zinc chelators, hydroxamates from the MMP inhibitor field). If the residues remain separated even with zinc, the metalloenzyme hypothesis is weakened.

## Sequence

Length: 145 aa
Source: ATCC 25286 genome (from Argus v9 -- originally misannotated as "histidine kinase")

FASTA available at the protein sequence embedded in the Argus v9 operon analysis. The ESMFold structure is at:
`/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/HK_lktA_adjacent_ESMFold.pdb`

## Job Parameters

- **Job name:** fold_lktc_fnecrophorum_with_zinc
- **Mode:** Monomer + ion
- **Co-factors:** 1x Zn2+ ion (coordinated by C101, C105, H128, H132)
- **Alternative job:** Also submit WITHOUT zinc to see if AF3 native prediction differs from ESMFold

## Questions This Structure Answers

1. Does the CCHH motif form a zinc-binding site?
2. If yes: what is the active site geometry, and where is the substrate-binding cleft?
3. If no: is there an alternative catalytic mechanism (e.g., H128-H132 as general acid/base dyad)?
4. Is Cys19 (rSASA 0.46 in ESMFold) truly surface-accessible for covalent drug design?

## Existing Data

- ESMFold structure: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/HK_lktA_adjacent_ESMFold.pdb`
- Pocket analysis: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/results/lktc_pocket_analysis.md`
- Operon analysis: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/results/operon_protein_analysis.md`
- Fragment library: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v9/bioinfo/structures/lktc_fragment_library.sdf`
