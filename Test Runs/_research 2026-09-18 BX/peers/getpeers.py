import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get, strip, grab
import fetch_core
HERE = os.path.dirname(os.path.abspath(__file__))
fetch_core.HERE = HERE
P = {
 "KKR": (1404912, "0001404912-26-000007", "kkr-20251231.htm"),
 "APO": (1858681, "0001858681-26-000013", "apo-20251231.htm"),
 "CG":  (1527166, "0001527166-26-000009", "cg-20251231.htm"),
 "ARES":(1176948, "0001628280-26-011413", "ares-20251231.htm"),
 "OWL": (1823945, "0001823945-26-000009", "owl-20251231.htm"),
 "TPG": (1880661, "0001880661-26-000011", "tpg-20251231.htm"),
 "BLK": (2012383, "0001193125-26-071966", "blk-20251231.htm"),
 "TROW":(1113169, "0001628280-26-008002", "trow-20251231.htm"),
}
for k,(cik,acc,doc) in P.items():
    try: grab(acc, doc, k + "_10K_FY2025", cik=cik)
    except Exception as e: print("FAIL", k, e)
# BAM: find the primary doc from the index
a = "0001628280-26-013098".replace("-","")
idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/1937926/{a}/index.json"))
docs = [i["name"] for i in idx["directory"]["item"] if i["name"].endswith(".htm")]
print("BAM docs", docs[:8])
