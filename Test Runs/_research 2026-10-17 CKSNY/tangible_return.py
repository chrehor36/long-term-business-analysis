# Pre-tax trading profit on tangible operating capital (PPE + inventories + trade and other receivables
# - trade and other payables), year-end balances from the filed balance sheets; trading profit from the income statements.
B={2016:(323.6,207.7,394.1,239.7,133.3),2017:(311.3,222.8,422.2,292.6,165.5),2018:(303.7,244.3,440.4,311.8,197.2),
   2019:(337.7,212.9,379.6,273.6,181.4),2020:(337.5,187.3,369.9,288.7,101.4),2021:(352.5,299.4,445.2,372.9,142.4),
   2022:(417.6,316.0,476.9,378.4,227.2),2023:(460.8,291.0,460.5,377.8,200.4),2024:(482.6,295.4,438.9,363.4,188.0),
   2025:(539.2,287.3,451.0,359.7,151.1)}
tot_tp=tot_cap=0
for y,(ppe,inv,rec,pay,tp) in B.items():
    cap=ppe+inv+rec-pay; tot_tp+=tp; tot_cap+=cap
    print(y, f"capital {cap:6.1f}  TP {tp:6.1f}  pre-tax {tp/cap*100:5.1f}%")
print("ten-year aggregate", round(tot_tp/tot_cap*100,1),"%")
