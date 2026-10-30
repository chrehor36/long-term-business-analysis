"""KVUE return series on the CL run's NTOA construction (peer_metrics.py), keyed by fiscal-year END DATE,
not by calendar year of the end date: Kenvue's 52/53-week years end 2022-01-02 (fiscal 2021) and 2023-01-01
(fiscal 2022), which a year-of-end-date label collides with fiscal 2022 and 2023. Arithmetic only."""
import json,os,io,sys
from datetime import date
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__))
FN=sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,'..','companyfacts.json'); F=json.load(open(FN,encoding='utf-8'))['facts']['us-gaap']
def ser(tag,instant=False):
    out={}
    if tag not in F: return out
    for u,arr in F[tag]['units'].items():
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A') or x.get('fp')!='FY': continue
            if not instant:
                if 'start' not in x: continue
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if not 340<=d<=380: continue
            e=x['end']
            if e not in out or x['filed']>out[e][1]: out[e]=(x['val'],x['filed'])
    return {k:v[0] for k,v in out.items()}
def first(tags,instant=False):
    d={}
    for t in tags:
        for k,v in ser(t,instant).items(): d.setdefault(k,v)
    return d
M=1e6
sales=first(['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet','SalesRevenueGoodsNet']); gross=first(['GrossProfit']); op=first(['OperatingIncomeLoss'])
assets=first(['Assets'],True); cash=first(['CashAndCashEquivalentsAtCarryingValue'],True)
gw=first(['Goodwill'],True); it=first(['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],True)
rou=first(['OperatingLeaseRightOfUseAsset'],True); cl=first(['LiabilitiesCurrent'],True)
debtc=first(['DebtCurrent'],True); stb=first(['ShortTermBorrowings','LoansAndNotesPayable','CommercialPaper'],True); ltdc=first(['LongTermDebtCurrent'],True)
leasec=first(['OperatingLeaseLiabilityCurrent'],True); eq=first(['StockholdersEquity'],True); ni=first(['NetIncomeLoss'])
ends=[e for e in sorted(set(assets)&set(cl)) if e>='2015-06-01']
print('instants:',ends)
print('| FY end | sales | gross margin | op profit | op margin | NTOA | ret avg NTOA | goodwill+intang | gw share of op capital | ret incl gw+intang | NI/avg equity |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
prev=None;prevcap=None;preveq=None
for e in ends:
    d=debtc.get(e)
    if d is None: d=(stb.get(e) or 0)+(ltdc.get(e) or 0)
    ntoa=((assets[e]-(cash.get(e) or 0)-(gw.get(e) or 0)-(it.get(e) or 0)-(rou.get(e) or 0))-(cl[e]-d-(leasec.get(e) or 0)))/M
    g=((gw.get(e) or 0)+(it.get(e) or 0))/M; cap=ntoa+g
    s=sales.get(e); o=op.get(e); gp=gross.get(e); n=ni.get(e); q=(eq.get(e) or 0)/M
    avg=(ntoa+prev)/2 if prev is not None else None; avgc=(cap+prevcap)/2 if prevcap is not None else None; avge=(q+preveq)/2 if preveq else None
    f=lambda v,sp='{:,.0f}': sp.format(v) if v is not None else 'n/f'
    print(f"| {e} | {f(s/M if s else None)} | {f(gp/s if gp and s else None,'{:.1%}')} | {f(o/M if o else None)} | {f(o/s if o and s else None,'{:.1%}')} | {f(ntoa)} | {f(o/M/avg if o and avg else None,'{:.1%}')} | {f(g)} | {f(g/cap,'{:.0%}')} | {f(o/M/avgc if o and avgc else None,'{:.1%}')} | {f(n/M/avge if n and avge else None,'{:.1%}')} | debt<1y {d/M:,.0f} eq {q:,.0f}")
    prev=ntoa;prevcap=cap;preveq=q
