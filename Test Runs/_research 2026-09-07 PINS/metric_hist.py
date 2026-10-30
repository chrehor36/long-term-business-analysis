import os,re,sys
sys.stdout.reconfigure(encoding="utf-8")
OUT=os.path.dirname(os.path.abspath(__file__))
V=[("FY2020","10K_FY2020.txt"),("FY2021","10K_FY2021.txt"),("FY2022","10K_FY2022.txt"),
   ("FY2023","10K_FY2023.txt"),("FY2024","10K_FY2024.txt"),("FY2025","10K_FY2025.txt")]
TERMS=["Monthly Active Users","monthly active users","MAUs","MAU","Weekly Active Users","weekly active users",
 "WAUs","WAU","Daily Active","daily active","DAU","Average Revenue per User","average revenue per user",
 "ARPU","Global ARPU","key metric","key metrics","key operating metric","no longer","discontinu","cease",
 "Users We define","engagement"]
print("TERM COUNTS BY VINTAGE (Pinterest 10-Ks)")
hdr="  {:34s}".format("term")+"".join(f"{v:>9s}" for v,_ in V)
print(hdr)
texts={v:open(os.path.join(OUT,f),encoding="utf-8").read() for v,f in V}
for term in TERMS:
    row="  {:34s}".format(repr(term)[1:-1][:33])
    for v,_ in V:
        row+=f"{texts[v].count(term):>9d}"
    print(row)
