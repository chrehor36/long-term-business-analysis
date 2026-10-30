import json
d=json.load(open("competitor_xbrl.json"))
def pick(f,tags):
    for t in tags:
        if t in f and f[t]: return f[t]
    return {}
def yr(rows,y):
    for k,v in rows.items():
        if k.startswith(str(y)): return v["val"]
    return None
print(f"{'tkr':5s} {'window':13s} {'OCF mean':>9} {'SBC mean':>9} {'D&A':>8} {'capex':>8} {'OE(D&A)':>9} {'OE(cpx)':>9} {'SBC/OCF':>8}")
for t,e in d.items():
    f=e["facts"]
    ocf=pick(f,["us-gaap:NetCashProvidedByUsedInOperatingActivities"])
    sbc=pick(f,["us-gaap:ShareBasedCompensation"])
    cpx=pick(f,["us-gaap:PaymentsToAcquirePropertyPlantAndEquipment"])
    # fiscal-year alignment: use the last 5 available years in ocf
    yrs=sorted(set(k[:4] for k in ocf))[-5:]
    o=[];s=[];c=[]
    for y in yrs:
        a=yr(ocf,y); b=yr(sbc,y); cc=yr(cpx,y)
        if a is None: continue
        o.append(a); s.append(b or 0); c.append(cc or 0)
    if not o: print(t,"no data"); continue
    n=len(o); M=1e6
    om=sum(o)/n/M; sm=sum(s)/n/M; cm=sum(c)/n/M
    print(f"{t:5s} {yrs[0]+'-'+yrs[-1]:13s} {om:9.1f} {sm:9.1f} {'n/a':>8} {cm:8.1f} {'n/a':>9} {om-sm-cm:9.1f} {100*sm/om if om else float('nan'):8.1f}")
