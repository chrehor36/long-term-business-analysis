# ANIOY research notes (2026-10-13)

Run file copied from template 2026-10-13 21:48 EDT before any fetch.

## Documents fetched (raw PDFs and text extracts in cache/, gitignored)
- 2025 Acerinox Group Annual Accounts (Consolidated Financial Statements, Dec 31 2025; authorised 2026-02-25), acerinox.com
  `.../memoria-e-informe-anual/2025-Acerinox-Group-Annual-Accounts.pdf`. In-house translation; Spanish original prevails.
- 2024 Acerinox Group Annual Accounts, same folder.
- 2023 Consolidated Annual Accounts and Integrated Annual Report, acerinox.com `.../informes-trimestrales-doc/`.
- Management Report Business Year 2022 and Explanatory Notes to the Annual Financial Report (IFRS statements 2022 and 2021).
- 2021 Business Year Results Report (company format; the only 2020 source read).
- CNMV AUDITA 2019/18351_en.pdf (PwC report, consolidated annual accounts FY2019 with FY2018), signed 2020-02-27.
- CNMV AUDITA 2017/17363_en.pdf (consolidated annual accounts FY2017 with FY2016).
- Condensed consolidated interim financial statements H1 2026 with interim management report (PwC limited review), acerinox.com.
- Rival: Outokumpu Annual Report 2025 (cision) and Annual Report 2020 (cision): key figures and business-area tables.
- EDGAR: F-6EF filed 2019-11-22, accession 0001193805-19-001764 (JPMorgan Chase Bank depositary), CIK 1438557:
  "Share representing one-half of one ordinary share of Acerinox, S.A."
- Not found: the FY2021 or FY2020 statutory consolidated accounts PDF (URLs guessed, CNMV listing unreachable);
  the FY2025 Consolidated Management Report (site behind bot protection). CNMV inside-information notices not read
  (CNMV portal query returned an error page).

## Tools
- tools/run.py ANIOY: "not an SEC filer"; cover_shares.py: "NOT AN SEC REGISTRANT". Arithmetic by hand: figures.py.
- Sovereign EUR: 3.76% (ECB euro area AAA yield curve SR_30Y, 2026-10-12) via tools/sources.py.
- Price ACX.MC 16.77 EUR close 2026-10-13 (aggregator, Yahoo chart via tools/sources.py; flagged). ANIOY $9.29 2026-10-12.
- Cross-check on price: H1 2026 Note 17, 169,622 treasury shares bought 2026-06-30 for EUR 2,702k = EUR 15.93 each.

## Shares
249,335,371 ordinary shares of EUR 0.25 (Note 15, 2025 accounts; unchanged at 2026-06-30, H1 Note 17);
treasury 176,622 at 2026-06-30 -> 249,158,749 outstanding.

## Net debt at 2026-06-30 (H1 balance sheet)
Bank borrowings 1,287.2 + 990.8 = 2,278.0; cash 916.8; company NFD 1,361 (stated). Leases inside other financial
liabilities, not separated in the condensed statements; right-of-use assets 23.5 (lease liability taken at ~ that, said so).

## Contamination (declared, not used)
Commit subjects in the session context name another company's run (APEMY, a stainless rival) and its Q2 reasoning.
Memory index lines name counts of gate-clearers. Directory listing of git status shows other research folder names.
