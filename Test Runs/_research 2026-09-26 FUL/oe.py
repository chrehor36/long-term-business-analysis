import json
cf={int(k):v for k,v in json.load(open('cf_parsed.json')).items()}
# 2005: the 2005 10-K carries no SBC line; use the 2006 10-K prior-year column (continuing operations)
cf[2005]=dict(ocf=116.152,sbc=2.278,dep=49.381,amo=2.763,capex=-25.066,ppe_sale=12.196,acq=-0.537)
fcf=json.load(open('companyfacts.json'))['facts']['us-gaap']
ip={}
for t in ['InterestPaidNet','InterestPaid']:
    for x in fcf.get(t,{}).get('units',{}).get('USD',[]):
        if x.get('fp')=='FY' and 'frame' in x and len(x['frame'])==6: ip.setdefault(int(x['frame'][2:]),x['val']/1e6)
CAP=2694.7
Y=list(range(2005,2026)); rows={}
out=open('oe_out.txt','w')
def p(*a):
    print(*a); print(*a,file=out)
p('year  OCF    SBC   netcapex  dep   amort  OE_capex OE_dep  acq    OE_capex_incl_acq  netcapex/dep  cash_int  cov  cov_acq')
for y in Y:
    r=cf[y]; nc=-r['capex']-r['ppe_sale']
    a=r['ocf']-r['sbc']-nc; b=r['ocf']-r['sbc']-r['dep']; acq=-r['acq']
    ci=ip.get(y)
    cov=(r['ocf']+ci-nc)/ci if ci else None; cova=(r['ocf']+ci-nc-acq)/ci if ci else None
    rows[y]=(a,b,a-acq)
    p(y,'%7.1f %5.1f %7.1f %6.1f %6.1f %7.1f %7.1f %7.1f %7.1f %5.2f %s %s %s'%(r['ocf'],r['sbc'],nc,r['dep'],r['amo'],a,b,acq,a-acq,nc/r['dep'],'%6.1f'%ci if ci else '   n/a','%5.1f'%cov if cov else ' n/a','%5.1f'%cova if cova else ' n/a'))
p('\nwindow  capex_end  dep_end  yld_capex  yld_dep  capex_end_incl_acq')
lo,hi=1e9,-1e9
for n in range(3,22):
    ys=Y[-n:]; m=lambda i:sum(rows[y][i] for y in ys)/n
    a,b,c=m(0),m(1),m(2); lo=min(lo,a,b); hi=max(hi,a,b)
    p('%2dy %d-%d  %7.1f %7.1f  %5.2f%% %5.2f%%  %7.1f'%(n,ys[0],ys[-1],a,b,a/CAP*100,b/CAP*100,c))
p('range %.1f to %.1f  (%.2f%% to %.2f%%)'%(lo,hi,lo/CAP*100,hi/CAP*100))
