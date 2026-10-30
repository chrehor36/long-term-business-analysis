"""COMPUTATION - NOT A CLEARANCE. Yields and a staged engine at the ~10% floor [E4-28]; the engine casts no vote [E3-34]."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
oe = json.load(open(os.path.join(H, "oe_out.json")))
SH = 12539542899; PX = 140.5; CAP = PX * SH / 1e6  # NT$ millions
STAKES = 230720.8  # nine quoted stakes at 2026-09-11 quotes, NT$ millions (step0)
CAPX = CAP - STAKES
TWD, USD = 1.886, 5.35
bases = {"10-yr capex end": oe["windows"]["10-yr 2016-2025"]["oe_capex"], "10-yr judged end": oe["windows"]["10-yr 2016-2025"]["oe_judged"],
         "5-yr capex end": oe["windows"]["5-yr 2021-2025"]["oe_capex"], "5-yr judged end": oe["windows"]["5-yr 2021-2025"]["oe_judged"],
         "3-yr capex end": oe["windows"]["3-yr 2023-2025"]["oe_capex"], "3-yr judged end": oe["windows"]["3-yr 2023-2025"]["oe_judged"],
         "TTM capex end (display)": oe["rows"]["TTM"]["oe_capex"], "TTM judged end (display)": oe["rows"]["TTM"]["oe_judged"],
         "5-yr D&A end (INVALID, display)": oe["windows"]["5-yr 2021-2025"]["oe_da"]}
print(f"cap NT${CAP/1e3:,.1f}bn; stakes NT${STAKES/1e3:,.1f}bn; cap ex-stakes NT${CAPX/1e3:,.1f}bn; stakes per share NT${STAKES*1e6/SH:.1f}")
def engine(base, g, yrs=10, r=0.10, gt=0.03):
    v = 0; e = base
    for t in range(1, yrs + 1):
        e *= 1 + g; v += e / (1 + r) ** t
    return v + e * (1 + gt) / (r - gt) / (1 + r) ** yrs
out = {}
print("base | OE NT$bn | yield on cap | yield ex-stakes | vs TWD | vs USD | perpetual g for 10% (ex-stakes) | NT$/sh at 0%, 5%, 10% for 10y (+stakes)")
for n, b in bases.items():
    y1 = 100 * b / CAP; y2 = 100 * b / CAPX
    g = (0.10 * CAPX - b) / (CAPX + b) if b > 0 else None
    vals = [(engine(b, gg) + STAKES) * 1e6 / SH for gg in (0.0, 0.05, 0.10)]
    out[n] = dict(oe=b, y_cap=y1, y_ex=y2, g10=g, vals=vals)
    gs = f"{100*g:.1f}%" if g is not None else "n/a"
    print(f"{n:30s} {b/1e3:6.1f} | {y1:4.2f}% | {y2:4.2f}% | {y2-TWD:+.2f} | {y2-USD:+.2f} | {gs} | " + " / ".join(f"{v:,.0f}" for v in vals))
# what growth for a decade does the price need from each base (10y growth, then 3%)?
def need(base):
    lo, hi = -0.5, 1.5
    target = CAPX
    for _ in range(80):
        mid = (lo + hi) / 2
        if engine(base, mid) < target: lo = mid
        else: hi = mid
    return mid
for n, b in bases.items():
    if b > 0:
        out[n]["g_decade_needed"] = need(b)
        print(f"{n:30s} decade growth needed (then 3%, at 10%): {100*need(b):.1f}%")
json.dump(dict(cap=CAP, capx=CAPX, stakes=STAKES, out=out), open(os.path.join(H, "q5_out.json"), "w"), indent=1)
