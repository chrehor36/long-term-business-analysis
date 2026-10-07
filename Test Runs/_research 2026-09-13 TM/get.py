"""TM run fetcher. Downloads EDGAR primary docs and exhibits, strips HTML to text.
Usage:
  python get.py doc <accession> <primarydoc> <outname>     -> outname.txt
  python get.py all <accession> <prefix>                   -> every .htm/.txt in the accession
"""
import json, os, re, sys, time, urllib.request, html as _h
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = 1094517


def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            data = urllib.request.urlopen(req, timeout=90).read()
            time.sleep(0.2)
            return data
        except Exception as e:
            print("retry", url, e)
            time.sleep(2 + i * 3)
    raise SystemExit("failed " + url)


def strip_html(h):
    h = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?i)<br[^>]*>', '\n', h)
    h = re.sub(r'(?i)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?i)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    h = _h.unescape(h)
    h = h.replace('\xa0', ' ').replace('’', "'").replace('“', '"').replace('”', '"')
    h = re.sub(r'[ \t]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h


def save_txt(name, raw):
    txt = strip_html(raw.decode('utf-8', 'replace'))
    with open(os.path.join(HERE, name), 'w', encoding='utf-8') as f:
        f.write(txt)
    print("saved", name, len(txt))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "doc":
        acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4]
        url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/{doc}"
        save_txt(out + ".txt", get(url))
    elif cmd == "all":
        acc, prefix = sys.argv[2], sys.argv[3]
        base = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/"
        d = json.loads(get(base + "index.json"))
        for it in d["directory"]["item"]:
            n = it["name"]
            if n.lower().endswith((".htm", ".html", ".txt")) and not n.endswith("-index.htm") \
                    and not n.startswith(acc) and "index" not in n:
                save_txt(f"{prefix}__{os.path.splitext(n)[0]}.txt", get(base + n))
