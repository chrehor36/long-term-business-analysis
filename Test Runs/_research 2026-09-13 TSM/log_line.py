"""Append one line to Screens/_daily/OVERNIGHT LOG.md in the existing format (CRLF endings, as the file uses)."""
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
P = os.path.join(ROOT, "Screens", "_daily", "OVERNIGHT LOG.md")
LINE = ("- 2026-09-13 07:44 EDT | TSM | Q1 IN / Q2 OUT (on the business, on [E4-04]; Q3-Q6 recorded, not governing; "
        "FY2025 20-F not in companyfacts, read by hand; TWD 30-yr sovereign fetched by hand from the CBC auction for the MOF "
        "(1.814%, 2026-05-26) and the TPEx curve (1.886%, 2026-09-11), not added to sources.py; 25,932,364,992 shares derived "
        "from the dividend re-set 6-K; ADR 1:5 at a 10-14% premium, TWSE quote used; passes [E3-03] at the leading edge on "
        "customers' filings, fails [E2-44](2) and the rapid-change class on its own 20-F; 2023-meeting purchase-and-praise "
        "tension flagged; Q4 would be UNKNOWABLE on a twelfth shape THE ADDRESS) | NT$2,410 (2026-09-11 close) | PASS | f13e5e3")
data = open(P, "rb").read()
if b"| TSM |" in data:
    raise SystemExit("TSM line already present")
if not data.endswith(b"\r\n"):
    data += b"\r\n"
data += LINE.encode("utf-8") + b"\r\n"
open(P, "wb").write(data)
print("appended")
