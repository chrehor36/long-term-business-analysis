# Company Run: Spire Inc. (NYSE: SR), 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 68463bbf). Every judgment cites a v5
ledger id in bold; every filing fact carries its accession. A dispatched blind run under `Screens/_daily/_dispatch_brief.md`,
with the two departures the brief states (lines of evidence derived by the analyst; competitors chosen as below).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold (overnight 2026-10-18), after the run was committed: the operator does not hold this name (`PORTFOLIO.md`
carries no SR, Spire or Laclede line).*

**Contamination, declared and not used.** (1) Listing `Test Runs/` for today's date to check my own file name showed the
names of seven other run files and research folders dated 2026-10-18 (HOKCY, MDU, NJR, NWN, OGS, SWX, XNGSY); none was
opened. (2) The session context carried recent commit subjects about the SWX run of today (its box, its range and its fair
price); not used. (3) The memory index loaded with the session carries general queue lines (counts of gate-clearers, a
wave state); not used, and nothing in it names this company. ONE Gas is one of my comparators below: its figures come from
its own SEC filings only, never from the OGS run file, which I did not open.

**The lines of evidence (chosen by me, as the brief requires), and from which Item of the fiscal 2025 10-K:**
(a) Item 1: the franchise and its competitors ("Spire Missouri is the only distributor of natural gas within its franchised
service areas"; "The principal competition for the Utilities comes from the local electric companies"), customer counts
and volumes, the PGA/GSA pass-through, the segments; (b) Item 1A: decarbonization and fuel-switching rules, regulatory lag
and cost disallowance, the ISRS statute expiring 2029-08-28, the NOLs, the holding-company dependence, ratings and parental
guaranties, the acquisition risk; (c) Item 7: adjusted earnings and contribution margin featured, the Piedmont Tennessee
deal and its financing, the cash-flow history and capital plan ($809 for fiscal 2026), the debt maturities, the equity
issuance through the ATM, forward sales and equity units. Read beside them: the 10-Q to 2026-06-30, the Piedmont Tennessee
abbreviated statements (8-K/A), the proxy, the 8-Ks listed in Step 0.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $82.03, close 2026-10-16 (last trading day before the run date), via `tools/run.py` from an aggregator
  (flagged per operator rule 5: aggregator, live quote only).
- **Shares:** 59,112,807 common shares at 2026-07-31, cover of the 10-Q for the quarter to 2026-06-30 (accession
  0001193125-26-334335). `Screens/cover_shares.py SR` printed three numbers: the other two (26,822 and 1,972,052) are the
  shares of Spire Missouri and Spire Alabama, all owned by Spire Inc., not classes of the parent; one class only. Check
  against the balance sheet: "59.1 million ... shares issued and outstanding at June 30, 2026", no treasury line. No 8-K
  after the 10-Q issues shares (the 8-Ks of 2026-09-01, 2026-10-08 and 2026-10-13 are a $400 delayed-draw term loan, $350 of
  Spire Missouri first mortgage bonds and a credit-agreement extension). The 5.90% Series A preferred was redeemed in full on
  2026-02-13 (10-Q, Note on equity), so no preferred sits ahead of the common at the price date.
- **Market cap:** $82.03 x 59.1128M = **$4,849.0M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-16 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for fiscal 2025 (filed 2025-11-14, accession 0001193125-25-282583): Items 1, 1A,
  1C, 2, 5, 7, 8 (statements, Notes 12, 14, 15, 18); 10-Q to 2026-06-30 (filed 2026-08-05, 0001193125-26-334335): statements,
  Notes 2 (acquisition), 3 (divestitures), financing; proxy DEF 14A filed 2025-12-16 (0001308179-25-000657): CD&A, summary
  compensation table, ownership; 8-K/A of 2026-04-06 (0001193125-26-144025) Exhibit 99.1, audited abbreviated statements of
  the Tennessee Piedmont business for calendar 2024 and 2025; 8-Ks of 2026-03-31 (0001193125-26-134715), 2026-04-30
  (0001193125-26-197505), 2026-06-30 (0001193125-26-290674), 2026-08-05 (0001193125-26-333825), 2026-09-01
  (0001193125-26-378491), 2026-10-08 (0001193125-26-417983), 2026-10-13 (0001193125-26-420501); 8-Ks of 2025-04-25
  (0000950170-25-058353, the CEO change) and 2025-09-22 (0001193125-25-210056, the COO hire); for the ten-year history the
  10-Ks for fiscal 2018 (0001126956-18-000065), 2021 (0001564590-21-057844) and 2022 (0001437749-22-027522): statements and
  segment notes.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, fiscal 2025,
  $578.0M in the filed consolidated statement of cash flows (10-K, page 53) equals the `tools/run.py` figure 578.0; also
  fiscal 2016-2018 operating cash (328.3, 288.3, 456.6) and capital spending (293.3, 438.1, 499.4) in the fiscal 2018 10-K
  equal the XBRL series.
- **`python tools/run.py SR` arithmetic lines** (used for arithmetic only, Part VII): OCF 440.2 / 912.4 / 578.0, stock pay
  9.8 / 5.8 / 6.7, D&A 254.8 / 278.4 / 298.2, capital spending 662.5 / 861.3 / 922.4 for fiscal 2023-2025; owner cash after
  all capital spending -232.1 / 45.3 / -351.1; five-year means: after all capital spending -286.1, after D&A only 182.2.
  Its debt table line "d1 = CapitalizationLongtermDebtAndEquity" includes equity and is not debt; ignored. Stock pay is
  resolved from the filings: expense 13.9, 6.4, 9.8, 5.8, 6.7 for fiscal 2021-2025 (XBRL AllocatedShareBasedCompensationExpense;
  the equity statements show "Stock-based compensation costs" 9.1 for 2021 and 6.1 for 2025, the difference being capitalized
  or liability-classified amounts); I deduct the larger expense figure. No other stock-pay line, no securities purchases
  inside operating cash (run.py, confirmed by reading the cash-flow statement).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years" **[M1997-109]**,
and for a regulated gas distributor the question is answerable, since its cash depends on rate orders and winters, not on the
quotation. The margin of safety is the foundation that bears hardest: the price must not need a pencil **[M1996-084]**, and
the margin widens as understanding falls and volatility rises **[M1997-080]**. No macro view enters: I make no forecast of
gas prices or interest rates **[M2000-094]**. Who is paid to tell you: the 10-K's own case for the Tennessee deal ("We expect
the Transaction to support Spire’s long-term adjusted earnings per share growth expectations") is the seller of the plan
describing the plan, and is read with the rows' warning: "don’t ask the barber whether you need a haircut" **[M2011-083]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) capital spending exceeded operating cash in every one of the last ten years read; (2) the earned return
on common equity averaged 8.2% over fiscal 2016-2025 against an allowed 9.5% to 9.9% in Alabama; (3) shares outstanding
rose from 45.65M (2016-09-30) to 59.11M (2026-07-31); (4) three chief executives across fiscal 2023-2025 (proxy, pay-versus-performance table), the second
"terminated without “Cause”" (8-K 2025-04-25); (5) a $148.6M impairment in 2020 (Spire Storage, "Other" segment, fiscal 2022 10-K segment
table) and a storage business built, expanded and then sold in 2026; (6) debt rose to $7,259.6M at 2026-06-30 against
equity of $3,583.0M.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of these shares for cash, unlevered, and sized so that the buyer can see
it "go down 50 percent — or more — and be comfortable with it" **[M2020-022]**, puts the buyer at no risk of ruin;
"Never risk permanent loss of capital." **[L2023-005]** binds the sizing, not the business. Nothing in this run proposes
borrowing to buy **[L2014-005]**.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from Item 1.** After the 2026 transactions Spire is four regulated gas distributors (Spire
  Missouri, about 1.2 million customers in St. Louis and Kansas City; Spire Alabama, more than 0.4 million in Birmingham and
  Montgomery; Spire Gulf near Mobile; Spire Tennessee, more than 200,000 around Nashville from 2026-03-31) plus two
  FERC-regulated pipelines (Spire STL Pipeline, merged into Spire MoGas) whose revenue is "derived primarily from Spire
  Missouri as its foundation shipper". Spire Mississippi is under contract for sale ($75.0, 10-Q Note 3). Gas Marketing and
  Spire Storage were sold in 2026 and are discontinued operations (10-Q Note 3). The gas cost passes through to customers
  under the PGA clauses and the GSA rider; the earnings are the regulated margin on the distribution system: "The earnings
  of Spire Missouri are primarily generated by the sale of heating energy" (Item 1).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) rate base, which grows with capital spending
  that the commissions approve (Missouri rate base plant in service $4,379.6 in the 2025 order, Note 15); (2) the allowed
  return (Missouri "a 7.05 % post-tax total rate of return for future ISRS purposes"; Alabama "allowed range of RCE is
  9.50 % to 9.90 %", Note 15) and the lag between spending and recovery (Item 1A); (3) the volume and customer count,
  which barely move (1,735,633 average customers in fiscal 2023, 1,744,537 in 2025, Item 1) and are weather-normalized by
  riders; (4) the long-run demand for gas against electrification and efficiency rules (Item 1A, first risk). The first
  three are set by regulators on stated formulas and are about as foreseeable ten years out as anything I read: the
  question is the one the rows ask, "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, and the regulated return gives that fix within a band. The fourth is a slow
  change, named by the filer itself ("Management believes it is likely that any such resulting impacts would occur over a
  long period of time", Item 1A), and is carried to Q2, which owns change **[M2014-038]**.
- **Do the past statements tell me the future ones** **[M2008-033]**? Yes, with one confusion handled at Q4: the
  revenues swing with gas costs that pass through, so the filer's own segment operating income and the cash-flow statement
  are read rather than revenue.
- **Would the insiders write it down** **[M2000-105]**? They do: the commissions write the allowed return into orders, and
  the company files a capital plan ($809 for fiscal 2026, Item 7). This is not a forecast the industry declines to write.
- **The perimeter.** A regulated distributor of an essential fuel is the kind of business the rows describe as one where
  "you shouldn’t expect to make extraordinary profits" **[M2000-131]**, inside the circle by its simplicity. Doubt about
  the circle means outside **[M2002-092]**: I have none about understanding it; my doubts are about its returns and its
  price, which later questions own.
- **VERDICT: IN.** The ten-year economics of a regulated gas distributor can be foreseen within a band from its rate orders,
  its filed capital plan and its customer counts **[M2012-065]**, **[M2000-037]**; the one slow threat (electrification) is
  carried to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**

**The parts table** (five-year operating income, fiscal 2021-2025, from the segment tables of the fiscal 2022 10-K,
0001437749-22-027522, and the fiscal 2025 10-K, 0001193125-25-282583; USD M):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share | castle | decides? |
|---|---|---|---|---|---|---|---|---|---|
| Gas Utility (MO, AL, Gulf, MS) | 374.0 | 339.9 | 350.8 | 400.6 | 406.2 | 1,871.5 | 81.8% | regulated franchise | **yes, more than half** |
| Gas Marketing (sold 2026-04-30) | 58.5 | 46.9 | 49.3 | 41.2 | 42.1 | 238.0 | 10.4% | none claimed; "directly impacted by the effects of competition" (Item 1) | no; gone |
| Midstream and Other (storage sold 2026-06-30; pipelines kept; corporate) | 17.7 | 21.4 | 18.5 | 46.5 | 75.6 | 179.7 | 7.9% | storage "a competitive business" (Item 1A); pipelines tied to Spire Missouri | no |
| Consolidated | 450.2 | 408.2 | 418.6 | 488.3 | 523.9 | 2,289.2 | 100% | | |

The business that remains at the price date is the Gas Utility plus Spire Tennessee (acquired 2026-03-31; calendar 2025
excess of revenues over direct expenses $121.6M on its abbreviated statements, 8-K/A 0001193125-26-144025) and the two
pipelines. The file closes on the Gas Utility, the deciding part (the CONVENTION of section B); Spire Tennessee is the same
kind of castle under a fourth commission and is read with it.

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**: "Spire Missouri is the only distributor of natural gas within its
   franchised service areas, while Spire Alabama is the main distributor of natural gas in its service areas" (Item 1), over
   "more than 60,000 miles of mains and services" (Item 1). Nobody with money builds a second gas grid under St. Louis; the
   franchise is a municipal permit plus a state certificate. The answer to "could I do it?" is no. The castle against a
   second gas distributor stands.
2. **Pricing power and the agony before a rise** **[M2005-020]**: the business has none of its own. Prices are set in rate
   cases that "can take up to eleven months to be finalized" (Item 1) and through riders; the 2025 Missouri case granted
   $210.0 on a 7.05% post-tax return on rate base (Note 15). This is the monopoly without the pricing power: the regulator
   holds the switch. The rows say what the trade is: "in utilities the trade has been the compact has been that you get a
   modest return" **[M2024-011]**.
3. **Unit volume and share of mind** **[M1999-054]**: customers 1,735,633 (2023) to 1,744,537 (2025), about a quarter of a
   percent a year; residential volume 965.3M CCF (2023), 890.8 (2024), 948.8 (2025), weather-driven (Item 1 tables). Flat
   volume, not falling; the earnings grow by rate base, not by units.
4. **Would the customer still choose it over the low bid** **[M2017-009]**: the customer cannot choose another gas
   distributor; he can choose another fuel. "The principal competition for the Utilities comes from the local electric
   companies" (Item 1); the filer believes the cost comparison "will not change significantly in the foreseeable future"
   (Item 1). Large customers can bypass by connecting to interstate pipelines (Item 1A).
5. **Ask the competitors** **[M1999-130]**: the 10-K names its rivals only by kind (local electric companies, suppliers of
   fuel oil, coal and propane, interstate pipelines, district steam, adjacent municipal distributors): no named rival, so
   none to flag as a non-filer. **CONVENTION of this run:** the comparators are chosen by me, two gas distributors that file
   with the SEC (Atmos Energy, ATO, latest 10-K 0000731802-25-000056; ONE Gas, OGS, latest 10-K 0001587732-26-000009) and the
   electric company of the largest territory, Ameren (AEE, latest 10-K 0001002910-26-000009); rationale: the 10-K names
   categories, not companies, and the brief asks for SEC filers with the same metric in their own filings.
6. **Widening or narrowing** **[M1999-108]**: on the regulatory side, slightly better in Missouri (the 2025 rate order; the
   proxy credits management with supporting "the future test year legislation", Senate Bill 4), but the ISRS statute "will
   expire on August 28, 2029" absent legislation (Item 1A), and Spire Alabama's allowed RCE was cut from 10.15%-10.65% to
   9.50%-9.90% effective 2022-10-01 (Note 15). On the demand side, flat customers. Neither widening nor narrowing on the
   evidence; holding.
7. **What could destroy, modify or reduce it** **[M2000-014]**: (a) rules that restrict gas use or new gas connections
   (Item 1A, first risk: "restricting the use of fossil fuels, such as natural gas"), a slow change that "can lull you to
   sleep easier" **[M2014-038]**; (b) the regulatory compact itself, which the rows record breaking elsewhere: "it is
   difficult to project both earnings and asset values in what was once regarded as among the most stable industries in
   America" **[L2023-011]** (a pull carried OPEN in section VI); (c) a single accident: "A catastrophic event can render a
   single utility insolvent" **[L2005-019]**, softened here by four commissions and a holding structure.

**The competitor row: return on average common equity** (net income to common over average common equity, fiscal
2016-2025; XBRL company facts drawn from each filer's 10-Ks, transcription; script `scripts/peers.py`, output
`peers_out.txt`; Spire's equity is taken net of the $242.0 preferred from 2019):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | ten-year average |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Spire (SR) | 8.6% | 8.6% | 10.1% | 8.0% | 3.2% | 10.9% | 8.3% | 7.7% | 8.3% | 8.4% | **8.2%** |
| Atmos (ATO) | 10.5% | 10.8% | 13.9% | 9.7% | 9.6% | 9.1% | 8.9% | 8.7% | 9.1% | 9.3% | 10.0% |
| ONE Gas (OGS) | 7.5% | 8.5% | 8.6% | 9.0% | 9.0% | 9.0% | 9.0% | 8.6% | 7.6% | 8.1% | 8.5% |
| Ameren (AEE) | 9.3% | 7.3% | 11.0% | 10.6% | 10.2% | 10.6% | 10.6% | 10.5% | 10.1% | 11.4% | 10.2% |

(2018 is flattered across the field by the remeasurement of deferred taxes in the tax-law change; Spire's 2020 carries the
$148.6M impairment; its 2021 carries the Uri off-system sales and marketing gains the fiscal 2021 10-K describes.)

**The field's returns over the last full cycle, judged in words.** The span is ten years, at least two rate cycles in each
jurisdiction and one tax-law change. Every company in the field earns on book equity close to what its commissions allow,
around nine to ten percent, and Spire earns at the bottom of that band, below its own Alabama range in most years. These
are ordinary returns, held there by design: "The whole idea behind the utility industry is not to allow extraordinary
profits." **[M2000-131]** The castle protects a return, but not an excellent one, where the rows' moat "protects excellent
returns on invested capital" **[L2007-004]**. Section C would close a durable castle protecting only ordinary returns OUT;
the same item makes the exception for a return set by a regulator, carried to Q3 as a second best, the rows being "there’s
no way we get rich on our utility investments. But there’s no way we get poor, either." **[M2009-104]** and the 2009
letter's willingness to enter capital-heavy businesses that earn "decent returns on the incremental sums they invest"
**[L2009-012]**. This is that case: the return is set by four commissions on stated formulas.

**Change for the better?** None is credited: the Missouri legislation (Senate Bill 4) is a change in the rules, not yet
shown through a full rate cycle, and section C credits nothing until one has run.

- **VERDICT: IN**, as the regulated exception. The castle against a second distributor stands on franchise and certificate
  **[M2011-015]**; it protects only a regulated, ordinary return **[M2024-011]**, **[M2000-131]**, which section C carries to
  Q3 as a second best **[M2009-104]**, **[L2009-012]**; the slow threats (rules on gas use, the compact) are named and
  carried **[M2000-014]**, **[L2023-011]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The question: "does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**, and of
growth, "whether that’s good or bad depends on what we earn on that incremental $130 million over time" **[M2001-019]**.

**What it has earned on the capital it needs** (script `scripts/q3_returns.py`, output `q3_out.txt`; capital employed is
equity, including the preferred while outstanding, plus long-term debt, current maturities and notes payable, less cash;
goodwill of $1,171.6 is constant from 2017 to 2025 and removed for the tangible figure; filed balance sheets of the fiscal
2018, 2021 and 2025 10-Ks, three year-ends from XBRL, flagged):

| fiscal year | 2018 | 2019 | 2020* | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| operating income on average tangible capital, pre-tax | 8.3% | 7.7% | 8.2% | 9.4% | 7.4% | 6.8% | 7.4% | 7.4% |
| the same after tax at 24.7% (21% federal plus 3.7% state, Note 12) | 6.2% | 5.8% | 6.2% | 7.0% | 5.6% | 5.1% | 5.6% | 5.6% |

*2020 before the $148.6 impairment. The measure is "what it earns on capital" **[M1998-005]**, the capital "actually needed
in the business" **[M2010-090]**: about five to six percent after tax, which is the regulated return the castle protects.

**What the added capital earned.** Fiscal 2017 to 2025: operating income rose $183.0 while capital employed rose $4,001.4,
4.6% pre-tax and 3.4% after tax on the increment. Fiscal 2021 to 2025: $73.7 on $2,236.8, 3.3% pre-tax (the 2021 base carries
the Uri off-system sales). Fiscal 2022 to 2025, the kindest span: $115.7 on $1,468.6, 7.9% pre-tax, 5.9% after tax. Part of the
capital added is regulatory assets (gas costs deferred after Uri), and part is construction not yet in rates, so the measure
understates the eventual regulated return. The filer's own Missouri figures say the same in another way: fiscal 2025 net
income plus after-tax interest of Spire Missouri was 4.65% of the rate base the 2025 order recognizes ($4,379.6), against a
7.05% post-tax allowed return (Note 15): spending ran years ahead of recovery.

**How much must be reinvested to stand still, and how much to grow.** Capital spending ran at 2.93x, 2.33x, 2.60x, 3.09x and
3.09x depreciation in fiscal 2021-2025 (2.83x over the five years) while customers grew about a quarter of a percent a year
(Item 1). The 10-K describes the spending as "infrastructure upgrades, advanced meter installations, and new business" (Item
7) and Missouri's ISRS as recovery "for its investment to replace qualifying components of its infrastructure" (Note 15).
Most of it replaces old pipe and meters under federal safety rules (Item 1A: PHMSA integrity programs "may require
significant capital and operating expenditures"): spending the business must make to stay in its franchise, which the
regulator then pays a return on. The rows name both halves: "Every year we spend amounts equal to our depreciation charge
simply to stay in the same economic place" **[L2000-035]**, and for utilities, "To earn more, their owners must invest more."
**[L2011-019]**; "you have to keep putting more and more money into a public utility" **[M2005-052]**. Munger's warning is
the one that bites: "we have tried to avoid places where there was a lot of compulsory reinvestment just in order to stand
still" **[M1997-016]**.

**The growth arithmetic.** Earnings here grow by putting in capital, not by selling more gas: the 2023 meeting's line fits
it exactly, "we’re not earning a higher rate of return on capital than we were when we started. We just put way more capital
into the business" **[M2023-081]**. Whether that growth adds value depends on the incremental return against the rate, and
over the eight years read it has been 4.6% pre-tax, below the 5.43% long Treasury and far below the floor of about ten percent.
A regulated business is the rows' second best only on a condition: "We expect only that these businesses have reasonable
expectations of earning decent returns on the incremental sums they invest." **[L2009-012]**; "cash-consuming businesses, by
their nature, are unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**. The pull the
other way is real and is written down: the speakers like "a growing utility" because "we have such confidence that the
reinvested money is going to do exceptionally well" **[M2014-088]**, and the regulated return is near-guaranteed within a
range **[M2009-104]**; the 2025 Missouri order and Senate Bill 4 should narrow the lag that depressed the record.

- **WEIGHS AGAINST.** A capital-heavy second best **[M2018-055]** whose added capital earned 4.6% pre-tax over 2017-2025 and
  whose largest utility earned 4.65% after tax on its new rate base against 7.05% allowed, with reinvestment that is largely
  compulsory **[M1997-016]**, **[L2011-019]**: the condition of "decent returns on the incremental sums" **[L2009-012]** is not
  shown on the record. (The "little or no debt" criterion is applied at Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends and the latest quarter, before the income account** **[M2025-032]** (USD M;
2017, 2018, 2020, 2021, 2024, 2025 and 2026-06-30 read in the filed statements; the other year-ends from first-filed XBRL,
`tools/run.py` and `scripts/inst.py`, transcription):

| Sept 30 | total assets | net utility plant | goodwill | regulatory assets, non-current / current | shareholders' equity (preferred incl. 2019-2025) | retained earnings | long-term debt | current LTD + notes payable | deferred taxes | AROs | pension liability | shares (M) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 6,077 | 3,287 | 1,165 | 838 / 94 | 1,768 | 551 | 1,834 | 399 + ? | 607 | 206 | 304 | 45.65 |
| 2017 | 6,547 | 3,665 | 1,172 | 791 / 176 | 1,991 | 614 | 1,995 | 577 | 708 | 297 | 237 | 48.26 |
| 2018 | 6,844 | 3,970 | 1,172 | 670 / 73 | 2,255 | 716 | 1,900 | 729 | 436 | 321 | 180 | 50.67 |
| 2019 | 7,619 | 4,352 | 1,172 | 768 / 79 | 2,543 | 776 | 2,083 | 743 + ? | 451 | 338 | 265 | 51.00 |
| 2020 | 8,241 | 4,680 | 1,172 | 1,069 / 70 | 2,522 | 721 | 2,424 | 708 | 511 | 540 | 309 | 51.60 |
| 2021 | 9,356 | 5,056 | 1,172 | 994 / 306 | 2,658 | 843 | 2,939 | 728 | 612 | 520 | 236 | 51.70 |
| 2022 | 10,084 | 5,370 | 1,172 | 1,112 / 355 | 2,818 | 906 | 2,958 | 1,319 | 675 | 521 | 163 | 52.50 |
| 2023 | 10,314 | 5,779 | 1,172 | 1,249 / 348 | 2,917 | 958 | 3,554 | 1,113 | 744 | 577 | 137 | 53.20 |
| 2024 | 10,861 | 6,243 | 1,172 | 1,252 / 115 | 3,233 | 1,019 | 3,704 | 989 | 808 | 580 | 147 | 57.70 |
| 2025 | 11,575 | 6,757 | 1,172 | 1,324 / 78 | 3,389 | 1,088 | 3,369 | 1,805 | 887 | 583 | 75 | 59.00 |
| 2026-06-30 | 14,091 | 8,925 | 1,895 | 1,395 / 79 | 3,583 (no preferred) | 1,516 | 5,758 | 1,502 | 1,055 | 597 | 43 | 59.11 |

What the figures say. (1) Net utility plant doubled in nine years (3,287 to 6,757) and rose to 8,925 with Tennessee; the
balance sheet is the rate base, and the income account follows it. (2) Equity rose 1,768 to 3,389, but retained earnings
only 551 to 1,088 while net income over fiscal 2017-2025 summed to $1,881.6 (XBRL): the dividends took most of the earnings,
and the equity growth came from issuance (shares 45.65M to 59.00M) and the $242.0 preferred. (3) Debt rose faster than
equity: long-term debt plus current maturities plus notes payable from about $2,233 (2016, current maturities untagged) to
$5,174 (2025) and $7,259.6 at 2026-06-30, when equity was $3,583.0; the filer's own capitalization was "47% equity" at
2025-09-30 counting the current maturities but not the notes payable (Item 7). (4) Cash is never more than single digits:
the company lives on commercial paper (notes payable $1,317.0 at 2025-09-30), which matters at Q9. (5) Regulatory assets
grew 838 to 1,324 non-current while plant doubled, not out of line; the current spike of 2021-2023 is the Uri gas cost
deferral, collected by 2024 (306, 355, 348, then 115 and 78). (6) Goodwill was flat at 1,172 for nine years (no impairment of
the Alabama or EnergySouth goodwill) and rises by $741.7 for Tennessee. (7) Deferred taxes rose 607 to 887 while cash taxes
paid were under $3 a year (cash-flow supplements): the company pays almost no cash income tax (bonus depreciation and NOLs,
Item 1A; loss carryforwards $646.1, Note 12).

What they do not say and cannot say: whether the regulatory assets will be recovered (the auditor's critical audit matter is
"Regulatory Matters – Impact of Rate Regulation on the Financial Statements", 10-K pages 42-43: "management’s analysis of the
regulatory orders that support the probability of recovery"); whether the plant will earn its allowed return (Q3 says it
has not yet); and what Tennessee earns under Spire, since its 2024-2025 statements are abbreviated, exclude corporate overhead,
income tax and interest, and have no cash-flow statement (8-K/A Exhibit 99.1, Note 1).

**The real costs.** Depreciation is real **[R1996-023]**: $298.2 in fiscal 2025, against capital spending of $922.4; whether
it is enough to keep the business in place is the maintenance question, taken up at Q7 (e). Stock pay is small ($6.7) and
deducted. Restructuring and deal costs: excluded from "adjusted earnings" in every recent year ("Acquisition activities"
$2.5 in 2023, $7.6 in 2024 with restructuring, $15.2 in 2025; $26.4 of Tennessee transaction costs in the nine months of 2026,
10-Q Note 2); telling owners year after year to leave out business adjustments "is misleading" **[L2016-007]**, and I count
them. EBITDA: no instance found in the 10-K, the 10-Q or the August 2026 release (text search for "EBITDA"). Pensions:
liability down from 304 to 43, the expense largely deferred under regulation (Note 13); no fanciful assumption found in
the sensitivity table read.

**The habits, recorded here as a weighing and carried to Q5** (section A of the gaps case). (a) **An adjusted figure
featured**: the MD&A opens its results with "NON-GAAP MEASURES" and reconciles to "adjusted earnings", and the same
adjusted figures "determine incentive compensation" (Item 7); a management that would "wave away very real costs" makes the
speakers nervous **[L2016-006]**, here mitigated by small adjustments that are reconciled line by line. (b) **Guidance and a
growth target**: the August 2026 release "Reaffirmed fiscal 2026 adjusted earnings guidance", "Reaffirmed fiscal 2027
adjusted earnings guidance range of $5.40–$5.60" and "Reaffirmed long-term adjusted earnings growth target of 5-7%", and
states the target is measured "using the original fiscal 2027 adjusted EPS guidance midpoint of $5.75 as a base" (8-K
0001193125-26-333825, Exhibit 99.1), a base above the guidance now given for the same year. The rows on guidance: "the
scourge of earnings" guidance **[L2019-006]**; incredulity at those who "consistently reach their declared targets"
**[L2002-041]**. (c) The accounts themselves raise no suspicion of the kind that closes the file: no prepaid or deferred
accounts building out of line **[M1995-064]**, no profits on both sides of a contract, gas costs passed through by tariff and
audited by the commissions. One item I could not reconcile: the 10-Q's cash-flow summary of discontinued operations shows
Spire Storage "Net cash provided by operating activities" of $567.0 for nine months on $76.2 of revenue (10-Q Note 3), while
consolidated operating cash rose only $30.7 year on year; probably intercompany settlement before the sale, but the filing
does not say. It concerns a business sold, not the one valued, and does not confuse the continuing accounts.

**Equity-method income:** none material found. **The make-the-numbers tell in the ISRS history**: the fiscal 2021 and 2022
10-Ks carry "Missouri regulatory adjustments" and a "Missouri Supreme Court ruling" on ISRS charges recorded and later
reversed; recorded, weighed with (b), not a suspicion on its own.

- **VERDICT on the accounts: no STOP; WEIGHS AGAINST** on the habits (the adjusted figure featured and paid on, annual
  guidance with a growth target measured off a superseded base) **[L2016-006]**, **[L2019-006]**, **[M1994-018]**, carried
  to Q5; the statements themselves are clear enough to recast. **The recast for Q7:** owner cash = operating income after the
  company's tax, plus depreciation, less capital spending (or the maintenance guess at Q7 (e)), less stock pay, less the
  working-capital and other operating cash lines the cash-flow statement carries, with deal and restructuring costs counted,
  not added back **[L2021-003]**.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The two yardsticks: "how well they run the business" and "how well that they treat their owners" **[M1994-008]**; read
"the proxy statements" for "how they treat themselves versus how they treat the shareholders" **[M1994-009]**. For a stock
bought in the market the reading tests carry the weight (Q5, tests).

**The people, from the filings.** Scott E. Doyle, president and CEO since 2025-04-24, joined as COO in January 2024 from
CenterPoint Energy (10-K, executive officers; 8-K 0000950170-25-058353). His predecessor Steven L. Lindsey (the principal executive officer for fiscal 2024 and
part of 2025, after Suzanne Sitherwood for fiscal 2021-2023, proxy pay-versus-performance table) was CEO until his "employment as President and CEO of the Company was terminated without “Cause”" on 2025-04-24 (same 8-K), no
reason given in the 8-K or the proxy; the proxy shows $2,532,813 of "All other compensation" to him for fiscal 2025.
The CFO (Rasche) retired 2024-12-31; Adam Woodard, CFO from 2025-01-01, was treasurer before. A new COO from Enbridge from
2025-10-13 with a $1,400,000 special equity grant and a $250,000 hire bonus (8-K 0001193125-25-210056). The board: ten
directors, nine independent, an independent chair (Rob L. Jones); "There were no related party transactions in fiscal"
2025 (proxy). Ownership: directors and executive officers as a group 1,333,680 shares, 2.26%, of which 1,121,160 belong to
one director (Stupp); the CEO 3,420 shares, all restricted, plus 8,400 units (proxy ownership table).

**Integrity, the STOP.** What I looked for, and found or did not:
- *Reports that dance* **[M1995-111]**: the 10-K reconciles every adjusted figure to GAAP line by line, states the gas-cost
  pass-through plainly, and names its own risks (ISRS expiry, NOL value, ratings, storage competition). The risk of
  climate rules is stated against the company's interest. No dancing found.
- *The habits carried from Q4*: annual guidance and a 5-7% growth target, measured off "the original fiscal 2027 adjusted
  EPS guidance midpoint of $5.75" when the current guidance for that year is $5.40-$5.60. This is a promise-making habit,
  "things that they do in public in relation to their investors and the promises they make" **[M2004-067]**; the rows'
  warning is that those who always promise to make the numbers "will at some point be tempted to make up the numbers"
  **[L2002-041]**. Read with the rest of the record I find the habit, not the temptation acted on: the vesting record of the
  performance units (71%, 121%, 85%, 89%, 95%, 111% of target for 2018-2020 to 2023-2025, proxy) does not show targets
  always met, and the annual plan paid 95% of target in 2025 on adjusted operating income of $527.9 against a $537.0 target.
- *Errors found and corrected*: the fiscal 2021-2022 10-Ks record ISRS charges reversed after a Missouri Supreme Court
  ruling and "Missouri regulatory adjustments"; a regulatory dispute over which pipe qualified, disclosed, not concealed.
- *Affiliate dealing*: Spire STL Pipeline was built with Spire Missouri as "foundation shipper", and on 2021-06-22 the D.C.
  Circuit vacated its FERC certificate (fiscal 2021 10-K, Item 1A); FERC later let it operate and the pipeline now runs
  under one tariff with MoGas (Item 1). The filings read do not give the court's reasoning, so I record the fact and draw
  no conclusion on character from it.
- *How they talk about mistakes* **[L2024-003]**: the storage business, impaired by $148.6 in 2020 ($117.3 after tax, fiscal
  2021 10-K), expanded, then sold in 2026 at a pretax gain of $210.8; the marketing business sold at a pretax gain of $118.6
  (10-Q Note 3). The CEO describes the result as "transforming Spire into a simpler, fully regulated business" (release of
  2026-08-05). No filing read calls any of it a mistake; nor does any hide it.
- *The CEO change*: a chief executive terminated without cause after about a year and a half, with no stated reason, is a fact the
  owners were not told the why of. The rows ask whether management tells "about the things that we would want to know about
  if we owned a hundred percent of the company" **[M1998-036]**; an owner of the whole would want to know why. Weighed, not
  closing: nothing read suggests dishonesty, and silence about a personnel decision is the ordinary practice.

Doubt closes the file: "If you’ve got doubts, forget it." **[M2013-088]**. I have doubts about the promises and the pace of
spending, which are ability and capital questions; I find no doubt about honesty in what I read.

**Ability, the WEIGHING.** The record against the hand dealt **[M1994-008]**: the hand is four franchises with stated allowed
returns. The record: Spire earned 8.2% on common equity over ten years against 8.5% (ONE Gas) and 10.0% (Atmos), and
Spire Missouri earned 4.65% on its new rate base against 7.05% allowed (Q3); the diversifications (storage, the STL
pipeline, marketing) took capital for a decade, produced an impairment and a vacated certificate, and were then sold or
merged back; three chief executives across fiscal 2023-2025 (Sitherwood, Lindsey, Doyle). Against it: the 2025
Missouri order, the Missouri legislation the proxy credits to management, the sales of storage and marketing at gains above
book, and a constructive start with Tennessee. The rows put the business first, "And we still look to the underlying
business, though." **[M1996-037]**, and the moat and the management "enter into our thinking as to the degree of certainty that we attribute to the stream of income" **[M1999-104]**; here a
regulated business needs less of the lord's genius than most, and the record is the lord's: middling.

- **VERDICT on integrity: IN** (no doubt on honesty found in the filings read; the guidance habit and the unexplained CEO
  change recorded and weighed) **[M2013-088]**, **[M2004-067]**. **Ability WEIGHS AGAINST**: earned returns at the bottom of
  the field and below allowed, a decade of diversifications unwound, three chief executives in three years
  **[M1994-008]**, **[M1999-104]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
**The retention test** (script `scripts/q6_retention.py`, output `q6_out.txt`). The rule: retention must deliver "at least
$1 of market value for each $1 retained" **[R1995-009]**, checked over "three or four years" **[M1998-110]** or five. Here
the owners put in two kinds of dollar, the earnings kept and the new shares sold:
- fiscal 2021-2025: retained $383.5 plus new common issued $458.0 = $841.5; market value from $2,745.7 (2020-09-30, $53.20)
  to $4,812.1 (2025-09-30, $81.52), +$2,066.5, $2.46 per dollar put in. But the base is aberrational, a close 39% below the
  prior year-end ($87.24 at 2019-09-30, aggregator closes, flagged); "it will pay you to be suspicious as to why the
  beginning and terminal years have been selected" **[L2005-003]**.
- fiscal 2018-2025: retained $497.0 plus new common $673.3 = $1,170.3; market value $3,602.6 to $4,812.1, +$1,209.5, $1.03
  per dollar. Over the longer span the market leg is met with nothing to spare, and the intrinsic-value leg, which the
  2009 revision insists on **[R2009-002]**, is answered at Q7: the dollars went into rate base that earned 4.6% pre-tax on
  the increment (Q3), below the long Treasury.
- Payout of net income to common: 69.5% over fiscal 2018-2025; "22nd consecutive year of increasing dividends on an
  annualized basis" (Item 5). A dividend set by habit while the company sells stock to fund the capital plan is the policy
  the rows call nuts in its ratio form, "the idea of paying out 20 percent of your earnings, or 10 percent, or 30 percent of
  earnings in dividends strikes us as nuts" **[M2000-051]**, and it imposes "a specific cash-out policy upon all
  shareholders" **[L2012-014]**; here the cash paid out is raised again from the same owners by issuance.

**Buybacks.** None: "During the three months ended September 30, 2025, there were no repurchases" (Item 5), none in the
cash-flow statements read. Nothing to test against the Q7 range (the bottom of the range is written back below with Q7).

**Issuance and deals.** (1) *Issuance*: shares from 45.65M (2016-09-30) to 59.11M (2026-07-31), +29.5%, through the ATM, forward
sales, the 2021 equity units (2,745,733 shares for $175.0 in March 2024) and the 2024 offering ($287.0 of stock issued in
fiscal 2024), plus the $242.0 preferred (2019-2026) and $1,100 of junior subordinated notes (2025-2026, the $200 of January 2026 used to redeem
the preferred, 10-Q financing note). The rows' candidate second STOP: "we have never invested in companies that are hell-bent on
issuing shares" **[L2014-015]** (OPEN whether a STOP, section VI). A utility funding a filed rate-base plan is not the
promotion the row describes, but the habit is steady and is weighed against. (2) *The Tennessee deal, value given against
value got* **[M1995-001]**: $2,500.8 in cash (10-Q Note 2) for net assets of $1,759.1 and goodwill of $741.7; the business
earned $121.6 and $124.9 of revenues over direct expenses in calendar 2025 and 2024 before corporate overhead, interest and
income tax (8-K/A Exhibit 99.1). After interest income, other income and tax at 24.7% that is about $84 to $90 a year,
3.4% to 3.6% on the price, below the 5.43% long Treasury; the price is justified only by growth the seller's and buyer's
plans project. The rows' base rate: "the acquirer typically gives up more intrinsic value than it receives" **[L1994-015]**,
and the warning on the financing: "even a high-priced deal will usually boost per-share earnings if it is debt-financed"
**[L2017-004]**; the deal was paid with $825 of Spire Tennessee senior notes, $900 of junior subordinated notes and the sale
proceeds of storage and marketing (10-Q, financing note), and management's own claim is that it will "provide accretive
earnings" (10-Q Note 2). It was paid in cash, so Q6's all-stock STOP **[L2009-019]** does not apply. (3) *The sales*:
storage for $657 against a carrying value of about $442 (pretax gain $210.8) and marketing for about $212 (pretax gain
$118.6) (10-Q Note 3), both above book; recorded for the defence.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**: the annual plan pays on "adjusted operating income" weighted by
  business-unit budgets, safety and individual goals; the long-term plan is 75% performance units, of which 75% vests on
  "relative total shareholder return" and 25% on three-year average adjusted EPS, plus 25% time-vested restricted stock
  (proxy CD&A). Three quarters of the performance award rides on the share price against a peer group, which the person
  does not control, the "lottery ticket" the 1996 letter shuns **[L1996-018]**.
- **A capital charge**: none found in either plan. "In a capital-intensive business, you have to have something that —
  you have to have a factor in the compensation arrangement that includes a capital cost element." **[M2009-081]**; the
  plans pay for operating income and per-share earnings in a business that raises both by adding capital at 4.6% pre-tax
  (Q3). This is the weightiest Part B fact.
- **Size and terms**: CEO total compensation $3,328,340 for fiscal 2025 (summary compensation table), moderate for the
  industry; a departing CEO's "All other compensation" of $2,532,813; a new COO's $1,400,000 special grant. Clawback,
  hedging and pledging ban, ownership guidelines of 6x salary for the CEO, awards capped at 150% and 200% of target (proxy).
- **The board** **[M2007-120]**: an independent chair; nine of ten directors independent; directors paid $230,000 a year,
  $125,000 of it in stock; directors' holdings small except one family holder (1,121,160 shares). The board replaced a CEO
  without cause within about eighteen months of appointing him and approved a $2.48 billion acquisition financed largely
  with debt and hybrids.
- **The owners as partners** **[L1994-023]**: the reports are full and reconciled; the guidance habit (Q4) is the opposite
  of the rows' own rule.

- **Part A WEIGHS AGAINST**: dollars retained and raised returned about $1.03 of market value per dollar over eight years
  with the intrinsic leg failing at Q7; a habitual payout funded by habitual issuance **[L2014-015]**, **[M2000-051]**; a cash
  acquisition at about 3.5% on its price **[L1994-015]**, **[L2017-004]**; no STOP (no all-stock deal). **Part B WEIGHS
  AGAINST**: performance pay mostly on relative share price and adjusted EPS with no capital charge in a capital-heavy
  business **[M2009-081]**, **[L1996-018]**; the board's structure is sound.

## Q7: WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at "the yield on long-term U.S. bonds" **[L2000-021]**, the business getting credit only "for whatever net cash is left every
year" **[M1998-080]**. All arithmetic is in `scripts/q7_value.py`, output `q7_out.txt` (USD M unless per share).

**The inputs, and the conventions each uses.**
- **Basis (Q7, On what the floor is earned):** all-equity. Owner cash before interest, after the company's tax, against market
  value $4,849.0 plus net debt at 2026-06-30 of $7,238.9 (long-term debt $5,758.0 + current maturities $238.1 + notes payable
  $1,263.5 - cash $20.7; 10-Q balance sheet; "no significant finance leases", 10-Q; operating leases left out; the preferred
  redeemed in February 2026; the 10-Q states no subsequent events): enterprise value **$12,087.9**. The equity-only figure is
  beside it, on owner cash after the run-rate interest ($85.6 for the quarter to 2026-06-30, 10-Q, annualized $342.4, $257.8
  after tax).
- **Whose tax (Q7):** the company's own tax, taken at the statutory 24.7% (21% federal plus 3.7% state, Note 12).
  **CONVENTION of this run:** the statutory rate, not the cash rate, although cash taxes are under $3 a year; rationale: the
  shelter is bonus depreciation and NOLs that "begin to expire in fiscal 2030 for certain state purposes and fiscal 2037 for
  federal" (Note 12), so the section E convention (a shelter that runs out inside ten years) does not fit, and the deferral is
  a timing difference that a regulator deducts from rate base and that reverses when growth stops, which the no-growth tail
  requires; the rows treat a utility's deferred taxes the same way: "I don’t think I would look at that as a hidden form of
  equity" **[M2015-030]**. The cash-tax ceiling is shown in the floor test.
- **The business valued (c):** the business at the price date. The Gas Utility segment (the deciding part, Q2), the two
  pipelines and corporate costs, and Spire Tennessee; not Spire Marketing or Spire Storage, whose sale proceeds are already in
  the 2026-06-30 net debt (to count their past cash and their proceeds would count them twice). **Spire Tennessee**, closed
  2026-03-31, after the window, is valued on its own filed record, the abbreviated statements for calendar 2024 and 2025
  (8-K/A Exhibit 99.1): revenues over direct expenses less other income and interest income, $119.9 and $112.1 pre-tax, $87.4
  after tax on average; its financing is in the 2026-06-30 net debt. The statements exclude corporate overhead, so this
  overstates it. **Spire Mississippi** (signed, not closed, $75.0) stays in the central figure, the sale beside.
- **CONVENTION of this run (the pipelines and corporate):** the pipelines kept are taken at 27% of fiscal 2025 Midstream
  operating income ($83.8), the filer's own "net income mix of 73% and 27%" between storage and pipelines (Item 7), plus the
  Other segment's operating loss ($8.2): $10.9 after tax, held flat; rationale: the filer reports storage and pipelines
  together until 2026 and gives only that mix.
- **The cycle base (a):** fiscal 2021 is aberrational on the filer's own description ("higher off-system sales ... during
  the cold weather events in February 2021", fiscal 2021 10-K). **CONVENTION of this run:** the Gas Utility's base is the
  average of fiscal 2022-2025, four years, and its growth is measured 2022 to 2025, the literal five-year window shown beside;
  rationale: a weather event is one year, not a cycle with a peak-to-peak span to average over.
- **Working capital (d):** the cash-flow statement's working-capital and other operating lines (receivables, inventories,
  regulatory assets and liabilities, payables, billings, taxes accrued, "Other assets and liabilities", "Other") were
  -302.0, -461.0, -69.0, +326.1 and -49.2 in fiscal 2021-2025; the five-year mean of **-111.0** is charged, all five years
  kept because the Uri build (2021-2022) and its collection (2023-2024) both fall inside the window. The recurring "Other assets
  and liabilities" outflow (-93 to -118 in four of the five years) is a real operating cash cost and is charged.
- **The maintenance guess (e):** the filing allows one: depreciation, "not inappropriate in most companies to use as a proxy
  for required capital expenditures" **[M1998-127]**, with customers growing a quarter of a percent a year. If anything it is
  low (Q3: most spending replaces pipe; BNSF's case, "must annually spend more than its depreciation charge to simply maintain
  its present level of business" **[L2023-009]**), so the maintenance-only case flatters.
- **Growth shown:** Gas Utility operating income 339.9 (2022) to 406.2 (2025), **6.12%** a year, aggregate, not per share
  (literal 2021-2025: 2.09%). **The cap (f):** the owner-cash share of Gas Utility revenue peaked at 14.4% (fiscal 2020) in
  the filings read; carried ten years at 6.12% against revenue growing at its own 4.29% (2022-2025) it would reach 15.2%, so
  the cap binds and would cut the rate to 4.29%. But (e) forbids charging the growth spending and also capping the growth it
  bought, so the central growth end is the shown 6.12% with the growth spending charged, and the capped case is shown beside
  (see "What in the framework was wrong or unclear").
- **Growth spending charged (e):** Gas Utility capital spending less depreciation, fiscal 2022-2025 average, **$402.9** a year,
  grown with the business for ten years, then stopped with the growth.

**The base.** Maintenance-only owner cash, before interest, after tax: Gas Utility $281.9 + working capital and other
-$111.0 + pipelines and corporate $10.9 + Spire Tennessee $87.4 = **$269.1** a year, 2.23% of the enterprise value. The
all-spending base is **-$265.4** (Tennessee alone -$44.3 on its calendar-2025 spending of $167.5): not positive.
Literal window beside (consolidated as filed, all businesses): after all spending -314.6, -413.3, -135.4, +24.2, -195.2,
mean **-$206.9**; after depreciation only, mean **$304.0**.

**The range, at 5.43%, all-equity (central):**

| case | value of the business | less net debt | per share |
|---|---|---|---|
| no growth, maintenance only (top) | $4,956.0 | -$2,282.9 | **-$38.62** |
| growth at 6.12% for ten years, growth spending charged, then none (bottom) | $4,292.3 | -$2,946.6 | **-$49.85** |
| beside: growth cut to 4.29% by (f), spending charged | $3,438.0 | | -$64.30 |
| beside: literal-window growth 2.09%, spending charged | $2,577.1 | | -$78.86 |
| beside: literal window, consolidated, maintenance at D&A, no growth | | | -$27.75 |

**The growth inverts the range** (e): $402.9 a year of growth spending buys about $17 to $18 a year of added owner cash, a
return near 4% on the spending, below the 5.43% rate, so the growth case is the bottom and the no-growth case the top. That
is the finding, "growth can destroy value if it requires cash inputs in the early years of a project or enterprise that
exceed the discounted value of the cash that those assets will generate in later years" **[L2000-023]**, and it is Q3's
finding in cash.

**Value range: -$49.85 to -$38.62 a share (all-equity), against $82.03.** Equity-only beside: -$7.71 (growth) to $3.52 (no
growth) a share at 5.43%.

**The floor, tested first** (2026-10-10). The expected return at the price, on the enterprise value: central no-growth 2.23%;
central growth case 2.82%. The most generous case I can defend (fiscal 2025 run-rate Gas Utility income, the 18.0% effective
book tax rate of 2025, no working-capital drag at all, Tennessee before its interest income is removed, growth 6.12% uncapped,
growth spending charged): 3.68% at no growth, 4.09% with growth. Even the indefensible ceiling (that case with the growth
spending not charged at all) returns 5.42%. The defence's best new fact, the fiscal 2026 step-up from the Missouri rate order
(nine-month continuing operating income $488.8 against $434.9, 10-Q), would add perhaps $75 a year after tax to the base;
the no-growth return would still be about 2.8%. **No case earns the floor of about ten percent at the price** **[M2003-149]**:
"there’s just a point at which we drop out of the game". The width test does not arise; nor the screamer **[M2009-005]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged,
after the company's tax: **all-equity (central): -$90.95 a share** (no growth -$76.93, growth -$104.97); **equity-only beside:
-$12.11 a share** ($1.91 and -$26.13). Neither is positive: at ten percent the business is worth less than its debt. No cheap
price is reported. Beside: the Mississippi sale (+$75.0 cash, its earnings out), the $50.0 deferred storage consideration,
and the October 2026 $350 Spire Missouri bonds if not used to repay notes (net debt $7,588.9) move the per-share figures by
under $6 either way and change no conclusion.

- **VERDICT: OUT.** No case in the range earns the floor at $82.03: the business is worth less than its net debt at the long
  Treasury rate on every case built, and the price stands above the top of every range **[M2003-149]**, **[L2013-012]**;
  growth bought at about 4% on its cost lowers the value rather than raising it **[L2000-023]**.

**Written back to Q6 (the buyback line):** the bottom of the Q7 range is -$49.85 a share (all-equity); no repurchases were
made, so there is nothing to read against it.

---
## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP. NOT REACHED (Q7 closed the file OUT).
## Q9: COULD IT RUIN US? WEIGHING. NOT REACHED (facts under AFTER THE STOP).
## Q10: IS IT THE FAT PITCH? WEIGHING. NOT REACHED.
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED (a gas distributor; no named business of Q12).


---
## THE BOX
**OUT at Q7, on the floor**: value range -$49.85 to -$38.62 a share (all-equity, 5.43%) against $82.03; no case built earns
the floor (best defensible case 4.09% at the price); fair price -$90.95 all-equity, -$12.11 equity-only, neither positive.
Q1 IN; Q2 IN as the regulated exception; Q3 weighs against; Q4 no STOP, weighs against; Q5 integrity IN, ability weighs
against; Q6 weighs against in both parts. Not a TOO HARD, so no research pass.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on questions not reached, each with its source **[M1997-127]**; no verdict; the box is
unchanged.)*
- **Q9, the debt.** Long-term debt $5,758.0, current maturities $238.1, notes payable (commercial paper) $1,263.5, cash $20.7
  at 2026-06-30, against shareholders' equity $3,583.0: debt about 67% of debt plus equity (10-Q balance sheet). The $400
  delayed-draw term loan of 2026-08-31 requires "a consolidated capitalization ratio of not more than 70% at the end of each
  fiscal quarter" (8-K 0001193125-26-378491; the agreement's definition was not read and may differ from my ratio). Ratings
  BBB / Baa2 at Spire Inc., S&P outlook negative (10-K Item 7). Short-term needs met by commercial paper up to $1,500.0 and a
  $1,500.0 revolver, extended to 2031-10-11 (8-K 0001193125-26-420501). Interest at the run-rate is about $342 a year (10-Q,
  quarter to 2026-06-30, annualized) against fiscal 2025 pre-tax income of $331.4 plus interest of $204.1 (10-K). Spire
  Missouri's gas hedges can require margin deposits (Item 1A). The "little or no debt" criterion **[R1997-001]** is not met.
- **Q9, one event.** Explosion, leak and storage-field risks are named (Item 1A), "To the extent ... self-insured or not
  fully covered by insurance"; four utilities under four commissions after 2026, not one **[L2005-019]**.
- **Q8.** The 30-year Treasury yields 5.43%; the business's best defensible expected return at the price is 4.09% (Q7).
- **Q10, Q12.** Nothing found that bears on them beyond the above.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 68463bbf); written question by question; committed after each (Step 0
      and Q1, Q2, Q3, Q4, Q5, Q6, Q7, close).
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (operator rule ten); this
      run binds nothing until it is folded into the register.
- [ ] **Slip, declared:** one directory listing of `Test Runs/` filtered for today's date (to confirm my own file name before
      copying the template) showed the names of other companies' run files and research folders dated 2026-10-18, which the
      blind rule forbids listing; none was opened, read or searched, and nothing of them is used (declared under
      contamination at the top). No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened, listed or
      searched.
- [x] Every v5 id resolves (`scripts/check_cites.py`: every M/L/R id in `principle_ledger_v5.csv`, every quoted fragment
      directly before an id found in that row, no E-ids); every filing fact has its accession; three year-ends of the Q3
      capital table and several balance-sheet cells are XBRL transcription, flagged where used.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; nothing after it is a clearance (Q8 to Q12 not
      reached; facts for Q9 under AFTER THE STOP).
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): built from segment operating income after
      tax, depreciation, capital spending or the stated maintenance guess, stock pay inside operating expense, and the
      cash-flow statement's working-capital and other operating lines; the sovereign from the US Treasury; aggregator quotes
      (the price and the fiscal year-end closes of Q6) flagged.
- [x] Contrary evidence written down as it was found **[M1997-127]** (foundations, then each question); facts for later
      questions under AFTER THE STOP; Q5 was answered, so no integrity flag is needed in the box line.
- [x] Not a point-in-time run; no anchor bars any row.
- [x] Only the arithmetic lines of `tools/run.py` were used (its debt line "CapitalizationLongtermDebtAndEquity" includes
      equity and was ignored).
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded below).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 (e) against Q7 (f).** The cap of (f) binds here (the shown 6.12% growth would carry owner cash to 15.2% of revenue
against a 14.4% historical peak), but (e) says "Never charge all spending and also cap the growth that spending bought."
Applying both would charge $402.9 a year of growth spending while crediting only 4.29% growth. I made the central growth end
the shown rate with the spending charged and showed the capped case beside; the text should say which of the two rules gives
way. (2) **"Sales" in the cap (f) for a pass-through business.** A gas utility's revenue includes the cost of gas passed to
customers (fiscal 2023 revenue $2,456.9, fiscal 2025 $2,207.6, with higher operating income in 2025), so owner cash as a share
of revenue moves with gas prices, not with the business; the filer's contribution margin would be the economic sales. I used
revenue as written. (3) **Businesses sold after the window.** Specific (c) values a deal closed after the window "on its own
filed record" and says nothing of a business sold after the window whose cash sits in the window's average and whose
proceeds sit in today's net debt. I removed the sold businesses from the base and kept the proceeds in net debt; a sentence
in (c) would settle it. (4) **An acquired business filed only on abbreviated statements** (no cash-flow statement, no
corporate overhead, no tax): "its own filed record" had to be read as revenues over direct expenses taxed at the statutory
rate, which overstates it. (5) **A one-year aberration that is not a cycle.** Specific (a) prescribes a cycle average; a
weather event (Uri, fiscal 2021) has no peak-to-peak span, and I set the year aside as a CONVENTION of this run. (6) **Whose
tax for a regulated company.** Section E covers carryforwards that run out inside ten years; it does not say what to do where
cash tax is near zero because of accelerated depreciation and NOLs expiring beyond ten years, and the regulator returns the
deferral to customers through rate base. I used the statutory rate as a CONVENTION of this run. (7) **Q2's regulated
exception sends the case to Q3 "as a second best"** but does not say what Q3 should do when the incremental return on the
regulated capital is below the long Treasury; the weighing carried it to Q7, where the floor closed it, which seems the right
outcome but rests on my reading.

**Acceptance test:** `python tools/check_framework.py` run before the closing commit: result recorded in the commit message.
