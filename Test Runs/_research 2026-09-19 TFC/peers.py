"""TFC competitor row - ONE basis for every peer, computed from XBRL companyfacts.

The CCB run of 2026-09-19 recorded that a bank competitor row assembled from each filer's
own reported ratios is directionally but not decimally comparable, because the basis differs
by filer (all-deposit vs interest-bearing cost of deposits, TE vs not, etc). This script
computes four metrics on identical definitions for every peer, then the run cross-checks the
computed figure against the subject's own filed figure to show the method is sound.

Metrics, all from annual (FY) facts:
  ROTCE       = NI available to common / avg (common equity - goodwill - other intangibles)
  efficiency  = noninterest expense / (net interest income + noninterest income)
  cost of dep = interest expense on deposits / avg total deposits
  NIM proxy   = net interest income / avg total assets  (a common denominator, stated as such)
"""
import sys, os, json, urllib.request, time

sys.path.insert(0, os.path.join("C:/Users/chreh/OneDrive/Documents/BRK", "tools"))
import sources

D = os.path.dirname(os.path.abspath(__file__))

PEERS = ["TFC", "PNC", "USB", "FITB", "KEY", "RF", "CFG", "MTB", "HBAN"]

TAGS = {
    "ni_common": ["NetIncomeLossAvailableToCommonStockholdersBasic", "NetIncomeLoss"],
    "equity": ["StockholdersEquity"],
    "pref": ["PreferredStockValue", "PreferredStockValueOutstanding"],
    "goodwill": ["Goodwill"],
    "intang": ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"],
    "nii": ["InterestIncomeExpenseNet"],
    "nonii": ["NoninterestIncome", "RevenuesExcludingInterestAndDividends"],
    "nie": ["NoninterestExpense"],
    "int_dep": ["InterestExpenseDeposits", "InterestExpenseDepositLiabilities",
                "InterestExpenseDomesticDepositLiabilities"],
    "deposits": ["Deposits"],
    "assets": ["Assets"],
    "prov": ["ProvisionForLoanLeaseAndOtherLosses",
             "ProvisionForLoanAndLeaseLosses",
             "ProvisionForCreditLossesExpenseReversal",
             "ProvisionForLoanLossesExpensed"],
}


def facts(t):
    cik, name = sources.cik_for(t)
    p = os.path.join(D, "cf_%s.json" % t)
    if not os.path.exists(p) or os.path.getsize(p) < 5000:
        txt = sources.sec_facts(cik)
        if isinstance(txt, (dict, list)):
            txt = json.dumps(txt)
        open(p, "w", encoding="utf-8").write(txt)
        time.sleep(0.2)
    return name, json.loads(open(p, encoding="utf-8").read())


def duration(j, tags, fy):
    """Annual duration fact for fiscal year fy, latest vintage (recast wins)."""
    for tg in tags:
        node = j["facts"].get("us-gaap", {}).get(tg)
        if not node:
            continue
        best = None
        for unit, arr in node["units"].items():
            for it in arr:
                if it.get("form") not in ("10-K", "10-K/A"):
                    continue
                if it.get("fp") != "FY":
                    continue
                s, e = it.get("start"), it.get("end")
                if not s or not e:
                    continue
                if not e.startswith(str(fy)) or not e.endswith("12-31"):
                    continue
                days = (int(e[:4]) - int(s[:4])) * 365 + (int(e[5:7]) - int(s[5:7])) * 30
                if days < 330 or days > 400:
                    continue
                if best is None or it.get("filed", "") > best[0]:
                    best = (it.get("filed", ""), it["val"])
        if best:
            return best[1], tg
    return None, None


def instant(j, tags, date):
    for tg in tags:
        node = j["facts"].get("us-gaap", {}).get(tg)
        if not node:
            continue
        best = None
        for unit, arr in node["units"].items():
            for it in arr:
                if it.get("end") != date:
                    continue
                if it.get("form") not in ("10-K", "10-K/A", "10-Q"):
                    continue
                if best is None or it.get("filed", "") > best[0]:
                    best = (it.get("filed", ""), it["val"])
        if best:
            return best[1], tg
    return None, None


def row(t, years):
    name, j = facts(t)
    out = {"ticker": t, "name": name, "years": {}}
    for fy in years:
        d0, d1 = "%d-12-31" % (fy - 1), "%d-12-31" % fy
        g = {}
        for k in ("ni_common", "nii", "nonii", "nie", "int_dep", "prov"):
            g[k], g[k + "_tag"] = duration(j, TAGS[k], fy)
        for k in ("equity", "pref", "goodwill", "intang", "deposits", "assets"):
            a, ta = instant(j, TAGS[k], d0)
            b, tb = instant(j, TAGS[k], d1)
            g[k + "_beg"], g[k + "_end"], g[k + "_tag"] = a, b, tb or ta
        out["years"][fy] = g
    return out


def compute(g):
    r = {}

    def avg(k):
        a, b = g.get(k + "_beg"), g.get(k + "_end")
        if a is None or b is None:
            return None
        return (a + b) / 2.0

    def tce(suffix):
        eq, pf = g.get("equity_" + suffix), g.get("pref_" + suffix) or 0
        gw, it_ = g.get("goodwill_" + suffix) or 0, g.get("intang_" + suffix) or 0
        if eq is None:
            return None
        return eq - pf - gw - it_
    a, b = tce("beg"), tce("end")
    atce = None if a is None or b is None else (a + b) / 2.0
    if g.get("ni_common") is not None and atce:
        r["ROTCE"] = 100.0 * g["ni_common"] / atce
    if g.get("nie") is not None and g.get("nii") is not None and g.get("nonii") is not None:
        rev = g["nii"] + g["nonii"]
        if rev:
            r["efficiency"] = 100.0 * g["nie"] / rev
    ad = avg("deposits")
    if g.get("int_dep") is not None and ad:
        r["cost_dep"] = 100.0 * g["int_dep"] / ad
    aa = avg("assets")
    if g.get("nii") is not None and aa:
        r["nii_assets"] = 100.0 * g["nii"] / aa
    if g.get("prov") is not None and aa:
        r["prov_assets"] = 100.0 * g["prov"] / aa
    return r


if __name__ == "__main__":
    years = [2021, 2022, 2023, 2024, 2025]
    allout = {}
    for t in PEERS:
        try:
            rw = row(t, years)
        except Exception as e:
            print("FAIL", t, e)
            continue
        allout[t] = rw
        print("=" * 72)
        print(t, rw["name"])
        for fy in years:
            c = compute(rw["years"][fy])
            print("  %d  ROTCE %7s  eff %7s  costdep %6s  NII/assets %6s  prov/assets %6s" % (
                fy,
                ("%.2f" % c["ROTCE"]) if "ROTCE" in c else "n/a",
                ("%.2f" % c["efficiency"]) if "efficiency" in c else "n/a",
                ("%.2f" % c["cost_dep"]) if "cost_dep" in c else "n/a",
                ("%.2f" % c["nii_assets"]) if "nii_assets" in c else "n/a",
                ("%.2f" % c["prov_assets"]) if "prov_assets" in c else "n/a",
            ))
    json.dump(allout, open(os.path.join(D, "peers_raw.json"), "w"), indent=1)
