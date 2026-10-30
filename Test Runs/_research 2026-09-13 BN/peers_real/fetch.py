"""Fetch SEC filings as text. Usage:
  python fetch.py list CIK FORM[,FORM]        -> list filings of those forms
  python fetch.py get CIK ACCESSION FILE OUT  -> download doc, strip HTML to text OUT
  python fetch.py idx CIK ACCESSION           -> list files in filing
"""
import urllib.request, json, sys, re, html, os, time, gzip

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
HERE = os.path.dirname(os.path.abspath(__file__))


def get(u):
    for k in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                b = gzip.decompress(b)
            time.sleep(0.2)
            return b
        except Exception as e:
            print("retry", k, e, file=sys.stderr)
            time.sleep(2 + 3 * k)
    raise SystemExit("failed " + u)


def to_text(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)</(p|div|tr|br|h\d|li|table)>|<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


cmd = sys.argv[1]
if cmd == "list":
    cik = sys.argv[2].zfill(10)
    forms = sys.argv[3].split(",")
    d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
    r = d["filings"]["recent"]
    print(d["name"])
    for i in range(len(r["form"])):
        if r["form"][i] in forms:
            print(r["form"][i], r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i])
elif cmd == "idx":
    cik = str(int(sys.argv[2]))
    a = sys.argv[3].replace("-", "")
    j = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json"))
    for it in j["directory"]["item"]:
        print(it["name"], it.get("size"))
elif cmd == "get":
    cik = str(int(sys.argv[2]))
    a = sys.argv[3].replace("-", "")
    b = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{sys.argv[4]}")
    t = to_text(b)
    open(os.path.join(HERE, sys.argv[5]), "w", encoding="utf-8").write(t)
    print("wrote", sys.argv[5], len(t))
