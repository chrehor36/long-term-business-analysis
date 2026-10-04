# Company Run — BuzzFeed, Inc. (BZFD) — 2026-09-19
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

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in
> character. If a business is complex or subject to constant change, we're not smart enough to predict future cash
> flows."* **[E3-31]**

### What the filings show, in my own words, without management's language
BuzzFeed makes free articles, quizzes, lists, recipes and videos under three names (BuzzFeed, HuffPost, Tasty) and gets paid in
four ways (FY2025 10-K MD&A and Note 3; $M):

| | FY2022 | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Advertising (display, video; mostly auctioned programmatically) | 165.4 | 113.6 | 94.4 | 91.7 | 44.0 | 34.4 |
| Content (branded content made for advertisers; since 2025 also feature films and micro-dramas) | 109.3 | 66.7 | 33.9 | 37.0 | 15.1 | 17.5 |
| Commerce and other (affiliate commissions, mostly from Amazon) | 51.1 | 50.1 | 61.7 | 56.5 | 23.3 | 15.9 |
| **Total revenue, continuing operations** | **325.8** | **230.4** | **189.9** | **185.3** | **82.4** | **67.9** |
| Time Spent (millions of hours; U.S. owned sites, Apple News, YouTube; Comscore) | 314.6 | 306.3 | 297.9 | 276.5 | 137.7 | 122.9 |
| Revenue per hour of Time Spent | $1.04 | $0.75 | $0.64 | $0.67 | $0.60 | $0.55 |
| Advertising revenue per hour | $0.53 | $0.37 | $0.32 | $0.33 | $0.32 | $0.28 |
| Net branded content advertiser revenue retention (trailing twelve months) | n/a | 50% | 41% | 48% | 46% | 41% |
| Loss from continuing operations (GAAP operating) | | (44.8) | (23.5) | (47.9) | (17.2) | (23.8) |

(FY2022-24 from the FY2024 10-K recast without Complex and First We Feast; FY2025 and H1 from the FY2025 10-K and the Q2 2026 10-Q;
`units.py`, `units_out.txt`. FY2025's loss includes a $30.2M goodwill impairment.)

**Advertising** (49% of FY2025 revenue): people read or watch; each view shows ads; most of the ad space is sold in automated auctions
(*"programmatic advertising revenue was $69.6 million"* of $91.7M in FY2025), so the price per thousand views is set by the auction, and
revenue is views times that price. **Commerce** (31%): shopping articles link to retailers; when a reader buys, the retailer pays a
commission; *"approximately 28% of our revenue was derived from Amazon, primarily from affiliate commerce transactions"* (FY2025 10-K
Item 1), and Amazon *"currently accounts for the vast majority of our affiliate commerce revenue"* (Item 1A). **Content** (20%):
advertisers commission sponsored quizzes, videos and posts; since 2025 a film studio (a 70% stake in Girls Like Girls Film Inc.) books
feature-film and *"micro-drama"* revenue. **The costs** are writers and video makers, web hosting, rent and the stock pay; cost of revenue
alone was $45.2M of $67.9M of H1 2026 revenue (10-Q). **So each dollar is: hours of attention x the auction price of the ads shown
against them, plus a commission on what readers buy at Amazon, plus sponsored work sold one campaign at a time.** Where the hours come
from is the business's first variable, and the company says it does not control it: it depends on *"referrals from third-party
platforms and Internet search companies, most prominently Apple News, Google, Facebook, YouTube, Instagram, TikTok, Snapchat, and X"*
(Item 1A).

**The scarce input the business controls:** three brand names with long-established audiences (83 U.S. and 333 foreign trademarks),
a content library, and the relationships with retailers and advertisers. **What it does not control, on its own filing:** the traffic
(*"the decline in referrals from third-party platforms and major tech companies has had, and may continue to have, an adverse impact on
our revenues"*), the ad price (set in auctions), the commission (Amazon's; *"less supplemental bonuses from our affiliate partners"*
cut FY2025 affiliate revenue), and now the owner's strategy (control passed to Byron Allen on 2026-05-26; Step 0).

**Will the fundamentals look broadly the same in ten years?** **Not on the company's own record, and it says so:** *"Our strength has
always been to adapt our business model to the evolution of the digital landscape"* (FY2025 10-K Item 1). In five years the model moved
from Facebook-distributed video (65% of 2021 Time Spent on third-party platforms when Facebook was counted, FY2022 10-K) to owned
sites (88% of 2023 Time Spent on the narrower definition that drops Facebook, FY2023 10-K), closed its news division (2023), sold Complex and First We Feast (2024), added a film studio (2025), announced *"an AI-app
incubator (Branch Office)"* (FY2025 10-K), changed owner and CEO (2026) and cut 35% of the remaining staff (8-K of 2026-07-27).

### THE CASE FOR UNKNOWABLE, AT FULL STRENGTH **[E4-26, E4-51]**
(1) [E3-31] asks for a business *"relatively simple and stable in character"*, and the filer describes its own strength as changing
its model. (2) Since May 2026 the strategy belongs to a new controller whose plans are not filed (Allen's 13D Item 4 reserves every
option; the 10-Q says the company *"is evaluating strategic changes to its operations, including asset divestitures, restructurings ...
or the discontinuance of unprofitable lines of business"*), and a related-party ad-sales agreement with Allen Media, LLC was signed on
2026-06-11 with *"no activity"* yet (10-Q Note 9). (3) Two growing pieces (the studio's film economics, which rest on estimates of
*"ultimate revenue"* over ten years, and the AI-app incubator) have no filed record to read.

**Why it does not carry, and what is excluded.** The filed business is the declared one and its economics are plain from filed series
FY2022 to H1 2026: attention hours, revenue per hour, revenue by type, the customer concentration, the retention of branded-content
buyers. Change in the model is a question about durability, which [E4-04] asks at Q2, not a gap in understanding how the money is made
today. **What is outside the circle is named: the studio (feature films and micro-dramas, $16.1M or 9% of FY2025 revenue), the AI-app
incubator, and whatever the new controller does with the company.** [E4-46] says study will not repair those; they are recorded as
outside the circle and **cannot be counted at any later gate**.

- **VERDICT: [x] IN** on the business the filings show (advertising sold against attention hours on three free-to-read brands,
  affiliate commissions chiefly from Amazon, and sponsored content; $185.3M of FY2025 revenue on 276.5M measured hours). **Not IN** for
  the studio's film economics, the AI-app incubator or the new controller's plans: outside the circle [E3-31, E4-46], never counted later.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have **no close
> substitute** and; (3) is not subject to price regulation."* **[E3-03]**, 1991 letter

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
The brief's prior was that **the hard question would be whether a publisher has any franchise against the platform owners who control
distribution**, and it asked me to argue against it. Two arguments had to be tested. **First, for a franchise:** the brands are real and
established (BuzzFeed *"Founded by Jonah Peretti in 2006"*, Tasty *"first launched in 2015"*, HuffPost bought in 2021; 416
registered trademarks); the audience is large (276.5M measured hours in
FY2025, *"a leader amongst other digital media companies in our competitive set, according to Comscore"*, Item 1); the company has
already done what a platform-dependent publisher is told to do, moving its attention onto its own sites (on the narrower Time Spent
definition, 80% owned in 2021, 83% in 2022, 88% in 2023, FY2023 10-K; on the old one, which counted Facebook, 35% in 2021 and 47% in
2022, FY2022 10-K); HuffPost *"continues to attract millions of loyal readers directly to its front page"*; programmatic prices rose in FY2025
(*"improved pricing on our owned and operated properties"*, FY2025 MD&A); and Adjusted EBITDA turned positive ($5.5M, $8.8M in
FY2024-25). **Second, against the prior's framing:** perhaps the platforms are not the decisive substitute at all, and the question is
not hard. **The evidence settles it the second way: criterion (2) fails on six records, and the decisive ones are the customers who pay
(advertisers and Amazon) and a named competitor, not the platforms alone.**

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES, and shrinking.** 276.5M hours in FY2025, down 12.1% from FY2022; H1 2026 122.9M, down 10.7%.
- **(3) Not subject to price regulation: YES.** No filing names a regulator of BuzzFeed's ad or commission prices. Privacy law constrains
  data use, not price.
- **(2) No close substitute: NO, on six independent records.**
  1. **The advertisers' own vote, measured by the company.** Net branded content advertiser revenue retention: **50%** (2023), **41%**
     (2024), **48%** (2025), **41%** (twelve months to 2026-06-30) (FY2024 and FY2025 10-K MD&A, Q2 2026 10-Q). The branded-content
     buyers of one year spent less than half as much the next; their number fell from *">40"* to *">20"*. Direct-sold advertising fell
     from $29.5M to $22.1M (FY2024-25) and direct-sold content from $28.2M to $21.0M, on *"reduced advertiser demand"*. A buyer who can
     halve his spend with you every year has a close substitute.
  2. **The company's own Item 1A names the substitutes, in the present and past tense (FY2025 10-K):** *"The increasing number of
     digital media options available, through social networking tools and news aggregation websites, has expanded consumer choice
     significantly, resulting in traffic fragmentation and increased competition for advertising"*; risks include that *"traffic engages
     with other platforms or content as an alternative to ours"*; and on search: *"AI-generated summaries, such as Google's AI Overviews
     and AI Mode, often provide answers directly on the search results page"*, with *"pressure to permit AI access to content in order to
     maintain baseline visibility, weakening our leverage in negotiating content licensing or access terms."* A reader who gets the answer
     without the click has a substitute for the page.
  3. **The platform record, the brief's prior, is real and is already history.** Time Spent on Facebook *"approximately 58 million, 184
     million, and 428 million hours for the years ended December 31, 2023, 2022, and 2021"*, after which *"Facebook now contributes an
     immaterial amount of advertising revenue"* and was dropped from the metric (FY2023 10-K). The founder's own post-mortem: *"I made the
     decision to overinvest in BuzzFeed News ... This made me slow to accept that the big platforms wouldn't provide the distribution or
     financial support required to support premium, free journalism purpose-built for social media"* (EX-99.1, 2023-04-20).
  4. **The price of the product, per unit, fell faster than the volume [E4-55].** Advertising revenue per measured hour **$0.53, $0.37,
     $0.32, $0.33** (FY2022-25), **-37%**, while hours fell 12%; revenue per hour $1.04 to $0.67; H1 2026 $0.28 of advertising per hour
     against $0.32 a year earlier. The FY2025 uptick is the auction's price, not BuzzFeed's: the 2026 10-Qs say the programmatic
     decline *"reflects traffic headwinds, which offset improved pricing and monetization efficiency"*. **Limit of this record:** Time
     Spent covers U.S. owned sites, Apple News and YouTube only, and revenue includes studio and international lines; it is a unit
     series, not a price series, carried as one record among six.
  5. **The largest single customer sets the commission.** Amazon is 28% of revenue and *"the vast majority of our affiliate commerce
     revenue"*; FY2025 affiliate revenue fell $4.1M because of *"less supplemental bonuses from our affiliate partners"*, and H1 2026
     affiliate revenue fell 31% on *"an intentional reduction in marketing spend as we manage liquidity, coupled with traffic headwinds"*.
     The price of the commerce service is the retailer's to set.
  6. **The competitor the company itself names grew through the same headwind.** BuzzFeed's 10-K names *"People, Inc. (formerly Dotdash
     Meredith)"* as a competitor. People Inc.'s FY2025 10-K (`0001628280-26-009997`): Digital revenue **$892.4M, $1,004.4M, $1,108.4M**
     (FY2023-25), Digital segment Adjusted EBITDA **$307.2M (27.7%)**, while *"Total Sessions"* fell **10%**; its growth came from
     affiliate commerce (*"the achievement of volume-related retailer incentive programs"*), *"Apple News+ and content syndication
     partners and ... OpenAI revenue"*. Same search headwind, same retailers, same Apple News: **the competitor's position held and
     BuzzFeed's did not.** No BuzzFeed filing read discloses an AI licensing agreement or any price increase (`price_sweep.txt`: six
     10-Ks FY2021-25 and two 2026 10-Qs swept for "price increase", "increase(d) (our) price", "raise(d) (our) price", "OpenAI",
     "licens... agreement with", "higher pricing", "rate increase": **no instance found**; the only hits are the UK brand licence to
     Independent Digital News and Media and the auction's *"improved pricing"*).

### [E4-04]: MUST THE MOAT BE CONTINUOUSLY REBUILT?
The test v4 sets: does the spending defend the same advantage or buy its replacement? **It buys the replacement, and the company says
so.** The basis of the business has been replaced four times in five years (Facebook distribution, then owned sites and search, then a
studio, now *"an AI-app incubator"*), and each replacement was paid for with a restructuring (15% in 2023, 16% in 2024, 5% in 2025, 35%
in 2026). This is the excluded class: *"A moat that must be continuously rebuilt will eventually be no moat at all"* [E4-04].

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
Same window where the filers allow it (FY2022-25, BuzzFeed's one-basis window), each figure from the filer's own XBRL or 10-K
(`peers/row.py`, `peers/row_out.txt`, `units_out.txt`; peer 10-Ks in `peers/`). **Owner cash** = operating cash less stock pay less
purchases of property and capitalised software, the same construction for every whole-company filer. Multi-segment filers are shown at
the segment that competes, in the segment's own measure, **labelled as a different metric**.

| Company (10-K) | what is measured | revenue, FY2025 | revenue growth, a year | owner cash / revenue, FY2022-25 | same, FY2025 | note |
|---|---|---:|---:|---:|---:|---|
| **BZFD** (`0001828972-26-000030`) | whole company, continuing | $185.3M | **-17.2%** (FY2022-25) | **-12.1%** | **-21.0%** | Adjusted EBITDA 4.7% of FY2025 revenue |
| **PPLI** People Inc. (`0001628280-26-009997`) | **Digital segment** | $1,108.4M | **+11.4%** (FY2023-25) | segment Adj. EBITDA 27.9% (FY2023-25) | 27.7% | named by BuzzFeed; whole company 0.6% (FY2025), mixed with print, search and Care.com |
| **ZD** Ziff Davis (`0001084048-26-000005`) | Digital Media segments (Tech & Shopping, Gaming & Ent., Health & Wellness) | $942.5M | +4.6% (FY2023-25) | whole company 15.5% | 16.7% | segment operating income 16.1% of revenue (FY2025) |
| **NYT** New York Times (`0000071691-26-000011`) | whole company | $2,824.9M | +7.0% | 11.4% | 16.9% | Cooking named by BuzzFeed; *"price increases on certain tenured subscribers"* |
| **TDAY** USA TODAY Co. (former Gannett) (`0001579684-26-000010`) | whole company | $2,302.2M | -7.9% | 1.1% | 2.3% | digital 46% of revenue |
| **AREN** Arena Group, now Paradium.AI (`0001628280-26-018153`) | whole company | $134.8M | -15.2% | -9.3% | 28.7% | lists *"Vice, Buzzfeed, Business Insider"* among its competitors; FY2025 figure not investigated |

**Peers taken: five SEC filers** (People Inc. and NYT because BuzzFeed's 10-K names them or their brands; Ziff Davis and USA TODAY Co.
because the brief proposed them and both run ad- and affiliate-funded digital publishing; Arena Group because EDGAR full-text search
finds it naming BuzzFeed as a competitor in 10-Ks FY2022-26, `peers/fts_out.txt`). **Not taken:** *"Vox Media (which combined with
Group Nine Media), Bustle Digital Group ... and Condé Nast"* (BuzzFeed's list) are private; Food Network sits unsegmented inside Warner
Bros. Discovery; Pinterest, Meta and Alphabet are traffic sources and ad-budget rivals, not publishers. **The class is not held
PROVISIONAL on the absent private peers**, because the verdict rests on criterion (2) in the subject's own customers' behaviour and its
own words, and the one publisher the subject names that files segment data grew 11% a year at a 28% margin through the same search decline
while the subject shrank 17% a year at a loss; no private filer could reverse that.

**What the row shows.** BuzzFeed is **last on growth and last on owner cash** among the six, below even the shrinking print-heavy
filers. **Direction [E4-32]:** owner cash per revenue dollar -9.0%, -9.1%, -12.6%, -21.0% (FY2022-25): narrowing every year.
**The row's limit [E3-61]:** it shows position, not conduct; segment EBITDA is not owner cash, and People Inc.'s and Ziff Davis's
segment figures exclude corporate costs and stock pay.

### THE OTHER Q2 TESTS
- **Returns on capital, asked about the business [E3-46]:** net loss from continuing operations **$55.7M, $34.0M, $57.3M** (FY2023-25)
  on equity of $111.2M, $106.9M, $50.1M: negative every year; no return to measure.
- **[E2-44], both halves:** price with flat demand: **not shown**; ad revenue per hour fell 37% as hours fell. Growth with minor
  capital: revenue has not grown; it fell 48% from FY2022 to the twelve months to 2026-06-30 ($325.8M to $170.7M).
- **[E4-37] agony pricing:** the company does not set its main prices (auctions, Amazon's commission schedule); where it sells direct,
  buyers kept 41-50% of their spend a year later.
- **[E3-33] untapped pricing power / [E5-28]:** claiming it would be claiming near-monopoly; the reader pays nothing and has, in the
  company's words, *"expanded consumer choice significantly"*.
- **[E2-53] the dominance class:** no. Position has not carried the economics; revenue halved in three years.
- **[E2-45] the attacker's test:** the attackers are already in: search engines answering on the results page, platforms that
  *"prioritize their formats, in lieu of sending audience traffic to publishers such as us"* (Item 1A), and every publisher bidding for
  the same Amazon commissions. The cost of entry is a website.
- **[E4-36] which cause of success:** wave-riding. The 2014-2021 record rode Facebook distribution (428M Facebook hours in 2021); the
  wave passed (58M in 2023) and the company fell off it [E3-51].
- **[E4-23] key person:** the founder left the CEO role in May 2026; the filings do not show the economics depended on him. Not recorded
  as a moat defect.
- **[E2-59]:** does not arise; no regulator sets the price.

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** · not price-regulated **[x]**
- Class: **[ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL** as a franchise; recognised brands with falling attention, sold to advertisers
  who keep under half their spend each year and to one retailer who sets the commission. Direction: **narrowing** on hours, revenue per
  hour, retention and owner cash [E4-32].
- **VERDICT: [x] OUT, ON THE BUSINESS. Permanent.** Criterion (2) of **[E3-03]** fails on six independent records: the advertisers'
  retention (41-50% a year, the company's own metric); the company's own Item 1A (*"expanded consumer choice significantly"*; AI summaries
  that *"provide answers directly on the search results page"*); the platform record (Facebook hours 428M to 58M, the founder's *"slow
  to accept that the big platforms wouldn't provide the distribution"*); advertising revenue per hour down 37% in three years; Amazon at 28%
  of revenue setting the commission; and People Inc., the competitor BuzzFeed names, growing its digital revenue 11% a year at a 28%
  segment margin through the same headwind while BuzzFeed's revenue fell 17% a year. [E4-04] fires independently: the basis has been
  replaced four times in five years. **The brief's prior is half right and half wrong:** platform dependence is real and is on the record,
  but the question was not hard, and the decisive substitutes are the paying customers' alternatives and a better-placed competitor, not
  the platforms alone. **The file closes here.** Q3 to Q6 are recorded below, **not governing**, as PATH and PUBM did.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(RECORDED, NOT GOVERNING: the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**Who "they" are changed in May 2026.** The record below covers two managements: Jonah Peretti's (founder, CEO from 2006 to 2026-05-26,
now *"President of BuzzFeed AI"*) and Byron Allen's (CEO and Chairman since 2026-05-26, controlling holder). Four months of the second
are on file. Each matter is dated to when it became public.

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution** **[E3-38, E3-43]**: Q2 found a business, not a franchise, whose traffic, prices and commissions are set by
  others and whose model has been replaced four times in five years. *"a business, unlike a franchise, can be killed by poor
  management"* [E3-43].
- [ ] **Control** **[E1-16]**: not the buyer's case (a minority purchase). **Recorded instead as the minority holder's position:** Allen
  Family Digital, LLC holds **45.7M shares, 53.5%** (13D/A of 2026-09-15), with the right to appoint six of nine directors; Peretti's
  LLC appoints one; each agreed *"to vote all shares ... in favor of the other party's director nominees"* (8-K of 2026-05-11). The
  control sale was made **without a shareholder vote**, under Nasdaq's *"financial viability exception"*. An outside holder cannot change
  management; the remedy is to sell [E4-24].
- [x] **Leverage, in its solvency form** **[E3-29, E2-54]**: a $25.0M first-lien term loan at about 10.2% (effective 15.9%) with a
  $5.0M minimum-liquidity covenant, $11.9M of film debt, against $16.3M of cash and negative operating cash; the lender moved one $5.0M
  payment three times in ten weeks (8-Ks of 2026-02-24, 2026-03-03, 2026-05-07) and fined missed *"operational milestones"* ($0.2M
  twice, 10-Q Note 8). Small absolute debt, but small errors have already threatened the equity.
- **Case declared: GATE (daily execution, with the solvency record).** No price would compensate a failure here.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
- **2021-11-15, the SPAC's Item 4.02** (`0001104659-21-139370`): 890 5th Avenue Partners re-classed its redeemable shares as temporary
  equity after SEC staff guidance; the shell's accounting, pre-merger, industry-wide. Not a conduct matter of this management.
- **2022-03-15, employee mass arbitrations**: 91 former Legacy BuzzFeed employees alleged they could not convert Class B shares and sell
  on the first trading day after the merger; the company fought arbitrability in Delaware and lost (Chancery 2024-05-15; appeal noted
  2024-09-09). A dispute over transfer mechanics, not a fraud finding; absent from the FY2025 10-K's legal discussion.
- **2023, a Video Privacy Protection Act class action** over tracking pixels on BuzzFeed.com; *"settled on January 4, 2024"*.
- **2025-03-14 (FY2024 10-K) and 2026-03-16 (FY2025 10-K): material weaknesses and going concern.** IT general controls and the close
  process (FY2024); the close-process weakness *"remained unremediated as of December 31, 2025"*. Deloitte's FY2024 and FY2025 reports
  carried a going-concern paragraph. **2026-04-13: Deloitte dismissed**, *"no 'disagreements'"*, Deloitte's letter filed (Exhibit 16.1);
  CBIZ engaged. **2026-08-06 (Q2 10-Q):** management says the substantial doubt *"has been resolved"* after the Allen money and
  $20.0M of debt repayment. Recorded as flags, below; none is a misconduct finding.
- **2026-05-11 to 2026-09-16, the control transactions, all disclosed as related-party**: 40M shares at $3.00, of which $100M is a
  note from an LLC that *"currently holds no assets other than the Shares"*, secured by 33.33M of them; 4.0M shares (2.17M new and
  1.83M from treasury) at $1.44 and 217K to Allen affiliates, and 1.7M at $1.06, each at a recent closing price (2026-06-15 for a 2026-06-17 agreement; 2026-09-10 for a 2026-09-11 agreement), approved by the audit
  committee or disinterested directors (*"Mr. Folks disclosed his interest and abstained"*, 8-K of 2026-09-16); a non-exclusive
  advertising-sales agreement with Allen Media, LLC for *"a commission on certain net revenues"*, *"subject to the Company retaining final
  approval over pricing, contracts, and content"* (10-Q Note 9). **A Special Committee of three independent directors met 11 times and
  engaged with more than 30 counterparties** before accepting (10-Q MD&A). Disclosed, priced and approved by disinterested directors; the
  terms are read at capital allocation, below.
- **A promised disclosure not yet on file.** The 8-K of 2026-05-11 says the company *"will file an amendment to this report regarding the
  material terms of the employment arrangement for Mr. Allen"* (and for Peretti) *"within four business days of the determination of such
  information"*. **No 8-K/A exists in the submissions index to 2026-09-18.** Either the terms have not been determined or the amendment is
  late; the filings do not say which. A prompt, not a finding.
- **Binary: no disqualifier found.** Written as [E5-17] requires: the absence of found disqualifiers, not a finding that the managers are
  honest.

### THE INCENTIVE READ **[E4-27]**
- **The cash bonus paid on the budget's revenue and EBITDA:** *"35% of his bonus opportunity was based upon achievement of a 2025 revenue
  target"*, *"35% was based upon achievement of a 2025 EBITDA target"*, 30% discretionary (DEF 14A 2026). Paid on the adjusted profit
  line that excludes stock pay, restructuring and impairment (below).
- **The formula paid nothing for 2024 or 2025, and discretion paid anyway:** *"no bonuses would be paid ... under the corporate bonus
  plans for 2024"*, yet *"In February 2025, the compensation committee approved the following discretionary cash bonuses and a one-time
  equity award grants ... to acknowledge their significant contributions to the company in 2024"* ($50,076, $84,094 and $82,733 to the
  CEO, CLO and CFO). **Transaction bonuses** on both disposals ($95,000 to the CFO at the Complex sale; $95,000 and $96,562 to the CFO and
  CLO at the First We Feast sale; 8-Ks of 2024-02-21 and 2024-12-12). Small sums; the direction is pay for events and effort, not for
  owner results.
- **The founder cut his own salary** from $325,000 to $115,000 for options (DEF 14A 2026), and his share of the company went from voting
  control to about 2% of the Class A on the control sale. **Equity vests on service** (*"subject to vesting based on each named executive
  officer's continued service"*).
- **The new controller's incentive is structural, and it is stated here without imputing motive:** Allen paid $20.0M in cash for 40M
  shares (about $0.50 a share in cash) and owes $100.0M, due 2031, from an entity whose only assets are BuzzFeed shares, secured by
  33.33M of them. Economically that is close to owning 6.67M shares outright at $3.00 plus a five-year right to keep 33.33M more by paying
  about $3.00 plus 5% a year, with board control meanwhile. Whether the note is paid is his choice; its value to the other holders rises
  and falls with the share price (carried at Q5).

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **weak accounting [E4-22]**: material weaknesses in FY2024 and FY2025, the close-process one unremediated at FY2025; a going-concern
  paragraph two years running; the auditor dismissed in the same season. *"There is seldom just one cockroach in the kitchen."* No
  restatement of the operating company's figures was found.
- [ ] unintelligible footnotes: none found. (One oddity recorded: the FY2024 10-K states the *"weighted average fair value of stock options
  granted"* in 2024 as $2.19, equal to the weighted exercise price in its option table; a Black-Scholes value equal to the strike is
  implausible, so one of the two figures is probably mislabelled. Carried at Q4 as a limit of the grant-value measure.)
- [x] **trumpeted projections [E4-22, E5-30], against outturn [E3-48]:**
  - **The SPAC projections** (424B3 of 2021-11-12, *"Certain Projected Financial Information"*): revenue **$521M, $654M, $833M, $1,063M**
    and Adjusted EBITDA **$57M, $117M, $187M, $263M** (2021E-24E), on *"a blended 26% compound annual growth rate"*. **Outturn**: revenue
    $397.6M (FY2021 as first reported), $436.7M (FY2022, with Complex), $252.7M (FY2023 without Complex), $189.9M (FY2024 without Complex
    and First We Feast); Adjusted EBITDA $41.5M, $0.5M, $(4.7)M, $5.5M. The passage read does not say whether the projections were
    pro forma for Complex; on either reading FY2022 missed by a third and Adjusted EBITDA by more than 99%.
  - **FY2023**: the March 2024 release, candidly, *"fell short of its initial expectations"*.
  - **FY2025**: guided at *"$195 million to $210 million"* of revenue and *"$10 million to $20 million"* of Adjusted EBITDA (EX-99.1 of
    2025-03-13), held in May and August, **cut** in November to *"$185 million to $195 million"* and *"break-even to $10 million"*;
    **actual $185.3M and $8.8M**, below the original range on both.
  - **FY2026: no guidance** (*"we are withholding 2026 guidance"*, 2026-05-11; *"focused on full-year operational targets rather than
    quarterly guidance"*, 2026-08-04). Several quarterly outlooks were reported as met (*"in line with"* the outlook, releases of 2023-03-13, 2024-05-13, 2024-08-12,
    2025-03-13, 2026-03-12); not every quarterly guide was checked against outturn. The long-range and full-year ones missed.
- [x] **serial share issuance [E5-15]**: shares outstanding 37.4M at 2025-12-31 (36.0M A plus 1.3M B) to **85.0M** at 2026-09-11
  (+128% in nine months): 40M to the controller, 2.39M in June private placements plus 1.83M treasury shares reissued, 1.7M in September, 1.85M under
  share plans; an at-the-market programme on a $150.0M shelf since 2023 (1,153,345 shares sold at an average $2.52). Driven by solvency,
  not promotion; it fires as a prompt all the same.
- [x] **adjusted-earnings promotion [E4-29], at full strength**: Adjusted EBITDA is one of the company's *"four key metrics"*
  (*"profitability ( on an Adjusted EBITDA basis, a non-GAAP financial measure )"*, FY2025 10-K Item 1), the only profit line ever guided,
  and in every release headline. It excludes D&A ($15.8M in FY2025, more than cash capital spending of $14.4M), stock pay, **restructuring
  every year** ($6.8M, $3.2M, $3.5M in FY2023-25, with $6.5-8.5M more announced for Q3 2026), impairment, transaction costs, litigation
  costs and, from FY2025, *"Amortization of capitalized interest for content"*. **FY2025: Adjusted EBITDA +$8.8M; net loss from
  continuing operations -$57.3M; owner earnings -$38.9M (Q4).** The except-for flag [E2-57, E3-53, E5-33] fires with it: a restructuring
  charge in four consecutive years is a cost of the business, not a one-off.
- [x] **[E2-49] metric switching: FIRED, mitigated.** Effective 2023 the headline Time Spent metric dropped Facebook, after Facebook hours
  fell *"approximately 58 million, 184 million, and 428 million hours"* (2023, 2022, 2021), the reason stated (*"Facebook now contributes
  an immaterial amount of advertising revenue"*) and the dropped figure disclosed that year in the FY2023 10-K. A switch that follows
  deterioration fires; the disclosure is the mitigation. Time Spent then stayed in every release through 2026 while it fell (7-22
  mentions a release, `release_metric_counts.txt`), which is the candor case for that
  metric. Net branded content advertiser revenue retention (41-50%) has been in the 10-Ks and 10-Qs since 2023 and in no release.
  The prior's tally: fired at SHOP, MRVL, PAY, ARM, CALX, BE, PUBM and now BZFD; failed at QLYS, CRM, CORT, PLTR, INOD, PATH.
- [ ] filed-figure tells [E4-30]: pretax losses in every continuing year FY2022-25; the cash-tax test has no positive base; growth is
  not smooth. Not fired.
- [ ] dividends funded by issuance [E2-52]: no dividend.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net loss from continuing operations over average total equity: **-36%** (FY2023, $55.7M on $152.9M), **-31%** (FY2024, $34.0M on
$109.1M), **-73%** (FY2025, $57.3M on $78.5M). Equity fell from $194.6M (2022-12-31) to $50.1M (2025-12-31) before the Allen issue.
There is no return on capital to judge; there is a record of capital consumed.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
**For:** the founder's 2023 memo is a rare plain post-mortem (*"I made the decision to overinvest in BuzzFeed News because I love their
work and mission so much. This made me slow to accept that the big platforms wouldn't provide the distribution or financial support
required"*; and *"the potential to generate much more revenue than we delivered"*), the kind [E4-39] calls *"almost never witnessed"*;
the 2024 release admitted the year *"fell short of its initial expectations"*; Facebook hours were disclosed when the metric dropped them;
the going-concern facts were stated plainly in the 10-K and the release. **Against:** the headline profit number excludes stock pay, D&A
and a restructuring that recurs every year; the SPAC projections were never revisited in any filing read; the promised employment-terms
amendment is not on file. **Mixed; the candor record under the founder is better than the metrics record.**

### RATIONALITY IS CAPITAL ALLOCATION
- **Complex Networks [E3-40, E2-56]:** bought 2021-12-03 for **$294.2M** ($198.0M cash plus 10M shares valued at $9.62 before the
  split), funded partly by $150M of 8.5% convertible notes; sold in two pieces for **$108.6M** (2024-02-21) and **$82.5M** (First We
  Feast, 2024-12-11), **$191.1M in all**, all of it used to repay the notes and the revolver. About $103M of the consideration did not come back, and the
  notes carried 8.5% interest for three years.
- **Buybacks [E5-08, E4-31, E5-24]:** one, on 2025-05-23: 1,826,845 shares from New Enterprise Associates at $1.82 ($3.3M), **in a year
  whose audit report already carried a going-concern paragraph**. **Condition (1) fails** (no ample funds; the company borrowed a
  $40.0M asset-backed term loan the same day). Those shares were reissued to Allen on 2026-06-18 at $1.44. **CAPITAL-ALLOCATION FLAG, with
  the humility clause [E4-13]:** management knew the business better; *"infractions, even serious ones, are innocent"* [E5-08]. It binds
  position size, never the rate. (A privately negotiated purchase from one holder; the filing gives no reason beyond the board's approval.)
- **The control sale [E5-44] in reverse:** the company sold 40M shares at a headline $3.00, four times the prior close ($0.73 on
  2026-05-11), but received $20.0M of cash (about $0.50 a share) and a non-recourse-in-substance note. Whether the other holders gained
  depends on the note's collection in 2031; the Special Committee's alternatives (more than 30 counterparties) are not filed.
- **[E2-30] institutional imperative:** (2) projects soak up funds: a studio and an AI-app incubator started while the company was
  borrowing to meet a $5.0M payment; (4) peer imitation: the SPAC listing of 2021 and the *"AI-powered"* language of 2025-26 follow the
  industry; (1) resisting change: not observed (the company changed constantly); (3) staff studies: not observable from filings.
- **[E3-58] delegation:** the 2021 SPAC and Complex purchase were banker-shaped transactions; noted, not scored further.

### THE GUARDRAIL
- [x] Nothing here promotes the name; a strong Q3 could not repair Q2 [E2-37, E2-38, E3-39].
- [x] No key-person moat defect recorded at Q2.
- [x] **Is the new controller the plan?** On the record, yes: the 10-Q ties the resolved going-concern doubt to his money, and the
  strategy is his to set. That is the *"corporate Pygmalion"* case [E2-35, E2-36], not the excisable-cancer case: there is no intact
  franchise for a manager to defend (Q2).

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary (no disqualifier found; [E5-17]'s cap applies), GATE case, with five flags
  live as prompts** (weak accounting: material weaknesses, going concern, auditor change; a projections record of large misses;
  issuance of 128% in nine months; Adjusted EBITDA as the headline profit with restructuring excluded every year; Time Spent redefined
  after Facebook collapsed, with disclosure) **and a capital-allocation flag** (a buyback in a going-concern year, and Complex bought for
  $294M and sold for $191M).

## Q4 — WILL IT SURVIVE? *(RECORDED, NOT GOVERNING)*

### Owner earnings — the one number **[E2-23]**
Built from the filed faces on the continuing perimeter (`oe.py`, `oe_out.txt`): operating cash from continuing operations, less stock
pay, less (c). **(c), the capex end** = *"Capital expenditures"* plus *"Capitalization of internal-use software"*; no stock pay is
capitalised into software (none found on the face or in the notes). **The D&A end** = the face's *"Depreciation and amortization"*.
**What the D&A is made of** (FY2025): chiefly software amortisation and leasehold depreciation; *"Depreciation and amortization decreased
... primarily due to a decrease in the depreciation of certain leasehold improvements, which were fully depreciated"*; $39.8M of
fully-depreciated headquarters leaseholds were written off in Q2 2026. **[E5-20] asked on the filing: NO.** This is not a
capital-intensive business; cash capital spending ($12.8-17.8M a year) sits near D&A ($15.8-22.7M), the [E2-41]/[E3-44] default case,
and 70-95% of it is software. **The film studio's outlay runs through operating cash** as *"Film costs"* ($18.5M absorbed in FY2025),
so a column without it is shown; the studio is outside the circle (Q1) and cannot be credited either way. **The working-capital
increment** is inside operating cash: receivables released $40.6M in FY2023 and $25.8M in FY2024 as revenue fell, which **flatters**
those years' operating cash; payables took $30.5M in FY2024. **Stock pay** is subtracted in full [E5-06]; the grant table was read by hand
[E3-70] (RSUs and options granted x weighted grant-date fair value): $6.9M, $17.3M, $6.3M (FY2023-25) against charges of $5.3M, $5.5M,
$5.8M; FY2024's option value rests on the filed $2.19 per option, which may be mislabelled (Q3).

| $M, continuing operations | FY2021* | FY2022 | FY2023 | FY2024 | FY2025 | TTM to 2026-06-30 |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash | -22.0 | 7.0 | -0.7 | -5.7 | -18.7 | -15.3 |
| Stock pay, charge | 23.6 | 18.6 | 5.3 | 5.5 | 5.8 | 6.2 |
| Stock pay, grant value | n/r | n/r | 6.9 | 17.3 | 6.3 | about 0.5 (H1 RSUs) |
| (c) capex end / D&A end | 16.0 / 22.1 | 17.8 / 22.7 | 14.9 / 20.3 | 12.8 / 19.1 | 14.4 / 15.8 | 14.4 / 15.5 |
| Film cost outlay inside operating cash | 0.0 | 0.0 | -1.7 | 0.0 | -18.5 | -17.8 |
| **Owner earnings, capex end** | **-61.6** | **-29.4** | **-20.9** | **-24.0** | **-38.9** | **-35.9** |
| Owner earnings, D&A end | -67.7 | -34.3 | -26.3 | -30.4 | -40.4 | -37.0 |
| Owner earnings, larger stock-pay measure | -61.6 | -29.4 | -22.5 | -35.7 | -39.4 | n/a |
| Owner earnings, capex end, without the film outlay | -61.6 | -29.4 | -19.2 | -24.0 | -20.4 | -18.1 |
| Owner earnings per revenue dollar (capex end) | -16.1% | -9.0% | -9.1% | -12.6% | -21.0% | -21.0% |

*FY2021 is the FY2023 10-K's basis (without Complex, with one month of First We Feast and the SPAC year's costs); FY2022-TTM are one
basis. n/r = grant table not read; the charge is used.*

- **Five-year mean (FY2021-25, a splice of two vintages):** **-$35.0M** capex end, **-$39.8M** D&A end, **-$37.7M** at the larger stock-pay
  measure, -$30.9M without the film outlay.
- **Four-year mean (FY2022-25, one basis):** **-$28.3M** capex end, **-$32.8M** D&A end, -$31.7M larger measure, -$23.2M without film.
- **Three-year mean (FY2023-25):** **-$27.9M** capex end, **-$32.4M** D&A end, -$32.5M larger measure, -$21.2M without film.
- **Twelve months to 2026-06-30:** **-$35.9M** capex end, **-$37.0M** D&A end, **-$18.1M** without the film outlay; H1 2026 alone -$15.6M.
- **Combined range: about -$18M to -$62M a year. Every window, every (c) end, every stock-pay measure and the film-free column are
  negative.** The range is wide, but it does not span zero, so a conclusion **can** be reached [E4-25]: this business has consumed cash
  for its owners in every year on file. **Favourable breaks named and removed [E4-41]:** the FY2023-24 receivable releases flatter those
  years, so the true means are worse than shown. **Management's July 2026 plan** (*"annualized savings of approximately $29.0 million to
  $32.0 million"* against $6.5-8.5M of charges) would, if achieved on flat revenue, bring the capex-end run-rate to roughly break-even;
  revenue fell 18% in H1 2026. That is a forecast, recorded and not counted.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [ ] good · [x] **gruesome, in its shrinking form**: *"the gruesome account both pays an inadequate interest rate and
  requires you to keep adding money"*. Owners and lenders have added money every year (the 2021 notes, the 2025 term loan, $26.3M from
  the controller in 2026) and the account has paid a negative rate throughout. It does not even have the growth that lures money into
  the airline case; revenue fell 48% from FY2022 to the last twelve months.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **NO**; owner earnings negative in every year FY2021-TTM.
- (2) massive liquid assets: **NO**; $16.3M of unrestricted cash at 2026-06-30 against a twelve-month cash use of about $36M at the
  capex end. The $100.5M receivable from the controller is due in 2031 and is recorded in equity, not as an asset.
- (3) no significant near-term cash requirements: **NO**; film debt of $7.7M due in the rest of 2026 and $3.9M in 2027; $3.6M of lease
  payments in the rest of 2026; $6.5-8.5M of restructuring cash by Q4 2026; the term loan's permitted overadvance steps down (*"$20.0
  million through ... August 31, 2026, and thereafter $10.0 million"*, 10-Q Note 8) against a borrowing base of receivables that shrink
  with revenue, with mandatory prepayment on asset sales or equity issuance *"subject to the Company retaining liquidity of $7.5 million"*.
  **None of three.** Leverage [E4-16]: small in dollars ($36.9M of debt), large against a business with no earnings; [E2-54]'s coverage
  test fails outright (interest cannot be met out of cash flow net of capex, because there is none).

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism, in the bear's own terms:** the route to the reader is rented. Search engines answer on the results page (*"zero-click
  searches"*), platforms *"prioritize their formats, in lieu of sending audience traffic to publishers such as us"*, and Amazon sets the
  commission on 28% of revenue; each change moves the hours or the price, and the company cannot move either back. Hours fall (-11% in
  H1 2026), revenue per hour falls (-8% in H1 2026), fixed costs are cut again (35% of staff), and the gap is filled by selling new
  shares to the controller at the market price.
- **Quantified from filed figures:** at the TTM capex-end owner earnings of -$35.9M, the $16.3M of cash lasts about half a year; at the
  film-free -$18.1M, about eleven months. Each further year funded by issuance at $1.12 needs roughly 16-32M new shares (19-38% of the
  current count). If the controller stopped buying, the lender's first lien on *"substantially all assets"* and the $5.0M liquidity
  covenant decide the outcome; the equity's claim is behind $36.9M of debt and $15.5M of leases.
- **Likelihood: [x] likely** that the owner's per-share return is destroyed by continued losses and issuance unless the 2026 cuts reverse
  the record; **a real possibility** that the company fails outright, which the controller's willingness to buy shares has so far
  prevented. The company itself wrote the going-concern doubt in March 2026.
- **VERDICT (RECORDED, NOT GOVERNING): [x] OUT.** Owner earnings negative on every window, every (c) end and every stock-pay measure
  (about -$18M to -$62M a year); gruesome; none of [E5-11]'s three strengths. *Not UNKNOWABLE: the range is wide but lies wholly below
  zero, so the conclusion is reachable [E4-25].* **Shape #19, THE SHELF, as the mechanism** (`Screens/SURVIVAL SHAPES - index.md`: the
  brand is owned but the route to the buyer is rented from counterparties who hold the buyer's data, stock a cheaper substitute beside it
  and reprice the terms; here search engines that answer on their own page, platforms that keep the traffic, and Amazon setting the
  commission) **with #8, THE EQUITY IS THE REVENUE, as a feature** (the 2026 losses were paid by new shareholders, chiefly the
  controller). No new shape.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** It did not open: Q2 OUT. What follows is arithmetic only.

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Headed as operator rule 3 requires; no entry language; no ranking.*
- **Cap:** US$93.3M on the cover count (US$95.2M after the 2026-09-11 issue). **Sovereign:** 5.34% (US Treasury, 09/18/2026).
  **Floor:** ~10% [E4-28].
- **Yield, owner earnings / cap:** five-year **-37.5%**; four-year -30.3%; three-year **-29.9%** (capex end), -34.7% (D&A end);
  twelve months **-38.4%**; the best column (twelve months without the film outlay) **-19.4%**. Every figure is negative.
- **What the price assumes:** a 10% expectancy on the cap needs about **+$9.3M a year** of owner earnings; the record's best window is
  -$18.1M, so the price assumes a swing of at least $27M a year from the record, which is roughly what management's announced savings
  would deliver if revenue stopped falling. [E4-35]'s base rate governs growth claims; here the claim is not growth but reversal.
- **The subscription, shown both ways:** (a) counting all 83.3M shares and treating the $100.5M note as worth its collateral at market
  (33.33M x $1.12 = $37.3M) leaves the cap as it is; (b) treating the 33.33M collateral shares as an unexercised option (excluded) and the
  note as uncollected gives a cap of about **$56M** on 50.0M shares. Neither changes the sign of the yield.
- **Value, no growth, at the floor, round numbers [E4-01]:** **not computable on earnings** (the earnings are negative). On assets: $16.3M
  of cash against $36.9M of debt and $15.5M of leases. The ceiling [E2-63]: bounded by what the controller pays for new shares, which has
  been the market price.
- **Bar:** none chosen; no margin applied; windage count zero. **VERDICT: none. Q5 did not open (Q2 OUT).**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? *(RECORDED, NOT GOVERNING)*

**Nothing is armed.** No band, no PORTFOLIO row: a Q2 OUT is a finding about the business (the QLYS ruling). **The reversal condition,
in words, pre-committed [E1-02]:** reopen Q2 only if (1) net branded content advertiser revenue retention holds above 100% for three
consecutive years, **and** (2) advertising revenue per measured hour rises for three years while Time Spent is flat or rising, on an
unchanged definition, **and** (3) the company files a pricing action it set itself (a subscription, a licence fee from an AI company, or a
commission rate negotiated up) that holds for two years, **and** (4) owner earnings at the capex end are positive for three consecutive
years on one perimeter with no share issuance to fund operations, **and** (5) the peer row shows BuzzFeed's revenue growth at or above
People Inc.'s Digital segment for three years. The monitoring question [E3-30, E4-17] does not arise for an unowned name.

**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. The file closed at Q2 (OUT); Q3-Q6 are labelled RECORDED, NOT GOVERNING in
      every heading and verdict line.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on filed revenue by type, Time Spent,
      revenue per hour, customer concentration and branded-content retention, FY2022 to H1 2026; the excluded parts (studio, AI-app
      incubator, the new controller's plans) are named as outside the circle, not as caveats on the IN. Q3's IN is recorded, not governing.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none is used.
- [x] Every UNKNOWABLE verdict states what cannot be known: none is used; Q4's OUT explains why UNKNOWABLE was not taken.
- [x] Step 0: the filing was read, with accession numbers; operating cash, stock pay, both capital lines, D&A and revenue cross-checked to
      the FY2025 10-K face (and to companyfacts for FY2024-25); the cover count against the 10-Q balance sheet and equity statement and
      against `Screens/cover_shares.py` (`cover_shares_out.txt`, same 83,301,378 / 33,355 / 0 and accession).
- [x] Owner earnings on multi-year means (five, four and three years plus twelve months); the perimeter splice named; (c) disclosed as a
      judgment with both ends and what the D&A is made of; stock pay subtracted in full with the grant table read by hand [E3-70]; the
      film outlay and the receivable releases named [E4-41]; discontinued operations excluded explicitly, on the filer's own recast.
- [x] Competitor row filled from five SEC filers' own filings (PPLI segment, ZD segments, NYT, TDAY, AREN) beside BZFD; unavailable
      peers named with the reason (Vox, Bustle, Condé Nast private; Food Network unsegmented) and why the class is not PROVISIONAL.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury par yield curve), dated 09/18/2026;
      `sources.sovereign()` stale and not used.
- [x] Value stated as a round-number range where computable, and only as a COMPUTATION - NOT A CLEARANCE; the earnings value is not
      computable because the earnings are negative, and the file says so.
- [x] One bar chosen, not both: none, because Q5 did not open; windage count zero.
- [x] Prices dated; aggregator (Yahoo) used for the live quote only, flagged, corroborated by two 8-K closing prices and one 13D sale.
- [x] Every ledger id cited was checked against `principle_ledger.csv` (84 distinct ids across the file, each present exactly once).
- [x] Run committed to git (template `f995f92`, Step 0 `b8e8379`, Q1-Q2 `f63b433`, Q3-Q6 with audit and register in the next commit,
      fold after).

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Two Time Spent definitions mixed in a draft.** The Q1-Q2 draft compared a 35% owned-site share (2021, a definition that counted
   Facebook) with 88% (2023, a definition that drops it) as one series. Caught before the Q1-Q2 commit; the committed text shows both
   series on their own definitions.
2. **A founding year from memory.** The same draft gave HuffPost's founding year, which no filing read states; removed before commit.
3. **The first commit attempt failed.** `git commit -F msg -- <new file>` refuses an untracked path (*"did not match any file(s) known to
   git"*); the template was staged by name and then committed with the pathspec (`f995f92`). Every later commit did the same.
4. **`cover_shares.py` was run late**, after the count had been read from the raw inline XBRL and the 10-Q face; it agreed exactly.
5. **The first 13D fetch timed out** (it tried the filer-agent CIK path first, with retries); it completed in the background and was read.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The convertible notes were repaid, not refinanced.** The brief: notes *"that were refinanced or restructured"*. The filings: the
   $150.0M 8.5% notes were amended four times (supplemental indentures 2023-07-10, 2024-02-28, 2024-10-28, 2024-12-10) and **repaid in
   full**: $120.0M in 2024 from the Complex and First We Feast sale proceeds and the last $30.0M in 2025 from a new $40.0M asset-backed
   term loan (Sound Point), which is now the debt that matters.
2. **The brief's priors omit the single largest fact: the sale of control to Byron Allen** (2026-05-11 signing, 2026-05-26 Item 5.01),
   without a shareholder vote, for $20M of cash and a $100M note secured by the shares issued. The brief did direct a deal check, which
   found it.
3. **Two proposed competitors have changed names.** *"Dotdash Meredith inside IAC/People Inc."*: IAC Inc. itself is now **People Inc.**
   (ticker PPLI, former name IAC Inc. to 2026-06-02), with a *"People Inc."* segment; **Gannett is now USA TODAY Co., Inc.** (TDAY, since
   2025-11). Vox and Vice are private, as the brief said.
4. **Pinterest is not a named traffic source in the current filings.** It appears in the FY2021 10-K's list of distribution platforms and
   in no BuzzFeed 10-K since (grepped FY2022-25); the FY2025 list is *"Apple News, Google, Facebook, YouTube, Instagram, TikTok, Snapchat,
   and X"*.
5. **The commit instruction does not work as written for new files** (above): `git commit -F <msgfile> -- <path>` on an untracked path
   fails; the path has to be staged by name first, which the pathspec then isolates.
6. **The prior the brief asked to be argued against was half wrong.** Platform dependence is real and on the record, but the franchise
   question was not hard: it fails on the paying customers' own behaviour (41-50% retention; Amazon's commission) and against the
   competitor BuzzFeed names, not only against the platforms.
- **What the brief got right:** the SPAC and Complex history; the 2024 sale of Complex and First We Feast; the 2023 closure of
  BuzzFeed News; the 1-for-4 reverse split in 2024 (effective 2024-05-06); going-concern language (FY2024 and FY2025 audit reports,
  resolved per the Q2 2026 10-Q); three share classes with Class C (empty); and the instruction to read the cover's inline XBRL first
  and compare the screen's capex end with the face, both of which found something.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`sources.sovereign("USD")` served the cached 09/17 row (5.29%) again**; the eleventh recorded occurrence across runs.
- **`a8bc84f`'s `owner_earnings()` omitted capitalised software at the capex end** for this filer too (the second after PUBM); the
  current screen's `capital_acquired()` reads it.
- **Both screens read mixed perimeter vintages** for a filer that recast discontinued operations twice: FY2023 and earlier take the
  first-filed basis, FY2024-25 the latest. `restatement_shift` measured the recast correctly (1.340) and the pipeline does not call it.
- **The dei zero for an empty class is tagged two ways by the same filer**: `ixt:fixed-zero` in its 10-Qs and `ixt-sec:numwordsen` in its
  FY2025 10-K. A reader matching only `fixed-zero` would miss the 10-K's.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**When a skip reason is a share-count problem, read the 8-Ks between the cover date and today before trusting the cover.** BuzzFeed's
latest cover (2026-08-04) is right, but a primary filing issued 1.7M more shares on 2026-09-11, and the 40M shares on the cover are paid
mostly with a note secured by themselves. The count is the easy part; what the counted shares were paid with is the part that changes
what the price means.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- **One line:** BZFD FAILS at Q2 (OUT, on the business): criterion (2) of [E3-03] fails on six records: branded-content buyers keep
  41-50% of their spend a year (the company's own metric); its Item 1A says digital options have *"expanded consumer choice
  significantly"* and AI summaries *"provide answers directly on the search results page"*; Facebook hours fell 428M to 58M (2021-23);
  advertising revenue per measured hour fell 37% (FY2022-25); Amazon, 28% of revenue, sets the commission; and People Inc., the competitor
  BuzzFeed names, grew Digital revenue 11.4% a year at a 27.7% segment margin while BuzzFeed shrank 17.2% a year; [E4-04] fires (the basis
  replaced four times in five years). Q1 IN. Price US$1.12 (2026-09-18 close); 83,334,733 shares (A 83,301,378 + B 33,355 + C 0, Q2
  2026 10-Q cover `0001828972-26-000138`; 85,034,733 after the 2026-09-11 issue); cap US$93.3M; sovereign 5.34% (US Treasury, 09/18/2026).
  Q3-Q6 recorded, not governing: Q3 IN on the binary with five flags and a capital-allocation flag (a GATE case; control sold to Byron
  Allen 2026-05-26), Q4 OUT (owner earnings about -$18M to -$62M a year on every window; gruesome; none of three strengths), Q5
  computation only (yield -19% to -38% against 5.34% and a ~10% floor).
- **If UNRESEARCHED - THE WORK ORDER:** not applicable to the governing verdict.
- **If UNKNOWABLE:** not applicable to the governing verdict.
