## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 5.35%** · **date 2026-09-11** (the latest print; 2026-09-12/13 are a weekend) · source:
  **US Treasury daily par yield curve, 30-year, from the issuing authority**, struck fresh by this run
  through `tools/sources.py:sovereign("USD")` on 2026-09-13. The brief's 5.35% agrees; it was not
  inherited, it was re-read.
- **Earnings currency: USD.** Newegg is a British Virgin Islands company filing Form 20-F as a
  foreign private issuer, but it is a California-headquartered retailer that reports in US dollars and
  sells in the United States: FY2025 net sales by customer location **United States $1,338.8M, Canada
  $96.2M, rest of world $9.4M** of $1,444.5M (20-F Note 17) — **92.7% US, 6.7% Canada, 0.7% elsewhere**.
  *"Our cash and cash equivalents are primarily denominated in U.S. dollars"* (Item 5.B). *"We publish our
  financial statements in United States dollars"* (F-3, 2026-06-01). The 241 employees in China and 22 in
  Taiwan (Item 6.D, 263 of 714) are an RMB/TWD **cost exposure**, not a repricing of the earnings
  currency, exactly as ARM's rupee and sterling wages were. **And the filer says it is taxed as a US
  corporation:** *"We believe that we are an inverted corporation for U.S. federal tax purposes ... we will
  be treated for all U.S. federal tax purposes as if we are a U.S. corporation"* (Item 3.D). The USD
  sovereign is the right one; no FX conversion is needed.
- **No ADS.** The Common Shares themselves are listed: *"Common Shares, par value $0.43696 | NEGG | The
  Nasdaq Capital Market"* (20-F cover). One quote, one class: *"Each share of common stock is entitled to
  one vote"* (Note 11). ARM's ADS-ratio step does not arise.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 20-F, FY ended 2025-12-31, filed 2026-04-28, accession `0001213900-26-048633`**, primary document
  `ea0286017-20f_newegg.htm` — the anchor annual document. Read: Item 3.D risk factors (competition,
  memory shortage, vendor terms, credit agreements, the pledged-share and controlling-shareholder
  factors, controlled-company exemptions, Nasdaq compliance, the Chairman's detention), Item 4
  (history, the share combination, business model, sourcing concentration, private labels, platforms,
  fulfilment, competition, properties), Item 5 (key metrics, revenue by stream, cost of sales by
  component, SG&A by component, results, GMV and Adjusted EBITDA reconciliations, cash flows, capex,
  credit agreements), Item 6 (directors, compensation, bonus programs, plans, the CEO's employment
  agreement, board practices, involvement in legal proceedings, committees, employees), Item 7 (major
  shareholders, the pledge, three-year ownership table), Items 15, 16C, 16E, 16G, the auditor's report
  and critical audit matter, the four statements and Notes 1 (organisation, share combination), 3
  (policies), 4 (fair value), 5 (PP&E), 6 (Bitmain), 7 (accrued liabilities), 8 (lines of credit), 11
  (common stock, ATM), 12 (stock-based compensation), 13, 14, 15, 16 (related parties), 17 (segment,
  category, geography), 18 (subsequent events).
- **Form 20-F FY2024** (`0001213900-25-036055`, filed 2025-04-28), **FY2023** (`0001213900-24-035840`,
  2024-04-24), **FY2022** (`0001213900-23-033334`, 2023-04-27) and **FY2021** (`0001213900-22-022346`,
  2022-04-28) — read for the 2019–2024 cash-flow statements, the key-operating-metrics tables in each
  vintage (the [E2-49] check), revenue by stream and cost-of-sales components, and the 2019 related-party
  loan's origin.
- **Form 6-K, Q2 2026 results, furnished 2026-08-27, accession `0001213900-26-094402`** (EX-99.1) —
  **the current perimeter document**: unaudited balance sheet at 2026-06-30, six-month cash-flow
  statement, the credit-agreement extension to 2026-11-25. Every level-setting balance-sheet figure below
  is from it.
- **Form 6-K earnings releases**: FY2025 (`0001213900-26-048303`, 2026-04-28, carries FY2026 guidance),
  Q1 2026 (`0001213900-26-061809`, 2026-05-28), H1 2025 (`0001213900-25-079437`, 2025-08-21), FY2025
  guidance 6-K (`0001213900-25-098392`, 2025-10-14), FY2024 (`0001213900-25-035774`, 2025-04-28, no
  guidance), FY2023 (`0001213900-24-035566`, 2024-04-24, carries FY2024 guidance). *The CGNX companion
  rule was followed — every release was pulled before scoring [E4-29] and [E4-22]'s third flag.*
- **Governance 6-Ks**: ATM sales agreement (`0001213900-25-063935`, 2025-07-15); ATM upsizing and the East
  West Bank foreclosure on the founder's pledged shares (`0001213900-25-078137`, 2025-08-19); the Third
  Amendment to the Shareholders Agreement loosening the right of first refusal (`0001213900-25-077585`,
  2025-08-15); the CEO's election to the board (`0001213900-25-075279`, 2025-08-13); Chang's
  self-reappointment (`0001213900-25-113726`, 2025-11-24); the Chairman's detention (`0001213900-26-005772`,
  2026-01-20) and release (`0001213900-26-019915`, 2026-02-24); Galkin's board nominee
  (`0001213900-26-012278`, 2026-02-04).
- **Form F-3, filed 2026-06-01, accession `0001213900-26-063041`** (and F-3/A `0001213900-26-067370`,
  effective 2026-06-12) — a $250M primary shelf plus **7,000,000 secondary shares for the three
  controlling holders**; the registrant's own share count and non-affiliate float.
- **Forms 4, 2025-07 to 2026-09-10** (104 transactions parsed from the XML, `form4_2025-2026.txt` in the
  research folder).
- **Figure cross-checked against the filed statement:** *Net cash used in operating activities*, FY2025
  Consolidated Statements of Cash Flows, **$(26,973) thousand** — agrees with XBRL
  `NetCashProvidedByUsedInOperatingActivities` −26,970,000 as used by `tools/run.py` (−27), and with the
  MD&A summary *"$(27.0)"*. *Stock-based compensation* **21,659**, *Depreciation and amortization*
  **7,591** and *Payments to acquire property and equipment* **(2,691)** likewise agree to the thousand.
  **Equity recomputed from A − L [E5-32]:** 468,907 − 308,199 = **160,708**, as filed. Q2 2026:
  422,458 − 251,303 = **171,155**, as furnished.
- **One XBRL defect found in the filer's own tagging, recorded, not used:** the FY2021 20-F tags 2020 and
  2021 `NetIncomeLoss` as **−30.43 and −36.26** where the filed statement reads **net income $30,426 and
  $36,262**, and the FY2022 20-F tags 2022 as **+57.43** where the filed statement reads a **net loss of
  $(57,429)**. Three sign errors in two vintages. Operating cash tags agree with the statements in every
  vintage, so owner earnings are unaffected — but a screen reading net income off this filer's tags would
  have read the 2022 loss as a profit.

**Price, shares and cap — how a 20-F filer's count was derived:**
- **price $14.67**, 2026-09-11 close (Yahoo chart via `tools/sources.py:price` — **aggregator, live quote
  only, flagged** per operator rule 5).
- **`Screens/cover_shares.py NEGG` returned 20,972,505 as of 2025-12-31** — the 20-F cover count. As
  recorded in the resume note, it cannot see a later count because 6-Ks carry no cover tag. **So the count
  was walked forward by hand through four filed documents:**

| as of | count | document |
|---|---|---|
| 2025-12-31 | 20,972,505 | 20-F cover, `0001213900-26-048633` |
| 2026-03-31 | 20,973,060 | 20-F Item 7.A, same document |
| 2026-05-26 | **20,973,423** | F-3 cover and selling-shareholder table, `0001213900-26-063041` |
| 2026-06-30 | 20,974 thousand | Q2 2026 6-K balance sheet, `0001213900-26-094402` |
| 2026-06-30 → 09-10 | **+31,923 net** (CEO PRSU vest 69,323 less 37,400 withheld, 2026-08-31) plus ~+230 net from routine RSU vests | Forms 4 |

- **shares used: ~21,006,000** (the F-3's precise 20,973,423 plus the Form 4 net issuance since). The
  difference between that and the plain F-3 count is 0.15%; it is carried, not argued.
- **Share consolidation checked: a twenty-for-one share combination took effect 2025-04-07**
  (*"On April 7, 2025, the Company effected a share combination ... at a ratio of twenty-for-one"*, Note 1;
  the Yahoo split event reads 1:20 on the same date). **Every count above post-dates it**, so the
  split-invariant construction `cap = close(anchor) × shares(measurement) × splits AFTER measurement`
  applies a factor of 1. The par value moved $0.021848 → $0.43696, exactly ×20, which is the check that
  the combination is the only one. (Pre-combination share counts in the FY2021–FY2024 20-Fs — e.g. 366.7M
  weighted shares in 2021 — are ×20 the post-combination basis; none is used for the cap.)
- **Market cap $308M** (21,006,000 × $14.67 = $308.2M; on the F-3 count alone $307.7M). The queue's
  `cap_m 332` is the same construction at about $15.83; the price moved. `tools/run.py` printed $0.31bn
  on 21.0M, which agrees.
- **Who owns it, and the free float — the controlling shareholder is not Liaison Interactive in name
  only; it is a distressed Chinese parent whose Newegg shares are pledged to a bank that has won a final
  judgment.** Item 7.A at 2026-03-31: **Zhitao He 11,835,144 (54.6%)** — Digital Grid (Hong Kong), a
  wholly owned subsidiary of Hangzhou Lianluo Interactive Information Technology Co., holds 11,141,079
  (a Lianluo warrant for 6,250 at $352.00, 2,946 through Hyperfinite, and 684,869 vested options at
  $10.95 make up the rest); **Fred Chang, the founder, 4,689,596 (21.9%)**; **Vladimir Galkin 4,392,812
  (20.9%)**. **The registrant's own non-affiliate count: *"20,973,423 Common Shares outstanding, of which
  1,273,376 Common Shares were held by non-affiliates"*** (F-3, 2026-05-26) — **a free float of 6.1%,
  worth $18.7M at $14.67.** The $308M cap is **16.5x the value of the shares that trade.** (ARM's was
  7.3x.) Recorded here; weighed at Q3 as the control case and at Q4 as the pledge.

---
# STAGE 0 — THE SCREEN ROW, REBUILT BY HAND, AND THE THREE EXPLODING RATIOS

## The first finding is that the screen's "16 years filed" are two different companies

**This CIK was not Newegg until 2021-05-19.** EDGAR's own `formerNames`: **Dehaier Medical Systems Ltd
(2009-11-12 to 2016-11-18)** and **Lianluo Smart Ltd (2016-11-22 to 2021-05-12)** — a Beijing
medical-device and smart-hardware company that filed 10-Ks, then 20-Fs, on revenue of $0.4M to $21.6M a
year. *"Newegg Commerce, Inc. (previously known as 'Lianluo Smart Limited' or 'LLIT') ... References to the
'Merger' refer to the merger of Newegg Inc. with Lianluo Smart Limited"* (20-F, Background). Newegg Inc.
was the accounting acquirer, so from the FY2021 20-F onward the comparative years 2019–2020 were **re-filed
as Newegg's**, under the same element names, **on top of Lianluo's own earlier values for the same period
ends.** Companyfacts therefore carries two companies' numbers for 2019-12-31 and 2020-12-31, and which one
a screen reads depends only on which vintage it prefers:

| period end | `NetCashProvidedByUsedInOperatingActivities` | `DepreciationDepletionAndAmortization` | `IncreaseDecreaseInAccountsPayable` | whose |
|---|---|---|---|---|
| 2018-12-31 | −3.63 | 0.83 | +0.19 | **Lianluo only** |
| 2019-12-31 | −1.67 (20-F 2020-05-15) · **−10.08** (20-F 2022-04-28) | 0.78 · **10.71** | −0.01 · **−100.73** | Lianluo · **Newegg** |
| 2020-12-31 | −2.34 (20-F 2021-03-31) · **+84.51** (20-F 2022-04-28) | 0.45 · **9.09** | −0.06 · **+76.34** | Lianluo · **Newegg** |
| 2021-12-31 → | Newegg only | | | |

($M. Reproduced from `companyfacts.json` by `facts.py` in the research folder; the Newegg values agree with
the FY2021 20-F cash-flow statement to the thousand: −10,077 / 84,512; 10,708 / 9,091; −100,733 / 76,337.)

## The three flags, in dollars, year by year

**THE DENOMINATOR, which is the whole story** — Newegg's own operating cash, filed statements, $M:

| FY | **OCF** | **Δ accounts payable** | Δ inventories | **D&A** | SBC | capex | net income |
|---|---|---|---|---|---|---|---|
| 2019 | **−10.1** | **−100.7** | +110.1 | **10.7** | 0.7 | 10.3 | (17.0) |
| 2020 | **+84.5** | **+76.3** | −76.2 | **9.1** | 1.6 | 6.2 | 30.4 |
| 2021 | **−53.3** | **−20.1** | −70.8 | **10.8** | 6.3 | 13.8 | 36.3 |
| 2022 | **+20.5** | **−14.1** | +78.8 | **11.0** | 33.9 | 9.2 | (57.4) |
| 2023 | **−3.8** | **−0.9** | +16.8 | **13.4** | 33.7 | 30.3 | (59.0) |
| 2024 | **−0.8** | **−57.4** | +32.9 | **10.7** | 27.3 | 3.6 | (43.3) |
| 2025 | **−27.0** | **+11.6** | −70.9 | **7.6** | 21.7 | 2.7 | (4.9) |
| H1 2026 | −19.5 | −37.5 | −24.2 | 2.6 | 0.4 | 1.8 | 10.0 |
| **TTM to 2026-06-30** | **+3.5** | +4.7 | −40.0 | **5.8** | **10.4** | 3.2 | 9.3 |

(Filed statements: FY2021 20-F for 2019–2021, FY2022 20-F for 2022, FY2025 20-F for 2023–2025, Q2 2026
6-K for the half-years. Inventory sign as the cash-flow statement shows it: a negative is a build.)

**1. `wc_note` — accounts payable at 6,992% of a year's operating cash (2024).** In dollars: **payables
fell $57.4M in a year when operating cash was −$0.8M** (57,403 ÷ 821 = 69.9x). The payables move is real
and large — it is **39% of the year-end payables balance of $148.3M** and it was offset by **$32.9M of
inventory released and $14.5M of receivables collected**, so operating cash landed near zero by
coincidence of offsetting lines, not because the business was at breakeven. *"We purchase our inventory
from vendors on trade accounts typically requiring payment between 30 and 60 days ... As of December 31,
2025, our accounts payable balance was $160.3 million with 46 days of payables outstanding"* (Item 3.D).
**Read in dollars, 2024 says: vendor credit shrank by $57M as the business shrank ($1,497M → $1,236M of
sales), and the ratio says nothing.** The tool's own note already concedes this ("arithmetic on a near-zero
denominator").

**2. `best_year_dep 99.178` — one year carries the window at 9,918%.** Reproduced to the third decimal by
`floor_screen.best_year_dependence()` on the newest-vintage nine-year OCF series, **which is: 2017 −5.41
(Lianluo), 2018 −3.63 (Lianluo), 2019 −10.08, 2020 +84.51, 2021 −53.29, 2022 +20.48, 2023 −3.84, 2024 −0.82,
2025 −26.97.** Its mean is **+$0.11M**. Drop the best year — **2020's +$84.5M, the pandemic PC boom, when
payables rose $76.3M and deferred revenue $21.8M** — and the other eight average −$10.4M. (−10.4 ÷ 0.11 is
the 99x.) **In dollars and a word: the nine-year mean is zero, two of its nine years belong to a Beijing
medical-device company, and the "window" is one pandemic year of vendor credit set against eight years
of cash consumption.** Owner earnings are never computed from this series.

**3. `da_note` — D&A steps 12.9x at 2019-12-31.** In dollars: **$0.83M (Lianluo Smart's 2018 D&A) to
$10.71M (Newegg Inc.'s 2019 D&A)** — 10.71 ÷ 0.83 = 12.9. **Not an acquisition, not a change of estimate,
and not a semantics change within one filer: it is a splice of two companies under one CIK**, a new, fourth
cause for the flag's docstring, which names three. (Read on the earliest vintage the same splice moves to
2021 and reads 24.0x: $0.45M Lianluo 2020 → $10.84M Newegg 2021.) **Newegg's own D&A has never stepped**:
$10.7M, 9.1, 10.8, 11.0, 13.4, 10.7, 7.6 (2019–2025) — a gentle schedule, rising with the 2023 headquarters
purchase and falling as warehouses were consolidated and subleased. Note 5: *"Depreciation and
amortization expense associated with property and equipment was $7.6 million, $10.7 million and $13.0
million"*; the cash-flow add-back is slightly larger (7,591 / 10,703 / 13,437) because it includes
non-PP&E amortisation. **Both ends of (c) are usable once the splice is removed.**

## Owner earnings, rebuilt — Newegg only, filed statements

Construction as everywhere in this queue: **OCF − SBC − (c)**, with (c) at total capex (one end) and D&A
(the other). SBC resolves in every year and is **complete**: the cash-flow add-back equals the equity
statement's *"Stock-based compensation"* credit to APIC in every year checked (21,659 / 27,255 / 33,660 /
33,939), Note 12 attributes it to RSUs, PRSUs and options, and **no stock-settled 401(k) or other
equity-settled line exists** — the 401(k) match is cash, $1.2M (Note 15). The BE and Boeing defects do not
recur here.

| FY | OE (capex end) | OE (D&A end) |
|---|---|---|
| 2019 | −21.1 | −21.5 |
| 2020 | **+76.7** | **+73.8** |
| 2021 | −73.4 | −70.4 |
| 2022 | −22.6 | −24.5 |
| 2023 | −67.8 *(capex includes the $23.2M HQ building)* | −50.9 |
| 2024 | −31.7 | −38.8 |
| 2025 | −51.3 | −56.2 |
| TTM to 2026-06-30 | −10.1 | −12.7 |

| window | capex end | D&A end |
|---|---|---|
| **3-yr 2023–25** | **−50.3** | **−48.6** |
| **5-yr 2021–25** (the corpus default [E2-42]) | **−49.4** | **−48.2** |
| 7-yr 2019–25 (includes the pandemic year) | −27.3 | −26.9 |
| TTM to 2026-06-30 | −10.1 | −12.7 |

**The screen's `oe_bottom −50 / oe_top −48` reproduces exactly on the 3- and 5-year windows.** The splice
never touched it, because `owner_earnings()` starts at 2021. **What the splice corrupted was only the three
diagnostic flags.**

**THE SENSITIVITY THE READER WILL ASK FOR, AND WHY IT IS NOT OWNER EARNINGS.** Operating cash here is
dominated by inventory and payables timing, so the cash-flow statement was also read **before** its
working-capital lines *(CONVENTION: a disclosed sensitivity to show how much of the negative is timing; it is
not the owner-earnings figure, because [E2-23] puts the working-capital increment inside (c) where the
business requires it, and a retailer building inventory into a memory shortage requires it)*:

| | pre-working-capital OCF | less SBC | less capex | less D&A instead |
|---|---|---|---|---|
| 2023 | −15.6 | −49.2 | **−79.5** | −62.7 |
| 2024 | −0.6 | −27.9 | **−31.5** | −38.6 |
| 2025 | +28.1 | +6.4 | **+3.8** | −1.1 |
| TTM to 2026-06-30 | +31.0 | +20.6 | **+17.4** | +14.8 |

**So: negative on every multi-year window at −$27M to −$50M; −$10M to −$13M on the trailing year; and
positive, +$15M to +$17M, only on the trailing year with working capital set aside and SBC taken at a
trailing $10.4M that the 2021-era RSU cliff has temporarily emptied** ($21.1M unrecognized at YE2024, $1.0M
at YE2025 — and **249,061 new RSUs granted 2026-07-29**, Forms 4). **The rebuilt range, in dollars and a
word: −$50M to −$10M — NEGATIVE; the trailing pre-working-capital sensitivity is the only construction
above zero, and it is the strongest fact against this file's conclusion.** It is carried to Q4 and weighed
there.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Newegg is **a reseller of other companies'
computer parts**, with a small commission business bolted on. It buys GPUs, CPUs, memory, drives,
motherboards and prebuilt PCs from about 280 suppliers — **the ten largest supply 68.8% of what it buys;
66.0% comes straight from manufacturers, 30.7% from distributors** (Item 4.B) — holds them in three leased
warehouses (Southern California, Indiana, Ontario), and ships them to hobbyists, gamers and businesses who
ordered on a website. **For every $100 of its own goods it sells, about $87 goes to the supplier and $3 to freight;
about $9.50 of gross margin is left on its own inventory (2025), and card processors then take another
$2.40 of every sales dollar out of SG&A before a warehouse, a website or a salary is paid.** On the third-party side it lets 5,100 sellers list 4.5 million SKUs and
keeps **about 8 cents of each marketplace dollar**. Vendors also pay it — rebates, marketing funds, price
protection — **$48.5M of such receivables at year-end, the auditor's one critical audit matter.** The
business turns inventory on vendor credit: at 2025-12-31 **payables of $160.3M financed 96% of $166.3M of
inventory.**

**Filed revenue and gross margin by line** (20-F Item 5.A revenue and cost-of-sales tables, $M;
*CONVENTION: the cost-of-sales table does not split freight and write-downs by line — they are assigned to
direct sales, where the inventory and the parcels are, which slightly flatters marketplace and services;
the two lines reconcile to filed gross profit to $0.1M in 2023–2025; in 2020–2022 an unallocated residual of
$1.6M–$5.9M — reserve releases and other small cost lines — sits in neither*):

| FY | direct sales | direct margin after freight & write-downs | marketplace commission | services | marketplace + services margin | **gross profit (filed)** | GP % |
|---|---|---|---|---|---|---|---|
| 2020 | 1,974.9 | 207.1 (10.5%) | 57.6 | 82.4 | 70.1 | 273.7 | 12.9% |
| 2021 | 2,243.4 | 254.4 (11.3%) | 63.5 | 69.3 | 73.2 | 326.0 | 13.7% |
| 2022 | 1,607.0 | 146.8 (9.1%) | 47.0 | 66.3 | 63.9 | 216.6 | 12.6% |
| 2023 | 1,396.6 | 118.1 (8.5%) | 32.3 | 68.1 | 49.5 | 167.6 | 11.2% |
| 2024 | 1,123.5 | 92.1 (8.2%) | 25.2 | 86.9 | 39.4 | 131.5 | 10.6% |
| 2025 | 1,394.8 | 132.0 (9.5%) | 28.6 | 21.1 | 36.5 | 168.5 | 11.7% |
| H1 2026 | — | — | — | — | — | 83.5 | 13.3% |

**Against that gross profit sits an operating cost that has never been covered on a GAAP basis since the
pandemic**: SG&A **$178.0M in 2025** (salaries $87.0M incl. SBC, merchant fees $34.4M, marketing $13.0M,
D&A $7.6M, other $36.0M). **Operating result: 2022 −$49.5M, 2023 −$71.1M, 2024 −$51.6M, 2025 −$9.5M;
H1 2026 +$8.8M.** 2020 and 2021 were the only operating profits in the seven years filed ($23.4M, $33.5M).

**GMV, customers and units [E4-55] — the physical series, and it is shrinking:**

| FY | GMV | of which marketplace | take rate | active customers (12-mo) | repeat rate | AOV | visits |
|---|---|---|---|---|---|---|---|
| 2019 | 1,977.6 | 495.2 | 9.2% | 3.2M | 30.0% | $310 | 262.2M |
| 2020 | 2,745.2 | 663.7 | 8.7% | **4.7M** | 32.5% | $301 | 382.2M |
| 2021 | 3,028.4 | 742.4 | 8.6% | 3.5M | 31.9% | $442 | 305.1M |
| 2022 | 2,196.1 | 552.2 | 8.5% | 2.7M | 31.3% | $411 | *(~241M, narrative only)* |
| 2023 | 1,812.5 | 369.7 | 8.7% | 2.5M | 29.2% | $379 | — |
| 2024 | 1,533.7 | 318.6 | 7.9% | 2.1M | 26.0% | $396 | — |
| 2025 | 1,770.5 | 350.2 | 8.2% | **2.2M** | 26.9% | **$448** | — |

(FY2021, FY2022, FY2023, FY2025 20-F key-metrics and GMV reconciliation tables; take rate = marketplace
revenue ÷ marketplace GMV.)

**Is revenue units or price? Price.** FY2025 net sales rose 16.9%, and the filing says why: *"primarily
attributable to robust demand and higher selling prices for next-generation PC components ... Average
selling prices were further supported by macroeconomic factors, including tariff uncertainties and
component shortages."* AOV rose **13.1% ($396 → $448)** while active customers rose 4.8% and the repeat rate
0.9 points. **Against 2019, GMV is 10% lower in nominal dollars while AOV is 45% higher, so orders are down
by roughly 38%** *(CONVENTION: GMV ÷ AOV as an order proxy; on net sales ÷ AOV the fall is 35% — the
filing defines AOV as "sales volume by number of transactions" without saying which sales figure)*. **The
Q1 and Q2 2026 releases say the quiet part in words**: *"The industrywide shortage has driven memory and
storage component prices significantly higher, which has elevated average selling prices and further
pressured unit volumes"*; *"consumers pulled back on purchase volume."* This is [E4-55]'s Precision Steel
shape exactly — dollars flattered by price while the physical series falls — and the corpus's reading
of it is *"a serious reverse, not likely to disappear in some 'bounce back' effect."*

**[E2-49] — was a yardstick withdrawn? YES, twice, and both followed deterioration.** (The prior stood at
nine fires and seven failures; this is checked, not assumed.)
1. **Total visits and conversion rate were dropped from the key-metrics table between the FY2021 and
   FY2022 20-Fs.** The FY2021 table carried six metrics — *"Total visits 305.1 million | 382.2 million |
   262.2 million"*, number of customers, active customers, *"Conversion rate 2.3% | 2.4% | 2.4%"*, repeat
   rate, AOV. **Visits had just fallen 20% and conversion had just ticked down.** The FY2022 table carries
   three (active customers, repeat rate, AOV); visits survive only as a narrative line (*"an average of 20.1
   million visits per month in 2022"* — about 241M, down another 21%), and by FY2025 not at all.
2. **In 2026 the active-customer and repeat-rate definitions were switched from 12 months to three months
   in the quarterly releases** — Q1 2026: *"Active customers, defined as unique customer IDs with at least
   one item purchased on Newegg platforms in the past three months, totaled approximately 0.57 million"*,
   down from 0.67M; repeat rate *"17.59% ... compared to 22.12%"*. The switch **is** disclosed and the prior
   year is restated on the same basis — which is the candor half of [E2-49] — but it arrived in the first
   quarter the 12-month series could no longer be read as a recovery, and the 20-F still reports the
   12-month form. **Fired, and scored honestly: the first withdrawal is a clean fire; the second is a
   disclosed switch whose timing matches the rule's description.** The prior now stands at **ten fires and
   seven failures.**

**The scarce input this business controls.** **Very little, and the filing says so first**: *"The e-commerce
market is intensely competitive with limited barriers to entry"* (Item 3.D, the second risk factor in the
book). What it has: (1) a **25-year brand and a review base** — 4.9 million customer reviews, *"87% of traffic
was free"* in 2025 (Item 4.B); (2) **authorised-reseller allocation** from the GPU and CPU makers — *"early
allocation of new products, preferential allocation of products in shortage"* — which is the input that
mattered in 2025's memory shortage; (3) a PC-builder community. **None of the three is owned**: the traffic
arrives through Google and affiliates (paid search is 49% of marketing spend), the allocation is the
suppliers' to give, and the ten suppliers who hold 68.8% of the purchases also *"sell their products directly
to customers"* (Item 5).

**Will the fundamentals look broadly the same in ten years?** **The business model will — reselling
components is a 25-year-old model and will still be one — but the size of it has not held still for any
five-year stretch in the record**: GMV $1.98bn → $3.03bn → $1.53bn → $1.77bn in six years, active customers
3.2M → 4.7M → 2.1M. The direction of the physical series is down, and the category's own manufacturers,
Amazon and the club and big-box stores are all in the same aisle.

**The Q1 test is understanding, not quality [E4-46].** The mechanism is plain: buy parts on 30–60-day vendor
terms, sell them for a ~9.5% product margin plus an ~8% marketplace commission, pay warehouses, card fees and
people out of what is left. A reader can predict the *direction* of cash flows from three observable things
— component price cycles, vendor terms and unit demand — and the filing discloses all three. **What cannot
be predicted is the level**, and that is a Q2 and Q4 question, not a failure to understand how the money is
made. No five-month study is needed to know what this company does; **Q1 does not close the file on
competence**, and it must not be allowed to close it on dislike.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *The evidence is here and it clears: a reseller-and-marketplace whose unit economics are disclosed line
  by line. Nothing about IN here is a compliment — [E4-46]'s bar is understanding, and the understanding is
  what makes Q2 answerable.*

