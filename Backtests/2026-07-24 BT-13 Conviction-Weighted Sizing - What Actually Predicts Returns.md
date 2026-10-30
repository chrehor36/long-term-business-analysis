# BACKTEST BT-13 — Conviction-Weighted Sizing: What Actually Predicts Returns — 2026-07-24

Every backtest through BT-12 used equal weighting — every gate-passer got
the same size slot. But the corpus is explicit that position sizing
should NOT be equal: **E1-08** (1965 partnership letter) — *"we might
invest up to 40% of our net worth in a single security under conditions
coupling an extremely high probability that our facts and reasoning are
correct with a very low probability that anything could drastically
change the underlying value"* — and **E3-21** (Munger, 1994 USC talk) —
*"the wise ones bet heavily when the world offers them that opportunity...
They bet big when they have the odds."* This test operationalizes that
principle and checks, honestly, whether it actually improves on equal
weighting. **The first, most obvious way to operationalize it doesn't
work. A more specific reading of E1-08 does, modestly, in both
independent samples.**

## METHOD
Two conviction proxies were tested, applied to both the 2018 cohort
(BT-10's 18 full-gate survivors) and the 1993 cohort (BT-11/12's 12
full-gate survivors) — two independent samples, not one:

1. **Margin × Moat** (the naive, first-pass reading of E1-08's two
   conditions combined): weight ∝ (entry Book One yield − hurdle) ×
   (2.0 if moat class WIDE, 1.0 if NARROW). This treats "how mispriced"
   and "how durable" as equally important, multiplied together.
2. **Moat-only**: weight ∝ moat class alone (WIDE = 2x NARROW), dropping
   the valuation-margin term entirely.

Moat classifications are the real WIDE/NARROW verdicts already reached
in BT-10's and BT-11's actual Gate 2 research — not re-derived or
adjusted for this test.

## RESULT 1: MARGIN-BASED WEIGHTING DOESN'T WORK — CHECKED DIRECTLY, NOT ASSUMED
Before building anything, the core assumption was tested directly: does
a bigger statistical discount (yield margin above the hurdle) actually
predict which survivors go on to compound fastest?

| Cohort | Correlation(margin above hurdle, subsequent CAGR) |
|---|---|
| 2018 (18 names) | **-0.024** |
| 1993 (12 names) | **-0.154** |

**Essentially zero, trending slightly negative, in both independent
samples.** Among names that have *already cleared* the qualitative gates,
how much of a discount they were trading at tells you nothing about
subsequent performance — if anything, a very slight negative
relationship. Concretely: NVDA (2018's best performer, 55.60% CAGR) had
an unremarkable 7.97-point margin, ranked 9th of 18 by that measure.
GWW (1993's best performer, 11.97% CAGR) had the *smallest* margin in its
cohort (0.33 points — it barely cleared the hurdle at all). Both would
have been *underweighted* by a margin-based conviction rule, not
overweighted.

**Applying the Margin × Moat formula confirms this empirically**: it
underperforms equal weighting in both cohorts (-0.13 pts/yr in 2018,
-0.65 pts/yr in 1993) — the valuation-margin term actively hurts more
than the moat term helps, because it puts real weight on names that
happened to be statistically cheapest without that cheapness predicting
anything about subsequent quality of compounding.

## RESULT 2: MOAT ALONE IS A SMALL, REAL, POSITIVE SIGNAL — IN BOTH COHORTS
Dropping the valuation term and weighting purely by moat durability:

| | 2018 cohort | 1993 cohort |
|---|---|---|
| WIDE-moat names, mean CAGR | 18.62% (n=15) | 7.17% (n=6) |
| NARROW-moat names, mean CAGR | 12.81% (n=3) | 5.39% (n=6) |
| Equal-weight portfolio CAGR | 22.98% | 7.22% |
| **Moat-only-weighted portfolio CAGR** | **23.61%** | **7.56%** |
| Improvement over equal-weight | **+0.63 pts/yr** | **+0.34 pts/yr** |

WIDE-moat businesses outperformed NARROW-moat businesses, on average, in
**both** independent 8-year and 32-year samples — a directionally
consistent, modest, real edge. Weighting the portfolio toward moat
durability (not toward statistical cheapness) recovers a small but real
improvement over equal weighting in both cases.

## WHAT THIS MEANS FOR E1-08 — THE TWO CONDITIONS AREN'T EQUALLY IMPORTANT
E1-08 names two conditions for concentrating capital: (a) high confidence
the reasoning is correct, and (b) low probability of drastic value
change. This test's evidence points to **(b) — moat durability — being
the condition that actually correlates with outcomes**, while a
mechanical proxy for (a) built from statistical cheapness does not. This
is a meaningful refinement, not a rejection of the corpus principle: Gate
2's moat classification is doing real predictive work; Book One's yield
margin, once past the pass/fail hurdle, is not a useful *sizing* signal —
it's a floor to clear, not a ranking to size by.

## HONEST CAVEATS — THIS IS A SMALL, PRELIMINARY RESULT
- **Sample sizes are tiny** (18 and 12 names) and the moat classifications
  themselves came from AI-run qualitative research (BT-10/BT-11's
  standing caveat), not independently re-verified here.
- **The moat-only edge is modest** (+0.34 to +0.63 pts/yr) — real and
  consistent in direction across two independent samples, but small
  enough that a slightly different moat-classification call on a handful
  of borderline names (FAST, USB, PNC in 2018; EMR, PCAR in 1993, all
  called NARROW with some hedging in the original research) could move
  it meaningfully.
- **Neither weighting scheme closes the 1993 cohort's gap to SPY**
  (moat-only: 7.56% vs. SPY's 10.73%, still -3.17 pts/yr) — sizing
  discipline is a real, incremental improvement, not a fix for the
  deeper sampling/selection issues already flagged in BT-11.
- **This tested only a binary WIDE/NARROW split at a fixed 2:1 ratio** —
  not a continuous conviction scale, and not combined with BT-12's
  rotation logic in this pass (a combined moat-weighted-and-monitored
  test is the natural next step, not yet run).
- **A specific overfitting trap was deliberately avoided and should stay
  avoided**: the data shows small-margin names (GWW, STT, NVDA) happened
  to be the best performers in each cohort. It would be easy to now
  "discover" that an *inverse* margin weighting (smaller discount = more
  conviction) works even better — but that would be reverse-engineering
  a rule to fit these two specific small samples after seeing the
  answer, not a principled hypothesis. That temptation is named here
  explicitly and not acted on.

## WHAT THIS SETTLES, AND WHAT'S STILL OPEN
1. **The first, most literal reading of "bet heavily when odds favor" —
   size up on statistical cheapness — is empirically wrong**, checked
   directly with a correlation analysis before being asserted, not
   assumed to work because the corpus says to bet heavily.
2. **A more specific reading — size up on moat durability, not
   valuation — is a small, real, replicated edge** across two
   independent multi-year samples (8 years and 32 years), consistent
   with E1-08's "low probability of drastic value change" being the
   operative condition.
3. **Still open**: whether a continuous, better-differentiated moat/
   quality score (rather than a binary WIDE/NARROW split) would produce
   a larger, more reliable sizing edge; whether combining moat-weighted
   sizing with BT-12's rotation-on-real-thesis-break discipline compounds
   the improvement further; and whether this holds at a third,
   independent historical date.

## SELF-AUDIT
- [x] The core hypothesis (valuation margin predicts returns) was tested
  with a direct correlation check *before* building the weighting scheme
  — found to be ~zero/negative, reported as a negative result rather than
  quietly dropped
- [x] The naive full formula's underperformance (-0.13, -0.65 pts/yr) is
  reported plainly, not hidden behind the more flattering moat-only
  variant
- [x] The moat-only result is real but modest, and stated as such — not
  oversold as "the framework's edge, solved"
- [x] An explicit overfitting trap (inverse-margin weighting, which would
  fit these two small samples suspiciously well) was named and
  deliberately not pursued
- [x] Tested on two independent historical samples (2018, 1993), not one
- [x] All data and scripts committed under `Backtests/`
