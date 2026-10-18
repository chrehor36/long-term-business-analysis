"""COMPUTATION, NOT A CLEARANCE. Q7's range convention applied to Libbey's last five filed years (FY2015-FY2019),
for the operator's reporting figures only. Inputs are transcriptions of the filed statements (see run file)."""
ocf  ={2015:69.7,2016:83.9,2017:45.3,2018:36.9,2019:63.4}
sbc  ={2015:5.9, 2016:4.8, 2017:3.5, 2018:2.8, 2019:3.2}
capex={2015:48.1,2016:34.6,2017:47.6,2018:45.1,2019:31.2}
intpd={2015:16.5,2016:21.6,2017:18.6,2018:20.1,2019:20.7}   # interest paid, cash flow supplemental (XBRL InterestPaidNet)
yrs=sorted(ocf)
eq ={y:ocf[y]-sbc[y]-capex[y] for y in yrs}          # equity-only owner cash (after interest)
ae ={y:eq[y]+intpd[y] for y in yrs}                  # all-equity owner cash (before interest; no tax shield deducted, see run file)
SOV=0.0543; FLOOR=0.10; NETDEBT=479.3-45.8; SH=22.667869
def halves(s):
    a=(s[2015]+s[2016])/2; b=(s[2018]+s[2019])/2
    return a,b,(b/a)**(1/3)-1
def pv(base,g,r,n=10):
    v=0; cf=base
    for t in range(1,n+1):
        cf=cf*(1+g); v+=cf/(1+r)**t
    return v+cf/r/(1+r)**n                            # zero nominal growth after year ten
for name,s in (("ALL-EQUITY",ae),("EQUITY-ONLY",eq)):
    base=sum(s.values())/5; a,b,g=halves(s)
    print(f"{name}: by year {{{', '.join(f'{y}: {s[y]:.1f}' for y in yrs)}}}; five-year mean {base:.1f}")
    print(f"   halves 2015-16 {a:.1f} -> 2018-19 {b:.1f}; growth between halves {100*g:.1f}% a year (decline: bottom of range)")
    for r,lab in ((SOV,"at the sovereign 5.43%"),(FLOOR,"at ten percent (fair-price leg)")):
        top=pv(base,0.0,r); bot=pv(base,g,r)
        if name=="ALL-EQUITY":
            print(f"   {lab}: business top {top:.0f}, bottom {bot:.0f}; less net debt {NETDEBT:.1f} -> equity top {top-NETDEBT:.0f}, bottom {bot-NETDEBT:.0f};"
                  f" per old share top {(top-NETDEBT)/SH:.2f}, bottom {(bot-NETDEBT)/SH:.2f}, average {((top+bot)/2-NETDEBT)/SH:.2f}")
        else:
            print(f"   {lab}: equity top {top:.0f}, bottom {bot:.0f}; per old share top {top/SH:.2f}, bottom {bot/SH:.2f}, average {(top+bot)/2/SH:.2f}")

print("\n--- per Q7 specifics, read literally (supersedes the halves case above for the ALL-EQUITY series) ---")
g_end=(ae[2019]/ae[2015])**(1/4)-1
base=sum(ae.values())/5
cf10=base*(1+g_end)**10
sales15,sales19=822.3,782.4
sg=(sales19/sales15)**(1/4)-1
hi_share=max(ae[y]/s for y,s in {2015:822.3,2016:793.4,2017:781.8,2018:797.9,2019:782.4}.items())
print(f"ALL-EQUITY end-year growth 2015->2019: {100*g_end:.1f}%/yr; carried ten years from the mean {base:.1f} -> {cf10:.1f} in year ten,"
      f" {100*cf10/sales19:.1f}% of 2019 sales against the highest share in the filings read {100*hi_share:.1f}% -> cap (f) applies")
print(f"cut to the business's own sales growth 2015->2019: {100*sg:.2f}%/yr (negative: bottom of the range by (b); no-growth case the top)")
for r,lab in ((SOV,"at 5.43%"),(FLOOR,"at 10% (fair-price leg)")):
    top=pv(base,0.0,r); bot=pv(base,sg,r)
    print(f"  {lab}: business {bot:.0f} to {top:.0f}; width {top/bot:.2f} to 1; less net debt {NETDEBT:.1f}: equity {bot-NETDEBT:.0f} to {top-NETDEBT:.0f};"
          f" per pre-cancellation share {(bot-NETDEBT)/SH:.2f} to {(top-NETDEBT)/SH:.2f}; midpoint per share {((top+bot)/2-NETDEBT)/SH:.2f}")
