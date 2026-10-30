# Arithmetic for the CDTG run. Every input is a filed figure (USD as filed, translated by the filer at its stated average rates).
# Sources: 20-F FY2025 0001731122-26-000740; 20-F FY2023 0001731122-24-000803; 424B4 0001731122-24-000653;
# F-1 0001731122-21-000083; F-1/A6 0001731122-22-000538.
ocf   = {2018:-2155783,2019:-2319179,2020:-568854,2021:-129639,2022:-4472780,2023:-3132666,2024:-1987028,2025:-1490957}
sbc   = {2018:0,2019:0,2020:0,2021:0,2022:0,2023:0,2024:454250,2025:2145000}
capex = {2018:129332,2019:94944,2020:28029,2021:101279,2022:53187+33754,2023:21550,2024:3893,2025:2233}
intr  = {2021:58709,2022:64658,2023:106130,2024:137072,2025:89695}   # cash paid for interest
ni    = {2018:2743077,2019:2496129,2020:-1528273,2021:6578260,2022:5242789,2023:7024054,2024:1406282,2025:-10366087}
rev   = {2018:14145960,2019:18732266,2020:8.9e6,2021:23556820,2022:28849362,2023:34209919,2024:29765205,2025:18225819}
avgfx = {2021:6.45,2022:6.73,2023:7.05,2024:7.14,2025:7.19}   # filer's average translation rates, RMB per USD
oc = {y: ocf[y]-sbc[y]-capex[y] for y in ocf}
print('owner cash after interest (OCF - SBC - all capital spending), USD:')
for y in sorted(oc): print(' ', y, f'{oc[y]:>12,.0f}', '  net income', f'{ni[y]:>12,.0f}')
w = range(2021,2026)
eq = sum(oc[y] for y in w)/5
ae = sum(oc[y]+intr[y] for y in w)/5
print(f'5-yr avg equity-only {eq:,.0f}; all-equity (interest added back, no cash tax paid) {ae:,.0f}')
print(f'8-yr avg 2018-2025 equity-only {sum(oc.values())/8:,.0f}; cumulative OCF {sum(ocf.values()):,.0f}; cumulative NI {sum(ni.values()):,.0f}')
# rebase to RMB then to USD at today's CFETS central parity
cny = 6.7147
ae_rmb = sum((oc[y]+intr[y])*avgfx[y] for y in w)/5
eq_rmb = sum(oc[y]*avgfx[y] for y in w)/5
print(f'5-yr avg all-equity RMB {ae_rmb:,.0f} = USD {ae_rmb/cny:,.0f} at {cny}; equity-only RMB {eq_rmb:,.0f} = USD {eq_rmb/cny:,.0f}')
r = 0.020467
sh = 3021000
# net debt at 2025-12-31 (borrowings less cash), then the April 2026 offering's stated net proceeds (~$6.3M) added as a subsequent event
borrow = 1153654+2057311+2560675+357495
cash = 66686
nd = borrow - cash - 6300000
print(f'borrowings {borrow:,.0f}; net debt after the stated April 2026 net proceeds {nd:,.0f}')
AE = ae_rmb/cny; EQ = eq_rmb/cny
v_sov = AE/r; v_10 = AE/0.10
print(f'no-growth all-equity value at sovereign {v_sov:,.0f}; per share {(v_sov-nd)/sh:,.2f}')
print(f'fair price (no-growth case alone, at 10%) all-equity per share {(v_10-nd)/sh:,.2f}; equity-only {(EQ/0.10)/sh:,.2f} (cash raise excluded), {(EQ/0.10 + 6300000+cash)/sh:,.2f} (raise and cash added)')
print('AR+contract assets / revenue:')
arca = {2018:8915213+2295309,2019:18359298+4781953,2020:11678088+4352489,2021:14671310+15677452,2022:20090775+26090390,2023:29076549+39165839,2024:45188231+39989358,2025:44128933+39309995}
for y in sorted(arca): print(' ', y, f'{arca[y]/rev[y]:.2f}')
price = 1.01
print(f'market cap at ${price}: {price*sh:,.0f}')
