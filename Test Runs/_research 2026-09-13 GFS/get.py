"""GFS run fetcher. EDGAR primary docs to text. Transcription only.
  python get.py sub                      -> submissions.json + filings list
  python get.py doc <acc> <doc> <out>    -> out.txt (and out.htm raw)
  python get.py facts                    -> companyfacts.json
"""
import json, os, re, sys, time, urllib.request, html as _h
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = 1709048

def get(url):
    last = None
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            data = urllib.request.urlopen(req, timeout=90).read()
            time.sleep(0.15)
            return data
        except Exception as e:
            last = e
            print("retry", url, e)
            time.sleep(2 + i * 3)
    raise SystemExit("failed " + url + " " + str(last))

def strip_html(h):
    h = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', h)
    h = re.sub(r'(?i)<br[^>]*>', '\n', h)
    h = re.sub(r'(?i)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?i)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    h = _h.unescape(h)
    h = h.replace('\xa0', ' ').replace('’', "'").replace('“', '"').replace('”', '"')
    h = re.sub(r'[ \t]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sub":
        raw = get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json")
        open(os.path.join(HERE, "submissions.json"), "wb").write(raw)
        d = json.loads(raw); r = d["filings"]["recent"]
        with open(os.path.join(HERE, "filings_list.txt"), "w") as f:
            for i in range(len(r["form"])):
                f.write("\t".join([r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("primaryDocDescription", [""]*len(r["form"]))[i], r["reportDate"][i]]) + "\n")
        print(d.get("name"), d.get("fiscalYearEnd"), len(r["form"]), d["filings"].get("files"))
    elif cmd == "doc":
        acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4]
        url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/{doc}"
        raw = get(url)
        txt = strip_html(raw.decode('utf-8', 'replace'))
        open(os.path.join(HERE, out + ".txt"), "w", encoding="utf-8").write(txt)
        print("saved", out, len(txt))
    elif cmd == "idx":
        acc = sys.argv[2]
        base = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/"
        d = json.loads(get(base + "index.json"))
        for it in d["directory"]["item"]:
            print(it["name"], it.get("size"))
    elif cmd == "facts":
        raw = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK:010d}.json")
        open(os.path.join(HERE, "companyfacts.json"), "wb").write(raw)
        d = json.loads(raw)
        for ns, tags in d["facts"].items():
            print(ns, len(tags))
