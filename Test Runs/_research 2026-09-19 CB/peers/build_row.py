# THE COMPETITOR ROW FOR CB, EXTENDED FROM Test Runs/_research 2026-09-02 MKL/competitor-row.md
# Two bases: (1) the REPORTED GAAP consolidated combined ratio, which that file already built and
# which is carried forward unchanged; (2) the CURRENT-ACCIDENT-YEAR combined ratio, built here by
# adding back each filer OWN published favourable prior-year development, which the MKL run
# showed is the decisive series for an insurer.
# Every figure is from a primary filing named in the comment. Nothing is estimated.
import sys, os, re, html, json
sys.path.insert(0, os.path.abspath("tools"))
import sources
sys.path.insert(0, os.path.abspath("Test Runs/_research 2026-09-19 CB/peers"))
from fetch_ppd import strip, D

# --- one more document: KNSL FY2022 10-K, for the 2021 PPD ratio ---
out = os.path.join(D, "KNSL_tenk_FY2022.txt")
if not os.path.exists(out):
    url = "https://www.sec.gov/Archives/edgar/data/1669162/000166916223000009/knsl-20221231.htm"
    raw = sources._get(url, headers=sources.SEC_UA, cache_name="peer22_KNSL", max_age_h=999)
    if not isinstance(raw, str):
        raw = raw.decode("utf-8", "replace")
    open(out, "w", encoding="utf-8").write(strip(raw))
print("KNSL FY2022 10-K acc 0001669162-23-000009 knsl-20221231.htm bytes %d" % os.path.getsize(out))
for l in open(out, encoding="utf-8"):
    if "prior year development" in l.lower() and "%" in l:
        print("  KNSL FY2022 10-K line:", l.strip()[:160])

P = print
# REPORTED GAAP consolidated combined ratio - carried from the MKL run competitor row, unchanged
REP = {
 "KNSL": (77.1, 78.5, 75.4, 76.4, 75.9),
 "ACGL": (85.2, 81.6, 79.3, 82.5, 82.8),
 "RLI":  (86.8, 84.4, 86.6, 86.2, 83.6),
 "WRB":  (89.6, 89.3, 89.7, 90.3, 90.7),
 "FFH":  (95.0, 94.7, 93.2, 92.7, 93.0),
 "MKL":  (90.0, 92.0, 98.8, 95.5, 94.6),
 "AXS":  (97.5, 95.8, 99.9, 92.3, 89.8),
 "CB":   (89.1, 87.6, 86.5, 86.6, 85.7),
}
# FAVOURABLE prior-year development in COMBINED RATIO POINTS (positive = favourable, i.e. it
# IMPROVED the reported ratio and must be added back to get the current accident year).
# ratio published by the filer -> "pub"; dollars/NPE computed here -> "calc" with the inputs shown.
PPD = {
 # CB: FY2025 10-K p.51 and FY2023/FY2021 10-K equivalents, published in points
 "CB":   dict(v=(2.8, 2.8, 1.9, 2.0, 2.5), how="pub", src="FY2025 10-K 0000896159-26-000005 p.51; FY2023 10-K 0000896159-24-000003; FY2021 10-K 0000896159-22-000005"),
 # KNSL: "Effect of prior year development" ratio, MD&A loss-ratio table
 "KNSL": dict(v=(5.5, 4.4, 3.2, 2.7, 3.9), how="pub", src="FY2025 10-K 0001669162-26-000015 (2025 3.9, 2024 2.7); FY2023 10-K 0001669162-24-000006 (2023 3.2, 2022 4.4); FY2022 10-K 0001669162-23-000009 (2022 4.5, 2021 5.5) - 2021 is on the SUPERSEDED denominator, the basis break the MKL row already flagged"),
 # AXS: "Prior year reserve development ratio", total company (negative in the filing = favourable)
 "AXS":  dict(v=(0.7, 0.5, -8.1, 0.5, 1.6), how="pub", src="FY2025 10-K 0001214816-26-000097 line 1335 (2025 (1.6), 2024 (0.5), 2023 8.1 ADVERSE); FY2023 10-K 0001214816-24-000024 line 1355 (2023 8.1, 2022 (0.5), 2021 (0.7))"),
 # MKL: "Prior accident years loss ratio", Markel Insurance segment
 "MKL":  dict(v=(None, None, 0.5, 5.6, 5.8), how="pub", src="FY2025 10-K 0001096343-26-000020 lines 1266-67; 2021-22 not published on this basis in that filing"),
 # ACGL: net favourable development in dollars, over net premiums earned
 "ACGL": dict(v=None, how="calc", d=(355, 769, 538, 507, 600), npe=(8082, 9679, 12440, 15100, 17065),
              src="FY2025 10-K 0000947484-26-000017 note (600/507/538 by segment and tail); FY2023 10-K 0000947484-24-000020 lines 3536/3551/3558 (538/769/355); NPE from each 10-K income statement"),
 # RLI: favourable development in dollars, over net premiums earned
 "RLI":  dict(v=None, how="calc", d=(None, 123, 109, 95, 99), npe=(None, 1144.4, 1294.3, 1526.4, 1614.3),
              src="FY2025 10-K 0001104659-26-018013 line 4009 (99/95); FY2023 10-K 0001558370-24-001599 line 3990 (109/123); NPE from each 10-K consolidated revenue table"),
 # WRB: net prior year development in dollars (2021 favourable, 2022-23 ADVERSE), over NPE
 "WRB":  dict(v=None, how="calc", d=(6.647, -36.405, -18.899, 4.432, 3.246), npe=(8106.0, 9561.4, 10400.7, 11548.5, 12446.9),
              src="FY2025 10-K 0000011544-26-000005 line 1016 (3,246 / 4,432 / (18,899) thousands); FY2023 10-K 0000011544-24-000005 line 987 ((18,899) / (36,405) / 6,647 thousands); NPE from each 10-K"),
 # FFH: IFRS 17. The combined ratio it publishes is undiscounted and P&C-only; it does not publish a
 # comparable current-accident-year separation, and the discounted IFRS 17 ratio is a different construct.
 "FFH":  dict(v=None, how="none", src="IFRS filer (40-F). No comparable current-accident-year / prior-year separation of the undiscounted combined ratio located in Exhibit 99.3."),
}
YRS = (2021, 2022, 2023, 2024, 2025)


def ppd_points(tk):
    d = PPD[tk]
    if d["how"] == "pub":
        return list(d["v"])
    if d["how"] == "calc":
        out = []
        for dd, nn in zip(d["d"], d["npe"]):
            out.append(None if (dd is None or nn is None) else dd / nn * 100.0)
        return out
    return [None] * 5


P("\n=== BASIS 1: REPORTED GAAP CONSOLIDATED COMBINED RATIO (carried from the MKL run, unchanged) ===")
P("| company | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |")
P("|---|---|---|---|---|---|---|")
rows = []
for tk in REP:
    m = sum(REP[tk]) / 5.0
    rows.append((m, tk))
for m, tk in sorted(rows):
    P("| %-5s | %s | **%.2f** |" % (tk, " | ".join("%.1f" % x for x in REP[tk]), m))

P("\n=== BASIS 2: CURRENT-ACCIDENT-YEAR COMBINED RATIO = reported + favourable prior-year development ===")
P("(a positive PPD number is FAVOURABLE development that improved the reported ratio)")
P("| company | 2021 | 2022 | 2023 | 2024 | 2025 | mean of the years available | years |")
P("|---|---|---|---|---|---|---|---|")
rows = []
for tk in REP:
    pp = ppd_points(tk)
    cay = []
    for r, p in zip(REP[tk], pp):
        cay.append(None if p is None else r + p)
    have = [c for c in cay if c is not None]
    if not have:
        rows.append((999.0, tk, cay, 0))
    else:
        rows.append((sum(have) / len(have), tk, cay, len(have)))
for m, tk, cay, n in sorted(rows):
    cells = " | ".join("n/a" if c is None else "%.1f" % c for c in cay)
    P("| %-5s | %s | %s | %d |" % (tk, cells, "NOT COMPARABLE" if n == 0 else "**%.2f**" % m, n))

P("\n=== THE PPD POINTS THEMSELVES, which is what the two bases differ by ===")
P("| company | 2021 | 2022 | 2023 | 2024 | 2025 | source |")
P("|---|---|---|---|---|---|---|")
for tk in ("CB", "KNSL", "ACGL", "RLI", "WRB", "AXS", "MKL", "FFH"):
    pp = ppd_points(tk)
    cells = " | ".join("n/a" if p is None else "%+.2f" % p for p in pp)
    P("| %-5s | %s | %s |" % (tk, cells, PPD[tk]["src"]))

P("\n=== RANK CHANGE BETWEEN THE TWO BASES (the point of doing this) ===")
rep_rank = [tk for m, tk in sorted((sum(REP[tk]) / 5.0, tk) for tk in REP)]
cay_list = []
for tk in REP:
    pp = ppd_points(tk)
    have = [r + p for r, p in zip(REP[tk], pp) if p is not None]
    if have:
        cay_list.append((sum(have) / len(have), tk))
cay_rank = [tk for m, tk in sorted(cay_list)]
P(" reported basis, best to worst: %s" % " > ".join(rep_rank))
P(" current-accident-year basis:   %s" % " > ".join(cay_rank))
