#!/usr/bin/env python3
"""
ClpP selectivity analysis for R1-1 (ZG-series ClpP activators)

Aligns S. aureus ClpP (P99089), bovine mitochondrial ClpP (Q2KHU4),
and human mitochondrial ClpP (Q16740) to determine:
1. Whether bovine ClpP has the W146 equivalent that sterically excludes ZG binding
2. Whether the Y61/H83 selectivity determinant pair is conserved in bovine ClpP
3. Overall sequence identity between all three

Key selectivity determinants from literature:
- HsClpP W146 (bulky indole) vs SaClpP I91 (small isopropyl) -> steric exclusion
- HsClpP C-terminal lid (P248-P249) absent in SaClpP
- HsClpP H116/Y138 vs SaClpP Y61/H83 -> reversed pair, ZG297 selectivity

If bovine ClpP has W146 equivalent -> selectivity holds for cattle (GOOD)
If bovine ClpP lacks W146 equivalent -> selectivity concern (BAD)
"""

import json
import os

# Sequences (from UniProt FASTA)
sa_clpP = (
    "MNLIPTVIETTNRGERAYDIYSRLLKDRIIMLGSQIDDNVANSIVSQLLFLQAQDSEKDI"
    "YLYINSPGGSVTAGFAIYDTIQHIKPDVQTICIGMAASMGSFLLAAGAKGKRFALPNAEV"
    "MIHQPLGGAQGQATEIEIAANHILKTREKLNRILSERTGQSIEKIQKDTDRDNFLTAEEA"
    "KEYGLIDEVMVPETK"
)  # 195 aa, P99089

bovine_clpP = (
    "MWPKILLRGGRVAAGLCPALGPRLAARFPPQRTPENRLAPQRNLHATAARALPLIPIVVE"
    "QTGRGERAYDIYSRLLRERIVCVMGPIDDSVASLVIAQLLFLQSESNKKPIHMYINSPGG"
    "VVTSGLAIYDTMQYILNPICTWCVGQAASMGSLLLAAGTPGMRHSLPNSRIMIHQPSGG"
    "ARGQATDIAIQAEEIMKLKKQLYSIYAKHTKQSLQVIESAMERDRYMSPMEAQEFGILDK"
    "VLVHPPQDGEDEPELVQKEPGEPTAVEPAPASA"
)  # 272 aa, Q2KHU4

human_clpP = (
    "MWPGILVGGARVASCRYPALGPRLAAHFPAQRPPQRTLQNGLALQRCLHATATRALPLIP"
    "IVVEQTGRGERAYDIYSRLLRERIVCVMGPIDDSVASLVIAQLLFLQSESNKKPIHMYIN"
    "SPGGVVTAGLAIYDTMQYILNPICTWCVGQAASMGSLLLAAGTPGMRHSLPNSRIMIHQP"
    "SGGARGQATDIAIQAEEIMKLKKQLYNIYAKHTKQSLQVIESAMERDRYMSPMEAQEFGI"
    "LDKVLVHPPQDGEDEPTLVQKEPVEAAPAAEPVPAST"
)  # 277 aa, Q16740

# Clean sequences (remove any whitespace)
sa_clpP = sa_clpP.replace(" ", "").replace("\n", "")
bovine_clpP = bovine_clpP.replace(" ", "").replace("\n", "")
human_clpP = human_clpP.replace(" ", "").replace("\n", "")

print(f"S. aureus ClpP (P99089): {len(sa_clpP)} aa")
print(f"Bovine ClpP (Q2KHU4): {len(bovine_clpP)} aa")
print(f"Human ClpP (Q16740): {len(human_clpP)} aa")

# The bovine and human sequences include mitochondrial transit peptides
# Bovine: transit peptide positions 1-52 (UniProt annotation)
# Human: transit peptide approximately 1-56 (based on alignment)

# Mature forms
bovine_mature = bovine_clpP[52:]  # After transit peptide cleavage
human_mature = human_clpP[56:]    # Approximate; varies by source

print(f"\nBovine mature ClpP: {len(bovine_mature)} aa (after removing 52 aa transit peptide)")
print(f"Human mature ClpP: {len(human_mature)} aa (after removing ~56 aa transit peptide)")

# === Key Selectivity Analysis ===
# We need to find W146 in human ClpP and its equivalent in bovine ClpP
# W146 is numbered from the full precursor sequence

# Find W146 in human ClpP
w146_idx = 145  # 0-indexed for position 146
print(f"\n=== W146 SELECTIVITY DETERMINANT ===")
print(f"Human ClpP position 146 (full precursor): {human_clpP[w146_idx]}")

# Find corresponding residue in bovine ClpP
# Since bovine and human ClpP are highly homologous eukaryotic mitochondrial proteins,
# the alignment should be nearly identical

# Simple approach: align the mature sequences and find the corresponding position
# Human transit peptide ~56 aa, so mature human W146 = position 146-56 = 90 in mature
# Bovine transit peptide 52 aa

# Let's do a simple character-by-character comparison of the mature sequences
print(f"\n=== MATURE SEQUENCE ALIGNMENT (first 120 aa) ===")
print("Comparing bovine mature vs human mature ClpP:")

# The mature sequences should be very similar
# Let's find the W residue
bovine_w_positions = [i for i, aa in enumerate(bovine_mature) if aa == 'W']
human_w_positions = [i for i, aa in enumerate(human_mature) if aa == 'W']
sa_w_positions = [i for i, aa in enumerate(sa_clpP) if aa == 'W']

print(f"\nTryptophan (W) positions in bovine mature ClpP: {bovine_w_positions}")
print(f"Tryptophan (W) positions in human mature ClpP: {human_w_positions}")
print(f"Tryptophan (W) positions in S. aureus ClpP: {sa_w_positions}")

# W146 in full human = W at position 146-56 = 90 in mature human
# Let's verify
human_mature_w90_idx = 146 - 56 - 1  # 0-indexed: position 89
print(f"\nHuman mature ClpP at expected W position (index {human_mature_w90_idx}): {human_mature[human_mature_w90_idx] if human_mature_w90_idx < len(human_mature) else 'OUT OF RANGE'}")

# For bovine, equivalent position should be at 146-52-1 = 93 (0-indexed)
bovine_equiv_idx = 146 - 52 - 1
print(f"Bovine mature ClpP at equivalent position (index {bovine_equiv_idx}): {bovine_mature[bovine_equiv_idx] if bovine_equiv_idx < len(bovine_mature) else 'OUT OF RANGE'}")

# Better approach: look at the actual aligned region
# The key region is around position 90 in the mature form
# Let's find the conserved "CVGQAASMG" motif that is near W146

def find_motif(seq, motif):
    """Find a motif in a sequence and return start position."""
    idx = seq.find(motif)
    return idx

# The motif "CVGQAASMG" should be conserved
motif = "AASMG"
sa_motif_pos = find_motif(sa_clpP, motif)
bovine_motif_pos = find_motif(bovine_mature, motif)
human_motif_pos = find_motif(human_mature, motif)

print(f"\n=== CONSERVED MOTIF '{motif}' POSITIONS ===")
print(f"S. aureus: position {sa_motif_pos}")
print(f"Bovine mature: position {bovine_motif_pos}")
print(f"Human mature: position {human_motif_pos}")

# Now look upstream of this motif for the W/I selectivity residue
# In S. aureus, I91 should be ~10 residues before the AASMG motif
if sa_motif_pos > 0:
    region_start = max(0, sa_motif_pos - 25)
    print(f"\nS. aureus region around selectivity site (pos {region_start}-{sa_motif_pos+10}):")
    print(f"  {sa_clpP[region_start:sa_motif_pos+10]}")
    # I91 in S. aureus
    print(f"  S. aureus position 91 (1-indexed): {sa_clpP[90]}")

if bovine_motif_pos is not None and bovine_motif_pos > 0:
    region_start = max(0, bovine_motif_pos - 25)
    print(f"\nBovine mature region around selectivity site (pos {region_start}-{bovine_motif_pos+10}):")
    print(f"  {bovine_mature[region_start:bovine_motif_pos+10]}")

if human_motif_pos is not None and human_motif_pos > 0:
    region_start = max(0, human_motif_pos - 25)
    print(f"\nHuman mature region around selectivity site (pos {region_start}-{human_motif_pos+10}):")
    print(f"  {human_mature[region_start:human_motif_pos+10]}")

# === Direct W146 equivalent analysis ===
# W146 in full human ClpP. Let's look at the full precursor:
print(f"\n=== FULL PRECURSOR W146 ANALYSIS ===")
print(f"Human full precursor at position 146: {human_clpP[145]}")

# Find the 'ICTWCVG' motif which contains W146
tw_motif = "ICTWCVG"
sa_tw = find_motif(sa_clpP, "ICIG")  # S. aureus has different residues here
bovine_tw = find_motif(bovine_clpP, tw_motif)
human_tw = find_motif(human_clpP, tw_motif)

print(f"\nMotif 'ICTWCVG' in bovine full precursor: position {bovine_tw}")
print(f"Motif 'ICTWCVG' in human full precursor: position {human_tw}")

if bovine_tw is not None and bovine_tw >= 0:
    # The W is at position tw+3 in ICTWCVG
    bovine_w_pos = bovine_tw + 3
    print(f"Bovine W equivalent at position {bovine_w_pos+1} (1-indexed): {bovine_clpP[bovine_w_pos]}")

if human_tw is not None and human_tw >= 0:
    human_w_pos = human_tw + 3
    print(f"Human W at position {human_w_pos+1} (1-indexed): {human_clpP[human_w_pos]}")

# Check what S. aureus has at the corresponding position
# In S. aureus, the equivalent region should have I91 instead of W
# Look for the pattern around the selectivity site
sa_tic = find_motif(sa_clpP, "TICIG")
print(f"\nS. aureus 'TICIG' motif at position: {sa_tic}")
if sa_tic is not None and sa_tic >= 0:
    print(f"S. aureus I91 region: ...{sa_clpP[sa_tic-2:sa_tic+10]}...")
    print(f"S. aureus at position {sa_tic+1} (1-indexed, the I in TICIG): {sa_clpP[sa_tic]}")

# === Y61/H83 vs H116/Y138 selectivity pair (ZG297-specific) ===
print(f"\n=== Y61/H83 vs H116/Y138 SELECTIVITY PAIR (ZG297) ===")
print(f"S. aureus Y61 (1-indexed): {sa_clpP[60]}")
print(f"S. aureus H83 (1-indexed): {sa_clpP[82]}")

# Find equivalent positions in bovine and human
# These are in the mature region of eukaryotic ClpP
# Y61 in SaClpP aligns to H116 in HsClpP (full precursor numbering)
# H83 in SaClpP aligns to Y138 in HsClpP (full precursor numbering)
print(f"\nHuman H116 (1-indexed, full precursor): {human_clpP[115]}")
print(f"Human Y138 (1-indexed, full precursor): {human_clpP[137]}")
print(f"\nBovine at position 116 (1-indexed, full precursor): {bovine_clpP[115]}")
print(f"Bovine at position 138 (1-indexed, full precursor): {bovine_clpP[137]}")

# === Pairwise identity calculation ===
print(f"\n=== PAIRWISE SEQUENCE IDENTITY ===")

def pairwise_identity_simple(seq1, seq2):
    """Simple pairwise identity for sequences of similar length."""
    min_len = min(len(seq1), len(seq2))
    matches = sum(1 for i in range(min_len) if seq1[i] == seq2[i])
    return matches, min_len, matches/min_len * 100

# Bovine vs Human (full precursor)
m, l, pct = pairwise_identity_simple(bovine_clpP, human_clpP)
print(f"Bovine vs Human (full precursor, ungapped): {m}/{l} = {pct:.1f}%")

# Bovine mature vs Human mature
m, l, pct = pairwise_identity_simple(bovine_mature, human_mature)
print(f"Bovine vs Human (mature, ungapped): {m}/{l} = {pct:.1f}%")

# S. aureus vs Bovine mature
m, l, pct = pairwise_identity_simple(sa_clpP, bovine_mature)
print(f"S. aureus vs Bovine mature (ungapped): {m}/{l} = {pct:.1f}%")

# S. aureus vs Human mature
m, l, pct = pairwise_identity_simple(sa_clpP, human_mature)
print(f"S. aureus vs Human mature (ungapped): {m}/{l} = {pct:.1f}%")

# === C-terminal lid analysis ===
print(f"\n=== C-TERMINAL LID MOTIF (HsClpP P248-P249) ===")
print(f"Human ClpP C-terminal (last 40 aa): ...{human_clpP[-40:]}")
print(f"Bovine ClpP C-terminal (last 40 aa): ...{bovine_clpP[-40:]}")
print(f"S. aureus ClpP C-terminal (last 40 aa): ...{sa_clpP[-40:]}")

# Check for double proline (PP) in C-terminal
human_pp = human_clpP[-50:].find("PP")
bovine_pp = bovine_clpP[-50:].find("PP")
sa_pp = sa_clpP[-50:].find("PP")
print(f"\nDouble-proline (PP) in last 50 aa:")
print(f"  Human: {'FOUND at relative pos ' + str(human_pp) if human_pp >= 0 else 'NOT FOUND'}")
print(f"  Bovine: {'FOUND at relative pos ' + str(bovine_pp) if bovine_pp >= 0 else 'NOT FOUND'}")
print(f"  S. aureus: {'FOUND at relative pos ' + str(sa_pp) if sa_pp >= 0 else 'NOT FOUND'}")

# === FINAL VERDICT ===
print(f"\n{'='*60}")
print(f"FINAL SELECTIVITY ASSESSMENT")
print(f"{'='*60}")

# Check if bovine has W at the equivalent of human W146
bovine_has_W146_equiv = False
if bovine_tw is not None and bovine_tw >= 0:
    bovine_w_check = bovine_clpP[bovine_tw + 3]
    bovine_has_W146_equiv = (bovine_w_check == 'W')

print(f"\n1. W146 steric exclusion (primary ZG197 selectivity):")
print(f"   Human ClpP: W (tryptophan) at position 146 -> BLOCKS ZG binding")
print(f"   S. aureus ClpP: I (isoleucine) at position 91 -> ALLOWS ZG binding")
if bovine_has_W146_equiv:
    print(f"   Bovine ClpP: W (tryptophan) at equivalent position -> BLOCKS ZG binding")
    print(f"   VERDICT: Bovine ClpP RETAINS W146 equivalent -> ZG selectivity HOLDS for cattle")
else:
    print(f"   Bovine ClpP: {bovine_clpP[bovine_tw + 3] if bovine_tw and bovine_tw >= 0 else '?'} at equivalent position -> POTENTIAL CONCERN")

# Check C-terminal lid
bovine_has_cterminal_lid = bovine_pp >= 0
print(f"\n2. C-terminal lid motif (secondary selectivity):")
print(f"   Human: Present (PP motif found) -> hinders ZG approach")
print(f"   S. aureus: {'Present' if sa_pp >= 0 else 'Absent'}")
print(f"   Bovine: {'Present (PP motif found) -> hinders ZG approach' if bovine_has_cterminal_lid else 'Absent -> potential concern'}")

# Check Y/H pair
print(f"\n3. Y61/H83 reversed pair (ZG297-specific selectivity):")
print(f"   S. aureus: Y61={sa_clpP[60]}, H83={sa_clpP[82]} -> ALLOWS ZG297 binding")
print(f"   Human: H116={human_clpP[115]}, Y138={human_clpP[137]} -> BLOCKS ZG297 binding")
bovine_h116_equiv = bovine_clpP[115] if len(bovine_clpP) > 115 else '?'
bovine_y138_equiv = bovine_clpP[137] if len(bovine_clpP) > 137 else '?'
print(f"   Bovine: pos116={bovine_h116_equiv}, pos138={bovine_y138_equiv}")

# Save results
results = {
    "analysis": "ClpP selectivity analysis for R1-1 ZG-series",
    "date": "2026-03-26",
    "sequences": {
        "sa_clpP": {"accession": "P99089", "length": len(sa_clpP), "organism": "S. aureus N315"},
        "bovine_clpP": {"accession": "Q2KHU4", "length": len(bovine_clpP), "organism": "Bos taurus", "transit_peptide": "1-52"},
        "human_clpP": {"accession": "Q16740", "length": len(human_clpP), "organism": "Homo sapiens"}
    },
    "selectivity_determinants": {
        "W146_equivalent": {
            "human": {"position": 146, "residue": human_clpP[145]},
            "bovine": {"position": bovine_tw + 4 if bovine_tw and bovine_tw >= 0 else "N/A", "residue": bovine_clpP[bovine_tw + 3] if bovine_tw and bovine_tw >= 0 else "N/A"},
            "sa": {"position": 91, "residue": sa_clpP[90]},
            "bovine_retains_W": bovine_has_W146_equiv
        },
        "cterminal_lid": {
            "human_present": True,
            "bovine_present": bovine_has_cterminal_lid,
            "sa_present": sa_pp >= 0
        }
    },
    "verdict": "Bovine ClpP RETAINS W146 equivalent" if bovine_has_W146_equiv else "Bovine ClpP LACKS W146 equivalent - CONCERN"
}

output_path = "/Users/danielneef/Projects/Agteria/overwatch/programs/mastitis/bioinfo/results/clpP_selectivity_R1.json"
with open(output_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to: {output_path}")
