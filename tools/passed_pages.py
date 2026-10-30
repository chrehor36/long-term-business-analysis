#!/usr/bin/env python3
"""PASSED PAGES - build `Passed Companies/`, one plain-English folder per business that passed.

    python tools/passed_pages.py [--no-quotes]

Written 2026-10-28 at the operator's word: "on the public github page i want a folder dedicated to each passed company
that is extremely easy to read and understand. as more pass this grows. it should prioritize price, and name and
explanations." A name is listed when it is on `Screens/V5 PASSERS - the alert list.md` (every business question
passed; OUT at Q7 on price, or IN) AND has a plain-English file `Passed Companies/_data/<TICKER>.json`, written at the
fold from the run file and nothing else. The fair price is read from `tools/alerts.json`, never from the data file, so a
re-run that moves the alert moves the page. The price is a live aggregator quote taken when this script runs (flagged
on every page as such). The pages conclude nothing the run did not: they restate the run's box in plain words.
A passer with no data file yet is listed at the foot of the index as "write-up pending", never silently dropped.
"""
import glob, json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Passed Companies")
DATA = os.path.join(OUT, "_data")
sys.path.insert(0, os.path.join(ROOT, "tools"))

SYM = {"USD": "$", "EUR": "€", "GBP": "£", "GBp": "", "SEK": "SEK ", "BRL": "R$", "JPY": "¥", "CAD": "C$",
       "CHF": "CHF ", "DKK": "DKK ", "HKD": "HK$", "AUD": "A$", "NOK": "NOK ", "INR": "₹", "KRW": "₩"}


def money(x, cur):
    if x is None:
        return "-"
    if x < 0:
        return "below zero"  # a central case whose costs exceed its cash; a minus price reads as a typo
    if cur == "GBp":
        return f"{x:,.0f}p"
    return f"{SYM.get(cur, cur + ' ')}{x:,.2f}"


def link(path):
    return path.replace(" ", "%20")


def folder(t, name):
    return re.sub(r'[<>:"/\\|?*]', "", f"{t} - {name}").strip()


def passers():
    """(ticker, company, run file, alert id) from the passers list, in its order."""
    s = open(os.path.join(ROOT, "Screens", "V5 PASSERS - the alert list.md"), encoding="utf-8").read()
    out = []
    for t, name, run, al in re.findall(r"^\| ([A-Z0-9.\-]+) \| (.*?) \| (.*?) \| (.*?) \|$", s, re.M):
        if t == "ticker":
            continue
        m = re.search(r"`(Test Runs/[^`]*\.md)`", run)
        f = m.group(1) if m else None
        if not f or not os.path.exists(os.path.join(ROOT, f)):  # a row reading "(see register)": the latest run file
            c = sorted(glob.glob(os.path.join(ROOT, "Test Runs", f"2026-*-* Run - {t} *.md")))
            f = os.path.relpath(c[-1], ROOT).replace(os.sep, "/") if c else None
        ids = re.findall(r"`([^`]+-v5-[^`]+)`", al)
        out.append((t, name.split(";")[0].strip(), f, ids[0] if ids else None))
    return out


def main():
    quotes = "--no-quotes" not in sys.argv
    if quotes:
        from price_alerts import quote
    alerts = {a["id"]: a for a in json.load(open(os.path.join(ROOT, "tools", "alerts.json"), encoding="utf-8"))["alerts"]}
    today = date.today().isoformat()
    rows, pending = [], []
    for t, company, run, aid in passers():
        p = os.path.join(DATA, f"{t}.json")
        if not os.path.exists(p):
            pending.append((t, company))
            continue
        d = json.load(open(p, encoding="utf-8"))
        a = alerts.get(aid) if aid else None
        fair = a["threshold"] if a and a.get("active") else None
        cur = (a or {}).get("currency") or d.get("currency", "USD")
        px = None
        if quotes and a:
            try:
                px = quote(a["ticker"])
            except Exception:  # noqa: BLE001 - a missing quote shows as a dash, never a guess
                px = None
        run = d.get("run_file") or run
        rows.append(dict(t=t, d=d, fair=fair, cur=cur, px=px, run=run,
                         ratio=(px / fair) if (px and fair and fair > 0) else None))

    rows.sort(key=lambda r: (r["ratio"] is None, r["ratio"] or 0))
    os.makedirs(OUT, exist_ok=True)
    for r in rows:
        write_page(r, today)
    write_index(rows, pending, today)
    print(f"{len(rows)} pages written, {len(pending)} write-ups pending: {', '.join(t for t, _ in pending)}")


def gap(r):
    if r["ratio"] is None:
        return "no fair price" if r["fair"] is None else "-"
    if r["ratio"] <= 1:
        return "**at or below fair price**"
    return f"{(1 - 1 / r['ratio']):.0%}"


def write_page(r, today):
    d, t, cur = r["d"], r["t"], r["cur"]
    lo, hi = d.get("value_low"), d.get("value_high")
    vcur = d.get("currency") or cur  # the run's range can be in the filing's currency (an ADR's local shares)
    worth = f"{money(lo, vcur)} to {money(hi, vcur)} a share" if lo is not None and hi is not None else "-"
    fair_line = money(r["fair"], cur) if r["fair"] is not None else (
        "none: " + d.get("no_fair_reason", "the run set no positive fair price"))
    L = [f"# {d['name']} ({t})", "",
         f"> **{d['headline']}**", "",
         "| | |", "|---|---|",
         f"| **Price** | {money(r['px'], cur)} ({today}, market quote) |",
         f"| **Our fair price** | {fair_line} |",
         f"| **Price would need to fall** | {gap(r)} |",
         f"| **What we think it is worth** | {worth} |",
         f"| **Date analysed** | {d.get('run_date', '-')} |",
         f"| **Type** | {'Regulated utility (returns capped by a regulator)' if d.get('utility') else 'Business'} |",
         "", "## What it does", "", d["what_it_does"], "",
         "## Why it passed", ""] + [f"- {b}" for b in d["why_it_passed"]] + [
         "", "## Why we are not buying at today's price", "", d["why_not_now"], "",
         "## What to watch", ""] + [f"- {b}" for b in d["watch"]] + [
         "", "## The full analysis", "",
         f"[{os.path.basename(r['run'])}]({link('../../' + r['run'])}), analysed {d.get('run_date', '')}.", "",
         "---",
         "*The fair price is the price at which this business would earn about 10% a year for an owner, on the "
         "analysis's own numbers. Reaching it starts a fresh analysis; it is never a buy signal by itself. "
         "Not investment advice.*", ""]
    path = os.path.join(OUT, folder(t, d["name"]))
    os.makedirs(path, exist_ok=True)
    open(os.path.join(path, "README.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))


def write_index(rows, pending, today):
    L = ["# Passed Companies", "",
         "Businesses that passed every quality question in the analysis: we can understand them, they have a "
         "lasting edge over competitors, the accounts are clean and management is honest. **None is a buy today: "
         "every one costs more than it is worth.** The list grows as more companies pass.", "",
         f"**Sorted by price: the closest to our fair price comes first.** Prices are market quotes from {today}.", "",
         "| # | Company | What it is | Price | Fair price | Needs to fall | Analysed |",
         "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        d = r["d"]
        name = f"[{d['name']}]({link(folder(r['t'], d['name']) + '/README.md')}) ({r['t']})"
        kind = d["what_short"] + (" *(utility)*" if d.get("utility") else "")
        L.append(f"| {i} | {name} | {kind} | {money(r['px'], r['cur'])} | "
                 f"{money(r['fair'], r['cur']) if r['fair'] is not None else 'none'} | {gap(r)} | "
                 f"{d.get('run_date', '-')} |")
    if pending:
        L += ["", "**Write-up pending** (passed; plain-English page not written yet): "
              + ", ".join(f"{c} ({t})" for t, c in pending) + "."]
    L += ["", "---",
          "*\"Fair price\" is the price at which the business would earn about 10% a year for an owner, on the "
          "analysis's own numbers. A utility's return is capped by its regulator, so its fair price sits far below "
          "today's price. Each page links to the full analysis. Not investment advice.*", ""]
    open(os.path.join(OUT, "README.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))


if __name__ == "__main__":
    main()
