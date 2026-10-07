
---

# MCFT - MasterCraft Boat Holdings, Inc. - RUN 2026-09-20, WAVE 7 NAME 8, REGISTER ENTRY 140
**Q1 IN. Q2 OUT, on the business. The file closed at Q2.**
Run file: `Test Runs/2026-09-20 Run - MCFT MasterCraft Boat Holdings.md`.
Research: `Test Runs/_research 2026-09-20 MCFT/`.
Price **US$19.82** (close 2026-09-18, Yahoo Finance, aggregator, flagged, raw response saved).
Shares **24,339,371** from the cover of the **FY2026 10-K, accession `0001193125-26-387432`,
filed 2026-09-10**, as of 2026-09-04, **one class**. **Cap re-struck by hand: US$482M** against
the screen's $389M. Sovereign **5.34%**, 30-year US Treasury par yield, 2026-09-18, issuing
authority, struck fresh with `tools/sources.py`.

## The four findings that matter

**1. The screen was reading a company that no longer exists in that form.** MasterCraft
**completed a merger with Marine Products Corporation on 2026-05-15** for approximately **$284.2
million**, and filed its **FY2026 10-K on 2026-09-10, ten days before this run**. Neither event
is in the screen row. The merger added roughly **8.0 million shares (+48.9%)**, a third
reportable segment, the Chaparral and Robalo brands, a 1,262,000 sq ft plant in Georgia, and two
new 10%-plus holders. **MPX was one of the five comparables the brief told this run to put in its
competitor row.** It is now inside the subject. The row was built anyway, using MPX's final
10-K, and it is the most informative line in the table.

**2. The `cap_flag` is a units error, and that completes the flag's evidence set.** The FY2025
10-K cover says the float *"was approximately $ 236,100,000 "*: **$236.1 million, not $236,100
million**, a clean 1000x extractor error. **CALM and EMBC both resolved this flag as a real
drawdown; MCFT resolves it as the other branch.** The flag now has instances of both hypotheses
on the record, which means it genuinely cannot be scored and must always send a reader to the
cover page. The cap was wrong for a second and independent reason: the screen's share count was
pre-merger.

**3. The `wc_note` is right about the arithmetic and wrong about the verb, for the second wave-7
name running.** The flag heading is *ONE LINE MADE THE CASH*. Accounts payable in fiscal 2024
was **(7,594)** against continuing operating cash flow of **12,200**: **62.2% reproduced to the
decimal**, and the line **consumed** the cash rather than making it. And **the flag named the
second-biggest line again**, exactly as at EMBC: accrued expenses and other current liabilities
moved **(12,208)**, **100.1%** of the year's operating cash. **Two wave-7 runs in a row have now
found `wc_note` pointing at the wrong line.** The tooling note is below.

**4. `best_year_dep` was the honest statistic and `spread` was the misleading one.** The screen
carried `spread` 0.271 with a caveat, and `best_year_dep` 0.186 against `best_year_dep_oe`
0.209. The [E4-25] rebuild ran here (twelve fiscal years of 10-Ks under one CIK, unlike EMBC
where it could not run at all) and produced a **window spread of 1.7%** between a five-year
[E2-42] default and a nine-year window. **That agreement is fake.** Both windows contain FY2022
and FY2023, the two years of the pandemic boat boom. **Delete the three wave years as [E4-41]
requires and the same arithmetic falls from $36M-$42M to $11.5M-$11.8M**, thirty cents on the
dollar. The narrow spread was concealing precisely what the dependence statistic was disclosing.
`best_year_dep` was also decoded: it is *the fraction by which the multi-year mean falls if its
single best year is deleted*, reproduced at **18.58%** against the screen's 0.186. **Of the two
constructions, `best_year_dep_oe` 0.209 is right**, on operator rule 8 and [E2-23]: the
framework's one number is owner earnings, so the dependence statistic that counts is the one
measured on the series that carries the verdict.

## Why the gate closed, and it closed on the filer's own sentences

**[E3-03] criterion 2 fails in the FY2026 risk factors.** Three classes of close substitute are
named by the registrant: rival new boats, **used boats** (*"We also compete against consumer
demand for used boats"*), and, since May 2026, **its own newly acquired Chaparral** (*"certain of
our Chaparral models compete in the wake and surf category alongside our MasterCraft brand, which
may result in intra-company competition that could affect the sales or pricing of products within
our portfolio"*). Competition is *"based primarily on brand name, price, product selection, and
product performance"* in an industry *"characterized by intense competition"*.

**The competitor row is the strongest evidence in the file.** Gross and operating margin, FY2019
through FY2026, filing-sourced, for **MBUU, BC, MPX, PII, HZO, ONEW** and the subject: **all
seven print their best operating margin in FY2021 or FY2022 and their worst in FY2025 or FY2026,
and four of the seven go negative at the bottom.** Four builders, one diversified powersports
maker, two retailers: one shape. That is **[E3-51]**'s surfing run with the wave visible and
**[E4-36]**'s fourth cause of extreme success, the one that is not ownable. **MCFT lost the most
revenue of anyone in the row**: peak to trough **-59.9%**, against MBUU -41.8%, MPX -38.3%, BC
-23.1%, PII -19.9%, ONEW -8.5%, HZO -5.0%.

**[E4-55], the physical series, is the second-strongest.** MasterCraft brand units **3,596
(FY2022) to 1,639 (FY2026), -54%**; Crest units **3,156 to 716, -77%**; net sales per unit up
**20%** and **24%** over the same span. *"Dollar revenue flattered by pricing is how a shrinking
franchise hides."* And the filer wrote down the Crest brand intangibles by **$10.1 million** in
the fiscal 2026 fourth quarter, eight years after buying it.

**[E4-37]'s inverse metric fires from the risk factors**: *"we have offered and expect to
continue offering dealer incentives to pass through the additional dealer costs to us, which in
turn negatively impacts our margins."* A business with pricing power does not volunteer to pay
its distributor's interest bill. **[E2-58]** is the doctrine that fits, and its one exception, a
cost advantage *"both wide and sustainable"*, is ruled out by the row: **Brunswick out-earns MCFT
on gross margin in every one of the seven comparable years.**

## The refuted priors

- **The brief's prior that MPX would be a comparable: refuted. It is now the subject.**
- **The prior that the `cap_flag` would be a drawdown, as at CALM and EMBC: refuted.** It is a
  units error.
- **The prior that the 2018 name change might be a perimeter event: refuted.** It is cosmetic.
  The real perimeter events are four and none of them is the rebrand.
- **The prior that `newest_filing` being older than `newest_periodic` was an anomaly: refuted.**
  The two columns measure different things (newest annual period end versus newest quarterly
  period end) and the comparison is meaningless. **Both were stale anyway.**
- **My own prior that MCFT would be mid-pack on margin: refuted, and carried at full strength
  [E4-26].** In the downturn MCFT beats Malibu's gross margin by **6.9 points** (22.9% against
  16.0% in FY2026) while running at half of peak volume. It does not carry the gate, because the
  lead did not exist in FY2019-FY2023, because Brunswick beats MCFT every year, and because
  FY2026 still produced a **consolidated operating loss**. But it is a real operating result and
  it is on the record.

## The uncomfortable part, written down rather than hedged

This is a **debt-free** manufacturer with **$43.9 million of cash**, **$381.3 million of book
equity**, a 1968 brand with 90 US patents and 130 trademarks, and a Performance and Wake segment
that earned **$21.5 million of operating income** in the worst retail year of the cycle, trading
at **$482 million**. **[E3-47]** says the omission errors are the expensive ones and *"their
invisibility does not reduce their cost."* If this OUT is wrong, that is where the cost lives,
and the reversal condition is recorded in words at Q6 of the run file rather than as a price
band, because the name failed on the **business** and a band would be the QLYS category error.

## Beneath the close, seen and not scored

The standing [E4-29] instruction from the CGNX run was performed before the gate closed, and the
result is **the inverse of Cognex**: MasterCraft promotes Adjusted EBITDA in **both** the 10-K
and the furnished release. The EX-99.1 of 2026-09-10 headlines *"Adjusted Net Income … $30.2
million, or $1.76 per diluted share"* and *"Adjusted EBITDA margin was 13.1%"* against a **GAAP
loss from continuing operations of $1.6 million, $(0.09) per diluted share** and a **GAAP
operating margin of -0.3%**; the CEO's quoted line is *"these results were earned, not
market-driven"*, which the competitor row contradicts. **The fiscal year end changes from June 30
to December 31 effective 2026-07-01**, announced ahead with a reason, which under [E2-49] is the
candour case rather than the flag but which breaks every multi-year series at 2026-06-30.
Register concentrated: **LOR, Inc. 20.0%, Coliseum Capital 15.2%, Forager 6.0%**, with LOR
holding two of ten board seats under a stockholders agreement. And the Q1 finding that carries
furthest: the **floor-plan repurchase guarantee of $63.5 million, up 55% in the year, reserved at
$1.5 million** on a three-year no-default record, which is **[E4-40]** exactly, *"focusing on
experience, rather than exposure."* **None of it scored; Q3 through Q6 were not opened.**

## Tooling defects found

1. **`wc_note` carries no sign and its heading asserts one.** The flag text says *ONE LINE MADE
   THE CASH*; at MCFT the line **consumed** 62% of the cash. A flag whose prose asserts a
   direction the arithmetic does not carry is a diagnostic that misleads the reader it was built
   to help. **Suggested fix, not applied: emit the signed value, or drop the verb.**
2. **`wc_note` selects the wrong line twice in a row.** At EMBC and again at MCFT the flagged
   line was the **second** biggest working-capital mover. At MCFT the biggest was accrued
   expenses and other current liabilities at **100.1%** of operating cash, against the flagged
   accounts payable at 62.2%. **Suggested fix, not applied: rank all working-capital lines and
   name the largest, or name every line above a threshold.**
3. **The public-float extractor reads dollars as thousands.** MCFT's filed float of $236,100,000
   came through as $236,100M. This is the mechanism behind an entire class of `cap_flag` firings
   and it is separable from the genuine-drawdown class by a single read of the cover page.
4. **`newest_filing` and `newest_periodic` are not comparable and are presented as if they
   were.** One is an annual period end, one a quarterly period end. At MCFT the brief was sent
   to investigate an "anomaly" that is an artifact of the column definitions, while the real
   problem, that both were superseded by a 10-K filed ten days earlier, was not flagged at all.
   **Suggested fix, not applied: carry the newest FILING DATE of any periodic report, not a
   period end.**
5. **The screen's cap is not refreshed after a share issuance.** MCFT's share count rose 48.9%
   on 2026-05-15 and the screen still carried the pre-merger count in September.

## Acceptance test and the pointer

`python tools/check_framework.py` **PASS before the commit**: **311 ledger rows, 311 unique ids**,
source files on disk 311/311, **verbatim against cited source 310/311 OK** with E5-07 declared
not a quote; **1,067 test-run files, 24,075 distinct id citations, 0 phantom citations**;
`THE FRAMEWORK v4.md` 204 ledger ids cited, **0 phantom, 0 unlabelled numbers**; the four other
governing documents likewise 0 and 0. **`CLAUDE.md` still says the ledger is 267 rows; the file
is 311.** The pointer is stale, **the file was counted and not the pointer**, and nothing in
`Framework/`, `CLAUDE.md` or `principle_ledger.csv` was edited by this run. **Fifth consecutive
wave-7 fold to record that stale pointer, which remains the operator's call and not a run's.**
