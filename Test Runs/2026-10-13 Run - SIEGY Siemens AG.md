# Company Run — Siemens AG (Xetra: SIE; US OTC ADS: SIEGY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (Siemens files no
SEC report, so the document and its date stand in place of an accession, as the brief directs). A STOP that returns OUT
or TOO HARD closes the run and later questions are marked NOT REACHED. Copied to its dated name before any fetch
(commit 042c16a1).

**Dispatched blind run.** The brief's two stated departures from the canonical brief: the lines of evidence and the
competitors were derived by the analyst from the company's own reports, and the primary documents are the company's own
annual reports and quarterly statements (no SEC filings).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session
fills it at the fold. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (SIEGY; also searched for Siemens and SIE); not held.*

**Contamination declared.** Seen without searching, and not used: the recent commit subjects in the session's opening
git status (the SQFT run of 2026-10-13 and its fold), and the untracked file names in that status (research folders of
other names, daily digests, MBA coursework files). The directory listing of `Screens/_daily/` (read to confirm the lock
file was present) showed file names only. A memory index line seen in the session context names counts of
"gate-clearers" without naming this company. Nothing of any of them bears on this name.

**Lines of evidence chosen, and why.** From the Siemens Report for fiscal 2025's organization and segment sections
(chapter 1 and 3), its risk report (8.3), its results discussion (4 to 6), Note 22 (legal proceedings) and the
Compensation Report: (1) the parts and their margins over a cycle, FY2016 to FY2025 and the nine months of FY2026,
because Q2 closes on the deciding part; (2) customers and suppliers, from the segment descriptions; (3) pricing through
the 2022 to 2023 inflation, from the FY2022 and FY2023 reports; (4) acquisitions and goodwill (Mentor Graphics 2017,
Varian 2021, Altair and Dotmatics 2025) against what they earned; (5) debt, the SFS lending book, pensions and lease
liabilities; (6) buybacks and their prices, from the company's own buyback pages; (7) stock pay, from Notes 19 and 26;
(8) litigation and investigations, from Note 22 and the half-year report's Note 7. Chosen because each is a place the
report itself says the risk or the money lies.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** EUR 272.10, Xetra close 2026-10-09 (Yahoo Finance chart for SIE.DE, exchange "GER"; **AGGREGATOR, live quote
  only, flagged** per operator rule 5). No close is printed for 2026-10-12; the intraday quote of 2026-10-13 was EUR 278.15
  and is not used. Cross-check from the company: the 15th interim buyback report (Siemens AG, 12 October 2026) gives a
  Xetra weighted average purchase price of EUR 271.05455 on 09/10/2026. ADS: USD 153.36, OTC close 2026-10-12 (same
  aggregator, flagged); EUR/USD 1.1187 (same aggregator, flagged).
- **The ADS ratio, established:** one ADS represents one-half of one ordinary share. Source: Amendment No. 2 to the Deposit
  Agreement (Deutsche Bank Trust Company Americas, depositary), Exhibit 99.(a)(3) to the Form F-6 POS filed with the SEC on
  2017-03-08, accession 0001193805-17-000417 (Section 2.02: "replacing "one Share" with "one-half of one Share""). The
  company's EDGAR file (CIK 1135644) shows no later F-6 amendment as of 2026-10-13. Check: 2 x USD 153.36 / 1.1187 =
  EUR 274.2 a share, against EUR 272.10; the ratio holds.
- **The Healthineers spin-off, established: it has not taken place.** Siemens press release of April 17, 2026
  (HQCOPR202604177384EN): "Siemens plans a shareholder vote on direct spin-off of Siemens Healthineers shares at the next
  ordinary Siemens Annual General Meeting in February 2027." The Q3 FY2026 Earnings Release (August 6, 2026) quotes the CFO:
  "we've now received binding decisions from the tax authorities clarifying the relevant tax topics. As a result, we can
  proceed with the spin-off of Siemens Healthineers as planned." The Half-year Financial Report (May 4, 2026), Note 2:
  Siemens sold 2% of Healthineers for EUR 1,101 million and "subsequently holds 67%". The run therefore values Siemens with
  Healthineers consolidated and its minority deducted; the spin-off is a future event, not valued.
- **Shares** (no SEC cover page; `Screens/cover_shares.py` and `tools/run.py` read SEC data and do not serve this name; the
  arithmetic is done from the reports, as the brief directs). Siemens Report FY2025, Note 19: 800,000,000 issued, 19,735,802
  in treasury at Sep 30, 2025 = 780,264,198 outstanding. Half-year Financial Report FY2026, Note 5: 7,338 thousand
  repurchased and 3,534 thousand transferred in the six months to March 31, 2026; 18 million cancelled in March 2026,
  "which reduced issued capital to 782 million shares". Treasury at Mar 31, 2026 = 19,736 + 7,338 - 3,534 - 18,000 =
  5,540 thousand; outstanding 776.46 million. Q3 FY2026 purchases under the 2024-2026 programme (company buyback page,
  monthly table): April 2,555,416, May 684,599, June 613,442 = 3,853,457. Purchases under the 2026 programme from 1 July to
  11 October 2026: 4,497,911 (15th interim report, 12 October 2026). Outstanding = 776.46 - 3.85 - 4.50 = **768.1 million**
  (CONVENTION of this run: transfers to employees after March 31, 2026 are not published by count and are left out, which
  understates the count by perhaps one to two million shares, under 0.3%; rationale: the alternative is a number the
  filings do not state). Check against the Q3 FY2026 statement: weighted average basic shares for the quarter 774,050
  thousand, consistent with a count falling from 776.5 to about 772.6 million across the quarter.
- **Market cap:** 768.1 million x EUR 272.10 = **EUR 209,000 million** (ADS equivalent: 1,536.2 million ADS at USD 153.36).
- **Sovereign for the earnings currency (EUR):** **3.78%**, ECB euro area AAA yield curve, 30-year spot rate
  (YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), observation 2026-10-09, issuing authority, via `python tools/sources.py`.
- **Filings read** (operator rule 4), in place of accessions: Siemens Report for fiscal 2025 (fiscal year ended Sep 30,
  2025; Managing Board responsibility statement dated Munich, December 1, 2025; downloaded from the address in the brief);
  the Annual Reports for FY2016 to FY2024 (siemens-ar2016 to Siemens-Annual-Report-2024, company IR site), for ten years of
  balance sheets; the Half-year Financial Report for the first half of FY2026 (dated Munich, May 4, 2026); the Q3 FY2026
  Earnings Release and Financial Results (Quarterly Statement, August 6, 2026); press release April 17, 2026; the share
  buyback pages (2024-2026 programme, final; 2026 programme to 11 October 2026). The Compensation Report and the Report of
  the Supervisory Board are inside the FY2025 Siemens Report and stand in place of a proxy. Raw PDFs and text dumps are in
  `Test Runs/_research 2026-10-13 SIEGY/cache/` (gitignored).
- **One figure cross-checked against the filed statement:** Free cash flow, continuing operations, FY2025, EUR 11,004
  million (Five-Year Summary and Note 29) = Cash flows from operating activities, continuing operations, 13,448 less
  Additions to intangible assets and property, plant and equipment 2,445 = 11,003 (Consolidated Statements of Cash
  Flows); agrees to rounding.
- **Arithmetic lines** (by hand from the filed statements, script `q7_calc.py` in the research folder; EUR million):

| FY | FCF, continuing ops | stock pay (Note 19/20) | NCI share of net income | owner cash (all-equity basis) | interest paid | owner cash after interest |
|---|---|---|---|---|---|---|
| 2021 | 8,379 | 294 | 537 | 7,548 | 704 | 6,844 |
| 2022 | 8,304 | 376 | 669 | 7,259 | 824 | 6,435 |
| 2023 | 10,146 | 444 | 579 | 9,123 | 1,208 | 7,915 |
| 2024 | 9,726 | 530 | 691 | 8,505 | 1,462 | 7,043 |
| 2025 | 11,004 | 535 | 767 | 9,702 | 1,733 | 7,969 |
| **avg** | 9,512 | 436 | 649 | **8,427** | 1,186 | **7,241** |

  Free cash flow is the company's own: operating cash flow (after tax paid, after working capital, before interest paid,
  including interest and dividends received) less all additions to intangibles and property, plant and equipment.
  FY2022 to FY2025 are the restated continuing figures of the FY2025 Five-Year Summary (Innomotics out); FY2021 is as filed
  in the FY2021 report (Innomotics in; no restatement of FY2021 is published). Capex against depreciation: additions
  2,445 against amortization, depreciation and impairments 3,389 less amortization of intangibles acquired in business
  combinations 819 = 2,570 in FY2025, so the depreciation variant would lower owner cash by about 125 million; the filing
  states no maintenance figure. Two CONVENTIONS of this run, confessed: (1) stock pay is deducted at the expense the
  company credits to capital reserve (equity-settled awards), since free cash flow leaves it out and the rows count "all
  forms of compensation" **[L2021-003]**; (2) the minority's claim (chiefly about a third of Siemens Healthineers) is deducted
  as the year's net income attributable to non-controlling interests, because Siemens owns only its share of that cash;
  rationale: the filing gives no attributable cash figure and the earnings figure is the minority's stated claim.

## THE FOUNDATIONS (not a gate)
The foundations that bear on this name are three. A share is a business: the test is whether one would be "happy buying
this stock if the market closed for five years" **[M1997-109]**; Siemens is a group of four operating businesses and a
lender, and the run reads it as such. The market serves: the price of EUR 272.10 instructs nothing, it "just tells us
prices" **[M2006-077]**; the price has roughly doubled since September 2021 (EUR 141.92, aggregator, flagged), which is no
reason to buy. Margin of safety: "if you have to actually do it on [...] with pencil and paper, it's too close to think
about" **[M1996-084]**; a group of this size and complexity cannot be valued without a pencil, which already says something.
No macro forecast enters: the FY2025 report's tariff and China commentary is read only as evidence about the businesses.
Who is paid to tell you: the company's own "EPS pre PPA" and its guidance are read as the seller's figures (Q4, Q5).

**Contrary evidence, written down as found** **[M1997-127]**: (1) the risk report (8.3, "Digital transformation") says
"There are risks associated with technologies such as artificial intelligence, including generative artificial
intelligence, that domain expertise will not be a significant distinguishing feature in the future, and that additional
competitors may therefore emerge more easily or rapidly"; this is the company's own statement against the deciding part's
moat. (2) Digital Industries' profit margin fell from 22.6% (FY2023) to 14.9% (FY2025), with price pressure in China that
"intensified again after the announcement of the U.S. tariffs" (FY2025 report, 3.2). (3) Acquisitions of businesses,
net of cash acquired, were EUR 31.7 billion over FY2021 to FY2025 (Varian 14.4, FY2022 2.2, FY2023 0.4, FY2024 0.4,
Altair and Dotmatics 14.2), more than half of owner cash even after disposals are netted: the group buys a large part of
its growth. (4) The competitive-environment risk names "rising competitors from emerging markets and new industries, which
may have a better cost structure". (5) Treasury interest and the SFS lending book sit inside the reported free cash flow
and its net debt, which makes the all-equity basis harder to state cleanly than for a pure industrial (Q7).

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase would be bought with owned money, unlevered, and sized so that a fall of
half "or more" leaves the buyer "comfortable" **[M2020-022]**; on those terms owning it does not risk "what we have and
need for what we don't have and don't need" **[M2012-081]**. Nothing in Siemens' structure (a quoted equity, no calls on
the holder) puts a demand for sudden sums on the buyer **[L2014-024]**. Passes as conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **Read by its parts** (Q1, A holding company, and Q2, A business of parts: a part "matters" when it decides, more than
  half of five-year operating profit or else the largest). Segment Profit, FY2021 to FY2025, as filed in each year's Note
  29 (FY2021 from the FY2021 report, FY2022 and FY2023 from the FY2023 report, FY2024 and FY2025 from the FY2025 report;
  EUR million):

| part | FY21 | FY22 | FY23 | FY24 | FY25 | five-year | share of Industrial Business |
|---|---|---|---|---|---|---|---|
| Digital Industries | 3,362 | 3,892 | 4,947 | 3,498 | 2,643 | 18,342 | 34% |
| Siemens Healthineers (67% to 79% owned) | 2,847 | 3,369 | 2,527 | 3,172 | 3,519 | 15,434 | 29% |
| Smart Infrastructure | 1,743 | 2,222 | 3,074 | 3,707 | 4,506 | 15,252 | 28% |
| Mobility | 857 | 794 | 882 | 1,013 | 1,099 | 4,645 | 9% |
| Industrial Business | 8,809 | 10,277 | 11,430 | 11,390 | 11,766 | 53,672 | 100% |

  No part carries more than half; **Digital Industries is the largest and decides** (34%). Siemens Financial Services
  (EBT 512, 498, 563, 637, 622) is a lender reported apart and is not an industrial part; it is read under the bank door
  below. Healthineers is counted at 100% here as filed; on Siemens' attributable share (about 67% to 79%) it is smaller,
  which does not change the order.
- **What Digital Industries is** (FY2025 report, 3.2): automation (factory automation, motion control, process automation:
  PLCs, drives, numerical controls, sensors) and software (PLM, electronic design automation, simulation including Altair
  from the second quarter of FY2025, life-science R&D software through Dotmatics from the fourth quarter). Software revenue
  EUR 6,174 million of 17,788 in FY2025 (35%). Customers: "the automotive industry, the machine-building industry, the
  pharmaceutical and chemicals industry, the food and beverage industry and the electronics and semiconductor industry",
  served through "a common regional sales organization" and distributors. The report says demand for standard products is
  "driven strongly by macroeconomic cycles and can lead to significant short-term fluctuation in Digital Industries'
  profitability".
- **The key variables and whether they are foreseeable** **[M1998-044]**: (a) automation volume through the cycle and the
  price it holds; (b) the margin of the software business as it moves to subscription and meets AI. The record of the
  margin over a full cycle is in the filings: Digital Factory 16.6% (FY2016) and 18.8% (FY2017); Digital Industries 18.6%
  (FY2018), 17.9% (FY2019), 21.7% (FY2020), 20.4% (FY2021), 19.9% (FY2022), 22.6% (FY2023), 18.9% (FY2024), 14.9% (FY2025,
  destocking plus EUR 356 million severance), 18.3% (nine months FY2026, Q3 FY2026 Financial Results). Ten years inside a
  band of about 15% to 23%, through a destocking cycle and an inflation, is a record from which the past statements tell
  "the information that's useful to me in making a judgment about what the future financial statements are going to look
  like" **[M2008-033]**. As to "how far off we can be" **[M2011-084]**: on the automation half, within that band; on the
  software half, wider.
- **Customers or technology** **[M2017-019]**, **[M2023-030]**: the automation half is a forecast about customers, the
  factories and machine builders who keep the controller their engineers are trained on; the software half is partly a
  forecast about technology (EDA and simulation under AI), which the company's own risk report flags (contrary evidence 1).
  The insiders do write down a mid-term figure: the FY2025 report states Digital Industries' margin range of 17 - 23%
  (Siemens Financial Framework, 2.2), which is evidence that this is not a forecast they "would not want to put down on
  paper" **[M2000-105]**, though it is the seller's figure and is read as such.
- **Doubt** **[M2002-092]**: I have a reasonable fix on what the automation half's "earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**; my fix on the software half is weaker. The software half is about a
  third of the deciding part, and its record (PLM and EDA held as an oligopoly through the decade read) has held. Judged
  inside, with the software half's change carried to Q2 test 11 and to the width of Q7's range. A second analyst could
  reasonably close here TOO HARD (NATURE) on the software half; the run records that it did not, and why.
- **The lender (bank door):** SFS has EUR 33.1 billion of total assets (FY2025, 3.6), "with the highest share in the U.S.",
  in "investment-grade countries", lending to equipment and project borrowers in Siemens' own markets. Both sides can be
  read from the filings at the level the report gives (assets in the segment note; funding through group debt, EUR 28.9
  billion of SFS debt in Note 20); it takes no deposits and the report names no derivatives book of its own that it calls
  unpredictable. It does not decide; the reading "we don't understand how much risk the institution is running"
  **[L2002-018]** is not reached for a book of this size inside a EUR 166 billion balance sheet, and the book is weighed
  at Q9.
- **Abroad** **[M2000-141]**: a German stock corporation with a two-tier board and employee co-determination, IFRS accounts
  in English, German tax; the governance and tax are knowable from the report.
- **VERDICT: IN** **[M1995-051]**, on the deciding part's ten-year record in the filings, with the software half's doubt
  written down and carried.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is asked of the deciding part, Digital Industries (Q1's parts table), "why is that castle still standing?"
**[M1995-038]**, with the other parts read briefly and carried.

- **The castle questions: what keeps it standing, and how permanent** **[M1995-038]**. The report names the reasons
  customers come in its own terms: a "comprehensive product portfolio" across automation and software, one sales
  organization, and an installed base (the risk report itself names the danger that "competitors may offer their services
  to our installed base", which says the base exists and is worth attacking). The automation half's reason is the trained
  engineer and the installed controller: a plant built on one automation system is reprogrammed, extended and serviced on it.
  The software half's reason is the design file and the workflow (PLM, EDA), which the FY2025 report says is moving to
  subscription. The permanence of the first is shown by a decade of margins (below); of the second, less so.
- **Would it stand without the lord?** The decade of margins spans two chief executives of the group and the 2020 spin-off
  of Siemens Energy; no superstar is named or needed in the filings.
- **The money test** **[M1997-103]**, **[M2011-015]**: an attacker with tens of billions would have to persuade the world's
  factories to re-engineer lines built on an existing controller standard and retrain their engineers. The filings show the
  attack being made on price, not on the standard: "In China, price pressure initially eased following the end of
  destocking but intensified again after the announcement of the U.S. tariffs" (FY2025, 3.2). The answer is "no" for the
  installed base in the West; it is less sure in China, where the attacker has the home market.
- **Pricing power, and the agony before a rise** **[M2005-020]**, **[M2005-017]**: through the 2022 to 2023 inflation the
  automation businesses raised prices and margins rose: FY2022 report (3.2), "The increases were supported by higher capacity
  utilization and pricing measures to offset cost inflation"; FY2023 outlook, "We expect improvements in productivity and
  adjusting prices for our own products, solutions and services to more than offset effects from wage increases and higher
  prices for raw materials and components"; Digital Industries' margin went 19.9% (FY2022) to 22.6% (FY2023). The
  passing-through of cost increases is the mark the rows give of "strong competitive positions" **[M2005-017]**. Against it:
  FY2025 "Growth in the U.S. automation market was primarily price-driven" while volume "remained on the prior-year level",
  and China price pressure; the price held in the West and was attacked in China.
- **Unit volume and share of mind; the brand; the low bid** **[M2016-006]**: no market-share figure is published in the
  filings read; the report's own claim of "leading" software offerings is the seller's. The customer buying a factory's
  control system does not "simply just take the low bid" **[M2016-006]** where a line's uptime rides on it; the distributor
  destocking of FY2024 to FY2025 shows the short-cycle product is bought through channels, where price competes.
- **The low-cost position** **[M2001-013]**: not claimed by the filer; the FY2025 severance (EUR 356 million, "capacity
  adjustments in the automation business") is a cost being cut, not a cost advantage shown.
- **Ask the competitors / the competitor row.** The filer's reports name its rivals in two places: the Compensation Reports'
  peer group for the Stock Awards (FY2021 report: ABB, GE, MHI, Rockwell, Schneider for the 2017 tranche; FY2023 report: ABB,
  Eaton, General Electric, Mitsubishi Heavy Industries, Schneider for the 2019 tranche) and the Mobility sections (FY2021
  report: Alstom, which "announced the closing of the acquisition of Bombardier Transportation", and Hitachi Rail; FY2019
  report: "a large Chinese competitor", unnamed). Three that file with the SEC are read from their own 10-Ks (header
  User-Agent as the brief directs; XBRL transcription with the filed statement cross-checked for Rockwell FY2025, total sales
  USD 8,342 million and total segment operating earnings 1,703 in the 10-K text): **Rockwell Automation** for Digital
  Industries (10-K FY2025, accession 0001024478-25-000116; FY2022, 0001024478-22-000093; FY2019, 0001024478-19-000044;
  FY2017, 0001024478-17-000034), **Eaton** for Smart Infrastructure (10-K FY2025, 0001551182-26-000007), and **GE
  HealthCare** for Siemens Healthineers (10-K FY2025, 0001932393-26-000007; flagged: the reports name "General Electric",
  whose healthcare business was spun off as GE HealthCare in January 2023, so its record before 2021 is not in its own
  filings). Named rivals that do not file with the SEC and were not read: ABB (deregistered), Schneider Electric,
  Mitsubishi Heavy Industries, Alstom, Hitachi, and the unnamed Chinese rail competitor.

| year (FY) | Digital Industries profit margin (Siemens, segment Profit, before acquired-intangible amortization) | Rockwell total segment operating margin (same basis: excludes purchase accounting amortization) |
|---|---|---|
| 2016 | 16.6% (Digital Factory only) | 20.2% |
| 2017 | 18.8% (Digital Factory only) | 19.5% |
| 2018 | 18.6% | 21.6% |
| 2019 | 17.9% | 22.0% |
| 2020 | 21.7% | 19.9% |
| 2021 | 20.4% | 19.9% |
| 2022 | 19.9% | 19.9% |
| 2023 | 22.6% | 21.3% |
| 2024 | 18.9% | 19.3% |
| 2025 | 14.9% | 20.4% |

  Over the decade the two sit in the same band (Siemens about 19% average, Rockwell about 20%); Siemens fell further in the
  FY2025 trough and has recovered to 18.3% in the nine months of FY2026. Returns on capital: Digital Industries' segment
  assets (net capital employed, which includes the acquired goodwill) were EUR 10,123 million (FY2021), 10,861 (FY2022),
  10,946 (FY2023), 10,476 (FY2024) against Profit of 3,362, 3,892, 4,947, 3,498, which is 31% to 45% pre-tax on capital
  including goodwill; then 22,885 at Sep 30, 2025 after Altair and Dotmatics, against 2,643 (12%). Rockwell's tangible
  equity has been negative since FY2019 (XBRL, StockholdersEquity less Goodwill and intangibles), so its return on tangible
  capital is very high. Other parts, same metric where comparable: Smart Infrastructure 9.1% (FY2020) rising to 19.6%
  (FY2025) against Eaton's pre-tax margin 9.8% (2020) rising to 18.0% (2025); Siemens Healthineers 11.7% (FY2023) to 15.1%
  (FY2025) against GE HealthCare's operating margin 12.5% (2023) to 13.4% (2025).
- **The field's returns over the last full cycle, judged in words**: the field is not ordinary. Both the deciding part and its
  named SEC-filing rival earned high pre-tax margins through FY2016 to FY2025, a decade that holds a pandemic, an inflation
  and a destocking, and high returns on the capital the businesses need. The "standing castle that protects only ordinary
  returns" exit does not apply **[L2007-004]**.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: mixed. The Western price held through the inflation; FY2025 shows
  a notch lost against Rockwell and in China; nine months of FY2026 show recovery (Q3 FY2026: Digital Industries profit
  margin 18.7%, "Higher volume, profit, and profitability in both the automation business and the software business").
  The rows sort a bad year by whether the position held: "a cyclical problem, not a secular one" **[L1995-022]**; the evidence of the next downturn will say more.
- **What could destroy, modify or reduce it** **[M2000-014]**: (1) AI making domain expertise "not [...] a significant
  distinguishing feature" (the company's own risk report); (2) Chinese automation rivals with "a better cost structure"
  moving from their home market outward; (3) software-defined automation reducing the value of the proprietary controller.
  None is shown happening in the filings beyond the China price pressure; each is a slow threat of the kind the rows warn
  "can lull you to sleep" **[M2014-038]**. The automation half is not "prone to rapid and continuous change" on the
  decade's evidence **[L2007-005]**; the software half is closer to it, and is carried as the main reason Q7's range is wide.
- **The parts table** (section B): Digital Industries decides (34%); its castle stands on the evidence. Non-deciding parts,
  carried: Smart Infrastructure (28%), a castle whose margin has risen for five years; under the "change for the better"
  paragraph the rise is credited only on a full cycle, and it does not decide, so it is carried at the figures filed.
  Healthineers (29%), whose imaging competition the report describes as "a small number of large multinational companies", steadier, with a China
  diagnostics weakness the Q3 FY2026 release calls "a structural change in the market environment in China". Mobility (9%),
  project business with margins of 8% to 9% but high returns on its small capital (net capital employed EUR 2,165 million
  against Profit 1,099 in FY2025, because customers prepay); not open on the evidence.
- **VERDICT: IN** **[M1995-038]**, **[M2011-015]**: the deciding part's castle is shown standing over a full decade against a
  named rival's own filings; the narrowing of FY2025 and the AI threat are written down and carried to Q7.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**. Industrial Business Profit (pre-tax, before
  acquired-intangible amortization) against Industrial Business net capital employed (segment Assets, Note 29, which include
  purchased goodwill): FY2021 8,808 / 48,658 = 18.1%; FY2022 10,277 / 56,857 = 18.1%; FY2023 11,430 / 53,991 = 21.2%; FY2024
  11,390 / 52,601 = 21.7%; FY2025 11,766 / 64,224 = 18.3%. Those assets carry goodwill of EUR 40.7 billion and other
  intangibles of 12.2 billion at Sep 30, 2025 (group figures); with them taken out, as the rows ask when judging the
  business rather than the allocator **[M2011-060]**, the tangible capital the operations need is roughly EUR 11 billion
  against 11.8 billion of profit, a return of the order of 100% pre-tax. The company's own ROCE (after tax, including
  goodwill) was 19.1% (FY2024) and 17.8% (FY2025); its target is 15% to 20%.
- **Reinvestment to stand still and to grow** **[L2000-035]**: additions to intangibles and property, plant and equipment
  were 1,730, 2,084, 2,218, 2,088 and 2,445 (FY2021 to FY2025), against depreciation and amortization excluding acquired
  intangibles of about 2.6 billion in FY2025; the operations grew revenue 8%, 11%, 3% and 5% on a comparable basis (FY2022
  to FY2025) while spending about their depreciation. Working capital is partly funded by customers (contract liabilities
  12,761 against contract assets 8,141 at Sep 30, 2025). This is near the "best business" of **[M1998-081]** for the
  organic operations.
- **What the added capital earns.** The added capital went mostly into purchases: Varian (EUR 14.4 billion, FY2021), FY2022
  2.2 billion (Brightly, Supplyframe, Sqills and others), Altair and Dotmatics (14.2 billion, FY2025). Digital Industries' segment
  assets rose from 10,476 to 22,885 million in FY2025, while its Profit fell from 3,498 to 2,643 (Altair and Dotmatics
  "burdened profit by 135 million (including severance)"); in the nine months of FY2026 its Profit rose 719 million over
  the year before, part of it organic. On EUR 14.2 billion the return shown so far is in the low single digits pre-tax.
  Healthineers' Profit rose from 2,184 (FY2020, before Varian) to 3,519 (FY2025), an increase of 1,335 million against
  14.4 billion paid plus organic growth, under 10% pre-tax on the price even if all of it were Varian's. Rising earnings
  bought this way show a larger business, not a higher return: "we're not earning a higher rate of return on capital than
  we were when we started. We just put way more capital into the business" **[M2023-081]**.
- **The growth arithmetic and its caps**: organic growth reported 6.7% a year compound (FY2022 to FY2025); owner cash grew
  6.5% a year between FY2021 and FY2025 with the purchases in it. Neither runs past the rate's arithmetic over ten years.
- **WEIGHS FOR** on the operations, which earn high returns on the capital they need and reinvest little to grow
  **[M1998-081]**, **[L2009-012]**; the purchased growth has not yet shown a decent return on its price and is carried to
  Q6 as a use of the money. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (Consolidated Statements of Financial Position as filed in the
  FY2017, FY2019, FY2021, FY2023 and FY2025 reports; EUR million; FY2016 to FY2019 include the energy business spun off as
  Siemens Energy in September 2020; FY2018 onward under IFRS 15, which moved part of inventories to contract assets):

| Sep 30 | revenue (FY, as filed) | cash | receivables | inventories | contract assets | goodwill | other intangibles | total assets | debt (short + long) | pensions provision | total equity | equity to shareholders |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 79,644 | 10,604 | 16,287 | 18,160 | n/a | 24,159 | 7,742 | 125,717 | 30,967 | 13,695 | 34,816 | 34,211 |
| 2017 | 83,049 | 8,375 | 17,160 | 19,942 | n/a | 27,906 | 10,926 | 133,804 | 32,224 | 9,582 | 44,527 | 43,089 |
| 2018 | 83,044 | 11,066 | 18,455 | 13,885 | 8,912 | 28,344 | 10,131 | 138,915 | 32,177 | 7,684 | 48,046 | 45,474 |
| 2019 | 86,849 | 12,391 | 18,894 | 14,806 | 10,309 | 30,160 | 9,800 | 150,248 | 36,448 | 9,896 | 50,984 | 48,125 |
| 2020 | 57,139 | 14,041 | 14,074 | 7,795 | 5,545 | 20,449 | 4,838 | 123,897 | 44,567 | 6,360 | 39,823 | 36,390 |
| 2021 | 62,265 | 9,545 | 15,518 | 8,836 | 6,688 | 29,729 | 10,964 | 139,608 | 48,700 | 2,839 | 49,274 | 44,373 |
| 2022 | 71,977 | 10,465 | 16,701 | 10,626 | 7,559 | 33,861 | 12,196 | 151,502 | 50,636 | 2,275 | 54,805 | 48,895 |
| 2023 | 77,769 | 10,084 | 17,405 | 11,548 | 7,581 | 32,224 | 10,641 | 145,067 | 46,596 | 1,426 | 53,060 | 47,791 |
| 2024 | 75,930 | 9,156 | 16,963 | 10,923 | 7,985 | 31,384 | 9,593 | 147,812 | 47,919 | 912 | 56,231 | 51,264 |
| 2025 | 78,914 | 14,495 | 16,628 | 10,582 | 8,141 | 40,670 | 12,199 | 166,202 | 56,015 | 732 | 68,371 | 62,244 |

  What moved and why. (1) **Goodwill and intangibles against equity**: 31.9 billion against equity of 34.8 billion in 2016;
  52.9 billion against 68.4 billion in 2025, after Mentor Graphics (2017), Varian (2021) and Altair and Dotmatics (2025);
  equity to shareholders less goodwill and other intangibles is about 9 billion, so most of the book is purchased
  goodwill, and the purchases were funded largely with debt. (2) **Pensions**: the provision fell from 13.7 billion (2016)
  to 0.7 billion (2025, and 0.68 billion at June 30, 2026), through contributions (including shares of Atos in FY2018, of Siemens Energy in FY2020 and of Fluence in October 2025 transferred to the
  Siemens Pension-Trust, the last in the Half-year report's Note 3) and higher
  discount rates; the "big annuity company on the side" **[M2013-075]** is now nearly funded on the company's assumptions.
  (3) **Inventories and receivables against revenue** fell (inventories 14.2% of revenue in 2021, 13.4% in 2025;
  receivables 24.9% to 21.1%), nothing building out of line with sales **[M1995-064]**. (4) **Debt** rose from 31.0 to 56.0
  billion; about 29 billion of it is SFS debt funding the lending book (Note 20), and Industrial net debt by the company's
  own measure was 12.2 billion at Sep 30, 2025 and 9.3 billion at June 30, 2026. (5) **Retained earnings** grew from 27.5
  to 49.6 billion with cancellations of treasury shares charged against them (50 million shares in FY2023, 18 million in
  March 2026). (6) **What the figures cannot say**: the "Other financial assets" of 30.7 billion mix SFS loans with equity
  stakes carried at fair value (remeasurements of equity instruments added EUR 6.6 billion through other comprehensive income in
  FY2025, which the report attributes mainly to the Siemens Energy stake); the balance sheet does not say what the SFS loans would fetch in a bad year.
- **The real costs.** Depreciation: capex runs at about the depreciation charge, so the free cash flow figure is not
  flattered by under-investment. Stock pay: EUR 294 to 535 million a year, real and deducted in owner cash
  **[L2015-003]**; the featured EPS pre PPA does not deduct it either way, being a net-income measure that already includes
  it. Restructuring: severance every year (FY2025 continuing 636 million, FY2024 312 million), recurring and so treated as a
  running cost, already inside free cash flow. Lease payments: under IFRS 16 the principal is a financing cash flow, so free
  cash flow is stated before the lease principal payments; the run carries lease liabilities (EUR 3.2 billion
  at March 31, 2026, Half-year report Note 4) inside net debt so the cost is counted once.
- **The filer's habits, recorded here and carried to Q5.** (a) The featured figure is "EPS pre PPA", defined as "basic
  earnings per share from net income adjusted for amortization of intangible assets acquired in business combinations and
  related income taxes", "used for our capital market communication" (FY2025, 2.1 and 2.2), and the outlook is given in it.
  Part of what it adds back is amortization of acquired software technology (Mentor, Altair), where "amortization charges
  are very real expenses" **[L2012-003]**; a management highlighting "adjusted per-share earnings" is a weighing against
  **[L2016-006]**. (b) Annual earnings guidance, raised during the year (Q3 FY2026: EPS pre PPA "to a range of 11.20 to
  11.50 (previously 10.70 to 11.10)"), the habit **[L2019-006]** names. (c) EBITDA in the filer's mouth **[M1998-086]**: the
  capital structure target is "Industrial net debt to EBITDA" of "up to 1.5" (FY2025, 2.3); it is a leverage
  yardstick, not an earnings claim, and the company's own primary profit measures (Profit, net income, free cash flow) are
  after depreciation. Against the habits: the report explains its non-GAAP measures and reconciles them, and states the
  free cash flow definition plainly, which is the "clear terms" the rows credit **[M1994-018]**.
- **VERDICT on the accounts: WEIGHS AGAINST** (the adjusted figure featured and earnings guidance, carried to Q5)
  **[L2016-006]**, **[M1994-018]**. No confusion and no suspicion: the statements are readable, reconcile across ten years of
  reports, and show none of the tells of the list (no prepaid or deferred accounts building, inventories in line, no
  reserve release driving profit). Not a STOP. The recast owner cash (Step 0) feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. How well they run it, against the hand dealt: since 2016 the group has spun off its
  energy business (Siemens Energy, September 2020), listed Siemens Healthineers (2018), sold Flender (FY2021), Innomotics
  (FY2025, EUR 3,175 million cash, gain 2,326 million before tax) and smaller units, and kept the deciding part's margin in
  the band of its main rival (Q2). Industrial Business Profit rose from 8,808 (FY2021) to 11,766 (FY2025) and free cash
  flow to a record in FY2025. Against it: the capital allocated to purchases at full prices (Q6). How they treat the owners:
  Part B of Q6 and the proxy reading below.
- **The integrity record** **[M2013-088]**, **[M2005-003]**. Note 22 of the FY2025 report lists the open matters, every one
  arising from conduct dated 1992 to 2011: the OTE claim over "alleged bribery payments to OTE employees" in contracts of
  calendar 1992 to 2006 (dismissed in full at first instance in August 2024, on appeal); the Sao Paulo suits over train
  refurbishment and maintenance contracts of 2000 to 2011 (damages claimed of about EUR 400 million, 78 million and 147
  million); the Brazilian postal tender matter of 1999 and 2004. The Half-year report (Note 7) adds a January 2026 suit by
  the State of Sao Paulo and CPTM over a 2009 bidding process in which, the company says, "Neither Siemens Ltda. nor
  Siemens AG participated in the bidding or were contracted for the project". These are the legacy of the company's
  bribery era, nearly two decades old, under managements long since replaced; no instance was found in the filings read of
  an integrity matter arising from the conduct of the present Managing Board (CEO Roland Busch since February 2021).
- **The habits carried from Q4, read with the record.** (a) The featured EPS pre PPA. (b) Guidance, and the yearly claim to
  have met it: the FY2025 report says, metric by metric, "We thus fulfilled the forecast" and "We thus met the forecast",
  and reaches the EPS pre PPA range only "Excluding these effects" (the Innomotics gain and the Altair and Dotmatics burden,
  together EUR 2.23 a share): "EPS pre PPA was 10.71, well within our forecast range of 10.40 to 11.00". That framing is
  the "make the numbers" pattern the rows grow "incredulous" at **[L2002-041]**. Against doubt: the same report shows a miss
  plainly, Digital Industries' margin at 14.9% below its own forecast range of 15% to 19% (FY2024 report outlook), with the
  severance named; and the excluded items are disclosed and quantified, not hidden. Read together with a clean recent
  integrity record, the habits leave a weighing against, not a doubt about honesty.
- **The proxy** **[M1994-009]** (Compensation Report in the FY2025 Siemens Report): CEO compensation for FY2025 EUR 12,544
  thousand (base salary 1,770, fringe 109, pension 933, bonus 2,801, Stock Awards 2021 tranche 6,931), under a cap of
  13,604; bonus target achievement 140.38%. The CEO holds 74,086 shares verified under the Share Ownership Guidelines,
  746% of base salary against a requirement of 300%. Long-term pay is Stock Awards vesting on total shareholder return
  against the MSCI World Industrials index (80%) and an internal ESG index (20%).
- **How they talk; the letters** **[M1998-038]**, **[L2024-003]**: the report carries no letter from the chief executive; its
  language is house terminology ("ONE Tech Company", "Siemens Xcelerator", "Industrial Copilot"), which reads as the
  product of a communications department, a mild turnoff. Mistakes are named where they show in numbers (the Digital
  Industries miss, severance for "capacity adjustments"), not in a narrated account.
- **Love of the business, after the sale**: a hired management of a 318,000-person group; the share ownership above is the
  available evidence, and it is substantial against salary.
- **VERDICT on integrity: IN** **[M2013-088]**: no doubt about the honesty of the present management arises from the filings;
  the legacy cases are recorded. **Ability WEIGHS FOR** **[M1994-008]** on the portfolio work and the operating record, with
  the habits (adjusted figure, guidance framing) and the acquisition prices weighing against.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A: the retention test** **[R1995-009]**, **[M2011-072]**. Over FY2021 to FY2025: net income to shareholders of
  Siemens AG 6,161 + 3,723 + 7,949 + 8,301 + 9,620 = 35,754; dividends paid 2,804 + 3,215 + 3,362 + 3,709 + 4,093 = 17,183;
  purchases of treasury shares 547 + 1,565 + 884 + 1,625 + 2,269 = 6,890; retained 11,681 million. Market value: 799.31
  million shares outstanding (850 million issued less 50,690,288 in treasury, FY2020 report) at EUR 107.88 on Sep 30, 2020
  = 86.2 billion; 780.26 million at EUR 229.20 on Sep 30, 2025 = 178.8 billion (closes from the aggregator, flagged). Market
  value rose 92.6 billion against 11.7 billion retained: the market leg passes by a wide margin, though more than half of the rise is
  a higher price per euro of cash: continuing free cash flow rose from 6,352 (FY2020, FY2021 report Note 29) to 11,004
  (FY2025), up 73%, while the market value rose 107%. On intrinsic value the test cannot be closed without Q7's
  range for 2020, not built.
- **Buybacks** **[L1999-023]**, **[L2016-002]**, **[M2014-008]**. The 2024 to 2026 programme bought 28,261,391 shares for EUR
  5,999 million at an average EUR 212.28 (company buyback page, final); the 2026 programme has bought 4,497,911 at an
  average EUR 274.20 to 11 October 2026. Neither names a price above which buying stops; the stated purposes are
  "retirement, use for employee share programs, including the issuance to board members [...] and to members of the Managing
  Board" and "to allow shareholders to continuously participate in the Company's success" (FY2025 report, Note 19 and
  chapter 10.4), which is a fixed-sum programme, part of it to serve share plans, the purpose the rows rule out by name
  **[M2014-008]**. Read against the bottom of Q7's range (written back from Q7: EUR 254.06 a share on the central basis):
  the 2024 to 2026 programme's average price (212.28) sits below the bottom, so by the convention its purchases are read by
  what they did; the 2026 programme's average (274.20) sits above the bottom, and it weighs against.
- **Issuance and deals** **[L2011-003]**, **[L2009-019]**. No all-stock deal by Siemens AG was found in the window: Varian
  (FY2021) was bought for cash by Siemens Healthineers (Healthineers "carried out a capital increase during fiscal 2021 without the participation of Siemens", FY2021
  report; the rest was debt), Altair (consideration EUR 9.5 billion, "9.1 billion in cash") and Dotmatics (3.3 billion, "mainly paid in cash")
  for cash (FY2025 Note 3). The narrower STOP is not reached. The prices: Altair contributed revenue of EUR 258 million and
  a net loss of 89 million from late March to September 30, 2025, and goodwill of 7.6 billion was booked against 9.5
  billion paid; Dotmatics contributed revenue of 57 million and a net loss of 31 million in about two and a half months,
  goodwill 3.0 billion against 3.3 billion plus a 0.9 billion loan settled. On the company's own figures these were bought
  at well over ten times revenue, with the return left to "revenue synergies". Net purchases over FY2021 to FY2025 were EUR
  23.4 billion against owner cash of 42.1 billion (56%): by Q7's specific (c) this is the serial acquirer, and "what is
  smart at one price is dumb at another" **[L2011-003]**; the history of such buying "is that it's not an enormous way to
  wealth" **[M2014-074]**. Weighs against.
- **Dividends and cash**: the policy is a dividend per share "that exceeds the amount for the preceding year, or at least
  matches it" (FY2025, 2.4), a progressive dividend set by habit rather than by the retention test; the rows find payout by
  ratio "nuts" **[M2000-051]** and ask that policy be "clear, consistent and rational" **[L2012-015]**; it is clear and
  consistent.
- **Part B: pay, board, owners.** Pay: the bonus and Stock Awards reward EPS pre PPA, ROCE and relative TSR; relative TSR
  removes the market's ride but not the sector's, and Stock Awards carry no strike or step-up for retained earnings
  **[L1994-020]**; two thirds of each Managing Board member's bonus rides on group EPS pre PPA and adjusted ROCE and one third
  on individual targets including cash conversion and comparable growth "in the area of responsibility", so business
  heads are paid mostly on what the whole group does, against the rule of tying pay "to what is actually under the
  reasonable control of the person" **[M2003-019]**; the bonus also allows "Consideration of extraordinary developments". Board: two-tier, chief executive and chair separate (Supervisory Board chaired by Jim Hagemann Snabe),
  which avoids the combined role the rows warn of **[L2014-026]**; half the Supervisory Board are employee representatives
  under German co-determination. Owners: the dividend, the buybacks without a price, the guidance.
- **WEIGHS AGAINST** on Part A, for the serial acquisitions at full prices and the 2026 buyback above the range's bottom,
  with the retention test's market leg and the 2024 to 2026 buyback in favour **[L2011-003]**, **[L2016-002]**;
  **UNDECIDED** on Part B **[M2003-019]**.

## Q7 — WHAT IS IT WORTH? STOP.
Arithmetic in `Test Runs/_research 2026-10-13 SIEGY/q7_calc.py`, output in `q7_output.txt` beside it (EUR million unless
stated). The rate is the ECB AAA 30-year rate, 3.78% (2026-10-09), used as the common yardstick **[M1996-025]**; value is
held as a range **[L2000-024]**.
- **The cash input** (Step 0's table): owner cash after every real cost, five-year average FY2021 to FY2025, **8,427** on
  the all-equity basis (company free cash flow, continuing operations, which is after tax paid and all capital spending and
  before interest paid; less stock pay; less the minority's share). The business gets credit only "for whatever net cash is
  left every year" **[M1998-080]**. Two things inside the company's free cash flow are confessed rather than removed: it
  includes interest and dividends received (SFS's interest income, treasury interest on cash and dividends from stakes),
  and it is stated before lease principal payments; the first is matched by keeping SFS debt inside net debt and the second
  by keeping lease liabilities inside net debt. Equity-only owner cash (after interest paid): **7,241**.
- **The PG re-test's four specifics.** (1) Growth measured on aggregate owner cash, not per share. (2) All capital spending
  deducted; the depreciation variant (depreciation and amortization excluding acquired intangibles, about 2,570 in FY2025,
  against capex 2,445) would lower owner cash by about 125, immaterial. (3) After year ten, zero nominal growth. (4) A price
  above the top closes OUT; here the price sits inside the range, so the floor decides.
- **The six specifics.** (a) **Cycles:** the window's end years are FY2021 (recovery from the FY2020 pandemic year) and FY2025
  (Digital Industries' trough; group free cash flow a record). On the filer's own description neither is aberrational for
  the group, whose parts' cycles offset; the literal window is used and is the window shown **[L2005-003]**. (b) **Decline:**
  none; owner cash grew. (c) **Acquisitions:** net purchases over the window were 23,398 (acquisitions 31,654 less business
  disposals 8,256, including the Flender and Innomotics sales carried in discontinued investing) against owner cash of 42,137:
  more than half, so **the serial acquirer: the central figure is the organic pair**, purchases left out and only the
  organic growth the filer reports credited, the comparable revenue growth of 8%, 11%, 3% and 5% (FY2022 to FY2025), 6.71% a
  year compound **[M1998-080]**, **[M2014-068]**. The default pair is shown beside it. The MERMEC purchase, signed in May
  2026 and not closed (Q3 FY2026 release), has no price or earnings filed and is left out, said so. No deal closed between
  the window's end and the price date beyond the minor U.S. airport logistics sale (EUR 189 million, February 2026). No
  merger (a deal paid in shares) by Siemens AG in the window. (d) **Working capital:** counted inside free cash flow.
  (e) **Growth spending:** the filing states no maintenance figure **[M2000-144]**; capex runs at about depreciation, so the
  all-spending case is the central one and no growth spending is separated out. (f) **The cap:** organic growth is revenue
  growth, so owner cash is carried at its own share of sales (about 11.7% on the average base, against 12.3% earned in
  FY2025, the highest in the window); nothing traces to an absurdity **[M1999-067]**, and 6.71% is not carried past year ten
  **[M1997-095]**.
- **Whose tax:** the company's own tax, as paid inside free cash flow (FY2025 rate 23%; FY2024's 21% "had benefited from a
  reversal of income tax provisions"); no expiring carryforward shelter is stated in the filings read.
- **On what the floor is earned** **[L2017-004]**: central all-equity basis, the whole-business values less net debt. Net
  debt at June 30, 2026 (Q3 FY2026 statement of financial position): short-term debt 8,600 + long-term debt 41,324 - cash
  10,930 = 38,994; plus the 2026 buyback cash paid 1 July to 9 October 2026, EUR 1,233 million (company buyback page), since
  the share count already excludes those shares; less listed equity securities, Level 1 equity instruments at fair value
  through other comprehensive income of 12,420 at March 31, 2026 (Half-year report Note 8, the latest filing that states
  them; chiefly the Siemens Energy stake) = **27,807**. Included: SFS debt (about 28.9 billion) and lease liabilities (3.2
  billion); left out: the pension provision (0.68 billion) and current tradable debt instruments (not stated at June 30;
  1,024 at Sep 30, 2025), both said so. CONVENTION of this run: listed equity stakes counted as "securities" in net debt;
  rationale: the convention's wording is "cash and securities", the stake is a quoted security, and its dividends inside
  owner cash are small; the figure without it is shown beside.
- **The floor, tested first** **[M2003-149]**: at the price the whole business costs 209,000 + 27,807 = **236,807**. Each end
  case valued at ten percent: no-growth 84,274, organic growth 133,760. **No case earns the floor at the price.** The
  expected return at the price is about 6.0% a year on the organic growth case and 3.6% on the no-growth case.
- **Value range** (at 3.78%): **EUR 254.06 to EUR 475.40 a share** (whole business 222,947 to 392,959) against **EUR 272.10**;
  ADS equivalent EUR 127.03 to 237.70 (USD 142.11 to 265.91 at 1.1187, flagged) against USD 153.36. Width 1.87 to one.
  Beside it: the default pair (purchases of 4,680 a year deducted, total growth 6.48% credited, purchases stopping after
  year ten): EUR 254.06 to 395.30; securities not deducted: EUR 237.89 to 459.23; the industrial basis (SFS's free cash flow
  out of owner cash, SFS debt out of net debt, SFS's net assets of 4,467 added back): EUR 268.64 to 467.98; the equity-only
  figure: EUR 265.57 to 455.76.
- **Closes: OUT**, because no case earns the floor at the price, which is tested first and decides whatever the width
  **[M2003-149]**. Were the floor not decisive, the price sits inside a range narrower than three to one, which also closes
  OUT as a case that "would need a pencil", not a screamer **[M2009-005]**, **[M1996-084]**.
- **Fair price** (a reporting figure, never a verdict; Part VII): each end case at ten percent, averaged, less net debt:
  **EUR 105.73 a share on the all-equity basis** (ADS EUR 52.86, about USD 59.14), after the company's own tax; the
  equity-only figure beside it **EUR 138.12** (ADS EUR 69.06, about USD 77.26). Beside these: default pair EUR 78.76;
  securities not deducted EUR 89.56; industrial basis EUR 135.06. No cheap price is reported.
- **Back to Q6:** the bottom of the central range, EUR 254.06, is the figure Q6's buyback reading uses: the 2024 to 2026
  programme's average of EUR 212.28 sits below it; the 2026 programme's EUR 274.20 sits above it.
- **VERDICT: OUT** **[M2003-149]**: "there's just a point at which we drop out of the game"; at EUR 272.10 the best case the
  analyst can defend returns about 6% a year, below the floor of about ten percent.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked by the operator; no named business of the rows is among the parts).

---
## THE BOX
**OUT at Q7** (no case earns the floor at the price): range EUR 254.06 to 475.40 a share against EUR 272.10 (ADS EUR
127.03 to 237.70 against USD 153.36); fair price EUR 105.73 all-equity, EUR 138.12 equity-only. Q1 to Q6 passed or were
weighed (Q1 IN, Q2 IN, Q3 weighs for, Q4 weighs against, Q5 integrity IN, Q6 weighs against on Part A). No integrity
facts bearing against the present management were found; the legacy proceedings of 1992 to 2011 are recorded at Q5.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, written down, not weighed **[M1997-127]**; the box is unchanged.
- **Q9 (debt and exposures).** Industrial net debt EUR 9,342 million at June 30, 2026, 0.6 times trailing EBITDA by the
  company's own measure (Q3 FY2026 Financial Results); total debt 49,924 million, of which SFS debt about 28.9 billion
  (Sep 30, 2025, Note 20) funds a lending book of EUR 33.4 billion of SFS total assets "with the highest share in the U.S.";
  unused syndicated credit facility EUR 7.0 billion extended to fiscal 2031 (Half-year report Note 4); commercial paper
  USD 686 million at March 31, 2026; ratings A1 / A+ were shown in the FY2017 and FY2019 reports (not re-read for FY2025).
  Credit guarantees 296 million and performance guarantees 2,695 million at March 31, 2026, plus 1,764 million of Siemens
  Energy contingencies for which Siemens holds reimbursement rights (Half-year report Note 6). The FY2025 report records
  EUR 0.3 billion of "impairments of trade receivables in connection with central financing activities". Pension provision
  0.68 billion. The acquisition criterion of "little or no debt" **[R1997-001]** is stated for whole businesses and would be
  weighed, not applied, for a part-interest.
- **Q8.** The ECB 30-year rate is 3.78%; the expected return at the price on the best case is about 6.0%, on no growth
  about 3.6%.
- **Q12.** No part is among the businesses the rows name.
- **Spin-off.** A vote on transferring 30% of Siemens Healthineers to Siemens shareholders is planned for February 2027;
  the CFO says the tax rulings now allow it (Q3 FY2026 release). It would change the group's perimeter, not the floor test
  at today's price.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 042c16a1); written question by question; committed after each
      question or pair: Step 0 to Q1, Q2, Q3 and Q4, then Q5 to Q7 together because the brief asks Q6's buyback line, which
      needs Q7's bottom, to be committed with Q7. One departure, confessed: the Q7 arithmetic script was written and run in
      the research folder while Step 0 was being assembled, before Q1 to Q4 closed in the run file. Its output was not put
      into the run file before Q4 closed and carried no entry language, but it was committed (in the Q1 commit) under no
      COMPUTATION heading; operator rule 3 is about the run's reported valuation math, and the run file itself kept the
      order.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock file was present in `Screens/_daily/` (seen in a
      directory listing, not opened), held by the dispatching session; the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; `Test Runs/` was not listed or
      searched. Seen by accident and declared under contamination: commit subjects and untracked file names in the
      session's opening git status, a memory index line with counts. None used.
- [x] Every v5 id resolves (`check_ids.py` in the research folder: no E-ids, every M/L/R id in `principle_ledger_v5.csv`,
      every quoted fragment beside an id inside that row); every filing fact carries its document and date (no
      accessions exist for this filer; the SEC accessions are given for the ADS deposit agreement and the three competitors).
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (company free cash flow less stock pay less the minority's share), never a
      net-income proxy; the sovereign from the issuing authority (ECB, dated); aggregator quotes flagged (price, ADS price,
      exchange rate, historical closes).
- [x] Contrary evidence written down as found (foundations); facts for later questions are under AFTER THE STOP.
- [x] Not a point-in-time run; no row dated after the anchor issue arises.
- [x] `tools/run.py` was not used (it reads SEC data and does not serve this name); no v4 material entered.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The all-equity basis for a group with a captive lender.** Q7's convention says owner cash "before interest" against
market value plus net debt, but a company whose free cash flow is defined before interest paid and after interest
received, and which carries a EUR 29 billion lending book funded with debt, cannot be put on that basis cleanly: keeping
SFS debt in net debt while SFS interest income stays in owner cash values the loan book by capitalizing its gross yield,
which overstates it at the government rate and understates it at ten percent. The inventory-finance paragraph is the
nearest text and does not fit a lender. The run kept the company's own definitions (SFS debt and lease liabilities in net
debt) and showed an industrial basis beside (SFS cash flow out, SFS debt out, SFS net assets added back); the floor test
is the same on both. A sentence saying how a captive finance arm is treated would settle it. (2) **"Securities" in net
debt.** It is not stated whether listed equity stakes (here about EUR 12 billion, mainly Siemens Energy) count; the run
counted them and showed the figure without them. (3) **The minority interest.** Q7 says nothing about deducting the share
of a consolidated subsidiary owned by others (a third of Siemens Healthineers); the run deducted the minority's net income
each year as a confessed convention. (4) **Stock pay inside "owner cash".** Neither Q4 nor Q7 says at what figure stock
pay is deducted when the filer's free cash flow excludes it; the run used the expense credited to capital reserve. (5)
**Q1's doubt rule for a part that is itself two businesses.** The deciding part here is an automation business with a
decade's record and a software business exposed to AI; the doubt row ("if you have doubts [...] it isn't") and the parts
threshold do not say whether a doubt about a third of the deciding part keeps the whole outside. The run judged it inside
and wrote that a second analyst could close TOO HARD (NATURE) there. (6) **The share count for a filer that publishes no
treasury count at the latest quarter.** The template asks for the cover page; for a German filer the count had to be built
from the half-year note and the buyback reports, with transfers to employees after March 2026 unknown; the run confessed a
CONVENTION. (7) **Commit order versus Q6.** The brief asks Q6's line to be committed with Q7, which means Q5 and Q6 wait
for Q7, a small conflict with "commit after each question"; the run committed Q5 to Q7 together and says so.
