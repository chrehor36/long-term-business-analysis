"""Cumulative sums of the FILED volume / net selling price / foreign exchange components, by region, 2016-2025.
ARITHMETIC ONLY, no conclusion. Each cell is transcribed from that year's own 10-K MD&A sentence
(resume/q2_org_out.md carries the source sentence for every cell). Two cells that q2_org_out.md left as '?'
are filled here from the filing and flagged: Latin America 2018 (the FY2018 10-K splits the sentence in two:
"Net sales in Latin America decreased 7.5% in 2018 to $3,605 . Volume declines of 2.5% and negative foreign
exchange of 6.5% were partially offset by net selling price increases of 1.5% .") and Africa/Eurasia 2023
(the FY2023 10-K uses "were flat", which the extractor's increased/decreased pattern missed: "Net sales in
Africa/Eurasia were flat in 2023, as volume growth of 4.5% and net selling price increases of 13.0% were offset
by negative foreign exchange of 17.5%."). Asia Pacific 2017 and 2018 price are 0.0 because both sentences say
net selling prices "were flat"; they are NOT missing cells."""
Y = list(range(2016, 2026))
# (volume, price, fx) by year 2016..2025
D = {
 "Worldwide":      [(-3.0,2.5,-4.5),(0.5,0.5,0.5),(1.0,0.5,-1.0),(2.5,2.0,-3.5),(5.5,3.0,-3.5),(1.0,3.5,1.5),(-2.0,9.5,-4.5),(-0.5,10.0,-1.0),(3.1,4.4,-4.1),(-0.4,2.1,-0.3)],
 "North America":  [(2.5,-1.0,-0.5),(0.0,-2.0,0.0),(6.5,1.0,0.0),(2.0,0.5,-0.5),(8.0,1.5,0.0),(-4.0,2.0,1.0),(-2.0,5.5,0.0),(-4.5,7.5,0.0),(2.6,-1.9,-0.1),(-1.4,-0.2,-0.1)],
 "Latin America":  [(-14.0,8.5,-10.0),(2.5,3.0,1.0),(-2.5,1.5,-6.5),(3.0,4.0,-7.0),(0.5,8.5,-14.0),(1.0,7.0,-1.0),(-5.0,15.5,-2.0),(2.5,13.0,1.0),(3.9,12.9,-13.7),(0.9,2.9,-4.0)],
 "Europe":         [(2.5,-2.5,-3.0),(2.0,-1.0,1.0),(2.5,-2.0,4.0),(4.0,-0.5,-5.5),(11.0,-0.5,1.5),(-0.5,0.0,4.0),(-4.0,4.0,-10.5),(-4.5,9.5,2.5),(4.1,2.5,1.1),(1.1,1.5,4.4)],
 "Asia Pacific":   [(-1.0,0.0,-4.0),(-0.5,0.0,0.0),(-1.5,0.0,0.0),(0.5,1.0,-2.5),(-1.5,2.0,-1.0),(3.0,0.0,3.0),(-0.5,5.5,-6.5),(-3.5,6.0,-4.0),(3.1,1.0,-1.3),(-2.7,1.7,-0.5)],
 "Africa/Eurasia": [(-4.0,9.5,-9.5),(-4.5,3.5,3.5),(-1.0,3.5,-4.0),(3.5,4.0,-6.0),(5.0,3.5,-8.5),(1.0,6.0,-0.5),(-9.5,21.5,-8.5),(4.5,13.0,-17.5),(7.6,5.7,-12.1),(0.5,6.0,0.5)],
 "Hill's":         [(0.0,2.5,0.0),(-1.0,1.5,0.5),(1.5,2.0,0.5),(3.5,4.0,-1.5),(10.5,4.0,-0.5),(8.0,5.5,1.5),(4.0,11.5,-3.5),(5.0,11.0,-0.5),(0.8,4.1,-0.4),(-0.6,3.0,0.5)],
 "OPHC":           [(-4.0,2.5,-5.0),(0.5,0.5,1.0),(1.0,0.5,-1.5),(2.5,1.5,-4.0),(4.5,3.5,-5.0),(0.0,2.5,1.5),(-3.5,9.0,-4.5),(-1.5,9.5,-1.5),(3.7,4.4,-5.2),(-0.3,1.8,-0.5)],
}
print("| scope | sum volume 2016-2025 | sum net selling price | sum FX | price + FX | sum volume 2021-2025 | sum price 2021-2025 |")
print("|---|---|---|---|---|---|---|")
for k, rows in D.items():
    v = sum(r[0] for r in rows); p = sum(r[1] for r in rows); f = sum(r[2] for r in rows)
    v5 = sum(r[0] for r in rows[-5:]); p5 = sum(r[1] for r in rows[-5:])
    print(f"| {k} | {v:+.1f} | {p:+.1f} | {f:+.1f} | {p+f:+.1f} | {v5:+.1f} | {p5:+.1f} |")
