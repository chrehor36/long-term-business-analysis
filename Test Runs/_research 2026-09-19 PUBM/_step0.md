## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (from about 01:00 local); the template was copied and committed before any fetch
(`6bcdaa9`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the fourth name in
the "no share count from dei: read the cover" row (META, DASH and PATH were the first three). Research, scripts and downloaded
filings are in `Test Runs/_research 2026-09-19 PUBM/`. **No PUBM row exists in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**
(the triage skip reason says why). Every figure below is from PubMatic's own filings, fetched by this run, with the accession.

### The entity, in every year used
CIK 0001422930, `submissions.json` (fetched by this run, `subs.py`): *"PubMatic, Inc."*, SIC 7370 *"Services-Computer
Programming, Data Processing, Etc."*, `stateOfIncorporation` **"DE"**, `fiscalYearEnd` **1231**, one former name (*"Komli Inc"*,
an entry dated 2008-01-02), ticker PUBM on Nasdaq. **The charter has not moved (the DASH check):** the 8-K of 2026-04-22
(`0001422930-26-000016`) and the 8-K of 2024-06-05 (`0001422930-24-000030`) give *"Delaware"* on their covers; the FY2025 10-K says
*"We were incorporated in the State of Delaware in 2006"*; the only charter events since the IPO are the Restated Certificate
filed *"THE ELEVENTH DAY OF DECEMBER, A.D. 2020"* and a Certificate of Amendment filed 2024-06-03 adding officer exculpation under
DGCL 102(b)(7) (8-K Item 5.03 of 2024-06-05). IPO December 2020 (S-1 effective 2020-12-08, 424B4 2020-12-09). One reporting entity
throughout. Fiscal years are calendar years.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The probe (`_probe_screen.py`,
copied from PATH's with the CIK and ticker changed; output `_probe_screen_output.txt`) shows companyfacts carries **one** dei
element for PubMatic, `EntityPublicFloat` (five facts, FY2021-25 10-Ks), and **no `EntityCommonStockSharesOutstanding` at all**;
`share_count_shift` returned **None** under both the current screen and `a8bc84f` (not measured, not stable: the RIVN reading),
and `shares_outstanding` returned None. **The META/DASH/PATH hypothesis (a dimensioned per-class cover) was tested on the inline
XBRL** of the two latest periodic filings (`dei.py`, output `dei_out.txt`; raw `10Q_2026Q2_raw.htm`, `10K_FY2025_raw.htm`), and
**it holds, in META's and PATH's form: two classes, both non-zero.** In the Q2 2026 10-Q (`0001422930-26-000030`):

- *"name="dei:EntityCommonStockSharesOutstanding" ... 37,303,647"* in context c-2, segment
  *"dimension="us-gaap:StatementClassOfStockAxis">us-gaap:CommonClassAMember"*, instant 2026-07-30;
- the same element in context c-3, *"us-gaap:CommonClassBMember"*, **8,246,414**.

No `ixt:fixed-zero` class (PubMatic has two classes). The FY2025 10-K (`0001422930-26-000010`) tags the same two dimensioned facts
at 2026-02-19 (39,142,185 A; 8,263,239 B). **companyfacts publishes only undimensioned facts, so a cover tagged per class never
reaches it. For PUBM the label was the META kind: a tagging convention for a two-class cover, not a missing or stale count.**

**The other `a8bc84f` guards, on facts filed by 2026-09-01:** `scale_shift` **1.525** (did not fire); `restatement_shift`
**(1.0, FY2020)**, a null and not a guard (the SNOW note). **Unlike PATH, and like DASH, the count WAS the only thing that stopped
the name: `a8bc84f`'s `owner_earnings()` returns POSITIVE figures at every end** (`{'5y_da': 32.0M, '5y_capex': 32.4M, '3y_da':
19.5M, '3y_capex': 29.4M}`). **But that positive screen is itself flattered, and this is the one new thing the reproduction
found:** `a8bc84f`'s capex end reads `annual(CAPX_TAGS)`, which for PubMatic is purchases of property only; it omits
*"Capitalized software development costs"*, a separate face line of $17.7-20.9M a year (FY2023-25). The current screen reads
`capital_acquired()`, which adds it, and returns a five-year capex end of **$16.2M, half of `a8bc84f`'s $32.4M**
(`{'5y_da': 32.0M, '5y_capex': 16.2M, '3y_da': 19.5M, '3y_capex': 9.7M}`). The screen's D&A end is also not the face's:
`da_annual` returns $19.0M for FY2025 against *"Depreciation and amortization | 43,769"* on the FY2025 cash-flow face (it reads a
depreciation-only element; the TOST/SPGI "what is the D&A made of" question, taken up at Q4). **Not a verdict**: Q4 rebuilds owner
earnings from the filed statements. Also printed by the current screen and carried to Q4 as a prompt: `working_capital_flag` on
FY2023, *"AccountsPayable moved 98% of 2023 OCF"*.

**Restatement check:** one 10-Q/A (`0001422930-24-000037`, 2024-08-08) on the Q1 2024 10-Q, filed *"to revise Part II 'Item 5.
Other Information' by adding Rule 10b5-1 trading arrangements entered into by each of Rajeev K. Goel, our Chief Executive
Officer, and Mukul Kumar, our President, Engineering ... which were inadvertently omitted"*; *"No changes have been made to the
financial statements"*. **No restatement of figures.** The disclosure omission is carried to Q3. No 10-K/A. **Auditor:** Deloitte
& Touche LLP (ratified 2024-05-31, 8-K `0001422930-24-000030`); no Item 4.01 in the index. **SEC comment letters** (CORRESP of
2023-09-26, 2023-10-11 and 2023-11-03, read): on the FY2022 10-K's non-GAAP measures; carried to Q3.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run
  at 01:05 local on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** one second earlier (`step0_out.txt`): the stale-cache defect
  again (PATH recorded the ninth occurrence; this is the tenth recorded). The issuing-authority figure is used. FRED not used.
  Struck by this run, not inherited from the brief or from PATH.
- **Earnings currency: USD, with a large foreign share** (H1 2026: United States 53%, EMEA 33%, APAC 12%, rest 2%, by publisher
  billing address, 10-Q Note 12). No ADR or FX conversion of the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$17.55, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("PUBM", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 17.55,
  `regularMarketTime` 1789761601 = **16:00:01 EDT**, the closing print, exchange NGM; the day's bar $17.09-$17.665.
  `tools/sources.price()` returned the same 17.55 stamped 2026-09-18.
- **The month and the year, recorded rather than choosing a day:** 08-19 $16.78 · 09-02 $17.38 · 09-10 $16.23 · 09-16 $16.85 ·
  09-17 $17.33 (intraday high $19.19 on double volume; no 8-K was filed that day or since 2026-08-12) · **09-18 $17.55**. Over two
  years (`price1y_out.txt`): $14-16 through January 2025, **$6.28 at the low of 2026-02-05**, then up about 2.8 times to $17.78 on
  2026-08-07. The quote sits near its two-year high.
- **Primary-filing cross-check (Form 4s, `f4.py`, `form4_table.txt`):** Mukul Kumar sold 8,000 shares on 2026-09-16 at a
  weighted $16.7785, *"The lowest price at which shares were sold was $16.68 and the highest price at which shares were sold was
  $16.88"* (`0001833462-26-000016`), inside Yahoo's 09-16 range ($16.67-$16.92); Amar K. Goel sold 6,250 on 2026-09-03 at a
  weighted $17.0443, *"$16.795 and the highest price ... $17.73"* (`0001833508-26-000012`), inside Yahoo's 09-03 range
  ($16.78-$17.88). **The aggregator's series is corroborated on two dates. No Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-07-30): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the class treatment from the charter
- **Class A 37,303,647 + Class B 8,246,414 = 45,550,061 shares**, from the cover of the **Form 10-Q for the quarter ended
  2026-06-30, filed 2026-08-06, accession `0001422930-26-000030`**, the latest periodic filing (the submissions index carries no
  later 10-Q or 10-K; the next is due in November): *"As of July 30, 2026, the registrant had 37,303,647 shares of Class A common
  stock outstanding and 8,246,414 shares of Class B common stock outstanding."* The brief's pre-check (`cover_shares.py`) gave the
  same two figures and accession; re-verified here from the raw inline XBRL, not inherited.
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's face: *"52,673 shares issued and 37,148 shares
  outstanding as of June 30, 2026"* (Class A, thousands) and *"11,400 shares issued and 8,259 shares outstanding as of June 30,
  2026"* (Class B); the equity statement's *"Balance as of June 30, 2026 | 45,407"*. The cover moves +156K A and -13K B in 30
  days. **Consistent.** (Class B issued exceeds Class B outstanding by 3,141K: the treasury stock line, 18,666K shares in all,
  carries repurchased shares of both classes.)
- **After the cover date:** Form 4s show Class B converted to Class A on sale (code C) by Rajeev K. Goel (211,302 on 2026-08-07;
  34,371 on 2026-08-20), Mukul Kumar (8,000 on 2026-08-17 and 2026-09-16) and Amar K. Goel (6,250 on 2026-09-03). One for one, so
  **the sum is unchanged** by conversion; buybacks since 2026-07-30 are unknown until the Q3 10-Q.
- **Why the classes are added, one for one.** The governing charter is the **Restated Certificate of Incorporation filed
  2020-12-11**, read in text as Exhibit 3.1 to the FY2020 10-K (`0001422930-21-000009`, `amendedandrestatedcertif.htm`, saved as
  `CHARTER_2020.txt`; the text carries OCR artifacts, e.g. *"affrrmative"*, *"Section S(a)"*, *"1PO Date"*, flagged and not
  smoothed). The later certified copy (FY2024 10-K Exhibit 3.1, `pubmaticrestatedcoi2024.htm`) is a scanned image whose text layer
  holds only the Delaware certification page; its amendment of 2024-06-03 is officer exculpation only (8-K Item 5.03). Art. IV:
  *"3.1. Equal Status. Except as otherwise provided in this Restated Certificate of Incorporation or required by applicable law,
  shares of Class A Common Stock and Class B Common Stock shall have the same rights and powers, rank equally (including as to
  dividends and distributions, and upon any liquidation, dissolution or winding up of the Corporation), share ratably and be
  identical in all respects and as to all matters."* Dividends (3.3): *"treated equally, identically and ratably, on a per share
  basis"*, unless a disparate distribution is approved by a majority of each class voting separately; liquidation (3.5):
  *"entitled to receive ratably all assets of the Corporation available for distribution"*; merger (3.6): *"made ratably on a per
  share basis among the holders of the Class A Common Stock and Class B Common Stock as a single class"*. Votes differ: *"one (1)
  vote per share of Class A"* and *"ten (10) votes per share of Class B"* (3.2). Class B converts *"into one (1) fully paid and
  nonassessable share of Class A Common Stock"* at the holder's option (not for directors and officers), on transfer, and
  automatically *"ten (10) years from the Initial Public Offering Closing"*, which the Description of Securities (FY2020 10-K
  Exhibit 4.3) dates *"December 11, 2030"*. The 10-Q's own note: *"Basic and diluted earnings per share ... for Class A and Class
  B common stock were the same because they were entitled to the same liquidation and dividend rights."* **Economically
  identical, so the cash-flow claim is the sum; the votes belong at Q3 (control), not in the count.**
- **Dilution not in the count** (10-Q Note 9, 2026-06-30): **7,344 thousand options** at a weighted exercise price of **$12.58**
  (5,838 thousand vested) and **5,624 thousand unvested RSUs**, together 12.97M, **28.5% of the cover count**; by the treasury
  method at $17.55 the options add about 2.08M, so about **7.7M (16.9%)**. No convertible debt; no preferred outstanding. Shown
  beside the cap, not in it.

### The market cap
**$17.55 x 45,550,061 = US$799.4M.** Split factor 1.0. **With the RSUs and the options by the treasury method: about $935M**
(about $1.03bn counting every option share). Public float on the FY2025 10-K cover: $458.3M at 2025-06-30 (companyfacts, the one dei
element). Cash and cash equivalents $120.0M plus marketable securities $17.5M = **$137.5M at 2026-06-30, no debt** (10-Q balance
sheet; *"Ended the quarter with total cash, cash equivalents, and marketable securities of $137.5 million with no debt"*, EX-99.1
of 2026-08-06): carried at Q4 and Q5, not netted here. **Note what that cash is:** accounts receivable $383.2M sit against accounts
payable $390.0M (money owed to publishers), so the cash is not surplus in the ordinary sense (Q4).

### THE DEAL CHECK: none live on the registrant as target
`sources.deal_filings("0001422930")` returned `([], [], '2026-02-26')` and `deal_note` returned empty (`step0_out.txt`). The
submissions index since the IPO carries **no 425, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D** on this registrant (grepped,
`filings_list.txt`). The 8-K of 2025-09-08 (Items 7.01, 8.01) announced PubMatic's own lawsuit against Google, not a deal. **The
quote is not a spread and buys this company.**

### The perimeter: what (c), the five-year mean and the cap must see
- **One acquisition since the IPO:** ConsultMates, Inc. (dba "Martin"), closed 2022-09-16, *"Total cash consideration payable by
  the Company pursuant to the terms of the merger agreement was $45.0 million, inclusive of"* $14.2M of vesting payments to two
  key employees (CORRESP of 2023-10-11); `acquisition_flag` reads $28.1M of cash paid (FY2022). Goodwill $29.6M and intangibles
  $1.9M at 2026-06-30. **It moves no revenue line by more than a few percent**, so no splice is needed; the cash is carried in its
  own column at Q4 (the DASH practice).
- **Small equity investments:** $3.5M purchased in H1 2026 (10-Q cash-flow face), non-marketable, at cost.
- **The Google lawsuit** (filed 2025-09-08, PubMatic as plaintiff) is not a perimeter event; read at Q2 and Q3.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K** (year ended 2025-12-31), filed **2026-02-26**, accession **`0001422930-26-000010`** (`10K_FY2025.txt`),
  and the **Q2 2026 Form 10-Q** (quarter ended 2026-06-30), filed **2026-08-06**, accession **`0001422930-26-000030`**
  (`10Q_2026Q2.txt`).
- Also read: the FY2020-FY2024 10-Ks (`0001422930-21-000009`, `-22-000009`, `-23-000008`, `-24-000012`, `-25-000012`); the Q1
  2026 and Q2 2025 10-Qs (`0001422930-26-000024`, `-25-000040`); the Q1 2024 10-Q and its 10-Q/A; the DEF 14A of 2026-04-15
  (`0001140361-26-014825`); the 8-Ks of 2022-01-03, 2022-06-08, 2022-09-14 (1.01, Martin), 2022-10-17 (1.01, credit facility),
  2023-02-28 (5.03 bylaws), 2023-04-04, 2023-06-09, 2023-08-30, 2023-12-12 (5.02), 2024-06-05 (5.03), 2025-09-08 (Google suit),
  2026-04-22 (preliminary results), 2026-08-06 and 2026-08-12; the charter, the 2023 bylaws and the Description of Securities;
  **every 8-K EX-99.1 earnings release from 2021-05-13 to 2026-08-06** (22, plus the 2026-04-22 preliminary release and the CFO
  retirement release); the three 2023 CORRESP letters; five Form 4s and a two-year price series.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statement of cash flows, $ thousands,
  FY2025/24/23): *"Net cash provided by operating activities | 81,059 | 73,425 | 81,121"*, *"Stock-based compensation | 38,378 |
  37,676 | 28,862"*, *"Purchases of and deposits on property and equipment | ( 14,345 ) | ( 17,592 ) | ( 10,601 )"* and
  *"Capitalized software development costs | ( 20,511 ) | ( 20,936 ) | ( 17,687 )"* match companyfacts (`ocf`, `sbc_annual`,
  `annual(CAPX_TAGS)`, `capital_acquired` = the two capital lines summed) to the thousand. Revenue *"Revenue | $ | 282,926 | $ |
  291,256 | $ | 267,014"* matches. **D&A does not match the screen**: the face's *"Depreciation and amortization | 43,769 | 45,352
  | 44,770"* against `da_annual` $19.0M, $24.8M, $28.5M (above).
