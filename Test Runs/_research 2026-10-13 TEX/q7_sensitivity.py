exec(open('q7_computation.py').read().split('out = []')[0])
ev_price = PRICE * SHARES + NET_DEBT
def irr(c, gg):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(c, gg, mid) > ev_price: lo = mid
        else: hi = mid
    return mid
g = 0.0230
print("default pair (acquisitions deducted, total growth 8.67%%): per share at 5.6%%: %.2f, at 10%%: %.2f" % (per_share(pv(42.7, 0.0867, R)), per_share(pv(42.7, 0.0867, FLOOR))))
for lab, c in (("2025 only, all-spending", 401.7 + 191.1), ("2025 only, maintenance-only", 447.7 + 217.9), ("2024-2025 avg all-spending", (190.2+401.7)/2 + (31.1+191.1)/2)):
    for gl, gg in (("no growth", 0), ("organic 2.30%", g)):
        print("%-30s %-14s value/share at 5.6%% %6.2f  at 10%% %6.2f  return at price %.2f%%" % (lab, gl, per_share(pv(c, gg, R)), per_share(pv(c, gg, FLOOR)), irr(c, gg)*100))
