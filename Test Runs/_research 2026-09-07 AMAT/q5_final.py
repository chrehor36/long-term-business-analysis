import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
SH=793597443; PX=454.71; CAP=SH*PX/1e6; SOV=5.24; FLOOR=10.0
NETCASH=14501-6544
print(f"cap ${CAP:,.0f}M  net cash ${NETCASH:,.0f}M = ${NETCASH*1e6/SH:.2f}/sh  ex-cash cap ${CAP-NETCASH:,.0f}M")
W=[("19-yr FY2007-25",2768.4),("15-yr FY2011-25",3149.1),("10-yr LTO",3404.8),("10-yr FY2016-25",4125.2),
   ("8-yr FY2018-25  JUDGED",4524.5),("5-yr LTO",4552.3),("5-yr FY2021-25",5534.2),("3-yr FY2023-25",6348.0),
   ("best yr FY2023",7104.0),("best yr, D&A end FY2024",7708.0)]
print(f"\n{'window':26s} {'OE $M':>9s} {'yield%':>7s} {'ex-cash y%':>10s} {'g to bond':>10s} {'g to floor':>11s} {'$/sh @sov':>10s} {'+cash':>8s} {'$/sh @10%':>10s} {'+cash':>8s}")
for lab,oe in W:
    y=oe/CAP*100; yx=oe/(CAP-NETCASH)*100
    v=oe*1e6/(SOV/100)/SH; vf=oe*1e6/(FLOOR/100)/SH
    c=NETCASH*1e6/SH
    print(f"{lab:26s} {oe:9.1f} {y:7.3f} {yx:10.3f} {SOV-y:10.2f} {FLOOR-y:11.2f} {v:10.2f} {v+c:8.2f} {vf:10.2f} {vf+c:8.2f}")
print(f"\nprice ${PX}")
print("\n=== EXPECTANCY = yield + growth, [E4-28] floor 10% ===")
for g in (5.0,6.5,8.0):
    print(f"  growth {g}%:")
    for lab,oe in [("19-yr",2768.4),("8-yr JUDGED",4524.5),("5-yr",5534.2),("3-yr",6348.0),("best yr",7104.0)]:
        y=oe/CAP*100; yx=oe/(CAP-NETCASH)*100
        print(f"     {lab:12s} yield {y:5.3f}% -> {y+g:5.2f}%   |  ex-cash {yx:5.3f}% -> {yx+g:5.2f}%")
print("\n=== screen reproduction ===")
sy=5512/368001*100
print(f"  screen: oe_bottom 5,512 / cap 368,001 = {sy:.3f}% ; growth_required {10-sy:.2f}% (row says 8.5)")
print(f"  vs sovereign {sy-5.24:.4f} (row says -0.0377)")
print("\n=== price vs bands ===")
for lab,lo,hi in [("zero-growth at sovereign, with net cash", 2768.4*1e6/(SOV/100)/SH+NETCASH*1e6/SH, 6348.0*1e6/(SOV/100)/SH+NETCASH*1e6/SH),
                  ("at the 10% floor, with net cash", 2768.4*1e6/0.10/SH+NETCASH*1e6/SH, 6348.0*1e6/0.10/SH+NETCASH*1e6/SH)]:
    print(f"  {lab}: ${lo:.0f} to ${hi:.0f}  -> price is {PX/hi:.2f}x the TOP, {PX/lo:.2f}x the bottom")
bestv=7708.0*1e6/(SOV/100)/SH+NETCASH*1e6/SH
print(f"  most generous single construction (best yr, D&A end, +net cash): ${bestv:.0f} -> price {PX/bestv:.2f}x")
