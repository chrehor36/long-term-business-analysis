# Owner cash and the Q7 COMPUTATION for GRFXY (Graphex Group, HKSE 6128), HK$'000.
# Every input is read from the consolidated statement of cash flows of the annual report named beside it
# (HKEXnews PDFs, text extracted with pdftotext -raw into cache/, which is not committed).
# COMPUTATION, NOT A CLEARANCE: the run closed at Q1.

years = [2021, 2022, 2023, 2024, 2025]
src = {2021: "AR2021 (HKEX 2022-04-28)", 2022: "AR2022 (HKEX 2023-04-27)", 2023: "AR2023 (HKEX 2024-04-29)",
       2024: "AR2024 (HKEX 2025-04-29)", 2025: "AR2025 (HKEX 2026-04-30)"}
cfo      = {2021: -12850, 2022: 64942, 2023: -11156, 2024: -5312, 2025: -9787}   # net cash flows from operating activities (after tax paid; interest paid is in financing)
ppe      = {2021: 811, 2022: 429, 2023: 738, 2024: 152, 2025: 74}                # purchases of property, plant and equipment
intang   = {2021: 943, 2022: 393, 2023: 424, 2024: 318, 2025: 323}               # purchases of other intangible assets
deposits = {2021: 0, 2022: 0, 2023: 0, 2024: 0, 2025: 40795}                     # deposits for PPE (the Anhui anode plant: growth spending)
lease    = {2021: 11280, 2022: 8247, 2023: 5264, 2024: 4879, 2025: 4804}         # repayment of lease liabilities (principal)
sbc      = {2021: 14067, 2022: 0, 2023: 16433, 2024: 14009, 2025: 12}            # equity-settled share-based payment added back in CFO
interest = {2021: 17398, 2022: 23280, 2023: 3621, 2024: 5230, 2025: 14094}       # interest paid (financing section)

allsp, maint, eq_maint, eq_all = {}, {}, {}, {}
print("year  CFO   capex  deposits lease  SBC  | owner cash all-spending | maintenance | equity-only (maint) | source")
for y in years:
    base = cfo[y] - ppe[y] - intang[y] - lease[y] - sbc[y]
    maint[y] = base
    allsp[y] = base - deposits[y]
    eq_maint[y] = base - interest[y]
    eq_all[y] = allsp[y] - interest[y]
    print(y, cfo[y], ppe[y] + intang[y], deposits[y], lease[y], sbc[y], "|", allsp[y], "|", maint[y], "|", eq_maint[y], "|", src[y])

avg = lambda d: sum(d.values()) / len(d)
a_all, a_m, a_em, a_ea = avg(allsp), avg(maint), avg(eq_maint), avg(eq_all)
print("five-year averages: all-spending %.0f, maintenance %.0f, equity-only maintenance %.0f, equity-only all %.0f" % (a_all, a_m, a_em, a_ea))

# Growth, specific (b): the series changes sign (2022 positive, the others negative), so the end-year rate is meaningless;
# halves: first half 2021-2022, second half 2024-2025.
h1 = (maint[2021] + maint[2022]) / 2
h2 = (maint[2024] + maint[2025]) / 2
print("halves (maintenance): first %.0f, second %.0f -> sign change, meaningless; range is the no-growth case alone" % (h1, h2))

shares = 941313336            # ordinary shares, monthly return for September 2026 (HKEX 2026-10-02), no treasury shares
rate = 0.0207                 # PRC MoF 30-year treasury yield, 2026-10-12
price = 0.051                 # HK$ close 2026-10-13, aggregator (Yahoo 6128.HK), flagged
# Net debt at 30 June 2026 (Interim Report 2026, HKEX 2026-09-29), HK$'000:
borrow = 142250 + 23815; prom = 27963; conv = 3023; leases = 2884 + 11712; cash = 19436 + 554
nd_ex = borrow + prom + conv - cash
nd_in = nd_ex + leases
print("net debt 30 Jun 2026: ex leases %.0f; incl. IFRS 16 leases %.0f" % (nd_ex, nd_in))
print("market cap HK$'000: %.0f" % (shares * price / 1000))

def per_share(ev):
    return ev * 1000 / shares

for label, oc in [("central (maintenance, all-equity)", a_m), ("all-spending (literal window, all-equity)", a_all)]:
    v = oc / rate
    print("%s: business value at %.2f%%, zero growth = %.0f; per share less net debt ex leases HK$%.3f (incl leases HK$%.3f)"
          % (label, rate * 100, v, per_share(v - nd_ex), per_share(v - nd_in)))
print("equity-only (maintenance, after interest): value %.0f; per share HK$%.3f" % (a_em / rate, per_share(a_em / rate)))

# Fair price (Part VII): each end case at ten percent, averaged. Range is one case (no growth), so fair = that case at 10%.
fair_all_equity = per_share(a_m / 0.10 - nd_ex)
fair_eq_only = per_share(a_em / 0.10)
print("FAIR PRICE (reporting figure): all-equity HK$%.3f a share (incl leases HK$%.3f); equity-only HK$%.3f; price HK$%.3f"
      % (fair_all_equity, per_share(a_m / 0.10 - nd_in), fair_eq_only, price))
