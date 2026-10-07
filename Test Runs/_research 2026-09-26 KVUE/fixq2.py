import io
p='q2.md'; s=open(p,encoding='utf-8').read()
reps=[
("**Perrigo** (the largest US store-brand OTC maker, the substitute itself)","**Perrigo** (in its own 10-K for 2025, `peers/prgo_10k_2025.txt`: *\"In North America, Perrigo is the leading store brand private label provider of self-care products in many categories, including upper respiratory, healthy lifestyle and women's health\"*; the substitute itself, with a European branded business beside it)"),
("and the only one in 2025 with flat price and falling units; Clorox, the one peer this project closed OUT, is the nearest pattern.","and, with Clorox (FY2026 0 / −7), the only one whose latest year had flat price and falling units; Clorox, the one peer here this project closed OUT, is the nearest pattern."),
("**The substitute is a poor business**: Perrigo, which makes the store-brand acetaminophen, antihistamines and nicotine gum, earns 2.6-3.3% operating margins and 1-2% on its total capital before the 2025 write-down;","**The substitute is a poor business**: Perrigo earns 2.6-3.3% operating margins and 1-2% on its total capital before the 2025 write-down, and says of its own store brands that they *\"generate cash for investments into the Company’s key higher margin, higher growth brands\"*;"),
("and bought (Ci:z/Dr.Ci:Labo, Zarbee's, NeoStrata)","and bought (Ci:z Holdings, the Dr.Ci:Labo owner: J&J's 2019 growth was *\"primarily driven by incremental sales from the acquisition of Ci:z Holding\"*)"),
("2010 $14.6bn (the McNEIL recall year, *\"an operational decline\"* of 8.9%)","2010 $14.6bn (*\"an operational decline\"* of 8.9%, the McNeil recall year: *\"McNeil’s recalls of products manufactured at both Las Piedras and Fort Washington facilities impacted the total year sales by approximately $900 million\"*)"),
("5. **The names survived worse**: the 2010 McNEIL recalls","5. **The names survived worse**: the 2010 McNeil recalls"),
("6. **Kimberly-Clark is paying about $48.7bn for it** (its own 10-Q), which is a purchaser's judgment on the brands.","6. **Kimberly-Clark agreed a price that *\"values Kenvue at an enterprise value of approximately $48.7 billion\"*** (joint release, EX-99.1 to the 8-K of 2025-11-03, on KMB's 2025-10-31 close), *\"approximately 14.3x Kenvue’s LTM adjusted EBITDA\"*: a purchaser's judgment on the brands."),
("because no filed figure yet measures an effect (Pain Care 11-12% of sales in both halves of 2025 and 2026, the 10-Q's category table).","because no filed figure yet measures an effect (Pain Care 11-12% of sales in the second quarter and first half of both 2025 and 2026, the 10-Q's category table)."),
]
for a,b in reps:
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
print('ok')
