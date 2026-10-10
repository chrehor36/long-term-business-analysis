# Q7 range, all-equity basis (CONVENTION of v5 Q7 and its specifics). USD M. Inputs from ownercash.py, segments.py and the 10-Q Q2 2026.
r = 0.0564            # 30-yr Treasury par yield 2026-10-06
shares = 63.581       # cover 2026-07-27
price = 120.25
net_debt = 217.540 + 31.699 + 1118.415 - 190.402 - 6.864   # borrowings (finance leases inside) less cash and short-term investments, 2026-06-30
minority = 27.722 + 18.430                                  # redeemable and other noncontrolling interests, 2026-06-30
claims = net_debt + minority
def pv(stream_fn, rate, years=10, terminal_fn=None):
    v = sum(stream_fn(t)/(1+rate)**t for t in range(1, years+1))
    if terminal_fn: v += terminal_fn()/rate/(1+rate)**years
    return v
def case(M, S, share_growing, g, rate):
    """M: maintenance-basis owner cash; S: growth spending (growth capex + acquisitions), charged to the growing part;
    share_growing: share of M in the deciding part (Pharma); the rest carried at no growth (section B)."""
    Mg = M*share_growing; Mo = M - Mg
    other = Mo/rate
    grow = pv(lambda t: (Mg - S)*(1+g)**t, rate, 10, lambda: Mg*(1+g)**10)
    return other + grow
def nogrowth(M, rate): return M/rate
out=[]
def report(label, M, S, sh, g):
    lo = nogrowth(M, r); hi = case(M, S, sh, g, r)
    a, b = sorted([lo, hi])
    ps = lambda ev: (ev - claims)/shares
    # fair price: midpoint of the two cases valued at the floor of ~10% (CONVENTION), all-equity basis
    f_lo = nogrowth(M, 0.10); f_hi = case(M, S, sh, g, 0.10)
    fair_ev = (f_lo + f_hi)/2
    out.append(f"{label}: EV range {a:,.0f} to {b:,.0f} (no-growth {lo:,.0f}; growth case {hi:,.0f}); per share {ps(a):.2f} to {ps(b):.2f}; "
               f"width {b/a:.2f}x; fair EV at 10% {fair_ev:,.0f} -> {ps(fair_ev):.2f}/sh")
    return a,b,fair_ev
print(f"net debt {net_debt:.1f}, minority {minority:.1f}, market cap {price*shares:,.0f}, EV at market {price*shares+claims:,.0f}")
sh = 0.771  # Pharma share of segment profit 2019-2025 (segments.py)
for label, M, S in [("cycle 2019-25", 318.9, 318.9-146.9), ("literal window 2021-25", 300.4, 300.4-150.5)]:
    for g in (0.050, 0.088, 0.103):
        report(f"{label}, g={g:.1%}", M, S, sh, g)
# equity-only beside: owner cash after interest, no-growth and growth, against market cap
Meq = 318.9 - 29.2
lo = Meq/r; hi = case(Meq, 172.0, sh, 0.050, r)
out.append(f"equity-only (cycle, g=5.0%): {lo:,.0f} to {hi:,.0f} -> per share {lo/shares:.2f} to {hi/shares:.2f}; fair at 10%: {((Meq/0.10)+case(Meq,172.0,sh,0.05,0.10))/2/shares:.2f}")
# expected return at the price: the rate at which the central cycle case equals EV at market
evm = price*shares + claims
for g in (0.0, 0.05):
    lo_, hi_ = 0.0001, 0.5
    f = (lambda rate: nogrowth(318.9, rate)) if g == 0 else (lambda rate: case(318.9, 172.0, sh, g, rate))
    for _ in range(100):
        mid = (lo_+hi_)/2
        if f(mid) > evm: lo_ = mid
        else: hi_ = mid
    out.append(f"rate at which the cycle case (g={g:.0%}) equals EV at market {evm:,.0f}: {mid:.2%}")
print("\n".join(out))
