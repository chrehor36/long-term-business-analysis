import re, io, os, sys, html
OUT = "Test Runs/_research 2026-09-12 ACMR"
def conv(fn):
    s = io.open(os.path.join(OUT,fn), encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    # table cells -> pipe separated
    s = re.sub(r"(?is)</t[dh]>", " | ", s)
    s = re.sub(r"(?is)</tr>", "\n", s)
    s = re.sub(r"(?is)<(p|div|br|li|h[1-6])[^>]*>", "\n", s)
    s = re.sub(r"(?is)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = s.replace("\u00a0"," ").replace("\u2019","'").replace("\u201c",'"').replace("\u201d",'"')
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n[ \t]*", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    o = fn.rsplit(".",1)[0] + ".txt"
    io.open(os.path.join(OUT,o), "w", encoding="utf-8").write(s)
    print(o, len(s))
for f in sorted(os.listdir(OUT)):
    if f.endswith(".htm"):
        conv(f)
