#!/usr/bin/env python3
"""RUN — pre-fill a company run file with everything that is arithmetic.

    python tools/run.py TJX
    python tools/run.py ASML --currency EUR --years 3

It fetches the filings and the sovereign, computes owner earnings, and writes a
dated run file with the numeric fields filled and every judgment field left blank.

It does NOT form a verdict. Framework v4 forbids that: tagged data is transcription
and screening, and no name reaches Q5 on tags alone [E3-27, E4-14]. The output is
headed with the Step 0-B work you still owe -- reading the actual filing.
"""
import sys
try:  # Windows consoles default to cp1252 and cannot encode the
    sys.stdout.reconfigure(encoding="utf-8")  # box-drawing / minus glyphs
except Exception:
    pass
import argparse, csv, os, statistics, sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as S


def _annual(facts, tags):
    """Every read in this file is LIVE, so a restated period reads its NEWEST filing.

    The DELL fix of 2026-09-07 made vintage a parameter in sources.annual() with the default
    left at 'earliest' so nothing anchored in the past would change by my hand - and this
    file, which prices companies at today's quote, was never switched. The SNPS run found it
    reading Synopsys's ORIGINAL FY2024 capex rather than the restated figure. Fixed here in
    one place rather than at each of the call sites."""
    return S.annual(facts, tags, vintage="newest")

ROOT = S.ROOT

OCF = ["NetCashProvidedByUsedInOperatingActivities",
       "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
SBC = ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"]
DA  = ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
       "DepreciationAndAmortization", "Depreciation"]
CAP = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
       "PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets"]
# CAPITALISED SOFTWARE IS PART OF (c), AND IT IS SUMMED, NOT RANKED. Ported from
# floor_screen.capital_acquired() on 2026-09-07 after the CERT run reported that the two
# owner-earnings paths DISAGREE: floor_screen resolves Certara's $24.8M capitalised-software
# line correctly (the HAS fix works), while this file's CAP list never had it - and
# tools/screen.py imports from here, so the master queue was built from the unfixed path.
# A fix applied on one path and not the other is worse than no fix, because it looks applied.
#
# WHY A SEPARATE LIST RATHER THAN THREE MORE ENTRIES IN CAP: _annual() picks ONE element
# per period by rank, so appending these would only use them when PP&E capex is ABSENT.
# A filer that reports both spends both. Software development is capital that buys next
# year's product; leaving it out understates (c) and overstates owner earnings.
SOFTWARE_CAP = ["PaymentsToDevelopSoftware", "PaymentsForSoftware",
                "PaymentsToAcquireSoftware", "PaymentsForCapitalizedInternalUseSoftware"]
DA_TOTAL = ["DepreciationDepletionAndAmortization",
            "DepreciationAmortizationAndAccretionNet",
            "DepreciationAndAmortization"]
DA_COMPONENT = ["Depreciation", "AmortizationOfIntangibleAssets"]
NI  = ["NetIncomeLoss", "ProfitLoss"]
SH  = ["WeightedAverageNumberOfDilutedSharesOutstanding",
       "WeightedAverageNumberOfSharesOutstandingBasic"]
# The cover-page element, preferred over SH above. Ported from
# floor_screen.shares_outstanding() on 2026-09-07; see the note at the call site.
COVER_SH = [("EntityCommonStockSharesOutstanding", "dei"),
            ("CommonStockSharesOutstanding", "us-gaap"),
            ("CommonStockSharesIssued", "us-gaap"),
            ("NumberOfSharesOutstanding", "ifrs-full")]


def cover_count(facts, today=None):
    """(as_of, millions of shares) from the cover page, or None if absent or stale.

    Returns MILLIONS, to match the scaling _annual() applies. Refuses a count older than
    550 days rather than pricing a company on a number that has been superseded twice: the
    CRWD run of 2026-09-07 found a 4-for-1 split five months after the 10-K cover date, and
    the QLYS run found a cover count stale by six months and 3.1% against the company.

    THIS DOES NOT SUM SHARE CLASSES, and that is deliberate - whether two classes are
    economically equivalent is a judgment from the charter, not arithmetic. For a multi-class
    filer the reader still goes to Screens/cover_shares.py and the charter."""
    today = today or date.today()
    obs = []
    for tag, space in COVER_SH:
        for x in (facts.get("facts", {}).get(space, {}).get(tag, {})
                  .get("units", {}).get("shares", [])):
            e, v = x.get("end"), x.get("val")
            if e and v and float(v) > 0:
                obs.append((date.fromisoformat(e), float(v)))
        if obs:
            break
    if not obs:
        return None
    d, v = max(obs)
    return (d, v / 1e6) if (today - d).days <= 550 else None

# SIC ranges the sector method covers. Found by the WTM run of 2026-09-02, which reported
# that this script hands back confident owner-earnings yields with "points over the
# sovereign" for MKL (10.44-10.77%, +8.13 pts) and L (11.90-12.23%, +9.65 pts) - both
# overstated, because float growth sits inside operating cash flow and investment income
# double-counts a portfolio nothing here values. It fails safe on WTM only BY ACCIDENT
# (missing capex tags), and MKL and L tag capex through non-insurance subsidiaries, so the
# accident does not extend to them.
INSURER_SIC = [(6311, 6411)]     # life, accident & health, P&C, title, surety, brokers


def is_insurer(cik):
    """(True/False, sic, description) from the SEC submissions endpoint."""
    import json as _j, urllib.request as _u
    try:
        d = _j.loads(_u.urlopen(_u.Request(
            f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json",
            headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com"}), timeout=45).read())
        sic = int(d.get("sic") or 0)
        return (any(lo <= sic <= hi for lo, hi in INSURER_SIC), sic,
                d.get("sicDescription", ""))
    except Exception:
        return (False, 0, "")


def owner_earnings(facts, years):
    """OE = mean(OCF - SBC) - mean maintenance capex, over the last `years` fiscal years.

    Maintenance capex is a DISCLOSED JUDGMENT, not an output -- Buffett says (c)
    "must be a guess" [E2-23]. We return the BAND (D&A .. total capex) and the run
    states where in it the figure sits, and why, citing the filing.
    """
    ocf, ocf_tag, unit = _annual(facts, OCF)
    # LARGEST RESOLVING SBC ELEMENT, ported from floor_screen.sbc_annual() on 2026-09-07
    # after the CGNX run: rank precedence returned ShareBasedCompensation at $1.40M against
    # the filed AllocatedShareBasedCompensationExpense of $42.66M for FY2020. A subcomponent
    # can never exceed its total, and SBC is SUBTRACTED, so max() fails safe both ways.
    sbc = {}
    for _tag in SBC:
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            if _e not in sbc or abs(_v) > abs(sbc[_e]):
                sbc[_e] = _v
    # LARGEST RESOLVING D&A ELEMENT PER PERIOD, ported from floor_screen.da_annual() on
    # 2026-09-03 after the MCD run confirmed the defect LIVE here: first-tag-wins returned
    # a $457M subcomponent against a $2,199M filed charge - the exact case that motivated
    # the floor_screen fix on 2026-09-01, never ported. A filer may tag both a component
    # and the total; the total is never smaller.
    # PREFER A FILED TOTAL; WHERE NONE EXISTS, SUM THE COMPONENTS. Ported from
    # floor_screen.da_annual() on 2026-09-07 after the CGNX run, which found the max rule
    # returning Cognex's Depreciation of $20.3M against a filed $30.8M - 34% low - because
    # Cognex tags Depreciation and AmortizationOfIntangibleAssets as two COMPONENTS with no
    # combined total. The max rule is right for a subcomponent-versus-total filer (the MCD
    # case) and wrong for a two-component one. Fixed in both paths at once, because a fix
    # applied to one path and not its twin has now been found three times in two days.
    da = {}
    for _tag in DA_TOTAL:
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            if _e not in da or abs(_v) > abs(da[_e]):
                da[_e] = _v
    _parts = {}
    for _tag in DA_COMPONENT:
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            _parts[_e] = _parts.get(_e, 0.0) + abs(_v)
    for _e, _v in _parts.items():
        if _e not in da or _v > abs(da[_e]):
            da[_e] = _v
    cap, _, _ = _annual(facts, CAP)
    soft, _, _ = _annual(facts, SOFTWARE_CAP)
    if soft:
        cap = {e: abs(v) + abs(soft.get(e, 0.0)) for e, v in cap.items()}
    ni,  _, _ = _annual(facts, NI)
    ys = sorted(set(ocf) & set(da) & set(cap))
    if not ys:
        return None
    sel = ys[-years:]
    rows = []
    for y in sel:
        cash = ocf[y] - sbc.get(y, 0.0)
        lo = cash - max(da[y], cap[y])      # conservative end of the capex band
        hi = cash - min(da[y], cap[y])      # generous end
        rows.append(dict(fy=y, ocf=ocf[y], sbc=sbc.get(y, 0.0), da=da[y],
                         capex=cap[y], ni=ni.get(y), oe_lo=lo, oe_hi=hi))
    return dict(unit=unit, ocf_tag=ocf_tag, rows=rows, all_years=ys,
                mean_lo=statistics.fmean(r["oe_lo"] for r in rows),
                mean_hi=statistics.fmean(r["oe_hi"] for r in rows))


def implied_growth(cap_mn, base_mn, rate, tgr=0.025, yrs=10):
    """Year-1 growth the quote already assumes. The DCF is an ENGINE here, not a
    voter [E3-34] -- it converts growth into a rate you can set beside a bond.

    Returns None when the base is non-positive. THE MU CRASH, 2026-09-07: this raised
    ZeroDivisionError on Micron and Intel - both names whose owner earnings sit at or below
    zero - and the screen re-triaged them as UNPRICED indefinitely. A discounted-cash-flow
    engine run on negative owner earnings does not produce a wrong number; it produces no
    number, and the honest output is a refusal the caller must print. Refusing is also the
    framework's own answer: a negative bottom boundary is a statement about the CONSERVATIVE
    construction [E5-34], not an input to a growth calculation."""
    if base_mn is None or base_mn <= 0 or rate <= tgr:
        return None
    def pv(g1):
        v, oe = 0.0, base_mn
        for t in range(1, yrs + 1):
            g = g1 + (tgr - g1) * (t - 1) / (yrs - 1)
            oe *= (1 + g)
            v += oe / (1 + rate) ** t
        d = rate - tgr
        return v + (oe * (1 + tgr) / d) / (1 + rate) ** yrs if d > 1e-9 else float('inf')
    lo, hi = -0.50, 1.50
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(m) < cap_mn: lo = m
        else: hi = m
    return (lo + hi) / 2


def points_over(cap_mn, base_mn, g1, sov_pct, tgr=0.025, yrs=10):
    """Return at the current price, expressed as points over the sovereign [E4-21].

    Returns None on a non-positive base - see implied_growth() for the MU/INTC crash."""
    if base_mn is None or base_mn <= 0:
        return None
    def pv(r):
        v, oe = 0.0, base_mn
        for t in range(1, yrs + 1):
            g = g1 + (tgr - g1) * (t - 1) / (yrs - 1)
            oe *= (1 + g)
            v += oe / (1 + r) ** t
        d = r - tgr
        return v + (oe * (1 + tgr) / d) / (1 + r) ** yrs if d > 1e-9 else float('inf')
    lo, hi = 1e-4, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(m) > cap_mn: lo = m
        else: hi = m
    return (lo + hi) / 2 * 100 - sov_pct


# BALANCE SHEETS OVER TEN YEARS, added 2026-10-05. v5's Q4 directs the reader to "look at balance sheets
# over an 8 or 10 year period before I even look at the income account" [M2025-032], and no run had done it:
# this tool pulled no balance-sheet history and the template did not ask. Transcription only (the
# tooling test: the same filed numbers, sooner); each value is the FIRST-filed vintage for its year-end,
# so a later restatement shows up as a difference when the filing is read, and the accession is printed.
BS_ROWS = [
    ("assets",      ["Assets"]),
    ("liabilities", ["Liabilities"]),
    ("equity",      ["StockholdersEquity",
                     "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]),
    ("cash",        ["CashAndCashEquivalentsAtCarryingValue",
                     "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]),
    ("receivables", ["AccountsReceivableNetCurrent", "ReceivablesNetCurrent"]),
    ("inventory",   ["InventoryNet"]),
    ("goodwill",    ["Goodwill"]),
    ("intangibles", ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"]),
    ("lt debt",     ["LongTermDebtNoncurrent", "LongTermDebt", "LongTermNotesPayable"]),
    ("retained",    ["RetainedEarningsAccumulatedDeficit"]),
]
BS_FORMS = {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A", "10-KT"}


def balance_history(facts, currency="USD", n=10):
    """{year_end: {row: (value, accession)}} for the last n fiscal year-ends, first-filed vintage."""
    ns = facts.get("facts", {})
    pool = dict(ns.get("us-gaap", {}))
    for k, v in ns.get("ifrs-full", {}).items():
        pool.setdefault(k, v)
    out = {}
    for row, tags in BS_ROWS:
        for tag in tags:
            got = {}
            for x in pool.get(tag, {}).get("units", {}).get(currency, []):
                if x.get("form") not in BS_FORMS or x.get("start") or not x.get("end"):
                    continue
                if x.get("fp") not in (None, "FY"):
                    continue
                e, f = x["end"], x.get("filed", "9999")
                if e not in got or f < got[e][2]:
                    got[e] = (float(x["val"]), x.get("accn", "?"), f)
            if got:
                for e, (v, accn, _) in got.items():
                    out.setdefault(e, {})[row] = (v, accn)
                break
    ends = sorted(out)[-n:]
    return {e: out[e] for e in ends}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--currency", default="USD", help="currency the business EARNS in")
    ap.add_argument("--years", type=int, default=3, help="averaging window for owner earnings")
    ap.add_argument("--shares", type=float, help="shares outstanding, millions (overrides XBRL)")
    ap.add_argument("--quote", help="ticker to take the PRICE from, when the filer's "
                    "home listing quotes in the earnings currency (e.g. ASML.AS for EUR). "
                    "Data routing only - the currency guard still applies.")
    # DEFAULT CHANGED 3.0 -> 0.0 ON 2026-09-02. The WTM run found the run TEMPLATE still
    # carrying "the corpus gives a floor of +3% over the long bond", a rule THE FRAMEWORK
    # v4.md had explicitly REWRITTEN on 2026-08-28 as a misreading of [E3-13]. The same
    # retired rule was here, and worse - it was BAKED INTO THE ARITHMETIC as a default,
    # silently adding three points to every discount rate this script computed. [E3-42],
    # four independent times 1996-1999: "If you say I'm going to stick an extra 6 percent
    # in on the interest rate ... it's mathematical gibberish in my view. You better just
    # stick with businesses that you can understand, USE THE GOVERNMENT BOND RATE."
    # Certainty is handled at the understanding gate and in the end margin, once [E4-11].
    ap.add_argument("--spread", type=float, default=0.0,
                    help="points added to the sovereign. DEFAULT 0 AND IT SHOULD STAY 0 - "
                         "[E3-42] calls a per-name rate premium mathematical gibberish. "
                         "Exposed only so a deliberate departure has to be typed.")
    ap.add_argument("--write", action="store_true", help="write the run file")
    # 2026-10-05: the v5 test runs found this tool printing v4 ledger ids and the v4 floor into blind
    # runs. The arithmetic is framework-free and always prints; the v4 commentary prints only under
    # --framework v4, and --write fills the template of the framework named.
    ap.add_argument("--framework", choices=("v4", "v5"), default="v5",
                    help="which framework's template --write fills and whose commentary prints")
    a = ap.parse_args()
    t = a.ticker.upper()

    cik, name = S.cik_for(t)
    if not cik:
        print(f"{t}: not an SEC filer. Use the evidence ladder: company IR site (English),")
        print("exchange filings (TDnet / RNS / SEDAR+). This is UNRESEARCHED, not UNKNOWABLE.")
        return 1

    sov, sov_date, sov_src = S.sovereign(a.currency)
    px, px_date, px_ccy = S.price(a.quote or t)
    facts = S.sec_facts(cik)
    oe = owner_earnings(facts, a.years)
    if not oe:
        print(f"{t}: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED.")
        return 1

    # THE INSURER GATE, added 2026-09-02 after the WTM run. An insurer's operating cash flow
    # contains premiums received before losses are paid - borrowed money [E2-61] - and net
    # investment income belonging to a portfolio this script does not value [E5-48]. A yield
    # computed from it is not conservative, it is wrong, and it errs in the FLATTERING
    # direction. Refuse rather than print it.
    ins, sic, sicdesc = is_insurer(cik)
    if ins and not a.shares:
        print(f"{t}: SIC {sic} ({sicdesc}) is an insurer.")
        print("  THIS SCRIPT CANNOT PRICE IT. Operating cash flow contains float growth,")
        print("  which is borrowed money, and investment income, which belongs to a")
        print("  portfolio nothing here values. The yield would be overstated.")
        print("  USE Framework/SECTOR METHOD - owner earnings for insurers and")
        print("  float-bearing holding companies.md, which values two components separately.")
        print("  (Pass --shares to override if you have already made the corrections.)")
        return 1

    shares, sh_src = a.shares, "--shares, supplied by the operator"
    if shares is None:
        # COVER COUNT FIRST, WEIGHTED AVERAGE ONLY AS A LABELLED FALLBACK. Added 2026-09-07
        # after the CRM run reported the consequence of leaving this at the weighted average:
        # 956M against the cover page's 823M, a market cap 16.2% TOO HIGH, so every yield this
        # script printed for Salesforce was too LOW - the flattering direction is not the safe
        # direction when the question is whether to buy.
        #
        # The basis label was added on 2026-09-02 from the UAL and WTM runs, and it was not
        # enough: a script that announces the wrong basis and then uses it anyway still hands
        # back a wrong cap, and the reader has to know to distrust it. floor_screen.py has read
        # the cover element since 2026-09-01; this path never did, so the two owner-earnings
        # paths disagreed on the DENOMINATOR as well as on (c).
        #
        # A weighted average is a denominator for EPS, not a count of the shares that exist.
        cover = cover_count(facts)
        if cover:
            shares, sh_src = cover[1], f"dei cover-page count as of {cover[0]}"
        else:
            sh, sh_tag, _ = _annual(facts, SH)
            shares = (sh[max(sh)] if sh else None)
        # THE SHARE-BASIS LABEL, added 2026-09-02. The UAL run reported that this script used
        # diluted weighted-average shares WITHOUT saying so, and the WTM run reported the
        # consequence on Berkshire: a weighted-average A-share count of ~1.6M gives a $0.83bn
        # cap and a 2,668-3,491% yield, +94.73 points over the sovereign. A WEIGHTED AVERAGE
        # IS NOT A SHARE COUNT - it is a denominator for EPS - and for a multi-class filer it
        # is denominated in whichever class the filer chose. Say which basis produced the cap.
            sh_src = (f"{sh_tag} - a WEIGHTED AVERAGE, not a cover-page count")
    if not shares:
        print(f"{t}: no share count in XBRL; pass --shares (millions) from the cover page.")
        print("  `python Screens/cover_shares.py {t}` reads it off the filed cover by class.")
        return 1

    cap = px * shares
    rate = (sov + a.spread) / 100
    note = print if a.framework == "v4" else (lambda *x, **k: None)
    if a.spread:
        print(f"  ** DISCOUNT RATE CARRIES A +{a.spread:.2f} POINT SPREAD over the "
              f"sovereign. Both frameworks refuse a risk premium in the rate; certainty is "
              f"priced once, in the margin demanded at the end. State the reason or drop it. **")
    y_lo, y_hi = oe["mean_lo"] / cap * 100, oe["mean_hi"] / cap * 100
    g_imp = implied_growth(cap, oe["mean_lo"], rate)
    pts_lo = points_over(cap, oe["mean_lo"], 0.03, sov)
    pts_hi = points_over(cap, oe["mean_hi"], 0.03, sov)

    W = 78
    print("=" * W)
    print(f"{name}  ({t})   —  ARITHMETIC ONLY, NOT A VERDICT")
    print("=" * W)
    print(f"  sovereign {a.currency}   {sov:.2f}%   {sov_date}   {sov_src}")
    print(f"  price     {px:,.2f} {px_ccy}   {px_date}"
          f"{'  via ' + a.quote if a.quote else ''}   (aggregator — live quote only)")
    if px_ccy and oe and px_ccy.upper() != oe["unit"]:
        print(f"  ** CURRENCY MISMATCH: earnings in {oe['unit']}, quote in {px_ccy}."
              f" Refusing to convert. Pass --quote with the home listing. **")
        return 1
    print(f"  shares    {shares:,.1f}M      market cap {cap/1000:,.2f}B {oe['unit']}")
    print(f"  share basis: {sh_src}")
    if "WEIGHTED AVERAGE" in sh_src:
        print("  ** A weighted average is an EPS denominator, not a share count.")
        print("     For a multi-class filer it is denominated in ONE class. Verify:")
        print(f"     python Screens/cover_shares.py {t} **")
    print(f"\n  OWNER EARNINGS   mean of {a.years} years of (OCF − SBC) − maintenance capex")
    print(f"  OCF tag: {oe['ocf_tag']}")
    print(f"\n  {'FY end':>12}{'OCF':>11}{'SBC':>9}{'D&A':>10}{'capex':>11}"
          f"{'OE lo':>11}{'OE hi':>11}")
    for r in oe["rows"]:
        print(f"  {r['fy']:>12}{r['ocf']:>11,.0f}{r['sbc']:>9,.0f}{r['da']:>10,.0f}"
              f"{r['capex']:>11,.0f}{r['oe_lo']:>11,.0f}{r['oe_hi']:>11,.0f}")
    print(f"  {'mean':>12}{'':>41}{oe['mean_lo']:>11,.0f}{oe['mean_hi']:>11,.0f}")
    # v4 amendment 2026-08-27: BOTH windows, always. Test A showed two analysts
    # reaching a 28% different owner-earnings figure from the same filings purely
    # by choosing 3 years versus 5. The window is a judgment; it gets disclosed.
    alt_years = 5 if a.years == 3 else 3
    oe_alt = owner_earnings(facts, alt_years)
    if oe_alt:
        ya_lo = oe_alt["mean_lo"] / cap * 100
        ya_hi = oe_alt["mean_hi"] / cap * 100
        div = ((oe_alt["mean_lo"] - oe["mean_lo"]) / abs(oe["mean_lo"]) * 100
               if oe["mean_lo"] else float("nan"))
        print(f"\n  THE OTHER WINDOW ({alt_years}-yr, {len(oe_alt['rows'])} yrs of data)"
              f"   OE {oe_alt['mean_lo']:,.0f} .. {oe_alt['mean_hi']:,.0f}"
              f"   yield {ya_lo:.2f}%..{ya_hi:.2f}%")
        print(f"  DIVERGENCE vs the {a.years}-yr window: {div:+.1f}% on the conservative end")
        if abs(div) > 15:
            print("  ** The spread between the windows is part of the range, not a tiebreak;")
            print("     do not pick a window and defend it. **")
            note("     [E4-25] Working with a range of possibilities is the better approach.")
            note("     If the combined range (window spread x capex band) is too wide to reach")
            note("     a conclusion, THAT IS THE CONCLUSION [E4-25]. A wide spread is also a Q4")
            note("     finding about earnings reliability [E5-11].")

    print(f"\n  1. THE YIELD                 {y_lo:5.2f}% .. {y_hi:5.2f}%   "
          f"vs sovereign {sov:.2f}%")
    if g_imp is None:
        print(f"  2. GROWTH THE PRICE ASSUMES  REFUSED - the conservative owner-earnings")
        print(f"     base is at or below zero. A DCF on a non-positive base produces no")
        print(f"     number; the negative bottom boundary IS the statement.")
    else:
        print(f"  2. GROWTH THE PRICE ASSUMES  {g_imp*100:5.1f}%  (at a {rate*100:.2f}% rate)")
    if pts_lo is None or pts_hi is None:
        print(f"  3. POINTS OVER THE SOVEREIGN REFUSED on the same ground"
              f"{'' if pts_hi is None else f' at the conservative end; generous end {pts_hi:+.2f}'}")
    else:
        print(f"  3. POINTS OVER THE SOVEREIGN {pts_lo:+5.2f} .. {pts_hi:+5.2f}")
    # SIXTH HOME OF THE RETIRED RULE, found by the PEP run 2026-09-03. The framework
    # rewrote "no hurdle, it ranks" into "the floor first, then the ranking" on 2026-08-28;
    # copies have since been found and fixed in the template, run.py's --spread default,
    # the sector method's step 4, CLAUDE.md's one-screen summary - and this print, which
    # told every run.py user the opposite of the framework at the moment of decision.
    note(f"\n  THE FLOOR FIRST [E4-28]: below ~10% honest expectancy the name is quit on,")
    note(f"  not ranked. What clears the floor ranks against the opportunity set [E4-21].")
    bs = balance_history(facts, a.currency)
    bs_lines = []
    if bs:
        cols = [r for r, _ in BS_ROWS if any(r in v for v in bs.values())]
        bs_lines.append(f"\n  BALANCE SHEETS, {len(bs)} fiscal year-ends ({a.currency} millions; first-filed XBRL "
                        f"vintage, transcription only; read the filed statements)")
        bs_lines.append("    year-end    " + "".join(f"{c:>12}" for c in cols))
        for e, v in bs.items():
            bs_lines.append(f"    {e}  " + "".join(
                f"{v[c][0] / 1e6:>12,.0f}" if c in v else f"{'-':>12}" for c in cols))
        accns = sorted({acc for v in bs.values() for _, acc in v.values()})
        bs_lines.append("    accessions: " + ", ".join(accns))
        print("\n".join(bs_lines))
    else:
        print(f"\n  BALANCE SHEETS: no annual {a.currency} instant facts found; read them from the filings")

    print("\n  STILL OWED BEFORE THE VALUE QUESTION OPENS:")
    print("    - read the balance sheets over the years above BEFORE the income account (v5 Q4)")
    print("    - read the filing: MD&A, cash-flow detail lines, footnotes; record accession no.")
    print("    - cross-check one figure above against the filed statement")
    print("    - say where in the capex band maintenance sits, and why, citing the filing")
    print("    - fill the competitor row from the competitors' own filings")

    if a.write:
        today = date.today().isoformat()
        if a.framework == "v5":
            tpl = open(os.path.join(ROOT, "Test Runs", "_TEMPLATE - Company Run.md"),
                       encoding="utf-8").read()
            tpl = tpl.replace("<COMPANY>", name).replace("<TICKER>", t).replace("<YYYY-MM-DD>", today)
            tbl = "\n".join(
                f"  {r['fy']}  OCF {r['ocf']:,.0f}  SBC {r['sbc']:,.0f}  D&A {r['da']:,.0f}  "
                f"capex {r['capex']:,.0f}  ->  owner cash {r['oe_lo']:,.0f} .. {r['oe_hi']:,.0f}"
                for r in oe["rows"])
            block = (f"\n  run.py arithmetic ({oe['unit']}M), {today}: price {px:,.2f}; shares {shares/1e6:,.3f}M; "
                     f"cap {cap/1e6:,.0f}M; sovereign {sov:.2f}% ({sov_date}, {sov_src})\n{tbl}\n"
                     f"  {a.years}-yr mean owner cash {oe['mean_lo']:,.0f} .. {oe['mean_hi']:,.0f}; "
                     f"yield {y_lo:.2f}% .. {y_hi:.2f}%\n"
                     + ("\n".join(bs_lines) + "\n" if bs_lines else ""))
            marker = "  capex and D&A, SBC resolved and complete."
            tpl = tpl.replace(marker, marker + block, 1)
            out = os.path.join(ROOT, "Test Runs", f"{today} Run - {t} {name}.md")
            if os.path.exists(out):
                print(f"\n  NOT WRITTEN: {out} exists"); return 0
            with open(out, "w", encoding="utf-8", newline="\n") as f:
                f.write(tpl)
            print(f"\n  written: {out}")
            return 0
        tpl = open(os.path.join(ROOT, "Test Runs",
                                "_ARCHIVE - Company Run TEMPLATE v4.1 (superseded 2026-10-05).md"),
                   encoding="utf-8").read()
        tpl = tpl.replace("[COMPANY]", name).replace("[TICKER]", t).replace("[DATE]", today)
        tbl = "\n".join(
            f"  {r['fy']}  OCF {r['ocf']:,.0f}  SBC {r['sbc']:,.0f}  D&A {r['da']:,.0f}  "
            f"capex {r['capex']:,.0f}  ->  OE {r['oe_lo']:,.0f} .. {r['oe_hi']:,.0f}"
            for r in oe["rows"])
        tpl = tpl.replace(
            "- rate ____ % · date ____ · source (issuing authority) ____",
            f"- rate **{sov:.2f}** % · date **{sov_date}** · source **{sov_src}**")
        tpl = tpl.replace(
            "- Owner earnings by year: ____",
            f"- Owner earnings by year ({oe['unit']}M):\n{tbl}\n"
            f"  **{a.years}-yr mean: {oe['mean_lo']:,.0f} .. {oe['mean_hi']:,.0f}**")
        tpl = tpl.replace(
            "- owner earnings ____ ÷ market cap ____ = **____ %** · sovereign **____ %**",
            f"- owner earnings **{oe['mean_lo']:,.0f}..{oe['mean_hi']:,.0f}** ÷ market cap "
            f"**{cap:,.0f}** = **{y_lo:.2f}..{y_hi:.2f} %** · sovereign **{sov:.2f} %**")
        tpl = tpl.replace(
            "- year-1 growth needed to justify the quote: **____ %**",
            f"- year-1 growth needed to justify the quote: **{g_imp*100:.1f} %**")
        tpl = tpl.replace(
            "- return at the current price = **____ points over the sovereign**",
            f"- return at the current price = **{pts_lo:+.2f} .. {pts_hi:+.2f} points over "
            f"the sovereign**")
        out = os.path.join(ROOT, "Test Runs", f"{today} Run - {t} ({name}).md")
        with open(out, "w", encoding="utf-8") as f:
            f.write(tpl)
        print(f"\n  wrote {os.path.relpath(out, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
