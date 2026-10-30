p='body_q2.md'
s=open(p,encoding='utf-8').read()
reps=[("(more than the $767M of segment D&A over\n  the same years, 2023-2025 alone $395M)","(against $605M of segment depreciation and\n  amortization over the same years, which itself includes the amortization of the 2019 purchase's customer intangibles)"),
("Its best\n  year (8.5%, 2025) is below the five-year figure of nine of the thirteen peers.","Its best\n  year (8.5%, 2025) is below the five-year figure of eleven of the thirteen peers."),
("The 2023-2024 equity-investment base fell by $927M when","The equity-investment base fell by $903M from 2022 to 2024 when")]
for a,b in reps:
    assert a in s,a[:40]
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
