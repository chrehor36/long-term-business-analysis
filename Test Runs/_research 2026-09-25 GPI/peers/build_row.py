# Arithmetic only. Every input below is transcribed from the filed 10-K text files in this folder.
# Years: 2021, 2022, 2023, 2024, 2025. Units: USD millions.
Y=[2021,2022,2023,2024,2025]
P={}
P['AN']=dict(name='AutoNation, Inc.', cik=350698,
 src={2021:'FY2023',2022:'FY2023',2023:'FY2025',2024:'FY2025',2025:'FY2025'},
 rev=[25844.0,26985.0,26948.9,26765.4,27631.4],
 cos=[20891.4,21719.7,21817.4,21980.0,22682.9],
 gp =[4952.6,5265.3,5131.5,4785.4,4948.5],
 psr=[3706.6,4100.6,4533.7,4614.6,4835.4],
 psc=[2033.9,2200.3,2394.4,2405.6,2480.3],
 psg=[1672.7,1900.3,2139.3,2209.0,2355.1],
 op =[1902.8,2024.5,1651.9,1305.5,1239.9],
 imp=[0,0,0,12.5,159.0],          # face lines: goodwill + franchise rights impairment
 fp =[25.7,41.4,144.7,218.9,188.8])
P['PAG']=dict(name='Penske Automotive Group, Inc.', cik=1019849,
 src={2021:'FY2023',2022:'FY2023',2023:'FY2025 (recast for PMG)',2024:'FY2025 (recast for PMG)',2025:'FY2025'},
 rev=[25554.7,27814.8,30916.5,31864.8,31808.5],
 cos=[21113.9,22976.0,25769.1,26647.7,26591.5],
 gp =[4440.8,4838.8,5147.4,5217.1,5217.0],
 psr=[2165.6,2426.7,2863.2,3182.8,3377.9],   # retail automotive only, MD&A table
 psc=None,
 psg=[1307.3,1439.4,1679.3,1847.5,1973.8],
 op =[1356.4,1487.8,1409.3,1370.1,1280.7],
 imp=[0,0,40.7,0,0],
 fp =[26.2,52.4,135.3,193.1,170.6])
P['LAD']=dict(name='Lithia Motors, Inc.', cik=1023128,
 src={2021:'FY2023',2022:'FY2023',2023:'FY2025 (reclassified lines)',2024:'FY2025',2025:'FY2025'},
 rev=[22831.7,28187.8,31042.3,36188.2,37634.9],
 cos=[18572.7,23035.4,25813.4,30627.2,31901.9],
 gp =[4259.0,5152.4,5228.9,5561.0,5733.0],
 psr=[2110.9,2738.8,3206.8,3818.9,4086.8],
 psc=[1000.4,1275.8,1447.7,1684.8,1729.7],
 psg=None,
 op =[1662.5,1941.1,1692.4,1568.6,1594.7],
 imp=[1.9,0,0,0,5.8],
 fp =[22.3,38.8,150.9,278.8,228.2])
P['ABG']=dict(name='Asbury Automotive Group, Inc.', cik=1144980,
 src={2021:'FY2023',2022:'FY2023',2023:'FY2025',2024:'FY2025',2025:'FY2025'},
 rev=[9837.7,15433.8,14802.7,17188.6,17999.0],
 cos=[7935.5,12333.3,12046.9,14240.0,14927.3],
 gp =[1902.2,3100.6,2755.8,2948.6,3071.7],
 psr=[1182.9,2074.2,2081.5,2354.7,2506.8],
 psc=[461.0,921.6,931.0,1003.5,1034.3],
 psg=None,
 op =[791.8,1272.6,953.5,835.6,860.6],
 imp=[0,0,117.2,149.5,141.0],
 fp =[8.2,8.4,9.6,89.9,91.2])
P['SAH']=dict(name='Sonic Automotive, Inc.', cik=1043509,
 src={2021:'FY2023',2022:'FY2023',2023:'FY2025',2024:'FY2025',2025:'FY2025'},
 rev=[12396.4,14001.1,14372.4,14224.3,15153.6],
 cos=[10482.1,11684.1,12126.7,12031.5,12770.7],
 gp =[1914.3,2317.0,2245.7,2192.8,2382.9],
 psr=[1340.4,1599.7,1759.5,1846.5,2019.1],
 psc=[667.5,807.2,885.5,917.6,990.0],
 psg=None,
 op =[538.4,314.0,423.6,461.5,367.5],
 imp=[0.1,320.4,79.3,3.9,173.8],
 fp =[16.7,34.3,67.2,86.9,84.7])
# Operating-income re-add checks (2025, face lines)
OPCHK={'AN':('4,948.5 + 9.8 (ANF income) - 3,362.2 - 251.4 - 65.3 - 93.7 + 54.2 (other income, net)',4948.5+9.8-3362.2-251.4-65.3-93.7+54.2),
 'PAG':('5,217.0 - 3,764.0 - 172.3',5217.0-3764.0-172.3),
 'LAD':('5,733.0 + 74.6 (financing ops) - 5.8 - 3,944.7 - 262.4',5733.0+74.6-5.8-3944.7-262.4),
 'ABG':('3,071.7 - 1,987.6 - 82.4 - 141.0',3071.7-1987.6-82.4-141.0),
 'SAH':('2,382.9 - 1,678.2 - 173.8 - 163.4',2382.9-1678.2-173.8-163.4)}
def pct(a,b): return 100*a/b
def mean(v): return sum(v)/len(v)
out={}
for t,d in P.items():
    if d['psg'] is None: d['psg']=[round(r-c,1) for r,c in zip(d['psr'],d['psc'])]
    d['gm']=[pct(g,r) for g,r in zip(d['gp'],d['rev'])]
    d['om']=[pct(o,r) for o,r in zip(d['op'],d['rev'])]
    d['omx']=[pct(o+i,r) for o,i,r in zip(d['op'],d['imp'],d['rev'])]
    d['psm']=[pct(g,r) for g,r in zip(d['psg'],d['psr'])]
    d['gpchk']=[round(r-c,1) for r,c in zip(d['rev'],d['cos'])]
def f1(x): return f'{x:,.1f}'
def f2(x): return f'{x:.2f}'
def table(t):
    d=P[t]; L=[]
    L.append('| Year | Source 10-K | Revenue | Cost of sales | Gross profit | GP check (Rev - COS) | GM % | P&S revenue | P&S gross profit | P&S GM % | Operating income (as filed) | Impairment lines on face | OpM % as filed | OpM % ex-impairment | Floorplan interest |')
    L.append('|'+'---|'*15)
    for i,y in enumerate(Y):
        L.append(f"| {y} | {d['src'][y]} | {f1(d['rev'][i])} | {f1(d['cos'][i])} | {f1(d['gp'][i])} | {f1(d['gpchk'][i])} {'OK' if abs(d['gpchk'][i]-d['gp'][i])<0.15 else 'MISMATCH'} | {f2(d['gm'][i])} | {f1(d['psr'][i])} | {f1(d['psg'][i])} | {f2(d['psm'][i])} | {f1(d['op'][i])} | {f1(d['imp'][i])} | {f2(d['om'][i])} | {f2(d['omx'][i])} | {f1(d['fp'][i])} |")
    L.append(f"| **5-yr mean** | | | | | | **{f2(mean(d['gm']))}** | | | **{f2(mean(d['psm']))}** | | | **{f2(mean(d['om']))}** | **{f2(mean(d['omx']))}** | |")
    s,v=OPCHK[t]; L.append(''); L.append(f"Operating income re-add, 2025: {s} = {v:,.1f} (filed {f1(d['op'][4])}) {'OK' if abs(v-d['op'][4])<0.15 else 'MISMATCH'}.")
    return '\n'.join(L)
def summary(acc):
    L=['| Company | GM% 2021 | 2022 | 2023 | 2024 | 2025 | GM mean | OpM% 2021 | 2022 | 2023 | 2024 | 2025 | OpM mean | OpM ex-impairments mean | P&S GM% mean | Accessions |','|'+'---|'*16]
    for t,d in P.items():
        L.append(f"| {t} | "+' | '.join(f2(x) for x in d['gm'])+f" | {f2(mean(d['gm']))} | "+' | '.join(f2(x) for x in d['om'])+f" | {f2(mean(d['om']))} | {f2(mean(d['omx']))} | {f2(mean(d['psm']))} | {acc[t]} |")
    return '\n'.join(L)
if __name__=='__main__':
    import sys
    for t in P: print(table(t)); print()
