# Competitor row (Q2): same metrics from each filer's own XBRL (transcription of the filed 10-Ks; accessions in the run file).
import json
def series(path, tag):
    g = json.load(open(path))['facts']['us-gaap']
    u = list(g[tag]['units'].values())[0]; rows = {}
    for f in u:
        if f.get('form') == '10-K' and f['end'][5:] == '12-31' and (not f.get('start') or f['start'][5:] == '01-01'):
            rows.setdefault(int(f['end'][:4]), f['val'] / 1e6)
    return rows
cos = {'CPK': 'cache/cf.json', 'OGS': 'cache/peers/cf_0001587732.json', 'NWN': 'cache/peers/cf_0001733998.json', 'UTL': 'cache/peers/cf_0000755001.json'}
yrs = range(2021, 2026)
for c, p in cos.items():
    ni = series(p, 'NetIncomeLoss'); eq = series(p, 'StockholdersEquity')
    ocf = series(p, 'NetCashProvidedByUsedInOperatingActivities'); cx = series(p, 'PaymentsToAcquirePropertyPlantAndEquipment')
    roe = [ni[y] / ((eq[y] + eq[y - 1]) / 2) * 100 for y in yrs]
    fcf = [ocf[y] - cx[y] for y in yrs]
    print(f"{c}: ROE % " + " ".join(f"{r:5.1f}" for r in roe) + f"  avg {sum(roe)/5:5.1f} | OCF-capex " + " ".join(f"{v:7.1f}" for v in fcf)
          + f" sum {sum(fcf):8.1f} | NI sum {sum(ni[y] for y in yrs):7.1f} | capex/OCF {sum(cx[y] for y in yrs)/sum(ocf[y] for y in yrs):4.2f} | equity x {eq[2025]/eq[2020]:.2f}")
