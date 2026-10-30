from fetch_core import *
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
for acc, doc, name in [("0001792789-26-000050","dash-20260630.htm","10Q_2026Q2"),("0001792789-26-000013","dash-20251231.htm","10K_FY2025"),("0001792789-26-000035","dash-20251231.htm","10KA_FY2025")]:
    a = acc.replace("-","")
    raw = get(f"https://www.sec.gov/Archives/edgar/data/1792789/{a}/{doc}")
    open(name+"_raw.htm","w",encoding="utf-8").write(raw)
    open(name+".txt","w",encoding="utf-8").write(strip(raw))
    print("=====", name, acc, len(raw))
    for m in re.finditer(r'<ix:nonFraction[^>]*name="dei:EntityCommonStockSharesOutstanding"[^>]*>[^<]*', raw):
        s = m.group(0); cid = re.search(r'contextRef="([^"]+)"', s).group(1)
        c = re.search(r'<xbrli:context id="%s">.*?</xbrli:context>' % re.escape(cid), raw, re.S)
        print(re.sub(r"\s+"," ",s)[-120:], "|", re.sub(r"\s+"," ", c.group(0))[:500] if c else None)
    time.sleep(0.5)
