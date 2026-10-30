# Company Run — Lonking Holdings Limited (HKEX: 3339; OTC: LONKF) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (LONKF; also searched for Lonking and 3339, no match); not held.*

**Resume note.** The template was copied to this file by an earlier cycle that a usage limit killed at 09:18 today, before
any fetch; this session (dispatched, resumed 10:16) filled it in place. Nothing had been fetched or written before.

**Contamination declared (seen by accident, not used).** (1) The session's opening git snapshot printed recent commit
subjects: "Overnight log: LONKF skipped, run file fresh" (no content about the business) and three subjects of another
company's run (KMTUY, Komatsu) that state that run's box and figures, including segment margins quoted for Caterpillar and
Deere and "China share lost to domestic makers". That run is about a different company in the same industry; none of its
figures or judgments is used here, and no Komatsu, Caterpillar or Deere figure enters this file. (2) The same snapshot
listed untracked research folders of other names (AYI, ARCB and others); none was opened. (3) The session memory index
carries lines on the queue and the portfolio in general terms; none names this company, and nothing in it is used.
No blind-listed file was opened, listed or searched.

**Lines of evidence (chosen by the analyst, as the brief directs).** From the Annual Report 2025 (AR2025): the MD&A's
product and geographic review (pp. 8-14), the Directors' Report's principal risks and uncertainties (pp. 26-27), connected
transactions (pp. 24-25), the corporate governance deviations (pp. 28-30), and notes 4 (segments), 5, 15, 17, 19, 22, 25,
27, 37 and 40. Chosen lines: product lines and margins over the cycle; customers, dealers and receivables (including the
dealer repurchase loans); pricing through the 2021 cost rise and the 2012-15 and 2022-24 downturns; the finance-lease arm;
acquisitions and goodwill (none found); debt, bills and recourse; buybacks (none, 2014 to H1 2026); pay; the controlling
holders and related-party dealings; litigation (no instance found by a search of AR2025 for "litigation" and "legal
proceeding"); the financial-investment book.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** HKD 3.04, Hong Kong close of 3339 on 2026-10-13 (Yahoo Finance chart API, symbol 3339.HK, an aggregator,
  flagged per operator rule 5). OTC LONKF: USD 0.39, last trade 2026-10-12 (same aggregator, flagged; thin).
- **Currency.** Earnings are in RMB, the quote in HKD. Rate used: **HKD 1 = RMB 0.85753**, the RMB central parity rate
  for HKD/CNY published by the China Foreign Exchange Trade System for the People's Bank of China, 2026-10-13 09:15
  (chinamoney.com.cn `ccpr.json`). Price in RMB: 3.04 x 0.85753 = **RMB 2.6069**. (The aggregator's market cross the same
  day was 0.8524; the parity is the issuing authority's figure and is used.)
- **Shares:** 4,280,100,000 ordinary shares of HKD 0.10, treasury shares nil (Monthly Return of Equity Issuer for the month
  ended 30 September 2026, HKEXnews 2026-10-06, file 2026100600233); the same count at 31 December 2025 (AR2025, Financial
  Highlights) and at 30 June 2026 (Interim Report 2026). One class. `Screens/cover_shares.py LONKF` returned "NOT AN SEC
  REGISTRANT in the live ticker file"; the count is taken from the filed return, checked against issued shares less
  treasury shares (nil).
- **Market cap:** 4,280.1m x HKD 3.04 = **HKD 13,011.5m = RMB 11,157.8m**.
- **Sovereign for the earnings currency:** **2.069%**, the 30-year point of the ChinaBond Government Bond Yield Curve (YTM),
  2026-10-13, from China Central Depository & Clearing (yield.chinabond.com.cn, curve id 2c9081e50a2f9606010a3068cae70001).
  ChinaBond is the curve the Ministry of Finance publishes through CCDC; the 30-year tenor is used (the 10-year point the
  same day: 1.665%).
- **Filings read** (operator rule 4; HKEXnews, Lonking Holdings Limited, stock code 3339; no accession numbers exist, so
  each document is recorded by title, filing date and HKEXnews file number): Annual Report 2025 (2026-04-30, 2026043004262);
  Interim Report 2026 (2026-09-30, 2026093002403); Annual Reports 2024 (2025043003981), 2023 (2024042503879), 2022
  (2023042700075), 2021 (2022042502068), 2020 (2021042602008), 2019 (2020042900081), 2018 (ltn201904293590), 2017
  (ltn201804251484), 2016 (ltn201704241557), 2015 (ltn20160422467), 2014 (ltn20150424558), 2013 (ltn20140424880), 2012
  (ltn20130423385), 2010 (ltn20110414797); Monthly Return September 2026 (2026100600233); Clarification Announcement on the
  Annual Report 2025 (2026-07-03, 2026070301709: a water-consumption unit in the ESG report, nothing financial); AGM poll
  results 28 May 2026 (2026052801733: final dividend HKD 0.20 "will be distributed on or before 31 July 2026"); the
  continuing connected transaction announcements of 2026-01-01 and 2026-01-21 (2026010100045, 2026012100631); the
  discloseable transaction on wealth management products of 2025-05-02 (2025050202999). Hong Kong has no proxy statement;
  pay and holdings are read from the Directors' Report and note 8.
- **One figure cross-checked against the filed statement:** revenue 2025 RMB 11,215,184k appears identically in the
  Financial Highlights (p. 3), the MD&A (p. 9, "RMB11,215 million"), the consolidated statement of profit or loss (p. 68)
  and segment note 4 (p. 107). Net profit 2025 RMB 1,300,748k (p. 68) equals the five-year summary (p. 160).
- `tools/run.py LONKF`: returned "not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE"; no arithmetic lines were
  produced, so the arithmetic below is the analyst's own from the filed statements, shown in
  `Test Runs/_research 2026-10-13 LONKF/scripts/lonkf_calc.py` (every input is a filed figure with its report named).

**Owner cash after every real cost, by year (RMB m).** Owner cash = cash generated from operations (after working capital,
before interest) less income tax paid less purchases of property, plant and equipment; interest received and paid are left
out on the all-equity basis and added back on the equity-only basis. Never a net-income proxy. No stock-based pay exists
("At no time during the year was the Company ... a party to any arrangements to enable the directors of the Company to
acquire benefits by means of the acquisition of shares", AR2025 p. 22; no share option scheme in the monthly return).

| Year | Revenue | Gross margin | Machinery segment result (margin) | Net profit | Owner cash, all-equity | Owner cash, after net interest | Capex | Depreciation |
|---|---|---|---|---|---|---|---|---|
| 2010 | 12,020 | n.r. | n.r. | n.r. | -740 | -806 | 509 | 204 |
| 2011 | 12,721 | n.r. | n.r. | 1,730 | 216 | 16 | 1,055 | 284 |
| 2012 | 7,896 | n.r. | n.r. | 152 | 483 | 241 | 559 | 329 |
| 2013 | 8,158 | 23.6% | n.r. | 480 | 1,315 | 1,104 | 242 | 357 |
| 2014 | 7,427 | 25.5% | 724 (9.8%) | 417 | 1,823 | 1,679 | 105 | 392 |
| 2015 | 4,829 | 22.8% | 84 (1.7%) | 117 | 1,613 | 1,534 | 70 | 390 |
| 2016 | 5,146 | 24.2% | 308 (6.0%) | 462 | 1,912 | 1,912 | 27 | 380 |
| 2017 | 8,994 | 26.6% | 1,228 (13.7%) | 1,046 | 1,394 | 1,589 | 170 | 354 |
| 2018 | 11,868 | 23.0% | 1,431 (12.1%) | 1,144 | 373 | 438 | 349 | 347 |
| 2019 | 11,744 | 23.9% | 1,483 (12.6%) | 1,643 | 1,240 | 1,330 | 197 | 344 |
| 2020 | 12,880 | 23.4% | 1,647 (12.8%) | 1,959 | 661 | 764 | 290 | 335 |
| 2021 | 13,691 | 17.9% | 1,183 (8.6%) | 1,275 | -104 | 26 | 382 | 286 |
| 2022 | 11,150 | 16.7% | 627 (5.6%) | 400 | 1,515 | 1,599 | 239 | 271 |
| 2023 | 10,523 | 17.5% | 800 (7.6%) | 645 | 1,698 | 1,754 | 187 | 269 |
| 2024 | 10,214 | 19.6% | 1,042 (10.2%) | 1,018 | 1,164 | 1,261 | 83 | 253 |
| 2025 | 11,215 | 21.4% | 1,309 (11.7%) | 1,301 | 1,057 | 1,180 | 62 | 234 |
| H1 2026 | 6,658 | 21.55% | n.r. | 773 | (operating cash flow 491) | | 75 | |

(n.r. = not read for this run. Each year from the latest report that prints it. 2009: owner cash 34. Segment result is
note 4's "sale of construction machinery" result, pre-tax and before interest income.)

- **Five-year average (literal window 2021-2025):** RMB 1,065.9m all-equity; 1,163.9m after net interest.
- **Last full cycle of the owner-cash series** (trough 2010 to the next trough 2021, the years 2010-2020): RMB 935.2m.
  The literal window opens on 2021, the series' trough in the filings read, a year in which, in the filer's words, "the Group’s operating revenue reached a record high" and raw material prices
  rose sharply (AR2021), with the working-capital build that goes with it; Q7 specific (a) would set the base on the full cycle.
- **Capex against depreciation:** over 2010-2020, capex RMB 3,573m against depreciation RMB 3,715m (about level); over
  2021-2025, capex RMB 953m against depreciation RMB 1,312m. The depreciation variant: cycle average RMB 922.3m, window
  average RMB 994.1m.
- **Stock pay:** none. **Acquisitions:** none in the window ("There was no major acquisition and disposal of subsidiaries
  and associated companies during the year", AR2025 p. 25); no goodwill or intangible line on any balance sheet read.

**The balance sheets, 2014 to 30 June 2026, read before the income account** **[M2025-032]** (RMB m; year-end; read
here because the file closes before Q4).

| Year-end | Cash | Pledged dep. | Time dep. | Fin. investments | Borrowings | Net financial assets | Total equity | Operating capital (equity less net fin.) | Inventory | Trade & bills rec. | LT rec. | Trade & bills pay. | PPE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2014 | 1,089 | 2,358 | 0 | 300 | 4,281 | -534 | 7,029 | 7,563 | 1,796 | 2,354 | 87 | 869 | 3,264 |
| 2015 | 1,146 | 2,424 | 0 | 1,466 | 4,365 | 671 | 6,624 | 5,953 | 1,281 | 1,931 | 115 | 684 | 2,829 |
| 2016 | 1,131 | 2,468 | 0 | 847 | 2,151 | 2,294 | 6,720 | 4,425 | 1,508 | 1,365 | 101 | 1,526 | 2,465 |
| 2017 | 1,634 | 1,465 | 0 | 2,395 | 1,503 | 3,992 | 7,730 | 3,739 | 2,446 | 1,970 | 158 | 3,331 | 2,279 |
| 2018 | 2,565 | 1,067 | 0 | 1,424 | 1,287 | 3,769 | 8,207 | 4,438 | 2,858 | 2,529 | 160 | 3,507 | 2,189 |
| 2019 | 2,502 | 673 | 0 | 2,337 | 709 | 4,802 | 9,077 | 4,274 | 3,006 | 2,454 | 249 | 3,650 | 2,081 |
| 2020 | 2,781 | 838 | 0 | 2,347 | 664 | 5,301 | 10,094 | 4,793 | 3,754 | 3,399 | 603 | 4,900 | 2,026 |
| 2021 | 2,025 | 784 | 0 | 2,486 | 648 | 4,647 | 10,205 | 5,558 | 4,061 | 3,457 | 478 | 4,302 | 2,063 |
| 2022 | 2,032 | 1,656 | 0 | 2,132 | 708 | 5,112 | 9,751 | 4,639 | 3,591 | 2,615 | 161 | 3,793 | 2,097 |
| 2023 | 3,471 | 708 | 744 | 1,998 | 727 | 6,194 | 9,982 | 3,788 | 2,877 | 2,850 | 75 | 3,869 | 1,952 |
| 2024 | 1,218 | 599 | 1,059 | 4,254 | 0 | 7,130 | 10,704 | 3,575 | 2,287 | 3,091 | 192 | 3,745 | 1,760 |
| 2025 | 4,365 | 256 | 2,474 | 919 | 20 | 7,994 | 11,482 | 3,488 | 2,257 | 3,483 | 480 | 4,157 | 1,585 |
| 30 Jun 2026 | 3,724 | 457 | 3,552 | 901 | 0 (dividend payable 743) | 7,891 | 11,476 | 3,585 | 2,554 | 4,251 | 872 | 5,427 | 1,531 |

(Financial investments: wealth management and fund products, listed equities held for trading, "loans and receivables at
fair value" of 2015-17 and available-for-sale investments, as each year's notes class them. Trade and bills receivables
include bills at fair value through other comprehensive income where shown.)

**What the figures are saying** **[M2025-032]**: (1) Equity grew from RMB 6.6bn (2015) to RMB 11.5bn (2025) with no
goodwill, no intangible line and no share issued; the growth is retained cash. (2) Net financial assets went from RMB 0.7bn
(2015) to RMB 8.0bn (2025): about 70% of equity at end-2025 is cash, deposits and investment products; the business itself
runs on operating capital of RMB 3.5-4.8bn in most years. (3) Borrowings of RMB 4.4bn in 2015 (offshore loans set against
onshore pledged deposits of RMB 2.4bn) were run down to nil by 2024 ("repayment of offshore USD loans in April 2024",
AR2025 p. 12). (4) Plant shrank from RMB 3.26bn (2014) to RMB 1.58bn (2025) as capex ran below depreciation after the
2010-12 build; over the whole cycle 2010-2020 capex and depreciation were level. (5) Suppliers fund the working capital:
trade and bills payables of RMB 4.2bn exceed inventory of RMB 2.3bn at end-2025 and rose to RMB 5.4bn at June 2026
(payables days 164 in 2025, 168 in H1 2026); bills payable were RMB 2.13bn at end-2025, and a further RMB 2.37bn of
endorsed bank bills were derecognised with recourse to the Group if the accepting PRC banks default (note 37). (6)
Receivables: trade receivables gross RMB 3.83bn against an allowance of RMB 492m (12.8%) at end-2025, plus loans to
dealers of RMB 443m impaired by RMB 437m, both the residue of the 2012-15 credit losses (note 19: dealers were obliged to
repurchase machines under third-party finance leases and the Group lent them the money). (7) In H1 2026 trade receivables
rose 25.6% and long-term (instalment) receivables 81.8% against revenue growth of 19.0%, on "higher-priced electric
machinery with extended payment terms" (IR2026 MD&A). **What they don't and can't say:** whether the shrinking plant is
efficiency or under-investment; what the recourse on RMB 2.37bn of endorsed bills would cost in a bank failure; how the
new instalment book will collect through the next downturn (the last one cost about RMB 0.9bn of allowances still on the
books).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this business "if the market closed for five
years" **[M1997-109]**, and the price here is the market serving, not instructing: "It just tells us prices" **[M2006-077]**.
No macro enters: the MD&A's case for 2026 rests on the PRC GDP target, fiscal policy and the "15th Five-Year Plan"; "macro
conclusions are — just never enter into the discussion" **[M2000-094]**, so none of it is used. The margin-of-safety
attitude bears directly, because the arithmetic below looks cheap: "if you have to actually do it on — with pencil and
paper, it’s too close to think about" **[M1996-084]**, and the analyst's own incentive runs toward clearing a cheap name, so
the hunt is for "what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**:
(a) the gross margin fell from 23.4% (2020) to 17.9% (2021) when costs rose and had recovered only to 21.4% by 2025;
(b) revenue in 2025 (RMB 11.2bn) is below 2011 (RMB 12.7bn); (c) forklift sales fell 7.04% in 2025 and 10.2% in H1 2026
while the forklift specialist read below grew; the filer says its "penetration rate in the electric forklift market remains
below the industry average" (AR2025 p. 10); (d) receivables and instalment credit are growing faster than sales again,
the pattern that preceded the 2012-15 losses; (e) the financial-investment book lost RMB 207.5m (2018) and RMB 285.4m
(2022) at the segment level; (f) the founder is 75, chairman and chief executive together since 2015, and no successor is
named; (g) related-party purchases from companies owned by the controlling holders' relatives (note 36; RMB 43m in 2025);
(h) the interim MD&A describes the company's own results in an outsider's voice ("these movements appear to be largely in
line", "This margin improvement suggests enhanced pricing power"), and AR2025 note 4 prints a segment result as
"1,Z041,850".

## THE STANDING RULE
The buyer's conduct: a purchase of a quoted minority interest paid in cash, unlevered and sized so that a total loss leaves
the buyer whole, puts no one at risk of ruin: "We are never going to risk what we have and need for what we don’t have and
don’t need" **[M2012-081]**; borrowed money is "the one thing that ends — or can prevent you from playing out your hand"
**[M2004-065]**. The holding would be an HKD-quoted claim on RMB earnings; "Any currency-related investment is a bet on how
government now, and in the future, will behave" **[M2011-025]**, so size, not leverage, carries that exposure. Nothing here
is a verdict on the business.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the industry"
  **[M2011-014]**. The key variables, and how predictable they are **[M1998-044]**: (1) PRC and export demand for loaders,
  excavators and forklifts, cyclical and policy-driven (revenue swung from RMB 12.7bn in 2011 to RMB 4.8bn in 2015 and back
  to RMB 13.7bn in 2021); (2) steel and component costs against the price the dealers will bear; (3) the credit the Group
  extends to dealers and end-buyers; (4) the move to electric machines. Each is visible in the filings over two full
  cycles, 2010 to 2025: the business makes machines in China, sells "substantially all of our products through sales
  agents" (AR2025 p. 27) on credit of "six to twelve months, extending up to eighteen to twenty-four months for some
  customers" (note 17), and the past statements show how the cycle passes through them. A dependence on a cyclical price is
  "never by itself a STOP at Q1" (Q2, A commodity business), and the decision can be made "off the figures" **[M2008-069]**.
- **Routing.** Not a business of fast-moving technology in the sense of **[L1993-023]** and **[M1998-008]**: the products
  (ZL50-class loaders, crawler excavators, counterbalance forklifts) are decades old; the change under way is the power
  train (electric loaders and forklifts), which bears on who wins (Q2), not on whether the economics can be read.
  **The finance-lease arm**, read by the framework's text on lenders: the segment "finance lease of construction machinery"
  had no revenue in 2024 or 2025, a result of RMB -70k and assets of RMB 244.8m (note 4); the Group's credit exposure is its
  trade and instalment receivables and the old dealer loans, all on the balance sheet with their ageing and allowances
  (notes 15, 17, 19, 40). Both sides can be read: the asset side is customer credit with stated terms and loss history, and
  the funding side is equity, supplier bills and no borrowings. This is not an institution whose condition cannot be seen
  **[M2001-066]**, **[L2002-018]**; "even though I could understand every individual transaction" **[M2002-094]** is the
  warning, and here the whole lending activity is a bounded part of a manufacturer's balance sheet.
- **Abroad.** A Cayman company listed in Hong Kong, operating in the PRC, controlled 56.92% by a founder's wife (AR2025
  p. 21). The rows ask "where we think we understand the nuances of the corporate governance system and taxation"
  **[M2000-141]** and, for China, a higher price rather than a pass: "We wanted to get paid more for going into China"
  **[M2006-021]**. The tax is read from note 10 (PRC enterprise tax at 25%, 15% at the 13 entities qualified as High and
  New Technology Enterprises, and a 5% withholding tax on dividends paid to the offshore holding companies); dividends have been paid in HKD every year 2016-2025 (RMB 5.74bn in the ten years' cash-flow statements).
  The governance is read at Q5 and Q6, not here.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The doubt
  found is about who wins (the castle), not about how the business makes or loses money; that belongs to Q2.
- **VERDICT: IN.** The economics of a cyclical, dealer-sold, credit-financed machinery maker can be read from fifteen years
  of its own filings **[M2012-065]**, **[M2011-014]**, **[M2008-069]**; the lease arm is dormant and its book readable.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The rivals (CONVENTION of this run).** AR2025 names no competitor: its risk section says only "We face competition in
the market from international and domestic construction machinery manufacturers, many of which entered the market before us
and currently have larger market shares than us" (p. 26). No named rival therefore files with the SEC or otherwise. Rivals
chosen, read from their own annual reports on the Shenzhen and Shanghai exchanges (cninfo.com.cn; primary filings, flagged
as not SEC filers; FY2016, FY2019, FY2022 and FY2025 reports, each carrying three years of key data): **Guangxi LiuGong
Machinery (000528.SZ)** and **XCMG Construction Machinery (000425.SZ)**, the two listed makers whose own 2025 reports claim
the wheel-loader lead (LiuGong FY2025 pp. 20-21: its loader business "稳守全球销量领先的地位", holds the global sales lead;
XCMG FY2025: "装载机稳居国内第一", loaders first in China), and **Hangcha Group (603298.SH)**, the listed forklift
specialist, for Lonking's second product line. Rationale: they are the listed makers of the same machines, and the loader
pair says in its own filings that it holds the volume. Flagged, not read: Shandong Lingong (SDLG, Volvo-owned; files no
separate statements), Heli (600761.SH; the three-rival limit), Sany (its loaders are a small part of a large group). XCMG's
figures from 2022 include the parent it absorbed that year (restated as a common-control merger; the originally reported
figures are used for 2020 and 2021).

**The competitor rows (same metric, each filer's own report; whole span, not one year).**

| Year | Lonking ROE (net profit / average equity) | LiuGong ROE (weighted, as reported) | XCMG ROE (weighted, as reported) | Hangcha ROE (weighted, as reported) |
|---|---|---|---|---|
| 2014 | 6.0% | 2.16% | 2.10% | 25.33% |
| 2015 | 1.7% | 0.24% | 0.27% | 19.90% |
| 2016 | 6.9% | 0.56% | 1.01% | 19.95% |
| 2017 | 14.5% | 3.66% | 4.70% | 14.25% |
| 2018 | 14.4% | 8.46% | 8.28% | 14.95% |
| 2019 | 19.0% | 10.23% | 12.56% | 15.85% |
| 2020 | 20.4% | 11.49% | 11.74% | 18.21% |
| 2021 | 12.6% | 6.64% | 16.24% | 17.22% |
| 2022 | 4.0% | 3.85% | 8.13% | 16.70% |
| 2023 | 6.5% | 5.40% | 9.86% | 22.17% |
| 2024 | 9.8% | 7.93% | 10.30% | 21.68% |
| 2025 | 11.7% | 9.03% | 11.00% | 20.34% |
| **Average 2014-2025** | **10.6%** | **5.8%** | **8.0%** | **18.9%** |

| Gross margin | 2015 | 2016 | 2018 | 2019 | 2021 | 2022 | 2025 |
|---|---|---|---|---|---|---|---|
| Lonking | 22.8% | 24.2% | 23.0% | 23.9% | 17.9% | 16.7% | 21.4% |
| LiuGong (whole company; 2025 construction machinery) | 25.5% | 24.9% | 22.8% | 23.7% | 17.5% | 16.8% | 22.0% |
| XCMG (whole company; 2021 restated; 2025 construction machinery) | n.r. | n.r. | 16.7% | 17.5% | 21.5% | 20.2% | 22.6% |
| Hangcha (whole company; 2025 forklifts and parts) | 24.5% | 23.6% | 20.6% | 21.3% | 15.5% | 17.8% | 24.8% |

| Net margin (attributable profit / revenue) | 2016 | 2019 | 2022 | 2025 | Revenue 2016 to 2025 |
|---|---|---|---|---|---|
| Lonking | 9.0% | 14.0% | 3.6% | 11.6% | RMB 5.1bn to 11.2bn (x2.2) |
| LiuGong | 0.7% | 5.3% | 2.3% | 4.9% | RMB 7.0bn to 33.1bn (x4.7) |
| XCMG | 1.2% | 6.1% | 4.6% | 6.5% | RMB 16.9bn to 100.8bn (x6.0, merger included) |
| Hangcha | 7.5% | 7.3% | 6.9% | 12.4% | RMB 5.4bn to 17.7bn (x3.3) |

Lonking's own return on the capital it needs: the machinery segment's pre-tax result against operating capital (equity less
net financial assets, Step 0) averaged about 26% over 2016-2025, from 5.9% (2016) and 12.3% (2022) at the troughs to
35-37% at the peaks (`scripts/lonkf_calc.py`). The rivals' ROE figures above carry their own leverage and cash; the bases
differ and are not made to match.

**The parts table.** The filer reports three segments (note 4): sale of construction machinery; finance lease of
construction machinery; financial investment. Five-year segment results 2021-2025: machinery RMB 4,960.6m; financial
investment RMB -48.5m; finance lease about nil. **Machinery decides** (more than half). Product lines (loaders 41.0% of 2025
revenue, forklifts 30.8%, excavators 15.1%, then components, skid steers, rollers) are revenue lines without reported
profit, not parts; forklift gross margin 21.25% is the only line margin given (AR2025 p. 10).

**The castle tests on the deciding part, each with its filing fact.**
1. *What keeps it standing, and how permanent* **[M1995-038]**. The filings show what Lonking's results rest on: a lower
   total cost than the two state-owned loader makers (net margins about double theirs in each year sampled), supplier
   credit that funds the working capital (payables above inventory every year since 2017), and capital spending below
   depreciation in every year since 2014 except 2021. The gross margin, the cost of production against the price, is level with LiuGong's in every
   year read and below XCMG's and Hangcha's in 2025; the edge is in overhead and capital, not in making the machine. "How
   much do they depend on the genius of the lord in the castle?" **[M1995-038]**: see test 2.
2. *Without the lord.* The founder, Mr. Li San Yim, is 75, chairman and chief executive together since 21 December 2015
   (AR2025 p. 30); with his wife he controls 56.92%; no successor is named in AR2025 or IR2026. A low-cost position in a
   commodity field is kept only by management: "a company holding a low-cost advantage must pursue an unrelenting
   foot-to-the-floor strategy" **[L2004-007]**; "the poor business is one that can only succeed, or even survive, with great
   management" **[M1996-037]**; "if a business requires a superstar to produce great results, the business itself cannot be
   deemed great" **[L2007-006]**. Whether the overhead discipline outlives its author cannot be read from any filing.
3. *The money test* **[M2011-015]**. The attackers with money are already in the field and hold the volume: XCMG (RMB 100.8bn
   revenue, loaders first in China), LiuGong (RMB 33.1bn, the global loader lead and close to half of China's
   electric-loader exports by its own FY2025 report, pp. 20-21), Hangcha (forklifts RMB 17.4bn). They have not broken
   Lonking's margins over a full cycle, but "one competitor is frequently enough to ruin a business" **[M2012-108]**, and
   none of the three FY2025 reports mentions Lonking at all (a search of each for its Chinese name found no instance).
4. *Pricing power* **[M2005-020]**. In the 2021 cost rise Lonking's gross margin fell from 23.4% to 17.9% in one year and
   was 21.4% in 2025, still below 2019's 23.9%; the whole field fell together (LiuGong 23.7% to 17.5%, Hangcha 21.3% to
   15.5%), and LiuGong (22.0%) and Hangcha (24.8%) recovered further by 2025. "over time the businesses with strong
   competitive positions manage to pass through increases in raw material costs" **[M2005-017]**: no one in this field did
   in 2021, and Lonking recovered least.
5. *Volume and share.* AR2025 gives no unit sales or national market share. The filer's own earlier reports claimed the
   loader volume lead: "Loaders ranked top in the industry in both production and sales volume" (AR2017), and "the domestic
   market share of the loaders continued to remain at the top spot of the industry" (AR2019, AR2021). No such claim appears
   in AR2023, AR2024 or AR2025 (a search of each for "market share"), while XCMG's FY2025 report claims the domestic first
   place and LiuGong's the global lead. Revenue 2025 (RMB 11.2bn) is below 2011 (RMB 12.7bn);
   from 2016 to 2025 Lonking grew 2.2 times, LiuGong 4.7, Hangcha 3.3. Forklift sales fell 7.04% in 2025 ("both volume and
   price declining") and 10.2% in H1 2026, while Hangcha's forklift revenue rose 5.77% and its units 19.4% in 2025.
6. *The low-cost position* **[L2000-017]**, **[M1997-010]**. The rows' low-cost producer is the one whose advantage "is the
   reason that over time it will inevitably increase its market share significantly while simultaneously achieving excellent
   profits" **[L2000-017]**, and whose aim is "not to widen our profit margin but rather to enlarge the price advantage we
   offer customers" **[L1996-016]**. Lonking has the margin; the share it claimed in loaders to 2021 it no longer claims, and in
   forklifts it is shrinking. It is lower-cost than LiuGong and XCMG in overhead, level with them in production cost, and
   not shown to be the low-cost producer against the volume leaders. SDLG,
   the other loader leader, files no statements, so its cost cannot be read from any filing ("we would measure it,
   probably, more by cost of production" **[M2006-004]**; "The figures are available" **[M2009-059]**, but not for SDLG).
7. *Brand and the low bid.* Lonking sells on price: its chairman's own words are that its products "maintained core
   competitive advantage in cost effectiveness" (AR2025 p. 5). That is the commodity mark, "most insureds don't care from
   whom they buy" **[L2004-003]**, against the exception, "Another way to prosper in a commodity-type business is to be the
   low-cost operator" **[L2004-007]**; the file stands or falls on test 6.
8. *Widening or narrowing* **[M1999-108]**. Narrowing in forklifts on the evidence (the filer's own words on electric
   penetration, its sales fall against the specialist's rise); widening is not shown in loaders (the domestic top-spot claim of AR2017 to
   AR2021 is no longer made, and the volume and electric leads are the rivals', by their own filings), though loader and excavator sales rose 16.9% and 60.1% in 2025 and 37% and
   28% in H1 2026 on the domestic upturn and exports.
9. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. The move to electric machines,
   which the two loader leaders and the forklift leader each say in their filings they lead; selling on instalment credit
   (long-term receivables +81.8% in six months), the road the 2012-15 losses came by; and succession.

**The field's returns over the last full cycle (judged in words; section C).** The cycle 2014-2025 runs from the 2015
trough through the 2020-21 peak to the 2022-24 trough and the 2025 recovery. The two largest listed loader makers earned
ordinary returns on equity over it (averages 5.8% and 8.0%; about 1% or less in 2015-16). The forklift specialist earned
excellent returns (18.9%) and grew. Lonking earned more than the loader pair on equity (10.6%, with about 70% of its 2025
equity in cash and investments) and well above ordinary on the capital its machinery business needs (about 26% pre-tax on
average). So Lonking's own returns are not the field's ordinary returns, and the convention's OUT (the standing castle that
protects only ordinary returns) does not describe it on the evidence. What the evidence does not show is the castle that
protects those returns: not a lower cost of production, not pricing power, not share, not a brand; an overhead and capital
discipline that the filings tie to one founder, in a field whose volume leaders are moving the product to a new power train.

**Why the box.** "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**: it has stood a full cycle on its owner's discipline; what keeps it standing
for ten to twenty years cannot be judged from the filings, because the one advantage they show depends on the lord in the
castle and on a power-train race the rivals say they lead. "when we see a moat that’s tenuous in any way [...] it’s just too
risky. We don’t know how to valuate that, and therefore we leave it alone" **[M2000-019]**; where what will "destroy, or
modify, or reduce the economic strengths" cannot be figured, "we don’t even think about it then" **[M2000-014]**. A castle
shown open on the evidence is not what was found (the margins held through the 2015 and 2022 troughs better than the loader
pair's), so the box is not OUT; it is "too hard" **[M2006-013]**.

**The cause: NATURE.** The deciding question, whether Lonking's cost edge survives its founder and the move to electric
machines against rivals that hold the volume, is a forecast the industry's own insiders "would not want to put down on
paper" **[M2000-105]**; no filing states the loader leader SDLG's cost (the commodity paragraph sends that case to TOO HARD
(NATURE)); and the succession is not knowable from outside. More reading would not answer it: "We couldn't solve this
problem, moreover, even if we were to spend years intensely studying those industries" **[L1993-023]**, and "if we can’t
make a decision in five minutes, we can’t make it in five months" **[M2008-086]**. A lower price does not reopen it
(section I).

- **VERDICT: TOO HARD (NATURE).** The deciding part's returns are well above ordinary over a full cycle, but the castle
  that protects them, an overhead discipline tied to a 75-year-old founder in a commodity field whose volume leaders lead the
  move to electric, cannot be judged ten to twenty years out **[M1995-038]**, **[M2000-019]**, **[M2000-014]**,
  **[L2004-007]**, **[M2006-013]**. Q3 to Q12: NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 **[M2025-032]**; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's reporting figures are computed below the stop under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q2**: returns on the capital the machinery business needs have been well above the field's
over a full cycle, but the only castle the filings show, an overhead and capital discipline in a commodity field, rests on
a 75-year-old founder with no named successor, and the rivals that hold the loader and forklift volume say in their own
filings that they lead the move to electric machines; what keeps it standing ten to twenty years cannot be judged
**[M1995-038]**, **[M2000-019]**, **[M2000-105]**. Integrity facts recorded, not judged. (For the operator, below the stop:
the computed range is RMB 12.30 to 14.01 a share, HKD 14.34 to 16.33, against HKD 3.04; COMPUTATION, NOT A CLEARANCE; a
NATURE box is not reopened by price.)

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(The file closed at Q2. Facts already found that bear on later questions, each with its source **[M1997-127]**; written
down, not weighed; no verdict; the box unchanged.)*

**Q3 (capital).** Operating capital (equity less net financial assets) RMB 3.5bn to 5.6bn over 2016-2025 (Step 0 table);
the machinery segment's pre-tax result on it averaged about 26%, 5.9% in 2016 and 12.3% in 2022 at the troughs. Capital
spending RMB 3,573m against depreciation RMB 3,715m over 2010-2020, and RMB 953m against RMB 1,312m over 2021-2025; H1 2026
capex RMB 75m against RMB 29m a year earlier. The capital kept and not used in the business, RMB 8.0bn of net financial
assets at end-2025, earned interest of RMB 148m in 2025 and segment gains in the investment book that summed to RMB 934.5m
over 2016-2025, with losses of RMB 207.5m (2018), RMB 285.4m (2022) and RMB 82.8m (2023).

**Q4 (the accounts).** Auditor Ernst & Young, unqualified, 26 March 2026; the one key audit matter is the expected credit
loss on receivables, "21% of the Group's total assets" (AR2025 p. 64). EBITDA and an "EBITDA margin" are featured in the
filer's own Financial Highlights (AR2025 p. 3; IR2026 p. 2); the income statement and cash-flow statement are complete and
reconcile (revenue cross-check, Step 0). Allowances on trade receivables RMB 492m (12.8% of gross) and on dealer
repurchase loans RMB 437m of RMB 443m (notes 17, 19). Receivables and instalments rising faster than sales in H1 2026 (trade
receivables +25.6%, long-term +81.8%, revenue +19.0%). Derecognised endorsed bills with recourse RMB 2,371.8m (note 37).
"Additional value-added tax deduction" RMB 56.4m and government grants RMB 41.8m in other income (2025). No guidance found;
positive profit alerts (2025-01-17, 2025-07-21, 2026-01-20, 2026-07-20) are listing-rule notices, not forecasts. A segment
figure printed "1,Z041,850" (AR2025 note 4, 2024 column; 1,041,850 in AR2024).

**Q5 (integrity facts, recorded, not judged).** Mr. Li San Yim, founder, 75, chairman and chief executive since 21 December
2015, a deviation from code provision C.2.1 that the board defends as "continuity" (AR2025 p. 30); his wife Ms. Ngai Ngan
Ying (non-executive vice-chairman) holds 56.92%. Connected purchases from LongYan City Jinlong Machinery (82.67% owned by
Ms. Ngai's brother; RMB 31m in 2025, a new three-year master agreement from 1 January 2026) and from Herkules (Shanghai)
Automation (owned by Mr. Li's son-in-law; RMB 12m), reviewed by the auditor under Practice Note 740 (AR2025 pp. 24-25).
Two independent directors have served more than nine years (since 2005 and 2013), and two of the three are former
Songjiang district officials; three independent directors and the non-executive director missed the 2025 AGM; no
directors' liability insurance (AR2025 pp. 28-29). The interim report's MD&A comments on the company's own results in a
third party's voice ("these movements appear to be largely in line with sales growth", "This margin improvement suggests
enhanced pricing power", IR2026 pp. 35-37). Directors' pay 2025 RMB 12.6m in total (Mr. Li RMB 7.64m in salary, no bonus;
independent directors RMB 100k to 200k each in fees), note 8. No share options or share awards. No litigation found (search
of AR2025 for "litigation" and "legal proceeding": no instance found).

**Q6 (the money and the owners).** Dividends paid RMB 5,737.5m over 2016-2025 against attributable profit of about
RMB 10.9bn (cash-flow statements); 2025 final HKD 0.20, 58% of profit; dividend policy on AR2025 p. 38. No share bought back
or issued from 2014 to H1 2026 (each annual report's "neither the Company nor any of its subsidiaries purchased, sold or
redeemed"); Q6's buyback test against the bottom of the Q7 range therefore has no purchases to read. Equity rose from
RMB 6.72bn (2016) to RMB 11.48bn (2025) while net financial assets rose from RMB 2.3bn to RMB 8.0bn: most of the money kept
was kept as cash and investment products (wealth management products issued by mainland financial institutions RMB 666m;
listed equities held for trading RMB 253m with a "guaranteed return clause" triggered in H1 2026; discloseable transaction
of 2025-05-02). No acquisition in the window.

**Q9 (debt and exposures).** Borrowings nil at 30 June 2026 (RMB 20m at end-2025); bills payable RMB 2,131.6m at end-2025
secured partly by pledged deposits; recourse on RMB 2,371.8m of derecognised endorsed bills if the accepting banks default;
customer credit of up to 24 months and instalment receivables bearing 3% to 8%; the 2012-15 dealer repurchase losses
(note 19). Current ratio 2.01 at June 2026. Exports 33.9% of 2025 revenue (exchange exposure).

## COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures; Q7 never reached)
*(Reporting convention at the owner's request, not a rule. Figures in RMB millions unless stated; arithmetic in
`Test Runs/_research 2026-10-13 LONKF/scripts/lonkf_calc.py`; rate HKD 1 = RMB 0.85753, CFETS central parity 2026-10-13.)*

- **Input.** Owner cash after every real cost, all-equity basis (before interest, after the company's own tax paid, all
  capital spending and working capital deducted; Step 0). The literal window 2021-2025 averages **1,065.9**. Its first year,
  2021, is the series' trough in the filings read and the year the filer reports as its record revenue year
  ("the Group’s operating revenue reached a record high", AR2021), with a working-capital build; by specific (a) the base is the last full cycle of owner cash, trough 2010 to trough 2021, i.e. the
  years 2010-2020: **935.2**. Growth between cycles: only one full cycle lies in the filings read (AR2010 reaches back to
  2009 only), so the growth is measured from the full-cycle average (midpoint 2015) to the latest five-year average
  (midpoint 2023): **+1.65% a year**; the halves of the last ten years (2016-20 against 2021-25) give **-0.91% a year**,
  shown beside as the decline case of (b).
- **Specifics.** (a) cycle base, literal window beside; (b) the halves decline shown beside as a lower bottom; (c) no
  acquisitions, no merger, no signed deal; (d) working capital counted (it is inside cash generated from operations); (e)
  the filing allows no split of maintenance from growth spending, and over the full cycle capital spending equalled
  depreciation, so the all-spending case is central and the depreciation variant (cycle base 922.3) is beside; (f) the
  shown rate 1.65% is below the 2.069% discount rate, and carried ten years it gives owner cash of about 10% of sales
  against the highest share earned, 37% (2016): no cut. Tax: the company's own tax as paid (13 subsidiaries at the 15%
  High and New Technology rate, a renewable status rather than a carryforward running out, so no section-E adjustment).
- **Net debt** at 30 June 2026 (IR2026), with the subsequent event that filing and the AGM announcement state: cash
  3,724.2 + time deposits 3,552.5 + financial assets at fair value through profit or loss 900.8, less the final dividend
  payable 743.5 (distributed by 31 July 2026), borrowings nil: **net cash 7,433.9**. Pledged deposits (457.3) are left out
  because they secure bills payable, which are left in working capital as the filing classes them (non-interest-bearing
  trade payables); operating leases left out.
- **The floor, tested first.** At the price the market value is 11,157.8 and the all-equity price of the business
  11,157.8 - 7,433.9 = **3,723.8**; owner cash on it: 935.2 / 3,723.8 = **25.1%** on the cycle base (28.6% on the literal
  window). Every case clears about ten percent. Equity-only (owner cash after net interest against the market value): 8.0%
  on the cycle base (891.0), 10.4% on the window (1,163.9).
- **(a) VALUE RANGE (all-equity, central; ten years at the growth case, then zero, at 2.069%), plus net cash:**
  no growth 45,201 + 7,434 = 52,635, **RMB 12.30 / HKD 14.34 a share**; +1.65% for ten years 52,518 + 7,434 = 59,952,
  **RMB 14.01 / HKD 16.33 a share**. Width 1.14 to 1. Beside: literal window RMB 12.81 to 13.77 (HKD 14.94 to 16.06); cycle
  base with the halves decline as the bottom RMB 11.45 (HKD 13.36). Against **HKD 3.04 (RMB 2.61)**.
- **(b) FAIR PRICE** (each end case valued at ten percent, averaged; Part VII): all-equity, central: no growth 9,352 and
  growth 10,461, plus net cash 7,434, average **RMB 4.05 / HKD 4.72 a share**. Equity-only beside (owner cash after net
  interest, no cash added): **RMB 2.35 / HKD 2.74 a share**. Beside, with bills payable net of pledged deposits (1,674,
  end-2025 split) counted as debt: RMB 3.66 / HKD 4.27; on the literal window: RMB 4.15 / HKD 4.84.
- The two bases part widely because about two thirds of the market value is net cash: the all-equity figure counts the cash
  at its face; the equity-only figure counts it only through the interest it earns. Neither figure is a verdict, and the
  box is TOO HARD (NATURE) whatever the price.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (by the earlier cycle); written question by question; committed after Q1
      and after Q2 (two commits before this close) (write-early).
- [x] Dispatched: the brief allowed the per-question commits; the lock file in `Screens/_daily/` was present when this
      session began (not written or touched here); the fold is the dispatching session's (operator rule ten). A run not in
      the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (commit
      subjects of another company's run, folder names, memory lines) is declared under contamination at the top, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `Test Runs/_research 2026-10-13 LONKF/scripts/check_ids.py`); filing facts carry the document, date and HKEXnews file
      number (no accession numbers exist for this filer); the rivals' figures carry their report year.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance, and the figures below it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from ChinaBond (CCDC, the Ministry of Finance's published curve), dated; the HKD/RMB rate from CFETS for the
      PBOC, dated; the price quotes are an aggregator's and flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, items a to h); facts for later
      questions are under AFTER THE STOP, and the integrity flag is in the box line.
- [x] No row dated after the anchor is cited (this is a current run, not a point-in-time test).
- [x] `tools/run.py` produced no arithmetic lines for this filer; nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before the close commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 specific (a) on a countercyclical series.** The cycle is to be defined on owner cash, but this business's owner
cash moves against its demand cycle (working capital is built in the boom and released in the bust), so the owner-cash
troughs fall in the industry's peak years (2010, 2021) and the "full cycle" so defined (2010-2020) is not the industry's
(peak 2011, trough 2015, peak 2020-21, trough 2022-24). The text also asks for growth "between the averages of successive
cycles", and the filings read hold only one full cycle; I measured growth from the cycle average to the latest five-year
average and showed the halves beside. A sentence saying which series defines the cycle when owner cash and demand move
oppositely, and what to do with one cycle, would settle it. (2) **Q2's "ordinary returns" convention** does not say whose
returns or on what base: the field's durable players (here 5.8% and 8.0% average ROE) or the filer's; on equity or on the
capital actually needed **[M2010-090]** (here 10.6% on equity, about 26% pre-tax on operating capital, because 70% of
equity is cash). I judged both and said so. (3) **The commodity paragraph's low-cost test** quotes cost of production
**[M2006-004]**, while the rows' examples of the low-cost producer (GEICO, Costco) are low operating cost, overhead
included **[L2007-004]**; a business level on production cost and lower on overhead falls between them, as this one does.
(4) **The equity-only fair price for a net-cash company** counts the cash only through its after-tax interest capitalised at
ten percent, so RMB 7.4bn of cash enters at a fraction of its face, and the two reporting figures differ by 70% (HKD 4.72
against HKD 2.74); the text says the equity-only figure "never decides alone", but a cash-rich filer makes it misleading
beside the central figure. (5) **The brief's rival rule** assumed the annual report names rivals; this one names none, and
the confessed choice of three rivals is the run's. (6) **TOO HARD (NATURE) at Q2 and the reporting figures**: the computed
range sits four to five times the price, and the framework gives the NATURE box no re-look condition except for a change
for the better; whether a founder's succession is a dated event that should carry one (as the change-for-the-better
convention carries the first down year) is not said.
