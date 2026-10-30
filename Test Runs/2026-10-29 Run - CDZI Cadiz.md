# Company Run — Cadiz Inc. (Nasdaq: CDZI; depositary shares of the Series A preferred: CDZIP) — 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-29, after the run was committed (b033e194): not held (`PORTFOLIO.md` read for this ticker only).*

**Dispatched run.** Done by a dispatched analyst under the brief of 2026-10-29 (the canonical brief
`Screens/_daily/_dispatch_brief.md` with two stated departures: the repository path is `C:\Projects\BRK`, and the lines of
evidence and the competitors were derived by the analyst, not listed in the brief). Template copied to this file before any
fetch (commit `0f7005d6`).

**Contamination, declared.** (1) Before any fetch I ran one file-name search of the `Test Runs/` listing for "cdzi" or
"cadiz", to confirm no earlier run file stood under the dated name; it returned no match, and no other file name was read.
The brief counts a search across `Test Runs/` as opening it, so it is declared here; nothing was seen. (2) The session
context showed three recent commit subjects (Passed Companies pages; the overnight log; the audit of the automated runs of
2026-10-28) and the git status listing of untracked daily digests and coursework files; none names this company. (3) The
memory index lines loaded with the session name no company. Nothing from any of these was used.

**Lines of evidence chosen, and why** (derived from Item 1, Item 1A and Item 7 of the 10-K for FY2025): (a) the two segments
and which one carries the value (Note 3); (b) the state of the Mojave Groundwater Bank: permits held and still needed, the
water-supply contracts and their conditions, the construction budget and its guaranteed maximum prices (Item 1; 8-Ks of
2026-07-15 and 2026-07-28); (c) the financing the project needs and what the owner of a common share keeps after it (Item 1,
Project Infrastructure Finance; the Lytton Credit Agreement, 8-K and 424B5 of 2025-10-28; MWI); (d) the debt, its
maturities and its interest paid in kind, the preferred stock, the lease obligation (Note 7; the 10-Q for 2026-06-30);
(e) share issuance and its prices over ten years (balance sheets; Item 7 equity offerings); (f) stock pay and the milestones
it vests on (proxy of 2026-04-30); (g) the record of the project's earlier forecasts (10-Ks for FY2012 and FY2016), because
Item 1A says the company "cannot predict with certainty when, if ever" the water assets will earn. Litigation: Item 3 reports
none material. Acquisitions: ATEC assets in 2022 (goodwill $1.9 million) and the Northern Pipeline in 2021 ($19 million).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $4.72 (close 2026-10-28; `tools/run.py` aggregator quote, flagged per operator rule 5: a live quote only).
- **Shares by class** from the latest filing's cover: 84,677,075 common shares (10-Q for the quarter ended 2026-06-30,
  filed 2026-08-13, accession `0001437749-26-027664`, cover as of 2026-08-11; `python Screens/cover_shares.py CDZI`, single
  class). Check: the 10-Q balance sheet shows 84,161,245 issued and outstanding at 2026-06-30, no treasury shares; the
  difference of about 0.5 million is consistent with the August 2026 Lytton draw of $10 million, which carries a funding fee
  of 25,000 shares per $1 million (250,000 shares), and quarterly vesting of restricted units (10-Q, Note 3 and liquidity
  section). Also outstanding: 329 shares of Series 1 Preferred (convertible at 405.05 common each, about 133,000 common) and
  2,300 shares of 8.875% Series A Cumulative Perpetual Preferred (2,300,000 depositary shares, liquidation preference
  $25,000 a share, $57.5 million in all; 10-K FY2025 Item 5). Potential dilution not in the count: about 11.4 million shares
  from options, units, convertible debt, preferred and warrants (10-Q, net loss per share note); the Heerema convertible
  loan alone converts into 4,590,867 shares at $5.04 and the Heerema warrant into 1,000,000 at $4.75 (proxy of 2026-04-30,
  accession `0001437749-26-014053`, ownership table notes). No 424B5 after the 10-Q was found in the filing index (read
  2026-10-29); an S-8 of 2026-08-14 registers plan shares.
- **Market cap:** $399.7M (84.677M x $4.72).
- **Sovereign for the earnings currency:** USD 5.37%, 30-year par yield, US Treasury daily par yield curve, 2026-10-28
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-03-31, accession `0001437749-26-010517` (Items 1, 1A, 2, 3,
  5, 7, the statements and Notes 2, 3, 7, 12); 10-Q for 2026-06-30, accession `0001437749-26-027664` (statements, going-concern
  and liquidity paragraphs, Notes 3 and 10, MD&A liquidity); DEF 14A filed 2026-04-30, accession `0001437749-26-014053`
  (summary compensation, employment arrangements, ownership); 8-Ks of 2026-07-15 (`0001213900-26-078146`, BLM right-of-way),
  2026-07-28 (`0001213900-26-082311`, GMP agreements), 2026-07-27 (`0001213900-26-081581`, CFO succession), 2026-06-23
  (`0001437749-26-021420`, authorized shares 100M to 125M), 2026-05-20 (`0001437749-26-017950`), 2026-02-04
  (`0001213900-26-012370`), 2025-10-28 (`0001213900-25-102822`, Lytton) with the 424B5 of the same day
  (`0001213900-25-102814`); for the record of the project and the cash interest, the 10-Ks for FY2012
  (`0000727273-13-000008`), FY2016 (`0000727273-17-000008`), FY2021 (`0001437749-22-007512`), FY2022 (`0001437749-23-008639`)
  and FY2023 (`0001437749-24-009847`). **One figure cross-checked against the filed statement:** net cash used in operating
  activities FY2025, $(18,930) thousand on the filed cash-flow statement of `0001437749-26-010517`, against -18.9 in
  `tools/run.py`; agrees. Also checked: FY2025 capital spending $7,576 thousand (statement) against 7.6 (tool).
- `python tools/run.py CDZI` arithmetic lines only: owner cash (operating cash less stock pay less capital spending) was
  negative in every year shown: FY2023 -28.2, FY2024 -27.1, FY2025 -31.8 ($ millions); the five-year window FY2021 to FY2025
  averages -30.8 on the capital-spending basis and -23.6 on the depreciation basis. The tool found no securities inside
  operating cash, no other stock-pay line, no intangible or software spending. It does not see two items read in the
  filing: a $5.0 million deposit for a pipe purchase option in FY2025 (investing, "Additions to deposits for asset purchase
  options") and interest paid in kind and accreted on the lease obligation ($2.8 million and $2.7 million in FY2025), which
  are non-cash in operating cash and are added to the debt. Stock pay is resolved: "Compensation charge for stock and share
  option awards" $5,299 thousand FY2025, $4,605 thousand FY2024 (cash-flow statement).

**The balance sheets, ten year-ends, read before the income account** **[M2025-032]** ("balance sheets over an 8 or 10 year
period before I even look at the income account"; `tools/run.py` table, first-filed XBRL, checked against the FY2025 and
2026-06-30 statements). What moved and why:
- **Equity** was negative from 2016 to 2020 (-$54.3M to -$86.2M), turned positive in 2021 ($40.6M) only by share issuance and
  the conversion of debt, and has fallen since every year: $34.2M (2022), $40.0M (2023, after a raise), $34.0M (2024), $23.3M
  (2025), $4.7M at 2026-06-30. The accumulated deficit went from -$409.9M (2016) to -$712.2M (2026-06-30). Additional
  paid-in capital is $716.0M: the owners have put in about $716 million and the business has lost about $712 million of it.
- **Cash** never exceeded $17.3M at a year-end in ten years and stood at $5.3M at 2026-06-30, against an operating cash
  drain of about $19M to $22M a year; the company has been financed from outside every year (proceeds from common stock in
  ten of the twelve years 2014 to 2025, $207.8M in all, by XBRL `ProceedsFromIssuanceOfCommonStock`).
- **Receivables and inventory** were trivial until ATEC (receivables $39 thousand in 2016, $5.6M in 2025; inventory $3.0M in
  2024, $1.1M in 2025); they move with ATEC's single large Utah order, which MD&A names.
- **Debt** on the face of the balance sheet: $102.5M (2016) rising to $137.6M (2019), cut to $78.6M (2020) and $46.6M (2021)
  by conversion and refinancing, then $37.9M (2023), $56.8M (2024), $72.8M (2025), $87.0M at 2026-06-30, plus a lease
  obligation labelled "with related party" of $29.4M that accretes interest (it began as a $12.0 million one-time payment
  in 2016 from Fenner Valley Farms for a 99-year farm lease, carried as a financing obligation: `CapitalLeaseObligations`
  $12.8M in 2016; 10-K FY2025 Note 12). The 10-Q states the annual effective interest rate on the debt at 15.4%.
- **Goodwill** $3.8M (land and water) plus $1.9M (ATEC) since 2022. **Water programs** are carried at cost and not depreciated
  because "the Mojave Groundwater Bank is not operating" (10-K FY2025, Note 2).
- **Shares outstanding** (balance-sheet counts): 13.7M (2010), 21.8M (2016), 36.9M (2020), 55.8M (2022), 75.4M (2024),
  83.2M (2025), 84.7M (cover, 2026-08-11). About six times the 2010 count.
- What the figures say: a forty-year-old company whose principal asset has never earned, funded by selling shares and
  borrowing. What they cannot say: whether the project will be built, financed and paid for, and what share of its cash a
  common holder would keep.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, bought for what the asset produces. "Would I be happy
buying this stock if the market closed for five years?" **[M1997-109]**: with the market closed, a holder of this share owns a
business that has consumed cash every year on record and must sell more shares or borrow to continue (Step 0). Whatever
return a buyer gets must come from the project being built and paying, not from the record. **Contrary evidence, written
down as found** **[M1997-127]** ("write it down in the first 30 minutes"): (1) the BLM granted the Northern Pipeline
right-of-way for water conveyance, effective 2026-07-14, after a NEPA assessment and a finding of no significant impact
(8-K `0001213900-26-078146`); (2) guaranteed maximum prices of $273.8M were signed on 2026-07-27 for the pump stations and
pipeline replacement, inside a Northern Pipeline budget of $403.3M (8-K `0001213900-26-082311`); (3) contracts for 21,275
acre-feet a year with public water systems exist, subject to conditions (10-K Item 1); (4) the CEQA permits of 2012 were
upheld by the courts in 2014 and 2016 and can no longer be challenged (10-K Item 1); (5) ATEC grew revenue from $7.9M to
$14.5M in 2025 with segment operating income of $2.5M (Note 3). Each is weighed at Q1 below.

## THE STANDING RULE
Owning this does not put the buyer at risk of ruin so long as the purchase is made without borrowed money and sized so that
a total loss of it is bearable; "Never risk permanent loss of capital." **[L2023-005]** and "We are never going to risk what
we have and need for what we don’t have and don’t need." **[M2012-081]**. The buyer's financing and sizing are not known to a
blind analyst; nothing in the target changes this line. Not a verdict on the business.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the text states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The
first step is the key variables and how predictable they are: "If something is not very predictable, forget it."
**[M1998-044]**; and whether the past statements tell the future ones, "do I understand enough about this business so that the
financial statements will tell me the information that’s useful to me in making a judgment about what the future financial
statements are going to look like" **[M2008-033]**.

**Which part decides.** Two segments (10-K FY2025, Note 3). Land and Water Resources: FY2025 revenue $1.8M, operating loss
$(28.1)M, assets $130.9M; it holds the Mojave Groundwater Bank, "pre-revenue development" in the filer's words. Water
Filtration Technology (ATEC): revenue $14.5M, operating income $2.5M, assets $10.0M. The company's five-year operating result
is a loss in every year, so no part carries "more than half" of a positive five-year operating profit, and Q2's business-of-
parts paragraph falls to "the largest part". **CONVENTION of this run:** where the company's five-year operating profit is
negative, the largest part is read by segment assets and by what the market price pays for; rationale: the text's threshold
needs a positive total, and here ATEC's operating income ($2.5M in its best year) could not account for a market value of
about $400M plus about $111M of net debt, so the price is a price for the water project. The deciding part is Land and Water
Resources; ATEC does not decide and is carried to the facts below.

**The key variables of the deciding part, and whether they are foreseeable from the filings:**
1. *Permits still to come.* Before water moves in the Northern Pipeline the company needs change-of-use authorizations from
   the BLM (granted, effective 2026-07-14), the Air Force and the California State Lands Commission, the last including a
   finding under California Water Code Section 1815, "the 2019 law that requires desert groundwater projects to apply for a
   review by the CSLC prior to moving water" (10-K Item 1). The Southern Pipeline, meant for about 30,000 of the 50,000
   acre-feet a year, needs an agreement with the Metropolitan Water District to use the Colorado River Aqueduct and the same
   CSLC finding (10-K Item 1). Storage of imported water needs a third EIR addendum and amended monitoring plans (10-K Item
   1). The filer: "Because of the discretionary nature of these approvals, our ability to secure these approvals and receive
   income from our water assets could be delayed, reduced or eliminated based on regulatory processes." (10-K Item 1,
   Regulation).
2. *The record of the same kind of decision.* Between 1997 and 2002 the company and Metropolitan received "substantially all
   of the state and federal approvals required", and in October 2002 "By a very narrow margin, the Metropolitan Board voted
   not to accept the right-of-way grant nor proceed with the 2002 Project" (10-K FY2016, `0000727273-17-000008`, Item 1). In
   2015 the BLM's California office found the Southern Pipeline outside the railroad right-of-way, reversed by a new
   evaluation in 2020 (10-K FY2016; 10-K FY2025 Item 1). In 2019 California enacted the Section 1815 review the CSLC must now
   make. The key approvals have turned on boards' and agencies' votes, and have turned both ways.
3. *Financing.* The full build is estimated at $1.25 to $1.5 billion, up from about $800 million "from our previous estimate"
   (10-K Item 1); the Northern Pipeline alone at $403.3M (8-K 2026-07-28). Equity of about $451M is targeted, of which $51M
   (Lytton) is committed and $400M is in "due diligence with private equity investors"; the filer: "Any agreements announced
   with these potential investors are not binding" (10-K Item 1A). The 10-Q of 2026-08-13 still reports the $400M in due
   diligence. The WIFIA loan of up to $194M is an invitation to apply (10-K Item 1).
4. *What a common share keeps.* On closing, Cadiz expects to contribute its pipelines and the supply contracts' cash flows to
   MWI and to receive "an upfront capital reimbursement payment at closing and an equity interest in MWI" (10-Q MD&A);
   Lytton may convert its loan into a right to 51% of the cash flows of water storage (10-K Note 7). The terms of Cadiz's
   equity interest in MWI are not set in any filing read. So even the fraction of the project's cash that belongs to this
   share cannot be read today.
5. *Price and volume.* About $850 an acre-foot (2024 dollars) net to Cadiz at the wellhead, "estimated", after the buyers pay
   capital and operating costs (10-K Item 1); 21,275 acre-feet a year contracted, "subject to the satisfaction of certain
   contractual conditions and completion of the necessary construction" (8-K 2026-07-15). At full contracted Northern
   volume that is about $18M a year before the company's own costs; the Land and Water segment's general and administrative
   expense alone was $25.0M in FY2025 (Note 3). Whether the whole 50,000 acre-feet is ever sold depends on items 1 to 4.
6. *The filer's own forecast.* "We have not received significant revenues from these development activities to date and we
   cannot predict with certainty when, if ever, we will receive operating revenues from these business segments sufficient
   to offset the costs of our development activities." (10-K Item 1A). The FY2016 10-K expected in 2017 "to finalize contracts
   with Project participating agencies, as well as continue final design and implementation planning for Project
   construction"; no water has been delivered nine years later.

**Applying the tests.** The past statements cannot tell the future ones **[M2008-033]**: the record is of a business that has
never sold its principal product, and the figures that would matter (volume delivered, price realized, the owner's share of
MWI) have no history. The key variables are approvals by bodies that have reversed themselves, financing not yet signed, and
terms not yet negotiated; they are important and, today, not knowable: "If something’s important but unknowable, forget it."
**[M2006-076]**; "If something is not very predictable, forget it." **[M1998-044]**. The filer itself will not write the
forecast down (item 6), which is test 5's mark **[M2000-105]** ("would not want to put down on paper their predictions").

**The routing.** In substance the deciding part is a project that has not begun business: no water sold in forty years, a
construction programme of $1.25 to $1.5 billion still to be financed, an operating entity (MWI, formed December 2024) still to
receive its equity. Q1's list of what it rules OUT names it: "Start-ups are not our game." **[L2007-015]**, a sentence the row
sets against businesses that "began business in 1837 and 1886"; "We don’t do startups." **[M2008-088]**. The 2000 letter puts
the same class among those whose birds cannot be counted: "This kind of uncertainty frequently occurs when new businesses and
rapidly changing industries are under examination. In cases of this sort, any capital commitment must be labeled
speculative." **[L2000-026]**. A doubt about the circle is an answer: "if you have doubts about something being into your
circle of competence, it isn’t." **[M2002-092]**. The contrary evidence written down above is real progress (a federal
right-of-way, fixed construction prices for the pump stations and pipe, contracts for 85% of the Northern Pipeline's
capacity), and it narrows one of the six variables; it does not make the other five foreseeable, and it is evidence about
the project's next step, not about the economics ten years out.

**VERDICT: OUT** at Q1, on the start-up rows **[L2007-015]**, **[M2008-088]** applied to the deciding part, with the filing
facts above (10-K `0001437749-26-010517` Items 1 and 1A; 10-Q `0001437749-26-027664`; 8-Ks of 2026-07-15 and 2026-07-28).
The alternative reading, TOO HARD (NATURE) on test 4 **[M2006-076]** and test 5 **[M2000-105]**, closes the file the same way:
the deciding questions are future votes, signatures and terms that no filing not yet read can answer, and a lower price
reopens neither box **[M2000-038]** ("It just means that we don’t know how to evaluate it."). The choice between the two is
set out under WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (Q1 closed the file).
The competitor row was not filled: the file closed at Q1. For the record: the 10-K names no competitor by name for either
segment ("We face competition in the acquisition, development and sale of water and land assets from a variety of parties";
in groundwater treatment "we compete with companies that offer products similar to ours", Item 1, Competition), so no
SEC-filing rival is named by the filer, and none was chosen.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the balance sheets were read in Step 0).
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.

## Q7 — WHAT IS IT WORTH? NOT REACHED. The reporting figures below are COMPUTATION, NOT A CLEARANCE.
**COMPUTATION, NOT A CLEARANCE** (operator rule 3; the brief's reporting convention; Part VII, The owner's price). Built by
Q7's range convention from the five-year window FY2021 to FY2025 (script and output: `Test Runs/_research 2026-10-29
CDZI/calc.py`, `calc_output.txt`). USD millions unless per share.

| FY | operating cash | stock pay | capital spending (+ option deposit) | depreciation | cash interest paid | owner cash, all spending, before interest | owner cash, maintenance only, before interest |
|---|---|---|---|---|---|---|---|
| 2021 | -15.274 | 4.747 | 22.908 (Northern Pipeline bought for $19M inside it) | 0.423 | 2.6 | -40.329 | -17.844 |
| 2022 | -18.599 | 1.876 | 3.376 | 0.654 | 3.5 | -20.351 | -17.629 |
| 2023 | -20.924 | 1.496 | 5.787 | 1.247 | 1.6 | -26.607 | -22.067 |
| 2024 | -21.532 | 4.605 | 0.934 | 1.214 | 1.5 | -25.571 | -25.851 |
| 2025 | -18.930 | 5.299 | 7.576 + 5.000 | 1.264 | 1.7 | -35.105 | -23.793 |
| average | | | | | | **-29.593** | **-21.437** |

Sources: the filed cash-flow statements of each year's 10-K (accessions in Step 0; FY2024 from `0001437749-25-009714` via
`tools/run.py` and XBRL); cash interest from each 10-K's debt note ("approximately $2.6 million", $3.5M, $1.6M, $1.5M, $1.7M
"paid in cash"). Operating cash already excludes the interest paid in kind and the accretion on the lease obligation; on the
equity-only basis below those non-cash charges are a further real cost to the common holder that the figure does not show.
- **The maintenance guess (specific (e)).** The water assets are not in service and are not depreciated (Note 2); the
  depreciation charge, $0.4M to $1.3M a year, covers the farm, ATEC and offices, and is taken as the maintenance guess,
  "not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**, with the
  owner "entitled to my best guess" **[M2000-144]**. Spending above it (the pipeline, engineering, the pipe option) is growth
  spending. Most of the Land and Water segment's $25.0M of general and administrative expense is in substance project
  development, but the filing does not split it, so it stays a cost in both cases.
- **Growth (specific (b)).** Owner cash is negative in every year of the window; a compound rate between two negative figures,
  and between the halves of the window, is meaningless, so the range is the no-growth case alone, said so. No growth
  spending is carried (year one $0, year ten $0). Growth that consumes cash early can destroy value **[L2000-023]**; the
  window shows only the cost side.
- **Cycles (a), acquisitions (c), working capital (d), the cap (f).** No end year is called aberrational by the filer;
  the 2021 pipeline purchase is an asset bought for cash and is counted as capital spending; working capital moves are
  inside operating cash; no growth is carried, so no cap applies.
- **Net debt at the latest filed date (2026-06-30, 10-Q `0001437749-26-027664`):** long-term debt $86.978M + current
  $0.007M + the lease obligation with related party $29.446M (a financing obligation accreting interest, counted as debt;
  operating leases of $3.5M left out, said so) less cash $5.319M (long-term restricted cash $2.759M not counted) =
  **$111.1M**. The subsequent event the 10-Q states, a $10M Lytton draw in August 2026, adds equal debt and cash and leaves
  net debt unchanged. **CONVENTION of this run:** the Series A preferred, liquidation preference $57.5M, cumulative at
  8.875%, is a claim senior to the common that the text's definition of net debt does not name; it is shown deducted beside
  the central figure; rationale: its $5.1M a year is paid in cash ahead of the common, and leaving it out flatters the common.
- **Value range (sovereign 5.37%, no growth, ten years then zero nominal growth, i.e. a level perpetuity), all-equity basis
  (central):** enterprise -$399.2M (maintenance only, the top) to -$551.1M (all spending, the bottom); less net debt, **-$6.03
  to -$7.82 a share** against a price of **$4.72**; with the preferred deducted, -$6.71 to -$8.50. Equity-only basis
  (owner cash after cash interest, against the market value of the shares), beside: -$5.19 to -$6.99 a share. The literal
  window and the convention coincide (no end year adjusted).
- **The floor, tested first:** no case earns about ten percent at the price, or any positive return; the owner-cash yield at
  the price on the all-equity, maintenance-only case is -4.2% (-$21.4M against an enterprise value of $510.8M). On the
  record, "there’s just a point at which we drop out of the game" **[M2003-149]**. The width test is not reached.
- **Fair price** (Part VII: each end case valued at ten percent, the two averaged, after the company's own tax, which is
  about nil: income tax paid $11 thousand a year): all-equity basis (central) **-$4.33 a share** (-$5.00 with the preferred
  deducted); equity-only basis beside, -$3.27 a share. A negative fair price is the statement: the business as filed
  consumes cash, and every dollar of value in the price rests on the project, which the record does not show. No cheap
  price is reported.
- **What the range leaves out, said plainly.** The convention values the record. The bush here is a project whose cash, if
  it comes, comes after a construction programme of $1.25 to $1.5 billion financed mostly by others, and whose share for
  this common stock is not yet defined (Q1, item 4); "if somebody is reinvesting all their cash flow the next five years,
  they’d better have some very big figures coming in down the road" **[M1998-082]**, and the first question is "are you going
  to have to put more cash into after you buy it?" **[M2014-068]**. No project case was computed: it would be a projection of
  management's, which the rows do not use **[M1995-050]**, and Q1 closed the file before any value question opens **[M1994-077]**.
- **Research pass:** none is owed. The box is OUT, not TOO HARD (WORK); and under Part VII a pass is run only where some
  case of the range earns the floor at the price, which none does.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
## Q10 — IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q1** (the deciding part, the Mojave Groundwater Bank, is a start-up in substance: no water sold in forty
years, permits, financing and the owner's share of MWI still to come; **[L2007-015]**, **[M2008-088]**). COMPUTATION, NOT A
CLEARANCE: value range -$6.03 to -$7.82 a share on the all-equity basis against $4.72; fair price -$4.33. Integrity facts
recorded, not judged (serial issuance; see AFTER THE STOP, Q5). No re-look alert can be set at the top of the computed
range, which is negative.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).

**Bearing on Q2 (the castle).**
- ATEC: revenue $7.9M (2024) and $14.5M (2025); segment operating income $1.7M and $2.5M, 21.7% and 17.2% of revenue; the
  2025 figure includes the company's largest project ever (320 filters, Central Utah); revenue fell to $0.98M company-wide in
  the second quarter of 2026 against $4.1M a year earlier (10-Q). The filer names no dominant competitor (Item 1).
- The water supply's stated cost to buyers is $1,450 to $1,950 an acre-foot before grants (Item 1); the filer calls it
  "among the lowest cost supplemental water supply available in the region" (Item 1). The competitive factors it names are
  "location, price and reliability of delivery" (Item 1).
- The Southern Pipeline needs the agreement of Metropolitan, whose board refused the 2002 project (10-K FY2016).

**Bearing on Q3 (capital).** Owners have paid in $716.0M and the accumulated deficit is $712.2M (10-Q). The build cost rose from
about $800M to $1.25 to $1.5 billion in the latest estimate (Item 1). Capital costs are to be "recovered in fees collected
from agencies" (Item 1), so the capital is mostly not Cadiz's; nor, therefore, is most of the cash.

**Bearing on Q4 (the accounts).** Stock pay $5.3M in FY2025 against revenue of $16.3M. Interest paid in kind $2.8M and lease
accretion $2.7M in FY2025 are non-cash in operating cash and added to debt. The balance-sheet line "Long-term lease
obligations with related party" ($29.4M) is not explained in the notes read (Note 12 covers operating leases only); its
origin was traced through XBRL history to the $12.0M Fenner Valley Farms payment of 2016, carried as a capital lease
obligation from 2016 to 2018. Who the related party is was not found in the documents read. The auditor (PwC, since at least
1995) gave a clean opinion; its critical audit matter was the accounting for the Lytton Credit Agreement's fee shares
(10-K, auditor's report). No EBITDA or adjusted figure was found featured in the 10-K or 10-Q text searched.

**Bearing on Q5 (the people), integrity facts recorded, not judged.**
- Serial issuance: common shares from 13.7M (2010) to 84.7M (2026); equity sold in ten of the twelve years 2014 to 2025
  (XBRL), most recently 7,000,000 shares at $3.34 (November 2024) and 5,715,000 at $3.50 (March 2025) (Item 7); authorized
  shares raised from 100M to 125M on 2026-06-18 (8-K `0001437749-26-021420`). The text names this among the tells: "we have
  never invested in companies that are hell-bent on issuing shares" **[L2014-015]** (carried at Q6 as a candidate second
  STOP, OPEN). The filer's own explanation: development costs must be bridged until revenue begins (Item 7).
- The forecast record: the FY2016 10-K expected in 2017 to "finalize contracts with Project participating agencies"; the
  FY2025 10-K expected a Northern Pipeline GMP "during the second quarter of 2026", and GMPs were signed on 2026-07-27. The
  rows ask for the projector's past projections beside the new ones **[M1995-050]**.
- The chief executive, Susan Kennedy, has been Chair since February 2022 and CEO since January 2024 (proxy). Total pay
  $2.28M (2024) and $1.06M (2025) (summary compensation table). Her 600,000 milestone units vest on events such as "the
  closing of project financing necessary for the construction of the Northern Pipeline" and a binding federal right-of-way
  (proxy, Employment Arrangements): pay tied to approvals and financings, not to cash delivered to owners. The new CFO's
  inducement is 800,000 RSUs (200,000 vested on grant) and 800,000 PSUs that vest on stock price hurdles (8-K 2026-07-27).
  The proxy is to be read for how they "treat themselves versus how they treat the shareholders" **[M1994-009]**; not judged here.
- Heerema (HHC $ Fund 2012) holds 25,695,300 shares, 30.5%, and is the senior secured lender, with a convertible loan at $5.04
  and a warrant at $4.75; a gain on the 2024 debt assignment was booked to paid-in capital because Heerema "is a significant
  shareholder" (10-Q Note 3).

**Bearing on Q6 (the money and the owners).** No buybacks. Preferred dividends of $5.1M a year paid in cash in each of 2024 and
2025 while operating cash was negative (cash-flow statements). The Lytton facility pays its lender in shares as well as
interest: 600,000 commitment shares and 25,000 shares per $1M drawn, 800,000 more on an extension (10-K Note 7).

**Bearing on Q9 (could it ruin us).** Total indebtedness $78.3M at 2025 year-end, $63.3M of it secured on substantially all
assets (Item 1A, Item 2); the Heerema secured loans and the older convertible loan mature on 2027-06-30 (Item 7); cash $5.3M
at 2026-06-30; the effective interest rate 15.4% (10-Q). The going-concern assessment in both filings rests on "the ability
to raise capital". "Occasionally, though, [...] maturities must actually be met by payment." **[L2010-020]**. For a whole
business the criterion is "little or no debt" **[R1997-001]**; this is a part-interest, so it would be weighed.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `0f7005d6`); written question by question; committed after Q1 and
      after the closing sections (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (operator rule
      ten). The fold is the dispatcher's; this run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. One file-name search of the `Test Runs/` listing for this
      company was made before any fetch and returned nothing; declared under contamination above.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (check script
      `Test Runs/_research 2026-10-29 CDZI/check_ids.py`, output in the same folder); no E-id; every filing fact carries its
      document and accession.
- [x] The order was kept; Q1 closed the file OUT; every figure after it is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending, with the maintenance case
      beside), never a net-income proxy; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS); facts for later questions under AFTER THE STOP; the integrity
      flag is in the box line.
- [x] No point-in-time anchor; rows of any date may be cited.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield line, its "refused" lines and anything printed as a
      rule were not.
- [x] `python tools/check_framework.py` PASS before the final commit (result in `Test Runs/_research 2026-10-29 CDZI/notes.md`).
- Honest gaps: the shareholder letter of 2026-05-20 (8-K exhibit) was not read beyond its cover; the related party behind
  the lease obligation was not identified; the Air Force and CSLC applications' status after the 10-K was searched for in
  the 10-Q only; the FY2017 to FY2020 10-Ks were not read; no competitor filings were read, since none is named and Q2 was
  not reached.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **"Start-up" is not defined.** Q1's OUT list names start-ups **[L2007-015]**, **[M2008-088]** without saying
whether a company incorporated decades ago, with a small operating business beside it, is one when its deciding part has
never sold its product. I read the start-up by the deciding part's business, which L2007-015 measures by when a business
began business, and closed OUT; a reader who takes the corporate age would reach TOO HARD (NATURE) on tests 4 and 5
**[M2006-076]**, **[M2000-105]**. The two boxes close the file alike here, but they would differ for the alert and for any
re-run, and the text should say which governs a pre-revenue project inside an old company. (2) **The business-of-parts
threshold fails when the company's five-year operating profit is negative**: "more than half" of a loss is meaningless, and
"the largest part" is not said to be largest by what. I confessed a CONVENTION of this run (segment assets, and what the
price pays for). (3) **Q7 on a cash-consuming business.** Specific (b) handles a negative growth rate and a series that
changes sign, but not a series negative in every year; I read "meaningless" to cover it and used the no-growth case alone.
The resulting range and fair price are negative, which is the honest arithmetic and tells the operator nothing he cannot
see at once; the text might say that a range whose top is negative is reported as "no value on the record" rather than as a
figure. (4) **Preferred stock is not named in the net-debt definition** ("borrowings and finance leases less cash and
securities"); a cumulative preferred paid in cash ahead of the common is a senior claim, and I showed it deducted beside the
central figure under a CONVENTION of this run. Also minor: the template's competitor row sits under Q2, while the brief asks
for a competitor comparison in every reply; for a file closed at Q1 the run records only what the 10-K names.
