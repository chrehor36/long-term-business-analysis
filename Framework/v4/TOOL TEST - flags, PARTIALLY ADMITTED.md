# TOOL TEST — `tools/flags.py`. **VERDICT: PARTIALLY ADMITTED.**
**2026-08-27.** The second attempt at tooling Q3. Built against the corpus's own red-flag
checklist rather than against Legal Proceedings, tested on ten companies, and admitted in
part. Companion to `TOOL TEST - integrity check, NOT ADMITTED.md`, which this supersedes as
the live design.

## What changed since the first attempt

The first tool scanned **Item 3 Legal Proceedings** for regulatory keywords and was rejected
the same day: blind before ~2010, identical keyword counts across seventeen Wells Fargo
annual reports, and a window that swept in adjacent sections.

The corpus sweep completed 2026-08-26 then found the reason it could never have worked:
**Buffett's own red-flag checklist never looks at litigation.** **[E4-22]**, 2002 letter —
weak accounting, unintelligible footnotes, trumpeted projections — plus serial share
issuance **[E5-15]**. Three of those four are readable from the filed record.

**That is the whole case for rebuilding rather than patching, and it is corpus-sourced.**

---

# THE TEST SET

Ten companies. Four are carried over from the failed test so the two attempts can be
compared, including **WFC and KLAC — the two the first tool reported as clean.** Six are
chosen for the *new* flags: filers with defined-benefit plans, spinoff history, and known
share-count behaviour.

| | |
|---|---|
| carried over | WFC, C, KLAC, FITB, MO, TJX, ROST, ORLY |
| added for the new flags | GE (spinoffs), IBM (spinoff + recent issuance) |

---

# FLAG 4 — SHARE ISSUANCE. **ADMITTED.**

The corpus's most computable flag: *"companies that are **hell-bent on issuing shares**…
one of the surest indicators of a promotion-minded management, weak accounting, a stock
that is overpriced and — all too often — outright dishonesty"* **[E5-15]**.

**It only works because the test caught two bugs first.**

## Bug 1 — the split feed was a ten-year window. Caught on the second company.

`sources.split_factor_after()` read Yahoo's `range=10y` feed. Ross Stores split 2:1 in 2011
and again in 2015 — **both invisible** — so pre-2016 counts were never normalised:

```
ROST   printed series:  372.7 -> 324.4   (visibly falling)
       reported CAGR:   +1.64%/yr  "ISSUING"          <-- WRONG DIRECTION
       after the fix:   -2.67%/yr  "retiring"         <-- correct
```

**A silent failure pointing the wrong way** — the same class as the look-ahead bug that
voided four backtests. Fixed at source: splits are permanent facts, fetched over full
history and cached for a week. A pre-1970 split also crashed the call on Windows (negative
epoch); such a split necessarily predates any anchor, so skipping it is correct rather than
merely safe.

## Bug 2 — spinoffs are recorded as splits.

Yahoo files spinoff adjustments as split events. GE returned factors of **x0.200637**,
**x1.60509**, **x1.253**; IBM **x1.046** (Kyndryl). Adjusting a share count by those numbers
corrupts it.

**Fix: a clean split is a small integer ratio.** Anything else is flagged and the affected
years are declared unusable rather than printed as fact:

```
GE   2018-12-31  1,743.7  [x0.200637] ** NOT A CLEAN SPLIT RATIO - likely a SPINOFF **
     ** spinoff-corrupted years: 2012..2017 - flag 4 not usable here **
```

## Bug 3 — a single CAGR hid a live trend.

IBM's full-span figure said **−2.31%/yr, "retiring."** Its visible recent series does the
opposite: 892.8M in 2019 rising to 948.7M in 2025. A decade-old buyback was masking current
issuance — precisely Munger's *"cognition, misled by tiny changes involving low contrast,
will often miss a trend that is destiny."*

**Fix: report both windows and say so when they disagree.**

```
IBM  full  2010-12-31 -> 2025-12-31: -2.31%/yr  (retiring)
     5-yr  2020-12-31 -> 2025-12-31: +1.14%/yr  (ISSUING)
     ** the two windows DISAGREE in direction - the recent one is the live fact **
```

## Controls behave

TJX −2.57, ROST −2.67, ORLY −5.90, KLAC −1.68, MO −1.40, WFC −3.18, C −3.02 %/yr. All
retiring, all plausible, ORLY and KLAC correct across a 15:1 and a 10:1 split.

---

# FLAG 1b — PENSION ASSUMPTIONS. **ADMITTED AS A PROMPT ONLY.**

*"if its pension assumptions are fanciful, watch out"* **[E4-22]**. The tool prints the
assumed long-term return by year, dated to the filing, beside the contemporaneous 30-year
sovereign. **It sets no threshold** — "fanciful" is the reader's call, and inventing a
cutoff is exactly what v4 deleted 43 rules for.

Works where cleanly tagged: FITB (6.00% in 2018 falling to 2.43% in 2021, back to 5.51%),
TJX (6.50% → 6.00%).

**Two limits, both material:**

1. **False negative on Wells Fargo.** WFC has a defined-benefit plan and tags nothing under
   the concepts checked. **Absence is not coverage**, and the tool now says so in those words
   rather than printing "no DB plan."
2. **Cannot separate a company-level figure from one plan's.** Citigroup returns **1.50%**
   for 2022 — not plausible for a US pension, almost certainly a non-US or frozen plan.
   `companyfacts` does not expose the dimension, so the figure cannot be attributed.
   Where one filing carries several values for a date the tool now **REFUSES** the period
   instead of picking one; where it carries a single dimension-qualified value, **it cannot
   tell, and this remains unresolved.**

---

# FLAG 1a — SBC EXPENSED. **DEMOTED TO CONTEXT. Not a flag.**

Buffett's 2002 wording is *"if a company still does not expense options"* — written when
that choice was live. **Post-FAS 123R it is not.** A missing tag is a *tagging* fact:

- **MO** tags nothing under either concept and certainly expenses SBC — a false alarm.
- **C** reports its last SBC tag in **2012**; a naive reading gives "expensed: YES" on a
  fourteen-year-old fact.

The tool now prints the magnitude and the latest tagged year, marks a stale series, and
states explicitly that absence is **not** a finding that comp is unexpensed.

---

# FLAG 3 — TRUMPETED PROJECTIONS. **NOT ADMITTED. Wrong document.**

Tested on MO and TJX:

- **MO** — one match, and it is **capital expenditure** guidance. **[E4-22]** objects to
  *"earnings projections and growth expectations,"* not capex. **False positive.**
- **TJX** — no match, despite guiding EPS and comparable sales every quarter.
  **False negative.**

**The cause is structural, not a regex problem: earnings guidance lives in 8-K earnings
releases and call transcripts, not in the 10-K.** The tool was reading the wrong filing.
Left visible in the output, labelled NOT ADMITTED, so the next attempt starts here: the
target is the 8-K/EX-99 series, and the honest signal is Buffett's second-order one —
whether the company *consistently hits* its declared targets, which needs guidance history
matched against actuals.

---

# FLAG 2 — UNINTELLIGIBLE FOOTNOTES. **NOT BUILT.**

*"unintelligible footnotes usually indicate untrustworthy management"* **[E4-22]**. No
defensible implementation was found. A readability score on the notes would be a number the
corpus does not authorise, and note length tracks business complexity as much as evasion.
Recorded as not built rather than approximated.

---

# VERDICT

**PARTIALLY ADMITTED.** One flag of four is admitted outright, one as a prompt, one demoted
to context, one rejected, one unbuilt.

**What it may be used for:** assembling and dating the share-count record, and surfacing
pension assumptions to read. Every output is stamped with the date it became **public**, so
a run anchored at any date can cut the series there.

**What it may never be used for:** a Q3 verdict. A fired flag obliges a read; a clean sheet
is not a clearance. TJX's 2022 CPSC penalty remains the worked case for why — a real penalty
that is **not** a Q3 failure, and no computable test can make that distinction.

**Q3 remains a person reading the filed record and citing the ledger [E5-17].**

---

# WHAT THIS TEST WAS WORTH

It found **three bugs, two of them silent and one pointing the wrong way**, before any of
them reached a run file. The ten-company set cost one build and caught:

- a share count that was falling being reported as rising,
- four companies' worth of spinoff-corrupted history presented as fact,
- a live issuance trend hidden behind a decade-old buyback,
- and two flags that do not work at all.

**The first attempt nearly shipped a tool that reported Wells Fargo and KLA as clean. This
one nearly shipped a tool that reported Ross Stores as diluting its owners.** Both were
caught the same way: run it on ten names first and look at the output.
