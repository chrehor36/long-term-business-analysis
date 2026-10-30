# filed unit series (10-K key metrics tables; 424B4 for 2019-2020; 10-Qs for H1)
units={2019:241477,2020:391466,2021:560959,2022:546088,2023:598767,2024:743008,2025:829276,"H1-25":418454,"H1-26":424964,"Q2-25":210429,"Q2-26":211472}
gmv={2019:1.8e9,2020:3.3e9,2021:7.9e9,2022:9.0e9,2023:8.8e9,2024:9.5e9,2025:10.4e9,"H1-25":5.3e9,"H1-26":5.4e9,"Q2-25":2.7e9,"Q2-26":2.7e9}
auction={2019:49216,2020:99205,2021:164215,2022:175721,2023:210930,2024:303037,2025:347642,"H1-25":182250,"H1-26":186178,"Q2-25":92267,"Q2-26":92401}
other={2019:None,2020:None,2021:121020,2022:152959,2023:179002,2024:236672,2025:295804,"H1-25":143074,"H1-26":168657,"Q2-25":75397,"Q2-26":88306}
tde={2019:38534,2020:73915,2021:144135}
data={2021:23115,2022:32905,2023:32595,2024:33262,2025:34518,"H1-25":16608,"H1-26":16622}
rev={2019:106847,2020:208357,2021:358435,2022:421529,2023:481234,2024:637156,2025:759606,"H1-25":376400,"H1-26":418133,"Q2-25":193703,"Q2-26":213941}
prev=None
for k in units:
    u=units[k]; a=auction[k]*1000
    print(k, f"units {u:,}", f"yoy {u/units[prev]-1:+.1%}" if isinstance(k,int) and prev else "", f"GMV/unit ${gmv[k]/u:,.0f}", f"auction rev/unit ${a/u:,.0f}", f"auction take {a/gmv[k]:.2%}", f"total rev/unit ${rev[k]*1000/u:,.0f}")
    if isinstance(k,int): prev=k
print("H1 units yoy", units["H1-26"]/units["H1-25"]-1, "Q2", units["Q2-26"]/units["Q2-25"]-1)
print("H1 auc/unit", auction["H1-26"]*1000/units["H1-26"], auction["H1-25"]*1000/units["H1-25"])
print("Q2 auc/unit", auction["Q2-26"]*1000/units["Q2-26"], auction["Q2-25"]*1000/units["Q2-25"])
print("2019->2025 units x", units[2025]/units[2019], "auc/unit x", (auction[2025]/units[2025])/(auction[2019]/units[2019]), "auction rev x", auction[2025]/auction[2019])
print("2023->2025 units", units[2025]/units[2023]-1, "auc/unit", (auction[2025]/units[2025])/(auction[2023]/units[2023])-1)
import math
# decomposition of auction revenue growth 2019->2025 into units and price (log shares)
lu=math.log(units[2025]/units[2019]); lp=math.log((auction[2025]/units[2025])/(auction[2019]/units[2019]))
print("log share units", lu/(lu+lp), "price", lp/(lu+lp))
lu=math.log(units[2025]/units[2023]); lp=math.log((auction[2025]/units[2025])/(auction[2023]/units[2023]))
print("2023-25 log share units", lu/(lu+lp), "price", lp/(lu+lp))
# FY2025 per-unit economics
u=829276
for name,r,c in [("auction",347642,68300),("other mkt (transport+finance)",295804,206900),("data",34518,12900),("assurance",81642,73288)]:
    print(name, f"rev/unit ${r*1000/u:,.0f}", f"cost/unit ${c*1000/u:,.0f}", f"margin ${ (r-c)*1000/u:,.0f}", f"{(r-c)/r:.1%}")
