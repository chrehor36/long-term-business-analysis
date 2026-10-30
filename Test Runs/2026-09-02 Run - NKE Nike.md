# Company Run — NIKE, Inc. (NYSE: NKE) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this template and
that document disagree, the document governs.

**POSITION NOTE, declared before any verdict:** the operator holds **no NKE position** (checked
against `PORTFOLIO.md`). This is a fresh entry run: Q1→Q5 in hard sequence, stop at the first
non-IN. Q6 is answered regardless, but there is no **[E2-28]** hold read, because nothing is held.

**BIAS DECLARATION [operator protocol rule 9; E4-27, E4-26, E3-41].** Six pulls were named before
the arithmetic started. All six are recorded so a reader can check them against the file.

1. **This project has never found a consumer brand that clears Q2, and the operator said so in the
   brief.** That is a prior, and a prior is exactly what **[E4-26]** says to hunt against. The Q2
   test was therefore framed the hard way — *what would have to be true for NIKE to be a franchise*
   — and the answer was hunted in NIKE's filings, in eleven competitors' filings, and in the two
   series that would settle it (units and ASP, and the same-market head-to-head in China).
2. **NIKE is the strongest brand in its category and the analyst knows it.** *"Never, ever, think
   about something else when you should be thinking about the power of incentives"* **[E4-27]**.
   The pull here runs **toward** clearing Q2 on reputation. The antidote applied: **no Q2 limb is
   scored on brand strength as such**; every limb is scored on a filed number.
3. **Seven names have already failed at Q2 in this queue and it would be easy to reach for the same
   conclusion by habit.** So the counter-case is written out in full at Q2 under **[E4-51]** —
   *"I'm not entitled to have an opinion unless I can state the arguments against my position better
   than the people who are in opposition"* — before the ruling, and it is a real case.
4. **The disconfirming facts run the other way in five places and this file states them first.**
   NIKE is the largest seller of athletic footwear and apparel in the world; its gross margin **rose**
   20 basis points in fiscal 2026; **North America — 44% of revenue — turned**, with revenue +5%,
   wholesale +14%, footwear units +6% and EBIT +14%; it holds **$9.0 billion** of cash and short-term
   investments against $7.9 billion of debt; and it is rated **A+ / A2**. None of that is undone by
   anything below and none of it is omitted.
5. **The operator supplied two factual premises and one of them is wrong.** The brief says the screen
   counts one share class, and that capex/D&A is 2.51x so the capex end is conservative. **Both are
   tested at Stage 0 against the filed cover page and the filed cash-flow statement. The share-count
   defect is real but it is not a class defect, and the capex/D&A direction is the opposite of the
   brief's.** Corrected before anything is built on them.
6. **The analyst who spends a long run on a big name has an incentive to produce a big finding.** The
   run therefore pre-registered, before computing, that **a Q2 IN would be a fully successful run**,
   and that the deciding evidence would be the **competitor row in Greater China** — same market,
   same consumer, same period — because that single comparison strips out every confound (scale,
   fiscal-year offset, cost-of-sales definition) that makes the rest of the row arguable.

**A "no" is a fully successful run. So is a "yes." Neither was decided in advance.**

---
# STAGE 0 — FIVE-MINUTE ARTIFACT CHECK
*Reported before the framework opens, per the operator's instruction. Four legs: share classes and
market cap by hand, the dividend decomposition, the boom test the operator asked to have verified,
and the capex band direction. Each leg names what it corrects.*

## (a) SHARE CLASSES AND MARKET CAP — **done by hand. The screen's cap is wrong by 19.5%, but NOT for the reason the brief gives, and the error runs the CONSERVATIVE way.**

**The brief's premise:** *"NKE has Class A and Class B — the screen counts ONE class and this is a
live defect, see the Ford run."* **Tested against the filed cover page. The premise is half right:
the cap is defective; the mechanism is staleness, not class omission.**

**The filed cover page, FY2026 Form 10-K, verbatim:**

> *"As of July 8, 2026, the number of shares of the Registrant's Common Stock outstanding were:
> **Class A 281,387,752** · **Class B 1,202,110,951** · **1,483,498,703**"*

**Both classes are economic and both must be counted.** Item 5 of the same filing, verbatim:
*"The Class A Common Stock is not publicly traded, but **each share is convertible upon request of
the holder into one share of Class B Common Stock**."* One-for-one, at the holder's option, with no
consideration. Class A is therefore Class B with a voting privilege and a trading restriction, and
**1,483,498,703 is the economic share count**. The Consolidated Statements of Shareholders' Equity
confirm the conversion is live and continuous: 7 million Class A converted in fiscal 2024, 8 million
in fiscal 2025, **9 million in fiscal 2026**.

**What the screen actually did, traced to the tag:**

| step | value | evidence |
|---|---|---|
| newest `dei:EntityCommonStockSharesOutstanding` in SEC `companyfacts` | **855,351,589 at 2015-07-17** | accession 0000320187-15-000113 — the **FY2015** 10-K |
| what that 2015 number is | **Class A 177,457,876 + Class B 677,893,713 = 855,351,589** | FY2015 10-K cover, read directly |
| split guard applied (2-for-1, December 2015, after the measurement date) | **× 2 = 1,710,703,178** | correct behaviour of the guard |
| true count today | **1,483,498,703** | FY2026 10-K cover, 2026-07-08 |
| **error** | **+15.3% too many shares** | |

**So the 2015 figure was already the COMBINED count of both classes. The screen did not omit a
class. It froze the count at 2015 — because `dei:EntityCommonStockSharesOutstanding` went
DIMENSIONAL (Class A / Class B members) after the December 2015 split and SEC `companyfacts` drops
dimensioned facts — and then correctly doubled a stale number.** This is the **LEVI mechanism**
recorded in `Screens/shares_staleness.py`, firing on a mega-cap. The 18-month staleness guard in
`prep_lists.py` should have caught it and returned `SHARES_STALE`; **NKE nonetheless carries a
cap in `2026-09-01 MASTER RUN QUEUE.csv`, so the guard did not bind on the path that built that
file.** Recorded as a tooling work order at the foot of this run.

**And the direction matters.** The stale count is 15.3% **too high**, so the screen's cap was too
high, so the screen's yield was too **low**. **The defect made NIKE look worse, not better** — the
opposite of the LEVI and Ford direction. The screen's 4.66% bottom-boundary yield is really 5.57%
on its own owner-earnings number.

**THE CAP, built by hand:**
- **1,483,498,703 shares (FY2026 10-K cover, 2026-07-08) × $38.12 (close, 2026-09-01) = $56,551M.**
- **Prices are aggregator-sourced and flagged: Yahoo Finance chart API, retrieved 2026-09-02.**
  Closes: **$38.12 (09-01), $39.06 (08-31), $39.60 (08-28), $38.44 (08-27), $38.59 (08-26).**
  **52-week range $37.97 – $76.97. The stock is within 0.4% of its 52-week low.**
- The screen's **$67,598M** reconciles to $39.51 × 1,710,703,178 — a live price on a dead share
  count. **The run uses $56,551M throughout.**
- **No convertible instrument, no warrants, no preferred outstanding.** Redeemable preferred stock
  is carried at **$—** on the balance sheet at both year ends (Note 8). Long-term debt is eight
  plain senior unsecured bonds, none convertible (Note 6).

**Leg (a) verdict: the brief's class premise is corrected and discarded. A real staleness defect is
found, quantified at 15.3%, and it runs the conservative way. The cap is $56,551M.**

## (b) DIVIDEND INTEGRITY AND THE PER-SHARE DECOMPOSITION — **the compounder label does not survive. This is the TWELFTH of FIFTEEN names in this project to fail it.**

**Dividends DECLARED per share, from each 10-K's Consolidated Statements of Shareholders' Equity —
actual declared cash, no restatement, twelve consecutive years:**

| FY2015 | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $0.540 | $0.620 | $0.700 | $0.780 | $0.860 | $0.955 | $1.070 | $1.190 | $1.325 | $1.450 | $1.570 | **$1.630** |

**No cut, no flat year, no special dividend anywhere in the filed record.** Cash paid rose
$899M → **$2,407M**. **[E2-52] — dividends funded by issuance: NOT FIRED.** Net issuance is deeply
negative across the whole window: $38,085M of repurchases against $354M of option proceeds in
fiscal 2026 alone. The dividend is paid out of operating cash flow.

### The decomposition — and the engine is PAYOUT EXPANSION, on falling earnings
Run on reported totals so nothing hides. Every row reconciles exactly:
(1+earnings)×(1+retirement)×(1+payout)−1 = dividend growth.

| Window | **dividend growth** | **from real earnings** | **from share retirement** | **from PAYOUT** |
|---|---|---|---|---|
| **FY2021 → FY2026 (5y)** | **+8.78%/yr** | **−11.51%/yr — NEGATIVE** | +1.68%/yr | **+20.90%/yr — the whole engine** |
| **FY2019 → FY2026 (7y)** | **+9.56%/yr** | **−3.64%/yr — NEGATIVE** | +1.28%/yr | **+12.27%/yr** |
| **FY2016 → FY2026 (10y)** | **+10.15%/yr** | **−1.89%/yr — NEGATIVE** | +1.64%/yr | **+10.46%/yr** |

**Payout of net income went 28.7% (FY2016) → 30.1% (FY2021) → 77.7% (FY2026).**

**Three findings, and the third is the one that matters:**
1. **Real earnings growth is negative on every window tested, including the ten-year one.** Net
   income $3,760M (FY2016) → **$3,108M (FY2026)**. This is the COLM/UNH artifact, not the PNR engine.
2. **Share retirement contributes 1.3 to 1.7 points of a 9 to 10 point dividend growth rate** —
   despite **$38,085 million** of repurchases over the same eleven years.
3. **Diluted EPS was $2.16 in FY2016 and $2.10 in FY2026 — a compound rate of −0.28% a year over ten
   years, through $38 billion of buybacks.** The per-share compounding is not merely weak. It is
   **negative**, and it is negative *after* the mechanism that is supposed to manufacture it.

**Leg (b) verdict: PASS on integrity (no specials, no issuance-funded payout, no cut in twelve
years) and FAIL on the compounder label. The dividend record is real; the earnings behind it are
not growing.**

## (c) ⛔ THE BOOM TEST — **THE OPERATOR IS RIGHT. The test is wrong here, and the run reproduces both the test and its failure from the filed statements.**

**The operator's instruction:** *"MY BOOM TEST SAID 'STEADY' AND I THINK THE TEST IS WRONG HERE —
VERIFY IT."* **Verified. It is wrong, the mechanism is identified, and the correction changes the
answer by roughly a third.**

### (c)(i) The nine-year series, reproduced to the dollar from the filed cash-flow statements

Owner earnings on the screen's construction, OCF − SBC − capital acquired, $ millions. **Every row
below was recomputed from the filed Consolidated Statements of Cash Flows, not from the brief:**

| FY | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| OCF | 4,955 | 5,903 | 2,485 | 6,657 | 5,188 | 5,841 | **7,429** | 3,698 | **2,868** |
| SBC | 218 | 325 | 429 | 611 | 638 | 755 | 804 | 709 | 715 |
| capex | 1,028 | 1,119 | 1,086 | 695 | 758 | 969 | 812 | **430** | 684 |
| **OE (capex end)** | **3,709** | **4,459** | **970** | **5,351** | **3,792** | **4,117** | **5,813** | **2,559** | **1,469** |

**All nine figures match the brief exactly. The series is sound. The test applied to it is not.**

### (c)(ii) Why the test returns "steady", and why that is the wrong answer

The test compares **recent-3 (FY2024–26) = 3,280** against **earlier-6 (FY2018–23) = 3,733** and
finds them within 12%, so it reports no boom signature. **The comparison is arithmetically correct
and substantively meaningless, for one reason:**

> **The recent-3 window STRADDLES the break. FY2024 (5,813) is the BEST of the nine. FY2025 (2,559)
> and FY2026 (1,469) are the two WORST of the nine. The window averages the peak against the trough
> and reports the midpoint as the level.**

**Split the series where the business actually broke, not where the window happens to fall:**

| period | years | mean OE (capex end) | mean OE (D&A end) |
|---|---|---|---|
| **FY2018 – FY2024** | 7 | **4,030** | 4,213 |
| **FY2025 – FY2026** | 2 | **2,014** | **1,810** |
| **change** | | **−50.0%** | **−57.0%** |

**A 50% two-year step down is not "steady." It is the largest break in the series, and the test
cannot see it because the test measures a mean, not a level.**

### (c)(iii) The break is NOT a cash-flow artifact — it is on the income statement too

This is the test that matters, because a two-year cash-flow dip can be working capital. **It is not.
The income statement moves with it, from the filed Consolidated Statements of Income:**

| | FY2021 | FY2022 | FY2023 | **FY2024** | **FY2025** | **FY2026** |
|---|---|---|---|---|---|---|
| Revenues | 44,538 | 46,710 | 51,217 | **51,362** | 46,309 | 46,398 |
| Gross margin | 44.8% | 46.0% | 43.5% | **44.6%** | 42.7% | **42.9%** |
| **EBIT** | 6,923 | 6,856 | 6,195 | **6,539** | **3,778** | **3,850** |
| **EBIT margin** | 15.5% | 14.7% | 12.1% | **12.7%** | **8.2%** | **8.3%** |
| Net income | 5,727 | 6,046 | 5,070 | **5,700** | **3,219** | **3,108** |
| Diluted EPS | $3.56 | $3.75 | $3.23 | **$3.73** | **$2.16** | **$2.10** |

**Revenue fell 9.7% from the FY2024 peak and has not recovered. EBIT fell 42% in one year and stayed
down. Net income fell 44% and stayed down. The cash-flow collapse and the earnings collapse are the
same event, and it is two years old, not one.**

### (c)(iv) [E4-41] applied in BOTH directions — the honest run-rate

> *"about $500 million less than we actually reported"* — **[E4-41]**, the corpus's only pro-forma
> that ever disclosed earnings too **high**. Favourable exogenous breaks in the window are named and
> removed before the mean is trusted.

**Removed from the HIGH end (against the bear case):**
- **FY2024's $7,429M of OCF contains a $908 million inventory RELEASE** (filed cash-flow line,
  *"(Increase) decrease in inventories 908"*) — a one-time working-capital drawdown after the
  2022–23 glut, not earnings. FY2024 OE at the capex end falls **5,813 → 4,905**.
- **FY2021's 5,351** sits on the stimulus and reopening year: revenue +19%, and capex was cut to
  **$695M**, the lowest in a decade.

**Added back to the LOW end (against the bull case being over-punished):**
- **FY2026's $2,868M of OCF is depressed by a $684 million IEEPA tariff receivable** outstanding at
  year end. The 10-K states, verbatim: *"As of May 31, 2026, we received $302 million and recorded
  **$684 million of outstanding IEEPA tariff receivables** … Subsequent to May 31, 2026, we received
  substantially all of the remaining IEEPA tariff receivable."* **That is cash, it arrived, and it is
  added back: adjusted OCF $3,552M.**
- **FY2025's $430M of capex is the lowest in eleven years** against a D&A charge of $775M. Capex at
  55% of depreciation is under-maintenance, not efficiency, so FY2025's capex-end figure is
  flattered and the **D&A end ($2,214M) is the honest one for that year** — which is exactly what
  **[E3-44]**'s default is for.

**THE RUN-RATE, built from those two corrections:**

| | (c) = capex | (c) = D&A |
|---|---|---|
| FY2025 | 2,559 *(flattered — capex 55% of D&A)* | **2,214** |
| FY2026, adjusted for the collected tariff receivable | 2,153 | **2,090** |
| **two-year run-rate** | **2,356** | **2,152** |

### (c)(v) ⚠️ THE OPERATOR'S FRAMING IS PARTLY DISCONFIRMED, and the AEO precedent requires this be said before the verdict

**The AEO run of 2026-09-01 ran the same boom flag, partly disconfirmed it, and showed that five
independent windows clustered tightly. The operator's instruction on this run was explicit:
*"Do not assume my framing is right in either direction — report what the windows give."* Reported.
The windows cluster, and the clustering is real:**

| window | (c) = capex | (c) = D&A |
|---|---|---|
| 3y FY2024–26 | 3,280 | **3,150 — the low** |
| 4y FY2020–23 | 3,558 | 3,713 |
| 5y FY2022–26 *(the corpus default [E2-42, E1-03])* | 3,550 | 3,533 |
| 9y FY2018–26 *(the brief's window)* | 3,582 | **3,685 — the high** |
| 11y FY2016–26 | 3,298 | 3,463 |

**Five independent multi-year windows, ten constructions, and every one of them falls between
$3,150M and $3,685M — a total width of 17%.** On the mean, the series is not merely "steady"; it is
**remarkably** steady, and a reader who saw only this table would be right to say so. **That half of
the operator's suspicion is disconfirmed and the run states it plainly rather than burying it.**

**But the clustering is not independent evidence of a stable level, and the reason is mechanical:**

> **Every multi-year window from three years upward CONTAINS FY2024 — the best year of the nine at
> $5,813M — and the longer ones also contain FY2021 at $5,351M. The windows do not agree because the
> earnings are stable. They agree because they are re-averaging the same two peak years.** The first
> window that excludes FY2024 is the two-year, and it drops **43%**, to $2,014M / $1,810M.

**So the honest report is that the two halves of the question have different answers, and both are
recorded:**
- **On the MEAN: the operator's framing is WRONG. Ten constructions across five windows cluster
  within 17% and the mean genuinely is steady.**
- **On the LEVEL: the operator's framing is RIGHT, and it is right for exactly the reason given —
  the last two years are the two worst of the nine, they are 50% below the prior seven-year mean,
  and the income statement moves with them.** Revenue, gross margin, EBIT, net income and EPS all
  broke in the same year and all stayed broken. **A collapse that is visible on five separate
  statement lines is a level, not a dispersion.**

**Which one governs is a judgment, and the run makes it and shows its work.** **[E2-42]** sets the
corpus default at five years and that window gives **$3,533–3,550M**; that figure is carried at Q5
and it is the most favourable defensible number in this file. **[E5-11]** and **[E4-41]** are the
authority for going further: a window that straddles a structural break is measuring two businesses,
and *"a wide spread is also a Q4 finding in its own right."* **[E3-55]** is the check in the other
direction — volatility with a certain endgame is not a defect — and it does not rescue this series,
because the mechanism here is **not** a bouncing figure around a stable mechanism (See's losing money
eight months a year); it is **five income-statement lines that reset together and did not come back.**

**Both numbers are therefore reported at Q5, side by side, and neither is suppressed.**

**LEG (c) VERDICT — the answer to the operator's question, in one line:**

> **The mean is steady and the level is not, and the level is what a buyer receives. Ten
> constructions across five multi-year windows cluster within 17% at $3,150–3,685 million — but
> every one of them contains the peak year, and the corrected current run-rate is roughly
> $2.0–2.4 billion. On the corpus's own five-year default window the bottom-boundary yield is 6.25%
> against a 5.27% sovereign; on the corrected run-rate it is 3.8% to 4.2%, which does not clear the
> bond. Neither figure clears the [E4-28] floor.**

**And the reason the test failed is generalisable, so it is written down as a tooling finding:** the
boom detector compares a **recent-3 mean** with an **earlier mean**. It is built to catch a *spike
inside the window*. It is structurally blind to a **step change at the window's own boundary**,
because a peak year sitting one place inside the recent window cancels the trough years beside it.
**NKE is the cleanest possible instance: best year and two worst years, all three inside recent-3.**
The fix is not a new threshold; it is that a **level test** (latest year, and the last two, against
the earlier mean) must run beside the mean test. Recorded as a work order.

## (d) THE CAPEX BAND — **the brief's 2.51x is wrong, and the direction is the OPPOSITE of the one stated.**

The brief says: *"capex/D&A is 2.51x, so the CAPEX end is the conservative one."* **Computed from the
filed cash-flow statements, capex/D&A has not been above 1.76x in eleven years and is below 1.0x on
both windows the screen uses:**

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capex | 1,143 | 1,105 | 1,028 | 1,119 | 1,086 | 695 | 758 | 969 | 812 | 430 | 684 |
| D&A | 649 | 706 | 747 | 705 | 721 | 744 | 717 | 703 | 796 | 775 | 747 |
| **capex/D&A** | 1.76 | 1.57 | 1.38 | 1.59 | 1.51 | 0.93 | 1.06 | 1.38 | 1.02 | **0.55** | **0.92** |

- **five-year window FY2022–26: capex/D&A = 0.98x**
- **three-year window FY2024–26: capex/D&A = 0.83x**
- **eleven-year: 1.23x**

**So the D&A end is the LOWER end on both live windows, and the screen's own output proves it:
the $3,150M bottom boundary the brief quotes IS the three-year D&A construction** (`3y_da`), not a
capex construction. The four constructions the screen computes are 5y_capex **3,550**, 5y_da
**3,533**, 3y_capex **3,280**, 3y_da **3,150**; the min is the D&A end.

**This is the same defect the BBWI run found on 2026-09-01** — `DA_TAGS` in
`Screens/floor_screen.py` mis-stating the **[E3-44]** direction — except that here the tag list
resolves correctly and it is the **brief's** figure that is wrong. **Recorded and corrected. NIKE is
NOT in the [E5-20] capital-intensive exception class:** capex is 1.5% of revenue, net property,
plant and equipment is $4,796M on $46,398M of revenue, and nearly all manufacturing is done by
**95 contract-manufacturer footwear factories** NIKE does not own. **D&A is a legitimate (c) proxy
here under [E3-44] and [E2-41], and both ends of the band are shown throughout.**

---
**STAGE 0 SUMMARY — three legs correct the brief, one confirms it.**
**(a)** two classes, both economic, **1,483,498,703 shares**; the screen's cap is 19.5% too high on a
**2015** share count, a staleness defect, not a class defect, and it runs the **conservative** way;
**(b)** the dividend is clean but **real earnings growth is negative on every window** and diluted
EPS is **lower than ten years ago** after $38bn of buybacks;
**(c)** **the operator is right — the boom test is blind to a step change at its own window boundary,
and the honest run-rate is $2.0–2.4bn, not $3.15bn**;
**(d)** capex/D&A is **0.83–0.98x**, not 2.51x, so **the D&A end is the conservative one** and the
screen's bottom boundary already is it.

**The framework opens.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"** **[E4-19]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a
forecast **[E4-15, E3-32]**:
- rate **5.27%** · date **2026-09-01** · source **U.S. Department of the Treasury, Daily Treasury
  Par Yield Curve Rates, 30-year constant maturity** (`home.treasury.gov` daily CSV, retrieved
  2026-09-02) — **the issuing authority itself**, per CLAUDE.md as corrected 2026-09-02. Adjacent
  observations: 5.25% (08-31), 5.22% (08-28), 5.19% (08-27). **FRED `DGS30` is the fallback and was
  not needed.**
- **Currency: USD, and this needs a note.** NIKE reports in US dollars and **44% of fiscal 2026
  revenue was United States NIKE Brand and Converse sales** (Item 1). The other 56% is earned in
  euros, yen, renminbi, sterling, won, real and others and translated. The 10-K quantifies the
  translation: *"The impact of foreign exchange rate fluctuations on the translation of our
  consolidated Revenues was **a benefit of approximately $1,023 million** for the year ended
  May 31, 2026. The impact of foreign exchange rate fluctuations on the translation of our Income
  before income taxes was **a benefit of approximately $184 million**."* **The reporting currency is
  USD and the USD sovereign is correct; the FX benefit is named and carried into [E4-41] below.
  There is no ADR and no FX step in the cap.**
- **Price: $38.12, close of 2026-09-01, via aggregator — live quote only, flagged.** 52-week range
  **$37.97 – $76.97**.
- **Market cap: 1,483,498,703 shares (FY2026 10-K cover, 2026-07-08) × $38.12 = $56,551M.**

**The filing was read** — not tagged data **[E3-27, protocol rule 4]**:
- [x] **MD&A** — the fiscal 2026 financial highlights; **"Factors Impacting Our Business"** with the
  three named action areas and the completion date; **"Other Matters"** with the IEEPA tariff ruling
  and the receivable; the non-GAAP section including the EBIT and ROIC reconciliations and the
  comparable-store-sales definition; the full results-of-operations walk; revenues disaggregated by
  product line, by channel and by segment with **unit and ASP commentary for every segment**; the
  gross-margin bridge; the selling-and-administrative walk with demand creation split out; other
  income; income taxes; **all five operating segments plus Global Brand Divisions and Corporate,
  each with its own gross margin, demand creation, overhead and EBIT**; the foreign-currency section
  with the translation quantification; **liquidity and capital resources** including the cash-flow
  activity table, the share-repurchase paragraph, the credit facilities, the commercial-paper
  programme and **the full material-cash-requirements list**; and all five critical accounting
  estimates.
- [x] **Cash-flow statement including its detail lines** — depreciation and amortisation; deferred
  income taxes; stock-based compensation; impairment and other; net foreign currency adjustments;
  **all four working-capital lines separately**; additions to property, plant and equipment;
  short-term investments in all three directions; repayment of borrowings; option proceeds;
  repurchases; dividends; **and the supplemental cash-paid-for-interest, non-cash PP&E additions and
  dividends-declared-not-paid lines** — for FY2026, FY2025 and FY2024 from the FY2026 10-K, plus the
  FY2021, FY2023 and FY2025 10-Ks for the earlier years, giving a continuous eleven-year series.
- [x] **Footnotes** — Note 1 significant accounting policies including **the cost-of-sales
  composition, demand creation, inventory valuation and PP&E lives**; Note 2 property, plant and
  equipment; Note 3 accrued liabilities; Note 5 short-term borrowings and credit lines; **Note 6
  long-term debt with the full maturity schedule and the swap notionals**; Note 7 income taxes;
  Note 8 redeemable preferred stock; Note 9 common stock and stock-based compensation; Note 10
  earnings per share; Note 14 revenues; **Note 15 segment information with the CODM disclosure**;
  Note 16 commitments and contingencies including the Belgian customs claim; **Note 17 leases with
  the maturity ladder, the weighted-average term and discount rate, and the ROU-asset additions**;
  **Note 18 severance, restructuring and other employee costs**; **Note 19 supplier finance
  programs**. Also **Item 1 Business in full** (US and international markets, significant customer,
  R&D, manufacturing concentration, competition, human capital), **Item 1A Risk Factors in full**,
  Item 2 Properties, **Item 5 with the holders-of-record counts, the repurchase-programme paragraph
  and the performance graph**, Item 9A controls, and the auditor's report with its critical audit
  matter.
- **Documents, dated, with accession numbers:**
  - **Form 10-K FY2026 (fiscal year ended 2026-05-31), filed 2026-07-15, accession
    0000320187-26-000088**, primary document `nke-20260531.htm`, US GAAP, USD. Auditor
    **PricewaterhouseCoopers LLP, Portland, Oregon**, report dated 2026-07-15, verbatim: *"**We have
    served as the Company's auditor since 1974.**"* Unqualified on the financial statements **and**
    on internal control over financial reporting. **One critical audit matter: "Accounting for
    Income Taxes."**
  - **Form 10-K FY2025, filed 2025-07-17, accession 0000320187-25-000047** — read for the fiscal
    2025 unit and ASP series.
  - **Form 10-K FY2023, accession 0000320187-23-000039** and **FY2021, accession
    0000320187-21-000028** — read for the FY2019–FY2023 channel and Greater China series.
  - **Form 10-K FY2015, accession 0000320187-15-000113** — read for the 2015 cover count that the
    screen froze on.
  - **Form 8-K 2026-06-23, accession 0000320187-26-000070** — Item 5.02, the CFO transition, with
    exhibit 99.1.
  - **Form 8-K 2026-08-10, accession 0000320187-26-000112** — Item 5.02, the Chief Accounting
    Officer resignation.
  - **Form 8-K 2026-06-18, accession 0000320187-26-000068** — director retirement, exhibit 99.1.
  - **Form 8-K 2026-06-30, accession 0000320187-26-000076** — fiscal 2026 results, exhibit 99.1.
  - **DEF 14A filed 2026-07-15, accession 0000320187-26-000089.**
- **Figure cross-checked against the filed statement (operator rule 4):** **Net cash provided by
  operations, fiscal 2026 = $2,868 million**, identical in (a) the Consolidated Statements of Cash
  Flows, (b) the MD&A "Cash Flow Activity" table, (c) the MD&A narrative (*"In fiscal 2026, cash
  provided by operations was **$2,868 million**"*), and (d) the XBRL tag
  `NetCashProvidedByUsedInOperatingActivities` under accession 0000320187-26-000088.
  **Second check: Depreciation and amortisation, fiscal 2026 = $747 million**, identical on the
  filed cash-flow statement and in the tagged data — this is the figure that decides the (c)
  direction at Stage 0(d), so it was verified on the face of the statement rather than taken on the
  tag. **Third check: total shares outstanding 1,483,498,703**, reconciled from the cover page to
  the Consolidated Statements of Shareholders' Equity (281 + 1,202 million at 2026-05-31).
- **Fiscal-year convention:** *"All references to fiscal 2026, 2025 and 2024 are to NIKE, Inc.'s
  fiscal years ended May 31."* **No 53-week years and no fiscal-calendar change in the window.**
- **Perimeter:** **no acquisition, disposal, spin-off, restatement or reverse split in the eleven-year
  window.** Goodwill is **$240M** and identifiable intangibles **$259M** — together **1.3% of total
  assets** — unchanged for two years. **This is not the HON, PNR or BBWI perimeter class.** The
  share count moves only through buybacks, option exercises and Class A→B conversions, all visible
  on the equity statement.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language.** NIKE owns a trademark and rents the
  attention of athletes. It designs shoes and clothes, has **none of them made in its own factories**
  — *"Nearly all of our footwear and apparel products are manufactured outside the United States by
  independent manufacturers"*, **95 finished-goods footwear factories in 11 countries**, with
  **Vietnam 52%, Indonesia 27% and China 16%** of footwear units — and sells them two ways: to
  **wholesale accounts** ($27,453M, 61% of NIKE Brand revenue) and through **NIKE Direct**
  ($17,720M, 39%), which is 587 owned stores in the United States and abroad plus digital in over
  40 countries. It keeps **42.9 cents of gross profit on the revenue dollar** — struck after
  inventory cost, warehousing, freight and product design, which NIKE puts **inside** cost of sales.
  Out of that 42.9 cents, **10.2 cents goes to demand creation** (advertising and athlete
  endorsements) and **24.5 cents to operating overhead**, leaving roughly **8.3 cents of EBIT**.
  The balance sheet is almost all working capital: **$7,501M of shoes and clothes, $5,931M owed by
  wholesalers, $4,796M of net property**, on $38,410M of assets. Capital expenditure is **1.5% of
  revenue**. The whole business is: *put a trademark on a shoe somebody else made, spend $4.75
  billion a year making people want it, and sell it for two and a half times what it cost.*
- **The scarce input this business controls.** **The Swoosh, the Jumpman, and the athlete roster.**
  The trademark is genuinely owned and genuinely permanent. The roster is **rented**: the 10-K
  discloses **"endorsement contract obligations, including associated marketing commitments, of
  approximately $15.5 billion, with approximately $1.7 billion payable within 12 months."** The
  factories are not owned, the retail shelf is mostly not owned, and the consumer is not contracted.
  **One scarce input is owned outright and one is leased at $1.7 billion a year.** Whether the
  combination is a moat is Q2's question, and Q2 tests it.
- **Will the fundamentals look broadly the same in ten years?** **Yes as to the mechanism.** People
  will buy athletic footwear; branded athletic footwear will be designed in one place, made in
  another, and sold through a mix of wholesale and direct. Nothing about the physics is changing.
  What is uncertain is **whose** trademark is on the shoe — a question about the business, tested at
  Q2, not about understandability.
- **[E4-46] check:** *"if we can't make a decision in five minutes, we can't make it in five
  months."* This decision does not need five months. Five reportable segments, one industry, one
  reporting currency, nineteen footnotes, no financial subsidiary, no equity-method investee of any
  size, and a product a child can identify by its logo at fifty paces. **It is inside the circle.**
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**This is the question, and it is not obvious either way. The run states the case FOR first, in
full, per [E4-51], then tests each limb against a filed number, then rules.**
Class **NARROW and NARROWING** → **NONE on [E3-03]'s decisive criterion** · Direction **[E4-32]
NARROWING, and the competitor row proves the narrowing is RELATIVE, not cyclical**.

### THE CASE FOR NIKE AS A FRANCHISE — stated as its holders would state it **[E4-51]**

> *"I'm not entitled to have an opinion unless I can **state the arguments against my position
> better than the people who are in opposition**."* — **[E4-51]**

1. **NIKE is the largest seller of athletic footwear and apparel in the world**, and says so on the
   first page of its MD&A. At $46,398M it is **1.9x adidas** (EUR 24,811M), **8.5x Deckers**
   ($5,472M), **15x On** (CHF 3,014M), **4.2x Lululemon** ($11,103M) and **5.0x New Balance**
   ($9.2bn, company-stated). No competitor is within a factor of two.
2. **Gross margin ROSE 20 basis points in fiscal 2026, to 42.9%**, in the worst two years the company
   has had — and it rose while the company was deliberately liquidating inventory. A commodity does
   not hold 42.9% through a destocking.
3. **North America — 44% of revenue — turned.** Fiscal 2026: revenue **+5%**, wholesale **+14%**,
   **footwear units +6%**, gross margin **+210 basis points**, **EBIT +14%**. This is the first
   segment to finish the reset and it worked.
4. **The damage is self-inflicted, named, and being reversed.** The 10-K describes the three actions
   in plain words and dates their completion: *"we expect to complete these actions by the end of
   December 2026."*
5. **The brand has outlived every previous attacker.** Reebok, adidas twice, and Under Armour — which
   is now at **−3.3% operating margin and −3.8% revenue** on its own latest 10-K.
6. **It is capital-light and it is not levered.** $4,796M of net property on $46,398M of revenue;
   **$9,027M of cash and short-term investments against $7,942M of debt**; rated **A+ / A2**;
   interest covered **6.8x by operating cash flow after all capital expenditure** even in the worst
   year of the eleven.
7. **Even in that worst year it earned 26.3% pre-tax on unleveraged net tangible operating assets**
   **[E2-43]**, and its own disclosed ROIC was **18.7%**.

**That is a real case. Every number in it is filing-sourced and none of it is withdrawn below. What
follows does not dispute that NIKE is a large, profitable, well-financed business. It disputes that
it is a franchise, which under [E3-03] is a different and narrower claim.**

### [E3-03], the three criteria

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."*
> — **[E3-03]**

- **(1) Needed or desired — [x] YES, emphatically.** People buy athletic footwear every year and
  NIKE sells more of it than anyone.
- **(2) Thought by its customers to have NO CLOSE SUBSTITUTE — [ ] FAILS, on two years of the
  company's own unit-and-price disclosure and on eleven competitors' filings.** The evidence is
  set out in the next three sections. **This limb is the criterion, and it is the one that fails.**
- **(3) Not subject to price regulation — [x] YES.** Passes, and it is passed by almost every
  business.

### THE PRICING TEST — **[E2-44]** and **[E4-37]** — and it fires in the company's own words

> can it raise prices *"even when product demand is flat and capacity is not fully utilized"*
> without fear of significant loss of market share or unit volume? — **[E2-44]**

> *"you can almost measure the strength of a business over time by **the agony they go through in
> determining whether a price increase can be sustained**"* … *"it's not a great business when you
> have to have a prayer session before you raise your prices a penny."* — **[E4-37]**

**Fiscal 2026 is exactly [E2-44]'s condition — demand flat, capacity under-utilised — and NIKE's
answer, on the face of its own MD&A, is that average selling price went DOWN.**

**NIKE Brand footwear, global, currency-neutral, verbatim from the two most recent 10-Ks:**

> **FY2025:** *"NIKE Brand footwear revenues decreased 11% on a currency-neutral basis. **Unit sales
> of footwear decreased 8%**, while **lower average selling price ("ASP") per pair reduced footwear
> revenues by approximately 3 percentage points. Lower ASP per pair was primarily due to higher
> discounts** and changes in channel mix, partially offset by strategic pricing actions."*

> **FY2026:** *"NIKE Brand footwear revenues were $29.5 billion … On a currency-neutral basis, NIKE
> Brand footwear revenues decreased 2%. **Unit sales of footwear decreased 1%, while lower average
> selling price ("ASP") per pair reduced footwear revenues by approximately 1 percentage point.**"*

**Two consecutive years in which BOTH units and price fell.** And the word "discounts" is the
company's own explanation, segment by segment, in fiscal 2026:

| segment | fiscal 2026 footwear ASP, verbatim from the MD&A |
|---|---|
| **EMEA** | *"**Lower ASP per pair was primarily due to higher discounts**, partially offset by product mix."* — footwear ASP −3pp |
| **APLA** | *"ASP per pair was flat as product mix and strategic pricing were **offset primarily by higher discounts** and channel mix."* |
| **Converse** | *"Gross margin contraction of 490 basis points **primarily due to lower ASP** … **Lower ASP primarily reflects higher discounts** and channel mix."* |
| **EMEA apparel** | *"**Lower ASP per unit was primarily due to higher discounts**, partially offset by product mix."* |

**And the strategy itself is written as a discounting programme.** MD&A, "Factors Impacting Our
Business", verbatim:

> *"Marketplace Management: Repositioning NIKE Brand Digital as a full-price platform and reinvesting
> in wholesale distribution. This includes **liquidating inventory through increased markdowns across
> NIKE Direct, and higher sales returns and discounts with our wholesale partners** to reduce
> inventory and create capacity for new product."*

**[E4-37]'s agony metric does not merely fire. There is no price increase to have agony about: the
plan is markdowns, in writing, in the filing.** **[E2-44] limb 1: FAIL.**

**[E2-44] limb 2 — can it grow dollar volume "with only minor additional investment of capital"?**
**The capital-lightness is genuine and passes** (capex 1.5% of revenue; net PP&E fell from $5,000M
to $4,796M while revenue was flat). **But there is no dollar-volume growth to accommodate:** revenue
$51,362M (FY2024) → **$46,398M (FY2026), −9.7%**. **Score [E2-44] at 1 of 2, and the limb that fails
is the one about pricing power.**

**[E3-33] and [E5-28] — untapped pricing power: NOT CLAIMED and NOT CLAIMABLE.** **[E5-28]** says
claiming this class is claiming a monopoly or near-monopoly. **Sweep named and bounded, per the
absence-claim rule: the FY2026 and FY2025 10-Ks' MD&A, Item 1 Competition and Item 1A Risk Factors
were read for any statement that price is being held below what the market would bear. No instance
found** — the disclosure runs the other way, to markdowns. **No computation anywhere in this file
rests on unexercised pricing power.**

### THE PHYSICAL SERIES — **[E4-55]**, and it is worse than the Precision Steel case

> Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level — *"a serious
> reverse, not likely to disappear in some 'bounce back' effect."* Dollar revenue flattered by
> pricing is how a shrinking franchise hides; **the physical series is the honest one.** — **[E4-55]**

**NIKE publishes its unit series every year, by segment, and it is a candour credit — recorded as
one before it is used.** COLM, RPM, CSL and ALG did not.

**NIKE Brand footwear UNITS, currency-neutral, from the FY2025 and FY2026 10-Ks:**

| | FY2025 | FY2026 | **two-year cumulative** |
|---|---|---|---|
| **Global** | **−8%** | **−1%** | **−8.9%** |
| North America | −10% | **+6%** | −4.6% |
| EMEA | −8% | −2% | −9.8% |
| **Greater China** | **−11%** | **−14%** | **−23.5%** |
| APLA | −2% | −3% | −4.9% |
| **Converse (total units)** | not stated | **−31%** | — |

**The [E4-55] pattern here is the inverse of Precision Steel's and it is worse. There, units fell
and price rises held the dollars up. Here, units fell AND price fell, in the same two years,
and the company names discounts as the reason.** Corroborating physical series from the same
filings: **comparable store sales −4% globally** in fiscal 2026 (North America −2%, EMEA −7%,
Greater China −6%, APLA −4%); **NIKE Brand Digital sales $9.6bn → $8.6bn, −12%**, *"primarily due
to reduced traffic"*; **Jordan Brand $8,701M (FY2024) → $7,034M (FY2026), −19.2%.**

**And the honest counterweight [E4-26]: North America footwear units rose 6% in fiscal 2026.** That
is real, it is the largest segment, and it is the single strongest piece of evidence against
everything above. It is also **one year, in the one geography where NIKE is repairing distribution
it had itself removed** — the wholesale doors it cut under the direct-to-consumer pivot and has now
restored. **Recovering ground you gave away is not the same as taking ground.**

### THE COMPETITOR ROW — required **[E3-28]**

> *"**I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing.**"* — **[E3-28]**

**Peers named: 11 — and the list is NIKE's own.** Item 1, Competition, FY2026 10-K, verbatim:

> *"We compete internationally with a significant number of athletic and leisure footwear companies,
> athletic and leisure apparel companies, sports equipment companies and large companies having
> diversified lines of athletic and leisure footwear, apparel and equipment, including **adidas,
> Anta, ASICS, Deckers, Li Ning, lululemon athletica, New Balance, On, Puma, Under Armour and V.F.
> Corporation**, among others."*

**Nine of the eleven were obtained from filings. ASICS and Puma were not pulled** (Tokyo and
Frankfurt listings; the fetch was not attempted within this session) — **named, and the obstacle is
named: not a data gap in the deciding evidence, because the deciding evidence is Greater China and
neither ASICS nor Puma leads there.** New Balance is private and appears only as a company
statement, flagged as such.

**THE ROW, each company's own latest fiscal year, in its own reporting currency, never converted:**

| | **NIKE** | Deckers | On Holding | Lululemon | adidas | ANTA | Li Ning | *Skechers* | VF Corp | Under Armour |
|---|---|---|---|---|---|---|---|---|---|---|
| FY end | **2026-05-31** | 2026-03-31 | 2025-12-31 | 2026-02-01 | 2025-12-31 | 2025-12-31 | 2025-12-31 | *2024-12-31* | 2026-03-28 | 2026-03-31 |
| source | 10-K | 10-K | 20-F | 10-K | Annual Report | HKEX | HKEX | *10-K* | 10-K | 10-K |
| accession / ref | 0000320187-26-000088 | 0001628280-26-037664 | 0001858985-26-000008 | 0001397187-26-000020 | pub. 2026-03-04 | HKEXnews 2026-03-25 | HKEXnews 2026-03-19 | *0000950170-25-030016* | 0000103379-26-000030 | 0001336917-26-000073 |
| Revenue | **$46,398M** | $5,472M | CHF 3,014M | $11,103M | €24,811M | RMB 80,219M | RMB 29,598M | *$8,969M* | $9,605M | $4,966M |
| **Revenue growth** | **+0.2% rep · −2% c/n** | **+9.8%** | **+30.0% · +35.6% cc** | +4.9% | +5% · **+10% cc** | **+13.3%** | +3.2% | *+12.1%* | +1.1% | **−3.8%** |
| Gross margin | **42.9% — LAST of 10** | 57.7% | **62.8% — 1st** | 56.6% | 51.6% | 62.0% | 49.0% | *53.2%* | 54.8% | 45.5% |
| **Operating margin** | **8.2% — joint 7th of 10** | 23.1% | 12.5% | 19.9% | 8.3% | **23.8% — 1st** | 13.2% | *10.1%* | 6.0% | **−3.3% — last** |
| Net income | $3,108M | $1,024M | CHF 204M | $1,579M | €1,385M | RMB 15,662M | RMB 2,936M | *$730M* | $255M | $(496)M |

**THREE LIMITS ON THIS ROW, stated BEFORE it is used [E3-61]:**

1. **GROSS MARGIN IS NOT COMPARABLE ACROSS THESE TEN, AND THE RUN THEREFORE DOES NOT RANK ON IT.**
   NIKE's own accounting policy, verbatim: *"**Cost of sales consists primarily of inventory costs,
   as well as warehousing costs (including the cost of warehouse labor), shipping and handling
   costs**, third-party royalties, certain foreign currency hedge gains and losses and **product
   design costs**."* NIKE puts warehousing, freight **and design** inside cost of sales; several
   peers do not. **NIKE's 42.9% and On's 62.8% are not the same measure and the run does not treat
   them as such. Operating margin is the cleaner cross-peer line and it is the one ranked above.**
   The row is still worth printing because the *direction* of NIKE's own gross margin over time is
   internally comparable, and because the operating-margin ranking is not close.
2. **THE PERIODS ARE NOT ALIGNED.** NIKE's fiscal 2026 ends 2026-05-31; Deckers and Under Armour end
   2026-03-31; VF 2026-03-28; Lululemon 2026-02-01; **On, adidas, ANTA and Li Ning all end
   2025-12-31, five months before NIKE**. Skechers' last data point is eighteen months older than
   NIKE's. **A five-month offset in a fast-moving consumer market is a real limit and it is carried
   explicitly rather than smoothed.**
3. **[E3-61]'s deeper limit governs everything:** *"The row shows position; it cannot show conduct …
   **I think you'd have to know the people involved.**"* On's +35.6% and ANTA's +13.3% are conduct as
   much as position.

### ⛔ THE DECIDING COMPARISON — GREATER CHINA, where every confound disappears

**This is the test that was pre-registered at the bias declaration, and it is the one that settles
Q2. Same market. Same consumer. Same currency exposure. Roughly the same period. No cost-of-sales
definitional problem, because the metric is REVENUE GROWTH.**

| company | China line as each defines it | latest year | growth | source |
|---|---|---|---|---|
| **NIKE** | **Greater China segment** | **$5,847M** | **−11% reported · −13% currency-neutral** | FY2026 10-K, segment table |
| **Lululemon** | China Mainland segment | $1,755M | **+29% · +28% constant dollar; comps +20%** | FY2025 10-K |
| **ANTA Sports** | group revenue, overwhelmingly China | RMB 80,219M | **+13.3%** | HKEX annual results 2026-03-25 |
| **adidas** | Greater China segment | €3,623M | **+5% reported · +9% currency-neutral** (adidas brand alone **+13% c/n**) | Annual Report 2025 |
| **Li Ning** | PRC channels (29,598.4 less 427.1 other regions) | RMB 29,171M | **+3.5%** *(arithmetic on filed absolutes)* | HKEX annual results 2026-03-19 |
| On Holding | not disaggregated below Asia-Pacific | APAC CHF 511M | *APAC +96.4% · +106.7% cc* | 20-F; **China-only UNAVAILABLE** |

**EVERY OBTAINABLE COMPETITOR GREW IN CHINA. NIKE ALONE SHRANK, AND IT SHRANK 13% CURRENCY-NEUTRAL.**

**And the margin moves the same way, which removes the last escape.** adidas's Greater China segment
gross margin **rose 2.9 percentage points to 52.6%**, and adidas's own attribution is verbatim:
*"**reduced discounting**, lower sourcing costs, and a better business mix"* — while NIKE's Greater
China gross margin **fell 30 basis points** and NIKE's own explanation for its ASP declines, in the
same market, is **higher discounts and channel mix**. **In the same country in the same period, one
competitor raised margin by discounting less and NIKE lowered price and lost 14% of its footwear
units.**

**ANTA states the share number, verbatim from its Chairman's Statement:**
> *"According to data from a global authoritative institution, **ANTA Sports' market share in the
> Chinese sportswear market climbed to 21.8% (2024: 20.8%)**, reinforcing its position as the
> industry leader, while maintaining a firm foothold among the top three globally."*

*(Recorded with its own limit: ANTA's FY2024 IR release claimed 23.0% for 2024 and the FY2025
report restates 2024 as 20.8% — a different provider or basis, and the two series are not mixed. The
institution is not named. The number is reported as ANTA's claim, not as a fact.)*

**adidas's CEO states the direction, verbatim from the Annual Report 2025 interview:**
> *"adidas' market share is significantly higher than it was three years ago."*
> *"If you look at **our biggest competitor** and its size compared to ours, then that should be
> answer enough. I can't see any market where we cannot gain substantial share over time."*

**And NIKE's five-year Greater China record, from its own segment tables across four 10-Ks:**

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | **FY2026** |
|---|---|---|---|---|---|---|
| Revenue | **8,290** | 7,547 | 7,248 | 7,545 | 6,586 | **5,847** |
| **EBIT** | **3,243** | 2,365 | 2,283 | 2,309 | 1,602 | **1,278** |
| **EBIT margin** | **39.1%** | 31.3% | 31.5% | 30.6% | 24.3% | **21.9%** |

**Revenue −29.5% and EBIT −60.6% over five years, in a market every named competitor grew in. That
is not an aberrational cycle [E3-30]. It is a share transfer, and the recipients are named and
filed.**

### THE ATTACKER'S TEST — **[E2-45]** — answered by two live companies, not hypothetically

> *"how I would like, assuming I had ample capital and skilled personnel, to compete with it"* —
> the shelf's one forward-looking moat test. — **[E2-45]**

**The attack does not need to be imagined. It has been executed twice inside the window, by
companies a fraction of NIKE's size, and both are in NIKE's own competitor list.**

- **On Holding**, founded 2010: net sales **CHF 724.6M (2021) → CHF 3,014.0M (2025)**, a **4.2x in
  four years**, **+35.6% currency-neutral in 2025**, at a **62.8% gross margin** and a **12.5%
  operating margin**, with **Asia-Pacific +106.7% currency-neutral**. On's 20-F names its target
  first: *"Primary competitors include established global sportswear companies and specialized
  performance brands, such as **Nike, Inc.**, adidas AG, Under Armour, Inc., Brooks Sports Inc.,
  Hoka One One (Deckers Outdoor Corporation), ASICS Corporation, New Balance Athletics, Inc.,
  lululemon athletica Inc., …"* and states the intent: *"we believe we are well-positioned to
  **capture further market share**."*
- **HOKA (Deckers)**: brand revenue **$891.6M (FY2022) → $2,587.3M (FY2026)**, a **2.9x in four
  years**, **+15.9% in the latest year**, at a **56.9% brand gross margin and a 35.2% brand
  operating margin** — a segment operating margin **4.2x NIKE's company-wide 8.3%**.
- **New Balance**, private: **$9.2 billion of CY2025 sales, +19%**, on the company's own statement
  of 2026-02-19 *(company statement, not a filing, and flagged as such — no SEC registration
  exists; EDGAR company search returns "No matching companies")*.

**The attacker's answer is therefore not a thought experiment.** With **no scale, no endorsement
roster on NIKE's order of magnitude, and no distribution advantage**, a fifteen-year-old Swiss
running company grew 35.6% currency-neutral while NIKE fell 2%, and a boot company's running brand
compounded to $2.6 billion at a 35% operating margin. **[E2-45] is answered against NIKE by the
filed record, not by speculation.**

### ⛔ THE SHARPEST FORM OF THE ATTACKER TEST — return on unleveraged net tangible operating assets

**Method imported unchanged from the AEO run of 2026-09-01, which found Abercrombie earning 66.9%
against AEO's 15.1% on this measure. It is the sharpest available [E2-45] test because it asks the
attacker's actual question: how much capital does it take to earn a dollar here, and does the
incumbent's scale buy it a better answer than the challenger's?**

**Denominator, per [E2-43]** — *"unleveraged net tangible assets … the best guide to the economic
attractiveness of the operation"* — **= net property, plant and equipment + inventories + trade
receivables − trade payables. Numerator = operating income. Both sides computed by the same formula
for every company, every figure from SEC `companyfacts` form 10-K or 20-F, deduplicated by period
end.**

| company | FY end | operating income | denominator | **return on unleveraged net tangible operating assets** |
|---|---|---|---|---|
| **Deckers (HOKA, UGG)** | 2026-03-31 | $1,263M | $759M | **166.3% — 1st** |
| **Lululemon** | 2026-02-01 | $2,211M | $3,594M | **61.5% — 2nd** |
| **On Holding** | 2025-12-31 | CHF 377M | CHF 719M | **52.4% — 3rd** |
| **NIKE** | **2026-05-31** | **$3,797M** | **$14,628M** | **26.0% — 4th** |
| *Skechers (last filed)* | *2024-12-31* | *$904M* | *$3,503M* | *25.8%* |
| VF Corp | 2026-03-28 | $577M | $2,647M | 21.8% |
| Under Armour | 2026-03-31 | $(163)M | $1,775M | **−9.2% — last** |

**Three limits, stated before the row is used.** (1) **adidas, ANTA and Li Ning are NOT on this
table** — they are not SEC registrants and their balance sheets were not pulled from HKEX and the
adidas annual report within this session. **Named, with the obstacle. The three missing filers are
the three that would most likely score BELOW NIKE** (adidas's operating margin is 8.3%, level with
NIKE's), **so their absence flatters NIKE's ranking rather than damaging it, and the run says so.**
(2) **Operating-lease right-of-use assets are excluded from every denominator**, consistently — the
SHOE-run convention. NIKE ($2,838M) and Lululemon ($2,034M of PP&E plus a large lease book) are both
affected; capitalising leases into the denominator would lower NIKE and Lululemon together and would
not change the ordering against Deckers or On. (3) **Deckers' 166.3% sits on a $759M denominator**
and a tiny $338M property base; the ratio is genuine but the base is small, and a reader should
know it.

**What the row says, and it is the [E2-45] answer in one number:**

> **A well-capitalised attacker with skilled personnel does not need NIKE's scale to beat NIKE's
> returns. Deckers earns 6.4x NIKE's return on the same measure. Lululemon earns 2.4x. On — one
> fifteenth of NIKE's revenue, fifteen years old, with no endorsement roster of consequence — earns
> 2.0x.** The incumbent's $46 billion of revenue, sixty-year trademark, $15.5 billion endorsement
> book and 587 owned stores buy it **the fourth-best return of seven**, and it is only ahead of a
> stale Skechers, a conglomerate in decline and a company losing money.

**And NIKE's own series on the same measure, from its own balance sheets, is the [E4-32] direction
test stated in the one metric [E3-46] says to ask first** — *"the best businesses, by definition,
are going to be businesses that earn very high returns on capital employed over time"*:

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | **FY2026** |
|---|---|---|---|---|---|---|
| EBIT ÷ unleveraged net tangible operating assets | **51.7%** | 47.2% | 41.8% | 46.4% | 27.9% | **26.3%** |

**Halved in two years, and NIKE was ahead of every company in the table above at 51.7% in fiscal
2021. It is now behind three of them. That is not a margin cycle; it is the relative position
moving, which is what [E4-32] says to measure.**

### **[E4-04]** — must the moat be CONTINUOUSLY REBUILT, or merely defended?

> *"A moat that must be **continuously rebuilt** will eventually be no moat at all."* — **[E4-04]**
> The test the framework sets: *"does a lapse in spending destroy the structure, or merely narrow it
> — and does the spending defend the same advantage, or buy its replacement?"* Coca-Cola's
> advertising defends the same trademark **[E3-49]**; Mitsui's Rhodes Ridge buys a replacement
> deposit.

**NIKE's moat has two components and they answer this test differently, so the run splits them.**

- **The Swoosh trademark is the Coca-Cola case.** It is owned outright, it is sixty years old, and
  advertising defends the same asset. **This half passes [E4-04].**
- **The athlete and team roster is the replacement case.** It is contracted, it expires, the
  incumbent ages out, and a competitor can outbid for the successor. **$15.5 billion of contracted
  obligations, $1.7 billion payable within twelve months.** That spending does not defend the same
  advantage; it **re-buys** it, athlete by athlete, cycle by cycle.

**And the maintenance cost is rising against a falling base, which is the observable form of the
test:**

| demand creation expense | FY2021 | FY2023 | FY2024 | FY2025 | **FY2026** |
|---|---|---|---|---|---|
| $ millions | 3,114 | 4,060 | 4,285 | 4,689 | **4,754** |
| **% of revenue** | 7.0% | 7.9% | 8.3% | 10.1% | **10.2%** |

**Spending on the moat is up 53% since fiscal 2021 in dollars and up 320 basis points as a share of
revenue, while revenue is down 9.7% from its peak and EBIT margin has halved.** That is money going
into the moat and coming out narrower — which is what [E4-04]'s "continuously rebuilt" describes.

**And the surfing question [E3-51], [E4-36].** *"when a surfer gets up and catches the wave … he can
go a long, long time. But if he gets off the wave, he becomes mired in shallows."* Of the **four
causes of extreme success [E4-36]**, NIKE's record reads as a **nonlinear combination** — brand,
scale, endorsement and distribution — **with a large wave component**: basketball and the
sneaker-as-fashion wave from the 1980s, and the athleisure and retro wave through 2021. **The
current wave is running comfort and performance, and On and HOKA are on it.** A surfing run is not a
moat; the advantage lives in the wave.

### **[E2-53]** — the dominance class — **FAILS, and this is the sharpest single test in the file**

> *"Once dominant, **the newspaper itself, not the marketplace, determines just how good or how bad
> the paper will be. Good or bad, it will prosper.**"* — **[E2-53]**

**NIKE holds the most dominant position in its industry that exists — the largest seller of athletic
footwear and apparel in the world, 1.9x its nearest rival. It did not prosper.** Between fiscal 2024
and fiscal 2026, on that dominant position: **revenue −9.7%, EBIT −41%, net income −45%, diluted EPS
−44%, and the share price from a 52-week high of $76.97 to $38.12.** Position did not set the
economics. **Execution did — every day, in product, in channel and in markdown timing.** That is
[E2-53] failing on the record, and it is also **[E3-38]**'s have-to-be-smart-**every-day** condition
being met, which is why Q3 would have been a binary gate.

**[E5-18]'s companion test — *"if it won't stand a little mismanagement it's not much of a
business… We're not looking for mismanagement. We like the capacity to stand it."*** NIKE **survived**
its strategy error: it is solvent, investment-grade, and still the largest. **But it did not stand
it.** Four years of a mistaken channel strategy cost roughly half the operating profit and roughly
half the market value, and required a CEO change to reverse. **The capacity to stand mismanagement is
what a franchise has. This business absorbed the mismanagement in its earnings.**

### **[E4-32]** — DIRECTION, which outranks existence

> the moat *widened every year* is *"the primary criterion of a great business"* — *"that does not
> necessarily mean that the profit is more this year than last year."* — **[E4-32]**

**[E4-32] explicitly forbids reading falling profit as a narrowing moat. So the direction is scored
on relative and structural measures only, not on the profit line:**

| axis | direction | evidence |
|---|---|---|
| Share in the second-largest market | **NARROWING** | China −13% c/n while adidas +9%, ANTA +13.3%, Li Ning +3.5%, Lululemon +29% |
| Pricing conduct **[E2-44]** | **NARROWING** | ASP down two years running; company names "higher discounts" |
| Physical units **[E4-55]** | **NARROWING** | footwear units −8% then −1%; China −23.5% cumulative |
| Cost of maintaining the moat **[E4-04]** | **NARROWING** | demand creation 7.0% → 10.2% of revenue |
| Return on operating assets **[E2-43]** | **NARROWING** | 51.7% (FY2021) → 46.4% (FY2024) → **26.3% (FY2026)** |
| Owned brand portfolio | **NARROWING** | Converse revenue **−31%**, EBIT **−93%** to $18M, in one year |
| Direct channel asset | **NARROWING** | NIKE Direct $21,519M → $17,720M (−17.7%); digital −12% on *"reduced traffic"* |
| North America distribution | **WIDENING** | wholesale +14%, units +6%, EBIT +14% — **the one axis that widened** |

**Seven axes narrowing, one widening, and the one widening is the repair of self-inflicted damage in
the home market.**

### THE [E2-30] AND [E3-48] READING OF THE DTC PIVOT — recorded HERE because it is a Q2 fact

**The direct-to-consumer pivot and its reversal, quantified from four 10-Ks:**

| NIKE Brand, $M | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | **FY2024** | FY2025 | **FY2026** |
|---|---|---|---|---|---|---|---|---|
| Sales to wholesale customers | 25,423 | 23,156 | 25,898 | 25,608 | 27,397 | 27,758 | **25,883** | **27,453** |
| **Sales through NIKE Direct** | 11,753 | 12,382 | 16,370 | 18,726 | **21,308** | **21,519** | 18,783 | **17,720** |
| **NIKE Direct % of NIKE Brand** | 31.6% | 34.8% | 38.7% | 42.2% | **43.7%** | 43.6% | 42.1% | **39.2%** |

**NIKE Direct grew from 31.6% to 43.7% of NIKE Brand revenue in four years, then fell back to 39.2%
in two. The asset the company spent four years and billions of dollars building is $3,799 million
smaller than at its peak, a decline of 17.7%, and the digital half of it is shrinking fastest
(−12% in fiscal 2026, on "reduced traffic").** Wholesale, the channel that was deliberately reduced,
is back to within 1% of its fiscal 2024 level.

**This is a Q2 fact, not only a Q3 one, because of what it proves about substitution.** When NIKE
withdrew from wholesale doors, **the doors did not stay empty.** They were filled — by On, by HOKA,
by New Balance, by adidas, by Anta in China. **A product with no close substitute cannot be
displaced from a shelf it vacates, because there is nothing to put there.** NIKE vacated shelf and
the shelf was refilled, and when NIKE came back it had to come back **at a discount** and with
*"higher sales returns and discounts with our wholesale partners."* **[E3-03] criterion 2 was tested
by the company itself, unintentionally, over four years, and the answer came back negative.**

*(The strategy history is recorded for Q3's register: "Consumer Direct Offense" (2017), "Consumer
Direct Acceleration" (2020), and now the "Sport Offense operating model" named in the 8-K of
2026-06-23. Three strategy relabelings in nine years is an **[E2-30]** institutional-imperative
reading — *"an institution will resist any change in its current direction"* until it reverses, then
*"the behavior of peer companies … will be mindlessly imitated."* It is recorded, not used to decide
Q2, because **[E2-37]**, **[E2-38]** and **[E3-39]** forbid a manager finding from deciding a
business question in either direction.)*

### INVENTORY — the branded-goods test the operator asked for

> *"a branded goods company with rising inventory and falling margin is discounting."*

| | FY2022 | FY2023 | FY2024 | FY2025 | **FY2026** |
|---|---|---|---|---|---|
| Inventories, $M | **8,420** | 8,454 | 7,519 | 7,489 | **7,501** |
| Revenue, $M | 46,710 | 51,217 | 51,362 | 46,309 | 46,398 |
| **Inventory / revenue** | 18.0% | 16.5% | 14.6% | **16.2%** | **16.2%** |
| Inventory valuation reserve, $M | n/d | n/d | 155 | 233 | 213 |
| Gross margin | 46.0% | 43.5% | 44.6% | 42.7% | 42.9% |

**The honest reading, and it is mixed [E4-26]. Absolute inventory did NOT rise in fiscal 2026** —
$7,501M against $7,489M, and the 10-K states the composition: *"Inventories as of May 31, 2026 were
$7.5 billion, flat compared to the prior year, **primarily reflecting an increase in units, offset
by product mix**."* **More units, cheaper units, same dollars.** **But inventory as a share of
revenue is 160 basis points HIGHER than in fiscal 2024 on 9.7% less revenue**, and the reserve
against it is **37% higher than two years ago**. **The classic pattern — inventory ballooning while
margin collapses — belongs to fiscal 2022–23 (18.0% of revenue, margin 46.0% → 43.5%), and NIKE has
worked most of it off. What remains is a unit-heavy, mix-cheapened book at an elevated ratio. That is
a discounting position, not a crisis position.**

### THE RULING

**Score of the Q2 tests, each against a filed number:**

| test | result |
|---|---|
| **[E3-03]** (1) needed or desired | **PASS** |
| **[E3-03]** (2) **no close substitute** | **FAIL** — the deciding limb |
| **[E3-03]** (3) not price-regulated | **PASS** |
| **[E2-44]** limb 1 — price with flat demand | **FAIL** — ASP down two years, "higher discounts" |
| **[E2-44]** limb 2 — capital-light growth | **PASS on capital, but there is no growth** |
| **[E4-37]** agony metric | **FIRES** — the plan is markdowns, in writing |
| **[E4-55]** physical series | **FAIL** — units and price both down, two years |
| **[E3-33] / [E5-28]** untapped pricing power | **NOT CLAIMABLE** — no instance found |
| **[E2-53]** dominance class | **FAIL** — the most dominant position did not carry it |
| **[E4-04]** continuously rebuilt | **SPLIT** — trademark passes, roster fails, cost rising |
| **[E4-32]** direction | **NARROWING on seven of eight axes** |
| **[E2-45]** attacker's test | **FAIL** — already executed, twice, by On and HOKA |
| **[E2-45] / [E2-43]** return on unleveraged net tangible operating assets | **FAIL — 4th of 7. Deckers 166.3%, Lululemon 61.5%, On 52.4%, NIKE 26.0%. NIKE led this table at 51.7% in FY2021** |
| **[E3-46]** high returns on capital employed *over time* | **FAIL on the second half — 51.7% → 26.3% in two years** |
| **[E3-28]** competitor row | **9 of 11 obtained; NIKE last of 10 on gross margin, joint 7th of 10 on operating margin, 9th of 10 on growth** |

**And the deciding evidence, in one sentence:**

> **In Greater China, in the same period, on the same consumer, every obtainable competitor grew —
> adidas +9% currency-neutral with its gross margin UP 290 basis points on "reduced discounting",
> ANTA +13.3% with its stated share up a point, Lululemon +29%, Li Ning +3.5% — and NIKE fell 13%
> currency-neutral with its footwear units down 14% and its EBIT margin down from 39.1% to 21.9%.
> A product thought by its customers to have no close substitute does not lose a quarter of its unit
> volume in five years in the world's second-largest market to four named companies that all file
> their numbers.**

**What this ruling does NOT say.** It does not say NIKE is a bad business — it earns 26.3% pre-tax on
its net tangible operating assets in its worst year, holds net cash, and is rated A+. It does not
say NIKE will not recover — North America says it may. It does not say the brand is worthless — a
42.9% gross margin on a cost base that includes warehousing and freight says otherwise. **It says
that under [E3-03] the class is a franchise only if customers think there is no close substitute,
and the customers have answered, with their feet, in units, in China, and in the doors NIKE vacated
and could not reclaim at full price.** **[E4-18]** applies: *"I'd rather have the universe be a
little smaller than it really is, than being interpreted as larger than it is."*

**Can I name the document that would resolve this differently?** **No — the documents are in, on both
sides.** Eleven filings were read and nine competitors were priced from theirs. **This is not
UNRESEARCHED. It is a finding about the business.**

- **VERDICT: [x] OUT** — at **[E3-03]** criterion 2, on the pricing conduct **[E2-44, E4-37]**, the
  physical series **[E4-55]**, the direction **[E4-32]** and the Greater China head-to-head
  **[E3-28]**.

---
# ⛔ THE FILE CLOSES HERE.
**Operator rule 2: hard sequence. Q2 returned OUT, which is permanent and about the business.**
Q3 and Q4 below are **NOT REACHED** and are recorded for the register only. Q5 **does not open**;
what appears under it is **COMPUTATION — NOT A CLEARANCE** (operator rule 3) and carries **no entry
language**. Q6 is answered because a closed file still owes the next reader the metric that would
reopen it.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **NOT REACHED. Recorded for the register.**

**STEP 1 — THE WEIGHT CASE, declared even though the gate is not reached.**
- [x] **Daily execution [E3-38, E3-43, E2-70]** — **TICKED, and this is now proven rather than
  asserted.** Fashion-adjacent branded consumer goods is a have-to-be-smart-**every-day** business:
  product pipeline, channel mix, markdown timing, athlete signings. The proof is fiscal 2024–26,
  where a channel strategy error cost roughly half the operating profit.
- [ ] Control **[E1-16]** — not ticked; this would be a marketable-security position.
- [ ] Leverage **[E3-29]** — not ticked; net cash, A+/A2, 6.8x coverage.

**One box ticked → Q3 would have been a BINARY GATE and no price would compensate.** It is not
reached because Q2 closed first.

**Honesty — no disqualifier found, and that is not a finding that they are honest [E5-17].**
- **Auditor: PricewaterhouseCoopers LLP, Portland, Oregon, "auditor since 1974"** — 52 years.
  **Unqualified on both the financial statements and internal control over financial reporting.**
  One critical audit matter, **"Accounting for Income Taxes"**, driven by $953M of unrecognised tax
  benefits.
- **No restatement, no Item 4.02 filing, no material weakness disclosed** in the window read.
- **Belgian Customs Claim** disclosed in Note 16, disputed, under appeal, bank guarantees issued.
  Disclosed by the company, quantified in the guarantee balance ($1.3bn of total guarantees and
  letters of credit).

**⚠️ THE FINDING THAT WOULD HAVE DRIVEN THIS GATE — a CFO and a Chief Accounting Officer left within
seven weeks of each other, both inside the last ten weeks.**

| date | event | filing |
|---|---|---|
| **2026-06-23** | **Matthew Friend ceases as EVP & CFO** effective 2026-08-16, becomes an adviser, separates 2026-09-04. **David Denton** (ex-Pfizer, ex-Lowe's, ex-CVS) appointed EVP & CFO. | 8-K, acc **0000320187-26-000070**, Item 5.02 |
| **2026-08-04** | **Johanna Nielsen resigns as VP, Chief Accounting Officer and Corporate Controller**, effective 2026-09-04, *"to pursue another opportunity."* **Denton assumes Interim Corporate Controller and principal accounting officer.** | 8-K, acc **0000320187-26-000112**, Item 5.02 |

**Both filings carry the standard no-disagreement language, verbatim:** *"Mr. Friend's transition and
separation was not the result of any disagreement with Company management or the Company's board of
directors relating to the Company's operations, policies or practices"*; *"Ms. Nielsen's resignation
is not the result of any disagreement with the Company relating to the Company's operations, policies
or practices."* **[E4-22]**'s cockroach line is a **prompt to read, never a verdict** — and
**[E5-38]** is explicit that a fired flag is not a venality finding. **Recorded as a prompt. Both
departures are disclosed on time, with reasons, in the correct Item. The company now has a
seven-week-old CFO also serving as its principal accounting officer.** Had Q2 cleared, this would
have been the first thing read, and the resolving document is named: **the FY2027 Q1 10-Q, due
approximately 2026-10-01, and its Item 4 controls conclusion.**

**Denton's package, from the offer letter filed with the 8-K:** base **$1,450,000**, target bonus
**120%**, annual long-term target **$11,500,000** (50% PSUs / 25% options / 25% RSUs), plus a
**one-time cash award of $7,250,000** to make him whole for forfeited compensation. **Disclosed in
full, in the filing. That is candour, and it is recorded as such [E2-26].**

**⚠️ CAPITAL ALLOCATION — the buyback, and it fails [E5-08] condition 2 on the company's own
disclosed average price.**

> the two conditions: *"first, a company has ample funds … second, its stock is selling at a
> **material discount** to the company's intrinsic business value, conservatively calculated."*
> — **[E5-08]** · *"what is smart at one price is dumb at another"* — **[E5-24]**

**Item 5 of the FY2026 10-K, verbatim:**
> *"In June 2022, the Board of Directors approved a four-year, $18 billion share repurchase program …
> As of May 31, 2026, the Company had **repurchased 124.4 million shares at an average price of
> $97.57 per share for a total approximate cost of $12.1 billion** under the Share Repurchase
> Program, and approximately $5.9 billion of the Company's Class B Common Stock remains available for
> repurchase."*

**$12.1 billion spent at an average of $97.57. The quote on the run date is $38.12 — 61% below the
average paid.** Widening the window: **$38,085 million of repurchases across fiscal 2015–2026**
against a fall in diluted shares from **1,768.8 million to 1,481.0 million**, i.e. **$132.33 of cash
per net share permanently retired**, against a $38.12 quote. **Retained earnings on the fiscal 2026
balance sheet is NEGATIVE $155 million** — the accumulated profits of a sixty-year-old company have
been fully absorbed by repurchases.

**Stated with the humility clause [E4-13, E5-08]:** *"it is natural for CEOs to be optimistic about
their own businesses. They also know a whole lot more about them than I do"*, and *"infractions, even
serious ones, are innocent; many CEOs never stop believing their stock is cheap."* **This rests on
our own range and NIKE's board knew the business better than we do.** And the corpus's counter-tell
**[E2-51]** — *"A manager who consistently turns his back on repurchases … reveals more than he
knows"* — points the other way on the fiscal 2026 conduct: **NIKE paused the programme in the first
quarter of fiscal 2026 and bought nothing in the fourth**, spending only **$146M** for the year.
**Pausing at $38 after buying at $97.57 is the wrong way round on [E5-24]'s first law, and it is
recorded as such.**

**[E2-49] metric-switching, [E4-29] EBITDA promotion, [E5-15] serial issuance, [E4-30] cash-tax
tell:** NIKE presents **EBIT and EBIT margin** as non-GAAP measures with a full line-by-line
reconciliation to net income, and **ROIC** with both numerator and denominator printed. **It does not
promote EBITDA.** **[E4-29] does not fire.** Net issuance is deeply negative; **[E5-15] does not
fire.** Cash taxes paid were **$1,299M / $1,226M / $1,270M** on pre-tax income of $6,700M / $3,885M /
$3,900M — a cash-tax ratio of 19.4% / 31.6% / 32.6%, **rising, not falling**; **[E4-30] does not
fire.** **[E2-49] is a live prompt** — the company introduced ROIC as a headline measure in the same
period its EBIT margin halved — but it is disclosed with its full arithmetic and the prior-year
comparative, which is the candour case.

**Guidance [E3-48]:** NIKE's **filed** documents (10-K, 10-Q, 8-K Item 2.02) carry **no numeric
forward guidance**; the outlook is given only on the earnings call, which is not a filed document.
**Under [E3-48] there is therefore no filed projection record to score against outturn**, and the
absence of trumpeted numeric targets in the filings is, on **[E4-22]**'s third flag, a point in the
company's favour rather than against it.

- **VERDICT: NOT REACHED.** *For the record: a binary gate on [E3-38]; no honesty disqualifier found;
  the capital-allocation flag FIRES on [E5-08] condition 2 and [E5-24]; the CFO/CAO double departure
  is a live prompt to read with a named resolving document.* **Nothing in this Q3 is used to promote
  or to demote the name — [E2-37], [E2-38], [E3-39] and the guardrail forbid it in both directions.**

## Q4 — WILL IT SURVIVE? — **NOT REACHED. COMPUTATION — NOT A CLEARANCE.**

### Owner earnings — the one number **[E2-23]**

> *"(c) **the average annual amount** … that the business **requires to fully maintain** its long-term
> competitive position and its unit volume. (… the working capital **increment also should be included
> in (c)**.)"* … *"**(c) must be a guess.**"* — **[E2-23]**

**Construction (CONVENTION, per the framework's confessed conventions):** operating cash flow less
share-based compensation less (c). OCF nets the working-capital change from one audited line.
**Stock compensation is subtracted in full [E5-06]: $715M in fiscal 2026, and the eleven-year series
is subtracted in every year.** **[E3-70]** notes the reported charge is the *floor* of the correct
subtraction; the market-value measure is not obtainable from the filing and the reported charge is
used, flagged. **No look-through adjustment [E3-04] is needed: NIKE has no material equity-method or
unconsolidated minority stake.**

**THE (c) JUDGMENT, DISCLOSED [E2-23], [E3-44], [E2-41], [E5-20]:**
**(c) = the DEPRECIATION AND AMORTISATION CHARGE, and the reason is stated rather than defaulted to.**
- **NIKE is NOT in the [E5-20] capital-intensive exception class.** It owns almost no manufacturing:
  95 contract-manufacturer footwear factories in 11 countries, none of them NIKE's. Capital
  expenditure is **1.5% of revenue**; net property, plant and equipment is **$4,796M on $46,398M of
  revenue** and has **fallen** for three consecutive years. Nothing in the filing says depreciation
  understates renewal.
- **[E3-44]'s default therefore applies and is used:** *"by and large, the depreciation charge is not
  inappropriate in most companies to use as a proxy for required capital expenditures"*, and
  **[E2-41]**: *"At 95% of American businesses, capital expenditures that over time roughly
  approximate depreciation are a necessity."* Over eleven years NIKE's capex/D&A is **1.23x**; over
  the five-year default window **0.98x**. **The two ends nearly coincide, which is what [E2-41]
  describes.**
- **On the recent windows the D&A end is the LOWER of the two** (capex/D&A 0.83x on three years),
  because **fiscal 2025 capex of $430M was 55% of that year's depreciation** — the lowest ratio in
  eleven years. **Spending 55% of depreciation is under-maintenance, so the capex end of fiscal 2025
  is invalid as a maintenance figure and the D&A end is the honest one.** Both ends are printed
  throughout; nothing in the ruling turns on the choice.
- **Working-capital increment [E2-23] constraint 3:** included, because OCF carries it. Fiscal 2026's
  OCF is net of a **$1,678 million** working-capital and other outflow, of which **$684 million is the
  IEEPA tariff receivable that was collected after year end** — added back explicitly at Stage 0(c)
  rather than left buried.

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE **[E4-25]**

| window | OCF − SBC mean | **(c) = capex** | **(c) = D&A** | spread |
|---|---|---|---|---|
| **5y FY2022–26 — the corpus default [E2-42, E1-03]** | 4,281 | **3,550** | **3,533** | 0.5% |
| 9y FY2018–26 — the brief's window | 4,318 | 3,582 | 3,685 | 2.9% |
| 11y FY2016–26 | 4,192 | 3,298 | 3,463 | 5.0% |
| **3y FY2024–26 — the screen's bottom boundary** | 3,922 | 3,280 | **3,150** | 4.1% |
| **2y FY2025–26 — the post-break level** | **2,571** | **2,014** | **1,810** | 11.3% |
| **[E4-41]-corrected run-rate** *(FY2025 D&A end; FY2026 D&A end + collected tariff receivable)* | — | **2,356** | **2,152** | 9.5% |
| 1y FY2026 as filed | 2,153 | 1,469 | **1,406** | 4.5% |

- **Combined range (window spread × capex band): $1,406M to $3,685M — a width of 162%.**
- **Is the range too wide to reach a conclusion [E4-25]?** **On the level, yes — and that width IS a
  Q4 finding [E5-11].** But **[E3-55]** scopes it honestly: *"If we have a business about which we're
  extremely confident as to the business result, we would prefer that it have high volatility."*
  **The width here is NOT confident-mechanism noise. It is a step change** — the mean of the first
  seven years is 4,030 and of the last two is 2,014, and the income statement moves with it. **The
  range is wide because the level changed, which is the [E5-11] earnings-reliability finding, not a
  measurement problem.**
- **Distorted years named [E4-41], both directions:** **FY2024** carries a **$908M inventory release**
  and its owner earnings fall to 4,905 without it; **FY2021** is the stimulus and reopening year on
  the lowest capex in a decade; **FY2020** is the pandemic trough; **FY2026** carries a **$1,023M FX
  translation benefit to revenue and a $184M FX benefit to pre-tax income**, an **$986M IEEPA tariff
  recovery in cost of sales** that the company states *"largely offset[s] the impact of the IEEPA
  tariffs recognized during fiscal 2026"* — **NIKE does not quantify the tariff COST, so the run
  cannot separate the two and treats the pair as approximately neutral, and says so** — and **$385M
  of severance charges**, which under **[E5-33]** are real costs and stay in the mean.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — [x] **good, and sliding** — [ ] gruesome
**Evidence:** it is not gruesome — it does not consume capital to grow; capital expenditure is 1.5%
of revenue and net property is falling. It is not great — the return is no longer rising and the
capital it retains has not produced growth: **$38 billion of repurchases over eleven years against
diluted EPS of $2.10 versus $2.16 ten years earlier**. **[E4-43]** says the *good* class **passes**
Q4 — *"nothing shabby about earning $82 million pre-tax on $400 million of net tangible assets"* —
and NIKE earns **$3,850M pre-tax on $14,628M of net tangible operating assets, 26.3%**, which is
better than [E4-43]'s benchmark. **Q4 would not have failed here. It fails nowhere. Q2 closed it.**

### Staying power — score all three **[E5-11]**
1. **A large and reliable stream of earnings — LARGE, and no longer RELIABLE.** $3,108M of net income
   and $3,850M of EBIT, but EBIT halved in one year and the two-year owner-earnings level is 50%
   below the prior seven-year mean.
2. **Massive liquid assets — YES.** **$7,563M cash and equivalents + $1,464M short-term investments
   = $9,027M**, weighted-average maturity 103 days, all investment grade. Against **$7,942M** of
   total debt. **Net cash.**
3. **No significant near-term cash requirements — THIS IS THE TIGHT ONE, and it is the one [E5-11]
   says usually kills.** Within twelve months, from the filing's own material-cash-requirements list:
   **$2,000M of long-term debt maturing** (the 2.375% November 2026 and 2.75% March 2027 notes),
   **$1.7bn of endorsement obligations**, **$4.7bn of product purchase obligations**, **$1.6bn of
   other purchase obligations**, and roughly **$2.43bn of dividends at the declared rate**. Against
   **$9,027M of liquidity and $2,868M of operating cash flow.** The product purchases are self-funding
   from sales; **the endorsement, debt and dividend calls — roughly $6.1bn — are not.** **It is
   covered, but it is covered by the cash pile, not by the year's cash flow.**
   *(**[E5-39]**: no bank line is counted. The $2bn five-year facility, the $1bn 364-day facility and
   the $3bn commercial-paper programme are all **undrawn at both year ends** and none is relied on
   above.)*
- **Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this framework:*
  **$7,942M of long-term debt at fixed coupons of 2.375% to 3.875%, laddered to 2050**, plus
  **$3,091M of operating lease liabilities** on a 7.7-year weighted-average term at a 3.6% discount
  rate. Cash interest paid **$323M**. **[E2-54] coverage:** operating cash flow less all capital
  expenditure = $2,184M against $323M of interest = **6.8x, in the worst year of the eleven.**
  **[E3-52]** applies favourably: this is long-dated, covenant-light, fixed-rate paper, not
  covenanted bank debt due next year. **Leverage is not the problem here and is not used as one.**

### Name the specific way THIS business dies **[E2-27, E3-24]** — and model EXPOSURE, not experience **[E4-40]**

**THE MECHANISM: brand-preference migration in the two segments that carry the profit, made
irreversible by the discounting used to defend the volume.** Not bankruptcy — NIKE has net cash and
6.8x coverage and cannot die financially in any modelable scenario. **It dies as a franchise, by
becoming an ordinary large apparel company at an ordinary large apparel company's margin.** The
route: units held with markdowns → the consumer learns the price → full-price sell-through falls →
gross margin resets down → demand creation cannot be cut because the roster is contracted →
operating margin compresses toward the mid single digits, where adidas (8.3%), VF (6.0%) and Under
Armour (−3.3%) already sit.

**QUANTIFIED FROM FILED FIGURES [E3-24]:**
- **Greater China alone:** revenue 8,290 → 5,847 over five years; **EBIT 3,243 → 1,278**. Extending
  the observed −13% currency-neutral rate for three more years takes Greater China revenue to
  roughly **$3.9 billion** and, at the observed 21.9% margin, **EBIT to roughly $850 million** —
  a further **$430 million off consolidated EBIT**, 11% of the fiscal 2026 total, from one segment,
  at the rate already being run.
- **The margin scenario, in the corpus's own arithmetic style:** apply the peer-group modal operating
  margin of **6% to 8%** — where adidas, VF and a normalised Under Armour sit — to fiscal 2026
  revenue of $46,398M. **EBIT $2,784M to $3,712M**, against $3,850M reported. **NIKE is already
  inside that band at 8.3%.** That is the point: **the death is not a future event to be modelled;
  its first two years are on the filed statements.**
- **The fixed-cost floor that makes it bind:** **$15.5 billion of contracted endorsement obligations**
  cannot be cut with revenue. At $1.7bn payable within twelve months against $3,850M of EBIT, the
  roster is **44% of EBIT** and contractually senior to it.
- **What would falsify it:** North America. Fiscal 2026 gave **+5% revenue, +6% footwear units, +210
  basis points of gross margin, +14% EBIT** on a restored wholesale base. **If that repeats for two
  more years AND Greater China stops declining, the mechanism above is wrong.**

**LIKELIHOOD: [ ] likely · [x] a real possibility · [ ] a low-level possibility.**
**[E4-40] check** — *"focusing on experience, rather than exposure"*: the bull case rests on
**experience** (NIKE beat Reebok, adidas and Under Armour before). The **exposure** is different this
time and is on the filings: **the attackers are profitable at 12.5% to 23.1% operating margins while
attacking**, which Reebok and Under Armour never were, and **the largest single market loss is in a
country where the four leading competitors are domestic or entrenched and all four grew.** The
exposure, not the experience, is what is modelled above.

- **VERDICT: NOT REACHED.** *For the record: Q4 would have returned **IN**. The business is a
  **good** business under [E4-20]/[E4-43], it has net cash and 6.8x coverage, and no filed figure
  puts its survival in question. It is failing on what it IS, not on whether it lasts.*

---
# ⛔ Q5 DOES NOT OPEN. Q2 returned OUT.
**Operator rule 2.** What follows is **COMPUTATION — NOT A CLEARANCE** (operator rule 3), reported
because the queue's output contract requires a price either way, and carrying **no entry language**.

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? — COMPUTATION — NOT A CLEARANCE

**Inputs, both dated:** market cap **$56,551M** (1,483,498,703 shares, FY2026 10-K cover 2026-07-08,
× $38.12, close 2026-09-01); sovereign **5.27%** (US Treasury 30-year CMT, 2026-09-01, issuing
authority).

### 1. THE YIELD — owner earnings ÷ market cap, beside the sovereign

| owner-earnings construction | OE, $M | **yield** | **vs sovereign** | growth needed for the [E4-28] floor |
|---|---|---|---|---|
| **5y FY2022–26, (c) = capex — THE CORPUS DEFAULT WINDOW [E2-42, E1-03]** | **3,550** | **6.28%** | **+1.01 pts** | **3.72%** |
| **5y FY2022–26, (c) = D&A — the corpus default, conservative end** | **3,533** | **6.25%** | **+0.98 pts** | **3.75%** |
| 9y FY2018–26, (c) = capex *(the brief's window)* | 3,582 | 6.33% | +1.06 pts | 3.67% |
| **3y FY2024–26, (c) = D&A — the screen's bottom boundary** | **3,150** | **5.57%** | **+0.30 pts** | **4.43%** |
| **[E4-41]-corrected RUN-RATE, (c) = capex** | **2,356** | **4.17%** | **−1.10 pts** | **5.83%** |
| **[E4-41]-corrected RUN-RATE, (c) = D&A** | **2,152** | **3.81%** | **−1.46 pts** | **6.19%** |
| 2y FY2025–26 as filed, (c) = D&A | 1,810 | 3.20% | −2.07 pts | 6.80% |
| FY2026 alone as filed, (c) = D&A | 1,406 | 2.49% | −2.78 pts | 7.51% |

**The screen's own figures, corrected:** the screen reported **cap $67,598M, OE bottom $3,150M,
yield 4.66%, sovereign 5.18%, growth required 5.34%.** On the hand-built cap and the day's sovereign
the same OE figure gives **5.57% and +0.30 points, needing 4.43% growth.** **The share-count fix makes
the name look BETTER; the run-rate fix makes it look decisively WORSE, and the run-rate fix is the
larger of the two.**

**BOTH ANSWERS ARE CARRIED, per Stage 0(c)(v), and neither is suppressed.** On **[E2-42]**'s five-year
default window NIKE yields **6.25–6.28% and beats the sovereign by a full point**; on the corrected
run-rate it yields **3.81–4.17% and trails the sovereign by 1.1 to 1.5 points**. **The gap between
those two answers is the whole of the boom question, and the reason it exists is that the five-year
window contains FY2024, the best year of the nine.** **Under [E5-34] — *"we will buy the stock … if it
sells at a reasonable price in relation to **the bottom boundary of our estimate**"* — the operative
figure is the bottom, which is $2,152M and 3.81%.** **Under [E4-28]'s floor neither figure is
reached, so the choice between them does not change the Q5 outcome; it only changes how far short it
falls.**

### 2. WHAT THE PRICE ALREADY ASSUMES
- **Year-1 growth needed to justify the quote at the [E4-28] floor:** **3.7%** on the five-year mean;
  **6.2% in perpetuity** on the corrected run-rate.
- **What the business has actually done:** revenue **−9.7% over two years**; currency-neutral revenue
  **−2%** in the latest year; **net income −1.89% a year compounded over ten years**; **diluted EPS
  −0.28% a year compounded over ten years**. **Greater China −29.5% over five years.**
- **[E4-35]'s base rate applies to the 6.2% case only lightly** — the corpus's wager is that *"fewer
  than 10 of the 200 most profitable companies"* achieve 15% EPS growth over twenty years, and 6.2%
  is not 15%. **But the burden here is not the rate; it is the sign.** The business has produced
  negative real earnings growth on every window tested, and the run-rate case needs +6.2% forever.

### 3. WHAT YOU ARE PAID
- **+1.0 points over the sovereign** on the five-year mean.
- **−1.1 to −1.5 points over the sovereign** on the corrected run-rate.
- **The [E4-28] floor** — *"that's the figure we quit on"*, **rate-invariant** — **is not cleared on
  any construction.** The best of the eight, the nine-year capex mean, returns **6.33%**.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
*Zero perpetual growth, which is what the last ten years of per-share earnings support.*

| owner earnings | at the **5.27% sovereign** | at **8%** | at the **10% [E4-28] floor** |
|---|---|---|---|
| $3,550M (5y, capex end) | ~$45 | ~$30 | ~$24 |
| $3,150M (3y, D&A end) | ~$40 | ~$27 | ~$21 |
| **$2,152M (corrected run-rate)** | **~$28** | **~$18** | **~$15** |

- **conservative ~$15 · optimistic ~$45 · current price $38.12.**
- **The quote sits inside the range and above the conservative end on every construction.** Under
  **Bar 2 [E4-01]** that is the middle outcome — **"no useful conclusion — move on"** — and it is a
  finished answer. **Under Bar 1 [E4-11] no margin is applied, because there is no entry to apply one
  to.**
- **[E2-63] — state the ceiling too:** the upside is capped by the same thing that caps most
  operating businesses — *"unless more capital is continuously invested"*. NIKE's problem is the
  reverse: it has $9.0bn of liquid assets, spends 1.5% of revenue on capital, and **has no
  reinvestment outlet that has produced growth**; $38 billion of repurchases produced negative EPS
  growth over ten years. **The ceiling is a recovery to the fiscal 2024 EBIT margin of 12.7%, which
  on flat revenue would give roughly $5.9bn of EBIT and, at the 5-year owner-earnings-to-EBIT
  relationship, roughly $4.9bn of owner earnings — about $92 a share at the sovereign and about $33
  at the [E4-28] floor.** That is the bull case's arithmetic, printed, and it still needs a full
  return to the pre-break margin.

**WHICH BAR:** **neither is applied to a decision, because there is no decision.** The table is
recorded under Bar 2's arithmetic for reference only.
**WINDAGE COUNT: ONE.** Conservatism is applied once — at the **[E4-41]** normalisation, which is
applied in **both directions** (removing FY2024's $908M inventory release from the high end and
adding back FY2026's $684M collected tariff receivable to the low end). It is **not** also applied in
the discount rate — **[E3-42]**: any per-name risk premium in the rate is the named error — **not**
in the capex band (both ends are printed everywhere), and **not** in a margin of safety.

- **VERDICT: NOT OPENED.** The gate is shut by Q2, not by price. **For the record: NIKE would also
  have failed the [E4-28] floor on every construction, which makes it the fourteenth name in this
  project to reach a floor test and fail it.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*Answered because a closed file still owes the next reader the metric that would reopen it.
**Nothing is held; there is no [E2-28] hold read.***

**Pre-committed, before any entry [E1-02] — written now so it cannot be retro-fitted:**
- **Thesis-confirming metric (confirming the OUT): Greater China revenue, currency-neutral, from the
  segment table in each 10-K and 10-Q.** A third consecutive year of currency-neutral decline while
  adidas, ANTA and Li Ning grow confirms this file.
- **THESIS-BREAKING METRIC AND ITS THRESHOLD:** **two consecutive fiscal years in which NIKE Brand
  footwear ASP RISES on flat or growing unit volume, globally, as disclosed in the MD&A's own unit-
  and-ASP sentence — with Greater China currency-neutral revenue growth at or above zero in the
  second of those years.** That combination is the only evidence that would reverse the two findings
  this ruling rests on: **[E2-44]**'s pricing limb and the **[E3-28]** China head-to-head. Price
  rising while units hold is the definition of the franchise NIKE is claimed to be.
  *A secondary breaker: demand creation falling below 8.5% of revenue while revenue grows — the
  [E4-04] test running the other way, a moat getting cheaper to hold rather than dearer.*
- **Next catalyst date: the fiscal 2027 first-quarter results and Form 10-Q, expected late September
  / early October 2026** — which will also carry the first controls conclusion signed by a CFO who is
  simultaneously the principal accounting officer.

**The monitoring question [E4-17, E3-30]:** *"is this erosion just part of an aberrational cycle …
or … a way that permanently reduces intrinsic business values?"* **The competitor row answers it:
an aberrational cycle is a market event and would show up in the competitors' numbers too. It does
not. Every named China competitor grew while NIKE fell 13%. This run reads that as permanent
slippage, and states plainly that [E4-17]'s "beliefs change quite gradually" is a warning against
exactly this kind of two-year conclusion — which is why the breaker above is set at two years, not
one.**

**Position size:** **zero.** No position is taken, and none is contemplated.

- **VERDICT: [x] IN** — the exit metric is pre-committed, quantified and sourced to a line NIKE
  publishes every year.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped; **stopped at the first non-IN (Q2)**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 and Q6 are the
      only IN verdicts and both rest on filed documents.
- [x] Every UNRESEARCHED verdict names the artifact — **there are no UNRESEARCHED verdicts in this
      file**
- [x] Every UNKNOWABLE verdict states what cannot be known — **there are none**
- [x] Step 0: the filing was read, with accession numbers; **three figures cross-checked against the
      filed statements** (OCF $2,868M, D&A $747M, shares 1,483,498,703)
- [x] Owner earnings on a multi-year mean; **seven windows shown**; capex band disclosed as a
      judgment with its reasoning, and **both ends printed in every table**
- [x] Competitor row filled — **9 of NIKE's own 11 named competitors obtained from filings**; the two
      not obtained (ASICS, Puma) are named with the obstacle, and **the moat class is NOT held
      PROVISIONAL** because the deciding evidence (Greater China) is complete across every competitor
      that operates there
- [x] Sovereign is for the earnings currency, from the issuing authority, dated
- [x] Value stated as a round-number range, not a point estimate
- [x] One bar identified, and **neither applied to a decision, because there is no decision**;
      **windage count stated: one**
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] **Bias declaration written before the arithmetic; the deciding test pre-registered**
- [x] **Both halves of the boom question reported — the half that DISCONFIRMS the operator's framing
      is stated first**, per the AEO precedent and the operator's own instruction not to assume the
      framing is right in either direction
- [x] `python tools/check_framework.py` run — **PASS**: 261 ledger rows, 261 source files on disk,
      **0 phantom citations and 0 unlabelled numbers** in the framework and the template
- [x] **The same phantom-citation test applied to THIS file: 86 distinct ledger ids cited,
      0 phantom.** Every judgment in this run is justified from the corpus by ledger id
      (operator rule 8)
- [x] Run committed to git, incrementally, under the write-early protocol

## REGISTER
- **Verdict: [x] OUT (about the business, at Q2).** No position held; no hold read required.
  **Q1: IN. Q2: OUT. Q3: NOT REACHED** (would have been a binary gate on [E3-38]; no honesty
  disqualifier found; **the [E5-08]/[E5-24] capital-allocation flag FIRES**; a CFO and a Chief
  Accounting Officer departed within seven weeks). **Q4: NOT REACHED** (for the record: would have
  been **IN** — a *good* business under [E4-20]/[E4-43], net cash, 6.8x coverage). **Q5: NOT OPENED**
  (for the record: **fails the [E4-28] floor on all eight constructions**). **Q6: IN.**
- **One line:** **the largest athletic brand in the world, still earning 26.0% pre-tax on its net
  tangible operating assets and holding net cash — which has now cut its average selling price for
  two consecutive years while its unit volume also fell, which describes its own plan as
  "liquidating inventory through increased markdowns", which lost 13% of its Greater China revenue
  currency-neutral in a year when adidas, ANTA, Li Ning and Lululemon all grew there, which spends
  10.2 cents of every revenue dollar defending a moat that cost 7.0 cents five years ago, which now
  earns a lower return on its operating assets than Deckers, Lululemon and On — three companies
  between one-fifteenth and one-quarter its size — having led all three at 51.7% just five years
  ago, and whose diluted EPS is lower than it was ten years and $38 billion of buybacks ago:
  a great brand, a good business, and not a franchise.**
- **THE FOUR FINDINGS RETURNED TO THE OPERATOR:**
  1. **THE BOOM TEST IS RIGHT ABOUT THE MEAN AND WRONG ABOUT THE LEVEL — and the operator's framing
     is therefore HALF disconfirmed, which is reported before the half that is confirmed.**
     **Disconfirmed:** ten constructions across five multi-year windows cluster inside
     **$3,150–3,685M, a width of 17%** — on the mean the series really is steady, exactly as the AEO
     run found. **Confirmed:** the clustering is **mechanical, not evidential** — *every* window from
     three years upward contains **FY2024, the best of the nine at $5,813M**, and the first window
     that excludes it drops **43%**. The last two years are the two worst of the nine, they sit 50%
     below the prior seven-year mean, and **revenue, gross margin, EBIT, net income and EPS all broke
     in the same year and all stayed broken** — a collapse visible on five statement lines is a
     level, not a dispersion. **The tool's blind spot is generalisable: a recent-3-mean-versus-
     earlier-mean comparison is built to catch a spike INSIDE the window and is structurally blind to
     a STEP CHANGE at the window's own boundary, because one peak year inside the recent window
     cancels the trough years beside it. The fix is a LEVEL test running beside the mean test —
     latest year, and last two, against the earlier mean — not a new threshold.**
     **Correct run-rate: $2.0–2.4bn. The corpus's own five-year default window [E2-42] gives
     $3.53–3.55bn, and both are carried at Q5 because [E4-28]'s floor is unreached either way.**
  2. **THE SCREEN'S CAP IS 19.5% TOO HIGH, ON A 2015 SHARE COUNT.** Not a class defect: the 2015
     `dei` value of 855,351,589 was already Class A + Class B combined. The tag went **dimensional**
     after the December 2015 split, `companyfacts` drops dimensioned facts, and the split guard then
     correctly doubled a stale number to 1,710,703,178 against a true 1,483,498,703. **This is the
     LEVI mechanism firing on a mega-cap, and `prep_lists.py`'s 18-month staleness guard did not
     bind on the path that produced `2026-09-01 MASTER RUN QUEUE.csv`.** The error runs the
     **conservative** way here, which is why it survived unnoticed.
  3. **THE BRIEF'S capex/D&A OF 2.51x IS WRONG AND ITS DIRECTION IS INVERTED.** Filed capex/D&A is
     **0.98x** on five years and **0.83x** on three; the highest single year in eleven is 1.76x.
     **The D&A end is the conservative end**, and the screen's own $3,150M bottom boundary is the
     three-year D&A construction, which proves it.
  4. **THE AEO ATTACKER METRIC TRANSFERS AND IT IS THE SHARPEST TEST IN THE FILE.** Imported
     unchanged from the AEO run of 2026-09-01 (Abercrombie 66.9% against AEO's 15.1%). On
     unleveraged net tangible operating assets **[E2-43]**, same formula both sides, all from SEC
     `companyfacts`: **Deckers 166.3%, Lululemon 61.5%, On 52.4%, NIKE 26.0%, Skechers 25.8%
     (stale), VF 21.8%, Under Armour −9.2%.** **NIKE is 4th of 7 and was at 51.7% — ahead of every
     one of them — in FY2021.** Recommend this metric become a standing line in the competitor row
     for every brand-layer run.
- **Work orders: none for the business.** No verdict in this file is UNRESEARCHED. **Three tooling
  work orders** are recorded at items 1, 2 and 4 above. *(Named with the obstacle and NOT bearing on
  the deciding evidence: **ASICS and Puma** were not pulled — Tokyo and Frankfurt listings, fetch not
  attempted this session; and **adidas, ANTA and Li Ning balance sheets** were not pulled for the
  attacker metric — not SEC registrants. **All three of the missing balance sheets belong to filers
  that would most likely score BELOW NIKE, so their absence flatters NIKE and does not damage it.**)*
- **THE SINGLE STRONGEST DISCONFIRMING FACT — stated against this file's own conclusion [E4-26]:**
  **North America, which is 44% of revenue, grew 5% in fiscal 2026 with footwear UNITS up 6%,
  wholesale up 14%, gross margin up 210 basis points and EBIT up 14% — the exact combination this
  file's Q6 breaker is written to detect, achieved in the largest segment, in the first year of the
  reversal, one year before this run.** If it repeats in fiscal 2027 and Greater China stops falling,
  the Q2 ruling is wrong and the file should be reopened on the terms written at Q6.

---
## THE OUTPUT CONTRACT

**(a) THE PRICE — COMPUTATION, NOT A CLEARANCE (operator rule 3).**
> **Roughly $15 to $45 a share**, zero perpetual growth: **~$15** on the [E4-41]-corrected run-rate
> of $2,152M at the [E4-28] 10% floor, **~$28** on that same run-rate against the 5.27% sovereign,
> and **~$45** on the corpus's five-year default window [E2-42] of $3,550M against the sovereign.
> **Current price $38.12 (2026-09-01). CORRECTED MARKET CAP $56,551M** — 1,483,498,703 shares
> (Class A 281,387,752 + Class B 1,202,110,951, FY2026 10-K cover, 2026-07-08) × $38.12, against
> the screen's $67,598M. **The quote sits inside the range on every construction, which under
> Bar 2 [E4-01] is the middle outcome — no useful conclusion.**
> **No entry language. No margin of safety is applied, because there is no entry to apply one to.**

**(b) PASS / FAIL.**
> **FAIL. The file closed at Q2 — IS IT A FRANCHISE? — with a verdict of OUT**, on [E3-03]'s
> criterion 2 (no close substitute), evidenced by two consecutive years of falling average selling
> price alongside falling units, by the company's own written plan of increased markdowns, and by a
> Greater China head-to-head in which every obtainable competitor grew while NIKE fell 13%
> currency-neutral. **Q1 returned IN. Q3, Q4 and Q5 were not reached; for the record, Q4 would have
> returned IN and Q5 would have failed the [E4-28] floor on all eight constructions. Q6 returned IN.
> All six did not return IN.**
