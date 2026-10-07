## UPDATE 2026-09-21 — BLMN (Bloomin' Brands): Q1 IN, Q2 OUT on the business. Wave 7, name 17; register entry 149.

**Run file:** `Test Runs/2026-09-21 Run - BLMN Bloomin Brands.md`.
**Research:** `Test Runs/_research 2026-09-21 BLMN/` (competitor row, 10-K/10-Q text, companyfacts,
seven peers' 10-Ks).
**Step 0.** Sovereign **USD 30-year 5.34% at 09/18/2026**, struck fresh 2026-09-21 from the **US
Treasury daily par yield curve** (issuing authority; FRED not touched). Price **$8.07**, close of
2026-09-18, Yahoo, flagged aggregator. Shares **85,620,917** hand-read from the cover of the 10-Q
for the period ended 2026-06-28, accession **`0001546417-26-000032`**. **Cap $690.9M.** Anchor
filing **10-K FY2025, `0001546417-26-000009`**; cross-check by hand on FY2025 operating cash flow,
$276,694 thousand, split $275,946 continuing / $748 discontinued in the filed statement.

## What the run found
1. **The gate closed on the company's own Item 1, not on an outside judgment.** **[E3-03]**
   criterion 2 asks whether customers think the product has **no close substitute**. Bloomin'
   Brands answers in its own Business section: *"At an aggregate level, all major casual dining
   restaurants in markets in which we operate would be considered competitors of our concepts. We
   also face growing competition from the supermarket industry which offers expanded selections of
   prepared meals. Further, improving product offerings and convenience options from quick-service
   and fast-casual restaurants, and the expansion of home delivery services … could cause consumers
   to choose less expensive alternatives than our restaurants."* Item 1A calls the segment
   *"hyper-competitive"*.
2. **The physical series says the same thing in numbers [E4-55].** Combined U.S. comparable traffic
   **(5.3)% / (3.1)% / (4.4)% / (1.4)%** across FY2022-FY2025 and **(1.8)%** in H1 FY2026: five
   consecutive negative periods, **(13.5)% compounded**, while average check rose **+19.9%**. Outback
   alone: traffic **(15.1)%**, check **+19.3%**. **[E3-43]** says the three franchise conditions are
   demonstrated by pricing aggressively **and thereby** earning high returns on capital; BLMN did
   the first and got **0.94%** of revenue in operating income and **5.8%** on net tangible operating
   assets. Aggressive pricing plus low returns is the filed signature of the condition being absent.
3. **The competitor row put a number on the relative claim.** Eight filers, each from its own newest
   10-K, all struck 2026-09-21. GAAP operating margin: DRI 12.0%, EAT 10.7%, TXRH 8.1%, CAKE 5.0%,
   BJRI 3.3%, CBRL 1.6%, **BLMN 0.94%**, RRGB 0.23%. Return on net tangible operating assets, one
   construction applied identically to all eight: **BLMN last of eight at 5.8%**, against EAT 101%,
   DRI 34.9%, TXRH 34.7%, CAKE 32.8%. Latest-year traffic: EAT/Chili's **+3.6%**, TXRH **+2.8%**,
   BJRI **+2.8%** — in the same period BLMN lost guests. Two peers excluded with named reasons
   (DIN almost wholly franchised; DENN's newest 10-K is FY2024).

## The bull case, built at full strength before it was tested
Written into the run file first, per **[E4-26]** and operator rule 9, because the liked hypothesis
here was the **cheap** one and it needed the hardest hunting. At its best: Outback AUV **$4,008**
thousand and Fleming's **$6,071** (from $4,422 in FY2019); Carrabba's **+2.8%** and Fleming's
**+2.5%** comps in FY2025; H1 FY2026 comps **+1.6%** with Bonefish at **+7.0%** and **+3.7% traffic**;
an International Franchise segment earning **$30,412 thousand of operating income on $31,297 thousand
of revenue** — 82% of the company's operating income on 0.8% of its revenue, from 355 restaurants it
does not own; **$227.4M** of Brazil proceeds applied to the revolver across 2025; **nothing due
before 2029**; and a November 2025 turnaround funded by suspending the dividend.
**It did not survive the test, and the reason is structural, not tonal.** Every item on that list is
an operating improvement, a balance-sheet event, or a royalty derived from the same brand. None of
them makes a customer think there is no close substitute. **[E4-23]** and **[E2-36]** then bind: the
company's stated route to acceptable results **is** the turnaround — four platforms and a remodel of
nearly the whole Outback estate by 2028 — which is the *"corporate Pygmalion"* side of [E2-36], and
the framework says record that at **Q2 as a moat defect**, not at Q3 as a strength. Done.

## Priors refuted, in both directions
- **REFUTED, in the company's favour: the DRI missing-capitalised-software defect does not apply.**
  BLMN's consolidated statement of cash flows carries **one** investing line for fixed assets,
  *"Capital expenditures"*, in each of FY2023-FY2025. There is no separate software line to miss.
- **REFUTED, in the company's favour: the working-capital worry does not apply.** BLMN's seven
  change-in-assets-and-liabilities lines sit inside operating cash flow; FY2025 they net to
  **+$5,476 thousand**, 2% of OCF. `working_capital_flag` returned None and the filed lines confirm
  it. The framework's OCF-based CONVENTION already captures **[E2-23]**'s increment here.
- **REFUTED, against the screen: the row does not reproduce, on any field that matters.** Published
  `74 / 159`, spread `1.141`, cap `903`. Rebuilt on `floor_screen.owner_earnings()` against
  companyfacts pulled 2026-09-21: **60.0 / 124.8 / 108.4 / 150.3** ($M), spread **1.505**, cap
  **690.9**. The cap error is a stale price (about $10.55 against $8.07) and it propagates into
  `yield_bottom`, `vs_sovereign` and `growth_required` — in the direction that makes a falling stock
  look **less** cheap, i.e. the direction that gets a name skipped.
- **CONFIRMED and understated: `level_note_oe` "STEP DOWN".** The series steps **twice**. COVID in
  2020, and the **Brazil Sale Transaction of 2024-12-30**, after which Brazil is discontinued
  operations for all periods: FY2023 capex restated $324,255 to $282,229, FY2022 $219,691 to
  $192,791, and operating cash of discontinued operations was **$78,255 / $12,132 / $748** thousand
  in FY2023 / FY2024 / FY2025.
- **UPHELD, but NOT for the reason it gives: `spread_caveat`'s [E4-25] rebuild order.** Rebuilding
  the same mixed-perimeter series over **ten** windows (3y to 16y, both capex ends) gives
  **99.6 to 193.5** — a spread of **94%, NARROWER than the published 114%**. So window length was
  not what was hiding the width. Fixing the **perimeter** is: on continuing operations only, the
  four-year series runs **$38M to $145M — 281%**, and counting the lease note's **$57.2M / $91.3M /
  $74.5M** of new operating-lease right-of-use assets as committed capital takes the three-year
  mean to **zero**. This is the TAIL-TRIAGE CORRECTION working exactly as intended: the imperative
  was right in its order and wrong in its diagnosis, and only a rebuild could tell them apart.

## Tooling defects found — reported, not patched
1. **`tools/run.py` has no `ocf_continuing()`, and mixes accounting perimeters in the flattering
   direction.** `Screens/floor_screen.py` has carried one since the AMD run of 2026-09-07, which
   removes separately-tagged discontinued-operations cash from operating cash flow. **`run.py` never
   got the fix.** Its `OCF` list lets the *total* tag win, while its capex and D&A lists resolve to
   the *restated continuing-operations* figures from the newest 10-K. For BLMN FY2023 that pairs
   **$532.4M of operating cash including $78.3M Brazil earned** with **$282.2M of capex that excludes
   Brazil**, overstating that year's conservative end by **$78.3M, or 49%**. This is the fourth
   recorded instance of "a fix applied to one path and not its twin", and the first found in this
   direction — `floor_screen.py`'s own comments warn about it three times.
2. **`Screens/floor_screen.py` mixes the perimeter the other way, conservatively.**
   `ocf_continuing()` correctly returns continuing-operations OCF, but `da_annual()` and
   `capital_acquired()` take the **largest resolving value per year**, which for FY2022 and FY2023
   returns the **pre-restatement, Brazil-inclusive** capex ($330.7M vs $282.2M) and D&A ($191.2M vs
   $169.3M). The max rule is right for the MCD subcomponent case and wrong for a restatement. Its
   direction is conservative, so it does not flatter — but it is still not one company, and it is
   part of why the published row cannot be reproduced.
3. **Neither tool counts operating-lease right-of-use additions.** They are not capex and it is not
   obvious they should be counted, but for a filer that leases nearly every box they are **$57.2M**
   of capital committed in FY2025 against **$179.9M** of cash capex, and a run that does not open
   the lease note cannot even see the question. Recorded as a reader's checklist item in
   **[E3-68]**'s sense, not as a code change.

## No price band, and the reversal condition in words
`tools/alerts.json` and `PORTFOLIO.md` both carry **zero BLMN**, verified after the fold. A name that
failed on the business gets a reversal condition, not an alert (the QLYS ruling, 2026-09-07):
**four consecutive quarters of positive Combined U.S. comparable-restaurant traffic with average
check growth no greater than traffic growth — guests returning rather than prices rising — together
with a restaurant-level operating margin back above 13.3% and a GAAP operating margin out of the
competitor row's bottom two.** Price is not a reopening condition at any level **[E5-35]**.

## The uncomfortable part, written down rather than hedged
The arithmetic under **COMPUTATION — NOT A CLEARANCE** in the run file sits above **[E4-28]**'s ~10%
floor on most constructions and at zero on one. That is precisely the condition operator rule 9
names: a cheap price creates an incentive to clear a gate. The gate was not cleared, and the honest
statement of what was given up is that **if the traffic decline is cyclical rather than structural,
this file will look like a missed opportunity, and [E3-47] prices omission errors as the expensive
kind.** The answer is not that the risk is absent; it is that **[E5-42]** and **[E5-35]** put the
business question first and refuse to let the price answer it, and the business question was
answered by the filer itself.

## Acceptance test
`python tools/check_framework.py` **PASS** before the commit. `tools/ledger_verbatim.py` not run —
the ledger was not touched. **Every ledger id written into the run file was first resolved against
`principle_ledger.csv`; all resolve and PHANTOM is 0.** The **[E4-55]** OCR artifacts are reproduced
in the run file rather than smoothed, per PRIME RULE 1: the doubled opening quotation marks, the two
apostrophes closing *bounce back*, and the **U+FFFD replacement character** standing where the `ff`
ligature of *effect* was, written as the numeric entity `&#65533;` so the artifact survives the
file's own encoding.
