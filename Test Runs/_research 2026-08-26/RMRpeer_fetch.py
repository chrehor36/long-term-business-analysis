import json, urllib.request, time, sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    r=urllib.request.Request(url,headers=UA)
    try: return json.load(urllib.request.urlopen(r))
    except Exception as e: return None

TAGS=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','NetIncomeLoss','ProfitLoss',
'NetIncomeLossAttributableToNoncontrollingInterest','StockholdersEquity',
'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','MinorityInterest',
'AssetManagement1Member','Assets']
PEERS={'BRDG':1854401,'AINC':1604738,'OWL':1823945,'ARES':1176948,'BAM':1937926,'RMR':1644378}

out={}
for tk,cik in PEERS.items():
    out[tk]={}
    for tag in TAGS:
        d=get(f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/us-gaap/{tag}.json')
        time.sleep(0.12)
        if not d: continue
        rows=[]
        for unit,items in d.get('units',{}).items():
            for it in items:
                # annual FY figures only, no dimensional members
                if it.get('form') not in ('10-K','20-F','40-F'): continue
                if it.get('fp')!='FY': continue
                start=it.get('start'); end=it.get('end')
                if start:
                    # duration ~ 1 year
                    from datetime import date
                    y1=date.fromisoformat(start); y2=date.fromisoformat(end)
                    if not (330 < (y2-y1).days < 400): continue
                rows.append((end,it['val'],it.get('accn'),it.get('fy'),start))
        if rows:
            seen={}
            for end,val,accn,fy,start in rows: seen[(start,end)]=(val,accn)
            out[tk][tag]=sorted([(k[1],k[0],v[0],v[1]) for k,v in seen.items()],reverse=True)[:5]
json.dump(out,open('RMRpeer_xbrl_facts.json','w'),indent=1)
for tk in PEERS:
    print('='*70); print(tk)
    for tag,rows in out[tk].items():
        print(' ',tag)
        for end,start,val,accn in rows:
            print(f'    {start} -> {end}  {val:>20,}  {accn}')
