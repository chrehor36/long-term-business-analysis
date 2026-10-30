"""Competitor comparison FY2016-FY2025 from filed figures (see sources in run file)."""
Y = list(range(2016, 2026))
ni = {
 "PCG": [1393,1646,-6851,-7656,-1318,-102,1800,2242,2475,2593],
 "EIX": [1311,565,-423,1284,739,759,612,1197,1284,4457],
 "SDGE":[570,407,669,767,824,819,915,936,891,563],
 "XEL": [1123,1148,1261,1372,1473,1597,1736,1771,1936,2018],
}
# common equity at year end, 2015..2025
eq = {
 "PCG": [16576,17940,19220,12651,5136,21001,20971,22823,25040,28570,30961],
 "EIX": [None,11996,11671,10459,13303,14048,13911,13643,13828,13920,17082],
 "SDGE":[5223,5641,5598,6015,7100,7730,8249,9067,9902,10564,10933],
 "XEL": [10601,11021,11455,12222,13239,14575,15612,16675,17616,19522,23609],
}
for k in ni:
    e = eq[k]; rs=[]
    for i,y in enumerate(Y):
        b, en = e[i], e[i+1]
        avg = en if b is None else (b+en)/2
        rs.append(ni[k][i]/avg)
    cum = sum(ni[k]); avgeq = sum(x for x in e[1:])/10
    neg = sum(1 for x in ni[k] if x<0)
    print(f"{k:5s} ROE by year: " + " ".join(f"{y%100:02d}:{r*100:5.1f}" for y,r in zip(Y,rs)))
    print(f"      cumulative NI {cum:,} / average year-end equity {avgeq:,.0f} = {cum/avgeq/10*100:.1f}%/yr; mean of yearly ROE {sum(rs)/10*100:.1f}%; loss years {neg}")
    if k!="PCG":
        rs2=rs[:]
    print(f"      FY2021-25 mean ROE {sum(rs[5:])/5*100:.1f}%")
