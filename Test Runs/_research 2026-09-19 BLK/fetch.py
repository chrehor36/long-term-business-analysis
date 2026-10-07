import sys, io, os, re, html as H
sys.path.insert(0,r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S

def grab(name, cik, acc, doc):
    a=acc.replace("-","")
    url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    raw=S._get(url, headers=S.SEC_UA, cache_name=f"doc_{name}")
    htm=raw.decode("utf-8","replace") if isinstance(raw,bytes) else raw
    io.open(name+".htm","w",encoding="utf-8").write(htm)
    t=re.sub(r"(?is)<(script|style).*?</\1>"," ",htm)
    t=re.sub(r"(?is)<br[^>]*>","\n",t)
    t=re.sub(r"(?is)</(p|div|tr|h[1-6]|li|table)>","\n",t)
    t=re.sub(r"(?is)</t[dh]>"," | ",t)
    t=re.sub(r"(?s)<[^>]+>"," ",t)
    t=H.unescape(t)
    t=re.sub(r"[ \t\xa0]+"," ",t)
    t=re.sub(r"\n *","\n",t)
    t=re.sub(r"\n{2,}","\n",t)
    io.open(name+".txt","w",encoding="utf-8").write(t)
    print(name, len(htm), len(t), url)

if __name__=="__main__":
    for row in [
     ("10K_FY2025","0002012383","0001193125-26-071966","blk-20251231.htm"),
     ("10Q_2026Q2","0002012383","0001193125-26-337177","blk-20260630.htm"),
     ("10K_FY2023_old","0001364742","0000950170-24-019271","blk-20231231.htm"),
    ]:
        grab(*row)
