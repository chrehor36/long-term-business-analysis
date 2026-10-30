# KHI Powersports & Engine segment, JPY millions; KHI "FY2021" = FYE March 2022.
rows = [("FYE Mar-2022", 447927, 448773, 37523, None), ("FYE Mar-2023", 591151, 592184, 71533, None),
        ("FYE Mar-2024", 592421, 593594, 48071, None), ("FYE Mar-2025", 609357, 610684, 47884, 697708),
        ("FYE Mar-2026", 682812, 683960, 22750, 820075)]
for n, ext, tot, bp, a in rows:
    s = f"{n}: profit {bp:,} / total revenue {tot:,} = {100*bp/tot:.1f}% | / external revenue {ext:,} = {100*bp/ext:.1f}%"
    if a: s += f" | / segment assets {a:,} = {100*bp/a:.1f}%"
    print(s)
units = {"FYE Mar-2022": (208, 283), "FYE Mar-2023": (237, 318), "FYE Mar-2024": (211, 233), "FYE Mar-2025": (234, 246), "FYE Mar-2026": (239, 270)}
mcrev = {"FYE Mar-2022": (169.9, 100.8), "FYE Mar-2023": (211.2, 115.8), "FYE Mar-2024": (217.9, 103.4), "FYE Mar-2025": (245.3, 99.2), "FYE Mar-2026": (261.9, 102.6)}
for k in units:
    print(f"{k}: wholesale motorcycles {units[k][0]} + {units[k][1]} = {sum(units[k])}k | motorcycle revenue {mcrev[k][0]} + {mcrev[k][1]} = {sum(mcrev[k]):.1f} bn")
