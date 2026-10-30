import sys, urllib.request, gzip, json, re, os, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    return data
def text_of(htmlbytes):
    s = htmlbytes.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "subs":
        cik = sys.argv[2].zfill(10)
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
        json.dump(d, open(f"sub_{cik}.json","w"))
        r = d["filings"]["recent"]
        for i in range(len(r["form"])):
            if r["form"][i] in sys.argv[3].split(","):
                print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("reportDate",[""]*999)[i])
        for f in d["filings"].get("files", []):
            print("OLDER FILE", f["name"], f["filingFrom"], f["filingTo"])
    elif mode == "older":
        d = json.loads(get("https://data.sec.gov/submissions/" + sys.argv[2]))
        for i in range(len(d["form"])):
            if d["form"][i] in sys.argv[3].split(","):
                print(d["form"][i], d["filingDate"][i], d["accessionNumber"][i], d["primaryDocument"][i], d["reportDate"][i])
    elif mode == "doc":
        cik, acc, doc, out = sys.argv[2:6]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        b = get(url)
        open(out, "w", encoding="utf-8").write(text_of(b) if doc.endswith((".htm",".html")) else b.decode("utf-8","ignore"))
        print("wrote", out, len(b))
    elif mode == "url":
        b = get(sys.argv[2]); open(sys.argv[3],"w",encoding="utf-8").write(text_of(b)); print("wrote", sys.argv[3], len(b))
