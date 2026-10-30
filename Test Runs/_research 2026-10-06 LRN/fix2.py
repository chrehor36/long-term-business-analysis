p=r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-06 Run - LRN Stride.md'
t=open(p,encoding='utf-8').read()
R=[
("Reading: Stride ran about two to three points ahead\n   of the rival's flattering measure in 2019 and 2025, and **both margins rose about thirteen points together**. The rise is\n   the industry's tide (pandemic demand, state funding) at least as much as Stride's castle.",
 "Reading: Stride's GAAP margin was ahead of the rival's flattering measure in 2019 to 2022 (by 2.3, -1.1, 2.7 and 0.8\n   points), behind it in 2023 and 2024 (by 3.3 and 1.3 points), and between 0.9 behind (FY2025) and 2.0 ahead (FY2026) in\n   2025. There is no steady lead, and **both margins rose by eleven to fourteen points over the same years**. The rise is\n   the industry's tide (pandemic demand, state funding) at least as much as Stride's castle."),
("the margin gain is scale leverage on overhead, which is\n   Stride's own. But it is leverage on volume;",
 "the margin gain is leverage on overhead. But the rival's\n   margin rose as far without Stride's scale (table at test 10), so the leverage is not shown to be an edge over the rival;\n   and it is leverage on volume:"),
("margins are near their highs, the rival holds a quarter of the schools, and no single rival is taking it.",
 "margins are near their highs, the rival holds 41 schools to Stride's 92, and no single rival is taking it."),
("The deciding question is not whether Stride has a scale edge (knowable, and the filings already say\nit does) but whether the payer's terms hold for a decade, because the same scale earned thin returns when they did not.",
 "The deciding question is not whether Stride has a scale edge (knowable: it is the larger operator, though its margin\nlead over the rival is not steady) but whether the payer's terms hold for a decade, because the same scale earned thin\nreturns when they did not."),
("The castle (scale, a 31-state bundle, multi-year contracts) is real and Stride's own,\nbut it was there in FY2013-2017 when it earned 1.5% to 5.4%;",
 "The castle (scale, a 31-state bundle, multi-year contracts) is real, but it was there in\nFY2013-2017 when it earned 1.5% to 5.4%;"),
]
for a,b in R:
    if a not in t: print("NOT FOUND:",a[:90].replace('\n','/')); continue
    t=t.replace(a,b,1)
open(p,'w',encoding='utf-8').write(t)
print('done')
