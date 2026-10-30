# Company Run: AECOM (NYSE: ACM), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch
(commit `ea6d12cf`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (efb554c2): `PORTFOLIO.md` read for this ticker only; not held.*

**CONTAMINATION, declared.** (1) While checking whether the dated file name was free I ran a file-name listing of `Test Runs/`
filtered for "ACM|AECOM"; it returned `2026-09-12 Run - ACMR ACM Research.md` and `_research 2026-09-12 ACMR` (another company,
ACM Research). Neither was opened; nothing of them is used. (2) The session context showed the subjects of the five most recent
repository commits, which concern another company's run (VSEC), including its box; not used. (3) A memory index line in the
session context names a count of v4.1 gate-clearers and holding reviews owed, with no company named; not used. No blind-listed file
was opened, listed or searched beyond (1).

**Lines of evidence chosen, and why** (the brief's departure: derived from the 10-K's Item 1, Item 1A and Item 7). (a) What the
filer says sets its price and protects it: Item 1 "Competition" and the first risk factor, read against the two rivals' own
competition text. (b) The contract mix and the at-risk work: Item 1 "Contracts" (38% cost-reimbursable, 37% guaranteed maximum
price, 25% fixed price in fiscal 2025) and the Construction Management losses of fiscal 2026 (10-Q and 8-K of 2026-08-10),
because the discontinued businesses and the 2026 charge are both at-risk construction. (c) Cash against reported earnings:
claims recorded in contract assets, receivables sold, operating cash flow, because Item 7 says revenue recognition on claims
is a critical estimate. (d) The business that changed form: the self-perform construction and Management Services businesses
sold in fiscal 2020 and carried as discontinued; the window is set after the sale. (e) The AI risk factor of Item 1A, because the
filer bills "our employees’ time" and says AI "will accelerate design delivery".

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $58.94 (close 2026-10-16; Yahoo Finance chart API `regularMarketPrice`, market time 2026-10-16 20:00 UTC;
  **aggregator, live quote only, flagged** per operator rule 5). The same source shows a close of $131.00 on 2025-10-16 and a
  52-week range of $56.39 to $135.52; no split in the series.
- **Shares by class** from the latest filing's cover: Common Stock, $0.01 par, **128,696,425** (10-Q for the quarter ended
  2026-07-03, filed 2026-08-11, accession `0000868857-26-000021`; `python Screens/cover_shares.py ACM`). One class. Cross-check:
  the same 10-Q's balance sheet gives 128,695,633 shares "issued and outstanding" at 2026-06-30 (the company retires repurchased
  shares, so issued equals outstanding and there is no treasury line). No 8-K filed after the 10-Q bears on the count (8-Ks of
  2026-09-16, officer retirement, `0001104659-26-108255`; 2026-09-17, dividend, `0001104659-26-108415`).
- **Market cap:** $7,585M (128.696M x $58.94).
- **Sovereign for the earnings currency (USD):** 5.43%, US Treasury daily par yield curve, 30-year, 10/15/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for fiscal 2025 (period 2025-09-30, filed 2025-11-19, `0000868857-25-000013`): Items 1,
  1A, 7, the balance sheet, cash-flow statement, Notes 4 and 19; 10-K fiscal 2024 (`0001410578-24-002030`), fiscal 2022
  (`0001104659-22-119637`) and fiscal 2020 (`0001104659-20-126988`) for the cash-flow lines and the history; 10-Qs for fiscal 2026
  Q1 (`0000868857-26-000011`), Q2 (`0000868857-26-000014`) and Q3 (`0000868857-26-000021`); proxy filed 2026-01-20
  (`0000868857-26-000006`), pay and board passages only; 8-K exhibits 99.1 of 2025-11-18 (`0001104659-25-113439`), 2026-02-09
  (`0001104659-26-012069`), 2026-05-11 (`0001104659-26-058656`), 2026-08-10 (`0001104659-26-093421`), 2026-03-05, 2026-06-03 and
  2026-09-17 (dividends), and the 8-K of 2026-06-11 (`0001104659-26-072942`, the revolving credit agreement).
  **One figure cross-checked against the filed statement:** net cash provided by operating activities, fiscal 2025, $821,602
  thousand in the filed cash-flow statement, against 821.6 printed by `tools/run.py`; they agree.
- `python tools/run.py ACM`, arithmetic lines only (output kept in `Test Runs/_research 2026-10-16 ACM/run_py_output.txt`; nothing it
  prints as a rule, an id or a verdict is used, Part VII). Its OCF tag is total operating cash, discontinued operations included.
  The five-year owner cash used below is built in `Test Runs/_research 2026-10-16 ACM/q7.py` from the filed cash-flow statements:

  | USD M | FY21 | FY22 | FY23 | FY24 | FY25 |
  |---|---|---|---|---|---|
  | Operating cash flow (filed, incl. discontinued) | 704.7 | 713.6 | 696.0 | 827.5 | 821.6 |
  | less stock pay (non-cash stock compensation) | 44.7 | 38.5 | 45.9 | 61.5 | 61.4 |
  | less capital expenditures | 136.3 | 137.0 | 105.6 | 119.6 | 136.7 |
  | less finance-lease principal | 13.7 | 19.8 | 23.7 | 28.9 | 32.4 |
  | less net distributions to noncontrolling interests | 10.3 | 12.4 | 2.2 | 16.2 | 53.4 |
  | **Owner cash, equity-only** | **499.7** | **505.9** | **518.6** | **601.3** | **537.7** |
  | plus interest paid less interest income, after 21% | 196.7 | 76.2 | 89.8 | 93.9 | 82.2 |
  | **Owner cash, all-equity** | **696.4** | **582.1** | **608.4** | **695.2** | **619.9** |
  | Acquisitions, net of cash acquired | 0 | 0 | 0 | 18.7 | 212.5 |

  Five-year averages: equity-only $532.6M; all-equity $640.4M; acquisitions $46.2M. Depreciation and amortization (176.4, 170.9,
  175.7, 178.8, 175.9) exceeds capital spending in every year; the depreciation variant is shown at Q7. The 21% is a CONVENTION of
  this run (rationale: the US statutory rate, used only to put interest on an after-tax footing; the effective rate is not far from
  it). SBC is resolved from the cash-flow statement's "Non-cash stock compensation" line, every year.
  **Trailing twelve months to 2026-07-03** (fiscal 2025 less its first nine months plus the first nine of fiscal 2026, from the Q3
  10-Q): operating cash $365.4M, stock pay $41.9M, capital spending $161.9M, noncontrolling distributions $50.7M, finance-lease principal taken at
  the fiscal 2025 figure ($32.4M, the 10-Q does not show it separately); equity-only owner
  cash about $78.5M. The 10-Q attributes the fall to "an increase in net cash outflow of $283.5 million [...] related to two
  Construction Management projects".

- **The balance sheets, ten year-ends, read before the income account** **[M2025-032]** (the file closes before Q4, so they are
  read here). Source: the ten-year table of `tools/run.py` (XBRL first-filed vintages, transcription; accessions listed in its
  output), read against the filed balance sheets of the 10-Ks for fiscal 2025, 2024, 2022 and 2020 and the Q3 fiscal 2026 10-Q.

  | USD M | 2016 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06-30 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | Total assets | 13,727 | 14,681 | 14,462 | 12,999 | 11,734 | 11,139 | 11,233 | 12,062 | 12,200 | 12,027 |
  | AECOM equity | 3,367 | 4,093 | 3,691 | 3,293 | 2,712 | 2,477 | 2,212 | 2,184 | 2,493 | 2,193 |
  | Goodwill | 5,824 | 5,921 | 5,275 | 3,484 | 3,502 | 3,381 | 3,419 | 3,480 | 3,701 | 3,767 |
  | Retained earnings (deficit) | 618 | 948 | 600 | 174 | (504) | (702) | (1,104) | (1,282) | (1,225) | (1,602) |
  | Cash (incl. in consolidated JVs) | 692 | 887 | 1,080 | 1,708 | 1,229 | 1,172 | 1,260 | 1,581 | 1,586 | 1,013 |
  | Debt on the face | 4,125 | 3,627 | 3,403 | 2,062 | 2,212 | 2,205 | 2,203 | 2,517 | 2,714 | 2,715 |
  | Accounts receivable | 4,531 | 5,469 | 2,869 | 2,866 | 2,619 | 2,318 | 2,544 | 2,793 | 2,497 | 2,390 |

  What moved and why. (1) The company shrank by sale: assets fell from $14.7B (2018) to about $11 to 12B after fiscal 2020, when
  the Management Services business was sold ("(Payments for) proceeds from sale of discontinued operations, net of cash disposed",
  $2,218.9M in fiscal 2020, 10-K FY2022 cash-flow statement) and the self-perform construction businesses were exited; goodwill fell
  with them from $5.9B to $3.5B. (2) **Equity was below goodwill at every year-end of the ten**, so tangible equity was negative
  throughout; the business runs on almost no tangible capital. (3) Retained earnings went from $948M (2018) to a deficit of $1,602M
  (2026-06-30). The company retires the shares it buys and charges the excess to the deficit ($424.7M of the $444.0M repurchased in
  the first nine months of fiscal 2026, Q3 10-Q equity statement); repurchases were $867.1M, $473.0M, $379.3M, $478.5M and $388.4M in
  fiscal 2021 to 2025, and diluted shares fell from 161.3M (fiscal 2020) to 133.3M (fiscal 2025). (4) Debt was cut from $4.1B to
  $2.1B with the sale proceeds and has risen again to $2.75B of principal (Note 7, Q3 10-Q: credit agreement $1,448.8M, 6.000% notes
  due 2033 $1,200.0M, other debt including finance leases $96.4M; $2,627.4M of it due after fiscal 2030) while the buybacks went
  on. (5) Cash fell from $1,586M to $1,013M in nine months of fiscal 2026, and $250.9M of what is left sits in consolidated joint
  ventures. (6) Receivables fell with the exits, but the working capital is moving toward claims: "Significant claims recorded in
  contract assets" were about $160M (2023), $180M (2024), $400M (2025) and $620M (2026-06-30) (Note 4 of each filing), and contract
  assets rose from $1,785M to $2,115M in nine months. (7) Off the balance sheet, receivables sold to banks were $291.0M (2023),
  $319.5M (2024), $268.2M (2025) and $348.9M (2026-06-30); their changes pass through operating cash. What the figures do not say:
  whether the $620M of claims will be collected; the filer says resolution "will likely take several years and litigation"
  (8-K 2026-08-10). What the management would like them to say is printed beside them in every release: results "excluding this
  project’s impacts".

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**. The quotation has halved in a year ($131.00 to $58.94) while the filer reports a record backlog; the market "just
tells us prices" **[M2006-077]**, so the fall is neither a reason to buy nor evidence against the business by itself, but it is the
extreme example on which to ask "what in hell is going on here" **[M1997-129]**. The filer's guidance and long-term targets
(fiscal 2029 EPS growth and margin targets in the 8-Ks) are projections and are not used **[M1995-050]**. The analyst's habit
applied: look for "what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the
filer itself says its services "provide limited barriers against new competitors" (10-K FY2025, Item 1 and Item 1A); (2) a $336.8M
loss in fiscal 2026 Q3 on a Construction Management project bid in 2019; (3) claims recorded as contract assets grew from about
$160M (2023) to $180M (2024), $400M (2025) and $620M (2026-06-30); (4) reported operating income rose from $629.6M (FY21) to
$1,026.5M (FY25) while all-equity owner cash went from $696.4M to $619.9M; (5) $441.9M paid to repurchase stock in the first nine
months of fiscal 2026 (Q3 10-Q cash-flow statement; the equity statement shows $444.0M of repurchases for the nine months and none in
the third quarter), at prices above $70 a share on the quotation series; (6) the filer's own AI
risk factor. Evidence for the business, written down too: number one in the ENR design survey (Item 1); a "22nd consecutive quarter
with a book-to-burn ratio in excess of 1" (8-K 2026-05-11); backlog $39.7B at 2025-09-30 against $37.4B a year earlier.

## THE STANDING RULE
Owning a part-interest bought with cash and no borrowed money puts the buyer at no risk of ruin from this name; the rule binds
the buyer's financing and sizing, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, **[M2012-081]**. Nothing
here is a reason to depart from it.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five
  or 10 years" **[M2012-065]**, **[M2000-037]**; the product may stay opaque if "I understand the economic dynamics of the
  industry" **[M2011-014]**.
- **What the business is, from the filing.** "Our business focuses primarily on providing fee-based knowledge-based services. We
  primarily derive income from our ability to generate revenue and collect cash from our clients through the billing of our
  employees’ time spent on client projects and our ability to manage our costs." (10-K FY2025, Item 1.) Clients are governments for
  half of revenue (U.S. federal 7%, state and local 24%, non-U.S. governments 19%) and private entities for half; no client is 10%.
  About 53% of revenue is pass-through subcontractor cost (Item 7: $8.6B of $16.1B). Segments: Americas (design and consulting,
  and the Construction Management operating segment), International, AECOM Capital (Note 19).
- **The key variables and whether they are foreseeable** **[M1998-044]**. (1) Demand for infrastructure design and program
  management: public budgets and private capital programs; the filer names the U.S. infrastructure act and ageing assets. Demand
  for this work in ten years is foreseeable in broad terms; its level moves with public spending, which the filer calls vulnerable
  to "sudden economic downturns and reductions in government and private industry spending" (Item 7). (2) What the firm keeps per
  hour billed: set by the contract form (cost-plus fees negotiated with the client, guaranteed maximum price, fixed price) and by
  the competition; readable from the filings. (3) The at-risk losses on guaranteed-maximum-price and fixed-price work (62% of
  fiscal 2025 revenue by contract type): readable in kind, unforeseeable in timing, and visible twice in the record (the
  discontinued self-perform construction businesses; the $336.8M Construction Management loss of fiscal 2026). (4) The hours a
  design needs: the filer says AI "will accelerate design delivery and reduce the materials and costs required for a project"
  (Item 1) and that "Our competitors or other third parties may incorporate AI [...] more quickly or more successfully than us"
  (Item 1A).
- **Do the past statements tell me the future ones** **[M2008-033]**? For the design business, yes in kind: a labour business whose
  revenue is hours and pass-through, whose costs are compensation and subcontractors, and whose capital is working capital. The
  accounts of the continuing business since the fiscal 2020 exits are readable; the window used below starts after them.
- **Routing.** A business whose ten-year economics cannot be foreseen because its industry changes fast closes here TOO HARD
  **[M1998-008]**. The filings do not show the industry's economics changing fast over the decade read: the same three contract
  forms, the same billing of hours, the same field of rivals named in both rivals' 10-Ks. AI is a threat to the business "as it
  presently exists" in the sense of **[M1998-008]**, but the filings show it as a prospect, not as a change that has yet moved the
  economics; I carry it to Q2's test 11 (what could destroy, modify or reduce it **[M2000-014]**) rather than close on it here, and
  record in the last section that the text could be read to close here instead. Not a bank; not a holding company. Of the parts,
  Americas carries about three quarters of segment earnings in each of the three years Note 19 gives (fiscal 2025: $868.9M of
  $1,181.3M) and decides; it is understood by the same reading.
- **Doubt test** **[M2002-092]**: I do not doubt that I can see what this business is, what it sells and what its earning power
  depends on; what I doubt is whether it is protected, which is Q2's question, not Q1's.
- **VERDICT: IN.** The economics of a fee-based engineering and program-management firm can be pictured from its figures
  **[M2012-065]**, **[M2011-014]**; the threat from AI is carried to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now" **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**Competitors.** The 10-K names none: "The markets we serve are highly fragmented and we compete with a large number of regional,
national and international companies" (Item 1, Competition). The rivals used are therefore a **CONVENTION of this run**: Jacobs
Solutions (10-K FY2025, filed 2025-11-20, `0001628280-25-053316`) and Tetra Tech (10-K FY2025, filed 2025-11-20,
`0000831641-25-000032`), each chosen because its own 10-K names AECOM as a competitor and it files 10-Ks with the SEC (rationale: a
rival that names the filer in its own filing is the least invented choice available). Others named in those
lists that file 10-Ks were not read (Parsons, Fluor, Leidos, SAIC, ICF, Booz Allen Hamilton, Exponent, Montrose); named and not
filing 10-Ks with the SEC: WSP, Stantec (files a 40-F), Arcadis, AtkinsRealis, Arup, Mott MacDonald, GHD, Black & Veatch, CDM Smith.

**The parts table** (Note 19, segment earnings before taxes and amortization, USD M; Note 19 gives three years):

| Part | FY23 | FY24 | FY25 | three-year total | castle | decides |
|---|---|---|---|---|---|---|
| Americas (design and consulting, and Construction Management) | 721.6 | 776.2 | 868.9 | 2,366.7 of 2,870.1 (82%) | below | **yes** |
| International | 236.6 | 310.7 | 321.4 | 868.7 (30%) | the same field, same tests | no |
| AECOM Capital | (315.8) | (40.5) | (9.0) | (365.3) | real estate co-investing, team moved to a third-party platform in fiscal 2024 | no |

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**. The filer names its own: "our reputation, our cost effectiveness, our long-term
   client relationships, our extensive network of offices, our employee expertise, and our broad range of services" (Item 1).
   "Our principal asset is our employees" (Item 1, Human Capital Management), and the risk factors include "Our ability to compete
   in our industry will be harmed if we do not retain the continued services of our senior management and key technical
   personnel." An asset that can leave is kept only by paying it the market's rate, so its returns go first to the staff.
2. *Without the lord* **[L2007-006]**: no single superstar; the dependence is on about 51,000 staff (fiscal 2025 year-end), the same
   dependence spread wide. Neutral.
3. *The money test* **[M2011-015]**, **[M1997-103]**: could a well-funded attacker take it? The filer answers in its own words: "The
   technical and professional aspects of our services generally do not require large upfront capital expenditures and,
   therefore, provide limited barriers against new competitors." (10-K FY2025, Item 1; repeated in Item 1A.) Tetra Tech's 10-K
   uses the same words ("provide limited barriers against new competitors", Item 1A), and Jacobs's 10-K says "Typically, no single
   company or companies dominate the markets in which we provide services" and names twenty-three competitors, among them
   Accenture, Deloitte, KPMG, PwC, Bain & Company and McKinsey & Company (Item 1). This is the industry with no barriers to entry, in
   which "you better be running very fast" **[M2012-106]**, and "one competitor is frequently enough to ruin a business"
   **[M2012-108]**. **Fails.**
4. *Pricing power* **[M2005-020]**, **[M2000-031]**: none shown. 38% of fiscal 2025 revenue is cost-reimbursable work billed at costs
   "plus a negotiated fee or rate" (Item 1, Contracts), and on federal work the FAR "can limit the recovery of certain specified
   indirect costs" (Note 1); the filer lists price among the clients' "competitive determinations" and warns of "increased margin
   pressure" (Item 1A). The Americas gross-margin rise of fiscal 2025 is explained by the filer as "the benefit from restructuring
   actions taken last year, growth in enterprise capability centers, ongoing continuous improvement initiatives, and growth in
   higher margin advisory services" (Item 7): cost and mix, not price.
5. *Unit volume and share of mind* **[M1999-054]**: volume is the business's best evidence. Backlog $39.7B at 2025-09-30 against
   $37.4B; a "22nd consecutive quarter with a book-to-burn ratio in excess of 1" (8-K 2026-05-11); "two of the largest recompetes in
   our Company’s history" won (8-K 2026-08-10). Clients keep hiring the firm; that does not show it can charge more for the hours,
   and the margin record shows it keeps little of them.
6. *The low-cost position* **[M2018-043]**: not shown. On the same metric over the decade AECOM's operating margin (0.1% to 6.4%,
   average 3.4%) sits below Jacobs's (3.1% to 7.2%, average 4.9%) and Tetra Tech's (5.3% to 9.7%, average 7.6%). Pass-through
   revenue (53% of AECOM's in fiscal 2025) blurs the comparison, but nothing in the filings shows AECOM the low-cost producer.
7. *The brand in the customer's mind* **[M2015-038]**: the ENR ranking and "reputation" are named by the filer, and clients choose on
   "qualifications, experience, performance, reputation, technology, customer relationships, price" (Item 1A). This is the
   business's strongest point; the same reputation is claimed by each rival in its own filing.
8. *Over the low bid* **[M2017-009]**, **[M1997-102]**: partly. Qualifications come first in the clients' list and price after, but
   the filer still writes of its "inability to win bids" (Item 1A), and no filing shows a premium charged and kept.
9. *Ask the competitors* **[M1999-130]**: both rivals' 10-Ks list AECOM among their principal competitors (first in each list,
   Tetra Tech's being alphabetical). That says where the threat is, not that the target fails **[M2017-022]**.
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**: margins widened from fiscal 2020 to 2025, by the filer's own account
    through restructuring, "enterprise capability centers, shared service centers, and delivery efficiencies" and the "exiting of
    lower margin countries" (10-K FY2024, Item 7). Jacobs's margin widened over the same years (4.0% in 2020 to 7.2% in 2025). This
    is "the improvement you get one day, your competitor gets the next day" **[M2004-053]**, in a product of "very high labor
    content" that "can be shipped in from abroad very easily" **[M2007-116]**, which the filer is doing itself and any rival can do.
11. *What could destroy, modify or reduce it* **[M2000-014]**: (a) the at-risk work: the self-perform construction businesses, sold in
    fiscal 2020 with losses still carried in discontinued operations in fiscal 2026 (a $61.8M non-cash loss on the DOE claims,
    Q3 10-Q, Note 3), and in the continuing business the Construction Management project charged $336.8M in fiscal 2026 Q3, "bid in
    2019 under terms and conditions that would not clear our substantially transformed risk processes today" (8-K 2026-08-10),
    with a second Construction Management project also in claims (Q3 10-Q); (b) public budgets; (c) AI, by the filer's own words a
    tool that will "accelerate design delivery" for a firm paid by "the billing of our employees’ time", in a field where
    competitors "may incorporate AI [...] more quickly or more successfully than us" (Items 1 and 1A). Whether AI makes the hours
    fewer or the firm's knowledge dearer is a forecast I cannot make; it is not needed, because test 3 fails on the filed record.

**The competitor row** (operating income over revenue, and over equity plus debt less cash; XBRL first-filed vintages,
transcription, read against each FY2025 10-K; `Test Runs/_research 2026-10-16 ACM/compare_output.txt`; AECOM's 2016 to 2019 as
first filed include the businesses sold in fiscal 2020):

| FY | ACM margin | ACM OI/capital | J margin | J OI/capital | TTEK margin | TTEK OI/capital |
|---|---|---|---|---|---|---|
| 2016 | 2.2% | 5.5% | 3.1% | 8.5% | 5.3% | 19.2% |
| 2017 | 3.6% | 9.3% | 3.9% | 10.1% | 6.7% | 24.8% |
| 2018 | 2.1% | 6.2% | 4.3% | 9.0% | 6.4% | 23.2% |
| 2019 | 0.1% | 0.4% | 3.2% | 6.4% | 6.1% | 16.7% |
| 2020 | 2.9% | 10.5% | 4.0% | 8.1% | 8.1% | 20.6% |
| 2021 | 4.7% | 17.0% | 4.9% | 8.8% | 8.7% | 21.8% |
| 2022 | 4.9% | 18.4% | 6.2% | 11.0% | 9.7% | 27.1% |
| 2023 | 2.3% | 10.3% | 6.6% | 12.7% | 7.9% | 16.9% |
| 2024 | 5.1% | 26.5% | 6.0% | 12.3% | 9.6% | 20.8% |
| 2025 | 6.4% | 28.4% | 7.2% | 18.6% | 7.5% | 17.2% |
| average | 3.4% | 13.3% | 4.9% | 10.5% | 7.6% | 20.8% |

**The field's returns over the last full cycle, judged in words.** Against the capital paid for these businesses (equity plus net
debt, much of it purchased goodwill: AECOM's goodwill exceeded its equity at every year-end from 2016 to 2025), the field earned
ordinary-to-modest pre-tax returns across the decade: AECOM and Jacobs about 10% to 13% pre-tax on average, AECOM below 11% in six
of the ten years; Tetra Tech did better. Against tangible capital the returns are very high or undefined, because tangible capital
is near nil or negative for all three. The capital "actually needed in the business" is small **[M2010-090]**, and goodwill is set
aside in judging the business **[M2011-060]**, so the high tangible return is real; but a business that needs no capital and has
"limited barriers" offers that return to whoever enters, which is what test 3 found. A thin margin "only works in terms of return on
capital if you turn your equity extraordinarily fast" **[M2017-096]**; here it works because almost no equity is needed, for every
rival alike. No change for the better is credited: the margin rise since fiscal 2020 has not been through a downturn, and the field
rose with it.

**Contrary evidence, written down** **[M1997-127]**: the reputation and scale are real; clients do not buy design purely on the low
bid; recompetes are being won and backlog is a record; and pre-tax operating income on capital employed was 26.5% and 28.4% in
fiscal 2024 and 2025. If those two years are a new level that holds through a downturn, the reading of "ordinary" would change.
None of it answers test 3: an attacker needs people, not capital, and the filer, a rival, and that rival's list of twenty-three
competitors say the field is open.

- **Routing.** A castle shown open on the evidence closes OUT **[M2011-015]**: "If the answer had been yes, we wouldn’t have done
  it." The evidence is affirmative and in the filer's own 10-K, not a forecast, so this is not the tenuous moat that goes to TOO
  HARD **[M2000-019]**; "anything you do, your competitors can copy" **[M1996-017]**.
- **VERDICT: OUT.** The deciding part, Americas, sells knowledge work whose "technical and professional aspects [...] provide limited
  barriers against new competitors" (the filer's words), at fees negotiated with clients who list price among their tests, in a
  field no firm dominates; the money test fails **[M2011-015]**, **[M2012-106]**, and the margin gains are cost gains the rivals made
  too **[M2004-053]**. The file closes here; Q3 to Q12 are NOT REACHED.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0; the facts that bear on the accounts are under AFTER THE STOP, not weighed.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. Facts that bear on it are under AFTER THE STOP, and the box line carries the flag.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback line Q6 would need from Q7's range is recorded under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The figures below are the operator's reporting figures, computed beneath the stop.

### COMPUTATION, NOT A CLEARANCE
Built by Q7's range convention (five-year owner cash, growth shown and capped, ten years then zero nominal growth, discounted at the
5.43% sovereign; the four specifics of the PG re-test and specifics (a) to (f)); arithmetic in
`Test Runs/_research 2026-10-16 ACM/q7.py`, output in `q7_output.txt`. All figures USD.

- **The window and the business that changed form.** Fiscal 2021 to 2025, the five fiscal years after the fiscal 2020 sale of
  Management Services and the exit from self-perform construction. Fiscal 2020, the year of the sale, is left out. Operating cash is
  taken as filed, discontinued operations included, because the tail costs of the sold businesses (claims, guarantees, the DOE and
  refinery matters) were paid by the owners in these years. Fiscal 2026 has not closed (its 10-K is not filed); the trailing twelve
  months to 2026-07-03 are shown beside, not inside, the window.
- **(a) Cycle.** Neither end year is described by the filer as aberrational, and the series is not cyclical in the filings read; the
  literal window is the window. The trailing year that followed it is aberrational by the filer's own description (the Construction
  Management charge) and is shown beside: equity-only owner cash about $78.5M, all-equity about $160.6M.
- **Owner cash** (Step 0 table): all-equity average $640.4M; equity-only $532.6M.
- **(c) Acquisitions.** $18.7M (fiscal 2024) and $212.5M (fiscal 2025), average $46.2M, deducted, total growth credited (the default
  pair). Net purchases over the window ($231.2M) are far below half of owner cash before purchases ($3,202M), so this is not the
  serial acquirer. Payments made on businesses sold earlier ($265.9M in fiscal 2021, $42.3M in fiscal 2022, cash-flow statement
  "(Payments for) proceeds from sale of discontinued operations") are read as exit costs of the discontinued businesses, not as
  purchases, and are shown beside. No signed unclosed deal and no deal closed after the window was found in the 8-Ks read.
- **(d) Working capital** is inside operating cash and is counted.
- **(e) Maintenance.** The filing does not split capital spending into maintenance and growth. My guess, stated as the rows ask
  **[M2000-144]**: all of it is maintenance (offices, equipment, software for a labour business), so the maintenance case and the
  all-spending case are the same; capital spending ran below depreciation and amortization every year, and the depreciation
  variant is shown beside.
- **Growth shown**, on aggregate all-equity owner cash: $696.4M (FY21) to $619.9M (FY25), **minus 2.87% a year**. By (b) a decline is
  carried as the bottom and the no-growth case is the top. Beside it, the halves (FY21 and FY22 against FY24 and FY25): plus 0.94% a
  year; the end-year rate is driven by fiscal 2021's high interest paid ($255.7M against $104.6M the next year), which the filer does
  not describe as aberrational, so the literal rate decides. Equity-only series: plus 1.85% a year. (f) The cap is not reached.
- **Net debt** at 2026-06-30 (the latest filed balance sheet): total debt principal $2,745.2M (Note 7) less cash $1,012.9M = **$1,732.3M**;
  operating leases left out (operating lease liabilities $487.8M non-current); the receivables sold ($348.9M) left out and said so.
  No subsequent event stated in the 10-Q changes it materially (the July 2026 DOE settlement brings a $58.5M payment to the company,
  already reflected in the revised recovery estimate).

| Case (all-equity, central) | base | growth | value a share at 5.43% | at 10% |
|---|---|---|---|---|
| Top: no growth | $594.1M | 0% | **$71.56** | $32.71 |
| Bottom: shown decline | $594.1M | minus 2.87% | **$54.22** | $24.65 |

| Beside (never decides) | value a share | at 10% |
|---|---|---|
| Halves growth, plus 0.94% | $78.21 | $35.76 |
| Exit payments also deducted, no growth / decline | $62.74 / $47.20 | $27.92 / $20.69 |
| Organic pair (acquisitions left out), no growth / decline | $78.18 / $59.49 | $36.30 / $27.61 |
| Depreciation variant, no growth / decline | $64.62 / $47.98 | $28.94 / $21.20 |
| Equity-only, no growth / plus 1.85% | $69.60 / $80.68 | $37.79 / $42.86 |

- **VALUE RANGE (reporting figure): $54.22 to $71.56 a share** (all-equity basis, the central figure), against **$58.94**. Literal
  window shown: it is the window used. Equity-only beside: $69.60 to $80.68.
- **The floor, tested first.** At the price the business costs $9,317.6M (market value $7,585.3M plus net debt $1,732.3M). Owner cash
  of $594.1M is a 6.38% return on that with no growth; the halves case adds less than one point. To earn the floor of about ten
  percent at no growth the business would need about $932M of all-equity owner cash a year, half again what it has produced in
  any year of the window. **No case in the range earns the floor at the price**, so had Q7 been reached it would close OUT whatever
  the width ("there’s just a point at which we drop out of the game" **[M2003-149]**). The range is narrow (top to bottom 1.3 to
  1), and the price sits inside it, which would also be OUT: not a screamer **[M2009-005]**.
- **FAIR PRICE (reporting figure, never a verdict; Part VII): $28.68 a share** on the all-equity basis (each end valued at ten
  percent, $32.71 and $24.65, averaged), after the company's own tax (owner cash is after the company's tax as paid; no conversion).
  **Equity-only beside: $40.33** ($37.79 and $42.86 averaged). The all-equity figure is the central one; the equity-only figure is
  shown and does not decide. No cheap price is reported.

## Q8 to Q12
NOT REACHED.

---
## THE BOX
**OUT** at Q2 (Q1 IN): the castle shown open on the filer's own 10-K, whose services "provide limited barriers against new
competitors", sold at fees negotiated with clients who list price among their tests, in a field no firm dominates (Jacobs, Tetra Tech),
with the margin gains since fiscal 2020 cost gains the rivals made too; COMPUTATION, NOT A CLEARANCE beneath the stop: value
$54.22 to $71.56 a share (all-equity) against $58.94, no case earns the floor, fair $28.68 ($40.33 equity-only); integrity facts
recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Bearing on Q3 (capital).**
- Capital spending $105.6M to $137.0M a year in fiscal 2021 to 2025, below depreciation and amortization ($170.9M to $178.8M) every
  year (cash-flow statements). Tangible equity negative at every year-end 2016 to 2025 (Step 0).
- Operating income rose from $629.6M (FY21) to $1,026.5M (FY25); all-equity owner cash went from $696.4M to $619.9M over the same
  years (Step 0 table).

**Bearing on Q4 (the accounts).**
- Significant claims recorded in contract assets: about $160M, $180M, $400M and $620M at 2023, 2024 and 2025 year-ends and
  2026-06-30 (Note 4 of the 10-Ks for fiscal 2024 and 2025 and of the Q3 10-Q). The filer: "Except for significant claims,
  substantially all contract assets are expected to be billed and collected within twelve months."
- A $336.8M loss on one Construction Management project in fiscal 2026 Q3; "We may be required to make subsequent changes to
  estimates [...] which could result in additional estimated losses and could be material" (Q3 10-Q). Revenue recognized on claims
  is named by the filer as a critical estimate (10-K FY2025, Item 7).
- Restructuring and acquisition costs in every year of the window: $48M, $108M, $188M, $99M, $59M (fiscal 2021 to 2025, Item 7
  table), and $53.6M in the first nine months of fiscal 2026 (Q3 10-Q).
- Losses from discontinued operations in fiscal 2024 ($105.0M), fiscal 2025 ($75.4M) and fiscal 2026 (including the $61.8M DOE
  revision), five years after the sale (10-K FY2025 Item 7; Q3 10-Q).
- Receivables sold to financial institutions outstanding: $291.0M, $319.5M, $268.2M, $348.9M (2023 to 2026-06-30).
- Every quarterly release features adjusted figures beside GAAP: "Adjusted EPS", "Adjusted EBITDA", "segment adjusted operating
  margin", and in the 8-K of 2026-08-10 a table of "Metrics Excl. Const. Mgmt. Project Charge" (adjusted EPS of $1.49 against a GAAP
  loss of $0.65 a share).
- Guidance is given and raised: "Raised earnings guidance for a second consecutive quarter" (8-K 2026-05-11); fiscal 2026 guidance
  "excluding the Construction Management charge" kept at "Adjusted EPS of between $5.90 and $6.10" (8-K 2026-08-10); long-term
  targets of "a 20%+ margin exit rate by fiscal 2028" and "adjusted EPS at a 15%+ CAGR from fiscal 2026 to fiscal 2029, excluding
  the Construction Management charge" (8-K 2026-08-10).

**Bearing on Q5 (the people; the flag in the box line).**
- The three Q4 habits above (adjusted figures featured, guidance raised and kept, long-term targets restated excluding a loss) are
  the ones v5 carries to Q5 to be read with the integrity record; not judged here.
- Of the $336.8M loss the chief executive said: "This project was bid in 2019 under terms and conditions that would not clear our
  substantially transformed risk processes today" (8-K 2026-08-10); the Q2 release three months earlier spoke of "an enduring
  competitive advantage" and raised guidance (8-K 2026-05-11), while that quarter's operating cash was $4M, down 98% from a
  year earlier (same release), explained as "delayed payment timing in the Middle East business, as well as longer-than-anticipated claim resolution
  on certain projects".
- The chief executive is also chairman, with a lead independent director (proxy 2026, `0000868857-26-000006`). Long-term pay vests
  on ROIC, adjusted EPS growth and relative TSR (proxy). The Chief Legal Officer gave notice of retirement on 2026-09-14 and is
  succeeded by the general counsel, corporate (8-K 2026-09-16).

**Bearing on Q6 (the money).**
- Repurchases of $2,586M in fiscal 2021 to 2025 and $441.9M paid in the first nine months of fiscal 2026 (cash-flow statements),
  under a programme stated as a dollar authorization ("$1.0 billion", raised 2026-02-04) with no stated price (Q3 10-Q, Item 2). The
  quotation series puts the fiscal 2026 first-half purchases at prices above $80, against the computed range's bottom of $54.22
  and top of $71.56: the buyback line Q6 would need, recorded, not weighed. The company says "any further significant delay in the
  collection of our claims could constrain our capital allocation strategy with respect to the timing of stock repurchases" (Q3
  10-Q).
- Dividend $0.31 a quarter (8-Ks of 2026-03-05, 2026-06-03, 2026-09-17).

**Bearing on Q9 (debt and exposures).**
- Total debt principal $2,745.2M, net debt $1,732.3M at 2026-06-30; leverage covenant at or below 4.00 to 1 on the credit
  agreements; a new $500M revolving credit agreement of 2026-06-10 (8-K 2026-06-11).
- Guarantees: AECOM Capital "may provide guarantees of certain financial obligations, including guarantees for completion of
  projects, repayment of debt" (Item 1); "a potential liability as one of the indemnitors on a divested business’ surety bonds" with
  no range given (Q3 10-Q, Note 15). Guaranteed-maximum-price work was 37% of fiscal 2025 revenue.

**Bearing on Q12.** Nothing found that bears on it.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (`ea6d12cf`); written question by question; committed after Q1 (`bc99b023`) and Q2
      (`4aa0380b`), and after the computation and the box.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (`_overnight.lock` was present in
      `Screens/_daily/` when the run began); the fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One file-name listing of `Test Runs/` filtered for
      the ticker was run before I recalled that a listing counts; it showed two names of another company (ACM Research), declared
      under contamination at the top and not opened. That is a breach of the letter of the blind rule, confessed.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-16 ACM/check_ids.py` (no E-ids; every
      id present; every quoted fragment beside an id found in that row); every filing fact carries its document and accession.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is NOT REACHED or headed COMPUTATION,
      NOT A CLEARANCE, with no entry language.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash less stock pay, capital spending, finance-lease
      principal and minority distributions; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations and Q2); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings mean (three years) was not used; the five-year
      series was rebuilt from the filed statements.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 on a technology threat that has not yet arrived.** **[M1998-008]** sends to Q1's filter any business "where we
think the future technology could hurt the business as it presently exists", while the routing paragraph sends to Q1 only the
business "whose industry changes fast", and Q2's test 11 asks what "could destroy, modify or reduce" the strengths. AECOM's own
10-K names AI as a tool that will speed design for a firm paid by the hour; the industry has not changed fast on the filed record.
I read the routing paragraph as governing and carried AI to Q2; another analyst could close at Q1 TOO HARD (NATURE) on the same
row, and the box would differ (TOO HARD against OUT) with a different re-look. The text could say whether a prospective technology
threat that the filer itself names, but that has not yet moved the figures, belongs at Q1 or at Q2 test 11. (2) **"Ordinary
returns" for a business with no tangible capital.** Q3 measures on tangible capital and sets goodwill aside **[M2011-060]**, which
gives returns of several hundred percent or an undefined figure for all three firms; the capital paid for them gives ordinary
returns. The ordinary-returns item of Q2 does not say which capital it means; I did not rest the box on it and decided on the money
test. (3) **Net of businesses sold.** Specific (c) deducts "cash paid for businesses, net of businesses sold"; it does not say how to
treat payments made after the window on a sale made before it (here $308M of exit payments in fiscal 2021 and 2022). I treated them
as exit costs shown beside; the text could say. (4) **A window that ends just before a known loss.** Fiscal 2026 has not closed, but
three quarters of it are filed and contain a $336.8M loss and an operating-cash collapse. Specific (a) speaks of end years of the
window, not of a filed year after it; I kept the literal window and showed the trailing year beside. (5) **Interest on the
all-equity basis.** The text says owner cash "before interest" but not whether to add back interest paid (cash) or interest expense
(which here included a redemption premium classified in financing); I used cash interest paid less interest income, after a
21% rate confessed as this run's CONVENTION, and the choice decides the sign of the shown growth (minus 2.87% against plus 1.85% on the
equity-only series). (6) The brief and the template ask for the balance sheets "in Step 0" when the file closes before Q4; the
template's Step 0 has no line for them. I added one.
