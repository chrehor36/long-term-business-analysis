p = 'Test Runs/_research 2026-09-28 ATR/body_q2.md'
s = open(p, encoding='utf-8').read()
R = [
 ('(Pharma +12%, +10%, +9%, +2%, +13%, +10%, +8%, +3% in 2018-2025; −? not filed before 2016)',
  '(Pharma +5% in 2016; +12%, +10%, +9%, +2%, +13%, +10%, +8%, +3% in 2018-2025; the 2017 figure is described, *"core sales growth in each end market"*, not stated)'),
 ('; the emergency medicine line is part of a prescription division whose core sales rose in every year 2018-2025 but one.',
  '; the named weakness is one product line inside a segment whose core sales grew in every year the filer states (2016, 2018-2025).'),
 ("Quaker's price followed raw materials both ways and its return never exceeded 9.7%;",
  "Quaker's price followed raw materials both ways and its return on all capital had not exceeded 9.7% in any year since 2019;"),
 ('West, the class leader, reports', 'West, the largest SEC filer in injectable components, reports'),
 ("(Nemera, Kindeva, the Bespak business, Coster), with no document at any rung of the ladder;",
  "(Nemera, Kindeva and Coster are named here from outside the filings; none appears in the SEC's company ticker list, searched for this run, and no filing at any rung of the ladder gives a pump or valve segment's margin);"),
 ('and West\'s (the leader in injectable components, which names Aptar)', "and West's (the largest SEC filer in injectable components, which names Aptar)"),
]
for a, b in R:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print('ok')
