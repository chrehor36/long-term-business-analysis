# DIS research notes, 2026-10-06 (filing extracts, transcribed; raw filings in cache/, gitignored)

All figures USD millions unless stated. Fiscal years end on the Saturday nearest 30 September.

## Filings read (EDGAR, CIK 1744489)
- 10-K FY2025 (year ended 2025-09-27), filed 2025-11-13, accession 0001744489-25-000155
- 10-Q Q3 FY2026 (quarter ended 2026-06-27), filed 2026-08-05, accession 0001744489-26-000057
- 8-K 2026-08-05 (Item 2.02), EX-99.1 Q3 FY2026 earnings release, accession 0001744489-26-000056
- 8-K 2025-11-13 (Item 2.02), EX-99.1 Q4 FY2025 earnings release, accession 0001744489-25-000154
- DEF 14A filed 2026-01-22, accession 0001744489-26-000013 (fetched; not read in full, Q5 and Q6 not reached)
- 8-K 2026-02-03 (Items 5.02, 8.01), CEO succession, accession 0001744489-26-000022
- 8-K 2026-02-24 (Item 5.02), accession 0001744489-26-000025; 8-K 2026-03-20 (Items 5.02, 5.07), accession 0001628280-26-020172
- Competitor: Netflix, Inc. 10-K FY2025, filed 2026-01-23, accession 0001065280-26-000034 (XBRL company concept, Revenues and OperatingIncomeLoss)

## Cross-check (operator rule 4)
10-K FY2025 Consolidated Statements of Cash Flows: cash provided by operations 18,101 (FY2025), 13,971 (FY2024),
9,866 (FY2023); investments in parks, resorts and other property (8,024), (5,412), (4,969); equity-based compensation
1,363, 1,366, 1,143. All match `tools/run.py`.

## Segment operating income (10-K FY2025 MD&A)
| | FY2025 | FY2024 |
|---|---|---|
| Entertainment | 4,674 | 3,923 |
| of which Linear Networks | 2,955 | 3,452 |
| of which Direct-to-Consumer | 1,327 | 143 |
| of which Content Sales/Licensing and Other | 392 | 328 |
| Sports | 2,882 | 2,406 |
| of which ESPN domestic | 2,801 | 3,056 |
| Experiences | 9,995 | 9,272 |
| of which Parks & Experiences domestic | 6,375 | 5,878 |
| of which Parks & Experiences international | 1,442 | 1,354 |
| of which Consumer Products | 2,178 | 2,040 |
| Total of the three segments | 17,551 | 15,601 |

Share of FY2025 segment operating income: Experiences 9,995 / 17,551 = 56.9%; Entertainment 26.6%; Sports 16.4%.
Entertainment plus Sports = 7,556 = 43.1%.

## Linear and ESPN unit trends (10-K FY2025 MD&A)
- Linear Networks revenue 9,364 vs 10,692 (-12%); domestic affiliate fees: "a decline of 9% from fewer subscribers,
  partially offset by an increase of 7% from higher effective rates"; domestic advertising: "a decline of 8% from fewer
  impressions attributable to lower average viewership".
- ESPN domestic affiliate and subscription fees: "an increase of 7% from higher effective rates was offset by a decrease
  of 7% from fewer subscribers". ESPN domestic programming and production costs 11,240 vs 10,435 (+8%) "primarily due to
  expanded college football programming rights and contractual rate increases". ESPN domestic OI 2,801 vs 3,056 (-8%).
- Contractual commitments for sports programming rights at 2025-09-27: 84,076 (2026: 9,894; 2027: 9,797; 2028: 9,540;
  2029: 9,101; 2030: 9,134; thereafter 36,610); total programming and other commitments 104,088 (10-K Note on commitments).
- 10-Q Q3 FY2026: Sports OI 858 vs 1,037 in the quarter (-17%), 1,701 vs 1,971 nine months (-14%); programming costs +10%
  "primarily due to contractual rate increases, costs for new sports rights and an impact from the timing of rights costs
  recognition as a result of the NBA contract renewal"; nine-month affiliate fees: "decreases of 3% from fewer subscribers".

## Direct-to-Consumer (10-K FY2025)
- Revenue 24,614, OI 1,327 (margin 5.4%). Subscription fee growth "8% attributable to higher effective rates reflecting
  increases in pricing and 4% from more subscribers". Disney+ paid subscribers 131.6M (2025-09-27) vs 125.3M; Hulu 64.1M
  vs 52.0M. Disney+ domestic ARPU $8.06 vs $7.89.
- Risk factor: "There are a number of competing DTC businesses. Consumers may not be willing to pay for an expanding set
  of DTC services at increasing prices [...] The highly competitive environment in which we operate puts pricing pressure
  on our DTC offerings and may require us to lower our prices or not increase our prices".
- Netflix (competitor, own filing 0001065280-26-000034): revenue 2025 45,183, operating income 13,327 (29.5%);
  2024 39,001 and 10,418 (26.7%); 2023 33,723 and 6,954 (20.6%).

## Experiences (10-K FY2025)
- Revenue 36,156 vs 34,151; OI 9,995 vs 9,272. Domestic attendance (1)%, per capita guest spending +5% (FY2025 vs FY2024).
- Capex FY2025 8,024; FY2026 expected "approximately $9 billion" (10-Q Q3 FY2026), Experiences 5,596 of 6,780 in nine months.

## Structural changes recorded in the filings
- Hulu: 8,610 paid FY2024 for Hulu's redeemable noncontrolling interest, a further 439 FY2025 on final appraisal.
- Star India transferred to a joint venture (FY2024); Fubo: 70% interest from 2025-10-29 (Hulu Live TV combined).
- NFL Transaction: ESPN to acquire NFL Network and other media assets for a 10% noncontrolling interest of ESPN (10-K);
  included in FY2026 results per the 10-Q ("2% from the NFL Transaction").
- YouTube TV removed Disney channels 2025-10-30 on contract expiry (10-K risk factor); 10-Q Q3 FY2026 notes "temporary
  suspension of carriage with an affiliate".
- CEO: Josh D'Amaro elected CEO effective 2026-03-18, succeeding Robert Iger (8-K 0001744489-26-000022, EX-99.1).

## Owner-cash notes for any later reader (Q4 and Q7 were not reached)
- Income taxes paid (supplemental disclosure, 10-K): FY2023 1,193; FY2024 3,963; FY2025 1,221. MD&A: FY2024 paid the
  FY2023 taxes deferred under California storm relief; FY2025 taxes were deferred to October 2025 under wildfire relief
  and paid in FY2026 (10-Q Q3 FY2026 MD&A). The FY2025 cash from operations is therefore lifted by a deferral that
  reverses in FY2026.
- Outside run.py's capex line: dividends to noncontrolling interest holders 0.6bn (FY2025) and 0.5bn (FY2024); the Hulu
  buyout above; equity award activity in other financing (410 FY2025, 374 FY2024).
- Borrowings 2026-06-27: current 8,627, non-current 37,414 (46,041); cash 5,185 (10-Q balance sheet). Nine-month FY2026
  change in borrowings +3,689 while repurchases were 7,245; release targets "at least $9 billion in share repurchases in
  fiscal 2026".
