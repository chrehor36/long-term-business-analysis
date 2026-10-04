# Company Run — Hub Group, Inc. (HUBG) — 2026-09-25
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
## STEP 0 — THE RATE, AND THE FILING

**Registrant, by CIK 0000940942**: Hub Group, Inc., Delaware (the 8-K covers; EDGAR's
`stateOfIncorporation` field reads IL, which is the business address state, not the charter), fiscal year
to December 31, Class A common on Nasdaq (Global Select), file no. 0-27754. **WAVE 7, name 41 of 218**
(`Screens/_daily/_wave7_order.txt` line 41; `_wave7_done.txt` held 40 lines, the last PG, when this run
started). Name claimed at dispatch, commit `0ec8961`.

**THE STATUS OF THE FILER, read before anything else, because it governs what "the filing" can mean
here.** The EDGAR submissions index (saved as `submissions.json`) shows, since the last 10-Q:

| date | document | accession | what it says |
|---|---|---|---|
| 2026-02-05 | 8-K Items 2.02, **4.02**, 9.01 | `0001193125-26-039396` | Q1-Q3 2025 10-Qs *"materially misstated"* and *"should no longer be relied upon"*; an error *"that resulted in the understatement of purchased transportation costs and accounts payable"*, $77M recorded against accounts payable and purchased transportation in the nine months |
| 2026-03-03 | **NT 10-K** for FY2025 | `0001193125-26-086687` | cannot file by 2026-03-02 |
| 2026-03-24 | 8-K Items 1.01, **3.01**, 7.01 | `0001193125-26-121851` | Nasdaq deficiency (10-K); credit agreement *"First Amendment to Credit Agreement and Waiver"* |
| 2026-05-12 | 8-K Item **4.02** | `0001193125-26-218141` | **the audited FY2024 and FY2023 statements** *"were in each case materially misstated and should no longer be relied upon"* |
| 2026-05-12 | **NT 10-Q** Q1 2026 | `0001193125-26-218159` | |
| 2026-05-21 | 8-K Items **3.01**, 7.01 | `0001193125-26-234605` | Nasdaq deficiency (Q1 10-Q) |
| 2026-06-02 | 8-K Items 5.02, 7.01 | `0001193125-26-253759` | CFO Kevin Beth and COO Brian Meents *"have departed"*; interim CFO by consulting agreement |
| 2026-08-11 | **NT 10-Q** Q2 2026 | `0001193125-26-343399` | |
| 2026-08-24 | 8-K Items **3.01**, 7.01 | `0001193125-26-363681` | Nasdaq deficiency (Q2 10-Q) |
| 2026-09-15 | 8-K Items 1.01, 2.02, 5.02, 7.01 | `0001193125-26-391228` | preliminary H1 2026; *"anticipate reporting an operating loss for the first half of 2026 before the impact of one-time charges"*; filings now expected *"in the fourth quarter of 2026"*; David Yeager (73) back as CEO; credit agreement third amendment |
| 2026-09-17 | 8-K Items **3.01**, 7.01 | `0001193125-26-394408` | **Nasdaq Staff Delisting Determination** received 2026-09-16; the company intends to appeal |

**So on 2026-09-25 there is no reliable filed financial statement for any period after 2022-12-31.** The
FY2025 10-K has not been filed; the FY2024 and FY2023 audited statements and the three 2025 10-Qs are
withdrawn by the registrant under Item 4.02; no 10-Q exists for 2026; no 2026 proxy has been filed (the
last DEF 14A is 2025-04-03, `0001140361-25-012045`). **The newest statements the company still stands
behind are in the FY2022 10-K.** This is recorded here, at Step 0, because the template sends a run with
no obtainable filing to UNRESEARCHED; it is not the verdict of Step 0, because the filings that exist
were obtained and read, and the question is what each can carry. Each gate below says which years it
rests on.

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.47** % · date **09/24/2026** (the newest row on the curve at the time of the run) · source
  (issuing authority) **US Treasury daily par yield curve, 30 Yr**, `home.treasury.gov`
  daily-treasury-rates.csv for 2026, struck fresh by this run and saved raw as
  `Test Runs/_research 2026-09-25 HUBG/treasury_2026.csv`; `tools/sources.py` returned the same row.
  **FRED not used.** Neighbouring rows: 5.40 (09/23).
- FX if the quote and the earnings differ in currency: **not required.** The earnings are dollars:
  the 2024 10-K describes a North American business, and the one foreign piece, the controlling stake in
  EASO (Mexico) bought in October 2024, had 608 of 6,604 employees at 2025-09-30 (Q3 2025 10-Q). USD
  sovereign.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2024, filed 2025-02-25, `0000950170-25-026866`** (`hubg-20241231.htm`): Items 1, 1A, 5,
    7, the four statements and notes. **Its financial statements are withdrawn (Item 4.02 of
    2026-05-12); its business description, risk factors and share terms are not financial statements
    and are used for those.**
  - **10-K FY2022, filed 2023-02-24, `0000950170-23-004358`** (`hubg-20221231.htm`): statements,
    MD&A, notes. **The newest statements not withdrawn.**
  - 10-K FY2023 (`0000950170-24-021432`, withdrawn statements), FY2019 (`0001564590-20-007787`),
    FY2016 (`0001564590-17-002435`), FY2013 (`0001193125-14-065229`), FY2010 (`0001193125-11-045282`)
    for the long series.
  - 10-Q for 2025-09-30, filed 2025-11-05, `0001193125-25-266623` (withdrawn statements; cover and
    acquisition text used).
  - Every 8-K, NT 10-K and NT 10-Q in the table above, with exhibits; the 8-Ks of 2025-06-26
    (`0001171843-25-004144`, the $450M revolver), 2025-10-03, 2024-01-11 and 2023-02-28 (bylaw
    amendment separating Chairman and CEO); **DEF 14A 2025-04-03, `0001140361-25-012045`.**
- figure cross-checked against the filed statement (say which): **FY2022 net cash provided by
  operating activities $458,163K**, read in the Consolidated Statements of Cash Flows of the FY2022 10-K
  (`0000950170-23-004358`), equal to the companyfacts value under all three accessions that carry it
  (2023, 2024, 2025 filings). **And FY2024's $194,419K**, read in the FY2024 statement and rebuilt from
  its own lines (104,043 + 192,562 + 0 − 13,814 + 19,157 − 1,273 = 300,675 of earnings-side cash, less
  working capital (106,256) = **194,419**), ties to the dollar; it is a withdrawn figure and is used
  only as a withdrawn figure.
- *If the filing could not be obtained → UNRESEARCHED.* **The rung that is missing is not EDGAR's: the
  FY2025 10-K and the restated FY2023-24 statements do not exist yet. Failure is at the registrant.**

**The quote and the count** (used nowhere before Q5, recorded here so every gate shares one set):
- Price **$30.03**, Nasdaq close **2026-09-24** (Yahoo chart endpoint, **aggregator, flagged**, raw
  response `price_raw.json`); intraday 2026-09-25 $30.285. The quote was $39.98 on 2026-08-27 and has
  fallen 25% through the delisting notices.
- Shares **61,153,510 = 60,578,607 Class A + 574,903 Class B**, from the **cover of the 10-Q for
  2025-09-30, filed 2025-11-05, accession `0001193125-25-266623`**: *"On October 29, 2025, the registrant
  had 60,578,607 outstanding shares of Class A common stock ... and 574,903 outstanding shares of Class B
  common stock"*. `cover_shares.py` agrees and refuses to sum. **Summing is licensed by the charter as
  the 10-K reports it**: *"The rights of holders of Class A Common Stock and Class B Common Stock are
  identical, except each share of Class B Common Stock entitles its holder to approximately 84 votes"*,
  and *"any cash dividends must be paid equally on each outstanding share"*. Economically one class;
  voting is not (Q3). **It is the latest count any filing carries**: no periodic report since, and the
  8-K covers carry none. Eleven months stale; the 2025 release reports $14M of buybacks for the year.
- Cap **$1,836.4M** (61,153,510 × $30.03). The screen's $2,956M was struck at about $48.
- **Deals**: the screen's `deal_note` (two Item 1.01 8-Ks since 2025-02-25) is **confirmed as credit,
  not deals**: 2025-06-26 is the $450M revolving credit agreement with Bank of Montreal maturing
  2030-06-20; 2026-03-24 is the *"First Amendment to Credit Agreement and Waiver"* after the 4.02. A third
  arrived after the screen: 2026-09-15, the *"Third Amendment to Credit Agreement"* (deadline for the
  audited statements moved to 2026-11-30; restatement costs added back to covenant EBITDA). **A second
  amendment is implied by the numbering and no 8-K for it was found.** No merger agreement, no tender,
  no 13D: **HUBG is not a target and the quote is not a spread.** Buy-side deals with no 8-K item, found
  in the 10-K and 10-Q text: EASO (controlling interest, October 2024), Forward Air Final Mile
  (2023-12-20), TAGG (2022-08-22), and the Marten Intermodal container assets (closed 2025-09-30, $53M of
  containers per the Q3 2025 10-Q).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** Hub sells a shipper a door-to-door move
  of a 53-foot container and buys almost all of it from someone else. For intermodal (57% of 2024
  revenue with dedicated trucking, the ITS segment), it rents the long haul from a railroad under a
  multi-year rate contract, supplies the box (about 50,000 owned dry containers and 900 refrigerated at
  2024-12-31), and trucks the two ends ("drayage", 73% on its own 2,300 tractors and 3,200 drivers plus
  500 owner-operators). Its margin is what the shipper pays less what the railroad, the drayage and the
  box cost. The Logistics segment is the same arithmetic with trucks: brokerage (buy a truckload from a
  carrier, resell it), managed transportation (run a customer's freight buying for a fee), consolidation
  and fulfilment in about 7 million square feet, and final-mile delivery of appliances through about
  540 contractors. **Purchased transportation and warehousing was 74% of 2024 revenue, 75% of 2023, 76%
  of 2022** (FY2024 10-K, Item 1A). What is left pays the people, the equipment and the offices;
  consolidated operating income was 2-8% of revenue across the reliable years (Q2).
- **The scarce input this business controls:** access to rail capacity at contracted rates, plus the
  container fleet that rides on it. **The 10-K says how scarce it is:** *"We primarily rely on
  contractual relationships with two railroads"*, and *"To date, our primary railroad providers have
  chosen to rely on us and other intermodal providers to market their intermodal services rather than
  fully developing their own marketing capabilities. If one or more of the major railroads reduced
  their dependence on us or decreased the capacity that they made available to us, including by
  servicing additional intermodal marketing companies, the volume of intermodal shipments we arrange
  would likely decline"*. The input is controlled by the railroads; Hub holds a contract to it. (The
  railroads have changed: Union Pacific and Norfolk Southern in the FY2010, FY2016 and FY2019 10-Ks;
  *"two railroads"*, unnamed, in the FY2024 10-K.)
- **Will the fundamentals look broadly the same in ten years?** Yes for the mechanism: the company has
  done this since 1971, and containers on rail between trucks is a stable way to move freight over 750
  miles. The mix around it has moved (acquired logistics lines, TAGG 2022, Forward Air Final Mile 2023,
  EASO 2024, Marten Intermodal containers 2025), and that is a question for Q2 and Q4, not for whether
  the money is understandable.
- **What Q1 does NOT claim.** Understanding how the business makes money is not knowing how much it
  made. **The registrant itself does not yet know how much it made in 2023, 2024 or 2025** (Item 4.02
  twice; *"certain transactions that were prematurely or incorrectly recognized or not adequately
  supported"*). That is a question about the level of earnings, which Q4 owns and which the reliable
  record up to 2022 can partly answer; it is not a failure to understand the mechanism. **[E4-46]'s
  test**: this is not a business that needs months of study; it is a business whose last three years of
  numbers are unfiled.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  The mechanism is simple and stable in character **[E3-31]**, the scarce input is named from the
  company's own risk factor, and nothing in this gate rests on a withdrawn number.
## Q2 — IS IT A FRANCHISE? **[E3-03]**
*Written 2026-09-25 (night) by the resume session, after the 13:46 cycle was killed at the weekly limit with
Step 0 and Q1 on disk. Step 0 and Q1 are not edited.*

**The rule, from the ledger row** (E3-03, 1991 letter): *"An economic franchise arises from a product or service
that: (1) is needed or desired; (2) is thought by its customers to have no close substitute and; (3) is not subject
to price regulation. The existence of all three conditions will be demonstrated by a company's ability to regularly
price its product or service aggressively and thereby to earn high rates of return on capital."* **The commodity end
has its own row, [E2-58]** (1982 letter): *"persistent over-capacity without administered prices (or costs) equals
poor profitability"*, with one exception, *"a cost advantage that is both wide and sustainable"*.

**WHICH YEARS THIS GATE RESTS ON.** The registrant's own words about competition, price and the railroads come from
Items 1 and 1A of the 10-Ks for FY2010, FY2013, FY2016, FY2019, FY2022, FY2023 and FY2024; those are descriptions,
not financial statements, and Item 4.02 withdraws none of them. **Every margin and return below for Hub is from
statements the registrant still stands behind, FY2009-FY2022** (the FY2022 10-K, `0000950170-23-004358`, and the
earlier 10-Ks); FY2023-FY2024 figures appear only in a column marked WITHDRAWN and carry no weight. **What the
withdrawal can and cannot do to this gate**: the one error quantified so far (Q1-Q3 2025) *"resulted in the
understatement of purchased transportation costs and accounts payable"*, and the FY2023-24 error is *"certain
transactions that were prematurely or incorrectly recognized or not adequately supported"*. Neither describes a
franchise hidden by the books; the restatement cannot put a higher margin into FY2009-FY2022, on which the verdict
rests.

- Needed or desired [x] · no close substitute [ ] **refuted by the registrant, below** · not price-regulated [x]
  (DOT broker and motor-carrier licences, FMC licence as an ocean intermediary; *"compliance with these regulations
  and licensing requirements has not had a material adverse effect on our capital expenditures, earnings or
  competitive position"*, FY2024 10-K; no rate is administered)
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** Not the ground. The
  perimeter close (UNKNOWABLE) is for a name that passes [E3-03] first **[E4-08]**; this one does not.

### THE REGISTRANT'S OWN WORDS ABOUT SUBSTITUTES AND PRICE
- **The same sentence for fifteen years.** FY2010 10-K (`0001193125-11-045282`): *"The transportation services
  industry is highly competitive. We compete against other IMCs, as well as logistics companies, third party brokers,
  trucking companies and railroads that market their own intermodal services. Several larger trucking companies have
  entered into agreements with railroads to market intermodal services nationwide. Competition is based primarily on
  freight rates, quality of service, reliability, transit time and scope of operations."* The FY2013, FY2016 and
  FY2019 10-Ks repeat it; FY2022 (`0000950170-23-004358`) and FY2024 (`0000950170-25-026866`): *"Competition is based
  primarily on rates charged for services provided, quality of service, reliability, transit time and scope of
  operations."*
- **How customers buy**, FY2022 10-K risk factor: *"many customers periodically accept proposals from multiple
  carriers for their shipping needs, and this process may depress rates or result in the loss of some of our
  business to competitors"*; *"our competitors may periodically reduce their prices to gain business, especially
  during times of weak economic conditions, which may limit our ability to maintain or increase prices"*;
  *"customers may choose to provide for themselves the services that we now provide"*; *"we compete with many other
  transportation and logistics service providers, some of which have greater capital resources or lower cost
  structures than us"*. A shipper that re-bids its lanes among several carriers does not think there is no close
  substitute.
- **Who holds the scarce input** (Q1 named it): FY2022 10-K, *"We primarily rely on contractual relationships with
  two railroads"*; *"To date, our primary railroad providers have chosen to rely on us and other intermodal
  competitors to market their intermodal services rather than fully developing their own marketing capabilities"*.
  The FY2016 10-K adds: *"the railroads are relatively free to adjust shipping rates up or down as market conditions
  permit"*. The access is on the railroads' terms and is shared with *"other intermodal competitors"*.
- **Where the margin sits**, FY2022 10-K: *"Transportation and warehouse costs represented 83% of our consolidated
  revenue in 2022, 86% in 2021 and 88% in 2020"*, and *"Any inability to pass cost increases to our customers is
  likely to have a significant adverse effect on our gross margin and operating income and cash flows."*

### THE PRICE SERIES, IN THE REGISTRANT'S WORDS [E2-44, E4-55]
| year | intermodal price, as the MD&A states it | source |
|---|---|---|
| 2009 | *"a 5% decrease in volume, a 3% price decrease"* | 10-K FY2010 |
| 2010 | volume +19%; *"Pricing was flat year-over-year."* | 10-K FY2010 |
| 2012 | loads +10%, *"an increase for price and fuel"* | 10-K FY2013 |
| 2013 | loads +4%; *"Price was up, but was offset by the impact of lower fuel surcharges."* | 10-K FY2013 |
| 2015, 2016 | volume +3%, +2%; *"price and mix combined were also up"*, revenue flat | 10-K FY2016 |
| 2019 | *"a 7.2% decrease in volume and lower fuel revenue, partially offset by improved pricing"* | 10-K FY2019 |
| 2022 | *"a 31% increase in intermodal revenue per load"* | 10-K FY2022 |
| 2023 (WITHDRAWN) | *"a 14% decrease in intermodal volume due to low transportation demand and an oversupply of truckload carrier capacity, a 14% decrease in intermodal revenue per load"* | 10-K FY2024 |
| 2024 (WITHDRAWN) | *"a 15% decline in intermodal revenue per load (primarily due to lower prices ...)"* | 10-K FY2024 |

Price falls in 2009 with the recession, holds flat through the 2010 volume recovery, rises with the tight truck
market of 2018-2022, and (in the withdrawn years) falls 14% and 15% into *"an oversupply of truckload carrier
capacity"*. **That is [E2-58]'s mechanism: the price is set by the supply of trucks, not by Hub.** The one entry
that reads the other way, 2019's *"improved pricing"* against volume −7.2%, is answered in the strongest-evidence
section below.

### THE COMPETITOR ROW — required [E3-28]
*Two metrics, same window, same definition for every company. (a) GAAP operating income over revenue; (b) GAAP
operating income over average capital, where capital is net tangible operating assets plus goodwill and
intangibles (the price paid for acquisitions put back). Script `peers/q2_row.py` and `peers/q2_gw.py`, outputs
`q2_row_out.txt` and `q2_gw_out.txt`, re-derived tonight from the companyfacts JSON on disk (the uncommitted
`hubg_row.py` of 18:58 was read, its functions reused, and one revenue tag added so that JBHT's 2018+ revenue
resolves). Peers from XBRL (transcription, flagged); **Hub cross-checked to the filed statements: operating income
$474,721K (2022) and $238,457K (2021), FY2022 10-K; $152,420K (2019), FY2019 10-K `0001564590-20-007787`; all equal
the XBRL values.** Hub is read only from filings made on or before 2023-02-28.*

| Company | operating margin, FY2013-2020 | FY2021, FY2022 | mean FY2013-22 | op. income / avg capital incl. goodwill | source |
|---|---|---|---|---|---|
| **Hub Group** | **3.4, 2.3, 3.3, 3.5, 2.3, 3.4, 4.2, 3.0** | **5.6, 8.9** | **4.0%** | **18.4% (2013), 11.8, 15.3, 11.8, 7.0, 9.4, 10.8, 7.3 (2020); 15.0, 27.0** | 10-Ks, filed statements (XBRL cross-checked) |
| Hub, WITHDRAWN | | 2023 5.1, 2024 3.6 | | | 10-Ks FY2023-24, **not relied upon** |
| **J.B. Hunt** (JBHT) | 10.3, 10.2, 11.6, 11.0, 8.7, 7.9, 8.0, 7.4 | 8.6, 9.0 | 9.3% | 26.2, 24.3, 24.1, 22.7, 18.4, 18.1, 17.5, 16.0; 21.8, 23.7 | XBRL, flagged |
| **Schneider** (SNDR) | (from 2016) 7.2, 6.4, 7.6, 4.4, 6.3 | 9.5, 9.1 | 7.2% (7 yrs) | NTOA basis 8.3-21.3% | XBRL, flagged |
| **Knight-Swift** (KNX) | 8.7, 8.6, 15.0, 13.3, 8.3, 10.6, 8.8, 12.1 (2013-2016 mix the Swift and Knight histories under one CIK; revenue $4.1bn in 2014 and $1.2bn in 2015; flagged) | 16.1, 14.7 | 11.6% | NTOA basis 8.8-27.6% | XBRL, flagged |
| **Landstar** (LSTR) | 6.6, 7.0, 7.3, 7.0, 6.7, 7.2, 7.3, 6.1 | 7.7, 7.7 | 7.1% | NTOA basis 46.8-79.5% | XBRL, flagged |
| **C.H. Robinson** (CHRW) | 5.4, 5.6, 6.4, 6.4, 5.2, 5.5, 5.2, 4.2 | 4.7, 5.1 | 5.3% | NTOA basis 57.2-97.2% | XBRL, flagged |
| **Werner** (WERN) | 6.9, 7.5, 9.6, 6.3, 6.8, 9.1, 9.2, 9.6 | 11.3, 9.8 | 8.6% | NTOA basis 8.6-15.4% | XBRL, flagged |
| **ArcBest** (ARCB) | 0.8, 2.7, 2.8, 1.3, 2.2, 3.5, 2.1, 3.3 | 7.4, 7.8 | 3.4% | NTOA basis 4.3-46.9% | XBRL, flagged |
| **Forward Air** (FWRD) | 12.9, 12.3, 8.5, 5.8, 9.3, 10.3, 9.3, 5.8 | 10.6, 14.7 | 10.0% | NTOA basis 19.6-50.1% | XBRL, flagged |
| **RXO**, **GXO** | spun 2022 / 2021 | RXO 4.1, 2.6; GXO 1.9, 2.7 | short | | XBRL, flagged |

**The intermodal segment against the intermodal segment**, the nearest like-for-like: **J.B. Hunt's JBI segment**
(segment tables of the JBHT 10-Ks FY2019 `0001437749-20-004119`, FY2022 `0001437749-23-004530`, FY2024
`0001437749-25-004736`, read tonight): operating income over segment revenue **10.0% (2017), 8.5% (2018, after a
$152.3M arbitration charge), 9.4%, 9.2%, 11.1%, 11.4% (2022), 9.2%, 7.2% (2024)**. **Hub's ITS segment: 10.5% in
2022** (Hub first reported the ITS segment after the FY2022 10-K, which says the realignment was still being evaluated; the 2022 figure is a recast comparative printed in the FY2024 10-K, a withdrawn document, and is used here only because it is the one reading that favours Hub),
then **4.3% (2023) and 2.5% (2024), both WITHDRAWN**. Before 2022 Hub reported no intermodal segment margin. **Scale
of the fleet on the rail**: Hub *"owned approximately 38,000 53-foot containers"* at 2019-12-31 (FY2019 10-K); JBI
*"operates 96,743 pieces of company-owned trailing equipment systemwide"* at the same date, with its own chassis,
and 122,272 at 2024-12-31.

- **Peers named: 10 filers** (JBHT, SNDR, KNX, LSTR, CHRW, WERN, ARCB, FWRD, RXO, GXO) **of the industry's real
  competitors, which the registrant describes as *"intermodal providers, logistics companies, third-party brokers,
  trucking carriers, transportation management providers, warehousing providers and railroads that market their
  own services"*: thousands in brokerage and trucking, and in intermodal marketing a handful of large marketers
  plus the railroads.** Not obtained: the private brokers and IMCs (no filings), the railroads' own retail
  intermodal (not segmented against Hub's product), and the intermodal segments of Schneider and Knight-Swift (the
  segment tables were not read; their consolidated rows are above). **The verdict does not rest on the row**, and the
  row's limit is stated **[E3-61]**: it shows position, not conduct.
- **What the row shows.** On the same metric over the same reliable window Hub earned **2.3-4.2% on revenue in every
  year 2013-2020**, below every peer in the row in every year except ArcBest, an LTL carrier (0.8-3.5%), and **4.0% over the decade against
  J.B. Hunt's 9.3%**. On capital including the goodwill it paid for, Hub's return **fell from 18-22% (2010-2013) to
  7-11% (2017-2020)** as acquisitions were added (goodwill and intangibles $279M in 2013, $673M in 2020), while J.B.
  Hunt's stayed at 16-26%. The two years that break Hub's pattern, 2021 and 2022, are the years every carrier in the
  row posted its record.
- **[E3-46]**, returns on capital over time: pretax 7.0-18.4% on capital including goodwill across 2013-2020, the
  best years at the start of the window; the 27.0% of 2022 is one year of the freight boom. Not *"very high returns on
  capital employed over time"*.
- **[E2-44] characteristic (1)**, raising prices *"even when product demand is flat and capacity is not fully
  utilized"*: fails on the registrant's series. Price fell 3% in 2009, was *"flat"* in 2010 with volume up 19%, and
  the registrant's own risk factor says competitors *"may periodically reduce their prices ... which may limit our
  ability to maintain or increase prices"*. Characteristic (2), growth with little added capital: the containers,
  tractors and acquisitions grew capital from $347M (2010) to $1,862M (2022) for operating income that went from
  $70M to $106M (2020) before the boom.
- **Untapped pricing power [E3-33, E5-28]**: no. Claiming it is claiming near-monopoly in a market the registrant
  calls *"highly competitive and cyclical"*, bought by re-bid.
- **The prayer session [E4-37]**: the registrant's sentence, *"Any inability to pass cost increases to our customers
  is likely to have a significant adverse effect"*, with 83-88% of revenue passed to railroads, truckers and
  warehouses.
- **The attacker's test [E2-45]**: the attacker exists and is larger. J.B. Hunt held about 2.5 times Hub's owned trailing equipment on
  the rail at 2019-12-31 (96,743 pieces against about 38,000 containers), its own chassis, and agreements *"with most major North American rail carriers"*; the registrant
  itself records that *"Several larger trucking companies have entered into agreements with railroads to market
  intermodal services nationwide"*, and that the railroads could market their own.
- **[E3-62]'s second step**: Hub's own drayage rose to *"78% in 2023 as compared to 55% in the prior year"*
  (withdrawn document), a cost saving; in the same two years ITS operating income fell from 10.5% of revenue to 2.5%.
  The saving went to the shipper, as the commodity class predicts.
- **Direction [E4-32]**: margin 3.4% (2013) to 3.0% (2020) and return on capital down by half across the reliable
  decade before the boom; after it, the registrant's own unrestated figures went 8.9% (2022) to 5.1% and 3.6%, and it
  now anticipates *"an operating loss for the first half of 2026 before the impact of one-time charges"* (8-K
  2026-09-15). Not widening.
- **Which cause of success [E4-36]**: 2021-2022 is the freight wave, a surfing run **[E3-51]**; the wave was in the
  truck market, and every peer rode it.
- Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: **flat to eroding before 2021; a boom and a fall
  since; the fall is in statements the registrant has withdrawn, and the first half of 2026 is a loss in its own
  preliminary words.**

### THE STRONGEST EVIDENCE AGAINST THIS VERDICT, stated as its holders would state it [E4-51, E3-47, E4-26]
1. **2022, segment against segment, Hub's ITS earned 10.5% of revenue against JBI's 11.4%.** At its best Hub ran
   intermodal almost as well as the leader.
2. **2019: *"improved pricing"* while volume fell 7.2%.** That is [E2-44]'s test passed in one year: price up in a
   falling market.
3. **The capital-light return**: on net tangible operating assets alone (goodwill left out) Hub earned 10-50% pretax
   in 2013-2022 (`q2_row_out.txt`), because railroads own the track and third parties do most of the trucking.
4. **Fifty-five years in the trade** and preferred access to two railroads, which *"have chosen to rely on us"*.

**Answered, not dismissed.** (1) is the peak year of the freight boom, the only year Hub reported the segment
before the withdrawn ones; JBI earned 7.2-11.4% in every year 2017-2024, and in the next two years Hub's figure, on
its own now-disowned books, fell to 4.3% and 2.5%. One year at parity at the top of a wave is the wave. (2) is real
and is one year, and it is not [E2-44]'s test: that test asks for price *"without fear of significant loss of either
market share or unit volume"*, and the 2019 price came with volume down 7.2%, price held by giving up loads; the
10-K credits the margin to *"improved prices and network optimization"* against *"rail cost increases"*. The next
soft market (2023-24, withdrawn figures) shows the price falling 14% and 15%. (3) is what an asset-light intermediary looks
like when its acquisitions' cost is left out; put the goodwill back and the return is 7-11% before the boom, below
the asset-heavy leader. And a high return on little capital earned at a 2-4% margin on re-bid freight is [E2-58]'s
commodity with low capital needs, not a franchise: C.H. Robinson shows 57-97% on the same basis without anyone
calling brokerage a franchise. (4) is access held on the railroads' terms, shared with *"other intermodal
competitors"*, which the registrant itself lists as a risk. **[E2-37] applies**: a capable operator in a
price-competed trade is a remarkable operator, not a remarkable business.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — **OUT, on the business.** [E3-03] criterion (2)
  is refuted by the registrant in every 10-K read from FY2010 to FY2024 (*"Competition is based primarily on ...
  rates"*; customers *"periodically accept proposals from multiple carriers"*; competitors *"may periodically reduce
  their prices"*), and the demonstration clause fails on the statements it still stands behind: operating margin
  2.3-4.2% in every year 2013-2020 against J.B. Hunt's 7.4-11.6%, return on capital including goodwill falling from
  18% to 7-11% before the 2021-22 wave, price following the truck market. **The scarce input is the railroads', held
  by contract and shared.** This is [E2-58]'s class without a wide and sustainable cost advantage, and on the row
  the scale advantage belongs to J.B. Hunt, not Hub. **Nothing in the withdrawn years is needed for this verdict, and
  nothing a restatement can do reaches FY2009-FY2022.** The file closes here. Q3-Q6 are not opened as gates.

*"Can I name the document that would resolve this?"* Not asked: the verdict is OUT, not a non-IN pending evidence.
Recorded: the restated FY2023-FY2024 statements and the FY2025 10-K (the credit agreement now requires the audited
statements by 2026-11-30, 8-K 2026-09-15) will show how far the fall ran; they cannot turn a re-bid, price-competed
service into one its customers think has no close substitute.

---
## MATERIAL BENEATH THE CLOSE — recorded, not governing

*The file closed at Q2, OUT on the business. What follows is recorded the way the WS, NATH, CAH, MHH and ICFI runs
recorded theirs: no verdict box is ticked for Q3-Q6, nothing here reopens Q2, and nothing here is a clearance. It
is written because the filer's status (two Item 4.02 notices, a delisting determination) is the first thing the
next reader of this name will ask about.*

### Q3 prompts (no verdict)
- **Weight case, had the gate opened: a GATE, on daily execution.** A re-bid freight business priced against the
  truck market every contract season is have-to-be-smart-every-day **[E3-38]**; the registrant's own 2026 release
  shows the lag: *"higher fuel, rail and drayage costs incurred prior to rate increases implemented beginning in the
  third quarter of 2026"* (EX-99.1 to 8-K 2026-09-15). **Leverage is not the determinant**: debt about $198M and cash
  about $132M at 2026-06-30, *"net debt of approximately $66 million"* (same release, preliminary and unaudited),
  and a further *"$75 million under its $450 million revolving credit facility"* borrowed in August 2026 **[E3-29]**.
  **Control [E1-16]**: 574,903 Class B shares at *"approximately 84 votes"* each carry about 48.3M votes against
  60,578,607 Class A votes, about **44% of the vote** (my arithmetic, cover counts of 2025-10-29); the CEO is again
  David Yeager, 73, *"the father of Mr. Phillip Yeager"*, who *"will continue to serve as President and Vice
  Chairman"*, and *"Matthew Yeager, the son of Mr. David Yeager, is an employee"* (8-K 2026-09-15). A buyer of Class
  A is a minority beside the family.
- **Honesty [E5-16], each matter dated to when it became public.** (1) **2026-02-05**, Item 4.02: the three 2025
  10-Qs *"materially misstated"*, an error *"that resulted in the understatement of purchased transportation costs
  and accounts payable"*. (2) **2026-05-12**, Item 4.02: the audited FY2023 and FY2024 statements *"materially
  misstated"*, after a review that *"identified certain transactions that were prematurely or incorrectly recognized
  or not adequately supported"*; the company *"is continuing to review additional accounting issues"* and *"expects to
  conclude that it did not maintain effective disclosure controls and procedures and internal control over financial
  reporting for each of the years ended December 31, 2024 and 2023"*. (3) **2026-06-02**, the CFO who signed the
  4.02 notice and the COO *"departed"* on 2026-05-27; the 8-K/A of 2026-06-26 files a separation agreement with
  severance (three months' salary, continued vesting), which reads as a departure without cause; no reason is
  stated. (4) **2026-09-17**, the Nasdaq Staff Delisting Determination. **No finding of personal misconduct is in
  any document read**; the audit committee's review has not been published. Had Q3 opened, the verdict could not be
  written before the FY2025 10-K with its restatement note and Item 9A, which the company expects *"in the fourth
  quarter of 2026"*: a named document, so UNRESEARCHED, not IN.
- **[E4-22] first flag, weak accounting, FIRES in its strongest form**: *"seldom just one cockroach in the kitchen"*.
  The first notice (February) found one error in three quarters; the second (May) reached back two audited years;
  the second says more issues are under review.
- **[E4-27], incentives**: the interim CFO's letter agreement pays *"a cash retention bonus of $1,250,000, payable
  after the Company files its Annual Report on Form 10-K for the year ended December 31, 2025"*, conditioned on
  filing *"on or before December 31, 2026"* and on his having *"executed any required representations,
  certifications"*; the fee rises to $175,000 a month from 2026-12-01. Pay tied to the date of the document whose
  accuracy is the whole question. Recorded as a prompt: the certification condition is the counterweight.
- **[E4-29], EBITDA promotion**: not found in the releases read (no "adjusted" measure in the 2026-02-05 release);
  the credit agreement's covenant EBITDA now adds back *"costs and expenses incurred on or prior to December 31, 2026
  in connection with the accounting review and restatement process"* (8-K 2026-09-15), a lender's definition, not a
  promotion.
- **Capital allocation [E5-08], the prompts**: treasury stock bought $75.0M plus **$34.8M *"from related party (Note
  17)"*** in 2022 (FY2022 10-K), $143.8M in 2023 and $68.3M in 2024 (withdrawn statements), at prices above the
  $30.03 of Step 0; whether (2), a material discount to conservative value, held is not assessable while the
  statements that would value it are withdrawn. The related-party purchase note was not read.

### Q4 prompts: owner earnings the corpus's way [E2-23], every window [E4-25]
*OCF − SBC − (c), no net-income proxy. Every input typed from the filed Consolidated Statements of Cash Flows of the
10-Ks FY2010, FY2013, FY2016, FY2019 and FY2022 (the `cf_FY*_flat.txt` extracts of 18:58 were checked against the
filed text on disk tonight: OCF $117,417K, $102,473K, $171,697K, $254,509K, $210,839K, $125,220K, $458,163K,
$252,835K, $174,954K, capex $219,140K and SBC $16,286K and $20,426K each found in the filed 10-K). Script `oe.py`,
output `oe_out.txt`. **FY2023-FY2024 are shown only as WITHDRAWN.** **SBC RESOLVES AND IS NEARLY COMPLETE**: the
cash-flow line resolves in every year; the FY2022 note gives *"Share-based compensation expense for 2022, 2021 and
2020 was $ 20.6 million, $ 20.1 million and $ 17.1 million"* against lines of $20.4M, $20.1M, $17.1M ($0.2M apart in
2022, immaterial); the 401(k) match ($6.7M in 2022) is cash. **(c) is a disclosed guess [E2-09]**: the band runs from
the smaller to the larger of D&A and capex less proceeds from equipment sales. The fleet grew (about 38,000 owned
containers at 2019-12-31, about 50,000 at 2024-12-31), so part of capex is growth and the capex end is conservative;
from FY2019 the cash-flow D&A exceeds net capex in most years. Not [E5-20]'s railroad class: the track is the
railroads'.*

| FY | OCF | SBC | capex net of sales | D&A | OE low | OE high |
|---|---|---|---|---|---|---|
| 2013 | 117.4 | 7.7 | 109.1 | 21.3 | 0.7 | 88.4 |
| 2014 | 98.5 | 8.3 | 118.6 | 29.4 | **−28.3** | 60.9 |
| 2015 | 171.7 | 7.8 | 80.7 | 37.0 | 83.1 | 126.8 |
| 2016 | 102.5 | 8.5 | 105.3 | 44.7 | **−11.4** | 49.3 |
| 2017 | 125.2 | 9.9 | 69.2 | 62.2 | 46.1 | 53.2 |
| 2018 | 210.8 | 13.5 | 188.8 | 83.9 | 8.5 | 113.4 |
| 2019 | 254.5 | 16.3 | 84.8 | 116.9 | 121.3 | 153.4 |
| 2020 | 175.0 | 17.1 | 112.0 | 123.7 | 34.2 | 45.9 |
| 2021 | 252.8 | 20.1 | 87.8 | 130.6 | 102.2 | 145.0 |
| 2022 | 458.2 | 20.4 | 176.2 | 153.7 | 261.5 | 284.0 |
| 2023 WITHDRAWN | 422.2 | 21.3 | 112.4 | 184.4 | 216.4 | 288.5 |
| 2024 WITHDRAWN | 194.4 | 19.2 | 38.7 | 192.6 | −17.3 | 136.6 |

*$M. FY2008-FY2012 are in `oe_out.txt` ($9.4M to $64.8M a year). FY2017-FY2018 OCF includes Mode, sold 2018-08-31
(discontinued operations; the FY2019 10-K says its cash flows *"have been reported ... under operating and investing
activities"*).*

| window | mean owner earnings | yield on $1,836.4M |
|---|---|---|
| 3y FY2020-22 | $132.6M to $158.3M | 7.22-8.62% |
| **5y FY2018-22 (the corpus default [E2-42], newest reliable)** | **$105.6M to $148.3M** | **5.75-8.08%** |
| 5y FY2017-21 | $62.5M to $102.2M | 3.40-5.56% |
| 5y FY2016-20 | $39.8M to $83.0M | 2.17-4.52% |
| 5y FY2013-17 | $18.1M to $75.7M | 0.98-4.12% |
| 10y FY2013-22 | $61.8M to $112.0M | 3.37-6.10% |
| 15y FY2008-22 | $50.3M to $90.1M | 2.74-4.90% |
| 5y FY2020-24, WITHDRAWN years included, for reference only | $119.4M to $180.0M | 6.50-9.80% |

- **Where the bottom sits near or below zero: FY2014, minus $28.3M (negative); FY2016, minus $11.4M (negative);
  FY2013, $0.7M (near zero); FY2018, $8.5M (near zero)**, each a year of container or tractor purchases above D&A.
  **FY2024 (withdrawn) is minus $17.3M at the capex end.**
- **The width is the window, not the band [E4-25]**: the five-year means run from $18.1-75.7M (FY2013-17) to
  $105.6-148.3M (FY2018-22), and the newest reliable window is carried by 2022, the freight-boom year ($261.5-284.0M,
  between a third and a half of the window's sum). **[E4-41]**: a boom year is a windfall to normalise, and the registrant's own words for
  the first half of 2026 are *"an operating loss ... before the impact of one-time charges"*. **The screen's
  `level_shift` 1.92 and "STEP UP - normalize down [E4-41]" are this, read.**
- **The screen's `wc_note` answered**: accounts payable was −$73.9M in the FY2024 statement (38% of its $194.4M OCF),
  in a year whose statements are withdrawn and whose restatement concerns *"accounts payable"*. It bears on nothing
  above, because FY2024 carries no weight.
- **The screen's `acq_note` answered**: acquisitions of $585M sit inside its window (2020 $84.8M, 2021 $122.4M, 2022
  $102.7M, 2023 $260.8M, 2024 $14.6M; $585.3M, the last two from withdrawn statements); owner earnings exclude acquisition cash by construction, and the acquired earnings are
  inside OCF. Numerator and denominator are different companies, as the screen warned.
- **Great, good or gruesome [E4-20]**: on the reliable decade, the good-to-gruesome border: capital including
  goodwill grew from $662M (2013) to $1,514M (2020) while operating income went from $114M to $106M. Recorded, not
  scored.
- **Staying power [E5-11]**: (1) stream: $18-148M a year on five-year means, negative in two reliable years; the
  current half-year is a loss on the company's own preliminary word. (2) liquid assets: about $132M cash at 2026-06-30
  (preliminary). (3) near-term requirements: the credit agreement's deadline for audited statements, **2026-11-30**,
  after three amendments; the Nasdaq hearing on the delisting; restatement costs large enough to be added back to
  covenant EBITDA; the revolver drawn $75M in August 2026. **Leverage [E4-16]**: net debt about $66M, small against the
  business; the risk is the waiver, not the debt.
- **Named death, as a signature only: #11 THE PASS-THROUGH, with #13 THE TENANT as a feature.** The linehaul is rented
  from two railroads that *"rely on us and other intermodal competitors"*, the price follows truck capacity, and the
  2026 release shows the cost arriving before the price. **Not entered in the index's instances column** (file closed
  at Q2, the PAGP, CALM and WS precedent). **No new shape.** The restatement, delisting and covenant deadline are a
  filer's risk, not a way the business dies; had Q4 opened they would have been its question (3) **[E5-11]**.

### COMPUTATION — NOT A CLEARANCE
*No box, no ranking, no entry language.* Price and count from Step 0 (**$30.03**, Nasdaq close 2026-09-24,
aggregator, flagged; **61,153,510 shares**; cap **$1,836.4M**); not re-struck, because Q5 is not opened. On the newest
reliable five-year window, owner earnings of **$105.6M to $148.3M are 5.75-8.08% of the cap**, against the 5.47%
sovereign (US Treasury 30-year par, 09/24/2026, Step 0) and below the ~10% floor **[E4-28]**; on the ten-year window,
$61.8M to $112.0M, **3.37-6.10%**. At the floor with no growth they capitalise to **$1,056M-$1,483M, about $17-24 a
share (five-year), or $618M-$1,120M, about $10-18 a share (ten-year)**, against $30.03 quoted; at the 5.47% sovereign
with no growth, about **$32-44 a share (five-year) and $18-33 (ten-year)**. **Every one of these figures rests on
statements for years that end in 2022**; the company has no reliable filed statement for any later period, and it
anticipates an operating loss for the first half of 2026. **Windage count: ONE** (the conservative end of the (c)
band; no premium in the rate **[E3-42]**). Upside ceiling **[E2-63]**: a 2-9% operating margin intermediary whose
price is set by truck capacity.

### Q6 — reversal conditions, in words (no alert: the file failed on the business)
The Q2 verdict would reopen on **filed evidence that Hub prices independently of the truck market**: several
reliable years in which ITS operating margin holds near J.B. Hunt's JBI segment through a soft freight year, or an
exclusive rail arrangement that the railroads do not also give *"other intermodal competitors"*. **Next dates**: the
credit agreement deadline for audited statements, **2026-11-30**; the FY2025 10-K with restated FY2023-FY2024, which
the company expects *"in the fourth quarter of 2026"*; the Nasdaq Hearings Panel on the appeal.

---
⛔ **Q5 does not open: Q2 is OUT.** The computation above is headed as the protocol requires and carries no box.

## Q5 — not opened. ## Q6 — not opened as a gate (reversal conditions in words above).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; the file closed at Q2. Step 0 and Q1 were
      written by the 13:46 cycle and committed at `dd28674d` after it was killed; this session resumed at Q2 and did
      not edit them)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the 10-K business
      descriptions and risk factors, which Item 4.02 does not withdraw, and on no withdrawn number)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued; beneath the close, Q3 is noted
      as one that would have been UNRESEARCHED on the FY2025 10-K, had it opened)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; the [E4-04] perimeter close
      was considered and refused because [E3-03] is not passed first)
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (Step 0: FY2022 OCF $458,163K
      and FY2024's withdrawn $194,419K rebuilt from its lines; Q2 adds operating income $474,721K, $238,457K and
      $152,420K against the filed statements, each equal to XBRL)
- [x] Owner earnings on a multi-year mean; every window FY2008-FY2022 published with both (c) ends; the negative and
      near-zero years (FY2014, FY2016; FY2013, FY2018) named in dollars and a word; withdrawn years shown apart and
      carrying no weight (beneath the close)
- [x] Competitor row filled (10 filers on the same two metrics over the same reliable window, plus J.B. Hunt's JBI
      segment from three JBHT 10-Ks; private brokers and IMCs, the railroads' retail intermodal and the Schneider and
      Knight-Swift intermodal segments not obtained, stated; the verdict does not rest on the row)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.47%, US Treasury 30-year par,
      09/24/2026, Step 0; not re-struck because Q5 did not open)
- [x] Value stated as a round-number range, not a point estimate (computation only)
- [x] One bar chosen, not both; windage count stated (ONE; no bar applied, Q5 not opened)
- [x] Prices dated; aggregator used for the live quote only and flagged ($30.03, 2026-09-24 close, Step 0; not
      re-struck, Q5 not opened)
- [x] Run committed to git (claim `0ec8961`, Step 0 and Q1 `dd28674d`, Q2 `5300099e`, beneath the close
      `f9f869ad`, this section and the fold after)

**WHICH STATEMENTS EACH GATE RESTS ON** (the brief's requirement): Q1, the 10-K business descriptions and risk
factors FY2010-FY2024, none withdrawn, no financial statement needed. Q2, the same descriptions for the registrant's
words; **for every Hub number, statements for FY2009-FY2022 only, which the registrant still stands behind**; FY2023-24
figures appear only in columns marked WITHDRAWN and the verdict needs none of them. Beneath the close, the same
FY2008-FY2022 statements; FY2023-24 shown apart; the 2026 figures are a furnished, preliminary, unaudited release.

**Brief priors, each tested:**
1. *Step 0 and Q1 written, Q1 IN; resume at Q2* — **confirmed**; both read in full, no error found that needs a
   correction note.
2. *The deal_note's two Item 1.01 8-Ks are credit, not deals* — **confirmed at Step 0**, not re-opened.
3. *wc_note: accounts payable moved 38% of 2024 OCF* — **confirmed and read**: −$73.9M against $194.4M, in a year the
   registrant has withdrawn and whose restatement concerns accounts payable; carries no weight.
4. *level_shift 1.92, "STEP UP - normalize down [E4-41]"* — **confirmed**: the newest reliable five-year window is
   carried by the 2022 freight boom; the reliable decade's means are a third to a half lower.
5. *acq_note: acquisitions $585M inside the window* — **confirmed** ($585.3M, 2020-2024, the last two years from
   withdrawn statements).
6. *spread_caveat: rebuild the width over older windows* — **done**: 3, 5, 10 and 15-year windows, both (c) ends.
7. *The 18:58-18:59 files are unverified* — **re-derived**: `hubg_row.py`'s functions were read and re-run with one
   tag added (`q2_row.py`); its HUBG and peer numbers reproduce; the `cf_FY*_flat.txt` values were each found in the
   filed 10-K text before use.

**Brief errors found:** (1) the brief says the 18:58-18:59 files came from a session *"that never committed"*;
**`peers/hubg_row.py` and `peers/hubg_row_out.txt` are tracked, committed inside `4f5af858` "LDP: write the paper"
(2026-09-25 19:09), an unrelated MBA commit that also carried fifteen daily digests and ACMR research files**: a
crossing of the kind `## THE FOLD` step 6 describes, recorded, not rebased. The `cf_FY*_flat.txt` files are
gitignored by the `*_FY20*.txt` pattern and were never committed. (2) The brief's commit trailer (Opus 5) differs from
the session's attribution instruction (Opus 5.5); the brief's trailer was used, as the WS, NATH and CAH runs recorded.
Neither is verdict-bearing.

**My own errors caught before commit:** (1) my first Q2 draft said Hub's margin was *"below every asset-based peer and
below both large brokers"* in every year 2013-2020; ArcBest was below Hub in several years; corrected to *"every peer
in the row except ArcBest"*. (2) I first gave Schneider's row as starting in 2017; the data start in 2016; corrected.
(3) I first answered the 2019 *"improved pricing"* point by calling 2018-2019 a tight truck market; 2019 was not shown
to be one in any document read; replaced by the text's own answer ([E2-44] asks for price *"without fear of
significant loss of ... unit volume"*, and volume fell 7.2%). (4) I first wrote JBI's range as 7.4-11.4%; the 2024
figure is 7.2%; corrected. (5) I first called Hub's 2022 ITS figure the first year Hub "reported" the segment; it is a
recast comparative printed in a withdrawn 10-K; relabelled. (6) The screen's $585M of acquisitions was first
attributed to 2022-2024; it is 2020-2024; corrected.

**Tooling defects, reported, not patched:**
1. **The screen and `run.py` have no Item 4.02 check.** `oe_bottom_m`, `oe_top_m`, `wc_note`, `level_shift` and the
   growth figure for HUBG are all computed on FY2023-FY2024 statements the registrant withdrew on 2026-05-12, and on
   companyfacts values filed before the withdrawal; nothing in the row says so. A registrant with an 8-K Item 4.02 in
   its submissions index should carry a flag naming the withdrawn periods.
2. **`hubg_row.py`'s revenue tag list misses `RevenueFromContractWithCustomerIncludingAssessedTax`**, so J.B. Hunt's
   2018+ revenue printed "n/f"; worked around in `q2_row.py`, not patched.
3. Knight-Swift's companyfacts series mixes the Swift and Knight histories under one CIK for 2013-2016 (revenue $4.3bn
   in 2014, $1.2bn in 2015); flagged in the row, not a tool defect of ours but a trap for any peer script.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **Hub Group arranges door-to-door intermodal and truck freight on rail capacity it rents from two railroads
  that *"rely on us and other intermodal competitors"*; in every 10-K from FY2010 to FY2024 it says competition *"is
  based primarily on ... rates"*, and its customers *"periodically accept proposals from multiple carriers"*. On the
  statements it still stands behind (FY2009-FY2022) its operating margin was 2.3-4.2% in every year 2013-2020 against
  J.B. Hunt's 7.4-11.6%, and its return on capital including goodwill fell from 18-22% to 7-11% before the 2021-22
  freight wave. [E2-58]'s commodity class, no wide and sustainable cost advantage. Its FY2023-FY2024 statements and
  2025 10-Qs are withdrawn under Item 4.02, the FY2025 10-K is unfiled, and Nasdaq has issued a delisting
  determination; the verdict needs none of the withdrawn years.**
- **PASS/FAIL: FAIL at Q2 (OUT, ON THE BUSINESS).** Price **$30.03** (2026-09-24 close, aggregator, flagged) ×
  **61,153,510 shares** (60,578,607 Class A + 574,903 Class B, 10-Q cover for 2025-09-30, accession
  `0001193125-25-266623`) = cap **$1,836.4M**; sovereign **5.47%** (US Treasury, 09/24/2026). Owner earnings on
  reliable statements: newest five-year window FY2018-22 **$105.6-148.3M (5.75-8.08%)**, ten-year FY2013-22
  $61.8-112.0M (3.37-6.10%); FY2014 and FY2016 negative at the capex end.
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
