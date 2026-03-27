# AF3 Submission Request: FomA/43K OMP Monomer

**Target:** FomA (42.4 kDa outer membrane protein) -- dual-function target
**Organism:** *Fusobacterium necrophorum*
**Priority:** HIGH (4 of 4)

## Rationale

FomA is the strongest convergence point between Forge and Vulcan analyses. It serves DUAL functions:
1. **Factor H binding** -- enables complement evasion during portal transit (Friberg 2008)
2. **Endothelial adhesion** -- mediates attachment to bovine endothelial cells via fibronectin binding (Kumar 2013, Singh 2022)

An anti-FomA antibody could block BOTH mechanisms simultaneously. To design such an antibody, we need to know:
- Which surface regions mediate Factor H binding
- Which surface regions mediate endothelial adhesion
- Whether these interfaces overlap or are spatially distinct

No pre-computed AlphaFold DB structure exists. No experimental structure exists for any *Fusobacterium* FomA.

## Sequence

GenBank: JQ740821
Length: 377 aa (42.4 kDa by SDS-PAGE)

## Job Parameters

- **Job name:** fold_foma_fnecrophorum_monomer
- **Mode:** Monomer
- **Co-factors:** None

## Questions This Structure Answers

1. Where are the surface-exposed epitope regions for antibody/vaccine design?
2. Is FomA a beta-barrel OMP (expected) or a different fold?
3. Where is the fibronectin-binding domain relative to the putative Factor H-binding domain?
4. Which loops/regions are most conserved (for cross-strain vaccine coverage)?

## Follow-up Jobs (after monomer)

If the monomer structure is confident:
- **FomA + Factor H complex:** Co-fold FomA with bovine Factor H SCR domains to identify the binding interface
- **FomA + fibronectin:** Co-fold with bovine fibronectin type III domains

## Existing Data

- No structural predictions exist for this protein
- Functional data: Kumar 2013 (PMID 23153522), Singh 2022 (PMID 35121302), Friberg 2008 (J Immunol)
