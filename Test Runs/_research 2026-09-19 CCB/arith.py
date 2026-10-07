"""CCB - the arithmetic for Q3 (the [E2-01] return series), Q4 (the capital-retention
requirement that stands in for (c), and the [E3-24] stress) and the below-gate Q5.

Every input is a figure read off a filed statement; the accession is in the comment.
Arithmetic is automated; judgment is in the run file (operator rule 8).
"""

M = 1e6

# --- filed figures, FY2025 10-K acc 0001437958-26-000013 and Q2 2026 10-Q acc 0001437958-26-000061
equity = {2016: 59.90, 2017: 65.71, 2018: 109.16, 2019: 124.17, 2020: 140.22,
          2021: 201.22, 2022: 243.49, 2023: 294.98, 2024: 438.70, 2025: 490.96}
net_income = {2017: 5.44, 2018: 9.70, 2019: 13.20, 2020: 15.15, 2021: 27.00,
              2022: 40.62, 2023: 44.58, 2024: 45.22, 2025: 46.99}
pretax = {2021: 34.38, 2022: 50.62, 2023: 57.13, 2024: 57.32, 2025: 61.24}
cash_tax = {2021: 8.76, 2022: 23.50, 2023: 6.84, 2024: 10.54, 2025: 7.63}
assets = {2020: 1766.12, 2021: 2635.52, 2022: 3144.47, 2023: 3753.37,
          2024: 4121.21, 2025: 4741.44}
sbc = {2021: 1.28, 2022: 2.52, 2023: 3.69, 2024: 4.84, 2025: 8.60}
roe_filed = {2021: 17.24, 2022: 18.24, 2023: 16.41, 2024: 14.11, 2025: 10.17}

# Q2 2026
eq_2026H1 = 463.447
assets_2026H1 = 5456.152
ni_2026H1 = -30.086
tier1_lev_2026H1 = 9.11 / 100.0
tier1_lev_2025 = 10.62 / 100.0

print("=" * 72)
print("[E2-01] RETURN ON EQUITY CAPITAL EMPLOYED - the primary test, multi-year")
print("  yr   NI     avg equity   my ROE   filer ROE   pretax/avg eq  cash tax % pretax")
for y in range(2021, 2026):
    ae = (equity[y - 1] + equity[y]) / 2
    print("  %d  %6.2f  %8.2f   %6.2f%%   %6.2f%%      %6.2f%%        %5.1f%%"
          % (y, net_income[y], ae, 100 * net_income[y] / ae, roe_filed[y],
             100 * pretax[y] / ae, 100 * cash_tax[y] / pretax[y]))
ae26 = (equity[2025] + eq_2026H1) / 2
print("  H1-26 %6.2f  %8.2f   %6.2f%% (annualised %.2f%%)  filer -12.04%%"
      % (ni_2026H1, ae26, 100 * ni_2026H1 / ae26, 200 * ni_2026H1 / ae26))

print()
print("=" * 72)
print("THE CONVENTION FOR (c) IN A BANK - capital retention required to hold the")
print("regulatory leverage ratio constant while assets grow.  Tier 1 leverage used:")
print("  2021-25 at the FY2025 Company ratio %.2f%%; H1-26 at %.2f%%"
      % (100 * tier1_lev_2025, 100 * tier1_lev_2026H1))
print("  yr   d(assets)  capital required   net income   surplus/(shortfall)")
tot_req = tot_ni = 0.0
for y in range(2021, 2026):
    d = assets[y] - assets[y - 1]
    req = d * tier1_lev_2025
    tot_req += req
    tot_ni += net_income[y]
    print("  %d  %9.2f  %14.2f  %11.2f  %15.2f"
          % (y, d, req, net_income[y], net_income[y] - req))
d = assets_2026H1 - assets[2025]
req = d * tier1_lev_2026H1
print("  H1-26 %8.2f  %14.2f  %11.2f  %15.2f" % (d, req, ni_2026H1, ni_2026H1 - req))
print("  FIVE-YEAR TOTAL 2021-25: required %.1f  earned %.1f  shortfall %.1f"
      % (tot_req, tot_ni, tot_ni - tot_req))
print("  equity actually rose %.1f (%.1f -> %.1f); cumulative net income %.1f;"
      % (equity[2025] - equity[2020], equity[2020], equity[2025], tot_ni))
print("  so %.1f of the equity increase came from ISSUANCE, not earnings."
      % (equity[2025] - equity[2020] - tot_ni))
print("  owner earnings on this construction (net income less the retention (c)):")
for y in range(2021, 2026):
    req = (assets[y] - assets[y - 1]) * tier1_lev_2025
    print("    %d  %7.2f" % (y, net_income[y] - req))
oe = [net_income[y] - (assets[y] - assets[y - 1]) * tier1_lev_2025 for y in range(2021, 2026)]
print("    5-year mean %.2f ; 3-year (2023-25) mean %.2f"
      % (sum(oe) / 5, sum(oe[-3:]) / 3))

print()
print("=" * 72)
print("[E2-50] THE RESERVING RECORD AGAINST SUBSEQUENT CHARGE-OFFS")
# ACL and net charge-offs by segment, FY2023-FY2025 10-Ks and Q2 2026 10-Q
# 2023 figures are the RESTATED ones from the FY2024 10-K Note 23 (acc 0001437958-25-000058)
acl = {2023: (21.595, 95.786, 117.381), 2024: (18.924, 158.070, 176.994),
       2025: (18.231, 151.299, 169.530)}          # (community bank, CCBX, total)
nco = {2023: (0.052, 144.491, 144.543), 2024: (0.540, 215.510, 216.050),
       2025: (0.027, 196.806, 196.833)}
covered = {2021: 100.0, 2022: 99.4, 2023: 97.5, 2024: 97.4, 2025: 97.7}
print("  ACL at 31-Dec (CB / CCBX / total), next year's net charge-offs, and the ratio")
for y in (2023, 2024):
    print("   %d ACL %6.2f/%7.2f/%7.2f -> %d NCO %6.3f/%7.2f/%7.2f  ACL covers %.2fx"
          % (y, acl[y][0], acl[y][1], acl[y][2], y + 1, nco[y + 1][0], nco[y + 1][1],
             nco[y + 1][2], acl[y][2] / nco[y + 1][2]))
print("  community bank ACL vs its OWN next-year charge-offs:")
for y in (2023, 2024):
    print("   %d ACL %.3f covers %d NCO %.3f  = %.0fx"
          % (y, acl[y][0], y + 1, nco[y + 1][0], acl[y][0] / nco[y + 1][0]))
print("  %% of CCBX net charge-offs covered by the partner credit enhancement:",
      covered)

print()
print("=" * 72)
print("[E3-24] THE STRESS, IN THE CORPUS'S OWN FORM, ON COASTAL'S OWN BOOK")
# Q2 2026 10-Q segment note
cb_loans = 1982.518
ccbx_loans = 2225.752
enh_asset = 154.346
cash_reserve = 72.2          # FY2025 10-K; the quarterlies do not disclose it
pretax_run = 61.24           # FY2025 pre-tax, the last full clean year
enh_income_2025 = 187.653    # BaaS credit enhancements, FY2025 noninterest income
print("A. THE CORPUS'S LITERAL TEST on the community bank book ($%.1fM at 2026-06-30):"
      % cb_loans)
for share, sev in ((0.10, 0.30), (0.15, 0.40), (0.20, 0.50)):
    loss = cb_loans * share * sev
    print("   %2.0f%% of loans at %2.0f%% severity = $%.1fM loss, vs a year's pre-tax of "
          "$%.1fM -> %s" % (100 * share, 100 * sev, loss, pretax_run,
                            "roughly break even" if abs(loss - pretax_run) < 15
                            else ("absorbed by earnings" if loss < pretax_run
                                  else "$%.1fM out of equity" % (loss - pretax_run))))
print()
print("B. THE ACTUAL DEATH: the counterparty, not the borrower.")
print("   uncollateralised credit enhancement asset = %.1f - %.1f = $%.1fM"
      % (enh_asset, cash_reserve, enh_asset - cash_reserve))
print("   FY2025 BaaS credit enhancement income = $%.1fM" % enh_income_2025)
print("   if the enhancement were worth nothing for ONE YEAR at FY2025 volumes:")
print("     consolidated pre-tax %.1f - %.1f = %.1f"
      % (pretax_run, enh_income_2025, pretax_run - enh_income_2025))
loss1 = enh_income_2025 - pretax_run
print("     equity 463.4 -> %.1f after tax at 25%% (%.1f)"
      % (eq_2026H1 - loss1 * 0.75, loss1 * 0.75))
for n in (1, 2):
    eq = eq_2026H1 - n * loss1 * 0.75
    lev = eq / assets_2026H1
    print("     after %d such year(s): equity $%.1fM, equity/assets %.2f%% %s"
          % (n, eq, 100 * lev,
             "(below the 5%% well-capitalised Tier 1 leverage line)" if lev < 0.05 else ""))
print()
print("C. THE GRADED VERSION - what one partner failing costs, calibrated on the one")
print("   that already failed (Q2 2026: $22.8M provision + $46.0M valuation adjustment")
print("   = $68.8M pre-tax on ONE non-public partner):")
for k in (1, 2, 3, 5):
    print("     %d partner(s) of 28 at the observed $68.8M = $%.1fM pre-tax, %.0f%% of"
          " 2026-06-30 equity" % (k, 68.8 * k, 100 * 68.8 * k / eq_2026H1))

print()
print("=" * 72)
print("BELOW-GATE COMPUTATION - NOT A CLEARANCE")
price = 45.97
shares = 15286327
cap = price * shares / M
print("  price $%.2f (2026-09-18) x %d shares (cover 2026-08-03) = cap $%.1fM"
      % (price, shares, cap))
print("  book value per share 2026-06-30 = %.2f / %d = $%.2f  -> price/book %.2fx"
      % (eq_2026H1, shares, eq_2026H1 * M / shares, price / (eq_2026H1 * M / shares)))
print("  sovereign 5.34%% (US Treasury 30y, 2026-09-18)")
for lab, e in (("FY2025 net income", 46.99), ("FY2025 pre-tax", 61.24),
               ("5y mean net income 2021-25", sum(net_income[y] for y in range(2021, 2026)) / 5),
               ("5y mean pre-tax 2021-25", sum(pretax.values()) / 5),
               ("5y mean retention-adjusted (the CONVENTION)", sum(oe) / 5),
               ("3y mean retention-adjusted", sum(oe[-3:]) / 3),
               ("TTM net income (H2-25 + H1-26)", 26.235 + ni_2026H1)):
    print("   %-44s $%8.2fM -> %7.2f%% of cap" % (lab, e, 100 * e / cap))
print("  pre-tax expectancy vs the ~10%% floor [E4-28]:")
for lab, e in (("FY2025 pre-tax", 61.24), ("5y mean pre-tax", sum(pretax.values()) / 5)):
    print("   %-24s %.2f%%" % (lab, 100 * e / cap))
print("  growth needed for the 5y retention-adjusted mean to reach a 10%% pre-tax yield:")
tgt = 0.10 * cap
print("   target $%.1fM against 5y mean $%.1fM -> %.0f%% higher" % (tgt, sum(oe) / 5,
      100 * (tgt / (sum(oe) / 5) - 1)))
