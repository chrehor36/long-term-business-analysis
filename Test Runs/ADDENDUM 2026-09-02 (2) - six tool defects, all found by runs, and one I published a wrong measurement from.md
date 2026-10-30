# ADDENDUM — 2026-09-02 (second)
## Six tool defects, every one found by a run rather than by me — and one I had already published a wrong measurement from

**Operator rule 6: violations found later are corrected in an addendum, never by editing
history.** Operator rule 8 is the reason this file exists at all: *tools fetch and compute
and are forbidden to conclude; every flag is a prompt to read, never a score.* Three runs
completed on 2026-09-02 — **AATC, UAL and DKS** — and between them they found six defects in
tooling I wrote, two of them **today**, one of them in a measurement I had **already
published**.

---

## DEFECT 1 — `acquisition_flag()` had no recency bound, and I published 30% from it

**Found by: AATC.** Written this morning, used this afternoon, wrong by lunchtime.

The flag summed acquisitions with `ends = sorted(acq)[-window:]` — **the last five periods
the tag happens to carry, not the last five years.** Autoscope's only tagged acquisition is
a single payment in **fiscal 2010**, and the flag duly reported it as *"27% of market cap
inside the window."* A sixteen-year-old event on a company with no perimeter question at
all.

**And the error propagated straight into my own brief**, which told the AATC run that the
flag fired *"inside the window"* as though it were a fact about the company. The only reason
it was caught is that the brief also instructed the run to verify it. **Operator rule 8 held
because it was written down, not because I remembered it.**

**The published figure was wrong and is corrected here.**

| | claimed 2026-09-02 | corrected |
|---|---:|---:|
| no tagged acquisition in window | 88 | **173** |
| 5–15% of market cap | 72 | **55** |
| ≥15% of market cap | 74 | **47** |
| net-inflow sign | 38 | **25** |
| **READ-THE-FILING tier** | **112 = 30%** | **72 = 19%** |

The window is now bounded by the **owner-earnings window itself** — the same annual OCF
period ends `owner_earnings()` means by "five years" — so the numerator and the perimeter
test span the same years by construction rather than by coincidence.

**Sign convention corrected too, by DKS.** The XBRL element is a *payments* element, so a
negative value means cash acquired exceeded cash paid. **On the face of DKS's statement the
identical fact appears as a POSITIVE $257,095k inflow.** The note now describes the
substance rather than naming a sign the reader will not find in the filing.

---

## DEFECT 2 — `level_shift()` inverts on loss-making early years

**Found independently by AATC and by UAL, which is what makes it certain.**

The guard tested `earlier == 0` and not `earlier < 0`. Measured on constructed series:

| series | returned | truth |
|---|---|---|
| −300 mean → +300 mean | **−1.00, "STEP DOWN"** | a recovery. Exactly backwards. |
| −300 mean → −250 mean | 0.83, **"no step"** | still losing money |

UAL reported **−7.58 and "STEP DOWN"** on its own nine-year series because its 2017–2021
mean is −$543M. **A ratio is not defined across zero, and no threshold on it can be.**

**Where this bites is the part of the queue nobody was watching: TIER 3 IS DEFINED BY A
NEGATIVE BOTTOM BOUNDARY — fifteen names.** The population most likely to invert is precisely
the population the test was silently run on.

The fix **refuses the ratio rather than repairing it**, and returns a worded direction
instead. That is operator rule 8 again: a flag is a prompt to read, never a score.

---

## DEFECT 3 — two guards sat below `if __name__ == "__main__"` and could never fire

**Found by: UAL.** `level_shift()` and `best_year_dependence()` were defined *after* the
module's entry point in the file that owns them. Importable from outside, **dead inside the
screen itself** — `main()` never called either. **A guard that cannot fire in its own tool is
not a guard.** Moved above `main()`.

---

## DEFECT 4 — the sovereign was read from the wrong rung of the evidence ladder

**Found by: UAL, confirmed by DKS.**

`tools/sources.py` carried a docstring saying *"from the ISSUING AUTHORITY"* and a comment
saying *"never an aggregator"* — and then named **FRED DGS30**, a Federal Reserve Bank of
St. Louis redistribution of a Treasury series. **The module contradicted itself in the space
of four lines.**

CLAUDE.md was corrected on 2026-09-02 and `daily_fetch.py` had already moved to the Treasury
curve. **`sources.py` was missed — and `run.py` calls `sources.py`.** So every `run.py`-driven
run was taking its sovereign from the wrong rung while a comment two lines above forbade it.

DKS reports the sharper version: at the moment that run started, `sources.py` returned a bare
**`USD FAILED`** with no fallback at all. Now: **Treasury daily par curve primary, FRED as a
labelled fallback**, so the run file records which rung was used. Verified — **USD 5.27% at
2026-09-01**, which independently reproduces the rate DKS struck by hand.

---

## DEFECT 5 — no staleness gate on the *time* axis

**Found by: AATC.** Every guard in `floor_screen.py` watched the share count, the revenue or
the perimeter. **None watched the clock.**

Autoscope filed **Form 25 on 2023-01-06 and Form 15-12G on 2023-01-17** — it deregistered.
Its last 10-K is FY2021. **It sat in TIER 1 of the watchlist queue, priced at a live 2026
quote against a five-year-old cash-flow statement**, and nothing noticed. That is the
Hamilton Beach defect rotated onto the time axis.

`stale_filer()` added. **Note what it does not do:** deregistration is not a verdict on a
business. AATC still publishes audited annual reports (Boulay PLLP) on its own site — a
demoted-but-primary evidence class — and its run proceeded on them rather than closing
UNRESEARCHED. **The flag says the SCREEN cannot price the name, not that the name cannot be
read.**

---

## DEFECT 6 — the one the staleness gate uncovered, and the largest of the six

**Found by me, downstream of AATC's defect 5 — and it is a fix that was made once already
and never propagated.**

The staleness gate returned four names. **Three of them were not stale at all.**

| | screen's newest annual OCF | most recent annual filing on EDGAR |
|---|---|---|
| **APD** (Air Products) | **2011-09-30** | 10-K filed **2025-11-20** |
| **BDX** | 2021-09-30 | 10-K filed **2025-11-25** |
| **ESI** | 2022-12-31 | 10-K filed **2026-02-18** |
| AATC | 2021-12-31 | 10-K filed 2022-03-22 *(genuinely deregistered)* |

`floor_screen.annual()` wrote **`if by_end: break` — the first tag yielding ANY data won and
the rest were never read.** Air Products tags annual operating cash flow under the plain
element only through FY2011 and under `…ContinuingOperations` from FY2012 on. **The screen
took three years ending 2011 and stopped**, then divided a live 2026 quote by a fifteen-year-old
cash-flow statement.

**THIS EXACT DEFECT WAS FOUND AND FIXED IN `tools/sources.py` ON 2026-08-27, on Apple, and
that file's docstring still describes the fix: *"A tag list is a UNION."* It was never
propagated to `floor_screen.py`.** The screen has run with it ever since, including through
every sweep and every tier assignment.

**Measured cost: owner earnings move by more than 2% on 70 of 379 names.** The extremes are
severe — **APD from +$294M to −$2,845M**, ESI from $4M to $133M, BDX −31%, CGNX −35%,
DAL −15%, UAL −10%.

### What it did NOT cost, stated because the temptation runs the other way

**Not one name in the operator's queue changes tier.** Of 62 queue names re-computed, exactly
one moves materially — **CGNX, 1.48% → 0.97%, tier 2 either way.** The three worst-affected
names (APD, BDX, ESI) are **not on the operator's lists at all.**

**So: a systematic defect, running since at least 2026-08-27, touching 18% of the priced
universe, and it changes no verdict and no reading order in the work actually done.** Both
halves of that sentence are true and both belong in it.

**UAL is the one live intersection.** Its bottom boundary moves $1,467M → $1,327M. The UAL
run of 2026-09-02 built owner earnings **from the filings by hand** and reached its own
construction, so its conclusion is untouched — which is operator rule 4 doing exactly the job
it was written for. **No name reaches Q5 on XBRL alone**, and this is what that rule buys.

---

## MY OWN BRIEFS WERE WRONG IN FIVE PLACES, AND THE RUNS SAID SO

Recorded under **[E3-41]** — *"you must not fool yourself, and you're the easiest person to
fool"* — and **[E4-26]**: hunt disconfirming evidence hardest for your favourite hypothesis.
A brief is a hypothesis.

1. **UAL — I asserted audited standalone MileagePlus statements exist.** They do not. What
   exists is a 2020 lender-presentation exhibit labelled *"Historical amounts, as reported,"*
   **restated eight days later**, with the 144A memorandum never filed. I called it *"the
   best market test available"* and it is not audited at all.
2. **UAL — I sent the run to the wrong lease element.**
   `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability` reads **$(25)M**; total finance
   lease liabilities are $474M. The real leakage is **operating leases: $1,901M of ROU assets
   acquired in 2025**, plus **$427M of sale-leaseback gains booked inside operating income.**
   *"A run following the brief literally would have concluded there was no leakage."*
3. **UAL — I named SAVE as a competitor row candidate.** The US industry no longer carries
   [E3-28]'s eight competitors, and the run correctly made that a **finding** rather than a
   caveat.
4. **AATC — I assumed it was an SEC registrant.** It deregistered in January 2023, and my
   brief's entire evidence plan presumed 10-Ks that stop in FY2021.
5. **AATC — I stated defect 1 as a fact about the company.** Covered above.

**Against that: DKS reports "no arithmetic defect in the brief — all your figures reproduce
exactly," and ULTA reported the same.** The failures cluster in the parts of a brief that
assert what a document *says* without my having opened it. That is the pattern, and it is the
one operator rule 4 exists to prevent.

---

## AND THE ADDENDUM THIS SUPERSEDES IN ONE PLACE

`ADDENDUM 2026-09-02 - DKS and PINS re-priced…` told the DKS run to build owner earnings pro
forma **because the direction of the perimeter bias was not determinable from the screen.**
The run built it, and the answer is now on the record:

**Foot Locker's four-year mean owner earnings are +$51M to +$94M against $2.5bn of
consideration — 2.1% to 3.8%, below the bond**, before $500–750M of acquisition charges; two
of its last three standalone years are negative on both constructions; fiscal 2026 is guided
to a segment **loss**.

**So the screen's 4.34% was biased UPWARD, not downward.** The addendum was right to refuse to
guess the direction, and the filing settled it in the direction that makes DKS worse.
