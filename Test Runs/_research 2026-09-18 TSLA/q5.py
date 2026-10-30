import sys; sys.stdout.reconfigure(encoding="utf-8")
capL, capE, sov, shE = 1438702.0, 1284344.0, 5.34, 3525.803490
cases=[("5y FY2021-25, capex end",3065),("5y FY2021-25, PP&E depreciation end",8192),("3y FY2023-25, capex end",2296),("3y, depreciation end",7725),
       ("TTM to 2026-06-30, capex end",1964),("TTM, depreciation end",9447),("5y depreciation end LESS regulatory credits (display)",8192-1957)]
print("case | $M | yield legal cap | yield economic cap | pts vs 5.34% | perpetual g needed for 10% (economic cap)")
for n,oe in cases:
    y1,y2=100*oe/capL,100*oe/capE; g=100*(0.10-oe/capE)/(1+oe/capE)
    print(f"{n} | {oe:,} | {y1:.2f}% | {y2:.2f}% | {y2-sov:+.2f} | {g:.2f}%")
print("owner earnings needed today for a 10%% yield at the economic cap, no growth: $%.0fM (%.1fx the 5y depreciation end)"%(0.10*capE, 0.10*capE/8192))
print("value per economic share = OE/(0.10-g)/3,525.8M:")
for n,oe in [("capex end 5y",3065),("dep end 5y",8192)]:
    print(n, " | ".join(f"g={g}%: ${oe/(0.10-g/100)/shE:,.0f}" for g in (0,3,5,7)))
print("years at 15%% a year for the dep end to reach $128.4bn: %.1f"%(__import__('math').log(128434/8192)/__import__('math').log(1.15)))
print("years at 20%% a year: %.1f"%(__import__('math').log(128434/8192)/__import__('math').log(1.20)))
