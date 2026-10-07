import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
fn, pat = sys.argv[1], sys.argv[2]
occ = int(sys.argv[3]) if len(sys.argv) > 3 else 1
n = int(sys.argv[4]) if len(sys.argv) > 4 else 6000
t = open(fn, encoding="utf-8").read().replace("\u202f"," ")
i = -1
for k in range(occ):
    i = t.find(pat, i+1)
    if i < 0: print("NOT FOUND", k); sys.exit()
print(t[i:i+n])
