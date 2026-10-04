#!/usr/bin/env python3
"""FLAGS — the Q3 red-flag record, assembled from the corpus's own checklist.

    *** TESTED ON TEN COMPANIES 2026-08-27. PARTIALLY ADMITTED. ***

    Full record: Framework/v4/TOOL TEST - flags, PARTIALLY ADMITTED.md

      [4]  share issuance   ADMITTED. The corpus's most computable flag [E5-15].
                            Only after two bugs were fixed: the split feed was a
                            10-year window (Ross Stores' falling count read as
                            RISING), and spinoffs are recorded as splits (GE, IBM).
                            Refuses spinoff-corrupted years rather than printing
                            them. Reports full-span AND 5-year, and says so when
                            they disagree in direction -- IBM has been ISSUING
                            since 2019 behind a decade-old buyback.
      [1b] pension          ADMITTED AS A PROMPT ONLY. Works where cleanly tagged
                            (FITB, TJX). False negative on WFC, which has a DB
                            plan and tags nothing. Cannot tell a company-level
                            figure from one plan's (Citigroup returns 1.50%).
                            Absence is NOT coverage.
      [1a] SBC              DEMOTED TO CONTEXT, not a flag. Post-FAS 123R
                            essentially everyone expenses, so a missing tag is a
                            TAGGING fact (MO tags nothing; Citi's last is 2012).
      [3]  guidance         NOT ADMITTED. Wrong document -- guidance lives in 8-K
                            releases, not the 10-K.
      [2]  footnotes        NOT BUILT. No defensible implementation found.

    python tools/flags.py WFC KLAC TJX --since 2005
    python tools/flags.py MO --text        # also pull guidance language + note bulk

WHY THIS EXISTS AND WHY THE LAST ATTEMPT DIED
---------------------------------------------
tools/integrity.py scanned Item 3 Legal Proceedings for regulatory keywords. It
was rejected 2026-08-26: XBRL litigation tags are blind before ~2010, keyword
counts were identical across seventeen Wells Fargo annual reports, and the Item 3
window swept in adjacent sections.

The corpus sweep then found that BUFFETT'S OWN CHECKLIST NEVER LOOKS THERE
[E4-22, 2002 letter]. It looks at accounting and disclosure CHOICES:

    1. weak accounting  -- comp not expensed, or "pension assumptions are
       fanciful"; "There is seldom just one cockroach in the kitchen"
    2. unintelligible footnotes -- "it's usually because the CEO doesn't want you to"
    3. trumpeted earnings projections and growth expectations
    4. serial share issuance [E5-15] -- "one of the surest indicators of a
       promotion-minded management, weak accounting, a stock that is overpriced
       and -- all too often -- outright dishonesty"

Three of the four are computable from the filed record. That is the whole reason
to rebuild rather than patch.

WHAT IT REFUSES TO DO
---------------------
Score, rank, or decide. Every flag is A PROMPT TO READ [E4-22]. TJX's 2022 CPSC
penalty is a real penalty and NOT a Q3 failure -- no keyword can make that
distinction, which is exactly why the judgment stays with the person running it
and must be justified against the ledger, not against a regex.

Every figure is stamped with the date it BECAME PUBLIC (the filing date), so a
run anchored at any date can cut the series there.

Ruling 14 test: does this get the same number sooner, or add a number? It gets
the same record sooner. It adds nothing -- the thresholds stay with the reader.
"""
import sys
try:  # Windows consoles default to cp1252 and cannot encode the
    sys.stdout.reconfigure(encoding="utf-8")  # box-drawing / minus glyphs
except Exception:
    pass
import argparse, os, re, sys, html, statistics
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as S

# ---- FLAG 1a: is share-based compensation expensed at all? -------------------
SBC_TAGS = ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"]

# ---- FLAG 1b: the pension return assumption Buffett calls "fanciful" ---------
PENSION_TAGS = [
    "DefinedBenefitPlanAssumptionsUsedCalculatingNetPeriodicBenefitCostExpectedLongTermReturnOnAssets",
    "DefinedBenefitPlanExpectedLongTermReturnOnPlanAssets",
    "DefinedBenefitPlanAssumptionsUsedCalculatingNetPeriodicBenefitCostExpectedLongTermRateOfReturnOnPlanAssets",
]

# ---- FLAG 4: the share count ------------------------------------------------
SHARE_TAGS = ["WeightedAverageNumberOfDilutedSharesOutstanding",
              "WeightedAverageNumberOfSharesOutstandingBasic"]

# ---- FLAG 3: guidance language (text) ---------------------------------------
# Deliberately narrow. The last tool drowned in boilerplate; these target a
# FORWARD NUMERIC COMMITMENT, which is the thing the corpus objects to.
GUIDANCE_PAT = re.compile(
    r"(?:we (?:expect|anticipate|project|target|forecast)[^.]{0,120}"
    r"(?:to be (?:in the range of|between|approximately)|will be approximately)"
    r"[^.]{0,80}(?:\$|\d+(?:\.\d+)?\s*(?:%|percent))"
    r"|(?:full[- ]year|fiscal \d{4}) guidance"
    r"|long[- ]term (?:earnings|EPS|revenue|growth) target"
    r"|we (?:reaffirm|raise|raised|lower|lowered) our (?:guidance|outlook))",
    re.I)


def facts_series(facts, tags, want_units=None):
    """{fiscal_end: (value, filed_date, ambiguous)} for the first tag that has any.

    AMBIGUITY IS REPORTED, NEVER RESOLVED BY GUESSING. Caught 2026-08-27: Citigroup
    returned a 1.50% "expected long-term return on plan assets" for 2022, which is
    not plausible for a pension. Cause -- a filer with several plans reports several
    values against the SAME period end, and taking the most-recently-filed one
    silently picks whichever happened to land last. A company-level reading cannot
    be recovered from companyfacts, which does not expose the dimension. So when one
    filing carries multiple distinct values for a period, the period is marked
    ambiguous and the caller must refuse it rather than print one.
    """
    for tax in ("us-gaap", "ifrs-full"):
        node = facts.get("facts", {}).get(tax, {})
        for t in tags:
            if t not in node:
                continue
            for unit, pts in node[t]["units"].items():
                if want_units and unit not in want_units:
                    continue
                buckets = {}
                for x in pts:
                    if x.get("form") not in ("10-K", "20-F"):
                        continue
                    end, filed, val = x.get("end"), x.get("filed"), x.get("val")
                    if not (end and filed) or val is None:
                        continue
                    if x.get("start"):          # duration fact -- annual only
                        d = (date.fromisoformat(end)
                             - date.fromisoformat(x["start"])).days
                        if not 340 <= d <= 380:
                            continue
                    buckets.setdefault(end, {}).setdefault(filed, set()).add(val)
                out = {}
                for end, byfiled in buckets.items():
                    newest = max(byfiled)
                    vals = byfiled[newest]
                    out[end] = (sorted(vals)[0], newest, len(vals) > 1)
                if out:
                    return out, t, unit
    return {}, None, None


def share_series(facts, ticker, since):
    """Diluted share count by fiscal year, NORMALISED TO TODAY'S SPLIT BASIS.

    A count reported in a filing dated D is on the share basis as of D. Splits
    effective after D must be applied to compare it with a later year, or a 2:1
    split reads as the company doubling its shares out of nowhere. Same
    split-invariance fix as the market-cap formula.
    """
    raw, tag, _ = facts_series(facts, SHARE_TAGS, want_units={"shares"})
    if not raw:
        return [], None, False
    rows, crossed = [], False
    for end in sorted(raw):
        if end < since:
            continue
        val, filed, amb = raw[end]
        try:
            f = S.split_factor_after(ticker, filed)
        except Exception:
            f = 1.0
        if abs(f - 1.0) > 1e-9:
            crossed = True
        # Yahoo records SPINOFFS as split events. A clean split is a small integer
        # ratio (2:1, 3:2, 10:1); a spinoff is not, and adjusting for it corrupts
        # the count. GE 2018 came back x0.200637, IBM x1.046 -- both spinoffs.
        ratio_ok = any(abs(f - r) < 1e-3 for r in
                       (1, 2, 3, 4, 5, 10, 15, 20, 1.5, 2.5, 0.5, 0.25, 0.1, 0.05,
                        6, 8, 7.5, 1.25, 30, 40, 50))
        rows.append(dict(fy=end, filed=filed, raw=val / 1e6, ambiguous=amb,
                         adj=val * f / 1e6, split_factor=f, ratio_ok=ratio_ok))
    return rows, tag, crossed


def item_text(cik, ticker, fd, acc, doc, cap=1_500_000):
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/{doc}"
    raw = S._get(url, S.SEC_UA, f"ar_{ticker}_{fd}.htm", max_age_h=24 * 90)
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"[ \t\xa0]+", " ", t)[:cap]


def annual_filings(cik, since):
    """Every 10-K/20-F, oldest first. Lifted unchanged from integrity.py, which
    was rejected for its DETECTION, not for this."""
    import json
    out = []
    d = json.loads(S._get(f"https://data.sec.gov/submissions/CIK{cik}.json",
                          S.SEC_UA, f"sub_{cik}.json", max_age_h=24 * 7))
    shards = [d["filings"]["recent"]]
    for f in d["filings"].get("files", []):
        try:
            shards.append(json.loads(S._get(
                f"https://data.sec.gov/submissions/{f['name']}", S.SEC_UA,
                f["name"], max_age_h=24 * 30)))
        except Exception:
            pass
    for r in shards:
        for fd, form, acc, doc in zip(r["filingDate"], r["form"],
                                      r["accessionNumber"], r["primaryDocument"]):
            if form in ("10-K", "20-F") and fd >= since and doc:
                out.append((fd, acc.replace("-", ""), doc))
    return sorted(set(out))


def run(ticker, since, want_text):
    cik, name = S.cik_for(ticker)
    if not cik:
        return dict(ticker=ticker, refused="NOT_AN_SEC_FILER")
    facts = S.sec_facts(cik)
    out = dict(ticker=ticker, name=name, cik=cik)

    sbc, sbc_tag, _ = facts_series(facts, SBC_TAGS)
    out["sbc"] = {k: v for k, v in sbc.items() if k >= since}
    out["sbc_tag"] = sbc_tag

    pen, pen_tag, pen_unit = facts_series(facts, PENSION_TAGS)
    out["pension"] = {k: v for k, v in pen.items() if k >= since}
    out["pension_tag"], out["pension_unit"] = pen_tag, pen_unit

    rows, sh_tag, crossed = share_series(facts, ticker, since)
    out["shares"], out["share_tag"], out["split_crossed"] = rows, sh_tag, crossed
    out["spinoff_suspect"] = [r["fy"] for r in rows if not r["ratio_ok"]]

    def cagr(sub):
        if len(sub) < 2:
            return None
        a, b = sub[0]["adj"], sub[-1]["adj"]
        y = (date.fromisoformat(sub[-1]["fy"])
             - date.fromisoformat(sub[0]["fy"])).days / 365.25
        return ((b / a) ** (1 / y) - 1) * 100 if a > 0 and y else None

    # BOTH windows. A single full-span CAGR hid IBM ISSUING since 2019 behind a
    # decade-old buyback, and the corpus's own warning is about exactly this:
    # "cognition, misled by tiny changes involving low contrast, will often miss
    # a trend that is destiny."
    out["cagr_full"] = cagr(rows)
    out["cagr_5y"] = cagr(rows[-6:])
    if rows:
        out["span_full"] = (rows[0]["fy"], rows[-1]["fy"])
        out["span_5y"] = (rows[-6:][0]["fy"], rows[-1]["fy"])

    if want_text:
        fl = annual_filings(cik, since)
        if fl:
            fd, acc, doc = fl[-1]
            try:
                txt = item_text(cik, ticker, fd, acc, doc)
                hits, seen = [], set()
                for m in GUIDANCE_PAT.finditer(txt):
                    s = txt[max(0, m.start() - 90): m.end() + 90].strip()
                    k = s[:60].lower()
                    if k not in seen:
                        seen.add(k)
                        hits.append(s)
                out["guidance"] = hits[:6]
                out["guidance_ar"] = fd
                out["doc_chars"] = len(txt)
            except Exception as e:
                out["text_err"] = f"{type(e).__name__}"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--since", default="2005-01-01")
    ap.add_argument("--text", action="store_true",
                    help="also scan the latest annual report for guidance language (slow)")
    a = ap.parse_args()
    if len(a.since) == 4:
        a.since += "-01-01"

    try:
        sov, sov_d, sov_src = S.sovereign("USD")
    except Exception:
        sov, sov_d, sov_src = None, None, None

    W = 100
    print("=" * W)
    print("Q3 RED-FLAG RECORD — the corpus's own checklist [E4-22, E5-15]. CANDIDATE TOOL.")
    print("Assembled and dated. NOT scored. Every flag is a prompt to READ.")
    if sov:
        print(f"USD 30y sovereign for reference: {sov:.2f}%  ({sov_d}, {sov_src})")
    print("=" * W)

    for t in a.tickers:
        r = run(t.upper(), a.since, a.text)
        print(f"\n{'-'*W}\n{r['ticker']}  {r.get('name','')}")
        if r.get("refused"):
            print(f"  REFUSED: {r['refused']}")
            continue

        # FLAG 1a -- report, do not adjudicate. Post-FAS 123R nearly every filer
        # expenses SBC, so absence of a tag is a TAGGING fact, not an accounting one.
        if r["sbc"]:
            yrs = sorted(r["sbc"])
            stale = yrs[-1] < "2020"
            print(f"  [1a] SBC tagged {len(yrs)} yrs, latest {yrs[-1]} = "
                  f"{r['sbc'][yrs[-1]][0]/1e6:,.0f}M  tag={r['sbc_tag']}")
            if stale:
                print("        ** STALE: no SBC tagged since then. Says nothing about "
                      "whether it is expensed — read the filing. **")
        else:
            print("  [1a] SBC: not tagged under the concepts checked. NOT a finding "
                  "that it is unexpensed — read the filing.")

        # FLAG 1b
        if r["pension"]:
            print(f"  [1b] pension expected long-term return  tag={r['pension_tag']} "
                  f"({r['pension_unit']})")
            shown = 0
            for k in sorted(r["pension"])[-8:]:
                v, filed, amb = r["pension"][k]
                if amb:
                    print(f"        {k}  REFUSED — filing carries several plan values "
                          f"for this date; no company-level figure in companyfacts")
                    continue
                pct = v * 100 if r["pension_unit"] == "pure" and v < 1 else v
                sp = f"  spread vs 30y {pct - sov:+5.2f}" if sov else ""
                print(f"        {k}  assumed {pct:5.2f}%   public {filed}{sp}")
                shown += 1
            if shown:
                print("        ^ \"fanciful\" is the reader's call [E4-22]. No threshold here.")
        else:
            print("  [1b] pension assumption: not tagged. NOT a finding that there is "
                  "no DB plan — Wells Fargo has one and tags nothing here.")

        # FLAG 4
        if r["shares"]:
            print(f"  [4]  diluted shares (M), split-normalised to today  "
                  f"tag={r['share_tag']}")
            for row in r["shares"][-8:]:
                mark = ""
                if row["split_factor"] != 1:
                    mark = f"  [x{row['split_factor']:g}]"
                    if not row["ratio_ok"]:
                        mark += " ** NOT A CLEAN SPLIT RATIO — likely a SPINOFF "
                        mark += "recorded as a split; this count is UNRELIABLE **"
                print(f"        {row['fy']}  {row['adj']:>12,.1f}   public {row['filed']}{mark}")
            for label, key, span in (("full", "cagr_full", "span_full"),
                                     ("5-yr", "cagr_5y", "span_5y")):
                if r.get(key) is not None:
                    d = "ISSUING" if r[key] > 0 else "retiring"
                    print(f"        {label:5} {r[span][0]} -> {r[span][1]}: "
                          f"{r[key]:+.2f}%/yr  ({d})")
            if r.get("cagr_full") is not None and r.get("cagr_5y") is not None \
                    and (r["cagr_full"] > 0) != (r["cagr_5y"] > 0):
                print("        ** the two windows DISAGREE in direction — the recent "
                      "one is the live fact **")
            if r["spinoff_suspect"]:
                print(f"        ** spinoff-corrupted years: "
                      f"{', '.join(r['spinoff_suspect'][:6])} — flag 4 not usable here **")
            elif r["split_crossed"]:
                print("        series crosses a split; counts normalised, raw differs")
        else:
            print("  [4]  no diluted share count in XBRL — read the cover page")

        # FLAG 3 -- NOT ADMITTED. Kept visible so the next attempt starts here.
        if a.text:
            print("  [3]  ** NOT ADMITTED — WRONG DOCUMENT. ** Earnings guidance lives "
                  "in 8-K releases and calls,")
            print("        not the 10-K. Tested 2026-08-27: MO matched only CAPEX "
                  "guidance (not the earnings")
            print("        guidance [E4-22] objects to); TJX matched nothing despite "
                  "guiding EPS every quarter.")
            if r.get("text_err"):
                print(f"        scan error: {r['text_err']}")
            elif r.get("guidance"):
                print(f"        raw matches in AR {r['guidance_ar']}, shown as evidence "
                      f"of the defect only:")
                for s in r["guidance"]:
                    print(f"          ...{s[:140]}...")

    print(f"\n{'-'*W}")
    print("A fired flag obliges a read, not a verdict. A clean sheet is not a clearance.")
    print("Q3 stays a person reading the filed record and citing the ledger [E5-17].")
    return 0


if __name__ == "__main__":
    sys.exit(main())
