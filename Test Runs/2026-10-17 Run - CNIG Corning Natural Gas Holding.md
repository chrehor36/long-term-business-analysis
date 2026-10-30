# Company Run — Corning Natural Gas Holding Corporation (formerly OTCQX: CNIG; delisted and deregistered July 2022) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run, unattended overnight. Brief: `C:\Users\chreh\AppData\Local\Temp\cnig_brief.md`, which departs from the
canonical brief in one stated place (the analyst derives the lines of evidence from the 10-K) and notes that the company stopped
filing with the SEC in July 2022. Research folder: `Test Runs/_research 2026-10-17 CNIG/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (e8f6f655): `PORTFOLIO.md` read for this one ticker; the operator does not hold CNIG (no line names CNIG or Corning).*

**Contamination declared (seen by accident, not used):** (1) the opening `git log --oneline -3` printed the subjects of the last
three commits, which name another company's v5 re-run (CLNE) and its box; nothing of it bears on this name and none of it is
used. (2) Before the template was copied, one filtered listing of `Test Runs/` for file names containing "cnig" or "corning"
was run to make sure the dated file name was free; it returned nothing. A name listing is a listing under the blind rule, so it
is declared here; no file was opened and nothing was learned. (3) The memory index loaded into this session names an older
queue state and a count of gate-clearers; it names no company and is not used.

**Lines of evidence chosen from the latest 10-K (fiscal 2021, filed 2021-12-17, accession 0001174947-21-001128), as the brief
asks:** (L1) the regulated earning power: the rate orders of the New York PSC and the Pennsylvania PUC, the allowed returns and
the earnings sharing (Item 1, Regulatory Matters; Item 7, Overview and Regulatory Matters); (L2) the climate laws and their
treatment by the regulator: the CLCPA and "government-imposed limitations, prohibitions or moratoriums on the use of gas"
(Item 1A; Item 7, Environmental Matters); (L3) the capital the system needs against the cash it produces, and the financing
that fills the gap (Item 1A, "Our cash flows from operations may not be sufficient"; Item 7, Liquidity and Capital Resources);
(L4) customer concentration and bypass (Item 1, Significant Customers; Item 1A, competition by direct connection to an
interstate pipeline); (L5) the pending Argo merger and the delisting it brings (Item 1, Pending Merger; Item 1A, first risk).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price: none exists.** No share or other security of this company can be bought today. The evidence, in order:
  - 8-K of 2022-07-06 (accession 0001174947-22-000776), Item 2.01: on July 6, 2022 ACP Crotona Merger Sub Corp. merged into the
    company, "with the Company surviving as a wholly-owned subsidiary of Parent"; common shares were converted into the right to
    receive $24.75 in cash; Series A, B and C preferred into $25, $29.70 and $25 a share plus unpaid dividends; "The holders of
    these shares ceased to have any rights as the Company’s shareholders other than the right to receive the Merger
    Consideration and the Preferred Payment." Aggregate cash to shareholders about $99.6 million, funded by "equity contribution
    by investment funds affiliated with Argo."
  - Form 15-12G of 2022-07-07 (accession 0001174947-22-000800): registration terminated for the common stock, the 6% Series A
    Cumulative Preferred and the Series B Convertible Preferred; "Approximate number of holders of record as of the
    certification or notice date: One".
  - The Series D preferred (5,000 shares, $5 million) was issued on December 8, 2021 to ACP Crotona Corp. itself in a private
    placement (10-Q of 2022-05-12, accession 0001174947-22-000671, note on Series D); it was never a public security.
  - DEFM14A of 2021-04-22 (accession 0001174947-21-000427): "our stock will be delisted from the OTCQX and deregistered under the
    Exchange Act and we will no longer file periodic reports".
  - The company's own website (fetched 2026-10-17, excerpts in `Test Runs/_research 2026-10-17 CNIG/web_excerpts.txt`): the
    Merger Information page says the holding company and its subsidiaries "were acquired by Argo Infrastructure Partners/ACP
    Crotona on July 6th, 2022"; the press release of May 30, 2025 says "Corning Energy is wholly owned by funds managed by Argo
    Infrastructure Partners"; the corporate page lists "SEC Filings Prior to July 2022 Sale to Private Investment Group".
  - The company's debt is bank debt (M&T Bank term, demand and revolving loans; Wayne Bank loans) per the 10-K's Liquidity
    section; no instance found in the filings read of a publicly traded bond or note.
  - The price feed used by `tools/run.py` returned HTTP 404 for CNIG (2026-10-17). To let the arithmetic lines print, the run
    was wrapped (`Test Runs/_research 2026-10-17 CNIG/run_wrap.py`) with the 2022 merger consideration of $24.75 as a
    placeholder. **$24.75 is a historical cash-out price paid by a private buyer in 2022, not a price at which anything can be
    bought; it is shown nowhere below as a price.** For reference only: the last OTCQX quarterly range in the filings is
    $23.00 to $24.65 for the quarter to September 30, 2021 (10-K Item 5), and the DEFM14A gives the pre-announcement close of
    $16.45 on January 12, 2021.
- **Shares by class**, last filed: common 3,083,577 (10-K cover, as of December 17, 2021; 10-Q cover, as of May 12, 2022,
  accession 0001174947-22-000671; the 10-Q balance sheet shows the same count issued and outstanding at March 31, 2022, no
  treasury shares). Preferred at March 31, 2022: Series A 260,600; Series B 244,263 (convertible, temporary equity); Series C
  180,000; Series D 5,000. `python Screens/cover_shares.py CNIG` returned "NOT AN SEC REGISTRANT in the live ticker file"; the
  count is taken from the cover pages above. Since July 6, 2022 every common share has been held by ACP Crotona Corp.
- **Market cap:** none; no market. (At the merger, common consideration was 3,083,577 x $24.75 = $76.3M; total cash to all
  shareholders about $99.6M per the 8-K. Historical, not a price.)
- **Sovereign for the earnings currency:** USD 5.43%, US Treasury daily par yield curve, 30-year, 10/16/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for fiscal 2021 (2021-12-17, 0001174947-21-001128), Items 1, 1A, 5, 7, 11, the cash
  flow statement and the segment note; the 10-Q for the quarter to March 31, 2022 (2022-05-12, 0001174947-22-000671), balance
  sheet and Series D note; the 8-Ks of 2022-07-06 (0001174947-22-000776), 2022-06-17 (0001104659-22-072432), 2022-03-22
  (0001174947-22-000391), 2022-01-14 (0001174947-22-000044), 2022-01-05 (0001174947-22-000024), 2021-12-22
  (0001174947-21-001161); Form 15-12G (0001174947-22-000800); DEFM14A (0001174947-21-000427), background and reasons; the 10-Ks
  for fiscal 2020 (0001174947-20-001229), 2019 (0001582244-19-000049), 2018 (0001582244-18-000068), 2017
  (0001582244-17-000114) and 2016 (0001582244-16-000187), segment notes and cash flow statements. Proxy: no DEF 14A was filed for
  fiscal 2021; Part III is inside the fiscal 2021 10-K (Item 11 read).
  **One figure cross-checked against the filed statement:** net income for fiscal 2021, $1,524,903 in the 10-K's key-indicator
  table, against $1.52M in the XBRL series `tools/run.py` used; and stockholders' equity at September 30, 2021, $35,472,550 on
  the 10-Q's comparative balance sheet, against $35,473K in the XBRL table. Both agree.
- `tools/run.py` arithmetic lines only (wrapped, see above; output in `Test Runs/_research 2026-10-17 CNIG/run_py_output.txt`):
  operating cash, capital spending and D&A for fiscal 2017 to 2021 agree with the filed cash flow statements. Two corrections
  from the filings: (a) stock pay is NOT absent: the cash flow statements carry "Stock issued for services and stock option
  expense" of $149,510 (FY2017), $223,783 (FY2018), $239,481 (FY2019), $197,180 (FY2020) and $96,211 (FY2021), which the tool
  reported as not found; (b) cash paid for businesses sits on its own line outside capital spending: the Leatherstocking
  acquisition, $1,893,081 in FY2020, and a $724,544 receipt on the Pike purchase price in FY2017. Recast in
  `Test Runs/_research 2026-10-17 CNIG/calc.py` (output `calc_output.txt`): **owner cash after every real cost** (operating cash
  less stock pay, less all capital spending, less net cash paid for businesses), USD millions: FY2017 -2.92, FY2018 -2.17,
  FY2019 -0.26, FY2020 -5.22, FY2021 -6.84; **five-year average -3.48**. Depreciation variant (depreciation and amortization in
  place of capital spending): 0.47, 2.78, 3.08, 0.10, 0.13; average 1.31. Capital spending ran 2.1 to 2.7 times depreciation
  and amortization in every year. The window's last year is five years before the run date; no later financial statement of the
  company is public on EDGAR.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own it "if the market closed for five years"
**[M1997-109]**, and here the market has in fact closed for good: the business goes on, the quotation is gone, and the owner is
a single private fund. The market serves, it does not instruct, and "It just tells us prices" **[M2006-077]**; this name has no
price to tell. The price is never waived: "we don’t do anything when the phrase “regardless of price” enters into the sentence"
**[M2008-041]**, and the same row says why a private seller is no source of bargains, "The stock market gives you bargain
prices; individual owners won’t." **[M2008-041]**; and earlier, "in the stock market, you get a chance to buy businesses at foolish prices" **[M1994-040]**. Who is paid to tell you: the only valuation of the
equity on the record is the fairness opinion and the "14.3 times EBITDA" multiple in the merger proxy, written for a seller.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the board itself, recommending the sale, listed "a burdensome
regulatory framework for utilities imposed by the State of New York" and "limitations on our ability to finance growth"
(DEFM14A, Reasons); (2) the NYPSC's order of May 19, 2021 denied a requested $6.2M increase and ordered a base-rate decrease
of $766,000 citing "pandemic austerity", lower than its own staff recommended (10-K Item 7); (3) capital spending exceeded
operating cash in every year of the window, and the 10-K says new debt and equity "will be required"; (4) the company's own
press release of July 31, 2024 names, among the three largest drivers of its rate request, "additional depreciation expense
resulting from the shortening of service lives of Corning's system to reflect the impact of the Climate Leadership and Community
Protection Act" (web excerpt); (5) there is no security to buy.

## THE STANDING RULE
No purchase can be made, so no financing, size or holding of the buyer's is in question; nothing in this run puts the buyer at
risk of ruin **[M2012-081]**, **[L2023-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic
  dynamics of the industry" **[M2011-014]**.
- **What the business is** (10-K FY2021, 0001174947-21-001128, Item 1): natural gas and electric distribution under franchise.
  Corning Gas serves about 15,000 customers around Corning, Hammondsport and Virgil, New York, and wholesales to the gas
  utilities of Elmira and Bath; "It is franchised to supply gas service in all the political subdivisions in which it operates"
  and is rate-regulated by the NYPSC. Pike serves about 4,900 electric and 1,300 gas customers in Pike County, Pennsylvania;
  Leatherstocking Gas distributes gas in Susquehanna and Bradford Counties, Pennsylvania; both under the PAPUC. 73 employees.
- **The parts** (segment note, 10-Ks FY2017 to FY2021): segment operating profit taken as net income plus income tax plus
  interest, USD millions, five years FY2017-21: Gas Company 2.81, 4.35, 5.28, 5.72, 4.79 (sum 22.95); Pike 2.14, 1.75, 1.68,
  1.12, 1.41 (sum 8.11); Leatherstocking (from July 2020) -0.09, -0.10; holding company negative every year. **The Gas Company
  carries about 74% of the positive five-year operating profit and decides** (Q2's business-of-parts paragraph, which defines
  "matters" for Q1 as well). Pike, the electric part, does not decide.
- **The key variables and whether they are foreseeable** **[M1998-044]**. The earning power of a regulated distributor is the
  allowed return on the rate base, less what the regulator disallows and the lag before rates catch costs. The filings state
  each variable: the rate base grows with mandated main replacement (9.0 miles of bare steel main replaced in FY2021); the
  allowed return was set at 9.25% for the three rate years to June 30, 2025, with sharing above 9.75% (8-K of 2022-06-17,
  0001104659-22-072432); the cost of gas passes through ("Purchased gas costs are subject to a NYPSC approved reconciliation
  that permits recovery of all prudently incurred costs", Item 7); weather risk at Corning Gas is mitigated by "weather
  normalization and revenue decoupling clauses" (Item 1A). The past statements tell the shape of the future ones
  **[M2008-033]**: revenue follows the rate orders and earned returns follow the allowed returns with a lag.
- **Contrary evidence written at once** **[M1997-127]**: the regulator is the variable, and its behaviour inside the window was
  not steady (the 2021 order cut base rates below its staff's recommendation on "pandemic austerity" grounds; the company sued
  under Article 78); and the 10-K says the climate initiatives "could impact the Company's customer base and assets depending on
  regulatory treatment afforded in the process" and "make it difficult to predict a long-term business impact across twenty or
  more years" (Item 7, Environmental Matters). The filer places that difficulty at "twenty or more years" and says climate
  impacts "would likely occur over a long period of time" (Item 1A), which is the horizon of the castle question (Q2's "ten or
  twenty years"), not the five-to-ten-year fix on earning power this question asks for.
- **Routing.** No fast-changing technology is in the economics; the product and the way it earns are plain. The doubt the
  filings raise is about how long the franchise lasts and what the regulator will allow, which is Q2's question (what keeps the
  castle standing ten to twenty years), and is carried there. On the five-to-ten-year earning power, I do not doubt that this is
  inside the perimeter of a reader of rate orders **[M2002-092]**, **[M2010-083]**.
- **VERDICT: IN.** A franchised, rate-regulated gas distributor whose earnings are the allowed return on a rate base the filings
  describe; the ten-year earning power can be fixed within a range from the rate orders **[M2012-065]**, **[M2000-037]**,
  **[M1998-044]**. The decisive uncertainty is the castle's life under the climate law, carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. Read on the deciding part, the Gas Company (Q1, the parts).

- **1. The key factors and how permanent** **[M1995-038]**. The castle is the franchise and the pipe in the ground: Corning Gas
  is "franchised to supply gas service in all the political subdivisions in which it operates", owns about 434 miles of main,
  15,000 services and 86 regulating stations (Item 1, Item 2), and is paid an allowed return on that plant. Its permanence is
  not set by competitors but by the New York legislature and the NYPSC, which approve the rates (Item 1A, "Our earnings may
  decrease in the event of adverse regulatory actions").
- **2. Without the lord.** It needs no superstar; a utility of 73 employees runs on its tariff. The skill that matters is in the
  rate case, and the 2021 order (below) shows even a well-argued case can be cut.
- **3. The money test.** No attacker with money would lay a second gas main in Steuben County **[M2011-015]**: on this test the
  castle stands. The attacks that exist are of another kind: substitution by electricity, "Historically, the competition [...]
  has been primarily from electricity for water heating and clothes drying" and "we could experience competition from customer
  owned solar in the future" (Item 1); and bypass, "If a major customer decided to connect directly to either an interstate
  pipeline or a local producer, our earnings and revenues would decrease" (Item 1A), where three customers (Corning
  Incorporated, NYSEG and Bath Electric, Gas & Water Systems) gave 14.98% of the Gas Company's revenue in FY2021 (Item 1).
- **4. Pricing power.** None of its own. Prices are set in rate cases: the NYPSC's order of May 19, 2021 (Case 20-G-0101) denied a
  requested $6,223,603 increase and ordered a $766,000 base-rate reduction, "lower than the rate increase recommended by the
  NYPSC staff", citing "pandemic austerity" (Item 7); the June 16, 2022 order then granted levelized increases of $1.7M, $1.8M
  and $1.7M with a 9.25% ROE (8-K 2022-06-17); the July 31, 2024 filing asks 13.76% a year for four years (company press release,
  web excerpt). The "prayer session" **[M2005-020]** here is a litigated proceeding with intervenors (UIU, PULP, Multiple
  Intervenors, the Village of Bath; 8-K 2022-03-22).
- **5. Volume.** Firm sales rose by 299,998.6 Mcf in FY2021 (Item 7); the customer count is about 15,000 against 13,000 in 1991
  (company timeline, web), slow growth over three decades.
- **6. The low-cost position.** Against other fuels: "The price of gas remains low in comparison to that of alternative fuels in
  our service territories and our competitive position in the residential, commercial and industrial markets continues to be
  strong" (Item 1). That is the fuel's position today, and the law is what may change it.
- **7 and 8. Brand and the low bid.** A customer cannot choose another gas distributor; he can choose another fuel, and the state's
  policy is aimed at that choice.
- **9. Ask the competitors.** No rival company is named in the 10-K; the named competition is fuels and solar (Item 1, Item 1A).
- **10. Widening or narrowing.** The one dated fact after the window points to narrowing: the company's own July 31, 2024
  release names "additional depreciation expense resulting from the shortening of service lives of Corning's system to reflect
  the impact of the Climate Leadership and Community Protection Act" among the three largest drivers of its rate request (web
  excerpt). The economic life of the castle is being written down, by the company, because of the law.
- **11. What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**. The 10-K names it: "Federal, state
  and local legislative and regulatory initiatives [...] could have significant impacts on the energy industry including
  government-imposed limitations, prohibitions or moratoriums on the use of gas"; the CLCPA "could ultimately impact the
  Company’s customer base" (Item 1A); it mandates emissions at 60% of 1990 levels by 2030 and 15% by 2050, and "These climate
  change and greenhouse gas initiatives could impact the Company's customer base and assets depending on regulatory treatment
  afforded in the process. [...] Changing market conditions and new regulatory requirements [...] make it difficult to predict
  a long-term business impact across twenty or more years." (Item 7, Environmental Matters). The board, recommending the sale,
  cited "a burdensome regulatory framework for utilities imposed by the State of New York" (DEFM14A, Reasons).
- **The competitor row.** The 10-K names no rival company, so the comparators are chosen. **CONVENTION of this run:** two
  SEC-filing gas distributors with nearly all their earnings in regulated distribution, RGC Resources (a small single-state LDC)
  and ONE Gas (a large three-state LDC); rationale: the field's returns are what Q2 section C asks for, and a franchised
  distributor's only rivals for capital are other franchised distributors. Named non-filers: none named as rivals; the two
  gas utilities Corning wholesales to (Elmira via NYSEG, and the Village of Bath's municipal system, which does not file) are
  customers, not rivals. Metric: net income over year-end common equity, from each filer's own 10-K XBRL facts
  (`Test Runs/_research 2026-10-17 CNIG/peers.py`):

  | filer | span | net income / equity, by year | mean | accession (last year) |
  |---|---|---|---|---|
  | Corning Natural Gas Holding | FY2013-21 | 7.6, 7.8, 6.0, 9.8, 6.5, 6.5, 9.1, 8.9, 4.3 | 7.4% | 0001174947-21-001128 |
  | RGC Resources | FY2013-21 (and 2022-25) | 8.6, 9.1, 9.6, 10.4, 10.4, 9.2, 10.5, 11.9, 10.1 (then -34.1, 11.2, 10.9, 11.7) | 10.0% (FY13-21) | 0001437749-21-027683; 0001437749-25-036827 |
  | ONE Gas | 2014-21 (and 2022-25) | 6.1, 6.5, 7.4, 8.3, 8.4, 8.8, 8.8, 8.8 (then 8.6, 8.4, 7.2, 7.7) | 7.9% (2014-21) | 0001587732-22-000019; 0001587732-26-000009 |

  Over the whole span Corning earned below both and below its own allowed returns (9.5% under the 2017 order, 9.25% under the
  2022 order); its best years reached the allowed level and its last filed year fell to 4.3%. RGC's FY2022 loss is shown and not
  explained here; its cause was not read, and it sits outside Corning's span.
- **The field's returns over the last full cycle**, judged in words: ordinary. A franchised distributor earns about what its
  regulator allows, single-digit returns on equity, and Corning earned less. Under section C a standing castle that protects
  only ordinary returns would close OUT, but the framework's Q2 list makes a return set by a regulator the exception, carried
  to Q3 as a second best; the row behind it: "there’s no way we get rich on our utility investments. But there’s no way we get
  poor, either." **[M2009-104]**. So the question is not whether the returns are rich; it is whether
  the regulated return will still be there for ten to twenty years.
- **Contrary evidence, the other side stated as well as I can** **[M1997-127]**: shortening service lives lets the company
  recover its invested capital faster, through rates, which is the regulator honouring the compact rather than breaking it; the
  2022 order granted increases and a 9.25% ROE; the climate effects "would likely occur over a long period of time". On that
  reading the castle shrinks in an orderly way and the owner is paid back. The rows name the other outcome for the same
  industry: "the regulatory climate in a few states has raised the specter of zero profitability or even bankruptcy [...] In such
  jurisdictions, it is difficult to project both earnings and asset values in what was once regarded as among the most stable
  industries in America." **[L2023-011]**, and "whether you earn X or go broke is not an equation that works" **[M2024-011]**.
  Which of the two New York will deliver for a gas distributor over the next twenty years is the deciding question, and the
  filings do not answer it. These rows speak of jurisdictions and an industry, not of this company; they are weighed with the
  tests and the filings and do not decide alone.
- **Why the box is TOO HARD and why the cause is NATURE.** The castle stands today and on test 3 no attacker could take it; what
  keeps it standing ten to twenty years is the legislature's and the commission's future treatment of gas service, which the
  filer itself declines to forecast ("difficult to predict a long-term business impact across twenty or more years",
  "depending on regulatory treatment afforded in the process") and has begun to price as a shorter life. That is a castle whose
  future cannot be judged: "it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone."
  **[M2000-019]**; where what could "destroy, or modify, or reduce the economic strengths" five to fifteen years out is
  impossible to figure, "we don’t even think about it then." **[M2000-014]**. It is not OUT: no filing shows the castle filling
  in on the evidence, and the regulated return is the stated exception to the ordinary-returns rule. The cause is NATURE, not
  WORK: the insiders, asked for the forecast, "would not want to put down on paper their predictions" **[M2000-105]** (said of
  technology companies; here the filer is the insider and says the same of its own business), and no filing not yet read could
  supply it, since it depends on laws and orders not yet made: "We couldn't solve this problem, moreover, even if we were to
  spend years intensely studying those industries." **[L1993-023]**. A lower price would not reopen it: "It doesn’t mean it
  isn’t a good buy. [...] It just means that we don’t know how to evaluate it." **[M2000-038]**; and here there is no price at
  all.
- **VERDICT: TOO HARD (NATURE)** on the deciding part's castle **[M2000-019]**, **[M2000-014]**, **[M2006-013]**, **[L1993-023]**.
  The file closes here. Q3 to Q10 and Q12 are NOT REACHED; the facts already found are written below, not weighed.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (closed at Q2).
## Q5 — WHO RUNS IT. NOT REACHED (closed at Q2).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (closed at Q2).
## Q7 — WHAT IS IT WORTH. NOT REACHED (closed at Q2); the reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED (closed at Q2).
## Q9 — COULD IT RUIN US. NOT REACHED (closed at Q2).
## Q10 — THE FAT PITCH. NOT REACHED (closed at Q2).
## Q12 (optional) — PROUD OF HOW THE MONEY IS MADE. NOT REACHED (closed at Q2).

---
## THE BOX
**TOO HARD (NATURE), decided at Q2**: the deciding part (the Gas Company, about 74% of five-year operating profit) holds an
exclusive franchise that no attacker could take today, but whether its regulated return survives ten to twenty years turns on
New York's future treatment of gas under the CLCPA, a forecast the filer says it cannot make and has begun to price as shorter
service lives. Integrity facts recorded, not judged. **No security of the company can be bought**: since July 6, 2022 it is
wholly owned by ACP Crotona Corp. (Argo Infrastructure Partners), with one holder of record, and it files nothing with the SEC.
Q7 not reached; the COMPUTATION below finds no case that earns the floor, and there is no price to set it against. Q11 belongs to
the holding review, not to this run.

**How the framework's text treats a business with no purchasable security** (the brief asks this to be stated): no instance
found in `Framework/THE FRAMEWORK v5.md` of a rule for it (a full read of the document for this run; the scope paragraph says
the framework "governs every purchase and every add", and no purchase can be made here). What the text does say bears on it in
three places. Q7 is a STOP that closes on the price (its heading asks whether the price is so far below value that it needs no pencil;
the floor is "about ten percent pre-tax on the price paid"), so without a price Q7 cannot close IN. Q8 closes on "a loss to the alternatives
on the day", and the bond can be bought on the day while this cannot. And the rows refuse the decision without a price: "we
don’t do anything when the phrase “regardless of price” enters into the sentence" **[M2008-041]**. Had the business cleared Q1
to Q6, the file could not have closed IN at Q7 for want of a price; it closed earlier, at Q2, on the business.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no verdict;
the box unchanged, operator rule 2.)*

**Q3, capital.** Capital spending exceeded operating cash in every year FY2017-21 (Step 0 table) and ran 2.1 to 2.7 times
depreciation and amortization; the spending is described as "NYPSC mandated system safety and reliability measures, including
replacement of older pipe and regulator stations" (10-K FY2021, Item 7, Case 20-G-0442), with $11.3M planned for fiscal 2022;
"We believe new debt and proceeds from equity will be required to satisfy our capital expenditures" (Item 7). Return on
year-end equity 4.3% to 9.8% over FY2013-21, mean 7.4% (competitor row, Q2).

**Q4, the accounts. Balance sheets FY2013-21 read first** (XBRL table in `run_py_output.txt`, checked against the filed FY2021
and March 2022 balance sheets): total assets rose from $55.0M to $144.1M, with a step from $71.4M to $107.0M in FY2016 when
Pike was bought; common equity rose from $23.4M to $35.5M, but retained earnings only from $2.1M to $7.1M, so most of the
equity growth was paid-in capital (shares outstanding 2.26M at September 2013 to 3.08M at September 2021, with a jump of about
0.52M in FY2017); long-term debt (non-current) rose from $13.5M to $46.1M; cash was never above $3.8M and was $0.33M at
September 2021; goodwill appears only in FY2020, $0.9M, from Leatherstocking. At March 31, 2022: long-term debt $49.6M with the
current part, demand notes $5.9M, lines of credit $9.2M, redeemable preferred A, C and D $16.0M classified as debt with their
dividends reported as interest, Series B convertible preferred $5.0M in temporary equity, pension and post-retirement liability
$7.8M against a $4.9M deferred pension regulatory asset (10-Q, 0001174947-22-000671). Other facts: Corning Gas "does not accrue
revenue for gas delivered but not yet billed" (Item 7); a $1.17M gain on PPP loan forgiveness in FY2021 income, with a $490,000
reserve against a NYPSC order to show cause why it should not be refunded (Item 7); EBITDA appears in the filer's mouth only in
the sale context (Argo's "fifteen times our management team’s projection of 2019 EBITDA" and the board's "implied multiple of
14.3 times EBITDA", DEFM14A) and in the M&T revolver's pricing grid ("funded debt to leveraged EBITDA ratio", 8-K 2021-12-22,
0001174947-21-001161). Stock issued for services ($96K to $239K a year) is a real cost the XBRL did not tag.

**Q5, the people (integrity facts recorded, not judged).** (1) Directors Joseph P. Mirabito and William Mirabito are officers,
directors and significant shareholders of Mirabito Holdings, sister company of MRI; the July 2020 purchase of MRI's 50% of the
Leatherstocking companies gave MRI an option to buy Corning's shares of Leatherstocking NY for $100,000 "beginning on the earlier
of a change in control of Corning or July 1, 2021"; MRI exercised it on October 5, 2021, and Corning sold its interest to MRI
for $100,000 on December 31, 2021, during the pending sale of Corning (8-K 2022-01-05, 0001174947-22-000024). Joseph Mirabito
chairs the nominating and compensation committee; the 10-K says "There are no interlocks" and in the same paragraph names his
company's joint venture with the Company (Item 11). (2) On January 14, 2022, with the merger pending, Corning extended two
officers' change-in-control agreements by three years and added one for the corporate secretary (8-K 2022-01-14,
0001174947-22-000044). (3) For the other side: executive pay was modest (CEO total $281,936 in FY2021, Item 11); director stock
compensation was stopped on January 12, 2021 because of the merger (Item 11); in the merger the board refused Argo's draft
voting agreement binding "several of our significant shareholders that were unaware of the transaction", ran a go-shop that
contacted 64 parties, and took the higher of two bidders' prices in rounds (DEFM14A, Background). Management changed after the
window: Michael German retired as CEO on June 1, 2025, succeeded by Tony Dorazio (company press release, web excerpt).

**Q6, the money and the owners.** Common dividends $0.61 a share in FY2021 and $0.603 in FY2020, paid while capital spending
was financed by new debt and preferred stock (Series C, $4.5M net, FY2020); shares issued every year for services and through
the DRIP (11,030 shares in FY2021, 25,487 in FY2020; Item 5); the DRIP was suspended when the merger was signed (Item 1). Q6's
buyback test does not arise: no repurchase program in the filings read. The sale itself: $24.75 a share in cash, a 50% premium
to the pre-announcement close (DEFM14A).

**Q9, debt and exposures.** Net debt at March 31, 2022, $78.1M including preferred A, C and D (below); the demand notes and
revolving lines, $15.1M, are payable on demand ("All amounts under the Note are due and payable upon demand by M&T", 8-K
2021-12-22); the holding company guarantees the Pike and Leatherstocking loans (Item 7); Item 1A: "If cash flows from operations
are not sufficient to fund these capital expenditures, we will need to rely on new debt or equity financing which may be
difficult to obtain." Operating hazards: "leaks, accidental explosions" (Item 1A); a ransom-seeking cyber-attack in FY2020 was
resolved without payment (Item 1A).

## COMPUTATION, NOT A CLEARANCE: the two reporting figures (a reporting convention, not a rule; no entry language)
Built by Q7's range convention in full, from `Test Runs/_research 2026-10-17 CNIG/calc.py` (output `calc_output.txt`).
USD millions unless per share.
- **The cash input.** Owner cash after every real cost, FY2017-21 (Step 0): -2.92, -2.17, -0.26, -5.22, -6.84; average -3.48 on
  the equity-only basis. **All-equity basis** (the central figure): add back interest after tax (interest expense, which
  includes the Series A and C, and later D, preferred dividends the filer reports as interest: 1.90, 2.10, 2.33, 2.57, 3.43;
  tax at 23%, a **CONVENTION of this run**, the filer's effective rate in FY2020 and FY2021, 23.1% and 23.3%, because the FY2018
  rate was distorted by the Tax Act remeasurement): -1.46, -0.56, +1.53, -3.25, -4.20; **average -1.59**. Company's own tax:
  operating cash is after taxes paid; no carryforward found.
- **(a) Cycles.** The series is not cyclical and no end year is aberrational on the filer's description in a way that changes
  the base: FY2021 carried $667,585 of merger costs and the 2021 rate order, but its capital spending ($11.0M) matches the plan
  for FY2022 ($11.3M). The literal window is the base.
- **(b) Decline and sign.** The all-equity series changes sign (FY2019 positive), so growth is measured between the halves:
  FY2017-18 average -1.01, FY2020-21 average -3.72, both negative, a meaningless rate. **The range is the no-growth case alone**,
  said so.
- **(c) Acquisitions.** Deducted (Leatherstocking $1.89M in FY2020; a $0.72M receipt on the Pike price in FY2017). The filer
  reports no organic growth figure; with purchases left out the equity-only average is -3.25. Not a serial acquirer (one
  purchase in the window; the test's ratio is meaningless when owner cash before purchases is negative). The 2022 merger is a
  sale of the company, not a deal by it; the December 2021 sale of the Leatherstocking NY stake for $100,000 is immaterial.
- **(d) Working capital** is inside operating cash.
- **(e) Maintenance.** The filing gives no maintenance figure and describes the replacement program as mandated "replacement of
  older pipe" to keep the system safe, which is spending to stay in place; the growth spending (new customers, Leatherstocking
  expansion) is not separated. The filing does not allow a maintenance guess below total spending, so the all-spending case is
  central and the depreciation variant is shown beside it.
- **(f) The cap.** No growth is carried; nothing to cap.
- **Net debt** at the latest filed balance sheet, March 31, 2022 (10-Q, 0001174947-22-000671): borrowings $64.67M (long-term
  $42.80M, current $6.78M, demand notes $5.90M, lines of credit $9.19M) plus preferred A $6.50M, C $4.50M and D $5.00M (the filer
  classifies all three as debt) = $80.66M, less cash $0.33M and marketable securities $2.18M = **$78.15M**; the Series B
  convertible preferred ($4.99M, temporary equity; paid $29.70 a share in the merger) is deducted as a senior claim. Operating
  leases left out. The lines of credit buy gas and electricity; they are not stated to be inventory-secured, so they stay in net
  debt (leaving them out would add $2.98 a share). Subsequent event the 10-Q itself states: the pending merger. Common shares
  3,083,577.
- **The floor, tested first** (2026-10-10 convention). On the all-spending basis no case earns the floor at any positive
  price: owner cash is negative on both bases. On the depreciation variant, all-equity, the whole business at ten percent is
  $32.1M against $83.1M of net debt and Series B. "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **(a) VALUE RANGE: -$36.44 a share, the no-growth case alone, all-equity basis** (whole business -$29.2M at 5.43%, less net
  debt and Series B). Beside it: equity-only -$22.42; depreciation variant, all-equity -$7.80 and equity-only +$6.21.
- **(b) FAIR PRICE: -$32.11 a share on the all-equity basis** (the single case valued at ten percent: whole business -$15.9M,
  less net debt and Series B); **equity-only -$12.92**. Depreciation variant beside: all-equity -$16.56, equity-only +$2.63. The
  tax treatment is the company's own tax, as above.
- **Against the price: no price exists.** No security of the company trades or can be bought (Step 0). The 2022 merger price
  of $24.75 is shown only as history.
- **What the arithmetic leaves out, said plainly:** a regulated distributor's growth spending is financed with new capital and
  earns the allowed return on the rate base it adds; the owner-cash construction charges all of it and, because the series is
  negative, credits no growth. The buyer that paid $24.75 in 2022 was valuing rate-base growth at an allowed return, a figure
  this construction has no place for (see the last section).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). (The first
      template-copy commit preceded every fetch; Step 0, Q1 and Q2 were committed as each closed.)
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session; the run is folded into the register before the dispatcher moves on (operator rule ten). A run not in the
      register binds nothing. (The lock and the fold are the dispatcher's; not checked from here.)
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); anything of
      them seen by accident is declared under contamination, not used. (One filtered name listing of `Test Runs/` before the
      copy, which returned nothing, and the commit subjects of the opening `git log`, both declared at the top.)
- [x] Every v5 id resolves (grep it in `principle_ledger_v5.csv`); every filing fact has its accession; no number
      without a row or a filing. (Check script `Test Runs/_research 2026-10-17 CNIG/check_run.py`.)
- [x] The order was kept; the first STOP that failed closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; aggregator quotes flagged. (No quote exists; the tool's price feed returned 404 and the placeholder is
      labelled.)
- [x] Contrary evidence was written down as it was found **[M1997-127]**; if a STOP closed the file, the facts found for
      later questions are under AFTER THE STOP, with the integrity flag in the box line where they bear on Q5.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII). (Not a point-in-time run; the anchor is today.)
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII). (Its share basis is stale and its stock-pay line was
      wrong; both corrected from the filed statements in Step 0.)
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **No rule for a name that cannot be bought.** The scope is "every purchase and every add", Step 0 asks for a price, Q7 and
Q8 close on one, and the reporting convention reports two figures "against the price"; nothing says what a run does when the
company was taken private and no security exists. I ran the questions in order, decided the box on the business at Q2, and
stated the absence in the box section; had Q1 to Q6 passed, Q7 could neither close IN nor fit any of its three named closes,
and a run would have had to invent one. A one-line rule at Step 0 (no purchasable security: the run is written as a business
record and the box line says so) would settle it. (2) **Stale filings.** The only annual reports end in fiscal 2021, five years
before the run date. Q4 asks whether the condition "can be known" from the figures, and Q7 takes "the last five years", but no
text says what to do when the last filed five years end years ago; I used them, said so, and drew one later fact (the 2024 rate
case release) from the company's own website, a source the brief admits for tradability and the framework does not mention.
(3) **Q2's regulated-return exception has no test for the regulator itself as the threat.** The text sends a regulated return
"to Q3 as a second best", while the rows on utilities say the regulatory climate can make earnings and asset values hard to
project **[L2023-011]**. I put that threat under test 11 and closed TOO HARD (NATURE); another analyst could read the exception
as passing Q2 and carry the name to Q7. (4) **The owner-cash range misreads a regulated grower.** A utility's mandated
replacement is both maintenance and rate-base growth that earns an allowed return; specific (e) wants a maintenance guess the
filing cannot give, and when the series is negative (b) leaves only the no-growth case, so the construction values a rate base
that earns about 9% at less than nothing. I applied the text as written and recorded the gap beside the figures rather than
invent a rate-base method. (5) **Net debt and preferred stock.** The all-equity basis names "borrowings and finance leases"; it
does not say whether redeemable preferred that the filer classifies as debt is net debt, or how a convertible preferred in
temporary equity is treated. I counted the former in net debt and deducted the latter as a senior claim, and said so.
