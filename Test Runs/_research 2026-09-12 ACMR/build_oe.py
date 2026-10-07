# All figures in $ thousands, from the FILED cash-flow statements and income statements
# of the 10-Ks named in the run file. Vintage = newest filed restatement.
Y = [2018,2019,2020,2021,2022,2023,2024,2025]
ocf  = {2018:6909, 2019:9403, 2020:-13547, 2021:-40093, 2022:-62194, 2023:-75323, 2024:152450, 2025:-10325}
sbc  = {2018:3363, 2019:3572, 2020:5628,   2021:5117,   2022:7730,   2023:27338,  2024:49576,  2025:33577}
dep  = {2018:417,  2019:788,  2020:1502,   2021:2353,   2022:5366,   2023:8092,   2024:9967,   2025:16328}
capx = {2018:1830, 2019:971,  2020:5211,   2021:9153,   2022:91094,  2023:61876,  2024:82463,  2025:56283}
intg = {2018:241,  2019:154,  2020:324,    2021:559,    2022:1426,   2023:2462,   2024:3485,   2025:1372}
rev  = {2018:74643,2019:107524,2020:156624,2021:259751, 2022:388832, 2023:557723, 2024:782118, 2025:901309}
pl   = {2018:6574, 2019:19458,2020:21677,  2021:42921,  2022:50564,  2023:96852,  2024:131269, 2025:121893}
nci  = {2018:0,    2019:564,  2020:2897,   2021:5164,   2022:11301,  2023:19503,  2024:27642,  2025:27815}

print("YEAR  REV      OCF      SBC      D&A    CAPEX+INTG   OE(D&A end)  OE(capex end)  ACMRshare%  OE_parent(D&A)  OE_parent(capex)")
oe_d, oe_c, oepd, oepc = {},{},{},{}
for y in Y:
    tc = capx[y]+intg[y]
    oe_d[y] = ocf[y]-sbc[y]-dep[y]
    oe_c[y] = ocf[y]-sbc[y]-tc
    share = 1.0 - nci[y]/pl[y] if pl[y] else 1.0
    oepd[y] = oe_d[y]*share; oepc[y] = oe_c[y]*share
    print(f"{y}  {rev[y]:>8,} {ocf[y]:>8,} {sbc[y]:>8,} {dep[y]:>7,} {tc:>10,}  {oe_d[y]:>11,.0f}  {oe_c[y]:>13,.0f}   {share*100:>7.1f}%  {oepd[y]:>13,.0f}  {oepc[y]:>15,.0f}")

def mean(d, ys): return sum(d[y] for y in ys)/len(ys)
windows = {"5y 2021-25":[2021,2022,2023,2024,2025], "5y 2020-24":[2020,2021,2022,2023,2024],
           "3y 2023-25":[2023,2024,2025], "3y 2022-24":[2022,2023,2024],
           "8y 2018-25":Y, "7y 2019-25":Y[1:], "6y 2020-25":Y[2:], "4y 2022-25":[2022,2023,2024,2025],
           "10y-as-filed 2018-25":Y}
print("\nWINDOW              OE mean D&A end   OE mean capex end   PARENT D&A end   PARENT capex end")
allv=[]
for k,ys in windows.items():
    a,b,c,d = mean(oe_d,ys), mean(oe_c,ys), mean(oepd,ys), mean(oepc,ys)
    allv += [c,d]
    print(f"{k:<20} {a:>14,.0f}   {b:>17,.0f}   {c:>14,.0f}   {d:>16,.0f}")
print(f"\nPARENT-ATTRIBUTABLE BAND across all windows x both (c) ends: {min(allv):,.0f} to {max(allv):,.0f}  width {max(allv)-min(allv):,.0f}")
cons=[]
for k,ys in windows.items(): cons += [mean(oe_d,ys), mean(oe_c,ys)]
print(f"CONSOLIDATED BAND: {min(cons):,.0f} to {max(cons):,.0f}  width {max(cons)-min(cons):,.0f}")
print(f"\nCumulative OCF 2018-2025: {sum(ocf.values()):,}")
print(f"Cumulative SBC 2018-2025: {sum(sbc.values()):,}")
print(f"Cumulative capex+intg   : {sum(capx.values())+sum(intg.values()):,}")
print(f"Cumulative OE (capex end) 2018-25: {sum(oe_c.values()):,}   (D&A end): {sum(oe_d.values()):,}")
print(f"\nFY2025 AP check: OCF {ocf[2025]:,}  AP move 67,854 -> {67854/abs(ocf[2025])*100:.1f}% of |OCF|")
print(f"FY2025 OCF ex-AP increase: {ocf[2025]-67854:,}   ex-AP and ex-related-party-AP: {ocf[2025]-67854-15927:,}")
print(f"\nSBC/OCF cumulative 2018-25: SBC {sum(sbc.values()):,} vs OCF {sum(ocf.values()):,} -> ratio n/a (OCF negative)")
