import json, re, sys, time, os, html
import requests

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
HERE = os.path.dirname(os.path.abspath(__file__))
CIKS = {"GM": 1467858, "F": 37996, "TSLA": 1318605, "HMC": 715153, "STLA": 1605484}


def get(url):
    time.sleep(0.25)
    r = requests.get(url, headers=UA, timeout=120)
    r.raise_for_status()
    return r


def strip(h):
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d|table)>", "\n", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h


def listing():
    out = []
    for t, c in CIKS.items():
        p = os.path.join(HERE, t + "_submissions.json")
        if not os.path.exists(p):
            open(p, "wb").write(get("https://data.sec.gov/submissions/CIK%010d.json" % c).content)
        j = json.load(open(p))
        r = j["filings"]["recent"]
        for i, f in enumerate(r["form"]):
            if f in ("10-K", "20-F", "10-K/A", "20-F/A"):
                out.append("%s %s fd=%s rd=%s acc=%s doc=%s" % (t, f, r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]))
    print("\n".join(out))


def fetch(t, acc, doc, name):
    c = CIKS[t]
    url = "https://www.sec.gov/Archives/edgar/data/%d/%s/%s" % (c, acc.replace("-", ""), doc)
    txt = strip(get(url).text)
    open(os.path.join(HERE, name), "w", encoding="utf-8").write("SOURCE URL: " + url + "\nACCESSION: " + acc + "\n\n" + txt)
    print(name, len(txt))


if __name__ == "__main__":
    if sys.argv[1] == "list":
        listing()
    else:
        fetch(*sys.argv[2:6]) if sys.argv[1] == "get" else None
