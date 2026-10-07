import io, os
for p in os.listdir("."):
    if not p.endswith(".txt") or p=="cm.txt": continue
    L = io.open(p, encoding="utf-8").read().split("\n")
    L2 = [l for l in L if not (len(l) > 3000 and "0001680062" in l)]
    if len(L2) != len(L):
        io.open(p, "w", encoding="utf-8").write("\n".join(L2)); print("stripped", p)
