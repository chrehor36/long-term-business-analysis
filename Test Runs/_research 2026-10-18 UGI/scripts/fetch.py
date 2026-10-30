"""Fetch SEC filings for UGI into cache/ (gitignored). Usage: fetch.py list | fetch.py get URL NAME"""
import sys, os, json, time, urllib.request, gzip, re, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
os.makedirs(CACHE, exist_ok=True)
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    time.sleep(0.2)
    return data
def text_of(htmlbytes):
    s = htmlbytes.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        cik = sys.argv[2]
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
        r = d["filings"]["recent"]
        forms = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
        for i in range(len(r["form"])):
            if forms and r["form"][i] not in forms: continue
            print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items",[""]*99999)[i])
    elif cmd == "get":
        url, name = sys.argv[2], sys.argv[3]
        data = get(url)
        open(os.path.join(CACHE, name), "wb").write(data)
        t = text_of(data) if url.endswith((".htm", ".html")) else data.decode("utf-8","replace")
        open(os.path.join(CACHE, name + ".txt"), "w", encoding="utf-8").write(t)
        print(name, len(data), "bytes;", len(t), "chars text")
