"""MRK owner cash after every real cost, from the filed cash-flow statements (USD millions).
Sources: 10-K FY2025 0000310158-26-000063 (2023-2025); 10-K FY2022 0001628280-23-005061 (2021-2022, continuing operations);
10-Q Q2 2026 0000310158-26-000212 (H1 2026 acquisitions). Arithmetic only; no verdict."""

rows = {  # FY: (OCF continuing, share-based comp, capex, cash paid for businesses/pipeline bought, net of cash acquired)
    2021: (13122, 479, 4448, 11174 + 1554 + 179),   # Acceleron, Pandion, other
    2022: (19095, 541, 4388, 121),                   # other acquisitions
    2023: (13006, 645, 3863, 10705 + 1327),          # Prometheus, Imago
    2024: (21468, 761, 3372, 1344 + 1303 + 746 + 700),  # EyeBio, Elanco aqua, Harpoon, Curon MK-1045
    2025: (16472, 820, 4112, 10042),                 # Verona Pharma
}
tot_oc = tot_acq = 0
print("FY    OCF    SBC  capex  owner_cash  bought  owner_cash_after_bought")
for y, (ocf, sbc, capex, acq) in rows.items():
    oc = ocf - sbc - capex
    tot_oc += oc
    tot_acq += acq
    print(y, ocf, sbc, capex, oc, acq, oc - acq)
n = len(rows)
print("5-yr mean owner cash", round(tot_oc / n, 1), " mean bought", round(tot_acq / n, 1),
      " mean after bought", round((tot_oc - tot_acq) / n, 1))

price, shares_m = 139.54, 2467.171638   # close 2026-10-05 (aggregator, flagged); 10-Q cover 2026-07-31
cap = price * shares_m
print("market cap $M", round(cap, 1))
print("owner cash yield", round(100 * tot_oc / n / cap, 2), "%;  after bought",
      round(100 * (tot_oc - tot_acq) / n / cap, 2), "%")

sales25 = 65011
keytruda = 31680
loe_2026_2028 = {"Keytruda": 31680, "Gardasil/Gardasil 9": 5233, "Januvia/Janumet": 2544,
                 "Bridion": 1841, "Lynparza alliance": 1450}  # US key-patent expiry 2026-2028 per 10-K Item 1 table
print("Keytruda share of 2025 sales", round(100 * keytruda / sales25, 1), "%")
s = sum(loe_2026_2028.values())
print("sales of products whose US key patent expires 2026-2028:", s, round(100 * s / sales25, 1), "% of 2025 sales")
h1_2026_bought = 8779 + 5842   # Cidara, Terns
print("bought 2021 to H1 2026:", tot_acq + h1_2026_bought)
