import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from edgar import get, strip_html
J = [
 ('TME_20F_FY2025.txt','https://www.sec.gov/Archives/edgar/data/1744676/000119312526160257/tme-20251231.htm'),
 ('TME_20F_FY2024.txt','https://www.sec.gov/Archives/edgar/data/1744676/000095017025056949/tme-20241231.htm'),
 ('TME_20F_FY2023.txt','https://www.sec.gov/Archives/edgar/data/1744676/000095017024045593/tme-20231231.htm'),
 ('TME_20F_FY2022.txt','https://www.sec.gov/Archives/edgar/data/1744676/000095017023014459/tme-20221231.htm'),
 ('TME_20F_FY2021.txt','https://www.sec.gov/Archives/edgar/data/1744676/000119312522120210/d242038d20f.htm'),
 ('SIRI_10K_FY2025.txt','https://www.sec.gov/Archives/edgar/data/908937/000090893726000006/siri-20251231.htm'),
 ('SIRI_10K_FY2024.txt','https://www.sec.gov/Archives/edgar/data/908937/000090893725000005/siri-20241231.htm'),
 ('SIRI_10K_FY2023.txt','https://www.sec.gov/Archives/edgar/data/908937/000090893724000008/siri-20231231.htm'),
 ('SIRI_10K_FY2022.txt','https://www.sec.gov/Archives/edgar/data/908937/000090893723000006/siri-20221231.htm'),
 ('SIRI_10K_FY2021.txt','https://www.sec.gov/Archives/edgar/data/908937/000090893722000007/siri-20211231.htm'),
 ('AAPL_10K_FY2025.txt','https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm'),
 ('GOOGL_10K_FY2025.txt','https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm'),
 ('AMZN_10K_FY2025.txt','https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm'),
 ('WMG_10K_FY2022.txt','https://www.sec.gov/Archives/edgar/data/1319161/000131916122000035/wmg-20220930.htm'),
 ('WMG_10K_FY2021.txt','https://www.sec.gov/Archives/edgar/data/1319161/000131916121000036/wmg-20210930.htm'),
]
for fn, u in J:
    if os.path.exists(fn): print('have', fn); continue
    t = strip_html(get(u))
    open(fn,'w',encoding='utf-8').write(t)
    print(fn, len(t))
