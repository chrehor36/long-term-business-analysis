# All figures $M from the filed 10-Ks named in the run file (selected data tables, balance sheets, cash-flow statements).
# year: (total OI, ocean OI, ocean identifiable assets or None, total debt, equity, cash, CCF)
D={
2012:(96.7,96.6,1097.2,16.4+302.7,279.9,19.9,0),
2013:(100.3,94.3,1168.6,12.5+273.6,338.2,114.5,0),
2014:(140.0,131.1,1313.9,21.6+352.0,363.8,293.4,27.5),
2015:(196.3,187.8,1601.0,22.0+407.9,450.6,25.5,0),
2016:(156.7,144.5,1726.3,738.9,494.9,13.9,None),
2017:(147.3,126.4,1941.5,857.1,677.2,19.8,None),
2018:(163.8,131.1,2071.6,856.4,755.3,19.6,None),
2019:(129.1,90.8,2424.5,958.4,805.7,21.2,None),
2020:(280.3,244.8,2431.1,744.8,961.2,14.4,None),
2021:(1187.5,1137.7,None,629.0,1667.4,282.4,0),
2022:(1353.6,1281.2,3705.2,517.5,2296.9,249.8,518.2),
2023:(342.8,294.8,3645.3,440.6,2400.7,134.0,599.4),
2024:(551.3,500.9,None,400.9,2652.0,266.8,642.6),
2025:(499.8,455.6,None,361.2,2759.0,141.9,532.7),
}
print('year  totOI  oceanOI  ocean/segassets  capital(D+E-cash)  OI/capital  capital-less-CCF  OI/that')
for y,(oi,o,sa,d,e,c,ccf) in D.items():
    cap=d+e-c
    s=f'{o/sa*100:5.1f}%' if sa else '   n/a'
    if ccf is None: c2='   n/a'; r2='   n/a'
    else: c2=f'{cap-ccf:8.1f}'; r2=f'{oi/(cap-ccf)*100:5.1f}%'
    print(f'{y} {oi:7.1f} {o:7.1f}   {s}        {cap:8.1f}          {oi/cap*100:5.1f}%     {c2}   {r2}')
