# Argus Quality Standards

These standards are mandatory. They are derived from two independent AI drug discovery agents (Argus and Kestrel), cross-model adversarial review, and human scientific oversight across three animal health programs. Each standard exists because its absence caused a specific, documented error.

---

## Evidence Standards (1-9)

### 1. Evidence Tiers on Every Claim

Every biological claim, mechanism assertion, or efficacy statement must be tagged:

- **[ESTABLISHED]** — ≥3 independent replications in target species
- **[MODERATE]** — 2+ studies, or strong data in a closely related model
- **[PRELIMINARY]** — Single study, single lab, or unreplicated
- **[INFERRED]** — Extrapolated from another species, in silico, or theoretical

Never present a [PRELIMINARY] finding as though it were [ESTABLISHED]. The v8 HCAR2 antagonist thesis was built on a single unreplicated in vitro paper — tagging it [PRELIMINARY] from the start would have flagged the risk immediately.

### 2. The 20-Year Test

For any promising approach published for >5 years with no commercial product, explain why no product exists. Possible answers:

- Scientific failure (didn't work in vivo)
- Manufacturing/formulation barrier
- Regulatory pathway uncertainty
- No commercial champion / stayed in academic lab
- IP expired or fragmented
- Market too small to justify investment

Silence is data. If nobody has commercialized a 20-year-old finding, there is usually a reason. Find it.

**Example:** DPC3147 has 28 years of published work and no product. The reasons (expired patent, no industry partner, Teagasc can't commercialize, cure rate only matches antibiotics) should have been part of the target evaluation. **Example:** sEH inhibitors have been studied for human inflammatory diseases since ~2005 with zero approved products in any species — this killed sEH as a mastitis co-lead.

### 3. Information Trajectory Framing

When comparing targets at different evidence levels, distinguish between:

- **Ceiling-bounded targets:** Substantial data exists but the trajectory is flat. More data confirms the ceiling, doesn't raise it. (e.g., DPC3147 → ~47% cure rate after 28 years)
- **Open-ceiling targets:** Less evidence but each de-risk experiment has high discriminatory power. (e.g., a novel target where $20K tells you go/no-go)

Present both types honestly. Don't inflate confidence on open-ceiling targets or dismiss ceiling-bounded targets — let the partner's risk appetite decide.

### 4. Citation Verification

Every PMID must be checked against the actual paper. The claim attributed to the citation must match what the paper actually says. Author attributions must be correct.

Known failure modes:
- "Kenez 2024" was actually Mamedova et al. 2024 — propagated through 5+ documents
- PMID 24430849 cited for transgenic cattle lysozyme was actually a paper about albatross habitat
- "Tsai 2024" was Caldera et al. with the wrong journal
- Nakaminami 2017 listed as PMID 28892486 (a psychology paper)

One wrong citation in a partner presentation destroys credibility. Run a verification pass on all citations before any external document.

### 5. Re-Read Primary Sources for Strategic Claims

For any claim that becomes a strategic pillar (top 3 ranking, kill decision, Tier 1 promotion), dispatch an agent to fetch and read the FULL TEXT of the key paper — not just verify the PMID exists. Iterative analysis compresses claims: "A, but also B" becomes "A" becomes "A, proving X" where X was never in the paper.

**Example:** Bramley 1989 ("also developed acute mastitis, but no deaths occurred") was compressed to "zero lethality" implying complete protection — a significant overstatement detected only when the primary source was re-read.

### 6. Species and Model Tagging

Every evidence claim must be tagged with the species and model system it comes from: bovine in-vivo, bovine cell (MAC-T/BMEC), mouse in-vivo, human cell, or computational.

A mouse mastitis result is NOT bovine evidence. A human MRSA wound study is NOT bovine intramammary evidence. Tuchscherr 2008 was cited as "direct proof passive immunization works in the mammary gland" — but the study was in lactating mice, not cows. Both GPT-5.4 and Gemini caught this error.

### 7. Old Claims Require Modern Confirmation

Any finding >10 years old cited as established fact must have modern confirmation. If it doesn't, ask why. Bramley 1989 (35 years old, mouse model) should not be treated as definitive bovine evidence without modern replication.

If a "known" mechanism hasn't been confirmed in 20 years, either it's wrong, it's more complex than assumed, or nobody cared enough to replicate it. All three possibilities are informative.

### 8. Computational Evidence Is Triage, Not Validation

Genome search, orthology mapping, docking scores, and AlphaFold structures are screening tools. They triage targets for experimental validation. They do not validate a target on their own. Never promote a target based solely on computational evidence.

**Example:** The sea-lice IR25a family was computationally identified as promising, but PRIORITIZE status required functional RNAi data (Nunez-Acuña 2019), not just genome annotation.

### 9. Extraordinary Claims Require Extraordinary Scrutiny

If a single lab reports results 100-1000x better than the rest of a field, treat it as artifact until independently replicated. Apply the stoichiometric test: for any mechanism requiring intracellular accumulation (antisense, enzyme inhibition), calculate whether the reported effective concentration provides enough molecules per cell to engage the target.

**Example:** Penchovsky picomolar MIC claims yielded 0.00075 molecules/cell at 1.25 nM — physically impossible for the claimed mechanism. This standard would have caught it before analysis cycles were wasted.

---

## Target Standards (10-17)

### 10. Target Product Profile Required

Every target proposed for a partner portfolio must include:

- **Indication:** What disease state, what animals, what production stage
- **Route of administration:** Intramammary, injectable, oral, topical
- **Target price point:** What a farmer/vet would pay per treatment
- **Withhold period:** Milk and meat withdrawal requirements
- **Regulatory pathway:** USDA-CVB (biologics), FDA-CVM NADA (drugs), or feed additive
- **Who buys it:** Veterinarian prescribes? Producer administers? Sold through what channel?

A target without a TPP is a hypothesis, not a product concept.

### 11. Separate Target From Lead Molecule

A validated target is NOT the same as a viable lead compound. Always assess in two columns:
- Column 1: Is the TARGET validated? (genetics, mechanism, disease relevance)
- Column 2: Is the LEAD MOLECULE suitable for THIS INDICATION? (physicochemistry, milk matrix, COGS, safety)

A target can be Tier 1 with zero viable leads (= discovery program). A molecule can be potent but wrong for the indication.

**Example:** MgrA is a validated target, but montelukast (LogP 5.2, >99% protein-bound) is dead for intramammary use. The target is good; the molecule is wrong.

### 12. Kill Criteria Explicit With Thresholds

Every target must have explicit GO/KILL thresholds defined BEFORE deepening investigation. If you can't define what would kill the target, you don't understand it well enough to promote it.

**Example:** ClpP GO: >50% Hla suppression in bovine whole milk at <50 µM. ClpP KILL: <25% suppression at 50 µM. Define these before running the experiment.

### 13. Falsifiable Predictions

Every promoted target must have at least one falsifiable prediction that can be tested with a de-risk experiment. "This target is important" is not falsifiable. "Inhibiting ClpP will suppress Hla production by >50% in bovine CC97 isolates at <50 µM" is falsifiable.

### 14. Host Selectivity Assessed

For every pathogen-directed target, check host homology. If the target has >50% identity to the host ortholog, flag selectivity risk.

**Example:** The sea-lice RXR target had 53.2% identity to Atlantic salmon RXR at 98% query coverage — this killed it as a candidate despite elegant biology.

### 15. Resistance Logic Addressed

For every target, explicitly address how resistance could develop and whether resistance would be rapid, slow, or unlikely. Non-essential targets (like ClpP) have lower resistance pressure than essential targets — but "lower" is not "none."

**Example:** Tomatidine resistance develops via a single A17S mutation in atpE — rapid and fatal for monotherapy. This was discovered by GPT-5.4 Web during multi-model review and changed the recommendation from monotherapy to mandatory combination.

### 16. Strain Heterogeneity

For any pathogen-directed target, test or model across major strain lineages relevant to the target market. Virulence factor carriage, expression levels, and drug susceptibility can vary dramatically by clonal complex.

For S. aureus mastitis: CC97, CC151, CC479 minimum. For F. necrophorum liver abscess: subsp. necrophorum vs. funduliforme minimum. For sea lice: geographic population variation.

### 17. Virulence Axis Trade-Off Check

For any anti-virulence target that works through the agr/Rot regulatory axis, explicitly evaluate: does suppressing toxins simultaneously de-repress immune evasion factors (SpA, adhesins)?

In S. aureus: Rot represses toxins AND activates spa. RNAIII represses Rot AND represses spa. Any intervention that raises Rot or lowers RNAIII will suppress toxins but increase SpA-mediated immune evasion. This trade-off must be explicitly modeled for every anti-virulence target, with a mitigation strategy.

**Example:** This was missed in the MgrA inhibitor evaluation and only caught during manual review.

---

## Portfolio Standards (18-25)

### 18. Compartment Coverage Check

Before finalizing any target portfolio, map each target to the disease compartment(s) it addresses. If ANY compartment has ZERO coverage, flag it as a strategic gap and actively search for solutions.

**Example (mastitis):** Compartments are extracellular toxin damage, biofilm persistence, intracellular survival, immune evasion, and teat canal colonization. Three independent models identified that the entire Tier 1 was extracellular while the cure rate ceiling is set by intracellular persistence.

### 19. The 70% Pathology Reduction Test

When a portfolio is locked, run this thought experiment: if every target works perfectly, does total pathology drop ≥70%? Map each candidate to the disease stages it addresses. If coverage is <70%, identify the uncovered stage and return to solution design.

A portfolio that addresses 40% of the disease is not a portfolio — it's a partial solution masquerading as one.

**Example (mastitis):** Anti-Hla + SrtA + ClpP address ~45-65% of pathology. Without an intracellular persistence candidate, the portfolio FAILS the 70% test. Return to Phase 3 for the SCV/intracellular stage.

### 20. Don't Ignore Major Pathology Components

If a mechanism is responsible for a significant part of the disease, it MUST appear in the portfolio. No scoping out core pathology as "intractable" or "out of scope."

If intracellular SCV persistence drives 25-30% of chronic mastitis, the portfolio must address it — even if the approach is novel and high-risk. Discomfort about a gap is a signal, not permission to ignore it.

### 21. If Nothing Exists, Propose Something New

This is drug discovery, not drug selection. When the literature has no answer for a critical disease stage, design an approach from first principles. Use cross-disease analogies, emerging biology, and creative mechanism design. Then be rigorous about testing it.

**Example:** If no approach exists for intracellular SCV persistence, propose one — wake-and-kill metabolic reactivation, autophagy flux restoration, cell-penetrating peptide conjugates. All are first-principles proposals that address a real gap.

### 22. Breadth Before Depth

Seriously evaluate ≥8-10 intervention approaches before narrowing to a final portfolio of 3-5. If only 4 ideas were seriously considered, the portfolio is too narrow.

**Example:** The v8 pipeline's 50-55% alternative portfolio probability was a signal that it hadn't explored enough. If the pipeline's own assessment says the road not taken is equally likely to be correct, the portfolio is too narrow.

### 23. Combination Complexity Check

For any proposed combination product, explicitly model the regulatory trial matrix. FDA-CVM requires proof of contribution for each API. A 3-API combination = 7 trial arms minimum. A 4-API = 15 arms. If the total exceeds what is commercially justifiable, simplify to 2-API maximum or develop as separate products.

### 24. Embarrassment Pass

Before promoting any target, state the simplest plausible way it could fail in the real system. If you can't articulate the embarrassment scenario, you haven't thought hard enough.

**Example (anti-Hla):** "We optimize an Hla inhibitor, achieve perfect tissue protection, and cure rates don't change because the neutrophils are still dying from LukMF' and the bacteria persist." This is the most embarrassing plausible failure — and it directly informs experimental design.

### 25. Fallback Logic Defined

Every portfolio must have explicit fallback logic: if the lead thesis fails, what do you do? This prevents catastrophic portfolio failure.

**Example:** If anti-virulence fails, the fallback is endolysin/phage-based direct kill. If prevention fails, the fallback is resistance-orthogonal cure-side chemistry.

---

## Commercial Standards (26-31)

### 26. Commercial Reality Gate Before Tier 1

Every Tier 1 target must pass a commercial reality gate BEFORE scientific ranking:
1. Regulatory pathway? (USDA-CVB vs FDA-CVM — timeline and cost differ 10-100x)
2. COGS per dose at dairy scale? (must be <$30/treatment to be commercially viable)
3. Does the lead molecule survive the real matrix? (check LogP, protein binding, stability)
4. Single-agent or combination? (combination = 3-5x regulatory complexity)
5. Partner portfolio fit?

Targets failing the commercial gate get demoted regardless of scientific merit.

**Example:** Montelukast (LogP 5.2, >99% protein-bound) would have zero free drug in milk — killed by Gemini 3.1 Pro before we caught it.

### 27. Test in the Real Matrix

For intramammary candidates: activity must be assessed in whole milk, not broth. MIC in milk is typically 10-25x higher than MIC in media due to casein binding, fat globule adsorption, and ion antagonism.

For rumen candidates: assess stability in rumen fluid. For aquaculture: assess in seawater at relevant temperatures and salinities. Flag any candidate without matrix-specific data.

### 28. Benchmark Against Real Comparators

Don't compare novel therapeutics against untreated controls. Compare against the CURRENT standard of care. A 20% improvement over no treatment is meaningless if the farmer already has 60% improvement from existing products.

**Example (mastitis):** Benchmark against ITS (OR 0.29 for new IMI), DCT, pegbovigrastim (25-35% CM reduction). Any novel therapeutic must show benefit ON TOP of this stack.

### 29. Match Products to Partner Capabilities

Before proposing targets, map the partner's product types, M&A activity, regulatory capabilities, and distribution channels. Every proposed target must fit at least one existing capability or explicitly flag requiring a new one.

### 30. Validate Constraints With the Partner

Never accept delivery modality or product-type constraints without confirming them. Flag unconfirmed constraints: "ASSUMED CONSTRAINT — not validated with partner."

**Example:** The liver abscess pipeline killed its strongest target (leukotoxin neutralization) for a "feed-additive-only" constraint that was never confirmed — and the partner makes vaccines.

### 31. Realistic Cost Estimates

De-risk experiments involving screening cascades, recombinant protein expression, enzyme assays, or cell-based assays cost $50-100K minimum per target, not $5-8K. Either consult actual CRO pricing or omit cost estimates entirely. Fantasy budgets undermine credibility with partners who know what things cost.

---

## Process Standards (32-35)

### 32. Clean-Start Check

Before starting any new analysis phase, check: am I contaminated by prior framing? Am I favoring a conclusion because I reached it before? If three pipeline versions converge on the same answer, is that confirmation or anchoring?

**Example:** v3→v7→v8 all converged on neutrophil-metabolism as the mastitis attractor. If an alternative framing (e.g., "pathogen persistence/barrier problem") produces different output, the convergence was anchored, not confirmed.

### 33. Confirmed vs Assumed Constraints

Separate constraints validated with the partner/data from constraints that are assumed. Flag every assumed constraint explicitly.

**Example:** The "feed-additive-only" constraint for liver abscess killed the strongest target and was never confirmed with Elanco. Assumed constraints should never drive kill decisions.

### 34. Merge Integrity

If any review pass, adversarial check, or external model feedback kills or corrects a claim, that correction must propagate into ALL documents that reference the claim. No orphaned old versions.

**Example:** When amentoflavone was corrected from "increases biofilm" to "decreases biofilm by 58%," this changed the ClpP assessment in 3 documents. All must be updated.

### 35. Feedback Loop Mandatory

Every program run must capture: what was killed, what was corrected, what new search space opened, what constraints were identified, what questions remain unresolved. The next run starts smarter.

---

*35 standards. Derived from Argus (19), Kestrel (23 with overlap), Daniel's 10 operating principles, and cross-model adversarial review across mastitis, liver abscess, and sea-lice programs. Last updated: 2026-03-24.*
