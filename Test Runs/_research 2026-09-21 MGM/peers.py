# -*- coding: utf-8 -*-
"""Same-metric, same-window competitor row, built from each registrant's own companyfacts.
Arithmetic only. It concludes nothing (operator rule 8)."""
import json, io, os, sys, time, urllib.request
from datetime import date
D = os.path.dirname(os.path.abspath(__file__))
PD = os.path.join(D, "peers")
os.makedirs(PD, exist_ok=True)
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
PEERS = {
    "MGM": "0000789570", "LVS": "0001300514", "WYNN": "0001174922",
    "CZR": "0001590895", "BYD": "0000906553", "PENN": "0000921738",
    "MLCO": "0001381640", "VICI": "0001705696",
}
FORMS = ("10-K", "20-F")


def facts(t, cik):
    p = os.path.join(PD, t + "_companyfacts.json")
    if not os.path.exists(p):
        r = urllib.request.Request(
            "https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json" % cik, headers=UA)
        with urllib.request.urlopen(r, timeout=90) as f:
            b = f.read()
        io.open(p, "wb").write(b) if isinstance(b, bytes) else None
        time.sleep(0.4)
    return json.load(io.open(p, encoding="utf-8"))


def dur(fx, tags):
    us = {}
    us.update(fx["facts"].get("us-gaap", {}))
    us.update(fx["facts"].get("ifrs-full", {}))
    out = {}
    for tag in tags:
        if tag not in us:
            continue
        for u, items in us[tag]["units"].items():
            for it in items:
                if it.get("form") not in FORMS:
                    continue
                s, e = it.get("start"), it.get("end")
                if not s:
                    continue
                d0 = date(*map(int, s.split("-")))
                d1 = date(*map(int, e.split("-")))
                if not (340 <= (d1 - d0).days <= 380):
                    continue
                k = e
                p = out.get(k)
                if p is None or it.get("filed", "") > p[1]:
                    out[k] = (it["val"], it.get("filed", ""), tag)
    return {k: v[0] for k, v in sorted(out.items())}


def instant(fx, tags):
    us = {}
    us.update(fx["facts"].get("us-gaap", {}))
    us.update(fx["facts"].get("ifrs-full", {}))
    out = {}
    for tag in tags:
        if tag not in us:
            continue
        for u, items in us[tag]["units"].items():
            for it in items:
                if it.get("form") not in FORMS:
                    continue
                if it.get("start"):
                    continue
                e = it["end"]
                p = out.get(e)
                if p is None or it.get("filed", "") > p[1]:
                    out[e] = (it["val"], it.get("filed", ""), tag)
    return {k: v[0] for k, v in sorted(out.items())}


M = {
    "REV": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "RevenueFromContractWithCustomerExcludingAssessedTaxMember"],
    "OPINC": ["OperatingIncomeLoss"],
    "OCF": ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "CAPEX": ["PaymentsToAcquireProductiveAssets", "PaymentsToAcquirePropertyPlantAndEquipment",
              "PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets"],
    "DA": ["DepreciationAndAmortization", "DepreciationDepletionAndAmortization",
           "DepreciationAmortizationAndAccretionNet"],
    "SBC": ["ShareBasedCompensation"],
    "OPLEASECOST": ["OperatingLeaseCost", "OperatingLeaseExpense"],
    "NI_PARENT": ["NetIncomeLoss"],
}
I = {
    "PPE": ["PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization", "PropertyPlantAndEquipmentNet"],
    "ROU": ["OperatingLeaseRightOfUseAsset"],
    "ASSETS": ["Assets"],
    "EQ_PARENT": ["StockholdersEquity"],
    "DEBT_LT": ["LongTermDebtNoncurrent"],
    "CASH": ["CashAndCashEquivalentsAtCarryingValue"],
    "GW": ["Goodwill"],
    "OPLEASELIAB_NC": ["OperatingLeaseLiabilityNoncurrent"],
}
if __name__ == "__main__":
    res = {}
    for t, cik in PEERS.items():
        fx = facts(t, cik)
        d = {}
        for k, tags in M.items():
            d[k] = dur(fx, tags)
        for k, tags in I.items():
            d[k] = instant(fx, tags)
        res[t] = d
        print(t, "ok")
    json.dump(res, io.open(os.path.join(PD, "peer_series.json"), "w", encoding="utf-8"))
    yrs = ["2021-12-31", "2022-12-31", "2023-12-31", "2024-12-31", "2025-12-31"]
    print()
    print("ticker,year,rev_m,opinc_m,opmargin,ppe_m,rou_m,opleasecost_m,assets_m,eq_parent_m,ocf_m,capex_m,da_m")
    for t in PEERS:
        d = res[t]
        for y in yrs:
            def g(k):
                v = d[k].get(y)
                return "" if v is None else "%.1f" % (v / 1e6)
            om = ""
            if d["REV"].get(y) and d["OPINC"].get(y) is not None:
                om = "%.3f" % (d["OPINC"][y] / d["REV"][y])
            print(",".join([t, y[:4], g("REV"), g("OPINC"), om, g("PPE"), g("ROU"),
                            g("OPLEASECOST"), g("ASSETS"), g("EQ_PARENT"), g("OCF"),
                            g("CAPEX"), g("DA")]))
