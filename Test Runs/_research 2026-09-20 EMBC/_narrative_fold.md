
# EMBC (Embecta Corp.) - Q2 OUT on the business. Wave 7, name 7, register entry 139. 2026-09-20

Run file: `Test Runs/2026-09-20 Run - EMBC Embecta.md`. Research:
`Test Runs/_research 2026-09-20 EMBC/`. Seventh and last of the wave-7 file, and the third name
of the day after CALM and HESM.

## The verdict in one paragraph

**Q1 IN, Q2 OUT, on the business, permanently.** Embecta sells disposable insulin pen needles
and syringes, about $1.08bn of revenue, spun out of Becton, Dickinson on 2022-04-01. The file
closes at Q2 because **[E3-03]** criterion 2 fails on the company's own filed words. The FY2025
10-K's MD&A carries the filer's own headings **"Commoditization of Injection Devices"** and
**"Pricing Pressures"**, and a third, **"Changes in Clinical Practice"**, which says in the past
tense that GLP-1s, SGLT-2s and once-weekly insulin *"have delayed initiation of insulin therapy
and contributed to less demand for our products"* while developed-market insulin therapy
*"continues to transition to infusion pumps"*. A company that files that its category is
commoditized and that substitutes have already taken its demand has answered criterion 2 itself.

## The measurement, and it is the price and volume bridge

Most Q2 OUTs in this project are arguments about position. This one is arithmetic the filer
publishes. The price/volume/FX bridge, verbatim from the filings:

| period | volume | price | source |
|---|---|---|---|
| FY2025 vs FY2024 | **-$52.9M** | +$2.0M | 10-K FY2025 MD&A, `0001872789-25-000036` |
| 9M FY2026 vs 9M FY2025 | **-$60.0M** | **-$27.4M** | 10-Q Q3 FY2026 MD&A, `0001872789-26-000033` |
| Q3 FY2026 vs Q3 FY2025 | **-$19.9M** | **-$20.1M** | same 10-Q |

**$20.1M of price given back in one quarter is 7.4% of that quarter's $271.7M of revenue.**
**[E2-44]**'s two-characteristic test asks whether the business can raise price when demand is
flat; demand is falling and price is falling with it. **[E4-37]**'s inverse metric asks about
*"the agony they go through in determining whether a price increase can be sustained"*; there is
no agony on the record because there is no price increase.

**[E4-55]**'s physical read is the same story: Pen Needles $596.3M to **$517.6M (-13.2%)** over
nine months, United States revenue $437.1M to **$347.1M (-20.6%)**, and the Q3 release reports
*"U.S. revenues decreased 24.6%"*. Gross margin 66.9% (FY2023), 62.6% (FY2025), **58.7%** (9M
FY2026).

## The [E4-04] finding: the brand is being rebuilt from zero, and it was never theirs

The framework's scope test for **[E4-04]** asks whether spending **defends the same advantage or
buys its replacement**. Coca-Cola's advertising defends a trademark it owns; Mitsui's Rhodes
Ridge buys a replacement deposit. Embecta's is unambiguously the replacing case, and the filing
says so: the 100-year brand is BD's, held under *"a temporary license"*, and *"While we have
officially launched our brand transition from the "BD" name and logo in the U.S. and Canada"*,
the new marks *"may not benefit from the same recognition and association with product quality as
the BD name"*.

**The transition launched in the United States first. United States revenue then fell 20.6% in
the following nine months.** The run does not claim the filing proves causation. It records what
it is: the named risk, followed by the matching outturn, in that order, in the one segment where
the change had already happened.

**The other candidate scarce input is also BD's.** Item 1, Raw Materials and Components: *"**BD
retained ownership of all cannula production activities and the associated intellectual property
rights** of BD and its subsidiaries relating to cannula, the manufacture thereof and other
critical cannula-related technology."* The cannula is the hard part of a pen needle. So the
registrant owns neither the needle's core technology nor the name on the box, and the 39.4% net
margin it printed in FY2020 was **[E3-51]**'s surfing run under a parent's brand and cost base.
Ask **[E4-36]** which of the four causes of extreme success the record came from, and the answer
is wave-riding, which is the one that is not ownable.

## The tooling finding: the screen's 4.151x band spread is the spin, not volatility

**This is the most transferable thing in the run.** The screen row published owner earnings of
**$35M to $181M, a spread of 4.151x**, with `level_shift`, `level_shift_oe`, `window_disagree`
and a `spread_caveat` ordering an **[E4-25]** rebuild. Rebuilt by hand from the filed statements
(`_research 2026-09-20 EMBC/oe_rebuild.py`; headed **COMPUTATION - NOT A CLEARANCE** in the run
file, because Q5 never opened):

| window | mean OCF | mean SBC | (c) = D&A | (c) = capex | OE at capex end | OE at D&A end |
|---|---|---|---|---|---|---|
| FY2023-FY2025, 3y, **standalone only** | 98.4 | 26.5 | 36.5 | 17.2 | **54.7** | **35.4** |
| FY2022-FY2025, 4y, includes the stub year | 176.8 | 24.5 | 35.3 | 18.8 | 133.5 | 117.0 |
| FY2021-FY2025, 5y, **the corpus default [E2-42]** | 232.7 | 22.2 | 35.9 | 22.4 | 188.1 | 174.6 |
| FY2020-FY2025, 6y, everything filed | 277.0 | 20.6 | 36.3 | 25.7 | 230.8 | 220.1 |

**$35M is the three-year standalone window at the D&A end. $181M sits inside the five-year
window.** The band is not a measure of how volatile this business is. **It is the distance
between two different companies**: Embecta Corp., carrying $1.4bn of spin debt and $107.3M of
annual interest, and the Diabetes Care Business of Becton, Dickinson and Company, carrying
neither. The FY2022 10-K warned the reader in Note 1: *"The Consolidated Financial Statements
did not purport to reflect what the Company's results of operations … would have been had the
Company operated as a standalone public company during the periods presented."*

**And the [E4-25] rebuild cannot be performed in the direction the caveat assumed.** The caveat
says the four-construction width *"CANNOT see variation older than the 5-year window; rebuild
it"*. Rebuilt, the finding is that **there is no older window to see.** Before FY2023 there is no
standalone company. The corpus's five-year default **[E2-42]** is **unavailable on this
registrant**, and the honest window is three years.

**The transferable rule, for every spin-off in the queue:** where `name_change_note` fires and
the entity is a spin, **the band width and the level-shift flags are measuring the spin boundary
before they measure anything about the business.** Check the first standalone fiscal year before
reading any owner-earnings band on such a row. The BE run named the "too little filed history"
shape (HHH's shape); this is its twin, and it is worse, because here the history *looks* long.

## The `wc_note` fired correctly and pointed at the second-biggest line

Flagged: `AccountsPayableAndAccruedLiabilities moved 168% of 2024 OCF`. It reproduces exactly:
FY2024's *"Accounts payable, accrued expenses and other current liabilities | 60.0"* against
$35.7M of operating cash is 168%. **But FY2024's *"Trade receivables, net | ( 174.7 )"* is 489%
of the same denominator**, and FY2025's $191.7M of operating cash carries its partial reversal
plus **$63.2M of receivables sold** under an agreement entered *"during the third quarter of
fiscal year 2025"*. Operating cash is not owner earnings in either year. The flag's 30%
threshold did its job; its pointer picked the smaller of two qualifying lines. **Not a bug, and
not worth a tool change:** the flag is a prompt to read, and a reader who follows it to the
cash-flow statement sees both lines at once.

## The competitor row, and why three of six were enough

3 of 6 real competitors, same metric, same window, filing-sourced. Insulet **+59.6%** (gross
margin 68.3% to 71.6%), Tandem Diabetes **+35.7%** (49.2% to 53.8%), Novo Nordisk **+33.1%**,
against **Embecta -3.6%** with gross margin falling 4.3 points and then 3.9 more. Insulet and
Tandem are precisely the modality the subject's own MD&A says developed-market therapy
*"continues to transition to"*, so **the substitution is measured on both sides of the trade**,
which is rarer than it sounds: most Q2 OUTs can show only the subject's side.

Terumo (rung 3, **HTTP 403**), Ypsomed (rung 3, **HTTP 404**) and MTD Group (no public filings on
any rung) are unavailable and are named as such with the obstacle. **They do not make the class
PROVISIONAL**, and the reasoning is worth recording because it will recur: the PROVISIONAL rule
exists so that a missing peer cannot be used to *establish* a moat. Here the class is **NONE**,
established from the subject's own filings, and the three missing names are exactly the *"existing
and new local and regional low-cost providers"* the subject blames for its price cuts. Their
filings could only deepen the finding. **No gate in this file is marked IN carrying a
PROVISIONAL caveat**, which is the protocol violation the rule actually guards against.

## Beneath the close, seen and not scored

Q3 and Q4 were not opened. The standing CGNX instruction was performed anyway.

- **[E4-29].** Adjusted EBITDA seven times in each of the Q3 FY2026 and FY2025 EX-99.1 releases,
  with GAAP shown beside adjusted on every highlight line (better than most) but **no
  quantitative reconciliation of forward guidance**.
- **The proxy makes it the pay system.** DEF 14A `0001140361-25-046025`: the bonus plan is *"80%
  Financial Metrics (40% Adjusted Constant Currency Revenue $, 40% Adjusted EBITDA $)"*, and it
  funded at **110.2% of target** for FY2025, a year in which reported revenue fell 3.8% on
  falling volume and the equity fell about 63%. **[E4-27]**: *"Never, ever, think about something
  else when you should be thinking about the power of incentives."* The counterweight is recorded
  too: the Committee applied **negative discretion** to strike the Net Debt Focus Plan even
  though *"The Net Debt target was also exceeded"*.
- **[E5-08] and [E4-31].** In the single month of May 2026 the board cut the quarterly dividend
  from **$0.15 to $0.01**, authorised a **three-year $100M buyback**, and closed a **£100M cash
  acquisition part-funded by a revolver drawdown**. It then bought 2.7M shares for $8.7M, about
  $3.22 each. **[E5-25]** shows what real compliance with the two conditions looks like: numbers
  published in advance. None are published here.
- **[E5-11] strength 3, which is the one that usually kills.** $1.469bn of debt principal at
  2026-06-30 against $218.2M of cash, rated **B1 / B+**, with a **$500M revolver maturing 2027**
  now carrying $129.9M drawn, Term Loan B $716.8M to March 2029, $700M of secured notes to
  February 2030, and a **total net leverage covenant tested quarterly on EBITDA** while the
  filer's own Adjusted EBITDA fell **23.9%** over the nine months to 2026-06-30. Had Q4 opened,
  **[E2-54]**'s coverage test and **[E5-39]**'s *"kindness of strangers"* would have been run
  here. **Total Equity is negative $650.6M**, so **[E2-01]**'s book denominator is unusable and
  **[E2-43]**'s unleveraged net tangible assets is the one the corpus supplies.

## Three screen cells refuted at source, and one confirmed twice in one day

1. **`deal_note`'s first branch is wrong.** Embecta is the **acquirer**, not the target. The
   EX-2.1 is the purchase of Owen Mumford Holdings Limited from six private individuals for
   £100M cash plus up to £50M of milestones, **closed 2026-05-15** (Item 2.01,
   `0000947871-26-000546`), with acquiree accounts in the 8-K/A `0001872789-26-000026`. **Not a
   merger spread.** Third wave-7 name in a row where this note pointed at the wrong branch or the
   wrong instrument.
2. **`cap_flag`'s premise is wrong and the flag is right.** Neither input is broken. Float $732M
   at 2025-03-31, cap $299.7M at 2026-09-18, and the share price fell about 63% in between.
   **Second confirmation in one day of CALM's drawdown-detector reading.** Two independent
   confirmations on one day is enough to treat this as the flag's *primary* meaning rather than
   an exception: **read `cap_flag` as a drawdown detector first and a data error second.**
3. **`name_change_note`'s odds description is right and its shape guess is wrong.** It is a real
   perimeter event, but a **spin-off registration shell**, not a reverse merger or de-SPAC, and
   the break is at FY2022 rather than at the 2021 name change.
4. **`wc_note` fires correctly on the second-biggest line** (above).

## The uncomfortable part, written down rather than hedged

**The current returns are good and the run should not be read as saying otherwise.** Operating
income of $242.1M on roughly $0.7bn of unleveraged net tangible assets is a pre-tax return in the
low thirties. Gross margin, even after two years of decline, is 58.7%. Capital spending is under
1% of sales. Had **[E4-20]** been reached it would not have called this gruesome.

**The file closed at Q2 for one reason: direction.** **[E4-32]** makes the moat *widened every
year* the primary criterion of a great business, and here every filed metric narrows at once:
units, price, gross margin, geography, and the ownership of the brand itself. **[E2-58]** explains
why a high current return in a commoditizing category is not evidence of durability, and the
filer disclaims **[E2-58]**'s only exception in its own Pricing Pressures paragraph.

**The honest counterweight, because [E4-26] runs both ways.** International revenue **grew** 7.5%
over the nine months while the United States fell 20.6%, the Owen Mumford acquisition brings a
genuinely different asset (an auto-injector platform sold to pharmaceutical partners rather than
a commodity consumable sold to distributors), and the Q3 release notes that *"our GLP-1 B2B
partners launched generic GLP-1 therapies co-packaged with our pen needles in Canada and
Brazil"*, which is an attempt to sell into the substitute rather than against it. **None of that
reverses a Q2 that failed on the core product's filed price and volume.** It is the reversal
condition, and it is recorded in words: two consecutive periods in which the bridge shows
favourable price, with pen needle revenue and United States revenue both growing, on a perimeter
that excludes Owen Mumford. **No price band is armed and no `PORTFOLIO.md` row is added**,
because the name failed on the business and a band would be the QLYS category error.

## Acceptance test and the pointer

`python tools/check_framework.py` **PASS before the commit**: 311 ledger rows, 311 unique ids,
**verbatim against cited source 310/311 OK** with E5-07 declared not a quote; 1,064 test-run
files, 23,945 distinct id citations, **0 phantom citations**; `THE FRAMEWORK v4.md` 204 ledger
ids cited, 0 phantom, 0 unlabelled numbers. **All 45 distinct ledger ids cited in the EMBC run
were checked to exist in `principle_ledger.csv` before they were written**, with the file opened
`encoding="utf-8-sig"`. **`CLAUDE.md` still says the ledger is 267 rows; the file is 311.** The
pointer is stale, **the file was counted and not the pointer**, and nothing in `Framework/` or
`CLAUDE.md` was edited by this run. **Fourth consecutive wave-7 fold to record that same stale
pointer, which remains the operator's call and not a run's.**
