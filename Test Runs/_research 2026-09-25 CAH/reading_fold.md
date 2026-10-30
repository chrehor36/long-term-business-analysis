
## UPDATE 2026-09-25 - CAH: Q2 OUT. One of three national drug wholesalers, and its largest customer is also McKesson's largest; three big accounts have left for rivals since 2012.

**Cardinal Health, Inc. (CAH), wave 7 name 35, register entry 167.** Run file `Test Runs/2026-09-25 Run - CAH Cardinal
Health.md`. Price $222.62 (close 2026-09-24, aggregator, flagged) x 232,575,728 shares (10-K cover for 2026-06-30,
`0000721371-26-000038`) = cap $51.78bn; sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 OUT on the
business.**

### The finding
- **[E3-03] criterion (2) fails on what the customers did, recorded in three registrants' filings.** Express Scripts
  (2012), Walgreens (2013, $16.9bn of revenue, *"our second largest customer in fiscal 2013"*) and OptumRx (2024, 17% of
  revenue) left for rivals; Cencora's FY2025 10-K shows Walgreens and Boots at about 25% of its revenue and Evernorth at
  about 13%; **CVS Health is the largest customer of both Cardinal (28%) and McKesson (24%)**; and Cardinal pays CVS
  quarterly under the Red Oak generic-sourcing venture.
- **The demonstration clause fails on the margin record**: gross margin 5.57% (FY2015) to 3.84% (FY2026); pharmaceutical
  segment profit about the same in dollars in FY2023 as in FY2015 while revenue more than doubled; medical products at
  0.7-2.0% with $5.4bn of goodwill written off. Competitor row: distribution margins of 1.09% (McKesson), about 1.2%
  (Cencora) and 1.19% (Cardinal); Cardinal is not the low-cost operator [E3-43].
- **The strongest counter-case any wave-7 Q2 has had, stated in the run and answered**: operating working capital of
  -$8.1bn (suppliers finance the business, so growth releases cash), a rational three-firm structure with no price-war
  losses and no fourth entrant, and profit that rose after the lowest-margin customer left. The answer: the negative
  working capital travels with the account (Walgreens released it; OptumRx unwound about $2.0bn of it), and the position
  belongs to three firms jointly, priced by the customer at renewal.

### Priors refuted or confirmed
- **The screen's `wc_note` ("ONE LINE MADE THE CASH: AccountsPayable moved 114% of 2025 OCF") is wrong about the year
  it names**: FY2025 total working capital was a $523M USE; the year working capital made the cash was FY2026 (+$1,661M).
  The same defect the MHH run found in 2021, a second time running.
- **`acq_note` reproduced exactly** ($8,463M FY2022-26) and extended: $21.9bn of acquisitions since FY2012, $6.4bn of
  goodwill written off, Cordis bought for $1.9bn and sold for $923M.
- **SBC resolves and is complete**, but half of it is new: $245M of the FY2026 $367M is The Specialty Alliance's own
  unit plan for physicians, $407M more unrecognised; the managers' pay metrics exclude it.

### What the rebuild found
- **Owner earnings depend on one construction choice more than on (c) or the window**: five-year $2.52-2.72bn with
  operating cash as filed, $1.12-1.32bn with the three trade working-capital lines stripped; fifteen-year $1.80-2.08bn
  and $1.23-1.51bn. The screen, `run.py` and every published band are the first construction. For a negative
  working-capital distributor, half the recent "owner earnings" is the growth of the suppliers' credit.
- Named death as a signature only: **#6 THE BORROWED BALANCE SHEET** (NEGG's supplier-credit pendulum, at the scale of
  a $254bn distributor), with #11 and #10 as features. Not entered in the index's instances column (closed at Q2).

### Tooling defects (reported, not patched)
- `working_capital_flag()` wrong-signed a second time (see above); a sign check on total working capital would stop it.
- The screen band's two ends come from different windows again (5y D&A bottom, 3y capex-plus-finance-lease top).
- `run.py`'s D&A rule overrides a filed total with a larger component sum (FY2024: $470M + $264M = $734M against a filed
  $710M), contrary to its own comment; conservative direction, small.
- No published construction strips trade working capital; every distributor on negative working capital is
  overstated by it on the recent windows.
- `sources.cik_for()` 404 on OMI (Owens & Minor).
