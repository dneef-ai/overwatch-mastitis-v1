# AF3 Submission Request: CpMyb-M (cgd6_2250)

**Program:** Cryptosporidiosis | **Priority:** 1 (HIGHEST)
**Date:** 2026-03-27

## Target

- **Protein:** Myb-M transcription factor
- **Gene:** cgd6_2250 (CryptoDB legacy) / cpbgf_6002250 (BroadGenomics)
- **Organism:** Cryptosporidium parvum Iowa II (Tax ID: 5807)
- **Published:** Nature 2024, Striepen lab

## Sequence

Sequence to be retrieved from CryptoDB for cgd6_2250. The protein contains a Myb DNA-binding domain (expected ~50 aa repeat x 2-3) plus regulatory domains.

**Action for Daniel:** Retrieve the full amino acid sequence from CryptoDB (https://cryptodb.org/cryptodb/app/record/gene/cgd6_2250) and paste into AlphaFold Server.

## Job Configuration

- **Job name:** CpMyb-M_monomer
- **Prediction type:** Monomer (first pass)
- **Co-factors/ions:** None (DNA-binding protein, but monomer structure first)
- **Templates:** Allow automatic template selection

## What This Structure Answers

1. **Is Myb-M druggable?** Myb-family transcription factors have been targeted via protein-protein interaction (PPI) disruption (Myb-p300 in AML). The AF3 structure will reveal:
   - The DNA-binding domain architecture and whether it has accessible binding pockets
   - Whether the protein has a defined protein-protein interaction interface (similar to the Myb-p300 interaction surface in human c-Myb)
   - Disordered regions that might be targeted by PROTACs/molecular glue degraders

2. **Structural basis for selectivity:** Comparison with human c-Myb/A-Myb/B-Myb structures to identify C. parvum-specific features.

3. **Forced activation strategy:** If Myb-M stabilization (not inhibition) is the goal (driving premature male terminal differentiation), the structure would identify surfaces that could be stabilized by a small molecule.

## Rationale

Myb-M is the single highest-impact novel target in the cryptosporidiosis portfolio. Genetic ablation eliminates male gametes and blocks ALL oocyst production (both thick-walled for transmission AND thin-walled for autoinfection). Forced overexpression creates a parasitic "death switch" by driving all parasites into terminal male differentiation. No structure exists. Structure prediction is the critical next step for druggability assessment.

## Follow-Up

If the monomer structure reveals promising features, a second AF3 job may be requested:
- **CpMyb-M + DNA complex** -- to map the DNA-binding interface
- **CpMyb-M + predicted binding partner** -- if interacting partners are identified
