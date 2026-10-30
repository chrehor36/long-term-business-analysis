## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
**NOT OPENED.** Q2 returned OUT. Operator rule 2: *"No Q5 output may be reported unless Q1-Q4 each
show IN"*, and the framework's own instruction is to **stop at the first verdict that is not IN**.
No weight case is declared, no flag is scored, and nothing here may be read as a finding about
Bloomin' Brands' managers in either direction. **VERDICT: not reached.**

*One procedural note, because the queue's standing rule for this gate exists and the run should
record that it was not skipped for convenience: the standing instruction is to pull the latest 8-K
EX-99.1 before scoring [E4-29] and [E4-22]'s third flag. That pull was **not made**, because the
gate was not opened. If this file is ever reopened — see the reversal condition below — the 8-K
exhibits to `0001546417-26-000030` (2026-08-05) and `0001546417-26-000023` (2026-05-06) are the
first documents to read, and the FY2025 10-K's own non-GAAP section (Adjusted restaurant-level
operating margin, Adjusted income from operations, Adjusted net income, Adjusted diluted EPS) is
the place [E4-29] would be tested.*

## Q4 — WILL IT SURVIVE?
**NOT OPENED.** Q2 returned OUT. **VERDICT: not reached.**

---
⛔ **Q5 does not open.** Q2 is OUT. UNRESEARCHED and UNKNOWABLE both close the file; OUT closes it
permanently.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**NOT OPENED, AND NO VALUATION IS REPORTED.** Operator rule 3 governs everything in the next
section. **VERDICT: not reached.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**NOT OPENED** — there is no position and none is contemplated. **VERDICT: not reached.**
The reversal condition, in words, is recorded in the fold section below in place of a price alert;
a price band on a name that failed on the business would be a category error (the QLYS ruling,
2026-09-07).

---

# COMPUTATION — NOT A CLEARANCE
**Operator rule 3.** *Any valuation math produced before Q1-Q4 close must be headed*
**"COMPUTATION — NOT A CLEARANCE"** *and may carry no entry language.* Q1-Q4 did **not** close; Q2
is OUT. Nothing below is a valuation, a ranking, a yield to act on, or a statement that this
security is cheap. It exists for one reason: the run was dispatched to **reproduce the screen row's
arithmetic and say whether it reproduces**, and that obligation to the screen survives the verdict
on the business.

## 1. THE SCREEN ROW, FIELD BY FIELD — IT DOES NOT REPRODUCE
The row as dispatched:
`BLMN,"Bloomin' Brands, Inc.",903,74,159,1.141,$74M to $159M,…,0.0821,0.0286,0.0179,…`

| field | screen | rebuilt 2026-09-21 | reproduces? |
|---|---|---|---|
| `cap_m` | 903 | **690.9** ($8.07 × 85,620,917 cover shares) | **NO — 30.7% high** |
| `oe_bottom_m` | 74 | **60.0** (`3y_capex`) | **NO — 19% high** |
| `oe_top_m` | 159 | **150.3** (`5y_da`) | **NO — 5.5% high** |
| `spread` | 1.141 | **1.505** | **NO** |
| `yield_bottom` | 0.0821 | **0.0868** (60.0 ÷ 690.9) | no, and the two errors partly cancel |
| `vs_sovereign` | 0.0286 | 0.0868 − 0.0534 = **0.0334** | no |
| `growth_required` | 0.0179 | 0.10 − 0.0868 = **0.0132** | no |
| `years_filed` | 16 | **16** (FY2010 … FY2025) | yes |
| `newest_filing` | 2025-12-28 | 2025-12-28 | yes |
| `newest_periodic` | 2026-06-28 | 2026-06-28 | yes |

The rebuild ran `Screens/floor_screen.py`'s own `owner_earnings()` against companyfacts pulled fresh
on 2026-09-21, and returned exactly four constructions:
**`3y_capex` 60.0 · `3y_da` 124.8 · `5y_capex` 108.4 · `5y_da` 150.3 ($M).**
So the published 74/159 was computed on an earlier cut of the same tagged data. The **cap** error is
independent and larger: it is a stale price, ~$10.55 a share against a 2026-09-18 close of $8.07.

## 2. THE ROW'S TWO IMPERATIVES, TESTED RATHER THAN INHERITED
Per the TAIL-TRIAGE CORRECTION of 2026-09-12, both were read as unlabelled and tested.

**(a) `level_note_oe` — "STEP DOWN - the series has changed level".** **CONFIRMED, and the screen
understates it: the series changes level TWICE, and both are disclosed events.**
- **2020:** dining rooms closed. FY2020 operating cash fell to $138.8M from $317.6M.
- **2024-12-30:** the **Brazil Sale Transaction**. Brazil is reported as **discontinued operations
  for all periods** in the FY2024 and FY2025 10-Ks. The filed cash-flow statement
  (`0001546417-26-000009`) separates them: operating cash of **discontinued** operations was
  **$78,255 / $12,132 / $748** thousand in FY2023 / FY2024 / FY2025, and **capital expenditures were
  restated** from $324,255 to $282,229 (FY2023) and from $219,691 to $192,791 (FY2022).
  **A mean drawn across FY2021-FY2025 is therefore measuring two different companies.**

**(b) `spread_caveat` — "4-construction width only (3y/5y × two capex ends): CANNOT see variation
older than the 5-year window; rebuild it [E4-25]".** **CONFIRMED. Rebuilt three ways below.**

## 3. THE REBUILD [E4-25]
*"Working with a range of possibilities is the better approach … Usually, the range must be so wide
that no useful conclusion can be reached."*

**(i) Ten windows on the mixed-perimeter tagged series** (`tools/run.py`'s own construction, 3 to
16 years, both capex ends), $M:

| window | 3y | 4y | 5y | 6y | 7y | 8y | 10y | 12y | 14y | 16y |
|---|---|---|---|---|---|---|---|---|---|---|
| capex end | 109.1 | 127.3 | 144.8 | 111.3 | 109.1 | 102.0 | 99.6 | 104.4 | 106.3 | 105.1 |
| D&A end | 162.6 | 178.1 | 193.5 | 167.3 | 162.1 | 149.3 | 150.0 | 151.0 | 152.1 | 154.2 |

Full width **99.6 to 193.5**, a spread of **94%** — which is **narrower** than the published 114%.
**So on the screen's own mixed-perimeter series, adding eleven more windows does NOT widen the
range, and the caveat's stated direction does not bite.** It bites on construction (ii) below, where
the perimeter is fixed: **the caveat is right, but for a reason it does not name.** This is exactly
what the TAIL-TRIAGE CORRECTION requires a run to check rather than inherit.

**(ii) The perimeter-consistent series — continuing operations only, which is the only version that
divides the same company by the same company.** All six inputs per year taken from the filed
cash-flow statements in `0001546417-25-000034` and `0001546417-26-000009`, $ thousands:

| FY | OCF continuing | SBC | capex | D&A | (OCF−SBC)−capex | (OCF−SBC)−D&A |
|---|---|---|---|---|---|---|
| 2022 | 348,332 | 16,282 | 192,791 | 149,900 | **139,259** | **182,150** |
| 2023 | 454,166 | 11,690 | 282,229 | 169,266 | **160,247** | **273,210** |
| 2024 | 216,000 | 7,484 | 220,737 | 175,580 | **(12,221)** | **32,936** |
| 2025 | 275,946 | 7,780 | 179,924 | 177,680 | **88,242** | **90,486** |

means: **4y 93.9 / 144.7 · 3y 78.8 / 132.2 · 2y 38.0 / 61.7 · FY2025 alone 88.2 / 90.5** ($M).
**Range on the only internally consistent perimeter: $38M to $145M — a spread of 281%, against the
published 114% and the ten-window mixed-perimeter 94%.** The screen's rebuild imperative is
therefore **upheld**, and the thing hiding the width was not the length of the window at all: it is
that inside the published series the operating-cash line and the capital-expenditure line describe
two different companies on either side of 2024-12-30.

**(iii) The lease question the brief asked.** BLMN leases nearly all its boxes. The lease note
discloses *"Leased assets obtained in exchange for new operating lease liabilities"* of
**$57,211 / $91,305 / $74,539** thousand in FY2025 / FY2024 / FY2023, plus finance-lease additions
of **$3,386 / $4,038 / $6,480**. Neither tool counts either. Treating both as capital committed,
the FY2023-FY2025 mean owner earnings is **−$0.2M** — i.e. **zero**. That construction is not
asserted as the right one; it is shown because **[E4-25]** says the width of the range is the
finding, and this is the width.

**(iv) Two constructions the brief warned about, TESTED AND REFUTED for BLMN.**
- **Capitalised software missing from capex** (the DRI defect). **Does not apply.** BLMN's filed
  consolidated statement of cash flows carries **one** investing line for fixed assets,
  *"Capital expenditures"*, and no separate capitalised-software line in any of FY2023-FY2025.
- **Working capital omitted.** **Does not apply.** BLMN's working-capital movements sit inside
  operating cash flow as seven separate change-in-assets-and-liabilities lines; the OCF-based
  construction already nets them, which is why the framework's CONVENTION uses OCF. FY2025 they net
  to **+$5,476** thousand — 2% of operating cash, not a swing factor. `floor_screen`'s
  `working_capital_flag` returned **None** for BLMN, and opening the lines confirms it.

## 4. THE FLOOR, AND WHY IT IS NOT A VERDICT
On the widest construction the arithmetic sits above **[E4-28]**'s ~10% honest expectancy and above
the **5.34%** sovereign; on the narrowest (lease-inclusive) it sits at zero. **This decides nothing.**
Q5 never opens, and the reason is the corpus's own ordering **[E5-42]**: business quality first,
price second. Recording the yield here and calling it an opportunity would be exactly the error
operator rule 9 exists to prevent — *"the analyst holding a position has an incentive to clear it."*

## 5. TOOLING DEFECTS FOUND
1. **`tools/run.py` mixes accounting perimeters on any filer with discontinued operations, in the
   flattering direction.** `floor_screen.py` has carried `ocf_continuing()` since the AMD run of
   2026-09-07 — it removes separately-tagged discontinued-operations cash from OCF. **`run.py` has
   no such function**; its `OCF` tag list lets the *total* tag win, while its capex and D&A lists
   resolve to the *restated continuing-operations* figures from the newest 10-K. For BLMN FY2023
   that pairs **$532.4M of operating cash (which includes $78.3M Brazil earned)** with **$282.2M of
   capex that excludes Brazil**, overstating that year's conservative end by **$78.3M, or 49%.**
   This is the "fix applied to one path and not its twin" hazard that `floor_screen.py`'s own
   comments say has been found three times in two days — found a fourth time here, in the other
   direction. **No tool was changed by this run; the defect is reported, not patched.**
2. **`Screens/floor_screen.py` mixes the perimeter the other way, conservatively.** Its
   `ocf_continuing()` correctly returns continuing-operations OCF, but `da_annual()` and
   `capital_acquired()` take the **largest resolving value per year**, which for BLMN FY2022 and
   FY2023 returns the **pre-restatement, Brazil-inclusive** capex ($330.7M vs $282.2M for FY2023)
   and D&A ($191.2M vs $169.3M). The max rule is right for the MCD subcomponent case and wrong
   here. The direction is conservative, so it does not flatter — but it is still not one company,
   and it is part of why the published 74/159 cannot be reproduced.
3. **The published row's `cap_m` was ~24% stale in price.** Not a code defect; a refresh-date one.
   It is worth recording because `cap_m` is the denominator of four downstream fields, and a stale
   cap on a falling stock makes a name look **less** cheap than it is, which is the direction that
   causes a name to be *skipped*, not bought.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, file closed. Q3-Q6 recorded
      as **not opened** with the reason, which is the hard sequence, not an omission.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on
      the filed FY2025 income statement and Item 1 alone.
- [x] Every UNRESEARCHED verdict names the artifact — **there are none.**
- [x] Every UNKNOWABLE verdict states what cannot be known — **there are none.** The Q2 verdict is
      OUT, and [E4-19]'s separating test was asked aloud: no document is missing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked by hand
      (FY2025 operating cash flow $276,694 against the filed statement, plus the continuing /
      discontinued split of $275,946 / $748 that neither tool reads correctly).
- [x] Owner earnings on a multi-year mean; windows stated (ten of them, plus a perimeter-consistent
      four-year rebuild); capex band disclosed as a judgment — **and reported ONLY under the
      COMPUTATION — NOT A CLEARANCE heading**, because Q4 never opened.
- [x] Competitor row filled — eight filers, each from its own most recent 10-K with the accession
      recorded; two peers excluded with named reasons; two disclosure limits stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury daily
      par yield curve), dated 09/18/2026, struck 2026-09-21.
- [x] Value stated as a round-number range, not a point estimate — **not applicable; no value is
      stated**, because Q5 did not open.
- [x] One bar chosen, not both — **not applicable; neither bar was used.** Windage count: **zero.**
      No conservatism was applied anywhere, because no valuation was made.
- [x] Prices dated; aggregator used for the live quote only and flagged (Yahoo, close of
      2026-09-18).
- [x] Run committed to git — after Step 0, after Q1, after Q2, and at the fold.

## REGISTER
- Verdict: [ ] IN  [x] **OUT (about the business)**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
- **One line:** Bloomin' Brands fails **[E3-03] criterion 2** on its own Item 1 — *"At an aggregate
  level, all major casual dining restaurants in markets in which we operate would be considered
  competitors of our concepts"* — with combined U.S. traffic down in five consecutive filed periods
  and **(13.5)% compounded FY2022-FY2025** against average check **+19.9%**, a restaurant-level
  margin falling 13.3% → 11.7%, and a position of **7th of 8 on operating margin and 8th of 8 on
  return on net tangible operating assets** in a competitor row struck from eight filers' own 10-Ks.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
- **REVERSAL CONDITION, recorded in words in place of a price alert** (gate-clearers only get
  alerts; the QLYS ruling of 2026-09-07). This file reopens only on a change in the **business**,
  never on a change in the price. The named test: **four consecutive quarters of positive Combined
  U.S. comparable-restaurant traffic, with average check growth no greater than traffic growth**,
  reported in BLMN's own 10-Q MD&A traffic table — i.e. guests returning rather than prices rising —
  **accompanied by a restaurant-level operating margin back above 13.3% and a GAAP operating margin
  that moves BLMN out of the bottom two of the competitor row.** Anything short of that is the
  turnaround working on the P&L without changing the answer to [E3-03] criterion 2, which is what
  the file turned on. Price is not a reopening condition at any level **[E5-35]**.
