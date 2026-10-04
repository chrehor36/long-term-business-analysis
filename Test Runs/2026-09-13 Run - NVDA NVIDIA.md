# Company Run — NVIDIA Corporation (NVDA) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*WAVE 5 of the watchlist queue, row "capex unresolved [E5-20]: build (c) by hand from the filing". NVIDIA had no row in the master
queue or the triage CSV; it was never priced by the screen. Research, scripts and extracted filing text: `Test Runs/_research 2026-09-13
NVDA/`. Run unattended under the write-early protocol; each section was written as it closed. Prior art read for what it found, binding
nothing: the semiconductor and customer runs of 2026-09-06/07/13 (AMD, AVGO, MRVL, INTC, DELL, ORCL, TSM, AMZN), each opened before use.*

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
- rate **5.35%** · date **09/11/2026** · source (issuing authority) **US Treasury daily par yield curve, 30-year**, struck fresh by
  `tools/sources.py` `sovereign("USD")` on 2026-09-13 (a Sunday; 09/11 is the latest business day). Not inherited from any run.
- FX: none. NVIDIA reports in USD and the quote is USD. Revenue is assigned by customer headquarters (United States 69.6% of H1 FY2027,
  Taiwan 21.9%, China incl. Hong Kong 7.0%); that is a mix of customers, not a quote-currency mismatch.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (stock compensation, intangibles, marketable and non-marketable
  securities, supplemental information, derivatives and guarantees, debt, commitments and contingencies, income taxes, equity, segments,
  leases), Part II risk factors, Item 2 repurchases, Item 5 trading arrangements
- documents · date · accession no. (newest 10-K and 10-Q confirmed from EDGAR submissions, `submissions.json`, not from the brief):
  - **10-Q for the quarter ended 2026-07-26 (Q2 FY2027)**, filed 2026-08-26, `0001045810-26-000075` (primary: balance sheet, six-month
    cash flows, commitments, guarantees, investments, debt, segments, risk factors)
  - **10-Q for the quarter ended 2026-04-26 (Q1 FY2027)**, filed 2026-05-20, `0001045810-26-000052`
  - **10-K for FY2026 (ended 2026-01-25)**, filed 2026-02-25, `0001045810-26-000021`; and the 10-Ks for FY2025 `0001045810-25-000023`,
    FY2024 `0001045810-24-000029`, FY2023 `0001045810-23-000017`, FY2022 `0001045810-22-000036`, FY2021 `0001045810-21-000010`
  - **DEF 14A**, filed 2026-05-12, `0001045810-26-000036`
  - **8-K EX-99.1 earnings releases** (and EX-99.2 CFO commentaries): 2026-08-26 `0001045810-26-000073`, 2026-05-20 `0001045810-26-000051`,
    2026-02-25 `0001045810-26-000019`, 2025-11-19 `0001045810-25-000228`, 2025-08-27 `0001045810-25-000207`, 2025-05-28 `0001045810-25-000115`
  - **Other 8-Ks read:** 2026-09-03 Item 8.01 (`0001045810-26-000078`, Hugging Face); 2026-08-17 Items 1.01/2.03/7.01 (`0001045810-26-000069`,
    SB Energy guarantees); 2026-06-18 Item 8.01 (`0001193125-26-275783`, $25.0bn notes); 2025-04-15 Item 8.01 (`0001045810-25-000082`, H20
    licence); 2025-01-17 Item 8.01 (`0001045810-25-000007`, AI Diffusion rule); 2023-10-17 and 2023-10-24 Item 8.01 (`0001045810-23-000217`,
    `-000221`); 2022-08-31 and 2022-09-01 Item 8.01 (`0001045810-22-000146`, `-000151`, A100/H100 licence); 2022-02-08 Item 1.02
    (`0001045810-22-000005`, Arm termination)
- **figure cross-checked against the filed statement:** FY2026 net cash provided by operating activities **$102,718M**: `tools/run.py`
  (XBRL) reads 102,718; the FY2026 10-K consolidated statement of cash flows reads *"Net cash provided by operating activities | 102,718 |
  64,089 | 28,090 |"*. **Match.** Also: *"Purchases related to property and equipment and intangible assets | ( 6,042 ) | ( 3,236 ) | ( 1,069 )"*
  matches the screen's capex for FY2026-FY2024 to the million. Six-month FY2027 OCF
  **$74,421M** read off the 10-Q face. SBC FY2026 **$6,386M** matches the screen's resolved value.
- **Share count:** the 10-Q cover, `0001045810-26-000075`: *"The number of shares of common stock, $0.001 par value, outstanding as of
  August 21, 2026, was 24.1 billion."* **The cover is rounded to a tenth of a billion**, so the measurement uses the condensed consolidated
  statement of shareholders' equity in the same 10-Q: **24,147 million shares at 2026-07-26** (*"Balances as of Jul 26, 2026 | 24,147"*),
  with the cover as the cross-check (24,147M rounds to 24.1bn). **Single class**: *"Preferred stock, $ 0.001 par value; 2 shares
  authorized; none issued"* and *"Common stock, $ 0.001 par value; 80,000 shares authorized; 24,304 shares issued and outstanding as of
  January 25, 2026"* (10-K FY2026 balance sheet, in millions). **Splits verified from the filings, not memory:** FY2022 10-K *"On July 19,
  2021, we executed a four-for-one stock split"*; FY2025 10-K *"Shareholders of record at the close of market on June 6, 2024 received nine
  additional shares"* (ten-for-one). **No split after the measurement date** (`split_factor_after("NVDA", "2026-07-26")` = 1.0).
- **Price:** **US$218.29, close of 2026-09-11** (Yahoo via `tools/sources.py:price()`; **aggregator, flagged: live quote only**).
- **Market cap:** 218.29 × 24,147M = **US$5,270.9bn** (on the rounded cover 24.1bn: US$5,260.8bn, which is `run.py`'s figure).

### THE DEALS, READ BEFORE PRICING (the `deal_note` said nothing deal-shaped, and it was wrong)
`deal_note(CIK)` returned *"1 8-K Item 1.01 filing(s) since 2026-02-25, none carrying a merger agreement (EX-2.1) - most likely a credit
facility or offering"*. **The Item 1.01 is the SB Energy guarantee, not a credit facility. And the acquisition was announced under Item
8.01, which `deal_filings()` does not read at all.**
- **NVIDIA IS THE ACQUIRER of Hugging Face** (8-K 2026-09-03, Item 8.01): *"On September 2, 2026, NVIDIA Corporation ("NVIDIA") entered
  into a definitive agreement to acquire Hugging Face, Inc. ... The transaction includes an approximately $11.9 billion purchase price
  payable to Hugging Face stockholders, subject to certain adjustments, and an equity-based retention program of up to approximately $1.0
  billion"*; *"expected to close in the first half of 2027"*. Against a US$5,271bn cap it is ~0.2%. **Nothing on file makes NVIDIA a target,
  so the quote is not a spread.** The perimeter will change after the close; no owner-earnings window below crosses it.
- **SB Energy residual value guaranties** (8-K 2026-08-17 and 10-Q Note 10): *"NVIDIA's aggregate payment obligation is cumulatively
  capped at $105 billion for its initial commitment"*, on leases of ~4.25 GW whose tenant is *"An affiliate of OpenAI Group PBC"*, payable on
  *"OpenAI's insolvency resulting in a default under a lease, or ... OpenAI's failure to make payments under a lease"*, first phase expected
  in fiscal 2029. Carried to Q2 and Q4; it is not a merger and does not make the quote a spread.
- **$25.0bn of senior notes** (June 2026, seven tranches, 2028-2056; 8-K `0001193125-26-275783`, 10-Q Note 9). Financing, not a deal.
- **Groq, Inc.:** a financing-activities line *"Groq, Inc. | ( 2,944 )"* in H1 FY2027 and *"Accrued purchase consideration (3) | 986 |
  3,921"* footnoted *"Related to the Groq, Inc. non-exclusive license agreement"* (10-Q). Read at Q1 from the 10-K.

### THE SKIP REASON, TESTED FIRST: a TOOLING ARTEFACT, the same class as AMZN
The wave 5 row says *"capex unresolved [E5-20]: build (c) by hand from the filing"*. Tested in two parts, as the AMZN dated note asks.
- **The screen as it stood when the label was written.** `Screens/floor_screen.py` at `a8bc84f` (2026-09-01 22:15), run on NVIDIA's
  companyfacts of today (`old_screen.py`, output `old_screen_out.txt`), returns **`CAPEX_UNRESOLVED`**. Its `annual()` carries the comment
  *"first tag that yields data wins, like the run convention"* and its `CAPX_TAGS` begins `PaymentsToAcquirePropertyPlantAndEquipment`,
  which **NVIDIA used only for FY2010-FY2012** ($77.6M, $97.9M, $138.7M); `PaymentsToAcquireProductiveAssets` carries FY2022-FY2026 and was
  never read. **Every window after FY2012 therefore had no capex, and the row went unpriced.**
- **The current screen prices it.** `floor_screen.owner_earnings()` today (`screen_check_out.txt`): `{'5y_da': 36,250.6, '5y_capex':
  35,420.8, '3y_da': 57,978.7, '3y_capex': 56,626.0}` ($M). `tools/run.py NVDA` (no `--write`, `runpy_out.txt`): three-year mean
  **$56,480M-$58,125M**, five-year $35,293M-$36,378M, yield 1.07%-1.10%.
- **A second, real gap the fix does not close:** companyfacts carries **no undimensioned us-gaap capex fact for FY2013-FY2021 under any tag**
  (the FY2019-FY2021 values are absent from every tag searched). NVIDIA's own line is *"Purchases related to property and equipment and
  intangible assets"*. Any window longer than five years must be built from the filed cash-flow statements, which Q4 does.
- **So the label was wrong for a tooling reason, as at AMZN.** Whether the [E5-20] exception class applies is a separate question, asked at
  Q4 on the filing.

**Tooling defects found at Step 0 (recorded, no tool edited):**
1. `Screens/cover_shares.py NVDA` printed **"Common Stock, $0.001 par value per share 1,045,810,000,000,000"**: it read NVIDIA's CIK
   (1045810) as the share count and scaled it by the renderer's "shares in Billions" header. The cover says 24.1 billion.
2. `tools/sources.py:deal_filings()` reads only deal forms and 8-K Item 1.01; **an acquisition announced under Item 8.01 (Hugging Face,
   $11.9bn) is invisible to it.** Here the subject is the acquirer and the miss does not change the quote; had NVIDIA been the target, the
   ROKU error would have repeated.
3. The screen's D&A end reads `DepreciationDepletionAndAmortization`, which includes amortization of acquisition intangibles (FY2021:
   depreciation $486M plus intangible amortization $612M = $1,098M); for NVIDIA the "D&A end" of (c) is not property depreciation (Q4).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Where the money is, FY2026 and the trailing twelve months to 2026-07-26** (TTM = FY2026 − H1 FY2026 + H1 FY2027, from the FY2026 10-K
segment note and the Q2 FY2027 10-Q segment note; $M):

| | FY2024 | FY2025 | FY2026 | TTM to 2026-07-26 |
|---|---|---|---|---|
| Revenue | 60,922 | 130,497 | 215,938 | **302,970** |
| Compute & Networking revenue / segment operating income | 47,405 / 32,016 | 116,193 / 82,875 | 193,479 / 130,141 | 275,409 / **195,755** |
| Graphics revenue / segment operating income | 13,517 / 5,846 | 14,304 / 5,085 | 22,459 / 9,156 | 27,561 / 12,114 |
| Data Center revenue (of which networking) | 47,525 (8,575) | 115,186 (12,990) | 193,737 (31,376) | H1 FY27 164,269 of 177,837 (92.4%) |
| Gross margin (GAAP) | 72.7% | 75.0% | 71.1% (incl. $4.5bn H20 charge) | 75.0% in Q2 FY27 |
| Operating income (consolidated) / margin | 32,972 / 54.1% | 81,453 / 62.4% | 130,387 / 60.4% | 197,579 / 65.2% |
| Research and development, % of revenue | 14.2% | 9.9% | 8.6% | 7.5% (H1 FY27) |
| Property and equipment, net (period end) | — | 6,283 | 10,383 | 14,285 |

The ten-year arc (companyfacts, screening only; the FY2024-FY2026 rows above were re-read in the 10-K): revenue **$5,010M (FY2016) →
$26,914M (FY2022) → $26,974M (FY2023) → $215,938M (FY2026)**; gross margin 56.1% → 64.9% → 56.9% → 71.1%; operating margin 14.9% → 37.3%
→ **15.7%** → 60.4% (`facts_out.md`). **FY2023 is the filed down-year: revenue flat, operating margin cut from 37.3% to 15.7%.**

- **Unit economics in my own words, no management language:**
  1. NVIDIA designs the processors that train and run AI models (and graphics chips for PCs), plus the switches, network cards, CPUs
     and the software that make thousands of them work as one machine. **It owns no chip factory**: TSMC and Samsung make the wafers,
     SK Hynix, Micron and Samsung supply the memory, and Hon Hai, Wistron and Fabrinet assemble (10-K Item 1, *"Manufacturing"*).
  2. It sells these mostly as complete rack systems and boards to server makers, to the big cloud companies and, increasingly, to AI
     model makers and smaller "AI clouds", who rent the capacity on. **It keeps about three dollars of every four as gross profit and
     about two of every three as operating profit**, because the cost of making a unit is small beside what a customer will pay for the
     computing it delivers, and because R&D (8.6% of FY2026 revenue) is spread across a revenue base that grew 3.5x in two years.
  3. **The plant is small and the working capital is large.** Net property and equipment is $14.3bn against TTM revenue of $303.0bn.
     The capital that the business actually ties up sits in receivables ($63.1bn, with *"longer payment terms ranging from 90 days up
     to one year"* for large investment-grade customers), inventory ($31.6bn), **supply and capacity commitments of $279bn** (up from $119bn
     one quarter earlier), and a new layer described below: equity stakes in customers, cloud-capacity buy-back commitments and lease
     guarantees.
  4. **Who pays:** one direct customer was 22% and another 14% of FY2026 revenue; in H1 FY2027 three direct customers were 16%, 15% and
     13%. The indirect buyers are the cloud companies and model makers, and *"one AI research and deployment company contributed a meaningful
     amount of our revenue by purchasing cloud services from our customers"* (10-Q MD&A).
- **The scarce input this business controls:** (a) **the software and developer base** that runs on its chips (*"over 7.5 million
  developers worldwide using CUDA and our other software tools"*, 10-K Item 1), which makes a rival chip cost more to adopt than its
  sticker price; (b) **the co-designed system** (GPU, CPU, NVLink interconnect, networking, software) sold as one rack, which no single
  rival files as selling whole; (c) **secured supply** at the bottleneck: leading-edge wafers, advanced packaging and high-bandwidth
  memory, bought forward under $279bn of commitments. (a) and (b) are ownable; (c) is bought with cash each cycle.
- **Will the fundamentals look broadly the same in ten years?**
  - *The mechanism* (design, outsource manufacture, sell accelerated computing with a software layer): **broadly yes**; it is the same
    mechanism the FY2017 10-K describes for GPUs, and graphics has run on it for thirty years.
  - *What is sold, to whom, at what price and against whom*: **it is changing now, by the filer's own account.** 10-K FY2026 Item 1: *"The
    market for our products is intensely competitive and is characterized by rapid technological change and evolving industry
    standards"*; MD&A: *"bringing new advanced architectures on a one-year product cadence"*; three of its named competitors are its own
    largest customers (*"large cloud services companies with internal teams designing hardware and software ... such as Alibaba Group,
    Alphabet Inc., Amazon, Inc., ... Baidu, Inc., Huawei, and Microsoft Corporation"*). [E3-31] asks for businesses *"relatively simple and
    stable in character"*. **The mechanism is understandable; its stability is the question [E4-04] asks at Q2** (*"industries prone to rapid
    and continuous change"*), and it is carried there by name, as the TSM, INTC and AMZN runs carried it, not assumed away here.

### EQUITY STAKES, CAPACITY BUY-BACKS AND GUARANTEES — carried separately and kept OUT of owner earnings
All from the 10-Q `0001045810-26-000075` unless stated.
| item | 2026-01-25 | 2026-07-26 | how it reaches the statements |
|---|---|---|---|
| Publicly-held equity securities (current, Level 1 + 2) | 12,886 | **42,783** ($36.9bn under *"short-term lock-up restrictions"*) | fair value through Other income |
| Publicly-held equity, long-term, locked up *"through December 2027"* (in Other assets) | 4,840 | 4,957 | fair value through Other income |
| Non-marketable equity securities (measurement alternative) | 22,251 | **47,898** (plus $3.3bn equity-method *"investments in infrastructure financiers"*) | *"Unrealized gains"* $7,504M H1 FY27; reclassification of $12,712M to marketable *"following public market trading"* |
| Equity investment commitments outstanding | $11.4bn (10-K) | **$25bn** | — |
| MD&A total: *"equity investments of $99 billion and equity investment commitments of $25 billion as of July 26, 2026"* | | | *"Gains from equity securities, net"* **$23,707M in H1 FY27** (removed inside OCF) |
| Cloud service agreements (NVIDIA buys capacity) | $27bn (10-K) | **$29bn** | operating cost as used |
| **AI cloud agreements** (partners buy NVIDIA systems; NVIDIA commits to buy the capacity back) | — | **$36bn**, *"typically six years"* | operating cost as used |
| Data center leases not commenced, own use / for third parties | — | $25bn / **$20bn** (*"We expect to reassign these data center leases to third parties"*) | leases on commencement |
| Land, power and shell guarantees for AI clouds | $3.5bn | $3.5bn (partners' escrow $712M) | credit derivatives, fair value not significant |
| **SB Energy guarantees for OpenAI's leases** | — | **$105.0bn cap** (first phase expected FY2029) | not yet effective |

- **What the filings say about the named stakes (priors tested):** the Q3 FY2026 10-Q (`0001045810-25-000230`) reads *"Investment commitments
  are $ 6.5 billion as of October 26, 2025, including $ 5 billion in Intel Corporation which is subject to regulatory approval. In the third
  quarter of fiscal year 2026, we entered into a letter of intent with an opportunity to invest in OpenAI. In November 2025, we entered into
  an agreement, subject to certain closing conditions, to invest up to $ 10 billion in Anthropic."* The FY2026 10-K: *"gains from our
  previously announced investment in Intel's common stock"* and *"We are finalizing an investment and partnership agreement with OpenAI.
  There is no assurance ..."*. **Confirmed from filings: $5bn in Intel stock; up to $10bn in Anthropic; an OpenAI letter of intent.
  NOT found in any filing on disk: the "$100bn" OpenAI figure** (no amount is filed for the OpenAI opportunity), **a Nokia stake** (the
  releases describe a partnership only), **and a CoreWeave stake by name** (the releases name CoreWeave as a partner; the 10-Q names no
  investee). The 10-Q does not itemise the $99bn.
- **Groq, confirmed and larger than the prior implied:** 10-K Note 2: *"In December 2025, we entered into a non‑exclusive license agreement
  with Groq, Inc., or Groq, for its language processing unit technology and hired certain Groq employees. No customer contracts, existing
  products, or equity interests were purchased. We recorded $ 14.4 billion of goodwill and a $ 2.5 billion developed technology intangible
  asset ... Total consideration consists of $ 13.0 billion paid at closing and $ 4 billion, inclusive of imputed interest, payable within one
  year"*. **About $17bn for a licence to a rival inference-chip design and its engineers**; the Q2 FY27 release: *"NVIDIA Groq 3 LPX, the
  interactive AI inference accelerator, is now in full production."* Carried to Q2 (what it says about substitutes) and Q3 (allocation).
- **Why they are kept out of owner earnings:** the gains are non-cash marks removed inside operating cash flow by the filing itself
  (*"Gains from equity securities, net | ( 23,707 )"*, H1 FY27). **H1 FY2027 net income of $118,010M includes $24,140M of Other income**, which
  is why operator rule 5 forbids a net-income proxy. No look-through earnings are added [E3-04]: no investee's undistributed earnings are
  evidenced, and the equity-method income is *"not significant"*.
- **The same counterparties are customers**, which is why this table is carried to Q2 and Q4: Anthropic *"will run and scale on NVIDIA
  infrastructure, initially adopting 1 gigawatt"* (Q3 FY26 release) in the quarter NVIDIA agreed to invest up to $10bn in it; OpenAI
  *"to deploy at least 10 gigawatts of NVIDIA systems"* (same release) and is the tenant NVIDIA guarantees up to $105bn for.

### PERIMETER EVENTS INSIDE THE WINDOWS (priors tested)
- **Mellanox:** *"In April 2020, we completed the acquisition of all outstanding shares of Mellanox for a total purchase consideration of
  $ 7.13 billion"* (10-K FY2021, `0001045810-21-000010`); cash-flow line *"Acquisitions, net of cash acquired | ( 8,524 )"* in FY2021. **Inside
  FY2021**, so every window that includes FY2021 or earlier crosses it; the five-year default (FY2022-FY2026) does not.
- **Arm (terminated):** 8-K 2022-02-08: *"the Sellers will retain the $1.25 billion prepaid by the Company"*; 10-K FY2023: *"We recorded an
  acquisition termination cost of $1.35 billion in fiscal year 2023 reflecting the write-off of the prepayment provided at signing."* The
  cash left in FY2021 (the prepayment); the charge was non-cash in FY2023 (*"Acquisition termination cost | 1,353"* added back). **Not a
  perimeter change**: nothing was acquired.
- **Groq (FY2026, ~$17bn)** is accounted for as a business combination (goodwill) and its cash sits in investing (*"Groq, Inc. | ( 13,000
  )"*) and financing (*"Groq, Inc. | ( 2,944 )"*, H1 FY27). **Hugging Face ($11.9bn)** is pending. Both carried to Q4's (c) judgment.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  How the money is made is legible from the filings and statable without management's words, and it passes the five-minute test
  [E4-46]: a fabless designer selling complete AI computers and their software at three-quarters gross margin, with its capital in
  working capital and forward supply rather than plant. **What is not simple and stable is the product basis, and the framework locates
  that test at Q2 [E4-04]**, so it is carried by name, not used to fail Q1 and not used to excuse Q2. No "unverified" or "provisional"
  caveat attaches: the unitemised $99bn of stakes is disclosed in total and is kept out of owner earnings, and understanding how the
  business makes money does not require the list.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no close
> substitute and; (3) is not subject to price regulation."* — **[E3-03]**; *"The existence of all three conditions will be demonstrated by a
> company's ability to regularly price its product or service aggressively and thereby to earn high rates of return on capital."* — **[E3-43]**

**Where the weight is:** Compute & Networking is **94.2% of segment operating income** in FY2026 (130,141 of 139,297) and 94.2% in H1 FY2027
(116,031 of 122,871); Data Center is 92.4% of H1 FY2027 revenue. Graphics is recorded (below) and does not carry the verdict. The test is
run on the data-center accelerator business, which is the company.

### THE THREE CONDITIONS, AND THE RETURN TEST
- **(1) Needed or desired: [x] YES.** TTM revenue $303.0bn; Data Center +117% year on year in Q2 FY2027; *"we are currently experiencing
  certain supply constraints"* (10-Q MD&A).
- **(3) Not subject to price regulation: [x] YES as to price; with a regime that sets WHERE it may sell.** No filed price regulation. But the
  export-licence regime decides which products may be sold to whom, and a licence carried an economic condition: *"USG officials expressed an
  expectation that the USG will receive 15% or more of the revenue generated from licensed sales of our products"* (10-K FY2026 Item 1), and the
  H200 route carries a 25% tariff *"We have been unable to pass along"*. China's regulator has a *"preliminary finding"* (published 2025-09-15)
  that NVIDIA's export compliance *"violated the terms of China's approval of our Mellanox acquisition"* (10-Q Part II Item 1A). **[E2-59]**:
  where a regime reaches the terms of sale, part of the economics belongs to the regime. Recorded; not the decisive test.
- **[E3-43]/[E3-46] high returns on capital: [x] YES, extraordinarily.** Operating income $130.4bn (FY2026) on net plant of $10.4bn; net
  income ÷ average equity 91.5% (FY2024), 119.2% (FY2025), 101.5% (FY2026) (`facts_out.md`, re-read against the 10-K income statement and
  balance sheet for FY2026). On any denominator this is the highest return in any semiconductor row this queue has built.
- **(2) Thought by its customers to have no close substitute: [ ] NO, on the customers' and the rivals' own filings.** This is the decisive
  condition, and it is tested on what the largest customers are filed as DOING, not on what NVIDIA says (full text and accessions in
  `peers/competitor_row.md`, Table B):
  1. **The largest AI laboratories have contracted substitutes at gigawatt scale.** Amazon's Q1 2026 release: OpenAI committed to *"approximately
     two gigawatts (GW) of Trainium capacity"*; Anthropic *"will secure up to five gigawatts (GW) of current and future generations of Amazon's
     Trainium chips"*. **These are the same two laboratories NVIDIA agreed to invest in (Anthropic, up to $10bn), signed a letter of intent with
     (OpenAI), and now guarantees up to $105bn of leases for (OpenAI).** AMD issued OpenAI and Meta warrants for up to 160 million shares each,
     vesting *"based on specified AMD Instinct GPU purchase milestones"*.
  2. **A custom-accelerator supplier has filed a pipeline of comparable size.** Broadcom (10-Q filed 2026-09-10): *"more than 20 gigawatts in
     compute capacity using our custom AI accelerators or XPUs ... customized for the leading frontier AI labs through 2028"*; its
     semiconductor segment grew **+127%** in its latest quarter at a **61.3%** segment margin. Against that, NVIDIA's disclosed laboratory
     deployments are OpenAI *"at least 10 gigawatts"* and Anthropic *"initially adopting 1 gigawatt"* (Q3 FY2026 release).
  3. **A customer NVIDIA names as a competitor now sells its accelerator to others.** Alphabet, Q2 2026 10-Q: *"in the second quarter of 2026,
     we began recognizing revenue from the sale of TPU systems."*
  4. **NVIDIA's own filing concedes it:** *"Some of our customers have in-house expertise and internal development capabilities similar to some
     of ours and can use or develop their own solutions to replace those we are providing"*; rivals' products *"may be cheaper or provide better
     functionality or features than ours, which has resulted and may in the future result in lower-than-expected selling prices or demand for our
     products"* (10-K FY2026, Item 1A). **"Has resulted" is a statement of fact about the past, not a hypothetical.**
  5. **NVIDIA paid for a substitute rather than let a rival own it.** About **$17bn** for *"a non‑exclusive license agreement with Groq, Inc., or
     Groq, for its language processing unit technology"* and its engineers, booked as $14.4bn of goodwill (10-K Note 2); within two quarters,
     *"NVIDIA Groq 3 LPX, the interactive AI inference accelerator, is now in full production"* (Q2 FY2027 release). **A franchise whose customers
     had no close substitute would not need to buy the licence to one.**
  6. **Where a regime removed NVIDIA, substitutes filled the space at once, in NVIDIA's words:** *"our effective foreclosure from the China market
     helped our competitors build larger developer and customer ecosystems to challenge us worldwide"* (10-Q Q2 FY2027). **The software ecosystem
     that is the strongest part of the franchise case is described by its owner as buildable by rivals when they are given room.**

**The pricing test [E3-03]'s own sentence names, [E2-44](1) and [E4-37]:**
- **For the present:** gross margin 72.4% → 73.4% → 75.0% → 74.9% → 75.0% (Q2 FY2026 to Q2 FY2027) and guided 74.0% for Q3 FY2027. **Price is
  holding margin through a new-architecture ramp, which is the strongest evidence FOR the franchise, and it is stated at full strength.**
- **No price, unit or ASP series is filed** ("unit shipments" 0, "price increase" 0 in the 10-Ks FY2023-FY2026 and the Q2 FY2027 10-Q), so
  [E4-55]'s physical series cannot be run.
- **The filed record of price conduct in a soft year runs the wrong way for [E2-44](1)** (*"an ability to increase prices rather easily (even when
  product demand is flat"*): FY2023, revenue flat at $26,974M: *"We introduced pricing programs for our channel partners and started undershipping
  GPU supply"*; 10-K FY2023 and FY2024: *"we have experienced a reduction in average selling prices, including due to channel pricing programs ...
  as a result of our overestimation of future demand"*, and prices were raised only *"as a result of our suppliers' increase in prices"*. Operating
  margin fell from 37.3% (FY2022) to 15.7% (FY2023). **In the one flat-demand year on file, NVIDIA cut prices and its margin more than halved.**
- **Today's demand is partly financed by the seller, which is [E4-37]'s agony in a new form.** The 10-Q says the buyers *"currently lack the
  ability to secure long-term infrastructure contracts and investment-grade financing capacity"*, and NVIDIA supplies it: $99bn of equity
  stakes, *"AI cloud agreements"* under which *"AI clouds procure our data center infrastructure products and we commit to cloud service
  agreements"* ($36bn), $20bn of leases taken to reassign, $3.5bn of partner lease guarantees, the $105bn SB Energy cap, *"longer payment
  terms ranging from 90 days up to one year"*, and a proposed *"more than $500 billion"* financing platform. **A seller whose customers think it
  has no substitute does not need to lend them the price.** Broadcom is doing the same for its custom accelerators ($29bn backstop), which is
  **[E2-27]**'s picture of a race, not a toll.

### [E4-04] — must the moat be continuously rebuilt? **YES, on the filer's own words, cadence and write-offs.**
**The full ledger row:** *"Our criterion of 'enduring' causes us to rule out companies in industries prone to rapid and continuous change. Though
capitalism's 'creative destruction' is highly beneficial for society, it precludes investment certainty. A moat that must be continuously rebuilt
will eventually be no moat at all."* — **[E4-04]**
- **The filer's description of its industry:** *"The market for our products is intensely competitive and is characterized by rapid technological
  change and evolving industry standards"* (10-K FY2026 Item 1); *"bringing new advanced architectures on a one-year product cadence"* (MD&A).
- **Does the spending defend the same advantage, or buy its replacement? It buys the replacement, every year.** The premium is earned on the
  current architecture's performance per dollar: Blackwell Ultra *"delivers up to 50x better performance and 35x lower cost for agentic AI compared
  with the NVIDIA Hopper platform"* (Q4 FY2026 release); Rubin *"up to a 10x reduction in cost per token compared to Blackwell"* (10-K). Customers
  pay for the step; the step must be re-won by the next architecture against Broadcom's XPUs, Google's TPUs, Amazon's Trainium and AMD's Instinct.
  **The old architecture's value collapses on the new one's arrival**, and the filings quantify it: inventory and purchase-obligation provisions
  **$2.17bn (FY2023), $3.7bn (FY2025), $7.2bn (FY2026)**, including the **$4.5bn H20** charge *"as the demand for H20 products diminished"* and
  $0.4bn more on H200 in H1 FY2027; *"We have experienced and may in the future experience reduced demand for current generation architectures
  when customers anticipate transitions"* (10-K FY2023).
- **What carries across generations is real, and it is the franchise case's best asset:** CUDA and its 7.5 million developers, NVLink, the
  networking business (Data Center networking $31.4bn, +142%, FY2026), the supply relationships. **Those defend the ability to sell the next
  architecture; they are not what the customer pays the premium for**, and the filer itself says in the China passage that a rival ecosystem
  grows when the architecture is absent. *"certainly should be working at improving your own moat and defending your own moat all of the time"*
  **[E5-23]** is prescribed for every moat; the framework's line is whether the thing defended or the thing replaced earns the return.
- **Does a lapse destroy the structure, or merely narrow it? The two filed lapses answer "sharply narrow, and in one case, exit".** (a) FY2023:
  demand paused, prices were cut, $2.17bn was provisioned, and operating margin went **37.3% → 15.7%** in one year. (b) Mobile: the FY2017 10-K
  records *"the wind-down of Icera modem operations"*, NVIDIA's exit from a processor race it had entered. Neither is a death; both show that
  position in this industry is re-won, not held.
- **[E3-51] and [E4-36]:** the record since FY2023 is a **surfing run** on the AI wave, and a superb one: of the four causes of extreme success
  it draws on the second (*"a nonlinear combination"* of chip, system, network and software, which is ownable) and the fourth (wave-riding,
  which is not). *"If he gets off the wave, he becomes mired in shallows"* is FY2023 in one sentence. **Revenue 8.0x in three years is the
  wave's height, not the moat's width.**
- **[E4-23] key-person dependence:** the founder has been CEO since 1993; the 10-K lists *"We may be unable to attract, retain, and motivate our
  executives and key employees"* among risks and names no individual dependence. Not recorded as a moat defect on the filed text.

### THE COMPETITOR ROW — required **[E3-28]** *(CONVENTION, confessed at VI)*
Full row, accessions and sweeps: `Test Runs/_research 2026-09-13 NVDA/peers/competitor_row.md`. Arithmetic ratios.

| company | accelerator-bearing segment | latest FY revenue growth | latest FY segment margin | latest interim growth | latest interim margin | source |
|---|---|---|---|---|---|---|
| **NVIDIA** | **Compute & Networking** | **+66.5%** (FY Jan-2026, $193.5bn) | **67.3%** | **+101.2%** (H1 FY27, $162.9bn) | **71.2%** | 10-K `0001045810-26-000021`; 10-Q `0001045810-26-000075` |
| Broadcom | Semiconductor solutions | +22.5% (FY Nov-2025, $36.9bn) | 57.6% | +87.6% (9M FY26, $48.4bn); +127% Q3 | 61.1%; 61.3% Q3 | 10-K `0001730168-25-000121`; 10-Q `0001730168-26-000080` |
| AMD | Data Center | +32.2% (FY2025, $16.6bn) | 21.7% | +81% (H1 2026, $12.5bn) | 29.6% | 10-K `0000002488-26-000018`; 10-Q `0000002488-26-000123` |
| Intel | DCAI | +4.9% (FY2025, $16.9bn) | 20.2% | +40.3% (H1 2026, $11.3bn) | 35.5% | 10-K `0000050863-26-000011`; 10-Q `0000050863-26-000157` |
| Marvell | Data center end market | +46.5% (FY Jan-2026, $6.1bn) | 16.1% (company; no segment OI) | +36.6% (H1 FY27, $4.0bn) | not filed | 10-K `0001835632-26-000011`; 10-Q `0001835632-26-000025` |
| Alphabet (TPU) | inside Google Cloud | *"began recognizing revenue from the sale of TPU systems"* (Q2 2026) | not filed | amount not stated | — | 10-Q `0001652044-26-000071` |
| Amazon (Trainium) | inside AWS | OpenAI ~2 GW, Anthropic up to 5 GW committed | not filed | — | — | 8-K EX-99.1 `0001018724-26-000012` |

- **Peers named: 5 filed accelerator rivals with segment figures plus 2 customer-builders with filed commitments**, of roughly ten real competitors
  NVIDIA's 10-K names. **Not rowed, and stated:** Huawei (not an SEC filer; no figure guessed), Groq (private, now licensed by NVIDIA), Microsoft's
  in-house chips (0 hits for "Maia", "Cobalt" or "custom silicon" in the FY2026 10-K text searched), Chinese accelerator makers, Cerebras. **None is
  load-bearing**: the verdict rests on NVIDIA's own filings and the filed commitments of its largest customers. **Not PROVISIONAL.**
- **What the row shows:** **NVIDIA leads the row on nearly every filed measure of position**: the fastest segment growth on the tabulated interim
  windows (though Broadcom's latest quarter, +127%, outgrew NVIDIA's latest quarter, +114%), the highest segment margin in both periods, and 2.2x the four filed rivals' combined accelerator-segment revenue in their latest interims. **The row does not
  show a franchise; it shows the leader of a race in which the second-best margin (Broadcom's 61%) belongs to the supplier of the customers' own
  substitutes, and in which every rival's interim growth is 37-88%.**
- **The row's limit [E3-61]:** position, not conduct. Whether the hyperscalers and laboratories will keep dividing their purchases, or behave like
  *"a demented Kellogg"* once their own chips mature, no filing can say.
- **Untapped pricing power [E3-33]: not claimable.** A 75% gross margin is tapped pricing, not untapped; the licensed China sale could not pass on
  a tariff; and **[E5-28]** (near-monopoly) is contradicted by the gigawatt-scale substitute commitments above.
- **[E2-53] dominance class:** the position is dominant, but its economics are re-set each architecture by the race, not by the position ("good or
  bad, it will prosper" is not what FY2023 shows).
- **[E2-45] the attacker's test** is not hypothetical here: it is being run by five filed attackers at once, three of them NVIDIA's own customers,
  with capital from the laboratories' investors and, in Broadcom's case, backstops of the same kind NVIDIA writes.
- **Graphics (5.8% of segment operating income):** GeForce and workstation GPUs, 40.8% segment margin FY2026; the record of FY2023 channel
  price programs applies to it; it does not carry the verdict.

### What the franchise case rests on, stated at full strength [E4-26, E4-51]
*"NVIDIA is the toll on AI. Every cloud and every laboratory runs on it; it grew its accelerator segment 101% in six months at a 71% margin, faster
and more profitably than anyone in the row; gross margin went UP through the Blackwell transition; the software base of 7.5 million developers is a
switching cost no custom chip has; the customers who build their own chips still buy NVIDIA by the gigawatt; and it has a new architecture every year
that cuts the customer's cost per token by an order of magnitude, which is why they keep coming back. The custom chips are niche workloads; Groq was
bought cheaply to close a gap. Ruling this out is the omission error the corpus rates most expensive."*
**The answer, on the filed record:** (1) every clause about position is granted and is in the row (with one exception: Broadcom's latest quarter grew faster); (2) the premium is earned on an architecture that
is replaced each year, the filer says its industry is one of *"rapid technological change"*, and each replacement leaves provisions of $2-7bn a
year behind it; (3) the customers' own filings show substitutes contracted at gigawatt scale by the two laboratories NVIDIA is financing, a supplier
filing 20+ GW of custom accelerators, and a customer selling its own accelerators to others; (4) NVIDIA itself paid ~$17bn to license a rival
architecture; (5) in the one flat year on file, prices were cut and margin more than halved; (6) demand is now supported by $99bn of customer equity,
buy-back commitments and guarantees of up to $108.5bn, which a toll does not need. **The strongest case describes the best-positioned surfer in the
industry; [E4-04] rules out the industry for the certainty it precludes, not for the leader's current numbers.** The omission cost of a wrong close
**[E3-47]** is acknowledged; the reopening conditions at Q6 are written to catch it.

### THE TSMC TENSION, FLAGGED AND NOT RESOLVED (the TSM run's open operator question)
[E4-04] is live at NVIDIA, as it was at TSMC. The TSM run (`Test Runs/2026-09-13 Run - TSM Taiwan Semiconductor.md`, Q2 and self-audit item 5)
recorded that **the corpus authors bought TSMC in 2022 and left for location, not franchise, reasons**, while the framework's [E4-04] scope excludes
leading-edge semiconductors. NVIDIA is TSMC's customer in the same industry and the same wave. **This run applies [E4-04] as the framework scopes it,
exactly as the TSM, INTC and AVGO (AI half) runs did, and carries the tension to the operator unresolved. A corpus sweep for NVIDIA itself (nine
source folders, case-insensitive) found no instance of the corpus naming the company.** Changing how [E4-04] scopes the class would be a structural
change requiring a written case (prime rule 5); this run does not make it.

- **Class: [ ] WIDE [ ] NARROW [ ] NONE [ ] PROVISIONAL → POSITION DOMINANT, franchise class NONE under [E4-04] (a surfing run [E3-51])** — the TSM
  run's wording, used for the same finding. **Direction of the position [E4-32]: widening on every filed margin and growth figure**; direction of the
  substitutes: growing at 37-127% with committed gigawatts behind them.
- **Can I name the document that would resolve it?** The documents that decide criterion (2) and [E4-04] exist and were read: NVIDIA's 10-K and 10-Q
  and the rivals' and customers' filings. **So the verdict is not UNRESEARCHED; and it is not UNKNOWABLE, because the evidence is in and it answers
  the question the framework asks.**
- **VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *OUT on [E4-04], with [E3-03] criterion (2) as the customers' filings test it. NVIDIA passes criteria (1) and (3) and [E3-43]'s return test at a
  level no row in this queue has shown; it fails [E4-04] on its own description of its industry, its one-year cadence and the provisions each
  replacement leaves, and it fails criterion (2) because its largest customers have contracted substitutes at gigawatt scale, a rival files 20+ GW
  of custom accelerators, a customer sells its own, and NVIDIA paid ~$17bn for a licence to one. The ten-year record is a surfing run at its best.
  Not a finding that NVIDIA is a poor business. **The file closes here.** Q3-Q6 below are RECORDED, NOT GOVERNING.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

*Resumed 2026-09-13 by a fresh session after the first was killed at a session limit; Step 0, Q1 and Q2 are the killed session's, read whole and not re-derived. Working: `q3calc.py` / `q3calc_out.txt`; the SEC order `SEC_order_33-11060.txt` (`sec_order.py`); the FY2023 guidance record `8K_2022-*` and `8K_2023-02-22` (`fetch_fy23.py`), all in the research folder.*

**What the killed session's last three fetches were for (opened, not assumed).** `SEC_press_2022-79.txt` is the SEC's release of 2022-05-06 charging NVIDIA over its FY2018 cryptomining disclosures (the honesty matter below). `10Q_FY23Q1.txt` (quarter ended 2022-05-01, `0001045810-22-000079`) carries the company's own disclosure of that settlement. `10Q_FY26Q2.txt` (quarter ended 2025-07-27, `0001045810-25-000209`) carries the H1 FY2026 comparatives and the only interim cash-tax line on disk (*"Cash paid for income taxes, net | $ | 8,451"*), which the Q2 FY2027 10-Q does not print; that is the most likely purpose, and it is the use made of it here. The killed session left no note saying so.

**STEP 1: DECLARE THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution [E3-38]**, through its 1991 original: *"a business, unlike a franchise, can be killed by poor management"* **[E3-43]**. Q2 found a
  dominant position in a race, not a franchise, so the original governs. The decisions that decide a year are made every quarter: supply and capacity
  commitments raised **from $119bn to $279bn in one quarter** (10-Q Note 10), what to build for which architecture, whom to finance, and which export
  regime a product will meet. The filed cost of one such decision going wrong is on record: $2.17bn of provisions in FY2023 and the $4.5bn H20 charge
  in Q1 FY2026.
- [ ] **Control [E1-16]: not ticked.** A listed minority position; single class (Step 0); Mr. Huang holds **3.58%** (DEF 14A 2026, `0001045810-26-000036`,
  as of 2026-03-23).
- [ ] **Leverage [E3-29]: not ticked, argued both ways.** *For ticking:* the contingent layer is large and new. Commitments of **$366bn** (Note 10 first
  table), additional commitments of **$56bn** (AI cloud agreements and third-party leases) and guarantees capped at **$108.5bn** sum to **$530.5bn, 2.3x
  shareholders' equity of $228,984M**; and **43.2% of that equity is the carrying value of stakes** in companies that are also customers (`q3calc_out.txt`).
  One demand pause would hit the commitments, the stakes, the receivables ($63.1bn on terms *"up to one year"*) and the guarantees together, so the
  errors are correlated, which is what makes leverage dangerous. *Against:* [E3-29]'s mechanism, in its own words, is that *"leverage of 20:1 magnifies the effects of
  managerial strengths and weaknesses"* (the framework's gloss: small asset errors destroy equity). Recognised liabilities are **$91,288M against equity of $228,984M (0.4:1)**; debt of $33,366M sits beside cash and
  debt securities of $56,586M; most of the $279bn is a purchase of inventory that the 10-Q says is *"in certain instances ... cancelable, rescheduled, or
  adjustable"*, and the guarantees are not yet effective (first SB Energy phase expected FY2029). A FY2023-sized error at today's exposure is quantified at
  Q4 (~$58bn) and is about a quarter of equity, not all of it. **Not ticked; recorded as the determinant most likely to tick if the commitments keep
  growing at this quarter's rate.** The weight case does not turn on it, because daily execution already makes Q3 a gate.
- **Case declared: Q3 is a BINARY GATE, on daily execution.** *(Recorded, not governing.)*

**Honesty: binary, permanent, filings-based [E5-16].** *Each matter dated to when it became public.*
1. **The SEC cease-and-desist order, public 2022-05-06** (Securities Act Release No. 11060, Exchange Act Release No. 94859, File No. 3-20844; order text
   `SEC_order_33-11060.txt`, fetched from sec.gov at the resume). **The conduct:** the Forms 10-Q for Q2 and Q3 FY2018, *"filed ... on August 23, 2017 and
   November 21, 2017"*. **The finding:** *"NVIDIA had information indicating that cryptomining was a significant factor in the year-over-year growth in
   revenue from the sale of GPUs that NVIDIA designed and marketed for gaming. The company, however, did not disclose this"*; Gaming revenue rose *"by 52%,
   year over year for the second fiscal quarter 2018, and by 25% ... for the third"*; the omission, beside disclosure of crypto sales in OEM, *"gave the
   misimpression ... that the year-over-year growth in the company's Gaming revenue was not meaningfully impacted by cryptomining"*; and *"NVIDIA's senior
   management internally expressed a desire to capture the cryptomining demand"*. **Its legal basis and limits, in the order's words:** Sections 17(a)(2)
   and (3), *"A violation of these provisions does not require scienter and may rest on a finding of negligence"*; plus disclosure controls under Rule
   13a-15(a); *"without admitting or denying the findings"*; a **$5,500,000** penalty; **the respondent is the company and no individual is charged.** **The
   correction:** *"The company's periodic reports did not identify cryptomining as a significant factor in year-over-year growth in Gaming revenue until ...
   its Form 10-K for fiscal year 2018 (filed on February 28, 2018)"*, one quarter after the second omission. The company's own disclosure of the settlement:
   10-Q Q1 FY2023 (`0001045810-22-000079`): *"NVIDIA entered into a settlement with the SEC relating to MD&A disclosures in our Forms 10-Q for the second and
   third quarters of fiscal year 2018 concerning the impact of cryptocurrency mining"*. **The same CEO (founder, CEO since 1993) and CFO (Ms. Kress, since
   2013, 10-K FY2019) signed then and sign now.**
   **Read against the corpus.** [E5-22] (penalty size is not seriousness, in the framework's summary of it), so $5.5M is not read as small; the test is whether they acted when they learned,
   and the filed record is that the next annual report named cryptomining as a significant factor, and that in the second crypto wave the FY2022 10-K
   reported *"CMP revenue was $550 million for the fiscal year"* separately and shipped LHR cards, while still saying *"we have limited visibility into how
   much this impacts our overall GPU demand"*. [E2-68]: disclosure where the company holds the information advantage is the sharpest read, **and in 2017 this
   company failed it**: the SEC's finding is exactly that the company knew more than the 10-Q said. [E5-16] refuses **personal misconduct**; the order finds a
   corporate disclosure failure on a standard that needs no intent, names no person, and was corrected within a quarter. **Not a disqualifier on the record
   read. It is the most serious candour fact in this file and is carried at [E2-26] below, dated 2017 (conduct) and 2022 (public).**
2. **The securities class action, In re NVIDIA Corporation Securities Litigation, 4:18-cv-07669-HSG, filed 2018-12-21** (10-Q Q2 FY2027 Note 10): alleged
   *"materially false or misleading statements related to channel inventory and the impact of cryptocurrency mining on GPU demand between May 10, 2017 and
   November 14, 2018"*, a longer window than the SEC's; dismissed 2021-03-02; reversed in part by the Ninth Circuit 2023-08-25; the Supreme Court dismissed
   NVIDIA's writ *"as improvidently granted on December 11, 2024"*; **on March 25, 2026 the district court certified a class** of purchasers from
   2017-08-10 to 2018-11-15. Four derivative suits on the same facts are stayed. *"there are no accrued contingent liabilities ... liabilities, while
   reasonably possible, are not probable"*. **Open allegations of knowing falsity against executives; not a finding. A judgment of scienter against a named
   officer would be a [E5-16] matter, and is written into Q6.**
3. **China's antitrust regulator, preliminary finding published 2025-09-15** (10-Q Part II Item 1A): that compliance *"with applicable U.S. export controls
   ... violated the terms of China's approval of our Mellanox acquisition"*. A dispute over obeying the home government's export law; not dishonesty toward
   owners. **Open; recorded at Q2 as a regime reach [E2-59] and at Q4 as an exposure.**
4. **Competition inquiries** (EU, US, UK, China, South Korea requests for information; the French Competition Authority on whether gaming and data-center
   GPUs are separate categories): inquiries, no finding. **Open.**
5. **Related parties** (DEF 14A 2026): *"The total compensation for Fiscal 2026 of the daughter and son of Mr. Huang was approximately $1,232,000 and
   $1,320,000"*, set *"without the involvement of Mr. Huang"*. Disclosed with amounts; not a flag. Hedging and pledging of NVIDIA stock are prohibited.
- **No finding of personal misconduct by a named officer or director in any document read** (10-Ks FY2017, FY2019, FY2021-FY2026; 10-Qs FY23Q1, FY26Q1-Q3,
  FY27Q1-Q2; DEF 14A 2026; thirteen releases; the SEC order). Written as the absence of found disqualifiers, not a finding that the managers are honest
  **[E5-17]**, and the 2017 matter shows why: the filing read at the time looked clean.

**STEP 2: THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to READ, never a verdict. Thirteen EX-99.1 releases were read before scoring (six
from 2025-05-28 to 2026-08-26 on disk from the killed session; six from the FY2023 down-year, fetched at the resume; and the SB Energy release).*
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]: NOT FIRED, and the direction since FY2027 is the inverse.** "EBITDA" appears **0 times** in every
  release on disk. Non-GAAP measures are in every release, presented in a GAAP table first and a non-GAAP table second. **Until FY2026 the non-GAAP
  measures excluded stock-based compensation** ([E5-06]: *"even more cavalier"*); **the Q4 FY2026 release announced the end of that a quarter ahead, with a
  reason**: *"Beginning in the first quarter of fiscal year 2027, NVIDIA will include stock-based compensation expense in non-GAAP financial measures.
  Stock-based compensation is a foundational component of NVIDIA's compensation program"*, and recast history. Today's non-GAAP net income is **below**
  GAAP because it strips the equity marks: **$45,548M against $58,321M (Q1 FY2027) and $53,954M against $59,688M (Q2 FY2027)**. A switch made at record
  results, announced ahead, toward the stricter number is [E2-69]'s direction toward candour, and the reverse of [E2-49]'s form.
- [x] **The except-for prompt [E2-57] and the restructuring charge [E3-53, E5-33]: FIRES as a prompt; read; passes on disclosure, fails on frequency.**
  Q1 FY2026: *"Excluding the $4.5 billion charge, first quarter non-GAAP gross margin would have been 71.3%"*, with an "as adjusted" EPS line. **Against the
  flag:** GAAP is stated first; the favourable reversal the next quarter was stripped too (*"Excluding the $180 million release, non-GAAP gross margin for
  the quarter would have been 72.3%"*), so both innings were counted. **For it:** provisions for inventory and purchase obligations are filed every year,
  **$354M (FY2022), $2.17bn (FY2023), $2.2bn (FY2024), $3.7bn (FY2025), $7.2bn (FY2026), $2.1bn (H1 FY2027)** (MD&A of each 10-K and the 10-Q), including
  $0.4bn more on H200. A charge that recurs with every architecture and regime change is the cost of this business, and an "excluding" figure invites
  treating it as one-time. **Kept inside the owner-earnings mean** (the cash is inside OCF; Q4).
- [x] **Trumpeted projections [E4-22, third]: FIRES as a prompt; the record is checked [E3-48], across a down-year and a boom.** NVIDIA guides one quarter
  ahead, revenue *"plus or minus 2%"*:
  | quarter | revenue outlook | outturn | GAAP gross margin outlook | outturn | source |
  |---|---|---|---|---|---|
  | Q1 FY2023 | $8.10bn | **$8.29bn** (above the top) | 65.2% | 65.5% (inside) | EX-99.1 2022-02-16, 2022-05-25 |
  | **Q2 FY2023** | **$8.10bn** | **$6.70bn (17% below; pre-announced 2022-08-08)** | 65.1% | **43.5%** | EX-99.1 2022-05-25, 2022-08-08, 2022-08-24 |
  | Q3 FY2023 | $5.90bn | $5.93bn (inside) | 62.4% | **53.6% (8.8 points below)** | EX-99.1 2022-08-24, 2022-11-16 |
  | Q4 FY2023 | $6.00bn | $6.05bn (inside) | 63.2% | 63.3% (inside) | EX-99.1 2022-11-16, 2023-02-22 |
  | Q2 FY2026 | $45.0bn | **$46.7bn** (above) | 71.8% | 72.4% (above; includes a $180M release) | EX-99.1 2025-05-28, 2025-08-27 |
  | Q3 FY2026 | $54.0bn | **$57.0bn** (above) | 73.3% | 73.4% (inside) | 2025-08-27, 2025-11-19 |
  | Q4 FY2026 | $65.0bn | **$68.1bn** (above) | 74.8% | 75.0% (inside) | 2025-11-19, 2026-02-25 |
  | Q1 FY2027 | $78.0bn | **$81.6bn** (above) | 74.9% | 74.9% (inside) | 2026-02-25, 2026-05-20 |
  | Q2 FY2027 | $91.0bn | **$96.2bn** (above) | 74.9% | 75.0% (inside) | 2026-05-20, 2026-08-26 |
  **Revenue met or beaten 8 of 9, above the top of the range 6 of 9; one miss of 17% in the down-year, when gross margin came in 21.6 points under the
  outlook, and gross margin missed again the next quarter by 8.8 points. Gross margin met or beaten 7 of 9.** The miss was **pre-announced eight days after the quarter closed**, with the cause and the price action named: *"the company implemented pricing
  programs with channel partners to reflect challenging market conditions"* (2022-08-08). That is the candour case [E2-26] handled well. The ratchet
  [E5-30] is live (a quarterly outlook for at least four years). The promotional register is in the CEO quotations (*"the largest infrastructure expansion
  in human history"*, 2026-05-20; *"Now, compute is revenue"*, 2026-08-26) and the *"over $500 billion"* financing platforms announced *"subject to
  definitive agreements"*, not in multi-year numeric targets. **Recorded as a live behaviour whose one test in a soft year was a large miss disclosed
  promptly.**
- [ ] **Serial share issuance [E5-15]: prompt run, NOT FIRED as issuance.** Split-adjusted shares (cover pages; 4-for-1 2021 and 10-for-1 2024 verified at
  Step 0): **21,664M (2016-03) → 23,544M (2017-02) → 25,100M (2022-03 peak) → 24,147M (2026-07-26)**: +11.5% in ten years, +2.6% since February 2017, and
  **-3.8% from the 2022 peak**. The 2016-17 step is convertible-note conversions (FY2017 cash-flow *"Loss on early debt conversions"*); the rest is employee
  stock. **What it cost to hold the count:** repurchases of $135,635M and RSU tax withholding of $28,884M FY2017-H1 FY2027; since FY2023, **$156,075M bought
  a net reduction of 953M shares, about $164 per share retired** (`q3calc_out.txt`). No issuance for cash in the decade.
- [ ] **Dividends funded by issuance [E2-52]: not fired.** The quarterly dividend rose from $0.01 to $0.25 a share from June 2026 (release 2026-05-20), about
  $24bn a year on 24.1bn shares, with no share issuance for cash. *(But see condition (1) below: H1 FY2027's distributions exceeded cash left after
  investment, and the half raised $24.9bn of debt.)*
- [ ] **Filed-figure tells [E4-30]: NOT FIRED.** Cash taxes as a share of pre-tax income: **0.7-5.9% (FY2017-FY2022) → 33.6% (FY2023, on a small
  pre-tax) → 19.4% → 18.0% → 14.3% (FY2024-FY2026)**; 15.3% in FY2026 excluding the $8,918M of non-cash equity gains; cash tax $20,288M against book tax
  expense $21,383M in FY2026. **Rising across the decade, not falling.** Reported growth is not unnaturally smooth (FY2020 revenue fell 6.8%; FY2023 operating
  income fell 58%). *Presentation note:* the Q2 FY2027 10-Q cash-flow statement prints no cash-tax line (the Q2 FY2026 10-Q did), so a trailing figure is not
  computable from the filing; recorded, not a flag.
- [x] **Weak accounting: a PROMPT on useful lives, read, not a cockroach.** *"In February 2023, we assessed the useful lives of our property, plant, and
  equipment. Based on advances in technology and usage rate, we increased the estimated useful life of a majority of the server, storage, and network
  equipment from three years to a range of four to five years, and assembly and test equipment from five years to seven years ... an increase in operating
  income of $135 million"* (10-K FY2024). **Lengthening lives lowers depreciation**, the direction Amazon reversed in the same era; at 0.4% of FY2024
  operating income it is immaterial, and from the FY2025 10-K the stated range is *"two to seven years"*, so some assets now carry shorter lives. Carried to
  Q4's [E5-20] question. SBC has been expensed throughout.
- [x] **Metric-switching [E2-49]: two switches, neither fires on the rule's form; one soft note.** (1) SBC into non-GAAP, above. (2) From Q1 FY2027 the
  market platforms changed (*"NVIDIA will have two market platforms — Data Center and Edge Computing"* (the dash is the release's), Hyperscale and ACIE within Data Center; Gaming no
  longer reported alone), comparatives recast, announced at record results. **The soft note:** the Q1 FY2027 release bridged the old split once (*"Data
  Center compute revenue was a record $60.4 billion, up 77% ... networking revenue was a record $14.8 billion, up 199%"*), and the compute line, the one
  growing more slowly than the total, is absent from the Q2 FY2027 release and 10-Q. My [E2-49] prior (six fires, five failures as of 2026-09-12) is checked,
  not assumed: **not a fire; recorded for the next filing to test.**
- [ ] **Stock-price targeting [E3-50]: not fired.** One of three pay elements vests on *"3-Year Relative TSR"*; that ties pay to the price, not to the premise
  *"that their job at all times is to encourage the highest stock price possible"*; no stratagem found.
- [ ] Unintelligible footnotes: not fired. The commitments and guarantees notes name counterparties, triggers, caps and timing.

**Where the flags converge [E4-52]?** The fired prompts are a recurring charge treated as "excluding", a live guidance habit, and a useful-life extension;
the older facts are a 2017 candour failure and a decade of SBC excluded from the headline. **Since 2022 they point the same way, toward more disclosure**
(the pre-announcement, SBC put back, the commitments and guarantee tables). **No confluence toward one outcome is found.**

**STEP 3: THE PRIMARY TEST [E2-01]**, balance sheet first **[E5-27]** (`q3calc_out.txt`; FY2016-FY2024 balance sheets are companyfacts screening
values, the FY2025, FY2026 and 2026-07-26 balance sheets re-read on the filed faces):
| FY | equity | NI ÷ avg equity | operating capital (equity − cash − debt securities − stakes + debt) | after-tax operating income ÷ avg operating capital | same, ex goodwill and intangibles [E2-43] |
|---|---|---|---|---|---|
| FY2017 | 5,762 | 32.6% | 1,743 | 127% | 304% |
| FY2018 | 7,471 | 46.1% | 2,363 | 133% | 201% |
| FY2019 | 9,342 | 49.3% | 3,908 | 103% | 131% |
| FY2020 | 12,204 | 26.0% | 3,298 | 67% | 82% |
| FY2021 (Mellanox) | 16,893 | 29.8% | 12,295 | 49% | 96% |
| FY2022 | 26,612 | 44.8% | 16,350 | 60% | 114% |
| **FY2023** | 22,101 | **17.9%** | 19,470 | **20%** | 31% |
| FY2024 | 42,978 | 91.5% | 25,382 | 129% | 174% |
| FY2025 | 79,327 | 119.2% | 41,193 | 212% | 257% |
| FY2026 | 157,293 | 101.5% | 76,114 | 189% | 254% |
| TTM to 2026-07-26 | 228,984 | 99.9% (Jan/Jul average) | 106,867 | 181% | 246% |

*(CONVENTION, confessed: after-tax operating income uses the filed effective rate for FY2024 onward and 15% where the rate was not extracted, FY2017-FY2023;
"stakes" are non-marketable and publicly-held equity securities, which were immaterial before FY2023.)*
- **Primary test: passed at a level no run in this queue has shown, and not steady.** The one soft year (FY2023) fell to 17.9% on equity and 20% on operating
  capital; the series is a wave, which is Q2's finding read through the owners' capital.
- **What the $99bn of stakes and H1 FY2027's $24,140M of other income do to it.** Stakes are **43.2% of equity at 2026-07-26** (25.4% at 2026-01-25). TTM
  net income of $192,880M includes **$32,164M of other income**; net income without it (taxed at the TTM rate of 16.0%) over average equity **without the
  stakes** is **134.1%**, against 99.9% reported. **The stakes lower the reported return, not raise it:** they add a large denominator and marks that are
  small beside operating income. The primary test is carried by the chip business; the capital now going to stakes earns marks, not cash, and its return is
  not computable from the filings.
- **[E2-56], judged incrementally:** operating capital rose from $19,470M (FY2023) to $106,867M (2026-07-26) while after-tax operating income rose by about
  $162bn: **the increment earns far above any hurdle.** The capital outside operating capital (stakes $99bn, commitments $25bn more) has no cash return on
  file; the consolidated series cannot camouflage it because it is not yet in the series.
- **[E3-54] retention:** passes by orders of magnitude (retained earnings $219,157M against a cap of $5,270.9bn), which measures the wave as much as the
  allocation.

**The half-owner test [E2-26].** The filings tell the owner the commitments by type and year, the guarantee caps with counterparty (*"an affiliate of
OpenAI Group PBC"*), triggers and timing, the stakes in total with measurement, every provision with its product, customer concentration by percentage,
the AI cloud mechanics (*"which the AI clouds can unilaterally stop providing to us and sell to third-party customers at more advantageous rates"*), and the
FY2023 miss eight days after quarter-end. **They do not tell the owner:** the $99bn itemised by investee (only Intel $5bn and Anthropic up to $10bn are named,
in the Q3 FY2026 10-Q); **how much revenue comes from customers NVIDIA has invested in, financed or guaranteed** (the 10-K says only *"These investments include
AI model makers that purchase our products directly or through CSPs"*); the revenue recognised on sales to AI clouds that carry NVIDIA's buy-back commitment;
the price paid per share for any stake; or who the 22% and 14% customers are. **Mixed: candid in the notes where the numbers are large and new; silent on the
one number that sizes the round trip. And in 2017, by the regulator's finding, it failed the test outright.**

**The institutional imperative: score all four [E2-30].** *Not a fraud test.*
- [ ] resists change: not ticked (a new reporting framework, SBC put back into non-GAAP, a new AI cloud business model in Q2 FY2027).
- [x] **projects soak up funds (prompt):** $17.5bn into private companies and infrastructure funds in FY2026; **$42,404M of equity purchases in H1 FY2027**
  and $25bn more committed; ~$17bn for the Groq licence and hires; $11.9bn plus up to $1.0bn of retention equity for Hugging Face; guarantees capped at
  $105bn; *"more than $500 billion"* of financing platforms in memorandum form. The cash is large and the projects have materialised as fast as it has.
- [ ] staff studies to justify a craving: no evidence either way in a filing.
- [x] **peers imitated (prompt):** Broadcom backstops its custom-accelerator customers ($29bn, Q2 row), Amazon funds OpenAI and Anthropic (AMZN run), and
  NVIDIA funds and guarantees the same laboratories; **[E2-27]**'s picture, each rational alone.

**Capital allocation: buybacks [E5-08, E4-31, E5-24, E4-50].**
- **(1) Ample funds for operations and liquidity: met on liquidity, with a borrowed half-year.** Cash and debt securities $56,586M, OCF $134,360M TTM. But in
  H1 FY2027 OCF of $74,421M less capex $4,434M, net equity purchases $35,163M, Groq $2,944M, repurchases $39,044M, dividends $6,290M and withholding $4,531M
  leaves **-$17,985M** before the smaller lines, and the half raised **$24,896M of notes**. Against **$120bn of commitments due in the rest of FY2027**, distributions were in effect
  partly borrowed. [E4-50] licenses borrowing to buy back **only at a true discount**; that is condition (2)'s question. Prompt, and [E2-60]'s "financial
  strength" dimension is carried to Q4.
- **(2) A material discount to intrinsic value conservatively calculated: FAILS on this run's computation. CAPITAL ALLOCATION FLAG.** Average prices paid
  (split-adjusted, from the 10-K equity notes and the 10-Q): **$15.94 (FY2023), $46.19 (FY2024), $109.68 (FY2025), $143.26 (FY2026), $196.06 (H1 FY2027),
  $209.57 (Q2 FY2027)**. Q5's computation (below) values the business at the 10% floor at roughly **$50 a share with no growth, ~$105 at 5% a year forever
  and ~$175 at 7% forever, all from the best twelve months on file.** The FY2026 and FY2027 purchases sit at the 6-7%-forever end of that range, which is
  no discount. The stated reason was never value: *"Our share repurchase program aims to offset dilution from shares issued to employees"* (10-Ks FY2024,
  FY2025); the FY2026 10-K drops the sentence and gives none; "intrinsic value" appears 0 times in the FY2026 10-K, the Q2 FY2027 10-Q, the DEF 14A and the Q1 FY2027 CFO commentary. **[E4-31]'s
  third condition (owners supplied the information to estimate value) is therefore not addressed at all.** With the humility clause **[E4-13]**: *"They also
  know a whole lot more about them than I do"*; and **[E5-08]**: *"infractions, even serious ones, are innocent; many CEOs never stop believing their stock is
  cheap"*. **Binds position size, never the discount rate. The FY2023 purchases ($10.04bn at ~$16) were, in hindsight, the cheapest capital this company ever
  retired; hindsight is not the test, and the FY2023 10-K stated no rationale for them either (0 hits for "offset dilution").**
- **The refusal test [E2-51]:** not applicable (repurchasing heavily).
- **Groq [E5-24, E4-39]:** ~$17bn for *"a non-exclusive license agreement ... and hired certain Groq employees"*, booked as $14.4bn of goodwill *"primarily
  attributable to the workforce and future development of the licensed technology"*; *"NVIDIA Groq 3 LPX ... is now in full production"* two quarters later.
  No return case and no post-mortem supplied. At Q2 it was evidence of a substitute; here it is a price paid for position without a value case.
- **Hugging Face [E5-44]:** *"approximately $11.9 billion purchase price payable to Hugging Face stockholders ... and an equity-based retention program of up
  to approximately $1.0 billion"*; the 8-K does not state the form of the purchase price (0 hits for "cash"), so [E5-44]'s test on shares given cannot be run; no value
  case filed.
- **The equity in customers [E3-40]:** $99bn plus $25bn committed, including companies that *"purchase our products directly or through CSPs"*. This is not
  [E3-40]'s manager wandering off the base business into so-so businesses: **it is the base business's demand being financed by the seller**, the Q2 finding
  seen as allocation. Recorded as a prompt, and as the channel through which a demand pause becomes a capital loss (Q4).
- **Tenure [E3-58]:** the same CEO since 1993 and CFO since 2013 allocated all of it; allocation is not visibly outsourced to bankers or consultants.

**Pay and what it vests on [E4-27]** (DEF 14A 2026): three elements: *"variable cash awards based on annual revenue"*; *"PSUs based on annual Non-GAAP Operating Income performance with a single-year
performance metric, vesting over four years"*, where Non-GAAP Operating Income is *"GAAP operating income ... excluding stock-based compensation expense, acquisition-related and other costs, and other"*,
and multi-year PSUs on *"3-Year Relative TSR"*. The FY2026 stretch goals *"would automatically be reduced to $160.0 billion and $96.0 billion"* if H20 controls came
in the first half, a rule set *"at the time it set the Fiscal 2026 performance goals"* (pre-set, which [E2-49] asks for), and irrelevant to the outcome: revenue
of $215.9bn beat even the original $190.0bn. **The incentive to note:** cash pay rewards revenue whether or not NVIDIA financed the buyer, and equity pay
rewards an operating profit that excludes the executives' own stock pay and ignores capital committed to stakes, guarantees and buy-backs. **A prompt, not a
flag**; it points at the same round trip as the half-owner gap.

**THE GUARDRAIL: checked before the verdict.**
- [x] Nothing in this Q3 is used to **promote** the name **[E2-37, E2-38, E3-39]**; the extraordinary returns above are the wave's, and Q2 has ruled on that.
- [x] **Key-person dependence [E4-23]:** none filed (recorded at Q2).
- [x] Is a great manager the reason to act? **No; the file is closed on the business.** [E2-35, E2-36] do not arise.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *No personal-misconduct disqualifier found (the absence of found disqualifiers, not a finding of honesty [E5-17]). Carried, heaviest first: the SEC's 2022
  finding that the company's 2017 10-Qs omitted what it knew about cryptomining, on a negligence standard with no individual charged, corrected in the next
  10-K, by the same CEO and CFO who run it now [E2-26, E2-68]; the certified class action on the same facts, open, which would become a [E5-16] matter on a
  scienter finding against a named officer; a capital-allocation flag on buyback condition (2), no value rationale ever stated [E5-08, E4-31], and H1 FY2027
  distributions partly borrowed [E4-50]; recurring provisions presented "excluding" [E2-57]; pay on revenue and on an operating profit that excluded SBC
  [E4-27]. IN never promotes.*

---

## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

*Working: `oe.py` / `oe_out.md` in the research folder. Every input is hand-read from the filed consolidated statements of cash flows: FY2017-FY2019
from the FY2019 10-K (`0001045810-19-000023`; FY2017 matched on the FY2017 10-K, `0001045810-17-000027`), FY2020 from the FY2022 10-K
(`0001045810-22-000036`), FY2021-FY2023 from the FY2023 10-K (`0001045810-23-000017`), FY2024-FY2026 from the FY2026 10-K (`0001045810-26-000021`), and
the two half-years from the Q2 FY2027 10-Q (`0001045810-26-000075`), with H1 FY2026 matched on the Q2 FY2026 10-Q. No line differed between vintages. The
FY2018 and FY2020 10-Ks were not needed: every year FY2017-FY2026 sits inside a 10-K on disk. Depreciation is property-and-equipment depreciation from each
10-K's note, not the cash-flow D&A line (Step 0 defect 3).*

### Owner earnings by year, $M **[E2-23]** (OCF less SBC less (c); CONVENTION at VI)
| year | OCF | SBC | OCF−SBC | capex (P&E and intangibles) + financed principal | P&E depreciation | capex ÷ depreciation | **OE, (c) = capex + principal** | OE, (c) = depreciation | acquisitions (Groq in FY2026) |
|---|---|---|---|---|---|---|---|---|---|
| FY2017 | 1,672 | 247 | 1,425 | 176 | 118 | 1.49x | 1,249 | 1,307 | 0 |
| FY2018 | 3,502 | 391 | 3,111 | 593 | 144 | 4.12x | 2,518 | 2,967 | 0 |
| FY2019 | 3,743 | 557 | 3,186 | 600 | 233 | 2.58x | 2,586 | 2,953 | 0 |
| FY2020 | 4,761 | 844 | 3,917 | 489 | 355 | 1.38x | 3,428 | 3,562 | 4 |
| FY2021 | 5,822 | 1,397 | 4,425 | 1,145 | 486 | 2.36x | 3,280 | 3,939 | 8,524 (Mellanox) |
| FY2022 | 9,108 | 2,004 | 7,104 | 1,059 | 611 | 1.73x | 6,045 | 6,493 | 263 |
| **FY2023** | 5,641 | 2,709 | 2,932 | 1,891 | 844 | 2.24x | **1,041** | 2,088 | 49 |
| FY2024 | 28,090 | 3,549 | 24,541 | 1,143 | 894 | 1.28x | 23,398 | 23,647 | 83 |
| FY2025 | 64,089 | 4,737 | 59,352 | 3,365 | 1,300 | 2.59x | 55,987 | 58,052 | 1,007 |
| FY2026 | 102,718 | 6,386 | 96,332 | 6,143 | 2,355 | 2.61x | 90,189 | 93,977 | 14,535 (13,000 Groq) |
| **TTM to 2026-07-26** | 134,360 | 7,241 | 127,119 | 7,474 | 2,972 | 2.51x | **119,645** | 124,147 | 17,100 (incl. 2,944 Groq in financing) |

*(The FY2025 depreciation figure is the note's rounded "$1.3 billion"; FY2026 is D&A of 2,843 less intangible amortization of 488; TTM = FY2026 − H1
FY2026 + H1 FY2027.)*

### Stock compensation: subtracted in full **[E5-06]**; RESOLVES, and the charge is the floor **[E3-70]**
- The cash-flow add-back *"Stock-based compensation expense"* resolves in every year FY2017-TTM from the filed statements. SBC ÷ OCF: **9.2% cumulative
  FY2022-FY2026**, 6.2% in FY2026, 5.4% TTM; far below the 50% level at which the resume state asks for a grant table read by hand.
- **Read anyway, because the market measure is the rule:** the estimated total grant-date fair value of awards granted was **$3,492M, $4,505M, $5,316M,
  $7,834M and $9,389M (FY2022-FY2026), 1.47-1.74x the charge** (10-K stock compensation notes). On grant-date value the five-year mean owner earnings fall
  from $35,332M to **$33,102M**. Shown as a band end, not stacked. Tax withholding on vesting ($7,948M in FY2026) is not added: it buys back part of what
  the charge already counts.

### MORE THAN ONE WINDOW, AND EVERY (c) QUESTION SHOWN BOTH WAYS **[E4-25, E4-38]**
| window | OE, (c) = capex + principal | OE, (c) = depreciation | capex end, less acquisitions | capex end, SBC at grant-date value |
|---|---|---|---|---|
| **5-yr FY2022-FY2026 (the default [E2-42])** | **35,332** | 36,851 | 32,145 | 33,102 |
| 3-yr FY2024-FY2026 | 56,525 | 58,559 | 51,316 | 53,902 |
| 10-yr FY2017-FY2026 (crosses Mellanox) | 18,972 | 19,898 | 16,526 | not computable (grant values not extracted before FY2022) |
| 5-yr FY2017-FY2021 (crosses Mellanox) | 2,612 | 2,946 | 907 | not computable |
| FY2023-FY2025 + TTM (five periods; the TTM overlaps H2 FY2026, stated) | 58,052 | 60,382 | 51,497 | not computed |
| **TTM to 2026-07-26** | **119,645** | 124,147 | 102,545 | 116,240 (FY2026's 1.47x applied to TTM SBC, CONVENTION) |

- **The spread is the wave, and it is enormous:** the TTM is **3.4x** the five-year mean and **6.3x** the ten-year mean; FY2023 alone was $1,041M. By
  **[E3-55]**, volatility around a certain endgame is not a defect; **here the endgame is what Q2 found uncertain**, so the spread is uncertainty about the
  level, not noise around it.
- **[E4-41], normalise the mean down for luck:** the TTM sits at the top of a filed boom (Data Center revenue +117% year on year in Q2 FY2027), with the outlook
  assuming no Data Center compute revenue from China. The favourable exogenous break is the AI buildout itself, and it cannot
  be stripped out by a figure; it is named, and it is why the five-year mean rather than the TTM is the default.
- **Perimeter:** the five-year default does not cross Mellanox (FY2021); the ten-year and FY2017-FY2021 windows do. **Groq sits inside FY2026 and the TTM**,
  and the 10-K says *"No customer contracts, existing products, or equity interests were purchased"*, so it is a purchased technology and workforce, not a
  revenue perimeter. Hugging Face is pending and crosses no window.

### Maintenance capex: a DISCLOSED JUDGMENT with a corpus DEFAULT **[E3-44, E2-41, E5-20, E4-47]**
**THE [E5-20] QUESTION, ASKED ON THE FILING, SEPARATELY FROM THE LABEL. Answer: NOT the exception class on the plant, and the plant is not where (c) lives.**
- **What NVIDIA's own filing says about useful lives:** *"In February 2023, we assessed the useful lives of our property, plant, and equipment. Based on
  advances in technology and usage rate, we increased the estimated useful life of a majority of the server, storage, and network equipment from three
  years to a range of four to five years, and assembly and test equipment from five years to seven years"* (10-K FY2024). **The filer lengthened lives; at
  AMZN the filer shortened them "due to the increased pace of technology development".** From the FY2025 10-K the equipment range reads *"two to seven
  years"* (FY2026: gross *"Equipment, compute hardware, and software | 12,619"* at *"2 - 7"* years). **No instance found**, in the FY2024-FY2026 10-Ks or the
  Q2 FY2027 10-Q, of NVIDIA saying depreciation understates what it must spend to renew its plant.
- **Where the product cadence does its damage: inventory, not plant.** Provisions for inventory and excess purchase obligations **$116M (FY2021), $354M
  (FY2022), $2.17bn (FY2023), $2.2bn (FY2024), $3.7bn (FY2025), $7.2bn (FY2026), $2.1bn (H1 FY2027)**, less releases of $137M, $540M, $689M, $1.5bn and
  $280M (FY2023-H1 FY2027). *"We have experienced and may in the future experience reduced demand for current generation architectures when customers
  anticipate transitions"* (10-K FY2023).
- **Do the provisions belong in (c)? They belong in owner earnings, and they are already there; adding them to (c) would count them twice.** A provision
  reduces net income and reduces the inventory balance (or raises the accrued obligation) by the same amount, so operating cash flow is unchanged in the
  quarter it is booked; **the cash was spent when the inventory was bought, or leaves when the obligation is settled**, and both sit inside OCF. Over any
  multi-year window, the OCF-based owner earnings above already carry the cash cost of every transition in the window. What they do **not** carry is the
  transition not yet taken: the next write-down is inside the **$279bn** of supply commitments, which is exposure, and it is quantified in the named death,
  not guessed into (c).
- **Plant, the corpus default [E3-44]:** capex (with financed principal) ran **1.28-2.61x depreciation** FY2022-TTM while revenue grew 11x. The two plant
  ends differ by **$1.5bn on the five-year mean and $4.5bn on the TTM (about 4% of each)**. **The plant band does not move any conclusion here; the D&A end is not
  INVALID on NVIDIA's filing, and the capex end is used as the stated (c) because it is the more conservative and the difference is immaterial.**

**THE WORKING-CAPITAL INCREMENT [E2-23]: included, through OCF, and it is large.**
- **The flag (a single line above 30% of a period's OCF) fires twice:** FY2023 inventories **−$2,554M (45.3% of OCF)**, the down-year build that preceded the
  provisions; H1 FY2027 accounts receivable **−$24,590M (33.0%)**. Near misses: FY2023 prepaid and other −26.9% (supply prepayments), FY2017 and FY2019
  inventories −22.4% and −20.7%.
- **TTM working capital consumed $40,745M, 30.3% of OCF** (receivables −$35,246M, inventories −$16,648M, prepaid and other −$6,849M, against payables and
  accruals +$15,163M and other +$2,835M), while customer advances rose (deferred revenue note: *"Included $ 15.6 billion and $ 7.5 billion of customer advances for the first half of fiscal years
  2027 and 2026"*).
- **Growth or maintenance?** *For adding it back:* most of the build is the growth [E2-23] does not ask (c) to carry; without it TTM owner earnings would be
  ~$160bn. *Against:* the receivable build is partly the price of volume: *"longer payment terms ranging from 90 days up to one year"* for large customers,
  and *"Financing arrangements with certain investment-grade customers, including extended payment terms under large, multi-quarter agreements, will continue
  to affect the timing of our operating cash flows"* (10-Q MD&A). **Terms extended to keep customers buying are a cost of maintaining unit volume. No
  "ex-working-capital" figure is used; the ~$160bn is displayed only as the most generous number constructible.**

**THE PRIOR I WAS TOLD I AM MOST LIKELY WRONG ABOUT: are the capacity buy-backs, stakes and guarantees purely balance-sheet items outside (c)?** *Built both
ways before ruling.*
- **(a) AI cloud agreements, $36bn.** *The mechanism:* *"AI clouds procure our data center infrastructure products and we commit to cloud service agreements,
  which the AI clouds can unilaterally stop providing to us and sell to third-party customers at more advantageous rates. Our commitments, which are
  typically six years in duration, totaled $36 billion as of July 26, 2026, and decrease as capacity is used by third-party customers or by us for our
  research and development efforts"* (10-Q MD&A; schedule **$6bn FY2028, $8bn FY2029, $7bn FY2030, $6bn FY2031, $9bn after**, nothing in the rest of FY2027).
  *For (c):* the partner buys NVIDIA's systems (revenue now, inside the TTM) **because** NVIDIA stands behind the capacity for six years (cost later, outside
  every window); that is a cost of the unit volume, booked after the volume. *Against:* it is a backstop, not a certain cost; it falls away as third parties
  use the capacity, NVIDIA uses it for R&D, and *"we will participate in revenue share"*. **Ruled: partly (c).** The cost is contingent, so the band is
  **$0 (never called) to ~$6bn a year (fully called, $36bn over six years)**. The revenue booked on these sales is not disclosed (Q3 half-owner gap).
- **(b) Cloud service agreements, $29bn** (*"cloud infrastructure to support our research and development of our open models"*): rented R&D compute, a
  cost of competitive position, **already expensed inside OCF as it is used**. Not added.
- **(c) Equity stakes in customers.** *For (c):* the 10-K says *"These investments include AI model makers that purchase our products directly or through
  CSPs"*, and the 10-Q says the buyers *"currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity"*.
  Where the stake finances the purchase, the cash is a demand-maintenance cost that the cash-flow statement files under investing. *Against:* the stakes
  are assets with market values (*"Gains from equity securities, net | ( 23,707 )"* H1 FY2027) and some are sold (*"Proceeds from sales of equity securities |
  7,241"*); Intel's $5bn is not customer finance; Step 0 ruled the **gains** out of owner earnings, which stands. **Ruled: shown both ways, not chosen.**
  Equity purchases: five-year mean ~$4.0bn (FY2022-FY2026 investing lines, gross: *"Investments and other, net"* 24 and 77, then non-marketable equity
  862, 1,486 and 17,502); **TTM at least $51.4bn** (FY2026 non-marketable
  purchases net 17,418, less H1 FY2026's 1,175, plus H1 FY2027's 35,163; FY2026 public-equity purchases sit inside "Purchases of marketable securities" and
  are not separable on the face).
- **(d) Guarantees ($108.5bn cap) and third-party leases ($20bn).** No cash in any window; the SB Energy guarantees are *"triggered upon certain tenant
  defaults"* and not yet effective. **Ruled: outside (c); exposure, carried to the named death.** Treating a contingent guarantee as an annual cost would
  guess a default rate no document supplies.
- **(e) Groq (~$17bn) and Hugging Face ($11.9bn).** *For (c):* Q2 found the moat is rebuilt by buying the replacement, and Groq is a licence to a rival
  inference architecture, which is [E2-23]'s *"to fully maintain its long-term competitive position"* in its plainest form. *Against:* one-off purchases;
  Mellanox added a business. **Shown both ways** (the "less acquisitions" column).
- **So the prior was half right.** The guarantees are exposure, not (c). **The AI cloud buy-backs are a contingent maintenance cost booked after the
  revenue, and the stakes in buyers are, in part, demand finance filed as investment**; a TTM owner-earnings figure that counts the sale and not the
  financing overstates what owners keep.

**The combined range, stated in dollars (windows × (c)):**
- **Five-year default:** $35.3bn (capex end) → **~$26bn** with the five-year means of net equity purchases (~$4.0bn), acquisitions (~$3.2bn) and SBC at
  grant value (~$2.2bn) all taken as (c); $36.9bn at the depreciation end.
- **TTM:** $119.6bn (capex end) → **~$62bn** with TTM net equity purchases ($51.4bn) and a fully called AI cloud backstop ($6bn) as (c); $102.5bn less
  acquisitions alone; $124.1bn at the depreciation end; ~$160bn before the working-capital build (most generous, not a judgment).
- **The judged central figure is the capex end ($35.3bn five-year, $119.6bn TTM), with the stake and backstop question displayed as the downward band.**
  *Is that range too wide to reach a conclusion [E4-25]?* **For survival, no: every construction is positive, in every window, in every year including
  FY2023.** For value it is a factor of about five from the conservative five-year end to the generous TTM end, and that width is carried to Q5, where it
  does not matter because the price sits above all of it.
- **Look-through [E3-04]: none added** (no undistributed investee earnings are evidenced, and the equity-method income is *"not significant"*).

### Great, good, or gruesome? **[E4-20, E4-43]**
- **[x] great, on the filed record of capital required** · [ ] good · [ ] gruesome
- **Evidence:** after-tax operating income ÷ average operating capital **127% (FY2017) to 212% (FY2025), 181% TTM, 20% in FY2023** (Q3 table); net plant
  $14.3bn carries TTM operating income of $197.6bn; in the six months to 2026-07-26 operating capital rose ~$31bn while after-tax operating income for the half was ~$98bn. That
  is [E4-20]'s great account, *"an extraordinarily high interest rate"*.
- **But [E4-20]'s great account is one whose rate *"will rise as the years pass"*, and two things move the account on the filed record.** (1) The rate is a
  wave: 20% in FY2023, and Q2 found its basis re-won each cadence. (2) **The capital is now going outside operating capital**: $99bn of stakes, $25bn more
  committed, $36bn of buy-backs and $108.5bn of guarantees, none earning a filed cash return. On the operating capital alone the account is great; **counted
  with the capital committed to keep the customers buying, it is travelling toward good**, and at Q2's close no class above good is claimable for the whole.

### Staying power: score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: LARGE, NOT RELIABLE.** Owner earnings $119.6bn TTM; but two filed pauses in seven years: FY2020 revenue
  −6.8% and operating income −25%; FY2023 revenue flat and operating income −58%, owner earnings $1.0bn. **Half.**
- **(2) Massive liquid assets: YES.** Cash $22,443M and marketable debt securities $34,143M (**$56,586M**) at 2026-07-26; marketable equity $42,783M, of which
  *"$36.9bn under short-term lock-up restrictions"* (Step 0 table), not counted; the $25.0bn commercial paper program is undrawn and **not counted** [E5-39].
  **One.**
- **(3) No significant near-term cash requirements: NO.** 10-Q Note 10: **commitments of $120bn due in the remainder of FY2027** (supply and capacity $92bn,
  equity investments $18bn, capital expenditures $7bn, cloud $3bn) and **$100bn in FY2028**; Hugging Face ~$11.9bn on close (expected first half of
  2027; the 8-K does not state the form of payment); accrued Groq consideration $986M; the dividend at $0.25 a quarter (~$24bn a year); repurchase authorization of ~$99.0bn. In a normal year these
  are paid from revenue (TTM OCF $134.4bn). **In a FY2023-type year they are not, and the supply commitments are the part the 10-Q says may be adjustable
  only *"in certain instances"*.** **Zero.**
- **Score: 1.5 of 3.**
- **Leverage, named and quantified [E4-16, E3-29]:** senior notes **$33.5bn** face (from $8.5bn at 2026-01-25; $25.0bn issued June 2026 in seven tranches,
  2028-2056, coupons 4.25%-5.625%), $1.0bn due in FY2027 and $4.75bn in 2028 (Note 9); operating lease liabilities $4,985M long-term plus $25bn of leases not
  commenced for own use and $20bn for third parties; guarantees capped at $108.5bn; equity $228,984M, of which 43.2% is stakes.
- **Coverage [E2-54]:** interest expense TTM **$464M** (FY2026 259 − H1 FY2026 124 + H1 FY2027 329), rising to roughly $1.4-1.5bn a year on the new notes'
  coupons (my arithmetic); against OCF net of capital expenditure of **$127bn** TTM, **met about 90 times over**. [E2-54] is comfortably passed.
- **[E2-60] the third dimension of maintenance (financial strength):** H1 FY2027 distributions and investments exceeded cash generated by ~$18bn and the half
  raised $24.9bn of notes (Q3). Not yet a restricted-earnings finding; recorded as the direction to watch.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: THE ROUND TRIP [#18], from the vendor's side, on top of CONTRACTED NOT TO STOP [#1].** *NVIDIA finances and guarantees the laboratories and
AI clouds whose purchases are its demand, extends them terms of up to a year, stands behind their capacity, and commits $279bn forward to supply them. A
demand pause at an architecture transition, the FY2023 mechanism, arriving while those positions are open would turn one lost year of margin into a capital
loss across inventory, stakes, receivables, buy-backs and guarantees at once, because they are the same few counterparties.* The company does not die;
**the owners' return on several years of the wave does.**

**Exposure, from the filing, not experience [E4-40]:**
- **Supply:** inventory $31,575M and supply and capacity commitments **$279bn**, raised from $119bn in one quarter, *"for long-term demand across current and
  future product architectures"*.
- **The counterparties:** three direct customers were 16%, 15% and 13% of H1 FY2027 revenue; receivables $63,059M; *"one AI research and deployment company
  contributed a meaningful amount of our revenue by purchasing cloud services from our customers"*; stakes of $99bn and $25bn committed; AI cloud buy-backs
  $36bn; SB Energy guarantees capped at $105bn for *"an affiliate of OpenAI Group PBC"*, payable on tenant default, phases from FY2029, each over a 20-year
  lease; land, power and shell guarantees $3.5bn.
- **The regime:** H20 ($4.5bn) and H200 ($0.4bn) charges followed export rules; China's preliminary finding on the Mellanox conditions is open (Q3). A rule
  change is the other filed trigger for a sudden write-down, and it has fired twice in eighteen months.
- **The address (#12, carried, not the death):** *"geopolitical tensions and conflicts, including but not limited to China, Hong Kong, Israel, Korea and Taiwan
  where the manufacture of our product components and final assembly of our products are concentrated"* (10-K FY2026). TSMC is the named foundry; the TSM
  run's shape applies to the supplier and reaches NVIDIA through it.

**Quantified, from filed figures (my arithmetic; the scalings are CONVENTION, confessed):**
- **The FY2023 ratio, scaled.** FY2023 provisions of $2.17bn were **18.7%** of the opening exposure (inventory $2,605M plus inventory purchase and supply
  obligations of $9.00bn at 2022-01-30, FY2022 10-K). The same ratio on 2026-07-26's exposure ($31.6bn plus $279bn) is **~$58bn**. In FY2023 operating
  margin went from 37.3% to 15.7%; the same fall on TTM revenue of $303.0bn takes operating income from $197.6bn to **~$48bn**.
- **The stakes:** $99bn carrying value; a pause that closes the laboratories' funding would mark them down. Half is **~$50bn** (illustrative; non-cash; the
  10-Q itemises no investee, so no filed basis exists for a better figure).
- **The backstop:** up to **$36bn** over six years if the AI clouds' third-party customers disappear; up to **$105bn** over twenty-year leases if OpenAI's
  affiliate defaults after the phases commence, less whatever NVIDIA recovers by hosting its own infrastructure on the site (*"the site will exclusively
  host NVIDIA AI infrastructure"*).
- **Against what survives it:** equity **$229.0bn**; liquid assets $56.6bn; notes $33.5bn with nothing large due before 2028; FY2023 itself, when the
  company stayed profitable, kept paying its dividend and repurchased $10.04bn. **A pause plus a half write-down of the stakes plus the full AI cloud backstop
  (~$58bn + ~$50bn + $36bn = ~$144bn) consumes most of a year's operating income and about 63% of equity, and the company survives it.** Only the pause and
  a laboratory default together, with the guarantees called over years, reach the $105bn cap on top, and no document on disk lets that joint case be sized
  honestly.
- **Likelihood:** the erosion (demand partly financed by the seller, commitments outrunning a quarter's revenue by 2.9x) is **not a possibility but the
  filed present**. **A FY2023-type pause at today's scale is a real possibility**: two filed pauses in seven years, a one-year cadence that invites buyers to
  wait (*"reduced demand for current generation architectures when customers anticipate transitions"*), and an export regime that has twice turned product
  into write-downs. **A laboratory default that calls the guarantees cannot be placed**: no document states OpenAI's finances, and [E4-40] forbids reading
  the last three years of its fundraising as the guide.

**Against the index (18 shapes, six proposed, as read at 2026-09-13 after the AMZN fold):**
- **#18 THE ROUND TRIP (AMZN, proposed)** is the nearest, and NVIDIA is a **later instance from the vendor's side**: Amazon funds the laboratories and sells
  them cloud capacity it builds with borrowed money; NVIDIA funds and guarantees the same laboratories and the AI clouds, and sells them the chips. **The
  difference is where the loss lands:** at Amazon on plant with five-year lives; at NVIDIA on inventory, forward supply, receivables, stakes and guarantees,
  with almost no plant.
- **#1 CONTRACTED NOT TO STOP (ORCL)** is carried beside it: $279bn of supply and $36bn of buy-backs are commitments the business may not recover.
- **#11 THE PASS-THROUGH (TM)** does not fit the record: gross margin has held at ~75% through the transitions; nothing on file shows gains passed to buyers
  outside the FY2023 channel programs and the H200 tariff it could not pass on.
- **#12 THE ADDRESS (TSM)** applies through the supplier and is carried as exposure.
- **No new shape is proposed.** The FY2023 mechanism (the surfer off the wave [E3-51]) is Q2's finding; the death is what the financing does to it.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *The company survives every mechanism quantified from the filing ([E5-11] 1.5 of 3; [E2-54] met ~90x; owner earnings positive in every window and year).
  Great on operating capital, travelling toward good once the capital committed to customers is counted. The owner-earnings level spans about five times
  (~$26bn on the conservative five-year end to $124bn at the TTM depreciation end), which is a Q5 width. The named death is the round trip from the
  vendor's side on top of $279bn of supply: a real possibility of a capital loss of the order of $144bn in a FY2023-type pause, survivable; a joint pause and
  laboratory default is not sizable from any document. Not a finding against the business, and not what closed this file.*

---

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** **Q2 is OUT; Q5 does not open.** What follows is headed as operator rule 3 requires, and carries no entry language.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Operator rule 3 and the queue's instruction that every run ends with a price. The file closed at Q2 (OUT). Nothing below is an entry signal, a ranking or
a verdict. Working: `q5calc.py`, output `q5calc_out.txt`.*

**The price and what the buyer is paying for, in words.** At **US$218.29 × 24,147M shares = US$5,271.0bn** (Step 0 printed $5,270.9bn; the product is
$5,271,049M, a rounding slip corrected here), the buyer pays **~44 times the best twelve months of owner earnings ever filed** (TTM, capex end, $119.6bn),
**~149 times the five-year default mean** ($35.3bn) and **~278 times the ten-year mean**. Put plainly: the price already pays for **the AI buildout continuing
at something near its present pace for a decade, NVIDIA keeping ~75% gross margins through a new architecture every year against its customers' own chips,
the financed customers staying funded, and no FY2023-type pause**, and it asks nothing of the 10% floor in return for the race Q2 found.

**THE FLOOR, before the ranking [E4-28, E3-13].** Honest pre-tax expectancy at this price, on the arithmetic below: **an owner-earnings yield between 0.5% and
2.4% plus whatever growth the buyer believes**; reaching ~10% needs **7.5-7.6% a year forever from the best twelve months on file, or 9.2-9.5% forever from the
five-year mean**. Below roughly 10% the name is quit on, not ranked.

**1. THE YIELD** (cap $5,271,049M)
| base | owner earnings $M | yield | vs sovereign 5.35% | perpetual growth needed for the 10% floor | for the bond |
|---|---|---|---|---|---|
| 5-yr FY2022-26, stakes, acquisitions and grant-date SBC all as (c) (conservative) | 25,925 | **0.49%** | −4.86 pts | 9.5% | 4.8% |
| 5-yr FY2022-26, SBC at grant-date value | 33,102 | 0.63% | −4.72 | 9.3% | 4.7% |
| **5-yr FY2022-26, (c) = capex + principal (the judged figure)** | **35,332** | **0.67%** | **−4.68** | **9.3%** | 4.6% |
| 5-yr FY2022-26, (c) = depreciation | 36,851 | 0.70% | −4.65 | 9.2% | 4.6% |
| 3-yr FY2024-26, capex end | 56,525 | 1.07% | −4.28 | 8.8% | 4.2% |
| TTM, TTM stake purchases and the full AI cloud backstop as (c) | 62,239 | 1.18% | −4.17 | 8.7% | 4.1% |
| TTM, capex end less acquisitions | 102,545 | 1.95% | −3.40 | 7.9% | 3.3% |
| **TTM, (c) = capex + principal (best judged twelve months)** | **119,645** | **2.27%** | **−3.08** | **7.6%** | 3.0% |
| TTM, (c) = depreciation (most generous judged) | 124,147 | 2.36% | −2.99 | 7.5% | 2.9% |

*Not in owner earnings, and added to value instead so the stakes are not lost:* liquid assets $56.6bn less notes $33.4bn plus stakes at carrying value $99bn
is **~$122bn, about $5 a share**, added to every cell below at most. Marks, not cash; shown once.

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Perpetual growth needed to earn the 10% floor: 7.6% from the best twelve months; 9.3% from the five-year judged mean; 9.5% from the conservative end.**
  To earn merely the bond: 3.0% to 4.8%.
- **DCF engine (casts no vote [E3-34]):** ten years of growth, then 3% forever, discounted at 10%, to equal the cap: **17.8% a year for ten years from the best
  twelve months**, 34.9% from the five-year judged mean, 39.4% from the conservative end.
- **What the business has actually done:** revenue **+46.6% a year FY2017-FY2026** and +68.3% a year FY2022-FY2026; owner earnings (capex end) +60.9% a year
  FY2017-FY2026, from $1.2bn to $90.2bn. **The record beats every growth rate the price needs.** But the record is the wave Q2 described, with FY2020 and FY2023
  inside it, and the question at Q5 is what can be counted on, not what happened.
- **[E4-35]:** *"fewer than 10 of the 200 most profitable companies"* would attain 15% annual EPS growth for twenty years. The engine's **17.8% for ten years
  from the best twelve months ever filed**, then 3% forever, carries that burden in writing, for a company already earning $119.6bn a year of owner earnings and
  whose largest customers are building substitutes (Q2). **[E4-44]:** value cannot outgrow earnings; the price already sits at 44 times the best
  year. **The ceiling [E2-63]:** revenue is bounded by what a handful of hyperscalers and laboratories can spend on compute, and the filings say they cannot all
  finance it (*"currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity"*); price is bounded by Broadcom's
  custom accelerators at a 61% segment margin, Google's TPUs and Amazon's Trainium (the Q2 row).

**3. WHAT YOU ARE PAID**
- **−3.0 to −4.9 points against the sovereign** on today's owner earnings, depending on the window and the (c) judgment. Nothing is paid for the certainty
  question Q2 answered.

**WHERE CERTAINTY IS PRICED: AND IT IS NOT IN THE RATE [E3-42].** Sovereign used **5.35%**, bare. The end margin is the only place certainty is priced
**[E4-11, E4-48]**; it is not needed below, because the price sits above the whole range this run can defend.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:** at the 10% floor, Gordon OE × (1+g) ÷ (0.10 − g), per share (24,147M shares), before the ~$5 of net cash and
stakes:
| owner earnings | g = 0% | 3% | 5% | 6% | 7% | 8% |
|---|---|---|---|---|---|---|
| $25.9bn (5-yr conservative) | $11 | $16 | $23 | $28 | $38 | $58 |
| $35.3bn (5-yr judged) | $15 | $22 | $31 | $39 | $52 | $79 |
| $56.5bn (3-yr) | $23 | $34 | $49 | $62 | $83 | $126 |
| $62.2bn (TTM, stakes and backstop as (c)) | $26 | $38 | $54 | $68 | $92 | $139 |
| $119.6bn (TTM judged) | $50 | $73 | $104 | $131 | $177 | $268 |
| $124.1bn (TTM depreciation end) | $51 | $76 | $108 | $136 | $183 | $278 |

**Conservative: roughly $20-35 a share** (the five-year judged mean at 0-5% forever, with the ~$5) · **optimistic: roughly $135-185** (6-7% forever on the best
judged twelve months, with the ~$5) · **current price $218.29.** The price enters a cell only at **8% a year forever on the best twelve months ever filed
($268-278)**, or at ~7.5% on the same base.

**Set against Q3's buybacks (as computation, not as a verdict on the managers):** the average prices paid imply perpetual growth from the TTM base, at the 10%
floor, of **5.2% ($109.68, FY2025), 6.3% ($143.26, FY2026) and 7.3% ($196.06, H1 FY2027)**. Each purchase sat inside the range, toward or at its optimistic end;
none was at a discount to its conservative end.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **0.5% to 2.4% plus growth, needing 7.5-9.5% perpetual growth** vs ~10% **[E4-28]**; **below → quit on; the ranking
  lines are not filled in.**

**WHICH BAR? Screamer test [E4-01]:** does the price clear the conservative case? **No: the price is six to eleven times the conservative end and above the whole
defensible range.** No margin added. **Windage count one**: the capex end of (c), which is immaterial here (about 4% of owner earnings). The stake and backstop
band, grant-date SBC and the depreciation end are displayed, not used; the scaled FY2023 write-down at Q4 is stated, not stacked.

- **VERDICT: none. Q5 did not open (Q2 OUT).** The computation shows the price above the whole value range at the 10% floor; had every gate been IN, this would
  have failed on price.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

**Pre-committed [E1-02]: reopening conditions, in words, because nothing is owned and nothing is armed:**
- **Why nothing is armed:** the file failed at Q2 on the business; a price alert would be a category error (the QLYS ruling, 2026-09-07).
- **What would reopen Q2 (the error this run most fears [E3-47], and the largest omission cost in the queue if it is one):**
  1. **The substitutes stall on the customers' own filings:** Amazon's Trainium commitments, Alphabet's TPU sales or Broadcom's XPU pipeline cut back or
     cancelled, and Broadcom's semiconductor growth running below NVIDIA's Compute & Networking growth for a full fiscal year. That would move [E3-03]
     criterion (2).
  2. **An architecture transition passes without the write-down:** a full year in which a new generation ships, the prior generation's provisions do not rise,
     and gross margin holds. That would be the first filed evidence that the spending defends the same advantage rather than buying its replacement [E4-04].
  3. **A soft year passes with price held:** a year of flat industry demand in which NVIDIA files no channel pricing programs and its margin stays near its
     prior level, the first [E2-44](1) year on file (FY2023 was the opposite).
  4. **The seller stops financing the demand and the demand stays:** stakes, AI cloud buy-backs and guarantees falling relative to revenue while revenue holds.
  5. **The operator re-scopes [E4-04]** on the TSMC tension by a written structural case (prime rule 5). This run does not make it.
- **What would confirm the close:** transition provisions above the prior year's again; supply commitments rising faster than revenue for a second quarter;
  any AI cloud buy-back or land, power and shell guarantee called; a write-down of a named laboratory stake; filed disclosure that invested or financed
  customers are a large share of revenue; Broadcom's custom-accelerator revenue passing NVIDIA's growth for a full year.
- **Honesty conditions carried from Q3 [E5-16]:** a judgment in 4:18-cv-07669 finding that a named officer knowingly misled would be a personal-misconduct
  matter and would change Q3 from IN to OUT on the binary; a settlement without findings would not.
- **Next catalyst dates:** Q3 FY2027 results (late November 2026; outlook *"Revenue is expected to be $108.0 billion, plus or minus 2%"*, gross margin 74.0%);
  the FY2027 10-K (~late February 2027: the first annual commitments, stakes and AI cloud tables after the new business model); the Hugging Face close
  (*"expected to close in the first half of 2027"*); the first SB Energy phase (fiscal 2029); the class action's trial schedule (not on disk).
- **Sell rule [E2-28] / monitoring [E4-17, E3-30]:** not applicable: nothing owned. Position size: **none**.
- **VERDICT (RECORDED, NOT GOVERNING): not applicable: the file closed at Q2; reopening conditions recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT, the file closed**; Q3-Q6 recorded beneath explicit RECORDED, NOT GOVERNING banners;
  Q5 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN (the killed session's) rests on named filings; the recorded Q3 and Q4
  INs carry no such word. The after-tax operating capital return, the scaled FY2023 write-down and the illustrative half write-down of stakes are labelled
  CONVENTION or illustrative and sit under no IN they could promote.
- [x] Every UNRESEARCHED verdict names the artifact: none issued. The Q2 non-IN verdict was put to the separating test aloud by the killed session (the deciding
  documents exist and were read) → OUT. Q4's one unsizable case (a laboratory default calling the guarantees) is named as what no document states, and it
  does not decide survival.
- [x] Step 0: filing read with accession numbers (the killed session's); figures cross-checked at the resume: every owner-earnings input re-read from the filed
  cash-flow statements across four 10-Ks and two 10-Qs (no vintage differences); the FY2026 and 2026-07-26 balance sheets re-read on the filed faces; the
  screen's D&A traced to its tags (defect 4 below).
- [x] Owner earnings on multi-year means; six windows including one that crosses Mellanox; two plant ends; every out-of-OCF (c) question built both ways
  (stakes, AI cloud buy-backs, guarantees, acquisitions, grant-date SBC, the working-capital build); SBC resolves; the working-capital flag run (fires FY2023
  inventories, H1 FY2027 receivables); [E5-20] asked on the filing and answered there.
- [x] Competitor row filled from filings (the killed session's, `peers/competitor_row.md`), limits stated [E3-61]; not PROVISIONAL.
- [x] Sovereign for the earnings currency, from the issuing authority, dated (USD 30-year 5.35%, US Treasury, 09/11/2026, struck at Step 0 on 2026-09-13; not
  re-struck at the resume, which was the same day and the same latest business day).
- [x] Value stated as a round-number range under the COMPUTATION heading.
- [x] One bar (screamer), windage count one.
- [x] Prices dated; aggregator used for the quote only and flagged (US$218.29, 2026-09-11 close).
- [x] Every ledger id cited in the file checked against `principle_ledger.csv` by `cite_check.py` before each commit (none missing).
- [x] Run committed to git with a pathspec at each stage (Step 0 `1efd45d`, Q1 `03875d1`, Q2 `b65758e` by the killed session; Q3 `364515f`; Q4 `af0c27f`;
  Q5-Q6, audit and register in the next commit).

**Errors of the killed session and of mine, recorded rather than smoothed:**
1. **Killed session: the Step 0 market cap reads $5,270.9bn; 218.29 × 24,147M is $5,271.0bn** ($5,271,049M). Left in Step 0 as committed history; corrected
   at Q5.
2. **Killed session: the Q2 provisions series ($2.17bn FY2023, $3.7bn FY2025, $7.2bn FY2026) skips FY2024's $2.2bn**, and FY2022's $354M. Every year on file
   carries a provision, which strengthens Q2's [E4-04] reading rather than weakening it. Corrected at Q3 and Q4.
3. **Killed session: the FY2017 and FY2019 10-Ks were fetched through `fetch.py`'s ad hoc branch, which records no accession**; recovered from companyfacts
   (`0001045810-17-000027`, `0001045810-19-000023`) and written into Q4.
4. **Mine, caught before commit:** a first draft said Hugging Face was "paid in cash"; the 8-K does not say so (0 hits for "cash"). A first draft quoted the
   framework's gloss of [E3-29] as if it were the ledger text, and put [E5-22]'s summary in quotation italics; both reworded. A first draft misquoted the proxy's
   PSU wording and the 10-Q's customer-advance footnote; both replaced with the filed text. A first draft called a six-month rise in operating capital a TTM
   increment; corrected.
5. **Mine, a judgment to flag:** Q3's after-tax operating-capital return uses a 15% tax rate for FY2017-FY2023 where the filed rate was not extracted
   (CONVENTION, confessed in the table note). It changes no reading: the series is above 100% in most years on any plausible rate.

**Tooling and brief defects found:**
- **Step 0's three stand** (`cover_shares.py` read the CIK as a share count; `deal_filings()` cannot see an 8-K Item 8.01 acquisition; the screen's D&A end
  includes acquisition-intangible amortization).
- **4 (new). `floor_screen.da_annual()` replaces a filed D&A total with a sum of ROUNDED components.** NVIDIA tags `Depreciation` from the note's rounded
  *"$2.4 billion"* and *"$1.3 billion"* (2,400 and 1,300) and `AmortizationOfIntangibleAssets` exactly (488 and 593); the sums (2,888 and 1,893) exceed the
  filed cash-flow total `DepreciationDepletionAndAmortization` (2,843 and 1,864), and the rule *"a filer that tags both is trusted on its own total unless the
  components plainly exceed it"* is coded as `v > abs(out[e])` with no tolerance, so a $45M rounding excess overrides the filed statement. That is why
  `run.py`'s D&A column (1,893; 2,888) matches no line NVIDIA filed. 1.6% here; on a filer that rounds to the nearest tenth of a billion with a small total it
  would not be. Not fixed (this run edits no tool).
- **5 (new, process). The "capex unresolved" label had a second NVIDIA-specific cause the AMZN note did not cover:** companyfacts carries no capex fact for
  FY2013-FY2021 at all (Step 0), so any window longer than five years still needs the hand build done here, even after the tag-union fix.
- **Brief errors:** (a) it grouped *"capacity buy-back agreements ($36bn AI cloud, $29bn cloud service)"*: **the $29bn cloud service agreements are not
  buy-backs**; the 10-Q says they *"provide the cloud infrastructure to support our research and development of our open models"*; only the $36bn AI cloud
  agreements are tied to partners' purchases of NVIDIA systems. (b) It asked whether transition provisions belong in (c); **they are already inside OCF**, and
  putting them in (c) would count them twice (Q4). (c) Its provisions list copied the Q2 series that omits FY2024 (above). (d) It listed FY2018 and FY2020
  10-Ks as possibly needed; **no window needed them**, because each 10-K carries three years of cash flows. Everything else checked (the $25.0bn notes, the
  $105bn cap, $36bn, $99bn and $25bn commitments, SBC $6,386M, other income $24,140M, ROE 101.5%, Groq ~$17bn, Hugging Face $11.9bn, the Mellanox year, the
  disk inventory, the last three fetches) matched.
- Research dumps follow the gitignored patterns (`10K_`, `10Q_`, `8K_`, `DEF14A`); `companyfacts.json` and `submissions.json` match no ignore pattern and were
  left uncommitted by pathspec, as at AMZN.

---
## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line: FAIL at Q2 (OUT on [E4-04], with [E3-03] criterion 2 as the customers' filings test it): a one-year architecture cadence whose every transition
  leaves a write-down ($354M FY2022 to $7.2bn FY2026), customers contracting substitutes at gigawatt scale, a rival filing 20+ GW of custom accelerators, and
  ~$17bn paid to license a rival design; a surfing run at its best. Q1 IN. Price US$218.29 × 24,147M = US$5,271.0bn; COMPUTATION — NOT A CLEARANCE: owner
  earnings $35.3bn on the five-year default (~$26bn to $36.9bn across (c)), $119.6bn TTM (~$62bn to $124.1bn), yield 0.5% to 2.4% against USD 5.35%, 7.5-9.5%
  perpetual growth needed for the 10% floor, value roughly $20-35 (five-year judged) to $135-185 (6-7% forever on the best judged year) a share; price above the
  whole range.**
- If UNRESEARCHED: not applicable. If UNKNOWABLE: not applicable (Q3 recorded IN on the binary; Q4 recorded IN on survival).
