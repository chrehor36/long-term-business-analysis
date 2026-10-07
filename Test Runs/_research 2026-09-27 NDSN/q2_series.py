import json
# Income statements as first filed: FY2000-2002 10-K FY2002 (0000950152-03-000680); FY2003-2005 10-K FY2005 (0000950152-06-000197);
# FY2006-2008 10-K FY2008 (0000950152-08-010466); FY2009-2011 10-K FY2011 (0001193125-11-343516); FY2012+ companyfacts ($K)
IS={2000:(740568,332597,91452,54632),2001:(731416,337129,59537,24610),2002:(647756,310542,53019,22072),
2003:(667347,301566,68221,35160),2004:(793544,354313,110470,63334),2005:(839162,371298,121667,78338),
2006:(892221,379800,147615,90598),2007:(993649,439804,152142,90692),2008:(1124829,494394,190338,117504),
2009:(819165,350239,-127807,-160055),2010:(1041551,419937,234833,168048),2011:(1233159,484727,315543,222364)}
X=json.load(open('xb_rows.json')); g=lambda n,y:(X[n].get(str(y)) or 0)/1e3
for y in range(2012,2026): IS[y]=(g('Rev',y),g('COGS',y),g('OpInc',y),g('NI',y))
B=json.load(open('oldbs.json'))
BS={}
for y in range(2001,2010):
    b=B[str(y)]; BS[y]=dict(cash=b['cash']+b['mkt'],gw=b['gw'],intang=b['intang'],debt=b['notes']+b['curltd']+b['ltd'],eq=b['equity'])
import collections
cf=json.load(open('companyfacts.json'))['facts']['us-gaap']
def inst(tag,y):
    best=None
    for u,fs in cf.get(tag,{}).get('units',{}).items():
        for f in fs:
            if f['form']=='10-K' and f['end'][:7]=='%d-10'%y and (best is None or f['filed']>best[1]): best=(f['val'],f['filed'])
    return best[0]/1e3 if best else 0.0
for y in range(2010,2026):
    BS[y]=dict(cash=g('Cash',y),gw=g('GW',y),intang=inst('FiniteLivedIntangibleAssetsNet',y) or g('Intang',y),debt=inst('LongTermDebt',y)+g('STB',y),eq=g('Equity',y))
print('FY   sales   growth  GM%   OM%   opinc   eq      debt    cash    gw+int   opcap   tangcap  op/opcap op/tang  NI/avgEq')
rows={}
for y in sorted(IS):
    s,c,o,n=IS[y]; b=BS.get(y); pb=BS.get(y-1); ps=IS.get(y-1)
    gr='%6.1f%%'%(100*(s/ps[0]-1)) if ps else '      '
    if b:
        oc=b['eq']+b['debt']-b['cash']; tc=oc-b['gw']-b['intang']
        roe=100*n/((b['eq']+pb['eq'])/2) if pb else float('nan')
        print('%d %8.1f %s %5.1f %5.1f %7.1f %7.1f %7.1f %6.1f %8.1f %7.1f %7.1f %6.1f%% %6.1f%% %6.1f%%'%(y,s/1e3,gr,100*(1-c/s),100*o/s,o/1e3,b['eq']/1e3,b['debt']/1e3,b['cash']/1e3,(b['gw']+b['intang'])/1e3,oc/1e3,tc/1e3,100*o/oc,100*o/tc,roe))
        rows[y]=dict(sales=s,gm=1-c/s,om=o/s,op=o,ni=n,opcap=oc,tangcap=tc,eq=b['eq'])
    else:
        print('%d %8.1f %s %5.1f %5.1f %7.1f'%(y,s/1e3,gr,100*(1-c/s),100*o/s,o/1e3))
        rows[y]=dict(sales=s,gm=1-c/s,om=o/s,op=o,ni=n)
json.dump(rows,open('q2_rows.json','w'))
