import sys, os, re, json, urllib.request, html, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(url):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read()
        except Exception as e: last=e; time.sleep(2*(i+1))
    raise last
def strip(h):
    h=h.decode('utf-8','replace')
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
    h=re.sub(r'(?is)<br\s*/?>','\n',h)
    h=re.sub(r'(?is)</(p|div|tr|h1|h2|h3|h4|li|table)>','\n',h)
    h=re.sub(r'(?is)</t[dh]>','\t',h)
    h=re.sub(r'(?is)<[^>]+>',' ',h)
    h=html.unescape(h)
    h=re.sub(r'[ \u00a0]+',' ',h)
    h=re.sub(r'\n[ \t]+','\n',h)
    h=re.sub(r'\n{3,}','\n\n',h)
    return h
def fetch(cik, acc, doc, name):
    a=acc.replace('-','')
    p=os.path.join(OUT,name)
    if os.path.exists(p) and os.path.getsize(p)>1000: print('have',name); return
    raw=get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}")
    open(p,'w',encoding='utf-8').write(strip(raw)); print(name, os.path.getsize(p))
def ex99(cik, acc, name):
    a=acc.replace('-','')
    idx=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/index.json"))
    for it in idx['directory']['item']:
        n=it['name'].lower()
        if 'ex99' in n or 'ex-99' in n or 'exhibit99' in n:
            if n.endswith('.htm'):
                fetch(cik,acc,it['name'],name); return
    print('no ex99 in',acc,[it['name'] for it in idx['directory']['item']])
C=1321655
jobs=[
 ('0001321655-26-000011','pltr-20251231.htm','10K_FY2025.txt'),
 ('0001321655-25-000022','pltr-20241231.htm','10K_FY2024.txt'),
 ('0001321655-24-000022','pltr-20231231.htm','10K_FY2023.txt'),
 ('0001321655-23-000011','pltr-20221231.htm','10K_FY2022.txt'),
 ('0001193125-22-050913','d273589d10k.htm','10K_FY2021.txt'),
 ('0001193125-21-060650','d65934d10k.htm','10K_FY2020.txt'),
 ('0001321655-26-000041','pltr-20260630.htm','10Q_2026Q2.txt'),
 ('0001321655-26-000028','pltr-20260331.htm','10Q_2026Q1.txt'),
 ('0001321655-25-000106','pltr-20250630.htm','10Q_2025Q2.txt'),
 ('0001321655-26-000019','pltr-20260423.htm','DEF14A_2026.txt'),
 ('0001321655-25-000057','pltr-20250424.htm','DEF14A_2025.txt'),
 ('0001193125-20-250103','d904406ds1a.htm','S1A_2020.txt'),
]
for acc,doc,name in jobs:
    try: fetch(C,acc,doc,name)
    except Exception as e: print('ERR',name,e)
for acc,name in [('0001321655-26-000039','8K_EX991_2026Q2.txt'),('0001321655-26-000004','8K_EX991_2025Q4.txt'),('0001321655-26-000026','8K_EX991_2026Q1.txt')]:
    try: ex99(C,acc,name)
    except Exception as e: print('ERR',name,e)
