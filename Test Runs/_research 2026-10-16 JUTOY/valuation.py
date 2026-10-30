# COMPUTATION, NOT A CLEARANCE (the file closed at Q2). Arithmetic for the two reporting figures.
# Inputs from owner_cash.py (filed cash-flow statements) and the 30 June 2026 interim balance sheet.
import importlib.util, io, contextlib, os
spec = importlib.util.spec_from_file_location("oc", os.path.join(os.path.dirname(__file__), "owner_cash.py"))
oc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(oc)

SHARES = 2_488_835_287          # Monthly Return FF301, month ended 30 Sep 2026
HKD_CNY = 0.85658               # CFETS central parity, 2026-10-16 (RMB per HK$1)
USD_CNY = 6.7220                # CFETS central parity, 2026-10-16
PRICE_HKD = 0.38                # 3303.HK last, 2026-10-16 (aggregator, flagged)
ADR = 250                       # ordinary shares per ADS (Form F-6EF)
R = 0.0206                      # PRC MOF 30-year treasury yield, 2026-10-16
FLOOR = 0.10

# Net debt at 30 June 2026 (RMB'000), as the interim balance sheet states it
cash, fvtpl, pledged = 641_157, 81_394, 53_757
borrow = 182_871 + 294_528 + 2_520
leases = 7_492 + 13_824
net_cash = cash + fvtpl - borrow - leases          # pledged deposits left out (restricted), shown beside
print(f"net cash 30 Jun 2026 RMB'000 {net_cash:,} (pledged deposits {pledged:,} beside, excluded)")

def avg(xs): return sum(xs) / len(xs)
def dep_ppe(y):  # PPE depreciation + intangible amortisation (ROU depreciation left out: lease principal already charged)
    ppe = {2014: 25256, 2015: 28389, 2016: 31490, 2017: 31105, 2018: 121848, 2019: 103322, 2020: 128645, 2021: 143913,
           2022: 133390, 2023: 115417, 2024: 95775, 2025: 93608}[y]
    am = {2014: 1777, 2015: 1176, 2016: 1150, 2017: 1302, 2018: 780, 2019: 1079, 2020: 1345, 2021: 2009, 2022: 1928,
          2023: 1716, 2024: 1311, 2025: 1119}[y]
    return ppe + am

def bases(years):
    ae = avg([oc.oc_allequity(y) for y in years]); eq = avg([oc.oc_equity(y) for y in years])
    capx = avg([oc.capex[y] + oc.intang[y] for y in years]); dp = avg([dep_ppe(y) for y in years])
    return ae, eq, ae + capx - dp, eq + capx - dp, capx, dp

def per_share(total_rmb_k):
    rmb = total_rmb_k * 1000 / SHARES
    return rmb, rmb / HKD_CNY

def show(label, years):
    ae, eq, ae_d, eq_d, capx, dp = bases(years)
    print(f"\n== {label} {years[0]}-{years[-1]}: OC_ae {ae/1e3:.1f}M  OC_eq {eq/1e3:.1f}M  | dep variant OC_ae {ae_d/1e3:.1f}M OC_eq {eq_d/1e3:.1f}M  (capex {capx/1e3:.1f}M vs dep {dp/1e3:.1f}M)")
    for nm, flow, add in [("all-equity, all spending", ae, net_cash), ("all-equity, dep variant", ae_d, net_cash),
                          ("equity-only, all spending", eq, 0), ("equity-only, dep variant", eq_d, 0)]:
        v_sov = flow / R + add; v_10 = flow / FLOOR + add
        s_r, s_h = per_share(v_sov); f_r, f_h = per_share(v_10)
        print(f"  {nm:27s} value@2.06% RMB{s_r:.3f} HK${s_h:.3f} | @10% RMB{f_r:.3f} HK${f_h:.3f}")
    return ae, eq, ae_d, eq_d

mcap = PRICE_HKD * HKD_CNY * SHARES / 1000
ev = mcap - net_cash
print(f"price HK${PRICE_HKD} = RMB{PRICE_HKD*HKD_CNY:.4f}; market cap RMB'000 {mcap:,.0f}; EV {ev:,.0f}; per ADR HK${PRICE_HKD*ADR:.1f} = US${PRICE_HKD*ADR*HKD_CNY/USD_CNY:.2f}")

ae, eq, ae_d, eq_d = show("CYCLE BASE peak to peak (central)", [2021, 2022, 2023, 2024])
show("trough to trough prior cycle", [2019, 2020, 2021, 2022])
show("LITERAL WINDOW", [2021, 2022, 2023, 2024, 2025])
show("twelve years", list(range(2014, 2026)))

# The range on the cycle base: top = all spending, no growth; bottom = depreciation variant, no growth (run CONVENTION)
top_v = ae / R + net_cash; bot_v = ae_d / R + net_cash
print(f"\nRANGE (all-equity, at 2.06%): RMB{per_share(bot_v)[0]:.3f}-{per_share(top_v)[0]:.3f}  HK${per_share(bot_v)[1]:.3f}-{per_share(top_v)[1]:.3f}  width {top_v/bot_v:.2f}x")
print(f"   per ADR HK${per_share(bot_v)[1]*ADR:.1f}-{per_share(top_v)[1]*ADR:.1f}")
print(f"floor test at price: expected return on EV top {ae/ev:.1%} bottom {ae_d/ev:.1%}; equity-only top {eq/mcap:.1%} bottom {eq_d/mcap:.1%}")
fair_ae = (ae / FLOOR + ae_d / FLOOR) / 2 + net_cash
fair_eq = (eq / FLOOR + eq_d / FLOOR) / 2
fr, fh = per_share(fair_ae); er, eh = per_share(fair_eq)
print(f"FAIR all-equity RMB{fr:.3f} HK${fh:.3f} per ADR HK${fh*ADR:.1f} US${fh*ADR*HKD_CNY/USD_CNY:.2f}")
print(f"FAIR equity-only RMB{er:.3f} HK${eh:.3f} per ADR HK${eh*ADR:.1f} US${eh*ADR*HKD_CNY/USD_CNY:.2f}")
# H1 2026 owner cash, for the record (not in any base)
h1 = -148_214 - 125_851
print(f"H1 2026 CFO less PPE purchases RMB'000 {h1:,}")
