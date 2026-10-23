
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (USD millions; `tools/run.py` first-filed
  XBRL vintage, transcription, with materials and supplies from the filed balance sheets; accessions
  `0000065984-17-000067` through `0000065984-26-000174`, listed by the tool).

| year-end | assets | equity | cash | goodwill | LT debt (non-current) | debt on the face (sum)* | retained earnings | materials and supplies |
|---|---|---|---|---|---|---|---|---|
| 2016 | 45,904 | 8,082 | 1,188 | 377 | 14,468 | 14,833* | 8,196 | 698.5 |
| 2017 | 46,707 | 7,993 | 781 | 377 | 14,315 | 16,654* | 7,978 | 723.2 |
| 2018 | 48,275 | 8,844 | 481 | 377 | 15,518 | 18,111* | 8,721 | n/r |
| 2019 | 51,724 | 10,224 | 426 | 377 | 17,079 | 19,820* | 9,258 | 825.0 |
| 2020 | 58,239 | 10,926 | 1,759 | 377 | 21,206 | 23,997* | 9,897 | n/r |
| 2021 | 59,454 | 11,637 | 443 | 377 | 24,842 | 27,082* | 10,241 | 1,041.5 |
| 2022 | 58,595 | 12,967 | 224 | 377 | 23,624 | 26,760* | 10,502 | 1,183.3 |
| 2023 | 59,703 | 14,623 | 133 | 374 | 23,009 | 26,246* | 11,940 | 1,419.0 |
| 2024 | 64,790 | 15,084 | 860 | 368 | 26,614 | 28,919* | 12,014 | 1,631.1 |
| 2025 | 71,891 | 16,923 | 1,929 | 368 | 27,902 | 30,935* | 12,698 | 1,710.4 |

  *non-current and current long-term debt plus short-term borrowings as tagged; the tool marks every year a partial sum
  (finance leases and some lines untagged). n/r = not read. 2026-06-30 (10-Q): total assets $79,003M, equity $18,229M, debt
  $34,627M, cash $3,854M.

  **What moved and why.** Assets rose $26.0B in nine years and equity $8.8B, of which retained earnings $4.5B (after the
  2016 to 2017 losses on the merchant-nuclear exit) and the rest new stock (Q3). Debt on the face roughly doubled, from $14.8B
  to $30.9B; the MD&A's debt-to-capital ratio was 69.5% at end-2018 and 66.9% at end-2019 (FY2019 10-K), 63.8% at end-2023,
  65.3% at end-2024 and 64.3% at end-2025 (FY2024 and FY2025 10-Ks), against a credit-facility covenant of "65% or less of its
  total capitalization", calculated differently (Item 7). Goodwill flat at $368M to $377M: the growth was built, not bought.
  Cash is a parking place between financings (lowest $133M at end-2023, $3,854M at mid-2026 after debt and stock were raised
  ahead of spending). Materials and supplies rose from $698.5M to $1,710.4M; set against the spending they serve (cash
  construction spending of $2.78B in 2016 and $7.68B in 2025, FY2016 and FY2025 cash-flow statements) they fell from about
  25% to 22% of a year's construction, so the balance does not look out of line with the business **[M1995-064]**. What the
  balance sheet cannot say: what $5.0B of regulatory assets will in fact be collected, and what the off-balance-sheet build of
  the Legend Power Station will cost (below).
- **Owner cash, recast from the filed cash-flow statements** (USD millions; `calc.py` in the research folder; operating cash
  plus all investing lines plus the storm-securitization trust proceeds, less stock pay; before any borrowing):

| year | operating cash | investing (all) | storm trust proceeds | stock pay | owner cash before borrowing | net borrowing (long-term + commercial paper) | OCF less D&A less stock pay |
|---|---|---|---|---|---|---|---|
| 2021 | 2,300.7 | -6,179.3 | 0 | 62.6 | -3,941.2 | 3,054.3 | -4.8 |
| 2022 | 2,585.5 | -5,709.9 | 3,163.6 | 63.8 | -24.6 | -349.6 | 331.3 |
| 2023 | 4,294.3 | -4,629.0 | 1,457.7 | 58.2 | 1,064.8 | -551.9 | 1,991.6 |
| 2024 | 4,488.5 | -5,849.0 | 0 | 63.0 | -1,423.5 | 2,634.0 | 1,981.9 |
| 2025 | 5,150.7 | -7,109.5 | 0 | 65.2 | -2,024.0 | 1,979.1 | 2,548.3 |
| mean | 3,763.9 | -5,895.3 | 924.3 | 62.6 | -1,269.7 | 1,353.2 | 1,369.7 |

  Sources: FY2022 10-K (`0000065984-23-000014`) for 2021 and 2022, FY2025 10-K (`0000065984-26-000174`) for 2023 to 2025;
  stock pay from Note 12 of each. **CONVENTION of this run:** the storm-securitization proceeds (financing activities, 2022
  and 2023) are counted as owner cash, because the bonds are "the obligation of the LCDA" and Entergy and Entergy Louisiana "do
  not report the bonds [...] on their balance sheets" (Note 2), while the storm costs they recover were paid inside the same
  window (2020 to 2021 storms); rationale: counting the cost and not its recovery would charge the storms twice. Customer
  advances for construction (financing, $1,474M net over 2023 to 2025) are not counted and are shown beside at Q7: the filing
  says they are "recognized as revenue as the related costs are incurred" (Note 1), so they are the customer's money owed back
  in kind.
- **The real costs.** Depreciation, decommissioning and nuclear fuel amortization are real and are inside the "OCF less D&A"
  column **[L2015-004]**; stock pay is deducted in full, expensed and capitalized **[L2021-003]**; the pension settlement
  charge of $320M in 2024 and contributions ($897M of pension and postretirement funding-status changes in 2021, cash-flow
  statement) are inside operating cash. Two items flatter GAAP earnings against cash: the allowance for equity funds used during
  construction, a non-cash credit to income of $181M in 2025 (income statement), and "Other regulatory charges (credits) - net"
  of -$162M in 2025. The Legend Power Station is being built for Entergy Texas by investors at up to $1.45B under a
  build-to-suit lease that the auditor made a critical audit matter, because the company "is not the deemed accounting owner
  of the Facility during the construction period" (auditor's report, FY2025): a plant Entergy will control from 2028 is off
  the balance sheet while it is built. Weighed, not a STOP: the filing says what it is and what it will cost.
- **EBITDA in the filer's own mouth:** not used; the company's credit measure is "Adjusted FFO/Debt" (proxy). **The featured
  figure and the habit.** The company guides on and features "ETR Adjusted EPS", "the earnings measure by which we provide
  external guidance" (proxy, `0000065984-26-000211`), and its 8-Ks strip the real costs of regulation out of it: the $132M
  write-off when a federal court upheld the APSC "will be considered an adjustment and excluded from Entergy’s adjusted
  earnings (non-GAAP) and does not impact Entergy’s adjusted earnings per share outlook" (8-K 2024-03-12); the $78M increase in
  Entergy New Orleans's customer credit "will be considered an “adjustment” [...] and therefore will not affect Entergy’s
  adjusted earnings per share" (8-K 2024-04-18, `0000065984-24-000039`); the SEC settlement 8-K "affirms its previously
  published adjusted earnings per share and credit outlooks" (8-K 2024-12-20, `0000065984-24-000131`). And: "Our adjusted
  earnings per share was in the top half of our guidance range set at the beginning of the year, as it has been consistently
  for the past ten years." (proxy). The rows: "a management that regularly attempts to wave away very real costs by
  highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; "we become downright incredulous if they
  consistently reach their declared targets" **[L2002-041]**; telling owners "year after year, "Don't count this,"" is
  misleading **[L2016-007]**. Refunds ordered by regulators are not one-time costs for a utility; they recur in this record
  (2022, 2024). Under the convention of section A of the gaps case, recorded here as a WEIGHING against **[M1994-018]** and
  carried to Q5.
- **What the accounts say of the books.** FY2025 10-K Item 9B: the SEC's Division of Enforcement investigated "Entergy’s
  processes and controls relating to its accounting for materials and supplies inventory"; in December 2024 "Entergy consented
  to the entry of an injunction, paid a $12 million civil penalty", "neither admitted nor denied the SEC’s allegations", and
  "agreed to engage a consultant"; the consultant's follow-up audit is due December 2026. The company says its enhanced
  controls "did not result in a material change in the value of its materials and supplies inventory" (8-K 2024-12-20). The
  balance itself does not look out of line (above), so the statements raise no suspicion of their own **[M1995-064]**; the
  books-and-records finding is carried to Q5.
- **VERDICT on the accounts: no STOP; WEIGHS AGAINST.** Not confusion: regulatory accounting is dense, but each item here
  (securitization, customer advances, the build-to-suit lease, AFUDC) is explained in the filing and was traced to cash
  **[M1995-063]**. Not suspicion raised by the statements themselves **[M1995-065]**. Against: the adjusted figure featured and
  the decade of targets met **[L2016-006]**, **[L2002-041]**, and an injunction on books and records; both carried to Q5. The
  recast owner cash feeds Q7.
