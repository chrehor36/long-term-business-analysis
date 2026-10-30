# Pre-tax earnings before corporate interest, against net tangible capital and against total capital.
# All figures USD millions, transcribed from the filed statements (accessions in the run file).
yrs   = [2018, 2019, 2021, 2022, 2023, 2024, 2025]
ptx   = {2018:403, 2019:273, 2021:269, 2022:481, 2023:449, 2024:136, 2025:175}  # income before income taxes
intr  = {2018:30,  2019:43,  2021:105, 2022:142, 2023:178, 2024:329, 2025:311}  # corporate interest expense
eq    = {2018:616, 2019:570, 2021:1988,2022:2151,2023:2115,2024:1895,2025:1440}  # total equity
debt  = {2018:604, 2019:828, 2021:2913,2022:2651,2023:3049,2024:4601,2025:4545}  # Debt, net (corporate)
cash  = {2018:108, 2019:67,  2021:432, 2022:223, 2023:589, 2024:328, 2025:239}
gw    = {2018:0,   2019:0,   2021:1377,2022:1416,2023:1418,2024:1985,2025:1985}
intg  = {2018:81,  2019:89,  2021:1441,2022:1277,2023:1158,2024:1787,2025:1670}
print("year  EBT+int  net-tangible  return  total-capital  return")
for y in yrs:
    e = ptx[y] + intr[y]
    tot = eq[y] + debt[y] - cash[y]
    tan = tot - gw[y] - intg[y]
    print(f"{y}  {e:6.0f}  {tan:10.0f}  {e/tan:6.1%}  {tot:10.0f}  {e/tot:6.1%}")
# incremental, 2019 -> 2025
d_e = (ptx[2025]+intr[2025]) - (ptx[2019]+intr[2019])
d_tan = (eq[2025]+debt[2025]-cash[2025]-gw[2025]-intg[2025]) - (eq[2019]+debt[2019]-cash[2019]-gw[2019]-intg[2019])
d_tot = (eq[2025]+debt[2025]-cash[2025]) - (eq[2019]+debt[2019]-cash[2019])
print(f"2019->2025: added pre-tax earnings {d_e}, added tangible capital {d_tan}, added total capital {d_tot}, incremental return on total {d_e/d_tot:.1%}")
