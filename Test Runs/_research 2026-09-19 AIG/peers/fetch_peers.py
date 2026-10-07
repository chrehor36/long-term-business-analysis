import sys, os
sys.path.insert(0, os.path.abspath('tools')); sys.path.insert(0, os.path.abspath('Test Runs/_research 2026-09-19 AIG'))
import sources
from fetch import strip
D = os.path.abspath('Test Runs/_research 2026-09-19 AIG/peers')
for cik, acc, doc, out in [
    ('86312', '0000086312-26-000065', 'trv-20251231.htm', 'TRV_10K_2025.txt'),
    ('86312', '0000086312-24-000012', 'trv-20231231.htm', 'TRV_10K_2023.txt'),
    ('874766', '0000874766-26-000012', 'hig-20251231.htm', 'HIG_10K_2025.txt'),
    ('874766', '0000874766-24-000016', 'hig-20231231.htm', 'HIG_10K_2023.txt'),
]:
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (cik, acc.replace('-', ''), doc)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='aigpeer_' + out, max_age_h=999)
    if not isinstance(raw, str): raw = raw.decode('utf-8', 'replace')
    open(os.path.join(D, out), 'w', encoding='utf-8').write(strip(raw)); print(out, len(raw))
