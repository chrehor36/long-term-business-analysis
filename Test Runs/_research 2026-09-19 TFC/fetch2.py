"""TFC (Truist Financial Corporation, CIK 0000092230) - fetch primary documents.

Written 2026-09-19, the fourth bank this project has run. Pattern copied from
`Test Runs/_research 2026-09-19 CCB/fetch.py`. sec.gov/Archives answers 403 to the
default Mozilla agent, so every request carries sources.SEC_UA.
"""
import sys, os, re, json, urllib.request, html, time

sys.path.insert(0, os.path.join("C:/Users/chreh/OneDrive/Documents/BRK", "tools"))
import sources

D = os.path.dirname(os.path.abspath(__file__))
CIK = "92230"

DOCS = [
    ("tenk_FY2025", "0000092230-26-000030", "tfc-20251231.htm"),
    ("tenk_FY2024", "0000092230-25-000020", "tfc-20241231.htm"),
    ("tenk_FY2023", "0000092230-24-000010", "tfc-20231231.htm"),
    ("tenk_FY2022", "0000092230-23-000034", "tfc-20221231.htm"),
    ("tenk_FY2021", "0000092230-22-000008", "tfc-20211231.htm"),
    ("tenk_FY2020", "0000092230-21-000032", "tfc-20201231.htm"),
    ("tenq_2026Q2", "0000092230-26-000099", "tfc-20260630.htm"),
    ("tenq_2026Q1", "0000092230-26-000062", "tfc-20260331.htm"),
    ("proxy_2026", "0001193125-26-107144", "d12240ddef14a.htm"),
    ("proxy_2025", "0001193125-25-055156", "d826258ddef14a.htm"),
    ("proxy_2020", "0001193125-21-081387", "d26214ddef14a.htm"),
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
    open(out, "w", encoding="utf-8").write(totext(raw))
    print("wrote", name, len(raw))
    time.sleep(0.3)


def fetch_ex99(acc, label):
    a = acc.replace("-", "")
    idx = json.loads(get(
        "https://www.sec.gov/Archives/edgar/data/%s/%s/index.json" % (CIK, a)
    ).decode())
    found = False
    for it in idx["directory"]["item"]:
        n = it["name"]
        if n.endswith(".htm") and re.search(r"ex-?x?99", n.lower()):
            raw = get("https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (CIK, a, n))
            tag = re.search(r"99[._-]?(\d)", n)
            suffix = tag.group(1) if tag else "x"
            open(os.path.join(D, "EX99%s_%s.txt" % (suffix, label)), "w",
                 encoding="utf-8").write(totext(raw))
            print("wrote EX99", label, n, len(raw))
            found = True
            time.sleep(0.3)
    if not found:
        print("no ex99 in", acc, [i["name"] for i in idx["directory"]["item"]])


if __name__ == "__main__":
    for t in DOCS:
        fetch_doc(*t)
