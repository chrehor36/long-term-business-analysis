import re, os, sys, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
_cache = {}
def load(f):
    if f in _cache: return _cache[f]
    raw = open(f, encoding="utf-8").read()
    lines = raw.split("\n")
    out = []; lmap = []
    prev_space = True
    for li, l in enumerate(lines):
        for ch in l + "\n":
            if ch.isspace():
                if not prev_space:
                    out.append(" "); lmap.append(li); prev_space = True
            else:
                out.append(ch); lmap.append(li); prev_space = False
    s = "".join(out)
    _cache[f] = (s, lmap)
    return s, lmap
def find(f, pat, after_line=0, regex=False, flags=re.I):
    s, lmap = load(f)
    # first char index at or after after_line
    import bisect
    start = bisect.bisect_left(lmap, after_line)
    r = re.compile(pat if regex else re.escape(pat), flags)
    m = r.search(s, start)
    return m
def Q(f, start, end=None, after=0, sre=False, ere=False, maxlen=3000):
    """return (text, line) from start phrase through end phrase (inclusive)."""
    s, lmap = load(f)
    m = find(f, start, after, sre)
    if not m: raise Exception(f"START NOT FOUND {f} {start!r} after {after}")
    a = m.start()
    if end is None:
        b = m.end()
    else:
        r = re.compile(end if ere else re.escape(end), re.I)
        m2 = r.search(s, m.end() if not ere else m.end())
        if not m2 or m2.end()-a > maxlen: raise Exception(f"END NOT FOUND {f} {start!r} {end!r}")
        b = m2.end()
    return s[a:b].strip(), lmap[a]
def ctx(f, pat, n=400, after=0, regex=False, maxhits=20):
    s, lmap = load(f)
    import bisect
    r = re.compile(pat if regex else re.escape(pat), re.I)
    k = 0
    for m in r.finditer(s, bisect.bisect_left(lmap, after)):
        print(f"--- line {lmap[m.start()]}: ...{s[max(0,m.start()-n//4):m.start()+n]}...")
        k += 1
        if k >= maxhits: break
    print(f"[{k} shown]")
if __name__ == "__main__":
    a = sys.argv
    ctx(a[1], a[2], int(a[3]) if len(a) > 3 else 400, int(a[4]) if len(a) > 4 else 0, False, int(a[5]) if len(a) > 5 else 20)

# ---------- builder helpers ----------
import bisect as _bis
def q(f, start, end=None, after=0, sre=False, ere=False, maxlen=3000):
    t, ln = Q(f, start, end, after, sre, ere, maxlen)
    return f"> {t}\nSource: {f} line {ln}\n"
def qt(f, start, end=None, after=0, sre=False, ere=False, maxlen=3000):
    """return (quote_block, text, line)"""
    t, ln = Q(f, start, end, after, sre, ere, maxlen)
    return f"> {t}\nSource: {f} line {ln}\n", t, ln
_BND = re.compile(r'(?<=[a-z0-9\)”"’%])[.;:] (?=[A-Z“"•(])|(?<=\S) • ')
def sentence_at(f, pos, width=450):
    s, lmap = load(f)
    a = max(0, pos - width)
    left = s[a:pos]
    ms = list(_BND.finditer(left))
    if ms:
        st = a + ms[-1].end()
    else:
        sp = left.find(" ")
        st = a + (sp + 1 if a > 0 and sp >= 0 else 0)
    right = s[pos:pos + width]
    m2 = _BND.search(right)
    if m2:
        en = pos + m2.start() + 1
    else:
        sp = right.rfind(" ")
        en = pos + (sp if sp > 0 else len(right))
    return s[st:en].strip(), lmap[st]
def hits(f, pat, flags=re.I):
    s, lmap = load(f)
    return [(m.start(), m.group(0), lmap[m.start()]) for m in re.finditer(pat, s, flags)]
def raw_count(f, pat, flags=re.I):
    return len(re.findall(pat, open(f, encoding="utf-8").read(), flags))
def hit_quotes(f, pat, flags=re.I, width=450):
    out = []; seen = set()
    for pos, g, ln in hits(f, pat, flags):
        t, l2 = sentence_at(f, pos, width)
        if t in seen: continue
        seen.add(t)
        out.append((t, l2))
    return out
def verify(md_path):
    import os
    txt = open(md_path, encoding="utf-8").read().split("\n")
    bad = 0; n = 0
    for i, l in enumerate(txt):
        if l.startswith("> "):
            n += 1
            src = txt[i+1] if i + 1 < len(txt) else ""
            m = re.match(r"Source: (\S+) line (\d+)", src)
            if not m:
                print("NO SOURCE", i, l[:80]); bad += 1; continue
            s, lmap = load(m.group(1))
            quote = " ".join(l[2:].split())
            k = s.find(quote)
            if k < 0:
                print("NOT FOUND", i, m.group(1), l[:120]); bad += 1
            elif abs(lmap[k] - int(m.group(2))) > 0 and s.find(quote, 0) >= 0:
                # line mismatch: check any occurrence matches
                ok = False; j = k
                while j >= 0:
                    if lmap[j] == int(m.group(2)): ok = True; break
                    j = s.find(quote, j + 1)
                if not ok: print("LINE MISMATCH", i, m.group(1), m.group(2), "actual", lmap[k], l[:80]); bad += 1
    if "—" in "\n".join(txt): print("EM DASH PRESENT (count)", "\n".join(txt).count("—"))
    print(f"verified {n} quotes, {bad} problems")

def P(phrase):
    toks = phrase.split()
    return r"(?: ?\|)* ?".join(re.escape(t) for t in toks)
def QF(f, start, end=None, after=0, maxlen=3000):
    return Q(f, P(start), P(end) if end else None, after, True, True, maxlen)
def qf(f, start, end=None, after=0, maxlen=3000):
    t, ln = QF(f, start, end, after, maxlen)
    return f"> {t}\nSource: {f} line {ln}\n"
