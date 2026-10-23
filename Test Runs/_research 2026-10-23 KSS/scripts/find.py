import sys
t = open(sys.argv[1], encoding="utf-8").read()
pat = sys.argv[2]; n = int(sys.argv[3]); occ = int(sys.argv[4]) if len(sys.argv)>4 else 1
i = -1
for _ in range(occ):
    i = t.find(pat, i+1)
    if i < 0: print("NOT FOUND"); sys.exit()
print(t[i:i+n])
