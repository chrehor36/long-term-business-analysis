"""PM Q3: return on the tangible capital the business needs, FY2025 balance sheet (10-K 0001628280-26-005939), USD M."""
assets = 69185; goodwill = 17264; intang = 10884; equity_inv = 2891; cash = 4872
ap = 4407; mkt = 1354; taxes_nonincome = 7555; emp = 1545; other_accr = 3298; inc_tax = 1255
op_income = 14892
tangible_operating_assets = assets - goodwill - intang - equity_inv - cash
nibcl = ap + mkt + taxes_nonincome + emp + other_accr + inc_tax  # dividends payable and debt excluded
ntc = tangible_operating_assets - nibcl
print(f"tangible operating assets {tangible_operating_assets}; non-interest-bearing current liabilities {nibcl}")
print(f"net tangible operating capital {ntc}; operating income {op_income}; pre-tax return {op_income/ntc*100:.0f}%")
# incremental: 2018 -> 2025
oi18, oi25 = 11377, 14892
oc18, oc25 = 7479, 10026
acq = 22545  # acquisitions, rights, minority buyouts 2018-2025 (owner_cash.py), includes 1346 RBH deconsolidated cash
print(f"operating income +{oi25-oi18}; owner cash +{oc25-oc18}; acquisitions/rights {acq}")
print(f"incremental owner cash / acquisitions = {(oc25-oc18)/acq*100:.1f}%; incremental operating income / acquisitions = {(oi25-oi18)/acq*100:.1f}%")
