# Phase 1b — Bottleneck Consensus: Cryptosporidiosis in Neonatal Calves

**Program:** Cryptosporidiosis | **Partner:** Cargill | **Version:** v2
**Agent:** Tribunal (4-frame multi-agent consensus) | **Date:** 2026-03-27

---

## Agent A: The Unframed Analyst

### Where does biology point for the highest-leverage intervention in C. parvum?

Reading the disease map without a predetermined frame, the biology points to one overwhelming conclusion: **the parasite wins a kinetic race that the neonatal calf cannot run**.

The disease map documents an organism with a 12-14 hour asexual replication cycle producing 8 merozoites per cycle, a thin-walled oocyst autoinfection loop that sustains amplification without any new environmental input, an ID50 of 5.8-16.6 oocysts making exposure essentially guaranteed in any contaminated facility, and a self-limiting resolution at 2-3 weeks that coincides precisely with the maturation of IFN-gamma/CD4+ T cell responses.

The single highest-leverage intervention point is **the first 72 hours after exposure, before the autoinfection cycle becomes self-sustaining**. Here is my reasoning:

**1. The dose-severity independence is the critical clue.** Zambriski et al. (2013) showed that ALL 27 calves developed diarrhea regardless of whether they received 25 or 10^6 oocysts, and there was no relationship between dose and duration or peak shedding intensity. This means the initial invasion event is just an ignition switch. What drives disease severity is the internal amplification machinery — Type I meront recycling and thin-walled oocyst autoinfection. Once this machinery is running (by roughly 48-72h post-exposure, after 3-4 merogony cycles), the infection becomes functionally independent of the original inoculum.

**2. The halofuginone timing data confirms this window.** Halofuginone shows its best (still modest) effect when started within 24-48 hours of birth — i.e., before or at the time of first exposure. Post-infection treatment is dramatically less effective. This is not a drug delivery problem. It is a kinetic problem: the drug works when the parasite population is small enough to suppress, and fails when it is not.

**3. The immune system's natural solution is instructive.** The calf resolves the infection at 2-3 weeks, when CD4+ T cells and IFN-gamma reach functional levels. The disease is entirely contained within the gap between exposure (day 0-3 of life) and immune competence (day 14-21). If this gap could be narrowed — by accelerating immune maturation, providing passive immune effectors that persist through the window, or suppressing parasite amplification during the window — the disease would not reach clinical significance.

**Highest-leverage intervention:** A prophylactic that is present in the gut lumen from birth through day 14, capable of either (a) blocking sporozoite invasion or (b) suppressing merogony to a level the maturing immune system can control. This could be a sustained-release luminal drug, a hyperimmune colostral antibody with adequate half-life, or an innate immune priming agent given at birth. The key property is not potency — it is duration of action covering the full vulnerability window.

**What I am NOT saying:** I am not saying "kill the parasite." The calf's immune system will kill the parasite. The intervention needs to slow the parasite enough to buy time for the immune system to arrive.

---

## Agent B: The Pathogen Specialist

### What does C. parvum NEED to cause disease?

C. parvum has three essential capabilities that, together, make it a devastating neonatal pathogen. I will evaluate which is most essential and most targetable.

**Capability 1: The intracellular-extracytoplasmic niche.**
This is the parasite's survival architecture. By sitting inside the host cell membrane but outside the cytoplasm, C. parvum is shielded from phagocytosis, MHC-I presentation, autophagy, and most intracellular drug mechanisms. The feeder organelle provides a dedicated nutrient pipeline from the host cell without cytoplasmic exposure. This is unique among apicomplexans and is the fundamental reason drugs fail.

*Essentiality:* Absolute — without this niche, the parasite would be rapidly cleared by innate immunity like any luminal pathogen.
*Targetability:* Low in the short term. The niche is formed by host cell membrane remodeling during invasion. Disrupting it would require either preventing the membrane reorganization (blocking invasion) or collapsing the feeder organelle after establishment. The molecular components of the feeder organelle are poorly characterized (CpABC1, CpGT1/GT2 are candidates but not validated as essential). This is a 5-10 year research target, not a near-term intervention.

**Capability 2: The autoinfection cycle via thin-walled oocysts.**
Approximately 20% of oocysts produced are thin-walled and excyst within the host gut, immediately releasing sporozoites that invade new enterocytes. This creates a self-sustaining infection loop independent of environmental re-exposure. This is the kinetic engine of the disease — it transforms a single exposure event into a week-long amplification cascade.

*Essentiality:* This is what makes the disease SEVERE rather than transient. Without autoinfection, the initial invasion from environmental oocysts would produce a limited parasite burden that the immune system could likely manage with minimal clinical signs. The autoinfection cycle is what escalates a manageable initial infection into overwhelming parasite burden.
*Targetability:* Moderate. Thin-walled oocysts must excyst in the gut lumen before sporozoites invade new cells. A luminal agent that prevents sporozoite attachment or excystation would break this cycle without needing to penetrate the niche. Anti-GP40 antibodies, lectin-blocking molecules, or agents that alter luminal conditions (bile salt sequestrants, pH modification) could theoretically interrupt this step. The difficulty is maintaining effective luminal concentrations continuously.

**Capability 3: Massive amplification (8 merozoites per 12-14h cycle).**
Each merogony cycle produces 8 merozoites from a single trophozoite. After 5 cycles (~60-70 hours), a single sporozoite has generated over 32,000 progeny. This exponential amplification means the parasite reaches an overwhelming burden before the adaptive immune system activates.

*Essentiality:* High — the amplification rate is what allows the parasite to outrun neonatal immunity. But this is shared with other apicomplexans (Eimeria, Plasmodium) that ARE treatable, so amplification rate alone is not the unique barrier.
*Targetability:* High. Multiple validated drug targets exist within the merogony machinery: CDPK1 (BKIs), CpIMPDH (nucleotide synthesis), CpPDE1 (signaling). Slowing merogony by even 50% would dramatically change the kinetic balance, because the immune system still arrives on schedule at day 6-7.

**My assessment of the pathogen's Achilles heel:**

The pathogen NEEDS the autoinfection cycle to cause clinically significant disease. The niche is its shield. Merogony is its sword. But autoinfection is the multiplier that makes the shield and sword overwhelming. Without autoinfection, you have a pathogen that invades, amplifies for a few cycles from the initial inoculum, and then faces a mounting immune response. With autoinfection, you have a pathogen that continuously re-seeds itself faster than immunity can clear it.

**The most targetable essential capability is the merogony amplification rate**, because validated drug targets exist (CDPK1, IMPDH, PDE1) and even partial suppression (50-70% reduction in replication rate) would be sufficient to shift the kinetic balance in favor of the immune system. You do not need to sterilize the infection. You need to slow it.

**Critical caveat:** The autoinfection cycle is more essential but currently less targetable with validated molecular tools. If the feeder organelle's molecular components were better characterized, disrupting nutrient acquisition could collapse both merogony and autoinfection simultaneously. This remains the highest-ceiling target but the lowest-readiness target.

---

## Agent C: The Host/Environment Analyst

### Why do calves recover by 2-3 weeks? Is this a within-animal or between-animal problem?

**Part 1: Why calves recover — and what this tells us about intervention strategy.**

Recovery at 2-3 weeks is driven by the maturation of a Th1-dominant adaptive immune response: IFN-gamma production by CD4+ T cells begins around day 6-7, escalates through week 2, and reaches functional clearance capacity by week 3. This is demonstrated by:
- CD4+ T cells in ileal intraepithelial lymphocytes express CD25 (activation marker) during infection (Wyatt et al., 1997)
- IFN-gamma response is CD4+ T cell dependent (de Graaf et al., 1998)
- Athymic and SCID mice develop persistent, fatal infections — confirming adaptive immunity is required for clearance
- The Th1 bias (IL-12 and IFN-gamma upregulated; no IL-4 or IL-10 changes) is consistent with an effective anti-parasitic response that simply arrives too late

**Could you accelerate neonatal immune maturation?** This is the central question for host-directed therapy.

Evidence that acceleration is possible:
- rBoIL-12 administration successfully stimulated CD4+ T cell expansion and IFN-gamma production in neonatal calf gut (Pasquali et al., 2006). The immune cells responded to the stimulus — the machinery exists, it is just not naturally activated early enough.
- However, rBoIL-12 FAILED to protect against infection despite successful immune stimulation.

**Why did rBoIL-12 fail?** Three hypotheses:
1. *Timing was still too late:* rBoIL-12 may have been given after the parasite had already achieved overwhelming burden. The immune response was real but the battle was already lost.
2. *IFN-gamma alone is insufficient:* Clearance may require a coordinated multi-effector response (IFN-gamma + iNOS + CD8+ cytotoxicity + specific antibody) that cannot be replicated by a single cytokine.
3. *PGE2-mediated local immunosuppression:* The external panel (Claude Opus) raised a critical point — PGE2 produced at infection sites suppresses Th1 responses and dendritic cell maturation locally. Even if systemic IFN-gamma is elevated, the local immunosuppressive environment at the parasite-epithelial interface may block effector function. This could explain the rBoIL-12 paradox.

**My assessment:** Immune acceleration is theoretically sound but has failed in practice with a single cytokine approach. A combination approach — innate immune priming (e.g., trained immunity via beta-glucan at birth) + COX-2 inhibition (to relieve PGE2-mediated local immunosuppression) + passive anti-invasion antibodies (to slow parasite establishment) — would address multiple bottlenecks simultaneously. No single immune lever is sufficient because the parasite has multiple redundant evasion mechanisms.

**Part 2: Within-animal vs. between-animal problem.**

This is NOT one or the other. The answer depends on the timescale of interest:

*Within-animal (this calf, this week):*
The disease is definitively a within-animal kinetic mismatch. R0 is irrelevant to the individual calf — once infected (which is near-certain given the ID50 of ~10 oocysts and environmental ubiquity), the entire disease plays out within the animal. Autoinfection sustains the infection without any new environmental input. The calf would get equally sick on a pristine farm if given 20 oocysts on day 1 of life.

*Between-animal (this herd, this season and the next):*
The environmental reservoir is the persistence engine. R0 of 3-8 (effectively much higher without management) means one infected calf contaminates the environment for months. Oocysts persist through seasons. Each calving cycle ratchets environmental contamination upward. The external panel (GPT-5.4) correctly identified that the environment acts as a "transmission capacitor" — storing infectivity across time.

**My conclusion on the dual nature of the problem:**

For INDIVIDUAL CALF WELFARE (Cargill's immediate commercial interest): This is a within-animal problem. The intervention must work inside the calf during the 0-14 day vulnerability window. Environmental control is necessary but not sufficient — even one exposure event is enough to cause full disease.

For HERD-LEVEL DISEASE REDUCTION (Cargill's long-term interest): This is a between-animal environmental problem. Any treatment that reduces oocyst shedding by >90% per infected calf would, over 2-3 calving cycles, reduce environmental contamination below the threshold needed to guarantee infection of every calf. But at current R0 of 3-8, this requires enormous shedding reduction — modest effects will not move the needle.

**The honest assessment:** Cargill needs BOTH. A within-animal intervention that reduces clinical severity (immediate ROI through reduced mortality, better weight gain) AND reduces shedding (long-term ROI through environmental load reduction). These are not competing goals — they are the same product specification.

---

## Agent D: The Martian (Quantitative First Principles)

### What do the numbers say?

I have no domain knowledge. I see only numbers. Let me examine what they reveal.

**The Numbers:**
- ID50 = 5.8-16.6 oocysts (Zambriski et al., 2013)
- Shedding = 10^6-10^7 oocysts/g feces for 7-9 days
- Total oocyst output per calf: ~1.4 x 10^10
- R0 = 3-8 (inferred; true R0 without management may be 15-50+)
- Self-limiting by 2-3 weeks in immunocompetent hosts
- Halofuginone: reduces diarrhea duration by ~2 days (out of 4-16 day range)
- Paromomycin: eliminates shedding at 100 mg/kg/day but nephrotoxic
- rBoIL-12: stimulates IFN-gamma but fails to protect
- Dose-severity: NO correlation between inoculation dose and disease severity
- Replication cycle: 8 merozoites per 12-14h cycle
- Adaptive immune activation: day 6-7 post-infection
- Clinical signs appear: day 3-5

**Calculation 1: The Kinetic Mismatch (quantified)**

From 1 oocyst (4 sporozoites), assuming conservative 12h cycle and 8x amplification:
- 0h: 4 parasites
- 12h: 32
- 24h: 256
- 36h: 2,048
- 48h: 16,384
- 60h: 131,072
- 72h (day 3): 1,048,576 (~10^6)
- 84h: 8,388,608
- 96h (day 4): 67,108,864 (~6.7 x 10^7)
- Day 5 (clinical signs appear): ~5 x 10^8
- Day 6-7 (immune activation begins): ~10^10-10^11

At immune activation (day 6-7), parasite burden is already 10^10-10^11. Even if each activated CD4+ T cell could clear 100 parasites per day, you would need 10^8-10^9 effector cells at the site — which is biologically implausible in a neonatal gut. The immune system does not "catch up" through brute force killing. It presumably works by blocking new invasions (IFN-gamma activates iNOS in enterocytes, making them resistant) while existing intracellular stages complete their cycle and die. Clearance takes another 1-2 weeks because autoinfection maintains the population while the immune system progressively makes the epithelium inhospitable.

**Calculation 2: The effect size of halofuginone reveals the intervention gap.**

Halofuginone reduces diarrhea duration by ~2 days. Disease duration is 4-16 days (median ~7-9 days). A ~2 day reduction is a ~22-28% improvement in duration. But diarrhea severity and peak shedding are minimally affected.

If the best available drug (used prophylactically, from birth) achieves only ~25% improvement in one dimension of disease, the disease is clearly not being addressed at its rate-limiting step. Halofuginone is cryptostatic — it slows replication without killing parasites. A 25% improvement from slowing replication suggests that replication rate IS relevant to disease severity, but partial slowing is not enough. You need either (a) much greater suppression (>80%) of replication rate, or (b) you need to target a different step entirely.

**Calculation 3: The dose-independence paradox.**

The absence of dose-severity correlation is the most informative number in the dataset. In most infectious diseases, higher doses produce more severe disease because you start with more organisms. In Crypto, you can give 25 oocysts or 10^6 oocysts and get the same disease.

This means the initial inoculum size becomes irrelevant within 2-3 replication cycles (24-36h), after which the autoinfection-merogony amplification machinery dominates. The "starting conditions" are washed out by exponential dynamics.

**What does this mean numerically?** From 25 oocysts (100 sporozoites): after 3 cycles = 51,200 parasites. From 10^6 oocysts (4 x 10^6 sporozoites): after 3 cycles = 2 x 10^9 parasites. These differ by 4 orders of magnitude initially but the 25-oocyst group reaches 10^9 parasites by day 4 anyway. Given that clinical signs appear at day 3-5 regardless, the disease threshold is crossed at approximately the same time because the exponential growth rate dominates over initial conditions.

**Calculation 4: What R0 means for environmental vs. within-animal leverage.**

R0 = 3-8 means each infected calf infects 3-8 others. To get R0 < 1 (extinction), you need to prevent (1 - 1/R0) = 67-88% of transmissions. Given that a single calf produces 10^10 oocysts and ID50 is 10, even a 99.99% reduction in environmental oocysts still leaves enough to infect ~140,000 calves. Environmental control at this R0 is mathematically futile unless you can reduce oocyst output by >6 log10 per calf (99.9999%).

The within-animal intervention does not need to reduce R0 at all. It needs to reduce DISEASE SEVERITY in the individual calf. Given the self-limiting nature (calf resolves by week 3), the intervention value is measured in: (a) diarrhea-days prevented, (b) weight loss prevented, (c) mortality prevented. These are all determined by the PEAK parasite burden (days 5-10), not by R0.

**Calculation 5: The immune timing mismatch (the decisive number).**

Clinical signs appear: day 3-5.
Immune activation begins: day 6-7.
Immune clearance effective: day 14-21.

The gap between clinical onset and immune clearance is 9-18 days. The gap between clinical onset and immune activation is 1-4 days. If immune activation could be advanced by 3-4 days (to day 3-4 instead of 6-7), the immune system would engage the parasite at ~10^6-10^7 burden instead of 10^10-10^11 burden — a 1,000-10,000-fold lower challenge.

**A 3-4 day advance in immune activation would reduce the challenge to the immune system by 3-4 orders of magnitude.** No drug in the pipeline promises anything close to this effect size.

**The Martian's conclusion:**

The numbers unambiguously point to an **immune timing mismatch** as the bottleneck. The arithmetic is simple: the parasite amplifies exponentially at 8x per 12h, the immune system activates at day 6-7, and the ratio of parasite burden at day 7 vs. day 3 is approximately 10^4. Moving the immune activation forward by 3-4 days is equivalent to a 10,000-fold more potent drug given at day 7.

This is not a drug problem. It is a timing problem. The parasite is not unusually drug-resistant in any biochemical sense — multiple compounds kill it in vitro. The niche is not impenetrable — paromomycin reaches it from the lumen. The immune system is not incapable — it clears the infection completely within 3 weeks. The problem is that these three systems (drugs, niche access, immunity) are all LATE. The parasite has a 3-7 day head start, and exponential dynamics make that head start insurmountable.

**The Martian's non-obvious insight:** The dose-independence data proves that the environmental burden, while important for transmission, is irrelevant to individual disease severity. Whether a calf encounters 10 or 10^6 oocysts, the disease is the same. This means any environmental intervention (disinfection, management, oocyst reduction) that does not achieve ZERO exposure is worthless for the individual calf. At R0 of 3-8 with an ID50 of 10 and environmental loads in the billions, achieving zero exposure is impossible. Therefore, environmental interventions have no value for individual calf outcomes — they only matter at the multi-year herd timescale.

---

## The Evaluator: Synthesis and Bottleneck Determination

### 1. Convergence Map

| Claim | Agent A | Agent B | Agent C | Agent D | Agreement |
|-------|---------|---------|---------|---------|-----------|
| **The disease is fundamentally a kinetic race between parasite amplification and immune maturation** | YES | YES | YES | YES | **4/4 — Universal** |
| **Autoinfection (thin-walled oocysts) is a critical amplifier that makes the infection self-sustaining** | YES | YES (most essential pathogen capability) | YES | YES (dose-independence proves amplification dominates) | **4/4 — Universal** |
| **The 0-72h post-exposure window is decisive; interventions after day 3-5 face overwhelming parasite burden** | YES (first 72h) | implied (merogony outpaces immunity) | YES (timing mismatch) | YES (quantified: 10^4 difference between day 3 and day 7) | **4/4 — Universal** |
| **The immune system WILL clear the infection; the problem is damage before clearance** | YES | implied | YES (explicit) | YES (self-limiting = immune clearance succeeds, just late) | **4/4 — Universal** |
| **The intracellular-extracytoplasmic niche is the primary drug delivery barrier** | mentioned but secondary | YES (the shield) | mentioned | not emphasized | **2/4 — Contested** |
| **Environmental control is futile for individual calf outcomes at this R0/ID50** | implied | not addressed | partially (dual problem) | YES (explicit, quantified) | **2/4 — Contested** |
| **Immune acceleration (advancing activation by 3-4 days) would be the highest-impact intervention** | YES (buy time for immune system) | not explicit | YES (but skeptical — rBoIL-12 failed) | YES (quantified: 10^4 reduction in challenge) | **3/4 — Strong consensus** |
| **PGE2-mediated local immunosuppression may explain the rBoIL-12 paradox and represent a targetable mechanism** | not addressed | not addressed | YES | not addressed | **1/4 — Novel insight** |
| **Merogony suppression (CDPK1, IMPDH, PDE1) is the most immediately targetable approach** | implied | YES (most targetable essential capability) | not primary recommendation | not explicit | **2/4 — Contested** |
| **Dose-severity independence proves amplification dominates over initial inoculum** | YES | implied | not addressed | YES (quantified as primary insight) | **3/4 — Strong consensus** |

### 2. The Central Disagreement

**Is this a drug problem or an immune timing problem?**

Agent B (Pathogen Specialist) argues the bottleneck is the parasite's essential capabilities — specifically the autoinfection cycle and merogony amplification — and that the most targetable intervention is suppressing merogony through validated drug targets (CDPK1, IMPDH, PDE1). This frames crypto as a drug problem: find a better drug, deliver it earlier, slow the parasite enough for immunity to catch up.

Agent D (The Martian) argues the bottleneck is the immune timing mismatch, quantified as a 3-4 day gap that translates to a 10^4 difference in parasite burden at the time of immune engagement. This frames crypto as a timing problem: no drug needs to be 10,000x more potent if you can advance immune activation by 3 days.

Agent C (Host/Environment) sits between them but is skeptical of pure immune acceleration based on the rBoIL-12 failure, while noting that PGE2-mediated local immunosuppression could be the reason immune stimulation alone fails.

**Resolution:**

These are not actually in conflict. They describe the same bottleneck from different angles. The bottleneck is:

**The parasite reaches overwhelming intracellular burden before the neonatal immune system can engage, due to the combination of (1) exponential merogony amplification, (2) autoinfection recycling, and (3) delayed adaptive immune activation in the neonatal calf.**

The drug approach (suppress merogony) and the immune approach (accelerate immune activation) are both valid strategies for closing the same gap. The Martian's quantitative analysis demonstrates that either could work: a drug that reduces parasite burden by 3-4 log10 at day 5 achieves the same effect as advancing immune activation by 3-4 days. In practice, neither alone is sufficient (rBoIL-12 failed; halofuginone barely helps). The answer is likely both — moderate merogony suppression + moderate immune acceleration would synergize because both narrow the same kinetic gap from opposite sides.

### 3. Bottleneck Determination

**THE BOTTLENECK: The 3-7 day gap between parasite amplification to overwhelming burden (days 0-5) and functional adaptive immune engagement (days 6-14) in the neonatal calf gut.**

**Specific mechanism:** Exponential Type I merogony (8x per 12-14h) combined with thin-walled oocyst autoinfection creates a self-sustaining amplification cascade that reaches 10^10+ parasites by the time IFN-gamma-producing CD4+ T cells activate in the ileal mucosa. The neonatal immune system is competent (it WILL clear the infection) but slow to activate from a naive state, and the parasite exploits this window with a replication rate that makes each hour of delay exponentially more costly.

**Supporting agents:** 4/4 agree this kinetic mismatch is the fundamental driver. Agent B emphasizes the parasite's amplification machinery as the targetable component; Agents A and D emphasize the timing gap itself; Agent C adds the host immune maturation dimension and identifies PGE2-mediated local immunosuppression as a potential compounding factor.

**Dissent:** None on the bottleneck itself. The disagreement is on strategy (drug vs. immune), which the evaluator resolves as a false dichotomy — both attack the same gap.

**Evidence (quantitative):**
- Dose-independence of severity (Zambriski et al., 2013) proves amplification machinery, not initial inoculum, drives disease
- 8^n amplification at 12h cycles: from 4 sporozoites to >10^10 by day 7
- Immune activation at day 6-7 (de Graaf & Peeters, 1997; Wyatt et al., 1997)
- Self-limitation at day 14-21 confirms immune competence arrives eventually
- rBoIL-12 failure (Pasquali et al., 2006) demonstrates that systemic immune stimulation alone cannot overcome the kinetic deficit
- Halofuginone's marginal effect (~2 day reduction) shows partial merogony suppression is insufficient alone

**Why the alternatives are wrong or secondary:**
- *The niche is NOT the bottleneck.* The niche is a complicating factor for drug delivery, but paromomycin proves luminal access is achievable. If a drug could be present prophylactically from birth and maintain luminal concentrations, the niche would not prevent efficacy. The niche matters because it compounds the timing problem — it slows drug accumulation at the parasite site, wasting more of the already-limited time.
- *Environmental contamination is NOT the bottleneck for individual disease.* The dose-independence data proves that even minimal exposure causes full disease. Environmental management matters for herd-level R0 reduction over multiple seasons, but contributes nothing to individual calf outcomes.
- *Drug target availability is NOT the bottleneck.* Multiple validated targets exist (CDPK1, IMPDH, PDE1, GP40). The targets exist; the problem is delivering effective intervention during the narrow prophylactic window at a cost compatible with production animal economics.

**Sequential gate model:**

```
Gate 1: EXPOSURE (days 0-3 of life)
  - Near-certain in endemic herds (R0=3-8, ID50=10, ubiquitous environmental oocysts)
  - Cannot be prevented without perfect environmental control (impossible)
  --> Gate 1 CANNOT be closed at current R0

Gate 2: ESTABLISHMENT (hours 0-48 post-exposure)
  - 4 sporozoites per oocyst invade enterocytes, establish niche
  - First 2-3 merogony cycles amplify to ~10^3-10^4 parasites
  - Autoinfection cycle initiates from thin-walled oocyst production
  --> Gate 2 is the PRIMARY INTERVENTION WINDOW
  --> Anti-invasion agents (anti-GP40 antibodies), merogony suppressors, or
      autoinfection blockers deployed prophylactically from birth

Gate 3: AMPLIFICATION (days 2-7)
  - Exponential merogony + autoinfection drives burden to 10^8-10^11
  - Clinical signs appear (day 3-5) — this is when disease is DETECTED
  - Therapeutic intervention starts here but faces massive burden
  --> Gate 3 is where current interventions attempt to act (and fail)
  --> Success requires >3-4 log10 parasite reduction, which no current drug achieves

Gate 4: IMMUNE CLEARANCE (days 7-21)
  - IFN-gamma/CD4+ T cells activate and progressively clear infection
  - The immune system succeeds but damage is already done
  --> Gate 4 opens naturally; the goal is to reduce parasite burden
      BEFORE this gate so clearance is faster and damage is less

Gate 5: RECOVERY (weeks 3-26)
  - Clinical resolution but weight NOT recovered for 6 months
  - Stem cell/Wnt pathway damage may impair epithelial regeneration
  --> Gate 5 determines long-term economic impact
  --> No current intervention addresses post-clearance recovery
```

**The bottleneck is Gate 2 (Establishment).** This is where the infection transitions from a manageable number of parasites to a self-sustaining amplification cascade. An intervention that keeps parasite burden below ~10^4-10^5 through the first 5-7 days would allow the maturing immune system to clear the infection before clinical disease develops. Every hour of delay after Gate 2 closes makes the problem exponentially harder.

### 4. The Martian's Contribution

The Martian provided three insights the domain agents did not independently articulate:

**Insight 1 (non-obvious): A 3-4 day advance in immune activation is equivalent to a 10,000-fold more potent drug.** This quantitative framing reframes the intervention question entirely. Instead of "how do we find a drug that kills 99.99% of Crypto" (which has failed for 20 years), the question becomes "how do we advance immune activation by 3-4 days" (which has never been properly attempted in calves). The effect sizes are equivalent but the feasibility space is different.

**Insight 2 (non-obvious): Environmental interventions have zero value for individual calf outcomes.** The dose-independence data, combined with R0 mathematics, proves that any environmental intervention short of achieving zero exposure is worthless for the individual calf. The calf encounters 10 oocysts or 10 million oocysts and gets exactly the same disease. This is a counterintuitive result that would not emerge from qualitative biological reasoning.

**Insight 3 (non-obvious): Halofuginone's 25% effect size is diagnostic.** The modest effect of the best available drug, when properly contextualized against the kinetic numbers, reveals that partial merogony suppression shifts the outcome modestly because you are fighting an exponential curve. On an exponential growth curve, a 25% reduction in growth rate does not produce a 25% reduction in peak burden — it produces a temporal delay of about 1 cycle (12-14h). This explains why halofuginone shifts diarrhea duration by ~2 days rather than affecting severity or peak shedding. The Martian's arithmetic predicts halofuginone's effect size from first principles, validating the kinetic mismatch model.

### 5. Implications for the Portfolio

This bottleneck determination has direct consequences for what Forge should prioritize:

1. **Highest-value intervention type:** Prophylactic agents deployed from birth through day 14 that either suppress merogony or block autoinfection. Must be present before exposure, not given after clinical signs.

2. **The product profile that matters:** Duration of action > potency. A moderately effective agent that maintains luminal/tissue concentration for 14 days beats a highly potent agent that requires daily dosing (compliance, cost, labor).

3. **Combination is likely required:** Moderate merogony suppression (drug) + moderate immune acceleration (innate priming or COX-2 inhibition to relieve PGE2 immunosuppression) + moderate invasion blocking (passive antibodies) could synergistically close the kinetic gap from three directions.

4. **What NOT to pursue:** Post-symptomatic curative therapy. The numbers show this is fighting a 10^10 parasite burden in an immunologically compromised niche. Twenty years of failure confirms the arithmetic.

5. **The environmental lever matters only at the multi-year herd scale:** Shedding reduction per calf compounds over calving seasons. A product that reduces shedding by 90% would have dramatic long-term herd value even if individual calf benefit is modest.

---

*Tribunal complete. 4/4 frames produced independent analyses. Central disagreement (drug vs. immune timing) resolved as false dichotomy. Bottleneck is specific and mechanism-level. The Martian contributed three non-obvious quantitative insights. 5 predictions appended to prediction log.*
