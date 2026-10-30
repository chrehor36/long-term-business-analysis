# Company Run — Aqua Metals, Inc. (Nasdaq: AQMS) — 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (2026-10-29), after the run was committed: not held (`PORTFOLIO.md` does not name AQMS or Aqua Metals).

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the departures the brief states
(the repository path; lines of evidence and competitors derived by the analyst from the filing; the commit trailer).

**Contamination, declared and not used.** (1) The session context opened with the repository's recent commit subjects,
which name two other companies' v5 re-runs of the overnight cycle of 2026-10-29 (one subject gives that company's box and
deciding question in a phrase) and an overnight log line for a third. (2) The project map and the memory index, loaded
automatically, carry queue state (counts of gate-clearers, a paused wave and its next name) and name no box for this
company. (3) The `.gitignore` comments name four other companies whose research folders once misbehaved. (4) The
governing framework itself names companies from its tests. None of this concerns Aqua Metals and none of it was used;
no other run file, holding review, `PORTFOLIO.md`, queue file or reading list was opened, listed or searched.

**Lines of evidence chosen from the 10-K (as the brief asks):** from Item 1, whether the business has commercial
operations and what it sells; from Item 1A and the MD&A, the funding position, the going-concern doubt and the dilution;
from Item 1 and the 2026 8-Ks and 10-Qs, the changes of strategy (lead to lithium, the product slate, the real estate
sale, the Lion Energy term sheet and its end); from Item 1's Competition paragraph, who the rivals are.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.45 (quote 2026-10-29 as printed by `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: common stock 3,563,531, one class (10-Q for the quarter to
  2026-06-30, filed 2026-07-30, accession `0001437749-26-025091`, cover as of 2026-07-24; `python Screens/cover_shares.py
  AQMS` agrees). Check against the balance sheet of the same 10-Q: 3,548,104 issued and 3,543,978 outstanding at
  2026-06-30 (4,126 treasury shares); the cover is later by the ATM, ESPP and award issuance of July. Filings after the
  10-Q read for share changes: the 8-K of 2026-08-21 (`0001437749-26-028733`, the annual meeting, which added 750,000
  shares to the 2019 Stock Incentive Plan, about a fifth of the count, voted 345,976 for, 266,657 against), the S-8 of
  2026-08-21 (`0001437749-26-028747`) registering them, the 8-K of 2026-09-08 (`0001437749-26-029824`, the ATM agent's
  assignment of its agreement to an affiliate). No prospectus or 8-K after the 10-Q states a new count; Forms 4 of
  2026-08-26 and 2026-10-15 were not opened. The count is taken at 3,563,531.
- **Market cap:** $5.17M (1.45 x 3.5635M).
- **Sovereign for the earnings currency:** 5.37%, US Treasury daily par yield curve, 30-year, 2026-10-28, as fetched by
  `tools/run.py` from the issuing authority.
- **Filings read** (operator rule 4): the 10-K for FY2025, filed 2026-03-31, accession `0001437749-26-010705` (Items 1,
  1A in part, 7 in part, 8: balance sheet, statement of operations, cash flows, Note 1 going concern); the 10-K/A of
  2026-04-30, accession `0001437749-26-014205` (Part III only, by its own statement of purpose); the 10-Q for the quarter
  to 2026-06-30, accession `0001437749-26-025091` (balance sheet, statement of operations, Notes 1 and 3); the proxy, DEF
  14A filed 2026-07-08, accession `0001437749-26-023053` (summary compensation table, employment agreements, beneficial
  ownership); the 8-K of 2026-02-11, accession `0001437749-26-003828` (Lion Energy term sheet and participation agreement);
  the 8-Ks of 2026-08-21 and 2026-09-08 above. The SEC company-facts XBRL series were used for the ten-year table and
  read against the filed statements where stated. **One figure cross-checked against the filed statement:** net cash
  used in operating activities FY2025, $(10,253) thousand in the filed consolidated statement of cash flows of the 10-K
  (`0001437749-26-010705`), against $(10.3)M in `tools/run.py`'s tagged series: agrees.
- `python tools/run.py AQMS` arithmetic lines only: owner cash after every real cost (operating cash less stock pay
  less capital spending), USD millions: 2021 -11.61, 2022 -17.17, 2023 -11.32, 2024 -24.29, 2025 -12.94; five-year
  average -15.47 (the tool's -15.5); on the depreciation basis -12.2. Capital spending 2021 to 2025: 2.35, 4.77, 5.60,
  7.92, 0.42; depreciation and amortization about 1 a year. Stock pay 2.20, 2.25, 2.53, 2.74, 2.27, plus $261 thousand of
  stock issued for consulting services in 2025 (the cash-flow statement's own line), which the tool did not add; with it
  2025 is -13.20 and the average -15.52. Every year of the ten in the XBRL series has negative operating cash (2016 to
  2025). The tool's yield and growth lines refuse on a non-positive base; its v4 material is not read (Part VII).

## THE FOUNDATIONS (not a gate)
The foundation that bears on this name is the first, a share is a business: the test is whether one would be content to
own it if the market closed for years **[M1997-109]**, and for a company that states it "has not generated revenues from
commercial operations and expects to continue incurring losses for the foreseeable future" (10-Q, Note 1,
`0001437749-26-025091`) and whose auditor states substantial doubt about its ability to continue as a going concern
(10-K, `0001437749-26-010705`), the owner of a closed market would own a claim on cash that has so far run only out. The
analyst's habits apply: "write it down in the first 30 minutes" **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) the 10-K calls lithium-ion recycling "a nascent industry" with "no predominant technology to displace", so the
company's own description of its field is of one whose economics are not yet formed; (2) the Lion Energy term sheet of
2026-02-06 would have turned a recycling developer into an energy-storage seller and was ended on 2026-05-11, with $4.1M
lent to Lion Energy, then in default, carried at $1.64M after a 60% allowance (10-Q Note 3); (3) shares issued: weighted
average 641,960 in 2024 and 1,494,502 in 2025 after reverse splits of one-for-20 (2024-11-05) and one-for-10
(2025-08-04), and 3,563,531 on the 2026-07-24 cover; (4) evidence for the business: 4 US patents and 24 pending, a
pilot plant run in a multi-week continuous campaign in late 2024 (10-K Item 1). Nothing found contradicts the
company's own statement that it is pre-commercial.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not by the business: a part-interest bought for cash without borrowing
can lose all that is paid and no more; the rule binds the buyer's financing and sizing, "Never risk permanent loss of
capital." **[L2023-005]**, and borrowed money "has no place in the investor's tool kit" **[L2014-005]**. Nothing here
reaches a sizing question, since the file closes at Q1.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**; "being able to asses where the business will
  be in 10 years" **[M2000-037]**; and the first step is "trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**.
- **What the filings say the business is.** "The Company has not yet commenced large-scale commercial lithium-ion battery
  recycling operations." (10-K Item 1, `0001437749-26-010705`). "The Company has not generated revenues from commercial
  operations and expects to continue incurring losses for the foreseeable future." (10-Q Note 1,
  `0001437749-26-025091`). Revenue by year from the tagged 10-K series, USD millions: 2017 2.09, 2018 4.45, 2019 4.87
  (the lead demonstration plant), 2020 0.11, 2021 0.17, 2022 0.00, 2023 0.03, 2024 0.00; the FY2025 statement of
  operations shows operating expenses and no revenue line (10-K). Eleven full-time employees (10-K Item 1). Net losses
  every year from 2015 to 2025, the accumulated deficit $270.4M at 2025-12-31 and $278.9M at 2026-06-30, against paid-in
  capital of $288.4M. The auditor's report states substantial doubt about the company's ability to continue as a going
  concern (10-K); management repeats it at 2026-06-30 with $4.7M of cash and $6.5M of operating cash used in the half
  year (10-Q Note 1).
- **The key variables, and whether they are foreseeable.** (1) Whether AquaRefining works at commercial scale and at what
  unit cost: demonstrated at bench and pilot scale only; the commercial facility at TRIC was abandoned in 2025 with a
  $9.1M impairment of construction in progress and the real estate for a recycling campus sold (10-K cash flows and Item
  1); no site is chosen. (2) What the product slate will be: lithium hydroxide, cobalt, nickel, copper and manganese
  dioxide in 2022 to 2024; "a simplified product slate, including lithium carbonate and mixed hydroxide precipitate" in
  2025; polymetallic nodules and rare earths under evaluation (10-K Item 1). (3) The field: the company's own words are
  that lithium-ion recycling "is a nascent industry. With no predominant technology to displace" (10-K Item 1,
  Competition). (4) Funding: the business plan depends on capital not yet raised (10-K Item 1A). (5) The line of
  business itself: in February 2026 the company signed a term sheet to buy an energy-storage seller, Lion Energy, LLC,
  which the 10-K says "aims to expand the Company’s participation in energy storage systems, energy management software,
  and battery cell production"; it was terminated on 2026-05-11 (10-Q Note 3). None of the five is foreseeable ten years
  out from these filings: the company has changed what it means to sell three times in five years.
- **Routing.** The rows put the start-up outside the circle by name: "Start-ups are not our game." **[L2007-015]**;
  "We don’t do startups." **[M2008-088]**. Aqua Metals was incorporated in 2014, but by its own filings it has never had
  commercial operations in the business it now pursues and has earned no material revenue since 2019; it is a start-up
  in substance, a development company funded by issuing shares. There is no earning power to put a fix on **[M2012-065]**,
  and nothing in the past statements tells what the future statements will be **[M2008-033]**. The alternative routing
  was weighed: a business in a fast-changing technology whose winners cannot be named goes to TOO HARD, not OUT
  **[M1998-008]**, **[M2012-067]**, **[L1993-023]**, and the company's own description of its field ("nascent", "no
  predominant technology") fits that too. The start-up item is the narrower and the more specific fact: the file is not
  closed because the industry's future is hidden, which a research pass could not cure either, but because there is no
  business yet to understand, which the rows rule out as a class. Box OUT. The reading is stated under WHAT IN THE
  FRAMEWORK WAS WRONG OR UNCLEAR.
- **VERDICT: OUT** at Q1, a start-up in substance: no commercial operations, no revenue since 2021 worth the name, a
  going-concern doubt, and a business model changed three times in five years **[L2007-015]**, **[M2008-088]**,
  **[M2012-065]**, **[M2006-013]**. The file closes here; later questions are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten balance sheets were read in Step 0's work and are written under AFTER THE STOP.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts found are recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The reporting figures the brief asks for are computed below.

**COMPUTATION, NOT A CLEARANCE** (operator rule 3; no entry language; `Test Runs/_research 2026-10-29 AQMS/computation.py`
and its output file).
- Cash input: owner cash after every real cost (operating cash less stock pay less all capital spending), five years
  2021 to 2025, USD millions: -11.61, -17.17, -11.32, -24.29, -12.94; average -15.47 (equity-only basis). All-equity
  basis (interest paid added back, XBRL InterestPaidNet 0.08, 0.08, 0.48, 0.33, 0.53): average -15.16. With the 2025
  consulting stock counted as pay: -15.52 equity-only.
- Specifics applied. (b) Decline: every year is negative, so a compound growth rate between end years is meaningless;
  the halves are -14.39 (2021 and 2022) and -18.61 (2024 and 2025), a deepening loss, and a growth rate on a negative
  base is also meaningless; the range is therefore the no-growth case alone, as (b) directs, said so. (a) Cycles: no
  year is a cyclical peak or trough; the business has no cycle, only a burn. (c) No acquisitions closed; the Lion Energy
  deal was terminated and is not valued beside. (d) Working capital is inside operating cash. (e) No maintenance guess
  is possible: there is no operating business to maintain; the all-spending case is the only case. (f) Not reached:
  no growth is carried.
- Net debt at 2026-06-30 (10-Q `0001437749-26-025091`): finance lease $0.122M less cash $4.744M, net cash $4.62M;
  operating leases ($0.319M) left out, said so; no borrowings. The Lion Energy receivable ($1.64M net) is not counted as
  cash. Subsequent events in the 10-Q were not read for net debt.
- **VALUE RANGE (COMPUTATION):** the no-growth case at the sovereign of 5.37%, all-equity: -$282.4M for the business,
  -$277.8M after net cash, **-$77.95 a share**; equity-only beside it, **-$80.82 a share**. The range is a single
  negative point. Against the price of $1.45.
- **The floor, tested first:** no case earns about ten percent at the price; at the price the owner cash, on the
  all-equity basis of $0.55M (market value $5.17M less net cash $4.62M), is a loss of many times the outlay every year
  **[M2003-149]**. Had the file reached Q7 it would close OUT on the floor, whatever the width.
- **FAIR PRICE (COMPUTATION, a reporting figure, never a verdict; Part VII):** each end case is the same no-growth case;
  at ten percent the business is -$151.6M, after net cash **-$41.26 a share** on the all-equity basis (central), and
  **-$43.40 a share** equity-only beside it; after the company's own tax (it pays none, having no profit; no conversion,
  and no carryforward shelter is priced since there is no profit to shelter). A negative fair price means there is no
  positive price at which the midpoint of the range earns the floor. Growth spending charged: none (no growth case);
  year one and year ten both nil.

## Q8 to Q10, Q12
NOT REACHED.

---
## THE BOX
**OUT** at **Q1** (a start-up in substance: no commercial operations, no revenue since 2021 worth the name, a
going-concern doubt). Q7's COMPUTATION, not a clearance: the range is a single negative point, -$77.95 a share
all-equity, against $1.45; fair price -$41.26 a share. **Integrity facts recorded, not judged** (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2 **[M1997-127]**.)*

**Q2, the castle.** The 10-K names no rival by name: its Competition paragraph speaks of "smelting" as "the only
commercially proven process for recycling lithium-ion batteries" and of "other technologies currently under
development" using "a predominately hydrometallurgical approach" (10-K Item 1, `0001437749-26-010705`); a search of the
10-K for rival names found none. So no competitor row was filled from rivals' filings, as the brief directs when the
10-K names none. The company's claimed advantages are its own words ("Only electro-hydrometallurgy recycler in North
America", "Strong IP protection: 4 US patents; 24 US and global patents pending"), and its patent paragraph says
"Competitors may work around our patents" (10-K Item 1). Its product sells into "globally traded commodities" priced off
the LME (10-K Item 1, Metals Markets), so it would be a price-taker. No field returns over a cycle can be read: the
company has never operated commercially.

**Q3, the capital.** Paid-in capital $288.4M against an accumulated deficit of $278.9M at 2026-06-30: nearly every dollar
put in has been spent (10-Q). Capital spending of $11.6M (2015), $29.2M (2016), $12.8M (2019), $7.9M (2024) went into
plants that produced no lasting earnings; 2025 recorded $9.1M of impairment and loss on disposal of property, plant and
equipment (10-K cash flows).

**Q4, the accounts: the ten balance sheets** (XBRL first-filed values, USD thousands, read against the 2025 10-K and the
2026 10-Q for the last two dates): total assets 71,529 (2016), 74,442 (2017), 71,371 (2018), 69,454 (2019), 35,138
(2020), 33,269 (2021), 33,502 (2022), 33,600 (2023), 26,365 (2024), 19,706 (2025), 12,622 (2026-06-30); equity 56,990,
58,965, 50,090, 49,589, 31,139, 27,533, 20,916, 26,064, 16,244, 14,770, 9,530; accumulated deficit -28,262 rising every
year to -270,416 (2025) and -278,850 (2026-06-30); cash 25,458 (2016) falling to 4,079 (2024), 10,810 (2025), 4,744
(2026-06-30); receivables nil or near nil throughout (no sales); inventory 244 and 242 of raw materials at the last two
dates; goodwill none; intangibles 1,137 (2016) amortized to 46; notes payable about 9M from 2016 to 2019, nil at 2021, a
5.9M current note at 2022, 3.5M at 2024, nil at 2025 (the 2025 cash flows show $4.5M of note payments and a $0.8M loss on
extinguishment). What the figures say: the equity has been kept above zero only by issuing shares, about $12M in 2025
and $7.3M in 2024 (10-K financing cash flows), while the assets bought with it were written down. What they cannot say:
what any asset would earn, since none has earned. The liabilities include a Level 3 warrant liability ($112K at
2026-06-30) whose fair-value changes ran through the income statement as gains of $1.27M in 2025 and $0.12M in the 2026
half, gains that arise as the share price falls (10-K, 10-Q). The 2025 investing section lists "Payments for note
receivable - LION ENERGY (2,069)" as cash; the 8-K of 2026-02-11 describes the same $2.1M as "$2.1 million in product
previously delivered to Lion Energy" (`0001437749-26-003828`), and the 10-Q Note 3 as "$2,069,000 of short-term
financing". The three descriptions were not reconciled in this run.

**Q5 and Q6, the people and the money (integrity facts recorded, not judged).**
- Share issuance: weighted average shares 641,960 (2024) and 1,494,502 (2025) after reverse splits of one-for-20
  (2024-11-05) and one-for-10 (2025-08-04), 3,563,531 at 2026-07-24; an ATM program of up to $50M with $48.05M
  unused at 2026-06-30, an equity line of $10M with Lincoln Park, a registered direct offering with warrants of
  2025-10-15 (8-K `0001437749-25-031102`), an ESPP that sold 131,569 shares in the 2026 half (10-Q Note 1), and 750,000
  shares added to the stock plan on 2026-08-18. The rows name serial issuance among the tells **[L2014-015]**; not weighed
  here.
- Pay (DEF 14A, `0001437749-26-023053`): the chief executive, Stephen Cotton, total $1,869,000 for 2025 (salary
  $511,000, bonus $610,000, stock awards $729,000) and $1,460,000 for 2024; two years' salary as severance, and two
  times salary and two times bonus after a change of control; 2025 bonus grants included 11,250 and 14,749 fully vested
  shares. The 2025 net loss was $22.6M and the auditor's going-concern doubt stood. Directors and officers as a group
  own 251,046 shares; the chief executive 151,231, 4.3%.
- Lion Energy: the company lent $2.069M in December 2025, due 2025-12-30 and unpaid, then bought a $4.1M subordinated,
  last-out participation in Lion Energy's senior loan on 2026-02-06 alongside a term sheet to acquire Lion Energy for up
  to $94.9M, mostly in shares and an earn-out (8-K `0001437749-26-003828`). Lion Energy was in default from 2026-03-31;
  the term sheet was terminated on 2026-05-11; on 2026-06-17 the senior lender assigned its position to "an entity that
  the Company believes may be affiliated with an owner of Lion Energy"; the company recorded a $2.5M allowance (60%) and
  "is evaluating, with the assistance of legal counsel" its rights (10-Q Note 3). The term sheet would have put Lion
  Energy's majority owner on the board.
- On 2024-12-18 the company sold $1.5M of secured promissory notes with warrants for 75,000 shares to eight accredited
  investors "including executives and related parties of the Company" ($850K of the notes related-party at 2024-12-31);
  both related-party debts were repaid by 2025-12-31 (10-K Note 10 and the related-party note, `0001437749-26-010705`).

**Q9, the debt and exposures.** No borrowings at 2026-06-30; the risk is the funding of the burn, $4.7M of cash
against $6.5M of operating cash used in the first half of 2026 (10-Q Note 1), so continued operation depends on issuing
shares.

**Q12.** Nothing found that bears on it.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The
      template copy was committed before the first fetch; Step 0 to the standing rule was committed before Q1; Q1 and
      everything after it, being closed by Q1, in the next commit.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (as the brief states; not verified by the analyst); the run is folded into the register by the dispatcher
      (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen
      by accident is declared under contamination above and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `Test Runs/_research 2026-10-29 AQMS/check_ids.py`);
      every filing fact has its accession; no number without a row or a filing.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance, and the Q7
      figures are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (US Treasury); the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**; the facts found for later questions are under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before the commit (run 2026-10-29 before the Q1 commit: PASS); the run's own
      check script (no E-ids, every id in the CSV, every quoted fragment in its row): 16 ids, 0 problems.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Q1 sends start-ups to OUT ("What it rules OUT", **[L2007-015]**, **[M2008-088]**) and fast-moving technology and
industries whose winners cannot be named to TOO HARD (**[M1998-008]**, **[M2012-067]**), and a pre-commercial company in a
field its own 10-K calls nascent fits both; the text gives no rule for which governs when both apply, nor any definition
of "start-up" for a company incorporated twelve years ago that has never had commercial operations in its current line.
This run read "start-up" in substance (no commercial operations by the company's own statement, no material revenue,
funded by share issuance) and let the narrower, factual item govern, because the start-up's defect is that there is no
business yet, which no research and no industry insider could cure, while the TOO HARD routing presumes a business whose
future is hidden. A second gap: Q7's fair-price definition presumes positive cash ends; with a negative single-point
range the "fair price" is a negative number that means only that no positive price earns the floor, and this run reports
it so rather than inventing a substitute. A third, in the brief rather than the framework: the brief describes the Lion
Energy deal as a potential acquisition in the 10-Q to 2026-06-30, but that 10-Q (Note 3) says the term sheet was
terminated on 2026-05-11; the filing was followed.
