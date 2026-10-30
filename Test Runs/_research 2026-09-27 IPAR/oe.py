import json
x=json.load(open('xb_rows.json')); g=lambda k,y: (x[k].get(str(y)) or 0)/1e6
CAP=117.93*32025781/1e6; USD=5.49; EUR=3.74
R={}
# FY2003-FY2008 from the filed cash-flow statements (10-Ks for FY2005 and FY2008), $M; NI attributable and minority from the same statements
pre={2003:(19.346,0.0,2.545,0.0,3.344,13.837,3.392),2004:(-4.383,0.0,3.254,24.465+4.481,3.988,15.703,4.393),2005:(30.380,0.0,2.429,0.465,4.513,15.263,5.328),
     2006:(13.367,0.625,3.452,5.042,5.347,17.742,6.192),2007:(38.517,1.096,2.380,58.723,8.031,23.817,6.784),2008:(-6.428,1.119,3.803,1.095,9.925,23.765,6.357)}
for y,(ocf,sbc,cx,intg,da,ni,nci) in pre.items(): R[y]=dict(ocf=ocf,sbc=sbc,cx=cx,intg=intg,da=da,ni=ni,nci=nci)
imp={2021:2.4,2022:7.7,2024:4.0}
for y in range(2009,2026):
    da=g('DA',y)-imp.get(y,0)
    R[y]=dict(ocf=g('OCF',y),sbc=g('SBC',y),cx=g('Capex',y),intg=g('IntangBuy',y),da=da,ni=g('NI',y),nci=g('NIminor',y))
R['TTM']=dict(ocf=214.900-4.510+45.667,sbc=1.568-0.946+0.850,cx=24.414-16.631+2.389,intg=23.786-23.852+2.736,da=25.302-12.291+11.631,ni=168.387,nci=39.758)
# Burberry exit tax: accrued in FY2012 OCF (income taxes +81.1), paid in FY2013; the gain's cash was investing
btax={2012:-81.062,2013:81.062}
print('FY | OCF | SBC | capex | licence and brand payments | D&A ex impairment | attributable share | OE capex end | OE D&A end | OE capex + intangibles | capex end, Burberry tax normalized')
for y in list(range(2003,2026))+['TTM']:
    r=R[y]; r['att']=r['ni']/(r['ni']+r['nci'])
    r['A']=r['ocf']-r['sbc']-r['cx']; r['B']=r['ocf']-r['sbc']-r['da']; r['C']=r['A']-r['intg']; r['An']=r['A']+btax.get(y,0); r['Bn']=r['B']+btax.get(y,0); r['Cn']=r['C']+btax.get(y,0)
    print(f"{y} | {r['ocf']:.1f} | {r['sbc']:.1f} | {r['cx']:.1f} | {r['intg']:.1f} | {r['da']:.1f} | {100*r['att']:.1f}% | {r['A']:.1f} | {r['B']:.1f} | {r['C']:.1f} | {r['An']:.1f}")
ys=list(range(2003,2026))
def win(n,k,end=2025):
    yy=[y for y in ys if end-n<y<=end]; return sum(R[y][k] for y in yy)/len(yy), sum(R[y][k]*R[y]['att'] for y in yy)/len(yy)
print('\nwindow | capex end | D&A end | capex+intangibles | (normalized for the Burberry tax) | attributable to IPAR owners, three ends | yields on cap, consolidated, three ends')
allv=[];alla=[]
for n in range(1,24):
    a=win(n,'An'); b=win(n,'Bn'); c=win(n,'Cn')
    allv+= [a[0],b[0],c[0]]; alla+=[a[1],b[1],c[1]]
    print(f"{n}y ({2026-n}-2025) | {a[0]:.1f} | {b[0]:.1f} | {c[0]:.1f} | att {a[1]:.1f} / {b[1]:.1f} / {c[1]:.1f} | {100*a[0]/CAP:.2f}% / {100*b[0]/CAP:.2f}% / {100*c[0]/CAP:.2f}%")
print('\nas filed (not tax-normalized), 5y:', [round(win(5,k)[0],1) for k in ('A','B','C')], '10y:',[round(win(10,k)[0],1) for k in ('A','B','C')])
print('ALL windows consolidated min/max', round(min(allv),1), round(max(allv),1), '%.2f-%.2f%%'%(100*min(allv)/CAP,100*max(allv)/CAP))
print('ALL windows attributable min/max', round(min(alla),1), round(max(alla),1), '%.2f-%.2f%%'%(100*min(alla)/CAP,100*max(alla)/CAP))
t=R['TTM']; print('TTM', round(t['A'],1), round(t['B'],1), round(t['C'],1), 'att', round(t['A']*t['att'],1), round(t['B']*t['att'],1), round(t['C']*t['att'],1), 'yields %.2f/%.2f/%.2f'%(100*t['A']/CAP,100*t['B']/CAP,100*t['C']/CAP))
print('cap', round(CAP,1))
print('\nrolling five-year means, capex end / D&A end / capex+intangibles (normalized)')
for e in range(2007,2026): print(e-4,e,[round(win(5,k,e)[0],1) for k in ('An','Bn','Cn')])
print('\nscreen reproduction: 5y capex end as filed', round(win(5,'A')[0],1),' 3y capex end as filed', round(win(3,'A')[0],1))
print('SBC/OCF', {y:round(100*R[y]['sbc']/R[y]['ocf'],1) for y in range(2006,2026) if R[y]['ocf']>0})
json.dump({str(k):v for k,v in R.items()},open('oe_rows.json','w'),indent=0)
