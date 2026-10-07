
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Q1, Q2, Q3 and Q4 all returned IN, so this output is reportable under operator protocol 2.** It is not headed
"COMPUTATION — NOT A CLEARANCE", because the hard sequence was satisfied before it was run.

### THE PAIR IS STRUCK FRESH, AND BOTH PAIRS ARE RECORDED
**[E4-15]** asks for *"the currently observed rate"*, and Step 0's pair is five days old, so both were struck again.
- **Struck at Step 0 on 2026-09-13, left as filed and NOT used below:** USD 30-year **5.35%** (09/11/2026); price
  **US$86.80** (close of 2026-09-11); cap **US$69,194.6M**.
- **STRUCK FRESH THIS SESSION, 2026-09-18, and used for every figure below:**
  - **Sovereign: USD 30-year 5.29%, dated 09/17/2026, US Treasury daily par yield curve** — the issuing authority, through
    `tools/sources.py sovereign("USD")`. **Not FRED**, which is the fallback only. 09/17 is the latest business day the
    curve carries on 2026-09-18.
  - **Price: US$87.73, close of 2026-09-17**, through `tools/sources.py price()`. **Aggregator, flagged: live quote only.**
    *Cross-checked against a primary filing, which is a stronger check than usual: the eight Forms 4 filed 2026-09-15 report
    RSU-vesting tax withholding at* **$86.80** *on 2026-09-11 — the identical figure the same aggregator gave Step 0 for that
    date.*
  - **Share count re-confirmed, not inherited:** **797,172,829**, from the cover of the 10-Q for the quarter ended
    2026-06-30, accession **`0000021665-26-000042`**. **EDGAR was re-queried on 2026-09-18** (CIK 0000021665): the only
    filings since 2026-09-13 are **eight Forms 4 dated 2026-09-15**, all transaction code **F**, *"Withholding of shares for
    payment of tax liability incident to the vesting of restricted stock units"* — no open-market sale, and **no new 10-Q,
    10-K or 8-K**. The cover count therefore stands and the split factor after the measurement date is **1.0**.
  - **MARKET CAP, recomputed on the fresh close: 87.73 × 797,172,829 × 1.0 = US$69,936.0M.**
- **FX:** none. The quote is in USD on the NYSE and the statements are in USD. The currency argument for using the USD
  sovereign against a two-thirds-international earnings stream was made at Step 0 and is not re-opened.

### 1. THE YIELD — owner earnings over market cap, beside the sovereign
*(Arithmetic in `resume/q5.py`. Owner-earnings windows are Q4's, unchanged.)*

| window | owner earnings $M | yield on $69,936M | multiple | points vs the 5.29% sovereign | expectancy = yield + realised growth (5.3%) | vs the ~10% floor |
|---|---|---|---|---|---|---|
| most conservative (10-yr, working-capital release stripped) | 2,680 | 3.83% | 26.1x | **-1.46** | 9.13% | **-0.87** |
| 10-yr 2016-25 | 2,738 | 3.92% | 25.5x | **-1.37** | 9.22% | **-0.78** |
| **5-yr 2021-25 — the [E2-42] DEFAULT** | **2,833** | **4.05%** | **24.7x** | **-1.24** | **9.35%** | **-0.65** |
| 3-yr 2023-25 | 3,269 | 4.67% | 21.4x | **-0.62** | 9.97% | -0.03 |
| TTM to 2026-06-30 *(one year, not a mean)* | 3,680 | 5.26% | 19.0x | **-0.03** | 10.56% | +0.56 |

**On every window, including the trailing twelve months, the owner-earnings yield is BELOW the thirty-year Treasury.**
The growth term is the only thing that lifts the expectancy above the bond, and it is the realised 2016-2025 compound rate of
owner earnings per diluted share (**$2.70 to $4.29, +5.3% a year**) taken at face value — which is generous, because Q2 showed
that growth was price and that most of the price was devaluation recovery.

### 2. WHAT THE PRICE ALREADY ASSUMES
| window | perpetual growth in owner earnings per share needed to reach the ~10% floor | needed merely to match the 5.29% bond |
|---|---|---|
| most conservative | **6.17%/yr** | 1.46%/yr |
| 10-yr | **6.08%/yr** | 1.37%/yr |
| **5-yr default** | **5.95%/yr** | **1.24%/yr** |
| 3-yr | 5.33%/yr | 0.62%/yr |
| TTM | 4.74%/yr | 0.03%/yr |

**Against what the business has actually done:** +5.3% a year in owner earnings per share over 2016-2025, of which about
**1.1 points a year came from the share count alone** (898.4M diluted to 811.1M) and the rest from price, with **worldwide
unit volume up 7.7 points in ten years and the Oral, Personal and Home Care segment up 2.9**. **So $87.73 requires the best
decade the filings show, repeated in perpetuity, and slightly bettered.**
- **[E4-35] is NOT the binding constraint here and is not misapplied:** 5.95% is not a claim of *"15% annual growth in
  earnings-per-share"*, so the fewer-than-10-of-200 base rate does not fire. **What fires instead is [E4-44]'s second bound** —
  *"the value of an asset, whatever its character, cannot over the long term grow faster than its earnings do"* — and the
  earnings growth on offer is the pricing Q2 measured.
- **State the ceiling too [E2-63].** The upside is bounded, and the bound is nameable: return on average net tangible
  operating assets is already **79%-101% pre-tax** and cannot usefully rise, so growth must come from units, price or the
  share count. Units have been flat for a decade; hard-currency pricing has run at about 1% a year; the buyback adds about 1.1
  points a year and is itself being done at $78.54-$95.90 a share. **There is no source of a step change in the filings.**

### 3. WHAT YOU ARE PAID — and the value range, in round numbers [E4-01]
**Value per share at the [E4-28] floor, at three growth assumptions, value = owner earnings / (10% − g):**

| window | g = 5.3% *(the full realised decade rate, granted)* | g = 3.0% *(hard-currency pricing ~1% + buyback ~1.1% + a point)* | g = 0% *(static)* |
|---|---|---|---|
| most conservative | $71.53 | $48.03 | $33.62 |
| 10-yr | $73.08 | $49.07 | $34.35 |
| **5-yr default** | **$75.61** | **$50.77** | $35.54 |
| 3-yr | $87.25 | $58.58 | $41.01 |
| TTM | $98.22 | $65.95 | $46.16 |

**THE RANGE, in round numbers as [E4-01] requires: roughly $50 to $75 a share on the corpus's default five-year window,
widening to roughly $50 to $90 only if the three-year window and the full decade growth rate are both granted at once.**
The quote is **$87.73**.

**No end margin is subtracted on top, and the reason is stated.** *"you don't try and put too much windage in at every level
... And then when you get all through, you apply the margin of safety"* **[E4-11]**. **Q4 already spent conservatism twice and
counted it** (c) set at total capex rather than the depreciation default, and the working-capital release stripped. Applying a
third discount here would be exactly the stacking the framework forbids. **The range above is therefore the honest value, not a
value net of margin; the margin is what the gap between it and the price would have to be, and there is no gap.**

**Bar 2, the screamer test [E4-01, E3-25]:** the conservative end of the range is about **$48-$51**. The price is **$87.73**.
It does not *"scream"*; it sits **above the whole default-window range** and only inside the widest range if two optimistic
choices are made together. **Bar 2's answer for this cell of the table is "no".**

- **THE FLOOR COMES FIRST, AND IT IS NOT CLEARED.** *"that's the figure we quit on ... we don't want to buy equities where our
  real expectancy is below 10 percent. Now, that's true whether short rates are 6 percent or whether short rates are 1
  percent"* **[E4-28]**. On the corpus's own default five-year window the honest pre-tax expectancy at $87.73 is **9.35%**,
  **0.65 points below the floor** — and that figure already grants the full realised decade growth rate. On the ten-year window
  it is 9.22%. Only the trailing-twelve-months reading, a single year rather than a mean, clears it, at 10.56%.
- **RANKING POSITION: NOT RANKED.** A candidate below the floor *"is not ranked — it is quit on, however it compares with the
  bond of the day."* It is not placed in `PORTFOLIO.md`'s ranked opportunity set as an actionable line.
- **VERDICT: the business is IN and the price is not.** **[ ] IN at this price**  [ ] UNRESEARCHED  [ ] UNKNOWABLE →
  **the four business gates are IN; Q5 returns BELOW THE [E4-28] FLOOR at $87.73, NOT RANKED, WATCH-LIST ONLY.**
  *This is the ASML shape of 2026-08-28 and the PNR shape of 2026-09-01, not a finding against the business. **[E5-42]** is the
  reason the two are reported separately: business quality is *"the capital actually needed in the business"*, and *"whether
  it's a good investment for us depends on how much we pay for that in the end."* Colgate needs very little capital and costs
  24.7 times a conservative year's owner earnings.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No position is held** (CL has no row in `PORTFOLIO.md`), so this section sets the yardsticks **prior to the act**
**[E1-02]** — the entry conditions, and the conditions under which the four IN verdicts above should be re-read as wrong.

### A. THE PRICE LINES, pre-committed, and armed because the business cleared all four gates (the QLYS ruling)
- **$75.61 — the five-year floor value with the full 5.3% decade growth rate granted.** At or below this, the ~10% floor is met
  **on the most generous growth assumption the record supports**. **Action: a full v4.1 re-run, not a purchase** — the growth
  assumption must be re-tested against the then-current share and volume series before it is spent.
- **$50.77 — the five-year floor value on g = 3.0%**, the growth the hard-currency pricing record and the buyback actually
  support. At or below this the floor is met **without granting the devaluation-recovery pricing**. **Action: a full v4.1
  re-run, and this is the price at which the name would be expected to rank.**
- Both are armed in `tools/alerts.json` as **prompts to read, never verdicts**, in the PNR two-band form.
- **These lines expire at the next 10-K.** The bands are derived from owner earnings and must be re-derived when the FY2026
  10-K lands (expected February 2027), per the alerts file's own standing note.

### B. WHAT WOULD PROVE Q2 WRONG — the moat downgrade, and [E4-17] says it arrives slowly
*"we sell — really when we ... reevaluat[e] the economic characteristics of the business ... And those beliefs change quite
gradually."* **[E4-17]**. Each of these is an annual read off the 10-K, not a quote to watch:
1. **Global toothpaste share falls below 39.4%** (the 2021 trough) in any full year. The class NARROW would be re-read as
   NONE, because the 2022-2025 re-widening would have failed.
2. **North American net selling price is negative for a third and a fourth consecutive year.** Two years is the [E4-37] agony
   signal already recorded; four would make it the state of the business rather than a cycle.
3. **Advertising passes 14.0% of net sales while global toothpaste share is still below 41.3%.** That is the cost of holding
   position rising again with nothing bought.
4. **Worldwide volume is negative in two consecutive full years.** [E4-55]'s physical series is the honest one, and two
   negative years would end the "franchise, narrowed" reading.
5. **The Personal and Home Care third loses segment margin while Latin America, Asia Pacific and Africa/Eurasia begin to
   follow North America's path.** That is Q4's named death — **#19 THE SHELF** — spreading beyond the concentrated-retail
   third, and it would move the likelihood from *low-level possibility* to *real possibility* for the whole company.

### C. WHAT WOULD PROVE Q3 WRONG
6. **A fourth impairment of an acquired brand**, or any new adjacency purchase above $1bn while the core's share is falling.
   That is **[E3-40]**'s loss of focus and **[E2-56]**'s camouflage confirmed rather than flagged, and **[E4-24]** is the
   corpus's answer to it: *"you'll probably do better to get out"*, not to engage.
7. **An EBITDA or adjusted-EBITDA measure appearing in any release or filing [E4-29]**, where today the sweep returns zero
   files.
8. **Restructuring charges rising above about 5% of base operating profit**, roughly double the decade's 2.5%, without a
   filed statement of what is being rebased and for how long **[E5-33]**.

### D. WHAT WOULD PROVE Q4 WRONG
9. **Interest cover after capital expenditure falls below 8x** (it is 13.5x), or **operating cash flow falls below $3.0bn in a
   year the filings do not attribute to a raw-material shock**.
10. **Cash and the revolver arrangement change** such that commercial paper is not fully backstopped — strength 2 of
    **[E5-11]** already fails, and this is the line at which that failure would start to matter.

### E. THE STANDING NOTE
**No band, and no entry, repairs a gate.** If any condition in B fires, the price lines in A are void until a fresh run is
done, because a moat downgrade changes the owner-earnings growth term the lines are built on. **And the reverse: a fall to
$50.77 on a business that has failed B is not an opportunity, it is a re-rating.** *"what is smart at one price is dumb at
another"* **[E5-08]**.
