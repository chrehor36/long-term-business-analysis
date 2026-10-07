## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

### The entity, in every year used
CIK 0001040470, `submissions.json` (fetched by this run): *"AEHR TEST SYSTEMS"*, SIC *"Instruments For Meas & Testing
of  Electricity & Elec Signals"*, no former names. One California corporation since 1977 (*"incorporated in California in
May 1977"*, FY2026 10-K Note 1); no reverse recapitalization, no shell, no conversion (the DJT check was run and does not
apply). `submissions.json` gives `fiscalYearEnd` **1231**, which is wrong: every 10-K in the index reports a May period
end (FY2026 ended 2026-05-29, FY2025 2025-05-30, FY2024 2024-05-31). **And the fiscal year is changing:** FY2026 10-K Note
1, *"On April 2, 2026, the Company's board of directors approved a change in the Company's fiscal year-end from the 52- or
53-week period ending on the Friday nearest May 31 to the 52- or 53-week period ending on the Friday nearest June 30. The
change will be effective beginning in fiscal year 2027, which begins on June 27, 2026 and ends on June 25, 2027."* The
four weeks from 2026-05-30 to 2026-06-26 are a transition period no filing yet covers. Every year used below is a May
fiscal year, FY2017-26.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list: *"revenue step
or cross-accession restatement above threshold."* **A prompt to read, never a verdict.** Reproduced by the brief-writer
against `Screens/floor_screen.py` at `a8bc84f` (`floor_screen_a8bc84f.py`) over companyfacts cut to facts filed by
2026-09-01 (`triage_repro.py`, `triage_repro_out.txt`, re-read by this run):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | 1.098 | no | ordinary issuance: the Incal stock (552,355 shares, July 2024), ATM sales and employee plans; no split (`split_factor_after` 1.0). A dei element exists (the RIVN None check was run); single class. |
| **2. `scale_shift`** | **3.062** | **YES: THE GUARD THAT RETURNED AEHR UNPRICED** | **A REAL ORGANIC REVENUE STEP, ONE CUSTOMER'S CAPACITY BUILD. Not a perimeter and not a restatement.** FY2021 $16.6M to FY2022 $50.8M under `RevenueFromContractWithCustomerExcludingAssessedTax`, **consecutive fiscal years, same element on both sides** (the TSLA check was run: that element carries every year FY2017-26; `Revenues` carries the same totals). The FY2022 10-K MD&A (`0001654954-22-011877`): *"Net sales increased to $50.8 million for the fiscal year ended May 31, 2022 from $16.6 million for the fiscal year ended May 31, 2021, an increase of 206.2%. ... Net sales of our wafer-level products for fiscal 2022 were $48.9 million, and increased approximately $33.9 million from fiscal 2021 due to stronger demand related to silicon carbide applications."* Risk factors, same 10-K: *"During fiscal 2022, ON Semiconductor accounted for approximately 82% of the Company's net sales."* **No acquisition in FY2021-22** (no business-combination payment on either cash-flow face); the one acquisition in the window is Incal, FY2025 (below). The later steps (1.278, 1.019, 0.891, 0.848) are the same customer class peaking and falling away. |
| 3. `filed_years` | 17 | no | |
| 4. `owner_earnings` | 5y -$4.84M D&A end / -$5.44M capex end | (not reached) | OCF less SBC less (c); reproduced from the filed faces at Q4 |
| (`restatement_shift`, not a guard in that pipeline) | (1.0, FY2018) | n/a | a null, as at SMCI, SNOW, TSLA, RIVN, DJT and BX |

**No restatement exists**: no 10-K/A, 10-Q/A or NT filing in the 1,005-row filing index (`filings_list.txt`); the FY2026
10-K cover leaves the error-correction box unticked (*"reflect the correction of an error to previously issued financial
statements. ☐ Yes ☒ No"*). One presentation change was found and is carried rather than smoothed: FY2022 D&A is
*"Depreciation and amortization | 307"* on the FY2022 10-K face and **356** on the FY2024 10-K face
(*"Depreciation and amortization | 657 | 450 | 356"*, FY2024/23/22), a reclassification of $49K; immaterial, and the later
face is used.

**So the label was, for AEHR: a real organic revenue step, the start of one customer's silicon-carbide capacity purchases
(onsemi, 82% of FY2022 sales), on consecutive years and one element.** The same class as SNOW's, RIVN's and DJT's
step, except that this one was **made by a single buyer**, and the buyer's share is the Q2 fact.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by
  this run at 20:41 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned the cached **09/17/2026 5.29%** row half a second later (`step0_out.txt`): the
  stale-cache defect, reproduced a sixth time. The issuing-authority figure is used. FRED not used. Not inherited from BX
  (the figure agrees because it is the same day's print).
- **Earnings currency: USD.** The company reports in dollars; 59% of FY2026 sales were *"attributable to sales to
  customers for delivery outside of the United States"* (FY2026 10-K Item 1A), invoiced as reported in dollars. No FX or
  ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$93.49, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("AEHR", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 93.49,
  `regularMarketTime` 1789761601 = 20:00:01 UTC = **16:00:01 EDT**, so the figure is the closing print. The day's bar had
  not finalised (open 92.02, high 93.90, low 87.15, close None; the BX run recorded the same None). `tools/sources.price()`
  returned the same 93.49 stamped 2026-09-18.
- **The quote moves violently, and the run records it rather than choosing a day:** 08-19 $107.96 · 08-28 $80.81 · 09-01
  $76.59 · 09-11 $94.69 · 09-14 $83.37 · 09-17 $90.55 · 09-18 $93.49. Insider Form 4 open-market sales in August were at **$100.70 to
  $143.77** (`form4_table.txt`); the FY2026 10-K: *"during the two-year period ended May 29, 2026, the price of our common stock has
  ranged from $6.27 to $112.00."* The screen's 2026-09-01 cap ($2,520M) was struck at about $77.
- **Primary-filing cross-check:** Form 4 `0001040470-26-000265` (Didier Wimmers, filed 2026-09-03) reports shares
  withheld for tax on **2026-09-03 at $76.27**, which is the Yahoo close for 2026-09-03 to the cent (76.27); Form 4
  `0001040470-26-000263` (Chris Siu, CFO) reports withholding on **2026-09-01 at $76.59**, the Yahoo close for 2026-09-01.
  **The aggregator's series is corroborated on two dates; no Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-07-20): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession
- **32,620,450 shares of common stock**, from the cover of the **FY2026 Form 10-K** (fiscal year ended 2026-05-29, filed
  **2026-07-27**, accession **`0001654954-26-006919`**): *"The number of shares of registrant's common stock, par value
  $0.01 per share, outstanding at July 20, 2026 was 32,620,450 ."* `Screens/cover_shares.py AEHR` returns the same figure
  and accession (*"(single class / undimensioned) 32,620,450"*). **This is the latest periodic filing**: no 10-Q has
  followed (the first FY2027 quarter ends in late September 2026 under the new June year).
- **Sold after the cover date:** nothing found. The April 2026 ATM was *"fully utilized"* (8-K `0001654954-26-003746`,
  2026-04-20); an automatic shelf **S-3ASR** was filed the same day as the 10-K (`0001654954-26-006922`, 2026-07-27) and **no
  prospectus supplement (424B) has been filed under it** in the index to 2026-09-10. Post-cover Form 4s are RSU vesting,
  tax withholding and open-market sales by insiders (existing shares).
- **Dilution not in the count:** 316,000 options (weighted exercise price $5.11) and 707,000 unvested RSUs and PRSUs at
  2026-05-29 (FY2026 10-K equity note), 3.1% of the cover count; 2,997,000 shares remain available under the 2023 plan. Shown
  beside the cap, not in it (the cover is the rule).

### The market cap
**$93.49 x 32,620,450 = US$3,049.7M ($3.05bn).** With the options and unvested awards: $3,145M. Split factor 1.0. Public
float on the cover: *"$ 671,378,691"* at *"the closing price of $22.97 on November 28, 2025"*; the price has quadrupled
since the float date.

### THE DEAL CHECK: none live
`sources.deal_filings("0001040470")` returned no deal forms since the annual report of 2026-07-27, and `deal_note` returned
empty (`step0_out.txt`). Read on the index: **no 425, S-4, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D filed on this
registrant.** The 8-Ks carrying Item 1.01 in the last three years are the ATM sales agreements (2023-02-08, 2026-04-08) and
the Incal purchase (2024-07-16, with Item 3.02 for the stock consideration); Item 2.01 appears on 2024-08-01 (Incal
closing) and on 2022-07-19, where the document itself reads *"Item 2.02. Results of Operations and Financial Condition"*: an earnings release indexed as 2.01, the mistagging class the RESUME STATE records for PAY.
**The quote is not a spread and buys this company.**

### The perimeter: one acquisition inside the window, and the cash
- **Incal Technology, Inc., closed 2024-07-31** (FY2025 10-K Note 4, `0001654954-25-008553`): *"The acquisition date fair
  value of the consideration transferred for Incal was approximately $ 22.2 million"*: cash $10,631K, *"Common stock under
  transfer restriction"* $9,381K (552,355 shares), escrow $2,381K, working capital $(240)K. Assets: intangibles $12,000K
  (developed technology $9,130K over 12 years), goodwill $10,719K, inventory $2,558K. **What it added:** *"$ 18.6 million in
  revenue and $ 3.8 million in net income contributed by Incal from the date of acquisition through May 30, 2025"* (FY2026
  10-K Note 4); the package-level line it became was **$19.8M in FY2025 and $18.5M in FY2026, 34% and 37% of revenue**.
  Cash paid: $11,075K in FY2025 and $1,801K in FY2026 (*"a $1.8 million escrow release"*, FY2026 MD&A), the brief's
  `acquisition_flag` $12.9M. What it added to D&A: intangible amortization of about $1.2M a year (intangibles $10,781K to
  $9,552K in FY2026), inside the D&A line from FY2025. **Q4 carries it.**
- **The cash is new, and it was raised, not earned.** Cash $116,358K at 2026-05-29 against $24,529K a year earlier;
  *"net proceeds of $97.4 million from the issuance of common stock under the Company's ATM offering program"* (FY2026
  MD&A). The equity note: 384,380 shares at an average $25.89 (November 2025), 269,439 at $39.20 (February 2026), 476,649
  at $40.88 (March 2026), and 812,185 at $73.87 (April 2026): **1,942,653 shares for about $100.0M gross, an average of
  $51.48**. No debt: the Silicon Valley Bank facility was terminated on 2024-01-04 with nothing drawn (8-K
  `0001654954-24-000428`: *"There are no financial covenants in the Loan Agreement. No amounts were outstanding"*).

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K**, fiscal year ended 2026-05-29, filed **2026-07-27**, accession **`0001654954-26-006919`**
  (`10K_FY2026.txt`).
- Also read: FY2019-25 10-Ks (`0001654954-19-010095`, `-20-009618`, `-21-009505`, `-22-011877`, `-23-011271`,
  `-24-009642`, `-25-008553`) for the FY2017-25 statements and customer notes; the Q3 FY2026 10-Q (`0001654954-26-003348`);
  the DEF 14A of 2026-09-09 (`0001654954-26-008222`); the 2023, 2024 and 2026 ATM prospectus supplements; the 8-K earnings
  releases (EX-99.1) of July 2022 to July 2026; the Incal and ATM 8-Ks; 156 Form 4 transactions filed since 2025-06-01
  (`form4_table.txt`).
- **Figures cross-checked against the filed statement** (FY2026 10-K consolidated statement of cash flows, $K, FY2026 /
  2025 / 2024): *"Net cash provided by (used in) operating activities | (3,310) | (7,400) | 1,756"*, *"Stock-based
  compensation expense | 6,761 | 5,162 | 2,518"*, *"Purchases of property and equipment | (2,066) | (4,992) | (749)"* and
  *"Payments for business acquisition, net of cash and cash equivalents acquired | (1,801) | (11,075) | -"* match
  companyfacts to the thousand; revenue *"$50,001 | $58,968 | $66,218"* matches. The FY2017-23 faces (FY2019, FY2020,
  FY2021, FY2022 and FY2024 10-Ks) match the tagged OCF series in the brief to the thousand.
