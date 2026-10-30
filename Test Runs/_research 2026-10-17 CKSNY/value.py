# COMPUTATION, NOT A CLEARANCE. Q7 construction applied after the Q2 STOP for the reporting figures only.
R_SOV=0.057225   # BoE IUDLNPY 20-year nominal par gilt yield, 14 Oct 2026
SH=248.171717    # m shares in issue excl. treasury, Rule 2.9 statement 29 Sep 2026
PRICE=465.0      # pence, LSE close 16 Oct 2026 (aggregator, flagged)
ND_HY=429.6; DIV_FINAL=0.165*SH; DIV_INT=0.071*SH; LEASES=51.2
ND = ND_HY + DIV_FINAL + DIV_INT - LEASES   # net debt ex IFRS16 leases, subsequent dividends added
def pv(base,g,r,yrs=10):
    v=0; c=base
    for t in range(1,yrs+1):
        c=c*(1+g); v+=c/(1+r)**t
    return v + (c/r)/(1+r)**yrs   # zero nominal growth after year ten
cases = {
 "TOP: maintenance-only, no growth, cycle base 2018-25 before purchases (69.8 + 12.5 growth capex added back)": (82.3, 0.0),
 "no growth, all spending, cycle base 2018-25 before purchases": (69.8, 0.0),
 "literal window 2021-25, all spending, purchases deducted, no growth": (30.2, 0.0),
 "BOTTOM: literal window after purchases, declining at halves rate (22.5 -> 8.5 over 3 yrs)": (30.2, (8.5/22.5)**(1/3)-1),
}
print(f"net debt used {ND:.1f} (HY {ND_HY} + final {DIV_FINAL:.1f} + interim {DIV_INT:.1f} - leases {LEASES})")
print(f"market cap {SH*PRICE/100:.1f}m; EV {SH*PRICE/100+ND:.1f}m")
out={}
for k,(b,g) in cases.items():
    ev=pv(b,g,R_SOV); ev10=pv(b,g,0.10)
    out[k]=(ev,ev10)
    print(f"{k}\n   g={g*100:.1f}%  EV@sov {ev:7.1f} -> {(ev-ND)/SH*100:6.0f}p ; EV@10% {ev10:7.1f} -> {(ev10-ND)/SH*100:6.0f}p ; yield on EV at price {b/(SH*PRICE/100+ND)*100:.1f}%")
top=out[list(cases)[0]]; bot=out[list(cases)[-1]]
fair_ae=((top[1]-ND)+(bot[1]-ND))/2/SH*100
print("FAIR PRICE all-equity basis (avg of end cases at 10%, less net debt):", round(fair_ae), "p")
# equity-only: owner cash after interest (cycle base eq 61.4 + 12.5 maintenance add-back; window eq after acq 39.5-17.2)
top_eq=pv(61.4+12.5,0,0.10); bot_eq=pv(39.5-17.2,(8.5/22.5)**(1/3)-1,0.10)
print("FAIR PRICE equity-only basis:", round((top_eq+bot_eq)/2/SH*100), "p")
# what owner cash would the price need at 10% with no growth
print("owner cash needed (all-equity, no growth) to earn 10% at 465p:", round((SH*PRICE/100+ND)*0.10,1))

print("\n--- cycle-based range (specific (a): 2021 working-capital build and 2025 trough are aberrational end years)")
h1=(102.3+86.3+104.9-57.6)/4; h2=(102.7+88.7+37.0-20.0)/4; g=(h2/h1)**(1/4)-1
print("cycle halves after purchases 2018-21 vs 2022-25:", round(h1,1), round(h2,1), "g/yr", round(g*100,2))
bot_c=(pv(55.5,g,R_SOV), pv(55.5,g,0.10))
print(f"BOTTOM (cycle): base 55.5 after purchases, g {g*100:.1f}%: EV@sov {bot_c[0]:.1f} -> {(bot_c[0]-ND)/SH*100:.0f}p; EV@10% {bot_c[1]:.1f} -> {(bot_c[1]-ND)/SH*100:.0f}p")
print(f"TOP: EV@sov -> {(top[0]-ND)/SH*100:.0f}p; EV@10% -> {(top[1]-ND)/SH*100:.0f}p")
print("width top/bottom EV@sov:", round(top[0]/bot_c[0],2), " per share:", round((top[0]-ND)/(bot_c[0]-ND),2))
fair=((top[1]-ND)+(bot_c[1]-ND))/2/SH*100
print("FAIR PRICE all-equity (cycle range):", round(fair),"p")
# equity-only: owner cash after interest: cycle eq avg 2018-25 = 61.4 before purchases; after purchases 61.4-14.3
acq_avg=sum([1.0,25.9,1.4,43.7,3.5,0,0,38.9])/8
te=pv(61.4+12.5,0,0.10); be=pv(61.4-acq_avg,g,0.10)
print("acq avg 2018-25", round(acq_avg,1), "FAIR PRICE equity-only:", round((te+be)/2/SH*100),"p")
print("expected return at price, top case no growth (all-equity):", round(82.3/(SH*PRICE/100+ND)*100,1),"%")
