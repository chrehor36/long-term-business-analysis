## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥7,358 per Tokyo share, close of 2026-10-09 (Friday; 2026-10-12 is a Japanese holiday and the Tokyo market
  was closed), Yahoo Finance chart API, **aggregator, flagged** (operator rule 5). The ADR NPNYY closed $9.33 the same day
  (aggregator). ADS ratio from the company's own ADR page (`www.nyk.com/english/ir/stock/adr/`, read 2026-10-12):
  **5 ADRs : 1 ordinary share**, so one ADS is 0.2 share; depositary Bank of New York Mellon, CUSIP 654633304, OTC.
  Check: ¥7,358 × 0.2 ÷ ¥158.06 per $ (Yahoo USD/JPY close 2026-10-08, aggregator) = $9.31 against $9.33 quoted. The ratio holds.
- **Share changes checked from the company's own documents:** a 1-for-10 reverse split on October 1, 2017 and a 3-for-1 split
  on October 1, 2022 (IR Data Book 2026, note 3 to the indicators table); cancellations of treasury shares of 25,321,600 on
  2026-03-25 and 3,458,300 on 2026-05-29 (TSE notice "Notice Regarding Results and Completion of Stock Acquisition, and
  Retirement of Own Stock", May 7, 2026). No merger paid in NYK shares and no spin-off found in the documents read. Nippon
  Cargo Airlines left the group by a share exchange with ANA Holdings effective August 1, 2025 (NYK issued no shares; it
  received ANA shares); Movianto International B.V. was bought for cash in the year to March 2026.
- **Shares:** issued 405,321,700 less treasury 1,766,082 = **403,555,618** outstanding at June 30, 2026 ("Consolidated
  Financial Results for Three Months Ended June 30, 2026", TSE, August 5, 2026, item 4(4)); at March 31, 2026 the figures were
  408,780,000 issued less 3,288,388 treasury ("Consolidated Financial Results for the Year Ended March 31, 2026", TSE, May 11,
  2026). The IR news list (read 2026-10-12) shows no buyback, issue or cancellation announced after August 5, 2026, and the
  company's stock page gives 405,321,700 issued, agreeing.
- **Market cap:** 403,555,618 × ¥7,358 = **¥2,969.4bn** ($18.79bn at ¥158.06).
- **Sovereign for the earnings currency (yen):** **4.085%**, the 30-year JGB, 2026-10-09, Japan Ministry of Finance
  `jgbcme.csv` (issuing authority; `tools/sources.py` returned 4.136% for 2026-10-08 from the same file).
- **Filings read** (operator rule 4; the company has no SEC periodic filings, so its own documents are primary; title and date
  stand in place of an accession number):
  - "Financial Results 2026, Year Ended March 31, 2026" (audited English consolidated statements, NYK IR library), and the
    same series for the years to March 2018, 2019, 2021, 2022, 2023 and 2025 (balance sheets and the antitrust notes).
  - "Consolidated Financial Results for the Year Ended March 31, 2026" (TSE tanshin, May 11, 2026), and the first-quarter
    tanshin of August 5, 2026 (balance sheet and interest-bearing debt at June 30, 2026).
  - "IR Data Book 2026" (May 11, 2026): eleven years of statements, segments and cash flows, years to March 2016-2026.
  - "NYK FACT BOOK 2018" (Fact Book II): cash flows for the years to March 2008-2018.
  - "NYK Report 2025" (integrated report, November 2025): business and segment description, liner strategy, risks.
  - "IR Fact book 2025" (October 2025): competitor fleet table, the ONE 2030 plan, the medium-term plan.
  - Briefing materials of May 26 2020, May 9 2022, May 8 2024 and May 11 2026, each carrying Ocean Network Express's own
    annual results pages (ONE's "Financial Results" decks, reproduced inside NYK's briefings).
  - TSE notices: revision of forecasts (July 30, 2026); revision of the dividend forecast (August 5, 2026); the scheduled
    tender offer for NS United Kaiun (July 31, 2026); the DGMO third-party allotment (July 30, 2026); buyback completion and
    retirement (May 7, 2026).
  - Not read: the Japanese-language annual securities report (yuho) on EDINET, the corporate governance report and the notice
    of the June 2026 general meeting (the file closed before Q5 and Q6; listed under what could not be got).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, year to March 2026,
  ¥473,358m in the IR Data Book 2026, page 6 = ¥473,358m in the audited consolidated statement of cash flows, Financial
  Results 2026, page 6. Total assets ¥5,201,670m also agree.
- `python tools/run.py NPNYY`: "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE"; `python Screens/cover_shares.py NPNYY`:
  "NOT AN SEC REGISTRANT". Both expected; every figure below is from the company's documents. The arithmetic is in
  `Test Runs/_research 2026-10-12 NPNYY/compute.py`, with its output in `compute_out.txt` beside it.
- **Owner cash after every real cost** (¥bn, years to March 31): operating cash flow, which already carries tax paid,
  interest paid, the change in working capital and the dividends received from equity-method affiliates; less purchases of
  vessels, property, plant, equipment and intangibles; less repayment of lease liabilities; less cash paid for subsidiaries
  net of subsidiaries sold. Vessel-sale proceeds and the depreciation variant are shown beside, not used.

  | YE Mar | OCF | capex | lease | net acq. | **owner cash** | with vessel-sale proceeds | D&A variant |
  |---|---|---|---|---|---|---|---|
  | 2016 | 142.9 | 115.9 | 0.0 | -9.4 | **36.4** | 110.5 | 48.9 |
  | 2017 | 27.9 | 156.2 | 0.0 | 2.3 | **-130.6** | -100.0 | -66.3 |
  | 2018 | 89.1 | 199.2 | 0.0 | 8.3 | **-118.5** | -47.5 | -7.1 |
  | 2019 | 45.3 | 169.6 | 2.4 | -7.7 | **-119.0** | -33.7 | -39.1 |
  | 2020 | 116.9 | 138.8 | 19.3 | 0.0 | **-41.2** | 29.7 | -6.4 |
  | 2021 | 159.3 | 102.1 | 19.9 | -2.1 | **39.4** | 115.4 | 42.7 |
  | 2022 | 507.8 | 192.7 | 20.4 | -36.0 | **330.6** | 366.0 | 421.7 |
  | 2023 | 824.9 | 198.4 | 24.2 | 12.9 | **589.4** | 618.4 | 666.1 |
  | 2024 | 401.4 | 336.3 | 27.0 | -4.0 | **42.1** | 121.9 | 236.8 |
  | 2025 | 510.8 | 206.5 | 26.0 | -85.8 | **364.1** | 452.5 | 416.0 |
  | 2026 | 473.4 | 304.5 | 29.4 | 263.1 | **-123.6** | -41.3 | 5.7 |

  Five-year literal average (YE Mar 2022-2026): ¥240.5bn. For YE Mar 2008-2015 (Fact Book 2018), owner cash on the same
  definition was negative in every year, from -¥301.9bn to -¥55.2bn; the nineteen years YE Mar 2008-2026 sum to
  **-¥637.9bn** (+¥1,619.5bn if every vessel-sale proceed is credited). Stock pay is immaterial (a share-delivery trust;
  provision for stock payment ¥0.3bn at March 2026).

### The balance sheets, ten years, before the income account [M2025-032]
*(Read here because the file closes before Q4.)* ¥bn at March 31 (IR Data Book 2026 items 9 to 12; cash from its cash-flow
page; the other lines from the filed balance sheets of the Financial Results series; n.r. = not read):

| Mar 31 | total assets | shareholders' equity | interest-bearing debt | cash eq. | investment securities | goodwill | retained earnings |
|---|---|---|---|---|---|---|---|
| 2017 | 2,044 | 522 | 945 | 137 | 410 | 18.6 | 202 |
| 2018 | 2,072 | 552 | 983 | 103 | 423 | 22.0 | 345 |
| 2019 | 2,002 | 487 | 1,046 | 78 | 479 | 16.4 | 294 |
| 2020 | 1,933 | 463 | 1,050 | 77 | 449 | 11.1 | 312 |
| 2021 | 2,125 | 625 | 951 | 104 | 579 | 10.2 | 445 |
| 2022 | 3,080 | 1,714 | 808 | 227 | 1,146 | 8.7 | 1,396 |
| 2023 | 3,777 | 2,479 | 694 | 196 | 1,688 | 13.7 | 2,019 |
| 2024 | 4,255 | 2,650 | 914 | 145 | 1,813 | 27.7 | n.r. |
| 2025 | 4,320 | 2,919 | 738 | 150 | 1,993 | 22.9 | 2,298 |
| 2026 | 5,202 | 3,072 | 1,201 | 211 | 1,975 | 250.6 | 2,118 |
| Jun 30 2026 | 5,397 | 3,115 | 1,362 | 226 (deposits) | 2,023 | 246.1 | n.r. |

What the figures say: until March 2021 this was a thin, levered balance sheet (equity ratio 24% to 29%, debt-equity 1.5 to
2.3 times), and the year to March 2017 took a ¥265.7bn net loss with ¥168.1bn of impairments, a third of equity. What came
after is the container windfall of 2020-2023, held mostly in the equity-method affiliate: investment securities rose by
¥1.5 trillion (chiefly the ONE stake) and retained earnings by ¥1.7 trillion in three years. What they do not say: the equity
gain was not made by the consolidated fleet. Receivables rose from 11.5% of revenue (March 2020) to 16.4% (March 2026, with
Movianto consolidated); inventories, mainly fuel, from ¥32.5bn to ¥72.6bn. Since March 2023 debt has nearly doubled
(¥694bn to ¥1,362bn at June 30, 2026, leases of ¥248bn included) while the company paid for buybacks (¥200bn, ¥125bn and
¥144bn in the three years to March 2026), a ¥390bn dividend in the year to March 2023, the cash purchase of Movianto (¥263bn,
goodwill up ¥228bn) and a capex step-up to ¥305bn. Operating leases (chartered-in ships) are not in the debt figures; a
residual value guarantee of ¥29.7bn on leased vessels sits in the contingencies note.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this if the market closed for years **[M1997-109]**,
which for a shipping group means owning the freight cycle itself, not the next quote. The market serves and does not
instruct **[M2006-077]**: the quote has risen several-fold with the container windfall and says nothing of value by itself.
No macro forecast enters **[M2000-094]**, and that cuts hard here, because the company's own explanations of its results are
almost all macro (the Red Sea, tariffs, the Strait of Hormuz, the yen, bunker prices); what counts instead is "the average
profitability of the business over time" **[M2015-016]**. The analyst's habit applied: I am looking "for what’s wrong in
things" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) for Q1, the company's own one-year forecast moved by a
third in eleven weeks (recurring profit ¥185bn on May 11, 2026, ¥250bn on July 30, 2026), so the key variable is not
foreseeable even one year out by the insiders; (2) for Q2, ONE's full-cycle return on its founding capital was very high
(profits of $40.3bn over FY2018-FY2025), which runs against any reading that the field earns only ordinary returns and has to
be explained, not ignored; (3) for Q3, owner cash was negative in every year from March 2008 to March 2020 but one, and over
nineteen years is negative in sum; (4) the company's own note records "its conspiracy to fix prices of shipping with major
automobile shipping companies" (an integrity fact for Q5).

## THE STANDING RULE
The buyer's rule: a part-interest bought with the buyer's own money, and sized so that a fall of half or more is borne without
a forced sale, puts nothing the buyer has and needs at risk **[M2012-081]**; borrowed money to hold a stock this volatile is
what the rows name as the way to be prevented from "playing out your hand" **[M2004-065]**. Nothing in this business changes
that; the target's own debt is Q9's and is recorded under AFTER THE STOP.

---
### The lines of evidence, and where they were derived
Derived from the NYK Report 2025 (business and segment description, the liner and logistics growth strategy, "Past changes in
business environment"), the segment note and "Overview by Business Segment" of the May 11, 2026 tanshin (the equivalent of
Item 7), the risk and outlook statements in the tanshin, the briefing materials and the forecast revisions (the equivalent of
Item 1A; the yuho's own business-risk section was not read), and the contingencies notes of the Financial Results series.
Lines chosen: (1) the parts and their share of five-year segment profit; (2) ONE's own results, liftings, freight and margins
over FY2018-FY2025, and what NYK can and cannot see of ONE (equity method; dividends received); (3) pricing through the
2020-2022 spike and the collapse after, and the forecast record; (4) fleet spending against depreciation over nineteen years
and its financing; (5) acquisitions (Movianto, NS United Kaiun, DGMO) and goodwill; (6) debt and leases; (7) buybacks and
their prices; (8) the car-carrier price-fixing investigations and class actions; (9) the one SEC-filing liner rival's record.

## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The parts that matter** (Q1's holding-company paragraph, with Q2's threshold). Segment profit as the filer reports it
  (recurring profit, the only segment profit measure in its filings), years to March 2022-2026, of a consolidated
  ¥3,076.3bn: **Liner Trade ¥1,916.9bn, 62.3%**; Automotive, Dry Bulk and Energy (one "Bulk Shipping" segment until the year
  to March 2024) ¥859.4bn, 27.9%; Air Cargo ¥164.6bn, 5.4% (passed to ANA by share exchange, August 2025); Logistics
  ¥170.4bn, 5.5%; Others ¥13.4bn; eliminations -¥48.5bn (IR Data Book 2026, page 4). The part that matters is Liner Trade,
  and Liner Trade is in substance Ocean Network Express (ONE), the 38% equity-method affiliate formed in 2018 from the
  container businesses of NYK, MOL and K Line. Counted by cash received instead (the framework's equity-method convention),
  the result is the same: interest and dividends received were ¥1,331.6bn over the same five years, against ¥42.0bn in the
  year to March 2021, the difference being ONE's dividends.
- **What the business is.** ONE carries containers on scheduled services. It is sixth of the world's carriers by fleet,
  2,005,871 TEU and 6.4% of capacity at April 30, 2025, against MSC 6,502,429 TEU (20.7%), Maersk 14.3%, CMA CGM 12.4%,
  COSCO 10.5% and Hapag-Lloyd 7.6% (IR Fact book 2025, page 16); its fleet was 2,231,703 TEU at March 31, 2026 with 67 ships
  on order (ONE results deck in the NYK briefing of May 11, 2026).
- **The key variables and whether they are foreseeable** **[M1998-044]**: liftings (12.1m TEU in FY2021, 12.9m in FY2025;
  steady) and the freight rate against the cost of the fleet (wildly unsteady: ONE's revenue went from $10.9bn in FY2018 to
  $30.1bn in FY2021 and back to $16.6bn in FY2025 on nearly the same liftings). The freight rate is set by the supply of ships
  against demand: ONE's own FY2025 analysis gives "Freight Decreased due to softer supply-demand balance" and names newbuild
  deliveries that "increased market supply". It is not foreseeable: NYK's forecast of recurring profit for the year to March
  2027 went from ¥185bn (May 11, 2026) to ¥250bn (July 30, 2026), explained by "container freight market conditions [that]
  have continued to outperform our initial assumptions" (TSE notice, July 30, 2026).
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**. The freight rate of 2036 cannot be fixed; but the definition asks for the
  economics, and the economic dynamics of this industry can be stated from the filings with confidence. What matters is "are
  there competitive moats? Is there ease of entry?" **[M2011-014]**, and the documents answer: entry is open to anyone with
  money to order ships, and the largest carrier became the largest by ordering them; the product is a commodity; ONE is a
  mid-sized price-taker that NYK's own report says "has been working to close the fleet scale gap with its major competitors"
  (NYK Report 2025, Liner & Logistics). That is a fix on the competitive position and on the kind of earning power (the
  commodity's cycle average), and Q2 then tests it. The industry is not one of rapid technological change (the box ship is
  seventy years old), so the routing rule for change **[M1998-008]** does not send it to TOO HARD here.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. My doubt is
  about the year's price, not about the economics: I hold no doubt that this is a commodity business whose returns are set
  by its field. A narrower reading is open and is carried to WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR: that the
  unforeseeable key variable alone ("If something is not very predictable, forget it." **[M1998-044]**) closes the file here
  TOO HARD (NATURE).
- **The other parts** (not deciding): car carriers, dry bulk and tankers are ship-operating businesses of the same commodity
  kind; LNG carriers and FPSOs earn on "medium- to long-term contracts that generate stable earnings" (tanshin, May 11, 2026);
  logistics is forwarding and contract logistics. All are understood in the same sense; none decides.
- **VERDICT: IN**, narrowly, on the economics of the deciding part (Liner Trade through ONE): a commodity carrier whose
  competitive position and kind of earning power can be stated, though its ten-year freight rate cannot; Q2 decides whether
  that matters **[M2012-065]**, **[M2011-014]**.
