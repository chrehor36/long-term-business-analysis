# -*- coding: utf-8 -*-
"""Owner earnings on ONE construction for every BA peer. Arithmetic only; no conclusions."""
import sys, io, json, os
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
OUT="Test Runs/_research 2026-09-12 BA/peers"
raw=json.load(open(os.path.join(OUT,"xbrl_raw.json")))

# fill-ins read off the filings (see COMPETITOR ROW.md sources section)
FILL = {
 "HEI": {"SBC": {"2025-10-31":34.381, "2024-10-31":18.775, "2023-10-31":15.475}},
 "TXT": {},  # TXT tags no OperatingIncomeLoss; segment profit used instead (see notes)
}
ERJ = {  # 20-F acc 0001628280-26-021824 (FY2025) / 0001193125-25-069283 (FY2024)
 "REV": {"2025":7577.5,"2024":6394.7,"2023":5268.5},
 "OPINC": {"2025":607.6,"2024":667.5,"2023":314.5},
 "OCF": {"2025":870.0,"2024":871.0,"2023":617.0},
 "CAPEX": {"2025":187.2+296.7,"2024":200.4+265.8,"2023":238.7+192.1},  # PP&E + intangibles (dev spend)
 "CAPEX_PPE": {"2025":187.2,"2024":200.4,"2023":238.7},
 "DA": {"2025":259.5,"2024":243.6,"2023":241.7},
 "SBC": {"2025":None,"2024":None,"2023":None},
}
SPR = {  # 10-K acc 0001628280-25-009088 (FY2024, the LAST 10-K)
 "REV": {"2024":6316.6,"2023":6047.9,"2022":5029.7},
 "OPINC": {"2024":-1786.1,"2023":-134.2,"2022":-281.0},
 "OCF": {"2024":-1121.0,"2023":-226.0,"2022":-395.0},
 "CAPEX": {"2024":152.0,"2023":148.0,"2022":122.0},
 "DA": {"2024":305.4+15.2,"2023":315.6+15.2,"2022":337.1+14.4},
 "SBC": {"2024":38.0,"2023":29.0,"2022":37.0},
}

def yr(k): return k[:4] if k[:4] not in ("2026",) else "2025"   # TXT FY2025 ends 2026-01-03

print(f"{'TK':<5}{'FY':<6}{'REV':>10}{'OPINC':>9}{'OPM%':>7}{'OCF':>9}{'SBC':>7}{'D&A':>8}{'CAPEX':>8}{'OE(capex)':>11}{'OE(D&A)':>10}")
rows={}
for tk in ("BA","LMT","NOC","RTX","GD","TXT","TDG","HEI","ERJ","SPR"):
    if tk=="ERJ": src=ERJ; ends=["2023","2024","2025"]
    elif tk=="SPR": src=SPR; ends=["2022","2023","2024"]
    else:
        d=raw[tk]; s=d["series"]
        for k,v in FILL.get(tk,{}).items():
            s.setdefault(k,{}).update(v)
        ends=sorted(s["REV"])[-3:]
        src={k:{yr(e):s[k].get(e) for e in ends} for k in ("REV","OPINC","OCF","CAPEX","DA","SBC")}
        ends=[yr(e) for e in ends]
    rows[tk]={}
    for e in ends:
        rev=src["REV"].get(e); op=src["OPINC"].get(e); ocf=src["OCF"].get(e)
        sbc=src["SBC"].get(e); da=src["DA"].get(e); cx=src["CAPEX"].get(e)
        opm = f"{100*op/rev:.1f}" if (op is not None and rev) else "n/a"
        oec = ocf-(sbc or 0)-cx if (ocf is not None and cx is not None) else None
        oed = ocf-(sbc or 0)-da if (ocf is not None and da is not None) else None
        rows[tk][e]=dict(rev=rev,op=op,opm=opm,ocf=ocf,sbc=sbc,da=da,cx=cx,oec=oec,oed=oed)
        f=lambda v: f"{v:,.0f}" if isinstance(v,(int,float)) else "n/a"
        print(f"{tk:<5}{e:<6}{f(rev):>10}{f(op):>9}{opm:>7}{f(ocf):>9}{f(sbc):>7}{f(da):>8}{f(cx):>8}{f(oec):>11}{f(oed):>10}")
    print()
json.dump(rows, open(os.path.join(OUT,"computed.json"),"w"), indent=1)

print("3y MEAN owner earnings ($M, latest three FY on each company's own calendar)")
print(f"{'TK':<5}{'window':<16}{'mean OE(capex)':>16}{'mean OE(D&A)':>14}{'mean REV':>11}{'mean OPM%':>10}")
for tk,d in rows.items():
    ys=sorted(d)
    a=[d[y]["oec"] for y in ys if d[y]["oec"] is not None]
    b=[d[y]["oed"] for y in ys if d[y]["oed"] is not None]
    r=[d[y]["rev"] for y in ys if d[y]["rev"] is not None]
    m=[100*d[y]["op"]/d[y]["rev"] for y in ys if d[y]["op"] is not None and d[y]["rev"]]
    g=lambda v: f"{sum(v)/len(v):,.0f}" if v else "n/a"
    print(f"{tk:<5}{ys[0]+'-'+ys[-1]:<16}{g(a):>16}{g(b):>14}{g(r):>11}{(f'{sum(m)/len(m):.1f}' if m else 'n/a'):>10}")
