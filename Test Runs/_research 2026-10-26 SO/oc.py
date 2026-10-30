# Owner cash, Southern Company consolidated, USD millions, from the filed cash-flow statements
# FY2021-2023: 10-K FY2023 acc 0000092122-24-000009; FY2023-2025: 10-K FY2025 acc 0000092122-26-000006
Y=[2021,2022,2023,2024,2025]
OCF=[6169,6302,7553,9788,9802]
SBC=[144,127,137,132,136]
CAPEX=[7586,7923,9095,8955,12737]           # property additions
REMOVAL=[442,649,592,632,655]               # cost of removal net of salvage
LTSA=[188,190,99,108,159]
CPAY=[-124,203,18,106,301]                  # change in construction payables (investing, +=less cash out)
NDT=[1598-1593,1125-1112,1142-1121,1551-1535,1702-1685]
OTHINV=[-75,133,43,164,58]                  # other investing activities, outflow positive
ACQ=[-917,-275,-164,-369,635+286-1]         # acquisitions (incl. NCI membership purchase 2025) net of disposition proceeds
NCI=[351-501,259-73,234-21,185,200]         # distributions to minority partners net of their contributions
FLP=[17,16,18,11,21]                        # finance lease principal
DA=[3973,4064,4986,5266,6030]               # D&A total, cash-flow statement
INTPAID=[1718,1758,2184,2538,2692]
def avg(x): return sum(x)/len(x)
rows=[]
for i,y in enumerate(Y):
    allspend = OCF[i]-SBC[i]-CAPEX[i]-REMOVAL[i]-LTSA[i]+CPAY[i]-NDT[i]-OTHINV[i]-NCI[i]-FLP[i]
    allacq = allspend-ACQ[i]
    capex_cash = CAPEX[i]+REMOVAL[i]+LTSA[i]-CPAY[i]+NDT[i]+OTHINV[i]+FLP[i]
    dabase = OCF[i]-SBC[i]-DA[i]-NCI[i]
    rows.append((y,allspend,allacq,capex_cash,dabase))
    print(y,'OC all spending ex-acq',allspend,'| incl net acq',allacq,'| capital spending (cash)',capex_cash,'| D&A variant',dabase)
for k,n in [(1,'all spend ex acq'),(2,'incl acq'),(3,'capital spending'),(4,'D&A variant')]:
    print('mean',n,round(avg([r[k] for r in rows])))
print('mean OCF-SBC-NCI', round(avg([OCF[i]-SBC[i]-NCI[i] for i in range(5)])))
print('mean D&A',avg(DA),'mean interest paid',avg(INTPAID))
