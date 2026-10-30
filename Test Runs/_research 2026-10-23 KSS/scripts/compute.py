# COMPUTATION, NOT A CLEARANCE. KSS owner cash and the Q7 range arithmetic (USD millions).
# Inputs transcribed from the filed cash-flow statements (10-K FY2016, FY2019, FY2022, FY2025 accessions in the run file).
T = 0.243   # marginal tax: 21.0% federal + 3.3% state and local (FY2025 10-K tax note)
yrs  = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
ocf  = [2024,1474,2148,1691,2107,1657,1338,2271, 282,1168, 648,1380]
sbc  = [  48,  48,  41,  55,  87,  56,  40,  48,  30,  42,  30,  34]
capx = [ 682, 690, 768, 672, 578, 855, 334, 605, 826, 577, 466, 372]
flp  = [ 114, 114, 127, 138, 126, 113, 105, 125, 106,  93,  79,  83]   # capital/finance lease and financing obligation payments
intp = [ 329, 318, 299, 297, 282, 193, 254, 246, 284, 331, 312, 295]   # interest paid, net of capitalized
da   = [ 886, 934, 938, 991, 964, 917, 874, 838, 808, 749, 743, 700]
rev  = [19023,19204,18686,20084,20229,19974,15955,19433,18098,17476,16221,15527]  # total revenue (2014-16 net sales, pre ASC 606)
nsal = [19023,19204,18686,19036,19167,18885,15031,18471,17161,16586,15385,14775]
EO = [o-s-c-f for o,s,c,f in zip(ocf,sbc,capx,flp)]                     # equity-only, all spending
AE = [e+f+i*(1-T) for e,f,i in zip(EO,flp,intp)]                        # all-equity, before interest, after tax
AE_DA = [o-s-d+i*(1-T) for o,s,d,i in zip(ocf,sbc,da,intp)]             # depreciation variant, all-equity
EO_DA = [o-s-d-f for o,s,d,f in zip(ocf,sbc,da,flp)]
print("year   EO    AE   AE_DA  EO_DA  AE/rev")
for y,a,b,c,d,r in zip(yrs,EO,AE,AE_DA,EO_DA,rev): print(y, f"{a:6.0f} {b:6.0f} {c:6.0f} {d:6.0f}  {b/r*100:5.1f}%")
avg = lambda xs: sum(xs)/len(xs)
w = slice(7,12); p = slice(2,7)
base = {k:(avg(v[w]), avg(v[p])) for k,v in dict(EO=EO,AE=AE,AE_DA=AE_DA,EO_DA=EO_DA).items()}
for k,(b,pb) in base.items():
    g = (b/pb)**(1/5)-1 if b>0 and pb>0 else float('nan')
    h1 = avg(dict(EO=EO,AE=AE,AE_DA=AE_DA,EO_DA=EO_DA)[k][7:9]); h2 = avg(dict(EO=EO,AE=AE,AE_DA=AE_DA,EO_DA=EO_DA)[k][10:12])
    gh = (h2/h1)**(1/3)-1 if h1>0 and h2>0 else float('nan')
    print(f"{k:6} window FY21-25 avg {b:7.1f}  prior FY16-20 avg {pb:7.1f}  successive-window growth {g*100:6.2f}%/yr  halves {h1:.1f}->{h2:.1f} = {gh*100:5.2f}%/yr")
gs = (nsal[11]/nsal[7])**(1/4)-1; gd = (nsal[11]/nsal[1])**(1/10)-1
print(f"net sales growth FY21->FY25 {gs*100:.2f}%/yr; FY15->FY25 {gd*100:.2f}%/yr")
def pv(c, g, r, n=10):
    v = sum(c*(1+g)**t/(1+r)**t for t in range(1,n+1))
    return v + c*(1+g)**n / r / (1+r)**n
R = 0.0529; F = 0.10; ND = 2891.0; SH = 113.376445; PRICE = 24.00
print(f"\nnet debt {ND} (LTD 1,325 + finance leases and financing obligations 92 + 2,295 - cash 821, 10-Q Aug 1 2026); shares {SH}M; price {PRICE}")
def report(label, c, g, ae=True):
    vs = pv(c,g,R); vf = pv(c,g,F)
    if ae: ps, pf = (vs-ND)/SH, (vf-ND)/SH
    else: ps, pf = vs/SH, vf/SH
    irr_lo, irr_hi = 0.0, 1.0
    target = PRICE*SH + (ND if ae else 0)
    for _ in range(200):
        mid=(irr_lo+irr_hi)/2
        if pv(c,g,mid) > target: irr_lo=mid
        else: irr_hi=mid
    print(f"{label:52} c={c:7.1f} g={g*100:6.2f}%  value@5.29% {vs:8.0f} -> ${ps:7.2f}/sh   value@10% {vf:7.0f} -> ${pf:7.2f}/sh   return at price {mid*100:5.1f}%")
    return ps, pf
print("\nCENTRAL: all-equity, all spending deducted, successive five-year windows (specifics (a),(b))")
b = base["AE"][0]; g = (base["AE"][0]/base["AE"][1])**(1/5)-1
t_s, t_f = report("top: no growth", b, 0.0)
b_s, b_f = report("bottom: decline carried ten years, then flat", b, g)
print(f"  range ${b_s:.2f} to ${t_s:.2f}; width {t_s/b_s:.2f} to 1; FAIR PRICE (avg of ends at 10%) ${(t_f+b_f)/2:.2f}")
print("\nBESIDE: equity-only, all spending")
b2 = base["EO"][0]; g2 = (base["EO"][0]/base["EO"][1])**(1/5)-1
t2s,t2f = report("EO top: no growth", b2, 0.0, ae=False)
b2s,b2f = report("EO bottom: decline", b2, g2, ae=False)
print(f"  range ${b2s:.2f} to ${t2s:.2f}; FAIR PRICE equity-only ${(t2f+b2f)/2:.2f}")
print("\nBESIDE: depreciation variant, all-equity")
b3 = base["AE_DA"][0]; g3 = (base["AE_DA"][0]/base["AE_DA"][1])**(1/5)-1
t3s,t3f = report("AE_DA top: no growth", b3, 0.0)
b3s,b3f = report("AE_DA bottom: decline", b3, g3)
print(f"  range ${b3s:.2f} to ${t3s:.2f}; FAIR PRICE ${(t3f+b3f)/2:.2f}")
print("\nBESIDE: literal window, specific (b) halves (series changes sign in FY2022)")
gh = (avg(AE[10:12])/avg(AE[7:9]))**(1/3)-1
l1 = report("AE halves growth case", b, gh)
print(f"  literal pair: no-growth ${t_s:.2f} and halves-growth ${l1[0]:.2f}; fair ${(t_f+l1[1])/2:.2f}")
print("\nSENSITIVITY: base without FY2021 (FY22-25 average), all-equity")
b4 = avg(AE[8:12]); report("no growth on FY22-25 avg", b4, 0.0); report("decline on FY22-25 avg", b4, g)
print("\nSENSITIVITY: legal settlement $129M (FY2025) removed after tax")
b5 = (sum(AE[7:12]) - 129*(1-T))/5; report("no growth", b5, 0.0); report("decline", b5, g)
