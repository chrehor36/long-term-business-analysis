# Effective fee rate = base fees (investment advisory, administration fees and securities
# lending revenue) / full-year average AUM, in basis points. All inputs filing-sourced.
# 2021-2023 old presentation (CIK 1364742 10-Ks FY2022, FY2023);
# 2024-2025 new presentation (CIK 2012383 10-K FY2025); H1 2026 from the 10-Q.
bp = lambda rev, aum: rev*10000.0/aum

TOT = {  # (base fees $M, full-year average AUM $M)
 2021: (15260, 9364948),
 2022: (14451, 8948570),
 2023: (14399, 9220700),
 2024: (16100, 10804007),
 2025: (19179, 12603633),
 "H1-26 ann.": (11164*2, 14640729),
}
ETF = {  # ETF base fees, ETF average AUM
 2021: (4658+1201+216, 2976332),
 2022: (4345+1122+216, 2957869),
 2023: (4418+1230+185, 3156656),
 2024: (5124+1367+247, 3892488),
 2025: (6043+1532+502, 4772325),
 "H1-26 ann.": ((3782+877+342)*2, 5836753),
}
EQACT = {2021:(2571,466291),2022:(2147,426141),2023:(2000,409687),
         2024:(2166,461583),2025:(2167,496505),"H1-26 ann.":(1219*2,580183)}
FIACT = {2021:(2191,1053764),2022:(1977,1016918),2023:(1897,1080917),
         2024:(1952,1133152),2025:(2018,1183030),"H1-26 ann.":(1070*2,1262392)}
NONETF = {2021:(771+471,3242627),2022:(711+396,2916080),2023:(743+353,2895618),
          2024:(1183,3359298),2025:(1321,3753346),"H1-26 ann.":(727*2,4193133)}
PRIV = {2021:(668,94768),2022:(741,111075),2023:(889,127655),
        2024:(1196,154597),2025:(2350,261535),"H1-26 ann.":(1297*2,323993)}
CASH = {2021:(470,711160),2022:(864,719284),2023:(909,696355),
        2024:(1049,806123),2025:(1245,975780),"H1-26 ann.":(683*2,1073788)}
MA   = {2021:(1414,736078),2022:(1299,723919),2023:(1203,787193),
        2024:(1248,921364),2025:(1332,1072635),"H1-26 ann.":(758*2,1259956)}

rows=[("TOTAL",TOT),("ETFs (all)",ETF),("Equity active",EQACT),("Fixed income active",FIACT),
      ("Non-ETF index",NONETF),("Private markets / illiquid alts",PRIV),
      ("Multi-asset (active)",MA),("Cash management",CASH)]
yrs=[2021,2022,2023,2024,2025,"H1-26 ann."]
print(f"{'segment':34s}" + "".join(f"{str(y):>12s}" for y in yrs) + "   chg 21-25")
for name,d in rows:
    line=f"{name:34s}"
    for y in yrs:
        r,a=d[y]; line+=f"{bp(r,a):11.2f} "
    c=(bp(*d[2025])/bp(*d[2021])-1)*100
    print(line+f"  {c:+6.1f}%")
print()
# ex-private-markets total
for y in (2021,2025):
    r,a=TOT[y]; pr,pa=PRIV[y]
    print(f"{y} total ex private markets: {bp(r-pr,a-pa):.2f} bp")
print()
print("AUM end-2021 10,010,143 -> end-2025 14,041,518 : %+.1f%%" % ((14041518/10010143-1)*100))
print("avg AUM 2021 -> 2025                           : %+.1f%%" % ((12603633/9364948-1)*100))
print("base fees 2021 -> 2025                         : %+.1f%%" % ((19179/15260-1)*100))
print("total revenue 2021 -> 2025                     : %+.1f%%" % ((24216/19374-1)*100))
print("technology services 2021 -> 2025               : %+.1f%%  (2025 incl ~$210M Preqin)" % ((1981/1281-1)*100))
print("tech services as %% of revenue 2025             : %.1f%%" % (1981/24216*100))
