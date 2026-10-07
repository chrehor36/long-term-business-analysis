# UAL PHYSICAL UNITS SERIES, 2017-2025
### The [E4-55] test: where units exist, monitor units

**Compiled** 2026-09-02. **Scope:** United Airlines Holdings, Inc. (UAL), CIK 0000100517,
fiscal years 2017 through 2025, plus peer PRASM/yield for Delta, American, Southwest and
Alaska.

**No verdict is drawn in this file.** It is a series and its provenance. Anything that looks
like a conclusion is a caveat about a definition, not a judgment.

---

## 0. SOURCES OF RECORD

### UAL 10-K filings used

| Fiscal year(s) taken | Filing date | Accession number | Primary document | Years shown in the table |
|---|---|---|---|---|
| 2017, 2018, 2019 | 2020-02-25 | 0000100517-20-000010 | `ual201910k.htm` | 2019, 2018, 2017, 2016, 2015 |
| 2020, 2021 | 2022-02-18 | 0000100517-22-000009 | `ual-20211231.htm` | 2021, 2020, 2019 |
| 2022 | 2024-02-29 | 0000100517-24-000027 | `ual-20231231.htm` | 2023, 2022, 2021 |
| 2023, 2024, 2025 | 2026-02-12 | 0000100517-26-000023 | `ual-20251231.htm` | 2025, 2024, 2023 |

Supplementary, for fuel / fleet / headcount where the four above are silent:

| Purpose | Filing date | Accession number | Primary document |
|---|---|---|---|
| FY2018 detail | 2019-02-28 | 0000100517-19-000009 | `ual_201810k.htm` |
| FY2020 detail | 2021-03-01 | 0000100517-21-000016 | `ual-20201231.htm` |

Base URL pattern: `https://www.sec.gov/Archives/edgar/data/100517/{accession-no-dashes}/{document}`

**Overlap cross-checks (the same year read out of two different filings):**
- 2019 ASMs: 284,999 m in the FY2019 10-K and 284,999 m in the FY2021 10-K. Agree.
- 2019 PRASM: 13.90c in both. Agree.
- 2021 PRASM: 11.30c in the FY2021 10-K and 11.30c in the FY2023 10-K. Agree.
- 2023 PRASM: 16.84c in the FY2023 10-K and 16.84c in the FY2025 10-K. Agree.
- 2023 ASMs: 291,333 m in both. Agree.
- 2019 fuel: 4,292 m gallons at $2.09 in the FY2019, FY2020 and FY2021 10-Ks. Agree.
- 2023 fuel: 4,205 m gallons at $3.01 in the FY2023 fuel table and the FY2025 stats table. Agree.

No restatement of the operating statistics was found across the overlap windows.

### CPI-U

**Primary, from the issuing authority.** Bureau of Labor Statistics, series **CUUR0000SA0**
("All items in U.S. city average, all urban consumers, not seasonally adjusted"), the **M13
annual-average** period. Taken from the BLS public time-series flat file
`https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems`, retrieved 2026-09-02.

The BLS public API v1 (`api.bls.gov/publicAPI/v1/...`) was tried first but, without a
registration key, returns only the three most recent years, so it could not span 2017-2025.
The flat file is the same authority and covers the whole window.

**Cross-check, not the source.** FRED `CPIAUCNS` (a St. Louis Fed redistribution of the same
BLS series), annual mean of the twelve monthly observations, downloaded 2026-09-02. It
reproduces the BLS annual averages to within rounding at every year 2017-2025:

| Year | BLS M13 | FRED CPIAUCNS 12-month mean |
|---|---|---|
| 2017 | 245.120 | 245.1196 |
| 2018 | 251.107 | 251.1068 |
| 2019 | 255.657 | 255.6574 |
| 2020 | 258.811 | 258.8112 |
| 2021 | 270.970 | 270.9698 |
| 2022 | 292.655 | 292.6549 |
| 2023 | 304.702 | 304.7016 |
| 2024 | 313.689 | 313.6888 |
| 2025 | 321.943 | 321.943 |

---

## 1. UAL OPERATING STATISTICS, NOMINAL, AS FILED

All figures as reported in the "Operating Statistics" / "Select operating statistics" table
of the 10-K MD&A for the year shown. Cents are cents per mile. ASMs and RPMs in millions.

| Year | ASMs (m) | RPMs (m) | Load factor % | PRASM (c) | TRASM (c) | Yield (c) | CASM (c) |
|---|---|---|---|---|---|---|---|
| 2017 | 262,386 | 216,261 | 82.4 | 13.13 | 14.40 | 15.93 | 13.02 |
| 2018 | 275,262 | 230,155 | 83.6 | 13.70 | 15.00 | 16.38 | 13.83 |
| 2019 | 284,999 | 239,360 | 84.0 | 13.90 | 15.18 | 16.55 | 13.67 |
| 2020 | 122,804 | 73,883 | 60.2 | 9.61 | 12.50 | 15.98 | 17.68 |
| 2021 | 178,684 | 128,979 | 72.2 | 11.30 | 13.79 | 15.66 | 14.36 |
| 2022 | 247,858 | 206,791 | 83.4 | 16.15 | 18.14 | 19.36 | 17.19 |
| 2023 | 291,333 | 244,435 | 83.9 | 16.84 | 18.44 | 20.07 | 16.99 |
| 2024 | 311,185 | 258,503 | 83.1 | 16.66 | 18.34 | 20.05 | 16.70 |
| 2025 | 330,284 | 271,619 | 82.2 | 16.18 | 17.88 | 19.67 | 16.46 |

Definitions, verbatim from the FY2025 10-K footnotes: RPMs are "the number of scheduled miles
flown by revenue passengers"; ASMs are "the number of seats available for passengers
multiplied by the number of scheduled miles those seats are flown"; passenger load factor is
"RPMs divided by ASMs"; yield is "the average passenger revenue received for each revenue
passenger mile flown."

### Passengers and cargo, same source

| Year | Passengers (000) | Cargo revenue ton miles (m) | Average stage length (mi) |
|---|---|---|---|
| 2017 | 148,067 | 3,316 | 1,460 |
| 2018 | 158,330 | 3,425 | 1,446 |
| 2019 | 162,443 | 3,329 | 1,460 |
| 2020 | 57,761 | 2,711 | 1,307 |
| 2021 | 104,082 | 3,285 | 1,315 |
| 2022 | 144,300 | 3,041 | 1,437 |
| 2023 | 164,927 | 3,159 | 1,479 |
| 2024 | 173,603 | 3,604 | 1,490 |
| 2025 | 181,053 | 3,626 | 1,488 |

### Physical volume, indexed

| Year | ASMs idx 2017=100 | RPMs idx 2017=100 |
|---|---|---|
| 2017 | 100.0 | 100.0 |
| 2018 | 104.9 | 106.4 |
| 2019 | 108.6 | 110.7 |
| 2020 | 46.8 | 34.2 |
| 2021 | 68.1 | 59.6 |
| 2022 | 94.5 | 95.6 |
| 2023 | 111.0 | 113.0 |
| 2024 | 118.6 | 119.5 |
| 2025 | 125.9 | 125.6 |

ASMs 2017 to 2025: +25.9%. RPMs 2017 to 2025: +25.6%.
ASMs 2019 to 2025: +15.9%. RPMs 2019 to 2025: +13.5%.

---

## 2. THE DEFLATED SERIES (CPI-U, 2025 = 100)

Deflator applied: `real = nominal x (CPI-U 2025 / CPI-U year)`.

| Year | CPI-U annual avg | Index (2025 = 100) | Deflator multiplier |
|---|---|---|---|
| 2017 | 245.120 | 76.1377 | 1.31341 |
| 2018 | 251.107 | 77.9973 | 1.28209 |
| 2019 | 255.657 | 79.4106 | 1.25928 |
| 2020 | 258.811 | 80.3903 | 1.24393 |
| 2021 | 270.970 | 84.1671 | 1.18811 |
| 2022 | 292.655 | 90.9027 | 1.10008 |
| 2023 | 304.702 | 94.6447 | 1.05658 |
| 2024 | 313.689 | 97.4362 | 1.02631 |
| 2025 | 321.943 | 100.0000 | 1.00000 |

### PRASM, nominal versus real

| Year | Nominal (c) | YoY nominal | Real (2025 c) | YoY real |
|---|---|---|---|---|
| 2017 | 13.13 |  | 17.25 |  |
| 2018 | 13.70 | +4.3% | 17.56 | +1.9% |
| 2019 | 13.90 | +1.5% | 17.50 | -0.3% |
| 2020 | 9.61 | -30.9% | 11.95 | -31.7% |
| 2021 | 11.30 | +17.6% | 13.43 | +12.3% |
| 2022 | 16.15 | +42.9% | 17.77 | +32.3% |
| 2023 | 16.84 | +4.3% | 17.79 | +0.1% |
| 2024 | 16.66 | -1.1% | 17.10 | -3.9% |
| 2025 | 16.18 | -2.9% | 16.18 | -5.4% |

**2017 to 2025: nominal +23.2% (13.13 to 16.18). Real -6.2% (17.25 to 16.18 in 2025 cents).**
2019 to 2025: nominal +16.4%. Real -7.6% (17.50 to 16.18).

### TRASM, nominal versus real

| Year | Nominal (c) | YoY nominal | Real (2025 c) | YoY real |
|---|---|---|---|---|
| 2017 | 14.40 |  | 18.91 |  |
| 2018 | 15.00 | +4.2% | 19.23 | +1.7% |
| 2019 | 15.18 | +1.2% | 19.12 | -0.6% |
| 2020 | 12.50 | -17.7% | 15.55 | -18.7% |
| 2021 | 13.79 | +10.3% | 16.38 | +5.4% |
| 2022 | 18.14 | +31.5% | 19.96 | +21.8% |
| 2023 | 18.44 | +1.7% | 19.48 | -2.4% |
| 2024 | 18.34 | -0.5% | 18.82 | -3.4% |
| 2025 | 17.88 | -2.5% | 17.88 | -5.0% |

**2017 to 2025: nominal +24.2%. Real -5.5% (18.91 to 17.88).**
2019 to 2025: nominal +17.8%. Real -6.5% (19.12 to 17.88).

### Yield (passenger revenue per RPM), nominal versus real

| Year | Nominal (c) | YoY nominal | Real (2025 c) | YoY real |
|---|---|---|---|---|
| 2017 | 15.93 |  | 20.92 |  |
| 2018 | 16.38 | +2.8% | 21.00 | +0.4% |
| 2019 | 16.55 | +1.0% | 20.84 | -0.8% |
| 2020 | 15.98 | -3.4% | 19.88 | -4.6% |
| 2021 | 15.66 | -2.0% | 18.61 | -6.4% |
| 2022 | 19.36 | +23.6% | 21.30 | +14.5% |
| 2023 | 20.07 | +3.7% | 21.21 | -0.4% |
| 2024 | 20.05 | -0.1% | 20.58 | -3.0% |
| 2025 | 19.67 | -1.9% | 19.67 | -4.4% |

**2017 to 2025: nominal +23.5%. Real -6.0% (20.92 to 19.67).**
2019 to 2025: nominal +18.9%. Real -5.6% (20.84 to 19.67).

### CASM, nominal versus real (cost side, for symmetry)

| Year | Nominal CASM (c) | Real CASM (2025 c) |
|---|---|---|
| 2017 | 13.02 | 17.10 |
| 2018 | 13.83 | 17.73 |
| 2019 | 13.67 | 17.21 |
| 2020 | 17.68 | 21.99 |
| 2021 | 14.36 | 17.06 |
| 2022 | 17.19 | 18.91 |
| 2023 | 16.99 | 17.95 |
| 2024 | 16.70 | 17.14 |
| 2025 | 16.46 | 16.46 |

CASM 2017 to 2025: nominal +26.4%. Real -3.7%.

### Implied real passenger revenue (real PRASM x ASMs)

An arithmetic derivation, not a filed line. It separates the price effect from the volume
effect: the units grew, the real unit revenue fell.

| Year | Real PRASM (2025 c) | ASMs (m) | Implied real passenger revenue ($m, 2025 dollars) | idx 2017=100 |
|---|---|---|---|---|
| 2017 | 17.25 | 262,386 | 45,249 | 100.0 |
| 2018 | 17.56 | 275,262 | 48,349 | 106.9 |
| 2019 | 17.50 | 284,999 | 49,886 | 110.2 |
| 2020 | 11.95 | 122,804 | 14,680 | 32.4 |
| 2021 | 13.43 | 178,684 | 23,990 | 53.0 |
| 2022 | 17.77 | 247,858 | 44,035 | 97.3 |
| 2023 | 17.79 | 291,333 | 51,836 | 114.6 |
| 2024 | 17.10 | 311,185 | 53,208 | 117.6 |
| 2025 | 16.18 | 330,284 | 53,440 | 118.1 |

---

## 3. FUEL, HEADCOUNT, FLEET, CASM-EX

### Fuel

Gallons and average price per gallon (including fuel taxes). For 2020-2022 the operating
statistics table omits fuel, so the figures come from the "Aircraft fuel" expense table in
the same 10-K MD&A, which gives gallons consumed, fuel expense and average price per gallon.

| Year | Fuel gallons (m) | Avg price / gal ($) | Fuel expense ($m) | ASMs per gallon | Source filing |
|---|---|---|---|---|---|
| 2017 | 3,978 | 1.74 | 6,913 | 65.96 | FY2020 10-K stats table (0000100517-21-000016); fuel expense from FY2017 10-K |
| 2018 | 4,137 | 2.25 | 9,307 | 66.54 | FY2020 10-K stats table; FY2020 10-K fuel table |
| 2019 | 4,292 | 2.09 | 8,953 | 66.40 | FY2019 and FY2020 10-K |
| 2020 | 2,004 | 1.57 | 3,153 | 61.28 | FY2020 / FY2021 10-K fuel table |
| 2021 | 2,729 | 2.11 | 5,755 | 65.48 | FY2021 / FY2023 10-K fuel table |
| 2022 | 3,608 | 3.63 | 13,113 | 68.70 | FY2023 10-K fuel table (0000100517-24-000027) |
| 2023 | 4,205 | 3.01 | 12,651 | 69.28 | FY2023 fuel table; FY2025 10-K stats table |
| 2024 | 4,444 | 2.65 | n/d in FY2025 stats table | 70.02 | FY2025 10-K (0000100517-26-000023) |
| 2025 | 4,663 | 2.44 | n/d in FY2025 stats table | 70.83 | FY2025 10-K |

"ASMs per gallon" is a derived ratio (ASMs divided by gallons), not a filed line.

**Caveat.** The 2017 fuel-price figure of $1.74 is the average price per gallon *after* fuel
hedge impacts as presented in the FY2017 and FY2020 10-Ks. The FY2017 10-K separately shows
total aircraft fuel purchase cost excluding hedge impacts also at $1.74 for 2017 (hedge losses
in 2017 rounded to zero cents per gallon); for 2016 the two differ ($1.43 excluding hedges vs
$1.49 including). Only 2017 onward is used here, so the distinction does not bind the series.

### Employees

**UAL does not disclose an average full-time-equivalent employee count in its 10-K.** The
filings give **year-end headcount** only, and describe changes in average FTEs in narrative
percentage terms (for example the FY2019 10-K: "a 4.0% increase in average full-time
equivalent employees"). The requested "average FTE employees" line therefore does not exist
in the source for UAL. Delta, American, Southwest and Alaska do disclose an FTE count; see
section 5 for the definitional mismatch.

| Year | UAL employee headcount at Dec 31 | Source |
|---|---|---|
| 2017 | 89,800 | FY2020 10-K stats table (shown as 89.8 thousand) |
| 2018 | 91,700 | FY2020 10-K stats table (91.7 thousand) |
| 2019 | 95,900 | FY2020, FY2021, FY2022 10-Ks |
| 2020 | 74,400 | FY2020, FY2021, FY2022 10-Ks |
| 2021 | 84,100 | FY2021, FY2022, FY2023 10-Ks |
| 2022 | 92,800 | FY2022, FY2023 10-Ks |
| 2023 | 103,300 | FY2023, FY2025 10-Ks |
| 2024 | 107,300 | FY2025 10-K |
| 2025 | 113,200 | FY2025 10-K |

Derived: ASMs per employee (thousands), not a filed line.

| Year | ASMs (m) | Headcount | ASMs per employee (000) |
|---|---|---|---|
| 2017 | 262,386 | 89,800 | 2,922 |
| 2018 | 275,262 | 91,700 | 3,002 |
| 2019 | 284,999 | 95,900 | 2,972 |
| 2020 | 122,804 | 74,400 | 1,651 |
| 2021 | 178,684 | 84,100 | 2,125 |
| 2022 | 247,858 | 92,800 | 2,671 |
| 2023 | 291,333 | 103,300 | 2,820 |
| 2024 | 311,185 | 107,300 | 2,900 |
| 2025 | 330,284 | 113,200 | 2,918 |

### Fleet at year end

From the aircraft tables in Item 2 (Properties) of each year's own 10-K. Nine separate
filings were read, because each 10-K shows only its own year-end fleet.

| Year | Mainline | Regional | Total | Source accession |
|---|---|---|---|---|
| 2017 | 744 | 518 | 1,262 | 0001193125-18-054235 (filed 2018-02-22) |
| 2018 | 770 | 559 | 1,329 | 0000100517-19-000009 (filed 2019-02-28) |
| 2019 | 777 | 581 | 1,358 | 0000100517-20-000010 (filed 2020-02-25) |
| 2020 | 812 | 475 | 1,287 | 0000100517-21-000016 (filed 2021-03-01) |
| 2021 | 826 | 518 | 1,344 | 0000100517-22-000009 (filed 2022-02-18) |
| 2022 | 868 | 470 | 1,338 | 0000100517-23-000048 (filed 2023-02-16) |
| 2023 | 945 | 413 | 1,358 | 0000100517-24-000027 (filed 2024-02-29) |
| 2024 | 994 | 412 | 1,406 | 0000100517-25-000046 (filed 2025-02-27) |
| 2025 | 1,066 | 424 | 1,490 | 0000100517-26-000023 (filed 2026-02-12) |

Mainline 2017 to 2025: +322 aircraft, +43.3%. Regional: -94 aircraft, -18.1%. Total: +228,
+18.1%. Derived ratio, not a filed line: ASMs per total aircraft rose from 207.9m in 2017 to
221.7m in 2025 (+6.6%); the mainline/regional mix shift is the reason the ASM count grew
faster than the aircraft count.

**Caveat on the fleet count.** Each filing footnotes additional aircraft not in the table
(temporarily grounded, held for sale, subleased to third parties, or owned regional aircraft
not in operation). The counts above are the "Total mainline" and "Total regional" lines as
printed and are not adjusted for those footnoted extras. The 2017 and 2018 tables also present
a "Capacity Purchase Agreement" column structure that later filings dropped; the total lines
are still directly comparable.

### CASM-ex

**UAL discloses CASM-ex in only two of the nine 10-Ks.** It appears in the FY2021 filing (for
2019 alone) and in the FY2022 filing (for 2019, 2020, 2021 and 2022). It does not appear at
all in the FY2017, FY2018, FY2019, FY2020, FY2023, FY2024 or FY2025 10-Ks. The measure is
carried in UAL's quarterly earnings releases furnished on Form 8-K, which were not read for
this file (the instruction was 10-K sourced).

| Year | CASM (GAAP) | Fuel | Profit sharing | Third-party business exp. | Special charges (credits) | CASM-ex |
|---|---|---|---|---|---|---|
| 2019 | 13.67 | 3.14 | 0.17 | 0.06 | 0.09 | **10.21** |
| 2020 | 17.68 | 2.57 | - | 0.11 | (2.13) | **17.13** |
| 2021 | 14.36 | 3.22 | - | 0.06 | (1.88) | **12.96** |
| 2022 | 17.19 | 5.29 | 0.06 | 0.06 | 0.05 | **11.73** |

Source: FY2022 10-K, accession 0000100517-23-000048, filed 2023-02-16, "Supplemental
Information" non-GAAP reconciliation, in cents. Verbatim definition from the same filings:
CASM-ex is "a non-GAAP financial measure defined as cost or operating expense per available
seat mile ('CASM') excluding fuel, profit sharing, third-party business expense and special
charges."

**2017, 2018, 2023, 2024 and 2025 CASM-ex are NOT AVAILABLE from the 10-K.** They are not
computed here; a reconstruction would require reading fuel, profit sharing, third-party
business expense and special charges out of the income statement and notes for each year,
which is a different exercise from transcribing a disclosed figure.

Real (2025 cents) CASM-ex over the four disclosed years, for reference: 2019 = 12.86,
2020 = 21.31, 2021 = 15.40, 2022 = 12.90.

---

## 4. PEER COMPARISON

Same metric, same window, same deflator. Delta and American are the two nearest peers;
Southwest and Alaska are included as requested and are less comparable (see caveats).

### Sources

| Carrier | CIK | Filing date | Accession number | Primary document | Years taken |
|---|---|---|---|---|---|
| Delta (DAL) | 0000027904 | 2020-02-13 | 0000027904-20-000004 | `dal-20191231.htm` | 2019 (and 2015-2018) |
| Delta (DAL) | 0000027904 | 2024-02-12 | 0000027904-24-000003 | `dal-20231231.htm` | 2023, 2022 |
| Delta (DAL) | 0000027904 | 2026-02-11 | 0000027904-26-000013 | `dal-20251231.htm` | 2025, 2024 |
| American (AAL) | 0000006201 | 2020-02-19 | 0000006201-20-000023 | `a10k123119.htm` | 2019, 2018 |
| American (AAL) | 0000006201 | 2024-02-21 | 0000006201-24-000010 | `aal-20231231.htm` | 2023, 2022 |
| American (AAL) | 0000006201 | 2026-02-18 | 0000006201-26-000014 | `aal-20251231.htm` | 2025, 2024 |
| Southwest (LUV) | 0000092380 | 2020-02-04 | 0000092380-20-000024 | `luv-12312019x10k.htm` | 2019 (and 2015-2018) |
| Southwest (LUV) | 0000092380 | 2024-02-06 | 0000092380-24-000027 | `luv-20231231.htm` | 2023, 2022 |
| Southwest (LUV) | 0000092380 | 2026-02-05 | 0000092380-26-000004 | `luv-20251231.htm` | 2025, 2024 |
| Alaska (ALK) | 0000766421 | 2020-02-12 | 0000766421-20-000013 | `alk-20191231.htm` | 2019 (and 2015-2018) |
| Alaska (ALK) | 0000766421 | 2024-02-14 | 0000766421-24-000012 | `alk-20231231.htm` | 2023, 2022 |
| Alaska (ALK) | 0000766421 | 2026-02-12 | 0000766421-26-000010 | `alk-20251231.htm` | 2025, 2024 |

### PRASM, nominal cents

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 | 2019-2025 nominal |
|---|---|---|---|---|---|---|
| **UAL** | 13.90 | 16.15 | 16.84 | 16.66 | 16.18 | **+16.4%** |
| DAL | 15.35 | 17.24 | 17.98 | 17.65 | 17.37 | +13.2% |
| AAL | 14.74 | 17.13 | 17.47 | 16.93 | 16.58 | +12.5% |
| LUV | 13.21 | 14.42 | 13.88 | 14.09 | 14.18 | +7.3% |
| ALK | not disclosed | not disclosed | not disclosed | 13.99 | 13.81 | n/a |

### PRASM, real (2025 cents, CPI-U deflated)

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 | 2019-2025 real |
|---|---|---|---|---|---|---|
| **UAL** | 17.50 | 17.77 | 17.79 | 17.10 | 16.18 | **-7.6%** |
| DAL | 19.33 | 18.97 | 19.00 | 18.11 | 17.37 | -10.1% |
| AAL | 18.56 | 18.84 | 18.46 | 17.38 | 16.58 | -10.7% |
| LUV | 16.64 | 15.86 | 14.67 | 14.46 | 14.18 | -14.8% |
| ALK | n/a | n/a | n/a | 14.36 | 13.81 | n/a |

### Yield (passenger revenue per RPM), nominal cents

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 | 2019-2025 nominal |
|---|---|---|---|---|---|---|
| **UAL** | 16.55 | 19.36 | 20.07 | 20.05 | 19.67 | **+18.9%** |
| DAL | 17.79 | 20.57 | 21.06 | 20.68 | 20.74 | +16.6% |
| AAL | 17.41 | 20.67 | 20.92 | 19.93 | 19.83 | +13.9% |
| LUV | 15.82 | 17.29 | 17.35 | 17.53 | 18.31 | +15.7% |
| ALK | 14.45 | 17.16 | 16.61 | 16.68 | 16.64 | +15.2% |

### Yield, real (2025 cents, CPI-U deflated)

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 | 2019-2025 real |
|---|---|---|---|---|---|---|
| **UAL** | 20.84 | 21.30 | 21.21 | 20.58 | 19.67 | **-5.6%** |
| DAL | 22.40 | 22.63 | 22.25 | 21.22 | 20.74 | -7.4% |
| AAL | 21.92 | 22.74 | 22.10 | 20.45 | 19.83 | -9.6% |
| LUV | 19.92 | 19.02 | 18.33 | 17.99 | 18.31 | -8.1% |
| ALK | 18.20 | 18.88 | 17.55 | 17.12 | 16.64 | -8.6% |

### Total revenue per ASM (TRASM / RASM), nominal cents

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 | Metric label as filed |
|---|---|---|---|---|---|---|
| **UAL** | 15.18 | 18.14 | 18.44 | 18.34 | 17.88 | TRASM |
| DAL as filed | 17.07 | 21.69 | 21.34 | 21.37 | 21.26 | TRASM (includes refinery sales) |
| DAL adjusted | not shown 2019 | 19.55 | 20.10 | 19.76 | 19.56 | TRASM, adjusted (ex third-party refinery sales) |
| AAL | 16.05 | 18.82 | 19.01 | 18.51 | 18.25 | Total revenue per ASM |
| LUV | 14.26 | 16.04 | 15.32 | 15.51 | 15.59 | Operating revenues per ASM |
| ALK | 13.17 | 15.87 | 15.21 | 15.41 | 15.32 | RASM |

Real (2025 cents) for the two nearest peers on the same basis: UAL TRASM 19.12 (2019) to 17.88
(2025), -6.5%. AAL total revenue per ASM 20.21 (2019) to 18.25 (2025), -9.7%. Delta is not put
on this line because its as-filed TRASM carries refinery revenue and its adjusted TRASM is not
disclosed for 2019 in the filings read.

### Capacity and traffic, nominal units

| Carrier | ASMs 2019 (m) | ASMs 2025 (m) | change | RPMs 2019 (m) | RPMs 2025 (m) | change |
|---|---|---|---|---|---|---|
| **UAL** | 284,999 | 330,284 | **+15.9%** | 239,360 | 271,619 | **+13.5%** |
| DAL | 275,379 | 298,045 | +8.2% | 237,680 | 249,578 | +5.0% |
| AAL | 285,088 | 299,411 | +5.0% | 241,252 | 250,294 | +3.7% |
| LUV | 157,254 | 180,046 | +14.5% | 131,345 | 139,443 | +6.2% |
| ALK | 66,654 | 92,962 | +39.5% | 56,040 | 77,110 | +37.6% |

Alaska's 2025 figures include Hawaiian Airlines, acquired in September 2024. The change is not
organic. See caveats.

### Load factor, percent

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| **UAL** | 84.0 | 83.4 | 83.9 | 83.1 | 82.2 |
| DAL | 86.3 | 84 | 85 | 85 | 84 |
| AAL | 84.6 | 82.9 | 83.5 | 84.9 | 83.6 |
| LUV | 83.5 | 83.4 | 80.0 | 80.4 | 77.4 |
| ALK | 84.1 | 84.5 | 83.7 | 83.9 | 82.9 |

Delta reports load factor to the whole percentage point in the 2023 and 2025 10-Ks and to one
decimal in the 2019 10-K. The precision difference is Delta's, not a transcription loss.

### Cost per ASM, nominal cents (as filed, DEFINITIONS DIFFER)

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 | Label as filed |
|---|---|---|---|---|---|---|
| **UAL** | 13.67 | 17.19 | 16.99 | 16.70 | 16.46 | CASM |
| DAL | 14.67 | 20.12 | 19.31 | 19.30 | 19.31 | CASM |
| AAL | 14.98 | 18.20 | 17.92 | 17.61 | 17.76 | Total operating cost per ASM |
| LUV | 12.38 | 15.36 | 15.19 | 15.32 | 15.35 | Operating expenses per ASM |
| ALK | not shown | not shown | not shown | not shown | not shown | CASM defined but level not in the stats table |

### Ex-fuel unit cost, nominal cents. **THESE ARE NOT THE SAME MEASURE. DO NOT COMPARE ACROSS COLUMNS.**

| Carrier | 2019 | 2022 | 2023 | 2024 | 2025 | What is excluded |
|---|---|---|---|---|---|---|
| **UAL CASM-ex** | 10.21 | 11.73 | n/d | n/d | n/d | fuel, profit sharing, third-party business expense, special charges |
| DAL CASM-Ex | n/d in FY2019 stats table | 12.87 | 13.17 | 13.54 | 13.86 | fuel, expenses related to third-party refinery sales, "and other items" |
| AAL | n/d in the stats table | n/d | n/d | n/d | n/d | AAL's 10-K non-GAAP tables reconcile pre-tax and net income excluding net special items, not a unit cost |
| LUV ex fuel | 9.62 | 11.33 | 11.54 | 12.05 | 12.44 | fuel only |
| LUV ex fuel and profit sharing | 9.19 | 11.25 | 11.47 | 11.99 | 12.38 | fuel and profit sharing |
| LUV ex fuel, profit sharing, special items | n/d | n/d | n/d | 11.95 | 12.32 | fuel, profit sharing and special items (2025 10-K reconciliation) |
| ALK CASMex | 8.70 | 10.41 | 10.14 | 10.80 | 11.42 | fuel, **freighter costs**, special items |

### Fuel and employees, peers

| Carrier | Year | Fuel gallons (m) | Avg price / gal | Employees | Basis of employee count |
|---|---|---|---|---|---|
| DAL | 2019 | 4,214 | 2.02 | 91,224 | full-time equivalent, end of period, excludes non-owned regional carriers |
| DAL | 2023 | 3,926 | 2.82 | ~103,000 | as above, "approximate" |
| DAL | 2024 | 4,114 | 2.57 | ~103,000 | as above |
| DAL | 2025 | 4,269 | 2.30 | ~103,000 | as above |
| AAL | 2019 | 4,537 | 2.07 | 133,700 | full-time equivalent, end of period |
| AAL | 2023 | 4,140 | 2.96 | 132,100 | as above |
| AAL | 2024 | 4,391 | 2.60 | 133,300 | as above |
| AAL | 2025 | 4,488 | 2.39 | 139,100 | as above |
| LUV | 2019 | 2,077 | 2.09 | 60,767 | active full-time equivalent |
| LUV | 2023 | 2,143 | 2.89 | 74,806 | as above |
| LUV | 2024 | 2,194 | 2.64 | 72,450 | as above |
| LUV | 2025 | 2,169 | 2.41 | 72,790 | as above |
| ALK | 2023 | 824 | 3.21 (economic) | 23,319 | **average** full-time equivalent |
| ALK | 2024 as reported | 925 | 2.74 (economic) | 25,751 | as above |
| ALK | 2025 | 1,146 | 2.52 (economic) | 31,585 | as above |
| **UAL** | 2019 | 4,292 | 2.09 | 95,900 | **year-end headcount, not FTE** |
| **UAL** | 2023 | 4,205 | 3.01 | 103,300 | as above |
| **UAL** | 2024 | 4,444 | 2.65 | 107,300 | as above |
| **UAL** | 2025 | 4,663 | 2.44 | 113,200 | as above |

Aircraft at end of period, where the peer discloses one line: AAL 1,547 (2019), 1,521 (2023),
1,562 (2024), 1,580 (2025). LUV 747 (2019), 817 (2023), 803 (2024), 803 (2025). Alaska
discloses a mainline and a regional "operating fleet" separately (231 mainline and 83 regional
at 2023) rather than a single total. Delta's 10-K fleet table is by aircraft type; a single
total line was not transcribed here.

---

## 5. CAVEATS AND DEFINITION DIFFERENCES

These are material. A number that is not comparable is worse than a missing number, because it
looks usable.

1. **CASM-ex is defined differently by every carrier.** UAL excludes fuel, profit sharing,
   third-party business expense and special charges. Delta excludes fuel, expenses related to
   third-party refinery sales, "and other items" (Delta owns the Trainer refinery; no other
   carrier here does). Alaska excludes fuel, **freighter costs** and special items (Alaska
   flies freighters under an Amazon agreement and says explicitly that it strips them "to
   allow for better comparability to other carriers that do not operate freighter aircraft").
   Southwest publishes three different ex-fuel lines and none of them matches UAL's. American
   does not publish a unit-cost non-GAAP measure in the 10-K at all. **The ex-fuel unit cost
   row is not a peer comparison. It is five different measures printed side by side.**

2. **Delta's TRASM includes third-party refinery sales.** As-filed Delta TRASM (21.26c in 2025)
   is not on the same basis as UAL's TRASM (17.88c). Delta's own "TRASM, adjusted" (19.56c in
   2025) removes the refinery and is the closer comparison, but Delta does not disclose an
   adjusted figure for 2019 in the FY2019 10-K, so the 2019-2025 adjusted change cannot be
   computed from the filings read.

3. **Alaska's 2024 and 2025 include Hawaiian Airlines.** Alaska closed the Hawaiian
   acquisition in September 2024. The FY2025 10-K presents 2024 three ways: "As Reported",
   "Hawaiian Airlines" standalone, and "Pro Forma". The 2024 column used above is **As
   Reported**. Alaska's +39.5% ASM growth 2019 to 2025 is an acquisition, not organic capacity.

4. **Alaska does not disclose consolidated PRASM before 2024.** The FY2019 and FY2023 10-Ks
   give Yield, RASM and CASMex but no consolidated PRASM line. It is not computed here.

5. **UAL does not disclose average FTE employees.** UAL gives year-end headcount. Delta,
   American and Southwest give end-of-period FTE; Alaska gives **average** FTE. Four different
   employee bases. Per-employee productivity ratios across these carriers are not sound
   without rebuilding the counts.

6. **Delta's FTE excludes regional carriers it does not own; UAL's headcount is United's own
   employees and likewise excludes third-party regional operators.** UAL's ASMs, however,
   include regional flying. Any ASM-per-employee figure is therefore inflated for every
   carrier in the table, and inflated by a different amount for each depending on the size of
   its purchased regional flying.

7. **UAL's CASM-ex is missing for five of nine years in the 10-K record** (2017, 2018, 2023,
   2024, 2025). It exists in UAL's Form 8-K earnings releases, which were outside the sourcing
   instruction for this file. This is a gap, not a zero.

8. **Southwest changed the footnoting of its unit revenue lines in 2025.** The FY2025 10-K
   marks passenger yield, RASM and PRASM with footnote (k), which was not present on the same
   lines in the FY2019 10-K. The footnote text was not transcribed; if the Southwest lines are
   load-bearing for any later argument, read footnote (k) in `luv-20251231.htm` before using
   them.

9. **2020 and 2021 are pandemic years and every rate in them is a different animal.** UAL's
   2020 CASM of 17.68c and CASM-ex of 17.13c reflect an ASM denominator that fell 57% while
   fixed costs did not. They are reported here because the instruction asked for the full nine
   years, and they are the honest record. They are not a trend observation.

10. **The 2025 CPI-U annual average (321.943) is a published BLS annual average and is final
    for the deflator's purpose.** No forecast or partial-year figure was used. One 2025 monthly
    observation came back as a dash in the BLS API response; the M13 annual average was taken
    directly and cross-checks against FRED.

11. **PRASM, TRASM, yield and CASM are all ratios UAL computes and files.** They were
    transcribed, not recomputed from revenue and ASMs. Where a derived figure appears in this
    file (ASMs per gallon, ASMs per employee, ASMs per aircraft, implied real passenger
    revenue) it is labelled as derived.

---

## 6. WHAT IS NOT IN THIS FILE

- UAL CASM-ex for 2017, 2018, 2023, 2024, 2025. Not in the 10-Ks. Available in Form 8-K
  earnings releases.
- UAL average full-time-equivalent employees, any year. Not disclosed as a level.
- Alaska consolidated PRASM for 2019, 2022, 2023. Not disclosed.
- Delta adjusted TRASM for 2019. Not disclosed in the FY2019 10-K.
- American ex-fuel unit cost, any year. Not disclosed in the 10-K.
- A single "total aircraft" line for Delta. Delta's 10-K fleet table is by type.
- Any verdict. Section 5 contains caveats about comparability, not conclusions about the
  business.

