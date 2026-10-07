"""Fetch helper for the CENT run, 2026-10-05. Saves SEC documents to this folder. No numbers computed here."""
import sys, os, json, re, time, urllib.request, gzip, html

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
HERE = os.path.dirname(os.path.abspath(__file__))


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    time.sleep(0.15)
    return data


def save(url, name, text=False):
    path = os.path.join(HERE, name)
    if os.path.exists(path):
        return path
    data = get(url)
    if text:
        s = data.decode("utf-8", "replace")
        s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
        s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
        s = re.sub(r"(?i)</td>|</th>", " | ", s)
        s = re.sub(r"<[^>]+>", " ", s)
        s = html.unescape(s)
        s = re.sub(r"[ \t\xa0]+", " ", s)
        s = re.sub(r"\n\s*\n+", "\n", s)
        data = s.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return path


def submissions(cik, name):
    return save(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json", name)


def facts(cik, name):
    return save(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json", name)


def list_filings(subpath, forms):
    d = json.load(open(subpath))
    r = d["filings"]["recent"]
    out = []
    for i in range(len(r["form"])):
        if r["form"][i] in forms:
            out.append((r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i]))
    return out


def doc(cik, acc, primary, name):
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{primary}"
    return save(url, name, text=True)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        p = submissions(sys.argv[2], sys.argv[3])
        for row in list_filings(p, set(sys.argv[4].split(","))):
            print(*row)
    elif cmd == "facts":
        print(facts(sys.argv[2], sys.argv[3]))
    elif cmd == "doc":
        print(doc(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
    elif cmd == "url":
        print(save(sys.argv[2], sys.argv[3], text=(len(sys.argv) > 4)))
