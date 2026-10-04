import json, os, csv, datetime, sys

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
REBAL = datetime.date.fromisoformat(sys.argv[1])
LABEL = sys.argv[2]

TICKERS = json.load(open(os.path.join(SCRATCH, f"top45_{LABEL}.json")))
FINANCIAL = set(json.load(open(os.path.join(SCRATCH, f"financial_set_{LABEL}.json"))))

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
missing_facts = []
for t in TICKERS:
    fn = os.path.join(CACHE, f"facts_{t}.json")
    if not os.path.exists(fn):
        missing_facts.append(t)
        continue
    fd = json.load(open(fn))
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
        w = wc[e][0] if e in wc else 0
        oe = n + d - c - w
        oe_years.append((e, oe, n, d, c, w, e in wc))

    if not oe_years and t not in FINANCIAL:
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
        if debt is not None and equity:
            fortress_note = f"debt/equity={debt/equity:.2f} (mechanical proxy only)"

    results.append({
        "ticker": t, "is_financial": is_fin,
        "oe_years": oe_years, "oe_method": oe_method,
        "n_oe_years": len(oe_years),
        "lowest_oe": min((v[1] for v in oe_years), default=None),
        "assets": assets, "equity": equity, "debt": debt, "cash": cash,
        "leverage_ratio": leverage, "fortress_mechanical_pass": fortress_pass,
        "fortress_note": fortress_note,
    })

with open(os.path.join(SCRATCH, f"gate4_results_{LABEL}.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker","is_financial","n_oe_years","lowest_oe","assets","equity","debt","cash",
                "leverage_ratio","fortress_mechanical_pass","fortress_note"])
    for r in results:
        w.writerow([r["ticker"], r["is_financial"], r["n_oe_years"], r["lowest_oe"], r["assets"],
                    r["equity"], r["debt"], r["cash"], r["leverage_ratio"], r["fortress_mechanical_pass"],
                    r["fortress_note"]])

json.dump(results, open(os.path.join(SCRATCH, f"gate4_results_full_{LABEL}.json"), "w"), indent=1, default=str)

print(f"Processed {len(results)} tickers ({len(missing_facts)} missing companyfacts: {missing_facts})")
for r in results:
    print(f"{r['ticker']:6s} fin={str(r['is_financial'])[0]} OE_yrs={r['n_oe_years']} "
          f"lowest_OE={r['lowest_oe']} | {r['fortress_note']}")
