import json,sys
def ratios(d, units=None):
    out=[]
    for y,v in d.items():
        rev,gb,op,ocf,sbc,capex,mkt = [v.get(k) for k in ("rev","gb","op","ocf","sbc","capex","mkt")]
        r={"y":y}
        r["take"]= f"{rev/gb*100:.2f}%" if gb else "n/d"
        r["opm"]= f"{op/rev*100:.1f}%"
        r["sbc_ocf"]= f"{sbc/ocf*100:.1f}%" if ocf and ocf>0 else "n/m"
        r["capex_rev"]= f"{capex/rev*100:.1f}%"
        r["fcf_sbc_rev"]= f"{(ocf-sbc-capex)/rev*100:.1f}%"
        r["mkt_rev"]= f"{mkt/rev*100:.1f}%" if mkt is not None else "n/d"
        out.append(r)
    return out
BKNG={
"2019":dict(rev=15066,gb=96443,op=5345,ocf=4865,sbc=325,capex=368,mkt=4967),
"2020":dict(rev=6796,gb=35395,op=-631,ocf=85,sbc=255,capex=286,mkt=2179),
"2021":dict(rev=10958,gb=76586,op=2496,ocf=2820,sbc=376,capex=304,mkt=3801),
"2022":dict(rev=17090,gb=121253,op=5102,ocf=6554,sbc=404,capex=368,mkt=5993),
"2023":dict(rev=21365,gb=150627,op=5835,ocf=7344,sbc=530,capex=345,mkt=6773),
"2024":dict(rev=23739,gb=165580,op=7555,ocf=8323,sbc=599,capex=429,mkt=7278),
"2025":dict(rev=26917,gb=186107,op=8825,ocf=9409,sbc=617,capex=322,mkt=8186),
"H1 2025":dict(rev=11560,gb=93406,op=3312,ocf=6484,sbc=297,capex=185,mkt=3916),
"H1 2026":dict(rev=12884,gb=104716,op=3771,ocf=6934,sbc=281,capex=183,mkt=4439),
}
if __name__=="__main__":
    d=eval(sys.argv[1])
    for r in ratios(d): print(r)
    ks=[k for k in d if k.isdigit() and "2021"<=k<="2025"]
    s=sum(d[k]["sbc"] for k in ks); o=sum(d[k]["ocf"] for k in ks)
    print("SBC/OCF 2021-25 cum", s, o, f"{s/o*100:.1f}%")
    print("2020 vs 2019 rev", f"{(d['2020']['rev']/d['2019']['rev']-1)*100:.1f}%", "gb", f"{(d['2020']['gb']/d['2019']['gb']-1)*100:.1f}%" if d['2019'].get('gb') else "")
