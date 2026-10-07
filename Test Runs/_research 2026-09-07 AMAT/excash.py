import json, collections, sys
from datetime import date
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
def load(t):
    return json.load(open(f"companyfacts_{t}.json", encoding="utf-8"))["facts"]["us-gaap"]
def mk(US):
    def s(tag):
        if tag not in US: return {}
        by = collections.defaultdict(list)
        for u, rows in US[tag]["units"].items():
            for r in rows:
                if r.get("form") not in ("10-K","10-K/A") or r.get("fp") != "FY": continue
                if "start" in r:
                    a = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                    if not (330 <= (e-a).days <= 400): continue
                by[r["end"]].append((r["filed"], r["val"]))
        return {e: sorted(v)[0][1] for e, v in by.items()}
    return s
for T in ("AMAT","LRCX","KLAC"):
    s = mk(load(T))
    A=s("Assets");G=s("Goodwill")
    I=s("IntangibleAssetsNetExcludingGoodwill") or s("FiniteLivedIntangibleAssetsNet")
    CL=s("LiabilitiesCurrent");CD=s("LongTermDebtCurrent")
    cash=s("CashAndCashEquivalentsAtCarryingValue")
    sti=s("ShortTermInvestments") or s("AvailableForSaleSecuritiesDebtSecuritiesCurrent")
    lti=s("LongTermInvestments") or s("AvailableForSaleSecuritiesDebtSecuritiesNoncurrent")
    rev={}
    for t in ("SalesRevenueNet","RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueGoodsNet"):
        for e,v in s(t).items(): rev.setdefault(e,v)
    cogs={}
    for t in ("CostOfGoodsAndServicesSold","CostOfRevenue","CostOfGoodsSold"):
        for e,v in s(t).items(): cogs.setdefault(e,v)
    rd=s("ResearchAndDevelopmentExpense")
    sga=s("SellingGeneralAndAdministrativeExpense")
    mkt=s("SellingAndMarketingExpense"); ga=s("GeneralAndAdministrativeExpense")
    print(f"--- {T}")
    for e in sorted(A):
        if e < "2021": continue
        R=rev.get(e);C=cogs.get(e);D=rd.get(e)
        S=sga.get(e) if e in sga else ((mkt.get(e,0)+ga.get(e,0)) or None)
        if None in (R,C,D,S): print(f"  {e}  missing R={R is None} C={C is None} D={D is None} S={S is None}"); continue
        op=R-C-D-S
        nt=A[e]-G.get(e,0)-I.get(e,0)-(CL.get(e,0)-CD.get(e,0))
        cc=cash.get(e,0)+sti.get(e,0)+lti.get(e,0)
        ex=nt-cc
        print(f"  {e}  OP {op/1e6:9.1f}  NTOA {nt/1e6:9.1f}  cash+inv {cc/1e6:9.1f}  exNTOA {ex/1e6:9.1f}  RO_incl {op/nt*100:6.1f}%  RO_excash {op/ex*100:7.1f}%")
