"""Transcribe annual (fiscal June) cash-flow and earnings series from cache/companyfacts.json.
Transcription only; the run cross-checks against the filed statements."""
import json, pathlib, sys
p = pathlib.Path(__file__).parent / "cache" / "companyfacts.json"
d = json.load(open(p))["facts"]["us-gaap"]
tags = sys.argv[1:] or ['NetCashProvidedByUsedInOperatingActivities', 'ShareBasedCompensation',
        'PaymentsToAcquireOtherPropertyPlantAndEquipment', 'PaymentsToAcquirePropertyPlantAndEquipment',
        'PaymentsToAcquireIntangibleAssets', 'PaymentsToAcquireBusinessesNetOfCashAcquired',
        'PaymentsForRepurchaseOfCommonStock', 'PaymentsOfDividendsCommonStock', 'PaymentsOfDividends',
        'NetIncomeLoss', 'Revenues', 'DepreciationDepletionAndAmortization', 'InterestPaidNet',
        'WeightedAverageNumberOfDilutedSharesOutstanding', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest']
for t in tags:
    if t not in d:
        print(t, "MISSING"); continue
    u = d[t]["units"]; k = list(u)[0]
    by = {}
    for f in u[k]:
        if f.get("form") == "10-K" and f["end"][5:7] == "06" and f.get("start", "x")[:4] == str(int(f["end"][:4]) - 1):
            by.setdefault(f["end"][:4], f["val"])  # first-filed vintage
    print(t, {y: round(v / 1e6, 1) for y, v in sorted(by.items()) if y >= "2014"})
