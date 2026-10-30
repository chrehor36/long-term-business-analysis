# Company Run: Adient plc (NYSE: ADNT), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before
any fetch. Working folder: `Test Runs/_research 2026-10-05 ADNT/` (filings as text, the XBRL facts, the peers' filings,
`fetch.py`, `series.py`, `led.py`).

*(Style note: the operator's standing rule forbids em dashes in written work, so the template's dashes are rendered as
colons or hyphens, and operator rule 3's heading is written "COMPUTATION - NOT A CLEARANCE". Quoted ledger fragments are
chosen so that none carries one.)*

**POSITION NOTE, declared before any verdict:** not known to this analyst. The blind rule of this run forbids opening
`PORTFOLIO.md`, so whether the operator holds Adient was not checked and played no part.

**CONTAMINATION DECLARED.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, the run queue, the
prepped reading list, any other `Test Runs/` file about Adient (a directory listing showed none by the ticker), any other
company's 2026-10-05 run or research-pass file, and the unadopted small-cap gaps case. Seen without opening: the file
names in `Test Runs/` (a listing, which showed many other 2026-10-05 runs and research passes by name), and, in the
session's starting context, the git status and the subjects of five recent commits, which name the boxes, deciding
questions and prices of ABG (Asbury Automotive, OUT at Q7, a car dealer), WSC, CAG and GIII. ABG is in the same broad
industry (cars) at the other end of the chain; its subject line says nothing about seat suppliers. The memory index
loaded with the session names no company. Nothing seen bears on Adient's figures.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $17.20 (2026-10-05, live quote printed by `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: Ordinary Shares, par $0.001, **77,096,932**; one class (10-Q for the
  quarter to 2026-06-30, filed 2026-08-05, accession `0001670541-26-000093`; `python Screens/cover_shares.py ADNT`).
  No preferred outstanding (10-K balance sheet: "zero shares issued and outstanding").
- **Market cap:** $17.20 x 77.097M = **$1,326M**.
- **Sovereign for the earnings currency:** **5.63%**, the US Treasury 30-year par yield, 2026-10-02 (issuing authority,
  via `tools/run.py`/`tools/sources.py`). Adient reports in USD; much of its cash is earned in EUR, MXN and CNY, but the
  reporting and debt currency is USD, so the USD rate is used.
- **Filings read** (operator rule 4):
  - 10-K for FY2025 (year to 2025-09-30), filed 2025-11-18, accession `0001670541-25-000152` (Item 1, Item 1A, Item 7,
    the statements, notes on revenue, customers, off-balance-sheet programs, debt).
  - 10-Q for Q3 FY2026 (to 2026-06-30), filed 2026-08-05, accession `0001670541-26-000093`.
  - Proxy (DEF 14A) filed 2026-01-21, accession `0001670541-26-000011` (CD&A, summary compensation table, ownership).
  - 8-Ks: 2026-07-10 `0001670541-26-000080` (CFO Oswald to leave by 2026-12-31); 2026-08-21 `0001670541-26-000100`
    ($500M incremental term loan to redeem the 7.000% secured notes due 2028; term loans then $1.12B); 2026-09-18
    `0001670541-26-000105` (director Peter H. Carlin, a former hedge-fund analyst, resigns from the board to become CFO
    from 2026-11-16; target equity award $4.25M).
  - Earlier 10-Ks for the history: FY2017 `0001670541-17-000071`, FY2018 `0001670541-18-000065`, FY2019
    `0001670541-19-000057`, FY2020 `0001670541-20-000080`, FY2021 `0001670541-21-000133`, FY2022
    `0001670541-22-000118`, FY2023 `0001670541-23-000153`, FY2024 `0001670541-24-000109`.
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025, **$449M** on
  the filed consolidated statement of cash flows (10-K FY2025, `0001670541-25-000152`, page 61) = the $449.0M
  `tools/run.py` transcribed from XBRL. Also equity-based compensation $32M / $31M / $34M (FY2025/24/23) match.
- `tools/run.py ADNT` arithmetic lines only (Part VII). **What its "owner earnings" line leaves out, found on reading the
  filing:** (a) **dividends paid to noncontrolling interests** ($90M FY2025, $72M FY2024, $67M FY2023; financing
  section of the cash-flow statement). Adient consolidates joint ventures in which partners own a share; their part of
  the operating cash belongs to the partners and leaves as these dividends. Its owner earnings are therefore overstated
  for an Adient shareholder by $67M to $106M a year. (b) **Receivables sold without recourse** inside operating cash:
  funded balances $132M (FY2021), $269M (FY2022), $170M (FY2023), $170M (FY2024), $185M (FY2025), $157M (2026-06-30)
  (10-K FY2022, FY2023, FY2024, FY2025, 10-Q). The changes (+$137M FY2022, -$99M FY2023, 0, +$15M FY2025) move
  operating cash. A supplier-finance program adds $105M (FY2025) of payables timing. (c) **Dividends from
  partially-owned affiliates** are inside operating cash: equity income $68M with a "net of dividends received"
  adjustment of +$36M (FY2025), so roughly $104M received; about $73M (FY2024) and $50M (FY2023). This is the Q4
  equity-method convention's own measure (dividends received), so they stay in. The run.py yields, "growth the price
  assumes" and its owner-earnings means are not used.

### Owner cash after every real cost, to Adient's own shareholders (USD millions)
Operating cash, less stock pay (added back in operating cash, a real cost **[L2015-003]**: "is the most egregious
example"), less capital expenditures, less dividends to noncontrolling interests. Source: XBRL transcription of each
10-K (accessions above), FY2025 checked to the statement.

| FY (Sept) | OCF | SBC | Capex | Depreciation | Amort. | NCI dividends | **Owner cash (capex)** | Owner cash (depreciation + amortization) |
|---|---|---|---|---|---|---|---|---|
| 2017 | 746 | 45 | 577 | 337 | 21 | 79 | **45** | 264 |
| 2018 | 679 | 47 | 536 | 400 | 47 | 74 | **22** | 111 |
| 2019 | 308 | 20 | 468 | 278 | 40 | 62 | **-242** | -92 |
| 2020 | 246 | 15 | 326 | 295 | 37 | 71 | **-166** | -172 |
| 2021 | 260 | 36 | 260 | 285 | 45 | 69 | **-105** | -175 |
| 2022 | 274 | 29 | 227 | 298 | 52 | 106 | **-88** | -211 |
| 2023 | 667 | 34 | 252 | 290 | 50 | 67 | **314** | 226 |
| 2024 | 543 | 31 | 266 | 285 | 47 | 72 | **174** | 108 |
| 2025 | 449 | 32 | 245 | 279 | 46 | 90 | **82** | 2 |
| TTM to 2026-06 | 579 | 38 | 284 | n/a | n/a | 91 | **166** | n/a |

- **Five-year mean, FY2021-FY2025 (the Q7 convention's window): $75.4M** on the capex basis; **-$10M** on depreciation
  plus amortization; **$38M** on depreciation alone. Excluding the factoring swings FY2022-FY2025 (FY2021's change not
  found, the FY2020 balance is not disclosed in that wording): **$64.8M**.
- **Nine-year mean, FY2017-FY2025 (whole cycle since the spin): $4M.** Its first four years carry China joint-venture
  dividends from businesses sold in 2020-2021 (YFAI 30% for $369M; YFAS 49.99% for $1,210M; 10-K FY2021, Note on the
  2021 Yanfeng Transaction), so it is a different business in part; its last five years carry the chip shortage.
- **Normal-volume variant, FY2023-FY2025: $190M**, falling each year (314, 174, 82).
- **TTM: $166M** (10-K FY2025 less the nine months to 2025-06-30 plus the nine months to 2026-06-30). The 10-K warned
  that FY2026 cash flow would be lower than FY2025 "due primarily to reduced profitability resulting from lower
  production volumes, higher capital spending to fund growth initiatives, non-recurring tax settlements and an
  acceleration in the timing of commercial settlements in fiscal 2025"; the nine months came in higher on payables.
- Capex against depreciation: nine-year capex $3,157M against depreciation $2,747M; but in the last five years capex
  ($1,250M) ran below depreciation ($1,437M). The FY2026 capex is rising ($205M in nine months against $166M).
  Maintenance cannot be separated from the filing; the 10-K gives no maintenance figure **[M2000-144]**, so the capex
  basis is used as the central input and the depreciation basis shown beside it.
- **Restructuring every year:** cash-type restructuring charges (impairments removed) $46M, $46M, $110M, $185M, $21M,
  $25M, $40M, $159M, $51M FY2017-FY2025, and "In each of the last seven fiscal years, Adient announced restructurings"
  (10-K FY2025, Item 1A). These are counted as real costs: "when management is simply making business adjustments that
  are necessary, is misleading" **[L2016-007]**.

---
## THE FOUNDATIONS (not a gate)
A share is a business: would the buyer be content to own this "if the market closed for five years?" **[M1997-109]**
That question bears hardest here, because the stock's own recent prices (about $26.9 average paid in the FY2023-FY2025
buybacks, $21.43 in FY2026, $17.20 today) invite a trade on the quotation rather than a judgment of the business. The analyst's habits govern the reading: look "at what you’re missing"
**[M2025-013]**, "destroy our previous ideas" **[M2016-054]**, and make the reading "to possibly reject your original
hypothesis" **[M1998-144]**. No macro forecast enters: the industry's 2026 volumes, tariffs and EV pace are recorded only
as facts about the business. **Contrary evidence, written down as found** **[M1997-127]** ("write it down in the first 30
minutes"):
1. *(found reading Item 1, against the OUT that was forming)* Adient calls itself "a global leader in the automotive
   seating supply industry with leading market positions in the Americas, Europe and Asia", vertically integrated in
   foam, trim, frames and mechanisms; seats are delivered "just-in-time" or "in-sequence" to the assembly line, which
   makes them hard to ship in from abroad.
2. *(found reading the segment table)* Asia earns adjusted EBITDA of 14.8% of sales (FY2025: $440M on $2,983M), far
   above any other region.
3. *(found reading MD&A)* Gross margin rose in FY2025 (6.6% against 6.3%) on "favorable commercial and supplier
   pricing adjustments"; Americas adjusted EBITDA rose three years running ($336M, $375M, $402M).
4. *(found reading the 9-month 10-Q)* Operating cash for nine months was $366M against $236M a year before, and TTM
   owner cash ($166M) is double the five-year mean.
5. *(found reading the Lear comparison)* Lear, the stronger competitor, also earns only 5.5% to 7.9% in seating: if
   the whole industry is thin, Adient's thinness is partly the industry's and not only Adient's.
6. *(found reading the 2023 transcript row)* Buffett himself says of the auto industry, "I don’t think I can tell you
   what the auto industry will look like five or ten years from now" **[M2023-100]**, which argues that Q1 should close
   this file TOO HARD rather than let Q2 close it OUT (see Q1).

## THE STANDING RULE
Owning this would not put the buyer at risk of ruin provided it is bought without borrowed money and sized so that a
total loss cannot touch what the buyer needs: "We are never going to risk what we have and need for what we don’t have
and don’t need." **[M2012-081]**; "the only way smart people can get clobbered, really, is through leverage"
**[M2004-065]**. The target's own debt is a Q9 matter and is not reached.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
"the first question is, can I understand it?" **[M1995-051]**; understanding is "a reasonable fix on about what the
earning power and competitive position will look like in five or 10 years" **[M2012-065]**.

- **What the business is (10-K FY2025, Item 1).** Adient designs and builds complete seats and their components
  (frames, mechanisms, foam, trim covers, head restraints) in about 200 plants in 29 countries, with more than 65,000
  employees, and delivers complete seats "on a “just-in-time” or “in-sequence” basis" to the automakers' lines.
  "Essentially all of Adient’s sales are to the automotive industry." Ford 11%, Volkswagen 10%, Stellantis 10% of FY2025
  sales (Note 1). Raw materials: steel, aluminum, polyurethane chemicals, fabrics, leather, vinyl.
- **The key variables** **[M1998-044]** ("trying to identify the key variables in that particular business, and
  evaluating how predictable they were first"): (1) vehicles built on Adient's programs, by region (10-K: "Demand for
  automotive parts in the OEM market is generally a function of the number of new vehicles produced"); (2) Adient's share
  of seat awards, including with the Chinese automakers; (3) the annual price reductions the contracts impose against the
  cost savings Adient can find; (4) recovery of input costs (steel, chemicals, labor, tariffs) from the customers.
- **Foreseeable?** The product does not change fast: the 10-K says "seating systems are not largely impacted by the shift
  to EVs", and no technology threatens to make a seat obsolete. What matters is "the economic dynamics of the industry"
  **[M2011-014]**, and those can be read from ten years of filings: a build-to-order supplier whose price is set by
  contract downward each year, whose volume is set by its customers' production, and whose margin has stayed thin in
  every year since the spin (Step 0 table; Q2 competitor row). The earning power ten years out can be foreseen in its
  shape: thin, cyclical, and capped by the customers. The competitive position can be foreseen in its shape: one of two
  global seat leaders with Lear, under pressure from Chinese competitors and automakers. The volumes and the exact rank
  cannot be foreseen, and are not needed to judge the castle.
- **Against IN, written down:** "or an auto business, I’m not sure I’d know where we would stand in the competitive
  pecking order five or 10 years from now" **[M1996-062]**; "I don’t think I can tell you what the auto industry will look
  like five or ten years from now" and "It’s just a business where you’ve got a lot of worldwide competitors, they’re not
  going to go away." **[M2023-100]**. These rows are the speakers' own words about the auto business, and "if you have
  doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. My reading: both rows deny a
  fix on the *pecking order* and on the *industry's shape*; neither denies that the economics of a supplier to that
  industry can be seen to be poor. The framework sends a business to TOO HARD at Q1 when "its industry changes fast"; the
  seat does not change fast, and what is uncertain is who wins, which is the Q2 question.
- **VERDICT: IN, narrowly.** The economics of Adient are understood well enough to judge the castle, and the judgment is
  made at Q2. A second analyst who reads **[M2023-100]** as the speakers' verdict on the whole auto chain could close here
  TOO HARD (NATURE) "If something’s important but unknowable, forget it." **[M2006-076]**; the box would differ and the
  decision (no purchase) would not.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. Each test with its filing fact.

1. **The money test** **[M2011-015]**. Could a well-funded attacker take this business? The filings say it is being done:
   Adient's former China partner Yanfeng took the seating joint venture in 2021 (YFAS, 49.99% sold for $1,210M) and is
   now listed by Adient among its principal competitors with Lear, Toyota Boshoku, Forvia and Magna (10-K FY2025, Item
   1, Competition); the automakers themselves are attackers: "Several OEMs have shifted from sourcing a complete seating
   system to a components approach" and "Some OEMs are conducting the design and engineering internally" (Item 1,
   Sourcing Patterns); the 10-K names "intensifying competition from Chinese imports" and "market share loss for
   foreign/luxury OEMs in the Asia reporting unit combined with modest expected margin declines as Adient continues to win
   new business with local OEMs in China" (Item 7). The answer is yes. "If the answer had been yes, we wouldn’t have done
   it." **[M2011-015]**
2. **Pricing power and the agony before a rise** **[M2005-020]**. "it’s not a great business when you have to have a
   prayer session before you raise your prices a penny". Adient's contracts run the other way: "Contracts with customers
   may provide for annual price reductions over the production life of the awarded program" (10-K, Note 2); the risk
   factor: Adient "may be unable to achieve product cost reductions that offset customer-imposed price reductions", and
   "large commercial settlements with Adient's customers likely would adversely affect Adient's results" (Item 1A).
   Programs "do not contain a firm commitment by the customer for volume or price" and "the program can be canceled at
   any time without cause by the customer" (Note 2). Pricing power belongs to "a business that’s a monopoly or a near
   monopoly" **[M2010-092]**; here the power sits with the customer.
3. **Would the customer still choose it over the low bid?** **[M2017-009]** ("it wouldn’t be a question of people
   buying candy for the low bid"). The seat is built to the automaker's design and the award is competed; Adient pays the
   customer to win it: "In pursuit of new program awards, Adient at times agrees to make upfront payments to customers",
   with $174M of such payments capitalized at 2025-09-30 ($155M a year earlier) and amortized against revenue (Note 2).
   The automaker does not ask for the seat by name; the end buyer does not know who made it. The insurance row fits it
   closely: "the product is available from many suppliers" and "most insureds don't care from whom they buy"
   **[L2004-003]**. Contrast the castle the speakers name, where "most of the customers would be totally crazy to hire
   some other supplier" **[M2016-009]**.
4. **The low-cost position** **[M1997-010]**: "commodity businesses have risk unless you’re the low-cost producer,
   because the low-cost producer can put you out of business". The competitor row below shows Lear's seating segment
   earning 2.8 to 7.2 points of sales more than Adient's whole business in every comparable year from 2017 to 2025 (1.7
   points at the narrowest after the comparability adjustments below), and
   Lear's seating sales ($17.3B in 2025) are larger than Adient's ($14.5B). Adient is not the low-cost producer; "being
   the low-cost producer is all-important" **[L2000-017]** where the product is commodity-like, and "the guy with the lower
   cost comes in and kills you" **[M2001-013]**.
5. **Unit volume and share of mind.** Net sales $16.8B (FY2016, a spin year) to $14.5B (FY2025); part is divestiture
   (RECARO and the fabrics business sold in FY2020, Adient Aerospace deconsolidated, China joint-venture interests sold), part is volume: FY2025 MD&A, "lower
   overall production volumes in EMEA" and "other intentional portfolio reductions ($336 million)". Share of mind does not
   apply: the customer is an automaker's purchasing department.
6. **Ask the competitors** **[M1999-130]**: not available on the public record beyond the filings; the competitors'
   own margins are in the row below.
7. **Widening or narrowing** **[M1999-108]** ("whether it’s likely to widen further or shrink on you"). Adjusted EBITDA
   (before depreciation of about 1.9% of sales, before corporate costs) by region, from the 10-Ks:

   | FY | Americas | EMEA | Asia |
   |---|---|---|---|
   | 2019 | 2.7% ($210M / $7,785M) | 2.4% ($161M / $6,675M) | 22.0% ($513M / $2,337M) |
   | 2020 | 3.9% | 2.0% | 23.3% |
   | 2021 | 3.8% | 5.0% | 22.9% |
   | 2022 | 3.7% | 2.9% | 13.1% |
   | 2023 | 4.7% | 4.5% | 15.0% |
   | 2024 | 5.5% | 3.1% | 14.7% |
   | 2025 | 5.9% ($402M / $6,856M) | 2.6% ($124M / $4,773M) | 14.8% ($440M / $2,983M) |

   (10-K FY2021 `0001670541-21-000133`, FY2022 `0001670541-22-000118`, FY2025 `0001670541-25-000152`, segment tables.)
   Asia's figure includes equity income from Chinese affiliates and earnings shared with minority partners; its margin
   fell from about 23% to about 13% to 15% after the joint-venture interests were sold. EMEA, a third of sales, earns 2.6% before depreciation, which means a loss or
   close to it after depreciation; its goodwill was written down by $333M in FY2025 and the 10-K names "overcapacity in
   the EMEA reporting unit resulting in pricing pressure". Equity income fell in FY2025 by $39M from "the KEIPER supply
   agreement modifications, including the addition of a performance based rebate to the shareholders" (value moving to
   the joint-venture partner). Americas improved, mostly on "commercial and supplier pricing adjustments" and tariff
   recoveries, not on a position that changed. The castle, where there is one (Asia), is narrowing; where there is none
   (EMEA), the business is restructuring every year.
8. **What could destroy, modify or reduce it** **[M2000-014]** ("destroy, or modify, or reduce the economic
   strengths"): Chinese automakers and suppliers taking share at home and in Europe (Item 1A: "As the size of the Chinese
   market evolves and as Chinese OEMs penetrate other markets around the globe, often with lower-cost products"), OEM
   component sourcing and insourcing, and a large customer's program cancellation, which the contract allows "at any time
   without cause".

**The competitor row** (same kind of figure from each company's own filing; the fiscal years differ: Adient to September,
Lear and Magna to December):

| Year | Adient whole company: gross profit less SG&A less cash-type restructuring, excl. equity income and non-cash impairments, % of sales | Lear Seating segment earnings, % of sales | Magna Seating Systems Adjusted EBIT, % of sales |
|---|---|---|---|
| 2017 | 3.8% | 7.9% | not read |
| 2018 | 0.7% | 7.9% | not read |
| 2019 | 0.1% | 6.4% | not read |
| 2020 | -1.2% | 4.6% ($590.5M / $12,712.7M) | 2.4% |
| 2021 | 2.0% | 5.9% | 3.1% |
| 2022 | 1.3% | 5.7% | 1.9% |
| 2023 | 2.9% | 6.1% ($1,066.9M / $17,548.8M) | 3.6% ($218M / $6,047M) |
| 2024 | 1.8% | 5.7% | 3.8% |
| 2025 | 2.7% ($388M / $14,535M) | 5.5% ($948.8M / $17,283.0M) | 3.6% ($210M / $5,898M) |

Sources: Adient from the XBRL lines of each 10-K (gross profit, SG&A, restructuring and impairment, with the named
non-cash impairments removed: SS&M $1,086M and held-for-sale $49M in FY2018, SS&M $66M in FY2019, $53M of non-cash
items in FY2020, Aerospace $9M in FY2024, EMEA goodwill $333M and Aerospace $8M in FY2025). Lear: 10-K FY2025
`0000842162-26-000011`, FY2022 `0000842162-23-000011`, FY2019 `0000842162-20-000006`, FY2016 `0000842162-17-000006`,
Seating segment discussion and segment note (segment earnings are after depreciation, amortization and restructuring,
before corporate costs, interest, other expense and equity income). Magna: Form 40-F annual reports, MD&A, Seating Systems
segment, `0001193125-26-128771` (2025, 2024), `0001193125-25-066935` (2023), `0001193125-23-087951` (2022, 2021),
`0001193125-22-085474` (2020); Magna's Adjusted EBIT includes equity income; 2017 to 2019 for Magna were not read (the
40-F exhibits fetched for those years were the annual information forms, not the MD&A). **Comparability:** Lear's segment
figure excludes corporate costs (Lear's "Other" category ran $(362.6)M in 2023 on total sales of $23,466.9M, about 1.5%
of sales); Adient's figure is after its corporate costs ($85M FY2025, about 0.6% of sales) and before its equity income
($68M FY2025, about 0.5%). Put both adjustments into Adient's favor and its FY2025 figure is about 3.8%, against Lear's
5.5%; over 2017 to 2025 the gap never closes. **Forvia (Faurecia) and Toyota Boshoku** file no reports with the SEC; their
own reports were not read and no figure is written for them (flagged, not on the evidence ladder this run used).

**Reading the row.** The best operator in the field (Lear) earns 4.6% to 7.9% before corporate costs; the third (Magna)
1.9% to 3.8%; Adient, "a global leader" by its own description, sits with Magna and below Lear. The row shows three things: no
seat maker has a castle against its customers; within the industry Adient is not the low-cost producer; and the gap is
steady across the whole span, so it is not a bad year. "you can have only two competitors and they’re still terrible
businesses, they beat each other’s brains out" **[M2013-052]**; "the improvement you get one day, your competitor gets
the next day" **[M2004-053]**; "one competitor is frequently enough to ruin a business" **[M2012-108]**.

**The evidence for the castle, weighed.** The sequencing and just-in-time delivery are real: seats are not "a product that
can be shipped in from abroad very easily" **[M2007-116]**, so the labor-content test does not condemn the assembly
(though trim covers are sewn in low-cost countries by Adient itself and its rivals). A program, once won, runs for the
life of a vehicle. But the same filing says the customer can cancel without cause, sets the price downward by contract,
and is paid by Adient to award the work; and the competitors build the same sequencing plants beside the same assembly
lines. The protection is against a newcomer for the life of one program, not against the customer or the incumbent
rival, and it does not show up in the margins of any of the three companies. A castle would show as the opposite of
**[M2000-031]** ("Anytime you can charge more for a product and maintain or increase market share against
wellentrenched, well-known competitors"); Adient's sales are shrinking while its prices are cut.

- **VERDICT: OUT.** The castle is shown open on the evidence, not merely unclear: the customer sets and cuts the price
  by contract, can cancel without cause, is paid to award the business, and the leading rival earns more on the same
  product in every year since the spin. Three items on the framework's list of what Q2 rules OUT fit (named here in my
  words, not quoted): the high-cost producer in a commodity field, where "a company must lower its costs to competitive
  levels or face extinction" **[L1994-035]** (also **[M1997-010]**, **[M2001-013]**); the customer indifferent to the
  supplier, "most insureds don't care from whom they buy" **[L2004-003]** (also **[M2017-009]**); and the business whose
  improvements pass to the customer **[M2004-053]**.
  A low price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little"
  **[M2019-015]**. In the three boxes **[M2006-013]**, OUT.

---
## Q3: NOT REACHED (the file closed OUT at Q2).
## Q4: NOT REACHED as a verdict. The balance sheets are read below under COMPUTATION, as the template asks when the file
closes before Q4.
## Q5: NOT REACHED.
## Q6: NOT REACHED.
## Q7: NOT REACHED.
## Q8: NOT REACHED.
## Q9: NOT REACHED.
## Q10: NOT REACHED.
## Q12 (optional): NOT ASKED.

---
## COMPUTATION - NOT A CLEARANCE
*Everything in this section was computed after the file closed OUT at Q2. It carries no entry language and clears
nothing (operator rule 3). It is reported at the owner's request, not as a step of the run.*

### The balance sheets, ten year-ends, before the income account **[M2025-032]**
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. From
`tools/run.py`'s first-filed XBRL table, read against the FY2025 and FY2018 filed statements (USD millions):

| Sept 30 | Assets | Equity (Adient) | Goodwill | Intangibles | Tangible equity | Retained earnings | Cash | Inventory | Debt on the face |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 12,956 | 4,176 | 2,179 | 113 | 1,884 | 0 | 105 | 660 | 3,521 |
| 2018 | 10,942 | 2,392 | 2,182 | 460 | -250 | -1,028 | 687 | 824 | 3,430 |
| 2020 | 10,261 | 1,213 | 2,057 | 443 | -1,287 | -2,096 | 1,692 | 685 | 4,307 |
| 2022 | 9,158 | 2,073 | 2,057 | 467 | -451 | -1,108 | 947 | 953 | 2,578 |
| 2024 | 9,351 | 2,134 | 2,164 | 371 | -401 | -885 | 945 | 758 | 2,405 |
| 2025 | 8,954 | 1,766 | 1,807 | 319 | -360 | -1,166 | 958 | 695 | 2,397 |
| 2026-06 (10-Q) | n/a | 1,729 | 1,799 | n/a | n/a | n/a | 924 | n/a | 2,379 long-term |

What the figures say: the equity handed over at the spin has been more than lost. Net income attributable to Adient
summed over FY2016 to FY2025 is **-$2,462M** (-1,546, +877, -1,685, -491, -547, +1,108, -120, +205, +18, -281); the
one large positive year (FY2021, +$1,108M) is the gain on selling the China joint ventures, not operations. Tangible
equity has been negative since FY2018. Goodwill has been written down twice (SS&M $299M in FY2018, EMEA $333M in FY2025)
and long-lived assets once ($787M SS&M, FY2018). Debt peaked at $4.3B in FY2020 (COVID, cash held at $1.7B) and was cut to
$2.4B mainly with the proceeds of the China and other disposals ($2,024M received FY2020-FY2022), not from operating cash. Inventory has risen against falling sales (3.9% of sales in
FY2016 to 4.8% in FY2025). Payables ($2,549M) equal receivables plus inventory ($1,873M + $695M): the suppliers finance
the working capital, helped by $185M of sold receivables and a $105M supplier-finance program. Noncontrolling interests
($297M plus $95M redeemable) are a claim on the consolidated cash ahead of Adient's owners. What they cannot say: the
value of the customer relationships and the sequencing network, which the balance sheet carries as intangibles still
being amortized ($319M).

### Earnings after every real cost
Adient's own headline measure is "Adjusted EBITDA" ($881M FY2025), the segment metric and the main pay metric. "The one
figure we regard as utter nonsense is the so-called EBITDA." **[M1998-086]**; depreciation is "an economic cost every bit
as real as wages, materials, or taxes" **[R1996-023]**. After depreciation ($279M), stock pay ($32M), purchase-accounting
amortization ($47M), restructuring ($51M cash-type), corporate costs ($85M), interest ($193M) and the partners' share
($90M), the old-fashioned earnings "after interest, taxes, depreciation, amortization and all forms of compensation"
**[L2021-003]** are close to nothing: net income attributable to Adient was $205M (FY2023), $18M (FY2024), -$281M
(FY2025, after the two non-cash impairments of $341M; their tax effect is not separated in the filing), and $30M for the nine months
to 2026-06-30, on a nine-month tax charge of $97M against pre-tax income of $182M. Cash taxes paid ran $77M to $96M a year
FY2021-FY2025 whatever the pre-tax income was (withholding on repatriation, valuation allowances in Germany, Mexico, the
U.S. and others).

### Value range (the Q7 CONVENTION construction, run as computation)
Inputs: owner cash five-year mean **$75.4M** (capex basis, after NCI dividends); the sovereign 5.63%; ten years then no
growth; 77.097M shares. Growth shown: the owner cash has no computable rate over the window (FY2021 is negative, and "a
base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**), and over
FY2023-FY2025 it fell each year. **CONVENTION of this run:** the top end is no growth (the convention never carries
growth above what was shown, and nothing positive was shown); the bottom end is a decline of 2.6% a year for ten years,
which is net sales FY2018 ($17,439M) to FY2025 ($14,535M), a figure that includes divestitures and is used because it is
the business's own shown direction, not a forecast.

| Case | Owner cash base | Growth, years 1-10 | Value | Per share |
|---|---|---|---|---|
| Convention, no growth (top) | $75.4M | 0% | $1,339M | **$17.37** |
| Convention, shown decline (bottom) | $75.4M | -2.6% | $1,091M | **$14.15** |
| Five-year, excluding factoring swings | $64.8M | 0% / -2.6% | $1,151M / $938M | $14.93 / $12.16 |
| **Whole-cycle variant, FY2017-FY2025** | $4M | 0% / -2.6% | $71M / $58M | **$0.92 / $0.75** |
| Normal-volume variant, FY2023-FY2025 | $190M | 0% / -2.6% | $3,375M / $2,749M | $43.77 / $35.66 |
| TTM | $166M | 0% / -2.6% | $2,948M / $2,402M | $38.24 / $31.15 |

- **(a) VALUE RANGE per the Q7 convention: $14.15 to $17.37 a share against $17.20.** The convention's range is narrow
  (about 1.2 to 1) and the price sits inside it, near the top: by the convention's own close this would be OUT (not a
  screamer; a pencil is needed **[M1996-084]**: "it’s too close to think about").
- **Whole-cycle variant**, because the five-year window holds abnormal years (the chip shortage of FY2021-FY2022) and
  the business changed inside the span (the China JV sale): the nine years since the spin produced **$0.75 to $0.92 a
  share** of value on the same construction, and the three normal-volume years **$35.66 to $43.77**. Across the variants
  the range is more than forty to one; under the convention's three-to-one test that alone would be TOO HARD: "the range
  must be so wide that no useful conclusion can be reached" **[L2000-025]**, and a wide range is not cured by a bigger
  discount: "we don’t really try to compensate for that sort of thing by having some extra large margin of safety"
  **[M2007-022]**. The speakers' own rule for a cyclical earner points to the whole cycle: "we would rather buy at a 10 or
  12 times multiple of a bad year than buy at an eight times multiple of a good year" **[M2015-079]**.
- **(b) FAIR PRICE: about $14.00 a share** (central case $75.4M, no growth). **Tax treatment:** the owner cash is after
  Adient's cash taxes, so the floor is applied in its after-tax form. The floor is "a very high probability of at least
  10% pre-tax returns" **[L2002-020]**, whose own after-tax translation in that row carries a damaged character before
  the 7% and reads as 6 to 7 percent; the stricter 7% is used: $75.4M / 7% = $1,077M = **$13.97**. At 6.5%, $15.05. The
  pre-tax form (owner cash plus the five-year mean cash tax of $87.4M = $162.8M, at 10%) gives $21.12; it is shown and not
  used, because Adient's cash taxes run at more than half of its pre-tax income in FY2026's nine months and are a
  recurring cost that never reaches the owner, so a pre-tax yield on this company overstates what the buyer gets.
- **(c) CHEAP PRICE: about $7.00 a share.** **Rule (CONVENTION of this run):** half the fair price, a margin of one half,
  because the margin must widen as understanding falls and volatility rises, "the larger the margin of safety"
  **[M1997-080]**, and the speakers take the margin as "a big discount from that present value" **[M1997-126]**. Even at
  $7.00 the whole-cycle variant ($0.75 to $0.92) says the decision would still need a pencil; no price was found at which
  this business screams.
- **Against the price:** $17.20 is above the fair price ($13.97), inside the convention range near its top ($17.37), far
  above the cheap price ($7.00), and about nineteen times the top of the whole-cycle value. The five-year owner-cash yield at $17.20 is 5.7%,
  against a sovereign of 5.63%.

### Notes for a later run, recorded only (none is a verdict)
- **Buybacks:** $465M for 17,297,377 shares FY2023-FY2025 (average about $26.9) and $55M for 2,566,693 shares in FY2026
  at $21.43 (10-Q, Part II Item 2); the program names no price. Every average paid is above the top of the convention range
  ($17.37) and above the fair price; read against **[L2016-002]** ("repurchases only make sense if the shares are bought at
  a price below intrinsic value") and **[L2011-003]** ("what is smart at one price is dumb at another"), the Q6 convention
  would weigh this against. Dividends were suspended after the first quarter of FY2019.
- **Pay** (proxy `0001670541-26-000011`): the annual bonus pays on Adjusted EBITDA (40%), "Free Cash Flow" defined as
  operating cash less capex, before the partners' dividends (40%), and "Corporate Transformational Projects" judged
  achieved or not (20%). For FY2025 the committee raised the measured Adjusted EBITDA by $12M and Free Cash Flow by $32M to
  remove restructuring and tariff costs, lifting the payout from 98% to 108%; the FY2023 performance shares, which had
  missed the return-on-sales threshold (5.6% against 5.7%), were adjusted by 0.2 points and $22M to pay 43% instead of
  28%. The CEO's reported pay was $3.8M (FY2023), $9.5M (FY2024) and $13.1M (FY2025), the last in a year of a $281M net
  loss, against a market value of $1.3B. Directors and officers as a group own 735,239 shares, under 1%. Read against
  **[L1996-019]** ("we never greet good work by raising the bar"), whose inverse is lowering it after the fact, and
  **[M2003-019]**; recorded, not weighed, because Q5 and Q6 were not reached.
- **Debt:** about $2.4B (after the August 2026 refinancing: term loans $1.12B to 2031, $500M 8.250% notes 2031, $795M 7.50%
  notes 2033), $924M cash, an undrawn $1.0B asset-based revolver to 2030 secured on receivables and inventory. Coverage,
  measured as "pre-tax earnings/interest, not EBITDA/interest" **[L2012-002]**: (pre-tax income plus net financing
  charges) over net financing charges was 2.5x (FY2023), 1.7x (FY2024), 0.5x (FY2025; 2.3x before the two non-cash
  impairments). "Businesses earning good returns on equity while employing little or no debt" **[R1997-001]** is not met
  on either half. Q9 was not reached.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the filings: the customer cuts the price by contract, can cancel without
cause and is paid to award the work, and Lear earns 2.8 to 7.2 points of sales more on the same product in every year since
the spin, so Adient is neither protected from its customers nor the low-cost producer among its rivals. Q1 passed
narrowly (an analyst could close it TOO HARD (NATURE) on **[M2023-100]**; the decision would be the same). Computation
only: the Q7 convention range $14.15 to $17.37 against $17.20; the whole-cycle variant $0.75 to $0.92; fair about $14.00;
cheap about $7.00.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written question by question in one sitting; **not committed**, because
      this run's instructions forbid commits (the write-early commit rule could not be kept; declared).
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`; result below); every filing fact has its
      accession; no number without a filing or a CONVENTION label. No v4 (E-) id is cited.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance, and the later material sits under the
      COMPUTATION heading.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash less stock pay, capex and the partners'
      dividends, with the depreciation basis beside it (operator rule 5). The sovereign from the US Treasury; the price
      an aggregator quote, flagged.
- [x] Contrary evidence written down as it was found **[M1997-127]** (six items, in the foundations, before the verdicts).
- [x] No row dated after the anchor is cited (this is not a point-in-time test; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its yields, implied growth and v4 material were not.
- [x] `python tools/check_framework.py` run (result recorded below).

**Check results (2026-10-05):** `python tools/check_framework.py`: **PASS** (all checks, including phantom ids across every
run file). Citation check, `Test Runs/_research 2026-10-05 ADNT/cite_check.py`: no E- ids; 58 distinct M, L and R ids,
all present in `principle_ledger_v5.csv`; every quoted fragment set beside an id (before or after it) found in that id's
row, split on "[...]": 0 problems. Its first pass caught two places where the framework's own wording was quoted beside
row ids (the Q2 verdict); both were rewritten before the PASS.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 for a business whose economics are foreseeably poor.** Q1 asks for "a reasonable fix" on earning power and
   competitive position; it does not say whether foreseeing that the economics will stay thin counts as understanding.
   The speakers' own rows about the auto business (**[M1996-062]**, **[M2023-100]**) deny a fix on the pecking order and
   the industry's shape, yet the seat's economics are plain from ten years of filings. I passed Q1 narrowly and let Q2
   close the file OUT on the evidence; another analyst could close at Q1 TOO HARD (NATURE). The framework should say
   which question owns "the economics are visible and visibly poor".
2. **Partners' share of consolidated cash.** Neither Q4 nor the Q7 convention says what to do with cash that belongs to
   noncontrolling partners in consolidated joint ventures. `tools/run.py` counts all of operating cash as the owner's,
   which overstates Adient's owner cash by $67M to $106M a year (more than the whole five-year mean of $75.4M). I deducted
   the dividends paid to noncontrolling interests, by the definition "the cash that can be taken out of a business"
   **[R1996-018]**; the convention should state it.
3. **The growth input when the window's base is negative.** The Q7 convention measures growth on aggregate owner cash;
   with a negative first year there is no rate, and with a falling last three years the shown growth is negative. The
   convention does not say what the "shown-growth end" is then. I confessed a decline case taken from net sales.
4. **Pre-tax floor against after-tax owner cash.** The floor is "about ten percent pre-tax"; owner cash is after tax. For
   a company whose cash taxes run above half its pre-tax income, the two forms give $14.00 and $21.12. I used the
   after-tax form and said why; the convention should fix one.
5. **A window that straddles a change of business.** The five-year window FY2021-FY2025 and the nine-year cycle both
   cross the sale of the China joint ventures, whose dividends were part of the pre-2021 cash. The convention picks the
   window mechanically; it does not say when a window that crosses a large disposal stops being "the growth the business
   has actually shown".
6. **The protocol's dash.** Operator rule 3 prescribes the heading with an em dash between "COMPUTATION" and "NOT A CLEARANCE", and the operator's
   standing rule forbids em dashes; the heading is written with a hyphen here. One of the two should yield.
