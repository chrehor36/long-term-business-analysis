# Company Run: Jutal Offshore Oil Services Limited (HKEX: 03303; US OTC unsponsored ADR: JUTOY), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its HKEX file reference (this company files
no 20-F; the HKEX reference stands in place of an accession number, per the brief); a STOP that returns OUT or TOO HARD
closes the run and later questions are marked NOT REACHED. Copied from the template before any fetch (commit aad7b07f).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for JUTOY, Jutal or 3303).

**Dispatched run.** Brief of 2026-10-16 (dispatched analyst). Its stated departures from the canonical brief: a name with
no SEC filings (HKEX documents as primary filings, HKEX file references in place of accessions, the RMB sovereign from
the PRC Ministry of Finance curve); the lines of evidence derived by the analyst from the latest annual report rather
than listed in the brief.

**Contamination declared (seen, not used).** At session start the harness showed recent commit subjects of another
company's run (IOGPQ, folded 2026-10-16, with a line about "three bankrupt or dark filers tonight boxed two ways"), file
names of other runs' research folders in the git status (AYI 2026-09-26, ARCB 2026-09-27), and memory-index lines naming
the queue state ("wave 7 PAUSED at 111/218", "57 gate-clearers, nothing buyable") and the names of blind-listed files.
None concerns this company; none was opened or used. No `Test Runs/` file about Jutal was searched for beyond a
filename listing made before the template copy, which returned nothing.

**Lines of evidence, derived from the FY2025 annual report (HKEX 2026042900381) as the brief asks.** The Directors'
Report says the Group is "principally engaged in fabrication of facilities and provision of integrated services for oil
and gas industries, new energy and refining and chemical industries" and refers its principal risks to the Chairman's
Statement, the MD&A and the notes. From those: (1) workload and order intake, since "The projects obtained by the Group
are generally through tendering. The major customers of the year may not be the same as different projects undertaken
each year" (Directors' Report); (2) the two segments and their margins over the cycle (MD&A tables); (3) the fixed
overhead of two yards against a falling workload (MD&A: manufacturing overheads "have not decreased proportionally");
(4) the OFAC SDN listing of Penglai Jutal and its effect on clients (Chairman's Statement); (5) the move to EPC general
contracting and offshore wind, a "new business type" (Chairman's Statement, Prospects); (6) capital spending on Quay#2
and the funding of it by placings, a rights issue and bank borrowing (MD&A, supplementary announcement 2026-10-09);
(7) customer concentration (five largest customers 63.26% of 2025 sales, largest 21.28%, Directors' Report); (8) the
accounts themselves: qualified audit opinions FY2021 to FY2023, liquidated damages, warranty provisions. Chosen because
each is what the report itself names as moving the result.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** HK$0.38 per share (3303.HK last trade 2026-10-16, volume 384,000 shares; 2026-10-15 close HK$0.365;
  Yahoo chart API, **aggregator, flagged** per operator rule 5). ADR JUTOY last trade US$12.54 on 2026-10-14 (100 ADRs;
  aggregator, flagged; thinly traded). In RMB: HK$0.38 x 0.85658 = RMB0.3255.
- **ADR ratio:** 1 ADS = 250 ordinary shares (Form F-6EF, 2009-04-23, accession 0001019155-09-000474; the 2008 F-6EF,
  accession 0001144204-08-069883, states the same). At HK$0.38 an ADR is HK$95.0 = US$12.11 at the CFETS cross rate,
  consistent with the US$12.54 last ADR trade.
- **Shares:** 2,488,835,287 ordinary shares issued, 0 treasury shares (Monthly Return FF301 for the month ended
  30 September 2026, submitted 2026-10-06, HKEX 2026100600381). Checked against the rights-issue results announcement
  (2026-03-19, HKEX 2026031901220): 2,133,287,389 before + 355,547,898 rights shares = 2,488,835,287. Matches. One class.
  Options outstanding: 33,545,509 at HK$1.93 and 132,404,790 at HK$0.47, both out of the money at HK$0.38.
  `Screens/cover_shares.py JUTOY` refused ("NOT AN SEC REGISTRANT"); the count is taken by hand as the brief directs.
- **Market cap:** HK$945.8M = RMB810.1M. Net cash at 30 June 2026 (interim report, HKEX 2026092900313): bank and cash
  RMB641.2M + financial assets at fair value RMB81.4M - bank and other borrowings RMB479.9M - lease liabilities RMB21.3M
  = **RMB221.3M net cash** (pledged deposits RMB53.8M left out as restricted, shown beside; operating and finance
  leases are both on the balance sheet under HKFRS 16 and both are counted, said so). Enterprise value RMB588.8M.
- **Sovereign for the earnings currency (RMB):** **2.06%**, the 30-year point of the China Treasury Yield Curve of the
  PRC Ministry of Finance (财政部-中国国债收益率曲线), as published by ChinaBond on the Ministry's behalf
  (yield.chinabond.com.cn/cbweb-czb-web, key-term table, 2026-10-16; 10-year 1.65%). The protocol's table covers USD,
  JPY and EUR only; this is the RMB issuing authority's own curve, said so.
- **Translation:** RMB earnings to the HK$ price at the CFETS central parity published for the People's Bank of China,
  2026-10-16 09:15: HK$1 = RMB0.85658; US$1 = RMB6.7220 (chinamoney.com.cn ccpr.json). HK$ figures = RMB / 0.85658.
- **Filings read** (operator rule 4): annual reports FY2013 to FY2025 (HKEX 2014: ltn201404301184; 2015: ltn20150427441;
  2016: ltn20160429375; 2017: ltn201704181155; 2018: ltn201804272984; 2019: ltn20190430458; 2020: 2020042900645;
  2021: 2021042100251; 2022: 2022042802983; 2023: 2023042800919; 2024: 2024043000517; 2025: 2025043000803;
  2026: 2026042900381, the FY2025 report), the 2026 interim report (2026092900313) and interim results announcement
  (2026082800491); profit warnings 2025-02-13 (2025021300474), 2025-08-04 (2025080401432), 2026-03-03 (2026030300677),
  2026-08-04 (2026080400738); the SDN announcements 2024-06-13 (2024061300915) and 2025-10-14 (2025101400296); the
  rights-issue documents 2026-01-14 (2026011401240), prospectus 2026-02-06 (2026020600159), acceptances 2026-03-03
  (2026030300663), results 2026-03-19 (2026031901220); the supplementary announcement on the 2025 annual report,
  2026-10-09 (2026100900109); the EGM circular of 2026-10-14 (2026101400321) and the 2026 AGM circular and poll
  (2026042900431, 2026060502040); the 2022 requisition circular (2022080301679) and poll (2022082600605); the 2024 CEO
  change (2024062400207); the 2024 and 2022 placings (2024021500662, 2022090701284); two clarification announcements of
  2024 (2024030800339, 2024080502141). The full index of 536 filings since 2014 is in the research folder.
- **One figure cross-checked against the filed statement:** FY2025 revenue RMB799,930,000 in the consolidated statement
  of profit or loss (FY2025 annual report p.49) equals the MD&A figure and the brief's "about RMB 799.9M"; FY2024
  revenue RMB2,079,022,000 in the same statement equals the comparative. The 30 September 2026 share count is checked
  above against the rights-issue results.
- `python tools/run.py JUTOY` refused ("not an SEC filer ... UNRESEARCHED, not UNKNOWABLE"). No tool arithmetic was
  used; every figure below is taken by hand from the filed statements (word-position extraction of the PDF pages,
  kept in `stmts/`), and the arithmetic is in `owner_cash.py` and `valuation.py` in the research folder.

**Owner cash by year** (RMB M; operating cash flow as filed, which under HKFRS here already deducts interest paid and
tax paid; less purchases of property, plant and equipment, intangibles and land rights; less lease principal; plus
disposal proceeds, government grants received in investing, and settlements of the contract FX hedges; "OC_ae" adds
back interest paid and drops interest received, the all-equity basis; "OC_eq" keeps interest received, the
equity-only basis). Stock pay: the 2024 share-award expense of RMB94.4M is not added back in the filed cash statement,
so operating cash already bears it; the RMB144.7M of market purchases for the award scheme sits in financing and is
not deducted a second time (said so; RMB46.1M of purchased shares were still held for future awards at 31 Dec 2024).

| Year | Sales | Op. cash | Capex | OC_eq | OC_ae | Dep.+amort. | Net profit | ROE % |
|---|---|---|---|---|---|---|---|---|
| 2014 | 951 | 57 | 122 | -56 | -41 | 27 | 28 | 2.7 |
| 2015 | 659 | 74 | 40 | 58 | 67 | 30 | 27 | 2.3 |
| 2016 | 722 | 2 | 25 | -16 | -9 | 33 | 12 | 1.0 |
| 2017 | 724 | -158 | 10 | -127 | -122 | 32 | 56 | 3.4 |
| 2018 | 1,486 | -651 | 52 | -669 | -637 | 123 | 27 | 1.3 |
| 2019 | 1,761 | 149 | 141 | 24 | 51 | 128 | 4 | 0.2 |
| 2020 | 3,647 | 798 | 147 | 675 | 691 | 157 | 147 | 6.7 |
| 2021 | 3,982 | 79 | 82 | 11 | 23 | 169 | 11 | 0.5 |
| 2022 | 1,751 | -125 | 47 | -164 | -144 | 157 | -208 | -11.7 |
| 2023 | 2,592 | 287 | 26 | 244 | 250 | 137 | 255 | 13.6 |
| 2024 | 2,079 | 477 | 139 | 346 | 339 | 116 | 185 | 8.8 |
| 2025 | 800 | -53 | 197 | -192 | -195 | 114 | 46 | 2.1 |
| H1 2026 | 319 | -148 | 126 | n/a | about -268 | n/a | -71 | n/a |

(2014 operating cash is the comparative restated in the FY2015 report, 56.7 against 56.1 first filed. 2017 also carried
a RMB446.2M net cash inflow on acquiring the other 70% of Penglai Jutal, the cash it held, and a RMB108.0M dividend
from it while still an associate; both shown outside the table. Depreciation includes right-of-use and land
amortization.) Five-year average 2021 to 2025: OC_ae RMB54.6M, OC_eq RMB49.0M. Twelve-year average: OC_ae RMB22.7M,
OC_eq RMB11.1M. Net profit 2014 to 2025 sums to RMB588.8M on average equity of about RMB1,769M: about 2.7% a year.

**The balance sheets, twelve years of them, read before the income account** **[M2025-032]** (RMB M, 31 December):

| Year | Equity | Goodwill | PPE + land/ROU | Bank cash + pledged | Receivables + contract assets | Inventory | Borrowings |
|---|---|---|---|---|---|---|---|
| 2014 | 1,126 | 182 | 526 | 95 + 31 | 289 + 215 | 20 | 230 |
| 2015 | 1,157 | 191 | 537 | 58 + 22 | 165 + 190 | 26 | 131 |
| 2016 | 1,181 | 202 | 529 | 101 + 44 | 215 + 187 | 24 | 214 |
| 2017 | 2,059 | 55 | 1,622 | 1,443 + 299 | 425 + 411 | 57 | 846 + 80 parent loan |
| 2018 | 2,133 | 55 | 1,549 | 901 + 69 | 544 + 406 | 81 | 806 |
| 2019 | 2,151 | 55 | 1,173 + 452 | 808 + 57 | 932 + 162 | 194 | 682 |
| 2020 | 2,249 | 52 | 1,247 + 445 | 1,188 + 136 | 721 + 455 | 127 | 520 |
| 2021 | 1,805 | 52 | 1,179 + 430 | 663 + 134 | 420 + 488 | 175 | 482 |
| 2022 | 1,747 | 52 | 1,036 + 398 | 610 + 98 | 264 + 366 | 122 | 465 |
| 2023 | 2,012 | 52 | 918 + 379 | 753 + 51 | 1,119 + 505 | 111 | 309 |
| 2024 | 2,175 | 52 | 932 + 364 | 785 + 65 | 285 + 477 | 93 | 86 |
| 2025 | 2,188 | 52 | 1,064 + 346 | 666 + 69 | 158 + 427 | 91 | 200 |
| 30 Jun 2026 | 2,126 | 52 | 1,151 + 349 | 641 + 54 (+81 securities) | 214 + 474 | 117 | 480 |

What the figures say: equity roughly doubled from 2014 to 2025 (RMB1,019M at end 2013 to RMB2,188M), but not from
retained profit. Shareholders paid in about RMB1.18B over the twelve years (the 2017 subscription by Sanju HK and
Golden Talent at HK$1.20, RMB837.7M; warrants and options; a 2022 placing, RMB122.4M; a 2024 placing, RMB56.4M; and
the 2026 rights issue, RMB48.6M), while net profit summed to RMB0.59B and dividends paid summed to about RMB0.69B, of
which RMB512.7M in 2021 was paid out of the share premium account (an interim special dividend of HK$0.15 and a final
of HK$0.22, against 2020 profit of RMB146.7M). Goodwill has sat at RMB52.4M since the 2017 Penglai acquisition, with
no games there. Receivables and contract assets swing with the workload (RMB1,624M at the end of 2023 on sales of
RMB2,592M; RMB585M at the end of 2025); the cash swings with them, which is why owner cash moves by hundreds of millions
from year to year. Borrowings were cut from RMB806M (2018) to RMB86M (2024) and were raised again to RMB480M by June
2026 to fund the yard spending and the new EPC work. Capital spending ran well below depreciation from 2021 to 2024
(about RMB74M a year against about RMB124M of PPE depreciation and amortization) and then rose to RMB197M in 2025 and
RMB126M in the first half of 2026. What they do not say: the margin on any project before it is finished (three
qualified audit opinions turned on one such estimate, below), and whether the new EPC contracts will earn their cost.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the test is whether one would be content to own this yard business if the
market closed for five years, "Would I be happy buying this stock if the market closed for five years?" The question
bears hard here because the stock trades thinly (zero volume on several of the last six sessions) and the ADR trades
in hundreds of units; the market offers no exit and the owner must live on what the yards earn. The no-macro rule
bears too: the Chairman's Statement leans on IEA energy-investment forecasts and the PRC Five-Year Plan's 100GW
offshore-wind target; none of that enters, and the business is read off its own figures **[M2008-069]**. An
understood business abroad is asked a lower price rather than refused: "We wanted to get paid more for going into
China, and we did, because we don’t know the game as well there." **[M2006-021]**. **Contrary evidence, written down
as found** **[M1997-127]**: (1) the qualified audit opinions of FY2021, FY2022 and FY2023 over a liquidated-damages
provision (booked RMB65M, settled RMB138.6M); (2) the SDN listing of the principal yard under Executive Order 14024, the
Russia sanctions order, after it built modules for Arctic LNG 2; (3) a controlling shareholder that tried to replace
the board in 2022 and lost the vote 45 to 55; (4) a RMB512.7M payout from share premium in 2021, three and a half times
the prior year's profit; (5) a 2024 share award, bought in the market for RMB144.7M and vested on the day of grant,
when profit was RMB185.1M; (6) four capital raisings in five years; (7) three profit warnings in 2025 and 2026 and a
first-half 2026 loss; (8) 2025 profit before tax of RMB49.8M includes a RMB74.7M reversal of warranty provisions.

## THE STANDING RULE
The buyer's own conduct: a cash purchase of a thinly traded small share, sized so that its loss cannot touch what the
buyer has and needs, puts the buyer at no risk of ruin: "We are never going to risk what we have and need for what we
don’t have and don’t need." **[M2012-081]**. The one feature to state: the share is not easily sold in size (low daily
volume; the ADR rarely trades), so any holding must be one the buyer never needs to sell. Nothing in the target can
call on the buyer. No breach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "the first question is, can I understand it?" **[M1995-051]**, where understanding is "a reasonable
  fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**.
- **What the business is, from the filings.** Two yards in the PRC (Penglai, Shandong; Zhuhai, Guangdong) that build
  steel structures and process modules to customers' designs: offshore oil and gas platforms and jackets, LNG and
  petrochemical plant modules, FPSO topside modules, and now offshore-wind foundations and converter-station modules,
  with a move into EPC general contracting. Work is won "generally through tendering" and "The major customers of the
  year may not be the same as different projects undertaken each year" (FY2025 Directors' Report). Revenue is
  recognised over time on contracts; the yards carry a fixed overhead of about RMB216M a year (MD&A 2025).
- **The key variables and whether they are foreseeable** **[M1998-044]**. Two variables decide the result: the
  tonnage won in tenders, which sets yard utilisation, and the margin bid on it. Neither is foreseeable year by year:
  revenue went 659, 722, 724, 1,486, 1,761, 3,647, 3,982, 1,751, 2,592, 2,079, 800 (RMB M, 2015 to 2025). But the
  question Q1 asks is whether the economics can be read, not the timing. Twelve years of statements show their
  character plainly: a tendered fabricator whose capital earns low single digits through the cycle (about 2.7% a year on
  equity, 2014 to 2025), whose cash swings with working capital, and whose good years are single large contracts.
  Its workload follows its customers' spending on oil, gas and wind projects, a dependence on commodity cycles; the
  rows do not forecast those, "We don’t think we can predict commodity prices." **[M2016-025]**, and the framework
  routes such a business to be read off its figures, "if you can’t make a decision on something like PetroChina off the
  figures, forget about going further" **[M2008-069]** (Q2's commodity-business paragraph). Off its figures the
  business can be read **[M2023-031]**.
- **Fast change?** Steel module fabrication is not fast-moving technology; the products (jackets, modules, converter
  stations) change in size and customer, not in the economics of the yard. The routing to TOO HARD for rapid change
  does not apply.
- **Abroad.** A Cayman holding company with PRC operating subsidiaries, reporting under HKFRS, audited, listed in Hong
  Kong with a Hong Kong company secretary and Listing Rules disclosure; governance and tax can be read from the reports,
  "where we think we understand the nuances of the corporate governance system and taxation" **[M2000-141]**. The rows
  ask a lower price for the less familiar country, not a pass **[M2006-021]**.
- **The doubt test** **[M2002-092]**. The doubt that exists is about the outcome (sanctions, the new EPC line, order
  intake), not about what kind of business this is or how it earns; those doubts are Q2's and Q7's to weigh. The
  economics of a contract yard are inside the perimeter of a reader of its accounts.
- **The OFAC matter at Q1.** The SDN listing of Penglai Jutal (2024-06-13, HKEX 2024061300915) is a fact about the
  competitive position (which customers and banks will deal with the yard), carried to Q2; it does not make the
  economics unreadable.

**VERDICT: IN.** The economics of a tendered fabrication yard can be understood from twelve years of its own
statements **[M1995-051]**, **[M2012-065]**, **[M2008-069]**; the unforeseeable variables are the cycle and the
order book, which the framework weighs at Q2 and Q7, not here **[M2016-025]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**; a moat is what "protects excellent returns on invested capital"
**[L2007-004]**. Rivals: the annual reports name none (a text search of every report FY2013 to FY2025 for "competitor"
and for the obvious names found only generic uses), so the three read here are a **CONVENTION of this run**: the
nearest listed businesses of the same kind with their own primary filings, one for each of Jutal's lines. Rationale:
the brief asks for rivals from their own filings and the reports supply no names. They are Offshore Oil Engineering Co.
(COOEC, Shanghai 600583, 55.39% held by CNOOC; annual report summaries FY2016, FY2019, FY2022, FY2025 from cninfo,
files 1203181220, 1207393347, 1216167461, 1225023909), Wison Engineering Services (HKEX 02236, refining and chemical
EPC; annual reports 2015, 2020, 2025, HKEX ltn20160427847, 2021042500007, 2026042400107) and Gulf Island Fabrication
(SEC filer, steel modules and structures; XBRL facts, FY2024 net income cross-checked to the filed 10-K, accession
0000950170-25-032540). Not read and flagged: CIMC Raffles, BOMESC, Dalian Shipbuilding Offshore, the Korean and
Singapore yards, McDermott; Wison's own module yard (Wison Offshore & Marine) is outside the listed company. Figures and
file references in `rivals.md`.

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on
   See’s Candy, could I do it?" Here the filings answer it: capacity in this trade is bought with capital. Jutal itself
   is buying it, a new 50,000-tonne berth at Zhuhai (Quay#2) at an estimated RMB200M, new workshops, gantry cranes and a
   skidway, because "the current site conditions and facilities are insufficient to meet the requirements of new and
   future potential projects" (FY2025 Chairman's Statement). The largest domestic rival, COOEC, had 2025 revenue of
   RMB27.2B against Jutal's RMB0.8B and is controlled by the state oil company that is a principal customer of the
   trade. The Chairman's claim that "only a few of domestic construction sites, including those of the Group, can meet
   the construction and delivery requirements" for large converter stations is a claim about present yard size, which
   money is adding to, his own included. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
2. **Pricing power and the agony before a rise** **[M2005-020]**: none shown. Work is tendered contract by contract.
   Gross margin by year: 19.6%, 19.6%, 16.9%, 12.3%, 12.1%, 18.2%, 12.3%, 7.1%, 2.4%, 25.3%, 27.3%, 22.7% (2014 to
   2025), and 0.9% in the first half of 2026. On one delayed contract the yard paid liquidated damages of RMB138.6M
   against RMB29.0M received for extra work (FY2022 Corporate Governance Report). The margin is set by the bid and the
   utilisation, not by the yard.
3. **Unit volume and share of mind**: there is no product asked for by name. Tonnage swings with single contracts (the
   Arctic LNG 2 module contract alone was "over RMB3 billion", FY2019 Chairman's Statement), and "The major customers
   of the year may not be the same as different projects undertaken each year" (FY2025 Directors' Report).
4. **The low-cost position** **[M1997-010]**, **[M2006-004]**: "commodity businesses have risk unless you’re the
   low-cost producer". No filing states a cost per tonne for Jutal or its rivals; the cost position shows instead in
   what the capital earns through the cycle, "The figures are available." **[M2009-059]**. Jutal's return on average
   equity averaged about 2.7% from 2014 to 2025; COOEC's weighted return on equity averaged about 6.6% over the same
   twelve years (about 4.1% from 2016). Jutal was ahead of COOEC in six of the twelve years and behind it on the
   average and in the worst year (-11.7% in 2022, when COOEC earned 6.3%). Nothing in the filings shows Jutal as the
   low-cost producer.
5. **Would the customer still choose it over the low bid?** **[M2017-009]**: the customers tender; "it wouldn’t be a
   question of people buying candy for the low bid" is exactly the condition that does not hold here. The FY2024 10-K of
   the SEC-filing rival says the same of the trade: contracts "awarded on a competitively bid and negotiated basis". The
   kin row: "most insureds don't care from whom they buy" **[L2004-003]**.
6. **Ask the competitors**: not on the public record; not done (scuttlebutt is outside a filings run).
7. **Widening or narrowing** **[M1999-108]**: narrowing on the evidence. In June 2024 OFAC placed the principal yard,
   Penglai Jutal, on the SDN List under Executive Order 14024 (HKEX 2024061300915), after it built core modules for the
   Arctic LNG 2 project in Russia; the Chairman wrote that this "has significantly affected intentions of some clients
   for the business cooperation and is bringing uncertainties to Penglai Jutal's potential orders and some contracts
   settlement" (FY2024 Chairman's Statement). The removal application was filed 2025-10-14 and was still awaiting
   feedback at the 2026 interim report. Revenue fell 61.5% in 2025; the first half of 2026 lost RMB70.9M. The growth
   line, EPC general contracting, includes "new business types undertaken by the Group" (FY2025 Prospects), not a
   defended position.
8. **What could destroy, modify or reduce it** **[M2000-014]**: the sanctions (a listed yard loses any customer or bank
   that will not deal with an SDN entity); the fixed overhead of two yards against a falling workload (MD&A 2025:
   indirect manufacturing costs "have not decreased proportionally"); and the plain rule of the trade, "one competitor
   is frequently enough to ruin a business" **[M2012-108]**, and "the improvement you get one day, your competitor gets
   the next day" **[M2004-053]**.

**The competitor row** (from each company's own filings; Jutal's return on average equity computed from its statements;
COOEC's weighted return on equity as it reports it; Wison's profit attributable to owners, RMB M; Gulf Island's net
income, US$M):

| Year | Jutal ROE % | COOEC ROE % | Wison owners' profit | Gulf Island net income |
|---|---|---|---|---|
| 2014 | 2.7 | 22.80 | 179.0 | 15.3 |
| 2015 | 2.3 | 15.94 | 205.1 | -25.4 |
| 2016 | 1.0 | 5.72 | 15.2 | 3.5 |
| 2017 | 3.4 | 2.13 | 138.3 | -44.8 |
| 2018 | 1.3 | 0.35 | 56.3 | -20.4 |
| 2019 | 0.2 | 0.12 | 50.6 | -49.4 |
| 2020 | 6.7 | 1.61 | -271.2 | -27.4 |
| 2021 | 0.5 | 1.64 | -92.6 | -22.2 |
| 2022 | -11.7 | 6.30 | -1,185.5 | -3.4 |
| 2023 | 13.6 | 6.67 | -196.1 | -24.4 |
| 2024 | 8.8 | 8.47 | 141.6 | 14.7 |
| 2025 | 2.1 | 7.78 | 142.4 | not read |
| Twelve years | average about 2.7 | average about 6.6 | sum about -817, on equity of RMB1.8B to 3.8B | sum about -184 (2014 to 2024), equity down from 286 to 93 |

**The parts table** (the filer reports two segments with different results; the MD&A's gross profit by segment is used
as the filer's own split, the segment-results note not read; RMB M, 2021 to 2025): oil and gas fabrication and services,
gross profit 420, 103, 532, 451, 247 = **1,753, about 101% of the five-year group gross profit of about 1,730: decides**;
new energy and refining and chemical, -137, -61, 123, 117, -65 = -24, open, not deciding; "lumping them together [...]
impedes analysis" **[L2008-005]**. The file closes on the oil and gas part, whose castle is the one tested above. The
new-energy part is the one the company is building toward (offshore wind), and it lost money at the gross line in three
of the five years.

**The field's returns over the last full cycle** (judged in words; the framework's CONVENTION gives "ordinary" no
figure): the cycle from the 2014 peak of offshore spending through the 2015 to 2021 downturn, the 2023 to 2024 upswing
and the 2025 to 2026 fall is inside these filings. Over it the strongest player, the state-controlled COOEC, earned
ordinary returns, low single digits for six straight years (2016 to 2021) and six to eight and a half percent since; the
refining EPC rival lost money in aggregate; the SEC-filing fabricator lost money in eight of eleven years; and Jutal
earned about 2.7% a year, with two good years (2023, 2024) followed by 2.1% and a first-half 2026 loss. "you can have
only two competitors and they’re still terrible businesses" **[M2013-052]**; "there are some industries that are just
never going to have barriers to entry" **[M2012-106]**. A change for the better is credited only on a full cycle in
which the price behaviour held **[M2005-020]**, **[L1995-022]**; the 2023 to 2024 improvement did not hold into the
next downturn, and "the railroads were a terrible business for decades and decades and decades and then they got good"
**[M2017-026]** names a change these filings do not show. Price does not reopen it: "What you can’t do is turn any
investment into a good deal by paying little" **[M2019-015]**; "Time is the enemy of the poor business" **[M1998-006]**.

**Which closing ground decides.** Q2's commodity-business paragraph sends a file to TOO HARD (WORK) where the cost
position cannot be read because the operators' reports were not read. That is not the deciding ground here: the
deciding ground is the item on Q2's OUT list, a field whose durable players earn ordinary returns over a full cycle on
the evidence of the filer's and the rivals' own filings, which are read above; with it, the castle tests show a
tendered product bought on the bid **[M2017-009]**, capacity that money is adding **[M2011-015]**, and a position
narrowing under sanctions. The castle is shown open on the evidence, not merely unjudgeable **[M2000-019]**, so the box
is OUT, not TOO HARD **[M2006-013]**.

**VERDICT: OUT.** No castle: tendered work bought on the bid **[M2017-009]**, capacity that capital can and does add
**[M2011-015]**, no low-cost position shown against the largest rival over twelve years **[M1997-010]**,
**[M2009-059]**, and a field whose returns over the full cycle are ordinary at best **[M2013-052]**, **[L2007-004]**;
the one good stretch (2023 to 2024) did not hold **[M2005-020]**. The file closes here. Q3 to Q12 NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 as the template asks; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP. Buyback line for the Q7 range: the company made no share repurchases for
cancellation in the years read; the 2024 market purchases (228,750,000 shares for HK$158.56M) were for the share award
scheme, not a buyback, so there are no buyback prices to set against the bottom of the computed range.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The reporting figures are computed below under **COMPUTATION, NOT A CLEARANCE**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts under AFTER THE STOP.

---
## THE BOX
**OUT at Q2** (no castle: tendered work bought on the bid, capacity that capital adds, no low-cost position shown, a
field earning ordinary returns at best over the full cycle, and a position narrowing under the SDN listing); **integrity
facts recorded, not judged**. COMPUTATION, NOT A CLEARANCE, on the Q7 construction: value range about HK$1.62 to
HK$2.77 a share (RMB1.39 to 2.37) at the RMB 30-year rate, against HK$0.38; fair price about HK$0.53 all-equity
(HK$0.39 equity-only); both rest on a cycle base that the twelve-year record does not support (below). Q11 belongs to a
holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2; each with its source* **[M1997-127]**.*)*

**Bearing on Q3 (capital).** Equity rose from RMB1,019M (end 2013) to RMB2,188M (end 2025) on about RMB1.18B paid in by
shareholders, against cumulative net profit of RMB0.59B and dividends of about RMB0.69B (Step 0 tables). Capital
spending ran below depreciation 2021 to 2024 (about RMB74M a year against about RMB124M of PPE depreciation and
amortization), then rose to RMB197.3M (2025) and RMB125.9M (first half 2026); the new Zhuhai berth is budgeted at about
RMB200M (FY2025 MD&A, Significant Investment). The rows' picture of this kind of account: "the gruesome account both pays
an inadequate interest rate and requires you to keep adding money at those disappointing returns" **[L2007-010]**.

**Bearing on Q4 (the accounts).** The auditor qualified the FY2021 opinion: it "was unable to obtain sufficient
appropriate audit evidence to support the carrying amount of the provision for liquidated damages" (booked RMB65M; the
contract terms implied "materially in excess of the amount provided"; FY2021 annual report, independent auditor's
report). FY2022 was qualified on the same provision after it settled at RMB138.6M (RMB73.6M charged in 2022); FY2023 was
qualified by the new auditor for comparability (FY2023 Corporate Governance Report); FY2024 and FY2025 opinions are
unmodified ("BASIS FOR OPINION"). FY2025 profit before tax of RMB49.8M includes a RMB74.7M net reversal of warranty
provisions (FY2025 cash-flow statement adjustments), without which the pre-tax result is a loss of about RMB24.9M. In
FY2024 share-based charges were RMB116.2M (RMB21.8M options, RMB94.4M awards), 63% of that year's profit of RMB185.1M;
the award shares were bought in the market and vested on the day of grant (FY2024 note 42(b)). Two clarification
announcements corrected typographical errors in disclosure tables (2024-03-08, 2024-08-05). Revenue is recognised over
time on milestone contracts, the kind of matching the rows warn of, "when you don’t have a product where
revenues and expenses are being matched up on something close to cash in the short-term" **[M1995-065]**. The
confusion test is the rows': "when the accounting confuses you, I would just tend to forget about it as a company"
**[M1995-063]**. Not weighed here.

**Bearing on Q5 (integrity; recorded, not judged).**
- In June 2024 OFAC listed the principal operating subsidiary, Penglai Jutal, under Executive Order 14024 (HKEX
  2024061300915). The yard had built core modules for Arctic LNG 2, a Russian Arctic project, under a contract "over
  RMB3 billion" awarded in July 2019 (FY2019 Chairman's Statement). By 2025-10-14 "Penglai Jutal has ceased construction
  business of projects involving the SDN List" (HKEX 2025101400296). The filings read do not say when the Russian work
  stopped relative to the sanctions on that project.
- The chief executive and president, Cao Yunsheng, resigned "due to his other job assignment" on 2024-06-24, eleven
  days after the listing (HKEX 2024062400207); he came from the controlling shareholder's group (FY2017 directors'
  biographies).
- In July 2022 the then controlling shareholder, Sanju HK (now held by Beijing Haixin Energy Technology, Shenzhen
  300072), requisitioned an EGM to elect five directors and to require the Chairman to report on performance, on the
  qualified opinion and on "any corporate governance issues that may exist" (HKEX 2022080301679); every resolution failed,
  about 44.9% for and 55.1% against (HKEX 2022082600605). The founder-chairman, Wang Lishan, holds about 20.9% (18.61%
  through Cheung Hing Investments and 2.33% direct; rights-issue results, HKEX 2026031901220); Sanju HK 25.78% after
  declining its rights.
- In 2024 the Company spent HK$158.56M (RMB144.7M) buying 228,750,000 of its own shares through a trustee and awarded
  164,000,000 of them to directors and employees, vesting immediately; the Chairman received 32,000,000 (FY2024
  Directors' Report). The 2024 interim dividend (RMB54.9M) was paid the same year.
- Four share issues for cash in five years (2022 placing, 2024 placing at HK$0.42, 2026 rights issue at HK$0.16, plus
  the 2017 subscription at HK$1.20 when the share closed at HK$2.00); shares in issue rose from 800,354,278 (2016) to
  2,488,835,287. The rows on serial issuers: "we have never invested in companies that are hell-bent on issuing shares"
  **[L2014-015]**. Profit warnings were issued 2025-02-13, 2025-08-04, 2026-03-03 and 2026-08-04.
- The test that would apply: "If you’ve got doubts, forget it." **[M2013-088]**; things done "in public in relation to
  their investors and the promises they make" **[M2004-067]**. Any later run that reaches Q5 must answer these.

**Bearing on Q6 (the money and the owners).** RMB512.7M paid to shareholders in 2021 from the share premium account
(HK$0.15 special interim and HK$0.22 final for 2020), more than three times 2020 profit, after which borrowings rose
and new shares were placed in 2022. No buybacks for cancellation. The 2026 EGM (6 November) re-proposes articles
amendments, including power to hold treasury shares, after the June 2026 AGM failed to pass them by the 75% needed (HKEX
2026101400321).

**Bearing on Q9 (debt and exposures).** Borrowings RMB479.9M at 30 June 2026 against bank cash RMB641.2M, securities
RMB81.4M and pledged deposits RMB53.8M; performance bonds issued by banks for the Group RMB305.2M at end 2025; five
largest customers 63.26% of 2025 sales; contract liabilities (customer advances) up from RMB10.9M to RMB199.1M in the
first half of 2026 on the new EPC contracts. The sanctions are a counterparty exposure for every customer and bank. The
"little or no debt" criterion **[R1997-001]** is stated for whole businesses.

**Bearing on Q12.** The money of 2019 to 2023 included the Arctic LNG 2 modules for which the US Treasury later
sanctioned the yard; the rows' instrument is the newspaper test, "if a story were written by an unfriendly but
intelligent reporter" **[M2008-011]**. Not weighed.

## COMPUTATION, NOT A CLEARANCE (the reporting figures, at the owner's request; not a verdict, no entry language)
Built by Q7's range convention, on the all-equity basis with the equity-only figure beside, after the company's own
tax (operating cash as filed is after tax paid), at the RMB 30-year rate of 2.06%; arithmetic in `valuation.py`.

1. **The window and the cycle (specific (a)).** The literal window 2021 to 2025 averages OC_ae RMB54.6M (OC_eq RMB49.0M).
   Its last year is aberrational on the filer's own description: "the workload of the Group's construction sites
   decreased remarkably" (FY2025 MD&A; revenue -61.5%). The rows: "If either year was aberrational, any calculation of
   growth will be distorted." **[L2005-003]**. The series that defines the cycle, owner cash, peaks in 2020 and 2024 and
   troughs in 2018, 2022 and 2025, and the first half of 2026 is lower still (operating cash -RMB148.2M, capex
   RMB125.9M), so the current trough is not yet complete. The base is therefore the last full cycle peak to peak,
   2021 to 2024: **OC_ae RMB117.0M, OC_eq RMB109.2M**. Beside it: the prior cycle trough to trough, 2019 to 2022, OC_ae
   RMB155.2M; the twelve years 2014 to 2025, OC_ae RMB22.7M.
2. **Growth (specific (b)).** The prior peak-to-peak cycle (2016 to 2019) averages OC_ae of about -RMB179M, so growth
   between successive cycles changes sign and is meaningless; the halves of the literal window go from -RMB60.2M to
   +RMB71.8M, also a sign change. **The range is the no-growth case alone, said so.**
3. **Spending (the PG specific and (e)).** All capital spending is deducted in the central case. The filing gives no
   maintenance figure; the only spending it names as growth is the Zhuhai expansion and Quay#2 (supplementary
   announcement 2026-10-09). Over the cycle base, capital spending (RMB73.6M a year) ran below PPE depreciation and
   amortization (RMB123.9M a year), and spending has since risen well above it. Depreciation is "almost always true
   costs" **[L2015-004]** and "not inappropriate in most companies to use as a proxy for required capital expenditures"
   **[M1998-127]**. **CONVENTION of this run:** where the all-spending case on the cycle base rests on capital spending
   below depreciation, the depreciation variant (depreciation charged in place of capital spending) is carried as the
   bottom of the range and the all-spending case as the top; rationale: the no-growth range has only one growth case,
   and charging less than depreciation forever would count a yard run down as earnings. Depreciation variant on the cycle
   base: **OC_ae RMB66.8M, OC_eq RMB58.9M**.
4. **Acquisitions (c):** none in the window (the 2017 Penglai purchase lies outside it). **Working capital (d):** counted
   (operating cash as filed). **Cap (f):** not engaged (no growth carried). **Tax:** the company's own; no carryforward
   shelter was examined (not read). **Net debt:** net cash RMB221.3M at 30 June 2026 (bank cash plus securities less
   borrowings and leases; pledged deposits excluded, said so); no later subsequent event stated in that filing.
5. **The floor first.** At HK$0.38 the enterprise value is RMB588.8M; the expected return at no growth is 19.9% on the
   top case and 11.3% on the bottom (equity-only: 13.5% and 7.3%), so on the cycle base some case clears the floor
   **[M2003-149]**. On the literal window the top case returns 9.3% and on the twelve years 3.9%, both below it.
6. **VALUE RANGE (all-equity):** RMB1.39 to RMB2.37 a share = **HK$1.62 to HK$2.77 a share** (per ADR HK$406 to HK$692),
   width 1.70 to one, against HK$0.38. Equity-only beside: RMB1.15 to RMB2.13 = HK$1.34 to HK$2.49.
7. **FAIR PRICE (Part VII; each end valued at ten percent, the two averaged):** all-equity **RMB0.458 = HK$0.535 a share**
   (per ADR HK$133.7 = US$17.04); equity-only beside **RMB0.338 = HK$0.394 a share** (per ADR HK$98.6 = US$12.56).
   Beside them, the same arithmetic on the literal window gives HK$0.31 all-equity (average of HK$0.360 and HK$0.267), and
   on the twelve-year record about HK$0.21.

**What the computation does not say, written down as found** **[M1997-127]**. The cycle base 2021 to 2024 is the
stretch in which the yard delivered the Arctic LNG 2 core modules, the work for which it was later sanctioned; the
twelve years together average a tenth of that base on the equity-only basis; and the years since (2025 and the first
half of 2026) are negative. The range is narrow only because growth is meaningless and only two spending cases exist,
not because the cash is predictable: on the rows' own reading "the range must be so wide that no useful conclusion can be
reached" **[L2000-025]**, and a wide uncertainty is not cured by a bigger discount **[M2007-022]**. The price sits below
fair on the cycle base and above fair on the literal window and on the twelve-year record. None of this reopens Q2.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit aad7b07f); written question by question; committed after Step 0
      (0aa93675), Q1 (38313358) and Q2 (4edf6937), and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's (not written
      or touched here); the run binds nothing until folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident
      (commit subjects, other research-folder names, memory-index lines) is declared under contamination above.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `check_ids.py` in the research folder); every
      filing fact carries its HKEX file reference or SEC accession; no E-ids.
- [x] The order was kept; Q2's STOP closed the run; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash from the filed cash-flow statements after every real cost, never a net-income proxy (operator rule 5);
      the sovereign from the PRC Ministry of Finance curve, dated; the share and ADR quotes are aggregator quotes,
      flagged; the FX rate is the CFETS central parity, dated.
- [x] Contrary evidence written down as found (Foundations, eight items; the computation's closing paragraph); the
      facts found for later questions are under AFTER THE STOP, with "integrity facts recorded, not judged" in the box.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] `tools/run.py` and `Screens/cover_shares.py` refused the name; no tool output was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the closing commit message).
- Honest limits: the segment-results note and the tax notes were not read; COOEC was read from its annual report
  summaries only (Chinese), not its full reports; Gulf Island's FY2025 was not read; the rival set is this run's choice;
  the 2017 Penglai acquisition consideration and its settlement were not traced; the H1 2026 owner cash is approximate
  (operating cash less PPE purchases only).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The cycle base can carry a vanished customer.** Specific (a) sends an aberrational end year to the last full
cycle's average, and here the only full cycle in owner cash is the one carried by a Russian contract that later got the
yard sanctioned; the convention has no clause for a cycle whose peak came from business the company can no longer do.
I followed the text and showed the literal window and the twelve-year record beside it; an operator reading "price below
fair" from the central figure would be reading the Arctic LNG 2 years. (2) **Peak to peak is ambiguous in its years.**
"The average over the last full cycle, peak to peak" does not say whether both peak years are counted, or which of two
equally valid one-peak spans (2020 to 2023 gives RMB205.0M; 2021 to 2024 gives RMB117.0M) is meant; I took the span
ending at the latest peak and said so. (3) **No-growth ranges have one end.** Where specific (b) leaves only the
no-growth case, the range collapses to a point and the width test and the fair-price average of "each end case" have
nothing to work on; I confessed a run convention (depreciation variant as the bottom). (4) **Working capital swings
dominate a contractor's owner cash** (RMB-637M in 2018, RMB+691M in 2020); specific (d) counts working capital, which is
right over a cycle, but a four-year cycle average still depends on where in a contract's life the years fall. (5) **The
commodity-business paragraph's TOO HARD (WORK) route** (cost position unreadable because operators' reports were not
read) sits beside the OUT item for ordinary field returns; for a contract fabricator no filing states a cost per tonne, so
the two clauses could send the same file to different boxes. I decided on the OUT item because its evidence (the field's
returns from its own filings) was read; the text does not say which governs. (6) **The sovereign table** covers USD, JPY
and EUR only; the RMB rate was taken from the PRC Ministry of Finance curve published through ChinaBond, which the brief
anticipated but the protocol does not name.
