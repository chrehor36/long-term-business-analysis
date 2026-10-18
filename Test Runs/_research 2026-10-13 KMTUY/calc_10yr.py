"""Ten-year arithmetic for the KMTUY run (sums of filed figures only; no judgment).
Owner cash, equity-only = CFO - capex + proceeds from sale of fixed assets - acquisitions (net)
  - purchases of noncontrolling interests - dividends to noncontrolling interests.
All-equity = equity-only + (interest expense - interest and dividend income) x (1 - 0.271)
  [0.271 = FY2025 effective tax rate, ASR157 MD&A (x); a run CONVENTION, stated in the run file].
"""
import csv
T = 0.271
rows = list(csv.DictReader(open("data_10yr.csv")))
g = lambda r, k: float(r[k]) if r[k] else 0.0
print(f"{'FY':7}{'sales':>10}{'opinc':>9}{'op%':>6}{'CFO':>9}{'capex':>9}{'acq':>9}{'OC_eq':>9}{'OC_all':>9}{'OC_exacq':>9}{'OC%s':>6}{'D&Avar':>9}{'netdebt':>10}{'ROtc%':>7}{'ROtangc%':>9}")
out = []
for r in rows:
    oc_eq = g(r,'cfo') - g(r,'capex') + g(r,'sale_fa') - g(r,'acq_net') - g(r,'nci_acq') - g(r,'nci_div')
    oc_all = oc_eq + (g(r,'int_exp') - g(r,'int_inc')) * (1 - T)
    oc_exacq = oc_all + g(r,'acq_net') + g(r,'nci_acq')
    # depreciation variant: CFO - D&A instead of capex net of disposals
    da_var = g(r,'cfo') - g(r,'da') - g(r,'acq_net') - g(r,'nci_acq') - g(r,'nci_div') + (g(r,'int_exp') - g(r,'int_inc')) * (1 - T)
    debt = g(r,'debt_st') + g(r,'debt_cur') + g(r,'debt_lt')
    nd = debt - g(r,'cash')
    cap = g(r,'equity') + nd
    tcap = cap - g(r,'goodwill') - g(r,'intang')
    nopat = g(r,'op_income') * (1 - T)
    out.append(dict(fy=r['fy'], sales=g(r,'sales'), oc_all=oc_all, oc_eq=oc_eq, oc_exacq=oc_exacq, da_var=da_var, nd=nd, cap=cap, tcap=tcap, nopat=nopat))
    print(f"{r['fy']:7}{g(r,'sales')/1e3:10.1f}{g(r,'op_income')/1e3:9.1f}{100*g(r,'op_income')/g(r,'sales'):6.1f}{g(r,'cfo')/1e3:9.1f}{g(r,'capex')/1e3:9.1f}{(g(r,'acq_net')+g(r,'nci_acq'))/1e3:9.1f}{oc_eq/1e3:9.1f}{oc_all/1e3:9.1f}{oc_exacq/1e3:9.1f}{100*oc_all/g(r,'sales'):6.1f}{da_var/1e3:9.1f}{nd/1e3:10.1f}{100*nopat/cap:7.1f}{100*nopat/tcap:9.1f}")
import statistics as st
print("ten-year average NOPAT/capital %.1f%%, NOPAT/tangible capital %.1f%%" % (100*st.mean(o['nopat']/o['cap'] for o in out), 100*st.mean(o['nopat']/o['tcap'] for o in out)))
w = out[-5:]
print("five-year (FY2021-FY2025) average owner cash: all-equity %.1f, equity-only %.1f, ex-acquisitions %.1f, D&A variant %.1f (JPY bn)" % tuple(st.mean(o[k] for o in w)/1e3 for k in ['oc_all','oc_eq','oc_exacq','da_var']))
