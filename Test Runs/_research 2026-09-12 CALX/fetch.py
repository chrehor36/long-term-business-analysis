"""Fetch CALX primary documents from EDGAR into this folder as .htm and .txt.
Filing dumps are git-ignored by pattern; only analysis files get committed."""
import json, os, re, sys, time, html, functools
print = functools.partial(print, flush=True)
import urllib.request

CIK = 1406666
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
    "10K_FY2025": "0001406666-26-000005",
    "10K_FY2024": "0001406666-25-000008",
    "10K_FY2023": "0001406666-24-000012",
    "10K_FY2022": "0001406666-23-000026",
    "10K_FY2021": "0001628280-22-003338",
    "10K_FY2020": "0001406666-21-000029",
    "10K_FY2019": "0001406666-20-000018",
    "10K_FY2018": "0001406666-19-000029",
    "10K_FY2016": "0001406666-17-000012",
    "10K_FY2013": "0001406666-14-000039",
    "10K_FY2010": "0001193125-11-045511",
    "10Q_2026Q2": "0001406666-26-000034",
    "10Q_2026Q1": "0001406666-26-000019",
    "8K_20260720_Q2results": "0001406666-26-000028",
    "8K_20260421_Q1results": "0001406666-26-000017",
    "8K_20260421_item801": "0001406666-26-000016",
    "8K_20260128_Q4results": "0001406666-26-000004",
    "8K_20260128_item801": "0001406666-26-000003",
    "8K_20251117_502": "0001406666-25-000049",
    "8K_20251029_Q3results": "0001406666-25-000043",
    "8K_20250721_Q2results": "0001406666-25-000034",
    "8K_20250513_item801": "0001406666-25-000028",
    "8K_20250421_Q1results": "0001406666-25-000015",
    "8K_20250421_item801": "0001406666-25-000014",
    "8K_20250327_502": "0001406666-25-000010",
    "8K_20250129_Q4results": "0001406666-25-000001",
    "DEF14A_2026": "0001406666-26-000006",
    "DEF14A_2025": "0001406666-25-000011",
    "DEF14A_2017": "0001406666-17-000022",
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
    # LEAN: primary document plus EX-99 exhibits only; skip ex10/21/23/31/32/19/4 and filing-fee tables
    docs = [d for d in docs if not re.search(r"(?i)ex-?(10|21|23|31|32|19|4|97)|filingfees|xex(10|21|23|31|32|19|4|97)", d)]
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

