"""Additional companies for calc.py. (year, numerator, denominator)."""
EXTRA = {
    # Nissan, JPY millions, J-GAAP, Securities Report translation, segment note, Automobile column
    "NISSAN automobile (Segment profit (loss) / Net sales Total incl. inter-segment)": [
        ("FY3/2022", -155059, 7475648),
        ("FY3/2023", 42952, 9686842),
        ("FY3/2024", 221574, 11782516),
        ("FY3/2025", -267979, 11645478),
        ("FY3/2026", -292890, 10920106),
    ],
    "NISSAN automobile (Segment profit (loss) / Sales to third parties)": [
        ("FY3/2022", -155059, 7420892),
        ("FY3/2023", 42952, 9591859),
        ("FY3/2024", 221574, 11582863),
        ("FY3/2025", -267979, 11437856),
        ("FY3/2026", -292890, 10760298),
    ],
    # memo: Automobile & Eliminations operating income = consolidated operating income - sales
    # financing segment profit (computed), over consolidated net sales less sales-financing sales
    # to third parties (computed)
    "NISSAN memo (consolidated op. income - sales financing segment profit) / (consolidated net sales - SF sales to third parties)": [
        ("FY3/2022", 247307 - 374824, 8424585 - 1003693),
        ("FY3/2023", 377109 - 311908, 10596695 - 1004836),
        ("FY3/2024", 568718 - 308718, 12685716 - 1102853),
        ("FY3/2025", 69798 - 285647, 12633214 - 1195358),
        ("FY3/2026", 58005 - 297942, 12007888 - 1247590),
    ],
}

EXTRA.update({
    # Hyundai, KRW millions, K-IFRS audited consolidated FS, Note 40 (2021-2024 FS) / Note 37 (2025 FS)
    "HYUNDAI vehicle (Operating profit / Net sales (*1) external)": [
        ("2021", 4155765, 94143019),
        ("2022", 7910469, 113341992),
        ("2023", 12969227, 130149921),
        ("2024", 11074739, 136725011),
        ("2025", 7358550, 145631818),
    ],
    # 2021 FS has no Total sales row; computed as Net sales + Inter-company sales (52,033,375)
    "HYUNDAI vehicle (Operating profit / Total sales (*2) incl. inter-company)": [
        ("2021", 4155765, 94143019 + 52033375),
        ("2022", 7910469, 180440977),
        ("2023", 12969227, 212367654),
        ("2024", 11074739, 221891250),
        ("2025", 7358550, 232879832),
    ],
})

EXTRA.update({
    # BYD, RMB thousands, CAS; segment "Automobiles and related products and other products"
    # (includes power batteries, PV, rail); measure "Total profit" (adjusted profit before tax)
    "BYD auto segment (Total profit / Total revenue incl. inter-segment)": [
        ("2021r", 3136474, 132146746),
        ("2022", 18642184, 328662919),
        ("2023", 31107896, 489233672),
        ("2024", 36332561, 620730928),
        ("2025", 28417336, 652481997),
    ],
    "BYD auto segment (Total profit / Revenue from external trading)": [
        ("2021r", 3136474, 128960450),
        ("2022", 18642184, 324691175),
        ("2023", 31107896, 483453318),
        ("2024", 36332561, 617381933),
        ("2025", 28417336, 648645636),
    ],
    # BYD group gross profit / revenue, Five-Year comparison, 2025 AR (group, not segment)
    "BYD GROUP gross profit / revenue (memo, not segment)": [
        ("2021r", 26916097, 216142395),
        ("2022", 65731123, 424060635),
        ("2023", 111916409, 602315354),
        ("2024", 151055839, 777102455),
        ("2025", 142659797, 803964958),
    ],
    # 2021 as originally reported (HKFRS, three segments): automobiles segment results / sales to external customers
    "BYD 2021 ORIGINAL HKFRS automobiles segment results / sales to external customers": [
        ("2021o", 3187865, 109659458),
    ],
})

EXTRA.update({
    # Suzuki, JPY millions. J-GAAP Consolidated Financial Summary FY2021-FY2023; IFRS ASR FY2023-FY2025
    "SUZUKI automobile J-GAAP (Segment profit / Net sales)": [
        ("FY3/2022", 152832, 3204877),
        ("FY3/2023", 279084, 4162163),
        ("FY3/2024", 398173, 4883804),
    ],
    "SUZUKI automobile IFRS (Operating profit / Total revenue)": [
        ("FY3/2024", 423940, 4869579),
        ("FY3/2025", 567634, 5305217),
        ("FY3/2026", 547632, 5706420),
    ],
})
