import sys
p="C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-09-12 Run - ACVA ACV Auctions.md"
s=open(p,encoding="utf-8").read()
start=sys.argv[1]; end=sys.argv[2]; src=sys.argv[3]
a=s.index(start); b=s.index(end)
s=s[:a]+open(src,encoding="utf-8").read()+s[b:]
open(p,"w",encoding="utf-8").write(s); print("spliced",a,b)
