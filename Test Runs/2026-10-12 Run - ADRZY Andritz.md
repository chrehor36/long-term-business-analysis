# Company Run: ANDRITZ AG (Vienna: ANDR; US OTC ADR: ADRZY), 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its source document; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
995b258e).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-12, after the run was committed: not held (`PORTFOLIO.md` does not name Andritz, ADRZY or ANDR).*

**Dispatched run.** Written by a dispatched analyst under the brief of 2026-10-12 (two stated departures: the name files no
SEC documents, so the company's own annual financial reports replace accessions; the lines of evidence are derived here, not
listed in the brief). Working folder: `Test Runs/_research 2026-10-12 ADRZY/` (notes, `computations.py` and its output,
`extract_statements.txt` of the filed statements, `check_citations.py`); downloaded reports kept in its ignored `cache/`.

**Contamination declared.** Before the run I saw, without opening anything: the repository's recent commit subjects (the last
five, about another company's run and fold, nothing about this name) and the memory index line saying the queue holds
gate-clearers and that "nothing buyable" stood at some earlier date. Neither names this company. Not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** EUR 81.40 per ordinary share (ANDR.VI, Vienna, close 2026-10-09, the last close before this run; Yahoo Finance via
  `tools/sources.py price()`; **aggregator, live quote only, flagged**, operator rule 5). The US OTC ADR ADRZY closed USD 19.70
  the same day (same source). **ADR ratio:** not stated in any document I could reach. Andritz's own share page names no ADR
  programme, and the depositary directory page I tried returned an error. So no per-ADR figure is given; any per-ADR
  conversion is the euro figure times the ratio in the depositary's own terms.
- **Shares:** share capital 104,000,000 no-par bearer shares, one class (Andritz share page; FR2025 note 34). Outstanding at
  2025-12-31 **97,998,794**, treasury **6,001,206** (FR2025 note 34 c, the table "changes in the number of shares
  outstanding": 104,000,000 issued less 6,001,206 treasury). After the balance-sheet date, the H1 2026 report (note 12 b)
  records no buyback and 61,495 + 208,495 shares resold to executives under the option programme, plus 42,062 shares
  transferred to employees: **98,310,846 outstanding at 2026-06-30** (5,689,154 treasury). That is the count used.
  `python Screens/cover_shares.py ADRZY` returned "NOT AN SEC REGISTRANT in the live ticker file", so the count is taken from
  the reports, as the brief directs.
- **Market value:** 98,310,846 × EUR 81.40 = **EUR 8,002.5M**.
- **Sovereign for the earnings currency (EUR):** **3.78%**, ECB euro-area AAA yield curve, 30-year spot
  (YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), observation 2026-10-08, from the issuing authority (`python tools/sources.py`, run
  2026-10-12).
- **Documents read** (operator rule 4; no SEC filings, so title, date and URL replace an accession; all at
  https://www.andritz.com/group-en/investors/investors-downloads/financial-reports):
  - **ANDRITZ Financial Report 2025** (management report, audited consolidated statements, notes; Executive Board statement
    dated Graz, February 24, 2026): `/resource/blob/689114/6715754fcdb5a08fb20331cc2fa78ee2/andritz-financial-report-2025-data.pdf`
  - **ANDRITZ Annual Report 2025** (business-area descriptions, strategy): `/resource/blob/689306/6ad9400073c46323b95b1be977870245/andritz-annual-report-2025-data.pdf`
  - **ANDRITZ Interim Financial Report H1 2026** (unaudited; dated Graz, July 30, 2026): `/resource/blob/727606/b4d5b8227c18699fc74b06865da244ec/andritz-financial-report-h1-2026-en-data.pdf`
  - **Financial Reports 2015 to 2024**, one per year, for the statements, the business-area tables and the management reports
    (2024 dated Graz, February 28, 2025): FR2024 `/resource/blob/620908/...-2024-e-data.pdf`, FR2023 `/resource/blob/542952/...`,
    FR2022 `/resource/blob/492056/...`, FR2021 `/resource/blob/450322/...`, FR2020 `/resource/blob/405552/...`, FR2019
    `/resource/blob/340622/...`, FR2018 `/resource/blob/290372/...`, FR2017 `/resource/blob/257688/...`, FR2016
    `/resource/blob/49164/...`, FR2015 `/resource/blob/26658/...`; and FR2013 `/resource/blob/26556/...` for the 2013 loss year.
    The full URLs are in `cache/fr.html`, and the text of every statement used is in `extract_statements.txt`.
  - Andritz share page, https://www.andritz.com/group-en/investors/share (shareholder structure).
  - There is no proxy. The pay and governance facts come from FR2025 notes 7 (related parties) and the corporate governance
    chapter.
- **One figure cross-checked against the filed statement:** cash flow from operating activities 2025, **EUR 652.7M**, is the
  same in the consolidated statement of cash flows (FR2025 p. 46) and the key-figures table (FR2025 p. 02). Net liquidity
  at 2026-06-30 of **EUR 593.3M** in the H1 2026 key figures recomputes from its balance sheet: liquid funds 963.6 (cash
  769.4 plus investments and time deposits) less bank loans and Schuldscheindarlehen 179.9 non-current and 190.4 current.
- `python tools/run.py ADRZY` returned "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE" and printed no arithmetic. **Every
  line below is my own arithmetic from the filed statements, shown in `computations.py`.** Currency is EUR millions (MEUR)
  unless stated. The 2015 to 2020 reports file in TEUR and are rounded here to MEUR.

**Owner cash, as filed, by year** (MEUR; the consolidated statement of cash flows of each year's own report):

| Year | CFO | Capex paid (PP&E + intangibles) | Lease principal (IFRS 16, from 2019) | Acquisitions, net¹ | Owner cash, acquisitions deducted | Owner cash before acquisitions | Revenue |
|---|---|---|---|---|---|---|---|
| 2016 | 366.6 | 122.1 | n/a (rent inside CFO) | 106.5 | 138.0 | 244.5 | 6,039.0 |
| 2017 | 246.5 | 115.5 | n/a | -9.8 | 140.8 | 131.0 | 5,889.1 |
| 2018 | 7.8 | 127.1 | n/a | 251.4 | -370.7 | -119.3 | 6,031.5 |
| 2019 | 821.6 | 122.0 | 46.5² | 91.8 | 561.3 | 653.1 | 6,673.9 |
| 2020 | 461.5 | 87.9 | 48.9² | 25.5 | 299.2 | 324.7 | 6,699.6 |
| 2021 | 529.6 | 110.3 | 48.5 | 76.2 | 294.6 | 370.8 | 6,463.0 |
| 2022 | 710.8 | 155.0 | 59.3 | 62.1 | 434.4 | 496.5 | 7,542.9 |
| 2023 | 375.0 | 170.8 | 50.6 | 36.4 | 117.2 | 153.6 | 8,660.0 |
| 2024 | 636.5 | 179.5 | 53.3 | 51.8 | 351.9 | 403.7 | 8,313.7 |
| 2025 | 652.7 | 198.1 | 52.0 | 333.2 | 69.4 | 402.6 | 7,883.1 |

¹ Net cash flow from company acquisitions, plus purchases of non-controlling interests and payments to former shareholders
(contingent consideration), plus payments for equity-method investments, less the net cash from subsidiaries sold. ² In 2019 and
2020 the cash flow statement shows lease repayments together with loan repayments. The lease figure is the lease note's
"total cash outflow for leases" less the lease interest: 2020 53,998 TEUR less 5.1 MEUR; 2019 51,524 TEUR less about 5.0 MEUR,
**an estimate**, because the 2019 lease-interest line was not found. Proceeds from disposals of property (137.9 over 2021 to
2025) are **not** credited in the central figure. The variant that credits them is in `computations_output.txt`.

Operating cash **includes interest received and paid and tax paid**, so the figures above are on the equity basis. The
all-equity version takes out the net non-lease interest after the filer's stated 23.7% group tax rate (FR2025 management
report 4 c). Leases are treated as an operating cost: lease principal is deducted, and lease liabilities (249.9 at
2026-06-30) are left out of net debt, as Q7's basis rule allows for operating leases. **Stock pay** is expensed in EBIT
under IFRS 2, and the shares for the option and PSU plans come from treasury stock bought for cash, so the buybacks that
fund them sit in financing. Executive Board share-based expense was -0.1 MEUR in 2025 and 0.9 MEUR in 2024 (FR2025 note 7).
The company-wide plan cost was not separately extracted. It is small against owner cash, and I flag it here rather than
add it back.

**Net debt (all-equity basis):** net liquidity of **EUR 593.3M of net cash** at 2026-06-30 (H1 2026 key figures; liquid funds
less bank loans and Schuldscheindarlehen). No later event in that report changes it. Pension provisions (348.3 at
2026-06-30) are left out, as the basis rule names borrowings and finance leases only, and I say so. **Enterprise value at
the price: 8,002.5 − 593.3 = EUR 7,409.2M.**

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own Andritz "if the market closed for five years"
**[M1997-109]**, on the cash the business itself produces. The market serves and does not instruct **[M2006-077]**: the
EUR 81.40 quote tells me the price and nothing about the worth. Margin of safety is the attitude that "if you have to
actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. No macro forecast enters
**[M2000-094]**, and that matters here, because this is a capital-goods supplier whose order intake follows its customers'
investment cycles (pulp prices, steel and car output, utilities). Those cycles are recorded as the business's own
volatility, never forecast. The analyst's habits: hunt "what’s wrong" and "what you’re missing" **[M2025-013]**, and write
contrary evidence down at once **[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Owner cash swings violently with project working capital: operating cash was 7.8 in 2018 and 821.6 in 2019. On revenue
   of 6 to 8.7 billion, owner cash has run between -370.7 and +561.3 a year (table above).
2. The customer-advance float has shrunk. Net working capital (Andritz's definition) was -639.2 in 2011 and -570.9 in 2014
   (FR2015 key figures), and +118.0 at 2025 year end (FR2025 key figures). The net cash is partly customers' prepayments,
   and it unwinds when orders fall.
3. Fixed-price projects have produced large losses. In 2013 Pulp & Paper made an EBITA of **-35.7** on sales of 2,005.3,
   from "high provisions and expenses for cost overruns in connection with supplies to a pulp mill in South America"
   (FR2013 management report). The risk report says liabilities "can vastly exceed the value of the contract in question"
   (FR2025 D 2 d).
4. Restructuring recurs, and the company features an adjusted figure ("comparable EBITA") beside EBITA every year: capacity
   measures of 78 (2015, Schuler), 113 (2019) and about 79 (2020 gap), then 15, 30 and 50 in 2023 to 2025 (key-figure gaps).
5. "The product liability area includes some recent cases involving alleged physical injuries and/or deaths due to asbestos
   exposure." (FR2025 D 2 f).
6. The risk report on the competitive position: "highly competitive markets in which only a few large suppliers bid for only
   a few large orders. In addition, there are many small companies competing locally that have a comparatively low-cost
   base" (FR2025 D 1 c). Customer consolidation in pulp, paper and steel may leave "fewer customers, but with customers who
   have greater purchasing power" (D 1 d).
7. Metals (Schuler, bought 2013) has needed capacity cuts in 2015, 2019, 2020 and 2025, and earned an EBITA margin of -4.5% in
   2019 (FR2019).

## THE STANDING RULE
Owning a part-interest in Andritz, bought for cash and held without borrowing, puts the buyer at no risk of ruin. The
rule binds the buyer's conduct: "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own exposures
are Q9's question. The buyer's conduct passes, provided no margin or leverage is used.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence chosen** (the brief's second departure). From the Annual Report 2025's business-area descriptions,
the Financial Report 2025's management report (B market development, C business development, D risk management, J outlook)
and the same sections in the 2013 to 2024 reports, I chose: **(1)** the deciding part by profit, since Andritz reports four
business areas with different economics; **(2)** that part's revenue mix of service against capital equipment, and its
margin across the 2011 to 2025 span; **(3)** order intake and backlog as the variable that drives revenue; **(4)**
fixed-price project risk (risk report D 2 c and d), because it produced the 2013 loss; **(5)** working capital and customer
advances, because they swing owner cash; **(6)** acquisitions, because "complementary acquisitions" are named as a main
strategic goal (D 1 f). I chose them because the risk report names (3), (4), (6) and competition as its own principal
risks, and because (1), (2) and (5) are what the statements show moving most.

**The parts** (Q1's holding-company paragraph reaches operating segments: a part matters when it decides under Q2's
threshold). Five-year EBITA 2021 to 2025, from the FR2025 business-area key figures, restated to the present structure:

| Business area | EBITA 2021-2025 (MEUR) | Share | Decides? |
|---|---|---|---|
| Pulp & Paper | 335.4 + 374.1 + 412.5 + 373.7 + 304.6 = **1,800.3** | **54.6%** | **yes (more than half)** |
| Environment & Energy | 109.5 + 139.5 + 149.9 + 170.0 + 155.1 = 724.0 | 22.0% | no |
| Hydropower | 63.2 + 72.3 + 88.1 + 96.3 + 113.1 = 433.0 | 13.1% | no |
| Metals | 38.4 + 62.6 + 91.4 + 73.0 + 75.4 = 340.8 | 10.3% | no |
| Group | 3,298.1 (equal to the group EBITA sum 546.5 + 648.5 + 741.9 + 713.0 + 648.2) | 100% | |

**The test applied to Pulp & Paper.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**. The product can stay opaque: what matters is to "understand the
economic dynamics of the industry" **[M2011-014]**.
- **What it sells.** Complete pulp mills and their key islands (fiberline, chemical recovery, drying, power boilers), paper,
  tissue, board and nonwoven machines, and the service on the installed base. The Annual Report 2025 calls Andritz "the
  global market leader in the pulp industry" (the company's own claim). Service was **59%** of the area's 2025 revenue
  (51% in 2024; FR2025 C 2).
- **The key variables, and how predictable they are** **[M1998-044]**. (a) Service on the installed base: this follows the
  number of mills running, and pulp mills run for decades, so it is the predictable half. (b) Capital orders: lumpy,
  driven by the timing of greenfield pulp lines (South America, China) and rebuilds. The timing is not predictable, but the
  backlog (2,833.0 at end-2025) smooths revenue by one to two years. (c) Margins on fixed-price contracts: predictable as a
  range, not a point (2013 shows the tail).
- **Do the past statements tell the future ones** **[M2008-033]**? The area's EBITA margin was 6.4, 5.9, -1.8, 5.2, 8.7, 8.7,
  9.5, 9.9, 9.4, 9.7, 11.4, 10.9, 10.3, 10.8 and 10.3% over 2011 to 2025 (FR2015, FR2017, FR2020 and FR2025 tables; the area's
  scope was widened in 2018/2019 and restated in 2023, which I flag). Since 2015 the margin has stayed inside 8.7 to 11.4%
  through the 2019 to 2020 pulp-price trough, and through a fall in the area's revenue from 3,987.4 (2023) to 2,956.9 (2025).
  The statements do describe the next ones, as a range.
- **Would the insiders write it down** **[M2000-105]**? Yes. The nearest rival writes it down in its own annual statement:
  Valmet's Biomaterial Solutions and Services segment states "a target EBITA margin of 14% by 2030" (Valmet Financial
  Statements 2025, segment section). Insiders who put a ten-year margin on paper are not saying "That’s too hard"
  **[M2000-105]**.
- **Change.** The product changes slowly: kraft pulping, recovery boilers and paper machines are decades-old process
  technology, improved by increments (the R&D sections of FR2017 and FR2020 describe chip handling, emissions and
  by-products). The forecast is about customers' capacity decisions, not about a technology race. Graphic paper is in
  structural decline (FR2025 B 1: "the paper segment continued to face a challenging market environment"), and packaging,
  tissue and pulp are the growth. That is a mix shift I can see, not an unforeseeable one.
- **Doubt** **[M2002-092]**. My doubt is about **timing and the project tail** (contrary evidence 1 and 3), not about where the
  area's economics will be in ten years. A fixed-price loss like 2013's is a risk to the year, and Q9 and Q4 weigh it. The
  parts that do not decide are understood as businesses too. Metals sells presses and strip lines into car and steel capex
  cycles at thin margins, Hydropower sells turbines and generators to utilities, and E&E sells separation, pumps, clean air
  and feed lines. None of them is a fast-changing technology business.

**VERDICT: IN.** The deciding part's ten-year economics can be foreseen as a range: a slow-changing process-equipment
business, about half of it service on a long-lived installed base, whose margin held inside a narrow band for eleven years
**[M2012-065]**, **[M2011-014]**, **[M1998-044]**. The insiders write the forecast down **[M2000-105]**. It is IN, not TOO
HARD, because the doubt I hold is about the size and timing of individual years, which Q4, Q7 and Q9 carry, and not about
the business's place in ten years.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**. Andritz reports parts with different economics, so each part's castle is read
separately, since "lumping them together [...] impedes analysis" **[L2008-005]**. The file closes on the deciding part, Pulp &
Paper (54.6% of five-year EBITA, table at Q1). The parts that do not decide are read briefly at the end.

**The castle tests, Pulp & Paper, each with its filing fact.**
1. **What keeps it standing; how permanent; does it depend on the lord** **[M1995-038]**. Three things keep it standing.
   (a) The installed base: mills built by Andritz buy spare parts, rebuilds and service from the maker for decades. Service
   was 59% of 2025 area revenue (FR2025 C 2). (b) Process references for complete pulp mills, which the company claims to
   lead (AR2025, "the global market leader in the pulp industry"; a claim, not an independent figure). (c) In-house
   manufacture of key components (FR2025 D 2 b: "Process-relevant key components [...] are mainly manufactured and assembled
   in the Group's own workshops"). None of the three depends on one person. Leitner left the chief executive's chair in 2022
   (now Supervisory Board chairman), and the area's margin held after it (10.9, 10.3, 10.8, 10.3% in 2022 to 2025).
2. **The money test: could a well-funded attacker take it** **[M2011-015]**? Over the span read (2011 to 2025), neither
   Andritz's reports nor Valmet's statements describe a new entrant taking the complete-pulp-mill business. The risk report
   describes the field as "only a few large suppliers" bidding for "only a few large orders", with "many small companies
   competing locally" at "a comparatively low-cost base" (FR2025 D 1 c). Local low-cost rivals and Chinese equipment makers
   exist, but **their primary figures were not obtained** (flagged under What I could not get). A new entrant with money
   faces the installed base and the references, which money does not buy quickly. **Weighs for, with the flag.**
3. **Pricing power, the agony before a rise** **[M2005-020]**. The capital orders are bid, and the risk report says the
   competitive situation "can have a negative effect on order intake and on sales margins" (D 1 c). That counts against. The
   price behaviour across the cycle is the better evidence **[M2005-020]**: when the area's revenue fell from 3,987.4 (2023)
   to 3,461.1 (2024) and 2,956.9 (2025), its EBITA margin stayed at 10.3, 10.8 and 10.3%. Raw-material inflation in 2022 to
   2023 was "largely" compensated "through various operative measures" (D 2 c, of 2024). **Mixed: no pricing power on the
   capital bid, held margins through a volume fall.**
4. **Would the customer still choose it over the low bid** **[M2017-009]**? For a multi-hundred-million-euro pulp line carrying
   guaranteed performance values and penalties (D 2 c), the buyer is in the position of "buying a parachute", where you would
   not "necessarily take the low bid" **[M2001-014]**. The buyer of spare parts for an Andritz digester or recovery boiler buys
   them from the maker. Against: the capital tenders are competitive, and consolidating customers have "greater purchasing
   power" (D 1 d). **Weighs for on service, mixed on capital.**
5. **The low-cost position** **[L2004-007]**. No filing fact shows Andritz is the low-cost producer, and the risk report says
   local rivals have the lower cost base. Not claimed.
6. **Ask the competitors** **[M1999-130]**. Not possible from the record. The rival's own statements are used instead (the
   competitor row below).
7. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. The service share rose (51% to 59% of area revenue, 2024 to 2025,
   partly because capital revenue fell). Andritz bought A.Celli (tissue and paper machines), Diamond (boiler cleaning) and
   most of Allen-Sherman-Hoff (ash handling) in 2025, all described as high-service businesses (FR2025 C 8). The margin band
   moved up from about 6% (2011 to 2014) to about 10% (2017 to 2025). **Widening on the evidence of the span.**
8. **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**. (i) The structural decline of graphic
   paper, already under way (FR2025 B 1), offset so far by pulp, tissue and packaging. (ii) Customer consolidation (D 1 d).
   (iii) Chinese integration, "with leading players investing in fully integrated production capacities" (FR2025 B 1); whether
   Chinese mills buy their lines from Andritz or from local makers is not shown in the reports. (iv) A run of fixed-price
   losses like 2013's. Slow change "can lull you to sleep easier" **[M2014-038]**, so (i) and (iii) are written down here as
   the threats to watch. None is a filing fact showing the castle filling in.

**The competitor row** (the rivals the reports name: **none**. A search of FR2013 to FR2025, the AR2025 and the H1 2026 report
for "Valmet", "Voith" and "competitor" found no rival named. Chosen from the business-area descriptions, as the brief allows,
and said so: **Valmet Oyj**, which supplies pulp, paper, tissue, board and energy lines and their services. It is the plain
rival to the deciding part, and it publishes its own annual financial statements. Source: Valmet Financial Statements 2016,
2020 and 2025, https://www.valmet.com/investors/reports-and-presentations/ (financial indicators tables).)

| Year | Andritz P&P EBITA margin | Valmet group comparable EBITA margin | Valmet ROCE before taxes |
|---|---|---|---|
| 2014 | 5.2% | 4.3% | 9% |
| 2015 | 8.7% | 6.2% | 12% |
| 2016 | 8.7% | 6.7% | 12% |
| 2017 | 9.5% | 7.1% | 14% |
| 2018 | 9.9% | 7.7% | 19% |
| 2019 | 9.4% | 8.9% | 23% |
| 2020 | 9.7% | 9.8% | 22% |
| 2021 | 11.4% | 10.9% | 23.7% |
| 2022 | 10.9% | 10.5% | 17.6% |
| 2023 | 10.3% | 11.2% | 14.2% |
| 2024 | 10.8% | 11.4% | 11.4% |
| 2025 | 10.3% | 11.9% (its pulp/paper/tissue segment, Biomaterial Solutions and Services: 10.3%) | 10.9% |

Flags: Valmet took in Neles (flow control) in 2022, so its group figures after 2022 mix in a different business. Its 2025
segment figure is the like-for-like one, and it equals Andritz P&P's 10.3%. Andritz's area scope changed in 2018/2019 and
was restated in 2023. Named rivals I did not get primary figures for: **Voith** (paper and hydro; privately held, publishes a
group report, not fetched in this run), **SMS group** (metals; private), **GE Vernova** (hydro; an SEC filer, but hydro is
too small a part of it to compare), and the Chinese makers (no primary figures obtained).

**The parts table.**

| Part | Share of five-year EBITA | Castle | Decides |
|---|---|---|---|
| Pulp & Paper | 54.6% | standing (tests above) | **yes** |
| Environment & Energy | 22.0% | not decided; margins 10.3 to 11.8% (2021-2025, FR2025) with separation, pumps, clean air, feed and biofuel | no |
| Hydropower | 13.1% | not decided; 5.6 to 6.5% margins, legacy loss projects "phased out" (FR2025 C 4), backlog 4,535.2 to 6,122.5 (H1 2026) | no |
| Metals | 10.3% | **open on the evidence**: EBITA margins 2.0 to 6.0% (2021-2025), -4.5% (2019), "unchanged fierce competition" (FR2019 B), capacity cuts in 2015, 2019, 2020 and 2025 | no; carried to Q7 as an ordinary business at no growth |

**The field's returns over the last full cycle**, from both firms' filings, judged in words (section C, no figure). The two
durable players in the deciding field earned, over 2014 to 2025, margins that rose from about 5% to about 10 to 11% of
sales. Valmet's pre-tax return on capital employed ran from 9% to 24%. Andritz's return on equity ran from 10.1% (2019, the restructuring year) to
23.4% (2023) (FR2020 and FR2025 key figures), and its return on capital employed before goodwill was far higher, since customer advances fund its working
capital (Q3). The field is two leaders that do not "beat each other’s brains out" **[M2013-052]**: their returns are above
ordinary on both firms' own figures. **The change for the better** (about 6% margins before 2015, about 10% after) is
credited only on a full cycle in which the price behaviour held **[M2005-020]**, **[L1995-022]**. The area's revenue fell
13.2% in 2024 and 14.6% in 2025, and Valmet's segment sales fell 5% in 2025, while both held margins at about 10%. That is a
volume fall with the price behaviour held, so the change is credited **[M2017-026]**.

**Why not TOO HARD, why not OUT.** OUT needs a castle shown to be filling in **[M2011-015]**, and no filing fact shows it.
TOO HARD needs a castle whose future "we don’t know how to valuate" **[M2000-019]**, and the eleven-year margin band and the
rival's parallel record give a judgeable future. The strongest case against is the capital bid business, where a few
suppliers bid for a few orders and "one competitor is frequently enough to ruin a business" **[M2012-108]**. The rival has
been there all along, and the returns held anyway.

**VERDICT: IN** on the deciding part, Pulp & Paper. The castle is the installed base and the service on it, plus process
references in complete pulp mills. Its margin held through a volume fall, and the one rival's record moved the same way
**[M1995-038]**, **[M2005-020]**, **[L1995-022]**. Metals is a marginal part **[L2021-001]**, carried to Q7 at no growth.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**1. What it earns on the capital it needs.** The capital is "the capital actually needed in the business" **[M2010-090]**,
measured on tangible assets, with goodwill left out of the business test and kept in the allocation test **[M2011-060]**.
Andritz's own "capital employed" excludes goodwill: net working capital plus property, plant and equipment plus intangible
assets other than goodwill. For 2025 that is 118.0 + 1,351.2 + 246.0 = 1,715.2, which matches its key figures (FR2025 p. 02).
Earnings after depreciation (EBITA) against the average capital employed of each year:

| Year | EBITA | Capital employed, year end (FR key figures) | EBITA / average capital employed (pre-tax) |
|---|---|---|---|
| 2021 | 546.5 | 1,211.5 (2020: 1,345.1) | 42.8% |
| 2022 | 648.5 | 1,049.5 | 57.4% |
| 2023 | 741.9 | 1,433.8 | 59.7% |
| 2024 | 713.0 | 1,462.2 | 49.2% |
| 2025 | 648.2 | 1,715.2 | 40.8% |

The reason is that customers prepay. Contract liabilities (advances and billings in excess) were 1,825.9 at end-2025 against
receivables plus contract assets of 2,378.7 and inventories of 1,207.6 (FR2025 balance sheet). A high reported return is
checked for "a cyclical peak in earnings, a monopolistic position, or leverage" **[L1994-009]**. The return is not
leverage: the group holds net cash (Step 0). It is not one peak year: the ratio was above 40% in each of the five years. The
return is a property of the advance-funded project model.

**2. To stand still, and to grow.** Capital spending paid was 813.7 over 2021 to 2025, about 1.7 to 2.5% of revenue, against
depreciation and amortization of 1,183.1 charged in the same years. That charge includes right-of-use depreciation and the
amortization of acquired intangibles, and the split is not filed for every year, so no maintenance guess is made (Q7 deducts
all spending). The profit does end the year as cash over a span, not "sitting in the yard" **[M2008-036]**: owner cash
before acquisitions of 1,827.2 over 2021 to 2025 against net income of 2,182.2, 84%. Single years are not reliable. 2018
gave 7.8 of operating cash on 219.7 of net income, and 2023 gave 375.0 on 504.3. The cash shows up across a cycle, not in
every year **[M2003-122]**.

**3. What the added capital earns.** Over 2015 to 2025, capital employed rose from 736.7 to 1,715.2 and goodwill from 528.5 to
1,130.3, so total capital including goodwill rose by about 1,580. EBITA rose from 429.0 to 648.2, by 219.2 (FR2019 and FR2025
key figures). The added capital, goodwill included, earned about 14% pre-tax at the margin. The growth was mostly bought:
Schuler (2013), Xerium (2018, consideration 200.3 MEUR plus the refinanced debt) and the six deals of 2025 (333.2 of cash).
This is the second-best business, which "takes more money" but reinvests at "a very satisfactory rate" **[M1998-081]**, or
a decent return on the added sums **[L2009-012]**. It is not the best business, which grows on "very little" **[M1998-081]**.
Whether bought growth is good "depends on what we earn on that incremental" money **[M2001-019]**. On these figures it earns
an adequate return, not a high one, and Metals (Schuler) earned 2 to 6% margins with a 2019 goodwill impairment (29.1 MEUR,
"the business did not develop as expected", FR2019).

**WEIGHS FOR.** The capital the business needs earns very high pre-tax returns, because customers fund the working capital
**[M2010-090]**, **[M2011-060]**. The capital added by acquisition earns adequate, not high, returns **[M2001-019]**. The
"little or no debt" criterion is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, eleven of them, before the income account** **[M2025-032]**. Each year-end from that year's own
Financial Report (MEUR; `balance_sheets.py`). Borrowings are bonds, bank loans and Schuldscheindarlehen, without leases. Cash
is cash plus current investments or current financial assets as filed. From 2018 the IFRS 15 headings (contract assets and
liabilities) replace "cost and earnings of projects in excess of billings" and "billings in excess", which I flag for
comparability.

| Year | Equity | Goodwill + other intangibles | Cash + current investments | Borrowings | Inventories / revenue | Receivables + contract assets / revenue | Advances and contract liabilities / revenue | Total assets |
|---|---|---|---|---|---|---|---|---|
| 2015 | 1,215.6 | 731.9 | 1,359.3 | 467.4 | 10.4% | 22.7% | 20.6% | 5,778.0 |
| 2016 | 1,344.2 | 764.7 | 1,407.1 | 556.6 | 12.2% | 25.9% | 22.8% | 6,198.6 |
| 2017 | 1,325.4 | 708.3 | 1,637.3 | 855.6 | 12.9% | 25.3% | 22.6% | 6,265.3 |
| 2018 | 1,330.8 | 1,157.5 | 1,184.8 | 1,382.6 | 14.4% | 29.2% | 21.2% | 6,918.6 |
| 2019 | 1,219.6 | 1,086.1 | 1,504.8 | 1,359.4 | 12.6% | 25.0% | 21.9% | 7,234.1 |
| 2020 | 1,255.7 | 983.8 | 1,644.3 | 1,300.3 | 11.4% | 24.1% | 17.2% | 7,056.7 |
| 2021 | 1,567.3 | 969.2 | 1,757.7 | 1,136.7 | 14.0% | 29.0% | 22.6% | 7,672.8 |
| 2022 | 1,834.7 | 947.1 | 2,030.9 | 1,080.9 | 15.1% | 28.0% | 25.8% | 8,491.8 |
| 2023 | 2,157.5 | 969.1 | 1,772.2 | 933.1 | 13.5% | 26.7% | 20.5% | 8,497.3 |
| 2024 | 2,280.0 | 1,000.3 | 1,551.4 | 529.5 | 14.0% | 27.3% | 20.0% | 8,163.0 |
| 2025 | 2,455.8 | 1,376.3 | 1,381.4 | 547.6 | 15.3% | 30.2% | 23.2% | 8,610.1 |

**What moved, and why** ("what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**).
- **Equity doubled** (1,215.6 to 2,455.8) through retained earnings after dividends of 1,628.6 and buybacks of 260.9 paid in
  2016 to 2025 (cash flow statements). It dipped in 2019 (1,219.6), the restructuring and impairment year.
- **Goodwill and intangibles** jumped with Xerium in 2018 (708.3 to 1,157.5), were amortized down to 947.1 by 2022, and jumped
  again with the 2025 deals (1,000.3 to 1,376.3). Goodwill was impaired once in the span (29.1 in 2019, Metals; 15.9 in 2018).
- **Debt** rose to fund Xerium (Schuldscheindarlehen of 400 in 2017 and 500 in 2018; borrowings peaked at 1,382.6) and was
  repaid to 547.6 by 2025. Cash and current investments ran from 1.18 to 2.03 billion. The group held net cash at every
  year-end (FR key figures, "net liquidity").
- **Working capital: the figure to read twice** **[M1995-064]**. Inventories rose from 10.4% of revenue (2015) to 15.3% (2025),
  and receivables plus contract assets from 22.7% to 30.2%. Advances and contract liabilities moved only from 20.6% to
  23.2%. Customers now fund a smaller share of the working capital than in 2015, and Andritz's own net working capital went
  from -182.1 (2015) to +118.0 (2025) (key figures). The filer gives its own reasons: a rising service share (spare parts are
  held as inventory, and FR2025 C 2 puts service at 44% of group revenue, from 41%) and the acquired manufacturers (Xerium's
  roll covers and clothing). Neither ratio moved alone in one year, and nothing deferred or prepaid is "building up
  suspiciously high" in the statements. **A weighing against, with the cause stated by the filer, not a suspicion.**
- **What they can't say.** About half the revenue is recognized over time on long contracts, by percentage of completion,
  and the margin on each depends on estimated costs to complete. That is the kind of accounting where "anything where
  you’ve got construction in progress or progress payment-type things — there’s so many ways you can cheat in accounting"
  **[M2013-086]**. The 2013 loss (P&P EBITA -35.7) shows estimates that were later corrected by provisions.

**The real costs.** Depreciation and amortization are charged (240.6 in 2025), and capital spending is deducted in full in owner
cash. Stock pay is expensed under IFRS 2 and funded by buybacks (Step 0). Restructuring is the cost the company asks owners to
look through. It reports "comparable EBITA ... without taking into account one-off expenses for restructuring measures"
(FR2025 C 4 a) every year, and capacity measures were charged in 2015 (78), 2019 (113), 2020 (the EBITA to comparable gap,
79.4) and 2023 to 2025 (15.2, 29.8, 50.2). Restructuring "year after year" is a business cost, and telling owners not to count
it "is misleading" **[L2016-007]**. Mitigating: the IFRS EBITA, EBIT and net income are printed first, and the adjusted figure
stands beside them, not in their place. The tell is **an adjusted figure featured** **[L2016-006]**, and it is recorded here as
a weighing and carried to Q5. **EBITDA** appears in the filer's key-figures table and its EV/EBITDA line. It is not the
guided figure, and the guided figure is comparable EBITA, after depreciation. **Guidance** is given every year (2026: revenue
8.0 to 8.3 billion, comparable EBITA margin 8.7 to 9.1%, FR2025 J), and it is carried to Q5. The record on it: the 2025
guidance (revenue 8.0 to 8.3 billion; comparable margin 8.6 to 9.0%, FR2024 J) was missed on revenue (7,883.1) and met on
margin (8.9%). The restatement in FR2015 was a fair-value correction of a listed holding through other comprehensive income,
with no effect on net income (FR2015 note C).

**Confusion?** No. The cash flow statements reconcile year to year, the parts sum to the group (Q1 table), and the management
report explains each charge in plain words ("cost overruns", "did not develop as expected"). That is a management that
"does explain to you in clear terms what’s going on" **[M1994-018]**. Nothing here confuses **[M1995-063]**.

**VERDICT on the accounts: IN (no confusion, no suspicion); WEIGHS AGAINST** on three counts: the restructuring that recurs
while an adjusted figure is featured beside it **[L2016-007]**, **[L2016-006]**; the progress-payment accounting, whose
estimates cannot be checked from outside **[M2013-086]**; and working capital growing faster than sales **[M1995-064]**.
Carried to Q5: the featured adjusted figure and the annual guidance. The recast earnings feed Q7 as owner cash (Step 0
table), not as EBITA.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the managers are read, not met **[M2007-081]**. The record read: the management reports 2013 to 2025, the
H1 2026 report, FR2025 note 7 (pay) and the corporate governance chapter, and the share page.

**Who.** Joachim Schönbeck, President and CEO since April 8, 2022, on the Executive Board since October 1, 2014. Vanessa
Hellwing, CFO since March 28, 2025. Three further members (FR2025 corporate governance). Wolfgang Leitner, who ran the company
before Schönbeck, chairs the Supervisory Board (appointed April 7, 2022). He and Custos Privatstiftung hold about 31.5% of the
capital, partly directly and partly indirectly (Andritz share page). How that stake was acquired is not stated in the
documents read.

**The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* the deciding part's margin went from about
5 to 6% (2011 to 2014) to about 10 to 11% (2021 to 2025). The nearest rival made the same move in the same years (Q2 competitor
row), so part of the gain is the field's and not the managers' own. The group's EBITA margin went from 5.8% (2020) to 8.2 to
8.6% (2021 to 2025). The hand they played badly is Metals (Schuler, bought 2013): repeated capacity cuts and a 2019 goodwill
impairment that the filer itself says arose because "the business did not develop as expected". *How they treat owners:* see
Q6, Part B.

**Integrity, applied on doubt alone** **[M2013-088]**.
- *The reports.* Losses are named in plain words in the year they happen: the 2013 South American pulp-mill "cost overruns"
  (FR2013), the 2019 Metals EBITA margin "clearly negative at -4.5%" with "cost overruns on individual projects" (FR2019). The
  risk report names its own asbestos cases and its "significant losses on certain past projects" (FR2025 D 2). The reports
  tell an owner what an owner would want to know **[M1998-036]**.
- *The habits carried from Q4.* An adjusted figure (comparable EBITA) is featured beside the IFRS figures, and guidance is
  given every year on that adjusted margin. These are "things that they do in public in relation to their investors and the
  promises they make" **[M2004-067]**. Against a make-the-numbers reading: the 2025 revenue guidance was missed (7,883.1 against
  8.0 to 8.3 billion), and the miss was reported plainly. Nothing in the record shows targets "consistently" reached
  **[L2002-041]**. The adjusted figure excludes restructuring, which really does recur (Q4), and that weighs against candour.
  It is not a misstatement, because the IFRS figures come first.
- *Proceedings.* A search of the 2013 to 2025 reports for "investigation", "bribe", "cartel", "public prosecutor" and
  "whistleblow" found compliance-policy text only. **No instance found** of a proceeding against the company or its officers
  for dishonesty in those reports. (Not searched: press coverage, which the brief's primary-document rule does not reach.)
- *Related parties.* Transfer prices with non-consolidated companies are stated to be at arm's length (FR2025 note 7 a). A
  400 TEUR advance to an Executive Board member in 2025, and no loans (note 7).
- *People leave track records* **[M1998-168]**. Leitner's record as chief executive runs from before the 2001 listing, and
  Schönbeck has been on the board since 2014. Over the span read I found no restatement of earnings (the 2015 restatement
  touched other comprehensive income only, Q4). The 2025 audit opinion is unmodified ("present fairly, in all material
  respects", KPMG Austria, FR2025). There was one change of auditor, from Deloitte (the FY2015 report) to KPMG Austria, which
  has audited without interruption since the 31 December 2016 statements (KPMG's report in FR2025). No reason is given in
  the documents read.

**Doubt?** None that a filing raises. The featured adjusted figure and the guidance are a weighing against, read with the
rest of the record, and they do not reach doubt about honesty: the bad years are reported in the IFRS figures and named in the
text.

**Ability.** The moat carries more than the managers, but "the moat and the management are part of the valuation process"
**[M1999-104]**. The record: a doubled equity base without dilution, debt taken for Xerium and repaid within five years, and
the deciding part's margin raised in step with its rival. Against it: Schuler, and capital the business needs that grew
faster than sales (Q4). "We still look to the underlying business, though" **[M1996-037]**.

**VERDICT on integrity: IN. Ability WEIGHS FOR**, qualified by Metals **[M1994-008]**, **[M1999-104]**. The Q4 habits were read with
the integrity record, and they weigh against without raising doubt **[M2004-067]**, **[M2013-088]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
**The retention test** **[R1995-009]**, **[M1998-110]**: does a euro kept become at least a euro of market value? Year-end prices are
implied by the treasury-share disclosures (market value divided by shares held): end-2015 EUR 45.05 (FR2015 key figures),
end-2020 EUR 37.48 (177,809 TEUR / 4,744,104 shares, FR2020), end-2025 EUR 66.75 (400.6 MEUR / 6,001,206 shares, FR2025).

| Span | Net income to owners | Dividends paid | Buybacks paid | Retained | Market value at start | Market value at end | Change |
|---|---|---|---|---|---|---|---|
| 2021-2025 (five-year rolling) | 2,198.1 | 974.7 | 137.3 | **1,086.1** | 3,720.1 (99,255,896 sh × 37.48) | 6,541.4 (97,998,794 × 66.75) | **+2,821.3** |
| 2016-2025 | 3,292.6 | 1,628.6 | 260.9 | **1,403.1** | 4,609.7 (102,324,301 × 45.05) | 6,541.4 | **+1,931.7** |

Each euro retained produced more than a euro of market value over both spans, at the 2025 year-end price. At today's EUR 81.40
the margin is wider. The test also reads value against intrinsic value **[R1995-009]**, and Q7 measures that. Of the retained
money, about 1.0 billion went into acquisitions over the ten years (Step 0 table), so the test is mostly a test of the
acquisitions. **Passes in market value.**

**Dividends.** Payout ratios of 50.3, 50.7, 48.5, 51.8 and 57.8% of earnings (FR2025 C 4 d), cut to EUR 0.50 for 2019 and
restored. The ratio is steady, and it reads as a policy kept near half of earnings. That is the kind of fixed share the rows
call "nuts" **[M2000-051]**. Mildly against, though the documents read state no fixed-ratio policy in words.

**Buybacks.** The 2024 programme was fixed by count and dates ("up to 2,080,000 shares from August 5, 2024 [...] to January 31,
2025", FR2025 note 34 c). No price above which it would stop is named, which is what the rows find "puzzling" **[L2016-002]**.
2,080,000 shares were bought for 116.6 MEUR, **EUR 56.06 a share on average**. Smaller purchases came earlier (48.3 in 2017,
39.8 in 2019, 18.1 in 2020). The shares are used to service the option, PSU and employee programmes (note 34 c), so part of
the buying offsets dilution, which the rows do not accept as a reason **[L2016-002]**. **Written back at Q7 (committed with Q7):** the bottom of Q7's central range is **EUR 59.86** a share (all-equity; equity-only
54.79). The 2024 purchases averaged EUR 56.06, at or below that bottom, so under the convention for a buyback with no stated
price they are read by what they did, not by what the announcement left out **[L1999-023]**, **[L2013-012]**. Earlier buying
was done at lower prices: the year-end prices of 2017 and 2020 were EUR 47.09 and 37.48 (treasury disclosures). The
buyback therefore does **not** weigh against. One further test is noted and not weighed: the rows want every seller to
know "that we think that it’s dramatically — or significantly — undervalued" **[M2012-010]**, and no such statement was found
in the reports read.

**Issuance and deals.** No acquisition in the span was paid in shares. The share count has never risen above 104,000,000
(FR2015 to FR2025). **The all-stock STOP does not arise** **[L2009-019]**. Value given against value got: Schuler (2013) is the
deal that failed its test, with goodwill impaired in 2019 and four rounds of capacity cuts. Xerium (2018) sits in the
deciding part, whose margins rose afterwards. The 2025 deals (333.2 of cash) are too recent to judge. **No post-mortem of
an acquisition against its projections was found** in the reports read (a search of FR2013 to FR2025 for "post-mortem",
"post mortem", "post-acquisition review" and "compared to the original" found none). The rows call such post-mortems "standard practice" that "should" exist **[L2014-013]**.

**Part A WEIGHS FOR**, narrowly. Retention passes in market value. Deals are for cash and in-field. Against it: Schuler, the
payout ratio, and a buyback with no stated price (its reading against the bottom of Q7's range is below).

### Part B: the pay, the board and the owners
- **Pay** (FR2025 note 7; the separate remuneration report was not read and is flagged). Executive Board expense was 10,150 TEUR
  in 2025 and 16,709 TEUR in 2024, against net income of 457.1 and 496.5 MEUR. The short-term bonus is a target bonus plus an
  accident-rate target. The long-term plan is performance share units on **EBITA** and ESG targets over three years. EBITA
  carries no charge for the capital used to raise it, and much of Andritz's EBITA growth was bought (Q3). The rows ask "a
  capital cost element" in the pay of a business that uses capital **[M2009-081]**, and to "charge managers a high rate for
  incremental capital" **[L1994-019]**. Against.
- **Options.** "Holders of exercisable options have the right to purchase shares at the market price of the shares on the date
  of grant" (FR2025 note 34 d), with no step-up for retained earnings. That is the misalignment of the fixed-price option
  **[L1994-021]**. Against. In 2026 they were exercised at EUR 31.20 and 38.80 (H1 2026 note 12 b), against today's 81.40.
- **The board and the owner.** The Supervisory Board chairman and his foundation hold about 31.5% (share page), an ownership
  interest of the size the rows want, and far larger than any fee. Whether it was bought rather than granted, as **[L2002-033]**
  asks, is not stated in the documents read. For, with the flag.
- **Owners as partners.** Annual guidance on the adjusted margin (Q4). The rows name "the scourge of earnings "guidance""
  **[L2019-006]**. Against, mildly, since the guidance was missed and reported.

**Part B WEIGHS AGAINST**: EBITA-based long-term pay with no capital charge, fixed-price options and guidance, offset in part
by a large owner in the chair.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, and "What is the risk-free interest rate" **[L2000-021]**. The rate is the euro sovereign,
3.78% (Step 0), with no risk premium stacked into it **[M1996-024]**. The cash is owner cash after every real cost (Step 0
table), never EBITA or net income. Arithmetic: `computations.py`, output in `computations_output.txt`.

**The window and its aberrational end year** (specific a, **[L2005-003]**). The literal five-year window 2021 to 2025 ends in a year
the filer describes as aberrational. Investing cash flow changed "mainly due to higher net cash flow from company
acquisitions at -328.6 MEUR (2024: -36.9 MEUR)" (FR2025 C 7), with six acquisitions closed in the one year (C 8). Owner cash
with acquisitions deducted fell to 69.4, against a ten-year mean of acquisition spending near 102 a year. The window's
compound rate between end years (-32.1% a year, all-equity) is meaningless, and its halves (-18.5% a year) are dominated by
the same year. So the base is the average over a cycle, and growth is measured between the averages of successive cycles,
with the literal window shown beside. **CONVENTION of this run:** owner cash shows no clean peak-to-peak cycle (troughs in
2018, 2023 and 2025 are driven by working capital and acquisitions, not by one industry swing), so the two successive cycles
are taken as the two five-year windows, 2016 to 2020 and 2021 to 2025. Rationale: each window holds one acquisition spike
(Xerium 2018; the 2025 deals) and one working-capital swing (2018 out and 2019 back; 2023 out), so their averages compare
like with like.

**The inputs** (all-equity basis: owner cash before net non-lease interest, after the company's tax; MEUR).
- Ten-year average owner cash, acquisitions deducted: **200.0**. First cycle (2016 to 2020) average 158.1, second cycle (2021
  to 2025) average 242.0. Growth between them: **+8.9% a year** (aggregate, not per share). The total growth is credited
  because acquisitions are deducted (specific c, default pair).
- The cap (specific f): 200.0 grown 8.9% for ten years reaches about 469, which is 6.0% of 2025 revenue. The highest owner-cash
  share of sales in the filings read is 9.8% (2019, before acquisitions), so no cut is needed. No rate above the discount rate
  is carried after year ten. Zero nominal growth applies after year ten. After year ten, when growth stops, acquisition
  spending would stop with it (specific c), and the no-growth end is then the organic figure. That is shown beside as the
  organic pair, at no growth, because **the filer reports no organic growth rate** (a search of FR2023 to FR2025 for
  "organic" found none).
- Working capital is inside operating cash (specific d). The 2023 draw (-315.4, "project-related") is a single year inside the
  cycle average, not cut out.
- Growth spending (specific e): the filing does not separate maintenance from growth capital spending, so all spending is
  deducted.
- Deals closed after the window and before the price date: none (H1 2026 cash flow: "Net cash flow from company acquisitions
  0.0"). Deals signed but not closed: none stated ("There were no events of material significance after the balance sheet
  date", H1 2026 note 16).
- Net debt: **-593.3** (net cash) at 2026-06-30 (Step 0). Shares 98,310,846.

**The range** (each end valued at 3.78%, ten years, then flat; per share = (value + 593.3 net cash) / 98.31M):

| Case | Base | Growth, years 1-10 | Value @3.78% | Per share | Expected return at EUR 81.40 (EV 7,409.2) |
|---|---|---|---|---|---|
| **Central bottom:** cycle base, no growth | 200.0 | 0% | 5,292 | **EUR 59.86** | 2.7% |
| **Central top:** cycle base, growth between cycles | 200.0 | +8.9% | 11,184 | **EUR 119.80** | 5.5% |
| Beside: literal window, no growth | 242.0 | 0% | 6,402 | EUR 71.15 | 3.3% |
| Beside: literal window, decline by halves (specific b) | 242.0 | -18.5% | 1,378 | EUR 20.05 | 0.5% |
| Beside: organic pair, before acquisitions, no growth | 353.9 | 0% | 9,363 | EUR 101.27 | 4.8% |
| Equity-only, central (beside, never decides alone) | 203.6 | 0% / +10.5% | 5,387 / 13,034 | EUR 54.79 to 132.58 | 2.5% / 5.8% (on market value 8,002.5) |

**Value range (central, all-equity): EUR 59.86 to EUR 119.80 a share against EUR 81.40.** Width 2.0 to 1. The literal window
gives EUR 20.05 to 71.15 (3.5 to 1).

**The floor, tested first.** The floor is about ten percent pre-tax expected return, applied to owner cash after the company's
tax **[M1994-004]**, **[M2003-149]** (CONVENTION, Q7). At EUR 81.40 no case earns it. The best defensible case, the central top
(owner cash growing 8.9% a year for ten years, then flat), returns **5.5%**. The organic pair returns 4.8%, the literal
no-growth 3.3%. Even the equity-only top, which counts the net-cash interest as earnings, returns 5.8%. There is "a point at
which we drop out of the game" **[M2003-149]**, and every case is below it. **Closes OUT**, whatever the width (the floor
tested before the width, 2026-10-10).

What the price implies, for the record: a 10% return on EUR 81.40 would need owner cash of about 740 a year with no growth
(10% of EV 7,409.2). The best year in the eleven read was 573.5 (2019, all-equity, acquisitions deducted), and the ten-year
average is 200.0.

**Fair price** (a reporting figure, never a verdict; Part VII, the owner's price). Each end of the central range is valued at
10% instead of 3.78%, and the two are averaged, per share, after the company's own tax:
- **All-equity basis (the central figure): EUR 35.02 a share.** No-growth end: (2,000 + 593.3) / 98.31M = EUR 26.38. Growth
  end: (3,699 + 593.3) / 98.31M = EUR 43.66.
- **Equity-only basis, beside: EUR 31.84 a share** (20.71 and 42.97).
- Beside, on the literal window: EUR 22.30 (all-equity), EUR 17.46 (equity-only).

No cheap price is reported. Per-ADR figures are not given, because the ADR ratio was not confirmed from the depositary's
documents (Step 0).

**Certainty.** The margin a run asks for grows as certainty falls **[M1997-080]**. Here the owner cash series runs from -358.9
to +573.5 a year, so even the central figures carry a wide error. That does not change the close, since the floor fails on
every case.

**VERDICT: OUT.** The price does not clear the floor on any case in the range: expected returns of 0.5% to 5.5% at EUR 81.40,
against about 10% **[M2003-149]**, **[M1994-004]**. The price sits inside the central range, so even before the floor it would
be a case that "should scream at you" and does not **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file OUT). The bond fact is under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT**, decided at **Q7**: the price does not clear the floor on any case in the range. Central value range EUR 59.86 to
119.80 a share (all-equity), against EUR 81.40. Expected returns 0.5% to 5.5% against about 10%.

Q1 IN, Q2 IN (Pulp & Paper decides), Q3 weighs for, Q4 IN with weighings against, Q5 IN (ability for), Q6 Part A for narrowly and
Part B against. The box is a price close, not a business close: the castle stood on the evidence read. Reporting figures: fair
price EUR 35.02 (all-equity; equity-only EUR 31.84).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**, with sources. No verdict on them, and the box is unchanged (operator rule 2).

**Bearing on Q8 (the alternatives).** The euro 30-year AAA sovereign yields 3.78% (ECB, 2026-10-08). The best case at Q7 returns
5.5% at EUR 81.40, and the literal no-growth case 3.3%.

**Bearing on Q9 (debt and exposures).**
- Net cash of 593.3 at 2026-06-30. Borrowings of 370.3: Schuldscheindarlehen 301.4 at end-2025, an OeKB loan of 51.0, a bank
  loan of 100.0, a 50.0 RCF drawing and other local bank debt (FR2025 C 5 c; H1 2026 balance sheet). A committed 500 MEUR
  revolving facility runs to 2030. There are unused committed facilities of 737 and unused guarantee and surety lines of 3,417
  (FR2025 C 5 d). The guarantees issued against performance, advances and warranty are a contingent claim of the kind the
  standing rule names (collateral and sudden demands); **their amount outstanding was not extracted in this run.**
- Part of the net cash is customers' money. Contract liabilities were 2,181.2 at 2026-06-30 (1,718.9 + 462.3, H1 2026), and net
  working capital moved from -639.2 (2011) to +118.0 (2025). A fall in orders unwinds advances: operating cash was 7.8 in 2018,
  with a working-capital draw of -278.7.
- Fixed-price contracts with liabilities that "can vastly exceed the value of the contract in question" (FR2025 D 2 d), EPC and
  consortium risk (D 2 c), and government contracts with weaker safeguards (D 2 e).
- "The product liability area includes some recent cases involving alleged physical injuries and/or deaths due to asbestos
  exposure." (FR2025 D 2 f). Count, amounts and provisions were not extracted. The rows carry "So we don’t go near asbestos."
  **[M2001-032]** as a candidate exclusion, not a ruling (framework Q9); recorded here, not weighed.
- Pension and similar provisions of 348.3 (2026-06-30). The defined-benefit details were not read.

**Bearing on Q12.** No named business of Q12 is involved (equipment for pulp, paper, metals, hydropower, environment and feed).
Nothing was found.

**Bearing on Q5 (integrity):** none beyond what Q5 weighed. The box line carries no integrity flag, because Q5 was reached and
answered.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 995b258e); written question by question; committed after each
      (Q1 dda4a67d, Q2 3fab7d2a, Q3 d97d3fec, Q4 22853453, Q5 584fb925, Q6 aeb9f499, Q7 e3d3ce21, close in the commit after).
- [x] Dispatched run: the brief allowed pathspec commits of my two paths only; the lock and the fold are the dispatching
      session's (operator rule ten). This run binds nothing until it is folded into the register.
- [x] Blind rule kept: no other run file, holding review, `PORTFOLIO.md`, resume-state file, run queue or prepped reading list
      was opened, listed or searched. `ls "Test Runs" | grep -i -E "ADRZY|andritz"` was run once at the start, before the
      template copy, and returned nothing. It was a name search of the folder listing, and I declare it. The accidental
      sightings (commit subjects, a memory line) are under Contamination and were not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in its row
      (`check_citations.py`: 0 problems). No E-ids. Every filing fact names its report and section; no SEC accessions exist for
      this name, so the brief's departure was used (title, date, URL).
- [x] The order was kept; the first failing STOP (Q7) closed the run; Q8 to Q12 are NOT REACHED and nothing after Q7 is a
      clearance.
- [x] Owner cash after every real cost, from the filed cash flow statements (operating cash less all capital spending, lease
      principal and acquisitions); never net income. Sovereign from the ECB. The price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, seven items); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor rule applies.
- [x] `tools/run.py` produced no lines (not an SEC filer); all arithmetic is mine, in `computations.py` and `balance_sheets.py`.
- [x] `python tools/check_framework.py` PASS before each commit.
- **Weaknesses I admit.** (1) The 2019 lease principal is an estimate (lease interest not found); it is outside the central window
      and only touches the cycle base. (2) Company-wide stock-pay cost was not extracted, only the Executive Board figure. (3)
      The remuneration report, the guarantee amounts and the asbestos provisions were not read. (4) Segment scope changes in
      2018/2019 and 2023 blur the 2011 to 2025 Pulp & Paper margin series. (5) Valmet is the only rival with primary figures,
      and its group figures after 2022 include Neles. (6) The Q7 cycle definition is a CONVENTION of this run, and a
      different reasonable one changes the range. It does not change the close: the literal window, the organic pair and the
      equity-only basis all fail the floor too.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Specific (a) assumes an industry cycle, and this series has none.** Owner cash here swings with acquisitions and project
   working capital, not with one industry cycle. The rule says "peak to peak or trough to trough" and gives no way to pick
   cycles when the troughs are deal years and working-capital years. I used two successive five-year windows and confessed it
   as a CONVENTION of this run. The rule could say what to do when the aberration is a spending choice (an acquisition spike)
   rather than a cyclical turn.
2. **"Operating leases left out" has no meaning for an IFRS 16 lessee.** IFRS 16 puts every lease on the balance sheet. I
   deducted lease principal from owner cash and left lease liabilities out of net debt, consistently. The basis rule should
   say which treatment an IFRS filer takes.
3. **A non-deciding open part "carried to Q7 as an ordinary business at no growth"** (Q2, business of parts) has no mechanism in
   Q7, which values group owner cash. I could not value Metals separately from cash-flow data the filer does not split by
   segment. The instruction could say whether segment EBITA after a capital charge, or a share of group owner cash, is meant.
4. **Net cash that is customers' prepayments.** The basis rule subtracts all cash and securities as filed. For an
   advance-funded project business, part of that cash is owed back in work, and it unwinds when orders fall (2018). The rule
   is silent. I followed it as written and recorded the fact at AFTER THE STOP.
5. **Q1's doubt rule against Q4's and Q9's ground.** "If you have doubts [...] it isn't" **[M2002-092]** does not say whether doubt
   about the size and timing of single years (fixed-price project tails) is doubt about the circle. I read it as not, and
   carried that doubt to Q4, Q7 and Q9. A sentence in Q1 would settle it.
6. **The template's Step 0 asks for accessions and `cover_shares.py`**, which do not exist for a non-SEC filer. The brief's
   departure covered it. The template could carry the non-SEC substitute (document, date, URL; issued less treasury from the
   report) itself.
