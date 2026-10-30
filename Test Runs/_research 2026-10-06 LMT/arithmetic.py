"""Owner cash after every real cost, LMT, from the filed cash-flow statements (USD millions).
OCF, stock pay, capex, D&A: 10-K FY2025 (0001628280-26-004195) for 2023-2025; 10-K FY2022 (0000936468-23-000009) for
2021-2022. Sales and operating profit: the same filings. Price and shares: tools/run.py and Screens/cover_shares.py.
Owner cash = OCF - stock pay - all capital spending (OCF adds stock pay back, so it is taken out again).
Depreciation variant = OCF - stock pay - D&A. Output: arithmetic_output.txt."""
ocf = {2021: 9221, 2022: 7802, 2023: 7920, 2024: 6972, 2025: 8557}
sbc = {2021: 227, 2022: 238, 2023: 265, 2024: 277, 2025: 304}
capex = {2021: 1522, 2022: 1670, 2023: 1691, 2024: 1685, 2025: 1649}
da = {2021: 1364, 2022: 1404, 2023: 1430, 2024: 1559, 2025: 1687}
sales = {2021: 67044, 2022: 65984, 2023: 67571, 2024: 71043, 2025: 75048}
op = {2021: 9123, 2022: 8348, 2023: 8507, 2024: 7013, 2025: 7731}
oc = {y: ocf[y] - sbc[y] - capex[y] for y in ocf}
for y in oc:
    print(y, oc[y], ocf[y] - sbc[y] - da[y], round(oc[y] / sales[y] * 100, 1), round(op[y] / sales[y] * 100, 1))
m = sum(oc.values()) / 5
print("mean", m, "dvar", sum(ocf[y] - sbc[y] - da[y] for y in oc) / 5)
sh, px = 230.790753, 506.63
cap = px * sh
print("cap", cap, "yield", m / cap * 100)
print("per share", m / sh, oc[2025] / sh)
print("cagr", (oc[2025] / oc[2021]) ** 0.25 - 1)
