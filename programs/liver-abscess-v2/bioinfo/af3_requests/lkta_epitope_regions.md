# AF3 Submission Request: LktA Epitope Regions (PL1, PL3, PL4)

**Target:** LktA leukotoxin -- immunodominant epitope regions
**Organism:** *Fusobacterium necrophorum* subsp. necrophorum
**Priority:** HIGHEST (1 of 4)

## Rationale

The entire Gate 2 antibody/vaccine portfolio (G2-1 mAb, G2-2 mRNA vaccine, G2-3 subunit vaccine, COMBO-1, COMBO-2) depends on knowing the surface exposure and conformation of the immunodominant epitope regions identified by Xiao et al. (2009, Vet Res Commun).

LktA is 3,241 aa (336 kDa) -- far too large for a single AF3 submission. Only fragments (116-145 aa) have been predicted previously (Argus v15). The approach is to submit the three immunodominant regions (PL1, PL3, PL4) as individual jobs, plus a multi-epitope construct.

**Full-length LktA has:**
- Zero cysteines (no disulfide bonds -- unusual)
- No sequence homology to any other protein
- 10.6% glycine, 9.6% asparagine content
- Filamentous adhesin / leukotoxin family annotation

## Sequences

Source: GenBank AF312861 (9,726 bp lktA ORF encoding 3,241 aa)

**Job 1: PL1 region**
- Approximate position: N-terminal portion of LktA
- Xiao 2009 designates PL1 as one of three immunodominant truncated proteins
- Exact boundaries from Xiao 2009 paper

**Job 2: PL3 region**
- Central region of LktA

**Job 3: PL4 region**
- C-terminal region of LktA

**Job 4: Multi-epitope construct**
- PL1 + PL3 + PL4 concatenated with flexible linkers (GGGGS x 3)
- This mimics the proposed recombinant fusion vaccine antigen (G2-3)

## Job Parameters

- **Job names:** fold_lkta_PL1, fold_lkta_PL3, fold_lkta_PL4, fold_lkta_multi_epitope
- **Mode:** Monomer for each
- **Co-factors:** None (no metal binding expected given zero cysteines and no known cofactors)

## Questions These Structures Answer

1. Are the PL1/PL3/PL4 regions structured or disordered? (If disordered, epitope presentation in a vaccine may need scaffolding.)
2. What surface-exposed residues are available for antibody binding?
3. Does the multi-epitope fusion fold independently, or do the regions interact?
4. Where is the conserved B-cell epitope ISSFGVGV (Xiao 2024) in 3D space?

## Existing Data

- Argus v15 AF3 predictions: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/structures/lkta_monomer/`
- Argus v15 binder designs: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/results/lkta_ep3d7_binder_design/` and `.../lkta_ep3d7_extended_v2/`
- RFAntibody results: `/Users/danielneef/Projects/Argus/elanco-liver-abscess-v15/results/rfantibody/`

## NOTE FOR DANIEL

The exact amino acid boundaries for PL1, PL3, PL4 need to be extracted from Xiao et al. 2009 (Vet Res Commun, DOI 10.1007/s11259-009-9223-6). The paper describes truncated recombinant proteins but the exact residue ranges need to be confirmed before submission.
