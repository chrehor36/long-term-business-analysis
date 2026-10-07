import sys
sys.stdout.reconfigure(encoding="utf-8")
# $M, from the filed cash-flow faces (10-K FY2020, FY2022, FY2025; 10-Q Q2 2026)
Y=["2019","2020","2021","2022","2023","2024","2025","TTM"]
ocf ={"2019":10471,"2020":9844,"2021":12625,"2022":11018,"2023":11599,"2024":6805,"2025":7408,"TTM":7408+1391+7543}
capex={"2019":2054,"2020":1177,"2021":1367,"2022":1484,"2023":1852,"2024":2064,"2025":2112,"TTM":2112-751+684}
da  ={"2019":1365,"2020":1536,"2021":1452,"2022":1260,"2023":1128,"2024":1075,"2025":1050,"TTM":1050-546+530}
sbc ={"2019":201,"2020":126,"2021":337,"2022":356,"2023":254,"2024":286,"2025":279,"TTM":279-130+117}
# disclosed judgments: one-off cash inside operating cash
irs ={"2024":6000}                       # IRS Tax Litigation Deposit, paid 2024-09-10
fair={"2023":167,"2025":6069}            # fairlife milestone, operating-cash portion (275-108; 6,173-104); 2021's $100M split not disclosed, left in
pens={"2024":-523,"2025":-332,"TTM":0}   # surplus pension assets transferred into company cash (inflows, removed) [E4-41]; 2025's sat in H1 2025, outside the TTM
lp  ={"2024":-226,"2025":-306,"TTM":-(306-148)-75}  # tax-credit partnership investments (investing), cost of the tax benefit inside OCF
undist={"2019":421,"2020":511,"2021":615,"2022":838,"2023":1019,"2024":802,"2025":1038,"TTM":1038-387+520}  # equity income net of dividends
rows={}
print("FY | OCF | +IRS | +fairlife | -pension | -LP | adj OCF | SBC | capex | D&A | OE capex end | OE D&A end | look-through undistributed")
for y in Y:
    adj=ocf[y]+irs.get(y,0)+fair.get(y,0)+pens.get(y,0)+lp.get(y,0)
    oc=adj-sbc[y]-capex[y]; od=adj-sbc[y]-da[y]
    rows[y]=(ocf[y]-sbc[y]-capex[y], ocf[y]-sbc[y]-da[y], oc, od, undist[y])
    print(y, ocf[y], irs.get(y,0), fair.get(y,0), pens.get(y,0), lp.get(y,0), adj, sbc[y], capex[y], da[y], oc, od, undist[y])
def mean(ys,i): return sum(rows[y][i] for y in ys)/len(ys)
for name,ys in [("5y FY2021-25",Y[2:7]),("3y FY2023-25",Y[4:7]),("7y FY2019-25",Y[0:7])]:
    print(f"{name}: AS FILED capex-end {mean(ys,0):,.0f} D&A-end {mean(ys,1):,.0f} | ADJUSTED capex-end {mean(ys,2):,.0f} D&A-end {mean(ys,3):,.0f} | + look-through {mean(ys,4):,.0f}")
print("TTM to 2026-07-03: adjusted capex-end", rows["TTM"][2], "D&A-end", rows["TTM"][3], "look-through", rows["TTM"][4])
