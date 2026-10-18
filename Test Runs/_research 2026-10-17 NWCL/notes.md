# NWCL research notes (2026-10-17)
Run file copied from template before any fetch (commit 4e43dc10).

## Documents read (SEC EDGAR, CIK 0002131813; raw copies in cache/, gitignored)
- 424B3 resale prospectus, 2026-10-16, accession 0001140361-26-039925 (ny20082989x3_424b3.htm): Business (Competition, Legal Proceedings), Risk Factors (FPA), MD&A (Liquidity), Certain Relationships, audited FY2025/FY2024 statements (Grant Thornton, Dublin, report dated 2026-06-02), interim H1 2026 statements, Note 27.
- 6-K 2026-10-05, accession 0001140361-26-038557: ex 99.1 press release of 2026-10-02 (H1 2026 results; preliminary unaudited cash at 2026-09-30 about EUR 233M), ex 99.2 interim statements.
- 6-K 2026-10-06, 0000950103-26-015281 (general meeting approved the FPA off-market purchase of up to 7,000,000 shares).
- 6-K 2026-10-14, 0000950103-26-015583 (cover only read: press release on a MOX fuel engineering and testing centre in France).
- 6-K 2026-09-30, 0000950103-26-014872 (cover only read: Magwood to join the board in January 2027).
- 6-K 2026-09-25, 0000950103-26-014519 and 6-K 2026-09-23, 0000950103-26-014361: downloaded, exhibits not read for this run.
- 424B3 proxy statement/prospectus 2026-08-10, 0001140361-26-031950: searched only for audited years before FY2024 (none; equity at 2023-12-31 appears only as an opening balance).

## Key figures (EUR thousands, IFRS; audited FY, unaudited H1)
| | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|
| Revenue | 46,743 | 32,769 | 13,347 | 19,429 |
| Operating loss | (115,798) | (139,928) | (75,465) | (81,115) |
| Net loss | (110,163) | (139,965) | (74,293) | (81,981) |
| D&A and provisions (CF add-back) | 13,121 | 16,931 | 7,397 | 8,286 |
| Share-based payment | 8,316 | 14,895 | 4,975 | 21,010 |
| Operating cash flow | (104,477) | (119,678) | (72,233) | (53,687) |
| PP&E purchases | (37,712) | (43,002) | (18,542) | (25,328) |
| Intangible purchases | (11,751) | (2,861) | (458) | (1,642) |
| Cash and equivalents, end | 192,714 | 105,270 | 131,896 | 66,540 |
| Total equity, end | 361,243 | 296,928 | | 320,223 |
| Accumulated deficit, end | (185,782) | (324,123) | | n/a (share premium reduction) |
Equity at 2023-12-31: 326,454; accumulated deficit (75,619).

Cross-check (operator rule 4): H1 2026 cash EUR 66,540k in the press release (6-K 0001140361-26-038557, ex 99.1) equals the interim statement of financial position in the 424B3 (0001140361-26-039925); FY2025 cash EUR 105,270k is the same in the audited balance sheet and the H1 comparative column.

## Capital structure after the combination (424B3 of 2026-10-16)
- 281,534,950 Ordinary Shares outstanding "as of the date of this prospectus"; 10,354,197 Company Warrants (strike $11.50); about 8,855,000 NextChem Warrants (earn-out, set-off, no cash); 17,677,233 Class B earnout shares (VWAP $15 and $18 within five years), not outstanding.
- PIPE: 21,600,000 shares at $10.00, $216.0M gross.
- Trust: about $106.1M released; about $74.6M paid to Tech Opportunities LLC as the FPA prepayment (up to 7,000,000 shares; maturity up to 24 months; cash settlement at the lesser of 95% of VWAP and the Reset Price if not physically settled); SPAC expenses $12.4M and company expenses $16.5M paid at closing.
- Pro forma: FPA recognised as a decrease in cash of EUR 65.7M and treasury shares of EUR 65.4M (IAS 32).

## Price and rate
- $5.88 close 2026-10-16 (tools/sources.py price(), an aggregator quote, flagged); $6.37 close 2026-10-15 printed in the 424B3 cover.
- EUR sovereign: 3.671% ECB euro area AAA yield curve SR_30Y, 2026-10-15 (tools/sources.py sovereign('EUR')).

## Competitors named in the Competition section
NuScale (SEC filer, SMR), GE Vernova Hitachi BWRX-300 (GE Vernova files; the reactor is not a reported segment), X-energy (SEC filer, ticker XE; no annual tagged figures found), TerraPower Natrium (no SEC ticker found), Oklo (SEC filer, OKLO).
SEC companyfacts, 10-K annual, USD millions (XBRL transcription, not read against the filed statements):
- NuScale revenue 2022 11.8, 2023 22.8, 2024 37.0, 2025 31.5; operating loss 2022 -230.0, 2023 -275.6, 2024 -138.7, 2025 -689.6; operating cash flow 2022 -148.6, 2023 -183.3, 2024 -108.7, 2025 -459.6 (2025 10-K accn 0001822966-26-000018). 2020-2021 figures look like the pre-merger shell's and are not used.
- Oklo: no revenue tag; operating loss 2022 -1.8, 2023 -4.3, 2024 -52.8, 2025 -139.3; operating cash flow 2023 -10.8, 2024 -38.4, 2025 -82.2.
