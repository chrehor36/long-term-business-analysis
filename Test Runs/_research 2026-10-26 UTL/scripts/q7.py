# Q7 arithmetic for the UTL run (2026-10-26). All inputs from filed statements (FY2025, FY2022, FY2019 10-Ks; 10-Q Q2 2026).
import sys
sys.stdout.reconfigure(encoding="utf-8")
yrs = [2021, 2022, 2023, 2024, 2025]
ocf   = [107.8, 97.7, 107.0, 125.9, 131.3]
capex = [115.0, 122.1, 141.0, 169.9, 185.1]
acq   = [0, 0, 0, 0, 160.4]
da    = [59.5, 62.6, 67.4, 76.1, 88.7]
sbc   = [1.4, 2.1, 1.9, 2.4, 3.3]          # restricted stock expense (10-K notes)
intpd = [26.0, 26.0, 30.9, 31.2, 39.3]     # interest paid (supplemental)
deftx = [10.8, 11.0, 7.4, 13.2, 9.6]       # deferred tax provision (cash flow statement)
pis   = {2020:1595.0, 2021:1688.9, 2022:1791.3, 2023:1907.8, 2024:2051.2, 2025:2342.2}
cwip  = {2020:34.8, 2021:47.5, 2022:52.6, 2023:65.3, 2024:92.9, 2025:101.7}
rate  = {2021:.0329, 2022:.0326, 2023:.0333, 2024:.0349, 2025:.0345}
dep = [ (( (pis[y-1]-cwip[y-1]) + (pis[y]-cwip[y]) )/2)*rate[y] for y in yrs]
avg = lambda v: sum(v)/len(v)
print("plant depreciation", [round(x,1) for x in dep], "avg", round(avg(dep),1))
oc_all  = [o-s-c-a for o,s,c,a in zip(ocf,sbc,capex,acq)]
oc_allx = [o-s-c for o,s,c in zip(ocf,sbc,capex)]
oc_mnt  = [o-s-d for o,s,d in zip(ocf,sbc,dep)]
oc_mda  = [o-s-d for o,s,d in zip(ocf,sbc,da)]
gs      = [c-d for c,d in zip(capex,dep)]
print("owner cash after all spending incl acq", [round(x,1) for x in oc_all], "avg", round(avg(oc_all),1))
print("owner cash after all capex, acq excl", [round(x,1) for x in oc_allx], "avg", round(avg(oc_allx),1))
print("owner cash after maintenance (plant dep)", [round(x,1) for x in oc_mnt], "avg", round(avg(oc_mnt),1))
print("owner cash after maintenance (full D&A)", [round(x,1) for x in oc_mda], "avg", round(avg(oc_mda),1))
print("growth spending", [round(x,1) for x in gs], "avg", round(avg(gs),1))
print("book-tax variant (maint less deferred tax)", round(avg([m-t for m,t in zip(oc_mnt,deftx)]),1))
# shown growth, aggregate, end years
g = (oc_mnt[-1]/oc_mnt[0])**(1/4)-1
h1 = avg(oc_mnt[:2]); h2 = avg(oc_mnt[3:])
g_half = (h2/h1)**(1/3)-1
print(f"shown growth end years {g*100:.2f}%  halves(2021-22 vs 2024-25, 3 yrs apart) {g_half*100:.2f}%")
# sales growth for cap test
rev = {2021:473.3, 2025:536.0}
print(f"revenue growth 2021-2025 {((rev[2025]/rev[2021])**0.25-1)*100:.2f}%")
# debt credit
ltd2020, ltd2025 = 523.1+8.5, 632.6+37.9
credit = (ltd2025-ltd2020)/5
cap = 0.48
credit_c = min(credit, cap*avg(gs))
print(f"LTD increase/yr {credit:.1f}; cap 48% x growth spend {cap*avg(gs):.1f}; credit {credit_c:.1f}")
sh = 18.236674; netdebt = 234.8+40.8+680.4-9.2; price = 55.15
after_tax_int = [i*(1-0.234) for i in intpd]
def value(base, growth, gspend, r, years=10):
    pv = 0; oc = base; gsp = gspend
    for t in range(1, years+1):
        oc = base*(1+growth)**t
        gsp_t = gspend*(1+growth)**(t-1) if gspend else 0
        pv += (oc-gsp_t)/(1+r)**t
    term = (base*(1+growth)**years)/r/(1+r)**years
    return pv+term
S = 0.0533
base = avg(oc_mnt); gsp_net = avg(gs)-credit_c
print(f"base {base:.1f}; growth spend net of credit {gsp_net:.1f}; market cap {price*sh:.1f}; net debt {netdebt:.1f}")
for label, gr in [("total shown", g)]:
    ng = value(base, 0, 0, S); gc = value(base, gr, gsp_net, S)
    print(f"EQUITY-ONLY at sovereign: no-growth {ng:.1f} (${ng/sh:.2f}); growth case {gc:.1f} (${gc/sh:.2f}); width {max(ng,gc)/min(ng,gc):.2f}")
    ng10 = value(base, 0, 0, .10); gc10 = value(base, gr, gsp_net, .10)
    print(f"  at 10%: no-growth {ng10:.1f} (${ng10/sh:.2f}); growth {gc10:.1f} (${gc10/sh:.2f}); FAIR (avg) ${(ng10+gc10)/2/sh:.2f}")
    print(f"  implied return at price, no-growth case: {base/(price*sh)*100:.2f}%")
# all-equity: add back after-tax interest; no debt credit
base_ae = avg([m+i for m,i in zip(oc_mnt, after_tax_int)])
gs_ae = avg(gs)
ng = value(base_ae,0,0,S)-netdebt; gc = value(base_ae,g,gs_ae,S)-netdebt
ng10 = value(base_ae,0,0,.10)-netdebt; gc10 = value(base_ae,g,gs_ae,.10)-netdebt
print(f"ALL-EQUITY: base {base_ae:.1f}; no-growth ${ng/sh:.2f}; growth ${gc/sh:.2f}; at 10%: ${ng10/sh:.2f}, ${gc10/sh:.2f}; FAIR ${(ng10+gc10)/2/sh:.2f}")
# all-spending case (beside): growth spending charged in full, no credit, same growth
gc_all = value(base, g, avg(gs), S)
print(f"equity-only, growth case all growth spending no credit: ${gc_all/sh:.2f}")
# organic pair (serial acquirer test)
before_purch = sum(oc_mnt); print(f"serial acquirer test: purchases {sum(acq):.1f} vs half owner cash before purchases {before_purch/2:.1f}")
# literal window all-spending
print(f"literal all-spending avg incl acquisitions {avg(oc_all):.1f}; excl acquisitions {avg(oc_allx):.1f}")

print("\n--- organic pair (serial acquirer convention) ---")
# acquired contribution in 2025, from the filer's own figures (10-K MD&A): gas margin 16.6, O&M 4.2, property tax 1.4, D&A 3.3
acq_pre = 16.6-4.2-1.4                       # cash before interest and tax
acq_debt_avg = 71.4*11/12 + 86.0*2/12         # months held in 2025
acq_int = acq_debt_avg*0.055                  # guess: 5.5%, between the term-loan and note rates the filings state
acq_after = (acq_pre-acq_int-3.3)*(1-0.234)
org2025 = oc_mnt[-1]-acq_after
g_org = (org2025/oc_mnt[0])**(1/4)-1
print(f"acquired after-tax contribution {acq_after:.1f}; organic 2025 owner cash {org2025:.1f}; organic growth {g_org*100:.2f}%")
bot = value(base, g_org, gsp_net, S); bot10 = value(base, g_org, gsp_net, .10)
ng = value(base,0,0,S); ng10 = value(base,0,0,.10)
print(f"CENTRAL equity-only organic: top no-growth ${ng/sh:.2f}; bottom growth-case ${bot/sh:.2f}; width {ng/bot:.2f}; at 10%: ${ng10/sh:.2f}, ${bot10/sh:.2f}; FAIR ${(ng10+bot10)/2/sh:.2f}")
print(f"  year-1 growth spending charged (net of credit) {gsp_net:.1f}; year-10 {gsp_net*(1+g_org)**9:.1f}; credit year1 {credit_c:.1f} year10 {credit_c*(1+g_org)**9:.1f}")
# default pair beside: acquisitions deducted, total growth
base_d = avg([m-a for m,a in zip(oc_mnt,acq)])
top_d = value(base_d,0,0,S); gc_d = value(base_d,g,gsp_net,S)
top_d10 = value(base_d,0,0,.10); gc_d10 = value(base_d,g,gsp_net,.10)
print(f"DEFAULT pair beside: base {base_d:.1f}; no-growth ${top_d/sh:.2f}; growth ${gc_d/sh:.2f}; FAIR ${(top_d10+gc_d10)/2/sh:.2f}")
# all-equity beside on organic pair
bot_ae = value(base_ae, g_org, gs_ae, S)-netdebt; bot_ae10 = value(base_ae, g_org, gs_ae, .10)-netdebt
top_ae = value(base_ae,0,0,S)-netdebt; top_ae10 = value(base_ae,0,0,.10)-netdebt
print(f"ALL-EQUITY organic beside: top ${top_ae/sh:.2f}; bottom ${bot_ae/sh:.2f}; FAIR ${(top_ae10+bot_ae10)/2/sh:.2f}")
print(f"expected return at price, top case equity-only: {base/(price*sh)*100:.2f}% ; all-equity top: {base_ae/(price*sh+netdebt)*100:.2f}%")
# cap test: owner cash share of sales
print(f"owner cash/revenue 2025 {oc_mnt[-1]/536.0*100:.1f}%; max share in window {max(o/r for o,r in zip(oc_mnt,[473.3,563.2,557.1,494.8,536.0]))*100:.1f}%")

print("\n--- water deal closed 2026-06-30 (after window): cash paid 42.1 + 0.6, credited at nothing ---")
w = 42.7
print(f"central top ${(ng-w)/sh:.2f}; bottom ${(bot-w)/sh:.2f}; width {(ng-w)/(bot-w):.2f}; FAIR ${((ng10+bot10)/2-w)/sh:.2f}")
print(f"book-tax variant top ${(40.1/S - w)/sh:.2f}; full D&A variant top ${(avg(oc_mda)/S - w)/sh:.2f}")
print(f"expected return at price incl water debt, top case: {base/(price*sh+w)*100:.2f}%")
print(f"growth spending gross year1 {avg(gs):.1f} year10 {avg(gs)*(1+g_org)**9:.1f}")
print(f"AWC-MA beside: ~{(70.0-42.1)/sh:.2f}/share on cash alone")
print(f"exact: ng {ng:.1f} bot {bot:.1f} ng10 {ng10:.1f} bot10 {bot10:.1f} fair {((ng10+bot10)/2-w)/sh:.3f}")
