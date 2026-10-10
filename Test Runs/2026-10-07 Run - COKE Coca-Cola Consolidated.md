# Company Run — Coca-Cola Consolidated, Inc. (NASDAQ: COKE) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

*Dispatched run under `Screens/_daily/_dispatch_brief.md` (operator rule 10). Analyst: a dispatched session (Claude Opus 5.5).
Run file copied from the template at 2026-10-07 before any fetch; working folder `Test Runs/_research 2026-10-07 COKE/`; raw
filings are kept under its `cache/` subfolder, which `.gitignore` excludes.*

**CONTAMINATION, declared as found (not used):** (1) the dispatching message says earlier run files on this name exist; their
contents, dates and verdicts were not seen. (2) The session's opening context showed the last five commit subjects of the
repository (another company's run, CB, closing OUT at Q7, and a re-run batch naming AVGO, BMI, CB, CHD); none bears on this name.
(3) The session's memory index carried a line about the queue state and a count of "gate-clearers"; no name was in it. Nothing
of these is used below. (4) After the closing commit, `git log` printed
the subjects of three commits by other analysts running CL and CSL the same morning (Q3 and Q4 lines of their runs); seen after
this file's box was written, and not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $194.61 (close 2026-10-06; Yahoo Finance chart feed, an aggregator, flagged per operator rule 5; `tools/run.py`
  printed the same close from its own aggregator). This is the post-split price: a 10-for-1 forward split of both classes took
  effect on the market on 2025-05-27 (10-K FY2025, Liquidity, accession 0001628280-26-009057; announced by 8-K 2025-03-04,
  accession 0000317540-25-000030).
- **Shares by class** from the latest filing's cover: Common Stock 56,517,334; Class B Common Stock 10,046,960; as of
  2026-07-24 (10-Q for the quarter to 2026-07-03, filed 2026-08-05, accession `0001628280-26-053370`;
  `python Screens/cover_shares.py COKE`). Check against issued less treasury: the FY2025 balance sheet shows 56,517,334 Common and
  10,046,960 Class B issued and no treasury shares (all treasury shares were retired in Q3 2025; the 18,835,460 shares bought
  from The Coca-Cola Company were retired on 2025-11-07), and the 10-Q says no shares were repurchased in Q2 2026 with the
  remaining authorization unchanged at $136.3 million since 2025-12-31, so the count holds. No 8-K after the 10-Q changes it
  (8-K of 2026-08-05 is the earnings release, items 2.02 and 9.01). **Charter note:** the two classes have participated equally
  in every dividend for more than 30 years (10-K FY2025, Liquidity); Class B carries the larger vote (the 10,043,940 Class B
  shares Mr. Harrison controls are about 78% of the vote) and is exchangeable with Common one for one (Mr. Harrison's right to
  exchange 2,923,860 Common for Class B, 10-K FY2025, Item 1A). The classes are treated as economically equivalent and summed:
  **66,564,294 shares**. (`tools/run.py` used a stale XBRL weighted average of 94.17M split-adjusted shares and a cap of
  $18.33B; both are wrong after the 2025 repurchase and are not used.)
- **Market cap:** 66,564,294 x $194.61 = **$12,954M**.
- **Sovereign for the earnings currency:** USD, **5.64%**, US Treasury daily par yield curve, 30-year, 2026-10-06
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-18, accession 0001628280-26-009057); 10-Q Q2 2026 (filed
  2026-08-05, 0001628280-26-053370); DEF 14A 2026 (filed 2026-03-23, 0001628280-26-020505); 8-K 2025-11-07 (repurchase from The
  Coca-Cola Company, 0001628280-25-050682); 8-K 2025-12-08 (term loans, 0001628280-25-055830); 8-K 2024-05-06
  (0000317540-24-000030); 8-K 2025-03-04 (split, 0000317540-25-000030); the 10-Ks for the span: FY2014 0001193125-15-091165, FY2015
  0001564590-16-015048, FY2016 0001564590-17-004316, FY2017 0001564590-18-003845, FY2018 0001564590-19-005000, FY2019
  0001564590-20-006432, FY2020 0000317540-21-000006, FY2021 0000317540-22-000009, FY2022 0000317540-23-000009, FY2023
  0000317540-24-000009, FY2024 0000317540-25-000025. **One figure cross-checked against the filed statement:** net cash provided
  by operating activities FY2025 $931,904 thousand on the filed cash-flow statement (10-K FY2025, page 44) equals the $931.9M
  `tools/run.py` transcribed from XBRL; FY2024 $876,357 thousand and FY2023 $810,690 thousand also agree.
- `python tools/run.py COKE` arithmetic lines only (Part VII): OCF FY2023 to FY2025 $810.7M, $876.4M, $931.9M; capital spending
  $282.3M, $371.0M, $312.3M; depreciation of PP&E $153.5M, $170.3M, $195.1M. The tool found no stock pay in XBRL after 2021
  (read below at Q4: the filer reports none). The tool's owner-earnings lines leave out the sub-bottling payments to The
  Coca-Cola Company, which the filer puts in financing; they are a real operating cost and are deducted at Q4. The tool's share
  basis, cap, yield and "growth the price assumes" rest on the stale share count and are not used. The FY2025 balance sheet
  shows total equity of **minus $739.7M** (the repurchase was charged to retained earnings).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what this bottler's territories will earn, not what the quotation does **[M1997-109]**;
the stock has risen from the $127 a share paid to The Coca-Cola Company in November 2025 ($2.4B for 18,835,460 shares, 10-K
FY2025, Liquidity) to $194.61, and appreciation "is never a reason to buy it" **[L2013-007]**. No macro enters: the inflation
of 2021 to 2023 is read only as a property of the business, its freedom to price **[M2011-054]**, **[M2015-016]**. Who is paid to
tell you: the company features an "adjusted" net income in its 10-K **[L2016-006]** (weighed at Q4). The analyst's habits: look
for what is wrong in things **[M2025-013]** and destroy the previous idea **[M2016-054]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) from FY2009 to FY2019 the company earned an operating margin of 1.3% to 6.5% (XBRL OperatingIncomeLoss over
revenue, filed 10-Ks), the margin of an ordinary business; the margin of about 13% is a fact of FY2022 to FY2025 only. (2) The
Coca-Cola Company, which sets the concentrate price and knows the bottler's economics best, sold its entire 19% holding to the
company in November 2025. (3) The repurchase was paid largely with $2.35B of new borrowing and left equity negative. (4) Walmart
and Kroger take 29% of net sales (10-K FY2025, Item 1). (5) The incidence-based concentrate price moves with the bottler's own
selling price (10-K FY2025, Item 1), so part of every price rise goes to The Coca-Cola Company.

## THE STANDING RULE
Owning this stock puts the buyer at risk of ruin only through the buyer's own borrowing or sizing; bought with no borrowed money
it does not **[L2014-005]**, **[M2012-081]**. The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; "the first question is, can I understand it?" **[M1995-051]**.
  The product is not the question; the economic dynamics are **[M2011-014]**.
- **What the business is, from the filing.** The largest Coca-Cola bottler in the United States: it makes, sells and delivers
  finished beverages in territories spanning 14 states and the District of Columbia, serving about 60 million consumers,
  through 10 plants and 60 distribution centres; about 85% of bottle/can volume is The Coca-Cola Company's brands and about 15%
  is Monster, Dr Pepper and others (10-K FY2025, Item 1, accession 0001628280-26-009057). The rights rest on the comprehensive
  beverage agreement (CBA) of 2017 with The Coca-Cola Company and CCR: exclusive rights in the territories, "a term of ten
  years" renewable by the company "indefinitely for successive additional terms of ten years", terminable by The Coca-Cola
  Company only on an uncured default, in which case The Coca-Cola Company must buy the business; conditions are minimum capital
  spending and a volume-per-capita change rate not less than one standard deviation below the median U.S. Coca-Cola bottler
  (10-K FY2017, Item 1, accession 0001564590-18-003845). Concentrate is priced under an incidence-based agreement that moves with
  the bottler's own selling prices, channels and package mix; The Coca-Cola Company unilaterally sets the prices of sales between
  bottlers under the regional manufacturing agreement; and "there are no limits on the prices The Coca-Cola Company and other
  beverage companies can charge for concentrate" outside that agreement (10-K FY2025, Item 1).
- **The key variables and whether they are foreseeable** **[M1998-044]**. For Coca-Cola the speakers named two, "unit case
  sales and shares outstanding" **[M1998-040]**; for the bottler they are: (1) physical cases in the territory, which have moved
  from about 343 million (FY2019, derived from the 4.5% rise to 358.8M in FY2020, 10-K FY2020) to 366.0M (FY2021), 355.4M on the
  restated standard (FY2023), 353.1M (FY2024) and 354.0M (FY2025): flat within a few percent for six years, sparkling steady,
  still beverages the moving part; (2) net price per case, bottle/can sales over cases, $12.06 (FY2019) to $18.68 (FY2025);
  (3) the concentrate price, set by formula with The Coca-Cola Company; (4) inputs (aluminium, PET, corn syrup, about 20% of
  cost of sales excluding concentrate) and labour (about two-thirds of SD&A). Variables (1), (3) and (4) are of the kind that
  can be foreseen within a range ten years out; the contracts run indefinitely at the bottler's option; the customers are
  consumers buying a century-old product, a forecast of "consumer behavior" **[M2023-030]**, **[M2017-019]**, not of
  technology. Variable (2), the margin the bottler keeps on the price, is the one that moved: operating margin 1.3% to 6.5%
  from FY2009 to FY2019 and about 12.6% to 13.2% from FY2023 to FY2025. That is a question of the castle and of the cash base,
  carried to Q2 and Q7; it is knowable from the filings and the field's own filings, which is what Q1 asks **[M2006-076]**.
- **Do the past statements tell me the future ones?** **[M2008-033]**: the statements are those of a distributor (net sales,
  cost of goods, delivery cost, capital spending on trucks, plants and coolers); nothing in them is opaque, and their two
  regimes (before and after FY2020) are each legible. Would the insiders write the ten-year forecast down **[M2000-105]**?
  The CBA's own volume-per-capita test, the 40-year life assigned to the sub-bottling payments and the distribution rights
  (10-K FY2025, Notes) show the system itself plans on that horizon.
- **What could make it TOO HARD here.** Slow change in what people drink (sugar, health trends, energy drinks, the state limits
  on SNAP purchases named in the 10-K, Item 1) is slow change, "much harder to perceive" **[M2014-038]**, owned by Q2; it does
  not put the ten-year economics out of reach. No fast-moving technology is involved.
- **VERDICT: IN.** The ten-year shape (the same exclusive territories, roughly the same cases, a product asked for by name) can
  be foreseen; the doubt is about how much of the price the bottler keeps, which Q2 and Q7 take up. No doubt that it is inside
  the circle as the rows define it **[M2002-092]**, **[M2000-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]**

**The castle tests, each with its filing fact.**
- **What keeps it standing, and how permanent.** The castle is not the bottler's own. It is the exclusive right, under the CBA,
  to make and sell in its territories a brand people "ask for by name"; the speakers' one row on the bottling business itself
  says "that is why a bottling system is valuable" and that "the right to distribute that product is worth good money"
  **[M2002-091]**. The right is permanent at the bottler's option (ten-year terms renewable "indefinitely", 10-K FY2017,
  accession 0001564590-18-003845) and is protected by the Soft Drink Interbrand Competition Act (10-K FY2025, Item 1). It does
  not depend on "the genius of the lord" **[M1995-038]**. Against it: the brand, the formula and the concentrate price belong to
  The Coca-Cola Company, which may sell concentrate at prices "determined from time to time by The Coca-Cola Company in its sole
  discretion" (DEF 14A 2026, Related Person Transactions, accession 0001628280-26-020505), qualified by the incidence-based
  pricing agreement under which the concentrate price rises with the bottler's own prices (10-K FY2025, Item 1). The Coca-Cola
  Company's own 10-K says that under most bottler agreements it "generally" has "complete flexibility to determine the price" of
  concentrate, subject to competitive conditions (KO 10-K FY2025, accession 0001628280-26-010047). In 2025 the company paid The
  Coca-Cola Company $2,264M, 31% of net sales, more than 80% of it for concentrate, syrup, sweetener and finished goods (DEF 14A
  2026), plus $68.9M of sub-bottling payments for the territories bought in 2014 to 2017, payable for about 40 years (10-K FY2025,
  Liquidity). The same speaker's second row on bottlers prefers "the syrup business better than the bottling business", calls
  bottling "a perfectly decent business" and says it is not a wonderful one because it is "very competitive out there"
  **[M2002-062]**. These are rows
  about one industry seen through one system in 2002; they are weighed with the tests and the filings, not taken as the verdict
  (Q2, A row about one company, applied by analogy **[M1994-086]**).
- **The attacker with money.** No sum of money buys the right to sell Coca-Cola in Charlotte; the attacker is the Pepsi system
  and private label (10-K FY2025, Competition). The speakers' test is put of the brand itself **[M2011-015]**; for the bottler
  the question is the rival bottler. PepsiCo's North American beverage business, brand and bottler together, earned 12.0% to 13.9%
  of revenue in 2014 to 2016 and 8.3% to 10.8% in 2018 to 2024 (table below): the rival with money has been losing ground, not
  gaining it.
- **Pricing power and the agony before a rise** **[M2005-020]**. Net bottle/can price per case rose from $12.06 (FY2019) to
  $18.68 (FY2025), 55%, while cases rose 3% (bottle/can sales over physical cases, 10-K MD&A tables FY2020 to FY2025;
  `_arith.py`). Gross margin went from 34.6% (FY2019) to 39.7% (FY2025). "Anytime you can charge more for a product and maintain
  or increase market share against wellentrenched, well-known competitors, you have something very special in people’s minds."
  **[M2000-031]**. But the price behaviour is young, and it is being tested now: cases fell 1.9% in FY2023 and 0.6% in FY2024
  (10-K FY2023 and FY2024), and in Q2 2026 aluminium costs "outpaced our annual pricing actions", gross margin fell 210 basis
  points to 37.9% and operating margin to 13.2% from 14.7% (10-Q Q2 2026, Executive Summary, accession 0001628280-26-053370). "if
  you establish too wide a differential between Coke and a private label product, you will change consumption patterns
  somewhat" **[M2001-088]**.
- **Unit volume and share of mind** **[M1999-054]**. Cases flat for six years (343M derived FY2019, 354.0M FY2025; Q1); sparkling
  steady, still beverages the swing. H1 2026 cases rose 10.3% (7.1% adjusted; 10-Q Q2 2026). Volume shows the place in the mind
  holding, not growing.
- **The low-cost position.** Not shown: no filing gives a cost per case against the Pepsi bottler in the same territory. SD&A
  per case rose from about $4.34 (FY2019) to $5.43 (FY2025) (SD&A over cases), about 25%, while price per case rose 55%: the
  margin came from price, not from cost.
- **The brand in the customer's mind, and against the retailer.** The brand is The Coca-Cola Company's; Walmart and Kroger take 21%
  and 15% of cases and 29% of net sales (10-K FY2025, Item 1). "the brand is our protection against the intermediaries making
  all the money" **[M2019-041]**; the retailer's pressure **[M2001-090]** falls on a bottler that owns no brand.
- **Would the customer still choose it over the low bid?** For the drink, yes on the record of 2021 to 2025 **[M2008-076]**; for
  the bottler the retailer has no choice of Coca-Cola supplier inside the territory.
- **Ask the competitors** **[M1999-130]**, **[M2017-091]**. The best-informed party in the system, The Coca-Cola Company, which
  sets the concentrate price and sees every U.S. bottler's figures, sold 598,619 shares to the company at $925 in July 2024
  ($92.50 after the split; 10-K FY2024, accession 0000317540-25-000025) and the rest, 18,835,460 shares, for about $2.4B (about
  $127.42 a share) on 2025-11-07, leaving it with no shares and no board seat (8-K 2025-11-07, accession 0001628280-25-050682;
  DEF 14A 2026). No reason for the sale is given in the filings read. Written down as contrary evidence, not weighed alone.
- **Widening or narrowing** **[M1999-108]**, **[M2000-075]**. On the filings it has widened since FY2020 (operating margin 6.3% to
  13.2%); before that it narrowed for a decade (6.5% FY2009 to 1.3% FY2018).
- **What could destroy, modify or reduce it** **[M2000-014]**: a change by The Coca-Cola Company in the incidence rate or
  concentrate terms; state limits on buying soft drinks with SNAP benefits, sugar and container taxes (10-K FY2025, Item 1);
  retailer power; slow change in what is drunk. None is a sudden end; each can move the share of the price the bottler keeps.

**The competitor row** (operating income over revenue, each from its own filings; the whole span read, not one year):

| Filer | Metric | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COKE | operating income / net sales | 4.9% | 4.3% | 4.1% | 2.2% | 1.3% | 3.7% | 6.3% | 7.9% | 10.3% | 12.5% | 13.3% | 13.2% | 10-Ks FY2014 to FY2025 (FY2025 0001628280-26-009057; XBRL OperatingIncomeLoss checked against the FY2025 statement, $950.7M); FY2009 to FY2013 4.5% to 6.5% |
| Coca-Cola FEMSA (KOF), **20-F filer, flagged** | (gross profit less selling and administrative expenses) / total revenues, MXN | 14.6% | 15.6% | 13.6% | 13.1% | n/r | 13.9% | 14.4% | 14.3% | n/r | 14.2% | 14.5% | 14.2% | 20-F FY2017 0001193125-18-121141, FY2021 0001628280-22-008868, FY2025 0001628280-26-025313 |
| Coca-Cola Europacific Partners (CCEP), **20-F filer, flagged** | operating profit / revenue, EUR | n/r | 12.0% | 9.3% | 11.4% | 11.3% | 12.9% | 7.7% | 11.0% | 12.0% | 12.8% | 10.4% | 13.4% | 20-Fs FY2016 to FY2025 (XBRL; the FY2025 figure, €2,793M on €20,901M, checked in 20-F 0001650107-26-000029) |
| PepsiCo North American beverages (NAB to 2016, PBNA after; brand and in-house bottling) | segment operating profit / segment net revenue | 12.0% | 13.5% | 13.9% | n/r | 10.8% | 10.0% | 8.6% | n/r | n/r | 9.4% | 8.3% | 3.9% (9.3% before a $1,539M Rockstar impairment) | 10-K FY2016 0000077476-17-000010; FY2020 0000077476-21-000007; FY2025 0000077476-26-000007 (segments restated in 2025) |
| Keurig Dr Pepper | Packaged Beverages (its U.S. bottling and direct-store delivery) operating income / net sales; from 2024 U.S. Refreshment Beverages (includes concentrates) | | | | | 10.6% (part year) | 15.3% | 15.3% | | | | 20.1% | 28.2% | 10-K FY2020 0001418135-21-000005; FY2025 0001418135-26-000016 |
| The Coca-Cola Company (the concentrate side) | consolidated operating margin; its own Bottling Investments segment | | | 20.6% | 21.2% | 27.3% | 27.1% | 27.3% | 26.7% | 25.4% | 24.7% | 21.2%; bottling 8.0% | 28.7%; bottling 7.4%; North America 25.9% | 10-K FY2025 0001628280-26-010047 (segments); XBRL for 2016 to 2023 |

n/r = not read for this run. **Return on the capital employed** (operating income over equity plus debt less cash, year end,
COKE's filed balance sheets; earnings after depreciation against capital employed): 15.5% to 16.2% FY2010 to FY2012, 12.1% to
13.9% FY2013 to FY2015, 11.0% FY2016, 6.7% FY2017, 4.0% FY2018, 13.2% FY2019, then 22.4%, 34.0%, 42.3%, 59.6%, 44.5% and 53.9%
FY2020 to FY2025 (`_peers.py`; the contingent consideration owed to The Coca-Cola Company, $381M at FY2017 and $718M at FY2025,
is left out of capital, which flatters the later years). The expansion of 2014 to 2017 cost $691.1M in net cash (eighteen
transactions, 10-K FY2017 table) plus the sub-bottling payments ($332.3M paid FY2018 to FY2025) and more than doubled net sales
($1,746M FY2014 to $4,625M FY2018); in its first years the larger company earned less operating income than the smaller one had
(FY2014 $86M; FY2018 $58M).

**The parts table.** Two segments: Nonalcoholic Beverages, "the vast majority" of net sales and income from operations ($925.2M
of $950.7M in FY2025), and All Other (the Red Classic transport subsidiaries, $25.5M). Nonalcoholic Beverages decides, with more
than half of five-year operating profit **[L2008-005]**.

**The field's returns over the last full cycle, judged in words.** The durable bottlers of the Coca-Cola system earn steady,
decent and unspectacular margins: Coca-Cola FEMSA about 13% to 16% every year from 2014 to 2025, through Latin American
recessions and the pandemic; CCEP 8% to 13%; The Coca-Cola Company's own bottlers 7% to 8%; PepsiCo's integrated North American
beverages 8% to 14% and falling. This company, over the full record before the change (FY2009 to FY2019, a decade that included
the expansion), earned 1.3% to 6.5% of sales and a pre-tax return on capital of 4% to 16%: ordinary returns **[M2013-052]**, not
the castle that "protects excellent returns on invested capital" **[L2007-004]**. Since FY2020 it has earned 13% of sales and a
return on capital several times its old one, at the top of the field. That is a change for the better.

**Is the change credited?** A change for the better is credited only on the evidence of a full cycle in which the price
behaviour held **[M2005-020]**, **[L1995-022]**; until then the file is TOO HARD (WORK) on that question, not IN (Q2, section C of
the gaps case, a CONVENTION of the framework). The rows say such changes happen **[M2017-026]**; they do not say how long to
watch, and section C gives no span. **CONVENTION of this run:** the cycle is read on the series Q7's first specific names, owner
cash as Q4 recasts it, peak to peak or trough to trough. Rationale: section C needs a span and Q7(a) is the only place the
framework defines a cycle. On that series (`_arith.py`; the Q4 facts below) owner cash after every real cost went $95.9M (FY2019),
$246.6M, $318.5M, $193.1M, $498.6M, $439.1M and $555.5M (FY2020 to FY2025): one dip (FY2022, a capital-spending year), no trough
in demand, and the first real test of the new price behaviour, a cost squeeze that outran the price increases, began only in Q2
2026 (10-Q Q2 2026). The price behaviour has held through one swing of input costs (the inflation of 2021 and 2022 and its easing
in 2023 and 2024, prices not given back); it has not yet been seen through a full cycle. The change is therefore not credited,
and the castle is judged neither IN (on six years of a new regime) nor OUT (on the decade before it).

**Why WORK and not NATURE.** The deciding question, whether the margin and the price per case the bottler keeps will hold
through a cycle, is important and partly knowable now **[M2006-076]**: the company's record before FY2009 (its 10-Ks back to the
1990s), its concentrate cost as a share of sales over time (the related-party payments in each proxy), its price and cases
through the recession of 2008 and 2009, the Pepsi rival's price and volume in the same years, and FY2026's answer to the
aluminium squeeze can all be read. The system's insiders do write the long-range plan down: the CBA requires one every year
(DEF 14A 2026) **[M2000-105]**. It is not a forecast the industry would refuse to make.

- **VERDICT: TOO HARD (WORK).** The castle, an exclusive and perpetual right to a brand asked for by name, stands; what it
  protects is the question. Over its last full record it protected ordinary returns; since FY2020 it has protected excellent
  ones, and a change for the better is not credited before a full cycle in which the price behaviour held **[M2005-020]**,
  **[L1995-022]**; a moat whose worth cannot yet be judged is not valued **[M2000-019]**. The file closes here. Research-pass
  steps 1 and 2 are written at the end and not run.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read (the brief asks for them when the file closes before Q4); the reading is under AFTER
THE STOP, not weighed.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The reporting figures the brief asks for are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (WORK), at Q2**: the castle (an exclusive, perpetual right to make and sell a brand asked for by name) stands, but
the returns it protects changed for the better only from FY2020, and a change for the better is not credited before a full cycle
in which the price behaviour held; the deciding question is knowable from filings not yet read and from FY2026. Q7 not reached;
the reporting figures below are COMPUTATION, NOT A CLEARANCE ($75.62 to $154.30 a share against $194.61). **Integrity facts
recorded, not judged.** Q11 belongs to the holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.*

**Bearing on Q3 (capital).**
- Capital spending $282.3M, $371.0M, $312.3M (FY2023 to FY2025; 3.9% to 5.4% of net sales) against depreciation of PP&E $153.5M,
  $170.3M, $195.1M (10-K FY2025 cash-flow statement); FY2026 guidance about $300M (10-K FY2025, Liquidity). The CBA and the RMA
  require "minimum, ongoing capital expenditures" at a level not disclosed (10-K FY2025, Item 1), so the filing does not allow a
  maintenance guess. A 2002 row about bottlers put the spending needed "just to stay in the same place" at 5 to 6 percent of
  revenues **[M2002-061]**, which is above what this company spends.
- Earnings after depreciation against capital employed (operating income over equity plus debt less cash): 11% to 16% FY2010 to
  FY2016, 4% to 7% FY2017 to FY2018, 22% to 60% FY2020 to FY2025 (Q2). Cases flat for six years, so growth has been price.
- PP&E net $813M (FY2016) to $1,605M (FY2025) while net sales went from $3,130M to $7,228M.

**Bearing on Q4 (the accounts). The balance sheets, FY2016 to FY2025 (USD millions; `tools/run.py` table from first-filed XBRL,
the FY2024 and FY2025 columns checked against the filed balance sheet, 10-K FY2025 page 43):**

| Year end | Total assets | Equity | Cash | Inventory | Trade receivables (gross) | Goodwill | Debt (current + long-term) | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017-01-01 | 2,449 | 277 | 22 | 144 | 272 | 145 | 907 | 302 |
| 2017-12-31 | 3,073 | 367 | 17 | 184 | 396 | 169 | 1,088 | 389 |
| 2018-12-30 | 3,010 | 358 | 14 | 210 | 437 | 166 | 1,104 | 359 |
| 2019-12-29 | 3,127 | 347 | 10 | 226 | 434 | 166 | 1,030 | 381 |
| 2020-12-31 | 3,222 | 513 | 55 | 226 | 425 | 166 | 940 | 544 |
| 2021-12-31 | 3,446 | 712 | 142 | 303 | 472 | 166 | 723 | 724 |
| 2022-12-31 | 3,710 | 1,115 | 198 | 348 | 532 | 166 | 599 | 1,112 |
| 2023-12-31 | 4,289 | 1,436 | 635 | 322 | n/r | 166 | 599 | 1,352 |
| 2024-12-31 | 5,313 | 1,418 | 1,136 (+301 short-term investments) | 330 | 568 | 166 | 1,786 | 1,395 |
| 2025-12-31 | 4,303 | (740) | 282 | 336 | 586 | 166 | 2,786 | (824) |

  What they say: goodwill has not moved since the expansion closed in 2017 ($166M), and distribution agreements ($767M at FY2025)
  are amortized over 20 to 40 years; inventory (2.3 times FY2016) and trade receivables (about 30 to 31 days of sales in FY2016,
  FY2022 and FY2025) have grown with sales, nothing building ahead of them; prepaid and other current assets $108.7M (FY2025) on
  $7.2B of sales. Debt rose to $1.1B with the expansion, was paid down from operations to $599M by FY2022 while cash built to
  $1.1B, and then rose to $2.8B to pay for the repurchases of 2024 and 2025; retained earnings were wiped out by the $2.4B
  repurchase from The Coca-Cola Company (charged against them), so equity is negative ($(739.7)M at FY2025, $(500.1)M at
  2026-07-03, 10-Q). What they cannot say: the liability that grows with the business's success, the acquisition-related
  contingent consideration owed to The Coca-Cola Company, $381M (FY2017) to $718M (FY2025) despite $332M paid, is remeasured
  each quarter at the company's WACC, so its income-statement charge swings with interest rates ($31M to $159M a year, FY2020 to
  FY2025).
- **The real costs.** Depreciation is real and below capital spending. Stock pay: none found; the chief executive's long-term
  plan is settled in cash or Class B shares (DEF 14A 2026), XBRL shows no share-based compensation after FY2019, and the diluted
  Class B count adds about 0.1M shares (10-K FY2025, EPS). The sub-bottling payments to The Coca-Cola Company ($28.2M to $68.9M a
  year, FY2023 to FY2025) are classed in financing; they are an operating cost of the territories and are deducted from owner cash
  below. The 10-K features "Comparable and Adjusted Results (Non-GAAP)" that remove the remeasurement of that liability and the
  commodity hedge marks (adjusted net income FY2025 $668.5M against GAAP $570.6M); the cash payments themselves are not removed.
  No earnings guidance found in the filings read (capital spending is the only forward figure given). A pension settlement of
  $112.8M (FY2023, non-cash) was a one-time item.
- **Owner cash after every real cost** (operating cash flow, less capital spending net of disposals, sub-bottling payments, finance
  lease principal and distribution rights bought; `_arith.py`): FY2019 $95.9M; FY2020 $246.6M; FY2021 $318.5M; FY2022 $193.1M;
  FY2023 $498.6M; FY2024 $439.1M; FY2025 $555.5M (after interest). Before after-tax net interest (all-equity basis): $343.2M,
  $211.5M, $497.9M, $440.5M, $587.1M (FY2021 to FY2025). Never a net-income proxy (operator rule 5). One figure checked: the FY2025
  OCF, $931.9M, against the filed cash-flow statement.

**Bearing on Q5 (integrity facts, recorded, not judged).**
- Control: J. Frank Harrison, III, Chairman and CEO, controls 10,043,940 Class B shares, about 78% of the vote, with a trust's right
  to exchange 2,923,860 Common for Class B (to about 83%) (10-K FY2025, Item 1A; DEF 14A 2026).
- Related persons: the headquarters and an adjacent office are leased from Beacon Investment Corporation, of which Mr. Harrison is
  the majority stockholder and his daughter (Vice Chair) a minority stockholder; rent $4.1M in fiscal 2025; lease to 2029,
  approved by the Audit Committee and a special committee. The Vice Chair (his daughter) was paid $2,054,925 and the Chief Sales
  and Service Officer and director nominee (his son-in-law) $742,638 in fiscal 2025 (DEF 14A 2026, Related Person Transactions).
- Pay: the CEO's total compensation $19.78M (2023), $19.03M (2024), $16.71M (2025); the plans pay on three-year EBIT, EBIT margin
  and free cash flow; the company pays tax gross-ups on certain pay and "requires the CEO to use the Company’s corporate aircraft
  whenever reasonable for both business and personal travel" (DEF 14A 2026, Summary Compensation Table and Perquisites).
- Reports: an adjusted net income is presented beside GAAP in the 10-K (Q4 facts above).
- The repurchase from The Coca-Cola Company in 2025 named Mr. Harrison as a party for certain articles and ended the agreement
  under which The Coca-Cola Company nominated a director; that director resigned (8-K 2025-11-07).

**Bearing on Q6 (the money and the owners).**
- Buybacks and their prices (split-adjusted): July 2024, 598,619 pre-split shares from The Coca-Cola Company and 14,391.5 in a
  Dutch-auction tender, both at $925 ($92.50); 2025, 1,778,081 shares in the open market for $212.0M (about $119.23); 2025-11-07,
  18,835,460 shares from The Coca-Cola Company for about $2.4B (about $127.42). The programme names no price ("depend on market
  conditions, the prevailing market price", 10-K FY2025); authorization cut from $1.0B to $400M on 2025-11-07; $136.3M left, none
  used in Q2 2026. Against the computed range below (all-equity bottom $75.62), every price paid sits above the bottom.
- Funding: the 2024 purchases were paid with $1.2B of bonds (2029 and 2034), the 2025 purchase with cash and $2.35B of new bank
  loans; $275M of the term loans prepaid in H1 2026 (10-Q).
- Dividends: regular $0.50 a quarter before the split; special dividends of $3.00 (2023) and $16.00 (declared December 2023, paid
  February 2024) a pre-split share (10-K FY2023); $86.7M paid in 2025.
- Shares: diluted Common plus Class B fell from about 104.2M (FY2023 weighted, split-adjusted) to 66.56M today.

**Bearing on Q7 (the reporting figures, COMPUTATION, NOT A CLEARANCE).** Built as Q7 builds the range (CONVENTION of the
framework), with its specifics; `_arith.py`.
- Base: five-year average of owner cash after every real cost, FY2021 to FY2025 (the literal window; the filer describes no end
  year as a peak or trough, so specific (a) leaves the window as it is): **$416.0M before interest** (all-equity), $401.0M after
  interest (equity-only). Specific (c): distribution rights bought ($9.0M FY2021, $30.6M FY2022) deducted, total growth credited;
  organic growth is not reported. (d): working capital is inside operating cash flow. (e): the filing allows no maintenance guess,
  so all capital spending is charged; the depreciation variant is shown beside. (b): no decline.
- Growth shown, aggregate owner cash between the end years: 14.4% a year (all-equity), 14.9% (equity-only). (f): carried ten years
  it gives owner cash of about four times today's, about 15 to 16% of a net sales line growing at its window rate, twice the
  free-cash margin of today and far above what the field's best bottler earns (Q2 table), with cases flat: a result that traces
  to an absurdity and is cut back **[M1999-067]**. **CONVENTION of this run:** cut back to the growth of net sales over the same
  window, 6.8% a year (FY2021 $5,562.7M to FY2025 $7,228.1M), i.e. owner cash at the end-of-window margin; rationale: the excess
  of the shown rate over sales growth is the margin's rise from 7.9% to 13.2%, which cannot compound for ten more years in a
  field whose best margin is about 14%. Ten years, then zero nominal growth; discounted at 5.64%.
- Net debt at 2026-07-03 (10-Q, the latest filed balance sheet; no subsequent events stated): debt $2,513.1M plus finance leases
  $1.5M less cash $171.7M = **$2,342.9M**. Operating leases ($137.7M of minimum payments) are left out. The contingent
  consideration ($718M) is not added: its cash payments are already deducted from owner cash.
- **(a) VALUE RANGE, all-equity (central): $75.62 to $154.30 a share** (whole business $7,376M to $12,614M, less net debt, over
  66.564M shares; width 1.71 to one). With the literal shown growth beside: $75.62 to $308.98 (width 3.11 to one, past the
  framework's three-to-one). Equity-only beside: $106.80 to $182.63 (literal $106.80 to $346.47); the equity-only figure uses
  owner cash after the low interest of FY2021 to FY2025; at the contractual interest due in 2026 on today's debt ($138.7M, 10-K
  FY2025) that base would be about $313M, not $401M. Depreciation variant, all-equity: $106.26 to $206.70.
- **(b) FAIR PRICE, all-equity (central): $46.03 a share**; equity-only $78.28. Tax: owner cash after the company's own income tax
  (effective rate about 26%, FY2024 and FY2025), no conversion; no carryforward found. **CONVENTION of this run** on "the price at
  which the midpoint of the range earns the floor": the midpoint is read as the owner-cash stream whose value at the sovereign is
  the range's midpoint (the base growing 3.83% a year for ten years, then flat), and the fair price is that same stream discounted
  at the floor of ten percent; rationale: the midpoint is a value, the floor is a rate of return, and the stream is the one object
  both can be applied to. Depreciation variant fair price, all-equity: $68.49.
- At $194.61 the market value is $12,954M and the enterprise value $15,297M; the five-year owner cash is a 2.7% yield on it before
  interest (3.8% on FY2025 alone), against a 30-year Treasury of 5.64%. No other price figure is reported (the brief).

**Bearing on Q8.** The 30-year Treasury yields 5.64%; owner cash yields 2.7% (above).

**Bearing on Q9 (debt and exposures).**
- Debt at 2026-07-03 $2,513.1M: senior notes $100M due 2026-10-10; term loans $1.08B (2028 and 2030, floating, partly swapped);
  senior bonds $700M (2029) and $500M (2034); senior notes $150M (2030); revolver $500M undrawn (10-Q; 10-K FY2025). Ratings Baa1
  stable, BBB+ negative (10-K FY2025). Covenants on the bank and private debt: cash flow to fixed charges at least 1.5 and funded
  debt to cash flow at most 6.0 (8-K 2025-11-07); in compliance. No subsidiary debt and no guarantees.
- FY2025 operating income $950.7M against interest expense $102.9M; contractual interest due in 2026 $138.7M.
- Other claims: contingent consideration $717.9M (about $50M to $80M a year for five years); a take-or-pay of 16.0M cases a year
  from the South Atlantic Canners cooperative to June 2034 (about $1.20B); executive benefit plans $217.1M; postretirement $73.7M;
  marketing commitments $151.1M; a supply-chain finance programme for suppliers (10-K FY2025, Contractual Obligations).
- Concentration: Walmart and Kroger 29% of net sales; two can suppliers; bottles from two cooperatives (10-K FY2025, Item 1 and 1A).

**Bearing on Q10.** None beyond Q7 and Q8.

**Bearing on Q12.** Sugared drinks and energy drinks are the subject of school, SNAP and tax restrictions named in the 10-K (Item 1);
the company gave $52M to charities and donor-advised funds in 2025 (10-K FY2025, Item 1). Not a business the rows name.

---
## RESEARCH PASS, STEPS 1 AND 2 (written, not run; Part VII)
**Step 1. "What do I not know that I need to know?"** **[M1999-129]**. The deciding question (Q2): will the margin and the price
per case the bottler now keeps hold through a full cycle, or revert toward the 1% to 7% it earned before FY2020? Each sub-question
marked knowable or not **[M2006-076]**:
1. Before FY2009, did the company ever earn an operating margin near today's, and if so, did it hold through a downturn?
   Knowable (10-Ks FY1995 to FY2008).
2. Has the share of the bottler's net sales paid to The Coca-Cola Company risen as the bottler's prices rose, that is, is the
   concentrate owner taking the gain back? Knowable (related-party tables in the proxies and the related-party note of each 10-K,
   FY2017 to FY2025).
3. Through the recession of 2008 and 2009 and the input-cost rise of 2010 and 2011, what did price per case, cases and the
   operating margin do? Knowable (10-Ks FY2007 to FY2012).
4. Does price catch up with the aluminium squeeze that began in 2025 and outran pricing in Q2 2026? Knowable on the record of
   FY2026 (10-Q Q3 2026, 10-K FY2026, due about February 2027).
5. Will the next consumer recession hold the price? Not knowable now; recorded and set aside; the close is decided on 1 to 4.

**Step 2. Evidence, span and source fixed now, and the single fact that would close the file OUT** **[M1998-144]**:
1. Span FY1995 to FY2008, source the company's 10-Ks on EDGAR (income statement and MD&A). OUT fact: in any year of the span the
   operating margin stood at 10% or more and within five years fell below 6%.
2. Span FY2017 to FY2025, source the proxies' "payments made by Coca-Cola Consolidated to The Coca-Cola Company" over 10-K net sales.
   OUT fact: that share is higher in FY2025 than in FY2021 by more than the operating margin's gain over the same years (5.3
   points), i.e. the concentrate owner took back more than the bottler kept.
3. Span FY2007 to FY2012, source the 10-Ks (MD&A price per unit, cases, operating income). OUT fact: bottle/can price per unit fell
   in FY2009 or FY2010 while the operating margin fell below FY2007's.
4. Span FY2026, source the 10-K FY2026. OUT fact: the FY2026 operating margin is below 11.0% with cases up for the year.
How step 4 closes: OUT if any one OUT fact is found; IN if none is, and question 4 shows the FY2026 operating margin at or above
12.5% (the low of FY2023 to FY2025), the change then being credited on the cost cycle of 2021 to 2026; TOO HARD (NATURE) only if
the pass ends unsure **[M2002-092]**, never TOO HARD (WORK) again on the same question **[M2008-086]**. A capital test in the pass
sets earnings after depreciation against capital employed, or cash earnings against capital spending, never one against the
other; every margin comparison covers the whole span named.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): the template
      copy and position note (commit ecf0120b), Step 0 to Q1 (53bd67d2), Q2 (69ec07d5), the close (this commit).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the dispatcher's lock was seen present in `Screens/_daily/`
      ("interactive v5 re-runs batch 3", written 09:26), read only to confirm it. Folding into the register is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; `Test Runs/` was never listed. Seen by
      accident and declared under contamination at the top: the dispatch message's mention of earlier runs on this name; five
      commit subjects in the session context (CB and a re-run batch of AVGO, BMI, CB, CHD); a memory line with a count of gate
      clearers; and the lock's text, which names this batch "v5 re-runs batch 3". None used.
- [x] Every v5 id resolves (checked by `_check.py` against `principle_ledger_v5.csv`); every filing fact has its accession or its
      named document; no E-ids.
- [x] The order was kept; Q1 IN, Q2 closed TOO HARD (WORK); nothing after Q2 is a clearance; the reporting figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sub-bottling payments the filer puts in
      financing are deducted; the sovereign from the U.S. Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (THE FOUNDATIONS; Q2); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its share basis, cap and yield (stale weighted average) were rejected.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the commit).
- Declared departures: two CONVENTIONs of this run (the cycle for section C read on Q7(a)'s series; the cut-back of the shown
  growth to the window's sales growth) and one reading (the fair price's midpoint as a stream); each is labelled where used.
- Declared limits: KOF's operating margin is computed from its income statement lines (its operating income is not tagged in
  XBRL); CCEP and the other peers' 2016 to 2023 figures are XBRL transcriptions with one figure checked per filer, not every year;
  peers' returns on capital were not computed (their XBRL debt tags are inconsistent) and the competitor row is on margins only;
  the FY2019 case count is derived from the FY2020 growth rate.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Section C ("a change for the better is credited only on a full cycle") gives no span and no series, and it decided this file.
I read the cycle on the series Q7(a) defines (owner cash, peak to peak or trough to trough) and confessed it as a CONVENTION of this
run; two analysts could otherwise credit or refuse the same six years by choice. (2) It is unclear whether a change for the better
that is not credited leaves the castle to be judged on the old record (which here would read OUT, a castle protecting ordinary
returns) or sends it to TOO HARD (WORK); the text says TOO HARD (WORK) "on that question", and I applied that, but the old
record's OUT is then never tested. (3) The fair price's "midpoint of the range earns the floor" is a value meeting a rate; the text
does not say how one is applied to the other, and I confessed my reading. (4) Q7(f) says a result that "traces to an absurdity is
cut back" but not to what; I confessed my cut-back. (5) "A row about one company" speaks of one named company; the two 2002 rows
on the bottling business are about one industry seen through one system, and the convention does not say whether it reaches them
(I weighed them, by analogy). (6) Part VII still says "The run template for v5 does not yet exist; it is written at adoption",
which is stale: the template exists. (7) The brief: the dispatch message says its blind rule covers "every run file of other
companies", while the canonical brief's rule covers other companies' files "of the last week"; I kept the wider rule. The brief's
reporting paragraph has a garbled clause ("with a built by Q7's six specifics"), and its "Doing the run" line calls Q6 a weighing
with no STOP although Q6 carries the all-stock-deal STOP.
