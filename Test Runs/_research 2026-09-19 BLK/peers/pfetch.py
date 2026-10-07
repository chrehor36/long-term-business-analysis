import sys, os, json, re
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S

HERE = os.path.dirname(os.path.abspath(__file__))

def sub(ticker):
    cik, title = S.cik_for(ticker)
    n = int(cik)
    raw = S._get("https://data.sec.gov/submissions/CIK%010d.json" % n,
                 headers=S.SEC_UA, cache_name="sub_%s.json" % ticker.lower(), max_age_h=240)
    return n, json.loads(raw)

def recent(ticker, forms=("10-K",), limit=12):
    n, d = sub(ticker)
    r = d["filings"]["recent"]
    out=[]
    for i in range(len(r["form"])):
        if r["form"][i] in forms:
            out.append(dict(form=r["form"][i], fdate=r["filingDate"][i],
                            period=r.get("reportDate",[None]*99)[i],
                            acc=r["accessionNumber"][i], doc=r["primaryDocument"][i]))
    return n, d.get("name"), out[:limit]

def doc_url(n, acc, doc):
    return "https://www.sec.gov/Archives/edgar/data/%d/%s/%s" % (n, acc.replace("-",""), doc)

def grab(ticker, n, acc, doc, tag):
    url = doc_url(n, acc, doc)
    path = os.path.join(HERE, "%s_%s.htm" % (ticker, tag))
    if not os.path.exists(path):
        raw = S._get(url, headers=S.SEC_UA, cache_name="doc_%s_%s" % (ticker, tag), max_age_h=100000, binary=True)
        open(path,"wb").write(raw)
    return path, url

if __name__=="__main__":
    for t in sys.argv[1:]:
        n, name, fl = recent(t)
        print("===", t, n, name)
        for f in fl: print("   ", f["form"], f["fdate"], f["period"], f["acc"], f["doc"])
