"""Fetch UPWK filings list and documents from SEC EDGAR. Working-folder script for this run only."""
import json, re, sys, time, urllib.request, html, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
HERE = os.path.dirname(os.path.abspath(__file__))
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    time.sleep(0.2)
    return data
def text_of(raw):
    s = raw.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "list":
        cik = sys.argv[2].zfill(10)
        j = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
        json.dump(j, open(os.path.join(HERE, f"sub_{cik}.json"), "w"))
        r = j["filings"]["recent"]
        forms = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
        for i in range(len(r["form"])):
            if forms is None or r["form"][i] in forms:
                print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""]*9999)[i])
    elif cmd == "doc":
        cik, acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        raw = get(url)
        open(os.path.join(HERE, out), "w", encoding="utf-8").write(text_of(raw))
        print("wrote", out, len(raw))
