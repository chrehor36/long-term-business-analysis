# ORCL competitor row — filing-sourced

**Built 2026-09-06.** Source: SEC EDGAR only. XBRL `companyfacts` for tagged values, filed
statements (Financial Report R-files) and the primary 10-K/20-F HTML for cross-checks and
verbatim text. **No aggregators, no memory, no web articles.**

Fetch method: `urllib`, User-Agent `Chris Hrehor chrehor36@gmail.com`, against
`data.sec.gov/api/xbrl/companyfacts/CIK##########.json`,
`data.sec.gov/submissions/CIK##########.json`, and `www.sec.gov/Archives/edgar/data/...`.

Every fact below is restricted to the accession named in its row — no cross-filing splicing,
no frame data. Per operator rule 4, each company's capex, depreciation and operating-income
figures were cross-checked against the filed cash flow statement / income statement, not
taken from the tagged data alone.

---

## Filings used

| Ticker | CIK | Form | FY end | Accession | Filed | Primary document |
|---|---|---|---|---|---|---|
| MSFT | 0000789019 | 10-K | **2026-06-30** | `0001193125-26-323660` | 2026-07-29 | `msft-20260630.htm` |
| GOOGL | 0001652044 | 10-K | **2025-12-31** | `0001652044-26-000018` | 2026-02-05 | `goog-20251231.htm` |
| AMZN | 0001018724 | 10-K | **2025-12-31** | `0001018724-26-000004` | 2026-02-06 | `amzn-20251231.htm` |
| SAP | 0001000184 | **20-F** | **2025-12-31** | `0001104659-26-020058` | 2026-02-26 | `sap-20251231x20f.htm` |
| IBM | 0000051143 | 10-K | **2025-12-31** | `0000051143-26-000010` | 2026-02-24 | `ibm-20251231.htm` |
| CRM | 0001108524 | 10-K | **2026-01-31** | `0001108524-26-000060` | 2026-03-02 | `crm-20260131.htm` |
| *ORCL (subject, reference)* | 0001341439 | 10-K | **2026-05-31** | `0001193125-26-277521` | 2026-06-22 | `orcl-20260531.htm` |

SAP CIK **verified**: `0001000184` returns `entityName = "SAP SE"`. Its companyfacts carry
`ifrs-full` (368 tags), not `us-gaap`.

---

## The row

All figures in **millions**. **MSFT, GOOGL, AMZN, IBM, CRM, ORCL in USD. SAP in EUR** — SAP
reports in euro and every SAP number below is euro, unconverted. No FX rate has been applied
anywhere in this file.

| # | Item | MSFT FY26 | GOOGL FY25 | AMZN FY25 | SAP FY25 **(EUR)** | IBM FY25 | CRM FY26 | *ORCL FY26* |
|---|---|---|---|---|---|---|---|---|
| 1 | **Total revenue** | 331,839 | 402,836 | 716,924 | 36,800 | 67,535 | 41,525 | *67,357* |
| 2 | **Operating income** | 155,237 | 129,039 | 79,975 | 9,617 | **not presented** | 8,331 | *20,606* |
| 2b | **Operating margin %** | **46.78%** | **32.03%** | **11.16%** | **26.13%** | **n/a — see note E** | **20.06%** | *30.59%* |
| 3 | **Capex** | 115,948 | 91,447 | 131,819 | 739 | 1,091 | 594 | *55,663* |
| 4 | **Depreciation** (`Depreciation`) | 34,300 | 21,136 | 41,860 | 1,311 (D&A) | 2,284 | 1,200 | *7,623* |
| 4b | **`DepreciationDepletionAndAmortization`** | **tag absent** | **tag absent** | 65,756 | n/a (IFRS) | **tag absent** | 1,200 | **tag absent** |
| 5 | **capex ÷ depreciation** | **3.38x** | **4.33x** | **3.15x** (2.01x vs D&A) | **0.56x** | **0.48x** | **0.50x** (0.16x vs 3,631) | ***7.30x*** |
| 6 | **capex ÷ revenue** | **34.94%** | **22.70%** | **18.39%** | **2.01%** | **1.62%** | **1.43%** | ***82.64%*** |
| 7 | **Operating cash flow** | 182,935 | 164,713 | 139,514 | 9,156 | 13,193 | 14,996 | *31,977* |
| 8 | **Share-based compensation** | 12,405 | 24,953 | 19,467 | 1,695 | 1,715 | 3,509 | *4,811* |
| 9 | **Total debt** (LT incl. current) | 40,294 | 48,543 | 68,396 | 6,150 | 61,260 | 14,439 | *129,541* |

Memo lines (same filings):

| Item | MSFT FY26 | GOOGL FY25 | AMZN FY25 | SAP FY25 (EUR) | IBM FY25 | CRM FY26 | *ORCL FY26* |
|---|---|---|---|---|---|---|---|
| OCF ÷ revenue | 55.1% | 40.9% | 19.5% | 24.9% | 19.5% | 36.1% | *47.5%* |
| SBC ÷ revenue | 3.7% | 6.2% | 2.7% | 4.6% | 2.5% | 8.5% | *7.1%* |
| Finance lease liability, total | **66,594** | **2,500** | **12,286** | 1,684 (all leases, IFRS 16) | 1,153 | 535 | *7,701* |
| Operating lease liability | 21,925 | 15,954 | 89,252 | — (IFRS: single figure) | 3,347 | 2,737 | *30,190* |

### Cloud / segment operating margin (item 10)

Taken from the segment footnote detail of each latest 10-K (rendered XBRL R-file of the
same accession).

| Segment | FY | Revenue | Segment operating income | **Margin** | Source |
|---|---|---|---|---|---|
| **Microsoft Intelligent Cloud** | FY2026 (2026-06-30) | 137,791 | 56,972 | **41.35%** | `0001193125-26-323660`, R107 "Segment Revenue, Cost of Revenue, Operating Expenses and Operating Income (Detail)" |
| **Amazon AWS** | FY2025 (2025-12-31) | 128,725 | 45,606 | **35.43%** | `0001018724-26-000004`, R87 "Segment Information — Reportable Segments and Reconciliation to Consolidated Net Income (Details)" |
| **Google Cloud** | FY2025 (2025-12-31) | 58,705 | 13,910 | **23.69%** | `0001652044-26-000018`, R90 "Information about Segments and Geographic Areas — Revenue and Operating Income/Loss by Segment (Details)" |

Prior-year segment operating income, from the same tables (comparatives inside the same
accession, so same-source):

| Segment | FY-2 | FY-1 | FY-0 |
|---|---|---|---|
| Intelligent Cloud | 37,813 (FY24) | 44,589 (FY25) | 56,972 (FY26) |
| AWS | 24,631 (2023) | 39,834 (2024) | 45,606 (2025) |
| Google Cloud | 1,716 (2023) | 6,112 (2024) | 13,910 (2025) |

**Oracle discloses no cloud-segment operating income.** Oracle's 10-K reports operating
segments on a basis that excludes most allocated costs and does not present an OCI/IaaS
segment margin comparable to the three above. Nothing has been substituted.

---

## Leases that have not yet commenced — verbatim (item 11)

Fetched from the primary 10-K HTML of the accession named, searched for "not yet commenced"
/ "have not yet commenced". Text below is transcribed from the filed document; `$` amounts
appear as filed. Note the filings insert spaces around inline-XBRL tagged numbers — that
artifact is preserved rather than smoothed, per prime rule 1.

### MSFT — `0001193125-26-323660`, Note 13 (Leases), FY end 2026-06-30

> "As of June 30, 2026, we had additional leases, primarily for datacenters, that had not yet
> commenced of $ 329.1 billion, with some arrangements subject to certain contractual
> conditions being met. These leases will commence between fiscal year 2027 and fiscal year
> 2033 with lease terms of 1 year to 20 years."

Same note, verbatim: "Total finance lease liabilities $ 66,594 $ 46,172" (FY2026, FY2025).
Maturities: "Total lease payments 24,706 89,686 Less imputed interest ( 2,781 ) ( 23,092 )
Total $ 21,925 $ 66,594".

**MSFT finance lease liability total: $66,594 million. Not yet commenced: $329.1 billion.**

### GOOGL — `0001652044-26-000018`, Note 4 (Leases), FY end 2025-12-31

> "As of December 31, 2025 , we have entered into leases primarily related to data centers
> that have not yet commenced with short-term and long-term future lease payments of $ 5.8
> billion and $ 52.7 billion, respectively, that are not yet recorded. These leases will
> commence between 2026 and 2031 with non-cancelable lease terms primarily between one and
> 25 years. In January 2026, we executed a power purchase agreement which we expect to be
> accounted for as a lease resulting in future payments depending on certain agreement terms
> of $ 9.9 billion between 2027 and 2047. If certain contractual conditions for the project
> are not met, we would instead make a one-time payment of approximately $ 3.5 billion and
> assume ownership of the power generating assets."

Two further verbatim mentions in the same 10-K:

> "The year ended December 31, 2025 includes $ 1.1 billion of prepayments for finance leases
> not yet commenced."

> (Note 5, VIEs) "The maximum exposure arising from leases with VIEs is limited to the net
> carrying value of commenced finance lease assets, plus the undiscounted future obligations
> for leases that have not yet commenced."

Same note: "Total lease liability balance $ 15,954 $ 2,500" (operating, finance).

**GOOGL finance lease liability total: $2,500 million. Not yet commenced: $5.8bn short-term
+ $52.7bn long-term = $58.5 billion undiscounted.**

### AMZN — `0001018724-26-000004`, Note 7 (Commitments and Contingencies), FY end 2025-12-31

**Amazon does not write a narrative "leases that have not yet commenced" sentence.** The only
occurrence of the phrase in the entire 10-K is a **row label in the contractual commitments
table**. Verbatim, the table row as filed:

> "Leases not yet commenced 5,808 9,103 6,420 6,571 6,738 61,733 96,373"

columns being, per the table header: "Year Ended December 31, 2026 2027 2028 2029 2030
Thereafter Total". Table preamble, verbatim:

> "The following summarizes our principal contractual commitments, excluding open orders for
> purchases that support normal operations and are generally cancellable, as of December 31,
> 2025 (in millions):"

**AMZN leases not yet commenced: $96,373 million ($96.4 billion) undiscounted.** Adjacent
rows in the same table, verbatim: "Operating lease liabilities 15,380 13,186 12,140 10,911
9,710 45,587 106,914"; "Finance lease liabilities, including interest 1,838 1,626 1,726
1,285 1,122 7,320 14,917"; "Financing obligations, including interest 577 582 592 601 612
6,651 9,615".

**AMZN finance lease liability total: $12,286 million** (current 1,544 + non-current 10,742,
balance-sheet carrying value; the 14,917 above is undiscounted and includes interest).

### ORCL (subject) — `0001193125-26-277521`, Note 12 (Leases), FY end 2026-05-31

Included for the comparison it exists to serve:

> "As of May 31, 2026 , we had $ 260 billion of additional lease commitments, substantially
> all related to data center arrangements, that are generally expected to commence between
> the first quarter of fiscal 2027 and fiscal 2029 and for terms of fifteen to nineteen years
> that were not reflected on our consolidated balance sheet as of May 31, 2026 or in the
> maturities table above. These additional lease commitments include a lease for which we
> have guaranteed up to $ 3.3 billion of the lessor's borrowing..."

Same note: "Total lease payments 41,867 11,460 Less: imputed interest ( 11,677 ) ( 3,759 )
Total lease liability $ 30,190 $ 7,701" (operating, finance).

**Off-balance-sheet lease commitment, side by side, as filed:**

| | Not-yet-commenced leases | FY revenue | ×revenue |
|---|---|---|---|
| **ORCL** | **$260.0bn** | 67,357 | **3.86x** |
| MSFT | $329.1bn | 331,839 | 0.99x |
| GOOGL | $58.5bn | 402,836 | 0.15x |
| AMZN | $96.4bn | 716,924 | 0.13x |

*(The ×revenue column is arithmetic on the two filed figures beside it, not a disclosed
number.)*

---

## Notes — tag choices, cross-checks, and every judgment call

**A. Which depreciation tag.** Stated per company because they differ, and the difference
moves the capex ÷ depreciation ratio a lot.

- **MSFT** — used **`Depreciation` = 34,300**. `DepreciationDepletionAndAmortization` **is not
  tagged in this filing**. The cash flow statement line is "Depreciation, amortization, and
  other = 38,534", which Microsoft tags with a **company extension element** that does not
  appear in `companyfacts` (which carries only `us-gaap` and `dei`). 34,300 is property-and-
  equipment depreciation. The 38,534 figure is read off the filed cash flow statement (R6).
- **GOOGL** — used **`Depreciation` = 21,136**. This *is* the cash flow statement line,
  verbatim "Depreciation of property and equipment | 21,136". `DepreciationDepletionAnd-
  Amortization` not tagged. Clean, no ambiguity.
- **AMZN** — **both** are tagged and they are far apart. `Depreciation = 41,860` (property and
  equipment, incl. finance-lease assets, from the segment/PP&E disclosure);
  `DepreciationDepletionAndAmortization = 65,756`, which is the cash flow line "Depreciation
  and amortization of property and equipment and capitalized content costs, operating lease
  assets, and other". **Headline capex ÷ depreciation uses 41,860 (3.15x); against the full
  65,756 it is 2.01x.** Both shown.
- **SAP** — IFRS, so neither US-GAAP tag exists. Used
  **`AdjustmentsForDepreciationAndAmortisationExpense` = 1,311**, the cash flow line
  "Depreciation and amortization". SAP separately tags `DepreciationRightofuseAssets = 275`.
- **IBM** — used **`Depreciation` = 2,284**, the cash flow line, which IBM footnotes:
  "Includes operating lease right-of-use assets amortization expense of $0.9 billion in 2025,
  2024 and 2023." `DepreciationDepletionAndAmortization` **not tagged**. IBM separately
  reports "Amortization of capitalized software and acquired intangible assets = 2,737".
- **CRM** — **both tagged, and the smaller one is not the cash flow line.**
  `DepreciationDepletionAndAmortization = 1,200` is the **property-and-equipment footnote**
  figure: verbatim, "Depreciation and amortization of fixed assets totaled $1.2 billion, $1.0
  billion and $1.1 billion during fiscal 2026, 2025 and 2024, respectively."
  `DepreciationAndAmortization = 3,631` is the **cash flow line**, footnoted "Includes
  amortization of intangible assets acquired through business combinations, depreciation of
  fixed assets and amortization and impairment of right-of-use assets." **Headline ratio uses
  1,200 (0.50x) because that is the like-for-like PP&E figure; against 3,631 it is 0.16x.**
- **ORCL** — used `Depreciation = 7,623`, the cash flow line. `DepreciationDepletionAnd-
  Amortization` not tagged; "Amortization of intangible assets = 1,671" is separate.

**B. Capex tag — Amazon does not use the requested element.**
`PaymentsToAcquirePropertyPlantAndEquipment` is **absent from Amazon's FY2025 10-K**. Amazon
tags the cash flow line "Purchases of property and equipment | (131,819)" as
**`PaymentsToAcquireProductiveAssets`**. That is the figure used. Amazon also discloses
"Proceeds from property and equipment sales and incentives | 3,499" on the next line; **net
capex would be 128,320 (17.9% of revenue)**; the gross 131,819 is used above for consistency
with the other companies. All other six use `PaymentsToAcquirePropertyPlantAndEquipment`,
each cross-checked to its cash flow line: MSFT "Additions to property and equipment 115,948";
GOOGL "Purchases of property and equipment 91,447"; IBM "Payments for property, plant and
equipment 1,091"; CRM "Capital expenditures 594"; ORCL "Capital expenditures 55,663".

**IBM caveat:** IBM's 1,091 excludes "Investment in software | (647)", a separate investing
line. Capex including software = 1,738, giving capex ÷ (2,284+2,737) = 0.35x.

**ORCL caveat:** Oracle discloses "Unpaid capital expenditures | 5,279" as a non-cash item, so
cash capex of 55,663 understates FY2026 additions.

**GOOGL caveat:** Alphabet discloses "Purchases of property and equipment included in accrued
liabilities and accounts payable | $ 15,090", same effect.

**C. Total debt (item 9) — carrying value, long-term debt including its current portion.**
Cross-checked to each debt footnote, because the `LongTermDebt` tag is *face value* for two
of them and the difference is real:

- **MSFT** 40,294 = `LongTermDebtNoncurrent` 31,067 + `LongTermDebtCurrent` 9,227. `LongTermDebt`
  tag also 40,294 (consistent). **Excludes the 66,594 finance lease liability** — flagged
  because for Microsoft that liability is 1.65x its funded debt.
- **GOOGL** 48,543 = 46,547 + 1,996. The `LongTermDebt` tag reads **49,085, which is *face*
  value**: debt note, verbatim "Total face value of long-term debt 12,000 49,085 / Unamortized
  discount and debt issuance costs (118) (542) / Less: current portion of long-term notes
  (999) (1,996) / Total long-term debt $ 10,883 $ 46,547". Commercial paper outstanding at
  2025-12-31: **zero** ("no commercial paper outstanding as of December 31, 2025").
- **AMZN** 68,396 = 65,648 + 2,748. `LongTermDebt` tag **68,836 is face value** ("Total face
  value of long-term debt 58,000 68,836 / Unamortized discount and issuance costs, net (360)
  (440)"). Amazon additionally has `ShortTermBorrowings` 455 under other short-term credit
  facilities; including it, total debt = 68,851. Commercial paper outstanding: **zero**.
- **SAP** 6,150 = `LongtermBorrowings` 4,550 + `CurrentBorrowingsAndCurrentPortionOfNoncurrent-
  Borrowings` 1,600. Disclosed weighted borrowing rate 3.23%. Lease liabilities of 1,684
  (254 current + 1,430 non-current) are **excluded** from this line, matching the US-GAAP
  treatment used for the others.
- **IBM** 61,260 = `LongTermDebtNoncurrent` 54,836 + `ShortTermBorrowings` 6,424 (IBM tags the
  same two amounts as `LongTermDebtAndCapitalLeaseObligations` / `...Current`). IBM's debt is
  the only one here materially inflated by a captive financing arm — not adjusted for.
- **CRM** 14,439 = 10,439 + 4,000.
- **ORCL** 129,541 = `DebtLongtermAndShorttermCombinedAmount`, carrying value; face value
  `DebtInstrumentFaceAmount` 130,105 less `DebtInstrumentUnamortizedDiscountPremiumAndDebt-
  IssuanceCostsNet` 564. `DebtCurrent` 7,199. Cross-checked against the maturity ladder,
  which sums to 130,105 face.

**D. Revenue tag.** MSFT / AMZN / CRM: `RevenueFromContractWithCustomerExcludingAssessedTax`.
GOOGL / IBM: `Revenues`. ORCL tags both, identical at 67,357. SAP: `Revenue` (IFRS),
cross-checked to the filed income statement line "Total revenue | 36,800" — the round number
is as filed, not a rounding introduced here.

**E. IBM has no operating income — this is an absence, not a gap in the research.**
IBM's consolidated income statement (R3 of `0000051143-26-000010`) runs: Revenue 67,535 →
Cost 28,239 → **Gross profit 39,297** → "Total expense and other (income)" 28,968 → **"Income
from continuing operations before income taxes" 10,328**. There is **no operating income
subtotal**, and `us-gaap:OperatingIncomeLoss` is **not tagged in the filing**. The 28,968
expense block *includes* interest expense of 1,935 and "Other (income) and expense" of (442),
so the 10,328 pre-tax figure is not an operating figure.

A derived operating income can be constructed as gross profit 39,297 − SG&A 20,123 − R&D
8,316 + IP and custom development income 964 = **11,822 (17.5% of revenue)**. **That is my
arithmetic, not a filed line** — labelled here as a **CONVENTION** so it is never mistaken
for a disclosure. Rationale: it is the only subtotal that puts IBM on the same operating
basis as the other six, and every input to it is a filed line from the same statement. It
carries no authority beyond that.

**F. Share-based compensation.** All from the cash flow statement add-back
(`ShareBasedCompensation`), which is the comparable basis. One exception worth naming:
Alphabet also tags `AllocatedShareBasedCompensationExpense = 27,100` against the cash flow
add-back of **24,953**; the 27,100 is total SBC expense before amounts capitalized. **24,953
is used.** MSFT, AMZN and IBM tag both elements at identical values, so no choice arises. SAP
uses `ExpenseFromSharebasedPaymentTransactions... = 1,695`, matching the cash flow line
"Share-based payment expense | 1,695"; SAP's cash *outflow* for share-based payments was a
separate (817).

**G. SAP obtained in full from EDGAR — no rung failed.** The 20-F carries complete inline
XBRL under `ifrs-full`, and both the income statement and cash flow statement were read from
the filed statements as rendered from that accession. Values used, all EUR millions, all from
`0001104659-26-020058`:

| SAP line, as filed | EUR m | IFRS tag |
|---|---|---|
| "Total revenue" | 36,800 | `Revenue` |
| "Operating profit" | 9,617 | `ProfitLossFromOperatingActivities` |
| "Purchase of intangible assets and property, plant, and equipment" | (739) | `PurchaseOfPropertyPlantAndEquipmentIntangibleAssetsOtherThanGoodwillInvestmentPropertyAndOtherNoncurrentAssets` |
| "Depreciation and amortization" | 1,311 | `AdjustmentsForDepreciationAndAmortisationExpense` |
| "Net cash flows from operating activities" | 9,156 | `CashFlowsFromUsedInOperatingActivities` |
| "Share-based payment expense" | 1,695 | `ExpenseFromSharebasedPaymentTransactionsInWhichGoodsOrServicesReceivedDidNotQualifyForRecognitionAsAssets` |
| Borrowings (4,550 non-current + 1,600 current) | 6,150 | `LongtermBorrowings` / `CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings` |

**One SAP caveat:** the capex line is **combined intangibles + PP&E**; SAP does not disclose a
cash PP&E-only capex figure. SAP separately tags `AdditionsOtherThanThroughBusiness-
CombinationsPropertyPlantAndEquipmentIncludingRightofuseAssets = 1,130`, which is *additions
including right-of-use assets*, a different concept, and is **not** used. SAP's capex ÷
depreciation of 0.56x is therefore slightly overstated on the numerator (it includes
intangibles) and not strictly comparable to the US filers' PP&E-only capex.

Also note SAP's own presentation change, verbatim from the cash flow statement footnote:
"As of January 2025, SAP no longer classifies interest paid and interest received as a part
of cash flows from operating activities. The presentation for prior periods was amended
accordingly." SAP's 9,156 OCF is therefore on a different basis than a pre-2025 SAP figure.

---

## What could NOT be obtained — absence is a finding

Stated explicitly, and **not filled in from memory or from any non-EDGAR source**:

1. **IBM operating income and operating margin — DOES NOT EXIST as a filed figure.** Not a
   fetch failure. IBM's income statement presents no operating income subtotal and the
   filing does not tag `us-gaap:OperatingIncomeLoss`. The 11,822 / 17.5% in note E is my own
   derivation, labelled CONVENTION.
2. **MSFT `DepreciationDepletionAndAmortization` — not tagged.** Microsoft tags its cash flow
   D&A line with a company extension element, which `companyfacts` does not carry. The
   38,534 was read directly off the filed cash flow statement instead.
3. **GOOGL, IBM, ORCL `DepreciationDepletionAndAmortization` — not tagged.** `Depreciation`
   used, as noted per company.
4. **AMZN `PaymentsToAcquirePropertyPlantAndEquipment` — not tagged.**
   `PaymentsToAcquireProductiveAssets` used instead; same cash flow line.
5. **AMZN has no narrative "leases that have not yet commenced" sentence.** The requested
   verbatim sentence does not exist in the FY2025 10-K. The disclosure is a table row label
   only, reproduced verbatim above. The dollar figure ($96,373m) is real and sourced; the
   *sentence* is not.
6. **Oracle cloud-segment operating margin — not disclosed.** Oracle publishes no OCI/cloud
   segment operating income comparable to Intelligent Cloud / AWS / Google Cloud, so the
   fourth cell of that comparison is empty and stays empty.
7. **SAP cloud-segment operating margin — not gathered.** Not requested; SAP does report
   segment results (R19/R20 of the 20-F) and it is available if wanted.
8. **SAP PP&E-only cash capex — not disclosed.** The cash flow line combines intangibles and
   PP&E (note G).
9. **No FX conversion of SAP.** SAP's row is EUR throughout. Converting it would require a
   rate from outside EDGAR, which the brief excludes. Any USD comparison of SAP must be done
   downstream with a dated, sourced rate.
10. **NVDA was not built.** A CIK was supplied (0001045810) but NVDA was not in the list of
    six companies requested, so no row was produced. The companyfacts file was fetched and
    is available.

## Standing caution on the comparison itself

The capex ÷ depreciation column spans **0.48x (IBM) to 7.30x (ORCL)** and is the single most
load-bearing number in this row. It is not clean across companies: the denominator is a
different concept for AMZN (41,860 vs 65,756), for CRM (1,200 vs 3,631), and for IBM (which
folds $0.9bn of ROU amortization into "Depreciation"). Both readings are given wherever they
diverge. The ratio also silently omits the leased fleet — and for Microsoft, Oracle and
Amazon the leased datacenter capacity is the larger commitment. **Read row 5 next to the
not-yet-commenced lease table above, never on its own.**
