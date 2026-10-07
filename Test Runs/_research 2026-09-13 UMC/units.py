import re, os
for y in [2016, 2017, 2019, 2020, 2021, 2022, 2023, 2024, 2025]:
    fn = f"20F_FY{y}.txt"
    if not os.path.exists(fn):
        continue
    t = re.sub(r"\s+", " ", open(fn, encoding="utf-8").read())
    print("== FY", y)
    for pat in [r"Operating revenues (?:increased|decreased)[^§]{0,700}?(?:\d{4}\.)",
                r"Our average capacity utilization rate was [\d.]+%[^§]{0,160}?\d{4}(?:, respectively)?\.",
                r"Our average selling price (?:increased|decreased)[^§]{0,300}?\d{4}[^§]{0,80}?\."]:
        for m in re.finditer(pat, t):
            print("  ", m.group(0)[:900]); break
