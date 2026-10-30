import sys, json, time, urllib.request, re, html, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    raise SystemExit("fail "+url)
def text(b):
    s = b.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sub":
        b = get("https://data.sec.gov/submissions/CIK0000866729.json")
        open("sub.json","wb").write(b)
        d = json.loads(b); r = d["filings"]["recent"]
        for i in range(len(r["form"])):
            if r["form"][i] in ("10-K","10-Q","DEF 14A","8-K","SC 13D","SC 13D/A","10-K/A","SC TO-I","SC TO-I/A"):
                print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items",[""]*999)[i])
        print("older files:", [f["name"] for f in d["filings"].get("files",[])])
    elif cmd == "doc":
        acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4]
        url = f"https://www.sec.gov/Archives/edgar/data/866729/{acc.replace('-','')}/{doc}"
        b = get(url); open(out,"w",encoding="utf-8").write(text(b)); print(out, len(b))
    elif cmd == "idx":
        acc = sys.argv[2]
        b = get(f"https://www.sec.gov/Archives/edgar/data/866729/{acc.replace('-','')}/index.json")
        for it in json.loads(b)["directory"]["item"]: print(it["name"], it.get("size"))
    elif cmd == "url":
        b = get(sys.argv[2]); open(sys.argv[3],"w",encoding="utf-8").write(text(b)); print(sys.argv[3], len(b))
    elif cmd == "raw":
        b = get(sys.argv[2]); open(sys.argv[3],"wb").write(b); print(sys.argv[3], len(b))
