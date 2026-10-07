# Transcription of GPOR XBRL company facts: annual duration values by period, from 10-K filings.
# Arithmetic only. Usage: python facts_table.py
import json, datetime as dt, sys
F = json.load(open(r'C:/Users/chreh/OneDrive/Documents/BRK/tools/_cache/facts_0000874499.json'))['facts']['us-gaap']
tags = sys.argv[1:] or ['Revenues','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquireOilAndGasProperty',
 'DepreciationDepletionAndAmortization','ImpairmentOfOilAndGasProperties','ShareBasedCompensation','NetIncomeLoss',
 'InterestExpense','IncomeTaxExpenseBenefit','GainLossOnDerivativeInstrumentsNetPretax','ProceedsFromSaleOfOilAndGasPropertyAndEquipment',
 'PaymentsForRepurchaseOfCommonStock','StockRepurchasedDuringPeriodValue','StockRepurchasedAndRetiredDuringPeriodValue','ReorganizationItems',
 'ResultsOfOperationsProductionOrLiftingCosts','ResultsOfOperationsRevenueFromOilAndGasProducingActivities','CostsIncurredAcquisitionOfOilAndGasProperties','PaymentsForRepurchaseOfPreferredStockAndPreferenceStock','UnrealizedGainLossOnDerivativesAndCommodityContracts']
def d(s): return dt.date.fromisoformat(s)
for t in tags:
    if t not in F: print(t,'MISSING'); continue
    rows={}
    for u,v in F[t]['units'].items():
        for x in v:
            if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
            days=(d(x['end'])-d(x['start'])).days
            if days<120: continue
            key=(x['start'],x['end'])
            # keep latest filed
            if key not in rows or x['filed']>rows[key]['filed']: rows[key]=x
    print('==',t)
    for (s,e),x in sorted(rows.items(), key=lambda z:z[0][1]):
        print(f"   {s}..{e}  {x['val']/1e6:12.1f}  acc {x['accn']} filed {x['filed']}")
