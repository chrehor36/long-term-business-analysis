import csv, os, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
REBAL = datetime.date(2018, 6, 30)
TODAY = datetime.date(2026, 7, 22)
YEARS = (TODAY - REBAL).days / 365.25

rows = list(csv.DictReader(open(os.path.join(SCRATCH, "sp500_2013_screen_results.csv"))))
port = list(csv.DictReader(open(os.path.join(SCRATCH, "portfolio_returns.csv"))))
port_by_t = {r["ticker"]: float(r["total_return"]) for r in port}
yields = {r["ticker"]: float(r["yield"]) for r in rows if r["passed"] == "True"}
ranked = sorted(yields.items(), key=lambda x: -x[1])

def portfolio_cagr(tickers):
    rets = [port_by_t[t] for t in tickers if t in port_by_t]
    avg = sum(rets) / len(rets)
    cagr = (1 + avg) ** (1/YEARS) - 1
    return avg, cagr, len(rets)

spy_ret = 749.83 / 240.19 - 1.0
spy_cagr = (1 + spy_ret) ** (1/YEARS) - 1
print(f"SPY (same window): total {spy_ret*100:.1f}%  CAGR {spy_cagr*100:.2f}%\n")

for label, tickers in [
    ("All 142 passers (equal-weight)", [t for t,_ in ranked]),
    ("Top 10 by yield (incl. AIV)", [t for t,_ in ranked[:10]]),
    ("Top 20 by yield (incl. AIV)", [t for t,_ in ranked[:20]]),
    ("Top 30 by yield (incl. AIV)", [t for t,_ in ranked[:30]]),
    ("Top 10 by yield (ex. AIV)", [t for t,_ in ranked if t != "AIV"][:10]),
    ("Top 20 by yield (ex. AIV)", [t for t,_ in ranked if t != "AIV"][:20]),
    ("Top 30 by yield (ex. AIV)", [t for t,_ in ranked if t != "AIV"][:30]),
]:
    avg, cagr, n = portfolio_cagr(tickers)
    print(f"{label:36s}  n={n:3d}  total={avg*100:8.1f}%  CAGR={cagr*100:6.2f}%  vs SPY={cagr-spy_cagr:+.2f} pts/yr")

print()
for label, tickers in [
    ("Top 10 ex. AIV", [t for t,_ in ranked if t != "AIV"][:10]),
    ("Top 20 ex. AIV", [t for t,_ in ranked if t != "AIV"][:20]),
]:
    print(f"\n{label} constituents:")
    for t in tickers:
        r = port_by_t.get(t)
        y = yields[t]
        print(f"  {t:6s} entry-yield={y*100:5.2f}%  total_return={r*100 if r is not None else float('nan'):8.1f}%")
