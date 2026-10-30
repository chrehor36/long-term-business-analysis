"""Fetch helper for the MHO run (arithmetic and transcription only)."""
import sys, os, json, time, re, urllib.request, gzip, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
HERE = os.path.dirname(os.path.abspath(__file__))

def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                time.sleep(0.15)
                return data if binary else data.decode("utf-8", errors="replace")
        except Exception as e:
            err = e; time.sleep(1.5)
    raise err

def subs(cik):
    cik10 = str(int(cik)).zfill(10)
    j = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik10}.json"))
    rows = []
    r = j["filings"]["recent"]
    for i in range(len(r["form"])):
        rows.append((r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i]))
    for f in j["filings"].get("files", []):
        jj = json.loads(get("https://data.sec.gov/submissions/" + f["name"]))
        for i in range(len(jj["form"])):
            rows.append((jj["filingDate"][i], jj["form"][i], jj["accessionNumber"][i], jj["primaryDocument"][i], jj["reportDate"][i]))
    return j["name"], rows

def doc_url(cik, acc, doc):
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"

def to_text(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", h)
    h = re.sub(r"(?i)</td>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        cik = sys.argv[2]; forms = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        name, rows = subs(cik)
        print(name)
        for row in rows:
            if forms is None or row[1] in forms:
                print(" | ".join(row))
    elif cmd == "doc":
        cik, acc, doc, out = sys.argv[2:6]
        t = get(doc_url(cik, acc, doc))
        if doc.lower().endswith((".htm", ".html")):
            t = to_text(t)
        open(os.path.join(HERE, out), "w", encoding="utf-8").write(t)
        print(out, len(t))
