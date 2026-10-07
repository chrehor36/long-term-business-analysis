#!/usr/bin/env python3
"""Competitor row: return on unleveraged net tangible operating assets.
Same definition applied identically to every company (the AEO/NKE/ULTA metric).

NTOA = total assets - cash - short-term investments - goodwill - other intangibles
       - operating-lease ROU assets
       - (total current liabilities - current debt - current operating-lease liabilities)
Lease-inclusive variant adds the ROU asset back to the denominator.
Return = operating income / denominator.
"""
import json, os, sys

OUT = os.path.dirname(os.path.abspath(__file__))

TAGS = {
 "assets":      ["Assets"],
 "cash":        ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
 "sti":         ["ShortTermInvestments", "MarketableSecuritiesCurrent"],
 "goodwill":    ["Goodwill"],
 "intang":      ["FiniteLivedIntangibleAssetsNet", "IntangibleAssetsNetExcludingGoodwill"],
 "rou":         ["OperatingLeaseRightOfUseAsset"],
 "curliab":     ["LiabilitiesCurrent"],
 "curdebt":     ["LongTermDebtCurrent", "DebtCurrent", "CommercialPaper"],
 "curlease":    ["OperatingLeaseLiabilityCurrent"],
 "equity":      ["StockholdersEquity"],
 "ltdebt":      ["LongTermDebtNoncurrent"],
 "invent":      ["InventoryNet"],
 "ap":          ["AccountsPayableCurrent"],
}
FLOW = {
 "revenue":  ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"],
 "opinc":    ["OperatingIncomeLoss"],
 "gp":       ["GrossProfit"],
 "ocf":      ["NetCashProvidedByUsedInOperatingActivities"],
 "capex":    ["PaymentsToAcquirePropertyPlantAndEquipment"],
 "da":       ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
              "DepreciationAndAmortization"],
 "sbc":      ["ShareBasedCompensation"],
 "buyback":  ["PaymentsForRepurchaseOfCommonStock"],
 "netinc":   ["NetIncomeLoss"],
}


def load(cik):
    with open(os.path.join(OUT, f"facts_{cik}.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def pick(facts, tags, end, duration):
    """Latest-accession value for a tag list at a given period end."""
    for t in tags:
        best = None
        for taxo in ("us-gaap", "srt"):
            node = facts["facts"].get(taxo, {}).get(t)
            if not node:
                continue
            for u, items in node["units"].items():
                if u != "USD":
                    continue
                for it in items:
                    if it["end"] != end:
                        continue
                    if it.get("form") not in ("10-K", "10-K/A"):
                        continue
                    isdur = "start" in it
                    if isdur != duration:
                        continue
                    if duration:
                        from datetime import date as D
                        d = (D.fromisoformat(it["end"]) - D.fromisoformat(it["start"])).days
                        if not (300 <= d <= 400):
                            continue
                    if best is None or it["accn"] > best[1]:
                        best = (it["val"], it["accn"])
        if best:
            return best[0]
    return None


def fy_ends(facts):
    ends = set()
    for it in facts["facts"]["us-gaap"].get("Assets", {}).get("units", {}).get("USD", []):
        if it.get("form") in ("10-K", "10-K/A") and it.get("fp") == "FY":
            ends.add(it["end"])
    return sorted(ends)


def row(cik, name, end):
    f = load(cik)
    v = {k: pick(f, t, end, False) for k, t in TAGS.items()}
    w = {k: pick(f, t, end, True) for k, t in FLOW.items()}
    z = lambda x: x or 0
    # GPC does not tag an OperatingIncomeLoss subtotal (its income statement presents no
    # operating-income line). Construct it the same way its own statement does:
    # gross profit less SG&A. Flagged wherever used.
    if not w["opinc"]:
        sga = pick(f, ["SellingGeneralAndAdministrativeExpense"], end, True)
        if w["gp"] and sga:
            w["opinc"] = w["gp"] - sga
            print(f"  [note] operating income CONSTRUCTED as gross profit - SG&A "
                  f"({w['gp']:,.0f} - {sga:,.0f}); filer tags no operating-income subtotal")
    ntoa = (z(v["assets"]) - z(v["cash"]) - z(v["sti"]) - z(v["goodwill"]) - z(v["intang"])
            - z(v["rou"]) - (z(v["curliab"]) - z(v["curdebt"]) - z(v["curlease"])))
    ntoa_l = ntoa + z(v["rou"])
    op = z(w["opinc"])
    print(f"\n### {name}  FY end {end}")
    print(f"  revenue        {z(w['revenue']):>15,.0f}")
    print(f"  gross profit   {z(w['gp']):>15,.0f}   GM {z(w['gp'])/z(w['revenue'])*100:6.2f}%"
          if w["revenue"] else "  gross profit   n/a")
    print(f"  operating inc  {op:>15,.0f}   OM {op/z(w['revenue'])*100:6.2f}%"
          if w["revenue"] else "")
    print(f"  total assets   {z(v['assets']):>15,.0f}")
    print(f"  cash+STI       {z(v['cash'])+z(v['sti']):>15,.0f}")
    print(f"  goodwill+intan {z(v['goodwill'])+z(v['intang']):>15,.0f}")
    print(f"  op-lease ROU   {z(v['rou']):>15,.0f}")
    print(f"  cur liab       {z(v['curliab']):>15,.0f}  (cur debt {z(v['curdebt']):,.0f}, "
          f"cur lease {z(v['curlease']):,.0f})")
    print(f"  EQUITY         {z(v['equity']):>15,.0f}   {'<-- NEGATIVE' if z(v['equity'])<0 else ''}")
    print(f"  LT debt        {z(v['ltdebt']):>15,.0f}")
    print(f"  inventory      {z(v['invent']):>15,.0f}   AP {z(v['ap']):>13,.0f}   "
          f"AP/inv {z(v['ap'])/z(v['invent'])*100:6.1f}%" if v["invent"] else "")
    print(f"  NTOA (ex-lease){ntoa:>15,.0f}   ** RETURN {op/ntoa*100:7.2f}% **" if ntoa else "")
    print(f"  NTOA (lease in){ntoa_l:>15,.0f}   ** RETURN {op/ntoa_l*100:7.2f}% **" if ntoa_l else "")
    oe = z(w["ocf"]) - z(w["sbc"]) - z(w["capex"])
    print(f"  OCF {z(w['ocf']):>13,.0f}  capex {z(w['capex']):>12,.0f}  D&A {z(w['da']):>12,.0f}"
          f"  cx/D&A {z(w['capex'])/z(w['da']):.2f}" if w["da"] else "")
    print(f"  OE (OCF-SBC-capex) {oe:>12,.0f}   = {oe/z(w['revenue'])*100:5.2f}% of revenue"
          if w["revenue"] else "")
    print(f"  buybacks       {z(w['buyback']):>15,.0f}")
    return {"name": name, "end": end, "rev": z(w["revenue"]), "op": op,
            "ntoa": ntoa, "ntoa_l": ntoa_l, "eq": z(v["equity"]), "oe": oe,
            "gp": z(w["gp"])}


if __name__ == "__main__":
    peers = [("0000898173", "O'REILLY (ORLY)"),
             ("0000866787", "AUTOZONE (AZO)"),
             ("0001158449", "ADVANCE AUTO PARTS (AAP)"),
             ("0000040987", "GENUINE PARTS (GPC)")]
    if len(sys.argv) > 1 and sys.argv[1] == "ends":
        for cik, n in peers:
            print(n, fy_ends(load(cik))[-8:])
        sys.exit()
    res = []
    for cik, n in peers:
        ends = fy_ends(load(cik))
        latest = ends[-1]
        five = [e for e in ends if e <= f"{int(latest[:4])-5}-12-31"]
        res.append(row(cik, n, latest))
        if five:
            row(cik, n + " [5y earlier]", five[-1])
    print("\n" + "=" * 78)
    print("SUMMARY — latest fiscal year, same metric, same definition")
    print("=" * 78)
    print(f"{'company':<26}{'revenue':>13}{'op mgn':>8}{'GM':>8}{'RONTOA':>9}{'lease-in':>9}"
          f"{'equity':>13}")
    for r in res:
        print(f"{r['name']:<26}{r['rev']/1e6:>13,.0f}{r['op']/r['rev']*100:>7.2f}%"
              f"{r['gp']/r['rev']*100:>7.2f}%"
              f"{r['op']/r['ntoa']*100:>8.1f}%{r['op']/r['ntoa_l']*100:>8.1f}%"
              f"{r['eq']/1e6:>13,.0f}")
