
## UPDATE 2026-09-25 - WS: Q2 OUT. A steel processor that competes "primarily on the basis of price", and in June 2026 it borrowed $1.4bn to buy 62% of Klöckner & Co.

**Worthington Steel, Inc. (WS), wave 7 name 37, register entry 169.** Run file `Test Runs/2026-09-25 Run - WS
Worthington Steel.md`. Price $35.48 (close 2026-09-24, aggregator, flagged) x 50,948,146 shares (10-K cover for
2026-05-31, `0001968487-26-000026`) = cap $1,807.6M; sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 OUT
on the business.** This file's older screen note (WS among the decaying names, "five filed years, spun 2023, commodity
steel processing, decaying") is left as written; the run reached the same class from the filing's own words.

### The first thing the run found: the screen's Item 1.01 was the last step of a takeover, with WS as the buyer
- The screen guessed *"most likely a credit facility or offering"*. It was the **Domination and Profit and Loss
  Transfer Agreement with Klöckner & Co SE** (8-K `0001193125-26-385371`, 2026-09-08): WS *"will generally absorb all
  annual losses incurred by Kloeckner"* and offers the minority €11.00 cash or €0.67 a year.
- **The takeover**: €11.00 cash, a *"98%"* premium to the undisturbed price; 60.86% settled 2026-06-03 (€576.3M for the
  tendered shares), 61.87% on 2026-06-15, about 62% at the delisting offer; funded by **$700.0M of 7.750% secured notes
  and a $700.0M term loan at SOFR + 4.00%**. Klöckner is **two thirds of pro forma sales**; pro forma FY2025 interest
  $158.6M against operating income $204.4M; pro forma net earnings to WS $(12.4)M (8-K/A `0001193125-26-356964`).
  **WS is the acquirer, so the quote is not a spread**; the ROKU precedent excuses no gate.

### The finding
- **[E3-03] criterion (2) fails on the registrant's own words**: *"Competition is primarily on the basis of price,
  product quality and the ability to meet delivery requirements"*; products *"priced competitively, primarily based on
  market factors"*; the effect of its technical service and its plant locations *"has not been quantified"*; FY2026
  volume lost *"largely driven by increased competition"*; **the electrical-laminations leg (Tempel, bought FY2022 in
  a $376.7M year) had all its goodwill impaired *"due to increased foreign competition"***.
- **[E2-58]'s commodity equation, on the filed series**: price follows HRC ($869, $1,588, $889, $866, $754, $915 a ton,
  FY2021-FY2026); about $75M of FY2021's $221.5M operating income was inventory holding gains; **tons -14% FY2021-FY2026
  through two acquisitions [E4-55]** (a steel service-center row, Precision Steel's).
- **Competitor row (operating margin)**: WS 3.3-5.7% in normal years (0.0% in FY2026 after $114.3M of impairments);
  **Reliance 7.1-14.7%**; Ryerson -0.7% to 9.6%; Olympic Steel 2.5-5.2%; **Klöckner -0.3% (2024), 0.5% (2025)**. The
  exception's *"wide and sustainable"* cost advantage belongs, on the row, to Reliance.
- **The strongest counter-case, stated and answered**: Detroit Three shipments +17% against production +2%; gross margin
  per ton $89 to $112; "market leading positions" in tailor-welded blanks. Share won on price beside volume lost to
  competition, mix and acquisition in the per-ton figure, and a size claim the registrant does not quantify.

### Priors refuted or confirmed
- **Item 1.01 "most likely a credit facility": refuted** (the DPLTA; a cross-border takeover).
- **`wc_note` (payables 39% of FY2023 OCF): confirmed and read**: working capital absorbed $204.0M in FY2022 and
  released $139.9M in FY2023, which is also the screen's "early half straddles zero" (FY2022 owner earnings -$28.7M
  to -$5.6M).
- **SBC resolves 6 of 6 years and is complete.** **[E4-29] fires in the deal release** (EV/EBITDA 8.5x, net leverage
  "~4.0x range including synergies") and **[E4-22]'s projections flag fires** ($150M of synergies, "substantially
  accretive" to EPS); the annual bonus is 75% Adjusted EPS [E4-27].
- **Owner earnings, rebuilt FY2021-FY2026 from the Form 10 and three 10-Ks**: 5y $89.4-126.8M (4.95-7.01%), $72.0-109.3M
  to the WS owner after payments to noncontrolling interests (3.98-6.05%); the screen's $78-127M reproduces. **None of
  it includes Klöckner**, whose own 2025 owner cash was about -€37.8M; the combined company has no filed record.
- Named death as a signature only: **#11 THE PASS-THROUGH**, with #6 THE BORROWED BALANCE SHEET as a feature. Not
  entered in the index's instances column (closed at Q2); no new shape.

### Tooling defects (reported, not patched)
- **`deal_note()` classified a German domination agreement as "most likely a credit facility or offering"**, and
  **`deal_filings()` missed, for the second time in two runs, a deal signed before the latest 10-K** (the business
  combination agreement with EX-2.1, 8-K of 2026-01-22, before the 10-K of 2026-07-30): at NATH the target's side, here
  the acquirer's.
- **`acq_note` reads the acquisitions line only through the newest annual statement**, so a purchase closed three days
  after the year end is invisible, and the pre-closing stake-building sat on "Purchases of equity securities".
- `run.py`'s implied growth printed -6.6% against the screen's +5.52% (the terminal-rate definition NATH reported).
