import sys, os, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\Screens")
import floor_screen as F
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
def gp(facts):
    g = F.annual(facts, ["GrossProfit"])
    return g
def row(tk, facts):
    ocf = F.ocf_continuing(facts)[0]; sbc = F.sbc_annual(facts); cap = F.capital_acquired(facts)[0]
    rev = F.annual(facts, F.REV_TAGS); da = F.da_annual(facts); g = gp(facts)
    ys = sorted(ocf)[-5:]
    print(f"== {tk}  years {[str(y) for y in ys]}")
    tot_oe = tot_rev = tot_gp = 0
    for y in ys:
        oe = ocf[y] - sbc.get(y, float('nan')) - cap.get(y, 0)
        tot_oe += oe; tot_rev += rev.get(y, float('nan')); tot_gp += g.get(y, float('nan'))
        print(f"  {y} rev {rev.get(y,0)/1e6:9.1f} gp {g.get(y,float('nan'))/1e6:9.1f} ocf {ocf[y]/1e6:8.1f} sbc {sbc.get(y,float('nan'))/1e6:7.1f} capital {cap.get(y,0)/1e6:6.1f} OE {oe/1e6:8.1f} OE/rev {oe/rev.get(y,1)*100:6.1f}% OE/gp {oe/g.get(y,float('nan'))*100:6.1f}% sbc/ocf {sbc.get(y,0)/ocf[y]*100 if ocf[y] else float('nan'):6.1f}%")
    r0, r1 = rev.get(ys[0]), rev.get(ys[-1])
    print(f"  5y OE/rev {tot_oe/tot_rev*100:.1f}%  5y OE/gp {tot_oe/tot_gp*100:.1f}%  rev CAGR {((r1/r0)**(1/4)-1)*100:.1f}%  (first {ys[0]} to last {ys[-1]}, 4 steps)")
for tk in ["PUBM","MGNI","TTD","CRTO","TBLA","APPS"]:
    p = os.path.join(H, "..", "companyfacts.json") if tk=="PUBM" else os.path.join(H, f"{tk}_companyfacts.json")
    try: row(tk, json.load(open(p)))
    except Exception as e: print(tk, "ERR", repr(e))
