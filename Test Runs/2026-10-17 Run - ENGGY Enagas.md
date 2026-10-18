# Company Run: Enagás, S.A. (Madrid: ENG; OTC ADS: ENGGY) 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its source document; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch** (commit a08c08d0).

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md` with the three departures the brief states (lines of
evidence derived from the annual report; competitors from the annual report; no SEC annual report, so the company's own
annual report is the primary document). Research folder: `Test Runs/_research 2026-10-17 ENGGY/` (notes, extracts, the Q7
script `q7_compute.py` and its output `q7_output.txt`, the check script `check_run.py`; the downloaded reports sit under its
ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (59d09fe2): `PORTFOLIO.md` read for this one ticker; the operator does not hold ENGGY (no line names ENGGY, ENG or Enagas).*

**Contamination declared (seen by accident, not used).** (1) The session's opening git context showed the five latest commit
subjects of the repository, which concern another company's run (a New York gas distributor closed TOO HARD (NATURE) at Q2)
and an overnight log line; and a `git status` listing that names research folders of two other tickers. (2) The session's
auto-memory index (outside the tree) carries one-line summaries of the queue state (counts of gate-clearers, holding reviews
owed, a wave paused). (3) `ls Screens/_daily/` showed that `_overnight.lock` exists (the dispatcher's lock, rule 10(b)). None of
these was opened further or used; the other company's Q2 box in particular was not used as a precedent here, and the Q2
judgment below rests on this company's filings and the rows cited.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** Madrid close **EUR 16.81** (2026-10-16, ENG.MC, Yahoo Finance chart API via `tools/sources.py price()`;
  **aggregator, live quote only, flagged** per operator rule 5). ADS close **USD 9.37** (2026-10-16, ENGGY OTC, same
  aggregator, flagged; volume 400 ADSs that day, a thin unsponsored line). **ADS ratio: two ADSs per ordinary share** (each ADS
  is one-half of one share, Form F-6EF filed 2019-11-22, accession 0001193805-19-001749, per the brief). Cross-check: EUR 16.81 /
  2 x 1.1253 = USD 9.46 per ADS against the USD 9.37 quoted (within one percent).
- **FX:** **USD 1.1253 per EUR**, ECB euro reference rate, 2026-10-16 (ECB Data Portal, series EXR.D.USD.EUR.SP00.A; the
  issuing authority for the euro reference rate).
- **Shares by class** (one class): **261,990,074** shares of EUR 1.50 issued, less **1,980,298** treasury shares = **260,009,776**
  outstanding at 31 December 2025 (2025 Annual Report, Consolidated Annual Financial Statements, Note 3.1.a and 3.1.c; report
  dated by the Board's formulation in February 2026, results release 17 February 2026). `python Screens/cover_shares.py ENGGY`
  returned "NOT AN SEC REGISTRANT in the live ticker file"; the count is from the annual report. No later CNMV filing of the
  share count was read; the 2026 releases report no issuance (H1 2026 release, 22 July 2026). One oddity recorded for Q4:
  Note 1.7 gives a weighted average of 262,316 thousand shares outstanding for 2025, above the 261,990 thousand issued.
- **Market cap:** 16.81 x 260.010M = **EUR 4,371M** (about USD 4,918M at 1.1253).
- **Sovereign for the earnings currency (EUR):** **3.67%**, ECB euro area AAA yield curve, 30-year spot (series
  YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), observation 2026-10-15, from `python tools/sources.py` (issuing authority).
- **Filings read** (operator rule 4; no SEC filings exist, so documents are named and dated in place of accession numbers):
  - **2025 Annual Report** (English translation; contains the Consolidated Management Report, the risk section, the
    regulatory Appendix III and the audited Consolidated Annual Financial Statements, auditor EY), from enagas.es, read
    2026-10-17. The Spanish version prevails by its own statement.
  - **Informe Anual 2024** and **Informe Anual 2023** (Spanish, enagas.es), the **Annual Report 2020**, **2018** and **2016**
    (English, enagas.es "historico"), for the balance sheets, income statements and cash flows 2015 to 2024.
  - **Informe Anual 2022** (Spanish): the copy read is the mirror held by the Universitat Autonoma de Barcelona repository
    (ddd.uab.cat), the company's own document, used only for the 2021 balance sheet and 2021 and 2022 cash flows; **flagged as a
    mirror, not the issuer's site**; its 2022 figures agree with the 2022 column of the issuer-hosted Informe Anual 2023.
  - 2026 interim: **Q1 2026 results press release and CNMV note** (21 April 2026), **H1 2026 results press release** (22 July
    2026), **2025 Results and 2026 Targets release** (17 February 2026), all from enagas.es. The CNMV half-year financial report
    itself was not read (see "What I could not get").
  - **One figure cross-checked against the audited statements:** net financial debt EUR 2,475.1M at 31 December 2025 in the
    management report's Key indicators and APM section agrees with Note 3.4.a (gross financial debt 3,202,167 thousand less cash
    727,069 thousand = 2,475,098 thousand), and cash of 727,069 thousand agrees with the audited balance sheet.
- `python tools/run.py ENGGY` returned: "ENGGY: not an SEC filer. Use the evidence ladder ... This is UNRESEARCHED, not
  UNKNOWABLE." No arithmetic lines; all arithmetic below is taken from the filed statements by `q7_compute.py` in the research
  folder.
- **Owner cash after every real cost, by year (EUR M; the cash flow statements):** operating cash flow (after interest, tax and
  working capital) plus dividends received from equity investees (the cash flow line Note 1.6 identifies) less capital
  spending less cash paid for businesses and other financial assets: 2021 626.2; 2022 697.1; 2023 392.9; 2024 475.0; 2025
  179.7; **five-year average 474.2** (equity-only). Before purchases: 670.3, 756.5, 604.1, 517.2, 257.8, average 561.2.
  Capital spending against depreciation: 2021 69.9 / 262.8; 2022 90.8 / 264.1; 2023 157.0 / 273.3; 2024 97.9 / 287.1; 2025
  118.1 / 283.8. No material stock pay (incentive shares bought in the market for the plans, 18.3M in 2025, Note 3.1.c and cash
  flow statement); it is charged as personnel expense.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is "the market serves, it does not instruct" together with "who is paid to tell you":
the company's documents are written around a hydrogen future and a "growth project" whose economics no filing yet states, and
the reader must look at the cash, as "a share is a business" asks, "Would I be happy buying this stock if the market closed for
five years?" **[M1997-109]**. No macro view enters: the gas and hydrogen outlook is read only as it shows in the regulator's
documents and the company's figures **[M2000-094]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) EBITDA has
fallen every year of the window, 895.3 (2021) to 675.7 (2025), with a 2026 target of about 620 (Key indicators; 2026 targets
release); (2) capital spending has run at roughly a third to a half of depreciation every year since 2017, so the regulated
asset base on which the return is paid is shrinking; (3) the dividend was cut from 1.74 to 1.00 a share for 2024; (4) the 2019
to 2024 investment in Tallgrass Energy (USA), funded in part by a EUR 500M share issue in 2019, was sold in 2024 with a net loss
of EUR 363.7M recorded on the sale (Informe Anual 2024, Note 1.5); (5) dividends paid exceeded net profit over 2016 to 2025 by
about EUR 456M; (6) the 2027 to 2032 regulatory period is still in draft and the company itself booked a EUR 30M fall in
regulated revenue in H1 2026 under the current framework.

## THE STANDING RULE
A part-interest bought for cash, unlevered, in a single listed regulated utility does not put the buyer at risk of ruin; the
rule binds the buyer's financing and sizing, "We are never going to risk what we have and need for what we don’t have and
don’t need." **[M2012-081]**, and "borrowed money has no place in" the investor's kit **[L2014-005]**. Nothing in this run assumes
borrowing.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence chosen** (brief departure 1), from the 2025 Annual Report's business and segment note (Note 4.6), its
risk map (Management Report, Risk management) and the management report: (a) the regulated remuneration framework and the
regulator's decisions over the cycle (Appendix III; the 2027 to 2032 circulars); (b) the asset base, capital spending against
depreciation; (c) the equity-accounted investees and their dividends (Note 1.6); (d) divestments, acquisitions and their
write-downs (Tallgrass, GSP, Teréga, Saggas); (e) debt and its terms (Notes 3.4, 3.7); (f) dividends and their cover; (g) tax
and legal disputes (Notes 2.9, 4.1; the Peru proceedings); (h) pay (Note 4.3) and the board; (i) the hydrogen plan and its
regulatory status (risk map item 1, Appendix III b.1).

**What the business is, from the filings.** Enagás is Spain's gas transmission system operator: through wholly owned
Enagás Transporte it owns most of the Spanish high-pressure transmission network, the Barcelona, Huelva, Cartagena and (via
Musel Energy Hub) El Musel regasification plants and three underground storages, and through Enagás GTS it is the Technical
Manager of the gas system (Note 1.1, Note 4.6). Regulated income was EUR 949.1M of EUR 960.4M turnover in 2025 (Note 2.1.a).
It also holds equity stakes, mainly TgP (Peru), TAP (Italy, Greece, Albania), DESFA (Greece), Saggas (Spain), Altamira (Mexico)
and Stade (Germany), which paid EUR 145.6M of approved dividends in 2025 (Note 1.6). Regulated gas carried 67% of 2025
operating profit and 80% of 2024's (Note 4.6 segment table).

**The key variables and whether they are foreseeable** ("trying to identify the key variables in that particular business, and evaluating how
predictable they were first" **[M1998-044]**). For the regulated part the revenue is set by formula, not by volume: return on
investment equals depreciation plus a financial remuneration rate applied to the net (unindexed) value of each asset, plus
standard operating costs, with no automatic price indexation since 2021 (Appendix III a.2). The rate was 5.44% for 2021 to
2026; the CNMC approved in December 2025 the methodology that the company says yields "approximately 6.5%" for 2027 to 2032
(2025 Results release, 17 February 2026), and revised draft transmission and regasification circulars were published on 26 June
2026 and are before the Council of State (H1 2026 release). So the two key variables, the net asset base and the rate, are
written down by the regulator for six of the next ten years, and the company itself publishes six-year projections; the
insiders do "put down on paper" the forecast here **[M2000-105]**. The industry is not a fast-changing technology; the change
that matters is policy (decarbonisation) and the regulator, which Q2 owns. The hydrogen network the company plans (EUR 3,125M
of the EUR 4,035M plan to 2030 goes to hydrogen, Informe Anual 2024 CEO interview) has no remuneration framework yet; it is a
proposed use of the money, carried to Q3 and Q6, not a part of the present earnings.

**The perimeter.** "a reasonable fix on about what the earning power and competitive position will look like in five or 10
years" **[M2012-065]**: the earning power of the regulated base is a formula whose inputs are published; the investees are
read through the dividends they pay, as the framework's equity-method convention directs. Doubt test **[M2002-092]**: the
doubt I hold is about the regulator's future generosity and the hydrogen bet, which are castle and capital questions, not
about whether the economics can be read.

**VERDICT: IN.** The economics of a statutory, formula-remunerated gas network can be foreseen from the regulator's own
documents for most of ten years **[M1995-051]**, **[M2000-037]**; the open questions are carried to Q2 (the regulator and
decarbonisation) and Q3/Q6 (hydrogen capital).

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]**

**The castle tests, each with its filing fact.**
- **The attacker with money** ("if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
  it?" **[M2011-015]**). No. The castle is statutory: Enagás Transporte is the only company certified as a transmission network
  manager in Spain and was appointed Sole Transporter of the primary backbone network (Appendix III b.1.2; Main milestones,
  2009, 2012); remuneration is set per facility by the CNMC, and new infrastructure is discouraged except where the system
  needs it (Appendix III a.1, the 2021 to 2026 policy guidelines). An attacker with money cannot build a parallel high-pressure
  network: it would not be authorised and would not be remunerated.
- **Pricing power and the agony before a rise** **[M2005-020]**. None in the ordinary sense: the business does not set its price.
  Tolls are set by the CNMC and the Ministry (Appendix III a.5); remuneration parameters are fixed for six years and "Any
  procedure for automatic adjustment of values and remuneration parameters according to price indices is removed" (Appendix
  III a.2). The regulator, not a customer, is the counterparty whose judgment decides the price.
- **Unit volume and share of mind.** Transported demand rose 7.4% in 2025 to 372 TWh and 4.2% in Q1 2026; but volume does not
  drive the regulated revenue, which is calculated on assets and standard costs; the volume-linked continuity-of-supply term
  (RCS) is being phased out by coefficients of 95% (2021) down to 20% (2026) of its 2020 value (Appendix III a.2.3).
- **The low-cost position.** The company reports that the CEER's 2025 TSO cost-efficiency benchmark rated it the most
  efficient gas TSO in Europe (2025 Results release); under the framework, operating efficiencies are shared 50% with users
  (RMP, Appendix III a.2.3).
- **Would the customer still choose it over the low bid?** The customer has no choice: shippers must use the system;
  long-term regasification slot contracts reached 2,251 to 2041 (H1 2026 release).
- **Ask the competitors.** The 2025 Annual Report names no competitor for the Spanish regulated business; Reganosa (a Galician
  regasification and pipeline owner) appears only as the seller of 130 km of pipeline to Enagás and as holder of a put option
  (Main milestones; financial debt note). See the competitor row below.
- **Widening or narrowing** ("the number one question you want to ask yourself is whether the — could the competitive
  advantage have been made stronger and more durable" **[M2000-075]**). **Narrowing in money, not in legal position.** The
  remunerated asset base is shrinking because capital spending has run below depreciation every year since 2017 (2025: 118.1
  against 283.8), there is no inflation indexation, and the RCS term is being withdrawn; EBITDA fell from 895.3 (2021) to
  675.7 (2025) and the 2026 target is about 620; the H1 2026 release books a further EUR 30M fall in regulated revenue under the
  current framework. The legal monopoly is unchanged.
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**. Two things, both stated by the filer.
  (1) The regulator. The 2021 to 2026 framework cut the remuneration (RCS phase-out, removal of indexation), while the 2027 to
  2032 methodology raises the financial rate from 5.44% to about 6.5% on the company's own reading; the transmission circulars
  are not final (H1 2026 release). (2) Decarbonisation: the updated PNIEC raises the 2030 emissions cut to 32% against 1990 and
  plans 12 GW of electrolysers (Appendix III b.1.3), and the company's answer is to convert part of its role to hydrogen (risk
  map item 1, residual level "Significant", the only risk so rated). Against both: the law's stated principle is to "Ensure the
  recovery of the investments made by the titleholders during their useful life" (Appendix III a.2 and a.5, Law 18/2014), and
  gas demand for power generation rose 33.4% in 2025 after the 28 April blackout, when combined cycles went from about 5% to
  49% of generation (Chairman's letter).

**The competitor row** (brief departure 2). The annual report names no rival. **CONVENTION of this run:** the comparator chosen
is **Snam S.p.A.**, the Italian gas TSO, because it is the nearest regulated peer that publishes its own results and its
regulator indexes the asset base, which isolates the one difference that matters; rationale: a monopoly has no rival in its
own market, so the only comparison open is another regulator's treatment of the same business. Same metric, span endpoints,
each from the company's own regulated-information release (not the full annual report; flagged):

| | Snam 2021 | Snam 2025 | Enagás 2021 | Enagás 2025 |
|---|---|---|---|---|
| EBIT (Snam adjusted; Enagás reported, incl. equity-method result) | 1,430 | 1,845 | 583.4 | 368.1 |
| Capital spending (Snam "investimenti tecnici"; Enagás fixed assets) | 1,270 | 2,865 | 69.9 | 118.1 |
| Asset base | not in the release read | tariff RAB 26.2bn, up 8.3% in 2025 through inflation and asset growth | net PP&E 4,428.6 | net PP&E 3,679.4 |

Sources: Snam, FY2021 results release of 17 March 2022 (Borsa Italiana regulated-information store) and "CS Snam risultati
finanziari 2025 e piano strategico 2026 2030" (snam.it, March 2026); Enagás, statements above. Snam grew its operating profit
by about 29% over the span while investing heavily under an inflation-indexed regime; Enagás's fell by about 37% while it
invested less than half its depreciation. Snam's intermediate years were not read (flagged as incomplete; the span comparison
is endpoint to endpoint). Named rivals I could not read: none is named.

**The parts table** (Note 4.6, operating profit; five-year shares cannot be built because the segment structure changed at 31
December 2024, so the two years filed under the present structure are used, and this is said):

| Part | 2024 operating profit | 2025 operating profit | Share (2024 / 2025) | Castle | Decides |
|---|---|---|---|---|---|
| Regulated gas (transmission, regasification, storage, GTS; incl. Saggas, BBG) | 341.6 | 247.8 | 80% / 67% | statutory monopoly, regulator-set return | **yes** (more than half) |
| International (TgP, TAP, DESFA, Altamira, Stade; equity-accounted) | 126.6 | 125.2 | 30% / 34% | regulated or contracted pipelines and terminals abroad, read through dividends | no |
| New businesses, hydrogen, other, adjustments | -39.5 | -4.8 | n/a | not yet earning | no |

(2025 regulated operating profit is depressed by Castor decommissioning costs booked in "Other services", Note 2.1.c, which the
EUR 56.6M rise in regulated revenue largely offsets; the regulated segment decides on either year.)

**The field's returns over the last full cycle, judged in words.** The deciding part earns what the regulator allows: a 5.44%
financial rate on the net, unindexed value of each asset for 2021 to 2026, plus depreciation and standard operating costs, plus
life-extension uplifts on fully depreciated assets (Appendix III a.2). That is an ordinary return by design, as the speakers
say of utilities: "there’s no way we get rich on our utility investments. But there’s no way we get poor, either."
**[M2009-104]**. By the framework's text, a return set by a regulator is the exception, carried to Q3 as a second best; it does
not close OUT here.

**Judgment.** The castle stands because the law makes it the only network and the regulator pays for it; no attacker can take
it **[M2011-015]**. Its future can be judged in the way that matters for value: the existing assets' remuneration and recovery
over their lives are written in law and in published circulars to 2032, and the remaining net asset base (3,679 of PP&E,
depreciating at about 280 a year) is mostly recovered within thirteen years if the compact holds. What the castle protects is a
fair, shrinking return, not "excellent returns on invested capital" **[L2007-004]**; that is the regulated exception, carried to
Q3. The two threats are real and are weighed, not dismissed: the regulator has cut once in this window, and the speakers' own
utility lesson is "I did not anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**. I do
not find the moat "tenuous in any way" in the sense of **[M2000-019]**, because the doubt is about the size of the regulated
return, which the circulars state, not about whether the castle stands; the narrowing in money is carried to Q7 as a decline.

**VERDICT: IN** (statutory monopoly; regulator-set ordinary return carried to Q3 as a second best; narrowing in money carried to
Q7) **[M1995-038]**, **[M2011-015]**, **[M2009-104]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed.** Operating profit (which includes the equity-method result) against equity less
  intangibles plus net debt: 2021 583.4 / (3,101.7 - 86.6 + 4,276.8 = 7,291.9) = 8.0%; 2025 368.1 / (2,316.9 - 120.5 + 2,475.1 =
  4,671.5) = 7.9%, both before tax. The regulated segment alone: operating profit 341.6 on segment assets of 4,996.8 in 2024
  (6.8%) and 247.8 on 4,666.5 in 2025 (5.3%, Castor costs inside; Note 4.6). The regulator's rate on net assets is 5.44% for 2021
  to 2026 (Appendix III a.2.1). These are fair, not high, returns: "there’s no way we get rich on our utility investments"
  **[M2009-104]**; "deploy large sums at fair returns" **[L2005-005]**.
- **Reinvestment to stand still and to grow.** Under this framework the return is paid on the net, unindexed value of each
  asset, so standing still in money requires spending close to depreciation. Enagás has not: capital spending averaged 106.7 a
  year over 2021 to 2025 against depreciation of 274.3, and PP&E fell from 5,501.4 (2017) to 3,679.4 (2025). The business is
  being run down in its home market and the remuneration falls with it (Q2). No maintenance figure is stated in the filings;
  the shareholders "are entitled to my best guess" **[M2000-144]**, and the company gives none.
- **What the added capital earned.** The capital that did go in went mainly abroad: cash paid for businesses and associates of
  about 3.4bn over 2015 to 2020 (cash flow statements; 2016 820.1, 2019 727.5, 2020 785.2 among them), much of it for Tallgrass
  Energy (USA), funded in part by the EUR 500M share issue of 2019. Tallgrass was sold in July 2024 for USD 1,100M with a net
  loss on the sale of EUR 363.7M (Informe Anual 2024, Note 1.5). Dividends from the remaining investees run at about 160 a year
  (2021 to 2025) on equity-method investments of 1,107.0 at end-2025 plus the GSP award receivable (fair value 200.3). The GSP
  (Peru) investment was lost with the project's termination in 2017 and is being recovered through an ICSID award of USD 176M
  plus interest, raised by about USD 104M on rectification in May 2025 (Note 3.3: Peru terminated the concession on 24 January 2017; Note 2.9). "whether that’s good or bad
  depends on what we earn on that incremental $130 million over time" **[M2001-019]**: on the record here, the incremental
  money earned less than it cost.
- **The growth arithmetic and its caps.** The plan ahead is EUR 4,035M of investment to 2030, EUR 3,125M of it in hydrogen
  infrastructure (Informe Anual 2024, CEO interview), whose regulated remuneration framework does not yet exist (Appendix III
  b.1.1: the Directive is to be transposed by 5 August 2026; the draft bill was announced, not enacted, at the 2025 results);
  the risk map rates "Technological, regulatory and demand deployment of hydrogen" the only Significant residual risk. The
  rows' second best requires "reasonable expectations of earning decent returns on the incremental sums they invest"
  **[L2009-012]**; for the hydrogen spending no filing yet states the return.
- **WEIGHS AGAINST.** A regulated second best **[M1998-081]**, **[M2018-055]** whose home base is shrinking for want of
  reinvestment, whose past incremental capital (abroad) earned less than it cost, and whose next large commitment (hydrogen)
  has no stated return; the "little or no debt" criterion is applied at Q9.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eleven of them, 2015 to 2025** **[M2025-032]** (table in
  `Test Runs/_research 2026-10-17 ENGGY/balance_sheets.md`, each column from the filed statements). What moved and why:
  - **Assets and PP&E.** Total assets peaked at 9,873.7 (2021) and fell to 6,823.4 (2025). PP&E fell every year from 5,501.4
    (2017, with GNL Quintero consolidated) to 3,679.4 (2025): depreciation of 260 to 320 a year against capital spending of 42
    to 157. The balance sheet shows a home business being depreciated faster than it is renewed.
  - **Equity against goodwill and intangibles.** Intangibles are small (120.5 in 2025; the 2017 to 2018 jump to about 930 was
    GNL Quintero's concession, gone after the 2019 deconsolidation). Equity fell from 3,218.3 (2022) to 2,316.9 (2025): the
    2024 loss (-299.3, mostly the Tallgrass sale and the GSP mark) and dividends above earnings. Reserves fell from 2,036.9
    (2022) to 1,303.4 (2025).
  - **Equity-method investments** rose from 1,191.1 (2015) to 2,789.7 (2021) as the money went abroad, then fell to 1,107.0
    (2025) with the Tallgrass sale (cash proceeds 910.0 in 2024) and the GNL Quintero sale (659.6 in 2022).
  - **Cash, receivables, debt.** Receivables of 225 to 513 against revenue of about 900 to 960 swing with the gas system's
    settlement balances; trade payables include 427.0 owed to the CNMC for system surpluses and imbalances (Note 2.3), so
    working capital moves with money that is the system's, not the company's (2022 +235.3, 2023 +205.7, 2025 -259.9).
    Financial debt fell from 6,083.0 (2016) to 3,423.0 (2025), paid down from divestment proceeds; net debt 4,276.8 (2021) to
    2,475.1 (2025). More than 80% is fixed, average cost 2.1% in 2025, but the bonds carry coupons of 0.38% to 1.38% (2026,
    2028, 2032) beside a 3.63% issue to 2034 (Note 3.4), so the cost of debt will rise as the cheap bonds are refinanced.
  - **Retained earnings.** Net profit 2016 to 2025 summed 3,379.1; dividends paid 3,835.3. The company paid out about 456 more
    than it earned over ten years, and issued EUR 500M of shares in 2019. "what the figures are saying and what they don’t say
    and what they can’t say" **[M2025-032]**: the figures say the dividend was paid partly from capital and asset sales.
- **The real costs.** Depreciation is a true cost here, and the capital spending falls short of it, so reported earnings
  overstate what a holder could take out indefinitely if the asset base is to be kept; the speakers' warning runs the other way
  for railroads, where "merely spending their depreciation expense will not keep them in the same place" **[M2016-092]**; here
  even depreciation is not being spent, and the regulated revenue falls as a result. Stock pay is small and expensed. The
  Castor decommissioning costs (2025) are recurring regulated pass-throughs, matched in revenue. The GSP award is carried at
  fair value with marks through profit (+64.3 in 2025); such gains are excluded from owner cash, which counts cash only.
- **EBITDA in the filer's own mouth.** The CEO's first results sentence is "EBITDA reached 676 million and recurring Profit After
  Tax was 266 million, both above targets"; annual targets are published in EBITDA and "recurring" EAT (2026: about 620 and
  235), and a "Proforma EATI" is defined and featured among the APMs. "The one figure we regard as utter nonsense is the
  so-called EBITDA" **[M1998-086]**; a management "highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**;
  "we become downright incredulous if they consistently reach their declared targets" **[L2002-041]**; guidance is the
  "scourge" of **[L2019-006]**. These weigh against and are carried to Q5. Against them, the APM section reconciles every
  adjusted figure to the audited statements, the non-recurring items are named and explained (GSP mark, Axent step-up,
  Sercomgas and Soto la Marina gains), and the management report does not hide the 2024 loss; a management "that doesn’t care
  about the accounting but does explain to you in clear terms what’s going on" is a plus **[M1994-018]**, and preoccupation is
  "a negative" but not "a total exclusionary factor" **[M1994-018]**.
- **Confusion or suspicion?** None found that rises to the STOP **[M1995-063]**, **[M2003-029]**: the statements tie to each other
  and to the APMs; the one oddity is Note 1.7's weighted average of 262,316 thousand shares, above the 261,990 thousand issued
  (likely a translation or arithmetic slip; immaterial to any figure used here, and recorded, not explained away). The tax
  position after the Tallgrass liquidation (tax assets of 58.2 and 58.2 against a provision of 116, an IRS certificate and USD
  100M in escrow, Note 2.9 and Key indicators note 8) is disclosed and offset.
- **VERDICT on the accounts: WEIGHS AGAINST** (EBITDA and adjusted figures featured, targets beaten, guidance; dividends paid
  from capital; depreciation under-spent), no STOP. The recast earnings feed Q7: owner cash as in Step 0, five-year average
  474.2 equity-only, 509.9 on the all-equity basis.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**: "how well they run the business ... and seeing how they have allocated capital over
  time" (the row: "how well they run the business and I think you can learn a lot about that by reading about both what they’ve
  accomplished and what their competitors have accomplished, and seeing how they have allocated capital over time"). Running
  the network: 100% availability through the 28 April 2025 blackout and the 2022 supply crisis (Chairman's letter; Key
  indicators), the CEER efficiency ranking, recurring operating costs held about flat (H1 2026 release). Allocating capital:
  the record of Q3, a decade of foreign purchases (Tallgrass, GSP, GNL Quintero, Mexico) largely reversed at a loss or with
  litigation, and a dividend raised to 1.74 and then cut to 1.00. The hand dealt includes a regulator that cut the home
  remuneration in 2021, which is not management's doing.
- **The tells of dishonesty.** (1) The Peru proceedings (Note 2.9): two employees of Enagás, S.A. and Enagás Internacional are
  among those investigated in Folder 12-2017 connected with the GSP award to an Odebrecht-led consortium; the Public
  Prosecutor sought civil reparation (reference range stated by the company, USD 0 to 242M, not provided for, rated
  "possible"); at a hearing on 22 January 2026 the investigating court returned the indictment and declared the civil claim
  against Enagás inadmissible, subject to appeal; the related Folder 321-2014 ended in acquittals confirmed on appeal; and the
  ICSID tribunal that awarded Enagás USD 176M (raised by about USD 104M) "states, upon reviewing the matter, that the evidence in the arbitration file
  does not indicate any irregularities" (Note 2.9, the company's account of the award). (2) How they talk about mistakes: the
  2024 CEO interview calls the Tallgrass sale and the GSP mark, together a net loss of about EUR 600M for the year, "un
  saneamiento de la compañía que fortalece nuestro proyecto estratégico y nuestra política de dividendos" (a clean-up that
  strengthens the strategy and the dividend policy; Informe Anual 2024, CEO interview); the words "mistake" or "error" were not
  found in the interview read. The speakers name that taboo: "mistake" or "wrong" as "forbidden words ... always made me
  nervous" (the row: "That taboo, implying managerial perfection, always made me nervous") **[L2024-003]**. (3) Carried from
  Q4: EBITDA and "recurring" figures featured, annual guidance, targets reported as beaten every year read (2024, 2025 and on
  track in 2026): "things that they do in public in relation to their investors and the promises they make" **[M2004-067]**.
- **Read together, on doubt alone** ("If you’ve got doubts, forget it." **[M2013-088]**). I weigh it this way. The habits of
  (3) are the listed-utility custom, reconciled in full to audited figures, and they do not touch the regulated revenue, which
  the CNMC sets and audits; they are not evidence of numbers being made up. The Peru matter is an open criminal file against two
  employees over a 2014 award, with the courts so far ruling for the company and an international tribunal finding no
  irregularity in the award; it is recorded as an integrity fact, unresolved. The talk about the losses avoids the word
  mistake, but it does not hide the losses: the management report sets them out in figures. I do not find a doubt about
  honesty that the documents support; I do find a management that sells the future in adjectives and describes a loss as a
  strengthening, which I weigh against ability and candour, not as dishonesty.
- **Love of the business.** The CEO's own words are about the hydrogen future and the "growth project" (2025 CEO interview);
  the chairman's pay (Antonio Llardén, EUR 730 thousand, labelled "Executive Chairman" in the Note 4.3 table and "non-executive Chairman" in its footnote, a discrepancy recorded) and the CEO's fixed pay of EUR
  1.0M with EUR 538 thousand variable (Note 4.3) do not suggest the money comes first. The CEO was a director of Tallgrass
  Energy GP while it was held (Informe Anual 2024, directors' other positions), so the people who bought it are the people who
  sold it.
- **VERDICT on integrity: IN** (no doubt about honesty that the filings support; the Peru proceedings and the candour habits are
  recorded and weighed). **Ability WEIGHS AGAINST**: able operators of the network, poor allocators of the capital it threw
  off **[M1994-008]**; ability enters "as to the degree of certainty that we attribute to the stream" **[M1999-104]**, which
  matters most here at the hydrogen decision.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** ("any time we thought that we weren’t going to get more than a dollar of value per dollar retained,
  that, obviously, would be the course to follow" **[M1994-061]**; checked "on a five-year rolling basis" **[R1995-009]**). Over
  2021 to 2025 net profit summed 1,161.9 and dividends paid 1,982.8: nothing was retained; 820.9 more than profit was paid out,
  from divestment proceeds and the balance sheet. Year-end market value fell from 5,344.6 (2021) to 3,445.0 (2025) (Key
  indicators; 4,371 at today's price). Over 2016 to 2025 the company paid out about 456 more than it earned and raised EUR 500M
  of new equity on 19 December 2019 at EUR 21.50 a share (23,255,814 shares, Annual Report 2020, Note 3.1.a), in cash, which
  went with debt into Tallgrass (sold at a loss in 2024). The test cannot be passed by a company that keeps nothing; what it
  shows is that the capital it did raise and redeploy earned less than it cost (Q3). The dividend policy is now a flat EUR 1.00
  a share "beyond 2026" (2025 CEO interview), about 260 a year against recurring EAT guided at 235 for 2026: a fixed sum, not a
  test of a dollar kept against a dollar paid; the rows prefer that a company "that expects to regularly earn more than it can
  profitably employ in its business, should be paying out dividends" **[M2004-089]**, which fits the home business, but the 2026
  payout exceeds the guided earnings.
- **Buybacks.** Only purchases of shares for the incentive plans (1,500,000 shares in 2025 for EUR 18.3M, about EUR 12.2 each,
  Note 3.1.c and cash flow statement); no stated price **[L2016-002]**, but the programme's stated aim is delivery to managers,
  not value, and its size is immaterial. **Written back from Q7:** the prices paid (about EUR 12.2 in 2025) sit below the
  bottom of the Q7 range (EUR 29.72 a share on the all-equity basis at the sovereign), so by the framework's convention the
  purchases are read by what they did, not by the missing price; they do not weigh against, and they are too small to weigh for.
- **Issuance and deals** ("you just have to be sure that you’re getting as much as you’re giving" **[M2007-123]**). The 2019
  issue was a cash placement, not an all-stock acquisition, so the one STOP of Part A **[L2009-019]** does not apply. Value given
  against value got on the large deals: Tallgrass, bought in 2019 to 2020 and sold in 2024 for USD 1,100M with a net loss of EUR
  363.7M on the sale (Informe Anual 2024, Note 1.5); GSP, terminated by Peru in 2017 and pursued to an award. Pending now: 31.5%
  of Teréga (France) from GIC for EUR 573M in cash, agreed 21 April 2026, closing expected in 2026 (Q1 2026 release; H1 release:
  European Commission approval obtained, other approvals expected in Q3); a further 20% of Saggas for EUR 31M (H1 release);
  and the hydrogen plan, EUR 3,125M to 2030 with no framework yet (Q3). Asset sales: Enagás Renovable 40% for EUR 48M,
  Sercomgas, Soto la Marina (2025 to 2026 releases). The rows' test of the next 573M: "what is smart at one price is dumb at
  another" **[L2011-003]**; no filing read states what Teréga earns, so the price cannot be weighed here.
- **Part A WEIGHS AGAINST**: a decade in which the cash the home network threw off and new equity went abroad and came back
  smaller, a dividend partly paid from capital, and a next round (Teréga, hydrogen) begun before its returns are stated
  **[M2001-111]**.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**. The 2025 to 2027 long-term plan for the CEO and executives weighs
  cumulative FFO 20%, TSR 25% (absolute and relative to fifteen companies), "Hydrogen and new businesses" 25% measured as
  "investments in hydrogen infrastructure and the development of businesses", ESG indicators 15% and digital transformation 15%
  (Note 4.3). A quarter of the plan pays for investing in hydrogen, that is, for spending, not for the return on it: "you get
  what you reward for. So, if you have a dumb incentive system, you get dumb outcomes." **[M2016-083]**. The sums are modest
  (CEO 2,031 thousand in 2025; fixed 1,000, variable 538), and "any compensation sins are generally of minor importance compared
  to the sin of having somebody that’s mediocre running a huge company" **[M2007-006]**.
- **The board.** Fifteen directors, 73% independent, fees of 160 to 190 thousand (Note 4.3; Key indicators). No disclosure read
  of directors' own share purchases ("stock that they or their family have purchased" **[L2002-033]**).
- **The owners as partners.** By law no one may hold more than 5% or vote more than 3%, and gas-sector holders over 5% may vote
  no more than 1%; the state holding company SEPI holds 5.000% (Note 3.1.a). No owner can be the "very large shareholders"
  whom the rows call "The only cure" for governance **[M2006-011]**; the board answers to the regulator and the state as much as
  to the owners. The 2025 General Meeting quorum was 37% (Key indicators).
- **Part B WEIGHS AGAINST** (a quarter of the long-term plan pays for hydrogen spending; owners structurally unable to
  discipline the board).

## Q7: WHAT IS IT WORTH? STOP.
The arithmetic is `Test Runs/_research 2026-10-17 ENGGY/q7_compute.py`, output in `q7_output.txt` (EUR M unless stated).

**The cash input** (Q4 recast; "a figure calculated after interest, taxes, depreciation, amortization and all forms of
compensation" **[L2021-003]**): operating cash flow (after tax and interest, working capital counted, specific (d)) plus
dividends received from equity investees (the framework's equity-method convention: dividends, not the share of profit) less
all capital spending less cash paid for businesses, associates and other financial assets (specific (c), default pair:
purchases deducted, total growth credited).

| | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|
| Equity-only owner cash, after purchases | 626.2 | 697.1 | 392.9 | 475.0 | 179.7 | **474.2** |
| Net interest paid x (1 - 25%) | 51.9 | 44.1 | 52.5 | 9.4 | 21.1 | 35.8 |
| **All-equity owner cash, after purchases** | 678.1 | 741.1 | 445.4 | 484.4 | 200.7 | **509.9** |
| All-equity, before purchases (used after year ten) | 722.2 | 800.6 | 656.6 | 526.5 | 278.8 | 597.0 |

Tax is the company's own, as paid (cash tax 2021 to 2025: 64.1, 48.2, 151.4, 46.2, 24.3; average 66.8 against an average tax
charge of 75.6). The 2025 cash tax is low after the Tallgrass liquidation; the related tax assets are fully provided (Note 2.9),
so no carryforward shelter is priced separately (section E not triggered; said so). **CONVENTION of this run:** the interest
add-back uses the 25% Spanish statutory rate and nets interest received, because the cash that earns it is netted in net debt;
rationale: the all-equity basis needs an after-tax interest figure and the filing gives no allocation.

**The specifics, one by one.**
- **Growth shown, on aggregate owner cash.** The window's working-capital swings are the gas system's settlement money (trade
  payables include 427.0 owed to the CNMC for system surpluses and imbalances, Note 2.3; +235.3 in 2022, +205.7 in 2023, -259.9
  in 2025), which on the filer's own description is not the company's money and makes the literal end year aberrational, "a base
  year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. **CONVENTION of this
  run:** the growth is measured on owner cash before working capital and before purchases (630.9 in 2021 to 517.7 in 2025),
  while the level keeps working capital at its literal five-year total; rationale: specific (a) has no cycle to average here,
  and a growth rate set by pass-through balances would measure the system's settlement timing, not the business. Shown growth:
  **-4.82% a year**; it agrees with the course of EBITDA (895.3 to 675.7, about -6.8% a year) and the 2026 target (about 620).
  **The literal window beside it:** all-equity owner cash 678.1 to 200.7, **-26.2% a year**; carried ten years it values the
  equity below zero (EUR -2.76 a share at the sovereign), which is shown and not used.
- **(b) Decline.** The shown growth is negative, so the decline case (-4.82% for ten years) is the **bottom** and the no-growth
  case the **top**.
- **(c) Acquisitions.** Purchases are deducted (average 87.0 a year). Divestment proceeds (1,877.9 over the window) are **not**
  credited to owner cash. **CONVENTION of this run:** they already sit in today's lower net debt, so adding them to the stream
  would count them twice; rationale: the specific says "net of businesses sold", but the proceeds here were used to repay debt
  that the valuation subtracts at its current, reduced level. Serial-acquirer test: net purchases 435.1 against half of owner
  cash before purchases 1,492.4, not a serial acquirer. After year ten purchases stop (the before-purchase level, 597.0, at
  the year-ten decline factor). **Signed, unclosed deal:** Teréga, EUR 573M in cash, closing not confirmed by the price date;
  valued beside as financing added to net debt and credited at nothing, because Teréga's own filed record was not read (this
  understates the deal; said so). Saggas (EUR 31M) is immaterial and left out.
- **(d) Working capital** is counted in the level (its five-year net is +146.9, an inflow).
- **(e) Growth spending.** The filing states no maintenance figure, and spending runs below depreciation, so there is no
  growth spending to separate; the all-spending case is central. **The depreciation variant beside it** (capital spending
  replaced by depreciation, average 274.3 against 106.7, the spending that would hold the asset base): base 342.4, no-growth
  value EUR 32.72 a share at the sovereign, EUR 4.94 at ten percent.
- **(f) The cap.** Not triggered (the growth is negative).
- **Rate:** the EUR sovereign, **3.67%** (ECB, 30-year AAA spot, 2026-10-15); zero nominal growth after year ten.
- **Net debt:** **2,475.1** at 31 December 2025 (audited, Note 3.4.a: bonds, bank debt and IFRS 16 leases of 378.5, less cash
  727.1; the lease liability is kept because lease payments sit in financing, not in owner cash; the GSP award receivable of
  200.3 is not netted, said so). Beside it, the H1 2026 release's 2,305 (the half-year statement itself was not read), and
  2,475.1 plus Teréga's 573.
- **Shares:** 260.010M (two ADSs per share).

**Value range** (all-equity, central): enterprise value 10,202 (decline) to 15,548 (no growth), less net debt 2,475.1 =
**EUR 29.72 to EUR 50.28 a share** (USD 16.72 to 28.29 per ADS at 1.1253), against **EUR 16.81** (USD 9.37 per ADS). Width 1.69
to one per share. Equity-only beside: EUR 36.76 to 56.05 a share. Beside: with H1 2026 net debt EUR 30.37 to 50.93; with Teréga
EUR 27.51 to 48.08.

**The floor, tested first** ("we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**). The
expected return at today's price, on the all-equity basis (market value 4,371 plus net debt 2,475.1 = 6,846), is **8.04% in the
no-growth case** and **5.54% in the decline case**. **No case in the range earns the floor at the price.** With the H1 2026 net
debt the no-growth case is 8.23%; with Teréga added it is lower. The equity-only figures, which never decide alone, are 11.52%
(no growth) and 8.26% (decline); the gap between the two bases is the cheap fixed-rate debt (2.1% average cost, bonds at 0.38%
to 1.38% maturing 2026 to 2032), which flatters the per-share figure exactly as the all-equity convention warns: "even a
high-priced deal will usually boost per-share earnings if it is debt-financed" **[L2017-004]**.

**Why the range sits above the price while the floor fails.** The range is discounted at the 3.67% sovereign, as Q7's
construction requires; the floor asks whether the price earns ten percent. A shrinking stream bought at about 7.4% of
enterprise value in owner cash (509.9 / 6,846; 8.7% on the before-purchase level used after year ten) cannot earn ten percent: it would need growth, and the business has shown
decline. The width test is not reached (it decides only where some case clears the floor), and even if the floor were waived
the price would need a pencil: "if you really need a calculator to figure out that it’s — the discount rate is 9.6 percent
instead of 9.8 percent — forget about the whole exercise" **[M2009-005]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged,
after the company's own tax: **EUR 8.45 a share on the all-equity basis (central)** (no growth 11.38, decline 5.51), **USD 4.75
per ADS** at USD 1.1253 per EUR (ECB, 2026-10-16), against EUR 16.81 and USD 9.37. **Equity-only beside: EUR 16.78 a share, USD
9.44 per ADS.** Beside: with H1 2026 net debt EUR 9.10; with Teréga added EUR 6.24. No cheap price is reported.

**VERDICT: OUT.** No case of the range earns the floor of about ten percent at the price on the all-equity basis
**[M2003-149]**; the file closes here.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file). Facts under AFTER THE STOP.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT, at Q7** (no case earns the floor at the price: expected return 8.0% in the no-growth case and 5.5% in the decline case on
the all-equity basis). COMPUTATION range EUR 29.72 to 50.28 a share (all-equity, at the 3.67% sovereign) against EUR 16.81;
fair price EUR 8.45 a share all-equity (USD 4.75 per ADS), equity-only EUR 16.78 (USD 9.44 per ADS). Q1 IN, Q2 IN (regulated
exception), Q3 against, Q4 against (no STOP), Q5 integrity IN (Peru proceedings recorded), ability against, Q6 against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; the box is
unchanged, operator rule 2.)*
- **Q8 (the alternatives).** The EUR 30-year sovereign is 3.67% (ECB, 2026-10-15); the company's own bonds yield coupons of
  0.38% to 3.63% (Note 3.4).
- **Q9 (debt and exposures).** Net debt 2,475.1 at end-2025 (2,305 at 30 June 2026 per the H1 release), net debt to adjusted
  EBITDA 3.6 times, FFO to net debt 25.7% (APM section); BBB+ stable from S&P and Fitch; more than 80% fixed; average maturity
  4.7 years (4.4 at 30 June 2026); maturities: EUR 500M bond 2026, EUR 750M 2028, EUR 500M 2032, EUR 600M 2034, bank and EIB/ICO
  loans of 455.3 to 2031 (Note 3.4); liquidity 2,515 at end-2025 (2,626 at 30 June 2026). The CNMC's financial-prudence rule
  can cut remuneration by up to 1% if the regulated companies' ratio falls below 0.9 (Appendix III a.2.6; not applied to
  Enagás). Teréga's EUR 573M would add to debt on closing. Peru: a contingent civil liability rated possible, reference range
  USD 0 to 242M, and a USD 65.5M bank guarantee for the Category 2 escrow; USD 107.3M of cash held in Peru (Note 2.9).
  Dismantling provisions 188.7 (Note 2.9).
- **Q12.** No named business of the rows; gas transmission and LNG regasification.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit a08c08d0); written question by question; committed after each, except
      that Q3 and Q4 were written in one edit and committed together (56491b25), and the research downloads were fetched before
      Step 0 was written (all fetching after the copy).
- [x] Dispatched run: the brief allowed per-question pathspec commits; the lock in `Screens/_daily/` was present (held by the
      dispatching session; I did not touch it). The fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is declared
      under contamination at the top and not used.
- [x] Every v5 id resolves (`check_run.py`: all cited ids present, every quoted fragment beside an id found in its row, no
      E-ids); every filing fact names its document; no number without a filing or a CONVENTION label.
- [x] The order was kept; the first failing STOP (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the ECB (issuing authority); aggregator quotes flagged (ENG.MC and ENGGY via Yahoo).
- [x] Contrary evidence written down as found (foundations line and each question); facts for later questions under AFTER THE
      STOP; Q5 was reached and answered, so no integrity flag is needed in the box line.
- [x] No point-in-time anchor; no row dated after an anchor is at issue.
- [x] `tools/run.py` produced no arithmetic lines (not an SEC filer); nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit of the closing section).
- Departures, stated: the 2021 balance sheet and 2021 to 2022 cash flows come from a university mirror of the company's
  Informe Anual 2022 (flagged); the Snam comparison is endpoint to endpoint from two results releases, not the full span; the
  H1 2026 half-year financial statements were not read (the press release figures are shown beside, not central).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Working capital that is not the company's money.** Specific (d) counts working capital as capital spending and (a) treats
an aberrational end year by a cycle base; neither fits a system operator whose payables hold the gas system's settlement
surpluses (427.0 owed to the CNMC), which swing the operating cash flow by 200 to 260 a year. Taken literally the window shows
-26% a year and a negative value; I measured growth before working capital and confessed it as a CONVENTION of this run. A
rule is needed for pass-through balances (regulated settlement accounts, customer deposits held for a system). (2)
**Divestment proceeds under (c).** "Net of businesses sold" would credit 1,877.9 of sale proceeds to a five-year average for a
company that sold more than it bought, while the same proceeds already reduced the net debt the valuation subtracts; I left
them out (CONVENTION of this run). The specific should say how a net seller is treated. (3) **The range at the sovereign against
the floor at ten percent.** For a slowly shrinking regulated stream the range (EUR 29.72 to 50.28) sits far above the price
while every case fails the floor; the two tests answer different questions, and the template's line "OUT if the price sits
inside or just below a narrower range" reads oddly when the price is far below the range and the file still closes OUT. The
"floor tested first" convention settles the order, but the report figures invite misreading; a sentence in Q7 saying the
range is a sovereign-rate value and not a buy signal would help. (4) **Equity-only against all-equity when debt is very cheap.**
Here the equity-only no-growth case clears the floor (11.5%) and the all-equity case does not (8.0%), purely because 2.1% debt
will be refinanced at higher coupons; the convention correctly decides on the all-equity figure, but the text does not say
whether the after-tax interest add-back should use today's cost or a refinancing cost. (5) **Q2 for a regulated monopoly.**
The castle tests are written for competitive businesses; for a statutory monopoly the real question is the regulator's future
conduct, which Q2 handles only through the regulated-return exception and the utility mistake row; I treated the regulator's
published circulars as the evidence for the castle's future and carried the shrinking base to Q7. (6) **A company without SEC
filings.** The template asks for accession numbers and `tools/run.py`/`cover_shares.py` lines; neither exists for a Madrid
issuer, and the template could name the substitute (document and date) explicitly.
