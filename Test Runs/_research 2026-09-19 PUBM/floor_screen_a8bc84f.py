#!/usr/bin/env python3
"""FLOOR SCREEN â€” COMPUTATION, NOT A CLEARANCE (operator rule 3).

WHAT THIS IS NOT: it is not a verdict machine, it does not open or close any of the six
questions, and it cannot produce an OUT on a business. Every number below is a Q5-shaped
computation produced BEFORE Q1-Q4 have been asked, so under operator rule 3 it carries no
entry language and no clearance of any kind.

WHAT IT IS FOR: reading order. After 28 full v4.1 runs, seven businesses cleared every
gate and ALL SEVEN failed on price, most without their owner-earnings yield even reaching
the 30-year Treasury. A full run costs ~300-400k tokens. Spending that on a name whose
price cannot clear the [E4-28] floor even on generous inputs is the error [E4-46] warns
about from the other direction: the answer is already available in five minutes.

So this computes, for every name, from SEC XBRL only:
  owner earnings   = mean(OCF - SBC - (c)) over the 5-year and 3-year windows,
                     (c) shown at BOTH the D&A default [E3-44] and total capex,
  bottom boundary  = the lowest of those four constructions [E5-34],
  yield            = bottom boundary / house-rule market cap,
  required growth  = the perpetual growth needed to reach a ~10% expectancy [E4-28],
  window spread    = the [E4-25] width, which is itself a finding.

Then it sorts by required growth. Names needing more than the corpus's own base rate
([E4-35]: fewer than 10 of the 200 most profitable companies sustained 15%/yr for 20
years) are DEFERRED with a computed re-read band, not judged. Names whose price could
plausibly clear the floor go to the front of the reading queue and get the full six
questions, where the business - not this arithmetic - decides.

Usage: python floor_screen.py            # the 78 clean dividend growers
       python floor_screen.py --read     # every READ name in the prepped list
"""
import csv, json, os, sys, time
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
_ARGV = sys.argv[1:]
sys.argv = [sys.argv[0]]
import bt17_microcap as M  # noqa: E402
import dividend_integrity as DI  # noqa: E402

TODAY = date.today()
FLOOR = 0.10           # [E4-28] the quit point
BASE_RATE = 0.15       # [E4-35] what fewer than 10 of 200 great companies sustained

OCF_TAGS = ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
SBC_TAGS = ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"]
CAPX_TAGS = ["PaymentsToAcquirePropertyPlantAndEquipment",
             "PaymentsToAcquireProductiveAssets",
             "PaymentsForCapitalImprovements"]
DA_TAGS = ["DepreciationDepletionAndAmortization",
           "DepreciationAmortizationAndAccretionNet",
           "DepreciationAndAmortization",
           # The bare element, added 2026-09-01 after the BBWI run. Bath & Body Works tags
           # its post-separation D&A as plain `Depreciation`, so this list resolved only on
           # the older, Victoria's-Secret-inclusive years and the series simply STOPPED at
           # the last contaminated one. That put capex/D&A at 1.55x when the clean windows
           # are 1.06x and 0.95x - i.e. it reported the CAPEX end as conservative when on
           # the three-year window the D&A end is. This list decides the [E3-44] direction
           # for every name, so a missing element here silently mis-states (c) everywhere.
           "Depreciation"]


# A foreign private issuer files a 20-F, not a 10-K, and this screen was silently dropping
# every one of them: the 2026-09-01 watchlist pass returned "only 0 filed years" for Toyota,
# Sony, Honda, TSMC, ASML, UMC, Ericsson, Spotify, Stellantis, GlobalFoundries and Mercedes.
# Eleven real businesses discarded by a form-code filter, not by any judgment about them.
# 40-F is the Canadian equivalent. The statements are IFRS rather than US GAAP, which is a
# reason to READ them differently, not a reason to be unable to see them at all.
ANNUAL_FORMS = ("10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A")


def annual(facts, tags):
    """{fiscal_end: value} from annual durations, earliest-filed per end. Reads the us-gaap
    namespace first, then ifrs-full, so foreign filers are priced rather than skipped."""
    ns = facts.get("facts", {})
    gaap = dict(ns.get("us-gaap", {}))
    for k, v in ns.get("ifrs-full", {}).items():
        gaap.setdefault(k, v)
    by_end = {}
    for tag in tags:
        for x in gaap.get(tag, {}).get("units", {}).get("USD", []):
            if x.get("form") not in ANNUAL_FORMS:
                continue
            s, e, f = x.get("start"), x.get("end"), x.get("filed")
            if not (s and e and f):
                continue
            sd, ed, fd = date.fromisoformat(s), date.fromisoformat(e), date.fromisoformat(f)
            if not (300 <= (ed - sd).days <= 380) or fd > TODAY:
                continue
            prev = by_end.get(ed)
            if prev is None or fd < prev[1]:
                by_end[ed] = (float(x["val"]), fd)
        if by_end:
            break          # first tag that yields data wins, like the run convention
    return {e: v for e, (v, _) in by_end.items()}


def chart_events(ticker, i):
    """Cached split history only - no new fetch (the prep run already cached these)."""
    import json as _j
    for tk in (ticker, ticker.replace(".", "-")):
        for suf in ("", "_20y", "_10y"):
            p = os.path.join(M.CACHE, f"chart_{tk}{suf}.json")
            if not os.path.exists(p):
                continue
            try:
                r = _j.load(open(p, encoding="utf-8"))["chart"]["result"][0]
            except Exception:
                continue
            out = []
            for ev in (r.get("events", {}).get("splits", {}) or {}).values():
                num, den = float(ev.get("numerator") or 0), float(ev.get("denominator") or 1)
                if num and den:
                    out.append((date.fromtimestamp(ev["date"]), num / den))
            return None, None, sorted(out)
    return None, None, []


def restatement_shift(facts, tags=None):
    """Largest disagreement between what a filer FIRST reported for a period and what it
    LAST reported for that same period end. Returns (ratio, fiscal_end) or None.

    THE THIRD PERIMETER GUARD, and the only one that can see a SPIN-OFF. Added 2026-09-01,
    designed by the BBWI run after both existing guards let Bath & Body Works through:

      * share_count_shift() CANNOT EVER detect a spin-off. The parent distributes shares in
        the SPUN entity; its own count is unchanged. The guard is structurally blind here,
        not merely mis-tuned.
      * scale_shift() was reading the series that had ALREADY been restated, so it saw a
        smooth revenue history and no step at all.

    What is actually observable is that the same period end carries TWO different values in
    two different accessions. BBWI restated FY2019 revenue from 12,914 to 5,405 and FY2020
    from 11,847 to 6,434 - a 58% disagreement that this test fires on.

    The sting, and the reason this is a flag rather than an adjustment: BBWI restated its
    INCOME STATEMENT and did not restate its CASH FLOW STATEMENT. Its own FY2021 10-K says
    so under the statement: "The cash flows related to discontinued operations have not been
    segregated. Accordingly, the Consolidated Statements of Cash Flows include the results of
    continuing and discontinued operations." So owner earnings built on that OCF mix two
    companies even though revenue looks clean. No arithmetic fixes that. Read the filing.
    """
    tags = tags or REV_TAGS
    ns = facts.get("facts", {})
    gaap = dict(ns.get("us-gaap", {}))
    for k, v in ns.get("ifrs-full", {}).items():
        gaap.setdefault(k, v)
    worst = None
    for tag in tags:
        by_end = {}
        for x in gaap.get(tag, {}).get("units", {}).get("USD", []):
            if x.get("form") not in ANNUAL_FORMS:
                continue
            s, e, f = x.get("start"), x.get("end"), x.get("filed")
            if not (s and e and f):
                continue
            sd, ed = date.fromisoformat(s), date.fromisoformat(e)
            if not (300 <= (ed - sd).days <= 380):
                continue
            by_end.setdefault(ed, []).append((date.fromisoformat(f), float(x["val"])))
        for ed, obs in by_end.items():
            if len(obs) < 2:
                continue
            obs.sort()
            first, last = obs[0][1], obs[-1][1]
            if first > 0 and last > 0:
                r = max(first / last, last / first)
                if worst is None or r > worst[0]:
                    worst = (r, ed)
        if by_end:
            break
    return worst


def shares_outstanding(facts, today=None):
    """(as_of_date, count), trying dei first and then the us-gaap/ifrs share tags.

    Added 2026-09-01. The watchlist pass returned "no share count" for META, Graham
    Holdings, DoorDash, UiPath and PubMatic - all large, current filers. The dei cover-page
    element is simply absent or stale for them, and a screen that cannot count the shares
    cannot compute a market cap, which is how Hamilton Beach came back at a cap of ZERO and
    a yield of 854,301%. Falling back to the balance-sheet count fixes the input; the
    caller still has to sanity-check the output.
    """
    today = today or TODAY
    ns = facts.get("facts", {})
    obs = []
    for tag, space in (("EntityCommonStockSharesOutstanding", "dei"),
                       ("CommonStockSharesOutstanding", "us-gaap"),
                       ("CommonStockSharesIssued", "us-gaap"),
                       ("NumberOfSharesOutstanding", "ifrs-full")):
        for x in ns.get(space, {}).get(tag, {}).get("units", {}).get("shares", []):
            e, v = x.get("end"), x.get("val")
            if e and v and float(v) > 0:
                obs.append((date.fromisoformat(e), float(v)))
        if obs:
            break
    if not obs:
        return None
    obs.sort()
    d, v = obs[-1]
    return (d, v) if (today - d).days <= 550 else None


def share_count_shift(facts):
    """Newest dei share count divided by the count ~2 years earlier.

    THE PERIMETER GUARD, added 2026-09-01 after the HON run. Honeywell completed its
    Aerospace spin-off and a 1-for-2 reverse split on 2026-06-29. The screen took a
    five-year owner-earnings mean that INCLUDED Aerospace (67-76% of pre-tax income)
    and divided it by a market cap that EXCLUDES it - two companies on either side of
    a division sign. 6.36% was really 1.97%.

    Yahoo's split feed did not carry the event, so this reads the share count itself,
    which cannot hide it: HON went 635.7M to 316.9M. Ordinary buybacks and issuance
    move a count a few percent a year; anything outside 0.75-1.50x over two years is a
    corporate action, and the name is returned unpriced rather than mis-priced.
    """
    pool = facts.get("facts", {}).get("dei", {}).get(
        "EntityCommonStockSharesOutstanding", {})
    obs = []
    for x in pool.get("units", {}).get("shares", []):
        e, v = x.get("end"), x.get("val")
        if e and v:
            obs.append((date.fromisoformat(e), float(v)))
    if len(obs) < 2:
        return None
    obs.sort()
    latest_d, latest_v = obs[-1]
    if (TODAY - latest_d).days > 550 or not latest_v:
        return None
    older = [(d, v) for d, v in obs if (latest_d - d).days >= 550]
    if not older:
        return None
    return latest_v / older[-1][1]


REV_TAGS = ["RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax",
            "Revenues", "SalesRevenueNet"]


def scale_shift(facts):
    """Largest year-over-year revenue ratio inside the owner-earnings window.

    THE SECOND PERIMETER GUARD, added 2026-09-01 after the Amentum and Smurfit Westrock
    reads. share_count_shift() catches a spin-off or a reverse split because both move the
    share count. It is BLIND to the opposite corporate action: a merger that creates a new
    filer. Amentum passed the share-count guard at 1.005x and Smurfit Westrock at 1.008x,
    because each was a new registrant whose count has been stable since inception, while
    the business underneath tripled - Amentum's owner earnings went 18 to 495 across the
    Jacobs CMS combination, and Smurfit Kappa's 2022-23 years sit in the same mean as
    post-Westrock 2024-25.

    Revenue is the better perimeter proxy than owner earnings or the share count: a
    cyclical can double its cash flow honestly, but revenue rarely doubles organically in
    one year. Returns the maximum consecutive-year ratio, or None if fewer than two years
    are filed. The caller decides; this only measures.

    CONFESSION, and it is the reason filed_years() exists below. Measured on the two names
    that prompted this guard, it FAILS to catch either: Amentum steps 1.72x and Smurfit
    Westrock 1.75x, both under the 2.0x line, because each merger closed mid-fiscal-year
    and the step is split across two filings. What actually catches them is that both are
    four-year-old registrants. The 2.0x line is NOT tuned to catch them - moving it to
    1.65x would fit these three points and would be an invention dressed as a threshold,
    since Landstar steps 1.58x honestly on freight rates. This is kept as the weaker second
    net it is, and the years test is the one carrying the weight.
    """
    rev = annual(facts, REV_TAGS)
    ends = sorted(rev)[-6:]
    if len(ends) < 2:
        return None
    worst = 1.0
    for a, b in zip(ends, ends[1:]):
        lo, hi = rev[a], rev[b]
        if lo and hi and lo > 0 and hi > 0:
            worst = max(worst, hi / lo, lo / hi)
    return worst


def filed_years(facts):
    """How many annual OCF observations exist. A five-year mean over three filed years is
    not a five-year mean, and a tight spread across four years is a SHORT estimate rather
    than a well-determined one - the error made reading Ferguson's 2% spread."""
    return len(annual(facts, OCF_TAGS))


# Equipment acquired under a FINANCE lease never touches investing cash flow, so the
# cash-flow-statement capex line misses it. The LSTR run of 2026-09-01 found cash "purchases
# of operating property" understating capital acquired by ~$33M a year, taking
# capex/depreciation from the 0.43x this screen reported to 1.10x - the difference between
# "the D&A end is the conservative one" and "it is not". It always errs in the flattering
# direction.
#
# BUT THE SCREEN CANNOT FIX THIS BY ITSELF, AND THE ATTEMPT TO DO SO WAS WRONG. Measured
# across 84 priced names on 2026-09-01:
#   * Only RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability is unambiguous. It is
#     the ASC 842 element and means what it says. Adjust on it.
#   * CapitalLeaseObligationsIncurred is a LEGACY element that filers use inconsistently.
#     SHOE fires on it at $53-73M/yr, and the SHOE run had already established that its
#     leases are OPERATING and net to a $2.6M drag INSIDE operating cash flow. Adding that
#     to capex would double-count the same payments. Flag it; never compute with it.
#   * NoncashOrPartNoncashAcquisitionFixedAssetsAcquired1 is broader still and is not used.
#   * Landstar itself is NOT catchable here: its tag stops in 2018, so the finance leases the
#     run found are not in XBRL at any element. The run got them by reading the filing.
#
# That last point is operator rule 4 working as written - tagged data is transcription and
# screening, and no name reaches Q5 on XBRL alone. The tool's job is to raise the question,
# not to answer it: "every flag is a prompt to read, never a score" (operator rule 8).
FINLEASE_TAGS = ["RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability"]
FINLEASE_FLAG_TAGS = ["CapitalLeaseObligationsIncurred",
                      "NoncashOrPartNoncashAcquisitionFixedAssetsAcquired1"]


def capital_acquired(facts):
    """Cash capex PLUS unambiguous ASC 842 finance-lease additions, by year."""
    cash, lease = annual(facts, CAPX_TAGS), annual(facts, FINLEASE_TAGS)
    if not cash:
        return {}, {}
    return {e: abs(v) + abs(lease.get(e, 0.0)) for e, v in cash.items()}, lease


def lease_capex_flag(facts):
    """Returns a prompt-to-read string when a filer reports lease-financed asset additions
    under an element this screen refuses to compute with, sized against cash capex. Never a
    number that enters (c) - the reader decides after seeing the filing."""
    cash = annual(facts, CAPX_TAGS)
    legacy = annual(facts, FINLEASE_FLAG_TAGS)
    if not cash or not legacy:
        return None
    yrs = sorted(set(cash) & set(legacy))[-5:]
    if not yrs:
        return None
    c = sum(abs(cash[y]) for y in yrs)
    lg = sum(abs(legacy[y]) for y in yrs)
    if c <= 0 or lg / c < 0.10:
        return None
    return (f"LEASE-FINANCED ADDITIONS {lg / c:.0%} of cash capex under a legacy element - "
            f"READ THE LEASE NOTE before trusting (c). Finance leases belong in capex; "
            f"operating leases are already inside OCF and must NOT be added again.")


def da_annual(facts):
    """Total D&A by year, taking the LARGEST resolving element rather than the first.

    Added 2026-09-01 after the MCD check. annual() stops at the first tag that yields data,
    and for McDonald's that is DepreciationDepletionAndAmortization at $457M - a SUBCOMPONENT.
    The real charge is DepreciationAndAmortization at $2,199M. Total D&A is one add-back line
    in the cash-flow statement; a subcomponent is by construction smaller than the total, so
    taking the max across candidate elements is both the more correct reading and the one
    that fails safe: overstating D&A only lowers the D&A end, and the bottom boundary is a
    min() across constructions [E5-34] either way.

    What it was actually corrupting is the SPREAD. MCD's four constructions read 8,667 /
    6,364 / 9,271 / 6,512, a 46% width, on a D&A figure that was a quarter of the truth. The
    spread is a decision input - [E4-25] says the range width IS the finding, and it is what
    decides which names earn a full read - so a wrong width sends 400k-token runs to the
    wrong places.
    """
    out = {}
    for tag in DA_TAGS:
        for e, v in annual(facts, [tag]).items():
            if e not in out or abs(v) > abs(out[e]):
                out[e] = v
    return out


def owner_earnings(facts):
    ocf, sbc = annual(facts, OCF_TAGS), annual(facts, SBC_TAGS)
    capx, _lease = capital_acquired(facts)
    da = da_annual(facts)
    if not ocf:
        return None
    ends = sorted(ocf)[-5:]
    if len(ends) < 3:
        return None
    # THE E5-20 GUARD, added 2026-09-01 after the VZ run.
    # Verizon's $157bn of wireless licences are INDEFINITE-LIVED and are not amortised,
    # so its D&A charge contains nothing for the $58.4bn of spectrum it bought in five
    # years. Pricing it on OCF - D&A produced a 9.26% yield that the full run destroyed.
    # The framework had already ruled: for the capital-intensive class the D&A end is
    # "INVALID, not merely optimistic". So a name whose capex tag does not resolve must
    # NOT silently fall back to D&A - it is returned unpriced and flagged, because the
    # only construction available is the one the corpus forbids.
    out = {}
    for label, n in (("5y", 5), ("3y", 3)):
        w = ends[-n:]
        if len(w) < n:
            continue
        for cname, csrc in (("da", da), ("capex", capx)):
            vals = []
            for e in w:
                c = csrc.get(e)
                if c is None:
                    continue
                vals.append(ocf[e] - sbc.get(e, 0.0) - abs(c))
            if len(vals) == len(w):
                out[f"{label}_{cname}"] = sum(vals) / len(vals)
    if not any(k.endswith("_capex") for k in out):
        return "CAPEX_UNRESOLVED"
    return out or None


def main():
    src = os.path.join(HERE, f"{TODAY} PREPPED LIST.csv")
    if not os.path.exists(src):
        src = os.path.join(HERE, "2026-08-31 PREPPED LIST.csv")
    rows = [r for r in csv.DictReader(open(src, encoding="utf-8")) if r["status"] == "READ"]
    tick = M.cached_json("company_tickers.json", "https://www.sec.gov/files/company_tickers.json")
    sec = {str(v["ticker"]).upper(): int(v["cik_str"]) for v in tick.values()}
    sov = (M.dgs30_asof(TODAY) or 5.2) / 100.0
    print(f"FLOOR SCREEN â€” COMPUTATION, NOT A CLEARANCE   {TODAY}")
    print(f"sovereign {sov:.2%} (FRED DGS30) Â· floor {FLOOR:.0%} [E4-28] Â· "
          f"base rate {BASE_RATE:.0%} [E4-35]\n")

    # restrict to the clean dividend growers unless --read
    universe = None
    if "--read" not in _ARGV:
        universe = set()
        for r in rows:
            d = DI.divs(r["ticker"])
            if not d:
                continue
            from collections import defaultdict
            by_year = defaultdict(list)
            for ts, amt in d:
                by_year[time.gmtime(ts).tm_year].append(amt)
            now = time.time()
            def ttm(off):
                return sum(a for ts, a in d
                           if now - (off+1)*365*86400 < ts <= now - off*365*86400)
            if ttm(0) <= 0:
                continue
            last = round(d[-1][1], 4)
            streak = 0
            for ts, amt in reversed(d):
                if round(amt, 4) == last:
                    streak += 1
                else:
                    break
            recent = [y for y in sorted(by_year) if y >= TODAY.year - 6]
            if [y for y in recent[:-1] if len(by_year[y]) < 4] or streak >= 8:
                continue
            if not (sum(by_year.get(2019, [])) or sum(by_year.get(2018, []))):
                continue
            universe.add(r["ticker"])
        print(f"universe: {len(universe)} clean dividend growers\n")

    out, skipped, unpriced = [], 0, []
    for i, r in enumerate(rows):
        t = r["ticker"]
        if universe is not None and t not in universe:
            continue
        key = next((k for k in (t, t.replace(".", "-")) if k in sec), None)
        if key is None:
            skipped += 1
            continue
        p = os.path.join(M.CACHE, f"facts_{sec[key]}.json")
        if not os.path.exists(p):
            skipped += 1
            continue
        try:
            facts = json.load(open(p, encoding="utf-8"))
        except Exception:
            skipped += 1
            continue
        oe = owner_earnings(facts)
        cap = float(r["cap_m"]) * 1e6 if r["cap_m"] not in ("", None) else None
        if oe == "CAPEX_UNRESOLVED":
            unpriced.append((t, r["name"][:30], "capex tag unresolved - only the D&A end"
                             " is available and the corpus calls it INVALID [E5-20]"))
            continue
        # THE PERIMETER GUARD, added 2026-09-01 after the HON run.
        # Honeywell completed its Aerospace spin-off and a 1-for-2 reverse split on
        # 2026-06-29. The screen took a five-year owner-earnings mean that INCLUDED
        # Aerospace (67-76% of pre-tax income) and divided it by a market cap that
        # EXCLUDES it - two companies on either side of a division sign. 6.36% was
        # really 1.97%. A corporate action inside the window means the numerator and
        # the denominator are not the same company, so the name is returned unpriced.
        ratio = share_count_shift(facts)
        if ratio is not None and not (0.75 <= ratio <= 1.50):
            unpriced.append((t, r["name"][:30],
                             f"share count is {ratio:.2f}x its level ~2 years ago - a split, "
                             f"spin-off or major issuance means the filed history and the "
                             f"current cap may be different perimeters"))
            continue
        if not oe or not cap:
            skipped += 1
            continue
        vals = list(oe.values())
        bottom, top = min(vals), max(vals)
        spread = (top - bottom) / bottom if bottom > 0 else None
        y_bottom = bottom / cap
        y_top = top / cap
        req = FLOOR - y_bottom            # perpetual growth needed on the bottom boundary
        out.append(dict(ticker=t, name=r["name"][:30], cap_m=r["cap_m"],
                        oe_bottom_m=round(bottom/1e6), oe_top_m=round(top/1e6),
                        spread=round(spread, 3) if spread is not None else "",
                        yield_bottom=round(y_bottom, 4), yield_top=round(y_top, 4),
                        vs_sovereign=round(y_bottom - sov, 4),
                        growth_required=round(req, 4),
                        div_yield=r["div_yield"], statute=r["statute_yield"]))

    out.sort(key=lambda x: x["growth_required"])
    dest = os.path.join(HERE, f"{TODAY} FLOOR SCREEN.csv")
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader(); w.writerows(out)

    print(f"{'tick':6s} {'capM':>8s} {'OE bottom':>10s} {'yield':>7s} {'vs bond':>8s} "
          f"{'growth req':>10s} {'spread':>7s}  name")
    for x in out[:45]:
        sp = f"{x['spread']:.0%}" if x["spread"] != "" else "    -"
        print(f"{x['ticker']:6s} {x['cap_m']:>8} {x['oe_bottom_m']:>10,} "
              f"{x['yield_bottom']:>7.2%} {x['vs_sovereign']:>+8.2%} "
              f"{x['growth_required']:>10.2%} {sp:>7s}  {x['name']}")
    plausible = [x for x in out if x["growth_required"] <= BASE_RATE * 0.4]
    if unpriced:
        print(f"\nUNPRICED - the arithmetic would be dishonest ({len(unpriced)}):")
        for row in unpriced:
            print(f"   {row[0]:6s}  {row[1]:30s}  {row[2]}")
    print(f"\n{len(out)} priced ({skipped} lacked usable XBRL).")
    print(f"**{len(plausible)} need <=6% perpetual growth to reach the floor** â€” the only "
          f"names where a full run could plausibly end in anything but a price failure.")
    print(f"WROTE {dest}")


if __name__ == "__main__":
    main()



