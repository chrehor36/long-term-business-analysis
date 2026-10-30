"""Owner cash after every real cost for 3M, from the filed cash-flow statements (USD millions).
owner cash = operating cash flow (which adds stock pay back) - stock pay - all capital spending.
Sources: 10-K FY2025 (0000066740-26-000014) for 2023-2025; 10-K FY2022 (0000066740-23-000014) for 2021-2022
(XBRL facts, transcription; 2025 OCF read against the filed statement, page 44).
Caveat recorded in the run: every year's OCF includes discontinued operations (Health Care / Solventum) up to
its separation on 2024-04-01, and 2023-2025 include the PWS and CAE settlement payments."""
rows = {
    # year: (OCF, SBC, capex, D&A)
    2021: (7454, 274, 1603, None),
    2022: (5591, 263, 1749, None),
    2023: (6680, 274, 1615, 1987),
    2024: (1819, 289, 1181, 1363),
    2025: (2306, 225, 910, 1308),
}
oc = {}
for y, (ocf, sbc, capex, da) in rows.items():
    oc[y] = ocf - sbc - capex
    print(y, "owner cash", oc[y])
print("5-yr mean 2021-2025", round(sum(oc.values()) / 5))
print("3-yr mean 2023-2025", round(sum(oc[y] for y in (2023, 2024, 2025)) / 3))
price, shares = 163.19, 515.722417
cap = price * shares
print("market cap $M", round(cap))
for label, v in (("5-yr mean", sum(oc.values()) / 5), ("2025", oc[2025])):
    print(label, "yield on cap", round(100 * v / cap, 2), "%")
