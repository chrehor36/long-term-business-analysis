## STEP 0 (continued) — THE BALANCE SHEETS, TEN YEAR-ENDS, READ BEFORE THE INCOME ACCOUNT
Read because the dispatch asks for them in Step 0 when the file closes before Q4, and because the framework asks for
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. The table is
`tools/run.py`'s first-filed XBRL transcription for equity, goodwill, intangibles and debt, with the lease and
financing-obligation lines taken from the filed balance sheets (10-Ks FY2016, FY2018, FY2020 to FY2025; 10-Q Q2 2026).
USD millions, year-ends.

| Year-end | Equity (PENN) | Goodwill + intangibles | Debt (book) | Financing obligations | Operating lease liab. | Finance lease liab. | Debt + all lease-type liab. | Cash | Accumulated deficit |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | -543 | 1,425 | 1,416 | 3,514 | n/a (pre-ASC 842) | n/a | 4,930 | n/r | n/r |
| 2018 | 731 | 3,085 | 2,453 | 7,148 | n/a (pre-ASC 842) | n/a | 9,602 | 480 | -968 |
| 2019 | 1,853 | 3,297 | 2,419 | 4,143 | 4,575 | 226 | 11,363 | 437 | 162 |
| 2020 | 2,656 | 2,671 | 2,432 | 4,132 | 4,493 | 219 | 11,276 | 1,854 | -507 |
| 2021 | 4,098 | 4,695 | 2,841 | 4,097 | 4,454 | 317 | 11,709 | 1,864 | -86 |
| 2022 | 3,598 | 4,428 | 2,818 | 4,034 | 1,047 | 5,050 | 12,949 | 1,624 | 154 |
| 2023 | 3,202 | 4,313 | 2,798 | 2,427 | 4,246 | 2,103 | 11,574 | 1,072 | -336 |
| 2024 | 2,863 | 4,093 | 2,797 | 2,387 | 3,976 | 2,116 | 11,276 | 707 | -647 |
| 2025 | 1,834 | 3,191 | 2,904 | 2,344 | 3,978 | 2,063 | 11,289 | 687 | -1,490 |
| 2026-06-30 | n/r | n/r | 2,800 (principal, MD&A) | 2,321 | 3,904 | 2,063 | about 11,090 | 887 | n/r |

(n/r = not read for this run. The 2017 year-end was not read. The 2019 "retained earnings" of 162 is the first-filed XBRL
value printed by `tools/run.py`; the 2018 and 2025 figures were checked against the filed balance sheets.)

What the figures are saying, and what they are not:
- **The claim ahead of the owners has not shrunk in seven years.** Debt plus every lease-type liability has sat between
  $11.3B and $12.9B at every year-end since 2019; the accounting has moved the same rent between three lines (financing
  obligation, finance lease, operating lease) as the leases were amended in 2022 and 2023, which is why any single line
  jumps. Against a market value of about $2.0B the owners hold a thin slice on top of a long, escalating claim.
- **Equity rose only when shares were sold, and fell back.** $1,288.8M of common stock was sold in 2020 and theScore was
  paid for partly in 12.3 million shares in 2021 (10-Ks FY2020, FY2021), taking equity to $4.1B; by 2025 it was $1.8B,
  below 2019, after $1.1B of buybacks (2022 at $34.23, 2023 at about $27.55, 2025 at $17.64 average) and the losses and
  impairments of 2023 to 2025.
- **Tangible equity is negative**: goodwill and intangibles of $3,191M exceed equity of $1,834M at 2025-12-31. Of gross
  goodwill of $4,181.1M, $2,394.5M has been written off as accumulated impairment (XBRL, 10-K FY2025).
- **Cash fell** from $1,864M (2021) to $687M (2025) while debt rose, the revolver was drawn ($570.0M at year-end 2025),
  and buybacks and Interactive took the difference; it recovered to $887M by June 2026 after the term-loan and 6.75%-note
  refinancing (10-Q Q2 2026).
- **Receivables and inventories** do not carry the story: receivables $254.2M against revenue $6,961.0M (2025), much of it
  gaming tax reimbursable by online partners; a cash business, as the filer says.
- **What the balance sheet cannot say**: the value of the licences that are not on it at cost, and whether the operating
  lease liability (discounted only to 2033 or 2034, because the filer judges renewals not reasonably certain) understates a
  rent that the operator must in practice keep paying to keep its casinos.

