import sys, os, re, json, html, time
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

RES = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 SWK"
CIK = "93556"

WANT = [
    ("10K_FY2025", "0000093556-26-000009"),
    ("10Q_FY2026Q2", "0000093556-26-000031"),
    ("10Q_FY2026Q1", "0000093556-26-000015"),
    ("10K_FY2024", "0000093556-25-000007"),
    ("10K_FY2023", "0000093556-24-000032"),
    ("10K_FY2022", "0000093556-23-000007"),
    ("10K_FY2021", "0000093556-22-000015"),
    ("10K_FY2019", "0000093556-20-000010"),
    ("10K_FY2017", "0000093556-18-000009"),
]


def strip(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?is)<br[^>]*>", "\n", h)
    h = re.sub(r"(?is)</(p|div|tr|td|th|li|h[1-6]|table)>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h


def get_index(acc):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json"
    return json.loads(sources._get(url, sources.SEC_UA, f"idx_{a}.json", max_age_h=999))


for name, acc in WANT:
    try:
        idx = get_index(acc)
    except Exception as e:
        print("INDEX FAIL", name, acc, type(e).__name__, e)
        continue
    a = acc.replace("-", "")
    items = idx["directory"]["item"]
    mains = [i["name"] for i in items
             if i["name"].lower().endswith((".htm", ".txt"))
             and not i["name"].lower().endswith(("-index.htm", "_cal.xml"))
             and "ex" not in i["name"].lower()[:3]]
    # pick largest htm
    cand = sorted([i for i in items if i["name"].lower().endswith(".htm")],
                  key=lambda i: -int(i["size"]))
    if not cand:
        print("NO HTM", name)
        continue
    fn = cand[0]["name"]
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{fn}"
    txt = sources._get(url, sources.SEC_UA, f"doc_{a}_{fn}", max_age_h=99999)
    out = os.path.join(RES, name + ".txt")
    open(out, "w", encoding="utf-8").write(strip(txt))
    print(f"{name:16s} {fn:40s} {len(txt):>10,} html -> {os.path.getsize(out):>9,} txt")
    time.sleep(0.3)
