import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
res = json.load(open('cfs_parsed.json'))
ACQ = {1998: -32949, 1999: -12533, 2000: -34522, 2001: -5491, 2002: -2574, 2003: -10255, 2004: -1285, 2005: -5914, 2006: -27672,
       2007: 0, 2008: -22105, 2009: -172199, 2010: -100, 2011: -30504, 2012: -14671, 2013: -67590, 2014: -184324, 2015: -160620}
newest = {}; earliest = {}
for n, r in sorted(res.items(), key=lambda x: x[1]['fdate']):
    for k, v in r['rec'].items():
        if len(v) > 3: v = v[-3:]
        if len(v) != 3: continue
        for y, x in zip(r['years'], v):
            newest.setdefault(y, {})[k] = x
            earliest.setdefault(y, {}).setdefault(k, x)
for y in ACQ:
    newest.setdefault(y, {})['acq'] = ACQ[y]
    earliest.setdefault(y, {}).setdefault('acq', ACQ[y])
json.dump({'newest': newest, 'earliest': earliest}, open('cfs_series.json', 'w'), indent=0)
keys = ['ni','ocf','dep','amort_int','amort_mixed','sbc_opt','sbc_other','sbc_treas','gw_imp','capex','prop_sales','acq','buyback','div','withheld','taxpaid']
print('FY ' + ' '.join(f'{k:>10}' for k in keys))
for y in sorted(newest):
    print(y, ' '.join(f'{newest[y].get(k, ""):>10}' for k in keys))
print('restatements (earliest vs newest, OCF/capex/sbc):')
for y in sorted(newest):
    for k in ('ocf','capex','dep','sbc_opt','sbc_other','sbc_treas'):
        a, b = earliest[y].get(k), newest[y].get(k)
        if a is not None and b is not None and a != b: print(' ', y, k, a, '->', b)
