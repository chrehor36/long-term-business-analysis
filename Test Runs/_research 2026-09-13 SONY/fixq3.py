p='q3.md'; t=open(p,encoding='utf-8').read()
reps=[
("IFRS, PwC-type integrated audit with ICFR opinion (Item 15)","IFRS, integrated audit with an internal-control opinion (auditor's report at F-2, PCAOB ID 2743)"),
("| 4th mid-range plan: cumulative Adjusted EBITDA ¥4.3tn, FY3/22–24 (20-F FY3/22) | 1,597.9 + 1,816.9 + 1,826.1 = ¥5,240.9bn | beat +22% |",
 "| 4th mid-range plan: cumulative Adjusted EBITDA ¥4.3tn, FY3/22–24 (20-F FY3/22) | 1,597.9 (20-F FY3/22) + 1,797.6 + 1,818.0 (20-F FY3/24) = ¥5,213.5bn | beat +21% |"),
("*favourably* (¥5.24tn against ¥4.3tn)","*favourably* (¥5.21tn against ¥4.3tn)"),
("[E4-50] licenses borrowing to buy *\"only\"* at a true discount; condition (2) is the flag above.",
 "[E4-50] licenses aggressive buying, borrowing included, at a true discount; the discount does the licensing, and condition (2) is the flag above."),
("(2) equity rose partly on\ntranslation (the yen weakened across the window; AOCI moved from ¥(614.6)bn at April 2023 to ¥1,229.4bn\nat March 2026 in the equity statement, much of it FS-related and recycled at the spin).*",
 "(2) equity rose partly on\ntranslation: *\"Exchange differences on translating foreign operations\"* were +¥442.4bn, −¥79.3bn and +¥424.4bn\nin FY3/24–FY3/26 (continuing, consolidated statements of comprehensive income, 20-F FY3/26).*"),
("so cash tax\n  running below book tax in the spin-off year reads as timing, not the Chubb-type tell.",
 "so cash tax\n  running below book tax in the spin-off year reads as timing, not the [E4-30] pattern of a falling share\n  sustained over years."),
("A US-listed ADR\nholder stands behind the Tokyo register. No controlling shareholder was found in Item 7.",
 "A US-listed ADR\nholder stands behind the Tokyo register. Item 7: *\"To the knowledge of Sony Group Corporation, it is not directly\nor indirectly owned or controlled by any other corporation, by any foreign government or by any other natural or\nlegal person\"*; the largest bulk holding report is BlackRock Japan and joint holders, 8.53% (December 5, 2024)."),
]
for a,b in reps:
    assert a in t, a[:60]
    t=t.replace(a,b)
open(p,'w',encoding='utf-8').write(t); print('ok')
