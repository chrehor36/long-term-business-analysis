"""COMPUTATION, NOT A CLEARANCE. FSRDQ (Fisker Inc.) Q7 range and fair price by the v5 conventions,
computed only because the operator's reporting convention asks for the two figures after an earlier STOP.
Inputs from tools/run.py (as-filed XBRL, checked against the FY2023 10-K 0001720990-24-000045)."""
oc_capex = {2019:-7.4, 2020:-39.4, 2021:-441.3, 2022:-663.1, 2023:-904.7}   # OCF - SBC - capex, $M
oc_da    = {2019:-7.4, 2020:-38.8, 2021:-307.7, 2022:-477.4, 2023:-753.2}
interest = {2019:0.0, 2020:0.0, 2021:0.0, 2022:17.985, 2023:16.688}        # cash paid for interest, 10-K FY2023/FY2022
sov, floor = 0.056, 0.10
net_debt = 291.715 + 935.228 - 325.452     # convertible notes (current + non-current) less cash, 2023-12-31
shares = 1385.486856 + 132.354128          # Class A + Class B, 10-K cover as of 2024-04-15
m_eq = sum(oc_capex.values())/5
m_ae = sum(oc_capex[y]+interest[y] for y in oc_capex)/5
m_da = sum(oc_da.values())/5
print(f"mean owner cash, equity basis (capex): {m_eq:.1f}  D&A variant {m_da:.1f}  all-equity (before interest): {m_ae:.1f}")
print(f"net debt {net_debt:.1f}  shares {shares:.2f}M")
# Decline specific (b): series negative and worsening; growth meaningless; range is the no-growth case alone.
v_ae = m_ae/sov; v_eq = m_eq/sov
print(f"no-growth value at sovereign: all-equity {v_ae:,.0f}M -> per share {(v_ae-net_debt)/shares:.2f}; equity-only {v_eq/shares:.2f}")
f_ae = (m_ae/floor - net_debt)/shares; f_eq = (m_eq/floor)/shares
print(f"fair price (both ends = the single no-growth case, at 10%): all-equity {f_ae:.2f}; equity-only {f_eq:.2f}")
print(f"D&A variant, all-equity range per share {((m_da+6.93)/sov-net_debt)/shares:.2f}")
