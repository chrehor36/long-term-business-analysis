# SNIRF research notes (2026-10-17)
- run file copied from template before any fetch (commit e675c091).

## Documents read (primary first; operator rule 4; no SEC accession exists for this issuer)
| document | date | where | kept |
|---|---|---|---|
| Senior plc Annual Report and Accounts 2025 (FY to 31 Dec 2025) | approved 27 Feb 2026 | seniorplc.com reports-and-presentations/annual-report-2025.pdf | cache/ (gitignored) |
| Annual Report 2024, 2023, 2022, 2020, 2018, 2016, 2015 | each Feb/Mar of the following year | same path, annual-report-YYYY.pdf | cache/ |
| Annual Reports 2017, 2019, 2021 | not fetched (404 at the same URL pattern); their balance sheets are the comparatives in the 2018, 2020 and 2022 reports | | |
| Results for the half-year ended 30 June 2026 | Aug 2026 | seniorplc.com interim_results_2026_final.pdf | cache/ |
| RNS "Recommended cash acquisition of Senior plc" (Rule 2.7) | 7 Apr 2026 | investegate.co.uk/announcement/rns/senior--snr/recommended-cash-acquisition-of-senior-plc/9508660 | read via search summary only (aggregator of the RNS) |
| RNS "Court Sanction of Scheme of Arrangement" | 6 Oct 2026 | investegate 9809642 / Reuters-TradingView copy | read via TradingView copy |
| RNS "Scheme of Arrangement becomes Effective" | 8 Oct 2026 | TradingView/Reuters copy; LSE "Cancellation - SENIOR PLC" (investegate 9815354); FCA removal from Official List 09/10/2026 08:00 | search summaries |
| Rivals' 10-K facts | see run file | SEC companyfacts (data.sec.gov), CIK 76334 Parker-Hannifin, 1551182 Eaton, 67347 Modine | cache/ (gitignored); arithmetic in rivals.py |
| Price | last London close 297.5p, 7 Oct 2026; SNIRF 3.75 USD (stale) and 3.35 USD on 9 Oct 2026 | Yahoo chart API (aggregator, flagged) | cache/y_*.json |
| Sovereign | BoE IADB IUDLNPY (20-year nominal par gilt yield) 5.7225% on 14 Oct 2026 (5.758% on 7 Oct 2026) | bankofengland.co.uk IADB | |

## Cross-check (operator rule 4)
Five-year summary of the 2025 report gives 2025 net assets GBP 380.3m; the consolidated balance sheet on report page 132 gives Total equity 380.3 = Total assets 781.5 less Total liabilities 401.2. Agrees.

## Share count
419,418,082 issued (AR2025 note 25 and shareholder analysis); 7,331,947 shares held as own/treasury shares at 31 Dec 2025 (AR2025 Company note, "total number of treasury shares"; the own-shares reserve is described as EBT holdings). Outstanding 412,086,135. Offer document's fully diluted value GBP 1,275m at 300p implies about 425m fully diluted shares.

## Extracts committed: bs_extract.txt (balance sheets 2014-2025), rivals.py, q7.py, ids.py, check.py.
