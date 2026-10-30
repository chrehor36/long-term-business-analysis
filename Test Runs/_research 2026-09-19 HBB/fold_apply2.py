import sys
sys.stdout.reconfigure(encoding="utf-8")
H = "Test Runs/_research 2026-09-19 HBB/"
f = open(H + "_fold.md", encoding="utf-8").read()
for a, b in [("The family (81.0% of the vote), the sixty-year\nbrand and a ROTCE-based pay plan are real;",
              "The family (81.0% of the vote), a long-lived\nbrand and a ROTCE-based pay plan are real;"),
             (" HBB is THE SHELF without a scale defence: CL's copy sits beside a $20bn brand, HBB's beside a $600M one.", "")]:
    assert a in f, a[:50]
    f = f.replace(a, b)
assert "—" not in f
open(H + "_fold.md", "w", encoding="utf-8").write(f)
p = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
s = open(p, encoding="utf-8").read()
assert "## UPDATE 2026-09-19 - HBB" not in s
s = s.rstrip("\n") + "\n" + f.rstrip("\n") + "\n"
open(p, "w", encoding="utf-8").write(s)
q = "Screens/SURVIVAL SHAPES - index.md"
t = open(q, encoding="utf-8").read()
L = t.split("\n")
k = [i for i, l in enumerate(L) if l.startswith("| 19 | **The shelf**")]
assert len(k) == 1
row = L[k[0]]
assert row.rstrip().endswith("|")
add = ("; HBB (2026-09-19, the mechanism: owned brands sold on purchase orders to Walmart 29% and Amazon 19%, who stock private label beside them and can source "
       "direct from the same Asian factories; the filer says the industry *\"does not have substantial entry barriers\"*; #11 as a feature: $58.7M of price returned "
       "in 2023-24 *\"reflecting lower costs\"*)")
L[k[0]] = row.rstrip()[:-1].rstrip() + add + " |"
open(q, "w", encoding="utf-8").write("\n".join(L))
print("fold ok")
