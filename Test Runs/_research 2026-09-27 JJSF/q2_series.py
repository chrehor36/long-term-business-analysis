import json, datetime
exec(open('xb.py').read().split('T=[')[0])
def S(t,inst=False): return ser(t,inst)
sec={}
for t in ['HeldToMaturitySecuritiesCurrent','HeldToMaturitySecuritiesNoncurrent','AvailableForSaleSecuritiesNoncurrent','AvailableForSaleSecuritiesDebtSecuritiesNoncurrent','EquitySecuritiesFvNi','AvailableForSaleSecurities']:
    s=S(t,True)
    for y,v in s.items(): sec.setdefault(y,{})[t]=v
R=json.load(open('xb_rows.json')); g=lambda n,y: R[n].get(str(y))
ti=S(['IndefiniteLivedTrademarks','IndefiniteLivedIntangibleAssetsExcludingGoodwill'],True)
fi=S(['FiniteLivedIntangibleAssetsNet'],True)
oin=S('OtherIntangibleAssetsNet',True)
print('FY   sales  gr%    GM%   OM%   OI    eq    cash  secs  debt  opcap  GW+int  OI/opcap  OI/tangopcap  ROE(NI/avg eq)')
prev=None; preveq=None
out={}
for y in range(2009,2026):
    s=g('Rev',y); oi=g('OpInc',y); eq=g('Equity',y); c=g('Cash',y) or 0
    # avoid double count: AvailableForSaleSecurities (total) vs noncurrent
    sd=sec.get(y,{})
    secs=sd.get('HeldToMaturitySecuritiesCurrent',0)+sd.get('HeldToMaturitySecuritiesNoncurrent',0)+max(sd.get('AvailableForSaleSecuritiesNoncurrent',0),sd.get('AvailableForSaleSecurities',0),sd.get('AvailableForSaleSecuritiesDebtSecuritiesNoncurrent',0))+sd.get('EquitySecuritiesFvNi',0)
    debt=(g('LTD',y) or 0)+(g('LTDc',y) or 0)
    gw=(g('GW',y) or 0); it=(g('Intang',y) or 0) or oin.get(y,0)
    if y==2024: it=182.3e6  # gross 206.5 less accumulated 24.2 (companyfacts), trade name plus other
    if y==2025: it=(105920+66730)*1e3  # balance sheet at 2025-09-27 as filed in the 10-Q to 2026-06-27: trade name 105,920 plus other 66,730
    opc=eq+debt-c-secs if eq else None
    ni=g('NI',y)
    roe=ni/((eq+preveq)/2) if preveq and eq else None
    print('%d %7.1f %5s %5.1f %5.1f %6.1f %6.1f %5.1f %5.1f %5.1f %6.1f %6.1f %7.1f%% %9s %8s'%(y,s/1e6,('%.1f'%((s/prev-1)*100)) if prev else '',g('GP',y)/s*100,oi/s*100,oi/1e6,eq/1e6,c/1e6,secs/1e6,debt/1e6,opc/1e6,(gw+it)/1e6,oi/opc*100,('%.1f%%'%(oi/(opc-gw-it)*100)) if opc-gw-it>0 else 'n/a',('%.1f%%'%(roe*100)) if roe else ''))
    out[y]=dict(sales=s,oi=oi,eq=eq,cash=c,secs=secs,debt=debt,opc=opc,gwint=gw+it)
    prev=s; preveq=eq
json.dump(out,open('q2_rows.json','w'))
