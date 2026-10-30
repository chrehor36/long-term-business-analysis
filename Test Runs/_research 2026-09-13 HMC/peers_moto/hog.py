import json, re, html, os, sys, time, urllib.request, gzip
UA = {"User-Agent": "BRK research chrehor36@gmail.com", "Accept-Encoding": "gzip"}
HERE = os.path.dirname(os.path.abspath(__file__))

def get(url):
    req = urllib.request.Request(url, headers=UA)
    r = urllib.request.urlopen(req, timeout=60)
    raw = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        raw = gzip.decompress(raw)
    time.sleep(0.2)
    return raw.decode("utf-8", "replace")

def rows(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    out = []; pos = 0
    def txt(s):
        s = re.sub(r'(?i)</(p|div|h\d|li)>|<br\s*/?>', '\n', s)
        s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
        for line in s.split('\n'):
            line = re.sub(r'\s+', ' ', line).strip()
            if line: out.append(line)
    for m in re.finditer(r'(?is)<table.*?</table>', h):
        txt(h[pos:m.start()])
        for tr in re.findall(r'(?is)<tr.*?</tr>', m.group(0)):
            cells = []
            for td in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>', tr):
                c = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', td))).strip()
                if c and c not in ('$', ')', '%'): cells.append(c)
            if cells:
                out.append(' | '.join(cells).replace('( ', '(').replace(' | )', ')').replace(' | %', '%'))
        pos = m.end()
    txt(h[pos:])
    return out

if __name__ == "__main__":
    sub = json.loads(get("https://data.sec.gov/submissions/CIK0000793952.json"))
    rec = sub["filings"]["recent"]
    ks = [(rec["filingDate"][i], rec["accessionNumber"][i], rec["primaryDocument"][i], rec["reportDate"][i])
          for i in range(len(rec["form"])) if rec["form"][i] == "10-K"]
    for k in ks[:6]:
        print(k)
    for fd, acc, doc, rd in ks[:6]:
        url = "https://www.sec.gov/Archives/edgar/data/793952/%s/%s" % (acc.replace("-", ""), doc)
        fn = os.path.join(HERE, "HOG_10K_FY%s_%s.txt" % (rd[:4], acc))
        if os.path.exists(fn):
            continue
        t = rows(get(url))
        with open(fn, "w", encoding="utf-8") as f:
            f.write("SOURCE: %s\nFILED: %s  PERIOD: %s  ACCESSION: %s\n\n" % (url, fd, rd, acc))
            f.write("\n".join(t))
        print("wrote", fn, len(t))
