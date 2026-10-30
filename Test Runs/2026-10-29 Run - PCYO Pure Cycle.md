# Company Run — Pure Cycle Corporation (Nasdaq: PCYO) — 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (2026-10-29), after the run was committed: not held (`PORTFOLIO.md` does not name PCYO or Pure Cycle).

**Dispatch:** a dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's two stated departures (the
repository path, and the lines of evidence left to the analyst). Research folder: `Test Runs/_research 2026-10-29 PCYO/`
(notes, the tool outputs, the computation scripts; raw filings in its ignored `cache/`).

**Contamination, declared.** The session context showed, before any work: recent commit subjects about another company's
run (a different ticker), a modified file in another company's research folder in the working-tree status, and a memory
index line giving general queue and holdings counts. None names this company; none was opened or used. No file under the
blind list was opened, listed or searched. The framework, the template, the protocol and the ledger were the only
repository files read besides my own folder and the tools.

**Lines of evidence chosen, and why.** From the FY2025 10-K: Item 1 for the three segments and the contracts that make the
water business (the Rangeview District service agreements, the Land Board lease, the Sky Ranch CAB funding agreements),
because the castle is in those contracts; Item 1's two competition paragraphs, because they are the filer's own account of
its rivals; Item 1A for what the filer says can break it (competition among developers, the CAB advances, the conflicts of
interest, the Public Utilities Commission, the Land Board); Item 7 for revenue by line, the two critical estimates and the
cash flows; and Note 13 (segments) for the parts table. Then the latest 10-Q for the current balance sheet and the cash
burn since, the proxy for ownership and pay, and the 8-Ks of 2026 for the board changes. Ten balance sheets from the
filed XBRL, checked against the filed statements for FY2021, FY2023, FY2025 and May 2026.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $10.65 (close 2026-10-28; `tools/run.py`'s live quote, an aggregator, flagged per operator rule 5). The company's
  own last open-market buyback, May 2026, averaged $10.65 a share (10-Q, 0001104659-26-081778, Part II Item 2).
- **Shares by class:** one class of common, 24,097,370 shares (10-Q for the quarter ended 2026-05-31, filed 2026-07-08,
  accession `0001104659-26-081778`, cover; the balance sheet at 2026-05-31 shows the same 24,097,370 outstanding; no
  treasury line, repurchased shares are not carried as treasury stock). `python Screens/cover_shares.py PCYO` returns the
  same count. Also outstanding: 432,513 Series B preferred, par $0.001, liquidation preference $432,513 (immaterial).
  After the 10-Q: Forms 3 and 4 of September 2026 for directors (stock grants, small); no 8-K or prospectus issuing shares.
- **Market cap:** 24.097M × $10.65 = **$256.6M**.
- **Sovereign for the earnings currency (USD):** **5.37%**, US Treasury daily par yield curve, 30-year, 2026-10-28
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY ended 2025-08-31, filed 2025-11-12, `0001104659-25-110312` (Items 1, 1A,
  5, 7, 8 with Notes 2, 5, 13, 14); 10-Q for the quarter ended 2026-05-31, filed 2026-07-08, `0001104659-26-081778`; DEF 14A
  filed 2025-12-04, `0001104659-25-118311`; 8-Ks `0001104659-26-004427` (2026-01-14, cooperation agreement with Maran),
  `0001104659-26-082168` (2026-07-07, results, a director's resignation), `0001104659-26-066072` (2026-05-21, the Maran
  director resigns), `0001104659-26-100607` (2026-08-24, two directors appointed); DEFA14A `0001104659-26-092839`
  (2026-08-10, Maran nominates five directors for the 2027 meeting); prior 10-Ks for the span: FY2024
  `0001558370-24-015541`, FY2023 `0001558370-23-019110`, FY2022 `0001558370-22-017799`, FY2021 `0001558370-21-015383`,
  FY2020 `0001140361-20-025088`, FY2019 `0001140361-19-020266`, FY2018 `0001140361-18-042948`, FY2017
  `0001654954-17-010721`. **The FY2026 10-K (year ended 2026-08-31) is not on EDGAR** as of 2026-10-29 (the submissions
  list's latest filing is a Form 4 of 2026-09-23); the 10-Q above is the latest period.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $13,164
  thousand in the filed Consolidated Statements of Cash Flows (10-K `0001104659-25-110312`, F-8), equal to the XBRL value
  `tools/run.py` used ($13.16M). Also equity at 2025-08-31, $142,738 thousand, filed and tagged alike.
- `python tools/run.py PCYO`, arithmetic lines only (output kept in the research folder): OCF FY2023 −2.3, FY2024 2.3,
  FY2025 13.2 ($M); SBC 0.5, 0.4, 0.3; D&A 2.2, 2.1, 2.3. **The tool's capex line is wrong for this company and is not
  used:** it took only "PaymentsToAcquireOtherPropertyPlantAndEquipment" (0.4, 0.5, 0.9), while the filed investing section
  carries four spending lines (property and equipment, future land development, single-family rentals, water and
  wastewater infrastructure: FY2025 $0.9M + $0.9M − $0.5M + $8.6M). Owner cash is recomputed from the filed statements at
  Q7 below. SBC resolved: the only stock-pay line is "Share-based compensation expense"; no other was found.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**; here that
means owning a stake in one Colorado master-planned community, a water-rights portfolio carried at cost, and a loan book
to a metropolitan district, with no quotation to steer by. The market serves and does not instruct: the price of $10.65
carries no information about the water's value, and the run treats it so. Who is paid to tell you: the company's own
narrative ("valuable water rights", "attractive recurring monthly income", Item 1) and an activist holder's campaign
(Maran, 14.7%, five nominees) are both interested parties; neither is used as evidence. The analyst's habits: look for
"what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the company
has exclusive, long-dated water and wastewater service rights (Lowry Ranch to 2081; Sky Ranch; Wild Pointe) and an owned
water portfolio the filer sizes at about 60,000 single-family equivalents against about 1,600 connected (10-K Item 1); that
is a real franchise and the strongest fact for the name. (2) On its own capital at historical cost, the land segment
earns a high margin during the build-out (FY2025 segment profit $10.2M on $15.3M revenue, Note 13). (3) Since FY2019 the
company has been profitable every year after four decades of losses. Each is weighed where it bears, below.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if bought with the buyer's own money and sized so a total loss is
bearable: "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**;
borrowed money to own it is ruled out, "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in
the target forces the buyer's hand. Satisfied as a matter of the buyer's conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10 years"
  **[M2000-037]**, "what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**.
- **What the business is, from the 10-K (`0001104659-25-110312`, Item 1, Note 13).** Three segments: (i) wholesale water
  and wastewater services, provided by contract to the Rangeview Metropolitan District (the largest customer), which serves
  the end users; revenue from tap (connection) fees paid by homebuilders at building permit, monthly usage fees (the company
  keeps 98% of water usage and 90% of wastewater fees), and water sold to oil and gas operators for hydraulic fracturing,
  which the filer calls "unpredictable" and says can "fluctuate dramatically"; (ii) land development at Sky Ranch, a
  930-acre community bought in 2010, zoned for up to 3,200 homes, 1,169 finished lots delivered to national homebuilders by
  2025-08-31, full development "another eight to ten years depending on market conditions"; the company also advances the
  cost of the community's public improvements to the Sky Ranch Community Authority Board (CAB), repaid from property taxes,
  fees and municipal bonds; (iii) single-family homes built for rent at Sky Ranch (14 homes at FY2025; $14.6M of rental
  units on the balance sheet at 2026-05-31). Oil and gas royalties from wells under Sky Ranch ($6.7M in FY2025, $0.8M in
  FY2024) are reported outside the segments as passive.
- **Is it a regulated utility in Q7's sense?** No. The filer: "We do not believe that we are a public utility under
  Colorado law"; it serves by contract a quasi-municipal district, not the public; no regulator sets a return on invested
  capital. Lowry Ranch rates and tap fees are capped by the Land Board lease at "the average of the rates of three nearby
  water providers", and the Rangeview District (whose board is the company's CEO, three employees and one independent
  member) sets them annually (Item 1, Item 1A). A contractual cap with no allowed return is not "an allowed return"; the
  utility paragraph of Q7 does not apply, and the deciding part (Q2) is land development in any case.
- **Key variables and how predictable** **[M1998-044]**: lots delivered and taps sold a year at Sky Ranch (the Denver
  entry-level housing cycle; contracted by phase with national builders, Phase 2E's 148 lots under contract for FY2027);
  the tap fee (about $40,000 a Sky Ranch tap in FY2025, $38,000 in FY2024, Item 7); the development cost per lot; the CAB's
  capacity to repay ($43.8M owed at FY2025; $59.1M of related-party notes at 2026-05-31); frac-water sales; royalties.
  The first three are cyclical but bounded and visible: the community is zoned, phased and partly contracted, and the filer
  gives its own horizon. The last two are unpredictable but small beside the first.
- **Do the past statements tell me the future ones** **[M2008-033]**? Over a cycle, yes, roughly: revenue is lots plus
  taps plus usage, and the 10-K discloses each by phase. Year to year, no: revenue $20.4M, $25.9M, $17.1M, $23.0M, $14.6M,
  $28.7M, $26.1M (FY2019 to FY2025) and operating cash swings with CAB bond issues.
- **Where it will be in ten years.** Sky Ranch largely built out on the filer's own schedule; the company then a water and
  wastewater operator for the community's few thousand connections plus the rentals, with any further land development
  depending on land not yet bought ("we continue to source additional land acquisitions", Item 1) and on Lowry Ranch, whose
  development "is not within our control" (Item 1A). The first is an understandable residual; the second and third are
  options, not the base, and are treated so.
- **Routing.** Not a start-up **[L2007-015]**: revenue-producing since FY2018 and profitable since FY2019. Not a fast-change
  industry. The CAB note is a loan to a municipal district repaid from property taxes and bonds, with a filed repayment
  record (bond repayments of $10.5M in 2019, $23.6M in 2022, $10.1M in 2024; Item 1); it can be read. Doubt about the
  circle **[M2002-092]**: the economics of lots, taps and water fees are plain; my doubts are about durability and price,
  which are Q2's and Q7's questions, not about understanding.
- **VERDICT: IN.** The ten-year economics of the parts that matter can be pictured from the filings
  **[M2012-065]**, **[M2000-037]**; the unknowable items (new land, Lowry Ranch) are set aside as options, not counted.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table (section B).** Segment profit as Note 13 reports it (revenue less cost of revenue including depreciation;
corporate G&A, royalties and interest excluded), $ thousands, from the 10-Ks of FY2021 (`0001558370-21-015383`, "gross
profit"), FY2023 (`0001558370-23-019110`, FY2023 and FY2022) and FY2025 (`0001104659-25-110312`, FY2025 and FY2024):

| part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Land development (Sky Ranch) | 4,934 | 10,704 | 5,206 | 13,225 | 10,157 | 44,226 | 62% | a finite parcel paired with owned water; a cost edge on lots in a field the filer calls highly competitive | **yes** (more than half) |
| Water and wastewater | 5,789 | 5,611 | 2,742 | 6,241 | 5,553 | 25,936 | 37% | exclusive service contracts and owned water rights | no |
| Single-family rental | n/a | 59 | 92 | 293 | 320 | 764 | 1% | none claimed | no |

The interest on the CAB note ($3.3M in FY2025, reported under corporate) arises from the land business, so land's share is
larger, not smaller, if it is counted. The parts are integrated (the filer: the land business "was borne from our desire to
capitalize on the increase in the value our water can provide to raw land"; lots sold become tap and usage customers), and
the convention reads them apart all the same, "lumping them together [...] impedes analysis" **[L2008-005]**. The file
closes on land development; the water part is read below as well, and the close does not turn on which part decides.

**The castle tests, on the deciding part (land development).** "why is that castle still standing?" **[M1995-038]**
1. *Key factors and how permanent.* The filer's stated edge: owning the water lets it avoid buying "expensive water" or
   paying another provider and "a more efficient development timeline, with more competitive lot pricing" (Item 1);
   Colorado requires a developer to show water supply before zoning (Item 1). The parcel is the castle's limit: Sky Ranch
   builds out in "another eight to ten years" (Item 1). Past that the land part has nothing until new land is bought; none
   has been bought since 2010, fifteen years.
2. *The money test* **[M2011-015]**: could a well-funded developer take it on? The filer answers in its own words:
   "Developing raw land is a highly competitive business [...] There are many developers, as well as properties and
   development projects, in the same geographic area in which Sky Ranch is located" (Item 1, Competition). Water can be had
   elsewhere at a price: "Alternate sources of water are available, principally from other private parties such as farmers
   [...] and from municipalities seeking to annex new development areas" (Item 1). The answer is yes, at a higher cost.
3. *Pricing power and the low bid* **[M2017-009]**: the buyers are national homebuilders; the filer positions Sky Ranch
   on "segment pricing (entry level) lots" (Item 7) and lists among the factors of competition "the cost and value of the
   end product". The edge is passed to the builder as a lower lot price, not banked as a premium. Tap fees rose about 5% in
   FY2025 ($38,000 to $40,000), set by a district the company's officers direct and capped on Lowry Ranch at the
   neighbours' average.
4. *The low-cost position* **[L2004-007]**: real on this parcel, because the water is owned and the land was bought in
   2010. It is a cost position on one inventory, not a process others cannot copy.
5. *Widening or narrowing* **[M1999-108]**: the parcel is consumed by design; each lot sold is castle used up. The filer
   names "Significant competition from other development projects" as a risk (Item 1A).
6. *What could destroy or reduce it*: a Denver housing downturn (FY2023 revenue fell to $14.6M from $23.0M); the CAB's
   ability to repay ($85.6M advanced since inception, $43.8M unpaid at FY2025, "cannot guarantee that repayment", Item 1A);
   the water court (in February 2025 it denied a new 1,635 acre-foot right and a reservoir enlargement, Item 1).

**The water part, read too.** Exclusive service rights on 24,000 acres of Lowry Ranch to 2081, at Sky Ranch and Wild
Pointe; owned rights of 30,602 acre-feet (Item 1). Inside its service areas it has no competitor; outside, "Our principal
competition in areas close to the Lowry Ranch is the city of Aurora" (Item 1). Its weakness is that its volume is not its
own to make: it follows the land part's lots at Sky Ranch, and Lowry Ranch "is not within our control" (Item 1A). It earned
segment profit of $5.2M a year on average (FY2021 to FY2025) on segment assets of $64.6M to $69.4M (Note 13), about 8%
before any corporate cost, and less after.

**The competitor row.** The 10-K names one rival for water, the City of Aurora, a municipality that does not file with the
SEC (flagged), and for land only "many developers", unnamed; it names no rival that files with the SEC. **CONVENTION of this
run:** the comparison set is three SEC-filing land developers that sell lots or master-planned-community land to
homebuilders: Forestar Group (lot developer, CIK 1406587), Five Point Holdings (master-planned communities, CIK 1574197),
The St. Joe Company (Florida land and community developer, CIK 745308); rationale: the deciding part is land development
and these are the listed businesses closest to it in what they sell and to whom. Metric: net income attributable to the
company divided by average equity, each fiscal year, summed over the span (net income summed over average equity summed),
transcribed from the filed 10-Ks' XBRL (script `rivals.py` in the research folder; transcription, the latest 10-Ks read
for the accession only):

| company | span | sum of net income / sum of average equity | range of single years | latest 10-K |
|---|---|---|---|---|
| Pure Cycle (filer) | FY2014 to FY2025 | **4.1%** | −28.7% (FY2015) to 21.8% (FY2021, inflated by a one-time $20.2M recognition, Q4 facts) | `0001104659-25-110312` |
| Pure Cycle, profitable years only | FY2018 to FY2025 | 8.9% | 0.6% to 21.8% | same |
| Forestar Group | 2014 to FY2025 (Sept; the 2018 transition period not tagged as a year) | 7.9% | −35.2% (2015) to 16.2% (FY2022) | `0001628280-25-053125` |
| Five Point Holdings | 2015 to 2025 | 1.1% | −3.6% to 4.3% | `0001574197-26-000005` |
| The St. Joe Company | 2014 to 2025 | 12.8% (2014 includes a large land sale; 2015 to 2025, 8.4%) | −0.2% to 53.1% | `0001104659-26-019676` |

**The field's returns over the last full cycle (section C), judged in words.** The span runs from the tail of the last
land bust (Forestar's 2015 loss, Five Point's losses) through the 2022 to 2023 rate shock and the recovery. Over it the
durable players in this field earned ordinary returns: one about 8%, one about 1%, one about 8% from 2015 (13% with a 2014
year of large land sales). The filer itself earned about 4% over twelve years and about 9% in its eight profitable years, the
best of them including a one-time catch-up and, in FY2025, oil and gas royalties that are not land development at all. On
the capital the business carries (equity of $142.7M at FY2025; the speakers' measure is "the capital actually needed in
the business" **[M2010-090]**, "return on tangible assets" **[M2011-060]**), these are ordinary returns. The moat is what
"protects excellent returns on invested capital" **[L2007-004]**, and none are shown. The contrary evidence (the land
segment's high margin on its 2010-cost land) is the harvest of one parcel bought cheaply, consumed in eight to ten years;
the company-level return on the capital it actually employs, including the CAB loans that the land sales require, is the
ordinary figure above. The water part, read on its own, earns about 8% before corporate cost on its segment assets, also
ordinary, so the close is the same whichever part decides.

**The change for the better.** The company lost money for decades (accumulated deficit $102.3M at FY2016) and has earned
since FY2019. The convention credits such a change only on a full cycle **[M2017-026]**, **[M2005-020]**, **[L1995-022]**;
it is not needed here, because even the improved years are ordinary on the evidence above.

**Why the box is OUT and not TOO HARD.** The tenuous-moat row sends a castle to TOO HARD because "We don’t know how to
valuate that" **[M2000-019]**; that reason does not apply where the returns are known from the filings. A field whose
durable players earn ordinary returns over a full cycle is OUT (Q2, What it rules OUT, the standing castle that protects only
ordinary returns): "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**, and here the
filer says there are "many". The land castle is also one that must be rebuilt with each new parcel, "A moat that must be
continuously rebuilt will eventually be no moat at all." **[L2007-005]**, with no new parcel bought in fifteen years.
- **VERDICT: OUT** **[M2006-013]**. The deciding part, land development at Sky Ranch, is a finite parcel in a field the filer
  calls highly competitive, whose durable players, the filer included, earned ordinary returns over the span read
  **[L2007-004]**, **[M2013-052]**; its edge (owned water, cheap 2010 land) is real and is passed to homebuilders as lower lot
  prices and used up as the lots are sold **[L2007-005]**.

## Q3 — NOT REACHED (closed at Q2).
## Q4 — NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.
## Q5 — NOT REACHED (closed at Q2). Integrity facts found are under AFTER THE STOP.
## Q6 — NOT REACHED (closed at Q2).
## Q7 — NOT REACHED (closed at Q2). The figures below are a COMPUTATION, NOT A CLEARANCE.
## Q8 — NOT REACHED.
## Q9 — NOT REACHED.
## Q10 — NOT REACHED.
## Q12 — NOT REACHED.

---
## THE BOX
**OUT at Q2**: the deciding part (land development, 62% of five-year segment profit) is a finite parcel in a field of
ordinary returns, the filer's own included. COMPUTATION, NOT A CLEARANCE: value range $0.10 to $3.20 a share against
$10.65. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box unchanged, operator rule 2.)*

**Bearing on Q3 (capital).** Five-year spending (FY2021 to FY2025) of $33.5M against depreciation of $10.5M; the
nine months to 2026-05-31 alone spent $19.2M (rentals $9.8M, water infrastructure $5.8M, future land $3.0M) against
operating cash of −$1.7M (10-Q). The filer estimates the full water build-out at "in excess of $900 million" over "many
decades", to be funded, it believes, by tap fees (Item 1). The CAB advances: $85.6M since inception, $23.5M more expected
for Phase 2 (Item 1A).

**Bearing on Q4 (the accounts).** *The balance sheets first, ten year-ends* ($ thousands, XBRL as first filed,
checked to the filed statements at FY2021, FY2023, FY2025 and 2026-05-31):

| year-end | assets | liabilities | equity | cash | receivables | debt | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016-08 | 70,880 | 1,882 | 68,998 | 4,697 | 181 | 0 | −102,283 |
| 2017-08 | 69,788 | 2,281 | 67,506 | 5,576 | 664 | 0 | −103,994 |
| 2018-08 | 71,907 | 2,453 | 69,453 | 11,565 | 1,067 | 0 | −102,524 |
| 2019-08 | 83,721 | 8,990 | 74,731 | 4,478 | 1,100 | 0 | −97,713 |
| 2020-08 | 89,761 | 7,717 | 82,044 | 21,797 | 1,124 | 0 | −90,963 |
| 2021-08 | 117,177 | 14,437 | 102,740 | 20,117 | 1,532 | 0 | −70,853 |
| 2022-08 | 129,229 | 16,233 | 112,996 | 34,894 | 2,425 | 3,960 | −61,234 |
| 2023-08 | 133,216 | 14,982 | 118,234 | 26,012 | 1,092 | 6,916 | −56,535 |
| 2024-08 | 147,354 | 17,652 | 129,702 | 22,113 | 1,472 | 6,885 | −45,503 |
| 2025-08 | 162,279 | 19,541 | 142,738 | 21,931 | 1,330 | 6,791 | −32,790 |
| 2026-05 (10-Q) | 175,978 | 24,394 | 151,584 | 8,440 | 2,486 | 14,123 | −24,372 |

What they say: no goodwill or purchased intangibles in any year; equity rose by $82.6M from 2016 to May 2026, almost all
retained earnings (the deficit fell by $77.9M), little issuance. What they do not say on their face: of the assets, the
related-party notes (the CAB and the Rangeview District) were $45.0M at FY2025 and $59.1M at 2026-05-31, a third of total
assets, collectable only when the CAB raises taxes, fees or bonds; the water system ($72.3M) is carried at cost. Cash fell
from $21.9M to $8.4M in nine months while debt doubled to $14.1M (a single-family rental facility, raised to $20M of
capacity on 2026-06-15, 10-Q Note 14). Restricted cash of $6.2M secures twelve letters of credit for construction
performance (10-K Note 2). What they cannot say: what the water rights would fetch, and whether the CAB will repay before
its 2058 and 2060 discharge dates ("Any advances not paid or reimbursed [...] shall be deemed forever discharged", Item 1).
*"what the figures are saying and what they don’t say"* **[M2025-032]**.

*The income account.* (a) FY2021 net income of $20.1M included $20.2M of "Recognition of public improvement reimbursables
including interest income - related party" (10-K FY2021 `0001558370-21-015383`, statement of operations): costs expensed in
FY2018 to FY2020 (land cost of revenue was $15.9M of $18.9M of lot sales in FY2020) were recognized as a receivable when the
company judged collection probable; the CAB then repaid $23.6M from bonds in August 2022. (b) From FY2021 the land
segment's cost of revenue excludes public improvements, which go to the note receivable; lot revenue is recognized by
percentage of completion with the reimbursable public-improvement costs inside the completion ratio (Item 7, critical
estimates). Construction "in progress or progress payment-type things" is the area the speakers call prone to games
**[M2013-086]**; recorded, not judged. (c) The two critical estimates the filer names are the CAB note's collectability
and the completion ratio; both are judgments made on an entity whose board the company's officers control (below).
(d) Real costs: depreciation and depletion about $2.1M to $2.3M a year; stock pay small ($0.3M to $0.6M).

**Bearing on Q5 (integrity), recorded, not judged.** (1) The company's CEO, CFO and employees are a majority of the boards
of the Rangeview District (its largest customer, which sets the tap fees and rates paid to the company), the Sky Ranch
Districts and the Sky Ranch CAB (the debtor on the related-party notes); the filer names this a risk, "Conflicts of
interest may arise relating to the operation of the Rangeview District, the Sky Ranch Districts and the Sky Ranch CAB"
(Item 1A); the directors forgo the district meeting fees (Item 1). (2) The company judges the collectability of notes owed
to it by a body its officers direct (Note 2). (3) The FY2025 proxy says the compensation committee is "emphasizing an
adjusted return on equity ("ROE") and earnings before interest, tax, depreciation and amortization ("EBITDA")" in judging
executives (DEF 14A `0001104659-25-118311`); the speakers call EBITDA "utter nonsense" **[M1998-086]**; a weighing for Q4
and Q5, recorded only. CEO pay: salary $525,000, discretionary bonus $300,000 (FY2025) and $675,000 (FY2024), 10,000 shares
(proxy). The CEO holds 4.3% including options. (4) A cooperation agreement with Maran Capital (14.7%) on 2026-01-14 put
Maran's principal on the board and created a strategy and capital-allocation committee he chaired; he resigned on
2026-05-21, the other Maran-associated director on 2026-07-07, both "not [...] from any disagreement"; on 2026-08-07 Maran
nominated five directors for the 2027 meeting; two new independent directors were appointed 2026-08-24 (8-Ks and DEFA14A
listed in Step 0). Any later run that reaches Q5 must answer these **[M2013-088]**.

**Bearing on Q6 (the money).** A repurchase programme of 200,000 shares (2022), open-ended, **no stated price**; purchases
of $0.58M (FY2024), $0.40M (FY2025), $0.20M (nine months FY2026), the last 7,500 shares at $10.65 in May 2026 (10-Q).
Against the COMPUTATION below, those prices sit far above the bottom of the range; recorded only. No dividend. No
acquisition of a business; no all-stock deal.

**Bearing on Q9 (exposures).** Debt $14.1M at 2026-05-31, secured, limited-recourse, rates "up to 7.51%" (10-K Item 7);
fixed-price development contracts with performance guarantees and bonds (Item 1A); credit exposure to one municipal
borrower for a third of assets; concentration in one county's housing market.

**COMPUTATION, NOT A CLEARANCE (Q7 as it would be built; the operator's two reporting figures).** Script and output:
`q7_compute.py`, `q7_output.txt` in the research folder. $ thousands, from the filed cash-flow statements.
- *Owner cash after every real cost* = operating cash − stock pay − all investing spending (securities purchases and
  maturities left out, the FY2023 Treasury-bill discount added back as interest, the FY2025 land sale of $179 netted). The
  CAB advances and repayments sit inside operating cash and are counted as working capital (specific (d)):
  FY2021 63; FY2022 10,183; FY2023 −12,119; FY2024 −2,953; FY2025 3,189; **five-year average −327** (equity-only), −173 before
  interest (all-equity; interest paid added back after tax at 25%, **CONVENTION of this run**: federal 21% plus Colorado
  4.4%, rounded; the filer's effective rate was about 25%).
- *Maintenance-only (specific (e), central where the filing allows the guess)*: the filing separates spending into water
  infrastructure, rentals and future land phases, all for growth by the filer's own description ("to provide water and
  wastewater services to our growing number of customers", Item 1), so the maintenance guess is depreciation and depletion
  **[L2015-004]**: FY2021 1,187; FY2022 14,726; FY2023 −4,778; FY2024 −224; FY2025 10,544; **average 4,291** equity-only,
  **4,445** all-equity. Growth spending above the guess: 4,618 a year on average.
- *Growth shown*: the series changes sign, so growth is measured between the halves of the window (specific (b)):
  FY2021 to FY2022 average 7,956, FY2024 to FY2025 average 5,160, **−13.4% a year**: a decline, carried as the bottom; the
  no-growth case is the top. Sales grew 11.1% a year FY2021 to FY2025 (shown beside, not a case). The end years: FY2025
  carries $6.7M of royalties against $0.8M the year before and a $10.1M CAB bond repayment; the filer does not call either
  aberrational, so the literal window stands.
- *Net debt* at 2026-05-31: debt $1,454 + $12,669 less cash $8,440 = **$5,683** (restricted cash $6,193 left out as
  collateral; leases nil; the June 2026 facility increase is capacity, not a draw).
- **(a) VALUE RANGE, all-equity, at the sovereign 5.37%, ten years then zero nominal growth: $0.10 to $3.20 a share**
  (bottom: maintenance-only at −13.4% with the growth spending charged, $4,618 in year one, $1,260 in year ten, none after,
  as specific (e) reads; top: maintenance-only at no growth). Equity-only beside: $0.29 to $3.32. All-spending case beside:
  negative ($−0.37). Against **$10.65**. The width is far over three to one, but the floor is tested first: **no case earns
  about ten percent at $10.65**; the top case at the sovereign is 30% of the price; the maintenance-only owner cash is
  1.7% of enterprise value; earning the floor at no growth would need about $26.2M a year of owner cash against $4.4M
  shown. Even carried at the 11.1% sales growth for ten years (not a case of the convention) the figure is $8.09 at the
  sovereign. Were Q7 reached it would close OUT on the floor **[M2003-149]**.
- **(b) FAIR PRICE (Part VII; each end valued at ten percent, the two averaged; after the company's own tax): $0.71 a
  share on the all-equity basis (central); $0.90 equity-only (beside).** Not a regulated utility, so no debt credit. There
  is no cheap price.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch (yes: the first commit, with the framework notes, came before the first
      EDGAR call). **Not kept: written question by question with a commit after each.** The research for Step 0, Q1 and Q2
      was done first and the sections from Step 0 to the facts after the stop were written in one pass and committed
      together; the research folder held the working notes and outputs throughout. A violation of the write-early rule,
      declared here (operator rule 6).
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's (not checked here, by the
      brief); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_ids.py` (research folder); every quoted fragment
      beside an id found in that row; no E-ids; every filing fact carries its accession.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; nothing after it is a clearance; the figures after it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; `tools/run.py`'s
      capex line found incomplete and replaced; sovereign from the Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations paragraph, Q2's water part and land margin).
- [x] No row dated after the anchor cited (not a point-in-time run; today's run).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS (2026-10-29, before the commit of this file); `check_ids.py`: 33 ids, 0 problems.
- Weak points, said plainly: the competitor set is my choice (CONVENTION above) and the metric is transcribed XBRL, not read
  from each rival's statements; the parts are integrated and the segment split is the filer's; the window's owner cash is
  dominated by CAB bond timing, so any five-year figure for this company is rough.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The business of parts on an integrated business.** The convention reads land and water apart, but here the land part
exists to sell water taps (the tap fees are booked in the water segment) and the land castle is the water; which part
"decides" is an artefact of where the filer books revenue. I read both, and both gave ordinary returns, so the box did not
turn on it; a case where they diverge would need a rule. (2) **A liquidating parcel.** Q2 asks what keeps the castle standing
ten to twenty years, and Q7 carries five-year cash ten years and then forever; neither speaks to a business whose main
inventory is consumed by design within the ten years (Sky Ranch, eight to ten years left). I treated the build-out as the
castle's limit at Q2; at Q7 the convention carries the window forward as if the parcel renewed, which overstates the top.
(3) **Specific (e) with a negative shown growth.** The text grows the growth spending "at the growth rate carried" and
stops it at year ten, but does not say whether spending above maintenance is charged in a case where the window shows
decline; I charged it (bottom $0.10) and showed the uncharged decline beside in the script ($0.97). (4) **A related-party
loan book inside operating cash.** The CAB advances are part loan (6% interest, repaid from bonds) and part cost of selling
lots; Q7's parenthesis on debt "dedicated to [...] lending" (the regulated-utility paragraph) leaves a lending book
undecided, and specific (d) counts working capital. I counted the advances as working capital inside operating cash, which
makes owner cash swing with the district's bond issues. (5) **The template's tool line.** `tools/run.py` took one capex tag
and missed three of the four filed spending lines; the template trusts its "capex" line, and a run that did not read the
investing section would have overstated owner cash fourfold.
