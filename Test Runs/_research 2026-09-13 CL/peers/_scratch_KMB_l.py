import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
L=open(sys.argv[1],encoding="utf-8").read().split("\n")
w=int(sys.argv[4]) if len(sys.argv)>4 else 400
for i in range(int(sys.argv[2]),min(int(sys.argv[3]),len(L))): print(i,L[i][:w])
