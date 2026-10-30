# All figures hand-transcribed from the filed Consolidated Statements of Cash Flows ($M).
# FY2016 10-K 0001628280-17-001442 (2014-16, thousands rounded); FY2019 10-K 0001628280-20-001541 (2017-19);
# FY2022 10-K 0001628280-23-004043 (2020-22, CONTINUING operations after TAP); FY2025 10-K 0001628280-26-008033 (2023-25).
# cols: yr, OCF, excess_tax_benefit_reclass(2014-16 only), SBC(filer's own "Noncash compensation" line,
#        max with note-sum SBC+ESOP for 2023-25), D&A, capex, other_capex(2024 developed tech), JV_dist, JV_inv, WC_total
rows = [
 (2014, 529.3, 37.0, 63.2, 127.5, 205.1, 0.0, 31.3, 32.6),
 (2015, 440.2, 34.7, 61.9, 152.1, 249.5, 0.0, 42.5, 23.1),
 (2016, 571.8,  3.6, 57.9, 167.5, 209.1, 0.0, 43.8,  8.6),
 (2017, 585.4,  0.0, 50.1, 191.1, 184.4, 0.0, 57.5, 25.2),
 (2018, 477.1,  0.0, 64.0, 211.0, 225.4, 0.0, 39.1, 12.3),
 (2019, 655.0,  0.0, 75.0, 234.5, 251.4, 0.0, 30.8, 17.0),
 (2020, 961.8,  0.0, 65.3, 235.8, 204.3, 0.0,100.4, 30.6),
 (2021, 286.8,  0.0, 60.6, 216.4, 282.8, 0.0, 60.0, 42.2),
 (2022, 534.5,  0.0, 62.9, 232.8, 306.6, 0.0, 30.6, 59.3),
 (2023, 925.8,  0.0, 59.5, 258.9, 412.6, 0.0, 37.0, 43.5),
 (2024, 268.2,  0.0, 49.2, 286.3, 261.7,62.7, 68.2, 10.0),
 (2025, 741.0,  0.0, 64.4, 286.5, 182.9, 0.0, 61.5, 14.2),
]
# working-capital lines (sum of "Changes in operating assets and liabilities") per filed statement
wc = {2014:-15.6,2015:-155.6,2016:179.7,2017:96.4,2018:-142.2,2019:58.5,2020:319.5,2021:-536.2,2022:-300.1,2023:235.9,2024:-67.6,2025:552.4}
out={}
print(f"{'yr':>5}{'OCF':>8}{'+xtb':>6}{'-SBC':>7}{'+JVnet':>8}{'base':>8}{'D&A':>7}{'capex':>8}{'OE_DA':>8}{'OE_cap':>8}{'WC':>8}{'OE_cap_exWC':>12}")
for yr,ocf,xtb,sbc,da,cap,ocap,jd,ji in rows:
    base=ocf+xtb-sbc+(jd-ji)
    oe_da=base-da; oe_cap=base-cap-ocap
    out[yr]=(oe_da,oe_cap,base)
    print(f"{yr:>5}{ocf:>8.1f}{xtb:>6.1f}{sbc:>7.1f}{jd-ji:>8.1f}{base:>8.1f}{da:>7.1f}{cap+ocap:>8.1f}{oe_da:>8.1f}{oe_cap:>8.1f}{wc[yr]:>8.1f}{oe_cap-wc[yr]:>12.1f}")
def m(ys,i): return sum(out[y][i] for y in ys)/len(ys)
print()
for lab,ys in [("12y 2014-25",range(2014,2026)),("10y 2016-25",range(2016,2026)),("5y 2021-25",range(2021,2026)),
               ("5y 2016-20",range(2016,2021)),("5y 2019-23",range(2019,2024)),("6y post-TAP 2020-25",range(2020,2026)),("3y 2023-25",range(2023,2026))]:
    ys=list(ys)
    print(f"{lab:>22}  D&A-end {m(ys,0):8.1f}   capex-end {m(ys,1):8.1f}   WC mean {sum(wc[y] for y in ys)/len(ys):7.1f}")
import statistics as st
print("mean D&A %.1f  mean capex(incl 2024 tech) %.1f ratio %.2f"%(st.mean(r[4] for r in rows),st.mean(r[5]+r[6] for r in rows),st.mean(r[5]+r[6] for r in rows)/st.mean(r[4] for r in rows)))
print("capex>D&A years:",sum(1 for r in rows if r[5]+r[6]>r[4]))
# TTM to 2026-06-30
ocf=741.0-403.5-90.0; cap=182.9-76.1+73.8; sbc=59.9-32.8+34.9; jv=(61.5-14.2)-16.4+20.1
print("TTM 2026-06-30: OCF %.1f capex %.1f SBC %.1f JVnet %.1f -> OE_cap %.1f  OE_DA(D&A %.1f) %.1f"%(ocf,cap,sbc,jv,ocf-sbc+jv-cap,286.5-146.3+128.5,ocf-sbc+jv-(286.5-146.3+128.5)))
print()
# judged (c): 12-year mean capex incl. 2024 developed-technology purchase
c=st.mean(r[5]+r[6] for r in rows)
for lab,ys in [("12y",range(2014,2026)),("10y",range(2016,2026)),("5y 2021-25",range(2021,2026)),("5y 2016-20",range(2016,2021)),("post-TAP 2020-25",range(2020,2026)),("3y 2023-25",range(2023,2026))]:
    ys=list(ys); b=st.mean(out[y][2] for y in ys)
    print(f"{lab:>18} base mean {b:7.1f}  OE at judged (c) {c:.1f}: {b-c:7.1f}")
ip={2014:11.3,2015:11.5,2016:15.8,2017:30.9,2018:51.0,2019:77.0,2020:67.0,2021:44.8,2022:71.2,2023:120.6,2024:141.5,2025:125.5}
print("mean interest paid 12y %.1f, 10y %.1f, 5y %.1f; 2025 %.1f"%(st.mean(ip.values()),st.mean(ip[y] for y in range(2016,2026)),st.mean(ip[y] for y in range(2021,2026)),ip[2025]))
