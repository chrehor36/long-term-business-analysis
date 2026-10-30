#!/usr/bin/env python3
"""Convert filed DOLLAR prior-year development into combined-ratio POINTS.

Only for the three filers that publish no points figure: WRB, RLI, ACGL.
Numerator and denominator are both taken from the filings named in
PEER_ROW_extension.md. Arithmetic only; no judgment (operator rule 8).

Sign convention here: POSITIVE = FAVOURABLE (reduces the combined ratio).
"""
DATA = {
    # name: [(year, favourable_development, net_premiums_earned, units)]
    "WRB": [(2021, 6647, 8106031), (2022, -36405, 9561429), (2023, -18899, 10400687),
            (2024, 4432, 11548485), (2025, 3246, 12446938)],          # $000
    "RLI": [(2021, 125463, 980903), (2022, 122579, 1144436), (2023, 108547, 1294306),
            (2024, 95309, 1526406), (2025, 98978, 1614346)],          # $000
    "ACGL": [(2021, 355, 8082), (2022, 769, 9679), (2023, 538, 12440),
             (2024, 507, 15100), (2025, 600, 17065)],                 # $mm
}

if __name__ == "__main__":
    for name, rows in DATA.items():
        print(name)
        for y, d, n in rows:
            print(f"  {y}  {d:>12,}  /  {n:>12,}  =  {100.0*d/n:6.2f} pts favourable")
