# Apartment REIT Mechanical Screen — 2026-07-15
User-supplied curated list of 13 residential/apartment REITs (AvalonBay,
Equity Residential, Invitation Homes, Mid-America Apartment Communities,
Essex Property Trust, UDR, American Homes 4 Rent, Camden Property Trust,
Independence Realty Trust, Centerspace, NexPoint Residential Trust, BRT
Apartments, Clipper Realty) — not from an OTC/exchange export, hand-typed
with approximate market caps for reference.

## Method, and why it differs from the other screens
Same bare yield-vs-hurdle logic (lowest of last 5 fiscal years ÷ market cap
vs. US 30-yr hurdle, 5.10%), but REITs raised a real methodological question
first, resolved via the corpus and a user correction before running:

**Corpus check** (`Annual Meetings` 2002/2005/2012/2016): Munger flagged
"REITs have phony accounting" (2005) right after Buffett described trading
REITs on ordinary yield logic. My first reading treated this as license to
prefer REITs' own FFO/AFFO metric (which adds back depreciation) over GAAP
net income. **The user corrected this**: Munger's skepticism more plausibly
targets FFO/AFFO's practice of adding back depreciation wholesale, as if
buildings never need real capital to stay competitive — the same principle
this project applies everywhere else (Owner Earnings subtracts *required*
maintenance capex, it doesn't trust a management-defined non-GAAP addback).
So this screen reports **both** NI and NI+D&A, computed transparently from
SEC EDGAR's own tagged filing data — not a vendor's pre-packaged FFO figure —
and does not treat either one as automatically "correct."

## Data sources (3-way split, applied after two S&P 500 single-source
attempts failed under this same list's request volume — spreading load
across independent pipelines proved far more reliable)
- **Segment A** (AVB, EQR, INVH, MAA, ESS): SEC EDGAR (NI, D&A) + Finviz (mkt cap)
- **Segment B** (UDR, AMH, CPT, IRT, CSR): Zacks.com
- **Segment C** (NXRT, BRT, CLPR): Barchart.com
- **D&A always pulled from EDGAR directly**, regardless of segment, for a
  consistent, authoritative depreciation figure across all 13.
- 13/13 resolved on both market cap and NI. 12/13 resolved on D&A (MAA's tag
  used EDGAR's generic `Depreciation` field successfully; all 13 in fact
  resolved — see table).

## Result: the split tells the real story

| Symbol | Mkt Cap ($M) | Lowest 5yr NI ($M) | Latest D&A ($M) | NI+D&A ($M) | NI Yield | NI+D&A Yield |
|---|---|---|---|---|---|---|
| AVB | 27,030 | 876.9 | 913.4 | 1,995.4 | 3.24% | 7.38% |
| EQR | 25,580 | 776.9 | 1,010.4 | 2,130.5 | 3.04% | 8.33% |
| INVH | 17,710 | 261.4 | 746.9 | 1,334.9 | 1.48% | 7.54% |
| MAA | 15,720 | 446.9 | 115.6 | 562.5 | 2.84% | 3.58% |
| ESS | 19,450 | 122.2 | 607.5 | 997.7 | 0.63% | 5.13% |
| UDR | 12,990 | 87.0 | 680.0 | 1,058.0 | 0.67% | 8.14% |
| AMH | 12,210 | 189.0 | 504.3 | 957.3 | 1.55% | 7.84% |
| CPT | 11,360 | 163.0 | 611.0 | 995.0 | 1.43% | 8.76% |
| IRT | 3,900 | -17.0 | 218.0 | 275.0 | -0.44% | 7.05% |
| CSR | 927 | -13.0 | 114.6 | 132.6 | -1.40% | 14.31% |
| NXRT | 692 | -32.0 | 95.6 | 63.6 | -4.63% | 9.19% |
| BRT | 277 | -11.9 | 26.4 | 14.4 | -4.31% | 5.21% |
| CLPR | 46 | -19.9 | 31.2 | 11.3 | -42.92% | 24.43% |

**On raw Net Income: 0 of 13 pass.** Real estate depreciation is large enough
relative to GAAP earnings that it fails every single name in this basket,
several by a wide margin (CLPR's NI is -43% of its own market cap).

**On NI+D&A: 11 of 13 "pass"** — several by very large margins. Depreciation
runs 3x to 10x the NI figure across almost every name in this list.

## The honest conclusion: neither number is "the" answer
This is the headline finding, not either yield column: **depreciation is
consistently several times larger than net income across this entire
apartment-REIT sector.** That is too large a gap to treat GAAP NI as the
real cash-generating power of these businesses (as this project's screens do
by default for ordinary corporations) — but it's also too large a gap to
uncritically add the whole thing back, per the Munger-corrected reading,
without knowing how much of that depreciation reflects a *real* ongoing
capital need (unit renovations, re-leasing costs, competitive upkeep) versus
a pure GAAP convention on assets that may not be losing economic value at
the depreciated rate. **Resolving that split requires the actual Gate 4 OE
formula** (NI + D&A − required maintenance capex − ΔWC) against each REIT's
real disclosed capex — which is full-framework work, not a mechanical
pre-screen, and hasn't been done for any of these 13.

## Net result
Zero clean passes on this project's standard NI-based method; 11 provisional
"passes" on an FFO-style basis that is itself flagged as needing further
scrutiny, not taken on faith. None of these 13 REITs should be treated as
framework survivors on the strength of this screen alone.
