# Q3 arithmetic for the CL run: net tangible operating capital and the return on it (transcription from XBRL; read against the filed balance sheets)
from xbrl import annual
T = ["Assets","CashAndCashEquivalentsAtCarryingValue","MarketableSecuritiesCurrent","Goodwill","IntangibleAssetsNetExcludingGoodwill",
     "DeferredIncomeTaxAssetsNet","DeferredTaxAssetsNetNoncurrent","LiabilitiesCurrent","DebtCurrent","ShortTermBorrowings",
     "LongTermDebtCurrent","ShortTermBankLoansAndNotesPayable","PropertyPlantAndEquipmentNet","OperatingIncomeLoss"]
o = annual("cache/CL_companyfacts.json", T)
g = lambda t, y: (o[t].get(y) or 0) / 1e6
# segment operating profit before Corporate, from the segment notes (FY2014, FY2016, FY2019, FY2022, FY2025 10-Ks)
seg = {2014: 4053+592, 2015: 3864+612, 2016: 3814+653, 2017: 3841+677, 2018: 3616+680, 2019: 3505+703, 2020: 3594+793,
       2021: 3495+901, 2022: 3348+850, 2023: 3882+806, 2024: 4088+965, 2025: 3959+1064}
print("year  tangible_op_capital  PPE   segment_OP  pre-tax return on tangible capital")
for y in range(2016, 2026):
    curdebt = g("ShortTermBankLoansAndNotesPayable", y) if g("ShortTermBankLoansAndNotesPayable", y) else 0
    # 2016-2018 the short-term line excludes current portion; filed 'notes and loans payable' + 'current portion of long-term debt'
    if y <= 2018: curdebt = g("ShortTermBankLoansAndNotesPayable", y) + g("LongTermDebtCurrent", y)
    cap = (g("Assets", y) - g("CashAndCashEquivalentsAtCarryingValue", y) - g("MarketableSecuritiesCurrent", y) - g("Goodwill", y)
           - g("IntangibleAssetsNetExcludingGoodwill", y) - (g("DeferredIncomeTaxAssetsNet", y) or g("DeferredTaxAssetsNetNoncurrent", y))
           - (g("LiabilitiesCurrent", y) - curdebt))
    print(y, f"{cap:10.0f} {g('PropertyPlantAndEquipmentNet', y):8.0f} {seg[y]:8.0f}   {100*seg[y]/cap:6.0f}%")
