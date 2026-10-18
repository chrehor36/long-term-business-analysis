# Owner cash from the filed consolidated cash flow statements (R$ million), continuing operations.
# Sources: FY2025 20-F (0001439124-26-000013) for 2025, 2024, 2023; FY2023 20-F (0001104659-24-052084) for 2022, 2021.
Y = [2021, 2022, 2023, 2024, 2025]
ocf      = dict(zip(Y, [7565.8, 8104.3, 8235.3, 12385.6, 14509.8]))   # net cash from operating activities, continuing
mkt_sec  = dict(zip(Y, [2561.5, 1499.9, 0, 0, 0]))                   # marketable-securities purchases inside OCF (2021-22 as restated), added back
int_paid = dict(zip(Y, [2176.1, 3211.3, 5512.4, 6650.9, 5831.6]))    # payment of interests (incl. CDE interest from 2024)
ppe      = dict(zip(Y, [1085.1, 1585.6, 3862.8, 3099.5, 2065.5]))
intang   = dict(zip(Y, [103.5, 32038.8, 258.4, 425.9, 443.2]))       # 2022 includes the concession grant of the privatization
trans    = dict(zip(Y, [1299.7, 1653.0, 3269.4, 4286.9, 4914.9]))    # transmission infrastructure, contractual asset
lease    = dict(zip(Y, [571.8, 721.1, 765.5, 757.2, 51.0]))
acq      = dict(zip(Y, [274.4 + 2447.5, 74.3, 1439.5, 176.6, 247.7 + 320.6]))  # acquisitions/capital injections (2021 incl. advance for future capital increase)
int_recv = dict(zip(Y, [672.1 + 589.1, 316.3 + 3764.0, 172.5 + 4066.5, 57.7 + 529.8, 209.7 + 741.0]))  # financial charges + interest on securities received (investing)
cde_tot  = dict(zip(Y, [0, 0, 1433.8, 1975.0 + 239.1, 2575.6 + 434.1]))   # CDE + basin payments; 2023 interest not split out (in interest paid)
cde_int  = dict(zip(Y, [0, 0, 0, 239.1, 434.1]))
rev      = dict(zip(Y, [34627, 34074, 37159, 40182, 41282]))
grant2022 = 32038.8 - 103.5  # privatization concession payment inside 2022 intangibles, approx (intangibles less the 2021 run-rate)
rows = {}
for y in Y:
    capex = ppe[y] + intang[y] + trans[y]
    allеq = ocf[y] + mkt_sec[y] + int_paid[y] - capex - lease[y] - acq[y]
    eq = allеq - int_paid[y] + cde_int[y] + int_recv[y] - cde_tot[y]   # after interest paid (ex CDE), after all CDE payments, plus interest received
    rows[y] = (capex, allеq, eq)
    print(y, f"OCF {ocf[y]:8.0f} capex {capex:8.0f} all-equity {allеq:8.0f} equity-only {eq:8.0f}  ex-grant all-eq {allеq + (grant2022 if y == 2022 else 0):8.0f} eq {eq + (grant2022 if y == 2022 else 0):8.0f}  rev {rev[y]}")
avg = lambda xs: sum(xs) / len(xs)
print("5y avg all-equity", avg([rows[y][1] for y in Y]), "equity-only", avg([rows[y][2] for y in Y]))
print("5y avg ex-grant all-equity", avg([rows[y][1] + (grant2022 if y == 2022 else 0) for y in Y]), "equity-only", avg([rows[y][2] + (grant2022 if y == 2022 else 0) for y in Y]))
