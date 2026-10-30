"""Fetch EDGAR documents for the PLTR run and save HTML plus a plain-text copy into ../cache/.
Usage: python -I fetch.py <cachedir> <accession> <primarydoc> <label> [...more triples]
"""
import sys, os, re, time, urllib.request, html
from html.parser import HTMLParser

UA = "Chris Hrehor chrehor36@gmail.com"
CIK = os.environ.get("FETCH_CIK", "1321655")  # another filer's CIK for competitor documents


class T(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "table"):
            self.out.append("\n")
        if tag in ("td", "th"):
            self.out.append(" | ")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


def totext(raw):
    p = T()
    p.feed(raw)
    s = "".join(p.out)
    s = s.replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


def main():
    cache = sys.argv[1]
    args = sys.argv[2:]
    for i in range(0, len(args), 3):
        acc, doc, label = args[i:i + 3]
        url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/{doc}"
        hp = os.path.join(cache, label + ".htm")
        if not os.path.exists(hp):
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            open(hp, "wb").write(data)
            time.sleep(0.3)
        raw = open(hp, "rb").read().decode("utf-8", "replace")
        txt = totext(raw)
        open(os.path.join(cache, label + ".txt"), "w", encoding="utf-8").write(txt)
        print(label, acc, len(txt))


if __name__ == "__main__":
    main()
