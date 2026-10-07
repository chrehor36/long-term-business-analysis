"""Guidance against outturn, from the quarterly earnings decks (6-K Ex. 99.2) and releases (Ex. 99.1).
Each deck's P&L table reads: current actual | current guidance | prior quarter | year-ago quarter.
Arithmetic and transcription only; prints what the decks say."""
import re, glob, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
rows = []
for fn in sorted(glob.glob(os.path.join(HERE, "q", "Q_*presentation*.txt"))):
    q = os.path.basename(fn)[2:8]
    t = re.sub(r"\s+", " ", open(fn, encoding="utf-8").read())
    def grab(label, n=40):
        m = re.search(re.escape(label) + r"(.{0,%d})" % n, t)
        return m.group(1).strip() if m else ""
    rev = grab("Net Revenue (US$ billions)", 60)
    gm = grab("Gross Margin", 60)
    om = grab("Operating Margin", 60)
    ship = grab('Shipment (Kpcs, 12"-equiv. Wafer)', 40)
    fx = grab("Average Exchange Rate--USD/NTD", 40)
    roe = grab("ROE", 30)
    outlook = grab("Future Outlook", 300)
    g_next = grab("Guidance Based on our current business outlook, management expects:", 260)
    rows.append({"q": q, "rev_usd": rev, "gm": gm, "om": om, "ship": ship, "fx": fx, "roe": roe,
                 "next_guidance": g_next, "outlook": outlook})
for r in rows:
    print(r["q"], "| REV", r["rev_usd"], "| GM", r["gm"], "| OM", r["om"], "| SHIP", r["ship"], "| FX", r["fx"], "| ROE", r["roe"])
    print("    NEXT:", r["next_guidance"][:230])
    print("    OUTLOOK:", r["outlook"][:200])
json.dump(rows, open(os.path.join(HERE, "guide_out.json"), "w"), indent=1)
