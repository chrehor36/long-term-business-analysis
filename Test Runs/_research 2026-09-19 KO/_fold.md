
## UPDATE 2026-09-19 - KO: all four gates IN, FAIL at Q5 on price; the franchise is still there, and so is the price
`Test Runs/2026-09-19 Run - KO Coca-Cola.md`. **Q1 IN; Q2 IN, class WIDE with two limits; Q3 IN as an overlay (four prompts); Q4 IN (owner earnings about
$10.0bn, range $7.8-11.4bn); Q5 quit on at the ~10% floor, not ranked; Q6 a monitoring plan with two bands armed.** Price **US$88.25** (2026-09-18 close,
aggregator flagged; corroborated by the Q2 2026 10-Q repurchase prices) x **4,302,549,243** (the Q2 2026 10-Q cover, `0001628280-26-050503`) = cap
**US$379.7bn**; sovereign **USD 30-year 5.34%** (US Treasury, 09/18/2026). **WAVE 6, the first of the five ordinary businesses the triage dropped. Register
count at the fold, read from the register: 118 runs** (KO adds one Q5 close: Q1 4, Q2 83, Q4 2, Q5 29).

### WHAT THE 2020s FILINGS SAY ABOUT THE CORPUS'S MOST-CITED FRANCHISE
- **The case against was built first, from the filer's own text**: substitutes on the shelf and *"powerful buyers"*; currency cutting operating income 9%, 8%, 11%
  and 12% in 2022-25; US unit cases level; weight-loss drugs and sugar taxes named in Item 1A; energy ceded to Monster under a non-compete; the bottler keeping part
  of each price rise; BodyArmor written down $1.72bn.
- **What refuted the OUT case was the head-to-head, not the history.** North America price/mix compounded about +49% over 2021-25 on level cases, and segment
  operating income rose from $3,331M to $5,070M; in the same country and years PepsiCo's beverage volume fell and its margin with it. Worldwide cases 29.3bn to
  33.8bn in ten years. Operating income on the tangible capital that earns it: 67-89% (FY2021-25). **Nothing before FY2016 was used.**
- **A correction to a number carried in this file since the PEP and COKE runs**: KO's 31.5% return on NTOA (FY2025) is right on the standard formula, and on that
  formula PepsiCo is level with it (32.9%). The formula counts $18-20bn of bottler stakes, whose income sits below operating income; without them KO's figure is
  67%. **The standard formula understates a company whose bottlers are equity stakes.**

### THE PRIOR MOST LIKELY WRONG, AND HOW IT FARED
The brief's warning (operator rule 9) was that a corpus reader has an incentive to clear Coca-Cola. **The favourite hypothesis survived Q2 on 2020s evidence, and
the file then closed on price**, which is the verdict the incentive argues against: the same franchise the corpus bought at a price assuming 1.2% growth against a
9% bond (VERIFICATION, CASE 2) is priced today to need 2.6% just to match a 5.34% bond and 7.2% forever to reach the floor, against a filed 4-6%.

### A TOOLING FINDING: TWO $6BN ONE-OFFS INSIDE OPERATING CASH, THE REVERSE OF THE COKE CASE
- **The COKE run found a perpetual royalty in FINANCING, outside operating cash, which flattered the screen. At KO two one-offs sit INSIDE operating cash and
  depress it**: the $6.0bn IRS deposit (2024; the 10-K tax note says the $3,262M of 2024 tax payments *"does not include $ 6.0 billion paid in relation to
  invoices"*) and $6,069M of the $6,173M fairlife milestone (2025; the rest, $104M, in financing). `tools/run.py KO` therefore prints five-year owner earnings of
  $7.8-8.4bn and three-year $6.3-7.2bn, about $2bn a year below the adjusted $10.0-10.9bn. **The error runs the conservative way here, so no verdict turns on
  it**, but any screen ranking KO by yield ranked it about a quarter too dear. **Not fixed** (the run does not change tooling): the same class as the resume note's
  "a diagnostic that exists but never reaches the reader". A screen would need an operating-cash outlier guard that sends a reader to the MD&A liquidity
  paragraph, where both items are named.
- **Three smaller operating-cash items a TTM reader would take at face value**: the receivables factoring programme ($14.7-21.9bn of receivables sold a year; the
  outstanding balance is not disclosed, so its lift is unmeasurable), transfers of surplus pension assets into company cash ($523M, $332M), and tax-credit
  partnerships whose cost sits in investing while the benefit sits in operating cash. The TTM's $16.3bn of operating cash would have printed a 3.6% yield.
- **`tools/run.py` read the Q1 2026 cover** (*"share basis: dei cover-page count as of 2026-04-28"*) when the Q2 10-Q of 2026-07-29 was on file; immaterial here
  (the count barely moved), recorded as the known companyfacts lag. `Screens/cover_shares.py` read the right filing.

### Q3 FINDINGS WORTH KEEPING
- **The except-for flag [E2-57] fires in the headline metrics and in the pay plan together.** Releases lead with *"Comparable Currency Neutral Operating Income
  (Non-GAAP)"*; FY2024 operating income fell 12% GAAP while that measure grew 16%. The annual incentive pays on organic revenue and comparable currency-neutral
  operating income; the PSU free cash flow is adjusted to exclude *"impacts resulting from the application of the tax court rulings"*. The mitigation is
  real: the GAAP figure leads each headline pair, and the cash line is GAAP with both $6bn items named.
- **The IRS case is a candor pass**: the full exposure (*"approximately $ 14 billion"* for 2010-25), the quarterly accrual and a 3.8-point tax-rate effect are
  printed beside management's own view. No penalty has been asserted.
- **About $18bn of acquisitions in 2019-21**; BodyArmor written down twice, the second time for *"an intensifying competitive environment"*. The franchise did not
  transfer to a bought brand in a category it does not lead: the same lesson the PEP run drew from Rockstar.

### Q4
- **Owner earnings**: adjusted $9.98-10.57bn (five-year), $9.94-10.86bn (three-year), $9.52-9.99bn (seven-year), both (c) ends; as filed $7.8-8.4bn and $6.3-7.2bn;
  undistributed equity income +$0.75-0.95bn shown apart. SBC resolves in 7 of 7 years. D&A end admissible, capex end the default (capex about 2x D&A for three years).
- **Named death: stagnation, and a new shape proposed, #22 THE HABIT** (added to `Screens/SURVIVAL SHAPES - index.md`, pending the operator): the franchise is a
  consumer habit priced above its cost; medicine, taxes and labels can weaken it market by market; the business lives, rich-market volume drifts down, and the growth
  left arrives in currencies that lose value against the owner's. The tax case is a dated feature (about $20bn at worst, +3.8 points of tax rate).

### BANDS ARMED (fold step 4: a gate-clearer, as COKE and CL)
`tools/alerts.json`: **KO-rerun-band at $63** (the ~10% floor met if 2019-25's 6.1% growth in operating income before charges is granted in perpetuity on
$10.0bn of owner earnings) and **KO-floor-band at $41** (the floor met on the owner-earnings record itself, 4.1%). A ping is a prompt to re-run the gates, never
an action. A `PORTFOLIO.md` watch row was added.

### FOR THE OPERATOR
- **The Eleventh Circuit decision in the IRS case** is the one dated event that would re-price the business (about $20bn and 6% of owner earnings either way);
  it was argued 2026-06-25.
- **Proposed survival shape #22 THE HABIT**, pending your ruling, with the others (#13-#21).
- **The operating-cash outlier guard** above, for whoever next touches the screen.

### ONE THING TO KEEP
**A franchise and a purchase are different questions.** Coca-Cola passed every business gate on filings the corpus never saw, and failed on a price that asks
for growth its own record does not show.
