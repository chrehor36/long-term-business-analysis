PRICE = 1069.78          # close 2026-09-18, aggregator (tools/sources.py price()), FLAGGED
COMMON = 154.869259      # 10-Q cover, as of 2026-07-31, acc 0001193125-26-337177
SUBCO = 7.606927         # Class B-2 units of BlackRock Saturn Subco, exchangeable 1-for-1
SH = COMMON + SUBCO
SOV = 5.34               # US Treasury 30-yr par yield, 2026-09-18
OE_LO, OE_HI = 4756.0, 5583.0     # combined range, both windows, both ends of (c)
TAX_BOOK, TAX_CASH = 0.220, 0.302  # 2025 book and cash effective rates on pretax income
AUM = 15344624.0         # 2026-06-30
BASEFEES = 19179.0       # FY2025

cap = PRICE * SH
cap_common = PRICE * COMMON
print(f"shares incl Subco Units      {SH:.6f}M   (common {COMMON:.6f}M + Subco {SUBCO:.6f}M)")
print(f"market cap incl Subco Units  ${cap:,.0f}M      common only ${cap_common:,.0f}M")
print()
print("1. THE YIELD")
for nm, oe in (("conservative end", OE_LO), ("optimistic end", OE_HI)):
    print(f"   {nm:17s} OE ${oe:,.0f}M / cap ${cap:,.0f}M = {oe/cap*100:.2f}%   "
          f"(on common only {oe/cap_common*100:.2f}%)   sovereign {SOV:.2f}%")
print()
print("2. THE FLOOR [E4-28] - honest PRE-TAX expectancy")
for nm, t in (("at the 22.0% book rate", TAX_BOOK), ("at the 30.2% cash rate", TAX_CASH)):
    lo, hi = OE_LO/(1-t), OE_HI/(1-t)
    print(f"   {nm:24s} pre-tax OE ${lo:,.0f}M-${hi:,.0f}M -> "
          f"{lo/cap*100:.2f}% to {hi/cap*100:.2f}% pre-tax yield")
lo_p, hi_p = OE_LO/(1-TAX_BOOK)/cap*100, OE_HI/(1-TAX_BOOK)/cap*100
print(f"   observed growth in owner earnings PER SHARE 2021-2025: "
      f"{(32.82/32.65)**0.25*100-100:+.2f}%/yr (c=capex) to {(28.15/32.17)**0.25*100-100:+.2f}%/yr (c=D&A)")
print(f"   honest pre-tax expectancy = pre-tax yield + per-share growth "
      f"= {lo_p:.2f}% to {hi_p:.2f}%, plus roughly zero")
print(f"   FLOOR IS ~10% [E4-28]. SHORTFALL: {10-hi_p:.1f} to {10-lo_p:.1f} POINTS.")
print(f"   growth in owner earnings per share needed FOREVER to reach the floor: "
      f"{10-hi_p:.2f}% to {10-lo_p:.2f}% a year")
print()
print("3. WHAT THE PRICE ALREADY ASSUMES")
for nm, oe in (("conservative end", OE_LO), ("optimistic end", OE_HI)):
    g = SOV - oe/cap*100
    print(f"   {nm:17s} perpetual growth implied at the bare sovereign: g = "
          f"{SOV:.2f}% - {oe/cap*100:.2f}% = {g:.2f}%")
print(f"   what the business has actually done, per share: 0.0% to -3.3% a year over four years")
print()
print("4. WHAT YOU ARE PAID")
print(f"   {OE_LO/cap*100-SOV:+.2f} to {OE_HI/cap*100-SOV:+.2f} POINTS versus the sovereign")
print()
print("5. THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]")
for label, r in (("at the bare sovereign, no growth", SOV/100),
                 ("with 2% perpetual growth allowed", (SOV-2.0)/100)):
    lo, hi = OE_LO/r, OE_HI/r
    print(f"   {label:33s} ${lo:,.0f}M to ${hi:,.0f}M = "
          f"${lo/SH:,.0f} to ${hi/SH:,.0f} a share")
print(f"   current price ${PRICE:,.2f} a share = ${cap:,.0f}M")
print()
print("6. WHAT THE BUYER IS PAYING FOR, IN WORDS - the multiples")
print(f"   price / owner earnings                   {cap/OE_HI:.1f}x to {cap/OE_LO:.1f}x")
print(f"   price / FY2025 base fees                 {cap/BASEFEES:.1f}x")
print(f"   price as a percentage of the AUM itself  {cap/AUM*100:.3f}% of $15.3 trillion")
print(f"   years of GROSS base fees to repay        {cap/BASEFEES:.1f}")
print(f"   price / FY2025 GAAP net income to BLK    {cap/5553:.1f}x   "
       f"(/ as-adjusted net income {cap/7736:.1f}x)")
print(f"   price / book value per share of $371.70  {PRICE/371.70:.2f}x")
