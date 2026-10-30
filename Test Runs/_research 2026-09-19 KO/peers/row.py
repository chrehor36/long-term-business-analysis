import json, sys
sys.stdout.reconfigure(encoding="utf-8")
m=json.load(open("metrics.json"))
Y=[str(y) for y in range(2021,2026)]
adj={"KO":{"2021":100*0,"2023":167,"2024":6000,"2025":6069}}  # operating-cash one-offs added back (fairlife 2021 split not disclosed: 0)
for t in ["KO","PEP","KDP","MNST","CELH","COKE"]:
    d=m[t]; r=d["rev"]; 
    cagr=(r["2025"]/r["2021"])**(1/4)-1
    om=sum(d["oi"][y] for y in Y)/sum(r[y] for y in Y)
    gm=[round(100*d["gp"][y]/r[y],1) for y in Y]
    sb=lambda y: d["sbc"].get(y,0.0)
    oc=sum(d["ocf"][y]-d["capex"][y]-sb(y) for y in Y)/sum(r[y] for y in Y)
    line=f"{t}: rev {r['2021']/1e6:,.0f} -> {r['2025']/1e6:,.0f} CAGR {100*cagr:.1f}% | op margin 5y {100*om:.1f}% | owner cash/rev 5y {100*oc:.1f}% | GM {gm}"
    if t in adj:
        oca=sum(d["ocf"][y]+adj[t].get(y,0)*1e6-d["capex"][y]-sb(y) for y in Y)/sum(r[y] for y in Y)
        line+=f" | owner cash/rev ADJ {100*oca:.1f}%"
    print(line)
    print("   op margin by year", [round(100*d["oi"][y]/r[y],1) for y in Y])
