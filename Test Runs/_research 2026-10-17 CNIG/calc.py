# COMPUTATION, NOT A CLEARANCE. Owner cash and the Q7 range arithmetic for CNIG, from the filed cash-flow statements
# (10-K FY2017 0001582244-17-000114 [FY2016-17 cols], FY2018 0001582244-18-000068, FY2019 0001582244-19-000049,
#  FY2021 0001174947-21-001128 [FY2020-21 cols]) and the 10-Q of 2022-05-12 (0001174947-22-000671) for net debt.
# USD millions.
yrs  = [2017, 2018, 2019, 2020, 2021]
ocf  = [2.951887, 5.885984, 6.607439, 5.538357, 4.243425]
sbc  = [0.149510, 0.223783, 0.239481, 0.197180, 0.096211]   # "Stock issued for services and stock option expense"
capx = [6.447279, 7.832707, 6.628162, 8.672162, 10.988091]
acq  = [-0.724544, 0.0, 0.0, 1.893081, 0.0]                  # Pike purchase-price cash received 2017; Leatherstocking 2020
dna  = [2.143084+0.910163, 2.375500+0.509183, 2.499558+0.787116, None, 3.338769+0.681553]  # segment-note dep + amort
# FY2020 D&A from the FY2021 10-K segment note is read below
intr = [1.895170, 2.096626, 2.325642, 2.567064, 3.433379]    # interest expense incl. Series A/C preferred dividends
TAX = 0.23   # CONVENTION of this run: the filer's effective rate in FY2020-21 (23.1%, 23.3%)
import sys
dna[3] = float(sys.argv[1]) if len(sys.argv) > 1 else dna[3]
oe = [o - s - c - a for o, s, c, a in zip(ocf, sbc, capx, acq)]
oe_d = [o - s - d - a for o, s, d, a in zip(ocf, sbc, dna, acq)]
ae = [x + i * (1 - TAX) for x, i in zip(oe, intr)]
ae_d = [x + i * (1 - TAX) for x, i in zip(oe_d, intr)]
m = lambda v: sum(v) / len(v)
for y, a, b, c, d in zip(yrs, oe, oe_d, ae, ae_d):
    print(f"FY{y}  equity-only: all-spend {a:6.2f}  D&A-variant {b:6.2f}   all-equity: all-spend {c:6.2f}  D&A-variant {d:6.2f}")
print(f"mean  equity-only: all-spend {m(oe):6.2f}  D&A-variant {m(oe_d):6.2f}   all-equity: all-spend {m(ae):6.2f}  D&A-variant {m(ae_d):6.2f}")
gov = 0.0543
debt = 42.797116 + 6.776409 + 5.900000 + 9.191625 + 6.499772 + 4.498847 + 5.000000
cash = 0.333485 + 2.184478
nd = debt - cash
serB = 4.993375
sh = 3.083577
print(f"net debt 2022-03-31: borrowings+pref A/C/D {debt:.2f} less cash+securities {cash:.2f} = {nd:.2f}; Series B (temporary equity) {serB:.2f}; common shares {sh}M")
for lab, base in [("all-spend", m(ae)), ("D&A-variant", m(ae_d))]:
    v = base / gov
    print(f"no-growth value at {gov:.2%} ({lab}, all-equity): whole {v:7.2f}  per common share {(v - nd - serB)/sh:7.2f}")
    f = base / 0.10
    print(f"   at 10% (fair-price basis): whole {f:7.2f}  per share {(f - nd - serB)/sh:7.2f}")
for lab, base in [("all-spend", m(oe)), ("D&A-variant", m(oe_d))]:
    print(f"equity-only {lab}: no-growth at gov per share {(base/gov - serB)/sh:7.2f}; at 10% per share {(base/0.10 - serB)/sh:7.2f}")
# halves test for growth (rule b): first two vs last two years of all-equity all-spend series
print("halves (all-equity, all-spend): first", m(ae[:2]), "last", m(ae[3:]))
