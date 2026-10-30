# COMPUTED ratios. Pure MANAGEMENT-FEE line only (not total fee-related revenue).
P = {
 'RMR  FY25(9/30)': dict(mf=182.703, fe=27180.0, aum=39000.0, fre=None,  frr=182.703),
 'BRDG FY24':       dict(mf=245.781, fe=22306.0, aum=49845.0, fre=137.078, frr=324.153),
 'OWL  FY25':       dict(mf=2521.937,fe=187735.0,aum=307432.0,fre=1496.536,frr=2654.712),
 'ARES FY25':       dict(mf=3680.467,fe=384900.0,aum=622500.0,fre=1775.300,frr=None),
 'BAM  FY25':       dict(mf=3384.0,  fe=602714.0,aum=None,    fre=2995.0, frr=5487.0),
 'CNS  FY25':       dict(mf=524.834, fe=90544.0, aum=90544.0, fre=None,   frr=556.116),
 'KW   FY25':       dict(mf=115.2,   fe=11000.0, aum=36400.0, fre=None,   frr=None),
}
print(f"{'':17} {'mgmt fee / FEAUM':>18} {'mgmt fee / AUM':>16} {'FRE margin (FRE/FRR)':>22}")
for k,v in P.items():
    fr = f"{v['mf']/v['fe']*10000:.0f} bp" if v['fe'] else "n/d"
    fa = f"{v['mf']/v['aum']*10000:.0f} bp" if v['aum'] else "n/d"
    fm = f"{v['fre']/v['frr']*100:.1f}%" if v['fre'] and v['frr'] else ("48.2% (FRE/mgmt fee)" if k.startswith('ARES') else "n/d")
    print(f"{k:17} {fr:>18} {fa:>16} {fm:>22}")
print()
print("AUM direction ($B):")
for k,v in {'RMR (9/30 FYE)':[('FY22',37.3),('FY23',35.9),('FY24',40.9),('FY25',39.0),('6/30/26',37.5)],
 'BRDG':[('2021',36.315),('2022',43.292),('2023',47.702),('2024',49.845)],
 'OWL':[('2023',165.687),('2024',251.119),('2025',307.432)],
 'ARES':[('2024',484.4),('2025',622.5)],
 'BAM fee-bearing':[('2023',457.0),('2024',538.5),('2025',602.7)],
 'CNS':[('2022',80.425),('2023',83.136),('2024',85.814),('2025',90.544)],
 'KW AUM':[('2021',21.6),('2022',23.0),('2023',24.5),('2024',28.0),('2025',36.4)],
 'KW fee-bearing':[('2021',5.0),('2022',5.9),('2023',8.4),('2024',8.8),('2025',11.0)]}.items():
    s=' -> '.join(f'{a} {b}' for a,b in v)
    cagr=(v[-1][1]/v[0][1])**(1/(len(v)-1))-1
    print(f"  {k:18} {s}   [CAGR/yr {cagr*100:+.1f}% computed]")
