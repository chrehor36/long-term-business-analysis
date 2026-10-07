# Suzuki Motorcycle business segment, JPY millions. Suzuki "FY2021" = April 2021 - March 2022.
rows = [("FY2021 (FY3/22) J-GAAP", 253458, 10859, 257509), ("FY2022 (FY3/23) J-GAAP", 333151, 29340, 281167),
        ("FY2023 (FY3/24) J-GAAP", 366934, 39013, 322256), ("FY2023 (FY3/24) IFRS", 365041, 39086, 358732),
        ("FY2024 (FY3/25) IFRS", 398131, 40822, 380629), ("FY2025 (FY3/26) IFRS", 454488, 44770, 419115)]
for n, r, o, a in rows:
    print(f"{n}: {o:,} / {r:,} = {100*o/r:.1f}% | op / segment assets {o:,} / {a:,} = {100*o/a:.1f}%")
