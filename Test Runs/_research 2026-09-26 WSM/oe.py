# Owner earnings, the corpus's way [E2-23]: operating cash flow as filed, less stock compensation, less (c).
# Each year from the LATEST filed 10-K statement that shows it. No net-income proxy anywhere.
import json
cf = {int(k): v for k, v in json.load(open('cf_parsed.json')).items()}
wc = {int(k): v for k, v in json.load(open('wc_parsed.json')).items()}
CAP = 231.90 * 117779173 / 1e6
SOV = 5.49
def latest(field, y):
    for src in (y + 2, y + 1, y):
        if src in cf and cf[src].get(field):
            return cf[src][field][src - y] / 1e3, src
    return None, None
def latest_wc(y):
    for src in (y + 2, y + 1, y):
        if src in wc:
            return wc[src][src - y] / 1e3
    return None
rows = {}
for y in range(2006, 2026):
    ocf, s1 = latest('ocf', y); sbc, s2 = latest('sbc', y); da, s3 = latest('da', y); cx, s4 = latest('capex', y)
    cx = -cx
    w = latest_wc(y)
    rows[y] = dict(ocf=ocf, sbc=sbc, da=da, capex=cx, wc=w, oe_da=ocf - sbc - da, oe_cx=ocf - sbc - cx,
                   oe_cx_nowc=(ocf - w - sbc - cx) if w is not None else None, src=s1)
print('FY    OCF      SBC    D&A    capex   WC lines  OE D&A end  OE capex end  OE capex, WC stripped   (source 10-K FY)')
for y, r in rows.items():
    wcs = f"{r['wc']:+8.1f}" if r['wc'] is not None else '     n/a'
    nw = f"{r['oe_cx_nowc']:10.1f}" if r['oe_cx_nowc'] is not None else '       n/a'
    print(f"{y} {r['ocf']:8.1f} {r['sbc']:6.1f} {r['da']:6.1f} {r['capex']:7.1f} {wcs} {r['oe_da']:10.1f} {r['oe_cx']:12.1f} {nw}   ({r['src']})")
# TTM to 2026-08-02: FY2025 + H1 FY2026 - H1 FY2025 (10-Q 0000719955-26-000208)
h = dict(ocf=(695.862, 401.678), sbc=(61.530, 46.974), da=(112.683, 113.165), capex=(116.434, 110.293))
ttm = {k: rows[2025][k] + a - b for k, (a, b) in h.items()}
print('TTM', {k: round(v, 1) for k, v in ttm.items()}, 'OE D&A', round(ttm['ocf'] - ttm['sbc'] - ttm['da'], 1),
      'OE capex', round(ttm['ocf'] - ttm['sbc'] - ttm['capex'], 1), '| less $200.2M tariff refunds collected:',
      round(ttm['ocf'] - 200.2 - ttm['sbc'] - ttm['capex'], 1))
print(f'\nCAP {CAP:,.1f}  SOV {SOV}%')
print('window        capex end   D&A end   yield capex  yield D&A   capex end WC stripped   capex/D&A')
out = []
for n in range(3, 21):
    ys = list(range(2026 - n, 2026))
    cx = sum(rows[y]['oe_cx'] for y in ys) / n; da = sum(rows[y]['oe_da'] for y in ys) / n
    nw = [rows[y]['oe_cx_nowc'] for y in ys]
    nwm = sum(nw) / n if None not in nw else None
    ratio = sum(rows[y]['capex'] for y in ys) / sum(rows[y]['da'] for y in ys)
    out.append((n, ys[0], cx, da))
    print(f"{n:2d}y FY{ys[0]}-25  {cx:9.1f} {da:9.1f}   {100*cx/CAP:6.2f}%    {100*da/CAP:6.2f}%     {'' if nwm is None else f'{nwm:9.1f}':>12}          {ratio:.2f}")
lo = min(min(a[2], a[3]) for a in out); hi = max(max(a[2], a[3]) for a in out)
print(f'\ncombined range every window 3-20y, both ends: {lo:,.1f} to {hi:,.1f}  ({100*lo/CAP:.2f}% to {100*hi/CAP:.2f}%)')
json.dump({str(k): v for k, v in rows.items()}, open('oe_rows.json', 'w'), indent=0)
