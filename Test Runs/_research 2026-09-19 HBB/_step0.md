## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (from about 03:00 local); the template was copied and committed before any fetch
(`17481c9`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the first name in
the "cap rejected as a broken input: read the cover" row (HBB, LCID, SOUN, BIRD). Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-19 HBB/` (scripts copied from the BZFD folder with the CIK and ticker changed). **No HBB row exists in
`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**, and none in `Screens/2026-09-01 WATCHLIST TRIAGE.csv` (grepped). Every
figure below is from Hamilton Beach's own filings, fetched by this run, with the accession.

### The entity, in every year used
CIK 0001709164, `submissions.json` (fetched by this run, `subs.py`): *"Hamilton Beach Brands Holding Co"*, SIC 3634 *"Electric
Housewares & Fans"*, `stateOfIncorporation` **"DE"**, `fiscalYearEnd` **1231**, no former names, ticker HBB on NYSE. The cover of the
Q2 2026 10-Q gives *"Delaware"*, commission file 001-38214. The registrant is a holding company whose *"only material assets held by
us are the investments in our consolidated subsidiary"*, Hamilton Beach Brands, Inc. (FY2025 10-K, MD&A liquidity). **It was spun off
from NACCO Industries on 2017-09-29**: the registrant's own companyfacts still carries its pre-spin capitalisation as a NACCO
subsidiary, **100 shares at 2017-06-30** (see the skip reason below). The 8-K list (`filings_list.txt`, 1,851 filings) begins
2017-06-16.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"cap rejected as a broken input: read the cover."* The triage narrative (reading list line 1429): *"Hamilton Beach came
back at **a market cap of ZERO and a yield of 854,301%**, because the share count did not resolve and nothing checked the quotient."*
**A prompt to read, never a verdict.** The brief's hypothesis was a per-class dei cover, the META/PATH/PUBM kind. **It holds, and it
is only half the story.** Two layers, both measured:

1. **The cover is dimensioned per class (the META/PATH/PUBM kind: two classes, no empty class).** The inline XBRL of the three latest
   periodic filings (`dei.py`, output `dei_out.txt`; raw `10Q_2026Q2_raw.htm`, `10K_FY2025_raw.htm`, `10Q_2026Q1_raw.htm`) tags
   `dei:EntityCommonStockSharesOutstanding` twice in each, each dimensioned on `us-gaap:StatementClassOfStockAxis`: in the Q2 2026
   10-Q (`0001709164-26-000160`), instant 2026-07-31, **9,858,179** (`us-gaap:CommonClassAMember`, context c-2) and **3,584,153**
   (`us-gaap:CommonClassBMember`, c-3); the FY2025 10-K (`0001709164-26-000037`) tags 9,839,337 and 3,585,996 at 2026-02-20 (twice
   each, once on the cover and once more, one pair written `9,839,337.00`); the Q1 2026 10-Q (`0001709164-26-000067`) tags 9,960,258
   and 3,585,472 at 2026-05-01. No `ixt:fixed-zero` class. **companyfacts publishes only undimensioned facts, so it carries one dei
   element for HBB, `EntityPublicFloat`** (six facts, FY2020-25 10-Ks; `_probe_screen_output.txt`), and `share_count_shift` and
   `shares_outstanding` return **None** under the current screen.
2. **What the triage actually divided by was a stale pre-spin fact, not a missing one.** The undimensioned
   `us-gaap:CommonStockSharesOutstanding` in companyfacts carries **100 shares at 2017-06-30** (filed in the 10-Q of 2018-08-01, the
   pre-spin NACCO-subsidiary capitalisation) and **zeros** at every later date (the per-class counts are dimensioned there too).
   `Backtests/scripts/bt17_microcap.py`'s `shares_asof()` falls back from the absent dei element to `CommonStockSharesOutstanding`,
   skips zero values, and **has no staleness guard**, so it returns **(2017-06-30, 100)**. **Reproduced by arithmetic:** the
   `a8bc84f` five-year D&A-end owner earnings of **$27,000,200** divided by 854,301% gives a cap of **$3,160.50**, which is **100
   shares x $31.605**, inside the 2026-08-31 trading range ($30.60-$32.03, Yahoo). A cap of $0.003M prints as **0** in a column of
   millions. **So the label "cap rejected as a broken input" was RIGHT for HBB**: the cap really was broken, by a 100-share fact nine
   years stale, reached because the per-class cover kept the real count out of companyfacts. **Which code produced the
   triage row is not on disk** (corrected before close, see the self-audit): `floor_screen.main()` at `ce98258^` reads `cap_m` from an
   input row, and the watchlist pricing script that wrote that row was never committed. What is proven is the arithmetic (100 shares
   reproduces the yield to four figures) and that `shares_asof()` is a fallback in this repository that returns exactly 100 for HBB;
   any reader of the undimensioned element without a staleness test would do the same. The current `shares_outstanding()`
   (added 2026-09-01 in `ce98258`) returns None rather than 100 because it carries a 550-day staleness test that `shares_asof()`
   does not. **The same `shares_asof()` still has no staleness guard** (read at `Backtests/scripts/bt17_microcap.py` lines 101-119);
   whether any backtest panel priced a spin-off registrant on its pre-spin share fact has not been tested by this run and is
   recorded as a tooling question, not a finding.

**The other guards, on the current screen and on `a8bc84f` over facts filed by 2026-09-01** (`_probe_screen.py`, output
`_probe_screen_output.txt`): `scale_shift` 1.09 (current) and 1.21 (`a8bc84f`), neither fired; `restatement_shift` **(1.210,
FY2017)**, which is not a triage guard (the SNOW note) and is the **Kitchen Collection removal, reproduced to the fourth decimal**: FY2017 revenue
$740,749K as first filed (FY2017 10-K, with the retail stores) against **$612,056K in the restated FY2019 10-K/A of 2020-07-24**
(continuing operations, after the Mexican-subsidiary restatement), 740,749 / 612,056 = **1.2103**; the stores were wound down in 2019
and reported as discontinued (perimeter below). `owner_earnings()` returns **positive figures at every end** (`a8bc84f`: `{'5y_da': 27.0M,
'5y_capex': 27.2M, '3y_da': 45.7M, '3y_capex': 47.4M}`; current identical to within $0.02M), **so unlike PATH and BZFD, the count WAS
the only thing that stopped the name.** `working_capital_flag` fires on 2022 (*"AccountsPayable moved 2045% of 2022 OCF"*, a
small-denominator artefact: operating cash was -$3.4M that year) and `ocf_continuing` removes discontinued cash in 4 of 11 years
($21M, the Kitchen Collection years). **Not a verdict**: Q4 rebuilds owner earnings from the filed faces.

**Restatement check.** One amendment in the window: **10-Q/A for Q1 2025, filed 2026-02-25 (`0001709164-26-000035`)**, whose
explanatory note says it was filed *"to include inline eXtensible Business Reporting Language ("iXBRL") data tagging information that
was inadvertently omitted in the original filing"*: tagging, not figures. **Two Item 4.02 non-reliance filings, 2020**, and they
matter (carried to Q3): 8-K of 2020-06-11 (`0001709164-20-000022`), the 2018 and 2019 statements *"should no longer be relied
upon"* after *"certain employees of the Company's Mexican subsidiary engaged in unauthorized transactions with the Company's Mexican
subsidiary that resulted in the recording of assets that are not realizable"*, estimated at $6-9M of 2019 and $4-6M of 2018 net
income, with a material weakness at 2019-12-31; and 8-K of 2020-07-24 (`0001709164-20-000030`), extending non-reliance to FY2017.
Preceded by a NYSE late-filing notice (8-K Item 3.01, 2020-05-22). **Auditor:** Ernst & Young LLP (PCAOB ID 42) throughout, FY2025
report signed; FY2025 Item 9A: disclosure controls and ICFR **effective**; Q2 2026 10-Q: disclosure controls effective, no changes.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run at
  03:03 local on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.34, '09/18/2026', 'US Treasury daily par yield curve')** one minute later
  (`step0_out.txt`): **current this time, not the stale cache BZFD recorded.** FRED not used. Struck by this run, not inherited.
- **Earnings currency: USD.** The business is managed from Virginia and sells chiefly in the US (Walmart 29% and Amazon 19% of FY2025
  revenue); Canada and Mexico are translated (FY2025 foreign-currency effect on revenue -$2.2M of $606.9M). No ADR or FX conversion of
  the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$31.64, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("HBB", rng="1mo", max_age_h=0)`
  (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 31.64, `regularMarketTime`
  1789761603 = 16:00:03 EDT, the closing print, exchange NYQ; the day's bar $30.95-$31.76 on 125,800 shares. `tools/sources.price()`
  returned the same 31.64 stamped 2026-09-18.
- **The month and the two years, recorded rather than choosing a day** (`price2y_out.txt`, `price2y_daily.txt`): $18.73 on
  2025-03-14, **$13.04 at the two-year low of 2025-08-15**, $16.45 at 2025-12-31, $20.92 on 2026-05-08, $23.87 on 2026-08-05 (the Q2
  release), **$27.00 on 08-06 and $31.42 on 08-07 on 227,900 shares**, $33.00 on 08-10, **two-year high $34.00 on 2026-08-17**,
  $31.64 on 09-18. **The price rose 32% in the two sessions after the release that disclosed $36.5M of IEEPA tariff refunds**, which
  the company itself calls *"non-recurring"* (10-Q MD&A). Carried to Q4 and Q5 as a windfall, not a run-rate.
- **Primary-filing cross-check:** the Q2 2026 10-Q, Part II Item 2, gives the company's own average repurchase price by month:
  *"April 1 to 30, 2026 | 33,513 | $ | 20.16"*, *"May 1 to 31, 2026 | 32,855 | $ | 19.63"*, *"June 1 to 30, 2026 | 31,501 | $ | 20.20"*.
  Yahoo's mean daily close for the same months: **$20.16, $19.49, $20.17**. **The aggregator's series is corroborated in three
  months by the issuer's own purchases.**
- **Split factor after the count's date (2026-07-31): 1.0** (`sources.split_factor_after`; no split in the filings list since the
  2017 spin). `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the class treatment from the charter
- **Class A 9,858,179 + Class B 3,584,153 = 13,442,332 shares**, from the cover of the **Form 10-Q for the quarter ended 2026-06-30,
  filed 2026-08-05, accession `0001709164-26-000160`**, the latest periodic filing: *"Number of shares of Class A Common Stock
  outstanding as of July 31, 2026: 9,858,179"* and *"Number of shares of Class B Common Stock outstanding as of July 31, 2026:
  3,584,153"*. Re-verified from the raw inline XBRL above.
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's Note 4 at 2026-06-30: *"Class A Common issued (1)(2) |
  12,083"*, *"Treasury Stock (3) | 2,219"* (thousands), so **9,864K Class A outstanding**, and *"Class B Common issued (1) | 3,584"*.
  **Consistent**: the 6K fall in Class A between 06-30 and 07-31 is inside the buyback pace (97,869 shares bought in Q2). Basic
  weighted shares Q2 2026: 13,496K.
- **Why the classes are added, one for one.** FY2025 10-K, Note on stockholders' equity: *"each share of Class A Common and Class B
  Common will be equal in respect of rights to dividends, except that in the case of dividends payable in stock, only Class A Common
  will be distributed with respect to Class A Common and only Class B Common will be distributed with respect to Class B Common. As the
  liquidation and dividend rights are identical, any distribution of earnings would be allocated to Class A and Class B stockholders on
  a proportionate basis"*. Votes differ: *"each share of the Company's Class B Common will entitle the holder of the share to ten votes"*;
  Class B is *"convertible into Class A Common on a one-for-one basis"* and *"Because of transfer restrictions, no trading market has
  developed"*. **The economic claim is one for one, so the classes add; the Class B has no quote, so it is valued at the Class A
  price, which is what its one-for-one conversion right supports.**
- **Control, measured (FY2025 10-K Item 1A):** *"certain members of the Company's extended founding family held approximately 34.4% of
  Class A Common and 93.7% of Class B Common ... could exercise 81.0% of the Company's total voting power"*, with *"no voting agreement
  among such family members"*. Class A holders carry *"approximately 21.5% of the voting power"*. Carried to Q3.

### THE PAIR
**US$31.64 x 13,442,332 x 1.0 = market cap US$425.3M** (425,315,384). Net cash at 2026-06-30: cash $101.5M less the revolver $50.0M
= **+$51.5M**, of which the $36.5M IEEPA refund is the bulk of the rise from $47.3M at 2025-12-31 (enterprise value about $374M;
recorded, not used as the yield denominator, which stays the equity cap as in every run in this queue).

### The deal check
`sources.deal_filings("0001709164")` returned **no** SC TO, SC 13E-3, DEFM14A or 425 (`step0_out.txt`, `([], [], '2026-02-25')`).
The filings list since 2024 carries: family Schedule 13D/As (2024-03-13, 2024-12-10), CEO succession (8-K 2024-09-24), two director
appointments (2024-11-20), a new Wells Fargo ABL (8-K 2024-12-17), investor presentations (Item 7.01, 2024-08-28 and 2026-01-12), a
5.02 on 2026-06-18, and the earnings 8-Ks. **No live offer.** The perimeter changes are below.

### The perimeter
- **Kitchen Collection** (160 retail stores) wind-down approved 2019-10-10 (8-K `0001709164-19-000034`, Item 2.05), *"reflected as
  discontinued operations beginning in the fourth quarter of 2019"*. Every year from FY2020 is on the continuing (Hamilton Beach
  Brands, Inc.) perimeter; FY2018-19 are recast in the FY2020 10-K.
- **Brazil and China consumer moved to a licensing model in 2022** (FY2022 10-K MD&A), a small revenue-perimeter change inside the
  continuing segment.
- **HealthBeacon Limited acquired February 2024** (FY2025 10-K Item 1), now the Health segment; *"contributed $4.3 million in revenue
  for 2024"* (FY2024 MD&A). Small against $600M+ of revenue.
- **Honest windows:** FY2021-25 (five years) and FY2023-25 (three years) on one perimeter to within the small Health addition; the
  twelve months to 2026-06-30 carry the IEEPA refund.

### The filing was read (rule 4)
- [x] MD&A [x] cash-flow statement incl. detail lines [x] footnotes
- **Documents:** FY2025 10-K filed 2026-02-25 (`0001709164-26-000037`); Q2 2026 10-Q filed 2026-08-05 (`0001709164-26-000160`); Q1
  2026 10-Q (`0001709164-26-000067`); 10-Ks FY2020-24 (`0001709164-21-000015`, `-22-000009`, `-23-000015`, `-24-000011`,
  `-25-000008`); Q1 2025 10-Q/A; DEF 14A 2026 (`0001193125-26-122754`); the 8-Ks named above. Raw text in the research folder
  (`10K_FY*.txt`, `.flat.txt`).
- **Figure cross-checked against the filed statement:** FY2025 net cash provided by operating activities, *"Net cash provided by
  (used for) operating activities | $ | 13,813 | $ | 65,415"* (FY2025 10-K MD&A table) against companyfacts' 13,813,000 and 65,415,000:
  **identical**. The Q2 2026 cash-flow face (*"Net cash provided by (used for) operating activities | 61,543 | ( 23,773 )"*) was read
  line by line for Q4.
