# Owner earnings, non-financial perimeter, yen billions. Every input is a filed figure (see run file Q4 table).
Y = ['FY3/21','FY3/22','FY3/23','FY3/24','FY3/25','FY3/26']
ocf_B   = [1150.265, 813.268, 415.473, 1177.828, 1972.439, None]      # "Sony without FS" (unaudited, Item 5)
fs_div  = [30.454, 39.159, 41.335, 50.037, 0.0, None]                   # FS segment dividends paid (to parent)
ocf_A   = [None, None, None, 1103.645, 1971.349, 1966.292]             # continuing ops (audited, FY3/26 20-F)
sbc     = [8.892, 11.105, 15.781, 21.657, 29.416, 39.102]              # total SBC expense (Note 21 / XBRL)
da      = [663.513, 810.301, 978.257, 1117.292, 1125.588, 1180.655]    # D&A ex-FS (without-FS schedule; continuing from FY3/24)
content = [293.239, 400.900, 510.123, 571.008, 535.829, 595.178]      # content-asset amortization (content note)
capex   = [458.700, 420.542, 590.320, 605.779, 620.985, 457.681]      # PP&E + intangibles payments (ex-FS / continuing)
lease   = [81.399, 83.546, 89.681, 90.849, 98.949, 85.946]             # lease cash (net outflows FY3/21-23 incl FS; principal FY3/24-26)
ocf = []
for i in range(6):
    if ocf_A[i] is not None: ocf.append(ocf_A[i])
    else: ocf.append(ocf_B[i] - fs_div[i])
print('basis check FY3/24: B-adj', round(ocf_B[3]-fs_div[3],1), 'A', ocf_A[3], 'resid', round(ocf_B[3]-fs_div[3]-ocf_A[3],1))
print('basis check FY3/25: B-adj', round(ocf_B[4]-fs_div[4],1), 'A', ocf_A[4], 'resid', round(ocf_B[4]-fs_div[4]-ocf_A[4],1))
lo_c = [da[i]-content[i] for i in range(6)]
hi_c = [capex[i]+lease[i] for i in range(6)]
oe_lo = [ocf[i]-sbc[i]-hi_c[i] for i in range(6)]   # conservative: capex end
oe_hi = [ocf[i]-sbc[i]-lo_c[i] for i in range(6)]   # D&A end
print('year    OCF    SBC   c(DA-ex-content) c(capex+lease)  OE@DA  OE@capex')
for i in range(6):
    print(f"{Y[i]} {ocf[i]:8.1f} {sbc[i]:6.1f} {lo_c[i]:10.1f} {hi_c[i]:12.1f} {oe_hi[i]:9.1f} {oe_lo[i]:9.1f}")
def mean(a): return sum(a)/len(a)
for name, idx in [('3y audited FY3/24-26',[3,4,5]),('5y default FY3/22-26',[1,2,3,4,5]),('6y FY3/21-26',[0,1,2,3,4,5]),('5y ex-FY3/26 FY3/21-25',[0,1,2,3,4])]:
    a=[oe_hi[i] for i in idx]; b=[oe_lo[i] for i in idx]
    print(f"{name:28s} OE@DA {mean(a):7.1f}  OE@capex {mean(b):7.1f}  OCF mean {mean([ocf[i] for i in idx]):7.1f}")
# working-capital lines inside OCF (ex-FS): receivables, inventories, payables
rec = [-141.064,-121.684,-110.668,-223.150,227.664,124.104]; inv=[-56.509,-194.624,-560.382,75.641,199.916,155.382]; pay=[258.994,93.660,-64.765,-40.737,105.643,70.541]
print('WC (rec+inv+pay):', [round(rec[i]+inv[i]+pay[i],1) for i in range(6)])
cap = 3632*5843334871/1e9
print('cap bn', round(cap,1))
for name, v in [('5y@capex',mean([oe_lo[i] for i in [1,2,3,4,5]])),('5y@DA',mean([oe_hi[i] for i in [1,2,3,4,5]])),('3y@capex',mean([oe_lo[i] for i in [3,4,5]])),('3y@DA',mean([oe_hi[i] for i in [3,4,5]]))]:
    print(name, round(v,1), 'yield', round(100*v/cap,2))
