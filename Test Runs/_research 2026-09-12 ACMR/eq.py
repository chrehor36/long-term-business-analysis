import json, io, datetime
d=json.load(io.open("Test Runs/_research 2026-09-12 ACMR/companyfacts.json",encoding="utf-8"))
us=d["facts"]["us-gaap"]; dei=d["facts"].get("dei",{})
def inst(tag, unit="USD"):
    out={}
    for f in us.get(tag,{}).get("units",{}).get(unit,[]):
        if f.get("form") not in ("10-K","10-K/A") or f.get("start"): continue
        if not f["end"].endswith("12-31"): continue
        k=f["end"]; p=out.get(k)
        if p is None or f["filed"]>p[1]: out[k]=(f["val"],f["filed"])
    return dict(sorted(out.items()))
def dur(tag, unit):
    out={}
    for f in us.get(tag,{}).get("units",{}).get(unit,[]):
        if f.get("form") not in ("10-K","10-K/A") or not f.get("start"): continue
        a=datetime.date.fromisoformat(f["start"]); b=datetime.date.fromisoformat(f["end"])
        if not 330<=(b-a).days<=400: continue
        k=f["end"]; p=out.get(k)
        if p is None or f["filed"]>p[1]: out[k]=(f["val"],f["filed"])
    return dict(sorted(out.items()))
for t in ["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest","MinorityInterest","Assets","CashAndCashEquivalentsAtCarryingValue","IncomeTaxesPaidNet","IncomeTaxesPaid","IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"]:
    s=inst(t) if not t.startswith("IncomeTax") and not t.startswith("IncomeLoss") else dur(t,"USD")
    print(t); [print("  ",k,f"{v[0]:,}") for k,v in s.items()]
s=dur("WeightedAverageNumberOfSharesOutstandingBasic","shares")
print("WeightedAverageNumberOfSharesOutstandingBasic"); [print("  ",k,f"{v[0]:,}", v[1]) for k,v in s.items()]
