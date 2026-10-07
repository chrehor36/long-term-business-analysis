# Owner earnings from filed cash-flow statements ($K). Sources: 10-K FY2016 (2014-16), FY2019 (2017-19), FY2022 (2020-22), FY2025 (2023-25)
# yr: (OCF, SBC, D&A, capex, WC_sum, acq)
D={2014:(3253,330,143,679,-281-144-495-190+348+72,0),
2015:(3027,262,660,168,-4017+348+699+953+1094+191,16987),
2016:(2292,408,1016,105,-1987-173-250+1680-945-145,0),
2017:(3347,381,1942,1127,-3322-618+1685+472+1000+234,34799),
2018:(-471,470,3182,771,-7428+283-901-1241-461-172,0),
2019:(16084,936,3434,1014,5648-386-100+174-264-21,0),
2020:(21231,2021,3589,298,2133+251-1613+6287+91+146,9345),
2021:(5216,2212,3979,1895,-11389-2544+2365-429+202+66,0),
2022:(12615,2225,4195,835,1021+95-479-3155-41-337,0),
2023:(15978,3082,3855,335,12537-1718+186+1276-248+477,0),
2024:(7192,2200,3499,941,-1411-1605+39+1452-386-355,0),
2025:(11135,3118+617,3324,376,5013+1729-1215+1756+357-288,0)}
# 2025 SBC includes the $616,932 CEO 2025 bonus accrued as cash and settled in 100,314 shares on 2026-03-30 (10-Q Q2 2026 note 7): stock pay outside the SBC line
# CARES payroll tax deferral: +4.6M in 2020 OCF, repaid 2.3M 2021 and 2.3M 2022 (10-K FY2020 Note 8; FY2021 liquidity)
cares={2020:4600,2021:-2300,2022:-2300}
rows={}
print('yr   OCF    SBC   D&A  capex   WC   | OEcap  OEda | preWC_cap preWC_da | OCF-cares cap/da')
for y,(o,s,d,c,w,a) in D.items():
    oc=o-s-c; od=o-s-max(d,c)
    pc=o-w-s-c; pd=o-w-s-max(d,c)
    xc=o-cares.get(y,0)-s-c; xd=o-cares.get(y,0)-s-max(d,c)
    rows[y]=(oc,od,pc,pd,xc,xd)
    print(y,o,s,d,c,w,'|',oc,od,'|',pc,pd,'|',xc,xd)
def win(a,b,k):
    v=[rows[y][k] for y in range(a,b+1)]; return sum(v)/len(v)/1000
print()
for name,(a,b) in {'3y 2023-25':(2023,2025),'5y 2021-25':(2021,2025),'7y 2019-25':(2019,2025),'10y 2016-25':(2016,2025),'12y 2014-25':(2014,2025),'FY2025':(2025,2025),'5y 2016-20':(2016,2020)}.items():
    print(name,'OCF-based cap %.1f da %.1f | preWC cap %.1f da %.1f | CARES-stripped cap %.1f da %.1f'%(win(a,b,0),win(a,b,1),win(a,b,2),win(a,b,3),win(a,b,4),win(a,b,5)))
print('cum acq',sum(v[5] for v in D.values()))
print('cum OE 12y OCF cap/da',sum(r[0] for r in rows.values()),sum(r[1] for r in rows.values()))
print('sbc/ocf 5y',sum(D[y][1] for y in range(2021,2026))/sum(D[y][0] for y in range(2021,2026)))
