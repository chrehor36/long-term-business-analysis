# AAPL — THE PRIMARY TEST [E2-01] AND THE BUYBACK RECORD [E5-08] / [E2-60] (Task 2)
Research file. Gathered 2026-09-06. CIK 0000320193. All figures in $ millions unless stated.

## METHOD AND VERIFICATION
Series assembled from the SEC XBRL companyfacts API and **cross-checked against the filed
statements in five separate 10-K vintages**, per operator rule 4:

| cross-check | filed doc | figure verified | result |
|---|---|---|---|
| FY2013 | 10-K acc. 0001193125-13-416534 | repurchases $(22,860); equity $123,549; cover 899,738,000 sh | **MATCH** |
| FY2015 | 10-K acc. 0001193125-15-356351 | repurchases $(35,253); liquidity table cash+MS $205,666 / $155,239 / $146,761 for FY15/14/13 | **MATCH** |
| FY2017 | 10-K acc. 0000320193-17-000070 | equity-stmt share counts FY15/16/17 | **MATCH** |
| FY2019 | 10-K acc. 0000320193-19-000119 | repurchases $(66,897); equity $90,488; cover 4,443,265,000 sh | **MATCH** |
| FY2021 | 10-K acc. 0000320193-21-000105 | repurchases $(85,971); equity $63,090; cover 16,406,397,000 sh | **MATCH** |
| FY2025 | 10-K acc. 0000320193-25-000079 | repurchases $(90,711); equity $73,733; 402m shares for $89.3bn | **MATCH** |

**SPLIT TRAP — HANDLED.** Two splits sit inside the window: **7:1 on 2014-06-09** and **4:1 on
2020-08-31**. The XBRL API returns each period's value at the vintage last reported, so the raw
`CommonStockSharesOutstanding` series is internally inconsistent (FY2013–FY2018 carry the 7:1
only; FY2019 onward carry both). Every share count below has been restated to **today's basis**
(FY2013 × 28; FY2014–FY2019 × 4; FY2020 onward × 1). Dollar figures need no adjustment.

---

## 2A. THE MASTER TABLE (FY2013–FY2025)

| FY | Buyback $ | Divs $ | Total returned | Sh. repurch. (m, today) | Avg px $ (today) | Sh. o/s FYE (bn, today) | Equity $ | ROE % | Total debt $ | Cash+MS $ | **Net cash $** | OCF−capex $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2013 | 22,860 | 10,528 | 33,388 | 1,315.3 | 17.45 | 25.178 | 123,549 | — | 16,960 | 146,761 | **129,801** | 45,501 |
| 2014 | 45,000 | 11,031 | 56,031 | 1,954.7 | 23.02 | 23.465 | 111,547 | 33.6 | 35,295 | 155,239 | **119,944** | 50,142 |
| 2015 | 35,253 | 11,561 | 46,814 | 1,300.1 | 27.71 | 22.315 | 119,355 | 46.2 | 64,328 | 205,666 | **141,338** | 70,019 |
| 2016 | 29,722 | 12,150 | 41,872 | 1,118.4 | 25.93 | 21.345 | 128,249 | 36.9 | 87,032 | 237,585 | **150,553** | 53,497 |
| 2017 | 32,900 | 12,769 | 45,669 | 986.0 | 33.47 | 20.505 | 134,047 | 36.9 | 115,680 | 268,895 | **153,215** | 51,774 |
| 2018 | 72,738 | 13,712 | 86,450 | 1,622.0 | 45.04 | 19.020 | 107,147 | 49.4 | 114,483 | 237,100 | **122,617** | 64,121 |
| 2019 | 66,897 | 14,119 | 81,016 | 1,380.8 | 48.60 | 17.773 | 90,488 | 55.9 | 108,047 | 205,898 | **97,851** | 58,896 |
| 2020 | 72,358 | 14,081 | 86,439 | 917.0 | 79.06 | 16.977 | 65,339 | 73.7 | 112,436 | 191,830 | **79,394** | 73,365 |
| 2021 | 85,971 | 14,467 | 100,438 | 656.0 | 130.34 | 16.427 | 63,090 | 147.4 | 124,719 | 190,516 | **65,797** | 92,953 |
| 2022 | 89,402 | 14,841 | 104,243 | 569.0 | 158.52 | 15.943 | 50,672 | 175.5 | 120,069 | 169,109 | **49,040** | 111,443 |
| 2023 | 77,550 | 15,025 | 92,575 | 471.0 | 162.63 | 15.550 | 62,146 | 171.9 | 111,088 | 162,099 | **51,011** | 99,584 |
| 2024 | 94,949 | 15,234 | 110,183 | 499.0 | 190.38 | 15.117 | 56,950 | 157.4 | 106,629 | 156,650 | **50,021** | 108,807 |
| 2025 | 90,711 | 15,421 | 106,132 | 402.0 | 222.14 | **14.773** | 73,733 | 171.4 | 98,657 | 132,420 | **33,763** | 98,767 |

**Definitions and disclosed judgments.**
- *Buyback $* = cash-flow line `Repurchases of common stock` (excludes the separate financing line
  `Payments for taxes related to net share settlement of equity awards`, which was **$5,960m in
  FY2025** and **$6,462m in 9M FY2026** — a real, additional, share-reducing cash cost).
- *Avg px* = the equity-statement **charge to retained earnings** ÷ shares retired (trade-date
  basis), not the cash-flow figure; the two differ by settlement timing.
- *Total debt* = `LongTermDebtNoncurrent` + current term debt + commercial paper.
- *Cash+MS* = cash & equivalents + current marketable securities + **non-current** marketable
  securities.
- **ROE method: net income ÷ AVERAGE of beginning and ending shareholders' equity.** FY2013 is
  blank because FY2012 equity would come from a pre-window filing. **This ROE is not an economic
  return — see 2E. Do not use it as a franchise measure.**

## 2B. CUMULATIVE RECORD FY2013–FY2025 (13 years)

| | $m |
|---|---|
| Cumulative buybacks | **816,311** |
| Cumulative dividends | **174,939** |
| **TOTAL RETURNED TO SHAREHOLDERS** | **991,250** |
| Cumulative net income | 893,401 |
| Cumulative operating cash flow | 1,119,068 |
| Cumulative capex (total, not maintenance) | 140,199 |
| **Cumulative OCF − capex** | **978,869** |
| Total returned ÷ (OCF − capex) | **101.3%** |
| Total returned ÷ net income | **111.0%** |
| Shortfall (returned − FCF) | **(12,381)** |

Adding 9M FY2026 (buybacks $62,094m, dividends $11,778m) the running total is
**$1,065,122m — over one trillion dollars returned since FY2013.**

Share count: **25.178bn (FY2013) → 14.773bn (FY2025) → 14.609bn (2026-06-27). A 42.0%
reduction in the share count over thirteen years.** Verbatim from the FY2025 10-K rollforward
(in thousands): beginning 15,116,786; repurchased (401,672); issued net of withholding 58,146;
ending **14,773,260**.

## 2C. TODAY — THE [E5-11] NET CASH CHECK (Q3 FY2026 10-Q, balance sheet 2026-06-27)

Read directly off the filed condensed balance sheet:

| | 2026-06-27 | 2025-09-27 |
|---|---|---|
| Cash and cash equivalents | 39,544 | 35,934 |
| Marketable securities — current | 22,855 | 18,763 |
| Marketable securities — non-current | 84,118 | 77,723 |
| **Gross cash + marketable securities** | **146,517** | **132,420** |
| Commercial paper | 1,997 | 7,979 |
| Term debt — current | 11,007 | 12,350 |
| Term debt — non-current | 71,340 | 78,328 |
| **Total debt** | **84,344** | **98,657** |
| **NET CASH POSITION** | **62,173** | **33,763** |
| Total shareholders' equity | **107,520** | 73,733 |

**THE BRIEF'S PREMISE NEEDS SPLITTING IN TWO — this matters, so state it exactly.**

1. **Over the long arc the premise is CORRECT and dramatic.** Net cash peaked at **$153,215m at
   FY2017 year-end** and fell to a trough of **$33,763m at FY2025 year-end — a fall of $119.5bn,
   78%.** Gross cash+MS peaked at $268,895m (FY2017) and is now $146,517m, down $122.4bn.
2. **Over the last three quarters the premise is WRONG — net cash has RISEN sharply, by $28.4bn,
   from $33,763m to $62,173m.** Debt fell $14.3bn (no term debt issued at all in 9M FY2026;
   $8,146m repaid and $5,911m of commercial paper retired) while gross cash rose $14.1bn.
   Apple has begun *deleveraging*.

Also note: **Apple ran a slight net-cash-consumption year in FY2025 and a net-cash-rebuild year in
FY2026 to date.** The FY2026 net income run-rate ($101,464m in 9M, +20% y/y) is now comfortably
above the payout, which is why the position is rebuilding.

Debt note verbatim, Q3 FY2026 10-Q Note 6:
> *"As of June 27, 2026 and September 27, 2025, the Company had **$2.0 billion and $8.0 billion of
> commercial paper outstanding**, respectively."*
> *"...an aggregate carrying amount of **$82.3 billion and $90.7 billion**, respectively
> (collectively the 'Notes'). As of June 27, 2026 and September 27, 2025, **the fair value of the
> Company's Notes, based on Level 2 inputs, was $71.2 billion and $80.4 billion**, respectively."*

**The fair-value gap is an unrecorded gain to the equity holder: Apple carries $82.3bn of debt
that could be retired for $71.2bn — an $11.1bn (13.5%) discount, the mirror image of the low
coupons it locked in during 2013–2021.** Economic net cash is therefore nearer **$73bn** than
$62bn.

## 2D. THE [E2-60] QUESTION, ANSWERED PLAINLY

**Was equity consumed? YES, and the filing says so in one word.** The FY2025 10-K's consolidated
statement of shareholders' equity does not have a "retained earnings" line. It is headed
**"Accumulated deficit"**:

> *"**Accumulated deficit:** Beginning balances **( 19,154 )** ... Net income 112,010 ... Dividends
> and dividend equivalents declared ( 15,413 ) ... Common stock withheld related to net share
> settlement of equity awards ( 1,655 ) ... **Common stock repurchased ( 90,052 )** ... Ending
> balances **( 14,264 )**"*

Apple has bought back more stock than it has ever earned in retained profit. Book equity fell from
a peak of **$134,047m (FY2017) to a trough of $50,672m (FY2022)** — a **62% destruction of book
equity** — before recovering to $73,733m (FY2025) and $107,520m today. The accumulated deficit
crossed back into positive retained earnings only in the June 2026 quarter (+$11,326m).

**Did leverage rise to fund the payout? YES — but not to a dangerous level, and it is now
reversing.**
- Total debt went from **$16,960m (FY2013) to a peak of $124,719m (FY2021)** — **+$107.8bn** — and
  is **$84,344m today**. Apple was **debt-free until April 2013**; the entire debt stack was
  created to fund the return-of-capital program (and, initially, to avoid repatriation tax on
  offshore cash).
- Net new debt over FY2013–FY2025: **+$81,697m**.
- Sources/uses over the 13 years: FCF **$978.9bn** + new debt **$81.7bn** + net cash drawdown
  **$96.0bn** ≈ funded payout **$991.3bn** + net-share-settlement taxes (~$50bn) + acquisitions
  and other.

**The honest verdict for the run file.** Apple returned **101.3% of its cumulative free cash flow
and 111% of its cumulative net income**. This was **not** funded out of operating strength alone;
it was funded out of operating strength **plus** a deliberate conversion of a $153bn net-cash
fortress into an $84bn debt stack. That is a real, permanent leverage decision, taken over a
decade, in full view, and disclosed line by line. It is not concealed and it did not impair the
business: interest cover is enormous, the debt was raised at coupons now trading 13.5% below par,
and net cash never went negative. **Apple has never been net-debt in the window.**

Two distinct judgments follow and should be kept apart in the run file:
- **On honesty [Q3]: this is a PASS.** The disclosure is complete, the equity statement names the
  accumulated deficit rather than hiding it, and no non-GAAP measure is deployed to soften it.
- **On rationality [Q3] and durability [Q4]: this is a QUESTION, not a pass.** The 13-year average
  repurchase price rose monotonically from **$17.45 to $222.14** (and $287.44 in 9M FY2026 —
  16.5× the FY2013 price). Apple bought most heavily in dollars at the highest prices. A
  price-indifferent, calendar-driven program that spends ~100% of FCF regardless of valuation is
  the opposite of the discipline in [E5-08]; **the shareholder's per-share outcome was excellent
  only because the business compounded fast enough to outrun the prices paid.** State this as a
  windage item, not a violation.

## 2E. WARNING ON ROE — DO NOT CARRY THE HEADLINE NUMBER FORWARD

FY2025 ROE of **171.4%** (and FY2022's 175.5%) is an **artifact of the buyback, not a measure of
franchise economics.** The denominator has been deliberately destroyed: equity fell 62% while
earnings tripled. In FY2013, with equity at $123.5bn, ROE was ~31%. Any Q2 franchise argument
built on "Apple earns 170% on equity" is a category error and will not survive audit. If a
capital-productivity number is needed, use return on *invested* capital with the cash pile and
the debt both reinstated, or use owner earnings against enterprise value. **Flag for the Q2/Q4
author.**

## 2F. AUTHORIZATIONS (disclosed, FILED)
Board authorization ceiling by announcement date, from XBRL `StockRepurchaseProgramAuthorizedAmount1`
tagged in the respective 10-Ks: 2012 $10bn → Apr-2013 $60bn → Apr-2014 $90bn → FY2015 $140bn →
Apr-2016 $175bn → May-2017 $210bn → Apr-2019 $175bn (new program) → FY2020 $225bn → FY2021 $315bn
(cumulative program totals; later years increase the authorization annually each April). The
FY2025 10-K and Q3 FY2026 10-Q both state the program **"do[es] not obligate the Company to
acquire a minimum amount of shares."**

## 2G. THINGS I DID NOT ESTABLISH (UNRESEARCHED — nameable documents exist)
- **Maintenance vs total capex.** I used **total** capex ($140.2bn cumulative) as the FCF
  deduction. Owner earnings under the framework require the maintenance figure. Apple does not
  disclose a maintenance/growth split. The resolving documents would be the PP&E note plus the
  D&A series (D&A $11,698m FY2025 vs capex $12,715m — capex ≈ 1.09× D&A, suggesting little growth
  capex at the corporate level, but this is inference, not disclosure). **See
  `q3_disclosure_flags.md` and the Task 4 file on supplier tooling, which is the load-bearing
  omission here.**
- The **current** (FY2024–FY2026) buyback authorizations were not read off the April 8-Ks; only
  the amounts tagged through FY2021 are recorded above.
