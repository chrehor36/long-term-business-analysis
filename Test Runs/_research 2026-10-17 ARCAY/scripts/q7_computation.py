"""COMPUTATION, NOT A CLEARANCE (the file closed OUT at Q2). Q7's range by the range convention, EUR M and EUR/share."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
SH=85.205601; PX=41.20; ND=813.0          # shares 30 Jun 2026 (H1 IFS note 17); net debt ex leases 30 Jun 2026 (H1 IFS BS)
R=0.0367                                   # ECB EUR 30Y, 2026-10-15
MC=SH*PX; EV=MC+ND
def pv(c0,g,r,years=10,purch=0.0,c_after=None):
    """cash in year t = c0*(1+g)^t - purch for t=1..10; after year 10, flat at c10 (or c_after*(1+g)^10 when given) forever."""
    v=0.0
    for t in range(1,years+1):
        v+=(c0*(1+g)**t-purch)/(1+r)**t
    base_after=(c_after if c_after is not None else c0)*(1+g)**years
    v+=(base_after/r)/(1+r)**years
    return v
def irr(f,target,lo=0.0001,hi=0.5):
    for _ in range(200):
        m=(lo+hi)/2
        if f(m)>target: lo=m
        else: hi=m
    return m
B=231.6; Beq=211.3; G_org=0.0540; G_tot=0.0562; P=176.9; Bafter=54.6
print(f"market cap {MC:,.1f}  net debt {ND}  EV {EV:,.1f}")
cases={
 'central low  (organic pair, no growth, all-equity)':  lambda r: pv(B,0.0,r),
 'central high (organic pair, 5.40% x10y, all-equity)':  lambda r: pv(B,G_org,r),
 'default low  (purchases deducted, no growth: 54.6 x10y then 231.6)': lambda r: pv(Bafter,0.0,r,c_after=B),
 'default high (total growth 5.62%, purchases 176.9/yr deducted x10y, then flat before purchases)': lambda r: pv(B,G_tot,r,purch=P),
}
vals={}
for k,f in cases.items():
    v=f(R); vals[k]=v
    print(f"{k}: value {v:,.0f}  per share {(v-ND)/SH:6.2f}  | at 10%: {f(0.10):,.0f} -> {(f(0.10)-ND)/SH:6.2f}/sh | expected return at price (IRR vs EV {EV:,.0f}): {irr(f,EV)*100:5.2f}%")
eq={'equity-only low (211.3 no growth)':lambda r: pv(Beq,0.0,r),'equity-only high (211.3 at 5.40%)':lambda r: pv(Beq,G_org,r)}
for k,f in eq.items():
    print(f"{k}: value {f(R):,.0f} per share {f(R)/SH:6.2f} | at 10%: {f(0.10):,.0f} -> {f(0.10)/SH:6.2f}/sh | IRR vs market cap {MC:,.0f}: {irr(f,MC)*100:5.2f}%")
lo=(vals['central low  (organic pair, no growth, all-equity)']-ND)/SH; hi=(vals['central high (organic pair, 5.40% x10y, all-equity)']-ND)/SH
print(f"\nCENTRAL RANGE per share: {lo:.2f} to {hi:.2f}; width top/bottom {hi/lo:.2f}")
fair=((cases['central low  (organic pair, no growth, all-equity)'](0.10)+cases['central high (organic pair, 5.40% x10y, all-equity)'](0.10))/2-ND)/SH
fair_eq=((eq['equity-only low (211.3 no growth)'](0.10)+eq['equity-only high (211.3 at 5.40%)'](0.10))/2)/SH
print(f"FAIR PRICE (all-equity, central): {fair:.2f} ; equity-only: {fair_eq:.2f}")
dl=(vals['default low  (purchases deducted, no growth: 54.6 x10y then 231.6)']-ND)/SH; dh=(vals['default high (total growth 5.62%, purchases 176.9/yr deducted x10y, then flat before purchases)']-ND)/SH
fd=((cases['default low  (purchases deducted, no growth: 54.6 x10y then 231.6)'](0.10)+cases['default high (total growth 5.62%, purchases 176.9/yr deducted x10y, then flat before purchases)'](0.10))/2-ND)/SH
print(f"DEFAULT PAIR beside: {min(dl,dh):.2f} to {max(dl,dh):.2f}; fair {fd:.2f}")
# year-end net debt sensitivity (not a reporting figure)
print(f"net debt at 31 Dec 2025 (556) instead of 30 Jun 2026 (813) moves every all-equity per-share figure by {(813-556)/SH:.2f}")
# floor at the price: owner cash yield
print(f"owner cash yield at price: all-equity {B/EV*100:.2f}% ; equity {Beq/MC*100:.2f}%")
