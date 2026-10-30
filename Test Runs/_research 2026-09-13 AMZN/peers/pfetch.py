import sys, os, re, urllib.request, time
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "Test Runs", "_research 2026-09-13 AMZN"))
import sources
import fetch as F
HERE = os.path.dirname(os.path.abspath(__file__))
F.OUT = HERE

def index_docs(cik, acc):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{acc}-index.htm"
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    return re.findall(r'href="/Archives/edgar/data/\d+/\d+/([^"]+)"', raw)

JOBS = [
    (1652044, "0001652044-26-000071", "goog-20260630.htm", "GOOGL_10Q_2026Q2"),
    (1326801, "0001628280-26-003942", "meta-20251231.htm", "META_10K_FY2025"),
    (1326801, "0001628280-26-050705", "meta-20260630.htm", "META_10Q_2026Q2"),
    (1065088, "0001065088-26-000027", "ebay-20251231.htm", "EBAY_10K_FY2025"),
    (1065088, "0001065088-26-000177", "ebay-20260630.htm", "EBAY_10Q_2026Q2"),
    (1099590, "0001099590-26-000006", "meli-20251231.htm", "MELI_10K_FY2025"),
    (1099590, "0001099590-26-000023", "meli-20260630.htm", "MELI_10Q_2026Q2"),
    (1737806, "0001104659-26-050727", "pdd-20251231x20f.htm", "PDD_20F_FY2025"),
    (1594805, "0001594805-26-000007", "shop-20251231.htm", "SHOP_10K_FY2025"),
    (1594805, "0001594805-26-000047", "shop-20260630.htm", "SHOP_10Q_2026Q2"),
    (1341439, "0001193125-26-389274", "orcl-20260831.htm", "ORCL_10Q_FY2027Q1"),
]
if __name__ == "__main__":
    for cik, acc, doc, name in JOBS:
        try:
            F.grab(cik, acc, doc, name)
        except Exception as e:
            print("FAIL", name, e)
        time.sleep(0.4)
    for acc in ["0001104659-26-100534", "0001104659-26-099679", "0001104659-26-067186"]:
        try:
            print(acc, index_docs(1737806, acc))
        except Exception as e:
            print("FAIL idx", acc, e)
        time.sleep(0.3)
