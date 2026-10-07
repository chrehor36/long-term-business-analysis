# -*- coding: utf-8 -*-
import re
p = "Test Runs/2026-09-20 Run - SIG Signet Jewelers.md"
s = open(p, encoding="utf-8").read()

i = s.index("## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?")
head = s[:i]

rest = """## Q3 ITEMS — NO VERDICT IS WRITTEN; THE GATE IS CLOSED AT Q2 **[E2-01, E4-22, E4-29, E2-49, E4-30, E5-08, E5-24, E2-51, E3-53, E2-26]**
*Full standard, unused because no verdict is drawn: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

Recorded because the run read the filings and the findings are owed to the register, and
because the standing instruction since the CGNX run requires the **8-K EX-99.1 earnings
release** to be read before any Q3 scoring. **No verdict is drawn, and nothing here promotes
or rescues anything [E2-37, E3-39]** — *"a good managerial record … is far more a function of
what business boat you get into than it is of how effectively you row."*

**THE WEIGHT CASE, DECLARED ANYWAY.**
- **Daily execution — TICKED.** The corpus's own named example of the have-to-stay-smart class
  is this industry: *"retailing is a good case of a business where you have to stay smart …
  you cannot coast in retailing"* **[E3-74]**. Position has to be re-won at every assortment
  reset and every lease renewal, which puts Signet on **[E3-43]**'s *"a business, unlike a
  franchise, can be killed by poor management"* side of the line.
- **Control — no.** A marketable minority interest, exitable.
- **Leverage — no, and emphatically so.** **Zero debt** at 2026-08-01, $526.8M of cash, and a
  $1.2 billion asset-based revolver undrawn and extended to August 2029. The Senior Notes were
  repaid at maturity in Fiscal 2025 and the Series A convertible preferred was bought back for
  $813.8M in the same year.
- **One of three ticked → had the run reached Q3, it would have been a BINARY GATE and no price
  would compensate [E1-16, E3-29, E5-35].**

**THE FIFTH FLAG FIRES, AND IT FIRES IN BOTH DOCUMENTS [E4-29].** *"Trumpeting EBITDA … is a
particularly pernicious practice. Doing so implies that depreciation is not truly an expense,
given that it is a 'non-cash' charge. That's nonsense."*
- The Fiscal 2026 10-K's non-GAAP section carries **six** measures, of which three are earnings
  before something: **EBITDA ($539.8M), Adjusted EBITDA ($687.2M) and Adjusted EBITDAR
  ($1,116.2M)** — against **GAAP operating income of $393.1M**. The ladder is worth reading
  slowly: Adjusted EBITDA is 75% above operating income, and **Adjusted EBITDAR gets there by
  also adding back $429.0 million of rent**. For a company whose entire operating structure is
  **2,582 leased stores**, EBITDAR deletes the two largest real costs of being in business at
  all — the depreciation of the fit-out and the rent on the box. **[E5-41]** names exactly what
  is being deleted: *"Depreciation is where you spend the money first … and record the expense
  later. And it's reverse float"* — the worst kind of expense, already paid.
- **The EX-99.1 of 2026-09-09 (accession `0000832988-26-000227`) goes further and is the reason
  the CGNX rule exists.** Every forward number the company gives is non-GAAP: third-quarter
  **"Adjusted operating income $31 to $48 million"** and **"Adjusted EBITDA $82 to $100
  million"**; full-year **"Adjusted operating income $535 to $605 million"**, **"Adjusted EBITDA
  $730 to $800 million"**, **"Adjusted diluted EPS $10.45 to $12.15"**. **No GAAP forecast is
  given at all**, under the standard formula: *"we cannot provide forecasted GAAP operating
  income or the probable significance of such items without unreasonable efforts."* The item
  excluded to make that true is *"restructuring and reorganizational charges or asset
  impairments"* — which this company recorded at **$9.1M, $372.0M and $91.6M** in the last three
  fiscal years and in **ten of the eighteen filed years**.

**THE THIRD FLAG FIRES WITH IT [E4-22, E3-48, E5-30].** The release is headed **"Raises Fiscal
2027 Guidance"**, and the CFO is quoted: *"We are raising our full year adjusted EPS guidance by
over 10%."* **[E5-30]** is the reason this is not a small thing: *"once you start it, it's all
over. You can't quit … And forecasting earnings, I can't imagine anything more destructive."*
**[E3-48]**'s action — set past guidance against outturn — **is named as an open work order
below and was not performed, because the gate is closed.**

**[E2-49] METRIC-SWITCHING: IT FIRES. This is the seventh fire against five failures.** The
framework's operational form is *"compare the headline metric across successive filings; a
switch that follows deterioration fires."* Run across four annual reports:

| filing | the numbered non-GAAP measures | GAAP operating income that year |
|---|---|---|
| **FY2023 10-K** (`0000832988-23-000032`) | net cash · free cash flow · **non-GAAP** operating income · **non-GAAP** diluted EPS · leverage ratios. **EBITDA appears only inside the leverage-ratio definition.** | $604.9M |
| **FY2024 10-K** (`0000832988-24-000083`) | identical five. **EBITDA still only inside the leverage ratio.** | $621.5M |
| **FY2025 10-K** (`0000832988-25-000018`) | net cash · free cash flow · **"EBITDA, adjusted EBITDA and adjusted EBITDAR" promoted to its own numbered headline section** · "**adjusted**" operating income (renamed from "non-GAAP") · adjusted diluted EPS · leverage ratios | **$110.7M, down 82%** |
| **FY2026 10-K** (`0000832988-26-000055`) | the same six, and Adjusted EBITDA is now a **guided** metric in the quarterly release | $393.1M |

  **The yardstick was not discarded; a more flattering one was added, in the year the reported
  one collapsed by 82%.** **[E2-49]** is written about disposal — *"most managers favor
  disposition of the yardstick rather than disposition of the manager"* — and the demand it
  makes is for *"pre-set, long-lived and small bullseyes."* A measure introduced as a headline
  in the worst year of the decade is the opposite of pre-set, and the framework's candor case
  (a switch *announced ahead with reasons*, as Berkshire's own 1982 switch was) is not what
  happened here. **Prior updated: [E2-49] now stands at seven fires and five failures.**

**[E4-30] DOES NOT FIRE, AND THE REASON IS WORTH RECORDING.** The two tells are reported growth
engineered to be **unnaturally smooth**, and **cash taxes falling as a share of reported pretax
income**. Neither is present.
- **Smoothness: the opposite.** Reported net income across the eighteen filed years runs
  −$402.6M, $157.1M, $200.4M, $324.4M, $359.9M, $368.0M, $381.3M, $467.9M, $543.2M, $519.3M,
  −$657.4M, $105.5M, −$15.2M, $769.9M, $376.7M, $810.4M, $61.2M, $294.4M. A filer smoothing its
  numbers does not print two years of nine-figure losses and a 1,224% one-year swing.
- **Cash taxes as a share of pretax income: volatile, with a disclosed cause, not a downtrend.**
  FY2016 27.4%, FY2017 14.6%, FY2018 23.2%, FY2020 4.4%, FY2022 13.6%, FY2023 16.5%, **FY2024
  2.0%**, **FY2025 93.0%**, FY2026 19.5% *(cash taxes paid ÷ income before income taxes, both
  from the filed statements; Fiscal 2019 and Fiscal 2021 are not meaningful because pretax
  income was negative)*. The FY2024 low has a named cause in the 10-K: Bermuda enacted a 15%
  corporate income tax effective for Signet in Fiscal 2026, and the economic transition
  adjustment let the company book **"a $263.3 million deferred tax asset in the fourth quarter
  of Fiscal 2024"** — disclosed, quantified, and the same note volunteers that OECD Pillar Two
  guidance **"would limit the cash benefit … to … approximately $52.7 million."* Volunteering
  the limitation on your own tax asset is a **[E2-26]** candor point, not a flag.

**THE PRIMARY TEST [E2-01, E2-43, E2-73], RECORDED AS A SERIES, NOT SCORED.** *"The primary
test of managerial economic performance is the achievement of a high earnings rate on equity
capital employed … and not the achievement of consistent gains in earnings per share."*
Book equity is unusable here — **$2,093.4M of treasury stock sits against $1,835.6M of equity**,
so return on book equity measures the buyback, not the business, and **[E2-73]** says the
denominator is what the manager has to work with. On operating income ÷ (total assets − cash −
goodwill − intangibles − current liabilities): **FY2023 29.6% · FY2024 27.0% · FY2025 4.4% ·
FY2026 15.9%.** On reported net income ÷ book equity: 23.9% · 37.4% · 3.3% · 15.0%, with the
FY2024 figure inflated by a **$170.6 million net tax benefit** rather than by operations.

**THE CAPITAL-ALLOCATION RECORD, TRANSCRIBED [E2-56, E5-24, E2-51, E3-53, E5-33].** Two filed
series, both from `companyfacts` cross-read against the cash-flow statements:
- **Acquisitions:** $331.8M (FY2018, R2Net/James Allen) · **$515.8M (FY2022, Diamonds Direct and
  Rocksbox)** · **$391.8M (FY2023, Blue Nile)** · $6.0M (FY2024). **The screen's `acq_note` of
  $914M is CORRECT** and reconciles to $913.6M of FY2022 + FY2023 + FY2024 cash consideration.
  It is also correct that this sits **inside the five-year owner-earnings window**, so the
  numerator and denominator of any five-year figure are **not the same company**.
- **Impairments of goodwill and indefinite-lived trade names, the same assets:** $516.9M
  (FY2009) · $521.2M + $214.2M (FY2019) · $47.7M (FY2020) · $10.7M + $83.3M (FY2021) · $272.5M +
  $94.0M (FY2025) · $53.6M + $21.0M (FY2026) — **$1,835.1 million written off across the
  eighteen filed years, against $4,664.4 million of cumulative net income over the same
  eighteen years.** Goodwill and intangibles fell from **$1,159.1M at FY2023 to $714.8M at
  FY2026** while no business was sold. **[E3-53]** and **[E5-33]** are the relevant rows: the
  charges are real costs, they belong in the mean, and *"to tell owners year after year, 'Don't
  count this' … is misleading"* — and Signet's adjusted operating income adds impairments back
  in **every one of the last three years**.
- **Buybacks, cumulative from the filed financing lines: $3,679.8 million** since Fiscal 2012,
  including **$1,000.0M in Fiscal 2017, $460.0M in Fiscal 2018 and $485.0M in Fiscal 2019** —
  the three years immediately before the Fiscal 2019 loss of $657.4M — plus $205.2M in Fiscal
  2026 and a further **$125M accelerated repurchase begun 2026-09-11**, with the authorization
  expanded by $385M to $700M on 2026-09-09. **[E5-24]** is the row this record is measured
  against: *"what is smart at one price is dumb at another."* **[E5-08]** condition (1), ample
  funds, is plainly met. **Condition (2), a material discount to conservatively calculated
  intrinsic value, IS NOT SCORED**, because scoring it requires a Q5 verdict this run is
  forbidden to reach, and **[E4-13]**'s humility clause would apply to it in any case.
- **[E2-52] dividends funded by issuance: DOES NOT FIRE.** Dividends of $51.9M in Fiscal 2026
  against **zero share issuance** in every year since Fiscal 2012. **[E5-15] serial share
  issuance: DOES NOT FIRE**, and the record is the opposite.

**THE HALF-OWNER TEST [E2-26], recorded as an observation and not as a finding.** *"the business
facts that we would want to know if our positions were reversed."* The Fiscal 2027 second-quarter
release quotes the CEO on *"high single-digit unit growth at higher price points"*. The
same-day 10-Q MD&A says **"the number of units sold having decreased 8.3% year over year"** in
North America. **Both statements can be true at once** — units at higher price points may well
have grown while the total fell — and no accusation is made. What is recorded is that **the
aggregate unit figure, the one this run found to be the most informative series in the file,
appears only in the 10-Q and never in the release the market reads first.**

**OPEN WORK ORDERS, NONE OF THEM A GATE VERDICT.** (1) **The guidance-versus-outturn table
[E3-48]** — the EX-99.1 series from Fiscal 2025 forward, accessions `0000832988-25-000015`,
`-25-000101`, `-25-000170`, `-25-000228`, `0000832988-26-000050`, `-26-000054`, `-26-000158`,
`-26-000227`; not built, because the gate is closed. (2) **The retention test [E3-54]**, $1 of
market value per $1 retained on a five-year roll — not run, because it needs a point-in-time
market-value series that is not on disk and the run has no verdict to support with it.
(3) **The Comenity/Bread Second Amended and Restated Credit Card Program Agreement** of
2026-09-04, whose **signing bonus** and **profit share** are quantified nowhere in the 8-K; the
document *"will be filed with the Company's next quarterly report on Form 10-Q"*, expected
early December 2026.

---
## Q4 ITEMS — RECORDED, NO VERDICT **[E2-23, E3-44, E5-20, E4-25, E4-41, E5-11, E4-20, E2-54, E3-52]**

**THE [E4-25] REBUILD IS DONE, BECAUSE THE SCREEN'S `spread_caveat` ASKED FOR IT AND THE ANSWER
IS WORTH HAVING EVEN THOUGH THE GATE IS SHUT.** The screen's own caveat reads *"4-construction
width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild
it [E4-25]"*, and `years_filed` is **18**. Method is the framework's confessed convention:
**operating cash flow less share-based compensation less the (c) guess**, never a net-income
proxy (operator rule 5, PRIME RULE 3).

**THE FINDING THE FIVE-YEAR WINDOW CANNOT SEE, AND IT IS LARGE.** Fiscal 2018's operating cash
flow of **$1,940.5 million** is not operating cash flow in any sense a buyer should use. The
Fiscal 2019 10-K's cash-flow statement (accession `0000832988-19-000003`) carries, inside
operating activities, a line reading **"Proceeds from sale of in-house finance receivables"** of
**$952.5 million in Fiscal 2018 and $445.5 million in Fiscal 2019**, beside **"Decrease
(increase) in accounts receivable"** of **$242.1M** and **"Decrease in accounts receivable held
for sale"** of **$27.6M**. Signet sold the prime portion of its customer credit book in the
third quarter of Fiscal 2018 and the non-prime in June 2018, recognising **$167.4 million of
charges** on the second sale. **That is the liquidation of a balance-sheet asset routed through
the operating section, not earnings.** Removing the two explicit proceeds lines takes Fiscal
2018 from $1,940.5M to **$988.0M** and Fiscal 2019 from $697.7M to **$252.2M**; removing the
receivable run-off with them takes them to **$745.9M** and **$206.5M**. **A screen reading
tagged `NetCashProvidedByUsedInOperatingActivities` cannot see this, and neither can any
five-year window, because both years are outside it.**

| window | OE at c = D&A **[E3-44]** | OE at c = total capex | note |
|---|---|---|---|
| **18 years, FY2009–FY2026, as filed** | **$406.4M** | **$409.2M** | |
| **18 years, receivable-sale proceeds removed** | **$390.4M** | **$393.2M** | **the honest long figure** |
| 10 years, FY2017–FY2026, proceeds removed | $546.5M | $561.2M | |
| **5 years, FY2022–FY2026** (the corpus default **[E2-42]**) | **$581.6M** | **$598.7M** | unaffected by the adjustment; both distorted years are outside it |
| 4 years, FY2023–FY2026 (the pandemic year removed, **[E4-41]**) | **$465.0M** | **$477.8M** | |
| 3 years, FY2024–FY2026 | $422.9M | $431.5M | |
| **TTM to 2026-08-01** | **$520.3M** | **$505.8M** | 10-K less H1 FY2026 plus H1 FY2027 |

- **The spread is the range [E4-25], and it is wide: roughly $390M to $600M, a factor of 1.5.**
  **The screen's band was $423M to $599M.** Its **top is right** and its **bottom is 8% too
  high**: the eighteen-year figure the caveat asked for is **$390M**, and the screen could not
  reach it. **The rebuild was owed, it was performed, and it moved the bottom of the band down.**
- **[E4-41] normalize DOWN for luck, applied and named.** Two favourable exogenous breaks sit in
  the record and both are removed in the fourth row above. **Fiscal 2022 is the pandemic
  goods-spending wave**: revenue $5,226.9M → $7,826.0M in one year, **+49.7%**, with operating
  cash flow of $1,257.3M after $1,372.3M the year before on an inventory liquidation. **Fiscal
  2026's gold windfall** is the second and is smaller: the 10-K credits gross margin partly to
  *"accelerating scrap recovery to take advantage of higher gold prices."* **The receivable-sale
  adjustment is NOT an [E4-41] normalization** and is not claimed as one — it is the removal of
  an asset sale wrongly resident in the operating section, which is a different and more basic
  correction.
- **(c) is a DISCLOSED JUDGMENT and it is judged at the capex end [E2-23, E3-44, E5-20].**
  D&A is the corpus default and Signet is **not** in **[E5-20]**'s capital-intensive exception
  class — it is not a railroad, an airline or a utility, and its own D&A of $147.5M and capex of
  $153.5M are within 4% of each other, so the band is narrow either way. **The capex end is
  preferred**, for a reason the filing gives: the company guides **"planned capital expenditures
  of approximately $150 to $180 million"** for Fiscal 2027 against $147.5M of D&A, so renewing a
  2,582-store fit-out costs a little more than the charge. **The guess is disclosed as a guess,
  because Buffett says it must be one.**
- **Working capital:** included, because operating cash flow nets it from one audited line
  (the framework's confessed convention on **[E2-23]** constraint 3). Signet's is severely
  seasonal — **operating cash flow is negative in the first half of every year** (−$73.5M in
  H1 FY2027, −$89.0M in H1 FY2026) and the whole year is made in the fourth quarter, which the
  10-K puts at **"approximately 35 - 40% of annual sales."**
- **SBC subtracted in full [E5-06], and the [E3-70] limit stated:** $26.9M in Fiscal 2026 is
  **4.0% of operating cash flow**, far below the 50% threshold at which the resume state says
  a run must read the grant table by hand. The reported charge is used and is the floor of the
  correct subtraction, not necessarily its measure.

**GREAT, GOOD OR GRUESOME [E4-20, E4-43] — recorded, not scored. GOOD, and shrinking.** Not
great: the return is not rising and the moat is not widening. Not gruesome: this is emphatically
**not** the business that *"grows rapidly, requires significant capital to engender the growth,
and then earns little or no money"* — it does not grow, it consumes **$153.5M of capex against
$678.8M of operating cash**, and it returns the difference. **[E4-43]** says the good class
passes Q4 and ranks below great at Q5, and that is where it would have sat.

**STAYING POWER — all three scored [E5-11], and this is the strongest part of the file.**
1. **A large and reliable stream of earnings:** large, yes; reliable, only in the aggregate —
   two nine-figure loss years in eighteen, and everything made in one quarter.
2. **Massive liquid assets:** **$526.8M of cash at 2026-08-01, $874.8M at the fiscal year end**,
   plus **$1.2 billion of undrawn asset-based revolver to August 2029**. Note the corpus's
   caution **[E5-39]**: bank lines are *"the kindness of strangers"* and are not counted in the
   score; **on cash alone, the test still passes.**
3. **No significant near-term cash requirements — passes, and this is the one that usually
   kills.** **There is no debt at all.** The Senior Notes were repaid at maturity in Fiscal 2025
   and the preferred was retired for $813.8M in the same year. **[E2-54]**'s coverage test is
   vacuous here because there is no interest to cover. What remains is **$1,224.4M of operating
   lease liabilities**, real and contractual, against $429.0M of annual rent — and the
   **$1,277.2M of deferred revenue**, which is **[E3-52]**'s class: *"liabilities without
   covenants or due dates attached to them … the benefit of debt … but saddle us with none of
   its drawbacks."* Customers prepay for lifetime repairs; there is no date on which they must
   all be served.
- **Jurisdiction [E3-66], because this is not a US registrant.** Signet Jewelers Limited is
  **incorporated in Bermuda**, listed on the NYSE, and files a full 10-K as a domestic filer.
  Shareholders stand where a Bermuda company's shareholders stand, and the 10-K's own risk
  factors name *"risks related to international laws and Signet being domiciled in Bermuda."*
  **Recorded, not quantified, and it is not the reason for any verdict.**

**THE NAMED WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40], modelled from filed figures.**
- **Mechanism: the unit series reaches the operating leverage.** Signet's cost base is fixed —
  **$429.0M of rent, 2,582 leases, $555.0M of advertising, $2,173.2M of SG&A against $2,694.6M
  of gross margin.** Gross margin is **39.5%** of sales and SG&A is **31.9%**, so the operating
  line is the **7.6-point gap between them**. North America units have fallen **7.4%, 6.9% and
  6.3%** in the last three filed periods and the dollar line has been held by **AUR up 3.3%,
  7.6% and 6.3%**. The death is not a default; it is the arithmetic of the day the price
  offset stops.
- **Quantified.** Hold units falling at the filed **7%** a year and suppose AUR growth returns
  to the **2%** the 10-K reports for the UK market's own growth rate rather than the 6–8% mix
  effect of the last two years. Sales then fall about **5% a year**. With SG&A fixed in dollars
  and gross margin held at 39.5%, a **5% sales decline costs $135M of gross margin** and the
  **$393.1M of operating income is gone in under three years.** Signet closed 76 and then 82
  stores a year to defend this, which slows it and does not stop it.
- **Exposure, not experience [E4-40].** *"focusing on experience, rather than exposure …
  assuming a huge terrorism risk for which we received no premium."* The recent experience is
  benign — gross margin up 30 basis points, guidance raised, no debt. **The exposure is that
  49% of merchandise sales are bridal, the central stone is a commodity whose lab-grown
  substitute the company's own risk factors name, and the customer can price-check on a phone
  in the store.**
- **Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility** — as a
  ten-year statement. **Not near-term:** with no debt, $526.8M of cash and $525.3M of Fiscal
  2026 free cash flow, nothing forces the issue for years, which is precisely why the framework
  separates survival from the franchise.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

**No Q5 verdict is reported and none may be.** Q2 returned OUT, the hard sequence stops, and
**no box below is ticked.** The arithmetic is recorded because the register asks for a price,
a cap and a sovereign, and because the honest thing to say about this name is **where it did
not fail**.

- **Price US$100.38** (close 2026-09-18, aggregator, FLAGGED) · **shares 38,317,243** (10-Q
  cover, accession `0000832988-26-000229`) · **market cap US$3,846.3M** · net cash $526.8M, so
  enterprise value about **US$3,319.5M**.
- **Sovereign 5.34%**, US Treasury daily par yield curve 30-year, dated **09/18/2026**, struck
  this session. **The bare rate, with no per-name premium added [E3-42].**

| window | owner earnings | yield on the $3,846.3M cap | points over the 5.34% sovereign |
|---|---|---|---|
| 18 years, proceeds removed | $390.4–393.2M | **10.1–10.2%** | +4.8 |
| 5 years (corpus default) | $581.6–598.7M | **15.1–15.6%** | +9.8 to +10.3 |
| 4 years, pandemic year removed | $465.0–477.8M | **12.1–12.4%** | +6.8 to +7.1 |
| 3 years | $422.9–431.5M | **11.0–11.2%** | +5.7 to +5.9 |
| TTM to 2026-08-01 | $505.8–520.3M | **13.2–13.5%** | +7.8 to +8.2 |

- **What this says, and it matters for the register: SIGNET DID NOT FAIL ON PRICE.** On every
  window the run built, including the harshest one, the trailing owner-earnings yield is
  **above the ~10% floor [E4-28]**, and on the five-year corpus default it is roughly **15%**.
  **The value, as a round-number range [E4-01]: roughly $3,900 million to $6,000 million of
  business against a $3,850 million quote**, which is inside the range and would have been
  **"no useful conclusion"** on Bar 2 in any case.
- **[E5-35] is why none of that promotes anything:** *"You can turn any investment into a bad
  deal by paying too much. **What you can't do is turn any investment into a good deal by paying
  little.**"* The file closed at Q2 on the business, and a cheap price is not an answer to it.
- **Growth needed to justify the quote: none.** The price is covered by trailing owner earnings
  at a double-digit yield, which is the shape of a name the market expects to **shrink**. That
  is a coherent market view and this run does not dispute it: the market is pricing the unit
  series, and so is the run.
- **Windage count: ONE.** Conservatism is spent once, at the (c) end and in choosing the
  proceeds-removed long window as the honest figure. **No margin is applied on top and no
  risk premium touches the rate [E4-11, E4-48, E3-42].**
- **VERDICT: NOT REACHED — no box ticked.** Q5 did not open.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

No position is taken, so there is nothing to sell. **[E1-02]** governs the reversal, written
before the fact: *"I believe in establishing yardsticks prior to the act."* **Pre-registered
before the Q5 arithmetic above was run, per operator rule 9.**

**WHAT WOULD PROVE THE Q2 OUT WRONG — and it is a unit test and a share test, never a price
test [E4-55, E4-32, E2-44]:**
1. **North America units positive for four consecutive filed periods, with AUR not falling to
   buy them.** Units bought with discounts prove the opposite of the thesis. This is the
   criterion (2) evidence currently absent, and the company files the series itself.
2. **US market share above 8.5% for two consecutive annual reports, on the company's own
   MasterCard/Circana basis** — the same source and the same method, so the comparison is not
   an artifact of a changed denominator. **[E4-32]**: *"we want the moat widened every year."*
3. **A full fiscal year with no goodwill or indefinite-lived trade-name impairment**, ending a
   run that has produced $1,835.1M of them in eighteen years.
- **Threshold and window: all three, read on the Fiscal 2027 and Fiscal 2028 10-Ks.** Any two
  of three would reopen the file for a fresh Q2; one alone would not.

**WHAT WOULD CONFIRM THE OUT:** a further brand impairment in the Fiscal 2027 fourth-quarter
test; or units continuing to fall while share slips below 8.5%; or gross margin giving back its
gains when the gold price retreats, which would say the Fiscal 2026 margin was metal and scrap
recovery rather than mix.

**NEXT CATALYSTS:** the third-quarter Fiscal 2027 earnings release, early December 2026, which
will also carry the Bread program agreement as a 10-Q exhibit and the first quantification of
its signing bonus; and the Fiscal 2027 10-K, expected March 2027.

**The monitoring question [E3-30, E4-17]:** *is this erosion part of an aberrational cycle, or
has the business slipped in a way that permanently reduces intrinsic business values?* **This
run answers: slipped, and structurally** — because the erosion is in units and in the number of
places the customer can get the same stone, not in the cycle. **[E4-17]** is right that such
beliefs form gradually, and this one rests on four filed periods pointing the same way rather
than on one.

**Position size: ZERO.** **No alert band is armed in `tools/alerts.json` and no `PORTFOLIO.md`
row is added**, per the **QLYS ruling of 2026-09-07**: a name that failed on the **business**
gets no price alert, because a price alert on it is a category error. The reversal condition is
recorded in words above.

- **VERDICT: [x] OUT** — the file is closed at Q2, on the business. Q6 records the reversal
  condition rather than an exit.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT, stop. Q3 and Q4
      recorded without verdicts; Q5 headed **COMPUTATION — NOT A CLEARANCE** with no box
      ticked.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The only IN is
      Q1, and it rests on the 10-K and the 10-Q read directly. The moat class is **NONE**, not
      PROVISIONAL, and the reason is given in the row.
- [x] **Every UNRESEARCHED item names the artifact and where it lives.** Three are named in the
      Q3 block (the guidance-versus-outturn table and its eight accessions; the retention test
      and the market-value series it needs; the Bread program agreement due as a 10-Q exhibit in
      December 2026). **None of the three is a gate verdict**, and none of them is load-bearing
      for the Q2 OUT, which rests on the registrant's own risk factors and its own unit series.
- [x] **No UNKNOWABLE verdict was written**, and the run states positively why not: Q2 failed
      **[E3-03]** criterion (2) on evidence, so the **[E4-04]** perimeter close does not arise.
- [x] **Step 0: the filings were read, with accession numbers, and two figures were
      cross-checked against the filed statements** (the 10-Q cover's 38,317,243 against 70.0
      issued less 31.3 treasury on the face of the same balance sheet; total sales $6,813.6M on
      the 10-K statement of operations against the tagged value).
- [x] **Owner earnings on a multi-year mean and never via a net-income proxy.** Seven windows
      and two (c) ends published; (c) disclosed as a judgment and placed at the capex end with
      the filing's own capex guidance as the reason.
- [x] **Competitor row filled**, five companies, every figure computed in this run from filed
      10-Ks, with five unavailable peers named and each obstacle stated.
- [x] **Sovereign is USD for a predominantly USD earner, from the issuing authority, dated
      09/18/2026, struck this session**, and the 9% of earnings in GBP and CAD is disclosed
      rather than averaged away.
- [x] **Value stated as a round-number range**, not a point estimate, and headed as a
      computation.
- [x] **One bar chosen: neither, because Q5 did not open.** Windage count stated: **one**.
- [x] **Prices dated; the aggregator was used for the live quote only and is FLAGGED.**
- [x] **Every judgment carries a ledger id**, and every id cited was checked against
      `principle_ledger.csv` **(311 rows on disk; CLAUDE.md's pointer says 267 and the file was
      counted, not the pointer)** before it was written, with the quoted text read against the
      row.
- [x] **One error of my own was caught and corrected in place, not silently**: the run first
      wrote "third CEO in three years" from memory, and the 8-K of 2024-10-01 says Gina Drosos
      retired "after twelve years." The correction is written into Q2 where the error was.
- [x] `python tools/check_framework.py` run and PASSING before the fold commit.
- [x] Run committed to git with a pathspec, at each stage.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** The largest specialty jewelry retailer in America, debt-free and trading at a
  double-digit trailing owner-earnings yield, closed at **Q2** because its own 10-K says
  competitors sell *"easily comparable pieces of jewelry, of similar quality"* nearby with
  *"increased price transparency"*, and its own MD&A shows **North America units down 7.4%,
  6.9%, 6.3% and 8.3% across four consecutive filed periods** while the dollar line was held up
  by average price — **[E3-03]** criterion (2) failing on the company's own evidence, with
  **[E4-55]** naming the pattern.
- **It did NOT fail on price and it did NOT fail on survival.** Q4 items record **GOOD** under
  **[E4-20]**, zero debt, $526.8M of cash and a $1.2bn undrawn revolver; the Q5 computation puts
  trailing owner earnings at **$390M–$599M on a $3,846.3M cap, a 10.1%–15.6% yield, above the
  ~10% [E4-28] floor** on every window built. **[E5-35]** is why that promotes nothing.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable; the verdict is OUT.
- **If UNKNOWABLE:** not applicable.

## RUN LOG
- Sovereign struck 2026-09-20 from the **US Treasury daily par yield curve**, cache deleted and
  re-fetched: **5.34%, dated 09/18/2026**.
- Price struck 2026-09-20: **$100.38, close of 2026-09-18**, aggregator, FLAGGED.
- Filings read: 10-K FY2026 `0000832988-26-000055`; 10-Q Q2 FY2027 `0000832988-26-000229`;
  8-K `0000832988-26-000227` and its EX-99.1; 8-K `0000832988-26-000231`; 8-K
  `0000832988-24-000214` (the CEO succession); 8-K `0000832988-26-000105`; 8-K
  `0000832988-26-000185`; 10-K FY2025 `0000832988-25-000018`; 10-K FY2024
  `0000832988-24-000083`; 10-K FY2023 `0000832988-23-000032`; 10-K FY2019
  `0000832988-19-000003`.
- Peer filings read from `companyfacts` and cross-checked on revenue: BRLT (CIK 0001866757),
  MOV (0000072573), FOSL (0000883569), TPR (0001116132).
- Research folder: `Test Runs/_research 2026-09-20 SIG/`.
"""

open(p, "w", encoding="utf-8").write(head + rest)
print("ok", len(head + rest))
