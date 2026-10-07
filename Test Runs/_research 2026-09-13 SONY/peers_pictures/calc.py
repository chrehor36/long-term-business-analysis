import sys
# usage: calc.py label:num/den ...
for a in sys.argv[1:]:
    lab, e = a.split(":")
    n, d = e.split("/")
    print(f"{lab}: {float(n)}/{float(d)} = {100*float(n)/float(d):.1f}%")
