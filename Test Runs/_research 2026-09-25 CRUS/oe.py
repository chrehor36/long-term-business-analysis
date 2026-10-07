# Owner earnings from filed cash-flow statements ($K). OE = OCF - SBC - (c); (c) band: total capex (PP&E+software + investments in technology) to D&A.
D={ # FY: OCF, SBC, D&A, capex_ppe, tech, prepaid_wafers_line, acq_liab_line
2015:(163477,37549,34855,32311,4387,0,0),
2016:(149046,33506,58060,41569,4519,0,0),
2017:(369751,39593,63433,41849,9447,0,0),
2018:(318711,48741,81399,55180,29323,0,0),
2019:(206694,49689,79826,31615,4143,0,0),
2020:(295815,53757,68237,15656,5920,0,0),
2021:(348945,56762,47083,18253,2222,0,0),
2022:(124753,66392,62061,26139,3871,-195000,39656),
2023:(339568,81641,71202,35090,1624,0,12654),
2024:(421674,89271,48292,37650,695,47571,-21361),
2025:(444366,84146,50951,22776,5977,79357,0),
2026:(650598,81811,52300,13988,848,53339,0),
}
rows={}
print('FY    OCF    SBC   D&A  capex  OE_hi(capex)  OE_lo(D&A)  prepaid  OE_lo_exPrepaid OE_hi_exPrepaid')
for y,(o,s,d,c,t,p,a) in D.items():
    cap=c+t
    hi=o-s-min(cap,d); lo=o-s-max(cap,d)
    rows[y]=(lo,hi,lo-p,hi-p)
    print(y, round(o/1e3,1), round(s/1e3,1), round(d/1e3,1), round(cap/1e3,1), round(hi/1e3,1), round(lo/1e3,1), round(p/1e3,1), round((lo-p)/1e3,1), round((hi-p)/1e3,1))
def win(n,adj):
    ys=sorted(rows)[-n:]
    i=2 if adj else 0
    lo=sum(rows[y][i] for y in ys)/n/1e3; hi=sum(rows[y][i+1] for y in ys)/n/1e3
    return ys[0],ys[-1],round(lo,1),round(hi,1)
for adj in (False,True):
  for n in (3,5,7,10,12):
    print('adj' if adj else 'raw', n,'yr', win(n,adj))
