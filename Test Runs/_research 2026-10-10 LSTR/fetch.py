"""Fetch helper for the LSTR run: SEC EDGAR with the project's User-Agent; caches under cache/."""
import sys, os, json, time, urllib.request, re, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
HERE = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(HERE, "cache")
def get(url, name=None):
    name = name or re.sub(r"[^A-Za-z0-9_.-]", "_", url.split("/")[-1])
    p = os.path.join(C, name)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return open(p, "rb").read()
    for i in range(4):
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read(); break
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2*(i+1))
    else:
        raise SystemExit("fetch failed " + url)
    open(p, "wb").write(b); time.sleep(0.25); return b
def text(url, name=None):
    b = get(url, name).decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", b)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        cik = sys.argv[2].zfill(10)
        j = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json", f"subs_{cik}.json"))
        files = [j["filings"]["recent"]] + [json.loads(get("https://data.sec.gov/submissions/"+f["name"], f["name"])) for f in j["filings"].get("files", [])]
        forms = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
        for r in files:
            for f, d, a, doc, per in zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"], r.get("reportDate", [""]*len(r["form"]))):
                if forms is None or f in forms:
                    print(f, d, per, a, doc)
    elif cmd == "doc":
        cik, acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        t = text(url, acc + "_" + doc)
        open(os.path.join(C, out), "w", encoding="utf-8").write(t); print(len(t), "chars ->", out)
    elif cmd == "facts":
        cik = sys.argv[2].zfill(10)
        get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", f"facts_{cik}.json"); print("ok")
if __name__ == "__main__" and sys.argv[1] == "idx":
    cik, acc = sys.argv[2], sys.argv[3]
    j = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/index.json", f"idx_{acc}.json"))
    for it in j["directory"]["item"]:
        print(it["name"], it.get("size"))
