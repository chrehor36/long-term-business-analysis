# TXN — SEC primary-document research, 2026-09-06

Sourcing: **SEC EDGAR only** — `data.sec.gov` and `www.sec.gov/Archives`. Every request carried
`User-Agent: Chris Hrehor chrehor36@gmail.com`. No aggregators, no company website, no news. Operator
rule 4 satisfied throughout: the primary HTML documents were read, and XBRL figures were cross-checked
against the filed statements.

## FILE MAP

| file | task | contents |
|---|---|---|
| `00-filings-index.md` | 1 | accessions, filing dates, primary-document URLs, prior 10-K list |
| `10k-findings.md` | 2 | verbatim: capacity/fabs, 2026 capex guidance, FCF-per-share language, CHIPS Act, depreciation policy and lives |
| `capex-series.md` | 3 | capex, depreciation, CFO, FCF, revenue, GP, OP, R&D, SBC, buybacks FY2013–FY2025 + TTM 6/30/26 |
| `physical-series-sweep.md` | 4 | [E4-55] recorded sweep, exact counts, every physical number in the 10-K |
| `competitor-sweep.md` | 5 | [E2-45] competitor-name counts, full Competition text, China/geopolitical risk factors |
| `segment-series.md` | 6 | Analog / Embedded Processing / Other revenue and operating profit FY2019–FY2025 |
| `leases-and-commitments.md` | 7, 8 | ASC 842 leases; commitments, contingencies, purchase commitments, debt ladder |
| `acquisitions.md` | 9 | Lehi ($893M, Oct 2021, asset acquisition), Silicon Labs ($7.5bn pending), divestitures |
| `fab-naming-history.md` | supports 2 | SM1/SM2/RFAB2/LFAB across FY2019–FY2025 vintages and the FY2025 deletions |
| `txn-20251231_10K.htm` / `.txt` | 1 | downloaded FY2025 10-K, raw and text-extracted |
| `txn-20260630_10Q.htm` / `.txt` | 1 | downloaded Q2 2026 10-Q, raw and text-extracted |
| `prior10k/FY2018..FY2024.txt` | supports 2,3,6,9 | prior 10-K primary documents, text-extracted |
| `_companyfacts.json`, `_annual.json`, `_sweep.json`, `_table.md` | 3,4,5 | raw XBRL and sweep intermediates |

*(Other files in this folder — `10k-flag-sweep.md`, `capital-return.md`, `competitor-row.md`,
`proxy-findings.md`, `stage0-share-count.md`, `txn-FY2025-10K-flat.txt`, `txn-Q2-2026-10Q-flat.txt`,
`vintage-physical-series.json` — were written by a different worker and are not mine.)*

---

## THE IDENTIFICATION (Task 1)

**FY2025 10-K** — accession `0000097476-26-000059`, filed **2026-02-06**, period 2025-12-31, primary doc
`txn-20251231.htm`.
https://www.sec.gov/Archives/edgar/data/97476/000009747626000059/txn-20251231.htm

**Q2 2026 10-Q** — accession `0000097476-26-000152`, filed **2026-07-24**, period 2026-06-30, primary doc
`txn-20260630.htm`.
https://www.sec.gov/Archives/edgar/data/97476/000009747626000152/txn-20260630.htm

Both downloaded to this folder.

---

## THE TEN THINGS THAT MATTER

**1. Capex guidance is cut roughly in half and the six-year cycle is declared over.** FY2025 10-K, MD&A:
"We are nearing the end of our six-year elevated capital expenditures cycle, and consistent with our
capital management strategy, we are expecting to spend about **$2 billion to $3 billion in 2026**. Beyond
2026, capital expenditures will be dependent on revenue and growth expectations." Actual capex: $4,550M
(2025), $4,820M (2024), $5,071M (2023). H1 2026 actual is $1,190M against H1 2025's $2,428M — down 51%.

Cycle total: **$19.70 billion of capex FY2021–FY2025**, against $3.85 billion across FY2016–FY2020.
TI's own "about $24 billion" is a **ten**-year figure (FY2016–FY2025 sums to $23.55 billion) — do not read
it as the cycle total.

**2. Depreciation is still climbing and will cross capex.** $755M (2021) → $1,918M (2025) → $2,122M TTM.
Capex/depreciation fell from 4.3× (2023) to 1.56× (TTM). Depreciation is 10.9% of revenue against a
3.6–5.1% norm in 2017–2020.

**3. The CHIPS Act runs through the P&L as suppressed depreciation, not as income.** Policy: incentives
"related to the acquisition or construction of fixed assets are recognized as a reduction in the carrying
amounts of the related assets and reduce depreciation expense over the useful lives of the assets."
**Cumulative PP&E basis reduction: $4.51 billion** ($1.37bn in 2025, $1.78bn in 2024). Cost of revenue
benefit: **$353M / $159M / $45M** in 2025/24/23. Cash benefit: $670M (2025), $588M (2024), $1,405M in
H1 2026 alone. Receivable on balance sheet at 2025-12-31: **$3.35 billion**. Deferred income: $95M.
ITC rate raised from 25% to 35% by the OBBBA for assets placed in service after 2025-12-31. Direct funding
award up to $1.6bn, of which **$630M received** as of 2026-06-30. **Clawback rights exist and are
unquantified.** Grossed up for the subsidy, 2025 depreciation would be ~$2.27bn, not $1.92bn.

**4. TI's "free cash flow" adds the subsidy to the numerator — and the subsidy is already inside CFO.**
Definition changed in FY2025 to "cash flows from operating activities less capital expenditures, **plus
proceeds from CHIPS Act incentives**." On the pre-2025 definition, FY2025 FCF is **$2,603M**, not the
reported $2,938M, and the TTM is **$5,355M**, not $6,534M. TI names "growth of free cash flow per share"
as the governing metric and **never publishes a free-cash-flow-per-share figure anywhere in the 10-K**.

**5. Useful lives were lengthened twice, silently.** Machinery and equipment: "2 − 10" years through the
FY2022 10-K, "5 − 10" from FY2023. Buildings: "5 − 40" through FY2023, "Up to 40" from FY2024. **No
change-in-estimate disclosure exists in any vintage.** Both changes lengthen average depreciable life,
and both landed during the 300mm build.

**6. There is no physical series and there is no competitor row.** [E4-55]: "units shipped" 0,
"unit volume" 0, "wafers" 0, "wafer starts" 0, "SKU" 0, "part numbers" 0, "catalog" 0, "ASP" 0,
"average selling price" 0 (1 in the plural, inside a risk factor, unquantified). All 8 "units" hits are
restricted stock units. The only physical numbers in the whole document are 80,000 products, 100,000
customers, 33,000 employees, 30.6M sq ft, a 40% 300mm-vs-200mm cost gap, 222 days of inventory and 40 DSO.
[E2-45]: **zero named competitors** — Analog Devices, ADI, Microchip, NXP, STMicroelectronics, Infineon,
onsemi, Renesas, Broadcom, Qualcomm, Silergy, SG Micro, 3Peak and "Chinese" all return **0**. The entire
Chinese-competition disclosure is one sentence.

**7. Five checkable disclosures were deleted from the FY2025 10-K.** The named-fab bullet list
(RFAB2/LFAB1/LFAB2/SM1/SM2 — all now 0 occurrences), the construction pipeline, the "10 to 15 years"
growth horizon, the internal-sourcing percentages ("about 80% of our total wafers and about 65% of our
assembly/test production internally", FY2023 → "the majority", FY2024–25), and the cumulative CHIPS
expectation ("$7.5 billion to $9.5 billion through 2034", FY2024 → absent). Every deletion removes a
number a future year could have been checked against, in the year the story changed. SM3 and SM4 have
**never** appeared in any TXN 10-K.

**8. Embedded Processing has been gutted and the cause is a fab.** Operating profit $1,253M (2022) →
$1,008M (2023) → $352M (2024) → **$304M (2025)**; margin 38.5% → 11.3%. TI's stated reason: "Our LFAB
facility, which primarily supports our Embedded Processing business, was purchased as an operating fab and
is in the early stages of ramping" — five years after the $893M purchase. Analog held up far better:
$5,412M operating profit, 38.6% margin, but still well below the 54.4% of 2022.

**9. Dividends now exceed earnings and the buyback has been suspended in all but name.** Dividends paid
$4,557M / $4,795M / $4,999M in 2023/24/25 against net income of $6,510M / $4,799M / $5,001M. Retained
earnings **fell $26 million in 2025**. Repurchases ran $2.1–5.1bn/yr in 2013–2020 and are $293M / $929M /
$1,477M in 2023/24/25 and $707M TTM, against $18.79bn of remaining authorisation. The build was
debt-financed: total debt $14,048M, maturities to 2063, interest and debt expense $543M.

**10. A $7.5 billion all-cash acquisition lands immediately after the cycle.** Silicon Labs, $231.00/share,
announced 2026-02-04, expected close H1 2027, funded from $4.88bn of cash plus a $5bn 364-day delayed-draw
term loan arranged June 2026. It is 46% of stockholders' equity and 8.4× the Lehi purchase, and it goes
into Embedded Processing — the 11.3%-margin segment. In the prior **ten years TI made exactly one
acquisition**: the $893M Lehi fab, booked as an asset acquisition with no goodwill and buried inside the
FY2021 capex line (36% of that year's $2,462M capex). **Micron is never named in any TXN SEC filing.**

---

## OPEN ITEMS AND HONEST GAPS

| item | verdict | the document that would resolve it |
|---|---|---|
| Maintenance vs growth capex split | **UNRESEARCHED → likely UNKNOWABLE from SEC sources** | not disclosed in any 10-K; no SEC filing contains it |
| Unit volumes, wafer starts, ASPs | **UNKNOWABLE from SEC primary documents** | absent from every 10-K; TI's capital-management deck is not an SEC filing |
| Fab-level capacity, SM2/LFAB2 status after FY2024 | **UNRESEARCHED** | FY2026 10-K, or the 8-K/deck outside the SEC-primary rule |
| Competitor row (Q2 of the framework) | **UNRESEARCHED, not unknowable** | 10-Ks of ADI (CIK 0000006281), Microchip (0000827054), onsemi (0001097864); Chinese analog names file outside EDGAR |
| Reason for the two useful-life extensions | **UNRESEARCHED** | not in any 10-K; no change-in-estimate note exists |
| Clawback exposure quantum on $4.51bn of credits | **UNKNOWABLE from filings** | the Commerce Department award agreement is not filed as an exhibit |
| Seller of the Lehi fab | **not in the SEC record** | no 8-K was filed; "Micron" appears 0 times in every TXN 10-K FY2018–FY2025 |
| Identity of the 12%-of-revenue customer | **UNKNOWABLE from filings** | Note 1 says "One of our end customers" and does not name it |
| CFO for FY2013–FY2015 | **RESOLVED** | read from the FY2014 and FY2015 10-K statements, not XBRL |

**No valuation was computed and none is implied.** Nothing here constitutes a Q5 output; Q1–Q4 have not
been run. Under operator rule 3, any arithmetic downstream of this file must be headed
**"COMPUTATION — NOT A CLEARANCE"** until the gates close.
