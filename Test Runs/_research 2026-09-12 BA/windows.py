import json
s = json.load(open("Test Runs/_research 2026-09-12 BA/series.json"))
yrs = sorted(s["OCF"])
print(f"{'FY':<6}{'OCF':>10}{'SBC':>8}{'D&A':>8}{'CAPEX':>8}{'OE(D&A)':>10}{'OE(capex)':>11}")
rows={}
for y in yrs:
    ocf=s["OCF"][y]; sbc=s["SBC"].get(y); da=s["DA"].get(y); cx=s["CAPEX"].get(y)
    if sbc is None or da is None or cx is None:
        print(y[:4], "MISSING", "sbc" if sbc is None else "", "da" if da is None else "", "cx" if cx is None else ""); continue
    a=ocf-sbc-da; b=ocf-sbc-cx
    rows[y[:4]]=(ocf,sbc,da,cx,a,b)
    print(f"{y[:4]:<6}{ocf:>10,.0f}{sbc:>8,.0f}{da:>8,.0f}{cx:>8,.0f}{a:>10,.0f}{b:>11,.0f}")

def mean(ys,i):
    v=[rows[y][i] for y in ys if y in rows]
    return sum(v)/len(v), len(v)

print("\nWINDOWS (mean owner earnings, $M)")
ally=[y[:4] for y in yrs]
wins = {
 "19y FY2007-25": ally,
 "10y FY2016-25": [str(y) for y in range(2016,2026)],
 "8y  FY2018-25": [str(y) for y in range(2018,2026)],
 "7y  FY2019-25": [str(y) for y in range(2019,2026)],
 "6y  FY2020-25": [str(y) for y in range(2020,2026)],
 "5y  FY2021-25": [str(y) for y in range(2021,2026)],
 "5y  FY2014-18(pre-MAX)": [str(y) for y in range(2014,2019)],
 "4y  FY2022-25": [str(y) for y in range(2022,2026)],
 "3y  FY2023-25": [str(y) for y in range(2023,2026)],
 "2y  FY2024-25": ["2024","2025"],
 "1y  FY2025": ["2025"],
}
for k,ys in wins.items():
    a,na=mean(ys,4); b,nb=mean(ys,5)
    print(f"  {k:<24} n={na:<3} OE(D&A) {a:>10,.0f}   OE(capex) {b:>10,.0f}")

vals=[]
for k,ys in wins.items():
    if k.startswith("1y"): continue
    vals += [mean(ys,4)[0], mean(ys,5)[0]]
print(f"\nFULL BAND across windows x both (c) ends: {min(vals):,.0f} to {max(vals):,.0f}")
