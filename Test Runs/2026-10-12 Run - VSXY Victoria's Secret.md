# Company Run — Victoria's Secret & Co. (NYSE: VSXY) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatch.** A purchase run of record dispatched under `Screens/_daily/_dispatch_brief.md` (operator rule 10). Research
folder: `Test Runs/_research 2026-10-12 VSXY/` (notes, the fetch script, the Q7 arithmetic script `vsxy_q7.py`, the
citation check; raw filings under `cache/`, ignored).

**Contamination, declared.** (1) Before the template was copied, one shell command listed `Test Runs/` filtered for
"VSXY|VSCO|victoria". It returned nothing: no file about this company under any name was seen. The listing itself was a
search the blind rule forbids, and it is declared here. (2) The session's opening context showed the five most recent
commit subjects of the repository, all about another company's run (a Japanese trading house); nothing about this
company. (3) A memory index line visible at session start names counts of gate-clearers and a paused queue; it names no
company and was not used. No other run file, holding review, `PORTFOLIO.md`, resume-state file or register was opened.

**The company and its corporate events.** Victoria's Secret & Co. was separated from L Brands, Inc. (renamed Bath & Body
Works, Inc.) on 2021-08-02, one VS&Co share for every three L Brands shares (FY2022 10-K, 0001856437-23-000013, Note 1);
trading began on the NYSE on 2021-08-03 as VSCO (FY2025 10-K, Item 5). The ticker became **VSXY** when markets opened on
2026-06-02 (8-K 0001856437-26-000007, Item 8.01; 10-Q 0001856437-26-000021, Note 1). Later corporate events from the
8-Ks: the acquisition of Adore Me, closed 2022-12-30 for cash (8-K 0001193125-23-000224, Item 2.01); a one-year
shareholder rights plan adopted 2025-05-20 "In response to the substantial accumulation of shares" by BBRC International
Pte Limited (FY2025 10-K, Item 1A; 8-K 0001856437-25-000013), expired 2026-05-18 (10-Q, Q2 FY2026); a new director
appointed from 2026-09-14 (8-K 0001856437-26-000017); the Chief Legal and Compliance Officer leaving by 2027-03-31
(8-K 0001856437-26-000023). No signed and unclosed deal, no merger and no share issuance for a deal was found in the
8-Ks filed from 2025-01 to 2026-10-09 (the submissions index, `cache/sub.json`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $88.59 (quote of 2026-10-12 printed by `tools/run.py`; aggregator, a live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, **79,764,039** as of 2026-08-28 (10-Q for
  the quarter ended 2026-08-01, filed 2026-09-04, accession `0001856437-26-000021`; `python Screens/cover_shares.py VSXY`).
  Checked: the balance sheet of 2026-08-01 shows 80 million shares issued and outstanding with no treasury stock (shares
  bought back are retired, 10-Q Note on repurchases: 2.2 million retired year to date); the only 8-Ks after the 10-Q
  (2026-09-03 results, 2026-10-09 an officer's departure) report no issuance.
- **Market cap:** $7,066M (79.764M x $88.59).
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, the issuing authority).
- **Filings read** (operator rule 4): 10-K for fiscal 2025 (year ended 2026-01-31), filed 2026-03-20,
  `0001856437-26-000004` (Items 1, 1A, 2, 3, 5, 7, 7A, 8: statements and the notes on tax, debt, repurchases); 10-Q for
  the quarter ended 2026-08-01, filed 2026-09-04, `0001856437-26-000021`; proxy statement filed 2026-05-01,
  `0001193125-26-201438` (summary compensation table, say-on-pay, ownership); 10-Ks for fiscal 2021
  (`0001856437-22-000007`), 2022 (`0001856437-23-000013`), 2023 (`0001856437-24-000005`) and 2024
  (`0001856437-25-000006`) for the statements of the earlier years; 8-Ks listed above. **Carve-out figures, labelled:**
  fiscal 2019 and 2020 are combined carve-out statements printed in VS&Co's own fiscal 2021 10-K, and fiscal 2021 itself is
  "consolidated and combined" (carve-out until 2021-08-02); fiscal 2014 to 2018 appear only as the Victoria's Secret
  segment inside L Brands' 10-Ks (fiscal 2015, `0000701985-16-000051`; fiscal 2018, `0000701985-19-000015`), operating
  income and sales only, the international business reported in a separate segment.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, fiscal 2025,
  $499M in the filed consolidated statement of cash flows (10-K `0001856437-26-000004`, Item 8), equal to the XBRL figure
  `tools/run.py` printed. Capital expenditures $187M and share-based compensation $55M also agree.
- **`python tools/run.py VSXY`, arithmetic lines only** (Part VII; its v4 floor and verdict language not used): OCF less
  SBC less capex, fiscal 2023 $77M, 2024 $187M, 2025 $257M; on the D&A basis $49M, $107M, $206M. The five-year window it
  prints (OE capex mean $279M) begins in fiscal 2021. The run's own owner-cash series, the full window and the
  adjustments are under the Q7 COMPUTATION below and in `vsxy_q7.py`.
- **The lines of evidence chosen, from the latest 10-K's Items 1, 1A and 7** (the brief's instruction): (a) the
  customer and the fashion cycle, since the filer says "Customer demands and fashion trends change rapidly" (Item 1A) and
  names its dependence on "bras, panties and other intimates products" (Item 1A); (b) margins over the whole record,
  since Item 7 reports an operating income rate of 4.1% against 5.0% the year before; (c) the competition, which Item 1
  and Item 1A describe only by category ("specialty retailers, department stores, mass merchandisers, online retailers,
  discount retailers and private-label and emerging brands"); (d) tariffs and pricing, since Item 7 puts the net tariff
  cost of fiscal 2025 at about $85M and Item 1A says the "ability to mitigate cost increases through pricing is limited by
  competitive dynamics and consumer price sensitivity"; (e) debt, leases and buybacks (Item 7, Liquidity); (f) the Adore
  Me acquisition and its $120M impairment (Item 7, non-GAAP table note (a)); (g) stock pay and the adjusted figures
  (Item 7). Litigation: Item 3 reports only ordinary-course suits not expected to be material.
- **Competitors** *(CONVENTION of this run: the brief asks for "the rivals the 10-K itself names"; the fiscal 2025 10-K
  names none, only categories. The rivals chosen are the closest by product that file with the SEC; rationale: the brief's
  rule has no instance to apply, and a category cannot be compared)*: American Eagle Outfitters (its Aerie segment,
  intimates and apparel; 10-Ks `0001193125-26-132097`, `0000950170-23-007604`, `0001564590-20-010469`) and Bath & Body
  Works (fragrance and body care, the beauty half, and the former parent; 10-K `0000701985-26-000008`). Flagged as not read
  and not SEC filers in their own right: Skims and Savage X Fenty (private); Hanesbrands, now inside Gildan Activewear,
  which files a 40-F (not read).

### The balance sheets, read first (the file closes before Q4; the template asks for them here) **[M2025-032]**
Fiscal year-ends, USD millions, from the filed statements (fiscal 2019 and 2020 carve-out; `tools/run.py` table checked
against the 10-K balance sheets of fiscal 2021, 2022, 2025 and the 10-Q):

| year-end | total assets | equity (VS&Co) | cash | inventory | goodwill + trade names | debt (face of the sheet) | lease liabilities |
|---|---|---|---|---|---|---|---|
| 2020-02-01 (carve-out) | n/r | 1,314 (parent's net investment) | 245 | n/r | n/r | 0 | n/r |
| 2021-01-30 (carve-out) | 4,229 | 891 (parent's net investment) | 335 | 701 | n/r | 0 (97 from former parent) | n/r |
| 2022-01-29 | 4,344 | 257 | 490 | 949 | 0 | 982 | n/r |
| 2023-01-28 | 4,711 | 383 | 427 | 1,052 | 365 + 180 | 1,275 | n/r |
| 2024-02-03 | 4,600 | 417 | 270 | 985 | 367 + 155 | 1,124 | n/r |
| 2025-02-01 | 4,532 | 640 | 227 | 955 | 367 + 281 (trade names) + 95 other | 977 | 1,721 |
| 2026-01-31 | 5,013 | 856 | 518 | 1,071 | 367 + 246 | 975 | 1,871 |
| 2026-08-01 (10-Q) | 5,155 | 990 | 522 | 1,146 | 367 + 246 | 975 | 1,924 |

(n/r: not read in this run. The intangible column before 2023 is the `tools/run.py` transcription; the trade-name lines
for 2025 and 2026 are from the filed sheets.)

What the sheets say. (1) The equity is a separation artefact, not an accumulation: the parent's net investment of $2,380M
(2019) and $1,314M (2020) fell to $257M at the first standalone year-end, because the company borrowed $982M at the
spin and paid "Net Transfers to Former Parent" of $1,253M in fiscal 2021 (cash-flow statement, FY2021 10-K). Retained
earnings since then are $504M (2026-01-31), against $725M spent on buybacks from fiscal 2021 to the first half of fiscal
2026 (see Q6 facts below). (2) Debt has been flat at about $975M since 2024 (a $600M 4.625% note due July 2029 and a term
loan due August 2028), with cash rising to $518M at 2026-01-31 and $522M at 2026-08-01. (3) Inventory rose faster than
sales: $701M against sales of $5,413M (fiscal 2020, 13%) and $1,071M against $6,553M (fiscal 2025, 16%); the filer ties
the fiscal 2025 rise to international growth, the European distribution centre and tariff-inflated unit costs (Item 7,
operating activities). (4) The goodwill and trade names are Adore Me's and the Victoria's Secret names; the Adore Me
intangibles were written down by $120M in fiscal 2025 (Item 7). (5) Lease liabilities of $1.87B exceed the funded debt
and are the larger fixed claim; they are left out of net debt and said so (Q7 basis).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, which for a fashion retailer turns on the business, not the quote. The market serves and does not
instruct: the price has moved from $34.60 (November 2025 buyback-withholding average, 10-K Item 5) to $88.59 in eleven
months, and "It just tells us prices" **[M2006-077]**; the move is no evidence about the business. No macro forecast
enters **[M2000-094]**: tariffs appear below only as a property of the business (its pricing freedom), never as a
forecast. Who is paid to tell you: the company's own adjusted figures and guidance are noted under Q4 facts **[M2020-037]**.
The analyst's habits: the previous conclusion is the worst anchor **[M2016-054]**, and the search is for "what you’re
missing" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the first half of fiscal 2026
shows net sales up 12.7% ($3,170M against $2,812M) and an operating income rate of 10.5% (10-Q); even without the $135M
tariff refund booked in costs of goods sold the first half earned about $197M of operating income ($333M less $135M and $1M of refund) against $61M; the
business may be turning. (2) The international channel grew 27% in fiscal 2025 (Item 7), and franchise royalties need
little capital. (3) The filer calls itself "the world’s largest intimate apparel company" with "a leading market share"
(Item 1). Each is weighed where it belongs below; none is set aside.

## THE STANDING RULE
Owning this risks nothing of the buyer's that the buyer's own financing and sizing do not create: a common share bought
outright with no borrowed money cannot call the buyer **[L2014-005]**, and the rule binds the buyer: "We are never going to
risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. Nothing here raises it.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it.** "can I understand it?" **[M1995-051]**, where to understand is to have "a reasonable
fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**. The
product is not the question. Bras, panties, sleepwear, lounge, swim and fragrance, sold through 790 company-operated
North American stores (54% of fiscal 2025 sales), its own websites (31%) and partners in about 70 countries (15%), are
easy to describe (10-K `0001856437-26-000004`, Item 1). The rows say why that is not enough: "We just don’t know the
economics of it 10 years from now." **[M2000-104]**.

**The key variables, and how predictable they are** **[M1998-044]**. (1) The place of two brands in the customer's mind:
Victoria's Secret for bras and PINK for young women, read in units and average unit retail. (2) The promotional level,
which sets the gross margin: the filer credits fiscal 2025's gross profit to "a decrease in promotional activity, an
increase in regular-priced selling" (Item 7). (3) Mall traffic, since the filer relies "to a greater degree than some of
our competitors on physical locations in shopping malls" (Item 1A). (4) Input cost and duties, which the filer says it
cannot freely pass on (Item 1A). The filer itself rates the first variable: "Customer demands and fashion trends change
rapidly." (Item 1A).

**Do the past statements tell me the future ones?** **[M2008-033]** The record, operating income as a share of sales:

| fiscal year | net sales $M | operating income $M | rate | source and label |
|---|---|---|---|---|
| 2014 | 7,207 | 1,271 | 17.6% | L Brands 10-K FY2015 `0000701985-16-000051`, Victoria's Secret segment (carve-out inside L Brands' filings; international excluded) |
| 2015 | 7,672 | 1,391 | 18.1% | same |
| 2016 | 7,781 | 1,173 | 15.1% | L Brands 10-K FY2018 `0000701985-19-000015`, segment (2016 sales = 2017's 7,387 plus the 394 decline stated) |
| 2017 | 7,387 | 932 | 12.6% | same |
| 2018 | 7,375 | 462 | 6.3% | same |
| 2019 | 7,509 | (892) | (11.9%) | VS&Co FY2021 10-K, combined carve-out, after a $720M goodwill impairment |
| 2020 | 5,413 | (101) | (1.9%) | same, carve-out, pandemic store closures |
| 2021 | 6,785 | 870 | 12.8% | FY2021 10-K, consolidated and combined; the filer names "federal stimulus benefits" in the year's first quarter |
| 2022 | 6,344 | 478 | 7.5% | FY2022 10-K |
| 2023 | 6,182 | 246 | 4.0% | FY2025 10-K |
| 2024 | 6,230 | 310 | 5.0% | FY2025 10-K |
| 2025 | 6,553 | 271 | 4.1% | FY2025 10-K, after the $120M Adore Me impairment and the $69M interchange-fee gain |
| H1 2026 | 3,170 | 333 | 10.5% | 10-Q `0001856437-26-000021`, including $135M of tariff refund in costs of goods sold (about 6.2% without it) |

In twelve years the rate went from 18% to a loss, back to 13%, down to 4%, and the first half of fiscal 2026 is turning up
again. Sales of $7.7B in 2015 (the domestic segment alone) are $6.6B in 2025 (with the international channel). The past
statements do not tell me the future ones: they record a business whose earning power moved by more than ten points of
margin, twice, in both directions, inside one decade, with the same brands and the same stores. Asked "do I understand
enough about this business so that the financial statements will tell me the information that’s useful to me in making a
judgment about what the future financial statements are going to look like" **[M2008-033]**, the answer is no.

**Would the insiders write it down?** **[M2000-105]** The filer's own long-range writing is a strategy, not a forecast:
the "Path to Potential" of 2025, "built around four key priorities", among them "Recommit to PINK" and "Evolve Our Brand
Projection & Go-To-Market Strategy" (Item 7). The forecasts it does write run one quarter and one year ahead (the 8-K of
2026-09-03, `0001856437-26-000019`, furnishing "third quarter and updated full year 2026 earnings guidance"). The forecast
insiders wrote before, in the goodwill carried for the business, was written off: $720M impaired in fiscal 2019 (FY2021
10-K, combined statement of income). The management has turned over since the spin: a charge in fiscal 2024 "related to
the appointment of a new CEO and the elimination of two executive officer roles", and charges in fiscal 2025 "to continue
to restructure our executive leadership team" (Item 7, non-GAAP note (f)).

**Can I name the winner, not just the industry?** **[M2012-067]** The one rival that files and reports an intimates
business separately, Aerie (American Eagle Outfitters), grew from $990M of revenue in fiscal 2020 to $1,941M in fiscal
2025 (AEO 10-Ks `0000950170-23-007604` and `0001193125-26-132097`, segment notes), while the leader's sales fell from
$7,509M (fiscal 2019) to $6,553M (fiscal 2025). The private rivals (Skims, Savage X Fenty) are not on the public record.
The winner of the next ten years in women's intimates cannot be named from the filings, and on the filed evidence the last
five were won by a challenger, not by the leader.

**Is the forecast about customers or about technology?** **[M2017-019]**, **[M2023-030]** About customers, which is the
kind the rows say can sometimes be projected: "we know what we think we can project out in terms of consumer behavior and
threats to a business" **[M2023-030]**. Here the behaviour to be projected is fashion and the image of a brand among
young women, and the filer's own word for it is "rapidly". It is the case the 1993 letter names before it reaches
technology: "In many industries, of course, Charlie and I can't determine whether we are dealing with a "pet rock" or a
"Barbie."" **[L1993-023]**.

**Do I only think I understand it?** The narrated example is this very trade: "I think it’s easy to sort of think you
understand retail, and then subsequently find out you don’t" **[M2014-052]**; "what would bother me is if I think I
understand a business and I don’t." **[M1997-024]**. And the conservative edge of the perimeter: "if you have doubts
about something being into your circle of competence, it isn’t." **[M2002-092]**. I have the doubt, on the record above.

**Routing.** A business of parts? The company reports one segment (Item 1), and its channels share brands, stores and
supply; Q1's by-parts reading does not apply. A bank? No. The routing that applies is the one fixed in Q1: a business
whose ten-year economics cannot be foreseen because its industry changes fast closes at Q1, TOO HARD, not OUT; change is
"more of a threat into the investment process than an opportunity" **[M1999-063]**. The change here is in the customer,
not in technology; the filer names it, the record shows it, and the H1 2026 upturn is one more swing of the same kind,
not evidence that the swings have stopped.

**Which cause.** The deciding question is where the two brands' share of mind and their margin will stand in ten years.
It is important and not knowable: "If something’s important but unknowable, forget it." **[M2006-076]**. No filing not
yet read would answer it; the insiders' own record of forecasting it is the impairment and the strategy resets above; and
study would not cure it: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying
those industries." **[L1993-023]**; "we’re not going to learn enough in the followings five months to make up for the
fact that we went in deficient in the first place." **[M2008-086]**. The cause is NATURE. A lower price does not reopen it.

**What the verdict is not.** It is not a finding that the business is poor or the price high: "It doesn’t mean it isn’t a
good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate
it." **[M2000-038]**. The contrary evidence written at the foundations (the first-half recovery, the international
growth, the scale) is real; it is the kind of movement that cannot be projected ten years.

- **VERDICT: TOO HARD (NATURE)**, among the three boxes **[M2006-013]**. Filing facts: "Customer demands and fashion
  trends change rapidly." (10-K `0001856437-26-000004`, Item 1A); operating income rates from 18.1% (2015, carve-out
  segment inside L Brands) to (11.9%) (2019, carve-out) to 12.8% (2021) to 4.1% (2025); a rival's intimates revenue
  doubled in five years while the leader's sales fell.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (the file closed at Q1). Facts under AFTER THE STOP.
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0).
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED as a question; the operator's two reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price (the operator's two reporting figures)
*Operator rule 3: the file closed at Q1; everything in this section is arithmetic made after the closing STOP. It carries
no entry language and changes no box. The script is `Test Runs/_research 2026-10-12 VSXY/vsxy_q7.py`; every input is a
filed figure with its accession in the script's comments.*

**The cash input** (Q7's range convention; Q4's recast). Owner cash after every real cost = net cash from operations, less
share-based compensation, less all capital spending, less the minority partner's share of the China joint venture's net
income; on the all-equity basis the cash interest paid is added back after tax at 24.7% (21.0% federal plus 3.7% state,
the fiscal 2025 rate reconciliation). Equity-only figure (interest not added back) beside. *(CONVENTION of this run: the
minority's 49% of the consolidated China joint venture is deducted at its share of net income, the only figure the filer
gives for it; rationale: that cash is not the shareholders', and the text gives no rule for a consolidated partner.)* The
company's own tax is inside operating cash (cash taxes paid: $74M, $54M, $87M in fiscal 2023 to 2025); no carryforward
shelter is priced, since the U.S. business pays at the statutory rate and the $113M of loss carryforwards are mostly
non-U.S. and largely under a valuation allowance (FY2025 10-K, Note 10).

| fiscal year | OCF | SBC | capex | D&A | interest paid | NCI | owner cash, all-equity | equity-only | D&A variant | purchases of businesses |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019 (carve-out) | 315 | 38 | 225 | 411 | 8 (expense) | 0 | 58 | 52 | (128) | 0 |
| 2020 (carve-out) | 674 | 25 | 127 | 326 | 0 | 0 | 522 | 522 | 323 | 0 |
| 2021 (part carve-out) | 851 | 33 | 169 | 303 | 18 | 0 | 663 | 649 | 529 | 0 |
| 2022 | 437 | 48 | 164 | 274 | 52 | (10) | 274 | 235 | 164 | 387 |
| 2023 | 389 | 56 | 256 | 284 | 87 | 7 | 136 | 70 | 108 | 0 |
| 2024 | 425 | 60 | 178 | 258 | 77 | 4 | 241 | 183 | 161 | 161 |
| 2025 | 499 | 55 | 187 | 238 | 66 | 28 | 279 | 229 | 228 | 4 |

**The specifics, applied.** (a) **Cycle.** The literal window is fiscal 2021 to 2025. Its first year is aberrational on
the filer's own description: "federal stimulus benefits recognized in last year's first quarter" (FY2021 10-K, outlook),
and it is in part a carve-out year. So the base is the last full cycle of owner cash, trough to trough, fiscal 2019
(58) to fiscal 2023 (136), peak fiscal 2021 (663): average **$330M**, with fiscal 2019 and 2020 labelled carve-out. The
literal window's average, $318M, is shown beside. Growth between the averages of successive cycles cannot be measured:
only one full cycle is on file, and the years before 2019 exist only as segment operating income inside L Brands' filings.
*(CONVENTION of this run: the growth is then measured between the first and second halves of the literal window, the
fallback of specific (b); rationale: it is the text's own method where an end-year rate misleads.)* Halves: fiscal
2021-22 average $468M, fiscal 2024-25 average $260M, three years apart: **(17.8%) a year**. The end-year rate, fiscal
2021 to 2025, is (19.5%), shown beside. (b) **Decline.** The growth shown is negative, so the negative case is the bottom
of the range and the no-growth case the top. (c) **Acquisitions.** Adore Me (cash, $369M net of cash acquired, fiscal
2022), the Frankies Bikinis stake ($18M, fiscal 2022), and $161M and $4M of deferred and contingent consideration (fiscal
2024 and 2025, financing lines) are purchases paid in cash: acquisitions, not mergers (a merger is a deal paid in shares,
**[L2009-019]**'s usage as the text adopts it). Default pair: purchases deducted as capital spending, total growth
credited; the filer reports no organic growth separately, so no organic pair is shown. Serial acquirer: purchases over the
literal window ($552M) are less than half of owner cash before purchases ($1,592M), so no. Purchases stop after year ten;
the no-growth case buys nothing and deducts none *(the run's reading of the 2026-10-10 specific; see What was unclear)*.
No signed and unclosed deal and no deal after the window. (d) **Working capital** is inside operating cash; no single
year's draw is tied by the filer to one contract. (e) **Growth spending.** The filing gives no maintenance split (fiscal
2026 capital spending is guided at $220M to $240M for "our store capital program and the customer experience, along with
investments in technology and logistics", Item 7), so the all-spending case is central; the D&A variant is beside.
(f) **The cap** does not bind a negative rate. **Inventory-secured trade finance:** the ABL facility is secured by
inventory and card receivables, and nothing was drawn at 2026-01-31 or 2026-08-01; nothing to treat.

**Basis and net debt.** All-equity basis: debt $975M (4.625% notes due July 2029, $600M; term loan due August 2028) less
cash $522M at 2026-08-01 (10-Q `0001856437-26-000021`) = **net debt $453M**; no later event in the filings changes it.
Operating lease liabilities of $1,924M are left out of net debt, as the text directs, and said so. Shares 79.764M.

**The range** (ten years at the growth shown, then zero nominal growth, discounted at the 30-year Treasury, 5.60%):

| case | business value $M | per share, less net debt | against $88.59 |
|---|---|---|---|
| bottom: base $330M at (17.8%) for ten years, purchases $77M a year deducted, then flat | 964 | **$6.41** | below |
| top: base $330M, no growth, no purchases | 5,901 | **$68.30** | below |
| beside, literal window: bottom ($318M at (19.5%), purchases $110M a year) | 505 | $0.65 | |
| beside, literal window: top ($318M, no growth) | 5,685 | $65.60 | |

The bottom case's cash turns negative in the last years of the ten, where the declining stream falls below the average
purchase spending; that is the arithmetic of specifics (b) and (c) together, not a forecast.

**How it would close, had Q7 been reached.** The floor is tested first (2026-10-10): the top case valued at ten percent is
$3,304M against a business value at the price of $7,519M (market value $7,066M plus net debt $453M), so no case in the
range earns the floor at the price **[M2003-149]**; the file would close OUT whatever the width. The width is 6.1 to 1
(11.3 to 1 on the literal window), more than three to one as well **[L2000-025]**. The price is above the top of the range.
Sensitivity: crediting fiscal 2025 with the $148M of IEEPA tariff refunds received in fiscal 2026 lifts the literal base
to $348M; its no-growth value at ten percent, $3,480M, is still under half the business value at the price.

**THE TWO REPORTING FIGURES** (a reporting convention, not a rule and not a verdict; Part VII):
- **(a) VALUE RANGE: $6.41 to $68.30 a share** (all-equity basis less net debt; the cycle base, fiscal 2019 to 2023, with
  the halves growth), against a price of $88.59. Literal window beside: $0.65 to $65.60.
- **(b) FAIR PRICE: $18.96 a share** on the all-equity basis (each end case valued at ten percent: bottom $626M, top
  $3,304M, averaged, less net debt $453M, over 79.764M shares), after the company's own tax, no conversion.
  **Equity-only figure: $22.56** (owner cash after interest, base $306M, same construction, no net debt deducted). Which is
  which: the all-equity figure is the central one; the equity-only figure never decides alone. Literal window beside:
  $16.12 all-equity, $18.10 equity-only.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1** (the ten-year economics of a fashion-led intimates brand cannot be foreseen: the
filer's "Customer demands and fashion trends change rapidly", and an operating rate that moved from 18% to a loss to 13%
to 4% in a decade). Integrity facts recorded, not judged. COMPUTATION, NOT A CLEARANCE: value range $6.41 to $68.30 a
share and fair price $18.96 (equity-only $22.56) against $88.59. No research pass is opened: the cause is NATURE.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; each with its source **[M1997-127]**.)*

**Bearing on Q2 (the castle).**
- *The competitor row, operating income as a share of sales, same metric from each filer's own filings:*

| fiscal year | VS&Co (total) | Aerie segment (AEO), before unallocated corporate | Bath & Body Works (total) |
|---|---|---|---|
| 2020 | (1.9%) carve-out | 6.1% (adjusted 11.4%) | n/r |
| 2021 | 12.8% | 15.4% | n/r |
| 2022 | 7.5% | 10.9% | n/r |
| 2023 | 4.0% | 16.5% | 17.3% |
| 2024 | 5.0% | 18.2% | 17.3% |
| 2025 | 4.1% | 17.8% | 15.4% |

  Sources: VS&Co 10-Ks above. Aerie: AEO 10-K `0000950170-23-007604` (segment note; fiscal 2020 to 2022 operating
  income as reported) and `0001193125-26-132097` (segment note; fiscal 2023 to 2025 computed as revenue less cost of
  sales, SG&A and D&A as the note lists them). The Aerie figures exclude AEO's unallocated corporate expense ($429M in
  fiscal 2025, 7.7% of AEO's revenue), so they overstate Aerie against VS&Co's all-in rate; AEO as a whole earned 4.1% in
  fiscal 2025 after $102M of impairment and restructuring. BBWI: 10-K `0000701985-26-000008`, statement of income.
  Revenue: Aerie $990M (fiscal 2020) to $1,941M (fiscal 2025); VS&Co $7,509M (fiscal 2019) to $6,553M (fiscal 2025).
- *Pricing:* fiscal 2025 average unit retail rose and promotions fell (Item 7), while the filer says its ability to pass on
  cost "is limited by competitive dynamics and consumer price sensitivity" (Item 1A); net tariffs cost about $85M of
  operating income in fiscal 2025 (Item 7).
- *Footprint:* company-operated stores fell from 915 (start of fiscal 2023) to 858 (end of fiscal 2025); partner stores
  abroad rose from 463 to 562 in two years; U.S. sales per average selling square foot $624 against $589 (Item 1, Item 7).
- *Scale and share:* the filer claims "the world’s largest intimate apparel company" with "a leading market share" (Item 1);
  no market-share figure is given.

**Bearing on Q3 (capital).** Capital spending ran 2.5% to 4.1% of sales in fiscal 2021 to 2025, below depreciation in
each of the last three years ($256M against $284M; $178M against $258M; $187M against $238M) while the store count
shrank. Tangible capital at 2026-01-31, before leases: total equity $910M plus debt $975M less cash $518M, goodwill $367M
and trade names $246M = $754M, against operating income of $271M (fiscal 2025); with the $1,871M of lease liabilities
counted as capital, $2,625M. Arithmetic only; no grade given.

**Bearing on Q4 (the accounts).** The filer features adjusted figures beside GAAP: adjusted operating income $403M
against $271M reported, excluding the amortization of intangibles and "Organizational Restructuring and Other One-time
Items" in both fiscal 2024 ($13M) and 2025 ($20M) (Item 7), the kind of repeated item **[L2016-006]** speaks of; the
company furnishes quarterly and full-year earnings guidance (8-K `0001856437-26-000019`). The auditor (Ernst & Young,
since 2021) gave clean opinions on the statements and on internal control; its critical audit matter is the reserve for
store inventory losses (FY2025 10-K, Item 8). A change in the estimate of gift-card breakage was booked as a cumulative
adjustment in the fourth quarter of fiscal 2024 (Item 7, store data note (b)).

**Bearing on Q5 (integrity, recorded, not judged).** (1) The guidance habit and the featured adjusted figure above, which
the framework carries from Q4 to Q5 **[M2004-067]**. (2) Turnover: CEO appointed September 2024; CFO from January 2025,
who was CFO of JOANN Inc. when it filed for Chapter 11 in March 2024, as the 10-K itself states (Item 1, executive
officers); the COO role eliminated in August 2025 (8-K `0001856437-25-000035`); the Chief Legal and Compliance Officer
leaving by 2027-03-31 (8-K `0001856437-26-000023`). (3) The 2025 rights plan, adopted against BBRC's accumulation and
allowed to expire after one year; BBRC reported 10,310,631 shares (about 13%) in its 13D/A of November 2025 (proxy
`0001193125-26-201438`). (4) CEO total compensation for fiscal 2025 $14,381,494, including a $1,000,000 bonus and
$8,039,570 of stock awards; say-on-pay passed with 76% at the 2025 meeting (proxy). No finding of dishonesty was seen in
the filings read; none of these facts is weighed here.

**Bearing on Q6 (the money and the owners).** Buybacks since the spin: $250M in fiscal 2021 (an accelerated repurchase that
delivered 4.1 million shares and 0.3 million more at final settlement, FY2022 10-K: about $57 a share, computed), $250M in fiscal 2022 at $41.77, $125M in fiscal 2023 at $34.22, $100M in the
first half of fiscal 2026 at $45.27 (10-Ks and 10-Q above); the authorization is "open-ended in term and will continue
until exhausted" and names no price (Item 5). Every price paid is above the bottom of the COMPUTATION range ($6.41); all
four are below its top ($68.30). Adore Me: about $552M of cash over fiscal 2022 to 2025 (purchase price plus
deferred and contingent consideration), followed by a $120M impairment of its long-lived assets and a $36M restructuring
of its fulfilment in fiscal 2025 (Item 7). No dividend has been paid since the spin (Item 5).

**Bearing on Q9 (debt and exposures).** Debt $975M; ABL commitments $750M, availability $589M at 2026-01-31; ratings Ba3
and BB- (Item 7). Pre-tax income plus interest over interest: 2.5 times (fiscal 2023), 3.6 (2024), 4.0 (2025). Lease
obligations $2,452M and purchase obligations $877M (contractual obligations table). The ABL's maturity springs to 91 days
before any large debt maturity if availability and covenant tests are not met (Item 7), which would pull it ahead of the
term loan of August 2028.

**Bearing on Q12.** The filer reports compliance protocols for model engagement and photo shoots, with monitors at every
shoot (Item 1, Human Capital); recorded only.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Commits: template copy; Step 0 to the standing rule; Q1; the computation and the facts; the audit.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not written
      by this analyst, by the brief); the fold is the dispatcher's. Not yet in the register: binds nothing until folded.
- [ ] The blind rule: **one breach declared**. Before the template was copied, a filtered listing of `Test Runs/` for
      this company's names was run (no result). Declared under Contamination at the top; nothing seen, nothing used. No
      other run file, holding review or `PORTFOLIO.md` was opened.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; every quoted fragment beside an id is in that row
      (`check_citations.py` in the research folder, PASS); every filing fact has its accession.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance; the figures after it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less SBC less all capital spending), never a net-income proxy; the sovereign
      from the U.S. Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written as found (foundations); the facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the last commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a fashion business.** Q1's routing sends a business whose ten-year economics cannot be foreseen
"because its industry changes fast" to TOO HARD, and its rows and examples are about technology; the customer form
(**[M2017-019]**, **[M2023-030]**) says consumer behaviour can sometimes be projected. The text does not say whether a
fashion cycle is the fast change Q1 means. I closed at Q1 on the filer's own words and the record. A second analyst could
pass Q1 and close at Q2 OUT under "the standing castle that protects only ordinary returns" (VS&Co 4% to 5% against the
rivals' 15% to 18%), a different box (OUT, not TOO HARD (NATURE)) on the same facts. The text should say which question
owns a brand whose relevance has swung. (2) **Q7's cycle specific with one cycle on file.** Specific (a) measures growth
"between the averages of successive cycles"; with one full cycle on file the text is silent, and I used (b)'s halves as a
CONVENTION of this run. It is also silent on whether carve-out (combined) statements may sit inside a cycle; I used them,
labelled. (3) **Purchases in the no-growth case.** The 2026-10-10 specific stops purchases after year ten; it does not say
whether the no-growth end deducts them in years one to ten. I deducted none (a business that buys no growth spends nothing
to buy it), which raises the top; deducting the $77M a year would lower the top to $61.02 a share by the same script.
(4) **A consolidated joint venture's minority share** of owner cash has no rule; confessed above. (5) **The template**
still carries a Q7 line "Value range ... IN only if" for a run that closed earlier; the brief's reporting section is what
governs the computation here, and the two agree.
