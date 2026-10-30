"""Append one line to Screens/_daily/OVERNIGHT LOG.md in the existing format (CRLF endings, as the file uses)."""
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
P = os.path.join(ROOT, "Screens", "_daily", "OVERNIGHT LOG.md")
LINE = ("- 2026-09-13 10:50 EDT | UMC | Q1 IN / Q2 OUT (on the business, on [E3-03] criterion 2 and [E2-44](1); Q3-Q6 recorded, not governing; "
        "resumed from a session-limit cut before any file existed; FY2025 20-F not in companyfacts under the same agent prefix as FY2024; "
        "TWD 30-yr 1.886% re-fetched from TPEx (TSM's recorded endpoint path 404, corrected) and the CBC auction for the MOF; 12,539,542,899 shares "
        "as filed after the 2026-08-10 capital reduction, treasury excluded; ADR 1:5 at parity; quoted stakes ~NT$231bn kept out of owner earnings; "
        "customers' filings name mature-node substitutes and filed ASP fell 7 of 11 years while SMIC and Hua Hong added 49% capacity; Q3 binary "
        "reads OUT on the 2020 US plea and 2022 Taiwan conviction, scope flagged; PASS-THROUGH with ADDRESS, no new shape) | NT$140.5 (2026-09-11 close) | PASS | 52044cf")
data = open(P, "rb").read()
if b"| UMC |" in data:
    raise SystemExit("UMC line already present")
if not data.endswith(b"\r\n"):
    data += b"\r\n"
data += LINE.encode("utf-8") + b"\r\n"
open(P, "wb").write(data)
print("appended")
