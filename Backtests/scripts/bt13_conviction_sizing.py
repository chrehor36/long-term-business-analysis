import csv, os, datetime, statistics

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"

# ---- Moat classifications, from the real Gate 2 research already done in
# BT-10 and BT-11 (WIDE / NARROW as stated in each agent's writeup) ----
MOAT_2018 = {
    "AAPL": "WIDE", "GOOG": "WIDE", "BKNG": "WIDE", "ORLY": "WIDE", "FAST": "NARROW",
    "CMCSA": "WIDE", "MA": "WIDE", "WMT": "WIDE", "CME": "WIDE", "NVDA": "WIDE",
    "NEE": "WIDE", "CSX": "WIDE", "APH": "WIDE", "USB": "NARROW", "AFL": "WIDE",
    "V": "WIDE", "TJX": "WIDE", "PNC": "NARROW",
}
MOAT_1993 = {
    "WEC": "NARROW", "MMM": "WIDE", "WFC": "NARROW", "GL": "WIDE", "EMR": "NARROW",
    "HBAN": "NARROW", "NTRS": "WIDE", "HRB": "NARROW", "PCAR": "NARROW", "MCD": "WIDE",
    "GWW": "WIDE", "STT": "WIDE",
}
MOAT_MULT = {"WIDE": 2.0, "NARROW": 1.0}

HURDLE_2018 = 0.0400
HURDLE_1993 = 0.0635

YEARS_2018 = (datetime.date(2026, 7, 22) - datetime.date(2018, 6, 30)).days / 365.25
YEARS_1993 = (datetime.date(2026, 7, 24) - datetime.date(1993, 12, 31)).days / 365.25
SPY_2018_CAGR = 0.1517
SPY_1993_CAGR = 0.1073

def conviction_weights(yields, hurdle, moat_map):
    scores = {}
    for t, y in yields.items():
        margin = max(y - hurdle, 0.001)  # margin above hurdle; floor to avoid zero/negative weight
        scores[t] = margin * MOAT_MULT[moat_map[t]]
    total = sum(scores.values())
    return {t: s / total for t, s in scores.items()}

def moat_only_weights(tickers, moat_map):
    scores = {t: MOAT_MULT[moat_map[t]] for t in tickers}
    total = sum(scores.values())
    return {t: s / total for t, s in scores.items()}

def report(label, tickers, yields, hurdle, moat_map, returns, years, spy_cagr):
    weights_eq = {t: 1 / len(tickers) for t in tickers}
    weights_cw = conviction_weights(yields, hurdle, moat_map)

    print(f"\n=== {label} ===")
    print(f"{'Ticker':8s}{'Moat':8s}{'Yield':>8s}{'Margin':>8s}{'EqWt':>8s}{'ConvWt':>8s}{'CAGR':>8s}")
    for t in sorted(tickers, key=lambda t: -weights_cw[t]):
        y = yields[t]
        cagr = (1 + returns[t]) ** (1 / years) - 1
        print(f"{t:8s}{moat_map[t]:8s}{y*100:7.2f}%{(y-hurdle)*100:7.2f}%{weights_eq[t]*100:7.2f}%{weights_cw[t]*100:7.2f}%{cagr*100:7.2f}%")

    weights_mo = moat_only_weights(tickers, moat_map)
    eq_mult = sum(weights_eq[t] * (1 + returns[t]) for t in tickers)
    cw_mult = sum(weights_cw[t] * (1 + returns[t]) for t in tickers)
    mo_mult = sum(weights_mo[t] * (1 + returns[t]) for t in tickers)
    eq_cagr = eq_mult ** (1 / years) - 1
    cw_cagr = cw_mult ** (1 / years) - 1
    mo_cagr = mo_mult ** (1 / years) - 1
    print(f"\nEqual-weight CAGR:            {eq_cagr*100:.2f}%")
    print(f"Margin x Moat-weight CAGR:    {cw_cagr*100:.2f}%")
    print(f"Moat-ONLY-weight CAGR:        {mo_cagr*100:.2f}%")
    print(f"SPY CAGR:                     {spy_cagr*100:.2f}%")
    print(f"Margin x Moat vs equal:       {(cw_cagr-eq_cagr)*100:+.2f} pts/yr")
    print(f"Moat-only vs equal:           {(mo_cagr-eq_cagr)*100:+.2f} pts/yr")
    print(f"Moat-only vs SPY:             {(mo_cagr-spy_cagr)*100:+.2f} pts/yr")
    return eq_cagr, cw_cagr, mo_cagr

# ---- 2018 cohort (BT-10) ----
survivors_2018 = list(MOAT_2018.keys())
yields_2018 = {r["ticker"]: float(r["yield"]) for r in csv.DictReader(open(os.path.join(SCRATCH, "sp500_2013_screen_results.csv"))) if r["ticker"] in MOAT_2018}
returns_2018 = {r["ticker"]: float(r["total_return"]) for r in csv.DictReader(open(os.path.join(SCRATCH, "portfolio_returns.csv"))) if r["ticker"] in MOAT_2018}
report("2018 COHORT (18 full-gate survivors, BT-10)", survivors_2018, yields_2018, HURDLE_2018, MOAT_2018, returns_2018, YEARS_2018, SPY_2018_CAGR)

# ---- 1993 cohort, STATIC (BT-11, no rotation) ----
survivors_1993 = list(MOAT_1993.keys())
yields_1993 = {r["ticker"]: float(r["yield"]) for r in csv.DictReader(open(os.path.join(SCRATCH, "screen_1990s_results.csv"))) if r["ticker"] in MOAT_1993}
returns_1993_static = {r["ticker"]: float(r["total_return"]) for r in csv.DictReader(open(os.path.join(SCRATCH, "returns_1990s.csv"))) if r["ticker"] in MOAT_1993}
report("1993 COHORT, STATIC HOLD (12 survivors, BT-11 methodology)", survivors_1993, yields_1993, HURDLE_1993, MOAT_1993, returns_1993_static, YEARS_1993, SPY_1993_CAGR)
