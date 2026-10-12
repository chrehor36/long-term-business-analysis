# Company Run — Fisker Inc. (formerly NYSE: FSR; OTC: FSRN, then FSRNQ; the brief's ticker FSRDQ) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run; analyst working under `Screens/_daily/_dispatch_brief.md` as departed from in the brief (the brief's
two stated departures: the lines of evidence and the rivals derived by the analyst from the 10-K). SEC CIK 1720990.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker and for Fisker, FSR, FSRN and FSRNQ, 2026-10-12).

**Contamination declared.** The git status shown to this session at its start, and the five most recent commit subjects,
name other companies' runs (an EVI fold and its run commits) and other research folders (AYI, ARCB). Nothing of them
bears on Fisker and nothing of them is used. The user's memory index, loaded with the session, carries queue counts and
the names of the governing files; nothing in it names Fisker, and it is not used. No other `Test Runs/` file was opened,
listed or searched; no file about this company under any name was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Ticker.** The SEC ticker list no longer carries FSRDQ (or any Fisker ticker); both `tools/run.py` and
  `Screens/cover_shares.py` refused it ("not an SEC filer" / "NOT AN SEC REGISTRANT in the live ticker file"). The
  arithmetic was run through a wrapper in the research folder (`run_by_cik.py`) that hands CIK 1720990 to `tools/run.py`;
  output in `runpy_out.txt`. The filings show the ticker as FSR on the NYSE, then **FSRN** on OTC Pink (cover of the 8-K
  of 2024-06-24, 0001193125-24-167032), then **FSRNQ** (FINRA, below). **No filing or notice found carries "FSRDQ"**; the
  brief's ticker is recorded as given and flagged.
- **Price:** **none exists.** No aggregator quote was found for FSRDQ, FSRNQ, FSRN or FSR (Yahoo chart API, 2026-10-12:
  "No data found, symbol may be delisted", all four). The reason is a fact of record: FINRA Uniform Practice Advisory
  #75-24, dated 10/18/2024, "Fisker, Inc. (FSRNQ)": "Notice has been received that the Chapter 11 Plan has become effective
  on 10/17/2024. On the Effective Date, all Equity Interests in the Debtors shall be deemed automatically canceled,
  released, and extinguished [...] No holder of an Equity Interest will receive any Plan Distribution on account thereof."
  (finra.org, `UPC-75-2024-FSRNQ.pdf`, copy in `cache/finra/`, gitignored; FINRA is a regulator's notice, not the issuer's
  filing, flagged; it quotes the plan, In re Fisker Inc., Case No. 24-11390 (TMH), D. Del., which was not itself read.)
  The issuer had said the same before the plan: "The Company expects that its existing common stock will be cancelled and
  that holders of the common stock will not receive any amounts through the Chapter 11 Cases." (NT 10-Q, 2024-08-15,
  0001628280-24-037402, the last SEC filing.)
- **Shares by class** from the latest filing's cover: 1,385,486,856 Class A and 132,354,128 Class B outstanding as of
  April 15, 2024 (10-K FY2023 cover, 2024-04-23, 0001720990-24-000045). Class B carries ten votes a share (DEF 14A
  2023, 0001720990-23-000043); the charter was not read on economic equivalence, and the two are added for the
  computation only. Check against the balance sheet: 316,589,859 A and 132,354,128 B issued and outstanding at
  2023-12-31 (same 10-K); the A count rose more than four-fold in three and a half months, by conversions of the 2025
  Notes (10-K risk factors on the Investor's conversions). No treasury shares shown. No later share count was filed
  (no 10-Q after Q3 2023; NT 10-Q for Q1 2024, 0001720990-24-000051, and for Q2 2024). **Since 2024-10-17 the count of
  shares in existence is zero** (FINRA, above).
- **Market cap:** not computable (no price; equity extinguished).
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 10/09/2026 (printed by
  `tools/run.py` through `tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K FY2023 (filed 2024-04-23, 0001720990-24-000045): Item 1, Item 1A, Item 7,
  Item 9A, the balance sheet, the cash-flow supplemental; 10-K FY2022 (2023-03-01, 0001720990-23-000020) for the
  cash-interest line; 10-Q Q3 2023 (2023-11-22, 0001720990-23-000125, fetched, used only for the record of its lateness);
  DEF 14A 2023 (2023-04-27, 0001720990-23-000043), control and family facts only; 8-Ks of 2024-02-16
  (0001193125-24-038568), 2024-03-25 (0001720990-24-000032), 2024-04-03 (0001720990-24-000036), 2024-05-08
  (0001720990-24-000047), 2024-05-13 (0001720990-24-000050, Item 4.01), 2024-06-04 (0001193125-24-154369), 2024-06-24
  (0001193125-24-167032, Items 1.03 and 2.04); NT 10-Q 2023-11-13 (0001720990-23-000118); NT 10-K 2024-03-01
  (0001720990-24-000022); NT 10-Q 2024-05-13 and 2024-08-15. **One figure cross-checked:** cash and cash equivalents at
  2023-12-31, $325,452 thousand on the filed balance sheet, against 325 in the tool's balance-sheet table and $325.5
  million in Item 7: agrees.
- **Lines of evidence chosen** (the brief's departure: derived by the analyst from Items 1, 1A and 7 and the later 8-Ks):
  (1) what the business is, by its own description (start-up, contract-manufactured EV, one model); (2) whether it
  survived as a going concern (Item 1A, Item 7 liquidity, the 2024 8-Ks); (3) what the equity holder is left with (the
  Chapter 11 8-K, the last NT 10-Q, the FINRA notice); (4) the economics shown (revenue, gross margin, cash burn, Item 7);
  (5) the accounts and the controls (Item 9A, the late filings, the auditor's departure); (6) the field, from the rival the
  10-K names that files with the SEC.
- `python tools/run.py` arithmetic lines only (through the CIK wrapper; 5-year window FY2019 to FY2023, USD millions):
  owner cash after every real cost (OCF less stock pay less capital spending) -7.4, -39.4, -441.3, -663.1, -904.7; mean
  **-411.2**; D&A variant mean -316.9; with 2023 finance-lease principal ($18.3M) added to capital spending, mean -415.5.
  Capital spending 0.0, 0.7, 134.4, 191.0, 227.6; D&A 0.1, 0.1, 0.8, 5.3, 76.1; stock pay 0.1, 0.7, 5.6, 19.6, 8.2. The
  tool flagged its window as over 18 months old: correct, no later annual figures exist. Every year is negative.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own it "if the market closed for five years"
**[M1997-109]**, and here the market did close, by delisting (NYSE suspension 2024-03-25, Form 25 2024-04-10), and the
business beneath the share was liquidated with the share extinguished. Margin of safety bears too: no price exists to
set against a value, and no value is positive. Who is paid to tell you: the 10-K's Item 1 is written as a pitch (it
speaks of Henrik Fisker's legendary design and calls the model among the first of its kind). The speakers have "never
looked at a projection" **[M1995-050]**; the reading below rests on what the filings say happened, not what they
forecast. **Contrary evidence, written down as found**
**[M1997-127]**: (a) the brief's ticker FSRDQ appears in no filing or notice found; the security may have been
misidentified by the brief, or the ticker may be an aggregator's; the CIK, the name and the accessions the brief gives all
match, so the run proceeds on CIK 1720990. (b) Against my own close: the EV industry is itself a rapid-change case, and a
second analyst could send the file to TOO HARD (NATURE) at Q1 rather than OUT; written down at Q1 and answered there.
(c) Hunting for evidence that the equity kept any value: none found; the issuer, the plan (as FINRA quotes it) and the
missing quote all point the same way.

## THE STANDING RULE
A purchase of a security that no longer exists, or of a claim the plan says receives nothing, is a certain loss of what is
paid: "Never risk permanent loss of capital." **[L2023-005]**. No leverage is asked of the buyer here, so the rule's
leverage forms do not arise; the rule's own words decide that nothing would be put at risk here, because nothing can be
bought that carries a claim on anything.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
- **What the filings say the business was.** In its own words, "As a high-growth startup, Fisker is transforming its
  strategic efforts" (10-K FY2023, Item 1, 0001720990-24-000045); "As an early-stage company with a limited operating
  history, we face various risks and difficulties" and "Fisker was incorporated in September 2016 and we have a short
  operating history" (Item 1A). One model, the Ocean, built under contract by Magna Steyr in Austria from November 2022;
  first revenue in the second quarter of 2023; 4,847 vehicles delivered in 2023 for revenue of $272.9 million against
  cost of goods sold of $558.8 million (Item 7). A net loss in every year since inception (Item 1A).
- **The key variables** **[M1998-044]**: unit volume of one model, the price it fetches against far larger rivals, the
  cost of a contract-built car, and access to outside capital. The last decided everything: "We need significant
  additional funding in the near term to execute our business plan and to continue our operations" (Item 1A); substantial
  doubt about going concern (Item 1A, Item 7, and PwC's explanatory paragraph per the 8-K of 2024-05-13).
- **Where it stands in ten years: this is not a forecast here; it is on the record.** The US companies filed Chapter 11 on
  June 17 and 19, 2024 (8-K 2024-06-24, Item 1.03, 0001193125-24-167032); the Austrian subsidiary entered restructuring on
  May 7, 2024 (8-K 2024-05-08, 0001720990-24-000047); the issuer expected the common stock to be cancelled with nothing
  paid (NT 10-Q 2024-08-15); the plan, per FINRA's notice, became effective 2024-10-17 and extinguished every equity
  interest with no distribution.
- **Routing.** The draft lists start-ups among what Q1 rules OUT: "Start-ups are not our game." **[L2007-015]**; "We don’t
  do startups." **[M2008-088]**. The filer calls itself a start-up in its last 10-K. The draft also sends fast-moving
  technology to TOO HARD, not OUT **[L1993-023]**, **[M1998-008]**, and the electric-vehicle field reads as one of
  those (Item 1A: "The automotive industry and its technology are rapidly evolving and may be subject to unforeseen
  changes."). The two point to different boxes. I close OUT, for two reasons. First, the start-up item is named and is
  in the OUT list, and the filing names the thing the item names. Second, the TOO HARD routing exists for a forecast the
  insiders themselves would not "put down on paper" **[M2000-105]**; here the issuer itself wrote the outcome for the
  equity down ("existing common stock will be cancelled"), and the plan made it so. Nothing about the owner's ten-year
  economics is unknown: they are zero. The deciding fact is among "things that are important and knowable"
  **[M2006-076]**, and it is known. TOO HARD is not a judgment of quality **[M2000-038]**; a box saying the case cannot
  be evaluated would misstate a case whose value to the shareholder has been fixed by a court.
- The quick decision is made "off the figures" **[M2008-069]**, from documents "anybody can get" **[M2005-015]**: here a
  Chapter 11 8-K and a FINRA notice. "if we can’t make a decision in five minutes, we can’t make it in five months"
  **[M2008-086]**; this one is made.
- **VERDICT: OUT** **[M2006-013]**. A start-up by its own filing **[L2007-015]**, **[M2008-088]**, whose economics to
  the owner of its common stock are known, not forecast: the equity was cancelled on 2024-10-17 with no distribution
  (FINRA UPC #75-24; issuer's NT 10-Q 2024-08-15, 0001628280-24-037402; 8-K 2024-06-24, 0001193125-24-167032). Q2 to Q12
  NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 OUT). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets, read in Step 0 as the template asks when the file closes before Q4, are under AFTER THE
STOP, Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (The buyback line that Q6 takes from Q7 does not arise: no buyback, and Q7 is not reached.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The two reporting figures the operator asks for are computed below under the protocol's
heading.

### COMPUTATION, NOT A CLEARANCE
*(Operator rule 3; Part VII, The owner's price. Computed only because the brief's reporting convention asks for the two
figures after an earlier STOP; no entry language; nothing here is a verdict. Script and output: `q7_computation.py`,
`q7_out.txt`.)*
- **Input.** Owner cash after every real cost, five-year mean FY2019 to FY2023 (the literal window; the only window the
  filings allow): **-$411.2M** a year on the equity basis (OCF less stock pay less all capital spending); **-$404.2M** on
  the all-equity basis (cash interest paid added back: $0, $0, $0, $17.985M, $16.688M; 10-K FY2023 and FY2022 cash-flow
  supplementals). D&A variant -$316.9M. The company paid essentially no income tax ($1.3M provision in 2023), so the
  company's own tax changes nothing; no carryforward is priced, since none has a positive stream to shelter.
- **The specifics applied.** (a) Cycle base: not applicable; every window year is a start-up year, FY2019 and FY2020
  pre-production, FY2023 the first year of sales, so no year is a cyclical peak or trough, and no other window exists.
  (b) Decline: the series is negative in every year and worsens; a compound growth rate between negative end years is
  meaningless, and so is the half-window comparison (-$23.4M to -$783.9M a year), so **the range is the no-growth case
  alone, said so**. (c) Acquisitions: none (the 2021 $10.0M Allego PIPE is an equity investment, not a business bought).
  Merger: the 2020 reverse merger with Spartan was a recapitalization with no operating business on the Spartan side;
  the window's figures are Legacy Fisker's throughout. (d) Working capital: inside OCF as filed (inventory rose to
  $406.5M in 2023). (e) Growth spending: no maintenance guess is possible for a business that never reached a steady
  state; all spending deducted. (f) The cap: no positive growth is carried. The four PG specifics: aggregate, not per
  share; all spending deducted, the D&A variant beside; zero nominal growth after year ten (here from year one); the
  floor tested first.
- **Net debt** at the latest filed balance sheet (2023-12-31): convertible senior notes $291.7M current and $935.2M
  non-current, less cash $325.5M = **$901.5M** (restricted cash $70.4M and operating leases left out, said so). The
  filing's own stated subsequent events would only raise it: cash fell to $53.9M by April 16, 2024 (Item 7), and the 2026
  Notes and the 2025 Notes were later accelerated (8-Ks 2024-06-04 and 2024-06-24). Shares 1,517.84M (cover,
  2024-04-15).
- **(a) VALUE RANGE:** no-growth case at the sovereign 5.60%: whole business -$7,219M; **-$5.35 a share on the
  all-equity basis** (central figure); **-$4.84 a share equity-only** (beside). D&A variant, all-equity: -$4.24. A single
  case, so the range has no width; the literal window FY2019 to FY2023 is the window used.
- **(b) FAIR PRICE** (Part VII: each end case valued at ten percent, the two averaged; here one case): **-$3.26 a share
  on the all-equity basis**, **-$2.71 equity-only**.
- **Against the price:** there is no price. The shares were extinguished on 2024-10-17 (FINRA UPC #75-24) and no quote
  exists. No case earns the floor at any positive price **[M2003-149]**; a value "we don’t have the faintest idea" of is
  not what this is **[M1994-077]**: the stream is known, and negative.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q1**: a start-up by its own last 10-K whose common equity was cancelled under its Chapter 11 plan on
2024-10-17 with no distribution; the owner's economics are known and are nil. Not reached Q7; COMPUTATION, NOT A
CLEARANCE: value -$5.35 a share (all-equity; -$4.84 equity-only), fair -$3.26 (-$2.71 equity-only), against no price
(equity extinguished, no quote). **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2); each with its source **[M1997-127]**.)*

**Q2, the castle.**
- Rivals the 10-K names: **Tesla** (SEC filer, CIK 1318605) and **BMW** (named as the BMW X3 Series in the "premium with
  volume" definition; **does not file with the SEC, flagged, not compared**). The 10-K names no other rival; it refers to
  "a few Chinese EV independent start-ups" without names. Its own words on the field: "Many of our current and potential
  competitors have significantly greater financial, technical, manufacturing, marketing and other resources than we do"
  (Item 1A); "The Company's better capitalized competitors may seek to undercut the pricing or compete directly with the
  Company’s designs by replicating their features." (Item 7).
- **Competitor row, FY2019 to FY2023, same metrics from each filer's own 10-K:**

  | | 2019 | 2020 | 2021 | 2022 | 2023 |
  |---|---|---|---|---|---|
  | Tesla gross margin | 16.6% | 21.0% | 25.3% | 25.6% | 18.2% |
  | Tesla operating margin | -0.3% | 6.3% | 12.1% | 16.8% | 9.2% |
  | Fisker gross margin | no revenue | no revenue | no revenue | n.m. ($0.3M of merchandise) | -104.8% |
  | Fisker operating margin | no revenue | no revenue | no revenue | n.m. | -220.8% |

  Tesla from XBRL companyfacts (Revenues, GrossProfit, OperatingIncomeLoss, frames CY2019 to CY2023, as carried in
  Tesla's 10-Ks, latest-carrying accessions 0000950170-22-000796, 0000950170-23-001409, 0001628280-24-002390,
  0001628280-25-003063, 0001628280-26-003952; transcription, Tesla's filed statements not opened). Fisker from the 10-K
  FY2023 Item 7 (revenue $272.9M, gross margin -$285.9M including a $232.7M net-realizable-value write-down, loss from
  operations -$602.5M). Over the span the named rival earned positive margins in four of five years; Fisker never
  earned a gross profit on a car.
- Contract manufacturing by Magna Steyr; Magna holds 19,474,454 warrants at $0.01 (Item 1). Three NHTSA preliminary
  evaluations opened in 2024 (braking, unintended movement, door latch; Item 1).

**Q3, capital.** Cash used in operating and investing activities: $301.3M + $134.4M (2021), $452.5M + $201.0M (2022),
$668.9M + $235.9M (2023, "$904.9 million" in Item 1A). Funded by equity and convertible notes, never by operations
(Item 7).

**Q4, the accounts. The balance sheets read first** **[M2025-032]** (tool's table, first-filed vintages; FY2023 and FY2022
read on the filed statement): 2017 to 2019 rows are Spartan Energy, the SPAC, a trust and nothing else, and are not the
business. From 2020: total assets $1,064M, $1,593M, $1,515M, $1,832M; cash $991M, $1,202M, $737M, $325M; equity $1,045M,
$800M, $481M, **-$98M** (2023); accumulated deficit -$73M, -$619M, -$1,167M, -$2,107M; convertible notes $0, $659M, $661M,
$1,227M; inventory $4.3M (2022) to $406.5M (2023) against revenue of $272.9M; intangible asset $220.7M (2023). What the
figures say: equity raised in the 2020 merger was spent in three years and replaced with convertible debt; inventory in
2023 exceeded the year's revenue. Item 9A (10-K FY2023): internal control not effective, four material weaknesses
(control environment and staff, information sharing, inventory and revenue accounting, non-routine transactions
including convertible debt valuation), which "resulted in material audit adjustments to revenue, accounts receivable,
deferred revenue, inventory, costs of goods sold, convertible debt and derivative liability balances". A $327.8M
fair-value loss on the 2025 Notes in 2023, driven by "an enriched conversion feature which became available to the
Investor upon the event of default which occurred on November 13, 2023 related to the Company's late filing of Form 10-Q"
(Item 7). Whether an adjusted figure was featured in releases: not checked.

**Q5, integrity facts (recorded, not judged).**
- The Q3 2023 10-Q was filed late (NT 10-Q 2023-11-13, 0001720990-23-000118), after the chief accounting officer left
  effective October 27, 2023 and a new one started November 6, 2023; the late filing was itself an event of default under
  the 2025 Notes (Item 7).
- The FY2023 10-K was filed late (NT 10-K 2024-03-01, 0001720990-24-000022: "lacks a sufficient number of professionals
  with an appropriate level of accounting knowledge"), and the Q1 2024 10-Q was never filed.
- 2024 guidance given on 2024-02-29 was withdrawn on 2024-04-03 (8-K 0001720990-24-000036).
- PwC declined to stand for re-appointment, 2024-05-07, with no disagreements and the material weaknesses as the
  reportable events (8-K 2024-05-13, 0001720990-24-000050).
- The CEO and Chairman, Henrik Fisker, is married to the CFO and COO, Dr. Geeta Gupta-Fisker; together they controlled a
  majority of the vote through ten-vote Class B shares, and the company used the NYSE controlled-company exemption (DEF 14A
  2023, 0001720990-23-000043).
- A press report of an SEC investigation surfaced in a web search result title (dailyjournal.com); not read, not a
  filing, not used.

**Q6, issuance.** Class A shares outstanding 187.6M (2022-12-31), 316.6M (2023-12-31), 1,385.5M (2024-04-15); ATM sales
$190.5M (2022) and $135.9M (2023); $510.0M of 2025 Notes sold to a single investor in 2023, $145.5M converted in 2023
(Item 7).

**Q9, debt.** $667.5M 2.50% convertible notes due 2026; the March 15, 2024 interest payment (about $8.4M) missed; 2025
Notes in default on several counts (8-K 2024-05-08); a $3.456M senior secured 2024 note to CVI Investments accelerated
2024-05-29 (8-K 2024-06-04); Chapter 11 accelerated the 2026 Notes (8-K 2024-06-24, Item 2.04). The rows on leverage
would read this: "Even a short absence of credit can bring a company to its knees." **[L2010-020]**; recorded, not weighed.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      **Partly kept, said plainly:** the template was copied and the notes file written before the first fetch, but the
      run file was then written in one pass after the reading (Step 0 through the close, Q1 being the only question
      answered), and the first commit came only after that pass, not after Step 0 and again after Q1. The research was
      done before any judgment was written, so nothing was rewritten to fit; the discipline was still not kept.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session; the run is folded into the register before the dispatcher moves on (operator rule ten). A run not in the
      register binds nothing. (The fold is the dispatcher's.)
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen
      by accident (commit subjects, git status) is declared under contamination, not used.
- [x] Every v5 id resolves (checked by `check_citations.py` in the research folder); every filing fact has its accession;
      no number without a row or a filing. The FINRA notice is a regulator's notice, flagged as not a filing.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (Treasury, 2026-10-09); no aggregator quote exists, and that is said.
- [x] Contrary evidence was written down as it was found **[M1997-127]**; the facts found for later questions are under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII). Not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); it ran through a CIK wrapper, said so.
- [x] `python tools/check_framework.py` PASS before the commit (see the last commit of this run).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The framework has no rule for a security that no longer exists. Its questions assume a business with a future and a price;
here the equity was cancelled by a confirmed plan two years before the run, and the brief's ticker matches no filing.
I closed at Q1 because the start-up item is in Q1's OUT list and the owner's economics are known, but the same name
also fits Q1's fast-moving-technology routing to TOO HARD (NATURE), and Q1 does not say which governs when both apply;
a second analyst could close it TOO HARD (NATURE) on the same evidence and the record would then say the case
cannot be evaluated when a court has evaluated it. A line in section I or Q1 saying that an extinguished or plan-cancelled
equity closes OUT before any question (or that a start-up item outranks the change routing) would remove the choice.
Second, Q7's reporting convention asks for two figures "against the price" even when no price can exist; I computed
them as the brief asks, but negative figures on a cancelled share carry no information for an alert, and the convention
does not say whether to skip them. Third, Q7's decline specific (b) handles a negative growth rate, but not a series
that is negative throughout; I read its last clause ("the range is the no-growth case alone") as covering it, and said so.
Fourth, `tools/run.py` and `Screens/cover_shares.py` resolve only tickers in the live SEC list, so every delisted or
bankrupt name needs a hand wrapper; a `--cik` argument would get the same number sooner.
