# -*- coding: utf-8 -*-
p=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-12 Run - ROKU Roku.md"
t=open(p,encoding='utf-8').read()

blk = r"""## THE SCREEN ROW — EVERY NUMBER REPRODUCED FROM THE FILED STATEMENTS, AND WHAT EACH ONE MEANS

*Operator rule 8: a flag is a prompt to read, never a score. All seven reproduce; four of the
seven are arithmetically right and diagnostically misleading, and the reasons differ.*

**The series the screen reads is `NetCashProvidedByUsedInOperatingActivities` from the 10-Ks,
last nine years** — FY2017 through FY2025: 37,292 · 13,922 · 13,707 · 148,192 · 228,081 ·
11,795 · 255,856 · 218,045 · 483,718 (all $k, all cross-checked against the filed cash-flow
statements).

| screen output | reproduced? | what it actually means |
|---|---|---|
| `cap_m 22995` | **yes — $22,996M** | Correct, and correct **because it summed the two share classes**, which is the judgment this run made independently from the charter and the merger agreement (Step 0). Eight runs have found the queue's cap wrong; this is not one of them. |
| `oe_bottom_m −151` | **yes — −$150,725k** | The **five-year 2021-2025** mean at the capex end. |
| `oe_top_m −81` | **yes — −$81,434k** | The **three-year 2023-2025** mean at the capex end. **These are two different WINDOWS, not two ends of a capex band** — the INTC defect of 2026-09-07 repeating. The real capex band inside the five-year window is $272k wide. |
| `yield_bottom −0.66%` · `vs_sovereign −6.01 pts` | **yes** | −150,725 ÷ 22,996,000 = −0.66%, against 5.35%. |
| `growth_required: n/a — negative bottom` | **yes** | Correct and honest. |
| `level_shift 4.23 "STEP UP"` | **yes — 4.228** | mean(2023-2025) $319,206k ÷ mean(2017-2022) $75,498k. **The step is real and it is in the wrong series.** Operating cash flow adds SBC back; the last three years' operating cash averages 4.23x the prior six **because gross profit grew while $1.1bn of the cost of earning it was paid in stock.** |
| `level_shift_oe n/a "EARLY HALF STRADDLES ZERO (from −$509.8M)"` | **yes** | The owner-earnings series' early half runs from **−$509,832k (FY2022)** upward across zero, so the function refuses the ratio. Correct refusal. |
| `flags_disagree: FIRES` | **yes** | `ls[0]` is 4.23 and `ls_oe[0]` is None. **This disagreement is the whole file in one boolean: operating cash stepped up 4.2x and owner earnings did not step at all, because the entire step sits inside the stock-compensation add-back.** The PLPC run of 2026-09-07 added this flag for exactly this case, and Roku is the sharpest instance of it in the queue. |
| `window_disagree: FIRES` | **yes** | The nine-year window begins at FY2017 and **excludes FY2016's negative operating cash of −$32,463k**; on the full filed series the ratio is refused. The LRCX diagnosis applies verbatim: *the nine-year window's "earlier half" already contains part of the current wave.* |
| `best_year_dep 0.261 "ONE YEAR CARRIES THE WINDOW"` | **yes — 0.2608** | Drop FY2025 and the nine-year operating-cash mean falls from **$156,734k to $115,861k, −26.1%.** One year of nine carries a quarter of the mean, and it is the most recent one. |
| `wc_note: FIRES — the CONTRACT-LIABILITY line moved by 351% of a year's operating cash` | **yes — 351.0%** | Decoded in full below. **It is the largest reading in the 361-name queue and it is a denominator artifact that names the smallest of the three working-capital movements in the statement.** |
| `newest_filing 2025-12-31` · `newest_periodic 2026-06-30` | **yes** | Both read. **And neither the row nor the brief carries the fact that the company signed a definitive agreement to be acquired on 2026-06-14** — recorded at Step 0. |

**The honest summary of the row: the queue's cap is right, its two owner-earnings numbers are
right and are two different windows, and every one of its four flags fires for a true reason
and points at the wrong thing.** The screen's `level_shift` sees a business improving 4.2x; the
business's owner earnings have not improved at all, because the improvement is the SBC add-back.
The screen's `wc_note` sees a 351% working-capital swing; the swing it names is $41.4M and the
one it cannot see is $313.2M.

"""

anchor = "## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY?"
assert anchor in t
i = t.index(anchor)
t = t[:i] + blk + t[i:]

log = r"""
---
## RUN LOG
- **2026-09-12.** Framework and template read; run file created from the template before any
  filing was fetched (write-early protocol); committed after each gate, by file name.
- **Documents fetched and read:** eleven Roku 10-Ks (FY2015 figures via the FY2017 filing
  through FY2025), the Q2 FY2026 10-Q, four 8-Ks (the merger agreement, the segment recast, the
  Q2 earnings furnishing, the DOJ Second Request), four EX-99.1 shareholder letters (Q3 2025
  through Q2 2026), and the 2026 DEF 14A. Eleven peer primary documents for the competitor row.
  Artifacts and extraction scripts in `Test Runs/_research 2026-09-12 ROKU/`.
- **Priors in the brief that were REFUTED:**
  1. *"an advertising platform whose early years straddle zero"* (the PINS analogue) — **the
     straddle is not in the early years. Fourteen of sixteen constructions are negative,
     including the five-year default window, and the only positive ones are FY2025 and the TTM.**
  2. *"ARPU is not a price … the PINS run found ARPU rising 46% while the money segment's users
     fell. Run the same decomposition"* — **run, and it comes out inverted: users rose 49% while
     ARPU rose 1.1%.** The Precision Steel shape is present, but in the *streaming-player unit*
     series, not in ARPU.
  3. *"Devices … historically sold at or below cost"* — true, but the brief's framing misses that
     **OEM-licensed Roku TV models "account for the largest portion of our overall unit volume"**
     and cost Roku no device margin at all; the Devices gross loss is the minority channel.
  4. *"net cash and little debt is my expectation — check it"* — **confirmed and then some:
     $2,557M liquid, zero interest-bearing debt, $1,055k of interest paid in FY2025.**
  5. *"check whether the contract-liability balance is customer money on the balance sheet"* —
     **only 44% of it is. The larger half is an accounting allocation of cash already collected
     at the point of a device sale.**
- **Priors that were CONFIRMED:** the [E2-49] withdrawal prior (on all three series at once, a
  first for this queue); the Q2-OUT prior on [E3-03] criterion (2); the [E4-29] prior on Adjusted
  EBITDA; the Q1 segment-split prior (the split does kill a claim the consolidated numbers
  supported, as at AMAT and SHOP).
- **DEFECTS FOUND — in the brief:**
  1. **The brief does not contain the single most important fact about this security: Roku signed
     a definitive merger agreement with Fox Corporation on 2026-06-14.** Neither does the queue
     row, which reads `newest_periodic 2026-06-30` — a periodic filing whose own EX-99.1 says
     *"In light of the pending transaction, we will not host an earnings call and will not
     provide a financial outlook."* The screen reads the XBRL of the 10-Q and cannot see Item
     1.01 of an 8-K, which is a structural blind spot worth a guard: **a `merger_flag()` that
     tests for an 8-K Item 1.01 or a DEFM14A since the last 10-K would have caught it, and the
     same blind spot will recur on every name in the queue that gets taken over.**
  2. The brief calls the 351% line *"the CONTRACT-LIABILITY line"* and asks what it is at Roku.
     Answered — but the brief's two precedents (DELL's payables swing, INOD's $116M customer
     prepayment) primed the wrong shape. **At Roku the flag is a small-denominator artifact and
     the real working-capital events are untested lines.**
- **DEFECTS FOUND — in the tooling:**
  1. **`wc_note` divides one balance-sheet delta by a single year's operating cash.** On any year
     whose operating cash is near zero every routine delta reads as a giant percentage, and the
     flag then reports the smallest movement in the statement. Roku FY2022: the flag names
     `Deferred revenue` at +$41.4M and cannot see `Content assets and liabilities, net` at
     −$313.2M in the same column. **Same defect family as the `ZeroDivisionError` that made MU
     and INTC re-triage as UNPRICED: near-zero denominators.** The fix is not a threshold — it is
     to report the delta as a share of **revenue** or of the **largest working-capital line**
     alongside the operating-cash ratio, and to flag the largest movement rather than one chosen
     tag.
  2. **`oe_bottom` and `oe_top` are again two different windows on the same name** (five-year and
     three-year, both at the capex end), advertised as a spread. Found on INTC 2026-09-07,
     unfixed, and it recurs here.
  3. **No working-capital flag reads the content-asset line**, which is the largest
     working-capital line in Roku's cash-flow statement in every one of the last four years and
     is this business's real capital expenditure.
"""
t = t.rstrip() + "\n" + log
open(p,'w',encoding='utf-8').write(t)
print('ok', len(t))
