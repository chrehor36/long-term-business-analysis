---
## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (from about 01:50 local); the template was copied and committed before any fetch
(`f995f92`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the fifth and last
name in the "no share count from dei: read the cover" row (META, DASH, PATH and PUBM were the first four). Research, scripts and
downloaded filings are in `Test Runs/_research 2026-09-19 BZFD/`. **No BZFD row exists in `Screens/2026-09-02 MASTER RUN QUEUE
(corrected).csv`** (the triage skip reason says why). Every figure below is from BuzzFeed's own filings, fetched by this run, with
the accession.

### The entity, in every year used
CIK 0001828972, `submissions.json` (fetched by this run, `subs.py`): *"BuzzFeed, Inc."*, SIC 4899 *"Communications Services,
NEC"*, `stateOfIncorporation` **"DE"**, `fiscalYearEnd` **1231**, one former name, *"890 5th Avenue Partners, Inc."* (2020-10-26 to
2021-12-03), tickers BZFD and BZFDW on Nasdaq. **The registrant is the SPAC.** 890 5th Avenue Partners (IPO January 2021) merged with
Legacy BuzzFeed and bought Complex Networks on **2021-12-03** and took the BuzzFeed name (10-Q Note 1). **The charter has not moved
(the DASH check):** the Q2 2026 10-Q cover gives *"Delaware"*; the governing charter is the Second Amended and Restated Certificate
of Incorporation of 2021-12-03 (Exhibit 3.1 to the 8-K of 2021-12-09, `0001104659-21-148188`, saved as `CHARTER_2021.txt`), amended
2023-06-02 (officer exculpation, 8-K `0001828972-23-000112`) and 2024-04-26 (the reverse split, 8-K `0001828972-24-000099`); no
Item 5.03 since. `submissions.json` "DE" matches every filing read.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The probe (`_probe_screen.py`, copied
from PUBM's with the CIK and ticker changed; output `_probe_screen_output.txt`) shows companyfacts carries **one** dei element for
BuzzFeed, `EntityPublicFloat` (five facts, FY2021-25 10-Ks), and **no `EntityCommonStockSharesOutstanding` at all**;
`share_count_shift` returned **None** under both the current screen and `a8bc84f` (the RIVN reading: not measured, not stable), and
`shares_outstanding` returned None. **The META/DASH hypothesis (a dimensioned per-class cover) was tested on the inline XBRL** of the
three latest periodic filings (`dei.py`, output `dei_out.txt`; raw `10Q_2026Q2_raw.htm`, `10K_FY2025_raw.htm`, `10Q_2026Q1_raw.htm`),
and **it holds, in DASH's form: three classes, one of them empty.** In the Q2 2026 10-Q (`0001828972-26-000138`), each fact
dimensioned on `us-gaap:StatementClassOfStockAxis`, instant 2026-08-04:

- `dei:EntityCommonStockSharesOutstanding` **83,301,378**, `us-gaap:CommonClassAMember` (context c-4);
- the same element **33,355**, `us-gaap:CommonClassBMember` (c-5);
- the same element for `us-gaap:CommonClassCMember` (c-6): *"format="ixt:fixed-zero" ... >no"*, a zero tagged over the word "no".

The FY2025 10-K (`0001828972-26-000030`) tags the same three at 2026-03-12 (36,296,018 A; 1,342,709 B; Class C "no", **tagged there
`ixt-sec:numwordsen`, not `ixt:fixed-zero`**: the same zero under a second transform, which a reader looking only for
`fixed-zero` would miss). **companyfacts publishes only undimensioned facts, so a cover tagged per class never reaches it. For BZFD the
label was the DASH kind: a tagging convention for a three-class cover with an empty class, not a missing or stale count.**

**The other `a8bc84f` guards, on facts filed by 2026-09-01:** `scale_shift` **1.728** (did not fire); `restatement_shift` **(1.340,
FY2022)**, which is not a guard in the triage pipeline (the SNOW note) but is **a real perimeter recast, reproduced to the fourth
decimal**: FY2022 revenue of $436,674K as first filed (FY2022 10-K, with Complex) against $325,777K as recast in the FY2024 10-K (without
Complex and First We Feast), 436,674 / 325,777 = **1.3404**. **Like PATH, and unlike DASH and PUBM, the count was NOT the only thing
that stopped the name: `a8bc84f`'s `owner_earnings()` returns NEGATIVE figures at every end** (`{'5y_da': -45.9M, '5y_capex': -25.7M,
'3y_da': -39.8M, '3y_capex': -22.0M}`), so the triage would have priced it at a negative yield had it had a count. **And, as at PUBM,
`a8bc84f`'s capex end omitted capitalised software:** `annual(CAPX_TAGS)` reads *"Capital expenditures"* only ($0.7-5.4M a year
FY2021-25) and misses the separate face line *"Capitalization of internal-use software"* ($11.0-13.9M a year); the current screen's
`capital_acquired()` adds it (`{'5y_da': -44.4M, '5y_capex': -36.6M, '3y_da': -32.6M, '3y_capex': -27.6M}`), so the old capex end was
**$10.9M a year too high on five years**. The D&A end (`da_annual`) matches the face in FY2024-25 ($19,146K, $15,828K) but reads
**mixed perimeter vintages** in earlier years (FY2023 $21,941K is the FY2023 10-K's basis with First We Feast; the FY2025 10-K recasts
it to $20,333K), and the current screen's `ocf_continuing` says so itself: *"discontinued-operations cash removed from OCF in 4 of 7
years ($53M total)"*. Its `working_capital_flag` (*"ContractWithCustomerLiability moved 1198% of 2022 OCF"*) is a small-denominator
artefact: continuing operating cash was $0.6M that year on the FY2023 basis. **Not a verdict**: Q4 rebuilds owner earnings from the
filed faces on one perimeter.

**Restatement check:** no 10-K/A, 10-Q/A or 8-K/A on the registrant (`filings_list.txt`). One Item 4.02 (8-K of 2021-11-15,
`0001104659-21-139370`), **filed by the SPAC before the merger**, re-classing its redeemable public shares as temporary equity
*"In light of recent guidance provided by the U.S. Securities and Exchange Commission"*: the SPAC-wide ASC 480 correction of 2021, not
the operating company's figures. **Auditor:** Deloitte & Touche LLP through FY2025, **dismissed 2026-04-13** (8-K Item 4.01,
`0001828972-26-000033`): its FY2024 and FY2025 reports *"included an explanatory paragraph relating to substantial doubt about the
Company's ability to continue as a going concern"*; no disagreements; reportable events = material weaknesses (IT general controls,
remediated; *"a portion of the material weakness related to the financial statement close process remained unremediated as of December
31, 2025"*). CBIZ CPAs P.C. engaged for FY2026, ratified 2026-06-02 (8-K `0001828972-26-000097`). All carried to Q3.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run at
  02:04 local on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** one second earlier (`step0_out.txt`): the stale-cache defect again
  (PUBM recorded the tenth occurrence; this is the eleventh recorded). The issuing-authority figure is used. FRED not used. Struck by
  this run, not inherited from the brief or from PUBM (it happens to equal PUBM's, being the same day's row).
- **Earnings currency: USD.** H1 2026 revenue: United States $63.9M of $67.9M (94%), international $4.0M (10-Q Note 3). No ADR or FX
  conversion of the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$1.12, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("BZFD", rng="1mo", max_age_h=0)`
  (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 1.12, `regularMarketTime` 1789761602
  = **16:00:02 EDT**, the closing print, exchange NCM (Nasdaq Capital Market); the day's bar $1.103-$1.16 on 244,000 shares.
  `tools/sources.price()` returned the same 1.12 stamped 2026-09-18.
- **The month and the two years, recorded rather than choosing a day** (`price2y_out.txt`, `price2y_daily.txt`): $2.20 on 2025-03-14,
  $0.93 at 2025-12-31, **$0.567 at the low of 2026-03-30**, $0.73 on 2026-05-11 (the day the Allen purchase at $3.00 was announced),
  $1.39 on 2026-05-12 on 131.4M shares, $1.97 on 2026-05-26 (the closing date), $1.44 on 2026-06-15, $1.22 on 2026-08-04, $1.06 on
  2026-09-10, **$1.12 on 2026-09-18**. Two-year high $5.36 (2024-12-06, split-adjusted basis already; the reverse split preceded it).
- **Primary-filing cross-check:** the company's 8-K of 2026-06-22 (`0001828972-26-000102`) prices the second Allen purchase at *"$1.44
  per share, which represents the closing price on June 15, 2026"*; Yahoo's 2026-06-15 close is **$1.44**. The 8-K of 2026-09-16
  (`0001828972-26-000146`) prices the third at *"$1.06 per share, which represents the closing price on September 10, 2026"*; Yahoo's
  2026-09-10 close is **$1.06**. Vivek Ramaswamy's Schedule 13D of 2026-05-14 (`0002007997-26-000002`) reports a sale of 3,090,779
  shares on 2026-05-12 *"at an average price of $1.56"*, inside Yahoo's 2026-05-12 range ($1.35-$1.80). **The aggregator's series is
  corroborated on three dates by primary filings.**
- **Split factor after the count's date (2026-08-04): 1.0.** The **1-for-4 reverse split effective 2024-05-06** (8-K of 2024-05-02,
  `0001828972-24-000099`: *"every four (4) shares of Class A Common Stock and Class B Common Stock will be automatically combined into one
  share"*, 140,961,058 A and 5,473,940 B becoming about 35,240,370 and 1,368,493; warrants from $11.50 to *"approximately $46.00"*; note
  conversion from $12.50 to *"approximately $50.00"*) **precedes the count, so the count needs no adjustment**; every per-share figure
  before May 2024 in this file is put on the post-split basis (x4) where used. `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the class treatment from the charter
- **Class A 83,301,378 + Class B 33,355 + Class C 0 = 83,334,733 shares**, from the cover of the **Form 10-Q for the quarter ended
  2026-06-30, filed 2026-08-06, accession `0001828972-26-000138`**, the latest periodic filing: *"As of August 4, 2026, there were
  83,301,378 shares of the registrant's Class A common stock outstanding, 33,355 shares of the registrant's Class B common stock
  outstanding and no shares of the registrant's Class C common stock outstanding."* Re-verified from the raw inline XBRL above.
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's face: *"83,301 and 37,857 shares issued; 83,301 and 36,030
  shares outstanding at June 30, 2026 and December 31, 2025"* (Class A, thousands) and *"33 and 1,343 shares issued and outstanding"*
  (Class B). **Consistent; no movement between 2026-06-30 and the cover date.** The equity statement reconciles the jump: +40,000K
  (the first Allen purchase), +2,390K (private placements: 2,173K new plus 217K to Allen affiliates; 1,827K treasury shares reissued),
  +1,573K and +278K share-plan issuance, +1,310K Class B converted by Jonah Peretti, LLC.
- **After the cover date, one known issuance: 1,700,000 Class A shares to Allen Family Digital, LLC on 2026-09-11** at $1.06 (8-K
  `0001828972-26-000146`; Schedule 13D/A No. 2, `0001493152-26-042803`, reports 45,700,000 shares, *"53.5"*%). **The known count at
  2026-09-11 is therefore 85,034,733** (plus any share-plan issuance, unknown until the Q3 10-Q). Both counts are carried below; the
  register pair uses the cover as the protocol requires, with the later issuance stated beside it.
- **Why the classes are added, one for one.** Charter Art. IV: *"3.1 Equal Status . Except as expressly set forth in this Article
  IV(3), the Class A Common Stock, Class B Common Stock and Class C Common Stock shall each have the same rights and powers of, rank
  equally to (including as to dividends and distributions, and upon any liquidation, dissolution or winding up of the Corporation), share
  ratably with and be identical in all respects and to all matters to each other class of Common Stock."* Dividends (3.3) *"treated
  equally, identically and ratably, on a per share basis"*; liquidation (3.5) *"entitled to receive ratably, on a per share basis"*;
  merger (3.6) *"ratably on a per share basis"*. Votes differ: Class A one, Class B *"fifty (50) votes"*, Class C *"no voting rights except
  as required by applicable law"* (3.2.2). The 2024 amendment combined both voting classes four for one and changed no economic term.
  The 10-Q: *"net loss per share amounts were the same for Class A and Class B common stock because the holders of each class are
  entitled to equal per share dividends."* **Economically identical; the sum is the claim.** (OCR artefact flagged, not smoothed: the
  liquidation clause reads *"available for distribution to its stockholders =;"*.)
- **THE ALLEN SUBSCRIPTION: 40,000,000 of the counted shares are paid largely with a note.** Issued 2026-05-26 at $3.00 for *"$20.0
  million in cash"* plus *"a five-year secured promissory note in the principal amount of $100.0 million"* (8-K `0001828972-26-000078`;
  note filed as its Exhibit 10.3). The note: 5% interest payable semi-annually, principal of $100,000,000 due in one payment on
  *"May 26, 2031"* (Annex A), prepayable at will, secured by *"33.33 million of the Shares"*; and *"the Company understands that the
  Investor currently holds no assets other than the Shares"* (8-K of 2026-05-11). No guarantor appears in the note (grepped). On the
  balance sheet it is a **"Stock subscription receivable | ( 100,479 )"**, a contra-equity line, not an asset. **The shares are legally
  issued, vote and count in EPS** (10-Q Note 10), so they are in the count; what they are worth to the other holders depends on whether
  $100M is ever paid, which is carried at Q5.
- **Dilution not in the count** (10-Q Note 9, 2026-06-30): **5,675 thousand options at a weighted $2.83** (all out of the money at
  $1.12), **1,838 thousand unvested RSUs**, **2,469 thousand warrants at about $46.00** (expiring within the year; *"$0.02"* a warrant).
  An at-the-market programme under a $150.0M shelf remains open. No convertible debt; no preferred outstanding.

### The market cap
**$1.12 x 83,334,733 = US$93.3M** on the cover count (split factor 1.0); **$95.2M** on the known count of 85,034,733 after
2026-09-11; about $97M with the RSUs. Public float on the FY2025 10-K cover: $65.3M at 2025-06-30. **Balance sheet at 2026-06-30** (10-Q):
unrestricted cash **$16.3M** plus restricted $3.5M; term loan principal **$25.0M** (SOFR + 6.5%, floor 3.5%, *"approximately 10.2 %"*,
matures 2028-05-23, *"a first lien on substantially all assets"*, minimum liquidity $5.0M); film financing **$11.9M**; operating lease
liabilities $15.5M; the Allen receivable $100.5M in equity. Carried at Q4 and Q5, not netted here.

### THE DEAL CHECK: a completed change of control; no live offer
`sources.deal_filings("0001828972")` returned no deal forms and five 8-K Item 1.01 filings since 2026-03-16; `deal_note`: *"none
carrying a merger agreement (EX-2.1)"*. The submissions index carries **425 filings only in 2021** (the SPAC merger) and **no SC TO,
SC 13E-3, DEFM14A or PREM14A** ever. **But the 2026 record is deal-shaped and was read:** after a going-concern year, lender consents
that moved a $5.0M payment three times (8-Ks of 2026-02-24, 2026-03-03, 2026-05-07) and a Nasdaq bid-price notice (2026-03-02), a
Special Committee *"engaged with more than 30 counterparties"* (10-Q MD&A) and the company sold control to **Byron Allen** (Allen Family
Digital, LLC) under Nasdaq's *"financial viability exception"* without a shareholder vote (8-K of 2026-05-11, Item 7.01). **Item 5.01
Change in Control, 2026-05-26** (8-K `0001828972-26-000078`). Allen became CEO and Chairman; the board went to nine with Allen
appointees; Jonah Peretti converted his Class B and became *"President of BuzzFeed AI"*. Allen bought again at $1.44 (June) and $1.06
(September). **Allen's Schedule 13D (`0001493152-26-026459`) Item 4 is the standard reservation** (the reporting persons *"may ...
consider or explore extraordinary corporate transactions, such as: a merger, reorganization or take-private transaction"*); no proposal
is on file. **The quote buys a minority share of a company controlled by one holder with 53.5% of the vote and six of nine board
seats' appointment rights, not a spread on an offer.**

### The perimeter: what (c), the five-year mean and the cap must see
- **2021-02-16: HuffPost** acquired *"from entities controlled by Verizon Communications Inc."* for non-voting Class C shares (FY2021
  10-K); inside continuing operations from then. (That Class C converted to Class A in 2023, which is why the class is now empty.)
- **2021-12-03: Complex Networks** acquired at the SPAC closing ($189.9M of cash for acquisitions, FY2021); **sold 2024-02-21** for
  $108.6M cash (8-K `0001828972-24-000015`) and **recast as discontinued**.
- **2023-04-20: BuzzFeed News closed** (the founder's memo, Exhibit 99.1 to 8-K `0001828972-23-000062`: *"beginning the process of
  closing BuzzFeed News"*); its costs stay inside continuing operations.
- **2024-04: UK operations licensed** to Independent Digital News and Media; **2024-06-13: BringMe sold** ($1.3M).
- **2024-12-11: First We Feast** (Hot Ones; a Complex brand kept in February) **sold** for $82.5M (8-K `0001828972-24-000249`) and
  **recast as discontinued** in the FY2024 10-K.
- **2025-06-26: Girls Like Girls Film Inc.**, 70% bought with $4.8M of its debt; a feature-film and micro-drama studio grows inside
  "content" (studio revenue $5.7M FY2024, $16.1M FY2025).
- **2025-12-09: Goodful and As/Is sold** ($0.5M).
- **So the continuing business (BuzzFeed, HuffPost, Tasty, the studio) is filed on ONE basis for FY2022-25 and H1 2026** (FY2024 and
  FY2025 10-Ks, 2026 10-Qs; FY2022 revenue $325.8M, continuing operating cash $6,982K), on a SECOND basis for FY2021 (FY2023 10-K:
  without Complex but with one month of First We Feast; revenue $383.8M, operating cash -$22,043K, and the SPAC year's costs), and not
  at all before FY2021 on either basis (FY2020 is pre-HuffPost). **The honest windows are three years (FY2023-25) and four years
  (FY2022-25) on one basis; the five-year window FY2021-25 is a splice of two vintages and is shown as such.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K** (year ended 2025-12-31), filed **2026-03-16**, accession **`0001828972-26-000030`** (`10K_FY2025.txt`), and the
  **Q2 2026 Form 10-Q** (quarter ended 2026-06-30), filed **2026-08-06**, accession **`0001828972-26-000138`** (`10Q_2026Q2.txt`).
- Also read: the FY2021-FY2024 10-Ks (`0001104659-22-040234`, `0001828972-23-000029`, `-24-000057`, `-25-000073`); the Q1 2026 and Q2
  2025 10-Qs (`0001828972-26-000056`, `-25-000195`); the DEF 14A of 2026-04-23 (`0001828972-26-000045`) and its supplement of 2026-05-22;
  every 2026 8-K (fourteen), and the 8-Ks of 2021-11-15 (4.02), 2023-04-20 (2.05, with the memo), 2023-06-02, 2024-02-21 (Complex),
  2024-05-02 (split), 2024-12-12 (First We Feast), 2025-05-27 (term loan) and others listed in `fetch_8k.py`; the charter, its 2024
  amendment and the FY2025 Description of Securities; the promissory note and stock purchase agreement of 2026; the Schedule 13D
  filings of 2026.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statement of cash flows, $ thousands, FY2025/24/23):
  *"Cash used in operating activities from continuing operations | ( 18,748 ) | ( 5,686 ) | ( 692 )"*, *"Stock-based compensation |
  5,820 | 5,531 | 5,282"*, *"Capital expenditures | ( 1,958 ) | ( 691 ) | ( 964 )"*, *"Capitalization of internal-use software | ( 12,394
  ) | ( 12,078 ) | ( 13,934 )"* and *"Depreciation and amortization | 15,828 | 19,146 | 20,333"* match companyfacts (`ocf`,
  `sbc_annual`, `annual(CAPX_TAGS)`, `capital_acquired` = the two capital lines summed, `da_annual`) to the thousand for FY2024-25;
  revenue *"Total revenue | $ | 185,266 | $ | 189,887 | $ | 230,441"* matches for FY2024-25. **FY2023 and earlier do not match the
  screen**, because the screen reads the first-filed perimeter (above).
