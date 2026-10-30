# Owner earnings by hand, Amazon. Every input is read off a filed cash-flow statement, supplemental
# cash-flow table, property note or segment note (accessions in owner_earnings.md). $M.
Y = ["2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","TTM2Q26"]
OCF = [17203,18365,30723,38514,66064,46327,46752,84946,115877,139514,161403]
SBC = [2975,4215,5418,6864,9208,12757,19621,24023,22011,19467,19314]
CAPEX=[7804,11955,13427,16861,40140,61053,63645,52729,82999,131819,173028]   # purchases of P&E, gross
PROC =[1067,1897,2104,4172,5096,5657,5324,4596,5341,3499,4021]            # proceeds from P&E sales and incentives
FLADD=[5704,9637,10615,13723,11588,7061,675,642,854,2911,4048]            # P&E acquired under capital/finance leases
BTS  =[1209,3541,3641,1362,2267,5846,3187,357,97,441,None]                # build-to-suit / financing-obligation additions
FLREP=[3860,4799,7449,9628,10642,11163,7941,4384,2043,1557,1599]          # principal repayments of finance (capital) leases
FOREP=[147,200,337,27,53,162,248,271,669,328,308]                         # principal repayments of financing obligations
TNA  =[13585,29783,25068,30018,57976,72325,60836,48344,85752,142352,142352-58210+118648]  # total net additions to P&E (segment note)
DEP  =[6400,8831,12138,15150,16239,22909,24924,30225,32067,41860,41860-18822+26703]      # D&A on P&E incl. finance-lease amortization
REV  =[135987,177866,232887,280522,386064,469822,513983,574785,637959,716924,716924-323369+382125]
rows=[]
for i,y in enumerate(Y):
    base = OCF[i]-SBC[i]
    cashc = CAPEX[i]-PROC[i]+FLREP[i]+FOREP[i]          # (c) cash basis: plant paid for in cash, incl. lease principal
    formc = TNA[i]                                       # (c) capital-formation basis: filed total net additions
    capexonly = CAPEX[i]                                  # the screen's construction, for reproduction
    rows.append(dict(y=y, base=base, oe_capexonly=base-capexonly, oe_cash=base-cashc, oe_form=base-formc,
                     oe_dep=base-DEP[i], cashc=cashc, formc=formc, dep=DEP[i], ratio=formc/DEP[i], rev=REV[i],
                     sbc_ocf=SBC[i]/OCF[i]))
def mean(k, ys): 
    v=[r[k] for r in rows if r["y"] in ys]; return sum(v)/len(v)
hdr="| year | OCF−SBC | (c) cash basis | (c) formation (TNA) | P&E D&A | TNA/D&A | OE capex-only | OE cash basis | OE formation | OE D&A end (INVALID) | SBC/OCF |"
print(hdr); print("|"+"---|"*11)
for r in rows:
    print(f"| {r['y']} | {r['base']:,} | {r['cashc']:,} | {r['formc']:,} | {r['dep']:,} | {r['ratio']:.2f}x | {r['oe_capexonly']:,} | {r['oe_cash']:,} | {r['oe_form']:,} | {r['oe_dep']:,} | {r['sbc_ocf']*100:.1f}% |")
W = {"5-yr 2021-25":["2021","2022","2023","2024","2025"], "3-yr 2023-25":["2023","2024","2025"],
     "5-yr 2016-20":["2016","2017","2018","2019","2020"], "10-yr 2016-25":Y[:10],
     "5-yr to TTM (2022-TTM)":["2022","2023","2024","2025","TTM2Q26"], "TTM alone":["TTM2Q26"],
     "5-yr 2019-23":["2019","2020","2021","2022","2023"]}
print()
print("| window | OE capex-only | OE cash basis | OE formation | OE D&A end (INVALID) |"); print("|---|---|---|---|---|")
for w,ys in W.items():
    print(f"| {w} | {mean('oe_capexonly',ys):,.0f} | {mean('oe_cash',ys):,.0f} | {mean('oe_form',ys):,.0f} | {mean('oe_dep',ys):,.0f} |")
# cumulative SBC/OCF
for w,ys in [("10-yr 2016-25",Y[:10]),("5-yr 2021-25",W["5-yr 2021-25"])]:
    idx=[Y.index(y) for y in ys]
    print(w, "cumulative SBC/OCF = %.1f%%  (SBC %s / OCF %s)" % (100*sum(SBC[i] for i in idx)/sum(OCF[i] for i in idx), f"{sum(SBC[i] for i in idx):,}", f"{sum(OCF[i] for i in idx):,}"))
# judged maintenance: k x P&E D&A, k in 1.0..1.6
print()
print("| window | OE at (c)=1.0x D&A | 1.3x | 1.6x |"); print("|---|---|---|---|")
for w,ys in W.items():
    idx=[Y.index(y) for y in ys]
    b=sum(OCF[i]-SBC[i] for i in idx)/len(idx); d=sum(DEP[i] for i in idx)/len(idx)
    print(f"| {w} | {b-d:,.0f} | {b-1.3*d:,.0f} | {b-1.6*d:,.0f} |")
