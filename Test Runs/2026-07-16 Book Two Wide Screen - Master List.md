# Book Two Wide Screen — Full Master List — 2026-07-16
Ruling 4's Aesop certainty-spread DCF applied as a **wide mechanical
screen** (the ruling explicitly contemplates this: same two core inputs —
sovereign yield, moat class — as the Statute screens) to all 51 confirmed
Statute passes that did not yet have Book Two, plus CB. This document is
the Book Two addendum of record for these names; individual run files are
not separately edited (51 files), consistent with how the mechanical
screens are documented once, centrally.

## Method (documented conventions, applied uniformly)
- **Discount rate** = sovereign yield + certainty spread [E3-13/E3-10]:
  US names 5.10%, Japan names raw JGB 3.76% (not the 4.00% Statute floor —
  Book Two uses the actual bond yield per E4-01). NARROW +2.5%, NONE +4.5%.
  **Gate-3 caveat bump +0.75% applied to every name here except CB** — all
  had provisional/unverified Gate 3s (certainty factors 2-3). CB's Gate 3
  was a real proxy read (clean) → 7.60%.
- **Moat class** from each run file's Gate 2. Mixed/"NONE-to-NARROW"
  classes resolved conservatively to **NONE** (wider spread, 5-yr fade,
  30% MOS): NPNYY, UNTC, MZDAY, IPXHY, RICOY, DNPLY, CAJPY, MAURY.
- **OE base** = each run's lowest verified tier (full-formula OE for the
  S&P batch; NI-proxy convention for Japan/UNTC, as documented in those
  runs).
- **g1** = LOWER of most-recent-YoY OE growth vs. multi-year CAGR from the
  run file's tier table. Japan/UNTC names (no OE series) use the 2%
  terminal-rate convention — i.e., no above-terminal growth assumed.
- **Terminal growth** 2% [E2-22 growing-coupon]. Fade: NARROW 10yr, NONE 5yr.
- **Gate 8** (for names Book Two clears): implied g1 at current price;
  bear case g1 = min(-5%, g1−5pp); asymmetry ≥2:1 required.
- **Scream-Test-style robustness check**: any name whose BUY-ELIGIBLE
  verdict came from a g1 anchor ABOVE 2% was re-run at the 2% floor. **If
  the verdict flips at 2%, it is classified as growth-dependent — WHISPER —
  and stays STATUTE-ONLY**, per the Scream Test principle (verdicts must
  agree across constructions or you pass).

## RESULT 1 — Robust BUY-ELIGIBLE: clears both books AND the 2% floor AND Gate 8 (18 names)

### US (8)
| Ticker | r | g1 anchor | IV ($M) | Max buy ($M) | Mkt cap ($M) | Gate 8 | Caveats |
|---|---|---|---|---|---|---|---|
| CTSH | 8.35% | 0.0% | 38,409 | 30,727 | 20,460 | fav/undef | GCC-insourcing moat erosion named |
| SYF | 8.35% | +1.5% | 35,214 | 28,172 | 24,784 | fav/undef | card lender: credit-cycle [P]s, one [U] |
| UHS | 8.35% | +30.5%* | 39,157 | 31,326 | 8,731 | fav/undef | *survives at 2% floor (IV $12,598 vs cap $8,731); leverage + conduct-history [U] open |
| ACN | 8.35% | +3.5% | 136,856 | 109,485 | 83,850 | fav/undef | FY2025 D&A gap (anchor likely understated) |
| VZ | 8.35% | +0.8% | 252,494 | 201,996 | 177,336 | fav/undef | anchored to real impairment year |
| CMCSA | 8.35% | +24.2%* | 471,679 | 377,343 | 83,910 | fav/undef | *survives at 2% floor (IV $193,052); FY2022 anchor cause unconfirmed, media segment unassessed — the widest margin AND the weakest-verified anchor in this table |
| PYPL | 8.35% | +18.9%* | 113,784 | 91,027 | 41,785 | fav/undef | *survives at 2% floor (IV $57,176) |
| UNTC | 10.35% | +2.0% | 508 | 355 | 304 | fav/undef | NONE moat; single-tier anchor; replaces the retired WACC-era Book Two |

### Japan (10) — all g1=2% (already the conservative floor), NI-proxy OE
| Ticker | r | IV ($M) | Max buy ($M) | Mkt cap ($M) | Gate 8 | Caveats |
|---|---|---|---|---|---|---|
| SKHSY | 7.01% | 28,523 | 22,819 | 13,940 | fav/undef | demographic headwind |
| ISUZY | 7.01% | 18,059 | 14,447 | 9,830 | fav/undef | EV-transition risk |
| DIFTY | 7.01% | 10,729 | 8,584 | 6,710 | fav/undef | **guarantee-liability capital coverage still open — resolve before entry** |
| HTCMY | 7.01% | 9,834 | 7,867 | 7,080 | fav/undef | |
| SGIOY | 7.01% | 20,685 | 16,548 | 15,200 | ~fav | **weakest evidence base in Japan batch** |
| BRDCY | 7.01% | 38,296 | 30,637 | 30,120 | 4.12:1 | |
| KDDIY | 7.01% | 89,601 | 71,681 | 69,370 | 5.72:1 | regulatory pricing pressure |
| KUBTY | 7.01% | 24,492 | 19,594 | 19,000 | 5.47:1 | |
| OTSKY | 7.01% | 46,114 | 36,891 | 36,670 | 3.39:1 | thin margin over max-buy |
| NPNYY | 9.01% | 20,342 | 14,239 | 13,400 | fav/undef | **shipping-cycle peak flag — the "lowest 5yr NI" may itself be cyclically inflated; treat this mechanical pass with the most suspicion in this table** |

## RESULT 2 — Growth-dependent: clears at the anchored g1 but FLIPS at the 2% floor → WHISPER, stays STATUTE-ONLY (5)
| Ticker | g1 anchor | Verdict at anchor | Verdict at 2% floor |
|---|---|---|---|
| ZTS | +7.3% | BUY-ELIGIBLE | above max-buy |
| FOX | +20.3% | BUY-ELIGIBLE (asym 7.73:1) | above max-buy |
| FOXA | +20.3% | BUY-ELIGIBLE (asym 4.37:1) | above max-buy |
| ADBE | +12.9% | BUY-ELIGIBLE (asym 2.07:1) | **above IV entirely** |
| CB | +8.9% | BUY-ELIGIBLE (asym 4.96:1) | above max-buy — and Ruling 1 still blocks any entry regardless |

## RESULT 3 — Below IV but above the MOS-floored max buy → STATUTE-ONLY stands (8)
TROW ($27,356 IV vs $24,870 cap), GL ($14,334 vs $13,900 — and the conduct
[U] outranks the arithmetic anyway), FUJIY ($26,507 vs $26,490 —
essentially AT IV), DNPLY, SZKMY, NHNKY, FUJHY, IPXHY.

## RESULT 4 — Above Book Two IV entirely → Scream Test disagreement, effectively WAIT (22)
US: DHI, IT (Gartner — IV $2,496 vs cap $8,900, the starkest gap in the
batch: the -37% g1 anchor collapses the DCF, consistent with the
already-visible AI-erosion), NVR, HON, TSCO, BF.B, LULU, ELV, AFL (the
unexplained FY2025 drop feeds a -32.9% g1 — resolving WHY it dropped could
change this materially), UPS, REGN, GEHC, LOW, BLDR, BBY, CDW.
Japan: MZDAY, RICOY, NDEKY, MAURY, CAJPY, FJTSY.

**Note the pattern**: names whose Book One pass was anchored to a genuine
cyclical trough (DHI, NVR, BLDR, CDW, AFL) fail Book Two precisely BECAUSE
the framework's own anchoring rule feeds the trough-driven negative growth
into g1. This is conservative by design — a cyclical at its trough with
collapsing trailing OE must be cheap enough to clear even a
continued-decline projection, or it waits. If any of these post a
recovery year, their g1 anchors and verdicts change on the next pass.

## What changed vs. the mechanical screens
Book One passed all 51 of these. Book Two, applied with the framework's own
anchoring discipline: **18 robust clears, 5 growth-dependent whispers, 8
in the no-man's-land between IV and max-buy, 22 effective WAITs.** The
dual-book design is doing exactly what Ruling 4 intended — the bare
yardstick finds candidates; the certainty-spread DCF (with the trough-
anchored g1 rule) sorts genuine cheapness from statistical cheapness.

## Standing caveats on the whole exercise
1. Every clear here is a **mechanical wide-screen result**, not a deep-dive
   dual-book clearance. Each run file's open items (unverified management
   [U]s, NI-proxy OE for Japan, data gaps) still stand and are NOT cured by
   Book Two arithmetic.
2. Gate 8 was computed inside this screen for clearing names; entry sizing
   (Gate 7) remains a per-name decision the user makes, with the caveat
   column above binding.
3. NPNYY, DIFTY, SGIOY, UHS, GL carry caveats serious enough that this
   document recommends resolving them before any entry regardless of the
   arithmetic.
