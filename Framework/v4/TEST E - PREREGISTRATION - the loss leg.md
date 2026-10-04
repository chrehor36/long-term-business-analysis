# TEST E — PRE-REGISTRATION. The loss leg of Ground Rule 7.
**2026-08-28. Committed BEFORE any result was computed.** Results will be appended below the
line; nothing above it may be edited afterward.

## The question, and its corpus source

Ground Rule 7 **[E1-17]** promises no results. What it promises is an *attempt*:

> "we will **attempt to bring risk of permanent capital loss (not short-term quotational
> loss) to an absolute minimum** by obtaining a wide margin of safety in each commitment and
> a diversity of commitments"

The yardstick leg (Ground Rules 4 and 5, **[E1-01]**) has been tested and stands on the
honest record: the corrected basket beat SPY at 2 of 8 anchors, mean −0.81 pts/yr. **The
loss leg has never been scored.** Test E scores it.

**Question: does the mechanical screen deliver fewer and shallower losses than the names it
rejected, at the corpus's own judging windows?**

## Design

- **Panel:** the eight corrected point-in-time screens, anchors 2013-06-30 through
  2020-06-30 — the only anchors with five full years of forward air. 445 union tickers,
  696 pass-slots. Every name carries the screen's own `passed` flag, so **the control group
  is the rejected names from the same universe at the same anchor** — the sharpest possible
  control, since both groups passed the same reconstruction and differ only by the screen.
- **Windows:** 3-year and 5-year forward returns. Ground Rule 5: *"I much prefer a
  five-year test, I feel three years is an absolute minimum."* The BT-16 one-year panel is
  reported as context only — it sits below the corpus's own minimum.
- **Returns:** monthly adjusted closes, ratio only (the house rule: `adjclose` is permitted
  for ratios, never as a price). Entry = last monthly close at or before the anchor; exit =
  close at anchor +36 / +60 months.
- **SPY** is reported at the same windows for context, not as the criterion — an index
  diversifies name-level losses away by construction, so name-level loss rates against it
  would be a category error.

## Pre-registered outcomes

- **PASS:** the passed group shows a **strictly lower loss frequency** (fraction of names
  with a negative return) than the rejected group at **both** the 3-year and the 5-year
  window, pooled across anchors, **and** the mean depth of loss among losers is no worse.
- **FAIL:** loss frequency equal or higher at either window.
- **No numeric threshold is invented.** The test is comparative — a ranking, which is the
  only form Q5 permits **[E4-21]**.

## Biases, stated in advance

1. **Delisting under-counts losses.** The price source drops delisted names; a name that
   went to zero shows as NO DATA, not as −100%. Both groups' no-data counts are reported,
   and the direction of the bias is: **loss rates below are understatements**, most severely
   in whichever group had more delistings.
2. **Ticker recycling** (bug 6): a series that *starts after the anchor* is a different
   company wearing a recycled ticker, and is refused, not scored.
3. **A negative 3-year window is still quotational** by the corpus's own language; five
   years is a proxy for permanence, not permanence. The truncated/delisted column is the
   closest observable to true permanent loss and is reported beside the return-based rates.
4. **This tests the mechanical layer only.** Q1–Q4 are judgments no screen can run. Whatever
   the outcome, it says nothing about v4 applied in full, and **the market-beating claim
   remains UNPROVEN** — this is the loss leg, not the yardstick leg.

---
# RESULTS — appended after the pre-registration commit
**2026-08-28.** Panel: 696 pass-slots (666 scored) against 2,452 rejected-slots (2,111
scored), eight anchors. Data: `Backtests/2026-08-28 TEST-E Loss Panel.csv` and
`…TEST-E Summary.json`. Script: `Backtests/scripts/test_e_loss_side.py`.

## Pooled, per the pre-registered criterion

| window | group | loss rate | mean depth of losses | median return |
|---|---|---|---|---|
| **3y** | **passed** | **19.4%** | **−22.7%** | +35.4% |
| 3y | rejected | 21.6% | −27.3% | +35.9% |
| **5y** | **passed** | **17.0%** | **−29.6%** | +64.0% |
| 5y | rejected | 18.1% | −33.5% | +60.1% |

**VERDICT: PASS, on the pre-registered terms.** Loss frequency strictly lower at both
windows; mean depth shallower at both.

## What the pass is worth, stated honestly

- **The edge is thin: 2.2 points at 3y, 1.1 at 5y.** The slots overlap in names and in
  time and share one market factor, so no formal significance is claimable; by naive
  proportions arithmetic the gaps sit within roughly 1.3 and 0.7 standard errors of zero.
  The pre-registration set no significance test, so none is applied after the fact in
  either direction. The verdict stands on its stated terms **and its size is stated**.
- **The bias runs in the screen's favour.** No-data slots: **4.2% of passed vs 12.9% of
  rejected** — a three-to-one asymmetry. Delisted names return no price series at all, so
  the `delisted` counter reads 0 and every delisting sits inside no-data. Missing names
  skew toward failures, and the failures are three times as concentrated in the rejected
  group, so per pre-registered bias #1 **the true gap is probably wider than measured.**
- **The edge is not uniform.** The passed group did *worse* at 2 of 8 anchors on the
  3-year window (2017, 2019) and 3 of 8 on the 5-year (2015, 2018, 2019). The worst is the
  2017 anchor at 3y: 52.6% vs 38.0% — a window that closes into June 2020. The pooled pass
  coexists with anchor-level flips, and the pre-registration pooled deliberately; the
  flips are reported so the pooling cannot hide them.
- **SPY was positive in all sixteen windows** (+31% to +124%), so every scored loss was
  also a large relative failure. The rates above are absolute, per the design.

## The shape of the result

Put beside the yardstick leg (2 of 8 anchors, mean −0.81 pts/yr) and BT-16 (49.6% of
one-year holdings), the picture is consistent: **the mechanical screen does not pick
winners — the medians are nearly identical — but it modestly avoids losers, and avoids the
deep ones somewhat better than the shallow ones.**

That is the shape Ground Rule 7 **[E1-17]** predicts. The promise was never outperformance;
it was value-based selection and an *attempt* to minimize permanent capital loss. On the
first test of that attempt ever run against this screen, the attempt shows through —
thinly, with anchor-level exceptions, and with the delisting bias understating it.

**Boundaries, restated from the pre-registration:** this scores the mechanical layer only,
not v4 (Q1–Q4 are judgments no screen can run); a negative 5-year window is a proxy for
permanence, not permanence; and **the market-beating claim remains UNPROVEN — nothing here
touches the yardstick leg, which still stands at 2 of 8.**