## COMPUTATION, NOT A CLEARANCE (Q7's arithmetic after the Q2 STOP, at the owner's request; operator rule 3)
Nothing in this section is a verdict or entry language. The file is closed at Q2.

**Owner cash, recast from the filed statements** (`q7.py`, output in `q7_output.txt`; $M). For a lessor the cash-flow statement
splits fleet turnover in two: "Portfolio investments and capital additions" (cars, engines and containers bought, including
businesses and affiliates) and "Portfolio proceeds" plus "Proceeds from sales of other assets" (cars and other assets sold),
while operating cash has the gains on those sales taken out. Three cases:
- **Maintenance case (central, spec (e))**: operating cash less stock pay, less depreciation, plus net gains on disposal, less
  deferred income taxes. CONVENTION of this run: the maintenance outlay is depreciation net of the gain realised when used cars
  are sold; rationale: a fleet held level must buy back each year its depreciation plus the book value of the cars it sells,
  and the sale proceeds return that book value with the gain, so the net cost is depreciation less the gain. Depreciation is
  taken as the proxy the rows allow in most companies **[M1998-127]**; the rows also warn that in heavy-capital businesses it
  can fall short of what keeps the business in place **[L2015-004]**, **[M2016-092]**, and the filing allows no better guess,
  so the case flatters rather than understates. CONVENTION of this run: deferred taxes are charged as if paid, because they
  are deferred only while the fleet grows, and the case assumes it does not; the rows decline to treat deferred taxes as
  "a hidden form of equity" **[M2015-030]**.
- **All-spending case (beside)**: operating cash less stock pay, less all fleet spending and purchases of previously leased-in
  assets, plus portfolio and other sale proceeds (sale-leaseback proceeds left out as a financing).
- **Before interest (the all-equity basis)**: each case plus interest expense after tax. CONVENTION of this run: the tax on
  the add-back is 37% to 2017 and 24% from 2018 (the federal rate of each period plus state; the filed effective rates for 2023
  to 2025 were 22.6% to 23.9%); and the 2017 deferred tax line (-260.5, the tax-law remeasurement) is replaced by the mean of
  2016 and 2018 (45.5) so the charge is a normal year's.

| Year | Maint., after interest | Maint., before interest | All-spending, after interest | All-spending, before interest | Fleet spending beyond maintenance |
|---|---|---|---|---|---|
| 2021 | 176.6 | 331.6 | -477.5 | -322.5 | 688.3 |
| 2022 | 234.4 | 397.0 | -435.8 | -273.2 | 706.5 |
| 2023 | 202.6 | 402.8 | -869.9 | -669.7 | 1,110.8 |
| 2024 | 249.7 | 508.9 | -870.2 | -611.0 | 1,165.7 |
| 2025 | 257.6 | 555.1 | -396.8 | -99.3 | 707.6 |
| Mean 2021-2025 | 224.2 | 439.1 | -610.0 | -395.1 | |
| Mean 2014-2023 (cycle, beside) | 186.6 | 318.1 | | -144.5 | |

**The window and the cycle (spec (a)).** The filer does not call 2021 or 2025 a trough or a peak in words; its own index puts
2021 at the end of six years of falling renewal rates and 2025 in the fourth year of rising ones. The literal five-year window
2021 to 2025 is used as the central base, the more generous of the two; the cycle base, 2014 to 2023 (peak to peak of the
filer's LPI renewal-rate change, 38.8% and 33.5%; CONVENTION of this run, since the window spans one rising half only), is
shown beside. Before 2018 the figures include businesses since sold (American Steamship, Portfolio Management's marine
assets).

**Growth, the cap and the growth spending (specs (e) and (f)).** The shown growth of maintenance owner cash before interest,
2021 to 2025, is 13.75% a year; carried ten years it would take owner cash to about 51% of revenue against a highest share in
the filings read of 32.1% (2024), so the growth carried is the business's own revenue growth over the same window, **8.47%**
(the shown rate and the cut both written down, spec (f)). The growth is not free: GATX spent $3,690.6M beyond maintenance in
2022 to 2025 and maintenance owner cash before interest rose $223.5M, a return of **6.06%** after tax on the growth spending
(CONVENTION of this run: the return on growth spending is the rise in owner cash over the window divided by the spending
beyond maintenance in its last four years; rationale: spec (e) charges growth spending against the growth it buys and gives
no measure of the price of that growth; this one is the filer's own record, and it flatters, since part of the rise is the
lease-rate upswing on cars already owned). The growth case charges that spending each year, ten years, then no growth and no
spending.

**Acquisitions and GABX (spec (c)).** Fleet purchases from DB Cargo (2025, 5,882 cars) and the 2020 business purchase ($203.2M)
are inside the fleet spending above (deducted, total growth credited); net purchases of businesses over the window are small
against owner cash, so the serial-acquirer convention does not apply. GABX closed on 2026-01-01, after the window and before
the price date, and is a cash deal by GATX and Brookfield: valued on its own filed record, its financing in today's net debt.
Its record (10-Q 2026 Q2, note on GABX): six months to June 2026, income before taxes $6.1M, interest $80.5M, management fees
paid to GATX $24.9M (eliminated in consolidation). Annualised and taxed at 24%, **$169.5M** a year before interest for 100% of
GABX (CONVENTION of this run: the six-month record annualised; it is the higher of the two filed records, the 2025 pro forma
giving $128.2M). Because 100% of GABX's cash is counted, Brookfield's 66.5% is a claim ahead of GATX's shareholders: the
non-controlling interest at book, **$805.5M**, is added to net debt (CONVENTION of this run; rationale: the all-equity basis
counts market value plus net debt, and a consolidated joint venture's minority owner is paid before GATX's owners on the
cash counted). The 8-K/A's pro forma combined statements show GABX adding $0.6M to GATX's 2025 net income.

**Net debt** at the latest filed date, 2026-06-30 (10-Q): debt $12,333.3M less cash $747.1M and restricted cash $0.1M =
**$11,586.1M**; operating lease obligations ($143.8M) left out, as the convention says. No later filing states a subsequent
event that changes it. Enterprise value at the price: $5,820M + $11,586.1M + $805.5M = **$18,212M**.

**The range, all-equity basis (central), discounted at the sovereign 5.43%, ten years then zero growth:**

| Case | Owner cash before interest, incl. GABX | Whole business | Per share, less net debt and minority |
|---|---|---|---|
| No growth, window base | 608.6 | 11,208 | **-$33.54** |
| Growth 8.47%, spending charged at 6.06%, window base | 608.6 rising | 12,825 | **$12.28** |
| No growth, cycle base (beside) | 487.6 | 8,979 | -$96.65 |
| Growth, cycle base (beside) | 487.6 rising | 10,275 | -$59.94 |
| All-spending, window base, no growth (beside) | -225.6 | negative | -$468.69 |

**VALUE RANGE (reporting figure): -$33.54 to $12.28 a share, all-equity basis, against $164.85.** The literal window and the
cycle base are both shown above. The floor is tested first: at the price, the no-growth case returns 3.34% on enterprise value
(608.6 on 18,212) and the growth case 4.38% (the rate that equates it to enterprise value); on the cycle base, 2.68% and 3.79%.
**No case earns the floor of about ten percent; the close under Q7 would be OUT** **[M2003-149]**, whatever the width, and a
price above the top of the range closes OUT by the same convention. The width test does not arise; with a negative bottom the
ratio has no meaning.

**FAIR PRICE (reporting figure, Part VII; after the company's own tax, no conversion): -$212.97 a share on the all-equity
basis (central)**: each end case valued at ten percent instead of the sovereign (no growth -$178.61, growth -$247.32; growth
lowers value at ten percent because the growth spending earns 6.06%), averaged. Read plainly: at the floor of ten percent,
the window's owner cash before interest is worth less than the net debt and the minority's claim, so there is no positive
price at which the midpoint earns the floor. On the cycle base the figure is -$240.41.

**Equity-only basis, beside, never deciding alone:** owner cash after interest, window mean 224.2 plus GATX's after-interest
share of GABX (33.5% of its net income and the fees borne by Brookfield's 66.5%, after tax) 26.3 = 250.5, a 4.30% yield on the
market value of $5,820M. No growth: $130.66 a share at 5.43%, $70.95 at ten percent. Growth: $223.05 at 5.43%, $100.74 at ten
percent, where the equity pays only 11.4% of the growth spending because 88.6% of the net fleet investment of 2022 to 2025 was
matched by new net debt (net debt excluding GABX rose from $5,562M to $8,832M), which makes the equity's return on its share
of the spending 19.3%. **Fair price, equity-only: $85.85 a share.** This is the per-share magnification of a debt-financed
business that the all-equity basis exists to refuse **[L2017-004]**; and the window's after-interest mean understates today's
interest (expense $204.0M in 2021, $391.5M in 2025), so it flatters as well.

**The literal three-year window of `tools/run.py`** (2021 to 2023, capex basis -846.1, depreciation basis 123.6) is not used:
its capex column omits portfolio proceeds and its depreciation column omits the gains, as said in Step 0.

---
## THE BOX
**OUT at Q2** (Rail North America, the deciding part: a standing castle that protects only ordinary returns). COMPUTATION
beside the price: all-equity range -$33.54 to $12.28 a share against $164.85; no case earns the floor (3.3% to 4.4% on
enterprise value); fair price -$212.97 all-equity ($85.85 equity-only).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Bearing on Q3 (capital).** GATX must keep buying cars: purchase commitments of $1,643.7M for 2026 to 2030, mainly railcars,
including the Trinity agreement for 15,000 cars through 2028, of which 8,133 were ordered and 5,720 delivered by 2025-12-31
(10-K 2025). Fleet spending beyond maintenance was $3,690.6M in 2022 to 2025 against a $223.5M rise in maintenance owner cash
before interest (6.06% after tax). Pre-tax return on all capital 5.2% to 9.0% in 2013 to 2025 (`returns.py`). The 2026 year to
date investment volume was $4.7B including GABX (Q2 release).

**Bearing on Q4 (the accounts; the balance sheets 2016 to 2025, `run_py_output.txt` checked against the filed statements).**
Total assets rose from $7,105M to $18,000M; GATX equity from $1,347M to $2,750M, of which retained earnings $1,828M to $3,451M;
long-term debt from $4,286M to $12,506M (2025 includes the $2,959M GABX loan, with $4,241.9M of restricted cash held for the
purchase); goodwill small throughout ($78M to $144M; $123.4M at 2026-06-30); receivables small against a lease book. The
deferred income tax liability was $1,195.7M at 2025-12-31. Equity-method affiliates (the Rolls-Royce joint ventures) earned
$117.3M after tax in 2025 and paid $50.0M in dividends; operating cash counts the dividends, as the framework's equity-method
convention asks. The 10-K carries a "Non-GAAP Financial Measures" section; the second-quarter release leads with GAAP net income
per share. No figure was found that confused; the accounts read plainly.

**Bearing on Q5 (people; recorded, not judged).** GATX publishes a full-year earnings estimate per diluted share and raised it
on 2026-07-30 to $9.90 to $10.30 (8-K `0000040211-26-000073`); the rows on guidance and on hitting the number (**[L2019-006]**
among the Q5 tests) would read it there. The proxy was cached and not read. Integrity facts: none found beyond this habit; the
box line does not carry the integrity flag, since no fact bearing on honesty was found.

**Bearing on Q6 (money and owners).** Buybacks name no price: $65.0M for 416,699 shares in 2025 (about $156 a share) and $21.9M
for 167,452 in 2024 (about $131); treasury stock rose by 272,981 shares and $51.4M in the first half of 2026 (about $188, which
may include shares withheld for tax; not separated). All sit above the bottom of the all-equity range computed above
(-$33.54), and above its top. A new $300M programme was approved on 2026-02-18 with no price stated (10-K 2025, Item 5). Diluted
shares fell from 47.6M (2012) to 35.9M (2025). Dividends paid every quarter since 1919 (Q2 release). The GABX structure gives
GATX annual call options toward 100%; the first was exercised on 2026-06-30 for $66.2M, taking it to 33.5%.

**Bearing on Q9 (debt and exposures).** Consolidated debt $12,333.3M at 2026-06-30 against GATX shareholders' equity of
$2,784.4M; the filer's "recourse leverage" (debt and lease obligations net of cash, over total equity including the minority)
was 3.3 at 2025-12-31. Maturities: $653M (2026), $855M, $825M, $907M, $3,660M (2030) and $5,605M thereafter; weighted remaining
term 8.2 years at 4.78%. GATX guarantees the whole GABX term loan ($2,959M at 2025-12-31, $2,860.2M at 2026-06-30) while owning
33.5%; the GABX loan carries an asset-coverage covenant (a ratio not to exceed 0.85 to 1.0). Some derivative contracts "could
require us to make immediate payment on net liability positions in the event that we default on certain outstanding debt
obligations" (10-Q 2026 Q2). The filer relies "largely on the capital markets and banks to fund our operations" and names
ratings as the gate to that funding (10-K 2025, Item 1A); this is what the rows ask of a borrower that must refinance
**[L2010-020]**, **[L2014-023]**. Pre-tax earnings including affiliates before interest covered interest about 2.1 times in
2025 ((436.1 + 391.5) / 391.5). Exposures: the owner of a leased hazardous-materials car may be liable for a spill "without regard
to the owner’s fault" (10-K 2025, Note 24); Norfolk Southern's third-party claims against GATX over the East Palestine derailment
were dismissed in 2024 and the other East Palestine litigation against GATX is resolved; subsidiaries face asbestos claims; the
litigation accrual was $4.6M.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the first analyst, commit `0c41b965`); written question by question;
      committed after each by pathspec: Q1 `12093a2c`, Q2 `f2f35b2c`, and the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is held by the dispatching session (not checked
      here; this analyst wrote no lock); the fold into the register is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what the session context showed by
      accident is declared under contamination at the top and was not used.
- [x] Every v5 id resolves (`check_ids.py`: no E-ids, every M/L/R id in `principle_ledger_v5.csv`, every quoted fragment beside
      an id found in that row); every filing fact carries its document and accession; numbers not from a filing are labelled
      CONVENTION of this run.
- [x] The order was kept; Q2's STOP closed the run; everything after it is NOT REACHED or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, depreciation, deferred taxes charged), never a net-income proxy; the
      sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, and the warnings under the competitor row); facts for later
      questions under AFTER THE STOP; no integrity flag, since none was found.
- [x] No point-in-time anchor; every row cited is from the v5 ledger, none dated after today.
- [x] Only the arithmetic lines of `tools/run.py` were used, and those not used are named with the reason.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Honest limits: the competitor comparison uses three different definitions of capital (stated in the table); Trinity's
  2015 to 2018 leasing assets were not extracted, so its cycle coverage is four years, not thirteen; First Citizens' rail
  figures exist only from 2022 under that owner; GABX's record is six months; the proxy was not read (the file closed before
  Q5); the price is one aggregator quote.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Maintenance capital for a lessor.** Q7's specific (e) puts the maintenance case at the centre "where the filing allows
the guess", but a lessor's fleet turnover runs through two investing lines (purchases and portfolio proceeds) and the gains on
sale are taken out of operating cash; nothing says how proceeds and gains sit against maintenance. `tools/run.py` omits both,
and its two bases come out at -846.1 and 123.6 for the same years. I used depreciation net of the gain on sale, as a CONVENTION
of this run. (2) **The price of growth.** Spec (e) charges growth spending "against the growth it buys" and spec (f) caps the
rate, but neither says how to measure what a dollar of growth spending buys; I used the filer's own record over the window,
which flatters in an upswing. (3) **A consolidated joint venture with a minority owner.** The all-equity basis is "market value
plus net debt"; a consolidated 33.5%-owned joint venture puts 100% of its debt and cash in the statements and a minority claim
ahead of the shareholders, which the text does not mention; I added the minority interest at book to the claims. (4) **Deferred
taxes in a growing lessor.** The text does not say whether owner cash should charge deferred taxes that are deferred only while
the fleet grows; I charged them in the no-growth case, on **[M2015-030]**. (5) **The lender-funded lessor at Q1.** The bank
door and the finance-company row **[M2002-094]** sit in Q1, but the framework routes only banks and derivatives books; a
lessor with a readable asset side and wholesale term funding is not named, and I had to choose between Q1 TOO HARD on the
funding doubt and carrying it to Q2 and Q9 (I carried it). (6) **"Ordinary" returns.** Q2's convention judges them in words
with no benchmark; I set GATX's pre-tax return on capital against its own cost of debt and the long bond, which is my reading,
not the text's.
