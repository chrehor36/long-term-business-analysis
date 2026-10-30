"""Fetch AMZN filings from EDGAR into cache/ and write plain-text dumps (cache/ is gitignored).
usage: python -I fetch.py name,accession,document [...]"""
import sys, time, re, html, urllib.request, os

UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
CIK = "1018724"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def text(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(out, exist_ok=True)
for arg in sys.argv[1:]:
    name, acc, doc = arg.split(",")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/{doc}"
    b = get(url)
    time.sleep(0.3)
    open(os.path.join(out, name + ".htm"), "wb").write(b)
    open(os.path.join(out, name + ".txt"), "w").write(text(b))
    print(name, len(b), url)
