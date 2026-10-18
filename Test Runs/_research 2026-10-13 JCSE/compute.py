# JCSE arithmetic, SGD thousands, from the filed 20-F statements (see notes.md for accessions).
yrs=[2019,2020,2021,2022,2023,2024,2025]
cfo  ={2019:1545,2020:1114,2021:3373,2022:-5239,2023:1375,2024:2053,2025:2686}
capex={2019:615,2020:280,2021:788,2022:817,2023:211,2024:1253,2025:829}
leasefin={2019:108,2020:95,2021:0,2022:0,2023:0,2024:0,2025:58}   # lease principal shown in financing
sbc  ={2019:0,2020:0,2021:0,2022:0,2023:0,2024:466,2025:0}       # added back inside CFO
intr ={2019:458,2020:320,2021:217,2022:336,2023:511,2024:516,2025:412}
rev  ={2019:18219,2020:21397,2021:14764,2022:18631,2023:18032,2024:19279,2025:20296}
opinc={2019:2313,2020:3534,2021:59,2022:1764,2023:1010,2024:-30,2025:610}
T=0.17
oc_eq={y:cfo[y]-capex[y]-leasefin[y]-sbc[y] for y in yrs}
oc_all={y:oc_eq[y]+intr[y]*(1-T) for y in yrs}
for y in yrs: print(y, 'rev',rev[y],'opinc',opinc[y],'OC equity-only',oc_eq[y],'OC all-equity',round(oc_all[y]))
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
for name,ys in [('5yr 2021-25',[2021,2022,2023,2024,2025]),('cycle 2020-25 peak-to-peak',[2020,2021,2022,2023,2024,2025]),('7yr 2019-25',yrs)]:
    print(name,'avg OC eq',round(avg(oc_eq,ys)),'avg OC all',round(avg(oc_all,ys)), 'avg rev',round(avg(rev,ys)))
r=0.0273  # SGS 50-year benchmark, MAS, 2026-10-12
fx=1.2793 # S$ per US$, MAS noon 2026-10-12
shares=5536666
price_usd=1.51
mcap=shares*price_usd*fx/1000
cash=9931; bank=1152+2870; lease=191+217
netdebt=bank+lease-cash
div_usd=2314514; fraud_sgd=1009; car=285
div_sgd=div_usd*1.2693/1000  # filing's own implied rate (US$794,934 = S$1,009,000)
netdebt_adj=netdebt+div_sgd+fraud_sgd+car
print('mcap S$k',round(mcap),'net debt Dec25',netdebt,'adj',round(netdebt_adj),'EV',round(mcap+netdebt_adj))
for name,ys in [('cycle',[2020,2021,2022,2023,2024,2025]),('5yr',[2021,2022,2023,2024,2025]),('7yr',yrs)]:
    a=avg(oc_all,ys); e=avg(oc_eq,ys)
    v_gov=a/r; v10=a/0.10
    eq_gov=v_gov-netdebt_adj; eq10=v10-netdebt_adj
    print(name,'all-eq value at SGS S$k',round(v_gov),'per sh S$',round(eq_gov*1000/shares,2),'US$',round(eq_gov*1000/shares/fx,2),
          '| fair (10%) per sh S$',round(eq10*1000/shares,2),'US$',round(eq10*1000/shares/fx,2),
          '| equity-only at 10% US$',round(e/0.10*1000/shares/fx,2),'at SGS US$',round(e/r*1000/shares/fx,2),
          '| yield on EV',round(a/(mcap+netdebt_adj)*100,1),'%','| eq-only yield on mcap',round(e/mcap*100,1),'%')
print('owner cash needed for 10% on EV S$k', round(0.10*(mcap+netdebt_adj)))

# Capital employed = equity + bank loans + lease payables + shareholder loan - cash (year end), from the filed balance sheets
eq  ={2019:4164,2020:5945,2021:3023,2022:16281,2023:16713,2024:16493,2025:19772}
bk  ={2019:11185,2020:10516,2021:9878,2022:9433,2023:7981,2024:8794,2025:4022}
ls  ={2019:1283,2020:1259,2021:1553,2022:1686,2023:1583,2024:1278,2025:408}
shl ={2019:0,2020:0,2021:1523,2022:741,2023:0,2024:0,2025:0}
ca  ={2019:843,2020:550,2021:1108,2022:6561,2023:5089,2024:5742,2025:9931}
ce={y:eq[y]+bk[y]+ls[y]+shl[y]-ca[y] for y in yrs}
for y in yrs: print(y,'cap employed',ce[y],'op inc',opinc[y],'pre-tax ROCE %',round(opinc[y]/ce[y]*100,1),'OC all-eq / CE %',round(oc_all[y]/ce[y]*100,1))
print('7yr op inc avg',round(avg(opinc,yrs)),'avg CE',round(avg(ce,yrs)),'ratio %',round(avg(opinc,yrs)/avg(ce,yrs)*100,1))
print('7yr OC all avg / avg CE %',round(avg(oc_all,yrs)/avg(ce,yrs)*100,1))
seg_gp_clean={2019:4529,2020:5721,2021:2090,2022:4330,2023:3421,2024:4293,2025:4655}
gp_tot={2019:4951,2020:5904,2021:2348,2022:5128,2023:4366,2024:5194,2025:5775}
for y in yrs: print(y,'clean GP',seg_gp_clean[y],'dish GP',gp_tot[y]-seg_gp_clean[y])
s5=[2021,2022,2023,2024,2025]
print('5yr clean GP share %', round(sum(seg_gp_clean[y] for y in s5)/sum(gp_tot[y] for y in s5)*100,1))

# Working-capital-neutral case (Q7 specific (d), shown beside): CFO less the working-capital lines of the filed cash-flow statements
wc={2019:327+1077-1217, 2020:1597-4549+1508, 2021:-1177+5537-1480, 2022:-9335-2495+374+4319,
    2023:-2181+753-757+2641, 2024:1429+19-407-300+40, 2025:3442-1228+995-845+83}
oc_eq_n={y:cfo[y]-wc[y]-capex[y]-leasefin[y]-sbc[y] for y in yrs}
oc_all_n={y:oc_eq_n[y]+intr[y]*(1-T) for y in yrs}
for y in yrs: print(y,'WC lines',wc[y],'WC-neutral OC eq',oc_eq_n[y],'all',round(oc_all_n[y]))
EV=mcap+netdebt_adj
for name,ys in [('cycle',[2020,2021,2022,2023,2024,2025]),('5yr',[2021,2022,2023,2024,2025]),('7yr',yrs)]:
    a=avg(oc_all_n,ys); e=avg(oc_eq_n,ys)
    print('WC-neutral',name,'avg all',round(a),'avg eq',round(e),'value@SGS US$/sh',round((a/r-netdebt_adj)*1000/shares/fx,2),
          'fair@10% US$/sh',round((a/0.10-netdebt_adj)*1000/shares/fx,2),'eq-only@10% US$/sh',round(e/0.10*1000/shares/fx,2),'yield on EV %',round(a/EV*100,1))
print('net WC/revenue: 2019',round((4839+3097+220-2188-29)/18219*100,1),'2020',round((9230+1380+326-3296)/21397*100,1),'2021',round((3220+2557+847-2290)/14764*100,1),'2025',round((7411+9202+837-2673-5815)/20296*100,1))
print('D&A avg',round(sum([972,769,614,672,702,980,861])/7),'capex avg',round(avg(capex,yrs)))
print('rev CAGR 2019-25 %',round(((rev[2025]/rev[2019])**(1/6)-1)*100,1),'2020-25 %',round(((rev[2025]/rev[2020])**(1/5)-1)*100,1))
