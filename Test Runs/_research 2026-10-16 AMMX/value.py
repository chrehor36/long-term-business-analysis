# COMPUTATION, NOT A CLEARANCE. Q7's construction applied after the Q2 STOP, for the reporting figures only.
R=0.0543; F=0.10; SH=21112988; SH_SEC=14829155; P=0.099
ND=12426375            # net debt 2026-06-30 (R26Q2)
FLOOR=1549303          # lines of credit at 2026-06-30, shown as working capital beside
def pv(c0,g,r,years=10):
    v=0;c=c0
    for t in range(1,years+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**years   # no growth after year ten
cases={
 'central cycle 2020-23 all-equity':304764,
 'central cycle 2020-23 equity-only':-210134,
 'literal 2021-25 all-equity':965829,
 'literal 2021-25 equity-only':316831,
}
for k,c in cases.items():
    eq='equity-only' in k
    v=pv(c,0,R); f=pv(c,0,F)
    vs=(v if eq else v-ND)/SH; fs=(f if eq else f-ND)/SH
    print(f"{k:38s} value ${vs:7.3f}/sh  fair(10%) ${fs:7.3f}/sh  yield at price {c/((P*SH)+(0 if eq else ND))*100:5.1f}%")
# decline case on the literal window, halves 2021-22 vs 2024-25, three years apart
for k,(a,b) in {'all-equity':(2617202,1500369),'equity-only':(2104667,581637)}.items():
    g=(b/a)**(1/3)-1; c=965829 if k=='all-equity' else 316831
    v=pv(c,g,R); f=pv(c,g,F); eq=k=='equity-only'
    print(f"literal decline {k}: g={g*100:.1f}%  value ${((v if eq else v-ND)/SH):.3f}/sh  fair ${((f if eq else f-ND)/SH):.3f}/sh")
print('fair central with floor plan as working capital:', f"{(pv(304764,0,F)-(ND-FLOOR))/SH:.3f}")
print('central value on SEC share count:', f"{(pv(304764,0,R)-ND)/SH_SEC:.3f}", 'fair', f"{(pv(304764,0,F)-ND)/SH_SEC:.3f}")
print('EV at price', P*SH+ND)
