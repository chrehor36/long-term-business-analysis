# BRIEF - TOST (Toast, Inc.), run of 2026-09-18
Written by the overnight session before launch. **Assume this brief contains at least one error;
every brief since NKE has, and finding it is part of the run.** Nothing below is a verdict.

## 0. WHAT GOVERNS
- `CLAUDE.md`, then `Framework/THE FRAMEWORK v4.md`. This is a NEW NAME, not a holding: **v4 governs.**
- Operator protocol rules 1-9. **Hard sequence: no Q5 output unless Q1-Q4 each show IN.** Any
  valuation arithmetic produced before Q1-Q4 close is headed **"COMPUTATION - NOT A CLEARANCE"**
  and carries no entry language.
- Every judgment justified by ledger id from `principle_ledger.csv`, or it is an opinion.
- **VERBATIM ONLY.** Quotes exact, with the document and date. Paraphrase is never quotation.

## 1. WRITE-EARLY PROTOCOL - do this before any fetch
1. Copy `Test Runs/_TEMPLATE - Company Run.md` to
   **`Test Runs/2026-09-18 Run - TOST Toast.md`** and commit it empty.
2. Write each question into the file AS IT CLOSES, and **commit after every question**.
3. Research goes to `Test Runs/_research 2026-09-18 TOST/` as it is gathered. Some is already
   there (section 3 below) - **do not refetch it**.
4. **COMMIT WITH A PATHSPEC**: `git commit -F <fresh message file> -- <path> <path>`.
   `git add` + `git commit` commits the whole shared index and has crossed six commits in this
   tree. Write a FRESH message file every time; a stale one at a reused path has mistitled a commit.

## 2. WHAT THE QUEUE SAYS ABOUT THIS NAME - a prompt to read, never a verdict
TOST has **no screen row**. It is a WAVE 5 name: one of the 35 unpriced watchlist businesses
in `Screens/WATCHLIST RUN QUEUE.md` (line 248). Its triage skip reason is
**"capex unresolved [E5-20]: build (c) by hand from the filing"**, and it is the sixth of the
eight names in that row to be run. Four dated notes sit beside that table (lines 264-270) from the
AMZN, NVDA, CL and SPGI runs. Their standing instruction for TOST, EQIX and DLR is exactly three
things, and I have done the first two for you in section 3:
1. re-run the name through the CURRENT `owner_earnings()` to see which kind of gap it is;
2. check for missing early-year capex facts;
3. **ask what the D&A is actually made of before assuming the band is about plant.**
Of the five names run from this row so far: ABNB had a real presentation gap, AMZN had no gap,
NVDA had a tag gap plus a history gap, CL had a tag gap only, SPGI had a tag gap plus a (c)
question the label does not describe. **The exception class [E5-20] has applied at AMZN alone.**
Read the label as UNLABELLED: the tail-triage correction of 2026-09-12 is that a label describing
the arithmetic has repeatedly been right in substance and wrong about what the arithmetic was, and
four runs found the file closed at a gate the label did not point to.

## 3. STEP 0 EVIDENCE ALREADY ON DISK - verify it, do not inherit it
In `Test Runs/_research 2026-09-18 TOST/`:
- `companyfacts.json` (SEC XBRL, CIK **0001650164**, entityName "Toast, Inc.", fetched 2026-09-18)
- `submissions.json` (same fetch)
- `10K_FY2025.htm` and `10K_FY2025.txt` - the FY2025 10-K, accession **0001650164-26-000057**,
  filed 2026-02-18, primary document `tost-20251231.htm`
- `10Q_2026Q2.htm` - the Q2 2026 10-Q, accession **0001650164-26-000164**, filed 2026-08-05

**THE PAIR IS NOT STRUCK. Strike it yourself.**
- `tools/sources.py:price("TOST")` returned **(30.33, '2026-09-18', 'USD')** at 10:13 EDT today.
  **THAT IS AN INTRADAY QUOTE, NOT A CLOSE** - `price()` returns `regularMarketPrice` and stamps it
  with today's date; `regularMarketTime` was 14:11 UTC, i.e. 10:11 EDT, with the market open.
  A run that writes "$30.33 (2026-09-18 close)" states a falsehood. The **2026-09-17 close was
  $30.65**; the four prior closes were 09-11 $32.12, 09-14 $33.29, 09-15 $31.84, 09-16 $31.12.
  Choose one, name what it is, and flag the aggregator per operator rule 5.
- **USD 30-year sovereign 5.29%, 09/17/2026, US Treasury daily par yield curve** (the issuing
  authority). Re-fetch it yourself; it moved twice inside four days earlier this month.

**SHARE COUNT - and a source limit I could not get past.**
The Q2 2026 10-Q cover: *"The registrant had outstanding 514 million shares of Class A common
stock and 64 million shares of Class B common stock as of July 30, 2026."* The balance-sheet
parenthetical at 2026-06-30 gives Class A 512 million and Class B 65 million, against 523 million
and 66 million at 2025-12-31. **Toast tags its ENTIRE XBRL instance at `decimals="-6"`** - I
checked `tost-20260630_htm.xml` directly - **so no exact share count exists anywhere in the filing,
and neither does an exact dollar figure.** The cap therefore cannot be struck to better than about
+/-0.1%. State that as a limit rather than implying a precision the filer did not file. Check the
ERIC trap (issued vs outstanding) and the SPGI trap (a cover that excludes shares it calls
outstanding) on the actual document anyway; both were real at their names. Two classes: check the
charter for whether Class B is economically identical before summing.

**THE CAPEX LABEL, measured.** `PaymentsToAcquirePropertyPlantAndEquipment` carries 10-K years
**FY2021-FY2022** and stops; `PaymentsToAcquireProductiveAssets` carries **FY2023-FY2025**. The
current `owner_earnings()` union reaches every year and `annual(f, CAPX_TAGS)` returns a complete
**seven-year series FY2019-FY2025**: 9, 28, 12, 16, 42, 54, 53 ($m). **No early-year hole of the
NVDA kind.** It reconciles to the face of the FY2025 cash-flow statement, which reads
*"Capital expenditures ( 53 ) ( 54 ) ( 42 )"*. So the label is the CL/AMZN kind of tooling artefact
on its face - **but see the next paragraph before concluding that, because the third instruction
is the one that bites here.**

**WHAT THE D&A IS MADE OF - the thing the label does not describe.** Filed D&A is 64, 46, 32 ($m,
FY2025-23). `CapitalizedComputerSoftwareAmortization1` is **49, 30, 16** - so roughly **77% of
FY2025 D&A is amortization of capitalised internal-use software**, not plant.
`CapitalizedComputerSoftwareAdditions` is **54, 53, 48** ($m FY2025-23) against **total** cash
capital expenditure of **53, 54, 42**. **Additions EXCEED total cash capex in FY2025**, which they
cannot do if they were all cash - so some part of the software additions is non-cash, and the
obvious candidate is capitalised stock-based compensation. That matters twice: it is the known
**SBC max-rule double-count limit** recorded in `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md`
section 5 (*"can double-count SBC that was capitalised into software and already sits in (c)"*), and
it means the (c) question at this company is about **software and sales capacity, not plant.** Read
Note 1 and the property-and-equipment note and settle it on the document. `PaymentsForSoftware`
exists as a tag but stops at FY2022 (6, 8, 7, 17 for FY2019-22), so it is not the route.
**Ask [E5-20] separately on the filing**, as CL and SPGI did, and answer it in words.

**A SECOND CAPITALISED COST, larger than either.** The FY2025 cash-flow statement carries
*"Amortization of deferred contract acquisition costs 99 82 62"* as an add-back and
*"Deferred contract acquisition costs ( 147 ) ( 130 ) ( 107 )"* as a use - a net drag of about
$48m, $48m and $45m a year sitting inside operating cash. Decide on the corpus what that is:
capitalised sales commissions on a growing book. It is already inside OCF net, so it is not a
(b) or (c) adjustment, but its size relative to the capex line is worth stating.

**THE SCREEN'S OWN NUMBERS, so you can reproduce and then adjudicate them:**
- `owner_earnings(facts)` = `{'5y_da': -65.4M, '5y_capex': -68.2M, '3y_da': +80.7M, '3y_capex': +78.3M}`
- OCF FY2019-25 ($m): -126, -125, 2, -156, 135, 360, **661**
- SBC FY2019-25 ($m): 34, 86, 142, 228, 277, 253, **242**
- Revenue FY2019-25 ($m): 665, 823, 1,705, 2,731, 3,865, 4,960, **6,153**
- Operating income FY2019-25 ($m): -213, -220, -228, -384, -287, **+16**, **+292**
- Net income FY2019-25 ($m): -209, -248, -487, -275, -246, **+19**, **+342**
- `oe_annual(capex)` FY2019-25 ($m): -175, -247, -159, -417, -184, **+53**, **+366**
- **SBC/OCF in FY2025 is 242/661 = 36.6%**, and cumulatively over the filed life it is far higher
  because OCF was negative for four of seven years. The ARM and CALX runs set the marks at 96.6%
  and 98.4% cumulative and both closed at Q4; compute it here and let it fall where it falls.
- `working_capital_flag()` fires on FY2021 accounts payable and **refuses the ratio in words**
  (near-zero OCF). Read it; do not report the 750%.
- `shares_outstanding()` returns **None** - there is no undimensioned dei count, because the count
  is dimensioned by share class. That is why the cover must be read.

**THE FLOAT AND THE LENDER - two perimeter questions I have located but not answered.**
- *"Change in customer funds obligations, net 36 36 27"* sits in **FINANCING**, and the cash
  reconciliation carries *"Cash held on behalf of customers 159 123 87"* plus
  *"Restricted cash 71 59 55"* separately from *"Cash and cash equivalents 1,353 903 605"*.
  So merchant float is NOT inside operating cash the way ABNB's was - **but interest earned on it
  may be inside income.** The ABNB run's method (show owner earnings with float income removed as
  well as included) is the precedent.
- **Toast Capital.** The revenue note says financial technology solutions revenue *"also includes
  fees earned from marketing and servicing working capital loans to our customers through Toast
  Capital that are originated by a third-party bank."* Originated by a bank - yet
  **"Credit loss expense" is added back as non-cash at 91, 70, 64 ($m FY2025-23)** against $292m of
  FY2025 operating income. Who bears the loss? Settle it on the loan note and the risk factors.
  If Toast retains credit risk, the insurer/lender question arises and
  `Framework/SECTOR METHOD - owner earnings for insurers …` is the file to check for whether a
  components-plus-judgment treatment is owed. **The operator's bank directive of 2026-08-30 covers
  BANKS; this is not a bank holding company and it is on the wave 5 roster, so it is run.**
- A **warrant liability** runs through the statements: *"Change in fair value of warrant liability
  ( 3 ) 49 ( 3 )"*, *"Gain on warrant extinguishment ( 14 )"*, and **"Warrant repurchase ( 61 )"**
  in FY2025 financing. Find out whose warrant and what it was for.

**CAPITAL ALLOCATION, from the equity statement (shares in millions):** 523 at 2022-12-31 -> 543 ->
572 -> **589 at 2025-12-31**, with share repurchases of **(3) / $107m** in 2025 and **(2) / $56m**
in 2024 against stock-based compensation of $254m and $267m. The Q2 2026 balance sheet shows
**577m**, so the count fell in H1 2026. [E5-44] and [E2-56] are the rows for per-share dilution;
the SPGI run's construction (owner earnings PER SHARE across comparable perimeters) is the
precedent worth copying. **No debt drawn**: the only financing debt line is *"Payments of issuance
costs of the revolving credit facility ( 3 )"*.

**LIVE-DEAL CHECK.** `sources.deal_filings("0001650164")` returned empty lists. `submissions.json`
shows the newest filings as the Q2 2026 10-Q (2026-08-05) and the 8-K of 2026-08-04 (the Q2
earnings release), with 8-Ks on 2026-06-15, 2026-05-07, 2026-02-12 and 2026-01-15 unread.
**Re-query EDGAR yourself at the time of the run** - the SPGI run recorded "nothing filed after
2026-08-04" as a limit and the CL run found Forms 4 that confirmed the aggregator's quote against a
primary filing.

## 4. THE STANDING Q3 COMPANION, and it is not optional
**Pull the latest 8-K EX-99.1 earnings release before scoring [E4-29] and [E4-22]'s third flag.**
A run that reads only the annual report will score clean a company that has built its public
narrative on a non-GAAP metric. I grepped the FY2025 10-K: **"Adjusted EBITDA" appears 14 times**
and **"ARR" 147 times**. Both of those are counts, not findings - what they mean is for you to
determine from where the words sit (risk factor, MD&A reconciliation, compensation yardstick,
headline). The DEF 14A of 2026-04-23 (`0001650164-26-000098`) is the document for the pay yardstick.

## 5. THE COMPETITOR ROW - Q2 is a relative claim and cannot be answered without it
A moat claim requires the row. Restaurant point-of-sale and payments has an unusual number of
**filed** rivals, which is the opposite of the SPGI problem: **Block/Square (XYZ), Fiserv (Clover),
Shift4, Lightspeed, PAR Technology, Olo, Global Payments, Oracle (MICROS)** all file or publish.
Private participants (SpotOn, TouchBistro, SkyTab resellers) do not. **Before you mark any part of
the row PROVISIONAL because a competitor is private, read the SPGI finding of 2026-09-18 in
`Screens/WATCHLIST RUN QUEUE.md`**: Form NRSRO Item 7A turned out to be a complete competitor row
for an industry with private participants, and the general lesson is to look for a **regulatory
filing that every participant must make** before concluding no document exists. For payments the
candidates are card-network disclosures, state money-transmitter licence filings and the Nilson
counts; whether any of them resolves is for you to test, and "I tested X and it does not resolve"
is a recordable result. `sources.fts_count()` takes the bare zero-padded ten-digit CIK only -
a malformed CIK returns HTTP 200 with a well-formed ZERO, which is how a naming claim gets faked.
- [E3-03] criterion (2) is the pricing sentence and must be shown on the company's OWN filing.
- [E2-44] both halves, [E4-37], [E4-32] direction, [E2-53], [E5-18], [E2-59].
- Use the AMAT service-margin test where a company claims an annuity; it has landed at three names.
- [E2-49] metric-withdrawal stands at six fires and five failures. **Check it; assume neither way.**

## 6. THE PRIORS I AM MOST LIKELY WRONG ABOUT - argue against me
1. **I expect the capex label to be a tooling artefact and the real (c) question to be software.**
   That is a hypothesis built from tag series, not from the property note. If the note says the
   capex line is restaurant hardware placed with customers, my framing is wrong and the (c)
   question is about a subsidised terminal fleet instead.
2. **I have assumed Toast Capital's credit risk sits with the third-party bank because the revenue
   note says the bank originates.** The $91m credit loss expense is evidence against my own
   reading, and I have not opened the loan note. **Hunt this one hardest** [E4-26].
3. **I read "additions exceed cash capex" as capitalised SBC.** I did not verify it. It could be
   an accrual, a transfer, or my own arithmetic across two differently-scoped tags.
4. **I have said nothing about which gate will close this file, and you should not infer one.**
   The CGNX prohibition is that telling a run which gate will be boring is how a live flag gets
   scored clean. Every gate gets the same effort until the hard sequence stops the run.

## 7. THE FOLD - the run is not finished when the run file is
All six steps, in `Screens/WATCHLIST RUN QUEUE.md` under "THE FOLD":
1. Register entry under `## COMPLETED FROM THE QUEUE` with price, share count AND the cover
   accession it came from, cap, sovereign, and the PASS/FAIL line naming which question closed it.
   **Count the register from the file; do not carry a tally forward.**
2. Strike the ticker in the wave 5 table (`~~TOST~~`).
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`.
4. Bands in `tools/alerts.json` and a `PORTFOLIO.md` row - **for gate-clearers only.** A name that
   fails on the BUSINESS gets a reversal condition in words instead.
5. `python tools/check_framework.py` must PASS **before** the commit.
6. Commit with a pathspec.
Then the self-audit (operator rule 6): the run is incomplete until its self-audit is checked, and
**report the defects you find in this brief** - that report is the part that has caught the most.
