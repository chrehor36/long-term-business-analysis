import json
exec(open('peers.py').read().split("res={}")[0])
DT=['LongTermDebtNoncurrent','LongTermDebt','LongTermDebtAndCapitalLeaseObligations','LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities','OtherLongTermDebtNoncurrent']
CT=['LongTermDebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent','OtherLongTermDebtCurrent']
P=json.load(open('peers_extract.json'))
for tk in ['ABG','AN','LAD','GPI','PAG','SAH']:
    f=json.load(open(tk+'_facts.json'))
    g=f['facts']['us-gaap']
    def inst(tags):
        for t in tags:
            v=annual(f,[t],inst=True)
            if len(v)>8: return v,t
        return annual(f,tags,inst=True),'mixed'
    ltd,t1=inst(DT); cur,t2=inst(CT)
    d={k:{int(y):v for y,v in dd.items()} for k,dd in P[tk].items()}
    rows=[]
    for y in range(2010,2026):
        oi=d['oi'].get(y); e=d['eq'].get(y); gw=d['gw'].get(y,0) or 0; fr=d['fr'].get(y,0) or 0
        L=ltd.get(y); C=cur.get(y,0) or 0
        if None in (oi,e,L): rows.append((y,None)); continue
        cap=e+L+C-gw-fr
        rows.append((y,oi/cap*100 if cap>0 else None, cap/1e6))
    def avg(a,b,key):
        v=[d[key].get(y)/d['rev'].get(y)*100 for y in range(a,b+1) if d[key].get(y) and d['rev'].get(y)]
        return sum(v)/len(v) if v else float('nan'), len(v)
    print(tk,'debt tag',t1,'/',t2)
    print('  OM avg 2010-19 %.1f (%d)  2020-25 %.1f (%d)  2010-25 %.1f'%(avg(2010,2019,'oi')+avg(2020,2025,'oi')+(avg(2010,2025,'oi')[0],)))
    print('  PTM avg 2010-19 %.1f (%d)  2020-25 %.1f (%d)'%(avg(2010,2019,'pti')+avg(2020,2025,'pti')))
    print('  GM avg 2010-19 %.1f   2020-25 %.1f'%(avg(2010,2019,'gp')[0],avg(2020,2025,'gp')[0]))
    print('  OI/tangible capital (eq+LTD-gw-franchise):',' '.join(f"{r[0]}:{r[1]:.0f}" if len(r)>1 and r[1] else f"{r[0]}:-" for r in rows))
