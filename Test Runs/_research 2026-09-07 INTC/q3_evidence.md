# INTC: Q3 EVIDENCE FILE (management honesty and rationality)

**Company:** Intel Corporation (CIK 0000050863)
**Compiled:** 2026-09-07
**Status:** EVIDENCE GATHERING ONLY. This file makes no Q3 verdict and is not a clearance.

## Sources actually read

All four documents are local plain-text extractions of the filed HTML, read in full with Python
(`encoding='utf-8'`).

| Short name | File | Document | Period | Notes |
|---|---|---|---|---|
| FY2025 10-K | `FY2025_10K.txt` | Form 10-K | FY ended **Dec 27, 2025** | Auditor's report dated **January 22, 2026** (EY, unqualified, with ICFR opinion) |
| FY2024 10-K | `FY2024_10K.txt` | Form 10-K | FY ended **Dec 28, 2024** | |
| Q2 2026 10-Q | `Q2_2026_10Q.txt` | Form 10-Q | Q2/H1 ended **Jun 27, 2026** | |
| DEF 14A 2026 | `DEF14A_2026.txt` | Proxy statement | 2026 annual meeting | |

**Accession numbers were not present in these text extractions.** No instance found: searched each
file for `accession`, `0000050863-`, and `ACCESSION NUMBER`. Operator rule 4 requires the accession
number be recorded, **this is an open item to be closed from the EDGAR filing index before any Q3
verdict is written.**

**Text-extraction artifact, flagged not smoothed (PRIME RULE 1).** In the Notes to the financial
statements the extractor inserts spaces inside monetary amounts, `$ 2,191`, `( 121 )`, `49 %`.
The same figures appear unspaced in MD&A, `$2,191`, `(121)`. Quotes below are reproduced **as
extracted**; the spacing is an artifact of the HTML-to-text conversion, not of the filing.

**Cross-check performed (operator rule 4).** Total restructuring and other charges of **$2,191M for
2025** was read in two independent places in FY2025 10-K: the MD&A table (line 559, "MD&A 27") and
the Note 7 table (line 1615, "Financial Statements / Notes to Consolidated Financial Statements 81").
They agree. Income taxes paid of **$2,202M for 2024** was likewise read in both the FY2024 10-K cash
flow statement face (line 1253) and the FY2025 10-K Note 8 comparative table (line 1787). They agree.

---

# 1. THE RESTRUCTURING STREAK

## 1.1 What the two 10-Ks name

Three plans are named across the two 10-Ks. Searches run: `Restructuring Plan`, `Restructuring
Program`, `restructuring and other charges`, `2022 Restructuring`, `2024 Restructuring`,
`2025 Restructuring`, `2026 Restructuring`, and the regex `20(0|1)\d Restructuring`.

**No plan earlier than 2022 is named in either 10-K.** The regex `20(0|1)\d Restructuring` (which
would catch a 2016, 2015, 2013 etc. plan) returned **zero hits in all four documents**. Intel's
pre-2022 restructuring history is therefore not in this evidence set; it is UNRESEARCHED, not absent.
`2026 Restructuring` also returned zero hits in all four documents, no fourth plan had been named
as of the Q2 2026 10-Q.

| Plan | Announced | Status per latest filing | Total expected charges, and how that estimate moved |
|---|---|---|---|
| **2022 Restructuring Program** | Q3 2022 | Completed Q1 2024 | ~$1.3B (FY2024 10-K and FY2025 10-K agree) |
| **2024 Restructuring Plan** | Q3 2024 | "expected to be completed in 2026" | **$3.0B → $3.1B → $3.2B** across the three filings |
| **2025 Restructuring Plan** | Q2 2025 | substantial majority done Q4 2025, remainder in 2026 | $2.2B expected; cumulative $2.0B at FY2025, $2.2B at Q2 2026 |

**The 2024 plan's own cost estimate rose in each successive filing.** Verbatim, in order:

> "We expect to recognize total charges of approximately $ 3.0 billion under the 2024 Restructuring
> Plan. The cumulative cost of the 2024 Restructuring Plan as of December 28, 2024, was $ 2.8
> billion."
> — FY2024 10-K, Note 7: Restructuring and Other Charges (line 1697; page marker
> "Financial Statements / Notes to Consolidated Financial Statements 77")

> "In the third quarter of 2024, the 2024 Restructuring Plan was announced and a series of cost and
> capital reduction initiatives were implemented. We have incurred total charges of approximately $
> 3.1 billion under the 2024 Restructuring Plan, which is expected to be completed in 2026 ."
> — FY2025 10-K, Note 7 (line 1615; page marker "… 81")

> "In the third quarter of 2024, the 2024 Restructuring Plan was announced and a series of cost and
> capital reduction initiatives were implemented. We have incurred total charges of approximately $
> 3.2 billion under the 2024 Restructuring Plan, which is expected to be completed in 2026."
> — Q2 2026 10-Q, Note 6: Restructuring and Other Charges (line 502; page marker
> "Financial Statements / Notes to Financial Statements 15")

Note also the FY2024 10-K said the 2024 plan would be "substantially complete by the fourth quarter
of 2025"; it is now running into 2026, i.e. a plan announced in Q3 2024 is still incomplete two
years later, while two further plans were layered on top of it.

## 1.2 Verbatim description of each plan

**2022 Restructuring Program**, from FY2025 10-K, Note 7 (line 1615):

> "In the third quarter of 2022, the 2022 Restructuring Program was approved to rebalance our
> workforce and operations. We have incurred total charges of approximately $ 1.3 billion under the
> 2022 Restructuring Program, which was complete in the first quarter of 2024."

FY2024 10-K, Note 7 (line 1697) gives the fuller version:

> "Charges in 2023 and 2022 primarily related to the 2022 Restructuring Program, which was approved
> to rebalance our workforce and operations in alignment with our strategy and was completed in the
> first quarter of 2024. The cumulative cost of the 2022 Restructuring Program as of December 28,
> 2024 was $ 1.3 billion."

**2024 Restructuring Plan**, from FY2024 10-K, Note 7 (line 1697):

> "In the third quarter of 2024, the 2024 Restructuring Plan was announced, subsequently approved and
> committed to by our management team, and initiated to implement cost-reduction measures, including
> reductions in employee headcount, other operating expenditures, and capital expenditures.
> Restructuring charges are primarily composed of employee severance and benefit arrangements,
> non-cash charges related to asset impairments associated with exit activities, and charges relating
> to real estate exits and consolidations. These charges were included as "corporate unallocated
> expenses" within the restructuring and other category presented in "Note 3: Operating Segments"
> within Notes to Consolidated Financial Statements."

And in the FY2024 10-K MD&A overview (line 314):

> "In 2024, we announced our intention to implement a series of cost and capital reduction
> initiatives designed to adjust our spending to current business trends while enabling our new
> operating model and continuing to fund investments in our core strategy—returning to product and
> process competitiveness. These initiatives, which we refer to as our 2024 Restructuring Plan,
> include reducing headcount, consolidating and reducing our global real estate footprint, conducting
> portfolio reviews of our businesses under a "c[ost]…"

**2025 Restructuring Plan**, from FY2025 10-K, Note 7 (line 1615):

> "In the second quarter of 2025, we announced and commenced the 2025 Restructuring Plan, which was
> subsequently approved and committed to by our management. This initiative is intended to lower
> expenses, streamline our organizational structure and reduce management layers across functions
> while reallocating resources toward our core client and server businesses by reducing
> lower-priority programs and initiatives. Restructuring charges are primarily comprised of employee
> severance and benefit arrangements, non-cash asset impairment and accelerated depreciation charges
> resulting from exit activities, as well as impairment charges relating to real estate exits and
> consolidations. These charges were excluded from our operating segments' results and included as
> "corporate unallocated expenses" within the restructuring and other charges category presented in
> "Note 3: Operating Segments" within Notes to Consolidated Financial Statements. The cumulative cost
> of the 2025 Restructuring Plan as of December 27, 2025 was $ 2.0 billion. Any changes to our
> estimates or timing will be reflected in our results of operations in future periods. We expect to
> recognize total charges of approximately $ 2.2 billion under the 2025 Restructuring Plan. A
> substantial majority of actions pursuant to the 2025 Restructuring Plan were completed in the
> fourth quarter of 2025 with the remainder expected to be completed in 2026."

## 1.3 Total restructuring and other charges by year

From the two Note 7 tables (FY2025 10-K line 1615; FY2024 10-K line 1697) and the Q2 2026 10-Q
Note 6 (line 502). Six consecutive fiscal years plus the current half-year are covered.

| $M | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|---|
| Employee severance and benefit arrangements | 1,038 | 222 | 2,481 | 1,790 | 235 |
| Litigation charges and other | (1,187) | (329) | 858 | (121) | 38 |
| Asset impairment charges | 151 | 45 | 3,631 | 522 | 3,967 |
| **Total restructuring and other charges** | **2** | **(62)** | **6,970** | **2,191** | **4,240** |

Verbatim, FY2025 10-K Note 7 (line 1615):

> "Years Ended (In Millions) 	Dec 27, 2025 	Dec 28, 2024 	Dec 30, 2023 	
>  Employee severance and benefit arrangements 	$ 	1,790 	$ 	2,481 	$ 	222 	
>  Litigation charges and other 	( 121 ) 	858 	( 329 ) 	
>  Asset impairment charges 	522 	3,631 	45 	
>  Total restructuring and other charges 	$ 	2,191 	$ 	6,970 	$ 	( 62 )"

Verbatim, FY2024 10-K Note 7 (line 1697) for the 2022 column:

> "Years Ended (In Millions) 	Dec 28, 2024 	Dec 30, 2023 	Dec 31, 2022 	
>  Employee severance and benefit arrangements 	$ 	2,481 	$ 	222 	$ 	1,038 	
>  Litigation charges and other 	858 	( 329 ) 	( 1,187 ) 	
>  Asset impairment charges 	3,631 	45 	151 	
>  Total restructuring and other charges 	$ 	6,970 	$ 	( 62 ) 	$ 	2"

**Caution on the FY2022 and FY2023 totals.** The near-zero and negative totals are not evidence of
restraint. They are the net of large severance charges against large litigation *benefits*: a
$1.2B benefit in 2022 from an annulled EC fine, and a $1.2B benefit in 2023 from the VLSI
litigation. FY2024 10-K Note 7 (line 1721):

> "In 2023, a $ 1.2 billion benefit was recorded due to the reduction in the previously accrued charge
> as a result of developments in the VLSI litigation. 2023 charges also included a $ 401 million
> charge for an EC-imposed fine and a $ 353 million termination fee in connection with our inability
> to timely obtain required regulatory approvals needed to acquire Tower. In 2009, we recorded and
> paid an EC-imposed fine that was subsequently annulled, which resulted in a benefit of $ 1.2 billion
> in 2022."

On a severance-only basis the streak is unbroken: **$1,038M (2022), $222M (2023), $2,481M (2024),
$1,790M (2025), $235M (H1 2026)**, roughly **$5.8 billion of severance in four and a half years**.

## 1.4 The severance accrual rollforward

FY2025 10-K, Note 7 (line 1615). Note the column headings say "Restructuring **Program**" for all
three while the surrounding prose says "Restructuring **Plan**" for 2025 and 2024, an internal
inconsistency in the filing itself, reproduced here as found:

> "(In Millions) 	2025 Restructuring Program 	2024 Restructuring Program 	2022 Restructuring Program 	
>  Accrued balance as of December 31, 2022 	$ 	— 	$ 	— 	$ 	873 	
>  Accruals and adjustments 	— 	— 	222 	
>  Cash payments 	— 	— 	( 1,013 ) 	
>  Accrued balance as of December 30, 2023 	— 	— 	82 	
>  Accruals and adjustments 	— 	2,306 	— 	
>  Cash payments 	— 	( 2,004 ) 	( 82 ) 	
>  Accrued balance as of December 28, 2024 	— 	302 	— 	
>  Accruals and adjustments 	1,450 	265 	— 	
>  Cash payments 	( 1,033 ) 	( 541 ) 	— 	
>  Accrued balance as of December 27, 2025 	$ 	417 	$ 	26 	$ 	—"

Q2 2026 10-Q, Note 6 (line 502) continues it:

> "(In Millions) 	2025 Restructuring Plan 	
>  Accrued balance as of December 27, 2025 	$ 	417 	
>  Accruals and adjustments 	173 	
>  Cash payments 	( 288 ) 	
>  Accrued restructuring balance as of June 27, 2026 	$ 	302"

## 1.5 The H1 2026 line is not restructuring

The $4,240M H1 2026 "restructuring and other charges" is **93% a goodwill impairment**, booked into
the restructuring caption. Q2 2026 10-Q, Note 6 (line 502):

> "Asset impairment charges incurred in the first six months of 2026 were related to non-cash goodwill
> impairment charges of $ 3.9 billion (see "Note 10: Goodwill" within Notes to Consolidated Condensed
> Financial Statements)."

The same treatment was used in 2024, FY2025 10-K Note 7 (line 1615): "In addition, we recorded
non-cash goodwill impairment charges of $ 3.0 billion in 2024". Because restructuring and other
charges are excluded from segment results as "corporate unallocated expenses" (quoted in 1.2 above),
routing goodwill impairment through this caption removes it from every reported segment margin.

---

# 2. NON-GAAP / EBITDA PROMOTION

## 2.1 EBITDA: no instance found

**Search run:** `EBITDA` (case-insensitive) against all four documents.
**Result: 0 hits in FY2025 10-K, 0 in FY2024 10-K, 0 in Q2 2026 10-Q, 0 in DEF 14A 2026.**
Intel does not present EBITDA or adjusted EBITDA anywhere in this evidence set. On this specific
count the filings are clean.

## 2.2 The one non-GAAP measure: Adjusted Free Cash Flow

Non-GAAP density is low and falling: `non-GAAP` appears **4 times in FY2025 10-K, 9 in FY2024 10-K,
0 in the Q2 2026 10-Q**, and 14 in the DEF 14A. `free cash flow` appears 5 times in each 10-K and
**0 times in the Q2 2026 10-Q**: the measure was dropped from the quarterly report entirely.

Intel flags the measure up front. FY2025 10-K, "Organization of Our Form 10-K" (line 43):

> "The preparation of our Consolidated Financial Statements is in conformity with U.S. GAAP. Our Form
> 10-K includes Adjusted Free Cash Flow, a non-GAAP financial measure we use to evaluate the cash flow
> trends of our business. See "Liquidity and Capital Resources" within MD&A for a description of this
> measure, including why management uses it and why we believe it provides investors with useful
> supplemental information."

## 2.3 The definition, and what it adds back: verbatim

**FY2025 10-K**, MD&A "Liquidity and Capital Resources" → "Adjustments to Cash from Operating
Activities" (line 606; page marker "MD&A 29"):

> "Adjusted Free Cash Flow is a non-GAAP financial measure and an additional means used by management
> to evaluate the cash flow trends of our business as it is viewed as helpful in understanding our
> capital requirements and sources of liquidity. The measure is calculated using cash flow from
> operations and adjusted for the following:
>  ▪ additions to property, plant and equipment, net of proceeds from capital-related government
> incentives and net SCIP partner contributions; and
>  ▪ payments on financing leases.
>  This non-GAAP financial measure should not be considered a substitute for, or superior to, financial
> measures calculated in accordance with U.S. GAAP, and the financial results calculated in accordance
> with U.S. GAAP and reconciliations from these results should be carefully evaluated."

**FY2024 10-K**, MD&A "Non-GAAP Financial Measures" (line 693; page marker "MD&A 30"), note the
third adjustment, which the FY2025 version drops:

> "In addition to disclosing financial results in accordance with US GAAP, this document references
> adjusted free cash flow, a non-GAAP financial measure. This measure is used by management when
> assessing our sources of liquidity, capital resources, and quality of earnings and provides an
> additional means to evaluate the cash flow trends of our business. Adjusted free cash flow is
> operating cash flow adjusted for (1) additions to property, plant, and equipment, net of proceeds
> from capital-related government incentives and net partner contributions, (2) payments on finance
> leases, and (3) proceeds from the McAfee equity sale in 2022."

### What the definition actually does

Two features are worth recording precisely, because both flatter the measure:

1. **Capex is netted against government incentives and SCIP partner contributions before being
   deducted.** The subtracted figure is *net* capex, not gross. In FY2025 gross "Additions to
   property, plant and equipment" in investing was **$14,646M**, plus a further **$3,026M** of
   capex additions sitting in *financing* activities (extended payment terms), against $1,577M of
   incentives received, yet the AFCF reconciliation deducts only **$11,204M**. The measure
   therefore treats partner money and government money as if it reduced the cost of the plant.
2. **In FY2024 the definition explicitly added back "proceeds from the McAfee equity sale in 2022"
   ($4,561M)**, a one-time disposal of an equity stake, counted inside a measure named "free cash
   flow." That $4,561M is 100% of the difference between a 2022 AFCF of $(4,075)M and one of
   $(8,636)M without it. This clause was **removed from the FY2025 definition**, and with it the
   2022 column.

## 2.4 Adjusted Free Cash Flow vs GAAP, every year disclosed

**FY2024 10-K disclosed five years; FY2025 10-K disclosed three.** The disclosure window narrowed
by two years in one filing, dropping the two positive years (2020, 2021) from view.

FY2024 10-K, line 693 (page marker "MD&A 30"), verbatim:

> "Years Ended (In Millions) 	Dec 28, 2024 	Dec 30, 2023 	Dec 31, 2022 	Dec 25, 2021 	Dec 26, 2020 	
>  Net cash provided by (used for) operating activities 	$ 	8,288 	$ 	11,471 	$ 	15,433 	$ 	29,456 	$ 	35,864 	
>  Net purchase of property, plant, and equipment 	(10,515) 	(23,228) 	(23,724) 	(18,567) 	(14,086) 	
>  Payments on finance leases 	(1) 	(96) 	(345) 	— 	— 	
>  Sale of equity investment 	— 	— 	4,561 	— 	— 	
>  Adjusted free cash flow 	$ 	(2,228) 	$ 	(11,853) 	$ 	(4,075) 	$ 	10,889 	$ 	21,778 	
>  Net cash provided by (used for) investing activities 	$ 	(18,256) 	$ 	(24,041) 	$ 	(10,231) 	$ 	(24,283) 	$ 	(21,351) 	
>  Net cash provided by (used for) financing activities 	$ 	11,138 	$ 	8,505 	$ 	1,115 	$ 	(6,211) 	$ 	(12,842)"

FY2025 10-K, line 606 (page marker "MD&A 29"), verbatim:

> "Years Ended (In Millions) 	Dec 27, 2025 	Dec 28, 2024 	Dec 30, 2023 	
>  Net cash provided by (used for) operating activities 	$ 	9,697 	$ 	8,288 	$ 	11,471 	
>  Net purchase of property, plant and equipment (net capital expenditures) 	(11,204) 	(10,515) 	(23,228) 	
>  Payments on finance leases 	(105) 	(1) 	(96) 	
>  Adjusted free cash flow 	$ 	(1,612) 	$ 	(2,228) 	$ 	(11,853) 	
>  Net cash provided by (used for) investing activities 	$ 	(14,821) 	$ 	(18,256) 	$ 	(24,041) 	
>  Net cash provided by (used for) financing activities 	$ 	11,587 	$ 	11,138 	$ 	8,505"

### Combined table, GAAP beside non-GAAP

| $M | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| **GAAP** net cash from operating activities | 35,864 | 29,456 | 15,433 | 11,471 | 8,288 | 9,697 |
| Net purchase of PP&E (as adjusted) | (14,086) | (18,567) | (23,724) | (23,228) | (10,515) | (11,204) |
| Payments on finance leases | — | — | (345) | (96) | (1) | (105) |
| Sale of equity investment (McAfee) | — | — | **4,561** | — | — | — |
| **Non-GAAP Adjusted free cash flow** | **21,778** | **10,889** | **(4,075)** | **(11,853)** | **(2,228)** | **(1,612)** |
| GAAP net cash used for investing | (21,351) | (24,283) | (10,231) | (24,041) | (18,256) | (14,821) |
| GAAP net cash from financing | (12,842) | (6,211) | 1,115 | 8,505 | 11,138 | 11,587 |

**The measure has been negative for four consecutive years (2022-2025), cumulatively $(19.8)B.**
Operating cash flow has fallen from $35.9B to $9.7B in five years, a 73% decline. Intel's own
preferred measure does not flatter the record; it reports a business that has not funded its own
capital programme since 2021.

---

# 3. EARNINGS PROJECTIONS / GUIDANCE / TARGETS

## 3.1 "Five nodes in four years": no instance found

**Searches run:** `five nodes in four years`, `five nodes`, `5 nodes`.
**Result: 0 hits in all four documents.** The slogan that defined the Gelsinger era is not in the
FY2024 10-K, the FY2025 10-K, the Q2 2026 10-Q, or the 2026 proxy. It was not retracted in these
documents; it simply ceased to appear. Whether it appeared in earlier 10-Ks is UNRESEARCHED here.

## 3.2 "On track": no substantive instance found

**Search run:** `on track` (case-insensitive).
**Result: exactly 1 hit per 10-K and 1 in the 10-Q, and in every case it is inside the
forward-looking-statements boilerplate word list**, not an actual claim:

> "Words such as "accelerate", "achieve", "aim", "ambitions", "anticipate", "believe", "committed",
> "continue", "could", "designed", "estimate", "expect", "forecast", "future", "goals", "grow",
> "guidance", "intend", "likely", "may", "might", "milestones", "next generation", "objective", "on
> track", "opportunity", "outlook", "pending", "plan", "position", …"
> — FY2025 10-K, "Forward-Looking Statements" (line 80, page marker "1")

**Intel makes no "on track" assertion anywhere in these filings.**

## 3.3 Forward numeric commitments: there are almost none

**Search run:** regex `we (expect|anticipate|intend|plan|estimate|forecast|target)[^.]{0,240}\$
[\d.]+ (billion|million)` across the FY2025 10-K, excluding the XBRL header.
**Result: three hits, and only one is a business commitment:**

> "We expect to recognize total charges of approximately $ 2.2 billion under the 2025 Restructuring
> Plan." — FY2025 10-K, Note 7 (line 1615)

> "We expect to replace or amend the 364-day $5.0 billion credit facility agreement prior to its
> maturity at the end of January 2026." — FY2025 10-K, MD&A (line 632, and repeated at line 2011)

**There is no revenue, gross margin, operating margin, EPS, or free-cash-flow target anywhere in the
FY2025 10-K.** The only hard numbers about the future are contractual commitments, not forecasts:

> "We adjust the cadence of our investments based on the execution of our roadmap and changing
> business conditions. As of December 27, 2025, we had commitments for capital expenditures of $9.1
> billion for 2026 and had $3.7 billion in capital expenditures committed in the long term. As of
> December 27, 2025, other purchase obligations and commitments in 2026 under our binding commitments
> for purchases of goods and services were $2.2 billion, with an additional $4.5 billion committed in
> the long term."
> — FY2025 10-K, MD&A "Funding Requirements" (line 643, page marker "MD&A 30")

The forward statements that do exist are directional and hedged. The full set of 2026-2028 forward
statements in the FY2025 10-K includes:

> "We operate in a highly competitive market and expect this environment to further intensify in 2026."
> (line 187)

> "We expect these supply constraints to persist into 2026 and industry wide shortages of substrates,
> memory and other critical components may further limit our ability to meet CCG and DCAI customer
> demand in 2026." (line 535)

> "As a result of our 2025 and 2024 Restructuring Plans and other related cost-reduction measures and
> the divestiture of Altera, we expect total R&D and MG&A expenses to decrease in 2026 relative to
> recent historical periods." (line 548)

> "We anticipate that net income attributable to non-controlling interests will continue to increase
> in 2026 as additional tranches of Arizona SCIP's manufacturing assets are placed into service, and
> to increase significantly in 2027 following our expected completion of construction of Fab 34 in
> Ireland." (line 392)

**Assessment for the file:** on the narrow question of *promotional forward numbers in the 10-K*,
Intel is restrained to the point of silence. This is a point in management's favour and should be
recorded as such. Note the limitation: quarterly earnings-call guidance is not in this evidence set.

## 3.4 18A, 14A and external foundry customers: the central admission

This is the most important passage in the FY2025 10-K for Q3 purposes. MD&A / "Our Strategy"
(line 164, page marker "Our Strategy 4"):

> "However, the development and manufacturing of modern leading-edge process technologies,
> particularly those utilizing EUV lithography such as Intel 4, Intel 3, Intel 18A, Intel 14A and
> future nodes, require substantial capital investment. These leading-edge process technologies are
> essential to deliver competitive products, but their cost structure requires manufacturing volumes
> beyond what we expect from our own products to achieve economic efficiency. In light of these
> considerations, in 2025, we streamlined our footprint to improve operational efficiency and better
> align capacity with anticipated demand. We initiated the consolidation of our Costa Rican assembly
> and test operations into our other facilities, which we expect to be completed by the end of 2026,
> slowed the pace of construction for our new Ohio wafer fabrication facility, or fab, and
> discontinued planned expansions in Germany (fab) and Poland (assembly and test facility). Further,
> we announced that if we are unable to secure a significant external foundry customer for Intel 14A,
> we may pause or discontinue our pursuit of Intel 14A and successor leading-edge process
> technologies. In such event, we would expect, over time, to shift manufacturing to third-party
> foundries, particularly TSMC, as we develop products for nodes beyond Intel 18A and its derivative
> node, Intel 18A-P."

The same conditional is elevated to the forward-looking-statements risk list at the very front of the
10-K (line 107, page marker "1"):

> "▪ a potential pause or discontinuation of our pursuit of Intel 14A and other next generation
> leading-edge process technologies if we are unable to secure a significant external customer for
> Intel 14A;"

And the candid admission on the foundry business, "Growing Our External Foundry Business" (line 164,
page marker "Our Strategy 4"):

> "While we have few external customers to date, developing an external foundry business is a key
> long-term strategy for our business and one that we aim to have more success with as we move to more
> advanced nodes."

**No named external foundry customer, and no committed volume figure, appears in any of the four
documents.** Searches run: `committed volume`, `external customer`, `external foundry`, `design win`,
`customer commitment`. The only `committed volume` hits are generic risk-factor and Smart-Capital
language, e.g. FY2024 10-K (line 170):

> "▪ Customer commitments. Our foundry business works closely with potential customers to obtain
> advance payments to secure capacity and participate in manufacturing capacity build-outs. This
> provides us with the advantage of committed volume, derisking investments while providing capacity
> corridors for our foundry customers."

Intel Foundry external revenue is disclosed and is very small. Q2 2026 10-Q, Note 2 (line 329):

> "Intel Foundry also includes certain third-party foundry and assembly and test revenues from
> external customers that totaled $ 293 million in the three months ended June 27, 2026 and $ 467
> million in the first six months of 2026 ($ 22 million in the three months ended June 28, 2025 and $
> 53 million in the first six months of 2025)."

And the 10-Q explains the increase is not new third-party demand but a related party reclassified:

> "External revenue was $293 million in Q2 2026, up $271 million from Q2 2025, and $467 million in YTD
> 2026, up $414 million from YTD 2025, primarily due to Altera's transition to an external customer
> following the deconsolidation of Altera in Q3 2025."
> — Q2 2026 10-Q, MD&A (line 867, page marker "MD&A 31")

**By Q2 2026 the 14A conditional had been resolved in favour of proceeding, but still without a named
customer.** Q2 2026 10-Q, MD&A "Future Node Development and Manufacturing Expansion Projects"
(line 808):

> "We are focused and have made substantial progress in recent periods on the continued development of
> Intel 14A, the next generation node beyond Intel 18A and Intel 18A-P. During Q2 2026, we committed
> to completing development of Intel 14A, with a number of future Intel products designed to utilize
> the node and manufacturing expansion projects underway for production of products on the node. We
> also made continued progress towards meeting performance and design milestones for potential
> significant customers to evaluate Intel 14A for their future products. We intend to accelerate
> various of our manufacturing expansion projects, though the scale and pace of our manufacturing
> expansion projects will ultimately be dictated by the amount of committed demand for Intel 14A that
> we are able to obtain from our Intel products roadmap and design wins with potential significant
> external customers."

Note the sequence: FY2025 10-K (Jan 2026) says the node may be abandoned without a significant
external customer; Q2 2026 10-Q (Jul 2026) says the company has "committed to completing development"
while customers are still only "potential" and "evaluat[ing]". The commitment was made before the
stated precondition for it was met.

## 3.5 A prior-year forecast that can be scored

FY2024 10-K (line 241) made one checkable prediction:

> "We expect to commence high-volume manufacturing of Panther Lake, our new client family of products
> and our first processors on Intel 18A, in 2025."

FY2025 10-K (line 163) reports the outcome:

> "In 2025, we released our initial Intel Core Ultra Series 3 processors, the first products to be
> manufactured using our new Intel 18A process technology."

And Q2 2026 10-Q (line 808):

> "At the start of 2026, we released our first products manufactured on Intel 18A, our most advanced
> leading-edge semiconductor manufacturing technology, or node, in high volume production."

The FY2024 promise was "high-volume manufacturing … in 2025"; the FY2025 10-K claims a *release* in
2025, and the 10-Q dates *high volume production* to "the start of 2026". **The high-volume
milestone slipped past the year it was promised for, and the slip is visible only by reading the
three documents against each other, it is never stated as a miss.**

---

# 4. SEGMENT / METRIC SWITCHING [E2-49]

**The segment structure changed in three consecutive years: FY2024, FY2025, and FY2026.** In each
case prior periods were restated, so no reported segment series survives more than about two years
on a consistent basis.

## 4.1 Change 1, Q1 2024: internal foundry model; Altera moved out of DCAI

FY2024 10-K, Note 3: Operating Segments (line 1406; page marker at line 1443 area):

> "We previously announced the implementation of our internal foundry operating model, which took
> effect in the first quarter of 2024, and creates a foundry relationship between our Intel Products
> business (collectively CCG, DCAI, and NEX) and our Intel Foundry business. … We also previously
> announced our intent to operate Altera as a standalone business. Altera was previously included in
> our DCAI segment results and, beginning in the first quarter of 2024, is included in "all other." As
> a result of these changes, we modified our segment reporting in the first quarter of 2024 to align
> to this new operating model. All prior period segment data has been retrospectively adjusted to
> reflect the way our CODMs internally receive information and manage and monitor our operating
> segment performance. There are no changes to our Consolidated Financial Statements for any prior
> periods."

Structure as of FY2024:

> "We organize our business as follows:
>  ▪ Intel Products:
>  ▪ Client Computing Group (CCG)
>  ▪ Data Center and AI (DCAI)
>  ▪ Network and Edge (NEX)
>  ▪ Intel Foundry
>  ▪ All other:
>  ▪ Altera
>  ▪ Mobileye
>  ▪ Other
>  CCG, DCAI, and Intel Foundry qualify as reportable operating segments. NEX, Altera, and Mobileye do
> not qualify as reportable operating segments; however, we have elected to disclose certain of their
> results."

## 4.2 Change 2, Q1 2025: NEX dissolved into CCG and DCAI

FY2025 10-K, MD&A "Operating Segment Results" (line 403, page marker "MD&A 20"):

> "In Q1 2025, we made an organizational change to integrate NEX into CCG and DCAI and modified our
> segment reporting to align to this and certain other business reorganizations. All prior period
> segment data has been retrospectively adjusted to reflect the way our CODM internally receives
> information and manages and monitors our operating segment performance. There were no changes to our
> Consolidated Financial Statements for any prior periods."

FY2025 10-K, Note 3: Operating Segments (line 1347):

> "In the first quarter of 2025, we made an organizational change to integrate our NEX business into
> CCG and DCAI and modified our segment reporting to align to this and certain other business
> reorganizations. All prior period segment data have been retrospectively adjusted to reflect the way
> our CODM internally receives information and manages and monitors our operating segment performance
> starting in fiscal year 2025. Additionally, effective September 12, 2025, we completed the
> divestiture of 51 % of Altera. As of that date, Altera's results of operations are no longer included
> in our consolidated or segment results. Altera's financial results were included within our "all
> other" category for all periods presented through September 11, 2025."

**A reporting unit with $2.78 billion of goodwill was dissolved and the goodwill pushed into the two
surviving segments.** FY2025 10-K, Note 11: Goodwill (line 1910):

> "As described in "Note 3: Operating Segments" within the Notes to Consolidated Financial Statements,
> in the first quarter of 2025, we made an organizational change to integrate our NEX business into CCG
> and DCAI and modified our segment reporting to align to this and certain other business
> reorganizations. As a result, of the total $ 2.8 billion of goodwill previously allocated to NEX, we
> reallocated $ 1.8 billion to CCG and $ 1.0 billion to DCAI on a relative fair value basis. We
> performed a quantitative impairment assessment for each of our reporting units immediately before and
> after our business reorganization, concluding that goodwill was not impaired."

The rollforward, FY2025 10-K Note 11 (line 1884; page marker "… 89"):

> "(In Millions) 	Dec 28, 2024 	Divestitures 	Transfers 	Impairments 	Dec 27, 2025 	
>  Client Computing 	$ 	4,619 	$ 	— 	$ 	1,865 	$ 	— 	$ 	6,484 	
>  Data Center and AI 	7,944 	— 	1,001 	— 	8,945 	
>  Network and Edge 	2,780 	— 	( 2,780 ) 	— 	— 	
>  Mobileye 1 	8,306 	— 	— 	— 	8,306 	
>  Altera 	781 	( 781 ) 	— 	— 	— 	
>  All Other 	263 	— 	( 86 ) 	— 	177 	
>  Total 	$ 	24,693 	$ 	( 781 ) 	$ 	— 	$ 	— 	$ 	23,912"

**Point to hold for Q3:** a reporting unit whose goodwill was tested "immediately before and after"
the reorganisation and found unimpaired ceased to exist as a testable unit at that moment. Its
goodwill now sits inside two much larger, profitable segments where it is far harder to impair. Note
the prior-year column of the same table: Intel Foundry received $222M of goodwill by transfer in 2024
and impaired the entire $222M in the same year.

## 4.3 Change 3, 2026: CCG renamed CCPG

Q2 2026 10-Q, Note 2: Operating Segments (line 329):

> "We organize and manage our business as follows:
>  ▪ Intel Products:
>  ▪ Client Computing and Physical AI Group (CCPG), formerly the Client Computing Group (CCG)
>  ▪ Data Center and AI (DCAI)
>  ▪ Intel Foundry
>  ▪ All Other
>  ▪ M obileye
>  ▪ Other
>  CCPG, DCAI and Intel Foundry are our reportable operating segments."

*(the "M obileye" spacing is an extraction artifact, reproduced not smoothed)*

Confirmed in the Key Terms glossary, Q2 2026 10-Q (line 752):

> "CCPG 	Client Computing and Physical AI Group operating segment, formerly the Client Computing Group
> (CCG)"

The user's hypothesis is confirmed: **CCG → CCPG**. "Physical AI" was added to the name of the PC
segment. `CCPG` returns 21 hits in the Q2 2026 10-Q and **0 hits in both 10-Ks**; `CCG` returns 45 in
FY2025 10-K, 31 in FY2024 10-K, and only 3 residual hits in the 10-Q.

## 4.4 Change 4: the segment *measure* changed too, mid-2025

This is a separate switch from the structure changes and is easy to miss. FY2025 10-K, Note 3
(line 1378):

> "Our CEO is our CODM. The CODM uses segment revenue and segment operating income (loss) to evaluate
> each segment's performance and allocate resources. … Segment operating results regularly reviewed by
> our CODM also include total cost of sales and operating expenses directly attributable to each
> segment. **Prior to the second quarter of 2025, our CODM regularly reviewed cost of sales and
> operating expenses, on a discrete basis, attributable to each segment. We have recast prior period
> segment operating results to reflect the significant segment-level expenses as currently reviewed by
> our CODM.**" *(emphasis added)*

Compare FY2024 10-K, Note 3 (line 1443), which reported a **gross margin** measure that has since
disappeared:

> "Our interim Co-Chief Executive Officers are our CODMs. The CODMs primarily use operating income
> (loss) to evaluate each segment's performance and allocate resources. … While operating income (loss)
> is the primary measure used by our CODMs to allocate resources, they often review materials that
> present operating segment gross margin. Accordingly, we have included gross margin as a secondary
> measure within the accompanying reconciliation of our operating segment and consolidated results. The
> measures regularly provided to and used by our CODMs under our new operating model continue to
> evolve; currently, our CODMs do not regularly review or receive discrete asset information by
> operating segment."

**Segment gross margin was disclosed in FY2024 and is not disclosed in FY2025.** Segment-level
discrete cost of sales and opex was reviewed and disclosed until Q2 2025 and was then recast away.

## 4.5 The CODM itself changed

- **FY2024 10-K:** "Our interim Co-Chief Executive Officers are our **CODMs**" (plural).
- **FY2025 10-K and Q2 2026 10-Q:** "Our CEO is our **CODM**" (singular).

The glossary changed with it, FY2024: "CODMs 	Chief operating decision makers"; FY2025:
"CODM 	Chief operating decision maker".

## 4.6 Summary of every segment-definition change

| Fiscal year | Change | Prior periods restated? |
|---|---|---|
| **FY2024 (Q1)** | Internal foundry model split Intel Products / Intel Foundry; Altera moved from DCAI to "all other" | Yes, "retrospectively adjusted" |
| **FY2025 (Q1)** | NEX dissolved into CCG and DCAI; $2.78B goodwill reallocated | Yes, "retrospectively adjusted" |
| **FY2025 (Q3)** | Altera deconsolidated 12 Sep 2025 on sale of 51% | Prospective from close date |
| **FY2025 (Q2)** | Segment *measure* changed: discrete segment cost of sales/opex replaced; gross margin dropped | Yes, "We have recast prior period segment operating results" |
| **FY2025** | CODM changed from interim Co-CEOs (plural) to CEO (singular) | n/a |
| **FY2026** | CCG renamed **CCPG** (Client Computing and Physical AI Group) | Renaming; comparatives presented under new name |

## 4.7 A related disclosure line that disappeared

Not a segment change, but the same pattern of a line item appearing once and then being absorbed.
FY2024 10-K, Note 12: Identified Intangible Assets (line 1915) disclosed **Internal-use software** as
its own line, $128M gross, $(73)M accumulated amortization, $55M net, 5-year life, $24M of
amortization. In the FY2025 10-K, Note 12 (line 1914) that line is **gone**, folded into a renamed
"Licensed technology, patents and other" line. The arithmetic confirms the merge exactly: FY2024's
Licensed technology and patents ($3,387 / $(1,852) / $1,535) + Internal-use software ($128 / $(73) /
$55) + Other non-amortizing ($4 / nil / $4) = **$3,519 / $(1,925) / $1,594**, which is precisely the
restated FY2024 comparative shown in the FY2025 10-K. See section 8.

---

# 5. PAY VERSUS PERFORMANCE (Item 402(v)): DEF 14A 2026

## 5.1 The Company-Selected Measure

DEF 14A, page 78, "Company Selected Measure":

> "Company Selected Measure. Revenue (Non-GAAP) is the financial measure that was determined to be the
> most important financial performance measure linking "compensation actually paid" to our NEOs to
> company performance for 2025 and therefore was selected as the 2025 "Company-Selected Measure" as
> defined in Item 402(v) of Regulation S-K under the Exchange Act. For 2025, 2024, 2023 and 2022,
> revenue (non-GAAP) is the same as the company's reported consolidated GAAP revenue (i.e., no
> adjustments to GAAP revenue were made in 2025, 2024, 2023 and 2022). For 2021, revenue (non-GAAP) is
> the company's reported consolidated GAAP revenue ($79.0 billion) less revenue during 2021 from the
> NAND memory business we agreed to sell to SK hynix ($4.3 billion)."

**Company-Selected Measure: Revenue (Non-GAAP).** Note that for the CSM specifically, non-GAAP
revenue equals GAAP revenue in four of five years. This is *not* the same basis used to pay the
bonus, see 5.4.

The required tabular list, DEF 14A page 78, "2025 Performance Measures":

> "Three Most Important Performance Measures
>  Revenue (Non-GAAP)
>  Gross Margin Percentage (Non-GAAP)
>  Relative TSR"

## 5.2 The Pay Versus Performance table

DEF 14A, pages 77-79. Intel had **five different PEOs across the five-year window**, so the table
carries multiple PEO columns. Footnotes, verbatim (page 77):

> "† Mr. Tan was appointed Intel's CEO effective March 18, 2025.
>  †† Mr. Gelsinger ceased being Intel's CEO effective as of December 1, 2024. Ms. Johnston Holthaus and
> Mr. Zinsner served as Intel's Interim Co-CEOs effective as of December 1, 2024 until March 18, 2025.
>  ††† Mr. Swan ceased being Intel's CEO effective as of February 15, 2021, and Mr. Gelsinger was
> appointed Intel's CEO effective as of February 15, 2021."

### The full table, restated row by row

| Year | PEO | PEO SCT total ($) | PEO "Compensation Actually Paid" ($) | Avg Non-PEO NEO SCT ($) | Avg Non-PEO NEO CAP ($) | Intel TSR (on $100) | Peer group TSR (on $100) | Net income ($B) | Revenue Non-GAAP ($B) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | **Lip-Bu Tan** | 92,990,900 | **161,645,068** | 12,888,867 | 14,951,946 | **85.08** | **264.83** | **(0.3)** | 52.9 |
| 2025 | Johnston Holthaus | 33,073,500 | 55,929,253 | " | " | " | " | " | " |
| 2025 | Zinsner | 18,174,100 | 31,258,742 | " | " | " | " | " | " |
| 2024 | **Gelsinger** | 27,429,900 | **(82,216,617)** | 10,214,333 | (2,842,898) | 47.71 | 214.75 | (18.8) | 53.1 |
| 2024 | Johnston Holthaus | 12,626,000 | (13,792,850) | " | " | " | " | " | " |
| 2024 | Zinsner | 12,343,100 | (14,258,138) | " | " | " | " | " | " |
| 2023 | Gelsinger | 16,855,400 | 82,484,119 | 8,815,275 | 23,524,978 | 116.52 | 153.86 | 1.7 | 54.2 |
| 2022 | Gelsinger | 11,614,700 | (78,501,522) | 12,812,380 | 5,207,059 | 59.86 | 97.48 | 8.0 | 63.1 |
| 2021 | Swan | 605,300 | (26,428,474) | 10,538,800 | 2,003,497 | 111.80 | 135.12 | 19.9 | 74.7 |
| 2021 | **Gelsinger** | **178,590,400** | 124,177,488 | " | " | " | " | " | " |

**The TSR columns are the finding.** A $100 investment in Intel on 24 December 2020 was worth
**$85.08** at the end of fiscal 2025, a 15% loss over five years. The same $100 in the S&P 500 IT
Index was worth **$264.83**. Intel underperformed its own chosen benchmark by **180 percentage
points over five years**, and net income over the five years runs $19.9B → $8.0B → $1.7B →
$(18.8)B → $(0.3)B.

TSR basis, DEF 14A page 78:

> "TSR. Pursuant to the SEC rules, company TSR and Peer Group TSR is determined based on the value of an
> initial fixed investment of $100 on December 24, 2020, the last trading day prior to the commencement
> of fiscal year 2021, through the end of the listed year. The Peer Group TSR set forth in this table
> utilizes the S&P 500 IT Index…"

Intel's own caution on what CAP means, page 77:

> "Amounts included as "compensation actually paid" do not represent the value of cash compensation and
> equity awards actually received by the NEOs, but rather is an amount calculated under SEC rules that
> includes, among other things, the year-over-year changes in the "fair value" of unvested equity-based
> awards."

## 5.3 Lip-Bu Tan's compensation

### Summary Compensation Table, page 62

> "Lip-Bu Tan 	2025 	746,200 		— 		49,639,500 		39,523,200 		2,374,000 		708,000 		92,990,900
>  CEO"

| Component | 2025 ($) |
|---|---:|
| Salary (part-year from 18 Mar; $1,000,000 annualised) | 746,200 |
| Bonus | 0 |
| **Stock awards** | **49,639,500** |
| **Option awards** | **39,523,200** |
| Non-equity incentive plan compensation | 2,374,000 |
| All other compensation | 708,000 |
| **Total** | **92,990,900** |

**Equity is 96.0% of the package.** Component arithmetic ties: $24,717,700 + $24,921,800 =
$49,639,500 stock; $10,924,200 + $28,599,000 = $39,523,200 options; sum $89,162,700, which is exactly
the amount subtracted in the CAP reconciliation.

### The mega-grants: yes, and they are large

DEF 14A "Grants of Plan-Based Awards in Fiscal Year 2025", page 66:

| Award | Grant date | Target (#) | Maximum (#) | Exercise price | Grant-date fair value ($) |
|---|---|---:|---:|---:|---:|
| Annual PSU | 3/18/2025 | 631,796 | 1,263,592 | — | 24,717,700 |
| **New Hire PSU** | 3/18/2025 | 745,870 | **2,237,610** | — | 24,921,800 |
| Annual Option | 3/18/2025 | — | 1,029,579 | $25.90 | 10,924,200 |
| **New Hire Option** | 3/18/2025 | 1,792,938 | **2,689,407** | $25.90 | 28,599,000 |
| Annual Cash | — | $2,000,000 | $4,000,000 | — | — |

**The negotiated value and the reported value differ by $23.2 million.** DEF 14A page 62:

> "Award Type 	Negotiated Equity Award Value 	Summary Compensation Table Value
>  Annual PSUs 	$14,400,000 	$24,717,700
>  Annual Options 	$9,600,000 	$10,924,200
>  New Hire Options 	$25,000,000 	$28,599,000
>  New Hire PSUs 	$17,000,000 	$24,921,800
>  Total 	$66,000,000 	$89,162,700"

> "▪ for purposes of determining the number of units or options to award Mr. Tan, an average of Intel's
> trading prices over a 30-day period preceding the public announcement date of March 12, 2025 ($22.79);
> and
>  ▪ for purposes of the grant date fair value for the Compensation Tables, the value on the grant date of
> March 18, 2025 ($25.92), computed in accordance with … (FASB ASC Topic 718)."

**This is disclosed, reconciled and explained, a point in the company's favour.** The board
negotiated $66 million; the accounting produced $89 million because the stock rose 13.7% between the
pricing date and the grant date.

### The performance conditions are unusually demanding

DEF 14A page 43, verbatim:

**Annual PSUs ($14.4M):**
> "▪ Three-year performance period with vesting based on our TSR performance relative to the TSR of the
> S&P 500 Index
>  ▪ Vesting at target (100%) if TSR at the 55th percentile of the Index and payout capped at target if our
> absolute TSR is negative
>  ▪ Payout at 0% if Intel's TSR is 25th percentile or below the Index; payout at 200% of target (maximum
> payout) if Intel's TSR is 80th percentile or above the Index"

**New Hire PSUs ($17M):**
> "▪ Earned based on stock price growth over a three-year period:
>  ▪ Threshold : 0% payout if the stock price does not increase
>  ▪ Target : 100% payout for 200% increase in the stock price
>  ▪ Maximum : 300% payout for 300% increase in the stock price
>  … ▪ Requires that on each vesting date Mr. Tan continues to hold the shares with a target value of $25
> million that he purchased pursuant to the Tan Offer Letter
>  ▪ Requires absolute stock price growth for any award to be earned, and both absolute stock price growth
> and relative outperformance for payouts above target to be realized"

**A 200% share-price increase is required for target payout on the largest single grant.** And Tan
was required to buy stock with his own money, page 41:

> "Further, as agreed to pursuant to the terms of his offer letter (Tan Offer Letter), Mr. Tan purchased
> Intel shares with a target value of $25 million from Intel on March 21, 2025. He must hold those
> shares through each New Hire PSU vesting date for the New Hire PSUs to vest."

> "Almost 99% of his 2025 total compensation opportunity was "at-risk" and contingent on company
> performance, and more than 95% was delivered in the form of equity awards."

**No cash severance.** DEF 14A page 73:

> "Mr. Tan is not eligible to participate in the Executive Severance Plan or entitled to any cash
> severance benefits on a termination of employment."

### Why CAP is $161.6M when the grant was $93.0M

DEF 14A page 78, CAP reconciliation for Tan:

> "Summary Compensation Table (SCT) Total 	92,990,900
>  Minus, the amounts reported as "Stock Awards" and "Option Awards" in the SCT 	89,162,700
>  Plus, the fair value as of 2025 fiscal year end of equity awards granted in 2025 and unvested as of
> year end 	157,816,868
>  … Equals Compensation Actually Paid (CAP) 	161,645,068"

**The entire $161.6M figure is a nine-month mark-to-market.** Intel closed at $36.20 on 26 December
2025 against a $25.92 grant-date price and a $25.90 strike, a 40% rise. **Nothing has vested.**
DEF 14A pages 68-69: "Other than Mr. Tan, our NEOs did not hold any outstanding option awards as of
December 27, 2025", and Tan's 2025 vesting row reads "RSU, ,  ". The $161.6M is paper.

### CEO pay ratio, page 76

> "The 2025 annual total compensation of our CEO Mr. Tan is $93,244,700, the 2025 annual total
> compensation of our median compensated employee is $114,900, and the ratio of these amounts is **812 to
> 1**."

> "Our median employee works in Poland as a full-time software development engineer. … As of December 27,
> 2025, we had 85,100 worldwide employees…"

Intel volunteers a second, lower ratio:

> "Supplemental Pay Ratio … The supplemental pay ratio excludes the non-recurring special equity awards
> and includes the representative ongoing intended long-term incentive equity award target value he
> received in 2026. For purposes of this ratio, our CEO's 2025 annual total compensation would be
> $39,723,900, which when compared to the annual total compensation of our median compensated employee
> of $114,900, results in a pay ratio of **346 to 1**."

**Record this as a mild promotional tell.** The supplemental ratio is defensible in substance (a
new-hire grant genuinely is non-recurring) but it is a voluntary, self-selected alternative that
happens to cut the headline number by 57%.

## 5.4 Incentive plan metrics, and whether targets were met

### Annual cash bonus: the metrics, page 49

| Metric | Weight (NEOs) | Weight (Tan) |
|---|---|---|
| Revenue | 20% | 25% |
| Gross Margin Percentage | 20% | 25% |
| Operating Expense | 20% | 25% |
| Intel Top Jobs Goals | 20% | 25% |
| Individual Performance Goals | 20% | — |

> "The committee replaced the group operating income metric with a company-wide operating expense metric
> to align the Annual Cash Bonus Plan with our commitment to investors to reduce operating expenses in
> 2025."

### The results, page 50

| Metric | Threshold | Target | Maximum | **Achievement** | Score |
|---|---|---|---|---|---|
| Revenue (Adjusted) | $48.0B | $52.0B | $58.0B | **$53.36B** | 113.6% |
| Gross Margin % (Adjusted) | 34% | 37% | 40% | **36.96%** | 99.6% |
| Operating Expense (Adjusted) | $19.5B | $18.5B | $17.5B | **$16.48B** | **200%** (capped) |

Intel Top Jobs, pages 50-51, **every group scored below 100**:

> "Products Top Jobs: … 	69.0 /80.0
>  Foundry Top Jobs: World-class, financially self-sustaining … 	53.0 /80.0
>  Corporate Top Jobs: Unlock the full potential of Intel people, portfolio and assets … 	19.5 /20.0
>  Final Score 		Intel Product 	88.5 		Intel Foundry 	72.5 		Intel Corporate 	80.5"

### Final payouts, page 52

> "Lip-Bu Tan 	113.6 % 	99.6 % 	200 % 	80.5 % 	N/A 	118.7 % 	2,374,000
>  David A. Zinsner 	113.6 % 	99.6 % 	200 % 	80.5 % 	110 % 	120.7 % 	1,795,700
>  Naga Chandrasekaran 	113.6 % 	99.6 % 	200 % 	72.5 % 	110 % 	119.1 % 	1,636,700
>  April Miller Boise 	113.6 % 	99.6 % 	200 % 	80.5 % 	100 % 	118.7 % 	1,558,200
>  Michelle Johnston Holthaus 	113.6 % 	99.6 % 	200 % 	88.5 % 	100 % 	120.3 % 	2,406,400
>  Christoph Schell 	— % … 	— % 	—"

**Plain answer: mixed, and paid at ~119-121% of target in a year of a GAAP net loss attributable to
Intel of $(267) million.** Revenue and opex beat; gross margin missed narrowly; every operational
(Top Jobs) score missed, Foundry worst at 53.0/80.0.

### THE ADJUSTMENTS: the material finding in this section

**Every financial achievement was scored on an adjusted figure more favourable than the reported
one.** DEF 14A page 50, verbatim:

> "Adjustments. Achievement for the three performance metrics reflects permitted adjustments under the
> 2025 Annual Bonus Plan to reflect the impacts to our financials from M&A activity and divestitures,
> specifically the sale of a majority interest in and deconsolidation of Altera Corporation in the third
> quarter of 2025. **Adjustments were made starting from the company's reported consolidated GAAP revenue
> ($52.9 billion), non-GAAP gross margin percentage (36.7%) and non-GAAP operating expense ($16.5
> billion) and adjusting such numbers to a result that was designed to reflect what would have been
> achieved had Altera continued to be fully owned by Intel through the end of fiscal 2025 and achieved
> the results forecasted for the remainder of 2025 at the time of the divestiture.**" *(emphasis added)*

| Metric | Reported | Scored for bonus | Direction |
|---|---|---|---|
| Revenue | $52.9B (GAAP) | **$53.36B** | +$0.46B favourable |
| Gross margin % | 36.7% (non-GAAP) | **36.96%** | +0.26pp favourable |
| PSU revenue growth % | **-0.5%** | **+0.5%** | +1.0pp favourable |

**The adjustment credits Intel with revenue from a business it sold, at a level it "forecasted" at the
time of sale.** Note the double layer: the starting point for gross margin and opex is already a
*non-GAAP* figure from the earnings release, and the Altera pro-forma is then applied on top. This is
the "conservatism spent twice" pattern in compensation form.

### Discretion: exercised once, downward

DEF 14A page 52:

> "Tan Final Payout. After reviewing 2025 performance under the Annual Cash Bonus Plan, the Compensation
> Committee, in consultation with Mr. Tan, adjusted his bonus payout. Because his calculation excludes
> the individual performance metric applied to other employees, his formulaic payout was 123.4%, which
> was higher than that of the broader employee population due to the higher weighting of financial
> metrics alone. To maintain alignment and consistency, the committee— with Mr. Tan's agreement—reduced
> his payout to 118.7%, matching the general payout level for corporate employees."

**Record this in management's favour.** The CEO's own bonus was cut from 123.4% to 118.7%.

### Target-setting language worth flagging

DEF 14A, Compensation Committee Letter, page 38:

> "Targets were set at levels determined to be challenging yet achievable – **in certain cases disclosed
> in the following CD&A, these targets were below the actual results achieved in 2024.**"

Page 49:

> "The expectation that there could be a meaningful reduction in revenue from 2024 to 2025 factored
> significantly into the committee's decision to set a 2025 target goal for revenue lower than the target
> goal for 2024 and lower than the actual result for revenue in 2024."

Page 53, for the PSUs:

> "The expectation that there could be a meaningful reduction in revenue from 2024 to 2025 factored
> significantly into the committee's decision to set a 2025 target goal for revenue growth at -2.0%
> (i.e., target payout could be achieved with a decrease in revenue of not more than 2.0% versus 2024…).
> The committee set the 2025 target goal for CFFO lower than the target goal for 2024 and lower than the
> actual result for CFFO in 2024."

**Targets were set below the prior year's actual results, and the committee says so openly.** The
candour is genuine; the practice still means "target" meant "shrink by less than 2%".

Page 49, the committee grading its own work:

> "In reviewing these results, the Compensation Committee reaffirmed its belief that the 2025 goals were
> appropriate and rigorous given the operating environment Intel faced. The committee further determined
> that the resulting payout percentages accurately reflected our performance in 2025…"

### Long-term PSU outcomes: these did fail

DEF 14A page 67:

> "2022 PSU Payout. As reported in last year's proxy statement, in 2025 the payout for the PSUs granted
> in 2022, with a January 2022 through December 2024 performance period, which would have vested in
> January 2025, **paid out at 0% of target.** The performance metrics for the PSUs were annual revenue
> growth percentage and CFFO metrics and three-year relative TSR and revenue CAGR modifiers. The PSUs
> paid out at 0% as a result of average performance for the annual goals of approximately 50% and below
> threshold performance for both of the three-year modifiers, which impacted the payout by -50%."

DEF 14A page 54:

> "The 2023 PSUs vested on January 31, 2026 and were **earned at 76% of the target number of shares
> granted** … The 2023 PSUs paid out at 76% of target based on an average performance for the annual
> performance goals of 100%, below-threshold performance for the revenue CAGR modifier, and above-target
> performance for the relative TSR modifier, which together impacted the payout of the 2023 PSUs by -24%."

**The long-term plan worked as intended: 0% in 2022, 76% in 2023.** The three-year instruments
punished the three-year record even while the annual bonus paid ~119%. This is the strongest
pro-management fact in the compensation section.

Note also the return to multi-year goal setting, page 53:

> "With the 2025 PSUs, the Compensation Committee returned to setting three-year cumulative goals as
> compared to setting annual objectives for the PSUs granted in 2022, 2023 and 2024 … and the committee
> delivered on our previously disclosed commitment to our stockholders to return to multi-year goal
> setting by fiscal year 2025."

**Intel had been setting one-year goals inside three-year PSUs for 2022, 2023 and 2024**, a
well-known softening device, and has now reversed it. Both facts belong in the file.

### 2026 changes, page 56

> "▪ Added an operating margin percentage metric to replace the gross margin percentage metric, and
> removed the operating expense metric;
>  ▪ Added Intel Top Priorities … to replace Intel Top Jobs; and
>  ▪ Increased the weight of both financial metrics (revenue and operating margin percentage) to 30% …"

**The metric that paid 200% (operating expense) was removed for 2026**, and the softer gross margin
metric replaced by operating margin. Note also that this is the *third* consecutive year of metric
changes: group operating income → operating expense (2025) → operating margin (2026).

## 5.5 Say-on-pay

DEF 14A page 45:

> "At our 2025 Annual Meeting, our say-on-pay vote received **72% support.** Following the disclosure of
> Mr. Tan's compensation package, we engaged with stockholders ahead of our 2025 Annual Meeting as well
> as in the off-season ahead of the 2026 Annual Meeting."

> "While our stockholder base is broad and has varying perspectives on many issues, the selection of Mr.
> Tan as our new CEO and the structure of Mr. Tan's new-hire equity awards received consistently
> favorable feedback from stockholders. Additionally, our stockholders were generally supportive of our
> current executive compensation programs, and there were no common requests for changes to our
> programs. Nevertheless, taking into account the results of the say-on-pay vote, the Compensation
> Committee made certain refinements to our programs for 2026…"

**72% is a weak say-on-pay result** (the S&P 500 norm is above 90%; below 70% is generally treated as
a failure signal). The proxy reports the percentage and then characterises feedback as "consistently
favorable" and "generally supportive … no common requests for changes". **The characterisation and
the number sit awkwardly together.** No vote counts (for / against / abstain / broker non-votes) are
given, searches run: `Say-on-Pay`, `say-on-pay`, `say on pay`, `Advisory Vote`, `advisory vote`,
`72%`.

## 5.6 Pat Gelsinger's separation: NO INSTANCE FOUND

**There is no disclosure of Patrick P. Gelsinger's separation terms or any payment to him anywhere in
this proxy statement.**

**Searches run** (Python `re.finditer` over `DEF14A_2026.txt`): `Gelsinger` (10 hits), `Patrick`
(6), `Pat Gelsinger` (0), `separation` (5), `Separation` (1), `severance` (25), `Severance` (34),
`retirement` (37), `Retirement` (7), `departure` (8), `Departure` (4), `transition` (18),
`Transition` (3), `former CEO` (5), `Former CEO` (11), `prior CEO` (3), `Executive Severance Plan`
(25), `inducement` (0).

**All 10 `Gelsinger` hits are inside the Pay Versus Performance section (pages 77-79)**, table
column headers, the 2021-2024 data rows, the PEO/Non-PEO listing, the two footnotes quoted in 5.2,
and two chart series labels. **Every `severance` and `separation` hit was checked and none concerns
Gelsinger**; they concern Tan's offer letter, the Executive Severance Plan generally,
Chandrasekaran's offer letter, Johnston Holthaus's letter agreement, and Schell's non-entitlement.

The only two indirect references to his exit, both third-person, both without amounts:

> "Mr. Yeary served as Interim Executive Chair from December 2024, upon the departure of our prior CEO,
> through March 2025, when Lip-Bu Tan joined Intel as our new CEO." (page 28)

> "This flexibility has been particularly important for us during times of leadership transition. For
> example, in December 2024, following our prior CEO's departure, the Board appointed interim co-CEOs to
> run the business until a permanent CEO successor was appointed." (Proposal 8 opposition statement)

**This is not necessarily concealment.** Gelsinger departed 1 December 2024, inside fiscal 2024; his
separation terms would properly be disclosed in the **2025** proxy covering fiscal 2024, which is not
in this evidence set. **UNRESEARCHED. The document that would resolve it is Intel's DEF 14A filed in
2025, and the 8-K filed on or about 2 December 2024. Named and gettable.**

What the 2026 proxy *does* show is the mark-down: Gelsinger's 2024 CAP of **$(82,216,617)** against
an SCT total of $27,429,900, the forfeiture and revaluation of unvested equity, not cash paid.
Across 2021-2024 his cumulative CAP is roughly **negative $54 million** against cumulative SCT totals
of $234.5 million. Note his 2021 SCT total of **$178,590,400**, the largest single-year figure in the
table.

### Separation disclosure that IS present, for contrast

**Michelle Johnston Holthaus** (page 41 and page 58):

> "▪ Departure of CEO, Intel Products - On March 1, 2026, Ms. Johnston Holthaus departed Intel. Her
> departure followed a resignation for good reason (as defined in the letter agreement, executed on
> February 28, 2025). In connection with her resignation for good reason, Ms. Johnston Holthaus was
> eligible for severance benefits under the Intel Corporation Executive Severance Plan in exchange for a
> release of claims in favor of Intel."

> "On September 7, 2025, Ms. Johnston Holthaus notified us of her decision to resign for good reason, but
> agreed to remain employed by us in a non-executive role through March 1, 2026 to facilitate a smooth
> transition."

Her table (page 73) shows a $4,500,000 cash severance payment and $13.8M of equity acceleration on an
involuntary termination scenario.

**Christoph Schell:**

> "Schell Departure. Mr. Schell was not entitled to any severance payments or equity acceleration upon
> his resignation from Intel on June 30, 2025, as reflected in the table above."
> "Mr. Schell resigned from Intel effective June 30, 2025 and forfeited all of his outstanding equity
> awards."

**Naga Chandrasekaran's guaranteed severance** (page 58) is worth recording as an unusual term:

> "…he will be entitled to two severance payments depending on his separation date: (i) the value of the
> first payment declines from $7,000,000 by 1/3 each year over the three-year period following October
> 30, 2024 and (ii) the value of the second payment declines from $6,000,000 by 1/8 each quarter over the
> two-year period following October 30, 2024."

**A $13 million declining-balance severance guarantee** for the head of Intel Foundry, the segment
that scored 53.0 out of 80.0 on its own operational scorecard.

## 5.7 Non-GAAP inside compensation: all 14 occurrences accounted for

`non-GAAP` (case-insensitive) returns exactly **14 hits** in the DEF 14A. Classified:

| # | Location | Use |
|---|---|---|
| 1 | Audit Committee Report | Oversight of non-GAAP use in earnings releases, not a comp metric |
| 2-3 | p.48 "Use of Non-GAAP Measures and Adjustments" | Bonus targets set on non-GAAP revenue, gross margin %, opex |
| 4-5 | p.50 "Adjustments" | The Altera pro-forma, quoted in 5.4 |
| 6-8 | p.78 Company Selected Measure | The 402(v) CSM |
| 9-10 | p.78 tabular list | "Revenue (Non-GAAP)", "Gross Margin Percentage (Non-GAAP)" |
| 11-12 | p.79 chart title and legend | — |
| 13-14 | Proposal 4 / Appendix A, EIP §10(b) | Plan permits metrics "on a U.S. GAAP or non-GAAP basis" |

The key one, page 48:

> "Use of Non-GAAP Measures and Adjustments. The revenue, gross margin percentage and operating expense
> targets are generally established by the Compensation Committee using the company's non-GAAP measures
> of revenue, gross margin percentage and operating expense as reported in its annual and quarterly
> earnings releases. The company's achievement against those targets is then subject to further
> adjustments as permitted under our Annual Cash Bonus Plan."

**Note the tension with section 2.1.** The 10-K presents exactly one non-GAAP measure (Adjusted Free
Cash Flow) and no EBITDA. But the *compensation* apparatus runs on non-GAAP revenue, non-GAAP gross
margin and non-GAAP operating expense taken from the earnings releases, measures that appear nowhere
in the 10-K. **The 10-K's non-GAAP restraint does not extend to how the executives are actually paid.**

## 5.8 Summary judgement for the file (evidence, not verdict)

**Against:** every 2025 bonus metric was scored on an adjusted number more favourable than the
reported one, crediting Intel with revenue from a divested business; targets were deliberately set
below the prior year's actuals; the bonus paid ~119-121% of target in a year of a GAAP net loss and a
five-year TSR of -15% against a benchmark of +165%; the say-on-pay result of 72% is characterised as
"generally supportive"; incentive metrics have now changed in three consecutive years; a $13M
declining severance guarantee sits with the head of the worst-scoring segment.

**In favour:** the CEO's own bonus was cut by discretion; 96% of CEO pay is equity with genuinely
demanding conditions (a 200% share-price rise for target payout on the largest grant); the CEO bought
$25M of stock with his own money and must hold it; the CEO has no cash severance; the negotiated-value
vs SCT-value gap is disclosed and reconciled; the three-year PSUs actually paid 0% and 76%; and the
company voluntarily abandoned the one-year-goals-inside-three-year-PSUs device.

---

# 6. CONTINGENT LIABILITIES

## 6.1 The aggregate accrual, three dates

| | FY2024 (Dec 28, 2024) | FY2025 (Dec 27, 2025) | Q2 2026 (Jun 27, 2026) |
|---|---:|---:|---:|
| VLSI litigation | $1.0B | $1.0B | $1.0B |
| EC-imposed fine | $401M | **$311M** | **$308M** |
| R2 litigation (unpaid) | $655M | resolved | — |
| **Total accrued legal liabilities** | **~$2.06B** | **~$1.31B** | **~$1.31B** |

FY2025 10-K, Note 19: Commitments and Contingencies, "Legal Proceedings":

> "We are regularly party to various ongoing claims, litigation, and other proceedings, including those
> noted in this section. As of December 27, 2025, we have accrued liabilities of $ 1.0 billion related to
> litigation involving VLSI and $ 311 million, including revaluation effects and accrued interest, related
> to an EC-imposed fine, both as described below. **Excluding the VLSI claims described below**, management
> at present believes that the ultimate outcome of these proceedings, individually and in the aggregate,
> will not materially harm our financial position, results of operations, cash flows, or overall trends;
> however, legal proceedings and related government investigations are subject to inherent uncertainties,
> and unfavorable rulings, excessive verdicts, or other events could occur. Unfavorable resolutions could
> include substantial monetary damages, fines, or penalties. **Certain of these outstanding matters include
> speculative, substantial, or indeterminate monetary awards.**"

FY2024 10-K, Note 19:

> "As of December 28, 2024, we have accrued a charge of $ 1.0 billion related to litigation involving VLSI
> and a charge of $ 401 million related to an EC-imposed fine, both as described below."

> "In addition, in the second quarter of 2024, we accrued a charge of $ 780 million within restructuring
> and other related to three separate confidential settlement agreements with R2, Third Point, and TRGP
> (see R2 Semiconductor Patent Litigation below). The remaining unpaid liability was $ 655 million as of
> December 28, 2024."

Q2 2026 10-Q, Note 14: Contingencies:

> "As of June 27, 2026, we have accrued liabilities of $ 1.0 billion related to litigation involving VLSI
> and $ 308 million, including revaluation effects and accrued interest, related to an EC-imposed fine,
> both as described below."

## 6.2 Matter-by-matter register

### (a) European Commission competition matter: the fine

> "In 2009, the EC found that we had used unfair business practices to persuade customers to buy
> microprocessors in violation of Article 82 of the EC Treaty (later renumbered Article 102) … The EC
> ordered us to end the alleged infringement referred to in its decision and imposed a € 1.1 billion fine,
> which we paid in the third quarter of 2009."

> "In January 2022, the General Court annulled the EC's 2009 findings against us regarding rebates, as
> well as the € 1.1 billion fine imposed on Intel, which was returned to us in February 2022. … In October
> 2024, the Court of Justice dismissed the EC's appeal, upholding the judgment of the General Court."

**The live number:**

> "In September 2023, the EC imposed a € 376 million ($ 401 million) fine against us based on its 2009
> finding that we made payments to prevent sales of specific rival products. We appealed the EC's
> decision, and in December 2025 the General Court reduced the fine to € 237 million ($ 277 million).
> Intel may appeal the General Court's decision to the Court of Justice. We have reduced our previously
> accrued charge for the fine to approximately $ 311 million as of December 27, 2025, which includes
> foreign currency revaluation effects and accrued interest, and are unable to make a reasonable estimate
> of the potential loss or range of losses in excess of this amount given the procedural posture and the
> nature of these proceedings."
> — FY2025 10-K, Note 19

**Status at Q2 2026, Intel appealed:**

> "In February 2026, we appealed the General Court's decision to the Court of Justice. We have accrued a
> charge of $ 308 million as of June 27, 2026…"

**The cash side, which is easy to miss**, in FY2025 10-K, Note 7:

> "Litigation charges and other includes a $ 163 million benefit recorded in 2025 from the reduction of the
> previously accrued EC-imposed fine recorded in 2023. **While the fine remains unpaid on appeal, our
> obligation is guaranteed by a third party. We funded the guarantee in 2025 by depositing $ 340 million in
> legally restricted accounts, for which the restricted cash is presented within other long-term assets .**"

So the $163M P&L *benefit* in 2025 was accompanied by $340M of cash locked up as collateral. Total
restricted cash: "We have $ 447 million of restricted cash included in other long-term assets … as of
December 27, 2025".

**A $560M benefit that has now disappeared from view.** FY2024 10-K disclosed a counterclaim for
default interest on the original fine:

> "In April 2022, we filed applications with the General Court seeking an order requiring the EC to pay us
> approximately €593 million ($647 million) in default interest on the original €1.1 billion ($1.2 billion)
> fine that was held by the EC for 12 years. In November 2024, the EC paid us approximately €516 million
> ($560 million) in settlement of the applications."

Searched `default interest` in FY2025_10K.txt: **no instance found**; the matter is closed. It survives only
as a Note 6 line: "in 2024 included … $ 560 million of interest received and recognized as a benefit in
relation to the EC competition matter."

### (b) VLSI Technology LLC v. Intel: the largest single exposure

Accrued **$1.0 billion**, unchanged at all three dates. Four active fronts:

**First Texas case, the $2.2B judgment, partly vacated:**
> "The first Texas case went to trial in February 2021, and the jury awarded VLSI $ 1.5 billion for literal
> infringement of one patent and $ 675 million for infringement of another patent under the doctrine of
> equivalents. In April 2022, the court entered final judgment, awarding VLSI $ 2.2 billion in damages and
> approximately $ 162 million in pre-judgment and post-judgment interest. … In December 2023, the Federal
> Circuit reversed the finding of infringement as to the patent for which VLSI was awarded $ 675 million.
> The Federal Circuit affirmed the finding of infringement as to the patent for which VLSI had been
> awarded $ 1.5 billion, but vacated the damages award and sent the case back to the trial court for
> further damages proceedings on that patent."

**Second Texas case, $3.0B sought, Intel won:**
> "The second Texas case went to trial in April 2021, and the jury found that we do not infringe the
> asserted patents. VLSI had sought approximately $ 3.0 billion for alleged infringement, plus enhanced
> damages for willful infringement. In September 2024, the court denied VLSI's motion for a new trial.
> Other post-trial motions remain pending, and the court has not yet entered final judgment."

**Third Texas case, $949M verdict against Intel, licence defence pending:**
> "The jury found the patent valid and infringed, and awarded VLSI approximately $ 949 million in damages,
> plus interest and a running royalty. The court has not yet entered final judgment. … In May 2025, the
> court held a trial on an underlying factual question relating to Intel's license defense. The jury
> returned a verdict in Intel's favor."

**California case, reversed against Intel in April 2026.** FY2025 said the appeal was "set for oral
argument … in February 2026". Q2 2026 10-Q, Note 14:

> "Intel prevailed on all eight patents and the court entered final judgment in April 2024. VLSI appealed
> the Court's judgment of non-infringement as to one of the eight patents. **In April 2026, the Federal
> Circuit reversed and remanded the case back to the district court.**"

**The accrual language, and how it changed:**

FY2024: "While we dispute VLSI's claims and intend to vigorously defend against them, we are unable to
make a reasonable estimate of losses in excess of recorded amounts **given recent developments and
future proceedings**."

FY2025 and Q2 2026: "We are unable to make a reasonable estimate of losses in excess of recorded
amounts."

**Intel dropped both "we dispute VLSI's claims and intend to vigorously defend against them" and the
"given recent developments" qualifier.** Recorded as observed; the significance is not established.

**Aggregate VLSI exposure claimed across cases: roughly $2.2B + $3.0B + $0.949B, against a $1.0
billion accrual.** Intel's own aggregate-materiality sentence expressly carves VLSI out ("Excluding
the VLSI claims described below").

### (c) Security-vulnerability class actions (Spectre / Meltdown / Downfall)

> "Consumer class action lawsuits are pending against us in the U.S. and Canada. The plaintiffs, who
> purport to represent various classes of purchasers of our products, generally claim to have been harmed
> by our actions and/or omissions in connection with Spectre, Meltdown, and other variants of this class
> of security vulnerabilities that have been identified since 2018…"

> "In August 2025, the district court dismissed with prejudice the nationwide class claims under
> California law in plaintiffs' amended complaint, and denied Intel's motion to dismiss subclass claims
> pleaded in the alternative under the laws of certain other states. In October 2025, the plaintiffs filed
> a second amended complaint, which Intel moved to dismiss in December 2025."

> "…we are unable to make a reasonable estimate of the potential loss or range of losses, if any, that
> might arise from these matters."

**Amount at stake: no dollar figure disclosed. No accrual.** Status: narrowed but not closed 
nationwide class dismissed with prejudice, state subclasses survived.

### (d) Securities class action: segment reporting / internal foundry model

**This matter is directly about section 4 of this file.**

> "A securities class action lawsuit was filed in the U.S. District Court for the Northern District of
> California in May 2024 against us and certain officers **following the modification of our segment
> reporting in the first quarter of 2024 to align to our new internal foundry operating model.** … plaintiffs
> filed an amended consolidated complaint generally alleging that defendants violated the federal
> securities laws by making false or misleading statements about the growth and prospects of the foundry
> business and seeking monetary damages on behalf of all persons and entities that purchased or otherwise
> acquired our common stock … from January 25, 2024 through August 1, 2024."

**Intel won:**

> "In March 2025, the court dismissed plaintiffs' amended consolidated complaint, finding that plaintiffs
> failed to plead any false or misleading statements by defendants. The court granted plaintiffs leave to
> amend, but in July 2025 dismissed plaintiffs' second amended complaint and entered judgment in
> defendants' favor, again finding that plaintiffs failed to plead any false or misleading statements.
> Plaintiffs have appealed."

**Record this squarely.** Investors sued over exactly the segment-reporting change catalogued in
section 4.2 above, and **a federal court twice found no false or misleading statement.** That is
material evidence *for* management on the honesty question, and it must be weighed against the
E2-49 pattern, not ignored.

**Related derivative suits:**
> "Stockholder derivative lawsuits have been filed in Delaware state and federal courts alleging that our
> directors and certain officers breached their fiduciary duties and violated the federal securities laws
> by making or allowing the statements that are challenged in the securities class action lawsuit. … The
> cases are stayed pending developments in the securities class action lawsuit."

### (e) EireOg Innovations v IBM et al.: NEW in FY2025, quantified in 2026

> "Since April 2024, EireOg Innovations Ltd. has filed eleven separate complaints in the Eastern and
> Western Districts of Texas against Intel and AMD customers alleging that various products with Intel and
> AMD CPUs infringe numerous patents. EireOg seeks compensatory damages, future royalties, attorneys'
> fees, costs, and interest. Intel is indemnifying Acer, Amazon Web Services (AWS), Cisco, Dell, HPE, HPI,
> IBM, Lenovo, and Oracle…"
> — FY2025 10-K, Note 19. **No amount disclosed:** "alleged damages have not been specified"

Q2 2026 10-Q, Note 14, **first quantification, and a favourable verdict:**

> "**Across the cases, EireOg alleges past and future damages in excess of $ 2.0 billion.** The EireOg case
> against Cisco went to trial in April 2026. The jury returned a verdict finding no infringement by Cisco
> and finding the factual predicate for concluding that Intel is licensed to the asserted patent. The
> courts then stayed the remaining cases pending resolution of post-trial proceedings and any appeal in
> the Cisco case."

**A $2.0 billion indemnity exposure that was unquantified in the 10-K and quantified only in the next
10-Q.** Indemnified customers fell from 9 to 7 (Acer and HPI dismissed); patents at issue from four to
three. **No accrual.**

### (f) Media Content Protection v Intel: NEW in FY2025

> "MCP seeks $ 66 million to $ 398 million in damages for royalties between the 2020 case filing and the
> 2023 patent expiration date."

> "In November 2025, the court granted Intel's motion for summary judgment of invalidity of both patents
> and issued a final judgment in favor of Intel in December 2025. MCP has appealed."

**$66M-$398M claimed; Intel won at summary judgment; on appeal. No accrual.**

### (g) Litigation over the U.S. Department of Commerce equity stake: NEW in Q2 2026

**This is the newest matter and it goes to the government's ownership of Intel** (see section 9 and
the "Escrowed Shares" mark-to-market of $(13,619)M in H1 2026). Q2 2026 10-Q, Note 14:

> "**Litigation Related to Warrant and Common Stock Agreement between Intel and the U.S. Department of
> Commerce** — A stockholder filed a derivative lawsuit in the Delaware Court of Chancery in March 2026
> against our directors, the Department of Commerce and Secretary of the U.S. Department of Commerce,
> Howard W. Lutnick, claiming our directors breached their fiduciary duties and engaged in waste by
> approving the Warrant and Common Stock Agreement, dated as of August 22, 2025, between us and the U.S.
> Department of Commerce, and that the agreement was unlawful. **Plaintiff seeks invalidation of the
> agreement, as well as damages on our behalf.** In April 2026, the U.S. Department of Commerce removed the
> case to the U.S. District Court for the District of Delaware. In May 2026, defendants filed motions to
> dismiss."

**No amount, no accrual, and, uniquely among the matters, no estimability sentence at all.**
Searched for a loss-estimate sentence attached to this matter: **no instance found.**

### (h) R2 Semiconductor: resolved between the two 10-Ks

FY2024 10-K, Note 19:

> "In February 2024, the Dusseldorf court found Intel's processors infringe and issued an injunction and
> recall order against Intel and its customers."

> "In light of the potential disruption to Intel's and its customers' businesses in Europe were the
> Dusseldorf Regional Court's injunction and recall order to be enforced before a decision by the appeals
> court was expected … in August 2024 Intel entered into three separate confidential agreements with R2,
> Third Point (the controlling shareholder), and TRGP Capital (a third-party organization funding the
> lawsuits) … **Across the three agreements, Intel expects to pay an aggregate amount of $780 million.**"

**The R2 heading is removed entirely from the FY2025 10-K.** It survives only as a cross-reference:
"Refer to 'Note 19: Commitments and Contingencies' within the 2024 Form 10-K for more information on
the R2 litigation." **$780 million paid to settle a patent case, and the reader of the current 10-K
must go to the prior 10-K to learn what it was.** Searched `\b655\b` (the unpaid balance) in
FY2025_10K.txt: **no instance found.**

### (i) Business Interruption Insurance Proceeds: dropped

FY2024 10-K had a heading disclosing "$ 484 million of insurance proceeds, primarily in the fourth
quarter of 2022 … recognized these receipts as a reduction of cost of sales." Searched
`insurance proceeds` in FY2025_10K.txt Note 19: **no instance found.**

### (j) Product / warranty, Raptor Lake instability: NOT in the contingencies note

**Searches run** on FY2025_10K.txt: `Raptor` (0 hits), `instabilit` (4 hits, all in Risk Factors,
none in Note 19), `warrant(y|ies)` (11 hits, none in Note 19), `arbitrat` (0 hits). **There is no
warranty-liability rollforward table in either 10-K.**

The 13th/14th-Gen instability matter is disclosed **only as a Risk Factor, with no accrual and no
amount**:

> "For example, during 2024, some of our customers experienced instability issues when using Intel Core 13
> th and 14 th Gen desktop processors, which required us to undertake an investigation and deploy
> corrective actions. This adversely impacted sales volume during 2024 and may result in higher warranty
> costs in the future."
> — FY2025 10-K, Risk Factors (identical sentence in FY2024 10-K)

**It is absent from the Q2 2026 10-Q entirely**; searches `Raptor`, `instabilit`, `warrant(y|ies)`:
no instance found.

### (k) Tax disputes as a contingency: no instance found

Searches run on FY2025_10K.txt: `tax dispute` (0), `Internal Revenue` (0), `\bIRS\b` case-sensitive
(0), `tax authorit` (2 hits, both inside the income-taxes note, neither a dispute). **No tax matter
appears in Note 19.** Tax uncertainty appears only in Note 8, see 6.4 and section 11.

### (l) Other searches returning nothing

`arbitrat`, `qui tam`, `DOJ`, `SEC investigation`, `subpoena`, `inquiry`, `ERISA`,
`Korea Fair Trade`, `Japan Fair Trade`, **no instance found** in FY2025_10K.txt. `antitrust` returns
1 hit, in a China/trade Risk Factor, not a proceeding.

## 6.3 Year-over-year comparison: what persists, what resolved, what is new

### Persist across FY2024 → FY2025 → Q2 2026

| Matter | FY2024 | FY2025 | Q2 2026 | Direction |
|---|---|---|---|---|
| EC fine | $401M accrued | Reduced to €237M; **$311M** accrued; $163M benefit; $340M cash collateral posted | **$308M**; Intel appealed to Court of Justice Feb 2026 | Improved on accrual, cash locked up |
| VLSI | $1.0B accrued | $1.0B; May 2025 licence-defence jury verdict for Intel | $1.0B; **Federal Circuit reversed and remanded the California case in April 2026** | Accrual flat; **worsened in 2026** |
| Spectre/Meltdown class actions | MTD pending | Nationwide class dismissed with prejudice; subclasses survived | Continuing | Mixed |
| Foundry-model securities class action | MTD filed, undecided | **Dismissed twice; judgment for defendants July 2025**; on appeal | Continuing | **Materially improved** |
| Foundry-model derivative suits | Several, stayed | Stayed | Stayed | Unchanged |

### Resolved / dropped between FY2024 and FY2025

| Matter | Resolution | Note |
|---|---|---|
| **R2 Semiconductor** | Settled Aug 2024, **$780M aggregate**; $655M unpaid at FY2024-end | Heading deleted from FY2025 Note 19 |
| **EC default-interest claim** (€593M/$647M sought) | EC paid **€516M/$560M** Nov 2024 | Gone from FY2025 |
| **Business interruption insurance** ($484M) | — | Heading deleted from FY2025 |

### New in FY2025

| Matter | Amount at stake |
|---|---|
| EireOg Innovations v IBM et al. | Unquantified in FY2025; **">$2.0 billion"** in Q2 2026 |
| Media Content Protection v Intel | **$66M-$398M** |

### New in Q2 2026

| Matter | Amount at stake |
|---|---|
| Derivative suit over the Warrant and Common Stock Agreement with the U.S. Department of Commerce | Not quantified; seeks **invalidation of the agreement** plus damages |

## 6.4 The recognition policy, and the language Intel never uses

**The policy, verbatim**, from FY2025 10-K, Note 2 (and repeated in MD&A critical accounting estimates):

> "**Loss Contingencies** — We are subject to loss contingencies, including various legal and regulatory
> proceedings, asserted and potential claims, liabilities related to repair or replacement of parts in
> connection with product defects, as well as product warranties and potential asset impairments that
> arise in the ordinary course of business and are subject to change, including due to sudden or rapid
> developments in proceedings or claims. **An estimated loss from such contingencies is recognized as a
> charge to income if it is probable that a loss has been incurred and the amount of the loss can be
> reasonably estimated.** We evaluate developments that could affect prior disclosures or previously
> accrued liabilities, and make adjustments as appropriate. Significant judgment is required to determine
> both likelihood of there being, and the estimated amount of, a loss related to such matters. If one or
> more of these matters were resolved against us for amounts in excess of management's estimates of
> losses, our results of operations and financial condition could be materially adversely affected ."

The MD&A version carries one extra sentence the Notes version omits:

> "Certain factors have resulted in significant changes to our judgments and estimates that we made
> regarding these matters in previous quarters based on updated information that became available."

### The three findings on language

1. **"Probable" is never applied to a named matter.** The word appears only in the accounting policy.
   Search `probable` in FY2025_10K.txt: 4 hits, **none in Note 19**.
2. **"Reasonably possible" appears nowhere in any legal-contingency note.** In FY2025_10K.txt it
   returns 2 hits, both in Item 7A market-risk sensitivity (currency and equity price). In
   FY2024_10K.txt, 3 hits, two in Item 7A, one in the income-taxes note. In Q2_2026_10Q.txt:
   **no instance found.**
3. **Every unaccrued matter uses one identical formula:** "we are unable to make a reasonable estimate
   of the potential loss or range of losses, if any, that might arise from" the matter. Every accrued
   matter uses: "we are unable to make a reasonable estimate of losses in excess of recorded amounts"
   (VLSI) or "in excess of this amount" (EC).

**ASC 450-20-50-4 requires disclosure of the estimated range of reasonably possible loss in excess of
accrual, or a statement that such an estimate cannot be made.** Intel takes the second option
uniformly, on every matter, in every period. **That is permitted, and it is common practice. It is
also a total absence of quantified downside disclosure across an exposure set that includes a $2.2B
vacated judgment, a $949M verdict, and a $2.0B indemnity claim, against $1.31B of accrual.**

### One disclosure that was quantified and then stopped being

FY2024 10-K, Note 8, carried a quantified 12-month sensitivity on unrecognised tax benefits:

> "…it is reasonably possible that certain US federal and non-US tax audits may be concluded within the
> next 12 months, which could increase or decrease the balance of our gross unrecognized tax benefits. **We
> estimate that the unrecognized tax benefits as of December 28, 2024, could decrease by as much as $ 314
> million in the next 12 months.**"

Searches run on FY2025_10K.txt for a successor sentence: `reasonably possible` (2 hits, both Item 7A),
`next 12 months` within the Note 8 range, `could decrease by as much as`, `tax authorit` (2 hits, both
table labels). **No instance found. Intel removed the quantified 12-month UTB sensitivity in FY2025.**
Gross unrecognised tax benefits meanwhile *rose* from $1,130M to $1,384M.

## 6.5 Non-legal commitments in the same note

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Commitments for capital expenditures | $27.5B | $20.0B | **$12.8B** |
| Other purchase obligations and commitments | ~$8.3B | ~$7.0B | **~$6.7B** |
| Remaining unfunded Arizona SCIP contribution | — | $10.5B | **$5.2B** |

> "Commitments for capital expenditures totaled $ 12.8 billion as of December 27, 2025 ($ 20.0 billion as
> of December 28, 2024), a majority of which will be due within the next 12 months. Other purchase
> obligations and commitments totaled approximately $ 6.7 billion as of December 27, 2025 (approximately
> $ 7.0 billion as of December 28, 2024)."

**Capital commitments have more than halved in two years, from $27.5B to $12.8B.** This corroborates
the "more disciplined approach to the deployment of capital" language quoted in section 3.4. It is
consistent behaviour, not just consistent words.

**Note the Q2 2026 10-Q has no Leases/Commitments section in Note 14 at all**; searched
`Commitments for capital` in Q2_2026_10Q.txt: **no instance found.**

## 6.6 Summary for the file

**Total quantified claims outstanding against ~$1.31B of accrual:**

| Matter | Amount claimed / at stake | Accrued |
|---|---|---|
| VLSI, first Texas case | $2.2B judgment (damages vacated, remanded) | part of $1.0B |
| VLSI, second Texas case | $3.0B sought (Intel won at trial) | part of $1.0B |
| VLSI, third Texas case | $949M verdict + running royalty | part of $1.0B |
| EireOg (indemnity) | **">$2.0 billion"** | nil |
| EC fine | €237M / $277M as reduced | $308M |
| Media Content Protection | $66M-$398M (Intel won, on appeal) | nil |
| Spectre/Meltdown class actions | not specified | nil |
| Securities class action + derivatives | not specified | nil |
| DoC Warrant Agreement derivative suit | not specified; seeks invalidation | nil |
| Raptor Lake instability | not specified; Risk Factor only | nil |

**Balanced reading.** Intel's litigation record over the two years is mostly one of *winning*, the
foundry securities case dismissed twice with judgment entered for defendants, the second VLSI Texas
case won at trial, the VLSI licence-defence predicate won before a jury, the MCP patents invalidated
on summary judgment, the EireOg Cisco trial won, the nationwide Spectre class dismissed with
prejudice, and the EC fine cut by a third. Against that: the April 2026 Federal Circuit reversal in
the California VLSI case, an unaccrued $2.0B indemnity claim, a $780M settlement whose description was
removed from the current 10-K, and a new suit attacking the government equity agreement.

---

# 7. ASC 842 LEASES

## 7.1 Where the disclosure is

There is **no standalone lease note**. The lease disclosure sits inside **Note 19: Commitments and
Contingencies** under a "Leases" subheading (FY2025 10-K, line 2309; page marker "… 101").
Searches run: `operating lease` (10 hits FY2025, 11 FY2024, 0 Q2 10-Q), `finance lease` (4 / 5 / 2),
`right-of-use` (**0 hits in all four documents**; Intel uses "leased assets", not "right-of-use
asset" or "ROU"), `ASC 842` (0 hits), `Topic 842` (0 hits).

## 7.2 The full lease disclosure, verbatim

FY2025 10-K, Note 19, "Leases" (line 2309):

> "We recognized operating leased assets in other long-term assets of $ 421 million ($ 457 million in
> 2024) and corresponding other accrued liabilities of $ 110 million ($ 181 million in 2024), and other
> long-term liabilities of $ 281 million ($ 279 million in 2024) as of December 27, 2025. Our operating
> leases have remaining terms of 1 to 11 years and may include options to extend the leases for up to
> 36 years. The weighted average remaining lease term was 6.7 years ( 6.5 years in 2024), and the
> weighted average discount rate was 4.7 % ( 4.9 % in 2024) as of December 27, 2025 for our operating
> leases.
>  Operating lease expense was $ 212 million in 2025 ($ 248 million in 2024 and $ 407 million in 2023),
> including $ 100 million in variable lease expense in 2025 ($ 98 million in 2024 and $ 213 million in
> 2023).
>  We recognized finance leased assets in property, plant and equipment of $ 453 million as of December
> 27, 2025 ($ 470 million as of December 28, 2024) of which the majority is related to a prepaid finance
> lease for supplier capacity. This lease will commence upon start of supplier production and has a term
> of 6 years.
>  We incurred non-cash impairment charges of $ 48 million in 2025 on certain leased assets as a direct
> result of the 2025 and 2024 Restructuring Plans ($ 83 million in 2024 as a result of the 2024
> Restructuring Plan; see "Note 7: Restructuring and Other Charges" within Notes to Consolidated
> Financial Statements). These charges were included within restructuring and other ."

## 7.3 The maturity schedule

FY2025 10-K, Note 19 (line 2309), "Discounted and undiscounted lease payments under non-cancelable
leases as of December 27, 2025, were as follows:"

> "(In Millions) 	2026 	2027 	2028 	2029 	2030 	Thereafter 	Total 	
>  Operating lease payments 	$ 	94 	$ 	74 	$ 	63 	$ 	46 	$ 	45 	$ 	100 	$ 	422 	
>  Finance lease payments 	$ 	96 	$ 	6 	$ 	6 	$ 	3 	$ 	3 	$ 	19 	$ 	133 	
>  Present value of lease payments 	$ 	473"

## 7.4 Confirmed figures

| Item, as of Dec 27, 2025 | $M | Prior year |
|---|---|---|
| Operating leased assets (in *other long-term assets*) | **421** | 457 |
| Operating lease liability, current (*other accrued liabilities*) | 110 | 181 |
| Operating lease liability, long-term (*other long-term liabilities*) | 281 | 279 |
| **Total operating lease liabilities** | **391** | 460 |
| Undiscounted operating lease payments | 422 | — |
| Weighted average remaining term / discount rate | 6.7 yrs / 4.7% | 6.5 yrs / 4.9% |
| Operating lease expense (FY2025), incl. $100M variable | 212 | 248 (2024), 407 (2023) |
| **Finance leased assets (in *property, plant and equipment*)** | **453** | 470 |
| Undiscounted finance lease payments, total | **133** | — |
| of which, due in 2026 | **96** | — |

**The ~$421M operating ROU figure in the brief is confirmed exactly.** Leases are immaterial to
Intel: total operating lease liabilities of $391M against $211.4B of total assets is 0.19%. There is
no hidden off-balance-sheet lease obligation of any size here.

## 7.5 The finance lease payment anomaly: an open question

The brief flags an $832M finance lease payment in H1 2026. It is confirmed. Q2 2026 10-Q,
Consolidated Condensed Statements of Cash Flows, financing activities (line 247):

> "Payments on finance leases 	( 832 ) 	( 9 )"

**This does not reconcile to the FY2025 disclosure.** As of December 27, 2025 Intel disclosed total
*undiscounted* finance lease payments of **$133M**, of which **$96M** was due in the whole of 2026,
against finance leased assets of $453M. Six months later Intel paid **$832M**, 6.3x the entire
disclosed remaining obligation and 8.7x the amount scheduled for the full year.

Historic finance lease payments for context (from the AFCF reconciliations, section 2.4):
2020 $0, 2021 $0, 2022 $345M, 2023 $96M, 2024 $1M, 2025 $105M. **H1 2026 alone is larger than the
previous six years combined ($547M).**

**The Q2 2026 10-Q contains no lease note and no explanation of the $832M.** Searches run on the
10-Q: `finance lease` (2 hits, the cash flow line and the MD&A sentence below), `operating lease`
(0 hits), `right-of-use` (0 hits), `Leases` as a note heading (0 hits). The only narrative is:

> "Cash used for financing activities in the first six months of 2026, compared to cash provided by
> financing activities in the first six months of 2025, primarily related to partner distributions made
> to Apollo in connection with our repurchase of the 49% minority ownership interest in Ireland SCIP,
> repayment of term debt, the absence of proceeds from commercial paper issuances, **higher payments on
> finance leases** and restricted stock unit withholdings in the first six months of 2026."
> — Q2 2026 10-Q, MD&A "Financing Activities" (line 1046, page marker "MD&A 40") *(emphasis added)*

"Higher payments on finance leases" is the entire disclosure for an 832x year-on-year increase that
exceeds the disclosed total obligation by a factor of six. **Most likely explanation, to be
confirmed, not asserted:** the FY2025 note says the finance leased asset is "a prepaid finance lease
for supplier capacity" that "will commence upon start of supplier production", commencement in H1
2026 would bring a new, much larger liability on balance sheet that was never in the FY2025 maturity
table. **This is UNRESEARCHED. The document that would resolve it is the FY2026 10-K lease note, or
the Q3 2026 10-Q. Named and gettable.**

---

# 8. SOFTWARE CAPEX / CAPITALISED SOFTWARE

## 8.1 Explicit codification references: no instance found

**Searches run:** `ASC 350-40`, `350-40`, `985-20`, `Topic 350`, `capitalized software`,
`capitalised software`, `software development cost`.
**Result: `350-40` = 0 hits, `985-20` = 0 hits, `Topic 350` = 0 hits, `capitalized software` = 0 hits
in all four documents.** Intel never cites the internal-use software or software-to-be-sold
subtopics by number, and never uses the phrase "capitalized software".

`internal-use software` returns **1 hit in FY2025 10-K, 2 in FY2024 10-K, 0 in the Q2 2026 10-Q and
0 in the DEF 14A**.

## 8.2 What the filings do say

**Policy**, from FY2025 10-K, Note 2: Accounting Policies, "Identified Intangible Assets" (line 1255,
page marker "… 65"). This is the only surviving mention in the FY2025 10-K:

> "We amortize intangible assets, including internal-use software, that are subject to amortization
> using the straight-line method over their estimated useful lives."

**The only quantification ever given**, from FY2024 10-K, Note 12: Identified Intangible Assets
(line 1915, page marker "… 83"):

> "December 28, 2024 	December 30, 2023 	
>  (In Millions) 	Gross Assets 	Accumulated Amortization 	Net 	Gross Assets 	Accumulated Amortization 	Net 	
>  Developed technology 	$ 	8,007 	$ 	( 6,445 ) 	$ 	1,562 	$ 	10,520 	$ 	( 7,996 ) 	$ 	2,524 	
>  Customer relationships and brands 	1,907 	( 1,372 ) 	535 	1,986 	( 1,286 ) 	700 	
>  Licensed technology and patents 	3,387 	( 1,852 ) 	1,535 	3,088 	( 1,728 ) 	1,360 	
>  Internal-use software 	128 	( 73 ) 	55 	— 	— 	— 	
>  Other non-amortizing intangibles 	4 	— 	4 	5 	— 	5 	
>  Total identified intangible assets 	$ 	13,433 	$ 	( 9,742 ) 	$ 	3,691 	$ 	15,599 	$ 	( 11,010 ) 	$ 	4,589"

And the amortization table, FY2024 10-K (line 1924):

> "Internal-use software 	Marketing, general, and administrative 	24 	— 	— 	5 years"

## 8.3 The line existed for exactly one year

Internal-use software appears as a separate intangible line for the **first time in FY2024**
($128M gross, $55M net, zero in the FY2023 comparative) and is **gone from the FY2025 10-K**, where
Note 12 (line 1914) shows only three categories:

> "Developed technology … Customer relationships and brands … Licensed technology, patents and other …"

The merge is arithmetically exact (see 4.7): $3,387 + $128 + $4 = $3,519 gross, matching the restated
FY2024 comparative in the FY2025 10-K. **No restatement note explains the line's disappearance.**

## 8.4 Assessment

**Capitalised software is not a Q3 concern at Intel.** The maximum ever disclosed is $128M gross 
0.06% of $211B total assets, and 1.0% of the $13.4B intangible balance. There is no evidence of
software capitalisation being used to flatter earnings. The only criticism available is a
disclosure-granularity one: a line item was broken out for one year and then quietly re-absorbed.

---

# 9. SCIP / PARTNER ARRANGEMENTS

This section contains the single most important item in this evidence file.

## 9.1 What SCIP is, in the filing's own words

Search hits: `SCIP`, 81 (FY2025 10-K), 63 (FY2024), 78 (Q2 2026 10-Q), 12 (DEF 14A).
`Brookfield`, 6 / 10 / 3 / 0. `Apollo`, 8 / 11 / 11 / 0.

FY2024 10-K, "Our Strategy" / Smart Capital (line 170):

> "▪ SCIP. We access strategically aligned private capital to increase our flexibility and help
> efficiently accelerate and scale manufacturing build-outs. Our SCIP program has supported the period
> of accelerated manufacturing investment that commenced in early 2021. We signed our latest SCIP
> agreement in the second quarter of 2024 and are not contemplating further transactions in the near
> term."

**Ireland SCIP**, from FY2025 10-K, Note 4: Non-Controlling Interests (line 1448; page marker "… 75"):

> "In the second quarter of 2024, we closed a transaction with Apollo involving the sale of 49 % of our
> interest in an Irish limited liability company (Ireland SCIP) for net proceeds of $ 11.0 billion,
> which increased our capital in excess of par value. We consolidate the results of Ireland SCIP, a
> VIE, into our Consolidated Financial Statements because we are the primary beneficiary. Generally,
> distributions will be received from Ireland SCIP based on each investor's respective ownership of
> Ireland SCIP, of which Intel's is 51 %. Ireland SCIP has rights to factory output of an Intel owned
> wafer fabrication plant in Ireland (Fab 34) and rights to resell the factory output to us. We retain
> sole ownership of Fab 34 and we are engaged as the Fab 34 operator in exchange for variable payments
> from Ireland SCIP based on the related factory output."

**The obligations attached**, same note:

> "We are required to substantially complete construction of Fab 34 in accordance with contractual
> parameters and timelines or we will be required to pay delay-related liquidated damages to Apollo,
> the other investor, beginning in 2026, not to exceed $ 1.1 billion in total. As of December 27, 2025
> and December 28, 2024, we expected certain construction milestones for Fab 34 would be delayed as we
> refined our near-term production capacity requirements and related capital outlays relative to those
> that are required per the Ireland SCIP agreement. As a result, in 2024 we recognized a loss of $ 755
> million within interest and other, net from the change in fair value of the liquidated damage
> provisions, which qualify as a non-designated derivative we recognized within other accrued
> liabilities for $ 179 million and other long-term liabilities for $ 576 million as of December 27,
> 2025 ($ 755 million in other long-term liabilities as of December 28, 2024). … We will be required to
> purchase minimum quantities of the related factory output from Ireland SCIP, or we will be subject to
> certain volume-related damages payable to Ireland SCIP, beginning at the earlier of when construction
> is complete or the third quarter of 2027."

**Arizona SCIP**, from FY2025 10-K, Note 4 (line 1448):

> "We consolidate the results of an Arizona limited liability company (Arizona SCIP), a VIE, into our
> Consolidated Financial Statements because we are the primary beneficiary. Contributions and
> distributions made between Arizona SCIP and investors are generally made based on our and
> Brookfield's proportional ownership interest in Arizona SCIP.
>  We are the primary beneficiary of two new chip factories still partially under construction by
> Arizona SCIP; we have the right to direct how and for what purpose the underlying assets will be used
> and to purchase 100 % of the wafer output. During the year ended December 27, 2025, Arizona SCIP
> placed the first tranche of manufacturing assets into service, making the assets available for our
> use. When the production contract commences in 2026, as the sole operator we will be required to
> operate Arizona SCIP at minimum production levels and will be required to limit excess inventory held
> on site or we will be subject to certain volume-related damages payable to Arizona SCIP.
>  The property, plant and equipment assets owned by Arizona SCIP and included in our Consolidated
> Balance Sheets as of December 27, 2025, which are not available to us as they can be used only to
> settle obligations of the VIE, consisted of construction in progress assets of $ 5.6 billion ($ 11.5
> billion as of December 28, 2024) and assets that have been placed into service of $ 12.2 billion (none
> as of December 28, 2024). The remaining assets and liabilities of Arizona SCIP were eliminated in our
> Consolidated Balance Sheets."

**Remaining unfunded commitment**, from FY2025 10-K, Note 19 (line 2309 area):

> "Other purchase commitments also include our unrecognized commitment to fund our respective share of
> the total construction costs of Arizona SCIP in connection with the definitive agreement entered into
> with Brookfield during 2022 … Our remaining unfunded contribution was $ 5.2 billion as of December 27,
> 2025."

## 9.2 The non-controlling interest rollforward

FY2025 10-K, Note 4 (line 1448):

> "Non-Controlling Ownership % 	Dec 27, 2025 	Dec 28, 2024 	
>  Ireland SCIP 	49 	% 	49 	% 	
>  Arizona SCIP 	49 	% 	49 	% 	
>  Mobileye 	20 	% 	12 	% 	
>  IMS Nanofabrication (IMS Nano) 	32 	% 	32 	%"

> "(In Millions) 	Ireland SCIP 	Arizona SCIP 	Mobileye 	IMS Nano 	Total 	
>  Non-controlling interests as of Dec 31, 2022 	$ 	— 	$ 	874 	$ 	989 	$ 	— 	$ 	1,863 	
>  Partner contributions 	— 	1,511 	— 	— 	1,511 	
>  … Non-controlling interests as of Dec 30, 2023 	— 	2,359 	1,838 	178 	4,375 	
>  Partner contributions 	— 	1,702 	— 	— 	1,702 	
>  Partner distributions 	( 43 ) 	— 	— 	— 	( 43 ) 	
>  … Non-controlling interests as of Dec 28, 2024 	61 	3,888 	1,672 	141 	5,762 	
>  Partner contributions 	— 	5,108 	— 	— 	5,108 	
>  Partner distributions 	( 217 ) 	— 	— 	— 	( 217 ) 	
>  Changes in equity of non-controlling interest holders 	— 	— 	1,133 	— 	1,133 	
>  Net income (loss) attributable to non-controlling interests 	268 	110 	( 57 ) 	( 28 ) 	293 	
>  Non-controlling interests as of Dec 27, 2025 	$ 	112 	$ 	9,106 	$ 	2,748 	$ 	113 	$ 	12,079"

## 9.3 THE $14,339M: the Apollo round trip

**The $14,339M "Partner distributions" line in H1 2026 financing cash flow is the repurchase of the
49% of Ireland SCIP that Intel sold to Apollo in Q2 2024.**

Q2 2026 10-Q, Consolidated Condensed Statements of Cash Flows (line 219):

> "Partner contributions 	4,082 	2,238 	
>  Partner distributions 	( 14,339 ) 	( 91 )"

Q2 2026 10-Q, Note 3: Non-Controlling Interests (line 414; page marker "Financial Statements / Notes
to Financial Statements 12"):

> "On April 8, 2026, we reacquired Apollo's 49 % minority ownership interest in Ireland SCIP for
> aggregate cash consideration of $ 14.2 billion, inclusive of transaction costs. As of June 27, 2026,
> we own 100 % of Ireland SCIP and the related operating and other ancillary agreements between Ireland
> SCIP, ourselves and Apollo have been substantially terminated. As a result of this equity
> transaction, we eliminated the $ 142 million non-controlling interest balance related to Ireland SCIP,
> extinguished the $ 532 million derivative liability associated with the delay-related liquidated
> damage provisions (refer to "Note 13: Derivative Financial Instruments" within Notes to Consolidated
> Condensed Financial Statements) and recognized the residual consideration of $ 13.5 billion as a
> reduction to our capital in excess of par value. Cash consideration paid to Apollo has been included
> within partner distributions in the Consolidated Condensed Statements of Cash Flows for the six months
> ended June 27, 2026."

### The arithmetic of the round trip

| | |
|---|---|
| Q2 2024, sold 49% of Ireland SCIP to Apollo | **+$11.0B** net proceeds, credited to capital in excess of par |
| 2024, loss on liquidated-damages derivative from construction delay | **$(755)M** through interest and other, net |
| 2024-2025, partner distributions to Apollo | $(43)M + $(217)M = $(260)M |
| H1 2026, partner distributions declared to Apollo | $(105)M |
| Q1 2026, benefit from reduction in liquidated-damages liability | +$223M |
| **8 Apr 2026, bought the same 49% back** | **$(14.2)B** cash, of which **$13.5B** debited to capital in excess of par |

**Intel sold a 49% interest for $11.0 billion and bought it back 23 months later for $14.2 billion.**
The gross cash cost of the round trip is approximately **$3.2 billion**, before the $755M derivative
loss and the $365M of distributions paid to Apollo along the way.

**None of it touched the income statement.** The $11.0B in was "an increase [to] our capital in excess
of par value"; the $13.5B residual out was "a reduction to our capital in excess of par value". Both
legs are financing cash flows. **A shareholder reading only the income statement, or only net income,
would see no trace of a $3.2 billion cost.** The only place the round trip is visible is the equity
statement and the financing section of the cash flow statement.

Corroborating detail in the equity statement, Q2 2026 10-Q (line 247 area):

> "Partner distributions declared and repurchase of subsidiary shares 	— 	( 13,545 ) 	— 	— 	( 285 ) 	( 13,830 )"

And the ownership table now reads, Q2 2026 10-Q Note 3 (line 414):

> "Non-Controlling Ownership % 	Jun 27, 2026 	Jun 28, 2025 	
>  Ireland SCIP 	— 	% 	49 	%"

**Arizona SCIP continues.** Q2 2026 10-Q, Note 3:

> "The production contract commenced in the first quarter of 2026 and we are required to both operate
> Arizona SCIP at minimum production levels and limit excess inventory held on site or we will be
> subject to certain volume-related damages payable to Arizona SCIP."
> "… construction in progress assets of $ 6.0 billion ($ 5.6 billion as of December 27, 2025) and assets
> that have been placed into service of $ 13.8 billion ($ 12.2 billion as of December 27, 2025)."

Arizona SCIP non-controlling interest grew from $3,888M (Dec 2024) to $9,106M (Dec 2025) to
**$13,428M (Jun 2026)**, and total non-controlling interests are now **$15,601M**.

## 9.4 Why this matters for Q3

Three points, stated as evidence rather than verdict:

1. **The financing structure moves very large sums through equity, bypassing earnings entirely.**
   $11.0B in (2024) and $13.5B out (2026) were both booked to capital in excess of par value. Neither
   the gain nor the loss on a $3.2B round trip appears in net income in any year.
2. **The Adjusted Free Cash Flow definition nets "SCIP partner contributions" against capex** (section
   2.3). Partner money coming *in* improves the non-GAAP measure. It is not clear from these documents
   that the $14.3B going back *out* is treated symmetrically, and the Q2 2026 10-Q does not present
   Adjusted Free Cash Flow at all (0 hits for both `non-GAAP` and `free cash flow`).
3. **The SCIP agreements carry hard operating obligations that survive:** minimum production levels at
   Arizona SCIP with volume-related damages; up to $1.1B of Fab 34 delay damages (now extinguished for
   Ireland); a $5.2B remaining unfunded contribution to Arizona SCIP. These are commitments to run
   factories at volume, entered into by a company whose own MD&A says its "cost structure requires
   manufacturing volumes beyond what we expect from our own products."

---

# 10. ACQUISITIONS IN THE LAST 5 YEARS

## 10.1 The cash flow line

**Searches run:** `acquisition`, `acquired`, `Acquisitions, net of cash acquired`,
`Tower Semiconductor`, `SiFive`.

**`SiFive` returns 0 hits in all four documents.** No instance found.

FY2024 10-K, Consolidated Statements of Cash Flows (line 1229):

> "Acquisitions, net of cash acquired 	( 82 ) 	( 13 ) 	( 681 )"

i.e. **2024: $82M · 2023: $13M · 2022: $681M**.

**The FY2025 10-K cash flow statement has no "Acquisitions, net of cash acquired" line at all** 
the investing section (line 1158) runs: Additions to PP&E; Proceeds from capital-related government
incentives; Purchases of short-term investments; Maturities and sales of short-term investments;
Sales of equity investments; Proceeds from divestitures, net; Other investing. **Intel made no
acquisitions in FY2025.**

| Fiscal year | Acquisitions, net of cash acquired |
|---|---|
| 2022 | $681M |
| 2023 | $13M |
| 2024 | $82M |
| 2025 | **nil** (line absent from the statement) |
| H1 2026 | **$596M** |

**There is no absolute-size acquisition in the last five years.** The aggregate of all acquisitions
2022-H1 2026 is roughly **$1.37 billion**, against $211B of total assets. Intel's capital has gone
into fabs, not M&A. **On this count there is no empire-building-by-acquisition evidence.**

## 10.2 The $596M in H1 2026: identified

Q2 2026 10-Q, Note 9: Acquisitions and Divestitures (line 572; page marker "… 18"):

> "Mobileye's Acquisition of Mentee Robotics
>  On February 3, 2026, Mobileye closed the acquisition of Mentee Robotics, an AI-first humanoid
> robotics company, for a purchase price of $ 637 million. Acquisition consideration consisted primarily
> of $ 596 million in cash, net of cash acquired, with the residual in Mobileye's Class A shares that
> are not contingent on continuing employment. The purchase price, net of cash acquired, was primarily
> allocated to intangible assets of $ 128 million and goodwill of $ 498 million. The goodwill arising
> from the acquisition is attributed to the synergies and other benefits that are expected to be
> generated from the combination of Mobileye and Mentee Robotics, and the acquisition-related intangible
> assets are related to developed technology. We expect the goodwill to be deductible for tax purposes.
> The operating results of Mentee Robotics, which were not material for the three and six months ended
> June 27, 2026, are included in Mobileye's financial results within our "All Other" category of
> non-reportable segments. Our accounting for the transaction is based on our preliminary valuations and
> estimates and may be subject to change if additional information becomes available during the
> measurement period."

**The $596M is Mobileye's purchase of Mentee Robotics, not an Intel-level acquisition.** $498M of the
$637M price (78%) is goodwill.

### A price discrepancy worth noting

The FY2025 10-K, MD&A "Funding Requirements" (line 645), announced the deal at a materially higher
figure:

> "In January 2026, Mobileye entered into a definitive agreement to acquire Mentee Robotics for an
> aggregate purchase price of approximately $900 million, subject to customary adjustments and closing
> conditions."

The Q2 2026 10-Q records the closed price as **$637 million**. The gap is **~$263 million (29%)**.
The 10-Q offers no reconciliation. The FY2025 language does say "subject to customary adjustments and
closing conditions." **This is UNRESEARCHED, not a finding. The document that would resolve it is
Mobileye's own 10-Q/20-F or the transaction 8-K. Named and gettable.**

## 10.3 The Tower Semiconductor termination

`Tower Semiconductor` returns 1 hit in each 10-K (the Key Terms glossary: "Tower 	Tower Semiconductor
Ltd"). The substantive references are to the **terminated** acquisition and its break fee.

FY2025 10-K, Note 7 (line 1636):

> "The 2023 charges also included a $ 353 million termination fee in connection with our inability to
> timely obtain required regulatory approvals needed to acquire Tower in accordance with the contractual
> terms of the terminated acquisition agreement and a $ 401 million charge for the original EC-imposed
> fine."

FY2024 10-K, Note 7 (line 1721), same event, slightly different wording:

> "2023 charges also included a $ 401 million charge for an EC-imposed fine and a $ 353 million
> termination fee in connection with our inability to timely obtain required regulatory approvals needed
> to acquire Tower."

**The one large acquisition Intel attempted in this period failed on regulatory approval and cost
$353M in break fees for nothing.** Note the framing: "our inability to timely obtain required
regulatory approvals", Intel attributes the failure to itself, which is candid.

## 10.4 Divestitures dominate: the direction of travel is out, not in

The material transactions in the period are disposals:

**Altera**, from FY2025 10-K, Note 10 (line 1837; page marker "… 88"):

> "On September 12, 2025, we completed the divestiture of 51 % of Altera for net purchase consideration
> of $ 4.3 billion, consisting of: $ 4.3 billion in cash proceeds received at the closing; $ 500 million
> in deferred cash proceeds also received within the third quarter of 2025; $ 500 million in deferred
> cash proceeds payable to us no later than December 31, 2027; an offset of $ 400 million for cash
> transferred to Altera with the sale; an offset of approximately $ 469 million in separation and
> employee-related costs we have agreed to fund to SLP; and an offset for other direct and incremental
> costs incurred in connection with the sale."

> "Our sale of a 51 % controlling stake in Altera … resulted in a pre-tax gain of $ 5.6 billion
> recognized within interest and other, net in 2025."

**Note the asymmetry with section 9.3:** a $5.6 billion gain on the Altera disposal ran *through the
income statement* in interest and other, net. The $3.2 billion cost of the Apollo round trip did not.
Intel booked the favourable non-operating item in earnings and the unfavourable one in equity.
Retained interest: "The $ 3.2 billion value of our non-marketable equity investment in Altera".

**Mobileye stake sale**, from FY2025 10-K, Note 4 (line 1448):

> "In 2025, we converted 113.7 million of our Mobileye Class B shares into Class A shares. We
> subsequently sold 57.5 million of the Class A shares in a secondary offering, representing 7 % of
> Mobileye's outstanding capital stock, for $ 16.50 per share and received net proceeds of $ 921 million."

**NAND memory business**, from Q2 2026 10-Q, Note 9 (line 572):

> "We sold our NAND memory technology and manufacturing business to SK hynix, which we deconsolidated
> upon closing the first phase of the transaction on December 29, 2021. On March 27, 2025, we closed the
> second phase of the transaction, collected the outstanding receivable and entered into a final release
> and settlement agreement with SK hynix primarily related to certain penalties and contingencies
> associated with the manufacturing and sale agreement between us and SK hynix."

FY2025 10-K notes the charge side: "Other, net in 2025 included charges of $ 229 million related to
the sale of our NAND memory business".

---

# 11. CASH TAX TELL [E4-30]

## 11.1 A disclosure relocation to note first

**In FY2025 Intel removed "Income taxes, net of refunds" from the face of the cash flow statement.**

FY2024 10-K, Consolidated Statements of Cash Flows (line 1253; page marker "… 60"), both lines
present:

> "Cash paid during the year for: 	
>  Interest, net of capitalized interest 	$ 	987 	$ 	613 	$ 	459 	
>  Income taxes, net of refunds 	$ 	2,202 	$ 	2,621 	$ 	4,282"

FY2025 10-K, Consolidated Statements of Cash Flows (line 1185; page marker "… 63"), **income taxes
gone from the face**:

> "Cash paid during the year for: 	
>  Interest, net of capitalized interest 	$ 	1,106 	$ 	987 	$ 	613 	
>  See accompanying notes."

The figure moved into Note 8: Income Taxes, under a new "Cash Taxes Paid" heading (line 1787; page
marker "… 86"). **This is a required improvement, not concealment**: the relocation is the direct
consequence of adopting ASU 2023-09, and the new presentation is *more* informative because it adds a
jurisdictional split. Recorded here so the reader is not misled by the line's disappearance:

> "Cash Taxes Paid
>  We adopted ASU 2023-09 on a prospective basis for the year ended December 27, 2025 and have included
> the following table as a result of our adoption, which presents income taxes paid (net of refunds
> received) for the year ended December 27, 2025:
>  Year Ended (In Millions) 	Dec 27, 2025 	
>  Federal taxes 	$ 	1,393 	
>  State taxes 	( 7 ) 	
>  Foreign taxes: 	
>  China 	276 	
>  Israel 	197 	
>  Other foreign jurisdictions 	440 	
>  Total cash taxes paid 	$ 	2,299 	
>  Below is a summary of income taxes paid for the years ended December 28, 2024 and December 30, 2023:
>  Years Ended (In Millions) 	Dec 28, 2024 	Dec 30, 2023 	
>  Cash paid during the year for: 
>  Income taxes, net of refunds 	$ 	2,202 	$ 	2,621"

## 11.2 The table: cash taxes against pre-tax income

Sources: FY2025 10-K Note 8 (line 1787) and the tax provision table (line 1637); FY2024 10-K Note 8
(line 1740 area) and cash flow statement (line 1253); Q2 2026 10-Q Note 7 (line 524) and cash flow
(line 247).

| $M | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|---|
| **Income (loss) before taxes, total** | **7,768** | **762** | **(11,210)** | **1,557** | **(14,765)** |
| of which U.S. | (1,161) | (4,749) | (13,450) | (3,231) | n/d |
| of which non-U.S. | 8,929 | 5,511 | 2,241 | 4,788 | n/d |
| Current provision | 4,909 | 1,096 | 1,956 | 1,202 | n/d |
| Deferred provision | (5,158) | (2,009) | 6,067 | 329 | n/d |
| **Total provision for (benefit from) taxes** | **(249)** | **(913)** | **8,023** | **1,531** | **364** |
| Effective tax rate | (3.2)% | (119.8)% | 71.6% | 98.3% | (2.5)% |
| **Income taxes PAID, net of refunds** | **4,282** | **2,621** | **2,202** | **2,299** | **904** |
| **Cash taxes ÷ pre-tax income** | 55% | **344%** | n/m (loss) | **148%** | n/m (loss) |
| **Cash taxes ÷ book provision** | n/m (benefit) | n/m (benefit) | 27% | 150% | 248% |

## 11.3 What the tell says

**Intel pays substantial cash tax in years when it reports little or no book profit.** Over the four
full years 2022-2025 Intel paid **$11,404M of cash income tax** against **cumulative pre-tax income of
$(1,123)M**, i.e. it paid $11.4 billion of tax on a cumulative pre-tax loss. Add H1 2026 and it is
**$12,308M of cash tax against $(15,888)M of cumulative pre-tax loss.**

This runs in the *opposite* direction to the classic [E4-30] warning sign (book profits that never
become cash taxes, indicating soft earnings). Here the divergence is structurally explained and
disclosed:

1. **The profits are non-U.S.; the losses are U.S.** Non-U.S. income was positive in every year
   ($8,929M / $5,511M / $2,241M / $4,788M) while U.S. income was negative in every year
   ($(1,161)M / $(4,749)M / $(13,450)M / $(3,231)M). Foreign taxes are paid in cash regardless of the
   U.S. loss.
2. **A U.S. valuation allowance blocks any benefit from the domestic loss.** Q2 2026 10-Q, Note 7
   (line 524):

   > "In all periods presented, we were not able to benefit from our current year domestic loss before
   > taxes due to the domestic valuation allowance."

   The FY2025 10-K MD&A (line 389) attributes $9.9 billion of the 2024 tax charge to this:

   > "▪ $9.9 billion of non-cash charges recorded to provision for income taxes that substantially
   > related to valuation allowances recorded to our net deferred tax assets"

   This is what produced the 71.6% effective rate on a **pre-tax loss** in 2024, a $8,023M provision
   against an $(11,210)M loss, of which $6,067M was deferred.
3. **A large tax receivable is outstanding.** Q2 2026 10-Q, Note 7 (line 524):

   > "Additionally, our Consolidated Condensed Balance Sheets as of June 27, 2026 and December 27, 2025
   > contain certain tax receivables of $ 7.5 billion and $ 7.6 billion, respectively, within other
   > current assets , and $ 1.3 billion and $ 182 million, respectively, within other long-term assets ,
   > primarily associated with AMIC claims."

   **$8.8 billion of tax receivables at June 2026**, an asset whose realisation depends on the AMIC
   (advanced manufacturing investment credit) claims being honoured.

**Reading for Q3:** the cash-tax tell does not indicate fabricated earnings. It indicates the
opposite problem, a company whose *reported* results are propped up by non-U.S. operations while the
U.S. business loses money at a scale that has already forced a full valuation allowance against U.S.
deferred tax assets. The 98.3% effective rate in 2025, on $1,557M of pre-tax income producing $26M of
net income, is the arithmetic of that.

---
---

# OPEN ITEMS: named, gettable, and not yet obtained

Per the framework's own test, *"Can I name the document that would resolve this?"*, the following
are **UNRESEARCHED**, not UNKNOWABLE. Each names its document.

| # | Question | Document that resolves it |
|---|---|---|
| 1 | Accession numbers and filing dates for all four documents (operator rule 4) | EDGAR filing index for CIK 0000050863 |
| 2 | Pat Gelsinger's separation terms and payments | Intel DEF 14A filed 2025 (covering FY2024); Form 8-K of ~2 Dec 2024 |
| 3 | The $832M H1 2026 finance lease payment vs a $133M disclosed obligation (section 7.5) | FY2026 10-K lease note, or Q3 2026 10-Q |
| 4 | Mentee Robotics: $900M announced (FY2025 10-K) vs $637M closed (Q2 2026 10-Q) | Mobileye's own 10-Q / 20-F; the transaction 8-K |
| 5 | Restructuring plans before 2022, the full streak length | Intel 10-Ks for FY2016-FY2021 |
| 6 | Whether the $14.3B Apollo repurchase is deducted in Adjusted Free Cash Flow | FY2026 10-K MD&A "Adjustments to Cash from Operating Activities" |
| 7 | Quarterly earnings-call guidance and whether it was met | Intel Form 8-K earnings releases and CFO commentary, FY2024-FY2026 |
| 8 | The Warrant and Common Stock Agreement with the U.S. Dept of Commerce, and the Escrowed Shares mechanics behind the $13.6B H1 2026 mark-to-market loss | The agreement itself (exhibit to the Q3 2025 10-Q or an 8-K); FY2025 10-K Note 5 |

**None of the above prevents the Q3 judgement from being formed on the evidence in this file, but
items 2, 3 and 8 are material enough that the Q3 verdict should record them as open.**
