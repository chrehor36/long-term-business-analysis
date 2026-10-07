# ORLY COMPETITOR ROW — PRIMARY-FILING DATA
### Research pull, 2026-09-02. FETCH-AND-RECORD ONLY. No verdicts, no conclusions.
### Operator rule 8: tools fetch and compute and are forbidden to conclude.
### Operator rule 4: THE FILING GETS READ. Every figure below carries document, fiscal year, accession number.

**Source discipline.** All figures from SEC EDGAR primary filings retrieved with
User-Agent `Chris Hrehor chrehor36@gmail.com`. Tagged XBRL companyfacts used only to
locate and cross-check; every headline figure cross-read against the filed statement text.

---

## 0. THE PEER SET — filing status and comparability

| Company | Ticker | CIK | Files with SEC? | Fiscal year end | Comparable to ORLY? |
|---|---|---|---|---|---|
| AutoZone | AZO | 0000866787 | YES | late August | *pending* |
| Advance Auto Parts | AAP | 0001158449 | YES | late Dec / early Jan | *pending* |
| Genuine Parts Company | GPC | 0000040987 | YES | calendar 31 Dec | *pending* |
| Monro Inc | MNRO | 0000876427 | *pending* | *pending* | *pending* |
| Valvoline | VVV | *pending* | *pending* | *pending* | *pending* |
| Driven Brands | DRVN | *pending* | *pending* | *pending* | *pending* |

## 0b. FILING INDEX CONFIRMED (10-K list from data.sec.gov/submissions)

**AutoZone (AZO), CIK 0000866787 — AUTOZONE INC**

| Filed | FY end | Accession | Primary doc |
|---|---|---|---|
| 2025-10-27 | 2025-08-30 | 0001104659-25-102611 | azo-20250830x10k.htm |
| 2024-10-28 | 2024-08-31 | 0001558370-24-013758 | azo-20240831x10k.htm |
| 2023-10-24 | 2023-08-26 | 0001558370-23-016668 | azo-20230826x10k.htm |
| 2022-10-24 | 2022-08-27 | 0001558370-22-015239 | azo-20220827x10k.htm |
| 2021-10-25 | 2021-08-28 | 0001558370-21-013446 | azo-20210828x10k.htm |
| 2020-10-26 | 2020-08-29 | 0001558370-20-011748 | azo-20200829x10k.htm |
| 2019-10-28 | 2019-08-31 | 0001193125-19-276201 | d771460d10k.htm |
| 2018-10-24 | 2018-08-25 | 0001193125-18-306452 | d597971d10k.htm |
| 2017-10-25 | 2017-08-26 | 0001193125-17-319357 | d447746d10k.htm |

**Advance Auto Parts (AAP), CIK 0001158449 — ADVANCE AUTO PARTS INC**

| Filed | FY end | Accession | Primary doc |
|---|---|---|---|
| 2026-02-13 | 2026-01-03 | 0001193125-26-051305 | aap-20260103.htm |
| 2025-02-26 | 2024-12-28 | 0001158449-25-000064 | aap-20241228.htm |
| 2024-03-12 | 2023-12-30 | 0001158449-24-000048 | aap-20231230.htm |
| 2023-02-28 | 2022-12-31 | 0001158449-23-000035 | aap-20221231.htm |
| 2022-02-15 | 2022-01-01 | 0001158449-22-000037 | aap-20220101.htm |
| 2021-02-22 | 2021-01-02 | 0001158449-21-000036 | aap-20210102.htm |
| 2020-02-18 | 2019-12-28 | 0001158449-20-000035 | aap10k12282019secreport.htm |
| 2019-02-19 | 2018-12-29 | 0001158449-19-000043 | aap_10kx12292018secreport.htm |

**Genuine Parts Company (GPC), CIK 0000040987 — GENUINE PARTS CO**

| Filed | FY end | Accession | Primary doc |
|---|---|---|---|
| 2026-02-20 | 2025-12-31 | 0000040987-26-000003 | gpc-20251231.htm |
| 2025-02-21 | 2024-12-31 | 0000040987-25-000026 | gpc-20241231.htm |
| 2024-02-22 | 2023-12-31 | 0000040987-24-000024 | gpc-20231231.htm |
| 2023-02-23 | 2022-12-31 | 0000040987-23-000008 | gpc-20221231.htm |
| 2022-02-17 | 2021-12-31 | 0000040987-22-000013 | gpc-20211231.htm |
| 2021-02-19 | 2020-12-31 | 0000040987-21-000009 | gpc-20201231.htm |
| 2020-02-21 | 2019-12-31 | 0000040987-20-000010 | gpc-12312019x10k.htm |
| 2019-02-25 | 2018-12-31 | 0000040987-19-000015 | gpc-12312018x10k.htm |

**O'Reilly (ORLY, the subject), CIK 0000898173 — for reference alongside**

| Filed | FY end | Accession | Primary doc |
|---|---|---|---|
| 2026-02-27 | 2025-12-31 | 0000898173-26-000009 | orly-20251231x10k.htm |
| 2021-02-26 | 2020-12-31 | 0000898173-21-000012 | orly-20201231x10k.htm |

**THE 5-YEAR WINDOW USED BELOW**
- AZO: FY2025 (ended 2025-08-30) vs FY2020 (ended 2020-08-29)
- AAP: FY2025 (ended 2026-01-03) vs FY2020 (ended 2021-01-02)
- GPC: FY2025 (ended 2025-12-31) vs FY2020 (ended 2020-12-31)

---

*(sections below filled as documents are read)*

---

# 1. THE [E4-55] UNITS QUESTION — ANSWERED FIRST BECAUSE IT IS THE CRITICAL ITEM

**The question:** does the filer split comparable store sales into TRANSACTION COUNT
(traffic / ticket count) and AVERAGE TICKET / PRICE?

**Method.** Every 10-K below was searched twice: once on the converted text, and once on
the raw filed HTML with all tags stripped (so a phrase broken across `<span>` elements
cannot produce a false negative). Search terms: `ticket`, `average ticket`,
`transaction count`, `traffic count`, `units sold`, `Amazon`.

## 1a. THE RESULT TABLE — raw-HTML tag-stripped occurrence counts

| Filing | FY | Accession | "ticket" | "average ticket" | "transaction count" | "Amazon" |
|---|---|---|---|---|---|---|
| **ORLY** orly-20251231x10k.htm | 2025 | 0000898173-26-000009 | **4** | **4** | **4** | **1** |
| AZO azo-20250830x10k.htm | 2025 | 0001104659-25-102611 | **0** | **0** | **0** | **0** |
| AZO azo-20200829x10k.htm | 2020 | 0001558370-20-011748 | **0** | **0** | **0** | **0** |
| AAP aap-20260103.htm | 2025 | 0001193125-26-051305 | **0** | **0** | **0** | **0** |
| AAP aap-20210102.htm | 2020 | 0001158449-21-000036 | **0** | **0** | **0** | **0** |
| GPC gpc-20251231.htm | 2025 | 0000040987-26-000003 | **0** | **0** | **0** | **0** |
| GPC gpc-20201231.htm | 2020 | 0000040987-21-000009 | **0** | **0** | **0** | **0** |

## 1b. THE FINDINGS, STATED PLAINLY

**AutoZone (AZO) — DOES NOT SPLIT.** FY2025 10-K (accession 0001104659-25-102611) and
FY2020 10-K (accession 0001558370-20-011748) contain the words "ticket", "average ticket"
and "transaction count" **zero times each**. AZO's five-year selected financial data table
discloses same store sales only as a single blended percentage, decomposed by GEOGRAPHY
(domestic / international / total company / constant currency) and never by units versus
price. AZO's own definition of the measure, quoted verbatim from the FY2025 10-K:

> "The domestic and international comparable sales increases are based on sales for all
> AutoZone stores open at least one year. Constant currency same store sales exclude
> impacts from fluctuations of foreign exchange rates by converting both the current year
> and prior year international results at the prior year foreign currency exchange rate.
> Same store sales are computed on a 52-week basis. Relocated stores are included in the
> same store sales computation based on the year the original store was opened. Closed
> store sales are included in the same store sales computation up to the week it closes,
> and excluded from the computation for all periods subsequent to closing. All sales
> through our www.autozone.com website, including consumer direct ship-to-home sales, are
> also included in the computation."
> — AZO 10-K FY2025, footnote (4) to the five-year selected financial information table,
> accession 0001104659-25-102611. **No units/price decomposition appears anywhere in it.**

**Advance Auto Parts (AAP) — DOES NOT SPLIT.** FY2025 (0001193125-26-051305) and FY2020
(0001158449-21-000036) contain "ticket", "average ticket", "transaction count" zero times.
The single hit for "traffic count" in the FY2025 10-K is **site selection, not comp-sales
decomposition** — quoted verbatim so it is not miscounted as a units disclosure:

> "The key factors used in selecting sites and market locations in which the Company
> operates include population, demographics, traffic count, vehicle profile, number and
> strength of competitors' stores and the cost of real estate."
> — AAP 10-K FY2025, Item 1 Business / Stores, accession 0001193125-26-051305.

The single hit for "units sold" is a warranty-accrual sentence, likewise not a comp-sales
decomposition:

> "The Company's historical experience has been that failure rates are relatively
> consistent over time and that the ultimate cost of warranty claims to the Company has
> been driven by volume of units sold as opposed to fluctuations in failure rates or the
> variation of the cost of individual claims."
> — AAP 10-K FY2025, Note on warranty liabilities, accession 0001193125-26-051305.

**Genuine Parts Company (GPC) — DOES NOT SPLIT.** FY2025 (0000040987-26-000003) and FY2020
(0000040987-21-000009) contain "ticket", "average ticket", "transaction count", "traffic"
zero times each. GPC reports "comparable sales" at the segment level only (Automotive
Parts Group / Industrial Parts Group) as a single blended percentage.

## 1c. THE CONTRAST — ORLY (the subject) DOES split, in one sentence

Recorded here only as the reference point the peer row is being compared against.
ORLY 10-K FY2025, accession 0000898173-26-000009, MD&A "Sales":

> "Our comparable store sales increase for the year ended December 31, 2025, was driven by
> an increase in average ticket value for both professional service provider and DIY
> customers and an increase in transaction counts for professional service provider
> customers, partially offset by a decrease in transaction counts for DIY customers.
> Average ticket values benefited from increases in average selling prices on a same-SKU
> basis, as compared to the same period in 2024, driven by increases in acquisition costs
> of inventory, principally resulting from increased tariffs, which were passed on in
> selling prices. Average ticket values also continue to be positively impacted by the
> increasing complexity and cost of replacement parts necessary to maintain the current
> population of better-engineered and more technically advanced vehicles. These
> better-engineered, more technically advanced vehicles require less frequent repairs, as
> the component parts are more durable and last for longer periods of time. The resulting
> decrease in repair frequency creates pressure on customer transaction counts; however,
> when repairs are needed, the cost of replacement parts is, on average, greater, which is
> a benefit to average ticket values. The decrease in DIY customer transaction counts was
> driven by pressured consumer spending on discretionary categories and broader industry
> pressure on certain hard part categories."

**RECORDED, NOT CONCLUDED.** The units-versus-price decomposition is available in the
primary filings for ORLY and is NOT available in the primary filings for AZO, AAP or GPC
in either year of the five-year window. Whether a physical-units test can therefore be run
on the peers from 10-K data alone is a question for the run, not for this fetch.

