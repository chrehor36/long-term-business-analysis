import csv, os, itertools, statistics, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
REBAL = datetime.date(2018, 6, 30)
TODAY = datetime.date(2026, 7, 22)
YEARS = (TODAY - REBAL).days / 365.25

SURVIVORS = ['ORLY','GOOG','BKNG','AAPL','FAST','CMCSA','MA','WMT','CME','NVDA',
             'NEE','CSX','APH','USB','AFL','V','TJX','PNC']  # RTN removed: corrected data shows it FAILS Book One (see correction note)

port = {r["ticker"]: float(r["total_return"]) for r in csv.DictReader(open(os.path.join(SCRATCH, "portfolio_returns.csv")))}
returns = {t: port[t] for t in SURVIVORS}

SPY_TOTAL = 749.83 / 240.19 - 1.0
SPY_CAGR = (1 + SPY_TOTAL) ** (1/YEARS) - 1

def cagr_of(tickers):
    mult = statistics.mean(1 + returns[t] for t in tickers)
    return mult ** (1/YEARS) - 1

all_cagrs = []
combos = list(itertools.combinations(SURVIVORS, 10))
print(f"Full-gate survivors: {len(SURVIVORS)}")
print(f"Every possible 10-name portfolio: C({len(SURVIVORS)},10) = {len(combos)}")
print(f"SPY same window: {SPY_TOTAL*100:.1f}% total, {SPY_CAGR*100:.2f}% CAGR\n")

for combo in combos:
    all_cagrs.append(cagr_of(combo))

beat = sum(1 for c in all_cagrs if c > SPY_CAGR)
print(f"=== EVERY possible 10-name portfolio from the 19 full-gate survivors ===")
print(f"Beat SPY: {beat} / {len(all_cagrs)}  ({beat/len(all_cagrs)*100:.1f}%)")
print(f"Mean CAGR:   {statistics.mean(all_cagrs)*100:.2f}%")
print(f"Median CAGR: {statistics.median(all_cagrs)*100:.2f}%")
print(f"Stdev:       {statistics.stdev(all_cagrs)*100:.2f} pts")
print(f"Min / Max:   {min(all_cagrs)*100:.2f}% / {max(all_cagrs)*100:.2f}%")
qs = statistics.quantiles(all_cagrs, n=10)
print(f"10th/25th/75th/90th pctile: {qs[0]*100:.2f}% / {qs[2]*100:.2f}% / {qs[6]*100:.2f}% / {qs[8]*100:.2f}%")

# worst and best combos
ranked = sorted(zip(combos, all_cagrs), key=lambda x: x[1])
print("\nWorst portfolio (all 19-survivor universe):")
print(f"  CAGR={ranked[0][1]*100:.2f}%  {sorted(ranked[0][0])}")
print("Best portfolio:")
print(f"  CAGR={ranked[-1][1]*100:.2f}%  {sorted(ranked[-1][0])}")

# equal-weight ALL 19 survivors together (n=19, not 10) as a reference point
all19_cagr = cagr_of(SURVIVORS)
print(f"\nAll 19 survivors, equal-weight (reference, not a '10-name' portfolio): {all19_cagr*100:.2f}% CAGR")

# individual survivor returns, for context
print("\nIndividual survivor CAGRs:")
for t in sorted(SURVIVORS, key=lambda t: -returns[t]):
    ind_cagr = (1+returns[t])**(1/YEARS) - 1
    print(f"  {t:6s} {ind_cagr*100:7.2f}%")

with open(os.path.join(SCRATCH, "full_gate_all_10_portfolios.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tickers", "cagr"])
    for combo, c in zip(combos, all_cagrs):
        w.writerow([" ".join(sorted(combo)), c])
