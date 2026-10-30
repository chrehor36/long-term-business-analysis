import sys, re, html
raw = open(sys.argv[1], "rb").read().decode("utf-8", "replace")
raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
# rows: mark row ends; inside rows, cells separated by |
raw = re.sub(r"(?i)</tr>", "\n@@ROW@@\n", raw)
raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
raw = re.sub(r"(?i)</(p|div|li|h\d|table)>", "\n", raw)
raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
raw = re.sub(r"<[^>]+>", "", raw)
raw = html.unescape(raw).replace("\xa0", " ")
raw = re.sub(r"[ \t]+", " ", raw)
out=[]; buf=[]; inrow=False
for line in raw.split("\n"):
    s=line.strip()
    if s=="@@ROW@@":
        row=" ".join(x for x in buf if x)
        row=re.sub(r"(\|\s*)+\|", "|", row)
        row=re.sub(r"\$\s*\|\s*", "$", row)
        row=re.sub(r"\|\s*\)", ")", row)
        row=re.sub(r"\|\s*%", "%", row)
        if row.strip(" |"): out.append(row.strip())
        buf=[]; continue
    if "|" in s or buf:
        buf.append(s)
    elif s:
        out.append(s)
if buf: out.append(" ".join(buf))
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
