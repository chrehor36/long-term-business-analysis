# competitor comparison 2016-2025 from the peer tables (values in millions, filer's own currency)
# opening equity for the 2016 ROE: TX 2015 owners equity 4,033 (FY2017 20-F selected data); NUE 2015 stockholders equity; MT and GGB 2015 TOTAL equity (owners figure not tagged), so their 2016 ROE is slightly understated
D = {
 'TX (Ternium, USD)': dict(
   rev=[7224,9700,11455,10193,8735,16091,16414,17610,17649,15609],
   pbt=[1118,1360,2032,827,1159,5764,2666,1321,728,648],
   op=[1142,1457,2108,865,1079,5271,2700,2198,1263,705],
   ni=[596,886,1507,564,778,3825,1768,676,-54,425],
   eq=[4391,5010,6393,6612,7286,10535,11846,12419,11968,11944], eq0=4033),
 'NUE (Nucor, USD)': dict(
   rev=[16208,20252,25067,22589,20140,36484,41512,34714,30734,32494],
   pbt=[1299,1750,3229,1783,836,9201,10245,6273,2902,2568], op=None,
   ni=[796,1319,2361,1271,721,6827,7607,4525,2027,1744],
   eq=[7880,8739,9792,10358,10789,14016,18415,20940,20294,20936], eq0=7478),
 'MT (ArcelorMittal, USD)': dict(
   rev=[56791,68679,76033,70615,53270,76571,79844,68275,62441,61352],
   pbt=[2720,5007,4981,-1932,1088,18025,11255,1260,2915,3602],
   op=[4161,5434,6539,-627,2110,16976,10272,2340,3310,3628],
   ni=[1779,4568,5149,-2454,-733,14956,9302,919,1339,3152],
   eq=[30135,38789,42086,38521,38280,49106,53152,53961,49223,54466], eq0=27570),
 'GGB (Gerdau, BRL)': dict(
   rev=[37652,36918,46159,39644,43815,78345,82412,68916,67027,69859],
   pbt=[-2582,-43,2157,1675,3496,20273,15859,9347,5464,2524],
   op=[-1636,1100,4047,3184,5194,21023,17751,10453,7487,3739],
   ni=[-2891,-359,2304,1204,2366,15494,11426,7502,4566,1387],
   eq=[24028,23645,25731,26956,30860,42604,46116,49059,57949,53585], eq0=31970),
}
yrs = list(range(2016, 2026))
for k, v in D.items():
    print(k)
    pm = [p/r*100 for p, r in zip(v['pbt'], v['rev'])]
    print('  pretax margin %  ', ' '.join(f'{x:6.1f}' for x in pm), ' avg', round(sum(pm)/10, 1), ' total', round(sum(v['pbt'])/sum(v['rev'])*100, 1))
    if v['op']:
        om = [p/r*100 for p, r in zip(v['op'], v['rev'])]
        print('  operating margin %', ' '.join(f'{x:6.1f}' for x in om), ' avg', round(sum(om)/10, 1))
    eqs = [v['eq0']] + v['eq']
    roe = [n/((eqs[i]+eqs[i+1])/2)*100 for i, n in enumerate(v['ni'])]
    print('  ROE to owners %  ', ' '.join(f'{x:6.1f}' for x in roe), ' avg', round(sum(roe)/10, 1))
    print('  ROE ex-2021,2022 avg', round((sum(roe)-roe[5]-roe[6])/8, 1), ' 2016-2020 avg', round(sum(roe[:5])/5, 1), ' 2021-2025 avg', round(sum(roe[5:])/5, 1))
