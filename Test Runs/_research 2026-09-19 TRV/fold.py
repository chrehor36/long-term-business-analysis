# -*- coding: utf-8 -*-
"""TRV fold, 2026-09-19. One read-modify-write per shared file, immediately before the commit.

Concurrent runs share this tree. The USAR run found the trap: `## COMPLETED FROM THE QUEUE`
also appears inside the FOLD instructions lower in the file, so a bare last-occurrence search
inserts the entry OUTSIDE the slice the count measures. This anchors on a LINE-START regex,
counts the entries in that slice before and after, and asserts the delta is exactly one.
"""
import io, os, re, sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

QUEUE = os.path.join(BASE, "Screens", "WATCHLIST RUN QUEUE.md")
READING = os.path.join(BASE, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
OVERNIGHT = os.path.join(BASE, "Screens", "_daily", "OVERNIGHT LOG.md")

ENTRY = u"""- **TRV (The Travelers Companies, Inc.), 2026-09-19 - FAIL at Q2, OUT ON THE BUSINESS** (Q3 and
  Q4 RECORDED, NOT GOVERNING; Q5 headed COMPUTATION - NOT A CLEARANCE). **WAVE 6** and the
  **MINI BERK insurance track**, run under `Framework/SECTOR METHOD - owner earnings for insurers
  and float-bearing holding companies.md` with both amendments applied. **CIK 0000086312 found by
  `tools/sources.py:cik_for('TRV')`**, not taken from the brief. **Price US$374.62**, close of
  **2026-09-18** (Yahoo via `tools/sources.py:price()`, an aggregator, used for the live quote only
  and flagged). **Shares 208,575,022** off the cover of the **Form 10-Q for Q2 2026, accession
  0000086312-26-000145, filed 2026-07-17, count as at 2026-07-10**; the cover says
  **"outstanding"**, not issued (the ERIC/IHG trap checked, not assumed), and it reconciles to the
  filed balance sheet's 208.6-share common caption against **treasury stock of 586.8 shares**; the
  post-cover movement is **repurchases, not issuance** (217.5 shares at 2025-12-31 to 208.6 at
  2026-06-30, 10.3 repurchased against 1.4 issued), so the RGTI/USAR trap runs the safe way and the
  cover count is the CONSERVATIVE one. **Cap US$78,136M**, 2.36x the 2026-06-30 book value per share
  of $158.78. **Sovereign 5.34%**, US Treasury 30-year par yield curve, 2026-09-18, issuing
  authority. **Q1 IN**: three segments as filed - Business Insurance $22,679M net written at a 91.7%
  combined ratio, Personal Insurance $17,446M at 89.5% (homeowners $9,051M now larger than
  automobile $7,745M, whose premium FELL 2% in 2025), Bond & Specialty $4,262M at 81.9% - and the
  twelve-year decomposition answers where the money comes from: **GAAP underwriting result $13,265M
  against net investment income $33,100M, so the PORTFOLIO produced 71.4%** of the pre-tax income of
  the two engines, and underwriting produced under a tenth of it in five of the twelve years.
  **2025's 89.9% combined ratio is the best underwriting year in the window, not the normal
  condition.** **Q2 OUT, on three independent grounds.** (i) **The decisive series, built the way
  the MKL run built it: the CURRENT-ACCIDENT-YEAR combined ratio with prior-year development beside
  it, ten years** - 95.2 / 100.2 / 98.8 / 96.3 / 96.2 / 96.3 / 97.5 / 97.4 / 94.2 / **92.3** for
  2016-2025, mean **96.44** (five-year 95.54), against catastrophe loads of 3.6 to **8.4** points and
  favourable development of +1.6 points a year. **TRV is NOT Markel** - Markel's was 99.3 / 101.1 /
  100.3, so its profit WAS the releases, while TRV's current-accident-year ratio is **below 100 in
  nine of ten years** and the underwriting profit is real. That is recorded in its favour. But
  **1.6 of the 5.2-point average reported margin is prior-year release, about 31% of it, every year
  for ten years.** Each computed underlying level was checked against the filer's own stated
  year-over-year change at **all nine year-pairs with no residual** - the cross-check operator rule 4
  requires, done on the series that decides the gate. (ii) **Two of the three [E3-03] criteria fail on
  the filer's own words.** Criterion 2: *"approximately 1,100 property and casualty groups in the
  United States, comprising approximately 2,600 property and casualty companies"*, an industry
  *"highly competitive in the areas of price"*, with self-insurance, captives and risk retention
  groups named as the alternatives. Criterion 3 is a flat fail: *"rates must be approved by the
  regulator before being used by the insurer … **Approximately one-half of the states require prior
  approval of most rate changes**"*, against a statutory standard that rates be *"not excessive"*,
  and the filer's own warning that insurers *"may be unable to change prices until some time after
  the costs associated with coverage have changed, primarily because of state insurance rate
  regulation."* That is **[E2-59]** exactly - regulation caps a franchise and floors a commodity
  business, and creates neither class. (iii) **The competitor row, EXTENDED from the MKL row through
  the CB run rather than rebuilt - thirteen names, and TRV is TENTH.** Eight rows carried unchanged
  (KNSL 80.60, ACGL 86.99, CB 89.50, WRB 89.84, RLI 93.08, AXS 94.10, MKL 100.27, FFH not
  comparable); **six new in this run, the standard-lines peers that row lacks**: HIG Business
  Insurance **92.28**, PGR **92.57**, CNA **94.89**, **TRV 95.54**, ALL **96.94**, CINF **97.28**,
  all on the same current-accident-year basis, same 2021-25 window, each cell read from the filer's
  own 10-K with its accession number, and the two comparability limits disclosed (CNA's cell is
  flattered because it excludes the Corporate & Other segment where asbestos and legacy mass-tort ran
  $50-134M adverse a year, while TRV's includes its asbestos charges in full; HIG is segment-level
  because it publishes no consolidated P&C ratio). **TRV is fourth of the six peers it actually
  competes with and 6.0 points behind Chubb.** And **[E2-58]'s single exception to the commodity
  verdict - a cost advantage both wide and sustainable - is held by somebody else, seven points
  wide**: 2025 underwriting expense ratios PGR **21.5%** and ALL **21.4%** against **TRV 28.5%**, in
  exactly the lines TRV's premium growth is concentrated in; TRV's decade of expense improvement
  (31.5% in 2016) closed the gap to HIG 31.2% and CINF 29.3% and never touched the low-cost personal
  writers, and it **stalled in 2023** and has since ticked back up 0.4 points. **The sharpest single
  fact is [E4-55]'s physical series, which TRV publishes itself:** domestic Personal Insurance active
  policies **6.2M (2015) to a 9.2M PEAK (2022) to 8.4M (2025)** - down **8.7% from the peak, 800,000
  policies** - while **net written premium per domestic policy rose 50.6%**, $1,327 (2021) to $1,999
  (2025). The quarterly furnished supplement shows the decline **accelerating monotonically through
  2025 before the Canadian disposal muddies 2026**: automobile -2.9%, -3.1%, -3.4%, **-4.0%** year on
  year, homeowners -4.1%, -4.6%, -5.5%, **-6.3%**. **A DISCLOSURE FINDING on the way, and it defeated
  one instruction in the brief: for Personal Insurance, TRV publishes NEITHER retention NOR renewal
  price change as a number** - not in the 10-K (five occurrences, all adjectives: *"retention rates
  remained strong"*, *"renewal premium changes … remained positive but were lower than in 2024"*) and
  not in the furnished EX-99.2 supplement, which carries no retention table for any segment. The
  quantified series lives only in the earnings-call slides, which are neither filed nor furnished.
  Where numbers ARE furnished, the commercial books read: Business Insurance renewal premium change
  **4.8%** at **86%** retention in 2Q2026, Bond & Specialty management liability retention **88%** -
  and the 10-K records renewal premium change *"lower than in 2024"* in Select Accounts, Middle
  Market and National Accounts alike as capacity returns. **Where the filer's adjective and the
  filer's own physical count disagree, [E4-55] says the count wins.** Class **NONE at the group
  level**, direction **NARROWING [E4-32]**, with one dissent inside it: **Bond & Specialty is
  plausibly a narrow moat** (surety at an 81.9% combined ratio, $160.0M PML retained per principal)
  and it is **9.6% of net written premium** - one narrow moat over a tenth of the book does not make
  the group a franchise, which is the MKL shape and the MKL answer. **THE STRONGEST FACT AGAINST THE
  VERDICT, stated as [E4-51] requires: TRV's COST OF FLOAT over 2016-2025 was NEGATIVE 1.73% a
  year** - it was paid a mean of $907M a year to hold a mean of **$52.4bn** of other people's money,
  against a **5.34%** sovereign, a funding advantage of roughly 7 points and about **$3.7bn a year**
  of value created by the float mechanism alone. **By [E3-69], the one measure the corpus itself
  nominates for this business class, Travelers is a good business.** It does not rescue Q2 because
  [E3-69] measures how cheaply the business is funded while [E3-03] asks whether the product is
  substitutable and price-regulated, and passing the first while failing the second is [E2-59]'s
  named class. **Q3 RECORDED, NOT GOVERNING - and it is a BINARY GATE here** ([E2-70] is about this
  industry by name; reserves are 2.03x equity, so a 5% under-reserve is 10.2% of it). **The reserve
  finding is what the consolidated series conceals:** net favourable development in nine of ten years
  is produced by **workers' compensation releasing 20-24% of eight consecutive accident years'
  initial estimates** (AY2016 2,768 to 2,092, -24.4%) **to pay for GENERAL LIABILITY strengthening of
  7% to 28% in eight consecutive accident years** (AY2018 1,253 to 1,604, +28.0%), plus commercial
  automobile strengthening, plus an asbestos charge **every single year** ($277M / $242M / $284M in
  the last three third quarters, on $1.36bn of net asbestos reserves). **[E2-56]'s Pro-Am effect
  applied to reserves rather than to capital allocation - and the fuel is running out**: the
  workers' compensation release is 24.4% on AY2016 and **0.1% on AY2023**, and 1.6 points a year of
  reported combined ratio goes with it. **[E2-67] candor: above the industry, below the benchmark.**
  TRV publishes the ten-year triangles by line (GAAP-mandated, so compliance rather than volunteered)
  and **does voluntarily name the direction of its own error on asbestos** - *"the property and
  casualty insurance industry, **including the Company**, has experienced net unfavorable prior year
  reserve development with regard to asbestos reserves"* - and even discloses strengthening *"beyond
  the range of reasonable estimates"* in 2023; but it **never aggregates the triangles into the
  sentence they support**, so the reader must compute the systemic bias [E2-67] says the filer should
  name. **[E4-29] reads CLEAN and it was checked where the CGNX lesson says to check: zero
  occurrences of EBITDA in the 10-K, in the 8-K EX-99.1 earnings release, in the EX-99.2 supplement
  and in the proxy**, with "core income" reconciled on its own supplement page. **No numeric
  guidance is published at all**, so [E3-48] has nothing to test and [E5-30]'s ratchet was never
  started. **Shares 353.5M (2013) to 208.6M (2026), a 41.0% retirement**, so [E5-15] and [E2-52] run
  the other way. **[E4-30]: no smoothing** (net income fell 32% in 2017 and 23% in 2022, published
  as such) and **cash taxes show no downward drift** (current tax over pre-tax income 22.9% in 2016,
  16.4% in 2025, with the 2017-18 step being the Tax Cuts and Jobs Act and separately disclosed).
  **Two prompts fire and they do NOT converge [E4-52]:** the pay metric is **adjusted** core return
  on equity with catastrophes deliberately normalised out (*"not unduly rewarded, or disadvantaged,
  based on the level of catastrophe losses in a given year"*) **in a business whose catastrophe load
  went from 3.1 to 8.4 points of the combined ratio** - [E2-49], pre-set and long-lived, so a prompt
  and not metric-switching; and **$3,004M of 2025 buybacks plus $3,100M in the first half of 2026 at
  2.4-2.5x book with no published intrinsic-value estimate or price discipline of any kind**, which
  fails **[E4-31]'s third condition** outright against [E5-25]'s published 110%-of-book and $20bn
  floor, and whose pattern is the wrong way round on **[E5-24]** ($625M spent in 2020 near $140,
  $3,004M in 2025 near $290). **[E2-01] primary test: ten-year mean ROE 12.94%**, and the
  denominator is named both ways - AOCI was $(4,967)M at 2024-12-31 on a 94% fixed-maturity book
  held at market, so adding it back makes 2024 **15.8% rather than 18.9%** and 2023 **10.5% rather
  than 12.9%** (between a quarter and a third of the reported improvement is a denominator effect),
  while **[E2-43]**'s tangible denominator pushes 2025 to ~22% on $4,066M of goodwill. **[E3-54]
  passes decisively: $3.91 of market value per $1 retained over five years**, $3.39 over ten, $3.89
  over twelve, on 78.5% of twelve years' earnings returned. **Q4 RECORDED, NOT GOVERNING, and the
  sector method's substitutions are used, with the ordinary construction REFUSED and the refusal
  justified**: an owner-earnings yield off 2025's $10,606M of operating cash flow would count a
  $101bn portfolio twice, once as its coupons and again as component 1, which is the arithmetic
  error **[E5-48]** exists to prevent, so `arith.py` computes no such yield. **Stage 0(b): float
  $65,772M by CONVENTION 4, float / investments 65.0% - MORE float-funded than Berkshire's 41.8%,
  so step 2 is this run's centre of gravity, the opposite of White Mountains at 22.0%; and
  CONVENTION 5's ratio, investments / equity, is 3.08x against Markel 2.01x and Berkshire 0.45x,
  making TRV the MOST dependent on [E5-46]'s break-even condition of any name on this track.**
  **Component 1 $103,179M at market at 2026-06-30, and gross EQUALS net** - no noncontrolling
  interests, no finance-operation borrowings - with the deferred-tax item carried at filed value
  because **[E3-71] has no sign for a deferred tax ASSET** and TRV holds a $1,041M net asset, not a
  liability. **Component 2, pre-tax and ex-portfolio per [E5-47] and [E5-48]: ten-year mean $1,305M
  against 2025's $3,885M, a 33-fold range across the window** ($117M in 2017), which is [E5-49] word
  for word. Cross-checked exactly: underwriting $3,307M + fee $495M + other $508M - interest $425M =
  $3,885M. **The [E5-50] retained-earnings judgment is STATED as NEUTRAL** - no premium and no
  discount: the measured [E3-54] record earns the absence of a discount, and the absence of any
  published repurchase discipline forfeits the premium. **GOOD, not great [E4-20, E4-43, E5-40]**;
  all three **[E5-11]** strengths score with liquidity read as reserve adequacy and net worth per
  the method's substitution and **NOT** as the $10.6bn of operating cash flow, which [E2-61] says is
  the symptom of the walking dead; interest cover 19.3x on 2025 and 10.7x on the ten-year mean
  [E2-54]; debt-to-capital 22.0%. **The named death, against `Screens/SURVIVAL SHAPES - index.md`:
  shape #11 THE PASS-THROUGH is the mechanism with shape #7 THE LONG TAIL ON A SHORT CYCLE as its
  feature. No new shape proposed.** Quantified from **exposure, not experience [E4-40]**: 2017's own
  realised current-accident-year ratio of 100.2 applied to 2025's $43,914M of earned premium is a
  **$3,395M pre-tax swing**, plus one event inside the disclosed **$3.0bn corporate catastrophe
  retention**, is about **$6.4bn** against $7,796M of pre-tax income and $32,894M of equity - and
  with $4.0bn of continuing investment income **the company survives at roughly break-even.** What
  dies is the owner's return: in 2017, the last time this happened, TRV earned **$7.58** a diluted
  share against 2025's $27.43, a **2.0% earnings yield** on today's price - and the next soft market
  arrives with the reserve cushion spent and the catastrophe load doubled. **Likelihood: a real
  possibility**, because the pricing deceleration and the cushion's decline are both already in the
  filings and only the catastrophe timing is unknown. **Q5 is NOT OPEN and its arithmetic is headed
  COMPUTATION - NOT A CLEARANCE per operator rule 3.** Below the gate: **honest pre-tax expectancy
  5.28% on the ten-year mean and 6.44% on the five-year mean against the ~10% floor [E4-28]** - so
  **0.06 points BELOW the 5.34% long bond on the ten-year mean and 1.10 points over it on the
  five-year**, clearing 10% only on 2025, the best year of twelve. **This is the BRK shape the sector
  method's step 4 was corrected for on 2026-09-02 - above the bond, below the floor - at a much lower
  quality of business.** The **[E5-46]** gross-asset construction points the other way and is
  reported rather than suppressed: **$103.2bn of investments is 1.32x the entire $78.1bn market
  capitalisation**, so on Berkshire's own arithmetic the underwriting, fee and surety businesses come
  free. **It is not a screamer, and CONVENTION 5 is why**: at 3.08x equity essentially the whole gap
  between $103.2bn and $33.1bn of equity rests on the break-even condition [E5-46] itself calls
  *"volatile"*, and the two constructions differ only in the rate applied to component 2 - $94bn at
  the sovereign, $50bn at the floor, price $78.1bn, **inside the range, which by [E4-01] IS the
  conclusion**. To justify the quote at a 10% pre-tax expectancy the business must earn $7.8bn
  pre-tax permanently, **+55% on the five-year mean and +89% on the ten-year**, against [E4-35]'s
  base rate and [E4-44]'s bound; and [E2-63]'s ceiling is the portfolio's own 3.80% pre-tax yield,
  because 71% of the earnings are a bond coupon. **Windage count one.** **NOTHING ARMED: no
  `tools/alerts.json` band and no PORTFOLIO row**, per the QLYS ruling of 2026-09-07 - a name that
  failed at Q2 failed on the BUSINESS and a price alert on it would be a category error. The
  reversal conditions are recorded in words at Q6 instead: the current-accident-year ratio holding
  below 94 through three years of decelerating renewal price change; the domestic policy count
  turning up while premium per policy holds; or the expense ratio resuming its fall toward the 21%
  the personal-lines cost leaders run. Next catalyst the Q3 2026 earnings 8-K, expected mid-October
  2026, which carries the annual in-depth asbestos review. `python tools/check_framework.py` PASSES.
  Run file `Test Runs/2026-09-19 Run - TRV Travelers.md`; scripts, filings and the peer row in
  `Test Runs/_research 2026-09-19 TRV/`, with the row's cell-by-cell provenance in
  `peers/row_out.md`. **Register entry 125**, counted from this file's `## COMPLETED FROM THE QUEUE`
  heading line to the next top-level heading: 124 entries before this one, 125 after, asserted by
  `fold.py` rather than taken from any count quoted in a brief.
"""

NARRATIVE = u"""
### TRV (The Travelers Companies) - run 2026-09-19, FAIL at Q2, OUT on the business
**MINI BERK insurance track, WAVE 6.** Price US$374.62 (2026-09-18), 208,575,022 shares off the
10-Q cover of 2026-07-17 (0000086312-26-000145, count at 2026-07-10), cap US$78,136M, sovereign
5.34% (US Treasury 30-year, issuing authority). Run file
`Test Runs/2026-09-19 Run - TRV Travelers.md`.

**WHAT THE RUN FOUND.** Travelers is the purest insurer this track has met - no operating leg at
all - and it is a good business by the one measure the corpus nominates for the class: **its cost of
float over 2016-2025 was NEGATIVE 1.73% a year**, so it was paid about $907M a year to hold a mean
$52.4bn of other people's money while the long bond pays 5.34% to borrow. **[E3-69]**: *"a low cost
of funds signifies a good business."* It is nevertheless **not a franchise**, on three independent
grounds, and the file closes at Q2.

**REFUTED PRIORS.**
1. **The brief's MKL prior did not transfer, and that is the most useful thing here.** Markel's
   current-accident-year combined ratio was 99.3 / 101.1 / 100.3, so its reported underwriting
   profit *was* prior-year releases. **TRV's is below 100 in nine of ten years** - 95.2 / 100.2 /
   98.8 / 96.3 / 96.2 / 96.3 / 97.5 / 97.4 / 94.2 / 92.3, mean 96.44 - so its underwriting profit is
   real. **The same test that killed Markel clears Travelers, and Travelers still fails Q2 for
   different reasons.** A test that only ever fires one way is not a test.
2. **The brief asked what filed retention and renewal price change did together in personal lines.
   Neither is filed as a number.** The 10-K gives five adjectives and the furnished supplement
   carries no retention table for any segment; the quantified series lives only in earnings-call
   slides. **The substitute is better than what was asked for:** the policies-in-force series, which
   TRV publishes annually and quarterly, and which **[E4-55]** says is the honest series anyway -
   domestic personal policies 9.2M (2022 peak) to 8.4M (2025), **down 800,000 or 8.7%**, while net
   written premium per policy rose **50.6%** since 2021 and the quarterly decline accelerated
   monotonically through 2025.
3. **A prior TRV session had died in this tree at about 10:43 the same day**, uncommitted, having
   fetched seven 10-Ks, the proxy, the Q2 2026 supplement and a substantially complete CNA
   extraction. **All of it was usable and the CNA cell of this run's peer row rests on it.** The
   write-early protocol paid off *across* sessions, which the protocol does not currently claim.

**THE THREE GROUNDS FOR THE Q2 OUT.** (i) Two of three **[E3-03]** criteria fail on the filer's own
words - ~2,600 licensed US P&C companies in an industry it calls *"highly competitive in the areas
of price"*, with captives and self-insurance named as substitutes; and *"approximately one-half of
the states require prior approval of most rate changes"* against a standard that rates be *"not
excessive"*. **[E2-59]**: regulation caps a franchise and floors a commodity business, and creates
neither. (ii) **The competitor row, extended from MKL's through the CB run to thirteen names on the
current-accident-year basis, puts TRV TENTH** and fourth of the six standard-lines peers it actually
competes with, 6.0 points behind Chubb: KNSL 80.60, ACGL 86.99, CB 89.50, WRB 89.84, HIG-BI 92.28,
PGR 92.57, RLI 93.08, AXS 94.10, CNA 94.89, **TRV 95.54**, ALL 96.94, CINF 97.28, MKL 100.27.
(iii) **[E2-58]'s single exception - a cost advantage wide and sustainable - is held by Progressive
at a 21.5% expense ratio and Allstate at 21.4% against TRV's 28.5%**, seven points wide, in exactly
the lines TRV is growing.

**THE Q3 FINDING WORTH CARRYING TO OTHER INSURERS.** TRV reports net favourable prior-year
development in nine of ten years. **The mechanism, from the note 8 triangles: workers' compensation
released 20-24% of eight consecutive accident years to pay for general liability strengthening of
7-28% in eight consecutive accident years, plus commercial automobile, plus an asbestos charge every
year.** **[E2-56]**'s Pro-Am effect applied to reserves - and the fuel is measurably running out
(24.4% released on AY2016, 0.1% on AY2023), taking 1.6 points a year of reported combined ratio with
it. **The general test this suggests for any reserve-driven filer: the consolidated development
number is a NET of two opposite trends, and the line-level triangle is where the trend lives.**
Candor lands above the industry and below **[E2-67]**: TRV publishes the triangles (GAAP-mandated)
and voluntarily names the direction of its asbestos error, but never aggregates the triangles into
the sentence they support.

**TOOLING DEFECTS.** Two, both in the same family. `us-gaap:GeneralAndAdministrativeExpense` and
`us-gaap:ReinsuranceRecoverables` both stop at TRV's 2014, replaced by
`SellingGeneralAndAdministrativeExpense` and `ReinsuranceRecoverablesOnPaidAndUnpaidLosses`. **The
first draft of `arith.py` therefore printed a twelve-year table containing one row, 2014, and a mean
computed from it - without erroring.** `tools/sources.py:annual()` documents this exact defect
(added 2026-08-27 after Apple) and the fix is a tag UNION; the prompt is that a run-local script
repeats it, and that a single-row series is indistinguishable from a company with one year of filed
history, which is survival shape #3. Second: the recoverables break makes 2014 return $4,067M
against 2015's $8,910M, a concept break that would have put a spurious -4.06% into the first row of
the cost-of-float table; **no tool detects a level discontinuity at a tag boundary**, and one would
qualify under the tooling test because it removes friction from a check the run had to do by hand.

**SECTOR METHOD DEFECTS - three, none amended, all named per PRIME RULE 5.** (a) Step 1's
deferred-tax rule has **no sign**: **[E3-71]** values a deferred tax LIABILITY as an interest-free
loan, and TRV carries a $1,041M net deferred tax ASSET created by bond marks - the ordinary case for
any insurer holding bonds at market in a rising-rate world, not an exotic one. (b) **CONVENTION 5
guards the LOW side of the ratios and has no language for the high side**, and the high side is
where the method can flatter: at 3.08x investments to equity the **[E5-46]** gross-asset
construction produces **$103.2bn against a $78.1bn market capitalisation, 1.32x**, which a run that
did not stop to ask what funds the assets could report as a screamer. This run wrote that language
itself. (c) **The cost of float has no stated SIGN CONVENTION.** Every previous name had an
underwriting loss in some years; TRV has a gain in nine of ten, so the ratio is negative throughout,
and "cost of float 1.73%" versus "minus 1.73%" inverts the central economic fact about the company.
This run adopted **negative = paid to hold the money** and said so in the table header; the document
should carry it.

**THE NAMED DEATH: shape #11 THE PASS-THROUGH, with shape #7 THE LONG TAIL ON A SHORT CYCLE as its
feature. No new shape proposed.** Quantified from exposure not experience **[E4-40]**: 2017's own
realised 100.2 current-accident-year ratio on 2025's premium is a $3,395M swing, plus one event
inside the disclosed $3.0bn corporate catastrophe retention, is about $6.4bn against $7,796M of
pre-tax income - **the company survives at break-even and the owner's return falls to 2017's $7.58 a
share, a 2.0% yield on today's price**, with the next soft market arriving after the reserve cushion
is spent and with the catastrophe load doubled from 3.1 to 8.4 points. A real possibility.

**BELOW THE GATE, not a clearance:** honest pre-tax expectancy **5.28% (ten-year mean) to 6.44%
(five-year)** on a $78,136M cap against the ~10% floor **[E4-28]** - the BRK shape, above the bond
and below the floor, at a much lower quality of business. **Nothing armed.**
"""

OVERNIGHT_LINE = (u"- 2026-09-19 15:53 EDT | TRV | Q1 IN / **Q2 OUT** on the business (Q3 and Q4 "
                  u"RECORDED, NOT GOVERNING; Q5 headed COMPUTATION - NOT A CLEARANCE). WAVE 6 and "
                  u"the MINI BERK insurance track; CIK 0000086312 found by cik_for(). "
                  u"Price US$374.62 (2026-09-18), 208,575,022 shares off the 10-Q cover "
                  u"0000086312-26-000145, cap US$78,136M, sovereign 5.34%. Current-accident-year "
                  u"combined ratio 96.44% over ten years and below 100 in nine of them, so it is "
                  u"NOT the Markel shape - but two of three [E3-03] criteria fail on the filer's own "
                  u"words, it is tenth of thirteen peers on that ratio, [E2-58]'s cost-advantage "
                  u"exception is held seven points wide by Progressive and Allstate, and domestic "
                  u"personal policies are down 800,000 from the 2022 peak while price per policy is "
                  u"up 50.6%. Cost of float MINUS 1.73% over ten years is the strongest fact against "
                  u"the verdict and is recorded as one. Register 125. Nothing armed.\n")


def fold_queue():
    s = io.open(QUEUE, encoding="utf-8").read()
    # STEP 1 -- the register entry, anchored on a LINE-START regex (the USAR trap).
    ms = [m for m in re.finditer(r"(?m)^## COMPLETED FROM THE QUEUE[^\n]*\n", s)]
    if len(ms) != 1:
        sys.exit("register heading matched %d times at line start; expected 1" % len(ms))
    head_end = ms[0].end()
    nxt = [m.start() for m in re.finditer(r"(?m)^## ", s) if m.start() >= head_end]
    slice_end = nxt[0] if nxt else len(s)

    def count(txt):
        return len(re.findall(r"(?m)^- \*\*", txt))

    before = count(s[head_end:slice_end])
    if "TRV (The Travelers Companies" in s[head_end:slice_end]:
        sys.exit("TRV is already in the register slice; refusing to double-enter")
    s = s[:head_end] + ENTRY + s[head_end:]
    # recompute the slice on the NEW text
    ms = [m for m in re.finditer(r"(?m)^## COMPLETED FROM THE QUEUE[^\n]*\n", s)]
    head_end = ms[0].end()
    nxt = [m.start() for m in re.finditer(r"(?m)^## ", s) if m.start() >= head_end]
    slice_end = nxt[0] if nxt else len(s)
    after = count(s[head_end:slice_end])
    print("register entries in the measured slice: %d -> %d (delta %d)"
          % (before, after, after - before))
    if after - before != 1:
        sys.exit("FOLD ABORTED: the entry did not add exactly one entry to the measured slice")

    # STEP 2a -- strike TRV in the WAVE 6 table.
    old = ("| TRV | The Travelers Companies | insurer | **RUN on the Mini Berk track** |")
    if old not in s:
        sys.exit("WAVE 6 TRV row not found verbatim")
    new = ("| ~~TRV~~ | The Travelers Companies | insurer | **RUN 2026-09-19 - struck. FAIL at Q2, "
           "OUT on the business:** the current-accident-year combined ratio is below 100 in nine of "
           "ten years, so it is NOT the Markel shape, but about half the states must approve its "
           "rates before use, it is tenth of thirteen peers on that ratio and fourth of the six it "
           "actually competes with, [E2-58]'s cost-advantage exception is held seven points wide by "
           "Progressive and Allstate, and domestic personal policies are down 800,000 from the 2022 "
           "peak while price per policy is up 50.6%. Cost of float MINUS 1.73% over ten years is "
           "the strongest fact against the verdict. Price US$374.62, cap US$78,136M. Register entry "
           "125. See COMPLETED. |")
    s = s.replace(old, new, 1)

    # STEP 2b -- add TRV to the MINI BERK roster line as an insurer run on that track.
    anchor = (u"~~BN~~ *(run 2026-09-13 - FAIL at Q2, OUT on the business: a holding company, not "
              u"an asset manager, and no leg carrying the weight is a franchise; see COMPLETED)*")
    if anchor not in s:
        sys.exit("MINI BERK roster anchor not found verbatim")
    add = (anchor + u", ~~TRV~~ *(WAVE 6 insurer, run on this track 2026-09-19 under the SECTOR "
           u"METHOD with both amendments - FAIL at Q2, OUT on the business; float / investments "
           u"65.0% and investments / equity 3.08x, the most float-funded and the most dependent on "
           u"[E5-46]'s break-even condition of any name on the track; see COMPLETED)*")
    s = s.replace(anchor, add, 1)

    io.open(QUEUE, "w", encoding="utf-8").write(s)
    print("queue: register entry inserted, WAVE 6 row struck, MINI BERK roster updated")


def fold_reading():
    s = io.open(READING, encoding="utf-8").read()
    if "TRV (The Travelers Companies) - run 2026-09-19" in s:
        sys.exit("TRV narrative fold already present")
    if not s.endswith("\n"):
        s += "\n"
    io.open(READING, "w", encoding="utf-8").write(s + NARRATIVE)
    print("reading list: narrative fold appended (%d chars)" % len(NARRATIVE))


def fold_overnight():
    s = io.open(OVERNIGHT, encoding="utf-8").read()
    if "| TRV |" in s:
        sys.exit("overnight log already has the TRV line")
    if not s.endswith("\n"):
        s += "\n"
    io.open(OVERNIGHT, "w", encoding="utf-8").write(s + OVERNIGHT_LINE)
    print("overnight log: one line with a clock time appended")


if __name__ == "__main__":
    fold_queue()
    fold_reading()
    fold_overnight()
    print("FOLD DONE -- steps 1, 2, 3 and the overnight line. "
          "Step 4 is deliberately EMPTY (Q2 OUT: nothing armed, no PORTFOLIO row). "
          "Steps 5 and 6 are run by hand next.")
