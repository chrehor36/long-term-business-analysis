# INTC owner earnings by hand, from the filed cash-flow statements.
# OE = OCF - SBC - (c).  Both ends of the capex band shown.
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# FY: OCF, SBC, capex_investing, capex_financing, govt_incentives, depreciation
D = {
2016: (21808, 1444,  9625,    0,    0,  6266),
2017: (22110, 1358, 11778,    0,    0,  6752),
2018: (29432, 1546, 15181,    0,    0,  7520),
2019: (33145, 1705, 16213,    0,    0,  9204),
2020: (35864, 1854, 14259,    0,    0, 10482),
2021: (29456, 2036, 18733,    0,  166,  9953),
2022: (15433, 3128, 24844,    0,  246, 11128),
2023: (11471, 3229, 25750,    0, 1011,  7847),
2024: ( 8288, 3410, 23944, 1178, 1936,  9951),
2025: ( 9697, 2434, 14646, 3026, 1577, 10757),
}
# TTM = H2-2025 (FY2025 less H1-2025) + H1-2026, all from the filed statements
h1_25 = dict(ocf=2863, sbc=1348, cxi=8733, cxf=1962, gov=964,  dep=5213)
h1_26 = dict(ocf=8102, sbc=1307, cxi=6192, cxf=1423, gov=167,  dep=5891)
fy25  = dict(ocf=9697, sbc=2434, cxi=14646, cxf=3026, gov=1577, dep=10757)
ttm = {k: fy25[k]-h1_25[k]+h1_26[k] for k in fy25}
D[9999] = (ttm['ocf'], ttm['sbc'], ttm['cxi'], ttm['cxf'], ttm['gov'], ttm['dep'])

print('TTM components (H2-2025 + H1-2026):', ttm)
print()
hdr = f"{'FY':>6} {'OCF':>8} {'SBC':>6} {'capex tot':>10} {'gov':>6} {'depr':>8} {'OE capex':>9} {'OE net-gov':>10} {'OE D&A':>9} {'cx/dep':>7}"
print(hdr); print('-'*len(hdr))
rows = {}
for y,(ocf,sbc,cxi,cxf,gov,dep) in D.items():
    cx = cxi+cxf
    oe_cx  = ocf - sbc - cx
    oe_net = ocf - sbc - (cx-gov)
    oe_da  = ocf - sbc - dep
    rows[y] = (oe_cx, oe_net, oe_da)
    lbl = 'TTM' if y==9999 else str(y)
    print(f"{lbl:>6} {ocf:8,} {sbc:6,} {cx:10,} {gov:6,} {dep:8,} {oe_cx:9,} {oe_net:10,} {oe_da:9,} {cx/dep:7.2f}")

print()
SH = 5115.0            # economic count, millions
PX = 95.80
CAP = SH*PX
print(f"economic share count {SH:,.0f}M x ${PX} = CAP ${CAP:,.0f}M")
print()
def mean(ys, idx):
    return sum(rows[y][idx] for y in ys)/len(ys)

windows = {
 '3-yr FY2023-25' : [2023,2024,2025],
 '5-yr FY2021-25 (corpus default [E2-42])': [2021,2022,2023,2024,2025],
 '7-yr FY2019-25' : list(range(2019,2026)),
 '10-yr FY2016-25': list(range(2016,2026)),
 'TTM (H2-25+H1-26)': [9999],
 'pre-collapse 5-yr FY2016-20 (the old business)': list(range(2016,2021)),
}
print(f"{'window':<48} {'OE capex':>10} {'yield%':>8} {'OE net-gov':>11} {'yield%':>8} {'OE D&A':>10} {'yield%':>8}")
print('-'*110)
for k,ys in windows.items():
    a,b,c = mean(ys,0), mean(ys,1), mean(ys,2)
    print(f"{k:<48} {a:10,.0f} {a/CAP*100:8.2f} {b:11,.0f} {b/CAP*100:8.2f} {c:10,.0f} {c/CAP*100:8.2f}")

print()
print('=== SCREEN ROW REPRODUCTION: tail triage says INTC band = -14,652 to +2,201 ===')
for lbl,ys in [('3y',[2023,2024,2025]),('4y',[2022,2023,2024,2025]),('5y',[2021,2022,2023,2024,2025])]:
    # screen would use only the INVESTING capex tag and the Depreciation tag
    scx = sum((D[y][0]-D[y][1]-D[y][2]) for y in ys)/len(ys)
    sda = sum((D[y][0]-D[y][1]-D[y][5]) for y in ys)/len(ys)
    print(f"  {lbl}: investing-capex-only end {scx:10,.0f}   depreciation end {sda:10,.0f}")

print()
print('=== incremental return on capital deployed, 5 years FY2021-25 [E2-56] ===')
cap5 = sum(D[y][2]+D[y][3] for y in range(2021,2026))
print(f"  total capex FY2021-25: {cap5:,}M")
print(f"  operating income FY2020 {23678:,}M -> FY2025 {-2214:,}M ; delta {-2214-23678:,}M")
print(f"  operating income FY2021 {19456:,}M -> FY2025 {-2214:,}M ; delta {-2214-19456:,}M")
print(f"  gross profit FY2020 {43612:,} -> FY2025 {18375:,} ; delta {18375-43612:,}")
print()
print('=== [E2-54] coverage: OCF net of capex vs interest ===')
for y in [2021,2022,2023,2024,2025,9999]:
    ocf,sbc,cxi,cxf,gov,dep = D[y]
    intr = {2021:545,2022:459,2023:613,2024:987,2025:1106,9999:1048}[y]
    print(f"  {('TTM' if y==9999 else y)}: OCF {ocf:,} - capex {cxi+cxf:,} = {ocf-cxi-cxf:,}  vs interest paid {intr:,}  -> {'NEGATIVE' if ocf-cxi-cxf<0 else f'{(ocf-cxi-cxf)/intr:.2f}x'}")
