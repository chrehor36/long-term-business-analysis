import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import edgar
BASE = os.path.dirname(os.path.abspath(__file__))
ACC = '000162828026017045'
CIK = 1453015
DOCS = {'ballard993123125annualinfo.htm': 'BLDP_EX99-3_AIF_2025.txt',
        'ballard40-f992123125mda.htm': 'BLDP_EX99-2_MDA_2025.txt',
        'bldp-20251231.htm': 'BLDP_EX99-1_FS_2025.txt'}
for src, dest in DOCS.items():
    u = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{ACC}/{src}'
    try:
        txt = edgar.strip_html(edgar.get(u))
    except Exception as e:
        print('FAILED', src, e); continue
    p = os.path.join(BASE, dest)
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(f'SOURCE: BLDP 40-F acc=0001628280-26-017045 exhibit doc={src}\nURL: {u}\n\n' + txt)
    print('wrote', dest, len(txt))
