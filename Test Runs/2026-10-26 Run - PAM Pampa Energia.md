# Company Run — Pampa Energía S.A. (NYSE: PAM, ADS = 25 ordinary shares; BYMA: PAMP) — 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no Pampa row).*

**Dispatch.** Dispatched analyst run, brief of 2026-10-26, which departs from `Screens/_daily/_dispatch_brief.md` in one
stated place (the repository path, now `C:\Projects\BRK`) and fills the brief's slots for a 20-F filer (per-ADS figures,
the 6-Ks, the functional currency). Working folder: `Test Runs/_research 2026-10-26 PAM/` (notes on the framework in
`notes.md`; the computation in `q7_compute.py`, its output in `q7_output.txt`; raw filings in the ignored `cache/`).

**Contamination, declared and not used.** (1) A top-level `ls` of the repository listed the file name `PORTFOLIO.md`
(name only; not opened). (2) The first 80 lines of `CLAUDE.md`, read for orientation, name `Screens/RESUME STATE
2026-09-12 - Opus session, note for Fable.md` and `Screens/WATCHLIST RUN QUEUE.md` and describe `PORTFOLIO.md` as holding
"holdings, standing lines, the ranked opportunity set"; none was opened and nothing in those lines names this company.
(3) `ls Screens/_daily` listed the daily file names (2026-09-01 to 2026-10-04); none opened. (4) `git status` printed one
modified path under `MBA - UNG/` (not touched). (5) After the closing commit, `git log --oneline -2` printed the subject
line of another session's fold commit about a different company (PNW); read only as a commit subject, not used. Nothing seen bears on whether anyone holds or wants PAM.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $79.50 an ADS, close 2026-10-23 (the last close before this run; Yahoo Finance chart API through
  `tools/sources.py` `price()`, an **aggregator, flagged** under operator rule 5, live quote only). Per ordinary share
  $79.50 / 25 = $3.18.
- **Shares.** `python Screens/cover_shares.py PAM`: 1,359,606,137 common shares, the cover of the 20-F for FY2025 (filed
  2026-04-09, accession `0001292814-26-002185`, as of 2025-12-31). Checked against issued less treasury and against later
  filings: issued capital was 1,363,520,380 shares at 2025-12-31 (20-F Item 7); the meeting of 2026-04-07 cancelled
  19,920,279 treasury shares, leaving 1,343,600,101 issued (20-F Item 7; 2Q26 interim statements, Note 13.4, 6-K filed
  2026-08-04, accession `0001292814-26-004045`; registered 2026-05-29); the 2Q26 earnings release (6-K 2026-08-04,
  accession `0001292814-26-004047`) gives "Share capital as of August 3, 2026 1,343.6 million common shares/ 53.7 million
  ADS" and 3.5 million treasury shares held for the employee plan at 2026-06-30 (20-F Item 6: 3,505,832). **Shares used:
  1,343.6M less 3.5M = 1,340.1M outstanding = 53.60M ADS-equivalents.** The cover's 1,359.6M is superseded by the
  cancellation; it equals issued less the 3.9M plan shares, so it did not deduct the 19.9M shares bought back in 2025 and
  held by the subsidiary GASA (my inference from the arithmetic and the 20-F's Item 16E, not a statement of the filing).
  No 6-K after 2026-08-04 reports an issuance or a repurchase (the 6-Ks of 2026-08-11 and 2026-09-08 are an investor
  presentation and the fertilizer project's RIGI approval).
- **Market cap:** 53.60M ADS x $79.50 = **$4,261.5M**.
- **Earnings currency and sovereign:** the filer states "The Company’s functional currency is U.S. Dollars, which is also
  the presentation currency" (20-F FY2025, Presentation of Financial Information and Note 4.3.1); the changeover from the
  peso was 2019-01-01 (Note 4.3, "the functional currency changeover date (January 1, 2019)"). Peso-functional
  investees (TGS, Transener) are translated at year-end rates with IAS 29 applied. **Sovereign: US Treasury 30-year par
  yield 5.33%, 10/23/2026** (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 20-F FY2025 (2026-04-09, `0001292814-26-002185`), read for the business, Item 3 risk
  factors, Item 4 regulatory framework, Items 6 to 8, 16E and the statements and notes; 6-K 2Q26 interim statements
  (`0001292814-26-004045`) and release (`0001292814-26-004047`); 6-K 4Q25 release (2026-03-02, `0001292814-26-000623`);
  6-Ks of 2026-06-12 (`0001292814-26-003430`, S&P B- to B), 2026-07-17 (`0001292814-26-003804`, fertilizer FID),
  2026-07-21 (`0001292814-26-003834`, Rincón de Aranda RIGI), 2026-07-31 (`0001292814-26-004020`, HINISA handover),
  2026-09-08 (`0001292814-26-004487`, fertilizer RIGI); for the span, the 20-Fs for FY2024 (2025-04-16,
  `0001292814-25-001504`), FY2022 (2023-04-28, `0001292814-23-001936`), FY2020 (2021-04-30, `0001292814-21-001956`) and
  FY2019 (2020-04-30, `0001292814-20-001571`), statements and the notes named below. The 20-Fs for FY2016 to FY2018
  (peso functional currency, IAS 29) were not read; the FY2019 20-F's USD comparatives reach 2017. No proxy: a foreign
  private issuer files none; board pay is in 20-F Item 6 and Note 16.3. No 3Q26 results were filed by the run date.
- **One figure cross-checked against the filed statement:** net cash from operating activities 2024, US$435M in the XBRL
  company facts = US$435M in the filed consolidated statement of cash flows (20-F FY2025, `0001292814-26-002185`); capital
  spending 2024, US$447M tagged = US$447M filed.
- **`python tools/run.py PAM`:** printed only "PAM: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The tool's
  US-GAAP tags do not reach this IFRS filer; **no line of it is used**. Every figure below is from the filed statements.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own Pampa "if the market closed for five years" **[M1997-109]**, which here
means owning a set of Argentine power plants, Vaca Muerta acreage, two petrochemical plants and minority stakes in a gas
pipeline and a power grid, with the price of most of what they sell written by the Secretariat of Energy. No macro view
enters: "macro conclusions are — just never enter into the discussion" **[M2000-094]**. That cuts both ways here: no
forecast of the peso, of Argentine inflation or of the next election is made, but the government is not "macro" to this
business; it is the customer (CAMMESA, ENARSA), the price-setter (the remuneration resolutions, Plan Gas) and the grantor
of the concessions, so its conduct is read from the filings as a property of the business, not forecast. A holding whose
value is exposed to a currency is, in part, "a bet on how government now, and in the future, will behave" **[M2011-025]**.
**Contrary evidence, written down as found**, "in the first 30 minutes" **[M1997-127]**: (i) the deciding part's US$ operating income held between
US$204M and US$375M a year from 2020 to 2025 through a pesified tariff, a devaluation and payment in bonds (segment note,
20-F FY2025 and FY2022); (ii) the 2025 deregulation (SE Resolution 400/25) moved thermal generation toward marginal
pricing that the filer says "benefits more efficient units, particularly CCGTs" (4Q25 release), which favours Pampa's
combined cycles; (iii) S&P raised the company to B on 2026-06-12, and the company placed US$500M of 2037 notes at 7.6% in
May 2026, the lowest spread in its history (2Q26 release); (iv) 2Q26 adjusted EBITDA of US$415M was 75% above 2Q25, so a
five-year window may understate a business in transition (2Q26 release; a featured adjusted figure, read as such).

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of the NYSE ADS for cash, sized so that a total loss could not touch
what the buyer has and needs, puts the buyer at no risk of ruin; the rule forbids only borrowing to buy or sizing that
risks "what we have and need for what we don’t have and don’t need" **[M2012-081]**, and "Never risk permanent loss of
capital." **[L2023-005]** reads here as a sizing limit on a holding whose currency, transfer and expropriation risks the
20-F lists at length (Item 3). Nothing in the purchase itself requires leverage or collateral.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will be in 10
years" **[M2000-037]**; knowing the product is not enough: "We just don’t know the economics of it 10 years from now."
**[M2000-104]**. The way in is the key variables "and evaluating how predictable they were first" **[M1998-044]**; the
filter is "If something’s important but unknowable, forget it." **[M2006-076]**.

**Read by its parts** (holding company and operating segments, the Q1 and Q2 conventions: a part decides at more than half
of five-year operating profit, else the largest). Segment operating income, US$M, from the segment notes of the 20-F for
FY2025 (`0001292814-26-002185`, 2023 to 2025) and FY2022 (`0001292814-23-001936`, 2021 and 2022):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year | Share |
|---|---|---|---|---|---|---|---|
| Power generation | 350 | 336 | 272 | 204 | 375 | 1,537 | **59.6%** |
| Oil and gas | 130 | 194 | 140 | 69 | 91 | 624 | 24.2% |
| Holding, transport and others (TGS, Transener stakes) | 54 | 49 | (33) | 124 | 68 | 262 | 10.2% |
| Petrochemicals | 45 | 52 | 45 | 43 | (31) | 154 | 6.0% |
| Consolidated | 579 | 631 | 424 | 440 | 503 | 2,577 | 100% |

**Power generation decides.** The question is whether its earning power in ten years can be foreseen.

**The key variables of the deciding part, from the filings.**
1. *The price, and who sets it.* Units without a contract were paid under remuneration schemes written by the Secretariat:
   SEE Resolution 19/17 (US$-denominated) "remained in force until February 28, 2019"; SRRYME 1/19 to January 2020; SE
   31/20 from February 2020, priced in pesos with an automatic adjustment; SE 440/21 raised it 29% and "repealed the
   automatic adjustment mechanism", and Pampa adhered on condition that generators "waived and/or dismissed all
   administrative and/or judicial claims filed due to the non-application of the automatic adjustment formula"; then
   238/22, 826/22, 750/23, 869/23, 9/24 (a 74% rise described in its own recitals as "a transitional measure") and ten
   further resolutions in 2025 alone, each a rise of 0.4% to 4% (20-F FY2025, Item 4, Electricity Regulatory Framework, and
   Note 2.2.3.2). From 2025-11-01 the thermal units moved to a new framework, SE 400/25, "a marginal pricing spot market and
   the MAT", with capacity paid at "U.S.$ 12/MW" an hour in about 90 hours a week (20-F Item 4; 4Q25 release). The
   framework is eleven months old on the run date.
2. *Whether the price is paid.* "payments corresponding to the months of December 2023 and January 2024 were paid with
   Argentine Sovereign Bonds, resulting in significant losses to our results"; "in recent years there have been
   significant delays in such payments"; "We cannot guarantee that CAMMESA, ENARSA, the Argentine Government and/or other
   customers will not experience payment delays, or that such payments will not be altered in any way" (20-F Item 3).
3. *The contracts and their term.* The US$ PPAs that carried part of the window are government-written too: "Such PPAs
   could be revoked, modified or in any other way affected by any measure adopted by the Argentine Government"; the
   SE 220/07 PPAs of CTP and CTLL's TV01 ended in 2021 and CTEB's gas-turbine PPA in April 2022, after which "the units have
   been remunerated under the spot scheme"; and in November 2025 Pampa "suspended the PPAs relating to the combined cycles of
   CTGEBA, CTLL and CTB", whose obligations "will remain suspended as long as the conditions established in SE Resolution
   No. 400/25 remain unchanged" (20-F Item 3 and Item 4).
4. *The company's own forecast.* The filer does not write the ten-year economics down; it writes the opposite: of the
   2025 deregulation, "many are recent and their full impact on the electricity sector remains uncertain", and the
   government may adopt "further emergency legislation [...] unfavorable alterations to our tariff structures or
   remuneration scheme"; of its sector generally, "Since we operate in a context in which the governing law and applicable
   regulations change frequently, in part as the result of changes in government administrations, it is difficult to
   predict if and how our activities will be affected by such changes" (20-F Item 3).

**Judgment.** The deciding variable is the price a government agency pays for capacity and energy, and whether it pays it
in money. In the window it was set in dollars, then in pesos with indexation, then in pesos without indexation (with
Pampa giving up its claims to get a rise), then by some twenty ad hoc resolutions, then, from November 2025, by a
marginal-price market whose survival the filer itself conditions ("as long as the conditions [...] remain unchanged").
That is a key variable that is important and, ten years out, unknowable: "If something’s important but unknowable,
forget it." **[M2006-076]**; "If something is not very predictable, forget it." **[M1998-044]**. The rows' own regulated
case is the warning: "I did not anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**,
said of American utilities, where the compact had held for decades; here it was rewritten every year of the window. The
test abroad is whether "we understand the nuances of the corporate governance system and taxation and that sort of thing"
**[M2000-141]**, and the taxation here includes an income-tax inflation-adjustment regime the company calls "confiscatory"
and litigates (Note 11.6.1), with export duties and price controls in the oil and gas part (Item 3). "if you have doubts
about something being into your circle of competence, it isn’t." **[M2002-092]**.

**Contrary evidence, carried and weighed**, since the mind would otherwise "reject contrary evidence to cherished
beliefs" **[M1997-127]**: the deciding part earned US$204M to US$375M of operating income
in each of 2020 to 2025 through all of the above; the new framework may be the "change for the better" the rows allow,
"the railroads were a terrible business for decades and decades and decades and then they got good." **[M2017-026]**; and
an understood business abroad asks a lower price, not a pass: "We wanted to get paid more for going into China, and we did,
because we don’t know the game as well there." **[M2006-021]**. They do not carry the question. The stable US$ income of
2020 to 2025 rested on US$ PPAs that are rolling off or now suspended, and the rest on prices the government reset at will;
the improvement is eleven months old and depends on the same government's continued choice; and [M2006-021] presumes "a
business we understood", which is the question here, not its answer. Commodity dependence is not the ground (the commodity
paragraph of Q2 forbids that: "We don’t think we can predict commodity prices." **[M2016-025]**); the ground is that the
price of the deciding part is a regulator's decision with a record of reversal, and the counterparty a state agency that
paid in bonds.

**Which cause.** NATURE, not WORK. No filing not yet read can answer the question, because the question is what future
Secretariats of Energy and future governments will pay generators, and the company that knows the most writes that it
cannot say (item 4 above). That is the case in which "We couldn't solve this problem, moreover, even if we were to spend
years intensely studying those industries." **[L1993-023]**, and the insiders' test, "They would say, “That’s too hard.”"
**[M2000-105]**, is met by the filer's own risk factors. A lower price does not reopen it: "It doesn’t mean it isn’t a good
buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it."
**[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)**, the third of "three boxes at the company: in, out, and too hard" **[M2006-013]**. The deciding part's ten-year earning power rests on a government-set
  remuneration and a state counterparty, rewritten repeatedly over the window and replaced by a new market eleven months
  ago, which the filer itself will not forecast (20-F FY2025, `0001292814-26-002185`, Items 3 and 4).

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a question. The balance sheets, which the template asks to be read in Step 0 when the file closes before
Q4, are read under AFTER THE STOP, Q4.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The two reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED; not asked.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1** (the deciding part, power generation, 59.6% of five-year operating profit, earns
a price the Secretariat of Energy writes and a state agency pays, rewritten repeatedly in the window and replaced by a new
market eleven months ago; the filer will not forecast it). Cause NATURE: no filing not yet read answers what future
governments will pay generators: "We couldn't solve this problem, moreover, even if we were to spend years intensely
studying those industries." **[L1993-023]**; the box is closed and a lower price does not reopen it: "It just means that
we don’t know how to evaluate it." **[M2000-038]**. **Integrity facts recorded, not judged** (AFTER THE STOP, Q5). For the record only, the COMPUTATION below
shows no case of the range earning the floor at $79.50, so the file would also have closed OUT at Q7. No research pass:
the cause is NATURE, and Part VII runs a pass only where some case earns the floor at the price, which none does.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found, as the row asks, "write it down in the first 30 minutes" **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).*

### Q2 (the castle): the parts, the field, the rivals
- **Parts table**: Q1 above. Generation decides at 59.6%; oil and gas 24.2%; holding and transport 10.2%; petrochemicals
  6.0% (segment notes, `0001292814-26-002185`, `0001292814-23-001936`). The forward mix is moving to oil: 2025 capital
  spending was US$1,039M in oil and gas against US$66M in generation (20-F FY2025, Item 5, Capital Expenditures), and
  2Q26 adjusted EBITDA is described as driven by "higher contribution from RDA" (2Q26 release).
- **Generation's own returns** (segment operating income over segment assets, the segment note's figures): 2021 21.0%,
  2022 13.6%, 2023 10.1%, 2024 6.5%, 2025 12.3% (segment assets include equity-method investments). Capacity 5,472 MW,
  "approximately 12% of Argentina’s installed capacity" (2Q26 interim statements, Note 1.1).
- **The field's returns, whole company, operating income over total assets** (SEC company facts, XBRL, transcription,
  **flagged**; the peso reporters' frames mix restatement vintages and are shown only as a rough guide):

| Filer (currency) | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Pampa (US$; filed) | 6.5% | 10.9% | 8.1% | 5.0% | 15.0% | 13.3% | 9.0% | 6.9% | 7.6% |
| Vista Energy, VIST (US$) | 5.7% | n/f | 1.1% | -5.1% | 12.5% | 26.0% | 24.3% | 14.8% | n/f |
| YPF (US$) | n/f | n/f | n/f | -3.5% | 3.0% | 9.6% | -5.0% | 5.0% | 5.9% |
| TGS (AR$, IAS 29) | 21.3% | 31.3% | 31.2% | 16.1% | 16.4% | 12.7% | 7.6% | 16.5% | n/f |
| Central Puerto, CEPU (AR$, IAS 29) | 18.7% | 72.5% | 35.6% | 34.4% | 39.8% | 35.3% | 24.1% | 7.4% | n/f |

  CEPU's 2018 to 2023 figures carry non-operating items its filings book in operating income (an operating margin of 214%
  in 2018 and 108% in 2023 on the same tags), so the row does not compare. Pampa's pre-tax operating return on assets
  averaged 9.1% over 2017 to 2025; YPF's was about 2.5% over 2020 to 2025; Vista's, the Vaca Muerta pure play, was about 12%
  over 2019 to 2024 and above 24% in 2022 and 2023. Accessions of the peers' 20-Fs were not pulled into this file; the
  figures are the company-facts frames as tagged, read for ratios only (`Test Runs/_research 2026-10-26 PAM/peers_output.txt`).
- **Rivals that do not file with the SEC**: Pan American Energy, Tecpetrol, Pluspetrol, TotalEnergies Austral and
  Chevron's Argentine unit in Vaca Muerta; AES Argentina, Genneia, MSU Energy and SADESA in generation; none read.
- **Price power in the deciding part**: the remuneration history and the bond payment of 2024, Q1 items 1 to 3. The new
  framework's capacity price is "U.S.$ 12/MW" an hour with seasonal multipliers, and units without self-supplied fuel lose
  capacity pay by stages to 2028 (20-F Item 4); Pampa self-supplies gas to CTLL and CTGEBA from December 2025 (4Q25 release).
- **Oil and gas**: the part earned operating income of US$69M to US$194M a year in 2021 to 2025 and a loss after its
  financial costs in 2023, 2024 and 2025 (US$-47M, -5M, -55M; segment note). Its gas is sold largely under Plan Gas
  contracts with CAMMESA and ENARSA, whose "Payments [...] have suffered significant delays in recent years" (20-F Item 3).

### Q3 (capital): what went in, what is committed
- Capital spending against depreciation, US$M: 2021 210 / 205; 2022 447 / 212; 2023 758 / 267; 2024 447 / 342; 2025 993 /
  414; 1H26 518 paid (statements of cash flows and Note 14; 2Q26 interim statements). PP&E bought through payables, not yet
  paid, US$169M in 2025 (Note 14).
- Committed: Rincón de Aranda under RIGI, "The total estimated investment in the RDA Project amounts to US$4.522 billion"
  (6-K 2026-07-21); the urea plant, "an investment of approximately US$2.7 billion", FID taken 2026-07-17 with a 41-month
  build and an EPC guarantee granted by Pampa (6-Ks 2026-07-17 and 2026-09-08); the RDA midstream plant, US$376M (Note 17);
  20% of SESA's floating LNG project, vessel "expected to start operating in September 2027" (20-F Item 4).
- Depreciation and amortization doubled, US$205M (2021) to US$414M (2025), as shale depletion grew (Note 14).

### Q4 (the numbers): the balance sheets first, 2018 to 2025 and June 2026
Eight year-ends in the functional currency, US$M, from the filed statements (`0001292814-20-001571`,
`0001292814-21-001956`, `0001292814-23-001936`, `0001292814-25-001504`, `0001292814-26-002185`, `0001292814-26-004045`).
FY2016 and FY2017 were filed in pesos and not read; the US$ company facts give total assets of US$5,657M and equity of
US$1,969M at 2017 year-end (transcription, flagged). Read "over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.

| US$M | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Jun 2026 |
|---|---|---|---|---|---|---|---|---|---|
| PP&E | 3,316 | 3,507 | 1,610 | 1,659 | 2,164 | 2,544 | 2,607 | 3,303 | 3,479 |
| Investments in associates and JVs | 407 | 511 | 549 | 774 | 902 | 672 | 993 | 1,059 | 1,354 |
| Trade receivables, current | 703 | 561 | 341 | 397 | 470 | 296 | 488 | 614 | 948 |
| Inventories | 137 | 153 | 116 | 155 | 173 | 205 | 223 | 231 | 283 |
| Cash and current securities | 681 | 644 | 491 | 573 | 700 | 835 | 1,668 | 1,091 | 1,281 |
| Borrowings | 2,177 | 1,947 | 1,614 | 1,438 | 1,613 | 1,448 | 2,079 | 1,892 | 2,600 |
| Net debt (borrowings less cash and securities) | 1,496 | 1,303 | 1,123 | 865 | 913 | 613 | 411 | 801 | 1,319 |
| Equity attributable to owners | 1,366 | 1,917 | 1,428 | 1,785 | 2,277 | 2,404 | 3,286 | 3,596 | 4,027 |
| Non-controlling interest | 429 | 492 | 341 | 6 | 7 | 9 | 9 | 9 | 13 |
| Total assets | 5,672 | 5,684 | 4,890 | 3,861 | 4,742 | 4,722 | 6,345 | 6,594 | 7,749 |

What the figures say: 2018 and 2019 consolidate Edenor (held for sale at 2020 year-end, US$1,469M of assets and US$1,021M
of liabilities), so the continuing business is read from 2020. Owners' equity roughly doubled, US$1,785M to US$3,596M,
2021 to 2025, while buybacks took about US$104M and no dividend was paid to Pampa's owners; net income attributable over
those years was US$2,027M, of which gains on financial instruments were large (US$392M in 2023, US$213M in 2024, US$181M
in 2025, Note 14 adjustments) and a deferred-tax credit made 2024's tax a benefit of US$121M. Net debt fell to US$411M at
2024 and has tripled since, to US$1,319M at June 2026, as the oil build-out began. Receivables rose faster than sales:
26% of sales in 2021 and 2022, 17% in 2023, 26% in 2024, 31% in 2025, and US$948M at June 2026 against first-half sales the
release puts at US$746M for the second quarter alone. No goodwill line; intangibles fell from US$161M to US$87M. What they
cannot say: the price CAMMESA will pay, and whether it pays in money.
- **Tax.** Income tax paid in cash was US$13M, 2M, 0, 0 and 8M in 2021 to 2025 against current tax charged of US$67M,
  78M, 46M, 284M and 99M (Note 10.6 and Note 14); income-tax liabilities rose by about US$193M over the window. In November
  2025 the company entered a payment facility plan (ARCA General Resolution 5,684/25): "Payment plans" of US$212M non-current
  and US$14M current at 2025 year-end (Note 11.7). The company calls the tax inflation-adjustment regime "confiscatory"
  and provisions US$22M for the dispute (Note 11.6.1).
- **Featured figures.** Each release heads with "Adjusted EBITDA" (4Q25: "Adjusted EBITDA reached US$230 million"; 2Q26:
  "Adjusted EBITDA totaled US$415 million"), a habit the framework records at Q4 as a weighing and carries to Q5.
- **Other real costs.** Recurring impairments (US$139M 2020, 38M 2022, 39M 2023, 34M 2024, a 15M recovery in 2025);
  compensation-agreement accruals of US$37M, 61M and 14M in 2023 to 2025 (Note 16.3), non-cash in the year and inside
  operating cash only when paid; borrowing costs capitalized US$21M, 8M, 6M (Note 14); TGS and Transener are peso
  companies restated under IAS 29 and translated (Note 4.3.3).

### Q5 (who runs it): integrity facts, recorded, not judged
- **Control and owners.** Management control group at 2026-03-31: Marcos Marcelo Mindlin 13.87%, Gustavo Mariani 3.25%,
  Damián Mindlin 2.93%, Ricardo Torres 1.80% (21.85% together); ANSES, the state pension agency, 22.81%; Hidden Lake S.A.
  5.29% (20-F Item 7). Nicolás Mindlin, the chairman's son, is Executive Vice President (Item 6).
- **A related-party contractor.** SACDE, listed under "Other related parties", sold Pampa goods and services of US$65M
  (2023), US$103M (2024) and US$223M (2025), about 22% of 2025's capital spending (Note 16; R119 of the XBRL viewer). An
  alternate director, Diego Salaverri, sits on SACDE's supervisory committee, and his law firm, whose partners include two
  members and two alternates of Pampa's supervisory committee, is paid by Pampa (Item 6 and Item 7, Interests of experts
  and counsel). The 20-F does not state SACDE's owners; I did not look outside the filing.
- **Edenor's sale.** Control of Edenor was sold under an agreement of 2020-12-28 to Empresa de Energía del Cono Sur,
  Integra Capital and "Messrs. Daniel Eduardo Vila, Mauricio Filiberti and José Luis Manzano" for 21,876,856 Edenor class B
  shares and US$95M in cash, after a 2020 loss from discontinued operations of US$592M (20-F FY2022 Item 4; FY2020 income
  statement).
- **Proceedings.** A consumers' association's US$3,650M claim against Pampa and its 2016 directors over the Petrobras
  Argentina acquisition ended in the company's favour at the Supreme Court in 2025; Pampa lost its action to annul the ICC
  award to Petrobras Operaciones on 2026-03-31 (20-F Item 8). No instance found in the FY2025 20-F of a corruption or
  bribery proceeding against the company or its directors, by a text search for "Cuadernos", "notebook", "bribe", "briber",
  "corruption case", "indicted" and "FCPA"; the 20-F's general risk factor on corruption investigations in Argentina is the
  only hit near the subject.
- **Pay.** Senior management's compensation agreements pay "3.6% of the Company’s annual market value appreciation,
  measured in U.S. Dollars, with an annual cap of 50% of the accrued amount and 1.8% of the Company’s operating income before
  interest, taxes and other non-cash items", unpaid accruals carried forward (20-F Item 6). Key management pay was US$44M,
  US$67M and US$20M in 2023 to 2025 (Note 16.3), against attributable profit of US$302M, 619M and 377M. Directors' pay for
  2025 was set at Ps. 23,904 million by the meeting of 2026-04-07 (Item 6).
- **Targets.** The releases state production targets ("a plateau of 45 kbpd by 2027", 4Q25 release); no earnings guidance
  found in the two releases read.

### Q6 (the money and the owners)
- **Buybacks** (statements of cash flows): US$341M (2018, continuing), 141M (2019), 104M (2020), 39M (2021), 18M (2022),
  none in 2023 and 2024, 47M (2025), none in 1H26. Prices disclosed in Item 16E: April 2019, US$23.18 an ADS under a
  programme "for up to US$200 million" (an amount, no price); June to July 2022, US$20.23 to US$20.78 an ADS by the
  subsidiaries GASA and CISA; September to October 2025, US$58.65 and US$59.50 an ADS by GASA under a programme "with a
  maximum price of U.S.$ 60 per ADR and Ps. 3,480 per common share". Shares outstanding: 1,677.1M at 2019 year-end
  (FY2019 cover), 1,451.2M at 2020 year-end (FY2020 cover), 1,340.1M now.
- **The Q6 buyback line, COMPUTATION, NOT A CLEARANCE** (Q6's test against the bottom of Q7's range; recorded here
  because Q6 was not reached): the bottom of today's computed range is $40.55 an ADS. The 2019 and 2022 purchases, at
  about US$20 to US$23 an ADS, sit below it; the 2025 purchases, at US$58.65 to US$59.50, sit above it and below its top
  of $105.11. Today's range is not the range of 2019 or 2022, so the comparison is indicative only.
- **Dividends**: none paid to Pampa's own shareholders in 2021 to 2025 (the US$1M "Dividends payment" lines of 2023 and 2025 match a distribution to the related party EMESA in Note 16);
  the indentures restrict distributions on default or where the company "is not in a position to incur debt" (2Q26
  interim statements, Note 13.3).
- **Deals**: Petrobras Argentina, 67.2% bought for cash in July 2016, later merged into Pampa by absorption (20-F Item 4;
  the exchange terms are in the FY2017 20-F, not read, so Q6's STOP on an all-stock deal could not be tested); Edenor sold
  2021 (Q5 above); OCP Ecuador's last 36% bought for US$23M in August 2024 and the concession handed to the state at no cost
  three months later (Item 4); HINISA's concession handed back to Mendoza on 2026-07-31 (6-K `0001292814-26-004020`).

### Q9 (could it ruin us)
- Gross financial debt US$2.6bn at 2026-06-30, 97% capital markets; 79% foreign-law US$ notes at 7.8% with 9.2 years of
  average life; overall average cost 7.3% and life 7.7 years; US$500M of 2037 notes reopened in May 2026 at 7.6%; "Pampa
  remains in full compliance with all debt covenants" (2Q26 release). Net debt US$1,319M; S&P long-term rating B, stable
  (6-K 2026-06-12).
- Calls for cash: "increased collateral requirements linked to crude oil price hedging" raised net debt in 1H26, and a
  derivative liability of US$54M stood at June 2026 (2Q26 release and statements). The tax payment plan (US$226M at 2025
  year-end) and the guarantee of the urea plant's EPC contract sit outside borrowings.
- Cover: 2025 operating income US$503M against financial costs of US$196M (2.6 times); pre-tax profit US$582M (income
  statement). The committed projects (Q3) are a multiple of the 2025 owner cash in every case below.

---
## COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures; Q7's construction applied after the STOP)
*A reporting convention at the owner's request, not a rule and not entry language (operator rule 3). Script and output:
`Test Runs/_research 2026-10-26 PAM/q7_compute.py`, `q7_output.txt`.*

**Owner cash, US$M, continuing operations, from the filed statements of cash flows and Note 14** (operating cash is
before interest paid, which this filer reports under financing; investee profit counted as dividends received, the
equity-method convention, 2025 including US$45M of CIESA dividends received in securities):

| | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|
| Operating cash (2021: 729 less Edenor's 116) | 613 | 619 | 575 | 435 | 778 | 604 |
| Capital spending, PP&E and intangibles | 210 | 447 | 758 | 447 | 993 | 571 |
| Depreciation and amortization (the maintenance guess) | 205 | 212 | 267 | 342 | 414 | 288 |
| Net acquisitions (paid less collected) | -34 | 67 | -71 | -71 | 37 | -14 |
| Dividends from investees | 18 | 10 | 0 | 46 | 70 | 29 |
| **Owner cash, maintenance only, acquisitions deducted (central)** | 466 | 371 | 400 | 210 | 406 | **371** |
| Owner cash, maintenance only, organic | 432 | 438 | 329 | 139 | 443 | 356 |
| Owner cash, all spending, acquisitions deducted (literal) | 461 | 136 | -91 | 105 | -173 | 88 |
| Interest paid | 140 | 162 | 280 | 145 | 161 | 178 |

**The construction, by Q7's range convention in full.** Five-year window 2021 to 2025. Maintenance guess: depreciation as
"a proxy for required capital expenditures" **[M1998-127]**, the filing giving no maintenance figure; depreciation charges
"are almost always true costs" **[L2015-004]**. (a) Cycle: no end year is described by the filer as aberrational, so the literal window is
the base. (b) Decline: central owner cash fell from US$466M to US$406M, -3.39% a year (the halves agree: US$418M in
2021-22, US$308M in 2024-25), carried as negative and made the bottom; the no-growth case is the top. (c) Acquisitions:
deducted with total growth credited (the company was a net seller); the organic pair is beside (US$356M average, end years
+0.6% a year); not a serial acquirer; no signed unclosed acquisition (the urea plant and RDA are capital spending). (d)
Working capital counted inside operating cash (2024: US$-336M). (e) Maintenance case central; growth spending (capital
spending above depreciation) averaged US$283M, charged in the growth case at **US$273M in year one and US$200M in year ten,
none after**; the growth case falls below the no-growth case, the inversion the convention names, "growth can destroy
value", the window's US$1.4bn of growth spending having bought no growth in owner cash. (f) Cap: not binding (the shown
rate is negative; sales grew 7.3% a year). Rate 5.33%, ten years, then zero nominal growth. Net debt US$1,319M at
2026-06-30 (borrowings 2,575 + 25, less cash 979 and current securities 302; leases left out, right-of-use US$24M); no
subsequent borrowing stated in a later filing. Shares 53.60M ADS-equivalents.

**The floor first.** No case earns about ten percent at the price, the point where "we don’t want to buy
equities where our real expectancy is below 10 percent" **[M2003-149]**: the top case, maintenance owner cash of
US$371M with no growth, is 6.6% of the enterprise value at the price (US$4,262M + US$1,319M = US$5,581M); the literal
all-spending owner cash is 1.6%. By the computation Q7 would close OUT whatever the width (2.0 to 1).

**(a) VALUE RANGE** (all-equity basis, central; Q7, On what the floor is earned, whose principle is "we evaluate
acquisitions on an all-equity basis" **[L2017-004]**):
**$40.55 to $105.11 an ADS ($1.62 to $4.20 an ordinary share)**, against $79.50 an ADS ($3.18 a share). The price sits
inside the range. Beside it: the equity-only range $2.99 to $67.55 an ADS; the literal all-spending window at no growth
$6.05 an ADS; a tax-accrual variant (charging the US$39M a year of unpaid income-tax build-up) tops at $91.60 an ADS.

**(b) FAIR PRICE** (each end case valued at ten percent, the two averaged, after the company's own tax; Part VII):
**$23.69 an ADS ($0.95 an ordinary share) on the all-equity basis, central**; **$15.17 an ADS ($0.61 a share) on the
equity-only basis, beside**. Not a regulated utility: the deciding part earns no allowed return on invested capital, so the
utility exception does not apply. Neither figure is a verdict; the box is TOO HARD (NATURE) at Q1.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Committed after Q1 and again at the end,
      not after each question**: Step 0, the foundations, the standing rule and Q1 went in one commit (`1b1e5300`)
      because the file closed at Q1; the after-the-stop facts, the computation and this audit went in the next.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock and the fold are the dispatching
      session's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top (file names only) and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `check_run.py` in the research folder); every filing
      fact carries its accession or the filing it came from; the peer ratios are flagged as XBRL transcription.
- [x] The order was kept; Q1 closed the file; everything after it is a fact recorded or a COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash flows, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price quote flagged as an aggregator.
- [x] Contrary evidence written down as found (the foundations and Q1); the facts for later questions under AFTER THE
      STOP; the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor rule applies.
- [x] `tools/run.py` produced no arithmetic line for this IFRS filer; none was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (2026-10-26); the run's own check,
      `python -I "Test Runs/_research 2026-10-26 PAM/check_run.py" <run file> principle_ledger_v5.csv`, PASS: no E-id, 35
      citations of 26 distinct ids all in the ledger, every quoted fragment beside an id found in that row.
- **Weak points, stated.** (1) The maintenance guess for a shale producer is depreciation; if wells must be replaced
  faster than depletion is booked, the top of the range is too high. (2) Tax: operating cash carries cash tax, which ran far
  below the tax charged; the tax-accrual variant is beside, not central. (3) Peer ratios are XBRL frames, not read from the
  peers' filed 20-Fs, and the peso reporters' frames mix restatement vintages. (4) The FY2016 to FY2018 20-Fs (the peso
  years, which cover the 2018 crisis on the filer's old basis) were not read; the 2018 and 2019 figures come from the FY2019
  and FY2020 20-Fs' US$ comparatives. (5) Q1 rests on the deciding part; the oil part, now taking most of the capital, was
  not given its own Q1 reading and would raise the commodity paragraph instead.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A price set by a government, not a market or an allowed return.** The text has a commodity paragraph (price
dependence never alone a STOP; the low-cost test at Q2) and a regulated-utility paragraph (an allowed return on invested
capital), and nothing for the business between them: a generator paid a per-MW price the Secretariat writes by resolution,
with no return on a rate base and no market. I placed it at Q1 by the key-variable tests, "If something is not very
predictable, forget it." **[M1998-044]** and "If something’s important but unknowable, forget it." **[M2006-076]**, and the
insiders' test, "They would say, “That’s too hard.”" **[M2000-105]**. The same facts could be read at Q2 as a "change for the better"
(the November 2025 market), which the convention credits only on a full cycle and sends to TOO HARD (NATURE) *with a dated
re-look condition*; a Q1 TOO HARD (NATURE) carries none. The two routes give the same box but treat the future differently,
and the text does not say which governs a deregulation that is under a year old. (2) **The parts threshold and the
equity-method convention use different bases.** Segment operating income, which decides the parts, includes the share of
investee profit (TGS, Transener, CTEB), while owner cash counts only the dividends; a part made mostly of equity-accounted
stakes can decide Q2 on profit it does not pay out. (3) **Tax in a dollar-functional filer that pays in pesos.** Cash tax
was a small fraction of the tax charged, a payment plan financed the 2024 tax, and the carryforward convention of Q7 (Whose
tax) does not cover a tax deferred by an installment plan; I kept cash tax central and showed the accrual beside, with the
plan outside net debt (CONVENTION of this run: a tax installment plan is not counted in net debt and is shown in the
tax-accrual variant instead; rationale: counting both the plan's principal and the accrued tax would charge the same tax
twice). (4) **The maintenance guess for a depleting asset.** The text accepts depreciation as the proxy "in most companies"
and names railroads as the exception; it is silent on shale wells, whose decline may need spending above booked depletion.
(5) **Tooling.** `tools/run.py` printed nothing for an IFRS 20-F filer, and `Screens/cover_shares.py` returned the 20-F
cover count, which a share cancellation in a later 6-K had superseded by 16 million shares; the brief anticipated both.
