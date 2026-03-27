# AF3 Submission Request: CpPDE1 Catalytic Domain (cgd3_2320)

**Program:** Cryptosporidiosis | **Priority:** 3
**Date:** 2026-03-27

## Target

- **Protein:** CpPDE1 (Phosphodiesterase 1)
- **Gene:** cgd3_2320 (CryptoDB)
- **UniProt:** Q5CYQ3
- **Organism:** Cryptosporidium parvum Iowa II (Tax ID: 5807)
- **Published:** Nature Communications 2024
- **Sequence length:** ~1,060 aa (full protein)

## Sequence

**Option A (preferred):** Catalytic domain only (~300-400 aa). The 2024 Nature Communications paper identifies the PDE catalytic domain boundaries. Submit the catalytic domain to get the highest confidence prediction.

**Option B:** Full-length protein.

**Action for Daniel:** Retrieve sequence from UniProt (Q5CYQ3) or CryptoDB (cgd3_2320). If catalytic domain boundaries are known from the 2024 paper, submit catalytic domain only.

## Job Configuration

- **Job name:** CpPDE1_catalytic_domain
- **Prediction type:** Monomer
- **Co-factors/ions:**
  - Zn2+ (2 ions) -- PDE catalytic mechanism requires two metal ions in the active site
  - Mg2+ or Mn2+ (1 ion) -- common PDE cofactor
- **Templates:** Allow automatic template selection (human PDE-V structures will be used as templates)

## What This Structure Answers

1. **Active site architecture:** The V900 and H884 residues that confer selectivity over human PDE-V need to be mapped in 3D. An AF3 structure with metal ions will show the actual pocket shape.

2. **Inhibitor optimization:** The 2024 paper used an AlphaFold model for docking. An AF3 prediction (especially with metal ions co-folded) would provide a higher-quality template for structure-guided lead optimization.

3. **Selectivity pocket:** Visualizing the V900/H884 region in 3D vs. the equivalent A869/A853 in human PDE-V will guide design of compounds that exploit the selectivity handle.

4. **New binding modes:** If the AF3 structure reveals allosteric sites or binding pockets not visible in the AlphaFold model, these could provide new chemotypes for CpPDE1 inhibition.

## Rationale

CpPDE1 is a CRISPR-validated drug target with lead compounds showing oral efficacy in mice. The existing AlphaFold model was sufficient for initial docking but AF3 co-folding with catalytic metal ions would provide a higher-fidelity structure for medicinal chemistry optimization. This is the most tractable novel drug target in the pipeline (validated, lead compounds exist, mechanism is novel -- egress blockade).
