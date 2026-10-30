import sys, json, os, re, time, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
def get(url):
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    raise SystemExit("fail " + url)
def cell_fix(m):
    return re.sub(r"(?i)</p>|</div>|<br\s*/?>", " ", m.group(0))
def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"[\r\n]+", " ", t)
    t = re.sub(r"(?is)<table.*?</table>", cell_fix, t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", t)
    t = re.sub(r"(?i)</td>", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = t.replace("$ ", "$").replace("( ", "(").replace(" )", ")")
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        cik = sys.argv[2]
        b = get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
        open(os.path.join(OUT, f"sub_{cik}.json"), "wb").write(b)
        d = json.loads(b); r = d["filings"]["recent"]
        forms = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
        for i in range(len(r["form"])):
            if forms is None or r["form"][i] in forms:
                print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""]*99999)[i])
    elif cmd == "doc":
        cik, acc, doc, name = sys.argv[2:6]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        b = get(url)
        open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8").write(strip(b))
        print("wrote", name, len(b))
    elif cmd == "idx":
        cik, acc = sys.argv[2:4]
        b = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/index.json")
        for it in json.loads(b)["directory"]["item"]:
            print(it["name"], it.get("size"))
