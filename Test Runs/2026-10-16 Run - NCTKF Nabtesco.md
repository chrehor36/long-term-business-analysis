# Company Run: Nabtesco Corporation (TSE Prime 6268; US OTC NCTKF), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 1fe773ca). Every judgment cites a v5
ledger id in bold; every filing fact carries its document and date (Nabtesco is not an SEC filer, so the document, its
filing date and its page stand in place of an accession number; EDINET document numbers were not obtained, see
"What I could not get"). A STOP that returns OUT or TOO HARD closes the run; later questions are NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (cdfba0ac): `PORTFOLIO.md` read for this ticker only; not held.*

**Dispatch:** a dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the two departures the brief states
(primary documents are the company's own securities reports, not EDGAR; the lines of evidence derived by the analyst).

**Contamination declared (seen, not used):** (1) at the start I ran a file-name listing of `Test Runs/` filtered for
"nctkf", "nabtesco" and "6268" to check that my own run file did not already exist; it returned no file. That filtered
listing is a search across `Test Runs/` names, which the blind rule counts as opening; nothing was found and nothing was
opened. (2) The session's opening context showed the working tree's status and recent commit subjects: research folders of
other runs by ticker (AYI, ARCB) and five commit subjects about another company's run and fold. Not opened, not used. (3) The
memory index loaded into the session carries lines about the queue (a count of gate-clearers, "nothing buyable", "Japanese
names" owed) and the project map names the operator's sheet. None names this company; none was used.

**Lines of evidence (derived by me from the securities reports, as the brief asks).** From "Description of Business" and
the segment note (the 10-K Item 1 equivalent): the three reportable segments and "Others", the sub-segment sales by product,
the market shares the company states, the hydraulic equipment split and sale. From "Business Risks" (Item 1A): the
competition risk, the risks the company grades, and the material weakness. From "Management's Analysis" (Item 7): the
segment results and their causes, capital spending and its purpose, the ROIC target and result, cash flow causes, the
Harmonic Drive Systems share sale and its taxes. Added because the brief requires them: the TMT Machinery equity-method
error, the restatement of FY2021 to FY2025, the amended internal control reports, the auditor's role, and the delayed Q3
results.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** JPY 4,488, close 2026-10-16, TSE 6268 (Yahoo Finance chart API, an aggregator, flagged per operator rule 5;
  live quote only). The prior closes: 4,862 (10-13), 4,826 (10-14), 4,441 (10-15), the fall on 10-15 following the
  company's 2026-10-14 notice moving Q3 results to 2026-11-13.
- **Shares (one class, common):** 118,064,699 issued at 2026-06-30 and at 2026-08-14 (amended Semiannual Report FY2026,
  filed 2026-09-30, "Status of Shares", p.6), less 417,022 treasury shares held at 2026-06-30 (417,000 plus 22 in
  less-than-unit holdings, same report p.8), less 1,861,100 shares bought back 2026-08-03 to 2026-09-30 (company notice
  "Status of Acquisition of Own Shares", 2026-10-01) = **115,786,577 shares**. The company's own ratio checks it: the 4
  million share ceiling is "3.40%" of shares outstanding excluding treasury shares (117.65 million). Not deducted: 433,400
  shares held by the Stock Benefit Trust (BBT), counted as treasury under IFRS (0.4%, immaterial), and any purchases from
  2026-10-01 to today, not yet reported. `python Screens/cover_shares.py NCTKF` returned "NOT AN SEC REGISTRANT"; the count
  is by hand from the filed report.
- **Market cap:** JPY 4,488 x 115.79 million = **JPY 519.7 billion**.
- **Sovereign for the earnings currency (JPY):** 30-year JGB **4.02%**, 2026-10-15, Japan Ministry of Finance JGB curve
  (`jgbcme.csv`, via `python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4; English translations published by the company, the Japanese originals on EDINET
  prevail, which each translation states):
  - Amended Annual Securities Report FY2025 (23rd period), filed 2026-09-30 with the Kanto Local Finance Bureau, including
    the amended consolidated statements (pp.91-97), segment note 7 (pp.113-115), the error note "4. Additional
    information (1)" (p.108), KPMG AZSA's audit report dated 2026-09-30 and the Amendment to Internal Control Report
    (pp.200-203). The original FY2025 Annual Securities Report filed 2026-03-25 (MD&A, business risks, treasury stock,
    the hydraulic equipment note).
  - Amended Annual Securities Reports FY2024 and FY2023, filed 2026-09-30 (restated FY2022 to FY2024 statements and
    segments).
  - Amended Semiannual Report FY2026 (to 2026-06-30), filed 2026-09-30 (balance sheet, cash flows, shares, dividends,
    subsequent events, restatement note).
  - Earnings summaries (tanshin) for FY2016 to FY2025 (FY2017 tanshin carries the IFRS FY2016 comparatives), the
    2026-09-30 correction of the FY2025 tanshin and the 2026-08-14 and 2026-09-30 corrections of the FY2026 Q2 tanshin.
  - Company notices: 2026-09-30 "Notice of Filing Amended Annual Securities Reports..." (before and after figures by period),
    2026-09-30 "Notice Regarding Submission of Amendments to Internal Control Reports ... Material Weaknesses", 2026-10-01
    buyback status, 2026-10-14 Q3 date change. Results briefing FY2025 (2026-02-18) and FY2026 Q2 with script and Q&A
    (2026-08-04 to 08-06), referential sub-segment data 2026-02-12, IR Day 2026-09-07. Briefings are the company's own
    documents but not statutory filings; where they are used they are named.
  - Not read: the FY2026 convocation notice's pay tables and the corporate governance report (downloaded, not read,
    because the file closed at Q2 before Q5 and Q6).
- **One figure cross-checked against the filed statement:** operating cash flow FY2025 JPY 32,824 million in the amended
  ASR's consolidated statement of cash flows (p.97) equals the corrected FY2025 tanshin's cash flow line (32,824) and the
  original FY2025 tanshin (32,824); the restatement did not touch it.
- `python tools/run.py NCTKF`: "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE". No arithmetic lines; all arithmetic is
  by hand in `Test Runs/_research 2026-10-16 NCTKF/scripts/arith.py`, from the filed figures below.

**Owner cash by year (JPY million; IFRS; group as reported each year, hydraulic equipment inside through FY2024 and its
cash flows inside the FY2025 statement; FY2021 to FY2025 restated figures used where the restatement changed them, the
cash flow lines were not changed):**

| FY | Op. cash | Capex PPE + intangibles | Lease principal | Div. to minorities | Acquisitions, net | **Owner cash, all spending** | D&A | Maint. capex (guess) | **Owner cash, maintenance only** |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 27,730 | 15,394 | 0 | 14 | 778 | **11,544** | 7,422 | 7,422 | 20,294 |
| 2017 | 23,071 | 12,193 | 0 | 264 | 8,203 | **2,411** | 8,974 | 8,974 | 13,833 |
| 2018 | 24,165 | 21,490 | 0 | 340 | 0 | **2,335** | 10,011 | 10,011 | 13,814 |
| 2019 | 38,433 | 14,763 | 2,477 | 674 | 0 | **20,519** | 13,093 | 10,616 | 24,666 |
| 2020 | 34,203 | 18,697 | 2,547 | 1,215 | 0 | **11,744** | 13,730 | 11,183 | 19,258 |
| 2021 | 36,340 | 9,299 | 2,522 | 2,928 | 746 | **20,845** | 13,266 | 10,744 | 20,146 |
| 2022 | 7,717 | 11,368 | 2,854 | 3,101 | 0 | **-9,606** | 14,483 | 11,629 | -9,867 |
| 2023 | 11,177 | 25,599 | 3,060 | 1,563 | 9,933 | **-28,978** | 15,469 | 12,409 | -5,855 |
| 2024 | 26,650 | 28,351 | 3,424 | 1,249 | 0 | **-6,374** | 16,469 | 13,045 | 8,932 |
| 2025 | 32,824 | 16,015 | 3,669 | 2,610 | 0 | **10,530** | 17,258 | 13,589 | 12,956 |

Sources: FY2016 to FY2023 from the tanshin cash flow statements (FY2017, FY2019, FY2021, FY2023 tanshin, each with its
prior year); FY2024 and FY2025 from the amended FY2025 ASR p.97. Japanese IFRS cash flows put interest and taxes paid
inside operating cash, so owner cash is after the company's own tax and after interest. Equity-method income enters only
as dividends received (inside operating cash), as Q4's equity-method paragraph requires. Leases: before IFRS 16 (FY2016 to
FY2018) lease costs sat inside operating cash; from FY2019 the principal is deducted. The maintenance guess is
depreciation and amortization less right-of-use depreciation, the latter taken equal to lease principal paid (CONVENTION
of this run; rationale: the filing gives both, the principal is deducted separately, and the filed right-of-use
depreciation of FY2024 and FY2025, 3,258 and 3,381, is a little below the principal, so the guess errs toward the
company). FY2022 and FY2023 operating cash carries the income tax on the Harmonic Drive Systems share sale: the filer
names "the payment of income taxes" as the main negative factor in both years (FY2022 and FY2023 tanshin, p.5).
Ten-year averages: all spending 3,497; maintenance only 11,818. Literal window FY2021 to FY2025: all spending -2,717;
maintenance only 5,262.

**The balance sheets, ten years, before the income account [M2025-032] (JPY million, year-end; FY2021 to FY2025 restated):**

| FY | Cash | Receivables | Inventories | PPE | Goodwill | Intangibles | Equity-method inv. | Total assets | Borrowings | Equity (parent) | Sales | Op. income |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 41,780 | 65,569 | 32,704 | 63,155 | 14,361 | 2,671 | 15,952 | 256,973 | 16,949 | 147,929 | 244,968 | 25,982 |
| 2017 | 44,121 | 76,874 | 40,298 | 70,700 | 21,310 | 5,850 | 20,184 | 301,557 | 27,720 | 167,537 | 282,422 | 29,468 |
| 2018 | 54,039 | 74,952 | 43,592 | 80,573 | 15,512 | 5,076 | 29,641 | 328,568 | 45,310 | 178,702 | 294,626 | 21,889 |
| 2019 | 58,686 | 69,175 | 41,257 | 87,083 | 14,161 | 5,127 | 31,952 | 344,558 | 43,936 | 187,398 | 289,808 | 25,320 |
| 2020 | 64,665 | 74,632 | 36,505 | 89,522 | 14,658 | 3,905 | 34,887 | 351,723 | 39,866 | 198,031 | 279,358 | 28,533 |
| 2021 | 112,771 | 74,957 | 41,880 | 89,020 | 16,184 | 4,251 | 15,475 | 483,653 | 17,587 | 241,372 | 299,641 | 29,669 |
| 2022 | 124,413 | 77,227 | 49,236 | 95,901 | 18,025 | 6,554 | 20,080 | 462,440 | 19,943 | 251,250 | 309,123 | 18,654 |
| 2023 | 77,835 | 82,167 | 50,969 | 107,527 | 25,750 | 11,624 | 24,005 | 428,630 | 21,573 | 262,721 | 333,367 | 16,660 |
| 2024 | 74,476 | 88,932 | 53,273 | 114,340 | 26,259 | 12,955 | 24,348 | 449,845 | 31,884 | 272,559 | 323,384 | 15,012 |
| 2025 | 73,340 | 75,421 | 52,838 | 101,683 | 25,817 | 13,477 | 24,976 | 466,632 | 44,985 | 273,466 | 307,912 | 20,956 |
| H1 2026 | 99,583 | 65,763 | 57,870 | 99,601 | 26,111 | 12,735 | 33,924 | 456,867 | 43,427 | 284,971 | (H1) 167,401 | (H1) 15,759 |

(FY2024 sales and operating income include hydraulic equipment as restated in the amended FY2024 ASR; FY2025 is
continuing operations, with JPY 43,665 million of hydraulic assets held for sale. FY2021 total assets, equity, sales and
operating income are the "after correction" figures of the company's 2026-09-30 notice; its other FY2021 lines are the
original FY2021 tanshin.)

What the balance sheets say. Equity attributable to the parent rose from 147.9 to 273.5 billion in nine years (+85%), while
operating income went from 26.0 to 21.0 billion: the capital nearly doubled and the operating profit did not grow. Part of
the equity came from the Harmonic Drive Systems stake (a JPY 125.1 billion valuation gain in FY2021 on leaving the equity
method, partly reversed by a 57.0 billion valuation loss the same year, then sold in 2022 and 2023), not from operations.
Plant rose from 63.2 to 101.7 billion (114.3 before the hydraulic assets were moved out), goodwill and intangibles from 17.0
to 39.3 billion (OVALO, Germany, 2017; Deep Sea Technologies, Greece, 2023; Gilgen Door Systems, bought before the
window, carries 19.7 billion of the goodwill). Inventories rose faster than sales: 13.4% of sales in
FY2016, 17.2% in FY2025 (continuing). Receivables held near a quarter of sales. Debt is small against cash every year.
Retained earnings fell in FY2025 (219.4 from 225.3) because 10.4 billion of retired treasury stock was charged to them. What
the figures cannot say: the equity-method line was understated for years and nobody noticed until April 2026 (Q4 facts
below), so the balance sheet's equity-method line is only as good as a control the company now calls a material weakness.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would own this if the market closed for five years **[M1997-109]**, and the
quotation itself instructs nothing **[M2006-077]**. No macro view enters: the robot capital-spending cycle in China and Korea
is read only through the company's own figures, never forecast **[M2000-094]**. Two foundations bear hardest. Who is paid to
tell you: the company's market shares (about 60% of medium and large robot joints) are its own estimates, printed in its own
briefing. And the currency: for a dollar holder a yen share is in part a currency position, which the rows call "a bet on
how government now, and in the future, will behave" **[M2011-025]**. **Contrary evidence, written down as found**
**[M1997-127]**: the strongest evidence for the business is the stated world share in robot reducers held since the 1980s and
the Fanuc, Yaskawa, KHI, KUKA and ABB customer list; the strongest against is in Q2 and in the facts after the stop.

## THE STANDING RULE
Owning a small part-interest, unlevered and paid in cash, cannot ruin the buyer; the rule forbids borrowed money in the
investor's own kit, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and nothing in this purchase
requires it. Clear.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **The test** **[M1995-051]**, **[M2012-065]**: a reasonable fix on earning power and competitive position in five or ten
  years. The products are mechanical and electro-mechanical components with long design lives: cycloidal precision
  reduction gears for robot joints (FY2025 external sales JPY 78.6 billion), rail brakes and doors (29.5), aircraft flight
  control actuators (25.7), marine engine controls (25.4), truck brake parts (12.6), automatic doors and platform doors
  (110.7), packaging machines (16.5) (amended FY2025 ASR, note 25, p.148). None is a fast-changing technology in the sense
  of **[M1998-008]**; the RV reducer the company sells today is the design family it has sold for decades.
- **Key variables** **[M1998-044]**: robot makers' capital spending and the reducer's share of their joints; rail car and
  aircraft build rates; Japanese construction for doors. They are cyclical but not unknowable; the economic dynamics of each
  field can be read from the figures, which is the test, not the chemistry or the gearing **[M2011-014]**.
- **Abroad** **[M2000-141]**: Japanese IFRS reporting and governance are readable from the translated securities reports;
  the Japanese original prevails and was not read (noted under what I could not get).
- **Parts** (Q1's holding-company paragraph): the deciding part (Q2's parts table) is the Component Solutions segment; its
  economics are understandable as above.
- **Doubt** **[M2002-092]**: my doubt is not whether I understand what the business is or how it earns; it is whether its
  castle holds, which Q2 owns.
- **VERDICT: IN.**

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table (CONVENTION of section B: a part decides at more than half of five-year operating profit, else the
largest).** Segment income as each year's filing reports it (FY2022 to FY2024 restated, FY2025 continuing), JPY million:

| Part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Five-year | Share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Component Solutions (reducers; hydraulics to FY2024) | 22,903 | 15,948 | 10,376 | 4,523 | 5,420 | 59,170 | 39.0% | below | **yes (largest)** |
| Transport Solutions | 5,617 | 6,714 | 7,828 | 12,389 | 13,698 | 46,246 | 30.5% | not judged | no |
| Accessibility Solutions | 7,642 | 3,358 | 5,451 | 9,340 | 9,541 | 35,332 | 23.3% | not judged | no |
| Others (packaging etc.) | 2,736 | 1,484 | 3,385 | 1,043 | 2,194 | 10,842 | 7.2% | not judged | no |

Sources: FY2021 tanshin (original, the FY2021 restatement changed group operating income by -348 and no restated segment
table was read); amended FY2023 ASR (FY2022); amended FY2024 ASR (FY2023, FY2024); amended FY2025 ASR (FY2025). No part
carries half, so the largest decides. Caution written down: hydraulic equipment (now 70% sold) sat inside Component to FY2024
(it earned 1,856 in FY2024, by difference between the FY2024 and FY2025 presentations); with its earlier years removed,
Component and Transport may stand near level, and I could not split FY2021 to FY2023 between reducers and hydraulics. Either
part read alone would leave the field-returns finding below unchanged for the reducer part; Transport's castle was not
judged and is the open point if a later reader puts the hydraulic years out (see "What in the framework was wrong").

**The castle tests on the deciding part, each with its filing fact.**
- *What keeps it standing* **[M1995-038]**: the company states "Approx. 60" percent world share in joints of medium and
  large industrial robots (FY2026 Q2 briefing, p.28, "The market share is estimated by Nabtesco"); the customers are the
  large robot makers. The business has "a wide lineup of products with high market shares", and its own risk section says
  a fall in share from "the development of new products by other companies" could hurt it (FY2025 ASR, Business Risks,
  item 6).
- *Pricing power and the agony before a rise* **[M2005-020]**: through the inflation of 2022 to 2025 the segment's margin
  fell from 16.3% (FY2021, with hydraulics) to 3.9% (FY2024, reducers alone, the company's own figure) and 6.8% (FY2025).
  The company's own margin bridge puts price pass-through at +1.3 points against inflation of -0.6 points for FY2025, and
  in its FY2026 plan +0.6 points against -0.6 points, price only offsetting cost; for H1 2026 the price effect was "JPY
  0.5 billion" on about 45.5 billion of segment sales (FY2025 briefing p.32, "CMP Benefit Analysis"; FY2026 Q2 Q&A item 8). A strong position passes
  costs through over time **[M2005-017]**; this one passed through a little, late.
- *Unit volume*: reducer sales 89.7 (FY2022), 91.6 (FY2023), 65.9 (FY2024; 66.9 in the FY2025 presentation), 78.6 (FY2025)
  billion (amended ASRs, revenue notes). The FY2024 fall is the robot makers' inventory adjustment on the filer's own description; it is cyclical.
- *The money test and the attacker* **[M2011-015]**: the filings name no rival. In the half of the same segment that the
  company has just sold, its own words say the castle was open: "the competitive environment has remained challenging due
  to the rise of local Chinese hydraulic equipment manufacturers and the increasing in-house production by construction
  machinery manufacturers" (FY2025 ASR, note on the company split). For the reducer half the filings say nothing either way
  about Chinese entrants; no instance found in the documents read.
- *Widening or narrowing* **[M1999-108]**, **[L2005-010]**: the segment's pre-tax return on its own segment assets ran
  16.1%, 22.6%, 18.9%, 14.9%, 14.7%, 20.3%, 12.9%, 7.6%, 3.1% and 4.9% from FY2016 to FY2025 (segment income over year-end
  segment assets: 69,545 rising to 145,190 in FY2024, then 109,769 for reducers alone in FY2025). Each trough is deeper
  than the last (14.9% in FY2019, 3.1% to 4.9% in FY2024 and FY2025) and the last peak (20.3%) did not reach the one
  before (22.6%), while the capital in the segment roughly doubled. On the evidence the moat is narrowing, not widening.
- *What could destroy it* **[M2000-014]**: the customers are few and large; the filings name five robot makers. No row
  supplies a test for a few strong buyers; noted, not weighed.

**The competitor row (CONVENTION of this run: the filings name no competitor, so I chose the one rival in the deciding
part's field that publishes its own primary figures; rationale: no reducer maker files with the SEC, and Harmonic Drive
Systems, maker of the strain-wave gears used in robot joints, publishes its results on its own IR site).** Harmonic Drive
Systems Inc. (TSE 6324), fiscal years to March, from the chart data on its own IR highlights page (www.hds.co.jp, data
compiled by its IR vendor from its earnings announcements; flagged, not a filed statement; five years only):

| FY to March | Sales | Operating income | Margin | ROE |
|---|---|---|---|---|
| 2023 | 71,527 | 10,225 | 14.3% | 7.5% |
| 2024 | 55,796 | 125 | 0.2% | -27.1% |
| 2025 | 55,646 | 7 | 0.0% | 4.4% |
| 2026 | 59,558 | 2,568 | 4.3% | 2.0% |

Nabtesco over the same span (calendar FY2022 to FY2025, restated): operating margin 6.0%, 5.0%, 4.6%, 6.8%; return on
average parent equity 4.2%, 5.5%, 3.8%, 5.6%. Over its whole ten years (FY2016 to FY2025) Nabtesco's return on average
equity was 13.0%, 15.9%, 12.1%, 9.8%, 10.6%, 29.5% (the Harmonic gain year), 4.2%, 5.5%, 3.8%, 5.6%; about 9% leaving out
FY2021. The company's own ROIC was 3.8% (FY2024) and 4.4% (FY2025) against its medium-term target of "ROIC 10% or over"
(FY2025 ASR, MD&A ④; FY2025 briefing p.13). Flagged rivals not read: the Chinese reducer makers (not named in any filing,
reports in Chinese), and the rivals of the non-deciding parts.

**The field's returns over the last full cycle, judged in words (section C, no figure).** The reducer field went through two
full robot cycles in this span (troughs FY2019 and FY2024). Over them the deciding part earned good pre-tax returns on its
assets at the peaks and poor ones at the troughs, falling at each turn, and the whole company earned about ordinary returns
on its equity across the ten years and poor ones for the last four, below its own target every year it has had one. The one
rival whose figures I could read did the same or worse. The castle is standing, the share is high, and the returns it
protects are ordinary: a moat is what "protects excellent returns on invested capital" **[L2007-004]**, and a field can have
few players and still make poor returns, "you can have only two competitors and they’re still terrible businesses"
**[M2013-052]**. This is not the tenuous moat whose value cannot be judged **[M2000-019]**: the returns are known from the
filings, and the convention sends the standing castle that protects only ordinary returns to OUT, judged as the rows say a
moat is judged, not measured **[M1999-108]**. The half of the segment the company has sold was, on its own words, a castle
already open.

- **VERDICT: OUT.** The deciding part's castle stands but protects only ordinary returns over the last full cycle, on the
  filer's own figures and the one rival read, and is narrowing. The file closes here.

## Q3 to Q12: NOT REACHED (operator rule 2). Facts already found are below, not weighed.

---
## THE BOX
**OUT, at Q2** (the deciding part, Component Solutions, protects only ordinary returns over the last full cycle and is
narrowing; the hydraulic half of the same segment shown open on the filer's own words). COMPUTATION, NOT A CLEARANCE: value
range JPY 1,204 to 2,991 a share (all-equity) against JPY 4,488. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.*

**Bearing on Q3 (capital):** equity attributable rose 85% (147.9 to 273.5 billion) over FY2016 to FY2025 while operating
income fell from 26.0 to 21.0 billion (table in Step 0). Capital spending ran above depreciation in most years
(capex 16.0 to 28.4 billion against D&A 13.3 to 17.3 billion in FY2021 to FY2025); FY2023 and FY2024 spending was "primarily
for capacity expansion" in precision reduction gears (FY2025 ASR MD&A ③). The FY2026 plan is 12.5 billion of capex.

**Bearing on Q4 (the accounts):**
- *The TMT Machinery error.* TMT Machinery, Inc. (33% owned, unlisted, no consolidated statements) was accounted for from
  its standalone statements, so the profits of its own subsidiaries never reached Nabtesco's equity-method line. The
  company learned of it in April 2026 from a JPY 600 million gain at TMT; the unrecognized cumulative amount grew to about
  JPY 2.8 billion as the auditor's review proceeded (amended FY2025 ASR, "Reasons for Filing", p.2).
- *How it was first booked.* In the Q1 and the original Q2 2026 results the company booked the prior-period profits in
  current earnings: equity-method income of JPY 3,177 million in the H1 2026 summary of 2026-07-31, corrected to 1,488 on
  2026-08-14. The correction notice says that when the releases were prepared "both shared the understanding that the final
  amount would be recognized in the current fiscal year's earnings", and that "the independent auditor and the Company
  concluded that it would not be appropriate to recognize the entire amount in the current fiscal year"; the semiannual
  report says the restatement was made "based on the indication by the independent auditor". The Semiannual Report
  scheduled for 2026-08-07 was filed 2026-08-14. The full-year forecast was revised and the JPY 15 billion buyback announced
  on 2026-07-31, the day of the uncorrected H1 summary.
- *The restatement.* Annual reports FY2021 to FY2025, two quarterly and three semiannual reports amended on 2026-09-30,
  "In addition, certain items that had not been corrected previously due to immateriality have also been corrected at this
  time" (notice of 2026-09-30). Effects on net income attributable: FY2021 -47 (-0.1%), FY2022 +951 (+10.0%), FY2023 -328
  (-2.3%), FY2024 +69, FY2025 -440 (-2.8%); on operating profit: FY2023 -716 (-4.1%), FY2025 +230. The "other errors"
  moved operating profit, which the equity-method error cannot do.
- *Material weakness.* Amended internal control reports for FY2021 to FY2025 now say internal control over financial
  reporting "was not effective"; "the material weakness required to be disclosed has not yet been remediated" (Amendment to
  Internal Control Report, 2026-09-30). The Q3 2026 results move from 10-30 to 11-13 because an auditor's review report is
  now required (notice 2026-10-14).
- *An inconsistency in the English filing.* In the amended FY2025 ASR, KPMG AZSA's report dated 2026-09-30 carries an
  internal control audit opinion that the company's report "which states that Nabtesco Corporation's internal control over
  financial reporting as of December 31, 2025 was effective, present fairly" (p.193), while the amended internal control
  report in the same document says the opposite (p.202); the same wording stands in the amended FY2024 and FY2023 reports.
  The amended internal control report also opens by naming "the Internal Control Report for the 22nd fiscal year" (FY2024)
  while amending the 23rd. The Japanese originals prevail and were not read; whether this is a translation copy or the
  filed opinion is not known to me.
- *Other accounting facts.* Goodwill impairments and write-offs narrated by the company: Deep Sea Technologies (bought
  2023-07-14 for about JPY 7.8 billion, goodwill impaired by 989 million in FY2025; "the time to market and launch was later
  than originally planned", FY2025 briefing p.31); Gilgen Door Systems goodwill 19.7 billion tested without impairment, a key
  audit matter; FY2023 impairments 6.2 billion; the sale of a European rail subsidiary (December 2023) and a 1.3 billion loss
  on liquidating rail subsidiaries in FY2025. Inventories rose from 13.4% to 17.2% of sales over the decade.

**Bearing on Q5 (integrity, not judged here):** the facts above under Q4 (the current-year booking of prior-period profit,
reversed at the auditor's indication; the uncorrected H1 summary on the day of the buyback announcement and forecast
revision; the "other errors" carried as immaterial until now; the unremediated material weakness; the inconsistent English
auditor's opinion). The company apologized in its Q3 date notice. The company sets and reports against a medium-term ROIC
target (10%) and publishes annual forecasts and revisions (notices of 2026-04-30 and 2026-07-31); the rows weigh guidance
and targets at Q4 and judge them at Q5 **[M2004-067]**. Any later run that reaches Q5 must answer these first
**[M2013-088]**.

**Bearing on Q6 (money and owners):** buybacks: 2,999,400 shares for JPY 9,999.8 million in August to December 2025
(average about JPY 3,334; FY2025 ASR, treasury stock), and 1,861,100 shares for JPY 8,577.6 million in August and
September 2026 (average about JPY 4,609; notice 2026-10-01), under programmes that name a share count and a yen ceiling
but no price; all bought shares are cancelled. Average prices paid stand above the top of the COMPUTATION range below
(JPY 2,991); the programme's test **[L2016-002]**, **[L1999-023]** is not applied because Q6 was not reached. Shareholder
return policy "Approx. DOE 3.5%", total payout "102%" in FY2026 if the buyback completes (FY2026 Q2 briefing). The hydraulic
sale proceeds (JPY 11.9 billion received in H1 2026) and the buyback are funded from cash; short-term borrowings rose by
12.6 billion in FY2025.

**Bearing on Q9 (debt):** at 2026-06-30 borrowings JPY 43.4 billion (almost all short-term) against cash of 99.6 billion
and 3.8 billion of other current financial assets; lease liabilities 14.3 billion. Net cash about 46.6 billion after the
August interim dividend (4,824 million, stated in the semiannual report) and the August to September buyback.

### COMPUTATION, NOT A CLEARANCE: Q7's range and the two reporting figures
*(The file closed at Q2. These figures are arithmetic for the operator's reporting convention, not a value judgment, not a
clearance and not entry language, operator rule 3. Built by Q7's range convention.)*

- **Inputs.** Owner cash after every real cost, as tabled in Step 0, after the company's own tax **[L2021-003]**: the
  company gets credit "for whatever net cash is left every year" **[M1998-080]**. Value is "the discounted value of the cash
  that can be taken out of a business during its remaining life" **[R1996-018]**, at the long government rate
  **[L2000-021]**: JGB 30-year 4.02%.
- **(a) Cycle base.** The literal window FY2021 to FY2025 holds two aberrational years on the filer's own description
  (FY2022 and FY2023, operating cash cut by income tax on the Harmonic share sale) and a trough year (FY2024)
  **[L2005-003]**. The owner-cash series has no clean cycle of its own; the deciding segment shows two full robot cycles in
  FY2016 to FY2025, so the base is the ten-year average (CONVENTION of this run, in those words; rationale: (a) asks for the
  last full cycle, the owner-cash series is too erratic to date one, and ten years covers the segment's two). Literal
  window shown beside.
- **(b) Decline and sign change.** First half FY2016 to FY2020: all-spending 9,711, maintenance 18,373 a year; second half
  FY2021 to FY2025: -2,717 and 5,262. The all-spending series changes sign, so the growth rate is meaningless and the range
  is the no-growth case alone, said so.
- **(c) Acquisitions.** Deducted in the all-spending case (19,660 over ten years: Nabco Systems 2016, OVALO 2017, Deep Sea
  2023 net of a disposal, a small one in 2021), with no growth credited. Purchases are 36% of owner cash before purchases over ten years, under
  half, so the serial-acquirer specific does not apply.
- **(d) Working capital** is inside operating cash.
- **(e) Maintenance case.** The filing allows the guess (capex stated as "primarily for capacity expansion"; depreciation as
  the proxy **[M1998-127]**, the guess disclosed **[M2000-144]**). The growth spending bought no growth (owner cash and
  operating income both lower at the end), so by (e) the maintenance-only no-growth case is the top and the all-spending
  case the bottom: "growth can destroy value" **[L2000-023]**.
- **(f) The cap** does not bind (no growth carried).
- **All-equity basis** **[L2017-004]**: owner cash before interest (adds back interest paid after tax, 233 a year) against
  market value plus net debt; net cash JPY 46,597 million (cash 99,583 and other current financial assets 3,843, less
  borrowings 43,427, at 2026-06-30, less the August interim dividend 4,824 stated in that report and the August to September
  buyback 8,578 stated in the company's 2026-10-01 notice). Lease liabilities (14,264) left out, said so: their principal is
  already deducted inside owner cash. Non-current investment securities (20,051) left out.

| Case (no growth, 4.02%) | Owner cash a year | Whole business | Per share, all-equity | Per share, equity-only |
|---|---|---|---|---|
| Top: maintenance only, ten-year | 11,818 (+233) | 299,776 + 46,597 | **2,991** | 2,539 |
| Bottom: all spending, ten-year | 3,497 (+233) | 92,786 + 46,597 | **1,204** | 751 |
| Literal window FY2021-25, maintenance only (beside) | 5,262 | | about 1,583 | |
| Literal window FY2021-25, all spending (beside) | -2,717 | | not positive | |

- **The floor, tested first.** At JPY 4,488 the whole business costs about JPY 473 billion net of cash. The top case yields
  2.55% on it and the bottom case 0.79%, against the floor of about 10% **[M2003-149]**. No case in the range earns the floor
  at the price. Width 2.5 to 1. The price sits above the top of the range.
- **Variant beside (a disclosed guess, not central):** adding back an estimated JPY 20.2 billion of tax on the Harmonic gains
  (the filer's statutory rate of 30.6%, FY2025 ASR tax note, applied to about 66.0 billion of net Harmonic gains built from
  the filer's figures: the FY2021 valuation gain of 125,107 less the FY2021 valuation loss of 56,958 in that year's cash
  flow statement, the FY2022 net loss of 5,616 and the FY2023 gain of 3,485; the build is a CONVENTION of this run, a
  disclosed guess, rationale: the filer gives no tax split) lifts the range to JPY 1,638 to 3,425; still below the price,
  and no case earns the floor.
- **Fair price (Part VII; each end at 10%, averaged, all-equity less net debt): JPY 1,084 a share** (ends 1,443 and 725).
  Equity-only figure beside: JPY 661. The central figure is the all-equity one. Tax treatment: owner cash after the
  company's own tax, no conversion. No cheap price is reported.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 1fe773ca); written question by question; committed after each
      question that closed (Q1 and Q2 committed together with the facts, as the run closed at Q2; see below).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's. The run binds
      only once folded into the register by the dispatcher (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. One filtered name listing of `Test Runs/` was run at the
      start and found nothing; declared under contamination with what the session context showed.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `scripts/check_ids.py` in the research folder); every
      filing fact names its document and date; no accession numbers exist for this non-SEC filer and no EDINET numbers were
      obtained (declared).
- [x] The order was kept; Q2 closed the file OUT; everything after it is headed COMPUTATION or written as facts not weighed.
- [x] Owner cash after every real cost from the filed cash flow statements, never a net-income proxy; the sovereign from the
      Ministry of Finance; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found; the facts for later questions are under AFTER THE STOP, with the integrity
      flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` gave no arithmetic lines (non-SEC); nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before the commit (recorded in the final commit).
- Honest gaps: the Q1 commit was not made separately from Q2 (the two were written together once the parts table was
  built); the parts table's FY2021 row is unrestated; the hydraulic split of FY2021 to FY2023 is unknown; only one rival
  was read, for five years, from chart data on its IR page rather than its filed statements.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) Section B's parts threshold counts "five-year operating profit" of the parts as reported, but says nothing
about a part sold or discontinued inside the window. Here the largest part, Component Solutions, carried a hydraulic
business through FY2024 that is now 70% sold; on the filed basis Component decides at 39%, but with the sold business taken
out of the earlier years it may stand level with Transport Solutions, whose castle I did not judge. I read the parts as
filed and said so; the text should say whether a discontinued operation is removed from the five-year count. (2) Q7's
specific (a) says the series that defines the cycle is owner cash as Q4 recasts it, but owner cash for a business with
lumpy capacity spending, an acquisition and a one-off tax bill may not show a cycle at all, while the segment profit shows
two clean ones; I used the ten-year average and confessed it as a CONVENTION of this run. (3) Section C's "ordinary"
returns test asks for the rivals' own filings over a full cycle; for a Japanese field none of whose rivals files with the
SEC and whose Chinese rivals report in Chinese, the one rival I could read gave five years from its IR site's chart data,
not a filed statement. The test worked here because the filer's own ten years were enough to see the returns; the text
does not say whether the filer's own full cycle suffices when the rivals' cannot be read.
