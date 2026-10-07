from fetch_core import *
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
raw = get("https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm")
open("10Q_2026Q2_raw.htm","w",encoding="utf-8").write(raw)
for m in re.finditer(r'<ix:nonFraction[^>]*name="dei:EntityCommonStockSharesOutstanding"[^>]*>[^<]*', raw):
    print(m.group(0)[:400])
for cid in set(re.findall(r'name="dei:EntityCommonStockSharesOutstanding"[^>]*contextRef="([^"]+)"', raw) + re.findall(r'contextRef="([^"]+)"[^>]*name="dei:EntityCommonStockSharesOutstanding"', raw)):
    m = re.search(r'<xbrli:context id="%s">.*?</xbrli:context>' % re.escape(cid), raw, re.S)
    print(cid, re.sub(r"\s+"," ", m.group(0))[:600] if m else None)
