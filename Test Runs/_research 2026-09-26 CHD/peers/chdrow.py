"""CHD return series by the CL run's construction (peer_metrics.py), plus a goodwill-inclusive denominator.
Arithmetic only. Reads companyfacts. Operating profit = OperatingIncomeLoss (GAAP)."""
import json,sys,os
sys.path.insert(0, r'../../_research 2026-09-13 CL/peers')
HERE=os.path.dirname(os.path.abspath(__file__))
import peer_metrics as pm
pm.SALES.append("SalesRevenueGoodsNet")
def load(tk):
    p={'CHD':os.path.join(HERE,'..','companyfacts.json')}.get(tk, os.path.join(HERE,'..','..','_research 2026-09-25 PG','peers',f'{tk}_companyfacts.json'))
    return json.load(open(p,encoding='utf-8'))['facts']
pm.load=load
M=1e6
def full(tk, years):
    F=load(tk)
    rows=pm.metrics(tk, years)
    gw=pm.first(F,['Goodwill'],True); it=pm.first(F,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],True)
    pti=pm.first(F,['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'])
    ni=pm.first(F,['NetIncomeLoss'])
    eq=pm.first(F,['StockholdersEquity'],True)
    out=[];prevcap=None;preveq=None
    for y,m in rows:
        if not m: out.append((y,None)); prevcap=None; preveq=None; continue
        cap=m['ntoa']+((gw.get(y) or 0)+(it.get(y) or 0))/M
        avgc=(cap+prevcap)/2 if prevcap else cap
        e=(eq.get(y) or 0)/M; avge=(e+preveq)/2 if preveq else e
        m.update(gwint=((gw.get(y) or 0)+(it.get(y) or 0))/M, cap=cap, retcap=(m['op']/avgc if m['op'] else None),
                 roe=((ni.get(y) or 0)/M/avge if avge else None), ni=(ni.get(y) or 0)/M, eq=e)
        out.append((y,m)); prevcap=cap; preveq=e
    return out
if __name__=='__main__':
    y0=int(sys.argv[2]) if len(sys.argv)>2 else 2009
    for tk in sys.argv[1].split(','):
        print('='*60, tk)
        print('| FY | sales | gross margin | op profit | op margin | NTOA | ret avg NTOA | goodwill+intang | ret incl gw+intang | NI/avg equity |')
        print('|---|---|---|---|---|---|---|---|---|---|')
        for y,m in full(tk, range(y0,2026)):
            if not m or m['sales'] is None: continue
            f=lambda v,s='{:,.0f}': s.format(v) if v is not None else 'n/f'
            print(f"| {y} | {f(m['sales'])} | {f(m['gm'],'{:.1%}')} | {f(m['op'])} | {f(m['om'],'{:.1%}')} | {f(m['ntoa'])} | {f(m['ret'],'{:.1%}')} | {f(m['gwint'])} | {f(m['retcap'],'{:.1%}')} | {f(m['roe'],'{:.1%}')} |")
