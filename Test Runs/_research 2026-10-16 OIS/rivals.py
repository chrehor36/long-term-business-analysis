import sys; sys.path.insert(0,'.')
from facts import facts, annual
def series(cik,oi_tag,as_tag,gw_tag=None,ns='us-gaap'):
    d=facts(cik); oi=annual(d,oi_tag,'USD',ns); a=annual(d,as_tag,'USD',ns); gw=annual(d,gw_tag,'USD',ns) if gw_tag else {}
    return {y:(oi[y][0]/1e6,a[y][0]/1e6,gw.get(y,(0,))[0]/1e6,oi[y][2]) for y in oi if y in a}
out={}
out['OIS']=series(1121484,'OperatingIncomeLoss','Assets','GoodwillImpairmentLoss')
out['NOV']=series(1021860,'OperatingIncomeLoss','Assets','GoodwillImpairmentLoss')
bhi=series(808362,'OperatingIncomeLoss','Assets'); bkr=series(1701605,'OperatingIncomeLoss','Assets','GoodwillImpairmentLoss')
out['BHI/BKR']={**{y:v for y,v in bhi.items() if y<='2016'},**{y:v for y,v in bkr.items() if y>='2017'}}
out['BHI/BKR']['2015']=(-2396.0,24080.0,0.0,bhi['2015'][3])
out['TS']=series(1190723,'ProfitLossFromOperatingActivities','Assets',None,'ifrs-full')
for k,s in out.items():
    ys=[y for y in sorted(s) if '2014'<=y<='2025']
    print(k,' '.join('%s:%.1f%%'%(y[2:],100*s[y][0]/s[y][1]) for y in ys))
    oi=sum(s[y][0] for y in ys); gw=sum(s[y][2] for y in ys); a=sum(s[y][1] for y in ys)/len(ys)
    print('   years %s-%s avg OI/assets %.1f%%; ex goodwill impairment %.1f%%; accns %s'%(ys[0],ys[-1],100*oi/len(ys)/a,100*(oi+gw)/len(ys)/a, sorted(set(s[y][3] for y in ys))[-1]))
