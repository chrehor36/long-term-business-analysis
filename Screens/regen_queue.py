#!/usr/bin/env python3
"""Regenerate the master run queue with the 2026-09-02 fixes applied.

COMPUTATION - NOT A CLEARANCE (operator rule 3). This decides READING ORDER and nothing
else; it cannot open or close a question on any business.

Fixes now in force that were not when `2026-09-01 MASTER RUN QUEUE.csv` was written:
  * annual() is a UNION over the tag list, not first-tag-wins (70 of 379 names moved)
  * acquisition_flag() is bounded by the owner-earnings window, not by the tag's own periods
  * level_shift() refuses a ratio across zero instead of inverting
  * stale_filer() added - the time axis, which nothing watched
  * the sovereign comes from the issuing authority, with FRED a labelled fallback
"""
import csv, io, json, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"c:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
sys.path.insert(0, os.path.join(ROOT, "Screens"))
sys.argv = [sys.argv[0]]
import bt17_microcap as M
import floor_screen as F
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources as _S

SRC = os.path.join(ROOT, "Screens", "2026-09-01 MASTER RUN QUEUE.csv")
DEST = os.path.join(ROOT, "Screens", "2026-09-02 MASTER RUN QUEUE (corrected).csv")

sov, sov_src = F.live_sovereign()
print(f"sovereign {sov:.2%}  ({sov_src})\n")

tick = M.cached_json("company_tickers.json",
                     "https://www.sec.gov/files/company_tickers.json")
sec = {str(v["ticker"]).upper(): int(v["cik_str"]) for v in tick.values()}
# THE NAME COLUMN OF THE SOURCE CSV IS NOT ALWAYS A NAME. Found by the L run of
# 2026-09-02, which reported that this file printed Loews Corporation as "Fire, Marine
# & Casualt" - the SIC INDUSTRY TITLE, truncated. The watchlist-triage CSV that feeds
# the master queue carries industry in the name position for the rows it contributed,
# and the defect was inherited rather than introduced. Resolve the name from the SEC
# ticker file, which is the registrant's own title, rather than from a column that has
# already been wrong once.
names = {str(v["ticker"]).upper(): v["title"] for v in tick.values()}
rows = list(csv.DictReader(open(SRC, encoding="utf-8")))

# HAND-READ CAP OVERRIDES. Found 2026-09-02: this script recomputes OWNER EARNINGS with
# every fix but takes cap_m from the SOURCE CSV - so PINS, whose cap the addendum showed
# was 4.06x too small on a pre-IPO share count, sailed through with the WRONG CAP and
# printed a 4.98% yield the hand-reprice had already corrected to 1.23%. The numerator
# was fixed and the denominator was not. Counts below are read off filed covers by hand
# (see ADDENDUM 2026-09-02 and ADDENDUM 2026-09-02 (3)); quotes as of 2026-09-02.
HAND_CAPS_M = {
    "PINS": 566_313_027 * 21.22 / 1e6,   # cover 2026-07-28, two classes
    "DKS":   89_502_537 * 137.34 / 1e6,  # cover 2026-05-29, two classes
    "FLNC": 184_596_369 * 10.56 / 1e6,   # Up-C economic count, cover 2026-06-30
    "BE":   294_527_346 * 217.28 / 1e6,  # cover audit 2026-09-02
}

# THE LIVE SCREEN READS THE NEWEST FILING OF A RESTATED PERIOD (DELL run, 2026-09-07).
# floor_screen defaults to "earliest" - what was knowable then - which is right for anything
# anchored in the past and WRONG here: this file prices companies at today's quote, so a
# restatement is public and reading the withdrawn figure is the error. 278 of 361 priced
# names carry at least one restated annual value in the owner-earnings tags.
F.VINTAGE = "newest"

def newest_periodic_end(facts):
    """Newest OPERATING-CASH period end across any periodic form - the 10-Q the annual date hides.

    Restricted to the OCF tags and to dates that have happened, after the first version -
    which took the max `end` across EVERY tag - printed 2034-03-31 for Innodata within an
    hour of being written. Filers tag forward-dated facts (debt maturities, lease and purchase
    commitments) under period ends years out, and a screen that reports one as "the newest
    filing" has invented a filing. Found 2026-09-11, same day as the column."""
    today = str(F.TODAY)
    best = ""
    ns = facts.get("facts", {})
    for tax in ("us-gaap", "ifrs-full"):
        for tag in F.OCF_TAGS:
            for unit, pts in ns.get(tax, {}).get(tag, {}).get("units", {}).items():
                for x in pts:
                    e = x.get("end") or ""
                    if (best < e <= today and x.get("start")
                            and x.get("form") in ("10-Q", "10-K", "20-F", "40-F", "6-K")):
                        best = e
    return best


out, unpriced = [], []
for r in rows:
    t = r["ticker"]
    k = next((x for x in (t, t.replace(".", "-")) if x in sec), None)
    if not k:
        continue
    p = os.path.join(M.CACHE, f"facts_{sec[k]}.json")
    if not os.path.exists(p):
        continue
    try:
        facts = json.load(open(p, encoding="utf-8"))
    except Exception:
        continue
    cap = float(r["cap_m"]) * 1e6 if r["cap_m"] not in ("", None) else None
    if t in HAND_CAPS_M:
        cap = HAND_CAPS_M[t] * 1e6

    # THE CAP SANITY GUARD, from the SHOP run of 2026-09-07 and it is the run's own
    # suggestion. This script recomputes owner earnings with every fix and takes cap_m from
    # the SOURCE CSV verbatim, which is how PINS carried a 4.06x error and SHOP a 3.40x one -
    # both reproduced to the dollar from a PRE-IPO share count. Hand overrides caught four
    # names; they do not scale, and SHOP was not among them.
    #
    # A market capitalisation cannot be smaller than the company's own filed PUBLIC FLOAT,
    # which is a SUBSET of shares outstanding - and dei:EntityPublicFloat sat in the same
    # payload the whole time. It FLAGS rather than refuses (operator rule 8): the float is a
    # filed number that can itself be wrong - MCFT reports one 607x its cap, which is a
    # tagging error, not a cap error - and deciding which of the two is broken is a reading,
    # not an arithmetic. Fires on 80 of 361 names.
    pf = (facts.get("facts", {}).get("dei", {}).get("EntityPublicFloat", {})
          .get("units", {}).get("USD", []))
    cap_flag = ""
    if pf and cap:
        _l = max(pf, key=lambda x: x.get("end", ""))
        if cap < _l["val"]:
            cap_flag = (f"CAP BELOW FILED PUBLIC FLOAT - cap ${cap/1e6:,.0f}M against a filed "
                        f"float of ${_l['val']/1e6:,.0f}M ({_l['val']/cap:.2f}x) as of "
                        f"{_l['end']}. A cap cannot be smaller than a subset of itself. One "
                        f"of the two is wrong - RE-STRIKE THE CAP BY HAND before using any "
                        f"yield on this row [operator rule 4].")

    st = F.stale_filer(facts)
    if st and st[2]:
        unpriced.append((t, "STALE", st[2]))
        continue
    oe = F.owner_earnings(facts)
    if oe == "CAPEX_UNRESOLVED":
        unpriced.append((t, "CAPEX", "only the D&A end resolves and [E5-20] calls it INVALID"))
        continue
    if oe in ("SBC_UNRESOLVED", "SBC_PARTIAL"):
        unpriced.append((t, "SBC", "stock compensation does not resolve undimensioned, and "
                                   "[E5-06] says SBC is simply an expense - pricing this row "
                                   "would subtract ZERO for it. READ THE FILING (BE, 2026-09-12)"))
        continue
    if not oe or not cap:
        continue
    ratio = F.share_count_shift(facts, t)
    if ratio is not None and not (0.75 <= ratio <= 1.50):
        unpriced.append((t, "PERIMETER", f"share count {ratio:.2f}x its level ~2 years ago"))
        continue

    vals = list(oe.values())
    bottom, top = min(vals), max(vals)
    ocf = F.annual(facts, F.OCF_TAGS)
    series = [ocf[y] for y in sorted(ocf)[-9:]]
    ls = F.level_shift(series) if len(series) > 4 else None
    by = F.best_year_dependence(series) if len(series) > 4 else None
    # THE SAME TWO FLAGS ON THE SERIES THAT IS ACTUALLY VALUED (PLPC run, 2026-09-07).
    # Both above read RAW OPERATING CASH, which does not net capex. On PLPC the two series
    # give OPPOSITE answers. Carried alongside rather than instead, because a DISAGREEMENT
    # between them is itself a prompt to read.
    oes = list(F.oe_annual(facts, "capex").values())[-9:]
    ls_oe = F.level_shift(oes) if len(oes) > 4 else None
    by_oe = F.best_year_dependence(oes) if len(oes) > 4 else None
    disagree = bool(ls and ls_oe and ((ls[0] is None) != (ls_oe[0] is None)))
    # THE WINDOW IS ALSO A CHOICE, found by the LRCX run of 2026-09-07. The nine-year window
    # above is arbitrary, and for a long-cycle industry its "earlier half" already contains
    # part of the current wave - so the flag agrees with itself off a CONTAMINATED BASE.
    # Lam reads 1.68 "STEP UP" on nine years and REFUSES the ratio on its full eighteen.
    # Measured: the two give a different KIND of answer on 25 of 291 names with more than
    # nine years filed. Carried, not chosen - which window is relevant is a judgment for the
    # reader, and operator rule 8 forbids the tool making it.
    full = [ocf[y] for y in sorted(ocf)]
    ls_full = F.level_shift(full) if len(full) > 4 else None
    win_disagree = bool(ls and ls_full and len(full) > 9
                        and ((ls[0] is None) != (ls_full[0] is None)))
    aq = F.acquisition_flag(facts, cap)
    # THE SILENT-GARBAGE FLAG, carried into the CSV for the same reason as the spread
    # caveat below (added 2026-09-07, from the CERT run). An EMPTY D&A series fails
    # loudly; a BROKEN one does not, and Certara's published oe_bottom/oe_top reproduce
    # to three decimals off a series with a 38x discontinuity in it.
    dd = F.da_discontinuity_flag(facts)
    # THE LIVE-DEAL CHECK (ROKU run, 2026-09-12). Cached 24h; a merger is announced in an
    # 8-K and no XBRL screen can see it. Three of the queue's names are under a deal form.
    dn = _S.deal_note(sec[k])
    nc = _S.name_change_note(sec[k])
    wc = F.working_capital_flag(facts)

    out.append(dict(
        ticker=t, name=names.get(k, r.get("name", ""))[:40],
        cap_m=round(cap / 1e6) if cap else r["cap_m"],
        oe_bottom_m=round(bottom / 1e6), oe_top_m=round(top / 1e6),
        # A RATIO NEEDS A DENOMINATOR THAT MEANS SOMETHING. Found twice: DAL's rebuilt range
        # crossed zero (no percentage is defined at all) and PLPC's bottom sat so near zero
        # that the percentage form came out at 3,733% on a series whose annual values run
        # -$19.0M to +$67.4M. Where the bottom is non-positive or under 5% of the top, the
        # cell carries a WORD and the dollar range carries the finding [E4-25].
        spread=(round((top - bottom) / bottom, 3)
                if bottom > 0 and bottom >= 0.05 * top else "n/a - see spread_dollars"),
        spread_dollars=f"${bottom/1e6:,.0f}M to ${top/1e6:,.0f}M",
        cap_flag=cap_flag,
        deal_note=dn,
        name_change_note=nc,
        wc_note=("" if not wc else wc[3][:260]),
        yield_bottom=round(bottom / cap, 4),
        vs_sovereign=round(bottom / cap - sov, 4),
        # A NEGATIVE BOTTOM HAS NO GROWTH REQUIREMENT (MRVL run, 2026-09-11). The row printed
        # 10.20% on a bottom of -$373M - "the growth needed to reach the floor" from a base
        # that is below zero is not a number, and the spread cell already refuses on the same
        # condition. Sorted to the end by the numeric key below; displayed as a word.
        growth_required=(round(F.FLOOR - bottom / cap, 4) if bottom > 0
                         else "n/a - negative bottom; see spread_dollars"),
        _sort=(F.FLOOR - bottom / cap),
        level_shift=("" if not ls else (round(ls[0], 2) if ls[0] is not None else "n/a")),
        level_note=("" if not ls else ls[1][:60]),
        best_year_dep=("" if not by else (round(by[0], 3) if by[0] is not None else "n/a")),
        # THE BARE NUMBER IS AMBIGUOUS AND MY OWN BRIEF MIS-READ IT (PINS run, 2026-09-07).
        # best_year_dependence() returns the LEAVE-TWO-OUT value whenever the pair test
        # fires, so 0.446 was described in a brief as "the five-year mean moves 44.6% when
        # the best year is dropped" when it is a TWO-year drop on a NINE-year OPERATING-CASH
        # series, and the single-year figure is 0.241. Those are opposite diagnoses: a
        # one-year spike says normalize down, a two-year step at the end says the LEVEL may
        # have changed. The function knew which; the CSV threw it away.
        best_year_note=("" if not by else f"{by[1][:96]} (9-yr OCF series)"),
        # The same two flags on owner earnings at the capex end - the series that is valued.
        level_shift_oe=("" if not ls_oe else (round(ls_oe[0], 2) if ls_oe[0] is not None else "n/a")),
        level_note_oe=("" if not ls_oe else ls_oe[1][:70]),
        best_year_dep_oe=("" if not by_oe else (round(by_oe[0], 3) if by_oe[0] is not None else "n/a")),
        flags_disagree=("FLAGS DISAGREE - one series refuses the ratio and the other does "
                        "not; read the filing [E4-25]" if disagree else ""),
        level_shift_full=("" if not ls_full else
                          (round(ls_full[0], 2) if ls_full[0] is not None else "n/a")),
        years_filed=len(full),
        window_disagree=(f"WINDOW DISAGREE - 9yr and the full {len(full)}yr series give "
                         f"different KINDS of answer; the 9yr base may already contain the "
                         f"wave [E4-41]" if win_disagree else ""),
        acq_note=(aq[2][:110] if aq and aq[2] else ""),
        da_note=("" if not dd else
                 f"D&A steps {dd[1]:.1f}x at {dd[0]} - READ Note 1 and the cash-flow "
                 f"statement before using either end of (c) [CERT 2026-09-07]"),
        # The AAPL spread caveat, carried into the CSV that run BRIEFS are built from
        # (added 2026-09-07). It existed only in floor_screen.main()'s console output,
        # so every brief written off this file inherited a width with no warning
        # attached - and the four-construction trap has now misled six consecutive runs.
        spread_caveat=("4-construction width only (3y/5y x two capex ends): CANNOT see "
                       "variation older than the 5-year window; rebuild it [E4-25]"
                       if len(vals) <= 4 else ""),
        newest_filing=str(st[0]) if st else "",
        # THE ANNUAL DATE HID TWO 10-Qs (MRVL run, 2026-09-11). `newest_filing` is the newest
        # ANNUAL period end; Marvell's row read 2026-01-31 while a $3.5bn acquisition, a $2bn
        # preferred and a 59M-share customer warrant sat in two later 10-Qs and an 8-K. The
        # newest PERIODIC period end is carried beside it so the gap is visible.
        newest_periodic=newest_periodic_end(facts),
    ))

out.sort(key=lambda x: x["_sort"])
for x in out:
    del x["_sort"]
with open(DEST, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)

_g = lambda x: x["growth_required"] if isinstance(x["growth_required"], float) else 9.99
t1 = [x for x in out if _g(x) <= 0.06]
t2 = [x for x in out if 0.06 < _g(x) <= 0.10]
print(f"{len(out)} priced   tier1 <=6% growth: {len(t1)}   tier2 6-10%: {len(t2)}   "
      f"rest: {len(out)-len(t1)-len(t2)}")
print(f"\nUNPRICED, with the ground stated ({len(unpriced)}):")
for t, why, note in unpriced:
    print(f"   {t:7s} {why:10s} {note[:90]}")
print(f"\nWROTE {DEST}")
