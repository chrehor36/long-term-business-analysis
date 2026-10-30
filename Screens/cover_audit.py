#!/usr/bin/env python3
"""Audit: filed cover count vs whatever the screen's share count returns.

COMPUTATION - NOT A CLEARANCE. This decides which names need their cap rebuilt by hand
before any run spends tokens on them. It concludes nothing about any business.
"""
import io, os, sys, json, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"c:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
sys.path.insert(0, os.path.join(ROOT, "Screens"))
sys.argv = [sys.argv[0]]
import bt17_microcap as M
import floor_screen as F
import cover_shares as C

NAMES = """L WTM MKL BRK-B BRK-A HHH GHC BAM BN
PINS CVX ANF PEP MCD HAS TGT DRI CNR COKE TSCO ACLS CRM BMI ORLY DAL EFX QLYS EAT SBUX
CERT CMG AAPL CTAS GRMN CGNX AMAT PLPC KLAC WMT GOOGL DELL MSFT LRCX AVGO SHOP PAY CORT
TXN SNPS INOD MRVL ELF AMD CRWD PLTR SWK ARM CALX BE MU ROKU ORCL BA ACMR ALKT INTC
ACVA FLNC DKS""".split()

tm = C.ticker_map()
rows = []
for i, t in enumerate(NAMES):
    key = next((k for k in (t.upper(), t.upper().replace(".", "-"),
                            t.upper().replace("-", ".")) if k in tm), None)
    if key is None:
        rows.append((t, None, None, "NOT AN SEC REGISTRANT"))
        continue
    cik, name = tm[key]
    # what the screen would use
    p = os.path.join(M.CACHE, f"facts_{cik}.json")
    screen = None
    if os.path.exists(p):
        try:
            so = F.shares_outstanding(json.load(open(p, encoding="utf-8")))
            screen = so[1] if so else None
        except Exception:
            pass
    # what the cover says
    try:
        f = C.latest_periodic(cik)
        counts, _ = C.cover_counts(cik, f[3])
        cover = sum(n for _, n in counts) if counts else None
        nclass = len(counts)
    except Exception as e:
        rows.append((t, screen, None, f"cover fetch failed: {str(e)[:40]}"))
        continue
    note = f"{nclass} class{'es' if nclass != 1 else ''}"
    rows.append((t, screen, cover, note))
    time.sleep(0.15)

print(f"{'tick':8s}{'screen':>16s}{'cover sum':>16s}{'ratio':>9s}  note")
bad = []
for t, s, c, note in rows:
    r = (c / s) if (s and c) else None
    mark = ""
    if r and (r > 1.02 or r < 0.98):
        mark = "  <<< DISAGREES"
        bad.append((t, s, c, r))
    if s is None and c:
        mark = "  <<< SCREEN HAS NO COUNT"
        bad.append((t, s, c, None))
    print(f"{t:8s}{(s or 0):>16,.0f}{(c or 0):>16,.0f}"
          f"{(f'{r:.2f}x' if r else '-'):>9s}  {note}{mark}")

print(f"\n{len(bad)} of {len(rows)} need the cap rebuilt by hand:")
for t, s, c, r in sorted(bad, key=lambda x: -(x[3] or 0)):
    print(f"   {t:8s} screen {(s or 0):>16,.0f}  cover {(c or 0):>16,.0f}  "
          f"{(f'{r:.2f}x' if r else 'screen blank')}")
