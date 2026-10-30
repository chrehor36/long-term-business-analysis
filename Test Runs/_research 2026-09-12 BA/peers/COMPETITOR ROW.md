# COMPETITOR ROW — The Boeing Company (BA), Q2 (a moat is a relative claim)

**Built 2026-09-12.** Gather-and-compute only. **No moat conclusion is drawn here** — this file
is input to Q2, not an answer to it.

**Evidence class.** Everything in the peer tables is from a **primary SEC filing** (10-K or 20-F)
pulled through `tools/sources.py` (XBRL `companyfacts`) and then **cross-checked against the filed
statement** for at least one figure per company (operator rule 4). Segment-level revenue, operating
profit and backlog are **read off the filing text**, not off XBRL — `companyfacts` drops dimensioned
facts, so segment rows cannot come from the tagged data at all. The Airbus block is **one rung lower**
on the ladder (company IR site, English) and is labelled as such.

Accession numbers for every annual filing used are in **section 5, Sources**.

---

## 1. THE SAME METRIC, SAME WINDOW — latest three fiscal years

All figures **$ millions** except where noted. `OPM%` = operating profit / revenue.
Fiscal years are each company's own (TXT FY2025 ends 2026-01-03; TDG 2025-09-30; HEI 2025-10-31).

| Ticker | FY | Revenue | Op. profit | OPM% | OCF | SBC | D&A | Capex | **OE = OCF-SBC-capex** | **OE = OCF-SBC-D&A** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **BA** | 2023 | 77,794 | (773) | (1.0) | 5,960 | 690 | 1,861 | 1,527 | **3,743** | **3,409** |
| **BA** | 2024 | 66,517 | (10,707) | (16.1) | (12,080) | 407 | 1,836 | 2,230 | **(14,717)** | **(14,323)** |
| **BA** | 2025 | 89,463 | 4,281 | 4.8 | 1,065 | 426 | 1,953 | 2,942 | **(2,303)** | **(1,314)** |
| LMT | 2023 | 67,571 | 8,507 | 12.6 | 7,920 | 265 | 1,430 | 1,691 | 5,964 | 6,225 |
| LMT | 2024 | 71,043 | 7,013 | 9.9 | 6,972 | 277 | 1,559 | 1,685 | 5,010 | 5,136 |
| LMT | 2025 | 75,048 | 7,731 | 10.3 | 8,557 | 304 | 1,687 | 1,649 | 6,604 | 6,566 |
| NOC | 2023 | 39,290 | 2,537 | 6.5 | 3,875 | 87 | 1,338 | 1,775 | 2,013 | 2,450 |
| NOC | 2024 | 41,033 | 4,370 | 10.6 | 4,388 | 101 | 1,370 | 1,767 | 2,520 | 2,917 |
| NOC | 2025 | 41,954 | 4,511 | 10.8 | 4,757 | 119 | 1,472 | 1,450 | 3,188 | 3,166 |
| RTX | 2023 | 68,920 | 3,561 | 5.2 | 7,883 | 425 | 4,211 | 2,415 | 5,043 | 3,247 |
| RTX | 2024 | 80,738 | 6,538 | 8.1 | 7,159 | 437 | 4,364 | 2,625 | 4,097 | 2,358 |
| RTX | 2025 | 88,603 | 9,300 | 10.5 | 10,567 | 519 | 4,378 | 2,627 | 7,421 | 5,670 |
| GD | 2023 | 42,272 | 4,245 | 10.0 | 4,710 | 181 | 863 | 904 | 3,625 | 3,666 |
| GD | 2024 | 47,716 | 4,796 | 10.1 | 4,112 | 183 | 886 | 916 | 3,013 | 3,043 |
| GD | 2025 | 52,550 | 5,356 | 10.2 | 5,120 | 196 | 924 | 1,161 | 3,763 | 4,000 |
| TXT | 2023 | 13,683 | *1,327 (dagger)* | *9.7 (dagger)* | 1,266 | 94 | 395 | 402 | 770 | 777 |
| TXT | 2024 | 13,702 | *1,200 (dagger)* | *8.8 (dagger)* | 1,014 | 66 | 382 | 364 | 584 | 566 |
| TXT | 2025 | 14,799 | *1,363 (dagger)* | *9.2 (dagger)* | 1,312 | 81 | 401 | 383 | 848 | 830 |
| TDG | 2023 | 6,585 | 2,923 | 44.4 | 1,375 | 135 | 268 | 139 | 1,101 | 972 |
| TDG | 2024 | 7,940 | 3,531 | 44.5 | 2,045 | 188 | 312 | 165 | 1,692 | 1,545 |
| TDG | 2025 | 8,831 | 4,165 | 47.2 | 2,038 | 152 | 367 | 222 | 1,664 | 1,519 |
| HEI | 2023 | 2,968 | 625 | 21.1 | 449 | 15 | 130 | 49 | 384 | 303 |
| HEI | 2024 | 3,858 | 824 | 21.4 | 672 | 19 | 175 | 58 | 595 | 478 |
| HEI | 2025 | 4,485 | 1,019 | 22.7 | 934 | 34 | 196 | 73 | 827 | 704 |
| ERJ | 2023 | 5,268 | 314 | 6.0 | 617 | n/d (dd) | 242 | 431 | 186 | 375 |
| ERJ | 2024 | 6,395 | 668 | 10.4 | 871 | n/d (dd) | 244 | 466 | 405 | 627 |
| ERJ | 2025 | 7,578 | 608 | 8.0 | 870 | n/d (dd) | 260 | 484 | 386 | 610 |
| SPR | 2022 | 5,030 | (281) | (5.6) | (395) | 37 | 352 | 122 | (554) | (784) |
| SPR | 2023 | 6,048 | (134) | (2.2) | (226) | 29 | 331 | 148 | (403) | (586) |
| SPR | **2024 (sec)** | 6,317 | (1,786) | (28.3) | (1,121) | 38 | 321 | 152 | (1,311) | (1,480) |

**(dagger) TXT tags no `OperatingIncomeLoss` and presents no GAAP operating income line.** The figure
shown is **total segment profit** from the segment note — a company-defined measure that excludes
non-service pension, the LIFO provision, intangible amortisation, corporate expense and
Manufacturing-group interest. Reconciliation FY2025: segment profit 1,363 - corporate 149 - mfg
interest 108 - LIFO 199 - intangible amortisation 32 = income from continuing operations before tax.
**Not on the same footing as the other rows' OPM%**; it is the closest measure the filer discloses.

**(dd) Embraer** does **not** disclose a share-based-compensation add-back of material size in its IFRS
cash-flow reconciliation (`AdjustmentsForSharebasedPayments` last carries a figure for FY2022:
**US$2.9M**, about 0.04% of revenue). SBC is treated as approximately zero for ERJ. **This flatters
ERJ's owner earnings relative to the US filers by a trivial amount**, and it is a disclosure gap, not
a proven absence.

**(sec) SPR's FY2024 10-K is its LAST 10-K.** It is no longer an SEC reporting company — see
section 4(a).

### 1b. Three-year mean owner earnings, both (c) ends

| Ticker | Window | mean OE(OCF-SBC-capex) | mean OE(OCF-SBC-D&A) | mean revenue | mean OPM% |
|---|---|---:|---:|---:|---:|
| **BA** | FY2023-25 | **(4,426)** | **(4,076)** | 77,925 | (4.1) |
| LMT | FY2023-25 | 5,859 | 5,976 | 71,221 | 10.9 |
| NOC | FY2023-25 | 2,574 | 2,844 | 40,759 | 9.3 |
| RTX | FY2023-25 | 5,520 | 3,758 | 79,420 | 7.9 |
| GD | FY2023-25 | 3,467 | 3,570 | 47,513 | 10.1 |
| TXT | FY2023-25 | 734 | 724 | 14,061 | 9.2 (dagger) |
| TDG | FY2023-25 | 1,486 | 1,345 | 7,785 | 45.3 |
| HEI | FY2023-25 | 602 | 495 | 3,770 | 21.7 |
| ERJ | FY2023-25 | 326 | 538 | 6,414 | 8.1 |
| SPR | FY2022-24 | (756) | (950) | 5,798 | (12.0) |

**(c) is a disclosed judgment.** Neither column is the answer. The capex end is total capex, not
maintenance capex; the D&A end substitutes D&A for maintenance capex. Both ends are shown so the
spread is visible and nothing is hidden inside a single number. The working-capital increment is
already inside OCF as reported. **The spread is largest at RTX** (OE(capex) 5,520 against OE(D&A)
3,758, a 47% gap) because RTX carries roughly $2.0bn/yr of acquisition-accounting intangible
amortisation inside D&A; it is smallest at LMT and GD, where capex is approximately equal to D&A.

---

## 2. AEROSPACE-LEG SEGMENT ROW — revenue, operating profit, margin, backlog

Read off the filings. This is the row that makes the comparison relative rather than notional,
because none of these companies is Boeing-shaped at the consolidated level.

| Company / segment | FY2025 rev | FY2025 op. profit | margin | FY2024 margin | FY2023 margin | FY2025 backlog |
|---|---:|---:|---:|---:|---:|---:|
| **BA — total** | 89,463 | 4,281 | 4.8% | (16.1)% | (1.0)% | **$682.2 bn** |
| LMT — Aeronautics | 30,257 | 2,086 | **6.9%** | 8.8% | 10.3% | $59.4 bn |
| LMT — total | 75,048 | 7,731 | 10.3% | 9.9% | 12.6% | $193.6 bn |
| NOC — Aeronautics Systems | 12,992 | 813 | **6.3%** | 10.0% | (3.7)% | $23.1 bn |
| NOC — total | 41,954 | 4,511 | 10.8% | 10.6% | 6.5% | $95.7 bn |
| RTX — Collins Aerospace | 30,196 | 4,923 | **16.3%** | 14.6% | 14.6% | $42 bn |
| RTX — Pratt & Whitney | 32,916 | 2,596 | **7.9%** | 7.2% | (8.0)% | $151 bn |
| RTX — Raytheon | 28,043 | 3,227 | 11.5% | 9.7% | 9.0% | $75 bn |
| RTX — total (consolidated) | 88,603 | 9,300 | 10.5% | 8.1% | 5.2% | $268 bn |
| GD — Aerospace (Gulfstream) | 13,110 | 1,746 | **13.3%** | 13.0% | 13.7% | $21.8 bn |
| GD — total | 52,550 | 5,356 | 10.2% | 10.1% | 10.0% | $118.0 bn |
| TXT — Textron Aviation | 5,955 | 694 | **11.7%** | 10.7% | 12.1% | $7.7 bn |
| TXT — Bell | 4,282 | 363 | 8.5% | 10.3% | 10.2% | $7.8 bn |
| TXT — total | 14,799 | 1,363 (dagger) | 9.2% (dagger) | 8.8% (dagger) | 9.7% (dagger) | $18.8 bn |
| TDG — Power & Control | 4,559 | 2,595 (EBITDA As Def.) | 56.9% (dm) | 56.8% | — | not disclosed |
| TDG — Airframe | 4,112 | 2,210 (EBITDA As Def.) | 53.7% (dm) | 51.5% | — | not disclosed |
| TDG — total (GAAP op. income) | 8,831 | 4,165 | 47.2% | 44.5% | 44.4% | not disclosed |
| HEI — Flight Support Group | 3,117 | 750 | **24.1%** | 22.5% | — | not disclosed |
| HEI — Electronic Technologies | 1,413 | 325 | 23.0% | 22.8% | — | not disclosed |
| HEI — total | 4,485 | 1,019 | 22.7% | 21.4% | 21.1% | not disclosed |
| ERJ — Commercial Aviation | 2,369.8 | 62.9 | **2.7%** | 2.5% | 1.3% | $14.5 bn |
| ERJ — Executive Aviation | 2,205.1 | 265.4 | 12.0% | 11.7% | 9.0% | $7.6 bn |
| ERJ — Services & Support | 1,925.6 | 298.3 | **15.5%** | 16.5% | 15.2% | $4.9 bn |
| ERJ — Defense & Security | 983.9 | 77.5 | 7.9% | 6.2% | 5.5% | $4.6 bn |
| ERJ — total | 7,577.5 | 607.6 | 8.0% | 10.4% | 6.0% | **$31.6 bn** |
| SPR — Commercial (FY2024) | 4,927.4 | (1,523.1) | **(30.9)%** | 1.6% (FY23) | — | approx. $46.6 bn total |
| SPR — Defense & Space (FY2024) | 975.2 | 94.7 | 9.7% | 5.7% (FY23) | — | — |
| SPR — Aftermarket (FY2024) | 414.0 | 55.3 | 13.4% | 21.4% (FY23) | — | — |
| SPR — total (FY2024) | 6,316.6 | (1,786.1) | (28.3)% | (2.2)% (FY23) | — | approx. $46.6 bn |

**(dm) TDG reports no segment operating income** — only "EBITDA As Defined," a company-defined measure
that excludes D&A, non-cash stock and deferred comp, FX transaction losses and acquisition costs. It
is **not** comparable to the other segment margins in this column. TDG's consolidated GAAP operating
margin (47.2%) is the comparable figure.

**BA's own segment row is left for the run file**, not duplicated here; this file is the *competitor*
row. BA's consolidated line is carried so the peers have something to sit against.

**Backlog / RPO note.** LMT, NOC, RTX, GD, TXT and BA all tag backlog as
`us-gaap:RevenueRemainingPerformanceObligation` and each states in the filing that backlog **is** its
remaining performance obligations — so those six are on one definition. **SPR's approx. $46.6bn is NOT
an RPO**: it is a company estimate "calculated based on Boeing's and Airbus' announced backlog on our
supply agreements ... and the number of units the Company is under contract to produce," and Spirit
states Boeing's B737 MAX contract is a requirements contract Boeing can cut at will. **ERJ's $31.6bn
is a firm-order backlog** on its own definition. **TDG and HEI disclose no backlog figure at all.**
Backlog across this table is therefore *not* one metric; treat the six RPO filers as comparable and
the other three as separate disclosures.

---

## 3. BALANCE SHEET, SHARES, AND THE TEN-YEAR SHARE COUNT

| Ticker | FY | Cash | Short-term inv. | Total debt | Net debt | Equity | Cover shares (latest periodic filing) | Cover as-of |
|---|---|---:|---:|---:|---:|---:|---:|---|
| **BA** | 2025 | 10,921 | 18,479 | **53,848** | 24,448 | 5,454 | **790,370,020** | 10-Q 2026-06-30 |
| LMT | 2025 | 4,121 | — | 21,700 | 17,579 | 6,721 | 230,790,753 | 10-Q 2026-06-28 |
| NOC | 2025 | 4,403 | — | 15,696 | 11,293 | 16,674 | 142,063,026 | 10-Q 2026-06-30 |
| RTX | 2025 | 7,435 | 750 | 37,700 | 29,515 | 65,245 | 1,347,758,144 | 10-Q 2026-06-30 |
| GD | 2025 | 2,333 | — | 8,074 | 5,741 | 25,622 | 270,557,195 | 10-Q 2026-07-05 |
| TXT | 2025 | 2,025 | — | 3,878 (*) | 1,853 | 7,875 | 171,986,917 | 10-Q 2026-07-04 |
| TDG | 2025 | 2,808 | — | **29,291** | 26,483 | **(9,686)** | 55,276,525 | 10-Q 2026-06-27 |
| HEI | 2025 | 218 | — | 2,168 | 1,950 | 4,305 | 55,241,647 Common + 84,515,758 Cl. A (**) | 10-Q 2026-07-31 |
| ERJ | 2025 | 1,949.8 | 964.9 (***) | 2,593.8 | (320.9) | 3,812.0 | **722,766,139** | 20-F cover, 2025-12-31 |
| SPR | 2024 | 537.0 | — | 4,394.2 | 3,857.2 | **(2,621.5)** | 117,266,121 Cl. A | 10-K cover, 2025-01-16 |

(*) TXT: Manufacturing-group debt $3,539M + Finance-group debt $339M. Textron's XBRL carries no
consolidated long-term-debt tag because it reports the two groups separately; figures are off the
filed balance sheet (10-K text lines 588-596, 1307).

(**) HEI's cover is **two classes**. `Screens/cover_shares.py` deliberately refuses to sum them;
whether HEICO's Common and Class A are economically equivalent is a charter judgment, not arithmetic.

(***) ERJ: current financial investments $676.1M + non-current $288.8M. RTX total debt = LTD
noncurrent $34,288M + current $3,412M (the XBRL `LongTermDebt` tag last advanced at FY2024).

### Ten-year diluted weighted-average share count

| Ticker | approx. 10y ago | latest FY | change |
|---|---:|---:|---:|
| **BA** | FY2015 695.0M | FY2025 762.3M | **+9.7%** |
| LMT | FY2015 314.7M | FY2025 233.5M | -25.8% |
| NOC | FY2015 191.6M | FY2025 143.8M | -24.9% |
| RTX | FY2015 883.2M | FY2025 1,356.4M | **+53.6%** (Raytheon merger, 2020) |
| GD | FY2015 326.7M | FY2025 272.4M | -16.6% |
| TXT | FY2016 272.4M | FY2025 180.3M | -33.8% |
| TDG | FY2015 53.1M | FY2025 58.2M | +9.6% |
| HEI | FY2015 84.8M | FY2025 140.8M | **+66.1% — DO NOT USE AS IS** |
| ERJ | 2015-12-31 736,951,304 (20-F cover) | 2025-12-31 722,766,139 | -1.9% |
| SPR | FY2014 141.6M | FY2024 116.8M | -17.5% (last full year as a filer) |

**HEI's +66.1% is not a real issuance.** The FY2015 to FY2016 step (84.8M to 133.1M, 1.57x) is a
split/class artefact, not a share sale: HEICO's cover today carries 55.2M Common + 84.5M Class A =
139.8M, consistent with the FY2025 diluted count, and HEICO has run repeated 5-for-4 splits. Per the
working rule that **market cap is split-invariant**, a share-count *change* read straight off
`WeightedAverageNumberOfDilutedSharesOutstanding` across a split is meaningless. **UNRESEARCHED** if a
clean HEI ten-year dilution figure is needed — the document that would resolve it is the FY2016 10-K's
split disclosure and the split history in Note 1.

---

## 4. NOTES

### (a) Spirit AeroSystems (SPR) — NO LONGER AN SEC REGISTRANT

**SPR has been acquired and deregistered. There is no current row and none is faked here.**

- Not in SEC `company_tickers.json` at all (`sources.cik_for("SPR")` returns `None`);
  `python Screens/cover_shares.py SPR` returns **"NOT AN SEC REGISTRANT in the live ticker file."**
  Submissions JSON for CIK **0001364885** shows `tickers: []`, `exchanges: []`.
- **Form 8-K filed 2025-12-08** (acc `0001104659-25-119096`) — closing.
- **Form 25-NSE filed 2025-12-08** (acc `0000876661-25-000941`) — NYSE notification of removal from
  listing and registration.
- **Form S-8 POS filings 2025-12-08** deregistering the equity plan shares (e.g.
  `0001104659-25-119109`).
- **Form 15-12G filed 2025-12-18** (acc `0001193125-25-324804`) — certification and notice of
  termination of registration / suspension of the duty to file.
- **Last periodic report: 10-Q for the quarter ended 2025-10-02**, filed 2025-10-31, acc
  `0001364885-25-000011`, doc `spr-20251002.htm`.
- **Last 10-K: FY2024, period 2024-12-31**, filed 2025-02-28, acc `0001628280-25-009088`, primary
  doc `spr-20241231.htm`. That is the source of every SPR figure above.
- Effect on the row: Spirit's FY2024 numbers (revenue $6,316.6M, operating loss $(1,786.1)M,
  Commercial segment margin **(30.9)%**, OCF $(1,121)M, total debt $4,394.2M, equity $(2,621.5)M) are
  the **terminal condition of Boeing's largest structures supplier at the point Boeing took it back
  in-house**. They are a historical fact about the supply chain, not a live competitor. From FY2026
  on, Spirit's results sit inside BA and inside Airbus (the Airbus FY2025 release carries -EUR188M of
  Adjustments for "the acquisition and integration of certain Spirit AeroSystems work packages").

### (b) THE AIRBUS LIMIT — stated explicitly

**Airbus SE is not an SEC registrant.** There is no 10-K, no 20-F, no 40-F, no 6-K. It does not appear
in SEC `company_tickers.json` under any spelling (searched "AIRBUS"; zero hits — the only non-US
aerospace hit in that file is Embraer, ticker `EMBJ`, CIK 1355444). Its US ADR **EADSY is unsponsored**,
which is precisely why there is no filing: an unsponsored ADR is created by a depositary bank without
the issuer's participation and triggers no issuer reporting obligation. **No SEC filing for Airbus was
invented, and none exists to cite.**

What IS reachable, and at what rung:

> **Rung: company IR site (English) — one rung below a primary SEC filing.**
> Fetched 2026-09-12. Airbus publishes under IFRS in **EUR**, on a different accounting and
> presentational basis from the US filers above, and its headline profit measure (**EBIT Adjusted**)
> is an explicitly company-defined alternative performance measure.

**FY2025 (released 19 February 2026).** Source:
`https://www.airbus.com/sites/g/files/jlcbta136/files/2026-02/press-release-airbus-fy2025-results_hm0612.pdf`
(saved locally as `AIRBUS_FY2025_press_release.pdf` / `.txt`)

| Metric | FY2025 | FY2024 |
|---|---:|---:|
| Commercial aircraft delivered | **793** (93 A220, 607 A320 Family, 36 A330, 57 A350) | 766 |
| Commercial aircraft gross / net orders | 1,000 / **889** | 878 / 826 |
| Commercial aircraft order backlog (units) | **8,754** | 8,658 |
| Revenues (EUR m) | **73,420** (thereof defence 14,244) | 69,230 |
| — Airbus (commercial aircraft) | 52,577 | 50,646 |
| — Airbus Helicopters | 8,972 | 7,941 |
| — Airbus Defence and Space | 13,405 | 12,082 |
| **EBIT Adjusted (EUR m)** | **7,128** | 5,354 |
| — Airbus (commercial aircraft) | 5,470 | 5,093 |
| — Airbus Helicopters | 925 | 818 |
| — Airbus Defence and Space | 798 | (566) |
| EBIT reported (EUR m) | 6,082 | 5,304 |
| Net income (EUR m) / EPS (EUR) | 5,221 / 6.61 | 4,232 / 5.36 |
| FCF before customer financing (EUR m) | 4,574 | 4,463 |
| Order book, value (EUR m) | 618,824 (thereof defence 61,395) | 628,917 |
| Gross cash position (EUR m) | 27,218 | 26,864 |
| **Net cash position (EUR m)** | **12,171** | 11,753 |
| Employees | 165,294 | 156,921 |

**FY2025 cash-flow items, same construction as the peer table** — source:
`https://www.airbus.com/sites/g/files/jlcbta136/files/2026-02/airbus_fy_2025_financial_statements_1.pdf`
(saved as `AIRBUS_FY2025_financial_statements.pdf` / `.txt`), IFRS Consolidated Statement of Cash
Flows and Notes 32 / 36:

| Item (EUR m) | FY2025 | FY2024 |
|---|---:|---:|
| Cash provided by operating activities | **7,995** | 7,402 |
| Purchases of intangibles, PP&E, investment property | **(3,964)** | (3,669) |
| Depreciation and amortisation | **3,133** | 2,853 |
| IFRS 2 share-based payment (equity statement credit) | 310 | — |
| — of which LTI equity-settled compensation expense (Note 32) | 106 | 66 |
| Short-term financing liabilities | (5,186) | (3,924) |
| Long-term financing liabilities | (9,063) | (10,355) |
| Shares issued at period end / treasury | 792,283,683 / (5,055,938) | 792,283,683 / — |

On the peer table's own arithmetic: **OE(OCF-SBC-capex) = 7,995 - 310 - 3,964 = EUR 3,721M**;
**OE(OCF-SBC-D&A) = 7,995 - 310 - 3,133 = EUR 4,552M**. **These are EUR, not USD, and the currency is
not converted here** — operator rule 5 requires the sovereign for the *earnings currency*, so any
Airbus valuation runs against the EUR curve, not the USD one. The figures are placed here for scale
comparison only.

**H1 2026 (released 29 July 2026).** Source:
`https://www.airbus.com/en/newsroom/press-releases/2026-07-airbus-reports-half-year-h1-2026-results`
— 351 commercial aircraft delivered; 821 net commercial orders; revenues EUR 33.2bn (+12% y/y);
EBIT Adjusted EUR 2,727M; EBIT reported EUR 2,745M; net income EUR 2,243M; FCF before customer
financing EUR (1,166)M; net cash EUR 8.36bn at 2026-06-30; commercial backlog 9,222 aircraft.

**The obstacle that remains, named.** Airbus's IR HTML pages render their headline tables as images or
JS-loaded widgets; `https://www.airbus.com/en/investors` and
`https://www.airbus.com/en/investors/financial-results` returned document links and almost no figures.
Every number above came from the **PDFs**, fetched with `curl` and parsed with `pymupdf`. A future run
should go straight to the PDF.

### (c) WHICH PEERS ARE AND ARE NOT COMPARABLE TO WHICH BOEING SEGMENT

**Boeing Commercial Airplanes (BCA) — large commercial aircraft OEM.**

- **Comparable, and the only one: Airbus (commercial aircraft division).** A duopoly of two. Airbus is
  *not an SEC filer*, so **the single most important competitor row in this run cannot be built from
  primary SEC filings at all.** That is a structural limit on Q2 for Boeing, and it is not fixable by
  working harder inside EDGAR.
- **Partly comparable: Embraer Commercial Aviation** ($2,370M revenue, **2.7%** FY2025 op. margin).
  Different size class (E-Jet E2, 76-146 seats) and it does not compete for A320/737 orders; it is the
  nearest thing to a third commercial-jet OEM and files a **20-F**, so it is on primary filings.
- **Not comparable: every US defence prime in this file.** LMT Aeronautics, NOC Aeronautics Systems and
  RTX Raytheon sell to governments on cost-type and fixed-price development contracts with progress
  payments; BCA sells to airlines and lessors on fixed-price contracts with delivery payments. Their
  revenue is appropriated, not ordered.

**Boeing Defense, Space & Security (BDS).**

- **Directly comparable: LMT (whole company), NOC (whole company), GD's defence segments, RTX Raytheon,
  Textron Systems + Bell.** Same customer, same contract accounting (percentage-of-completion,
  cumulative catch-up, forward losses, EAC adjustments), same backlog definition (RPO).
- The closest single read on BDS is **LMT Aeronautics (6.9%) and NOC Aeronautics Systems (6.3%)** — both
  *military aircraft* primes, and note both took reach-forward losses in FY2025 (LMT $950M on a
  classified Aeronautics program plus $140M on C-130; NOC $477M on B-21 LRIP). Fixed-price development
  losses are an **industry-wide** pattern, not a Boeing-only one.

**Boeing Global Services (BGS) — aftermarket / parts / MRO.**

- **Comparable on economics: TDG (47.2% GAAP operating margin; commercial and non-aero aftermarket
  $2,804M of $8,831M), HEI Flight Support Group (24.1%), RTX Collins Aerospace (16.3%), ERJ Services &
  Support (15.5%).** These are the four cleanest aftermarket reads in the file and they bracket a wide
  range.
- **Caution on TDG:** it is a proprietary-part aftermarket at 47% operating margins financed with
  **$29.3bn of debt against $(9.7)bn of equity**. Its margin is not evidence about aftermarket
  economics generally; it is evidence about sole-source proprietary parts specifically.
- **Not comparable: GD Aerospace (Gulfstream).** 13.3% margin, but it is a *business-jet OEM plus its
  own service network* — a different customer (corporate / UHNW), different cycle, different backlog
  mechanics (deposits on definitive purchase contracts). Same with **Textron Aviation** (11.7%;
  Citation jets and commercial turboprops).

**Boeing's supply chain, not its competition.**

- **SPR** was Boeing's fuselage supplier, not its competitor, and is now inside Boeing — section 4(a).
- **RTX Pratt & Whitney (7.9% margin, $151bn backlog)** is a *supplier* to Airbus and to the narrowbody
  market, and the Airbus FY2025 release names "Pratt & Whitney's failure to commit to the number of
  engines ordered by Airbus" as the reason Airbus cut its A320 ramp guidance to rate 70-75/month by
  end-2027. P&W is therefore a constraint on **Airbus**, i.e. on Boeing's only real competitor —
  relevant to Q2 as a fact about the rival's supply chain, not as a comparable.
- GE Aerospace and Safran (CFM, the 737 MAX engine) are **not in this file.** GE Aerospace is an SEC
  filer and is **UNRESEARCHED** here; Safran is not an SEC filer.

**What this table does not settle, and cannot.** Revenue and margin comparisons across BCA and the
defence primes are comparisons of *different contract accounting*, and BA's FY2023-25 owner-earnings
mean of **$(4,426)M to $(4,076)M** against a peer group that is uniformly positive is a fact about a
three-year window containing the 2024 door-plug grounding, the IAM strike and the Spirit
re-acquisition. Whether that is cyclical or structural is a **Q2 and Q4 judgment**, made in the run
file with a ledger id — **not here.**

---

## 5. SOURCES

### Annual filings used (primary document; every figure in sections 1 and 2 traces here)

| Ticker | Form | Period | Filed | Accession | Primary doc |
|---|---|---|---|---|---|
| BA | 10-K | 2025-12-31 | 2026-01-30 | `0001628280-26-004357` | `ba-20251231.htm` |
| BA | 10-K | 2024-12-31 | 2025-02-03 | `0000012927-25-000015` | `ba-20241231.htm` |
| LMT | 10-K | 2025-12-31 | 2026-01-29 | `0001628280-26-004195` | `lmt-20251231.htm` |
| NOC | 10-K | 2025-12-31 | 2026-01-27 | `0001133421-26-000003` | `noc-20251231.htm` |
| RTX | 10-K | 2025-12-31 | 2026-02-06 | `0000101829-26-000006` | `rtx-20251231.htm` |
| GD | 10-K | 2025-12-31 | 2026-01-30 | `0000040533-26-000006` | `gd-20251231.htm` |
| TXT | 10-K | 2026-01-03 | 2026-02-11 | `0000217346-26-000006` | `txt-20260103.htm` |
| TDG | 10-K | 2025-09-30 | 2025-11-12 | `0001260221-25-000081` | `tdg-20250930.htm` |
| HEI | 10-K | 2025-10-31 | 2025-12-22 | `0000046619-25-000082` | `hei-20251031.htm` |
| ERJ | 20-F | 2025-12-31 | 2026-03-30 | `0001628280-26-021824` | `erj-20251231.htm` |
| ERJ | 20-F | 2015-12-31 | 2016-03-29 | `0001193125-16-519982` | `d139269d20f.htm` (10y cover shares) |
| SPR | 10-K | 2024-12-31 | 2025-02-28 | `0001628280-25-009088` | `spr-20241231.htm` (**last 10-K**) |

Each of these was **downloaded and read** (text renditions on disk in this folder), not taken on XBRL
alone. Consolidated revenue and operating profit were cross-checked filing-against-XBRL for all ten
names and agreed in every case: HEI $4,485,044 thousand = XBRL $4,485.0M; ERJ $7,577.5M = XBRL
$7,578M; GD operating earnings $5,356M both ways; TDG net sales $8,831M both ways; LMT total sales
$75,048M both ways; RTX consolidated $88,603M both ways; TXT revenues $14,799M both ways; SPR
$6,316.6M = XBRL $6,317M.

### Backlog / RPO, tagged with accession

| Ticker | FY2025 RPO | Accession |
|---|---:|---|
| BA | $682,207M | `0001628280-26-004357` |
| LMT | $193,600M | `0001628280-26-004195` |
| NOC | $95,681M | `0001133421-26-000003` |
| RTX | $268,000M | `0000101829-26-000006` |
| GD | $118,000M | `0000040533-26-000006` |
| TXT | $18,823M (FY end 2026-01-03) | `0000217346-26-000006` |
| TDG, HEI | **no backlog tag, no backlog figure disclosed** | — |
| ERJ | $31,642.3M firm order backlog (own definition) | `0001628280-26-021824` |
| SPR | approx. $46,600M company estimate, **not RPO** (FY2024) | `0001628280-25-009088` |

Prior-year RPO, same tag, for the trend: BA 521,336 (FY2024) / 520,195 (FY2023); LMT 176,000 /
160,600; NOC 91,468 / 84,200; RTX 218,000 / 196,000; GD 90,597 / 93,600; TXT 17,908 / 13,900.

### Cover share counts (`python Screens/cover_shares.py TICKER`)

| Ticker | Form | Period | Accession | Count |
|---|---|---|---|---|
| BA | 10-Q | 2026-06-30 | `0001628280-26-050038` | 790,370,020 |
| LMT | 10-Q | 2026-06-28 | `0001628280-26-049411` | 230,790,753 |
| NOC | 10-Q | 2026-06-30 | `0001133421-26-000034` | 142,063,026 |
| RTX | 10-Q | 2026-06-30 | `0000101829-26-000027` | 1,347,758,144 |
| GD | 10-Q | 2026-07-05 | `0000040533-26-000032` | 270,557,195 |
| TXT | 10-Q | 2026-07-04 | `0000217346-26-000036` | 171,986,917 |
| TDG | 10-Q | 2026-06-27 | `0001260221-26-000053` | 55,276,525 |
| HEI | 10-Q | 2026-07-31 | `0000046619-26-000020` | 55,241,647 Common + 84,515,758 Class A (**not summed**) |
| ERJ | 20-F cover | 2025-12-31 | `0001628280-26-021824` | 722,766,139 |
| SPR | 10-K cover | 2025-01-16 | `0001628280-25-009088` | 117,266,121 Class A |

### Airbus (rung: company IR site, English — NOT an SEC filing), all fetched 2026-09-12

- `https://www.airbus.com/en/investors` — index only; headline figures not in the HTML text.
- `https://www.airbus.com/en/investors/financial-results` — document links only.
- `https://www.airbus.com/sites/g/files/jlcbta136/files/2026-02/press-release-airbus-fy2025-results_hm0612.pdf`
  — FY2025 press release, dated 19 February 2026. **All section 4(b) FY2025/FY2024 headline figures.**
- `https://www.airbus.com/sites/g/files/jlcbta136/files/2026-02/airbus_fy_2025_financial_statements_1.pdf`
  — Airbus SE IFRS Consolidated Financial Statements 2025, 121 pp. **Cash flow, Note 32 (share-based
  payment), Note 36 (net cash), issued shares.**
- `https://www.airbus.com/en/newsroom/press-releases/2026-07-airbus-reports-half-year-h1-2026-results`
  — H1 2026 press release, dated 29 July 2026.

### Scripts and artefacts in this folder

`pull.py` (XBRL series, all peers) - `fetch.py` (filing downloads) - `compute.py` (owner earnings, both
(c) ends) - `xbrl_raw.json` - `shares_history.json` - `computed.json` -
`LMT_10K_FY2025.txt`, `NOC_10K_FY2025.txt`, `RTX_10K_FY2025.txt`, `GD_10K_FY2025.txt`,
`TXT_10K_FY2025.txt`, `TDG_10K_FY2025.txt`, `HEI_10K_FY2025.txt` - `SPR_10K_FY2024.txt` -
`ERJ_20F_FY2025.txt` - `AIRBUS_FY2025_press_release.pdf` / `.txt` -
`AIRBUS_FY2025_financial_statements.pdf` / `.txt`

### Open items flagged UNRESEARCHED (documents nameable, so not UNKNOWABLE)

1. **GE Aerospace** — SEC filer, the 737 MAX engine supplier through CFM, absent from this file.
   Document: GE Aerospace FY2025 10-K.
2. **Safran** — CFM's other half; not an SEC filer. Document: Safran FY2025 Universal Registration
   Document (company IR site rung, same as Airbus).
3. **HEI clean ten-year dilution** — document: HEI FY2016 10-K split disclosure and Note 1 split
   history.
4. **Airbus maintenance-capex split** — Airbus reports one line for intangibles + PP&E + investment
   property, so the (c) judgment cannot be narrowed from the press release. Document: Airbus FY2025
   Financial Statements Note 20 detail (already on disk, unread for this purpose).
5. **ERJ share-based compensation** — the IFRS cash-flow add-back stops after FY2022. Document: ERJ
   FY2025 20-F Note on share-based payment / employee benefits.
