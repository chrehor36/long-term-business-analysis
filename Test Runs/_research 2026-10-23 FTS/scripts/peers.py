"""Peer comparison from SEC companyfacts (10-K). ROE on average common equity, OCF less capex, by year."""
import json, urllib.request, time, sys
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
peers = {"AEE Ameren": "0001002910", "XEL Xcel Energy": "0000072903", "PNW Pinnacle West": "0000764622", "FTS Fortis": "0001666175"}
def get(cik):
    r = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers=UA)
    return json.load(urllib.request.urlopen(r, timeout=60))
def series(g, tags, dur=True):
    for t in tags:
        if t not in g: continue
        out = {}
        for x in list(g[t]['units'].values())[0]:
            if x.get('form') not in ('10-K', '40-F'): continue
            if dur:
                if 'start' not in x: continue
                from datetime import date
                if not 340 <= (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days <= 380: continue
            y = int(x['end'][:4])
            if y not in out or x['filed'] > out[y][1]: out[y] = (x['val'], x['filed'])
        if out: return {k: v[0] for k, v in out.items()}, t
    return {}, None
for name, cik in peers.items():
    g = get(cik)['facts']['us-gaap']; time.sleep(0.3)
    ni, t1 = series(g, ['NetIncomeLossAvailableToCommonStockholdersBasic', 'NetIncomeLoss'])
    eq, t2 = series(g, ['StockholdersEquity'], dur=False)
    ocf, _ = series(g, ['NetCashProvidedByUsedInOperatingActivities'])
    cap, t4 = series(g, ['PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets'])
    rev, _ = series(g, ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax'])
    print(f"\n{name}  (NI tag {t1}; capex tag {t4})")
    print("year | NI | avg equity | ROE % | OCF | capex | OCF-capex | revenue")
    rs = []
    for y in range(2016, 2026):
        if y in ni and y in eq and (y-1) in eq:
            ae = (eq[y] + eq[y-1]) / 2; roe = 100 * ni[y] / ae; rs.append(roe)
            print(f"{y} | {ni[y]/1e6:,.0f} | {ae/1e6:,.0f} | {roe:.1f} | {ocf.get(y,0)/1e6:,.0f} | {cap.get(y,0)/1e6:,.0f} | {(ocf.get(y,0)-cap.get(y,0))/1e6:,.0f} | {rev.get(y,0)/1e6:,.0f}")
    if rs: print(f"mean ROE {sum(rs)/len(rs):.1f}% over {len(rs)} years")
