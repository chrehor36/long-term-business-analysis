# Owner cash for ENN Energy (2688.HK), RMB million, from the consolidated statements of cash flows
# in the annual reports (FY2025 AR for 2025/2024, FY2023 AR for 2023/2022, FY2021 AR for 2021/2020,
# FY2019 AR for 2019/2018, FY2017 AR for 2017/2016). Every input is a line of a filed statement.
# Definitions are the run's (see run file, Q4): all-equity owner cash is before interest paid and
# interest received, after tax paid, less the 25% PRC statutory tax shield on interest paid.
D = {
2025: dict(ocf=10433, capex=6718+333+37+4, disp=205+33, divjv=227+215, divfin=140+8, deriv=404-83,
           lease=187, nci=798-187+51, award=0, intp=626, intr=123,
           acq=(224-3-1-3-90-48-429+0+61+59+4-0), buyback=0, divsh=3059, rev=111905, dep=3486),
2024: dict(ocf=10294, capex=6177+509+48, disp=212+30, divjv=207+202, divfin=128+10, deriv=315-56,
           lease=171, nci=709-122, award=665, intp=823, intr=234,
           acq=(-6-70-10-23-15+1+28+111+70-15), buyback=0, divsh=3015, rev=109853, dep=3106),
2023: dict(ocf=9612, capex=6495+274+218, disp=201+66, divjv=243+119, divfin=187+7, deriv=2549-1577,
           lease=140, nci=879-70+7, award=229, intp=891, intr=189,
           acq=(-5+84-5-6-11-1+63+394+36-12), buyback=0, divsh=2977, rev=113858, dep=2233+212+395),
2022: dict(ocf=10102, capex=6241+495+172+5, disp=384+31, divjv=207+170, divfin=75+4, deriv=6469-5905-68,
           lease=96, nci=665-90+18, award=0, intp=814, intr=192,
           acq=(81-80-16-32-6+10+510+7+25-147), buyback=0, divsh=2657, rev=110051, dep=2081+167+355),
2021: dict(ocf=10466, capex=6253+37+102+6, disp=155+28, divjv=232+251, divfin=214+6, deriv=1558-1516-10,
           lease=98, nci=747-51+13, award=0, intp=686, intr=200,
           acq=(726-19-24-31-279-297+40+59+155+319), buyback=0, divsh=2827, rev=93113, dep=1783+156+324),
2020: dict(ocf=9696, capex=5515+61+80+13, disp=179+31, divjv=405+208, divfin=56+1, deriv=143-133-7,
           lease=107, nci=589-97, award=17, intp=756, intr=204,
           acq=(636-246-36-28-12+23+211+225+154-6), buyback=0, divsh=1719, rev=71617, dep=1603+174+304),
2019: dict(ocf=11690, capex=7146+39+197+18+126, disp=234+119, divjv=404+103, divfin=139+7, deriv=390-19,
           lease=101, nci=559-142, award=151, intp=806, intr=200,
           acq=(1175+100-42-17-26+12+14+74+109), buyback=0, divsh=1176, rev=70183, dep=1377+169+238),
2018: dict(ocf=8294, capex=5918+73+123+92+46, disp=93+39, divjv=463+100, divfin=352+2, deriv=-122+106,
           lease=0, nci=537-234, award=0, intp=748, intr=162,
           acq=(488-43-79-5-61+527+10+182+53+1121), buyback=78, divsh=952, rev=60698, dep=1144+142+43),
2017: dict(ocf=6093, capex=4527+88+11+19+74, disp=8+50, divjv=545+43, divfin=148, deriv=-55,
           lease=0, nci=668-79, award=0, intp=562, intr=222,
           acq=(91-8-11+52+27+186+94), buyback=0, divsh=775, rev=48269, dep=1016+102+38),
2016: dict(ocf=5366, capex=3049+106+32+77+25, disp=727+23, divjv=769+33, divfin=180, deriv=0,
           lease=0, nci=523-56, award=0, intp=668, intr=124,
           acq=(49-12-34+711+53+165+134+85), buyback=29, divsh=705, rev=34103, dep=969+95+36),
}
T = 0.25
out = {}
for y in sorted(D):
    d = D[y]
    pre = d['ocf'] - d['capex'] + d['disp'] + d['divjv'] + d['divfin'] + d['deriv'] - d['lease'] - d['nci'] - d['award']
    ae = pre - T * d['intp']                     # all-equity owner cash, before purchases of businesses
    ae_acq = ae - d['acq']                       # after net purchases of businesses and investees
    eq = pre - d['intp'] + d['intr']             # equity-only, before purchases
    eq_acq = eq - d['acq']
    maint = pre - T * d['intp'] + d['capex'] - d['dep']   # maintenance case: capex replaced by D&A
    out[y] = dict(ae=ae, ae_acq=ae_acq, eq=eq, eq_acq=eq_acq, maint=maint, maint_acq=maint - d['acq'])
    print(f"{y}: OCF {d['ocf']:>6} capex {d['capex']:>6} D&A {d['dep']:>5} acq {d['acq']:>6} | AE {ae:>7.0f} AE-acq {ae_acq:>7.0f} | EQ {eq:>7.0f} EQ-acq {eq_acq:>7.0f} | maint {maint:>7.0f} maint-acq {maint-d['acq']:>7.0f} | rev {d['rev']}")
def avg(k, ys): return sum(out[y][k] for y in ys) / len(ys)
W = [2021, 2022, 2023, 2024, 2025]; W0 = [2016, 2017, 2018, 2019, 2020]
for k in ['ae', 'ae_acq', 'eq', 'eq_acq', 'maint', 'maint_acq']:
    a = avg(k, W); b = avg(k, W0)
    print(f"{k:10s} 5yr avg 2021-25 {a:8.0f}   2016-20 {b:8.0f}   halves 2021-23 {avg(k,[2021,2022,2023]):8.0f} 2023-25 {avg(k,[2023,2024,2025]):8.0f}")
import json
json.dump({str(y): v for y, v in out.items()}, open(__file__.replace('owner_cash.py', 'owner_cash_out.json'), 'w'), indent=1)
