"""LADDER ENGINE v3.1 - implements the 2026-08-26 rulings.

Ruling 7  (windage): realism at every input; conservatism spent ONCE at the MOS.
Ruling 5-A (MOS):    severity ladder, 10% base for WIDE + 4/4 inversions resolved.
Ruling 9  (anchor):  Book One = 5-yr MEDIAN OE tier, shutdown years excluded.
                     Trough tier still computed, reported at Gate 4 as survival input.
Ruling 10 (OE):      WC increment REQUIRED (avg annual cash effect, clean years);
                     capex is MAINTENANCE capex, disclosed as a band
                     (D&A floor .. total capex ceiling).
Ruling 4/4-A (rate): Aesop certainty spread. NOT WACC/beta.
Ruling 6  (output):  the price ladder plus three diagnostics, two verdicts.
"""
import json, statistics, urllib.request
from datetime import date

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}

# ---------- XBRL ------------------------------------------------------------
def facts(cik):
    p = f"facts_{cik}.json"
    try:
        return json.load(open(p))
    except FileNotFoundError:
        req = urllib.request.Request(
            f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers=UA)
        d = json.loads(urllib.request.urlopen(req).read())
        json.dump(d, open(p, "w"))
        return d

def annual(f, tag, forms=("10-K",)):
    us = f["facts"].get("us-gaap", {})
    if tag not in us:
        return {}
    units = us[tag]["units"]
    key = "USD" if "USD" in units else list(units)[0]
    out = {}
    for u in units[key]:
        if u.get("form") in forms and u.get("start") and u.get("end"):
            s, e = date.fromisoformat(u["start"]), date.fromisoformat(u["end"])
            if 340 <= (e - s).days <= 380:
                out[u["end"]] = u["val"] / 1e6
    return out

WC_ASSET_TAGS = ["IncreaseDecreaseInAccountsReceivable", "IncreaseDecreaseInInventories",
    "IncreaseDecreaseInIncomeTaxesReceivable", "IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets",
    "IncreaseDecreaseInOtherReceivables", "IncreaseDecreaseInPrepaidExpense"]
WC_LIAB_TAGS = ["IncreaseDecreaseInAccountsPayable",
    "IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities",
    "IncreaseDecreaseInOtherAccountsPayableAndAccruedLiabilities",
    "IncreaseDecreaseInAccountsPayableAndAccruedLiabilities",
    "IncreaseDecreaseInOperatingLeaseLiability", "IncreaseDecreaseInAccruedIncomeTaxesPayable",
    "IncreaseDecreaseInDeferredRevenueAndCustomerAdvancesAndDeposits",
    "IncreaseDecreaseInContractWithCustomerLiability"]
DA_TAGS = ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
           "DepreciationAndAmortization", "Depreciation"]
CAPX_TAGS = ["PaymentsToAcquirePropertyPlantAndEquipment",
             "PaymentsToAcquireProductiveAssets",
             "PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets"]

def first(f, tags):
    for t in tags:
        a = annual(f, t)
        if a:
            return t, a
    return None, {}

# ---------- valuation -------------------------------------------------------
def dcf(base, g1, tgr, r, yrs=10):
    pv, oe = 0.0, base
    for t in range(1, yrs + 1):
        g = g1 + (tgr - g1) * (t - 1) / (yrs - 1)
        oe *= (1 + g)
        pv += oe / (1 + r) ** t
    return pv + (oe * (1 + tgr) / (r - tgr)) / (1 + r) ** yrs

def solve(fn, target, lo, hi, n=200):
    for _ in range(n):
        m = (lo + hi) / 2
        if fn(m) < target: lo = m
        else: hi = m
    return (lo + hi) / 2

def mos_ruling5a(moat, unresolved=0, tight=False, permanent_loss=False):
    """Ruling 5-A severity ladder."""
    if permanent_loss:
        return 0.50, "permanent-loss risk floor (Grand Canyon case)"
    m, why = 0.10, ["10% base"]
    if moat.upper() == "NARROW": m += 0.10; why.append("+10 NARROW moat")
    if moat.upper() == "NONE":   m += 0.20; why.append("+20 no moat")
    if unresolved:               m += 0.10*unresolved; why.append(f"+{10*unresolved} unresolved inversion(s)")
    if tight:                    m += 0.10; why.append("+10 tight fortress")
    return min(m, 0.60), ", ".join(why)

SPREAD = {"WIDE": 3.0, "NARROW": 4.5, "NONE": 6.0}

def run(name, ticker, cik, price, shares, sov, moat, *,
        unresolved=0, tight=False, permanent_loss=False, caveat=0.0,
        shutdown_years=(), g1_guidance=None, oe_override=None, note=""):
    print("=" * 86)
    print(f"{name} ({ticker})   price ${price:,.2f}   shares {shares:,.1f}M"
          f"   cap ${price*shares/1000:,.1f}B   sovereign {sov:.2f}%")
    print("=" * 86)

    if oe_override:
        NI, DA, CX, WC = oe_override["NI"], oe_override["DA"], oe_override["CX"], oe_override["WC"]
        datanote = oe_override.get("note", "")
    else:
        f = facts(cik)
        NI = annual(f, "NetIncomeLoss")
        dat, DA = first(f, DA_TAGS)
        cxt, CX = first(f, CAPX_TAGS)
        wa = {t: annual(f, t) for t in WC_ASSET_TAGS}
        wl = {t: annual(f, t) for t in WC_LIAB_TAGS}
        yrs_all = sorted(set(NI) & set(DA) & set(CX))
        WC = {}
        for y in yrs_all:
            a = sum(v.get(y, 0) for v in wa.values())
            l = sum(v.get(y, 0) for v in wl.values())
            WC[y] = l - a                      # cash effect (+ = source)
        datanote = f"D&A tag {dat}; capex tag {cxt}"

    yrs = sorted(set(NI) & set(DA) & set(CX))[-6:]
    clean = [y for y in yrs if y[:4] not in shutdown_years and y not in shutdown_years]
    wc_req = -statistics.fmean([WC[y] for y in clean[-4:]]) if clean else 0.0

    print(f"\nGATE 4 - OWNER EARNINGS   [{datanote}]")
    print(f"  required WC increment (Ruling 10) = ${wc_req:,.0f}M/yr"
          f"  (avg of {len(clean[-4:])} clean yrs)")
    print(f"\n{'FY end':>12}{'NI':>9}{'D&A':>9}{'totCapx':>9}{'dWC$':>8}"
          f"{'OE@totcapx':>12}{'OE@D&A':>10}")
    tiers_lo, tiers_hi = {}, {}
    for y in yrs:
        lo = NI[y] + DA[y] - CX[y] - wc_req          # conservative end (total capex)
        hi = NI[y] + DA[y] - DA[y] - wc_req          # generous end (maint = D&A)
        tiers_lo[y], tiers_hi[y] = lo, hi
        flag = "  <-- EXCLUDED (shutdown)" if y not in clean else ""
        print(f"{y:>12}{NI[y]:>9,.0f}{DA[y]:>9,.0f}{CX[y]:>9,.0f}{WC[y]:>8,.0f}"
              f"{lo:>12,.0f}{hi:>10,.0f}{flag}")

    ct = [y for y in yrs if y in clean][-5:]
    med_lo = statistics.median([tiers_lo[y] for y in ct])
    med_hi = statistics.median([tiers_hi[y] for y in ct])
    trough_lo = min(tiers_lo[y] for y in yrs)
    print(f"\n  BOOK ONE ANCHOR (Ruling 9) = 5-yr MEDIAN of clean years:"
          f"  ${med_lo:,.0f}M .. ${med_hi:,.0f}M  (capex band)")
    print(f"  trough tier ${trough_lo:,.0f}M -> relocated to Gate 4 survival input, NOT the anchor")

    cap = price * shares
    print(f"\nBOOK ONE - THE STATUTE   hurdle {sov:.2f}%")
    for lbl, v in (("median @ total capex", med_lo), ("median @ D&A floor", med_hi)):
        y_ = v / cap * 100
        print(f"  {lbl:22s} ${v:>8,.0f}M -> {y_:5.2f}%  {'PASS' if y_ >= sov else 'FAIL'}"
              f"   (pass price ${v/(sov/100)/shares:,.2f})")

    r = (sov + SPREAD[moat.upper()] + caveat) / 100
    base_lo, base_hi = tiers_lo[ct[-1]], tiers_hi[ct[-1]]
    g_recent = None
    if len(ct) >= 2 and tiers_lo[ct[-2]] > 0:
        g_recent = tiers_lo[ct[-1]] / tiers_lo[ct[-2]] - 1
    g1 = min([g for g in (g_recent, g1_guidance) if g is not None] or [0.03])
    g1 = max(g1, -0.05)
    mos, mos_why = mos_ruling5a(moat, unresolved, tight, permanent_loss)

    print(f"\nBOOK TWO - AESOP SPREAD   rate = {sov:.2f}% + {SPREAD[moat.upper()]:.1f}% {moat.upper()}"
          f" + {caveat:.1f}% caveat = {r*100:.2f}%")
    print(f"  g1 = {g1*100:.2f}%  (recent OE growth "
          f"{g_recent*100:.1f}%" if g_recent is not None else "  g1 = n/a", end="")
    print(f"; guidance {g1_guidance*100:.1f}%)" if g1_guidance is not None else "; no guidance)")
    print(f"  MOS = {mos*100:.0f}%  [Ruling 5-A: {mos_why}]")

    out = {}
    for lbl, b in (("total-capex (conservative)", base_lo), ("D&A-floor (generous)", base_hi)):
        iv = dcf(b, g1, 0.025, r) / shares
        out[lbl] = iv
        print(f"\n  base OE ${b:,.0f}M  [{lbl}]")
        print(f"    FAIR    ${iv:8,.2f}   CHEAP ${iv*(1-mos):8,.2f}"
              f"   CURRENT ${price:8,.2f} = {price/iv:.2f}x fair")

    ivs = sorted(out.values())
    print(f"\n  IV BAND: ${ivs[0]:,.2f} .. ${ivs[-1]:,.2f}"
          f"   -> FAIR band, CHEAP band ${ivs[0]*(1-mos):,.2f} .. ${ivs[-1]*(1-mos):,.2f}")
    verdict_band = "BUY-ELIGIBLE" if price <= ivs[0]*(1-mos) else (
        "CHEAP only at the generous end - BAND STRADDLES, verdict WAIT per Ruling 10(3)"
        if price <= ivs[-1]*(1-mos) else "WAIT")
    print(f"  BAND VERDICT: {verdict_band}")

    ir = solve(lambda m: dcf(base_lo, g1, 0.025, m), cap, 0.0001, 1.0)
    ir2 = solve(lambda m: dcf(base_hi, g1, 0.025, m), cap, 0.0001, 1.0)
    gi = solve(lambda m: dcf(base_lo, m, 0.025, r), cap, -0.5, 1.0)
    print(f"\n  DIAGNOSTICS")
    print(f"    IRR at current price: {ir*100:.2f}% .. {ir2*100:.2f}% vs {sov:.2f}% sovereign"
          f"  = {ir*100-sov:+.2f} .. {ir2*100-sov:+.2f} pts of equity premium")
    print(f"    implied year-1 OE growth to justify price: {gi*100:.1f}%  (base assumes {g1*100:.2f}%)")
    if note: print(f"\n  {note}")
    return dict(fair_lo=ivs[0], fair_hi=ivs[-1], mos=mos, g1=g1, rate=r,
                med_lo=med_lo, med_hi=med_hi, trough=trough_lo, verdict=verdict_band)
