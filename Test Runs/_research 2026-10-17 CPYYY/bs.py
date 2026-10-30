# pull key balance-sheet lines (current year column) from each report's Group Balance Sheet page
import sys, re, pymupdf, subprocess
pages={2018:129,2019:119,2020:105,2021:117,2022:126,2023:132,2024:172,2025:139}
keys=['Goodwill','Other intangible assets','Interests in joint ventures','Property, plant and equipment','Inventories','Cash and cash equivalents','Trade and other receivables','Derivative financial instruments','Bank overdrafts, loans','Bank loans and other borrowings','Provisions for other liabilities','Retirement benefit obligations','Total assets','Total liabilities','Net assets','Retained earnings','Share premium','Total shareholders']
for y,p in pages.items():
    out=subprocess.run([sys.executable,'-P','pg.py',f'cache/AR{y}.pdf',str(p)],capture_output=True,text=True,encoding='utf-8').stdout
    print('=====',y)
    for line in out.splitlines():
        for k in keys:
            if line.strip().startswith(k):
                print('  ',re.sub(r'\s{2,}',' | ',line.strip())[:140]); break
