## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (Q2 closed the file OUT). The facts already found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED** as a verdict. The template asks that the eight to ten years of balance sheets be read even when the file closes before Q4; they were read, and the reading is set down here as a record, with no verdict on the accounts.

**COMPUTATION, NOT A CLEARANCE: the balance sheets, FY2017 to FY2025 and 2026-06-30, read before the income account** **[M2025-032]**. Source: `tools/run.py`'s ten-year table (first-filed XBRL, accessions listed in `runpy_out.md`), checked against the filed balance sheets of the FY2025 10-K and the Q2 2026 10-Q; USD millions.

| year-end | total assets | equity | of which retained earnings | goodwill + intangibles | inventory | receivables | debt (current + long-term) | cash |
|---|---|---|---|---|---|---|---|---|
| 2017 | 629 | 293 | 268 | 310 | n/a | 98 | 173 | 1 |
| 2019 | 846 | 363 | 334 | 408 | n/a | 71 | 270 | 1 |
| 2021 | 919 | 417 | 328 | 357 | 323 | 77 | 285 | 1 |
| 2022 | 1,000 | 450 | 351 | 340 | n/a | 103 | 286 | 0 |
| 2023 | 1,350 | 617 | 385 | 466 | n/a | 128 | 429 | 8 |
| 2024 | 1,735 | 988 | 392 | 688 | 434 | 158 | 430 | 29 |
| 2025 | 2,029 | 1,439 | 396 | 937 | 554 | 191 | 293 | 69 |
| 2026-06-30 | 4,397 | 2,933 | 448 | 2,763 | 867 | 275 | 947 | 75 |

(Inventory at 2021-12-31 is the FY2021 10-K's $322.7M; inventory and receivables for 2024 and 2025 are continuing operations from the FY2025 10-K, the 2024 figures excluding the Fleet segment held for sale ($142.3M of inventory, $39.5M of receivables); the other 2024 columns are first-filed; n/a where the tool's table carries no inventory column.)

What the figures say, and what they do not:
- **Equity grew by selling shares, not by keeping earnings.** Equity rose from $293M to $2,933M; retained earnings rose $180M over the same span, from $268M to $448M, and were nearly flat from 2019 ($334M) to 2025 ($396M). Additional paid-in capital went from $92.6M (2022-12-31) to $1,041.5M (2025-12-31) to $2,484.1M (2026-06-30) (statements of equity).
- **The capital is mostly purchased goodwill and intangibles.** At 2026-06-30 goodwill ($1,810.4M) and intangibles ($952.1M) are $2,762.5M against equity of $2,933.4M; tangible equity is about $171M. Purchased goodwill is "forget it" for judging the business and counted for judging the capital allocation, "because we paid for it" **[M2011-060]**.
- **Inventory is half a year's revenue.** Continuing inventory was $553.8M at 2025-12-31 against FY2025 revenue of $1,112.3M; in the first half of 2026 inventory rose by $115.6M net of acquisitions (10-Q cash-flow statement) while organic revenue growth was "approximately 14%" in Q2. The rows ask whether "inventories look out of line, you know, with sales" **[M1995-064]**; for a distributor that stocks parts for OEM programs a high ratio is the model, and the 2021 provision shows what happens when demand does not meet it.
- **Debt moved with the deals.** $173M (2017) to $430M (2024), down to $293M after the October 2025 offering, up to $947M at 2026-06-30 after the $900M term loan B (8-K of 2026-05-07).
- **Cash was never held.** Year-end cash was under $10M in every year 2017 to 2023.
- **What they cannot say:** the balance sheets do not separate the continuing business from the sold segments before FY2024, and the held-for-sale lines of 2024 show the Fleet segment alone carried $142.3M of inventory and $63.2M of goodwill.

The real-cost facts and the reporting habits found are recorded under AFTER THE STOP (Q4 and Q5 headings), not weighed.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Integrity facts found are recorded under AFTER THE STOP, not judged; the box line carries the flag.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Q6's buyback test would need the bottom of Q7's range; the company made no repurchases in FY2025 other than 42,623 shares withheld for taxes (FY2025 10-K, Item 5), so there is no buyback line to write back. Facts on issuance and deals are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED** as a clearance. The owner's two reporting figures are computed below under the hard sequence, by Q7's range convention in full, at the brief's request.

**COMPUTATION, NOT A CLEARANCE.** Arithmetic in `scripts/q7.py`, output in `q7_out.txt` (research folder). USD millions unless per share.

*Inputs.* Discount rate 5.43% (US Treasury 30-year, 10/15/2026). Price $164.08 (aggregator, flagged). Share basis 31,927,924 (Step 0). Net debt at 2026-06-30: borrowings $32.0M current plus $915.0M long-term, less cash $75.4M, **$871.6M** (10-Q balance sheet; it already carries the PAG financing; no subsequent event is stated in the 10-Q; operating leases of $78.6M long-term left out, as the convention says; the PAG earn-out obligation of $33.9M is a liability of uncertain amount payable in cash or stock and is shown beside, not added). Tax: the company's own effective rate each year (FY2023 23.6%, FY2024 18.5%, FY2025 22.5%, from the FY2025 10-K); PAG at 25% (its own 2025 provision was $5.6M on $22.3M pre-tax, 25.3%). No carryforward shelter that runs out inside ten years: a text sweep of the FY2025 10-K for "net operating loss" and "carryforward" found only the accounting-policy sentence, so no shelter is priced.

*The literal window* (the brief's "literal window shown beside"): consolidated owner cash as filed, operating cash flow less stock pay less capital spending, FY2021 to FY2025: -$32.0M, -$7.6M, -$48.2M, -$60.1M, -$7.1M; average **-$31.0M** a year (FY2021 and FY2022 from the FY2022 10-K: OCF -$17.6M and $8.1M, stock pay $3.9M and $4.5M, capex $10.5M and $11.2M). On a negative base the literal window values the business at nothing; it carries the two sold segments and is not the business now.

*Specific (c), the serial acquirer.* Net purchases over FY2021 to FY2025 were $949.1M of acquisitions less $179.1M of segment sale proceeds, **$770.0M**, against owner cash before purchases that was negative in total over the window; purchases exceed half of owner cash before purchases, so the central figure is **the organic pair** (purchases left out, organic growth as the filer reports it), with the default pair beside. The default pair (acquisitions deducted, total growth credited) deducts $154M a year on average on top of a negative base: no positive value, said so.

*The base: the business now.* VSE continuing operations FY2023 to FY2025 (the three years the FY2025 10-K states on a continuing basis), plus PAG on its own audited 2024 and 2025 record (specific (c): a deal closed after the window and before the price date, valued on its own filed record with its financing in today's net debt). NorthStar ($10.1M, April 2026) is too small to matter and is left out. Owner cash on the all-equity basis: operating income (after stock pay, which is expensed in it) plus non-cash charges that are not the business's (the $29.2M Fleet earn-out remeasurement in FY2025; the $12.2M lease abandonment charge in FY2024), taxed at the company's rate, plus D&A, less capital spending, less the increase in working capital. Continuing D&A and capex are the consolidated figures less the discontinued figures the FY2025 10-K's Note 3 gives; the working-capital change is the consolidated one (the 10-K does not segregate it; said so).

| | VSE 2023 | VSE 2024 | VSE 2025 | PAG 2024 | PAG 2025 |
|---|---|---|---|---|---|
| owner cash after all spending (working capital included) | -54.4 | -41.6 | -3.0 | 43.4 | 63.1 |
| owner cash after maintenance only (capex at depreciation; working capital as growth spending) | 50.1 | 75.5 | 118.0 | 55.1 | 85.3 |
| revenue | 544.0 | 786.3 | 1,112.3 | 472.0 | 595.6 |

*Specific (e), the maintenance case central.* The filing allows the guess: MD&A ties inventory to "new distribution programs" and "large opportunistic inventory purchases", and the FY2021 10-K put "$80 million used for investments in new inventory to support recent distribution program wins and program launches"; so the working-capital build is treated as growth spending, and maintenance capex is guessed at depreciation (D&A less amortization of acquired intangibles: VSE $4.4M, $8.2M, $13.2M; PAG $6.4M, $9.5M), the stated guess **[M2000-144]**. Amortization of acquired intangibles is added back in the central case; since some of those intangibles are distribution rights and licences that run out, which "truly deplete" **[L2012-003]**, the case without the add-back is shown beside. Base, averaged: maintenance-only **$151.4M** (VSE $81.2M, PAG $70.2M); all-spending $20.3M; revenue $1,348.0M.

*Growth and its cost.* The filer reports organic growth once, "approximately 14%" for Q2 2026 (release `0000102752-26-000055`); it gives no organic figure for the window years. That figure is used as the growth case, carried ten years, then zero nominal growth (the four specifics). A like-for-like check from the 10-K's own pro forma tables (2024 base with Kellstrom, TCI and Aero 3 for the full year, $1,097.8M, against 2025 with Aero 3, $1,222.2M) gives about 11%, shown beside. The growth spending charged against the growth (specific (e)): working capital at the FY2025 year-end intensity, 50.2% of revenue (receivables, contract assets and inventories less payables and accrued expenses, $558.3M on $1,112.3M), plus growth capex of 3.5% of each added dollar of revenue (capex above depreciation against the window's revenue gain); 53.7 cents for each added dollar of revenue. After year ten the growth spending stops with the growth. Specific (f), the cap: the growth case holds owner cash at 11.2% of revenue throughout, below the highest share found in the filings read (combined 2025, 11.9%); no cut needed. Specific (a): FY2023 to FY2025 is the field's upswing; the Aviation segment's average operating margin over 2019 to 2025 was 8.5% against 11.9% over 2023 to 2025, so a full-cycle base would be lower; shown in words, not used. Specific (d): working capital is counted, as growth spending.

**Value range (organic pair, maintenance-only central, at 5.43%): $60.02 to $194.30 a share** against **$164.08**. The no-growth case is the bottom ($2,788M of enterprise value less $871.6M of net debt); the 14% growth case the top. The top is 3.2 times the bottom. Beside it: at 11% growth the top is $152.28; without the amortization add-back the range is $42.55 to $141.17; the literal window and the default pair give no positive value.

**The floor, tested first.** Expected return at $164.08 on the all-equity basis: 2.48% on the no-growth case, 6.05% on the 14% growth case (1.98% and 4.95% without the add-back). **No case in the range earns the floor of about ten percent at the price**, so the close is OUT whatever the width, by the floor convention tested before the width **[M2003-149]**. The three-to-one width test is not reached.

**Fair price (reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged, after the company's own tax. **All-equity basis (the central figure): $42.26 a share** (no-growth $20.12, growth $64.40). **Equity-only basis, beside: $56.23 a share** (owner cash after the company's after-tax interest, using the pro forma 2025 interest of $56.7M from Exhibit 99.3 at 25%: no-growth $34.09, growth $78.37). The equity-only figure is higher here because the pro forma interest, capitalized at ten percent, is smaller than the $871.6M of net debt the all-equity basis deducts. Without the amortization add-back the fair price would be $24.93 (all-equity) and $38.90 (equity-only). No cheap price is reported.

**VERDICT: NOT REACHED** (the computation would close OUT on the floor).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Debt facts are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** The draft would have the buyer do nothing: inaction is the default **[M1996-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** For the record: aviation parts distribution and repair is none of the businesses Q12 names.

---
## THE BOX
**OUT at Q2** (the castle shown open: the money test fails, the OEM-owned programs must be rebuilt one by one, price is a principal factor, and the field's distributors and repairers earned ordinary returns over 2019 to 2025). COMPUTATION, NOT A CLEARANCE: value range $60.02 to $194.30 a share against $164.08; no case earns the floor at the price; fair price $42.26 all-equity ($56.23 equity-only). **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2). Each with its source **[M1997-127]**.

**Bearing on Q3 (capital and its return).**
- Cash paid for acquisitions: FY2021 $53.3M, FY2023 $218.6M, FY2024 $283.1M, FY2025 $394.1M, H1 2026 $1,766.8M; plus stock to sellers of $30.3M (2024) and $238.0M (2026) (cash-flow statements and statements of equity).
- PAG was bought for an up-front $2.025 billion (plus up to $125M of earn-out) against 2025 income from operations of $92.4M and owner cash after all spending, on the all-equity basis computed above, of $63.1M (3.1% of the up-front price).
- Aviation segment operating income on segment assets less Aviation goodwill: 7.5% (2022), 10.8% (2023), 10.3% (2024); on total segment assets 5.7%, 7.5%, 7.2% (Q2 table).
- Working capital took more than the continuing business's after-tax operating cash in FY2023 and FY2024 (the all-spending row of the Q7 table is negative in every VSE year).

**Bearing on Q4 (the accounts).**
- The cash-flow statements of every year from FY2021 do not segregate discontinued operations (note (a) to each statement).
- Recurring "one-time" items: lease abandonment $12.2M and restructuring $4.2M (FY2024); earn-out remeasurement $29.2M (FY2025); acquisition, integration and restructuring costs $14.4M in H1 2026 (release reconciliation); a 2021 inventory provision of $24.4M.
- The company features adjusted EBITDA, "Adjusted EBITDA Margin", adjusted net income and adjusted EPS, and free cash flow, in every release read; the Q2 2026 release states "a change in the definition of Adjusted Net Income and Adjusted EPS (Diluted)", whose reconciliation now adds back "Amortization of intangible assets" ($18.5M in Q2) and "Stock-based compensation" ($4.0M in Q2). The rows on stock pay call leaving it out "the most egregious example" of real costs owners are told to ignore **[L2015-003]**; on featured adjusted figures, "makes us nervous" **[L2016-006]**. (Weighed at Q4 and judged at Q5 under section A; recorded only.)
- The company gives annual guidance and in the Q2 2026 release "Raises 2026 Guidance" for revenue growth (61% to 64%) and adjusted EBITDA margin (18.7% to 19.0%) **[L2019-006]** (recorded only).

**Bearing on Q5 (integrity, recorded, not judged).**
- The adjusted-figure definition change and the guidance above.
- Proxy (DEF 14A, `0000102752-26-000023`): the annual incentive pays on "revenue, adjusted EBITDA, and adjusted free cash flow"; the performance shares on three-year adjusted EBITDA; adjusted EBITDA excludes stock-based compensation; for 2025 the committee adjusted "the scope of the applicable financial metrics to exclude the Fleet segment and stock-based compensation expense [...] and to include the Turbine Weld acquisition". The proxy reports that some stockholders "suggested concerns with the use of retroactive adjustments to performance metrics in the 2024 compensation program", and that the committee is "evaluating if and when" to add a TSR or ROIC metric. None of the metrics charges for the capital used to buy the revenue and EBITDA it rewards.
- CEO total compensation $8,965,642 (2025), $4,945,400 (2024), $4,563,461 (2023), the 2025 figure including $300,000 of relocation costs (Summary Compensation Table).
- No restatement or material weakness: a text sweep of the FY2025 10-K and the Q2 2026 10-Q for "material weakness" and "restate" found only the auditor's standard wording, the cover-page check box (unchecked) and exhibit titles; Item 3 reports no material proceedings and notes that government agencies "from time-to-time" investigate the company's compliance, none named.

**Bearing on Q6 (the money and the owners).**
- Shares sold: 2,846 thousand for $129.1M (2023), 4,412 thousand for $325.2M (2024), 2,706 thousand at $170.00 for $441.1M (October 2025), 4,588 thousand at $188.00 for $829.0M (February 2026), 9.2M tangible equity units for $444.9M net (February 2026, up to 2.45M shares in 2029), and 1,415,752 exchangeable subsidiary shares to the PAG seller ($238.0M). Shares outstanding 12,817 thousand (2022) to 28,062 thousand (2026-06-30). Serial issuance is the candidate second STOP of Q6, Part A, "we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**, unresolved in the framework (recorded only). The shares were sold at $170.00 and $188.00, above both reporting figures computed here.
- The PAG deal was about 86% cash ($1.75 billion of $2.025 billion): an acquisition, not a merger, by the speakers' usage **[L2009-019]**; Q6's all-stock STOP does not apply on its facts.
- Dividend $0.40 a share a year, paid every year since 1973 (Item 5); no buybacks.
- The Fleet segment, sold for "up to $230 million", was written down by a $29.2M earn-out remeasurement in the year of sale.

**Bearing on Q9 (debt and exposures).**
- Debt at 2026-06-30 $947.0M on the balance sheet ($966.7M principal per the release), net debt $871.6M; a $900M term loan B at Term SOFR plus 2.00%, maturing 2033 with $9M a year of amortization; a $500M revolver to 2030; total net leverage and interest coverage covenants that do not apply to the term loan B (8-K of 2026-05-07). Pro forma 2025 interest $56.7M against pro forma operating income $118.4M (Exhibit 99.3); "pre-tax earnings/interest, not EBITDA/interest" **[L2012-002]** would be ($61.7M + $56.7M) / $56.7M, about 2.1 times on the pro forma.
- Earn-out obligation $33.9M (10-Q); one customer group about 20% of revenue (Item 1A).

---
