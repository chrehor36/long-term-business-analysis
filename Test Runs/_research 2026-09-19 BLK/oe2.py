# Owner earnings per year and PER SHARE, BLK. Inputs all filing-sourced; see oe.py for sources.
Y = [2021, 2022, 2023, 2024, 2025]
ocf_excip = {2021: 6168, 2022: 5668, 2023: 5684, 2024: 7267, 2025: 7463}
sbc_chg = {2021: 734, 2022: 708, 2023: 630, 2024: 753, 2025: 1307}
sbc_grant = {2021: 786, 2022: 826, 2023: 707, 2024: 1379, 2025: 1807}
capex = {2021: 341, 2022: 533, 2023: 344, 2024: 255, 2025: 375}
da = {2021: 415, 2022: 418, 2023: 427, 2024: 579, 2025: 1126}
# diluted weighted-average shares, including Subco Units from 2025 (10-K income statements)
sh = {2021: 154.4, 2022: 152.4, 2023: 150.7, 2024: 151.6, 2025: 160.9}

print("year  OCF exCIP   SBC(larger)   OE c=capex  OE c=D&A   sh(dil)  OE/sh c=capex  OE/sh c=D&A")
oe_lo = {}
oe_hi = {}
for y in Y:
    sv = max(sbc_chg[y], sbc_grant[y])
    hi = ocf_excip[y] - sv - capex[y]
    lo = ocf_excip[y] - sv - da[y]
    oe_lo[y] = lo
    oe_hi[y] = hi
    print(f"{y}  {ocf_excip[y]:9d}   {sv:11d}   {hi:9.0f}  {lo:8.0f}   {sh[y]:7.1f}  "
          f"{hi/sh[y]:12.2f}  {lo/sh[y]:11.2f}")

print()
print("PER SHARE, c=D&A:  2021 %.2f -> 2024 %.2f (peak) -> 2025 %.2f" %
      (oe_lo[2021]/sh[2021], oe_lo[2024]/sh[2024], oe_lo[2025]/sh[2025]))
print("  2025 vs 2024: %+.1f%%   2025 vs 2021: %+.1f%%" % (
    (oe_lo[2025]/sh[2025])/(oe_lo[2024]/sh[2024])*100-100,
    (oe_lo[2025]/sh[2025])/(oe_lo[2021]/sh[2021])*100-100))
print("PER SHARE, c=capex: 2021 %.2f -> 2024 %.2f (peak) -> 2025 %.2f  (2025 vs 2021 %+.1f%%)" % (
    oe_hi[2021]/sh[2021], oe_hi[2024]/sh[2024], oe_hi[2025]/sh[2025],
    (oe_hi[2025]/sh[2025])/(oe_hi[2021]/sh[2021])*100-100))

print()
print("--- the named death, quantified [E3-24, E4-40] ---")
aum = 15344624.0
eq_aum = 8888234.0
other = aum - eq_aum
print(f"AUM 2026-06-30 {aum:,.0f}M of which equity {eq_aum:,.0f}M = {eq_aum/aum*100:.1f}%")
for eqd, od in ((0.30, 0.05), (0.40, 0.10), (0.50, 0.15)):
    new = eq_aum*(1-eqd) + other*(1-od)
    print(f"  equity -{eqd*100:.0f}% and everything else -{od*100:.0f}%: "
          f"AUM {new:,.0f}M = {new/aum*100-100:+.1f}%")
    # base fees at the 2025 blended rate, and with the mix penalty (equity prices above the blend)
    bf = new*15.22/10000
    print(f"     base fees at the blended 15.22bp: ${bf:,.0f}M against $19,179M actual "
          f"({bf/19179*100-100:+.1f}%)")
print()
seclend = 353000.0
coll = 375000.0
eqty = 55888.0
print(f"securities on loan indemnified ${seclend:,.0f}M; collateral held ${coll:,.0f}M "
      f"= {coll/seclend*100:.1f}%")
for share, short in ((0.05, 0.15), (0.20, 0.15), (0.20, 0.30)):
    loss = seclend*share*short
    print(f"  {share*100:.0f}% of the book with defaulting borrowers and a {short*100:.0f}% "
          f"collateral shortfall: ${loss:,.0f}M = {loss/eqty*100:.1f}% of equity, "
          f"{loss/5553*100:.0f}% of one year of net income")
