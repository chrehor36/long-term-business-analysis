"""Annual 10-K duration facts from the SEC companyfacts cache for CIK 902274 (transcription only)."""
import json,sys
from datetime import date
f=r"C:\Users\chreh\OneDrive\Documents\BRK\tools\_cache\facts_0000902274.json"
d=json.load(open(f)); g=d['facts']['us-gaap']
def ann(tag, latest=False):
    out={}
    for u,vals in g.get(tag,{}).get('units',{}).items():
        for v in vals:
            if v.get('form')=='10-K' and 'start' in v:
                s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                if 340<(e-s).days<380:
                    if latest or v['end'] not in out: out[v['end']]=v['val']
    return dict(sorted(out.items()))
tags=sys.argv[1:] or ['Revenues','SalesRevenueNet','SalesRevenueGoodsNet','RevenueFromContractWithCustomerExcludingAssessedTax','GrossProfit','OperatingIncomeLoss','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeTaxExpenseBenefit','NetIncomeLoss','InterestExpense','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividendsCommonStock','PaymentsOfDividends','ProceedsFromIssuanceOfCommonStock','GoodwillImpairmentLoss','AssetImpairmentCharges','IncomeTaxesPaidNet','InterestPaidNet','InterestPaid','RepaymentsOfLongTermDebt','ProceedsFromIssuanceOfLongTermDebt','PensionAndOtherPostretirementBenefitContributions','DefinedBenefitPlanContributionsByEmployer','RestructuringCharges']
for t in tags:
    a=ann(t)
    if a: print(f"{t:<80}", {k[:4]:round(v/1e6,1) for k,v in a.items()})
