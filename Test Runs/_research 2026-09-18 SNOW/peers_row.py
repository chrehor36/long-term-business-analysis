import json, sys, re
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open("peers/peers_facts.json"))
out = []
for t, r in d.items():
    ys = sorted(r["rev"])[-3:]
    out.append(f"## {t} {r['name']} years {ys}")
    for y in ys:
        rev = r["rev"][y]; gp = r["gp"].get(y, rev - r["cor"].get(y, 0)); op = r["op"][y]; sbc = r["sbc"][y]; ocf = r["ocf"][y]
        prev = r["rev"].get(sorted(r["rev"])[sorted(r["rev"]).index(y) - 1])
        cap = r["capex"].get(y, 0) + r["capsw"].get(y, 0)
        out.append(f"{y} rev {rev:,.1f} growth {100*(rev/prev-1):.1f}% | GM {100*gp/rev:.1f}% | GAAP op {100*op/rev:.1f}% | op+SBC {100*(op+sbc)/rev:.1f}% | SBC/rev {100*sbc/rev:.1f}% | SBC/OCF {100*sbc/ocf:.0f}% | (OCF-SBC-capex)/rev {100*(ocf-sbc-cap)/rev:.1f}% ({ocf-sbc-cap:,.1f})")
t = open("peers/DDOG_10K_2025-12-31.txt", encoding="utf-8").read(); t = re.sub(r"\s+", " ", t)
m = re.search(r"Revenue \| \$? ?\|? ?3,427,[\d]+", t); out.append("DDOG face check: " + (t[m.start():m.start()+80] if m else "not found"))
open("peers/peers_row_out.txt", "w", encoding="utf-8").write("\n".join(out)); print("\n".join(out))
