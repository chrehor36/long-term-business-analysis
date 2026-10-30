"""EMBC [E4-25] window rebuild. COMPUTATION ONLY -- Q2 returned OUT and Q4 never opened.
Owner earnings CONVENTION (framework section VI): operating cash flow less SBC less (c).
(c) band ends: D&A (the [E3-44] default) and total capex.
All inputs are 10-K annual facts from companyfacts.json, cross-checked for FY2023-FY2025
against the filed FY2025 Consolidated Statements of Cash Flows.
"""
ocf   = {2020:498.5, 2021:456.3, 2022:412.2, 2023:67.7, 2024:35.7, 2025:191.7}
sbc   = {2020:12.7,  2021:12.8,  2022:18.7,  2023:21.5, 2024:26.3, 2025:31.6}
da    = {2020:38.3,  2021:38.3,  2022:31.7,  2023:32.6, 2024:36.2, 2025:40.7}
capex = {2020:41.9,  2021:36.8,  2022:23.6,  2023:26.5, 2024:15.8, 2025:9.3}

def mean(d, ys): return sum(d[y] for y in ys)/len(ys)

windows = {
    "FY2023-FY2025  (3y, standalone only)": [2023,2024,2025],
    "FY2021-FY2025  (5y, corpus default window [E2-42])": [2021,2022,2023,2024,2025],
    "FY2020-FY2025  (6y, everything filed)": [2020,2021,2022,2023,2024,2025],
    "FY2022-FY2025  (4y, includes the stub year)": [2022,2023,2024,2025],
}
print(f"{'window':52} {'OCF':>8} {'SBC':>7} {'(c)D&A':>8} {'(c)capex':>9} {'OE hi':>8} {'OE lo':>8}")
for name, ys in windows.items():
    o, s, d, c = mean(ocf,ys), mean(sbc,ys), mean(da,ys), mean(capex,ys)
    lo, hi = o-s-d, o-s-c
    print(f"{name:52} {o:8.1f} {s:7.1f} {d:8.1f} {c:9.1f} {hi:8.1f} {lo:8.1f}")
print()
print("Screen row published band: $35M to $181M, spread 4.151x.")
print("Note which windows those two ends come from.")
