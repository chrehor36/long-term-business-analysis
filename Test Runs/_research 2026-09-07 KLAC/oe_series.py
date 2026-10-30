"""KLAC owner-earnings series, built by hand from SEC companyfacts.
Arithmetic only. Tools fetch and compute; they are forbidden to conclude (operator rule 8).
"""
import json, urllib.request, collections, os

CIK = "0000319201"
UA = {"User-Agent": "Research research@example.com"}
OUT = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(OUT, "companyfacts_KLAC.json")
if not os.path.exists(path):
    req = urllib.request.Request(
        f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json", headers=UA)
    data = urllib.request.urlopen(req, timeout=120).read()
    open(path, "wb").write(data)
facts = json.load(open(path, encoding="utf-8"))["facts"]["us-gaap"]


def annual(tag, want_fp="FY"):
    """Return {fy: (val, accn, end, form)} preferring the ORIGINAL 10-K filing,
    then noting any restatement."""
    out = collections.defaultdict(dict)
    if tag not in facts:
        return {}
    for unit, rows in facts[tag]["units"].items():
        for r in rows:
            if r.get("fp") != want_fp or r.get("form") not in ("10-K", "10-K/A"):
                continue
            if "start" in r:
                # duration fact: require ~a full year
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e - s).days <= 400):
                    continue
            fy = r["fy"]
            key = (r["end"], )
            out[fy][r["accn"]] = (r["val"], r["end"], r.get("frame"))
    return out


def series(tag):
    """One value per fiscal-year END date, taking the EARLIEST-filed (original) value,
    and recording any later differing value as a restatement."""
    if tag not in facts:
        return {}, {}
    by_end = collections.defaultdict(list)
    for unit, rows in facts[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A") or r.get("fp") != "FY":
                continue
            if "start" in r:
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e - s).days <= 400):
                    continue
            by_end[r["end"]].append((r["filed"], r["accn"], r["val"]))
    orig, restated = {}, {}
    for end, lst in by_end.items():
        lst.sort()
        orig[end] = (lst[0][2], lst[0][1], lst[0][0])
        vals = {v for _, _, v in lst}
        if len(vals) > 1:
            restated[end] = sorted(vals)
    return orig, restated


TAGS = {
    "OCF": "NetCashProvidedByUsedInOperatingActivities",
    "SBC": "ShareBasedCompensation",
    "DA": "DepreciationDepletionAndAmortization",
    "DA2": "DepreciationAmortizationAndAccretionNet",
    "CAPEX": "PaymentsToAcquirePropertyPlantAndEquipment",
    "REV": "RevenueFromContractWithCustomerExcludingAssessedTax",
    "REV2": "Revenues",
    "GP": "GrossProfit",
    "COGS": "CostOfGoodsAndServicesSold",
    "RD": "ResearchAndDevelopmentExpense",
    "SGA": "SellingGeneralAndAdministrativeExpense",
    "NI": "NetIncomeLoss",
    "EQ": "StockholdersEquity",
    "DIV": "PaymentsOfDividendsCommonStock",
    "BUYBACK": "PaymentsForRepurchaseOfCommonStock",
    "TAXPAID": "IncomeTaxesPaidNet",
    "PRETAX": "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
    "TAXEXP": "IncomeTaxExpenseBenefit",
    "ASSETS": "Assets",
    "GOODWILL": "Goodwill",
    "INTANG": "FiniteLivedIntangibleAssetsNet",
    "DEBT": "LongTermDebtNoncurrent",
    "CASH": "CashAndCashEquivalentsAtCarryingValue",
}

data = {}
rest = {}
for k, t in TAGS.items():
    data[k], rest[k] = series(t)

ends = sorted({e for k in ("OCF",) for e in data[k]})
print("FY_end      OCF        SBC        D&A       capex     OE(capex)   OE(D&A)     rev")
rows = []
for e in ends:
    ocf = data["OCF"].get(e, (None,))[0]
    sbc = data["SBC"].get(e, (None,))[0]
    da = data["DA"].get(e, (None,))[0] or data["DA2"].get(e, (None,))[0]
    cap = data["CAPEX"].get(e, (None,))[0]
    rev = data["REV"].get(e, (None,))[0] or data["REV2"].get(e, (None,))[0]
    if None in (ocf, sbc, cap):
        print(e, "MISSING", ocf, sbc, da, cap)
        continue
    oe_cap = ocf - sbc - cap
    oe_da = (ocf - sbc - da) if da else None
    rows.append((e, ocf, sbc, da, cap, oe_cap, oe_da, rev))
    m = 1e6
    print(f"{e}  {ocf/m:9.1f} {sbc/m:9.1f} {(da or 0)/m:9.1f} {cap/m:9.1f} "
          f"{oe_cap/m:10.1f} {(oe_da/m if oe_da else 0):10.1f} {(rev or 0)/m:9.1f}")

print("\nRESTATEMENTS DETECTED (end: distinct values across vintages):")
for k, d in rest.items():
    if d:
        print(" ", k, {e: [round(v/1e6, 1) for v in vs] for e, vs in sorted(d.items())})

# windows
import statistics
m = 1e6
def win(rows, n, idx):
    vals = [r[idx] for r in rows[-n:] if r[idx] is not None]
    return sum(vals)/len(vals)/m if vals else None

print("\nWINDOWS (mean, $M):")
for n in (3, 5, 8, 10, len(rows)):
    print(f"  {n:2d}-yr:  capex-end {win(rows,n,5):9.1f}   D&A-end {win(rows,n,6) or 0:9.1f}")

# leave-two-out on the 5 and 10 year windows (drop the two highest)
def lto(rows, n, idx):
    vals = sorted([r[idx] for r in rows[-n:] if r[idx] is not None])
    vals = vals[:-2]
    return sum(vals)/len(vals)/m
print(f"  5-yr leave-two-out (drop 2 highest):  {lto(rows,5,5):9.1f}")
print(f" 10-yr leave-two-out (drop 2 highest):  {lto(rows,10,5):9.1f}")

print("\nOTHER SERIES ($M unless noted):")
for k in ("REV", "GP", "COGS", "RD", "SGA", "NI", "EQ", "DIV", "BUYBACK",
          "TAXPAID", "PRETAX", "TAXEXP", "ASSETS", "GOODWILL", "INTANG", "DEBT", "CASH"):
    d = data.get(k) or {}
    if d:
        print(f"  {k:9s}", {e: round(v[0]/1e6, 1) for e, v in sorted(d.items())})
