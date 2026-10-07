"""Fetch INOD primary documents from EDGAR into this folder as .htm and .txt.
Filing dumps are git-ignored by pattern; only analysis files get committed."""
import json, os, re, sys, time, html
import urllib.request

CIK = 903651
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}

def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            return data if binary else data.decode("utf-8", "replace")
        except Exception as e:
            print("  retry", attempt, url, e)
            time.sleep(2 + 2 * attempt)
    raise RuntimeError(url)

def strip_html(s):
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h\d|table|br)\s*>", "\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</t[dh]\s*>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = s.replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()

# label -> accession (with dashes)
FILINGS = {
    "10K_FY2025": "0001104659-26-020655",
    "10K_FY2024": "0001410578-25-000194",
    "10K_FY2023": "0001410578-24-000124",
    "10K_FY2022": "0001410578-23-000153",
    "10K_FY2021": "0001410578-22-000489",
    "10K_FY2020": "0001104659-21-035749",
    "10K_FY2019": "0001104659-20-034167",
    "10K_FY2018": "0001144204-19-015946",
    "10Q_2026Q2": "0001104659-26-092021",
    "10Q_2026Q1": "0001104659-26-057270",
    "8K_20260806_Q2results": "0001104659-26-092133",
    "8K_20260806_event0803": "0001104659-26-092010",
    "S3ASR_20260806": "0001104659-26-092086",
    "424B5_20260806": "0001104659-26-092131",
    "8K_20260617": "0001104659-26-075184",
    "8K_20260608": "0001104659-26-071384",
    "8K_20260507_Q1results": "0001104659-26-057150",
    "8K_20260324": "0001104659-26-033893",
    "8K_20260310": "0001104659-26-025739",
    "8K_20260226_Q4results": "0001104659-26-020514",
    "8K_20251107": "0001104659-25-108168",
    "8K_20251106_Q3results": "0001104659-25-107811",
    "8K_20250731_Q2results": "0001104659-25-072724",
    "8K_20250508_Q1results": "0001104659-25-046237",
    "8K_20250220_Q4results": "0001104659-25-015700",
    "8K_20241107_Q3results": "0001104659-24-115337",
    "8K_20240808_Q2results": "0001104659-24-087302",
    "8K_20240808_event0805": "0001104659-24-087285",
    "S3_20240808": "0001104659-24-087291",
    "8K_20240507_Q1results": "0001104659-24-058055",
    "8K_20240222_Q4results": "0001104659-24-026596",
    "8K_20240227": "0001104659-24-027981",
    "8K_20240313": "0001104659-24-033771",
    "8K_20231227": "0001104659-23-129734",
    "8K_20231017": "0001104659-23-109503",
    "DEF14A_2026": "0001104659-26-048201",
    "DEF14A_2025": "0001104659-25-039075",
    "10K_FY2013": "0001144204-14-015700",
    "10K_FY2016": "0001144204-17-014715",
}

def fetch_filing(label, acc):
    acc_nd = acc.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc_nd}/"
    idx = json.loads(get(base + "index.json"))
    items = idx["directory"]["item"]
    docs = [i["name"] for i in items if i["name"].lower().endswith((".htm", ".html", ".txt"))
            and not i["name"].lower().startswith(("r", "financial_report")) ]
    # keep primary docs + exhibits; skip R*.htm XBRL viewer pages and index
    docs = [d for d in docs if not re.match(r"(?i)^r\d+\.htm$", d) and "index" not in d.lower()]
    out = []
    for d in docs:
        raw = get(base + d)
        if len(raw) < 500:
            continue
        name = f"{label}__{d}"
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(raw)
        txt = strip_html(raw)
        with open(os.path.join(HERE, name.rsplit(".", 1)[0] + ".txt"), "w", encoding="utf-8") as f:
            f.write(txt)
        out.append((d, len(txt)))
        time.sleep(0.15)
    print(label, acc, out)

if __name__ == "__main__":
    only = sys.argv[1:]  # optional labels
    cf = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK:010d}.json")
    with open(os.path.join(HERE, f"companyfacts_{CIK}.json"), "w", encoding="utf-8") as f:
        f.write(cf)
    print("companyfacts", len(cf))
    for label, acc in FILINGS.items():
        if only and label not in only:
            continue
        try:
            fetch_filing(label, acc)
        except Exception as e:
            print("FAILED", label, e)

