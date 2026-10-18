# BROGF run notes (2026-10-17)
Working notes for the run file. Raw filings go under cache/ (gitignored); scripts/ holds the fetch and check scripts.

- 2026-10-17: run file copied from the template before any fetch (commit 86f53f29).
- `tools/run.py BROGF`: "not an SEC filer" (ticker gone from the SEC map after the 2025 deregistration). The tool takes no CIK; arithmetic done by hand from the filings.
- `Screens/cover_shares.py BROGF`: "NOT AN SEC REGISTRANT in the live ticker file". Count taken by hand from the FY2024 20-F cover.

## Documents read (SEC, CIK 0001774983)
| document | filed | accession |
|---|---|---|
| 20-F FY2024 | 2025-05-01 | 0001213900-25-038113 |
| 20-F/A FY2024 (iXBRL only) | 2025-05-01 | 0001213900-25-038264 |
| 20-F FY2023 (late) | 2024-11-12 | 0001213900-24-096530 |
| 20-F FY2022 (replaces FY2019-FY2020 20-Fs, covers FY2021-FY2022) | 2023-04-26 | 0001213900-23-032832 |
| 20-F FY2020 (reliance withdrawn 2022-08-17) | 2021-04-05 | 0001213900-21-020027 |
| 20-F FY2019 (reliance withdrawn 2022-08-17) | 2020-06-30 | 0001213900-20-016302 |
| 6-K, H1 2024 interim results | 2025-01-06 | 0001213900-25-001152 |
| 6-K + Ex 99.1, GulfNav SPA announced | 2025-05-27 | 0001213900-25-047862 |
| 6-K + Ex 99.1, voluntary Nasdaq delisting | 2025-05-28 | 0001213900-25-048302 |
| 6-K + Ex 4.94, the SPA itself | 2025-06-02 | 0001213900-25-050129 |
| Form 25 | 2025-06-09 | 0001213900-25-052639 |
| Form 15-12G (dated 2025-06-19) | 2025-06-20 | 0001213900-25-055785 |

## After the SEC filings stopped (primary, no accession)
- Brooge Energy Limited press release, 2025-11-25, "Brooge Energy Limited Announces Closing of Transaction and Declaration of Dividend" (GlobeNewswire; read through the financialcontent.com mirror because globenewswire.com returned 403). Closing, consideration received that day; substantially all of it distributed by dividend to holders of record of 2025-09-10 after reserving for anticipated liabilities and hold-backs; DTC holders USD 7.76 a share in cash on or about 2025-12-02, non-US registered holders about 22.787 GulfNav shares a share; BPGIC Holdings assumes certain liabilities and takes a reduced dividend; "no further distributions are anticipated"; the company expects to pay its debts as they fall due.
- Gulf Navigation Holding PJSC press release, 2025-11-14 (gulfnav.com, Article 20315): SCA approval to issue 358,841,476 new shares and to issue and convert 2.336 billion mandatory convertible bonds, both in favour of Brooge Energy Limited.
- Gulf Navigation completion release, 2025-11-27 (read on marketscreener, an aggregator, flagged): acquisition of all assets of Brooge Energy Limited and its operating subsidiaries completed.

## Aggregator, live quote only (flagged)
- `tools/sources.py` price (Yahoo chart): BROGF close $0.0003 on 2026-10-16; volume zero on most days since January 2026; one dividend event of $7.76, ex-date 2025-12-11; price $6.30 on 2025-12-08, $0.0002 on 2025-12-30.

## Sovereign
- USD 30-year par yield 5.43%, 2026-10-16, US Treasury daily par yield curve (`python tools/sources.py`).
