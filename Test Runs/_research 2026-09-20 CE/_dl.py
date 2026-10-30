import sys,os,subprocess,re,html
sys.path.insert(0,'.')
from _fetch import get
CIK='1306830'
def url(acc,doc):
    return f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
def totext(src,dst):
    raw=open(src,'rb').read().decode('utf-8','ignore')
    raw=re.sub(r'(?is)<(script|style).*?</\1>',' ',raw)
    raw=re.sub(r'(?is)<br[^>]*>','\n',raw)
    raw=re.sub(r'(?is)</(p|div|tr|h[1-6]|li)>','\n',raw)
    raw=re.sub(r'(?is)</t[dh]>',' | ',raw)
    raw=re.sub(r'(?s)<[^>]+>',' ',raw)
    raw=html.unescape(raw)
    raw=re.sub(r'[ \t\xa0]+',' ',raw)
    raw=re.sub(r'\n\s*\n+','\n',raw)
    open(dst,'w',encoding='utf-8').write(raw)
jobs=[
 ('0001306830-26-000031','ce-20251231.htm','fy2025_10k'),
 ('0001306830-26-000117','ce-20260630.htm','q2fy26_10q'),
 ('0001306830-26-000052','ce-20260304.htm','proxy_2026'),
 ('0001104659-26-090359','tm2622089d1_8k.htm','8k_20260804_item101'),
 ('0001306830-26-000119','ce-20260916.htm','8k_20260916'),
 ('0001104659-26-072110','tm2617385d1_8k.htm','8k_20260610'),
 ('0001306830-23-000023','ce-20221231.htm','fy2022_10k'),
]
for acc,doc,name in jobs:
    u=url(acc,doc)
    try:
        get(u,name+'.htm'); totext(name+'.htm',name+'.txt')
        print('OK',name,os.path.getsize(name+'.txt'))
    except SystemExit as e:
        print('FAIL',name,u)
