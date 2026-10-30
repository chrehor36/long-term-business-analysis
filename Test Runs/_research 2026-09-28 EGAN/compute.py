sh=26.171467; cash=73.336; cap=5.67*sh; ev=cap-cash
ni={2017:-1.7,2018:-1.0,2019:-0.3,2020:0.4,2021:0.0,2022:0.1,2023:2.4,2024:3.8,2025:2.5,2026:2.2}  # InterestIncomeExpenseNonoperatingNet
oe={2017:4.24,2018:4.76,2019:4.93,2020:11.68,2021:11.76,2022:-3.89,2023:-1.91,2024:7.73,2025:2.25,2026:16.38}
def w(n): ys=range(2027-n,2027); return sum(oe[y] for y in ys)/n, sum(ni[y] for y in ys)/n
cases={'5y':w(5),'10y':w(10),'3y':w(3),'FY26':(16.38,2.2),'FY26exAR':(16.38-8.026,2.2)}
print('cap',round(cap,1),'ev',round(ev,1))
for k,(o,i) in cases.items():
    op=o-i
    print(f'{k}: OE {o:.2f} interest {i:.2f} operating {op:.2f} | no growth/10% {(op/0.10+cash)/sh:.2f} | 5%g/10% {(op/0.05+cash)/sh:.2f} | op/EV {100*op/ev:.1f}%')
print('buybacks', 5.763/0.786, 17.268/2.752, 15.781/2.616, 11.510/1.607, 50.322/7.761)
print('SBC share FY2022 of OCF', 11.38/8.121)
