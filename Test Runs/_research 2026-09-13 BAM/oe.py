# Owner earnings for BAM, from the FILED cash-flow statements only (no companyfacts rows).
# Sources: 10-K FY2025 (0001628280-26-013098) cash-flow statement FY2023-25 (Predecessor-restated);
# 10-Q Q2 2026 (0001628280-26-054933) cash-flow statement H1 2026 and H1 2025; Note 12 SBC tables.
periods = ["FY2023", "FY2024", "FY2025", "H1_2025", "H1_2026"]
d = {
 # net cash from operating activities, as filed
 "ocf":        {"FY2023": 1439, "FY2024": 1612, "FY2025": 2101, "H1_2025": 643, "H1_2026": 883},
 # consolidated-fund investment flows INSIDE operating activities (reclassified there in FY2025 10-K)
 # FY: "Changes in investments of consolidated funds"; H1: investments (-) plus dispositions (+)
 "consfund":   {"FY2023": 0, "FY2024": -251, "FY2025": -467, "H1_2025": -465, "H1_2026": -85 + 136},
 # stock-based equity awards, cash-flow add-back
 "sbc_cf":     {"FY2023": 33, "FY2024": 103, "FY2025": 123, "H1_2025": 62, "H1_2026": 79},
 # Note 12: equity-settled expense + cash-settled (DSU/RSU) expense
 "sbc_note":   {"FY2023": 86 + 12, "FY2024": 95 + 43, "FY2025": 159 + 88, "H1_2025": 80 + 21, "H1_2026": 119 + 8},
 "da":         {"FY2023": 14, "FY2024": 14, "FY2025": 40, "H1_2025": 14, "H1_2026": 26},
 # investing: "Other assets" (the only capex-like line)
 "capex":      {"FY2023": 17, "FY2024": 8, "FY2025": 9, "H1_2025": 3, "H1_2026": 16},
 # financing: distributions to non-controlling and redeemable non-controlling interests (BN's carry/preferreds)
 "nci_dist":   {"FY2023": 42, "FY2024": 52, "FY2025": 216, "H1_2025": 11, "H1_2026": 76},
 # look-through: share of equity-method income net of cash distributions (sign flipped from the CF add-back)
 "lookthru":   {"FY2023": -21, "FY2024": 122, "FY2025": 7, "H1_2025": 36, "H1_2026": 200},
 # financing: distributions to common stockholders, and treasury purchases
 "div":        {"FY2023": 2101, "FY2024": 2478, "FY2025": 2818, "H1_2025": 1409, "H1_2026": 1611},
 "buyback":    {"FY2023": 0, "FY2024": 0, "FY2025": 412, "H1_2025": 116, "H1_2026": 576},
 # management's Distributable Earnings (non-GAAP), for reconciliation only
 "de":         {"FY2023": 2244, "FY2024": 2363, "FY2025": 2695, "H1_2025": 1267, "H1_2026": 1409},
}
# TTM to 2026-06-30 = FY2025 - H1_2025 + H1_2026
for k in d:
    d[k]["TTM_2026-06"] = d[k]["FY2025"] - d[k]["H1_2025"] + d[k]["H1_2026"]
cols = ["FY2023", "FY2024", "FY2025", "TTM_2026-06"]

def row(name, f):
    vals = {c: f(c) for c in cols}
    print(f"{name:58s} " + " ".join(f"{vals[c]:>9,.0f}" for c in cols))
    return vals

print(f"{'($M)':58s} " + " ".join(f"{c:>9s}" for c in cols))
row("OCF as filed", lambda c: d["ocf"][c])
row("+ strip consolidated-fund investment flows", lambda c: -d["consfund"][c])
adj = row("= OCF, BAM perimeter (A1)", lambda c: d["ocf"][c] - d["consfund"][c])
row("- distributions to NCI/redeemable NCI (BN carry, prefs)", lambda c: d["nci_dist"][c])
cons = row("CONSERVATIVE: A1 - NCI dist - SBC(note) - D&A", lambda c: adj[c] - d["nci_dist"][c] - d["sbc_note"][c] - d["da"][c])
gen = row("GENEROUS: A1 - NCI dist - SBC(CF) - capex + lookthru", lambda c: adj[c] - d["nci_dist"][c] - d["sbc_cf"][c] - d["capex"][c] + d["lookthru"][c])
filed = row("FILED-BASIS DISPLAY: OCF - SBC(CF) - D&A (no perimeter adj)", lambda c: d["ocf"][c] - d["sbc_cf"][c] - d["da"][c])
row("SBC (note, total)", lambda c: d["sbc_note"][c])
row("SBC (CF add-back)", lambda c: d["sbc_cf"][c])
row("Distributable Earnings (mgmt, non-GAAP)", lambda c: d["de"][c])
row("Dividends to common, paid", lambda c: d["div"][c])
row("Buybacks", lambda c: d["buyback"][c])
print()
for c in cols:
    print(c, "SBC/OCF(A1) note %.1f%%  CF %.1f%%" % (100*d["sbc_note"][c]/adj[c], 100*d["sbc_cf"][c]/adj[c]),
          "| div/OE cons %.0f%% gen %.0f%%" % (100*d["div"][c]/cons[c], 100*d["div"][c]/gen[c]),
          "| (div+bb)/A1 %.0f%%" % (100*(d["div"][c]+d["buyback"][c])/adj[c]),
          "| DE - A1 = %d" % (d["de"][c]-adj[c]))
import statistics as st
w3 = ["FY2023", "FY2024", "FY2025"]; w2 = ["FY2024", "FY2025"]
for nm, series in [("conservative", cons), ("generous", gen), ("filed-basis", filed)]:
    print(nm, "3yr mean %.0f" % st.mean(series[c] for c in w3), "2yr mean %.0f" % st.mean(series[c] for c in w2), "TTM %.0f" % series["TTM_2026-06"])
cum_sbc = sum(d["sbc_note"][c] for c in w3); cum_ocf = sum(adj[c] for c in w3)
print("cumulative FY23-25 SBC(note)/OCF(A1) %.1f%%" % (100*cum_sbc/cum_ocf))
cap = 47.26 * 1597251633 / 1e6
print("cap $M", round(cap))
for nm, series in [("conservative", cons), ("generous", gen)]:
    for lab, v in [("3yr", st.mean(series[c] for c in w3)), ("2yr", st.mean(series[c] for c in w2)), ("TTM", series["TTM_2026-06"])]:
        print(nm, lab, "yield %.2f%%" % (100*v/cap))
print("DE TTM yield %.2f%%" % (100*d["de"]["TTM_2026-06"]/cap))
