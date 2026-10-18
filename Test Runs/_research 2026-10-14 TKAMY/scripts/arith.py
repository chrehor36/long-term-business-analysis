# Arithmetic for the TKAMY run, every input typed from the filed statements (document and page in the run file).
# Same numbers sooner, no number added.
import sys
sys.stdout.reconfigure(encoding="utf-8")
yrs = ["FY21","FY22","FY23","FY24","FY25"]
# Group cash flow statement lines, EUR m (AR 2021/22 p.CF for FY21-22, AR 2022/23 for FY23, AR 2024/25 p.232-233 for FY24-25)
ocf   = [92, 617, 2064, 1353, 1684]
capex = [-1404, -1247, -1698, -1525, -1563]    # PP&E incl. advance payments and investment property
intang= [-44, -49, -59, -71, -91]              # intangible assets incl. advance payments
grants= [0, 0, 154, 417, 346]                  # proceeds from government grants (direct reduction plant)
lease = [-148, -141, -147, -139, -145]         # lease liabilities (principal) in financing
minor = [-44, -40, -51, -43, -43]              # profit attributable to non-controlling interest paid
acq   = [-36, -1, -3, -15, -5]                 # acquisitions of consolidated companies net of cash
disp  = [1, 855, -6, 60, 437]                  # disposals of previously consolidated companies net of cash
intpaid=[159, 131, 116, 97, 51]
intrec =[10, 29, 167, 210, 148]
dep   = [923, 910, 900, 749, 663]              # segment-table depreciation, group total
sales = [34015, 41140, 37536, 35041, 32837]
oc_eq = [o+c+i+g+l+m for o,c,i,g,l,m in zip(ocf,capex,intang,grants,lease,minor)]
oc_ae = [e + (p - r) for e,p,r in zip(oc_eq,intpaid,intrec)]
oc_dep= [o - d + l + m for o,d,l,m in zip(ocf,dep,lease,minor)]
print("year   owner cash equity-only | all-equity (before net interest) | depreciation variant | net M&A")
for y,a,b,c,d1,d2 in zip(yrs,oc_eq,oc_ae,oc_dep,acq,disp):
    print(f"{y}  {a:8d}  {b:8d}  {c:8d}  {d1+d2:6d}")
avg = lambda v: sum(v)/len(v)
print(f"5-yr avg: equity-only {avg(oc_eq):.0f}; all-equity {avg(oc_ae):.0f}; depreciation variant {avg(oc_dep):.0f}")
print(f"5-yr sums: equity-only {sum(oc_eq)}; all-equity {sum(oc_ae)}; dep variant {sum(oc_dep)}")
print("first half (FY21-22) vs second half (FY24-25) all-equity:", avg(oc_ae[:2]), avg(oc_ae[3:]))
# Parts: segment EBIT and adjusted EBIT, EUR m (segment notes: AR 2021/22 FY21, AR 2022/23 FY22 old structure, AR 2023/24 FY23, AR 2024/25 FY24-25)
parts = {
 "Steel Europe":        ([-59, 887, -1695, -770, 189], [116, 1200, 319, 261, 337]),
 "Materials Services":  ([594, 970, 204, 8, 82],       [587, 837, 178, 204, 132]),
 "Marine Systems":      ([24, 24, 70, 127, 123],       [26, 32, 73, 125, 127]),
}
for k,(e,a) in parts.items():
    print(f"{k:20s} EBIT 5y {sum(e):6d}   adjusted 5y {sum(a):6d}")
print("group EBIT 5y", sum([451,1827,-1431,-1041,76]), " group adjusted 5y", sum([796,2062,703,567,640]))
# Materials Services ten years FY16-FY25 (sales, EBIT, adjusted EBIT, average capital employed)
ms = [(11601,76,128,3861),(13364,220,312,3652),(14427,270,317,3621),(13607,66,107,3866),(9895,-540,-85,3031),
      (12315,594,587,2587),(16444,970,837,3921),(13613,204,178,3668),(12126,8,204,3307),(11432,82,132,3256)]
S=sum(x[0] for x in ms); E=sum(x[1] for x in ms); A=sum(x[2] for x in ms); C=sum(x[3] for x in ms)
print(f"MS 10y: sales {S}, EBIT {E} ({100*E/S:.2f}%), adj {A} ({100*A/S:.2f}%), EBIT/CE {100*E/C:.1f}%, adj/CE {100*A/C:.1f}%")
for i,(s,e,a,c) in enumerate(ms):
    print(f"  FY{16+i}: EBIT margin {100*e/s:5.2f}%  adj {100*a/s:5.2f}%  adj/CE {100*a/c:5.1f}%  EBIT/CE {100*e/c:5.1f}%")
# Rivals, ten calendar years 2016-2025 (2016-2024 for ZEUS), from rivals_xbrl.txt
rs_s=[8613.4,9721.0,11534.5,10973.8,8811.9,14093.3,17025.0,14805.9,13835.0,14294.3]; rs_o=[517.8,662.4,937.5,1013.5,565.8,1948.9,2506.9,1739.5,1160.0,1012.7]
ry_s=[2859.7,3364.7,4408.4,4501.6,3466.6,5675.3,6323.6,5108.7,4598.7,4571.3]; ry_o=[122.1,101.1,139.2,210.8,64.6,545.2,578.7,228.1,31.5,-30.8]
ze_s=[1055.1,1330.7,1715.1,1579.0,1234.1,2312.3,2560.0,2158.2,1941.7]; ze_o=[5.7,24.0,57.1,16.6,0.6,172.5,133.7,77.7,47.9]
for n,s,o in [("Reliance",rs_s,rs_o),("Ryerson",ry_s,ry_o),("Olympic",ze_s,ze_o)]:
    print(f"{n}: {len(s)}y operating margin {100*sum(o)/sum(s):.2f}%  (last five {100*sum(o[-5:])/sum(s[-5:]):.2f}%)")
print(f"tk MS last five EBIT margin {100*sum(x[1] for x in ms[-5:])/sum(x[0] for x in ms[-5:]):.2f}%  adj {100*sum(x[2] for x in ms[-5:])/sum(x[0] for x in ms[-5:]):.2f}%")
# Steel Europe five-year capex, depreciation, impairments
se_capex=[681,630,1065,974,1000]; se_dep=[274,288,270,95,46]; se_imp=[0,403,2111,962,602]; se_ce=[4062,5636,5401,3616,3044]
print("Steel Europe 5y capex",sum(se_capex),"dep",sum(se_dep),"impairments",sum(se_imp),"EBIT/CE",round(100*-1448/sum(se_ce),1),"% adj/CE",round(100*2233/sum(se_ce),1),"%")
# Price and shares
shares=622_531_741; px=13.825
print(f"market cap EUR m {shares*px/1e6:.1f}")
# ---- Q7 COMPUTATION, NOT A CLEARANCE ----
rf=0.0376; floor=0.10
nfa_jun26=2621; hkm=300   # HKM contribution: "low to mid three-digit million", midpoint 300 (CONVENTION of this run)
net_cash=nfa_jun26-hkm
oc_dep_ae=[c+(p-r) for c,p,r in zip(oc_dep,intpaid,intrec)]
base_ae=avg(oc_ae); base_eq=avg(oc_eq); base_dep=avg(oc_dep_ae)
def per(v): return v/shares*1e6
print("net cash used", net_cash, " dep-variant all-equity by year", oc_dep_ae, "avg", round(base_dep,1))
for lab,b in [("central all-equity",base_ae),("depreciation variant all-equity",base_dep)]:
    v=b/rf; f=b/floor
    print(f"{lab}: base {b:.0f}; no-growth value at 3.76% {v:.0f} -> equity {v+net_cash:.0f} = EUR {per(v+net_cash):.2f}/sh; fair (10%) {f:.0f} -> {f+net_cash:.0f} = EUR {per(f+net_cash):.2f}/sh; yield at price on EV {100*b/(shares*px/1e6-net_cash):.2f}%")
v=base_eq/rf; f=base_eq/floor
print(f"equity-only: base {base_eq:.0f}; value {v:.0f} = EUR {per(v):.2f}/sh; fair {f:.0f} = EUR {per(f):.2f}/sh")
