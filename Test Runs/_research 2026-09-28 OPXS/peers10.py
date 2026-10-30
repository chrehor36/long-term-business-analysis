import json,sys
sys.stdout.reconfigure(encoding='utf-8')
exec(open('peers.py',encoding='utf-8').read().split('res={}')[0])
for t in ['OPXS','ESP','CVU','AIRI','FEIM','ULBI','LPTH','POCI']:
    g=json.load(open(f'cache/peers/{t}_facts.json'))['facts']['us-gaap']
    rev=ann(g,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']); oi=ann(g,['OperatingIncomeLoss'])
    ys=[y for y in range(2012,2026) if y in rev and y in oi]
    print(t, ' '.join(f"{y%100:02d}:{oi[y]/rev[y]*100:.0f}" for y in ys))
    for a,b in [(2016,2020),(2021,2025),(2016,2025)]:
        yy=[y for y in ys if a<=y<=b]
        if yy: print('   ',a,b,len(yy), f"{sum(oi[y] for y in yy)/sum(rev[y] for y in yy):.1%}")
