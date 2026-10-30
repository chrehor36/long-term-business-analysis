import sys, json, urllib.request, collections
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

# Segment data is DIMENSIONED, so companyfacts cannot see it. Use the frames-free route:
# the Financial Statement Data Sets are not available here, so read the R-files of the 10-K
# segment note instead. Simpler: use the company's own XBRL viewer JSON per filing.
CIK = "93556"
ACCS = {
    "FY2025": "0000093556-26-000009",
    "FY2024": "0000093556-25-000007",
    "FY2023": "0000093556-24-000032",
    "FY2022": "0000093556-23-000007",
    "FY2021": "0000093556-22-000015",
    "FY2019": "0000093556-20-000006",
}
for tag, acc in ACCS.items():
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/cgi-bin/viewer?action=view"  # not used
    try:
        txt = sources._get(f"https://data.sec.gov/api/xbrl/frames/us-gaap/Revenues/USD/CY2024.json",
                           sources.SEC_UA, "frames_test.json", max_age_h=999)
    except Exception as e:
        print("frames", e)
    break

# Fall back to reading the filed segment table out of the stripped text.
import re, os
RES = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 SWK"
for tag in ("10K_FY2019", "10K_FY2021", "10K_FY2022", "10K_FY2023", "10K_FY2024", "10K_FY2025"):
    p = os.path.join(RES, tag + ".txt")
    if not os.path.exists(p):
        continue
    t = open(p, encoding="utf-8").read()
    i = t.find("BUSINESS SEGMENTS")
    while i != -1:
        seg = t[i:i + 3000]
        if "Segment profit" in seg or "SEGMENT PROFIT" in seg.upper():
            print("=" * 30, tag, "at", i)
            print(re.sub(r"\n+", " | ", seg[:2600]))
            break
        i = t.find("BUSINESS SEGMENTS", i + 1)
