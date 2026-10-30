import sys, re, html, os
def totext(p):
    s = open(p, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    for p in sys.argv[1:]:
        out = os.path.splitext(p)[0] + ".txt"
        open(out, "w", encoding="utf-8").write(totext(p))
        print(out, os.path.getsize(out))
