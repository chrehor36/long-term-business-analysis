import sys, os, re, html
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?i)<br\s*/?>','\n',h)
    h=re.sub(r'(?i)</(p|div|tr|h\d|li)>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h)
    h=h.replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
def grab(name,url):
    p=name
    if os.path.exists(p) and os.path.getsize(p)>0: print('have',name); return
    t=totext(get(url))
    open(p,'w',encoding='utf-8').write(t); print('saved',name,len(t))
if __name__=='__main__':
    B='https://www.sec.gov/Archives/edgar/data/1581990/'
    jobs=[
      ('10K_FY2025.txt','000158199026000012/pagp-20251231.htm'),
      ('10Q_2026Q2.txt','000158199026000025/pagp-20260630.htm'),
      ('8K_20260914.txt','000110465926107550/tm2625147d1_8k.htm'),
      ('8K_20260914_EX991.txt','000110465926107550/tm2625147d1_ex99-1.htm'),
      ('8K_20260807.txt','000158199026000023/pagp-20260807.htm'),
      ('8K_20260807_EX991.txt','000158199026000023/pagp08072026exhibit991.htm'),
      ('8K_20260512.txt','000110465926059512/tm2614304d1_8k.htm'),
      ('8K_20260512_EX991.txt','000110465926059512/tm2614304d1_ex99-1.htm'),
      ('8K_20260303.txt','000110465926022839/tm267811d1_8k.htm'),
      ('8K_20260617.txt','000110465926075189/tm2618136d1_8k.htm'),
    ]
    for n,u in jobs:
        try: grab(n,B+u)
        except Exception as e: print('FAIL',n,e)
