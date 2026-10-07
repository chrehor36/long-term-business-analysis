import json,re,os,sys,urllib.request,html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
def strip(h):
    h=h.decode('utf-8','replace')
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
    h=re.sub(r'(?is)</t[dh]>','\t',h)
    h=re.sub(r'(?is)</tr>','\n',h)
    h=re.sub(r'(?is)<[^>]+>','',h)
    h=html.unescape(h)
    h=re.sub(r'[ \u00a0]+',' ',h)
    h=re.sub(r'\n[ \t]+','\n',h); h=re.sub(r'\t[ ]+','\t',h)
    h=re.sub(r'\n{3,}','\n\n',h)
    return h
TARGETS=[
 ('CRWD',1535527,'0001535527-26-000010','FY2026'),
 ('CRWD',1535527,'0001535527-23-000008','FY2023'),
 ('PANW',1327567,'0001327567-25-000027','FY2025'),
 ('PANW',1327567,'0001327567-22-000028','FY2022'),
 ('S',1583708,'0001583708-26-000020','FY2026'),
 ('S',1583708,'0001583708-23-000014','FY2023'),
 ('FTNT',1262039,'0001262039-26-000007','FY2025'),
 ('FTNT',1262039,'0001262039-23-000010','FY2022'),
 ('MSFT',789019,'0001193125-26-323660','FY2026'),
 ('MSFT',789019,'0000950170-23-035122','FY2023'),
]
WANT=re.compile(r'(?i)(statements? of operations|statements? of income|income statements?|balance sheets?|statements? of cash flows|financial position)')
SKIP=re.compile(r'(?i)(parenthetical|comprehensive)')
os.makedirs(os.path.join(OUT,'stmts'),exist_ok=True)
for tick,cik,acc,fy in TARGETS:
    a=acc.replace('-','')
    base=f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}"
    fs=get(base+"/FilingSummary.xml").decode('utf-8','replace')
    reps=re.findall(r'<Report[^>]*>(.*?)</Report>',fs,re.S)
    picked=[]
    for r in reps:
        nm=re.search(r'<ShortName>(.*?)</ShortName>',r,re.S)
        fn=re.search(r'<HtmlFileName>(.*?)</HtmlFileName>',r,re.S)
        if not nm or not fn: continue
        n=html.unescape(nm.group(1)).strip()
        if WANT.search(n) and not SKIP.search(n):
            picked.append((n,fn.group(1).strip()))
    print(f"--- {tick} {fy} {acc}")
    for n,f in picked[:6]:
        try:
            t=strip(get(f"{base}/{f}"))
        except Exception as e:
            print("   ERR",n,e); continue
        safe=re.sub(r'[^A-Za-z0-9]+','_',n)[:60]
        p=os.path.join(OUT,'stmts',f"{tick}_{fy}_{safe}.txt")
        open(p,'w',encoding='utf-8').write(f"SOURCE: {base}/{f}\nACCESSION: {acc}\nSTATEMENT: {n}\n\n"+t)
        print(f"   saved {os.path.basename(p)}")
