p='q4_draft.md'; t=open(p,encoding='utf-8').read()
reps=[("| three-year, FY2023-25 | 2,767 | about $1.0bn | about $0.1bn | $2.61bn | $1.03bn |","| three-year, FY2023-25 | 2,787 | about $1.1bn | about zero | $2.61bn | $1.03bn |"),
("| ten-year, FY2016-25 | about 1,990 | about $0.6bn | negative | $1.80bn | $0.62bn |","| ten-year, FY2016-25 | about 2,000 | about $0.7bn | slightly negative (about -$0.1bn) | $1.80bn | $0.62bn |"),
("| TTM to 2026-06-30 | 3,187 | about $1.3bn | about $0.2bn | $2.97bn | $1.23bn |","| TTM to 2026-06-30 | 3,187 | about $1.2bn | about $0.05bn | $2.97bn | $1.23bn |"),
("""Owner earnings per diluted share at the central (c): about
**$10.6 (FY2021 five-year mean on 90.4M shares)** against **$13.5 (FY2025, $1.32bn on 98.1M)**; at
the displayed D&A end $5.83 (FY2021) to $13.73 (FY2025). Diluted shares rose **67.7% FY2015-25**
and **11.0% FY2020-25**, so a dollar of growth in the total is worth about nine-tenths of a dollar
per share over the last five years.""","""Owner earnings per diluted share with (c) at
depreciation excluding intangibles (the central level): about **$6.3 (FY2021, $567M on 90.4M
shares)** to **$13.5 (FY2025, $1,323M on 98.1M)**; at the displayed D&A end $5.83 to $13.73.
Diluted shares rose **67.7% FY2015-25** and **11.0% FY2020-25**, so per-share growth runs about a
tenth below total growth over the last five years."""),
("""business runs on other people's money it must keep rolling: $11.1bn of equity and a net $10bn+ of
  debt raised FY2015-25 to fund plant, dividends and acquisitions)""","""business runs on other people's money it must keep rolling: $11.1bn of equity raised FY2015-25
  and senior notes outstanding grown to $18.4bn at FY2025, funding plant, dividends and
  acquisitions)"""),
]
for a,b in reps:
    assert a in t, a[:60]
    t=t.replace(a,b)
open(p,'w',encoding='utf-8').write(t); print("ok")
