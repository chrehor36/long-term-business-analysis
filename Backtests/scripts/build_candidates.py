"""Build corrected top-45-by-yield candidate lists + financial classification.

Inputs : v3b_screen_{yr}.csv (the CORRECTED screens)
Outputs: top45_{yr}.json, financial_set_{yr}.json, candidates_report.txt

Three guards, each added because the first pass produced a visibly wrong list:

1. DATA-QUALITY EXCLUSION from the public-float validator instead of a
   hardcoded KNOWN_BAD list. A computed market cap materially BELOW the filed
   public float is near-impossible (float is a subset of market cap), so it
   reliably marks a bad share count or a cover-page typo. Threshold is looser
   in the +/-200d window because six months of price drift can breach a tight
   band on its own (EXC 2013 is a known false alarm there).

2. IMPLAUSIBLE-YIELD GUARD. A worst-5yr owner-earnings yield above 50% implies
   a market cap under 2x trough earnings -- that does not happen to a real
   S&P 500 constituent, so it marks broken share/price data. This is what
   caught COL at 10,482% in 2019/2020: Rockwell Collins was ACQUIRED by UTC in
   November 2018, so it was not investable at those anchors at all, but its
   last-filed financials still satisfied the 5-year history test and a stale
   10-K-implied price slipped past the price-recency check. Yields between 20%
   and 50% are additionally required to be float-validated, since that band is
   where genuine distress (PBI ~20%) and broken data overlap.

3. FINANCIAL CLASSIFICATION from filings, but only on tags that actually mean
   "balance-sheet levered." The Fortress Test's hard 10:1 asset/equity ceiling
   is for banks, insurers and similar. Deliberately EXCLUDED from the tag set:
   FinancingReceivableAllowanceForCreditLosses and InterestAndDividendIncome-
   Operating (present for almost any firm with trade receivables or interest
   income -- they wrongly caught WMT, TGT, CSCO, DGX, ADM), and the
   LoansAndLeasesReceivable family (captive finance arms at DE/CAT/F, which are
   industrials, not financial institutions). Mislabelling an industrial as
   financial is the dangerous direction: it would impose a leverage ceiling
   that names like Ford would fail for reasons the rule was never aimed at.
"""
import csv, json, os

SCRATCH = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SCRATCH, "bt_cache")
FAILCACHE = os.path.join(CACHE, "failures")
YEARS = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
TOP_N = 45
MAX_PLAUSIBLE_YIELD = 0.50
FLOAT_REQUIRED_ABOVE = 0.20

FIN_TAGS = [
    "Deposits",                                   # banks
    "PremiumsEarnedNet",                          # insurers
    "PolicyholderBenefitsAndClaimsIncurredNet",
    "LiabilityForFuturePolicyBenefits",
    "SeparateAccountAssets",
    "DeferredPolicyAcquisitionCosts",
    "RealEstateInvestmentPropertyNet",            # REITs
    "RealEstateInvestmentPropertyAtCost",
]


def facts_path(t):
    for base in (CACHE, FAILCACHE):
        p = os.path.join(base, f"facts_{t}.json")
        if os.path.exists(p):
            return p
    return None


_fin_cache = {}


def is_financial(t):
    if t not in _fin_cache:
        p, verdict, hit = facts_path(t), False, None
        if p:
            try:
                gaap = json.load(open(p)).get("facts", {}).get("us-gaap", {})
                for tag in FIN_TAGS:
                    if tag in gaap:
                        verdict, hit = True, tag
                        break
            except Exception:
                pass
        _fin_cache[t] = (verdict, hit)
    return _fin_cache[t]


def screen_row(r):
    """Returns (keep: bool, reason_if_dropped: str)."""
    flag = r.get("cap_flag", "") or ""
    y = float(r["yield"])

    if flag.startswith("CAP_BELOW_FLOAT"):
        try:
            ratio = float(flag.split("(")[1].rstrip("x)"))
        except (IndexError, ValueError):
            return False, f"unparseable cap flag [{flag}]"
        limit = 0.25 if "_APPROX" in flag else 0.5
        if ratio < limit:
            return False, f"cap/float {ratio:.2f}x < {limit}"

    if y > MAX_PLAUSIBLE_YIELD:
        return False, f"implausible yield {y*100:.0f}% (broken price/shares)"

    if y > FLOAT_REQUIRED_ABOVE and flag == "NO_FLOAT_NEAR_ANCHOR":
        return False, f"yield {y*100:.1f}% unverifiable (no float near anchor)"

    return True, ""


report = []
for yr in YEARS:
    rows = [r for r in csv.DictReader(
        open(os.path.join(SCRATCH, f"v3b_screen_{yr}.csv")))
        if r["passed"] == "True"]

    kept, dropped = [], []
    for r in rows:
        ok, why = screen_row(r)
        (kept if ok else dropped).append(r if ok else (r["ticker"], why))

    for r in kept:
        r["_y"] = float(r["yield"])
    kept.sort(key=lambda r: -r["_y"])
    top = kept[:TOP_N]
    tickers = [r["ticker"] for r in top]

    fins, why_fin = [], {}
    for t in tickers:
        v, hit = is_financial(t)
        if v:
            fins.append(t)
            why_fin[t] = hit

    json.dump(tickers, open(os.path.join(SCRATCH, f"top45_{yr}.json"), "w"))
    json.dump(fins, open(os.path.join(SCRATCH, f"financial_set_{yr}.json"), "w"))

    lines = [f"=== {yr}-06-30 ===",
             f"  passers {len(rows)} | excluded {len(dropped)} | "
             f"pool {len(kept)} | taken {len(top)}"]
    for t, why in dropped:
        lines.append(f"    EXCLUDED {t:6s} {why}")
    lines.append(f"  yield range: {top[0]['_y']*100:.2f}% .. {top[-1]['_y']*100:.2f}%")
    lines.append(f"  financials ({len(fins)}): " +
                 ", ".join(f"{t}({why_fin[t][:20]})" for t in fins))
    lines.append("  candidates: " + " ".join(tickers))
    report.append("\n".join(lines))

out = "\n\n".join(report)
open(os.path.join(SCRATCH, "candidates_report.txt"), "w").write(out)
print(out)
