
## UPDATE 2026-09-26 - SXC: Q2 OUT. SunCoke makes blast-furnace coke for two steelmakers under take-or-pay contracts priced as the customer's coal cost plus a fixed fee its own 10-K says is meant to earn "an adequate return on invested capital"; the market is, in its own words, "highly competitive", the fee has been cut at renewal and has lost 42% in real terms since 2012, and the business earned 6.2% before tax on its capital over fourteen years. Steady, and a toll processor, not a franchise.

**SunCoke Energy, Inc. (SXC), wave 7 name 51, register entry 193.** Run file `Test Runs/2026-09-26 Run - SXC SunCoke Energy.md`.
CIK 0001514705, fiscal year to 31 December. Price $9.57 (NYSE close 2026-09-25, aggregator, flagged) x 84,874,850 shares
(10-Q cover at 2026-07-24, `0001514705-26-000034`, outstanding; equals issued less treasury) = cap $812.3M; sovereign
5.49% (US Treasury, 30 Yr, 09/25/2026). **Q1 IN, Q2 OUT on the business.** One unattended session ran the whole file,
from the claim to the fold.

### The finding
- **[E3-03] criterion (2) fails in the registrant's own words**: *"The cokemaking market is highly competitive.
  Competitors include merchant coke producers as well as the cokemaking facilities owned and operated by blast furnace
  steel companies"*; *"coke quality and price"* are the competitive factors; Item 1A names coke substitutes, imports and
  the electric arc furnace.
- **The price is a regime, not a product's [E2-59]**: coal passed through (*"The customer can generally exercise an
  overriding vote on most coal procurement decisions"*), operating costs indexed or budgeted, and *"The fixed fee is
  intended to provide an adequate return on invested capital"*, fixed for the contract's term. At renewal it moves the
  customer's way: Granite City's extension *"results in significantly lower overall economics"*; Algoma walked away in
  2025 and Haverhill I closed.
- **[E3-43]'s demonstration is absent over fourteen filed years**: 6.2% pre-tax on net capital (8.3% before impairments),
  3.5% on equity; Domestic Coke Adjusted EBITDA per ton $57.38 in 2012, $58.27 in 2024, $46.35 in 2025, **−42% in real
  terms**. The operating margin was 5.4-5.6% through every steel cycle, steady and low, while the coal suppliers earned
  28-36% in 2021-2023: the chain's gains went to whoever held the scarce thing that year.

### Refuted or corrected priors
- **The brief's `tools/run.py` "wrong sign" defect is a misdiagnosis, and the earlier folds that reported it (MATX, PPG,
  LNN, SYY, MLI, CMT, WSM) should be read with this.** `implied_growth()` and `points_over()` fade into a **2.5% perpetual
  terminal growth rate** that the output never prints, and `points_over()` assumes **3% year-one growth**. The printed
  numbers are consistent with that engine; the defect is that the tool adds a growth number, which the protocol's tooling
  test forbids. Not patched.
- **Take-or-pay steadiness is not [E3-43]'s evidence.** The strongest fact for SunCoke (a 5.4-5.6% margin through busts in
  which its largest customer's aggregate operating margin was −26.6%) is the contract's floor, the same escape [E2-59]
  describes for administered prices, and the renewal is where it is re-set.
- **The screen's `acq_note` was right and its `deal_note` empty was right**: SunCoke was the buyer of Phoenix Global
  ($271.5M net of cash, closed 2025-08-01); nothing is live.

### Beneath the close
- **Owner earnings, every window 3 to 15 years, both ends, both NCI treatments: $29.0M to $96.5M (3.57-11.88%).** The
  width is the (c) judgment, not the window: capex ran at 0.73 times depreciation over 2012-2025, so here the D&A end is
  the conservative one, and the aging ovens (Jewell 1962, Indiana Harbor 1998) keep the question open. The screen's $33M and
  $104M reproduce on its basis, which omits the non-controlling interest (Indiana Harbor's 14.8%; the Partnership's public
  unitholders in 2013-2019) and finance-lease principal. **COMPUTATION - NOT A CLEARANCE**: about $3.40-11.40 a share at
  the ~10% floor and $6.20-20.70 at the sovereign, against $9.57, the price inside the range [E4-25].
- **Q3 prompts**: [E4-29] fires in the 10-K itself (Adjusted EBITDA is the MD&A's first table, the per-ton metric, the
  guidance and 70% of the bonus); 2025 free cash flow was guided at $100-115M and came in at $40M [E4-22, E3-48]; the
  2023 PSU payout excluded the Algoma default [E2-57]; 2025 and TTM dividends exceeded owner earnings in a year of rising
  debt [E2-60]; interest coverage out of cash net of capex 2.1 times in 2025 and 1.45 in the TTM [E2-54].
- **Signature, not a Q4 death: #11 THE PASS-THROUGH, with #14 THE PATRON's regime-withdrawal as a feature.** No alert,
  no PORTFOLIO row.

**Next in the order file: HII.**
