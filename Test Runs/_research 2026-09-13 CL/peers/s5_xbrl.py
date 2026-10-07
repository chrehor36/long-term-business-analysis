"""Item 5: companyfacts transcription for the 8 10-K filers. Transcription only; no ratios concluded."""
import json, os, csv, datetime as dt
from p_common import jload, HERE

TICK = ["PG", "CHD", "CLX", "KMB", "KVUE", "GIS", "SJM", "FRPT"]
GROUPS = [
    ("OperatingIncome", "D", ["OperatingIncomeLoss"]),
    ("Revenue", "D", ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet", "RevenueFromContractWithCustomerIncludingAssessedTax"]),
    ("PretaxIncome", "D", ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]),
    ("InterestExpense", "D", ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"]),
    ("GrossProfit", "D", ["GrossProfit"]),
    ("AdvertisingExpense", "D", ["AdvertisingExpense", "MarketingAndAdvertisingExpense"]),
    ("Assets", "I", ["Assets"]),
    ("Cash", "I", ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]),
    ("Goodwill", "I", ["Goodwill"]),
    ("IntangiblesExGoodwill", "I", ["IntangibleAssetsNetExcludingGoodwill"]),
    ("FiniteIntangibles", "I", ["FiniteLivedIntangibleAssetsNet"]),
    ("IndefiniteIntangibles", "I", ["IndefiniteLivedIntangibleAssetsExcludingGoodwill", "IndefiniteLivedTrademarks"]),
    ("LiabilitiesCurrent", "I", ["LiabilitiesCurrent"]),
    ("DebtCurrent", "I", ["DebtCurrent"]),
    ("LongTermDebtCurrent", "I", ["LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent"]),
    ("ShortTermBorrowings", "I", ["ShortTermBorrowings", "OtherShortTermBorrowings"]),
    ("CommercialPaper", "I", ["CommercialPaper"]),
    ("OperatingLeaseROU", "I", ["OperatingLeaseRightOfUseAsset"]),
]
man = jload("manifest.json")
d = lambda s: dt.date.fromisoformat(s)
rows_out = []
md = []
for t in TICK:
    cf = jload(f"{t}_companyfacts.json")["facts"].get("us-gaap", {})
    # accession -> fiscal period end of that annual filing
    acc_period = {v["acc"]: v["period"] for v in man[t].values() if v["form"] in ("10-K", "10-K/A")}
    ann_periods = sorted({v["period"] for v in man[t].values() if v["form"] == "10-K"})
    # fiscal year ends: annual periods plus earlier 12-month ends reported as comparatives (from OperatingIncome/Revenue)
    table = {}
    ends = set(ann_periods)
    for name, kind, tags in GROUPS:
        for tag in tags:
            if tag not in cf:
                continue
            units = cf[tag]["units"].get("USD", [])
            facts = [f for f in units if f.get("form") == "10-K" and f.get("fp") == "FY"]
            if kind == "D":
                facts = [f for f in facts if "start" in f and 350 <= (d(f["end"]) - d(f["start"])).days <= 380]
            else:
                facts = [f for f in facts if "start" not in f]
            byend = {}
            for f in facts:
                if f["end"] < "2020-04-01":
                    continue
                byend.setdefault(f["end"], []).append(f)
            for end, fs in byend.items():
                if kind == "D":
                    ends.add(end)
                fs.sort(key=lambda f: f["filed"])
                orig = [f for f in fs if acc_period.get(f["accn"]) == end]
                first = orig[0] if orig else fs[0]
                last = fs[-1]
                key = (name, end)
                if key in table:  # first tag in the list wins; keep a note of alternates
                    table[key]["alt"].append(f"{tag}={first['val']}")
                    continue
                table[key] = dict(tag=tag, val=first["val"], accn=first["accn"], filed=first["filed"],
                                  first_is_original=bool(orig), later_val=last["val"], later_accn=last["accn"], alt=[])
    # keep only fiscal-year ends that are annual periods or 12-month duration ends
    ends = sorted(e for e in ends if any(abs((d(e) - d(p)).days) < 8 or True for p in ann_periods))
    ends = [e for e in ends if e >= "2020-04-01"]
    md.append(f"\n#### {t} companyfacts (us-gaap, USD, form 10-K, fp FY) CIK file {t}_companyfacts.json\n")
    md.append("Values as first reported for each fiscal-year end (from the 10-K for that year where available; otherwise the earliest 10-K that carries it as a comparative, marked *). A later 10-K value that differs is shown as 'later: value (accession)'.\n")
    alts = []
    md.append("| item | tag | " + " | ".join(ends) + " |")
    md.append("|---|---|" + "---|" * len(ends))
    for name, kind, tags in GROUPS:
        used = sorted({table[(name, e)]["tag"] for e in ends if (name, e) in table})
        cells = []
        for e in ends:
            x = table.get((name, e))
            if not x:
                cells.append("nd")
                continue
            c = f"{x['val']:,}" + ("" if x["first_is_original"] else "*")
            if x["later_val"] != x["val"]:
                c += f" (later: {x['later_val']:,}, {x['later_accn']})"
            cells.append(c)
            rows_out.append(dict(ticker=t, item=name, tag=x["tag"], end=e, value=x["val"], accn=x["accn"], filed=x["filed"],
                                 from_own_year_10K=x["first_is_original"], later_value=x["later_val"], later_accn=x["later_accn"],
                                 alternates=";".join(x["alt"])))
        md.append(f"| {name} | {', '.join(used) or 'none of: ' + ', '.join(tags)} | " + " | ".join(cells) + " |")
        for e in ends:
            x = table.get((name, e))
            if x and x["alt"]:
                alts.append(f"{name} {e}: used {x['tag']}={x['val']:,}; also tagged " + "; ".join(sorted(set(x['alt']))))
    if alts:
        md.append("\nOther tags carrying a value for the same item and date (first tag in the priority list was used):\n")
        md += ["- " + a for a in alts]
with open(os.path.join(HERE, "item5_xbrl.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows_out[0]))
    w.writeheader(); w.writerows(rows_out)
open(os.path.join(HERE, "_item5_tables.md"), "w", encoding="utf-8").write("\n".join(md))
print("\n".join(md))
