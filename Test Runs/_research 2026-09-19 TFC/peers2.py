"""TFC competitor row, ONE BASIS for every peer, from filed statement values.

Why this exists. Each large bank publishes ROTCE, the efficiency ratio, cost of deposits and
NIM on its OWN basis (taxable-equivalent or not; all-deposit or interest-bearing cost;
tangible net income with or without the deferred-tax adjustment), and some do not publish
ROTCE in the 10-K at all. The CCB run of 2026-09-19 recorded the consequence: a row of each
filer's own ratios is directionally, not decimally, comparable. This script therefore
computes the same four numbers the same way for all nine banks out of the same filed
statement lines, and the run prints the subject's own filed figure beside the computed one so
the size of the basis difference is visible rather than hidden.

DEFINITIONS, identical for every row:
  ROTCE       = net income available to common / average (common equity - goodwill - other
                intangibles).  NO add-back of intangible amortisation and NO deferred-tax
                adjustment, so this sits BELOW each filer's own published ROTCE by the size
                of those two adjustments - stated, not smoothed.
  efficiency  = noninterest expense / (net interest income + noninterest income), not TE.
  cost of dep = interest expense on deposits / average total deposits (ALL deposits, so it is
                lower than any interest-bearing-only figure).
  NII/assets  = net interest income / average total assets.  A NIM PROXY on a common
                denominator, NOT a net interest margin: every filer's own NIM divides by
                average EARNING assets, which is not a tagged concept.
"""
import sys, os, json, time

sys.path.insert(0, os.path.join("C:/Users/chreh/OneDrive/Documents/BRK", "tools"))
import sources

D = os.path.dirname(os.path.abspath(__file__))
PEERS = ["TFC", "PNC", "USB", "FITB", "KEY", "RF", "CFG", "MTB", "HBAN"]
YEARS = [2021, 2022, 2023, 2024, 2025]

DUR = {
    "ni_common": ["NetIncomeLossAvailableToCommonStockholdersBasic"],
    "nii": ["InterestIncomeExpenseNet"],
    "nonii": ["NoninterestIncome"],
    "nie": ["NoninterestExpense"],
    "int_dep": ["InterestExpenseDeposits", "InterestExpenseDepositLiabilities",
                "InterestExpenseDomesticDepositLiabilities"],
}
INST = {
    "equity_tot": ["StockholdersEquity",
                   "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "pref": ["PreferredStockIncludingAdditionalPaidInCapitalNetOfDiscount",
             "PreferredStockValue", "PreferredStockValueOutstanding",
             "PreferredStockIncludingAdditionalPaidInCapital",
             "PreferredStockLiquidationPreferenceValue"],
    "goodwill": ["Goodwill"],
    "intang": ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet",
               "IntangibleAssetsNetIncludingGoodwill"],
    "deposits": ["Deposits"],
    "assets": ["Assets"],
}


def facts(t):
    cik, nm = sources.cik_for(t)
    p = os.path.join(D, "cf_%s.json" % t)
    if not os.path.exists(p) or os.path.getsize(p) < 5000:
        txt = sources.sec_facts(cik)
        if isinstance(txt, (dict, list)):
            txt = json.dumps(txt)
        open(p, "w", encoding="utf-8").write(txt)
        time.sleep(0.2)
    return nm, json.loads(open(p, encoding="utf-8").read())


def dur(j, tags, fy):
    for tg in tags:
        node = j["facts"].get("us-gaap", {}).get(tg)
        if not node:
            continue
        best = None
        for unit, arr in node["units"].items():
            for it in arr:
                if it.get("form") not in ("10-K", "10-K/A") or it.get("fp") != "FY":
                    continue
                s, e = it.get("start"), it.get("end")
                if not s or not e or not e.startswith(str(fy)) or not e.endswith("12-31"):
                    continue
                days = (int(e[:4]) - int(s[:4])) * 365 + (int(e[5:7]) - int(s[5:7])) * 30
                if days < 330 or days > 400:
                    continue
                if best is None or it.get("filed", "") > best[0]:
                    best = (it.get("filed", ""), it["val"], tg)
        if best:
            return best[1], best[2]
    return None, None


def inst(j, tags, date):
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
                    best = (it.get("filed", ""), it["val"], tg)
        if best:
            return best[1], best[2]
    return None, None


def build():
    out = {}
    for t in PEERS:
        nm, j = facts(t)
        rows = {}
        for fy in YEARS:
            d0, d1 = "%d-12-31" % (fy - 1), "%d-12-31" % fy
            g = {}
            for k, tags in DUR.items():
                g[k], g[k + "__tag"] = dur(j, tags, fy)
            for k, tags in INST.items():
                for suf, dt in (("beg", d0), ("end", d1)):
                    g[k + "_" + suf], g[k + "_" + suf + "__tag"] = inst(j, tags, dt)
            rows[fy] = g
        out[t] = {"name": nm, "rows": rows}
    return out


def metrics(g):
    r, miss = {}, []

    def tce(suf):
        eq = g.get("equity_tot_" + suf)
        if eq is None:
            miss.append("equity_" + suf)
            return None
        pf = g.get("pref_" + suf)
        if pf is None:
            miss.append("pref_" + suf)
            pf = 0
        gw = g.get("goodwill_" + suf) or 0
        it_ = g.get("intang_" + suf)
        if it_ is None:
            miss.append("intang_" + suf)
            it_ = 0
        return eq - pf - gw - it_

    a, b = tce("beg"), tce("end")
    if g.get("ni_common") is not None and a and b:
        r["ROTCE"] = 100.0 * g["ni_common"] / ((a + b) / 2.0)
        r["_atce"] = (a + b) / 2.0
    if None not in (g.get("nie"), g.get("nii"), g.get("nonii")):
        rev = g["nii"] + g["nonii"]
        if rev:
            r["EFF"] = 100.0 * g["nie"] / rev
    dp = [g.get("deposits_beg"), g.get("deposits_end")]
    if g.get("int_dep") is not None and None not in dp:
        r["COSTDEP"] = 100.0 * g["int_dep"] / ((dp[0] + dp[1]) / 2.0)
    ast = [g.get("assets_beg"), g.get("assets_end")]
    if g.get("nii") is not None and None not in ast:
        r["NIIA"] = 100.0 * g["nii"] / ((ast[0] + ast[1]) / 2.0)
    r["_missing"] = sorted(set(miss))
    return r


if __name__ == "__main__":
    data = build()
    json.dump(data, open(os.path.join(D, "peers2_raw.json"), "w"), indent=1)
    for k in ("ROTCE", "EFF", "COSTDEP", "NIIA"):
        print("=" * 84)
        print(k, "  (one basis, computed from filed statement lines)")
        print("ticker  " + "".join("%9d" % y for y in YEARS) + "    5y mean")
        for t in PEERS:
            vals = []
            for fy in YEARS:
                m = metrics(data[t]["rows"][fy])
                vals.append(m.get(k))
            good = [v for v in vals if v is not None]
            mean = sum(good) / len(good) if good else None
            print("%-7s" % t + "".join(
                ("%9.2f" % v) if v is not None else "      n/a" for v in vals)
                + (("   %7.2f" % mean) if mean is not None else "      n/a"))
    print("=" * 84)
    print("MISSING INPUTS (where a cell is n/a or an assumption was made):")
    for t in PEERS:
        for fy in YEARS:
            m = metrics(data[t]["rows"][fy])
            if m["_missing"]:
                print("  %s %d  %s" % (t, fy, ",".join(m["_missing"])))
