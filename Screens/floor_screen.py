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


def live_sovereign():
    """TODAY's USD 30-year, from the ISSUING AUTHORITY. Returns (rate_fraction, source).

    THE THIRD PLACE THE FRED DEFECT LIVED, and the one that needed a different fix.
    The UAL run of 2026-09-02 found `tools/sources.py` naming FRED as the USD source four
    lines under its own comment saying "never an aggregator"; that file was corrected to
    the Treasury daily par curve. This screen was still calling `bt17_microcap.dgs30_asof`,
    which is also FRED.

    BUT dgs30_asof MUST NOT BE CHANGED, and the reason is worth writing down. It takes an
    ANCHOR DATE and returns the rate as of that date - it is the BACKTEST's point-in-time
    path, and FRED's full-history CSV is genuinely the right instrument for that, because
    the Treasury endpoint serves one year at a time. Operator rule 5 wants the issuing
    authority for a LIVE rate; a historical series read for a dated anchor is a different
    job. So the fix goes here, at the live call site, and leaves the backtest alone.

    FRED remains the fallback and is LABELLED as one, so the run file records which rung of
    the evidence ladder produced the number.
    """
    try:
        sys.path.insert(0, os.path.join(ROOT, "tools"))
        import sources as S
        pct, when, src = S.sovereign("USD")
        return pct / 100.0, f"{src}, {when}"
    except Exception as e:
        v = M.dgs30_asof(TODAY)
        if v:
            return v / 100.0, f"FRED DGS30 (FALLBACK - issuing authority unreachable: {e})"
        return None, "UNAVAILABLE"

OCF_TAGS = ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]

# DISCONTINUED-OPERATIONS CASH IS NOT OWNER EARNINGS, found by the AMD run 2026-09-07.
# The FIRST tag above is the TOTAL, and for a filer with discontinued operations it
# INCLUDES cash the continuing business will never earn again. AMD's XBRL total reads
# $7,709M where the filed statement reads continuing $6,493M / discontinued $1,216M -
# and because the union rule lets the earlier tag win, the screen took the total. It
# overstated AMD's own CONSERVATIVE end by 26.3%, which is the flattering direction and
# the one [E5-34] exists to prevent. Subtracted where separately tagged.
OCF_DISCONTINUED_TAGS = [
    "CashProvidedByUsedInOperatingActivitiesDiscontinuedOperations",
    "NetCashProvidedByUsedInOperatingActivitiesDiscontinuedOperations"]


def ocf_continuing(facts):
    """Operating cash flow with separately-tagged discontinued-operations cash removed.

    Returns ({fiscal_end: value}, note). The note is empty unless something was removed,
    so a run can see that the correction happened rather than inferring it."""
    total = annual(facts, OCF_TAGS)
    disc = annual(facts, OCF_DISCONTINUED_TAGS)
    if not disc:
        return total, ""
    out, removed = {}, 0.0
    for e, v in total.items():
        d = disc.get(e)
        if d:
            out[e] = v - d
            removed += abs(d)
        else:
            out[e] = v
    return out, (f"discontinued-operations cash removed from OCF in "
                 f"{sum(1 for e in total if disc.get(e))} of {len(total)} years "
                 f"(${removed/1e6:,.0f}M total) - the XBRL total tag includes cash the "
                 f"continuing business will not earn again")
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

# THE COMPONENT/TOTAL SPLIT, found by the CGNX run of 2026-09-07 and present in BOTH paths.
# da_annual() took the LARGEST resolving element, which is right when a filer tags a
# SUBCOMPONENT and a TOTAL (the MCD case: DepreciationDepletionAndAmortization $457M against
# DepreciationAndAmortization $2,199M, and the total is never smaller). It is WRONG when a
# filer tags two COMPONENTS AND NO TOTAL. Cognex tags Depreciation $20.3M and
# AmortizationOfIntangibleAssets $10.5M against a filed $30.8M, and the max rule returned
# $20.3M - 34% low, on the (c) end that decides the D&A construction.
#
# So the rule is now: prefer a filed TOTAL; where none exists, SUM the components.
# CostOfGoodsAndServicesSoldDepreciationAndAmortization is deliberately NOT a component -
# it is the COGS portion only, and adding it would double-count.
DA_TOTAL_TAGS = ["DepreciationDepletionAndAmortization",
                 "DepreciationAmortizationAndAccretionNet",
                 "DepreciationAndAmortization"]
DA_COMPONENT_TAGS = ["Depreciation", "AmortizationOfIntangibleAssets"]


# A foreign private issuer files a 20-F, not a 10-K, and this screen was silently dropping
# every one of them: the 2026-09-01 watchlist pass returned "only 0 filed years" for Toyota,
# Sony, Honda, TSMC, ASML, UMC, Ericsson, Spotify, Stellantis, GlobalFoundries and Mercedes.
# Eleven real businesses discarded by a form-code filter, not by any judgment about them.
# 40-F is the Canadian equivalent. The statements are IFRS rather than US GAAP, which is a
# reason to READ them differently, not a reason to be unable to see them at all.
ANNUAL_FORMS = ("10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A")


# WHICH FILING OF A RESTATED PERIOD WINS, module-wide. See annual()'s docstring.
# "earliest" is what was knowable THEN and is the default, so nothing anchored in the past
# changes by my hand. A LIVE caller pricing a company today sets this to "newest" - the
# restatement is public, and reading the withdrawn figure is the error. regen_queue.py does.
VINTAGE = "earliest"


def annual(facts, tags, vintage=None):
    """{fiscal_end: value} from annual durations, earliest-filed per end. Reads the us-gaap
    namespace first, then ifrs-full, so foreign filers are priced rather than skipped.

    A TAG LIST IS A UNION, NOT A PRIORITY WITH AN EARLY EXIT. Corrected 2026-09-02.

    The previous version wrote `if by_end: break` - the first tag yielding ANY data won and
    the rest were never read. THIS EXACT DEFECT WAS FOUND AND FIXED IN `tools/sources.py` ON
    2026-08-27, on Apple, and the fix was never propagated to this file. The screen has been
    running with it ever since.

    What it costs, measured on the 379-name queue when the staleness gate exposed it:
      * AIR PRODUCTS tags annual operating cash flow under the plain element only through
        FY2011 and under ...ContinuingOperations from FY2012 on. The screen took THREE YEARS
        ENDING 2011 and stopped. It priced a live 2026 quote against a fifteen-year-old
        cash-flow statement.
      * BDX stopped at 2021-09-30, ESI at 2022-12-31, on the same mechanism. All three filed
        annual reports within the last ten months.

    Earlier tags in the list still win for any period BOTH cover, so a primary concept is
    never overwritten by a fallback - that is the sources.py convention, reproduced here so
    the two agree.

    VINTAGE - WHICH FILING OF A RESTATED PERIOD WINS. Found by the DELL run of 2026-09-07.
    SEC companyfacts carries EVERY vintage of a restated figure under the same period end,
    and this function kept the EARLIEST. Dell's Boomi divestiture line was -$3,957M as
    originally filed and RESTATED to +$16.0M in the FY2024 10-K, and the screen was reading
    the WITHDRAWN one - which is how acquisition_flag() reported a $4,237M perimeter against
    a true $296M. Measured across the priced queue: 278 of 361 names carry at least one
    restated annual value in the owner-earnings tags.

    THIS IS A PARAMETER RATHER THAN A FIX, BECAUSE THE TWO USES WANT OPPOSITE ANSWERS and
    choosing one silently is precisely how the look-ahead bug voided four backtests:
      * "earliest" - what was knowable THEN. Correct for anything anchored in the past.
        THE DEFAULT, so no existing caller changes behaviour by my hand.
      * "newest"   - what is known NOW. Correct for a LIVE screen pricing a company today,
        where a restatement is public and reading the withdrawn figure is the error.
    The live path (`regen_queue.py`) passes "newest". `tools/pit.py` remains the real anchor
    guard for anything historical: it REFUSES facts by `filed <= anchor` rather than
    trusting a caller's flag.
    """
    vintage = vintage or VINTAGE
    ns = facts.get("facts", {})
    gaap = dict(ns.get("us-gaap", {}))
    for k, v in ns.get("ifrs-full", {}).items():
        gaap.setdefault(k, v)
    by_end = {}
    for rank, tag in enumerate(tags):
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
            # A period already claimed by an EARLIER tag is never overwritten by a later
            # one. Within the same tag, `vintage` decides which FILING of a restated period
            # wins - see the docstring. Default "earliest" leaves every existing caller
            # unchanged; the live screen passes "newest".
            if prev is None or (rank == prev[2] and
                                (fd > prev[1] if vintage == "newest" else fd < prev[1])):
                by_end[ed] = (float(x["val"]), fd, rank)
    return {e: v for e, (v, _, _) in by_end.items()}


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
                    # Pre-1970 epoch guard, ported from sources.split_factor_after on
                    # 2026-09-04 after the TGT run crashed here: Windows raises OSError on
                    # negative timestamps, and Target's split feed carries a 1960s event.
                    # A pre-1970 split is older than any anchor this screen uses, so
                    # skipping it is correct rather than merely safe.
                    try:
                        out.append((date.fromtimestamp(ev["date"]), num / den))
                    except (OSError, OverflowError, ValueError):
                        continue
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


def share_class_flag(cik, ticker_map):
    """Warn when a CIK maps to more than one listed ticker, i.e. multiple share classes.

    THE STAGE 0(a) GUARD, added 2026-09-02 after the Ford run. The framework's Stage 0 has
    always required the cap to be taken ACROSS ALL SHARE CLASSES. The screen never did it,
    and the Ford run found the consequence: 3,916,743,591 Common plus 70,852,076 Class B is
    3,987,595,667 economic shares, so the cap is $55,188M and not the $51,810M this screen
    reported. Berkshire B came back at a $473M cap and a 4,683% yield from the same defect.

    AND IT CANNOT BE FIXED BY ARITHMETIC HERE. The SEC companyfacts API STRIPS DIMENSIONS,
    so per-class counts are simply not in the data: Ford's us-gaap share tags stop in 2009,
    Berkshire's dei count stops in 2011, and Under Armour, Lennar and McCormick report no dei
    count at all. There is no sum to take.

    So this returns a PROMPT TO READ rather than a number, which is what operator rule 8
    requires of a tool: "every flag is a prompt to read, never a score". It catches classes
    that are separately LISTED (GOOG/GOOGL, BRK-A/BRK-B). It CANNOT catch a class that is not
    publicly traded, which is exactly Ford's Class B - that one is visible only on the filing
    cover page, and only Stage 0 in the run will ever find it. Recorded as a known limit, not
    papered over.
    """
    others = sorted({t for t, c in ticker_map.items() if c == cik})
    if len(others) < 2:
        return None
    # Split the siblings by what they actually are. A preferred or a warrant is NOT another
    # class of common to add into a common-equity market cap - the first version of this
    # guard flagged Ford's F-PB/-PC/-PD preferreds and OXY-WT warrants as share classes,
    # which is wrong. They matter for a different reason and get their own flag.
    common, senior, warrants = [], [], []
    for t in others:
        u = t.upper()
        # Deliberately simple. A cleverer rule mis-sorted Alphabet's GOOGM and GOOGN as
        # preferreds because they end in a letter that follows a base ticker. Only the
        # explicit "-P" convention is treated as senior; everything else that is not a
        # warrant is treated as another class of common, which errs toward flagging.
        # Erring toward a flag is the right direction: the output is a prompt to read.
        if u.endswith(("W", "WT", "WS", "WW")) and len(u) > 3:
            warrants.append(t)
        elif "-P" in u:
            senior.append(t)
        else:
            common.append(t)
    msgs = []
    if len(common) > 1:
        msgs.append(f"MULTIPLE COMMON CLASSES ({', '.join(common)}) - the cap counts ONE. "
                    f"Do Stage 0(a) by hand.")
    if senior:
        msgs.append(f"SENIOR CLAIMS LISTED AHEAD OF COMMON ({', '.join(senior)}) - the market "
                    f"cap does not see them; owner earnings accrue to the preferred first.")
    if warrants:
        msgs.append(f"WARRANTS OUTSTANDING ({', '.join(warrants)}) - dilution the share count "
                    f"does not carry.")
    return " | ".join(msgs) or None


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


def share_count_shift(facts, ticker=None):
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

    SPLITS ARE NOW DIVIDED OUT FIRST. Corrected 2026-09-02, found while regenerating the
    queue. Because the guard was deliberately built to work WITHOUT the split feed (HON's
    reverse split was missing from it), it was blind to the ordinary case as well - and a
    forward split is a corporate action that changes NOTHING economically. It was refusing
    to price five names on that basis alone:

        ORLY 14.01x  (15-for-1, 2025-06-10)     KLAC 9.83x (10-for-1, 2026-06-12)
        POWL  3.03x  (3-for-1,  2026-04-06)     MLI  1.94x (2-for-1,  2026-07-01)
        NEGG  0.06x  (1-for-20, 2025-04-07)

    ORLY was in the operator's tier-2 queue and was being read when this was found.

    This project's own settled market-cap formula already says market cap is
    SPLIT-INVARIANT - `cap = close(anchor) x shares(measurement) x splits AFTER
    measurement` - so a guard that treats a split as a perimeter change contradicts the
    rule it sits beside. The residual test is unchanged, so an event the feed MISSES still
    fires exactly as HON's did; nothing is given up by using the feed when it has the
    answer. PLCE remains flagged at 1.74x with NO split in the feed, which is the
    guard working as intended.
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
    older_d, older_v = older[-1]
    raw = latest_v / older_v
    if ticker:
        factor = 1.0
        for sd, ratio in chart_events(ticker, 0)[2]:
            if older_d < sd <= latest_d:
                factor *= ratio
        if factor != 1.0:
            return raw / factor
    return raw


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


def annual_instant(facts, tags):
    """{fiscal_end: value} for BALANCE-SHEET (instant) facts.

    `annual()` cannot read these at all: it filters on x["start"], and an instant fact has
    only an "end". That silent inability is why the capex-funding flag below needed its own
    reader - noted because any future guard wanting a balance-sheet series will hit it too.
    """
    ns = facts.get("facts", {})
    gaap = dict(ns.get("us-gaap", {}))
    for k, v in ns.get("ifrs-full", {}).items():
        gaap.setdefault(k, v)
    by_end = {}
    for rank, tag in enumerate(tags):
        for x in gaap.get(tag, {}).get("units", {}).get("USD", []):
            if x.get("form") not in ANNUAL_FORMS or x.get("start") or not x.get("end"):
                continue
            e = date.fromisoformat(x["end"])
            f = date.fromisoformat(x["filed"]) if x.get("filed") else None
            if f and f > TODAY:
                continue
            prev = by_end.get(e)
            if prev is None or (rank == prev[1] and f and prev[2] and f < prev[2]):
                by_end[e] = (float(x["val"]), rank, f)
    return {e: v for e, (v, _, _) in by_end.items()}


def capex_funding_flag(facts, window=5):
    """Gross plant growing faster than the cash capex line. A PROMPT TO READ.

    THE INTC DEFECT, found 2026-09-07. Intel reports part of its PP&E additions in
    FINANCING (partner-funded fab structures), so `PaymentsToAcquirePropertyPlantAndEquipment`
    MISSES ABOUT A FIFTH OF ITS CAPEX - FY2025 is $17,672M, not the $14,646M the screen
    reads. The financing-side line sits under a COMPANY-EXTENSION tag that companyfacts does
    not carry, so it cannot be added to CAPX_TAGS; the same wall the COKE royalty hit.

    What IS visible is the consequence: if gross PP&E grows materially faster than cumulative
    cash capex, plant is arriving by a route the capex line does not show. Disposals make the
    comparison noisy in the OTHER direction (they shrink gross book), so a reading above ~1.3
    is the conservative signature rather than a precise measure. Flags, never adjusts.

    CONFESSION, AND IT IS THE SAME SHAPE AS scale_shift's: THIS FLAG DOES NOT CATCH INTEL,
    THE CASE THAT MOTIVATED IT. Measured on the day it was written, INTC reads 0.81x - it
    does not fire - for two independent reasons, both worth knowing before trusting the
    flag anywhere:
      1. Intel's `PropertyPlantAndEquipmentGross` series in companyfacts STOPS AT 2022-12-31,
         so the window cannot reach FY2023-25 where the financing-classified additions
         actually sit. The balance-sheet series is staler than the cash-flow series.
      2. Retirements and disposals shrink the gross book against exactly the growth being
         measured, and Intel's are large (the Altera sale, the Ireland SCIP round trip).
    The threshold was NOT lowered to make Intel fire. A 1.3x line that catches 19 of 379
    names is a prompt to read; a line tuned until one known case passes it is an invention
    dressed as a guard, and this project deletes those. The honest statement is that the
    flag catches ONE ROUTE (plant arriving faster than the cash line records it) and misses
    another (a filer whose balance-sheet tagging lapses), and that operator rule 4 remains
    the only complete answer: the filing gets read.
    """
    gross = annual_instant(facts, ["PropertyPlantAndEquipmentGross"])
    cash, _lease = capital_acquired(facts)
    ends = sorted(set(gross) & set(cash))[-window:]
    if len(ends) < 3:
        return None
    growth = gross[ends[-1]] - gross[ends[0]]
    spend = sum(abs(cash[e]) for e in ends[1:])
    if spend <= 0 or growth <= 0:
        return None
    ratio = growth / spend
    if ratio < 1.3:
        return None
    return (ratio, growth, spend,
            f"gross PP&E grew ${growth/1e6:,.0f}M against ${spend/1e6:,.0f}M of cash capex "
            f"({ratio:.2f}x) - plant is arriving by a route the capex line does not show "
            f"(partner-funded structures, financing-classified additions, or acquired plant). "
            f"(c) IS UNDERSTATED. READ THE CASH-FLOW STATEMENT AND THE PP&E NOTE.")


def stale_filer(facts, max_age_days=800):
    """Newest annual OCF observation, and whether the filer has stopped reporting.

    THE TIME AXIS OF THE HAMILTON BEACH DEFECT, found by the AATC run of 2026-09-02. Every
    guard in this file watches the SHARE COUNT, the REVENUE or the PERIMETER for staleness.
    None of them watched the CLOCK. Autoscope Technologies filed Form 25 on 2023-01-06 and
    Form 15-12G on 2023-01-17 - it deregistered - so its last 10-K is FY2021 and its newest
    annual observation here is 2021-12-31. It sat in TIER 1 of the watchlist queue, priced
    at a live 2026 quote against a five-year-old cash-flow statement, and nothing in the
    screen noticed.

    The queue already keeps a "no share count" bucket. It needed a "no recent filing" one.
    Note what this does NOT do: deregistration is not a verdict on the business. AATC still
    publishes audited annual reports on its own site, which is a demoted-but-primary
    evidence class, and its run proceeded on them. This flag says the SCREEN cannot price
    the name, not that the name cannot be read.

    Returns (newest_end, age_days, note) or None if no annual OCF exists at all.
    """
    ocf = annual(facts, OCF_TAGS)
    if not ocf:
        return None
    newest = max(ocf)
    age = (TODAY - newest).days
    note = ""
    if age > max_age_days:
        note = (f"newest annual filing ends {newest} - {age/365.25:.1f} years old. The "
                f"quote is live and the statements are not. CHECK FOR A FORM 15 OR 25 "
                f"before treating any yield here as current.")
    return newest, age, note


ACQ_TAGS = ["PaymentsToAcquireBusinessesNetOfCashAcquired",
            "PaymentsToAcquireBusinessesAndInterestInAffiliatesNetOfCashAcquired",
            "PaymentsToAcquireBusinessesGross"]


def acquisition_flag(facts, cap=None, window=5):
    """A PROMPT TO READ, never an adjustment. Cash paid for businesses inside the window.

    THE THIRD PERIMETER CLASS, added 2026-09-02 after the DKS re-price. Dick's Sporting
    Goods completed the Foot Locker acquisition on 2025-09-08 for $2.5bn of consideration,
    against a business that had done $8bn of sales the prior year - about 60% of Dick's own
    size. The screen then divided eight years of standalone Dick's, plus a five-month
    loss-making stub that EXCLUDED Foot Locker's peak season, by the market cap of the fully
    combined company.

    NEITHER EXISTING GUARD COULD HAVE CAUGHT IT, and the reason is structural rather than a
    threshold that wants tuning:
      * share_count_shift() watches the equity, because Honeywell's spin-off moved it
        635.7M -> 316.9M. DKS paid CASH AND DEBT; its count went 93.8M -> 89.5M, 0.95x,
        comfortably inside the band. A guard on the equity cannot see a deal without equity.
      * scale_shift() watches revenue and reads 1.28x against a 2.0x line, only because the
        stub was five months long.
    Both guards watch CONSEQUENCES that a particular deal shape happens to produce. The
    event itself is tagged, so read it directly.

    THE LIMIT, STATED RATHER THAN HIDDEN. DKS's own acquisition line reads MINUS $257M in
    fiscal 2026, because Foot Locker's cash on hand exceeded the net cash paid - the $2.5bn
    of consideration is nowhere in the cash-flow statement. So on the name that prompted
    this, the flag fires on the SIGN, not the size, and on filers who pay in stock it will
    not fire at all. A screen cannot establish a perimeter; only the filing can
    (operator rule 4). This raises the question and refuses to answer it (operator rule 8).

    MEASURED ACROSS THE 379-NAME MASTER QUEUE, 2026-09-02, so the noise rate is on the
    record rather than assumed: 88 tag nothing, 72 land in the 5-15% band, 74 are at or
    above 15% of market cap, and 38 carry a negative sign. The read-the-filing tier is
    112 names, THIRTY PERCENT of the queue. That is a statement about the opportunity set -
    a third of these five-year windows contain a material acquisition - and not evidence
    that the flag is mis-set.

    A CONJUNCTION WAS TESTED AND REFUSED. Gating the negative branch on a revenue step as
    well ("negative sign AND scale_shift >= 1.20") catches DKS and drops DELL, COKE, ECL
    and GS - but it still passes PLTR, CLNE and FSI, whose revenue stepped 55-64%
    ORGANICALLY. Fixing that would need a third parameter fitted to a handful of points,
    which is the invention this project deletes rather than the guard it needs. The
    negative sign means one thing and means it in all 38 cases: THE CONSIDERATION IS NOT IN
    THIS STATEMENT. A false positive costs the reader one glance at a small number. Missing
    DKS cost a tier assignment.

    THE RECENCY DEFECT, FOUND BY THE AATC RUN OF 2026-09-02 AND FIXED HERE. The first
    version wrote `ends = sorted(acq)[-window:]`, which takes the last five PERIODS THE TAG
    HAPPENS TO CARRY, not the last five years. Autoscope's only tagged acquisition is a
    single payment in FISCAL 2010, and the flag duly reported it as "27% of market cap
    inside the window" - a SIXTEEN-YEAR-OLD event, on a company with no perimeter question
    at all. Worse, the run's brief inherited the error and stated it as fact.

    The window is now bounded by the OWNER-EARNINGS WINDOW ITSELF - the same annual OCF
    period ends that owner_earnings() means by "five years" - so the numerator and the
    perimeter test are measured over the same span by construction rather than by
    coincidence.

    Returns (total_cash, share_of_cap, note) or None when nothing is tagged IN THE WINDOW.
    """
    acq = annual(facts, ACQ_TAGS)
    if not acq:
        return None
    ocf_ends = sorted(annual(facts, OCF_TAGS))[-window:]
    if not ocf_ends:
        return None
    lo = min(ocf_ends)
    ends = [e for e in sorted(acq) if e >= lo]
    if not ends:
        return None
    vals = [acq[e] for e in ends]
    total = sum(abs(v) for v in vals)
    if not total:
        return None
    share = (total / cap) if cap else None
    pct = f"{share:.0%} of cap" if share is not None else "cap unknown"
    note = ""
    if any(v < 0 for v in vals):
        # SIGN CONVENTION, corrected by the DKS run of 2026-09-02. The XBRL element is a
        # PAYMENTS element, so an outflow is positive and a negative value means the cash
        # acquired exceeded the cash paid. On the FACE of DKS's statement that same fact
        # appears as a POSITIVE $257,095k inflow. Substance identical, presentation
        # opposite - so the note says what it means rather than naming a sign the reader
        # will not find in the filing.
        note = (f"NET CASH INFLOW on the acquisition line (${total/1e6:,.0f}M, {pct}) - "
                f"cash acquired exceeded cash paid, so the CONSIDERATION IS NOT IN THIS "
                f"STATEMENT AT ALL. READ THE BUSINESS COMBINATION NOTE.")
    elif share is not None and share >= 0.15:
        note = (f"acquisitions are ${total/1e6:,.0f}M, {pct}, inside the window - the "
                f"numerator and denominator may be different companies. READ THE FILING.")
    # THE ABSOLUTE-SIZE GATE, added 2026-09-06 after the AVGO run. Broadcom bought VMware
    # for $86.3bn - the largest perimeter event this project has met - and the flag stayed
    # SILENT, because $79.6bn of cash against a $1.7 TRILLION market cap is 4.7%, under the
    # 5% line. The percentage test is the right instrument for a small filer and the wrong
    # one for a mega-cap: a deal can be immaterial to the CAP and still be the largest
    # single fact in the file, because the owner-earnings NUMERATOR is what it changes.
    # Ten billion dollars of acquired business is worth reading about at any market cap.
    elif total >= 10e9:
        note = (f"acquisitions are ${total/1e6:,.0f}M inside the window ({pct}) - small "
                f"against the cap but LARGE IN ABSOLUTE TERMS. A deal this size changes "
                f"the owner-earnings numerator even when it is immaterial to the "
                f"denominator. READ THE BUSINESS COMBINATION NOTE.")
    elif share is not None and share >= 0.05:
        note = f"acquisitions are ${total/1e6:,.0f}M, {pct}, inside the window."
    return total, share, note


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


# CAPITALIZED SOFTWARE IS CAPEX ON A SEPARATE LINE, found by the HAS run 2026-09-03.
# Hasbro's cash-flow statement carries "Additions to software development" ($135.0M FY2025)
# BESIDE "Additions to property, plant and equipment" ($63.3M) - and the screen read only
# the second, overstating owner earnings for every filer that capitalizes software. These
# are ADDITIVE to PP&E capex, never an alternative tag for the same number, so they get
# their own list summed on top (the finance-lease pattern), NOT a fallback slot in
# CAPX_TAGS - a fallback would silently pick one line or the other per period.
SOFTWARE_CAPX_TAGS = ["PaymentsToDevelopSoftware", "PaymentsForSoftware",
                      "PaymentsToAcquireSoftware",
                      "PaymentsForCapitalizedInternalUseSoftware"]

# RECURRING ROYALTIES CLASSIFIED AS FINANCING, found by the COKE run 2026-09-04. Coca-Cola
# Consolidated pays The Coca-Cola Company $50-70M/yr of contingent consideration on the
# 2017 System Transformation - perpetual in practice, economically a royalty on the
# licensed territories - and it is classified as a FINANCING outflow, so it never touches
# operating cash flow and every OCF-based yield on such a filer is overstated. This is the
# SHOE/finance-lease class of problem: the tag is used inconsistently across filers (some
# contingent consideration is a genuine one-time earnout), so the screen FLAGS and never
# adjusts (operator rule 8) - a recurring multi-year series under this tag is the signature
# to read for.
# CONFESSED LIMIT, measured before adoption: the PAYMENT is often tagged under a COMPANY
# EXTENSION (coke:...), which companyfacts does not carry - the standard payment tags
# returned ZERO hits across the whole queue including COKE itself. What IS standard-tagged
# is the LIABILITY, and the signature that separates a royalty from an earnout is that an
# earnout amortizes to zero within a year or two while a royalty-shaped liability PERSISTS.
CONTINGENT_LIABILITY_TAGS = [
    "BusinessCombinationContingentConsiderationLiability",
    "BusinessCombinationContingentConsiderationLiabilityNoncurrent"]


def contingent_royalty_flag(facts):
    """(years_present, latest_balance, note) or None. A PROMPT TO READ, never an adjustment.

    Fires on a contingent-consideration LIABILITY that persists 4+ fiscal year-ends -
    the perpetual-royalty shape, not the earnout shape. The payment tags were tried first
    and are useless (see the confession above)."""
    ns = facts.get("facts", {}).get("us-gaap", {})
    ends = {}
    for tag in CONTINGENT_LIABILITY_TAGS:
        for x in ns.get(tag, {}).get("units", {}).get("USD", []):
            if x.get("form") in ANNUAL_FORMS and x.get("end") and x.get("val"):
                e = x["end"]
                if e not in ends or abs(x["val"]) > abs(ends[e]):
                    ends[e] = x["val"]
    years = sorted(ends)[-6:]
    live = [(e, ends[e]) for e in years if abs(ends[e]) > 0]
    if len(live) < 4:
        return None          # an earnout amortizes away; a royalty persists
    latest = live[-1][1]
    return (len(live), latest,
            f"a contingent-consideration LIABILITY has persisted {len(live)} fiscal "
            f"year-ends (latest ${latest/1e6:,.0f}M). An earnout amortizes to zero; a "
            f"balance that persists is the ROYALTY shape, its payments are usually in "
            f"FINANCING (often under a company-extension tag invisible here), and the OCF "
            f"this screen prices excludes them. READ THE ACQUISITION AND COMMITMENT NOTES.")


def capital_acquired(facts):
    """Cash capex PLUS software-development additions PLUS unambiguous ASC 842
    finance-lease additions, by year."""
    cash, lease = annual(facts, CAPX_TAGS), annual(facts, FINLEASE_TAGS)
    soft = annual(facts, SOFTWARE_CAPX_TAGS)
    if not cash:
        return {}, {}
    return ({e: abs(v) + abs(soft.get(e, 0.0)) + abs(lease.get(e, 0.0))
             for e, v in cash.items()}, lease)


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



def sbc_annual(facts):
    """Stock compensation by year, taking the LARGEST resolving element.

    A CHECKLIST ITEM THAT CANNOT BE A RULE, from the BA run of 2026-09-12. SBC THAT RESOLVES
    CAN STILL BE INCOMPLETE. Boeing settles its 401(k) match in stock: FY2025 carries $1,530M
    of it, and NOT ONE SBC ELEMENT CONTAINS IT - it sits under the generic equity-statement tag
    `StockIssuedDuringPeriodValueOther` ($1,233M, $1,215M, $1,515M, $1,601M, $1,530M for
    FY2021-25), while every SBC tag this function reads returns $427M. The BE defect was SBC
    that did not resolve; this is SBC that resolves and is a QUARTER of the truth.

    WHY NO GUARD IS ADDED, measured before deciding. `DefinedContributionPlanCostRecognized`
    is the obvious candidate and it does not work. Across the 331 priced names, 181 file it;
    it exceeds the SBC tag on 24 of them at 5% of operating cash and 9 at 10%. But BOEING's
    is settled in STOCK and AMAT's ($320M) and DAL's ($1,400M) are settled in CASH, and
    NOTHING IN THE TAGS DISTINGUISHES THE TWO. A cash match is an operating expense already
    correctly inside operating cash flow; a stock match is a non-cash add-back that must be
    subtracted. A flag firing on all three would be wrong twice out of three times, and
    operator rule 8 forbids a tool concluding which it is.

    SO IT IS A READING TASK, and this is where it is written down: when a filer's
    `StockIssuedDuringPeriodValueOther` or defined-contribution cost is large against its SBC
    tag, OPEN THE EQUITY STATEMENT AND THE BENEFIT-PLAN NOTE and find out how the match is
    paid. Confirmed stock-settled: BA. Confirmed material and cash-settled: AMAT, DAL.

    Direction, for anything already run: an understated subtraction OVERSTATES owner earnings,
    so an affected name looked CHEAPER than it is and any failure holds a fortiori. AMAT (21st
    gate-clearer, failed on price by 3.99 points) is unaffected in substance for that reason.

    THE MCD DEFECT AGAIN, IN A NEW TAG, found by the CGNX run of 2026-09-07. annual() picks
    by RANK, so the first tag in SBC_TAGS wins - and for Cognex FY2020 that is
    ShareBasedCompensation at $1.40M against AllocatedShareBasedCompensationExpense at
    $42.66M, the filed figure. A 30x understatement on a line that is SUBTRACTED, so any
    window reaching 2020 overstated owner earnings by $41M in that year.

    max() is the right rule and it FAILS SAFE in both directions: a subcomponent can never
    exceed the total it belongs to, and because SBC is subtracted, preferring the larger
    value is the conservative end. Usually ShareBasedCompensation IS the cash-flow add-back
    total and the Allocated element is a per-plan detail; Cognex is the inversion, and rank
    cannot tell the two apart."""
    out = {}
    for tag in SBC_TAGS:
        for e, v in annual(facts, [tag]).items():
            if e not in out or abs(v) > abs(out[e]):
                out[e] = v
    return out

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
    totals = {}
    for tag in DA_TOTAL_TAGS:
        for e, v in annual(facts, [tag]).items():
            if e not in totals or abs(v) > abs(totals[e]):
                totals[e] = v
    parts = {}
    for tag in DA_COMPONENT_TAGS:
        for e, v in annual(facts, [tag]).items():
            parts[e] = parts.get(e, 0.0) + abs(v)
    out = dict(totals)
    for e, v in parts.items():
        # A filer that tags only COMPONENTS has no total to prefer, and a filer that tags
        # both is trusted on its own total unless the components plainly exceed it.
        if e not in out or v > abs(out[e]):
            out[e] = v
    return out


def da_discontinuity_flag(facts, ratio=4.0, floor_musd=5.0):
    """(year, factor, note) or None. A PROMPT TO READ, never an adjustment.

    THE SILENT-GARBAGE CASE, added 2026-09-07 after the CERT run. The CRWD run of the same
    day found da_annual() returning EMPTY for a filer, which fails loudly and gets noticed.
    Certara is worse: it returns 2.60, 2.44, 2.13, 1.73, 1.55, 1.99, 75.16 - a 38x
    discontinuity, unflagged - because the company consolidated two income-statement lines
    in FY2023 and THE TAG'S SEMANTICS CHANGED WHILE THE ELEMENT DID NOT. The published
    oe_bottom 28 / oe_top 35 reproduce to three decimals off that broken series, so nothing
    downstream looked wrong.

    An empty series fails loudly; a broken one does not. That is the whole reason this
    exists.

    WHY 4x, AND WHY IT IS NOT TUNED. Depreciation runs off a schedule: a book of assets does
    not quadruple in a year without an acquisition, a change of estimate, or a change in what
    the tag means - and all three are things the reader must go and read [operator rule 8].
    The threshold is deliberately left where it first caught Certara rather than tuned until
    the flag list looked tidy; tuning a detector against the cases you already know is how
    you get a detector that only finds them.

    THE MATERIALITY FLOOR IS A SEPARATE GUARD FROM THE RATIO, AND IT IS THE ACQUISITION-FLAG
    LESSON INVERTED. That flag's percentage test was right for a small filer and wrong for a
    mega-cap; a pure RATIO test is right for a large filer and meaningless for a micro-cap,
    where D&A going from $0.01M to $10M is arithmetic noise on a shell. Measured across 1,999
    cached filers the bare ratio fires on 10.7%, which is not a signal. Measured on the
    361-name priced queue: 4.2% at no floor, 1.9% at $5M, 1.4% at $25M. $5M is taken because
    it clears the shell universe while KEEPING small real filers - Certara's own owner
    earnings are ~$34M, so a $25M floor would protect exactly the size of company where (c)
    decides the file. The queue names it fires on at $5M are led by CERT at 37.7x.

    CONFESSED FALSE POSITIVES: this fires on genuine step-changes too - a large acquisition
    closing mid-year moves D&A by more than 4x at a small filer. It is a prompt to open the
    filing, and the cost of a false positive is one read. It also CANNOT see a semantics
    change that happens to be gradual, which is the case it would most want to catch."""
    da = da_annual(facts)
    if len(da) < 3:
        return None
    yrs = sorted(da)[-8:]
    worst = None
    for a, b in zip(yrs, yrs[1:]):
        lo, hi = abs(da[a]), abs(da[b])
        if lo <= 0 or hi <= 0:
            continue
        if max(lo, hi) < floor_musd * 1e6:
            continue                      # a ratio on a trivial base is noise, not a signal
        f = max(hi / lo, lo / hi)
        if f >= ratio and (worst is None or f > worst[1]):
            worst = (b, f, hi > lo)
    if worst is None:
        return None
    y, f, up = worst
    return (y, f, (f"the D&A series steps {f:.1f}x {'UP' if up else 'DOWN'} at {y} "
                   f"(${abs(da[yrs[yrs.index(y) - 1]])/1e6:,.0f}M to ${abs(da[y])/1e6:,.0f}M). "
                   f"Depreciation runs off a schedule and does not do this on its own. The "
                   f"three causes are an ACQUISITION, a CHANGE OF ESTIMATE, or a TAG whose "
                   f"SEMANTICS CHANGED WHILE THE ELEMENT DID NOT - the last is invisible "
                   f"here and was the Certara case, where two income-statement lines were "
                   f"consolidated in FY2023. READ THE CASH-FLOW STATEMENT AND NOTE 1 BEFORE "
                   f"USING EITHER END OF (c)."))


def owner_earnings(facts):
    ocf, _disc_note = ocf_continuing(facts)
    sbc = sbc_annual(facts)
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
    # SBC THAT DOES NOT RESOLVE IS NOT SBC OF ZERO. Found by the BE run of 2026-09-12, and it
    # is the worst class of defect this screen can have: a SILENT [E5-06] violation in the
    # NUMERATOR. Bloom Energy tags stock compensation as AllocatedShareBasedCompensationExpense
    # DIMENSIONED BY EXPENSE LINE, so an undimensioned annual fetch returns nothing after 2018 -
    # and `sbc.get(e, 0.0)` quietly substituted zero, omitting $70-200M a year and reproducing
    # the published band to the dollar while doing it. E5-06 is explicit that SBC is simply an
    # expense; a screen that drops it is not being conservative, it is overstating owner
    # earnings, which is the one direction that matters when the question is whether to buy.
    #
    # Measured across the 361 priced names over their last five OCF years: SBC resolves for
    # every year on 325, for SOME years on 14, and for NO year on 21 (MKL, MPLX, APLE, CTS,
    # CVX, NEU, PM, BRK-A, EME, TDY, GENC, BE, SEB, SO, UTL, NWN, TG, C and three MBIN
    # preferreds). Those 21 were priced with no stock compensation subtracted at all.
    #
    # So this REFUSES the window, exactly as CAPEX_UNRESOLVED does, rather than returning a
    # number that looks right. The reader goes to the filing; the dimensioned fact is not in
    # companyfacts at any rung, which is the same source limit as stock consideration and
    # grant-date SBC.
    if not sbc:
        return "SBC_UNRESOLVED"
    # SBC THAT RESOLVES CAN STILL BE INCOMPLETE, AND NOTHING HERE CAN DETECT THAT.
    # Found by the BA run of 2026-09-12, five days after the BE fix above, and it is the
    # HARDER half of the same defect class. BE's SBC tag returned NOTHING and was silently
    # zeroed; the guard above catches that, because absence is detectable. Boeing's
    # ShareBasedCompensation tag resolves cleanly for all 18 filed years -- and it is only
    # PART of the equity-settled pay, because Boeing's consolidated cash-flow statement
    # carries TWO non-cash compensation add-backs, not one:
    #
    #     Share-based plans expense                      426 / 407 / 690
    #     Treasury shares issued for 401(k) contribution  1,530 / 1,601 / 1,515
    #                                                    (FY2025 / FY2024 / FY2023)
    #
    # The second is the employee retirement match PAID IN SHARES instead of cash, added back
    # to operating cash flow for exactly the same reason SBC is. E5-06 ("to say
    # 'stock-based compensation' is not an expense is even more cavalier") and E3-70 (the
    # measure is market value, so the reported charge is the FLOOR of the subtraction) both
    # bind on it. Subtracting only the tagged line OVERSTATES owner earnings by $1.5-1.6bn a
    # year -- the one direction that matters when the question is whether to buy.
    # `StockIssuedDuringPeriodValueEmployeeBenefitPlan` carries it for FY2010-12 and FY2020
    # ONLY; from FY2021 the figure exists solely in the filed statement, at no rung of the
    # evidence ladder that this function can reach. Boeing also settled PENSION
    # contributions in stock ($3,000M / $2,048M / $952M in FY2020/21/22).
    #
    # WHY THERE IS NO CODE FIX HERE, deliberately. A refusal rule would need a heuristic for
    # "this tag looks too small", and every candidate produces false negatives across a
    # 331-name queue; a guard that cries wolf is worse than a documented hazard, and
    # operator rule 8 forbids a tool concluding anything. So this is a CHECKLIST item for
    # the reader, in E3-68's sense -- checklists are for coverage, formulas are refused:
    #
    #   READ EVERY LINE OF THE NON-CASH BLOCK IN THE CASH-FLOW STATEMENT. Do not assume
    #   `ShareBasedCompensation` is the whole of equity-settled pay. Benefits, pension
    #   contributions and 401(k) matches settled in shares all sit there, all are added back
    #   to OCF, and all must come out again.
    #
    # Boeing FY2025: total equity-settled compensation $1,956M against $1,065M of operating
    # cash flow -- 184%, the highest ratio recorded in this queue.
    out = {}
    for label, n in (("5y", 5), ("3y", 3)):
        w = ends[-n:]
        if len(w) < n:
            continue
        if any(e not in sbc for e in w):
            continue            # a partial window is refused too; see SBC_PARTIAL below
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
    if not out:
        return "SBC_PARTIAL"    # every window contained a year whose SBC did not resolve
    return out


WC_TAGS = ["IncreaseDecreaseInAccountsPayableAndAccruedLiabilities",
           "IncreaseDecreaseInAccountsPayable",
           "IncreaseDecreaseInContractWithCustomerLiability",
           "IncreaseDecreaseInDeferredRevenue"]


def working_capital_flag(facts, share=0.30):
    """(year, line, fraction_of_OCF, note) or None. A PROMPT TO READ, never an adjustment.

    THE OCF-IS-A-WORKING-CAPITAL-SERIES CASE, found twice in five days. DELL (2026-09-07):
    accounts payable ran +5,742 / -8,546 / -498 / +1,703 / +12,665 - a $21.2bn swing that was
    the entire distance between its worst owner-earnings year and its best. INOD
    (2026-09-12): H1 2026 operating cash of $164.4M carried a ~$116M customer prepayment,
    $71.9M of it through the payables line, so a trailing-twelve-month figure would report
    three times what the company earned. Neither is visible in a multi-year mean; both are
    visible in the line that produced them.

    Fires when a single working-capital line in the window moves by more than `share` of
    that year's operating cash. It says which year and which line, and stops. The reader
    decides whether it is a prepayment, a stretched payable, or a business whose cash
    conversion is genuinely lumpy - three different findings.

    A LIMIT, STATED: this reads ANNUAL facts, and Innodata's prepayment is a half-year fact
    that the annual screen cannot see until the FY2026 10-K. The place it is caught before
    then is tools/run.py's TTM, and only by a reader who opens the 10-Q liquidity note."""
    ocf, _ = ocf_continuing(facts)
    if not ocf:
        return None
    yrs = sorted(ocf)[-5:]
    worst = None
    for tag in WC_TAGS:
        ser = annual(facts, [tag])
        for y in yrs:
            v, o = ser.get(y), ocf.get(y)
            if v is None or not o:
                continue
            f = abs(v) / abs(o)
            if f >= share and (worst is None or f > worst[2]):
                worst = (y, tag, f)
    if worst is None:
        return None
    y, tag, f = worst
    # A RATIO AGAINST A NEAR-ZERO DENOMINATOR IS NOT A RATIO - the fourth time this defect class
    # has been found, and the first time in a flag I built myself, the same day. Measured
    # 2026-09-13: on 13 of the 150 names this fires on, the flagged YEAR's operating cash was
    # under 5% of the company's own five-year average. NEGG printed 6,992% on $0.8M of operating
    # cash against a $21.1M average; ORN 8,894% on $0.1M; ANF 4,915% on $2.3M against $452.6M.
    # The ROKU run had already diagnosed its own "351%" as exactly this - a denominator artifact.
    # The movement itself can still matter, so the flag still FIRES; in these cases it reports
    # the line in DOLLARS against the company's typical operating cash instead of the ratio.
    yrs_all = sorted(ocf)[-5:]
    scale = sum(abs(ocf[x]) for x in yrs_all) / len(yrs_all) if yrs_all else 0.0
    line_usd = abs(annual(facts, [tag]).get(y, 0.0))
    # CONCLUSION FIRST, AND SHORT (2026-09-13). The queue CSV truncates this note, and the first
    # near-zero version put its conclusion last - so NEGG's cell ended "...against a typi" and the
    # one sentence that mattered, that the ratio means nothing, never reached a brief. That is the
    # week's recurring defect class (a diagnostic that never reaches the reader), and it was
    # introduced by my own longer label. The IncreaseDecreaseIn prefix alone cost 18 characters.
    short = tag.replace("IncreaseDecreaseIn", "")
    yr = str(y)[:4]
    if scale and abs(ocf.get(y, 0.0)) < 0.05 * scale:
        return (y, tag, f, (f"RATIO MEANINGLESS - NEAR-ZERO OCF: {short} moved ${line_usd/1e6:,.1f}M in {yr} "
                            f"when OCF was ${abs(ocf[y])/1e6:,.1f}M against a typical |OCF| of "
                            f"${scale/1e6:,.1f}M. Judge the dollars, not the {f:,.0%}. Read the {yr} "
                            f"cash-flow statement."))
    return (y, tag, f, (f"ONE LINE MADE THE CASH: {short} moved {f:.0%} of {yr} OCF. Operating cash is "
                        f"not owner earnings when one balance-sheet line produced it (DELL, INOD). Read "
                        f"the {yr} cash-flow statement and liquidity note."))


def oe_annual(facts, end="capex"):
    """Owner earnings PER YEAR at one end of (c) - the series the flags should be reading.

    THE WRONG-SERIES DEFECT, found by the PLPC run of 2026-09-07 and it is general, not
    PLPC-specific. `level_shift()` and `best_year_dependence()` have always been fed RAW
    OPERATING CASH, which does not net capex - so they diagnose the shape of a number the
    framework does not value. On Preformed Line Products the two series give OPPOSITE
    answers: on OCF, level_shift returns 2.68 "STEP UP" and best_year_dependence 0.154; on
    owner earnings at the capex end, level_shift returns None "EARLY HALF STRADDLES ZERO"
    and best_year_dependence returns 0.586 "TWO YEARS JOINTLY CARRY THE WINDOW".

    The PINS guard added earlier the same day fires correctly here - it simply never got the
    chance, because it was handed the wrong series. That is the third instance this week of
    the same defect class: a diagnostic that is sound in itself and never reaches the thing
    it is meant to judge.

    Both series are now carried. OCF is kept rather than replaced because it is the less
    noisy of the two and a disagreement BETWEEN them is itself a prompt to read.

    Sign convention matches owner_earnings() exactly: ocf - sbc - abs(c)."""
    ocf, _disc = ocf_continuing(facts)
    if not ocf:
        return {}
    sbc = sbc_annual(facts)
    capx, _lease = capital_acquired(facts)
    src = capx if end == "capex" else da_annual(facts)
    return {e: ocf[e] - sbc.get(e, 0.0) - abs(src[e])
            for e in sorted(ocf) if src.get(e) is not None}


def main():
    src = os.path.join(HERE, f"{TODAY} PREPPED LIST.csv")
    if not os.path.exists(src):
        src = os.path.join(HERE, "2026-08-31 PREPPED LIST.csv")
    rows = [r for r in csv.DictReader(open(src, encoding="utf-8")) if r["status"] == "READ"]
    tick = M.cached_json("company_tickers.json", "https://www.sec.gov/files/company_tickers.json")
    sec = {str(v["ticker"]).upper(): int(v["cik_str"]) for v in tick.values()}
    sov, sov_src = live_sovereign()
    if sov is None:
        raise SystemExit("no sovereign available from any rung; the screen refuses to "
                         "invent one [operator rule 5]")
    print(f"FLOOR SCREEN â€” COMPUTATION, NOT A CLEARANCE   {TODAY}")
    print(f"sovereign {sov:.2%} ({sov_src}) Â· floor {FLOOR:.0%} [E4-28] Â· "
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
        ratio = share_count_shift(facts, t)
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
        # THE FOURTH SPREAD DEFECT, AND THE ONLY ONE THAT REPRODUCES EXACTLY WHILE STILL
        # MISLEADING. Found by the AAPL run of 2026-09-06. TSCO, EFX and ANF all reported
        # spreads that did not reproduce; Apple's DID - 2% to the million - and was wrong
        # anyway, because owner_earnings() computes only FOUR constructions (3y and 5y at
        # each capex end). On a business whose owner earnings grew 2.5x in nine years, a
        # 3y-vs-5y comparison measures the last two years and calls the answer "narrow":
        # against the AAPL run's own six windows the true width is 67.9%, not 2%.
        #
        # [E4-25] says the range width IS the finding, so a width computed over a window
        # too short to contain the variation is not a small finding - it is a FALSE one,
        # and it points the flattering way (narrow reads as well-determined). This is the
        # same lesson as best_year_dependence's leave-two-out fix: check WHY a range is
        # narrow before treating narrowness as knowledge.
        n_windows = len(vals)
        span_note = ""
        if n_windows <= 4:
            span_note = (f"spread spans only {n_windows} constructions (3y/5y x two capex "
                         f"ends) - it CANNOT see variation older than the 5-year window. "
                         f"On a fast-growing or fast-declining filer this understates the "
                         f"true width [E4-25]; the run must rebuild it over its own "
                         f"windows before treating a narrow reading as knowledge.")
        spread = (top - bottom) / bottom if bottom > 0 else None
        y_bottom = bottom / cap
        y_top = top / cap
        req = FLOOR - y_bottom            # perpetual growth needed on the bottom boundary
        out.append(dict(ticker=t, name=r["name"][:30], cap_m=r["cap_m"],
                        oe_bottom_m=round(bottom/1e6), oe_top_m=round(top/1e6),
                        spread=round(spread, 3) if spread is not None else "",
                        spread_caveat=span_note,
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


# MOVED ABOVE main() ON 2026-09-02, found by the UAL run. These two live BELOW
# `if __name__ == "__main__"` in the file that owns them, so they were importable
# but dead inside the screen itself - main() never called either. A guard that
# cannot fire in its own tool is not a guard.

def level_shift(vals, tail=3):
    """Step-change detector, to sit BESIDE the mean test rather than replace it.

    THE BLIND SPOT, diagnosed by the NKE run of 2026-09-02 and generalisable. A
    recent-3-mean-versus-earlier-mean test catches a spike INSIDE a window and is
    STRUCTURALLY BLIND TO A STEP CHANGE AT ITS BOUNDARY. Nike's ten constructions across
    five multi-year windows clustered inside 3,150-3,685M, a 17% width, and the mean test
    duly reported "steady". But the clustering was MECHANICAL: every window from three
    years up contained FY2024, the best of the nine, and the first window that excludes it
    drops 43%. Revenue, gross margin, EBIT, net income and EPS all broke in the same year
    and stayed broken. That is a LEVEL, not a dispersion, and no test of dispersion can see
    it.

    THE SIGN DEFECT, FOUND BY THE AATC RUN OF 2026-09-02. The first version guarded
    `earlier == 0` and NOT `earlier < 0`, so the ratio inverted whenever the early years
    were loss-making. Measured on constructed series: a genuine recovery from a -300 mean
    to a +300 mean returned -1.00 and the verdict "STEP DOWN", the exact opposite of the
    truth; and a business still losing money but improving (-300 mean to -250 mean)
    returned 0.83 and "no step". A RATIO IS NOT DEFINED ACROSS ZERO, and no threshold on it
    can be. This matters precisely where it was least noticed: TIER 3 OF THE WATCHLIST
    QUEUE IS DEFINED BY A NEGATIVE BOTTOM BOUNDARY - fifteen names - which is exactly the
    population that inverts.

    The fix refuses the ratio rather than repairing it, and describes the direction in
    words instead. That is operator rule 8: the flag is a prompt to read, never a score.

    THE HALF-FIX, FOUND BY THE DAL RUN OF 2026-09-07, AND IT IS MY DEFECT NOT THE SCREEN'S.
    The UAL run prescribed a TWO-PART fix - guard the negative early mean AND the NEAR-ZERO
    one - and only `earlier <= 0` was implemented. Delta's nine-year operating-cash series
    has an early mean of +$1.167M, which is positive, so the guard above waves it through and
    the function returns **2,040.0** with the confident string "STEP UP - normalize down".
    A ratio is not defined across zero and it is not INFORMATIVE anywhere near zero either:
    dividing by a number that is a rounding error on the series' own scale manufactures a
    figure with four significant digits out of noise.

    A PARTIAL FIX IS WORSE THAN NO FIX, because it now looks guarded. Recorded in those terms
    rather than quietly completed.

    Returns (ratio, verdict) where ratio is the mean of the last `tail` years over the mean
    of everything before them. A tight spread with a low ratio here is the dangerous case:
    it looks well-determined and is measuring a business that has already stepped down.
    Where the early mean is at or below zero, or is negligible against the series' own
    scale, returns (None, <a worded direction>).
    """
    if len(vals) < tail + 2:
        return None
    recent = sum(vals[-tail:]) / tail
    earlier = sum(vals[:-tail]) / (len(vals) - tail)
    # THE AGGREGATE/COMPONENT DEFECT, found by the PINS run of 2026-09-07 - the SAME DAY the
    # near-zero guard below was added, and it is the same error one level down. That guard
    # tests the MEAN of the early half, and a mean is exactly the statistic a sign change
    # inside that half destroys. Pinterest's early six are -102.9, -60.4, +0.7, +28.8,
    # +752.9, +469.2: three at or below zero and a fourth a rounding error, yet the single
    # year 2021 drags the mean to +$181.4M, so both `earlier <= 0` and the near-zero test are
    # FALSE and the row is waved through at 5.26x with a confident verdict string.
    #
    # THE UNDEFINED-ACROSS-ZERO CONDITION THE DOCSTRING EXISTS TO CATCH WAS PRESENT IN THE
    # DATA AND ABSENT FROM THE TEST. The generalisable lesson, and the third iteration of
    # this one function's guard: A GUARD THAT READS THE AGGREGATE CANNOT SEE A DEFECT THAT
    # LIVES IN THE COMPONENTS. The test below is the one the PINS run prescribed.
    #
    # IT FIRES ON 99 OF THE 361 PRICED QUEUE NAMES (27.4%), AND IT IS DELIBERATELY NOT
    # THRESHOLDED DOWN. I first assumed that rate meant over-firing and went looking for a
    # magnitude threshold to shrink it, using ADM as the supposed false positive. ADM turned
    # out to be a GENUINE straddle - early years of +2,211, -4,784, -5,452, -2,386, +6,595,
    # +3,478, with 50.7% of the early half's magnitude below zero - so a ratio against its
    # mean is exactly as meaningless as Pinterest's. The high rate is a fact about the queue
    # (it holds many cyclical and formerly loss-making names), not evidence of a bad test.
    # Thresholds measured before deciding: 27.4% at 0%, 21.3% at 5%, 19.7% at 10%, 14.7% at
    # 20% of early-half magnitude below zero. Adopting one would have been tuning to shrink a
    # count rather than to be correct - the trap named in da_discontinuity_flag's docstring.
    #
    # The asymmetry settles it: this is a REFUSAL, not an accusation. A false positive costs
    # one read, which operator rule 8 wants anyway; a false negative is a confident 5.26x
    # that means nothing.
    early = vals[:-tail]
    if min(early) < 0 < max(early):
        return (None, f"EARLY HALF STRADDLES ZERO - the pre-window years run from "
                      f"${min(early)/1e6:,.1f}M to ${max(early)/1e6:,.1f}M, crossing zero, so "
                      f"their mean (${earlier/1e6:,.1f}M) describes no year that happened and "
                      f"a ratio against it is undefined in substance even where it computes "
                      f"(it gives {recent/earlier:,.2f}x). The level HAS changed and the "
                      f"multi-year mean is averaging TWO DIFFERENT BUSINESSES. READ THE "
                      f"FILING [E4-25].")
    # The scale of the series itself, not of either half - so a near-zero EARLY mean is
    # judged against what this company's numbers normally look like.
    scale = sum(abs(v) for v in vals) / len(vals)
    if 0 < earlier < 0.05 * scale:
        return (None, f"EARLY MEAN NEGLIGIBLE - the pre-window mean is ${earlier/1e6:,.1f}M "
                      f"against a series averaging ${scale/1e6:,.0f}M, so the ratio would be "
                      f"arithmetic on a rounding error (it computes to {recent/earlier:,.0f}x "
                      f"and means nothing). The level HAS changed; the multi-year mean is "
                      f"averaging two different businesses. READ THE FILING [E4-25].")
    # THE MIRROR CASE, found on ARM's row 2026-09-11: the guards below test the EARLY half
    # for a sign change and never the RECENT one. Arm's early years earn and its recent
    # owner-earnings years do not, so recent/earlier printed -0.79 with the confident string
    # "STEP DOWN" - a negative ratio, which is not a ratio. Refused in words like its twin.
    if recent <= 0 < earlier:
        return (None, f"SIGN CHANGE, RECENT - the early years earn (mean ${earlier/1e6:,.0f}M) "
                      f"and the recent ones do not (mean ${recent/1e6:,.0f}M); a ratio is "
                      f"undefined across zero. The level HAS changed, downward. READ THE "
                      f"FILING [E4-25].")
    if earlier <= 0:
        if recent > 0:
            return (None, "SIGN CHANGE - the early years are loss-making and the recent "
                          "ones are not; a ratio is undefined across zero. The level HAS "
                          "changed and the multi-year mean is averaging two different "
                          "businesses. READ THE FILING [E4-25].")
        return (None, "STILL NEGATIVE - both halves of the window are at or below zero; "
                      "no ratio is meaningful and the bottom boundary is a statement "
                      "about the CONSERVATIVE construction, not a verdict.")
    r = recent / earlier
    if r < 0.70:
        v = "STEP DOWN - the series has changed level; a tight spread here is not safety"
    elif r > 1.60:
        v = "STEP UP - normalize down [E4-41]"
    else:
        v = "no step"
    return (r, v)

def best_year_dependence(vals):
    """How much of a window's mean rests on its single best year. Returns (drop, verdict).

    THE ACTUAL NIKE DIAGNOSIS, and level_shift() above does NOT catch it - Nike reads 0.88,
    "no step". Recorded honestly rather than claiming the first fix worked.

    The NKE run of 2026-09-02 found ten constructions across five multi-year windows
    clustering inside 3,150-3,685M, a 17% width, which the mean test and the level test both
    read as steady. The clustering was MECHANICAL: every window from three years up contained
    FY2024, the best of the nine years, and the first window that EXCLUDED it dropped 43%.
    Revenue, gross margin, EBIT, net income and EPS all broke in the same year and stayed
    broken.

    So the dangerous shape is not dispersion and not a tail step. It is a TIGHT SPREAD THAT IS
    TIGHT ONLY BECAUSE EVERY WINDOW SHARES ONE DOMINANT OBSERVATION. A leave-one-out on the
    maximum is the test that sees it, and it is cheap.

    [E4-25] says the range width IS the finding. This says: check WHY the range is narrow
    before treating narrowness as knowledge.
    """
    if len(vals) < 4:
        return None
    mean_all = sum(vals) / len(vals)
    if mean_all <= 0:
        return None
    # A POSITIVE MEAN CAN STILL BE NEAR ZERO (NEGG run, 2026-09-13) - the fifth instance of the
    # ratio-near-zero class and the gap level_shift had. Newegg's nine-year operating-cash mean is
    # +$0.11M, which passes `mean_all <= 0`, so the drop was computed against almost nothing and
    # printed 9,918%. Judged against the series' own typical magnitude, as level_shift does.
    scale = sum(abs(v) for v in vals) / len(vals)
    if scale and mean_all < 0.05 * scale:
        return (None, f"MEAN NEAR ZERO - the window's mean is ${mean_all/1e6:,.2f}M against a typical "
                      f"magnitude of ${scale/1e6:,.1f}M, so a best-year drop is arithmetic on almost "
                      f"nothing. The years are offsetting, not stable - READ THEM [E4-25].")
    # LEAVE-TWO-OUT ADDED 2026-09-02, found by the ANF run. Leave-ONE-out read ANF at
    # 0.119, "no single-year dependence" - on a series whose window is carried by FY2023
    # AND FY2024 JOINTLY. A two-year boom is the exact ETD/FLO/ASIX shape this test exists
    # to catch, and a leave-one-out is structurally blind to it: drop either boom year
    # alone and the other still holds the mean up.
    #
    # THE PAIR TEST AND ITS CONFESSED LIMITS. The k=2 flag fires only when BOTH hold:
    #   (a) dropping the best two years moves the mean by more than 25%, AND
    #   (b) that move is at least 1.8x the single-year move - i.e. the second year adds
    #       disproportionately, which is the signature of a JOINT pair rather than of a
    #       growth series whose top two years are simply its most recent.
    # Measured on the known shapes before adoption: the ANF pair (d2 0.333, ratio 2.3x)
    # fires; a genuine compounder (+15%/yr, d2 0.149) does not; the NKE one-year shape
    # stays a k=1 finding (ratio 1.0); ULTA stays clean (d2 0.097). CONVENTION: the 0.25
    # and 1.8 are not corpus numbers - they are prompt-to-read thresholds calibrated on
    # this project's own solved cases, and under operator rule 8 the flag is a prompt to
    # read, never a score. A first version used a 2/n "excess" baseline; it was WRONG
    # (dropping two average years moves a mean by zero, not 2/n) and is recorded here
    # rather than silently replaced.
    def drop_k(k):
        rest = sorted(vals)[:-k]
        return 1.0 - ((sum(rest) / len(rest)) / mean_all)
    d1 = drop_k(1)
    d2 = drop_k(2) if len(vals) >= 6 else None
    pair = (d2 is not None and d2 > 0.25 and d1 > 0 and d2 >= 1.8 * d1)
    if pair:
        return (d2, "TWO YEARS JOINTLY CARRY THE WINDOW - the exact two-year-boom shape "
                    "leave-one-out cannot see; re-price on a window that excludes both")
    if d1 > 0.20:
        v = ("ONE YEAR CARRIES THE WINDOW - a tight spread here is arithmetic, not "
             "knowledge; re-price on a window that excludes it")
    elif d1 > 0.12:
        v = "one year is doing heavy lifting - check it"
    else:
        v = "no single-year dependence"
    return (d1, v)

if __name__ == "__main__":
    main()
