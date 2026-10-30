# Owner cash, KION GROUP AG, EUR million, from the filed consolidated cash flow statements
# (AR2025 for 2025/2024, AR2023 for 2023/2022, AR2021 for 2021/2020, AR2019 for 2019/2018).
# OC_eq  = CFO - capex + disposals + dividends received - acquisitions + sale of businesses + sundry
#          - interest paid + interest received - financing costs - procurement leases (principal+interest)
# OC_all = OC_eq + net interest on financial debt + financing costs (before financial-debt interest; tax shield ignored)
# CFO already contains the lease and short-term rental business: fleet growth net of its own funding,
# and the interest paid/received in that business.
D = {
 2025: dict(cfo=1131.8, capex=-395.7, disp=14.3, div=13.0, acq=-34.6, sale=0.0,  sun=-19.3, ir=15.9, ip=-63.5, fc=0.0,   pl=-217.6, nwc=257.8, rev=11297.2),
 2024: dict(cfo=1170.6, capex=-462.9, disp=9.2,  div=11.6, acq=-36.7, sale=10.3, sun=-0.1,  ir=11.3, ip=-69.1, fc=0.0,   pl=-175.1, nwc=243.0, rev=11503.2),
 2023: dict(cfo=1144.0, capex=-442.8, disp=15.2, div=9.9,  acq=-2.8,  sale=0.0,  sun=-8.3,  ir=9.7,  ip=-69.7, fc=0.0,   pl=-157.9, nwc=27.5,  rev=11433.7),
 2022: dict(cfo=-345.9, capex=-382.7, disp=7.5,  div=10.5, acq=-4.9,  sale=0.0,  sun=-0.1,  ir=4.5,  ip=-32.6, fc=0.0,   pl=-151.7, nwc=-804.5,rev=11135.6),
 2021: dict(cfo=881.7,  capex=-333.8, disp=16.8, div=8.2,  acq=-17.0, sale=0.0,  sun=-12.1, ir=2.6,  ip=-29.5, fc=-7.6,  pl=-145.1, nwc=-201.9,rev=10294.3),
 2020: dict(cfo=527.1,  capex=-283.8, disp=5.7,  div=5.6,  acq=-133.5,sale=0.0,  sun=-0.3,  ir=1.5,  ip=-33.8, fc=-18.0, pl=-133.3, nwc=-150.3,rev=8341.6),
 2019: dict(cfo=846.3,  capex=-287.4, disp=3.6,  div=12.2, acq=-10.0, sale=0.0,  sun=3.8,   ir=3.1,  ip=-36.7, fc=-3.8,  pl=-126.5, nwc=-146.8,rev=8806.5),
 2018: dict(cfo=765.5,  capex=-258.5, disp=5.1,  div=14.2, acq=-1.6,  sale=0.0,  sun=-4.7,  ir=2.5,  ip=-42.9, fc=-5.0,  pl=-114.0, nwc=-54.3, rev=7995.7),
}
oc={}
for y in sorted(D):
    d=D[y]
    eq=d['cfo']+d['capex']+d['disp']+d['div']+d['acq']+d['sale']+d['sun']+d['ir']+d['ip']+d['fc']+d['pl']
    al=eq-(d['ir']+d['ip']+d['fc'])
    pre_acq_al=al-d['acq']-d['sale']
    oc[y]=(eq,al,pre_acq_al)
    print(y, 'OC_eq %7.1f  OC_all %7.1f  OC_all_before_acq %7.1f  margin_all %5.1f%%' % (eq,al,pre_acq_al,100*al/d['rev']))
def avg(ys,i): return sum(oc[y][i] for y in ys)/len(ys)
W=[2021,2022,2023,2024,2025]; C=list(range(2018,2026))
print('5y 2021-25 avg: eq %.1f all %.1f all_pre_acq %.1f' % (avg(W,0),avg(W,1),avg(W,2)))
print('8y 2018-25 avg: eq %.1f all %.1f all_pre_acq %.1f' % (avg(C,0),avg(C,1),avg(C,2)))
print('halves 2018-21 vs 2022-25 all: %.1f vs %.1f' % (avg([2018,2019,2020,2021],1),avg([2022,2023,2024,2025],1)))
print('halves 2021-22 vs 2024-25 all: %.1f vs %.1f' % (avg([2021,2022],1),avg([2024,2025],1)))
print('acq net 2021-25 %.1f ; pre-acq OC_all sum %.1f' % (sum(D[y]['acq']+D[y]['sale'] for y in W), sum(oc[y][2] for y in W)))
print('rev cagr 2021-25 %.2f%%; 2018-25 %.2f%%' % (100*((D[2025]['rev']/D[2021]['rev'])**(1/4)-1),100*((D[2025]['rev']/D[2018]['rev'])**(1/7)-1)))
print('max OC_all/rev', max(oc[y][1]/D[y]['rev'] for y in D))
