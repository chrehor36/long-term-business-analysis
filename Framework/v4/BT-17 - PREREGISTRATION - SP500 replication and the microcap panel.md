# BT-17 — PRE-REGISTRATION. The S&P 500 replication and the micro-cap panel.
**2026-08-28. Committed BEFORE any result is computed.** Results append below the line;
nothing above it may be edited afterward. Operator request: *"backtest and pit it against
the entire S&P 500, as well as 100 micro cap stocks."*

## What is being tested — and what cannot be

**The mechanical layer only.** The framework's judgment questions (Q1 understanding, Q2's
competitor row, Q3's conduct reading, Q4's named deaths) cannot be executed by a screen —
Test B established that the acceptance half is irreducibly judgment. Whatever BT-17
returns, it says nothing about v4.1 applied in full, and **the market-beating claim
remains UNPROVEN regardless of outcome** (operator protocol rule 7).

**The gate under test, frozen for comparability:** the corrected v3b statute exactly as
committed 2026-07-25 and used by Test E —

> PASS at anchor A ⟺ worst5_NI / market_cap ≥ max(DGS30(A), 4%), where worst5_NI is the
> MINIMUM of the last five annual net incomes from 10-Ks **filed ≤ A** (earliest-filed
> value per fiscal end), market cap = close(A) × shares(measurement ≤ A) × splits after
> measurement (close, never adjclose), and worst5_NI < 0 is an automatic fail.

Stated plainly: this is the v3-era, NI-based statute with its embedded 4% floor. v4.1
deleted that floor and forbids NI-proxy owner earnings in company runs. It is kept
verbatim here because the 13 committed anchor screens and Test E used it, and swapping
gates after seeing results is the forking-paths error. A v4-native mechanical gate would
be a different test, pre-registered separately.

## Hypotheses, framed to refute

- **H1 (the loss leg — the only promise the corpus makes, [E1-17]):** the passed group
  shows a strictly lower loss frequency than the rejected group of the same universe at
  the same anchor, at BOTH the 3y and 5y windows, pooled — and mean depth of loss among
  losers no worse. Refutation frame: we attempt to show passes lose as often or more.
- **H2 (the return leg — expected NOT to clear, stated in advance):** the equal-weight
  passed basket vs the universe mean and vs SPY, per anchor and pooled. Prior record:
  49.6% of 944 one-year holdings, basket −0.81 pts/yr, 2 of 8 anchors. **If H2 shows
  outperformance at these anchors it is treated as anchor noise, not proof; rule 7 stands.
  This sentence exists so a favourable number cannot be celebrated after the fact.**
- 1y windows are reported as context only (below Ground Rule 5's three-year minimum).

## Universe A — the S&P 500 (replication + extension)

- Panel: the **13 committed corrected screens** (anchors 2013-06-30 … 2025-06-30), the
  2013 point-in-time reconstruction — the only membership list on disk without
  membership look-ahead. Known limitations restated: no post-2013 entrant can appear;
  coverage gaps 80–136 of 503 documented in the coverage logs.
- Scoring: forward total-return windows 1y/3y/5y from each anchor where air exists
  (monthly adjclose ratios only — the house rule), passed vs rejected, plus SPY at the
  same windows for the return leg's context.
- This replicates Test E / BT-15/16 with today's price data and the post-July tool fixes;
  deltas from the July numbers are reported, not hidden.

## Universe B — the micro-cap panel (new)

- **Selection rule, locked:** iterate SEC `company_tickers.json` in the order of
  SHA-256 of the CIK string (deterministic; no seed to tune). For each candidate at the
  anchor: (a) five annual NIs from 10-Ks filed ≤ anchor exist (this is also the
  established-filer filter); (b) market cap at the anchor, house rule, in **[$50M, $300M]**;
  (c) a price series exists at the anchor (a series starting after it is a recycled
  ticker — refused); single-class common tickers only (unit/warrant suffixes excluded).
  The first **100** candidates meeting (a) and (c) with cap in range form the universe;
  they are then split by the frozen gate into passed/rejected. Examination stops at
  2,000 candidates; if fewer than 100 qualify, the found count is reported and used.
- **Anchors: 2018-06-30 (primary) and 2021-06-30 (secondary), each with its own
  independent hash-order sample.** Both have full 5y forward air. 2021 closes its windows
  into the 2022 micro-cap drawdown — chosen deliberately as the hard case.
- Windows and scoring identical to Universe A. The control group is the rejected members
  of the same 100-name universe at the same anchor.

## Biases, stated in advance

1. **Delisting under-counts losses, and micro caps delist more.** A dead micro cap shows
   as NO DATA, not −100%. Both groups' no-data counts are reported, AND the loss rates are
   shown under both treatments (no-data excluded; no-data counted as loss). In Test E the
   no-data asymmetry ran 3:1 **in the screen's favour** — if it recurs here it is named,
   and a "pass" that depends on the favourable treatment is reported as NOT ROBUST.
2. **The five-filed-years requirement is itself a survivorship-flavoured filter** — it
   excludes young companies and recent IPOs, which is where much micro-cap mortality
   lives. The panel therefore tests the gate among established micro caps only; the
   conclusion is scoped to that population.
3. **SEC coverage:** XBRL companyfacts thin out before ~2010; both anchors sit safely
   after. Names whose facts fetch fails are logged and skipped, count reported.
4. **One and two anchors are not eight.** The micro-cap result, whatever it is, is an
   opening panel, not a record.

## Pre-registered verdict rules

- **H1 PASS** requires the Test E criteria met in BOTH universes independently.
- **Mixed results are reported as mixed.** No pooling across universes to rescue a fail.
- Every number lands in `Backtests/` as CSV beside this file's appended results; the
  scripts land in `Backtests/scripts/bt17_*.py`.

---
# RESULTS — appended after the pre-registration commit

**2026-08-28, same day.** Scripts committed before results (b5595fb); raw CSVs committed
beside this file.

## First, the withdrawal — the bug the record exists to catch, caught again

The first micro-cap run was **WITHDRAWN before commit**: the split factor was applied only
through the anchor instead of through today, against Yahoo's retroactively split-adjusted
closes. Chipotle (50:1 split 2024) appeared as a "$240M micro cap" and Super Micro (10:1)
as "$115M"; both passed the gate and would have carried their later moonshots into the
PASS group. **This is the identical bug class that voided four backtests on 2026-07-25.**
The fix is committed with the withdrawal named in a comment; the corrected panels below
contain neither name. Caught by eyeballing the passed list before believing any summary —
the step this file now records as mandatory.

## Universe B — the micro-cap panel (corrected)

Universes: 73 names (2018 anchor) and 98 (2021) from 2,000 examined each (the cap bound,
as pre-registered; the binding filter was five filed years — 966/882 candidates lacked
them). Gate pass rates: **4/73 and 9/98** — the statute admits ~5–9% of established micro
caps. Passed lists eyeballed: small banks, Crown Crafts, a water utility; caps verified in
range.

Pooled across both anchors (ex-no-data; **no-data was zero within the panel — see
conditioning note**):

| window | group | n | median | mean | loss freq | depth of loss |
|---|---|---|---|---|---|---|
| 3y | PASS | 13 | +4.9% | +2.9% | **38.5%** | −29.0% |
| 3y | REJ | 158 | −13.5% | +15.7% | **57.0%** | −58.0% |
| 5y | PASS | 13 | +46.4% | +64.1% | **15.4%** | −23.5% |
| 5y | REJ | 158 | −19.4% | +23.6% | **60.1%** | −63.8% |

**H1 in Universe B: PASS** — loss frequency strictly lower at both windows pooled, depth
no worse. Per-anchor honesty: at 2018 alone the depth clause FAILS (one passed loser,
HNRG −59.5%, vs rejected mean −45.2%; n=4 passes). The headline base rate: **the median
established micro cap that the gate rejected lost money over BOTH the 3y and 5y windows.**

**Conditioning, prominent:** universe assembly requires a price series that still exists
in 2026 (59–63 no-chart and 19–25 recycled-ticker exclusions at examination). The panel is
therefore "established micro caps whose series survived to today"; both groups are equally
conditioned, the within-panel comparison stands, but the absolute loss rates are **floors**.

## Universe A — the S&P 500 re-score (13 anchors, 2013–2025)

457 union tickers; **74 chart fetches failed** (a mix of genuine delistings/acquisitions
and symbol-format casualties like BRK.B) — these land in no-data, which ran roughly
symmetric between groups (36.2% of pass slots vs 38.6% of reject slots at 1y).

| window | group | slots | scored | mean | loss freq (ex) | loss freq (incl. no-data) | depth |
|---|---|---|---|---|---|---|---|
| 3y | PASS | 887 | 565 | +46.6% | **20.5%** | 49.4% | −25.7% |
| 3y | REJ | 3,497 | 2,143 | +51.2% | **23.9%** | 53.4% | −27.6% |
| 5y | PASS | 739 | 467 | +84.9% | **17.8%** | 48.0% | −31.5% |
| 5y | REJ | 2,819 | 1,723 | +99.7% | **18.8%** | 50.4% | −36.0% |

SPY at the same windows: 3y +47.6% (11 anchors), 5y +88.1% (9 anchors).

**H1 in Universe A: PASS, thin** — lower loss frequency at both windows under BOTH
no-data treatments, depth no worse; the margins (3.4 pts at 3y, 1.0 pt at 5y) echo Test
E's thinness.

**H2, the return leg — no claim, as pre-stated:** the pooled passed basket TRAILS both the
rejects and SPY at 3y and 5y. The 1y anchor-by-anchor record is 7 of 13 positive vs SPY,
mean +1.0 pt/yr, dominated by the 2020 anchor (+31.6); the four most recent anchors
(2022–25) are all negative. This differs from July's 2-of-8/−0.81 record (different price
source, no-data pattern, and anchor set); the difference is reported, not resolved.
**Rule 7 stands: the market-beating claim remains UNPROVEN.**

## Verdict, per the pre-registered rules

- **H1 (the loss leg): PASS in both universes independently.** With named caveats: thin
  margins in A; pass-group n of 4 and 9 in B; survivorship conditioning in both; the
  2018-anchor depth wrinkle; and the gate is the frozen v3-era NI statute, not v4.1.
- **H2 (the return leg): no outperformance claim.** Pooled 3y/5y trails; the 1y mean
  delta is anchor noise per the no-celebration clause.
- **What this says, in one sentence:** the mechanical layer continues to do the only
  thing the corpus ever promised — its picks lose money less often and less deeply than
  what it rejects, now shown in a second universe where the base rate of loss is brutal —
  and it still shows no evidence of beating the market.
