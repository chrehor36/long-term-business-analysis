import re,os,urllib.request,html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
def strip(h):
    h=h.decode('utf-8','replace')
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
    h=re.sub(r'(?is)</t[dh]>','\t',h); h=re.sub(r'(?is)</tr>','\n',h)
    h=re.sub(r'(?is)<[^>]+>','',h); h=html.unescape(h)
    h=re.sub(r'[ \u00a0]+',' ',h); h=re.sub(r'\n[ \t]+','\n',h); h=re.sub(r'\t[ ]+','\t',h)
    return re.sub(r'\n{3,}','\n\n',h)
for cik,acc,fy in [(789019,'0001193125-26-323660','FY2026'),(789019,'0000950170-23-035122','FY2023')]:
    a=acc.replace('-','');base=f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}"
    fs=get(base+"/FilingSummary.xml").decode('utf-8','replace')
    for r in re.findall(r'<Report[^>]*>(.*?)</Report>',fs,re.S):
        nm=re.search(r'<ShortName>(.*?)</ShortName>',r,re.S); fn=re.search(r'<HtmlFileName>(.*?)</HtmlFileName>',r,re.S)
        if not nm or not fn: continue
        n=html.unescape(nm.group(1)).strip()
        if re.search(r'(?i)cash flow',n) and not re.search(r'(?i)parenthetical',n):
            p=os.path.join(OUT,'stmts',f"MSFT_{fy}_"+re.sub(r'[^A-Za-z0-9]+','_',n)[:50]+".txt")
            open(p,'w',encoding='utf-8').write(f"SOURCE: {base}/{fn.group(1)}\nACCESSION: {acc}\nSTATEMENT: {n}\n\n"+strip(get(f"{base}/{fn.group(1)}")))
            print("saved",os.path.basename(p))
