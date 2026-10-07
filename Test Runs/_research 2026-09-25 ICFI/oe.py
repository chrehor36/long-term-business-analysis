# Owner earnings from filed cash-flow statements ($K). OE = OCF - SBC - (c) - restricted-cash build inside OCF.
# (c) band: capex end = capex (PP&E + capitalized software) + payments on capital expenditure obligations (financing);
#           D&A end  = total D&A (includes amortization of acquired intangibles).
# SBC = "Non-cash equity compensation" (equity-settled; cash-settled RSUs are paid in cash inside OCF already).
D={ # FY: OCF, SBC, D&A, capex, capex_oblig, restricted_build_in_OCF
2014:(79160,11008,23806,10635,2339,0),
2015:(76319,10850,33406,12682,3289,0),
2016:(79563,9082,29119,13791,4041,0),
2017:(117191,10291,28579,14513,4808,0),
2018:(74670,11506,27206,21812,3726,0),
2019:(91440,15818,28182,26901,1621,0),
2020:(173145,17555,33748,17683,1712,0),
2021:(110205,13230,31970,19932,0,0),
2022:(162206,13171,49917,24475,0,0),
2023:(152383,14861,60738,22337,0,1789),
2024:(171544,16722,53476,21430,0,12785),
2025:(141870,17686,58147,21659,0,37170),
}
rows={}
print('FY     OCF   SBC   D&A  capex*  rc_build  OE_capex  OE_DA   (rc stripped)')
for y,(o,s,d,c,co,rc) in D.items():
    cap=c+co
    hi=o-s-cap-rc; lo=o-s-d-rc
    rows[y]=(lo,hi,lo+rc,hi+rc)
    print(y, *(round(x/1e3,1) for x in (o,s,d,cap,rc,hi,lo)))
def win(n,strip=True):
    ys=sorted(rows)[-n:]
    a=0 if strip else 2
    return ys[0],ys[-1],round(sum(rows[y][a] for y in ys)/n/1e3,1),round(sum(rows[y][a+1] for y in ys)/n/1e3,1)
for strip in (True,False):
  for n in (3,5,7,10,12):
    print('stripped' if strip else 'unstripped', n,'yr', win(n,strip))
cap=83.00*17933884/1e6
print('cap',round(cap,1))
for n in (3,5,10,12):
    y0,y1,lo,hi=win(n); print(n,'yr yield',round(100*lo/cap,2),round(100*hi/cap,2))
