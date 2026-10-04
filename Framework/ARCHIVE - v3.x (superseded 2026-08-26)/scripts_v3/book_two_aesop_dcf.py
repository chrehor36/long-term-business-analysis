# -*- coding: utf-8 -*-
"""
Book Two — the Aesop certainty-spread DCF (Ruling 4, ratified 2026-07-15).

Replaces the WACC/ERP/beta build-up (Convention P43, retired) with a discount
rate sourced directly to Buffett's own stated method:

  - [E4-01] 2000 Letter (Aesop): the discount rate is "the yield on long-term
    U.S. bonds" -- the risk-free/sovereign rate, not a beta-adjusted cost of
    equity.
  - [E3-13] 1994 Annual Meeting: "...discounting future after-tax streams of
    cash at at least a 10 percent rate [vs. 7% bonds]. But that will depend
    on the certainty we feel about the business. The more certain we feel
    about a business, the closer we are willing to play it." -- the spread
    over the sovereign rate is a CERTAINTY judgment, not a formula.
  - [E2-22] 1977 Fortune essay: the "equity coupon" / growing-coupon reading
    -- terminal value uses a modest sustainable growth rate, never the bare
    sovereign rate as a perpetuity input (the error already corrected once
    in this project, see CHANGELOG C10).

Certainty is NOT moat class alone -- [E3-10] (1993 Letter) defines it as
three factors: (1) certainty about the business's long-term economics
[Gates 1-2], (2) certainty about management's competence [Gate 3], and
(3) certainty management channels rewards to shareholders rather than
itself [Gate 3]. So the spread is anchored on Gate 2's moat classification
(factor 1) and then bumped if Gate 3 carried a real caveat (factors 2-3):
  WIDE moat   -> +3.0% over sovereign   [RULING 4-A, 2026-08-01: was +1.0%]
  NARROW moat -> +4.5% over sovereign (midpoint of the amended 4-5% band)
  NONE moat   -> +6.0% over sovereign

  RULING 4-A (2026-08-01) raised these. Ruling 4 had set WIDE at +1% while its
  own note said it was "calibrated off E3-13's 7%->10% example". E3-13 says
  "at least a 10 percent rate" in "a world of 7 percent long-term bond rates" --
  a FLOOR, not a midpoint to discount downward from. Buffett adds "we have to
  feel pretty certain about any business before we're even interested at all",
  so the gates have already filtered before any spread is assigned: a WIDE-moat
  name sits AT the floor, it does not get a discount below it.
  + gate3_caveat_bump (default 0.0; use ~0.0075 i.e. +0.75% if Gate 3 was
    PASS-with-caveats rather than clean -- unverified management, combined
    Chairman/CEO, external/advisor-managed structure, etc.)
These specific numbers are a labeled FRAMEWORK CONVENTION calibrated off
E3-13's own 7%->10% (+3%) example; the certainty-spread STRUCTURE itself --
built from the same three factors as the gate sequence -- is sourced to
E3-10/E3-13/E4-04, not invented.

Fade schedule by moat class reuses the framework's existing convention:
  WIDE -> 15yr fade, NARROW -> 10yr fade, NONE -> 5yr fade.
Terminal growth defaults to 2% (a labeled convention, roughly long-run
inflation) unless overridden per company for a documented reason.
"""

CERTAINTY_SPREAD = {
    "WIDE": 0.030,    # Ruling 4-A (2026-08-01), was 0.010
    "NARROW": 0.045,  # Ruling 4-A, was 0.025
    "NONE": 0.060,    # Ruling 4-A, was 0.045
}

FADE_YEARS = {
    "WIDE": 15,
    "NARROW": 10,
    "NONE": 5,
}

MOS_FLOOR = {
    "WIDE": 0.20,
    "NARROW": 0.20,
    "NONE": 0.30,
}


GATE3_CAVEAT_BUMP = 0.0075  # +0.75%, applied when Gate 3 passed with a real, stated caveat


def discount_rate(sovereign_yield: float, moat_class: str, gate3_clean: bool = True) -> float:
    """
    r = sovereign yield + certainty spread (Ruling 4).
    moat_class in {WIDE, NARROW, NONE} -- Gate 2, certainty factor 1.
    gate3_clean: False if Gate 3 passed WITH a stated caveat (unverified
    management, combined Chairman/CEO, external-advisor structure, etc.) --
    certainty factors 2-3 [E3-10] -- adds GATE3_CAVEAT_BUMP to the spread.
    """
    moat_class = moat_class.upper()
    if moat_class not in CERTAINTY_SPREAD:
        raise ValueError(f"moat_class must be one of {list(CERTAINTY_SPREAD)}, got {moat_class!r}")
    spread = CERTAINTY_SPREAD[moat_class]
    if not gate3_clean:
        spread += GATE3_CAVEAT_BUMP
    return sovereign_yield + spread


def project_cash_flows(oe_base: float, g1: float, moat_class: str, g_terminal: float = 0.02):
    """
    Explicit-period OE projection, fading linearly from g1 (year 1) to
    g_terminal over the moat-class fade window, then flat at g_terminal for
    the terminal-value calc. Returns (list_of_explicit_cfs, final_year_cf,
    fade_years_used).
    """
    moat_class = moat_class.upper()
    n = FADE_YEARS[moat_class]
    cfs = []
    cf = oe_base
    for t in range(1, n + 1):
        # linear fade of the growth rate itself from g1 down to g_terminal
        g_t = g1 + (g_terminal - g1) * (t - 1) / max(n - 1, 1)
        cf = cf * (1 + g_t)
        cfs.append(cf)
    return cfs, cfs[-1], n


def intrinsic_value(oe_base: float, sovereign_yield: float, moat_class: str,
                     g1: float, g_terminal: float = 0.02, net_cash: float = 0.0,
                     gate3_clean: bool = True):
    """
    Full Book Two IV per Ruling 4.
      oe_base       : latest verified owner-earnings tier ($M)
      sovereign_yield: US 30yr or JGB 30yr, as applicable (decimal, e.g. 0.0510)
      moat_class    : "WIDE" | "NARROW" | "NONE"  (certainty factor 1, Gates 1-2)
      g1            : year-1 growth, already = lower of recent OE growth or guidance
      g_terminal    : terminal sustainable growth (default 2%, labeled convention)
      net_cash      : net cash (+) or net debt (-) to add to enterprise PV ($M)
      gate3_clean   : False if Gate 3 passed with a real caveat (certainty
                      factors 2-3, [E3-10]) -- adds the Gate 3 caveat bump
    Returns a dict with r, cfs, terminal_value, pv_explicit, pv_terminal, iv,
    max_buy (IV x MOS floor by moat class).
    """
    r = discount_rate(sovereign_yield, moat_class, gate3_clean=gate3_clean)
    cfs, cf_final, n = project_cash_flows(oe_base, g1, moat_class, g_terminal)

    pv_explicit = sum(cf / (1 + r) ** t for t, cf in enumerate(cfs, start=1))

    if r <= g_terminal:
        raise ValueError(f"Discount rate {r:.4f} must exceed terminal growth {g_terminal:.4f} "
                          f"for the Gordon-growth terminal value to be meaningful.")
    tv_at_n = cf_final * (1 + g_terminal) / (r - g_terminal)
    pv_terminal = tv_at_n / (1 + r) ** n

    iv = pv_explicit + pv_terminal + net_cash
    mos_floor = MOS_FLOOR[moat_class.upper()]
    max_buy = iv * (1 - mos_floor)

    return {
        "discount_rate": r,
        "fade_years": n,
        "explicit_cfs": cfs,
        "terminal_value_at_fade_end": tv_at_n,
        "pv_explicit": pv_explicit,
        "pv_terminal": pv_terminal,
        "net_cash_added": net_cash,
        "intrinsic_value": iv,
        "mos_floor": mos_floor,
        "max_buy": max_buy,
    }


if __name__ == "__main__":
    # Worked example 1: AvalonBay (AVB) -- Statute-only pass from the
    # 2026-07-15 REIT run, OE lowest tier $1,567.478M, mkt cap $27,030M,
    # NARROW moat, US 30yr 5.10%, Gate 3 was clean (orderly CEO succession,
    # documented governance). g1: 3% is an illustrative placeholder pending
    # a real recent-OE-growth pull, not the run's actual anchored figure.
    print("=== AVB (Gate 3 clean) ===")
    result = intrinsic_value(
        oe_base=1567.478, sovereign_yield=0.0510, moat_class="NARROW",
        g1=0.03, g_terminal=0.02, net_cash=0.0, gate3_clean=True,
    )
    for k, v in result.items():
        if k != "explicit_cfs":
            print(f"{k}: {v}")
    print(f"Current mkt cap: 27030  |  IV: {result['intrinsic_value']:.1f}  |  "
          f"Max buy: {result['max_buy']:.1f}")

    # Worked example 2: same inputs, but Gate 3 carried a real caveat (e.g.
    # UDR's combined Chairman/CEO structure) -- shows the certainty-factor-
    # 2/3 bump in isolation.
    print("\n=== Same company, Gate 3 caveat (e.g. combined Chairman/CEO) ===")
    result2 = intrinsic_value(
        oe_base=1567.478, sovereign_yield=0.0510, moat_class="NARROW",
        g1=0.03, g_terminal=0.02, net_cash=0.0, gate3_clean=False,
    )
    print(f"discount_rate: {result2['discount_rate']} (vs {result['discount_rate']} clean)")
    print(f"IV: {result2['intrinsic_value']:.1f}  |  Max buy: {result2['max_buy']:.1f}")


# ---------------------------------------------------------------------------
# RULING 6 (2026-08-01) — THE PRICE LADDER is the required Gate 6 output.
# Never return a bare verdict. Every run states three prices in dollars, three
# diagnostics, and two separate verdicts.
# ---------------------------------------------------------------------------

def price_ladder(iv_per_share, price, mos, base_oe, g1, tgr, r, sovereign,
                 shares, recent_oe):
    """Returns the dict every Gate 6 must record. See Ruling 6."""
    import math
    mc = price * shares
    fair = iv_per_share
    cheap = iv_per_share * (1 - mos)

    def _dcf(base, gg1, tg, rr, yrs=10):
        pv, oe = 0.0, base
        for t in range(1, yrs + 1):
            g = gg1 + (tg - gg1) * (t - 1) / (yrs - 1)
            oe *= (1 + g)
            pv += oe / (1 + rr) ** t
        return pv + (oe * (1 + tg) / (rr - tg)) / (1 + rr) ** yrs

    lo, hi = 0.0001, 1.0                      # IRR at the current price
    for _ in range(300):
        m = (lo + hi) / 2
        if _dcf(base_oe, g1, tgr, m) > mc: lo = m
        else: hi = m
    irr = (lo + hi) / 2

    lo, hi = -0.5, 1.0                        # growth the price already implies
    for _ in range(300):
        m = (lo + hi) / 2
        if _dcf(base_oe, m, tgr, r) < mc: lo = m
        else: hi = m
    implied_g1 = (lo + hi) / 2

    y0 = recent_oe / mc
    yrs_to_sov = (math.log(sovereign / y0) / math.log(1 + g1)
                  if y0 < sovereign and g1 > 0 else None)

    return {
        "CHEAP": cheap, "FAIR": fair, "CURRENT": price,
        "x_fair": price / fair,
        "irr": irr,
        "equity_premium_pts": (irr - sovereign) * 100,
        "implied_g1": implied_g1, "assumed_g1": g1,
        "years_to_sovereign_yield": yrs_to_sov,
        # Ruling 6: these two are recorded SEPARATELY and never merged.
        "BUSINESS_VERDICT": None,   # fill from Gates 1-5
        "PRICE_VERDICT": None,      # fill from the ladder above
    }
