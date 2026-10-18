# COMPUTATION, NOT A CLEARANCE. NWN 2026-10-18. USD millions. Sources: 10-K FY2023 (0001733998-24-000011), FY2025 (0001733998-26-000012), 10-Q Q2 2026 (0001733998-26-000127).
yrs=[2021,2022,2023,2024,2025]
ocf  ={2021:160.353,2022:147.672,2023:279.949,2024:200.282,2025:269.124}
capex={2021:293.892,2022:338.602,2023:327.347,2024:394.400,2025:466.893}
dep  ={2021:113.534,2022:116.707,2023:125.581,2024:137.898,2025:165.506}
sbc  ={2021:3.615,2022:3.228,2023:3.598,2024:3.231,2025:4.122}
intp ={2021:43.719,2022:50.823,2023:80.197,2024:71.233,2025:111.257}
tax  ={2021:27.4,2022:29.1,2023:32.362,2024:31.071,2025:41.359}
ni   ={2021:78.666,2022:86.303,2023:93.868,2024:78.871,2025:113.319}
acq  ={2021:1.289,2022:94.279,2023:7.533,2024:29.816,2025:338.131}
rev  ={2021:860.4,2022:1037.4,2023:1197.5,2024:1153.0,2025:1289.4}
shares=42.093538; price=48.99; rf=0.0543; floor=0.10
nd=121.289+125.685+2376.685-24.234   # 2026-06-30 balance sheet
def m(d): return sum(d.values())/len(d)
rows=[]
for y in yrs:
    t=tax[y]/(ni[y]+tax[y]); ai=intp[y]*(1-t)
    all_eq_all = ocf[y]+ai-sbc[y]-capex[y]
    all_eq_mnt = ocf[y]+ai-sbc[y]-dep[y]
    eq_mnt = ocf[y]-sbc[y]-dep[y]
    eq_all = ocf[y]-sbc[y]-capex[y]
    rows.append((y,t,all_eq_all,all_eq_mnt,eq_all,eq_mnt,capex[y]-dep[y]))
    print(f"{y} tax {t:.3f} | all-equity: all-spend {all_eq_all:8.1f} maint {all_eq_mnt:7.1f} | equity-only: all-spend {eq_all:8.1f} maint {eq_mnt:7.1f} | growth capex {capex[y]-dep[y]:6.1f}")
A=sum(r[2] for r in rows)/5; Cm=sum(r[3] for r in rows)/5; E=sum(r[4] for r in rows)/5; Ce=sum(r[5] for r in rows)/5; G=sum(r[6] for r in rows)/5
print(f"means: all-eq all-spend {A:.1f}; all-eq maint {Cm:.1f}; eq-only all-spend {E:.1f}; eq-only maint {Ce:.1f}; growth capex {G:.1f}; acquisitions {m(acq):.1f}")
print(f"net debt 2026-06-30 {nd:.1f}; market cap {shares*price:.1f}; EV {shares*price+nd:.1f}")
print(f"serial acquirer test: purchases {sum(acq.values()):.1f} vs half of all-eq maint owner cash before purchases {sum(r[3] for r in rows)/2:.1f}")
h1=(rows[0][3]+rows[1][3])/2; h2=(rows[3][3]+rows[4][3])/2
print(f"maint series halves: {h1:.1f} -> {h2:.1f}, rate {(h2/h1)**(1/3)-1:.3f}; sales growth {(rev[2025]/rev[2021])**0.25-1:.3f}; max owner cash/sales {max(r[3]/rev[r[0]] for r in rows):.3f}")
def ann(d,n=10): return (1-(1+d)**-n)/d
U=0.5*0.095+0.5*0.0474*(1-0.267)   # unlevered after-tax authorized return, Oregon order 2025 (CONVENTION of this run)
print(f"unlevered authorized return {U:.4f}")
def M0(C,d): return C/d
def Gc(C,d,g_spend,r): return C/d + g_spend*(r/d-1)*ann(d)
def ps(ev,debt=nd): return (ev-debt)/shares
print("ALL-EQUITY (less net debt), per share")
for d in (rf,floor):
    print(f"  d={d}: M0 {ps(M0(Cm,d)):7.2f}  G {ps(Gc(Cm,d,G,U)):7.2f}  literal all-spend no-growth {ps(M0(A,d)):8.2f}  default pair (acq deducted) M0 {ps(M0(Cm-m(acq),d)):7.2f}")
fair=(ps(M0(Cm,floor))+ps(Gc(Cm,floor,G,U)))/2
print(f"  fair price all-equity {fair:.2f}")
print("EQUITY-ONLY, per share (growth half equity-financed at 9.5% authorized ROE)")
for d in (rf,floor):
    print(f"  d={d}: M0 {M0(Ce,d)/shares:7.2f}  G {Gc(Ce,d,G/2,0.095)/shares:7.2f}  literal all-spend {M0(E,d)/shares:8.2f}")
faire=(M0(Ce,floor)/shares+Gc(Ce,floor,G/2,0.095)/shares)/2
print(f"  fair price equity-only {faire:.2f}")
print(f"yields at price: all-eq maint {Cm/(shares*price+nd):.4f}; equity-only maint {Ce/(shares*price):.4f}")
# floor test: the expected return at the price on the most generous stream (maintenance-only, 5.43% growth for ten years, then flat, NO growth spending charged)
def pv(C,g,d): return sum(C*(1+g)**t/(1+d)**t for t in range(1,11)) + C*(1+g)**10/d/(1+d)**10
def irr(target,C,g):
    lo,hi=0.001,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        if pv(C,g,mid)>target: lo=mid
        else: hi=mid
    return mid
print(f"generous all-equity stream: value at rf {ps(pv(Cm,rf,rf)):.2f}/sh; return at price {irr(shares*price+nd,Cm,rf):.4f}")
print(f"generous equity-only stream: return at price {irr(shares*price,Ce,rf):.4f}")
