
## UPDATE 2026-09-19 - HBB: Q2 OUT, the trusted brand whose buyers can buy the same appliance from the same factory, and whose price follows its cost
`Test Runs/2026-09-19 Run - HBB Hamilton Beach Brands.md`. **Q1 IN; Q2 OUT on the business, file closed; Q3 recorded (a GATE case on daily execution; IN on the
binary with flags); Q4 recorded (IN: owner earnings positive on the five-year default); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing armed.**
Price **US$31.64** (2026-09-18 close, aggregator flagged, matched by the issuer's own monthly repurchase prices in three months) x **13,442,332** (Class A 9,858,179 +
Class B 3,584,153, the Q2 2026 10-Q cover, `0001709164-26-000160`, added one for one on identical dividend and liquidation rights) = cap **US$425.3M**; sovereign
**USD 30-year 5.34%** (US Treasury, 09/18/2026). **The first of wave 5's "cap rejected as a broken input" names. Register count at the fold, read from the register:
114 runs** (HBB adds one Q2 OUT).

### THE PRIOR THE BRIEF ASKED TO BE ARGUED AGAINST, AND HOW IT FARED
The brief named its own likeliest error: that a small, low-multiple, family-controlled appliance company is the kind of name a framework built on Berkshire's corpus
would look kindly on. **It was wrong, and the filings refute it at Q2, before the family or the multiple is reached.** The family (81.0% of the vote), a long-lived
brand and a ROTCE-based pay plan are real; none of them makes a buyer unable to find a substitute, and the filer says in its own risk factors that the buyer can.

### WHY Q2 CLOSED, ON FOUR INDEPENDENT RECORDS
- **The filer's own Item 1A**: the industry *"does not have substantial entry barriers"*; customers are *"sourcing, or expanding the extent of sourcing ... directly from
  manufacturers in Asia"*; *"we compete with our retail customers, who use their own private label brands"*; retailers *"have a large selection of ... suppliers from which
  to choose"*. Walmart 29%, Amazon 19%, top five 62%, all on purchase orders.
- **The price line follows the cost line, both ways [E2-44, E3-43, E3-62]**: the revenue bridge in every 10-K FY2019-25 shows +$42.9M of price in 2022 that did not restore
  the margin, then **-$28.1M (2023) and -$30.6M (2024), *"lower average selling prices reflecting lower costs"***. The savings went to the buyer the year they appeared.
- **Units and rank [E4-55, E4-32]**: revenue $603.7M (FY2020) to $606.9M (FY2025), flat nominal; *"#1 small kitchen appliance brand ... based on units sold"* (FY2020-23) to
  *"#1 ... national brand"* (FY2024) to *"#2 ... national brand ... and grew to #4 by dollars sold"* (FY2025); Amazon's buying -23.6% in 2025.
- **The row** (SN, SPB HPC segment, NWL H&CS segment, LCUT as a channel peer; De'Longhi, SEB, Donlim foreign; Conair, Sensio, Versuni, Gourmia private; private label
  unsegmented): HBB is **better run than Spectrum's and Newell's appliance segments and than Lifetime** (5.8% five-year operating margin against segment margins of
  -17.3% to 3.7% and a 3.5% five-year average), and **not the leader**: SharkNinja's kitchen categories alone are $3,367.1M, growing about 27% a year on a 49.0% gross
  margin, taking share from both sides. Spectrum is divesting its segment. **A competent operator in a category with no moat is [E2-37]'s remarkable textile company.**

### THE SKIP REASON, FROM THE FILED RECORD
- **The label was right: the cap really was broken, in two layers.** (1) A per-class dimensioned cover, the META/PATH/PUBM kind, two classes, no empty class, so
  companyfacts carries only `EntityPublicFloat`. (2) The undimensioned `us-gaap:CommonStockSharesOutstanding` carries **100 shares at 2017-06-30**, the pre-spin
  NACCO-subsidiary capitalisation, and zeros after. **$27,000,200 / (100 x $31.605) reproduces the 854,301%.** The code that wrote the triage row is not on disk; the
  current `shares_outstanding()` refuses the stale fact (550 days), but `Backtests/scripts/bt17_microcap.py` `shares_asof()` does not and returns exactly 100 for HBB.
- **Unlike PATH and BZFD, the `a8bc84f` owner earnings were positive at every end**, so the count was the only thing that kept HBB unpriced.

### WHAT CHANGED WHAT THE QUOTE MEANS
- **$36.5M of IEEPA tariff refunds in Q2 2026** (after the Supreme Court's ruling of 2026-02-20 that IEEPA does not authorise tariffs), booked in cost of sales under a gain
  contingency model and called *"non-recurring"* by the filer. The price went from $23.87 on 2026-08-05 to $31.42 two sessions later and to a two-year high of $34.00 on
  08-17. **A twelve-month yield at face value is 21.7%; without the refund 13.1%; on the five-year default 6.4%.** [E4-41] removes it.

### Q3 FINDINGS WORTH KEEPING (recorded, not governing)
- **The 2020 Mexican-subsidiary restatement** (FY2017-19; *"certain former employees"*; two material weaknesses, one in the income-tax process; remediated by FY2021;
  a $10.0M insurance recovery in 2022 that sits inside FY2022 operating profit and inside the 2022 guidance test). [E4-22]'s first flag, fired and remediated.
- **[E4-29] clean in all 28 releases (no EBITDA), and the adjustment lives in the proxy instead**: the 2025 short-term plan paid on operating profit of $47,327,405 against
  $36,579K reported [E2-57, E4-27]. Mitigated by a ROTCE override (up to -40%) and Class A stock restricted for 10 years; ROTCE carries 30-33% of both plans, [E2-01]'s
  own yardstick. **A run that reads only the 10-K and the releases scores this company clean on adjusted earnings; the pay table is where the except-for is.**
- **Guidance against outturn [E3-48]**: three of eight directional calls FY2022-25 hit. **[E2-49] fired mildly** on the rank's changing basis (the "national brand"
  qualifier arrived the year before the fall). Tally: nine fires (SHOP, MRVL, PAY, ARM, CALX, BE, PUBM, BZFD, HBB) and six failures.
- **Candor [E2-26, E2-69]**: both of the filer's own adjustments (the 2022 recovery, the 2026 refund) remove a favourable item. The General Counsel left "effective
  immediately" on 2026-06-18 after fifteen months with no reason given: a prompt for the next 10-Q, not a finding.

### Q4 AND (c)
- **Owner earnings**: **$27.0-27.3M five-year (FY2021-25)**, $45.7-47.6M three-year, $13.2-13.5M seven-year, $55.7M twelve months without the refund. The spread is working
  capital in named years (2020's pandemic and ERP inventory build, 2022's supply-chain build, 2023's release, the supplier-finance programme) that nets out over five:
  the five-year mean matches after-tax operating profit ($27.5M). (c) is the D&A default [E3-44]; capex $2.3-3.4M a year; the band is $0.3M wide.
- **Good, not great**: about 20% pre-tax on roughly $185M of capital employed, flat; ROE 41% (2020) to 15% (2025) as retained cash paid down the revolver.
- **Named death**: a large customer moves a category to its own label or buys direct, while a tariff or freight shock goes unpassed. Walmart is $178.3M; losing it at a
  25.7% gross margin turns a $36.6M operating profit into about a $9M loss. **A later instance of shape #19 THE SHELF as the mechanism, with #11 THE PASS-THROUGH as a
  feature** (index updated); no new shape.

### REVERSAL CONDITION, IN WORDS (fold step 4; nothing armed, no PORTFOLIO row)
Reopen Q2 only if the revenue bridge shows a positive price contribution in a year of falling costs in three years of four; the unit rank returns to #1 on an unchanged
basis and the dollar rank rises, for two 10-Ks; gross margin holds above 26% excluding windfalls for three years with Walmart's and Amazon's shares held; the
no-entry-barriers sentence is withdrawn with a reason; and revenue grows at least as fast as SharkNinja's kitchen categories for three years.

### FOR THE OPERATOR
- **`Backtests/scripts/bt17_microcap.py` `shares_asof()` has no staleness test** and returns a nine-year-old pre-spin share fact (100) for HBB. Whether any backtest
  panel priced a spin-off registrant on such a fact has not been tested. Recorded, not changed (tooling is not this run's to alter).
- **`tools/sources.sovereign()` was current this time** (09/18, 5.34%), after eleven stale readings recorded by earlier runs.
- **Seven defects in the brief** are listed in the register entry and the run file; the largest is that the triage history says the count "did not resolve" when it
  resolved to 100, and that the priors omitted the tariff refunds that doubled the price.

### ONE THING TO KEEP
**When a filer publishes its own revenue bridge, read the price line against the cost line before reading any rank or margin.** Hamilton Beach's bridge answered the
franchise question in two rows: when costs fell in 2023 and 2024, $58.7M of price went back to the buyer the same year. A moat keeps the saving; a supplier returns it.
