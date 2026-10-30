# COMPUTATION, NOT A CLEARANCE. Figures transcribed from the filed statements (accessions in the run file).
yrs={ # OCF, capex, SBC, stock for services, cash interest paid, revenue, operating income
 'FY2022':(-107162,-29354,13074,0,None,8363600,-36283),
 'FY2023':(-117892,-73571,5553,0,None,9209329,60881),
 'FY2024':(-1560375,0,196437,0,28157,6891223,-1745155),
 'FY2025':(-2065017,0,431005,125000,221880,3875793,-3698754),
}
oc={}
for y,(ocf,cx,sbc,svc,intp,rev,oi) in yrs.items():
    oc[y]=ocf+cx-sbc-svc
    print(y,'owner cash after every real cost',oc[y],'| before cash interest',oc[y]+(intp or 0),'| op margin %.1f%%'%(100*oi/rev))
avg=sum(oc.values())/len(oc); print('four-year average',round(avg))
h1=(oc['FY2022']+oc['FY2023'])/2; h2=(oc['FY2024']+oc['FY2025'])/2; print('halves',round(h1),round(h2))
# TTM to 2026-07-31
ocf9_26,sbc9_26,svc9_26=-1937196,81159,2481918
ocf9_25,sbc9_25=-1549753,126603
q4_ocf=-2065017-ocf9_25; q4_sbc=431005-sbc9_25; q4_svc=125000
ttm=ocf9_26+q4_ocf-(sbc9_26+svc9_26+q4_sbc+q4_svc)
print('TTM owner cash',ttm,'(Q4FY25 OCF',q4_ocf,')')
r=0.0543; shares=5190024; price=4.55
debt=680500+202930+70000+165000; cash=520504+126950
nd=debt-cash; print('net debt incl. 2026-09-01 note',nd)
for label,c in [('four-year average',avg),('TTM',ttm),('best year FY2022',oc['FY2022'])]:
    v=c/r; f=c/0.10
    print(label,'value at sovereign (no growth, perpetuity) %.0f -> per share %.2f'%(v,(v-nd)/shares),'| at 10%% %.0f -> per share %.2f'%(f,(f-nd)/shares))
print('market cap',shares*price)
print('derivative liability 1,655,559 and mezzanine preferred 333,096 left out of net debt')
print('--- the two bases')
pre=[-149590,-197016,-1756812+28157,-2621022+221880]
apre=sum(pre)/4; print('all-equity: avg owner cash before cash interest',round(apre))
for rate in (r,0.10):
    v=apre/rate; print(' rate',rate,'business %.0f, less net debt, per share %.2f'%(v,(v-nd)/shares))
for rate in (r,0.10):
    v=avg/rate; print(' equity-only rate',rate,'equity %.0f per share %.2f'%(v,v/shares))
