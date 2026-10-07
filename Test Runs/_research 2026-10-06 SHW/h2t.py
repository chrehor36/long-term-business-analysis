"""Strip an EDGAR .htm to plain text (cache/<name>.txt). Usage: python h2t.py cache/file.htm [...]"""
import sys, re, html

for p in sys.argv[1:]:
    s = open(p, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    out = re.sub(r"\.html?$", ".txt", p)
    open(out, "w", encoding="utf-8").write(s)
    print(out, len(s))
