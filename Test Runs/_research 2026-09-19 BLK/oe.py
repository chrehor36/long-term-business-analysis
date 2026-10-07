# Owner earnings, BLK. CONVENTION: operating cash flow less SBC less the (c) guess.
# The operating cash flow used is the filer own "excluding the impact of CIPs" column,
# because CIP flows are the funds money, not the owner. Both are shown.
Y=[2021,2022,2023,2024,2025]
ocf_gaap={2021:4944,2022:4956,2023:4165,2024:4956,2025:3927}   # as filed
ocf_excip={2021:6168,2022:5668,2023:5684,2024:7267,2025:7463}  # filer CIP reconciliation
sbc_chg={2021:734,2022:708,2023:630,2024:753,2025:1307}
sbc_grant={2021:786,2022:826,2023:707,2024:1379,2025:1807}     # RSU + perf-RSU grant-date FMV
capex={2021:341,2022:533,2023:344,2024:255,2025:375}
da={2021:415,2022:418,2023:427,2024:579,2025:1126}             # 2024 incl $50M impairment
acq_cash={2021:1106,2022:0,2023:189,2024:2936,2025:3496}
acq_paper={2021:0,2022:0,2023:0,2024:5904,2025:8694}           # noncash schedule

def mean(d,ys): return sum(d[y] for y in ys)/len(ys)
def block(ys,label):
    print(f"\n--- {label}  window {ys[0]}-{ys[-1]} ({len(ys)} yr) ---")
    o=mean(ocf_excip,ys); og=mean(ocf_gaap,ys)
    sc=mean(sbc_chg,ys); sg=mean(sbc_grant,ys); s=max(sc,sg)
    cl=mean(capex,ys); ch=mean(da,ys)
    print(f"mean OCF as filed (GAAP, CIPs in)        {og:9.1f}")
    print(f"mean OCF excluding CIPs (filer column)   {o:9.1f}")
    print(f"mean SBC, reported charge                {sc:9.1f}")
    print(f"mean SBC, grant-date market value [E3-70]{sg:9.1f}   <- the larger governs")
    print(f"(c) low  = PP&E capex mean               {cl:9.1f}")
    print(f"(c) high = D&A mean (corpus default)     {ch:9.1f}")
    for nm,sv in (("charge",sc),("grant value",s)):
        lo=o-sv-ch; hi=o-sv-cl
        print(f"  OWNER EARNINGS, SBC at {nm:11s}: {lo:8.1f} (c=D&A)  to {hi:8.1f} (c=capex)")
    return o,s,cl,ch
b5=block(Y,"FIVE-YEAR, the corpus default [E2-42]")
b3=block([2023,2024,2025],"THREE-YEAR")
print("\n--- TTM 2025-07-01 to 2026-06-30 ---")
ttm=7463-1979+3106
print(f"OCF excluding CIPs, TTM  = 7463 - 1979 (H1-25) + 3106 (H1-26) = {ttm}")
print("NOT used as the mean: a single year is not owner earnings [E2-23 constraint 1],")
print("and BLK operating cash is severely H2-weighted (year-end incentive comp accrued in")
print("the year and paid in Q1): H1-2025 ex-CIP OCF 1,979 against full-year 7,463 = 26.5%.")
print("\n--- the acquisition question, shown separately, NOT folded into the band ---")
print(f"cash paid for acquisitions, 5-yr mean      {mean(acq_cash,Y):9.1f}")
print(f"stock/units issued for acquisitions, mean  {mean(acq_paper,Y):9.1f}")
print(f"contingent consideration still payable      8429.0  (GIP 4.0-5.2M sh, HPS 2.8-4.4M units)")
o,s,cl,ch=b5
print(f"if the WHOLE acquisition programme were maintenance, (c) would rise by "
      f"{mean(acq_cash,Y)+mean(acq_paper,Y):.1f} and owner earnings fall to "
      f"{o-s-ch-mean(acq_cash,Y)-mean(acq_paper,Y):.1f}")
print("\n--- yields at the 2026-09-18 close of $1,069.78 ---")
sh=162.476186  # 10-Q cover 2026-07-31: 154,869,259 common + 7,606,927 Subco Units
cap=1069.78*sh
print(f"shares incl. Subco Units (10-Q cover 2026-07-31) {sh:.3f}M -> market cap ${cap:,.0f}M")
for nm,oe in (("5-yr, SBC at grant value, c=D&A", o-s-ch),
              ("5-yr, SBC at grant value, c=capex", o-s-cl),
              ("3-yr, SBC at grant value, c=D&A", b3[0]-b3[1]-b3[3]),
              ("3-yr, SBC at grant value, c=capex", b3[0]-b3[1]-b3[2])):
    print(f"  {nm:36s} OE {oe:8.1f}  yield {oe/cap*100:5.2f}%  vs sovereign 5.34%")
