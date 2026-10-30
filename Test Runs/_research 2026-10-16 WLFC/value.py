import io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def pv(c0,g,r,spend=0.0,years=10):
    v=0.0; c=c0
    for t in range(1,years+1):
        c*=1+g; v+=(c-spend)/(1+r)**t
    v+=c/r/(1+r)**years      # zero nominal growth after year ten, spending stops
    return v
SH_ISS=22.808; SH_COV=21.144; PRICE=37.61
ND_JUN=2320.9-10.7-161.5          # debt less cash and restricted cash, 10-Q 2026-06-30
WNG=262.9; SERB_CASH=35.0; PREF_LIQ=65.0+35.0
CLAIMS=ND_JUN+WNG-SERB_CASH+PREF_LIQ   # all-equity basis: net debt incl. stated subsequent events, preferred at liquidation
print(f"net debt Jun-26 {ND_JUN:.1f}; claims ahead of common {CLAIMS:.1f}; mcap {SH_ISS*PRICE:.1f} (issued) {SH_COV*PRICE:.1f} (cover); EV {SH_ISS*PRICE+CLAIMS:.1f}")
r=0.0543
cases={
 'all-equity, cycle base 2020-25': (111.6, 0.048, 247.9),
 'all-equity, literal 5-yr 2021-25': (132.9, 0.048, 247.0),
}
for name,(c,g,i) in cases.items():
    top=pv(c,0,r); bot=pv(c,g,r,spend=i); grow_free=pv(c,g,r)
    print(name)
    for lab,v in [('no growth (top)',top),('growth with its spending (bottom)',bot),('growth credited, spending not charged (shown beside only)',grow_free)]:
        print(f"   {lab:58s} firm {v:8.1f}  per share {(v-CLAIMS)/SH_ISS:8.2f}")
    t10=pv(c,0,0.10); b10=pv(c,g,0.10,spend=i)
    fair=((t10-CLAIMS)/SH_ISS+(b10-CLAIMS)/SH_ISS)/2
    print(f"   at 10%: top {(t10-CLAIMS)/SH_ISS:.2f} bottom {(b10-CLAIMS)/SH_ISS:.2f}  FAIR (avg) {fair:.2f}")
    print(f"   return at price, no-growth all-equity: {c/(SH_ISS*PRICE+CLAIMS)*100:.2f}%")
# equity-only
PREF_ONLY=PREF_LIQ
ND_EQ_ADJ=WNG-SERB_CASH   # equity-only: subsequent cash out for WNG not funded by new debt in the window... treated as claim
for name,(c,g,i) in {'equity-only, cycle base 2020-25':(37.2,None,None),'equity-only, literal 5-yr':(53.8,None,None)}.items():
    top=pv(c,0,r)
    print(name, f"no growth at 5.43%: equity {top:.1f} less preferred {PREF_LIQ:.0f} and WNG financing net {ND_EQ_ADJ:.1f} -> per share {(top-PREF_LIQ-ND_EQ_ADJ)/SH_ISS:.2f}; at 10%: {(pv(c,0,0.10)-PREF_LIQ-ND_EQ_ADJ)/SH_ISS:.2f}; yield at price {c/(SH_ISS*PRICE)*100:.2f}%")
print("\n--- corrected equity-only (preferred dividends already deducted in owner cash; Series B cash and claim offset; WNG financing a claim, credited at nothing)")
ADJ=WNG
g_eq=(37.2/47.0)**(1/5.5)-1
print(f"equity-only growth prior 2015-19 avg 47.0 -> cycle 2020-25 avg 37.2: {g_eq*100:.2f}%/yr (decline: carried as the bottom)")
for lab,c in [('cycle base',37.2),('literal 5-yr',53.8)]:
    top=(pv(c,0,r)-ADJ)/SH_ISS; bot=(pv(c,g_eq,r)-ADJ)/SH_ISS
    t10=(pv(c,0,0.10)-ADJ)/SH_ISS; b10=(pv(c,g_eq,0.10)-ADJ)/SH_ISS
    print(f"  {lab}: range {bot:.2f} to {top:.2f}; fair {(t10+b10)/2:.2f}; yield at price {c/(SH_ISS*PRICE)*100:.2f}%")
print("\n--- cash-tax variant beside (deferred tax not charged), all-equity cycle base")
c=111.6+19.6
print(f"  no growth: {(pv(c,0,r)-CLAIMS)/SH_ISS:.2f}; return at price {c/(SH_ISS*PRICE+CLAIMS)*100:.2f}%")
print("\n--- growth-bought test: net growth investment per year over the cycle vs added owner cash")
print(f"  all-equity maintenance owner cash prior 86.3 -> cycle 111.6, +25.3/yr of annual cash over 5.5 yrs, for {247.9:.1f}/yr of net fleet investment over 6 yrs = {25.3/(247.9*6)*100:.2f}% on the added capital")
print("\n--- per-share on the cover count 21.144M beside (all-equity cycle base)")
for lab,v in [('top',pv(111.6,0,r)),('bottom',pv(111.6,0.048,r,spend=247.9))]:
    print(f"  {lab}: {(v-CLAIMS)/SH_COV:.2f}")
print("\n--- the signed, unclosed building purchase ($118.0M) beside: all-equity top falls by", f"{118.0/SH_ISS:.2f}/share")
print("\n--- growth credited without its spending (not a permitted case under (c)/(e); shown only to test the floor)")
v10=pv(111.6,0.048,0.10)
print(f"  at 10%: per share {(v10-CLAIMS)/SH_ISS:.2f}; at 5.43%: {(pv(111.6,0.048,r)-CLAIMS)/SH_ISS:.2f}")
# rate at which that case's value equals the price (all-equity)
lo,hi=0.01,0.20
for _ in range(60):
    mid=(lo+hi)/2
    if pv(111.6,0.048,mid)-CLAIMS > SH_ISS*PRICE: lo=mid
    else: hi=mid
print(f"  expected return at the price on that case: {mid*100:.2f}%")
print("\n--- cap check (f): all-equity owner cash carried ten years at 4.8%:", f"{111.6*1.048**10:.1f}", "vs highest share of sales earned 40.7% (2019)")
