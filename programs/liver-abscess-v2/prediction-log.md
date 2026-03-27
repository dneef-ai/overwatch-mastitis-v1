# Prediction Log: Hepatic Abscessation in Feedlot Cattle

**Program:** Liver Abscess v2
**Phase:** 1 (Disease Map)
**Date:** 2026-03-27

---

## Prediction 1: Hindgut Contributes >20% of Hepatic F. necrophorum Seeding

**Prediction:** In feedlot cattle with liver abscesses, strain-level genomic matching will show that >20% of liver abscess F. necrophorum isolates are more closely related to colonic epithelial isolates than to ruminal epithelial isolates from the same animal.

**Basis:** Salih et al. (2025) found that colonic epithelial tissues yielded more subsp. funduliforme isolates than ruminal tissues. Fuerniss et al. (2022) showed Bacteroides (a predominantly hindgut genus) accounted for 33% of 16S reads in liver abscesses, with some abscesses being Bacteroides-dominated rather than Fusobacterium-dominated. These data suggest the hindgut is a non-trivial source.

**Test:** Matched qPCR + WGS on paired rumen epithelium, colonic epithelium, and liver abscess samples from the same animals (n >= 100) at slaughter. Strain concordance analysis via core genome MLST or SNP-based phylogenetics.

**Falsification:** If <5% of abscess isolates show closer relatedness to colonic than ruminal epithelial isolates across 100+ animals, the hindgut pathway is negligible for portfolio purposes.

**What changes if TRUE:** Rumen-only interventions (anti-adhesion at rumen wall, rumen F.n. suppression) will have an efficacy ceiling. Portfolio must include hindgut-targeted approaches. Starch overflow management becomes a critical dietary factor.

**What changes if FALSE:** Portfolio can safely focus on rumen wall colonization and portal transit as the sole intervention point. Bacteroides-dominated abscesses are an artifact or represent a rare alternate pathway not worth targeting.

**Cost:** $15--25K
**Timeline:** 6--8 weeks

---

## Prediction 2: Leukotoxin Neutralization Will Reduce Abscess Severity But Not Incidence

**Prediction:** An effective leukotoxin-neutralizing intervention (monoclonal antibody, vaccine generating >1:128 neutralizing titer, or small molecule inhibitor) will reduce the proportion of A+ (severe) abscesses by >50% but will reduce overall abscess incidence by <30%.

**Basis:** Leukotoxin is critical for immune evasion AFTER the bacteria reach the liver (Stage 4-5), not for rumen wall colonization or portal transit (Stage 2-3). Neutralizing leukotoxin should allow Kupffer cells and neutrophils to partially contain invading bacteria, reducing abscess size and severity. However, the bacteria will still reach the liver via portal blood (the translocation event is leukotoxin-independent), and some immune evasion will persist via LPS, platelet aggregation factor, and the anaerobic niche. The Centurion vaccine's reported ~40% reduction in incidence is consistent with partial but not complete protection.

**Test:** Vaccinate feedlot cattle with a leukotoxin-targeting immunogen (recombinant LktA subunit or toxoid) that generates high neutralizing titers, then compare abscess incidence AND severity distribution (A- vs A vs A+ vs A+ adhesion) at slaughter against unvaccinated controls (n >= 200 per group).

**Falsification:** If leukotoxin neutralization reduces overall incidence by >60% (comparable to tylosin), then leukotoxin is more important for early pathogenesis (colonization/transit) than currently understood, and the rate-limiting barrier analysis should be revised.

**What changes if TRUE:** Confirms that the portfolio needs BOTH a translocation-blocking intervention (Stage 2-3) AND an immune-evasion intervention (Stage 4) for comprehensive prevention. Neither alone achieves >70% coverage.

**What changes if FALSE (incidence drops >60%):** Leukotoxin neutralization alone may be sufficient as a single-target strategy. Portfolio simplifies to leukotoxin-focused approaches.

**Cost:** $80--150K (recombinant antigen production, immunization trial, slaughter monitoring)
**Timeline:** 6--9 months

---

## Prediction 3: Subsp. funduliforme-Only Abscesses Have Distinct Clinical Profile

**Prediction:** Liver abscesses caused exclusively by F. necrophorum subsp. funduliforme (without subsp. necrophorum co-infection) will be predominantly A- or A grade (small, well-organized) rather than A+ (severe), at a ratio of >3:1 compared to the severity distribution of subsp. necrophorum-containing abscesses.

**Basis:** Subsp. funduliforme produces 21-fold less leukotoxin transcript, has lower hemolytic and hemagglutinating activity, and is less virulent in mice. Pillai et al. (2021) showed that strains from severe abscesses produce significantly more leukotoxin. Subsp. funduliforme-only abscesses (16.9% of total by qPCR) should therefore cluster at the mild end of the severity spectrum if leukotoxin production is the primary determinant of abscess severity.

**Test:** In the KE#1 sampling cohort (or separately), grade all liver abscesses using the Elanco system, then perform qPCR subspecies typing. Compare severity distributions between funduliforme-only and necrophorum-containing abscesses using chi-squared or ordinal logistic regression.

**Falsification:** If funduliforme-only abscesses show the same severity distribution as necrophorum-containing abscesses (no significant difference in A+:A- ratio), then factors other than leukotoxin production level drive abscess severity (e.g., polymicrobial synergy, host factors, anatomical location).

**What changes if TRUE:** Subspecies-specific intervention becomes relevant. A strategy that selectively suppresses subsp. necrophorum while sparing funduliforme (and its lactate-fermenting role) could reduce severe abscesses without disrupting rumen ecology.

**What changes if FALSE:** Leukotoxin quantity is not the primary determinant of severity, and other virulence factors or host responses must be incorporated into target prioritization.

**Cost:** $5--10K (additional analysis on KE#1 samples -- subspecies typing + severity grading)
**Timeline:** Concurrent with KE#1 (6--8 weeks)

---

## Prediction 4: Anti-Hemagglutinin Intervention Will Reduce Rumen Wall Colonization by >50%

**Prediction:** Blocking hemagglutinin-mediated adhesion of F. necrophorum to ruminal epithelial cells (via anti-hemagglutinin antibody delivered to the rumen, or a competitive inhibitor) will reduce the concentration of F. necrophorum in ruminal epithelial tissue by >0.5 log CFU/g (a >3-fold reduction from the baseline of 4--5 log CFU/g).

**Basis:** Hemagglutinin mediates the initial adhesion of F. necrophorum to rumen epithelial cells (Kanoe & Iwaki 1987). Anti-hemagglutinin antiserum reduces bacterial attachment in vitro. All hepatic-origin subsp. necrophorum isolates are hemagglutination-positive, while only some ruminal isolates are -- suggesting hemagglutination is required for the commensal-to-pathogen transition. Blocking this adhesion should prevent the bacteria from establishing in the rumen wall, the necessary precursor to portal transit.

**Test:** Ex vivo rumen tissue explant assay: expose bovine rumen epithelial tissue (from slaughterhouse, with and without visible rumenitis lesions) to F. necrophorum subsp. necrophorum in the presence or absence of purified anti-hemagglutinin antibody or recombinant hemagglutinin as competitive inhibitor. Quantify adherent bacteria by CFU counting and fluorescence microscopy after 4h and 24h incubation.

**Falsification:** If anti-hemagglutinin treatment reduces adhesion by <25% in the ex vivo assay, then hemagglutinin is NOT the sole or primary adhesion mechanism, and other adhesins (43K OMP, FadA, OmpA) must be targeted simultaneously. The adhesion step is more redundant than hypothesized.

**What changes if TRUE:** Hemagglutinin becomes a tractable single-target for an anti-adhesion strategy (vaccine or competitive inhibitor). This would be the first specific molecular intervention targeting Stage 2.

**What changes if FALSE:** The adhesion machinery is redundant; a multi-target anti-adhesion approach (combination targeting hemagglutinin + 43K OMP + other adhesins) would be required, significantly increasing development complexity.

**Cost:** $20--40K (rumen tissue procurement, F.n. culture, antibody production, ex vivo assay)
**Timeline:** 8--12 weeks

---

## Prediction 5: Rumen Microbiome Composition (Specifically F.n. Load) Predicts Abscess Risk Better Than Rumen pH

**Prediction:** In a cohort of feedlot cattle on identical diets, the ruminal concentration of F. necrophorum subsp. necrophorum (quantified by qPCR from rumen fluid samples at the midpoint of the feeding period) will be a stronger predictor of liver abscess status at slaughter than any measure of ruminal pH (nadir, mean, time below 5.6).

**Basis:** The LASSO model by Weinroth et al. (2019) identified fecal and soil microbial communities as predictive of liver abscess prevalence (explaining 75% of variation), suggesting microbiome composition matters beyond pH alone. Not all animals with SARA develop abscesses, and some abscesses occur without documented rumenitis. If F. necrophorum load is the bottleneck (not just pH), then individual variation in rumen F.n. carriage may explain the unpredictable incidence pattern better than acidosis metrics.

**Test:** Prospective cohort study: 200 feedlot cattle on identical diets, with rumen fluid sampling via oral stomach tube at 60 and 120 DOF. Measure: (1) ruminal pH (continuous bolus or spot sampling), (2) F. necrophorum subsp. necrophorum concentration (qPCR), (3) total rumen microbiome (16S). At slaughter, record liver abscess presence and severity. Compare predictive models (logistic regression, random forest) using pH metrics alone, F.n. load alone, and combined.

**Falsification:** If ruminal pH (time below 5.6) is a stronger predictor (higher AUC-ROC) than F.n. load, then the acidosis-rumenitis pathway is truly rate-limiting and interventions should prioritize pH management over direct anti-F.n. strategies.

**What changes if TRUE:** Direct suppression or modulation of F. necrophorum (without necessarily changing diet or pH) becomes the highest-priority intervention strategy. Individual animal risk stratification based on rumen F.n. load becomes possible.

**What changes if FALSE:** The classical acidosis-rumenitis-liver abscess sequence is confirmed as the dominant pathway, and interventions should focus on preventing rumenitis rather than targeting F. necrophorum specifically.

**Cost:** $40--60K (rumen sampling logistics, continuous pH boluses, qPCR, 16S, slaughter data collection)
**Timeline:** Full feeding period (4--6 months) + 1 month analysis

---

*5 falsifiable predictions logged. All are testable with defined experimental designs, costs, and timelines. Predictions 1, 3, and part of 5 can be addressed with KE#1 sampling infrastructure.*

---

## Phase 1b -- Tribunal Bottleneck Predictions

*Source: 4-agent consensus + evaluator (2026-03-27)*
*All predictions derive from the Gate 2 (hepatic immune evasion) bottleneck determination.*

---

## Prediction T1: Portal Bacteremia Is Common -- >50% of Grain-Fed Cattle Experience Transient F. necrophorum Portal Bacteremia

**Prediction:** In feedlot cattle on high-concentrate finishing diets sampled at slaughter, >50% will have detectable F. necrophorum DNA in portal vein blood by qPCR, despite only ~21% having liver abscesses.

**Basis:** The Gate 2 bottleneck model requires that translocation (Gate 1) is common and that the liver's immune defense (Gate 2) is the step that separates affected from unaffected animals. If portal bacteremia is rare (<20% of cattle), then Gate 1 would be rate-limiting and the Tribunal's determination would be wrong. The Martian's analysis that rumenitis prevalence exceeds abscess prevalence, the Magrin 2021 finding of zero rumenitis-abscess correlation, and the liver's known capacity to clear >99% of portal bacteria all predict that transient bacteremia is frequent and usually subclinical.

**Test:** Portal vein blood sampling at slaughter from 100+ feedlot cattle on standard finishing diets. qPCR for F. necrophorum (both subspecies) and 16S amplicon sequencing. Correlate with rumenitis score and liver abscess status.

**Falsification:** If <20% of cattle have detectable portal F. necrophorum DNA, then translocation is rare and Gate 1 (barrier failure) is genuinely rate-limiting. The bottleneck determination would need revision -- the disease would be primarily a barrier failure disease, not an immune evasion disease.

**What changes if TRUE:** Confirms that the intervention priority is Gate 2 (hepatic immune defense), not Gate 1 (barrier prevention). Validates the strategy of raising the hepatic clearance threshold rather than preventing all translocation.

**What changes if FALSE:** Reverts bottleneck to Gate 1. Portfolio should prioritize anti-adhesion and barrier-strengthening approaches. Leukotoxin neutralization moves to secondary.

**Cost:** $15--25K (slaughter sampling + qPCR + 16S)
**Timeline:** 6--8 weeks

---

## Prediction T2: Leukotoxin Neutralization Raises the Hepatic Clearance Threshold by >=1 log

**Prediction:** In an ex vivo bovine liver perfusion model, the minimum bacterial inoculum (F. necrophorum subsp. necrophorum) required to establish viable bacterial foci at 24h will be at least 10-fold higher (>=1 log CFU/mL) when anti-leukotoxin polyclonal serum is added to the perfusate compared to bacteria alone.

**Basis:** The Tribunal's bottleneck determination places leukotoxin as the binary switch between clearance and abscess establishment. If neutralizing leukotoxin raises the clearance threshold significantly, it confirms that leukotoxin is the factor that overwhelms Kupffer cell defense. The Claude Opus external panel proposed this exact experiment with detailed design (ex vivo liver perfusion, dose-response inocula from 10^2 to 10^6 CFU/mL). The Saginala 1997 vaccine trial (leukotoxoid: 5/5 controls vs 1/5 vaccinated) provides in vivo support.

**Test:** Ex vivo perfused bovine liver model (n=20 livers from slaughter). Portal vein inoculation with defined F. necrophorum concentrations (10^2 to 10^6 CFU/mL) with and without anti-LktA serum. 24h biopsies for bacterial quantification, Kupffer cell viability (CD68 + TUNEL), and early stellate cell activation (alpha-SMA).

**Falsification:** If anti-leukotoxin serum raises the threshold by <0.5 log (less than 3-fold), then leukotoxin is not the dominant clearance determinant. Other virulence factors (LPS, complement evasion, biofilm) are more important than leukotoxin for initial establishment, and a vaccine strategy must be multicomponent.

**What changes if TRUE:** Leukotoxin neutralization alone is a viable single-target strategy. Vaccine design focuses on maximizing anti-LktA titer. The 40% field efficacy of historical vaccines was likely due to insufficient titer, not wrong target.

**What changes if FALSE:** Leukotoxin is a severity modifier (affecting A- vs A+) but not the establishment gate. Portfolio must pursue multi-target approaches (LktA + adhesion blockade + complement enhancement).

**Cost:** $15--18K (as detailed in Claude Opus external panel estimate)
**Timeline:** 8--12 weeks

---

## Prediction T3: Pen-Level Abscess Prevalence Correlates with Dominant F. necrophorum Strain Leukotoxin Production

**Prediction:** In a multi-pen feedlot cohort, the mean leukotoxic activity of F. necrophorum strains isolated from rumen fluid will positively correlate with pen-level liver abscess prevalence at slaughter, with r >= 0.5 (explaining >=25% of pen-level variance).

**Basis:** The Martian identified that 75% of abscess prevalence variance is at the pen level (Weinroth 2019) and inferred this reflects strain virulence ecology. If high-leukotoxin strains dominate certain pens' microbiomes, those pens should have higher abscess rates. This is the pen-level corollary of the individual-level leukotoxin-severity correlation (Pillai 2021). No study has directly tested this relationship.

**Test:** Sample 20+ pens (10+ cattle per pen) at a single feedlot on the same diet. Collect rumen fluid via oral stomach tube at mid-feeding period. Isolate F. necrophorum, quantify leukotoxic activity (cytotoxicity assay on bovine PMNs). At slaughter, record liver abscess prevalence and severity per pen. Correlate mean leukotoxic activity per pen with pen-level abscess prevalence.

**Falsification:** If r < 0.2 (leukotoxic activity explains <4% of pen-level variance), then the pen-level signal is driven by something other than strain virulence -- likely management factors, social dynamics (bunk competition), or non-leukotoxin microbial ecology. The bottleneck determination would still hold (Gate 2 is rate-limiting at the individual level) but the pen-level epidemiology would require a different explanation.

**What changes if TRUE:** Opens a pen-level intervention strategy: microbiome engineering to displace high-leukotoxin strains. Also validates strain-level screening as a risk assessment tool.

**What changes if FALSE:** Pen-level variance is driven by translocation frequency (Gate 1 variation between pens) rather than strain virulence (Gate 2 variation). Intervention strategy shifts toward pen-level management of barrier integrity.

**Cost:** $25--40K (rumen sampling, F.n. isolation + leukotoxin assay, slaughter data)
**Timeline:** Full feeding period (4--6 months) + 2 months lab/analysis

---

## Prediction T4: Cattle with Abscesses but WITHOUT Rumenitis Carry Higher-Leukotoxin Strains

**Prediction:** Among cattle with liver abscesses, those with NO visible rumenitis at slaughter will have abscess F. necrophorum isolates with significantly higher leukotoxic activity (P < 0.05) than those with concurrent rumenitis.

**Basis:** The Tribunal's model predicts that abscess formation requires either (a) high inoculum from severe barrier failure OR (b) low inoculum from mild/healed barrier failure with a hyper-virulent (high leukotoxin) strain that overwhelms even small-inoculum Kupffer cell defense. Animals without visible rumenitis who still have abscesses must have overcome Gate 2 despite a low-magnitude Gate 1 breach -- implying their strains compensated with extreme immune evasion capability. This is a direct test of the two-gate interaction model.

**Test:** At slaughter, score rumen for visible rumenitis (present/absent) and liver for abscesses (present/absent, grade). From cattle with abscesses, isolate F. necrophorum from abscess material. Stratify by rumenitis status. Compare leukotoxic activity between groups (cytotoxicity assay on bovine PMNs).

**Falsification:** If there is no difference in leukotoxin production between the two groups (or if rumenitis-absent/abscess-present cattle have LOWER leukotoxin strains), then the two-gate interaction model is wrong. Abscess formation without rumenitis would require an alternative explanation (e.g., hindgut pathway, chronic subclinical barrier defects not visible at slaughter).

**What changes if TRUE:** Confirms that leukotoxin potency can compensate for reduced translocation -- the strongest possible evidence that Gate 2 is the bottleneck. Also identifies a "hyper-virulent" strain phenotype that should be the primary vaccine target.

**What changes if FALSE:** The rumenitis-absent/abscess-present cases may represent a distinct disease pathway (hindgut origin, healed rumenitis) that doesn't fit the two-gate model.

**Cost:** $10--15K (can be run as add-on to KE#1 sampling; rumen scoring + abscess isolate leukotoxin assay)
**Timeline:** Concurrent with KE#1 (6--8 weeks) + 4 weeks assay

---

## Prediction T5: Anti-LktA IgG Concentration in Hepatic Sinusoidal Blood Is the Critical Variable for Vaccine Efficacy

**Prediction:** In cattle vaccinated with a leukotoxoid, the concentration of anti-LktA IgG in portal/hepatic venous blood (not systemic serum) will be the variable that best predicts protection against liver abscesses (AUC-ROC > 0.75), and will be a stronger predictor than systemic serum anti-LktA titer.

**Basis:** The Claude Opus external panel noted that previous vaccines generated systemic antibodies, but the critical defense is local -- in the hepatic sinusoids. Systemic IgG may not reach effective sinusoidal concentrations fast enough. If sinusoidal anti-LktA IgG is the determinant, this explains why field vaccines with moderate systemic titers fail: the correlation between systemic titer and sinusoidal concentration may be weak. This prediction tests whether vaccine failure is a titer/localization problem rather than a target selection problem.

**Test:** Vaccinate feedlot cattle (n=50+) with leukotoxoid at entry. At slaughter, collect both systemic blood (jugular) and hepatic venous blood (from the liver during processing). Measure anti-LktA IgG by ELISA in both compartments. Correlate each with liver abscess status (present/absent, grade). Compare predictive accuracy using ROC analysis.

**Falsification:** If systemic serum anti-LktA titer predicts protection equally well or better than hepatic venous concentration (i.e., no sinusoidal-specific effect), then the vaccine failure problem is simply insufficient immunogenicity, not wrong localization. Higher-dose or better-adjuvanted systemic vaccines should work.

**What changes if TRUE:** Vaccine development must focus on hepatic/mucosal immune responses, not just systemic titer. Adjuvant selection, route of administration (oral/mucosal vs injectable), and booster timing all need re-evaluation for hepatic IgG delivery. This explains why Centurion was inconsistent -- it generated variable sinusoidal penetration.

**What changes if FALSE:** Vaccine development is simpler than feared. The problem was just dose/adjuvant/immunogenicity. A more potent systemic vaccine with higher titers should succeed.

**Cost:** $30--50K (vaccination program + dual-compartment sampling + ELISA)
**Timeline:** Full feeding period (4--6 months) + 2 months analysis

---

*5 Tribunal bottleneck predictions appended. All derive from the Gate 2 determination. T1 and T4 are the most decisive -- if T1 is falsified (portal bacteremia is rare), the entire bottleneck determination reverses. T2 provides the mechanistic proof. T3 and T5 guide intervention strategy.*

---

## Phase 2 -- Sapper Failure Analysis Predictions

*Source: Sapper treatment archaeology (2026-03-27)*
*All predictions derive from the failure analysis of 13 intervention approaches, interpreted through the Gate 2 bottleneck framework.*

---

## Prediction S1: Tylosin's Efficacy Is Partially Immunomodulatory -- Antimicrobial Action Alone Accounts for <60% of Its Effect

**Prediction:** A non-macrolide antimicrobial with equal or greater F. necrophorum suppression in the rumen (measured by qPCR: equivalent log reduction in rumen F.n. concentration) but WITHOUT macrolide immunomodulatory properties will achieve <60% of tylosin's liver abscess reduction effect (i.e., <24-42% reduction vs tylosin's 40-70%).

**Basis:** The failure analysis reveals the "3-mechanism puzzle": tylosin's superiority over broader-spectrum CTC cannot be explained by antimicrobial action alone. Chlortetracycline achieves ~40% reduction (the low end of tylosin's range) despite broader spectrum. If we subtract the antimicrobial component (which CTC matches or exceeds), the residual effect (~0-30 percentage points) represents tylosin's immunomodulatory and microbiome-restructuring contributions. Macrolides suppress NF-kB, IL-1/IL-6/IL-8/TNF-alpha, and modulate neutrophil function -- effects that are absent from tetracyclines and streptogramins. Abbas & Keel (2020) showed NF-kB is downregulated in rumen epithelium of cattle with abscesses, consistent with tylosin restoring this pathway.

**Test:** Compare tylosin (macrolide, 60-90 mg/hd/d) head-to-head with a non-macrolide compound that achieves equivalent rumen F.n. suppression (verified by qPCR at week 4, 8, 12 of feeding). Candidate: a Fusobacterium-specific bacteriophage cocktail or anti-F.n. peptide. N >= 200/group. Measure liver abscess incidence and severity at slaughter.

**Falsification:** If the non-macrolide compound matches tylosin's efficacy (>90% of tylosin's abscess reduction despite no immunomodulatory activity), then the immunomodulatory hypothesis is wrong and tylosin's action is purely antimicrobial. Forge should focus solely on F.n. suppression without needing to replicate immunomodulation.

**What changes if TRUE:** Any tylosin replacement must include an immunomodulatory component. A "direct replacement" strategy (pure antimicrobial) will underperform. This constraints Forge toward multi-mechanism approaches or macrolide-adjacent molecules.

**What changes if FALSE:** Tylosin replacement simplifies to finding a non-AMR compound with equivalent F.n. suppression. Phage therapy, antimicrobial peptides, or competitive exclusion organisms become viable standalone strategies.

**Cost:** $80-120K (matched compound development/sourcing + feedlot trial + rumen qPCR + slaughter data)
**Timeline:** 6-9 months

---

## Prediction S2: Combining Gate 1 + Gate 2 Interventions Will Achieve >80% Liver Abscess Reduction -- Exceeding Either Alone

**Prediction:** A combination of (a) a non-antibiotic inoculum reducer targeting Gate 1 (anti-adhesion or rumen F.n. suppression, achieving >=0.5 log reduction in rumen wall F.n. concentration) with (b) a leukotoxin-neutralizing vaccine targeting Gate 2 (generating anti-LktA titer >=1:128) will reduce liver abscess incidence by >80% on high-grain finishing diets -- exceeding the individual effect of either component alone.

**Basis:** The failure analysis reveals that Gate 1-only interventions (SCFP, essential oils, DFMs = 0% effect; tylosin = 40-70%) and Gate 2-only interventions (Fusogard = 0-40% on grain; KSU leukotoxoid = 80% in challenge models only) each have ceilings. Fusogard fails on grain because the Gate 1 inoculum overwhelms vaccine-enhanced Gate 2 immunity. Tylosin succeeds partially by reducing inoculum below the Gate 2 threshold but cannot eliminate all translocation. A combination that BOTH reduces inoculum AND raises the clearance threshold should produce a multiplicative effect: the reduced inoculum is now far below the elevated threshold, yielding near-complete prevention.

**Test:** Feedlot trial (n >= 150/group, 3 groups): (a) Gate 1 intervention alone, (b) Gate 2 vaccine alone, (c) Gate 1 + Gate 2 combination. All groups on high-grain finishing diet with monensin. Measure liver abscess incidence and severity at slaughter.

**Falsification:** If the combination achieves <50% reduction (i.e., no better than tylosin alone), then either (a) the two-gate model is wrong, (b) the individual components are too weak, or (c) there is an unrecognized third gate limiting prevention. The two-gate model would need revision.

**What changes if TRUE:** The optimal portfolio structure is confirmed: one Gate 1 component + one Gate 2 component. Forge should prioritize combination approaches over single-target ones. The commercial product is a two-component preventive system.

**What changes if FALSE:** The disease is more complex than the two-gate model predicts. Additional mechanisms (polymicrobial synergy, hindgut pathway, host genetics) may impose ceilings that two-target approaches cannot breach.

**Cost:** $200-400K (vaccine production + anti-adhesion/suppression compound + 3-arm feedlot trial)
**Timeline:** 12-18 months

---

## Prediction S3: SCFP (Diamond V) Combined with a Gate 2 Vaccine Will Outperform SCFP Alone by >40 Percentage Points

**Prediction:** SCFP (Diamond V Original XPC or NaturSafe) combined with a leukotoxin-neutralizing vaccine will reduce liver abscess incidence by >=40% on high-grain finishing diets, despite SCFP alone having ZERO effect.

**Basis:** SCFP's zero effect (n > 4,689) proves that rumen condition improvement (Gate 1) alone does not prevent abscesses. However, SCFP may still contribute meaningful support IF Gate 2 is simultaneously addressed: SCFP stabilizes rumen pH (reduces severity of barrier failure episodes), reduces translocation event magnitude, and provides beta-glucan immune stimulation. These benefits are invisible when Gate 2 is unaddressed (because the bottleneck is downstream) but could become additive when a vaccine raises the Gate 2 threshold. The SCFP would reduce the inoculum volume, and the vaccine would raise the clearance threshold -- together crossing a threshold that neither achieves alone.

**Test:** 2x2 factorial design (n >= 100/group): SCFP alone, vaccine alone, SCFP + vaccine, control. All on high-grain finishing diet with monensin. Measure liver abscess incidence and severity at slaughter.

**Falsification:** If SCFP + vaccine performs no better than vaccine alone (i.e., SCFP adds zero additional benefit even when Gate 2 is addressed), then SCFP's rumen benefits genuinely contribute nothing to liver abscess prevention at any gate. Gate 1 improvement is irrelevant even as a support.

**What changes if TRUE:** Existing commercial products (SCFP) that have "zero effect" on liver abscesses may have hidden value as companions to Gate 2 interventions. This changes the commercial landscape -- SCFP becomes a portfolio component rather than a failed standalone.

**What changes if FALSE:** Gate 1 improvement is truly irrelevant. The entire lever is at Gate 2. Portfolio simplifies to Gate 2-focused approaches only.

**Cost:** $150-250K (4-arm feedlot trial + vaccine production)
**Timeline:** 12-18 months

---

## Prediction S4: F. necrophorum Tannase Activity Limits Tannin Blend Efficacy at the Rumen Wall

**Prediction:** F. necrophorum subsp. necrophorum possesses tannase activity that degrades quebracho and/or chestnut tannins at concentrations that reduce the local antimicrobial effect by >=50% at the rumen epithelial surface within 4 hours of exposure.

**Basis:** The failure analysis identified that tannin blends (Silvafeed BX) achieve partial liver abscess reduction with monensin but are inferior to MON+TYL by ~10 percentage points. A key unanswered question is why tannins underperform. The closely related species Fusobacterium nucleatum produces highly active tannase (Springer Nature 2018). If F. necrophorum has similar activity, it would degrade tannins at exactly the location where antimicrobial action is most needed -- the rumen wall colonization site where F. necrophorum concentrates. This would create a "zone of tannin destruction" around the pathogen, explaining why tannins work systemically (enough diffuse antimicrobial effect to partially reduce F.n. load) but cannot match the direct antimicrobial suppression of tylosin.

**Test:** In vitro tannase assay: incubate F. necrophorum subsp. necrophorum (ATCC 25286 and 3 clinical feedlot isolates) with quebracho tannin extract and chestnut tannin extract (at concentrations matching Silvafeed BX inclusion rates) for 1, 4, 8, and 24 hours. Measure tannin degradation by Folin-Ciocalteu assay and HPLC. Positive control: F. nucleatum (known tannase producer). Compare with and without F. necrophorum to determine degradation rate.

**Falsification:** If F. necrophorum shows <10% tannin degradation at 24 hours (no meaningful tannase activity), then tannin resistance is not the explanation for the efficacy gap. The gap would more likely be due to insufficient direct antimicrobial potency of tannins versus F. necrophorum, or the missing immunomodulatory effect that tylosin provides.

**What changes if TRUE:** Tannin-based approaches have an intrinsic ceiling because the target pathogen degrades the active agent. Forge should either develop tannase-resistant tannin derivatives or pursue non-tannin Gate 1 approaches. Explains the 10-point gap between MON+BX and MON+TYL.

**What changes if FALSE:** Tannin blends underperform for other reasons (insufficient concentration, wrong antimicrobial spectrum, missing immunomodulation). Optimization of existing tannin products may still narrow the gap to tylosin.

**Cost:** $5-10K (bacterial culture + tannin substrates + Folin-Ciocalteu + HPLC)
**Timeline:** 4-6 weeks

---

## Prediction S5: The Fusogard Forage-vs-Grain Differential Is Explained by Inoculum Volume, Not Antibody Titer

**Prediction:** In cattle vaccinated with a leukotoxoid, the anti-LktA antibody titer at slaughter will NOT differ significantly between cattle on forage diets (where the vaccine works) and cattle on high-grain diets (where it fails). The failure on grain is due to higher bacterial inoculum volume overwhelming fixed antibody titers, not to reduced antibody production on grain diets.

**Basis:** The failure analysis identifies the Fusogard forage-vs-grain differential as the most informative data point. Two competing explanations exist: (a) grain-fed cattle produce lower antibody titers (perhaps due to SARA-associated immune suppression), meaning the vaccine fails because of reduced host response; or (b) antibody titers are equivalent, but the inoculum is higher, and the vaccine-enhanced defense is overwhelmed by volume. If (a), then improving immunogenicity (better adjuvant, higher dose, booster schedule) could solve the problem. If (b), then no vaccine improvement can succeed alone -- inoculum reduction (Gate 1) must accompany vaccination (Gate 2). This prediction tests the fundamental strategic question: is the failure a vaccine problem or a volume problem?

**Test:** Vaccinate matched cohorts of cattle with identical leukotoxoid formulation and schedule. Place half on forage finishing (backgrounding diet, low abscess risk) and half on high-grain finishing (standard feedlot, high abscess risk). At slaughter: measure anti-LktA IgG titer (ELISA), liver abscess incidence and severity, and quantify portal bacteremia (portal blood qPCR for F.n., if technically feasible). Compare titers between groups.

**Falsification:** If grain-fed cattle have significantly lower anti-LktA titers (>2-fold lower) than forage-fed cattle, then SARA-associated immunosuppression is the primary explanation. A more immunogenic vaccine (better adjuvant, alternative route, booster during feeding period) could potentially restore field efficacy without Gate 1 combination.

**What changes if TRUE:** Confirms the "firehose problem" -- the vaccine works but the inoculum volume is too high. This MANDATES a combination strategy (Gate 1 + Gate 2). No vaccine-only approach will succeed on grain diets. Portfolio must be a combination product.

**What changes if FALSE:** Opens a path for vaccine-only solutions. Improved immunogenicity (novel adjuvant, prime-boost schedules, mucosal delivery) could solve the grain-diet failure without needing a Gate 1 companion. Simplifies the product to a single injection.

**Cost:** $40-60K (vaccination + split diet management + slaughter sampling + ELISA)
**Timeline:** Full feeding period (4-6 months) + 2 months analysis

---

*5 Sapper failure analysis predictions appended. S1 resolves tylosin's mechanism (critical for replacement strategy). S2 tests the core portfolio thesis (Gate 1 + Gate 2 combination). S3 rescues "zero-effect" products as potential companions. S4 is a cheap, fast de-risk on tannin biology. S5 determines whether the Fusogard failure is a vaccine problem or a volume problem -- the most strategically decisive prediction in the set.*

---

## Phase 3 -- Forge Candidate Predictions

*Source: Forge candidate proposals (2026-03-27)*
*All predictions derive from specific candidates and test their key biological assumptions.*

---

## Prediction F1: Anti-LktA Monoclonal Antibody Will Raise the Hepatic Clearance Threshold by >=2 log in Ex Vivo Perfusion

**Prediction:** In the ex vivo bovine liver perfusion model (Prediction T2 design), adding a purified anti-LktA monoclonal antibody to the perfusate at 10 ug/mL will raise the minimum F. necrophorum inoculum required for viable bacterial foci at 24h by >=2 log CFU/mL compared to perfusate without antibody. The mAb will outperform polyclonal anti-LktA serum (predicted 1 log shift in T2) because monoclonal antibodies have higher avidity and consistent neutralizing potency.

**Basis:** Candidate G2-1 (anti-LktA mAb) is the top-ranked candidate. Its entire value proposition rests on whether direct antibody delivery achieves a larger clearance threshold shift than vaccine-induced polyclonal antibodies. The mAb bypasses immunogenicity variance, guarantees titer, and should achieve higher sinusoidal concentrations than endogenous IgG. If the shift is >=2 log, then even the high bacterial inocula on grain diets (~10^4-10^5 CFU per translocation event) would be below the clearance threshold, explaining why Fusogard (lower polyclonal titer) failed on grain but a mAb could succeed.

**Test:** Same ex vivo liver perfusion design as T2, with additional arm: perfuse with bacteria + purified anti-LktA mAb at 1, 10, and 100 ug/mL (dose-response). Compare threshold shift to polyclonal serum (T2 arm) and no-antibody control.

**Falsification:** If the mAb achieves <1 log threshold shift (similar to or less than polyclonal serum), then the problem is not titer/avidity -- it is something else entirely (complement evasion, biofilm formation, other virulence factors). The mAb candidate would be de-prioritized in favor of multi-target approaches.

**What changes if TRUE:** G2-1 becomes the lead candidate. Proceed directly to in vivo cattle trial with anti-LktA mAb (single injection at feedlot arrival). The dose-response data defines the target sinusoidal concentration for mAb formulation.

**What changes if FALSE:** Leukotoxin neutralization alone is insufficient even at maximal antibody concentration. The disease requires multi-mechanism intervention. De-prioritize single-target mAb; escalate combination approaches (COMBO-1, COMBO-2).

**Cost:** $18-22K (adds mAb production to the T2 experimental design)
**Timeline:** 10-14 weeks

---

## Prediction F2: mRNA-LNP LktA Vaccine Will Generate >=10x Higher Anti-LktA Titers Than Historical Fusogard in Cattle

**Prediction:** An mRNA-LNP construct encoding the three immunodominant LktA epitope regions (PL1, PL3, PL4) will generate peak serum anti-LktA neutralizing titers >=10-fold higher than those reported for formalin-inactivated leukotoxoid (Fusogard) at the same timepoint post-vaccination in feedlot cattle. Specifically: peak neutralizing titer >=1:1,280 at 4-6 weeks post-second dose, vs historical Fusogard titers of ~1:64-1:128.

**Basis:** Candidate G2-2 (mRNA LktA vaccine) is ranked #2. Its advantage over Fusogard rests on two claims: (1) mRNA vaccines generate dramatically higher antibody titers than protein/toxoid vaccines (demonstrated in human COVID-19 trials: mRNA produced 10-100x higher titers than inactivated virus or protein subunit vaccines), and (2) LNP hepatotropism concentrates antigen presentation in the liver. If this titer advantage translates to veterinary use, the Fusogard "firehose problem" may be solvable by brute-force titer elevation alone.

**Test:** Manufacture mRNA-LNP encoding PL1+PL3+PL4 fusion construct (Medgene collaboration). Vaccinate 15 feedlot cattle (prime at arrival, boost at 28 days). Measure serum anti-LktA IgG and neutralizing titer at weeks 2, 4, 6, 8, 12, 16, 20. Compare to published Fusogard titer data. Also measure anti-LktA IgG in hepatic venous blood at slaughter (to test hepatotropism hypothesis).

**Falsification:** If mRNA vaccine titers are <3x higher than historical Fusogard titers, then the mRNA platform advantage does not translate to this antigen. Either the LktA epitopes are inherently poorly immunogenic (possible given the protein's unique structure with no homologs), or the mRNA construct design is suboptimal. Would require redesign before further investment.

**What changes if TRUE:** G2-2 becomes a strong lead vaccine candidate. Proceed to challenge trial. The titer data combined with hepatic venous IgG levels would determine whether titer alone is sufficient or whether hepatotropic delivery is the key advantage.

**What changes if FALSE:** mRNA platform may not solve the LktA immunogenicity problem. Shift investment to G2-1 (mAb -- guaranteed titer, no immunogenicity variance) and G2-3 (adjuvant-focused subunit vaccine with ISCOMATRIX).

**Cost:** $35-50K (mRNA construct design + manufacturing + 15-head cattle immunogenicity trial)
**Timeline:** 16-20 weeks

---

## Prediction F3: F. necrophorum Phages phiKSUM and phiBB Will Survive in the Bovine Rumen for >=8 Hours and Reduce F.n. Concentration by >=0.5 Log

**Prediction:** When administered via rumen fistula at 10^9 PFU into grain-fed cattle, obligately lytic phages phiKSUM and phiBB will be recoverable at >=10^5 PFU/mL of rumen fluid at 8 hours post-administration, and F. necrophorum subsp. necrophorum concentration in rumen fluid will decrease by >=0.5 log CFU/mL compared to pre-administration baseline.

**Basis:** Candidate G1-2 (phage cocktail) is ranked #5. The Gemini external panel declared phage therapy a "commercial dead-end" due to rumen pharmacokinetics. This prediction directly tests whether that assessment is correct. Schwarz et al. (2024) isolated phiKSUM and phiBB from rumen fluid, demonstrating that phages can exist in the rumen environment. The question is whether they can persist at therapeutically relevant concentrations after controlled administration.

**Test:** Administer phiKSUM + phiBB (10^9 PFU each) to 4 rumen-fistulated cattle on high-grain diets. Sample rumen fluid at 0, 1, 4, 8, 24h. Quantify phage (plaque assay on F. necrophorum lawns) and F. necrophorum (qPCR). Secondary: sample rumen epithelial biopsies at 24h for adherent F. necrophorum (qPCR).

**Falsification:** If phage titers drop below 10^3 PFU/mL by 4h (>4 log reduction) and F. necrophorum concentration does not change, then the rumen pharmacokinetic problem is real and continuous in-feed delivery at very high phage concentrations would be required. This is still feasible (phage production in bioreactors is cheap) but changes the economics significantly.

**What changes if TRUE:** Phage survives in the rumen and reduces F. necrophorum. Proceed to continuous in-feed phage delivery trial (daily dosing, 14-day period, measure sustained F.n. suppression). The phage becomes a viable non-antibiotic Gate 1 component for COMBO-1.

**What changes if FALSE (phage unstable):** Phage requires protective encapsulation for rumen delivery (alginate coating, pH-responsive capsules). This adds manufacturing complexity and cost. Alternatively, phage may be better suited for hindgut delivery (more stable at hindgut pH) -- repositioning G1-2 as a hindgut-targeted intervention (G1-5 synergy).

**Cost:** $15-20K (phage production + fistulated cattle access + sampling + assays)
**Timeline:** 6-8 weeks

---

## Prediction F4: LktB POTRA2 Domain Has a Druggable Binding Pocket Identifiable by AlphaFold3 + Virtual Screen

**Prediction:** AlphaFold3 structure prediction of the F. necrophorum LktB protein will reveal a POTRA2 domain with a defined binding pocket (pocket volume >=200 cubic angstroms, druggability score >=0.5 by fpocket or SiteMap) that can be targeted by virtual screening. At least 3 of the top 20 virtual screen hits will reduce supernatant leukotoxic activity by >=50% in a cell-free F. necrophorum culture assay at 10 uM concentration.

**Basis:** Candidate G2-4 (LktB secretion inhibitor) is the highest-IP novel target in the portfolio. LktB contains a POTRA2 polypeptide transport-associated domain responsible for LktA substrate recognition and secretion. No structure exists. However, POTRA domains in homologous two-partner secretion systems have been crystallized (e.g., FhaC in Bordetella pertussis -- PDB: 2QDZ), showing well-defined beta-barrel + POTRA architecture with identifiable binding pockets.

**Test:** (1) AlphaFold3 prediction of full-length LktB. (2) Extract POTRA2 domain coordinates. (3) Druggability assessment via fpocket + SiteMap. (4) If druggable: virtual screen of Enamine REAL library (10M compounds) using Glide SP + MM-GBSA rescoring. (5) Order top 20 compounds. (6) Test in vitro: grow F. necrophorum with each compound at 10 uM, measure supernatant leukotoxic activity at 24h (bovine PMN cytotoxicity assay).

**Falsification:** If (a) AlphaFold3 confidence (pLDDT) for the POTRA2 domain is <50 (unreliable prediction), or (b) no pocket with druggability score >=0.3 is identified, or (c) zero hits reduce leukotoxic activity by >=25%, then LktB is not a tractable small molecule target. De-prioritize G2-4 and redirect small molecule effort toward G2-5 (lktA transcription).

**What changes if TRUE:** First-in-class anti-virulence small molecule against F. necrophorum. Highest patentability in the portfolio. Proceed to medicinal chemistry optimization (potency, selectivity, rumen stability).

**What changes if FALSE:** LktB is undruggable. Shift small molecule efforts to lktA transcriptional regulation (G2-5) or the unidentified LktA receptor (G2-6, after receptor ID).

**Cost:** $12-18K (AlphaFold3 free; virtual screen computational cost ~$2K; compound purchase + in vitro assays ~$10-16K)
**Timeline:** 12-16 weeks

---

## Prediction F5: Parenteral Beta-Glucan Pre-Treatment Will Increase Bovine Kupffer Cell Resistance to LktA by >=2-Fold

**Prediction:** Bovine Kupffer cells pre-treated with particulate beta-glucan (100 ug/mL for 7 days in vitro) will show >=2-fold higher LD50 for purified LktA (measured by LDH release assay) compared to untreated Kupffer cells. Additionally, trained Kupffer cells will show >=50% higher phagocytic capacity (fluorescent bead uptake) and >=2-fold higher TNF-alpha production upon F. necrophorum challenge.

**Basis:** Candidate G2-7 (Kupffer cell trained immunity) proposes that beta-glucan-induced epigenetic reprogramming can protect Kupffer cells from leukotoxin killing. Adams et al. (2024) demonstrated that beta-glucan protects against sepsis-induced KC loss by inhibiting NLRP3/GSDMD pyroptosis and promoting self-renewal. However, LktA kills via a different mechanism (concentration-dependent apoptosis at low dose, necrosis at high dose -- Narayanan 2002). The key question is whether trained immunity protects against LktA's SPECIFIC killing mechanism, not just pyroptosis.

**Test:** Isolate Kupffer cells from fresh bovine livers (slaughterhouse, collagenase perfusion). Culture with or without particulate beta-glucan (100 ug/mL) for 7 days. Then challenge with purified LktA at graded concentrations (0.1, 1, 10, 100 ug/mL). Measure: LDH release (cytotoxicity), Annexin V/PI (apoptosis vs necrosis), phagocytic capacity, TNF-alpha, and survival at 24h. Compare trained vs naive KC dose-response curves.

**Falsification:** If trained Kupffer cells show <1.5-fold improvement in LD50 (essentially equivalent sensitivity to LktA as naive cells), then trained immunity does NOT protect against leukotoxin's killing mechanism. The Sapper analysis was correct: "an activated Kupffer cell killed by leukotoxin is just as dead as a resting one." De-prioritize G2-7.

**What changes if TRUE:** Opens a novel host-side intervention axis at Gate 2 that does not require antibodies. A single injectable beta-glucan particle formulation at feedlot arrival could prime Kupffer cells for the entire feeding period (trained immunity effects last months). This would complement antibody-based approaches (G2-1, G2-2) by providing a mechanistically distinct layer of protection.

**What changes if FALSE:** Kupffer cell protection against leukotoxin requires SPECIFIC anti-LktA antibodies, not non-specific immune priming. Focus all Gate 2 investment on antibody-generating approaches (mAb, mRNA vaccine, subunit vaccine).

**Cost:** $8-12K (bovine KC isolation + beta-glucan + LktA purification + cytotoxicity assays)
**Timeline:** 8-10 weeks

---

*5 Forge candidate predictions appended. F1 and F2 are the most strategically decisive -- they determine whether the top two candidates (mAb and mRNA vaccine) can solve the Fusogard problem. F3 tests the most controversial Gate 1 candidate (phage). F4 tests the highest-IP novel target (LktB inhibitor). F5 tests the most innovative host-side approach (trained immunity). Total de-risk cost for all 5: ~$88-122K. Timeline: 8-20 weeks.*

## Phase 3 -- Vulcan First-Principles Predictions

*Source: Vulcan quarantined analysis (2026-03-27)*
*All predictions derive from first-principles decomposition of the disease map, without knowledge of what has been tried or failed.*

---

## Prediction V1: LktC Is a Functional Acyltransferase Required for Leukotoxin Activity

**Prediction:** Recombinant LktC, when incubated with pro-LktA and acyl-ACP (or acyl-CoA donor), will catalyze the acylation of LktA at one or more internal lysine residues, detectable as a mass shift of 200-300 Da per site by MALDI-TOF mass spectrometry. Furthermore, non-acylated (pro-)LktA will show <10% of the cytotoxic activity of acylated LktA against bovine PMNs.

**Basis:** The lktBAC operon has the same gene order as canonical RTX toxin operons, where the C gene product is ALWAYS an acyltransferase required for toxin activation. In E. coli alpha-hemolysin, HlyC acylates HlyA at Lys564 and Lys690 using acyl-ACP as donor; without acylation, the toxin is inactive. LktC has been annotated with conflicting domains (histidine kinase/sensor AND potential acyltransferase), but the RTX paradigm strongly predicts acyltransferase function. LktA's complete lack of cysteine residues makes it structurally dependent on post-translational modifications and calcium binding for functional folding, reinforcing the importance of acylation.

**Test:** Express recombinant LktC in E. coli. Purify. Incubate with recombinant pro-LktA (or an LktA fragment containing candidate lysine sites) and acyl-ACP. Analyze by mass spectrometry for acylation. Test acylated vs. non-acylated LktA in bovine PMN cytotoxicity assay.

**Falsification:** If LktC shows zero acyltransferase activity under all tested conditions (multiple substrates, cofactors, pH values, temperatures), and pro-LktA retains >80% of cytotoxic activity without any post-translational modification, then LktC is NOT an acyltransferase and the RTX acylation paradigm does not apply to F. necrophorum leukotoxin. LktC's function would then be regulatory only (histidine kinase/sensor).

**What changes if TRUE:** Opens a first-in-class drug target -- LktC acyltransferase inhibitors would produce inactive leukotoxin without killing F. necrophorum or generating AMR. The active site chemistry (acyl-ACP dependent, conserved histidine catalytic residue) provides a clear drug design template. This becomes the highest-priority molecular target in the portfolio.

**What changes if FALSE:** LktC is purely a regulatory/sensor component. The RTX acylation paradigm does not extend to F. necrophorum's unique leukotoxin. Intervention must target other points in the leukotoxin lifecycle (secretion, receptor binding, or transcription).

**Cost:** $5-10K (recombinant protein expression + mass spectrometry + cytotoxicity assay)
**Timeline:** 4-6 weeks

---

## Prediction V2: F. necrophorum Is Uniquely Vulnerable to Iron/Heme Starvation Due to Absent Siderophore System

**Prediction:** F. necrophorum subsp. necrophorum growth in defined medium will be strictly dependent on exogenous heme (or hemoglobin/hemin) as the iron source, with no growth at heme concentrations <0.1 uM even in the presence of free ferric or ferrous iron at 10-100 uM. Furthermore, a gallium(III)-protoporphyrin IX analog (Ga-PPIX) at 5 uM will inhibit F. necrophorum growth by >90% while showing <10% toxicity to bovine hepatocytes at the same concentration.

**Basis:** In silico analysis of the F. necrophorum genome found NO Fur homolog and NO siderophore biosynthesis genes. This is exceptional among pathogenic bacteria. F. nucleatum (closely related) has a defined heme uptake operon; F. necrophorum likely has an analogous system as its sole iron acquisition pathway. Gallium(III) porphyrins are taken up by heme transporters but cannot participate in redox reactions, poisoning iron-dependent enzymes. Ga-PPIX has shown potency against multiple iron-dependent pathogens and has inherent hepatic tropism (porphyrins accumulate in the liver).

**Test:** (a) Growth curves of F. necrophorum in defined medium with varying heme concentrations (0, 0.01, 0.1, 1, 10 uM hemin) with and without free iron supplementation (FeCl3, FeSO4 at 10, 100 uM). (b) MIC/MBC determination of Ga-PPIX against F. necrophorum. (c) Cytotoxicity of Ga-PPIX against bovine hepatocyte primary culture.

**Falsification:** If F. necrophorum grows normally in iron-supplemented medium WITHOUT heme (using free iron at >10 uM), then a non-heme iron uptake pathway exists that was missed by the genomic analysis. Heme starvation would be ineffective. If Ga-PPIX MIC is >50 uM (beyond achievable tissue concentrations), the Trojan horse strategy is impractical.

**What changes if TRUE:** Gallium-porphyrin therapy becomes a candidate intervention with direct bactericidal potential, no AMR risk (not an antibiotic), and inherent liver targeting. This could be a standalone or combination product.

**What changes if FALSE:** F. necrophorum has a cryptic iron acquisition system not detectable by homology search. Iron starvation strategies are unlikely to work, and the portfolio should focus on leukotoxin-targeted approaches.

**Cost:** $5-10K (defined media preparation, growth curves, Ga-PPIX MIC, hepatocyte cytotoxicity)
**Timeline:** 4-6 weeks

---

## Prediction V3: Contact System Activation on F. necrophorum Surface Occurs in Bovine Plasma and Contributes to Hepatic Microthrombus Formation

**Prediction:** F. necrophorum subsp. necrophorum incubated with bovine plasma will generate bradykinin at >500 pmol/mL (within 60 minutes) and activate Factor XIIa (detectable by chromogenic substrate assay), at levels comparable to those observed with human plasma (3,300 pmol/mL bradykinin). Furthermore, addition of a plasma kallikrein inhibitor (PKI) to bovine plasma will reduce F. necrophorum-induced thrombin generation by >70%.

**Basis:** Contact system activation on F. necrophorum surfaces was demonstrated in human plasma (Holm et al. 2011, Infection and Immunity) via specific HK binding through the D5 domain. Both bradykinin release and thrombin generation via the intrinsic coagulation pathway were shown. The bovine contact system has the same components (Factor XII, HK, prekallikrein). This mechanism has NEVER been tested in the bovine system or connected to liver abscess pathogenesis, yet the disease map describes microthrombus formation around bacterial foci as a key mechanism for anaerobic niche creation -- currently attributed solely to LPS and a separate platelet aggregation factor. Contact activation would provide a THIRD, independent coagulation mechanism.

**Test:** Incubate F. necrophorum (10^7 CFU) with fresh bovine plasma for 15, 30, 60 minutes. Measure: (a) bradykinin concentration by ELISA, (b) Factor XIIa activity by chromogenic substrate, (c) thrombin generation (calibrated automated thrombogram). Repeat with PKI (H-D-Pro-Phe-Arg-CMK, 10 uM). Compare to F. necrophorum + human plasma (positive control).

**Falsification:** If bradykinin generation in bovine plasma is <50 pmol/mL (>60-fold lower than human) and Factor XIIa activation is undetectable, then F. necrophorum does not activate the bovine contact system. The HK-binding surface molecule may have human specificity. Contact activation would be irrelevant to liver abscess.

**What changes if TRUE:** Contact system blockade (via PKI or anti-HK D5 domain strategies) becomes a viable intervention for liver abscess. This is especially attractive because approved drugs exist for the contact system (lanadelumab for hereditary angioedema). Repurposing opportunity.

**What changes if FALSE:** Microthrombus formation in liver abscess is driven entirely by LPS-mediated extrinsic coagulation and the separate platelet aggregation factor. Contact system is not a target for this disease.

**Cost:** $5-8K (bovine plasma collection, F.n. culture, ELISA, chromogenic assay, thrombogram)
**Timeline:** 3-4 weeks

---

## Prediction V4: LktA Cytotoxicity Is Calcium-Dependent Despite Lacking Canonical RTX Repeats

**Prediction:** LktA cytotoxicity against bovine PMNs will be reduced by >90% when extracellular calcium is chelated to <10 uM using EGTA (5 mM), compared to standard calcium-replete conditions (~1.2 mM ionized Ca2+). This calcium dependence will be concentration-dependent (graded, not all-or-nothing), suggesting a structural rather than signaling role for calcium.

**Basis:** LktA has NO sequence homology to other leukotoxins and lacks canonical RTX glycine-rich nonapeptide repeats. However, the protein has (a) zero cysteine residues (cannot form disulfide bonds), (b) heat lability (56 C/5 min), and (c) narrow pH stability window (6.6-7.8). These properties indicate a conformationally fragile protein that relies on non-covalent stabilization. Calcium binding is the most common stabilization mechanism for large secreted bacterial proteins, and the RTX paradigm (where calcium promotes folding of the repeat domain from disordered to functional) may apply even without canonical repeat sequences. A 3,241 amino acid protein with no disulfide bonds MUST have some structural stabilization mechanism -- calcium is the most likely candidate.

**Test:** Bovine PMN cytotoxicity assay with purified LktA at fixed concentration (LD80 dose) in buffer with varying Ca2+ concentrations: 0 (5 mM EGTA), 0.01, 0.1, 0.5, 1.2 mM ionized Ca2+. Measure cell viability at 2h by LDH release and flow cytometry (Annexin V/PI). Plot dose-response curve. Confirm with add-back experiment: EGTA-treated LktA + excess CaCl2 restoration.

**Falsification:** If LktA retains >80% cytotoxic activity in calcium-free conditions (5 mM EGTA), then the toxin is calcium-independent. Its conformational stability must derive from other mechanisms (hydrophobic core packing, ionic interactions, or a novel structural feature). Calcium chelation is not a viable intervention strategy.

**What changes if TRUE:** Opens a chemical biology approach -- calcium chelation or calcium-binding domain disruption as an anti-virulence strategy. More practically, identifies the calcium-binding domain as a structural vulnerability that could be targeted by small molecules that displace calcium and unfold the toxin.

**What changes if FALSE:** LktA has a fundamentally different structural biology than other large bacterial toxins. This would make it more interesting scientifically but removes one intervention avenue.

**Cost:** $2-5K (purified LktA, bovine PMN isolation, cytotoxicity assay)
**Timeline:** 2 weeks

---

## Prediction V5: The lktBAC Operon Is Upregulated by an Environmental Signal Encountered During the Commensal-to-Pathogen Transition

**Prediction:** A lktA promoter-reporter construct in F. necrophorum (or a transcriptional fusion assay) will identify at least one environmental condition that upregulates lktA transcription by >5-fold compared to standard anaerobic culture in rich medium. The most likely candidates are: (a) iron/heme limitation (growth in iron-depleted medium), (b) bile acid exposure (0.1-1% chenodeoxycholic acid or deoxycholic acid -- concentrations encountered in portal blood), (c) elevated AI-2 concentration (exogenous DPD/AI-2 addition), or (d) sublethal oxidative stress (brief O2 exposure followed by anaerobic recovery -- simulating the transit from anaerobic rumen to microaerobic liver).

**Basis:** Subsp. necrophorum produces 21-fold more lktA transcript than funduliforme, but this differential is measured under standard culture conditions. In vivo, the transition from rumen commensal to liver pathogen likely involves environmental signals that further upregulate leukotoxin production. LktC's annotated histidine kinase/sensor domains suggest it is part of a two-component regulatory system that senses an environmental cue. Iron limitation alters F. necrophorum metabolism (preferential utilization of glucose-1-phosphate, D-mannitol, L-phenylalanine); bile acids are a unique signal of the portal blood environment; and AI-2/quorum sensing controls virulence in related organisms.

**Test:** Construct a transcriptional reporter (lktA promoter driving GFP or luciferase) in F. necrophorum. Expose to a panel of environmental conditions in anaerobic culture: (a) iron/heme limitation (no hemin, +/- DIP chelator), (b) bile acid exposure (CDCA, DCA, TCA at 0.01-1%), (c) synthetic AI-2 (DPD at 1-100 uM), (d) transient O2 exposure (5 min aerobic, then anaerobic recovery), (e) low pH (5.5 vs 7.0), (f) bovine plasma or serum (10-50% v/v). Measure reporter output over 24h.

**Falsification:** If NO condition upregulates lktA transcription by >2-fold (all conditions within 2-fold of baseline), then leukotoxin production is constitutive and not environmentally regulated. The 21-fold subspecies difference is genetically encoded (promoter sequence), not environmentally modulated. Transcriptional intervention strategies are unlikely to work.

**What changes if TRUE:** Identifies the virulence trigger signal. If the signal is a small molecule (bile acid, AI-2), then a receptor antagonist could silence the leukotoxin operon. If it is iron limitation, then iron supplementation in the liver (counterintuitive but potentially achievable) could suppress virulence. This is the highest-information-value experiment because it simultaneously informs V1 (transcriptional control), V2 (LktC function), and V14 (quorum sensing role).

**What changes if FALSE:** Leukotoxin production is constitutive. The commensal-to-pathogen transition is not controlled by a transcriptional switch -- it may be controlled entirely by the physical opportunity (rumenitis + translocation) rather than a molecular signal. Intervention must target the protein or its effects, not its production.

**Cost:** $10-15K (reporter construction, environmental panel, anaerobic culture)
**Timeline:** 6-8 weeks

---

*5 Vulcan first-principles predictions appended. V1 (LktC acyltransferase) is the single most decisive experiment -- it either opens or closes an entire first-in-class drug target. V2 (heme starvation) exploits a unique metabolic vulnerability. V3 (contact activation) connects a known mechanism to an unexplored disease context. V4 (calcium dependence) is the cheapest test ($2-5K, 2 weeks) and resolves a fundamental structural biology question. V5 (environmental trigger) has the highest information-to-cost ratio because it simultaneously informs three other targets.*
