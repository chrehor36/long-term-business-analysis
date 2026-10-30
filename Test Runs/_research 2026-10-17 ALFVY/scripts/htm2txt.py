import re, html, sys
sys.stdout.reconfigure(encoding="utf-8")
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8", errors="ignore").read()
t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t); t = re.sub(r"\s+", " ", t)
open(dst, "w", encoding="utf-8").write(t)
for pat in sys.argv[3:]:
    for m in re.finditer(re.escape(pat), t):
        print("@@", t[m.start():m.start() + 700]); print()
