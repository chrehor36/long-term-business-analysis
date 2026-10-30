# Company Run — Super Micro Computer, Inc. (SMCI) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stop at the first verdict that is not IN.** Run unattended from scratch (no
prior run file for SMCI exists; the DELL run of 2026-09-07 used Super Micro's filings as one line of its
competitor row, and every SMCI figure below is recomputed from SMCI's own filings). WAVE 5, the first of
the seven "perimeter or restatement above threshold" names. Research, scripts and downloaded filings are
in `Test Runs/_research 2026-09-18 SMCI/`.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Asked aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0: THE SKIP REASON, THE RATE, THE PRICE, THE COUNT, THE PERIMETER, AND THE FILING

### The skip reason, tested on the filing rather than inherited
The wave 5 row is *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason
list says *"revenue step or cross-accession restatement above threshold."* **A prompt to read, never a
verdict.** The brief's probe (`_probe_screen.py`) and this run's reproduction of the 2026-09-01 triage
code (`triage_repro.py`, running `Screens/floor_screen.py` as it stood at commit `a8bc84f`, the commit
that wrote the wave 5 table, over the same companyfacts pull) say what each guard was reacting to:

| guard | value | what it was reacting to, on the filings |
|---|---|---|
| `share_count_shift` (the guard that fires FIRST in the `a8bc84f` code and returns the name unpriced) | **11.22x** | **A 10-for-1 forward split, not a perimeter change.** The Yahoo split feed carries *"10:1"* effective 2024-10-01; the dei cover counts read 58,556,527 (2024-04-30) then 593,481,352 (2025-01-31). The `a8bc84f` guard did not divide out splits; the split fix landed on 2026-09-02 (docstring: *"SPLITS ARE NOW DIVIDED OUT FIRST"*) and **the row was never re-triaged**, the AMZN kind of tooling artefact. The current guard with the ticker passed returns **1.12x**. The brief's probe called it without the ticker and reprinted the old 11.2x. |
| `scale_shift` | **2.10x** | **A real revenue step, and it is organic.** Net sales **$7,123.5M (FY2023) to $14,989.3M (FY2024)** (FY2024 10-K income statement), then $21,972.0M and **$39,063.1M (FY2026)**. `acquisition_flag` reads $2.5M; the only acquisition line on any cash-flow face read is *"Acquisition, net of cash acquired ( 296 )"* thousand in FY2024. The step is AI rack demand, not a merger. |
| `restatement_shift` | **(1.0, 2018-06-30)** | **A ratio of 1.0 is a NULL: no disagreement found.** The function reads the first revenue tag that has data (`RevenueFromContractWithCustomerExcludingAssessedTax`, FY2017 onward), where FY2018 carries $3,360.5M in both the FY2019 and FY2020 10-Ks. **It is structurally blind to the restatement that did happen**: FY2015-FY2016 were restated in the FY2017 10-K filed 2019-05-17 (below), and the original and restated values sit under different elements (`SalesRevenueNet` FY2015 **$1,991.2M** original; `Revenues` FY2015 **$1,954.4M** restated, -1.8%; FY2016 $2,215.6M to $2,225.0M). |

**So the label was, for SMCI: a split artefact (the guard that actually stopped the name), a genuine
organic revenue step, and a real restatement history that the restatement guard cannot see.** The
restatement is a Q3 matter and is read there.

**What the current screen says behind the label (tagged data, a prompt only):** `owner_earnings()` prices
SMCI and returns **negative owner earnings at every end** (5y D&A -$1,730M, 5y capex -$1,794M, 3y D&A
-$2,906M, 3y capex -$3,003M), driven by operating cash of **-$6,809.9M in FY2026**. `working_capital_flag`
returned `None` on this series, and the reason is the flag's scope, not the data: `WC_TAGS` reads only the
liability side (payables, accrued liabilities, deferred revenue; built for DELL's payables and INOD's prepayment),
and none of those crossed 30% of operating cash (deferred revenue +$1,880.7M is 27.6% of FY2026's). **The asset
side is where SMCI's cash went and the flag cannot see it**: the FY2026 inventory line moved **-$8,876.7M**
and receivables **-$3,921.9M**, against operating cash of **-$6,809.9M** (`IncreaseDecreaseInInventories`,
`IncreaseDecreaseInAccountsReceivable`; tooling note at the audit). SBC resolves for every year FY2010-26 (`ShareBasedCompensation`
= face *"Stock-based compensation expense | 412,115 | 314,452 | 231,507"*) and is complete on the face (one line,
no separate capitalised-SBC or 401(k) stock line found). The screen's D&A for FY2026 (**$53.0M**,
`DepreciationDepletionAndAmortization`) is **not the face figure** (*"Depreciation and amortization | 53,673"*),
which sits in no element companyfacts publishes (searched by value); the difference is $0.7M and immaterial.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **09/17/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority.** Struck
  by this run: the cached curve was deleted and `tools/sources.sovereign("USD")` re-fetched it on
  2026-09-18 at about 18:40 UTC, returning `(5.29, '09/17/2026', 'US Treasury daily par yield curve')`
  (`step0_out.txt`). Not inherited from the DLR run; it happens to be the same figure because 09/17 is still
  the newest row published. FRED was not used.
- **Earnings currency: USD.** 10-K Item 7A: *"substantially all of our sales and purchases are denominated
  in United States dollars."* Sales outside the US were *"29.1%, 40.6%, and 32.0% of net sales in fiscal
  years 2026, 2025, and 2024"*.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$40.35, the close of 2026-09-17**, the last completed close. Source: Yahoo Finance daily chart via
  `sources._chart("SMCI", rng="1mo")` (aggregator, permitted for live quotes only, **flagged**;
  `step0_out.txt`). Bar: open 38.04, high 41.01, low 37.82, close 40.35, volume 62.4M.
- **`tools/sources.price()` was NOT used for the struck price.** At about 18:41 UTC on 2026-09-18 it
  returned `(38.72, '2026-09-18', 'USD')`, the intraday `regularMarketPrice` stamped with today's date,
  while its docstring says *"Latest close."* **The TOST, EQIX and DLR defect reproduces on a fourth name.**
- Recent closes: 09-10 $37.38 · 09-11 $40.10 · 09-14 $36.74 · 09-15 $35.64 · 09-16 $36.85 · 09-17 $40.35.
  Range over the month shown: $35.17 (08-24) to $40.35.
- **Primary-filing cross-check of the aggregator: two Form 4s, both inside the day's range.** Accessions
  **`0001392942-26-000013`** (Charles Liang) and **`0001392941-26-000014`** (Sara Liu, the same jointly held
  shares), filed 2026-09-08: sales of 42,565 shares at **$36.60** and 57,435 at **$37.62** on 2026-09-03 (Yahoo
  bar low $35.75, high $38.22) and 100,000 at **$40.00** on 2026-09-04 (low $37.92, high $40.91). The
  founders' own sales are also a Q3 fact.
- **Split factor after the count's date (2026-07-31): 1.0** (`sources.split_factor_after`); the one split
  in the full history is the 10-for-1 of 2024-10-01. `close` used, never `adjclose`.

### The share count: from the cover, with the accession
- **656,965,384 shares**, from the cover of the **FY2026 Form 10-K** (period ended 2026-06-30, filed
  **2026-08-31**, accession **`0001375365-26-000022`**): *"As of July 31, 2026, there were 656,965,384 shares
  of the registrant's common stock, $0.001 par value, outstanding, which is the only class of common stock of
  the registrant issued."* `Screens/cover_shares.py SMCI` returns the same figure from the same accession,
  *"(single class / undimensioned)"*. This is the latest periodic filing (the Q1 FY2027 10-Q is not due
  until November).
- **ERIC trap checked**: the balance sheet reads *"Issued and outstanding shares: 656,882 and 594,137 at June
  30, 2026 and 2025"* (thousands); no treasury line. **SPGI trap checked**: no exclusion clause on the cover;
  the preferred is a separate listed class (SMCIP) and is not common.
- **The count grew 10.6% in the year**, almost all in June 2026: 594,136,852 (2025-06-30) to 656,882,499
  (2026-06-30); **52,272,726 shares sold in a public offering** (45,454,545 plus the 6,818,181 option; 8-K
  `0001193125-26-269703`, 2026-06-12; *"Issuances of common stock in public offerings, net of issuance costs |
  52,272,726 | 1,405,950"*, statement of equity), the rest option exercises and RSU releases net of
  withholding. A **$1.25bn at-the-market programme** was opened the same week (same 8-K).

### The perimeter between the business and the common holder: stated, not blended
1. **7.00% Series A Mandatory Convertible Preferred Stock, issued June 2026**: 4,312,500 shares, $1,000
   liquidation preference each, **$4,231.6M net cash** (cash-flow statement), dividends 7.00% (**about $302M a
   year**, payable in cash or stock), and **mandatory conversion in June 2029 *"into between 30.3040 and 36.3640
   shares of Common Stock"*** per preferred share (8-K `0001193125-26-270430`, 2026-06-15). That is **130.7M to
   156.8M common shares, +19.9% to +23.9%** on the cover count; at any price above about $33.00 the lower
   figure applies, and $40.35 is above it. **Treatment: this claim is equity that WILL become common, so the
   perimeter-consistent cap adds the 130.7M shares at the struck price, and the preferred dividend is NOT
   also deducted from owner earnings on that basis** (it is one or the other, never both). Both caps are shown
   at Q5.
2. **Convertible notes**: $1,725.0M due 2029 (0.00%), $700.0M due 2028 (2.25%, conversion price *"approximately
   $ 61.06"*), $2,300.0M due 2030 (conversion price *"approximately $ 55.20"*) (10-K Note on convertible notes).
   All out of the money at $40.35; treated as debt, with capped calls purchased in FY2024 and FY2025.
3. **Bank debt**: *"$2.0 billion of outstanding borrowings under our Revolving Credit Facility with JP Morgan,
   $1,763.5 million outstanding borrowings under our CTBC Revolving Credit Facilities"*; total indebtedness
   *"approximately $8.7 billion"* at 2026-06-30. Cash $7,521.5M.
4. **No goodwill, no intangibles, no equity-method stake of size** (equity investees' share of loss $2.5M);
   non-controlling interest $0.2M.

### The market cap
- **$40.35 × 656,965,384 = US$26,508.6M.** Split factor after 2026-07-31 = 1.0.
- **Perimeter-consistent, with the mandatory preferred at its minimum conversion (130,686,000 shares):
  $40.35 × 787,651,384 = US$31,781.7M.** Displayed side by side, not blended.

### LIVE-DEAL CHECK: run by this run, not inherited
- `sources.deal_filings("0001375365")` returned `([], [], '2026-08-31')` and `deal_note` returned an empty
  string: no DEFM14A, PREM14A, S-4, SC 14D9, SC TO-T or 425 since the 10-K, and no 8-K Item 1.01 since it.
- **Every 8-K since 2024-01-01 was downloaded and the Item 1.01 ones were read** (`fetch8k.py`, `8k/`):
  credit agreements (JPMorgan revolver 2025-12-29 and amendments 2026-01-26, 2026-06-10; CTBC Taiwan facility
  2026-01-21), the MUFG receivables purchase agreement (2025-07-16), convertible-note indentures (2024-02,
  2025-02, 2025-06), the June 2026 common offering, ATM and mandatory-preferred filings. **None is an offer for
  Super Micro's shares and no EX-2.1 plan of merger was found. The quote is an owner-earnings price, not a
  spread.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K**, period ended 2026-06-30, filed **2026-08-31**, accession **`0001375365-26-000022`**
  (`10K_FY2026.txt`; auditor BDO USA, P.C., report dated August 31, 2026). It carries Part III (directors,
  compensation, related parties) in the 10-K itself.
- Also read: 10-Ks FY2025 (`0001375365-25-000027`), **FY2024 (`0001375365-25-000004`, filed 2025-02-25, six
  months late)**, FY2023 (`0001375365-23-000036`), FY2022 (`0001375365-22-000103`), FY2021
  (`0001375365-21-000060`), FY2020 (`0001375365-20-000064`), **FY2019 (`0001375365-19-000079`, filed
  2019-12-19)** and **the FY2017 10-K filed 2019-05-17 (`0001375365-19-000039`) carrying the FY2015-16
  restatement**; the Q3 FY2026 10-Q (`0001375365-26-000014`); the DEF 14A of 2026-03-03
  (`0001375365-26-000008`); 8-Ks and EX-99.1 releases 2024-2026 and the selected earlier ones named at Q3.
- **Figures cross-checked against the filed statement** (FY2026 consolidated statement of cash flows):
  *"Net cash (used in) provided by operating activities | ( 6,809,886 ) | 1,659,524 | ( 2,485,972 )"*,
  *"Stock-based compensation expense | 412,115"* and *"Purchases of property, plant, and equipment ... | (
  161,999 )"* all match companyfacts exactly (`NetCashProvidedByUsedInOperatingActivities`,
  `ShareBasedCompensation`, `PaymentsToAcquirePropertyPlantAndEquipment`, accession `0001375365-26-000022`).
  The face D&A line is the one that does not (above).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
Super Micro buys the expensive parts of a server from other companies (graphics processors, central
processors, memory, storage, network cards), designs and builds the cheaper parts itself or through two
related Taiwanese suppliers (boards, chassis, power supplies, and now liquid-cooling plumbing), assembles and
tests complete servers and increasingly whole racks and rows of racks in San Jose, Taiwan, the Netherlands
and Malaysia, and sells them to cloud operators, AI data-centre builders, enterprises and resellers. **It
keeps the difference between what the parts cost and what the customer pays, and that difference is thin.**

FY2026, from the 10-K income statement (accession `0001375365-26-000022`), $M:

| line | FY2026 | per $100 of sales | FY2025 | FY2024 |
|---|---:|---:|---:|---:|
| Net sales | 39,063.1 | 100.0 | 21,972.0 | 14,989.3 |
| Cost of sales (parts, contract manufacturing, freight, tariffs, factory labour, write-downs) | 34,835.8 | 89.2 | 19,542.1 | 12,927.8 |
| **Gross profit** | **4,227.3** | **10.8** | 2,429.9 | 2,061.4 |
| Research and development | 771.2 | 2.0 | 636.6 | 463.5 |
| Sales, marketing, general and administrative | 685.5 | 1.8 | 540.4 | 387.1 |
| **Income from operations** | **2,770.5** | **7.1** | 1,253.0 | 1,210.8 |

Read as an assembler:
1. **Almost all the money passes through.** $89.20 of every $100 goes to the parts and the making. *"One
   supplier accounted for 63.1 %, 64.4 %, and 65.4 % of total purchases for the fiscal years ended June 30,
   2026, 2025, and 2024"* (Note 1, supplier concentration; the supplier is not named in the note; the MD&A
   names NVIDIA first among the vendors whose *"product introduction cycles"* the company *"closely monitor[s]"*,
   and every FY2026 product line named is an NVIDIA platform: *"GB200 NVL72, GB300 ... HGX B300 and B200"*).
2. **The price of a server follows the price of its parts.** The MD&A: *"The prices for our server and
   storage systems can vary widely depending on the configuration, including factors such as speed,
   functionality and performance of key components, including CPUs, GPUs, SSDs, cooling systems, and
   memory."* The FY2025 average selling price rose 34%; FY2026 sales rose 77.8% *"primarily driven by
   fulfillment and shipment of orders to support our customers' data center deployment, including large
   design wins from a few customers."*
3. **A few customers.** *"sales to one customer represented 28.1 % of total net sales"* in FY2026 (about
   $11.0bn); four customers at 20.9%, 11.5%, 11.3% and 11.1% in FY2025.
4. **The business needs a great deal of working capital, and needs it before it is paid.** At 2026-06-30:
   inventories **$12,895.9M** (about 135 days of cost of sales), receivables **$6,125.4M** (about 57 days of
   sales), against payables of **$2,247.0M** and customer deposits and deferred revenue of **$2,612.0M**. The
   10-K: *"We maintain substantial inventories of our products because the computer server industry is
   characterized by short lead-time orders and quick delivery schedules"*, and *"We may place non-cancellable
   inventory orders for certain product components in advance of our historical lead times, pay premiums and
   provide deposits to secure future supply and capacity."* Plant is small: net property and equipment
   **$625.6M**, capex **$162.0M** in FY2026 (0.4% of sales).
5. **So growth is financed from outside.** FY2026 operating cash was **-$6,809.9M** (inventories -$8,876.7M,
   receivables -$3,921.9M); it was filled by **$4,231.6M** of mandatory convertible preferred, **$1,407.0M** of
   new common and **$3,948.3M** of net new bank borrowing (cash-flow statement). The MD&A says so: *"We have
   financed our growth primarily with funds generated from operations, as well as utilizing borrowing
   facilities, selling our common stock, issuing our Mandatory Convertible Preferred Stock, and issuing
   convertible notes."*

### The scarce input this business controls
**Named honestly, it is thin.** What the company claims is time-to-market: *"We seek to be the first to
market with superior product designs"*, built on in-house board, chassis, power and cooling design and US
rack-scale assembly (*"We believe we are the only major server, storage, and accelerated compute platform
vendor that designs, develops, and manufactures a significant portion of its systems in the United States"*).
What it does not control is the input that sets the product: **the accelerator, bought from one supplier
that is 63-65% of all purchases and sells the same platform to every rival.** The 10-K's own competitor list
is *"Cisco, Dell, Hewlett-Packard Enterprise, and Lenovo"* and *"ODMs, such as Foxconn, Quanta Computer, and
Wiwynn Corporation"*. Whether design speed and cooling are a position or only a lead is a relative claim,
and it is Q2's.

### Will the fundamentals look broadly the same in ten years?
**The mechanism, yes**: buy the leading processors, build them into servers and racks faster than rivals,
sell at a thin spread, carry large inventories. The 17-year record shows the spread itself has been stable in
kind: gross margin **12.8% to 18.0%** every year FY2010-FY2026 (companyfacts, checked to the FY2024-26 faces),
operating margin **2.3% to 10.7%**. **The products, certainly not the same**: the filing lists a new NVIDIA
generation every year (Hopper, Blackwell, Blackwell Ultra, *"the upcoming NVIDIA Vera Rubin platform"*), and
AMD, Intel and Arm platforms beside them. **The customers, not necessarily**: one customer was 28.1% of FY2026
sales. The volume is what cannot be foreseen; the way a dollar of sales becomes a few cents of profit can.

**The honest limit, stated rather than smoothed.** [E3-31] asks for businesses *"relatively simple and stable
in character"* and warns that *"If a business is complex or subject to constant change, we're not smart
enough to predict future cash flows."* The **unit economics** are simple and have been stable for seventeen
years; **the product and the customer list change every year**, and that is where a forecast of cash would
fail. v4 assigns that second question to Q2 ([E4-04], the moat that must be rebuilt) and Q4 (the range), and
this run carries it there rather than closing Q1 on it: how the money is made is writable in five minutes
**[E4-46]**, which is what Q1 asks.

- **VERDICT: [x] IN**
  *The unit economics are writable in plain words (a thin spread over bought-in processors, earned by
  assembling and shipping faster than rivals, with large inventories financed from outside); the mechanism is
  recognisable across seventeen years of filed margins [E3-31]. The scarce input is thin and not owned; whether
  it is a franchise is a relative claim, and it is Q2's.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHAT IS BEING TESTED, AND THE PRIOR THIS RUN WAS TOLD TO DISTRUST
Q1 named one claimed advantage: **design speed and rack-scale integration (liquid cooling included), sold
as time-to-market**, built on processors bought from one supplier that is 63-65% of purchases. [E3-03]'s
test is that the customer thinks there is *"no close substitute"*, and its demonstration clause is *"a
company's ability to regularly price its product or service aggressively and thereby to earn high rates of
return on capital."* **The prior on disk** is the DELL run (2026-09-07), which used SMCI's gross margin as
corroboration that AI-server dollars arrive with little margin. That was a figure computed for Dell's
question. **Every SMCI number below is rebuilt from SMCI's own filings** (`series.py`, `roic.py`), and the
strongest facts FOR a franchise are recorded first and at full strength **[E4-26, E4-51]**.

### THE CASE FOR, AT FULL STRENGTH
1. **The return on capital is not low.** Pre-tax operating income over average invested capital (equity plus
   all debt including convertibles, less cash; filed balance sheets, `roic_out.txt`): **42.6% (FY2023),
   31.3% (FY2024), 21.2% (FY2025), 25.7% (FY2026)**. Capital turns about **3.5-4.5 times a year** on sales in
   every year FY2015-26, so a thin margin still earns a real return on the capital in the business.
2. **The last quarter was very different from the year.** Q4 FY2026 gross margin **17.5%** (*"Gross margin
   of 17.5% versus 9.9% in Q3'26 and 9.5% in Q4'25"*, EX-99.1 of 2026-08-11, `0001375365-26-000021`); the
   preliminary update of 2026-07-21 says *"significantly higher than our guidance of 8.2% to 8.4%, primarily
   due to a favorable customer and product mix"*, with *"total new orders in excess of $60 billion"* in the
   quarter and FY2027 sales guided at *"$65.0 billion to $72.0 billion"*.
3. **Share is being won from larger rivals.** SMCI's sales rose from $7.1bn to $39.1bn (FY2023-26); Dell's
   ISG from $38.4bn to $60.8bn over roughly the same span (DELL fiscal FY2023-26, Dell 10-K
   `0001571996-26-000008`, checked by this run against the filed text: *"Total ISG net revenue | $ | 60,826"*).
4. **Something real is being sold beyond the chip**: in-house boards, chassis and power, US assembly, and a
   liquid-cooling stack the company designs (*"coolant distribution units, liquid-to-air heat exchangers,
   chilled doors, power shelves ..."*). Services and software revenue $538.3M (FY2026).

### WHAT DEFEATS IT: THE THREE CONDITIONS **[E3-03]**
**(1) Needed or desired: IN.** Record sales, *"generated more than $60 billion in new orders"* (release),
over 1,000 customers.

**(3) Not subject to price regulation: IN**, with one note: export controls ration who may be sold the
product (*"a worldwide authorization requirement for certain of our advanced computing products"*, 10-K
Item 1), which limits volume by market, not price. [E2-59] is not engaged either way.

**(2) No close substitute: FAILS, in the company's own words, in three places.**
1. **Price is cut to win share, and the company says so two years running.** FY2026: *"Gross margin decreased
   to 10.8% in the fiscal year 2026, from 11.1% in the fiscal year 2025, primarily due to our strategy to offer
   competitive pricing to gain market share, change in product and customer mix, and higher manufacturing
   related expenses."* FY2025: *"primarily due to our strategy to offer competitive pricing to gain market
   share, increased competition and a change in product and customer mix."* A buyer who can be won by a lower
   price had an alternative at the higher one.
2. **The long-run price direction is written down.** Item 1A: *"Historically, these pricing pressures have
   led to a continued decline of average selling prices across our business and we expect that these historical
   trends will continue"*, and *"Both legacy competitors as well as new entrants, predominantly Asia-based
   competitors, have intensified market competition in recent years leading to pricing pressure."* Item 1:
   *"we have experienced increased competition from original design manufacturers ('ODMs') that benefit from
   their scale and very low-cost manufacturing and are increasingly offering their own branded products."*
3. **The product the customer is buying is the supplier's platform, which every rival sells.** Every FY2026
   system line named in Item 1 is an NVIDIA platform (*"NVIDIA GB300 NVL72, GB200 NVL72, and HGX B300 and B200
   systems"*); one supplier is **63.1%** of all purchases; and the 10-K itself names four global vendors plus
   three ODMs as rivals. The Dell run records Dell selling the same NVIDIA platforms through ISG (its *"AI-optimized
   servers"* line, $24,683M in FY2026).

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
**Taken: Dell ISG, HPE Server, Celestica CCS (the one ODM-type server builder that files a US 10-K), and
NVIDIA as the supplier whose margin is the question.** Not taken, and why: **Lenovo** (HKEX, not an SEC
registrant; the Dell run carries its consolidated IFRS figures only), **Foxconn, Quanta and Wiwynn** (Taiwan
exchange filers, not on EDGAR; not fetched), **Cisco** (servers not segmented). **Two of the seven rivals the 10-K names (Dell, HPE) are in the row, with Celestica added as the one ODM-type
filer on EDGAR; the five missing are Cisco (unsegmented), Lenovo (IFRS, HKEX) and the three Taiwanese ODMs, which
the 10-K itself names as the low-cost pressure. That is the row's gap, stated.** Same metric, each filer's last three filed years; segment measures exclude stock compensation and
amortisation, so SMCI is shown both ways.

**ROW A: GROSS MARGIN**

| company | what | year 1 | year 2 | year 3 | years | source |
|---|---|---:|---:|---:|---|---|
| **Super Micro** | whole company, one segment | **13.75%** | **11.06%** | **10.82%** | FY2024-26 (Jun) | 10-K `0001375365-26-000022` face |
| Dell ISG | servers, storage, networking | 38.19% | 32.67% | 25.98% | FY2024-26 (Jan) | Dell 10-K `0001571996-26-000008`, segment cost of net revenue (Dell run table) |
| HPE Server | servers | 29.41% | 25.11% | 20.89% | FY2023-25 (Oct) | HPE 10-K `0001645590-25-000130` MD&A segment table (*"Gross profit \| 3,707 \| 4,044 \| 4,195"* on net revenue 17,745 / 16,104 / 14,266), this run |
| Celestica | whole company (CCS 74% of revenue in 2025) | 9.5% | 10.7% | 12.1% | CY2023-25 | Celestica 10-K `0001030894-26-000011` MD&A (*"Gross margin \| 12.1 % \| 10.7 % \| 9.5 %"*), this run |
| NVIDIA | the supplier | 72.72% | 74.99% | 71.07% | FY2024-26 (Jan) | NVIDIA 10-K `0001045810-26-000021` (Dell run table) |

**ROW B: OPERATING MARGIN (segment basis where the filer reports one)**

| company | year 1 | year 2 | year 3 | years |
|---|---:|---:|---:|---|
| **Super Micro, GAAP** | **8.08%** | **5.70%** | **7.09%** | FY2024-26 |
| **Super Micro, before stock compensation** (segment-comparable) | **9.62%** | **7.13%** | **8.15%** | FY2024-26 |
| Dell ISG (segment operating income) | 12.65% | 12.80% | 11.69% | FY2024-26 |
| HPE Server (segment earnings from operations) | 12.7% | 11.2% | 7.6% | FY2023-25 |
| Celestica CCS (segment margin) | 6.2% | 7.4% | 8.2% | CY2023-25 |
| NVIDIA Compute & Networking (segment) | 67.54% | 71.33% | 67.26% | FY2024-26 |

**ROW C: RETURN ON CAPITAL, [E2-43]'s unleveraged net tangible assets**, the Dell run's formula (operating
income x 0.79 over total assets less goodwill, intangibles and non-interest-bearing current liabilities),
latest year, from that run's table: **Super Micro 8.82% (FY2026)**, Dell 29.36%, HPE -1.34% (impairment year),
NVIDIA 67.99%. **The SMCI figure carries $7.5bn of cash (much of it from the June 2026 raises) in its denominator; without cash
it is 12.6%** (this run: $2,188.7M over $17,303.7M). Dell's carries $14.3bn of financing receivables. Segment
assets are not filed for Dell ISG or HPE Server, so no same-denominator segment return exists.

**What the row shows.**
- **Position: Super Micro now earns an ODM's gross margin.** Its FY2026 gross margin (10.82%) sits below
  Celestica's (12.1%), the contract manufacturer in the row, and at **less than half** Dell ISG's and HPE
  Server's; its operating margin before stock compensation (8.15%) sits between Celestica CCS (8.2%) and HPE
  Server (7.6%), below Dell ISG (11.69%). **It has no margin advantage over anyone in the row except the
  direction of travel of HPE.**
- **Direction: every server builder's gross margin is falling as AI mix rises, and the supplier's is not.**
  Dell ISG -12.2 points in two years, HPE Server -8.5 points, Super Micro -7.2 points from FY2023's 18.01%; NVIDIA
  71-75%. Super Micro's incremental gross profit per incremental dollar of sales FY2023-26 was **9.2 cents**
  ($4,227.3M less $1,283.0M over $39,063.1M less $7,123.5M). That is **[E3-62]**: *"All of the advantages from
  great improvements are going to flow through to the customers"*, and here the rest stops at the supplier.
- **The row's limit [E3-61]**: it shows position, not conduct. It cannot show how the three Taiwanese ODMs,
  which the 10-K names as the low-cost entrants, will price the next platform, and it cannot see their margins.
  **The gate does not close on that gap**: an ODM earning more than Super Micro would not give Super Micro a
  pricing position it says in its own 10-K that it does not have; one earning less would confirm the finding.

### THE OTHER Q2 TESTS
- **[E2-44] two-characteristic test.** (1) *"an ability to increase prices rather easily (even when product
  demand is flat and capacity is not fully utilized) without fear of significant loss of either market share
  or unit volume"*: **FAILS** in the company's words above (price cut to gain share; ASPs expected to keep
  declining). (2) *"an ability to accommodate large dollar volume increases in business ... with only minor
  additional investment of capital"*: **FAILS outright on working capital.** To add $17.1bn of sales in FY2026
  the business added **$8,215.6M of inventory and $3,921.5M of receivables** (balance sheets; cash-flow lines
  -$8,876.7M and -$3,921.9M), and operating cash was **-$6,809.9M**; FY2024, adding $7.9bn of sales, operating
  cash was **-$2,486.0M**. Growth here is bought with capital raised outside (Q1 item 5).
- **[E3-46] returns on capital, asked about the business.** The full-strength fact above stands: 21-43% pre-tax
  on book invested capital in FY2022-26. **Two things qualify it, both filed.** (a) The same formula gives
  **10.7-17.5% in FY2016-21** (`roic_out.txt`), before the AI volume arrived: the return is the product of turnover
  and an operating margin of 2.6-4.8% in those years, and it moves with volume, not with any price the company sets. (b) On [E2-43]'s
  tangible-asset basis at the latest year, Dell ISG's parent earns 29% and Super Micro 9-13%.
- **[E4-04] rapid change: ENGAGED, and v4's scope test answers "replacement".** *"Our criterion of 'enduring'
  causes us to rule out companies in industries prone to rapid and continuous change."* The advantage claimed
  is being first with each new supplier platform, and a new platform arrives every year (Hopper, Blackwell,
  Blackwell Ultra, Vera Rubin, each named in the last two 10-Ks). **The spending does not defend the same
  advantage; it buys the next one**, and the old one is written down: inventory write-downs **$83.0M, $232.1M,
  $188.1M** (FY2024-26, cash-flow face). Item 1A: *"The risk of obsolescence and/or excess inventory is
  heightened for semiconductor solutions due to the rapidly changing market for these types of products."*
- **[E4-36] which cause of extreme success: wave-riding.** Sales 5.5x in three years on AI demand; before it, sales grew 9.8% a year FY2016-21 ($2,225.0M to
  $3,557.4M) and 1.9% a year FY2018-21 ($3,360.5M to $3,557.4M).
  The advantage lives in the wave **[E3-51]**; a surfing run is not a moat.
- **[E2-45] the attacker's test: the attacker exists, is larger and is named.** Dell grew ISG revenue 39.5% in
  its FY2026; the 10-K names ODMs *"increasingly offering their own branded products"* and says *"most of our
  competitors have longer operating histories, significantly greater resources, greater name recognition, or
  deeper market penetration."*
- **[E2-58] the commodity end.** The product is differentiated at the edges (cooling, rack integration) and
  undifferentiated at its core (the accelerator every rival buys). No cost advantage *"both wide and
  sustainable"* appears in Row A or B. Supply is ample in the sense that matters: the supplier sells to all
  comers.
- **[E4-32] direction: narrowing.** Gross margin **18.01% (FY2023), 13.75%, 11.06%, 10.82% (FY2026)**; the
  quarterly path FY2025-26 was **13.1%, 11.8%, 9.6%, 9.5%, 9.3%, 6.3%, 9.9%, 17.5%** (EX-99.1 releases). The last
  quarter is the outlier the company itself had guided at 8.2-8.4%, and it is recorded, not averaged away.
- **[E4-55] units:** no unit series is filed (servers or racks shipped are not disclosed); the FY2025 MD&A
  gives only *"an increase of average selling price of 34%"*. Dollar revenue is the only series, which is the
  weaker one [E4-55] warns about.
- **[E3-33] untapped pricing power: REFUSED** under **[E5-28]** (*"a monopoly or a near monopoly"*): the
  company is cutting price to win share, the opposite conduct.
- **[E2-53] dominance: not available.** Super Micro's FY2026 sales ($39.1bn) are below Dell ISG's ($60.8bn)
  and it names four global vendors and three ODMs as rivals.
- **[E4-23] key-person dependence: RECORDED HERE AS A MOAT DEFECT.** Item 1A: *"Charles Liang ... is critical
  to the overall management of our company as well as to our strategic direction ... His experience in leading
  our business and his personal involvement in key relationships with suppliers, customers and strategic
  partners are extremely valuable to us. We currently do not have a succession plan for the replacement of Mr.
  Liang if it were to become necessary."* The one relationship that sets the product (the supplier's allocation)
  is described as personal. *"The moat will go when the surgeon goes."*

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** (the customer buys the supplier's platform, which
  every rival sells; the company cuts price to win share and expects selling prices to keep falling) · not
  price-regulated **[x]**
- **Class: NONE.** A fast, capable assembler with a real engineering lead in rack integration and cooling,
  earning a contract manufacturer's gross margin. **Direction: narrowing** (gross margin 18.0% to 10.8% over
  FY2023-26; the one strong quarter was a mix outlier the company had not guided).
- **The gate does not close on missing evidence.** The Taiwanese ODMs are not in the row and Lenovo is
  IFRS-only; neither is what fails the gate. It fails on Super Micro's own sentences about price, its own
  margin series, its own working-capital consumption, and a supplier margin six to seven times its own.

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
*OUT on the business: [E3-03] criterion (2) fails in the company's own words (price cut *"to gain market
share"* in FY2025 and FY2026; selling prices expected to keep declining); [E2-44] fails on both halves (no
pricing power; each dollar of growth consumes working capital, operating cash -$6.8bn in FY2026); [E4-04] is
engaged, the advantage re-won each platform generation with the old one written down; the return on capital is
real but is turnover times a thin margin that moves with the wave [E4-36, E3-51], and the gains sit with the
supplier [E3-62]; key-person dependence recorded as a moat defect [E4-23]. Not a finding that Super Micro is
badly run or technically weak: its engineering lead is recorded at full strength. **The file closes here.**
Q3-Q6 below are RECORDED, NOT GOVERNING, as at DLR, EQIX and the other Q2 closes in wave 5.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the brief
> asked for the conduct record to be settled on the filings and because a Q2 OUT written without reading it
> would leave the most consequential facts in the file unrecorded. It decides nothing and cannot reopen Q2
> [E2-37, E3-39].

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution [E3-38, E3-43, E2-70]: TICKED.** The product is the supplier's platform re-bought and
  re-sold every generation (Q2); the business carries **$12.9bn of inventory against a product cycle of about a
  year** and prices each large deal against Dell, HPE and the ODMs. [E2-70]'s root: an undifferentiated product
  *"magnifies"* the manager. A wrong inventory or pricing call is made every quarter, not once.
- [ ] **Control [E1-16]**: not ticked; a minority public holding.
- [ ] **Leverage [E3-29]**: not ticked. Assets $29.9bn on equity $14.5bn (about 2:1); debt $8.7bn against cash
  $7.5bn.

**Case declared: a BINARY GATE (daily execution). No price compensates [E5-35].**

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
**The record, from the filings and the SEC's own orders, in date order:**

| public | what | document |
|---|---|---|
| 2018-01-30 | the Senior VP Worldwide Sales and director **Wally Liaw** and the CFO **Howard Hideshima** *"have resigned"*, during an Audit Committee investigation begun August 2017 | 8-K `0001628280-18-000714` |
| 2018-08 to 2020-01 | stock suspended August 2018 and **delisted from Nasdaq March 2019 to January 2020** for failure to file (Form 25-NSE `0001354457-19-000123`; SEC order para. 5) | 25-NSE; SEC order |
| 2018-11-15 | Board concludes prior statements *"should no longer be relied upon"*; restatement *"primarily relates to the timing of recognition"* of revenue | 8-K Item 4.02 `0001628280-18-014419` |
| 2019-05-17 | FY2017 10-K filed, restating FY2015-16: the investigation *"determined certain employees had violated our Code of Business Conduct and Ethics and discovered accounting and financial reporting errors and certain irregularities"* | 10-K `0001375365-19-000039` |
| 2020-08-25 | **SEC cease-and-desist order**, Securities Act Rel. No. 10822: *"Super Micro's executives pushed employees to maximize end-of-quarter revenue and minimize expenses"*; revenue recognised *"before delivering the goods"*, *"incomplete or mis-assembled goods"* shipped at quarter-ends, a distributor's revenue *"more than $150 million"* recognised early, co-op marketing funds claimed *"to which Super Micro was not entitled"*; violations of **Securities Act 17(a)(2) and (3)** and Exchange Act 13(a), 13(b)(2)(A), 13(b)(2)(B); **$17.5M penalty**. The former CFO was separately ordered to pay disgorgement of $260,844, interest and a $50,000 penalty. **Charles Liang, then and now CEO, *"will also reimburse the Company for $2,122,000 pursuant to the claw-back provisions of the Sarbanes-Oxley Act"*.** | SEC order 33-10822 (fetched from sec.gov, `sec_order/`); Fair Fund orders 34-90313, 34-90373, 34-90784; 8-K `0001375365-20-000059` |
| 2021-05 to 2023-12 | **Liaw returns**: consultant May 2021, Senior VP Business Development August 2022, director December 2023 (DEF 14A `0001375365-26-000008`) | proxy |
| 2024-08-27 to 30 | a short-seller report (*"alleging evidence of accounting manipulation, sibling self-dealing and sanctions evasion"*, 10-K Item 1A); NT 10-K for FY2024 filed 2024-08-30; Special Committee formed | NT 10-K `0001375365-24-000031`; 10-K |
| 2024-10-30 | **Ernst & Young resigns** during its first audit: *"we are resigning due to information that has recently come to our attention which has led us to no longer be able to rely on management's and the Audit Committee's representations and to be unwilling to be associated with the financial statements prepared by management"*; EY had raised whether the Company *"demonstrates a commitment to integrity and ethical values"* (COSO Principle 1). EY's Exhibit 16.1 agrees with the 8-K's paragraphs describing its concerns. **The Company *"disagrees with EY's decision to resign"*.** | 8-K Item 4.01 `0001375365-24-000036`, EX-16.1 |
| 2024-11-18 | BDO appointed; SEC Enforcement subpoena received 2024-11-19 (*"In the Matter of Super Micro Computer, Inc."*), overlapping SDNY subpoenas of 2024-10-22 | 8-K `0001375365-24-000040`; 10-K Note 15 |
| 2024-12-02 | Special Committee (Cooley, Secretariat) reports: evidence *"does not give rise to any substantial concerns about the integrity of the Company's senior management or Audit Committee"*; but it reviewed the **rehiring of nine individuals who had resigned after the 2017 investigation**, found *"lapses"* for which the CFO/CCO *"had primary responsibility"*, including *"not informing EY prior to entering in June 2024 into a now terminated consulting arrangement with the Company's former CFO, who had resigned following the 2017 Audit Committee Investigation"*; recommended a **new CFO** (*"would commence a search for a new Chief Financial Officer immediately"*) and a Chief Accounting Officer | 8-K `0001375365-24-000044` and EX-99.1 |
| 2025-02-25 | FY2024 10-K filed six months late (no restatement); material weaknesses reported FY2024 and FY2025 | 10-K `0001375365-25-000004` |
| 2026-03-19/20 | **SDNY unseals an indictment of Liaw** (then Senior VP and director), a Taiwan sales manager and a contractor *"in connection with an alleged conspiracy to commit export-control violations"*; the Company *"is not named as a defendant"*; Liaw resigns from the Board | 8-K `0001375365-26-000011`, EX-99.1, EX-99.2 |
| 2026-08-31 | FY2026 10-K: SEC subpoena of 2026-04-28 on *"certain customers, including one customer that is the subject of the allegations in the Indictment"*; SDNY grand jury subpoena on *"the Company's compliance program and internal controls"*; multiple BIS/OEE subpoenas; *"The Company has not been informed that it is the target"*. An internal investigation (Munger, Tolles & Olson; AlixPartners) *"did not find any evidence that any current member of senior management had knowledge of the alleged diversion scheme"*. Internal control **not effective** at 2026-06-30 (one IT material weakness unremediated). **David Weigand is still CFO** (Item 10), twenty-one months after the Board adopted the recommendation to replace him; no filing read reports a successor. | 10-K `0001375365-26-000022` |

**Two things must be said, and neither is comfortable.**

**(a) The strongest case for OUT, at full strength [E4-51].** The same CEO has run the company since 1993 and
through all three episodes. The SEC found by consent that *"executives pushed employees to maximize
end-of-quarter revenue"* across three fiscal years and the CEO repaid $2.1M of pay under SOX 304. After that
investigation, management **rehired nine of the people who had resigned after it**; brought back the sales
executive who resigned alongside the CFO in January 2018 (Liaw: consultant 2021, Senior VP 2022, director 2023)
and put him on the Board; and took on as a consultant *"the Company's former CFO, who had resigned following the
2017 Audit Committee Investigation"* without telling the new auditor. (Inferences, stated as such: the Special
Committee release names neither the nine nor the former CFO. By the 2018 8-K's dates the CFO who resigned then was
Hideshima, whom the SEC later sanctioned; Liaw's resignation and return fit the description of the nine, but no
document read lists him among them.) That auditor then resigned, saying in writing it could no longer rely on
management's representations. The returned executive was indicted in 2026 for conspiring to evade export controls
on the company's own products. [E5-22]: *"the main problem was they didn't act when they learned"*;
here the filings show the opposite of acting: bringing the actors back. [E2-57]: *"the real mistake is not the
act, but the actor."* And the Special Committee's recommended CFO change had not happened by the latest 10-K.

**(b) Why it is not recorded as OUT here, and why it is not recorded as IN either.** [E5-16]'s binary is
*"personal misconduct"*. **No filing or order read makes a finding of personal misconduct against any current
officer**: the SEC order is against the company under negligence-based provisions (17(a)(2) and (3)); the SOX
304 reimbursement requires no personal fault; the Special Committee found no integrity concern about senior
management; the export investigation found no evidence that current senior management knew; the two sanctioned
or indicted individuals are gone. **Against that, the matters that would settle it are open and have not
produced their documents**: the SEC investigation opened 2024-11-19 and re-subpoenaed 2026-04-28, the SDNY grand
jury, BIS/OEE, and two consolidated securities class actions and several derivative suits (Note 15: *"too
preliminary"*). EY's letter and the Special Committee's report say opposite things about the same people, and
[E5-17] says *"Sincerity and empathy can easily be faked"*. **Can I name the document that would resolve this?
Not one that exists**: the SEC's and SDNY's conclusions have not been issued. **So the binary, if it governed,
would be UNKNOWABLE on the filed record, with the conduct record above stated in full**, and because the weight
case is a gate, no price would compensate [E5-35].

### THE INCENTIVE READ **[E4-27]**
*"Never, ever, think about something else when you should be thinking about the power of incentives."*
- **The CEO is paid in revenue and stock-price milestones.** FY2026 cash salary *"a nominal base salary of
  $1.00"*; the 2023 CEO Performance Award is *"a stock option for 5,000,000 shares at an exercise price of $
  45.00"*, vesting on *"specified stock price targets ($ 45.00 to $ 110.00 per share) and revenue-based operational
  milestones"*: annualized revenue milestones **$13.0bn to $21.0bn, all achieved**; price milestones $45-90
  achieved, $110 not (10-K equity note). The SEC's 2020 finding was pressure *"to maximize end-of-quarter
  revenue"*; the pay plan that followed pays on revenue. This is a prompt, not a finding [E5-38].
- **The CFO's bonus KPIs include "EPS (2x weighting)"** and *"Material Weakness Remediation"*, the latter scored
  **0%** for FY2026 (*"The Company did not achieve full remediation of material weakness with clean internal
  controls opinion"*).
- **The founders are selling.** Charles Liang and Sara Liu (joint holding) sold 200,000 shares on 2026-09-03/04
  at $36.60-$40.00 (Form 4s at Step 0).

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **Weak accounting [E4-22]: FIRES.** A restatement (FY2015-16), two years unfiled and a delisting
  (2018-20), an SEC antifraud order (2020), a six-month-late 10-K and an auditor resignation (2024), material
  weaknesses in FY2024, FY2025 and FY2026 (*"our internal control over financial reporting was not effective as
  of June 30, 2026"*). *"There is seldom just one cockroach in the kitchen."*
- [x] **Trumpeted projections [E4-22], and the record [E3-48]: FIRES.** Revenue guidance every quarter and every
  year, and the record against it (EX-99.1 releases): FY2025 guided **$26.0-30.0bn** (2024-08-06), cut to
  $23.5-25.0bn, then **$21.8-22.6bn** (2025-05-06), delivered **$21.97bn**; Q1 FY2026 guided $6.0-7.0bn,
  delivered **$5.0bn**; Q3 FY2026 guided *"at least $12.3 billion"*, delivered **$10.2bn**; Q4 FY2026 gross margin
  guided **8.2-8.4%**, delivered **17.5%**. FY2026 annual guidance rose from *"at least $33.0 billion"* to $38.9-40.4bn
  and was met ($39.06bn). FY2027 is guided at **$65.0-72.0bn**. Misses in both directions, large and frequent:
  not the smooth record [E4-30] describes, and [E5-30]'s ratchet is in place.
- [x] **Serial share issuance [E5-15]: FIRES.** 43.2M split-adjusted shares sold in FY2024 ($2.31bn); convertible
  notes of $1.725bn (2024), $0.7bn and $2.3bn (2025); **52.3M shares at $27.50 and $4.31bn of mandatory convertible
  preferred in June 2026** (converting into 130.7-156.8M more shares in 2029), plus a $1.25bn ATM; diluted
  weighted shares **602.1M (FY2024) to 697.3M (FY2026)**.
- [x] **EBITDA / adjusted earnings [E4-29], the CGNX companion rule applied: FIRES in the releases, not the
  10-K.** *"Adjusted EBITDA"* first appears in the EX-99.1 of 2025-05-06 (zero mentions in every release read
  before it, 2024-01 to 2025-04), **the same release that cut FY2025 guidance from $23.5-25.0bn to $21.8-22.6bn**,
  and is reconciled in every release since (FY2026: **$3,447.1M**, adding back $412.1M of stock compensation to
  $2,230.5M of net income). Headlines lead with GAAP net sales and gross margin; non-GAAP EPS excludes stock
  compensation. **[E2-49] metric-switching**: a yardstick added in the release that carried the deterioration
  fires small.
- [ ] **Unintelligible footnotes**: not ticked. The supplier that is 63.1% of purchases is not named in the note;
  the notes are otherwise legible.
- [ ] **Filed-figure tells [E4-30]**: not ticked. Cash taxes paid over pretax income: **15.2% (FY2023), 32.3%,
  27.0%, 14.3% (FY2026)** (cash-flow supplements; income statements); FY2026's fall sits beside income taxes
  payable rising $213.5M and is not a series trend. Reported growth is anything but smooth.
- [x] **The auditor's-eye test [E4-34], answered by an auditor in writing.** EY's letter is the rare case in which
  the auditor's view of management's representations is on the public record, and it is adverse. BDO has since
  given clean opinions on the statements with adverse ICFR opinions.
- **[E4-52] the flags converge**: weak accounting, a guidance culture, serial issuance, a pay plan on revenue and
  price milestones, and a late-added adjusted metric point the same way. Read as one system, per [E4-52], not as
  a count.

### STEP 3 - THE PRIMARY TEST **[E2-01]**, scoped by **[E2-43]**
- **Return on average equity** (net income over average stockholders' equity, filed balance sheets):
  **FY2022 22.6%, FY2023 37.7%, FY2024 31.2%, FY2025 17.9%, FY2026 21.5%**; FY2016-21 **5.7% to 11.0%**. Without
  undue leverage (debt $8.7bn against cash $7.5bn). The FY2026 denominator is inflated by $5.6bn of equity raised
  in June.
- **[E2-43] unleveraged net tangible assets**: Row C at Q2, **8.8% (with cash) to 12.6% (without)** after a
  notional tax in FY2026. No goodwill or intangibles exist to strip.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
**Mixed, with one sharp open question.** For: the 10-K states the EY resignation, the indictment, the subpoenas
and the material weaknesses in plain words, and the MD&A says twice that margin was given up *"to gain market
share"*. Against: the supplier that is 63% of purchases is unnamed; the Q4 FY2026 margin jump is explained in one
phrase (*"favorable customer and product mix"*) against guidance half its size. **The open question [E2-68]**: the
June 10, 2026 offerings (52.3M shares at $27.50 and $4.3bn of preferred convertible at the same reference price)
were sold under a prospectus whose *"Recent Developments"* section describes the ATM and a credit amendment and
nothing about the quarter then twenty days from its end (`424B5_2026-06-12_d44171.txt`, `0001193125-26-268520`);
on 2026-07-21 the company announced that quarter's gross margin at 15-17% against 8.2-8.4% guidance. **No document
read says what management knew on June 10.** It is recorded as a question, not a finding, and the documents that
would answer it (board and underwriter diligence records) are not public.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08, E5-24]**: one, **$200.0M for 4,891,171 shares (about $40.89) in June 2025**, from purchasers
  of the 2030 convertible notes. Condition (1), ample funds: operating cash had been **-$2,486.0M** the year before
  and the purchase was funded from a convertible issue. **Twelve months later the company sold 52.3M shares at
  $27.50.** *"What is smart at one price is dumb at another"*: it bought at about $40.89 and sold at $27.50, and
  the capital-allocation flag is stated with the humility clause [E4-13]: management knows the business better
  than this run does.
- **The institutional imperative [E2-30]**: (2) projects soak up funds: **ticked**, a new Silicon Valley campus,
  a Malaysia campus, capacity *"to support market demand"*, inventory bought ahead of lead times with deposits.
  (1), (3), (4): not scored from the filings.
- **Related parties**: purchases from Ablecom and Compuware (the CEO's brothers' companies; the CEO and his wife
  own about 10.5% of Ablecom) **$725.7M in FY2026, 2.1% of cost of sales** (face of the income statement), down
  from 4.3% in FY2024; family members of the co-founder director employed at $0.2-2.5M each (Item 13). Disclosed,
  and the kind of arrangement [E2-50] tells a reader to watch.

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name; the file is closed at Q2 [E2-37, E2-38, E3-39].
- [x] Key-person dependence recorded at Q2 as a moat defect [E4-23], not here as a strength.
- [x] No great-manager case is made [E2-35, E2-36].

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE on the binary.** Weight
  case a GATE (daily execution). No filed finding of personal misconduct against a current officer; a conduct
  record under the same CEO that includes an SEC antifraud order, the rehiring of the departed, an auditor's
  written refusal to rely on management, and a rehired director's indictment; three government investigations
  open whose conclusions do not yet exist. Flags live and converging: weak accounting, projections with a poor
  record, serial issuance, adjusted EBITDA added in a deteriorating release, pay on revenue and price milestones.
  *Not a finding that the managers are honest or dishonest [E5-17].*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks
> every run for a price and because the screen's negative owner earnings are the skip reason's other half; it
> decides nothing and cannot reopen Q2 [E2-37, E3-39].

### Owner earnings — the one number **[E2-23]**
Construction (CONVENTION, v4 section VI): operating cash flow, less stock compensation, less (c). Every figure
from the filed cash-flow statements: FY2024-26 from the FY2026 10-K face, FY2021-23 from the FY2023 10-K face,
FY2016-20 from companyfacts checked to the FY2019 and FY2020 faces (*"Net cash provided by (used in) operating
activities | 262,554 | | | 84,347"*; SBC *"20,189 | 21,184 | 24,656"*; D&A *"28,472 | 24,202 | 21,846"*)
(`oe.py`, `oe_out.txt`). No net-income proxy.

**What (c) is made of, asked before assuming it is plant.**
- **Plant is small and [E5-20] is not engaged for it.** Net property **$625.6M** on $39.1bn of sales; capex
  **0.4% of sales**; D&A $53.7M is all plant and equipment (no goodwill, no acquired intangibles exist). Capex ran
  **3.0x D&A in FY2026** because of expansion (*"the on-going construction of a new state-of-the-art business
  complex"*; FY2027 capex guided at *"$380.0 million to $400.0 million"*), which is growth, not renewal. The
  [E3-44]/[E2-41] default holds for plant, and the two plant ends differ by only about $60M a year over five years.
- **The real (c) question is working capital, which [E2-23] names in its own parenthesis:** *"If the business
  requires additional working capital to maintain its competitive position and unit volume, the increment also
  should be included in (c)."* SMCI's working-capital lines consumed **$9,648.3M in FY2026, $3,835.6M in FY2024**,
  and released $157.9M in FY2025 (the sum of the face's change lines). Part of that is growth (sales +78% and
  +110%); part is required to stand still, because **each supplier generation costs more per unit** (the FY2025
  average selling price rose 34%) and because the 10-K says it *"may place non-cancellable inventory orders for certain product
  components in advance of our historical lead times, pay premiums and provide deposits to secure future supply and
  capacity"* to hold its position. **No filing separates the two.** So (c) is shown at both of its honest ends: **all of the
  working-capital increment (the convention)** and **none of it (a display: operating cash before the
  working-capital lines, less the inventory write-downs the face adds back, because those are a real cost of the
  product cycle)**.
- **Stock compensation** subtracted in full at the face figure [E5-06]: $412.1M in FY2026, 14.5% of operating cash
  before working capital; SBC resolves and is complete on the face for every year used. [E3-70]'s market-value
  measure (the CEO's 2023 option alone is *"5,000,000 shares at an exercise price of $ 45.00"*) needs the grant
  table read by hand (a recorded source limit); the reported charge is the floor.

| $M | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| operating cash flow | -96.2 | 84.3 | 262.6 | -30.3 | 123.0 | -440.8 | 663.6 | -2,486.0 | 1,659.5 | -6,809.9 |
| of which working-capital lines | -209.0 | -36.1 | 116.5 | -164.4 | -40.0 | -769.8 | 26.9 | -3,835.6 | 157.9 | -9,648.3 |
| SBC (face) | 19.7 | 24.7 | 21.2 | 20.2 | 28.5 | 32.8 | 54.4 | 231.5 | 314.5 | 412.1 |
| capex | 29.4 | 24.8 | 24.8 | 44.3 | 58.0 | 45.2 | 36.8 | 124.3 | 127.2 | 162.0 |
| D&A | 16.4 | 21.8 | 24.2 | 28.5 | 28.2 | 32.5 | 34.9 | 29.6 | 41.3 | 53.7 |
| inventory write-downs added back on the face | 15.7 | 9.6 | 32.9 | 18.4 | 6.8 | 15.1 | n/a | 83.0 | 232.1 | 188.1 |
| **OE, convention, capex end** | **-145** | **35** | **217** | **-95** | **36** | **-519** | **572** | **-2,842** | **1,218** | **-7,384** |
| OE, convention, D&A end | -132 | 38 | 217 | -79 | 66 | -506 | 574 | -2,747 | 1,304 | -7,276 |
| *display:* before the working-capital build, capex end | 48 | 61 | 67 | 51 | 70 | 236 | 546 | 911 | 828 | 2,076 |
| *display:* same, D&A end | 61 | 64 | 68 | 67 | 99 | 249 | 547 | 1,006 | 914 | 2,185 |

*(FY2023's face carries no write-down add-back line, so nothing is deducted for that year. FY2016 is in
`oe_out.txt`; the screen's 5y capex end, -$1,793.7M, differs from this rebuild's -$1,790.9M because the screen
reads the $53.0M D&A element and an earlier vintage; immaterial.)*

**MORE THAN ONE WINDOW [E4-25, E4-38]:**

| window | convention, capex end | convention, D&A end | display, capex end | display, D&A end | working-capital lines, mean |
|---|---:|---:|---:|---:|---:|
| **five-year default [E2-42], FY2022-26** | **-$1,791M** | **-$1,730M** | **+$919M** | **+$980M** | -$2,814M |
| three-year, FY2024-26 | -$3,003M | -$2,906M | +$1,272M | +$1,368M | -$4,442M |
| ten-year, FY2017-26 | -$891M | -$854M | +$489M | +$526M | -$1,440M |
| FY2026 | -$7,384M | -$7,276M | +$2,076M | +$2,185M | -$9,648M |

**The combined range on the default window runs from about -$1.8bn to about +$1.0bn, and it SPANS ZERO.** In
words: over five years the business consumed about $1.8bn a year more cash than it produced for owners after
stock pay and plant, because it put about $2.8bn a year into inventory and receivables; before that build it
produced roughly $0.9-1.0bn a year. **[E4-25]: *"Usually, the range must be so wide that no useful conclusion can
be reached."* This is that case.** The width is itself the Q4 finding [E5-11]: every window contains a
working-capital year of several billion dollars in one direction or the other (FY2022, FY2024, FY2026 out; FY2023,
FY2025 back), and the quarterly gross margin ran from 6.3% to 17.5% within twelve months. **[E4-41] favourable
breaks named**: FY2026's display figure carries the 17.5% Q4 margin the company had guided at 8.2-8.4%; on the
first three quarters alone the year's gross margin was about 8.2% (full-year gross profit less Q4, $2,284.6M, over
sales less Q4, $27,943.3M).

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [x] **good, at its lower edge, on the book numbers** · [ ] gruesome
Pre-tax operating income over average invested capital was **21-43% in FY2022-26** (Q2). On the increment
FY2023 to FY2026, operating income rose **$2,009.4M** while invested capital (equity plus debt less cash) rose
**$13,856.4M**: **14.5% pre-tax on the added capital**, against [E4-43]'s *"$82 million pre-tax on $400 million of
net tangible assets"* (20.5%). **Against it, in cash**: cumulative operating cash FY2022-26 was **-$7,413.6M**
while cumulative net income was **$5,357.1M**; the added capital came from **$2.31bn (FY2024) and $5.64bn (FY2026)
of new equity, $4.73bn of convertibles and $3.76bn of net bank borrowing** (cash-flow statements FY2024-26). [E5-40]: cash-consuming businesses are *"unattractive
unless the cash they consume gets to earn a reasonable return"*; 14.5% pre-tax on the increment is a return, and
it is earned on capital the owners supply every year.

### Staying power — score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: NO.** Operating cash negative in three of the last five years;
  quarterly gross margin 6.3% to 17.5% within FY2026; one customer 28.1% of sales; guidance missed in both
  directions (Q3).
- **(2) Massive liquid assets: PARTLY.** Cash **$7,521.5M** at 2026-06-30, a month after $5.64bn of equity was raised,
  against **$8.7bn** of debt; $870.5M of the cash is held abroad.
- **(3) No significant near-term cash requirements: NO, and this is the one.** *"we have current obligations
  related to non-cancelable purchase commitments of $34.2 billion"* (MD&A; Note 15: *"primarily through the next 12
  months"*), against customers who *"cancel or defer purchase orders on short notice without incurring a
  significant penalty"* (Item 1A). Current bank debt **$2,039.8M**; the JPMorgan revolver is secured on *"substantially
  all assets"* during a non-investment-grade period; the Taiwan lender E.SUN granted *"A one-time waiver ... for the
  verification of the debt-to-net worth and interest coverage ratios for the period ending October 31, 2026"*;
  preferred dividends about **$302M a year**; convertibles of $0.7bn (2028), $1.725bn (2029), $2.3bn (2030).
- **Score: 0 to 1 of 3.** **Leverage [E4-16, E3-29]**: debt $8.7bn, equity $14.5bn; not the 20:1 case. **[E2-54]'s
  coverage test, as written**: FY2026 interest expense $194.6M against *"current cash flow net of ample capital
  expenditures"*: operating cash **-$6,809.9M** less capex = **not covered**; before the working-capital build
  ($2,838.4M less $162.0M), **13.8x**. Which of those two is the business's cash flow is the (c) question above.
  **[E3-52] terms**: covenanted bank lines, one waiver in hand; the preferred and convertibles carry no
  maintenance covenants read.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: the generation turns while the company is long it.** Super Micro is committed to buy **$34.2bn**
of product it may not cancel and holds **$12.9bn** of inventory, **$47.1bn together, 3.3 times its equity**, in
components whose value is set by a supplier that launches a new generation about every year, to sell to customers
who may cancel and one of whom is 28.1% of sales. The DELL run's own bear case lives here too.

**Quantified from filed figures, [E3-24]'s way.** A write-down of **10%** of inventory plus commitments is **$4.7bn**,
about one full year of FY2026 gross profit ($4.2bn); **30%** is **$14.1bn, about the whole of stockholders' equity
($14.5bn)**. The filed record of write-downs is **5.7% of opening inventory in FY2024 ($83.0M on $1,445.6M)**,
**5.4% in FY2025 ($232.1M on $4,333.0M)** and **4.0% in FY2026 ($188.1M on $4,680.4M)**, all in a rising market.
**[E4-40], exposure not experience**: every year of that record is a boom year; the exposure is the $47.1bn, and
the experience of 2024-26 is exactly what [E4-40] says not to extrapolate from. A second, separate mechanism is on
the filed record: *"BIS could seek to suspend, revoke or deny our export privileges, including through a temporary
or permanent denial order"* (Item 1A), which would stop the business's shipments regardless of demand.

- Survival shapes (`Screens/SURVIVAL SHAPES - index.md`): **#1 CONTRACTED NOT TO STOP** ($34.2bn of non-cancelable
  purchase commitments against cancellable customer orders), with **#11 THE PASS-THROUGH** as the reason margin
  cannot absorb a write-down (Q2: 9.2 cents of gross profit per incremental dollar), **#6 THE BORROWED BALANCE SHEET**
  as a feature (growth funded by $7.95bn of equity, $4.73bn of convertibles and $3.76bn of net bank borrowing since FY2024), and
  **#17 THE PERMIT** as a second exposure (export privileges held at a government's discretion while its own people
  are under indictment). **No new shape is proposed.**
- **Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility** for a multi-billion-dollar
  write-down year; **a low-level possibility** for insolvency while $7.5bn of cash and fresh equity stand behind it.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE**
  *The five-year owner-earnings range runs from about -$1.8bn to about +$1.0bn a year and spans zero, on a (c)
  whose working-capital part no filing separates into growth and maintenance [E4-25, E2-23]; staying power scores 0
  to 1 of 3, with $34.2bn of non-cancelable purchases against cancellable orders [E5-11]. The business is likely to
  survive the near term on the capital just raised; what it earns for an owner cannot be stated in a range narrow
  enough to use.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Q5 does not open: Q2 is OUT (and Q3 and Q4, recorded, are UNKNOWABLE). The arithmetic below is recorded
because the queue asks every run for a price, and it carries no entry language. It is not a ranking and it arms
nothing.*

**The pair:** price **US$40.35**, the **2026-09-17 close** (Yahoo daily chart, aggregator, flagged; corroborated
by Form 4s `0001392942-26-000013` and `0001392941-26-000014`, sales at $36.60-$40.00 on 2026-09-03/04 inside those
days' ranges) x **656,965,384 shares** (FY2026 10-K cover, accession `0001375365-26-000022`, as of 2026-07-31) x
split factor **1.0** = **market capitalisation US$26,508.6M**. **Perimeter-consistent, with the mandatory
convertible preferred at its minimum conversion (130,686,000 shares, the rate that applies above about $33.00):
US$31,781.7M**, used as the harder denominator; the preferred dividend is then not also deducted. **Sovereign USD
30-year 5.29%**, US Treasury daily par yield curve, the issuing authority, **09/17/2026**.

Owner earnings are levered (operating cash is after interest paid), so no debt is added to the cap; interest income
($186.9M in FY2026) is left in, and the $7.5bn of cash is left in the cap; they roughly offset. (`q5.py`,
`q5_out.txt`.)

| construction | owner earnings | yield on $26.5bn (common) | yield on $31.8bn (with preferred) | vs 5.29% (harder cap) | perpetual growth needed to reach ~10% |
|---|---:|---:|---:|---:|---:|
| **five-year default, convention, capex end** | **-$1,791M** | -6.76% | **-5.63%** | **-10.92 pts** | **refused: a negative base has no growth rate** |
| five-year, convention, D&A end | -$1,730M | -6.53% | -5.44% | -10.73 pts | refused |
| FY2026, convention, capex end | -$7,384M | -27.86% | -23.23% | -28.52 pts | refused |
| **five-year, display (before the working-capital build), capex end** | **+$919M** | 3.47% | **2.89%** | **-2.40 pts** | **6.9%** |
| five-year, display, D&A end | +$980M | 3.70% | 3.08% | -2.21 pts | 6.7% |
| three-year, display, capex end | +$1,272M | 4.80% | 4.00% | -1.29 pts | 5.8% |
| ten-year, display, capex end | +$489M | 1.85% | 1.54% | -3.75 pts | 8.3% |
| FY2026 alone, display, capex end (carries the 17.5% Q4) | +$2,076M | 7.83% | 6.53% | +1.24 pts | 3.3% |
| *display only, not owner earnings:* the company's Q1 FY2027 GAAP EPS guidance ($0.89-0.98 x 745M diluted), x4 | $2,652-2,920M net income | | 8.35-9.19% | | |

**1. THE YIELD.** On the convention: **negative on every window.** Before any working-capital build: **2.9% (five-year)
to 6.5% (FY2026 alone)** on the perimeter-consistent cap, against **5.29%**. **Even the company's own projection,
annualised, before a dollar of working capital, sits below the ~10% floor [E4-28]** (8.4-9.2%), and it is a
projection, which [E3-48] says to set against the record rather than use.

**2. WHAT THE PRICE ALREADY ASSUMES.** On the five-year display, about **6.9% a year of growth in perpetuity** to reach
~10%; on the convention, no growth rate exists because the base is negative. **What the business has done**: sales
+77.8% (FY2026), +46.6%, +110.4%, and owner earnings on the convention were negative in FY2024 and FY2026 and positive in FY2025
only because working capital was released that year. [E4-35]'s base rate (*"fewer than 10 of the 200 most profitable companies"* sustain
15% growth for 20 years) and **[E4-44]'s bound** (value *"cannot over the long term grow faster than its earnings
do"*) bind; **[E2-63]'s ceiling**: growth here is bought with working capital at about 14.5% pre-tax on the increment
(Q4), with the share count rising to pay for it.

**3. WHAT YOU ARE PAID.** On the five-year display, **-2.4 points against the sovereign**; on the convention, about
**-11 points**.

**Certainty is not priced in the rate [E3-42].** Sovereign used 5.29%, bare. No per-name premium.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
Value per share = owner earnings / (0.10 - g), over 787,651,384 shares (common plus the preferred's minimum conversion):

| owner earnings | g = 3% | g = 5% | g = 7% |
|---|---:|---:|---:|
| five-year display ($919M) | $17 | $23 | $39 |
| three-year display ($1,272M) | $23 | $32 | $54 |
| FY2026 display ($2,076M) | $38 | $53 | $88 |
| five-year convention (-$1,791M) | no value computable | | |

**Value, in round numbers: nothing on the convention; roughly $15-35 a share on the display at 3-5% growth over the
three- and five-year windows; $40-55 only at 7% growth forever on those windows, and up to about $90 on FY2026 alone
at 7%.** **Current price: $40.35, above the display's 3-5% band and inside the whole range, which runs from nothing to
about $90.**

**Which bar:** the screamer test [E4-01] only, because the file is closed and no margin is applied. **The price sits
inside the range: *"no useful conclusion can be reached"*; move on.** Windage count: **ONE** (the working-capital
part of (c) shown at both ends rather than chosen; growth rates displayed, not chosen).

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a business yield of
  **-5.6% (convention) to +2.9% (display) on the five-year default** against a 5.29% sovereign and a ~10% floor
  [E4-28]; even the best single year and the company's own projection sit below the floor. **FAIL on price as well,
  on every construction on disk.**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed. These are the conditions on which the file
> would be REOPENED at Q2 [E1-02]; a Q2 OUT is a finding about the business, so a price alert would be a category
> error (the QLYS ruling, 2026-09-07).

**What would reopen Q2 (each observable in a filing):**
1. **Gross margin that holds above its own FY2023 level through a platform transition.** Annual gross margin back
   above **15%** (FY2016-23 range 12.8-18.0%) for two consecutive 10-Ks, including a year in which the supplier
   launches a new generation, with the MD&A no longer attributing the change to *"competitive pricing to gain market
   share"*. The Q4 FY2026 17.5% is one quarter; four such quarters in a row would be the start.
2. **Growth that stops consuming the owners' capital.** Operating cash flow above stock compensation plus capex in
   a year in which sales grow more than 30%, i.e. the working-capital build funded by the business rather than by
   equity and bank lines; [E2-44](2)'s *"only minor additional investment of capital"*.
3. **A position the row can see.** Gross margin at or above Dell ISG's and HPE Server's for three years, or a filed
   statement that selling prices are no longer expected to decline (the Item 1A sentence withdrawn with reasons).
4. **A key-person answer.** A named CEO succession plan (Item 1A says there is none), and the Special Committee's
   CFO replacement completed.

**What would reopen Q3 on the record (recorded because Q3 is UNKNOWABLE, not OUT):** the conclusions of the SEC
investigation (*"In the Matter of Super Micro Computer, Inc."*), the SDNY grand jury and the BIS/OEE inquiries, in
either direction; and an unqualified internal-control opinion.

**Thesis-confirming (for the OUT):** gross margin back below 10% as the next platform ships; another year of negative
operating cash on sales growth; the ATM used; the preferred converting at the maximum rate (price below $27.50 at
the 2029 averaging period); inventory write-downs above FY2024-25's 5.4-5.7% of opening inventory; customer concentration above 25%.

**Next dated documents:** the Q1 FY2027 10-Q and earnings release (early November 2026; the $14.5-15.5bn guidance and
whether the Q4 margin held), the 2027 proxy (whether a CFO successor or CEO succession plan is named), and any SEC,
SDNY or BIS resolution.

**Position size:** none. **VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and the reopening
conditions are recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, **Q2 OUT, the file closed**; Q3, Q4, Q5 and Q6
  recorded beneath explicit RECORDED, NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed income
  statement, cash-flow statement and notes. The Taiwanese ODMs missing from the Q2 row are named and are not what
  closes the gate.
- [x] No UNRESEARCHED verdict was returned. The two recorded UNKNOWABLE verdicts (Q3, Q4) state what cannot be
  known: the conclusions of three open government investigations that do not yet exist (Q3); the split of the
  working-capital increment into growth and maintenance, which no filing makes, and a range that spans zero (Q4).
- [x] Step 0: the filing was read with accession numbers; three cash-flow figures cross-checked to companyfacts; the
  one that does not match (D&A $53.673M on the face, $53.0M in the only tagged element) named.
- [x] Owner earnings on the five-year default, three-year, ten-year and FY2026 windows, both plant ends of (c) and
  both working-capital ends of (c), from the filed cash-flow statements; (c) disclosed as a judgment [E2-23].
- [x] Competitor row filled from filings (Dell ISG, HPE Server, Celestica, NVIDIA; two of the seven rivals the 10-K
  names) with its gap stated; SMCI figures rebuilt from SMCI's own filings, not imported from the DELL run.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/17/2026, struck by this run.
- [x] Value stated as a round-number range under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as a close, aggregator flagged, corroborated by two Form 4s inside the days' ranges;
  `tools/sources.price()`'s intraday figure recorded and not used.
- [x] Run committed to git after every gate, with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this run wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q2, corrected in the next commit (`d6b0305`)**: the first committed Q2 said *"Four of the eight the 10-K names
   are in the row"* and that the 10-K *"names five rivals by name plus three ODMs"*. The 10-K names seven (Cisco, Dell,
   HPE, Lenovo; Foxconn, Quanta, Wiwynn); two are in the row, and Celestica is an addition the 10-K does not name.
2. **Q3, corrected before Q4 was committed (`26fbaa8`)**: the first committed Q3 (`a68666e`) said management rehired
   *"the sales executive who resigned alongside the sanctioned CFO"* as one of the nine and *"took the sanctioned
   former CFO on as a consultant"*. The Special Committee release names neither the nine nor the former CFO; both
   identifications are inferences from dates and are now labelled as such.
3. **Drafts corrected before commit, recorded because they were mine**: a Step 0 draft blamed `working_capital_flag`'s
   `None` on a defect before its code was read (it is a scope limit: the flag reads liability lines only); a Q2 draft
   gave the pre-AI growth rate as *"3.6% a year"* and *"2.2%"* (the filed figures give 9.8% FY2016-21 and 1.9%
   FY2018-21) and the pre-AI operating margin range as 2.6-6.8% (2.6-4.8% in the years cited); a Q3 draft gave ROE
   figures off by 0.1 point and an FY2016-21 range of 7.5-11.2% (5.7-11.0%); a Q4 draft gave FY2024's write-down as
   1.8% of opening inventory (5.7%), cumulative net income as $5,357.9M ($5,357.1M), the convertibles-and-bank total as
   $6.7bn ($4.73bn plus $3.76bn), and paraphrased the 10-K's *"may place"* as *"must place"*; the Step 0 minimum
   preferred conversion was first typed as 130,689,000 shares (130,686,000).

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The probe reprinted a guard the screen had already fixed.** `_probe_screen.py` calls `share_count_shift(facts)`
   without the ticker, so it returns the pre-2026-09-02 **11.2x**; with the ticker the current guard returns **1.12x**.
   The 11.2x is the 10-for-1 split of 2024-10-01, and it was the guard that actually stopped SMCI at triage.
2. **The brief read `restatement_shift -> (1.0, 2018-06-30)` as a flag.** A ratio of 1.0 means no disagreement was
   found; the function stops at the first revenue element with data and cannot see the FY2015-16 restatement, which
   sits under different elements.
3. **The six memory items, tested: all six held on the filings, and the filings add precision.** The restated
   annual statements are **FY2015-FY2016** (in the FY2017 10-K of 2019-05-17), with FY2017's quarters restated by 10-Q/A;
   the SEC order says the misstated reports ran *"beginning with the period ended September 30, 2014 through the period
   ended March 31, 2017"*. The order (Securities Act Rel. No. 10822, 2020-08-25) is against the company; the former CFO
   (Howard Hideshima) was sanctioned in a separate proceeding; the CEO repaid $2,122,000 under SOX 304. EY resigned
   2024-10-24 (8-K of 2024-10-30), BDO was appointed 2024-11-18, the split was 10-for-1 (2024-10-01), and Ablecom and
   Compuware are the related parties. **The 2026 matter the brief was unsure of is real and sharper than it
   suggested**: the indicted individual is a co-founder, Senior VP and sitting director who had resigned in January
   2018 during the first investigation and been brought back (consultant 2021, director 2023).
4. **The brief did not anticipate the perimeter change of June 2026**: $4.31bn of mandatory convertible preferred
   converting into 130.7-156.8M shares (+20-24%), a 52.3M-share offering and a $1.25bn ATM, all after the last dei
   count the probe read (601.4M at 2026-04-30).
5. **The brief did not anticipate the $34.2bn of non-cancelable purchase commitments**, which is the Q4 finding.
6. The brief was right that the skip reason was a prompt and not a verdict, and right to warn about `sources.price()`.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.price()` returns an intraday `regularMarketPrice` stamped with today's date** while its docstring
  says *"Latest close."* Fourth name (TOST, EQIX, DLR, SMCI).
- **`floor_screen.working_capital_flag` reads only liability-side lines** (`WC_TAGS`: payables, accrued liabilities,
  contract liabilities, deferred revenue). SMCI's working capital moved through **inventories (-$8,876.7M) and
  receivables (-$3,921.9M)** in FY2026 and the flag returned `None`. Adding `IncreaseDecreaseInInventories` and
  `IncreaseDecreaseInAccountsReceivable` would change which rows carry a note, so it is a proposal for the operator.
- **`restatement_shift` stops at the first revenue element with data**, so a restatement recorded across an element
  change (SMCI: `SalesRevenueNet` original, `Revenues` restated) returns 1.0, a null that reads like a finding.
- **`share_count_shift` is called without the ticker by the probe**; the split division only happens when the ticker
  is passed. A brief-writing probe should pass it.
- **D&A**: the FY2026 face line (*"Depreciation and amortization | 53,673"*) is in no published element; the screen reads
  `DepreciationDepletionAndAmortization` = $53.0M. Immaterial here.
- `Screens/cover_shares.py SMCI` matched the 10-K cover exactly.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Read the commitments note before the cash-flow statement tells you the business is growing.** SMCI's income
statement shows a record year and its Q4 release a 17.5% margin; its Note 15 shows **$34.2bn of purchases it cannot
cancel** against customers who can, which is 3.3 times its equity once the $12.9bn of inventory is added. The same
line exists in every hardware and component filer's 10-K, and it is the survival question [E5-11] calls the one
that usually kills.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** SMCI FAILS AT Q2 (OUT, on [E3-03] criterion (2) in the company's own words: gross margin given up
  *"to gain market share"* in FY2025 and FY2026 and selling prices *"we expect ... will continue"* to decline; the
  product is the supplier's platform, 63.1% of purchases from one supplier, sold by every rival; gross margin 18.0%
  (FY2023) to 10.8% (FY2026), below Celestica's 12.1% and under half Dell ISG's and HPE Server's; [E2-44] fails on both
  halves, operating cash -$6.8bn in FY2026 on a $9.6bn working-capital build; [E4-04] engaged, the advantage re-won
  each platform generation; key-person dependence [E4-23]). Q1 IN; Q3 recorded UNKNOWABLE on the binary (gate case;
  SEC antifraud order 2020 with a CEO SOX 304 clawback, EY's 2024 resignation letter, a co-founder director brought
  back and indicted in 2026, three investigations open); Q4 recorded UNKNOWABLE (five-year owner earnings -$1.8bn to
  +$1.0bn, spanning zero; $34.2bn of non-cancelable purchase commitments; shape #1); price $40.35 x 656,965,384 =
  $26.5bn ($31.8bn with the mandatory preferred's minimum conversion), headed COMPUTATION — NOT A CLEARANCE: yield
  -5.6% to +2.9% on the five-year default against 5.29%; Q6 arms nothing.
- Work order: none. UNKNOWABLE (recorded sections only): the SEC, SDNY and BIS conclusions (Q3); the growth and
  maintenance split of the working-capital increment (Q4).
