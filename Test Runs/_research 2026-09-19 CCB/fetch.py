"""CCB (Coastal Financial Corporation, CIK 0001437958) - fetch primary documents.

Written 2026-09-19 for the first bank run in this project. Downloads the primary
document of each named accession, strips tags to text, and writes both the raw
HTML and a text rendering into this directory.
"""
import sys, os, re, json, urllib.request, html, time

sys.path.insert(0, os.path.join("C:/Users/chreh/OneDrive/Documents/BRK", "tools"))
import sources

D = os.path.dirname(os.path.abspath(__file__))
CIK = "1437958"

DOCS = [
    ("tenk_FY2025", "0001437958-26-000013", "ck1437958-20251231.htm"),
    ("tenk_FY2024", "0001437958-25-000058", "ck1437958-20241231.htm"),
    ("tenk_FY2023", "0001437958-24-000052", "ck1437958-20231231.htm"),
    ("tenk_FY2022", "0001437958-23-000051", "ck1437958-20221231.htm"),
    ("tenk_FY2021", "0001564590-22-009970", "ck1437958-10k_20211231.htm"),
    ("tenk_FY2020", "0001564590-21-012709", "ck1437958-10k_20201231.htm"),
    ("tenq_2026Q2", "0001437958-26-000061", "ck1437958-20260630.htm"),
    ("proxy_2026", "0001437958-26-000023", "ck1437958-20260410.htm"),
]


def get(url):
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    return urllib.request.urlopen(req).read()


def totext(raw):
    s = raw.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style|ix:header)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)</(p|div|tr|table|h[1-6]|li)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = s.replace("\u00a0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n[ \t]*\n+", "\n", s)
    return s


def fetch_doc(name, acc, doc):
    a = acc.replace("-", "")
    url = "https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (CIK, a, doc)
    out = os.path.join(D, name + ".txt")
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        print("have", name)
        return
    raw = get(url)
    open(os.path.join(D, name + ".htm"), "wb").write(raw)
    open(out, "w", encoding="utf-8").write(totext(raw))
    print("wrote", name, len(raw))
    time.sleep(0.3)


def fetch_ex99(acc, label):
    """Earnings release exhibit EX-99.1 from an 8-K, for [E4-29] / [E4-22] flag 3."""
    a = acc.replace("-", "")
    idx = json.loads(get(
        "https://www.sec.gov/Archives/edgar/data/%s/%s/index.json" % (CIK, a)
    ).decode())
    for it in idx["directory"]["item"]:
        n = it["name"]
        if n.endswith(".htm") and re.search(r"ex-?x?99", n.lower()):
            raw = get("https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (CIK, a, n))
            open(os.path.join(D, "EX99_%s.txt" % label), "w",
                 encoding="utf-8").write(totext(raw))
            print("wrote EX99", label, n, len(raw))
            time.sleep(0.3)
            return
    print("no ex99 in", acc, [i["name"] for i in idx["directory"]["item"]])


if __name__ == "__main__":
    for t in DOCS:
        fetch_doc(*t)
    # earnings 8-Ks: the two filed on each results day; both are tried
    for acc, label in [("0001437958-26-000052", "2026Q2"),
                       ("0001437958-26-000053", "2026Q2b"),
                       ("0001437958-26-000031", "2026Q1"),
                       ("0001437958-26-000032", "2026Q1b"),
                       ("0001437958-26-000004", "2025Q4"),
                       ("0001437958-26-000005", "2025Q4b"),
                       ("0001437958-25-000164", "2025Q3"),
                       ("0001437958-25-000165", "2025Q3b")]:
        try:
            fetch_ex99(acc, label)
        except Exception as e:
            print("fail", acc, e)
