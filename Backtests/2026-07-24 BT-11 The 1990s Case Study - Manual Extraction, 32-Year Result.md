# BACKTEST BT-11 — The 1990s Case Study: Manual Extraction, a 32-Year Result — 2026-07-24

The user's explicit ask: push the point-in-time framework back toward 1990,
manually, across as many businesses as possible, and build every possible
10-business portfolio from the survivors — a genuinely massive, long-
horizon case study. This is that study. **The result is the most sobering
finding this project has produced, and it is reported in full, not
softened.**

## THE HARD DATA WALL, AND HOW FAR THROUGH IT THIS GOT
XBRL (the SEC's structured financial-data format every earlier backtest
this session was built on) did not exist in 1990 — it wasn't mandated
until 2009. EDGAR itself only phased in as mandatory between 1993 and
1996; before that, filings exist only on paper. There was never a
scriptable, API-driven path to 1990 the way there was to 2013 or 2018.
Getting there required doing the manual extraction by hand, at scale.

**What was actually done**:
- Of 403 resolved companies, **190 (47%) have EDGAR 10-K history reaching
  back before 1996** (into EDGAR's earliest voluntary/pilot years).
- Fetched each of those 190 companies' **earliest available 10-K**
  (mostly 1994-1995 vintage) and located its **Item 6 "Selected Financial
  Data" table** — a mandatory 5-year summary financial table every 10-K
  carries, which for a 1994 filing reaches back to **1990** directly.
- **First extraction pass**: only 45 of 187 (24%) yielded real numbers —
  the rest were "incorporated by reference to the Annual Report," a common
  1990s filing practice where the table lived in a printed document, not
  the EDGAR text itself.
- **Second pass, a genuine methodology fix, not just more effort**: a
  research pass investigating one failure (KLA-Tencor) found the real
  table wasn't missing — it was filed as **Exhibit 13** (the Annual
  Report, attached in full to the same submission) later in the same
  document, and the original extraction script only checked the *first*
  mention of "Selected Financial Data" (usually just the referencing
  sentence), never continuing to search the rest of the filing. Rewrote
  the search to check every occurrence across every attached exhibit and
  prefer the one actually followed by a table. Re-ran this on all 142
  previously-failed tickers: **recovered real data for 69 more —
  114 of 187 tickers (61%) ended up with at least one usable year**,
  more than double the first pass.
- Every extraction ran through parallel research agents instructed
  explicitly not to fabricate: unparseable snippets were logged as
  `UNKNOWN` with the specific reason (still incorporated-by-reference,
  wrong entity, garbled OCR, subsidiary-only data) rather than guessed.

## THE MECHANICAL SCREEN, AND TWO REAL BUGS CAUGHT BEFORE TRUSTING THE NUMBERS
Anchored the screen at **1993-12-31** (the best 5-year trailing window for
company coverage — 1989-1993 — not literally 1990, the same kind of
forced, disclosed date adjustment as BT-8's 2013→2018 shift), using
worst-of-trailing-NI-in-window ÷ market cap vs. the 30-year Treasury
yield (6.35% as of that date).

Two data bugs were found and fixed before any result was trusted, exactly
the discipline this project has maintained throughout:
1. **A share-count unit bug**: 1990s tables caption "all amounts in
   thousands, except per-share amounts" — the share count is subject to
   that multiplier too, but the first version of the script used a
   magnitude-guessing heuristic instead of applying it, producing
   nonsense market caps.
2. **A much larger, systemic problem**: Yahoo's historical price series is
   split-adjusted forward to today. A price quoted for 1993 has already
   been divided by every stock split since then — Apple alone has split
   5 times (cumulative 224x) since 1993. Multiplying that adjusted price
   by the *real* 1993 share count (from the filing) without reversing the
   split adjustment produces a market cap wrong by orders of magnitude.
   Fixed by reading each ticker's split-event history and multiplying
   back by the cumulative ratio of every split after the target date —
   but this exposed that **many cached price files were missing their
   split history entirely** (an incomplete-events problem in how the data
   was originally fetched earlier this session, not a one-off). A
   **P/E sanity check** (does the recovered price imply a plausible 3-60x
   multiple against the company's own disclosed EPS?) caught this
   directly — MO and PFE's initial "prices" implied a P/E of 0.2-0.8x,
   an impossibility, confirming the split data was incomplete rather than
   silently accepting a corrupted number. **Refetching all 114 tickers'
   price history with an explicit, full-range split-events query** (a
   direct, provable fix — verified against MO's real 5-split history
   before trusting it at scale) recovered clean, sane prices for the
   large majority: coverage rose from 28 screenable (mostly wrong) to
   **66 screenable, with plausible market caps throughout**.

## RESULT: 16 PASS BOOK ONE, 12 PASS THE FULL FRAMEWORK
16 of 66 screened names cleared the mechanical yield hurdle: WEC
(Wisconsin Energy), MMM (3M), WFC (Norwest Corp — see identity note
below), GL (Torchmark, the ancestor of today's Globe Life), EMR (Emerson
Electric), HBAN (Huntington Bancshares), LNC (Lincoln National), NTRS
(Northern Trust), PFE (Pfizer), HRB (H&R Block), PCAR (Paccar), OMC
(Omnicom), MCD (McDonald's), GWW (W.W. Grainger), STT (State Street), C
(Primerica Corporation / The Travelers Inc — see identity note below).

**Two identity notes, found and disclosed rather than silently
mishandled**: the ticker "WFC" in 1993 belongs to **Norwest
Corporation**, a Minneapolis bank holding company — Norwest acquired the
original, separate Wells Fargo & Co. in 1998 and took its name, but the
1993-era entity is Norwest, not the pre-1998 Wells Fargo brand. The ticker
"C" in 1993 belongs to **Primerica Corporation**, days away from closing
its acquisition of Travelers Corp and renaming itself Travelers Inc. (the
lineage that eventually became today's Citigroup after the 1998 Citicorp
merger) — not Citicorp or modern Citigroup. Both were flagged explicitly
to the qualitative-gate research so judgments were made about the real
1993 businesses, not their modern namesakes.

**Genuine Gates 1/2/3/5 research** (point-in-time, 1993-12-31, no
hindsight in either direction) eliminated 4 of the 16:
- **LNC (Lincoln National) — FAILS GATE 1**: an otherwise-evaluable
  life/annuity insurer carries an opaque, long-tail P&C reinsurance
  runoff (the 1984-1990 National Re exposure) whose reserve adequacy an
  outside analyst genuinely cannot verify from 1993 disclosures — the
  same exposure independently scored Dangerous on the Gate 5 balance-
  sheet inversion.
- **PFE (Pfizer) — FAILS GATE 3**: the Shiley heart-valve disclosure
  failure (Pfizer's Shiley Inc. subsidiary did not adequately disclose
  fracture-risk data to the FDA before the valve began fracturing
  fatally; $165-215M settlement approved 1992) is a confirmed, adjudicated
  deceptive-disclosure violation, fully knowable by year-end 1993 — the
  framework's binary integrity rule disqualifies it regardless of the
  otherwise-durable patent moat.
- **OMC (Omnicom) — FAILS GATE 2**: a well-run advertising holding
  company, but a "people business" where the core assets (creative
  talent, client relationships) can walk out the door — doesn't clear the
  franchise test's structural-barrier bar.
- **C (Primerica/Travelers) — FAILS GATE 1**: a freshly-assembled,
  four-way financial conglomerate (consumer finance + captive-agent life
  insurance + a just-acquired, recently-real-estate-loss-impaired P&C
  insurer + retail brokerage) with no combined operating history at the
  valuation date — exceeds a reasonable circle of competence regardless
  of Sandy Weill's individually strong capital-allocation reputation.

**12 survive all gates**: WEC, MMM, WFC, GL, EMR, HBAN, NTRS, HRB, PCAR,
MCD, GWW, STT.

## THE RESULT: EVERY ONE OF THE 66 POSSIBLE 10-BUSINESS PORTFOLIOS, OVER 32.6 REAL YEARS
All 12 survivors are still independently, continuously trading today —
no corporate-action complications (unlike BT-9's 2018 cohort, nothing
here was acquired, went bankrupt, or went private). Every C(12,10) = 66
possible 10-business portfolio was computed exhaustively.

| | |
|---|---|
| **Beat SPY (10.73% CAGR)** | **0 / 66 (0.0%)** |
| Mean portfolio CAGR | 7.19% |
| Median portfolio CAGR | 7.36% |
| Worst possible portfolio | 5.81% |
| Best possible portfolio | 7.68% |
| SPY, same window (1993-12-31 → today, 32.6 yrs) | 2,664% total, **10.73% CAGR** |

**This is the opposite of BT-10's finding, and it is reported exactly as
found.** Individual survivor CAGRs, for context:

| Ticker | CAGR | Beat SPY (10.73%)? |
|---|---|---|
| GWW (Grainger) | **11.97%** | Yes — the only one |
| MCD | 7.03% | No |
| NTRS | 6.93% | No |
| STT | 6.88% | No |
| WFC (Norwest) | 6.77% | No |
| PCAR | 5.95% | No |
| GL (Torchmark) | 5.90% | No |
| EMR | 5.45% | No |
| WEC | 8.38% | No |
| HRB | 3.11% | No |
| MMM | 4.30% | No |
| HBAN | 2.69% | No |

Only **one of twelve** individual survivors beat the index over 32.6
years. Every one of them still multiplied an original dollar several-fold
in absolute terms (GWW turned $1 into ~$39; even the weakest, HBAN, turned
$1 into ~$2.37) — this is not a story of bad businesses. It is a story of
**good, real businesses that individually did fine but collectively could
not keep pace with a continuously-rebalanced, cap-weighted index over
three decades.**

## WHY THIS DIFFERS SO SHARPLY FROM BT-10, AND WHY THAT'S NOT A CONTRADICTION
Three real, disclosable reasons, not excuses:

1. **The S&P 500 is not a static basket — it is a continuously curated
   one.** Over 32.6 years, the index committee has repeatedly dropped
   shrinking, acquired, or delisted constituents and replaced them with
   the era's new winners — culminating, over this exact window, in
   Apple, Microsoft, Nvidia, Amazon, and Google going from nonexistent-
   in-the-index or tiny in 1993 to together anchoring a large share of
   it today. A **static** 1993 buy-and-hold portfolio cannot do that; it
   is frozen at whatever business mix looked cheap in 1993.
2. **This screen's 1993 survivor pool is structurally tilted toward
   "old economy" sectors** — utilities, regional banks, insurers,
   industrial distributors — precisely because those are the companies
   whose 1990s 10-Ks were extractable at all (data availability itself
   introduced a sector bias, disclosed here rather than hidden) and
   precisely the sectors that, as a group, have structurally lagged a
   technology-and-services-driven market over the following three
   decades. This is not a flaw in the framework's stock-picking; it's a
   real, disclosed sampling constraint of what 1990s paper-era filing
   history this project could actually recover.
3. **Time horizon changes what "beating the index" requires.** BT-10's
   93.9% beat rate was over 8 years; a 5-7 point CAGR gap over 8 years is
   real but recoverable. Over 32.6 years, that same-sized gap compounds
   into an enormous divergence — SPY's 10.73% vs. the survivor pool's
   ~7.2% mean means SPY multiplied money roughly **3x more** over the
   full period. Small, persistent CAGR shortfalls are far more punishing
   the longer they're allowed to compound.

**This does not undo BT-10's finding — it sharpens what BT-10's finding
actually means.** BT-10 showed the full framework (Book One + qualitative
gates) reliably avoids value traps and picks businesses that beat the
market over a specific 8-year window that happened to include an AI-
driven tech re-rating. BT-11 shows that same rigor, applied to a 1993
sample structurally biased toward stalwart-but-mature sectors, does not
guarantee outperformance over multiple decades against an index that gets
to continuously replace its own losers. **The honest, combined reading**:
this project has real evidence the framework helps avoid catastrophic
failures (BT-7, BT-8) and can build genuinely outperforming concentrated
portfolios over medium (multi-year) horizons when qualitatively vetted
(BT-10) — it has no evidence, and BT-11 now provides real evidence
against, the claim that any static buy-and-hold portfolio, however
carefully selected, reliably beats a continuously-rebalanced index over
30+ years.

## LIMITATIONS, STATED PLAINLY
- **Sample size and sector concentration are real constraints, not just
  caveats.** 12 survivors, mostly financials/utilities/industrials, is a
  narrow slice of the full 1990s market — a genuinely different, much
  larger sample (if 1990s data for technology, retail, and consumer-
  growth names had been equally recoverable) might tell a different
  story. This is disclosed as the ceiling of what could be recovered,
  not asserted as representative of "the market in 1993."
  Correspondingly, the 190-company starting pool itself already
  reflects survivorship (only companies large enough, and lucky enough
  in filing-history terms, to have real 1994-1995-vintage 10-Ks
  reachable at all made it this far).
- **Static buy-and-hold, no rebalancing** — the test never sells a
  survivor even after 32 years of drift; a real long-term investor might
  have trimmed, rotated, or reinvested along the way. This is the same
  simplifying convention as every other backtest this session.
- **Price return only, no dividends**, on both sides — understates
  absolute returns for both the survivor portfolios and SPY, though
  utilities/insurers/banks in this survivor set are generally
  higher-dividend-payers than SPY's current composition, meaning a
  total-return calculation would likely narrow (not close) the gap
  somewhat.
- **The qualitative gates were AI-run research, not human-verified**,
  same caveat as BT-10 — real, sourced, specific reasoning (the Shiley
  heart-valve citation, the Primerica merger timeline) but not to the
  full per-claim citation depth of a human-run Test Run.
- **Only one entry date tested** (1993-12-31) — the same "still open"
  question flagged in BT-9/BT-10 applies here with even more force: does
  a 1990s-anchored concentrated portfolio look different starting from a
  different year in that decade?

## WHAT THIS SETTLES, AND WHAT'S STILL OPEN
1. **The manual, pre-XBRL extraction pipeline works and is real** — 114
   of 187 pre-1996 filers yielded genuine, human/agent-verified 1990-1994
   financial data, with two real bugs (share-count units, un-reversed
   stock splits) caught and fixed before any result was trusted, not
   after.
2. **The framework's qualitative gates did real work here too** — 4 of
   16 mechanical passers were correctly eliminated for substantive,
   specific reasons (an adjudicated product-safety disclosure failure, an
   opaque insurance runoff, a people-business with no moat, an
   unevaluable fresh conglomerate), not rubber-stamped through.
3. **The honest, sobering headline**: over a genuine 32.6-year horizon,
   this rigorously-selected 1990s portfolio did not beat the index —
   every one of the 66 possible 10-business combinations underperformed
   SPY, and only 1 of the 12 individual survivors beat it alone. This is
   reported as found, not reframed as a hidden win.
4. **Still open**: whether this result is a property of long horizons in
   general, or specific to this particular sector-tilted 1993 sample —
   the next real test is attempting the same pipeline on a broader or
   differently-tilted slice of the 1990s universe, data permitting.

## SELF-AUDIT
- [x] Genuine manual extraction from real 1990s SEC filings — no XBRL
  shortcut existed for this era, and none was faked
- [x] Two real methodology bugs found and fixed before results were
  trusted (share-count units; un-reversed stock-split adjustment,
  including a P/E-based sanity check that caught the remainder)
- [x] Every unparseable filing snippet logged as UNKNOWN with a specific
  reason — no fabricated numbers anywhere in the dataset
- [x] Two ticker-identity mismatches (WFC=Norwest, C=Primerica/Travelers)
  identified and disclosed to the qualitative research rather than
  silently judged under their modern names
- [x] Qualitative gates applied with real point-in-time discipline
  (1993-12-31, no hindsight either direction) and real eliminations (4 of
  16), not a rubber stamp
- [x] All C(12,10)=66 possible portfolios enumerated exhaustively, not
  sampled or cherry-picked
- [x] The unfavorable result (0% beat rate over 32.6 years) is reported
  as the headline finding, not buried or spun — this project's standing
  rule against reporting only flattering results applies here as much as
  anywhere else
- [x] The tension with BT-10's result is explained with real, specific
  reasons (index rebalancing, sector sampling bias, time-horizon
  compounding), not hand-waved away
- [x] All data (extraction snippets, screen results, gate verdicts,
  portfolio enumeration) and scripts committed under `Backtests/`
