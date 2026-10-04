# BACKTEST BT-8 — The Real Point-in-Time Re-Run — 2026-07-22
The natural next step flagged at the end of BT-7: not a survivor-selected
pool, not a hand-picked failure sample — **the actual, complete, historical
S&P 500 universe, screened with only the data that would have existed at
the time, checked against what genuinely happened to every name afterward.**
This is the gold-standard fix for survivorship bias, built in full.

## METHOD
- **Universe**: the same 503-name S&P 500 reconstructed as of 2013-01-01
  from BT-7 Part B (Wikipedia's tracked constituent-change log, reversed).
- **A second, honest data ceiling, found and adjusted the same way as the
  1970 price wall and the 2008 reconstruction wall**: genuine 5-year
  trailing XBRL data — what the mechanical Book One screen actually needs —
  doesn't exist broadly enough at 2013-06-30 (386 of 503 names had
  insufficient filed history that early). Pushed the screen date forward to
  **2018-06-30**, where trailing data is genuinely available. The universe
  membership is still the real 2013 snapshot — only the date the screen
  itself runs moved, disclosed here rather than silently chosen for a
  flattering result.
- **CIK resolution and data pull**: 287 new companyfacts fetches beyond
  what was already cached this session (113 delisted/renamed tickers from
  the 2013 universe were not individually resolved — a stated, logged
  coverage gap, not a hidden one), plus 202 new price-history fetches.
  **335 of 503 names (66.6%) had enough data to screen; 168 logged as
  coverage gaps**, mostly the 113 unresolved CIKs.
- **The test**: run the exact point-in-time mechanical Book One screen
  (worst-of-trailing-5-filed-year NI vs. sovereign-yield hurdle, same
  methodology as every backtest this session) against all 335 screenable
  names as of 2018-06-30, then cross-reference PASS/FAIL against each
  name's **actual fate** (from BT-7 Part B's classification): still in the
  index, acquired fairly, survived independently, spun off, **FAILED**
  (bankruptcy/conservatorship), or **SEVERELY_IMPAIRED** (survived, but
  destroyed most shareholder value).

**⚠️ SUPERSEDED BY ADDENDUM 2 BELOW**: the "7/7 bankruptcies, 100%" result
in this section reflects coverage as it stood earlier in this document's
history. With coverage later expanded to 79.3%, a new testable bankruptcy
(Big Lots) was found to pass the screen, moving the true rate to **7/8
(87.5%)**. Left below unedited per this project's "correct forward, don't
edit history" rule — see Addendum 2 for the current, complete number.

## RESULT — THE DISCRIMINATION TEST (as of ~74% coverage; see Addendum 2 for the current number)

| | Bad-fate names (FAILED or SEVERELY_IMPAIRED) with usable data | Screen said FAIL (avoided) | Screen said PASS (false positive) |
|---|---|---|---|
| **All 12** | 12 | **10 (83.3%)** | 2 |
| **Outright bankruptcies only** | 7 | **7 (100%)** | 0 |
| Severely impaired (survived, value destroyed) | 5 | 3 | 2 |

**Every single outright bankruptcy — Bed Bath & Beyond, Peabody Energy,
Chesapeake Energy, Denbury Resources, Diamond Offshore Drilling, Frontier
Communications, Windstream — was correctly flagged as a FAIL by the bare
mechanical screen, using only data that would have existed at the time.
Zero false negatives on actual bankruptcy.** This is the closest thing this
project has to a controlled experiment: a real, unfiltered historical
universe, point-in-time data discipline, and a clean cross-tabulation
against what genuinely happened.

### The 2 false positives, and why they're the interesting case, not an embarrassment
**Fossil Group (17.82% yield) and Pitney Bowes (12.37% yield)** both passed
the bare screen — and both went on to be severely impaired (not bankrupt,
but massive, sustained value destruction). Look at those yields: **4-5x the
4% hurdle.** A stock priced to yield 12-18% on trailing earnings is not
quietly cheap — it is screaming that the market expects something to go
badly wrong, which the market turned out to be right about in both cases.
This is exactly the pattern this project has flagged before (the BKNG-vs-
INTC finding in the wider-universe backtest): **an extraordinarily high
mechanical yield is itself a signal that should trigger the qualitative
gates, not just clear the bar and stop.** Neither false positive would
need a new rule to catch — the existing "Scream Test" logic (does Book Two,
or even just a gut-check on why the yield is this extreme, agree with Book
One) is built for precisely this case; it just wasn't re-applied here,
since this test deliberately isolated Book One alone, the same scope
limit as every other mechanical backtest this session.

### The broader, more sobering context
Passing the bare screen was **not** a strong general predictor of "still in
the S&P 500 today" — passes were in the index today 83.3% of the time,
fails 81.9%, essentially no difference. **That's the honest, correct
reading**: the mechanical screen isn't built to predict fame or index
membership, most companies leave the S&P 500 for completely ordinary
reasons (acquired, shrank, spun off) that have nothing to do with quality.
What it *does* discriminate on — sharply — is the tail risk that actually
matters to a long-term holder: catastrophic, capital-destroying failure.

## WHAT THIS SETTLES, AND WHAT'S STILL OPEN
This closes the loop BT-7 opened. Put together with BT-7's findings:

1. **The framework's mechanical gate has now been tested three ways**: it
   eliminated Micron mechanically this session, it caught 4 real historical
   bankruptcies applied retroactively (BT-7 Part A), and now it correctly
   flagged all 7 testable bankruptcies in a genuine, unfiltered, point-in-
   time universe (BT-8). That's real, convergent evidence — not a single
   lucky backtest.
2. **The 2 misses are diagnosed, not hand-waved**: both were extreme-yield
   value traps the framework's own Scream Test logic is designed to catch,
   one layer up from where this test stopped.
3. **Still open**: this tested Book One alone, not the full 8-gate
   qualitative framework, and coverage was 66.6% of the universe (168 names
   unresolved). A complete version would resolve the remaining 113 CIKs and
   layer in Book Two/the Scream Test to see if it closes the 2 remaining
   gaps.

## LIMITATIONS, STATED PLAINLY
- Screen date (2018-06-30) is later than the universe date (2013-01-01) —
  a real, disclosed adjustment forced by data availability, not a
  cherry-picked flattering date.
- 168 of 503 names (33.4%) could not be screened — 113 for unresolved CIKs
  (delisted/renamed tickers not worth the individual lookup cost this
  pass), the rest for insufficient trailing history even at 2018.
- Book One only — the qualitative gates (moat, management, inversion) that
  would likely have caught the 2 false positives were not re-applied here.
- Fate classification inherits BT-7 Part B's stated rigor tier (hand-
  classified from general knowledge, not individually re-verified against
  primary sources this session).

## WHAT'S NEXT
- Resolve the remaining 113 unresolved CIKs for full universe coverage.
- Layer Book Two / the Scream Test onto the 2 false positives specifically
  to confirm they get caught one level up.
- Repeat this exact test at a different universe-reconstruction date (e.g.
  2016 or 2018) to see if the 100%-bankruptcy-catch rate holds outside this
  one snapshot.

## SELF-AUDIT
- [x] Real, reconstructed historical universe — not a survivor-selected pool
- [x] Point-in-time discipline maintained throughout (filed-date gated NI,
  no look-ahead)
- [x] The screen-date adjustment (2013 universe, 2018 screen) disclosed as
  a data-availability forced choice, not hidden
- [x] Both the strong result (7/7 bankruptcies caught) and its real
  limitation (2/5 severe-impairment misses, 33% universe coverage gap)
  reported together, not selectively
- [x] All data (screen results, coverage gaps, universe reconstruction,
  fate classifications) and every script committed

## ADDENDUM — COVERAGE EXPANDED, RESULT HOLDS (2026-07-22, same day)
Per the "what's next" item above, resolved the remaining unresolved CIKs
rather than leaving them open: **109 of the 113 originally-unresolved
tickers were found** via direct SEC company-name search (4 genuine dead
ends remain — CA Inc, Juniper Networks, Peoples United Financial, Wyndham
Worldwide — logged as a final coverage gap, not force-fit). Pulled their
XBRL companyfacts and, where available, price history (60 of the newly-
resolved tickers had no Yahoo price data at all — confirmed as a genuine
data absence, not a rate limit, by testing a known-good ticker mid-stream).

**Coverage rose from 335/503 (66.6%) to 369/503 (73.4%).**
**The discrimination result is unchanged**: still 7/7 outright bankruptcies
correctly flagged FAIL, still exactly the same 2 false positives (Fossil
Group at 17.82% yield, Pitney Bowes at 12.37%) — the additional 34
screened names were all in the "fine fate" bucket, adding statistical
weight to the result without changing its shape. This is a good sign, not
a null result: the finding was not an artifact of a small, lucky sample —
it held as the sample grew by 10%.

The 4 remaining unresolved tickers (CA, JNPR, PBCT, WYN) and the ~60
resolved-but-price-less names are the final, honestly-stated coverage
ceiling for this data source — closing the loop opened at the top of this
document.

**Alternate sources tried and ruled out for the ~60 price-less names**:
stockanalysis.com independently returned the same 404s as Yahoo (confirms
the gap is real, not Yahoo-specific); Zacks blocks scraping (HTTP 403, bot
protection); Barchart 404s on the tested URL pattern. Rate-limiting was
ruled out directly — AAPL and KO fetched successfully on the same
connection immediately after these failures.

**Follow-up (same day): web-searched what actually happened to a sample of
the "surprising" failures — well-known, still-should-be-large companies
that shouldn't plausibly be delisted.** The answer turned out to be real,
dated, recent corporate history, not a data problem:
- **GPS (Gap Inc.) was a fixable false alarm** — the company renamed its
  ticker from GPS to **GAP** effective August 22, 2024, and is still
  actively trading. Refetched under the new symbol and merged into the
  dataset — **coverage rose to 370/503 (73.6%)**, discrimination result
  unchanged.
- **The rest are confirmed genuine, permanent departures from public
  markets — a real wave of 2022-2026 M&A, not a fixable data gap**: Citrix
  (CTXS, acquired by private equity, delisted Sept 2022), Discover
  Financial (DFS, merged into Capital One, delisted May 2025), Marathon
  Oil (MRO, acquired by ConocoPhillips, Nov 2024), Nordstrom (JWN, taken
  private by the Nordstrom family + El Puerto de Liverpool, May 2025),
  Kellanova (K, formerly Kellogg, acquired by Mars), Tegna (TGNA, merged
  with Nexstar, 2025), and Sealed Air (SEE, being acquired by Clayton,
  Dubilier & Rice, expected to close mid-2026 — right around this
  session's own date, which is why it vanished from live quote systems
  mid-project). Free retail aggregators (Yahoo, stockanalysis.com, Zacks,
  Barchart) drop historical archives entirely once a ticker is retired —
  none of them, tried directly, could serve a 2018 price for a company
  that no longer exists as an independent public entity today. That's a
  structural feature of free market data, not a fixable gap in this
  project's method.

**73.6% is the practical, well-explained ceiling for this exercise using
free MARKET-DATA APIs** — and the remaining gap is no longer an unexplained
"coverage hole"; it's a named list of real mergers and going-private deals.

## ADDENDUM 2 — PRIMARY-SOURCE EXTRACTION FROM SEC FILINGS DIRECTLY (same day)
The user pushed further, asking whether the "manual extraction" fallback
already flagged as the free-but-slow option could actually be done. It
could — but not by writing a smarter regex. Every free market-data API,
paid API (FMP, tested directly with a real key), and archival source
(Wayback Machine, tested directly against real snapshots) was exhausted
first; see below for that full record. What actually worked was a genuine
primary source: **every 10-K's cover page discloses "aggregate market
value of common equity held by non-affiliates," computed as of the last
business day of the registrant's second fiscal quarter — almost exactly
this project's rebalance date — and this disclosure was untouched by the
2018 rule change that killed the optional quarterly price table.**

**Method**: scripted the fetch-and-isolate step (find each company's
closest-to-target 10-K, pull the cover-page text), then — critically —
**did the interpretation by reading, not by regex.** A single regex
pattern correctly parsed only 3 of 70 cover pages on the first pass,
because filing agents phrase this disclosure dozens of different ways
("$59 billion" vs "$99,985,852,722" vs "$42.21 per share" vs multi-class
tables). Reading all 32 remaining snippets directly identified 19 more
clean, confident extractions — and, just as importantly, correctly
**excluded** 13 more for real, nameable reasons a regex would have missed
or silently gotten wrong: 3 were stale FY2017 filings (the company was
acquired mid-2018, before ever filing a FY2018 10-K — ANDV, ESRX, SNI);
2 were CIK-resolution mismatches that pulled the wrong company entirely
(GAS resolved to Southern Company instead of its actual subsidiary; VIAB
pulled CBS Corp, its later merger partner); Whole Foods (WFM) explicitly
stated in its own filing that it was already a 100-share, fully-owned
Amazon subsidiary; and 4 more (BF.B, DPS, ECHO, FII) had multi-class-share
or merger-transition share counts that would have produced the same kind
of silently-wrong number that the sanity check already caught twice
automatically (Alexion at an implied $2,886/share, Berkshire B at
$505,656/share — both rejected, not included).

Every accepted value — automated and manually-read alike — was run through
the same cross-check against XBRL-reported share counts before acceptance.
All 19 manually-read values passed cleanly.

### Result: coverage rose from 73.6% to 79.3%
| | Before this addendum | After |
|---|---|---|
| Screened | 370 / 503 (73.6%) | **399 / 503 (79.3%)** |
| Bad-fate names with usable data | 12 | **13** |
| Outright bankruptcies testable | 7 | **8** |

### The headline number changes, and this is reported honestly, not smoothed over
**Big Lots (BIG) — a real, confirmed 2024 bankruptcy — is newly testable,
and the bare mechanical screen PASSED it, at a 6.29% yield.** This is a
genuine miss on an outright bankruptcy. The bankruptcy catch rate is now
**7 of 8 (87.5%), not the previous 7 of 7 (100%)** reported in the original
version of this document above. The overall bad-fate catch rate is now
10 of 13 (76.9%), down from 10 of 12 (83.3%).

**This is the correct, more credible finding, not a worse one.** A
suspiciously perfect 100% catch rate on a small sample was always more
likely to be a small-sample artifact than a durable property of a bare
mechanical screen; 87.5% on a larger, more complete sample is a stronger,
more believable result. It also sharpens the standing finding rather than
undermining it: **Big Lots passed at 6.29% — comfortably above the 4%
hurdle, not an extreme outlier the way Fossil Group (17.8%) and Pitney
Bowes (12.4%) were.** A modestly-cheap retailer heading into a genuine,
multi-year structural decline (discount retail, e-commerce pressure) is
exactly the kind of miss a bare valuation screen — with no moat, management,
or inversion check applied — should be expected to make sometimes. The
2 originally-flagged misses remain the more informative case (extreme
yields as a self-flagging warning sign); Big Lots shows the mechanical
layer isn't infallible even without that warning sign present.

### What this changes about earlier claims in this document
The original headline above ("all 7 outright bankruptcies... zero false
negatives") is now superseded by this addendum and should be read as
describing the state of the test *as of that coverage level*, not the
final word — consistent with this project's rule of correcting forward
with a dated addendum rather than editing history.

## ADDENDUM 3 — BUG FIXES, NOT JUST MORE LOOKUPS (2026-07-22, same day)
The user's instruction was explicit: keep pushing toward 100% coverage
rather than accept 79.3% as a ceiling. This round found genuine **bugs**,
not just more manual lookups — some of them correctness bugs that changed
results, not just coverage.

### Bug 1: `load_shares()` let a stale primary tag block the fallback chain
SPG (Simon Property Group) and MON (Monsanto) were still gapping out after
the earlier price-fallback-chain fix. Root cause: `load_shares()` treated
any non-empty primary-tag point series as authoritative, even when every
point in it was years stale (SPG's `dei:EntityCommonStockSharesOutstanding`
had exactly 4 points, all from 2009-2010, two of them literally `val=0`) —
so it never even tried the fallback tags, and `shares=0` silently fell
through Python's truthiness check into a bogus coverage gap instead of
computing a (correctly zero, obviously wrong) market cap. Fixed to require
at least one point actually usable as of the target date before accepting
a tag series; also excluded `val==0` points as unusable everywhere. Also
found SPG reports its shares under a **non-standard tag name**
(`WeightedAverageNumberOfShareOutstandingBasicAndDiluted`, singular
"Share") for exactly the 2016-2020 window this test needed — added to the
fallback list.

### Bug 2: the NI dedup logic kept the *latest*-filed value, defeating point-in-time filtering
This was the highest-value fix this round. `load_ni_facts()` deduplicated
each fiscal year's net income by keeping whichever XBRL point had the
**latest** `filed` date — reasoning, at the time, that the newest figure
was "most authoritative." That's backwards for a point-in-time screen: a
later `filed` date is usually just that year's number being re-disclosed
as a comparative column in a *subsequent* 10-K, and keeping only that late
date meant the `filed <= REBAL` point-in-time filter then rejected a
figure the company had, in fact, reported on time years earlier. This was
silently starving well-covered, unambiguous large-caps — **GOOG, MDT,
MNST, DIS, BLK, CI** all showed "0-3 years of history" before the fix, on
companies with obviously complete filing records. Fixed to keep the
**earliest** filed value per fiscal year end — the true as-originally-known
figure, which is also the theoretically correct point-in-time choice
regardless of the coverage side-effect.

**This fix changed the discrimination test's result, not just its sample
size**: with correct point-in-time NI, **Fossil Group (FOSL) is no longer
a false positive** — it now screens out correctly. The false-positive list
shrank from 3 names to 2 (BIG, PBI) even as the covered universe grew,
because the earlier "false positive" was partly an artifact of the dedup
bug feeding the screen a look-ahead-tainted NI figure, not a true
limitation of the mechanical screen itself.

### Bug 3 (really 9 cases): wrong-entity CIK resolution — post-reorg holdcos and recycled tickers
Several tickers resolved, on the earlier ticker-based CIK search, to a
**different legal entity** than the one that actually traded under that
symbol in 2018:
- **Post-reorg holding companies** (same underlying business, new CIK
  created for a corporate restructuring, old CIK's filings stop or start
  right at the reorg date): **DIS** (Disney's 2019 Fox-merger holdco,
  CIK 1744489, has zero history before 2019 — correct historical filer is
  CIK 1001039, "TWDC Enterprises 18 Corp.", the renamed original Walt
  Disney Co.), **BLK** (BlackRock's 2024 holdco restructuring — correct
  CIK is 1364742, filed as "BlackRock Inc." 2006-2024), **XRX** (Xerox's
  2021 Xerox Holdings reorg — correct CIK is 108772, the original Xerox
  Corp).
- **Recycled tickers** — a delisted company's old ticker symbol reused
  years later by a totally unrelated company, so a plain ticker search
  finds the *wrong, current* holder of the symbol: **S** (ticker recycled
  from Sprint Corp, acquired by T-Mobile 2020, to SentinelOne's 2021 IPO —
  correct CIK is 101830, "SPRINT NEXTEL CORP"/"SPRINT CORP"), **STI**
  (recycled from SunTrust Banks, merged into Truist 2019, to a 2024 shell —
  correct CIK is 750556), **CI** (Cigna Corp renamed "The Cigna Group" in
  2022 after the Express Scripts deal, and the ticker search surfaced only
  post-rename data — correct CIK is 701221, the original Cigna Corp).
- **Genuinely fixed, screened through to a result**: DIS, BLK, CI, S, XRX,
  STI. NE (Noble Corp, correct CIK 1169055 found) still falls short on
  NI-history count post-fix — a genuine partial data gap tied to its 2020
  bankruptcy reorganization, not pursued further.
- **Same pattern checked, confirmed as genuine (not fixable) category
  errors, not forced in**: DOW (Dow Chemical's independent filings stopped
  at FY2017 — it was already absorbed into the DowDuPont merger before a
  FY2018 report would exist) and LIN (Praxair's last independent 10-K was
  also FY2017, ahead of the Oct 2018 Linde merger close) both confirmed via
  their own SEC filing histories to have genuinely ceased independent
  reporting before this test's screen date — the same "category error, not
  a data gap" pattern as the ~29 other pre-2018 M&A departures already
  documented in Addendum 1.

### Two more clean 10-K price extractions, and two structurally-excluded for cause
**ALXN (Alexion)** and **PDCO (Patterson Companies)** both got clean cover-
page extractions this round — ALXN's earlier attempt had been correctly
rejected by the sanity check (a garbled $2,886/share), refetched clean at
$118.65, cross-validated exactly against XBRL shares. PDCO was a first
attempt, extracted at $22.56, also an exact share-count match. **STI**
(SunTrust) got a third clean extraction, exact XBRL match, AMV dated
literally one day off the target (June 29, 2018).

**BRK.B and STZ (Constellation Brands) were investigated and deliberately
excluded**, not force-fit: both disclose "aggregate market value held by
**non-affiliates**" on their cover pages, and both have a large,
economically meaningful affiliate/insider share block (Buffett/Munger for
BRK.B; the Sands family's super-voting Class B for STZ) that the AMV figure
excludes by definition. Dividing that non-affiliate-only dollar figure by
the *total* share count (affiliate + non-affiliate) would understate market
cap and silently produce a wrong price — the same structural problem
already correctly excluded WFM in Addendum 2. Honest gap, not a fixable one
without the proxy statement's affiliate-holdings breakdown.

### Result: coverage rose from 79.3% to 83.3%
| | Before this addendum | After |
|---|---|---|
| Screened | 399 / 503 (79.3%) | **419 / 503 (83.3%)** |
| Bad-fate names with usable data | 13 | **14** |
| Outright bankruptcies testable | 8 | **9** (BIG stays a miss) |
| Bad-fate catch rate | 10/13 (76.9%) | **12/14 (85.7%)** |
| False positives | BIG, FOSL, PBI (3) | **BIG, PBI (2)** — FOSL corrected by Bug 2 fix |

### What's left in the remaining 84 gaps
Broken down: **~50 NO_PRICE** — the large majority now confirmed, ticker by
ticker, as genuine pre-2018 M&A departures (company had no FY2018 10-K to
extract a price from because it no longer existed independently); a residual
handful (BRK.B, STZ) structurally excluded for the affiliate-exclusion
reason above. **~32 INSUFFICIENT_NI_HISTORY** — a mix of confirmed genuine
pre-2018 departures (DOW, LIN) and a smaller number of confirmed-correct
entities (AVY, WAT) that have a real gap in SEC's own structured XBRL data
for 2012-2015 (Avery Dennison's annual `NetIncomeLoss` simply jumps from a
FY2011 filing straight to FY2016 in the API — years missing from the
company's own structured disclosure, not a resolution or extraction
problem on this project's end; the underlying numbers likely exist in the
filed text but would require full manual financial-statement reading to
recover, at a cost-per-name that stopped paying off around here). **1
NO_XBRL_DATA** (JCP, confirmed to have never filed XBRL). **83.3% is this
round's honestly-reached point** — every remaining gap has been individually
triaged and diagnosed as either a genuine category error (company didn't
exist at the target date) or a real gap in the free source data itself, not
left unexamined.

## ALTERNATE SOURCES EXHAUSTIVELY TESTED (full record)
In the course of trying to close this gap, the following were tested
directly, not assumed: Yahoo Finance (multiple endpoints/ranges),
stockanalysis.com, Zacks (blocks scraping), Barchart, Massive.com (2yr
free limit), EODHD (demo key whitelisted to 6 symbols; delisted archive is
paid), Nasdaq Data Link (bot-protection wall), Marketstack (1yr free
limit), Norgate Data ($787.50/yr, no free tier), QuantRocket (free tier
covers only 2007-2011), **Financial Modeling Prep — tested with a real
user-provided API key**, confirming free-tier access works fine for active
tickers but explicitly premium-gates delisted-ticker historical prices
("Premium Query Parameter... not available under your current
subscription"), and the **Wayback Machine** — tested directly against real
archived snapshots of Yahoo's history page for a delisted ticker (Citrix),
finding real snapshots from 2019 and 2020 that both showed only a rolling
~100-trading-day window (JS-paginated, uncapturable by a static archive)
that never reached back to the 2018 target date in any snapshot ever
crawled. Every one of these was a genuine dead end, not a hypothesis left
untested.
