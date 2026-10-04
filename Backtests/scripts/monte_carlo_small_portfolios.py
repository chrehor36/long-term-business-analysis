import csv, os, random, statistics, datetime, sys

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
REBAL = datetime.date(2018, 6, 30)
TODAY = datetime.date(2026, 7, 22)
YEARS = (TODAY - REBAL).days / 365.25

port = list(csv.DictReader(open(os.path.join(SCRATCH, "portfolio_returns.csv"))))
returns = {r["ticker"]: float(r["total_return"]) for r in port}
tickers = sorted(returns.keys())
print(f"Passer pool: {len(tickers)} names, all entered {REBAL}, held to {TODAY} ({YEARS:.2f} yrs)")

SPY_TOTAL = 749.83 / 240.19 - 1.0
SPY_CAGR = (1 + SPY_TOTAL) ** (1/YEARS) - 1
print(f"SPY same window: {SPY_TOTAL*100:.1f}% total, {SPY_CAGR*100:.2f}% CAGR\n")

def port_cagr(sample):
    mult = statistics.mean(1 + returns[t] for t in sample)
    return mult ** (1/YEARS) - 1

N_PORTFOLIOS = 500
rng = random.Random(42)
seen = set()
portfolios = []
attempts = 0
while len(portfolios) < N_PORTFOLIOS and attempts < N_PORTFOLIOS * 30:
    attempts += 1
    n = rng.choice([9, 10, 11])
    sample = tuple(sorted(rng.sample(tickers, n)))
    if sample in seen:
        continue
    seen.add(sample)
    portfolios.append(sample)

cagrs = [port_cagr(p) for p in portfolios]
beat = sum(1 for c in cagrs if c > SPY_CAGR)

print(f"=== {len(portfolios)} random portfolios, 9-11 names each, drawn from the 142 point-in-time passers ===")
print(f"Beat SPY: {beat} / {len(portfolios)}  ({beat/len(portfolios)*100:.1f}%)")
print(f"Mean portfolio CAGR:   {statistics.mean(cagrs)*100:.2f}%")
print(f"Median portfolio CAGR: {statistics.median(cagrs)*100:.2f}%")
print(f"Stdev of CAGR:         {statistics.stdev(cagrs)*100:.2f} pts")
print(f"Min / Max CAGR:        {min(cagrs)*100:.2f}% / {max(cagrs)*100:.2f}%")
qs = statistics.quantiles(cagrs, n=10)
print(f"10th/25th/75th/90th pctile CAGR: {qs[0]*100:.2f}% / {qs[2]*100:.2f}% / {qs[6]*100:.2f}% / {qs[8]*100:.2f}%")

# worst and best portfolios, for inspection
ranked = sorted(zip(portfolios, cagrs), key=lambda x: x[1])
print("\nWorst 3 random portfolios:")
for p, c in ranked[:3]:
    print(f"  CAGR={c*100:6.2f}%  {list(p)}")
print("Best 3 random portfolios:")
for p, c in ranked[-3:]:
    print(f"  CAGR={c*100:6.2f}%  {list(p)}")

# how many portfolios contain each of the big winners, for context
winners = ["NVDA", "KLAC", "LRCX", "PWR"]
for w in winners:
    n_containing = sum(1 for p in portfolios if w in p)
    print(f"\nPortfolios containing {w}: {n_containing} ({n_containing/len(portfolios)*100:.1f}%)")

# Beat rate EXCLUDING portfolios that happen to contain any of the top-4 outlier winners
no_outlier = [(p, c) for p, c in zip(portfolios, cagrs) if not any(w in p for w in winners)]
if no_outlier:
    c2 = [c for _, c in no_outlier]
    beat2 = sum(1 for c in c2 if c > SPY_CAGR)
    print(f"\n=== Portfolios containing NONE of NVDA/KLAC/LRCX/PWR ({len(no_outlier)} of {len(portfolios)}) ===")
    print(f"Beat SPY: {beat2} / {len(no_outlier)} ({beat2/len(no_outlier)*100:.1f}%)")
    print(f"Mean CAGR: {statistics.mean(c2)*100:.2f}%  Median CAGR: {statistics.median(c2)*100:.2f}%")

with open(os.path.join(SCRATCH, "monte_carlo_results.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["portfolio_tickers", "cagr"])
    for p, c in zip(portfolios, cagrs):
        w.writerow([" ".join(p), c])
