import sys, os, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\Screens")
import floor_screen as F
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
def row(tk, facts, nyears=4):
    ocf = F.ocf_continuing(facts)[0]; sbc = F.sbc_annual(facts); cap = F.capital_acquired(facts)[0]
    rev = F.annual(facts, F.REV_TAGS)
    ys = [y for y in sorted(ocf) if y.year >= 2022 and y.year <= 2025][-nyears:]
    print(f"== {tk}  years {[str(y) for y in ys]}")
    tot_oe = tot_rev = 0
    for y in ys:
        oe = ocf[y] - sbc.get(y, float('nan')) - cap.get(y, 0)
        tot_oe += oe; tot_rev += rev.get(y, float('nan'))
        print(f"  {y} rev {rev.get(y,0)/1e6:9.1f} ocf {ocf[y]/1e6:8.1f} sbc {sbc.get(y,float('nan'))/1e6:7.1f} capital {cap.get(y,0)/1e6:6.1f} OE {oe/1e6:8.1f} OE/rev {oe/rev.get(y,1)*100:6.1f}%")
    r0, r1 = rev.get(ys[0]), rev.get(ys[-1])
    print(f"  {len(ys)}y OE/rev {tot_oe/tot_rev*100:.1f}%  rev CAGR {((r1/r0)**(1/(len(ys)-1))-1)*100:.1f}% ({ys[0]} to {ys[-1]})")
for tk in ["ZD","PPLI","NYT","TDAY","AREN","BMTM"]:
    try: row(tk, json.load(open(os.path.join(H, f"{tk}_companyfacts.json"))))
    except Exception as e: print(tk, "ERR", repr(e))
