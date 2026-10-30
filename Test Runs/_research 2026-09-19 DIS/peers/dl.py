import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfetch import grab

JOBS = [
    # (cik, accession, primary doc, outfile)
    ('1166691', '0001628280-26-004994', 'cmcsa-20251231.htm', 'CMCSA_10K_FY2025.txt'),
    ('1166691', '0001166691-25-000011', 'cmcsa-20241231.htm', 'CMCSA_10K_FY2024.txt'),
    ('1166691', '0001166691-24-000011', 'cmcsa-20231231.htm', 'CMCSA_10K_FY2023.txt'),
    ('1999001', '0001999001-26-000048', 'fun-20251231.htm', 'FUN_10K_FY2025.txt'),
    ('1999001', '0001999001-25-000052', 'fun-20241231.htm', 'FUN_10K_FY2024.txt'),
    ('1564902', '0001193125-26-088288', 'prks-20251231.htm', 'PRKS_10K_FY2025.txt'),
    ('1564902', '0000950170-25-030398', 'prks-20241231.htm', 'PRKS_10K_FY2024.txt'),
    ('1754301', '0001628280-26-053960', 'fox-20260630.htm', 'FOXA_10K_FY2026.txt'),
    ('1754301', '0001628280-25-038077', 'fox-20250630.htm', 'FOXA_10K_FY2025.txt'),
    ('1437107', '0001437107-26-000020', 'wbd-20251231.htm', 'WBD_10K_FY2025.txt'),
    ('1091667', '0001091667-26-000017', 'chtr-20251231.htm', 'CHTR_10K_FY2025.txt'),
    ('1415404', '0001104659-26-021817', 'tmb-20251231x10k.htm', 'ECHO_10K_FY2025.txt'),
    ('1484769', '0001628280-25-009420', 'fubo-20241231.htm', 'FUBO_10K_FY2024.txt'),
]
for cik, acc, doc, out in JOBS:
    try:
        grab(cik, acc, doc, out)
    except Exception as e:
        print('FAIL', out, e)
