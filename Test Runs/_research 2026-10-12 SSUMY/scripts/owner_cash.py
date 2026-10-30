# Owner cash for Sumitomo Corporation, JPY millions, from the audited consolidated statements of cash flows
# (Annual Financial Reports FY2020..FY2025; company FY = year ended March 31 of the following calendar year).
# Every input is transcribed from docs/cf_*.txt (page dumps of the filed statements).
Y = ["FY2019","FY2020","FY2021","FY2022","FY2023","FY2024","FY2025"]  # years ended Mar 2020 .. Mar 2026
d = {
 "ocf":        [326618, 467097, 194066, 232801, 608850, 612281, 813456],
 "ppe_buy":    [-76935, -66342, -69716, -70295, -93380,-102799,-105910],
 "ppe_sell":   [  3472,   9034,   5300,  15140,   9385,   7782,   9953],
 "ip_buy":     [-42424,  -7986,  -7576, -44333, -28313, -20867, -35932],
 "ip_sell":    [ 15739,   8602,  22327,  32119,  13123,  21586,  37136],
 "sub_sell":   [ 15499,  -1700,  63737,  31530,   3579,   2323,  23912],
 "sub_buy":    [-73238, -13962,  -1792, -13565, -62343,-271701, -22348],
 "oi_sell":    [ 99909,  98577, 102280,  85241, 173414, 221900, 193639],
 "oi_buy":     [-135847,-123271,-93946,-131653,-238220,-290455,-225662],
 "loan_coll":  [ 42145,  23249,  50492,  20273,  30166,  14009,  13339],
 "loan_incr":  [-51737, -46308, -22067, -15982, -26621, -43164, -44019],
 "lease_rep":  [     0, -62586, -68365, -71509, -74710, -77238, -77427],  # FY2019 statement shows none separately (in debt repayments)
 "nci_div":    [-11821, -10455, -10708, -23555, -28562, -35213, -19145],
 "nci_buy":    [ -3798,   -280,  -2178,  -3247,  -3311,     -1,-754182],
 "int_paid":   [-45458, -27134, -22650, -46483, -71713, -67188, -75298],
 "int_recd":   [ 30587,  15904,  13601,  20728,  35352,  29165,  36309],
 "div_recd":   [114401,  97149, 142767, 205786, 217161, 214335, 203663],
 "wc":         [127337-97292+505-7228, -10383+138399+217409-4606, -148056-200792-28476+251924,
                -264356-9911-10599-39662, -4034-76554-18315-83175, -154014-89837+2004+113830, -82873-260091+2878+577825],
 "other_net":  [-114966, -91962,-249621,-118258, 130279,  30877,-122880],
 "dep":        [165340, 170906, 170363, 183749, 200172, 219467, 227623],
 "profit_par": [171359,-153067, 463694, 565178, 386352, 561859, 600334],
}
T = 0.31  # CONVENTION of this run: the applicable income tax rate in Japan, 31.0% (AFR FY2025 Note 30 reconciliation), for the after-tax add-back of net interest
rows = []
for i, y in enumerate(Y):
    g = lambda k: d[k][i]
    capex = g("ppe_buy")+g("ppe_sell")+g("ip_buy")+g("ip_sell")
    purchases = g("sub_buy")+g("sub_sell")+g("oi_buy")+g("oi_sell")+g("nci_buy")   # cash for businesses, net of businesses sold
    loans = g("loan_coll")+g("loan_incr")
    before_purch = g("ocf")+capex+loans+g("lease_rep")+g("nci_div")              # owner cash before purchases (equity basis, after interest)
    after_purch = before_purch + purchases
    net_int = (g("int_paid")+g("int_recd"))
    allequity_add = -net_int*(1-T)
    rows.append((y, g("ocf"), capex, loans, g("lease_rep"), g("nci_div"), before_purch, purchases, after_purch, allequity_add, g("wc"), g("other_net"), g("dep"), g("profit_par")))
hdr = "year ocf capex(net,PPE+invprop) loans(net) leases nci_div BEFORE_purch purchases(net,incl NCI buyouts) AFTER_purch +net_int_after_tax wc_in_ocf other_net_in_ocf D&A profit_parent"
print(hdr)
for r in rows: print(" ".join(f"{x:>9}" if not isinstance(x,str) else x for x in [r[0]]+[round(v/1000,1) for v in r[1:]]))
w = rows[2:]  # FY2021..FY2025 window
def avg(k): return sum(r[k] for r in w)/len(w)/1000
print("\nwindow FY2021-FY2025 averages (JPY bn):")
for k,n in [(6,"before purchases, equity basis"),(8,"after purchases, equity basis"),(7,"net purchases"),(9,"net interest after tax"),(10,"working capital in OCF"),(11,"other, net in OCF")]:
    print(f"  {n}: {avg(k):.1f}")
print(f"  before purchases, all-equity basis: {avg(6)+avg(9):.1f}")
print(f"  after purchases, all-equity basis: {avg(8)+avg(9):.1f}")
print(f"  before purchases, all-equity, working capital removed: {avg(6)+avg(9)-avg(10):.1f}")
np_ = -sum(r[7] for r in w)/1000; bp = sum(r[6] for r in w)/1000
print(f"\nserial-acquirer test: net purchases {np_:.1f} vs half of owner cash before purchases {bp/2:.1f} -> {'SERIAL' if np_>bp/2 else 'not serial'}")
# halves growth (first two vs last two years of window), before purchases, all-equity
a = [(r[6]+r[9])/1000 for r in w]
print("annual before-purchases all-equity:", [round(x,1) for x in a])
h1 = (a[0]+a[1])/2; h2 = (a[3]+a[4])/2
print(f"first-half avg {h1:.1f}, second-half avg {h2:.1f}, implied annual growth over 3 years {((h2/h1)**(1/3)-1)*100:.1f}%")
