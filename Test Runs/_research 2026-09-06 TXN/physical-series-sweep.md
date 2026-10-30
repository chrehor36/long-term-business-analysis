# [E4-55] PHYSICAL SERIES SWEEP — TXN FY2025 10-K (TASK 4)

**Method (recorded so it can be replicated in under two minutes).** Target: the FY2025 10-K **primary
document** `txn-20251231.htm` (accession 0000097476-26-000059), converted to plain text by stripping the
inline-XBRL header, script and style blocks, mapping `</td>`→` | ` and block-close tags→newline, then
removing remaining tags and unescaping entities. Result: `txn-20251231_10K.txt`, 196,503 characters,
1,811 lines. Counting regex: `(?<![A-Za-z0-9])TERM(?![A-Za-z0-9])`, case-insensitive, whitespace inside a
multi-word term allowed to match `\s+`. This is a strict word boundary — it does **not** match plurals or
possessives of the term unless the term itself is plural.

## THE COUNTS

| term (as specified) | strict word-boundary count |
|---|---|
| "units shipped" | **0** |
| "unit volume" | **0** |
| "units" | **8** |
| "wafers" | **0** |
| "wafer starts" | **0** |
| "300mm" | **6** |
| "200mm" | **1** |
| "SKU" | **0** |
| "part numbers" | **0** |
| "catalog" | **0** |
| "customers" | **46** |
| "average selling price" | **0** |
| "ASP" | **0** |
| "utilization" | **2** |
| "capacity" | **22** |

Supplementary counts run because a strict boundary would otherwise hide a real occurrence:

| variant | count |
|---|---|
| "unit" (singular, strict) | 5 |
| "unit" as a prefix/stem (incl. "United", "unit-") | 33 |
| "per-unit" | 1 |
| "wafer" (singular, strict) | 10 |
| "average selling prices" (plural — the actual filed form) | **1** |
| "SKUs" | 0 |
| "part number" (singular) | 0 |
| "capacities" | 2 |
| "shipment" / "shipments" | 3 / 1 |
| "volume" / "volumes" | 1 / 1 |
| "output" | 4 |
| "die" | 0 |
| "transistor(s)" | 2 |
| "chips" | 28 — **but 26 of these are "CHIPS Act"**; only 2 refer to semiconductor chips |
| "150mm" | 3 |

## ABSENCE IS THE FINDING — reported explicitly

**Zero occurrences of: "units shipped", "unit volume", "wafers", "wafer starts", "SKU", "SKUs",
"part number", "part numbers", "catalog", "ASP", "die".** "average selling price" is zero in the singular
and appears exactly once in the plural, inside a risk factor, with no number attached.

The eight "units" hits are **all** restricted stock units and stock units — none is a product unit:

- L549: "A portion of net income is allocated to unvested restricted stock **units** (RSUs) on which we pay dividend equivalents."
- L838: "…because the restricted stock **units** (RSUs) we grant are participating securities…"
- L905: "…annual grants of stock options and RSUs … and the issuance of TI common stock upon the distribution of stock **units** credited to director deferred compensation accounts."
- L1690 (×2): "(b) Restricted stock **units** and stock **units** credited to directors' deferred compensation accounts are settled in shares of TI common stock on a one-for-one basis. … Accordingly, such **units** have been excluded for purposes of computing the weighted average exercise price."
- L1691: "…awards may be granted in the form of restricted stock **units**, options or other stock-based awards…"
- L1692: "…5,987,019 shares for issuance upon vesting of outstanding grants of restricted stock **units**…"

The single "per-unit" occurrence is an accounting-allocation phrase, not an output measure (Note 1, L744):
> "Costs incurred by our centralized manufacturing and support organizations, including depreciation, are
> charged to the operating segments, including those in Other, on a **per-unit** basis."

**Conclusion: TXN's FY2025 10-K contains no unit-volume series, no wafer-start series, no ASP series and
no SKU count. There is no physical quantity anywhere in the document from which revenue can be
decomposed into price × quantity.** The company explicitly declines to give the decomposition and instead
asserts the direction (MD&A, L402):
> "Unless otherwise noted, changes in our revenue are attributable to changes in customer demand, which
> are evidenced by fluctuations in shipment volumes."
— an assertion of causality with no shipment-volume figure disclosed anywhere in the filing to evidence it.

## EVERY SENTENCE IN THE 10-K CARRYING AN ACTUAL PHYSICAL NUMBER

Exhaustive. These are the only ones.

1. **Product count** (Item 1, L133):
> "This broad portfolio includes **more than 80,000 products** that are integral to almost every type of
> electronic equipment."

2. **Customer count** (Item 1, L202):
> "We sell our products to **over 100,000 customers**. Our customer base is diverse, with about half of
> our revenue derived from customers outside of our largest 50."

3. **The 300mm cost ratio — the only manufacturing-economics number in the document** (Item 1, L208):
> "We have focused on creating a competitive manufacturing structural cost advantage by investing in our
> 300mm capacity, as an unpackaged chip built on a **300mm wafer costs about 40% less** than an unpackaged
> chip built on a **200mm wafer**."

4. **Headcount and turnover** (Item 1, L237):
> "At December 31, 2025, we had **about 33,000 employees** worldwide. Of those, about 90% were in R&D,
> sales or manufacturing. … In 2025, our turnover rate was **10.1%**."

5. **Floor space** (Item 2, L352):
> "Our facilities in the United States contained approximately **17.8 million square feet** at December 31,
> 2025, of which approximately **0.6 million square feet** were leased. Our facilities outside the United
> States contained approximately **12.8 million square feet** at December 31, 2025, of which approximately
> **2.4 million square feet** were leased."
And L353: "At the end of 2025, we occupied substantially all of the space in our facilities."

6. **Country count** (Item 1, L121 and risk factor L248): "we have design, manufacturing or sales
operations in **more than 30 countries**."

7. **Days-based working-capital physicals** (MD&A, L460–461):
> "Days sales outstanding at the end of 2025 were **40** compared with **39** at the end of 2024."
> "**Days of inventory** at the end of 2025 were **222** compared with **241** at the end of 2024, which
> reflects the continued execution of our inventory strategy."

8. **Stockholders of record** (Item 5, L367): "we had **10,238 stockholders of record**."

9. **Fab count, indirect** (L466, L870): "our **three** large-scale 300mm wafer fabs located in Sherman,
Texas, and Lehi, Utah"; and "the planned closures of our **two** remaining factories with 150mm production"
(L426).

## THE 22 "capacity" OCCURRENCES AND THE 2 "utilization" OCCURRENCES — none carries a number

Neither the word "capacity" nor "utilization" is ever paired with a quantity, a percentage, or a
wafer-per-week figure anywhere in the document. The two "utilization" sentences:
> L215: "Our objectives for inventory are to maintain high levels of customer service, maintain dependable
> and competitive lead times, minimize inventory obsolescence and improve manufacturing asset **utilization**."
> L864: "Standard cost is based on the normal **utilization** of installed factory capacity. Cost associated
> with underutilization of capacity is expensed as incurred."

The nearest thing to a utilization disclosure is the qualitative loadings language (MD&A, L407):
> "Because we own much of our manufacturing capacity, a significant portion of our operating cost is fixed.
> When factory **loadings** decrease, our fixed costs are spread over reduced output and, absent other
> circumstances, our profit margins decrease. Conversely, as factory loadings increase, our fixed costs are
> spread over increased output and, absent other circumstances, our profit margins increase."
"loadings" appears **6** times; no loading percentage is ever given.

## WHY THIS MATTERS FOR THE RUN

The physical layer of this business — how many chips, at what price, out of how much installed capacity —
is **entirely absent from the primary filing**. Revenue, gross margin and the capex series are all the
filings give. Question 1 ("can I understand how this makes money?") can be answered structurally
(80,000 products × 100,000 customers × 300mm cost advantage) but **not quantitatively**: the price/volume
decomposition is not in the SEC record, and no SEC document would resolve it. Under the framework's own
test — "can I name the document that would resolve this?" — the answer for unit volumes and ASPs from
SEC primary sources alone is **NO**, which makes it UNKNOWABLE from the filings, not UNRESEARCHED.
(TI's quarterly capital-management presentations on ti.com carry some of this, but those are not SEC
primary documents and are outside the sourcing rule applied here.)
