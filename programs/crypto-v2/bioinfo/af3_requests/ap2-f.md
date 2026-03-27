# AF3 Submission Request: CpAP2-F (cgd4_1110)

**Program:** Cryptosporidiosis | **Priority:** 2
**Date:** 2026-03-27

## Target

- **Protein:** AP2-F (Apetala 2-domain transcription factor, female-specific)
- **Gene:** cgd4_1110
- **Organism:** Cryptosporidium parvum Iowa II (Tax ID: 5807)
- **Published:** mBio 2023, Striepen lab
- **Notable:** Three predicted AP2 domains. Multi-domain protein. Plant-type transcription factor ABSENT from mammals.

## Sequence

Sequence to be retrieved from CryptoDB for cgd4_1110.

**Action for Daniel:** Retrieve the full amino acid sequence from CryptoDB (https://cryptodb.org/cryptodb/app/record/gene/cgd4_1110) and paste into AlphaFold Server.

## Job Configuration

- **Job name:** CpAP2-F_monomer
- **Prediction type:** Monomer
- **Co-factors/ions:** None
- **Templates:** Allow automatic template selection
- **Note:** Large multi-domain protein with 3 AP2 domains. If the full sequence exceeds AF3 limits, prioritize the region containing all three AP2 domains.

## What This Structure Answers

1. **Domain architecture:** How are the three AP2 domains arranged? Are they clustered or separated by linker regions?
2. **Druggable interfaces:** AP2 domains bind DNA via a beta-sheet/alpha-helix motif. Are the inter-domain interfaces or DNA-binding surfaces targetable?
3. **Selectivity basis:** AP2 domains are plant-type and absent from mammals. Any AP2-targeting compound would inherently be selective over host proteins.
4. **Oocyst wall biology:** AP2-F controls COWP gene transcription. Understanding the structure informs how to disrupt this specific transcriptional program.

## Rationale

AP2-F controls oocyst wall formation in female gametes. Genetic ablation blocks oocyst shedding. As a plant-type transcription factor absent from mammals, it offers intrinsic selectivity that Myb-M does not. The key biological question (does AP2-F inhibition block thin-walled oocysts for autoinfection, or only thick-walled for transmission?) requires wet-lab experiments, but the structural question (is AP2-F druggable?) can be addressed computationally.
