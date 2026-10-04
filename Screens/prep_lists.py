#!/usr/bin/env python3
"""PREP THE OPERATOR LISTS — merge, validate, exclude, enrich, tier.

Input: Screens/_input/list_{largecap,midcap,smallcap}.csv (operator-supplied 2026-08-31).
Output: Screens/2026-08-31 PREPPED LIST.csv + a tiered markdown reading list.

Stages, in order, cheapest first (nothing expensive runs on a name already killed):
  1 MERGE + DEDUPE across the three lists, recording which list(s) each came from.
  2 VALIDATE the ticker against SEC company_tickers.json  -> NOT_AN_SEC_FILER kills it
    (catches fabricated rows, foreign lines, and stale tickers) and against a LIVE price
    (no close in the last 45 days -> DEAD_OR_ACQUIRED).
  3 EXCLUDE by standing directive, with the corpus ground recorded on each:
      FINANCIAL   banks/BDCs/mortgage REITs/insurers  [operator directive 2026-08-30;
                  E2-50 stroke-of-a-pen, E3-29 leverage]
      REGULATED   rate-regulated utilities — [E3-03] criterion 3 is "NOT subject to price
                  regulation", so a regulated utility fails Q2 by definition
      MLP         K-1 partnerships — taxable-account friction; verify each (SGU elected
                  corporate tax and issues a 1099, so LP in the name is a prompt, not a verdict)
      ALREADY     names with a committed v4.1 run or a PORTFOLIO position
  4 ENRICH survivors only: 5-year worst filed NI (10-K, filed<=today, earliest-filed per
    fiscal end — the frozen statute rule), house-rule market cap, statute yield, trailing
    dividend + 5y dividend CAGR + cut flag, payout vs worst-5y EPS.
  5 TIER for reading order.

A READING LIST, NEVER A BUY LIST [E5-36]. Every flag is a prompt to read.
"""
import csv, json, os, re, sys, time
from datetime import date, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
sys.argv = [sys.argv[0]]
import bt17_microcap as M  # noqa: E402

TODAY = date.today()
AMONTH = f"{TODAY.year}-{TODAY.month:02d}"
PREVMONTH = (TODAY.replace(day=1) - timedelta(days=1)).strftime("%Y-%m")

ALREADY = {
    "COST": "run 2026-08-30: Q1-Q4 IN, below floor; alerts armed",
    "FLO": "run 2026-08-30: Q2 OUT (melt+leverage)",
    "OXM": "run 2026-08-30: Q2 OUT (dividend uncovered)",
    "ASIX": "run 2026-08-30: Q2 OUT (price taker)",
    "KOP": "run 2026-08-30: Q2 OUT (price is the guidance)",
    "CCS": "run 2026-08-30: Q2 OUT (commodity builder)",
    "SGU": "run 2026-08-30: Q2 OUT (managed melt)",
    "WEYS": "run 2026-08-30: Q2 OUT (specials, not compounding)",
    "AMPH": "run 2026-08-30: Q2 OUT (surfing, not moat)",
    "ETD": "run 2026-08-30: Q2 OUT (melt)",
    "AXR": "run 2026-08-30: Q2 OUT (depleting asset)",
    "SD": "run 2026-08-30: Q2 OUT (two books, one book)",
    "RMR": "run 2026-08-30: Q2 OUT (moat void on control change)",
    "CHWY": "run in flight 2026-08-31",
    "MITSY": "HELD; run 2026-08-28: Q2 OUT, HOLD under E2-28",
    "NCLTY": "HELD; re-run 2026-08-28 under v4.1",
    "ASML": "SOLD 2026-08-28 on the Q6 read; watch-list",
    "V": "HELD (Roth anchor)", "TJX": "Test A subject; ranks below the bond",
    "HRB": "HELD; Q6 read 2026-08-28", "TBTC": "HELD (starter)",
    "BRK.B": "the corpus itself - not a candidate",
}

FIN_PAT = re.compile(r"bank|bdc|mortgage reit|insur|financ|asset manag|payment network|"
                     r"business investment", re.I)
UTIL_PAT = re.compile(r"utilit|electric|gas distribution|gas utility", re.I)
MLP_PAT = re.compile(r"\bLP\b|\bL\.P\.\b|Partners|Midstream|MLP", re.I)
REIT_PAT = re.compile(r"REIT|Realty|Properties|Trust\b", re.I)


def chart_robust(ticker, i):
    """M.chart with two fixes found 2026-08-31:
       (a) quote source writes class shares with a hyphen (BF-B), the lists use a dot;
       (b) range=max on a 60-year history (KO, MMM, IBM, HON, MO) times out - fall back
           to 20y, which is more than the framework's five-year windows need."""
    for tk in dict.fromkeys([ticker, ticker.replace(".", "-"), ticker.replace("-", ".")]):
        try:
            c, a, s = M.chart(tk, i)
            if c:            # an EMPTY but well-formed payload is a wrong-symbol answer,
                return c, a, s   # not a delisting - fall through to the next variant
        except Exception:
            pass
        for rng in ("20y", "10y"):
            try:
                u = (f"https://query{1 + (i % 2)}.finance.yahoo.com/v8/finance/chart/{tk}"
                     f"?range={rng}&interval=1mo&events=div%2Csplit")
                d = M.cached_json(f"chart_{tk}_{rng}.json", u, sleep=0.6)
                r = d["chart"]["result"][0]
                ts = r.get("timestamp") or []
                q = r["indicators"]["quote"][0].get("close") or []
                ad = (r["indicators"].get("adjclose") or [{}])[0].get("adjclose") or []
                closes, adjs = {}, {}
                for tt, c, a in zip(ts, q, ad):
                    mo = time.strftime("%Y-%m", time.gmtime(tt))
                    if c is not None:
                        closes[mo] = c
                    if a is not None:
                        adjs[mo] = a
                splits = []
                for ev in (r.get("events", {}).get("splits", {}) or {}).values():
                    num, den = float(ev.get("numerator") or 0), float(ev.get("denominator") or 1)
                    if num and den:
                        splits.append((date.fromtimestamp(ev["date"]), num / den))
                if closes:
                    return closes, adjs, splits
            except Exception:
                time.sleep(1)
    return None, None, None


def read_list(path, label):
    out = []
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            t = (r.get("Ticker") or "").strip().upper()
            if not t:
                continue
            biz = (r.get("Industry / Business Line") or r.get("Sub-Industry / Business Focus")
                   or r.get("Category / Status") or "")
            out.append(dict(ticker=t, name=(r.get("Company Name") or "").strip(),
                            sector=(r.get("Sector") or "").strip(), biz=biz.strip(),
                            listed_yield=(r.get("Dividend Yield (%)") or "").strip(),
                            src=label))
    return out


def main():
    rows = (read_list(os.path.join(HERE, "_input", "list_largecap.csv"), "large")
            + read_list(os.path.join(HERE, "_input", "list_midcap.csv"), "mid")
            + read_list(os.path.join(HERE, "_input", "list_smallcap.csv"), "small"))
    print(f"raw rows: {len(rows)}")

    merged = {}
    for r in rows:
        m = merged.setdefault(r["ticker"], dict(r, srcs=set()))
        m["srcs"].add(r["src"])
        if not m.get("biz") and r["biz"]:
            m["biz"] = r["biz"]
    print(f"unique tickers: {len(merged)}  (dupes removed: {len(rows)-len(merged)})")

    tick = M.cached_json("company_tickers.json", "https://www.sec.gov/files/company_tickers.json")
    sec = {str(v["ticker"]).upper(): (int(v["cik_str"]), v.get("title", "")) for v in tick.values()}
    hurdle = max((M.dgs30_asof(TODAY) or 4.0) / 100.0, 0.04)
    print(f"SEC filers indexed: {len(sec)}   hurdle: {hurdle:.4f}")

    out = []
    for i, (t, m) in enumerate(sorted(merged.items())):
        rec = dict(ticker=t, name=m["name"], sector=m["sector"], biz=m["biz"],
                   lists="+".join(sorted(m["srcs"])), listed_yield=m["listed_yield"],
                   status="", note="", cap_m="", statute_yield="", worst5_ni_m="",
                   div_yield="", div_cagr_5y="", div_cut_5y="", payout_worst5="")

        if t in ALREADY:
            rec["status"], rec["note"] = "ALREADY", ALREADY[t]
            out.append(rec); continue
        # SEC writes class shares with a hyphen (BF-B), the lists use a dot (BF.B).
        key = next((k for k in (t, t.replace(".", "-"), t.replace("-", ".")) if k in sec), None)
        if key is None:
            rec["status"] = "NOT_AN_SEC_FILER"
            rec["note"] = "no CIK for this ticker - fabricated, foreign-only, or stale symbol"
            out.append(rec); continue
        cik, sec_name = sec[key]
        rec["sec_name"] = sec_name

        blob = f"{m['sector']} {m['biz']} {m['name']}"
        if FIN_PAT.search(blob):
            rec["status"] = "EXCL_FINANCIAL"
            rec["note"] = "operator directive 2026-08-30; E2-50 stroke-of-a-pen, E3-29 leverage"
            out.append(rec); continue
        if UTIL_PAT.search(blob):
            rec["status"] = "EXCL_REGULATED"
            rec["note"] = "E3-03 criterion 3: a rate-regulated utility is not a franchise by definition"
            out.append(rec); continue

        closes, adjs, splits = chart_robust(t, i)
        if closes is None:
            rec["status"] = "NO_PRICE_DATA"
            rec["note"] = "chart fetch failed 3x - verify listing status by hand"
            out.append(rec); continue
        last = max(closes) if closes else None
        if not last or last < PREVMONTH:
            rec["status"] = "DEAD_OR_ACQUIRED"
            rec["note"] = f"no close since {last or 'never'} - taken private, merged, or renamed"
            out.append(rec); continue

        try:
            facts = M.cached_json(f"facts_{cik}.json",
                                  f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",
                                  sleep=0.12)
        except Exception:
            rec["status"] = "NO_XBRL"; rec["note"] = "companyfacts unavailable"
            out.append(rec); continue

        ni = M.ni_series(facts, TODAY)
        ends = sorted(ni)[-5:]
        sh = M.shares_asof(facts, TODAY)
        px = closes.get(AMONTH) or closes[last]
        # STALE-SHARES GUARD, added 2026-08-31 after the LEVI run. companyfacts drops
        # DIMENSIONED facts, so a dual-class filer's dei share tag can stop updating at
        # the moment it added a second class - LEVI's last usable value was its pre-IPO,
        # pre-split cover count from 2019-01-30, understating the cap 10.23x. A pre-IPO
        # split has no market split event either, so the split guard cannot save it.
        if sh:
            _meas = sh[0]
            _months = (TODAY.year - _meas.year) * 12 + (TODAY.month - _meas.month)
            if _months > 18:
                rec["status"] = "SHARES_STALE"
                rec["note"] = (f"share count dated {_meas} ({_months} months old) - "
                               f"likely a dual-class filer whose dei tag went dimensional; "
                               f"read the latest filed cover before using any cap or yield")
                out.append(rec); continue
        if sh and px:
            meas, shares = sh
            factor = 1.0
            for sd, f in splits:
                if sd > meas:
                    factor *= f
            cap = px * shares * factor
            rec["cap_m"] = round(cap / 1e6)
            if len(ends) == 5:
                worst5 = min(ni[e] for e in ends)
                rec["worst5_ni_m"] = round(worst5 / 1e6, 1)
                rec["statute_yield"] = round(worst5 / cap, 4)
        else:
            cap = None

        # dividends from the same cached chart
        divs = []
        p = os.path.join(M.CACHE, f"chart_{t}.json")
        try:
            d = json.load(open(p, encoding="utf-8"))
            ev = (d["chart"]["result"][0].get("events", {}) or {}).get("dividends", {}) or {}
            divs = sorted((e["date"], e["amount"]) for e in ev.values())
        except Exception:
            pass
        now = time.time()
        def ttm(off): return sum(a for ts, a in divs if now - (off+1)*365*86400 < ts <= now - off*365*86400)
        d0, d5 = ttm(0), ttm(5)
        if d0 > 0 and px:
            rec["div_yield"] = round(d0 / px, 4)
            rec["div_cagr_5y"] = round((d0/d5)**0.2 - 1, 4) if d5 > 0 else ""
            rec["div_cut_5y"] = any(ttm(k) < 0.95*ttm(k+1) for k in range(0, 5))
            if rec["worst5_ni_m"] and cap:
                eps_w = (rec["worst5_ni_m"]*1e6) / (cap/px)
                rec["payout_worst5"] = round(d0/eps_w, 2) if eps_w > 0 else ""

        if MLP_PAT.search(f"{m['name']} {m['biz']}"):
            rec["status"] = "FLAG_MLP"
            rec["note"] = "K-1 risk in a taxable account - verify tax election (SGU issues a 1099)"
        elif REIT_PAT.search(f"{m['name']} {m['biz']}"):
            rec["status"] = "TIER2_REIT"
            rec["note"] = "sector method required before the yield means anything"
        else:
            rec["status"] = "READ"
        out.append(rec)
        if (i+1) % 25 == 0:
            print(f"  {i+1}/{len(merged)} processed")

    dest = os.path.join(HERE, f"{TODAY} PREPPED LIST.csv")
    cols = ["ticker","name","sector","biz","lists","status","note","cap_m","statute_yield",
            "worst5_ni_m","div_yield","div_cagr_5y","div_cut_5y","payout_worst5","listed_yield"]
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader(); w.writerows(out)

    from collections import Counter
    print("\n== TRIAGE ==")
    for k, v in Counter(r["status"] for r in out).most_common():
        print(f"  {k:18s} {v}")
    reads = [r for r in out if r["status"] == "READ"]
    reads.sort(key=lambda r: -(r["statute_yield"] or 0) if isinstance(r["statute_yield"], float) else 0)
    print(f"\n== READ tier, by statute yield ({len(reads)}) ==")
    for r in reads[:40]:
        sy = f"{r['statute_yield']:.1%}" if isinstance(r["statute_yield"], float) else "  n/a"
        dy = f"{r['div_yield']:.1%}" if isinstance(r["div_yield"], float) else "  -  "
        cg = f"{r['div_cagr_5y']:+.0%}" if isinstance(r["div_cagr_5y"], float) else "  - "
        cap = f"{r['cap_m']:>7}" if r["cap_m"] != "" else "      ?"
        print(f"  {r['ticker']:6s} cap{cap}M  statute {sy:>6s}  div {dy:>6s} cagr {cg:>5s} "
              f"cut={str(r['div_cut_5y'])[:5]:5s} {r['name'][:34]}")
    print(f"\nWROTE {dest}")


if __name__ == "__main__":
    main()
