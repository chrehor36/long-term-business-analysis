# Re-fetch a filing and flatten each table row onto ONE line (cells joined by " | ", empties dropped).
import sys, os, re, html, time
sys.path.insert(0, os.path.join(os.getcwd(), "Test Runs/_research 2026-09-13 CNR"))
from fetch import get, OUT
CACHE = os.path.join(OUT, "cache"); os.makedirs(CACHE, exist_ok=True)

def cell_text(s):
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s)
    return re.sub(r"[\s\u00a0]+", " ", s).strip()

def flatten(raw):
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    def row(m):
        cells = re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0))
        vals = [cell_text(c) for c in cells]
        vals = [v for v in vals if v not in ("", "$", ")", "%")]
        # glue "(123" + ")" pattern already dropped ")"; mark negatives
        vals = [("-" + v[1:]) if v.startswith("(") and not v.endswith(")") else v for v in vals]
        return "\n" + " | ".join(vals) + "\n"
    raw = re.sub(r"(?is)<tr[^>]*>.*?</tr>", row, raw)
    t = re.sub(r"(?i)</(p|div|li|h\d|table)>", "\n", raw)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def run(cik, acc, doc, name):
    p = os.path.join(OUT, name + ".flat.txt")
    if os.path.exists(p): print("have", p); return
    cp = os.path.join(CACHE, acc + "_" + doc)
    if os.path.exists(cp): raw = open(cp, encoding="utf-8").read()
    else:
        a = acc.replace("-", "")
        raw = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}")
        open(cp, "w", encoding="utf-8").write(raw); time.sleep(0.4)
    t = flatten(raw)
    open(p, "w", encoding="utf-8").write(t)
    print(name, len(t))

if __name__ == "__main__":
    args = sys.argv[1:]
    for i in range(0, len(args), 4):
        run(*args[i:i+4])
