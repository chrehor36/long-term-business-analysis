import json, sys
from datetime import date
def ann(d, tag, dur=True):
    g = d["facts"]["us-gaap"].get(tag)
    if not g: return {}
    out = {}
    for unit, arr in g["units"].items():
        if unit != "USD": continue
        for f in arr:
            if f.get("form") not in ("10-K","10-K/A","10-KT"): continue
            e = f["end"]
            if dur:
                if not f.get("start"): continue
                s = f["start"]; y1,m1,d1=map(int,s.split("-")); y2,m2,d2=map(int,e.split("-"))
                if (date(y2,m2,d2)-date(y1,m1,d1)).days < 350: continue
            elif f.get("start"): continue
            # keep fiscal-year-end facts: map by end date; first filed wins
            out.setdefault(e, f["val"])
    return out
for path in sys.argv[1:]:
    d = json.load(open(path, encoding="utf-8"))
    ni = {}
    for t in ["NetIncomeLossAttributableToParent","NetIncomeLoss","ProfitLoss"]:
        for k,v in ann(d,t).items(): ni.setdefault(k,v)
    eq = {}
    for t in ["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest","MembersEquity","MembersEquityIncludingPortionAttributableToNoncontrollingInterest"]:
        for k,v in ann(d,t,dur=False).items(): eq.setdefault(k,v)
    rev = {}
    for t in ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RealEstateRevenueNet","SalesRevenueNet"]:
        for k,v in ann(d,t).items(): rev.setdefault(k,v)
    print("==", d["entityName"])
    ends = sorted(k for k in ni if k >= "2014")
    tot_ni=tot_eq=0; n=0
    for e in ends:
        # prior year-end equity
        prev = [k for k in eq if k < e and (date(*map(int,e.split('-')))-date(*map(int,k.split('-')))).days in range(330,400)]
        eq0 = eq[prev[0]] if prev else None
        eq1 = eq.get(e)
        avg = (eq0+eq1)/2 if eq0 and eq1 else None
        roe = ni[e]/avg*100 if avg else None
        r = rev.get(e)
        print(f"  FY end {e}: revenue {r/1e6 if r else float('nan'):9.1f}M  net income {ni[e]/1e6:8.1f}M  avg equity {avg/1e6 if avg else float('nan'):9.1f}M  ROE {roe if roe is not None else float('nan'):6.1f}%")
        if avg: tot_ni+=ni[e]; tot_eq+=avg; n+=1
    if n: print(f"  span {n} yrs: sum NI / sum avg equity = {tot_ni/tot_eq*100:.1f}%")
