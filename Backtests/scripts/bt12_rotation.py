import csv, os, datetime, statistics

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
START = datetime.date(1993, 12, 31)
CHECKPOINT = datetime.date(2018, 6, 30)
END = datetime.date(2026, 7, 24)
YEARS_TOTAL = (END - START).days / 365.25

# The 12 BT-11 survivors, and their disposition at the 2018-06-30 checkpoint,
# per real Gate re-evaluation (not mechanical yield alone):
HELD = ["WEC", "MMM", "GL", "EMR", "HBAN", "NTRS", "PCAR", "MCD"]
SOLD = {
    # ticker: (period1_return 1993-2018, reason)
    "WFC":  (3.355, "Gate 3 FAIL -- 2016 fake-accounts scandal, Fed asset cap (per BT-10)"),
    "HRB":  (0.129, "Gate 2 FAIL -- DIY tax software eroding core moat (per BT-10)"),
    "STT":  (2.438, "Gate 4 FAIL -- Fortress leverage ceiling breached, 11.2:1 (per BT-10)"),
    "GWW":  (7.049, "Gate 2 FAIL -- Amazon Business forced 2017 pricing reset, margin/branch damage"),
}

# full 1993-2026 static returns (from BT-11), for the 8 HELD names
static_returns = {r["ticker"]: float(r["total_return"]) for r in csv.DictReader(open(os.path.join(SCRATCH, "returns_1990s.csv")))}

# 2018-2026 returns for the 18 rotation-destination tickers (BT-10's corrected full-gate survivors)
ROTATION_TARGETS = ['AAPL','GOOG','BKNG','ORLY','FAST','CMCSA','MA','WMT','CME','NVDA',
                     'NEE','CSX','APH','USB','AFL','V','TJX','PNC']
port_2018 = {r["ticker"]: float(r["total_return"]) for r in csv.DictReader(open(os.path.join(SCRATCH, "portfolio_returns.csv")))}
rotation_multiples = [1 + port_2018[t] for t in ROTATION_TARGETS]
avg_rotation_multiple = statistics.mean(rotation_multiples)
print(f"Rotation destination: {len(ROTATION_TARGETS)} BT-10 full-gate 2018 survivors, "
      f"average 2018-2026 multiple = {avg_rotation_multiple:.3f}x "
      f"({(avg_rotation_multiple**(1/((END-CHECKPOINT).days/365.25))-1)*100:.2f}% CAGR)")

print("\n=== HELD (no real thesis break found -- kept to today) ===")
held_multiples = []
for t in HELD:
    m = 1 + static_returns[t]
    held_multiples.append(m)
    print(f"  {t:6s} full-period multiple: {m:.2f}x")

print("\n=== SOLD at 2018 checkpoint, rotated into the 18-name 2018 survivor basket ===")
sold_final_multiples = []
for t, (period1_ret, reason) in SOLD.items():
    period1_mult = 1 + period1_ret
    final_mult = period1_mult * avg_rotation_multiple
    sold_final_multiples.append(final_mult)
    print(f"  {t:6s} 1993-2018 multiple: {period1_mult:.2f}x  x  rotation {avg_rotation_multiple:.2f}x  = {final_mult:.2f}x total")
    print(f"         reason: {reason}")

all_multiples = held_multiples + sold_final_multiples
port_total_mult = statistics.mean(all_multiples)
port_cagr = port_total_mult ** (1/YEARS_TOTAL) - 1
print(f"\n=== BT-12 ROTATED PORTFOLIO (12 slots: 8 held, 4 sold-and-rotated) ===")
print(f"Equal-weight final multiple: {port_total_mult:.2f}x")
print(f"CAGR over {YEARS_TOTAL:.2f} years: {port_cagr*100:.2f}%")

# compare to BT-11's static (no monitoring) result and to SPY
static_mult = statistics.mean(1 + static_returns[t] for t in HELD + list(SOLD.keys()))
static_cagr = static_mult ** (1/YEARS_TOTAL) - 1
spy_cagr = 0.1073  # from BT-11
print(f"\nBT-11 static-hold (same 12, no monitoring): {static_cagr*100:.2f}% CAGR")
print(f"BT-12 rotated (real Gate 7 monitoring applied): {port_cagr*100:.2f}% CAGR")
print(f"SPY, same window: {spy_cagr*100:.2f}% CAGR")
print(f"\nRotation improvement over static hold: {(port_cagr-static_cagr)*100:+.2f} pts/yr")
print(f"Still vs SPY: {(port_cagr-spy_cagr)*100:+.2f} pts/yr")
