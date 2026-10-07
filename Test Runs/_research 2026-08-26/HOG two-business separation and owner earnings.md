# HOG, separating the manufacturer from the finance company
**Built 2026-08-31. The method problem the operator flagged, solved from the filings.**

## The company solves it for you: Note 19, Supplemental Consolidating Data

The FY2025 10-K (acc. 0000793952-26-000011) and the Q2 2026 10-Q (acc.
0000793952-26-000061) both carry a **Supplemental Consolidating Data** note giving
separate legal-entity income statements, balance sheets and **cash-flow statements**
for:

- **Financial Services Entities**: Harley-Davidson Financial Services, Inc. and subsidiaries
- **Non-Financial Services Entities**, everything else (HDMC + LiveWire + the parent)

This is the single strongest candor item in the file **[E2-26]**: it is precisely the
disclosure a half-owner would want and it is not required by GAAP segment rules.
The run uses it. **Reportable segments (HDMC / LiveWire / HDFS) are used for
operating income; the consolidating note is used for cash flow and balance sheet.**

## Method adopted, stated explicitly

1. **Manufacturing business = Non-Financial Services Entities.** Owner earnings
   computed the framework way, multi-year mean of (operating cash flow less SBC)
   less the (c) guess, with **one correction that is mandatory here**: non-FS
   operating cash flow includes the **intercompany dividend HDFS pays up to the
   parent**, which is not an operating cash flow of the manufacturing business. It
   is removed. Its size equals the consolidating adjustment to net income each year,
   verified to the cent for 2025 (see the reconciliation below).
2. **HDFS = valued separately**, at its own filed book equity attributable to HOG,
   cross-checked against a **market-tested price**: KKR and PIMCO each paid $23.3M
   for 4.9% of HDFS in Q4 2025 (9.8% for $46.6M), stated by the company as
   "approximately 1.75x HDFS's post-transaction equity carrying value."
3. **No blended consolidated owner-earnings yield is reported anywhere as a
   valuation input.** Consolidated OCF is funded partly by $2.7bn of HDFS debt and
   deposits; a blended yield on it is an artifact. (The demonstration: consolidated
   OCF was **+$568.9M in FY2025 and NEGATIVE $59.7M in H1 2026**, same business,
   opposite sign, entirely because of where finance receivables sit.)

## The 2025 structural event, the HDFS Transaction (Q4 2025)

From the FY2025 10-K "Key Factors" and the E&Y critical audit matter:

- HDFS **sold $4.1bn of existing retail finance receivables** (the audit matter says
  $4.2bn including securitization interests), releasing the related allowance and
  **contributing a $191.4M BENEFIT to the 2025 provision for credit losses**.
- Sold **95% of its residual interests** in the securitization trusts:
  **gain $27.9M**, deconsolidating $1.9bn of net receivables and $1.7bn of debt.
- **Forward Flow Agreement**: HDFS will sell **up to two-thirds of new retail loan
  originations** to KKR/PIMCO over five years, earning servicing fees of 1%/yr
  (prime) and 2.5%/yr (subprime).
- **KKR and PIMCO bought 9.8% of HDFS equity for $46.6M** at ~1.75x post-transaction
  equity carrying value; exchangeable into HOG common stock from Q4 2032 (or on a
  change of control) at 1.75x HDFS equity carrying value, capped at 4.9% of HOG's
  outstanding shares. HOG may buy them back from Q4 2028, one-third per year.
- Proceeds funded a tender for HDFS medium-term notes (**$72.6M loss on
  extinguishment**), repayment of the parent's $450M term loan, and a **$200M
  accelerated share repurchase**.

**One-time items inside 2025 reported earnings (pre-tax):**

| item | $M |
|---|---:|
| provision-for-credit-losses release | **+191.4** |
| gain on sale of securitization beneficial interests | +27.9 |
| loss on sale of finance receivables | (11.4) |
| loss on debt extinguishment | (72.6) |
| **net one-time credit** | **+135.3** |

At the 2025 effective rate (28.2%) that is roughly **+$97M after tax**. Reported net
income attributable to HOG was $338.7M; **on a clean basis it was closer to $240M**,
and HDMC, the motorcycle company, **lost $28.7M at the operating line.**

## Consolidated balance sheet, split (Note 19)

| $M | Non-Financial Services | Financial Services | consolidated |
|---|---:|---:|---:|
| **2025-12-31** | | | |
| Cash and equivalents | 1,314.9 | 1,776.8 | 3,091.7 |
| Finance receivables (HFS + HFI) | n/a | 1,965.2 | 1,965.2 |
| Total assets | 4,245.6 | 4,031.6 | 8,044.8 |
| Short-term debt | n/a | 497.8 | 497.8 |
| Current portion of LTD | n/a | 819.6 | 819.6 |
| Long-term debt | **297.3** | 1,352.3 | 1,649.6 |
| Deposits | n/a | 536.6 | 536.6 |
| Shareholders' equity | 2,843.4 | 438.1 | 3,156.9 |
| **2026-06-30** | | | |
| Cash and equivalents | **1,283.3** | 612.5 | 1,895.8 |
| Finance receivables (HFS + HFI) | n/a | **2,645.2** | 2,645.2 |
| Total assets | 4,308.8 | 3,446.3 | 7,245.9 |
| Short-term debt | n/a | 613.1 | 613.1 |
| Current portion of LTD | n/a | 498.5 | 498.5 |
| Long-term debt | **297.3** | 833.5 | 1,130.8 |
| Deposits | n/a | 516.5 | 516.5 |
| Shareholders' equity | **2,864.5** | **377.0** | 3,116.0 |

**The manufacturing entity carries ONE debt instrument: $300M of 4.625% senior notes
issued July 2015 and due 2045** (net $297.3M of discount/issue costs). Nineteen years
to maturity, fixed rate, **no financial covenants** ("No financial covenants are
required under the medium-term or senior notes"). Read against **[E3-52]** this is
about as benign as a corporate obligation gets. Interest is roughly $13.9M/yr.

**Manufacturing net cash at 2026-06-30: $1,283.3M - $297.3M = +$986.0M.**

All the leverage sits at HDFS: $1,945.1M of debt plus $516.5M of deposits against
$377.0M of equity. The credit-facility covenant permits HDFS debt (ex-secured) to
reach **10.0x** its allowance-plus-equity; a separate covenant caps *parent* debt to
debt-plus-equity at 0.7x (parent is at 0.09x). Ratings at 2025-12-31: Moody's Baa3
stable, **S&P BBB- CreditWatch Negative**, Fitch BBB+ stable, one notch above
non-investment grade at two of three agencies.

## Segment operating income, the whole story in one table

| $M | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** | 2026 guided (raised 2026-07-23) |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| HDMC | 289.6* | (186.1)* | 476.8 | 677.1 | 661.2 | 277.8 | **(28.7)** | **+10 to +50** |
| LiveWire | (incl.) | (incl.) | (68.2) | (85.3) | (116.8) | (109.6) | (75.0) | **(70) to (80)** |
| HDFS | 266.0 | 195.8 | 414.8 | 317.5 | 234.7 | 248.4 | **490.4** | **+55 to +70** |
| **total** | **555.6** | **9.7** | **823.4** | **909.3** | **779.1** | **386.6** | **+0 to +40** |

\* 2019/2020 are the old "Motorcycles and Related Products" segment, which included
the electric programme before the LiveWire separation.

**Read the 2026 column.** HDMC + LiveWire, the motorcycle company, is guided to an
operating result of **-$70M to -$20M**. Every dollar of consolidated 2026 operating
income is guided to come from the finance company. **And 2025's $490.4M at HDFS is
$191.4M of allowance release plus $27.9M of gain, less $72.6M of extinguishment loss.**

Note also the seasonality, which matters for reading any half-year: H1 2025 HDMC
operating income was $177.6M against a full-year **-$28.7M**, i.e. H2 2025 HDMC was
**-$206.3M**. H1 2026 HDMC was $91.3M; full-year guidance of $10-50M implies H2 2026
HDMC of **-$81M to -$41M**.

## Manufacturing owner earnings, 2021-2025 [E2-23]

Convention: multi-year mean of (operating cash flow - SBC) - (c), with OCF taken from
the Non-Financial Services column of Note 19 and the intercompany dividend removed.

| $M | non-FS OCF | less HDFS dividend | **mfg OCF** | SBC | D&A | capex | **OE (c=D&A)** | **OE (c=capex)** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 643.0 | 239.9 | 403.1 | 38.9 | 156.0 | 116.0 | **208.2** | **248.2** |
| 2022 | 425.7 | 199.6 | 226.1 | 51.0 | 143.3 | 147.3 | **31.9** | **27.9** |
| 2023 | 769.3 | 199.8 | 569.5 | 79.3 | 149.2 | 202.3 | **341.0** | **287.8** |
| 2024 | 730.7 | 199.8 | 531.0 | 47.0 | 151.3 | 194.7 | **332.7** | **289.3** |
| 2025 | 1,283.5 | 999.8 | 283.7 | 29.6 | 163.0 | 152.7 | **91.1** | **101.5** |

- **Five-year mean (2021-25, the corpus default window [E2-42]): $191M - $201M**
- **Three-year mean (2023-25): $226M - $255M**
- **Two-year mean (2024-25): $195M - $212M**

### Reconciliation proof for 2025 (operator rule 4 cross-check)

Non-FS net income $976,716K includes a **$1,000,000K dividend from HDFS**, eliminated
in consolidation (Note 19 shows Investment income $1,044,270 with a $(1,000,000)
consolidating adjustment; the net-income consolidating adjustment is $(999,799)).
Manufacturing net result = 976,716 - 1,000,000 = **-$23,284K**.
Bridge to manufacturing OCF: -23,284 + D&A 163,013 + fee amortisation 2,465
+ SBC 29,580 + deferred tax 5,937 + other 6,799 - non-cash pension income 55,195
- benefit payments 6,835 + working-capital change 161,035 = **$283,515K**, against
$1,283,515K - $1,000,000K = **$283,515K. Exact.**

### THE FINDING THAT GOVERNS Q4, 2025's owner earnings are a working-capital liquidation

The $161.0M working-capital change in 2025 is a **release**: inventories -$47.6M,
receivables -$30.6M, other current assets -$60.8M. Strip it and manufacturing owner
earnings in 2025 were **-$69.9M (c = D&A)**.

It continued and accelerated in H1 2026: non-FS inventories fell a further **$221.8M**
(balance-sheet inventories $730.9M -> $500.9M). A shrinking business releases working
capital; that release is the mirror image of [E2-23] constraint 3's *increment*, and
it is not repeatable, inventory cannot go below zero, and it is now down 31% in six
months.

**H1 2026 manufacturing, same method:** non-FS OCF $162.6M less the $100.0M
intercompany dividend = $62.6M; less SBC $17.2M; less D&A $85.3M = **-$39.9M**
(or +$0.8M against capex of $44.6M). And that half-year *includes* the $221.8M
inventory release and *excludes* the seasonally loss-making second half.

### 2026 bottom boundary [E5-34], built from the company's own raised guidance

| item | $M |
|---|---:|
| HDMC operating income (guided 2026-07-23) | +10 to +50 |
| LiveWire operating loss (guided) | (70) to (80) |
| **manufacturing operating result** | **(70) to (20)** |
| investment income on ~$1.2bn of cash at ~4% | +45 |
| interest on the 2045 notes | (14) |
| add back D&A | +170 |
| less capital investments (company guidance $175-200M) | (187) |
| less stock compensation (run-rate) | (35) |
| less cash tax (nominal at a loss) | (10) |
| **manufacturing owner earnings, before working capital** | **(101) to (51)** |

**The bottom boundary of the manufacturing business's owner earnings in 2026 is
NEGATIVE.** Reported cash flow will look better than that only to the extent
inventory keeps being liquidated.

## HDFS, valued separately

| basis | 100% of HDFS | HOG's 90.2% |
|---|---:|---:|
| Book equity at 2026-06-30 (Note 19) | $377.0M | **$340.1M** |
| Market-tested: KKR/PIMCO paid $46.6M for 9.8% (Q4 2025) | $475.5M | **$428.9M** |

Earning power after the transaction: guided operating income **$55-70M for 2026**
(against $248.4M in 2024 and $490.4M in 2025), i.e. roughly $42-53M after tax on
~$380-440M of equity, an **11-13% return on equity**, on a book funded 5-6x with
debt and deposits. The company projects HDFS operating income reaching
"approximately three times 2026 expected" **in or around 2029**, that is a
four-year projection of a 3x, and it is a projection, treated as such **[E3-48]**.

Credit quality, managed basis (all loans serviced, including sold):
| | 2023 | 2024 | 2025 | H1 2026 |
|---|---:|---:|---:|---:|
| annualised retail credit losses | 3.00% | 3.31% | 3.37% | 3.00% (6mo) |
| 30-day delinquency (period end) | 5.09% | 5.34% | **5.77%** | 4.42% (mid-year) |

Losses and delinquencies rose every year 2023-2025 with "recovery values at auction
values ran below historical levels." H1 2026 shows losses improving and delinquency still
up year-on-year (4.42% vs 4.34% at the same mid-year date).

**The credit risk did not vanish with the sale.** Two-thirds of new originations go
to KKR/PIMCO, but HOG retains one-third on balance sheet, finance receivables
already rebuilt from $1,965M (2025-12-31) to **$2,645M (2026-06-30)**, plus all the
wholesale (dealer floorplan) exposure, plus servicing obligations, plus the
reputational and commercial consequence if the forward-flow buyers tighten credit
into a downturn. Wholesale credit losses rose $4.8M in 2025 "driven by the
charge-off of finance receivables at several troubled dealers."

## Coverage test [E2-54], run on the manufacturing business's obligations

*"all interest, both payable and accrued, comfortably met out of current cash flow
net of ample capital expenditures."*

| | 2024 | 2025 | 2026e |
|---|---:|---:|---:|
| manufacturing interest expense ($M) | 30.7 | 33.4 | ~14 |
| manufacturing OCF less capex ($M) | 336.3 | 131.0 | **negative** |
| coverage | 11.0x | 3.9x | **fails on the guided figures** |

The 2026 failure is not a solvency event, $986M of net cash and $1.28bn of gross
cash sit against $14M of annual interest and a 2045 maturity, so the coverage test's
*consequence* is nil. But the test is failed on flow, and that is the honest reading:
**the manufacturing business's obligations are trivially small; its operating cash
flow in 2026 is guided to be smaller still.**
