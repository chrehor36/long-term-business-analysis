"""PG owner earnings from the FILED cash-flow statements (each year from the first 10-K that reports it: FY2011 Ex.13 for 2009-11,
FY2014 for 2012-14, FY2017 for 2015-17, FY2020 for 2018-20, FY2023 for 2021-23, FY2026 for 2024-26; transcription in cfs_out.txt).
OE = OCF - SBC - (c); (c) at two ends: D&A (the [E3-44] default) and total capex. ARITHMETIC ONLY, NO CONCLUSION.
'onetime' = the company's own adjusted-FCF exclusions (divestiture tax 2015/2017; 2017 Tax Act transition tax 2019-2026), read from
the FY2017, FY2018, FY2020-FY2026 10-K reconciliations. Shown as a sensitivity, never substituted."""
from statistics import mean
D={2009:(14919,3082,516,3238),2010:(16072,3108,453,3067),2011:(13231,2838,414,3306),2012:(13284,3204,377,3964),
2013:(14873,2982,346,4008),2014:(13958,3141,360,3848),2015:(14608,3134,337,3736),2016:(15435,3078,335,3314),
2017:(12753,2820,351,3384),2018:(14867,2834,395,3717),2019:(15242,2824,515,3347),2020:(17403,3013,558,3073),
2021:(18371,2735,540,2787),2022:(16723,2807,528,3156),2023:(16848,2714,545,3062),2024:(19846,2896,562,3322),
2025:(17817,2847,476,3773),2026:(19556,3160,524,4409)}
one={2015:729,2017:418,2019:235,2020:543,2021:225,2022:225,2023:225,2024:422,2025:562,2026:688}
CAP_AS=2391.1*145.68; CAP_COM=2324.433*145.68
out=["| FY | OCF | SBC | D&A | capex | capex/D&A | OE, (c)=D&A | OE, (c)=capex | one-off tax in OCF |","|---|---|---|---|---|---|---|---|---|"]
for y,(o,da,s,c) in D.items():
    out.append(f"| {y} | {o:,} | {s} | {da:,} | {c:,} | {c/da:.2f} | {o-s-da:,} | {o-s-c:,} | {one.get(y,0)} |")
out.append("")
W={'3y FY24-26':range(2024,2027),'5y FY22-26':range(2022,2027),'10y FY17-26':range(2017,2027),'18y FY09-26':range(2009,2027),'5y prior FY17-21':range(2017,2022)}
out.append("| window | OE (c)=capex | OE (c)=D&A | yield on $348.3bn (capex / D&A end) | with one-off taxes added back (capex / D&A) |")
out.append("|---|---|---|---|---|")
for k,r in W.items():
    lo=mean(D[y][0]-D[y][2]-D[y][3] for y in r); hi=mean(D[y][0]-D[y][2]-D[y][1] for y in r); a=mean(one.get(y,0) for y in r)
    out.append(f"| {k} | {lo:,.0f} | {hi:,.0f} | {lo/CAP_AS*100:.2f}% / {hi/CAP_AS*100:.2f}% | {lo+a:,.0f} / {hi+a:,.0f} |")
out.append(f"\ncap as-converted {CAP_AS:,.0f}M, common only {CAP_COM:,.0f}M")
n=sum(1 for y,(o,da,s,c) in D.items() if c>da); out.append(f"capex > D&A in {n} of {len(D)} years")
for k,r in W.items():
    out.append(f"{k}: mean capex/D&A {mean(D[y][3]/D[y][1] for y in r):.2f}; SBC/OCF {mean(D[y][2]/D[y][0] for y in r)*100:.1f}%")
# buyback-price yields
for fy,px in [(2024,157.29),(2025,169.04),(2026,150.40)]:
    r=range(fy-4,fy+1); lo=mean(D[y][0]-D[y][2]-D[y][3] for y in r); hi=mean(D[y][0]-D[y][2]-D[y][1] for y in r)
    cap=2391.1*px  # share count approximated by today's as-converted count
    out.append(f"buyback FY{fy} avg ${px}: trailing 5y OE {lo:,.0f}-{hi:,.0f} -> yield {lo/cap*100:.2f}%-{hi/cap*100:.2f}% (today's share count)")
open('oe_out.md','w').write('\n'.join(out)); print('\n'.join(out))
