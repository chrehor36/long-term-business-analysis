# COMPUTATION, NOT A CLEARANCE. Owner cash from the filed cash-flow statements, USD millions.
T=0.21  # US statutory rate, used only to put net interest on an after-tax basis (CONVENTION of the run)
yrs={ # OCF, SBC, capex, net interest expense (+) / income (-)
 2019:(146.428,19.8,140.5, 98.312),   # 10-K FY2020 0000886835-21-000003 (2019 column); SBC/capex XBRL first-filed
 2020:(2.217,2.6,47.7, 92.399),
 2021:(58.884+5.383,2.710+0.935,34.152+3.035, 0.0),  # successor + predecessor, 10-K FY2023
 2022:(175.416,4.807,65.784,-11.713),
 2023:(202.390,4.123,74.496,-25.761),
}
eq={y:o-s-c for y,(o,s,c,i) in yrs.items()}
ae={y:eq[y]+i*(1-T) for y,(o,s,c,i) in yrs.items()}
for y in yrs: print(y, f"equity-only {eq[y]:7.1f}  all-equity {ae[y]:7.1f}")
m_eq=sum(eq.values())/5; m_ae=sum(ae.values())/5
print(f"5yr mean equity-only {m_eq:.1f}  all-equity {m_ae:.1f}")
# TTM to 2024-09-30
ocf=202.390-155.346+225.185; cap=74.496-67.218+67.447; sbc=4.123-3.100+2.436
print(f"TTM Sep-2024 owner cash (as filed) {ocf-sbc-cap:.1f}; WC release in 9M2024 67.4")
# sales growth over the window: 2019 1,425.4 -> 2023 919.4
g_sales=(919.420/1425.369)**0.25-1
g_ae=(ae[2023]/ae[2019])**0.25-1
print(f"shown growth all-equity {g_ae:.3%}; sales growth {g_sales:.3%}")
def pv(base,g,r,yrs=10):
    v=0;c=base
    for t in range(1,yrs+1):
        c=c*(1+g); v+=c/(1+r)**t
    v+= c/r/(1+r)**yrs   # zero nominal growth after year ten
    return v
r=0.0543
shares=20.127229
# net debt: latest filed (2024-09-30): no borrowings; cash & equivalents 325.881 (restricted 54.707 shown beside)
# subsequent events stated: going-private cash-out ~ $8.0M. Quail Tools (Aug 2025): $375M cash + $250M seller note (aggregator-reported), credited at nothing.
nd_filed=-325.881+8.0
nd_quail=nd_filed+625.0
for label,base in (("all-equity",m_ae),("equity-only",m_eq)):
    top=pv(base,0.0,r); bot=pv(base,g_sales,r)
    t10=pv(base,0.0,0.10); b10=pv(base,g_sales,0.10)
    print(f"\n{label}: base {base:.1f}")
    for ndl,nd in (("net debt as filed + cash-out",nd_filed),("plus Quail financing",nd_quail)):
        if label=="equity-only": nd_use=0.0
        else: nd_use=nd
        print(f"  [{ndl if label=='all-equity' else 'no net debt deduction (equity-only)'}]")
        print(f"   range per share: bottom {(bot-nd_use)/shares:7.2f}  top {(top-nd_use)/shares:7.2f}   (EV bottom {bot:.0f}, top {top:.0f})")
        print(f"   fair price (avg of ends at 10%): {((t10+b10)/2-nd_use)/shares:7.2f}  (ends at 10%: {b10:.0f}, {t10:.0f})")
        if label=="equity-only": break
    # earnings yield at the price
print("\nprice 80.00; market cap", 80*shares)
print("literal-window growth variant check: shown-growth case (uncut) all-equity:", pv(m_ae,g_ae,r))

# Beside: the uncut shown-growth case (12.8%) and the successor-only sales growth 2021-2023
g_succ=(919.420/(648.754+45.928))**0.5-1
print(f"\nsuccessor sales growth 2021-2023: {g_succ:.2%}")
ev_price=80*shares-325.881+8.0
print(f"EV at $80, net debt as filed + cash-out: {ev_price:.0f}; with Quail: {ev_price+625:.0f}")
for g in (g_ae,):
    v10=pv(m_ae,g,0.10); vr=pv(m_ae,g,r)
    print(f"uncut shown growth {g:.2%}: value at 5.43% {vr:.0f} (per share {(vr-nd_filed)/shares:.2f}); at 10% {v10:.0f} (per share {(v10-nd_filed)/shares:.2f}; with Quail {(v10-nd_quail)/shares:.2f})")
    print(f"  year-10 owner cash {m_ae*(1+g)**10:.0f} = {m_ae*(1+g)**10/919.42:.1%} of 2023 sales; best share of sales in window {103.4/919.42:.1%}")
print(f"no-growth yield on EV at $80: {m_ae/ev_price:.2%}; with Quail {m_ae/(ev_price+625):.2%}")
ttm_ae=194.0-(25.761-18.581+17.632)*(1-T)
print(f"TTM all-equity approx {ttm_ae:.1f}; yield on EV {ttm_ae/ev_price:.2%}; with Quail {ttm_ae/(ev_price+625):.2%}")
