import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
S = json.load(open('cfs_series.json'))['newest']
S = {int(k): v for k, v in S.items()}
CAP = 333.39 * 36698856 / 1e6
# SBC, $K: stock-settled items only, each year from the filed statement (see run file for the construction)
RESTR = {1998: 1586, 1999: 1209, 2000: 1192, 2001: 1146, 2002: 818, 2003: 1491, 2004: 2483}  # restricted-stock amortization (FY2003-04: whole mixed line, conservative)
PROFORMA = {1998: 509, 1999: 815, 2000: 1045, 2001: 1166, 2002: 1321, 2003: 1250}          # incremental fair-value option expense, after tax (APB 25 years)
rows = {}
for y in range(1998, 2027):
    d = S[y]
    treas = d.get('sbc_treas', 0) if y <= 2008 else 0
    other = d.get('sbc_other', 0) if y >= 2009 else 0
    opt = d.get('sbc_opt', 0) if y >= 2005 else 0
    sbc = treas + other + opt + RESTR.get(y, 0) + PROFORMA.get(y, 0)
    ocf = d['ocf']; capex = -d['capex']; dep = d['dep']; am = d.get('amort_int', 0) if y >= 2005 else 0
    acq = -d.get('acq', 0)
    rows[y] = dict(ocf=ocf, sbc=sbc, capex=capex, dep=dep, am=am, acq=acq,
                   oe_capex=ocf - sbc - capex, oe_dep=ocf - sbc - dep, oe_da=ocf - sbc - dep - am,
                   oe_all=ocf - sbc - capex - acq, ni=d['ni'])
json.dump(rows, open('oe_rows.json', 'w'), indent=0)
print('FY    OCF     SBC   capex    dep  amortInt    acq   OEcapex   OEdep   OE_DA   OEall  capex/dep')
for y, r in rows.items():
    print(f"{y} {r['ocf']/1e3:8.1f} {r['sbc']/1e3:6.1f} {r['capex']/1e3:6.1f} {r['dep']/1e3:6.1f} {r['am']/1e3:6.1f} {r['acq']/1e3:7.1f} {r['oe_capex']/1e3:8.1f} {r['oe_dep']/1e3:8.1f} {r['oe_da']/1e3:8.1f} {r['oe_all']/1e3:8.1f}  {r['capex']/r['dep']:.2f}")
print(f'\ncap ${CAP:,.1f}M')
def mean(k, ys): return sum(rows[y][k] for y in ys) / len(ys) / 1e3
print('window        capex_end          dep_end           D&A_end (screen)   all capital (acq counted)')
for n in list(range(1, 11)) + [15, 20, 25, 29]:
    ys = list(range(2027 - n, 2027))
    a, b, c, e = mean('oe_capex', ys), mean('oe_dep', ys), mean('oe_da', ys), mean('oe_all', ys)
    print(f"{n:2d}y {ys[0]}-26  {a:8.1f} ({a/CAP*100:4.2f}%)  {b:8.1f} ({b/CAP*100:4.2f}%)  {c:8.1f} ({c/CAP*100:4.2f}%)  {e:8.1f} ({e/CAP*100:5.2f}%)")
print('\nrolling 5y means, capex end / dep end / all capital:')
for s in range(1998, 2023):
    ys = list(range(s, s + 5))
    print(f"{s}-{s+4}: {mean('oe_capex', ys):7.1f} {mean('oe_dep', ys):7.1f} {mean('oe_all', ys):7.1f}")
tot = {k: sum(rows[y][k] for y in rows) / 1e3 for k in ('ocf', 'sbc', 'capex', 'dep', 'acq', 'ni')}
print('\ntotals FY1998-2026 $M:', {k: round(v, 1) for k, v in tot.items()})
print('SBC / OCF cumulative %.1f%%' % (tot['sbc'] / tot['ocf'] * 100), ' acq / OCF %.1f%%' % (tot['acq'] / tot['ocf'] * 100))
