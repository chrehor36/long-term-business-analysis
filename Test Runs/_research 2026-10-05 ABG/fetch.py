import warnings; warnings.filterwarnings("ignore")
import sys, os, time, urllib.request, re, html
UA="Chris Hrehor chrehor36@gmail.com"
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Encoding":"identity"})
    for k in range(4):
        try:
            return urllib.request.urlopen(req,timeout=60).read()
        except Exception as e:
            print("retry",e); time.sleep(2)
    raise SystemExit("fail "+url)
def totext(b):
    from bs4 import BeautifulSoup
    s=BeautifulSoup(b,"lxml")
    for t in s(["script","style"]): t.decompose()
    # table rows to lines with | separators
    for tr in s.find_all("tr"):
        cells=[c.get_text(" ",strip=True) for c in tr.find_all(["td","th"])]
        cells=[c for c in cells if c]
        tr.replace_with(s.new_string("\n"+" | ".join(cells)+"\n"))
    t=s.get_text("\n")
    t=re.sub(r"\n\s*\n+","\n",t)
    return t
cik, acc, doc, out = sys.argv[1:5]
url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
b=get(url)
open(out,"w",encoding="utf-8").write(totext(b))
print(out, len(b))
