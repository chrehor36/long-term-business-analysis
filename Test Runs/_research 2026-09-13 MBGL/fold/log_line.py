P = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\_daily\OVERNIGHT LOG.md"
line = ("- 2026-09-13 11:45 EDT | MBGL | Q1 IN / Q2 UNKNOWABLE (the first in the register; Q3-Q6 recorded, not governing; the triage's "
        "'Mercedes, 20-F' label was wrong - the ticker is Mobility Global Inc., S&P Global's Mobility segment spun off 1-for-1 on 2026-07-01, "
        "widely held, nothing pending, $2.0bn notes paid to S&P Global; audited combined cash flows 2023-25 found in its own Form 10-12B/A, "
        "none earlier; USD 30-yr 5.35% from the US Treasury; 294,821,320 shares from the 10-Q cover; CARFAX 43-45% before acquired amortization "
        "against CarGurus and Cars.com, but AutoCheck (Experian, unsegmented, IR site blocked) is the one direct substitute and no filing "
        "measures it, dealer customers a frozen 'more than 40,000' and monthly report views 31M+ -> 28M+ while growth turned price-led; "
        "B2B and Listings NONE; owner earnings ~$280-350M standalone, yield 4.7-5.9%, ~4-5% growth needed for the floor; THE DOWRY proposed) "
        "| US$20.16 (2026-09-11 close) | PASS | bdcd1b3\n")
s = open(P, encoding="utf-8").read()
if "| MBGL |" in s:
    raise SystemExit("already logged")
if not s.endswith("\n"):
    s += "\n"
s += line
open(P, "w", encoding="utf-8").write(s)
print("ok")
