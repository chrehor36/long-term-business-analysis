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
# STOCK PAY FALLBACKS, added 2026-10-05 after the EME and SXI runs: both filers tag the cash-flow
# add-back with a company tag and the standard expense only on the equity statement, as the APIC
# adjustment (EME $20,595K 2025, SXI $8,821K FY2026, each equal to the filed cash-flow line). The
# tool printed 0 for both. Used ONLY for a year in which neither SBC tag resolves, and the tag is
# printed. The last three are the IFRS names. A year that none of them resolves prints "n/f", never 0.
SBC_FALLBACK = ["AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue",
                "AdjustmentsForSharebasedPayments",
                "ExpenseFromSharebasedPaymentTransactionsWithEmployees",
                "ExpenseFromSharebasedPaymentTransactions"]
DA  = ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
       "DepreciationAndAmortization", "Depreciation"]
# PaymentsToAcquireOtherPropertyPlantAndEquipment added LAST on 2026-10-05: MTRN tags its FY2025
# capital spending ($53,279K, the filed line) only under it, so the window stopped at FY2024 although
# FY2025 was filed. Last in the list, so it can never displace a primary tag for a year both cover.
CAP = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
       "PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets",
       "PaymentsToAcquireOtherPropertyPlantAndEquipment"]
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


# EVERY FILED SHARE COUNT, WITH ITS DATE. Added 2026-10-05 after the SONY and IESC runs. cover_count()
# stopped at the first tag that had ANY observation, so a stale dei count (SONY, last tagged 2019) hid
# a newer IFRS count, and then refused the stale one, so the script fell to a pre-split weighted
# average. And a current cover count still predates a split made after the cover date (IESC: cover
# 2026-07-27, 2-for-1 distributed 2026-08-21), so a post-split quote was multiplied by a pre-split
# count and the cap came out half the truth. Now every candidate is listed with its date, the newest
# fresh one is used, and the split factor after its date is applied in the open: both counts print.
SHARE_CANDIDATES = [("EntityCommonStockSharesOutstanding", "dei", "dei cover-page count"),
                    ("CommonStockSharesOutstanding", "us-gaap", "balance-sheet count"),
                    ("NumberOfSharesOutstanding", "ifrs-full", "IFRS shares-outstanding count")]
SHARE_ISSUED = ("CommonStockSharesIssued", "us-gaap", "balance-sheet ISSUED count (includes treasury)")


def share_counts(facts):
    """[(date, millions, label, tag, n_values_at_that_date)], the latest observation of each tag."""
    out = []
    for tag, space, label in SHARE_CANDIDATES + [SHARE_ISSUED]:
        obs = []
        for x in (facts.get("facts", {}).get(space, {}).get(tag, {})
                  .get("units", {}).get("shares", [])):
            e, v = x.get("end"), x.get("val")
            if e and v and float(v) > 0:
                obs.append((date.fromisoformat(e), float(v)))
        if obs:
            d = max(o[0] for o in obs)
            at_d = {o[1] for o in obs if o[0] == d}
            out.append((d, max(at_d) / 1e6, label, tag, len(at_d)))
    return out


# ---------------------------------------------------------------- the filing's own statement lines
# WHY THE FILING AND NOT COMPANYFACTS, added 2026-10-05. The SEC companyfacts file carries standard
# taxonomy tags only. Three of the day's defects sit in filer-specific (extension) tags that it never
# sees: MBUU's "Non-cash compensation to directors" (mbuu:ShareBasedCompensationDirectors), MTRN's
# "Payments for mine development" (mtrn:PaymentsForMineDevelopment), and GENC's securities line inside
# operating cash flow. And which section a line sits in (operating or investing) is not in companyfacts
# at all. The filing's calculation linkbase says both: which lines sum to operating cash flow, which to
# investing, which to liabilities. Read from the last three annual reports, so five fiscal years of
# cash flows and four balance-sheet dates are covered. Transcription only: each value is the filed
# value of the filed line, printed with its tag; nothing is chosen.
_LB = "{http://www.xbrl.org/2003/linkbase}"
_XL = "{http://www.w3.org/1999/xlink}"
_XI = "{http://www.xbrl.org/2003/instance}"
ANNUAL_FORMS = ("10-K", "20-F", "40-F")
OCF_ROOTS = ("NetCashProvidedByUsedInOperatingActivities",
             "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
             "CashFlowsFromUsedInOperatingActivities")
INV_ROOTS = ("NetCashProvidedByUsedInInvestingActivities",
             "NetCashProvidedByUsedInInvestingActivitiesContinuingOperations",
             "CashFlowsFromUsedInInvestingActivities")
LIAB_ROOTS = ("LiabilitiesAndStockholdersEquity", "Liabilities", "LiabilitiesCurrent",
              "LiabilitiesNoncurrent", "EquityAndLiabilities", "CurrentLiabilities",
              "NoncurrentLiabilities")
import re as _re
# Securities bought or sold INSIDE operating cash flow (trading classification). Gains, income and
# impairments are non-cash reversals, not purchases or sales, and are left out.
RX_SEC = (_re.compile(r"Securit|Trading|Investments?(Held|Portfolio)?$|InvestmentPortfolio"),
          _re.compile(r"IncreaseDecrease|Payment|Purchase|Proceeds|Sale|Acquire|Transfer"),
          _re.compile(r"Gain|Loss|Income|Impairment|Dividend|Interest|Amortiz|Accretion|Unrealized|"
                      r"Realized|EquityMethod|Distribut|Tax"))
RX_SBC = (_re.compile(r"ShareBased|Sharebased|StockBased|Stockbased|StockCompensation|"
                      r"StockOption|RestrictedStock|EquityCompensation|NonCashCompensation|"
                      r"NoncashCompensation|StockIssuedForCompensation|EquityAward|SharebasedPayment"),
          _re.compile(r"Tax|Withholding|Excess|PaymentsFor|PaymentsRelated|Proceeds|Settle"))
RX_CAPX = (_re.compile(r"Mine|Mining|Mineral|Intangible|Software|ProductiveAssets|Development|"
                       r"Patent|Licens|Exploration|Capitalized|Rental|OnLease|LeasedEquipment|LeaseFleet|Fleet|Aircraft|FlightEquipment|Subscriber|DealerGenerated|CustomerAccount"),
           _re.compile(r"Business|Subsidiar|Securit|Proceeds|Sale|Disposal|Loan|Deposit|"
                       r"EquityMethod|Affiliate|Marketable|PropertyPlant|Grant"))
RX_DEBT = (_re.compile(r"Debt|Borrowing|CommercialPaper|LineOfCredit|LinesOfCredit|NotesPayable|"
                       r"LoansPayable|ConvertibleNotes|SeniorNotes|Bonds"),
           _re.compile(r"Interest|IssuanceCost|Discount|Securities|Receivable|Guarantee|Derivative"))


def annual_accessions(facts, n=3):
    """The n newest annual-report accessions in the facts, newest first."""
    seen = {}
    for tax in ("us-gaap", "ifrs-full"):
        for tag in OCF_ROOTS:
            for pts in facts.get("facts", {}).get(tax, {}).get(tag, {}).get("units", {}).values():
                for x in pts:
                    if x.get("form") in ANNUAL_FORMS and x.get("accn"):
                        seen[x["accn"]] = max(seen.get(x["accn"], ""), x.get("filed", ""))
    return [a for a, _ in sorted(seen.items(), key=lambda kv: kv[1], reverse=True)[:n]]


def _filing_files(cik, accn):
    import json as _j
    base = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn.replace('-', '')}/"
    idx = _j.loads(S._get(base + "index.json", cache_name=f"edgar_idx_{accn}.json",
                          max_age_h=24 * 365))
    names = [i["name"] for i in idx["directory"]["item"]]
    # Some filers (Donnelley-built, e.g. GENC 2024-25) embed the linkbases in the .xsd schema and
    # file no _cal.xml; the calculation links are read from the schema then.
    cal = next((x for x in names if x.endswith("_cal.xml")), None) or next(
        (x for x in names if x.endswith(".xsd")), None)
    inst = next((x for x in names if x.endswith("_htm.xml")), None) or next(
        (x for x in names if x.endswith(".xml")
         and not _re.search(r"_(cal|def|lab|pre)\.xml$|FilingSummary", x)), None)
    return base, cal, inst


def _calc_trees(txt):
    import xml.etree.ElementTree as ET
    trees = {}
    for link in ET.fromstring(txt.encode("utf-8")).iter(_LB + "calculationLink"):
        loc = {l.get(_XL + "label"): l.get(_XL + "href").split("#")[-1]
               for l in link.iter(_LB + "loc")}
        ch = trees.setdefault(link.get(_XL + "role"), {})
        for a in link.iter(_LB + "calculationArc"):
            ch.setdefault(loc[a.get(_XL + "from")], []).append(
                (loc[a.get(_XL + "to")], float(a.get("weight", "1"))))
    return trees


def _instance_values(txt):
    """{(local_name, (start|None, end)): value} for facts with no dimensions."""
    import xml.etree.ElementTree as ET
    root = ET.fromstring(txt.encode("utf-8"))
    ctx = {}
    for c in root.iter(_XI + "context"):
        if c.find(".//" + _XI + "segment") is not None or c.find(".//" + _XI + "scenario") is not None:
            continue
        p = c.find(_XI + "period")
        s, e, i = (p.find(_XI + k) for k in ("startDate", "endDate", "instant"))
        ctx[c.get("id")] = (s.text.strip(), e.text.strip()) if s is not None else (None, i.text.strip())
    vals = {}
    for el in root:
        cr = el.get("contextRef")
        if not cr or cr not in ctx or el.text is None or "}" not in el.tag:
            continue
        try:
            vals[(el.tag.split("}")[1], ctx[cr])] = float(el.text.strip())
        except ValueError:
            pass
    return vals


def _local(concept):
    return concept.split("_", 1)[1] if "_" in concept else concept


def _walk(ch, node, rx_in, rx_out, w=1.0, seen=None):
    """Descendants of node matching rx_in and not rx_out, with their compounded weight. A matching
    node is not descended into, so a subtotal and its parts are never both returned."""
    seen = seen if seen is not None else set()
    for kid, kw in ch.get(node, []):
        if kid in seen:
            continue
        seen.add(kid)
        loc = _local(kid)
        if all(r.search(loc) for r in rx_in) and not (rx_out and rx_out.search(loc)):
            yield kid, w * kw
        else:
            yield from _walk(ch, kid, rx_in, rx_out, w * kw, seen)


def _best_role(trees, roots):
    """The role in which one of roots has the most descendants (the face statement, not a note)."""
    def size(ch, n, seen):
        for k, _ in ch.get(n, []):
            if k not in seen:
                seen.add(k); size(ch, k, seen)
        return len(seen)
    best = None
    for role, ch in trees.items():
        for r in roots:
            for parent in ch:
                if _local(parent) == r:
                    s = size(ch, parent, set())
                    if not best or s > best[0]:
                        best = (s, role, parent)
    return best


def filing_lines(cik, facts, n=3):
    """Lines read from the last n annual reports' calculation linkbases. Returns
    {'read': [accn], 'failed': [(accn, why)],
     'sec': {fy_end: {concept: effect_on_ocf_mn}},     securities lines inside operating cash flow
     'sbc': {fy_end: {concept: add_back_mn}},          stock-pay lines inside operating cash flow
     'capx': {fy_end: {concept: payment_mn}},          intangible / mine / software payments in investing
     'debt': {instant: {concept: value_mn}}, 'debt_concepts': [concept]}   debt on the face
    Newest filing wins a period that two filings cover (a live read takes the restated figure)."""
    out = {"read": [], "failed": [], "sec": {}, "sbc": {}, "capx": {}, "debt": {},
           "debt_concepts": []}
    claimed_cf, claimed_bs = set(), set()
    for accn in annual_accessions(facts, n):
        try:
            base, cal, inst = _filing_files(cik, accn)
            if not cal or not inst:
                out["failed"].append((accn, "no calculation linkbase or instance in the filing"))
                continue
            trees = _calc_trees(S._get(base + cal, cache_name=f"edgar_cal_{accn}.xml",
                                       max_age_h=24 * 365))
            vals = _instance_values(S._get(base + inst, cache_name=f"edgar_inst_{accn}.xml",
                                           max_age_h=24 * 365))
        except Exception as e:
            out["failed"].append((accn, f"{type(e).__name__}: {e}"[:120]))
            continue
        out["read"].append(accn)

        # ONE FILING PER PERIOD. A year is taken whole from the newest filing whose statement covers
        # it, never assembled from two: GENC's FY2025 10-K recast FY2023's three securities lines
        # into one, and merging by element across filings counted FY2023 twice.
        def covered(roots, instant):
            return {e for (loc, (s, e)) in vals if loc in roots and (s is None) == instant
                    and (instant or 340 <= (date.fromisoformat(e) - date.fromisoformat(s)).days <= 380)}
        cf_years = covered(OCF_ROOTS, False) - claimed_cf
        bs_dates = covered(LIAB_ROOTS, True) - claimed_bs
        claimed_cf.update(cf_years)
        claimed_bs.update(bs_dates)

        def flows(concepts, key, sign):
            for c, w in concepts:
                for (loc, (s, e)), v in vals.items():
                    if loc != _local(c) or not s or e not in cf_years:
                        continue
                    if not 340 <= (date.fromisoformat(e) - date.fromisoformat(s)).days <= 380:
                        continue
                    out[key].setdefault(e, {})[c] = (w * v if sign else abs(v)) / 1e6

        ocf = _best_role(trees, OCF_ROOTS)
        if ocf:
            ch = trees[ocf[1]]
            flows(list(_walk(ch, ocf[2], RX_SEC[:2], RX_SEC[2])), "sec", True)
            flows(list(_walk(ch, ocf[2], RX_SBC[:1], RX_SBC[1])), "sbc", True)
        inv = _best_role(trees, INV_ROOTS)
        if inv:
            ch = trees[inv[1]]
            flows([(c, w) for c, w in _walk(ch, inv[2], RX_CAPX[:1], RX_CAPX[1]) if w < 0],
                  "capx", False)
        bs = _best_role(trees, LIAB_ROOTS)
        if bs:
            ch = trees[bs[1]]
            found = []
            for parent in ch:
                if _local(parent) in LIAB_ROOTS:
                    found += [c for c, _ in _walk(ch, parent, RX_DEBT[:1], RX_DEBT[1])]
            for c in dict.fromkeys(found):
                if c not in out["debt_concepts"]:
                    out["debt_concepts"].append(c)
                for (loc, (s, e)), v in vals.items():
                    if loc == _local(c) and s is None and e in bs_dates:
                        out["debt"].setdefault(e, {})[c] = v / 1e6
    return out

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
    sbc, sbc_tag = {}, {}
    for _tag in SBC:
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            if _e not in sbc or abs(_v) > abs(sbc[_e]):
                sbc[_e], sbc_tag[_e] = _v, _tag
    for _tag in SBC_FALLBACK:          # only where neither SBC tag resolves; see SBC_FALLBACK
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            if _e not in sbc:
                sbc[_e], sbc_tag[_e] = _v, _tag
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
    _part_tags = {}
    for _tag in DA_COMPONENT:
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            _parts[_e] = _parts.get(_e, 0.0) + abs(_v)
            _part_tags.setdefault(_e, set()).add(_tag)
    # AMORTIZATION ONLY, 2026-10-06 (the PTEN run): a filer that tags its depreciation under its own
    # element leaves only AmortizationOfIntangibleAssets in companyfacts, and the D&A column then shows
    # $126M against a filed charge near $1B. Such years are flagged, never silently used.
    da_amort_only = {e for e in _parts if e not in da and _part_tags.get(e) == {"AmortizationOfIntangibleAssets"}}
    for _e, _v in _parts.items():
        if _e not in da or _v > abs(da[_e]):
            da[_e] = _v
    # Per-year tag, so the printout can say which element each year's capex came from. Same
    # precedence as _annual(facts, CAP): the first tag in the list that has the year wins.
    cap, cap_tag = {}, {}
    for _tag in CAP:
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            if _e not in cap:
                cap[_e], cap_tag[_e] = _v, _tag
    soft, soft_tag = {}, {}
    for _tag in SOFTWARE_CAP:
        _series, _, _ = _annual(facts, [_tag])
        for _e, _v in _series.items():
            if _e not in soft:
                soft[_e], soft_tag[_e] = _v, _tag
    if soft:
        cap = {e: abs(v) + abs(soft.get(e, 0.0)) for e, v in cap.items()}
    ni,  _, _ = _annual(facts, NI)
    ys = sorted(set(ocf) & set(da) & set(cap))
    if not ys:
        return None
    sel = ys[-years:]
    rows = []
    for y in sel:
        # A year with no stock-pay tag deducts nothing, and says so (sbc_tag None prints "n/f").
        cash = ocf[y] - sbc.get(y, 0.0)
        # LABELLED BY DEFINITION, NOT BY POSITION (2026-10-05, the MBUU and HUBB runs). The columns
        # were "OE lo" and "OE hi", and which basis is lower changes from year to year: where D&A
        # exceeds capex (acquired-intangible amortization, HUBB 2023-25) "lo" was the D&A basis.
        # oe_lo / oe_hi stay (tools/screen.py ranks on them); the printout shows the two bases.
        oe_capex = cash - cap[y]            # OCF - SBC - all capital spending
        oe_da = cash - da[y]                # OCF - SBC - depreciation and amortization
        rows.append(dict(fy=y, ocf=ocf[y], sbc=sbc.get(y, 0.0), sbc_tag=sbc_tag.get(y),
                         da=da[y], capex=cap[y], cap_tag=cap_tag.get(y), soft_tag=soft_tag.get(y),
                         ni=ni.get(y), oe_capex=oe_capex, oe_da=oe_da,
                         oe_lo=min(oe_capex, oe_da), oe_hi=max(oe_capex, oe_da)))
    return dict(unit=unit, ocf_tag=ocf_tag, rows=rows, all_years=ys,
                da_amort_only=sorted(e for e in da_amort_only if e in sel),
                ocf_last=max(ocf) if ocf else None,
                mean_lo=statistics.fmean(r["oe_lo"] for r in rows),
                mean_hi=statistics.fmean(r["oe_hi"] for r in rows),
                mean_capex=statistics.fmean(r["oe_capex"] for r in rows),
                mean_da=statistics.fmean(r["oe_da"] for r in rows))


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
    # Fallbacks added 2026-10-05 (V): Visa tags total equity only as the NCI-inclusive element after
    # 2011, and the first-tag-wins read stopped at StockholdersEquity's 2011 values. The last two are IFRS.
    ("equity",      ["StockholdersEquity",
                     "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
                     "EquityAttributableToOwnersOfParent", "Equity"]),
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


def _pool(facts):
    ns = facts.get("facts", {})
    pool = dict(ns.get("us-gaap", {}))
    for k, v in ns.get("ifrs-full", {}).items():
        pool.setdefault(k, v)
    return pool


def _instants(pool, tag, currency):
    """{year_end: (value, accession, filed)} for one tag, annual forms, first-filed vintage."""
    got = {}
    for x in pool.get(tag, {}).get("units", {}).get(currency, []):
        if x.get("form") not in BS_FORMS or x.get("start") or not x.get("end"):
            continue
        if x.get("fp") not in (None, "FY"):
            continue
        e, f = x["end"], x.get("filed", "9999")
        if e not in got or f < got[e][2]:
            got[e] = (float(x["val"]), x.get("accn", "?"), f)
    return got


def balance_history(facts, currency="USD", n=10):
    """{year_end: {row: (value, accession, tag)}} for the last n fiscal year-ends, first-filed vintage.

    PER-YEAR UNION ACROSS THE TAG LIST (2026-10-05, the V run). This read the first tag that had ANY
    data and stopped, so a filer that moved between elements lost every year after the move (Visa's
    equity ends in 2011 under StockholdersEquity; IESC's cash is blank 2019-2022). Now each year takes
    the first tag in the list that has it, as sources.annual() does for flows, and the tag is kept so
    the printout can say when a column changes element."""
    pool = _pool(facts)
    out = {}
    for row, tags in BS_ROWS:
        for tag in tags:
            for e, (v, accn, _) in _instants(pool, tag, currency).items():
                if row not in out.setdefault(e, {}):
                    out[e][row] = (v, accn, tag)
    ends = sorted(out)[-n:]
    return {e: out[e] for e in ends}


# Fallback debt columns, used only when no calculation linkbase could be read. They can overlap
# (DebtCurrent includes the next two), so no sum is printed for them.
DEBT_FALLBACK = ["LongTermDebtCurrent", "ShortTermBorrowings", "CommercialPaper",
                 "LinesOfCreditCurrent", "OtherShortTermBorrowings", "DebtCurrent"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--currency", default=None, help="currency the business EARNS in; default: the XBRL unit "
                    "of its cash-flow series (2026-10-05: the default was USD, so SONY got the Treasury)")
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
        print("  USE Framework/SECTOR METHOD v5 - insurers and float companies.md,")
        print("  which values two components separately.")
        print("  (Pass --shares to override if you have already made the corrections.)")
        return 1

    # THE SOVEREIGN OF THE EARNINGS CURRENCY, 2026-10-05 (the SONY run). --currency defaulted to USD
    # and was never compared with the unit the earnings are filed in, so Sony, which files in yen,
    # was set against the US Treasury. Operator rule 5 asks for the sovereign "for the earnings
    # currency". The XBRL unit of the owner-earnings series IS the earnings currency; --currency, if
    # typed, overrides it and the disagreement is printed. A currency with no issuing-authority source
    # in tools/sources.py gets no rate: the line says so and every rate-dependent line is refused.
    earn_ccy = (a.currency or oe["unit"] or "").upper()
    ccy_note = None
    if a.currency and oe["unit"] and a.currency.upper() != oe["unit"].upper():
        ccy_note = (f"  ** --currency {a.currency.upper()} was typed; the XBRL earnings unit is "
                    f"{oe['unit']}. The sovereign below is for {a.currency.upper()}, as typed. **")
    sov = sov_date = sov_src = None
    if earn_ccy not in S.SOVEREIGN_SOURCES:
        sov_src = (f"NO ISSUING-AUTHORITY SOURCE configured for {earn_ccy} in tools/sources.py "
                   f"(have {', '.join(sorted(S.SOVEREIGN_SOURCES))}); no rate printed")
    else:
        try:
            sov, sov_date, sov_src = S.sovereign(earn_ccy)
        except Exception as e:
            sov_src = f"FETCH FAILED for {earn_ccy} ({type(e).__name__}); no rate printed"

    # THE SHARE COUNT. COVER COUNT FIRST, WEIGHTED AVERAGE ONLY AS A LABELLED FALLBACK. Added
    # 2026-09-07 after the CRM run reported the consequence of leaving this at the weighted average:
    # 956M against the cover page's 823M, a market cap 16.2% TOO HIGH, so every yield this script
    # printed for Salesforce was too LOW. A weighted average is a denominator for EPS, not a count of
    # the shares that exist (UAL, WTM, 2026-09-02).
    #
    # 2026-10-05 (SONY, IESC): every filed count is printed with its date; the newest that is not
    # stale (550 days, the CRWD and QLYS finding) is used; and a split after that date, read from the
    # quote's own split history (tools/sources.py, aggregator, flagged), is applied IN THE OPEN: the
    # count as filed and the count on the quote's basis both print, and so do both caps.
    share_lines = []
    shares, sh_src, split_f = a.shares, "--shares, supplied by the operator", None
    if shares is None:
        today = date.today()
        cands = share_counts(facts)
        for d, v, label, tag, nv in cands:
            stale = (today - d).days > 550
            share_lines.append(f"    {label:<46} {v:>12,.3f}M  as of {d}  ({tag})"
                               f"{'  STALE, not used' if stale else ''}"
                               f"{f'  [{nv} values at that date: share classes? the largest is shown]' if nv > 1 else ''}")
        fresh = [c for c in cands if (today - c[0]).days <= 550 and c[3] != SHARE_ISSUED[0]]
        fresh = fresh or [c for c in cands if (today - c[0]).days <= 550]
        if fresh:
            d, v, label, tag, _ = max(fresh, key=lambda c: c[0])   # newest; ties keep list order
            shares, sh_src, sh_date = v, f"{label} as of {d} ({tag})", d
        else:
            # Nothing fresh. The NEWEST filed figure is used, whichever kind it is, and labelled
            # STALE: before 2026-10-05 a stale cover count was refused in favour of a weighted
            # average that could be older still (SONY: FY3/21, against an IFRS count of 2025).
            sh, sh_tag, _ = _annual(facts, SH)
            pool_ = [(c[0], c[1], f"{c[2]} as of {c[0]} ({c[3]})") for c in cands
                     if c[3] != SHARE_ISSUED[0]]
            if sh:
                pool_.append((date.fromisoformat(max(sh)), sh[max(sh)],
                              f"{sh_tag} for the year to {max(sh)} - a WEIGHTED AVERAGE, not a "
                              f"cover-page count"))
            if pool_:
                sh_date, shares, sh_src = max(pool_, key=lambda c: c[0])
                sh_src = f"STALE ({(today - sh_date).days} days old; the newest filed) {sh_src}"
        if shares:
            try:
                split_f = S.split_factor_after(a.quote or t, sh_date.isoformat())
            except Exception as e:
                share_lines.append(f"    split history: could not be read ({type(e).__name__}); "
                                   f"check for a split after {sh_date} by hand")
    if not shares:
        print(f"{t}: no share count in XBRL; pass --shares (millions) from the cover page.")
        print(f"  `python Screens/cover_shares.py {t}` reads it off the filed cover by class.")
        return 1
    shares_filed = shares
    if split_f and abs(split_f - 1.0) > 1e-9:
        shares = shares_filed * split_f

    cap = px * shares
    rate = ((sov or 0.0) + a.spread) / 100
    note = print if a.framework == "v4" else (lambda *x, **k: None)
    if a.spread:
        print(f"  ** DISCOUNT RATE CARRIES A +{a.spread:.2f} POINT SPREAD over the "
              f"sovereign. Both frameworks refuse a risk premium in the rate; certainty is "
              f"priced once, in the margin demanded at the end. State the reason or drop it. **")
    y_lo, y_hi = oe["mean_lo"] / cap * 100, oe["mean_hi"] / cap * 100
    y_capex, y_da = oe["mean_capex"] / cap * 100, oe["mean_da"] / cap * 100
    g_imp = implied_growth(cap, oe["mean_lo"], rate) if sov is not None else None
    pts_lo = points_over(cap, oe["mean_lo"], 0.03, sov) if sov is not None else None
    pts_hi = points_over(cap, oe["mean_hi"], 0.03, sov) if sov is not None else None

    big = max(abs(r["ocf"]) for r in oe["rows"]) >= 1000
    fm = ",.0f" if big else ",.1f"           # small filers print a decimal: $1.0M is not 1

    W = 78
    print("=" * W)
    print(f"{name}  ({t})   —  ARITHMETIC ONLY, NOT A VERDICT")
    print("=" * W)
    if sov is not None:
        print(f"  sovereign {earn_ccy}   {sov:.2f}%   {sov_date}   {sov_src}")
    else:
        print(f"  sovereign {earn_ccy}   {sov_src}")
    print(f"  earnings currency: {earn_ccy} "
          f"({'typed with --currency' if a.currency else 'the XBRL unit of the cash-flow series'})")
    if ccy_note:
        print(ccy_note)
    print(f"  price     {px:,.2f} {px_ccy}   {px_date}"
          f"{'  via ' + a.quote if a.quote else ''}   (aggregator — live quote only)")
    if px_ccy and oe and px_ccy.upper() != oe["unit"]:
        print(f"  ** CURRENCY MISMATCH: earnings in {oe['unit']}, quote in {px_ccy}."
              f" Refusing to convert. Pass --quote with the home listing. **")
        return 1
    if share_lines:
        print("  share counts filed (millions):")
        print("\n".join(share_lines))
    if split_f and abs(split_f - 1.0) > 1e-9:
        print(f"  ** SPLIT AFTER THE COUNT'S DATE: factor {split_f:g} (split history of "
              f"{a.quote or t}, aggregator, flagged). Count as filed {shares_filed:,.3f}M; on the "
              f"quote's basis {shares:,.3f}M.")
        print(f"     cap on the filed count {px * shares_filed / 1000:,.2f}B; on the quote's basis "
              f"{cap / 1000:,.2f}B {oe['unit']} (used below). Check the split in the 8-K. **")
    print(f"  shares    {shares:,.1f}M      market cap {cap/1000:,.2f}B {oe['unit']}")
    print(f"  share basis: {sh_src}")
    if "WEIGHTED AVERAGE" in sh_src:
        print("  ** A weighted average is an EPS denominator, not a share count.")
        print("     For a multi-class filer it is denominated in ONE class. Verify:")
        print(f"     python Screens/cover_shares.py {t} **")

    oe_lines = []
    P = oe_lines.append
    P(f"\n  OWNER EARNINGS   mean of {a.years} years of (OCF − SBC) − maintenance capex"
      f"   ({oe['unit']} millions)")
    P(f"  OCF tag: {oe['ocf_tag']}")
    P(f"\n  {'FY end':>12}{'OCF':>11}{'SBC':>9}{'D&A':>10}{'capex':>11}"
      f"{'OE capex':>12}{'OE D&A':>12}")
    for r in oe["rows"]:
        sbc_s = format(r["sbc"], fm) if r["sbc_tag"] else "n/f"
        P(f"  {r['fy']:>12}{r['ocf']:>11{fm}}{sbc_s:>9}{r['da']:>10{fm}}"
          f"{r['capex']:>11{fm}}{r['oe_capex']:>12{fm}}{r['oe_da']:>12{fm}}")
    P(f"  {'mean':>12}{'':>41}{oe['mean_capex']:>12{fm}}{oe['mean_da']:>12{fm}}")
    P("  OE capex = OCF − SBC − capital spending;  OE D&A = OCF − SBC − depreciation and amortization.")
    lower = {}
    for r in oe["rows"]:
        lower.setdefault("capex basis" if r["oe_capex"] <= r["oe_da"] else "D&A basis",
                         []).append(r["fy"][:4])
    P("  lower of the two each year: " + "; ".join(f"{k} in {', '.join(v)}" for k, v in lower.items()))
    P(f"  mean of the year-by-year lower: {oe['mean_lo']:{fm}};  of the higher: {oe['mean_hi']:{fm}}"
      f"  (lines 2 and 3 below use these)")
    P("  SBC tag by year: " + "; ".join(
        f"{r['fy'][:4]} {r['sbc_tag'] or 'n/f'}" for r in oe["rows"]))
    if any(not r["sbc_tag"] for r in oe["rows"]):
        P("  ** n/f = stock pay not found in XBRL; read the cash-flow statement. OE in those years")
        P("     deducts NOTHING for stock pay, which overstates it if the filer pays in stock. **")
    P("  capex tag by year: " + "; ".join(
        f"{r['fy'][:4]} {r['cap_tag']}{' + ' + r['soft_tag'] if r['soft_tag'] else ''}"
        for r in oe["rows"]))
    # THE WINDOW'S LAST YEAR, 2026-10-05 (SONY, MTRN). The window is the years in which OCF, D&A and
    # capex are ALL tagged; a filer that changes taxonomy (SONY, US GAAP to IFRS after FY3/21) or tag
    # (MTRN's FY2025 capex) ends it early without a word. Say so.
    last = oe["rows"][-1]["fy"]
    if oe.get("ocf_last") and oe["ocf_last"] > last:
        P(f"  ** OCF is tagged through {oe['ocf_last']} but the window ends at {last}: D&A or capex is")
        P("     not tagged for the later years under the elements read here. Read the later filings. **")
    if (date.today() - date.fromisoformat(last)).days > 550:
        P(f"  ** The window's last year, {last}, is over 18 months old. Later years may be filed under")
        P("     another taxonomy (US GAAP to IFRS) or other elements; read the latest annual report. **")
    if oe.get("da_amort_only"):
        P(f"  ** D&A WARNING: for {', '.join(oe['da_amort_only'])} the only depreciation element found is "
          f"AmortizationOfIntangibleAssets. The filer tags depreciation under its own element, so the D&A "
          f"column and every D&A-basis figure here are too low. Read the cash-flow statement. **")
    print("\n".join(oe_lines))

    # THE STATEMENT LINES THE COLUMNS ABOVE LEAVE OUT, 2026-10-05 (IESC, GENC, MBUU, MTRN, OSIS).
    # Read from the filings' calculation linkbases (see filing_lines). Each alternate is printed
    # beside the filed figure, labelled; neither is chosen. The analyst decides which governs.
    fl = filing_lines(cik, facts)
    alt_lines = []
    A = alt_lines.append
    A(f"\n  STATEMENT LINES FROM THE FILINGS (calculation linkbase; transcription; {oe['unit']} millions)")
    A(f"  read: {', '.join(fl['read']) or 'none'}"
      + (f";  NOT read: {'; '.join(f'{x} ({w})' for x, w in fl['failed'])}" if fl["failed"] else ""))
    any_alt = False
    alt_rows = []
    # FINANCE-LEASE PRINCIPAL AND PAID-IN-KIND INTEREST, 2026-10-05 (the KLXE run): equipment bought on
    # finance leases is paid for in the financing section, and PIK interest is added back inside operating
    # cash flow though it is a real cost; together about $36M of KLXE's 2025. Standard tags, so read from
    # companyfacts. Printed as alternates: the lease principal joins "capex alt", the PIK interest comes
    # off "OCF ex-sec". Neither is chosen here.
    fin_lease, _, _ = _annual(facts, ["FinanceLeasePrincipalPayments"])
    pik, _, _ = _annual(facts, ["PaidInKindInterest"])
    # Dividends paid to minority partners in consolidated subsidiaries (the ADNT run, 2026-10-05: $67M
    # to $106M a year, more than its whole five-year owner cash). Cash the owners of the parent never get.
    nci_div, _, _ = _annual(facts, ["PaymentsOfDividendsMinorityInterest"])
    for r in oe["rows"]:
        y = r["fy"]
        sec = dict(fl["sec"].get(y, {}))
        if pik.get(y):
            sec["us-gaap_PaidInKindInterest (non-cash interest added back)"] = abs(pik[y])
        # A stock-pay line in the statement that IS the SBC column (a standard SBC element, or the same filed
        # figure under the filer's own tag, as SXI's ShareBasedCompensationContinuingOperations
        # equals its APIC-adjustment tag) is the same money and is not "other".
        xs = {c: v for c, v in fl["sbc"].get(y, {}).items()
              if _local(c) not in SBC + SBC_FALLBACK      # the SBC column already chose among these
              and not (r["sbc_tag"] and abs(v - r["sbc"]) <= max(0.05, 0.001 * abs(r["sbc"])))}
        xc = {c: v for c, v in fl["capx"].get(y, {}).items()
              if _local(c) not in (r["cap_tag"], r["soft_tag"])}
        if nci_div.get(y):
            xc["us-gaap_PaymentsOfDividendsMinorityInterest (to minority partners, financing section)"] = abs(nci_div[y])
        if fin_lease.get(y):
            xc["us-gaap_FinanceLeasePrincipalPayments (financing section)"] = abs(fin_lease[y])
        sec_eff = sum(sec.values())
        alt_rows.append((r, sec, xs, xc, sec_eff))
        any_alt = any_alt or bool(sec or xs or xc)
    if not fl["read"]:
        A("  ** No filing linkbase could be read: securities inside operating cash flow, stock pay")
        A("     under the filer's own tags, and mine, intangible or software payments are NOT checked.")
        A("     Read the cash-flow statement. **")
    elif not any_alt:
        A("  none in the window: no securities purchases or sales inside operating cash flow, no other")
        A("  stock-pay line, no intangible, software or mine-development payment beside capex.")
    else:
        for r, sec, xs, xc, sec_eff in alt_rows:
            for c, v in sec.items():
                if v == 0:
                    continue
                A(f"    {r['fy']}  {'non-cash add-back' if 'PaidInKind' in c else 'securities line'} INSIDE operating cash flow  {c.replace('_', ':', 1)}"
                  f"  effect on OCF {v:+{fm}}")
            for c, v in xs.items():
                A(f"    {r['fy']}  other stock-pay line in OCF (not in the SBC column)  "
                  f"{c.replace('_', ':', 1)}  {v:{fm}}")
            for c, v in xc.items():
                A(f"    {r['fy']}  other capital payment (not in capex)  "
                  f"{c.replace('_', ':', 1)}  {v:{fm}}")
        A(f"\n  {'FY end':>12}{'OCF filed':>11}{'OCF ex-sec':>11}{'SBC+other':>11}"
          f"{'capex':>9}{'capex alt':>11}{'OE capex alt':>14}{'OE D&A alt':>12}")
        alts = []
        for r, sec, xs, xc, sec_eff in alt_rows:
            ocf_x = r["ocf"] - sec_eff
            sbc_x = r["sbc"] + sum(xs.values())
            cap_x = r["capex"] + sum(xc.values())
            oc, od = ocf_x - sbc_x - cap_x, ocf_x - sbc_x - r["da"]
            alts.append((oc, od))
            A(f"  {r['fy']:>12}{r['ocf']:>11{fm}}{ocf_x:>11{fm}}{sbc_x:>11{fm}}"
              f"{r['capex']:>9{fm}}{cap_x:>11{fm}}{oc:>14{fm}}{od:>12{fm}}")
        A(f"  {'mean':>12}{'':>53}{statistics.fmean(x[0] for x in alts):>14{fm}}"
          f"{statistics.fmean(x[1] for x in alts):>12{fm}}")
        A("  OCF ex-sec = OCF as filed less the securities lines' and PIK interest's effect; SBC+other = the SBC column plus")
        A("  the other stock-pay lines; capex alt = capex plus the other capital payments. The columns")
        A("  above are AS FILED; these are the ALTERNATES. Neither is chosen here.")
    print("\n".join(alt_lines))

    # v4 amendment 2026-08-27: BOTH windows, always. Test A showed two analysts
    # reaching a 28% different owner-earnings figure from the same filings purely
    # by choosing 3 years versus 5. The window is a judgment; it gets disclosed.
    alt_years = 5 if a.years == 3 else 3
    oe_alt = owner_earnings(facts, alt_years)
    if oe_alt:
        div = ((oe_alt["mean_lo"] - oe["mean_lo"]) / abs(oe["mean_lo"]) * 100
               if oe["mean_lo"] else float("nan"))
        print(f"\n  THE OTHER WINDOW ({alt_years}-yr, {len(oe_alt['rows'])} yrs of data)"
              f"   OE capex {oe_alt['mean_capex']:{fm}}  OE D&A {oe_alt['mean_da']:{fm}}"
              f"   yield {oe_alt['mean_capex'] / cap * 100:.2f}% (capex) "
              f"{oe_alt['mean_da'] / cap * 100:.2f}% (D&A)")
        print(f"  DIVERGENCE vs the {a.years}-yr window: {div:+.1f}% on the lower of the two bases")
        if abs(div) > 15:
            print("  ** The spread between the windows is part of the range, not a tiebreak;")
            print("     do not pick a window and defend it. **")
            note("     [E4-25] Working with a range of possibilities is the better approach.")
            note("     If the combined range (window spread x capex band) is too wide to reach")
            note("     a conclusion, THAT IS THE CONCLUSION [E4-25]. A wide spread is also a Q4")
            note("     finding about earnings reliability [E5-11].")

    sov_s = f"vs sovereign {sov:.2f}%" if sov is not None else "no sovereign (see above)"
    print(f"\n  1. THE YIELD                 capex basis {y_capex:5.2f}%   D&A basis {y_da:5.2f}%   {sov_s}")
    if sov is None:
        print("  2. GROWTH THE PRICE ASSUMES  REFUSED - no sovereign for the earnings currency.")
        print("  3. POINTS OVER THE SOVEREIGN REFUSED on the same ground.")
    elif g_imp is None:
        print(f"  2. GROWTH THE PRICE ASSUMES  REFUSED - the lower owner-earnings mean")
        print(f"     is at or below zero. A DCF on a non-positive base produces no")
        print(f"     number; the negative bottom boundary IS the statement.")
    else:
        print(f"  2. GROWTH THE PRICE ASSUMES  {g_imp*100:5.1f}%  (at a {rate*100:.2f}% rate, "
              f"on the year-by-year lower mean)")
    if sov is not None:
        if pts_lo is None or pts_hi is None:
            print(f"  3. POINTS OVER THE SOVEREIGN REFUSED on the same ground"
                  f"{'' if pts_hi is None else f' at the lower mean; higher mean {pts_hi:+.2f}'}")
        else:
            print(f"  3. POINTS OVER THE SOVEREIGN {pts_lo:+5.2f} (lower mean) .. {pts_hi:+5.2f} (higher mean)")
    # SIXTH HOME OF THE RETIRED RULE, found by the PEP run 2026-09-03. The framework
    # rewrote "no hurdle, it ranks" into "the floor first, then the ranking" on 2026-08-28;
    # copies have since been found and fixed in the template, run.py's --spread default,
    # the sector method's step 4, CLAUDE.md's one-screen summary - and this print, which
    # told every run.py user the opposite of the framework at the moment of decision.
    note(f"\n  THE FLOOR FIRST [E4-28]: below ~10% honest expectancy the name is quit on,")
    note(f"  not ranked. What clears the floor ranks against the opportunity set [E4-21].")
    bs_ccy = oe["unit"] or earn_ccy
    bs = balance_history(facts, bs_ccy)
    bs_lines = []
    if bs:
        cols = [r for r, _ in BS_ROWS if any(r in v for v in bs.values())]
        biggest = max(abs(x[0]) for v in bs.values() for x in v.values())
        scale, unit = (1e6, "millions") if biggest >= 1e9 else (1e3, "thousands")
        bs_lines.append(f"\n  BALANCE SHEETS, {len(bs)} fiscal year-ends ({bs_ccy} {unit}; first-filed XBRL "
                        f"vintage, transcription only; read the filed statements)")
        bs_lines.append("    year-end    " + "".join(f"{c:>12}" for c in cols))
        for e, v in bs.items():
            bs_lines.append(f"    {e}  " + "".join(
                f"{v[c][0] / scale:>12,.0f}" if c in v else f"{'-':>12}" for c in cols))
        accns = sorted({x[1] for v in bs.values() for x in v.values()})
        bs_lines.append("    accessions: " + ", ".join(accns))
        # The element behind each column, and the years each one covers, where a column uses more
        # than one (equity for V; lt debt noncurrent in one year and total in another).
        for c in cols:
            spans = {}
            for e, v in bs.items():
                if c in v:
                    spans.setdefault(v[c][2], []).append(e[:4])
            if len(spans) > 1 or c in ("equity", "lt debt"):
                bs_lines.append(f"    {c}: " + "; ".join(
                    f"{tg} ({', '.join(ys)})" for tg, ys in spans.items()))
        # DEBT ON THE FACE, 2026-10-05 (EXTR, OSIS). "lt debt" is one element and usually the
        # NON-CURRENT one, so the current portion, bank lines and commercial paper never showed
        # (OSIS's $384M bank line in FY2024). The debt lines are the ones the filings' balance-sheet
        # calculation puts under liabilities; each is a column, and their sum is labelled.
        pool = _pool(facts)
        dc = fl["debt_concepts"]
        if dc:
            series = {}
            for c in dc:
                s = {e: x[0] for e, x in _instants(pool, _local(c), bs_ccy).items()}
                for e, v in fl["debt"].items():        # filer's own tags: the filings read only
                    if c in v and e not in s:
                        s[e] = v[c] * 1e6
                series[c] = s
            ends = sorted(set(bs) | {e for s in series.values() for e in s if e >= min(bs)})[-len(bs):]
            bs_lines.append(f"\n    DEBT ON THE FACE OF THE BALANCE SHEET ({bs_ccy} {unit}; the lines the "
                            f"filings' calculation linkbase puts under liabilities)")
            bs_lines.append("    year-end    " + "".join(f"{'d' + str(i + 1):>10}" for i in range(len(dc)))
                            + f"{'sum':>11}")
            for e in ends:
                vals = [series[c].get(e) for c in dc]
                if all(v is None for v in vals):
                    continue
                tot = sum(v for v in vals if v is not None)
                bs_lines.append(f"    {e}  " + "".join(
                    f"{v / scale:>10,.0f}" if v is not None else f"{'-':>10}" for v in vals)
                    + f"{tot / scale:>11,.0f}" + ("*" if any(v is None for v in vals) else ""))
            for i, c in enumerate(dc):
                bs_lines.append(f"    d{i + 1} = {c.replace('_', ':', 1)}")
            bs_lines.append("    sum = the lines tagged that year-end; '-' = not tagged under that element "
                            "that year (read the statement);")
            bs_lines.append("    * = a partial sum, some line untagged that year-end. Leases are not in it.")
        else:
            got = {tg: _instants(pool, tg, bs_ccy) for tg in DEBT_FALLBACK}
            got = {tg: s for tg, s in got.items() if any(e in s for e in bs)}
            if got:
                bs_lines.append(f"\n    CURRENT DEBT ELEMENTS TAGGED ({bs_ccy} {unit}; no linkbase was read, "
                                f"so NO SUM: these elements can overlap, DebtCurrent includes the others)")
                bs_lines.append("    year-end    " + "".join(f"{'c' + str(i + 1):>10}" for i in range(len(got))))
                for e in bs:
                    bs_lines.append(f"    {e}  " + "".join(
                        f"{s[e][0] / scale:>10,.0f}" if e in s else f"{'-':>10}" for s in got.values()))
                for i, tg in enumerate(got):
                    bs_lines.append(f"    c{i + 1} = {tg}")
        print("\n".join(bs_lines))
    else:
        print(f"\n  BALANCE SHEETS: no annual {bs_ccy} instant facts found; read them from the filings")

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
            sov_w = (f"sovereign {sov:.2f}% ({sov_date}, {sov_src})" if sov is not None
                     else f"sovereign: {sov_src}")
            # shares and cap are already in millions here; the old block divided them by 1e6 again
            # and wrote 0.000M (fixed 2026-10-05).
            block = (f"\n  run.py arithmetic ({oe['unit']}M), {today}: price {px:,.2f}; shares {shares:,.3f}M "
                     f"({sh_src}{f'; x{split_f:g} split after that date' if split_f and abs(split_f - 1) > 1e-9 else ''}); "
                     f"cap {cap:,.0f}M; {sov_w}\n"
                     + "\n".join(oe_lines) + "\n" + "\n".join(alt_lines) + "\n"
                     + f"  yield {y_capex:.2f}% (capex basis) .. {y_da:.2f}% (D&A basis)\n"
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
            f"  {r['fy']}  OCF {r['ocf']:,.0f}  SBC {format(r['sbc'], ',.0f') if r['sbc_tag'] else 'n/f (not found in XBRL; read the cash-flow statement)'}  D&A {r['da']:,.0f}  "
            f"capex {r['capex']:,.0f}  ->  OE capex basis {r['oe_capex']:,.0f}, D&A basis {r['oe_da']:,.0f}"
            for r in oe["rows"])
        if sov is not None:
            tpl = tpl.replace(
                "- rate ____ % · date ____ · source (issuing authority) ____",
                f"- rate **{sov:.2f}** % · date **{sov_date}** · source **{sov_src}**")
        tpl = tpl.replace(
            "- Owner earnings by year: ____",
            f"- Owner earnings by year ({oe['unit']}M):\n{tbl}\n"
            f"  **{a.years}-yr mean: capex basis {oe['mean_capex']:,.0f}, D&A basis {oe['mean_da']:,.0f}**")
        tpl = tpl.replace(
            "- owner earnings ____ ÷ market cap ____ = **____ %** · sovereign **____ %**",
            f"- owner earnings **{oe['mean_capex']:,.0f} (capex) / {oe['mean_da']:,.0f} (D&A)** ÷ market cap "
            f"**{cap:,.0f}** = **{y_capex:.2f} / {y_da:.2f} %** · sovereign "
            f"**{f'{sov:.2f} %' if sov is not None else 'none'}**")
        if g_imp is not None:
            tpl = tpl.replace(
                "- year-1 growth needed to justify the quote: **____ %**",
                f"- year-1 growth needed to justify the quote: **{g_imp*100:.1f} %**")
        if pts_lo is not None and pts_hi is not None:
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
