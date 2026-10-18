# Company Run — Ameren Corporation (NYSE: AEE) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run** under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the brief's one stated
departure: the lines of evidence are chosen by the analyst from the 10-K's Item 1, Item 1A and Item 7 (listed below under
Step 0), and the competitors are taken from the 10-K (it names none that file; see Q2).

**Quotation marks.** Double quotes beside a bold id are the ledger row's own words; single quotes (‘ ’) mark the
filings' words.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-18, after the run was committed: `PORTFOLIO.md` read for AEE only; not held.*

**CONTAMINATION, declared as found.** (1) The session context opened with the repository's recent commit subjects, which
name another company's v5 re-run (LNT, Alliant Energy) closing OUT at Q7 "on the floor and above the top of the range",
with one-line summaries of its Q3, Q4, Q5 and Q6 weighings. That is another utility's run of record, seen by accident; it
was not opened and is not used. Because it is a peer of this name, I did not use Alliant as a competitor in Q2, so that no
figure here could be borrowed from that run. (2) The session's memory index carries one-line notes on the queue (wave
counts, "nothing buyable" among gate-clearers); no line names this company. Not used. No `Test Runs/` file, holding
review, `PORTFOLIO.md` or register file was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $106.08 (close 2026-10-16; Yahoo chart feed through `tools/sources.py`; **aggregator, flagged per operator
  rule 5**, live quote only).
- **Shares by class** from the latest filing's cover: **276,843,251** common, $0.01 par, as of July 30, 2026 (10-Q for
  the quarter ended June 30, 2026, filed 2026-08-03, accession `0001002910-26-000023`). `Screens/cover_shares.py AEE`
  parsed no count ("read the filing by hand"); the count above is read from the cover by hand. Cross-checks: the 10-Q
  balance sheet shows 276.8 million outstanding at June 30, 2026, and the balance sheet tags issued shares equal to
  outstanding (276.800M issued, `tools/run.py`): no treasury stock. One class only (Union Electric's 102,123,834 and
  Ameren Illinois' 25,452,373 shares are held by Ameren). After the 10-Q: no 8-K reports a share issuance; the 8-K of
  2026-08-04 (accession `0001104659-26-090493`) raises the at-the-market program by $2.0 billion. **Unsettled forward
  sales** (10-Q Note 4): 16.0 million shares at June 30, 2026 (cash of $1.6 billion on physical settlement) plus 1.4
  million entered in July 2026 at an initial $112.62. These are not outstanding and are not counted in the share base;
  their effect is shown at Q7.
- **Market cap:** 276.843M x $106.08 = **$29,368M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, 30-year par yield, US Treasury daily par yield curve,
  10/16/2026 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-18, accession `0001002910-26-000009` (Item 1, Item
  1A, Item 7, the statements, Notes 2, 5, 12, 14 and 16 in the parts cited); 10-Q for Q2 2026, filed 2026-08-03,
  accession `0001002910-26-000023` (balance sheet, cash flows, Note 4); proxy statement DEF 14A filed 2026-03-31,
  accession `0001104659-26-037756` (compensation discussion, summary compensation, pay ratio, ownership); 10-K for FY2022
  (accession `0001002910-23-000053`) and FY2020 (accession `0001002910-21-000065`) for segment earnings and sales
  volumes 2018 to 2022; 8-Ks of 2025-10-03, 2025-10-14, 2025-12-15, 2026-02-09, 2026-06-26, 2026-06-29, 2026-08-04,
  2026-08-24, 2026-09-18 and 2026-09-28 (accessions in the research folder's notes).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025,
  $3,353M, on the filed Consolidated Statement of Cash Flows (10-K, `0001002910-26-000009`) equals the XBRL figure
  `tools/run.py` printed. Capital expenditures $4,128M and depreciation and amortization $1,612M also agree.
- `python tools/run.py AEE` arithmetic lines only (USD millions):

  | FY | OCF | SBC | D&A | capex | OCF-SBC-capex | OCF-SBC-D&A |
  |---|---|---|---|---|---|---|
  | 2021 | 1,661 | 22 | 1,219 | 2,954 | -1,315 | 420 |
  | 2022 | 2,263 | 24 | 1,438 | 3,351 | -1,112 | 801 |
  | 2023 | 2,564 | 26 | 1,432 | 3,597 | -1,059 | 1,106 |
  | 2024 | 2,763 | 28 | 1,524 | 4,319 | -1,584 | 1,211 |
  | 2025 | 3,353 | 28 | 1,612 | 4,128 | -803 | 1,713 |
  | 5-yr mean | | | | | **-1,175** | **1,050** |

  (2021 and 2022 from the XBRL facts of their 10-Ks, `peers_facts.txt` in the research folder; `tools/run.py` gives a
  five-year capex-basis mean of -1,280 on its own vintage choice; the difference is the 2021 figures' vintage and does
  not change any conclusion below.) Stock pay is resolved: $28M in 2025, the only stock-pay line found; other capital
  payments are $5M a year of dividends to minority holders of subsidiary preferred stock. No securities inside operating
  cash, no finance-lease principal line, no acquisitions in the window (the $600M Split Rail Solar purchase of February
  2026 is a construction project, inside capex in 2026).

**Lines of evidence chosen, and from where** (the brief's departure): from **Item 1**: the four segments, the rate orders
in force with allowed returns, equity ratios and rate bases (the table of rate orders), the regulatory structure by state
and the resource plan; from **Item 1A**: regulatory lag and disallowance, the size of the capital program and its funding,
the holding-company structure, distributed generation and data-center load; from **Item 7**: segment earnings, the rate
cases of 2024 to 2026, the 2026 to 2030 capital plan ($30.5 to $33.1 billion), liquidity and the at-the-market and forward
equity program, the statement that cash used for capital expenditures and dividends will exceed operating cash ‘over the
next several years’ (10-Q, Outlook), cash taxes and tax-credit sales, the Rush Island Clean Air Act litigation (Note 14).
Added from the older 10-Ks: segment earnings 2018 to 2022 and electric sales volumes 2018 to 2025, so the comparisons
cover the span.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: "if you have to actually do it on — with pencil and
paper, it’s too close to think about" **[M1996-084]**, and the rows tie the margin to the certainty: "the more
volatile the business is — or possibility is — but assuming you still want invest in it, the larger the margin of
safety" **[M1997-080]**. A share is a business **[M1997-109]**: the question is what the owner of all of Ameren gets
out of it in cash, not what the next buyer pays for a dividend stream. No macro enters **[M2000-094]**: the rate at
which this business is valued is the long Treasury rate of the day, not a forecast of rates. Who is paid to tell you
**[M2020-037]**: the 10-K and proxy feature rate-base growth and earnings-per-share growth, which are what a utility is
paid on; the owner's figure is cash after the capital that growth requires. **Contrary evidence, written down as found**
**[M1997-127]**: (a) the regulated return is real and was earned: book return on average equity has sat at 10.1% to
11.4% every year from 2018 to 2025 (Q3), which argues the business is understood and dependable; (b) against the buyer,
the company has issued shares every year since 2018 and says it will keep doing so ‘through at least 2030’ (10-Q,
`0001002910-26-000023`), and its operating cash has not covered its capital spending in any year of the decade
(Step 0), so the dividend is paid out of a business that raises outside money each year.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin, provided it is bought with the buyer's own money and sized so that a
fall of half does not force a sale: "you don’t want to put yourself in a position where you have to sell" **[M2020-007]**;
"Never risk permanent loss of capital." **[L2023-005]**. The target's own leverage is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**; the chemistry need not be understood if "the economic dynamics of
  the industry" are **[M2011-014]**. The economic dynamics here are written in the rate orders: Ameren earns a return
  set by three regulators on a rate base it builds (10-K Item 1, table of rate orders: Ameren Illinois electric
  distribution 8.72% allowed on 50% equity; Illinois gas 9.60%; FERC transmission 10.48% on 55% to 60% equity; Missouri
  orders ‘did not specify an ROE’; Missouri's pending case asks 10.25% on a $16.7 billion rate base, 8-K of 2026-06-26).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the rate base, which the company
  publishes five years ahead ($30.5 to $33.1 billion of capital spending 2026 to 2030, Item 7); (2) the allowed and
  earned return, which the rows say a utility is "almost certain of earning", "if you behave yourself" **[M2010-037]**;
  (3) the money needed to build the rate base, which the 10-Q says will exceed operating cash ‘over the next several
  years’. Each is knowable from the filings and the orders, and the insiders do write the forecast down **[M2000-105]**:
  Ameren files a five-year Smart Energy Plan and a resource plan to 2045 with its Missouri regulator (8-K of 2026-09-28).
- **What could make ten years unforeseeable.** The resource mix will change (coal retired by 2042; 1,500 MW of new
  nuclear by 2040; data-center load of 2.9 to 3.9 GW by 2030 in the 2026 plan), and the regulators' treatment of it is
  the risk the 2023 letter names: in "a few states" "it is difficult to project both earnings and asset values in what
  was once regarded as among the most stable industries in America" **[L2023-011]**. Missouri and Illinois are not named
  there, and the 10-K's risk factors carry no wildfire liability of the kind that row describes (a search of the 10-K for
  ‘wildfire’ finds two passing mentions in lists of weather and industry risks). The change is in what is built, not in
  the economics of how it is paid for: the speakers' own utility answer is that regulators "give us a fair return on the
  assets employed, and we will get that return whatever the assets may be" **[M2008-024]**. Doubt is applied to the
  perimeter **[M2002-092]**, and I hold the doubt on the regulator, not on the business; that doubt belongs to Q2's
  castle tests, where the routing of the framework puts it.
- **Routing:** no fast-changing technology closes this at Q1; a utility holding company is read by its parts, and every
  part is a rate-regulated wires, pipes or generation business of the same kind.
- **VERDICT: IN.** The ten-year economics are a regulated return on a published and growing rate base, foreseeable from
  the filings and orders **[M2000-037]**, **[M2012-065]**, **[M2010-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The castle.** A franchise by law: Ameren Missouri and Ameren Illinois deliver electricity and gas in service
  territories where no rival may string wires or lay mains, and Ameren Illinois is the ‘provider of last resort’ for
  customers who buy power elsewhere (10-K Item 1). The rows name the type: "a natural franchise because of surface
  capabilities" among the sources of a moat **[M1995-037]**, and of their own utilities, "offering monopoly service in
  most cases" **[L2009-011]**.
- **The attacker with money** **[M2011-015]**: no one can build a second distribution network in St. Louis or central
  Illinois; the money test passes for delivery. It does not pass for supply in Illinois, where customers may buy power
  from ‘an alternative retail electric supplier’ (Ameren Illinois procured power for only 28% of its delivered
  kilowatthours in 2025, 10-K Item 1), but Ameren Illinois owns no generation and earns on delivery, so supply choice
  does not touch its earnings (‘do not affect Ameren Illinois Electric Distribution’s earnings’, Item 1). For new
  data-center load the 10-K names ‘increased competition among utilities, independent power producers and non-traditional
  market entrants’ (Item 1A).
- **Pricing power and the agony before a rise** **[M2005-020]**: every price rise is a filed case before a commission
  that can cut it. Evidence: Missouri retail revenue per kilowatthour rose from 9.41 cents (2018: $3,173M on 33,718
  million kWh, FY2020 10-K) to 11.70 cents (2025: $3,719M on 31,796 million kWh, FY2025 10-K), about 24% over seven
  years, through an inflation that the price did not outrun. The commissions cut what is asked: the ICC's November 2025
  gas order removed ‘$75 million of planned distribution and transmission capital investments’ from the test year, and
  the Illinois electric distribution return was set at 8.72%, which Ameren is appealing (10-K Item 7). The prayer session
  here is a statutory proceeding.
- **Unit volume** **[M1999-054]**: total electric sales 80,468 million kWh in 2018 (including off-system sales), 71,907
  in 2020, 69,416 in 2025; Missouri retail load 33,718 (2018), 30,630 (2020), 31,796 (2025). Flat to down over the span;
  the 2026 plan forecasts large-load growth that has not yet appeared in the volumes (2.2 GW of signed large-load
  service agreements, February 2026).
- **The low-cost position** **[M2018-043]**: the 10-K presents its residential rates against an industry average from
  the Edison Electric Institute (Item 7 overview chart, note (g)); the chart's figures are not in the stripped text and
  are not used. No claim is made here.
- **Ask the competitors** **[M1999-130]**: no instance of a named rival in the 10-K (a sweep of every sentence containing
  ‘compet’ finds MISO transmission bids, data-center competition and pay; no company is named).
- **Widening or narrowing** **[M1999-108]**: on the regulatory side, narrowing in Illinois (an 8.72% allowed return on
  electric distribution under the 2024 to 2027 multi-year plan; an October 2024 FERC order reducing the base return on
  transmission and requiring refunds, 10-K Item 7) and widening in Missouri (the 2025 Missouri law allows construction
  work in progress in rate base for new gas generation and future test years for gas, Item 7). The earned return held
  through both (Q3).
- **What could destroy, modify or reduce it** **[M2000-014]**: a regulator that stops allowing a fair return, the case
  the 2023 letter narrates **[L2023-011]**; generation stranded "because of rank foolishness", which commissions "will be
  less inclined" to let into rate base **[M2017-094]**; customer generation and storage, which the 10-K calls ‘increasingly
  cost-competitive’ (Item 1A) and which the 2015 letter says "may eventually erode the economics of the incumbent
  utility, particularly if it is a high-cost operator" **[L2015-007]**.
- **The competitor row** (CONVENTION of this run: the 10-K names no rival that files; I take three regulated utility
  holding companies that file with the SEC and operate in the same or the adjacent regional market: **Evergy** (Missouri
  and Kansas, CIK 0001711269), **WEC Energy** (Wisconsin, MISO, CIK 0000783325) and **Xcel Energy** (MISO and SPP, CIK
  0000072903); rationale: the same regulated product in the same wholesale market is the nearest comparison the filings
  allow; Alliant was set aside for the contamination reason stated above). Figures from each company's own XBRL facts in
  its 10-Ks, 2016 to 2025 (`peers_facts.txt`, `peers_table.txt` in the research folder):

  | 2016-2025 | AEE | EVRG | WEC | XEL |
  |---|---|---|---|---|
  | mean net income / average equity | 10.3% | 8.1% | 12.0% | 10.4% |
  | mean net income / net plant | 3.31% | 3.37% | 4.70% | 3.41% |
  | capex / D&A, cumulative | 2.50 | 2.10 | 2.29 | 2.53 |
  | operating cash - stock pay - capex, cumulative ($M) | -7,248 | -1,586 | +635 | -17,980 |
  | common stock issued, cumulative ($M) | 2,452 | 113 | 925 | 6,839 |

  Flags: Evergy's figures before 2018 are Great Plains Energy's, and its 2018 return reflects the merger; WEC's capex for
  2018 to 2025 is its "PaymentsToAcquireOtherPropertyPlantAndEquipment" line (its utility capital expenditures, without
  its purchases of renewable-project stakes), and its equity for 2019 to 2025 includes a small noncontrolling interest;
  WEC's 2018 and 2019 returns are missing for want of a tagged 2018 equity figure. Ameren's 2017 return (7.3%) carries
  the 2017 federal tax-reform charge.
- **The parts table** (section B):

  | part | net income 2021-2025 ($M) | share of the four parts | castle | decides |
  |---|---|---|---|---|
  | Ameren Missouri | 2,931 | 46.7% | franchise, regulated, bundled generation | yes, the largest |
  | Ameren Transmission | 1,527 | 24.4% | franchise, FERC formula rates | no |
  | Ameren Illinois Electric Distribution | 1,140 | 18.2% | franchise, ICC multi-year plan | no |
  | Ameren Illinois Natural Gas | 672 | 10.7% | franchise, ICC future test year | no |

  Segment net income from Note 16 of the FY2025 10-K (2023 to 2025) and of the FY2022 10-K (2021 and 2022); the
  segments report net income, not operating profit, and that is the figure used (the parent's loss, -416 over the five
  years, is outside the parts; on the company's total of 5,854, Ameren Missouri is 50.1%). No part carries more than half
  of the four parts' total, so the largest, Ameren Missouri, decides; all four parts have the same kind of castle.
- **The field's returns over the last full cycle** (section C): the framework's list of what Q2 rules OUT excepts a return set by a regulator from the
  ordinary-returns OUT and carries it to Q3 as a second best (Q2, What it rules OUT; the rows it rests on are quoted
  next). The field's returns are what a regulator allows: 8% to 12% on book
  equity, about 3.3% to 4.7% on net plant, for all four companies across the decade. The speakers' words for it: "The
  whole idea behind the utility industry is not to allow extraordinary profits" **[M2000-131]**; "there’s no way we get
  rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]**; "the opportunity to deploy
  large sums at fair returns" **[L2005-005]**. The castle protects a fair return and the right to invest more at it; it
  does not protect an excellent return. That is carried to Q3, as the exception directs.
- **Judgment.** The castle is standing on the evidence of the decade: the franchise is legal and exclusive, the earned
  return held through the Illinois cut and the FERC refund order, and no attacker can duplicate the wires. Its future
  depends on the regulators' continued fairness, the bet the speakers name for their own utilities: "the bet we are
  making is that regulatory authorities will treat us fairly in the future" **[M2014-087]**; Ameren has two regulators in its larger part and a record
  of appeals against one of them, which is a weight, not a closure.
- **VERDICT: IN**, the castle standing as a regulated franchise whose return is set, not earned against rivals; the
  return is carried to Q3 as the exception directs **[M1995-037]**, **[L2009-011]**, **[M2009-104]**, **[L2009-012]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**. The capital this business needs is its plant, financed by
  debt and equity. After-tax operating earnings before interest (net income plus interest expense at the filer's
  blended statutory 26%) over average debt plus equity (`q3.py`, `q3_output.txt`): 5.3% (2017, tax-reform year), 6.9%,
  6.4%, 6.2%, 5.8%, 5.9%, 5.9%, 5.7%, 6.3% (2025); **mean 6.0%**. On the book equity alone the return is 10.1% to 11.4%
  in every year from 2018 (Q2's table). The difference is leverage: debt rose from 52% of debt plus equity (2016) to
  60% (2025). A reported return is read for "leverage" before it is credited **[L1994-009]**; "we could make it almost
  any number you want if we just used enough leverage" **[M2001-054]**. Unlevered, the business earns about the long
  government rate of the day (5.43%).
- **Reinvestment to stand still and to grow.** Capital spending was 2.5 times depreciation over 2016 to 2025 (Q2's
  table), and the company plans $30.5 to $33.1 billion for 2026 to 2030 against 2025 depreciation of $1,612M (10-K Item
  7). The 10-Q says cash used for capital spending and dividends will exceed operating cash ‘over the next several
  years’ and that new shares will be issued ‘through at least 2030’ (`0001002910-26-000023`, Outlook). The rows name the
  type: "cash-consuming businesses, by their nature, are unattractive unless the cash they consume gets to earn a
  reasonable return" **[M2012-057]**; of utilities in inflation, they "fail it because inflation places heavy capital
  requirements on them" **[L2011-019]**; and "it just keeps eating up more and more money, and your depreciation charges
  are inadequate and you’re kidding yourself as to your real economic profits" **[M2015-049]**. Part of the spending is
  compulsory (the obligation to serve, coal retirements under a resource plan, reliability standards), the kind the
  speakers avoid: "a lot of compulsory reinvestment just in order to stand still" **[M1997-016]**.
- **What the added capital earns.** After-tax operating earnings before interest rose $849M from 2020 to 2025 on
  $12,717M of added debt and equity: **6.7%**; from 2016 to 2025, $1,095M on $18,294M: **6.0%** (`q3_output.txt`). The
  speakers measure a utility's added capital this way, "by the operating earnings after depreciation", not by "the cash
  minus the increased capital investment" **[M2014-086]**. The added capital earns a regulated fair return, roughly the
  bond rate unlevered, and about 10% on the equity slice only because about 60% of it is borrowed.
- **The growth arithmetic.** Earnings per share rose because more capital went in, not because the return on it rose:
  the case the rows describe as "we’re not earning a higher rate of return on capital than we were when we started. We
  just put way more capital into the business" **[M2023-081]**.
- **Second best, named as such.** The rows accept the regulated utility: "they’re good enough" **[M2018-056]**; "there’s
  no way we get rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]**; on condition
  of "decent returns on the incremental sums they invest" **[L2009-012]**. The incremental return here is decent for a
  regulated asset and well below the floor of about ten percent that Q7 applies to a price.
- **WEIGHS AGAINST.** A cash-consuming business whose added capital earns, unlevered, about the long bond rate, and
  whose growth requires outside money every year **[M2012-057]**, **[L2011-019]**, **[M2015-049]**; the rows' second
  best, not their best **[M2018-056]**, **[L2009-012]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (`tools/run.py` table, first-
  filed XBRL vintages, read against the filed FY2025 balance sheet, `0001002910-26-000009`; USD millions):

  | year-end | total assets | net plant | equity | debt (LT + current + short-term) | retained earnings | receivables | inventory | goodwill |
  |---|---|---|---|---|---|---|---|---|
  | 2016 | 24,699 | 20,113 | 7,103 | 7,834 | 1,568 | 437 | 527 | 411 |
  | 2018 | 27,215 | 22,810 | 7,631 | 9,036 | 2,024 | 463 | 483 | 411 |
  | 2020 | 32,030 | 26,807 | 8,938 | 11,576 | 2,757 | 415 | 521 | 411 |
  | 2022 | 37,904 | 31,262 | 10,508 | 15,095 | 3,646 | 600 | 667 | 411 |
  | 2024 | 44,598 | 36,304 | 12,114 | 18,722 | 4,604 | 525 | 762 | 411 |
  | 2025 | 48,476 | 39,313 | 13,401 | 19,830 | 5,292 | 665 | 774 | 411 |

  (The other four year-ends are in `run_py_output.txt`; they lie on the same path.) What moved and why: net plant
  nearly doubled (x1.95); debt grew 2.53 times and equity 1.89 times, so the balance sheet carried more debt each year
  (52% of debt plus equity in 2016, 60% in 2025). Retained earnings rose $3,724M; the rest of the equity increase,
  about $2.6 billion, is new stock (at-the-market sales, dividend reinvestment and 401(k) plan issues, statement of
  shareholders' equity). Goodwill is fixed at $411M (about 3% of equity); there were no acquisitions. Cash is nil
  ($13M); the company runs on commercial paper and credit lines ($2.5 billion of liquidity at December 31, 2025, Item
  7). Receivables and inventory moved with revenue (receivables 7.2% of 2016 revenue, 7.6% of 2025 revenue). Below the
  line sit regulatory assets of $2,524M, regulatory liabilities of $6,255M and deferred taxes of $5,181M (2025); the
  speakers decline to count a utility's deferred tax as equity: "I don’t think I would look at that as a hidden form of
  equity" **[M2015-030]**. What the figures "don’t say and what they can’t say" **[M2025-032]**: the value of the plant
  rests on the commissions continuing to allow a return on it, which the balance sheet records as probable, not certain
  (critical accounting estimates, Item 7).
- **The real costs.** Depreciation is real and here it understates what keeps the system in place: capex ran 2.5 times
  depreciation for a decade with volumes flat (Q2), the case of "your depreciation charges are inadequate" **[M2015-049]**,
  which overrides the general use of depreciation "as a proxy for required capital expenditures" **[M1998-127]**.
  Non-cash income sits inside reported earnings: the allowance for equity funds used during construction ($88M in 2025,
  $76M in 2024, $54M in 2023) and the Missouri deferral of 85% of depreciation and a return on plant placed in service
  between rate cases (PISA, 10-K glossary and Note 2), which the 10-K credits with 17 cents of 2025 earnings per share
  (higher interest deferrals). Stock pay is small and expensed ($28M). No restructuring charges recur; the 2024 Rush
  Island charge ($59M) was a court-ordered mitigation program (Note 14). No instance of EBITDA in the 10-K, 10-Q or
  proxy (text search: zero hits).
- **Cash taxes.** The company paid no net income tax in any year of the decade (cash taxes from -$312M in 2025 to +$21M
  in 2018, XBRL IncomeTaxesPaidNet), helped by sales of production and investment tax credits ($314M in 2025, cash-flow
  supplement). These flow through operating cash; under ratemaking the deferred taxes and credits return to customers
  (Missouri's tracker for credit sales, 8-K of 2026-06-26), which is why the speakers say a utility's deferred tax "helps
  our customer and it doesn’t help us, basically" **[M2015-030]**. Carried to Q7 as a direction: owner cash at a full tax
  would be lower.
- **Coverage**, pre-tax earnings over interest **[L2012-002]**: 3.7 times in 2016 (pre-tax income $1,035M plus interest
  $382M, over $382M), 3.4 in 2023, 2.9 in 2024, 3.1 in 2025 ($1,597M plus $776M, over $776M). Falling.
- **What the accounts say of management's character.** The statements are complex (regulatory accounting) but readable
  and explained segment by segment, with the cents-per-share bridge stated net of a 26% tax rate. No tell of the list
  lives in these accounts: no prepaid or deferred accounts building out of line with the business **[M1995-064]**
  (regulatory assets grew with plant, $2,397M to $2,524M in 2025), no reserve releases, no restatement found. Two habits
  are recorded as a weighing and carried to Q5: (1) the proxy's summary features ‘weather-normalized adjusted earnings
  per share’ beside GAAP (proxy summary chart and Appendix A, ‘non-GAAP financial measures’), the practice the rows call
  "highlighting "adjusted per-share earnings"" **[L2016-006]**; (2) the company gives annual GAAP earnings guidance and
  sets the short-term incentive's target to it (proxy: ‘aligned with Ameren’s annual GAAP earnings guidance’), the
  "scourge of earnings "guidance"" **[L2019-006]**. Against both: the compensation committee adjusted 2025 earnings per
  share **downward** for pay, removing an $86M tax benefit it judged ‘not representative of 2025 performance’ (proxy,
  2025 STIP Performance Adjustments).
- **VERDICT on the accounts: WEIGHS AGAINST** (not a STOP): no confusion, no suspicion raised by the statements; earnings
  include non-cash construction and deferral income, and depreciation understates the spending that keeps the system in
  place **[M2015-049]**; the adjusted-figure and guidance habits are carried to Q5 **[L2016-006]**, **[L2019-006]**,
  **[M1994-018]**. The recast earnings feed Q7 as owner cash: operating cash less stock pay less spending, never net
  income.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Martin J. Lyons, Jr., Chairman, President and Chief Executive Officer; joined Ameren in 2001 as controller,
  chief financial officer 2009 to 2019, chairman and president of Ameren Missouri from December 2019, chief executive
  from January 2022, chairman from November 2023 (proxy, director biography). A career insider of this company. Twelve
  nominees, eleven independent, with an independent lead director (proxy). In October 2025 the chief financial officer
  moved to Group President, Ameren Utilities, and the head of Ameren Illinois became chief financial officer (8-K of
  2025-10-14, `0001104659-25-098988`); the head of Ameren Missouri retired that month (8-K of 2025-10-03).
- **The two yardsticks** **[M1994-008]**. How well they run it, given the hand dealt: the earned return on book equity
  held at 10.1% to 11.4% from 2018 through two adverse regulatory events (Q2, Q3), above Evergy's 8.1% mean and below
  WEC's 12.0% over the decade (Q2's table); the capital plan was delivered as announced ($4.1 billion in 2025 against the
  plan, proxy letter). How they treat the owners: read in the proxy and the financing record (Q6, Part B, and Part A).
- **The tells of dishonesty** (the proxy, the reports, how they talk about mistakes). The 10-K reports the bad news
  plainly: the Illinois return cut and the appeals, the FERC refund order, the turbine collapse at High Prairie in late
  2024, the Rush Island litigation and its cost. No instance found of reports that dance around the industry's key figure
  **[M2007-082]**; the cents-per-share bridge is in GAAP terms. **The one integrity fact on the record**: in January 2017
  a federal district court ruled that projects Ameren Missouri performed in 2007 and 2010 at the Rush Island coal plant
  violated the Clean Air Act; the Eighth Circuit affirmed the liability ruling and the desulfurization remedy in August
  2021; Ameren Missouri chose to retire the plant early instead (retired October 2024), was ordered in December 2024 to
  fund mitigation programs ($59M charge), and financed the plant's remaining balance by securitized bonds paid by
  customers (FY2022 10-K Note 14, `0001002910-23-000053`; FY2025 10-K Note 14 and the AMF securitization, Item 7). The
  speakers carry Kiewit's rule on character, "if they don’t have the last, be sure they don’t have the first two"
  **[M2016-033]**. I read this as a permitting dispute
  litigated for thirteen years and lost, not as deceit of owners or regulators: the record read contains no finding of
  false statement, no restatement, no regulator's finding of misconduct by the present officers, and the present chief
  executive was chief financial officer, not head of operations, when the projects were done. It is written down as
  found **[M1997-127]** and weighed; it is not, on this evidence, a doubt about honesty of the kind that closes the file.
- **The habits carried from Q4**, read with the integrity record **[M2013-088]**: annual GAAP earnings guidance and a
  short-term incentive aligned to it **[L2019-006]**; a non-GAAP ‘weather-normalized adjusted’ earnings figure featured
  in the proxy summary **[L2016-006]**. Read with the rest: the adjustment the committee actually made to the pay figure
  went against the managers ($86M of tax benefit removed, Q4); the 10-K's earnings discussion is in GAAP; no history of
  beating declared targets was assembled (a single year's guidance was not read against its result; noted as not done).
  These weigh against; they do not, read with the record, raise a doubt that closes **[M1994-018]**.
- **Love of the business.** A 25-year insider who rose through the accounts and the regulated subsidiaries; nothing in
  the filings speaks to love or money either way; for a marketable stock the after-the-sale test does not apply, and the
  reading tests carry the weight: "In terms of sizing up managements — obviously if we’re going to buy the whole
  business, that’s a different question." **[M2007-081]**.
- **Ability, what it shows in.** Facing reality in the reports **[L2000-018]** is in evidence (the 10-K states its
  losses); the regulatory record is mixed (constructive outcomes in Missouri law in 2025; an Illinois return set at
  8.72% and appealed). In a regulated monopoly the business, not the manager, carries most of the result: "If you have a
  big enough moat, you don’t need as much management" **[M1999-106]**.
- **VERDICT on integrity: IN**, the Rush Island liability ruling recorded and weighed, not closing **[M1997-127]**,
  **[M2013-088]**; **ability WEIGHS FOR, modestly**: the earned return held through adverse orders and the plan was
  delivered **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. 2021 to 2025: net income attributable to common
  $5,854M; dividends $3,319M (a payout of 57%); retained $2,535M; plus new common stock of $1,834M; so $4,369M of
  owners' money was kept or raised. Market value rose from $19,773M (253.3M shares at $78.06, 2020 year-end) to $27,601M
  (276.4M shares at $99.86, 2025 year-end; aggregator closes, flagged): $7,828M, about $1.79 per dollar kept or raised,
  so the market leg passes. The intrinsic leg, which the rows add because the market leg alone misleads **[R2009-002]**,
  fails on Q7's arithmetic: the business's value at the long rate is below its debt plus equity at book (Q7), so a dollar
  retained at a regulated 6% unlevered return is worth about a dollar at the bond rate and less at the floor. The
  forward question, "Can you keep using all of the capital you generate, effectively, for a very long time?"
  **[M2010-097]**: the company uses all of it and more, at the regulated rate.
- **Dividends while issuing shares.** The company pays out about 55% to 60% of earnings by policy (twelve consecutive
  annual increases, proxy letter) and raises new equity every year to fund the plan. The rows reject payout by ratio,
  "the idea of paying out 20 percent of your earnings, or 10 percent, or 30 percent of earnings in dividends strikes us
  as nuts" **[M2000-051]**, and the speakers' own utility, with the same capital appetite, paid "never had a penny of
  dividends" in close to 20 years **[M2019-059]**. Here part of each dividend is returned through the at-the-market
  program with fees and forward-sale costs.
- **Buybacks.** None since 2017 (repurchases $51M in 2016 and $24M in 2017, XBRL; none 2018 to 2025) and no program in
  the filings read. The no-stated-price test has nothing to read: **the bottom of Q7's range is $18.84 a share
  (all-equity; $69.86 equity-only), and no shares were bought.** (Line written back from Q7 and committed with it.)
- **Issuance and deals** **[M1995-001]**. Common stock issued in every year from 2018: $74M, $68M, $476M, $308M, $333M,
  $346M, $273M, $574M (XBRL ProceedsFromIssuanceOfCommonStock), at implied prices of roughly $67 to $88 a share
  (2020 to 2025: proceeds over the change in shares outstanding), with forward sales outstanding at $106.32 to $112.91
  (10-Q Note 4) and the at-the-market program raised by $2.0 billion in August 2026. The implied issue prices (proceeds over the
  change in shares: about $67 in 2020, $70, $77, $80, $76 and $88 in 2025, dividend-plan shares included) and the
  forward prices of $106 to $113 all sit above the top of Q7's all-equity range ($36.89); against the equity-only range
  ($69.86 to $87.91) the 2020 to 2025 prices sit inside it and the forwards above it (written back from Q7). The rows'
  test is "if you issue shares beneath that figure, you are harming your shareholders" **[M1996-013]**.
  It is serial issuance all the same, the behaviour the rows call "one of the surest indicators of a promotion-minded
  management, weak accounting, a stock that is overpriced and" worse **[L2014-015]**; the framework carries it as a
  candidate second STOP, unresolved (Q6, Part A). Here it is the utility's stated funding plan for a regulated rate base,
  disclosed in advance; I weigh it against and do not close on it. No deals; no all-stock acquisition, so the STOP on an
  all-stock deal in undervalued stock does not arise **[L2009-019]**.
- **Part B, pay tied to what the person controls** **[M2003-019]**. Short-term incentive: GAAP earnings per share,
  safety, operating and customer measures, with an individual modifier; 2025 paid 161.1% of target (proxy). Long-term:
  60% performance units on three-year total shareholder return relative to a peer group, 10% on megawatts of generation
  added and retired, 30% time-vested units (proxy). Chief executive's 2025 total compensation $14,056,510, 112 times the
  median employee's $125,070 (proxy, pay ratio). Against the rows: in a capital-intensive business the pay should
  carry "a capital cost element" **[M2009-081]**, **[L1994-019]**, and none of the measures charges for capital; earnings
  per share rises when rate base is added with outside money, so the incentive rewards the growth the owners fund. The
  relative-return units pay partly on the stock's ride against peers rather than on what the manager controls
  **[M2000-062]**. A megawatt-addition target pays for building, not for return. A clawback policy is in place and the
  committee cut the 2025 earnings figure for pay (Q4), both to its credit.
- **The board.** Chairman and chief executive combined since November 2023, with an independent lead director; the rows
  name the risk, "how hard it is to replace a mediocre CEO if that person is also Chairman" **[L2014-026]**; nothing here
  says the chief executive is mediocre. Directors must hold stock within five years, counting stock units granted, not
  shares bought by "purchasing shares with their savings" **[L2019-008]** (proxy, Director Stock Ownership Requirements). The chief executive
  beneficially owns 212,055 shares (proxy, March 16, 2026), about $22M at the price.
- **WEIGHS AGAINST.** Part A: a ratio dividend paid out of a business that re-raises equity every year, retention that
  passes only on the market leg, serial issuance (its prices above Q7's central range, so not harmful by **[M1996-013]**; the habit
  itself **[L2014-015]**); **[M2000-051]**, **[R2009-002]**. Part B: pay on earnings-per-share growth and relative return with no
  capital charge in a capital-hungry business **[M2009-081]**, **[L1994-019]**, combined chair, partly offset by the
  committee's downward adjustment and the clawback.

## Q7 — WHAT IS IT WORTH? STOP.
*(Arithmetic in `q7.py`, `q7b.py` and their outputs in the research folder. The first pass of `q7.py` was computed in
the research folder before Q3 to Q6 were written into this file; it carried no entry language and is declared under the
self-audit.)*

- **How much cash, how sure, how soon, at the long government rate** **[L2000-021]**, **[M2009-004]**. The cash
  counted is what comes out net of what must go back in **[M1998-080]**, **[M2014-068]**. Owner cash, from Q4's
  recast, never net income:
  - **All-equity basis (central):** operating cash less stock pay less spending, plus interest paid at the filer's
    blended statutory tax of 26% (CONVENTION of this run: the interest add-back uses cash interest paid, net of
    capitalized, from the cash-flow supplement, and the 26% the 10-K states for its cents-per-share bridge; rationale:
    operating cash is struck after cash interest, and the filer's own blended rate is the only rate the filing gives).
  - **The maintenance guess** **[M2000-144]**, **[L1999-024]**: the filing states no maintenance figure; depreciation is
    used, the proxy the rows allow **[M1998-127]**, flagged as generous because for a utility "your depreciation charges
    are inadequate" **[M2015-049]**. Growth spending is capex less depreciation, $2,224.8M a year on the 2021 to 2025
    means ($3,669.8M less $1,445.0M).

  | USD M | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
  |---|---|---|---|---|---|---|
  | owner cash after maintenance, all-equity | 735 | 1,153 | 1,510 | 1,663 | 2,272 | **1,467** |
  | owner cash after all spending, all-equity | -1,000 | -760 | -655 | -1,132 | -244 | -758 |
  | owner cash after maintenance, equity-only | 420 | 801 | 1,106 | 1,211 | 1,713 | 1,050 |
  | owner cash after all spending, equity-only | -1,315 | -1,112 | -1,059 | -1,584 | -803 | -1,175 |

- **The specifics applied.** (a) **Cycle base:** the first window year, 2021, is depressed on the filer's own
  description (the ‘extremely cold weather in mid-February 2021’ raised gas costs, deferred and collected over 18 months
  from April 2021, FY2022 10-K, Liquidity, quoted from the filing). Because the collection fell in 2021 and 2022, both
  inside the window, the five-year mean nets it out; only the growth end-points are distorted. The mean is kept as the
  base, and growth is not read from the 2021 end-point (below). (b) **Decline:** none in the maintenance series; the
  all-spending series is negative in every year and is carried beside, not as an end (see (e)). (c) **Acquisitions:**
  none in the window. (d) **Working capital:** inside operating cash, which is used as filed. (e) **Growth spending:**
  the central case is owner cash after maintenance; the growth case charges the growth spending each year for ten years
  and credits the growth it bought, at the incremental return Q3 measured on added debt plus equity, 6.68% (2020 to 2025;
  5.98% over 2016 to 2025 shown beside), so owner cash rises by that return on each year's growth spending; after year
  ten no growth and no growth spending. (f) **The cap:** the literal shown growth of the maintenance series, 32.6% a year
  (2021 to 2025; 27.7% between the window's halves), carried ten years would need owner cash of $24.6 billion against a
  best share of sales of 25.8% (2025): absurd, so the literal rate is not carried. The growth credited in (e) compounds
  to 7.25% a year over the ten years (owner cash $2,953M in year ten), inside the shown rate, and needs about 15% of
  sales at the shown sales growth: no cut is triggered. **The mechanical alternative**, the sales-growth cut of (f)
  (8.31% shown, cut to the 5.43% discount rate) applied while the growth spending is still charged, gives a lower growth
  case ($11.04 a share, all-equity); it is shown beside and not used, because (e) says ‘Never charge all spending and
  also cap the growth that spending bought’ (the framework's own words, Q7, six more specifics; single-quoted as not
  a ledger row). After year ten: zero
  nominal growth.
- **Whose tax** **[M1994-004]**, **[L2002-020]**: owner cash is after the company's own tax as paid, which was about
  nil for the decade (Q4: tax-credit sales and deferred taxes). The framework's statutory-rate convention is written for
  carryforwards or credits that run out inside ten years; part of Ameren's shelter is of that kind (credit carryforwards
  $178M and loss carryforwards $165M at 2025, 10-K Item 7; credit sales $314M in 2025) and part is deferred tax that
  ratemaking returns to customers **[M2015-030]**. Recomputing at the statutory rate would lower every figure below; it
  is not done, because every case already fails the floor (CONVENTION of this run, confessed: the more generous tax
  basis is kept where the stricter one cannot change the box).
- **Net debt** (all-equity basis): at June 30, 2026, current maturities $1,524M plus long-term debt $19,064M plus
  short-term debt $1,220M less cash $12M = **$21,796M** (10-Q balance sheet, `0001002910-26-000023`); operating leases
  left out; no finance-lease line found. The 10-Q's stated subsequent event is the July 2026 forward sale of 1.4M
  shares (not settled, no cash yet). Later debt issues ($400M Ameren Illinois bonds, 8-K of 2026-08-24; $900M junior
  subordinated notes, 8-K of 2026-09-18) are not in a filed balance sheet and are not added. Enterprise value at the
  price: $29,368M plus $21,796M = $51,164M.

- **The range, all-equity, at the long rate 5.43%** (USD M; per share after net debt, 276.843M shares):

  | case | value | per share |
  |---|---|---|
  | no growth, owner cash after maintenance ($1,467M a year) | 27,011 | **$18.84** |
  | growth bought by the growth spending, at 6.68% incremental return | 32,008 | **$36.89** |
  | beside: the same at 5.98% | 29,722 | $28.63 |
  | beside: the mechanical (f)-capped growth case, spending charged | 24,851 | $11.04 |
  | beside: all spending deducted, no growth ($-758M a year) | -13,962 | negative |
  | beside: forward sales settled (17.4M more shares, $1.76B less debt), no-growth and growth cases | | $23.70 to $40.68 |

  **Value range: $18.84 to $36.89 a share (all-equity) against $106.08.** The growth case is the top because the
  growth spending earns 6.68% against a discount rate of 5.43%, so it adds a little value at the long rate. Width 1.96 to
  one. **Equity-only, beside:** no growth $69.86, growth case $87.91 (`q7_output.txt`, `q7b_output.txt`; the equity-only
  growth case charges the full growth spending against owner cash after interest and credits the unlevered incremental
  return, which flatters it).
- **The floor, tested first** (about ten percent pre-tax, after the company's own tax). The return each case earns at
  the price (the rate that equates the case's cash to what is paid): all-equity, no growth **2.87%**, growth case
  **3.93%** (on enterprise value of $51,164M); equity-only, no growth 3.58%, growth case 4.85% (on the market value of
  $29,368M). For the no-growth case to earn ten percent on enterprise value, owner cash before interest would have to be
  $5,116M a year; the five-year mean is $1,467M and the best year $2,272M. **No case earns the floor at the price**; the
  price is above the top of the range on both bases. "there’s just a point at which we drop out of the game" **[M2003-149]**;
  a price above the top closes OUT however wide the range (Q7, the four specifics).
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two
  averaged, after the company's own tax. **All-equity (central): no positive fair price**: the no-growth end is worth
  $14,667M and the growth end $11,042M at ten percent, both below net debt of $21,796M (per share $-25.75 and $-38.85,
  average $-32.30). **Equity-only, beside: $31.39** (ends $37.93 and $24.84). The central figure is the all-equity one.
  No cheap price is reported.
- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case **[M2003-149]**: the regulated return on
  added capital, about 6% to 7% unlevered (Q3), cannot carry an enterprise value of about $51 billion to ten percent
  **[L2000-021]**, **[M1996-025]**. The range is narrow (under two to one), so the box is not TOO HARD **[L2000-025]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). The bond comparison is recorded under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts recorded under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts recorded under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**, the floor: value range **$18.84 to $36.89 a share on the all-equity basis** (equity-only $69.86 to
$87.91) against **$106.08** (close 2026-10-16, aggregator); no case earns about ten percent at the price (2.87% to
3.93% on enterprise value). Q1 IN, Q2 IN (a regulated franchise, its return carried to Q3), Q3 weighs against, Q4 weighs
against, Q5 integrity IN with ability weighing for modestly, Q6 weighs against. Re-look condition: the alert at the top
of the computed range, as for any OUT (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury yields 5.43% (US Treasury, 10/16/2026). The cases in Q7 return 2.87% to 3.93%
  at the price on the all-equity basis and 3.58% to 4.85% on the equity-only basis.
- **Q9 (debt and exposures).** Debt was 60% of debt plus equity at 2025 year-end (52% in 2016); pre-tax interest
  coverage 3.1 times in 2025, down from 3.7 in 2016 (Q4). Total debt $21.8 billion at June 30, 2026, including $1,220M
  of short-term debt; credit agreements of $3.2 billion through December 2030, subject to a 364-day repayment term for
  Ameren Missouri and Ameren Illinois (10-Q, Liquidity). Ameren is a holding company whose dividends and debt service
  depend on distributions from its subsidiaries (10-K Item 1A). After the quarter: $900M of junior subordinated notes due
  2057 (8-K of 2026-09-18) and $400M of Ameren Illinois first mortgage bonds (8-K of 2026-08-24). Planned capital spending
  of $30.5 to $33.1 billion for 2026 to 2030 is to be funded by debt and equity (10-K Item 7; 10-Q Outlook). The
  acquisition criterion "little or no debt" is stated for whole businesses **[R1997-001]**; this business would not meet
  it. Earnings come from two states and three regulators, four segments (Q2's parts table).
- **Q12.** Coal supplied 56.5% of Ameren Missouri's energy in 2025 (10-K Item 1, operating statistics); the Rush Island
  plant was retired early after a federal court found Clean Air Act violations (Q5). None of the businesses Q12 names
  (casinos, tobacco, loading schemes, gambling dressed as investing) is present.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      **Departures, declared:** (1) the first full write replaced the template's body after Q2, and the template's
      later headings were rebuilt in order as each question closed (Q3 onward appended one section at a time, each
      committed); (2) the Q7 arithmetic (`q7.py`) was first computed in the research folder after the Q2 commit and
      before Q3 to Q6 were written; it bore no entry language, but its result leaked into one sentence of Q6 committed
      before Q7 (Part A, the retention test's intrinsic leg: ‘fails on Q7's arithmetic’), which should have waited for
      the write-back; the sentence is true of the Q7 now committed and is left as written; (3) the Q6 buyback and issuance
      lines were committed as placeholders and written back with Q7, as the brief requires.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (not touched here); the run is folded into the register by the dispatcher (operator rule ten). A run not
      in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen
      by accident (another utility's commit subjects, the memory index) is declared under contamination and not used.
- [x] Every v5 id resolves (`check_run.py` in the research folder: every M, L and R id found in `principle_ledger_v5.csv`,
      every double-quoted fragment beside an id found in a cited row, no E-ids); every filing fact has its accession.
      Single quotes mark filing text, as stated at the top.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (US Treasury); the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: the steady earned return (for the business),
      the serial issuance and the cash shortfall (against), the Rush Island ruling (Q5).
- [x] No row dated after the anchor is cited in a point-in-time run (this is a run of today; not applicable).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 text and verdict-like lines were ignored.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specifics (e) and (f) of Q7 conflict for a business whose growth is bought by heavy spending.** (f) cuts an absurd
shown growth to the business's sales growth, capped at the discount rate; (e) says never charge the spending and also cap
the growth it bought. For a utility both trigger at once: the literal growth (32.6%) is absurd, and the growth spending
is charged. Applied mechanically, the cut and the charge together give $11.04 a share, a case (e) forbids. I credited
the growth case with the growth the spending bought at the incremental return Q3 measured (6.68%), which needs no cut,
and showed the mechanical figure beside. The text should say which specific governs when both apply. (2) **The
maintenance guess for a utility.** The rows allow depreciation as the proxy **[M1998-127]** and say a utility's
depreciation is inadequate **[M2015-049]**; the filing gives no maintenance figure. The framework's (e) asks for the
maintenance case ‘where the filing allows the guess’ and says nothing of what to use when the rows themselves call the
usual guess too low. I used depreciation, flagged as generous; a stricter guess only lowers the range. (3) **Whose tax,
for a regulated company.** The statutory-rate convention is written for carryforwards and credits that run out; a
utility's low cash tax is mostly deferred tax and credit sales that ratemaking passes to customers **[M2015-030]**. The
framework has no rule for that case, and none for the tax rate on the interest add-back of the all-equity basis when
the company pays no cash tax; I used the filer's blended 26% and kept the as-paid tax, both confessed. (4) **The
equity-only growth case** is ill-defined: growth spending in a utility is about 60% debt-funded, so charging all of it
against owner cash after interest, while crediting the unlevered return, mixes bases; the figure is shown beside, as the
text says, and flatters. (5) **Serial issuance** stays a candidate STOP (Q6, Part A); for a utility whose issuance is
its announced funding plan the framework gives no guidance on whether the rows' "hell-bent on issuing shares" reaches it.
(6) **The competitor row** needs a CONVENTION whenever a 10-K names no rival, which is the normal case for a regulated
monopoly; the framework could say that peer utilities in the same wholesale market are the default.
