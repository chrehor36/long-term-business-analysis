# BIPC run notes 2026-10-17
- template copied before any fetch
- run.py failed (20-F filer); cover_shares OK. Figures from filed statements via scripts/fetch.py text extraction.
- Business behind the share = BIP (CIK 1406234); BIP 20-Fs read. Deciding part Transport (35% of 5-yr FFO).
- Net debt attributable to partnership 2026-06-30: 33,969; preferred 729 + perpetual notes 293 = 1,022; units 791.7m.
- 2026-10-17: raw/ renamed cache/ (gitignored) after the first commit took ~2 MB of extracted filing text; the deletion is recorded in the next commit; history not rewritten.
## Q2 arithmetic
Transport (BIP share): AdjEBITDA 968/1082/1235/1646/1563; maint 151/175/179/328/367; seg assets 8601/8333/11840/11720/11582
 -> (EBITDA-maint)/assets = 9.5/10.9/8.9/11.2/10.3 %.
Triton (pre-tax+interest)/assets: 2016 (-14+184)/8714; 2017 (354+282)/9578; 2018 (357+323)/10270; 2019 (381+316)/9643;
 2020 (368+253)/9713; 2021 (581+222)/12644; 2022 (818+226)/12109; 2023 (529+241)/11233; 2024 (567+260)/11103; 2025 (554+263)/9814.
Textainer: 2016 (-61.3+85.2)/4294; 2017 (22.4+117.5)/4401; 2018 (56.3+138.4)/4769; 2019 (58.5+153.2)/5203; 2020 (73.3+123.2)/5741;
 2021 (286.1+127.3)/7367; 2022 (317.0+157.2)/7613.
- 2026-10-17 close: check_citations.py 0 problems (66 ids); tools/check_framework.py PASS.
