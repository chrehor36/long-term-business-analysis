# Company Run: STAK Inc. (Nasdaq: STAK), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form as the
template gives it; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns
OUT or TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before
any fetch (commit 6541265e).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for STAK).

**Dispatch.** Dispatched blind analyst under the brief of 2026-10-16 (canonical brief, with its one stated departure: the
lines of evidence derived by the analyst from the 20-F's Items 4.B, 3.D and 5). Pathspec commits after each question.

**Contamination, declared and not used.** (1) At the start of the run a listing of `Test Runs/` (to confirm no file of this
name existed) showed the names of eighteen other run files and research folders dated 2026-10-16 (CTBG, ENYN, HMH, INVX,
IOGPQ, JUTOY, KGS, LSE, NESR, NGS, NOA, NOV, OIS, OMSE, PED, RCON, SEI, USAC). None was opened. (2) The session's opening
context showed the last five commit subjects of the repository, three of them the fold of a run on LSE Leishen Energy: OUT
at Q2, a part sold by tender to PRC state oil buyers, "the RMB 2.06%", and "the one SEC-filing rival Recon losing money every
year". I did not use them: the RMB rate below is read from the Ministry of Finance page today, and Recon's record is read from
its own XBRL filings. The choice of Recon as this run's rival (Q2) is my own, but I cannot show it was not prompted by that
subject line, so I say so. (3) The operator's memory index shown at session start carries queue-state lines; none names STAK.
No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened, listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.03, close 2026-10-15 (Yahoo Finance chart via `tools/sources.py`; **aggregator, live quote only**, flagged
  per operator rule 5). The 2026-10-16 intraday print was $1.02 on 8,180 shares at 13:52 UTC; the prior full close is used.
  The record of the quote over the year is itself a fact (carried under AFTER THE STOP, Q5): $0.29 on 2026-02-05, $1.01 on
  2026-03-27, $5.13 on 2026-06-08 (the day of the U.S. power-unit MOU), a high of $9.27 on 2026-07-24 on 67.1 million shares,
  $1.14 on 2026-09-15.
- **Shares by class.** `python Screens/cover_shares.py STAK`: 13,210,349 Class A ordinary shares on the cover of the 20-F filed
  2025-11-05 (accession 0001493152-25-020818). Read against the filing: that figure is the whole issued count, 4,010,349 Class
  A plus 9,200,000 Class B (20-F Item 4.A: "an aggregate of 4,010,349 Class A Ordinary Shares with one vote each and 9,200,000
  Class B Ordinary Shares with 30 votes each"); the same two counts stand on the unaudited balance sheet at 2025-12-31 (6-K
  2026-05-13, accession 0001493152-26-022709). No treasury shares are shown: the 9,200,000 Class A shares repurchased in June
  2025 were exchanged for the Class B shares (6-K 2025-06-13, accession 0001641172-25-014950). After the last annual report:
  6,000,000 Class A shares issued on 2026-01-08 in a registered direct offering of units at $0.38, each unit with one and a half
  warrants (6-K 2026-01-08, accession 0001493152-26-000966; 424B4 2026-01-05, accession 0001493152-26-000242). The
  2026-10-09 reorganization reduces par to $0.0000001 and raises the authorized capital to 750,000,000,000 Class A and
  250,000,000,000 Class B shares; the notice states it "will not change the number of issued and outstanding class A ordinary"
  shares (6-K 2026-09-15 Ex. 99.2, accession 0001493152-26-042746; results 6-K 2026-10-09, accession 0001493152-26-046433).
  **Count used: 10,010,349 Class A + 9,200,000 Class B = 19,210,349 shares.** Charter note: "Each Class B Ordinary Share is
  convertible into one Class A Ordinary share at any time by the holder thereof" (20-F, Item 3.D, risk factor on the dual class structure), so both
  classes are counted at the Class A price. Beside it, not in the count: 9,000,000 warrants at $0.46 (exercisable from the
  second anniversary of 2026-01-08, three-year term) and 70,517 representative's warrants at $4.80; fully exercised, 28,280,866
  shares.
- **Market cap:** 19,210,349 x $1.03 = **$19.8M**.
- **Earnings currency and sovereign.** Reporting currency USD; "The functional currency of subsidiaries located in China is
  the Chinese Renminbi" (20-F, Note 2(d)). The earnings currency is the RMB. Sovereign: **2.06%**, 30-year, MOF-China Government
  Bond Yield Curve, 2026-10-16, page published under "Copyright: Ministry of Finance of the People's Republic of China"
  (yield.chinabond.com.cn, czb moreInfo page, fetched 2026-10-16). The issuing authority's own curve; `tools/sources.py`
  covers USD, JPY and EUR only. (`tools/run.py` printed the US Treasury 5.43%; not used, wrong currency.)
- **Filings read** (operator rule 4): 20-F for the year ended 2025-06-30 (filed 2025-11-05, 0001493152-25-020818; Items 3.D,
  4.A, 4.B, 5.A, 5.B, 6, 10.B, and the audited statements with Notes 1, 2, 12, 13, 16); **no 20-F for the year ended
  2026-06-30 is on EDGAR as of 2026-10-16** (submissions list fetched today; latest filing the 6-K of 2026-10-09; the NT 20-F
  of 2025 shows the last annual report came late); 6-Ks of 2025-05-13, 2025-06-13, 2025-10-17, 2026-01-08, 2026-04-14,
  2026-05-13 (unaudited first half of fiscal 2026 with statements), 2026-06-08, 2026-09-15, 2026-10-09; F-1 filed 2024-11-15
  (0001493152-24-046238; FY2024 and FY2023 statements, industry overview); F-1/A 2025-12-30 (0001493152-25-029497); 424B4s
  2025-02-26 (0001493152-25-008310) and 2026-01-05; DRS 2024-01-18 (0001493152-24-002860; FY2023 and FY2022 statements).
  Auditor HTL International, LLC, Houston, "since 2023". **Cross-check:** `tools/run.py` operating cash FY2025 -2.9 (USD M)
  against the filed statement, "Net cash used in operating activities | $ (2,878,901)": agrees.
- **`python tools/run.py STAK`, arithmetic lines only.** OCF FY2023 -1.5, FY2024 -2.7, FY2025 -2.9; SBC FY2025 3.9;
  capex 2.5, 0.0, 0.1; D&A 0.3 each year; "OE capex" -4.1, -2.8, -6.8. **The tool misses one line:** the filed cash-flow
  statement carries "Purchases of intangible assets (1,991,345)" in FY2025 and (73,343) in FY2023 beside the PP&E line, and
  the tool's capex column omits them, so its FY2025 figure is understated by $2.0M. The figures below are by hand from the
  filed statements.
- **Owner cash after every real cost, by year (USD M, by hand from the filings).** All spending deducted (PP&E and
  intangibles), stock pay deducted:

| FY (June) | Operating cash | Stock pay | PP&E | Intangibles | **Owner cash** | Interest paid | Loans to third parties, net (beside) | Source |
|---|---|---|---|---|---|---|---|---|
| 2022 | +0.149 continuing; -0.782 discontinued | 0 | investing -0.077 in total | (in investing) | **-0.710** | n/f | n/f | DRS 0001493152-24-002860 |
| 2023 | -1.530 | 0 | -2.522 | -0.073 | **-4.126** | 0.053 | -0.360 | 20-F 2025 |
| 2024 | -2.735 | 0 | -0.017 | 0 | **-2.753** | 0.121 | -0.256 | 20-F 2025 |
| 2025 | -2.879 | -3.906 | -0.062 | -1.991 | **-8.838** | 0.183 | -0.387 | 20-F 2025 |
| H1 FY2026 (unaudited) | +0.667 | 0 | 0 (disposal +0.506 not counted) | 0 | **+0.667** | 0.106 | -0.473 | 6-K 0001493152-26-022709 |

  Four-year mean FY2022 to FY2025: **-$4.11M a year**; three audited years FY2023 to FY2025: -$5.24M. The depreciation variant
  (operating cash less stock pay less D&A) is -1.86, -3.07, -7.11 for FY2023 to FY2025, negative every year as well. Operating
  cash already contains income tax accrued but not paid: "Income taxes paid" was $3,773, $3,058 and nil in FY2023 to FY2025
  (and nil in H1 FY2026) against an income tax payable that rose from $251,759 (2022) to $1,967,290 (2025-12-31).

**The balance sheets, read in Step 0 because the file closes before Q4** **[M2025-032]** (USD; DRS, F-1, 20-F, 6-K):

| Date | Total assets | Cash | Receivables | Inventory | Inventory / that year's revenue | PP&E | Intangibles | Short-term + long-term borrowings | Income tax payable | Equity | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022-06-30 | 7.83M | 0.03M | 0.85M | 3.20M | 39% (rev 8.13M) | 2.92M | 0 | 0.22M | 0.25M | 1.28M | 0.73M |
| 2023-06-30 | 15.00M | 0.59M | 4.02M | 6.18M | 29% (21.15M) | 2.90M | 0.07M | 1.45M | 1.06M | 8.12M | 3.84M |
| 2024-06-30 | 18.78M | 0.66M | 3.49M | 8.28M | 44% (18.92M) | 2.58M | 0.06M | 4.45M | 1.67M | 10.58M | 6.04M |
| 2025-06-30 | 26.75M | 1.02M | 1.99M | 17.02M | 68% (24.91M) | 0.29M | 2.02M | 6.06M | 1.69M | 12.90M | 0.32M |
| 2025-12-31 | 29.34M | 1.92M | 2.98M | 18.31M | (half year 19.23M) | 0.27M | 2.00M | 8.00M | 1.97M | 14.96M | 2.14M |

What moved and why: only four year-ends exist (operations began June 2020), so the eight to ten years the row asks for cannot
be read and the shortfall is itself the finding. Equity rose from $1.28M to $14.96M, of which paid-in capital supplied $3.66M
of shareholder contributions (FY2023), $4.19M of IPO proceeds (FY2025) and $3.91M of stock pay credited to capital, so the
equity growth is mostly money put in, not money earned and kept. Inventory rose from $3.2M to $18.3M, faster than revenue
($8.1M to an annual $24.9M), and by June 2025 stood at 68% of the year's revenue; the filer says the $8.6M build in FY2025 was
"materials for volume production and finished goods that we capitalized on the depressed material prices to lock in favorable
costs" (20-F Item 5.B). Borrowings rose from $0.22M to $8.00M, all but $0.43M short-term, against cash of $1.92M; the
2025-12-31 figure includes $1.54M of payables "reclassified into supplier finance obligations" (6-K cash-flow statement,
non-cash). PP&E fell from $2.58M to $0.29M in FY2025 with a $1.54M "loss from sale of property and equipment of $1.5 million
due to relocation of production factory" (20-F Item 5.A). Receivables fell in FY2025 after a $1.10M "loss from sale of
accounts receivable" to "accelerate cash consideration collection" (Item 5.A). Income tax payable built every year while cash
taxes were near nil. What the figures cannot say: whether the inventory is saleable at cost, and whether the tax payable will
be paid or forgiven; both are carried under AFTER THE STOP.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**. The quote has run from $0.29 to $9.27 and back to $1.03 inside eight months; the market "just tells us prices"
**[M2006-077]**, and nothing in that path is read as information about the business. Margin of safety is the attitude carried
to Q7: "if you have to actually do it on [...] with pencil and paper, it’s too close to think about" **[M1996-084]**. No macro
enters: the oil price and PRC oilfield spending are not forecast here. Who is paid to tell you: the industry figures in the
F-1 are from a consultant engaged for the prospectus ("cited from the industry report issued by Beijing Bo Yan Zhishang
Information Advise Co., Ltd", F-1 Industry Overview), so they are read as the seller's material and not relied on.
**Contrary evidence, written down as found** **[M1997-127]**: operating income was positive in FY2023 and FY2024 ($3.63M and
$2.80M) and the first half of FY2026 ($2.11M); operating cash turned positive in H1 FY2026 (+$0.67M, unaudited); revenue grew
from $8.1M (FY2022) to $24.9M (FY2025) and $19.2M in the first half of FY2026 (+13.4%). Against: operating cash negative in
every audited year; inventory 68% of revenue; taxes accrued and unpaid; borrowings up from $0.2M to $8.0M; equity growth
mostly paid in; the filer's own statement that permit-holding rivals "have a pricing advantage compared to us" (Q2).

## THE STANDING RULE
The buyer's conduct: a purchase of this name would be paid for in cash, without borrowing, at a size whose total loss would not
touch what the buyer has and needs **[M2012-081]**, **[L2023-005]**; nothing in the run asks for leverage, margin or an option
written. On that condition the rule is met; whether the target itself could be lost entirely is Q9's weighing, and its facts
are recorded below.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** It designs oilfield work equipment (workover rigs, fracturing, cementing, oil
  extraction, boiler and well-washing units) and has "qualified specialized vehicle manufacturing companies" mount it on truck
  chassis, because "we do not possess the qualifications for manufacturing specialized vehicles" (20-F Item 4.B). It sells to
  dealers, "who are the dealers and resell the products to end-users, oilfield service companies", against a deposit, with
  delivery in "three to six months" (Item 4.B). FY2025 revenue $24.9M: equipment $11.95M, vehicles $10.91M, automation
  services $1.76M, other $0.29M (Item 5.A); one reportable segment (Note 2(x)); all revenue in the PRC.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, **[M2000-037]**; the product may be opaque so long as "I
  understand the economic dynamics of the industry. Is there [...] are there competitive moats? Is there ease of entry?"
  **[M2011-014]**. The key variables **[M1998-044]**: (1) what PRC oilfield service companies spend on work vehicles; (2) the
  price STAK can get against rivals who hold the manufacturing permit; (3) whether the profit it books comes out as cash. None
  is a fast-changing technology: the products are diesel trucks carrying pumps, rigs and boilers, built to the 2023 revision
  of a 2005 industry standard (QC/T 739, Item 4.B). The commodity-price exposure is not by itself a STOP here: the speakers
  "don’t think we can predict commodity prices" **[M2016-025]** and decide "off the figures" **[M2008-069]**; the cost position
  is read at Q2 **[M2006-004]**, **[M2009-059]**.
- **Do the past statements tell me the future ones?** **[M2008-033]**. Partly: three audited years and two earlier reported
  periods, enough to see how the business converts profit to cash and how its prices move, which is what Q2 needs.
- **Contrary evidence for this question, written down** **[M1997-127]**: the business began in June 2020 and the speakers say
  "Start-ups are not our game." **[L2007-015]**; the doubt row says that a doubt about the circle means it is outside
  **[M2002-092]**. Weighed: the filer has filed revenues from FY2022 and audited statements from FY2023, a product whose economics
  are those of an equipment assembler selling through dealers, and the figures needed to judge its position exist; I do not
  doubt that I understand what moves its economics. What I cannot do is foresee that STAK will hold a place in its field, and
  that is Q2's question: "Q1 asks whether the economics and position can be foreseen at all; Q2 asks what the foresight shows
  about the castle" (the framework's reading under Q1, The order).
- **Routing.** Not a business whose industry changes fast (Q1 TOO HARD would route it); not a financial institution; not a
  holding company of parts that decide differently (one segment).
- **VERDICT: IN**, narrowly. The economics are an equipment assembler's and can be read from the filed figures **[M2011-014]**,
  **[M2008-069]**; the start-up row **[L2007-015]** is carried as the strongest pull the other way.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence, and why these** (the brief's departure: chosen by me from Items 4.B, 3.D and 5). (1) The products that
make the money: equipment and vehicles, $22.86M of $24.91M of FY2025 revenue (Item 5.A), because the castle must be found
there or nowhere. (2) The permit and the contract manufacturers (Items 4.B, 3.D), because they decide who is the low-cost
producer. (3) The price and the gross margin over the span (Item 5.A, 6-K of 2026-05-13), the pricing-power test. (4) The
customers, dealers, and their turnover (Item 4.B; Note 16), the low-bid test. (5) Whether profit comes out as cash (Item 5.B),
the field-returns test, with the rival's filings beside it.

- **The castle questions: what keeps it standing, and how permanent?** **[M1995-038]**. The filer names its advantages as
  "Independent Research and Development Capabilities", a "One-Stop Service Business Model" and "Rapid Response to Customer and
  Market Demands" (F-1 Competitive Advantages, 0001493152-24-046238), and in the same section its challenges: "Lack of Special
  Vehicle Production Permission" and "Competition from Established Competitors - The traditional oilfield equipment industry is
  highly competitive, with strong and well-established competitors." The advantages named are things a rival can match; none is
  a reason the customer cannot go elsewhere. The speakers buy barriers and do not build them **[M2012-105]**; this one is six
  years old and still being built.
- **The low-cost position.** The filer, in its own risk factor: "Some of our potential competitors may have special vehicles
  manufacture permits, and therefore, they can design and manufacture oil pumping trucks by themselves, and have a pricing
  advantage compared to us" (20-F Item 3.D). Its trucks are assembled by two permit-holding manufacturers under framework
  agreements "which will end on December 31, 2025" (Item 4.B; Baolu Auto Industrial (Shiyan) and Yizhuan Auto, exhibits 10.1
  and 10.2); no renewal is stated in any filing read. By its own account STAK is not the low-cost producer and depends on
  manufacturers who could be its rivals. "commodity businesses have risk unless you’re the low-cost producer, because the
  low-cost producer can put you out of business" **[M1997-010]**; "being the low-cost producer is all-important" **[L2000-017]**;
  "the guy with the lower cost comes in and kills you" **[M2001-013]**.
- **The attacker with money.** "The oilfield maintenance industry is intensely competitive and includes thousands of
  companies both domestically and internationally" (Item 3.D). The business was itself started in 2020 by a team that
  "shifted its focus" from automation modules and relocated to Changzhou under a local-government investment agreement (Item
  4.B), and reached $21M of revenue in its third year: the evidence is that entry is easy. Could a rival with money take it on?
  The filing's own account of how STAK entered says yes **[M2011-015]**; "there are some industries that are just never going
  to have barriers to entry" **[M2012-106]**.
- **Pricing power, and the agony before a rise** **[M2005-020]**. Gross margin 31.97% (FY2023), 29.99% (FY2024), 30.86%
  (FY2025), 27.24% (H1 FY2026). The filer's reasons: in FY2024 "the adoption of competitive pricing approaches starting from
  2023" (Item 5.A); in H1 FY2026 "our promotional sales policy to expand the market" (6-K 2026-05-13). Price is cut to win
  volume; no price rise is recorded in any period read.
- **Would the customer still choose it over the low bid?** **[M2017-009]**. The customers are dealers who resell to oilfield
  service companies, and the large ones change every year: the 10% customers were D, H and I in FY2023, A, B and D in FY2024,
  A, B and C in FY2025 (Note 16). No filing records a customer paying more to stay.
- **Ask the competitors** **[M1999-130]**: not possible from the public record; no rival's view of STAK is on file.
- **Widening or narrowing; what could destroy it.** The permit gap is not closing: the plan to "independently apply for
  specialized vehicle qualifications" or obtain them "through mergers and acquisitions" (F-1 Growth Strategy) is not reported as
  done in the 20-F. The June 2026 MOU for a 60% U.S. subsidiary selling gas-to-electricity units for "AI data centers" (6-K
  2026-06-08) is a new line outside the castle examined, not evidence for it.
- **The competitor row.** The 20-F and the prospectuses name no rival (searched for "competitor", "competition" and rival names;
  the F-1 Industry Overview gives market sizes only). **CONVENTION of this run:** the rival is Recon Technology, Ltd (Nasdaq
  RCON, CIK 1442620, a 20-F filer), whose 20-F describes "integrated automation services to Chinese petroleum companies at
  oilfields within China" with CNPC its largest customer (20-F FY2026, 0001104659-26-112415); rationale: it is the only
  SEC-filing supplier to the same PRC oilfield customers that I know of; the contamination note above applies to this choice.
  Rivals that do not file with the SEC, flagged and not read: Yantai Jereh Oilfield Services (Shenzhen) and Honghua Group (Hong
  Kong), my naming, not the filer's.

| Company | Metric | Span | Record | Source |
|---|---|---|---|---|
| STAK | operating income (loss), USD M | FY2023 to FY2025, H1 FY2026 | +3.63, +2.80, -3.13 (+0.78 before stock pay), +2.11 | 20-F 0001493152-25-020818; 6-K 0001493152-26-022709 |
| STAK | operating cash, USD M | FY2022 to FY2025, H1 FY2026 | -0.63 (incl. discontinued), -1.53, -2.74, -2.88, +0.67 | DRS 0001493152-24-002860; 20-F; 6-K |
| Recon | operating income (loss), RMB M | FY2012 to FY2026 | -3.5, -0.6, +2.8, -35.5, -39.9, -30.6, -40.9, -24.2, -20.2, -61.6, -82.3, -69.3, -71.6, -57.3, -41.2: a loss in 14 of 15 years | Recon 20-F XBRL, accessions 0001144204-13-052662 to 0001104659-26-112415 |
| Recon | operating cash, RMB M | FY2012, 2013, 2016 to 2026 | -21.7, +24.8, -0.3, +5.7, -21.1, -32.2, -5.2, -34.1, -26.2, -51.7, -43.7, -33.8, -58.8: negative in 11 of 13 years filed | same |

- **The parts table.** One reportable segment (Note 2(x)). By revenue line (FY2024, the last year whose gross profit by line I
  read): equipment $2.98M of gross profit, vehicles $1.52M, automation $0.80M, other $0.37M, of $5.67M (Item 5.A). Equipment
  and vehicles together carry 79% and decide; they are the castle tested above. Automation services ($1.76M of revenue in
  FY2025) is the part nearest Recon's business, and the filer is "not expecting to achieve such growth in service income from
  automation solutions continuously" (Item 5.A).
- **The field's returns over the last full cycle.** The rival over fifteen years has lost money at the operating line in
  fourteen and consumed cash in eleven of thirteen; STAK has reported operating profit in three of its four full periods and
  produced no operating cash in any audited year. The field's returns, as the filings show them, are below ordinary; a moat
  that "protects excellent returns on invested capital" **[L2007-004]** is not in evidence, and "you can have only two
  competitors and they’re still terrible businesses" **[M2013-052]**. The span is short for STAK (four periods, one rising
  oil-service market); the conclusion rests on the filer's own statements about its cost position, not on the span.
- **What the rows ask, answered.** The castle is shown open on the filer's own evidence: it is not the low-cost producer and
  says so, it cuts price to sell, its large customers rotate, entry is easy (it entered in 2020), and the field's one
  SEC-filing rival loses money year after year. This is not a castle whose future cannot be judged (which would be TOO HARD,
  **[M2000-019]**); it is one the filing shows to be open: "If the answer had been yes, we wouldn’t have done it."
  **[M2011-015]**
- **VERDICT: OUT.** The castle is open on the evidence: by its own statement the filer is not the low-cost producer in a
  competitive equipment field **[M1997-010]**, **[L2000-017]**, prices are cut to win volume **[M2005-020]**, and the field's
  returns are below ordinary **[L2007-004]**, **[M2013-052]**. The run closes here; Q3 to Q12 are NOT REACHED.

## Q3 to Q10, Q12: NOT REACHED
Closed at Q2 (operator rule 2). Nothing below is a clearance.

---
## THE BOX
**OUT at Q2**: the castle is open on the filer's own evidence (not the low-cost producer in a field of "thousands of
companies", price cut to sell, customers rotating, the one SEC-filing rival losing money in fourteen of fifteen years);
integrity facts recorded, not judged. COMPUTATION, NOT A CLEARANCE: no case of the range has a positive value; no case earns
the floor at $1.03; fair price not positive.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found, not weighed, each with its source **[M1997-127]**; the box is unchanged.

**Bearing on Q3 (capital):**
- Operating cash was negative in every audited year (FY2023 -$1.53M, FY2024 -$2.74M, FY2025 -$2.88M) while operating income
  was positive in two of them (20-F 0001493152-25-020818). Inventory grew from $3.20M (2022) to $18.31M (2025-12-31), 68% of
  FY2025 revenue at June 2025 (DRS; 20-F; 6-K 0001493152-26-022709).
- Of the rise in equity from $1.28M (2022) to $14.96M (2025-12-31), $11.76M was paid in (shareholder contributions $3.66M in
  FY2023, IPO net $4.19M, stock pay credited $3.91M) (20-F cash-flow and equity statements).
- PP&E fell from $2.58M to $0.29M in FY2025 with a $1.54M loss on sale "due to relocation of production factory" (Item 5.A);
  the F-1 Growth Strategy had planned "to build our own production facilities" (F-1 0001493152-24-046238).

**Bearing on Q4 (the accounts):**
- Income tax expense of $715,040 (FY2023) and $276,189 (FY2024); "Income taxes paid" $3,773, $3,058 and nil (FY2023 to
  FY2025) and nil in H1 FY2026; income tax payable $251,759 (2022) rising to $1,967,290 (2025-12-31) (DRS; 20-F; 6-K).
- At 2025-06-30, 79% of gross receivables were owed by Customers E (44%), F (19%) and G (16%), none of whom was a 10% revenue
  customer in FY2023, FY2024 or FY2025; at 2024-06-30, 85% was owed by Customer D (Note 16).
- A $1,097,204 "loss from sale of accounts receivable" in FY2025, "to accelerate cash consideration collection" (Item 5.A);
  $1,544,173 of payables reclassified "into supplier finance obligations" in H1 FY2026 (6-K cash-flow statement, non-cash).
- "Loans to third parties" paid out each year while borrowing: $599,689 (FY2023), $553,649 (FY2024), $989,999 (FY2025),
  $640,072 (H1 FY2026), against collections of $239,876, $297,863, $602,969 and $167,036 (20-F; 6-K). The borrowers are
  described only as "independent third parties" (Item 5.B); not further identified in what I read.
- Patents bought on 2025-01-24 "with a total consideration of $2,000,000" (Note 7), a month before the IPO; the seller is not
  named in what I read.
- Stock pay of $3,906,000 in FY2025: 1,800,000 RSUs granted 2025-04-22 "to certain consultants and management" "with no
  vesting conditions" (Note 12), two months after an IPO of 1,410,349 shares.
- No adjusted earnings figure or EBITDA is featured in the releases read; no guidance found.
- `tools/run.py` omits the intangible-asset purchases from its capex column (Step 0).

**Bearing on Q5 (integrity facts recorded, not judged):**
- Control: the chairman and CEO holds 7,700,000 Class B shares through Lanying Capital Ltd, which after the June 2025 exchange
  "would control 82.5% of the votes" (6-K 0001641172-25-014950; 20-F Item 6.E, share ownership note (2)); on 2026-10-09 the Class A holders approved
  raising each Class B share from thirty to one hundred votes (6-K 0001493152-26-046433).
- The authorized capital raised on 2026-10-09 to 750,000,000,000 Class A and 250,000,000,000 Class B shares, against
  19,210,349 issued (same 6-K).
- The quote: $3.63 at the IPO close (2025-02-27), $0.40 at 2025-12-31, units sold at $0.38 with one and a half warrants on
  2026-01-08, $0.29 on 2026-02-05, $5.13 on 2026-06-08, the day of the release announcing a "proposed U.S. subsidiary" for
  "AI-Ready Distributed Power Solutions" under an MOU "subject to the execution of definitive agreements" (6-K
  0001493152-26-027712), $9.27 on 2026-07-24 on 67.1 million shares, $1.03 on 2026-10-15 (aggregator). No 6-K reporting a
  definitive agreement for that subsidiary was found in the EDGAR list through 2026-10-16.
- The Nasdaq bid-price deficiency notice of 2025-10-15 and the regained compliance of 2026-04-13 (6-Ks 2025-10-17 and
  2026-04-14); the 20-F for FY2025 was filed after an NT 20-F (0001493152-25-020318).
- The taxes accrued and not paid, the receivables owed by non-revenue customers, and the loans to unnamed third parties, under
  Q4 above.

**Bearing on Q6 (the money and the owners):** the IPO of February 2025 ($5.6M gross at $4.00), the January 2026 offering
($2.3M gross at $0.38, 6,000,000 shares and 9,000,000 warrants at $0.46), the RSU grant of 1,800,000 shares, and an authorized
capital raised ten-thousandfold: shares issued rose from 10,000,000 (2024) to 19,210,349 in under two years, with 9,070,517
more under warrants (20-F; 6-Ks). No dividend; no buyback programme (the June 2025 repurchase was an exchange of Class A for
Class B shares).

**Bearing on Q9 (debt and exposures):** borrowings $8.00M at 2025-12-31, $7.57M of them short-term, against cash of $1.92M
(6-K); three patents pledged for a bank loan of "approximately $0.7 million" (Item 4.B); 62% of FY2025 revenue from three
customers (Item 4.B); "net assets restricted" in the PRC subsidiaries of $5,035,159 (20-F, restricted net assets note).

**Bearing on Q12:** oilfield work equipment; nothing in the named businesses.

---
## COMPUTATION, NOT A CLEARANCE (Q7, after the STOP)
Built by Q7's range convention, the floor tested first, all figures from Step 0 (script `calc.py` in the research folder).
- **Base.** Owner cash after every real cost, the years filed: FY2022 -0.710, FY2023 -4.126, FY2024 -2.753, FY2025 -8.838
  (USD M); only four years exist, so the average is of four, not five. Mean **-$4.11M** (before interest, the all-equity
  basis: -$4.02M). Specific (a): no year is aberrational on the filer's own description; FY2025 carries the RSU grant and the
  patent purchase, both real costs; without FY2025 the mean of FY2022 to FY2024 is still -$2.53M. Specific (d): working
  capital is inside operating cash, as counted. Specific (e): the filing allows no maintenance guess separate from growth
  spending (capital spending other than the patents and the FY2023 plant was under $0.07M a year); all spending is deducted.
- **Growth.** Specific (b): the series is negative in every year and more negative in the second half of the window (-5.80
  against -2.42); a growth rate of a negative series is meaningless, so the range is the no-growth case alone, said so.
- **Value range (the owner's reporting figure):** the no-growth case on -$4.02M a year has no positive value: at the RMB
  sovereign of 2.06%, -$195M for the business, less net debt of $3.87M, **-$10.35 a share**. The range is below zero on
  every case the convention builds. The literal window is the same four years.
- **Net debt** (all-equity basis): borrowings $7.998M (short-term $7.569M, which includes the supplier finance obligations,
  plus long-term $0.429M) less cash $1.923M at 2025-12-31 = $6.074M; less the January 2026 offering's net proceeds of about
  $2.2M (its own 6-K, after that balance-sheet date) = **$3.87M**. Operating leases left out (right-of-use asset $47,843).
  The income tax payable of $1.97M is not counted as debt; it would add to it if it is paid.
- **The floor, tested first.** No case earns the floor at the price. The convention's cases are negative. The most favourable
  figure in any filing, the unaudited first half of FY2026 doubled (owner cash $1.33M a year after interest, $1.55M before),
  would return 6.5% on the all-equity basis (against $19.79M of market value plus $3.87M of net debt) and 6.7% on the equity
  alone at $1.03, below about ten percent **[M2003-149]**. Closes OUT on the floor; the width test is not reached.
- **Fair price (the owner's reporting figure; Part VII; each end case valued at ten percent, the two averaged):** both ends
  are the same no-growth case; at ten percent, -$40.2M for the business less $3.87M of net debt = **-$2.29 a share,
  all-equity: not positive**. Equity-only beside it (owner cash after interest, -$4.11M a year, at ten percent, against the
  equity alone): -$41.1M, -$2.14 a share: not positive. Tax: the company's own; owner cash already reflects tax as accrued,
  and cash taxes were near nil, so the figures overstate owner cash by whatever part of the $1.97M payable is eventually paid.
  The central figure is the all-equity one. No cheap price is reported.
- Q6's buyback line: no buyback programme exists; nothing to write back.
- **Research pass:** not applicable; the box is OUT, not TOO HARD (WORK).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (6541265e); written question by question; committed after each (ae3dc34e Q1,
      70755cd3 Q2, this close).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is held by the dispatching session (not checked
      by me). The run binds nothing until folded into the register by the dispatcher.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, with one exception declared: a
      directory listing of `Test Runs/` at the start, which showed other runs' file names, and the commit subjects shown in
      the session context. Declared under Contamination; not used, with the Recon choice flagged.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `check_ids.py` in the research folder); every filing fact
      carries its accession or its document; numbers are from filings or labelled.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the computation is headed as such.
- [x] Owner cash after every real cost, by hand from the cash-flow statements (stock pay and intangible purchases deducted),
      never a net-income proxy; sovereign from the Ministry of Finance of the PRC, dated; aggregator quote flagged.
- [x] Contrary evidence written down as found (Foundations; Q1); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used, and one of them (capex) was found short and replaced by hand.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the reply).
- Honest gaps: the eight to ten years of balance sheets do not exist (four year-ends); the FY2026 20-F is not filed, so the
  last full year is FY2025 and the latest half is unaudited; the rival is mine, not the filer's, and only one rival files
  with the SEC; the identities of the third-party borrowers, Customers E to G and the patent seller were not found; I read
  Recon's figures from its XBRL and its business description from its FY2026 20-F, not its full accounts.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) Q7's range convention has no stated output for a base that is negative in every year: specific (b) says
"where that too is meaningless the range is the no-growth case alone", but the no-growth case of a negative stream is a
negative perpetuity (here -$195M at 2.06% for a company with $15M of book equity), which is not a value anyone would pay or
receive, since an owner would stop the losses or wind the business up. I reported the arithmetic as the convention builds it,
labelled not positive, and did not substitute a liquidation value, which the framework does not name; a line saying what a
run reports when every case is negative (for example "no positive value; the fair price is not reported") would make the
reporting figures comparable across such names. (2) The floor test says "no case in the range earns the floor"; it does not
say whether a figure outside the convention's window (here an unaudited half-year, doubled) may be tested as a case. I tested
it only as the most favourable figure in the filings, beside the range, to show the close does not depend on the window; the
text could say whether that is allowed. (3) The template's Q4 asks for eight to ten years of balance sheets **[M2025-032]**,
and Q1's start-up row **[L2007-015]** gives no age; for a company with four year-ends, neither says whether the missing years
are themselves a reason to close (Q1 TOO HARD) or only a gap to record. I recorded the gap and passed Q1 narrowly; another
analyst could close the same file at Q1 on the start-up row, and the box would be different though the outcome would not.
