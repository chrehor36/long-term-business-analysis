#!/usr/bin/env python3
"""Local price alerts. Fetches quotes (aggregator, live quote only, flagged) and pops a
Windows message box when a threshold crosses. A firing is A PROMPT TO READ, never a
verdict: the framework's gates decide actions, this script only pings.

Config: tools/alerts.json. State (cooldown): tools/_cache/alerts_state.json.
Log: tools/_cache/alerts.log. Scheduled via Windows Task Scheduler ("BRK price alerts").
Run manually with --status to see current quotes vs thresholds without popups.
"""
import ctypes, json, os, sys, time, urllib.request
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "alerts.json")
CACHE = os.path.join(HERE, "_cache")
STATE = os.path.join(CACHE, "alerts_state.json")
LOG = os.path.join(CACHE, "alerts.log")

MB_ICONINFORMATION = 0x40
MB_SETFOREGROUND = 0x10000
MB_TOPMOST = 0x40000


def quote(ticker):
    """Try both hosts and two ranges before giving up.

    Hardened 2026-09-01: the log showed intermittent HTTP 400s (ASML.AS, COST, LOW),
    each of which silently skipped that ticker for the cycle. A watch the operator
    believes in but that is not actually checking is worse than no watch, so failures
    now retry across hosts and, if they persist, escalate to a BLIND WATCH warning.
    """
    last = None
    for host in ("query1", "query2"):
        for rng in ("1d", "5d"):
            try:
                url = (f"https://{host}.finance.yahoo.com/v8/finance/chart/{ticker}"
                       f"?range={rng}&interval=1d")
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                d = json.load(urllib.request.urlopen(req, timeout=30))
                m = d["chart"]["result"][0]["meta"]
                px = m.get("regularMarketPrice")
                if px:
                    return float(px)
            except Exception as e:            # noqa: BLE001 - any failure is a retry
                last = e
                time.sleep(1)
    raise RuntimeError(f"all quote attempts failed: {last}")


def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def main():
    status_only = "--status" in sys.argv
    cfg = load(CONFIG, None)
    if cfg is None:
        print("no alerts.json; nothing to do")
        return
    os.makedirs(CACHE, exist_ok=True)
    state = load(STATE, {})
    cooldown_s = cfg.get("cooldown_hours", 24) * 3600
    now = time.time()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    prices = {}
    for a in cfg["alerts"]:
        if not a.get("active"):
            continue
        t = a["ticker"]
        if t not in prices:
            try:
                prices[t] = quote(t)
                state[f"ok:{t}"] = now          # last time this ticker was really priced
            except Exception as e:
                with open(LOG, "a", encoding="utf-8") as f:
                    f.write(f"{stamp} FETCH-FAIL {t}: {e}\n")
                # BLIND-WATCH ESCALATION: a ticker that has not been successfully priced
                # in 24h is not being watched at all, and silence would read as "no
                # alert" rather than "no data". Say so on screen, once a day.
                last_ok = state.get(f"ok:{t}", 0)
                if last_ok and now - last_ok > 86400 and \
                        now - state.get(f"blind:{t}", 0) > 86400:
                    state[f"blind:{t}"] = now
                    hours = int((now - last_ok) / 3600)
                    if not status_only:
                        ctypes.windll.user32.MessageBoxW(
                            0, f"{t} has not been priced for {hours} hours.\n\n"
                               f"Its alert bands are NOT being checked. Verify the "
                               f"ticker and your connection.\n\nLast error: {e}",
                            "BRK alerts - BLIND WATCH",
                            MB_ICONINFORMATION | MB_SETFOREGROUND | MB_TOPMOST)
                continue
        px = prices[t]
        hit = (px <= a["threshold"]) if a["op"] == "<=" else (px >= a["threshold"])
        if status_only:
            print(f"{a['id']}: {t} = {px} {a.get('currency','')} "
                  f"vs {a['op']} {a['threshold']} -> {'HIT' if hit else 'no'}")
            continue
        if not hit:
            continue
        last = state.get(a["id"], 0)
        if now - last < cooldown_s:
            continue
        state[a["id"]] = now
        msg = (f"{a['label']}\n\nQuote: {px} {a.get('currency', '')} ({t}, "
               f"aggregator, {stamp}).\nThreshold: {a['op']} {a['threshold']}.")
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{stamp} FIRED {a['id']} at {px}\n")
        ctypes.windll.user32.MessageBoxW(
            0, msg, "BRK price alert - a prompt to read, never a verdict",
            MB_ICONINFORMATION | MB_SETFOREGROUND | MB_TOPMOST)

    if not status_only:
        with open(STATE, "w", encoding="utf-8") as f:
            json.dump(state, f)


if __name__ == "__main__":
    main()
