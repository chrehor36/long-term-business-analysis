import sys, re, html
def strip(raw):
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    def row(m):
        t = m.group(0)
        t = re.sub(r"(?i)</t[dh]>", " | ", t)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t).replace("\xa0", " ")
        t = re.sub(r"\s+", " ", t)
        t = re.sub(r"(\|\s*)+\|", "|", t)
        return "\n" + t.strip() + "\n"
    raw = re.sub(r"(?is)<tr\b.*?</tr>", row, raw)
    raw = re.sub(r"(?i)</(p|div|li|h\d|table)>", "\n", raw)
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    txt = re.sub(r"<[^>]+>", " ", raw)
    txt = html.unescape(txt).replace("\xa0", " ")
    txt = re.sub(r"[ \t]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    return txt
for p in sys.argv[1:]:
    raw = open(p, "rb").read().decode("utf-8", "ignore")
    t = strip(raw)
    open(p[:-4] + ".txt", "w", encoding="utf-8").write(t)
    print(p, len(t), t.count("\n"))
