"""Owner cash for Localiza, COMPUTATION, NOT A CLEARANCE (the file closed at Q2).
Sources: CVM DFP consolidated statements (EBIT, cash flow lines) as transcribed in the company's own IR spreadsheet
(cross-checked: 2025 EBIT 7,811.6 and net operating cash 2,146.5 equal the DFP), the company's pro forma combined
EBIT for 2021-2022 (Localiza + Locamerica from 01/01/2021, spreadsheet 'Consolidated results proforma'). BRL millions."""
yrs = [2021,2022,2023,2024,2025]
ebit_combined = {2021:5142.1, 2022:6272.9, 2023:5898.5, 2024:5805.2, 2025:7811.6}   # 2021-22 pro forma combined
ebit_reported = {2021:3224.0, 2022:4529.4, 2023:5898.5, 2024:5805.2, 2025:7811.6}
ioc_paid      = {2021:282.1, 2022:725.9, 2023:1134.6, 2024:1294.4, 2025:1755.6}       # interest on capital paid (deductible)
other_da      = {2021:218.4+0, 2022:289.4, 2023:446.5, 2024:523.9, 2025:573.4}       # other assets D&A (incl. right of use)
other_capex   = {2021:143.4, 2022:352.8, 2023:387.4, 2024:445.0, 2025:435.4}
lease_princ   = {2021:144.0, 2022:187.3, 2023:249.3, 2024:284.3, 2025:301.3}
lease_int     = {2021:49.7, 2022:61.5, 2023:71.9, 2024:81.9, 2025:107.7}
cash_tax      = {2021:307.1, 2022:83.4, 2023:130.2, 2024:487.5, 2025:477.3}
# cash-flow lines (reported consolidated) for the all-spending case
ocf      = {2021:-3371.4, 2022:-8826.6, 2023:-9919.2, 2024:650.3, 2025:2146.5}
fin_assets_line = {2021:-3188.2, 2022:-396.6, 2023:-4103.9, 2024:433.8, 2025:-1056.2}   # short-term investments inside OCF
int_paid = {2021:-372.9, 2022:-2349.3, 2023:-4804.4, 2024:-5295.0, 2025:-5434.5}
sup_int  = {2021:0, 2022:-6.2, 2023:-9.9, 2024:-19.1, 2025:-14.8}
T = 0.34
rows=[]
print('year EBITcomb tax(34%x(EBIT-IOC)) otherAssetsNet ownercash_maint | FCF_allspend_preinterest_aftercashtax')
for y in yrs:
    tax = T*(ebit_combined[y]-ioc_paid[y])
    other_net = other_da[y]-other_capex[y]-lease_princ[y]-lease_int[y]
    oc_maint = ebit_combined[y]-tax+other_net
    # all spending: OCF with interest added back and short-term investment flows removed, less other capex and lease principal
    fcf = ocf[y]-fin_assets_line[y]-int_paid[y]-sup_int[y]-other_capex[y]-lease_princ[y]
    rows.append((y,oc_maint,fcf))
    print(y, round(ebit_combined[y]), round(tax), round(other_net), round(oc_maint), '|', round(fcf))
avg_m = sum(r[1] for r in rows)/5
print('avg owner cash maintenance 2021-2025 (combined basis):', round(avg_m))
avg_f3 = sum(r[2] for r in rows if r[0]>=2023)/3
print('avg all-spending FCF pre-interest 2023-2025 (after cash tax, reported):', round(avg_f3))
# growth of maintenance owner cash: halves (first two vs last two years), and end-to-end
g_ends = (rows[-1][1]/rows[0][1])**(1/4)-1
h1 = (rows[0][1]+rows[1][1])/2; h2=(rows[3][1]+rows[4][1])/2
g_halves = (h2/h1)**(1/3)-1
print('growth end to end %.3f; between halves (2021-22 vs 2024-25, 3 yrs apart) %.3f' % (g_ends,g_halves))
