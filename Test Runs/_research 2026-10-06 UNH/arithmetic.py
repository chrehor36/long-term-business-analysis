"""UNH run 2026-10-06: the arithmetic behind the run file. Inputs are filed figures (accessions in the run file).
Same number sooner, no number added."""

price = 378.58              # 2026-10-05 close, tools/run.py live quote (aggregator, flagged)
shares_m = 897.594847       # cover of 10-Q filed 2026-08-10, accession 0000731766-26-000197
print("market cap $M", round(price * shares_m, 1))

# 10-K FY2025 (0000731766-26-000062), results summary
prem_2025 = 352_229
mcr_2023, mcr_2024, mcr_2025 = 83.2, 85.5, 89.1
print("MCR swing 2023->2025, points", round(mcr_2025 - mcr_2023, 1),
      "= $M of 2025 premium", round(prem_2025 * (mcr_2025 - mcr_2023) / 100))
oi = {2007: 7849, 2008: 5263, 2009: 6359, 2010: 7864, 2011: 8464, 2012: 9254, 2013: 9623, 2014: 10274,
      2015: 11021, 2016: 12930, 2017: 15209, 2018: 17344, 2019: 19685, 2020: 22405, 2021: 23970,
      2022: 28435, 2023: 32358, 2024: 32287, 2025: 18964}   # XBRL OperatingIncomeLoss, 10-K FY values
rev = {2007: 75431, 2015: 157107, 2023: 371622, 2024: 400278, 2025: 447567}
for y in (2007, 2015, 2023, 2025):
    print("operating margin", y, round(100 * oi[y] / rev[y], 1), "%")
rises = [y for y in range(2009, 2024) if oi[y] > oi[y - 1]]
print("years 2009-2023 in which operating earnings rose:", len(rises), "of", 2023 - 2009 + 1)
print("operating earnings change 2024->2025", round(100 * (oi[2025] / oi[2024] - 1), 1), "%")
print("revenue change 2024->2025", round(100 * (rev[2025] / rev[2024] - 1), 1), "%")

# 2025 outlook against outcome, adjusted EPS (8-K EX-99.1s, accessions in the run file)
for g in (29.50, 30.00):
    print("Dec-2024 adjusted EPS outlook", g, "against actual 16.35: shortfall",
          round(100 * (1 - 16.35 / g), 1), "%")
print("GAAP: outlook 28.15-28.65 against actual 13.23: shortfall",
      round(100 * (1 - 13.23 / 28.15), 1), "to", round(100 * (1 - 13.23 / 28.65), 1), "%")

# 2026 outlook as of 2026-07-16 (8-K 0000731766-26-000191 EX-99.1), segment operating earnings floors, $M
seg = {"UnitedHealthcare": 12000, "Optum Health": 2275, "Optum Insight": 4925, "Optum Rx": 6250}
tot = sum(seg.values())
for k, v in seg.items():
    print("share of 2026 outlook operating earnings", k, round(100 * v / tot, 1), "%")
# UnitedHealthcare 2026 revenue outlook floors (8-K 0000731766-26-000025 EX-99.1), $M
mr, cs, ei, uhc = 165000, 95000, 75000, 335000
print("government programs (M&R + C&S) share of UHC revenue floor", round(100 * (mr + cs) / uhc, 1), "%")
