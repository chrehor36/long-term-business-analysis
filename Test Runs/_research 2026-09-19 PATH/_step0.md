## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (just after midnight EDT); the template was copied and committed before any fetch
(`71c902c`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the third name in
the "no share count from dei: read the cover" row (META and DASH were the first two). Research, scripts and downloaded filings
are in `Test Runs/_research 2026-09-19 PATH/`. **No PATH row exists in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**
(the triage skip reason says why), so there is no screen row to carry. Every figure below is from UiPath's own filings, fetched
by this run, with the accession.

### The entity, in every year used
CIK 0001734722, `submissions.json` (fetched by this run): *"UiPath, Inc."*, SIC 7372 *"Services-Prepackaged Software"*,
`stateOfIncorporation` **"DE"**, `fiscalYearEnd` **0131**, no former names, ticker PATH on NYSE. **The charter has not moved:**
the 8-K of 2026-09-03 (`0001734722-26-000047`) gives *"Delaware"* on its cover, the FY2026 10-K says the company *"was
incorporated in Delaware in June 2015"* and *"because we are incorporated in Delaware, we are governed by the provisions of
Section 203"*, and the 10-K exhibit index carries one certificate of incorporation, the 2021 one (*"3.1 | Amended and Restated
Certificate of Incorporation of UiPath, Inc. | 8-K | 001-40348 | 3.1 | 04/28/2021"*); the only later Item 5.03 (2023-03-10)
amended the bylaws. IPO April 2021 (S-1 effective 2021-04-20, 424B4 2021-04-21). One reporting entity throughout. **Fiscal years
end 31 January and are named for the calendar year in which they end: "FY2026" = the year ended 2026-01-31; "Q2 FY2027" = the
quarter ended 2026-07-31.**

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The probe (`_probe_screen.py`,
copied from DASH's with the CIK and ticker changed; output `_probe_screen_output.txt`) shows companyfacts carries **one** dei
element for UiPath, `EntityPublicFloat` (five facts, FY2022-26 10-Ks), and **no `EntityCommonStockSharesOutstanding` at all**;
`share_count_shift` returned **None** under both the current screen and `a8bc84f` (not measured, not stable: the RIVN
reading), and `shares_outstanding` returned None. **The META and DASH hypothesis (a dimensioned per-class cover) was tested on
the inline XBRL** of the two latest periodic filings (`dei.py`, output `dei_out.txt`; raw `10Q_2026Q2_raw.htm`,
`10K_FY2026_raw.htm`), and **it holds, in META's form: two classes, both non-zero.** In the Q2 FY2027 10-Q
(`0001734722-26-000050`):

- *"name="dei:EntityCommonStockSharesOutstanding" ... 456,464,703"* in context c-2, segment
  *"dimension="us-gaap:StatementClassOfStockAxis">us-gaap:CommonClassAMember"*, instant 2026-09-03;
- the same element in context c-3, *"us-gaap:CommonClassBMember"*, **64,690,706**.

No `ixt:fixed-zero` class (UiPath has no third class). The FY2026 10-K (`0001734722-26-000012`) tags the same two dimensioned
facts at 2026-03-20 (459,231,166 A; 64,690,706 B). **companyfacts publishes only undimensioned facts, so a cover tagged per class
never reaches it. For PATH the label was the META kind: a tagging convention for a two-class cover, not a missing or stale
count.**

**The other `a8bc84f` guards, on facts filed by 2026-09-01:** `scale_shift` **1.468** (did not fire); `restatement_shift`
**(1.0, FY2021)**, a null and not a guard (the SNOW note). **Unlike DASH, the count was NOT the only thing standing between PATH
and a positive price: `a8bc84f`'s `owner_earnings()` returns NEGATIVE figures at every end** (`{'5y_da': -214.1M, '5y_capex':
-210.9M, '3y_da': -28.9M, '3y_capex': -23.7M}`), so with a count the triage would have priced it at a negative yield. The current
screen returns the same shape (`5y_capex` -211.5M). **Not a verdict**: Q4 rebuilds owner earnings from the filed statements.
Also printed by the current screen and carried to Q4 as a prompt: `working_capital_flag` on FY2023, *"DeferredRevenue moved
$160.7M in 2023 when OCF was $10.0M"*.

**Restatement check:** no 10-K/A or 10-Q/A in the submissions index since the IPO. **Auditor change** read: 8-K of 2022-04-20
(`0001734722-22-000014`, Item 4.01), Grant Thornton dismissed, KPMG engaged, *"not the result of any disagreement"*, with one
reportable event disclosed (a FY2018 revenue-recognition material weakness, *"remediated"* by 2021-01-31). Carried to Q3.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run
  at 00:02 EDT on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** seconds later (`step0_out.txt`): the stale-cache defect
  again (DASH recorded the eighth occurrence; this is the ninth recorded). The issuing-authority figure is used. FRED not used.
  Struck by this run, not inherited from the brief or from DASH.
- **Earnings currency: USD, with a large foreign share** (the geography split is read at Q1). No ADR or FX conversion of the
  quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$13.39, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("PATH", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 13.39,
  `regularMarketTime` 1789761603 = **16:00:03 EDT**, the closing print; the day's bar $13.325-$13.95. `tools/sources.price()`
  returned the same 13.39 stamped 2026-09-18.
- **The month, recorded rather than choosing a day:** 08-19 $15.78 · 08-27 $18.33 · 08-31 $18.67 (the month's high close) ·
  09-03 $18.22 · **09-04 $15.19 (-16.6% on the day after the Q2 FY2027 release and the CFO change)** · 09-09 $13.57 · 09-14
  $14.66 · 09-18 $13.39. **-28% from the 08-31 close.**
- **Primary-filing cross-check (Form 4s, `f4.py`, `form4_table.txt`):** Ashim Gupta (COO) sold 117,339 shares on 2026-09-11 at
  a weighted $13.8539, range *"$13.7400 to $14.4100"* (`0001855778-26-000007`), inside Yahoo's 09-11 range ($13.74-$14.465);
  Raghu Malpani sold 98,429 on 2026-09-16 at $13.8135, range *"$13.5300 to $14.0400"* (`0002127293-26-000008`), inside Yahoo's
  09-16 range ($13.51-$14.08). **The aggregator's series is corroborated on two dates. No Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-09-03): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the class treatment from the charter
- **Class A 456,464,703 + Class B 64,690,706 = 521,155,409 shares**, from the cover of the **Form 10-Q for the quarter ended
  2026-07-31, filed 2026-09-08, accession `0001734722-26-000050`**, the latest periodic filing: *"As of September 3, 2026, the
  registrant had 456,464,703 shares of Class A common stock and 64,690,706 shares of Class B common stock, each with a par value
  of $0.00001 per share, outstanding."*
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's face: *"547,650 and 540,898 shares issued; 456,299
  and 472,346 shares outstanding, respectively"* (Class A, thousands, 2026-07-31 and 2026-01-31) and *"64,691 shares issued and
  outstanding"* (Class B). The cover moves +166K A in 34 days. **Consistent.**
- **After the cover date:** Daniel Dines converted **5,000,000 Class B into Class A on 2026-09-08** (Form 4
  `0001855767-26-000018`, codes C and J; the 8-K of 2026-09-03 announced it with a 10b5-1 plan to sell up to 5,000,000 Class A
  *"through February 1, 2027, subject to limit prices"*). One for one, so the **sum is unchanged**; the class split is now
  about 461.5M A and 59.7M B.
- **Why the classes are added, one for one.** The governing charter is the Amended and Restated Certificate of Incorporation
  (8-K of 2021-04-28, `0001193125-21-135339`, Exhibit 3.1, read as `CHARTER_2021.txt`): dividends *"shall be paid pro rata, on an
  equal priority, pari passu basis, unless different treatment of the shares of each such class is approved by the affirmative
  vote of the holders of a majority of the outstanding shares of Class A Common Stock and a majority of the outstanding shares
  of Class B Common Stock, each voting separately as a class"* (Art. IV.D.2(a)); stock dividends only in like kind and at the
  same rate (2(b)); *"the outstanding shares of all Common Stock will be subdivided or combined in the same proportion and
  manner"* (2(c)); on a Liquidation Event, assets and acquisition consideration *"shall be distributed on an equal priority, pro
  rata basis to the holders of Class A Common Stock and Class B Common Stock"* (3). Votes differ: *"one vote"* per A,
  *"thirty-five votes"* per B (4). Class B converts into *"one fully paid and nonassessable share of Class A Common Stock"* at
  the holder's option, on transfer, and on the founder's death. The 10-K's own note: *"The rights of the holders of our Class A
  and Class B common stock, including liquidation and dividend rights, are identical except with regard to voting and conversion
  rights."* **Economically identical, so the cash-flow claim is the sum; the votes (Dines holds all Class B, *"approximately 84%
  voting power"* at 2026-01-31) belong at Q3 (control), not in the count.**
- **Dilution not in the count:** 20,956 thousand unvested RSUs, 6,560 thousand options at a weighted $0.51, and 1.2 million
  PSUs expected to vest at 2026-07-31 (10-Q Note 12), plus **5.3 million PSUs granted to senior management on 2026-09-03** (10-Q Note 16, *"Subsequent Events"*; the 8-K names
  3,075,000 of them for four officers; share-price hurdles to 2029 and 2031) and 130,368 RSUs to the new CFO: about **34.1M, 6.6%
  of the cover count.** No
  convertible debt. Shown beside the cap, not in it.

### The market cap
**$13.39 x 521,155,409 = US$6.978bn.** Split factor 1.0. **With unvested RSUs, options and PSUs: about $7.44bn.** Public float on
the FY2026 10-K cover: $4.8bn at 2025-07-31 (companyfacts, the one dei element). Cash, cash equivalents and marketable securities
$1.405bn at 2026-07-31 (EX-99.1 of 2026-09-03), no debt: carried at Q4 and Q5, not netted here.

### THE DEAL CHECK: none live on the registrant as target
`sources.deal_filings("0001734722")` returned `([], [], '2026-03-25')` and `deal_note` returned empty (`step0_out.txt`). The
submissions index since the IPO carries **no 425, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D** on this registrant. **The quote is
not a spread and buys this company.**

### The perimeter: what (c), the five-year mean and the cap must see
- **Small, cash-paid tuck-ins only.** Peak AI Limited (UK), closed 2025-03-07: intangibles $16.2M, goodwill $27.3M (10-Q Note 6);
  cash *"Payments related to business acquisitions, net of cash acquired | ( 24,821 )"* in FY2026. **WorkFusion, Inc.**, closed
  2026-02-05: goodwill $58.2M; cash **$149.4M** in H1 FY2027 plus $29.6M of contingent and deferred consideration. **No
  acquisition moves revenue by more than a few percent in any year**, so no splice is needed; cash acquisitions are carried in
  their own column at Q4 (the DASH practice).
- **One minority investment**: convertible bonds of a private company, *"the H Company, purchased during fiscal year 2025"*, Level
  3. Immaterial to (c).

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K** (year ended 2026-01-31), filed **2026-03-25**, accession **`0001734722-26-000012`** (`10K_FY2026.txt`),
  and the **Q2 FY2027 Form 10-Q** (quarter ended 2026-07-31), filed **2026-09-08**, accession **`0001734722-26-000050`**
  (`10Q_2026Q2.txt`).
- Also read: the FY2022-FY2025 10-Ks (`0001734722-22-000006`, `-23-000017`, `-24-000011`, `-25-000007`); the Q1 FY2027 and Q2
  FY2026 10-Qs (`0001734722-26-000041`, `-25-000043`); the DEF 14A of 2026-05-12 (`0001734722-26-000027`); the 8-Ks of 2022-04-20
  (4.01), 2022-06-27, 2022-11-14, 2024-07-09 and 2025-03-12 (2.05 restructurings), 2023-03-10, 2026-03-25, 2026-06-29 and
  2026-09-03; the charter; **every 8-K EX-99.1 earnings release from 2022-03-30 to 2026-09-03** (19); eight Form 4s.
- **Figures cross-checked against the filed statement** (FY2026 10-K consolidated statement of cash flows, $ thousands,
  FY2026/25/24): *"Net cash provided by operating activities | 371,208 | 320,565 | 299,082"*, *"Stock-based compensation expense
  | 290,676 | 358,151 | 371,955"*, *"Depreciation and amortization | 16,969 | 17,232 | 22,597"*, *"Purchases of property and
  equipment | ( 19,048 ) | ( 14,923 ) | ( 7,342 )"* match companyfacts (`ocf`, `sbc_annual`, `da_annual`, `annual(CAPX_TAGS)`) to
  the thousand. Revenue *"Total revenue | 1,610,572 | 1,429,664 | 1,308,072"* matches.

