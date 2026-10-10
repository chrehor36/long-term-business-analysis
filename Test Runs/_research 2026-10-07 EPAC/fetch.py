"""Fetch an EDGAR document and strip it to text, saved as <name>_body.txt (gitignored).
Usage: python fetch.py <cik> <accession> <primary_doc> <name>
"""
import sys, re, html, time, urllib.request

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}

def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            time.sleep(2 + 2 * i)
            err = e
    raise err

def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

if __name__ == "__main__":
    cik, acc, doc, name = sys.argv[1:5]
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{doc}"
    txt = strip(get(url))
    open(f"{name}_body.txt", "w", encoding="utf-8").write(f"SOURCE {url}\nACCESSION {acc}\n\n" + txt)
    print(name, len(txt))
