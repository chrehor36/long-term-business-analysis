# Company Run — NEWEGG COMMERCE, INC. (NEGG) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Written under the write-early protocol; closed 2026-09-13. Research folder: `Test Runs/_research 2026-09-13 NEGG/`. The tier-3 label ("negative on every construction ... the file's work is Q1-Q2") is read as UNLABELLED per the dated correction of 2026-09-12; every gate is open.*

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
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

**[E2-49] — was a yardstick withdrawn? YES, twice, and both followed deterioration.** (The brief put the prior at nine fires and seven failures; the register already read **ten and seven** after FLNC
fired it on 2026-09-12. Checked, not assumed.)
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
   disclosed switch whose timing matches the rule's description.** The prior now stands at **eleven fires and
   seven failures** (SHOP, MRVL, PAY, ARM, CALX, BE, ROKU, SWK, ACVA, FLNC, NEGG; QLYS, CRM, CORT, PLTR, INOD, ACMR, ALKT).

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

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its customers to
> have **no close substitute** and; (3) is not subject to price regulation." — **[E3-03]**

- Needed or desired **[x]** — PC components and electronics are wanted; $1.44bn of them were bought here in 2025.
- No close substitute **[ ]** — **fails; argued below.**
- Not price-regulated **[x]** — no administered price anywhere in the chain; tariffs raise costs, they do not set margins.

**My prior was OUT on criterion (2). It was framed to be refuted [E4-26], so the bull case is built first,
as its holders would state it [E4-51].**

### THE BULL CASE, built as its holders would state it

1. **A 25-year specialist brand with an audience it does not rent.** *"In 2025, 87% of traffic was free, as
   compared to the paid traffic of 13%"*; 4.9 million customer reviews; a PC Builder tool and a gamer
   community (Item 4.B). The enthusiast who builds a PC buys a motherboard, CPU, GPU, memory, drives, case,
   cooler and power supply in one basket, and **Newegg is where that basket has been assembled since 2001.**
2. **Authorised-reseller allocation is real, and 2025 proved it.** *"Due to our strong supplier relationships
   and our purchasing volume, we are able to obtain ... early allocation of new products, preferential
   allocation of products in shortage"* (Item 4.B). **When DRAM prices rose ~172% (Item 3.D), Newegg had the
   stock**: gross margin 10.6% → 11.7% (2025) → **13.3% (H1 2026)**, gross profit up in Q1 2026 on sales down
   11.8%, and **H1 2026 net income $10.0M** — the first positive half since 2021.
3. **A capital-light marketplace layer on top.** 5,100 sellers, 4.5 million SKUs, commissions of 8–15% on
   $350M of marketplace GMV, and fulfilment and advertising services sold to the same sellers — revenue
   that carries no inventory.
4. **The working capital is financed by the suppliers.** Payables of $160.3M carried 96% of $166.3M of
   inventory at year-end, and capex has fallen to $2.7M a year. **A holder would say this is a retailer
   that needs almost no capital of its own** — the second half of [E2-44].
5. **B2B is growing and the costs are out.** B2B net sales $200.2M → $245.4M (2025); SG&A $238.6M (2023)
   → $178.0M (2025); headcount 762 → 714; warehouses consolidated and subleased.

### THE ATTACK

**1. Criterion (2): the product is not Newegg's, and the customer can buy the identical box elsewhere.**
An RTX 5080 or a Ryzen 9 is **the same SKU, same manufacturer warranty, same serial number range** at
Amazon, Best Buy, Micro Center, Walmart's marketplace, B&H, or the manufacturer's own store. The filing does
not dispute this; it says it: *"The e-commerce market is intensely competitive with limited barriers to
entry"*; *"some of our competitors have used and may continue to use aggressive pricing or promotional
strategies, may have stronger supplier relationships with more favorable terms and inventory allocation"*;
*"Because our manufacturers and distributors have access to merchandise at a lower cost than we do, they
could sell products at lower prices and maintain a higher gross margin on their product sales than we can
... This could result in our current and potential buyers deciding to purchase directly from these
manufacturers"* (Item 3.D). **And the pricing mechanism is stated in its own words: *"We are also able to
find optimized pricing points by leveraging our data and analytics capabilities and by monitoring our major
competitors' pricing trends"* (Item 4.B).** A business that sets its price by watching its competitors'
prices is, by its own description, selling a thing its customers treat as having close substitutes.

**2. [E2-44] both halves, through the 2022–24 PC-hardware downturn — and against Best Buy, which went
through the same downturn.** *Half one: can it raise prices "even when product demand is flat and capacity
is not fully utilized"?* When demand fell, Newegg's margin fell with it:

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | peak → trough |
|---|---|---|---|---|---|---|
| **Newegg net sales $M** | 2,376.2 | 1,720.3 | 1,497.0 | 1,235.6 | 1,444.5 | **−48.0%** |
| **Newegg gross margin** | 13.7% | 12.6% | 11.2% | **10.6%** | 11.7% | **−3.1 pts** |
| Newegg direct-sales margin after freight *(CONVENTION above)* | 11.3% | 9.1% | 8.5% | 8.2% | 9.5% | −3.1 pts |
| **Best Buy Computing & Mobile Phones revenue $M** (FY ending Jan–Feb of the next year) | 20,693 | 18,191 | 16,930 | 17,103 | 18,038 | **−18.2%** |
| **Best Buy gross margin (enterprise)** | 22.5% | 21.4% | 22.1% | 22.6% | 22.5% | **−1.1 pts, then fully recovered** |

(Best Buy 10-Ks FY2022–FY2026, revenue-by-category tables and XBRL; the fiscal year ending 2022-01-29 is
set against Newegg's calendar 2021, and so on.) **Best Buy's computing revenue fell by nearly a fifth and its margin
rate held; Newegg's revenue halved and its margin rate lost almost a quarter of itself.** *Half two: can it
grow dollar volume "with only minor additional investment of capital"?* Dollar volume did not grow across
the window — it fell by two-fifths from 2021 to 2025 ($2,376.2M to $1,444.5M) — and **the one year it grew, 2025, the growth consumed
$70.9M of inventory and took operating cash to −$27.0M.** Both halves fail.

**3. [E4-55] — the physical series is the honest one, and it is falling.** Active customers **4.7M (2020) →
2.2M (2025)**; repeat purchase rate **32.5% → 26.9%**; orders down roughly **38% from 2019** on the GMV ÷ AOV
proxy; visits dropped from the metrics table the year they fell 20%. **And the 20-F's own opening paragraph carries three more physical series,
restated each year (Item 4.A, FY2021–FY2025 20-Fs): cumulative orders since 2005 of *"over 176 million"* (2021),
187M, 193M, 198M, 203M — so roughly 11M orders in 2022, then about 6M, 5M and 5M a year (±1M on "over" rounding);
distinct items bought *"over 675,000"* (2021) → 604,000 → 436,000 → 302,000 → 312,000; and SKUs offered *"more than 38
million"* from 56,000 brands (2021) → 20M/51,000 → 6M/35,000 → 4M/27,000 → 4.9M/22,000.** On the filer's own
cumulative count, **annual orders are less than half what they were in 2022**. **2025's 16.9% revenue growth was
price** — AOV +13.1% — and the 2026 releases say unit volumes are being *"further pressured"*. Precision
Steel's pounds fell while dollars held; the corpus called it *"a serious reverse, not likely to disappear in
some 'bounce back' effect."*

**4. [E4-32] — direction outranks existence, and every direction series narrowed 2021–2024.** Marketplace
GMV **$742.4M → $318.6M**; marketplace take rate 8.6% → 7.9%; services revenue $86.9M → **$21.1M** in 2025
(*"reduced business from certain 3PL customers"*). B2C net sales did rise, $0.9bn → $1.2bn in 2025 — on price. **Whatever moat the bull case describes, it was narrower in 2024
than in 2021 on every physical measure the company files**, and 2025's widening is in dollars only.

**5. [E4-36] and [E3-51] — the record's only profits came from two waves, not from a castle.** Of the seven
Newegg years filed, **operating profit came in 2020 and 2021 (the pandemic PC boom: $23.4M and $33.5M) and
in H1 2026 (the memory shortage: $8.8M)** — and the filing names the cause each time: *"customers tend to
find better solutions to help them work, learn, entertain, and stay connected while being at home"* (FY2021);
*"By leveraging a favorable cost basis for memory-related components before Q4 supply constraints, we
realized significant margin expansion"* (FY2025); *"our early procurement of constrained categories continued
to pay off this quarter"* (Q2 2026). **Buying inventory ahead of a shortage is a trade that pays when prices
rise and costs when they fall** — the Item 3.D risk factor says the second half: *"products purchased at
elevated prices may be difficult to sell at margins sufficient to cover our costs if demand softens or prices
decline."* That is [E4-36]'s fourth cause, wave-riding, and [E3-51]'s surfer: *"if he gets off the wave, he
becomes mired in shallows."* **Of the four causes of extreme success, the only one this record shows is the
one that is not ownable.**

**6. [E2-58] — the commodity equation, from the reseller's seat.** The goods are undifferentiated, the
capacity to sell them online is effectively unlimited, and there is no administered price. The corpus's one
exception is *"a cost advantage that is both wide and sustainable"* — and **Newegg's filing says its
suppliers and larger rivals have the cost advantage over it, not the reverse** (point 1). The shortage gains
of 2025–26 are [E3-62]'s second step in miniature: they accrue to whoever holds inventory when the price moves,
and **in a glut they flow straight back to the buyer** — which is what 2022–24's margin compression was.

**7. [E2-45] — the attacker's test has already been run, by Amazon, and the result is on file.** *"How I would
like, assuming I had ample capital and skilled personnel, to compete with it."* Nothing about Newegg's
position requires a new invention to attack: the SKUs are the manufacturers', the ten suppliers who hold 68.8%
of its purchases sell to everyone, the traffic arrives through Google and affiliates, and a marketplace is
software. **Amazon's third-party seller services grew to $172.2bn (2025) while Newegg's marketplace GMV halved**;
Amazon's North America segment earned **$29.6bn of operating income on $426.3bn of sales (6.9%)** in 2025 while
Newegg lost $9.5M. **And Newegg sells its own private labels on the attacker's shelf**: *"We offer our Rosewill
and ABS products across our platforms and on other e-commerce platforms, such as Walmart, Amazon, and eBay"*
(Item 4.B) — the channel that owns the customer is not Newegg.

**8. [E5-28] and [E3-33] — no untapped pricing power, because there is no near-monopoly.** Newegg's $1.44bn
of 2025 sales is **8% of Best Buy's computing category alone ($18.0bn) and 0.5% of Amazon's online-stores
line ($269.3bn)**. When the demand wave receded in 2022–24 the company could not hold its price; a business
with untapped pricing power does the opposite.

**9. Key-person and control — recorded at Q2 as the corpus directs [E4-23], though it does not decide this
gate.** The allocation that bull point 2 rests on is a supplier relationship, and **the suppliers can
reallocate**: the ten largest are 68.8% of purchases and *"our contracts or arrangements with such suppliers
generally do not guarantee the availability of merchandise or provide for the continuation of particular
pricing or other practices"* (Item 5). A moat that exists at a supplier's discretion belongs to the supplier.

**Is it a moat that must be continuously rebuilt [E4-04]? Does a lapse in spending destroy it or narrow it?**
Neither framing applies cleanly, because the asset being defended is a **position in a stream of other
companies' product launches**. Each GPU and CPU generation must be re-won — allocation, launch-day stock,
pricing against the same launch at every rival — and the filing says future growth *"should be driven by
product releases or upgrades that may occur in the future. If such product releases do not occur or do not
drive sales ... our future sales may be less than predicted"* (Item 3.D). **That is a basis that is replaced
every product cycle — [E4-04]'s excluded class.**

### THE COMPETITOR ROW — required [E3-28]

**Same metrics, same five-year window (fiscal years ending 2021–2025 or the nearest fiscal equivalent),
filing-sourced.**

| Company | gross margin FY2021 → FY2025 | operating margin FY2021 → FY2025 | revenue, peak-to-trough in the downturn | marketplace take rate 2025 | OCF − SBC − capex, 5-yr sum | source |
|---|---|---|---|---|---|---|
| **Newegg (subject)** | 13.7% → 11.7% (trough 10.6%) | **+1.4% → −0.7%** (trough −4.7%) | **−48.0%** (2021→2024) | **8.2%** | **−$246.8M** | 20-F FY2021–FY2025 |
| **Amazon** (AMZN) | 42.0% → 50.3% consolidated | 5.3% → 11.2%; **North America segment 4.2% (2023) → 6.9% (2025)** | none — net sales rose every year ($469.8bn → $716.9bn) | third-party seller services $172.2bn vs online stores $269.3bn *(fees + fulfilment, not a commission rate)* | −$56.7bn *(the AWS and fulfilment build; not comparable in sign)* | 10-K FY2025 `AMZN_10K_2025-12-31`, XBRL |
| **Best Buy** (BBY) | 22.5% → 22.5% (trough 21.4%) | 5.9% → 3.3% | **−18.2%** on Computing & Mobile Phones (FY22→FY24); enterprise −19.8% | n/a (marketplace launched in Canada; not material) | +$6.0bn *(FY2022–FY2026)* | 10-Ks FY2022–FY2026, XBRL |
| **Walmart** (WMT) | 25.1% → 24.9% | 4.5% → 4.2% | none — net sales rose every year ($572.8bn → $713.2bn) | not disclosed as a rate | n/a *(SBC tag does not resolve undimensioned — the BE limit; OCF − capex +$65.8bn, FY2022–FY2026)* | 10-K FY2026, XBRL; `2026-09-06 Run - WMT Walmart.md` |
| **eBay** (EBAY) | 74.6% → 71.5% *(a pure marketplace)* | 28.1% → 20.5% | −6.0% (2021→2022), recovered | **13.9%** ($11.10bn on $79.6bn GMV) | +$6.6bn *(2021–2025)* | 10-K FY2025, XBRL |
| **Costco** (COST) — named by Newegg as a competitor | 12.9% → 12.8% *(includes membership fees)* | 3.4% → 3.8% | none — revenue rose every year | n/a | not computed | XBRL, FY ending Aug/Sep 2021–2025 |
| **Micro Center** — private | **not filed** | **not filed** | **not filed** | n/a | n/a | **LIMIT STATED**: Micro Center files nothing with the SEC. Its only trace found on EDGAR in 10-Ks since 2025 is as an **anchor tenant** in REIT property tables (Federal Realty 10-K FY2025, `0000034903-26-000017`: Federal Plaza, Perring Plaza, Providence Place) and as a named reseller in Super Micro's 10-Ks. Nothing there measures its economics. |

**Peers named: 6 of the industry's roughly 9 real competitors** — Amazon, Best Buy, Walmart, eBay, Costco
and Micro Center, against the filing's own list (*"superstores such as Best Buy, Costco and Walmart, hardware
and software vendors that sell directly to end users, online retailers such as Amazon"*; *"Temu and Shein"*)
plus the component makers' direct stores, B&H Photo (private) and Micro Center (private, and the one this
basket's customer knows best). **The manufacturer-direct channel, Temu, Shein and B&H are not in the row**: the
first is not segmented in any maker's filing, Temu (PDD) and Shein report nothing at the US-electronics level,
B&H is private.

**Who names whom — a prompt, then a read** (`tools/sources.py:fts_count`, correct ten-digit CIKs, verified by
NEGG's own 54 self-hits; then the latest 10-K of each opened and grepped on disk): **Best Buy, Amazon, eBay and
Walmart name Newegg zero times in their 10-Ks; Newegg names Amazon, Best Buy, Walmart, Costco, Temu and Shein.**
The asymmetry is itself the finding: **the naming runs one way.** Across all 10-Ks filed since 2025, the filers
who name Newegg are a supplier (Super Micro), a card partner (Synchrony) and three micro-caps selling through
it.

**What the row shows, and its limit [E3-61].** On every metric the row can carry, **Newegg is the lowest-margin,
most cyclical and only cash-consuming business in its own competitor set**, and the one whose margin rate
moved with demand. The row cannot show conduct — whether Amazon or Micro Center will price a GPU launch
rationally next year — and the corpus says even Munger had no model for that. **It does not need to**: criterion
(2) fails on the filing's own description of how its prices are set, before the row is read.

- **Untapped pricing power [E3-33]:** **none.** Margin fell when demand fell (2022–24) and rose only when
  supply fell (2025–26). [E5-28]: incredible pricing power requires near-monopoly; Newegg is 8% of one rival's
  computing category.
- **Class:** [ ] WIDE [ ] NARROW **[x] NONE** [ ] PROVISIONAL · **Direction:** narrowing on every physical
  series 2020–2024 (customers, repeat rate, marketplace GMV, visits); dollar widening in 2025 is price.
- **Is the moat class PROVISIONAL because Micro Center is private?** No. A missing peer holds the class
  provisional when the relative claim turns on it; here the claim fails on the subject's own filing
  (price set by watching rivals; suppliers and rivals with the cost advantage) and on four filed peers. Micro
  Center's numbers could make Newegg look better or worse **relative to Micro Center**; they cannot supply the
  missing condition that customers see no close substitute for a manufacturer's boxed part.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  **OUT on [E3-03] criterion (2):** the goods are identical SKUs sold by larger rivals and by the
  manufacturers themselves, and the company sets price by watching its competitors. **[E2-44] fails both
  halves** through the 2022–24 downturn against Best Buy's filed record; **[E4-55]'s physical series is
  falling**; the only profits in the record came from **two waves [E4-36, E3-51]**; and **the basis must be
  re-won every product cycle [E4-04].** *Evidence is in and the business fails the test; this is a finding
  about the business, not about the price.*

---
> ⛔ **THE FILE CLOSES HERE — Q2 OUT, on the business.** Per the hard sequence, Q5 does not open.
> **Q3 and Q4 are RECORDED BELOW, NOT GOVERNING**, at the brief's instruction and per the queue's
> prohibition on skimming a gate: the triage label that filed this name as "negative on every construction
> ... the file's work is Q1-Q2 plus the honest statement" is the defect the correction of 2026-09-12 names.
> Nothing below can reopen Q2 **[E2-37, E3-39]**, and nothing below is a clearance.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 on the business. This section is done in full because
> the queue forbids skimming a gate, and because a controlled foreign private issuer whose controlling
> shareholder is in insolvency proceedings is exactly the case where Q3 carries the most evidence. **It cannot
> reopen Q2 [E2-37, E3-39].**

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution [E3-38]** — an inventory reseller on a ~9.5% product margin whose results are set by
  what it buys ahead of each component cycle and at what price; the 2022–24 margin compression and the
  2025–26 recovery were both inventory-timing outcomes the filing attributes to procurement. **Without a
  franchise the manager is magnified [E3-43]:** *"a business, unlike a franchise, can be killed by poor
  management"* — and Q2 found no franchise.
- [x] **Control [E1-16] — ticked in mirror image, as the ARM run did.** The corpus's case is the owner who
  holds the whole business and cannot exit. A minority buyer here holds a sliver of a company **54.6%
  controlled by one person, 94.5% controlled by three**, with a **6.1% free float worth $18.7M**; the board
  is appointed by the holders, not the minority (*"Digital Grid and Mr. Fred Chang ... have the right to
  appoint four directors and two directors, respectively"*, Item 3.D); and exit is by a float a single
  secondary on the live F-3 would outnumber 5.5 times. **The minority cannot react; it can only be carried.**
- [ ] **Leverage [E3-29]** — no bank-scale asset leverage ($2.2M drawn at 2026-06-30). The leverage here is
  vendor credit and is scored at Q4.

**Case declared: GATE, on daily execution and on control.** Were Q3 governing, no price would compensate a
failure here **[E1-16, E5-35]**.

**Honesty — binary, filings-based [E5-16], each matter dated to when it became PUBLIC:**
- **2020-08-06 / 2020-10-19 — a regulatory sanction of the controlling person for unlawful disclosure.**
  *"Hangzhou Lianluo and Mr. Zhitao He received an investigation notice from the China Securities Regulatory
  Commission ('CSRC') for alleged violation of laws and regulations regarding information disclosures of
  Hangzhou Lianluo ... (i) Hangzhou Lianluo received a warning and would be required to correct its unlawful
  acts and pay a fine of RMB 300,000, and (ii) Mr. Zhitao He received a warning and was required to pay a fine
  of RMB 400,000"* (20-F Item 6.C). **This is not an allegation; it is a regulator's finished penalty against
  the man who chairs this board and controls its majority.** The 20-F does not say what was mis-disclosed.
- **2019-12-17 (public in the merger documents and every 20-F since FY2021) — a $15.0M loan from Newegg to its
  controlling shareholder's subsidiary, unpaid at maturity.** *"On December 17, 2019, the Company loaned $15.0
  million to Digital Grid under a term loan agreement with a maturity date of April 30, 2020 and a fixed
  interest rate of 5.0% ... The maturity date was subsequently extended to June 30, 2024. While Digital Grid
  has continued to make interest-only payments on the loan, the $15 million principal balance currently
  remains outstanding and the maturity date has not been subsequently extended"* (Note 16). **The lender's
  own accounting says what it thinks of the loan: it was booked as a reduction of equity on the day it was
  made** — *"Note receivable (15,000)"* in the 2019 equity statement (FY2021 20-F) — and it sits there still,
  $15.2M, *"Notes receivable – related party"*. **The borrower is the entity whose Newegg shares are pledged to
  a bank holding a final, non-appealable judgment of default, and whose parent faces a bankruptcy liquidation
  petition (filed 2026-03-20).** [E5-22]: penalty size is not seriousness — $15M is 9% of Newegg's equity and
  18% of its cash.
- **2020-05 onward — the controlling shareholder's own bank defaults.** BOC suit (May 2020; final judgment of
  default), ICBC suit (2023-04-11; RMB332M judgment 2024-02-26), Hangzhou Lianluo delisted from Shenzhen
  (2024-08-16), a reorganization application still unapproved (approved by its holders 2024-06-12), a CMB
  liquidation petition (2026-03-20). **Total owed at 2026-03-31 per the 20-F: RMB331M + $146.9M (BOC) +
  RMB660M (ICBC) + RMB185.3M (CMB) — roughly $318M of bank debt** *(converted at the 20-F's own stated
  equivalents: $48M, $96M, $26.9M)*. **A business failure, not a conduct finding** — [E5-16] separates the
  two, and so does this record.
- **2026-01-08 / 2026-01-20 — the Chairman detained by a PRC supervisory commission.** *"Mr. He Zhitao is
  being placed under investigation and has been detained"* (Hangzhou Lianluo announcement No. 2026-002, EX-99.2
  to the 6-K). Released 2026-02-24; *"the nature and status of any ongoing investigation by PRC authorities is
  not known to the Company"* (Item 3.D). **A dating discrepancy is recorded as a prompt, not a finding:** the
  exhibit is signed *"Board of Directors, January 8, 2026"*, while the 20-F says *"On January 20, 2026, Hangzhou
  Lianluo publicly announced"*. Either the parent's board signed twelve days before publishing, or Newegg
  reported twelve days after its controlling shareholder did. The document that resolves it is the NEEQ
  publication record for announcement No. 2026-002.
- **2025-01 to 2025-09 — the founder's pledged shares foreclosed.** *"In January 2025, EWB notified Tekhill that
  it was in default ... on various dates in June 2025, EWB completed foreclosure sales of a total of 662,480
  Common Shares held by Tekhill"* (6-K 2025-08-19); loan repaid 2025-09-26. **Both of the company's two largest
  holders have had Newegg shares seized or pledged against defaulted debt in the last two years.**
- **Finding:** **no integrity disqualifier found in Newegg's own filings about Newegg's own management** (the
  CEO, CFO, CLO). **About the controlling person, the filings contain a finished regulatory sanction for
  unlawful disclosure and an unrepaid loan from this company to his company.** [E2-31]: *"We've never
  succeeded in making a good deal with a bad person."* [E5-17]: *"Never deal with a rascal under the expectation
  that you can prevent him from cheating you."* **Whether the 2020 sanction describes concealment or a
  technical breach decides between OUT and a live flag, and the 20-F does not say.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30] — each a prompt to read, never a verdict.**
- [x] **weak accounting — the cockroach count [E4-22 first].** Three, none of them large alone: **(1)** material
  weaknesses in internal control at FY2021 and FY2022 (*"lack of structure and responsibility, insufficient
  number of qualified resources"*, FY2021 20-F Item 15), remediated by FY2023; **(2)** the XBRL sign errors on net
  income in two vintages (Step 0); **(3)** the auditor's one critical audit matter is **$48.5M of vendor-incentive
  receivables** estimated from *"a significant number of vendor agreements with various terms and conditions"* —
  [E2-50]'s *"stroke of a pen"* class, equal to 30% of year-end equity. **And an Interim CFO since May 2024,
  twenty-eight months.** *"There is seldom just one cockroach in the kitchen."* None found is a restatement.
  *(Corrected within this run, before it closed: commit `f4e17c3` carried a fourth "cockroach" — the 20-F's
  "2.2 million buyers purchased over 312,000 items" read as an impossible sentence — was withdrawn on reading the
  four prior 20-Fs, which carry the same construction every year (675,000 items in 2021). "Items" is the count of
  distinct products bought, and it is a units series, used at Q2.)*
- [ ] **unintelligible footnotes** — no. The notes are plain and the related-party note says the unflattering
  thing in one sentence.
- [x] **trumpeted earnings projections [E4-22 third; E3-48; E5-30] — fires, and the record was pulled.**
  | guidance | issued | net sales | GMV | gross profit | net income (loss) | Adj. EBITDA |
  |---|---|---|---|---|---|---|
  | FY2024 | 2024-04-24 | $1.36–1.56bn | $1.74–1.90bn | $154.6–171.7M | $(42.8)–(51.7)M | $(9.6)–0.2M |
  | **FY2024 actual** | | **$1,235.6M — missed the low end by 9.1%** | **$1,533.7M — missed by 11.9%** | **$131.5M — missed by 14.9%** | $(43.3)M — inside | $(9.5)M — at the bottom |
  | FY2025 | 2025-04-28 | *"we are not prepared to deliver full year 2025 guidance at this time"* | | | | |
  | FY2025 | **2025-10-14, nine months in** | $1,375.3–1,423.9M | $1,691.3–1,751.1M | $153.3–158.7M | $(15.8)–(10.4)M | $13.7–19.1M |
  | **FY2025 actual** | | $1,444.5M — beat | $1,770.5M — beat | $168.5M — beat | $(4.9)M — beat | $24.8M — beat |
  | FY2026 | 2026-04-28 | $1.23–1.47bn | $1.50–1.79bn | $144.0–170.9M | **$6.1–15.7M** | $10.0–19.6M |
  | **H1 2026 actual** | | $626.7M (H1 2025 was 48% of FY2025) | $780.7M | $83.5M | $10.0M | $13.7M |
  **The one full-year guide issued at the start of a year missed revenue, GMV and gross profit by 9–15%; the one
  that beat was issued with nine months of the year already known — and was issued, as a 6-K incorporated by
  reference into the F-3 shelf, while the at-the-market program on that shelf was open.** Buffett's base rate is
  *"about nine cases out of ten"* [E3-48]; this record is too short to score, and its shape is the one he
  describes.
- [x] **serial share issuance [E5-15].** Shares **18,834K (2023-01-01) → 20,973K (2025-12-31), +11.4% in three
  years**, from option and RSU vesting and **1,084,290 ATM shares sold at an average $34.45** in July–October 2025.
  Then **a $250M primary shelf registered 2026-06-01 on a $308M company** (limited by I.B.5 to a third of the $57M
  non-affiliate float per year), **with 7,000,000 secondary shares for the three controlling holders** — Digital
  Grid 4,000,000 (*"Digital Grid intends to use all or a portion of the proceeds received from this offering to
  repay and discharge these loans"*), Tekhill 1,500,000, Galkin 1,500,000 (F-3). **And 249,061 new RSUs granted
  2026-07-29**, 178,275 of them to the CEO, vesting in one year.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — fires at full strength, and it is written into pay.**
  Adjusted EBITDA is a headline bullet in every release read, and it excludes stock compensation: **FY2025
  Adjusted EBITDA $24.8M against a net loss of $(4.9)M, the difference being $21.7M of SBC and $7.6M of D&A.**
  **The executive profit-sharing program pays *"50% based on GMV performance and 50% based upon adjusted EBITDA
  performance"*, and the CEO's PRSUs vest on *"financial performance tied to GMV"*** (Item 6.B; Note 12) — pay is
  tied to a revenue-plus-marketplace volume figure that price inflation raises and to an earnings figure that
  deletes the stock the executives are paid in. To its credit, the release carries the *"assets being
  depreciated and amortized may have to be replaced"* limitation — boilerplate that does not change the headline.
- [x] **filed-figure tells [E4-30]** — not the smooth-growth tell (the series is anything but smooth); the
  **cash-tax tell cannot be read** on pretax losses (cash taxes $0.4M, $0.2M, $0.3M, 2023–25). Ticked only for the
  period-shifting prompt below.
- [x] **metric-switching [E2-49]** — two instances, scored at Q1: visits and conversion dropped after they fell;
  the active-customer basis moved from twelve months to three in 2026 releases.
- [ ] **dividends funded by issuance [E2-52]** — no dividends.
- [x] **stock-price targeting [E3-50] — not in words; in conduct, and scored as a prompt.** The ATM was signed
  **2025-07-15**, in the middle of the stock's run from a $3.50 close (May 2025) to **$128.09 (2025-08-14)**;
  **1,000,000 shares sold on 2025-07-17 for $29.3M gross**; the Pricing Committee authorised 500,000 more on
  2025-08-17, three days after the peak (6-K 2025-08-19). The same fortnight, **the principal shareholders amended their right of first refusal so that the
  first 35.28% of each holder's May-2021 shares could be sold free of it** (Third Amendment, dated 2025-08-13, the day before the closing peak), and the
  founder had resigned from the board on 2025-07-08. (Galkin was the buyer on the other side of much of the
  float: Forms 4 show him buying from 2025-07-08 at $18.10 to 2025-08-15 at $104.72.) **Selling stock when it is dear is what a rational owner does
  — it is the right side of [E5-24] — so this is not scored against the company's capital allocation. It is scored
  as the corpus's [E4-52] confluence:** a company, its founder and its controller each arranging to sell into the
  same spike.
- [ ] **except-for [E2-57] / restructuring charge [E3-53]** — no recurring "one-time" charges; warehouse
  consolidation ran through SG&A, not a charge.

**The auditor's-eye test [E4-34], fourth question — period-shifting.** *Is there any action with "the purpose and
effect of moving revenues or expenses from one reporting period to another"?* The candidate is **inventory
timing itself**: the FY2025 margin expansion is attributed to *"leveraging a favorable cost basis for memory-related
components before Q4 supply constraints"*, and **$187.7M of inventory at 2026-06-30 (up from $98.5M at YE2024)**
carries a FIFO cost basis that will decide 2026–27 margins. That is a business decision, not an accounting one, and
nothing in the filing suggests otherwise; **the provision for obsolete and excess inventory rose to $2.4M in H1
2026 against $1.4M in H1 2025**, which is the line to watch.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, balance sheet first. Equity
(no goodwill, so equity is net tangible assets **[E2-43]**, less the $15.2M related-party note already deducted):
**$182.3M (2021) → $155.2M → $129.4M → $106.1M (2024) → $160.7M (2025, after $35.2M of ATM proceeds) → $171.2M
(2026-06-30).**

| FY | net income | average equity | **return on equity** |
|---|---|---|---|
| 2022 | (57.4) | 168.8 | **−34.0%** |
| 2023 | (59.0) | 142.3 | **−41.5%** |
| 2024 | (43.3) | 117.7 | **−36.8%** |
| 2025 | (4.9) | 133.4 | **−3.7%** |
| H1 2026, annualised *(CONVENTION: ×2, shown only to date the turn)* | 20.1 | 165.9 | +12.1% |

**Four consecutive negative years; equity fell $76M in three years before being refilled by the ATM.** [E2-01]'s
yardstick reads management's economic performance as failing for 2022–2025 and turning in 2026 on the memory wave.
Judged against *"the hand they were dealt"* [E3-59] — the same downturn Best Buy's computing business rode at a flat
margin — the operating record is poor.

**The half-owner test [E2-26].** **Mixed, and the good half is real.** The 20-F's risk factors are unusually blunt
about the parent's defaults, the pledge, the detention, CFIUS exposure and the controlled-company exemptions — a
minority holder is told the worst facts in plain English. **Against it**: the Q2 2026 release calls the balance sheet
*"strong"* in the same paragraph that discloses the credit agreements expiring that day were extended only
*"for a period of ninety days from August 27, 2026 through November 25, 2026"*; the Q1 2026 release says *"minimal
debt and substantial available credit capacity"* three months before that maturity. **Authorship [E2-72]** cannot be judged; there is no shareholder letter.

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [x] resists change in current direction — the enthusiast-components model has been restated as "AI strategy" and
  "agentic AI commerce" in each 2026 release, while revenue mix by category is unchanged (components & storage 66.6%
  of 2025 net sales).
- [ ] projects or acquisitions soak up funds — no acquisitions; capex cut to $2.7M. Not fired.
- [ ] staff studies justify a craving — no evidence.
- [x] peer behaviour imitated — the "AI shopping assistant", "conversational AI shopping experience" and
  "agentic AI commerce" announcements (FY2025 and Q2 2026 releases) follow the retail sector's language without a
  filed investment figure behind them. Scored lightly.

**Capital allocation — the buyback conditions [E5-08, E4-31] and the first law [E5-24].**
- **The 2024 buyback: 177.7K shares at an average ~$19.7 (February–May 2024), $3.5M** (FY2024 20-F Item 16E).
  (1) Ample funds? Cash $96–103M, but **owner earnings −$31.7M that year and −$67.8M the year before**, the revolver's
  cap cut to $40–50M in August 2024, and the controlling shareholder in default. **Not ample.** (2) A material
  discount to intrinsic value conservatively calculated? **No intrinsic value can be calculated from negative owner
  earnings**, so the condition cannot be shown to hold. (3) Shareholders supplied the information to estimate value
  [E4-31]? The 20-F is candid; the earnings were negative. **CAPITAL ALLOCATION FLAG on condition (1)**, stated with the
  humility clause **[E4-13]**: *"They also know a whole lot more about them than I do."* — and sized to what it was, $3.5M.
- **The 2025 ATM**: 1.08M shares at $34.45 against book value of about $7.66 a share. **Selling paper at 4.5x book is
  [E5-24]'s "smart at one price" side and is recorded as rational.** [E5-44] runs the same law for shares given:
  the intrinsic value of what was given was well below what was received.
- **The $15.0M loan to Digital Grid (2019)** is a capital-allocation decision as much as a conduct one: **$15M of
  minority holders' capital lent at 5% to a borrower already in trouble, now two years past due.** [E3-57]: *"either
  way, very costly to you."*
- **Pay against performance [E3-58, E2-29].** FY2025: CEO cash compensation **$4.1M, of which a $2.8M bonus**, in a year
  of a $(4.9)M net loss and −$51.3M owner earnings; **vesting value received $26.3M**; executives' exercises **$29.4M**.
  The CEO's contract guaranteed $1.1M of base salary for four years *"even if he is terminated during the term, unless
  he is terminated for cause"* (Item 6.B). **The $26.3M vesting value is 8.5% of today's market cap.**

**THE GUARDRAIL — checked before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is being used to promote the name.
- [x] Key-person dependence is recorded at Q2 (supplier allocation) — here the key person is the **controlling
  shareholder**, whose incapacity *"could trigger a change in effective control of the Company"* (Item 3.D).
- [x] Is a great manager the reason to act? No. **The manager is not the plan, and the controller's creditors may
  become it.**

- **VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [x] UNRESEARCHED → the CSRC Zhejiang Regulatory Bureau's
  administrative penalty decision of 2020-10 against Hangzhou Lianluo and Zhitao He (what was mis-disclosed, and
  whether it was concealment) — lives on the CSRC website and in Hangzhou Lianluo's NEEQ/Shenzhen announcements
  (Chinese; the ladder rung is "exchange filings", not blocked, not fetched). Second artifact: the NEEQ
  publication record of announcement No. 2026-002 (the 12-day gap). [ ] UNKNOWABLE**
  *Asked aloud: can I name the document that would resolve this? Yes — so UNRESEARCHED, not UNKNOWABLE. The
  detention itself is separately UNKNOWABLE (no public document exists while a supervisory commission's investigation
  is open). **If the 2020 decision describes concealment, the verdict is OUT under [E5-16] and [E2-31], permanently;
  if it describes a technical breach, the file still carries a GATE-weight Q3 with a live related-party loan, four
  negative years on [E2-01], a trumpeted-guidance miss, EBITDA-and-GMV pay, and a rationality read that is adverse.***
  *IN would have meant no disqualifier found. It is not written, because one named document could be one.*

## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING** — the file closed at Q2. Done in full per the brief and the queue's
> prohibition on skimming a gate. It cannot reopen Q2.

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its long-term
> competitive position and its unit volume. (… the working capital **increment also should be included in
> (c)**.)" … "**(c) must be a guess**."

The series is built in Stage 0 above from the filed statements, Newegg only, the Lianluo splice removed.

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
- **Short-window mean** (3-yr, 2023–2025): **−$50.3M** (capex end) · **−$48.6M** (D&A end)
- **Long-window mean** (5-yr, 2021–2025, the corpus default [E2-42]): **−$49.4M** · **−$48.2M**
- **Seven-year** (2019–2025, containing the pandemic year): **−$27.3M** · **−$26.9M**
- **Trailing twelve months to 2026-06-30**: **−$10.1M** · **−$12.7M**
- **Spread, conservative end:** 3-yr against 5-yr, 1.8%; 3-yr against 7-yr, 46%; 3-yr against TTM, 80%.
- **Combined range** (window spread × capex band): **−$50.3M to −$10.1M.**
- *Is that range too wide to reach a conclusion?* **No, because every construction in it has the same sign.**
  [E4-25]'s width rule governs where the range straddles a decision; here the widest reading still says the
  business has not earned anything for its owners on any window, and the width only measures how negative.
- *A wide spread is also a Q4 finding — a distorted year sits in the window [E5-11].* **Two are named.**
  **2020** (+$76.7M, the pandemic PC boom, with $76.3M of payables growth and $21.8M of deferred revenue) lifts the
  seven-year mean by about $17M (the six years without it average −$44.7M); **the first half of 2026** (the memory shortage, *"our early procurement of constrained
  categories continued to pay off"*) lifts the TTM. **[E4-41] says to normalize both down**, not to average them
  in as earning power.
- **Owner earnings by year:** Stage 0 table — 2019 −21.1 · 2020 +76.7 · 2021 −73.4 · 2022 −22.6 · 2023 −67.8 ·
  2024 −31.7 · 2025 −51.3 · TTM −10.1 (capex end, $M). **Cumulative 2021–2025: −$246.8M.**
- **Maintenance capex — a disclosed judgment with a corpus default.** **D&A is the default [E3-44, E2-41], and this
  is not the capital-intensive exception class [E5-20]:** a leased-warehouse reseller whose PP&E is $44.6M
  against $1.4bn of sales. **Both ends are shown; neither is invalid.** Capex has run **below** D&A for two years
  ($3.6M and $2.7M against $10.7M and $7.6M) as warehouses were consolidated and subleased, so the capex end is
  the flattering one in 2024–25 and the D&A end in 2023 (when capex carried the $23.2M headquarters purchase).
- **The working-capital increment [E2-23].** This is a **FIFO** retailer (*"accounted for using the first-in,
  first-out (FIFO) method"*, Note 3), so the LIFO carve-out does not apply: inventory must be rebuilt at current
  prices whenever unit volume or unit price rises. **OCF carries the increment; it is not removed.** The
  pre-working-capital sensitivity in Stage 0 (+$14.8M to +$17.4M TTM) is shown precisely so the reader can see
  what removing it would do, and it is not owner earnings.
- **Stock compensation subtracted in full [E5-06]:** $21.7M (2025), $27.3M, $33.7M, $33.9M, $6.3M (2021).
  **[E3-70]'s market measure** runs the other way in different years: the 2021-era RSUs carried a grant-date fair
  value of **~$348 a share** (post-combination) and were expensed at that through 2025 while the stock traded at
  $4–$40, so the charge **overstated** value delivered in 2022–24 — and in 2025 the spike delivered **$26.3M of
  vesting value to the CEO alone** and **$27.5M of option intrinsic value on exercise**, so the charge
  **understated** it. Over the window the reported charge is a fair floor. **The TTM's $10.4M is not a run-rate**:
  unrecognized RSU cost fell from $21.1M to $1.0M across 2025, and **249,061 new RSUs** were granted 2026-07-29.
- *If the capex band changes the verdict → UNKNOWABLE.* **It does not:** the band is $0.4M–$16.8M wide in any
  year and never crosses zero on a multi-year window.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · **[x] gruesome — and a variant the passage does not quite name: it shrinks and still eats
  capital.**
- **Evidence:** *"the gruesome account both pays an inadequate interest rate and requires you to keep adding money at
  those disappointing returns."* **Return on equity −34.0%, −41.5%, −36.8%, −3.7% (2022–25)**; equity fell from
  $182.3M to $106.1M in three years, then was refilled with **$35.2M of new shares**. **The one year of growth
  (2025, +16.9% net sales) consumed $70.9M of inventory and took operating cash to −$27.0M.** And the years of
  contraction did not release cash either: 2023 and 2024 owner earnings were −$67.8M and −$31.7M while sales fell.
  [E4-43]'s "good" class requires capital-hungry growth to earn *"a reasonable return"*; there is no return to test.

### Staying power — score all three **[E5-11]**, the worst case **[E2-55]**
- **(1) Large and reliable stream of earnings — NO.** Owner earnings negative on every multi-year window; the
  only positive years are waves (2020, H1 2026). GAAP operating income: +$23.4M, +$33.5M, −$49.5M, −$71.1M,
  −$51.6M, −$9.5M (2020–25), +$8.8M (H1 2026).
- **(2) Massive liquid assets — NO.** At 2026-06-30: **cash $82.2M** (plus $0.9M restricted) against **accounts
  payable $122.6M, accrued liabilities $38.5M, deferred revenue $30.4M, a drawn line of $2.2M and lease liabilities
  of $50.3M.** Current ratio 1.55, but **inventory is 58% of current assets** and cash covers **67% of payables**.
  Cash has fallen **$157.7M (2020) → $104.3M → $123.5M → $106.5M → $99.7M → $108.6M (2025, after the ATM) → $83.1M
  (H1 2026)** (cash + restricted, cash-flow statements).
- **(3) No significant near-term cash requirements — NO, and this is the one that usually kills.**
  1. **The credit agreements matured.** Both revolvers — the $40–50M seasonal facility and the $13.41M facility
     added October 2025 — carried a **2026-08-27** maturity (Note 8). The Q2 release: *"we intend to renew and expand
     our existing credit agreements, which have been extended for a period of ninety days from August 27, 2026 through
     November 25, 2026, to facilitate the renewal process."* **$17M of letters of credit** were outstanding against the
     revolver at year-end (Note 8). A non-renewal means cash-collateralising them.
  2. **The seasonal build is due now.** *"In anticipation of such higher sales, we typically begin building up our
     inventory levels in the late third quarter. Such inventory build-up may require us to expend cash faster than we
     generate by our operations during these periods"* (Item 5.B) — **in the same weeks the revolver sits on a 90-day
     extension.**
  3. **Vendor terms are the real credit line, and they are short.** *"typically requiring payment between 30 and 60
     days ... An adverse change in our vendors' payment terms and conditions would significantly increase our working
     capital requirements and have a material adverse effect"* (Item 3.D). **$122.6M is owed to suppliers.**
  4. **Leases:** $18.2M of operating-lease cash a year (Note 9), 5.1 years remaining.
  5. **The equity lifeline is nearly shut.** The new F-3 is a baby shelf: *"in no event will we sell ... securities
     with a value exceeding one-third of the aggregate market value of our outstanding Common Shares held by
     non-affiliates in any 12-month period, so long as [it] is less than $75.0 million"*. **At today's non-affiliate
     float of $18.7M (1,273,376 × $14.67), that is about $6.2M a year.** The 2025 ATM raised $35.2M only because the
     stock was at $29–$128.
- **Leverage, named and quantified [E4-16, E3-29].** Bank debt **$2.2M**. **Operating leverage is the whole of it:**
  total liabilities $251.3M against equity $171.2M; payables alone are 72% of equity. **[E2-54]'s coverage test**
  is trivially met on interest ($0.9M in H1 2026) and failed on its premise, because cash flow *"net of ample capital
  expenditures"* is negative on every window. **[E3-52]: read the terms, not the quantity** — this is the opposite of
  float: supplier credit due in 30–60 days that contracts exactly when margins do. **[E5-39]: the business depends on
  the kindness of strangers** — vendors, their credit insurers and a bank group on a ninety-day extension.
- **Jurisdiction [E3-66].** A BVI company taxed as a US corporation, **controlled through a Hong Kong subsidiary of a
  PRC company in insolvency proceedings**, whose Newegg shares are pledged to Bank of China. The minority stands in
  line behind: the PRC court (*"the Hangzhou Court may appoint an administrator ... Such administrator could assume the
  director nomination rights currently held by Digital Grid"*), BOC (*"could attempt to foreclose upon and sell Digital
  Grid's shares in Newegg at any time ... done quickly and without regard for maximizing the sale price"*), and CFIUS
  (*"such a transaction could be subject to CFIUS review, potentially resulting in divestiture orders"*). And BVI law
  limits the remedy: *"unavailability of certain types of class or derivative actions under British Virgin Islands
  ('BVI') law"* (Item 3.D).

### Name the specific way THIS business dies **[E2-27, E3-24]** — stated as its holders would accept it [E4-51]

**The mechanism — the SIXTH shape (the borrowed balance sheet), in a third form: THE PENDULUM.** *Inventory bought on suppliers' credit into a component price
wave; when the wave turns, the margin and the credit reverse together.* Newegg holds **$187.7M of inventory at
2026-06-30, up from $98.5M at YE2024**, much of it bought at shortage prices in memory, storage and GPUs. The filing
states the exposure: *"Higher product cost bases increase our inventory risk, as products purchased at elevated prices
may be difficult to sell at margins sufficient to cover our costs if demand softens or prices decline"* (Item 3.D).
When the memory cycle turns — the same cycle that turned in 2022 — three things happen at once, and the record shows
each of them happening before: **(a)** gross margin compresses (13.7% → 10.6% over 2021–24); **(b)** payables shrink
with purchases (−$57.4M in 2024, −$100.7M in 2019); **(c)** operating losses return (−$49.5M to −$71.1M a year in
2022–24). **This time the bank lines are on a ninety-day extension, the equity shelf is capped near $6M a year, and the
controlling shareholder is in liquidation proceedings rather than a source of capital.**

**Why the sixth shape, and why a named form rather than a seventh class.** The register was reconciled on
2026-09-13 at **six** shapes, with FLNC's treadmill folded in as a form of ACVA's borrowed balance sheet *"so the register
stays countable"*. Newegg belongs to the sixth on its defining fact — **payables of $160.3M carried 96% of $166.3M of
inventory at year-end**, liquidity lent by others that runs backwards when the business turns. **What makes it a distinct
form:** ACVA's lender was customers' money in transit, which scales with volume; FLNC's was customer deposits that must
be discharged by building. **Newegg's lender is its suppliers, and supplier credit is pro-cyclical to the same component
price that sets the margin** — the pendulum swings both lines against the owner on the same day. It is not ARM's (SBC is
large but not the whole deficit), BA's, SWK's, ORCL's or BE's. **A secondary
vector is recorded rather than named as a shape: the pledged parent** — control can change hands through a Chinese
court or a bank's foreclosure, at a discount the filing itself predicts, and a new controller's first act is not
knowable.

**Quantified from filed figures** *(arithmetic on the 2026-06-30 balance sheet, H1 2026 run-rates and the 2022–24
record, not a forecast)*:
- **Margin leg:** a return to 2023–24's 10.6–11.2% gross margin from H1 2026's 13.3% is **~2.4 points on the $1.23–1.47bn
  guided year = $30–35M of gross profit.** Against H1 2026's SG&A run-rate of **~$149M a year** (which already reflects
  the cost cuts — 2022–24's SG&A was $183–266M), that takes the operating result from +$8.8M a half to **roughly −$2M to
  −$20M a year**. *Honest correction to this file's own first draft: the 2022–24 losses of ~$50M a year were earned on a
  cost base $35–115M larger, and are not the right yardstick for the margin leg alone.* **Add a markdown on shortage-cost
  stock** — 10% of the $187.7M inventory is ~$19M, once.
- **Credit leg:** H1 2026 cost of sales ran **~$3.0M a day** ($543.2M ÷ 181). **Payables of $122.6M are ~41 days.** Terms
  cut to 30 days release **~$33M** to suppliers; to 15 days, **~$78M** — nearly the whole cash balance.
- **Bank leg:** $17M of letters of credit to collateralise if the revolver lapses; no drawn balance to repay.
- **Against $82.2M of cash:** a low-end margin year (−$20M), the one-off markdown (−$19M), a 30-day terms tightening
  (−$33M) and LC collateral (−$17M) total **−$89M**. **The margin and markdown legs alone leave the company with ~$43M and
  a smaller business; it is the credit leg — which is the lenders' choice, not the company's — that empties it.** Over
  two such years, with a baby shelf worth ~$6M a year and a controller that cannot subscribe, **the cash does not
  survive without new credit.**
- **Likelihood:** [ ] likely **[x] a real possibility** [ ] a low-level possibility. *The margin leg has happened in the
  record already (2022–24), and the credit leg partly did (payables −$57.4M in 2024). What is new is that the backstops
  that carried the company through it — $123.5M of cash at YE2022, a $100M revolver, a parent not yet in liquidation
  proceedings — are smaller or gone. What argues for "low-level" is the lower cost base; it is recorded, and it is why
  the likelihood is not "likely".*
- **[E4-40] — exposure, not experience.** The most recent experience is the best half-year since 2021. The exposure is
  $187.7M of shortage-cost inventory on $122.6M of 41-day credit.

**The case against this death, stated fairly [E4-51].** Newegg has survived exactly this before: 2022–24 cost $172M of
operating losses and it is still here, with payables that shrank $57M in one year without a crisis. Its bank debt is
nil; its headquarters building and Shanghai warehouses are owned and pledgeable; H1 2026 net income was $10.0M; the
memory shortage may last *"through 2026 and beyond"* (Item 3.D). **A holder would say the pendulum has swung once
without killing it.** The reply is the balance sheet it swung with: **$123.5M of cash then against $83.1M now**, and
equity refilled once already by selling stock into a spike that will not be there to sell into twice.

- **VERDICT (recorded, not governing): [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — gruesome **[E4-20]**,
  none of the three strengths **[E5-11]**, a named death that is **a real possibility [E3-24]** with the near-term cash
  requirement already dated (2026-11-25).

---
⛔ **Q5 does not open.** Q2 is OUT. Recorded Q3 UNRESEARCHED and recorded Q4 OUT would each close the file too.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Q2 closed the file. This block exists so that no reader has to guess what the quote implies; it carries no entry
language, ranks nothing, and uses no margin of safety (operator rule 3).*

**THE FLOOR [E4-28].** Not applied as a test — there is no positive owner-earnings base on any construction to test
against ~10%. Stated as arithmetic below.

**1. THE YIELD**
- owner earnings **−$50.3M to −$10.1M** ÷ market cap **$308M** (~21,006,000 × $14.67, 2026-09-11) = **−16.3% to
  −3.3%** · sovereign **5.35%** (US Treasury 30-year, 2026-09-11).
- Against the screen row: `yield_bottom −15.14%` was −$50M on the frozen $332M cap; re-struck at today's price the
  bottom is **−16.3%**. The trailing year narrows the negative to −3.3%; it does not change its sign.
- **The sensitivity that is not owner earnings** (Stage 0, working capital set aside, TTM SBC): **+$14.8M to +$17.4M
  = 4.8% to 5.6% — the bond's yield, on the single most favourable construction this file can build, in a shortage
  half-year [E4-41].**

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote: **REFUSED** — a growth rate on a negative base is not a number [E5-34];
  `run.py` refused it too.
- **In words instead — what the buyer at $14.67 is paying for.** **$308M buys $171.2M of book equity ($8.15 a
  share)**, which is: **$187.7M of inventory bought at or near shortage prices**, $82.2M of cash, $38.0M of receivables
  (largely vendor incentives), **$44.6M of PP&E** including the Diamond Bar headquarters ($23.2M in 2023) and owned
  Shanghai warehouses leased to third parties — **financed by $122.6M owed to suppliers in 30–60 days** — with the
  $15.2M loan to the controlling shareholder's subsidiary already deducted. **So the price is 1.8x book: about $137M
  paid for earning power that the filings show only in waves.** To earn the ~10% floor [E4-28] on $308M the business
  would need **~$30.8M a year of owner earnings — a swing of ~$81M from the 3-year mean.** It has produced that in
  **one year of seven (2020, $76.7M, the pandemic).** The best non-pandemic construction, the trailing
  pre-working-capital sensitivity, is **~$17M — 56% of the floor**.
- **And what the buyer is buying into, structurally:** a **6.1% float**; **7,000,000 secondary shares registered for the
  three controllers (5.5x the float)**; a controller whose bank can sell 53% of the company *"quickly and without regard
  for maximizing the sale price"*; and the **Chairman's Digital Grid selling 39,414 shares on 2026-09-03** and the
  founder selling through September 2026 (Forms 4). **[E2-63]: the upside is capped** *"unless more capital is
  continuously invested"* — here, in inventory, on suppliers' terms.

**3. WHAT YOU ARE PAID**
- return at the current price: **REFUSED on the same ground** — **−21.7 to −8.6 points** is the naive subtraction,
  printed only so that the negative is explicit.

**WHERE CERTAINTY IS PRICED [E3-42]:** not reached — sovereign used bare (5.35%), no premium, no margin.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:** **not stated.** A range of values on negative owner earnings would be
a projection of a turnaround, which is the artifact the corpus refuses [E3-34, E4-21]. **Context, not a valuation:**
book value is **~$8 a share**; the stock closed at **$3.50 (2025-05)**, **$128.09 (2025-08-14)** and **$14.67
(2026-09-11)** — a 37x round trip in sixteen months on a 6% float. **[E5-29]**: volatility is not risk — here the risk
is the negative sign and the pendulum, and neither moves with the quote.

**WHICH BAR?** Neither — **[ ] Normal method [ ] Screamer test**, both closed by the hard sequence. **Windage count: 0.**

- **VERDICT: not opened — Q2 OUT. Ranking position: none.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Nothing is bought, so nothing is sold, and no price alert is armed.** A name that failed at Q2 failed on the business;
an alert on it would be a category error (the QLYS ruling, 2026-09-07). **What follows are the refutation conditions,
written in advance [E1-02], for whoever reopens this name.**

**What would reverse Q2 OUT — each a filed fact, not a price:**
1. **The margin holds through a falling-price year.** A 20-F or release reporting gross margin **held at or above its
   2025–26 level in a year when component prices and average order value fell** — the half of [E2-44] that failed in
   2022–24. One quarter will not do; the test is a year of falling AOV with the margin rate standing still, as Best
   Buy's did.
2. **The physical series turns.** Active customers on the **12-month** basis, annual orders (the cumulative-count
   increments in Item 4.A) and distinct items bought **rising for two consecutive years while AOV is flat or down**
   [E4-55] — units, not price.
3. **A rival names Newegg.** A competitor's filing that treats Newegg as a constraint on its own pricing — the
   one-way naming reversing [E3-28].
4. **The price mechanism is rewritten.** An Item 4.B that no longer describes pricing by *"monitoring our major
   competitors' pricing trends"* — with evidence (a margin line) that it no longer needs to.

**What would reverse the recorded Q3 UNRESEARCHED:** the CSRC Zhejiang Bureau's 2020 penalty decision, read — OUT if it
describes concealment; if technical, a real Q3 read beginning from the $15.0M loan's repayment (or write-off) and the
guidance record [E3-48].

**What would reverse the recorded Q4 OUT:** multi-year credit agreements renewed on filed terms; owner earnings positive
on the **three-year** window including a post-shortage year; cash rebuilt without share sales.

**Monitoring dates — for a reader, not triggers:**
- **2026-11-25** — the extended credit-agreement maturity; renewal terms (size, tenor, covenants) or not.
- **The next results release** (2026 moved to quarterly releases — Q1 on 2026-05-28, Q2 on 2026-08-27; 2025 had only an H1
  release): inventory, payables days, and the obsolete-inventory provision through the seasonal build.
- **FY2026 20-F** (due by 2027-04-30): outturn against the $6.1–15.7M net-income guidance; the $15.0M related-party note;
  whether the key-metrics table keeps the 12-month basis.
- **Hangzhou Lianluo's court process** — approval of the reorganization or the CMB liquidation petition; any BOC sale of
  Digital Grid's shares; any 424B prospectus supplement under the F-3 secondary.

**The sell rule [E2-28]** — not applicable; nothing held. **The monitoring question [E3-30]:** is H1 2026's profit the
start of a recovery or the top of a shortage wave? **This file's answer is that the question is moot at Q2**: even the
best two years in the record (2020–21) were a wave, and the business gave it all back.

**Position size:** **zero** — the business failed Q2 **[E3-45]**.

- **VERDICT: not reached — the file closed at Q2. Refutation conditions recorded above; nothing armed.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT (governing); Q3 and Q4 recorded under an
      explicit NOT GOVERNING banner at the brief's instruction; Q5 headed COMPUTATION — NOT A CLEARANCE; Q6 refutation
      conditions only.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 IN is on filed revenue, cost and
      unit series.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives — Q3: the CSRC Zhejiang Bureau 2020 penalty
      decision (CSRC site / Hangzhou Lianluo exchange announcements) and NEEQ announcement No. 2026-002's publication
      record.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known — none governs; the Chairman's detention is
      recorded as unknowable in nature.
- [x] Step 0: the filing was read, with accession numbers; FY2025 OCF $(26,973)K cross-checked to XBRL and MD&A;
      equity recomputed from A − L at two dates.
- [x] Owner earnings on multi-year means; four windows stated; capex band disclosed as a judgment; SBC resolved and
      complete; the Lianluo splice removed and shown.
- [x] Competitor row filled — Amazon, Best Buy, Walmart, eBay, Costco from filings; Micro Center private, limit stated
      with its only EDGAR trace; the naming test run with correct CIKs and verified by reading.
- [x] Sovereign is for the earnings currency (USD, 92.7% US sales), from the issuing authority, dated 2026-09-11.
- [x] Value stated as a round-number range — **not stated, with the reason** (negative base; the FLNC precedent); book
      value given as context only.
- [x] One bar chosen, not both — neither, file closed; windage count 0.
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Run committed to git — pathspec commits `3ca3e5f`, `8bc7608`, `f4e17c3` and this one.
- [x] **One error of my own caught and corrected inside the run:** a fourth "cockroach" at Q3 (the 312,000-items sentence
      read as impossible) was committed in `f4e17c3` and withdrawn on reading four prior 20-Fs; it became a units
      series at Q2.

## REGISTER
- **Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)**
- **One line:** Newegg resells other companies' identical boxes at prices it sets by watching its rivals, lost a
  quarter of its margin rate and half its customers when the pandemic wave receded while Best Buy's computing margin held,
  and has earned nothing for owners on any multi-year window — **FAIL at Q2 (OUT on [E3-03] criterion 2)**; price
  **$14.67**, cap **$308M**, owner earnings **−$50M to −$10M**, yield **−16.3% to −3.3%** against **5.35%**.
- **Recorded, not governing:** Q3 UNRESEARCHED (the controller's 2020 CSRC penalty decision); Q4 OUT (gruesome; none of
  the three strengths; the sixth shape in the form THE PENDULUM, a real possibility, with the credit agreements on a 90-day extension to 2026-11-25).

### THE THREE EXPLODING RATIOS — what they actually were
| flag | the ratio | the dollars | the word |
|---|---|---|---|
| `wc_note` | payables at 6,992% of a year's OCF (2024) | **−$57.4M of payables against −$0.8M of OCF** | **noise** — offsetting inventory and receivable lines put OCF near zero |
| `best_year_dep` | 99.178, one year carries the window | **nine-year OCF mean +$0.11M; the best year is 2020's +$84.5M; two of the nine years are Lianluo Smart's** | **splice plus noise** |
| `da_note` | D&A steps 12.9x at 2019-12-31 | **$0.83M (Lianluo Smart, 2018) to $10.71M (Newegg, 2019)** | **splice** — two companies under one CIK; Newegg's own D&A never stepped |

### TOOLING DEFECTS FOUND
1. **THE REVERSE-MERGER SPLICE — a fourth cause the D&A flag's docstring does not name.** `da_discontinuity_flag()`
   lists *"an ACQUISITION, a CHANGE OF ESTIMATE, or a TAG whose SEMANTICS CHANGED"*. NEGG adds **a different company**:
   the CIK was Dehaier Medical Systems (2009–16) and Lianluo Smart (2016–21) before Newegg reverse-merged in, and
   companyfacts carries **both companies' values for 2019-12-31 and 2020-12-31** under identical elements. The splice
   feeds `years_filed 16`, `best_year_dep`, `level_shift` and the D&A flag. **Worse, it is vintage-dependent: under the
   earliest vintage the D&A flag fires 24.0x at 2021; under the newest, 12.9x at 2019** — the same defect moves year.
   `owner_earnings()` was unaffected only because its window starts at 2021. **A detector is cheap and was not built
   here (operator rule 8 keeps tooling changes out of a run):** EDGAR `submissions.json` carries `formerNames` with
   dates; a revenue step of more than ~50x at a former-name boundary is the signature. Recorded for the tooling owner.
2. **`best_year_dependence()` guards only `mean_all <= 0`.** A mean of +$0.11M on a series whose absolute values average
   $21M returns 99.2 and the confident string "ONE YEAR CARRIES THE WINDOW". It needs the same near-zero-denominator
   guard `working_capital_flag()` already has — the fifth instance of a guard testing one side of a series.
3. **`working_capital_flag()`'s note says *"a five-year average of $21.1M"*.** Newegg's five-year average operating cash
   is **−$12.9M**; $21.1M is the average of the **absolute** values. The note tells the reader to *"judge the $57.4M against
   the average"* and hands it a number that is not the average. Relabel it as mean absolute OCF.
4. **Filer XBRL sign errors on `NetIncomeLoss`** (FY2021 and FY2022 20-Fs: three periods). No owner-earnings effect;
   any screen reading net income, ROE or the cash-tax tell off tags would read Newegg's 2022 loss as a profit.
5. **`cover_shares.py`'s FPI limit, re-confirmed, with a better source than the one recorded.** The resume note's method is
   *"the 20-F Item 7.A count plus the 6-K balance sheet"*. **A foreign private issuer's F-3 cover carries a dated exact
   count and the non-affiliate count** (*"20,973,423 Common Shares outstanding, of which 1,273,376 Common Shares were held
   by non-affiliates"*) — the float and the count in one sentence, where a 6-K balance sheet rounds to thousands.
6. **`fts_count()` worked correctly** (NEGG's own 54 self-hits verified the CIK form), and its zeros for four rivals were
   confirmed by grepping their 10-Ks on disk.

### DEFECTS IN THE BRIEF (every brief contains one; this one's)
1. **"a controlled foreign private issuer with a de-SPAC history" — there was no SPAC.** The 2021 transaction was a
   **reverse merger into a Nasdaq-listed operating shell the same controller already owned**, *"accounted for as a transfer
   of assets under common control"* (FY2021 20-F), with Lianluo Smart's legacy business disposed of the same day. The
   distinction matters at Q3: the controller sat on both sides.
2. **"Is revenue units or price [E2-63]?"** — ledger row E2-63 is the capped-upside Q5 output. The units test is
   **[E4-55]** (which the brief also cites, correctly, one line earlier).
3. **"Read Note 1 and the cash-flow statement for the D&A step"** — Note 1 of the FY2025 20-F covers only the share
   combination and says nothing about the step. The explanation lives in EDGAR's `formerNames` and the FY2021 20-F's
   merger note. The instruction to read was right; the pointer was not.
4. **"A concurrent FLNC run shares this tree"** — FLNC was already folded and struck before this run opened
   (`7c51b61`, `a9eaa6c`). Stale, harmless, recorded. **And "six to seven named survival shapes"** — the register
   was reconciled to **six** on 2026-09-13 (FLNC's treadmill is a form of ACVA's sixth); NEGG is recorded as the sixth's
   third form, not a seventh.
5. **The priors framed to be refuted, and what happened to them:** Q2 OUT on criterion (2) — **confirmed, not refuted**;
   "Q3 is not a formality" — **confirmed**; "the flags say the denominator is noise" — **true for one of three**: the
   payables ratio is noise, the other two are a splice of two companies; "[E2-49], nine fires and seven failures" — **stale (the register read ten and seven after FLNC); fired
   (eleven and seven)**; the label "negative on every construction" — **right about owner earnings, wrong as a description of
   the trailing business**, whose pre-working-capital sensitivity is positive and whose H1 2026 GAAP net income was $10.0M.

### THE STRONGEST SINGLE FACT AGAINST THIS FILE'S CONCLUSION
**H1 2026: net income $10.0M, operating income $8.8M, gross margin 13.3%, and a trailing pre-working-capital owner-earnings
sensitivity of +$14.8M to +$17.4M — the first positive trailing figure since 2021.** If the memory shortage lasts, as the
20-F itself says it may, the business is currently earning roughly the bond on the quote. It does not reopen Q2 — the
margin is a shortage margin on identical goods, and 2022–24 is the filed record of what happens after one — but it is the
fact a holder would lead with, and it is stated here first.
