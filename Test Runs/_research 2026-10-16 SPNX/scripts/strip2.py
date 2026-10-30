import sys, re, html
def cell(c):
    c = re.sub(r"<[^>]+>", " ", c); c = html.unescape(c).replace("\xa0"," ")
    return re.sub(r"\s+", " ", c).strip()
def row(m):
    cells = re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0))
    cs = [cell(c) for c in cells]
    out=[]
    for c in cs:
        if not c: continue
        if out and (c in (")", "%", ")%") or out[-1] in ("$", "(", "$(")):
            out[-1] = out[-1] + c if out[-1] in ("$","(","$(") else out[-1]+c
        else: out.append(c)
    return "\n" + " | ".join(out) + "\n"
def strip(t):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?is)<tr[^>]*>.*?</tr>", row, t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h\d>|</li>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
for f in sys.argv[1:]:
    b = open(f, encoding="utf-8", errors="ignore").read()
    open(f[:-4] + ".t2.txt", "w", encoding="utf-8").write(strip(b))
