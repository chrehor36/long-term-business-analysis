#!/usr/bin/env python3
"""ANF screen-row reproduction + full annual series, from cached SEC companyfacts.
COMPUTATION - NOT A CLEARANCE (operator rule 3). Transcription and screening only [E3-27].
"""
import json, os, sys
from datetime import date

ROOT = r"c:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "Screens"))
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
import floor_screen as FS  # noqa: E402

CIK = 1018840  # ABERCROMBIE & FITCH CO /DE/
p = os.path.join(ROOT, "Backtests", "bt17_cache", f"facts_{CIK}.json")
print("cache file:", p, "mtime:", date.fromtimestamp(os.path.getmtime(p)))
facts = json.load(open(p, encoding="utf-8"))

ocf = FS.annual(facts, FS.OCF_TAGS)
sbc = FS.annual(facts, FS.SBC_TAGS)
capx, lease = FS.capital_acquired(facts)
da = FS.da_annual(facts)
rev = FS.annual(facts, FS.REV_TAGS)
ni = FS.annual(facts, ["NetIncomeLoss"])
acq = FS.annual(facts, FS.ACQ_TAGS)

years = sorted(set(ocf) | set(rev))
print(f"\n{'fiscal end':>12s} {'revenue':>10s} {'net inc':>9s} {'OCF':>9s} {'SBC':>7s} "
      f"{'capex':>8s} {'D&A':>8s} {'OE(capex)':>10s} {'OE(D&A)':>9s}")
for e in years:
    def g(d):
        v = d.get(e)
        return f"{v/1e6:>9,.1f}" if v is not None else "        -"
    oc = ocf.get(e); cx = capx.get(e); dd = da.get(e); sb = sbc.get(e, 0.0)
    oe_c = f"{(oc - sb - abs(cx))/1e6:>10,.1f}" if (oc is not None and cx is not None) else "         -"
    oe_d = f"{(oc - sb - abs(dd))/1e6:>9,.1f}" if (oc is not None and dd is not None) else "        -"
    print(f"{str(e):>12s} {g(rev)} {g(ni)} {g(ocf)} {g(sbc)} {g(capx)} {g(da)} {oe_c} {oe_d}")

oe = FS.owner_earnings(facts)
print("\nowner_earnings() constructions ($M):",
      {k: round(v/1e6, 1) for k, v in oe.items()} if isinstance(oe, dict) else oe)
if isinstance(oe, dict):
    vals = list(oe.values())
    bottom, top = min(vals), max(vals)
    cap = 6555e6
    print(f"bottom {bottom/1e6:,.1f}M  top {top/1e6:,.1f}M  spread {(top-bottom)/bottom:.1%}")
    print(f"yield_bottom on screen cap $6,555M: {bottom/cap:.2%}   growth_required {0.10 - bottom/cap:.2%}")

# level_shift and best_year_dependence on the OE(capex) series, all filed years
series = []
for e in sorted(ocf):
    if e in capx:
        series.append(ocf[e] - sbc.get(e, 0.0) - abs(capx[e]))
print("\nOE(capex) series, all filed years ($M):", [round(v/1e6) for v in series])
print("level_shift:", FS.level_shift(series))
print("best_year_dependence:", FS.best_year_dependence(series))

# share count + capex/DA ratio
sh = FS.shares_outstanding(facts)
print("\nshares_outstanding (dei):", sh)
last5 = sorted(set(capx) & set(da))[-5:]
print("capex/D&A by year:", {str(e): round(abs(capx[e])/abs(da[e]), 2) for e in last5})
print("acquisition line by year ($M):", {str(e): round(v/1e6, 1) for e, v in sorted(acq.items())})
print("finance-lease additions:", {str(e): round(v/1e6, 1) for e, v in sorted(lease.items())} if lease else "none tagged")
