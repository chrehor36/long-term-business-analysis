# Company Run — ClearSign Technologies Corporation (Nasdaq: CLIR) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-12, after the run was committed: `PORTFOLIO.md` does not name CLIR or ClearSign; not held.*

**Dispatch.** Run by a dispatched analyst in an unattended overnight cycle under `Screens/_daily/_dispatch_brief.md`. The
brief's one stated departure: the lines of evidence and the competitors were not written by the dispatcher; they are derived
here from the latest 10-K (below, "Lines of evidence chosen").

**Contamination declared (seen by accident, not used).** The session context showed the repository's git status and
recent commit subjects: research-folder file names for AYI and ARCB runs, and commit subjects for a BOUYF run and fold of
2026-10-12. A memory index line named a wave count and a count of gate-clearers. None of it names ClearSign, CLIR or
ClearSign Combustion, and none of it was used. No `Test Runs/` file other than the template and this file was opened,
listed or searched; `ls "Test Runs" | grep -i clir` was run once at the start to confirm the dated file name was free (it
returned nothing). This is declared as a listing of `Test Runs/` filtered to this name.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $3.21 (close 2026-10-09, the last trading day before the run; `tools/run.py`, **aggregator, live quote only, flagged**
  per operator rule 5). Reference points from filings, not used as the price: the public offering of 2026-05-28 at $4.33
  (8-K 2026-06-01, 0001104659-26-068614) and the private sale of 2026-07-21 at $3.54 (8-K 2026-07-23, 0001104659-26-086099).
- **Shares by class** from the latest filing's cover: **6,807,455 common** (10-Q for the quarter to 2026-06-30, filed
  2026-08-14, accession `0001104659-26-096539`; `python Screens/cover_shares.py CLIR`). One class; preferred authorized, none
  issued. Check against the filed balance sheet: 6,307,455 shares issued and outstanding at 2026-06-30 (no treasury shares),
  plus the 500,000 shares sold to Otter Capital LLC on 2026-07-21 (8-K 0001104659-26-086099) = 6,807,455, which matches the
  cover. No later 8-K or prospectus reports a further issuance; an at-the-market programme of up to $6,875,000 with
  H.C. Wainwright was recommenced on 2026-07-06 (8-K 0001104659-26-080744; 424B5 0001104659-26-080740), so the count can rise
  without a separate 8-K. Pre-funded warrants are counted in the loss per share and are exercisable at $0.001 (10-Q Note 9);
  the 1-for-10 reverse split of 2026-03-16 (8-K 0001104659-26-025867) is reflected in every post-split figure here.
- **Market cap:** 6,807,455 × $3.21 = **$21.85M**. Net cash $11.64M (cash $9.889M at 2026-06-30 plus the $1.749M net
  proceeds of the private sale, which the 10-Q states as a subsequent event; no borrowings; lease liabilities $0.117M,
  operating leases, left out). Market value plus net debt: **$10.21M**.
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-03-31, accession 0001104659-26-037699 (Items 1, 1A, 7, the
  statements); 10-Q for the quarter to 2026-06-30, filed 2026-08-14, 0001104659-26-096539 (statements, Notes 5, 9, MD&A);
  DEF 14A filed 2026-04-28, 0001104659-26-049883 (pay, ownership); 8-Ks of 2026-06-01, 2026-06-18, 2026-07-06,
  2026-07-23, 2026-08-11, 2026-08-20, 2026-09-14; for the earlier years, the cash-flow and income statements of the 10-K for
  FY2023 (0001558370-24-004441, carrying FY2022) and the 10-K for FY2021 (0001558370-22-004842).
  **One figure cross-checked against the filed statement:** net cash used in operating activities FY2025 **$(4,736)k** in
  the filed cash-flow statement of 0001104659-26-037699 equals the `tools/run.py` OCF line (-4.7M) and the XBRL value.
- `python tools/run.py CLIR` arithmetic lines only (its v4 text, ids and floor ignored, Part VII): OCF FY2022 -5.0M, FY2024
  -4.4M, FY2025 -4.7M; SBC 0.4M, 0.5M, 0.9M; D&A 0.2M each year; fixed-asset capex near zero; patent spending
  (PaymentsToAcquireIntangibleAssets) 0.1M to 0.2M a year, which the tool lists as an alternate capital payment. The
  tool's FY2023 column is missing; it was taken from the filed statement. Owner cash by year is computed below from the
  filed statements (`Test Runs/_research 2026-10-12 CLIR/compute.py`):

  | FY | OCF | less SBC | less stock for services | less bonuses paid in stock (supplemental) | less fixed capex | less patents | **owner cash (after interest received)** | interest income | **before interest** |
  |---|---|---|---|---|---|---|---|---|---|
  | 2021 | -6,707 | 680 | 33 | 217 | 73 | 140 | **-7,850** | 1 | **-7,851** |
  | 2022 | -4,992 | 373 | 26 | 107 | 10 | 154 | **-5,662** | 83 | **-5,745** |
  | 2023 | -3,233 | 614 | 10 | 234 | 0 | 200 | **-4,291** | 324 | **-4,615** |
  | 2024 | -4,373 | 528 | 29 | 326 | 39 | 179 | **-5,474** | 516 | **-5,990** |
  | 2025 | -4,736 | 893 | 65 | 279 | 4 | 97 | **-6,074** | 439 | **-6,513** |
  | mean | | | | | | | **-5,870** | | **-6,143** |

  (USD thousands. The "bonuses paid in stock" column is the cash-flow statement's supplemental line "Officer and employee
  equity awards for prior year accrued compensation": a cash bonus accrued in one year and settled in shares the next, so the
  cost never passes through operating cash; it is a real cost and is deducted. With the SBC line alone the mean is -5,638.)
  **Owner cash is negative in every one of the five years, and in every year back to the first filed cash-flow statement
  read (OCF FY2016 to FY2025 runs -8.7M to -3.2M, XBRL, the filed FY2021 to FY2025 statements checked).**

**Lines of evidence chosen, and why** (the brief's departure: derived here from the 10-K). Item 1 says the operations "have
been funded primarily through sales of our equity securities"; Item 1A's first risk factor says "we may never be profitable";
Item 7 says "Our revenues to date have not been sufficient enough to meet operating expenses." The lines this name needs are
therefore: (1) whether the business has ever earned its own costs, and for how long it has tried (revenues, operating loss,
accumulated deficit over ten years); (2) how it has been paid for (equity raised, shares outstanding over ten years); (3)
whether its own officers can say where its economics will be in ten years (the 10-K's statements on adoption and
profitability); (4) customer concentration and the order book (Item 1, the 10-Q revenue note); (5) the field it sells into and
who leads it (Item 1, "Competition and Barriers to Entry"); (6) dependence on regulation (Item 1, "Government Regulation";
Item 1A). Lines (1) to (3) decide Q1; (4) to (6) are recorded for the later questions.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, bought for the cash the business produces, and the
test is "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. A company that has met its
costs every year since 2008 by selling new shares (MD&A: "As of December 31, 2025, we have raised approximately $105.3
million in gross proceeds through the sale of our equity securities", 0001104659-26-037699) depends on an open market to
continue; with the market closed for five years it would have had to cut back or stop, by its own MD&A ("we may be required
to scale back our development [...] or even to cease, our operations"). Who is paid to tell you: the shares reach the market
through an underwriter (Newbridge Securities, 2026-05-28) and an at-the-market agent (H.C. Wainwright, from 2025-07-17), and
"you do not get impartial advice from Wall Street" where there is an "enormous amount of fees possible from one action"
**[M2020-037]**; nothing here rests on any projection the company or its agents publish **[M2011-083]**. The margin of safety
cannot be argued for a business with no positive cash to discount **[M1996-084]**. The analyst's habit applied: look for
"what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: revenue has grown in
each of the last three years ($374k 2022, $2,403k 2023, $3,596k 2024, $5,234k 2025); gross profit turned positive from 2022
($116k to $1,424k); a regulator (SCAQMD, 2024-02-02) set new BACT guidelines from the performance of the company's installed
burners; an independent study (ICF, 2024-10-02) reported fuel savings of 3.3% and 4.7%; Zeeco, which the 10-K calls one of the
world's largest burner makers, launched a co-branded ClearSign Core line in December 2024; operating expenses fell 17% in
the first half of 2026 (10-Q). These are the evidence for the business; none of them has yet made operating cash positive.

## THE STANDING RULE
Owning a part-interest bought for cash, unlevered, puts the buyer at no risk of ruin from this purchase: the loss is capped at
the price paid, and "Never risk permanent loss of capital" **[L2023-005]** binds how much is put in, not whether the question
is asked. The rule bears on sizing only: a business whose filings say it "may never be profitable" carries a real chance of a
total loss on the money put in, and "anything times zero is zero" **[M2007-050]**. Recorded; it closes nothing.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10 years"
  **[M2000-037]**, "a reasonable fix on about what the earning power and competitive position will look like in five or 10
  years" **[M2012-065]**. The product can be understood from Item 1: a flame-holder (porous ceramic or metal) placed
  downstream of a burner's fuel injection so that a premixed flame forms on it, short and cool, cutting NOx to 5 ppm or below
  without catalysts or flue-gas recirculation. The product is not the question: understanding, in the row, is not
  knowing "what a certain business does" **[M2012-065]**.
- **The key variables** "and evaluating how predictable they were first" **[M1998-044]**: (a) the rate at which refiners,
  midstream operators, boiler owners and flare operators adopt a new burner technology; (b) whether NOx rules tighten,
  where, and when; (c) whether the large burner makers (Honeywell's Callidus, Eclipse and Maxon; Koch's John Zink; Zeeco;
  others, Item 1) carry the technology, copy it, or answer it; (d) the price ClearSign can earn per burner once it competes.
  The filer says of (a): "we cannot predict the rate of adoption or acceptance of our technology by potential customers"
  and "Market acceptance of our technology and business is difficult to predict" (Item 1A, 0001104659-26-037699); of (b):
  "such initiatives continue to be controversial and subject to frequent changes" and the EPA rescinded the 2009
  endangerment finding in February 2026 (Item 1); of its own result: "We may never generate significant revenue and we may
  never be profitable" (Item 1A). The people closest to the business will not write the ten-year economics down: the test
  of **[M2000-105]**, "They would say, “That’s too hard.”", is met by the company's own filing.
- **Do the past statements tell the future ones?** **[M2008-033]**. They do not: ten years of filed statements show an
  operating loss every year (FY2016 -11.2M; FY2019 -8.6M; FY2022 -6.1M; FY2025 -6.7M; first half 2026 -3.8M), revenue
  between nil (FY2019, FY2020) and $5.2M (FY2025), three customers at 81% of FY2025 revenue (Birwelco 66%), and an
  accumulated deficit that rose from $40.3M (end 2016) to $108.0M (2026-06-30). The figures say what the business has
  cost; they do not show what it will earn, because it has never earned.
- **What the filer calls itself.** MD&A: "other costs associated with an early stage, publicly traded technology company";
  Item 1A: "We are a company with a limited operating history and limited revenues to date. We have incurred losses since
  our inception"; Item 1: "To date, our operations have been funded primarily through sales of our equity securities." The
  company was incorporated on 2008-01-23 (Item 1). Eighteen years on, it is in its own words early stage, its development
  "has transitioned from research to commercialization" (Item 1), and it has never covered its costs.
- **Routing.** Q1's list of what it rules OUT begins: "Start-ups are not our game." **[L2007-015]**; "We don’t do
  startups." **[M2008-088]**, a filter applied "about halfway through the first sentence" so that "a whole layer of
  complexity" goes out. **CONVENTION of this run** (the text names start-ups and does not define one): a start-up is read
  by its economics, not its age: a business that has never met its costs from its own sales, is funded by issuing shares,
  and describes itself as early stage. Rationale: the rows exclude start-ups for the complexity of judging an unproven
  business, which is the same whether it was founded last year or in 2008; ClearSign meets all three marks on its own
  filing. The letter row on the same ground: "This kind of uncertainty frequently occurs when new businesses and rapidly
  changing industries are under examination. In cases of this sort, any capital commitment must be labeled speculative."
  **[L2000-026]**.
- **Why OUT and not TOO HARD.** Two routes lead here and they agree that the file closes. The start-up item stands in the
  list of what Q1 rules OUT **[L2007-015]**, **[M2008-088]**, and the business meets it on the filing, so the question is
  answered against the name. Had the start-up item not applied, the file would close TOO HARD (NATURE), not WORK: the
  deciding question (will conservative customers adopt the technology fast enough, against incumbents with "resources that
  are substantially greater than ours", for the company to earn its costs) is one the company itself says it cannot
  predict, "If something’s important but unknowable, forget it." **[M2006-076]**, and "if we can’t make a decision in five
  minutes, we can’t make it in five months" **[M2008-086]**. The doubt row decides the margin in either case: "if you have
  doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. Price does not reopen it: "It
  doesn’t mean it isn’t a good buy. [...] It just means that we don’t know how to evaluate it." **[M2000-038]**.
- **VERDICT: OUT.** A start-up by its economics on its own filing (never profitable since its incorporation in 2008, funded
  by $105.3M of equity sales to the end of 2025 and about $5.2M more, net, in 2026, "early stage" in its own MD&A, 0001104659-26-037699)
  **[L2007-015]**, **[M2008-088]**, **[L2000-026]**; its ten-year economics are not foreseeable, by the filer's own statement
  that it cannot predict adoption **[M2000-037]**, **[M2000-105]**. The file closes here; Q2 to Q12 are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED.
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0's order, below under AFTER THE STOP, as the template asks when the file closes before Q4).
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (the reporting figures are computed below under COMPUTATION NOT A CLEARANCE).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT at Q1** (a start-up by its economics on its own filing; its ten-year economics not foreseeable by the filer's own
statement). **Integrity facts recorded, not judged** (an SEC inquiry into trading in the company's securities in 2020; a
2025 board contest settled by cooperation agreements; three former directors suing for advancement of legal fees; see
AFTER THE STOP, Q5). The COMPUTATION below shows a value range negative on every case (all-equity no-growth case
**-$14.40** a share against **$3.21**); it is not a clearance and decides nothing.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.)*

**Bearing on Q2 (the castle).**
- Rivals the 10-K names (Item 1, "Competition and Barriers to Entry", 0001104659-26-037699): Callidus, Eclipse and Maxon
  (Honeywell subsidiaries; Honeywell files with the SEC); John Zink Hamworthy Combustion (Koch Industries; **private, does not
  file**); General Electric (files); Haldor Topsøe (**Danish, does not file with the SEC**); Hitachi (**Japanese, does not file
  a 10-K or 20-F**); Linde (files); Zeeco (**private, does not file**; also ClearSign's sole process-burner subcontractor and
  co-branding partner); Fives Group (**French, does not file**); Cleaver Brooks (**private**); Power Flame (Aztec Inc.,
  **private**). The rivals' filings were not read: Q2 was not reached. The analyst's expectation, not a read fact: the three
  that file are conglomerates whose burner lines are not reported as segments that would compare. Recorded as not done.
- The 10-K's own description of the field: the incumbents' products "have become commoditized with differentiation
  between suppliers most often based on price"; "There is very little differentiation between the products offered by the
  established burner equipment providers, which results in thin profit margins for the sale of new or replacement burners.
  A significant portion of a company’s profit results from the sales of replacement parts and equipment upgrades."
- Customer concentration: Birwelco 66%, Customer A 3%, Customer B 12% of FY2025 revenue (81% together); the two California
  refinery customers were 86% of FY2024 revenue (Item 1). Customers in the United States were 100% of revenue in FY2024,
  FY2025 and the first half of 2026.
- Performance: the twenty burners for a California refinery (ordered 2022, shipped Q3 2024, installed Q3 2025) "have met
  applicable emissions requirements up to 80% of the specified normal firing rates", and an adjustment for full firing
  "affected burner compliance with our emission guarantees"; the warranty accrual was raised by $410k in Q1 2026, and the
  warranty liability stood at $1,114k on 2026-06-30 against $471k at the start of 2025 (10-Q Note 5 and MD&A,
  0001104659-26-096539).
- Dependence on regulation: Item 1 says the standards "are a significant driver for our development and sales efforts";
  Item 1A: "If federal, state or local regulatory agencies relax the clean air regulations [...] our business and results of
  operations could be materially adversely affected"; the EPA's final rule rescinding the 2009 endangerment finding was
  published 2026-02-18, which the company says does not touch NOx rules.
- Protection: 75 active patents and 20 pending at 2025-12-31, "the majority approximating 11 years of life remaining"
  (Item 1).

**Bearing on Q3 (capital).** Gross equity raised to 2025-12-31: about $105.3M (MD&A); in 2026, $3,413k net from the public
offering and $1,749k net from the private sale. Accumulated deficit $108.0M at 2026-06-30. The company calls its model
"asset light" (fixed assets $141k at 2026-06-30); the capital consumed is operating loss, not plant.

**Bearing on Q4 (the accounts): the balance sheets, ten year-ends and the latest quarter, read before the income account**
**[M2025-032]**. USD thousands; FY2016 to FY2025 from `tools/run.py`'s first-filed XBRL table, FY2021 to FY2025 checked
against the filed statements read; 2026-06-30 from 0001104659-26-096539; share counts from the filed balance sheets.

| year-end | assets | liabilities | equity | cash | receivables | patents and intangibles | debt | accumulated deficit | shares outstanding (pre-split basis) |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,786 | 2,042 | 2,244 | 1,259 | 103 | 1,735 | none | -40,331 | 12.98M |
| 2017 | 4,161 | 1,729 | 2,432 | 1,247 | 0 | 1,856 | none | -50,011 | 15.61M |
| 2018 | 18,637 | 1,728 | 16,909 | 8,949 (plus 6,923 T-bills) | none | 1,759 | none | -59,511 | 26.70M |
| 2019 | 10,942 | 1,716 | 9,223 | 8,552 | none | 1,285 | none | -67,990 | 26.71M |
| 2020 | 11,121 | 1,580 | 9,540 | 8,824 | none | 1,302 | 251 (PPP loan, forgiven 2021) | -74,874 | 30.08M |
| 2021 | 9,363 | 1,081 | 8,282 | 7,607 | 33 | 799 | none | -82,765 | 31.58M |
| 2022 | 10,925 | 1,373 | 9,552 | 6,451 (plus 2,606 T-bills) | 79 | 798 | none | -88,523 | 38.02M |
| 2023 | 7,620 | 2,428 | 5,192 | 5,684 | 287 | 836 | none | -93,717 | 38.69M |
| 2024 | 15,916 | 2,152 | 13,764 | 14,035 | 165 | 830 | none | -99,016 | 50.29M |
| 2025 | 12,181 | 2,651 | 9,530 | 9,178 | 1,360 | 760 | none | -104,512 | 53.29M |
| 2026-06-30 | 12,190 | 2,356 | 9,834 | 9,889 | 234 | 737 | none | -108,009 | 63.07M (68.07M with the July sale) |

What the figures say: the balance sheet is cash and little else; equity is refilled by share sales (2017, 2018, 2020 to 2022,
2024, 2026) and drained by losses between them; the accumulated deficit grew every year, by $67.7M from end 2016 to
mid-2026; the share count rose about 5.2 times from end 2016 to today on a pre-split basis. What they do not say: no
inventory build, no capitalised development, no goodwill; patents are the only intangible and fell from $1.86M (2017) to
$0.74M. The receivable of $1,360k at end 2025 (Birwelco billing) was collected in 2026 ($234k at 2026-06-30). Revenue is
recognised on completion of non-refundable performance obligations, with progress payments held as contract liabilities
($415k at 2026-06-30). Government assistance (DOE grants, about $1.9M in total, project end Q1 2026) is booked in other
income ($736k FY2025) and sits inside operating cash. No adjusted earnings figure was seen in the filings read; the
quarterly press releases (8-K Item 2.02 exhibits) were not read. Disclosure controls were concluded effective at
2025-12-31 (Item 9A). The FY2023 10-K was amended twice; the second amendment (10-K/A 2024-11-07, 0001558370-24-014881)
answered an SEC comment letter of 2024-10-29: the officers' certifications "contained typographical errors" (a wrong date,
and the wrong fiscal year named).

**Bearing on Q5 (the people): integrity facts, recorded, not judged.**
- "a regulatory inquiry by the SEC into the trading of our securities in 2020", on which the company spent about $131k of
  legal fees in FY2025 (MD&A, 0001104659-26-037699). The filings read do not say what the inquiry concerns beyond those
  words, or whether it is closed.
- A board contest in 2025: a special committee formed on 2025-02-10 did work to "respond, manage and otherwise address
  attempts by several stockholders to submit director nomination notices" (10-Q MD&A); cooperation agreements of 2025-05-27
  with Richard D. Clarkson and Anthony DiGiandomenico withdrew their nominations, enlarged the board from five to seven, and
  seated Louis J. Basenese and Anthony DiGiandomenico, with standstill and voting undertakings (8-K 2025-05-27,
  0001104659-25-052998); the company agreed to reimburse up to $20,000 and $2,000 of their expenses (DEF 14A 2026).
  Special-committee legal fees: about $435k in FY2025; $750k lower year over year in the first half of 2026.
- Three former directors (Judith Schrecker, David Maley, Catharine M. de Lacy) petitioned the Delaware Court of Chancery on
  2026-01-16 (Case No. 2026-0082-CDW) for advancement of legal fees arising from the company's request "for the Former
  Directors to return material generated by the Special Committee"; the request totalled $319k after year-end (Item 3;
  10-Q Note 10).
- Pay (DEF 14A 2026, 0001104659-26-049883): CEO Colin J. Deller, FY2025 total $547,341 (salary $350,000, bonus $157,280 paid
  in shares); CFO Brent Hinds $311,787. Directors and officers owned 5.22% at 2026-04-13; Otter Capital LLC 19.99%, and it
  bought the 500,000 shares of 2026-07-21 at $3.54. The insider policy forbids short sales, margin accounts and pledging.
- Repeated Nasdaq minimum-bid notices (8-K Item 3.01 on 2020-01-17, 2020-06-22, 2022-11-04, 2023-05-02, 2023-11-27,
  2024-05-03, 2024-10-30, 2025-04-04, 2025-08-08, 2025-09-30) before the 1-for-10 reverse split of 2026-03-16; compliance
  regained 2026-03-30.

**Bearing on Q6 (the money and the owners).** Every year's deficit was met by issuing shares; the public offering of
2026-05-28 was sold "primarily to existing stockholders" at $4.33 with a 90-day lock-up on the company, waived on 2026-07-21
for a private sale at $3.54 to Otter Capital, an existing holder of more than 5%; the at-the-market programme (up to
$6.875M) was recommenced 2026-07-06. The amended 2021 equity plan approved on 2026-06-08 added 1,077 thousand shares for
awards (10-Q), about 17% of the shares then outstanding. No buyback, no dividend.

**Bearing on Q9 (debt).** No borrowings; operating lease liabilities $117k; contract and warranty liabilities as above.

## COMPUTATION NOT A CLEARANCE
*(The owner's two reporting figures, by Part VII's reporting convention and Q7's range convention; computed after the Q1
STOP, so neither is a clearance, a verdict or entry language (operator rule 3). Arithmetic in
`Test Runs/_research 2026-10-12 CLIR/compute.py`.)*

- **Cash input.** Owner cash after every real cost (Step 0 table): five-year mean **-$6,143k before interest** (all-equity
  basis) and **-$5,870k after interest received** (equity-only basis); the literal window FY2021 to FY2025 is the base.
  The specifics, in order: (a) **cycles**: no year is aberrational on the filer's own description; no cycle base is set,
  and the literal window stands alone. (b) **decline and sign**: the series is negative in every year (-7,851, -5,745,
  -4,615, -5,990, -6,513 before interest); a compound rate between negative end years, and between the halves of the
  window, is meaningless, so **the range is the no-growth case alone, said so**. (c) **acquisitions**: none; no merger in
  the window; no deal signed or closed after it. (d) **working capital**: inside operating cash as filed. (e) **growth
  spending**: the filing does not separate maintenance from growth; the alternate that treats all R&D as growth spending
  (R&D added back) gives a mean of -$4,779k before interest, still negative, shown beside. (f) **the cap**: not engaged.
  **Tax**: the company pays no income tax on its losses; the carryforward shelter is worth nothing to owner cash while the
  losses continue (Q7, Whose tax), and is not priced.
- **Value range (no-growth case alone, ten years then no growth, at the 5.60% sovereign):**
  all-equity: -$6,143k / 5.60% = -$109.7M, plus net cash $11.64M = **-$98.1M, -$14.40 a share**;
  equity-only (owner cash after interest, against the market value of the shares): -$5,870k / 5.60% = **-$104.8M, -$15.40 a
  share**. Maintenance-only alternate, all-equity: **-$10.83 a share**. Against the price of **$3.21**.
- **Fair price (Part VII: each end case valued at ten percent, the two averaged; here one case):**
  all-equity **-$7.31 a share** (central figure); equity-only **-$8.62 a share** beside it; maintenance-only alternate
  -$5.31. **No positive fair price exists.** For the price to earn the floor on the all-equity basis at no growth, the
  business would need owner cash of about +$1.0M a year against a best year of -$4.6M.
- **How Q7 would close if it had been reached:** the floor is tested first; no case in the range earns the floor at any
  positive price, so the file would close OUT whatever the width **[M2003-149]**. The rows' reading of such a stream: "if
  somebody is reinvesting all their cash flow the next five years, they’d better have some very big figures coming in down
  the road" **[M1998-082]**; the price the market pays is for a future the filings do not show, which the letter row calls
  speculative **[L2000-026]**. Net cash per share is $1.71.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was made first; its commit, 72162008, followed the `tools/run.py`
      and EDGAR-index fetches by a few minutes, said so); written question by question; committed after Q1 closed and again
      at the close (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is held by the dispatching session per the
      brief (not checked by the analyst); the fold into the register is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched; one listing of `Test Runs/` filtered to
      this name was made to confirm the dated file name was free, and is declared above; what was seen by accident is
      declared under contamination and not used.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-12 CLIR/check_ids.py` against `principle_ledger_v5.csv`);
      every filing fact has its accession; the numbers are from filings or the computation file.
- [x] The order was kept; Q1's STOP closed the run; nothing after it is a clearance; the computation is headed so.
- [x] Owner cash after every real cost, including stock pay in all three forms (SBC, stock for services, bonuses settled in
      stock), never a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations line); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its FY2023 gap was filled from the filed statement.
- [x] `python tools/check_framework.py` PASS before the commit.
- Not done, said so: the rivals' filings (Q2 not reached); the quarterly press releases and the earnings-call transcript
  (8-K 2026-08-20, exhibit 99.2); the FY2016 to FY2020 cash-flow figures were taken from XBRL, not read in the filed
  documents; the subject and status of the SEC inquiry.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. **First, "start-up" is not defined.** Q1's list of what it rules OUT opens with start-ups **[L2007-015]**,
**[M2008-088]** but says nothing of age or stage; ClearSign was incorporated in 2008, and a reader who takes "start-up" by
age would skip the item and close the file TOO HARD (NATURE) on the adoption question instead. This run read the term by its
economics (never met its costs from its own sales, funded by issuing shares, early stage in its own words) and confessed
that as a CONVENTION of the run; the file closes either way, but the label (OUT or TOO HARD (NATURE)) depends on the
reading, and two analysts could record the same name differently. A one-line definition in Q1 would settle it. **Second,
Q7's range convention has no stated treatment of a stream negative in every year.** Specific (b) covers a series that
changes sign and falls back to "the no-growth case alone", which this run used; but discounting a perpetual loss gives a
large negative "value" (-$14.40 a share) that no owner would realise, because a business that keeps losing money either
changes or stops, and its floor is nearer its net cash ($1.71 a share) less the cost of stopping. The figure misleads if read
as a liquidation value. A sentence saying that a range negative on every case is reported as "no positive value on the
convention" would be cleaner. **Third, the reporting figures assume a positive range**: the fair price "at which the
midpoint of the range earns the floor" does not exist when the midpoint is negative; this run reported the arithmetic
(-$7.31) and said no positive fair price exists, rather than invent another definition.
