# Company Run — Box Ships Inc. (OTC Pink: TEUFF; formerly NYSE: TEU) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind
run under `Screens/_daily/_dispatch_brief.md`, with the brief's three stated departures (lines of evidence derived from
the 20-F itself; competitors only as the 20-F names them; the filing set is the last 20-F and the 6-Ks after it, the company
having deregistered in 2018). Every judgment cites a v5 ledger id in bold; every filing fact carries its accession.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (3c91d728): `PORTFOLIO.md` read for this ticker only; not held.*

**Contamination declared.** Seen by accident, not used: the session's opening git status (research folders of two other
companies by date and ticker) and the last five commit subjects (two other companies' v5 re-runs), both put in front of the
session before any work; the operator's memory index lines on the queue (counts of runs and gate-clearers, nothing about this
name). One listing of `Test Runs/` filtered for "TEUFF" was made before the template was copied, to check that no file of
today's name existed; it returned nothing. No search was made for the former ticker TEU or the name in `Test Runs/`, and no
blind-listed file was opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.00001 (close 2026-10-15, volume 0; OTC Markets OTCPK; Yahoo chart API through `tools/sources.py`,
  **aggregator, flagged** per operator rule 5). The last day with any volume was 2026-03-13 (423 shares at $0.00001); the
  52-week high is $0.0001; the quote's own "regularMarketPrice" field prints 0.0. The quote is a sub-penny print on a stock
  that mostly does not trade.
- **Shares by class:** common 2,912,257 outstanding at 2016-12-31 (20-F cover and balance sheet; issued equals outstanding,
  no treasury shares at that date) and 2,913,370 "as of the date of this annual report" (Item 4.A), after the 1-for-50 reverse
  split of 2017-01-31; warrants for 75,847 common; 879,833 Series C 9.00% Cumulative Redeemable Perpetual Preferred, liquidation
  preference $25.00 a share plus accrued unpaid dividends (20-F FY2016, filed 2017-03-13, accession `0001615774-17-001018`).
  Later 6-Ks: two exchanges of Series C for convertible notes (36,900 preferred for a $143,910 note, 6-K 2017-07-17,
  `0001615774-17-003678`; 25,588 preferred for a $73,970 note, 6-K 2017-12-27, `0001615774-17-007607`), each convertible at 60%
  of the lowest VWAP of the prior 21 trading days; no 6-K states a later common count, and the Form 15 states none. **The
  count today is not on any record.** `python Screens/cover_shares.py TEUFF` failed ("NOT AN SEC REGISTRANT in the live ticker
  file"); the count is taken by hand from the filed cover (operator rule 4).
- **Market cap:** about $29 (2,913,370 × $0.00001), on the last filed count, which later conversions may have raised.
- **Sovereign for the earnings currency (USD):** 5.43%, US Treasury daily par yield curve, 30-year, 10/15/2026
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 20-F FY2016 (2017-03-13, `0001615774-17-001018`) and its 20-F/A (2017-03-16,
  `0001615774-17-001086`, filed "solely to correct a clerical error, whereby the name and signature of the auditing firm,
  Deloitte Certified Public Accountants S.A., was missing in the electronic version of the audit report"); the 20-Fs for FY2015
  (`0001615774-16-005107`), FY2014 (`0000919574-15-003118`), FY2013 (`0000919574-14-002363`), FY2012 (`0000919574-13-002244`)
  and FY2011 (`0001193125-12-119758`); the 6-Ks after the last 20-F (2017-04-19 `0001615774-17-001772`, 2017-05-31
  `0001615774-17-002816`, 2017-06-15 `0001615774-17-003176`, 2017-06-23 `0001615774-17-003320`, 2017-07-14 `0001615774-17-003647`,
  2017-07-17 `0001615774-17-003678`, 2017-12-27 `0001615774-17-007607`, 2018-03-09 `0001615774-18-001776`, 2018-04-20
  `0001615774-18-002774`); the Form 15-12B (2018-04-20, `0001615774-18-002778`, Rule 12g-4(a)(1), "Approximate number of
  holders of record as of the certification or notice date: 30"). No later primary document: EDGAR lists nothing from the
  company after 2018-04-20; www.box-ships.com did not respond on 2026-10-16, and its Wayback capture of 2023-03-20 is an empty
  "Index of /" (only cgi-bin). There is no proxy after the 2017 meeting materials of 6-K 2017-04-19.
- **One figure cross-checked against the filed statement:** total assets at 2016-12-31, $2,875,705, in Item 3.A's selected
  data, equals the consolidated balance sheet (page F-3); stockholders' equity $244,345 equals the balance sheet and Note 3.
- `python tools/run.py TEUFF` failed ("TEUFF: not an SEC filer", the ticker absent from the live ticker file). The arithmetic
  is by hand from the filed cash flow statements: owner cash = cash from operations less all capital spending (vessels,
  improvements, other fixed assets), USD: FY2012 -29,888,622 (32,531,933 less 62,420,555 of vessel acquisitions); FY2013
  38,197,504; FY2014 19,822,381; FY2015 13,213,612; FY2016 -9,434,063 (-9,299,923 less 134,140). Five-year average 6,382,162.
  Depreciation was 15.0 to 15.1 million a year in FY2012 to FY2015 against no vessel spending in FY2013 to FY2015. Stock pay
  (2,066,688 in FY2013, 2,247,002 in FY2014, 678,721 in FY2015, 200,205 in FY2016) is inside these figures as a non-cash add-back
  and is not deducted in them; it is noted, not recast, since the file closes at Q1 (below). Sources: FY2013 20-F cash flow
  statement for FY2012 and FY2013, FY2016 20-F cash flow statement for FY2014 to FY2016; working table in
  `Test Runs/_research 2026-10-16 TEUFF/_notes.md`.

**The lines of evidence (departure 1), chosen from the last 20-F and why.** (1) Item 4.B, Business Overview: what the
company is at its last report, since Q1 asks where its economics will be. (2) Item 3.D, Risk Factors, the going-concern factor
and the competition and conflicts factors: what the company itself says threatens it. (3) Item 5.A and 5.B, Operating Results
and Liquidity: how the fleet was lost and what income remains. (4) Item 7.B, Related Party Transactions: the chairman's
companies were the managers, the office landlord, the buyers of three vessel subsidiaries and the only customers after the
sales, so this item is where the remaining business lives. The 6-K of 2018-03-09 is read as the last word on (1).

**The balance sheets first, FY2010 to FY2016** **[M2025-032]** (read here because the file closes before Q4). USD millions,
from Item 3.A of the FY2012 20-F (2010, 2011) and of the FY2016 20-F (2012 to 2016, restated for the 2016 debt-cost
presentation):

| Dec 31 | Total assets | Vessels and fixed, net | Current liabilities | Long-term liabilities | Equity |
|---|---|---|---|---|---|
| 2010 | 0.43 | 0 | 0.43 | 0 | -0.004 |
| 2011 | 401.4 | 367.0 | 22.4 | 196.7 | 182.4 |
| 2012 | 443.0 | 401.3 | 42.1 | 180.2 | 220.8 |
| 2013 | 428.0 | 386.2 | 182.8 | 0.5 | 244.7 |
| 2014 | 396.9 | 371.1 | 140.0 | 0.3 | 256.7 |
| 2015 | 355.8 | 334.3 | 127.6 | 0.003 | 228.2 |
| 2016 | 2.88 | 0 | 2.63 | 0.001 | 0.24 |

What moved and why: a fleet bought in 2011 and 2012 ($328.5 million and $62.4 million of vessel spending, FY2013 20-F cash flow
statement) on about $200 million of bank debt; in 2013 the debt moved from long-term to current liabilities, the mark of
covenant waivers that the FY2016 20-F says ran through 2014, 2015 and 2016 ("During 2014 and 2015, we entered into new or
supplemental agreements with our lenders and agreed to certain amendments, waivers"); equity was held up by share and preferred
issues (common in 2012 to 2014, the Series C in 2013) while the vessels were written down ($21.6 million in 2015, $240.0 million
in 2016); in 2016 every vessel went, by settlement sales and by transfer of three vessel subsidiaries to the chairman's
affiliates, and the debt went with them. At 2016-12-31: cash $36,764, restricted cash $10,000, due from related parties
$2,712,303 (the bulk of the assets), dividends on preferred payable $1,994,812, accumulated deficit $248,390,627 against
additional paid-in capital of $248,597,051. What the figures say: the owners' paid-in capital is gone. What they do not say:
the common's position after the Series C, whose $25.00 liquidation preference on 879,833 shares is about $22.0 million plus
unpaid dividends, ranks ahead of it against $0.24 million of book equity. What they cannot say: anything after 2016; the company
filed no statements after the FY2016 20-F.

## THE FOUNDATIONS (not a gate)
The first foundation bears hardest: a share is bought for the cash the business will produce, and the test is "Would I be happy
buying this stock if the market closed for five years?" **[M1997-109]**. For this share the market has in practice already
closed (no volume on most days of 2026), and at its last report the business produced no cash: its own filing says general and
administrative expenses "are expected to exceed revenues from commercial services agreements". The market's quote of a
hundred-thousandth of a dollar instructs nothing **[M2006-077]**. Who is paid to tell you **[M2020-037]**: no adviser covers
the name; the only outside capital after the fleet was lost came from note holders converting at 60% to 65% of the lowest
recent price, who are paid by converting and selling, not by the business (20-F FY2016 Note 9; 6-Ks 2017-07-17 and 2017-12-27).
The habit asked of the analyst is to look for "what you’re missing" **[M2025-013]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the company was not liquidated on the record; the 6-K of 2018-03-09 says it "may continue to try again in
the future, to seek ways to restructure its equity and debt capitalization, and to raise capital sufficient to re-commence
operations in the shipping industry"; (2) the chairman's group owned and managed vessels at the last report (Item 7.B), so a
restart had a willing operator beside it; (3) at about $29 of market value the dollars at risk are trivial, which is a fact
about the price and not about the business; (4) nothing after 2018-04-20 is on the record, so a restart after that date, if one
happened, would be invisible to this run.

## THE STANDING RULE
A purchase of this common, unlevered and sized as a few dollars, puts the buyer at no risk of ruin: the loss is capped at the
price paid and no one can call for more; the rule's forms (borrowed money **[M2004-065]**, "Never risk permanent loss of
capital." **[L2023-005]** as a rule of conduct) bind only how it would be financed and held. The one feature to note for the
buyer is that the share cannot in practice be sold (zero volume), so it could not be a source of cash on any day **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**, and the
  question is whether "the financial statements will tell me the information that’s useful to me in making a judgment about what
  the future financial statements are going to look like" **[M2008-033]**, with the decision made off the figures: "if you can’t
  make a decision on something like PetroChina off the figures, forget about going further" **[M2008-069]**.
- **The filing facts.** (a) The business the statements of FY2011 to FY2015 describe, owning nine containerships on time
  charter, no longer exists: "Following the sale of all of our vessels in 2016, we began operations as a commercial management
  services provider to international shipping companies" (20-F FY2016, Item 4.B, `0001615774-17-001018`). (b) The business that
  replaced it was two commercial services agreements, effective 2016-12-01, with Mone Shipping Co. and Venet Shipping Co., "each
  the owner of a drybulk vessel" and "beneficially owned by our Chairman", paying "a chartering commission equal to 2% of the gross
  freight" (Item 7.B); it earned $11,542 in December 2016 (income statement, "Commercial services fees, related party"), and the
  filer expected about $140,000 over the next twelve months against general and administrative expenses expected to exceed it,
  "resulting in an operating cash deficit" (Note 3). (c) By 2018-03-09 that too had stopped: the company "currently has no active
  operations in the shipping industry" and "presently does not have any available credit, bank financing or other external
  sources of liquidity. The Company needs to obtain capital in order to re-commence operations and fund its activities." (6-K,
  `0001615774-18-001776`). (d) Six weeks later it ended its rights plan and filed Form 15 (`0001615774-18-002774`,
  `0001615774-18-002778`); it has filed nothing since.
- **The key variables and whether they are foreseeable** **[M1998-044]**. At the last report there is no earning power to
  foresee: no vessel, no charter, no credit, a fee stream below its costs that had itself stopped. The only path to earnings the
  filer names is to raise new capital and "re-commence operations", that is, to buy a fleet and start a containership owner
  again from nothing. Every variable that would decide the ten-year economics (what is bought, at what price, on what financing,
  chartered at what rates) belongs to a business that does not yet exist. That is a start-up, and the rows refuse it by name:
  "Start-ups are not our game." **[L2007-015]**; "We don’t do startups." **[M2008-088]**. Read as a whole-business test, the
  acquisition criteria ask for "Demonstrated consistent earning power" and exclude "turnaround" situations **[R1997-001]**; the
  record shows neither earning power nor anything but a hoped-for turnaround (said of whole businesses; weighed here, not a STOP
  by itself).
- **Why OUT and not TOO HARD.** The box TOO HARD is for a question that cannot be answered from where the analyst stands
  **[M2000-038]**. This one is answered by the company's own filings: the economics at the last report are stated (none), and
  the past statements cannot tell the future ones because the business they describe was surrendered **[M2008-033]**. What is
  unknown, the years since 2018-04-20, could change the box only if it showed a restarted business, and a business restarted
  from no fleet is the start-up the rows exclude; no primary document exists to read, so it is not WORK, and the forecast that
  is missing is not one the industry's insiders would decline to write but one the issuer stopped publishing. On the record
  that exists the question is answered against the name. The doubt rule points the same way: "if you have doubts about
  something being into your circle of competence, it isn’t." **[M2002-092]**.
- **Contrary evidence** **[M1997-127]**: the competing reading is TOO HARD (NATURE), on the ground that no one outside the
  company can now see what it is; it is set aside above because the deciding fact (no operations, no liquidity, a plan to start
  again) is on the record and does not need the missing years. A primary document from the company dated after 2018-04-20,
  if one ever appears, is new evidence for a new run, not a reopening of this one by price **[M2000-038]**.
- **VERDICT: OUT.** At its last filed record (6-K 2018-03-09, `0001615774-18-001776`) Box Ships has no operations, no
  liquidity and no reporting; its only route to earnings is a new start, which the rows rule out **[L2007-015]**,
  **[M2008-088]**; the statements that exist describe a business it no longer owns **[M2008-033]**, **[M2008-069]**.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1).

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion.
NOT REACHED. (The balance sheets were read in Step 0 as the template asks when the file closes before Q4.)

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts are recorded under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The reporting figures are under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q1**: at its last filed record the company has no operations, no liquidity and no reporting, and its
only route to earnings is a new start **[L2007-015]**, **[M2008-088]**; integrity facts recorded, not judged.
COMPUTATION, NOT A CLEARANCE: value range $0.00 to $0.00 a share against a flagged aggregator quote of $0.00001.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; no verdict; the box unchanged,
operator rule 2.)*

**Bearing on Q2 (the castle and the competitors).** The 20-F names no rival as a rival: "Ownership of containerships is
highly fragmented and is divided among over 600 independent containership owners" (Item 4.B, Competition), and "We expect
substantial competition for providing new containership service from a number of experienced companies, including
state-sponsored entities and major shipping companies" (Item 3.D), none named. Paragon Shipping is named only as an affiliate
bound by a non-competition agreement with the company and its chairman (Item 4.B), not as a competitor. So the brief's
competitor row (departure 2) has no named filer to read; no CONVENTION rivals were chosen, the file having closed at Q1.
Rate history in the filer's words: the Box Emma earned "approximately $12,300 during 2015, compared to $19,000 per day" in
2014, and the Box Hong Kong and Box China about $17,240 and $17,760 a day in 2015 against $26,800 in 2014 (Item 5.A).
Customers: MSC, CMA CGM, Hapag Lloyd and Chenglie Navigation were 91% of FY2016 revenues (Item 4.B). The vessels were sold
"at a time when vessel prices were low" under lender settlements (Item 3.D).

**Bearing on Q3 (capital).** "Our business is capital intensive" (Item 5.B). Vessel spending $328.5 million (FY2011) and
$62.4 million (FY2012); depreciation $15.0 to $15.1 million a year in FY2012 to FY2015 with no vessel spending in FY2013 to
FY2015 (cash flow statements, FY2013 and FY2016 20-Fs). Net income $13.2 million (FY2012) and $15.3 million (FY2013) on
year-end equity of $220.8 million and $244.7 million, then $2.6 million (FY2014), -$27.0 million (FY2015) and -$226.6 million
(FY2016) (Item 3.A). Accumulated deficit at 2016-12-31 $248.4 million against additional paid-in capital of $248.6 million.

**Bearing on Q4 (the accounts).** The auditor's report "contains an emphasis of matter paragraph indicating that there is a
substantial doubt concerning our ability to continue as a going concern" (Item 3.D; Note 3). The electronic audit report in the
original 20-F lacked the auditor's name and signature, corrected three days later by the 20-F/A (`0001615774-17-001086`).
FY2016 operating cash flow was -$9.3 million; the net loss of $226.6 million is mostly the $240.0 million impairment and $14.8
million loss on sales, offset by a $24.7 million gain on debt extinguishment and an $18.3 million gain on deconsolidation
(income statement). Stock pay was added back in cash from operations each year (Step 0) and not recast.

**Bearing on Q5 (integrity; recorded, not judged; a later run that reaches Q5 must answer them **[M2013-088]**).**
1. Mr. Michael Bodouroglou held the offices of Chairman, President, Chief Executive Officer and Interim Chief Financial Officer
   together (20-F FY2016, throughout).
2. In November 2016, in the settlement of the $100 million ABN AMRO loan, the company "sold all of the issued and outstanding
   capital stock of the subsidiaries owning the Box Voyager, Box Trader and Maule to entities affiliated with Mr. Michael
   Bodouroglou" and was released from the loan (Item 5.A); the income statement shows a "Gain from deconsolidation of
   subsidiaries" of $18,268,964, a "Loss from deconsolidation of subsidiaries, related party" of $403,090 and a "Loss on
   sale of vessels, related party" of $385,337. The exhibit list names the shareholders party to the 2016-11-24 Third Amending
   and Restating Agreement as Azul Shipping Co., Mist Shipping Co. and Great Wave Shipping Co. What the chairman's entities paid
   or assumed beyond the loan is not stated in the passages read.
3. After the sales the company's only revenue came from two drybulk owners "beneficially owned by our Chairman" at a 2% chartering
   commission, $11,542 in FY2016 (Item 7.B; income statement).
4. The managers of the fleet (Allseas, Seacommercial, Crewcare) and the office landlord (Granitis Glyfada Real Estate Ltd.) were
   companies controlled by the chairman (Item 7.B); management fees to Allseas were $2.2 million in FY2016 and $2.4 million in
   FY2015; related-party general and administrative expenses were $2.7 million in FY2016 (income statement). The 20-F itself
   names the conflict: "our Managers may give preferential treatment to vessels that are beneficially owned by related parties"
   (Item 3.D).
5. As of 2017-03-09 the chairman beneficially owned less than 1% of the common and 23.7% of the Series C preferred (Item 7.A),
   which ranks ahead of the common.
6. Series C dividends were not paid from 2016-04-01, and the company was out of the preferred's net-worth covenant (Note 3).
   Unrelated holders exchanged Series C at a fraction of liquidation value: 36,900 shares ($922,500 liquidation value) for a
   $143,910 note, and 25,588 shares ($639,700) for a $73,970 note (6-Ks 2017-07-17 and 2017-12-27), about 15.6% and 11.6%.
7. Financing after the fleet loss was by notes convertible at 65% (2016) and 60% (2017) of the lowest VWAP of the prior 21
   trading days; the two 2016 notes of $0.5 million converted into 2,042,527 common shares (Item 5.B; Note 9), against 629,775
   shares issued a year earlier (balance sheet).
8. Dividends of $54.00 (FY2012) and $26.00 (FY2013) a common share on the post-split basis were declared in the two years before
   the covenant waivers began (Item 3.A).
9. The 2017 annual meeting was adjourned three times to solicit votes; the reverse-split authority was "not approved" (6-K
   2017-07-14). The company deregistered on 2018-04-20 with 30 holders of record (Form 15), after which owners receive no reports.

**Bearing on Q6 (the money and the owners).** Share count: weighted average 359,620 (FY2012) to 1,461,786 (FY2016), 2,912,257
at year-end 2016, post-split (Item 3.A; cover). A repurchase of $113,667 in FY2015 (cash flow statement). The buyback test
needs Q7's bottom; not run.

**Bearing on Q9 (debt).** Debt about $200 million at 2011 and 2012; reclassified to current liabilities from 2013 under
waivers; $122.8 million current at 2015-12-31; nil at 2016-12-31 ("As of December 31, 2016, we had no debt outstanding.
Currently, we have no borrowing capacity.", Item 5.B). Senior to the common at the last report: the Series C, 879,833 shares
at $25.00 (about $22.0 million) plus unpaid dividends, with a default dividend step-up of 1.25 times (Item 3.D), less the 62,488
shares exchanged in 2017; and the two 2017 exchange notes ($217,880), redeemable at 127.5% on default.

**Bearing on Q12.** Nothing found.

### Q7 — COMPUTATION, NOT A CLEARANCE (the reporting figures, a reporting convention, not a verdict)
- **Owner cash, the literal window** (Step 0): FY2012 to FY2016 average $6,382,162 a year, after interest (equity-only basis).
  It is the cash of a fleet the company no longer owns: every vessel was sold or transferred in 2016.
- **Specific (a), the aberrational year.** The last window year, FY2016, is aberrational on the filer's own description (all
  vessels sold under lender settlements; the business changed to commercial services). There is no full cycle of the business
  that remains, so no cycle base exists for it; the base is the remaining business's own stated stream: commercial services
  fees of about $140,000 over twelve months against general and administrative expenses expected to exceed them, "resulting
  in an operating cash deficit" (Note 3), and from 2018-03-09 no operations at all (6-K `0001615774-18-001776`).
- **Specific (b), decline.** The series changes sign and the remaining stream is negative; the range is the no-growth case
  alone, said so. No growth case exists to make a second end.
- **Specifics (c) to (f).** (c) No acquisitions; the 2016 disposals are the loss of the earning base, not a deal to value
  beside. (d) Working capital: the remaining asset is $2.7 million due from related parties, not a stream. (e) No maintenance
  guess is possible for a company with no fixed assets. (f) No growth is carried, so no cap applies.
- **Value of the common.** A negative stream has no positive present value at the 5.43% Treasury rate **[M1994-077]**; on the
  last balance sheet the common ranks behind about $20.4 to $22.0 million of Series C preference against $0.24 million of book
  equity. **Value range: $0.00 to $0.00 a share** (the arithmetic is negative; a limited-liability share is floored at
  nothing).
- **The floor, tested first.** No case in the range earns the floor at any positive price, so none earns it at $0.00001
  **[M2003-149]**. Had Q7 been reached it would close OUT on the floor; it was not reached.
- **Fair price (Part VII, each end at ten percent, averaged): $0.00 a share** on the all-equity basis (no debt at the last
  report; the Series C counted as a senior claim) and **$0.00** on the equity-only basis beside it. The price, $0.00001
  (aggregator, flagged), is above both; no cheap price is reported.
- **The literal window beside, not a case:** at no growth, $6,382,162 at 5.43% is $117.5 million, less the Series C liquidation
  preference of $22.0 million, $95.5 million, $32.81 a share on 2,912,257 shares; at ten percent, $63.8 million less $22.0
  million, $14.36 a share. These figures value vessels the company surrendered in 2016 and are shown only because Q7's range
  convention asks for the literal window beside; they are not a value of this company.

### Research pass
None. The box is OUT, not TOO HARD (WORK), and no case of the computation earns the floor at the price (Part VII, When a
research pass is run).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `e5c0725f`); written question by question; committed after Q1's close
      and after the closing sections (write-early).
- [x] Dispatched: the brief allowed per-question pathspec commits; a lock file was present in `Screens/_daily/` (seen by a
      filtered listing, not opened); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, save the one filtered listing of
      `Test Runs/` for today's ticker before the copy, declared under Contamination; what was seen by accident is declared there.
- [x] Every v5 id resolves (`Test Runs/_research 2026-10-16 TEUFF/check_cites.py`: no E-ids, every M/L/R id in the CSV, every
      quoted fragment beside an id in that row); every filing fact has its accession; the share count after 2017 is stated as
      unknown, not guessed.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash from operating cash less all capital spending, never a net-income proxy (operator rule 5); the sovereign from
      the US Treasury, dated; the price an aggregator quote, flagged. Stock pay was not recast (noted in Step 0), which bears only
      on the literal window shown beside.
- [x] Contrary evidence written down as found (Foundations; Q1); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; rows of any date are admissible.
- [x] `tools/run.py` and `Screens/cover_shares.py` both failed for a deregistered foreign filer; no line of either was used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The framework has no rule for an issuer that has stopped reporting. Section I's recorded absence, "A verdict for a document
not yet read", is about a document that exists and was not read; here no document exists after 2018-04-20, so research cannot
cure the gap (not WORK), and the two-cause test for NATURE (would the industry's insiders write the forecast down) does not fit
a company whose own management simply stopped publishing. I closed OUT at Q1 because the last filed record states the deciding
fact itself (no operations, no liquidity, a plan to start again) and the rows exclude a start-up by name; another analyst could
close TOO HARD (NATURE) on the ground that no one outside can see the company now, and the framework does not choose between
them. Two smaller gaps followed from the same case: Q1's start-up exclusion does not say whether a former operator that must
"re-commence operations" from no assets is a start-up (I read it as one, my reading, not a row's); and Q7's specifics value a
deal closed after the window but say nothing of a business that lost its whole earning base inside the window, so the required
literal window beside produces a positive per-share figure from vessels the company no longer owns, which I printed and
labelled as not a case. The template's Step 0 also asks for "the latest 10-Q, the proxy", and both tools assume a live ticker;
for a deregistered 20-F filer there is no quarterly report, the last proxy is of 2017, and the share count after the 2017
convertible notes is on no record, so the market cap is undefined beyond "about $29 on the last filed count".
