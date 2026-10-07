# Owner earnings rebuild, ACVA. $ thousands. Inputs from filed cash-flow statements (newest vintage) and notes.
Y=["2019","2020","2021","2022","2023","2024","2025","H1-25","H1-26"]
ocf ={"2019":-72460,"2020":10368,"2021":85290,"2022":-75175,"2023":-17885,"2024":65397,"2025":78232,"H1-25":80339,"H1-26":41012}
sbc_cf={"2019":998,"2020":5705,"2021":23220,"2022":39324,"2023":49648,"2024":68010,"2025":56862,"H1-25":32028,"H1-26":28272}
sbc_cap={"2019":0,"2020":0,"2021":472,"2022":2013,"2023":3383,"2024":5516,"2025":7602,"H1-25":3613,"H1-26":3533}
ppe ={"2019":3373,"2020":3503,"2021":2569,"2022":3211,"2023":2330,"2024":4539,"2025":9098,"H1-25":4205,"H1-26":4898}
sw  ={"2019":3220,"2020":5382,"2021":11460,"2022":20185,"2023":25840,"2024":29702,"2025":35555,"H1-25":17932,"H1-26":18491}
da  ={"2019":1839,"2020":7244,"2021":8753,"2022":11378,"2023":19285,"2024":36808,"2025":43743,"H1-25":21449,"H1-26":23956}
acq_am={"2019":100,"2020":2962,"2021":4012,"2022":4900,"2023":5500,"2024":11687,"2025":10554,"H1-25":5364,"H1-26":5190}
capsbc_am={"2019":0,"2020":0,"2021":0,"2022":555,"2023":1836,"2024":4675,"2025":6214,"H1-25":2967,"H1-26":3034}
ap  ={"2019":46409,"2020":66217,"2021":242856,"2022":-73087,"2023":-34612,"2024":16167,"2025":46823,"H1-25":85423,"H1-26":13915}
ar  ={"2019":-51952,"2020":-29226,"2021":-120155,"2022":47170,"2023":14406,"2024":17466,"2025":-31022,"H1-25":-41714,"H1-26":-23233}  # cash-flow sign
finprov={"2019":65,"2020":107,"2021":1210,"2022":4214,"2023":4286,"2024":4323,"2025":31309,"H1-25":2306,"H1-26":4584}
finnco={"2019":0,"2020":132,"2021":614,"2022":2575,"2023":3133,"2024":3560,"2025":6474,"H1-25":1400,"H1-26":25097}
acqcash={"2019":14835,"2020":5500,"2021":64500,"2022":18913,"2023":29623,"2024":156475,"2025":0}
rev={"2019":106847,"2020":208357,"2021":358435,"2022":421529,"2023":481234,"2024":637156,"2025":759606,"H1-25":376400,"H1-26":418133}
def ttm(d): return d["2025"]-d["H1-25"]+d["H1-26"]
for d in (ocf,sbc_cf,sbc_cap,ppe,sw,da,acq_am,capsbc_am,ap,ar,finprov,finnco,rev): d["TTM"]=ttm(d)
P=["2019","2020","2021","2022","2023","2024","2025","TTM"]
rows={}
print("year | OCF | float(AP+AR lines) | OCF ex-float | SBC total | fin prov | cD&A-ex | c capex | A:asfiled-capex | B:+finprov capex | C:ex-float,finprov,DAex | C:ex-float,finprov,capex | screen(OCF-SBCcf-capex)")
for y in P:
    fl=ap[y]+ar[y]; sbc=sbc_cf[y]+sbc_cap[y]
    cda=da[y]-acq_am[y]-capsbc_am[y]; ccx=ppe[y]+sw[y]
    A_da=ocf[y]-sbc-cda; A_cx=ocf[y]-sbc-ccx
    B_da=A_da-finprov[y]; B_cx=A_cx-finprov[y]
    C_da=B_da-fl; C_cx=B_cx-fl
    scr=ocf[y]-sbc_cf[y]-ppe[y]-sw[y]
    rows[y]=dict(A_da=A_da,A_cx=A_cx,B_da=B_da,B_cx=B_cx,C_da=C_da,C_cx=C_cx,fl=fl)
    print(y, ocf[y], fl, ocf[y]-fl, sbc, finprov[y], cda, ccx, A_cx, B_cx, C_da, C_cx, scr, f"margin C_cx {C_cx/rev[y]:.1%}")
yrs=P[:-1]
print("\nwindows (mean, $k): construction C (ex-float, less floorplan provision) both ends; A (as filed) both ends")
allC=[];allA=[]
for n in (3,4,5,6,7):
    for i in range(0,len(yrs)-n+1):
        w=yrs[i:i+n]
        m=lambda k: sum(rows[y][k] for y in w)/n
        allC+= [m("C_da"),m("C_cx")]; allA+=[m("A_da"),m("A_cx")]
        print(f"{w[0]}-{w[-1]} ({n}y): C DAex {m('C_da'):,.0f} | C capex {m('C_cx'):,.0f} | B capex {m('B_cx'):,.0f} | A DAex {m('A_da'):,.0f} | A capex {m('A_cx'):,.0f} | float mean {m('fl'):,.0f}")
print("C range", min(allC), max(allC), "A range", min(allA), max(allA))
print("TTM", rows["TTM"])
# screen reproduction
scr=lambda y: ocf[y]-sbc_cf[y]-ppe[y]-sw[y]
scrda=lambda y: ocf[y]-sbc_cf[y]-da[y]
print("screen 3y capex 2023-25", sum(scr(y) for y in ["2023","2024","2025"])/3, "5y capex", sum(scr(y) for y in yrs[2:])/5, "5y D&A", sum(scrda(y) for y in yrs[2:])/5, "3y D&A", sum(scrda(y) for y in ["2023","2024","2025"])/3)
# wc flag
print("AP/OCF 2021", ap["2021"]/ocf["2021"], "2025", ap["2025"]/ocf["2025"])
# cumulative
c=lambda d,ys: sum(d[y] for y in ys)
f5=yrs[2:]
print("FY21-25: OCF", c(ocf,f5), "float", c(ap,f5)+c(ar,f5), "SBC tot", c(sbc_cf,f5)+c(sbc_cap,f5), "capex+sw", c(ppe,f5)+c(sw,f5), "finprov", c(finprov,f5), "acq", c(acqcash,f5), "SBC/OCF", (c(sbc_cf,f5))/c(ocf,f5), "SBC/OCF all", c(sbc_cf,yrs)/c(ocf,yrs))
print("SBC/OCF by year", {y: round(sbc_cf[y]/ocf[y],3) if ocf[y]>0 else None for y in P})
print("SBC/OCF ex-float FY21-25", c(sbc_cf,f5)/(c(ocf,f5)-c(ap,f5)-c(ar,f5)))
print("cum OCF ex float all yrs", c(ocf,yrs)-c(ap,yrs)-c(ar,yrs), "cum SBC cf all", c(sbc_cf,yrs), "cum OCF all", c(ocf,yrs))
