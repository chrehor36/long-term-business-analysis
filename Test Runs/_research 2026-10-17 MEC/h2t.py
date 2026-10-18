import sys, re, html
for p in sys.argv[1:]:
    s = open(p, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h\d|table)\s*>|<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</t[dh]\s*>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("\xa0", " ").replace("​", "")
    lines = []
    for ln in s.split("\n"):
        cells = [c.strip() for c in ln.split(" | ")]
        cells = [c for c in cells if c not in ("", "$", "%", ")")]
        ln = " | ".join(cells)
        ln = re.sub(r"[ \t]+", " ", ln).strip()
        if ln: lines.append(ln)
    s = "\n".join(lines)
    open(p.rsplit(".",1)[0] + ".txt", "w", encoding="utf-8").write(s)
    print(p, len(s))
