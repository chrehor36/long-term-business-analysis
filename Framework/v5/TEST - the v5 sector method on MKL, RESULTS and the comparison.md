# TEST — the v5 sector method on MKL — RESULTS and the comparison (P5) — 2026-10-05
Against `Framework/v5/TEST - the v5 sector method on MKL, PREREGISTRATION.md` (c1593df1, committed before the run). The run:
`Framework/v5/tests/SM MKL - the v5 sector method.md`, by a session blind to the earlier MKL run and the v4 method. The earlier
run: `Test Runs/2026-09-02 Run - MKL Markel Group.md` (v4.1 and the v4 method). Both are opened together here for the first time.

## The verdict as pre-registered
| | Result | Why |
|---|---|---|
| P1 executability | **PASS** | every step gave its figure from Markel's filings; four inputs estimated and labelled, none moving a figure by more than about 1% |
| P2 no double count | **PASS** | all investment income removed from component 2; underwriting entered once, as a developed-basis line |
| P3 one answer for component 1 | **PASS, in form only** | C5 decided "gross" and one figure was reported; see below |
| P4 scope | **PASS** | no v4 id; every id in the v5 ledger; check 7 passes |

**By the rule written before the run, the method passes.** The box was **OUT at Q2** (developed underwriting about break-even
over ten years with the first five at a loss; the highest combined ratio of four specialty peers in every year shown).

## P5: the two runs side by side
| | 2026-09-02, v4.1 and the v4 method | 2026-10-05, v5 and the case's method | the difference is one of |
|---|---|---|---|
| box | Q2 OUT | Q2 OUT | agreement |
| component 1, float as free money | $36,935M (construction B) | $36,323M (gross, chosen by C5) | data (a later balance sheet); same construction |
| component 1, float as a liability | $13,804M (construction A, float and debt deducted) | $15,950M (net, for comparison; float only) | method (debt treated differently) and data |
| which one the method reports | **both**, 2.68x apart; "the ambiguity is larger than the company" | **gross**, decided by C5 | method |
| component 2, pre-tax | $652M three-year mean, built from adjusted operating income, which carries the calendar underwriting result | $321M to $377M, with underwriting restated to its developed accident-year result ($0 to +$55M a year) | method: the September figure counted calendar reserve releases as earning power; the new one does not |
| value range | B: about $3,300 to $4,150; A: about $1,530 to $2,270 | gross: $3,296 to $3,598; net: $1,651 to $1,954 | the same fork, at nearly the same places |
| price | $1,827.44 | $1,737.18 | data |

**What the comparison shows.** The new method fixes the double count and the calendar-year reading of underwriting: component 2
is now about half the September figure, because reserve releases from old years no longer count as this year's earning power.
It does **not** fix the fork in component 1. Both runs find the value is either about twice the price or about the price,
depending on whether float is free money. The September analyst reported both and called the high side unbelievable; the new
method reports the high side because C5's test passed on a ten-year average. The blind analyst found that the test fails on the
first half of the window (float cost 3.35% against a 2.55% long rate, 2016 to 2020), ignores equity about equal to the float,
and cannot see the reinsurance run-off announced in August 2025 ($3.56B of reserves). The switch alone moves value by about
$1,645 a share against a $1,737 price. P3 passed because the method gave one answer, not because the answer is sound.

## Defects found, for amendment
1. **C5, gross or net.** Decides the whole valuation, mechanically, on a decade average. Proposed: net by default; gross only if
   the developed cost of float is below the long rate in each half of the window, the equity behind the float is large relative
   to it, and no run-off or exit is announced. (Blind analyst's point 1.)
2. **C1, float.** Prepaid reinsurance premiums are not deducted; on Markel's book that overstates float by $3.1B to $3.9B and flips
   C7's bracket check. The filer's own float figure ($18,827M) deducts them. Proposed: deduct, and reconcile to the filer's own
   figure where one is published.
3. **C3, "restated by later development".** Readable by accident year (+$55M a year) or by calendar year (+$292M a year, carrying
   about $2.4B of releases from reserves set before the window). Proposed: accident year, with immature years flagged.
4. **Pre-tax against after-tax.** The method's component 2 is pre-tax; v5's Q7 values cash after tax. The two differ by $96 to $177
   a share here. Proposed: after tax, as Q7 requires.
5. **The operating-income trap.** A filer's "operating income" already contains the calendar underwriting result ($503M in 2025);
   it must be removed before the developed figure is added. Proposed: a written step.
6. Lesser: quarter-end deferred tax on unrealized gains (filed only at year-end); where equity-method investments go; growth bought
   by acquisition; C7 did not catch the gross-or-net dependence.

**Recommendation.** Amend the case on items 1 to 5 before adoption, write the amendment down, and repeat the blind MKL run against
the same pass rules plus one more: that component 1's construction is defended on the case's amended C5, with both figures shown.
The pre-registered verdict (pass) stands as recorded; the recommendation is the analyst's, made because the pass on P3 hides the
defect the test was built to catch.

## The repeat, after the amendment (2026-10-05)
`Framework/v5/tests/SM MKL 2 - the amended sector method.md`, blind to the first test run, this file and the September run, with
the contamination it declared (the amendment's text names the first test's directions). **P1, P2, P3, P4 and the added rule all
PASS; the box is OUT at Q2** (underwriting by accident year lost money in every year 2016 to 2020; the highest combined ratio of
four specialty peers). The amended gross-or-net rule decided **net**, all three of its tests failing on the filing (the first half
of the window cost more than the long rate; the reinsurance book in run-off; float about 1.10 times equity). Component 1 net
$14,727M (gross $35,587M shown); component 2 $177.5M pre-tax, $139.6M after tax; **value $1,389 to $1,555 a share against
$1,737.18**. The rebuilt float reconciled to the filer's own published figure within 0.2%. The remaining fork inside "net" (whether
the first construction's deductions survive) moves component 1 by about $310 a share and not the box. Ten lesser defects are
listed as open items in the adopted method's header. **The method was adopted the same day.**
