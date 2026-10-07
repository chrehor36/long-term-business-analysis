# COMPETITOR ROW — MSFT run, 2026-09-06

**Rule applied:** a moat is a claim about relative position, so every peer gets the same
metric, the same window, filing-sourced. No press, no aggregators, no memory. Every number
below carries its form and fiscal year. All figures $ millions unless stated.

**Owner earnings, this project's construction (both ends):**
- capex end = operating cash flow − stock-based compensation − capital expenditures
- D&A end  = operating cash flow − stock-based compensation − depreciation & amortization

**Sources — every document read, with accession number.** Primary documents pulled from SEC
EDGAR; stripped text of each saved alongside this file.

| Peer | CIK | FY end | Filings read (accession) |
|---|---|---|---|
| GOOGL | 0001652044 | Dec 31 | FY2025 `0001652044-26-000018` · FY2024 `0001652044-25-000014` · FY2023 `0001652044-24-000022` · FY2022 `0001652044-23-000016` · FY2021 `0001652044-22-000019` · FY2015 `0001652044-16-000012` |
| AMZN | 0001018724 | Dec 31 | FY2025 `0001018724-26-000004` · FY2024 `0001018724-25-000004` · FY2023 `0001018724-24-000008` · FY2022 `0001018724-23-000004` · FY2021 `0001018724-22-000005` · FY2020 `0001018724-21-000004` · FY2015 `0001018724-16-000172` |
| ORCL | 0001341439 | May 31 | FY2026 `0001193125-26-277521` · FY2025 `0000950170-25-087926` · FY2024 `0000950170-24-075605` · FY2023 `0000950170-23-028914` · FY2022 `0001564590-22-023675` · FY2016 `0001193125-16-628942` |
| MSFT *(subject, for the depreciation table)* | 0000789019 | Jun 30 | FY2026 `0001193125-26-323660` · FY2025 `0000950170-25-100235` · FY2024 `0000950170-24-087843` · FY2023 `0000950170-23-035122` · FY2022 `0001564590-22-026876` · FY2021 `0001564590-21-039151` · FY2016 `0001193125-16-662209` |

**Operator rule 4 satisfied:** each cash-flow, income-statement and property-note figure was
read off the filed statement in the primary document, not off XBRL tags. No aggregator was
used for any fundamental.

---
## PEER 1 — ALPHABET INC. (GOOGL)

### Cash-flow inputs, as filed

| CY | OCF | SBC | Capex (purchases of P&E) | Depreciation of P&E | Revenue |
|---|---|---|---|---|---|
| 2021 | 91,652 | 15,376 | 24,640 | 10,273 | 257,637 |
| 2022 | 91,495 | 19,362 | 31,485 | 13,475 | 282,836 |
| 2023 | 101,746 | 22,460 | 32,251 | 11,946 | 307,394 |
| 2024 | 125,299 | 22,785 | 52,535 | 15,311 | 350,018 |
| 2025 | 164,713 | 24,953 | 91,447 | 21,136 | 402,836 |

**Presentation caveat, flagged.** The FY2022 10-K captioned the line "Depreciation **and
impairment** of property and equipment" and showed 11,555 (2021) and 15,287 (2022). From the
FY2023 10-K forward the caption is "Depreciation of property and equipment" and the same
years are restated to 10,273 and 13,475, with impairment moved to "Other". The table above
uses the **later, narrower** presentation for every year, so the capex/D&A ratio is not
flattered by an impairment sitting in the denominator.

Intangible amortization was a separate cash-flow line only through FY2022 (886 in 2021, 641
in 2022); from FY2023 it is folded into "Other" and is **not separately disclosed on the
cash-flow statement**. It is small relative to P&E depreciation and is excluded from the D&A
end above so that the same line is used in every year.

Non-cash capex accrual disclosed as a supplemental item: purchases of P&E in accrued
liabilities and accounts payable of 7,435 (2023), 10,326 (2024), **15,090 (2025)** — cash
capex understates the FY2025 commitment by roughly this rising accrual.

### Owner earnings, both ends

| CY | OE, capex end | OE, D&A end | Capex ÷ D&A | Capex ÷ revenue |
|---|---|---|---|---|
| 2021 | 51,636 | 66,003 | **2.40×** | 9.6% |
| 2022 | 40,648 | 58,658 | **2.34×** | 11.1% |
| 2023 | 47,035 | 67,340 | **2.70×** | 10.5% |
| 2024 | 49,979 | 87,203 | **3.43×** | 15.0% |
| 2025 | 48,313 | 118,624 | **4.33×** | 22.7% |

The two ends diverge by 70,311 in 2025 versus 14,367 in 2021. Owner earnings at the capex end
are **flat since 2021** (51,636 → 48,313) while the D&A end nearly doubles. The whole
apparent growth in Alphabet's cash generation over five years lives in the gap between what
it spends on plant and what it charges for plant.

### Depreciation life — every change, with the filing's own dollar effect

**FY2015 vintage (10-K for CY2015):** "We compute depreciation using the straight-line method
over the estimated useful lives of the assets, **generally two to five years**." Servers were
carried at three years.

**Change 1 — January 2021, servers 3→4 years, certain network equipment 3→5 years.** From
Note 1, FY2021 10-K, verbatim:

> "In January 2021, we completed an assessment of the useful lives of our servers and network
> equipment and adjusted the estimated useful life of our servers from three years to four
> years and the estimated useful life of certain network equipment from three years to five
> years. This change in accounting estimate was effective beginning in fiscal year 2021. Based
> on the carrying value of servers and certain network equipment as of December 31, 2020 and
> those acquired during the year ended December 31, 2021, the effect of this change in estimate
> was a **reduction in depreciation expense of $2.6 billion and an increase in net income of
> $2.0 billion, or $3.02 per basic share and $2.98 per diluted share**, for the year ended
> December 31, 2021."

**Change 2 — January 2023, servers 4→6 years, certain network equipment 5→6 years.** From
Critical Accounting Estimates, FY2023 10-K, verbatim:

> "In January 2023, we completed an assessment of the useful lives of our servers and network
> equipment and adjusted the estimated useful life of our servers from four years to six years
> and the estimated useful life of certain network equipment from five years to six years. This
> change in accounting estimate was effective beginning in fiscal year 2023. Based on the
> carrying value of servers and certain network equipment as of December 31, 2022, and those
> placed in service during the year ended December 31, 2023, the effect of this change in
> estimate was a **reduction in depreciation expense of $3.9 billion and an increase in net
> income of $3.0 billion, or $0.24 per basic and $0.24 per diluted share**, for the year ended
> December 31, 2023."

The FY2023 10-K also attributes segment results to it explicitly: Google Cloud's first
positive operating income year "benefited from a reduction in costs driven by the change in
the estimated useful lives of our servers and certain network equipment."

**No third change and NO REVERSAL through FY2025.** FY2024 and FY2025 Note 1 both read: "We
depreciate servers and network equipment generally over a period of six years."

One disclosure shift worth recording: FY2025 adds language absent earlier — depreciation is
recorded over lives "which we regularly evaluate **for factors such as technological
obsolescence and our planned use and utilization**", and a new critical-estimate paragraph:
"To determine the useful lives of our technical infrastructure, we rely on multiple inputs,
including historical asset performance, expected technology advancements, and our future
infrastructure deployment plans. Any change in the estimated useful lives is recognized on a
prospective basis." Alphabet has not reversed, but it has built the disclosure scaffolding
for a reversal.

### Google Cloud segment

| CY | Revenue | Operating income (loss) | Margin |
|---|---|---|---|
| 2021 | 19,206 | (2,282) | (11.9)% |
| 2022 | 26,280 | (1,922) | (7.3)% |
| 2023 | 33,088 | 1,716 | 5.2% |
| 2024 | 43,229 | 6,112 | 14.1% |
| 2025 | 58,705 | 13,910 | 23.7% |

**Recast flagged.** As originally filed in the FY2022 10-K, Google Cloud operating loss was
(3,099) for 2021 and (2,968) for 2022. The FY2023 10-K recast those to (2,282) and (1,922)
following a change in how centrally-managed costs are allocated to segments. The table uses
the later presentation throughout. The 2021 and 2022 losses were **larger as first reported**.

### Remaining performance obligation

| As of | RPO | Recognition period, as disclosed |
|---|---|---|
| Dec 31 2024 | **$93.2 bn** | "approximately half ... over the next 24 months with the remainder to be recognized thereafter" |
| Dec 31 2025 | **$242.8 bn** | "just over 50% of the revenue backlog as revenues over the next 24 months with the remainder to be recognized thereafter" |

Alphabet calls it "revenue backlog", primarily Google Cloud; excludes contracts with an
original expected term of one year or less and cancellable contracts. It rose 2.6× in one year.

### Return on equity

| CY | Net income | Equity, year-end | Average equity | ROE |
|---|---|---|---|---|
| 2021 | 76,033 | 251,635 | 237,090 | 32.1% |
| 2022 | 59,972 | 256,144 | 253,890 | 23.6% |
| 2023 | 73,795 | 283,379 | 269,762 | 27.4% |
| 2024 | 100,118 | 325,084 | 304,232 | 32.9% |
| 2025 | 132,170 | 415,265 | 370,174 | 35.7% |

(2020 year-end equity 222,544, used as the opening balance for the 2021 average.)

---
## PEER 2 — AMAZON.COM INC. (AMZN) / AWS SEGMENT

### Cash-flow inputs, as filed

| CY | OCF | SBC | Capex (purchases of P&E) | D&A, cash-flow line¹ | D&A, P&E only² | Net sales |
|---|---|---|---|---|---|---|
| 2021 | 46,327 | 12,757 | 61,053 | 34,433 | 22,900 | 469,822 |
| 2022 | 46,752 | 19,621 | 63,645 | 41,921 | 24,900 | 513,983 |
| 2023 | 84,946 | 24,023 | 52,729 | 48,663 | 30,225 | 574,785 |
| 2024 | 115,877 | 22,011 | 82,999 | 52,795 | 32,067 | 637,959 |
| 2025 | 139,514 | 19,467 | 131,819 | 65,756 | 41,860 | 716,924 |

¹ The cash-flow caption is "Depreciation and amortization **of property and equipment and
capitalized content costs, operating lease assets, and other**" — it is broader than property
depreciation and is **not** the right denominator against capex.
² From the property-and-equipment note, chained across four filings and consistent in every
overlap: "$16.2 billion, $22.9 billion, and $24.9 billion ... for 2020, 2021, and 2022"
(FY2022 10-K); "$22.9 billion, $24.9 billion, and $30.2 billion ... for 2021, 2022, and 2023"
(FY2023 10-K); "$24.9 billion, $30.2 billion, and $32.1 billion ... for 2022, 2023, and 2024"
(FY2024 10-K); "$30.2 billion, $32.1 billion, and $41.9 billion ... for 2023, 2024, and 2025"
(FY2025 10-K). Exact figures for 2023-2025 (30,225 / 32,067 / 41,860) are taken from the
segment note. All include amortization of P&E acquired under finance leases ($9.9bn 2021,
$6.1bn 2022, $5.9bn 2023, $3.9bn 2024, $3.3bn 2025).

**Capex is understated by the cash line alone.** Amazon discloses separately:

| CY | Purchases of P&E (cash) | Proceeds from P&E sales & incentives | P&E acquired under finance leases | Increase in P&E acquired but not yet paid | **Total net additions to P&E** (segment note) |
|---|---|---|---|---|---|
| 2023 | 52,729 | 4,596 | 642 | (1,414) | 48,344 |
| 2024 | 82,999 | 5,341 | 854 | 7,039 | 85,752 |
| 2025 | 131,819 | 3,499 | **2,911** | **10,155** | **142,352** |

Of the FY2025 total net additions of 142,352, **AWS accounts for 96,496** (2024: 53,267;
2023: 24,843), including finance-lease additions of 1.9bn and build-to-suit additions of
421m in the AWS segment alone. Amazon's own "cash capital expenditures" measure (capex net of
proceeds) was $77.7bn in 2024 and $128.3bn in 2025.

### Owner earnings, both ends

| CY | OE, capex end | OE, D&A end (CF line) | OE, D&A end (P&E only) | Capex ÷ D&A (P&E only) | Capex ÷ revenue |
|---|---|---|---|---|---|
| 2021 | **(27,483)** | (863) | 10,670 | 2.67× | 13.0% |
| 2022 | **(36,514)** | (14,790) | 2,231 | 2.56× | 12.4% |
| 2023 | 8,194 | 12,260 | 30,698 | 1.74× | 9.2% |
| 2024 | 10,867 | 41,071 | 61,799 | 2.59× | 13.0% |
| 2025 | **(11,772)** | 54,291 | 78,187 | 3.15× | 18.4% |

Amazon's owner earnings at the capex end are **negative in three of the five years**,
including the most recent. On the P&E-only D&A end every year is positive. The entire
difference between "this business generates $78bn" and "this business consumes $12bn" in
2025 is the $90bn gap between what Amazon spent on plant and what it charged for plant.

### Depreciation life — the only peer that has REVERSED

**FY2015 vintage (10-K for CY2015):** "**three years for our servers**, five years for
networking equipment, five years for furniture and fixtures, and ten years for heavy
equipment."

**Change 1 — January 1, 2020, servers 3→4 years.** FY2020 10-K, verbatim:

> "We review the useful lives of equipment on an ongoing basis, and effective January 1, 2020
> we changed our estimate of the useful life for our servers from three years to four years. The
> longer useful life is due to continuous improvements in our hardware, software, and data center
> designs. The effect of this change in estimate for the year ended December 31, 2020 ... was a
> **reduction in depreciation and amortization expense of $2.7 billion and an increase in net
> income of $2.0 billion, or $4.06 per basic share**" (pre-split shares).

**Change 2 — January 1, 2022, servers 4→5 years, networking equipment 5→6 years.** FY2022
10-K, Use of Estimates, verbatim:

> "We review the useful lives of equipment on an ongoing basis, and effective January 1, 2022
> we changed our estimate of the useful lives for our servers from four years to five years and
> for our networking equipment from five years to six years. The longer useful lives are due to
> continuous improvements in our hardware, software, and data center designs. The effect of this
> change in estimate for the year ended December 31, 2022 ... was a **reduction in depreciation
> and amortization expense of $3.6 billion and a benefit to net loss of $2.8 billion, or $0.28
> per basic share and $0.28 per diluted share**."

**Change 3 — January 1, 2024, servers 5→6 years.** Pre-announced in the FY2023 10-K: "in Q4
2023 we completed a useful life study for our servers and are increasing the useful life from
five years to six years in January 2024, which ... **will have an anticipated impact to our
2024 operating income of $3.1 billion**." Realized effect, FY2024 10-K, verbatim:

> "We had previously increased the useful life of our servers from five years to six years
> effective January 1, 2024. The effect of this change for the year ended December 31, 2024 ...
> was a **reduction in depreciation and amortization expense of $3.2 billion and a benefit to
> net income of $2.5 billion, or $0.23 per basic share and $0.23 per diluted share**."

**Change 4 — THE REVERSAL. January 1, 2025, a subset of servers and networking equipment
6→5 years.** Announced in the FY2024 10-K, verbatim:

> "We completed our most recent servers and networking equipment useful life study in Q4 2024,
> and are changing the useful lives of a subset of our servers and networking equipment,
> effective January 1, 2025, **from six years to five years**. For those assets included in
> 'Property and equipment, net' as of December 31, 2024, whose useful life will change from six
> years to five years, we anticipate a **decrease in 2025 operating income of approximately $0.7
> billion**. ... In 2024, we also determined, primarily in the fourth quarter, **to retire early
> certain of our servers and networking equipment. We recorded approximately $920 million of
> accelerated depreciation and related charges for the quarter ended December 31, 2024** related
> to these decisions. The accelerated depreciation will continue into 2025 and **decrease
> operating income by approximately $0.6 billion in 2025**. These two changes above are due to
> **an increased pace of technology development, particularly in the area of artificial
> intelligence and machine learning**."

Realized effect, FY2025 10-K, verbatim:

> "Effective January 1, 2025 we changed our estimate of the useful lives of a subset of our
> servers and networking equipment from six years to five years. **The shorter useful lives are
> due to the increased pace of technology development, particularly in the area of artificial
> intelligence and machine learning.** The effect of this change in estimate for the year ended
> December 31, 2025 ... was an **increase in depreciation and amortization expense of $1.4
> billion and a reduction in net income of $1.0 billion, or $0.10 per basic share and $0.10 per
> diluted share, which primarily impacted our AWS segment.**"

The realized reversal cost ($1.4bn of extra depreciation) came in **double the $0.7bn the
company had guided a year earlier**.

The FY2025 property note now reads "Servers and networking equipment | **Five to six years**"
with the footnote: "Effective January 1, 2024, we changed our estimate of the useful lives for
our servers from five to six years, and effective January 1, 2025, we changed our estimate of
the useful lives of a subset of our servers and networking equipment from six to five years."

*Separately and in the opposite direction:* effective January 1, 2025 Amazon **extended** heavy
equipment (fulfillment, not data-centre) from ten to thirteen years, "an increase in 2025
operating income of approximately $0.9 billion", recorded in Fulfillment and hitting the North
America and International segments — not AWS.

### AWS segment

| CY | Revenue | Operating income | Margin | Segment D&A | P&E, net | Net additions to P&E |
|---|---|---|---|---|---|---|
| 2021 | 62,202 | 18,532 | 29.8% | 10,653 | 43,245 | — |
| 2022 | 80,096 | 22,841 | 28.5% | 9,876 | 60,324 | — |
| 2023 | 90,757 | 24,631 | 27.1% | 12,531 | 72,701 | 24,843 |
| 2024 | 107,556 | 39,834 | 37.0% | 13,320 | 110,683 | 53,267 |
| 2025 | 128,725 | 45,606 | 35.4% | 21,450 | 190,055 | 96,496 |

The 2024 margin jump from 27.1% to 37.0% is the year of the 5→6 year server extension; the
FY2024 10-K attributes it directly: AWS operating income rose "due to increased sales,
decreased payroll and related expenses, and **a reduction in depreciation and amortization
expense from our change in the estimated useful lives of our servers**". The 2025 margin then
gives back 1.6 points in the reversal year. **AWS P&E net additions (96,496) exceeded AWS
revenue less operating income in 2025 — the segment consumed more plant than it earned.**

### Remaining performance obligation

Amazon does **not** use the caption "remaining performance obligations". The equivalent
disclosure sits in Note 1 under Unearned Revenue:

| As of | Commitments not yet recognized (contracts >1yr) | Recognition period, as disclosed |
|---|---|---|
| Dec 31 2024 | **~$177 bn** | "The weighted average remaining life of our long-term contracts is 4.1 years." |
| Dec 31 2025 | **~$244 bn** | "The weighted average remaining life of our long-term contracts is 4.1 years." |

"primarily related to AWS ... The amount and timing of revenue recognition will be driven by
customer usage and our performance in accordance with contractual obligations, which can
extend beyond the original contractual duration and commitment." Separately, total unearned
revenue on the balance sheet was $24.6bn (2024) and $25.0bn (2025).

### Return on equity

| CY | Net income | Equity, year-end | Average equity | ROE |
|---|---|---|---|---|
| 2021 | 33,364 | 138,245 | 115,824 | 28.8% |
| 2022 | (2,722) | 146,043 | 142,144 | (1.9)% |
| 2023 | 30,425 | 201,875 | 173,959 | 17.5% |
| 2024 | 59,248 | 285,970 | 243,922 | 24.3% |
| 2025 | 77,670 | 411,065 | 348,518 | 22.3% |

(2020 year-end equity 93,404, used as the opening balance for the 2021 average.)

---
## PEER 3 — ORACLE CORPORATION (ORCL) — THE STRESS CASE

FY ends May 31. FY2026 = year ended May 31, 2026.

### Cash-flow inputs, as filed

| FY | OCF | SBC | Capex | Depreciation | Amortization of intangibles | Revenue |
|---|---|---|---|---|---|---|
| 2022 | 9,539 | 2,613 | 4,511 | 1,972 | 1,150 | 42,440 |
| 2023 | 17,165 | 3,547 | 8,695 | 2,526 | 3,582 | 49,954 |
| 2024 | 18,673 | 3,974 | 6,866 | 3,129 | 3,010 | 52,961 |
| 2025 | 20,821 | 4,674 | 21,215 | 3,867 | 2,307 | 57,399 |
| 2026 | 31,977 | 4,811 | **55,663** | **7,623** | 1,671 | 67,357 |

Capex picture beyond the cash line, as disclosed separately:

| FY | Unpaid capital expenditures (non-cash) | Proceeds from short-term financing **related to capital expenditures**, net | Finance-lease ROU assets inside P&E, net |
|---|---|---|---|
| 2024 | 1,637 | — | — |
| 2025 | 2,970 | 1,422 | 2,900 |
| 2026 | **5,279** | **3,345** | **7,500** |

Oracle now funds part of its capital programme through a financing line that appears in
**financing** activities, not investing — "Proceeds from short-term financing related to
capital expenditures, net", $3,345m in FY2026. Cash capex alone therefore understates the
FY2026 capital bill. Construction in progress on the balance sheet is **39,973** at May 31
2026 against 16,510 a year earlier: a further ~$40bn of plant is not yet in service and not
yet depreciating.

### Owner earnings, both ends — the capex end is deeply negative

| FY | OE, capex end | OE, D&A end (depreciation only) | Capex ÷ depreciation | Capex ÷ revenue |
|---|---|---|---|---|
| 2022 | 2,415 | 4,954 | 2.29× | 10.6% |
| 2023 | 4,923 | 11,092 | 3.44× | 17.4% |
| 2024 | 7,833 | 11,570 | 2.19× | 13.0% |
| 2025 | **(5,068)** | 12,280 | **5.49×** | 37.0% |
| 2026 | **(28,497)** | 19,543 | **7.30×** | **82.6%** |

**Answer to the direct question: yes.** Oracle's owner earnings at the capex end are negative
in FY2025 and FY2026, and FY2026 is negative by **$28.5 billion** — larger in absolute terms
than the company's entire operating cash flow ($31,977) less SBC. Capex is **82.6% of
revenue**. Capex is **7.3× depreciation**. Oracle is spending seven dollars of plant for every
dollar of plant it charges against earnings, and funding the gap with debt.

### Total debt

| As of | Notes payable & other borrowings, current | Non-current | **Total debt** | Total stockholders' equity |
|---|---|---|---|---|
| May 31 2022 | 3,749 | 72,110 | **75,859** | **(5,768)** *(deficit)* |
| May 31 2023 | 4,061 | 86,420 | **90,481** | 1,556 |
| May 31 2024 | 10,605 | 76,264 | **86,869** | 9,239 |
| May 31 2025 | 7,271 | 85,297 | **92,568** | 20,969 |
| May 31 2026 | 7,199 | **122,342** | **129,541** | 43,056 |

Debt rose $36,973m in FY2026 alone. Financing activities show proceeds from senior notes,
term loans and other borrowings of **$46,093m** in FY2026 (FY2025: $19,548m), plus $4,954m of
mandatory convertible preferred stock issued net of costs — a new instrument in FY2026. Cash
paid for interest was $3,896m in FY2026. Buybacks have effectively stopped: $95m in FY2026
against $16,248m in FY2022.

### Depreciation life

**FY2016 vintage:** no server-specific life disclosed; the property note gives an aggregate
range. **Not found in filings** as a separately stated server life for FY2016.

**Change 1 — Q1 FY2023 (effective June 1, 2022), servers 4→5 years.** FY2023 10-K, verbatim:

> "During the first quarter of fiscal 2023, we completed an assessment of the useful lives of
> our servers and increased the estimate of the useful lives from four years to five years
> effective at the beginning of fiscal 2023. Based on the carrying value of our servers as of
> May 31, 2022, this change in accounting estimate **decreased our total operating expenses by
> $434 million during fiscal 2023**."

No net-income or per-share effect was disclosed for this change — an incomplete disclosure
relative to what Alphabet, Amazon and Microsoft each gave for their equivalent changes.

**Change 2 — Q1 FY2025 (effective June 1, 2024), servers and networking equipment 5→6 years.**
FY2025 10-K, verbatim:

> "During the first quarter of fiscal 2025, we completed an assessment of the useful lives of
> our servers and networking equipment and increased the estimate of the useful lives from five
> years to six years, effective at the beginning of fiscal 2025. Based on the carrying value of
> our servers and networking equipment as of May 31, 2024, this change in accounting estimate
> **decreased our total operating expenses by $733 million and increased our net income by $573
> million, or $0.21 per basic and $0.20 per diluted share**, during fiscal 2025."

**No further change and NO REVERSAL in FY2026.** The FY2026 property note still reads
"Computer, network, machinery and equipment | 1-6 years", footnoted "Comprised primarily of
servers and networking equipment with estimated useful life of **six years**."

Oracle does, however, carry a risk factor that names the exposure: "We typically depreciate
these assets over their estimated useful lives, **which could be shortened should our cloud
strategies change, which could adversely affect our profitability**", and, on AI accelerators,
"industry supply capacity for AI accelerators ... is competitive, and we at times have to
accept less favorable terms ... it has **increased excess and obsolescence risk** of such
hardware products."

### Cloud revenue — and the absence finding on cloud segment operating income

**ABSENCE FINDING. Oracle does not file a cloud segment operating income, and there is no
cloud reportable segment.** From the FY2026 10-K: "We have three businesses: **cloud and
software** (formerly referred to as cloud and license); **hardware**; and **services**. Each
business is comprised of a single operating segment." Cloud is a *revenue line*, not a
segment. There is no figure in any Oracle filing comparable to AWS operating income or Google
Cloud operating income. The nearest disclosure is the cloud-and-software business margin,
which bundles cloud infrastructure with legacy software licence support — a mix that carries
support-contract economics, not cloud-infrastructure economics.

| FY | Cloud revenue, as filed | Total revenue | Cloud % of total |
|---|---|---|---|
| 2022 | **not separately disclosed** | 42,440 | — |
| 2023 | **not separately disclosed** | 49,954 | — |
| 2024 | 19,774 | 52,961 | 37% |
| 2025 | 24,506 | 57,399 | 43% |
| 2026 | 33,989 | 67,357 | 51% |

A pure "Cloud" line first appeared on the face of Oracle's income statement in the **FY2026**
10-K, which recast FY2024 and FY2025 onto the new presentation. For FY2022 and FY2023 the
income statement shows only "Cloud services and license support" — 30,174 (FY2022) and 35,307
(FY2023) — which **combines cloud with software licence support** and is not comparable to
AWS or Google Cloud revenue. Do not use those two numbers as cloud revenue.

Cloud-and-software business revenue (the segment that contains cloud): 58,530 in FY2026 vs
49,230 in FY2025; 87% and 86% of total revenue respectively.

### Remaining performance obligation

| As of | RPO | Recognition period, as disclosed |
|---|---|---|
| May 31 2025 | **$137.8 bn** | "approximately 33% as revenues over the next twelve months, 41% over the subsequent month 13 to month 36, 23% over the subsequent month 37 to month 60 and the remainder thereafter" |
| May 31 2026 | **$638 bn** | "approximately 12% as revenues over the next twelve months, 34% over the subsequent month 13 to month 36, 34% over the subsequent month 37 to month 60 and the remainder thereafter" |

A **4.6× increase in one year**, "primarily attributable to certain significant cloud
contracts that were entered into during the period." Note what the recognition profile does:
the share landing in the next twelve months falls from 33% to **12%**. In dollars the
next-twelve-months slice is ~$45bn (2025) against ~$77bn (2026), so the near book grew, but
the great bulk of the $638bn sits beyond three years and is backed by a capital programme
Oracle has not yet built or paid for.

### Return on equity — REFUSED AS UNINTERPRETABLE

| FY | Net income | Equity, year-end | Average equity | ROE as computed |
|---|---|---|---|---|
| 2022 | 6,717 | (5,768) | 92 | 7301% |
| 2023 | 8,503 | 1,556 | (2,106) | (404)% |
| 2024 | 10,467 | 9,239 | 5,398 | 194% |
| 2025 | 12,443 | 20,969 | 15,104 | 82.4% |
| 2026 | 17,087 | 43,056 | 32,012 | 53.4% |

**Oracle's ROE is not a usable number and is not reported as one.** Oracle's stockholders'
equity was a **deficit of $5,768m** at May 31 2022 (May 31 2021: $5,952m positive), the
product of $16.2bn of buybacks in FY2022 alone. The denominator crosses through zero between
FY2022 and FY2023, which makes the ratio produce a 7301% and a negative 404% that mean
nothing about returns. The FY2025 and FY2026 figures are computed on an equity base that is
being rebuilt by retained earnings and a preferred issuance, not on a stable capital base.
**Comparing Oracle's ROE with Alphabet's or Amazon's would be a category error.** The honest
statement is that Oracle has bought back so much stock that it has no meaningful equity base
against which to measure return.

---
## MSFT — DEPRECIATION LIFE ONLY (subject company, for the cross-company table)

**FY2016 vintage:** "computer software developed or acquired for internal use, three to seven
years; **computer equipment, two to three years**".

**Change 1 — July 2020 (effective FY2021), server equipment 3→4 years, network equipment
2→4 years.** FY2021 10-K, verbatim:

> "In July 2020, we completed an assessment of the useful lives of our server and network
> equipment and determined we should increase the estimated useful life of server equipment from
> three years to four years and increase the estimated useful life of network equipment from two
> years to four years. This change in accounting estimate was effective beginning fiscal year
> 2021. Based on the carrying amount of server and network equipment included in property and
> equipment, net as of June 30, 2020, the effect of this change in estimate for fiscal year 2021
> was an **increase in operating income of $2.7 billion and net income of $2.3 billion, or $0.30
> per both basic and diluted share**."

**Change 2 — July 2022 (effective FY2023), server AND network equipment 4→6 years.** FY2023
10-K, verbatim:

> "In July 2022, we completed an assessment of the useful lives of our server and network
> equipment. Due to investments in software that increased efficiencies in how we operate our
> server and network equipment, as well as advances in technology, we determined we should
> increase the estimated useful lives of both server and network equipment **from four years to
> six years**. This change in accounting estimate was effective beginning fiscal year 2023. Based
> on the carrying amount of server and network equipment included in property and equipment, net
> as of June 30, 2022, the effect of this change in estimate for fiscal year 2023 was an
> **increase in operating income of $3.7 billion and net income of $3.0 billion, or $0.40 per
> both basic and diluted share**."

MSFT's own FY2023 10-K confirms the mechanical result: "**depreciation expense declined in
fiscal year 2023**" — to $11.0bn from $12.6bn in FY2022 — "due to the change in estimated
useful lives of our server and network equipment", in a year capex rose from 23,886 to 28,107.

**No change and NO REVERSAL through FY2026.** FY2025 and FY2026 property notes still give
"servers and network equipment, **two to six years**". No change-in-accounting-estimate
disclosure appears in the FY2025 or FY2026 10-K. *(The FY2026 note renames the class from
"computer equipment" to "servers and network equipment"; the range is unchanged.)*

MSFT ratios, for the comparison (FY ends June 30):

| FY | OCF | SBC | Capex | Depreciation (P&E note) | Revenue | OE capex end | OE D&A end | Capex ÷ dep | Capex ÷ rev |
|---|---|---|---|---|---|---|---|---|---|
| 2022 | 89,035 | 7,502 | 23,886 | 12,600 | 198,270 | 57,647 | 68,933 | 1.90× | 12.0% |
| 2023 | 87,582 | 9,611 | 28,107 | 11,000 | 211,915 | 49,864 | 66,971 | 2.56× | 13.3% |
| 2024 | 118,548 | 10,734 | 44,477 | 15,200 | 245,122 | 63,337 | 92,614 | 2.93× | 18.1% |
| 2025 | 136,162 | 11,974 | 64,551 | 22,000 | 281,724 | 59,637 | 102,188 | 2.93× | 22.9% |
| 2026 | 182,935 | 12,405 | 115,948 | 34,300 | 331,839 | 54,582 | 136,230 | 3.38× | 34.9% |

MSFT's cash capex materially understates its capital programme: **finance-lease right-of-use
assets obtained** were 11,633 (FY2024), 20,511 (FY2025) and **24,608 (FY2026)** — a further
$24.6bn of data-centre plant in FY2026 that never touches the investing section. Purchases of
P&E remaining in accounts payable were **$26.7bn** at June 30 2026 against $6.9bn a year
earlier. Adding finance-lease additions to cash capex puts the FY2026 capital bill at roughly
**$140.6bn on $331.8bn of revenue (42%)** against $34.3bn of depreciation — a capex/D&A of
about **4.1×**.

---
## THE CROSS-COMPANY DEPRECIATION-LIFE TABLE

| | Server life, ~10 yrs ago | Extensions, with effective date and the filing's own dollar effect | Life today | Reversed? |
|---|---|---|---|---|
| **MSFT** | **2-3 yrs** (FY2016 note: "computer equipment, two to three years") | **Jul 2020**, eff. FY2021: server 3→4, network 2→4. **+$2.7bn operating income, +$2.3bn NI, $0.30/sh**<br>**Jul 2022**, eff. FY2023: both 4→**6**. **+$3.7bn operating income, +$3.0bn NI, $0.40/sh** | **6 yrs** | **No** |
| **GOOGL** | **3 yrs** (FY2015 note gives a 2-5 yr range; the 3-yr server life is stated in the Jan 2021 change disclosure) | **Jan 2021**, eff. FY2021: servers 3→4, certain network 3→5. **−$2.6bn depreciation, +$2.0bn NI, $3.02 basic/$2.98 diluted**<br>**Jan 2023**, eff. FY2023: servers 4→**6**, certain network 5→6. **−$3.9bn depreciation, +$3.0bn NI, $0.24/sh** | **6 yrs** | **No** |
| **AMZN** | **3 yrs** (FY2015 note: "three years for our servers, five years for networking equipment") | **Jan 2020**: servers 3→4. **−$2.7bn D&A, +$2.0bn NI, $4.06/basic sh** (pre-split)<br>**Jan 2022**: servers 4→5, network 5→6. **−$3.6bn D&A, +$2.8bn NI, $0.28/sh**<br>**Jan 2024**: servers 5→**6**. **−$3.2bn D&A, +$2.5bn NI, $0.23/sh** (guided $3.1bn)<br>**Jan 2025 — REVERSAL: subset of servers & network 6→5. +$1.4bn D&A, −$1.0bn NI, −$0.10/sh, "primarily impacted our AWS segment"** (guided −$0.7bn), plus **$920m accelerated depreciation** booked Q4 2024 for early retirements and a further ~$0.6bn into 2025 | **5-6 yrs** | **YES — the only one** |
| **ORCL** | **not separately disclosed** (FY2016 note gives an aggregate range only) | **Q1 FY2023** (eff. Jun 1 2022): servers 4→5. **−$434m total operating expenses.** No NI or per-share effect disclosed<br>**Q1 FY2025** (eff. Jun 1 2024): servers & network 5→**6**. **−$733m operating expenses, +$573m NI, $0.21 basic/$0.20 diluted** | **6 yrs** | **No** |

### What the table says about the MSFT question

1. **MSFT's six-year life is industry-standard, not an outlier.** All four sit at six years at
   the top of the range. MSFT was, however, **first to six** (effective FY2023, July 2022),
   ahead of Alphabet (January 2023), Amazon (January 2024) and Oracle (June 2024). It got
   there from the *shortest* starting point (2-3 years in FY2016), so its cumulative
   extension is the largest: two-to-three years out to six.

2. **Cumulative disclosed benefit, per each company's own filings.** MSFT $6.4bn of operating
   income across two changes ($2.7bn FY2021 + $3.7bn FY2023). Alphabet $6.5bn of depreciation
   reduction across two ($2.6bn + $3.9bn). Amazon **$9.5bn of D&A reduction across three**
   ($2.7bn + $3.6bn + $3.2bn) — the largest — **but it has since handed $1.4bn of that back**,
   net $8.1bn. Oracle $1.2bn across two, and it is the only one that did not disclose a
   net-income effect for its first change.

3. **One peer has reversed, and it is the one closest to MSFT's business.** Amazon cut a
   subset of servers and networking equipment back from six years to five effective January
   1 2025, and said why in plain terms: "**the increased pace of technology development,
   particularly in the area of artificial intelligence and machine learning**", with the
   effect landing "primarily" on AWS. It also took $920m of accelerated depreciation for
   early retirements in Q4 2024. Amazon has seen inside its own AI fleet and concluded the
   six-year assumption was wrong for part of it. Neither MSFT, Alphabet nor Oracle has yet
   made that adjustment.

4. **The reversal cost double the guidance.** Amazon guided ~$0.7bn of 2025 operating income;
   the realized number was $1.4bn of extra D&A and $1.0bn of net income. A life reversal is
   not reliably estimable in advance even by the company doing it.

5. **Nobody's depreciation is keeping up with anybody's replacement bill.** Every peer's
   capex/D&A is above 2× and rising; Oracle is at 7.3×. The six-year life was adopted across
   the industry in a window when capex was 10-13% of revenue. It is now 22.7% (GOOGL), 18.4%
   (AMZN), 34.9% (MSFT cash-only) and 82.6% (ORCL). The assumption has not been re-tested
   against the new spending level by three of the four.

---
## COMPARISON TABLES

### Owner earnings, capex end ($m)

| FY | GOOGL | AMZN | ORCL | MSFT |
|---|---|---|---|---|
| −4 | 51,636 (2021) | (27,483) (2021) | 2,415 (FY22) | 57,647 (FY22) |
| −3 | 40,648 (2022) | (36,514) (2022) | 4,923 (FY23) | 49,864 (FY23) |
| −2 | 47,035 (2023) | 8,194 (2023) | 7,833 (FY24) | 63,337 (FY24) |
| −1 | 49,979 (2024) | 10,867 (2024) | (5,068) (FY25) | 59,637 (FY25) |
| latest | **48,313** (2025) | **(11,772)** (2025) | **(28,497)** (FY26) | **54,582** (FY26) |

### Owner earnings, D&A end ($m)

| FY | GOOGL | AMZN (P&E D&A) | ORCL | MSFT |
|---|---|---|---|---|
| −4 | 66,003 | 10,670 | 4,954 | 68,933 |
| −3 | 58,658 | 2,231 | 11,092 | 66,971 |
| −2 | 67,340 | 30,698 | 11,570 | 92,614 |
| −1 | 87,203 | 61,799 | 12,280 | 102,188 |
| latest | **118,624** | **78,187** | **19,543** | **136,230** |

### Capex ÷ D&A — the single most important row

| FY | GOOGL | AMZN | ORCL | MSFT |
|---|---|---|---|---|
| −4 | 2.40× | 2.67× | 2.29× | 1.90× |
| −3 | 2.34× | 2.56× | 3.44× | 2.56× |
| −2 | 2.70× | 1.74× | 2.19× | 2.93× |
| −1 | 3.43× | 2.59× | 5.49× | 2.93× |
| latest | **4.33×** | **3.15×** | **7.30×** | **3.38×** *(≈4.1× incl. finance leases)* |

### Capex ÷ revenue

| FY | GOOGL | AMZN | ORCL | MSFT |
|---|---|---|---|---|
| −4 | 9.6% | 13.0% | 10.6% | 12.0% |
| −3 | 11.1% | 12.4% | 17.4% | 13.3% |
| −2 | 10.5% | 9.2% | 13.0% | 18.1% |
| −1 | 15.0% | 13.0% | 37.0% | 22.9% |
| latest | **22.7%** | **18.4%** | **82.6%** | **34.9%** *(≈42% incl. finance leases)* |

### Cloud segment margin

| FY | AWS rev / OI / margin | Google Cloud rev / OI / margin | Oracle |
|---|---|---|---|
| 2021 | 62,202 / 18,532 / **29.8%** | 19,206 / (2,282) / **(11.9)%** | no cloud segment |
| 2022 | 80,096 / 22,841 / **28.5%** | 26,280 / (1,922) / **(7.3)%** | no cloud segment |
| 2023 | 90,757 / 24,631 / **27.1%** | 33,088 / 1,716 / **5.2%** | no cloud segment |
| 2024 | 107,556 / 39,834 / **37.0%** | 43,229 / 6,112 / **14.1%** | no cloud segment |
| 2025 | 128,725 / 45,606 / **35.4%** | 58,705 / 13,910 / **23.7%** | no cloud segment |

### Remaining performance obligation

| Peer | Prior year | Latest | Growth | Recognition period |
|---|---|---|---|---|
| GOOGL | $93.2bn (Dec 2024) | **$242.8bn** (Dec 2025) | 2.6× | just over 50% within 24 months |
| AMZN | ~$177bn (Dec 2024) | **~$244bn** (Dec 2025) | 1.4× | weighted-average remaining life 4.1 yrs |
| ORCL | $137.8bn (May 2025) | **$638bn** (May 2026) | 4.6× | 12% within 12 mo; 34% mo 13-36; 34% mo 37-60 |

### Return on equity

| FY | GOOGL | AMZN | ORCL |
|---|---|---|---|
| −4 | 32.1% | 28.8% | *n/m — equity deficit* |
| −3 | 23.6% | (1.9)% | *n/m — denominator crosses zero* |
| −2 | 27.4% | 17.5% | *n/m* |
| −1 | 32.9% | 24.3% | 82.4% *(on a rebuilding base)* |
| latest | **35.7%** | **22.3%** | 53.4% *(on a rebuilding base)* |

---
## NOT FOUND IN FILINGS

- **Oracle server useful life, FY2016 vintage.** The FY2016 10-K property note gives an
  aggregate range only; no server-specific life is stated.
- **Oracle FY2023 life-change effect on net income or EPS.** Only the $434m operating-expense
  effect is disclosed. The other three companies disclosed net income and per-share effects
  for every change.
- **Oracle cloud revenue for FY2022 and FY2023.** No pure cloud revenue line exists in those
  filings; "Cloud services and license support" bundles cloud with licence support and is not
  comparable.
- **Oracle cloud segment operating income, any year.** No cloud reportable segment exists.
- **Alphabet intangible amortization, FY2023-FY2025, on the cash-flow statement.** Folded into
  "Other" from FY2023; not separately stated on that statement.
- **Amazon "remaining performance obligations" under that caption.** Amazon discloses the
  economically equivalent figure under Unearned Revenue instead; the number and its weighted
  average life are given, but the standard RPO time-bucket table is not.
