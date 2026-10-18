# Owner cash for CHH, USD millions, from the filed cash-flow statements (accessions in the run file).
# columns: OCF, SBC(expense, note), PPE_total, PPE_other(maint, filer split from 2023), intang, affil_contrib, affil_dist(investing),
# notes_issued, notes_collected, acquisitions (business+asset, incl. acquired debt repaid), asset/business sale proceeds, interest_paid
D={
2016:(152.0,14.6,25.2,None,2.6,34.7,3.7,32.6,11.1,29.9,11.5,42.0),
2017:(257.4,24.9,23.4,None,2.5,50.6,4.6,19.7,0.7,0.0,1.0,42.4),
2018:(242.9,15.0,47.7,None,1.8,9.6,1.4,36.0,5.0,234.5,3.1,43.3),
2019:(270.6,16.6,57.3,None,6.7,27.8,19.2,20.7,14.2,179.7,10.6,48.2),
2020:(110.1,7.2,33.6,None,1.4,5.5,10.8,9.8,6.5,0.0,9.2,45.1),
2021:(383.7,23.4,74.3,None,3.6,2.8,15.6,20.1,0.5,0.0,6.1,43.9),
2022:(367.1,40.5,90.0,None,3.6,3.1,0.0,5.6,1.0,607.3,211.3,46.9),
2023:(296.6,40.5,116.3,47.7,2.0,38.9,0.9,4.3,10.9,0.0,0.0,60.8),
2024:(319.4,38.4,145.9,39.1,0.0,52.8,15.9,38.0,32.1,0.0,0.0,67.2),
2025:(270.4,38.3,145.8,38.9,0.0,93.7,44.6,6.9,7.4,73.4,52.0,90.3),
}
MAINT_GUESS=round((47.7+2.0+39.1+38.9)/3,1)  # CONVENTION of this run: 2023-2025 average of other PP&E + intangibles, used where filer gives no split
TAX=0.24  # interest tax shield rate, CONVENTION of this run (21% federal + state, near the filed effective rates 19.0-24.3%)
rows={}
for y,(ocf,sbc,ppe,ppeo,intg,ac,ad,ni,nc,acq,sale,intp) in D.items():
    maint=(ppeo+intg) if ppeo is not None else MAINT_GUESS
    growth_ppe=ppe+intg-maint
    oc_m=ocf-sbc-maint                         # maintenance-only, after interest
    prog=growth_ppe+(ac-ad)+(ni-nc)            # brand-support programme (owned hotels, JVs, notes)
    oc_all_pre=oc_m-prog                       # all capital spending, before acquisitions and sales
    oc_all=oc_all_pre-acq+sale                 # all spending incl. acquisitions, net of sale proceeds
    ib=intp*(1-TAX)
    rows[y]=dict(ocf=ocf,sbc=sbc,maint=maint,prog=prog,acq=acq,sale=sale,oc_m=oc_m,oc_all_pre=oc_all_pre,oc_all=oc_all,
                 oc_m_pre_int=oc_m+ib,oc_all_pre_int=oc_all+ib,oc_allpre_pre_int=oc_all_pre+ib,intp=intp)
if __name__=='__main__':
    print('maint guess',MAINT_GUESS)
    print('year   OCF   SBC  maint  prog   acq  sale | OCm  OCall-pre-acq  OCall | +int: OCm  OCall')
    for y,r in rows.items():
        print(y,'%6.1f %5.1f %5.1f %6.1f %6.1f %5.1f | %6.1f %6.1f %7.1f | %6.1f %7.1f'%(r['ocf'],r['sbc'],r['maint'],r['prog'],r['acq'],r['sale'],r['oc_m'],r['oc_all_pre'],r['oc_all'],r['oc_m_pre_int'],r['oc_all_pre_int']))
    import statistics as st
    for a,b in [(2021,2025),(2016,2020),(2019,2025),(2016,2025)]:
        ys=range(a,b+1)
        print(a,b,'avg OCm %.1f OCall-pre-acq %.1f OCall %.1f | before int: OCm %.1f OCall %.1f OCall-pre-acq %.1f'%tuple(st.mean(rows[y][k] for y in ys) for k in ['oc_m','oc_all_pre','oc_all','oc_m_pre_int','oc_all_pre_int','oc_allpre_pre_int']))
