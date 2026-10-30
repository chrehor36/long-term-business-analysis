import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
R = r"C:\Users\chreh\OneDrive\Documents\BRK"
H = os.path.join(R, "Test Runs", "_research 2026-09-19 KO")

# 3. narrative fold into the reading list (appended at the end, as every recent run did)
p = os.path.join(R, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
t = open(p, encoding="utf-8").read()
assert "## UPDATE 2026-09-19 - KO:" not in t
fold = open(os.path.join(H, "_fold.md"), encoding="utf-8").read()
t = t.rstrip("\n") + "\n" + fold
open(p, "w", encoding="utf-8").write(t)
print("reading list folded")

# 4a. alerts.json: two bands (a gate-clearer)
p = os.path.join(R, "tools", "alerts.json")
d = json.load(open(p, encoding="utf-8"))
ids = {a["id"] for a in d["alerts"]}
assert "KO-rerun-band" not in ids and "KO-floor-band" not in ids
d["alerts"].append({
    "id": "KO-rerun-band", "ticker": "KO", "currency": "USD", "op": "<=", "threshold": 63, "active": True,
    "label": "KO at/below $63: the E4-28 floor is met only if 2019-25's 6.1%/yr growth in operating income before other operating charges is granted in perpetuity on $10.0bn of owner earnings (adjusted five-year mean, capex end). Q1-Q4 all IN on 2026-09-19 (Q2 WIDE with two limits: energy ceded to Monster, bottler share of price rises); Q5 quit on at $88.25 (yield 2.63% vs 5.34%; the price needs 7.2% forever). Prompt for a FULL v4.1 re-run in which that growth is re-tested before it is spent, not a purchase. VOID if a Q2 falsifier has fired: two consecutive negative worldwide unit-case years outside a pandemic; North America price/mix negative in a year when commodity costs fell; North America unit cases down 3% or more two years running. Re-read on the Eleventh Circuit IRS decision (about $20bn and 6% of owner earnings at stake). Source: Test Runs/2026-09-19 Run - KO Coca-Cola.md"})
d["alerts"].append({
    "id": "KO-floor-band", "ticker": "KO", "currency": "USD", "op": "<=", "threshold": 41, "active": True,
    "label": "KO at/below $41: the E4-28 floor is met on the owner-earnings record itself (adjusted owner earnings +4.1%/yr 2019-25, $10.0bn base). A ping is a prompt to re-run the gates, never an action; recompute both bands at the rate of the day and at the FY2026 10-K (expected February 2027). Owner earnings as filed are about $2bn a year lower because the $6.0bn IRS deposit (2024) and the $6.1bn fairlife milestone (2025) sit inside operating cash. Source: Test Runs/2026-09-19 Run - KO Coca-Cola.md"})
json.dump(d, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(p, "a", encoding="utf-8").write("\n")
print("alerts armed")

# 4b. PORTFOLIO.md watch row, appended after the last row of the opportunity table
p = os.path.join(R, "PORTFOLIO.md")
t = open(p, encoding="utf-8").read()
assert "| — | KO |" not in t
lines = t.split("\n")
i = [k for k, l in enumerate(lines) if l.startswith("| — | SPGI |")][0]
row = ("| — | KO | 2.63 % default; 2.06–3.01 % on every construction (2026-09-19) | 5.34 % USD | **−2.71 points; below the bond on every construction, "
       "including the most generous** | **RUN DONE** (`Test Runs/2026-09-19 Run - KO Coca-Cola.md`): **Q1–Q4 all IN — Q2 WIDE with two limits** (energy ceded to "
       "Monster, 21% owned; the bottler keeps part of each price rise): North America price/mix about +49 % over 2021-25 on level cases, segment operating income "
       "+52 %, against PepsiCo's falling beverage volume; operating income on the tangible capital that earns it 67–89 %. Owner earnings about **$10.0bn** "
       "(adjusted five-year, capex end; range $7.8–11.4bn) once the $6.0bn IRS deposit (2024) and $6.1bn fairlife milestone (2025) are taken out of operating "
       "cash. Q5: expectancy about 7–9 % vs ~10 %; the price needs **7.2 %/yr forever** against a filed 4–6 %; value roughly **$40–$70** against **$88.25**. "
       "**NOT RANKED — watch-list only; no position held and none proposed.** Bands armed $63 (floor met only with 6.1 % granted forever) and $41 (floor met on "
       "the owner-earnings record), each a prompt for a full re-run, not a purchase. Watch items: the Eleventh Circuit IRS decision (about $20bn and +3.8 points "
       "of tax rate at worst); US unit cases (named death: stagnation, proposed shape #22 THE HABIT); the except-for gap between comparable and GAAP [E2-57] "
       "and the pay plan built on it [E4-27]; buybacks near value [E5-08](2) |")
lines.insert(i + 1, row)
open(p, "w", encoding="utf-8").write("\n".join(lines))
print("portfolio row added")

# 5. survival shape #22, proposed
p = os.path.join(R, "Screens", "SURVIVAL SHAPES - index.md")
t = open(p, encoding="utf-8").read()
assert "| 22 |" not in t
lines = t.split("\n")
i = [k for k, l in enumerate(lines) if l.startswith("| 21 |")][0]
lines.insert(i + 1, "| 22 | **The habit** *(proposed, pending the operator)* | KO (2026-09-19) | the franchise is a consumer habit priced above its cost for decades; medicine, taxes and labels can weaken the habit market by market; the business lives, the volume in the richest markets drifts down, and the growth left arrives in currencies that lose value against the owner's | |")
t = "\n".join(lines)
old = "**All nine are listed so briefs count correctly; none is settled.**"
assert t.count(old) == 1
t = t.replace(old, "KO proposed THE HABIT (2026-09-19), arguing it is neither #11 nor #19: the gains are not competed away or taken by a retailer (Coca-Cola raised US prices about 49% in 2021-25 on level cases and kept them), and the drinker, not the shelf, holds the choice; the risk is that the choice itself weakens under weight-loss drugs, sugar taxes and labels (named in the filer's Item 1A) while the case growth left is in markets whose currencies cut operating income 8-12% a year in 2022-25. The IRS transfer-pricing case is carried as a feature (the home sovereign re-pricing the royalty), not as the shape. **All ten are listed so briefs count correctly; none is settled.**")
open(p, "w", encoding="utf-8").write(t)
print("shape 22 added")
