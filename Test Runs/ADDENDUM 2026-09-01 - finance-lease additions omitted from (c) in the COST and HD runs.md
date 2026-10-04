# ADDENDUM — 2026-09-01
## Finance-lease additions were omitted from (c) in the COST and HD runs

**Operator rule 6: violations found later are corrected in an addendum, never by editing
history.** This corrects two committed run files without touching them.

---

## WHAT WAS FOUND, AND BY WHAT

The **LSTR run of 2026-09-01** established that Landstar buys most of its trailers with
finance leases, so the cash-flow statement's "purchases of operating property" line misses
roughly **$33 million a year** of capital actually acquired. That took Landstar's
capex-to-depreciation ratio from the **0.43x this project's screen reported** to **1.10x** —
the difference between *"the D&A end is the conservative one"* and *"it is not"*, which is
the [E3-44] direction question that PNR, SHOE and OTIS each had to settle from the filings.

Equipment acquired under a finance lease **never touches investing cash flow.** So any (c)
built on the cash capex line understates capital consumption, and it **always errs in the
flattering direction.**

Measured across 84 already-priced names: **20 show lease-financed additions above 5% of cash
capex.**

---

## THE TWO CLEARED NAMES AFFECTED

Neither run addressed it. **COST's run does not mention finance or capital leases anywhere.
HD's mentions them once, on the balance-sheet debt line (*"including $2,963M of finance
leases"*), not in (c).**

| | COST | HD |
|---|---|---|
| Price / cap | $945.53 / $419.3bn | $330.07 / $329.3bn |
| Owner earnings, cash capex only | $5,248M | $14,062M |
| **Owner earnings, finance leases included** | **$4,923M** | **$13,713M** |
| Effect on (c) | **+$325M/yr** | **+$349M/yr** |
| Yield | 1.25% → **1.17%** | 4.27% → **4.16%** |
| Growth needed for the [E4-28] floor | 8.75% → **8.83%** | 5.73% → **5.84%** |

Lease additions by year, $M — COST: 399, 794, 100, 200, 131. HD: 672, 322, 336, 153, 263.

## THE VERDICT ON THE ADDENDUM ITSELF

**The defect is real and the effect is immaterial to both conclusions.** Costco's yield falls
**0.08 points** and Home Depot's **0.11 points**. Both businesses had already failed Q5 by
margins an order of magnitude larger — Costco needs 8.8% perpetual growth and Home Depot
5.8%. **No verdict changes. No band is re-derived.** The armed thresholds stand, and this
addendum is carried in their alert labels so the next reader sees it before acting.

**Stated plainly because the temptation runs the other way:** an error found in one's own
work that turns out not to matter is still worth publishing, and an error that *would* have
mattered is exactly what this practice exists to catch. *"you must not fool yourself, and
you're the easiest person to fool"* **[E3-41]**.

---

## THE TOOL FIX, AND ITS DELIBERATE LIMIT

`Screens/floor_screen.py` now adds finance-lease additions to capex — **but only on
`RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`**, the unambiguous ASC 842
element. Two other elements were tested and **refused**:

- **`CapitalLeaseObligationsIncurred` is a legacy element filers use inconsistently.** SHOE
  fires on it at $53–73M a year, and the SHOE run had already established that its leases are
  **OPERATING**, netting to a $2.6M drag *inside* operating cash flow (ASC 842 add-back
  +$57.6M against a cash payment of −$60.2M). Adding that to capex would **double-count the
  same payments.** It now raises a flag instead: *"READ THE LEASE NOTE before trusting (c)."*
- **`NoncashOrPartNoncashAcquisitionFixedAssetsAcquired1`** is broader still and is not used.

### The limit worth recording

**Landstar itself is not catchable by the screen.** Its tag stops in 2018, so the finance
leases the run found are **not in XBRL under any element.** The run got them by reading the
filing.

That is **operator rule 4 working exactly as written** — tagged data is transcription and
screening, and no name reaches Q5 on XBRL alone. The tool's job here is to raise the
question, not to answer it: *every flag is a prompt to read, never a score* (operator rule 8).
The first version of this fix tried to compute the answer, and it was wrong on SHOE. **The
correct fix computes less and flags more.**

## NAMES NOW FLAGGED RATHER THAN ADJUSTED

LSTR (376% of cash capex), SHOE (165%), XPEL (111%), DXC (40%), and others above the 10%
line. **Adjusted** on the unambiguous element: PFGC +113%, GPI +30%, HD +11%, COST +7%.
**Unaffected**: ITW, PNR, OTIS, LOPE.
