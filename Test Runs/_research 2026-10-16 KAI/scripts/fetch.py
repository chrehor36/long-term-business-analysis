import sys, json, urllib.request, gzip, re, os, html, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        b = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            b = gzip.decompress(b)
    time.sleep(0.2)
    return b
def h2t(b):
    s = b.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        cik = sys.argv[2]
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
        r = d["filings"]["recent"]
        forms = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        for i in range(len(r["form"])):
            if forms and r["form"][i] not in forms: continue
            print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items",[""]*9999)[i])
        for f in d["filings"].get("files", []): print("OLDER", f["name"], f["filingFrom"], f["filingTo"])
    elif cmd == "doc":
        cik, acc, doc, name = sys.argv[2:6]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        b = get(url)
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(h2t(b))
        print("wrote", name, len(b))
    elif cmd == "older":
        d = json.loads(get("https://data.sec.gov/submissions/" + sys.argv[2]))
        forms = sys.argv[3].split(",")
        for i in range(len(d["form"])):
            if d["form"][i] in forms: print(d["filingDate"][i], d["form"][i], d["accessionNumber"][i], d["primaryDocument"][i])
