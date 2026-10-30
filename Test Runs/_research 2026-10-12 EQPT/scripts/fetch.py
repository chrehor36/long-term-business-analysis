import sys, os, re, time, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
CIK = "1693736"
out = sys.argv[1]
docs = sys.argv[2:]
for spec in docs:
    name, acc, doc = spec.split("|")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    p = os.path.join(out, name + ".htm")
    if not os.path.exists(p):
        req = urllib.request.Request(url, headers=UA)
        data = urllib.request.urlopen(req, timeout=60).read()
        open(p, "wb").write(data)
        time.sleep(0.3)
    raw = open(p, "rb").read().decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<ix:header>.*?</ix:header>", " ", raw, flags=re.S)
    raw = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", raw)
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
    txt = re.sub(r"<[^>]+>", " ", raw)
    txt = html.unescape(txt).replace("\xa0", " ")
    txt = re.sub(r"[ \t]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    open(os.path.join(out, name + ".txt"), "w", encoding="utf-8").write(txt)
    print(name, len(txt))
