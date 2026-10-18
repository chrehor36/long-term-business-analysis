"""MTW owner cash and Q7 COMPUTATION. Figures USD millions, from the filed cash-flow statements
(accessions in the run file). OCF 2017-2019 has cash receipts on sold receivables (deferred purchase
price, classified as investing by the filer) added back; the 2019 $75.0M repurchase of previously
sold receivables is shown as a variant."""
yrs = list(range(2017, 2026))
ocf   = {2017:-324.9,2018:-513.0,2019:-53.3,2020:-35.1,2021:76.2,2022:76.9,2023:63.0,2024:49.2,2025:22.2}
dpp   = {2017:402.8,2018:553.1,2019:126.3}
sbc   = {2017:8.5,2018:7.4,2019:9.5,2020:6.0,2021:7.1,2022:8.5,2023:11.5,2024:10.9,2025:9.5}
capex = {2017:28.9,2018:31.7,2019:35.1,2020:26.3,2021:40.4,2022:61.8,2023:77.4,2024:45.7,2025:37.5}
ppe   = {2017:7.0,2018:13.0,2019:17.2,2020:0.5,2021:0.3,2022:1.5,2023:5.6,2024:4.8,2025:0.9}
acq   = {2021:186.2,2022:-2.3,2025:12.9}
intr  = {2017:39.2,2018:39.1,2019:32.7,2020:29.1,2021:28.9,2022:31.6,2023:33.9,2024:38.3,2025:37.7}
T = 0.21   # US statutory rate (Q7, Whose tax): interest added back after tax
oc  = {y: ocf[y]+dpp.get(y,0)-sbc[y]-capex[y]+ppe[y] for y in yrs}          # equity-only, before purchases
oca = {y: oc[y]+intr[y]*(1-T) for y in yrs}                                  # all-equity, before purchases
print("year  equity-only  all-equity  purchases")
for y in yrs: print(y, round(oc[y],1), round(oca[y],1), acq.get(y,0))
def avg(d, ys): return sum(d[y] for y in ys)/len(ys)
W = {"literal 2021-2025": range(2021,2026), "cycle peak-to-peak 2019-2023": range(2019,2024), "nine years 2017-2025": range(2017,2026)}
rf, floor = 0.056, 0.10
sh = 36.061969; price = 21.91; mcap = price*sh
debt_principal = 469.5 + 4.0      # 10-Q 2026-06-30: total debt 469.5 net of 4.0 deferred financing costs
cash = 95.8
nd = debt_principal - cash
print("");print(f"market cap {mcap:.1f}  net debt (principal less cash, 2026-06-30) {nd:.1f}  EV {mcap+nd:.1f}")
epa = {2025:45.6}
for name, ys in W.items():
    ys=list(ys)
    for label, d in (("equity-only", oc), ("all-equity", oca)):
        c = avg(d, ys); ca = c - sum(acq.get(y,0) for y in ys)/len(ys)
        ce = c + sum(epa.get(y,0) for y in ys)/len(ys)
        for tag, x in (("before purchases", c), ("purchases deducted", ca), ("before purchases, EPA added back", ce)):
            v_rf = x/rf; v_fl = x/floor
            if label=="all-equity": ps_rf=(v_rf-nd)/sh; ps_fl=(v_fl-nd)/sh; ret = x/(mcap+nd)
            else: ps_rf=v_rf/sh; ps_fl=v_fl/sh; ret = x/mcap
            print(f"{name:30s} {label:11s} {tag:34s} C={x:7.1f}  value/sh at 5.60% {ps_rf:7.2f}  at 10% {ps_fl:7.2f}  yield at price {ret*100:5.2f}%")
# cash needed to earn the floor at the price, no growth
print("");print(f"all-equity cash needed for 10% at the price: {0.10*(mcap+nd):.1f}; equity-only: {0.10*mcap:.1f}")
# sales growth 2021-2025 and 2019-2023 (for the record; owner cash changes sign so no growth is carried)
sales={2017:1581.3,2018:1846.8,2019:1834.1,2020:1443.4,2021:1720.2,2022:2032.5,2023:2227.8,2024:2178.0,2025:2240.9}
print("sales CAGR 2021-2025", round(((sales[2025]/sales[2021])**(1/4)-1)*100,2), "% ; 2017-2025", round(((sales[2025]/sales[2017])**(1/8)-1)*100,2),"%")
# Ceiling check, beyond what the range convention allows (the series changes sign, so (b) permits no growth):
# the best base (nine years, all-equity, EPA added back) grown at the 2021-2025 sales rate for ten years, then flat.
def pv(c, g, r):
    v = sum(c*(1+g)**t/(1+r)**t for t in range(1,11)); return v + c*(1+g)**10/r/(1+r)**10
for r in (rf, floor):
    v = pv(35.7, 0.0683, r)
    print(f"ceiling check at {r*100:.1f}%: EV {v:.1f} -> per share {(v-nd)/sh:.2f} (price {price})")
# Variant: the 2019 $75.0M repurchase of receivables previously sold to the old securitization program (filer, 2020 10-K)
# treated as financing, so added back to 2019 operating cash.
c = avg(oca, range(2019,2024)) + 75.0/5
print(f"variant 2019-2023 all-equity with the $75.0M unwind added back: C={c:.1f} value/sh at 5.60% {(c/rf-nd)/sh:.2f} at 10% {(c/floor-nd)/sh:.2f} yield {c/(mcap+nd)*100:.2f}%")
