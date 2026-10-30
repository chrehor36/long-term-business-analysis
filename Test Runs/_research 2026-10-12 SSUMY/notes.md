# SSUMY research notes (2026-10-12)
- Run file copied from template before any fetch.

## Step 0 facts (2026-10-12)
- Price 8053.T JPY 1,708 close 2026-10-09 (Yahoo chart API, aggregator; 2026-10-12 is a Tokyo holiday). SSUMY USD 10.84 2026-10-12 (Yahoo, aggregator). USDJPY 158.68 (Yahoo, aggregator).
- ADS ratio 1 ADS = 1 common share: F-6EF, Citibank N.A., filed 2026-06-22, accession 0001193805-26-000852 (pre-split). Post-split check: 1708/158.68 = 10.76 vs 10.84 -> 1:1 holds after the split.
- JGB 30y 4.136% dated 2026-10-08, Japan MOF jgbcme.csv via tools/sources.py.
- Shares (post-split): issued 4,780,460,736, treasury 41,613,968, June 30 2026 (Q1 FY2026 Tanshin, 2026-07-31). Outstanding 4,738,846,768.
  Mar 31 2026 (AFR FY2025 note 20): issued 1,211,426,667, treasury 18,766,168 pre-split (x4 = 4,845,706,668 / 75,064,672: matches Tanshin).
- Net interest-bearing liabilities (company definition, ex leases): 3,147.2bn Mar 31 2026; 3,713.5bn Jun 30 2026 (+566 from Sumisho Air Lease acquisition, closed April 2026).
- Leases Jun 30 2026: 85,881 + 430,518 = 516,399m.
- Docs (cache/, gitignored): AFR FY2020..FY2025 (years ended Mar 2021..Mar 2026), IR2026 performance data, IR2023/2024/2025 parts, FY2023 results presentation (2024-05-02), Q1 FY2026 Tanshin + presentation (2026-07-31).
- FY naming: company "FY2025" = year ended March 31, 2026.
