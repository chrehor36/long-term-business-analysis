#!/usr/bin/env python3
"""Local alert: the v5 blind read is finished. Local only, per the standing rule.

The read cycle (Screens/_daily/_v5_read.ps1) writes Screens/_daily/V5 READ COMPLETE.md when every unit
of Screens/_daily/_v5_order.txt is done. This script watches for that file and alerts the operator once.

Two modes, written 2026-10-03 at the operator's "alert me when this is finished":
  python tools/v5_alert.py          poll every five minutes until the file exists, then alert and exit
                                    (launched in the background from the session, so its exit wakes it)
  python tools/v5_alert.py --once   check once; alert if the file exists and no alert has fired yet;
                                    then disable the Windows task BRK-v5-alert (the session-independent path)

The alert is a Windows message box plus a line in tools/_cache/v5_alert.log; the marker file
tools/_cache/v5_alert_fired.txt makes it fire once. It concludes nothing and writes nothing to the project.
"""
import ctypes, csv, os, subprocess, sys, time
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPLETE = os.path.join(ROOT, "Screens", "_daily", "V5 READ COMPLETE.md")
DONE = os.path.join(ROOT, "Screens", "_daily", "_v5_done.txt")
LEDGER_V5 = os.path.join(ROOT, "principle_ledger_v5.csv")
CACHE = os.path.join(ROOT, "tools", "_cache")
MARKER = os.path.join(CACHE, "v5_alert_fired.txt")
LOG = os.path.join(CACHE, "v5_alert.log")
TASK = "BRK-v5-alert"


def summary():
    units = rows = 0
    try:
        units = sum(1 for l in open(DONE, encoding="utf-8") if l.strip())
    except OSError:
        pass
    try:
        with open(LEDGER_V5, encoding="utf-8-sig", newline="") as f:
            rows = sum(1 for _ in csv.DictReader(f))
    except OSError:
        pass
    return units, rows


def fire():
    os.makedirs(CACHE, exist_ok=True)
    units, rows = summary()
    msg = ("THE v5 BLIND READ IS FINISHED\n\n"
           f"Units done: {units}. Rows in principle_ledger_v5.csv: {rows}.\n\n"
           "Next step (Framework/v5/PREREGISTRATION - v5 blind read and comparison.md):\n"
           "synthesis, with you present, from the v5 ledger only; then the reconciliation\n"
           "against v4.1 and the five pre-registered tests; then the ruling case.\n\n"
           "Read first: Framework\\v5\\READING REGISTER.md and Screens\\_daily\\V5 READ COMPLETE.md.\n"
           "v4.1 governs until you approve the ruling case. Wave 7 is still paused.")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} v5 read complete: {units} units, {rows} rows; alert fired\n")
    with open(MARKER, "w", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M}\n")
    ctypes.windll.user32.MessageBoxW(0, msg, "BRK - the v5 read is finished", 0x40 | 0x10000 | 0x40000)


def main():
    once = "--once" in sys.argv
    if once:
        if os.path.exists(COMPLETE) and not os.path.exists(MARKER):
            fire()
            subprocess.run(["schtasks", "/Change", "/TN", TASK, "/DISABLE"], capture_output=True)
        return 0
    while not os.path.exists(COMPLETE):
        time.sleep(300)
    if not os.path.exists(MARKER):
        fire()
    print(f"v5 read complete: {summary()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
