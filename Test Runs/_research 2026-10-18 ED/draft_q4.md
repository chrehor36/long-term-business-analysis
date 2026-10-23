
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintage, $M; checked against
the filed balance sheets for 2018 and 2019, 10-K FY2019: total assets $53,920M and $58,079M, long-term debt $17,495M and
$18,527M, common equity $16,726M and $18,022M, all equal; and for 2024 and 2025, 10-K `0001047862-26-000031`: total assets
$70,562M and $74,603M, equity $21,962M and $24,190M, equal; long-term debt for 2024 is $24,651M in the FY2025 10-K against
$24,710M first filed, a reclassification of $59M. Revenue from the filed income statements.)

| Year-end | Total assets | Common equity | Cash | Customer and other receivables | Goodwill | Intangibles | Long-term debt | Revenue |
|---|---|---|---|---|---|---|---|---|
| 2016 | 48,255 | 14,298 | 776 | 1,106 | 428 | 124 | 14,735 | 12,075 |
| 2017 | 48,111 | 15,418 | 797 | 1,103 | 428 | 131 | 14,731 | 12,033 |
| 2018 | 53,920 | 16,726 | 895 | 1,267 | 440 | 1,654 | 17,495 | 12,337 |
| 2019 | 58,079 | 18,022 | 981 | 1,236 | 446 | 1,557 | 18,527 | 12,574 |
| 2020 | 62,895 | 18,847 | 1,272 | 1,701 | 446 | 1,460 | 20,382 | 12,246 |
| 2021 | 63,116 | 20,037 | 992 | 1,943 | 439 | 1,293 | 22,604 | 13,676 |
| 2022 | 69,065 | 20,687 | 1,282 | 2,192 | 408 | 0 | 22,439 | 15,670 |
| 2023 | 66,331 | 21,158 | 1,189 | 2,418 | 408 | n/a | 21,989 | 14,663 |
| 2024 | 70,562 | 21,962 | 1,324 | 2,440 | 408 | n/a | 24,710 | 15,256 |
| 2025 | 74,603 | 24,190 | 1,629 | 2,583 | 406 | n/a | 25,551 | 16,918 |

What moved and why. (1) Equity rose $9,892M in nine years, long-term debt $10,816M: the two grew together, as a regulated
capital structure near 48 percent equity requires (the 10-K's own table: Con Edison 47.1 to 50.9 percent, CECONY 46.0 to 47.9
percent of capitalization, 2021-2025). (2) The intangibles of $1,654M that appear in 2018 are the renewable projects the Clean
Energy Businesses bought; they leave with the 2022 reclassification as held for sale and the 2023 sale. Goodwill is small and
flat. (3) Receivables rose 134 percent while revenue rose 40 percent: the "inventories look out of line" tell **[M1995-064]**
in a utility's form. The filer explains it in full (Item 7, Aged Accounts Receivable Balances): customer receivables of
$2,970M at CECONY at 2025-12-31 against $1,322M at 2020-02-28, of which $1,427M older than 60 days against $408M, after the
pandemic suspension of terminations and slower collection since, with write-offs reconciled to rates under caps "that produce
no more than a half percent (0.5 percent) total customer bill impact". It is explained and disclosed; it is not a profit that
may not exist, but a customer base paying more slowly (carried to Q2, test 10). (4) Cash stays near $1 to $1.6B against
$1.2 to $1.6B a year of dividends: the business holds no reserve of its own and lives on the capital markets (Q9). (5)
Retained earnings, tagged only for 2024 and 2025 ($14,048M, $14,857M), rose $809M in 2025 while $1,308M of new shares were
sold. What the figures cannot say **[M2025-032]**: whether the regulatory assets on the balance sheet will be recovered,
which depends on orders not yet written, the largest open one being the tax matter below.

**The real costs.**
- Depreciation and amortization $2,321M in 2025 (filed statement), counted in full **[R1996-023]**; cost of removal less
  salvage ($481M in 2025) is a cash cost of retiring plant that `tools/run.py` leaves out of its capital spending and that this
  run counts with the capital spending.
- Stock pay ($35M to $64M a year, 2021-2025) is deducted **[L2015-003]**.
- No EBITDA anywhere in the 10-K, the earnings presentation or the proxy (a text search returns none).
- Pensions: the rate plans reconcile pension and retiree costs to the amounts in rates (Note B), so the pension book is the
  customers' cost more than the owners'; the cash contributions run through operating cash.
- **The income-tax audit.** "In January 2018, the NYSPSC issued an order initiating a focused operations audit of the
  Utilities’ financial accounting for income taxes. The audit is investigating the Utilities’ inadvertent understatement of a
  portion, the amount of which may be material, of their calculation of total federal income tax expense for ratemaking
  purposes" (10-K Note B, Other Regulatory Matters). The result is an income-tax regulatory asset of $1,049M at CECONY and
  $10M at O&R at 2025-12-31, "which are not earning a return", whose recovery depends on a private letter ruling not yet
  sought. Eight years open. Disclosed plainly, with the amount; the open risk is a write-down of up to about $1.06B, some
  $2.86 a share before tax effects, carried to Q7 as a reason the range is not narrower and to Q5 as part of the record.
- **Operating cash is moved by deferrals.** The line for deferred charges and regulatory assets took $496M, $870M, $1,216M,
  $797M and $721M out of operating cash in 2021-2025 (filed cash-flow statements): costs paid now and collected later. Owner
  cash is therefore averaged over five years and not read from one year **[L2005-003]**.

**The recast owner cash, equity-only basis** (Q7, The regulated utility; $M; Clean Energy Businesses removed using the
segment cash-flow and depreciation figures in the 10-Ks; the computation in `q7.py`, output in `q7_output.txt`):

| | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|
| Operating cash (after interest and tax) | 2,558 | 3,429 | 2,156 | 3,614 | 4,800 | 3,311 |
| less stock pay | 35 | 64 | 53 | 35 | 55 | 48 |
| less depreciation (the maintenance guess) | 1,801 | 1,878 | 2,031 | 2,155 | 2,321 | 2,037 |
| **= owner cash after maintenance only** | 722 | 1,487 | 72 | 1,424 | 2,424 | **1,226** |
| capital spending with removal and transmission | 3,983 | 4,226 | 4,789 | 5,273 | 5,295 | 4,713 |
| Utilities' net long-term debt raised (credited, below the 52 percent cap) | 1,685 | 800 | 2,050 | 2,500 | 1,150 | 1,637 |
| **= owner cash after all spending, debt credited** | 225 | -61 | -636 | 806 | 600 | **187** |

The debt credit: CECONY's issuance less retirements from its own filed cash-flow statements (2,250 less 640; 700; 2,000;
2,850 less 475; 900); O&R's issuance as the 10-Ks state it (about 75, 100, 50, 125, 250), its small retirements not
separated, so the O&R figure is an upper bound (flagged). The cap: the allowed debt share is 52 percent (the 48 percent
equity ratio of every NYSPSC plan above), applied to utility capital spending of $23,343M, $12,138M; the credit of $8,185M is
below it. Against net income for common of $1,346M to $2,023M (2021, 2022, 2024, 2025), owner cash after all spending is a
small fraction: the reported earnings are reinvested and more, the case **[L2023-009]** describes, cash that "will regularly
fall considerably short" of reported earnings.

**Guidance and the adjusted figure.** The earnings presentation leads with "$5.66 earnings per share (GAAP) / $5.70 adjusted
earnings per share (non-GAAP) - top end of guidance for the year", introduces "$6.00 to $6.20 2026 adjusted earnings per share
(EPS) guidance range (non-GAAP)", and claims "Consistently delivering actual adjusted EPS growth rates in excess of guidance"
(8-K `0001047862-26-000028`). The rows: "we become downright incredulous if they consistently reach their declared targets"
**[L2002-041]**; "a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share
earnings" makes us nervous" **[L2016-006]**; earnings guidance **[L2019-006]**. Here the adjusted and GAAP figures differ by
four cents, and the five-year adjusted growth (6.4 percent) is stated below the GAAP growth (11.46 percent), so the adjusted
figure is not used to flatter growth. Recorded as a WEIGHING against and carried to Q5 (Q4, The make-the-numbers habit).

- **VERDICT on the accounts: WEIGHS AGAINST, no STOP.** The accounts are readable and explain their own oddities (the
  receivables, the deferrals, the tax asset); nothing confuses or raises suspicion in the statements themselves
  **[M1995-063]**, **[M1995-065]**. Against: owner cash after all spending is a fraction of reported earnings **[L2023-009]**,
  the eight-year-old tax audit leaves a $1.06B asset in doubt, and guidance with an adjusted figure is featured
  **[L2002-041]**, **[L2016-006]**, carried to Q5. The recast figures above feed Q7.
