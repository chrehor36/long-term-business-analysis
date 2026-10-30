# AMMX: the figures used, and where each comes from

Raw documents are in `cache/` (gitignored). Every figure below was typed from the document named beside it.

## Sources

| Key | Document | Date | Identifier | Audited? |
|---|---|---|---|---|
| F10 | Form 10-12G/A (FY2017, FY2018, Q1 2019) | 2019-07-02 | 0001099910-19-000046 | FY2017-18 audited |
| K19 | 10-K FY2019 | 2020-06-05 | 0001099910-20-000042 | audited (dbbmckennon) |
| K20 | 10-K FY2020 | 2021-04-16 | 0001099910-21-000051 | audited |
| K21 | 10-K FY2021 | 2022-03-31 | 0001099910-22-000055 | audited |
| Q122, Q222, Q322 | 10-Qs 2022 | 2022-05-23, 2022-08-15, 2022-11-23 | 0001099910-22-000107, -000157, -000243 | reviewed, unaudited |
| P21 | DEF 14A | 2021-10-15 | 0001099910-21-000121 | n/a |
| NT | NT 10-Q Q3 2022 | 2022-11-15 | 0001099910-22-000236 | n/a |
| F15 | Form 15 (Rule 12g-4(a)(1)) | 2023-04-05 | 0001099910-23-000058 | n/a |
| 8-K | 8-Ks 2020-07-29 (Geneva Roth note), 2020-12-21 (reverse split), 2021-02-01 (Series A preferred), 2021-12-03 (meeting) | | 0001099910-20-000070, -20-000112, -21-000003, -21-000152 | n/a |
| R22 | Company press release "Reports Revenue of $19.2 Million for the Year Ended December 31, 2022" (TheNewswire; read on the financialcontent mirror) | 2023-03-31 | no accession; company-published | "Unaudited" in its own headings |
| R24 | Company press release "Reports Revenue of $14.9 Million for the Year Ended December 31, 2024" (Newsfile 249749; read on the financialcontent mirror) | 2025-04-25 | Newsfile 249749 | "UNAUDITED" |
| R25 | Company press release "Delivered Strong Margin Gains and Returned to Profitability in 2025" | 2026-03-10 | Newsfile 287859 | "UNAUDITED" |
| R26Q2 | Company press release, second quarter and six months to 2026-06-30 | 2026-08-18 | Newsfile 310172 | "UNAUDITED" |
| OTC | OTC Markets disclosure list for AMMX (164 records, tier code PL): annual reports for FY2022 to FY2025 (FY2025 amended 2026-03-17), quarterlies to 2026-06-30 | listed 2026-10-16 | backend.otcmarkets.com list endpoint | the documents themselves could not be downloaded: the content endpoint returned "This site is temporarily unavailable ... scheduled maintenance" on every try, 19:50 to 20:05 EDT 2026-10-16 |
| PX | Price: Yahoo chart API, OTC Pink, close 2026-10-15 $0.099 on 300 shares | 2026-10-16 | aggregator, flagged | n/a |

## Owner cash by year (owner_cash.py)

Owner cash = operating cash + property and rental-fleet spending as printed + equipment-sale proceeds
- equipment financed under capital leases (non-cash spending) - finance-lease principal paid - stock paid for services.
All-equity owner cash adds back interest paid times (1 - 28.15%), the FY2021 tax note's 21.00% federal plus 7.15% state.

| Year | Source | Operating cash | Owner cash | All-equity | Revenue | Operating margin |
|---|---|---|---|---|---|---|
| 2017 | F10 | 1,975,547 | 240,627 | 630,512 | 8,709,514 | 17.4% |
| 2018 | K19 | 1,420,165 | -2,270,659 | -1,695,980 | 9,797,854 | 19.9% |
| 2019 | K20 (restated column) | -1,525,908 | -3,133,212 | -2,595,878 | 12,655,238 | 7.4% |
| 2020 | K21 | -256,068 | -1,261,415 | -609,352 | 12,279,120 | -0.5% |
| 2021 | K21 | 5,783,721 | 4,331,392 | 4,887,564 | 24,721,838 | 12.8% |
| 2022 | R22 | 1,906,657 | -122,059 | 346,839 | 19,222,509 | 9.2% |
| 2023 | R24 (comparative column) | -2,405,549 | -3,788,452 | -3,405,997 | 13,383,499 | -6.4% |
| 2024 | R25 (comparative column, restated) | 3,743,605 | -2,880,209 | -2,015,870 | 14,736,842 | 3.0% |
| 2025 | R25 | -791,671 | 4,043,482 | 5,016,608 | 14,034,542 | 6.6% |

Averages: 2021-2025 owner cash 316,831, all-equity 965,829; 2020-2023 (trough to trough) owner cash -210,134,
all-equity 304,764; 2017-2025 owner cash -537,834, all-equity 62,050.

## The same year printed differently by the company

| Item | First printing | Later printing |
|---|---|---|
| FY2019 operating cash | -2,491,724 (K19) | -1,525,908 (K20); the difference, 965,816, is twice the 482,908 loss on extinguishment, added back with the wrong sign in K19 |
| FY2022 net income | 871,060; year-end accumulated deficit (17,464,626) (R22) | deficit at 2022-12-31 (16,912,288) in R24's equity statement, which implies 1,423,398 |
| FY2023 net loss | (764,741), per the first FY2023 release as found by search (not read in full) | (1,374,361) (R24) |
| FY2024 net loss | (1,158,221); equity 2,241,493; total assets 17,505,773 (R24) | (856,734); equity 2,542,980; total assets 18,412,122 (R25) |
| 2025-12-31 balance sheet | total assets 18,197,479; inventory 11,040,250; rental fleet 739,805; equity 3,668,143; deficit (18,018,220) (R25) | total assets 17,363,629 (liabilities and equity 17,363,912); inventory 7,481,302; rental fleet 6,619,681; equity 3,005,677; deficit (18,680,969) (R26Q2) |
| Shares | 14,829,155 (Q322 cover, 2022-11-18) | 15,112,988 (R25 equity statement) / "14,829,155 shares issued and outstanding" (R25 balance sheet) / "14,112,988 at December 31, 2025" (R26Q2) / 21,112,988 at 2026-06-30 with common stock 21,112 and paid-in capital unchanged at 21,671,534 (R26Q2) |

## Net debt at the latest company-published date (R26Q2, 2026-06-30)

Lines of credit 1,549,303 + notes payable current 1,315,741 + notes payable long-term 10,656,060 = 13,521,104;
less cash 1,094,729 = 12,426,375. Finance-lease liabilities shown at 2025-12-31 in R25 (3,293,617) do not appear in R26Q2.
Operating lease (related party) left out.

## Competitors (SEC companyfacts, 10-K values; peers.py)

| Name | Kind | Operating margin, range of years | Latest 10-K |
|---|---|---|---|
| Caterpillar (named) | maker | 3.0% (2016) to 20.2% (2024); pre-tax 0.4% to 20.6% | 0000018230-26-000008 |
| Deere (named) | maker | 9.7% (2016) to 21.2% (2023); return on equity 19.4% to 46.7% | 0001104659-25-122321 |
| Titan Machinery (substitute) | dealer | -1.7% (FY2015) to 6.3% (FY2022); return on equity -11.2% to 19.0% | 0001628280-26-022376 |
| Alta Equipment Group (substitute) | dealer and renter | -0.9% (2020) to 2.9% (2023); net loss in five of seven years 2019-2025 | 0001193125-26-076932 |
