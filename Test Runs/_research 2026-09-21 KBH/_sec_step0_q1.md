## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year constant maturity**, file
  `daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve`, downloaded
  2026-09-21 and saved to `Test Runs/_research 2026-09-21 KBH/treasury_daily_par_yield_2026.csv`.
  **Struck fresh, not inherited from the brief.** 2026-09-18 is the newest row in the file (a
  Friday; the 2026-09-21 curve had not posted when this run fetched it). Neighbouring rows, so
  the reader can see how much the rate moves: 09/17 5.29, 09/16 5.35, 09/15 5.36, 09/14 5.34.
  **FRED DGS30 was not used and was not needed.**
- FX if the quote and the earnings differ in currency: **n/a — KB Home builds and sells homes
  in nine US states and reports in USD.** No foreign operations, so **[E3-66]**'s
  where-do-shareholders-stand-in-the-queue test is not engaged.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K, FY ended 2025-11-30, filed 2026-01-23, accession 0000795266-26-000017**
    (`kbh-20251130.htm`) — the primary document.
  - **10-Q, quarter ended 2026-05-31, filed 2026-07-09, accession 0000795266-26-000063**
    (`kbh-20260531.htm`) — the newest periodic.
  - **8-K / EX-99.1 earnings release, 2026-06-23, accession 0000795266-26-000060**
    (`exh991kbh-earningsrelease0.htm`) — pulled BEFORE Q3 was scored, per the CGNX standing
    instruction.
  - **DEF 14A, filed 2026-03-13, accession 0001308179-26-000068.**
  - **10-K, FY ended 2019-11-30, filed 2020-01-24, accession 0000795266-20-000007** — pulled
    to resolve the `da_note`, and it did resolve it. See Q4.
- figure cross-checked against the filed statement: **net cash provided by operating
  activities, FY2025.** The XBRL tag `NetCashProvidedByUsedInOperatingActivities` returns
  $335.7M; the filed CONSOLIDATED STATEMENTS OF CASH FLOWS reads **`335,682`** (in
  thousands). Match. Two more checked in passing: D&A **`37,303`** and stock-based
  compensation **`46,238`**, both agreeing with the tagged series.

### THE NEWEST-FILING COLUMN IS A REPORT DATE — the APOG tooling defect, confirmed again
The screen row says `newest_filing: 2025-11-30`. That is the **report date of the FY2025
10-K**, not a filing date. From `submissions.json` the true newest filing is a **Form 4 of
2026-08-07**, and the newest *periodic* is the **10-Q of 2026-07-09**. **No Q3 filing (quarter
ended 2026-08-31) exists as of 2026-09-21** — checked on EDGAR rather than assumed either way:
the recent-filings array ends at 2026-08-07. So the newest public operating read is the
2026-06-23 EX-99.1, and **the Q3 print is imminent and is not in this file.** Any reader
returning to this run after late September 2026 has a document I did not have.

### THE CAP, STRUCK BY HAND — and what the cap_flag actually showed
**Operator rule 4. The flag was not inherited; it was tested.**

| input | value | source |
|---|---|---|
| close | **$47.12** | 2026-09-18, Yahoo Finance chart API — **AGGREGATOR, FLAGGED**, live quote only; raw JSON saved to `price_KBH_yahoo_raw.json` |
| shares outstanding | **61,309,728** | **cover page of the 10-Q for the quarter ended 2026-05-31**, accession **0000795266-26-000063**: "There were 61,309,728 shares of the registrant's common stock, par value $1.00 per share, outstanding on May 31, 2026." |
| splits after the measurement date | **none** — the split-events query returns null and KBH has not split since before 2017 | |
| **cap = close x shares** | **$2,888.9M, call it $2,890M** | |

**The flag said: "A cap cannot be smaller than a subset of itself. One of the two is wrong."
It is wrong, and this run can show it by exact arithmetic rather than by argument.**

- The filed float is **$3,510,028,491** as of **2025-05-31** (10-K cover, accession
  0000795266-26-000017).
- Shares outstanding on **2025-05-31** were **68,050,184** (cover of the 10-Q for that
  quarter, accession 0000795266-25-000081).
- KBH's close on **2025-05-30**, the last trading day before that date, was **$51.58**.
- **68,050,184 x $51.58 = $3,510,028,491.** To the dollar.

So the "float" KB Home files is simply **every outstanding share priced at the May 2025
close** — the registrant reports no meaningful affiliate holding. The filed float is not a
subset of any later cap; it is **the whole market capitalisation on a date fifteen months
earlier**. The screen's $3,217M and the filing's $3,510M are both correct and are eleven
months apart, and the hand-struck $2,890M is correct on a third date. **Nothing is wrong.
This is the sixth consecutive firing of the flag and the sixth consecutive time its stated
conclusion has been false.** Its real content, once decoded, is a fact about the price and
the buyback: KB Home's market value is down **17.7%** from its May-2025 level, of which
**9.9 percentage points** is price ($51.58 to $47.12) and the remainder is the **6.74 million
shares retired** in between.

**RECOMMENDATION FOR THE TOOLING, recorded and not acted on** (operator rule 8 — a tool may
not conclude): the check should compare the filed float **against a cap struck on the float's
own as-of date**. It currently compares two different dates and reports the difference as an
error. Three of the four inputs it needs — cover float, cover share count, cover as-of date —
are already in the document it parses.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** KB Home buys parcels of land in
  49 major markets across nine states, pays to get water, sewer, roads and grading into them,
  puts a house on each lot using subcontracted trades, and sells the house to a retail buyer.
  In FY2025 it sold **12,902** houses at an average of **$481,400**, took **$6.21 billion** of
  housing revenue, and kept **18.6%** of that as gross profit after land and construction.
  Selling and overhead took **10.4%** of revenue, leaving an **8.2%** homebuilding operating
  margin. A second, small segment collects title and insurance commissions and an equity share
  of a mortgage joint venture (KBHS) that financed **85%** of its buyers; in FY2025 financial
  services contributed **$47.1M** of pretax income against **$507.1M** from homebuilding.
  *(FY2025 10-K MD&A, accession 0000795266-26-000017.)*
  **In one line: it is a land-inventory business with a construction service attached.** The
  money is the spread between what a finished house sells for and what the dirt plus the
  sticks cost, and the capital is not plant — it is **$5.67 billion of land and half-built
  houses** on the balance sheet, **85% of total assets** ($5,670.8M of $6,680.3M at
  2025-11-30). That single fact governs everything at Q4: for this business, **inventory is
  the capital account**, and it runs through operating cash flow.
- **The scarce input this business controls:** **entitled, developed lots in specific
  submarkets** — and the filing says plainly that it does *not* control them, it competes for
  them: *"We compete for homebuyers, construction resources and desirable land against
  numerous homebuilders"* (FY2025 10-K, Item 1, Competition). KB Home owns or has under
  contract **59,106 lots** (10-Q, 2026-05-31), of which about **62% owned, 38% under
  contract**. It controls nothing else in the chain: the trades are subcontracted, the
  materials are in its own words *"standardized materials that are commercially available on
  competitive terms from a variety of outside sources"* (FY2025 10-K), and the buyer's
  mortgage comes from a joint venture it does not consolidate.
- **Will the fundamentals look broadly the same in ten years?** **Yes.** Americans will still
  buy detached houses in Phoenix, Dallas and Jacksonville; the sequence land, entitlement,
  development, construction, sale has not changed in seventy years, and KB Home says it has
  *"built over 700,000 quality homes in our nearly 70-year history"* (EX-99.1, 2026-06-23).
  This is **[E3-31]**'s *"relatively simple and stable in character"*. What is **not** stable
  is the *level* of activity and price — but that is a cyclicality finding for Q4 and Q5, not
  an understanding failure. **[E5-29]** is explicit that *"Volatility is far from synonymous
  with risk"*, and **[E3-55]** that a business whose mechanism is certain may have a very
  bouncy annual figure without that being a defect in the analysis.
- **[E4-46] check — is this a five-minute business or a five-month one?** Five minutes. There
  is no technology to forecast, no reserve estimate to take on trust, no regulated rate base.
  The one genuinely hard judgment, land-value impairment, is disclosed on its own line
  (*"Inventory impairments and land option contract abandonments"*, $32.1M in FY2025) and is
  therefore visible rather than buried.
- **VERDICT: [x] IN**

