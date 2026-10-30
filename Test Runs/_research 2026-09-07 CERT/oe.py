import statistics, sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
# All $k, from the FILED consolidated statements of cash flows.
# 2019-2020: FY2021 10-K 0001558370-22-002608 | 2021-2022: FY2022 10-K 0001558370-23-002605
# 2023-2025: FY2025 10-K 0001827090-26-000011
D={
#  yr : (OCF, SBC, dep_ppe, amort_intang_total, capex_ppe, cap_software, acq_cash)
2019:(38025,  1691, 2596, 38964, 2107,  7410,      0),
2020:(44810, 64507, 2443, 40310,  863,  7074,    675),
2021:(60388, 29483, 2135, 42980, 1143,  7759, 261020),
2022:(92543, 30345, 1731, 50739, 1430, 11099,  15308),
2023:(82755, 28300, 1552, 54519, 1777, 13491,  64228),   # 1552+54519=56071 filed D&A
2024:(80466, 34774, 2000, 66033, 1625, 19416,  91327),   # 2000+66033=68033 filed D&A
2025:(96325, 33079, 2200, 72962, 1760, 24796,      0),   # 2200+72962=75162 filed D&A
}
# 2023 also had $54k "Investment in intangible assets"
EXTRA={2023:54}
rows=[]
for y,(ocf,sbc,dep,amint,capex,capsw,acq) in sorted(D.items()):
    da=dep+amint
    tcap=capex+capsw+EXTRA.get(y,0)
    rows.append(dict(y=y,ocf=ocf,sbc=sbc,da=da,tcap=tcap,capex=capex,capsw=capsw,acq=acq,
                     oe_cap=ocf-sbc-tcap, oe_da=ocf-sbc-da,
                     oe_ppe=ocf-sbc-capex))   # the screen's (wrong) narrow end
print(f"{'yr':>5} {'OCF':>8} {'SBC':>8} {'OCF-SBC':>9} {'D&A':>8} {'totcap':>8} | {'OE@cap':>8} {'OE@D&A':>8} | {'OE@PPEonly':>10} {'acq':>9}")
for r in rows:
    print(f"{r['y']:>5} {r['ocf']/1e3:8.1f} {r['sbc']/1e3:8.1f} {(r['ocf']-r['sbc'])/1e3:9.1f} {r['da']/1e3:8.1f} {r['tcap']/1e3:8.1f} | {r['oe_cap']/1e3:8.1f} {r['oe_da']/1e3:8.1f} | {r['oe_ppe']/1e3:10.1f} {r['acq']/1e3:9.1f}")
print()
def mean(ys,k): return statistics.mean(D and [r[k] for r in rows if r['y'] in ys])/1e3
wins=[('3yr 2023-25',range(2023,2026)),('4yr 2022-25',range(2022,2026)),
      ('5yr 2021-25',range(2021,2026)),('6yr 2020-25',range(2020,2026)),
      ('7yr 2019-25',range(2019,2026)),('5yr 2019-23',range(2019,2024))]
print(f"{'window':>14} {'OE@totcap':>10} {'OE@D&A':>10} {'OE@PPEonly':>11}")
allv=[]
for nm,ys in wins:
    ys=set(ys)
    a,b,c=mean(ys,'oe_cap'),mean(ys,'oe_da'),mean(ys,'oe_ppe')
    allv += [a,b]
    print(f"{nm:>14} {a:10.1f} {b:10.1f} {c:11.1f}")
lo,hi=min(allv),max(allv)
print(f"\nTRUE RANGE across 6 windows x 2 (c) ends: {lo:.1f} to {hi:.1f}  = {hi/lo:.2f}x width ({(hi/lo-1)*100:.0f}%)")
print(f"Published screen row: 28 to 35 = {35/28:.2f}x (23.2%)")
CAP=1211.0
print(f"\nYields on cap ${CAP:.0f}M:  bottom {lo/CAP*100:.2f}%   top {hi/CAP*100:.2f}%   sovereign 5.24%")
print(f"5yr window (corpus default [E2-42]): @totcap {mean(set(range(2021,2026)),'oe_cap'):.1f} = {mean(set(range(2021,2026)),'oe_cap')/CAP*100:.2f}%  |  @D&A {mean(set(range(2021,2026)),'oe_da'):.1f} = {mean(set(range(2021,2026)),'oe_da')/CAP*100:.2f}%")
print(f"\nAcquisition cash 2021-25: {sum(r['acq'] for r in rows if r['y']>=2021)/1e3:.1f}M")
