# GS 2026-10-06 — filings read, extracts, arithmetic
Research notes for `Test Runs/2026-10-06 Run - GS Goldman Sachs.md`. Raw filing dumps were kept in the session scratchpad
(not committed). EDGAR, CIK 0000886982, fetched 2026-10-06 with a User-Agent naming chrehor36@gmail.com, under 3 requests
a second.

## Documents
| Document | Filed | Accession |
|---|---|---|
| Form 10-K, FY2025 (gs-20251231.htm) | 2026-02-25 | 0000886982-26-000091 |
| Form 10-Q, quarter ended 2026-06-30 (gs-20260630.htm) | 2026-08-03 | 0000886982-26-000297 |
| DEF 14A (gs-20260319.htm) | 2026-03-20 | 0001193125-26-117433 |
| Form 8-K, Items 2.02/7.01/9.01, 2Q26 earnings; EX-99.1 a2q26gsearningsresults.htm | 2026-07-14 | 0000886982-26-000294 |
| Form 8-K, Items 2.02/8.01, Apple Card transition and segment change | 2026-01-08 | 0000886982-26-000004 |
| Peer XBRL facts, Morgan Stanley FY2025 10-K | | 0000895421-26-000086 |
| Peer XBRL facts, JPMorgan Chase FY2025 10-K | | 0001628280-26-008131 |

Latest earnings 8-K is the 2026-07-14 one (Q3 2026 results not yet filed on 2026-10-06).

## Cross-check (operator rule 4)
Total assets 2025-12-31: $1,809,320M on the filed Consolidated Balance Sheet (10-K, 0000886982-26-000091) = $1,809,320M in
`tools/run.py`'s XBRL transcription of the same accession. Agree. Total shareholders' equity $124,972M likewise agrees.

## Balance sheet, 10-K (2025-12-31 / 2024-12-31, $M)
Assets: cash 164,259 / 182,092; resale agreements 126,007 / 180,062; securities borrowed 208,208 / 194,645; customer and
other receivables 185,842 / 133,717; trading assets (at fair value) 656,796 / 570,555; AFS 99,244 / 79,458; HTM 69,193 /
78,713; other investments 25,825 / 26,343; loans net 237,734 / 196,200; other 36,212 / 34,187; total 1,809,320 / 1,675,972.
Liabilities: deposits 501,422 / 433,013; repo 223,384 / 274,380; securities loaned 53,644 / 56,060; other secured
financings 28,021 / 28,150; customer and other payables 231,865 / 223,255; trading liabilities 262,552 / 202,555;
unsecured short-term borrowings 70,459 / 69,709; unsecured long-term borrowings 285,500 / 242,634; other 27,501 / 24,220;
total liabilities 1,684,348 / 1,553,976. Equity 124,972 / 121,996 (preferred 15,153 / 13,253).

10-Q (2026-06-30): total assets 2,127,711; trading assets 789,083; deposits 557,955; repo 266,855; unsecured short-term
89,911; unsecured long-term 347,963; equity 122,742; shares outstanding 291,442,355.

## Deposits by source, 2025-12-31 (10-K MD&A, $M)
Consumer (Marcus and Apple Card) 207,902; private bank 100,770; brokered CDs 47,288; deposit sweep programs 34,363;
transaction banking 69,764; other (substantially all institutional) 41,335; total 501,422. Time deposits 185,270
(weighted average maturity about 0.7 years). Average rate on interest-bearing deposits: 3.94% (2025), 4.73% (2024),
4.36% (2023) (10-K statistical disclosures). Net yield on interest-earning assets 0.82% (2025).

## Derivatives, 2025-12-31 (10-K Note 7, $M)
Gross fair value: assets 360,080, liabilities 391,214. After counterparty netting (261,175) and cash collateral netting
(45,952 / 45,634): on balance sheet 52,953 / 84,405. Notional total 43,530,881 (2024: 37,127,322); of which interest
rates 29,222,716, currencies 7,725,602, equities 3,962,305, credit 1,745,397, commodities 555,133. Bilateral OTC notional:
interest rates 10,705,896; currencies 7,192,306; equities 1,634,183; credit 758,385; commodities 186,420.
10-Q 2026-06-30: total notional 52,831,907; gross fair value assets 443,299, liabilities 498,268.
Downgrade triggers (10-K): additional collateral or termination payments $224M one-notch, $1.80B two-notch.

## Level 3 (10-K / 10-Q)
Level 3 financial assets $20,324M at 2025-12-31 (1.1% of total assets), $20,839M at 2026-06-30; level 3 financial
liabilities $32,130M at 2025-12-31.

## Filing language bearing on Q1 (10-K, verbatim)
- Risk factors: "Changes in credit spreads are market-driven, and subject at times to unpredictable and highly volatile
  movements." ... "The market for credit default swaps has proven to be extremely volatile and at times has lacked a high
  degree of transparency or liquidity."
- Risk factors: "In periods when volatility is increasing, but asset values are declining significantly, it may not be
  possible to sell assets at all or it may only be possible to do so at steep discounts."
- MD&A, market risk: "Inherent limitations to VaR include: • VaR does not estimate potential losses over longer time
  horizons where moves may be extreme; • VaR does not take account of the relative liquidity of different risk positions;
  and • Previous moves in market risk factors may not produce accurate predictions of all future market moves." And:
  "Given its reliance on historical data, VaR is most effective in estimating risk exposures in markets in which there are
  no sudden fundamental changes or shifts in market conditions."
- "Our positional losses observed on a single day exceeded our 99% one-day regulatory VaR on three occasions during 2025
  and on two occasions during 2024."
- Average daily VaR $90M (2025), $92M (2024); period-end $79M.

## Revenue composition, 2025 (10-K, $M)
Investment banking 9,348; investment management 11,749; commissions and fees 4,042; market making 17,993; other principal
transactions 1,592; net interest income 13,559; total net revenues 58,283. Segment: Global Banking & Markets 41,453 (of
which FICC 14,522, Equities 16,535); Asset & Wealth Management 16,679; Platform Solutions 151. Segment assets: GBM
1,582,670 of 1,809,320. Net earnings 17,176 (2025), 14,276 (2024), 8,516 (2023).

## 8-K 2026-01-08
Apple Card program to transition to a new issuer over about 24 months; Q4 2025 effect: release of $2.48B of loan loss
reserves, net revenue reduction of $2.26B (markdowns and contract termination obligations), $38M of operating expenses.

## EX-99.1, 2Q26 (8-K 2026-07-14)
Net revenues $20,338M (2Q26), net earnings $6,628M, diluted EPS $20.98, annualized ROE 23.5%, book value per share
$367.67. The headline carries ROE, a GAAP-derived ratio; Q4 was not reached, so the non-GAAP reading was not carried
further.

## Peer row (XBRL facts from each company's own FY2025 10-K; $M; COMPUTATION, NOT A CLEARANCE)
| | Assets | Deposits | Equity | Deposit interest 2025 | Assets/equity | Deposits/assets | Deposit interest / average of year-end deposits |
|---|---|---|---|---|---|---|---|
| GS (0000886982-26-000091) | 1,809,320 | 501,422 | 124,972 | 18,393 | 14.48 | 27.7% | 3.94% |
| MS (0000895421-26-000086) | 1,420,270 | 415,523 | 111,632 | 10,626 | 12.72 | 29.3% | 2.68% |
| JPM (0001628280-26-008131) | 4,424,900 | 2,559,320 | 362,438 | 45,112 | 12.21 | 57.8% | 1.82% |
Prior year-end deposits used for the averages: GS 433,013; MS 376,007; JPM 2,406,032.

## Other arithmetic
Market cap 893.46 × 291,171,408 = $260.15B. Price to book 893.46 / 367.67 = 2.43. Notional / equity 2025 = 348 times.
Level 3 assets / equity = 16.3%. Total assets grew 17.6% in the first half of 2026. Wholesale funding at 2025-12-31
(repo + securities loaned + other secured + unsecured short- and long-term) = $661,008M, against deposits $501,422M.
