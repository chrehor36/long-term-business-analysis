from fetch_core import *
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
for acc, doc, name in [("0001828972-26-000138","bzfd-20260630.htm","10Q_2026Q2"),("0001828972-26-000030","bzfd-20251231.htm","10K_FY2025"),("0001828972-26-000056","bzfd-20260331.htm","10Q_2026Q1")]:
    a = acc.replace("-","")
    raw = get(f"https://www.sec.gov/Archives/edgar/data/1828972/{a}/{doc}")
    open(name+"_raw.htm","w",encoding="utf-8").write(raw)
    print("=====", name, acc, len(raw))
    for m in re.finditer(r'<ix:non(?:Fraction|Numeric)[^>]*name="dei:(EntityCommonStockSharesOutstanding|EntityPublicFloat)"[^>]*>[^<]*', raw):
        s = m.group(0); cid = re.search(r'contextRef="([^"]+)"', s).group(1)
        c = re.search(r'<xbrli:context id="%s">.*?</xbrli:context>' % re.escape(cid), raw, re.S)
        print(re.sub(r"\s+"," ",s)[-300:], "|", re.sub(r"\s+"," ", c.group(0))[:600] if c else None)
    time.sleep(0.5)
