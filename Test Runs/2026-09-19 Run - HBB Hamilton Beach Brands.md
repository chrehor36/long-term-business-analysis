# Company Run - Hamilton Beach Brands Holding Company (HBB) - 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
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

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** Hamilton Beach draws small kitchen appliances (blenders, coffee
  makers, toasters, slow cookers, air fryers, irons) to its own specifications, has about 70 contract factories in Asia build them
  (*"a majority of our finished products from suppliers in China"*, FY2025 10-K Item 1; *"approximately two-thirds of our suppliers
  currently based in China"*, Item 1A), pays for them in dollars, imports them through one distribution centre per region, and sells
  them on purchase orders, with no long-term contracts, to a handful of very large retailers: *"Walmart and Amazon.com accounted for
  approximately 29% and 19% of our revenue"*, the five largest 62% (FY2025). It keeps about a quarter of each sales dollar as gross
  margin (20.1% to 26.0%, FY2021-25), spends about a fifth on selling, design ($13.2M) and overhead, and keeps about 6% as operating
  profit. A smaller commercial line sells blenders and mixers to restaurants and bars (*"Approximately two-thirds of the Company's
  commercial sales are in the United States"*), and a third, tiny line (the Health segment, HealthBeacon, bought February 2024 for
  about $7.5M) leases connected sharps bins to specialty pharmacies: $7.3M of the $606.9M revenue in FY2025, a $1.3M segment loss.
  The money comes from the spread between a factory price and a retailer's buying price, per unit, on a brand the shopper recognises
  at the shelf or in the search result.
- **The scarce input this business controls:** the **Hamilton Beach and Proctor Silex trademarks** (*"the Hamilton Beach ®
  trademark is material to our business"*, Item 1) and the shelf and search placement that come with them at Walmart and Amazon.
  Not the factories (contracted, *"adequate supplier choices available"*), not a patent (*"not dependent upon any individual patent,
  copyright or license"*), not a customer contract (purchase orders). Whether the trademark is scarce **enough** is Q2's question,
  not Q1's.
- **Will the fundamentals look broadly the same in ten years?** The category will: people will still buy toasters and blenders from
  mass retailers, made in Asia, and the product changes slowly (the company's own words: *"The market for small electric household
  and specialty housewares appliances is fairly steady throughout the year"*). The revenue has sat between $603.7M and $658.4M in
  every year FY2019-25 on the continuing perimeter. What will not be the same is the cost line, which a tariff regime can move by
  more than a year's operating profit (below). **That is a question about who keeps the margin (Q2), not about how the money is
  made.**
- **Kept outside the circle, and small enough not to decide Q1 [E4-46]:** the Health segment (1.2% of revenue; regulated
  medical-device leasing in the US and Ireland), and the new premium brand Lotus (*"launched in September 2025"*). Neither is needed
  to understand where the money comes from.
- **The case for UNKNOWABLE, recorded and not taken:** the IEEPA tariff episode makes one input (the landed cost) move by policy,
  not by the business. But the mechanism is simple and the filings quantify it (a *"one-time incremental tariff cost of $5.3 million"*
  in 2025, *"IEEPA Tariff Refunds of $36.5 million"* in Q2 2026). A business whose costs are volatile but whose model is plain is
  understood; the volatility belongs to Q2 and Q4.
- **VERDICT: [x] IN**

## Q2 - IS IT A FRANCHISE? **[E3-03]**
- Needed or desired **[x]** · no close substitute **[ ] - FAILS** · not price-regulated **[x]**

**Criterion 2, on the company's own words.** The FY2025 10-K Item 1A, in the company's voice:
- *"The small electric household, specialty housewares appliances and commercial appliance industry is highly competitive and **does
  not have substantial entry barriers**."*
- *"some of our customers have expressed interest in **sourcing, or expanding the extent of sourcing, small electric household and
  commercial appliances directly from manufacturers in Asia**."*
- *"we compete with our retail customers, who use their own **private label brands**, and importers and foreign manufacturers of
  non-brand name products. Some competitors may be willing to reduce prices and accept lower profit margins to compete."*
- *"these retailers generally have **a large selection of small electric household and specialty housewares appliance suppliers from
  which to choose** ... we are increasingly dependent upon fewer customers whose **bargaining strength is growing**."*
- *"we may not be able to pass those costs on to our customers ... Our ability to raise prices to reflect increased costs may also be
  limited by competitive conditions in the market for our products."*

The buyer who writes the purchase order is the customer the [E3-03] test is put to, and the filer says that buyer can choose among many
suppliers, can source the same appliance from the factory directly, and sells its own label beside Hamilton Beach on the same shelf.
That is a close substitute, stated by the party with every incentive to say otherwise. **The two named rivals agree**: Spectrum Brands'
FY2025 10-K lists twelve *"Primary competitors for the home appliances product category"* including *"Hamilton Beach Holding Co.
(Hamilton Beach, Proctor Silex)"* and *"private label brands for major retailers"*; SharkNinja's FY2025 10-K: *"Ninja competes with brands
including Vitamix, De'Longhi, Breville, Hamilton Beach, Cuisinart and others"*, and SharkNinja says it takes *"market share from
competitors who sell products at price points above and below our own"*.

**Pricing, the test the corpus prefers to a rank [E2-44, E3-43, E3-62].** The company's own revenue bridge, every 10-K FY2020-25
(thousands; `10K_FY*.flat.txt`):

| year | unit volume and mix | average sales price | the filer's reason for the price line |
|---|---|---|---|
| 2019 | -19,613 | -1,688 | *"a loss of placements in the dollar store channel"*, tariffs |
| 2020 | -14,093 | +10,239 | *"driven primarily by product and customer mix"* |
| 2021 | +37,069 | +12,798 | *"price increases that were implemented during the back half of 2021"*; margin fell 23.0% to 20.7% because costs *"were not fully offset by the price increases"* |
| 2022 | -58,530 | +42,862 | *"Price increases implemented during 2022 partially offset the higher product and transportation costs"* |
| 2023 | +9,527 | **-28,105** | *"due primarily to lower average selling price"* |
| 2024 | +62,530 | **-30,559** | *"lower average selling prices **reflecting lower costs** during the year"* |
| 2025 | -52,943 | +7,340 | tariff price increases; *"retailers paused buying"* |
| H1 2026 | -12,052 | +11,948 | *"pricing offset volume and mix pressure"* |

**The price line follows the cost line in both directions.** When product and freight costs rose (2021-22) the price rose after them
and did not restore the margin; when costs fell (2023-24) **$58.7M of price was handed back in two years**, *"reflecting lower costs"*.
[E2-44] asks whether prices can be raised *"even when product demand is flat and capacity is not fully utilized"*; the filer shows the
opposite reflex, the pass-through, which is [E3-62]'s loom lesson in a housewares form: the savings *"flow through to the customer"*.
[E3-43]'s own test, *"a company's ability to regularly price its product or service aggressively"*, is not met in any year read.
[E4-37]'s agony measure is visible in the words: *"Our ability to raise prices ... may also be limited by competitive conditions."*
[E5-28] closes [E3-33]: nothing here resembles a near monopoly, so there is no untapped pricing power to find.

**Units, where units exist [E4-55].** Over FY2021-25 the volume-and-mix components sum to **-$2.3M** and the price components to
**+$4.3M**; nominal revenue went from $603.7M (FY2020) to $606.9M (FY2025), **+0.1% a year for five years, a real decline** across a
period of general inflation. The unit rank the filer publishes moved the wrong way: *"Hamilton Beach® is the #1 small kitchen appliance
brand in the US, in brick-and-mortar and ecommerce channels, based on units sold"* (FY2020, FY2021, FY2022, FY2023 10-Ks); FY2024 adds
a qualifier, *"the #1 small kitchen appliance **national** brand"* (which excludes store brands); **FY2025: *"the #2 small kitchen
appliance national brand in the U.S. based on units sold and grew to #4 by dollars sold"***. **Direction [E4-32]: narrowing.** And the
second-largest customer cut its buying by **23.6% in one year**: the segment note gives the two >10% customers at *"$178.3 million and
$117.7 million"* (2025) against *"$189.3 million and $154.1 million"* (2024), the second of which is Amazon by the 19%/24% shares in
Item 1.

**Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04, E4-23]** The filer's answer to its own
growth problem is to buy a new basis: *"We continue to expand in the home, health and wellness markets"* (HealthBeacon, 2024), a new
premium brand (Lotus, 2025), licensed brands it does not own (*"CHI ® premium garment care products and Clorox ™ home appliances"*,
*"Sunkist ®"*, *"Numilk ®"*). Those are purchases of replacements, not defence of the same advantage, the [E4-04] scope test. The core
brand's position is re-won each season on *"product design and innovation, quality, price and product features"* and on *"compelling
content, strong ratings and reviews"* online (Item 1): a surfing run at best [E3-51], and the wave is the retailer's.

**The second question about the business is a number [E3-46], and it is the argument against me, stated at full strength [E4-51].**
The business earns a respectable return on the little capital it uses: FY2025 operating profit $36.6M on equity of $182.8M plus the
$50.0M revolver less $47.3M of cash, about **20% pre-tax on capital employed**, with capex of $2.3-3.4M a year in FY2022-25. That is not
a franchise signature. It is the signature of an asset-light distributor whose factories, freight and shelf belong to others: the
return is high because the capital is small, not because the price is. The operating margin that return rests on is **5.8% over five
years**, and one tariff quarter moved the landed cost by $5.3M, a seventh of a year's operating profit, while a refund moved it back by
$36.5M, a full year's. **The margin is set by policy and by the buyer, not by the brand.**

**The attacker's test [E2-45].** With ample capital and skilled people, would I like to compete with Hamilton Beach? The filer says
the entry barriers are not substantial; SharkNinja did exactly that in the kitchen: its FY2025 10-K reports *"Cooking and Beverage Appliances"* of
$1,816.3M and *"Food Preparation Appliances"* of $1,550.7M, **$3,367.1M in the same categories against Hamilton Beach's whole $606.9M**,
up from $2,095.2M in FY2023, about +27% a year; and the two largest customers could and do compete through their own labels. Yes, I would.

**Which of the four causes of success [E4-36]?** None is extreme here. The record is a solid, low-margin operator of a long-lived brand,
which is Buffett's textile case [E2-37]: *"a remarkable textile company - but not a remarkable business"*, if that.

**THE COMPETITOR ROW - required [E3-28].** Same metrics, same window, filing-sourced. Consolidated figures from each filer's
companyfacts (`peers/metrics.py`, output in this run); segment figures read from the 10-Ks (`peers/*_10K_*.flat.txt`); arithmetic in
`peers/row.py`.

| Company | revenue FY2021 to FY2025, annual rate | operating margin, 5-yr | owner cash (OCF - capex - SBC) / revenue, 5-yr | gross margin FY2021 to FY2025 | source |
|---|---|---|---|---|---|
| **Hamilton Beach (HBB)** | $658.4M to $606.9M, **-2.0%** | **5.8%** | **4.3%** | 20.7% to 25.7% | 10-Ks FY2021-25; companyfacts |
| SharkNinja (SN) | $3,727.0M to $6,399.2M, **+14.5%** (kitchen categories alone $2,095.2M to $3,367.1M, FY2023-25) | 11.4% | 4.5% | 38.6% to 49.0% | 10-K FY2025 `0001957132-26-000015` (earlier years filed on 20-F); companyfacts |
| Spectrum Brands, HPC segment (SPB) | $1,260.1M to $1,153.7M (FY Sept), **-2.2%** (with the 2022 Tristar purchase inside) | segment operating margin 3.7% (FY2021), 2.2% (FY2022), -17.3% (FY2023); Adjusted EBITDA margin 8.1%, 5.1%, 3.5%, 6.1%, 4.9% | not segmented | not segmented | 10-Ks FY2022 `0000109177-22-000034`, FY2023 `-23-000054`, FY2025 `-25-000043` |
| Newell Brands, Home and Commercial Solutions segment (NWL) | $4,428M to $3,772M (FY2023-25 only), **-7.7%** | segment operating margin 0.8%, 0.0%, -3.7% (FY2023-25) | not segmented | 29.1% (FY2025, segment) | 10-K FY2025 `0000814453-26-000008` |
| Lifetime Brands (LCUT), non-electric kitchenware, same retailers | $862.9M to $647.9M, **-6.9%** | 3.5% | 3.0% | 35.1% to 37.2% | companyfacts |

HBB's comparable Spectrum-style margin (operating profit plus D&A plus stock pay), for the reader who wants the same basis as SPB's
Adjusted EBITDA: 6.0%, 7.3%, 7.2%, 8.3%, 7.7% (FY2021-25). **HBB is better run than the two segments it most resembles and than the
kitchenware channel peer, and it is not the leader.** The one filer growing is SharkNinja, which grew by taking share *"from competitors
priced both above and below"* on a 49% gross margin; Spectrum has announced *"our plan to divest our HPC business through a sale or spin
of the segment"*; Newell's segment lost money in FY2025 and its 10-K describes the same channel: retailers *"requiring suppliers to
maintain or reduce product prices"* and moving *"to import generic products directly from foreign sources and to source and sell
products under their own private label brands"*. **Nobody in the row shows pricing power, and the one who is winning is winning on the
product, not on a position.** [E3-61]: the row shows position, not conduct.

- **Peers named: 3 of the industry's ~12 real competitors, plus one channel peer.** The ~12 are Spectrum's list of twelve less
  Hamilton Beach, plus Spectrum. Taken: SharkNinja, Spectrum HPC, Newell H&CS; Lifetime Brands as a same-retailer channel peer that is
  not in Spectrum's list. **Unavailable:** De'Longhi, SEB (T-fal, Krups),
  Donlim (foreign, not SEC registrants); Conair (Cuisinart, Waring), Sensio (Bella), Versuni (Philips), Gourmia (private); Whirlpool's
  KitchenAid small appliances and Helen of Troy's appliances (inside unsegmented or mixed segments); **retailer private label
  (unsegmented, and the most important substitute of all)**.
- **Is the missing data a reason to hold the moat PROVISIONAL and call this UNRESEARCHED?** No. The verdict does not rest on the row:
  it rests on the filer's own statement that the industry *"does not have substantial entry barriers"*, on its price line following
  its cost line in every year read, and on its own rank falling from #1 to #2 by units. No missing peer's figures could turn a filer's
  own no-barrier statement and its pass-through record into a franchise. The row is corroboration, and the five filers it has agree.
- **Untapped pricing power [E3-33]:** none. A manager who raised prices without a cost reason would, on the filer's own account, lose
  placements (*"HBB's decision not to maintain very low margin business"* cost it the dollar-store channel in 2019) and face a buyer
  with *"a large selection"* of other suppliers.
- **Class: [x] NONE · Direction: narrowing** (#1 to #2 by units, #4 by dollars; the second-largest customer -23.6% in 2025; revenue flat
  nominal for five years).

**Priors argued against, as instructed.** The prior most likely wrong was that a small, low-multiple, family-controlled appliance
company is the kind of name this framework looks kindly on. **The filings refute it at Q2, before price or family is reached.** A family
that has run the business for decades and a long-lived brand name are Q3 and Q1 matters; neither makes a buyer unable to find a
substitute. Also checked and refuted or corrected: the brief's guess that the largest customers are Walmart and Amazon is **right**
(29% and 19%); its guess that private label and customer concentration are the obvious Q2 questions is **right** and they decide it;
its list of competitors was **partly right** (SharkNinja, Spectrum and Newell file usable figures; Conair is private); the rank
decline and the price pass-through were not in the brief.

- **VERDICT: [x] OUT - on the business, [E3-03] criterion 2**, with [E2-44], [E3-43], [E3-62], [E4-55], [E4-32], [E4-37], [E4-04],
  [E2-45]. *Can I name the document that would change this?* Not a document: the evidence is in, and it fails. **The file closes here.
  Q3-Q6 below are RECORDED, NOT GOVERNING.**

---
**THE FILE CLOSED AT Q2 (OUT, on the business).** Q3 to Q6 below are **RECORDED, NOT GOVERNING**: done because the evidence was
gathered and the queue records it, never to reopen Q2. Any valuation arithmetic is **COMPUTATION - NOT A CLEARANCE** and carries no
entry language.

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL? *(recorded, not governing)*

**STEP 1 - THE WEIGHT CASE.**
- [x] **Daily execution** - a have-to-be-smart-every-day business **[E3-38]**: the filer re-wins its shelf each season on *"product
  design and innovation, quality, price and product features"* against suppliers the buyer can swap; [E3-43]'s original form,
  *"a business, unlike a franchise, can be killed by poor management"*, applies because Q2 found no franchise.
- [ ] **Control** - a minority holder of Class A owns about 21.5% of the votes and cannot exit through control either way; [E1-16] is
  about owning the whole business and does not apply. (The family's 81.0% of the vote is recorded below as a fact about the register,
  not as a weight determinant.)
- [ ] **Leverage** - $50.0M of revolver against $36.6M of FY2025 operating profit and $47.3M of cash at year end; small asset errors do
  not destroy the equity.
- **Case declared: GATE, on daily execution.** No price compensates a failure here [E3-29, E1-16, E5-35 as the framework states them].

**Honesty - binary, filings-based [E5-16], each matter dated to when it became public.**
- **2020-05-11 (first disclosed; 4.02 filings 2020-06-11 and 2020-07-24): the Mexican-subsidiary irregularities.** *"certain former
  employees of one of the Company's Mexican subsidiaries engaged in unauthorized transactions with the Company's Mexican subsidiaries
  that resulted in expenditures being deferred on the balance sheet beyond the period for which the costs pertained"* (FY2020 10-K);
  FY2017-19 restated in the 10-K/A of 2020-07-24; charges of $6.9M (2019) and $1.9M (2020) in SG&A; a NYSE late-filing notice
  (2020-05-22); material weaknesses at 2019-12-31 and 2020-12-31 (the Mexican subsidiaries, and a second one *"within the income tax
  process"*), controls effective from 2021-12-31. A **$10.0M insurance recovery** for the same transactions was booked in Q1 2022 and
  received in Q2 2022 (FY2022 10-K). **Reading:** misconduct by subsidiary employees, found by the company, investigated by the audit
  committee with outside counsel, restated, disclosed in plain words, insured. No filing read names a senior officer; no SEC action
  or securities class action was found in the FY2020-22 10-Ks (a grep of the three for class-action and SEC-investigation language
  returned no instance; recorded as no instance found, per the absence-claim rule). **Not a disqualifier of the people running the
  company. It IS [E4-22]'s first flag, below.**
- **2026-06-18: the General Counsel left "effective immediately"** (8-K Item 5.02, `0001193125-26-275915`), fifteen months after
  joining, with no reason given and no successor named. Not a finding; a prompt to read the next 10-Q.
- **Related parties (DEF 14A 2026):** Alfred M. Rankin, Jr., non-executive chairman, age 84, paid **$781,625** for 2025 including a
  consulting agreement at $41,666.67 a month, reduced for 2026 to $16,666.67; his brother, daughter and son-in-law are directors
  ($187-199K each). The company says it *"may qualify as a 'controlled company'"* under NYSE rules. Disclosed, approved by the Audit
  Review Committee, and small against $36.6M of operating profit.
- **Binary: IN (no disqualifier found).** Not a finding that the managers are honest [E5-17].

**STEP 2 - THE FLAGS [E4-22, E5-15], read in the 10-Ks AND in the furnished 8-K EX-99 releases** (28 exhibits, 2021-03-16 to
2026-08-05, fetched by this run, `EX99_*.txt`; counts in `release_metric_counts.txt`):
- [x] **weak accounting - FIRED (2020), remediated.** The restatement and two material weaknesses in two consecutive years are the
  cockroach [E4-22]. Since FY2021: effective controls, Ernst & Young throughout, one critical audit matter. One further lapse: the Q1
  2025 10-Q was filed without its iXBRL tagging and amended ten months later (10-Q/A `0001709164-26-000035`), a filing-mechanics error,
  not a figure.
- [ ] unintelligible footnotes - none found; the IEEPA gain-contingency note, the supplier-finance note and the segment note are plain.
- [x] **projections - FIRED, mitigated.** Annual directional guidance every year, and since 2025 a cash range. **The record against
  outturn [E3-48]:** 2022 guided *"modest revenue growth"* and *"operating profit to increase"*: revenue -2.6%, operating profit $38.8M
  against $31.5M but **$28.8M without the $10.0M insurance recovery** (a miss). 2023 guided revenue *"flat"* and operating profit up
  *"excluding the $10.0 million insurance recovery"*: revenue -2.4% (a slight miss), operating profit $35.1M against $28.8M (a hit). 2024 guided revenue
  *"increase modestly"*, operating profit *"increase moderately"*: +4.6% and +23% (hits). 2025 guided revenue growth *"approaching the
  mid-single digit range"*, operating profit up faster than revenue, and operating-less-investing cash of *"$40 million to $50 million"*:
  **-7.3%, -15.3% and $15.7M** (misses, on the April 2025 tariffs). 2026 guidance was raised in August. **Of eight directional calls for FY2022-25, three hit (2023
  operating profit, 2024 revenue, 2024 operating profit) and five missed (2023 revenue only slightly), all modest in wording.** [E5-30]'s ratchet exists (the cash range is new since 2025); the wording is not
  trumpeting.
- [ ] serial share issuance - no. Basic weighted shares 14,036K (2023) to 13,552K (2025) to 13,496K (Q2 2026); issuance is the
  10-year-restricted equity plan (210K shares in H1 2026), bought back several times over.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] - CLEAN in all 28 releases** (the word EBITDA appears zero times; "adjusted" once
  each in 2021 and 2022, neither as a headline metric). **But the proxy is where the adjustment lives**: the 2025 short-term plan paid
  on operating profit of **$47,327,405 against the $36,579K reported**, and net sales of $630,379,388 against $606,852K reported, after
  *"adjustments ... for various items"* including *"costs relating to changes in laws and regulations"* (DEF 14A 2026). **[E2-57]'s
  except-for fires in the pay plan, mitigated**: the net-sales leg still paid only 81.7%, the ROTCE override can cut the payout by up to
  40%, the long-term award is Class A stock that *"may not be transferred for 10 years"*, and the company does not sponsor options.
  [E4-27]: what pay vests on is ROTCE (30% and 33% weights), net sales and operating profit; ROTCE is [E2-01]'s own yardstick, which
  is the best alignment feature found.
- [ ] filed-figure tells [E4-30] - FY2025 cash taxes $13,375K on pretax $35,641K (37.5%) against a 25.8% book rate: no falling-share
  tell in the one year the new ASU 2023-09 table covers; the multi-year cash-tax series was not built (limit stated). Reported growth is
  not smooth: revenue has moved -2.9%, -1.3%, +9.1%, -2.6%, -2.4%, +4.6%, -7.3% (FY2019-25).
- **Candor [E2-26]:** the IEEPA refunds are named *"non-recurring"* in the 10-Q and removed in the August outlook (*"Excluding the
  benefit from IEEPA tariff refunds, our income outlook has improved"*); the 2022 insurance recovery was excluded from the 2023 outlook.
  **Both adjustments remove a FAVOURABLE item** [E2-69's direction test]: the candor case, not the except-for case. **[E2-49]
  metric-switching, checked across the 10-Ks: FIRED, mildly.** The market-rank headline changed basis twice as the rank fell: *"#1 small
  kitchen appliance brand ... based on units sold"* (FY2020-23) to *"#1 ... national brand"* (FY2024, a narrower denominator) to *"#2
  ... national brand ... based on units sold and grew to #4 by dollars sold"* (FY2025). The fall is disclosed, not hidden, but the
  qualifier arrived the year before it.

**STEP 3 - THE PRIMARY TEST [E2-01]**, balance sheet first (companyfacts `StockholdersEquity`, cross-read to the faces; `roe_out.txt`):
net income on average equity **41.4% (2020), 23.4%, 22.3%, 18.6%, 19.6%, 15.2% (2025)**. Equity rose from $80.1M to $182.8M while net
income went from $24.1M to $26.5M: the retained earnings paid down the revolver ($98.4M to $50.0M) and built cash ($2.4M to $47.3M), so
capital employed (equity plus debt less cash) was about $176M in 2020 and $185.5M in 2025, earning a flat operating profit. The proxy's
own ROTCE for 2025, adjusted, is **21.0%** (*"Adjusted Average Total Capital Employed $170,229"*). **A good return on a small, unmoving
capital base; not a rising one.**

**The half-owner test [E2-26]:** the 10-Q reports the refund at every line, with the ex-refund margin beside it (*"Excluding these
benefits, gross profit margin would have been 26.1%"*): passes.

**The institutional imperative [E2-30]:**
- [ ] resists change - no: Kitchen Collection closed (2019), Brazil and China moved to licensing (2022), an ERP cutover in 2020 and a
  second replacement under way in 2026 (the *"accelerated depreciation of the Company's legacy enterprise resource planning (ERP) system"*).
- [x] **projects materialise to soak up funds - mild.** HealthBeacon (*"for € 6.9 million (approximately $ 7.5 million)"*, 2024), after
  a *"secured loan"* to it ($1.6M in 2023, $0.6M in 2024); a segment loss of $5.1M (2024) and $1.3M (2025). Small in dollars.
- [ ] staff studies - no instance found.
- [x] **peer imitation - mild.** Premium brands (Lotus), licensed brands, *"home, health and wellness"*: the category's common
  playbook, which SharkNinja's product-led growth has not been matched by.

**Capital allocation - the buyback conditions [E5-08, E4-31]:**
- (1) ample funds: yes; the revolver sits at $50.0M with $54.3M of excess availability and $101.5M of cash at 2026-06-30.
- (2) a material discount to conservatively calculated IV: repurchases of 638,381 shares for $13.5M in 2024 (about $21.1), 467,804
  for $8.3M in 2025 (about $17.7), and 153,282 for $2.9M in H1 2026 (about $19.0). Against the five-year owner earnings of about $27M
  (Q4), a price of $17-21 on about 13.5M shares is a cap of $230-285M, a yield of about 9.5-11.7% on a business whose revenue is flat
  nominal: **near the value this run would put on it, not at a material discount to it.** **CAPITAL-ALLOCATION FLAG, with the humility
  clause [E4-13]: management knows the business better than I do, and this rests on my own range.** It binds position size, never the
  rate; here there is no position.

**THE GUARDRAIL:** [x] nothing in this Q3 promotes the name; a long-tenured family, a ROTCE-based pay plan and a candid refund note
cannot repair Q2 [E2-37, E2-38, E3-39]. [x] No superstar dependence recorded at Q2 [E4-23]. [x] The manager is not the plan.
- **VERDICT (recorded, not governing): [x] IN** on the binary (no disqualifier found), with the weak-accounting flag (2020,
  remediated), a mild projections flag, a mild metric-switch, the pay-plan except-for, and a capital-allocation flag.

## Q4 - WILL IT SURVIVE? *(recorded, not governing)*

### Owner earnings **[E2-23]** - from the filed cash-flow faces (`oe.py`, output `oe_out.txt`), $M, continuing operations
CONVENTION per v4: operating cash flow less stock pay less (c).

| FY | OCF | capex | D&A | SBC | OCF - SBC - capex | OCF - SBC - D&A |
|---|---|---|---|---|---|---|
| 2019 | 0.2 | 4.1 | 4.0 | 2.8 | -6.7 | -6.6 |
| 2020 | -27.9 | 3.3 | 3.9 | 4.0 | -35.2 | -35.8 |
| 2021 | 17.9 | 11.8 | 4.9 | 3.2 | 2.8 | 9.7 |
| 2022 | -3.4 | 2.3 | 4.9 | 3.4 | -9.1 | -11.7 |
| 2023 | 88.6 | 3.4 | 4.4 | 5.4 | 79.8 | 78.9 |
| 2024 | 65.4 | 3.2 | 4.8 | 6.3 | 56.0 | 54.3 |
| 2025 | 13.8 | 2.8 | 5.9 | 4.1 | 6.9 | 3.8 |

- **Five-year mean, FY2021-25 (the corpus default [E2-42]): $27.0M (D&A end) to $27.3M (capex end).** Cross-check: five-year mean
  operating profit $37.0M after the FY2025 25.8% tax rate is $27.5M; the two constructions agree within 2%.
- **Three-year mean, FY2023-25: $45.7M to $47.6M.** **Seven-year mean, FY2019-25: $13.2M to $13.5M.**
- **Twelve months to 2026-06-30:** OCF $99.1M, capex $2.2M, SBC $4.7M = $92.2M; **less the $36.5M IEEPA refund = $55.7M** (the refund
  is removed as [E4-41] requires: a favourable exogenous break, which the filer itself calls non-recurring; the tax on it is not
  separately removed, so $55.7M is still slightly high).
- **Spread, conservative end:** the three-year mean is 1.7x the five-year and 3.5x the seven-year. **The width is working capital, and
  the filings name every distorted year** [E5-11]: 2020's inventory build of $65.8M (pandemic demand and the ERP cutover), 2022's payable
  release of $69.9M against the supply-chain build, 2023's reversal (+$30.8M inventory, +$37.5M payables), and the supplier-finance
  programme moving payables ($56.9M to $29.9M outstanding, 2024 to 2025). Over five years these net out, which is why the five-year mean
  matches after-tax operating profit. **Range: $27M (five-year, the default) to $48M (three-year, flattered by the 2023 release).**
- **(c) - the D&A default applies [E3-44, E2-41].** Not capital-intensive: PP&E net $25.5M, capex $2.3-3.4M a year FY2022-25 (FY2021's
  $11.8M was the ERP); the [E5-20] exception class does not apply. The capex band is $0.3M wide on five years and changes nothing.
- **Working-capital increment:** inside OCF, which is why OCF is used. **Stock pay [E5-06]:** subtracted at the charge ($2.8-6.3M a
  year; 12.3% of five-year OCF); restricted Class A stock at a formula price, no options, so [E3-70]'s option-value measure does not
  arise.
- *Does the capex band change the verdict?* No.

### Great, good, or gruesome? **[E4-20]**
- [ ] great [x] **good, on the capital it has** [ ] gruesome. About 20% pre-tax on roughly $185M of capital employed, needing almost no
  capex; but the return is not rising (ROE 23% to 15% as equity accumulated) and the business has not grown, so [E4-43]'s "earned also
  on added capital" is untested.

### Staying power **[E5-11]**
- (1) **large and reliable stream of earnings: partial.** Operating profit $31.5-43.2M in every year FY2020-25; operating cash negative
  in two of seven years (2020, 2022) and near zero in a third (2019) because of working capital.
- (2) **massive liquid assets: no.** $47.3M of cash against $50.0M of revolver at 2025-12-31; $101.5M at 2026-06-30 only because of the
  refund.
- (3) **no significant near-term cash requirements: mostly yes, with one dependence.** The revolver matures 2029-12-13; lease liabilities
  $39.6M; dividends about $6.6M a year. **But the seasonal inventory is financed by the bank**: *"We generally use cash on hand or
  borrowings under our $125 million senior secured floating-rate revolving credit facility ... to finance inventory"*, with a borrowing
  base on receivables and inventory and a springing fixed-charge covenant below $15M of availability. That is [E5-39]'s *"kindness of
  strangers"* for one season a year.
- **Leverage [E4-16, E2-54]:** $50.0M drawn, interest expense $0.7M against operating profit $36.6M (FY2025); covered many times out of
  cash flow net of capex. Low.

### The specific way THIS business dies **[E2-27, E3-24, E4-40]**
- **The mechanism:** a large customer moves a category to its own label or buys direct from the factory (both named by the filer), at
  the same time as a tariff or freight shock the price line cannot pass on. **Quantified from filed figures:** Walmart bought $178.3M in
  2025. Losing half of it at the FY2025 gross margin of 25.7% removes about $23M of gross profit against $36.6M of operating profit;
  losing all of it removes about $46M and turns operating profit into a loss of about $9M unless SG&A ($119.3M) falls by about 8%. The second customer
  already fell 23.6% in one year. A temporary spike to a 125% China tariff cost a *"one-time incremental tariff cost of $5.3 million"*; a sustained rate of that order,
  not passed on, would plausibly exceed a year's operating profit (an extrapolation, not a filed figure). **Likelihood: a real possibility** for a partial customer loss over a decade; the full loss of either
  a low-level possibility (the filer: *"we have long-established relationships with many customers, including Walmart and
  Amazon.com"*, but *"we do not have any long-term supply contracts with these customers"*).
- **VERDICT (recorded, not governing): [x] IN** - owner earnings positive on the default five-year window at both (c) ends and on the
  three-year; the range is wide but its cause is named and nets out; one strength partial, one absent, the third mostly present.
  **[E4-51]'s bear case above is the one its holders would accept.**

---
⛔ **Q5 is not a clearance.** Q2 is OUT. The arithmetic below is **COMPUTATION - NOT A CLEARANCE**.

## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? *(COMPUTATION - NOT A CLEARANCE)*
- **The yield:** owner earnings $27.0-27.3M (five-year) ÷ cap $425.3M = **6.35-6.41%**; three-year $45.7-47.6M = 10.7-11.2%;
  seven-year 3.1-3.2%; twelve months without the refund $55.7M = 13.1%. **Sovereign 5.34%** (US Treasury 30-year, 09/18/2026).
- **The floor first [E4-28]:** ~10% on $425.3M needs **$42.5M** a year of owner earnings. The five-year default gives $27.0-27.3M:
  **about 57% short**, and the business's own record is flat nominal revenue for seven years, so no growth closes it [E4-35, E4-44].
  Only the three-year window (flattered by the 2023 working-capital release) and the refund-inflated twelve months reach it. **Below the
  floor on the default window: quit on, whatever the bond.**
- **What the price already assumes:** a lasting step from $27M to about $42.5M of owner earnings, i.e. that the three-year mean (or the
  ex-refund twelve months) is the new level. The filer's own 2026 guidance is operating profit down *"high-single digits"* excluding the
  refunds.
- **Points over the sovereign:** +1.0 point on the five-year default.
- **Value range, round numbers [E4-01]:** at a 10% floor, $270M to $480M (five-year to three-year owner earnings), about **$20 to $35 a
  share**, before the roughly $50M of net cash at 2026-06-30. **Price $31.64 sits inside the range: [E4-01]'s middle outcome, no useful
  conclusion**, even before Q2's verdict is remembered. **What bounds the upside [E2-63]:** a no-growth business capped at its owner
  earnings.
- **Windage count:** one (the floor). **No bar is chosen, because no bar applies to a Q2 OUT.**
- **VERDICT: not reached (Q2 OUT).**

## Q6 - WHAT WOULD PROVE ME WRONG? *(recorded; reversal condition in words, no band)*
A Q2 OUT is a finding about the business; a price alert would be a category error (the QLYS ruling). **Reopen Q2 only if:**
1. the revenue bridge shows a **positive average-sales-price contribution in a year when product and freight costs fell**, in three
   years out of four [E2-44, E3-43];
2. the published unit rank returns to **#1 on an unchanged basis** and the dollar rank rises, for two consecutive 10-Ks [E4-55, E4-32];
3. gross margin **above 26%, excluding windfalls, for three years while Walmart's and Amazon's shares of revenue hold or rise**;
4. the Item 1A sentence that the industry *"does not have substantial entry barriers"* is withdrawn with a stated reason; and
5. revenue grows at least as fast as SharkNinja's kitchen categories for three years.
**The monitoring question [E3-30]:** the FY2025 rank fall and the Amazon cut could be tariff-year aberrations; the pass-through of 2023-24
was not, because costs were falling and there was no tariff to blame.

---
## SELF-AUDIT
- [x] Questions answered in order; the file closed at Q2 and Q3-Q6 are headed recorded, not governing.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Q1 IN rests on the 10-K's own description.
- [x] No UNRESEARCHED or UNKNOWABLE verdict issued. Q2's missing peers (De'Longhi, SEB, Donlim, Conair, Sensio, Versuni, Gourmia,
  private label) were weighed and did not make the moat PROVISIONAL, for the reason stated at Q2: the verdict rests on the filer's own
  words and its own price record.
- [x] Step 0: filings read with accession numbers; FY2025 OCF cross-checked to the face (13,813) and the cover count to Note 4.
- [x] Owner earnings on multi-year means, three windows and the twelve months, (c) disclosed, the refund removed [E4-41].
- [x] Competitor row filled from five filers' filings.
- [x] Sovereign from the US Treasury, dated 09/18/2026, for USD earnings.
- [x] Value stated as a round range; windage one; no bar applied (Q2 OUT).
- [x] Price dated and flagged, corroborated by the issuer's own monthly repurchase prices.
- [x] Committed: template `17481c9`, Step 0 `5755895`, Q1-Q2 `acf2bab`, Q3-Q6 and this audit in the next commit, fold after.

**Corrections made before close (operator rule 6 applies to closed runs; recorded here so nothing is silent):**
1. **Step 0 first said the triage "actually divided by" a fact reached through `bt17_microcap.shares_asof()`.** The arithmetic proves
   the 100 shares; which code ran is not on disk, because `floor_screen.main()` at `ce98258^` reads `cap_m` from an input row and the
   watchlist pricing script was never committed. The sentence was qualified in place before the Q3-Q6 commit.
2. **The spin-off date (2017-09-29) was first written from memory** and then verified against the FY2020 10-K (*"On September 29, 2017,
   NACCO Industries, Inc. ... spun-off the Company"*). It stands.
3. **A Q2 draft said SharkNinja had entered the market "from 2008" and outsold HBB "ten to one in the same categories".** Both were
   memory. Replaced before commit with SharkNinja's filed category revenue ($3,367.1M kitchen, FY2025) against HBB's $606.9M.
4. **A Q2 draft counted Spectrum's competitor list as thirteen.** It is twelve names, Hamilton Beach and private label among them;
   the peer count was corrected to 3 of about 12 plus one channel peer.

### THE BRIEF'S DEFECTS (every brief in this queue has had at least one)
1. **The triage history misdescribes the failure.** *"because the share count did not resolve"*: it **did** resolve, to the wrong
   number, **100 shares** (the pre-spin 2017-06-30 fact), which is why the quotient was 854,301% rather than a missing value.
2. **The pointer to `Screens/floor_screen.py` `shares_outstanding()` "around line 375" is to the FIX, not the cause.** That function
   was added in `ce98258`, the same commit that recorded the zero cap, and it returns None for HBB (it has a 550-day staleness test).
   The code that produced the zero is not on disk.
3. **The brief's hypothesis (a per-class dei cover) was right but half the story**, and "dual-class, family-controlled" conflates two
   things: the per-class tagging is why companyfacts lacks the count; the family control is irrelevant to it.
4. **The priors omitted the event that moved the price**: $36.5M of IEEPA tariff refunds in Q2 2026 (the stock went from $23.87 to
   $31.42 in two sessions and to a two-year high of $34.00). A run that took the twelve months at face value would have reported a
   21.7% yield.
5. **Newell's appliance brands are not separable** (inside Home and Commercial Solutions with Rubbermaid and Yankee Candle), and Spectrum's
   HPC segment includes personal care; Conair is private. The brief listed them as comparables without that limit (it said so honestly:
   *"I have not checked which of these file usable segment numbers"*).
6. **The prior about the Mexican subsidiary was right in substance and dates** (discovered Q1 2020, FY2017-19 restated), but it missed the
   second 2020 material weakness (income taxes) and the $10.0M insurance recovery of 2022, which sits inside the FY2022 operating profit
   and inside the 2022 guidance test.
7. **The prior about the largest customers (Walmart, Amazon) was right**; the one the brief called most likely wrong (that the framework
   would look kindly on a small, low-multiple family company) **was wrong, and the filings refute it at Q2**, before the family or the
   multiple is reached.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business), at Q2** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Hamilton Beach sells a trusted brand of small appliances through buyers who can source the same product from the same
  factories or under their own label, and its own 10-K says the industry *"does not have substantial entry barriers"*; its price line
  follows its cost line in both directions ($58.7M handed back in 2023-24 *"reflecting lower costs"*), its unit rank fell from #1 to #2,
  and it is better run than Spectrum's and Newell's appliance segments but is not the leader, SharkNinja is. **FAIL at Q2.**
  Price $31.64 (2026-09-18) x 13,442,332 shares (cover of 10-Q `0001709164-26-000160`) = $425.3M; five-year owner earnings $27.0-27.3M,
  a 6.4% yield against 5.34% and a ~10% floor, as COMPUTATION - NOT A CLEARANCE.
