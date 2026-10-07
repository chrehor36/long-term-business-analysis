import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
L=open(sys.argv[1],encoding="utf-8").read().split("\n")
for i in range(int(sys.argv[2]),min(int(sys.argv[3]),len(L))):
    if L[i].strip(): print(i, L[i])
