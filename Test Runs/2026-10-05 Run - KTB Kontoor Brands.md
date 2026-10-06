# Company Run: Kontoor Brands, Inc. (NYSE: KTB), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Written on the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated name before any fetch. Working folder:
`Test Runs/_research 2026-10-05 KTB/` (filings as text, `fetch.py`, `value.py`, `rows.py`). The session limit stopped the
first session while it read the 8-Ks; the second session resumed on 2026-10-06 from the files on disk under the same brief
and blind rule. Every judgment cites a v5 ledger id; every filing fact carries its accession.

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`, so
whether the operator holds KTB is unknown to this analyst.

**CONTAMINATION, declared.** I opened none of the forbidden files. I did see these things: the commit subjects in the session's
git snapshot (purchase runs of INVA, PBH and RHI, which mention a "fair" and a "cheap" price, and a `run.py` change for SKYW);
the file names of two other 2026-10-05 runs (AMN, POOL), which I did not open; and the auto-memory index line "57
gate-clearers, nothing buyable". None of them names Kontoor. My fair-price and cheap-price rules below are my own and are
confessed as CONVENTIONS of this run. I did not read how the other runs built theirs.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $64.19 (2026-10-05, from `tools/run.py`; an aggregator live quote, flagged under operator rule 5).
- **Shares:** one class, 54,653,620 common, no par value. The cover of the 10-Q for the quarter ended 2026-07-04 gives them
  as of 2026-07-31 (filed 2026-08-12, accession `0001760965-26-000059`; `python Screens/cover_shares.py KTB`). The balance
  sheet gives 54,650,957 at June 2026. No second class and no preferred is outstanding.
- **Market cap:** $3,508M.
- **Sovereign for the earnings currency (USD):** 5.66%, the US Treasury daily par yield curve 30-year rate, 10/05/2026
  (issuing authority, via `tools/sources.py` inside `tools/run.py`).
- **Filings read** (operator rule 4):
  - 10-K FY2025 (53 weeks to 2026-01-03, filed 2026-03-04, `0001760965-26-000014`);
  - 10-Q Q2 FY2026 (`0001760965-26-000059`);
  - proxy filed 2026-03-09 (`0001760965-26-000020`; fetched and searched, not read in full because Q5 was not reached);
  - 10-Ks FY2019 to FY2024 (`0001760965-20-000010`, `-21-000009`, `-22-000008`, `-23-000007`, `-24-000013`, `-25-000011`);
  - the Form 10 information statement, Exhibit 99.1 to the 10-12B/A of 2019-04-30 (`0001193125-19-127045`);
  - 8-Ks `0001760965-26-000035` (Lee sale), `-26-000064`, `-26-000057`, `-26-000045`, `-26-000039`, `-26-000006`,
    `-25-000090`, `-25-000086` and `-25-000075`.
- **One figure cross-checked against the filed statement:** cash from operations for FY2025 is $455.8M in the 10-K's MD&A
  cash-flow table (`0001760965-26-000014`), in the XBRL fact, and in `tools/run.py`. They agree.
- **`tools/run.py` arithmetic lines only** (v4 rule text it prints is ignored, Part VII). Owner cash after stock pay and all
  capital spending (property plus software) is shown below, in $M. I checked each line against the XBRL facts of the 10-Ks
  named.

  | FY | OCF | SBC | capex + software | D&A | owner cash (capex basis) | D&A basis |
  |---|---|---|---|---|---|---|
  | 2020 | 242.0 | 15.9 | 62.4 | 34.5 | 163.7 | 191.6 |
  | 2021 | 283.9 | 38.5 | 36.9 | 36.6 | 208.5 | 208.8 |
  | 2022 | 83.6 | 21.9 | 28.4 | 37.1 | 33.3 | 24.6 |
  | 2023 | 356.5 | 16.7 | 37.4 | 38.0 | 302.4 | 301.8 |
  | 2024 | 368.2 | 26.6 | 22.1 | 42.6 | 319.5 | 299.0 |
  | 2025 | 455.8 | 39.1 | 25.1 | 47.8 | 391.6 | 368.9 |

  - **Five-year means (2021 to 2025):** $251.1M on the capex basis and $240.6M on the D&A basis (the same as `run.py`'s
    "other window"). The three-year window that `run.py` puts first ($337.8M) begins after the 2022 inventory build, and it
    is not used as the base (**[L2005-003]**).
  - **FY2019 is excluded:** its OCF of $777.8M is swollen by the settlement with VF of receivables sold before the spin
    (10-K FY2019 MD&A).

---
## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the analyst's habit of writing contrary evidence down "in the first 30 minutes"
**[M1997-127]**. The filings tell two opposite stories: Wrangler's profit doubled after 2019, and the company as a whole
shrank against its largest customer. A reader who wants the first story can stop reading early. No macro view enters, for or
against: tariffs appear below only as a property of the business (an importer that sources 77% of its units from contract
factories abroad), not as a forecast **[M2004-102]**. The price is used only as a price: "It just tells us prices."
**[M2006-077]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Kontoor's own competition paragraph (10-K FY2025, Item 1) reads: "The apparel industry is highly competitive, highly
   fragmented and characterized by low barriers to entry", and "we see an increasing reliance on private label apparel created
   for our largest retailer partners."
2. Lee's revenue fell from $1,068.2M in 2016 (Form 10) to $750.4M in 2025, and its segment margin fell from 14.1% to 9.2%.
   The company has now agreed to sell Lee to an affiliate of Authentic Brands Group for $750M in cash plus an earnout of up to
   $250M (8-K `0001760965-26-000035`).
3. Sales to Walmart are about flat in dollars over nine years, about $934M in 2017 and about $946M in 2025 (the percentages
   are rounded). Walmart's own revenue rose from $485.9B (FY ended January 2017) to $713.2B (FY ended January 2026), a 47%
   increase (WMT 10-Ks `0000104169-17-000021` and `0000104169-26-000055`, XBRL).
4. Company units sold fell from about 170M (2019) to about 147M (2024). Revenue per unit rose.
5. Gross margin in FY2024 carried "90 basis points from lower pricing" (10-K FY2024 MD&A).
6. In the other direction, Wrangler's segment profit rose from $215.0M (2019) to $440.0M (2025), and its margin rose from
   14.2% to 23.0%.
7. The risk-factor sentence of the FY2025 10-K says Walmart was 30% of revenue "in 2025, 2024 and 2023". The audited segment
   note of the same filing says 30% in 2025 and 36% in 2024 and 2023, which agrees with the FY2024 10-K. I take the note.
   This is a drafting error in the filing, resolved by the note, and recorded.

## THE STANDING RULE
A part-interest bought for cash and held without borrowed money puts the buyer at no risk of ruin from this name: "We are
never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**, and "borrowed money has no
place in the investor's tool kit" **[L2014-005]**. Not engaged.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What is being bought.** After the Lee sale closes (expected in the second half of 2026), the company is three things:
  - **Wrangler:** about $1.9B of revenue. Segment profit was $440.0M in FY2025 and $260.7M in H1 2026.
  - **Helly Hansen:** bought on 2025-05-31 for C$1.3B ($957.5M), "funded by indebtedness and cash on hand" (10-K FY2025).
    Its segment profit was $31.8M on $459.7M of revenue in seven months of 2025, and $21.5M on $272.3M in H1 2026.
  - **The sale proceeds:** $750M of cash, which management says it will use for buybacks and debt repayment (10-Q Q2 FY2026).
- **The test.** Can I have "a reasonable fix on about what the earning power and competitive position will look like in five
  or 10 years" **[M2012-065]**, and see "where the business will be in 10 years" **[M2000-037]**?
- **Key variables.** Wrangler's units and price at mass and Western retailers, Helly Hansen's margin, and the cost of
  imported product.
- **Is it a forecast about technology?** No. The product is old, and the forecast is about customers and retailers, the kind
  of thing that is "much more of a consumer products business" **[M2017-019]**.
- **Cautions, written down.** First, "it’s easy to sort of think you understand retail" **[M2014-052]**. Second, the past
  statements tell less than usual about the future ones (test 3, **[M2008-033]**): Lee is a third of the history and is
  leaving, and Helly Hansen has thirteen months in these filings.
- **Helly Hansen, read as a part** (the holding-company CONVENTION). It is a technical outdoor and workwear apparel brand. I
  can understand it in kind. What I cannot foresee is its castle, and that is Q2's question, not Q1's.
- **VERDICT: IN.** The economics are of a kind I can picture (consumer apparel brands sold through retailers). The doubt
  that remains is about the castle, which Q2 owns.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is "why is that castle still standing?" **[M1995-038]**. The test starts from the attacker: "The dynamics of
capitalism guarantee that competitors will repeatedly assault any business" **[L2007-004]**.

**The segment record, from the Form 10 (2016 to 2018) and the 10-Ks (2019 to 2025), $M:**

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Wrangler revenue | 1,631.5 | 1,619.3 | 1,602.2 | 1,518.1 | 1,349.4 | 1,575.2 | 1,745.8 | 1,754.1 | 1,806.0 | 1,914.6 |
| Wrangler profit | 325.2 | 280.3 | 266.0 | 215.0 | 244.9 | 294.2 | 321.2 | 307.5 | 366.3 | 440.0 |
| Lee revenue | 1,068.2 | 1,005.8 | 960.2 | 882.3 | 687.6 | 887.1 | 874.4 | 842.5 | 790.6 | 750.4 |
| Lee profit | 150.9 | 107.2 | 92.7 | 68.2 | 37.9 | 128.3 | 121.1 | 98.1 | 89.7 | 68.9 |
| Company revenue | 2,926.5 | 2,830.1 | 2,764.0 | 2,548.8 | 2,097.8 | 2,475.9 | 2,631.4 | 2,607.5 | 2,607.6 | 3,152.5* |
| Gross margin % | 41.5 | 41.4 | 40.3 | 39.4 | 41.2 | 44.7 | 43.1 | 41.7 | 44.5 | 45.2* |

\*2025 includes seven months of Helly Hansen ($475.5M of revenue) and a 53rd week (about 2%). Before the spin, the company's
revenue was $3,011.5M in 2014 and $3,008.8M in 2015 (Form 10, selected data).

**The castle tests, each with its filing fact:**
- **1. Key factors, and how permanent.**
  - The key factors are the brand names and the place on the retailer's shelf. Wrangler is 79 years old and Lee 137
    (10-K FY2025).
  - Age did not protect Lee. A brand older than Wrangler lost 30% of its revenue in nine years and is being sold. "for every
    Inevitable, there are dozens of Impostors" **[L1996-031]**.
- **2. Would it stand without the lord?** The record does not test this.
  - Management turned over: a new COO in 2025, and the CFO became President in 2026.
  - The business ran Project Jeanius, a multi-year transformation with restructuring and transformation charges of $38.3M in
    2024 and $80.6M in 2025.
  - Part of Wrangler's margin gain is credited by the filer to Jeanius, that is, to the lords' cost work, not to the castle.
- **3. The money test.** Could a well-funded attacker take the castle?
  - The attacker is already inside the gate: "Many of our largest customers have already developed significant private label
    brands under which they design and market apparel and accessories that compete directly with our products" (10-K FY2025,
    risk factors).
  - "Sales to our wholesale customers are generally on a purchase order basis and not subject to long-term agreements" (same).
  - "there are some industries that are just never going to have barriers to entry" **[M2012-106]**, and the filer puts its
    own industry there in so many words: "low barriers to entry".
- **4. Pricing power.**
  - FY2024 gross margin carried "90 basis points from lower pricing".
  - In FY2025 "pricing adjustments" did not offset tariffs and product costs (a 60 basis point net drag, 10-K FY2025).
  - The FY2026 gains come from mix, Jeanius, a tariff refund receivable ($53.7M recognized) and pricing taken together.
  - The strength of a business shows in "the agony they go through in determining whether a price increase can be sustained"
    **[M2005-020]**. The filings show price given back in 2024, not taken.
- **5. Unit volume and share of mind.**
  - Units sold were about 170M (2019), 140M (2020), 152M (2021), 157M (2022), 149M (2023) and 147M (2024).
  - 2025 was about 150M, including seven months of Helly Hansen (10-Ks, Item 1).
  - "we want a lot more unit cases sold" **[M1999-054]**. Units here fell about 13% from 2019 to 2024, and revenue held
    only by price and mix.
- **6. The low-cost position.**
  - 77% of 2025 units came from about 330 contract factories in 28 countries, and 23% from owned plants in Mexico. Part of
    the owned capacity was closed in 2025.
  - No filing fact shows Kontoor as the lowest-cost maker against the retailers' own labels, which use the same contract base.
- **7. The brand against the retailer.** This is the decisive test.
  - The rows: "the value of having the brand moves over to the retailer from the product itself" **[M2001-090]**; "the
    retailer is going to use all the pressure they’ve got" **[M2015-038]**; and, of Buffett's own error, "we did underestimate,
    not what the consumer is doing so much, but what the retailer is" **[M2019-041]**.
  - Walmart was 30% to 38% of revenue every year from 2017 to 2025 (10-Ks), with the top ten customers at 53% to 62%.
  - The second-largest customer was 12% in 2025 (10-K FY2025, Note 4).
  - A brand sold mostly at Walmart, "even if you have distribution through something like Walmart, who has Sam’s Cola"
    **[M2023-073]**, is not shown to be asked for by name. No filing gives a price premium of Wrangler over the store labels.
- **8. Over the low bid?** "it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**. Wrangler at a
  mass merchant sits near the low bid. No filing fact either way.
- **9. Ask the competitors.**
  - The filer names Ariat, Carhartt, Columbia, Dickies, Levi's, Patagonia, The North Face, Tommy Hilfiger and the
    retailers' private labels.
  - Its own words on private label are quoted at test 3 above.
- **10. Widening or narrowing?** "whether it’s likely to widen further or shrink on you" **[M1999-108]**.
  - Wrangler alone widened in profit and margin after 2019.
  - Against its largest customer and the market, the company narrowed (the competitor row below).
  - The pattern is "the industry retains its excellent economics, but has lost still another notch" **[L1995-023]**.
- **11. What could destroy, modify or reduce it** **[M2000-014]**.
  - A purchase-order decision by Walmart to shift denim shelf to its own labels: "one competitor is frequently enough to ruin a
    business" **[M2012-108]**.
  - A tariff regime on imported, labour-heavy product.
  - Helly Hansen's thin margin. Its segment margin was 6.9% in 2025 and 7.9% in H1 2026. A castle earns "a high return on
    capital employed for a very long period of time" **[M2007-023]**, and $957.5M paid for about $50M of annual segment
    profit before corporate cost is not that return.

**The competitor row** (same metric, the competitors' own filings, XBRL of the 10-Ks; whole span):

| Company (customer or competitor) | Revenue, first year | Revenue, last year | Change | Gross margin, first to last | Accession (last) |
|---|---|---|---|---|---|
| Kontoor, whole (Wrangler, Lee, other) | 2,926.5 (2016) | 2,607.6 (2024) | -11% | 41.5% to 44.5% | `0001760965-25-000011` |
| Wrangler segment | 1,631.5 (2016) | 1,914.6 (2025) | +17% | segment margin 19.9% to 23.0% | `0001760965-26-000014` |
| Lee segment | 1,068.2 (2016) | 750.4 (2025) | -30% | segment margin 14.1% to 9.2% | `0001760965-26-000014` |
| Levi Strauss (LEVI) | 4,552.7 (FY2016) | 6,282.0 (FY2025) | +38% | 51.2% to 61.7% | `0000094845-26-000008` |
| Gap Inc., Old Navy Global (a retailer's own brand) | 6,814 (FY2016) | 8,657 (FY2025) | +27% | not split by brand | `0001628280-26-018573` |
| VF Corp (former parent; chose to separate jeanswear in 2019) | 12,019 (2016) | 9,605.2 (FY ended March 2026) | not comparable (divestitures) | n/a | `0000103379-26-000030` |
| Walmart (customer, total revenue) | 485.9B (FY ended January 2017) | 713.2B (FY ended January 2026) | +47% | n/a | `0000104169-26-000055` |

- **Reading of the row.** Over the whole span:
  - the premium jeans brand (Levi) grew and widened its gross margin by about ten points;
  - a retailer's own value brand (Old Navy) grew 27%;
  - the largest customer grew 47%.
- Kontoor's whole business shrank before the Helly Hansen purchase. Wrangler, the best part, grew 17% in nominal dollars in
  nine years. That is less than every comparator in the row.
- **Private-label jeans.** Walmart's and Target's own-label denim is not broken out in their filings. This could not be read
  from primary documents.

**The verdict and its cause.**
- **Lee** is a castle shown filling in on the evidence (revenue -30%, margin -5 points, now sold). That is OUT on its own.
- **Wrangler** is not shown filling in. Its profit and margin rose. But its gate is held by retailers who buy season by
  season on purchase orders and sell their own labels beside it. The filer itself calls the industry one of low barriers
  and rising private label. Its share of its largest customer's spending fell by about a third in nine years.
- **Helly Hansen** has no castle shown at a 7% to 8% margin, and thirteen months of history in these filings.
- **The deciding question:** will Wrangler hold its place and its terms on the shelves of Walmart and the Western and
  workwear retailers against their own labels for ten to twenty years? That question is important and, from where I stand,
  unknowable: "If something’s important but unknowable, forget it." **[M2006-076]**. The moat is tenuous: "We don’t know how
  to valuate that, and therefore we leave it alone." **[M2000-019]**.
- **Why NATURE and not WORK.** The answer is set each season by the retailer's purchase orders. Walmart does not disclose its
  own-label denim. Kontoor's own management misjudged its sister brand: it revived Lee's profit to $128.3M in 2021 and is
  selling it five years later. The people inside the industry would not write this forecast down **[M2000-105]**. In
  **[L1993-023]**'s words, "in other cases the nature of the industry would be the roadblock". More reading of public
  documents will not settle a retailer's ten-year shelf decision **[M2008-086]**.
- **Why not OUT for the whole.** A castle "shown on the evidence to be filling in" is OUT. The Wrangler record does not show
  that; it shows a castle whose future cannot be judged.
- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**. The run closes here. Q3 to Q12 are NOT REACHED as clearances. What follows
  under them is reporting at the owner's request.

---
## COMPUTATION: NOT A CLEARANCE
*(Operator rule 3. Everything below Q2 is arithmetic and reading recorded after a closing STOP. It carries no entry language.
Heading written with a colon in place of the protocol's dash, by the operator's standing no-dash rule.)*

### Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (recorded only)
- **Little fixed capital.** Capital spending including software was $22M to $62M a year against D&A of $35M to $48M
  (table above). Guidance is about $30M for 2026 (10-Q).
- **Working capital is the capital that moves.** Inventory was $363M at 2021 year end and $597M at 2022 year end, then fell
  back to $390M in 2024. That swing is why FY2022 owner cash was $33M.
- **Acquired capital.** The large capital the business put in was bought, not built: $957.5M for Helly Hansen. Its first
  thirteen months earned roughly 5% to 6% pre-tax at the segment line, before corporate cost.

### Q4: THE NUMBERS. NOT REACHED (recorded only)
**Balance sheets first, ten year ends** **[M2025-032]** ($M; `tools/run.py` table, read against the filed statements;
2016 and 2017 equity is VF's parent investment):

| year end | equity | goodwill | intangibles | cash | receivables (on BS) | sold receivables (off BS) | inventory | long-term debt |
|---|---|---|---|---|---|---|---|---|
| 2016 | 1,393 | n/a | n/a | 87 | n/a | n/a | n/a | 0 |
| 2017 | 1,358 | 219 | n/a | 81 | n/a | n/a | n/a | 0 |
| 2018 | 1,723 | 215 | 53 | 97 | 253 | 544.9 (due from VF) | 474 | 0 |
| 2019 | 69 | 213 | 17 | 107 | 228 | 188.1 | 458 | 913 |
| 2020 | 85 | 213 | 16 | 248 | 231 | 127.1 | 341 | 888 |
| 2021 | 148 | 212 | 15 | 185 | 290 | 170.6 | 363 | 791 |
| 2022 | 251 | 210 | 13 | 59 | 226 | 246.0 | 597 | 783 |
| 2023 | 372 | 210 | 12 | 215 | 218 | 197.7 | 500 | 764 |
| 2024 | 400 | 209 | 11 | 334 | 244 | 178.2 | 390 | 740 |
| 2025 | 565 | 531 | 450 | 108 | 276 | 261.4 | 567 | 1,135 |
| June 2026 | 619 | 461* | 448* | 58 | 221* | 239.0* | 526* | 1,144 incl. current |

\*Continuing operations only; Lee is held for sale ($390.5M of assets, $140.6M of liabilities).

What moved, and what the figures do not say:
- **The spin.** Equity fell from $1,723M to $69M in 2019. The company was spun with about $1B of debt.
- **Rebuilding.** Equity was rebuilt slowly, because dividends ($55M to $116M a year) and buybacks ($25M to $86M a year)
  took most of the earnings.
- **Inventory against sales.** Inventory jumped to 22.7% of sales in 2022 against 14.7% in 2021, then was cleared by
  what the filer calls proactive inventory management actions, which cost 2023 gross margin. That is the tell of **[M1995-064]**, "inventories
  look out of line", explained by the filer and since reversed.
- **What the balance sheet does not say: the receivables sold.** The receivables on the balance sheet understate the
  receivables the business carries. $178M to $261M a year end are sold to banks under a purchase agreement. The proceeds sit
  in operating cash, and funding fees were $11.7M to $12.0M a year in 2023 and 2024.
- **The 2025 factoring rise.** The sold balance rose $83.2M in 2025, partly under a new agreement of 2025-12-12. That $83.2M
  is a financing inflow counted as operating cash.
- **Goodwill and trademark.** They rose $570M with Helly Hansen (goodwill $320.7M and trademark $400.0M of the price). The
  May 2026 impairment test passed (10-Q Note 11).

The real costs:
- **Stock pay** is a real cost **[L2015-003]** and is deducted ($16.7M to $39.1M a year).
- **Depreciation** is "almost always true costs" **[L2015-004]**. The capex basis is used, with the D&A basis shown beside it.
- **Restructuring is recurring:**

  | year | 2016 | 2017 | 2018 | 2019 | 2020 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|
  | restructuring and transformation charges, $M | 21.6 | 9.5 | 20.4 | 18.6 | 14.7 | 38.3 | 80.6 |

  - 2021 to 2023 also carry charges (the EMEA restructuring) that are not tagged above.
  - The 2025 figure is beside $50.8M of acquisition costs.
  - To tell owners to ignore charges like these "is misleading" **[L2016-007]**. They are left in owner cash, which already
    bears them.
- **The tariff refund.** The 2026 margin includes a $53.7M tariff refund receivable, of which $29.0M relates to 2025 tariffs.
  That is non-recurring.
- **Earnings definition.** Earnings are taken "after interest, taxes, depreciation, amortization and all forms of
  compensation" **[L2021-003]**.

**Recast owner cash** (my recast, shown in `value.py`). Subtracting each year's rise in sold receivables, which is borrowing
against receivables and not operating cash, gives 2021 to 2025: 165.0, -42.1, 350.7, 339.0, 308.4. The five-year mean is
**$224.2M** (2020 to 2025: $224.3M).

Not confusion. The filer discloses the program fully, and one drafting error (the Walmart percentage) is resolved by the
audited note. If Q4 had been reached, it would WEIGH neither for nor against on confusion; recurring restructuring and the
factoring would weigh against the reported cash.

### Q5 and Q6: NOT REACHED (recorded only)
**Management and board, from the 8-Ks:**
- The CEO is also Chairman (8-K `0001760965-26-000057`).
- The COO left in 2025 with 18 months of salary ($1.35M; `0001760965-25-000086`) and joined the board in 2026
  (`0001760965-26-000045`).
- The board grew from six to nine in 2026.
- An executive severance plan was adopted on 2026-02-12 (`0001760965-26-000006`).
- The proxy was fetched but not read for these questions.

**Buybacks:**
- The $750M programme of 2026-05-06 names no price.
- **[L2016-002]** notes that announcements "almost never refer to a price above which repurchases will be eschewed".
- Prices actually paid: about $71 a share in 2024 ($85.0M for 1.2M shares); about $83 and $71 in H1 2026 ($25.0M for 0.3M
  and $50.0M for 0.7M).
- Those prices sit around or above the bottom of the recast range below ($72.48).

**The Helly Hansen deal:** paid in cash and debt, not stock, so the all-stock STOP does not arise.

### Q7: WHAT IS IT WORTH. COMPUTATION, NOT A CLEARANCE
**Method.** A range, not a point **[L2000-024]**, discounted at the long government rate **[L2000-021]**, **[M1996-025]**,
under the Q7 CONVENTION:
- five-year mean owner cash;
- carried ten years at the growth shown, then zero nominal growth;
- discounted at 5.66%;
- the two ends are the no-growth case and the shown-growth case.

**Growth shown (CONVENTION of this run, confessed).**
- Endpoint growth of owner cash, 2021 to 2025, is about 17% a year. It is an artifact of a poor base year **[L2005-003]**,
  of the Helly Hansen purchase and of factoring, so it is not used.
- I use the like-for-like growth of the business over the whole span instead: Wrangler segment revenue 2016 to 2025 is
  about 1.8% a year, rounded to **2%**. Whole-company revenue before Helly Hansen fell.
- Rationale: the convention forbids a rate above the growth shown, and this is the most generous growth the span shows
  for the part being kept.

| owner cash input ($M) | no growth | 2% for ten years, then flat |
|---|---|---|
| **recast, factoring-adjusted, 5-yr: 224.2** | **$3,961M, $72.48** | **$4,641M, $84.91** |
| capex basis as filed, 5-yr: 251.1 | $4,436M, $81.16 | $5,197M, $95.08 |
| D&A basis, 5-yr: 240.6 | $4,251M, $77.79 | $4,980M, $91.13 |
| whole-cycle variant (6-yr 2020 to 2025, recast): 224.3 | $72.50 | $84.94 |

- **(a) VALUE RANGE: $72.48 to $84.91 a share** on the recast owner cash, against **$64.19**. The ratio is 1.17 to one.
- **The as-filed range** ($81.16 to $95.08) is shown beside it.
- **The whole-cycle variant** (adding 2020, a year with the 2022 inventory build inside the five) barely moves the range.
- **Adjustments not in the range, named:**
  - Helly Hansen is in the base for seven months only.
  - Interest is higher after the 2025 borrowing: 2026 contractual interest is $58.0M against $35M to $40M a year in
    2021 to 2023.
  - Lee leaves for $750M. That is about 10.9 times its 2025 segment profit of $68.9M, before about $50M a year of overhead
    "previously allocated to the Lee business" that stays behind ($25.5M in H1 2026).
  - These pull in different directions. Their net is not estimated.

**(b) FAIR PRICE (CONVENTION of this run).** The price at or below which the central case clears the ~10% pre-tax floor
(**[M2003-149]**, **[L2002-020]**, **[M1994-004]**, qualified by **[M2003-151]**).
- **Floor basis:** the floor is set on equity, because owner cash is after interest.
- **Tax treatment:** owner cash is grossed up to pre-tax at the FY2025 effective rate of 24.3% (10-K FY2025 MD&A).
- **Central case:** the recast $224.2M at 1% growth, the midpoint of the two ends.
- **Formula:** the expected pre-tax return equals pre-tax owner cash divided by price, plus growth.
- **FAIR PRICE: about $60.21 a share.** On the as-filed $251.1M at 1%, it is $67.42.
- **Expected pre-tax return at $64.19:** 9.44% in the central case, which is below the floor. It is 10.45% on the as-filed
  cash.

**(c) CHEAP PRICE (CONVENTION of this run): about $36.24 a share.**
- **Rule:** half the bottom of the recast range.
- **Check:** at that price the recast owner cash alone yields 15% pre-tax with no growth, and the no-growth value at a rate
  200 basis points higher ($53.55) still sits far above it.
- **Rationale:** a price that needs no pencil **[M1996-084]**, **[M2009-005]**.

**What Q7 would have said.**
- The range is narrow, so not TOO HARD.
- The price sits about 11% below the bottom of the range: just below it, not a screamer **[M2009-005]**.
- The central case's expected return at the price is under the floor.
- Both convention closes point to **OUT** at Q7, had the file reached it.

### Q8 to Q10, Q12: NOT REACHED (recorded only)
- **Debt.** Debt at June 2026 is $1,144M (Term Loan A-1 $700M to 2030, Term Loan A-2 $50M, 4.125% notes $400M due November
  2029). Cash is $58.5M, and the $500M revolver is undrawn.
- **Coverage.** FY2025 pre-tax income was $293.3M against interest of $62.2M.
- **The criterion.** This is not "little or no debt" **[R1997-001]**. The debt must be related "to the ability to pay debt"
  **[M1995-104]**, and maturities may "actually be met by payment" **[L2010-020]**.
- **The Lee proceeds** would cut net debt by about two thirds, if they go to debt and not to the buyback.
- **Q12.** No named business.

---
## THE BOX
**TOO HARD (NATURE), at Q2.**
- **The deciding question.** Will Wrangler keep its place and terms on retailers' shelves against their own labels for ten
  to twenty years? That is a forecast that the retailers, buying on season-by-season purchase orders, and the industry's own
  insiders (who revived and then sold Lee) would not write down.
- **Lee's castle** is shown filling in. **Helly Hansen's** is not shown at all.
- **Recorded only:** recast range $72.48 to $84.91 against $64.19; fair about $60.21; cheap about $36.24 (all computation).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not** written question by question: the first session read and computed
  before writing, and was stopped at the session limit with only the template on disk. Not committed (the brief forbids
  commits). A breach of the write-early form, confessed.
- [x] Every v5 id was checked against `principle_ledger_v5.csv` by a script, and every quoted fragment beside an id was
  checked as a substring of that row. Every filing fact carries its accession.
- [x] The order was kept. Q2 closed the file. Nothing after it is a clearance, and all of it sits under COMPUTATION.
- [x] Owner cash is after stock pay and all capital spending, never a net-income proxy. The sovereign comes from the US
  Treasury. The price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found **[M1997-127]**. It is the numbered list under the foundations.
- [x] No point-in-time anchor: this is a live run.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py`: result recorded in the reply; no commit made.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**Two conventions disagree at the price.**
- The Q7 range is discounted at the sovereign (5.66% today), so the no-growth case values the recast owner cash at $72.48,
  above the price.
- The ~10% pre-tax floor, applied to the same cash, quits the name at the same price (a 9.44% expected return).
- A reader taking only the range would see a discount; a reader taking only the floor would see a pass.
- The framework says a price above the range closes through the floor. It does not say which governs when the price is
  below the range and still under the floor. I reported both and let the floor decide what Q7 would have said.

**A business in mid-portfolio change.** The framework has no rule for a company that is selling one third of what the filings
describe (Lee, held for sale) while holding a thirteen-month-old acquisition.
- The Q7 convention's five-year mean then values a business that will not exist.
- Q2 has no rule for judging the castle of the part kept when the customer data (Walmart's share) are not split by brand.
- I judged Wrangler on its segment data, read the customer concentration at the company level, and named the adjustments
  without netting them.

**Sold receivables.** The framework names the real costs at Q4. It does not say whether a rise in sold receivables is
operating cash or financing. I treated it as financing (a CONVENTION of this run), which moved the mean owner cash from
$251.1M to $224.2M and the fair price from $67.42 to $60.21.

**The dash.** The protocol's required heading "COMPUTATION" with an em dash collides with the operator's standing no-dash
rule. I used a colon.
