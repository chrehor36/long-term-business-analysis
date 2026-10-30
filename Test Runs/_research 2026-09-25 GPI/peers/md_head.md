# COMPETITOR ROW: Group 1 Automotive (GPI) against the five other US-listed franchised dealer groups

Built 2026-09-25. Fetch and compute only; no judgment is made in this file.

**Method.** Every figure is read off the filed 10-K primary document (EDGAR Archives, HTML stripped to text by `fetch.py`), not XBRL companyfacts. For each year the figure is taken from the newest 10-K that contains that year: 2023, 2024 and 2025 from the FY2025 10-K; 2021 and 2022 from the FY2023 10-K. USD millions throughout. CIKs were verified against the `name` field of each `data.sec.gov/submissions/CIK##########.json`:

| Ticker | CIK | Name in submissions JSON | FY2025 10-K (accession, filed, primary doc) | FY2023 10-K (accession, filed, primary doc) |
|---|---|---|---|---|
| AN | 350698 | AUTONATION, INC. | 0001628280-26-007800, 2026-02-12, an-20251231.htm | 0000350698-24-000021, 2024-02-16, an-20231231.htm |
| PAG | 1019849 | PENSKE AUTOMOTIVE GROUP, INC. | 0001628280-26-012830, 2026-02-27, pag-20251231.htm | 0001019849-24-000033, 2024-02-16, pag-20231231.htm |
| LAD | 1023128 | LITHIA MOTORS INC | 0001023128-26-000015, 2026-02-25, lad-20251231.htm | 0001023128-24-000032, 2024-02-23, lad-20231231.htm |
| ABG | 1144980 | ASBURY AUTOMOTIVE GROUP INC | 0001144980-26-000051, 2026-02-20, abg-20251231.htm | 0001144980-24-000076, 2024-02-29, abg-20231231.htm |
| SAH | 1043509 | SONIC AUTOMOTIVE INC | 0001628280-26-010570, 2026-02-23, sah-20251231.htm | 0001043509-24-000022, 2024-02-22, sah-20231231.htm |

All five FY2025 10-Ks are filed. Text copies: `AN_tenk_fy2025.txt`, `AN_tenk_fy2023.txt`, and the same pattern for PAG, LAD, ABG, SAH (this folder). Arithmetic: `build_row.py` (inputs transcribed by hand from the text files, then computed); `write_md.py` assembles this file.

**Definitions (CONVENTION, stated so the reader can reproduce them).**
- GM % = total gross profit / total revenues.
- OpM % as filed = operating income (income from operations) as printed / total revenues.
- OpM % ex-impairment = (operating income + impairment lines printed on the face of the income statement) / total revenues. Only face lines are added back, because that is the only like-for-like basis across all five; impairments buried inside other captions are listed in each peer's notes but NOT added back.
- P&S GM % = parts and service gross profit / parts and service revenue. Where the filing gives P&S cost of sales rather than P&S gross profit, gross profit = revenue less cost of sales (computed).
- 5-yr mean = simple arithmetic mean of the five annual percentages (not revenue-weighted).
- Floorplan interest is shown for reference; every peer reports it BELOW operating income, so neither OpM figure is after floorplan interest.

