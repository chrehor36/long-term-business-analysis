import sys
exec(open("calc.py").read().split("if __name__")[0])
d=eval(sys.argv[1]); a=d["2025"]; h1=d[sys.argv[2]]; h0=d[sys.argv[3]]
t={k:(a[k]+h1[k]-h0[k]) if a.get(k) is not None and h1.get(k) is not None else None for k in a}
print(t)
for r in ratios({"TTM":t}): print(r)
