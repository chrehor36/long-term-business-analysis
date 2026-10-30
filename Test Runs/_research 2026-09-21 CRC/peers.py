import json, os, re, sys, time, html, urllib.request, gzip, zlib

UA = {"User-Agent": "BRK research chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
OUT = os.path.dirname(os.path.abspath(__file__))
PEERS = {
    "BRY":  "0001705873",   # Berry Corporation (bry) - California heavy oil, last standalone 10-K
    "CVX":  "0000093410",   # Chevron - the "major international oil company which operate in California"
    "AMPY": "0001533924",   # Amplify Energy - offshore California (Beta) plus mid-continent
    "MTDR": "0001520006",   # Matador Resources - Delaware basin
    "MGY":  "0001698990",   # Magnolia Oil & Gas - Eagle Ford / Austin Chalk
    "OVV":  "0001792580",   # Ovintiv - multi-basin
    "CRGY": "0001866175",   # Crescent Energy - multi-basin conventional-weighted
}

def get(url, timeout=90):
    req = urllib.request.Request(url, headers=UA)
    for a in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = r.read()
                e = r.headers.get("Content-Encoding", "")
                if e == "gzip":
                    d = gzip.decompress(d)
                elif e == "deflate":
                    d = zlib.decompress(d)
                return d
        except Exception as ex:
            print("  retry", a, ex)
            time.sleep(3)
    raise SystemExit("failed " + url)

def totext(raw):
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|h[1-6]|li)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    lines = [l for l in t.split("\n") if not (len(l) > 400 and ("http://" in l or "us-gaap:" in l))]
    return "\n".join(lines)

def main():
    tick = sys.argv[1]
    cik = PEERS[tick]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 1   # how many 10-Ks back, 0 = newest
    sub = json.loads(get("https://data.sec.gov/submissions/CIK%s.json" % cik))
    r = sub["filings"]["recent"]
    hits = [(r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i])
            for i in range(len(r["form"])) if r["form"][i] == "10-K"]
    for h in hits[:4]:
        print(tick, h)
    d, acc, doc = hits[n]
    url = "https://www.sec.gov/Archives/edgar/data/%d/%s/%s" % (int(cik), acc.replace("-", ""), doc)
    print("fetching", url)
    txt = totext(get(url, 180))
    p = os.path.join(OUT, "peer_%s_10K_%s.txt" % (tick, d))
    open(p, "w", encoding="utf-8").write(txt)
    print("wrote", p, len(txt), "acc", acc, "filed", d)

main()
