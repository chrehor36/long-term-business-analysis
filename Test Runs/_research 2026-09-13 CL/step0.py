"""Step 0 for CL: sovereign, price, splits, CIK, submissions, deals. Fetch and print only."""
import sys, os, json
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources as S

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def p(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

for c in ("USD", "EUR", "JPY"):
    try:
        p("SOVEREIGN", c, S.sovereign(c))
    except Exception as e:
        p("SOVEREIGN", c, "FAILED", e)

cik, title = S.cik_for("CL")
p("CIK", cik, title)
p("PRICE", S.price("CL"))
# the 2026-09-11 close from the chart series, not the meta field
r = S._chart("CL")
import datetime as dt
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
for t, c in list(zip(ts, q["close"]))[-6:]:
    p("CLOSE", dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"), c)
rmax = S._chart("CL", rng="max", max_age_h=24 * 7)
p("SPLITS", json.dumps((rmax.get("events") or {}).get("splits") or {}))

txt = S._get(f"https://data.sec.gov/submissions/CIK{cik}.json", S.SEC_UA, f"sub_{cik}.json", max_age_h=1)
open(os.path.join(HERE, "submissions.json"), "w", encoding="utf-8").write(txt)
sub = json.loads(txt)
p("NAME", sub.get("name"), "FYE", sub.get("fiscalYearEnd"), "SIC", sub.get("sic"), sub.get("sicDescription"))
rec = sub["filings"]["recent"]
for i, f in enumerate(rec["form"]):
    if f in ("10-K", "10-Q", "DEF 14A", "8-K", "8-K/A", "10-K/A", "S-4", "425", "DEFM14A", "SC TO-T", "SC 14D9") and rec["filingDate"][i] >= "2021-01-01":
        p("FILING", f, rec["filingDate"][i], rec["reportDate"][i], rec["accessionNumber"][i], rec["items"][i], rec["primaryDocument"][i])
p("DEAL_FILINGS", S.deal_filings(cik))
p("DEAL_NOTE", S.deal_note(cik))
open(os.path.join(HERE, "step0_out.txt"), "w", encoding="utf-8").write("\n".join(out))
