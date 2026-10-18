"""Field returns over the cycle: EBIT (pre-tax income plus net interest; operating income for rivals) against
total assets and against debt plus equity. Figures transcribed from the filed statements (HRI) and companyfacts (rivals)."""
import json
def fy(path, tag):
    d = json.load(open(path)); g = d['facts']['us-gaap'][tag]['units']['USD']; v = {}
    from datetime import date
    for x in g:
        if x.get('form','').startswith('10-K') and x.get('fp') == 'FY':
            if 'start' in x and (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days < 300: continue
            v[int(x['end'][:4])] = x['val'] / 1e6
    return v
# HRI from filed statements (10-K accessions in notes.md): pre-tax income, interest expense net, revenue, total assets, debt incl. financing obligations, equity
HRI = {  # year: (pretax, interest, revenue, assets, debt, equity)
 2016: (-4.9, 84.2, 1554.8, 3463, 2194, 318), 2017: (-64.4, 140.0, 1754.5, 3550, 2160, 510),
 2018: (68.8, 137.0, 1976.7, 3610, 2157, 573), 2019: (63.6, 173.5, 1999.0, 3817, 2078, 644),
 2020: (94.1, 92.6, 1781.3, 3588, 1664, 742), 2021: (290.4, 86.3, 2073.1, 4490, 1928, 977),
 2022: (433.4, 122.0, 2738.8, 5957, 2934, 1109), 2023: (447, 224, 3282, 7061, 3688, 1273),
 2024: (291, 260, 3568, 7877, 4086, 1396), 2025: (1, 416, 4376, 13776, 8047, 1948)}
U = {k: fy('cache/facts_URI.json', k) for k in ['OperatingIncomeLoss','Assets','Revenues','DebtAndCapitalLeaseObligations','StockholdersEquity']}
H = {k: fy('cache/facts_HEES.json', k) for k in ['OperatingIncomeLoss','LiabilitiesAndStockholdersEquity','Revenues','StockholdersEquity']}
print(f"{'yr':5} | {'HRI EBIT':>8} {'/rev':>6} {'/avgTA':>7} {'/avg(D+E)':>9} | {'URI OI':>7} {'/rev':>6} {'/avgTA':>7} {'/avg(D+E)':>9} | {'HEES OI':>7} {'/rev':>6} {'/avgTA':>7}")
for y in range(2017, 2026):
    p, i, r, a, d, e = HRI[y]; pa, pd, pe = HRI[y-1][3], HRI[y-1][4], HRI[y-1][5]
    eb = p + i
    s = f"{y:5} | {eb:8.0f} {eb/r:6.1%} {eb/((a+pa)/2):7.1%} {eb/((d+e+pd+pe)/2):9.1%} | "
    try:
        oi = U['OperatingIncomeLoss'][y]; ta = (U['Assets'][y] + U['Assets'][y-1]) / 2
        de = (U['DebtAndCapitalLeaseObligations'][y] + U['StockholdersEquity'][y] + U['DebtAndCapitalLeaseObligations'][y-1] + U['StockholdersEquity'][y-1]) / 2
        s += f"{oi:7.0f} {oi/U['Revenues'][y]:6.1%} {oi/ta:7.1%} {oi/de:9.1%} | "
    except KeyError as k: s += f"{'n/a':>33} | "
    try:
        oi = H['OperatingIncomeLoss'][y]; ta = (H['LiabilitiesAndStockholdersEquity'][y] + H['LiabilitiesAndStockholdersEquity'][y-1]) / 2
        s += f"{oi:7.0f} {oi/H['Revenues'][y]:6.1%} {oi/ta:7.1%}"
    except KeyError: s += "n/a"
    print(s)
print("URI revenue 2016", U['Revenues'].get(2016), "assets", U['Assets'].get(2016))
