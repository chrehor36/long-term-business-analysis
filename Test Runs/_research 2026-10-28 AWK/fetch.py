"""Fetch SEC EDGAR documents for the AWK run into cache/ (untrusted data, no execution).
Usage: python -I fetch.py <url> <outname>   or   python -I fetch.py subs <cik>
"""
import sys, os, time, urllib.request, gzip, json, re, html

UA = "Chris Hrehor chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                return data
        except Exception as e:
            print("retry", i, e, file=sys.stderr)
            time.sleep(2 + i * 2)
    raise SystemExit("failed " + url)


def to_text(raw):
    s = raw.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = s.replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


if __name__ == "__main__":
    if sys.argv[1] == "subs":
        cik = sys.argv[2].zfill(10)
        data = get(f"https://data.sec.gov/submissions/CIK{cik}.json")
        open(os.path.join(CACHE, f"subs_{cik}.json"), "wb").write(data)
        j = json.loads(data)
        rec = j["filings"]["recent"]
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 80
        forms = set(sys.argv[4].split(",")) if len(sys.argv) > 4 else None
        print(j["name"])
        for k in range(len(rec["form"])):
            if forms and rec["form"][k] not in forms:
                continue
            print(rec["filingDate"][k], rec["form"][k], rec["accessionNumber"][k], rec["primaryDocument"][k], rec.get("items", [""] * 9999)[k])
            n -= 1
            if n <= 0:
                break
    elif sys.argv[1] == "facts":
        cik = sys.argv[2].zfill(10)
        data = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")
        open(os.path.join(CACHE, f"facts_{cik}.json"), "wb").write(data)
        print("ok", len(data))
    else:
        url, out = sys.argv[1], sys.argv[2]
        data = get(url)
        open(os.path.join(CACHE, out + ".raw"), "wb").write(data)
        txt = to_text(data)
        open(os.path.join(CACHE, out + ".txt"), "w", encoding="utf-8").write(txt)
        print("ok", out, len(txt))
