# BACKTEST RESULTS — Wider Universe Test — 2026-07-22
Follow-up to `2026-07-22 BT-0-1-2 Results...md`, answering that report's
own "What's next" item: is the original 36-name universe's coin-flip win
rate and value-trap concentration real, or an artifact of a small,
manually-selected list?

## METHOD
- **New sample**: 132 S&P 500 names, systematically drawn (every 3rd ticker
  alphabetically) from the **396 non-Financials/non-Real-Estate** S&P 500
  constituents (Wikipedia's live constituent table, which conveniently
  includes GICS sector — Financials and Real Estate excluded the same way
  this project has excluded banks/REITs throughout, since leverage-based and
  FFO-based earnings don't fit a plain E/P screen). This list was **not**
  cherry-picked from prior project work — it overlaps the original 36-name
  universe in only 10 names (ADBE, CDW, COP, HD, HON, HPQ, IT, REGN, SWKS,
  UHS).
- Identical pipeline, identical discipline, to the original test: SEC XBRL
  facts gated on `filed` date, worst-of-trailing-5-FY NI, 30yr Treasury
  hurdle floored at 4%, no size premium (all large/mega-cap), June 30
  rebalances 2013-2025, 1-year hold, SPY benchmark.
- Combined dataset: the two universes merged and deduplicated by
  ticker+year → **142 unique companies actually producing usable
  observations**, 1,451 total screen-year rows, 630 coverage gaps logged
  across both passes (mostly recent IPOs/spinoffs without 5 filed years yet
  early in the window — DASH, ABNB, KVUE, GEHC, and 2025 spinoffs FDXF/Q
  among them).

## RESULT: THE COIN-FLIP REPLICATES. THE VALUE-TRAP STORY GETS MORE NUANCED.

| Universe | n (passes) | Win rate vs SPY | Mean excess | Median excess |
|---|---|---|---|---|
| Original 36 | 71 | 49.3% | +0.88pp | **-1.38pp** |
| Wide 132 (new, independent) | 212 | 50.5% | +4.31pp | +0.43pp |
| **Combined 142 unique** | **270** | **51.1%** | **+4.04pp** | **+0.71pp** |

**The core finding replicates and gets stronger, not weaker, with scale**:
across three separate cuts of increasing size, the win rate against SPY sits
at 49-51% — a coin flip, full stop. That result did **not** depend on the
original small, manually-chosen list; a completely independent, mechanically
sampled 132-name universe reproduces it almost exactly. **That's the load-
bearing conclusion, now confirmed out-of-sample.**

The median excess return, however, flips from negative (-1.38pp) in the
narrow list to slightly positive (+0.71pp combined) in the broader one — a
real difference, small in magnitude (well inside the noise: individual-
observation standard deviation of excess return is ~44 percentage points),
but honest to report rather than paper over. **The original list's
specifically negative median was partly an artifact of that particular
36-name selection**, not a universal property of bare E/P screens.

## CONCENTRATION: STILL REAL, BUT THE COMPOSITION IS MORE INTERESTING
Only 70 of the 142 usable names ever passed, and the **top 10 recurring
passers still account for a third of all pass-observations (90/270 =
33.3%)** — almost identical concentration, proportionally, to the original
test. But the top-10 list itself is revealing:

| Ticker | Years passed | Character |
|---|---|---|
| CMCSA | 12/13 | Cable/telecom — the original test's top name, structural decline concern |
| **BKNG** | 11/13 | **Booking Holdings — a genuinely well-regarded moat business**, mechanically "cheap" mainly in the years its trailing NI anchor was depressed (COVID-era travel collapse) |
| GIS | 11/13 | General Mills — slow-growth packaged foods, margin pressure |
| TSCO | 10/13 | Tractor Supply — repeat from the original test |
| INTC | 9/13 | Intel — textbook structural-decline case (x86/foundry share loss) |
| CSX, EXC, HPQ, TROW, FAST | 7-8/13 each | Rail, regulated utility, legacy hardware, asset management, industrial distribution |

**This is the cleanest demonstration yet of why Gates 2-5 exist.** The
mechanical screen cannot distinguish BKNG (a real business temporarily
statistically cheap because of a demand shock) from INTC (a real business
getting structurally worse) — both trip the same trailing-earnings-yield
trigger for the same mechanical reason. Only the qualitative gates (moat
durability, management, inversion) can tell them apart, and that's exactly
the judgment a bare Book One pass is not equipped to make alone.

## WHAT THIS CHANGES ABOUT THE ORIGINAL WRITE-UP
- The **"coin-flip win rate, no reliable edge"** conclusion is now
  **strengthened** — it replicated cleanly out-of-sample.
- The **"the screen only finds value traps"** framing was too strong — the
  repeat-passer list is a mix of true structural decliners and temporarily
  cheap, genuinely good businesses (BKNG). The corrected claim: **a bare
  E/P screen cannot tell the two apart, which is the actual problem Gates
  2-5 solve** — not that the screen is *only* finding bad businesses.
- No PENDING RULINGS escalation triggered by this result — it refines the
  prior finding's language rather than contradicting the framework's design.

## LIMITATIONS (same as before, restated for this run)
- Financials/Real Estate excluded via GICS sector label, not independent
  verification — matches this project's standing "ignore banks" convention.
- Survivorship bias still present (today's S&P 500 constituents only) and,
  if anything, still flatters the passes.
- NI-proxy, not full owner-earnings formula — same stated scope as B1.
- 2025 spinoffs (FDXF, Q/Qnity) appeared in the systematic sample with zero
  usable history — logged, not silently dropped, contributed nothing to the
  result either way.

## WHAT'S NEXT
B2 (Graham's 2×AAA bar), B3 (the whisper filter — does requiring a Book Two
pass alongside Book One separate BKNG-type cases from INTC-type cases within
the repeat-passer list?), B4 (sell rules). B3 is now the most interesting
open question this result raises.

## SELF-AUDIT
- [x] Independent, non-cherry-picked sample (systematic draw from GICS
  sector data, only 10/132 overlap with the original list)
- [x] Coverage gaps logged (630 combined), not hidden
- [x] Result reported as found, including where it revises the prior
  write-up's framing rather than just confirming it
- [x] Raw results (wide + combined), coverage log, and scripts committed
