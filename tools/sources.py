#!/usr/bin/env python3
"""SOURCES — fetch and arithmetic only.

Framework v4 constrains tooling to efficiency: it may get the same number sooner,
it may not add a number. Nothing here forms a judgment.

Everything is cached under tools/_cache/ so a re-run costs no network.

  sovereign(ccy)          -> (rate_pct, date, source)   from the ISSUING AUTHORITY
  sec_facts(cik)          -> SEC XBRL companyfacts dict
  annual(facts, tags)     -> {fiscal_end: value_in_millions}
  price(ticker)           -> (last_close, date, currency)
  split_factor_after(t,d) -> product of split ratios effective after d
  market_cap(...)         -> the split-invariant formula
"""
import json, os, time, urllib.request, urllib.error
from datetime import date, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_cache")
os.makedirs(CACHE, exist_ok=True)

SEC_UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
WEB_UA = {"User-Agent": "Mozilla/5.0"}

# The sovereign is the rate for the currency the business EARNS in, taken from the
# authority that issues the debt -- never an aggregator, never a forecast [E4-15, E3-32].
# USD CORRECTED 2026-09-02, found by the UAL run. This module's own docstring said
# "from the ISSUING AUTHORITY" and the comment above says "never an aggregator" -- and
# then named FRED, which is a Federal Reserve Bank of St. Louis REDISTRIBUTION of a
# Treasury series, not the Treasury. CLAUDE.md was corrected on 2026-09-02 and
# daily_fetch.py had already moved to the Treasury curve; sources.py was missed, and
# run.py calls THIS module -- so every run.py-driven run was taking its sovereign from
# the wrong rung of the evidence ladder while a comment two lines above forbade it.
# FRED remains as the FALLBACK, which is what operator rule 5 permits and what the
# PLAB run of 2026-09-02 needed when FRED refused five consecutive connections.
USD_TREASURY = ("https://home.treasury.gov/resource-center/data-chart-center/"
                "interest-rates/daily-treasury-rates.csv/{yr}/all"
                "?type=daily_treasury_yield_curve&field_tdr_date_value={yr}"
                "&page&_format=csv")
USD_FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30"

SOVEREIGN_SOURCES = {
    "USD": ("US Treasury daily par yield curve",  # FRED is the fallback, see sovereign()
            USD_TREASURY),
    "JPY": ("Japan MOF official JGB curve",
            "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"),
    "EUR": ("ECB euro area AAA yield curve (SR_30Y)",
            "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y"
            "?lastNObservations=5&format=csvdata"),
}


def _get(url, headers=WEB_UA, cache_name=None, max_age_h=12, binary=False):
    # SEC REQUIRES A DECLARED USER AGENT (2026-09-19). The default here is a browser string,
    # and sec.gov answers HTTP 403 to it - so every caller that forgot `headers=SEC_UA` got a
    # hard failure on an SEC URL. Three runs hit it in one day (BLK, SOFI, and one more), each
    # losing fetches before diagnosing it. The SEC's own fair-access notice asks for a
    # declaring user agent, which SEC_UA carries, so an SEC host gets SEC_UA unless the caller
    # passed its own. No number changes; fewer lost fetches.
    if headers is WEB_UA and ("sec.gov" in url or "sec.report" in url):
        headers = SEC_UA
    path = os.path.join(CACHE, cache_name) if cache_name else None
    if path and os.path.exists(path):
        if (time.time() - os.path.getmtime(path)) / 3600 < max_age_h:
            mode = "rb" if binary else "r"
            with open(path, mode, **({} if binary else {"encoding": "utf-8"})) as f:
                return f.read()
    req = urllib.request.Request(url, headers=headers)
    try:
        raw = urllib.request.urlopen(req, timeout=45).read()
    except urllib.error.URLError as e:
        # INTERMITTENT CERTIFICATE FAILURE (2026-09-13). The ECB endpoint failed verification twice
        # in one night (once for me, once for the TM run) and succeeded on every retry, with both
        # the default and certifi trust stores. One retry against certifi's bundle - verification
        # stays ON; this never disables it. Same number, fewer lost fetches.
        if "CERTIFICATE_VERIFY_FAILED" not in str(e):
            raise
        import ssl
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
        raw = urllib.request.urlopen(req, timeout=45, context=ctx).read()
    data = raw if binary else raw.decode("utf-8", "replace")
    if path:
        mode = "wb" if binary else "w"
        with open(path, mode, **({} if binary else {"encoding": "utf-8"})) as f:
            f.write(data)
    return data


def sovereign(ccy="USD"):
    """30-year government yield for the earnings currency. Returns (pct, date, source)."""
    ccy = ccy.upper()
    if ccy not in SOVEREIGN_SOURCES:
        raise ValueError(f"no issuing-authority source configured for {ccy}; "
                         f"have {sorted(SOVEREIGN_SOURCES)}")
    label, url = SOVEREIGN_SOURCES[ccy]

    if ccy == "USD":
        yr = date.today().year
        try:
            txt = _get(USD_TREASURY.format(yr=yr), cache_name="sov_USD_treasury.csv")
            rows = [r for r in txt.strip().split("\n") if r.strip()]
            hdr = rows[0].split(",")
            i = hdr.index('"30 Yr"') if '"30 Yr"' in hdr else hdr.index("30 Yr")
            cells = rows[1].split(",")
            return (float(cells[i].strip('"')), cells[0].strip('"'), label)
        except Exception:
            pass
        # FALLBACK, and it is LABELLED as one so the run file records which rung was used.
        txt = _get(USD_FRED, cache_name="sov_USD_fred.csv")
        for line in reversed([r for r in txt.strip().split("\n") if r.strip()]):
            d, _, v = line.partition(",")
            if v.strip() not in (".", "", "value"):
                return float(v), d.strip(), "FRED DGS30 (FALLBACK - Treasury unreachable)"
        raise RuntimeError("could not parse USD sovereign from Treasury or FRED")

    txt = _get(url, cache_name=f"sov_{ccy}.csv")
    rows = [r for r in txt.strip().split("\n") if r.strip()]
    if ccy == "JPY":
        hdr = next(i for i, r in enumerate(rows) if r.startswith("Date,"))
        cols = rows[hdr].split(",")
        i30 = cols.index("30Y")
        for line in reversed(rows[hdr + 1:]):
            p = line.split(",")
            if len(p) > i30 and p[i30].strip():
                y, m, d = p[0].strip().split("/")
                return float(p[i30]), f"{y}-{int(m):02d}-{int(d):02d}", label
    elif ccy == "EUR":
        hdr = rows[0].split(",")
        ti, vi = hdr.index("TIME_PERIOD"), hdr.index("OBS_VALUE")
        last = rows[-1].split(",")
        return round(float(last[vi]), 3), last[ti], label
    raise RuntimeError(f"could not parse {ccy} sovereign feed")


def ticker_map():
    txt = _get("https://www.sec.gov/files/company_tickers.json", SEC_UA,
               "company_tickers.json", max_age_h=24 * 30)
    return {v["ticker"]: (str(v["cik_str"]).zfill(10), v["title"])
            for v in json.loads(txt).values()}


def cik_for(ticker):
    m = ticker_map()
    if ticker.upper() not in m:
        return None, None
    return m[ticker.upper()]


def sec_facts(cik):
    txt = _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",
               SEC_UA, f"facts_{cik}.json", max_age_h=24 * 7)
    return json.loads(txt)


def annual(facts, tags, forms=("10-K", "20-F"), lo=340, hi=380, vintage="earliest"):
    """Annual duration facts, MERGED ACROSS the tag list, newest last.
    Returns ({fiscal_end: value_in_millions}, tags_used, unit).

    Caught 2026-08-27: this used to return the FIRST tag that had any data and
    stop. Filers switch concepts mid-history -- Apple tags FY2013 operating cash
    flow under one and FY2014-15 under another -- so a whole-series read silently
    lost the years the other concept covered, and owner earnings were computed
    over a shorter window than the caller asked for. A tag list is a UNION.
    Earlier tags in the list still win for any period both cover, so a primary
    concept is never overwritten by a fallback.
    """
    out, used, unit_used = {}, [], None
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
                    if x.get("form") in forms and x.get("start"):
                        s = date.fromisoformat(x["start"])
                        e = date.fromisoformat(x["end"])
                        if lo <= (e - s).days <= hi:
                            hit = True
                            # VINTAGE: which filing of a restated period wins. Found by the
                            # DELL run of 2026-09-07. SEC companyfacts carries EVERY vintage
                            # of a restated figure under the same `end`, and this kept the
                            # FIRST one seen. Dell's Boomi divestiture line was -$3,957M as
                            # originally filed and RESTATED to +$16.0M in the FY2024 10-K,
                            # and the screen was reading the WITHDRAWN one - which is how
                            # acquisition_flag() reported a $4,237M perimeter against a true
                            # $296M. Measured across the priced queue: 278 of 361 names carry
                            # at least one restated annual value in the owner-earnings tags.
                            #
                            # WHY THIS IS A PARAMETER AND NOT A FIX. The two uses want
                            # OPPOSITE answers, and picking one silently is how the
                            # look-ahead bug voided four backtests:
                            #   "earliest" - what was knowable then. Correct for anything
                            #                anchored in the past. THE DEFAULT, so no
                            #                existing caller changes behaviour.
                            #   "newest"   - what is known now. Correct for a LIVE screen
                            #                pricing a company today, where a restatement is
                            #                public and pretending otherwise is the error.
                            # tools/pit.py remains the real anchor guard: it REFUSES facts
                            # by `filed <= anchor` rather than trusting a caller's flag.
                            #
                            # TAG PRECEDENCE IS PRESERVED either way - an earlier tag in the
                            # list still wins any period both cover, so only a later filing
                            # of the SAME concept can replace a value.
                            f = x.get("filed") or ""
                            prev = out.get(x["end"])
                            if prev is None or (vintage == "newest"
                                                and prev[1] == t and f > prev[2]):
                                out[x["end"]] = (x["val"] / 1e6, t, f)
                if hit:
                    unit_used = unit_used or unit
                    if t not in used:
                        used.append(t)
    return ({k: v[0] for k, v in out.items()},
            " + ".join(used) if used else None, unit_used)


def _chart(ticker, rng="10y", max_age_h=6):
    txt = _get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
               f"?range={rng}&interval=1d&events=div,split",
               WEB_UA, f"px_{ticker}_{rng}.json", max_age_h=max_age_h)
    return json.loads(txt)["chart"]["result"][0]


def price(ticker):
    """Latest close. Aggregator, permitted for LIVE QUOTES ONLY and flagged as such."""
    r = _chart(ticker)
    m = r["meta"]
    d = datetime.utcfromtimestamp(m["regularMarketTime"]).strftime("%Y-%m-%d")
    return m.get("regularMarketPrice"), d, m.get("currency")


def split_factor_after(ticker, anchor_iso):
    """Product of split ratios with an effective date AFTER anchor_iso.

    Market cap is split-invariant. Yahoo `close` is already on TODAY's share basis,
    so the correct fix is to bring the SHARE COUNT to today's basis rather than
    adjust the price. Use `close`, never `adjclose` (which also strips dividends
    and so is not a price at all).

    MUST use the FULL history, not the 10-year price window. Caught 2026-08-27:
    with range=10y, Ross Stores' 2011 and 2015 splits were invisible, so a share
    count that fell 2010-2026 was reported as RISING (+1.64%/yr, "ISSUING") --
    a silent failure pointing the wrong way, the same class as the look-ahead bug
    that voided four backtests. Splits are permanent facts; cache them for a week.
    """
    r = _chart(ticker, rng="max", max_age_h=24 * 7)
    ev = (r.get("events") or {}).get("splits") or {}
    anchor = datetime.strptime(anchor_iso, "%Y-%m-%d")
    f = 1.0
    for s in ev.values():
        try:
            when = datetime.utcfromtimestamp(s["date"])
        except (OSError, OverflowError, ValueError):
            # Pre-1970 epoch: Windows raises on negative timestamps. Such a split
            # is necessarily older than any anchor we use, and only splits AFTER
            # the anchor apply, so skipping it is correct rather than merely safe.
            continue
        if when > anchor:
            f *= s["numerator"] / s["denominator"]
    return f


def market_cap(close_at_anchor, shares_at_measurement, ticker, measurement_iso):
    """cap = close(anchor) x shares(measurement) x splits effective AFTER measurement."""
    return (close_at_anchor * shares_at_measurement
            * split_factor_after(ticker, measurement_iso))


if __name__ == "__main__":
    print("SOVEREIGNS — from the issuing authority\n")
    for c in ("USD", "JPY", "EUR"):
        try:
            rate, when, src = sovereign(c)
            print(f"  {c}  {rate:5.2f}%   {when}   {src}")
        except Exception as e:
            print(f"  {c}  FAILED: {e}")

# ---------------------------------------------------------------- EDGAR full-text search
FTS_URL = "https://efts.sec.gov/LATEST/search-index"


def fts_count(phrase, cik=None, forms=None):
    """(total_hits, url) for a phrase in EDGAR full-text search. RAISES on a malformed cik.

    THE SILENT-FALSE-NEGATIVE DEFECT, found by the CALX run of 2026-09-12 and diagnosed here.
    The `ciks` parameter accepts ONLY the bare zero-padded ten-digit CIK. Measured against
    ADTRAN (CIK 926282) and the phrase "Calix" in 10-Ks:

        ciks=0000926282      -> 200, 20 hits   CORRECT
        ciks=CIK0000926282   -> 200,  0 hits   the CALX harness sent this
        ciks=926282          -> 200,  0 hits   unpadded is equally silent

    BOTH malformed forms return HTTP 200 with a well-formed zero-hit body. Nothing errors,
    nothing warns, and "no competitor names this company" is exactly the conclusion a run
    draws from a zero - on a question the framework treats as evidence, because a moat is a
    relative claim [E3-03]. Primary documents on disk show ADTRAN naming Calix once, Cambium
    three times and Clearfield once, against the harness's zero for all three.

    So this REFUSES a malformed cik rather than passing it through. A guard that returns a
    plausible number on bad input is worse than no guard, which is the same lesson as the
    half-fixed level_shift of 2026-09-07.

    IT IS STILL A SCREEN, NOT EVIDENCE (operator rule 8). A hit count is a prompt to open the
    document; the naming test is settled by reading the competitor's filing, never by this."""
    import json as _j, urllib.parse as _up, urllib.request as _ur
    q = {"q": '"%s"' % phrase}
    if forms:
        # THE SAME SILENT-FALSE-NEGATIVE DEFECT IN THE OTHER PARAMETER, found by the SOFI run of
        # 2026-09-19 and fixed here. EDGAR wants `forms=10-K` or `forms=10-K,10-Q`. A Python list
        # urlencodes to `forms=%5B%2710-K%27%5D` and EDGAR answers HTTP 200 with a well-formed
        # ZERO and no error - exactly the failure the cik guard above exists to prevent, in the
        # parameter next to it. Measured on the phrase "Calix" the same afternoon:
        #     forms=['10-K']   -> 200,   0 hits   the natural Python idiom
        #     forms='10-K'     -> 200, 306 hits   CORRECT
        #     forms='10-K,10-Q'-> 200, 622 hits   CORRECT (306 + 316)
        #     forms=['10-K'] WITH a correct cik -> 0, where no-forms returns 40
        # So the cik guard could be defeated by the argument beside it. A list or tuple is now
        # joined the way the endpoint expects; a bad FORM NAME still fails loudly (HTTP 500),
        # so no further guard is needed.
        if isinstance(forms, (list, tuple, set)):
            forms = ",".join(str(f).strip() for f in forms)
        q["forms"] = str(forms).strip()
    if cik is not None:
        c = str(cik).strip()
        if not (c.isdigit() and len(c) == 10):
            raise ValueError(
                f"fts_count: cik must be the bare zero-padded 10-digit CIK, got {c!r}. "
                f"A 'CIK' prefix or an unpadded number returns HTTP 200 with ZERO hits and "
                f"no error - the CALX defect of 2026-09-12. "
                + (f"Use '{int(c):010d}'." if c.isdigit()
                   else "Strip any 'CIK' prefix and zero-pad to ten digits."))
        q["ciks"] = c
    url = FTS_URL + "?" + _up.urlencode(q)
    r = _ur.urlopen(_ur.Request(url, headers={
        "User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept": "application/json"}),
        timeout=60)
    return _j.loads(r.read()).get("hits", {}).get("total", {}).get("value"), url

# ---------------------------------------------------------------- live deals
# DEAL FORMS ONLY. A first pass included DEFA14A and the flag fired on MCD, COKE, BRK-B, CVX,
# PM, SO and C, because "Additional Definitive Proxy Soliciting Materials" is what almost every
# registrant files around its ANNUAL MEETING. Removed after measuring. 8-K Item 1.01 is carried
# as a SECONDARY note for the same reason: it covers an ordinary credit agreement and fires on
# ORLY, TSCO, GOOGL and a dozen others.
DEAL_FORMS = ("DEFM14A", "PREM14A", "S-4", "S-4/A", "SC 14D9", "SC TO-T", "425")


def deal_filings(cik, max_age_h=24):
    """(hard_hits, soft_hits, since) from the SEC submissions index. A PROMPT TO READ.

    THE BLIND SPOT NO XBRL SCREEN CAN SEE, found by the ROKU run of 2026-09-12 and the THIRD
    live merger this project has missed, after CTAS and ACLS. Roku signed a definitive merger
    agreement with Fox on 2026-06-14 - 0.9693 FOXA shares plus $96.00 cash - so its $154.93
    quote was a 3.1% MERGER SPREAD and not an owner-earnings price at all. The screen reads
    tagged financial data; a merger is announced in Item 1.01 of an 8-K, which has none.

    `hard_hits` are deal-specific forms. `soft_hits` are 8-K Item 1.01 filings, which cannot be
    told from a credit agreement without opening them. Both are filings, named and dated. This
    concludes nothing (operator rule 8): a live deal does not make a business good or bad, it
    makes the QUOTE a different kind of number, and the reader decides which.

    Measured across the unrun queue and all twenty-six gate-clearers: the hard list fires on
    THREE - ROKU (DEFM14A and 425, the Fox deal), ACLS (425) and AVGO (S-4) - while the soft
    list fires on roughly a third of everything."""
    import json as _j, urllib.request as _ur
    cik = f"{int(cik):010d}"
    txt = _get(f"https://data.sec.gov/submissions/CIK{cik}.json", SEC_UA,
               f"sub_{cik}.json", max_age_h=max_age_h)
    r = _j.loads(txt).get("filings", {}).get("recent", {})
    forms, dates = r.get("form", []), r.get("filingDate", [])
    items, accs = r.get("items", []), r.get("accessionNumber", [])
    since = max([d for f, d in zip(forms, dates) if f in ("10-K", "20-F", "40-F")], default="")
    hard, soft = [], []
    for i, f in enumerate(forms):
        d = dates[i]
        if since and d <= since:
            continue
        if f in DEAL_FORMS:
            hard.append((f, d, accs[i]))
        elif f == "8-K" and "1.01" in (items[i] if i < len(items) else "" or ""):
            # AN AMENDMENT IS NOT A SECOND AGREEMENT (FLNC run, 2026-09-13). Fluence's "two" Item
            # 1.01 filings were one revolver amendment and an 8-K/A correcting a typo in it. An
            # 8-K/A restates an event already filed; it never announces a new one. Originals only.
            soft.append((f, d, accs[i]))
    return hard, soft, since


def deal_note(cik):
    """One line for a screen row, or "" when nothing deal-shaped has been filed."""
    try:
        hard, soft, since = deal_filings(cik)
    except Exception as e:
        return f"deal check FAILED ({type(e).__name__}) - run it by hand"
    if hard:
        f, d, a = sorted(hard, key=lambda h: h[1])[0]
        return (f"LIVE DEAL FORM: {len(hard)} filing(s) since the annual report of {since}, first "
                f"{f} on {d} ({a}). IF A DEAL IS LIVE THE QUOTE IS A SPREAD, NOT AN "
                f"OWNER-EARNINGS PRICE - read it before pricing anything [ROKU, 2026-09-12].")
    if soft:
        # THE EXHIBIT TELLS THEM APART, measured 2026-09-13 after the ACVA run. A merger is
        # announced in an 8-K Item 1.01 DAYS before any proxy or 425 exists, so a fresh deal sat
        # in this soft note: Copart signed to buy ACV on 2026-09-10 and the run priced a quote
        # that was a 0.86% spread. The merger-agreement exhibit EX-2.1 ("plan of acquisition")
        # separates it. Validated on its motivating case AND three known non-deals (ACV's own
        # buyback, Stanley's credit facility, ACMR's share sale all carry no EX-2.1), then swept
        # across all 122 soft names: EX-2.1 on 18 filings at 16 names, and ALL 16 READ AS REAL
        # M&A AGREEMENTS - no false positive. This is the discipline Item 2.01 failed.
        #
        # IT DOES NOT SAY WHICH SIDE, and that is left to the reader on purpose: EX-2.1 is filed
        # by the target AND the acquirer. A regex classifier was tried and called Enerpac and
        # Embecta targets when both are buyers. A target's quote is a SPREAD; an acquirer's
        # perimeter changes. Different findings, same prompt: open it.
        m_and_a = []
        for f, d, a in soft:
            try:
                idx = _get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                           f"{a.replace('-', '')}/{a}-index.htm", SEC_UA,
                           f"idx_{a}.html", max_age_h=24 * 30)
            except Exception:
                continue
            import re as _re    # THE SAME REGEX THE 16-OF-16 SWEEP VALIDATED, not a look-alike
            if "EX-2.1" in set(_re.findall(r">\s*(EX-\d+(?:\.\d+)?)\s*<", idx)):
                m_and_a.append((d, a))
        if m_and_a:
            d, a = sorted(m_and_a)[0]
            return (f"M&A AGREEMENT ON FILE: EX-2.1 (plan of merger or acquisition) with the 8-K "
                    f"Item 1.01 of {d} ({a}). It is filed by the TARGET and the ACQUIRER alike - "
                    f"READ IT: if this company is being bought the quote is a SPREAD, if it is "
                    f"buying the perimeter changes [ACVA, 2026-09-13].")
        return (f"{len(soft)} 8-K Item 1.01 filing(s) since {since}, none carrying a merger "
                f"agreement (EX-2.1) - most likely a credit facility or offering; open them "
                f"only if something else is odd.")
    return ""

def name_change_note(cik, window_start="2017-01-01"):
    """A name change inside the data window that shares no word with the current name, or "".

    A PROMPT TO READ, with its precision stated. From the NEGG run of 2026-09-13: Newegg reverse-merged
    into a CIK that had belonged to Dehaier Medical and then Lianluo Smart, and companyfacts under that
    CIK held BOTH companies' 2019-2020 figures - which is what produced a 12.9x "D&A step" that was never
    Newegg's. Nothing in the screen could see that a different company's history sat under the same CIK.

    The SEC submissions record carries `formerNames` with dates, and it caught NEGG exactly. MEASURED
    before building: raw, it fires on 101 of 331 names and is mostly noise - Cisco, Walmart and ADM show
    a "former name" identical to the current one (SEC bookkeeping), and many are rebrands. Dropping
    names identical once normalised, and rebrands that share a real word, leaves 41; read by hand,
    ROUGHLY 26 ARE GENUINE PERIMETER EVENTS (de-SPACs, spin-off shells, reverse mergers like NEGG,
    TECX and ARMP, mergers like Helix into Hornbeck) and ~15 ARE STILL REBRANDS the word filter misses
    (Gannett to USA TODAY, A-Mark to Gold.com; Newtek counts six times across its share classes).
    ABOUT 60% PRECISION - a prompt to check whether multi-year figures are one company, not a finding.
    A de-SPAC usually carries the operating target's history, so the dangerous subset is the reverse
    merger into an operating shell, and only reading tells them apart."""
    import json as _j, re as _re
    stop = {"inc", "corp", "corporation", "co", "company", "ltd", "limited", "plc", "llc", "lp", "group",
            "holdings", "holding", "the", "de", "tx", "uk", "sa", "nv", "and", "of", "incorporated"}
    toks = lambda n: {w for w in _re.findall(r"[a-z0-9]+", n.lower()) if w not in stop and len(w) > 1}
    try:
        cik = f"{int(cik):010d}"
        d = _j.loads(_get(f"https://data.sec.gov/submissions/CIK{cik}.json", SEC_UA,
                          f"sub_{cik}.json", max_age_h=24))
    except Exception:
        return ""
    now = d.get("name", "")
    cand = [f for f in d.get("formerNames", [])
            if (f.get("to") or "")[:10] >= window_start
            and toks(f.get("name", "")) != toks(now) and not (toks(f.get("name", "")) & toks(now))]
    if not cand:
        return ""
    f = max(cand, key=lambda x: x.get("to", ""))
    return (f"NAME CHANGE inside the data window: was '{f.get('name','')}' until {(f.get('to') or '')[:10]}. "
            f"Possibly a reverse merger, de-SPAC, spin or merger whose predecessor's figures sit under this "
            f"CIK - or a rebrand (~60% of these are real perimeter events). CHECK THAT MULTI-YEAR FIGURES ARE "
            f"ONE COMPANY [NEGG, 2026-09-13].")

