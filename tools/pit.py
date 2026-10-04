#!/usr/bin/env python3
"""PIT — point-in-time evidence. The anchor guard.

    python tools/pit.py --selftest
    python tools/pit.py IBM --anchor 2011-11-14
    python tools/pit.py KHC --anchor 2015-07-02 --blind

WHY THIS EXISTS
---------------
Four backtests were withdrawn 2026-07-25 for a look-ahead bug. The lesson was not
"be careful"; it was that discipline is not enforceable by intention. So this
module REFUSES facts rather than trusting the caller to filter them.

THE RULE: a fact is admissible at an anchor only if the SEC received it on or
before that date -- `filed <= anchor`. Not the fiscal period end. The period a
figure describes is not when the public learned it; a FY2010 figure filed in
February 2011 is invisible on 2010-12-31 and must stay invisible.

Everything here returns (value, filed_date) pairs so the caller can never lose
the provenance, and `asof()` reports how many facts it BLOCKED, so a silent
zero-result is distinguishable from a genuine absence.

XBRL COVERAGE LIMIT, stated up front: SEC companyfacts is XBRL, which begins
around 2009 and is thin until ~2011. This module CANNOT build a case file for
Coca-Cola 1988 or Gen Re 1998. Those have to be done by hand from the filings.
Asking it for a pre-2009 anchor returns a refusal, not an empty sheet.
"""
import sys
try:  # Windows consoles default to cp1252 and cannot encode the
    sys.stdout.reconfigure(encoding="utf-8")  # box-drawing / minus glyphs
except Exception:
    pass
import argparse, json, os, sys
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as S

XBRL_FLOOR = "2009-01-01"


def asof(facts, tags, anchor, forms=("10-K", "20-F"), annual_only=True):
    """{period_end: (value_millions, filed)} for facts FILED on or before anchor.

    Returns (series, tag, unit, n_blocked). n_blocked is the count of otherwise
    matching facts rejected for being filed after the anchor -- report it, so an
    empty series caused by the guard is never mistaken for an absence of data.

    MERGES ACROSS TAGS, earlier tag winning per period. Caught 2026-08-27: Apple
    tags FY2013 operating cash flow under one concept and FY2014-15 under another,
    so "first tag that has any data wins" silently dropped two years and made the
    series look a year shorter than it was. Filers switch concepts mid-history;
    a tag list must be treated as a union, not as a priority-ordered fallback that
    stops at the first hit.
    """
    out, used, unit_used, blocked = {}, [], None, 0
    for tax in ("us-gaap", "ifrs-full"):
        node = facts.get("facts", {}).get(tax, {})
        for t in tags:
            if t not in node:
                continue
            for unit, pts in node[t]["units"].items():
                if unit_used and unit != unit_used:
                    continue
                hit = False
                for x in pts:
                    if x.get("form") not in forms:
                        continue
                    end, filed, val = x.get("end"), x.get("filed"), x.get("val")
                    if not (end and filed) or val is None:
                        continue
                    if annual_only and x.get("start"):
                        d = (date.fromisoformat(end)
                             - date.fromisoformat(x["start"])).days
                        if not 340 <= d <= 380:
                            continue
                    if filed > anchor:          # <-- THE GUARD
                        blocked += 1
                        continue
                    hit = True
                    prev = out.get(end)
                    # an earlier tag already holds this period -> keep it
                    if prev and prev[2] != t and prev[2] in tags[:tags.index(t)]:
                        continue
                    if not prev or filed > prev[1]:
                        out[end] = (val / 1e6, filed, t)
                if hit:
                    unit_used = unit_used or unit
                    if t not in used:
                        used.append(t)
    return ({k: (v[0], v[1]) for k, v in out.items()},
            " + ".join(used) if used else None, unit_used, blocked)


def sovereign_asof(anchor, ccy="USD"):
    """30y yield on the last business day at or before the anchor, from FRED.

    MUST request the full series explicitly. Caught 2026-08-27: the bare
    fredgraph.csv?id=DGS30 URL used elsewhere returns only recent observations
    (the cached file held FOUR rows), so a 2018 anchor found no observation at all
    and silently produced a null sovereign -- which would have made every
    historical Q5 uncomputable or, worse, defaulted.
    """
    if ccy != "USD":
        return None, None, f"no historical feed wired for {ccy}"

    # PRIMARY: the US Treasury's own daily yield curve. FRED is a redistributor;
    # Treasury is the issuing authority, which is what the protocol actually asks
    # for. Added 2026-08-27 after FRED refused connections on every endpoint.
    yr = anchor[:4]
    try:
        csv_txt = S._get(
            "https://home.treasury.gov/resource-center/data-chart-center/"
            f"interest-rates/daily-treasury-rates.csv/{yr}/all"
            "?type=daily_treasury_yield_curve&_format=csv",
            S.WEB_UA, f"ust_{yr}.csv", max_age_h=24 * 7)
        rows = [r.split(",") for r in csv_txt.strip().split("\n") if r.strip()]
        hdr = [h.strip().strip('"') for h in rows[0]]
        di = hdr.index("Date")
        i30 = next(i for i, h in enumerate(hdr) if h in ("30 Yr", "30 YR"))
        best = None
        for r in rows[1:]:
            if len(r) <= max(di, i30):
                continue
            raw_d = r[di].strip().strip('"')
            try:
                m, d, y = raw_d.split("/")
                iso = f"{y}-{int(m):02d}-{int(d):02d}"
            except ValueError:
                continue
            v = r[i30].strip().strip('"')
            if not v or iso > anchor:
                continue
            if best is None or iso > best[1]:
                best = (float(v), iso)
        if best:
            return best[0], best[1], "US Treasury daily yield curve (issuing authority)"
    except Exception:
        pass

    try:
        txt = S._get("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30"
                     "&cosd=1977-02-15",
                     cache_name="sov_USD_full.csv", max_age_h=24 * 7)
    except Exception as e:
        # An issuing-authority outage is a documented REFUSAL, not a crash and not
        # a licence to substitute an aggregator or a remembered figure. A run that
        # reaches Q5 without this returns UNRESEARCHED and names the document.
        return None, None, (f"REFUSED - FRED DGS30 unreachable ({type(e).__name__}). "
                            f"Q5 is UNRESEARCHED until it is fetched; the document "
                            f"that resolves it is FRED DGS30 at {anchor}.")
    best = None
    for line in txt.strip().split("\n")[1:]:
        d, _, v = line.partition(",")
        d, v = d.strip(), v.strip()
        if v in (".", "") or d > anchor:
            continue
        best = (float(v), d)
    if not best:
        return None, None, "no observation at or before anchor"
    return best[0], best[1], "FRED DGS30"


def price_asof(ticker, anchor):
    """Close on the last trading day at or before the anchor. `close`, never
    `adjclose` -- adjclose strips dividends and is therefore not a price.

    Fetches a TARGETED 90-day daily window around the anchor. Caught 2026-08-27:
    `range=max&interval=1d` silently degrades to quarterly points (168 samples
    back to 1984), so a 2018-01-02 anchor was answered with a 2017-12-01 close --
    a month-stale price feeding market cap, and therefore Q5.
    """
    end = int(datetime.strptime(anchor, "%Y-%m-%d").timestamp()) + 86400
    start = end - 90 * 86400
    txt = S._get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
                 f"?period1={start}&period2={end}&interval=1d",
                 S.WEB_UA, f"px_{ticker}_{anchor}.json", max_age_h=24 * 30)
    r = json.loads(txt)["chart"]["result"][0]
    ts = r.get("timestamp") or []
    q = (r.get("indicators", {}).get("quote") or [{}])[0]
    closes = q.get("close") or []
    best = None
    for t, c in zip(ts, closes):
        if c is None:
            continue
        try:
            d = datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
        except (OSError, OverflowError, ValueError):
            continue
        if d <= anchor:
            best = (c, d)
    return best if best else (None, None)


OCF = ["NetCashProvidedByUsedInOperatingActivities",
       "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
SBC = ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"]
DA = ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
      "DepreciationAndAmortization", "Depreciation"]
CAP = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
       "PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets"]
NI = ["NetIncomeLoss", "ProfitLoss"]
REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
       "SalesRevenueNet", "RevenueFromContractWithCustomerIncludingAssessedTax",
       # banks report none of the above; caught on Wells Fargo, whose revenue
       # series came back EMPTY and would have been read as "no data"
       "RevenuesNetOfInterestExpense", "InterestAndDividendIncomeOperating"]
SH = ["WeightedAverageNumberOfDilutedSharesOutstanding",
      "WeightedAverageNumberOfSharesOutstandingBasic"]
ASSETS = ["Assets"]
EQUITY = ["StockholdersEquity",
          "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
          "Equity", "EquityAttributableToOwnersOfParent"]
DEBT = ["LongTermDebtNoncurrent", "LongTermDebt", "LongTermBorrowings"]


def case_file(ticker, anchor, blind=False):
    """A point-in-time fact sheet. With --blind, identity is withheld: no name,
    no ticker, no SIC label -- only the numbers and the anchor year."""
    if anchor < XBRL_FLOOR:
        return dict(refused=f"ANCHOR {anchor} PREDATES XBRL (~{XBRL_FLOOR}). "
                            f"companyfacts cannot serve this case; it must be built "
                            f"by hand from the filed statements.")
    cik, name = S.cik_for(ticker)
    if not cik:
        return dict(refused="NOT_AN_SEC_FILER")
    facts = S.sec_facts(cik)

    out = dict(anchor=anchor)
    if not blind:
        out.update(ticker=ticker, name=name, cik=cik)

    # ---- BUG 6 GUARD: TICKER RECYCLING --------------------------------------
    # The ticker->CIK map is AS OF TODAY, not as of the anchor. Tickers get
    # reassigned: PARA now resolves to Banzai International, LZ to LegalZoom.
    # A ticker-keyed historical lookup therefore returns the WRONG COMPANY
    # silently. The guard is positive, not advisory: this CIK must actually have
    # been filing annual reports around the anchor, or the case is refused.
    try:
        ends = [x.get("end") for tax in ("us-gaap", "ifrs-full")
                for tag in ("Assets", "NetIncomeLoss", "ProfitLoss")
                for unit in facts.get("facts", {}).get(tax, {})
                             .get(tag, {}).get("units", {}).values()
                for x in unit
                if x.get("form") in ("10-K", "20-F") and x.get("filed", "9") <= anchor]
    except Exception:
        ends = []
    if not ends:
        return dict(refused=f"NO ANNUAL FACTS FILED ON OR BEFORE {anchor} for CIK {cik} "
                            f"({name}). Either this entity was not reporting then, or the "
                            f"ticker has been REASSIGNED to a different company since. "
                            f"Re-run with the CIK that was filing at the anchor.")
    newest = max(ends)
    gap_days = (date.fromisoformat(anchor) - date.fromisoformat(newest)).days
    out["ticker_map_check"] = dict(
        cik=cik, newest_annual_period_public_at_anchor=newest,
        gap_days=gap_days,
        basis="ticker->CIK resolved AS OF TODAY, not as of the anchor",
        status="OK" if gap_days <= 550 else
               "SUSPECT - the newest annual period public at this anchor is more than "
               "18 months old. Verify the ticker still mapped to this CIK at the anchor.")

    blocked_total = 0
    series = {}
    for label, tags, instant in (("revenue", REV, False), ("ocf", OCF, False),
                                 ("sbc", SBC, False), ("da", DA, False),
                                 ("capex", CAP, False), ("net_income", NI, False),
                                 ("shares_dil", SH, False),
                                 ("assets", ASSETS, True), ("equity", EQUITY, True),
                                 ("lt_debt", DEBT, True)):
        s, tag, unit, blocked = asof(facts, tags, anchor, annual_only=not instant)
        blocked_total += blocked
        series[label] = dict(tag=tag, unit=unit, blocked=blocked,
                             by_year={k: round(v[0], 1) for k, v in sorted(s.items())},
                             filed={k: v[1] for k, v in sorted(s.items())})
    out["series"] = series

    # ---- BALANCE-SHEET CROSS-CHECK -----------------------------------------
    # Caught 2026-08-27 by Test B. Occidental's FY2018 10-K (filed 2019-02-21)
    # tags StockholdersEquity for 2018-12-31 as -172M; the FY2019 10-K tags the
    # same date as 21,330M. The -172M is a dimension-qualified fragment that
    # companyfacts surfaces WITHOUT its dimension, so it is indistinguishable
    # from a consolidated figure.
    #
    # The anchor guard cannot save you here -- it works correctly and pins you to
    # the bad value, because the good one was filed seven months after the anchor.
    # Collision detection cannot save you either: there is only ONE fact for the
    # period. Only an independent identity can. Assets - Liabilities must equal
    # equity; where it does not, the equity figure is marked SUSPECT and the
    # reader is told, rather than being handed a number that looks filed and firm.
    liab, ltag, lunit, lblocked = asof(facts, ["Liabilities"], anchor, annual_only=False)
    blocked_total += lblocked
    series["liabilities"] = dict(tag=ltag, unit=lunit, blocked=lblocked,
                                 by_year={k: round(v[0], 1) for k, v in sorted(liab.items())},
                                 filed={k: v[1] for k, v in sorted(liab.items())})
    checks, A, E = {}, series["assets"]["by_year"], series["equity"]["by_year"]
    L = series["liabilities"]["by_year"]
    for yr in sorted(set(A) | set(E)):
        stated = E.get(yr)
        if stated is None:
            continue
        if yr not in A or yr not in L:
            # An unrunnable check is NOT a pass. Say so, or the reader will read
            # silence as reconciliation -- which is how the OXY figure survived.
            #
            # And where it cannot be run, apply a plausibility screen, because
            # Occidental tags no `Liabilities` at all: its -172M equity would
            # otherwise pass through carrying only a mild "not possible" note.
            # This is a DATA-QUALITY refusal, not a valuation threshold -- the
            # same class as screen.py's IMPLAUSIBLE_YIELD and FLOAT_STRICT.
            implausible = stated < 0 or (yr in A and A[yr] and
                                         abs(stated) / abs(A[yr]) < 0.01)
            checks[yr] = dict(
                stated_equity=stated,
                status="SUSPECT (UNVERIFIABLE)" if implausible
                       else "CROSS-CHECK NOT POSSIBLE",
                missing=("Assets" if yr not in A else "Liabilities"),
                assets=A.get(yr),
                verdict=("Equity is negative or under 1% of assets AND cannot be "
                         "reconciled - the hallmark of a dimension-qualified fact "
                         "surfaced without its dimension. DO NOT USE. Read the filed "
                         "balance sheet." if implausible else
                         "UNVERIFIED - no independent identity available at this "
                         "period. Read the filed balance sheet."))
            continue
        implied = A[yr] - L[yr]
        denom = max(abs(implied), abs(stated), 1.0)
        if abs(implied - stated) / denom > 0.05:
            checks[yr] = dict(stated_equity=stated, assets_less_liabilities=round(implied, 1),
                              status="SUSPECT",
                              verdict="Stated equity does not reconcile to assets minus "
                                      "liabilities; likely a dimension-qualified fact "
                                      "surfaced without its dimension. DO NOT USE without "
                                      "reading the filed balance sheet.")
    if checks:
        out["equity_cross_check"] = checks
        out["equity_reconciled_years"] = sorted(set(E) - set(checks))
    out["facts_blocked_by_anchor"] = blocked_total

    px, pxd = price_asof(ticker, anchor)
    out["price"] = dict(close=px, date=pxd,
                        basis="Yahoo close is stated on TODAY'S share basis: it is already "
                              "divided by every split effective after this date.")

    # ---- MARKET CAP ON A SINGLE, STATED SHARE BASIS -------------------------
    # Bug 9, found by a Test B analyst rather than by me. The file used to pair a
    # split-adjusted PRICE with an AS-REPORTED share count and no reconciling
    # factor, so Apple's May-2016 yield came out ~4x too high (a $23.47 close on
    # today's basis against a 5,793.1m count on 2015's, before the 2020 4:1).
    # The analyst refused to compute a cap and cited the house rule to say why:
    #   cap = close(anchor) x shares(measurement) x splits AFTER measurement
    # That rule is now executed here, and its three components are exposed so the
    # reader can check the arithmetic instead of trusting it.
    sh = series["shares_dil"]["by_year"]
    shf = series["shares_dil"]["filed"]
    cap = None
    if sh and px:
        yr = max(sh)
        measurement_filed = shf[yr]
        try:
            factor = S.split_factor_after(ticker, measurement_filed)
        except Exception:
            factor = None
        # Yahoo files SPINOFFS as split events. A clean split is a small integer
        # ratio; anything else corrupts the count. IBM came back x1.046 (Kyndryl),
        # inflating the cap ~5%. Same guard as flags.py, ported here.
        ratio_ok = factor is not None and any(
            abs(factor - r) < 1e-3 for r in
            (1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50,
             1.5, 2.5, 1.25, 7.5, 0.5, 0.25, 0.1, 0.05))
        if factor is not None and ratio_ok:
            cap = px * sh[yr] * factor
            out["market_cap"] = dict(
                value_millions=round(cap, 1),
                formula="close(anchor) x shares(measurement) x splits AFTER measurement",
                close=px, close_date=pxd,
                shares_millions_as_reported=sh[yr], shares_period=yr,
                shares_filed=measurement_filed,
                split_factor_after_measurement=factor,
                note="Both inputs are now on the same basis. Do NOT recompute from the "
                     "raw share count and the raw close - they are on different bases.")
        elif factor is not None:
            out["market_cap"] = dict(
                refused=f"SPLIT FACTOR {factor:g} IS NOT A CLEAN RATIO - almost certainly a "
                        f"SPINOFF recorded as a split. The share count cannot be put on the "
                        f"price's basis without corrupting it. Q5 is UNRESEARCHED until the "
                        f"count is read off the cover page of the filing.",
                close=px, close_date=pxd,
                shares_millions_as_reported=sh[yr], shares_period=yr)
        else:
            out["market_cap"] = dict(refused="SPLIT HISTORY UNAVAILABLE - cap cannot be "
                                             "put on a single share basis. Q5 is "
                                             "UNRESEARCHED until it is.")

    sov, sovd, sovsrc = sovereign_asof(anchor)
    out["sovereign"] = dict(rate_pct=sov, date=sovd, source=sovsrc)
    return out


def selftest():
    """Prove the guard actually blocks. Not a claim -- a demonstration."""
    print("ANCHOR GUARD SELFTEST")
    print("=" * 78)
    cik, name = S.cik_for("AAPL")
    facts = S.sec_facts(cik)
    ok = True
    for anchor in ("2015-01-01", "2019-01-01", "2026-08-27"):
        s, tag, unit, blocked = asof(facts, OCF, anchor)
        latest_end = max(s) if s else None
        latest_filed = max(v[1] for v in s.values()) if s else None
        leak = [e for e, v in s.items() if v[1] > anchor]
        print(f"\nanchor {anchor}")
        print(f"  admitted {len(s):>3} annual OCF facts, blocked {blocked:>3}")
        print(f"  newest period admitted : {latest_end}")
        print(f"  newest FILING admitted : {latest_filed}")
        print(f"  facts filed after anchor that leaked through: {len(leak)}")
        if leak:
            ok = False
        if latest_filed and latest_filed > anchor:
            ok = False
    print("\n" + "=" * 78)
    print("PASS - no fact filed after its anchor was admitted." if ok
          else "FAIL - the guard leaked.")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker", nargs="?")
    ap.add_argument("--anchor")
    ap.add_argument("--blind", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.ticker and a.anchor):
        ap.error("give TICKER --anchor YYYY-MM-DD, or --selftest")
    cf = case_file(a.ticker.upper(), a.anchor, blind=a.blind)
    txt = json.dumps(cf, indent=1)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"wrote {a.out}  ({cf.get('facts_blocked_by_anchor','?')} facts blocked "
              f"by the anchor)")
    else:
        print(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
