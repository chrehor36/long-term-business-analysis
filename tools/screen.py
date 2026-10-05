#!/usr/bin/env python3
"""SCREEN — rank a universe by owner-earnings yield against its own sovereign.

    python tools/screen.py --sp500                 # the committed 2013 reconstruction
    python tools/screen.py TJX ROST BURL V MA
    python tools/screen.py --file tickers.txt --out Screens/2026-08-26 v4 screen.csv

v4 CHANGES WHAT A SCREEN IS. There is no pass/fail column. Since v4.1 (Test D,
2026-08-28) Q5 applies the ~10% floor first [E4-28] and what clears it RANKS --
Buffett refuses the term "hurdle" and Munger says a threshold "doesn't work as
well as a system of comparing things" [E4-21]. The output is an ORDERED
opportunity set; the floor is applied in the run file, never here. The top of
that list is where the six questions get spent. (Docstring corrected 2026-09-25:
it carried the pre-Test-D "no hurdle" wording.)

THREE GUARDS, all learned the hard way and recorded in Screens/*.md:

  CURRENCY   A USD market cap divided by home-currency earnings once produced a
             false 19% yield (ATLKY: SEK vs USD, ~10x). Here the earnings
             currency comes from the XBRL unit key itself and is compared to the
             quote currency; a mismatch is REFUSED, never silently converted.

  UNITS      A double division by 1e6 once produced "509 passes". Every yield
             above IMPLAUSIBLE_YIELD is refused rather than reported.

  FLOAT      Market cap below filed public float is near-impossible, since float
             is a subset of cap. It reliably marks a bad share count or a
             cover-page typo. Thresholds from the corrected screen.

Anything refused is REPORTED, never dropped silently -- a screen that quietly
discards what it cannot compute reads as coverage it does not have.
"""
import sys
try:  # Windows consoles default to cp1252 and cannot encode the
    sys.stdout.reconfigure(encoding="utf-8")  # box-drawing / minus glyphs
except Exception:
    pass
import argparse, csv, json, os, statistics, sys, time
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as S
from run import owner_earnings, points_over, OCF, SBC, DA, CAP, SH, share_counts, SHARE_ISSUED

ROOT = S.ROOT
IMPLAUSIBLE_YIELD = 50.0     # % — above this it is a units or share-count fault
FLOAT_STRICT, FLOAT_APPROX = 0.50, 0.25   # cap/float exclusion floors

# Currency of the quote -> currency the sovereign should be taken in.
CCY_OK = {"USD": "USD", "EUR": "EUR", "JPY": "JPY"}


def public_float(facts):
    dei = facts.get("facts", {}).get("dei", {}).get("EntityPublicFloat")
    if not dei:
        return None, None
    pts = [x for u in dei["units"].values() for x in u if x.get("val")]
    if not pts:
        return None, None
    latest = max(pts, key=lambda x: x["end"])
    return latest["val"] / 1e6, latest["end"]


def screen_one(t, years=3):
    """Returns a dict. 'refused' is set when a guard fires -- never silently dropped."""
    out = {"ticker": t}
    cik, name = S.cik_for(t)
    if not cik:
        out.update(refused="NOT_AN_SEC_FILER — use the evidence ladder (IR site, exchange)")
        return out
    out["name"] = name
    try:
        facts = S.sec_facts(cik)
        px, px_date, px_ccy = S.price(t)
    except Exception as e:
        out.update(refused=f"FETCH_FAILED: {type(e).__name__}")
        return out
    if not px:
        out.update(refused="NO_PRICE")
        return out

    oe = owner_earnings(facts, years)
    if not oe:
        out.update(refused="NO_OVERLAPPING_OCF_DA_CAPEX_FACTS")
        return out

    # ---- GUARD 1: currency -------------------------------------------------
    earn_ccy, quote_ccy = oe["unit"], (px_ccy or "").upper()
    out.update(earn_ccy=earn_ccy, quote_ccy=quote_ccy)
    if earn_ccy != quote_ccy:
        out.update(refused=f"CURRENCY_MISMATCH earnings {earn_ccy} vs quote {quote_ccy} "
                           f"— refused, not converted")
        return out
    if earn_ccy not in CCY_OK:
        out.update(refused=f"NO_SOVEREIGN_SOURCE for {earn_ccy}")
        return out

    # 2026-10-05: the same share count run.py uses (the newest filed count under 550 days old, else
    # the weighted average), with any split after its date applied, so a post-split quote is never
    # multiplied by a pre-split count (IESC showed a cap twice its true size here).
    fresh = [c for c in share_counts(facts)
             if (date.today() - c[0]).days <= 550 and c[3] != SHARE_ISSUED[0]]
    if fresh:
        sh_date, shares = max(fresh, key=lambda c: c[0])[:2]
    else:
        sh, _, _ = S.annual(facts, SH)
        shares = sh[max(sh)] if sh else None
        sh_date = date.fromisoformat(max(sh)) if sh else None
    if not shares:
        out.update(refused="NO_SHARE_COUNT_IN_XBRL")
        return out
    try:
        split_f = S.split_factor_after(t, sh_date.isoformat())
    except Exception:
        split_f = None
    if split_f and abs(split_f - 1.0) > 1e-9:
        shares *= split_f
        out.update(split_after_count=split_f)
    cap = px * shares
    out.update(shares=round(shares, 1), price=px, price_date=px_date,
               cap=round(cap, 1), oe_lo=round(oe["mean_lo"], 1),
               oe_hi=round(oe["mean_hi"], 1), years=len(oe["rows"]))

    # ---- GUARD 3: float ----------------------------------------------------
    flt, flt_date = public_float(facts)
    if flt:
        ratio = cap / flt
        out.update(float_mn=round(flt, 1), cap_over_float=round(ratio, 2),
                   float_date=flt_date)
        if ratio < FLOAT_STRICT:
            out.update(refused=f"CAP_BELOW_FLOAT {ratio:.2f}x — bad share count or "
                               f"cover-page typo")
            return out

    y_lo = oe["mean_lo"] / cap * 100
    y_hi = oe["mean_hi"] / cap * 100

    # ---- GUARD 2: units ----------------------------------------------------
    if y_hi > IMPLAUSIBLE_YIELD:
        out.update(refused=f"IMPLAUSIBLE_YIELD {y_hi:.1f}% — units or share-count fault")
        return out

    sov, sov_date, sov_src = S.sovereign(earn_ccy)
    pts_lo = points_over(cap, oe["mean_lo"], 0.03, sov)
    pts_hi = points_over(cap, oe["mean_hi"], 0.03, sov)
    # 2026-10-05: points_over returns None when owner earnings are zero or negative (no
    # growth rate reconciles the price). Report it as refused rather than crash the screen.
    if pts_lo is None or pts_hi is None:
        out.update(yield_lo=round(y_lo, 2), yield_hi=round(y_hi, 2),
                   refused=f"POINTS_NOT_COMPUTABLE — owner earnings {oe['mean_lo']:.1f} .. "
                           f"{oe['mean_hi']:.1f} (zero or negative)")
        return out
    out.update(yield_lo=round(y_lo, 2), yield_hi=round(y_hi, 2),
               sovereign=sov, sov_date=sov_date,
               pts_lo=round(pts_lo, 2), pts_hi=round(pts_hi, 2))
    return out


def universe_sp500():
    p = os.path.join(ROOT, "Backtests", "2026-07-22 SP500 2013 Reconstruction.json")
    d = json.load(open(p, encoding="utf-8"))
    return d["reconstructed_tickers"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tickers", nargs="*")
    ap.add_argument("--sp500", action="store_true",
                    help="the committed 2013 S&P reconstruction (503 names)")
    ap.add_argument("--file")
    ap.add_argument("--years", type=int, default=3)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--out")
    a = ap.parse_args()

    names = list(a.tickers)
    if a.sp500:
        names += universe_sp500()
    if a.file:
        names += [l.strip() for l in open(a.file) if l.strip()]
    names = list(dict.fromkeys(n.upper() for n in names))
    if a.limit:
        names = names[:a.limit]
    if not names:
        ap.error("give tickers, --sp500, or --file")

    rows, refused = [], []
    for i, t in enumerate(names, 1):
        r = screen_one(t, a.years)
        (refused if r.get("refused") else rows).append(r)
        if len(names) > 12 and i % 25 == 0:
            print(f"  ...{i}/{len(names)}", file=sys.stderr)
        time.sleep(0.05)

    rows.sort(key=lambda r: r["pts_lo"], reverse=True)

    print("=" * 92)
    print(f"OWNER-EARNINGS SCREEN — {len(rows)} ranked, {len(refused)} refused"
          f"   ({a.years}-year mean)")
    print("There is no pass mark. This is an ordered opportunity set [E4-21].")
    print("=" * 92)
    print(f"{'#':>3} {'ticker':<7}{'yield lo..hi':>16}{'sov':>7}{'pts over sovereign':>22}"
          f"{'cap':>13}")
    for i, r in enumerate(rows, 1):
        print(f"{i:>3} {r['ticker']:<7}{r['yield_lo']:>8.2f}..{r['yield_hi']:<6.2f}"
              f"{r['sovereign']:>7.2f}{r['pts_lo']:>11.2f} ..{r['pts_hi']:>7.2f}"
              f"{r['cap']/1000:>12,.1f}B")

    if refused:
        print(f"\nREFUSED — reported, not silently dropped ({len(refused)}):")
        for r in refused:
            print(f"  {r['ticker']:<7} {r['refused']}")

    if a.out:
        path = a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out)
        cols = ["ticker", "name", "yield_lo", "yield_hi", "sovereign", "sov_date",
                "pts_lo", "pts_hi", "oe_lo", "oe_hi", "years", "cap", "price",
                "price_date", "shares", "earn_ccy", "quote_ccy", "float_mn",
                "cap_over_float", "refused"]
        with open(path, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for r in rows + refused:
                w.writerow(r)
        print(f"\nwrote {os.path.relpath(path, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
