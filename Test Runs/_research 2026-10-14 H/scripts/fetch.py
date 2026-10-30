"""Fetch SEC filings for a CIK into cache/ (gitignored). Usage: fetch.py list CIK | fetch.py get URL OUTNAME"""
import sys, json, os, re, time, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(os.path.dirname(HERE), "cache")
os.makedirs(CACHE, exist_ok=True)

def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            print("retry", i, e, file=sys.stderr); time.sleep(2 + 3 * i)
    raise SystemExit("failed " + url)

def to_text(b):
    s = b.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "list":
        cik = sys.argv[2].zfill(10)
        forms = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
        open(os.path.join(CACHE, f"sub_{cik}.json"), "wb").write(json.dumps(d).encode())
        r = d["filings"]["recent"]
        for i in range(len(r["form"])):
            if forms and r["form"][i] not in forms: continue
            print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""]*9999)[i], r["reportDate"][i])
    elif cmd == "get":
        url, out = sys.argv[2], sys.argv[3]
        b = get(url)
        p = os.path.join(CACHE, out)
        if url.endswith(".htm") or url.endswith(".html"):
            open(p, "w", encoding="utf-8").write(to_text(b))
        else:
            open(p, "wb").write(b)
        print(p, os.path.getsize(p))
