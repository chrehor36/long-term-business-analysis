
## UPDATE 2026-09-21 - JAKK (JAKKS Pacific, Inc.): Q1 IN, Q2 OUT on the business. Wave 7, name 22; register entry 154.

**Run file:** `Test Runs/2026-09-21 Run - JAKK JAKKS Pacific.md`.
**Research:** `Test Runs/_research 2026-09-21 JAKK/` (FY2025 and FY2021 10-Ks, the Q2 FY2026 10-Q,
the 8-K earnings release, the 2026 proxy, and the companyfacts of JAKK, MAT, HAS and FNKO).
**Claimed at dispatch, not at fold:** no `*Run - JAKK *.md` existed in `Test Runs/` of any vintage,
and the string JAKK appeared **once** in `Screens/WATCHLIST RUN QUEUE.md` before this entry - not
as a register entry, but **inside the HAS entry, where a previous run had already pulled JAKKS'
own 10-K sentence** *"the toy industry has no significant barriers to entry"* and computed its
unleveraged NTOA at 8.8% beside Mattel's 33.9%. An independent prior run reached the same reading
of this company from the other side of the row.

### THE FINDING: the competitor row splits the toy industry in two, and it is a single tagged line

The metric is **royalty expense as a percentage of net sales**, from `us-gaap:RoyaltyExpense` in
each registrant's own 10-K, same three fiscal years, aggregate:

| | royalty ÷ net sales FY2023-25 | operating margin, same window | net sales FY2022 → FY2025 |
|---|---|---|---|
| **JAKK** | **16.05%** | **+5.73%** | **-28.3%** |
| FNKO | 16.60% | -4.47% | -31.3% |
| HAS | 7.81% | -6.05% *(+9.94% ex impairment)* | -19.7% |
| MAT | 4.69% | +11.15% | -1.6% |

**The two that own their characters pay 4.7% and 7.8%; the two that rent them pay 16.1% and
16.6%.** The renters pay 2.1x to 3.4x the rent and cannot cover it. **This is the cheapest moat
test the project has found for a licensing industry** - one tagged annual line, available for every
SEC-filing toy company, immune to the impairments and restructurings that make the operating line
useless for cross-company comparison (Hasbro carries $1,191.2M of goodwill impairment in FY2023 and
$1,021.9M in FY2025). **Recommend it for any future run on a licensee-model business** - consumer
products, apparel with licensed marks, collectibles, mobile games.

JAKKS' own risk factors close the file by themselves: *"Sales of products under trademarks or trade
or brand names licensed from others **account for substantially all of our net sales**"*; *"the toy
industry has **no significant barriers to entry**"*; *"Our competitors have obtained and are likely
to continue to obtain **licenses that overlap our licenses**"*. And the licensor holds every veto -
royalty rate, minimum guarantee, product approval, contract-manufacturer approval, channel limits,
and a post-expiry audit right.

### Priors refuted, and one confirmed

1. **THE BRIEF'S SEASONAL-PAYABLES HYPOTHESIS IS REFUTED FOR FY2021.** The brief suggested the
   cause of the `wc_note` would be that *"toy companies carry seasonal payables and 2021 was a
   supply-chain year."* Half right and wrong where it counts: 2021 **was** a supply-chain year, but
   the FY2021 liquidity note names **receivables and in-transit freight**, not payables -
   *"higher working capital usage driven by an increase in accounts receivable due to higher Q4
   sales and a higher inventory balance resulting from an increase in freight-in-transit."*
   Payables rose, but by less than half of what they were funding.
2. **THE `wc_note` SIGN WAS **NOT** INVERTED THIS CYCLE - the third straight cycle has now produced
   a different failure mode from the same flag.** BELFB/IIIN/SGC found the direction wrong; here
   the direction is right and the **denominator** is the problem. **The generalisable statement is
   now: this flag's ratio has been correct arithmetic every time and its SENTENCE has been wrong
   every time.**
3. **A ratio against a NEGATIVE operating-cash year is the failure mode nobody had named yet.**
   `working_capital_flag` divides by the year's operating cash. FY2021 operating cash was
   **-$5,879k**. The flag printed "ONE LINE MADE THE CASH" about a year in which operating
   activities **used** cash. `level_shift` and `best_year_dependence` both carry near-zero and
   across-zero guards, added iteratively across five runs. **`working_capital_flag` has neither.**
   This is the sixth instance of the ratio-near-zero class in this project and the first in this
   function.
4. **CONFIRMED, and it is the third cycle running: the screen band is the highest and narrowest
   construction obtainable.** IIIN and SGC found the band 2.4x too high; here the seventeen-year
   D&A-end mean is **$6.98M** against a published floor of **$18.55M** - **2.7x**. The mechanism is
   the same every time: five years is the corpus default **[E2-42]**, and on a cyclical filer the
   most recent five contain the boom.
5. **The cap reproduced for the third consecutive cycle.** 11,445,012 x the 2026-08-28 close of
   $25.42 = $290.93M against the screen's 291. **Stale price, not a count error.** The BELFB (6.29x)
   and MCFT (1000x units) shapes remain the exceptions, not the rule.

### Tooling and documentation findings - reported, not patched (one tooling, one retrieval, one ledger)

1. **A STRUCTURAL DEFECT IN `working_capital_flag`: `WC_TAGS` CANNOT SEE RECEIVABLES OR
   INVENTORY.** The list in `Screens/floor_screen.py` is
   `IncreaseDecreaseInAccountsPayableAndAccruedLiabilities`, `IncreaseDecreaseInAccountsPayable`,
   `IncreaseDecreaseInContractWithCustomerLiability`, `IncreaseDecreaseInDeferredRevenue` - **four
   liability tags and nothing else.** The docstring promises the flag *"names the year and the
   line"*; it can only ever name a payable. At JAKKS the two largest working-capital lines in the
   flagged year (inventory 7.71x operating cash, receivables 7.44x) are invisible to it, and the
   line it did name ranked **third**. **Second half of the same defect:** JAKKS splits its filed
   payables line across `IncreaseDecreaseInAccountsPayable` (19,751) **and**
   `IncreaseDecreaseInAccountsPayableRelatedParties` (5,266); the tag list has only the first, so
   the flag **understated its own line by 27%** and printed 336% where the filed line gives 425%.
   **Not patched - operator rule 6 and PRIME RULE 5.** *(Note for whoever does patch it: adding
   receivables and inventory tags will raise the fire rate materially, and the resume-state note's
   warning against tuning a threshold to shrink a count applies in reverse here.)*
2. **A RETRIEVAL HAZARD FOR THIS QUEUE: JAKKS FURNISHES ITS EARNINGS RELEASE AS EX-10.1, NOT
   EX-99.1.** The 8-K of 2026-07-24 (accession `0001185185-26-003108`) carries Item 2.02 and the
   exhibit index reads *"10.1 | July 23, 2026 Press Release"*. **The dispatch brief, the framework
   and every prior run in this wave say "the latest 8-K EX-99.1 earnings release".** A run that
   globbed for `EX-99` would have found nothing and could have concluded the company furnishes no
   release. **The rule that survives: read the 8-K's own exhibit index, never the exhibit file
   naming convention.**
3. **A LEDGER FINDING: [E3-03] AND [E3-43] SHARE TWO VERBATIM SENTENCES AND NEITHER IS MARKED
   `ALIAS NOTE`.** Both rows are the 1991 letter. **[E3-03]**'s `quote_verbatim` ends *"…The
   existence of all three conditions will be demonstrated by a company's ability to regularly price
   its product or service aggressively and thereby to earn high rates of return on capital.
   Moreover, franchises can tolerate mis-management."* **[E3-43]**'s `quote_verbatim` **begins with
   those same two sentences**, and its own `evolution_notes` describes itself as *"Lines 276-289,
   **the sentences immediately following** E3-03's three franchise conditions"* - but they are not
   following E3-03's quote, they are **inside** it. Nine ledger rows carry the string ALIAS in
   their notes; neither of these two does. Consequence for runs: the framework cites *"franchises
   can tolerate mis-management"* under **[E3-43]** at Q3 while the identical sentence is verbatim
   in **[E3-03]** at Q2, so both citations are correct and a reader checking one against the other
   will believe one is wrong. `check_framework.py` cannot see it - both ids exist and both quotes
   are verbatim. **Reported for the operator; not edited.**
4. **A DOCUMENTATION FINDING IN THE FRAMEWORK'S RENDERING OF [E3-03], and this run acted on it.**
   `THE FRAMEWORK v4.md` renders the row at Q2 as *a franchise is a product or service that "(1) is
   needed or desired; (2) … no close substitute …; (3) is not subject to price regulation."* - and
   **stops**. The row's next sentence is the only **quantitative** test it contains: *"The existence
   of all three conditions will be demonstrated by a company's ability to **regularly price its
   product or service aggressively and thereby to earn high rates of return on capital.**"* A run
   reading only the framework gets three yes/no criteria; a run opening the row gets a fourth,
   arithmetic one. **This run quoted from the row and used it**: JAKKS cannot price aggressively
   (the retailer recalibrates the price, the customer cuts the order on tariffs) and does not earn
   high returns on capital (operating margin 2.49%, pre-tax return on average equity 6.0% in
   FY2025, both falling three years running). **This is the third consecutive cycle in which
   opening the ledger row rather than trusting the framework's rendering produced something the
   rendering did not carry** - IIIN found punctuation, SGC found a misattribution, JAKK found a
   dropped test.
5. **No other tooling defect.** `tools/sources.py` behaved: `sovereign`, `price`, `_chart`,
   `cik_for`, `annual(vintage='newest')`, `split_factor_after` and `_get(headers=SEC_UA)` all
   worked first time. **`cik_for` returns a `(cik, name)` TUPLE, not a string** - worth knowing
   before writing `int(cik)`. The known 403 on `www.sec.gov/Archives` under the default `WEB_UA`
   was routed around, not re-diagnosed. `pandas.read_html` was not needed; the filings were parsed
   with a plain tag-stripper, which handled all five documents.

### What this run adds to the reading of the rest of the queue

- **A negative operating-cash year makes every ratio in the screen row meaningless at once, and
  there is no column that says so.** JAKKS' FY2021 sits inside the priced five-year window with
  operating cash of -$5.9M. `wc_note` divided by it. `growth_required` did not refuse (it refuses
  only on a negative **bottom boundary**, and JAKKS' band bottom is +$18.55M). `level_shift`
  refused correctly and `best_year_dependence` fired correctly. **Three of five row-level guards
  handled it; the fourth printed a confident sentence.**
- **[E4-55] again: no SEC toy filer discloses unit volumes.** The HAS entry recorded *"no
  unit/player series has EVER been filed by HAS or any SEC toy peer"*; JAKKS confirms it - the
  10-K gives dollars, segments and divisions and no units anywhere. **The nearest physical series
  in a licensing business is the minimum-guarantee schedule**, and at JAKKS it runs the wrong way:
  **$71.9M total / $31.0M current at 2021-12-31 → $189.8M / $57.4M at 2025-12-31**, a 2.6x rise in
  fixed rent while net sales fell 8.1% over the same four years. Recommend reading that schedule on
  every licensee-model name.
- **The [E4-29] fifth flag and [E2-49] met in the proxy on this name.** The DEF 14A of 2026-04-22
  says cash bonus has been *"based **exclusively** upon Adjusted EBITDA"* since at least 2019,
  *"as adjusted in the **sole discretion** of the Compensation Committee"*, and that a 2025 bonus
  was *"based **solely upon the market performance of our common stock**"* (**[E3-50]**). Recorded
  beneath the close and **not scored**, because Q3 never opened and a Q3 finding cannot change a Q2
  verdict **[E2-37, E2-38, E3-39]**. Worth noting what did **not** fire: **no guidance, no growth
  target, no earnings projection anywhere** - [E4-22]'s third flag is clean and **[E5-30]**'s
  ratchet has not been started; and the ATM has never been drawn and the 2022 shelf expired unused,
  so **[E5-15]** does not fire on a share count that nonetheless rose 17.7% since Nov 2022.

## No price band, and the reversal condition in words

**No `tools/alerts.json` entry and no `PORTFOLIO.md` row.** The QLYS ruling of 2026-09-07: a name
that failed on the **business** gets no price alert. **The reversal condition, in words:** the
**royalty ratio falling decisively and durably toward the IP-owners' 5-8% of net sales** - which
means wholly-owned brands (Disguise and the proprietary lines) carrying the majority of revenue -
**or the minimum-guarantee obligation shrinking against a rising sales base.** Price is not a
reopening condition at any level, and neither is a good quarter.

## The uncomfortable part, written down rather than hedged

**[E4-51] demands the best argument against my own verdict.** It is that **JAKKS' gross margin ROSE
from 26.5% to 32.4% between FY2022 and FY2025 while revenue fell 28.3%** - price held, units lost,
which is what a franchise under stress looks like - **and that the balance sheet went from $2.9M of
equity at 2019-12-31 to $249.1M at 2025-12-31** with the $125.8M Recap term loan, the $69.2M BSP
term loan and the Series A preferred all retired, **with Q2 2026 net sales up 17%.** A reader could
fairly say I have written up a turnaround as a decline.

**Why it does not move the verdict.** The FY2025 MD&A attributes the gross margin itself: Toys'
cost-of-sales percentage fell *"due to **lower inventory obsolescence costs**"* - writing off less
stale inventory, not raising price - and in the same sentence notes *"royalty rates were higher
year-over-year."* Costumes' gross margin went the **other** way, *"attributable higher royalty
expense due to **higher royalty guarantee shortfalls**"*: JAKKS paid royalty on sales it did not
make. And where the rented input actually lands, the margin collapsed - **operating margin 8.31% →
2.49%, pre-tax return on average equity 49.5% → 26.8% → 18.5% → 6.0%** over the identical window.
A gross margin that rises while the operating margin falls by two-thirds is a smaller company
carrying the same rent. **Finally, gross margin is the wrong instrument for the question:**
[E3-03] criterion 2 asks whether the **customer** sees a close substitute, and Target and Walmart
consult Mattel's catalogue, not JAKKS' margin. The deleveraging is conceded and is exactly
**[E2-38]** - *"Good jockeys will do well on good horses, but not on broken-down nags."*

## Acceptance test

`python tools/check_framework.py` **PASS** before the fold commit (ledger **311 rows, 311 distinct
ids**; phantom citations **0** across 1,132 test-run files; unlabelled numbers 0 in all five
governing documents). **`CLAUDE.md`'s key-files table still says 267 rows; the file counts 311 and
`check_framework.py` agrees** - the same stale pointer the SGC cycle recorded, still standing, and
still not edited by a run. **49 distinct ledger ids are cited in the run file and all 49 were verified to exist in
`principle_ledger.csv`; fifteen
quoted fragments were matched word for word against `quote_verbatim` rather than against the
framework's rendering**, which is what produced findings 3 and 4 above.
