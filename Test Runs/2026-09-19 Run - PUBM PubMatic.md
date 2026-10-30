# Company Run — PubMatic, Inc. (PUBM) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
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

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in
> character. If a business is complex or subject to constant change, we're not smart enough to predict future cash
> flows."* **[E3-31]**

### What the filings show, in my own words, without management's language
A website or app owner (the "publisher") has empty ad slots each time a person loads a page or a video. In the fraction of a
second before the page appears, PubMatic's servers offer that slot to many buying programs at once (the "DSPs" that advertisers
and agencies use, The Trade Desk and Google's DV360 being the largest), take the highest bid, and hand the slot to the winner.
**It keeps a cut of the price.** The 10-K: *"We generate revenue through fees charged to our publishers, which are generally a
percentage of the value of the advertising impressions that publishers monetize on our platform"*, reported *"on a net basis.
This represents gross billings to buyers, net of amounts we pay publishers and rebates associated with SPO agreements with
buyers"* (FY2025 10-K MD&A). It bills the buyer for the whole price and pays the publisher the rest, typically on terms of
*"ninety days or less"*, which is why *"both accounts receivable and accounts payable appear large in relation to revenue"*
($383.2M and $390.0M at 2026-06-30 against $282.9M of FY2025 revenue). Smaller lines sell tools and data on the same auctions
(OpenWrap header bidding, Connect, Activate direct deals, Convert for retail media). **No filing discloses the percentage taken or
the gross spend it is taken on** (grepped: "take rate" appears only in risk factors; no "gross billings" or "ad spend" total is
filed), so the price of the service is visible only as revenue divided by volume.

The costs are servers and people. PubMatic *"own[s] and operate[s] our software and hardware infrastructure globally, which saves
significant infrastructure expenditures as compared to public cloud alternatives"* (10-K Item 1), in third-party co-location
centres ($75.5M of *"contractual obligations to third-party data center providers"* at 2025-12-31); cost of revenue is
*"data center co-location costs, depreciation expense related to hardware ... amortization expense related to capitalized
internal-use software development costs, personnel costs"*. **So each dollar of revenue is: the auctions cleared x the average
price x the cut, less the servers to run every auction offered (won or not) and the salesforce to hold the publishers and
buyers.** The filed series (10-Ks, 10-Q, EX-99.1s; impressions from each 10-K's quarterly list, summed; `unit_series.txt`):

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Revenue ($M) | 226.9 | 256.4 | 267.0 | 291.3 | 282.9 | 78.6 (qtr) |
| Impressions processed (trillions) | 92.2 | 159.1 | 210.7 | 263.1 | 336.8 | about 92 (qtr) |
| Revenue per million impressions | $2.46 | $1.61 | $1.27 | $1.11 | $0.84 | $0.85 |
| Cost of revenue per million impressions | $0.63 | $0.51 | $0.47 | $0.38 | $0.31 | n/a |
| Gross margin | 74.3% | 68.2% | 62.8% | 65.3% | 63.6% | 67.1% |
| Net dollar-based retention (publishers) | 149% | 108% | 101% | 107% | 96% | 98% (TTM, 10-Q) |
| Publishers served (approx.) | 1,450 | 1,650 | 1,800 | 1,900 | 1,980 | n/a |
| SPO share of activity | n/a | n/a | ~45% | ~50% | ~55% | >55% |
| GAAP operating income ($M) | 58.8 | 40.5 | 2.0 | 3.9 | (17.3) | 0.6 (qtr) |

**Cross-check of my construction:** the cost-per-impression column, computed from filed revenue, filed gross profit and filed
impressions, falls **-19.0%, -8.0%, -18.5%, -20.3%** (FY2022-25); the 10-Ks state *"cost of revenue per impression processed
decreased by 19% in 2022"*, *"declined by 8%"* (2023), *"decreased by 18%"* (2024) and *"decreased by 20%"* (2025). **The
construction reproduces the company's own figures.** FY2025 revenue by publisher billing address: United States 56% ($158.1M), EMEA 32%, APAC 10% (10-K
geography note); H1 2026: US 53%, EMEA 33%, APAC 12% (10-Q Note 12). *"no publisher represented more than 10% of the Company's revenue"*
(FY2023-25); on the buying side, *"A limited number of large demand side platforms ('DSPs') – The Trade Desk and Google DV360 in
particular – account for a significant portion of the ad impressions purchased on our platform"* (10-K Item 1A), with three
buyers at 24%, 16% and 14% of receivables at 2025-12-31 (10-K concentration note).

**The scarce input the business controls:** its integrations: code placed in about 1,980 publishers' pages and apps (header
bidding wrappers, the SDK) and live connections to the DSPs, plus a server fleet it built and runs itself at a cost per auction
falling about a fifth a year. **What it does not control, on its own filing:** the price (*"We experience requests from
publishers and buyers for discounts, fee concessions, rebates, refunds"*; *"we have experienced fee pressure"*, read at Q2), and the
buyers' algorithms (*"our business results, including revenues, may be impacted by changes in their pricing strategies, bidding
algorithms, or go-to-market efforts"*; two DSP changes have already cut revenue, read at Q2).

**Will the fundamentals look broadly the same in ten years?** The mechanism (a cut of each auction cleared for a publisher) has
held in every filing since the IPO. Against that, in the company's own words: *"The digital advertising ecosystem continues to
evolve and adapt at a rapid pace"* (10-K Item 1); *"Agentic AI is creating a structural shift that is redefining the entire
digital advertising market"* (CEO, EX-99.1 of 2026-04-22); and the company now also runs campaigns for buyers (*"AgenticOS"*,
*"more than 80 fully autonomous, end-to-end campaigns"*, EX-99.1 of 2026-08-06), which places it on the buying side of the same
auction.

### THE CASE FOR UNKNOWABLE, AT FULL STRENGTH **[E4-26, E4-51]**
(1) The price of the service (the cut) is never filed, so the one number a franchise claim would rest on is not visible, only its
product with ad prices and mix. (2) The filer says the market is being redefined by AI agents that may *"bypass sell-side
platforms"* (10-K Item 1A: *"Buyers may develop proprietary AI-driven media planning and execution tools that bypass sell-side
platforms"*; publishers *"may use AI to ... execute transactions without intermediaries"*). (3) Google, one of the two largest
buyers, is also the dominant competitor and the defendant in PubMatic's own antitrust suit; how that ends cannot be read from
any filing.

**Why it does not carry, and what is excluded.** The filed business is the declared one and I can state its economics from filed
series in every year FY2021 to Q2 2026: revenue, volume, cost per unit, retention, concentration. The missing cut is a gap in
disclosure, not in understanding; its product with volume (revenue per impression) is computable and, as the cross-check shows,
the filed figures reconcile. **What is outside the circle is named: the future economics of "agentic" buying products
(AgenticOS, Decision Fabric, Intelligent Yield) and whether AI buying agents route around sell-side platforms; and the outcome of
the Google litigation.** [E4-46] says study will not repair those; they are recorded as outside the circle and **cannot be counted
at any later gate**. Whether an auction house whose cut is set under pressure from its largest buyers has a position is the Q2
question, and it is carried there, not decided here.

- **VERDICT: [x] IN** on the business the filings show (a percentage fee on programmatic ad auctions run for about 1,980
  publishers, sold to a few large DSPs, on self-built infrastructure; $282.9M of FY2025 revenue on 336.8 trillion impressions).
  **Not IN** for the future economics of agentic buying products, for whether AI agents displace sell-side platforms, and for the
  Google litigation: outside the circle [E3-31, E4-46], never counted later.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have **no close
> substitute** and; (3) is not subject to price regulation."* **[E3-03]**, 1991 letter

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
The brief's prior was that this file closes at Q2 on price competition, as PATH did, and it asked to be argued against. The case
against it, from the filings: **PubMatic is profitable where PATH was not** (operating cash $73-89M in every year FY2021-25,
positive five-year owner cash, Q2 row below); **it owns its infrastructure** and has cut the cost of processing an impression by
19%, 8%, 18% and 20% in four successive years, a cost curve a cloud-rented rival cannot copy without building the same fleet
(*"We believe our platform would be difficult, time consuming, and costly to replicate"*, 10-K Item 1); it is **neutral**
(*"we do not own media"*) where Google, Amazon and The Trade Desk each own something that competes with its customers; buyers
have signed SPO agreements that route **over 55%** of its activity to it directly; volume grew **3.7 times in four years** (92.2 to
336.8 trillion impressions); publishers grew every year (1,450 to 1,980); gross margin held at 63-68% while volume nearly quadrupled; and
revenue returned to +11% in Q2 2026 with CTV, mobile app and new products at ~60% of it. **If a sell-side ad exchange can be a
franchise, a low-cost, neutral, profitable one is the candidate.**

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES.** About 1,980 publishers; 336.8 trillion impressions in FY2025; 92 trillion in Q2 2026 (+18%).
- **(3) Not subject to price regulation: YES.** No filing names a regulator of PubMatic's fee. Privacy law (GDPR, CCPA, state laws)
  constrains the data used, not the price charged; the DOJ's case against Google regulates a competitor, not PubMatic.
- **(2) No close substitute: NO, on five independent records.**
  1. **The company's own Item 1A, in the present and past tense (FY2025 10-K):** *"We experience requests from publishers and
     buyers for discounts, fee concessions, rebates, refunds, and greater levels of pricing transparency, in some cases as a
     condition to maintain the relationship or to increase the amount of advertising spend that the buyer sends to our
     platform. In addition, we may decide to offer discounts or other pricing concessions in order to attract more inventory or
     demand, or to compete effectively with other providers that have different or lower pricing structures and may be able to
     undercut our pricing due to greater scale or other factors."* And: *"In some cases, we have experienced fee pressure as we
     have built out our offerings, and we expect this fee pressure to increase as more competitors, including new entrants as
     well as publishers themselves, build their own technology and infrastructure to enter the markets in which we do
     business."* And: *"Our business suffers when publishers and buyers purchase and sell advertising inventory directly from
     one another or through other intermediaries other than us."* A supplier whose customers ask for fee concessions *"as a
     condition to maintain the relationship"* has told you it has close substitutes. The concession sentence and the fee-pressure sentence stand in
     all six 10-Ks FY2020-25, and the sentence on direct dealing in FY2023-25 (grepped in each 10-K).
  2. **Competitors' own 10-Ks name PubMatic as one of several interchangeable suppliers.** Criteo, FY2025 10-K
     (`0001576427-26-000014`): *"We currently compete with large, well-established companies, such as Amazon, Meta Platforms,
     Google, and Microsoft, pure play DSPs, such as The Trade Desk, pure play SSPs such as Magnite or PubMatic, and pure play
     retail SSPs such as Publicis' CitrusAd"*; Taboola, FY2025 10-K (`0001840502-26-000004`): *"Advertising Intermediaries. ...
     These include The Trade Desk, Magnite, PubMatic, Xandr, Plista, TripleLift, RevContent, Teads and others."* EDGAR full-text
     search finds "PubMatic" in 10-Ks of twenty other filers, some as competitor and some as partner or customer
     (`peers/fts_out.txt`; `fts_count` 119 hits, of which 56 are PubMatic's own); Magnite's FY2025 10-K does not name it. The largest buyer sources from *"over 430 directly integrated ad exchanges, publishers and supply-side
     platforms"* and has built a route around them: *"we launched our OpenPath offering in order to give clients a simplified,
     direct connection to publishers"* (The Trade Desk, FY2025 10-K, `0001671933-26-000014`).
  3. **The buyers' own algorithms move the revenue, twice on record.** *"our business was negatively impacted by bidding
     methodology changes implemented by one of our buyers in the second half of the second fiscal quarter of 2024"* (FY2024 10-K);
     *"Revenues for the year ended 2025 were also negatively impacted by platform changes implemented by one of our large DSP buyers
     in the second half of 2024 and subsequently platform changes implemented by another DSP buyer in the second half of 2025"*
     (FY2025 10-K), with the first still *"in the near term"* at the FY2025 10-K. Revenue fell 3% in FY2025 (-$8.3M, of which $14.2M
     was the 2024 election's absence) while impressions rose 28%. A supplier with no close substitute is not re-priced by a
     customer's software change.
  4. **The unit price of the service fell faster than its cost, so the cost advantage did not stay home [E3-62].** Revenue per
     million impressions processed **$2.46, $1.61, $1.27, $1.11, $0.84** (FY2021-25), **-66%**; cost of revenue per million
     **$0.63 to $0.31, -52%**; gross margin **74.3% to 63.6%**; GAAP operating income **$58.8M to -$17.3M** while revenue rose 25%.
     The company says where the savings go: *"As the sheer volume of data processed in digital advertising multiplies, these cost
     savings and efficiencies can be shared with our customers"* (10-K Item 1). This is the loom lesson in the corpus's words,
     *"how much is going to stay home and how much is just going to flow through to the customer"* **[E3-62]**. **Limit of this
     record:** impressions processed include auctions not won, and revenue per impression mixes ad prices, format mix and the cut;
     the cut itself is never filed. It is a unit series, not a price series [E4-55], and it is carried as one record among five.
  5. **The customer's own vote, measured by the company.** Net dollar-based retention of publishers **149%, 108%, 101%, 107%, 96%**
     (FY2021-25): existing publishers paid PubMatic **less** in FY2025 than in FY2024. No price increase is on record: six 10-Ks,
     two 2026 10-Qs and twenty-four releases were swept for "price increase", "increase(d) our price/fee/take rate", "raise(d)
     our price/fee" and "take rate increase" (`price_sweep.txt`): **no instance found**; every hit is the risk sentence *"we might
     not be able to fully offset such higher costs through price increases"* or *"increased price competition"*.

### [E4-04]: MUST THE MOAT BE CONTINUOUSLY REBUILT?
The test v4 sets: does the spending defend the same advantage or buy its replacement? **Part of each.** The server fleet is
defended by spending (capex and capitalised software $28-49M a year FY2021-25, read at Q4), which is the Coca-Cola case. But the
route to the buyer has been rebuilt twice in five years: header bidding (the IPO-era basis, *"OpenWrap, our header bidding
solution"*), then SPO agreements (*"We have been investing in SPO technology and partnerships for six years"*, now 55% of
activity, with *"rebates associated with SPO agreements with buyers"* netted from revenue), and now agentic buying, which the
company says is *"redefining the entire digital advertising market"* and which puts it on the buyers' side of the auction. The
cost curve is real, and Q2 record 4 shows it is passed on.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
Same metric, same five-year window (FY2021-25 for every filer except Digital Turbine, FY2022-26 to 2026-03-31), each figure from
the filer's own XBRL (`peers/row.py`, `peers/row_out.txt`; peer 10-Ks in `peers/`), cross-checked for PubMatic to the filed face at
Step 0 and for Magnite to its FY2025 10-K face (*"Revenue | $ | 713,953"*; operating cash *"$236.2 million"*; *"Stock-based
compensation expense | 76,648"*; *"Purchases of property and equipment | ( 70,535 )"* plus *"Capitalized internal use software
development costs | ( 13,768 )"*). **Owner cash** = operating cash less stock compensation less purchases of property and
capitalised software, the same construction for every filer.

| Company (10-K) | role | revenue, last FY | revenue growth, 4-step CAGR | owner cash / revenue, 5-yr | owner cash / revenue, last FY | stock pay / operating cash, last FY |
|---|---|---:|---:|---:|---:|---:|
| **PUBM** (`0001422930-26-000010`) | sell-side, net revenue | $282.9M | 5.7% | **6.1%** | **2.8%** | 47.3% |
| **MGNI** Magnite (`0001595974-26-000007`) | sell-side, 90% net revenue | $714.0M | 11.1% | **14.2%** | **10.5%** | 32.5% |
| **TTD** The Trade Desk (`0001671933-26-000014`) | buy-side, net of media | $2,896.3M | 24.7% | 4.2% | 10.1% | 49.4% |
| **CRTO** Criteo (`0001576427-26-000014`) | retail media and retargeting, gross revenue | $1,944.9M | -3.6% | 5.3% (12.0% of gross profit) | 7.7% | 18.8% |
| **TBLA** Taboola (`0001840502-26-000004`) | native ads, gross revenue | $1,912.0M | 8.5% | 0.1% | 5.2% | 30.7% |
| **APPS** Digital Turbine (`0001628280-26-038115`) | mobile app exchange, FY to 2026-03-31 | $565.3M | -6.8% | 2.1% | -0.9% | 39.1% |
| **GOOGL**, Google Network revenue only | the incumbent exchange | $29,792M | -2.5% (2023-25) | not segmented | not segmented | n/a |

**Peers taken: six SEC filers** of the field the filings name (PubMatic's 10-K names Google and The Trade Desk as its largest
buyers and Amazon's Transparent Ad Marketplace and Prebid as frameworks it interoperates with; Criteo, Taboola and Magnite's
10-Ks name the rest). Not taken: **Index Exchange, OpenX, Equativ/Sharethrough, Sovrn, TripleLift, FreeWheel (inside Comcast),
Xandr (inside Microsoft), Verve** are not on the SEC's `company_tickers.json` or are unsegmented inside a parent
(`peers/private_check.txt`); **Amazon's** publisher services are unsegmented. **Limits of the row:** Criteo and Taboola report
gross revenue (traffic acquisition cost inside cost of revenue), so their per-revenue-dollar figures understate their margin
against a net reporter (Criteo's is shown per gross-profit dollar too); `capital_acquired` returns zero for Criteo FY2021 and
Digital Turbine FY2022-23 (a tag gap, which flatters those years); Magnite carries debt, so its operating cash is after interest
and still leads. **The class is not held PROVISIONAL on the absent private peers**, because the verdict rests on criterion (2) in
the subject's own words, in two competitors' filings and in its own retention and unit series, and **the one like-for-like
public pure-play, Magnite, is ahead on every column**; no private filer could reverse that.

**What the row shows.** PubMatic is **second of two public pure-play SSPs** and behind its direct peer on growth (5.7% against
11.1% a year), on five-year owner cash per revenue dollar (**6.1% against 14.2%**) and in FY2025 (2.8% against 10.5%), with the
largest stock-pay load of the sell-side pair. **Direction [E4-32]:** PubMatic's owner-cash margin fell from 15.1% (FY2021) to
2.8% (FY2025) while Magnite's held at 10.5-16.8% and The Trade Desk's rose from -1.6% to 10.1%. **The owned-infrastructure cost
advantage does not show in the owner-cash row**: whatever it saves, the record says it is passed to customers (record 4 above).
**The row's limit [E3-61]:** it shows position, not conduct; and no filer publishes a share of sell-side spend.

### THE OTHER Q2 TESTS
- **Returns on capital, asked about the business [E3-46]:** net income over average equity **26.2%, 10.1%, 2.9%, 4.4%, -5.4%**
  (FY2021-25: $56.6M, $28.7M, $8.9M, $12.5M, $(14.5)M on average equity of $216.3M, $284.7M, $304.2M, $286.8M, $270.0M). Equity is
  mostly cash; the business's operating capital is roughly zero (receivables are matched by payables to publishers), so the return
  on tangible operating capital is not finite; that is true of any intermediary paid before it pays and says nothing about
  substitutes. The earnings on it fell from $56.6M to a loss.
- **[E2-44], both halves:** price with flat demand: **not shown**, and the unit series runs the other way. Growth with minor
  capital: volume nearly quadrupled on $28-49M a year of capital spending, so **the second half passes**; the capital this business
  consumes is stock pay and the server refresh, read at Q4.
- **[E4-37] agony pricing:** the concession sentence (*"in some cases as a condition to maintain the relationship"*) is the
  prayer session in writing.
- **[E3-33] untapped pricing power / [E5-28]:** claiming it would be claiming near-monopoly; Criteo's *"pure play SSPs such as
  Magnite or PubMatic"* and The Trade Desk's 430 supply sources refute it.
- **[E2-53] the dominance class:** position would have to set the economics regardless of execution. The record runs the other
  way: one DSP's bidding change in 2024 and another's in 2025 each moved the revenue.
- **[E2-45] the attacker's test:** the filer answers it: *"Some existing and potential buyers have their own relationships with
  publishers or are seeking to establish such relationships, and many publishers are investing in capabilities that enable them to
  connect more effectively directly with buyers."* The Trade Desk, PubMatic's largest buyer, is the attacker with OpenPath; the
  attacker does not need to build a better exchange, only a direct pipe for its own spend.
- **[E4-36] which cause of success:** wave-riding. Header bidding carried the FY2020-21 run (net retention 149% in FY2021); the
  retention series (108%, 101%, 107%, 96%) is the wave passing.
- **[E4-23] key person:** the 10-K says the co-founder CEO *"is critical to our overall management"*; the filings do not show the
  economics depend on him. Not recorded as a moat defect.
- **[E2-59]:** does not arise; no regulator sets the price.

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** · not price-regulated **[x]**
- Class: **[ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL** as a franchise; a real cost curve and real integrations, in a market the
  filer and two competitors describe as served by interchangeable intermediaries whose largest buyers route around them.
  Direction: **narrowing** on the company's own retention, unit-price and margin series [E4-32].
- **VERDICT: [x] OUT, ON THE BUSINESS. Permanent.** Criterion (2) of **[E3-03]** fails on five independent records: the company's
  own Item 1A (fee concessions *"in some cases as a condition to maintain the relationship"*; *"we have experienced fee
  pressure"*; the business *"suffers when publishers and buyers purchase and sell advertising inventory directly"*); two
  competitors' 10-Ks that list PubMatic among interchangeable intermediaries (Criteo: *"pure play SSPs such as Magnite or
  PubMatic"*; Taboola) and the largest buyer's direct route around SSPs (The Trade Desk's OpenPath); revenue moved twice by DSPs'
  bidding changes (2024, 2025); revenue per impression down 66% in four years against cost per impression down 52%, the savings
  *"shared with our customers"* **[E3-62]**; and publisher net retention of 96% in FY2025 with no price increase on record. The
  competitor row puts PubMatic behind Magnite on every column. **The brief's prior (Q2 on price competition) is confirmed, and it was
  argued against first**: the owned-infrastructure cost advantage the brief asked me to test is real, and the record shows it
  flowing to customers rather than to owners. **The file closes here.** Q3 to Q6 are recorded below, **not governing**, as PATH did.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(RECORDED, NOT GOVERNING: the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution** **[E3-38, E3-43]**: Q2 found a business, not a franchise, in a market the filer calls *"intensely
  competitive"* and moving *"at a rapid pace"*; the revenue has moved twice on a buyer's software change. *"a business, unlike a
  franchise, can be killed by poor management"* [E3-43].
- [ ] **Control** **[E1-16]**: not the buyer's case (a minority purchase). **Recorded instead as the minority holder's
  position:** the two co-founders, Rajeev K. Goel (CEO) and Amar K. Goel (Chairman), *"are brothers"*; they hold **29.3%** and
  **36.4%** of the total voting power, and directors and officers as a group **67.8%** (DEF 14A 2026, ownership table, as of
  2026-04-01, Class B at ten votes). Written consent stays available to stockholders until Class B falls below a majority of the
  vote (charter; Description of Securities), and Class B converts automatically on 2030-12-11. An outside holder cannot change
  management before then; the remedy is to sell [E4-24].
- [ ] **Leverage** **[E3-29]**: no debt; an undrawn $110.0M revolver (matures 2027-10-17).
- **Case declared: GATE (daily execution).** No price would compensate a failure here.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
- **2023, the SEC comment letters on non-GAAP measures** (staff letters of 2023-09-19 and 2023-10-23; company responses dated
  2023-09-26, 2023-10-11 and 2023-11-03, public on release of the correspondence). The staff asked why cash retention payments to
  two key employees of the Martin acquisition ($14.2M over three years) were excluded from Adjusted EBITDA; the company defended
  the exclusion, and the staff replied: *"Considering such arrangements require continued employment and the amounts will be paid
  in cash, it remains unclear how such charges are not a normal, recurring cash operating expenses. Accordingly, please remove
  these adjustments from your non-GAAP measures."* The CFO: *"The Company acknowledges the Staff's comment and confirms that it
  will remove this adjustment from its non-GAAP financial measures in future filings."* The staff also required GAAP margin
  *"with equal or greater prominence"* beside the Adjusted EBITDA margin. The FY2022 Adjusted EBITDA the company had reported as
  *"$98.0 million, or 38% margin"* (EX-99.1 of 2023-02-28) reappears as *"$97.0 million, or 38% margin, in 2022"* (EX-99.1 of
  2024-02-26). **A regulator's correction of an adjustment, accepted; not a misconduct finding.** It is the [E4-29] flag, below.
- **2024-08-08, the 10-Q/A** (`0001422930-24-000037`): the Q1 2024 10-Q had omitted the Rule 10b5-1 trading plans adopted by
  the CEO and the President, Engineering; the company amended it three months later. **A disclosure lapse, self-corrected; no
  figure changed.**
- **2023, a DSP buyer's bankruptcy** (*"filed for Chapter 11 bankruptcy on June 30, 2023"*): $14.5M of uncollectible receivables,
  $8.8M of it charged back to publishers; disclosed and quantified in the 10-K. A business loss, not conduct.
- **Litigation:** the 10-Q says *"we are not presently a party to any legal proceedings that ... would individually or taken
  together have a material adverse effect"*; the one live suit is PubMatic's own against Google (filed 2025-09-08).
- **Related parties:** *"From January 1, 2025 to the present, there have been no transactions other than the ones described
  below"*, and the exceptions are director and executive pay (DEF 14A 2026).
- **Binary: no disqualifier found.** Written as [E5-17] requires: the absence of found disqualifiers, not a finding that the
  managers are honest.

### THE INCENTIVE READ **[E4-27]**
- **The cash bonus pays on revenue and on a profit line that excludes the stock pay:** *"our NEOs were eligible for target bonuses
  ranging from 65% to 108% of base salary that could be earned based entirely on achievement against semi-annual revenue and
  adjusted pre-tax net income goals"*, and *"Adjusted pre-tax net income is defined as income before income taxes and excluding
  stock-based compensations costs"*, with *"greater weighting on revenue due to the importance of continued growth and the
  perceived importance of revenue to some of our investors"* (DEF 14A 2026). Paid on volume and on a profit that leaves out the
  cost that took 47% of FY2025 operating cash (Q4).
- **The equity vests on service, not results:** *"equity awards that vest over four years"*, *"generally subject to vesting based
  on each named executive officer's continued service"*.
- **Grant count rises when the price falls:** 3,448K RSUs granted in H1 2026 at a weighted *"6.64"* against 2,047K in all of
  FY2025 at *"14.39"* (10-Q Note 9; FY2025 10-K), near the two-year low of $6.28 (2026-02-05); the stock is now $17.55.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [ ] weak accounting: none found in the statements; Deloitte; no restatement of figures. (The non-GAAP correction is under
  [E4-29].)
- [ ] unintelligible footnotes: none found; the net-revenue, receivable/payable and software-capitalisation notes are plain.
- [x] **trumpeted projections [E4-22, E5-30], against outturn [E3-48]** (initial full-year guide in the Q4 release, then the
  10-K): **FY2022** revenue *"$282 million to $286 million"* and Adjusted EBITDA *"$101 million to $106 million"*, cut on
  2022-08-08 to $277-281M and on 2022-11-08 to $257-260M; **actual $256.4M, below even the second cut**, Adjusted EBITDA $98.0M
  as first reported. **FY2023** *"Adjusted EBITDA margin to be 30%+"*; **actual 28%**. **FY2024** *"Year-over-year revenue growth
  of over 10%"* and *"Adjusted EBITDA margin to be approximately 30%"*; **actual +9.1% (missed) and 32% (met)**. **FY2025 and
  FY2026: no full-year guide** (the releases of 2025-02-27 and 2026-02-26 guide the quarter only). Quarterly guides in 2026 were
  beaten (Q1 $58-60M guided, $62.6M actual, pre-announced on 2026-04-22 in the same release that announced two senior revenue
  officers' departures; Q2 $68-70M guided, $78.6M actual). **Three full-year guides, three misses on the headline line, then
  full-year guidance stopped.**
- [x] **serial share issuance [E5-15], gross not net:** the 2020 Plan reserve *"will increase automatically on January 1 for each
  of the first ten calendar years ... by the number of shares equal to the lesser of five percent (5%) of the aggregate number of
  outstanding shares"*, plus 1% a year for the ESPP; option and RSU shares issued 1,453K (FY2023), 1,963K (FY2024), 2,634K
  (FY2025) and about 1,639K in H1 2026 with the ESPP. **The net count fell from 52.7M (2022-12-31) to 45.6M at the cover (-13.6%)
  only because $211.4M of cash bought 15.5M shares** (*"Through June 30, 2026, used $211.4 million in cash to repurchase 15.5
  million shares of Class A common stock"*, EX-99.1 of 2026-08-06). The owner's cost of the stock pay is the cash that retired it.
- [x] **adjusted-earnings promotion [E4-29], at full strength:** Adjusted EBITDA (*"net income (loss) adjusted for stock-based
  compensation expense, depreciation and amortization, litigation related expenses, interest income, and provision for (benefit
  from) income taxes"*) is the only guided profit line in every release since 2021, the company's stated reason for not guiding
  GAAP being *"stock-based compensation expenses, are not predictable"*; the CFO retirement release says the company was *"profitable on an
  adjusted EBITDA basis for 41 consecutive quarters"* in a year of GAAP net losses (FY2025 $(14.5)M; H1 2026 $(13.7)M); D&A,
  the expense it deletes, was $43.8M in FY2025, more than cash capital spending ($34.9M). The SEC staff made the company remove one
  adjustment in 2023 (above). **The except-for flag [E2-57, E5-33]:** from FY2025 Adjusted EBITDA also excludes *"litigation
  related expenses"* ($0.9M in FY2025), which are the legal fees of PubMatic's own suit against Google, *"a discrete matter"*,
  while the 10-K says G&A will rise in 2026 *"primarily due to increases in litigation related expenses"*.
- [x] **[E2-49] metric withdrawal: FIRED, in the releases.** Net dollar-based retention was a headline bullet in every earnings
  release from 2021-05-13 to 2026-02-26 (twenty releases, grepped), the last reading *"Net dollar-based retention 1 was 96% for the
  year ended December 31, 2025"*; it is **absent from both 2026 quarterly releases** (2026-05-07 and 2026-08-06), whose headline
  bullets became *"AI customer adoption more than doubled sequentially"*, *"80+ agentic campaigns and 4,000+ AI-powered deals"*.
  **The mitigation, stated:** the 10-Qs still carry it (*"96% for the trailing twelve months ended March 31, 2026"*; *"98% for the
  trailing twelve months ended June 30, 2026"*), so the yardstick was moved out of the headline, not destroyed. A switch that
  follows deterioration fires; it was not announced ahead with reasons. The prior's tally: fired at SHOP, MRVL, PAY, ARM, CALX, BE
  and now PUBM; failed at QLYS, CRM, CORT, PLTR, INOD, PATH.
- [ ] filed-figure tells [E4-30]: cash taxes paid $6.8M, $9.2M, $15.6M, $14.2M, $8.6M against pretax income of $64.8M, $37.5M,
  $10.5M, $17.8M, $(16.0)M (FY2021-25): cash taxes **rose** as a share of pretax; growth is not smooth. Not fired.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net income over average equity **26.2%, 10.1%, 2.9%, 4.4%, -5.4%** (FY2021-25; Q2). No leverage and no gimmick flatter it; the
series is a decline from a header-bidding peak to a loss. [E3-54]'s retention test: retained earnings $121.2M (2026-06-30) against
$211.4M spent on buybacks; the market value added per dollar retained cannot be read as positive from the IPO-era cap.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
The 10-K names the DSP bidding changes, quantifies the election effect, states cost per impression every year, and explains the
receivable/payable gross-up; the bad debt was quantified with the publisher chargeback. Against that: the headline profit number
excludes the stock pay and the D&A; the regulator had to remove one adjustment; retention left the release headline when it
fell below 100%; the DSPs whose changes moved revenue are not named in any 10-K, 10-Q or release read; and the price of the service (the
cut) is never disclosed. **Mixed; no finding.**

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08, E4-31, E5-24]:** condition (1) passes ($137.5M of cash and securities, no debt, revolver undrawn).
  **Condition (2): the prices paid**, from the equity statements, were about **$14.76** (FY2023, 4,040K shares for $59.6M),
  **$17.69** (FY2024, 4,278K for $75.7M), **$11.42** (FY2025, 4,088K for $46.7M) and **$9.78** (H1 2026, 3,119K for $30.5M), against
  five-year owner earnings of about -$1M to +$16M a year (Q4), which at those prices is a yield of about 0-3%. No conservatively
  calculated value this run can build puts those prices at a material discount. **CAPITAL-ALLOCATION FLAG, with the humility clause
  [E4-13]:** management knows the business better than this run does, and *"many CEOs never stop believing their stock is cheap"*
  [E5-08]. The flag binds position size, never the rate. Much of the spending is better read as the cash cost of the stock pay
  than as a discretionary purchase.
- **[E2-30] institutional imperative:** (4) peer imitation: the move from header bidding to *"AI-powered"* and *"agentic"*
  language follows the industry's move to AI products; prompt only. (2) soak up funds: one
  acquisition (Martin, $45.0M) in five years; not observed as a pattern. (1) and (3) not observed.
- **[E3-58] delegation:** no banker-led serial M&A found.

### THE GUARDRAIL
- [x] Nothing here promotes the name; a strong Q3 could not repair Q2 [E2-37, E2-38, E3-39].
- [x] No key-person moat defect recorded at Q2 (the filings do not show the economics depend on the CEO).
- [x] Not a manager-as-the-plan case: there is no intact franchise for a manager to defend [E2-35, E2-36].

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary (no disqualifier found; [E5-17]'s cap applies), GATE case, with
  four flags live as prompts** (a full-year guidance record of three misses and then no full-year guide; gross issuance retired
  with cash; Adjusted EBITDA as the only guided profit line, with one adjustment removed at the SEC's instruction; retention
  dropped from the release headline after it fell to 96%) **and a capital-allocation flag on buybacks.**

## Q4 — WILL IT SURVIVE? *(RECORDED, NOT GOVERNING)*

### Owner earnings — the one number **[E2-23]**
Built from the filed faces (`oe.py`, `oe_out.txt`): operating cash, less stock pay, less (c). **(c), the capex end** = *"Purchases
of and deposits on property and equipment"* plus *"Capitalized software development costs"*, plus the stock pay capitalised into
software (*"Stock-based compensation capitalized as internal use software costs"*, $0.9-3.5M a year), which sits in neither the
expensed charge nor cash capex (the TOST practice). **The D&A end** = the face's *"Depreciation and amortization"*, which carries
that capitalised stock pay as it amortises. **What the D&A is made of** (FY2025, 10-K property and intangibles notes): hardware
and other plant depreciation **$19.0M**, *"Amortization expense of internal use software"* **$23.2M**, acquired intangibles
**$1.6M**; total $43.8M, matching the face. **53% of D&A is capitalised software on two-to-five-year lives**, a recurring cost of
staying in the auction, not a legacy asset; the hardware has *"useful lives ... generally three years"*.
**[E5-20] asked on the filing: NO for the plant.** Cash capital spending over FY2021-25 was $189.9M against D&A of $191.2M: the two
ends coincide over five years, the [E2-41]/[E3-44] default case. **The one thing to watch:** hardware purchases ran **$42.5M
against hardware depreciation of $72.3M over FY2023-25** while impressions grew 28% a year, and at 2026-06-30 *"Property and
equipment included in accounts payable and accrued liabilities"* was **$9.9M against $1.2M a year earlier**, with the 10-K
expecting cost of revenue to rise *"due to increases in our data center costs as well as increases in software, hardware, and
equipment maintenance"*. The capex end of FY2023-25 may be low for a refresh that is now arriving; the D&A end is the better
three-year figure.
**The working-capital increment** is inside operating cash, and here it is large: operating cash is receivables collected from
DSPs less payables remitted to publishers. The `working_capital_flag` prompt (FY2023 payables 98% of operating cash) was read: in
FY2023 receivables took $75.7M and payables gave $79.7M, so the net was **+$4.0M**; the net of the two lines by year is +$0.9M,
+$5.4M, +$4.0M, **-$11.2M**, **+$24.2M** (FY2021-25) and **+$20.2M** over the twelve months to 2026-06-30. **FY2025 and the
trailing year were lifted by a receivable release** (receivables fell $66.6M, payables $42.4M); [E4-41] says a favourable break
is removed before the mean is trusted, so a column without the net swing is shown. **Stock pay** is subtracted in full [E5-06];
at 33.9% of operating cash over five years and **51.3% and 47.3% in FY2024-25**, the grant table was read by hand [E3-70]
(options granted x weighted grant-date fair value + RSUs granted x weighted grant-date fair value, equity notes of each 10-K):
$33.9M, $45.9M, $52.9M, $54.2M, $38.2M (FY2021-25), above the charge in every year but FY2025; H1 2026 RSU grants alone $22.9M
(3,448K at $6.64; options granted 485K at a $6.29 exercise price, fair value not in the 10-Q).

| $M | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Operating cash | 88.7 | 87.2 | 81.1 | 73.4 | 81.1 |
| Stock pay, charge (+ capitalised) | 14.1 (+0.9) | 20.6 (+1.5) | 28.9 (+2.5) | 37.7 (+3.1) | 38.4 (+3.5) |
| Stock pay, grant value | 33.9 | 45.9 | 52.9 | 54.2 | 38.2 |
| (c) capex end / D&A end | 39.4 / 23.1 | 48.9 / 34.2 | 28.3 / 44.8 | 38.5 / 45.4 | 34.9 / 43.8 |
| Receivables + payables, net | +0.9 | +5.4 | +4.0 | -11.2 | +24.2 |
| **Owner earnings, capex end** | **34.3** | **16.2** | **21.5** | **-5.9** | **4.4** |
| Owner earnings, D&A end | 51.5 | 32.3 | 7.5 | -9.6 | -1.1 |
| Owner earnings, larger stock-pay measure | 15.4 | -7.6 | -0.1 | -19.3 | 4.4 |
| Owner earnings, capex end, without the net swing | 33.4 | 10.8 | 17.5 | 5.4 | -19.8 |

- **Five-year mean (FY2021-25):** **$14.1M** capex end, **$16.1M** D&A end, **-$1.4M** at the larger stock-pay measure, $9.5M
  without the swing, $8.5M with the Martin cash ($28.1M, FY2022) charged.
- **Three-year mean (FY2023-25):** **$6.7M** capex end, **-$1.1M** D&A end, **-$5.0M** larger measure, $1.0M without the swing.
- **Twelve months to 2026-06-30:** operating cash $88.0M, stock pay $35.7M (+$3.5M capitalised), capital spending $34.0M, D&A
  $40.2M: **$14.8M** capex end, **$12.1M** D&A end, **-$5.4M without the $20.2M receivable release**; $8.2M with the H1 2026 RSU
  grant run-rate in place of the charge.
- **Combined range: about -$5M to +$16M a year.** It spans zero. **The spread is a finding [E5-11]:** FY2021 (the header-bidding
  peak, 149% retention) carries the five-year mean; without it the four-year capex-end mean is $9.1M. **Is the range too wide to
  reach a conclusion? Yes [E4-25]**, in the sense that matters: every measure the filings support puts the owner's annual take
  between a small loss and about 2% of the cap.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [ ] good · [x] **gruesome-shaped at the owner level on the five-year record**: volume grew 3.7 times and revenue
  25%, on $189.9M of capital spending and $225M of stock granted, while owner earnings fell from $34.3M (FY2021) to about zero.
  The capital keeps being added; the rate paid on it is falling. Recorded, not governing.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **NO**; owner earnings near zero in three of the last three years at one end or
  another, and revenue moved twice by a buyer's software change.
- (2) massive liquid assets: **YES, with a qualification**: $137.5M of cash and securities at 2026-06-30, 17% of the cap, no debt.
  It is not publishers' money in disguise: receivables ($383.2M) roughly equal payables ($390.0M), so the net trade position is
  -$6.8M. The undrawn revolver is not counted [E5-39].
- (3) no significant near-term cash requirements: **YES**; $40.2M of data-centre obligations and $9.0M of leases due within a
  year (10-K contractual obligations), no maturities. **Credit exposure is the one tail**: a DSP failure leaves a receivable (2023:
  $14.5M, of which $8.8M was charged back to publishers). Leverage: none [E4-16]. **Two of three.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism, in the bear's own terms:** the two buyers that account for *"a significant portion of the ad impressions
  purchased"* each own a route that does not need an independent exchange (The Trade Desk's OpenPath *"direct connection to
  publishers"*; Google's own exchange, which PubMatic is suing), and AI buying agents may *"bypass sell-side platforms"*; each
  bidding change moves spend away overnight, and the cost savings that remain are *"shared with our customers"*. Revenue per
  impression keeps falling faster than cost per impression, and the stock pay (about $36-38M a year) and the server refresh take
  what is left.
- **Quantified from filed figures:** the three largest buyers held 24%, 16% and 14% of receivables at 2025-12-31 (revenue shares
  are not filed; receivables are gross billings, a proxy). If one buyer at about a fifth of spend routed around PubMatic, twelve-month
  revenue of $289.2M would lose about $58M; at the FY2025 gross margin of 64% that is about $37M of gross profit, and operating
  income (twelve months to 2026-06-30: -$14.6M) would fall to about -$50M. Owner earnings would go negative by $30M or more a year; the $137.5M of cash would
  fund buybacks at the FY2025 pace ($46.5M) for about three years. **The company does not fail; the owner's return does.**
- **Likelihood: [x] a real possibility.** Two such bidding changes are on the record in two years (2024 and 2025), and the
  company's Q1 and Q2 2026 guides were still *"inclusive of an impact from one of our top DSP buyers"*.
- **VERDICT (RECORDED, NOT GOVERNING): [x] UNKNOWABLE.** Owner earnings span about -$5M to +$16M across windows, (c) ends and
  stock-pay measures [E4-25]; strength (1) fails. *Can I name the document that would resolve it? No: the answer is whether the
  largest buyers and AI buying agents keep routing spend through independent exchanges, which no filing contains.* **Shape #11,
  THE PASS-THROUGH, as the mechanism** (`Screens/SURVIVAL SHAPES - index.md`: the company survives but gains are passed to customers,
  compressing the owner's return; here the cost curve, in the filer's own words *"shared with our customers"*), **with #2 (stock pay
  47-51% of operating cash FY2024-25, grant value above the charge) as a feature.** No new shape.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** It did not open: Q2 OUT. What follows is arithmetic only.

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Headed as operator rule 3 requires; no entry language; no ranking.*
- **Cap:** US$799.4M (Step 0; about $935M with RSUs and options by the treasury method). Cash and securities $137.5M, no debt, so
  about **$662M** for the operations. **Sovereign:** 5.34% (US Treasury, 09/18/2026). **Floor:** ~10% [E4-28].
- **Yield, owner earnings / cap:** five-year **1.8%** (capex end), **2.0%** (D&A end), **-0.2%** (larger stock-pay measure);
  three-year **0.8%** (capex end), **-0.1%** (D&A end); twelve months **1.9%** (capex end), and **-0.7%** without the receivable
  release. On the operations alone the best figure is 2.4%.
- **What the price assumes:** a 10% expectancy on the cap needs about **$80M a year** of owner earnings ($66M on the operations),
  **5.4 times** the best trailing twelve months and more than double the best year on file ($34.3M, FY2021). Reaching it by 20%
  annual growth from $15M takes about nine years; [E4-35]'s base rate is that fewer than one in twenty of the most profitable
  companies sustain 15% for twenty years, and this one's revenue grew 5.7% a year over four years and its owner earnings fell.
- **Value, no growth, at the floor, round numbers [E4-01]:** about **$0.15bn** for the operations on the best recent owner
  earnings, plus $0.14bn of cash: about **$0.25-0.3bn** against **$0.8bn**. The ceiling [E2-63]: the service's unit price has
  fallen 66% in four years (Q2).
- **Bar:** none chosen; no margin applied; windage count zero. **VERDICT: none. Q5 did not open (Q2 OUT).**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? *(RECORDED, NOT GOVERNING)*

**Nothing is armed.** No band, no PORTFOLIO row: a Q2 OUT is a finding about the business (the QLYS ruling). **The reversal
condition, in words, pre-committed [E1-02]:** reopen Q2 only if (1) the 10-K's Item 1A drops the sentences that fee concessions are
requested *"in some cases as a condition to maintain the relationship"* and that *"we have experienced fee pressure"*, **and** (2)
revenue per impression stops falling faster than cost per impression for three years, with gross margin rising, **and** (3)
publisher net dollar-based retention holds above 105% for three years and is restored to the earnings releases, **and** (4) the
peer row shows PubMatic's owner cash per dollar of revenue at or above Magnite's for three years, with no DSP bidding change moving
revenue in that time. The monitoring question [E3-30, E4-17] does not arise for an unowned name.

**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. The file closed at Q2 (OUT); Q3-Q6 are labelled RECORDED, NOT
      GOVERNING in every heading and verdict line.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed revenue, impressions,
      cost-per-impression (reconciled to the company's own stated declines), retention and concentration series, FY2021 to Q2
      2026; the excluded parts (agentic buying products; AI agents bypassing sell-side platforms; the Google litigation) are named
      as outside the circle, not as caveats on the IN. Q3's IN is recorded, not governing.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none is used.
- [x] Every UNKNOWABLE verdict states what cannot be known (Q4, recorded: whether the largest buyers and AI agents keep routing
      spend through independent exchanges; the range -$5M to +$16M spans zero [E4-25]).
- [x] Step 0: the filing was read, with accession numbers; operating cash, stock pay, both capital lines and revenue cross-checked
      against the FY2025 10-K face; FY2021-22 from the FY2023 and FY2022 10-K faces; D&A reconciled to its three components; the
      cover count against the 10-Q balance sheet and equity statement.
- [x] Owner earnings on multi-year means (five and three years, plus twelve months); windows stated; (c) disclosed as a judgment
      with both ends and what the D&A is made of; stock pay subtracted in full, capitalised stock pay included at the capex end, and
      because it reached about half of operating cash the grant table was read by hand and the larger of charge and grant value
      shown [E3-70]; the receivable release shown separately [E4-41].
- [x] Competitor row filled from five SEC filers' own filings (MGNI, TTD, CRTO, TBLA, APPS) and Google Network's segment revenue
      beside PUBM; Magnite cross-checked to its face; the unavailable peers named with the reason (eight private or unsegmented)
      and why the class is not PROVISIONAL.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury par yield curve), dated 09/18/2026;
      `sources.sovereign()` stale and not used.
- [x] Value stated as a round-number range (about $0.25-0.3bn no-growth at the floor), and only as a COMPUTATION - NOT A CLEARANCE.
- [x] One bar chosen, not both: none, because Q5 did not open; windage count zero.
- [x] Prices dated; aggregator (Yahoo) used for the live quote only, flagged, corroborated by two Form 4 sale ranges.
- [x] Every ledger id cited was checked against `principle_ledger.csv` (81 ids, each present exactly once).
- [x] Run committed to git (template `6bcdaa9`, Step 0 `e598de8`, Q1-Q2 `2734046`, Q3-Q6 with audit and register in the next
      commit, fold after).

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **The Q1 table's Q2 2026 retention cell.** The Q1-Q2 commit (`2734046`) carries *"n/a"* for net dollar-based retention in Q2
   2026; the Q2 2026 10-Q gives **98% for the trailing twelve months to 2026-06-30** (and 96% to 2026-03-31). Found while reading the
   10-Qs for [E2-49]; the cell is corrected in this commit. It moves nothing (Q2's record 5 rests on the FY2025 96%).
2. **A mis-grabbed exhibit.** The first release fetch used an exhibit-name pattern that matched nothing on PubMatic's filings
   except the 2026-08-06 CFO retirement exhibit (EX-99.2), which it saved as `EX991_2026-08-06`. Deleted before use and every
   release refetched by its listed file name (`fetch_ex.py`).
3. **Four Q1-Q2 draft claims narrowed before commit**, each then tested: the FY2025 US share (55% drafted, 56% filed); that the
   fee-concession sentence stood in *"every 10-K since FY2020"* as *"the take-rate sentence"* (the concession and fee-pressure
   sentences are in all six; the direct-dealing sentence only FY2023-25); that volume *"quadrupled"* (3.65 times); and that twenty
   other filers name PubMatic *"as a competitor"* (some are partners or customers; Magnite's 10-K does not name it at all).

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The DSP change was dated one year late.** The brief: *"a large DSP customer changed its bidding in 2025"*. The filings: a
   first buyer's *"bidding methodology changes implemented by one of our buyers in the second half of the second fiscal quarter of
   2024"* (FY2024 10-K; *"revised its auction approach in late May 2024"*, EX-99.1 of 2025-02-27), and a **second, different** DSP's
   *"platform changes ... in the second half of 2025"* (FY2025 10-K). Neither is named in any filing.
2. **Two named competitors are not in PubMatic's filings as competitors.** Amazon appears once in the FY2025 10-K, as a
   header-bidding framework PubMatic interoperates with (*"Amazon's Transparent Ad Marketplace"*); Index Exchange appears in no
   PubMatic 10-K (grepped FY2020-25) and is not an SEC registrant. Magnite and The Trade Desk hold; Google is a buyer, a competitor
   and a litigation adversary at once.
3. **"Owns much of its own data-centre infrastructure" is half right.** It owns and runs its hardware, but in third-party
   co-location centres (*"contractual obligations to third-party data center providers"*); capital spending is modest ($28-49M a
   year including software), and **the (c) question is mostly capitalised software (53% of FY2025 D&A), not plant.**
4. **"Founder-led" understates the control.** The vote is held by two co-founder brothers, the CEO (29.3%) and the Chairman
   (36.4%), 67.8% for directors and officers together; Class B sunsets on 2030-12-11.
5. **The reproduction file name.** The brief said PATH and DASH reproduced the triage *"with a `triage_repro.py`"*; both used
   `_probe_screen.py` (the `triage_repro.py` name belongs to the SNOW-to-AEHR runs). This run used `_probe_screen.py`, copied from
   PATH's.
- **What the brief got right:** the cover count and accession exactly (re-verified from the raw inline XBRL); a two-class charter to
  be read before adding (it is economically identical); net revenue recognition; the SSP description; and the prior it asked to be
  argued against, which survived the argument.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`sources.sovereign("USD")` served the cached 09/17 row (5.29%) again**; the tenth recorded occurrence across runs.
- **`a8bc84f`'s `owner_earnings()` omitted capitalised software at the capex end** for this filer (five-year $32.4M against the
  current screen's $16.2M); the current screen's `capital_acquired()` reads it. A name priced at the triage on the old capex end
  was ranked on about double its owner earnings.
- **`da_annual` reads a depreciation-only element here** ($19.0M for FY2025 against a face D&A of $43.8M): it misses the $23.2M of
  software amortisation and $1.6M of intangibles, so the screen's D&A end is too high by about $25M a year for this filer. The
  Marvell-class limit already recorded (no tag rule recovers what the filer did not tag in the element read).
- **`capital_acquired` returns zero** for Criteo FY2021 and Digital Turbine FY2022-23 in the peer row; carried as a stated limit.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Divide revenue by the filer's own volume series, and check the cost side reproduces the filer's own number first.** PubMatic
never files its price (the cut), but it files impressions and says each year by how much its cost per impression fell. Rebuilding
cost per impression from filed revenue, gross profit and impressions matched the company's stated -19%, -8%, -18% and -20%, which
licenses the same construction on the revenue side, and there the unit price fell 66% against the cost's 52%. That is [E3-62]'s
*"how much is going to stay home"* answered from the filings, for a business whose moat claim is a cost advantage.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- **One line:** PUBM FAILS at Q2 (OUT, on the business): criterion (2) of [E3-03] fails in the company's own words across six
  10-Ks (fee concessions requested *"in some cases as a condition to maintain the relationship"*; *"we have experienced fee
  pressure"*), in two competitors' 10-Ks (Criteo: *"pure play SSPs such as Magnite or PubMatic"*; Taboola) and the largest buyer's
  direct route (The Trade Desk's OpenPath), in two buyers' bidding changes that moved revenue (2024, 2025), in a unit price down 66%
  against a unit cost down 52% with the savings *"shared with our customers"* [E3-62], and in publisher retention of 96% with no
  price increase on record; the row puts it behind Magnite on every column. Q1 IN. Price US$17.55 (2026-09-18 close); 45,550,061
  shares (A 37,303,647 + B 8,246,414, Q2 2026 10-Q cover `0001422930-26-000030`); cap US$799.4M; sovereign 5.34% (US Treasury,
  09/18/2026). Q3-Q6 recorded, not governing: Q3 IN on the binary with four flags (a GATE case), Q4 UNKNOWABLE (owner earnings
  about -$5M to +$16M), Q5 computation only (yield -0.7% to 2.0% against 5.34% and a ~10% floor).
- **If UNRESEARCHED - THE WORK ORDER:** not applicable to the governing verdict.
- **If UNKNOWABLE:** not applicable to the governing verdict.

