# ARCHIVE — RULINGS 1 THROUGH 14
## ⚠ THIS FILE NO LONGER GOVERNS ANYTHING. Superseded 2026-08-26.

**The governing document is `Framework/THE FRAMEWORK v4.md`.** Every ruling below has been
either resolved into that document, or deleted with its reasons recorded in
`Framework/INVENTIONS - deleted and why.md`.

**Why this file was demoted.** It reached 1,372 lines across 18 ruling sections numbered
1, 2, 4, 4-A, 4-B, 5, 4-C, 6, 3, 7, 5-A, 8, 9, 10, 11, 12, 13, 14 — out of order, with
roughly half of them existing to correct the other half. Running one company required
reading it end to end. That is the opposite of what the corpus asks for: *"the math is not
complicated"* [E3-27].

**It is kept, not deleted**, because it is the dated record of how each rule was reached
and of the errors found along the way. Read it as history. Do not apply it.

**Known dead letters within it, for the avoidance of doubt:**
- Ruling 1 (Statute starter test) — STATUTE-ONLY was deleted by the one-book decision
- Ruling 3 (erosion tripwire) — never entered the documents; curve-fit to 24 episodes
- Ruling 5 (35% margin base) — rejected; it quoted half of its own source passage
- Rulings 4/4-A's spread ladder below the +3% floor — invented above the corpus
- Ruling 9 vs 9-A (median vs current tier) — reconciled in v4 in favour of neither: the
  anchor is stated per run, with the window disclosed

---

# PENDING RULINGS — field-amendment candidates awaiting user decision
Per Prime Rule 6, these change how the framework operates and need your sign-off.
Each was surfaced by live runs or backtests; evidence cited. Ruling = one line each;
they then get dated FIELD AMENDMENT labels and enter the docs/template.

---

## RULING 1 — Does a Statute starter bypass Gate 8? — ✅ RATIFIED 2026-07-16
**Conflict:** P45 (dual-book: Statute grants starter size at wonderful-at-fair) vs
Gate 8 acceptance (asymmetry ≥2:1 AND price below Book Two threshold for ANY entry).
**Surfaced by:** Chubb run 2026-07-14 — Statute passed (6.55% vs 5.10%), Gate 8
asymmetry negative → starter blocked under the strict reading.
**RULED: option (c).** FIELD AMENDMENT — JULY 2026 (ratified 2026-07-16, user
decision): **a STARTER position is permitted on a Book One (Statute) pass even
when Book Two/Gate 8 does not clear, IF AND ONLY IF Gate 8's Q1 also passes —
the current price must imply an OE base at or below the CURRENT verified level
(i.e., the market is not already paying for growth).** Full size still requires
the complete Gate 8 (asymmetry ≥2:1 + Book Two threshold). Rationale: preserves
a real wonderful-at-fair path (the point of P45's dual-book design, and of the
Munger mandate) while keeping the one mechanical check that blocks paying for
heroic assumptions. Context at ratification: Ruling 4 had made Book Two
universal, so the strict reading (b) had quietly turned "starter size" into
dead letter across the entire Statute-only class (~50 names).
**Applied to the surfacing case: CB remains blocked** — its Gate 8 Q1 shows the
price implying ~110% of current core OE, so Chubb stays WAIT even under the new
rule. The ruling changes the class's rights, not the outcome that raised it.
**Operational note:** every Statute-only/whisper name now needs a Gate 8 Q1
check (implied-OE vs current) before its starter eligibility is known —
computable from data already in the run files.

## RULING 2 — What does "fortress" mean in Gate 4? — ✅ RATIFIED 2026-07-15
**Conflict:** the Workbook/Framework carry both "net cash positive" and "survives a
50% OE decline for 2 years" formulations.
**Evidence:** strict version eliminated HD 2026-07-14 (net debt ~$50B) and SHW
2026-07-15 (net debt ~$10.7B) — and the SAME test mechanically rejected Citigroup
mid-2007 (19:1 leverage; −95% followed) while the Statute alone would have bought it
[Backtest #12]. Softening to survival-only keeps HD/SHW but needs a leverage
carve-out to still catch Citi.
**RULED: option (b).** FIELD AMENDMENT — JULY 2026 (ratified 2026-07-15):
**"Fortress" is now a two-track test, split by business model:**
- **Non-financial businesses:** the fortress test is SURVIVAL, not net-cash. Passes
  if the business can service its debt and fund operations through a 50% owner-
  earnings decline sustained for 2 consecutive years without existential risk —
  judged from investment-grade rating, undrawn revolver + cash vs. near-term
  maturities, and a termed-out (not cliff-concentrated) debt schedule. Ordinary
  corporate leverage serving routine capital needs is not a Gate 4 disqualifier.
- **Financial businesses (banks, insurers, anything float- or balance-sheet
  levered):** the survival test applies PLUS a hard mechanical ceiling — assets ÷
  equity > 10:1 is an AUTOMATIC Gate 4 FAIL, no exception, no judgment call. Basis:
  "When assets are twenty times equity — a common ratio in this industry — mistakes
  that involve only a small portion of assets can destroy a major portion of
  equity." (1990 letter, on banking [E3-02 context]). Citigroup 2007 at 19:1 fails
  this ceiling mechanically — exactly the case the amendment exists to catch.
**Why not option (a):** net-cash-positive eliminated ordinary, resilient industrials
(HD, SHW) for carrying normal investment-grade debt — a false-positive-generating
rule in the other direction. **Why not option (c) alone:** a pure survival test
without the numeric leverage ceiling would have talked itself into approving
Citigroup's balance sheet in real time using the same qualitative reasoning
("investment grade, big revolver, diversified") that a levered financial can always
produce right up until it can't.
**Revisit condition:** none anticipated; re-open only if a financial institution's
capital structure evolves such that the 10:1 mechanical ceiling itself needs
recalibration (e.g., regulatory capital regime changes).

## RULING 4 — Book Two discount rate: replace WACC/ERP/beta with the Aesop
## certainty-spread method — ✅ RATIFIED 2026-07-15
**Problem:** Book Two's build-up DCF (WACC = risk-free + 5.5% ERP + company
premium) was always labeled a CONFESSED CONVENTION because it uses machinery
(CAPM, beta, market-wide equity risk premium) that Buffett and Munger have
explicitly and repeatedly rejected:
- Buffett, 1993 Letter: "...these academics compute with precision the 'beta'
  of a stock... In their hunger for a single statistic to measure risk,
  however, they forget a fundamental principle: It is better to be
  approximately right than precisely wrong... equating beta with investment
  risk also makes no sense."
- Munger, "Academic Economics" talk (UC Santa Barbara, 2003-10-03): "Berkshire's
  whole record has been achieved without paying one ounce of attention to...
  such obscenities as the capital asset pricing model, which we also paid no
  attention to."
A framework built from their own writings should not run its central
valuation math on the one piece of finance theory they call an obscenity.

**Evidence for the replacement — already in the ledger, previously tagged to
the Statute only, now recognized as also describing Gate 6's DCF structure:**
- **[E4-01]**, 2000 Letter (Aesop): "...you must answer only three questions.
  How certain are you that there are indeed birds in the bush? When will
  they emerge and how many will there be? What is the risk-free interest
  rate (which we consider to be the yield on long-term U.S. bonds)?"
- **[E3-13]**, 1994 Annual Meeting: "...in a world of 7 percent long-term
  bond rates that we would certainly want to think we were discounting
  future after-tax streams of cash at at least a 10 percent rate. But that
  will depend on the certainty we feel about the business. **The more
  certain we feel about a business, the closer we are willing to play it.**"
- **[E2-22]**, 1977 Fortune essay ("How Inflation Swindles the Equity
  Investor"): "...it seems reasonable to think of it as an equity coupon...
  those who buy equities receive securities with an underlying fixed return
  — just like those who buy bonds" — the "growing coupon" reading that
  governs terminal value (never a bare perpetuity at the sovereign rate —
  the same error [C10] already corrected once in this project).

**Refinement (same day, before first use)**: the ledger already had the
precise definition of "certainty" on file, previously tagged only to the
gate sequence's origin, not yet connected to the discount rate itself —
**[E3-10]**, 1993 Letter: "The primary factors bearing upon this evaluation
are: 1) The certainty with which the long-term economic characteristics of
the business can be evaluated; 2) The certainty with which management can
be evaluated, both as to its ability to realize the full potential of the
business and to wisely employ its cash flows; 3) The certainty with which
management can be counted on to channel the rewards from the business to
the shareholders rather than to itself..." — i.e. certainty is Gates 1-2
(factor 1: business economics + moat durability) AND Gate 3 (factors 2-3:
management competence and integrity), not moat class alone. **[E4-04]**,
2007 Letter, sharpens factor 1: "A moat that must be continuously rebuilt
will eventually be no moat at all[;] this criterion eliminates the business
whose success depends on having a great manager" — durability and
non-dependence on a single great manager are both part of "certainty."

**RULED (revised)**: Book Two's discount rate is no longer WACC. It is now
**sovereign yield + a certainty spread anchored on Gate 2's moat
classification, then adjusted by the Gate 3 verdict actually recorded** —
reusing judgments the framework already makes at every company run, rather
than importing beta/ERP from outside the corpus:
- WIDE moat (highest certainty) → **+1%** over sovereign
- NARROW moat (moderate certainty) → **+2–3%** over sovereign
- NONE moat (lowest certainty, commodity-like) → **+4–5%** over sovereign
- **+0.5–1% adjustment** on top of the moat-based band if Gate 3 carried a
  real, stated caveat (unverified management, a [P]/[U] score, a combined
  Chairman/CEO role, external/advisor-managed structure, etc.) — since
  factors 2-3 of certainty are management-specific, not folded into moat
  class. A clean Gate 3 (no caveats) applies no adjustment.
(Calibrated off E3-13's own 7%→10% example — a +3% spread for a business
Buffett felt reasonably, not fully, certain about. The exact numbers are a
labeled FRAMEWORK CONVENTION; the structure — certainty-based spread built
from the SAME three factors as the gate sequence itself, not a formula — is
sourced to E3-10/E3-13/E4-04 directly.)

Cash-flow projection keeps the existing, already-established conventions
(OE base; year-1 growth = lower of recent OE growth or guidance; fade
schedule by moat class). Terminal value uses a modest sustainable growth
rate per the E2-22 "growing coupon" reading — never the bare sovereign rate
as a perpetuity input.

**Why this also answers the "make Book Two a wider screen" question**: WACC
required a company-specific premium judgment call that made Book Two slow
and one-company-at-a-time. The new discount rate needs only two inputs
already computed for every company in every mechanical screen — the
sovereign yield (Statute) and the moat class (Gate 2) — making it
computable at the same scale as Book One, not just in individual deep-dive
runs.

**Supersedes**: Convention P43 (ERP build-up, confessed) is retired. Gate 6
Book Two in the Framework/Workbook docs and all future company runs use this
method; existing runs that built a WACC-style Book Two (none yet completed
as of this ruling) would need to be redone under this method if revisited.

## RULING 4-A — AMENDMENT to Ruling 4: the certainty spread was calibrated
## off a misread of its own source — ✅ RATIFIED 2026-08-01
**Surfacing case:** the TJX run of 2026-08-01. Book Two at the Ruling 4 rate
(sovereign 5.28% + WIDE 1.00% = 6.28%) produced a base IV of $132.10/share and a
max buy of $105.68. At a rate built from a correct reading of the same source
quote, base IV is ~$85. TJX fails either way, so no verdict changed — which is
exactly why this is the right moment to fix it, before a closer name turns on it.

**The defect, in Ruling 4's own words.** Ruling 4 states it was *"calibrated off
E3-13's own 7%→10% example — a +3% spread for a business Buffett felt reasonably,
not fully, certain about"* — and then assigns the highest-certainty class, WIDE,
a spread of **+1%**. That treats +3% as a midpoint to be discounted downward for
better businesses. The source says the opposite. [E3-13], 1994 Annual Meeting:

> "in a world of 7 percent long-term bond rates that we would certainly want to
> think we were discounting future after-tax streams of cash at **at least a 10
> percent rate**. But that will depend on the certainty we feel about the
> business. The more certain we feel about a business, the closer we are willing
> to play it. **We have to feel pretty certain about any business before we're
> even interested at all.** But there are still degrees of certainty..."

Two things follow that Ruling 4 missed. First, **"at least" makes +3% a FLOOR, not
a midpoint** — the rate moves up from there, never down. Second, *"we have to feel
pretty certain about any business before we're even interested at all"* means the
entire investable set has already cleared a high certainty bar before any spread is
assigned; the gates do that filtering. So a WIDE-moat name is not a candidate for a
spread *below* the floor — it is simply a name that sits at the floor rather than
above it. Ruling 4 inverted a floor into a midpoint and then discounted from it,
producing rates roughly 200bp too generous for precisely the wide-moat compounders
Book Two is most often pointed at.

**A second, structural error.** Ruling 4 places certainty exclusively in the
DENOMINATOR. [E4-01], the 2000 Letter, puts it first in the NUMERATOR:

> "you must answer only three questions. How certain are you that there are indeed
> birds in the bush? When will they emerge and how many will there be? What is the
> risk-free interest rate (which we consider to be the yield on long-term U.S.
> bonds)?"

Certainty is question ONE — how many birds are really there — and the third
variable is the **bare** long-bond yield. On the plain text of the 2000 letter,
certainty belongs in the cash-flow estimate; the discount rate is the risk-free
rate. The 1994 quote shows Buffett *also* flexing the rate. The two passages are
reconciled below rather than one being ignored.

**RULED — three changes, effective for all runs from 2026-08-01:**

**(1) The spread ladder is raised so its floor matches E3-13.**
- WIDE moat (highest certainty) → **+3%** over sovereign  *(was +1%)*
- NARROW moat → **+4–5%** over sovereign  *(was +2–3%)*
- NONE → **+6%+** over sovereign  *(was +4–5%)* — largely moot, since a NONE moat
  fails Gate 2 and never reaches Gate 6.
- The **+0.5–1% Gate 3 caveat adjustment** from Ruling 4 is retained unchanged.
These numbers remain a labeled **FRAMEWORK CONVENTION**; what is now corpus-sourced
is the **floor** (+3% over sovereign for the most certain business), taken directly
from E3-13's "at least a 10 percent rate" in "a world of 7 percent long-term bond
rates."

**(2) Certainty is expressed in BOTH places, numerator first.** Per E4-01, the
primary expression of certainty is a conservative cash-flow estimate — fewer birds,
later. The spread is the secondary expression, per E3-13. A run may not use an
aggressive growth path and then claim the certainty adjustment was "handled in the
discount rate"; the existing input rule (year-1 growth = LOWER of recent OE growth
or guidance) is the operative numerator discipline and is now explicitly part of
this ruling.

**(3) The Scream Test is restored to its source meaning, as a PRIOR test.**
[1996 Annual Meeting] —
> CHARLIE MUNGER: "Warren talks about these discounted cash flows. **I've never
> seen him do one.**" … "If it isn't pluperfect obvious that it's going to work
> out well, if you do the calculation, he tends to go on to the next idea."
> WARREN BUFFETT: "if you have to actually do it on — with pencil and paper, it's
> too close to think about. I mean, **it ought to just kind of scream at you** that
> you've got this huge margin of safety."

The framework's existing Scream Test (Book One and Book Two must agree, else
whisper-and-pass) is **kept** but is now the *second* of two tests. The first is
Buffett's: **if the conclusion depends on the model's precision, the answer is
already pass.** Operationally — if a name only clears Book Two inside a narrow band
of discount-rate and terminal-growth assumptions, that is a pass regardless of what
the base case says. This is what the Gate 6 sensitivity grid was always for; it is
now dispositive rather than advisory. A name must hold across a MAJORITY of grid
cells, not merely at the base case.

**Why not simply drop the spread and use the bare sovereign (pure E4-01)?**
Because E3-13 shows Buffett explicitly flexing the rate by certainty, in his own
words, in a shareholder-facing setting. Dropping the spread would discard a
directly-quoted practice in favour of a stricter reading of a different passage.
The reconciliation above keeps both and lets the numerator carry the primary load.

**Impact on completed work:** no company run has yet cleared Gate 6, so no verdict
is reversed. The TJX run of 2026-08-01 recorded Book Two at 6.28%; it is corrected
forward in that file rather than rewritten, per the project's standing rule. The
"Book Two is computable as a wide screen" conclusion in Ruling 4 is unaffected —
the inputs are unchanged, only the constants move.

**Revisit condition:** if a future run is decided by the difference between a +3%
and a +4% WIDE spread, that run should be treated as a whisper under change (3)
rather than resolved by re-litigating the constant.

## RULING 4-B — Book Two is a confessed departure: the model may reject, it may
## not authorize — ✅ RATIFIED 2026-08-01
**Why this exists.** Rulings 4 and 4-A both argue about *how* to run Book Two. Neither
confronts the prior question the corpus actually answers: whether Buffett runs one at
all. He does not. [1996 Annual Meeting] —

> CHARLIE MUNGER: "Warren talks about these discounted cash flows. **I've never seen
> him do one.**" (Laughter and applause)
> WARREN BUFFETT: "Yeah."
> CHARLIE MUNGER: "If it isn't pluperfect obvious that it's going to work out well, if
> you do the calculation, he tends to go on to the next idea."
> WARREN BUFFETT: "Yeah, it's sort of — it is true. You don't — **if you have to
> actually do it on — with pencil and paper, it's too close to think about.** I mean,
> it ought to just kind of scream at you that you've got this huge margin of safety."

And [E4-01], 2000 Letter, on the same discipline:
> "Alas, though Aesop's proposition and the third variable — that is, interest rates —
> are simple, plugging in numbers for the other two variables is a difficult task.
> **Using precise numbers is, in fact, foolish; working with a range of possibilities
> is the better approach. Usually, the range must be so wide that no useful conclusion
> can be reached.**"

Read together: the calculation is not the decision procedure. It is a check that is
expected to be inconclusive most of the time, and an idea that needs the calculation
to look good has already answered the question.

**The problem this creates for us.** Book Two exists in this framework and is unlikely
to be removed — it imposes useful discipline and makes the reasoning auditable. But a
DCF has a well-known property: **it will produce a number for anything.** Adjust the
growth path, the fade, or the terminal rate within entirely defensible ranges and the
same business is worth half or double. That is precisely why Buffett declines to lean
on it, and precisely how a framework built in his name can end up authorizing a
purchase he would not make — as Ruling 4-A demonstrated, where a spread we invented
made TJX appear payable at $105 when his own stated arithmetic says $68.

**RULED — Book Two is a CONFESSED DEPARTURE, and its authority is one-directional:**

1. **Book Two may REJECT. Book Two may not, by itself, AUTHORIZE.** If the model is
   what makes the case, there is no case. A favourable Book Two output is a necessary
   condition for entry, never a sufficient one.

2. **The pre-model verdict is recorded first and is binding.** Before Book Two is run,
   the run file records — in one line, from Gates 1-5 and the Book One yield alone —
   whether the opportunity is *obvious*: `PRE-MODEL: OBVIOUS` or `PRE-MODEL: NOT
   OBVIOUS`. If NOT OBVIOUS, the Gate 6 verdict is **WAIT** regardless of what Book Two
   subsequently returns. Book Two is still run and recorded (it is evidence, and it
   guards against a lazy "obvious"), but it cannot rescue the name. This is the direct
   operational form of "if you have to actually do it with pencil and paper, it's too
   close to think about."

3. **A wide range is a pass, not a puzzle to solve.** Per E4-01, "usually the range must
   be so wide that no useful conclusion can be reached" — that is the *expected* result,
   not a failure of the analysis. When the Gate 6 sensitivity grid fails to hold across
   a majority of cells (Ruling 4-A change 3), the run stops there. No re-running with
   narrower assumptions to obtain a conclusion; narrowing the assumptions to force an
   answer is the exact error the passage warns against.

4. **Standing confession, to appear at the head of Gate 6 Book Two in the Framework and
   Workbook documents:** *"FRAMEWORK CONVENTION — Buffett does not run this calculation.
   Munger, 1996: 'I've never seen him do one.' Book Two exists here to impose explicit
   assumptions and make reasoning auditable, not because the corpus endorses DCF as a
   decision procedure. It can veto a purchase; it cannot justify one."*

**What this does NOT change.** Book One, the gates, and the Statute are unaffected.
Book Two continues to be computed for every name reaching Gate 6, and Ruling 4-A's
corrected spreads continue to govern the arithmetic. The change is to what the output
is *permitted to do*.

**Impact on completed work:** none of the six runs of 2026-07-31 are affected — three
were eliminated before Gate 6 and three failed Gate 6 on both books. TJX would have
recorded `PRE-MODEL: NOT OBVIOUS` (a 2.75% yield against a 5.28% hurdle is not a
screaming margin of safety), which under this ruling makes its WAIT verdict final
before the DCF is even run — reaching the same answer by the shorter road.

**Why this is worth having even though it costs us optionality:** a framework assembled
from someone's writings should not be more willing to buy than the person it is
assembled from. Where our machinery is gentler than his stated practice, the machinery
is wrong. This ruling makes that asymmetry structural rather than something that has to
be caught by hand each time.

## RULING 5 — The margin of safety is softer than the corpus, and has no
## scaling rule — ⚠ PROPOSED 2026-08-01, **ANSWERED AND SUPERSEDED BY RULING 5-A
## (2026-08-26). Do not apply the 35% base proposed below.** The corpus search that
## Ruling 5 called for was run on 2026-08-26; it found that this ruling's own source
## passage [E3-26] says the opposite in its first half, and that the corpus answers
## the question directly at [E4-12]. See RULING 5-A near the end of this file.
**Raised by the standing principle: the corpus has the final say, and both books
derive from it.** Ruling 4-A established the diagnostic — an invented constant that
is GENTLER than the corpus is a defect, because a framework assembled from someone's
writings should never be more willing to buy than that person. Applying the same test
to the rest of Gate 6 finds the margin of safety failing it more severely than the
discount rate did.

**Our rule:** Max buy = Base IV x **0.80** (a 20% margin), or x 0.70 for a no-moat
business. Neither number appears anywhere in the corpus. A full-text search of the
shareholder letters and annual meetings returns **no numeric margin of safety at all**.

**What the corpus does give — the same illustration, twice, both far larger:**

> [1996 Annual Meeting] "...the margin of safety, which means, don't try and drive a
> 9,800 pound truck over a bridge that says it's, you know, **'Capacity: 10,000
> pounds.' But go down the road a little bit and find one that says, 'Capacity:
> 15,000 pounds.'**"

9,800 / 15,000 = a load at 65% of capacity — a **~35% margin**, not 20%.

> [1997 Annual Meeting] "...9,800 pound vehicle, you know, if the bridge is about six
> inches above the crevice that it covers, you may feel OK. But if it's, you know,
> **over the Grand Canyon, you may feel you want a little larger margin of safety, in
> terms of only driving a 4,000 pound truck**"

4,000 / 10,000 = a **60% margin** where the consequence of error is catastrophic.

And [1992 Letter], the qualitative statement our 20% was presumably meant to
operationalise: *"If we calculate the value of a common stock to be only slightly
higher than its price, we're not interested in buying."*

**Two defects, not one.**
1. **The level is too soft.** 20% is roughly half the margin his own illustration
   uses. Under our rule a business worth $100 is buyable at $80; under the 1996
   illustration it is buyable at ~$65.
2. **There is no scaling rule at all.** The 1997 passage makes the margin a FUNCTION
   of how bad it is to be wrong — six inches versus the Grand Canyon. Our 0.80/0.70
   split scales on moat class only, which is a proxy for business quality, not for
   severity of loss. Gate 5's inversions already record severity and are not used here.

**PROPOSED — for ratification, not yet in force:**
- Base margin **35%** (max buy = Base IV x **0.65**), calibrated to the 1996
  illustration rather than invented.
- Scaled to downside severity per 1997, using the inversion scores Gate 5 already
  produces: every mandatory inversion left **UNRESOLVED** adds **10 percentage
  points** of margin (so one [U] -> 45%, two -> 55%), approaching the ~60% of the
  Grand Canyon case when the thesis has several open holes.
- The exact numbers remain a labelled **FRAMEWORK CONVENTION**; what changes is that
  they are now calibrated to a corpus illustration instead of chosen freely, and the
  scaling principle itself is sourced to the 1997 passage.

**Why this is PROPOSED rather than ratified.** Unlike Ruling 4-A, this changes buy
prices for every future name by roughly 19% (0.80 -> 0.65), and it is a structural
change to Gate 6 — which under the project's own rule requires written approval
before it takes effect, not after. No completed run is affected: all six runs of
2026-07-31 failed Gate 6 by margins far wider than this, so ratifying it would change
no verdict already recorded.

**Also flagged by the same audit, not yet drafted as rulings:**
- **The Coca-Cola clause** (a generational moat may pass at **70% of the hurdle**) is
  a softener with no corpus number behind it, and is the same failure mode as Ruling
  4's spread. It should be re-derived or retired.
- **The 4% hurdle floor** is invented but errs STRICTER (it raises the hurdle when
  rates are low), so it survives this test. Recorded for completeness.
- **Size premiums** (+1% small/mid, +2% micro) likewise err stricter and survive.

## RULING 4-C — CORRECTION to Ruling 4-B: "obvious" means obviously going to
## work out, NOT obviously cheap — ✅ RATIFIED 2026-08-01
**This corrects a drafting error in Ruling 4-B, made the same day, against the very
quote 4-B cites.** Raised by the objection: the recent tightening works for great
businesses at cheap prices, but what about wonderful businesses at fair prices?

**The error.** Ruling 4-B requires a PRE-MODEL VERDICT of `OBVIOUS` or `NOT OBVIOUS`
before Book Two may run, and makes `NOT OBVIOUS` binding. The source is Munger, 1996:

> "If it isn't pluperfect obvious that **it's going to work out well**, if you do the
> calculation, he tends to go on to the next idea."

The test is about the **outcome** — is it obvious this will work out well — not about
the **price** being obviously low. Ruling 4-B was drafted, and applied to TJX, as
though "obvious" meant "obviously cheap." That silently converted a quality test into
a bargain test, and in combination with Book One's static-yield hurdle it closed the
only route by which a wonderful business at a fair price could ever be bought.

**Why that is a serious error and not a quibble.** [1989 Letter], "Mistakes of the
First Twenty-five Years":

> "if you buy a business for $8 million that can be sold or liquidated for $10 million
> and promptly take either course, you can realize a high return. But the investment
> will disappoint if the business is sold for $10 million in ten years and in the
> interim has annually earned and distributed only a few percent on cost. **Time is
> the friend of the wonderful business, the enemy of the mediocre.**"
> "It's far better to buy a wonderful company at a fair price than a fair company at a
> wonderful price. **Charlie understood this early; I was a slow learner.**"

A framework that only clears statistically cheap names has re-implemented the cigar-butt
method that this letter exists to repudiate. Rulings 4-A, 4-B and the proposed Ruling 5
all push in that direction; without this correction their combined effect is to make
the framework a Graham machine wearing a Buffett label.

**The concrete test case.** Coca-Cola, bought 1988-89 at roughly 15x earnings — about a
6.7% earnings yield — against long bonds yielding roughly 9%. **It fails Book One
outright**, by more than two points. Any reading of this framework that rejects
Coca-Cola is not modelling Buffett, and the burden is on the framework, not on Coke.

**RULED:**

1. **The pre-model verdict tests the OUTCOME, not the price.** It is recorded as
   `PRE-MODEL: OBVIOUS — the business will very likely be materially larger and still
   advantaged in ten years` or `PRE-MODEL: NOT OBVIOUS`. It is a judgment about
   certainty of the business, sourced to E3-10's three certainty factors, and it may be
   answered YES for a business trading at a full price. Cheapness is Gate 6's separate
   question and must not be smuggled into this one.

2. **Book Two's one-directional authority (Ruling 4-B point 1) is narrowed.** Book Two
   may not authorize on *its own arithmetic* — i.e. a name may not be bought because
   the DCF says so when the business case is not independently obvious. But where the
   pre-model verdict is OBVIOUS, a favourable Book Two IS a legitimate authorization,
   because the model is then confirming a judgment rather than manufacturing one. This
   is the "wonderful business at a fair price" path and it is hereby explicitly open.

3. **The Coca-Cola clause is retained pending re-derivation, not retired.** Ruling 5's
   audit flagged it as an unsourced softener. That was too hasty: it is the framework's
   own attempt to solve exactly this problem, and removing it while leaving 4-A, 4-B and
   Ruling 5 in force would eliminate the wonderful-at-fair path entirely. It stays in
   force until a properly derived replacement exists.

4. **Standing directional check, both ways.** Ruling 4-A established that a convention
   softer than the corpus is a defect. This ruling establishes the converse: **a
   convention STRICTER than the corpus is also a defect** where it would reject
   purchases Buffett actually made. Both tests apply. The corpus is the ceiling and the
   floor, not merely the ceiling.

**Impact on completed work:** TJX's Gate 6 recorded `PRE-MODEL: NOT OBVIOUS` on the
mistaken cheapness reading. Under the corrected test TJX is arguably `OBVIOUS` — a WIDE
and widening moat, 4/4 inversions resolved, 23.6% ROIC. Its verdict is nonetheless
unchanged: Book Two returns $85.36 base IV against a $157.34 price, so a favourable
Book Two is simply absent. WAIT stands, now for the right reason — the price, not a
mis-specified gate.

**Open question this exposes, not resolved here:** Book One is a static yield test and
is therefore structurally hostile to compounders in a high-rate environment. At a 5.28%
sovereign it will reject almost every wonderful business. Whether that is correct
behaviour (rates are gravity — the corpus supports the comparison) or whether the
Statute needs a growth-aware form for WIDE-moat names is the substance behind the
Coca-Cola clause and should be settled deliberately, with the Coke 1988 numbers as the
worked test case.

## RULING 6 — THE PRICE LADDER: every Gate 6 must answer three price questions,
## not one — ✅ RATIFIED 2026-08-01
**Problem.** Gate 6 has been returning a single verdict — BUY-ELIGIBLE, STATUTE-ONLY,
or WAIT. For a business that passes Gates 1-5 and fails only on price, "WAIT" throws
away almost everything the run just established. It does not say what you are waiting
FOR, it does not say what the current quote actually pays you, and it forces the whole
analysis to be re-done if the price ever moves.

**RULED — every run reaching Gate 6 records a PRICE LADDER and the reverse-DCF
diagnostics beneath it. The three rungs are stated in dollars, always:**

    CHEAP    = IV x (1 - MOS)   the price at which you buy WITH a cushion
    FAIR     = IV               pay intrinsic value, earn exactly the discount rate
    CURRENT  = the quote        stated as a multiple of FAIR, premium or discount

**and three diagnostics that make the number decision-useful:**

1. **IRR at the current price** on the base-case forecast, stated against the sovereign
   as "X points of equity premium." This is the single most honest number in the whole
   framework: it says what you are actually paid for taking equity risk.
2. **Implied year-1 OE growth** required to justify the current price, set beside what
   the base case actually assumes. This is Gate 8's reverse-DCF logic, and it belongs
   here rather than only after a Gate 6 pass — its diagnostic value is HIGHEST on the
   names that fail, because it names the specific thing that would have to change.
3. **Years for the yield-on-cost to reach the sovereign** at a stated growth rate, when
   the current earnings yield is below it.

**Two verdicts, stated separately and never merged.** The run concludes with a business
verdict and a price verdict as distinct findings — e.g. *"a wonderful business; not a
fair price."* Merging them is what produces both classic errors: rejecting a great
business because it is expensive today, and buying a mediocre one because it is cheap.
The 1989 Letter ("Time is the friend of the wonderful business, the enemy of the
mediocre") and the cigar-butt passage are the same warning from opposite ends.

**Why this matters operationally.** A WAIT with a ladder is a standing order: the
business work is banked, the exit metric is pre-committed at Gate 5, and if the price
arrives you can act without re-litigating whether the business is any good. A WAIT
without one is just a shrug that has to be repeated from scratch.

**Worked output at ratification (2026-07-31 prices, sovereign 5.28%):**

| | CHEAP | FAIR | CURRENT | vs fair | IRR now | implied g1 |
|---|---|---|---|---|---|---|
| TJX  | $68.29 | $85.36  | $157.34 | 1.84x | 5.69% (+0.41) | 24.3% vs 9% assumed |
| DOV  | $98.29 | $122.86 | $204.62 | 1.67x | 7.19% (+1.91) | 16.9% vs 4% assumed |
| SBUX | $14.08 | $17.60  | $105.25 | 5.98x | 3.83% (-1.45) | 54.6% vs 6% assumed |

Note what the ladder exposes that the old single verdict hid. All three read "WAIT",
but they are not remotely the same case: **Dover is the only one whose current price
pays a real equity premium** (+1.91 pts) — it is expensive rather than absurd.
**Starbucks pays LESS than Treasuries** (-1.45 pts) even on a recovery assumption that
is already generous relative to the input rule, and needs 54.6% growth to justify its
quote. And TJX, the best business of the three, pays +0.41 pts — you are being handed
a bond-like return for owning a retailer.

**MOS caveat:** the ladder above uses the current 20% margin. If Ruling 5 is ratified
(35%, scaled by unresolved inversions), every CHEAP rung drops accordingly — TJX to
~$55, DOV to ~$80, SBUX to ~$11. The FAIR rung is unaffected, since it is IV itself.

## RULING 3 — P48 candidate: THE EROSION TRIPWIRE (fix for backtest false positives)
**Problem:** all 3 backtest false positives (IBM '11, INTC '19, Kodak '00) are
moat-direction cases — cheapness passed the arithmetic while the franchise eroded in
public data. A hard mechanical screen CANNOT fix this without killing true positives
(AAPL '16 revenue −8% at purchase; Moody's '09 −22%; Japan '20 COVID-crushed) —
cyclical dip and secular decay are identical to a screen.
**Proposed amendment (P48):** before any Statute PASS is recorded, compute from the
last 3 annual filings:
- T1: revenue below its level 3 fiscal years prior, OR down >15% vs prior year
- T2: gross margin down >200bp cumulative over the last 2 fiscal years
- T3: the current 10-K names a substitute product/technology taking share
If ANY trips → Statute verdict LOCKED at "SUSPENDED — substitution-vs-cycle ruling
required." The analyst must answer, in writing with filing data: is the erosion
demand-cyclical or substitution-driven? Substitution-driven or unanswerable → treat
as Gate 2 FAIL. Demand-cyclical with evidence → proceed, ruling recorded. The
tripwire never auto-blocks and never lets erosion slide through unexamined.

**Tested against all 24 backtest episodes:**
| Episode | Tripped? | Ruling that follows | Effect |
|---|---|---|---|
| Kodak '00 (FP) | T1 ✓ (rev < 1996-97) + T3 ✓ (digital in 10-K) | substitution → FAIL | **FIXED** |
| INTC '19 (FP) | T2 ✓ (GM 61.7%→58.6%, −310bp) + T3 ✓ (process delays, AMD/TSMC) | substitution/technology → FAIL | **FIXED** |
| IBM '11 (FP) | T1 marginal (2010 rev above 2007, below 2008); T2 no (GM RISING); T3 partial (cloud risk language) | question forced but honestly answerable either way in 2011 | **PARTIALLY fixed** — IBM fooled Buffett for 6 years; no honest mechanical rule catches it |
| Moody's '09 (TP) | T1 ✓ (−22% y/y) | demand-cyclical (issuance collapse; ratings duopoly intact, no substitute) → written, proceeds | friction only, not blocked ✓ |
| AAPL '16 (TP) | none (rev above 3-yr; GM stable) | n/a | untouched ✓ |
| Japan '20 (TP) | T1 ✓ (COVID) | commodity/demand cycle → written, proceeds | friction only ✓ |
| All other TPs/hits | no trips | n/a | untouched ✓ |

**Net effect: 2 of 3 false positives eliminated outright, the third gets the right
question forced in writing; ZERO true positives blocked.** Residual honesty: IBM-class
failures (margins rising while the franchise hollows) remain uncatchable by mechanics —
that is Gate 2's irreducible job, which live runs already require before valuation.
**Status: OPEN — proposed, tested, not yet in the docs.**


---
---

# THE 2026-08-26 CORPUS AUDIT: FOUR QUESTIONS PUT TO THE TEXT

Raised by the TJX refresh run (2026-08-26). The operator asked that each question be
answered from the corpus rather than from judgment. **All five rulings below were
RATIFIED by the operator on 2026-08-26 and are IN FORCE for every subsequent run.** What follows is the result of that
search: 13 new ledger entries (E2-23 to E2-25, E3-24 to E3-26, E4-10 to E4-13,
E5-08 to E5-10), and five rulings.

**The headline: three of the four questions turn out to be the same question.** The
corpus contains a direct, procedural statement of how to build a valuation, it names
the exact variables we have been loading with extra conservatism, and it tells us not
to. That statement is Ruling 7 below and it decides Questions 1, 3 and 4.

**Safety check applied to all five rulings (Ruling 4-C, "the corpus is the CEILING AND
THE FLOOR").** These corrections move the framework toward being MORE willing to buy.
That direction is dangerous, so each was tested against TJX at today's price. Adopting
every correction at its most generous setting (maintenance capex floored at D&A, MOS cut
to 10%, Book One anchored to normal earning power) still gives Book One 3.48% against a
5.19% hurdle and Book Two a FAIR of $83.91 against a $137.75 price, i.e. **still a
double FAIL, price still 1.64x fair.** The corrections do not manufacture a buy. They
change a rejection that was arithmetically rigged into a rejection that can be reasoned
about.

---
## RULING 7: THE WINDAGE RULE. Realism at every variable, conservatism applied ONCE, at the end.
## ✅ RATIFIED 2026-08-26. Governs Rulings 5-A, 9 and 10.

**The source [E4-11], 2004 annual meeting.** The question asked was precisely ours:
"when you assess a business and derive its intrinsic value, how do you estimate the
future growth of the business, and how do you decide what margin of safety to use?"

> "You calculate, I think you take all of the variables and calculate them reasonably
> conservatively. **But you don't try and put too much windage in at every level.** And
> then when you get all through, you apply the margin of safety. So I would say,
> **don't focus too much on taking it on each variable in terms of the discount rate and
> the growth rate and so on.** But try to be as realistic as you can on those numbers,
> but with any errors being on the conservative side. And then when you get all through,
> you apply the margin of safety."

and, restated two paragraphs later after the earthquake-pricing illustration:

> "I want to be conservative at all the levels and then I want to have that significant
> margin of safety at the end."

**What the framework currently does.** On the 2026-08-26 TJX run, conservatism was
applied at six separate places, compounding:

| # | Where | What it did |
|---|---|---|
| 1 | Numerator, capex | total capex used as if it were maintenance capex |
| 2 | Numerator, WC | omitted entirely, see Ruling 10 |
| 3 | Numerator, base | anchored to the LOWEST verified tier, a pandemic-shutdown year |
| 4 | Numerator, growth | g1 = LOWER of recent OE growth or guidance |
| 5 | Rate | Aesop certainty spread, +3.00% for a WIDE moat |
| 6 | End | 20% margin of safety |
| 7 | proposed | 35% MOS (Ruling 5) and a Gate 3 caveat spread |

Buffett names items 4 and 5 explicitly ("the discount rate and the growth rate") as the
places NOT to load. The framework loads both, plus three more, and then applies the MOS
on top of all of it.

**RULING.** Conservatism is applied at ONE place, the margin of safety, at the end.
Every input above it is set to the **realistic** value, with ties broken conservatively.
Concretely:
1. **Inputs are estimates, not floors.** Each variable is set to its best honest
   estimate. "Errors on the conservative side" means breaking a genuine tie downward,
   not selecting the worst observed value.
2. **Certainty is priced in exactly ONE place.** The framework has already ratified
   that place: the Aesop spread in the discount rate (Ruling 4, as amended by 4-A).
   Therefore the MOS may NOT also scale with certainty. It scales with **downside
   severity** instead. See Ruling 5-A.
3. **A conservatism already applied at an earlier gate may not be re-applied at Gate 6.**
   This is the specific defect Ruling 9 corrects.
4. **Every run states its windage count.** If a run applies conservatism at more than
   one place above the MOS, it says so and justifies it in writing.

**Standing tension, recorded not hidden.** [E4-01] (2000 letter) says the third Aesop
variable is "the risk-free interest rate (which we consider to be the yield on long-term
U.S. bonds)", i.e. the BARE sovereign, with certainty handled in the numerator by
question one. [E3-13] (1994 meeting) says the rate itself moves with certainty. These
two are not fully reconcilable. Ruling 4-A resolved it by putting certainty in the rate
and requiring honest numerator inputs. Ruling 7 does not reopen that. It only forbids
paying for certainty a third and fourth time.

---
## RULING 5-A: ANSWER TO RULING 5. The 35% base is REJECTED. The MOS scales with
## DOWNSIDE SEVERITY, not with certainty, and for a name that clears Gates 1-5 the
## corpus supports a SMALLER margin than our standing 20%.
## ✅ RATIFIED 2026-08-26. Supersedes the proposal in Ruling 5.

**Ruling 5's citations are arithmetically correct and were quoted incompletely.**

The bridge [E3-25], 1996 meeting: "don't try and drive a 9,800pound truck over a bridge
that says it's, you know, 'Capacity: 10,000 pounds.' But go down the road a little bit
and find one that says, 'Capacity: 15,000 pounds.'" 9,800/15,000 = 0.653, so ~35%.
The Grand Canyon variant [E3-26], 1997 meeting: a 4,000 pound truck on a 10,000 pound
bridge = 0.40, so ~60%. Ruling 5 read both correctly.

**What Ruling 5 did not quote is the first half of the same 1997 answer** [E3-26]:

> "Obviously, **if you understood a business perfectly, the future of a business, you
> would need very little in the way of a margin of safety.** So the more volatile the
> business is, or possibility is, but assuming you still want invest in it, the larger
> the margin of safety."

and the closing line of the Grand Canyon passage: **"So it depends on the nature of the
underlying risk."**

**And the corpus answers our exact question directly** [E4-12], 2007 meeting. The
questioner asked: "in a dominant, long-standing, stable business, would you demand a
10 percent margin of safety and, if so, how would you increase this in a weaker
business?"

> "We favor the businesses where we really think we know the answer. And, therefore, if a
> business gets to the point where we think the industry in which it operates, the
> competitive position or anything is so chancy that we can't really come up with a
> figure, **we don't really try to compensate for that sort of thing by having some extra
> large margin of safety. We really want to try to go on to something that we understand
> better.** So if we buy something like See's Candy as a business or Coca-Cola as a stock,
> **we don't think we need a huge margin of safety** because we don't think we're going to
> be wrong about our assumptions in any material way. [...] **We'd love to find them when
> they're selling at 40 cents on the dollar but we will buy those as much closer to a
> dollar on the dollar. We don't like to pay a dollar on the dollar, but we'll pay
> something close.**"

The fat-man illustration in the same answer puts a number on "close": the business is
"300 pounds or 325 pounds", and "if we can come in at the equivalent of 270 pounds, we'll
feel good". That is 270/300 = 0.90, i.e. **a 10% discount to the low end of the range.**

**Two rules follow, and the first is the one the framework was missing.**

1. **A large margin of safety is NOT the remedy for uncertainty. Walking away is.**
   "we don't really try to compensate for that sort of thing by having some extra large
   margin of safety. We really want to try to go on to something that we understand
   better." In our architecture, uncertainty is already handled: Gate 1 (circle of
   competence), Gate 2 (moat class), Gate 5 (inversions) and the Aesop spread all exist
   to price or exclude it. Loading it into the MOS as well is the windage Ruling 7
   forbids.
2. **The MOS carries downside SEVERITY: what happens if you are wrong.** Six inches above
   the crevice versus the Grand Canyon. That is a question about permanence of loss, not
   about forecast variance, and nothing else in the framework prices it.

**RULING. The margin of safety becomes a severity ladder, applied to a name that has
already passed Gates 1-5:**

| Condition | MOS |
|---|---|
| Base: WIDE moat, 4/4 inversions resolved, Fortress passed on the survival track with room | **10%** |
| NARROW moat | +10 pts |
| Each Gate-5 inversion left UNRESOLVED | +10 pts |
| Fortress passed but tight (cash < 2x debt due inside 24 months) | +10 pts |
| Any risk of PERMANENT capital loss identified at Gate 5 (leverage, single-customer, single-regulator, technological obsolescence): the Grand Canyon case | **floor of 50%, and consider that this is a Gate 5 FAIL instead** |

Ceiling of 60% (the Grand Canyon figure). A name requiring more than that should have
failed an earlier gate.

**Why this is not a softening.** It LOWERS the margin only for names that have already
cleared five gates including 4/4 inversions, which is precisely the case where the corpus
says the margin should be small. It RAISES it above the current flat 20% for every
NARROW-moat name, every name with an unresolved inversion, and every name with a tight
balance sheet, which the flat 20% treated identically to a fortress compounder. The flat
20% was wrong in both directions at once, which is the Ruling 4-C failure mode.

**Effect on TJX at $137.75:** CHEAP moves from $57.47 (20%) to $64.66 (10%). Price is
2.13x that line. **Verdict unchanged: WAIT.**

**Effect on Ruling 5's proposal:** its 35% base would have been the single largest
tightening ever applied to the framework, and it was derived from a passage whose other
half says the opposite. **Ruling 5 is not ratified. It is answered and closed.**

---
## RULING 8: ANSWER on the Gate 3 buyback caveat. NO rate penalty. It is a Gate 3
## flag with a defined test, and it carries a mandatory humility clause.
## ✅ RATIFIED 2026-08-26.

**The corpus is unambiguous that overpaying destroys value.**

[E4-10], 1999: "the continuing shareholder is penalized by repurchases above intrinsic
value. **Buying dollar bills for $1.10 is not good business for those who stick
around.**"

[E5-09], 2012: "**never forget: In repurchase decisions, price is all-important. Value is
destroyed when purchases are made above intrinsic value.**"

[E5-08], 2011, which supplies the actual test: "Charlie and I favor repurchases when two
conditions are met: **first, a company has ample funds** to take care of the operational
and liquidity needs of its business; **second, its stock is selling at a material
discount to the company's intrinsic business value, conservatively calculated.**" And:
"The first law of capital allocation, whether the money is slated for acquisitions or
share repurchases, is that **what is smart at one price is dumb at another.**"

**But the corpus is equally clear about what to DO with the finding, and it is not what
we proposed.** Three constraints:

1. **Buffett attaches an explicit humility clause in the same breath** [E4-13], 1999:
   "Charlie and I admit that we feel confident in estimating intrinsic value for **only a
   portion** of traded equities and then **only when we employ a range of values, rather
   than some pseudo-precise figure.** [...] In defense of those companies, I would say
   that **it is natural for CEOs to be optimistic about their own businesses. They also
   know a whole lot more about them than I do.**"
2. **He explicitly declines to read overpayment as a management indictment by default**
   [E5-08], 2011: "Sometimes, of course, **infractions, even serious ones, are innocent;
   many CEOs never stop believing their stock is cheap.**"
3. **When his own investees did exactly this, he recorded the reduced benefit and did
   not reprice the business.** 1997 letter: "the repurchases that Coca-Cola, The
   Washington Post and Wells Fargo made in past years at very low prices benefitted
   Berkshire far more than do today's repurchases, made at loftier prices." He noted it,
   held all three, and did not raise a discount rate on any of them.

**RULING.**
- **No caveat spread is applied to the discount rate for buybacks above IV.** It is
  windage in the rate (Ruling 7), and it would let a disagreement about OUR IV estimate
  silently reprice the BUSINESS. The Gate-3 caveat spread stays reserved for what it was
  built for: doubts about integrity, candor and competence in running the operation.
- **A new Gate 3 line is added instead, the two-condition test [E5-08], scored and
  recorded:** (1) ample funds for operations and liquidity; (2) repurchases made at a
  material discount to conservatively calculated IV. Score PASS / FAIL / UNKNOWN.
- **A FAIL on condition (2) is recorded as a CAPITAL ALLOCATION FLAG, and it must be
  stated with the humility clause attached**, naming that the judgment rests on our own
  IV range and that management knows more about the business than we do.
- **The flag becomes a Gate 3 FAIL only when it is repeated and unrepentant across three
  or more years AND accompanied by an integrity or candor failure.** Price-insensitive
  buying alone is a defect in capital allocation, not evidence of dishonesty.
- **The flag DOES bind at Gate 7.** Where a buyback flag is live, the position is sized
  DOWN, because a price-insensitive repurchaser will convert your future retained
  earnings into stock at prices you would not pay. Sizing is where the corpus lets this
  cost land, not the valuation.

**TJX ruling on the record:** condition (1) PASS (cash $6.0B, 6.0x total debt).
Condition (2) **FAIL** (8.9M shares at a $159.33 average in H1 FY27 against a $71.84
Book Two IV; roughly $779M transferred from continuing holders). **CAPITAL ALLOCATION
FLAG raised, with the humility clause: this rests on our IV range, which may be too low,
and TJX management knows the business better than we do.** Not a Gate 3 FAIL. It binds
Gate 7 sizing if TJX ever reaches the ladder. Discount rate stays at 8.19%.

---
## RULING 9: ANSWER on Book One anchoring. The trough-year anchor is a DEFECT and is
## RETIRED. Book One reads NORMAL earning power. The bad year is a survival test, and
## it is already run at Gate 4.
## ✅ RATIFIED 2026-08-26. This is the sharpest of the four findings.

**The corpus never anchors valuation to the worst observed year. It anchors to normal,
consistent, representative earning power, and runs the bad year separately as a survival
question.** Four passages, spanning 1983 to 2016:

[E2-24], 1983, See's, the most-cited private purchase in the corpus:
> "See's was earning about $2 million after tax at the time, and such earnings seemed
> **conservatively representative of future earning power** in constant 1972 dollars."

[E2-25], 1987 acquisition criteria, repeated verbatim in the 1982 through 1987 letters:
> "(2) **demonstrated consistent earning power** (future projections are of little
> interest to us, nor are 'turnaround' situations)"

[E5-10], 2016: "in estimating our **normal earning power**"

**And the decisive one** [E3-24], 1990, Wells Fargo, bought in the middle of a banking
panic. Buffett values it off CURRENT earnings ("we purchased our 10% interest in Wells
Fargo for $290 million, **less than five times after-tax earnings**, and less than three
times pre-tax earnings"), then handles the disaster case in a SEPARATE paragraph:

> "Consider some mathematics: Wells Fargo **currently earns** well over $1 billion pre-tax
> annually after expensing more than $300 million for loan losses. If 10% of all $48
> billion of the bank's loans, not just its real estate loans, were hit by problems in
> 1991, and these produced losses (including foregone interest) averaging 30% of
> principal, **the company would roughly break even. A year like that, which we consider
> only a low-level possibility, not a likelihood, would not distress us. In fact, at
> Berkshire we would love to acquire businesses or invest in capital projects that
> produced no return for a year, but that could then be expected to earn 20% on growing
> equity.**"

This is the exact question, answered. A catastrophic year is (a) modelled explicitly,
(b) tested for SURVIVAL, and (c) declared not to reduce the value of a business that can
then earn well on growing equity. It is never substituted for the earnings in the
valuation.

**What our rule does instead.** The range-anchoring field amendment reads Book One off
the lowest verified OE tier. For TJX that tier is FY2021, a year in which stores were
legally closed by government order. The resulting Book One pass price is **$6.78**, which
is not a price. It is a rejection dressed as arithmetic, and it would reject Wells Fargo
in 1990, See's in 1972, and every business that has ever had one bad year.

**It is also a double count.** Gate 4's Fortress Test already runs the bad year: "survives
a 50% OE decline for 2 consecutive years without existential risk." TJX passed it, and
passed it on the strength of the very year we then use to destroy its valuation. The
framework tests the disaster at Gate 4 and then charges for it again at Gate 6. That is
the Ruling 7 violation in its purest form.

**RULING.**
1. **Book One's anchor becomes NORMAL earning power: the median of the verified annual
   OE tiers over the last five fiscal years**, which is representative, filing-sourced,
   mechanically computable, and immune to a single distorted year in either direction.
2. **Years distorted by a government-mandated shutdown or an equivalent externally
   imposed suspension of operations are EXCLUDED from the tier set**, and the exclusion
   is stated in writing with the reason. This is not a licence to exclude bad years.
   Recessions, demand cycles, competitive losses, margin compression and management
   error all STAY IN. The exclusion covers only a year in which the business was
   prevented from operating.
3. **The trough tier is still computed and still reported**, and it moves to where the
   corpus puts it: **Gate 4, as the survival input.** Nothing is lost, it is relocated to
   the gate that already asks the question.
4. **Range anchoring survives intact in its original purpose:** thresholds rise only on
   published filings, never on a quote. That rule was always about preventing price from
   contaminating value, and it is untouched.

**Effect on TJX:** Book One moves from 0.26% (FY2021 shutdown anchor) to roughly 3.0% to
3.5% on normal earning power, against a 5.19% hurdle. **Still a FAIL.** The verdict does
not change. What changes is that the failure is now legible: TJX earns about three and a
half percent on your money against a risk-free five and a fifth, which is a fact you can
reason about, rather than a number produced by dividing today's price into the worst
year of a retailer's life.

**This also gives the STILL-OPEN question in CLAUDE.md its first real answer.** Book One
was called "structurally hostile to compounders." Part of that hostility was never the
static-yield design at all. It was this anchoring rule. Correcting it does not make
Book One friendly to compounders (TJX still fails, and Coca-Cola 1988 at a 6.7% yield
against 9% bonds still fails), but it isolates the remaining question to where it
actually lives: whether a static yield test should govern a business whose yield grows.
That question stays open, with Coca-Cola 1988 as the worked case, as before.

---
## RULING 10: ANSWER on the owner-earnings working capital term. Method C is adopted.
## And the same sentence exposes a SECOND defect: we have been using total capex where
## the corpus says maintenance capex.
## ✅ RATIFIED 2026-08-26.

**The governing text** [E2-23], 1986 letter, quoted in full because every clause does
work:

> "These represent (a) reported earnings plus (b) depreciation, depletion, amortization,
> and certain other non-cash charges such as Company N's items (1) and (4) less **(c) the
> average annual amount of capitalized expenditures for plant and equipment, etc. that
> the business requires to fully maintain its long-term competitive position and its unit
> volume. (If the business requires additional working capital to maintain its competitive
> position and unit volume, the increment also should be included in (c).** However,
> businesses following the LIFO inventory method usually do not require additional working
> capital if unit volume does not change.)"

> "Our owner-earnings equation does not yield the deceptively precise figures provided by
> GAAP, since (c) must be a guess, and one sometimes very difficult to make. [...] We
> agree with Keynes's observation: **'I would rather be vaguely right than precisely
> wrong.'**"

TEXT NOTE: the source .txt splits the literal "(c)" across four lines throughout this
passage, an extraction artifact. Reassembled, not smoothed.

**Four operative constraints, in one sentence:**

| Clause | What it settles |
|---|---|
| "the increment also should be included in (c)" | The WC term is REQUIRED. Method A, which omitted it, is wrong. |
| "requires to maintain its competitive position and unit volume" | It is the STRUCTURAL requirement, not the raw annual balance-sheet swing. Method B, which used the raw swing, is wrong. |
| "the **average annual amount**" | A multi-year average, not a single year. This is the clause that validates Method C's construction. |
| "usually do not require additional working capital **if unit volume does not change**" | The WC term is tied to UNIT GROWTH. A business adding 4% more stores a year requires some; a flat one requires almost none. |

**RULING on the WC term. Method C is adopted.** Required WC increment = the average
annual cash effect of working-capital changes over the last four clean fiscal years,
with years distorted by an externally imposed shutdown excluded (consistent with Ruling
9). For TJX that is **$134M/yr**, and the resulting tiers replace Method A's in all
future runs. The prior omission is recorded, not edited out of history.

**RULING on the capex term, which the same sentence forces and which is the larger
error.** Buffett's (c) is what the business "**requires to fully maintain** its long-term
competitive position and its unit volume." That is MAINTENANCE capex. We have been
subtracting TOTAL capex. For any business opening new units, total capex includes growth
capex, and subtracting it understates owner earnings, sometimes badly. TJX is opening
stores at 3-4% a year and raising that to 4%: on FY2026, total capex was $1,957M against
D&A of $1,247M, so the gap is $710M, roughly 15% of reported OE.

Under Ruling 7 this is not acceptable conservatism, it is windage in the numerator.
**However, maintenance capex is genuinely not disclosed by most filers, and Buffett says
(c) "must be a guess."** So the ruling is a disclosure requirement, not a formula:

1. **Every run states its maintenance-capex assumption explicitly and gives the band.**
   The template already has the field ("disclosed split? Y/N, band used: ___") and it has
   been left blank. It becomes mandatory.
2. **Default band, absent disclosure: D&A as the floor and total capex as the ceiling**,
   with the run stating where in the band it sits and why. [E2-23] supports D&A as a
   FLOOR rather than an estimate, via the See's note in the same letter: "at See's we
   annually make capitalized expenditures that exceed depreciation by $500,000 to
   $1 million, **simply to hold our ground competitively**."
3. **Where the band changes the verdict, the verdict is WAIT** and the run says so. A
   business whose classification depends on an undisclosed capex split has not screamed
   at you [E3-25, Ruling 4-B].
4. **This is a FRAMEWORK CONVENTION** and is labelled as such. The corpus mandates
   maintenance capex; it supplies no method for estimating it from public filings.

**Effect on TJX, full band, at $137.75:**

| Maintenance capex assumption | OE FY2026 | Book One yield | Book Two FAIR |
|---|---|---|---|
| 100% of total capex (what we used) | $4,650M | 3.02% | $69.47 |
| 85% of total capex | $4,944M | 3.21% | $74.57 |
| D&A x 1.10 (the See's rule) | $5,235M | 3.40% | $81.95 |
| D&A (floor, most generous reading) | $5,360M | 3.48% | $83.91 |

**The band does not change the verdict.** Book One fails against 5.19% across the whole
band; Book Two's FAIR line tops out at $83.91 against a $137.75 price. TJX remains WAIT
at every setting. Recorded as the test case for the ruling.

---
## WHAT THE FOUR ANSWERS ADD UP TO

The framework was built to be conservative and it succeeded at each individual point.
What the corpus says, in a sentence Buffett gave in direct answer to this exact question
[E4-11], is that conservatism compounds and must therefore be spent once, deliberately,
at the end, rather than sprinkled at every variable where it feels prudent.

Three of the four questions were symptoms of the same error. The MOS debate, the
trough-year anchor and the omitted-then-mis-specified owner-earnings terms are all the
same defect wearing different clothes: **conservatism applied at a variable that had
already been made conservative somewhere else.**

Ruling 4-C warned that a convention stricter than the corpus is as much a defect as one
softer than it, and required checking both directions on every constant. That check had
been applied to the hurdle floor and the size premiums. It had never been applied to the
margin of safety, the anchoring rule, or the owner-earnings formula. Applied now, all
three fail it in the strict direction.

**And the framework survives the test.** Every correction here makes the system more
willing to buy, and TJX at $137.75 still fails both books at every generous setting.
That is the outcome you want when loosening a constant: the loosening was warranted by
the text, and the thing it was wrongly rejecting is still rejected on the merits.


---
## RULING 11: XBRL IS A TRANSCRIPTION TOOL, NOT A SOURCE OF VERDICTS.
## The filing gets READ before any name reaches Gate 6.
## ✅ RATIFIED 2026-08-26. Raised by the operator asking
## the one-line question: "does the corpus use XBRL?"

**Literal answer: no.** XBRL appears nowhere in the corpus. It did not exist for most
of it (SEC phase-in from 2009). There is no reference anywhere on the citation shelf to
a database, data feed, screener or terminal as a research tool. The only two hits run
the other way:
- 2003 meeting [E4-14]: "you want to read lots of annual reports. You really want to have
  a **database in your mind** so that you can tell what kind of a business you are looking
  at, in general, by looking at the figures. It is far overrated -- **we never look at
  any analyst reports.**"
- Poor Charlie's Almanack: "Charlie is **no slave to a database**: He takes into account
  all relevant aspects, both internal and external to the company and its industry,
  **even if they are difficult to identify, measure, or reduce to numbers.**"

**The governing passage [E3-27], 1994 annual meeting**, answering a question about how
he gets from annual reports to intrinsic value:

> "**The numbers in any accounting report mean nothing, per se, as to economic value.
> They are guidelines to tell you something about how to get at economic value. But they
> do not tell you anything. There are no answers in the financial statements. There are
> guidelines to enable you to figure out the answer. And to figure out that answer, you
> have to understand something about business.** You do not have to understand a lot
> about mathematics. I mean, the math is not complicated. But you do have to understand
> something about the business."

**What he reads FOR [E3-28], 1996 annual meeting**, asked directly:

> "I like to know as much as I can about **the person that is running it and how they
> think about the business and what is really going on in the business.** [...] If we own
> stock in a company and in an industry, and there are eight other companies that are in
> the same industry, **I want to own or be on the mailing list for the reports for the
> other eight, because I cannot understand how my company is doing unless I understand
> what the other eight are doing.** I want to have the perspective of, in terms of market
> share, what is going on in the business or their margins or the trend of margins, all
> kinds of things that I cannot get unless I know -- **I cannot be an intelligent owner of
> a business unless I know what all the other businesses in that industry are doing.**"

**Not one item on that list is in XBRL.**

### THE DEFECT THIS DIAGNOSES
The 2026-08-26 TBTC error was blamed on the owner-earnings formula. That was the
proximate cause. **This is the root cause.** A verdict was computed on a business whose
10-K had not been opened. What corrected it was not better arithmetic on the tags; it
was reading the filing and finding, in the MD&A, that the swing was customer-deposit
timing on lumpy casino installs. Six lines of English overturned a conclusion that six
tagged numbers had produced.

The same defect is latent in the maintenance-capex band. Buffett says (c) **"must be a
guess -- and one sometimes very difficult to make"** [E2-23], a judgment formed by
understanding what the business needs to hold its ground. Ruling 10 turned it into
arithmetic on two tags (D&A and total capex). That is a reasonable DEFAULT when nothing
better is known, but it is not the thing the corpus asks for, and it must not be
presented as though it were.

### RULING
1. **XBRL is a TRANSCRIPTION and SCREENING tool.** It is the filer's own tagged
   submission of the same statements the corpus reads, so it is a legitimate primary
   source for a stated line item and is faster and less error-prone than manual
   transcription. It stays.
2. **No name may reach Gate 6 on XBRL alone.** Before valuation, the run must record
   that the actual filing was READ: the MD&A, the cash flow statement including its
   detail lines, and the footnotes. The run states the date and accession number of what
   was read.
3. **Any single-line figure that drives a verdict is checked against the filed
   statement**, and the check is recorded. (Done for TBTC: the 10-K states operating cash
   flow of $1,806,481 for 2025; XBRL returned the same figure.)
4. **Maintenance capex and the required WC increment are labelled JUDGMENTS, not
   outputs.** The D&A-to-total-capex band is the default when the filing does not support
   a better estimate, and the run says which it is using and why. A run may narrow the
   band only by citing something it read in the filing.
5. **Mechanical screens keep their place.** Screening a thousand names on tags to find
   twenty worth reading is exactly what the tags are good for, and it commits nobody to
   anything. The rule bites only where a VERDICT is issued.

### AND A GAP IN GATE 2 THIS EXPOSES
[E3-28] states a condition the framework has never required: Buffett says he **cannot**
evaluate a business without reading the reports of its competitors. Gate 2 asks for a
moat metric and an 8-quarter trend for the company alone. Every moat verdict in this
project so far has been issued without the comparative reading the corpus treats as
mandatory.

**PROPOSED addition to Gate 2:** a COMPETITOR ROW. Name the closest competitors, and for
each give the same primary moat metric over the same window, filing-sourced. A moat is a
claim about relative position and cannot be evidenced from one company's numbers alone.
Where competitor data is unavailable (private, foreign, unsegmented), say so, and treat
the moat class as PROVISIONAL rather than verified.

This is the most demanding of all the 2026-08-26 rulings and it will slow every run down.
It is also the one with the most direct textual support.


---
## RULING 12: THE THREE BOXES. Every gate returns IN, OUT or TOO HARD.
## ✅ RATIFIED 2026-08-26. This is the framework's primary simplification and it
## SUPERSEDES the "eight gates to six" proposal as the headline change.

Raised by reading `Annual Meetings/2006 Annual Meeting.txt:215` in full, at the
operator's instruction, after the 2026-08-26 audit.

**ATTRIBUTION, corrected under Prime Rule 1:** the line is **MUNGER'S**, quoted by
Buffett. The text reads "**Charlie says**, you know, 'We've got three boxes at the
company: in, out, and too hard.'" It was given as Buffett's in chat; corrected here.

> "There's just games that are too tough. Charlie says, you know, **'We've got three
> boxes at the company: in, out, and too hard.'** And **a lot of things end up in the
> 'too hard' pile, and it doesn't bother us.** [...] What I've learned is I know enough
> not — **to know that I don't know enough** to make an investment decision."

Munger again the same day (`:821`): "**If something is too hard to do, we look for
something that isn't too hard to do. What could be more obvious than that?**"

And 2005 (`Annual Meetings/2005 Annual Meeting.txt:977`): "there's **no degree of
difficulty factor**... we get paid, **not for jumping over 7-foot bars, but for stepping
over 1-foot bars**... **I'd rather have the universe be a little smaller than it really
is, than being interpreted as larger than it is.**"

### THE FINDING
The audit had proposed cutting eight gates to six. **Reading the passage in full shows
that was the wrong read.** The corpus does not complain about the NUMBER of tests. It
insists on a **THIRD OUTCOME**. Their filter has three boxes; ours had two, because every
gate returned PASS or FAIL.

**FAIL and TOO HARD are different findings.** FAIL says the business is bad. TOO HARD
says the business may well be excellent and I cannot tell. Collapsing the second into the
first produces false confidence in both directions: names get rejected that were merely
unexamined, and — the live failure mode — names get PASSED on thin evidence because the
only alternative on offer was a verdict the analyst did not believe.

### RULING
1. **Every gate returns IN, OUT or TOO HARD.**
   - **IN**: evidence present, clears the bar. Proceed.
   - **OUT**: evidence present, business fails. STOP. Permanent. Eliminated register.
   - **TOO HARD**: cannot tell. CLOSE the file **without prejudice**. No finding about the
     business. Re-openable if better evidence appears, and the run must record **what
     evidence would re-open it**.
2. **TOO HARD IS THE DEFAULT WHEN EVIDENCE IS THIN.** A gate marked IN carrying
   "unverified", "general knowledge", "not independently confirmed" or "provisional" is a
   TOO HARD verdict wearing an IN label. **This is now a protocol violation.**
3. **THE 7-FOOT BAR RULE.** A conclusion that required fighting for it is worth less, not
   more. If a verdict only holds after narrowing assumptions or adjudicating a
   sensitivity grid, the verdict is **TOO HARD**.
4. **TOO HARD is never reported as a pass**, never carried into a portfolio, and never
   used to authorize an order.

### THE LIVE FAILURE THIS FIXES
The July 2026 Japan runs (NCLTY, MITSY, NHNKY) each opened "No corpus/SEC sources --
general-knowledge", used **NI as an owner-earnings proxy**, and recorded **PASS** at
every gate. Two were marked BUY-ELIGIBLE and bought. **Those were TOO HARD verdicts
wearing a PASS label.** Under Ruling 12 all three close at Gate 4 (Step 0-B, filing not
read) and never reach a valuation, let alone an order.

### WHAT THIS DOES *NOT* CHANGE
The Gate 8 deletion stands on its own separate evidence (the asymmetry ratio was computed
in 10 of 121 run files; Ruling 6 already absorbed its useful output). Gate 7 merges into
Gate 6. **8 gates become 6 — but that is now the secondary change, not the headline.**
A framework with a real TOO HARD box is simpler in USE than a shorter one that forces
every name to a verdict.


---
## RULING 13: TOO HARD SPLITS IN TWO. One is a WORK ORDER. The other is the real pile.
## ✅ RATIFIED 2026-08-26. Amends Ruling 12 the same day it was written.

Raised by the operator: *"my goal is to use the technology at hand to get rid of the
TOO HARD verdict and find the info needed to make an analysis."*

**The operator is right, and Ruling 12 as drafted was sloppy.** It used one verdict for
two situations that have nothing in common.

### THE TWO THINGS I HAD CONFLATED

**A. The evidence exists and we did not go get it.** The Japan runs are this. Nitori's
consolidated financial statements are published **in English, on the company's own IR
site, going back to 2014**. Nobody had opened them. That is not a hard problem; it is an
unperformed task, and calling it TOO HARD dignifies laziness as judgment.

**B. The work was done and the future remains indeterminate.** This is Buffett's actual
too-hard pile:
> "you just get into businesses that — where **the future is so likely to be different
> than the present** that maybe there's a few people that have great insights on it, but
> **we sure don't**." — 2006 meeting (`Annual Meetings/2006 Annual Meeting.txt:215`)

No quantity of data fixes B. Any amount of work fixes A.

### THE CORPUS IS ON THE OPERATOR'S SIDE
The perimeter of the circle is a fact about **you**, and it moves when you do work:
> "**The biggest thing is not how big your circle of competence is, but knowing where the
> perimeter is.**" — 2010 meeting (`Annual Meetings/2010 Annual Meeting.txt:1037`)

And Buffett's own answer to "how do I understand this company" is **go read more**, to
the point of putting himself on eight competitors' mailing lists:
> "**I want to own or be on the mailing list for the reports for the other eight**,
> because I can't understand how my company is doing unless I understand what the other
> eight are doing." — 1996 meeting [E3-28]

**Getting more evidence is the corpus's own prescription. TOO HARD was never meant to
excuse not looking.**

### RULING
**TOO HARD is replaced by two verdicts.**

**1. `UNRESEARCHED` — a work order, never a resting state.**
- Recorded only with a **named artifact** and **where it lives**: the specific document,
  filing, or dataset that would resolve the gate.
- **It is not a verdict, it is a queue entry.** A name may sit UNRESEARCHED only as long
  as the work order is outstanding.
- It closes when the artifact is obtained, **or** when the artifact is shown to be
  genuinely unobtainable — at which point it converts to UNKNOWABLE with that finding
  written down.
- **A run may never report UNRESEARCHED without the work order attached.**

**2. `UNKNOWABLE` — Buffett's pile, and it stays.**
- Recorded only **after** the evidence has been gathered.
- Requires a one-line statement of *what specifically cannot be known*, in the 2006 form:
  the future of this business is too likely to differ from its present for us to judge.
- **The separating test, applied out loud on every TOO HARD call:**
  **"Can I name the document that would resolve this?"** Yes → UNRESEARCHED.
  No → UNKNOWABLE.

**3. The 7-foot bar rule survives, unchanged, and attaches to UNKNOWABLE only.** A
verdict that only holds after narrowing assumptions is still UNKNOWABLE. Gathering more
evidence is legitimate; torturing the evidence you have is not.

### THE EVIDENCE ESCALATION LADDER (run in order; stop when the gate resolves)
1. **SEC XBRL company facts** — transcription and screening only (Ruling 11).
2. **SEC EDGAR primary documents** — 10-K/10-Q/8-K text: MD&A, cash-flow detail,
   footnotes. Required by Step 0-B before Gate 6.
3. **Company IR site, English** — the step that was never taken for Japan.
   **PROVEN 2026-08-26:** Nitori publishes English consolidated statements at
   `nitorihd.co.jp/en/ir/library/financial_statements.html`, FY2014 through FY2026.
4. **Exchange/regulator filings** — TDnet and TSE (Japan), RNS (UK), SEDAR+ (Canada).
5. **EDINET API** (Japan, 有価証券報告書) — **BLOCKED: requires a subscription key**
   (returns 401 "invalid subscription key"). Recorded as a known gap. Route 3 covers
   most of what it would provide for large caps.
6. **Competitor filings**, for Gate 2's competitor row — the 1996 "other eight."

**Where a rung is blocked, say which rung and why.** "Could not obtain" is a finding and
must name the obstacle, not gesture at difficulty.

### WHAT TECHNOLOGY CANNOT DO, STATED SO IT IS NOT PROMISED
It can deliver every filed number and every word of management's own commentary. It
cannot tell you whether the business will still be advantaged in ten years. **Gate 1 and
the pre-model verdict remain judgment and always will.** The risk this ruling creates is
the mirror of the one it fixes: a diligent data-gathering exercise talking itself into a
verdict on a business whose future is genuinely unreadable. **UNKNOWABLE exists to stop
exactly that, and it may not be dissolved by more spreadsheets.**

### IMMEDIATE EFFECT ON THE OPEN FILES
| Name | Was | Now | Work order |
|---|---|---|---|
| NCLTY | TOO HARD | **UNRESEARCHED** | English consolidated statements FY2024-FY2026 (`nitorihd.co.jp/en/ir/library/`) — **FY2026 already retrieved 2026-08-26**; need SBC, share count, JPY 30-yr, competitor row |
| MITSY | TOO HARD | **UNRESEARCHED** | Mitsui English IR annual securities report + cash-flow statement; same four items |
| NHNKY | TOO HARD | **UNRESEARCHED** | Nihon Kohden English IR; same four items. GTC stays cancelled until it closes |
| ASML | no run file | **UNRESEARCHED** | ASML files a 20-F with the SEC — rung 2, already available |

**None of these four are UNKNOWABLE. All four are queue entries, and the queue is the
point.**


---
## RULING 14: ONE BOOK. Owner earnings is the number, and the DCF stops voting.
## ✅ RATIFIED 2026-08-26. Retires the dual-book regime.

Operator: *"Owner Earnings is a priority with every business. Do we really need the two
book process? Remember Munger and Buffett always tried to keep this simple as possible,
so we can't overcomplicate it with technology — just use technology as a means of
efficiency."*

**All three points hold, and the corpus is more one-sided here than I expected.**

### WHAT BUFFETT ACTUALLY REPORTS WHEN HE VALUES SOMETHING
Not a DCF. A **multiple of owner earnings**, set against the **risk-free rate**:
> "we purchased our 10% interest in Wells Fargo for $290 million, **less than five times
> after-tax earnings**, and less than three times pre-tax earnings." — 1990 letter
> (`Shareholder Letters/1990 Letter.txt:326`)

Coca-Cola 1988: ~15× earnings. See's 1972: $25M against ~$2M of earnings. **Every worked
example in the corpus is a yield or a multiple. There is not one DCF in it.**

> "Warren talks about these discounted cash flows. **I've never seen him do one.**"
> — Munger, 1996

> "**the math is not complicated.** But you do have to understand something about the
> business." — 1994 meeting [E3-27]

And the Aesop framing is **one equation with three inputs**, not two competing books
[E4-01]: how certain are the birds, when and how many, and what is the risk-free rate.

### THE OBJECTION, AND WHY IT DISSOLVES
The honest case for Book Two was that a bare yield is blind to growth. Buffett addresses
that directly (`Annual Meetings/1994 Annual Meeting.txt:1255`):
> "would you rather have something that paid you 10 percent a year and never changed, or
> would you rather have something that paid you 2 percent a year and increased at 10
> percent a year? **Well, you can work out the math to answer those questions.**"

He does not answer with a second appraisal. He says **work out the math** — one
calculation that converts growth into a rate you can compare to the bond. **That is an
IRR, and we already compute it as a Gate 6 diagnostic.** We were producing the answer and
then burying it under a second verdict that voted against the first.

### RULING — ONE BOOK, THREE NUMBERS

**Owner earnings is THE number for every business, and the whole of Gate 6 is what you
are paid for owning them.**

    1. THE YIELD          owner earnings / market cap, against the sovereign
    2. WHAT THE PRICE      implied year-1 OE growth needed to justify the quote
       ALREADY ASSUMES     (versus what the business has actually done)
    3. WHAT YOU GET        IRR at the current price, stated as
                           **POINTS OF EQUITY PREMIUM OVER THE SOVEREIGN**

**The discounted cash flow is not deleted. It is demoted from a voter to an engine.** It
computes numbers 2 and 3 and issues no verdict of its own. There is no "Book Two verdict,"
no dual-book regime, and **no WHISPER** — the whisper existed only to arbitrate between
two books, and with one book there is nothing to arbitrate.

**The single decision number is #3: points of equity premium.** It reconciles yield and
growth into one figure, in the units the corpus uses (a rate, compared to the long bond).
A wide sensitivity range around it is a **pass**, per [E4-01] and the 7-foot bar rule.

**The margin of safety is applied ONCE, at the end** (Ruling 7), to convert the fair price
into a buy price.

### WHAT THIS DELETES
- The Book One / Book Two split and the "dual-book regime"
- The **WHISPER** verdict and the Scream Test's arbitration role
- The separate "STATUTE-ONLY" verdict — the starter/full distinction now falls out of
  where the price sits against FAIR and CHEAP, which is simpler and already stated
- One of the two places conservatism could hide (Ruling 7's concern)

### WHAT IT KEEPS
- The sovereign hurdle and size premiums
- The Aesop certainty spread (Ruling 4-A) — it sets the rate the IRR is compared against
- The full owner-earnings formula (Ruling 10), which becomes **more** central, not less
- The MOS severity ladder (Ruling 5-A)

### THE IMMEDIATE PAYOFF — the whole portfolio on one number
Ranked by what you are actually paid to carry equity risk, 2026-08-26:

| Name | OE yield | sovereign | **equity premium** |
|---|---|---|---|
| **HRB** | 10.50% | 5.19% | **+7.07 pts** |
| **TJX** | 3.06% | 5.19% | +0.8 to +1.5 pts |
| **NCLTY** | 4.60% | 4.04% | **+0.56 pts** |
| **V** | 2.84% | 5.19% | +0.56 pts |
| **TBTC** | 4.29% | 7.19% (micro) | **−0.48 pts** |
| **ASML** | 1.33–1.98% | 3.70% (EUR) | **negative** |

**One column, one glance, and H&R Block is not close to the others.** That was true under
the dual-book regime too, but it took two verdicts, a whisper rule and a sensitivity grid
to see it.

### ON TECHNOLOGY — the operator's third point, recorded as a standing constraint
**Technology is for EFFICIENCY, not for complication.** It exists to fetch the filing
faster, not to add a model. The test on any tooling: *does this get the same number
sooner, or does it add a number?* The second is forbidden. Ruling 11 already says tags
cannot produce a verdict; this extends it — **no tool may add a step to the framework, only
remove friction from an existing one.**
