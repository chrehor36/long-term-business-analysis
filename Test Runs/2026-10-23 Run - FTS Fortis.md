# Company Run: Fortis Inc. (NYSE and TSX: FTS), 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 06504e86). Every judgment cites a v5
ledger id in bold; every filing fact carries its accession. Dispatched blind run under `Screens/_daily/_dispatch_brief.md`
with the brief's one stated departure (the analyst derives the lines of evidence; see Step 0).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-23, after the run was committed (bc147d34): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Contamination, declared and not used.** (1) The first directory listing of `Test Runs/` (taken to find the dated file
name) showed run files and research folders dated 2026-10-23 for EDN, ENIC, ES, ETR, EVRG and FE; none was opened. (2) The
session context carried git commit subjects of the FE run of 2026-10-23 (its box and computed figures) and a git status
naming research folders of ARCB and AYI; not used. (3) The adopted case `Framework/v5/CASE 2026-10-18 - the regulated
utility's fair price, decided from the corpus.md`, read because Q7's regulated-utility paragraph cites it, names sixteen
other utilities that closed OUT at Q7 on 2026-10-17 and 2026-10-18 and four that were re-queued; FTS is not among them;
not used. (4) The user's memory index, loaded with the session, carries queue-state lines (counts of gate-clearers, holding
reviews owed); it names no ticker of this run; not used. Nothing about Fortis from any other run file was seen.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** C$80.99 (TSX: FTS.TO, close 2026-10-22; Yahoo Finance chart endpoint through `tools/sources.py`,
  **aggregator, flagged** under operator rule 5, live quote only). NYSE line US$57.88 the same day; USD/CAD 1.4016
  (aggregator), consistent. The earnings currency is the Canadian dollar, so the TSX price is used throughout.
- **Shares:** one class of common shares (preference shares have no vote unless eight quarterly dividends are missed,
  MD&A 2025 p.17). `python Screens/cover_shares.py FTS`: 507,340,068 common shares, 40-F cover, period 2025-12-31, filed
  2026-02-12, accession `0001666175-26-000013`; the audited balance sheet says 507.3 million issued and outstanding (no
  treasury shares are reported). Later filings: 510.9 million at 2026-06-30 (Q2 2026 interim balance sheet, 6-K filed
  2026-07-31, accession `0001666175-26-000031`), plus 4,365,256 issued 2026-07-01 to 2026-09-04 under the ATM program,
  DRIP, employee plan and option plan for about C$331 million (prospectus supplement, SUPPL filed 2026-09-10, accession
  `0001104659-26-106675`, "Changes in Share and Loan Capital Structure"). **Count used: 515.27 million.** Options
  outstanding 0.9 million (MD&A 2025 p.17), not added.
- **Market cap:** C$80.99 x 515.27M = **C$41,731M**.
- **Sovereign for the earnings currency:** **4.19%**, Government of Canada long-term benchmark bond yield, Bank of Canada
  Valet series `BD.CDN.LONG.DQ.YLD`, observation of 2026-10-21 (issuing authority, operator rule 5; the protocol's table
  has no CAD row, so the series is named and dated here). For reference `tools/sources.py` printed USD 5.29% (US Treasury,
  10/22/2026).
- **Filings read** (operator rule 4): 40-F for FY2025 filed 2026-02-12, accession `0001666175-26-000013` (Exhibit 99.1
  Annual Information Form, Exhibit 99.3 MD&A, the audited statements `fts-20251231_d2.htm`); Q2 2026 6-K filed 2026-07-31,
  accession `0001666175-26-000031` (interim statements and MD&A); the 2026 Management Information Circular, 6-K filed
  2026-03-30, accession `0001104659-26-036461`, exhibit 99.1; prospectus supplement for the junior subordinated notes,
  accession `0001104659-26-106675`, and the pricing release, 6-K accession `0001104659-26-106434`; the 6-Ks of 2026-05-07
  (`0001171843-26-003143`, meeting results), 2026-07-29 (`0001171843-26-005039`, dividends), 2026-10-05
  (`0001171843-26-006410`, Q3 date and new capital outlook on 2026-11-03); the MD&A exhibits of the 40-Fs for FY2021
  (`0001666175-22-000019`), FY2022 (`0001666175-23-000014`), FY2023 (`0001666175-24-000020`) and FY2024
  (`0001666175-25-000017`); the Q1 and Q2 2024 MD&As (6-Ks `0001666175-24-000028`, `0001666175-24-000044`) for the
  Central Hudson billing proceeding. Ten-year figures transcribed from SEC companyfacts (XBRL of the 40-Fs), every one used
  in a judgment read back against a filed statement or MD&A.
- **One figure cross-checked against the filed statement:** cash from operating activities FY2025 C$4,062M (companyfacts)
  equals the audited consolidated statement of cash flows, accession `0001666175-26-000013`; FY2021 C$2,907M and FY2023
  C$3,545M equal the cash-flow summaries of the FY2021 and FY2023 MD&As.
- `python tools/run.py FTS` printed "FTS: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (it reads 10-K and
  20-F facts, not 40-F). Every figure below is therefore from the filed statements and the companyfacts transcription of
  them (`Test Runs/_research 2026-10-23 FTS/table10.txt`), not from `tools/run.py`.
- **The lines of evidence this name needs (the brief's departure: derived here from the filing).** From the AIF's business
  description, the MD&A's segments and its Business Risks, and Note 2 of the statements: (1) **regulation**: allowed ROE and
  deemed equity at each utility, rate cases, FERC challenges to ITC's ROE and adders, regulatory lag at UNS Energy, the
  FortisAlberta PBR appeal; (2) **the capital plan and its funding**: C$28.8B for 2026-2030, rate base CAGR 7.0%, funded
  by cash from operations, utility debt, the DRIP and an ATM program; (3) **the parts**: seven reporting utilities, ITC the
  largest; (4) **physical and wildfire risk**, which the MD&A names among its most significant climate hazards and which
  moved S&P's outlook; (5) **gas competitiveness** in British Columbia (about 20% of revenue from gas, 80% of that in BC);
  (6) **the holding company's debt, ratings and cover**, since Fortis has no revenue of its own; (7) **the people and the
  pay**, from the circular, with the Central Hudson billing-system and gas-explosion proceedings. Chosen because each is a
  line the filing itself says could have a "Material Adverse Effect" or is a measure management says it is judged by.

**Contrary evidence, written down as found** **[M1997-127]**: (a) owner cash after all capital spending was negative in
every year 2021 to 2025 (C$-702M to C$-1,886M); the dividend is in effect paid from borrowing and from shares issued;
(b) earnings cover of interest and preference dividends 1.89x and 1.97x (prospectus supplement); (c) Moody's Baa3 rating
withdrawn at the Corporation's own request in January 2026, after Fitch assigned BBB+ in May 2025; (d) return on book
common equity 7.1% to 7.7% a year 2021 to 2025, about three points below three U.S. peers, because of C$12.5B of goodwill;
(e) a US$63M write-off of Central Hudson's failed billing system, and a gas explosion in 2023 with a US$105M contingent
liability (insured); (f) CEO pay up 70% 2020 to 2025 against adjusted EPS up 37%; (g) shares issued every year, 466.8M at
end-2020 to 515.3M now.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the owner "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**, and a regulated monopoly whose earnings rest on rate base and allowed return passes that test
of mindset easily; the quotation "just tells us prices" **[M2006-077]**. No macro enters **[M2000-094]**: the run does not
forecast Canadian or U.S. rates or the exchange rate, though the filing says the share price is "inversely correlated to
interest rate changes" (MD&A 2025 p.27), which is a fact about the price, not a forecast. Who is paid to tell you
**[M2020-037]**: the company's own five-year capital plan and dividend guidance are a seller's projection, and are not used
as inputs. The margin of safety is an attitude here: "if you have to actually do it on — with pencil and paper, it’s too
close to think about" **[M1996-084]**. The analyst's incentive: none known (blind run); the builder's incentive to find a
"buyable utility" after a run of utility OUTs is named and set against.

## THE STANDING RULE
A part-interest bought for cash with no borrowing and sized so a fall of half leaves the buyer whole does not put the buyer
at risk of ruin: "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this name requires the buyer to
borrow or to give anyone an option on the buyer's cash. Satisfied as to the buyer; the target's own debt is Q9's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**; the definition "where the business will be in
  10 years" **[M2000-037]**.
- **The business, from the filing.** "Fortis is principally an energy delivery company, with approximately 95% of its
  assets related to transmission and distribution" (MD&A 2025 p.1, `0001666175-26-000013`). Ten regulated utilities in five
  provinces, ten states and Grand Cayman; regulated utility assets "represented virtually all" of assets (MD&A p.22). Its
  only non-regulated business (Belize hydro) was sold on 2025-10-31. Earnings are set under cost-of-service or PBR
  regulation "including a fair rate of return on a deemed or targeted capital structure applied to an approved Rate Base"
  (Note 2).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) rate base, C$42.4B midyear 2025, which grows
  by what is spent above depreciation; (2) the allowed ROE and deemed equity at each utility (Note 2 table: ITC 10.73% on
  60%, TEP 9.55% on 54.3%, Central Hudson 9.50% on 48%, FortisBC Energy 9.65% on 45%, FortisAlberta 8.97% on 37%, and so
  on); (3) regulatory lag, which the filing names as significant at UNS Energy; (4) the U.S. dollar (65% of assets in the
  U.S.); (5) physical risk, chiefly wildfire. The first two are set by commissions in published proceedings and change by
  tens of basis points (every 10 basis points at ITC is about C$0.01 of EPS, MD&A p.12); the economics of a wires business
  ten years out are as foreseeable as anything in this circle. Do the past statements tell the future ones **[M2008-033]**:
  yes, for a business whose revenue is a formula of rate base and allowed return. Would insiders write it down
  **[M2000-105]**: they do, every year, as a five-year rate base forecast; the run does not use it, but the test is met.
  The economics are understood though the engineering is not, as **[M2011-014]** allows: "What is important is that I
  understand the economic dynamics of the industry."
- **The parts** (Q1's holding-company paragraph): every part that matters is a regulated electric or gas utility read by
  the same tests; no part is a bank, a trading book or a fast-changing technology.
- **What is not foreseeable, written down.** Wildfire liability and the regulatory climate can take the return away; these
  are castle questions and go to Q2 and Q9, not grounds to say the economics cannot be pictured. Doubt rule **[M2002-092]**:
  no doubt that this is inside the circle; the doubt is about the castle's weak wall, the regulator, and is carried there.
- **VERDICT: IN.** A regulated wires-and-pipes holding company whose ten-year earning power is rate base times allowed
  return, both read from the filing **[M2012-065]**, **[M1998-044]**, **[M2006-076]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now" **[M1995-038]**.

**The parts table** (business of parts, Q2; segment common equity earnings as the filer reports them, MD&A "Business Unit
Performance", 40-Fs for FY2021 to FY2025. CONVENTION of this run: the filer reports earnings after interest by segment and
no operating profit by segment, so the threshold is applied to segment earnings; rationale: it is the only segment profit
the filing states, and no part comes near half on any measure.)

| part | 5-yr earnings 2021-25 (C$M) | share of the regulated and infrastructure total (C$8,331M) | castle | decides |
|---|---|---|---|---|
| ITC (FERC electric transmission, 80.1% owned) | 2,522 | 30.3% | legal monopoly on transmission in its zones, FERC formula rate | **yes, the largest** |
| UNS Energy (TEP, Arizona) | 1,905 | 22.9% | integrated utility under the ACC, historical test year | no |
| FortisBC Energy (gas, BC) | 1,291 | 15.5% | gas distribution monopoly; gas competes with electricity for heat | no |
| FortisAlberta | 817 | 9.8% | distribution under PBR | no |
| Other Electric (NL, PEI, Ontario, Cayman) | 728 | 8.7% | small integrated utilities | no |
| Central Hudson (New York) | 620 | 7.4% | T&D under the NY PSC | no |
| FortisBC Electric | 338 | 4.1% | integrated, BC | no |
| Energy Infrastructure (2021-22; then sold or folded into Corporate) | 110 | 1.3% | contracted generation, gas storage | no |
| Corporate and Other | (944) | holding company cost, not a part | | |

No part carries more than half of five-year earnings, so the largest, ITC, decides (Q2, A business of parts). Every other
part is also a regulated monopoly and none is shown open; they are read for the field-returns test below.

**The castle tests, on ITC and then the field.**
1. *What keeps it standing* **[M1995-038]**: a transmission line is a legal franchise priced by formula, "Cost-based
   formula rates, with annual true-up mechanism", with an allowed ROE of 10.73% on 60% equity including 0.75% of adders
   (Note 2, `0001666175-26-000013`). The customer comes because there is no other wire; the reason lasts because of
   statute and the cost of duplication.
2. *The attacker with money* **[M2011-015]**: nobody builds a parallel high-voltage grid into ITC's zones; the kin row is
   "You really couldn’t create another railroad" **[M2013-054]**. The attack the filing names is on new lines, not old:
   "The Corporation faces competition in its transmission business which may restrict its ability to grow this business
   outside of its established service territories. Challenges to existing right of first refusal statutes applicable to
   the transmission business may also restrict future growth" (AIF 2025, Competition). MISO tranche 2.1 projects outside
   right-of-first-refusal states go to competitive bidding, and in July 2025 state commissions filed a FERC complaint
   against the tranche 2.1 portfolio (MD&A 2025 p.20). The castle stands; part of its growth is contestable.
3. *Pricing power and the agony before a rise* **[M2005-020]**: none in the usual sense. The regulator sets the price, and a
   regulated business "operates under the threat of reregulation, which has a tempering effect on their pricing power"
   **[M2007-112]**. The evidence is the path of the allowed ROE: FERC cut ITC's MISO base ROE to 9.98% from 10.02% in
   October 2024 with a C$20M retroactive charge (MD&A 2025 p.7), after a May 2020 decision that raised it (FY2021 MD&A);
   the 2021 proposal to remove the 50-basis-point RTO adder is still open after five years (Note 2). The moves are tenths
   of a point: "whether you earn X or X plus a half a percent or X minus a half a percent, that differs by state"
   **[M2024-011]**.
4. *Would the customer choose it over the low bid*: the customer cannot choose. At FortisBC Energy, where a customer can
   choose electricity over gas for heat, the filing says "Upfront capital costs for gas service continue to present
   competitive challenges for natural gas compared to electricity service" (MD&A 2025 p.25). That part is 15.5% and does not
   decide; written down as the one part where a substitute is named.
5. *Widening or narrowing* **[M1999-108]**: rate base grew and ITC's earnings rose from C$426M to C$592M (2021 to 2025);
   allowed ROEs moved both ways (Central Hudson up to 9.50% from mid-2024; FortisAlberta down to 8.97% by formula; ITC's base
   down four basis points). Neither widening nor narrowing on the evidence; flat.
6. *What could destroy, modify or reduce it* **[M2000-014]**: the regulatory climate, which the speakers name as the one
   regulated moat that broke on them: "the regulatory climate in a few states has raised the specter of zero profitability
   or even bankruptcy" **[L2023-011]**; and wildfire, which the filing lists with strong winds, extreme heat and flooding as
   "its most significant climate hazards" (MD&A 2025 p.23), and which S&P cited when it moved the outlook to stable in
   November 2025 ("developments at the subsidiaries to mitigate physical risks, namely wildfires", MD&A p.18). Transmission
   is the least exposed part; TEP in Arizona and the BC and Alberta utilities are more so. This castle is breached by a
   commission or a court, not by a competitor: "courts can change values" **[M2025-045]**.

**The competitor row.** The filing names no rival company (AIF 2025, Competition: competition "is primarily from
alternative energy sources and on-site generation by customers", and in transmission from unnamed bidders).
**CONVENTION of this run:** three SEC filers chosen for overlap: Ameren (AEE, a MISO member with transmission and regulated
utilities in Missouri and Illinois), Xcel Energy (XEL, MISO and the upper Midwest, where ITC Midwest operates), Pinnacle West (PNW,
under the Arizona Corporation Commission, TEP's regulator); rationale: the field's returns are set by the same regulators,
so these are the nearest evidence of what the field earns. Canadian peers (Emera, Hydro One, AltaGas) do not file 10-Ks
with the SEC and are not used. Metric: net income to common over average common equity, and operating cash less capital
spending, each from its own 10-K facts (SEC companyfacts; `Test Runs/_research 2026-10-23 FTS/peers.txt`), 2016 to 2025.

| company | mean ROE | range | years with OCF less capex negative |
|---|---|---|---|
| Ameren (2016-25) | 10.2% | 7.3% to 11.4% | 9 of 10 |
| Xcel Energy (2016-25) | 10.4% | 9.4% to 10.8% | 10 of 10 |
| Pinnacle West (2016-25) | 9.5% | 8.1% to 10.7% | 9 of 10 |
| Fortis, book common equity, preference shares removed (2017-25) | 7.8% | 7.1% to 10.4% (2019 holds the Waneta sale gain) | 9 of 9 |

**The field's returns over the last full cycle, in words.** The field earns its allowed return, about nine to eleven percent
on equity, steadily, through the 2020 recession year and the rate rise of 2022 and 2023, and consumes more cash than it makes
in nearly every year. Fortis's utilities earn about the same on the equity the regulators deem (regulated segment earnings
of C$1,980M in 2025 against about 50.7% of a C$42.4B midyear rate base, roughly 9.2%, an arithmetic line); its lower 7.8% on
book equity is the C$12.5B of goodwill paid for ITC, UNS and Central Hudson, which is a capital-allocation fact (Q3, Q6),
not a castle fact **[M2011-060]**. These are ordinary returns, but "A return set by a regulator is the exception, carried to
Q3 as a second best" (Q2, What it rules OUT): "there’s no way we get rich on our utility investments. But there’s no way we
get poor, either" **[M2009-104]**. So the ordinary-returns line does not close the file; the second best is weighed at Q3.

- **Is the castle open on the evidence?** No: no attacker can duplicate the wires, and the returns held through the window.
  **Can its future be judged?** Yes, within a band: the ten-year economics of regulated transmission turn on tenths of a
  point of ROE, and the way the castle falls (a hostile regulator, a wildfire judgment) is named, read and carried to Q9.
- **VERDICT: IN**, with the regulator as the weak wall **[L2023-011]**, **[M2024-011]**, and a castle that protects a fair,
  not an excellent, return **[L2007-004]**, **[M2009-104]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital the business needs** **[M2010-090]**: the regulated utilities earn about their allowed returns on
  the equity the regulators deem, roughly 9.2% in 2025 (Q2). On what Fortis paid, which includes C$12.5B of goodwill,
  the return on book common equity was 7.1% to 7.7% a year in 2021 to 2025 (Q2 table). Goodwill is forgotten in judging the
  business and kept in judging the allocation, "because we paid for it" **[M2011-060]**: the business earns a fair regulated
  return; the price paid for it earns about seven and a half percent.
- **What must go back in to stand still, and to grow** **[L1999-024]**, **[M2000-144]**. The filing gives no maintenance
  figure. Capital spending net of contributions in aid of construction, with the "Other" investing line (which the MD&A ties in part to demand-side
  management spending at FortisBC, MD&A 2025 p.15) included, against depreciation and amortization (C$M, cash-flow statements,
  arithmetic in `Test Runs/_research 2026-10-23 FTS/q7_out.txt`):

| year | operating cash | capital spending, net of CIAC | D&A | spending above D&A | net debt raised |
|---|---|---|---|---|---|
| 2021 | 2,907 | 3,488 | 1,505 | 1,983 | 1,138 |
| 2022 | 3,074 | 3,959 | 1,668 | 2,291 | 1,790 |
| 2023 | 3,545 | 4,172 | 1,773 | 2,399 | 1,415 |
| 2024 | 3,882 | 5,395 | 1,927 | 3,468 | 1,944 |
| 2025 | 4,062 | 5,809 | 2,057 | 3,752 | 2,313 |

  Spending ran at 2.3 to 2.8 times depreciation; the five-year plan is C$28.8B more (MD&A p.18). The utilities "are
  obligated to provide service to customers within their respective service territories" (MD&A p.17), so much of the
  spending is compulsory; but it is compulsory at an allowed return, not at an unknown one. The speakers name both sides:
  "To earn more, their owners must invest more" **[L2011-019]**, and the capital-heavy business that frightens is the one
  "where you just pump in more money without knowing" the return **[M2009-104]**.
- **What the added capital earned.** Book common equity before AOCI rose about C$4.0B from end-2020 to end-2025 (about
  C$2.3B of it new shares, the rest retained) and debt about C$9.8B; common equity earnings rose from C$1,209M to C$1,714M
  and operating income from C$2,508M to C$3,492M (statements, `table10.txt`). About 12% on the added equity and about 7%
  pre-tax on all the added capital, both flattered by a stronger U.S. dollar (average 1.34 in 2020 against 1.40 in 2025).
  That is "decent returns on the incremental sums they invest" **[L2009-012]**, at the rate the regulator sets, not more:
  "we’re not earning a higher rate of return on capital than we were when we started. We just put way more capital into
  the business" **[M2023-081]**, said of the speakers' own utility.
- **The growth arithmetic.** The business is the second grade of **[M1998-081]**: it gives more money each year but takes
  more money to do it, at a rate the regulator calls fair. Owner cash after every dollar of spending was negative in each of
  the five years; the dividend is in effect funded by borrowing and by the DRIP. The rows accept such a business as "the
  second-best choice, still a good choice" **[M2018-055]**, provided "the cash they consume gets to earn a reasonable
  return" **[M2012-057]**.
- **WEIGHS: UNDECIDED.** The added capital earns its allowed return, which the rows call decent and second best
  **[L2009-012]**, **[M2018-055]**; against it, the capital Fortis paid for its utilities earns about 7.5%, below the field,
  and the business consumes more cash than it makes every year **[L2011-019]**, **[M2012-057]**. The "little or no debt"
  criterion is Q9's.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them** **[M2025-032]** (C$M at 31 December; SEC companyfacts transcription of the 40-Fs,
the 2024 and 2025 columns read against the audited balance sheet, `0001666175-26-000013`; total debt for 2016 to 2018 omits
finance leases, which were not tagged those years; receivables for 2016 not tagged):

| line | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 6,838 | 8,301 | 8,390 | 8,783 | 8,935 | 9,448 | 11,043 | 11,517 | 11,508 | 12,170 |
| Total assets | 47,904 | 47,822 | 53,051 | 53,404 | 55,481 | 57,659 | 64,252 | 65,920 | 73,486 | 74,830 |
| PP&E, net | 29,337 | 29,668 | 32,757 | 33,988 | 35,998 | 37,816 | 41,663 | 43,385 | 49,456 | 50,886 |
| Goodwill | 12,364 | 11,644 | 12,530 | 12,004 | 11,792 | 11,720 | 12,464 | 12,184 | 13,112 | 12,527 |
| Regulatory assets | 2,933 | 3,045 | 3,075 | 3,383 | 3,588 | 3,589 | 4,009 | 4,384 | 4,631 | 5,022 |
| Receivables | 0 | 991 | 1,080 | 1,070 | 1,102 | 1,269 | 1,759 | 1,549 | 1,669 | 1,493 |
| Inventories | 372 | 367 | 398 | 394 | 422 | 478 | 661 | 566 | 685 | 649 |
| Cash | 269 | 327 | 332 | 370 | 249 | 131 | 209 | 625 | 220 | 367 |
| Total debt (short-term, LTD incl. current, finance leases) | 22,223 | 21,605 | 24,145 | 23,140 | 24,832 | 25,919 | 29,003 | 29,992 | 33,659 | 34,634 |
| Deferred income taxes | 3,263 | 2,298 | 2,686 | 2,969 | 3,344 | 3,627 | 4,060 | 4,399 | 5,020 | 5,292 |
| Common shares (paid in) | 10,762 | 11,582 | 11,889 | 13,645 | 13,819 | 14,237 | 14,656 | 15,108 | 15,589 | 16,112 |
| Retained earnings | 1,455 | 1,727 | 2,082 | 2,916 | 3,210 | 3,458 | 3,733 | 4,112 | 4,521 | 4,969 |
| AOCI | 745 | 61 | 928 | 336 | 34 | -40 | 1,008 | 653 | 2,067 | 1,101 |
| Shareholders equity (incl. C$1,623M preference) | 14,597 | 15,003 | 16,533 | 18,531 | 18,697 | 19,288 | 21,030 | 21,505 | 23,808 | 23,810 |
| Non-controlling interests | 1,853 | 1,746 | 1,923 | 1,582 | 1,587 | 1,628 | 1,812 | 1,827 | 2,045 | 2,059 |
| Common shares outstanding (M) | 401.5 | 421.1 | 428.5 | 463.3 | 466.8 | 474.8 | 482.2 | 490.6 | 499.3 | 507.3 |

**What moved, and what the figures say and do not say.**
- *Goodwill against equity.* Goodwill of C$12.4B arrived with ITC in October 2016 and has moved since only with the
  exchange rate (C$11.6B to C$13.1B); goodwill impairment tagged at zero every year 2015 to 2025 (C$27M and C$50M written
  off with businesses sold in 2023 and 2025). It is 56% of common equity at end-2025
  (C$12,527M against C$22,187M). The equity is mostly paid in and goodwill: paid-in common capital rose C$5.35B over the
  decade, retained earnings C$3.51B. The owners have put in more than the business has kept.
- *Debt.* Total debt rose from C$22.2B to C$34.6B, faster than equity; the MD&A's own capital structure is 57.0% debt,
  2.7% preference shares and 40.3% common equity and minority interests at end-2025 (MD&A p.17), against a rate-base-weighted
  regulatory debt share of about 49% (Note 2 equity ratios, Q7). The gap is holding company debt that funded acquisitions.
- *Working capital against sales.* Receivables C$991M to C$1,493M (+51%) and inventories C$367M to C$649M (+77%) against
  revenue C$8,301M to C$12,170M (+47%) from 2017; the inventory rise is gas and fuel, a flow-through cost; nothing building
  out of line. Regulatory assets C$3.0B to C$5.0B (+65%); the MD&A explains the 2025 rise as deferred income taxes, deferred
  energy management costs and rate stabilization accounts (MD&A p.13).
- *Cash* is a few hundred million, a residual; the business runs on credit facilities (C$5.8B, C$3.7B unused).
- *What the figures cannot say:* whether the regulators will keep allowing the return on the C$50.9B of plant; that is
  Q2's and Q9's.

**The real costs.**
- Depreciation is charged (C$2,057M in 2025) and is "almost always true costs" **[L2015-004]**; "With rare exceptions,
  depreciation is an economic cost every bit as real as wages, materials, or taxes" **[R1996-023]**. Here spending runs
  2.3 to 2.8 times depreciation (Q3), so reported earnings are not cash to the owner.
- Stock pay is expensed and cash-settled for PSUs and RSUs; the MD&A names "higher stock-based compensation" among the
  2025 cost increases (MD&A p.2), and total return swaps hedge it. Counted inside operating cash.
- *Non-cash income.* The equity component of AFUDC was C$174M in 2025 (C$77M in 2021), about 10% of common equity
  earnings: earnings booked on plant under construction, recovered later in rates. It is removed in operating cash, which
  the run uses; written down because it grows with the capital plan.
- *Recurring "one-time" items.* Adjusted earnings remove the 2025 disposition losses (C$63M) and the 2024 FERC ROE refund
  (C$20M) (MD&A p.10). Over 2020 to 2025 the adjustments run both ways: adjusted common equity earnings were below reported
  in 2020 to 2023 (C$1,195M against C$1,209M; C$1,219M against C$1,231M; C$1,329M against C$1,330M; C$1,502M against
  C$1,506M) and above in 2024 and 2025 (circular 2026, p.68). Not a one-way habit.
- *EBITDA in the filer's own mouth:* not found in the 40-F exhibits, the Q2 2026 report or the circular (text search for
  "EBITDA"); the rows' test **[M1998-086]** is not engaged.
- *Pensions* are partly flowed through regulatory deferral (MD&A p.28); no fanciful assumption found in the documents read.
- *Deferred taxes* of C$5.3B: in a utility, "I don’t think I would look at that as a hidden form of equity" **[M2015-030]**.

**The habits carried to Q5** (Q4, the make-the-numbers paragraph): (i) the "Performance at a Glance" table puts "Adjusted"
common equity earnings and EPS beside "Actual" on the first page of the MD&A; the rows are "nervous" of a management that
"regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings"" **[L2016-006]**; here the
adjusted items are few, disclosed and reconciled, and run both ways, so this weighs lightly; (ii) guidance: "Fortis is
targeting annual dividend growth of approximately 4-6% through 2030" and a rate base CAGR of 7.0% (MD&A p.3, p.38); the
rows call predicting growth rates "both deceptive and dangerous" **[L2000-037]** and blame "the scourge of earnings
"guidance"" **[L2019-006]**; Fortis gives dividend and rate-base guidance, not EPS guidance; (iii) pay on EPS targets beaten
(circular; Q5, Q6). Clear speech is a plus **[M1994-018]**: the MD&A explains every segment's variance in plain words and
has named its own failures in its MD&As (the Central Hudson billing system, FY2022 to Q2 2024; the gas explosion, FY2024
and the statements since).

- **VERDICT on the accounts: WEIGHS AGAINST, lightly.** No confusion and no suspicion **[M1995-063]**: the statements are
  plain, the adjustments small and two-sided. Against: the adjusted figure is featured **[L2016-006]**, growth is guided
  **[L2000-037]**, and the earnings are not the owner's cash, since the business must reinvest more than it earns
  **[L2015-004]**. The recast earnings for Q7: owner cash after interest, tax, depreciation and all compensation
  **[L2021-003]**, computed from operating cash, which excludes the AFUDC equity income.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The question for a stock is read, not met: "We read a lot. We read annual reports. We read about competitors"
**[M2007-081]**; the after-the-sale test belongs to whole businesses (Q5, The tests). The yardsticks are "how well they run
the business" against "the hand they were dealt", and "how well that they treat their owners" **[M1994-008]**.

**The people, from the filings.** David Hutchens, President and CEO since 2021-01-01, a career utility operator (UNS Energy
in Arizona, its CEO from 2014, then Fortis's COO); not the chair: the board "is led by an independent chair and 11 of the
nominated directors are independent" (circular 2026, `0001104659-26-036461`). He holds 140,415 common shares and 128,809
RSUs, 11.9 times salary against a 6 times requirement (circular, share ownership table, 2026-03-20). The business is run
through autonomous subsidiaries, "Each of our significant operating subsidiaries is governed by its own board of directors,
with a majority of independent and local directors" (circular, letter to shareholders).

**1. The record against the hand dealt** **[M1994-008]**. The hand is a set of regulated monopolies whose return is set by
commissions; the play is whether the utilities earn what is allowed, keep the regulators' trust and fund the plan without
damage. On the evidence: regulated segment earnings of about 9.2% on deemed equity in 2025, near the allowed returns (Q2);
TSR over 2020 to 2025 of C$166 per C$100 against C$167 for the company's own TSR peer group, C$136 for the S&P/TSX Capped
Utilities Index and C$211 for the S&P/TSX Composite (circular p.68). Against the record: the Central Hudson billing system,
where the New York PSC opened a show-cause proceeding in December 2022 and US$63 million of costs "were agreed to not be
recovered from customers" (Q2 2024 MD&A, `0001666175-24-000044`); a gas explosion in November 2023 during contractor work
on Central Hudson's system, a PSC show-cause order on it in October 2024 (FY2024 MD&A), and a contingent liability raised
to US$105 million at 2026-06-30 with an equal insurance receivable (Q2 2026 statements, `0001666175-26-000031`); the 2025
FFO-to-debt incentive measure scored 0% (circular, 2025 corporate performance table); S&P's outlook was negative until November 2025 (MD&A 2025, Capital
Structure and Credit Ratings). Both Central Hudson failures sit in the smallest U.S. utility; neither touched the deciding part, ITC.

**2. The proxy: how they treat themselves against the owners** **[M1994-009]**. CEO pay awarded rose from C$10.2 million
(2020, the previous CEO) to C$17.3 million in 2025, +70%, against adjusted EPS +37% (circular p.68), the circular adding
that the increase "is significantly impacted by foreign exchange" since his pay is set in U.S. dollars. Pay of all named
executives as a share of adjusted earnings fell from 2.25% to 1.75% over the same years (p.68). The pay plan is weighed
at Q6, Part B; here the question is only whether it shows a management that favours itself, and the evidence is mixed:
the CEO's pay grew much faster than the per-share figure, but the whole team's take did not grow faster than earnings.

**3. The reports, and the habits carried from Q4** **[M1998-036]**, **[M2004-067]**. The MD&A explains each utility's
earnings in plain words, names its regulatory proceedings and their status every period, and gives the dividend payout
ratio and its five-year average. The habits: (i) an adjusted EPS figure on the first page beside the GAAP one, the
adjustments few, reconciled and two-sided (Q4); (ii) dividend guidance. The guidance record is the test of "the promises
they make" **[M2004-067]**: in September 2021 Fortis "reaffirmed its targeted average annual dividend growth of
approximately 6% through 2025" (FY2021 MD&A, `0001666175-22-000019`); a year later the target was "approximately 4-6%
through 2027" (FY2022 MD&A), and the increases actually paid were 5.6%, 4.4%, 4.2% and 4.1% in 2022 to 2025. The promise
was lowered in public and the payout was not stretched to keep it; the payout ratio fell from 78% (2022) to 70% (2025).
That is the opposite of making the number, though a guided figure remains a habit the rows dislike **[L2019-006]**. One
small change in the headline: the "Actual Payout Ratio" of 2021 to 2023 became the "Adjusted Payout Ratio" in 2024 and
2025, with the actual three-year average still given beside it (FY2024 and FY2025 MD&As). (iii) EPS targets beaten for
pay: the 2025 EPS of C$3.40 was adjusted to C$3.46 for the bonus, a 150% payout against a C$3.42 target (circular p.53),
weighed at Q6, Part B, as pay; as integrity it is disclosed to the cent, with the one adjustment that cut against the
managers (C$50 million of exchange gain removed) shown beside the two that helped them.

**4. Mistakes, and acting on them** **[M1998-039]**, **[M2017-007]**. The billing-system failure appears in every MD&A from
FY2022 to Q2 2024 in the regulator's terms, with the third-party verification and the costs written off; the explosion in
the FY2024 and FY2025 MD&As and the statements' contingency note. They are reported as facts and proceedings, not in the
first person; the word "mistake" does not occur in the eight MD&As or the circular read (text search). The rows are "nervous" where such
words are taboo **[L2024-003]**; here the bad news is told, without the confession. Action followed: an interim agreement
with the PSC in July 2023, monthly meter reading accelerated (FY2023 MD&A), and the order closing the investigation in
June 2024 (Q2 2024 MD&A).

**5. Love of the business or of the money** **[M2000-098]**. A career inside the utilities he now runs, a holding of
twice the required multiple, and no other public directorship (circular p.17) point to the business; nothing in the record
read points to the money first. The rows concede this is read only from evidence of behaviour over time
**[M1998-166]**, **[M1998-168]**.

**6. The tells of dishonesty** (Q5's list). Too good to be true: no. Reports that dance: no; the adjusted figures are
reconciled. A management fixed on its stock price: the pay plan carries relative TSR at 45% of the PSU, a stock-price
measure, but the documents read do not dwell on the share price. Serial issuance **[L2014-015]**: shares are issued every
year (466.8 million at end-2020 to 515.3 million now), chiefly through the dividend reinvestment plan at the holders'
election, about 1.5% a year; carried to Q6, Part A, where the framework places it.

- **VERDICT on integrity: IN.** No doubt of the kind that closes the file **[M2013-088]**: the accounts are plain, the
  failures are disclosed and acted on, the one broken promise (dividend growth) was cut in public rather than met by
  stretching. **Ability WEIGHS FOR, lightly**: the record is the hand played about as dealt, with two operational failures
  at Central Hudson; in a business of allowed returns "If you have a big enough moat, you don’t need as much management"
  **[M1999-106]**, and "we still look to the underlying business, though" **[M1996-037]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The use the money goes to.** Almost all of it goes back into the utilities, the first use the rows name: "A company's
  management should first examine reinvestment possibilities offered by its current business" **[L2012-011]**. The
  spending is largely obliged (the duty to serve, Q3) and earns the allowed return. No acquisition was made in 2021 to
  2025; two sets of small businesses were sold (Aitken Creek gas storage, C$454 million in 2023; FortisTCI and the Belize
  businesses, C$479 million in 2025, with a C$63 million loss; statements of cash flows and MD&A 2025 p.10).
- **The retention test** **[M1994-061]**, **[R1995-009]**, over five years, "three or four" in **[M1998-110]**. Kept and
  put in over 2021 to 2025: retained earnings C$3,210M to C$4,969M (+C$1,759M) and paid-in common capital C$13,819M to
  C$16,112M (+C$2,293M, most of it dividends reinvested through the DRIP), together C$4,052M. Market value of the common:
  466.8M shares at C$52.00 (TSX close 2020-12-31, aggregator, flagged) = C$24,274M; 507.3M at C$71.36 (2025-12-31) =
  C$36,201M; +C$11,927M, about three dollars of market value per dollar kept or put in. The market leg passes. The
  intrinsic leg, which the rows require beside it because the market leg alone misleads **[R2009-002]**: *written back at
  Q7:* at the 4.19% government rate the growth case is worth more than the no-growth case (C$97.93 against C$72.41), so the
  dollars retained add value at the yardstick rate; at the ten percent floor the growth case is worth less (C$27.59 against
  C$30.34), so they earn less than the owner's minimum. The leg passes at the yardstick and fails at the floor.
  The forward question, "Can you keep using all of the capital you generate, effectively, for a very long time?"
  **[M2010-097]**: yes in amount (the business uses more than it generates); at what return is Q3's answer, the allowed
  one, which the rows call decent **[L2009-012]**.
- **Buybacks.** None in the window; none announced. The test is idle here, and the bottom of Q7's range is written back
  below for the record **[L1999-023]**. *Written back at Q7 (committed with Q7):* the bottom of the range is **C$72.41** a
  share (equity-only, central, at the 4.19% sovereign); there are no purchases to read against it.
- **Issuance and deals.** Value given against value got is the rule for every issue **[R1995-010]**, **[M1996-013]**. Fortis
  issues common shares every year: 8.7 million for C$481 million in 2024 and 8.0 million for C$523 million in 2025, about
  C$55 and C$65 a share, nearly all through the DRIP (MD&A 2025, Common Equity Financing), and 4.4 million more for about
  C$331 million from July to early September 2026 (Step 0). Whether these prices were above or below value is written back
  at Q7. *Written back at Q7:* the 2024 and 2025 issues, at about C$55.29 and C$65.38, were below the bottom of the range
  (C$72.41), so shares were issued beneath the value computed at the government rate, which harms the continuing owners
  **[M1996-013]**; the 2026 issues, at about C$75.83, sat inside the range. At the owner's floor every issue was well above
  value (fair C$28.96). Serial issuance **[L2014-015]** is the candidate second STOP the framework leaves unresolved (section VI); read here
  as a weighing, because the issue is small (about 1.5% a year), made at the holders' own election through the DRIP rather
  than sold by the company in the market, and funds a build the regulator obliges and pays a return on; that is not
  "hell-bent on issuing shares" **[L2014-015]**. The all-stock deal STOP **[L2009-019]**: not engaged; no business was bought in the window,
  for stock or for cash.
- **Dividends.** A dividend is right where a company "expects to regularly earn more than it can profitably employ in its
  business" **[M2004-089]**. Fortis does the reverse: owner cash after all spending was negative in each of the five years
  (Q3), yet C$1,249 million of dividends were paid in 2025, about 37% of them taken back in new shares under the DRIP
  (C$461 million non-cash; MD&A 2025). The company pays out with one hand and borrows and issues with the other. The policy
  is at least "clear, consistent" **[L2012-015]**: 52 years of increases and a stated growth range. It is guided as a
  growth rate and reported as a payout ratio, the kind of fixed formula the rows call "nuts" **[M2000-051]**.
- **Part A WEIGHS AGAINST, lightly.** The money goes where the rows say it should go first, into the business, at the
  return a regulator allows; but a dividend paid from borrowing and new shares inverts the rows' test **[M2004-089]**, and
  the shares are issued every year at prices that Q7 must judge **[M1996-013]**.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**, **[L1996-018]**. The annual incentive is 90% corporate (EPS 50%,
  FFO to debt 10%, sustainability and people 40%) and 10% individual; the PSUs vest on cumulative EPS and relative TSR (45%
  each) and a climate measure (10%) (circular, 2025 executive compensation and the 2026 changes). "EPS is the key financial performance measure used in our annual
  incentive and long-term PSU awards" (circular, chair of the human resources committee). EPS in a regulated utility grows
  with rate base, so a plan built on EPS pays for capital deployed with no charge for the capital; the rows want "a factor in
  the compensation arrangement that includes a capital cost element" in a capital-intensive business **[M2009-081]**,
  **[L1994-019]**. The 2025 bonus EPS was set at a target of C$3.42 (minimum C$3.36, maximum C$3.49); reported EPS was C$3.40,
  between minimum and target; the committee removed the C$63 million loss on the dispositions and added back their C$17
  million post-close dilution (both decisions management made) and removed C$50 million of exchange gain (not under their
  control), for C$3.46 and a 150% payout (circular p.53). The exchange adjustment is the rows' principle applied; the
  disposition adjustments pay the managers as if their own decision had not cost anything. The 2023 PSUs vested at 170.6%.
- **"Heads I win, tails you lose"** **[L1994-020]**. Incentives pay zero below the minimum and are capped at 200%; a
  clawback applies; the PSUs can be cancelled if the S&P rating falls below BBB (circular, compensation design). That is a partner in both
  directions on the incentive half.
- **Who sets it** **[M2012-095]**, **[L2005-015]**. "We target executive pay at approximately the median of the market"
  against a comparator group, advised by Southlea, with WTW supplying market data; the subsidiaries paid about $2.96
  million more to the same and other consultants in 2025 (the circular's figures, summed). That is the comparative-data machine the rows name
  "ratchet, ratchet, and bingo" **[M2012-095]**. The compensation part of the circular runs from p.41 to p.85; "If you take 100
  pages to explain how you’re paying the people of the place, something is wrong." **[M2009-087]**: this is not 100, but it is
  long.
- **The board** **[M2007-120]**, **[L2014-026]**. An independent chair separate from the CEO; 11 of 12 nominees
  independent; directors elected individually with majority voting (circular). The directors' own holdings are mostly DSUs
  received as fees: common shares of 0 to 11,248 per director against DSUs of up to 37,763, the DSUs above three times the
  shares for eight of the twelve (circular, director equity table, 2026-03-20); the rows feel better where directors bought "with their savings, rather than simply having been the recipients
  of grants" **[L2019-008]**.
- **Owners as partners.** Candid reports (Q5); no EPS guidance, but dividend and rate-base guidance **[L2019-006]**; one
  class of common shares with equal votes; an annual say-on-pay vote (94.19% for in 2025).
- **Part B WEIGHS AGAINST, lightly.** The structure is sound (independent chair, caps, clawback, ownership well above the
  requirement), but the pay runs on EPS with no capital charge in the most capital-hungry of businesses **[M2009-081]**,
  is set by peer comparison **[M2012-095]**, and was lifted in 2025 by excluding the cost of a decision management made
  **[M2003-019]**. The rows rank this below the person: "any compensation sins are generally of minor importance compared
  to the sin of having somebody that’s mediocre running a huge company" **[M2007-006]**.

- **Q6 WEIGHS AGAINST, lightly**, both parts; no STOP engaged.

## Q7: WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
and the business gets "credit for whatever net cash is left every year" **[M1998-080]**, the fourth question being "are
you going to have to put more cash into after you buy it?" **[M2014-068]**. Arithmetic in
`Test Runs/_research 2026-10-23 FTS/scripts/q7.py`, output `Test Runs/_research 2026-10-23 FTS/q7_out.txt` (C$ millions
unless per share). The script written before the kill was checked against the Q7 text on resume and changed in three
places, each now in the script: (1) the debt credited is long-term debt only, as the regulated-utility paragraph says ("the
long-term debt raised over the window"): issues less repayments plus committed credit-facility borrowings, which the filer
classes as long-term (Note 14), and not the borrowings of three months or less (C$328M over the window); (2) businesses
sold are netted against the spending, as specific (c) requires ("Cash paid for businesses, net of businesses sold, is
capital spending"); (3) the cap test in (f) reads the highest share of sales over all ten years transcribed, not five.

**The rate.** 4.19%, the Government of Canada long-term benchmark bond, Bank of Canada, 2026-10-21 (Step 0): the long
government rate of the earnings currency. The rows use the long government bond as the yardstick **[L2000-021]**,
**[M1996-025]**, and operator rule 5 names the earnings currency.

**The basis.** The deciding part (Q2) is ITC, a FERC formula-rate transmission utility, and every other part is regulated;
the regulated-utility paragraph therefore puts the equity-only basis central, "the fixed-asset commitments at our
regulated utilities" being the row's own exception to the all-equity rule **[L2017-012]**, since "when you get an allowed
return in the electric utility you’re almost certain of earning it" **[M2010-037]**. The all-equity figure is shown beside
and does not decide. Owner cash on the equity-only basis: cash from operations (after interest, after the company's own
tax, after all compensation **[L2021-003]**, with working capital counted, specific (d)), less preference dividends and
dividends to the ITC minority. The debt credit: the allowed debt share is 49.3%, the rate-base-weighted complement of the
equity ratios in Note 2 (ITC 60%, TEP 54.3% for all of UNS Energy, Central Hudson 48%, FortisBC Energy 45%, FortisAlberta
37%, FortisBC Electric 41%), weighted by each utility's 2025 midyear rate base (MD&A 2025, Capital Plan). **CONVENTION of
this run:** Other Electric is taken at 42% equity, between Newfoundland Power's 45% and the 40% of Maritime Electric and
FortisOntario, Caribbean Utilities having none stated; rationale: the filer gives that segment's rate base only as one
figure (C$3.4B), and a point either way moves the 49.3% by under a tenth of a point. The consolidated debt share
the filer itself reports is higher, 57.0% (MD&A p.17); the difference is holding-company debt, which gets no credit.
Long-term debt raised 2021 to 2025: C$8,272M.

**The six specifics, in order.**
- (e) **Maintenance central.** The filing gives no maintenance figure; the guess **[M2000-144]**, **[L1999-024]** is
  depreciation: rate base, the regulator's measure of the plant, stands still when spending equals depreciation, and the
  regulator recovers depreciation in rates. Maintenance-case owner cash (operating cash less depreciation, preference and
  minority dividends): C$1,281M, 1,276, 1,622, 1,771, 1,866; average **C$1,563M**. Growth spending (spending above
  depreciation) C$13,893M over five years; the debt credit is capped at 49.3% of it, C$6,846M (all of it within the
  C$8,272M raised); the C$933M of businesses sold is netted (c); the equity-funded growth spending left is **C$1,223M a
  year**, charged against the growth it buys, growing with it and stopping after year ten. The all-spending case is beside.
- (a) **Cycle or aberration.** The maintenance series has no end year the filer describes as aberrational. The
  all-spending series does: 2025 spending is net of C$775M of contributions in aid of construction, chiefly for FortisBC
  Energy's Eagle Mountain pipeline ("largely funded by CIACs", MD&A 2025, Capital Expenditures), and 2023 and 2025 carry
  the sale proceeds; so its growth rate is not used (below).
- (b) **Decline.** The central series grew; not engaged.
- (c) **Acquisitions.** None in the window; the sales netted as above. Shown beside: the growth case without netting them
  (C$93.82 a share; fair C$27.44).
- (d) **Working capital.** Inside operating cash.
- (f) **The cap.** Shown growth of maintenance-case owner cash 9.86% a year (2021 to 2025). Carried ten years it would need
  owner cash of 17.5% of sales, above the highest share earned in the ten years transcribed (16.9%, 2017); so the growth
  carried is the business's own sales growth, **6.53%** a year (revenue 2021 to 2025), the cut written down as required.
  No growth after year ten, computed as zero nominal growth.

**The range (equity-only, central), at 4.19%, per share on 515.27M shares:**

| case | value | return at C$80.99 |
|---|---|---|
| no growth, maintenance case | **C$72.41** | 3.75% (owner cash yield) |
| growth at 6.53% for ten years, equity-funded growth spending charged | **C$97.93** | 4.83% (the rate at which this case equals the price) |

Width 1.35 to 1. The price, C$80.99, sits inside the range.

**The floor, tested first.** About ten percent, after the company's own tax, on the equity **[M2003-149]**; for a utility
the floor is unchanged and earned on the equity (Q7, The regulated utility). No case earns it at the price: the central
cases return 3.75% and 4.83%. The bound that settles it beyond any choice of maintenance figure: charge **no capital
spending at all** and the five-year average operating cash after preference and minority dividends, C$3,349M, is worth
C$65.00 a share at ten percent with no growth, still below C$80.99 (a yield of 8.03% at the price). The no-growth owner
cash yield of 3.75% is also below the 4.19% the Government of Canada pays (a fact for Q8, not weighed).

**Beside, not deciding.**
- *All spending charged, debt credited (the PG specific's literal case).* Series C$321M, 796, 1,218, 272, 521; average
  C$626M; yield 1.50% at the price. Its end-to-end growth (12.87%) and its growth between the halves of the window
  (-10.79%, 2021-22 against 2024-25) point opposite ways because of the contributions and sale proceeds named in (a); the
  range is C$28.98 (no growth) with C$83.87 or C$11.83 as the other end; fair C$20.94 or C$9.10.
- *All spending, no debt credit (the literal window).* Owner cash negative every year (C$-323M to C$-1,697M); no value on
  this basis.
- *All-equity basis.* Owner cash before interest (maintenance case plus preference dividends plus interest paid after the
  effective tax rate), average C$2,661M, against the market value plus net debt and preference shares of C$37,233M (net
  debt C$35,610M pro forma 2026-06-30 after the September 2026 notes and the share and loan changes to 2026-09-04,
  prospectus supplement `0001104659-26-106675`; operating leases left out): range C$51.01 to C$83.25 a share at 4.19%;
  yield on enterprise value 3.37%.
- *Tax.* Cash taxes paid were small (C$-17M to C$129M a year, 2021 to 2025) because deferred taxes grew with the plant
  (C$3.3B to C$5.3B). This is tax depreciation running ahead, not a carryforward or credit that runs out, so the section E
  convention is not engaged; restating to a full tax rate could only lower every figure above.

**The screamer** **[M2009-005]**: not reached; the price is about 2.8 times the fair price below.

**Reporting figures (Part VII, The owner's price; a reporting convention, not a verdict).**
- **Value range: C$72.41 to C$97.93 a share** (equity-only, central, at the 4.19% sovereign) against **C$80.99**.
- **Fair price: C$28.96 a share** (equity-only, central): the no-growth case valued at ten percent, C$30.34, and the
  growth case valued at ten percent, C$27.59, averaged; owner cash after the company's own tax, no conversion; the debt
  raised for the fixed assets credited against their spending up to the allowed 49.3%. **All-equity beside: C$-27.12**,
  not positive (no-growth C$-20.61, growth C$-33.63, after C$37,233M of net debt and preference shares).
- At ten percent the growth case is worth less than the no-growth case: the added capital, earning the allowed return, is
  worth less than it costs to an owner who demands ten percent; "growth can destroy value" **[L2000-023]**.

- **VERDICT: OUT.** The price does not clear the floor on any case the analyst could defend, nor on the bound with no
  capital spending charged at all: "there’s just a point at which we drop out of the game" **[M2003-149]**. The rows
  expected this of a utility at a full price, "there’s no way we get rich on our utility investments" **[M2009-104]**; and
  "a reasonable price in relation to the bottom boundary of our estimate" **[L2013-012]** is not what C$80.99 is.

## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
Not answered: the file closed OUT at Q7 (operator rule 2). Facts found are under AFTER THE STOP.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
Not answered: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
Not answered: the file closed OUT at Q7.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked: the file closed at Q7, and the operator has not chosen it for this run.

---
## THE BOX
**OUT at Q7**: no case earns the floor of about ten percent at C$80.99. Value range C$72.41 to C$97.93 a share
(equity-only, central, at the 4.19% Government of Canada long rate) against C$80.99; fair price C$28.96 (equity-only,
central), all-equity beside C$-27.12. Q1 IN, Q2 IN, Q3 weighs undecided, Q4 weighs against lightly, Q5 integrity IN and
ability weighs for lightly, Q6 weighs against lightly.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down under the question each bears on, each with its source **[M1997-127]**; no verdict; the box unchanged.

**Q8, the alternatives.**
- The maintenance-case owner cash yields 3.75% at the price, below the 4.19% Government of Canada long benchmark bond
  (Bank of Canada, 2026-10-21); the all-spending owner cash after the debt credit yields 1.50% (Q7).

**Q9, the target's debt and exposures.**
- Total debt C$34.6B at 2025-12-31 (C$22.2B in 2016); consolidated capital structure 57.0% debt, 2.7% preference shares,
  40.3% common equity and minority interests (MD&A 2025 p.17). Net debt C$35,610M pro forma 2026-06-30 (prospectus
  supplement `0001104659-26-106675`).
- Earnings before interest and tax covered interest and preference dividend requirements 1.89 times (twelve months to
  2025-12-31) and 1.97 times (twelve months to 2026-06-30) (the same supplement, Earnings Coverage Ratios).
- Holding-company debt (Corporate and Other, Note 14 of the 2025 statements): U.S. senior notes C$2,073M, debentures C$200M,
  senior notes C$2,600M, subordinated notes C$750M (2055); then US$1.0B of junior subordinated notes due 2057 issued in
  September 2026 (supplement). The holding company has no revenue of its own; its debt is served from subsidiary dividends.
- Long-term debt principal due: C$3,146M (2026), C$2,389M, C$1,880M, C$943M, C$1,714M (2030), C$23,985M thereafter
  (MD&A 2025, Contractual Obligations). Credit facilities C$5,773M, C$3,741M unused at 2025-12-31, C$5.4B committed with
  maturities 2027 to 2030 (MD&A 2025).
- Ratings at 2025-12-31: S&P A- issuer, BBB+ unsecured, outlook moved from negative to stable in November 2025; Fitch
  BBB+ (first assigned May 2025); Morningstar DBRS A (low). "In January 2026, Moody’s Investor Services, Inc. withdrew its
  ratings for Fortis at the Corporation's request" (MD&A 2025, Capital Structure and Credit Ratings). The PSUs can be
  cancelled if the S&P rating is below BBB (circular).
- Physical risk: the MD&A names wildfire among "its most significant climate hazards"; S&P's outlook change cited
  "developments at the subsidiaries to mitigate physical risks, namely wildfires" (MD&A 2025).
- Central Hudson explosion (November 2023): civil actions pending; contingent liability US$105M at 2026-06-30 with an equal
  insurance receivable (Q2 2026 statements, `0001666175-26-000031`).
- Unrecorded purchase commitments C$13,287M, of which gas and fuel C$6,592M and the Waneta Expansion capacity agreement
  C$2,307M (2025 statements, Commitments and Contingencies).
- Diversity of the earning sources: ten utilities in five provinces, ten states and Grand Cayman, the largest (ITC) about
  30% of five-year segment earnings (Q2).

**Q10, the pitch.** Nothing beyond Q7: the price is about 2.8 times the fair price.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 06504e86); written question by question; committed after each
      (Step 0 to Q1 42aa5212, Q2 674b7cc0, Q3 86ef8b7a, Q4 107617f9 and 49175fd9, then on resume Q5 c807b43b, Q6 064e6624,
      Q7 with the Q6 write-backs 0be83d5c, the close in the last commit). One slip: the Q6 commit 064e6624 went in before
      five corrections to it had been applied (my fix script stopped on an assertion and the commit command ran after it);
      it carried a quotation from row L2014-015 beside the id of row L2009-019, three page
      references I could not confirm and a director-holdings range that was wrong at its low end. All five were corrected in
      0be83d5c; the citation check would have failed on the first.
- [ ] If dispatched: the brief allowed the per-question commits; the lock and the fold are the dispatching session's and
      were not checked by me. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. The contamination declared at the
      head of the file stands; the resumed session saw the same session context (the memory index, a git status naming
      the ARCB and AYI research folders) and nothing about Fortis; not used.
- [x] Every v5 id resolves (`Test Runs/_research 2026-10-23 FTS/scripts/check_ids.py`: no E-ids, every M/L/R id in the
      CSV, every quoted fragment standing before an id found in that row); every filing fact has its accession or names its
      document; numbers without a filing are labelled CONVENTION.
- [x] The order was kept; Q7 closed the run; nothing after it is a clearance; Q8 to Q10 not answered.
- [x] Owner cash from operating cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from
      the issuing authority (Bank of Canada, a CAD series the protocol's table does not list, named and dated); the
      aggregator prices flagged (Yahoo through `tools/sources.py`: the price of 2026-10-22 and the 2020 and 2025 year-end
      closes used in Q6's retention test).
- [x] Contrary evidence written down as found **[M1997-127]** (Step 0 list; Q5 and Q6 facts against); facts for later
      questions under AFTER THE STOP. No integrity facts are open, since Q5 was answered (IN).
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used; it printed UNRESEARCHED and no figure of it was used.
- [x] `python tools/check_framework.py` PASS before each commit of this session.
- Honest limits: the maintenance figure is a guess at depreciation; the result does not turn on it (the bound with no
  spending at all is still below the price). The allowed debt share for Other Electric is a CONVENTION. The minority's
  claim on ITC is charged by its dividends, not its share of ITC's cash. Segment earnings for Q2 come from the MD&As, not
  the audited segment note. The DRIP issue prices are averages (amount over shares), not per-issue prices.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The regulated utility's debt credit against the maintenance case.** The paragraph credits "the long-term debt raised
   over the window" against "the capital spending it funded", and specific (e) puts the maintenance case central. Neither
   says how the two meet: whether the credit is set against all spending (then the all-spending case) or only against the
   growth spending (spending above maintenance) that the central case charges. I credited it against growth spending
   only, capped at the allowed share of that, on the reading that depreciation is recovered in rates and the debt funds the
   additions to rate base; the literal all-spending case is beside. The paragraph should say which.
2. **"Long-term debt raised".** Not defined: whether committed credit-facility borrowings that the filer classes as
   long-term count, and whether the short borrowings do. I counted the first and not the second; the difference here was
   C$328M and moved nothing.
3. **The allowed debt share of a holding company of many utilities.** "the debt share of the capital structure the
   regulator allows as the filing states it" assumes one regulator. Fortis has eleven allowed equity ratios; I weighted
   them by midyear rate base and confessed a figure for the segment the filer reports as one. The text should name the
   weighting.
4. **The sovereign for a Canadian-dollar business.** The protocol's table lists USD, JPY and EUR only; the rows name "long-term
   U.S. bonds". I used the Bank of Canada's long benchmark under operator rule 5's earnings-currency clause. A CAD row
   (series `BD.CDN.LONG.DQ.YLD`) would settle it.
5. **A consolidated subsidiary with a minority.** Owner cash from consolidated operating cash includes all of ITC's cash;
   the framework does not say whether to deduct the minority's dividends or its share of earnings. I deducted dividends,
   which overstates owner cash by the minority's retained share (C$61M a year on average, earnings over dividends); the
   verdict does not turn on it.
6. **Specific (c) for a seller.** Netting "businesses sold" against spending raises owner cash in the window while the sold
   businesses' cash leaves the future; for a business that sells and does not buy, the text gives no correction. I netted
   as written and showed the figure without netting beside.
7. **The retention test's intrinsic leg has no rate.** Q6 asks whether retention added intrinsic value, and the answer here
   is yes at the government rate and no at the ten percent floor; the text does not say which governs. I wrote both.
8. **Serial issuance through a dividend reinvestment plan.** The candidate second STOP **[L2014-015]** is unresolved in
   section VI, and the text does not separate shares sold by the company from dividends reinvested at the holders'
   election. I weighed it and said why.
9. **The template's Q5 heading** reads "able, honest, in love with the business, the same after being paid", while the
   framework's Q5 test of the after-the-sale question applies to whole businesses only; for a part-interest the heading
   asks a question the section says is not asked. Kept as the template has it.
