# WORKPAPER - BELFB market cap, struck by hand
**2026-09-21.** Ordered by the brief: the screen row's own flag said the cap ($541M) was smaller
than a filed public float ($1,200M), which is impossible. Operator rule 4: the screen figure is a
prompt to read a filing, never a score.

## 1. THE SHARE COUNTS, FROM THE COVERS, BY HAND

**10-K FY2025, accession `0001437749-26-005354`, filed 2026-02-24, period 2025-12-31.**
Cover, "Number of Shares of Common Stock Outstanding as of January 31, 2026":
- Class A Common Stock: **2,115,263**
- Class B Common Stock: **10,541,050**

**10-Q for the quarter ended 2026-06-30, accession `0001437749-26-025619`, filed 2026-08-04.**
Cover, "Number of Shares of Common Stock Outstanding as of July 31, 2026":
- Class A Common Stock: **2,115,263**
- Class B Common Stock: **12,324,187**
- **Total: 14,439,450**

Cross-check against the filed balance sheet in the same 10-Q (line 914 of the converted text):
*"Class B common stock, par value $.10 per share, 30,000,000 shares authorized; 12,324,187 and
10,543,368 shares outstanding at June 30, 2026 and December 31, 2025, respectively (net of
3,218,307 restricted treasury shares)"*. The cover count and the balance-sheet count agree.

**The Class B count rose 1,780,819 shares, 16.9%, in six months** (10,543,368 at 2025-12-31 to
12,324,187 at 2026-06-30). That is not a split - `split_factor_after` returns 1.0 for both tickers
after 2026-07-31 - and it is carried to Q3 as an issuance question [E5-15].

## 2. THE PRICES, FLAGGED AS AGGREGATOR (live quotes only, operator rule 5)
- **BELFB $241.97**, close 2026-09-18, aggregator (Yahoo chart via `tools/sources.py`), flagged.
- **BELFA $198.83**, close 2026-09-18, same source, flagged.

Two classes, two quotes. A cap built from one class's price is not the company's cap either.

## 3. THE CAP
| class | shares (cover, 2026-07-31) | close 2026-09-18 | cap |
|---|---|---|---|
| Class A (BELFA, voting) | 2,115,263 | $198.83 | **$420.6M** |
| Class B (BELFB, non-voting) | 12,324,187 | $241.97 | **$2,982.1M** |
| | | **TOTAL** | **$3,402.7M** |

Split-invariance: `close(2026-09-18) x shares(2026-07-31) x splits AFTER 2026-07-31`, and the
split factor is 1.0 for both classes, so the formula reduces to the product above.

## 4. HOW THE SCREEN GOT $541M - AND THE PRIOR IS REFUTED

The brief's prior to refute was **a stale price**, which is what BLMN's cap defect was. **It is not
the defect here. The price was fine.**

`dei:EntityCommonStockSharesOutstanding` resolves **undimensioned exactly once in Bel Fuse's entire
companyfacts file**:

    end 2011-08-01 | val 2,174,912 | fy 2011 | fp Q2 | form 10-Q/A | frame CY2011Q2I

That is the only row. Every filing since tags the element **dimensioned by class**, so an
undimensioned annual fetch falls back on a **fifteen-year-old Class A count from a 10-Q/A**.

Arithmetic check: **$248.69 (BELFB close, 2026-08-28) x 2,174,912 = $540.85M**, which is the
screen's $541M to the dollar. The anchor price is three weeks old and immaterial.

**So the defect is the share count, not the price, and it is a compound of two things: the wrong
class AND a fifteen-year-old measurement.** The understatement is **6.29x**: $541M against
$3,402.7M.

This is the same shape as the `AllocatedShareBasedCompensationExpense` defect recorded in
`RESUME STATE 2026-09-12` item 3F - a dimensioned tag read undimensioned, returning something
plausible rather than nothing. There it returned zero and was made to refuse; here it returns a
2011 number and does not refuse.

**The screen's `cap_flag` worked.** It compared the cap to `dei:EntityPublicFloat` ($1,200M at
2025-06-30) and said a cap cannot be smaller than a subset of itself. The diagnostic caught its
own tool. What it could not do is say which of the two was wrong, which is why the rule is that a
human reads the cover.

## 5. WHAT THIS DOES TO THE SCREEN ROW
Every per-cap figure on line 34 of `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` is built
on the $541M and is therefore void:
- `yield_bottom 0.0743` (7.43%) and `vs_sovereign 0.0208` - both **6.29x too high**
- `growth_required 0.0257` - void
- `acq_note` "acquisitions are $337M, **62% of cap**" - the true share is **9.9% of cap**
- `spread_dollars $40M to $70M` is an owner-earnings band, not a cap figure, and survives the
  correction; it is rebuilt from the filings at Q4 regardless.
