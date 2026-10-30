import re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
_cache = {}
def lines(f):
    if f not in _cache:
        _cache[f] = open(f, encoding="utf-8").read().split("\n")
    return _cache[f]
def norm(s): return re.sub(r"\s+", " ", s).strip()
def build(template, alias, out):
    errs = []
    def repl_L(m):
        a, n = m.group(1), int(m.group(2)); f = alias[a]
        t = lines(f)[n].strip()
        return f"> {t}\nSource: {f} line {n}"
    def repl_S(m):
        a, n, s, e = m.group(1), int(m.group(2)), m.group(3), m.group(4); f = alias[a]
        L = lines(f)[n]
        i = L.find(s)
        if i < 0: errs.append(f"start not found {a} {n} {s!r}"); return "ERR"
        if e == "$": t = L[i:].strip()
        else:
            j = L.find(e, i)
            if j < 0: errs.append(f"end not found {a} {n} {e!r}"); return "ERR"
            t = L[i:j+len(e)]
        return f"> {t.strip()}\nSource: {f} line {n}"
    txt = re.sub(r"@@L (\S+) (\d+)@@", repl_L, template)
    txt = re.sub(r"@@S (\S+) (\d+) <<(.*?)>> <<(.*?)>>@@", repl_S, txt)
    # verify
    ls = txt.split("\n")
    for k, l in enumerate(ls):
        if l.startswith("> "):
            src = ls[k+1]
            m = re.match(r"Source: (\S+) line (\d+)$", src)
            if not m: errs.append(f"bad source after {l[:60]}"); continue
            whole = norm(open(m.group(1), encoding="utf-8").read())
            if norm(l[2:]) not in whole: errs.append(f"quote not substring: {l[:80]}")
        else:
            if "—" in l or "–" in l: errs.append(f"dash in prose line {k}: {l[:100]}")
        if "@@" in l: errs.append(f"unresolved {l}")
    open(out, "w", encoding="utf-8").write(txt)
    print("written", out, "quotes:", sum(1 for l in ls if l.startswith("> ")), "errors:", len(errs))
    for e in errs: print(" ", e)
