import json, sys, re
sys.stdout.reconfigure(encoding="utf-8")
def ann(d, tags):
    out = {}
    for t in tags:
        if t not in d: continue
        for u in d[t]["units"].get("USD", []):
            if u["form"]=="10-K" and u.get("start") and 350 <= (int(u["end"][:4])*365+int(u["end"][5:7])*30+int(u["end"][8:]) - (int(u["start"][:4])*365+int(u["start"][5:7])*30+int(u["start"][8:]))) <= 380:
                out.setdefault(u["end"], u["val"])
        if out: pass
    return dict(sorted(out.items()))
R = ["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet"]
for t in ["FORM","COHU","TER"]:
    d = json.load(open(f"{t}_companyfacts.json"))["facts"]["us-gaap"]
    rev = ann(d, R); gp = ann(d, ["GrossProfit"]); oi = ann(d, ["OperatingIncomeLoss"]); ocf = ann(d, ["NetCashProvidedByUsedInOperatingActivities"]); sbc = ann(d, ["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"]); cap = ann(d, ["PaymentsToAcquirePropertyPlantAndEquipment"])
    txt = open(f"{t}_10K_2025-12-{'31' if t=='TER' else '27'}.flat.txt", encoding="utf-8").read() + open(f"{t}_10K_2022-12-31.flat.txt", encoding="utf-8").read()
    print("==", t)
    for e in sorted(rev):
        if e < "2020-06": continue
        r = rev.get(e); g = gp.get(e); o = oi.get(e)
        def chk(v):
            if v is None: return "-"
            s = f"{round(abs(v)/1000):,}"
            return s + ("*" if s in txt else "?")
        print(e, "rev", chk(r), "gp", chk(g), "gm %.1f%%" % (100*g/r) if g and r else "", "oi", chk(o), "om %.1f%%" % (100*o/r) if o and r else "", "ocf", chk(ocf.get(e)), "sbc", chk(sbc.get(e)), "capex", chk(cap.get(e)))
