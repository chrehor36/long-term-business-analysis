#!/usr/bin/env python3
"""DAILY FETCH — the standing watch on everything that can move a band.

The 30-minute price alert answers one question: has a price crossed a band? This answers
the other three, once a day:

  1. THE SOVEREIGN moved. Every band in this project is owner earnings against the long
     bond [E4-15 gravity]. PORTFOLIO.md's own maintenance rule re-derives ladders on a
     >50bp move, so a drift that large is reported loudly.
  2. A NEW FILING landed. The bands grow with owner earnings, and each run named its own
     catalyst - COST's 10-K (~Oct), SHW's FY2026 10-K (~Feb 2027), PNR's Q3 and the Taco
     close, HD's next 10-Q. A 10-K, 10-Q or 8-K from a watched name is the event that
     makes a band stale, and staleness is the failure mode a price alert cannot see.
  3. THE PRICE DRIFTED toward a band. Not a crossing - the distance, so the trend is
     visible before the pop-up.

Watched: the eleven businesses that cleared Q1-Q4 (COST, LOW, ITW, RPM, CSL, SHW, HD,
PNR, LOPE, OTIS, LSTR),
the sold-but-watched name (ASML), and the live holdings (HRB, MITSY, NCLTY, TBTC, V).

Writes a dated digest to Screens/_daily/ and pops a window ONLY when something material
happened: a new filing, a >50bp sovereign move, or a price within 10% of a band. Silence
means nothing changed, which is the normal and correct outcome [E5-13].
"""
import ctypes, json, os, sys, time, urllib.request
from datetime import date, datetime, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Screens", "_daily")
STATE = os.path.join(HERE, "_cache", "daily_state.json")
UA = {"User-Agent": "BRK framework research chrehor36@gmail.com"}
MB = 0x40 | 0x10000 | 0x40000

CLEARED = {"COST": "Costco", "LOW": "Lowes", "ITW": "Illinois Tool Works",
           "RPM": "RPM International", "CSL": "Carlisle", "SHW": "Sherwin-Williams",
           "HD": "Home Depot", "PNR": "Pentair",
           "LOPE": "Grand Canyon Education",
           "OTIS": "Otis Worldwide",
           "LSTR": "Landstar System"}
HOLDINGS = {"HRB": "H&R Block", "MITSY": "Mitsui", "NCLTY": "Nitori",
            "TBTC": "Table Trac", "V": "Visa"}
WATCHED_FORMS = ("10-K", "10-Q", "8-K", "DEF 14A", "20-F")


def get(url, timeout=30):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)


def load(p, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return d


def sovereign():
    """USD 30y from the issuing authority, with FRED as the fallback (it has been
    timing out; the Treasury daily par curve is the same series one rung higher)."""
    yr = date.today().year
    try:
        u = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
             f"daily-treasury-rates.csv/{yr}/all?type=daily_treasury_yield_curve"
             f"&field_tdr_date_value={yr}&page&_format=csv")
        rows = get(u).read().decode("utf-8").splitlines()
        hdr = rows[0].split(",")
        i = hdr.index('"30 Yr"') if '"30 Yr"' in hdr else hdr.index("30 Yr")
        cells = rows[1].split(",")
        return float(cells[i].strip('"')), cells[0].strip('"'), "US Treasury daily curve"
    except Exception:
        pass
    try:
        rows = get("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30").read() \
            .decode("utf-8").splitlines()
        for r in reversed(rows[1:]):
            d, v = r.split(",")[:2]
            if v not in (".", ""):
                return float(v), d, "FRED DGS30"
    except Exception:
        pass
    return None, None, None


def recent_filings(ticker, cik_map, since_iso):
    cik = cik_map.get(ticker)
    if not cik:
        return []
    try:
        sub = json.load(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    except Exception:
        return []
    r = sub.get("filings", {}).get("recent", {})
    out = []
    for form, filed, acc, doc in zip(r.get("form", []), r.get("filingDate", []),
                                     r.get("accessionNumber", []),
                                     r.get("primaryDocument", [])):
        if filed <= since_iso or not any(form.startswith(f) for f in WATCHED_FORMS):
            continue
        out.append((filed, form, acc, doc))
    return sorted(out, reverse=True)


def quote(t):
    for host in ("query1", "query2"):
        try:
            u = (f"https://{host}.finance.yahoo.com/v8/finance/chart/{t}"
                 "?range=1d&interval=1d")
            d = json.load(urllib.request.urlopen(
                urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30))
            px = d["chart"]["result"][0]["meta"].get("regularMarketPrice")
            if px:
                return float(px)
        except Exception:
            time.sleep(1)
    return None


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    st = load(STATE, {})
    today = date.today().isoformat()
    since = st.get("last_run", (date.today() - timedelta(days=3)).isoformat())
    alerts = load(os.path.join(HERE, "alerts.json"), {"alerts": []})
    bands = {}
    for a in alerts["alerts"]:
        bands.setdefault(a["ticker"], []).append((a["threshold"], a["id"]))

    lines = [f"# DAILY FETCH — {today}", "",
             f"Watching since {since}. Silence is the normal outcome [E5-13].", ""]
    material = []

    rate, rdate, rsrc = sovereign()
    prev = st.get("sovereign")
    lines.append("## The sovereign")
    if rate is None:
        lines.append("- **FETCH FAILED** on both the Treasury curve and FRED. "
                     "Bands cannot be re-derived today.")
        material.append("sovereign fetch failed")
    else:
        lines.append(f"- USD 30y **{rate:.2f}%** ({rdate}, {rsrc})")
        if prev:
            move = (rate - prev) * 100
            lines.append(f"- move since last run: **{move:+.0f}bp**")
            if abs(move) >= 50:
                lines.append("- **>50bp — PORTFOLIO.md's maintenance rule says re-derive "
                             "every ladder** [E4-15]")
                material.append(f"sovereign moved {move:+.0f}bp")
        st["sovereign"] = rate

    try:
        tick = json.load(get("https://www.sec.gov/files/company_tickers.json"))
        cik_map = {str(v["ticker"]).upper(): int(v["cik_str"]) for v in tick.values()}
    except Exception:
        cik_map = {}
    lines += ["", "## New filings from watched names"]
    any_filing = False
    for t, name in list(CLEARED.items()) + list(HOLDINGS.items()):
        for filed, form, acc, doc in recent_filings(t, cik_map, since):
            any_filing = True
            tag = "CLEARED" if t in CLEARED else "HOLDING"
            url = (f"https://www.sec.gov/Archives/edgar/data/{cik_map[t]}/"
                   f"{acc.replace('-', '')}/{doc}")
            lines.append(f"- **{t} ({name}, {tag}) {form}** filed {filed} — {url}")
            if form.startswith(("10-K", "10-Q", "20-F")):
                lines.append("  - **This can move the band.** Owner earnings are a "
                             "multi-year mean; a new annual or quarterly statement "
                             "re-derives it. Re-run the file before trusting the old band.")
                material.append(f"{t} filed a {form}")
    if not any_filing:
        lines.append("- none")

    lines += ["", "## Distance to bands"]
    for t in list(CLEARED) + ["ASML.AS"]:
        px = quote(t)
        if px is None:
            lines.append(f"- {t}: **no quote** (watch is blind for this name today)")
            material.append(f"{t} unpriced")
            continue
        near = None
        for thr, aid in sorted(bands.get(t, []), reverse=True):
            gap = (thr / px - 1) * 100
            lines.append(f"- {t} ${px:,.2f} vs {thr:,.2f} ({aid}): **{gap:+.0f}%**")
            if gap > -10 and near is None:
                near = (aid, gap)
        if near:
            material.append(f"{t} within 10% of {near[0]}")

    st["last_run"] = today
    json.dump(st, open(STATE, "w", encoding="utf-8"))
    path = os.path.join(OUT, f"{today} daily.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"\nWROTE {path}")

    if material and "--quiet" not in sys.argv:
        ctypes.windll.user32.MessageBoxW(
            0, "Something moved:\n\n- " + "\n- ".join(material[:8]) +
               f"\n\nDigest: {path}",
            "BRK daily fetch", MB)


if __name__ == "__main__":
    main()
