# EVI arithmetic, USD thousands; every input from the filed statements (accessions in the run file)
rev  = {2016:36016,2017:93978,2018:150007,2019:228318,2020:235802,2021:242005,2022:267316,2023:354173,2024:353563,2025:389830,2026:446570}
gp   = {2016:8212,2017:20339,2018:36506,2019:52698,2020:55207,2021:59840,2022:73707,2023:103683,2024:105253,2025:118348,2026:140724}
opi  = {2016:2791,2017:5350,2018:6934,2019:7005,2020:2780,2021:3246,2022:6389,2023:16506,2024:11628,2025:13768,2026:15712}
ocf  = {2017:2590,2018:11345,2019:-8725,2020:23066,2021:13694,2022:-1898,2023:940,2024:32652,2025:21265,2026:20606}
sbc  = {2017:421,2018:1575,2019:1740,2020:2302,2021:2437,2022:2598,2023:3062,2024:4974,2025:4558,2026:5298}
capex= {2017:237,2018:829,2019:2979,2020:3375,2021:2824,2022:3981,2023:3708,2024:4867,2025:4861,2026:7152}
acq  = {2017:14708,2018:13352,2019:12542,2020:1379,2021:4818,2022:11953,2023:2278,2024:1949,2025:46925,2026:7182}
stockacq={2017:16053,2018:21376,2019:17050,2020:8010,2021:8877,2022:4331,2023:503,2024:229,2025:0,2026:0}
intpaid={2017:152,2018:499,2019:1231,2020:1475,2021:511,2022:494,2023:2469,2024:2783,2025:2500,2026:3866}
pretax={2017:5190,2018:6382,2019:5616,2020:1348,2021:9888,2022:5710,2023:13999,2024:8884,2025:11025,2026:11775}
tax  = {2017:2023,2018:2416,2019:1873,2020:573,2021:1504,2022:1615,2023:4280,2024:3238,2025:3527,2026:4057}
eq   = {2018:57031,2019:77262,2020:87826,2021:106740,2022:117679,2023:130956,2024:136606,2025:143477,2026:150143}
cash = {2018:1330,2019:5038,2020:9789,2021:6057,2022:3974,2023:5921,2024:4558,2025:8852,2026:6774}
debt = {2018:8817,2019:40563,2020:25030,2021:11873,2022:27840,2023:34869,2024:12903,2025:53000,2026:51000}
gw   = {2018:37061,2019:54501,2020:56678,2021:63881,2022:71039,2023:73388,2024:75102,2025:91667,2026:93934}
intg = {2018:15775,2019:22351,2020:21754,2021:23677,2022:26234,2023:24128,2024:22022,2025:30875,2026:28859}
print("year  rev    GM%   opM%   opROTC%(incl gw)  opROTangC%")
for y in range(2016,2027):
    s=f"{y} {rev[y]/1e3:7.1f} {gp[y]/rev[y]*100:5.1f} {opi[y]/rev[y]*100:5.1f}"
    if y in eq:
        tc=eq[y]+debt[y]-cash[y]; tang=tc-gw[y]-intg[y]
        s+=f"   {opi[y]/tc*100:5.1f} (cap {tc/1e3:.1f})   {opi[y]/tang*100:5.1f} (tang cap {tang/1e3:.1f})"
    print(s)
print("\nyear  OCF-SBC-capex (before acq)   after cash acq   stock acq   eff tax")
for y in range(2017,2027):
    b=ocf[y]-sbc[y]-capex[y]; a=b-acq[y]
    print(y, f"{b:8,} {a:9,} {stockacq[y]:7,}  {tax[y]/pretax[y]*100:5.1f}%")
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
W=range(2022,2027); T=range(2017,2027)
before={y:ocf[y]-sbc[y]-capex[y] for y in T}; after={y:before[y]-acq[y] for y in T}
t_eff=sum(tax[y] for y in W)/sum(pretax[y] for y in W)
ia=avg(intpaid,W)*(1-t_eff)
print(f"\nwindow FY22-26: before acq avg {avg(before,W):,.0f}; after acq avg {avg(after,W):,.0f}; eff tax {t_eff*100:.1f}%; after-tax interest avg {ia:,.0f}")
print(f"ten-yr FY17-26: before acq avg {avg(before,T):,.0f}; after acq avg {avg(after,T):,.0f}")
print("halves FY22-23 vs FY25-26 after acq:", avg(after,[2022,2023]), avg(after,[2025,2026]), " before:", avg(before,[2022,2023]), avg(before,[2025,2026]))
# valuation
shares=12878.532  # thousands, cover 2026-09-03
nd_filed=51000-6774; sudsies=37400; nd=nd_filed+sudsies
def val(cf10, cfterm, r):
    ann=(1-(1+r)**-10)/r; disc=(1+r)**-10
    return cf10*ann + cfterm/r*disc
for label,base in (("window",W),("ten-year",T)):
    a_eq=avg(after,base); b_eq=avg(before,base)
    ia_b=avg(intpaid,base)*(1-t_eff)
    for r in (0.056,0.10):
        ev_c=val(a_eq+ia_b, b_eq+ia_b, r); ev_o=val(b_eq+ia_b,b_eq+ia_b,r)
        sud_int=sudsies*0.0524*(1-t_eff)
        eqo_c=val(a_eq,b_eq,r)-sud_int/r; eqo_o=val(b_eq,b_eq,r)-sud_int/r
        print(f"{label} r={r}: CENTRAL all-equity EV {ev_c:,.0f} less ND {nd:,.0f} = {(ev_c-nd)/shares:.2f}/sh | equity-only {eqo_c/shares:.2f}/sh || ORGANIC all-equity {(ev_o-nd)/shares:.2f}/sh | equity-only {eqo_o/shares:.2f}/sh")
# Sudsies beside, credited at its press-release operating income after tax
sud_cf=4700*(1-0.25)
for r in (0.056,0.10): print(f"Sudsies credited at PR op income after 25% tax ({sud_cf:,.0f}/yr) adds {sud_cf/r/shares:.2f}/sh at r={r}")
print("price 19.20 x shares =", 19.20*shares, " EV at price =", 19.20*shares+nd)
