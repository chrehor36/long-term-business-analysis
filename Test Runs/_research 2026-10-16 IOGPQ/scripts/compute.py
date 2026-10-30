# Owner cash and the COMPUTATION, NOT A CLEARANCE (USD millions). Figures as filed:
# 2016-2017 from the FY2017 10-K (0000866609-18-000006); 2018-2020 from the FY2020 10-K (0001437749-21-002669).
yrs=[2016,2017,2018,2019,2020]
ocf  ={2016:1.571,2017:28.030,2018:7.098,2019:34.150,2020:9.159}
sbc  ={2016:3.267,2017:2.552,2018:3.337,2019:4.701,2020:2.043}
capex={2016:1.488,2017:1.063,2018:1.514,2019:2.411,2020:1.121}
mcdl ={2016:14.884,2017:23.710,2018:28.276,2019:28.804,2020:27.247}
intp ={2016:15.691,2017:14.181,2018:12.463,2019:12.381,2020:12.520}
eq={y:ocf[y]-sbc[y]-capex[y]-mcdl[y] for y in yrs}
ae={y:eq[y]+intp[y] for y in yrs}  # before interest; no tax effect: no US tax paid in loss years (company's own tax unchanged)
for y in yrs: print(y, f"equity-only owner cash {eq[y]:8.3f}   all-equity (before interest) {ae[y]:8.3f}")
me=sum(eq.values())/5; ma=sum(ae.values())/5
print(f"5-yr mean equity-only {me:.3f}  all-equity {ma:.3f}")
h1=(ae[2016]+ae[2017])/2; h2=(ae[2019]+ae[2020])/2
print(f"halves all-equity: first {h1:.3f} second {h2:.3f}; equity-only first {(eq[2016]+eq[2017])/2:.3f} second {(eq[2019]+eq[2020])/2:.3f}")
r=0.0543; sh=29.617
nd=26.447+107.379-24.143  # 10-Q 2021-09-30 (0001437749-21-025105)
print(f"net debt 2021-09-30 {nd:.3f}")
v_ae=ma/r; v_eq=me/r
print(f"no-growth value at 5.43%: whole business {v_ae:.2f}; per share all-equity {(v_ae-nd)/sh:.2f}; equity-only {v_eq/sh:.2f}")
f_ae=ma/0.10; f_eq=me/0.10
print(f"fair (10%): whole business {f_ae:.2f}; per share all-equity {(f_ae-nd)/sh:.2f}; equity-only {f_eq/sh:.2f}")
mcdl_amort={2018:48.988,2019:39.541,2020:22.299}
print("MCDL amortization vs investment 2018-20:", {y:(mcdl_amort[y],mcdl[y]) for y in mcdl_amort})
# Specific (b): all-equity series changes sign; growth between half-window averages (2016-17 vs 2019-20, three years apart)
g=(h2/h1)**(1/3)-1
def val(base,g,rate):
    v=0; c=base
    for t in range(1,11):
        c*=1+g; v+=c/(1+rate)**t
    return v + c/rate/(1+rate)**10   # zero nominal growth after year ten
print(f"half-window growth all-equity {g*100:.1f}%/yr (decline: bottom case)")
lo=val(ma,g,r); hi=ma/r
print(f"range whole business at 5.43%: bottom {lo:.2f} top {hi:.2f}; per share {(lo-nd)/sh:.2f} to {(hi-nd)/sh:.2f}")
flo=val(ma,g,0.10); fhi=ma/0.10
print(f"fair at 10%: ends {flo:.2f} and {fhi:.2f}; average per share all-equity {((flo+fhi)/2-nd)/sh:.2f}")
