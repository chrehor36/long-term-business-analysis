#!/usr/bin/env python3
"""ORLY return on unleveraged net tangible operating assets, multi-year [E2-01, E2-43]."""
import json, os
from peers import pick, load

cik = "0000898173"
f = load(cik)
ends = [f"{y}-12-31" for y in range(2016, 2026)]
print(f"{'FY':>6}{'op inc':>11}{'assets':>11}{'cash':>8}{'GW+int':>8}{'ROU':>8}"
      f"{'curliab':>10}{'curlease':>9}{'NTOA':>11}{'RETURN':>9}{'lease-in':>9}")
prev = None
for e in ends:
    z = lambda v: v or 0
    op = z(pick(f, ["OperatingIncomeLoss"], e, True))
    A = z(pick(f, ["Assets"], e, False))
    C = z(pick(f, ["CashAndCashEquivalentsAtCarryingValue"], e, False))
    G = z(pick(f, ["Goodwill"], e, False)) + z(pick(f, ["FiniteLivedIntangibleAssetsNet"], e, False))
    R = z(pick(f, ["OperatingLeaseRightOfUseAsset"], e, False))
    L = z(pick(f, ["LiabilitiesCurrent"], e, False))
    CL = z(pick(f, ["OperatingLeaseLiabilityCurrent"], e, False))
    CD = z(pick(f, ["LongTermDebtCurrent", "DebtCurrent"], e, False))
    n = A - C - G - R - (L - CD - CL)
    nl = n + R
    print(f"{e[:4]:>6}{op/1e6:>11,.0f}{A/1e6:>11,.0f}{C/1e6:>8,.0f}{G/1e6:>8,.0f}{R/1e6:>8,.0f}"
          f"{L/1e6:>10,.0f}{CL/1e6:>9,.0f}{n/1e6:>11,.0f}{op/n*100:>8.1f}%{op/nl*100:>8.1f}%"
          if n else f"{e[:4]} incomplete")
