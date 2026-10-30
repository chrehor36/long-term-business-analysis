import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch import get
from datetime import date
peers={'TEX':97216,'REVG':1687221,'FSS':277509,'MLR':924822}
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for tk,cik in peers.items():
    fn=f'{tk}_facts.json'
    if not os.path.exists(fn): open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json'))
    d=json.load(open(fn))['facts']['us-gaap']
    def annual(tags):
        out={}
        for tag in tags:
            if tag not in d: continue
            for u,arr in d[tag]['units'].items():
                for x in arr:
                    if x.get('form')=='10-K' and 'start' in x:
                        s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                        if 340<(e-s).days<380: out.setdefault(x['end'][:4],x['val'])
        return out
    rev=annual(['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi=annual(['OperatingIncomeLoss'])
    print(tk, ' '.join(f"{y}:{oi[y]/rev[y]*100:.1f}%" for y in sorted(oi) if y in rev and y>='2008'))
