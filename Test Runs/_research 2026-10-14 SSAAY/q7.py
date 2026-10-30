"""Q7 arithmetic for SSAB (SEK m). Run: python -I q7.py"""
r_sov=0.03178; FLOOR=0.10; SH=996.617667
NETCASH=19657-(7252+143)          # 2026-06-30, leases excluded (lease cash charged in owner cash)
COMMIT=46968                      # AR2025 capex plan: Oxelosund SEK 6.2bn + Lulea EUR 4.5bn less paid, next five years
MCAP=295.96633*101.45+700.651337*102.20
SEKUSD=0.1005; ADS=0.5
def v(oc,g,r):
    s=sum(oc*(1+g)**t/(1+r)**t for t in range(1,11))
    return s+oc*(1+g)**10/r/(1+r)**10
def ann(x,r,n=5): return sum(x/(1+r)**t for t in range(1,n+1))
def case(label,oc,g,add_cash=True,commit=True):
    out={}
    for r in (r_sov,FLOOR):
        val=v(oc,g,r)-(ann(COMMIT/5,r) if commit else 0)+(NETCASH if add_cash else 0)
        out[r]=val/SH
    print(f"{label:58s} sov {out[r_sov]:7.1f}  @10% {out[FLOOR]:7.1f} SEK/sh")
    return out
print('market cap', round(MCAP), 'net cash', NETCASH, 'commitment PV sov', round(ann(COMMIT/5,r_sov)), '@10%', round(ann(COMMIT/5,FLOOR)))
g=r_sov  # shown growth (25%/yr between cycle averages) cut by (f) to sales growth 9.95%/yr, capped at the discount rate
print('\nCENTRAL: all-equity, maintenance case, cycle base 2016-25 (7,666), commitment deducted')
lo=case(' bottom: no growth',7666,0); hi=case(' top: growth 3.178% ten years',7666,g)
fair=(lo[FLOOR]+hi[FLOOR])/2; print(f" FAIR (all-equity) SEK {fair:.1f}  per ADS USD {fair*ADS*SEKUSD:.2f}; range at sovereign SEK {lo[r_sov]:.0f}-{hi[r_sov]:.0f}")
print('\nEQUITY-ONLY beside: maintenance case 7,506, no net cash added, commitment deducted')
le=case(' bottom',7506,0,add_cash=False); he=case(' top',7506,g,add_cash=False)
print(f" FAIR (equity-only) SEK {(le[FLOOR]+he[FLOOR])/2:.1f}")
print('\nBESIDE: all-equity, commitment NOT deducted')
a=case(' bottom',7666,0,commit=False); b=case(' top',7666,g,commit=False)
print(f" fair SEK {(a[FLOOR]+b[FLOOR])/2:.1f}")
print('\nBESIDE: all-spending case, cycle base 5,964, commitment deducted (historic strategic spend already inside)')
case(' bottom',5964,0); case(' top',5964,g)
print('\nBESIDE: literal window 2021-25, maintenance case 11,548, commitment deducted')
x=case(' bottom',11548,0); y=case(' top',11548,g); print(f" fair SEK {(x[FLOOR]+y[FLOOR])/2:.1f}")
print('\nprice B SEK 102.20; implied: market cap', round(MCAP))
