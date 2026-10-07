# -*- coding: utf-8 -*-
import os, json, urllib.request
from datetime import date
R = "Test Runs/_research 2026-09-20 CALM/peers"
os.makedirs(R, exist_ok=True)
UA = {"User-Agent": "BRK research chrehor36@gmail.com"}
CIK = {"CALM":"0000016160","VITL":"0001579733","POST":"0001530950","PPC":"0000802481","TSN":"0000100493"}
def facts(t):
    p = f"{R}/{t}_companyfacts.json"
    if not os.path.exists(p):
        req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]}.json", headers=UA)
        open(p,'wb').write(urllib.request.urlopen(req, timeout=240).read())
    return json.load(open(p))
def ann(us, tag, dur=True):
    if tag not in us: return {}
    out={}
    for u in us[tag]["units"].get("USD",[]):
        if u.get("form") not in ("10-K","10-K/A"): continue
        if dur:
            if "start" not in u: continue
            d=(date.fromisoformat(u["end"])-date.fromisoformat(u["start"])).days
            if not (340<=d<=380): continue
        else:
            if "start" in u: continue
        if any(k not in ("start","end","val","accn","fy","fp","form","filed","frame") for k in u): continue
        k=u["end"]
        if k not in out or u["filed"]>out[k][1]: out[k]=(u["val"],u["filed"])
    return {k:v[0] for k,v in sorted(out.items())}
for t in CIK:
    us = facts(t)["facts"]["us-gaap"]
    pre = ann(us,"IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest") or ann(us,"IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments")
    ni  = ann(us,"NetIncomeLoss")
    eq  = ann(us,"StockholdersEquity", dur=False)
    ta  = ann(us,"Assets", dur=False)
    rev = ann(us,"RevenueFromContractWithCustomerExcludingAssessedTax") or ann(us,"Revenues") or ann(us,"SalesRevenueNet")
    ys = sorted(set(ni)&set(eq))[-8:]
    print(f"\n=== {t}")
    print(f"{'FYend':12}{'revenue':>12}{'pretax':>12}{'netinc':>12}{'equity':>12}{'assets':>12}{'ROE%':>8}{'pretax/TA%':>11}")
    for y in ys:
        e=eq.get(y); a=ta.get(y); p=pre.get(y); n=ni.get(y); r=rev.get(y)
        roe = 100*n/e if e else float('nan')
        pta = 100*p/a if (p and a) else float('nan')
        f=lambda v: f"{v/1e6:12.1f}" if v is not None else f"{'-':>12}"
        print(f"{y:12}{f(r)}{f(p)}{f(n)}{f(e)}{f(a)}{roe:8.1f}{pta:11.1f}")
