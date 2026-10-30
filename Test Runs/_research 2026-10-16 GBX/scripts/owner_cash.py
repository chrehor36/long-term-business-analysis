# Owner cash from the filed cash-flow statements (USD millions). Sources: FY2016 10-K 0001193125-16-746547 (2014-2016),
# FY2019 10-K 0001193125-19-277713 (2017-2019), FY2022 10-K 0000950170-22-020502 (2020-2022), FY2025 10-K 0001193125-25-253612 (2023-2025).
# cols: OCF, SBC, capex, proceeds from asset sales, acquisitions, JV partner distributions net of partner investment,
#       affiliates net (distributions received less investment/advances), cash interest paid, D&A, revenue, earnings from operations
D = {
2014:(135.9,11.3, 70.2, 54.2,  0.0,  4.7,-13.8,14.3, 40.4,2204.0,239.5),
2015:(192.3,19.5,106.0,  5.3,  0.0, 20.4,-31.1,15.5, 45.2,2605.3,386.9),
2016:(331.7,24.0,139.0,103.7,  0.0, 89.7, -5.0,12.3, 63.3,2679.5,408.6),
2017:(285.6,26.4, 86.1, 24.1, 27.1, 28.5,-40.1,14.0, 65.1,2169.2,260.4),
2018:(103.3,29.3,176.8,153.2, 34.9, 66.5,-21.8,18.9, 74.4,2519.5,253.0),
2019:(-21.2,11.2,198.2,125.4,361.9, 16.9, -9.3,18.3, 83.7,3033.6,184.1),
2020:(272.2, 9.0, 66.9, 83.5,  0.0, 38.9, 10.9,31.7,109.9,2792.2,168.4),
2021:(-40.5,14.7,139.0, 15.9,  0.0, 18.3,  5.3,28.1,100.7,1747.9, 41.0),
2022:(-150.4,15.5,380.7,155.5, 0.0, 16.9,  1.2,45.1,102.0,2977.7,118.0),
2023:( 71.2,12.1,362.1, 78.8,  0.0, 13.0,  3.3,70.0,106.3,3944.0,176.4),
2024:(329.6,17.1,398.3, 75.0,  0.0,  9.3,  2.9,85.7,115.6,3544.7,324.5),
2025:(265.7,17.5,280.4, 77.3,  0.0, 17.9,  0.0,82.2,121.5,3240.2,360.1),
}
T = 0.25  # CONVENTION of the run: tax shield on interest added back
def oc(y, basis='eq', capex='all'):
    ocf,sbc,cx,pr,acq,jv,aff,intr,da,rev,eo = D[y]
    if capex=='all':   spend = cx - pr + acq
    elif capex=='noacq': spend = cx - pr
    elif capex=='maint': spend = da            # depreciation as the maintenance guess
    v = ocf - sbc - spend - jv + aff
    if basis=='all': v += intr*(1-T)
    return v
if __name__=='__main__':
    print('year  eq_all  eq_noacq  eq_maint | AE_all AE_noacq AE_maint | rev   EO')
    for y in sorted(D):
        print(y, *['%7.1f'%oc(y,'eq',c) for c in ('all','noacq','maint')], '|', *['%7.1f'%oc(y,'all',c) for c in ('all','noacq','maint')], '| %7.1f %6.1f'%(D[y][9],D[y][10]))
    for lo,hi in [(2021,2025),(2016,2025),(2014,2025),(2016,2020),(2021,2025)]:
        ys=range(lo,hi+1)
        avg=lambda b,c: sum(oc(y,b,c) for y in ys)/len(ys)
        print(lo,hi,'avg eq_all %.1f eq_maint %.1f | AE_all %.1f AE_noacq %.1f AE_maint %.1f | rev %.0f'%(avg('eq','all'),avg('eq','maint'),avg('all','all'),avg('all','noacq'),avg('all','maint'), sum(D[y][9] for y in ys)/len(ys)))
