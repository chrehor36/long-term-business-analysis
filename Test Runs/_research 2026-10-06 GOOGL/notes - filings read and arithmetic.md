# GOOGL 2026-10-06: filings read, extracts and arithmetic (working notes for the run file)

Raw filings are cached under `cache/` (gitignored; re-fetchable from EDGAR by accession). Fetched with a descriptive
User-Agent (contact chrehor36@gmail.com), one request at a time with a pause between.

## Documents
| document | filed | accession |
|---|---|---|
| 10-K FY2025 (goog-20251231.htm) | 2026-02-05 | 0001652044-26-000018 |
| 10-Q Q2 2026 (goog-20260630.htm) | 2026-07-23 | 0001652044-26-000071 |
| DEF 14A 2026 (goog-20260424.htm) | 2026-04-24 | 0001308179-26-000342 |
| 8-K Q2 2026 results, EX-99.1 (googexhibit991q22026.htm) | 2026-07-22 | 0001652044-26-000066 |
| 8-K equity raise and Berkshire private placement, EX-99.1 (d83560d8k.htm, d83560dex991.htm) | 2026-06-04 | 0001193125-26-257724 |
| 8-K mandatory convertible preferred closing (d36818d8k.htm), items 1.01, 3.03, 5.03 | 2026-06-05 | 0001193125-26-259830 |
| 8-K items 5.02, 5.07 (d57679d8k.htm), not read beyond the cover | 2026-06-11 | 0001193125-26-267578 |
| 8-K items 8.01, 9.01, notes (d171253d8k.htm), not read beyond the cover | 2026-08-10 | 0001193125-26-342390 |

## Shares (10-Q Q2 2026 cover, 0001652044-26-000071)
"As of July 15, 2026, there were 5,868 million shares of Alphabet's Class A stock outstanding, 835 million shares of
Alphabet's Class B stock outstanding, and 5,527 million shares of Alphabet's Class C stock outstanding."
Sum 12,230 million. Charter note (10-K FY2025, equity note): "The rights of the holders of each class of our common and
capital stock are identical, except with respect to voting." Class B has 10 votes, A one, C none; Page and Brin held about
52.7% of the voting power at 2025-12-31 (10-K, risk factors).
Not in the count: the 6.25% Series A and B mandatory convertible preferred (depositary shares GOOGM, GOOGN; $15B offered,
converting after about three years into a variable number of A or C shares) and any shares sold under the $40B ATM from Q3
2026 after the cover date.

## Price and cap
$346.47, GOOGL close 2026-10-05, aggregator (Yahoo chart endpoint via tools/run.py), live quote only, FLAGGED.
Applied to all three classes (CONVENTION of this run: the classes carry identical economic rights per the charter note;
Class C trades at a small discount, e.g. the June 2026 offering priced A at $355.1982 and C at $351.8018).
Cap = 12,230.0M x $346.47 = $4,237.3B.

## Sovereign
USD 30-year par yield 5.66%, US Treasury daily par yield curve, 10/05/2026 (`python tools/sources.py`).

## Cross-check (operator rule 4)
Net cash provided by operating activities FY2025 = 164,713 ($M) on the filed consolidated statement of cash flows (10-K
FY2025), equal to the 164,713 tools/run.py printed from XBRL. Purchases of property and equipment FY2025 = 91,447 on the
filed statement, equal to run.py's capex.

## Owner cash, arithmetic only (tools/run.py, USD M): OCF - stock pay - all capital spending
| FY | OCF | SBC | capex | owner cash (capex basis) | D&A basis |
|---|---|---|---|---|---|
| 2023 | 101,746 | 22,460 | 32,251 | 47,035 | 67,340 |
| 2024 | 125,299 | 22,800 | 52,535 | 49,964 | 87,188 |
| 2025 | 164,713 | 27,100 | 91,447 | 46,166 | 116,477 |
Five-year window (run.py): owner cash capex basis mean 46,997; yield on the cap 1.11%.
H1 2026 (10-Q): OCF 84,859; capex 80,598; SBC expense 15.2B (note: "total SBC expense was ... $15.2 billion" for six
months) -> owner cash about -10.9B for the half year (SBC expense used, not the cash-flow add-back; labelled as such).
Company's own non-GAAP "free cash flow" (OCF less capex, before stock pay), EX-99.1 Q2 2026: Q3 2025 24,461; Q4 2025
24,551; Q1 2026 10,116; Q2 2026 (5,855); TTM 53,273.

## Capital spending path (filer's words)
- 10-K FY2025: "we spent $52.5 billion and $91.4 billion on capital expenditures" (2024, 2025); "In 2026, we expect to
  significantly increase, relative to 2025, our investment in our technical infrastructure".
- 8-K EX-99.1 2026-06-01: "its 2026 capital expenditures are expected to be $180-$190 billion, and that it expects 2027
  capital expenditures to significantly increase compared to 2026."
- Same release: "$80 billion" of equity offerings ($15B mandatory convertible preferred, $15B A and C common, $40B ATM,
  plus $10B private placement to Berkshire Hathaway at $351.81 A and $348.20 C); "over the last year, Alphabet has raised
  over $85 billion of debt ... bringing its total debt balance to over $100 billion". About $30B of ATM proceeds "will be
  used to meet these 2026 calendar year tax obligations" on vesting employee equity awards.
- 10-Q Q2 2026: long-term debt carrying value $98.2B at 2026-06-30; capex H1 2026 $80.6B against $39.6B H1 2025.
- 2025: repurchased and retired 240 million shares for $45.4B (10-K). Repurchases of stock on the cash flow statement, six months: 28,306 (H1 2025), 0 (H1 2026) (10-Q).

## Revenue and segments (USD M)
FY: Search & other 175,033 / 198,084 / 224,532 (2023/24/25); YouTube ads 31,510 / 36,147 / 40,367; Cloud 33,088 / 43,229 /
58,705; total 307,394 / 350,018 / 402,836. Segment operating income 2025: Services 139,404; Cloud 13,910; Other Bets
(7,515); Alphabet-level (16,760) "primarily ... shared AI research and development".
Q2 2026 vs Q2 2025: Search & other 63,271 vs 54,190 (+16.8%); Cloud 24,768 vs 13,624; Cloud operating income 8,814 vs
2,826; total 119,796 vs 96,428. Paid clicks +13%, cost per click +3% (Q2 2026 y/y).
Revenue backlog 2026-06-30: $519.5B, of which $513.9B Google Cloud; "just over 50%" over 24 months.
Non-marketable equity securities (measurement alternative) carrying value $124.3B at 2026-06-30, "of which $87.9 billion
was remeasured at fair value during the three months ended June 30, 2026".

## Filer's statements bearing on Q1 (10-K FY2025, Item 1A)
- "Our business is characterized by rapid change as well as new and disruptive technologies."
- "We believe AI is quickly reshaping the advertising industry ... There is no assurance that we will adapt effectively and
  competitively to meet this shift".
- "AI technology and services are highly competitive, rapidly evolving, and require significant investment".
- "the consumers may change how they obtain information online, potentially reducing the utility of our existing products
  and services."
- "Due to these factors and the evolving nature of our business, our historical revenue growth rate and historical
  operating margin may not be indicative of our future performance."
- Search antitrust (10-Q Q2 2026, legal matters): final judgment December 2025 "imposes restrictions on how Google
  distributes its services and requires Google to share certain search data with and offer syndication services to certain
  competitors"; appealed January 2026.
