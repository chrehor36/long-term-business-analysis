# ACMR cells on the cohort formula built by the KLAC run 2026-09-07 and carried by AMAT/LRCX.
# All from 10-K FY2025, accession 0001628280-26-013231, filed 2026-03-02.
rev=901309; cor=501242; rd=144989; sm=76899; ga=68750
assets=2872185; gw=0; intang=2847
tcl=745712; stb=74041; cltd=35082
cash=757373; rcash=8589; stdep=366591; stinv=35524
op = rev-cor-rd-sm-ga
nibcl = tcl-stb-cltd
den = assets-gw-intang-nibcl
den_ex = den-(cash+rcash+stdep+stinv)
print(f"revenue        {rev:,}")
print(f"gross margin   {(rev-cor)/rev*100:.1f}%")
print(f"R&D % revenue  {rd/rev*100:.1f}%")
print(f"SG&A % revenue {(sm+ga)/rev*100:.1f}%")
print(f"operating inc  {op:,}   (filed 'Income from operations' 109,429 -> match: {op==109429})")
print(f"operating marg {op/rev*100:.1f}%")
print(f"NIBCL          {nibcl:,}")
print(f"ROUNTOA        {op/den*100:.2f}%  (denominator {den:,})")
print(f"ex-cash ROUNTOA{op/den_ex*100:.2f}%  (denominator {den_ex:,})")
print()
# incremental FY2022 -> FY2025, cohort's incremental measure
rev22=388832; cor22=205217; rd22=0; # FY2022 opex split
print("FY2022 filed: revenue 388,832 cost 205,217")
# gross margin series
gm={2016:(13329,27371),2017:(17225,36506),2018:(34449,74643),2019:(50654,107524),
    2020:(69599,156624),2021:(114856,259751),2022:(183615,388832),2023:(276215,557723),
    2024:(391554,782118),2025:(400067,901309)}
print("\nACMR gross margin series (filed, newest vintage):")
for y,(g,r) in gm.items(): print(f"  {y}: {g/r*100:.1f}%")
# service/spares share
print("\nServices+spares bucket (blended with advanced packaging ex-ECP):")
for y,v,t in [(2023,50516,557723),(2024,52174,782118),(2025,75794,901309)]:
    print(f"  {y}: ${v:,}k = {v/t*100:.1f}% of revenue")
# units
u={2019:80,2020:135,2021:225,2022:380,2023:765,2024:1120,2025:1435}
print("\nCumulative tools delivered since 2009 (Item 1, each 10-K) and annual delta:")
prev=None
for y,v in u.items():
    d=f"+{v-prev}" if prev else ""
    print(f"  FY{y}: >{v:,}  {d}")
    prev=v
print("  H1-2026: >1,590  +155 (six months; ~310 annualised)")
print("\nRevenue per incremental tool:")
for y,rv in [(2023,557723),(2024,782118),(2025,901309)]:
    d={2023:385,2024:355,2025:315}[y]
    print(f"  {y}: ${rv/d/1000:.3f}M per delivered tool ({d} tools)")
