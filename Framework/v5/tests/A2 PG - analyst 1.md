# A2 PG - analyst 1
**The Procter & Gamble Company (NYSE: PG), CIK 0000080424. Run under `Framework/v5/DRAFT - THE FRAMEWORK v5.md` (as corrected 2026-10-05) and `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`. Re-test of reproducibility after the correction pass, analyst 1. Run date 2026-10-04. Binds nothing; no position is taken or recommended.**

Working files (fetched filings converted to text, arithmetic script and its output): `Framework/v5/tests/_work_A2r1_PG/`.

---

## 0. Step 0

| Item | Value | Source |
|---|---|---|
| Price | **$144.91**, close of 2026-10-02 | `tools/sources.py` `price('PG')`, an aggregator quote, **FLAGGED: aggregator, live quote only** |
| Share count, cover | **2,324,433,060** common, single class | FY2026 Form 10-K cover, filed 2026-08-04, accession **0000080424-26-000103**, via `Screens/cover_shares.py PG` (cover count as of 2026-07-31) |
| Diluted weighted shares, FY2026 | **2,422.5M** (basic 2,333.7M, options and unvested awards 20.5M, convertible Class A preferred 68.3M) | same 10-K, Note on earnings per share (accession 0000080424-26-000103) |
| Market cap, cover basis | $144.91 x 2,324.4M = **$336.8B** | arithmetic line of `tools/run.py PG` |
| Market cap, diluted basis | $144.91 x 2,422.5M = **$351.0B** | my arithmetic on the filed diluted count. Used at Q7 because the owner cash below is the whole company's, and the ESOP convertible preferred has a claim on it (preferred dividends $292M in FY2026, same 10-K) |
| Sovereign, earnings currency USD | **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026 | issuing authority, as given in the task and as printed on the arithmetic line of `tools/run.py PG` |

Per Part VII of the draft, only the arithmetic lines of `tools/run.py PG` were read (price, shares, market cap, sovereign, and the filed OCF, SBC, D&A and capex columns). Its v4 ids, its v4 floor line and its "still owed" list were not used. Cross-check of one figure against the filed statement: run.py's FY2026 operating cash flow of 19,556 equals "TOTAL OPERATING ACTIVITIES | 19,556" in the Consolidated Statements of Cash Flows of the FY2026 10-K (accession 0000080424-26-000103); capex 4,409, SBC 524 and D&A 3,160 also match the same statement.

Filings read for this run:
- FY2026 Form 10-K, period 2026-06-30, filed 2026-08-04, accession **0000080424-26-000103** (Item 1, Item 1A, Item 5, MD&A, statements, Notes 1, 3, 4, 8 and EPS).
- FY2025 Form 10-K, filed 2025-08-04, accession **0000080424-25-000076** (net sales drivers table).
- FY2024 Form 10-K, filed 2024-08-05, accession **0000080424-24-000083** (FY2022 to FY2024 cash flows, earnings, drivers).
- FY2023 Form 10-K, filed 2023-08-04, accession **0000080424-23-000073** (net sales drivers table).
- FY2022 Form 10-K, filed 2022-08-05, accession **0000080424-22-000064** (FY2020 to FY2022 cash flows, earnings, drivers).
- 2026 DEF 14A, filed 2026-08-28, accession **0001193125-26-372211** (CD&A, board leadership, ownership rules).
- Competitors: Kimberly-Clark FY2025 Form 10-K, filed 2026-02-12, accession **0001628280-26-007567**; Colgate-Palmolive FY2025 Form 10-K, filed 2026-02-23, accession **0000021665-26-000006**.

---

## 1. The foundations

The foundation that bears hardest is **a share is a business**: the question is whether I would be content to own Tide, Pampers and Gillette if the market closed for five years **[M1997-109]**, judged on the business and not the quote. **The market serves, it does not instruct** **[M2006-077]**: the price is read only against where the facts lead. **Margin of safety** **[M1996-084]** governs Q7: a decision that needs a pencil is too close. **No macro forecast enters** **[M2000-094]**: the 10-K's pages on tariffs, the Middle East, currencies and Russia (FY2026 10-K, Item 1A and MD&A "Economic Conditions and Uncertainties", accession 0000080424-26-000103) are read as properties of the business (more than half of sales outside the U.S., pricing to offset inflation), never as a forecast. **Who is paid to tell you** bears on the tooling: `tools/run.py` prints a v4 floor and v4 ids, and the draft's Part VII bars them; the 10-K's own "Core EPS" and "adjusted free cash flow" are management's chosen numbers and are rebuilt from GAAP lines below. The index fork **[M2008-055]** is not decided by a single run. The analyst's habits: the falsifier CONVENTION (section II) applies "before any purchase"; none is made here, so it is noted below at the box and not required.

## 2. The standing rule

Owning PG bought for cash, unlevered, with no collateral or calls attached, does not put the buyer at risk of ruin; the rule binds the buyer's financing, which no position here involves: borrowed money "has no place in the investor's tool kit" **[L2014-005]**; **[M2012-081]**, **[L2014-024]**. Nothing about this target changes that.

---

## 3. The questions in order

### Q1. CAN I UNDERSTAND IT? STOP.

**The test as the draft states it:** "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; "a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]**; the key variables and how predictable they are **[M1998-044]**; whether the forecast is about customers or technology **[M2017-019]**, **[M2023-030]**; doubt means outside **[M2002-092]**.

**Applied to the filings.**
- What it sells: "a diversified portfolio of daily-use products" in five segments: Fabric & Home Care 35% of net sales, Baby, Feminine & Family Care 24%, Beauty 19%, Health Care 14%, Grooming 8% (FY2026 10-K, Item 1 and MD&A segment table, accession 0000080424-26-000103). These are laundry detergent, diapers, razors, toothpaste, paper towels: the same categories ten years ago and, on the evidence of daily use, ten years out.
- Key variables: unit volume, price, and share by category. The filing states them itself: the net sales drivers table splits every year into volume, foreign exchange, price and mix (FY2026 10-K MD&A, accession 0000080424-26-000103), and management "uses unit volume growth to evaluate drivers of changes in net sales" and market share "to evaluate performance relative to competition" (same).
- Do past statements tell me future ones **[M2008-033]**? Five years of statements (FY2022 to FY2026, accessions 0000080424-22-000064, -24-000083, -26-000103) show net sales $80.2B, $82.0B, $84.0B, $84.3B, $87.0B and operating cash flow $16.7B to $19.8B: a slow, stable series.
- Customers or technology: the changes the 10-K names are in how products reach the customer ("social media platforms, streaming services or AI based search", retailers "building their own media platforms", "growth in hard discounter channels"; FY2026 10-K, MD&A Strategic Focus and Item 1A). These are channel changes in a consumer business **[M2017-019]**, not a technology that turns the product over.
- The row that names the company: "it’s much easier to come to a conclusion on something like Coca-Cola or Procter & Gamble" **[M2009-060]**.

**Verdict: IN.** I can state the ten-year economics in two variables (volume and price within categories it leads) from the filings, and I have no doubt the categories exist and are bought daily in ten years **[M2012-065]**, **[M2002-092]**. Not a bank, not a holding company; the routing to Q2 is clean **[M1998-008]**.

### Q2. WHY IS THE CASTLE STILL STANDING? STOP.

**The test as the draft states it:** "why is that castle still standing? And what’s going to keep it standing [...] five, 10, 20 years from now" **[M1995-038]**; the money test **[M2011-015]**; pricing power **[M2005-019]**, **[M2000-031]**; brand asked for by name and the brand against the retailer **[M2023-073]**, **[M2001-090]**, **[M2019-041]**; ask the competitors; widening or narrowing **[M1999-108]**, **[L2005-010]**. A castle shown filling in is OUT; one whose future cannot be judged is TOO HARD **[M2000-019]**.

**Applied to the filings.**
1. **The castle questions** **[M1995-038]**. Brand, scale and distribution **[L1993-021]**. Filed shares (FY2026 10-K, MD&A "Organization Design", accession 0000080424-26-000103): grooming "more than 50% share", blades and razors "more than 60%"; fabric care "over 35%"; baby care "more than 30%"; feminine care "nearly 30%"; oral care "nearly 30%"; hair care "about 20%"; Bounty "nearly 40%" of North America.
2. **Without the lord** **[L2007-006]**, **[M1996-037]**. The CEO changed on 2026-01-01 and four of five sector CEOs changed in FY2026 (DEF 14A, "Leadership Changes", accession 0001193125-26-372211; FY2026 10-K executive officers). The business ran through it; no row-sized dependence on one person appears.
3. **Pricing power** **[M2005-019]**, **[M2000-031]**. Total-company price contribution by year, from the net sales drivers tables: FY2022 +4%, FY2023 +9%, FY2024 +4%, FY2025 +1%, FY2026 +1%, against unit volume +2%, (3)%, 0%, 0% (+1% excluding divestitures), 0% (FY2022 10-K 0000080424-22-000064; FY2023 10-K 0000080424-23-000073; FY2024 10-K 0000080424-24-000083; FY2025 10-K 0000080424-25-000076; FY2026 10-K 0000080424-26-000103). A 9% price rise in FY2023 cost three points of volume, and volume then held flat: sales did not "fall off a cliff" **[M2005-019]**. That is charging more and holding the business **[M2000-031]**.
4. **The brand against the retailer** **[M2001-090]**, **[M2019-041]**, **[M2006-091]**. Walmart is "approximately 16% of our total sales in 2026, 2025 and 2024"; top ten customers about 43% (FY2026 10-K, Item 1). The 10-K names "retailers' private-label brands" as competitors. This is the Kraft Heinz exposure the rows narrate **[M2019-041]**: real, carried into "how sure" at Q7.
5. **Ask the competitors: a same-metric comparison from their own filings.**

| Metric (GAAP, latest fiscal year) | P&G FY2026 | Kimberly-Clark FY2025 | Colgate-Palmolive FY2025 |
|---|---|---|---|
| Gross margin | 50.2% | 36.0% (gross profit 5,923 / net sales 16,447) | 60.1% |
| Operating margin | 22.7% | 14.3% (operating profit 2,351 / 16,447) | 16.2% |
| Volume / price | volume 0%, price +1% | volume +2.5%, net price (0.9)% | volume (0.4)%, net price +2.1% |
| Source | 10-K 0000080424-26-000103, MD&A | 10-K 0001628280-26-007567, MD&A "Summary of Results" and net sales drivers | 10-K 0000021665-26-000006, MD&A |

Against Kimberly-Clark, its direct rival in diapers, tissue and towels, P&G earns 14 points more gross margin and 8 more operating margin on the same GAAP lines. Against Colgate, the leader in toothpaste ("41.3%" global toothpaste share, Colgate 10-K), P&G's gross margin is lower and its operating margin higher. Kimberly-Clark's 2025 volume gain came with lower prices, while P&G reported North America baby care and family care volume down "due to competitive activity" and North America family care share down 0.7 points (FY2026 10-K, BFFC segment). One competitor buying volume with price in one segment is a pressure, not a breach **[M2012-108]** read as a warning.
6. **The money test** **[M2011-015]**, **[M1997-103]**. Could a well-funded attacker displace Tide or Pampers? The best-funded attackers are already in the field (Kimberly-Clark, Colgate, Unilever, the retailers' own labels) and P&G still holds the shares above with margins above theirs. The one breach on the record is grooming: Grooming goodwill is "net of $7.9 billion accumulated impairment losses" and the Gillette indefinite-lived brand took a further $1.3B impairment in FY2024 (FY2026 10-K, Note 4). Grooming is 8% of sales and still over 60% of blades.
7. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. FY2026 global share by segment: Beauty (0.3), Grooming (0.4), Health Care +0.4, Fabric & Home Care unchanged (fabric (0.4), home +0.3), BFFC (0.2) (FY2026 10-K, segment results). Mixed, slightly down in the year. The speakers' own reading of this industry: the packaged goods businesses: "they’re all weaker than they used to be at their peak" **[M2016-080]**, said as a reason not to sell on every small loss of advantage.
8. **What could destroy it, five to fifteen years out** **[M2000-014]**. Retailer power and private label **[M2001-090]**; channel change to online and hard discount (10-K Item 1A). Neither is shown to be filling the moat in on the filed evidence; both narrow it at the edge.

**Verdict: IN.** The castle stands: price was taken without losing volume **[M2000-031]**, shares lead in most categories it enters, and its margins exceed a direct competitor's on the same GAAP lines **[M1995-038]**. It is not shown filling in (that would be OUT **[M2011-015]**) and its future can be judged (so not TOO HARD **[M2000-019]**). The narrowing signs (FY2026 shares, retailer concentration, grooming) are carried to Q7's "how sure" **[M1999-104]**.

### Q3. HOW MUCH CAPITAL MUST GO IN? WEIGHING.

**The test:** returns on the capital the business needs **[M2010-090]**, **[M2011-060]**; what must go back to stand still and to grow **[L1999-024]**, **[M2000-144]**; the grade of business **[M1998-081]**.

**Applied.** Net tangible operating capital at 2026-06-30, from the balance sheet (FY2026 10-K, accession 0000080424-26-000103): PP&E 25,360 + inventories 8,170 + receivables 6,056 + prepaid 2,040 + other noncurrent assets 12,231, less accounts payable 16,306, accrued 11,091 and other noncurrent liabilities 4,914 = **about $21.5B** (cash, goodwill and intangibles excluded). FY2026 operating income 19,748 on that is a pre-tax return near 90%, the order of magnitude being the point, not the decimal **[M2011-060]**. What goes back in: capex exceeded depreciation every year, FY2022 to FY2026 (capex 3,156 / 3,062 / 3,322 / 3,773 / 4,409; depreciation, D&A less intangible amortization, about 2,495 / 2,387 / 2,558 / 2,527 / 2,852), while unit volume was flat over the span (Q2 point 3). With volume flat, I take the whole capex as the cost of standing still, the conservative guess **[M2000-144]**, **[L2000-035]**. The company itself says adjusted free cash flow is "after taking into account planned maintenance and asset expansion" and does not split the two (FY2026 10-K, non-GAAP measures). The money that came out: dividends plus buybacks over FY2022 to FY2026 were 47,185 + 33,890 = $81.1B against net earnings of $76.7B (cash flow statements and income statements, accessions 0000080424-22-000064, -24-000083, -26-000103): it pays out more than it earns, so little capital is retained to judge.

**Verdict: WEIGHS FOR.** A very high return on the tangible capital the business needs, with little added capital required, is the first grade of **[M1998-081]**; the growth it buys is slow, so it is "more and more money" only in nominal terms.

### Q4. DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion, otherwise WEIGHING.

**The test:** recast to earnings after every real cost **[L2021-003]**: depreciation **[L2015-004]**, stock pay **[L2015-003]**, recurring restructuring **[L2016-007]**; the tells **[M1995-064]**, **[L2016-006]**, **[L2002-041]**; confusion or suspicion is a STOP **[M1995-063]**, **[M2003-029]**; the two-tell CONVENTION for the make-the-numbers habit.

**Applied.**
- The cash statements are plain: OCF, capex, dividends, buybacks and debt flows reconcile year to year (FY2026 10-K cash flow statement). Adjusted free cash flow is reconciled line by line to OCF less capex, the only adjustment being the 2017 transition tax payments (688 in FY2026), "Adjusted Free Cash Flow | 15,835" (FY2026 10-K, non-GAAP measures).
- Real costs: stock pay $524M is added back in OCF and I subtract it **[L2015-003]**; capex exceeds depreciation so I subtract full capex, not depreciation **[L2015-004]**, **[M1998-127]**; cash restructuring is already inside OCF, so the owner cash carries it **[L2016-007]**.
- Tell one, adjusted earnings featured **[L2016-006]**: "Core EPS" excludes "incremental restructuring", which ran three years in a row (after tax $1.2B over the FY2024 program, $801M in FY2025, $903M in FY2026; FY2026 10-K, Note 3 and Core reconciliation). The ongoing $250 to $500M a year stays in Core, which is to its credit; the incremental layer has become recurring and is waved away.
- The make-the-numbers habit **[L2002-041]**, **[L2019-006]**: the company gives guidance ("0-4% Organic Sales Growth, 0-4% Core EPS Growth") and ties pay to it ("The Core EPS Growth target for year one of the PSP program is typically linked to the external financial guidance"; DEF 14A, accession 0001193125-26-372211). But the record is not one of always making it: the FY2026 bonus paid "approximately 60% of target", and the ten-year ranges are "55-184%" for the annual bonus and "39%-200%" for the PSP (same proxy). So the habit of making targets is not shown; under the two-tell CONVENTION the STOP is not triggered.
- Pension assumptions **[L2002-039]**: the retiree-health (OPRB) plan assumes an 8.5% return on assets that are mainly the company's own ESOP preferred stock (FY2026 10-K, Note 8). It moves GAAP expense, not the cash used here.

**Verdict: no STOP (not confused, not suspicious); WEIGHS FOR.** The owner cash can be built from GAAP cash lines with every real cost in **[L2021-003]**; the featured Core EPS and the recurring "incremental" restructuring are recorded against and carried to Q6 Part B **[L2016-006]**.

### Q5. WHO RUNS IT? STOP on integrity, WEIGHING on ability.

**The test:** the two yardsticks **[M1994-008]**; the proxy, how they treat themselves against the owners **[M1994-009]**; integrity is absolute and applied on doubt **[M2013-088]**, **[M2015-047]**; for a marketable stock the speakers read rather than meet **[M2007-081]**.

**Applied.** The proxy (accession 0001193125-26-372211): CEO salary $1,600,000; long-term award $14,000,000; annual bonus about 60% of target; CEO must own stock worth eight times salary; directors six times retainer; hedging and pledging prohibited. No tell from the list in the draft appears in the filings read: no too-good-to-be-true claims, the 10-K reports share losses by category and region and attributes several "due to competitive activity" (FY2026 10-K segment results), and the accounts are not obscured (Q4). The record against the hand dealt: price taken through the FY2022 to FY2024 cost inflation with volume broadly held (Q2), then organic growth slowing to 4%, 2% and 1% in FY2024, FY2025 and FY2026 (10-Ks 0000080424-24-000083, -25-000076, -26-000103). The new CEO was COO from 2021 to 2025 (DEF 14A), so the slowing record is partly his.

**Verdict: IN on integrity** (no doubt found **[M2013-088]**). **Ability: UNDECIDED**, one sentence: a long in-company record and a business that needs little management **[M1996-037]** sit against three years of slowing organic growth under the same team, and a CEO six months in cannot yet be read on his own record **[M1994-008]**.

### Q6. WHAT WILL THEY DO WITH THE MONEY AND WITH THE OWNERS? WEIGHING.

**Part A, the money.**
- Retention **[M1998-110]**, **[R1995-009]**, **[M2004-089]**: the company pays out more than it earns (Q3), which is what the rows ask of a business that cannot use its earnings at more than a dollar per dollar **[M2004-089]**. Dividends: "increased its dividend for 70 consecutive years" (FY2026 10-K, Item 5); the policy is clear and consistent **[L2012-015]**.
- Buybacks **[L1999-023]**, **[L2016-002]**, **[M2016-049]**: the programme is a fixed sum named without a price, "expected to reduce outstanding shares through direct share repurchases at a value of approximately $5 billion in fiscal year 2026", "financed through a combination of operating cash flows and issuance of debt" (FY2026 10-K, Item 5). That is nearly word for word the case in **[M2016-049]**: "we’re going to spend $5 billion this year buying a business, we don’t care what the price is." The 10-K also states the motive the same row rejects: "we have historically made adequate discretionary purchases [...] to offset the impacts of such activity" (dilution from options; FY2026 10-K, Note on stock plans), against "It’s got nothing to do with preventing dilution" **[M2016-049]**, **[M2014-008]**. The draft's CONVENTION reads the prices paid against the bottom of the Q7 range; Q7 comes later in the order, so that check is recorded at Q7 below, and this verdict does not wait on it.
- Deals **[L2009-019]**, **[L2014-012]**: the pending Thorne acquisition is "$3.8 billion" (FY2026 10-K, Recent Developments), not paid in stock, so the one STOP in Part A does not apply. The Gillette brand and Grooming goodwill impairments (Q2) are the record of an earlier stock deal that gave more than it got **[L2014-012]**; that management is long gone.

**Part B, pay, board, owners.**
- Pay on adjusted measures and on guidance: STAR and PSP pay on organic sales growth, Core EPS growth and adjusted free cash flow productivity, with year-one Core EPS tied to "external financial guidance" (DEF 14A). The rows read guidance and hitting the number as a scourge **[L2019-006]**, **[M2022-054]**; Core EPS leaves out a restructuring cost that recurs **[L2016-007]**.
- Options at market price with no step-up for retained earnings: "stock options are granted at an exercise price at or above the closing market price" (DEF 14A), the flaw named in **[L1994-021]**, **[M1997-043]**; mitigated in part by the 87% performance-based mix and the ownership rules.
- The board: the chair and CEO roles were recombined on 2026-08-01 with a lead director (DEF 14A, Board leadership); the rows note how hard it is to replace a mediocre CEO "if that person is also Chairman" **[L2014-026]**. Not a finding about this CEO.

**Verdict: WEIGHS AGAINST.** A dividend policy the rows approve is outweighed by a fixed-sum buyback named without a price and justified by dilution **[M2016-049]**, and by pay tied to guidance and to an adjusted EPS that drops a recurring cost **[L2019-006]**, **[L2016-007]**.

### Q7. WHAT IS IT WORTH? STOP.

Q1 and Q2 are IN, Q5 is IN on integrity, Q3, Q4 and Q6 are weighed; the value may now be computed.

**How much cash** **[R1996-018]**, **[M1998-080]**. Owner cash per year = OCF less stock pay less all capex (Q4), from the filed cash flow statements (accessions 0000080424-24-000083 for FY2022 to FY2024; 0000080424-26-000103 for FY2025 and FY2026):

| FY | OCF | SBC | Capex | Owner cash |
|---|---|---|---|---|
| 2022 | 16,723 | 528 | 3,156 | 13,039 |
| 2023 | 16,848 | 545 | 3,062 | 13,241 |
| 2024 | 19,846 | 562 | 3,322 | 15,962 |
| 2025 | 17,817 | 476 | 3,773 | 13,568 |
| 2026 | 19,556 | 524 | 4,409 | 14,623 |
| **five-year average** | | | | **14,087** ($M) |

The five-year average is the CONVENTION's base, so no single year sets it **[L2005-003]**. (Using depreciation in place of capex would give about 15,067; not used, since capex has exceeded depreciation every year with flat volume.)

**Growth shown.** Owner cash FY2022 to FY2026: 13,039 to 14,623, **2.9% a year** at the endpoints; 2.4% a year comparing the first two years' average to the last two. Net sales FY2021 to FY2026: 76,118 to 87,032, 2.7% a year (FY2022 and FY2026 10-Ks). Almost all of it is price, not volume (Q2 point 3). Capped by Q3's arithmetic: 2.9% is far below the 5.63% rate and traces to no absurdity **[M1997-095]**, **[M1999-067]**. Per-share growth (about 4.1% a year, helped by buybacks) is not used, since the buybacks are paid out of the same owner cash.

**How soon, at the long government rate.** Ten years, then no growth, discounted at **5.63%** **[L2000-021]**, **[M1996-025]** (the term and ends are the draft's CONVENTION; on "then at no real growth" see section 8).

| End of the range | Value | Per diluted share (2,422.5M) | Per cover share (2,324.4M) |
|---|---|---|---|
| No-growth case: 14,087 / 0.0563 | **$250B** | **$103** | $108 |
| Shown-growth case: 2.9% for ten years, then flat | **$315B** | **$130** | $136 |

**How sure** **[M1999-104]**. Fairly sure of the level (five years of owner cash within $13.0B to $16.0B; a castle that holds on price); less sure of the growth (flat volume, mixed FY2026 shares, retailer concentration, Q2). The range is narrow: top over bottom is **1.26**, well under the CONVENTION's three-to-one, so this is not TOO HARD **[L2000-025]**, **[M2007-022]**.

**The price against the range.** $144.91 is **above the top** of the range on either share count ($130 diluted, $136 cover). The expected return at the price, solving for the rate that makes the shown-growth stream equal the $351.0B diluted market cap, is about **5.1%**; the owner-cash yield alone is 4.0% (4.2% on the cover count). Either is below the long bond's 5.63% and far below the CONVENTION floor of "about ten percent pre-tax" **[M1994-004]**, **[L2002-020]**, **[M2003-149]**. Read as pre-tax on the business's own figures, FY2026 earnings before income taxes of 20,377 over $351.0B is 5.8%, plus 2.9% growth, still under ten. The value at a 10% expectancy on the shown-growth stream would be about $172B, $71 per diluted share.

**The Q6 buyback check (CONVENTION).** Shares bought in the last quarter of FY2026 averaged "$147.46" (FY2026 10-K, Item 5), above the $103 bottom of the range, so the unpriced programme is not rescued by its prices paid; Q6's WEIGHS AGAINST stands.

**Verdict: OUT.** Valued, but the price does not clear the floor: "there’s just a point at which we drop out of the game" **[M2003-149]**; and no screamer, since the price sits above the whole range rather than far below its bottom **[M2009-005]**, **[L2013-012]**. In the three boxes, OUT **[M2006-013]**.

### Q8. IS IT BETTER THAN THE ALTERNATIVES? STOP. **NOT REACHED** (the run closed at Q7).

---

## 4. Q9 and Q10

**Q9. NOT REACHED. Q10. NOT REACHED.** For the record only, and not weighed: FY2026 total debt $34.5B, of which $11.4B is due within one year; credit facilities of $8.0B undrawn with no ratings triggers; ratings Aa3 / AA- (FY2026 10-K, MD&A Liquidity and Contractual Commitments).

## 5. Q11 and Q12

**Q11.** Not answered: the operator does not hold PG.

**Q12. WOULD WE BE PROUD OF HOW THE MONEY IS MADE?** Asked at the operator's choice (Part VII). P&G is none of the businesses the draft names (casinos, tobacco, loading schemes, gambling dressed as investing) **[M2007-018]**, **[M2005-097]**, **[M2013-015]**, **[M2021-059]**, so Q12 is a WEIGHING here, and for a marketable stake in any case **[M2004-075]**. The newspaper test **[M2008-011]**: it sells detergent, diapers, razors and toothpaste; the legal proceedings disclosed are routine and one emissions-permit penalty in the U.K. "of less than $2 million", self-reported (FY2026 10-K, Item 3). **Verdict: WEIGHS FOR**: nothing in how the money is made would trouble an unfriendly reporter's readers **[M2008-011]**.

---

## 6. The box

**OUT, decided at Q7.** Value as a range, in the draft's form: how much cash, about $14B a year of owner cash after every real cost; how sure, sure of the level, less of the growth; how soon, now and every year, growing about 2.4% to 2.9% a year in nominal terms; at the long government rate of 5.63%, **worth about $250B to $315B, or about $105 to $130 a share**, against a price of **$144.91** (about $351B diluted). The price is above the range, not so far below it that it needs no pencil; the expectancy at the price, about 5%, is under the bond and under the ten percent floor.

(Falsifier CONVENTION, for the record since no purchase is made: the thesis "a castle that holds on price" would be shown wrong by total-company unit volume falling with price flat or down, or by global share falling in three or more of the five segments in one year; next read at the FY2027 10-K, due about August 2027.)

## 7. Self-audit

- **Every id resolves.** All v5 ids cited above were checked by script against `principle_ledger_v5.csv` (column `id`); none missing. No v4 id (E-series) is cited.
- **Every filing fact has an accession.** Each figure carries its document and accession at the point of use or in the Step 0 list; the competitor figures carry the competitors' own 10-K accessions.
- **No number without a row or a filing.** Filing figures carry accessions; derived figures (owner cash, growth, range, expectancy, net tangible capital) are arithmetic on those figures, shown, with the script in `_work_A2r1_PG/q7.py`; the ten-year term, the five-year average, the two ends, the three-to-one width and the ten percent floor are the draft's CONVENTIONS, named as such.
- **Whitelist.** Opened: the protocol, the v5 purchase draft, `principle_ledger_v5.csv`, `tools/sources.py` (function names only), my own working folder and output file. Executed: `tools/sources.py` `price()`, `tools/run.py PG` (arithmetic lines only), `Screens/cover_shares.py PG`. SEC EDGAR fetched directly. Not opened: v4 frameworks, `principle_ledger.csv`, anything under `Test Runs/` or `Screens/` other than executing `cover_shares.py`, `PORTFOLIO.md`, any other file under `Framework/v5/tests/`. Declared: the session's auto-loaded `CLAUDE.md`, `Framework/OPERATOR-PROTOCOL.md` and memory index were in context from the start; none names a PG verdict. `tools/run.py`'s printed v4 floor line and v4 ids were seen on screen and not used (Part VII).
- **Order kept; first failing STOP stopped the run.** Q1 IN, Q2 IN, Q3 weighed, Q4 no STOP and weighed, Q5 IN on integrity, Q6 weighed, Q7 OUT; Q8 to Q10 NOT REACHED. Q7's value is reported only after Q1 to Q6 were IN or weighed. Q12 answered at the operator's instruction, after the box was fixed and without bearing on it.
- **Evidence rules.** Price flagged as an aggregator quote; sovereign from the issuing authority, dated; filings read, not XBRL alone; one figure cross-checked against the filed statement (Step 0). No em dashes in my own prose.

## 8. What in the draft was wrong or unclear

The range CONVENTION in Q7 says the cash is carried ten years and "then at no real growth, discounted throughout at the long government rate"; but the rate is nominal (5.63%) and no row or CONVENTION supplies an inflation figure, so "no real growth" cannot be computed as written without inventing a number. I read it as zero nominal growth after year ten (a flat perpetuity), the lower and less invented reading, and said so; a run that grew the tail at an assumed inflation rate would get a materially higher top end, so the draft should say "no growth" or name the inflation figure. Three smaller points: (1) Q6's buyback CONVENTION reads the prices paid against "the bottom of the Q7 range", but Q7 comes after Q6 in the hard sequence; I gave Q6 its verdict on the grounds that stand without the range and recorded the price check at Q7. (2) The floor CONVENTION is "about ten percent pre-tax", but its source rows differ on what is pre-tax ("after-tax streams of cash at at least a 10 percent rate" **[M1994-004]** against "10% pre-tax returns" **[L2002-020]**); PG fails on either reading, but a closer name would not. (3) Q7's CONVENTION names two closes (TOO HARD on width, OUT when the price is "inside or just below" the bottom) and is silent on a price above the top; I closed it on the floor STOP stated under "Why it is a STOP", which covers it. Also unaddressed: whether value per share uses the cover count or the diluted count where a convertible preferred holds a claim on the owner cash; I used the diluted count and showed both.
