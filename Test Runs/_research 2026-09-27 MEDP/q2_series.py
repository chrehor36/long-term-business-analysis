import json
x=json.load(open('xb_rows.json')); g=lambda k,y: x[k].get(str(y),0)/1e6
reimb={2015:39.0,2016:51.0,2017:49.7,2018:236.775,2019:294.266,2020:292.773,2021:373.132,2022:492.671,2023:723.088,2024:770.654,2025:1037.488}
print('FY | total rev | pass-through | service rev | svc growth | op inc | amort | EBITA/svc | EBITA/total | op capital incl GW | net recv days (on total) | adv billings/total')
prev=None
for y in range(2015,2026):
    tot=g('Rev',y) or g('RevNet',y)
    svc = g('RevSvc',y) if y<=2017 else tot-reimb[y]
    if y<=2017: tot=svc+reimb[y]
    op=g('OpInc',y); am=g('Amort',y)
    ta=g('Liab',y)+g('Equity',y); cash=g('Cash',y); li=g('Liab',y); debt=g('Debt',y)+g('DebtC',y)+g('STB',y)
    cap=ta-cash-(li-debt)
    adv=g('CWCL',y) or g('DefRevC',y)
    rec=g('Recv',y)
    gr=(svc/prev-1)*100 if prev else float('nan')
    print(f'{y} | {tot:.1f} | {reimb[y]:.1f} | {svc:.1f} | {gr:.1f}% | {op:.1f} | {am:.1f} | {100*(op+am)/svc:.1f}% | {100*(op+am)/tot:.1f}% | {cap:.1f} | {(rec-adv)/tot*365:.0f} | {100*adv/tot:.1f}%')
    prev=svc
