#!/usr/bin/env python3
"""BT-17 Universe B: the micro-cap panel.

Pre-registration: Framework/v4/BT-17 - PREREGISTRATION - ... .md, committed b853dcf
BEFORE this script produced a number. The rules there govern; nothing here re-decides.

Selection: SEC company_tickers.json in SHA-256(cik-string) order (no tunable seed).
Eligible at anchor: (a) five annual NIs from 10-Ks filed <= anchor (earliest-filed value
per fiscal end - the v3b rule); (b) house-rule market cap in [50M, 300M]; (c) price
series exists at the anchor month (a later start = recycled ticker, refused); class/unit
suffix tickers excluded. First 100 qualifying form the universe; examination cap 2,000.
Gate (frozen v3b statute): worst5_NI / cap >= max(DGS30(anchor), 4%); worst5<0 fails.
Windows: 1y (context) / 3y / 5y forward, monthly adjclose ratios only.

Usage: python bt17_microcap.py 2018-06-30
"""
import csv, hashlib, json, os, sys, time, urllib.request, urllib.error
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
BT = os.path.dirname(HERE)
CACHE = os.path.join(BT, "bt17_cache")
os.makedirs(CACHE, exist_ok=True)

ANCHOR = date.fromisoformat(sys.argv[1] if len(sys.argv) > 1 else "2018-06-30")
AMONTH = f"{ANCHOR.year}-{ANCHOR.month:02d}"
CAP_LO, CAP_HI = 50e6, 300e6
TARGET, EXAM_CAP = 100, 2000
UA = {"User-Agent": "BRK framework research chrehor36@gmail.com"}
YHOSTS = ["query1", "query2"]


def fetch(url, tries=4, base_sleep=1.5):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):
                raise
            time.sleep(base_sleep * (2 ** k))
        except Exception:
            time.sleep(base_sleep * (2 ** k))
    raise RuntimeError(f"fetch failed: {url}")


def cached_json(path, url, sleep=0.0):
    p = os.path.join(CACHE, path)
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    data = fetch(url)
    open(p, "wb").write(data)
    if sleep:
        time.sleep(sleep)
    return json.loads(data)


def dgs30_asof(anchor):
    p = os.path.join(CACHE, "dgs30.csv")
    if not os.path.exists(p):
        open(p, "wb").write(fetch("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30"))
    best = None
    with open(p, encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row or row[0] in ("DATE", "observation_date"):
                continue
            try:
                d = date.fromisoformat(row[0]); v = float(row[1])
            except ValueError:
                continue
            if d <= anchor:
                best = v
    return best


def ni_series(facts, anchor):
    """{fiscal_end: worst-filed NI} per v3b: 10-K annual, earliest filed per end, filed<=anchor."""
    gaap = facts.get("facts", {}).get("us-gaap", {})
    by_end = {}
    for tag in ("NetIncomeLoss", "ProfitLoss"):
        for x in gaap.get(tag, {}).get("units", {}).get("USD", []):
            if x.get("form") not in ("10-K", "10-K/A"):
                continue
            s, e, f = x.get("start"), x.get("end"), x.get("filed")
            if not (s and e and f):
                continue
            sd, ed, fd = date.fromisoformat(s), date.fromisoformat(e), date.fromisoformat(f)
            if not (300 <= (ed - sd).days <= 380) or fd > anchor:
                continue
            prev = by_end.get(ed)
            if prev is None or fd < prev[1]:
                by_end[ed] = (x["val"], fd)
    return {e: v for e, (v, _) in by_end.items()}


def shares_asof(facts, anchor):
    best = None  # (end, val)
    pools = [facts.get("facts", {}).get("dei", {}).get("EntityCommonStockSharesOutstanding", {})]
    gaap = facts.get("facts", {}).get("us-gaap", {})
    for t in ("CommonStockSharesOutstanding", "CommonStockSharesIssued"):
        pools.append(gaap.get(t, {}))
    for pool in pools:
        for x in pool.get("units", {}).get("shares", []):
            e, f = x.get("end"), x.get("filed")
            if not (e and f):
                continue
            ed, fd = date.fromisoformat(e), date.fromisoformat(f)
            if fd > anchor or ed > anchor or not x.get("val"):
                continue
            if best is None or ed > best[0]:
                best = (ed, float(x["val"]))
        if best:
            return best
    return None


def chart(ticker, i):
    host = YHOSTS[i % 2]
    u = (f"https://{host}.finance.yahoo.com/v8/finance/chart/{ticker}"
         f"?range=max&interval=1mo&events=div%2Csplit")
    d = cached_json(f"chart_{ticker}.json", u, sleep=0.6)
    r = d["chart"]["result"][0]
    ts = r.get("timestamp") or []
    q = r["indicators"]["quote"][0].get("close") or []
    adj = (r["indicators"].get("adjclose") or [{}])[0].get("adjclose") or []
    months, closes, adjs = {}, {}, {}
    for t, c, a in zip(ts, q, adj):
        m = time.strftime("%Y-%m", time.gmtime(t))
        if c is not None:
            closes[m] = c
        if a is not None:
            adjs[m] = a
        months[m] = True
    splits = []
    for ev in (r.get("events", {}).get("splits", {}) or {}).values():
        sd = date.fromtimestamp(ev["date"])
        num, den = float(ev.get("numerator") or 0), float(ev.get("denominator") or 1)
        if num and den:
            splits.append((sd, num / den))
    return closes, adjs, splits


def shift_month(m, k):
    y, mo = int(m[:4]), int(m[5:7])
    mo += k
    y += (mo - 1) // 12
    mo = (mo - 1) % 12 + 1
    return f"{y}-{mo:02d}"


def main():
    hurdle = max((dgs30_asof(ANCHOR) or 4.0) / 100.0, 0.04)
    print(f"BT-17 microcap  anchor={ANCHOR}  hurdle={hurdle:.4f}")
    tick = cached_json("company_tickers.json", "https://www.sec.gov/files/company_tickers.json")
    cands = sorted(tick.values(), key=lambda v: hashlib.sha256(str(v["cik_str"]).encode()).hexdigest())

    rows, examined, yfetch = [], 0, 0
    skip = dict(suffix=0, nofacts=0, ni5=0, noshares=0, nochart=0, recycled=0, capout=0)
    for c in cands:
        if len(rows) >= TARGET or examined >= EXAM_CAP:
            break
        examined += 1
        t = str(c["ticker"]).upper()
        if "-" in t or (len(t) == 5 and t[-1] in "WU"):
            skip["suffix"] += 1
            continue
        cik = int(c["cik_str"])
        try:
            facts = cached_json(f"facts_{cik}.json",
                                f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",
                                sleep=0.12)
        except Exception:
            skip["nofacts"] += 1
            continue
        ni = ni_series(facts, ANCHOR)
        ends = sorted(ni)[-5:]
        if len(ends) < 5:
            skip["ni5"] += 1
            continue
        sh = shares_asof(facts, ANCHOR)
        if not sh:
            skip["noshares"] += 1
            continue
        try:
            closes, adjs, splits = chart(t, yfetch)
            yfetch += 1
        except Exception:
            skip["nochart"] += 1
            continue
        if AMONTH not in closes:
            first = min(closes) if closes else None
            if first and first > AMONTH:
                skip["recycled"] += 1
            else:
                skip["nochart"] += 1
            continue
        meas, shares = sh
        # House rule: cap = close(anchor) x shares(measurement) x ALL splits after
        # measurement -- full history through today, NOT capped at the anchor,
        # because Yahoo's close series is back-adjusted for later splits. Capping
        # at the anchor was the bug that put CMG (50:1 in 2024) and SMCI (10:1)
        # into the first, WITHDRAWN version of this panel.
        factor = 1.0
        for sd, f in splits:
            if sd > meas:
                factor *= f
        cap = closes[AMONTH] * shares * factor
        if not (CAP_LO <= cap <= CAP_HI):
            skip["capout"] += 1
            continue
        worst5 = min(ni[e] for e in ends)
        yld = worst5 / cap
        passed = worst5 > 0 and yld >= hurdle
        rets = {}
        for lbl, k in (("r1", 12), ("r3", 36), ("r5", 60)):
            exit_m = shift_month(AMONTH, k)
            if AMONTH in adjs and exit_m in adjs and adjs[AMONTH]:
                rets[lbl] = adjs[exit_m] / adjs[AMONTH] - 1.0
            else:
                rets[lbl] = None  # delisted / no data - its own class
        rows.append(dict(ticker=t, cik=cik, cap=round(cap), worst5_ni=worst5,
                         yld=round(yld, 5), passed=passed,
                         r1=rets["r1"], r3=rets["r3"], r5=rets["r5"]))
        if len(rows) % 10 == 0:
            print(f"  {len(rows)} found / {examined} examined")

    out = os.path.join(BT, f"2026-08-28 BT-17 Microcap {ANCHOR}.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"universe={len(rows)} examined={examined} skips={skip}")

    for grp_name, grp in (("PASSED", [r for r in rows if r["passed"]]),
                          ("REJECTED", [r for r in rows if not r["passed"]])):
        print(f"-- {grp_name}: n={len(grp)}")
        for lbl in ("r1", "r3", "r5"):
            vals = [r[lbl] for r in grp if r[lbl] is not None]
            nod = len(grp) - len(vals)
            if not vals:
                print(f"   {lbl}: all no-data ({nod})")
                continue
            losses = [v for v in vals if v < 0]
            mean = sum(vals) / len(vals)
            lf_ex = len(losses) / len(vals)
            lf_in = (len(losses) + nod) / len(grp)
            depth = sum(losses) / len(losses) if losses else 0.0
            print(f"   {lbl}: n={len(vals)} nodata={nod} mean={mean:+.1%} "
                  f"lossfreq_ex={lf_ex:.1%} lossfreq_incl_nodata={lf_in:.1%} depth={depth:+.1%}")
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
