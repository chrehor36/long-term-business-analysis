p='Test Runs/_research 2026-09-28 ATR/body_q3.md'
s=open(p,encoding='utf-8').read()
R=[('$6.4bn of cumulative purchases of businesses, equity stakes and intangibles across the filings read (the 2012 Stelmi, 2016, 2018 CSP, 2019-2021 digital health and 2025 Beauty purchases among them)',
    '$1,463.5M paid for businesses in the fourteen years companyfacts tags (2008-2012, 2016, 2018-2025; the 2012 Stelmi, 2016, 2018 CSP, 2019-2021 and 2025 Beauty purchases among them), besides equity stakes such as the $99.0M for 40% of Goldrain in 2024'),
   ('the segments were reorganised in 2011, 2019 and 2023', 'the segments were reorganised in 2011 and 2023'),
   ('through three chief executives\' tenures and three recessions', 'through three chief executives (Hagge *"since January 2012"*, Tanda *"since February 2017"*, and his predecessor) and three recessions'),
   ('adjusted EPS down 8% to 16% in the first two quarters of 2026', 'adjusted EPS down 8% and 15% in the first two quarters of 2026 ($1.19 against $1.30; $1.42 against $1.68)'),
]
for a,b in R:
    assert s.count(a)==1, a[:50]; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
