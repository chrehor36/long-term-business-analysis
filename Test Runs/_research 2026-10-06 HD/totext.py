"""Convert a cached EDGAR .htm to plain text in cache/ (gitignored). Usage: python totext.py NAME.htm [...]"""
import sys, os, re, html
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache")
for name in sys.argv[1:]:
    raw = open(os.path.join(cache, name), encoding="utf-8", errors="replace").read()
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", raw)
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    txt = re.sub(r"[ \t\xa0]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    out = os.path.join(cache, name.rsplit(".", 1)[0] + ".txt")
    open(out, "w").write(txt)
    print(out, len(txt))
