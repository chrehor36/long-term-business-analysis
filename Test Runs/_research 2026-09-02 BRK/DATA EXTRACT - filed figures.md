# BRK data extract — filed figures, gathered 2026-09-02
Sources: FY2025 10-K (filed 2026-03-02, acc. 0001193125-26-083899, period 2025-12-31);
2026 Q2 10-Q (filed 2026-08-10, acc. 0001193125-26-341032, period 2026-06-30).
All $ millions unless stated.

## STAGE 0
- Cover (10-Q 2026-08-10): Class A 488,450; Class B 1,408,035,161. A converts 1:1,500.
  B-equivalent = 2,140,710,161. Verified by `Screens/cover_shares.py BRK-B` this session.
- Price BRK-B $505.24, BRK-A $758,500 (2026-09-02, aggregator, flagged). A/1500=$505.67.
- Cap ≈ $1,081.6bn. Sovereign USD 30y 5.27% (Treasury par curve 2026-09-01).

## FLOAT (published, 10-K MD&A K-40 + 10-Q)
- $138bn (end 2020, stated in FY2025 10-K Item 1), $169bn (2023), $171bn (2024),
  $176bn (2025), $177.5bn (2026-06-30).
- "Our combined insurance operations generated pre-tax underwriting gains in each of the
  three years ending December 31, 2025 and the average cost of float was negative in each
  year." Same statement for H1 2026.
- Filer's own float definition = unpaid losses+LAE (incl. retro), life/annuity/health,
  unearned premiums, other policyholder liabilities, LESS premiums receivable, reinsurance
  receivables, retro deferred charges, DAC; excludes discount-rate AOCI on long-duration.

## CONVENTION 4 CONSTRUCTED FLOAT (2025-12-31, from filed balance sheet + notes)
+120,713 unpaid losses/LAE +31,048 retro +31,339 unearned +17,890 life/annuity/health
+10,312 other policyholder −18,656 premiums receivable −4,975 reinsurance recoverables
−4,800 DAC (note: "approximately $4.8 billion") −8,104 retro deferred charges
= **$174,767M vs published ~$176,000M → −0.7%.** Third validation (MKL was −1.1%).

## INSURANCE INVESTMENTS (10-K K-40 summary)
2025-12-31: cash+T-bills 212,651 · equities 294,144 · fixed 17,466 · other 4,702 = 528,963
2026-06-30: cash+T-bills 210,310 · equities 321,865 · fixed 16,781 · other 4,360 = 553,316

## CONSOLIDATED BALANCE SHEET
2025-12-31: I&O cash 47,719 + T-bills 321,434 + fixed 17,816 + equities 297,778 +
  equity method 19,978; RUE cash 4,158. Total assets 1,222,176.
  Consolidated cash+bills = 373,311 (369.0bn net of payables, per MD&A K-42 statement).
  BRK shareholders' equity 717,419; retained earnings 763,186; treasury (78,939).
  Income taxes principally deferred 86,955. Notes payable: I&O 45,763; RUE 83,318.
2026-06-30: I&O cash 35,096 + T-bills 324,905 + fixed 17,034 + equities 323,779 +
  equity method 19,948; RUE cash 5,513. Total assets 1,263,071.
  Consolidated cash+bills = 365,514 gross (771 unsettled payable).
  BRK shareholders' equity 747,910 (total 750,177 less NCI 2,267); retained 798,959;
  treasury (83,701).

## DEFERRED TAX (Note 20)
DTL: investments incl. unrealized appreciation **48,411**; PP&E 34,834; retro 1,702;
goodwill/intangibles 7,399; other 4,528 = 96,874. DTA 11,277. Net DTL 85,597.

## EARNINGS DISAGGREGATION (after-tax, MD&A K-34)
| | 2025 | 2024 | 2023 |
| Insurance underwriting | 7,258 | 9,020 | 5,428 |
| Insurance investment income | 12,513 | 13,670 | 9,567 |
| BNSF | 5,476 | 5,031 | 5,087 |
| BHE | 3,979 | 3,730 | 2,331 |
| MSR | 13,647 | 13,072 | 13,362 |
| Investment gains | 30,737 | 41,558 | 58,873 |
| OTTI KHC/OXY | (8,255) | — | — |
| Other | 1,613 | 2,914 | 1,575 |
| Net to BRK | 66,968 | 88,995 | 96,223 |
H1 2026: underwriting 3,448 · inv income 5,738 · BNSF 2,935 · BHE 2,005 · MSR 7,669 ·
gains 11,444 · other 2,534 · net 35,773. (Q2 2026 net 25,667.)

## PRE-TAX (segment note 26 + statements)
- Pre-tax underwriting: 9,460 (2025) / 11,405 (2024) / 6,913 (2023).
  GEICO 6,824/7,813/3,635 · BH Primary 785/855/1,374 · BHRG 1,851/2,737/1,904.
- Insurance pre-tax investment income: 15,261 / 16,748 / 11,581
  (interest+other 10,175; dividends 5,086 in 2025).
- Consolidated "Interest, dividend and other investment income" (I&O revenues line):
  23,261 / 21,825 / 15,764.
- Total operating businesses EBT: **51,714 / 53,936 / 43,637**; corporate+elims
  1,257 / 1,800 / (299); equity method (9,590) / 1,841 / 1,973; investment gains
  39,078 / 52,799 / 74,855; consolidated EBT 82,459 / 110,376 / 120,166.
- BNSF pre-tax 7,175 (2025); BHE pre-tax 2,194 (tax benefit −1,785).
- EPS per B: $31.04 (2025), $41.27 (2024), $44.27 (2023).

## UNDERWRITING RATIOS (MD&A; the word "combined ratio" appears ZERO times in the 10-K)
GEICO: loss ratio 72.3/71.8/81.0; expense 12.4/9.7/9.7; total 84.7/81.5/90.7 (2025/24/23).
  GEICO underwriting expenses +34.2% in 2025 (advertising push). Premiums written +5.3%
  (2025, PIF-driven) after +7.7% (2024, rate-driven, PIF −0.5%).
  Prior-yr favorable: GEICO 957 (2025) / 550 (2024) / 1,500 (2023).
BH Primary: 95.8 / 95.4 / 92.0. Prior-yr: ADVERSE 190 (2025) / fav 52 (2024) / fav 537
  (2023) — casualty/social inflation named.
BHRG P/C: 84.5 / 82.9 / 84.0. Prior-yr favorable 1,100 (2025) / 1,700 (2024) / 1,400
  (2023), mostly property. 2025: casualty estimates INCREASED.
Retro run-off: pre-tax losses 950/898/1,500 (before FX). Retro unpaid 31.0bn, deferred
  charges 8.1bn. Periodic payment annuity losses ~600/yr, liabilities 14.4bn.

## RESERVE DEVELOPMENT (Note 16, ex-retro)
Net favorable prior-year development: **1,854 (2025) / 2,322 (2024) / 3,541 (2023)**
  = 1.7% / 2.2% / 3.5% of opening net liabilities.
Current accident year incurred: 58,207 / 57,563 / 59,244 on P&C earned premiums
  83,633 / 83,259 / 78,331 → CAY loss ratio 69.6 / 69.1 / 75.6.
P&C u/w expenses (GEICO+BHP+BHRG-P/C): 16,502 / 15,515 / 14,112 → 19.7 / 18.6 / 18.0.
**CAY combined ≈ 89.3 (2025) / 87.7 (2024) / 93.6 (2023)** — profitable on the current
accident year in all three years; reported ratio is BETTER than CAY by ~2pts of releases.
Cross-check: MD&A per-segment development (GEICO +957 fav, BHP −190 adv, BHRG +1,100 fav)
reconciles to Note 16's 767+1,087=1,854. E&A net liabilities ~1.8bn (ex-retro).

## BUYBACKS
- Program (amended 2025): repurchase "any time that Berkshire's Chief Executive Officer,
  after consultation with the Chairman of the Board, believes that the repurchase price is
  below Berkshire's intrinsic value, conservatively determined." Floor: will not reduce
  consolidated cash+bills below **$30bn** (was $20bn in the 2011-era program).
- History: 2023 $9.2bn (cash flow) / 2024 $2,918M (all H1 2024) / **2025 ZERO** /
  Q1 2026 $235M / Q2 2026 $4,527M.
- Q2 2026 detail: May 65 A @ $716,231.37 + 1,458,312 B @ $476.01; June 413 A @
  $733,775.06 + 7,139,881 B @ $487.98. ≈ $4.53bn at ~$476-488/B-eq.
- Current price $505.24 = +3.5% over June's $487.98 average.

## EQUITY METHOD (Note 5)
KHC: 27.5%; carrying 8,634 (12/25), fair 7,897; $5.0bn pre-tax impairment Q2 2025;
  Berkshire's KHC board representatives RESIGNED 2025-05-19; one-quarter lag since.
OXY: 26.9% (26.7% at 6/26); carrying 10,894, fair 10,894 (12/25) — impaired Q4 2025 to
  market; fair 12,868 at 6/30/26. OXY warrants outstanding excluded.
Berkadia 450. Total carrying 19,978 (12/25) / 19,948 (6/26).
Equity method earnings 2025: −9,590 (incl. 10,681 impairments); 2024 +1,841; 2023 +1,973.

## ACQUISITIONS UNDER CURRENT MANAGEMENT (10-Q Note 2)
- OxyChem: $9.4bn cash, agreement 2025-10-01, closed 2026-01-02. Occidental retained
  legacy environmental liabilities. Assets $10.7bn (PP&E ~$7.0bn), liabilities $1.3bn.
- Taylor Morrison: $72.50/sh cash ≈ $6.8bn, agreement 2026-05-31, closed 2026-07-24.
  Homebuilder + financial services.

## CASH FLOW (10-K)
OCF 45,969 / 30,592 / 49,196 (2024 depressed by ~8.2bn tax payments on 2024 equity
sales). D&A 13,476 / 12,855 / 12,486. Capex 20,927 / 18,976 / 19,409.
Equity purchases (16,923) / (9,237) / (16,462); sales 30,686 / 143,359 / 40,631.
Treasury stock acquisitions 0 / (2,918) / (9,171).

## BNSF
Revenues 23,350 / 23,355 / 23,474. Operating earnings 8,055 / 7,469 / 7,415.
Pre-tax 7,175 (2025, +7.9%). Net 5,476 / 5,031 / 5,087.
Cars/units (thousands): **9,622 (2025) / 9,589 (2024) / 9,003 (2023)**.
Avg revenue per car/unit −0.5% (2025). 2024 SMART-TD labor charge $290M.
Consumer 5,601/5,537/4,765 · Industrial 1,382/1,448/1,471 · Ag+energy 1,421/1,399/1,299 ·
Coal 1,218/1,205/1,468.

## GEICO MARKET POSITION (Item 1)
"the five largest private passenger automobile insurers had a combined market share of
approximately 63.6%... GEICO's market share being the third largest at approximately
11.6%" (A.M. Best 2024 data, published 2025). Named competitors: State Farm, Progressive,
Allstate, USAA.

## ITEM 1 ON BARRIERS (the filer's own words)
"Except for regulatory considerations, there are virtually no barriers to entry into the
insurance and reinsurance industry."

## OTHER
- No dividend since 1967.
- Employees ~387,800.
- KHC/OXY OTTI after-tax (8,255) in 2025.
- Berkshire "held cash, cash equivalents and U.S. Treasury Bills (net of payables...) of
  $369.0 billion" at 2025-12-31 (I&O only; +4.2bn RUE cash).
- Significant catastrophe threshold: $150M/event. After-tax cat losses ~850 (2025) /
  1,200 (2024) / 725 (2023).
