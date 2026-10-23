# Company Run — CenterPoint Energy, Inc. (NYSE: CNP) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form: `Test Runs/_TEMPLATE - Company Run.md`,
copied to this dated file before any fetch. Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the one departure the
brief states: the lines of evidence were derived by the analyst from the 10-K's Item 1, Item 1A and Item 7 (listed in Step 0).
Working folder: `Test Runs/_research 2026-10-18 CNP/` (notes, the tool outputs, the arithmetic script, the citation check).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared and not used.** (1) Listing `Test Runs/` to check that no CNP file of today existed showed the file names of
other runs dated 2026-10-18 (twenty names, among them other gas and electric utilities); no file was opened. (2) The session's git
status and recent commit subjects named another company's run and its box (BEP, OUT at Q7). (3) The memory index loaded into the
session carries a line on the queue state (a count of gate-clearers and "nothing buyable"). (4) The adopted rule file
`Framework/v5/CASE 2026-10-18 - the regulated utility's fair price, decided from the corpus.md`, read for Q7's method, names sixteen
utilities run on 2026-10-17 and 2026-10-18 that closed OUT at Q7. None of this bears on CNP's filings and none of it is used below.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $40.55 (close 2026-10-16, the last close before this Sunday run; from `tools/run.py`, an aggregator, live quote only, flagged per operator rule 5).
- **Shares by class:** 658,720,288 common shares outstanding, excluding 166 treasury shares, on the cover of the 10-Q for the quarter to
  2026-06-30 (filed 2026-07-28, accession `0001130310-26-000041`; `python Screens/cover_shares.py CNP`). The two counts of 1,000 shares on
  the same cover are the common stock of the subsidiary co-registrants, all held inside the group, not CNP classes; there is one class.
  Cross-check: the 10-Q balance sheet shows 658,700,905 shares outstanding at 2026-06-30. The 8-Ks filed after the 10-Q (2026-07-31
  notes, 2026-09-09 credit facilities, 2026-09-14 data incident, 2026-10-01 Ohio closing) and the 424B5 of 2026-07-30 (junior
  subordinated notes) issue no common shares. **Pending:** forward sale agreements of May 2025 on 24,864,865 shares, to be settled on or
  before 2027-02-25 for about $910 million (10-Q, Note 15); shown beside the per-share figures, not in the central count.
- **Market cap:** 658.72M x $40.55 = **$26,711M** (with the forward shares: 683.59M shares, and the $910M they bring).
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-19, accession `0001130310-26-000008`): Item 1, Item 1A, Item 3,
  Item 7, the statements, Notes 4, 7, 11, 12, 14 and 16, and the Houston Electric statements; the 10-Ks for FY2023
  (`0001130310-24-000010`) and FY2021 (`0001130310-22-000023`) for the cash flows, segments and Houston Electric figures of 2019 to 2023;
  the 10-Q for 2026-06-30 (`0001130310-26-000041`); the proxy (DEF 14A, filed 2026-03-04, `0001104659-26-023457`); the 8-Ks of
  2026-02-12 (`0001104659-26-014406`), 2026-02-26 (`0001104659-26-020626`, convertible notes), 2026-07-28 with its press release
  (`0001104659-26-087279`), 2026-07-31 (`0001104659-26-089263`), 2026-09-09 (`0001104659-26-106356`), 2026-09-14
  (`0001104659-26-107560`) and 2026-10-01 (`0001104659-26-112565`); the 424B5s of 2026-05-15 (`0001104659-26-062746`, the $1 billion
  at-the-market and forward programme) and 2026-07-30 (`0001104659-26-088494`).
  **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025, $2,486M on the filed
  Statement of Consolidated Cash Flows (10-K FY2025), equal to the XBRL figure `tools/run.py` printed.
- **`python tools/run.py CNP`, arithmetic lines only** (saved as `run_py_output.txt` in the research folder): operating cash 2023 to 2025
  of $3,877M, $2,139M, $2,486M; capital spending $4,401M, $4,513M, $4,870M, plus the $357M Posey Solar asset purchase in 2025; D&A
  $1,401M, $1,439M, $1,530M; stock pay not found in XBRL (the cash flow statement carries no separate stock-pay line; the gap is
  declared at Q4, not filled). Owner cash after all capital spending is negative in each of the three years (mean -$1,761M; -$1,880M
  with the asset purchase). The tool's balance-sheet table is checked at Q4 against the filed statements; its debt table sums a non-debt
  line (d6, liabilities other than long-term debt) and is not used.
- **The lines of evidence this name needs, derived from the 10-K** (the brief's departure): from **Item 1**, the parts and their
  regulators (Houston Electric under the PUCT, Indiana Electric under the IURC, the gas utilities under four states), the exclusive
  certificated territories, the customers (REPs for Houston Electric) and the divestitures (Louisiana and Mississippi 2025, Ohio 2026);
  from **Item 1A**, rate regulation and regulatory lag (the 2024 Houston Electric case), the TEEEF procurement and the $800 million that
  officials argued shareholders should bear, severe weather and Hurricane Beryl, the financing of the 10-year plan, the REP receivable
  concentration; from **Item 7**, the $65.5 billion capital plan (raised to $66.7 billion in the 2026-07-28 release), the rate case
  outcomes (allowed ROE and capital structure), the debt and equity raised and the securitizations, and the non-GAAP EPS guidance.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: would I be content to own this "if the market closed for five years"
**[M1997-109]**, on the cash the business itself produces. The second is who is paid to tell you: the company's ten-year capital plan
and its 7 to 9 percent non-GAAP EPS growth outlook through 2035 (proxy letter, DEF 14A 2026) are a seller's projection of what it
sells, and the speakers have "never looked at a projection" **[M1995-050]**; "you do not get impartial advice" where fees ride on one
answer **[M2020-037]**. No macro view of rates or of data-center demand enters **[M2000-094]**; the load forecast is the company's claim,
not a fact. **Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after capital spending was negative in each of
the last three years, the gap closed by $3.7B to $6.0B of new long-term debt a year, by divestitures and by forward equity; (2) Houston
Electric's return on its own equity fell from about 11.8% (2022) to about 7.9% (2025) while its parent put $3.1B of equity into it over
2021 to 2025 (Houston Electric statements, FY2025 and FY2023 10-Ks); (3) the 2024 Houston Electric rate case ended in a $47M revenue cut
and a 9.65% ROE against 10.4% asked; (4) after Hurricane Beryl, officials argued shareholders should pay about $800M of TEEEF costs, and
a complaint to end TEEEF recovery is still open (Item 1A); (5) pay is tied to non-GAAP Adjusted EPS, relative TSR and a P/E modifier
(proxy); (6) a theft of customer data was reported on 2026-09-14 (8-K).

## THE STANDING RULE
The buyer's conduct: a part-interest bought for cash in a listed share, no borrowed money, no option given, nothing that can call
**[M2012-081]**, **[L2014-024]**. Nothing in this purchase puts the buyer at risk of ruin, provided it is bought with money the buyer
has and does not need. The target's own debt is Q9's, not this rule's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from Item 1.** A utility holding company whose parts are regulated monopolies: Houston Electric (transmission and
  distribution only, 2.86M metered customers served through 67 REPs, rates set by the PUCT); Indiana Electric (SIGECO, vertically
  integrated, 154k customers, IURC); and the gas distribution utilities (4.03M customers in Indiana, Minnesota, Texas, and Ohio until
  2026-10-01). The Electric segment carried 58% of five-year operating income 2021 to 2025 (Q2's parts table).
- **The key variables and whether they are foreseeable**, "evaluating how predictable they were first" **[M1998-044]**: the rate base
  (what is spent and allowed), the allowed return and equity share (set in rate cases: Houston Electric 9.65% ROE on a 43.25% equity
  share from the 2025 order; Indiana Electric 9.8% on 55%; Ohio 9.79%; 10-K Item 7), regulatory lag and disallowances, storm
  restoration costs and their securitization, and load growth. "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]** is available for the first four: the earning power of a regulated wires
  and pipes business is an allowed return on a rate base, and what is needed is to "understand the economic dynamics of the industry"
  **[M2011-014]**, not the engineering. The fifth, load growth from data centers, is the company's forecast and is not needed to read
  the castle or the value.
- **Would the insiders write the forecast down?** **[M2000-105]**: they do, in rate filings with forward test years and in a ten-year
  capital plan, and the regulators publish the allowed returns. This is not the fast-moving field of **[L1993-023]**; the change it faces
  (distributed generation, electrified heating against the gas parts, heavier storms) is slow change, which "can lull you to sleep
  easier" **[M2014-038]**, and is weighed at Q2.
- **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence" it is not inside
  **[M2002-092]**: no doubt on the economics of a regulated monopoly. What is not knowable with precision is the
  regulators' future conduct, which is the castle question (Q2), not the understanding question.
- **VERDICT: IN.** The economics ten years out are those of an allowed return on a rate base, foreseeable within a range
  **[M2000-037]**, **[M2011-084]**; "the first question is, can I understand it?" **[M1995-051]** is passed.
