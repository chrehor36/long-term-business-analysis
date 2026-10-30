"""Q4: eleven year-end balance sheets (FR2015 to FR2025, each year's own report; MEUR). Ratios to revenue."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
# year: revenue, inventories, trade receivables (current), POC/contract assets, contract liabilities+advances received+billings in excess,
#       equity, goodwill, other intangibles, cash, current investments/financial assets, borrowings (bonds+bank+Schuldschein), total assets
B = {
2015:(6377.2,665.4,735.4,711.1,1045.0+268.8,1215.6,528.5,203.4,1255.7,103.6,365.0+74.8+27.6,5778.0),
2016:(6039.0,736.9,840.1,726.3,1118.0+256.7,1344.2,563.4,201.3,1296.3,110.8,359.3+118.4+78.9,6198.6),
2017:(5889.1,761.0,892.0,599.6,1052.6+277.2,1325.4,547.6,160.7,1071.5,565.8,349.8+424.9+80.9,6265.3),
2018:(6031.5,869.3,974.1,786.4,1003.5+277.1,1330.8,784.6,372.9,858.8,326.0,343.7+922.5+116.4,6918.6),
2019:(6673.9,842.4,931.8,734.1,1230.3+232.0,1219.6,776.9,309.2,1200.8,304.0,1227.0+132.4,7234.1),
2020:(6699.6,761.2,818.3,795.6,895.7+256.6,1255.7,760.0,223.8,1158.0,486.3,1205.1+95.2,7056.7),
2021:(6463.0,905.0,936.8,935.0,1094.1+366.5,1567.3,778.3,190.9,1087.0,670.7,1061.8+74.9,7672.8),
2022:(7542.9,1135.5,1065.1,1047.5,1547.5+400.5,1834.7,787.0,160.1,1302.0,728.9,827.5+253.4,8491.8),
2023:(8660.0,1165.3,1076.0,1239.4,1419.6+357.0,2157.5,826.3,142.8,1507.1,265.1,503.7+429.4,8497.3),
2024:(8313.7,1162.4,1168.8,1099.3,1321.6+342.6,2280.0,860.4,139.9,1164.6,386.8,356.6+172.9,8163.0),
2025:(7883.1,1207.6,1285.5,1093.2,1396.3+429.6,2455.8,1130.3,246.0,911.6,469.8,363.6+184.0,8610.1),
}
print("| Year | Equity | Goodwill + other intangibles | Cash + current investments | Borrowings | Inventories / revenue | Receivables + contract assets / revenue | Advances and contract liabilities / revenue | Total assets |")
print("|---|---|---|---|---|---|---|---|---|")
for y,(rev,inv,rec,ca,cl,eq,gw,ia,cash,ci,bor,ta) in B.items():
    print(f"| {y} | {eq:,.1f} | {gw+ia:,.1f} | {cash+ci:,.1f} | {bor:,.1f} | {inv/rev:.1%} | {(rec+ca)/rev:.1%} | {cl/rev:.1%} | {ta:,.1f} |")
