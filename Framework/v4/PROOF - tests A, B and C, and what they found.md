# PROOF — Tests A, B and C
**2026-08-27.** Three tests run to answer "does v4 work?" before believing it. Pre-registered
at commit `2121a52` before any analyst saw a case. **One test passed with a specific defect
found, one was inconclusive by my own design error, one passed and in passing exposed eight
bugs.**

**None of this bears on the market-beating claim, which remains UNPROVEN.** These tests were
chosen precisely because that claim is not testable here: v4's gates require reading
documents, so a backtest tests a mechanised proxy, not v4. The 32-year full-gate test
underperformed; the mechanical layer wins 49.6% of 944 holdings. Nothing below changes that.

---

# TEST A — REPRODUCIBILITY. **PASSED, with one defect.**

Two independent analysts, same company, same anchor, same documents, no contact, neither
able to see prior run files or each other's work.

## HRB — near-total agreement

| | Analyst 1 | Analyst 2 |
|---|---|---|
| Q1 / Q2 | IN / **OUT** | IN / **OUT** |
| Q3 weight | **GATE** — daily execution | **GATE** — daily execution |
| Q3 | UNRESEARCHED (CEO 8 months) | UNRESEARCHED (CEO 8 months) |
| Q4 | IN | IN |
| Stopped at | **Q2** | **Q2** |
| Owner earnings | $615–670M, **5-yr** | $615–670M, **5-yr** |
| Leverage | 27.7x; net debt **0.50x** EBITDA | 27.7x; net debt **0.50x** EBITDA |

Same stop, same band, same window, same Q3 reason, same resolving document (the DEF 14A).
One divergence: Q6, where analyst 1 pre-committed a re-open yardstick and ruled IN while
analyst 2 ruled NOT REACHED because *"there is no act."* Both defensible; the spec is silent.

## TJX — verdicts identical, quantities not

| | Analyst 1 | Analyst 2 |
|---|---|---|
| Q1–Q6, stop | all IN, NONE | all IN, NONE |
| Leverage | 3.51x | 3.51x |
| **Action** | don't buy at $135.12 | don't buy at $135.30 |
| **Owner earnings** | **$3.76bn** (5-yr) | **$4.8bn** (3-yr) |
| **Points over sovereign** | **−0.25 .. +0.18** | **+0.6 .. +1.7** |

Both also converged on things the spec does not dictate: both hit the FRED outage and both
climbed to the **US Treasury** rather than an aggregator; both fired the guidance flag on the
same 8-K; both failed buyback condition two; both named merchandise-margin compression as the
death mechanism and **Marmaxx comps** as the sharpest monitorable.

## THE DEFECT — the averaging window is unspecified

**v4 requires each run to STATE its window but never fixes it.** One analyst took five years,
the other three. That single choice moved owner earnings **28%** and the ranking **~1.5
points**. It did not change the action on TJX because $135 sits far above both estimates.
**It would change the action for any name near the line** — which is where decisions are made.

Note where it did and did not bite: both HRB analysts chose five years and agreed. The
divergence appeared on TJX, where a distorted year (COVID) forces a judgment call. **The
defect surfaces exactly where judgment is required and the spec is silent.**

## AND TEST A CORRECTED A LIVE RULING

`RERUN - the six live names under the Q3 weight rule.md` ruled HRB a gate **because of**
27.72:1 leverage. Both analysts rejected that independently: **the ratio fires but the
mechanism does not.** **[E3-29]** is about small asset errors destroying equity, and H&R Block
has no asset book — net debt 0.50x EBITDA, cover 13.1x, the thin equity an artifact of
buybacks. The verdict stands (GATE) but on **daily execution [E3-38]**. Corrected in place,
recorded not silently edited.

---

# TEST B — CORPUS REPLICATION. **INCONCLUSIVE. THE TEST FAILED, NOT THE FRAMEWORK.**

Five de-identified, point-in-time case files. Pre-registered expectations sealed before any
analyst ran.

| case | identity | expected | result |
|---|---|---|---|
| A | WFC 2018-01-02 | Q3 should FAIL (2016 scandal public) | stopped **Q2**, UNRESEARCHED |
| B | AAPL 2016-05-16 | should PASS and rank well | stopped **Q1**, UNRESEARCHED |
| C | IBM 2011-11-14 | should FAIL, likely Q2 | stopped **Q1**, UNRESEARCHED |
| D | OXY 2019-08-08 | defended; Q4 the live question | stopped **Q1**; Q4 OUT **on bad data** |
| E | KHC 2018-01-02 | should FAIL or UNRESEARCHED | stopped **Q1**, UNRESEARCHED |

## Why it is inconclusive

**Every case stopped at Q1 or Q2 for the same reason: no business description.** v4 cleared
nothing — but it rejected Apple exactly as it rejected IBM and Kraft Heinz. **A test that
returns the same answer for the good case and the bad cases has not discriminated.**

**The cause is my design error.** De-identifying the case files to defeat contamination also
removed the evidence Q1 and Q2 require. Q1 asks for the unit economics *in your own words* and
the scarce input the business controls; Q2 requires a competitor row. Neither is answerable
from a tag dump. Every analyst said so, correctly, and named the resolving document.

**That is v4 behaving correctly under thin evidence** — UNRESEARCHED with a named work order,
never a thin-evidence pass. It is a real if modest finding: **the framework refuses rather
than guesses.** It is not the falsification test I set out to run.

## The signal that did survive: the SINGLE-BIGGEST-CONCERN field

Asked what in the numbers most argued against owning it, three of the four valid cases named
the thing that actually went wrong afterwards — blind, from figures alone:

- **IBM** — *"Revenue is flat (+0.36%/yr) while net income rose 42% and equity fell 19.5% —
  EPS compounded 17.2%/yr off margin expansion and a share count down 11.6% … precisely the
  'consistent gains in earnings per share' that [E2-01] names as not the test."* That is the
  IBM thesis, and it cites the 1979 row added to the standard yesterday.
- **KHC** — *"The equity base grew 8.1x while the earnings rate on it fell to ~6.3%."* The
  goodwill-laden merger whose $15.4bn writedown landed 13 months after the anchor.
- **WFC** — equity rose $15.2bn from 2014–16 while net income **fell** $1.1bn, ROE 13.4% →
  11.2%; flagged as **[E2-30]**'s "soak up available funds."
- **AAPL** — "a sawtooth, not a stream." A fair concern; not a failure.

**Read honestly: the quantitative layer surfaced the right worry in three of four, but could
not convert that into a pass/fail verdict.** The judgment layer — Q1 and Q2, the reading —
was doing the discriminating, and I had removed it.

## What a valid Test B requires

Give the analyst a **de-identified business description** — industry, what it sells,
competitive position, extracted from Item 1 and scrubbed of identity — alongside the numbers.
That makes Q1 and Q2 answerable while keeping the outcome hidden. It is real work and it is
the honest next attempt. **Pre-registration is retained regardless; it is the only control
that survives an imperfect blind.**

---

# TEST B v2 — RUN 2026-08-28 WITH THE DESCRIPTIONS. VERDICT: **PASSED ON THE FALSIFICATION
HALF; THE ACCEPTANCE HALF IS STRUCTURALLY UNTESTABLE BLIND.**

Five blind analysts, each given the point-in-time numbers (with the bug-8 equity flags and
bug-9 market cap), a description written from the Item 1 of the filing of record (accession
numbers logged), and **v4.1** — making this also the first live run of the amended framework.
Scored against the key sealed at `2121a52`. Identities now unsealed for the record:

| case | identity | pre-registered expectation | v2 result | score |
|---|---|---|---|---|
| A | **WFC** 2018-01-02 | Q3 should FAIL; *"a v4 that clears Q3 here has failed"* | Q2 UNRESEARCHED; Q3 gate declared (9.7x), never cleared | **not failed — and unconfirmable blind** |
| B | **AAPL** 2016-05-16 | should PASS Q1–Q4 and rank well | Q2 UNRESEARCHED (peer row absent); everything computable clean; single-company franchise test **[E3-43]** passing; 8.5–9.8% yield vs the floor | **miss in the pass direction — by design** |
| C | **IBM** 2011-11-14 | should FAIL; clearing = replicating Buffett's own graded error | Q2 UNRESEARCHED — **did not buy what Buffett bought**, and named the exact failure thesis blind: flat revenue, EPS from mix/margin/share count, cloud as the substitution vector against the annuity base; **[E4-30]** smoothness tell fired | **hit** |
| D | **OXY** 2019-08-08 | defended by Buffett, not graded; Q4 leverage the live question | **Q2 OUT** on the filing's own commodity language; Q4 diagnostic OUT on the 74% OCF collapse | **divergence, documented** |
| E | **KHC** 2018-01-02 | should FAIL or UNRESEARCHED (writedown 13 months post-anchor) | Q2 UNRESEARCHED; refused to splice pre-merger years; biggest concern = *"$94.4bn for an entity… resting on a single combined year"* — the writedown's exact mechanism | **hit** |

## What is now proven

1. **Zero false passes, five for five.** The falsification standard — does v4 clear a name
   it should refuse — came back clean: none of the graded errors was cleared, and the one
   outright rejection (D) was on the corpus's own doctrine. **v4 cannot be lured into a yes
   on partial evidence.** Under thin evidence it refuses; under disqualifying evidence it
   rejects; it articulated the correct failure mechanism blind on both graded errors (IBM's
   EPS engineering and cloud substitution; KHC's single-year base).
2. **The acceptance half cannot be tested blind, and that is a property of the framework,
   not of the test.** The two things a full pass requires — the same-metric competitor row
   and the filed conduct record for Q3 — are irreducibly identifying. A design that
   de-identifies must withhold them; a framework that demands them cannot say yes without
   them. Apple therefore stopped exactly where Wells Fargo did, at the evidence the blind
   withholds. **The framework refuses to distinguish a wonderful business from a scandal on
   numbers alone — which is the manager standard's own claim, now demonstrated.**
3. **The D divergence is recorded, not excused:** v4 refuses the commodity producer its own
   author bought and defended. This matches Test D's finding that the corpus's
   franchise-first doctrine and the author's practice diverge (the 1978–84 letters; register
   items L1-7/8), and it stays visible as such.
4. **v4.1 worked in live hands on its first outing:** the floor **[E4-28]** applied in two
   diagnostics; **[E3-43]**'s weight tracing produced a correct CANNOT-DETERMINE; the (c)
   default and exception class were applied per business class (capex basis for the oil
   producer, D&A default for food and electronics); window spreads carried per **[E4-25]**;
   every SUSPECT equity flag respected; the refused market cap treated as data.

**The market-beating claim remains UNPROVEN and none of this bears on it.**

---

# TEST C — POINT-IN-TIME DISCIPLINE. **PASSED. And it found eight bugs.**

`tools/pit.py` refuses any fact the SEC received after the anchor and reports the count
blocked, so an empty series is never mistaken for absent data. **Selftest: zero leaks** across
three anchors; 284–593 facts blocked per case file.

**Building and running it exposed eight defects, seven of them silent:**

| # | bug | consequence |
|---|---|---|
| 1 | `annual()` took the first XBRL tag with data and **stopped** | Filers switch concepts mid-history; whole-series reads silently lost years. **Four of five portfolio names affected.** |
| 2 | `split_factor_after()` read a **10-year** window | Ross Stores' 2011/2015 splits invisible — a **falling** share count reported as **RISING**. |
| 3 | Yahoo `range=max&interval=1d` degrades to **quarterly** | A 2018-01-02 anchor answered with a 2017-12-01 close. |
| 4 | FRED's default CSV returns recent observations only | Cached file held **four rows**; every historical sovereign came back null. |
| 5 | Bank revenue tags absent | Wells Fargo's revenue series returned **empty**. |
| 6 | **Ticker recycling** | `PARA` now resolves to **Banzai International**, `LZ` to LegalZoom. Silent wrong-company data. |
| 7 | `run.py` crashed on a Unicode minus | Died before printing owner earnings on any Windows console. |
| 8 | **Dimension-qualified facts surfaced without their dimension** | See below. |

## Bug 8 is the one that matters, and Test B found it

Occidental's FY2018 10-K (filed 2019-02-21) tags `StockholdersEquity` for 2018-12-31 as
**−$172M**. The FY2019 10-K tags the same date as **$21,330M**. The first is a
dimension-qualified fragment; `companyfacts` does not expose the dimension, so it is
indistinguishable from a consolidated figure.

**The anchor guard worked perfectly and delivered a wrong number.** At the 2019-08-08 anchor
the −172M was the only value public; the correct figure was filed seven months later and was
correctly blocked. **Point-in-time discipline pinned the analyst to a bad value**, and the
analyst then built a Q4 OUT on it.

Collision detection cannot catch this — there is only **one** fact for the period. Only an
independent identity can. `pit.py` now cross-checks **Assets − Liabilities against stated
equity**, marks a mismatch SUSPECT, and — because absence of a check is not a pass — reports
**CROSS-CHECK NOT POSSIBLE** where the identity cannot be formed at all.

## And a ninth, found by an analyst, not by me

CASE_B's analyst refused to compute a market cap: *"The house rule `cap = close ×
shares(measurement) × splits AFTER measurement` cannot execute: the file supplies no split
history."* It was right. The case file pairs a **split-adjusted price** with an
**as-reported share count** and no reconciling factor — Apple's May-2016 close appears as
$23.47 on today's basis against a 5,793.1m share count on 2015's. **The yield it computed was
wrong by roughly 4x, and it detected that from the framework's own rule rather than from the
number looking odd.** Unfixed as of this writing; case files must carry the split factor.

---

# THE VERDICT

**What is now evidenced:**
1. **v4 is reproducible at the verdict level.** Two independent analysts reached the same
   answer on every question on two companies, including the stop point.
2. **v4 refuses rather than guesses under thin evidence** — five for five.
3. **v4's own rules caught a tooling error a careful analyst would otherwise have missed**
   (the split-basis mismatch).

**What is now known to be defective:**
1. **Q6's status when the run stops earlier is undefined.** Still open.
2. **Test B cannot discriminate as designed.** Still open — needs de-identified business
   descriptions.

**What remains untested:** whether v4 reproduces the corpus's own decisions. Test B could not
answer it. **The market-beating claim remains UNPROVEN and was not tested.**

**Added 2026-08-28 — TEST E, the loss leg of Ground Rule 7 [E1-17]: PASSED on pre-registered
terms.** The mechanical screen's passes lost money less often (19.4% vs 21.6% at 3 years,
17.0% vs 18.1% at 5) and less deeply (−22.7% vs −27.3%; −29.6% vs −33.5%) than the names the
same screen rejected, with the delisting bias understating the gap. The edge is thin, flips
at 2–3 of 8 anchors, and the medians are nearly identical — **the screen does not pick
winners; it modestly avoids losers**, which is the shape the corpus's own promise structure
predicts. Pre-registration committed at `49be7b4` before any number existed. Full record:
`TEST E - PREREGISTRATION - the loss leg.md`. The yardstick leg is unchanged: 2 of 8.

---

# THE FIXES — all nine bugs and the Test A defect, closed 2026-08-27

| # | bug | fix | verified by |
|---|---|---|---|
| 1 | `annual()` first-tag-and-stop | tag lists treated as a **union**, earlier tag wins per period | Apple FY2014 now admitted at a 2015 anchor |
| 2 | 10-year split window | splits fetched over **full history**, cached a week; pre-1970 epochs skipped (Windows) | ROST now reads **−2.67%/yr retiring**, was "+1.64% ISSUING" |
| 3 | Yahoo quarterly degradation | targeted **90-day daily window** around the anchor | 2018-01-02 anchor now returns a 2018-01-02 close |
| 4 | FRED recent-only CSV | **US Treasury daily yield curve** promoted to primary — the issuing authority, which the protocol actually asks for | 5 anchors 2011→2026 all resolve exactly |
| 5 | bank revenue tags | `RevenuesNetOfInterestExpense`, `InterestAndDividendIncomeOperating` added | WFC revenue series now populates |
| 6 | ticker recycling | **positive guard**: the CIK must have annual facts filed on or before the anchor, else the case is **refused**; staleness reported | all four test cases OK, gaps 220–367d |
| 7 | Unicode minus crash | stdout forced to UTF-8 in all six tools | `run.py` completes; `check_framework` output legible |
| 8 | dimension-qualified facts | **Assets − Liabilities cross-check**; unrunnable checks reported as such; plausibility screen for negative or sub-1%-of-assets equity that cannot be reconciled | OXY's **−172M and −258M** now flagged `SUSPECT (UNVERIFIABLE)`, and only those two years |
| 9 | split-basis mismatch | market cap computed **in** the case file by the house rule, components exposed; non-integer split ratios **refused** as spinoffs | AAPL cap **$543.9bn** (was ~4x wrong); IBM now **REFUSED** on its 1.046 Kyndryl factor |

## The Test A defect is closed — and the first fix was wrong

**The first attempt invented a CONVENTION**: report both windows and "state which you rank on
and why." Challenged on the standing rule that *all judgements should be made by the corpus*,
I went back to the shelf instead of defending it. The corpus already governs this, and it says
something different:

> "Using precise numbers is, in fact, **foolish; working with a range of possibilities is the
> better approach.** **Usually, the range must be so wide that no useful conclusion can be
> reached.**" — **[E4-25]**, 2000 letter

**The window is not a choice to defend. It is part of the range.** The corpus does not ask you
to pick and justify; it asks you to carry the spread alongside the capex band and to accept
*"no useful conclusion"* as a real outcome. The invented convention would have forced a point
estimate out of exactly the input the corpus says to leave as a range.

Two things were checked before concluding the corpus was silent on the window itself: the
Owner's Manual's **"five-year rolling basis"** governs the *retention* test (does a retained
dollar produce a dollar of market value), not earnings averaging; and Graham's three-year
average is **off the shelf** under Prime Rule 4. The silence is real — but **[E4-25]** covers
the case anyway, so no convention was needed. **[E4-25]** added to the ledger, verified against
source. v4, the template and `run.py` now all state the corpus rule rather than the invention.

## The tool now reproduces the divergence

`tools/run.py` prints **both windows** and flags a material gap. Run today it recovers the
exact condition that split the two analysts:

```
TJX   other window (5-yr)  OE 3,444..4,050   DIVERGENCE -19.9%   ** MATERIAL **
HRB   other window (5-yr)  OE   615..  670   DIVERGENCE  +3.5%
```

The 5-year band brackets analyst 1's $3.76bn; the 3-year matches analyst 2's $4.8bn. **And it
discriminates correctly between the two companies** — TJX's window choice mattered and is
flagged, HRB's did not and both HRB analysts agreed. v4 and the run template now require both
windows, labelled a **CONVENTION** because the corpus sets none.

`check_framework.py` caught the amendment introducing unlabelled numbers and failed the build
until they carried that label. **PASS restored: 59 ledger ids in v4, 50 in the template, 0
phantom citations, 0 unlabelled numbers.**

---

**The honest summary: the specification held up; the plumbing did not. The plumbing is now
nine bugs and one spec defect better, because the tests were built to fail rather than to
reassure — and two of the nine were found by the analysts, not by me.**

## ADDENDUM 2026-08-28 — BT-17 (pre-registered b853dcf, results same day)
The loss leg replicated in two universes: the 13-anchor S&P re-score (loss frequency
20.5% vs 23.9% at 3y, 17.8% vs 18.8% at 5y, robust to no-data treatment) and a new
two-anchor micro-cap panel (38.5% vs 57.0% at 3y, 15.4% vs 60.1% at 5y, pooled;
survivorship-conditioned; pass-group n=13). The return leg trails at 3y/5y; no
market-beating claim arises. A split-factor bug (the July bug class, reintroduced)
was caught by reading the passed list - CMG/SMCI as fake micro caps - and the first
panel was withdrawn before commit. Full record: BT-17 pre-registration file.
