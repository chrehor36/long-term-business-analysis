import json,re
exec(open("scripts/peers.py").read().split("for cik,n in names.items():")[0])
out=[]
for cik,n in names.items():
    d=json.load(open(f"cache/facts_{cik}.json"))
    res={}
    for k,tl in tags.items():
        inst=k in ("gw","intg","assets","eq","cash","debt","ltdnc","ltdc")
        res[k]=series(d,tl,instant=inst)[0]
    ends=sorted(res["rev"].keys())[-10:]
    print(f"===== {n}  (fiscal year ends {ends[0]} to {ends[-1]})")
    print(f"{'end':>8} {'rev':>7} {'EBITA':>6} {'marg%':>6} {'TanCap':>7} {'EBITA/TanCap%':>13} {'InvCap':>7} {'EBITA/InvCap%':>13} {'OCF-capex':>9}")
    m=[];r1=[];r2=[]
    for e in ends:
        rev=res["rev"].get(e); oi=res["oi"].get(e); am=res["amort"].get(e,0) or 0
        eq=res["eq"].get(e); debt=res["debt"].get(e) or ((res["ltdnc"].get(e) or 0)+(res["ltdc"].get(e) or 0)); cash=res["cash"].get(e,0)
        gw=res["gw"].get(e,0); ig=res["intg"].get(e,0)
        ocf=res["ocf"].get(e); cx=res["capex"].get(e)
        if None in (rev,oi,eq): continue
        ebita=oi+am; inv=eq+debt-cash; tan=inv-gw-ig
        mg=100*ebita/rev; m.append(mg)
        a=100*ebita/tan if tan>0 else float('nan'); b=100*ebita/inv
        r1.append(a); r2.append(b)
        fcf="" if ocf is None or cx is None else f"{(ocf-cx)/1e6:.0f}"
        print(f"{e:>8} {rev/1e6:7.0f} {ebita/1e6:6.0f} {mg:6.1f} {tan/1e6:7.0f} {a:13.1f} {inv/1e6:7.0f} {b:13.1f} {fcf:>9}")
    import math
    mm=lambda x:sum(v for v in x if not math.isnan(v))/len([v for v in x if not math.isnan(v)])
    print(f"  mean margin {mm(m):.1f}%  range {min(m):.1f}-{max(m):.1f}; mean EBITA/InvCap {mm(r2):.1f}%; EBITA/TanCap mean of positive-capital years {mm(r1):.0f}%")
