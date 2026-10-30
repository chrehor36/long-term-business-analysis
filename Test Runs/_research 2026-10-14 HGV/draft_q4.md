## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]** (`tools/run.py` ten-year table, first-filed XBRL, checked against the filed
balance sheets of the FY2019, FY2022 and FY2025 10-Ks and the Q2 2026 10-Q; USD millions):

| Year-end | Total equity | Goodwill | Intangibles | Corporate debt | Non-recourse debt | Cash | Receivables, net | Inventory | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 167 | 0 | 70 | 490 | 694 | 48 | n/r | n/r | 28 |
| 2019 | 570 | 0 | 89 | 828 | 747 | 67 | 1,156 | 558 | 390 |
| 2021 | 1,988 | 1,377 | 1,441 | 2,913 | 1,328 | 432 | n/r | n/r | 357 |
| 2022 | 2,151 | 1,416 | 1,277 | 2,651 | 1,102 | 223 | n/r | n/r | 529 |
| 2024 | 1,895 | 1,985 | 1,787 | 4,601 | 2,318 | 328 | 3,006 | 2,244 | 352 |
| 2025 | 1,440 | 1,985 | 1,670 | 4,545 | 2,716 | 239 | 3,115 | 2,522 | 34 |
| 2026-06-30 | 1,258 | 1,986 | 1,592 | 4,876 | 2,896 | 272 | 3,591 | 2,546 | (101) |

(n/r: not read from the statement for that year in this run.) What moved, and why: equity was built by the Diamond share
issue (2021) and has since been drawn down by buybacks ($272M, $368M, $432M, $600M in 2022 to 2025 and $300M in the first
half of 2026) faster than earnings refilled it, so retained earnings fell from $593M (2023) to a deficit of $101M; the
purchases put $3.6B of goodwill and intangibles on a balance sheet that carried none in 2019; corporate debt rose from
$828M to $4,876M; inventory rose from $558M to $2,546M against contract sales that rose from $1,410M to $3,314M, so
inventory went from about 0.4 to about 0.8 of a year's contract sales. "if some prepaid expense, deferred asset accounts
start building up suspiciously high, and inventories look out of line, you know, with sales [...] you want to look twice"
**[M1995-064]**. Looking twice: the inventory build is explained in the filings (acquired inventory at fair value; $637M
of deferred revenue at 2025-12-31 against sales of units under construction; an inventory pipeline of $14.7B at current
pricing, Item 1), and other assets rose from $410M to $657M in six months of 2026 with an equal deferred-revenue rise
($637M to $864M). Explained, not cleared: the inventory is now a larger claim on the owners' capital than it was.
"what the figures are saying and what they don't say and what they can't say" **[M2025-032]**: the receivables carry a
29% allowance against the originated book, an estimate from static pools; the figures cannot say whether that is enough.

**The real costs.**
- Depreciation and amortization $273M (2025), of which a large part is amortization of purchased intangibles (club
  member relationships, management contracts, trade names); the member relationships deplete as members default and
  leave, so the charge is treated as real here **[R1996-023]**.
- Stock pay $40M / $47M / $64M (2023 to 2025), charged in owner cash **[L2015-003]**.
- Acquisition and integration expense in every year of the window: $106M (2021), $67M, $68M, $237M, $98M (2025), and
  $26M in the first half of 2026: the recurring "one-time" cost, left in **[L2016-007]**.
- The provision for loan losses ($422M deducted from 2025 sales, Item 7) is real; the defaulted loans' cash never comes.
- Securitizations are booked as secured borrowings with no gain on sale (Note 7), which is the conservative treatment.
- **EBITDA in the filer's own mouth.** The MD&A presents EBITDA, Adjusted EBITDA and Adjusted EBITDA Attributable to
  Stockholders ($950M for 2025 against net income attributable to stockholders of $81M); the earnings release gives
  guidance only in Adjusted EBITDA ($1.185B to $1.225B for 2026, 8-K `0001674168-26-000014`) and the CEO is quoted:
  "finishing in the upper half of our guidance range"; pay is set on "Economic Adjusted EBITDA" ($1,152M for 2025, proxy).
  The rows: EBITDA "utter nonsense" **[M1998-086]**, and "I'll look at that figure when you tell me you'll make all the
  capital expenditures" **[M2003-108]**. The 10-K itself lists EBITDA's limitations and says it "should not be considered
  as discretionary cash available to us" (Item 7).
- **Internal control.** Material weaknesses at 2022-12-31 (Diamond) and 2023-12-31 (IT access over a revenue and
  inventory application), both remediated; unqualified opinion on internal control at 2025-12-31 (Item 1A, Item 8).

**Owner cash, recast** (feeds Q7). OCF less stock pay less all capital spending (property and software), **plus the net
non-recourse borrowing** of the year. **CONVENTION of this run:** the non-recourse debt is treated as the finance arm's
working capital, by extension of Q7's convention on inventory-secured trade finance to receivable-secured non-recourse
debt; rationale: it is secured by the receivables and repaid as they collect, its interest is already charged inside
owner cash (consumer financing interest, in the financing segment), and the speakers keep a finance arm apart from the
operations **[L2008-005]** and fund such a book "almost entirely with debt" **[L2003-019]**; the alternative with the
non-recourse debt counted in net debt is shown beside at Q7. USD millions:

| Year | OCF | Net non-recourse borrowing | Stock pay | Capital spending | Owner cash (equity) | Corporate interest | Owner cash before corporate interest, after tax |
|---|---|---|---|---|---|---|---|
| 2021 | 168 | (95) | 48 | 39 | (14) | 105 | 64.75 |
| 2022 | 747 | (221) | 46 | 97 | 383 | 142 | 489.5 |
| 2023 | 312 | 174 | 40 | 75 | 371 | 178 | 504.5 |
| 2024 | 309 | 259 | 47 | 126 | 395 | 329 | 641.75 |
| 2025 | 300 | 404 | 64 | 146 | 494 | 311 | 727.25 |

(Cash flow statements of the FY2022 and FY2025 10-Ks; the interest shield at 25%, a **CONVENTION of this run**: the 21%
federal statutory rate plus state, which the 2025 reconciliation shows at 12 points that year and the 2023 one at about
4; rationale: a single marginal rate for the add-back, not the year's effective rate. Acquisitions are kept out of
these lines and handled at Q7.)

- **VERDICT on the accounts: WEIGHS AGAINST, no STOP.** The statements can be followed and reconciled; nothing in them
  confuses on a second reading **[M1995-063]**: the construction deferrals and the allowance are tabled, the inventory
  build is explained, the securitizations take no gain. Against: the featured adjusted figure, the guidance and the pay set
  on it, the recurring integration charges, two years of material weakness, and inventory and deferred accounts rising
  faster than sales **[M1995-064]**. Preoccupation with presentation is "a negative" but not "a total exclusionary factor"
  **[M1994-018]**; the habits are carried to Q5. *(The Q4 text also carries the EBITDA count, "about zero" **[M2002-026]**,
  as part of why confusion is a STOP; this run reads it under the 2026-10-06 convention that sends a featured adjusted
  figure to Q5; see "What in the framework was wrong or unclear".)*
