"""R2 arithmetic, research pass analyst A, MBUU, 2026-10-05.
Every input is transcribed from the filed segment note or income statement named beside it ($ thousands).
Same-number-sooner only: no input is estimated; where an allocation is used it is labelled CONVENTION.
Output: r2_output.txt beside this file.
"""
out = []
def p(s=""): out.append(s)

# ---------------- Inputs: Malibu (CIK 1590976) ----------------
# New basis, Segment Adjusted EBITDA (10-K FY2025 0001590976-25-000080 for FY2023-25; 10-K FY2026 0001590976-26-000037 for FY2024-26)
mb_seg = {  # year: (Malibu segment net sales, Malibu segment adj EBITDA, all segments adj EBITDA total, total net sales)
    2023: (636247, 186873, 303494, 1388365),
    2024: (279131, 42579, 100773, 829035),
    2025: (312698, 60611, 105139, 807561),
    2026: (312907, 50674, 97429, 914590),
}
# Consolidated Adjusted EBITDA, EX-99.1 results releases: FY2023 and FY2024 from 0001590976-24-000070; FY2025 from
# 0001590976-25-000076; FY2026 from 0001590976-26-000035
mb_cons_adj = {2023: 284036, 2024: 82237, 2025: 74770, 2026: 73936}
# Consolidated operating income, depreciation, amortization, impairment, abandonment (income statement and segment note,
# 10-K FY2026 for FY2024-26, 10-K FY2025 for FY2023)
mb_opinc = {2023: 144784, 2024: -55947, 2025: 21761, 2026: 3099}
mb_dep = {2023: 21912, 2024: 26178, 2025: 31794, 2026: 33147}
mb_amort = {2023: 6808, 2024: 6811, 2025: 6799, 2026: 10805}
mb_other_opex_excl = {2023: 0, 2024: 88389 + 8735, 2025: 0, 2026: 0}  # impairment + abandonment (FY2024 only)
# Old basis, segment net income before taxes + segment D&A, all costs allocated to segments
# (10-K FY2021 0001590976-21-000065 for FY2019-21; 10-K FY2023 0001590976-23-000069 for FY2022-23; 10-K FY2024 0001590976-24-000073 for FY2024)
mb_old = {  # year: (net sales, D&A, pretax)
    2019: (374611, 7674, 54160),
    2020: (354769, 8809, 55567),
    2021: (483525, 9397, 88511),
    2022: (607543, 8398, 137133),
    2023: (636247, 8974, 40157),
    2024: (279131, 9714, -11589),
}
BATCHELDER_FY2023 = 100000  # settlement charged in FY2023 G&A (10-K FY2023); shown both ways

# ---------------- Inputs: MasterCraft (CIK 1638290) ----------------
# Wake segment = "MasterCraft" segment, renamed "Performance and Wake" in FY2026, MasterCraft brand only from FY2020 restatement on.
# "All material corporate costs are included in" this segment (every 10-K FY2019 to FY2026).
# GAAP basis: segment operating income + segment D&A.
mc_gaap = {  # year: (net sales, operating income, D&A, source)
    2019: (311830, 53989, 3481, "10-K FY2019 0001564590-19-034678 (includes Aviara pre-launch)"),
    2020: (236856, 35833, 4078, "10-K FY2022 0001564590-22-031335 (Aviara separated)"),
    2021: (350812, 73354, 4479, "10-K FY2023 0000950170-23-045222"),
    2022: (466027, 105341, 4968, "10-K FY2023 0000950170-23-045222"),
    2023: (468656, 101324, 5555, "10-K FY2023 0000950170-23-045222"),
    2024: (262736, 262736 - 197622 - 35541, 5109, "10-K FY2025 0000950170-25-111682 (sales - cost of sales - operating expenses)"),
    2025: (240763, 240763 - 183180 - 36925, 5888, "10-K FY2026 0001193125-26-387432"),
    2026: (271177, 271177 - 194514 - 55125, 5837, "10-K FY2026 0001193125-26-387432"),
}
# Adjusted basis: segment Adjusted EBITDA as filed (CODM measure from FY2025 10-K on; excludes D&A, share-based pay,
# leadership transition, business development consulting, and in FY2026 ERP costs and Marine Products deal costs).
mc_adj = {2023: (468656, 110292), 2024: (262736, 38862), 2025: (240763, 29771), 2026: (271177, 45855)}
mc_adj_items_2026 = 18480   # Performance and Wake adjustment items, FY2026 (10-K FY2026 segment note)
mc_deal_costs_2026 = 15249  # Marine Products Transaction costs, in G&A (10-K FY2026 segment note); corporate, so in P&W
mc_total_sales_2026 = 348903

def pct(a, b): return 100.0 * a / b

p("R2 ARITHMETIC - Malibu segment against MasterCraft's wake segment ($ thousands)")
p("=" * 100)
p("")
p("1. ADJUSTED BASIS AS FILED (each filer's own segment measure; ex D&A, ex stock pay, ex one-off items).")
p("   Asymmetry: Malibu's segment carries only PART of its corporate cost; MasterCraft's carries ALL of it.")
p("   The asymmetry favours Malibu, so a Malibu figure at or below MasterCraft's here is at or below on any common treatment that charges corporate cost to the segment.")
for y in (2023, 2024, 2025, 2026):
    s, e, _, _ = mb_seg[y]; ms, me = mc_adj[y]
    p(f"   FY{y}: Malibu {e:>7,}/{s:>9,} = {pct(e,s):5.1f}%   MasterCraft {me:>7,}/{ms:>9,} = {pct(me,ms):5.1f}%   gap {pct(e,s)-pct(me,ms):+5.1f} pts")
p("")
p("2. ADJUSTED BASIS, MasterCraft's corporate rule mirrored: Malibu's unallocated recurring corporate cost")
p("   (segment total less consolidated Adjusted EBITDA) charged to the Malibu segment, as MasterCraft charges all of its own to its wake segment.")
for y in (2023, 2024, 2025, 2026):
    s, e, tot, _ = mb_seg[y]; corp = tot - mb_cons_adj[y]; ms, me = mc_adj[y]
    p(f"   FY{y}: unallocated recurring corporate {corp:>6,}; Malibu ({e:,} - {corp:,})/{s:,} = {pct(e-corp,s):5.1f}%   MasterCraft {pct(me,ms):5.1f}%")
p("")
p("2b. Same, but Malibu's unallocated recurring corporate spread by net-sales share (CONVENTION, ours: Malibu's own allocation key")
p("    for the part it does allocate is 'proportionate budgeted net sales'; actual sales used). MasterCraft left as filed, all-in, so this still favours Malibu.")
for y in (2023, 2024, 2025, 2026):
    s, e, tot, ts = mb_seg[y]; corp = tot - mb_cons_adj[y]; sh = s / ts; ms, me = mc_adj[y]
    p(f"   FY{y}: share {sh:5.3f}; Malibu ({e:,} - {sh*corp:,.0f})/{s:,} = {pct(e-sh*corp,s):5.1f}%   MasterCraft {pct(me,ms):5.1f}%")
p("")
p("3. GAAP BASIS, the definition step 2 names for MasterCraft: segment operating income + segment D&A (stock pay and one-offs included).")
p("   MasterCraft, every year:")
for y in sorted(mc_gaap):
    s, oi, da, src = mc_gaap[y]
    p(f"   FY{y}: ({oi:,} + {da:,})/{s:,} = {pct(oi+da,s):5.1f}%   [{src}]")
p("   Malibu, old segment basis FY2019-FY2024 (segment pre-tax + segment D&A; every corporate cost and interest allocated to segments by the filer):")
for y in sorted(mb_old):
    s, da, pt = mb_old[y]
    line = f"   FY{y}: ({pt:,} + {da:,})/{s:,} = {pct(pt+da,s):5.1f}%"
    if y == 2023:
        line += f"   (before the $100.0M Batchelder settlement charged in FY2023: {pct(pt+da+BATCHELDER_FY2023,s):5.1f}%; the filing does not say which segment carried it, the drop in Malibu pre-tax implies the Malibu segment)"
    p(line)
p("   Residual on the old basis: Malibu's segment pre-tax is after interest and other non-operating items, which MasterCraft's operating income is not.")
p("   Upper bound for Malibu: add back ALL consolidated interest expense and other (income) expense to the Malibu segment")
p("   (10-K FY2020 0001590976-20-000069 for FY2019-20; 10-K FY2022 0001590976-22-000050 for FY2021-22):")
mb_nonop = {2019: 6464 + 6315, 2020: 3888 + 1578, 2021: 2529 + 1514, 2022: 2875 + 3858}
for y in sorted(mb_nonop):
    s, da, pt = mb_old[y]; ms, oi, mda, _ = mc_gaap[y]
    lo, hi = pct(pt + da, s), pct(pt + da + mb_nonop[y], s)
    p(f"   FY{y}: Malibu {lo:5.1f}% to {hi:5.1f}%   MasterCraft {pct(oi+mda,ms):5.1f}%")
p("   Malibu, new basis FY2024-FY2026: corporate cost at the operating level = segment total - depreciation - amortization - impairment/abandonment - operating income.")
for y in (2024, 2025, 2026):
    s, e, tot, ts = mb_seg[y]
    corp_op = tot - mb_dep[y] - mb_amort[y] - mb_other_opex_excl[y] - mb_opinc[y]
    sh = s / ts
    p(f"   FY{y}: corporate at operating level {corp_op:,}; all charged to Malibu (MasterCraft's rule): ({e:,} - {corp_op:,})/{s:,} = {pct(e-corp_op,s):5.1f}%;"
      f" by sales share {sh:5.3f}: ({e:,} - {sh*corp_op:,.0f})/{s:,} = {pct(e-sh*corp_op,s):5.1f}%")
s, oi, da, _ = mc_gaap[2026]
p(f"   MasterCraft FY2026 for comparison: {pct(oi+da,s):5.1f}% with all corporate and the ${mc_deal_costs_2026:,}K deal costs in the wake segment.")
reall = mc_deal_costs_2026 * (1 - s / mc_total_sales_2026)
p(f"   If only MasterCraft's deal costs are spread by sales share ({s/mc_total_sales_2026:5.3f}), its wake segment regains {reall:,.0f}: ({oi+da:,} + {reall:,.0f})/{s:,} = {pct(oi+da+reall,s):5.1f}%"
  " (a floor: its other corporate overhead is not disclosed and would move the same way).")
p("")
p("4. FY2026 VERDICT ARITHMETIC (the OUT fact: Malibu FY2026 margin on MasterCraft's definition at or below MasterCraft's FY2026):")
s, e, tot, ts = mb_seg[2026]; ms, me = mc_adj[2026]
corp_adj = tot - mb_cons_adj[2026]; corp_op = tot - mb_dep[2026] - mb_amort[2026] - mb_opinc[2026]; sh = s / ts
s2, oi, da, _ = mc_gaap[2026]
rows = [
    ("Adjusted, as filed (Malibu favoured)", pct(e, s), pct(me, ms)),
    ("Adjusted, MasterCraft's corporate rule mirrored", pct(e - corp_adj, s), pct(me, ms)),
    ("Adjusted, Malibu corporate by sales, MasterCraft all-in (Malibu favoured)", pct(e - sh*corp_adj, s), pct(me, ms)),
    ("GAAP op income + D&A, MasterCraft's corporate rule mirrored", pct(e - corp_op, s), pct(oi+da, s2)),
    ("GAAP, both spread by sales (MasterCraft: deal costs only, a floor)", pct(e - sh*corp_op, s), pct(oi+da+reall, s2)),
    ("GAAP, Malibu by sales, MasterCraft all-in (asymmetric, Malibu favoured)", pct(e - sh*corp_op, s), pct(oi+da, s2)),
]
for name, a, b in rows:
    p(f"   {name:<78} Malibu {a:5.1f}%  MasterCraft {b:5.1f}%  {'Malibu AT OR BELOW' if a <= b else 'Malibu ABOVE'}")
p("   The last row is not a same-definition comparison (each company's corporate cost is treated differently) and is shown only because it is the one row where Malibu is above.")

open(__file__.replace("r2_compute.py", "r2_output.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
