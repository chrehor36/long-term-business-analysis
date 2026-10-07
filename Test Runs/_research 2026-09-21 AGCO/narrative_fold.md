
---
## UPDATE 2026-09-21 - AGCO: Q2 OUT. Deere earns more in its worst year than AGCO does in its best, and the pricing line is in AGCO's own MD&A.

**Run file:** `Test Runs/2026-09-21 Run - AGCO AGCO Corporation.md`. **Register entry 158.**
Price **$120.68** (aggregator, flagged, intraday) x **70,031,729 shares**, one class, from the
10-Q cover of 2026-07-30, accession `0000880266-26-000068`, = cap **$8,451M**. Sovereign
**5.34%** (US Treasury 30 Yr, 09/18/2026, issuing authority, struck fresh; FRED not used).

### THE FINDING: the competitor row is the whole file, and the registrant wrote it itself

AGCO's Item 1 does not make you guess who the comparators are. *"Our two principal competitors
on a worldwide basis are Deere & Company and CNH Industrial N.V."* Item 1A adds that they
*"are substantially larger than we are and have greater financial and other resources."* Both
are SEC registrants. **Five years, operating margin on equipment/ag net sales, each figure from
the comparator's own filed segment note:**

| | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| **AGCO** | 9.0% | 10.0% | 11.8% | **(1.1)%** | 5.9% | **7.1%** |
| **Deere, ag only (PPA+SAT)** | 19.0% | 17.9% | 23.2% | 19.3% | 14.1% | **18.7%** |
| **CNH, Agriculture segment** | 12.3% | 13.7% | 14.5% | 10.5% | 6.2% | **11.4%** |

**Deere earned a higher margin in its worst year of the five (14.1%) than AGCO earned in its
best (11.8%).** AGCO is last at the cycle peak and last at the cycle trough, and it posted an
operating **loss** in 2024. Every limit of the comparison runs in AGCO's favour and it still
comes last: CNH's figure is its own non-GAAP Adjusted EBIT, which strips restructuring and
impairment that AGCO's GAAP figure carries; CNH restated its own 2023 from 15.05% to 14.53%
between filings and the later number is used; Deere's year ends in late October. **A quarter's
offset does not explain an eleven-point gap.**

### THE SECOND FINDING: AGCO publishes its own pricing power, every year, and it is 1-2%

The MD&A carries an estimated worldwide average price change. Pulled across four 10-Ks:

| 2014 | 2015 | 2016 | 2018 | 2019 | 2021 | 2022 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| +1.5% | +1.8% | +1.5% | +1.4% | +1.9% | +6.6% | +11.6% | **-0.9%** | +1.1% |

**[E2-44]'s first characteristic - can it raise prices "even when product demand is flat and
capacity is not fully utilized" - fails on the filing's own number: in 2024, with net sales
down 19%, the worldwide average price FELL 0.9%.** The 2021-22 double digits are cost
pass-through inside a general inflation, bracketed by 1-2% years on both sides. South America
in 2025 is described in consecutive MD&A sentences as carrying *"negative pricing impacts."*
**[E4-37]** reads at the agony end. This is a metric worth lifting for other industrial runs:
**a filer that discloses an average realised price change has answered [E2-44] and [E3-33]
without being asked**, and most runs never look for it.

### THE HONEST QUALIFICATION, recorded because it is the strongest thing against the verdict

**There IS a franchise inside AGCO and it is one region.** Segment note 25: Europe/Middle East
earned **$1,006.8M on $6,736.7M of net sales in 2025 - 14.9%, against 14.3% in 2024 and 15.0%
in 2023**, stable through a full cycle and level with Deere's ag margin in Deere's worst year.
**The other three regions together earned $(32.8)M on $3,345.3M**, North America alone losing
**$112.0M** and printing a **(5.2)%** operating margin again in Q2 2026. Fendt in Europe is
real. **It does not reverse Q2**, because the unit of the test is the company **[E4-08]** and
the company is what is for sale - but it is the sharpest form of the bear-case-stated-fairly
that **[E4-51]** demands, and it is also the named way the business dies: **a 5-point fall in
the EME margin removes $337M, or 57% of consolidated income from operations, and North America
moved further than that in two years** ($398.1M -> $84.0M -> $(112.0)M).

### REFUTED PRIORS - two, and both were mine or the screen's

1. **"ONE LINE MADE THE CASH: AccountsPayable moved 44% of 2021 OCF" - the arithmetic is right
   and the inference is backwards.** Payables did add $292.2M against $660.2M of operating cash.
   **But the working-capital block as a whole took $451.2M OUT of 2021**: receivables $(207.7)M,
   inventories $(762.6)M, other assets $(268.0)M against payables +$292.2M, accruals +$241.2M,
   other liabilities +$253.7M. 2021 was a working-capital **build into a boom**, and payables
   merely funded part of the inventory. **The DELL/INOD shape is in 2025 instead, in two lines
   and the other direction**: receivables +$231.0M and inventories +$237.5M released as the
   business shrank - **$495.6M, 50.2% of the entire year's operating cash.** And the company
   headlines that year's cash as *"record free cash flow of $740 million"*, computed against a
   capital expenditure of $247.9M that is **below the same year's depreciation of $256.5M for
   the first time in twelve years.** Half the numerator is destocking; the denominator is
   deferral.
   **The observation for the screen, and it is not a defect:** `working_capital_flag()` fires
   when **a single line** crosses 30% of a year's operating cash. 2025's release is spread
   across two lines, neither dominant alone, so the flag pointed at 2021 instead. It still did
   its job - it sent a reader to the cash-flow statement, which is what a prompt is for
   **[E5-36]**. A two-line variant would fire on almost every cyclical.
2. **"acquisitions are $2,047M, 26% of cap, inside the window."** Read from the notes by hand,
   what actually moved is **three events, not one**, and they run in both directions: **PTx
   Trimble bought 2024-04-01** for $1,954.0M cash ($1,910.0M total consideration), 85/15 with
   **Trimble's put exercisable from 2027-04-01 on EBITDA multiples** and $299.2M of redeemable
   NCI in mezzanine equity; **Grain & Protein sold 2024-11-01** for $630.7M net against a
   **$507.3M loss on sale**; **the TAFE stake sold 2025-09-30** for $260M with a $251.9M gain.
   **The twelve-year owner-earnings numerator and today's market cap are not the same company,
   and the gap cannot be closed from the filings** - PTx Trimble's stand-alone result is
   disclosed exactly once ($171.3M of net sales and a **$350.9M net loss** for the nine months
   to 2024-12-31) and never again. **The rung that fails here is not the tag layer. It is the
   filer's own segment disclosure, which reports by geography and not by the acquired unit.**
   That is a *new* form of the perimeter limit the resume state already records.

### THE CAPITAL-ALLOCATION RECORD, which is the thing a future reader should not have to rebuild

- **$351.0M of the PTx Trimble goodwill was impaired at the 2024-10-01 test date - six months
  after the deal closed on 2024-04-01.** The 2025 test survived on **16% headroom, falling to
  3% if the discount rate rises 1.0 point**, and KPMG made it the sole critical audit matter.
- The 10-K discloses **accumulated goodwill impairment of approximately $708.2M across four
  separate acquired businesses**: PTx Trimble North America (2024), grain storage and protein
  production systems Europe/Middle East (2019), the Chinese harvesting unit (2012), and the
  former sprayer unit (2006). **Add the $507.3M G&P loss on sale and the acquisition record
  over two decades is a register of write-downs.**
- **And the metric the executives are paid on excludes it.** DEF 14A of 2026-03-12: *"the
  Talent and Compensation Committee determined that **the results related to the PTx Trimble
  joint venture in 2024 and 2025 should be excluded from the calculation of RONA**."*
  **[E2-57]** at the largest decision on the file.

### THE ADJUSTED-MARGIN FINDING - the [E4-29] companion check paid, but not where it usually does

The standing instruction to pull the 8-K EX-99.1 before scoring [E4-29] is what produced this,
and it produced something other than EBITDA. **The word EBITDA appears four times in the FY2025
10-K - all four mechanical (two in the goodwill valuation technique, one in a credit covenant,
one in the PTx put strike) - and ZERO times in either earnings release.** What fires instead is
**three different "operating margins" published for the same year 2025**:

| GAAP income from operations / net sales | **5.9%** | 10-K |
| "adjusted operating margin" | **7.7%** | 8-K EX-99.1 of 2026-02-05 |
| **the number the bonus was paid on** | **8.5%** | DEF 14A of 2026-03-12 |

The proxy prints the counterfactual itself, which is the candour half: *"If TAFE litigation and
effects of North America tariffs had not been excluded from the calculations, the results would
have been 7.7% for adjusted operating margin and 15.5% for RONA."* **The exclusions moved
margin from inside the 6.9-8.4% target range to above it, and RONA from below the 15.9% maximum
to above it.** And the pay-versus-performance table prints a company-selected **adjusted
operating margin of 9.2% for 2024**, a year whose GAAP operating margin was **(1.0)%** - a
**10.2-point wedge**. **The annual incentive paid 163.0% of target** for 2025; CEO short-term
incentive $3,651,200, summary-compensation total $19,657,541, compensation actually paid
$23,897,459 - in a year net sales fell 13.5%, North America lost $112.0M, and the company's own
five-year TSR index stood at **$120.10 against the S&P Midcap 400's $154.68**.

**The lesson for the next runs, and it generalises past AGCO:** [E4-29]'s flag is usually
scored by grepping for EBITDA. **Here EBITDA is clean and the company is still running its
public and compensation narrative on an adjusted number.** The test that caught it was
comparing **the same metric across three documents** - 10-K, earnings release, proxy - rather
than looking for one word. That should be the default: **find the headline margin in all three
places before scoring the flag.**

### WHAT READ CLEAN, said plainly because the flags are prompts and not scores

- **[E4-30]'s filed-figure tells read clean in both directions.** Nothing is smoothed (net sales
  14,412.4 -> 11,661.9 -> 10,082.0; income from operations 1,700.4 -> (122.1) -> 595.7), and
  cash taxes run **above** book, not below: income taxes paid net of refunds **$463.6M /
  $344.0M / $283.1M** for 2023/2024/2025, the last being **47.0% of reported pre-tax income**,
  because the **US pre-tax result was negative in all three years** while the profits are earned
  and taxed in Germany, Switzerland, France, India and Brazil.
- **[E5-15] serial issuance reads clean and inverted**: 74,420,952 -> 72,629,310 -> 70,002,207
  shares over eighteen months, a $250.0M ASR in November 2025 at **$100.14** against $120.68
  today, $785.0M of authorisation left.
- **The dividend was cut early and hard** - $3.66 a share in 2024 to $1.16 in 2025, cash paid
  $457.4M -> $273.1M -> $86.5M - which is the opposite of **[E2-60]** and **[E2-52]**.
- **The 2008-09 record answers the cycle question in AGCO's favour.** FY2009 10-K, accession
  `0000950123-10-017928`: net sales fell 21.3% from $8,424.6M to $6,630.4M and the company
  still earned $135.7M net, $219.3M from operations and **$351.7M of operating cash**. It has
  one loss year in nineteen and that one was self-inflicted.

### ONE STRUCTURAL ITEM FOR THE SECTOR METHOD FILE, decided from the filings and not from the brief

The brief asked whether AGCO's finance arrangement is float-bearing and therefore governed by
`Framework/SECTOR METHOD - owner earnings for insurers ...`. **Decided NO, from Note 10 and
Note 18.** The finance joint ventures are **49%-held, equity-method, and funded by Rabobank
lines** - *"The majority of the liabilities represents notes payable and accrued interest"* -
which is borrowed money with due dates, the opposite of **[E3-52]**'s covenant-free
customer-prepaid liability. There is no premium received before a loss is paid. **$10,433.1M of
assets against $9,284.6M of liabilities never enters AGCO's balance sheet**, and AGCO's share
of the earnings enters the income statement as one line, treated in owner earnings by
**[E3-04]**'s look-through addition of the undistributed portion.
**What the structure DOES do is keep the leverage box unticked at Q3's weight case** - a
9:1-levered captive inside the consolidation would have made Q3 a binary gate under
**[E3-29]**. **And what it costs is a counterparty concentration worth recording**: about
**$2.1 billion of AGCO's working capital is financed off balance sheet** through those JVs'
receivable purchases ($1.8bn outstanding at 2026-06-30), $257.2M of factoring and $41.8M of
supplier finance - **and Rabobank is also "the principal agent and participant in the Company's
revolving credit facility."** One counterparty funds the dealers, the receivables and the
revolver.

### TOOLING: .gitignore, two more un-patterned dump shapes

The MGM fold of the same morning added patterns for `tenk*.txt`, `tenq*.txt`, `*_body.txt` and
`companyfacts.json`. **Two shapes this run produced still slipped through all sixteen
patterns**: peer dumps named after the peer and its fiscal year (`peers/DE_fy2025.txt` at
683KB, `peers/CNH_fy2025.txt` at 558KB - "10-K" appears nowhere in the name) and the SEC
**submissions** feed saved as `subs.json`, where the existing block ignores only
`submissions.json` and `*submissions*.json`. Patterns added for `*_fy20*.txt`, `*_FY20*.txt`,
`subs.json` and `*_raw.json`, named rather than blanket, for the reason the 2026-09-07 block
gives.

### ONE ERROR OF MY OWN, recorded rather than quietly fixed

The summary block I appended to `Test Runs/_research 2026-09-21 AGCO/oe.py` indexed the row
tuple wrongly - `r[3]` and `r[4]` as SBC and capital expenditure, when the tuple is
`(yr, ocf, dep, amort, sbc, capex, eq)` - and printed **"mean capex 28.1"** against a filed
twelve-year series running $201.0M to $518.1M. Caught on the first read of its own output
because the number was absurd; fixed in place with the fix commented in the file; corrected
figure **$290.1M**. **The main year-by-year table was never affected** - it is produced by the
loop that unpacks the tuple by name, which is why naming beats indexing. Recorded under
operator rule 6.

### WHAT WOULD REVERSE IT - in words, because no price alert is armed on a business failure

The QLYS ruling applies: a name that failed at Q2 failed on the **business**, so no
`tools/alerts.json` band and no `PORTFOLIO.md` row. The headline reversal item is the pricing
line: **the MD&A's own worldwide average price printing +3% or better in a year when unit
demand falls**, which is [E2-44]'s first characteristic passing rather than failing. The others
are at Q6 of the run file: consolidated operating margin holding 12%+ across three years
including a trough (nineteen filed years contain no such reading); North America segment income
positive and above 8% of North America sales for two years; PTx Trimble's stand-alone result
disclosed and covering the $1,910.0M paid; and the Trimble put settling on 2027-04-01 without a
cash surprise.
