"""Extract the filed volume / pricing / FX decomposition sentences from each 10-K MD&A (annual, not quarterly), verbatim,
and parse the percentages into a table. Arithmetic and transcription only."""
import re, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
out, table = [], {}
SEG = ["Worldwide", "Oral, Personal and Home Care", "North America", "Latin America", "Europe", "Asia Pacific",
       "Africa/Eurasia", "Hill", "Pet Nutrition"]
for fy in range(2017, 2026):
    t = open(os.path.join(HERE, f"10-K_FY{fy}.txt"), encoding="utf-8", errors="replace").read()
    t = re.sub(r"\s+", " ", t)
    t = t.replace(" %", "%").replace(" ,", ",")
    sents = re.split(r"(?<=[a-z0-9%)])\. (?=[A-Z])", t)
    seen = set()
    for s in sents:
        if ("Net sales" in s and "volume" in s and (f"in {fy}" in s or f"{fy} to" in s)
                and "quarter" not in s and len(s) < 700):
            key = s[:120]
            if key in seen:
                continue
            seen.add(key)
            seg = next((g for g in SEG if g in s[:80]), "?")
            vol = re.search(r"volume (growth|declines?|decreases?|increases?) of ([\d.]+)%", s)
            prc = re.search(r"net selling price (increases?|decreases?|declines?) of ([\d.]+)%", s)
            fx = re.search(r"(positive|negative) foreign exchange of ([\d.]+)%", s)
            sign = lambda m, neg: (None if not m else (-float(m.group(2)) if any(w in m.group(1) for w in neg) else float(m.group(2))))
            v = sign(vol, ("decl", "decr")); pr = sign(prc, ("decr", "decl")); f = sign(fx, ("negative",))
            if fx is None and "Foreign exchange was flat" in s:
                f = 0.0
            table.setdefault(seg, {})[fy] = (v, pr, f)
            out.append(f"FY{fy} | {seg} | vol {v} | price {pr} | fx {f} | {s.strip()}")
open(os.path.join(HERE, "vpfx_out.txt"), "w", encoding="utf-8").write("\n".join(out))
for seg, d in table.items():
    print(seg)
    for fy in sorted(d):
        print("  ", fy, d[fy])
