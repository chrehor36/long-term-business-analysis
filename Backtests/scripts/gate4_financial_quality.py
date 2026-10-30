import json, os, csv, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
REBAL = datetime.date(2018, 6, 30)

TICKERS = ['TSN','ORLY','GOOG','BKNG','KLAC','AAPL','BBWI','FAST','LYB','CMCSA','MA','BEN','F',
           'WMT','CME','NVDA','NEE','TGNA','IVZ','LNC','GME','CSX','FITB','APH','WFC','HRB','CMG',
           'USB','HPQ','CVS','HOG','AN','AFL','OMC','V','PBI','RTX','PDCO','STT','TJX','KR','PNC',
           'GPS','MO','PFG']

# financial businesses -> leverage-ceiling track; else -> survival track
FINANCIAL = {'MA','BEN','CME','LNC','FITB','WFC','USB','AFL','V','STT','PNC','PFG','AN'}
# AN (AutoNation) is a dealer, not financial -- captive finance arm only; keep as non-financial.
FINANCIAL.discard('AN')

NI_TAGS = ["NetIncomeLoss", "ProfitLoss"]
DA_TAGS = ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
           "DepreciationAndAmortization", "Depreciation"]
CAPEX_TAGS = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsForCapitalImprovements",
              "PaymentsToAcquireProductiveAssets"]
WC_TAGS = ["IncreaseDecreaseInOperatingCapital"]
ASSETS_TAGS = ["Assets"]
EQUITY_TAGS = ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]
DEBT_TAGS = ["LongTermDebtNoncurrent", "LongTermDebt"]
CASH_TAGS = ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]

def annual_points(gaap, tags, unit="USD", min_dur=300, max_dur=380):
    """Latest-available-as-of-REBAL annual (10-K) points per fiscal end, earliest-filed kept."""
    by_end = {}
    for tag in tags:
        if tag not in gaap:
            continue
        for x in gaap[tag]["units"].get(unit, []):
            if x.get("form") not in ("10-K", "10-K/A"):
                continue
            s, e, f = x.get("start"), x.get("end"), x.get("filed")
            if not (s and e and f):
                continue
            sd, ed = datetime.date.fromisoformat(s), datetime.date.fromisoformat(e)
            if not (min_dur <= (ed - sd).days <= max_dur):
                continue
            fd = datetime.date.fromisoformat(f)
            if fd > REBAL or ed > REBAL:
                continue
            prev = by_end.get(ed)
            if prev is None or fd < prev[1]:
                by_end[ed] = (x["val"], fd)
    return by_end

def instant_points(gaap, tags, unit="USD"):
    """Latest balance-sheet point as of REBAL (10-K or 10-Q, point-in-time instant)."""
    by_end = {}
    for tag in tags:
        if tag not in gaap:
            continue
        for x in gaap[tag]["units"].get(unit, []):
            if x.get("form") not in ("10-K", "10-K/A", "10-Q", "10-Q/A"):
                continue
            e, f = x.get("end"), x.get("filed")
            if not (e and f):
                continue
            ed = datetime.date.fromisoformat(e)
            fd = datetime.date.fromisoformat(f)
            if fd > REBAL:
                continue
            prev = by_end.get(ed)
            if prev is None or fd < prev[1]:
                by_end[ed] = (x["val"], fd)
    return by_end

def latest_instant(gaap, tags):
    pts = instant_points(gaap, tags)
    if not pts:
        return None, None
    end = max(pts.keys())
    return pts[end][0], end

results = []
for t in TICKERS:
    fd = json.load(open(os.path.join(CACHE, f"facts_{t}.json")))
    gaap = fd.get("facts", {}).get("us-gaap", {})

    ni = annual_points(gaap, NI_TAGS)
    da = annual_points(gaap, DA_TAGS)
    capex = annual_points(gaap, CAPEX_TAGS)
    wc = annual_points(gaap, WC_TAGS)

    common_ends = sorted(set(ni) & set(da) & set(capex))
    oe_years = []
    oe_method = "full"
    for e in common_ends[-5:]:
        n = ni[e][0]
        d = da[e][0]
        c = capex[e][0]
        w = wc[e][0] if e in wc else 0  # working-capital tag frequently absent; 0 if not disclosed, flagged
        oe = n + d - c - w
        oe_years.append((e, oe, n, d, c, w, e in wc))

    if not oe_years and t not in FINANCIAL:
        # fallback for non-standard D&A tagging (e.g. GOOG, NEE use extension
        # tags this script's fixed list doesn't match): operating cash flow
        # minus total capex is a defensible FCF-based OE proxy -- it already
        # embeds the D&A add-back, at the cost of the same maintenance-vs-
        # growth-capex simplification the full formula makes when the split
        # isn't separately disclosed anyway. Labeled, not silently swapped.
        ocf = annual_points(gaap, ["NetCashProvidedByUsedInOperatingActivities"])
        common_ends2 = sorted(set(ocf) & set(capex))
        for e in common_ends2[-5:]:
            o = ocf[e][0]
            c = capex[e][0]
            oe = o - c
            oe_years.append((e, oe, o, None, c, 0, False))
        if oe_years:
            oe_method = "OCF-minus-capex (fallback -- D&A tag not found)"

    is_fin = t in FINANCIAL
    assets, a_end = latest_instant(gaap, ASSETS_TAGS)
    equity, e_end = latest_instant(gaap, EQUITY_TAGS)
    debt, d_end = latest_instant(gaap, DEBT_TAGS)
    cash, c_end = latest_instant(gaap, CASH_TAGS)

    leverage = (assets / equity) if (assets and equity) else None
    fortress_pass = None
    fortress_note = ""
    if is_fin:
        if leverage is not None:
            fortress_pass = leverage <= 10.0
            fortress_note = f"assets/equity={leverage:.1f}:1"
        else:
            fortress_note = "assets or equity data missing"
    else:
        # crude survival-track proxy: debt due vs cash+equity isn't fully computable
        # mechanically (needs maturity schedule + credit rating, both qualitative) --
        # flag ordinary leverage (debt/equity) for the qualitative agent to finish,
        # don't auto-pass/fail non-financials mechanically.
        if debt is not None and equity:
            fortress_note = f"debt/equity={debt/equity:.2f} (mechanical proxy only -- needs credit rating + maturity schedule for a real verdict)"

    results.append({
        "ticker": t, "is_financial": is_fin,
        "oe_years": oe_years,
        "oe_method": oe_method,
        "n_oe_years": len(oe_years),
        "lowest_oe": min((v[1] for v in oe_years), default=None),
        "assets": assets, "equity": equity, "debt": debt, "cash": cash,
        "leverage_ratio": leverage, "fortress_mechanical_pass": fortress_pass,
        "fortress_note": fortress_note,
    })

with open(os.path.join(SCRATCH, "gate4_results.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker","is_financial","n_oe_years","lowest_oe","assets","equity","debt","cash",
                "leverage_ratio","fortress_mechanical_pass","fortress_note"])
    for r in results:
        w.writerow([r["ticker"], r["is_financial"], r["n_oe_years"], r["lowest_oe"], r["assets"],
                    r["equity"], r["debt"], r["cash"], r["leverage_ratio"], r["fortress_mechanical_pass"],
                    r["fortress_note"]])

json.dump(results, open(os.path.join(SCRATCH, "gate4_results_full.json"), "w"), indent=1, default=str)

print(f"Processed {len(results)} tickers")
for r in results:
    print(f"{r['ticker']:6s} fin={str(r['is_financial'])[0]} OE_yrs={r['n_oe_years']} "
          f"lowest_OE={r['lowest_oe']} | {r['fortress_note']}")
