# USNZY research notes (2026-10-13)
Started: template copied before any fetch.

## Sources used (all fetched 2026-10-13)
- CVM open data (dados.cvm.gov.br): DFP 2016-2025 and ITR 2026 zips -> data/usim_*.csv via extract_cvm.py (Usiminas CNPJ 60.894.730/0001-05, CVM code 014320).
- CVM RAD documents (rad.cvm.gov.br): DFP FY2025 154757; FY2023 v2 144312; FY2021 111713; FY2020 100148; FY2019 90949; FY2017 71440; ITR 2026-06-30 159792; Formulario de Referencia 2026 v7 159805 (embedded PDFs extracted with fre_extract.py).
- English 2025 Sustainability/Annual Report, usiminas.com (36 MB, kept in cache/, not committed).
- SEC EDGAR: Usiminas depositary F-6 POS 0001019155-17-000265 (preferred) and -000266 (common); rival 20-Fs listed in the run file (sec_get.py).
- Tesouro Nacional, Tesouro Transparente PrecoTaxaTesouroDireto.csv: NTN-F 2037 12.57% (2026-10-09).
- Yahoo chart API (aggregator, flagged): USIM5, USIM3, USNZY, BRL=X.
## Outcome
Q1 IN; Q2 OUT (steel decides; not the low-cost producer; price set by imports). Computation beneath the stop in q7_output.txt.
check_cites.py: 33 ids, 17 fragments, 0 problems. tools/check_framework.py PASS.
