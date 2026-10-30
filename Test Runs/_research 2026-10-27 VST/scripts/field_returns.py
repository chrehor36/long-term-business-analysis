# COMPUTATION: field returns from XBRL first-filed annual values (transcription; checked for VST against filed statements)
import re,sys
D=sys.argv[1]
txt=open(f"{D}/peers_xbrl.txt").read().split("== ")[1:]
for blk in txt:
    lines=blk.strip().splitlines(); n=lines[0]
    rows={}
    for l in lines[2:]:
        p=l.split(); y=p[0]; v=[float(x) for x in p[1:]]
        rows[y]=dict(zip("REV OI PRETAX NI EQ GW INT LTD CUR CASH INTX".split(),v))
    ys=sorted(rows); out=[]
    import math
    for i,y in enumerate(ys):
        r=rows[y]
        if i==0: continue
        p=rows[ys[i-1]]
        def tc(x):
            vals=[x[k] for k in ("EQ","LTD","CUR","CASH","GW","INT")]
            vals=[0 if math.isnan(v) else v for v in vals]
            eq,ltd,cur,cash,gw,it=vals
            return eq+ltd+cur-cash-gw-it
        cap=(tc(r)+tc(p))/2
        oi=r["OI"]
        if math.isnan(oi) or cap<=0: continue
        out.append((y,oi,cap,oi*0.79/cap))
    if not out: continue
    print(n)
    for y,oi,cap,rt in out: print(f"  {y}  OI {oi:7.0f}  avg tangible capital {cap:7.0f}  after-tax OI / capital {rt*100:6.1f}%")
    s_oi=sum(o[1] for o in out); s_cap=sum(o[2] for o in out)
    print(f"  span {out[0][0]}-{out[-1][0]}: sum OI*0.79 / sum capital = {s_oi*0.79/s_cap*100:5.1f}%")
