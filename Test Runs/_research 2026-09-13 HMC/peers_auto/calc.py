"""Margin arithmetic for peers_auto.md. numerator / denominator, two decimals. Figures typed
from the filings as transcribed in peers_auto.md; nothing is fetched here."""
import sys

DATA = {
    # Toyota, JPY millions, 20-F Note "Segment information", Automotive column
    "TM automotive (Operating income / Total sales revenues)": [
        ("FY3/2022", 2284290, 28605738),
        ("FY3/2023", 2180637, 33820000),
        ("FY3/2024", 4621475, 41266204),
        ("FY3/2025", 3940278, 43199865),
        ("FY3/2026", 2777049, 45417703),
    ],
    "TM automotive (Operating income / Revenues from external customers)": [
        ("FY3/2022", 2284290, 28531993),
        ("FY3/2023", 2180637, 33776870),
        ("FY3/2024", 4621475, 41080731),
        ("FY3/2025", 3940278, 42996299),
        ("FY3/2026", 2777049, 45201924),
    ],
}

EXTRA = {}
try:
    from calc_extra import EXTRA  # later companies appended in a separate module
except ImportError:
    pass
DATA.update(EXTRA)


def fmt(x):
    return f"({abs(x):,.2f})%" if x < 0 else f"{x:,.2f}%"


for name, rows in DATA.items():
    if len(sys.argv) > 1 and sys.argv[1].lower() not in name.lower():
        continue
    print(name)
    tn = td = 0
    for yr, n, d in rows:
        print(f"  {yr}: {n:,} / {d:,} = {fmt(100 * n / d)}")
        tn += n
        td += d
    print(f"  pooled: {tn:,} / {td:,} = {fmt(100 * tn / td)}")
