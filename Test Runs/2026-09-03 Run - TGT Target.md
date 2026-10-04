# Company Run — Target Corporation (TGT) — 2026-09-03
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Research folder: `Test Runs/_research 2026-09-03 TGT/`. Write-early protocol in force:
each section written as it closes, committed after every question.*

**The [E4-26] prior, declared before the evidence was pulled (from the operator's brief):**
the expected shape is the KR run — Q2 OUT on [E3-03](2), no consumer franchise in a general
merchant whose customer re-chooses weekly on price and convenience — with the deflated
physical series convicting. The declared counter-case to hunt hardest: owned-brand
penetration ~1/3 of sales at above-company margins, RedCard/Circle data, and the fact that
COST cleared these gates from adjacent retail. **If the traffic series is positive and real
productivity is rising, the claim is taken seriously.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — currently observed, never a forecast
**[E4-15, E3-32]**:
- rate **5.27%** · date **2026-09-02** · source **US Treasury daily par yield curve, 30-year,
  issuing authority** (`tools/sources.py`, fetched 2026-09-03)
- FX: none — TGT earns, reports and quotes in USD. Single class of common stock.

**Price and count:**
- price **$164.01**, 2026-09-03, **aggregator — live quote only, flagged as such**
- shares **454,296,736** — hand-read off the Q2 FY2026 10-Q cover (filed 2026-08-28, as of
  cover date), single class, par $0.0833, via `Screens/cover_shares.py` and verified against
  the filing. Balance-sheet count at FY2025 year-end: 452,840,187 issued and outstanding.
- **market cap $74,509M** (= 454,296,736 × $164.01)

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A (executive overview, comparable-sales decomposition, gross margin, SG&A, ROIC,
  liquidity, capex, dividends, buybacks, critical estimates)
- [x] cash-flow statement including detail lines (D&A, SBC, deferred taxes, inventory, AP,
  finance/operating-lease supplemental lines, interest and the lease-addition lines)
- [x] footnotes (Note 2 revenue, Note 6 interchange settlements, Note 7 business
  transformation, leases, debt, taxes, pension, buyback)
- documents:
  - **Form 10-K FY2025 (52 weeks ended 2026-01-31), filed 2026-03-11, accession
    0000027419-26-000016** — the primary document of this run
  - **Form 10-Q Q2 FY2026 (13/26 weeks ended 2026-08-01), filed 2026-08-28, accession
    0000027419-26-000042** — freshness: latest comps, traffic, tariff-refund state
  - **DEF 14A filed 2026-04-27, accession 0001628280-26-027508** — pay vs performance
  - Older 10-K vintages for the ten-year physical series, listed at Q2
- figure cross-checked against the filed statement: **FY2025 operating cash flow $6,562M** —
  identical in the XBRL tag, `tools/run.py`, and the filed Consolidated Statements of Cash
  Flows ("Cash provided by operating activities | 6,562").

### STAGE 0(b) — THE SCREEN ROW, REPRODUCED BEFORE ADJUDICATION (operator instruction)

Queue row (2026-09-02 corrected): cap 73,973 · OE 2,475–4,260 · spread **72.1%** · yield
3.35% · growth required 6.65% · "no step" · best-year dependence 0.055.

**Reproduced to the million, both boundaries, from the filed series:**
- **Bottom 2,475** = 5-yr mean (FY2021–25) of OCF − SBC − (cash capex **plus finance-lease
  ROU additions**): (4,853 + [−1,730] + 3,564 + 4,172 + 2,554)/5 = 2,682.6, less the 5-yr
  mean of finance-lease additions (288+224+104+319+104)/5 = 207.8 → **2,474.8** ✓
- **Top 4,260** = 3-yr mean (FY2023–25) of OCF − SBC − D&A: 7,238.0 − 2,978.3 = **4,259.7** ✓
- yield 2,475/73,973 = **3.346%** ✓ · growth required 10% − 3.35% = **6.65%** ✓

**WHY the spread is 72.1% — the [E4-25] question, answered before any mean is trusted:**
1. **FY2022 (ended 2023-01-28) sits inside the 5-yr window and it is the inventory-glut
   year**: OCF fell to **$4,018M** (against $8,621M the following year) while capex peaked
   at **$5,528M** — the capex-end construction for that single year is **−$1,730M**.
2. **The capex band itself is wide because capex swung 2,891 → 5,528 across the window**
   (supply-chain build + remodel program), against D&A of 2,700–3,134. Capex/D&A ran 0.97x
   to 2.05x within five years. The gap between the 5-yr capex end and the 3-yr D&A end IS
   the maintenance-capex question, and it is adjudicated at Q4, not by the screen.
3. The 3-yr top excludes both the FY2021 boom and the FY2022 bust — a calmer window at the
   friendlier (c) end.
**So the 72.1% spread is real, diagnosable, and window-driven [E5-11]: a distorted year sits
in the window. It does not by itself void the mean; Q4 names the distortion and judges (c).**

**Tool defect logged:** `Screens/floor_screen.py TGT` crashes today in `chart_events`
(`OSError: [Errno 22] Invalid argument` at `date.fromtimestamp(ev["date"])`,
line 174) — the row above was reproduced by hand from companyfacts instead. Defect class:
share_count_shift → chart_events on this filer; queue row of 2026-09-02 was produced before
the crash appeared.

### STAGE 0(b) — THE DIVIDEND CLAIM, VERIFIED BY HAND (operator instruction)

The brief: "TGT claims 50+ years of increases: verify and run the RPM decomposition."
- **What the 10-K actually claims (FY2025, MD&A):** *"We have paid dividends every quarter
  since our 1967 initial public offering, and it is our intent to continue to do so in the
  future."* — a **payment** streak claim, not an increase streak claim, in this filing.
- **The increase record, from the filed statements (dividends declared per share):** $4.38
  (FY2023) → $4.46 (FY2024) → $4.54 (FY2025), +1.8%/yr in each of the last two years. Paid
  per share: $4.36 → $4.44 → $4.52. The ten-year declared series (filed statements of
  shareholders' investment, 10-K vintages): 2.20 / 2.36 / 2.44 / 2.54 / 2.62 / 2.68 / 3.38 /
  4.14 / 4.38 / 4.46 / 4.54 (FY2015→FY2025) — **rising every year in the filed decade**;
  the >50-year claim rests on company history predating EDGAR and is carried as the
  company's claim, not this run's finding.
- **RPM decomposition (earnings vs payout expansion vs retirement), FY2020→FY2025:**
  DPS +69% ($2.68 → $4.54). Decomposed: **net earnings FELL** ($4,368M → $3,705M, −15%);
  payout ratio **rose from 30.7% to 56.5% of net earnings** (declared $2,095M/$3,705M);
  share count fell 504.2M → 452.8M (−10.2%, and almost all of that retirement happened in
  FY2021–22 at $7.4bn+$2.8bn spent at prices far above today's). **The five-year dividend
  growth is roughly two-thirds payout expansion, one-sixth retirement, and NONE earnings**
  — the PEP shape, milder. Over ten years (FY2015→25) earnings did contribute (NI $3.4bn →
  $3.7bn) but the recent five are payout-funded. Recorded for Q3/Q4.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** Target buys general
  merchandise and groceries at wholesale, marks them up to a **27.9% gross margin**, and
  sells them through 1,995 big-box stores (250.5M retail sq ft) plus a website whose orders
  the stores themselves fulfill (>97% of all merchandise sales fulfilled by stores). Roughly
  **46% of merchandise sales are discretionary categories** (apparel $15.7bn, home $15.6bn,
  hardlines $15.8bn) — the mix that distinguishes it from Walmart (grocery-anchored) and
  Costco (membership-anchored) — and ~30% of merchandise sales are owned/exclusive brands
  that carry higher margins. On top of the merchandise engine sit three tolls: **Roundel
  advertising ($915M, growing fast), TD credit-card profit sharing ($522M, shrinking since
  the receivables were sold to TD), and marketplace/membership fees (~$626M other)**. It
  earns ~4.6–4.9% operating margin on ~$105bn of sales; suppliers finance most of the
  inventory (AP $12.6bn vs inventory $12.3bn); fiscal year peaks at Christmas.
- **The scarce input this business controls:** its trademark and design reputation
  ("Expect More. Pay Less.", the owned-brand stable) and 1,995 located boxes. It does NOT
  control price (set by Walmart/Amazon comparison shopping, conceded in its own risk
  factors), does not control its credit card (TD owns the receivables), and does not
  control the supply of anything it sells.
- **Will the fundamentals look broadly the same in ten years?** Yes — general-merchandise
  discount retail through stores plus digital, a format Target has run since 1962. The
  format's *position* is the Q2 question; the *understandability* is not in doubt. [E4-46]
  five-minute test passes; this is the seventh specialty/general retailer this project has
  run in eight days.
- **VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

*The operator's central question, run at length with the counter-case at full strength
[E4-51]. Full data pack: `_research 2026-09-03 TGT/TGT filed data - physical series and
decomposition.md`. Target sits structurally between KR (Q2 OUT) and COST (Q2 IN, WIDE):
no membership annuity, no fuel, no pharmacy, higher discretionary mix — but a real
owned-brand and design differentiation claim that KR never had.*

- Needed or desired **[x]** — general merchandise and groceries; ~54% of merchandise sales
  are staples (food & beverage, household essentials, beauty), ~46% discretionary.
- Not price-regulated **[x]** — met. (No pharmacy: CVS operates the pharmacies in Target's
  stores under a perpetual agreement; Target collects occupancy income instead. The KR
  IRA-reimbursement problem does not exist here.)
- **No close substitute [ ] — FAILS, on the filer's own words and the filed record below.**

### The subject's own statement of criterion 2

The entire Item 1 competition disclosure, verbatim (FY2025 10-K, acc 0000027419-26-000016):

> "We compete with omnichannel retailers, including department stores, off-price general
> merchandise retailers, wholesale clubs, category-specific retailers, drug stores,
> supermarkets, direct-to-consumer brands, online marketplaces, and other forms of retail
> commerce. **Our ability to positively differentiate ourselves from other retailers and
> provide compelling value to our guests largely determines our competitive position within
> the retail industry.**"

And the risk factor states what bounds the differentiation:

> "Since consumers can quickly comparison shop using digital tools, **they may make
> decisions based solely on price or convenience, which could limit our ability to
> differentiate from our competitors.**"

Nine named substitute classes, and a filed concession that the differentiation can be
overridden by a phone. That is the same self-denial the KR run found, one register milder.

### The deflated physical series — the decisive instrument, both halves reported

**Sales per square foot (computed — Target has NEVER published this metric; Item 6 of the
FY2016 10-K carries no per-square-foot line — stated per the absence-claim rule from a
sweep of eight vintages).** Merchandise sales ÷ average retail sq ft, CPI-U deflated
(BLS CUUR0000SA0, as recorded in the DG run; FY2023 ×52/53, CONVENTION):

| fiscal | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|---|---|---|
| nominal $/sqft | 300 | 311 | 321 | 383 | 431 | 441 | 423 | 424 | **412** |
| **real, 2025 $** | 394 | 398 | **405** | 477 | **513** | 485 | 447 | 435 | **412** |

**Four consecutive real declines from the FY2021 peak (513 → 485 → 447 → 435 → 412,
−19.6%).** But the level test is honest and it does NOT convict on the DG standard: FY2025
real productivity sits **+1.8% ABOVE pre-pandemic FY2019** and +4.6% above FY2017. DG was
9–10% *below* its pre-pandemic level; ANF was +37% above. Target is a boom fully given
back, not a structurally shrinking box. **The sq-ft instrument alone reads: direction
guilty, level acquitted.**

**The sharper physical instrument is the one Target itself files: the comp decomposition
[E2-44 first half / E4-55]. Twelve years of traffic vs ticket:**

| fiscal | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** | **H1-26** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| comps | −0.5 | +1.3 | +5.0 | +3.4 | +19.3 | +12.7 | +2.2 | −3.7 | +0.1 | **−2.6** | **+4.7** |
| traffic | −0.8 | +1.6 | +5.0 | +2.7 | +3.7 | +12.3 | +2.1 | −2.4 | +1.4 | **−2.2** | **+4.0** |
| ticket | +0.3 | −0.3 | +0.1 | +0.7 | +15.0 | +0.4 | +0.1 | −1.4 | −1.3 | **−0.4** | **+0.7** |

- **Real comparable sales were negative FOUR consecutive years: −5.4% (FY2022), −7.5%,
  −2.8%, −5.1% (FY2025) — roughly −19% of real comparable volume, cumulatively.**
- **[E2-44]'s question — "can it raise prices even when demand is flat?" — is answered by
  the ticket row: NO.** When volume left (FY2023–25), **nominal average ticket fell three
  consecutive years (−1.4, −1.3, −0.4) against +10.0% cumulative CPI**. Price did not hold
  when volume left; both series fell together. Contrast the same three years elsewhere:
  Walmart U.S. grew ticket AND transactions AND unit volumes; even DG held ticket positive.
- **The FY2022 record is the filed proof of what discretionary pricing power Target has:
  one misjudged inventory season took the gross margin rate from 28.3% to 23.6% and the
  operating margin from 8.4% to 3.5%** — $5.1bn of operating income gone in a year, cleared
  by markdown. The FY2025 10-K still concedes the mechanism as a live risk: *"We have not
  always been able to accurately forecast consumer demand … which has previously resulted
  in insufficient or excess inventory, increased inventory markdowns."* A franchise marks
  its price up when it errs on inventory; a merchant marks it down. Target filed which one
  it is.

### [E2-44] second half — dollar volume against capital, and [E3-62]

- Revenue FY2021 → FY2025: **$106,005M → $104,780M (−1.2%)** on **$16.95bn of capex**
  (FY2022–25). Four years of capital, negative dollar growth.
- The seven-year frame is worse for the claim: **revenue +34.1% (FY2019 → FY2025, +$26.7bn)
  against adjusted operating income +2.5% (+$117M: $4,658M → $4,775M)** — an incremental
  operating margin of **0.4%**. [E3-62]: the vendor projections showed the savings; the
  question *"how much is going to stay home"* is answered — **nothing stuck to the ribs.**
  Gross margin FY2025 (27.9%) sits 100bp below FY2019 (28.9%) despite ~30% owned brands
  and $915M of high-margin advertising revenue now landing in the P&L.

### Direction outranks existence **[E4-32]**, and the number **[E3-46]**

- Company's own after-tax ROIC: **15.4% (TTM Feb-2025) → 13.8% (TTM Jan-2026, including
  +0.8pt from the interchange gain net of transformation costs → ~13.0% underlying)**.
  Recovering to 15.4% TTM Aug-2026 — with the $994M tariff refund inside it.
- **[E2-43] return on unleveraged net tangible operating assets, computed:** assets 59,490
  − cash 5,488 − goodwill 631 = 53,371; less non-debt operating liabilities 23,407 →
  **NTOA $29,964M**; adjusted after-tax operating profit 3,710 → **12.4%** (13.3% GAAP).
  A good return, [E5-40]'s "quite satisfactory" band — **not** "very high returns on
  capital employed over time," and falling: the FY2021-era return on a smaller base was
  far higher (op income $8,946M on a ~$26bn base).
- Owned/exclusive-brand penetration — the moat candidate's own series, by filed wording:
  **"approximately one-third" (FY2016, FY2019, FY2022 10-Ks) → "approximately thirty
  percent" (FY2025 10-K).** Drifting down, not up.
- Credit-card profit sharing: **$667M → $576M → $522M** — the data/loyalty toll is
  shrinking, three years running.

### THE COMPETITOR ROW — required **[E3-28]**; same metric, same window, filing-sourced

Sources: WMT FY2026 10-K (`_research 2026-08-26/WMT_10K_FY2026.txt`), COST FY2025 10-K
(same folder), KR FY2025 10-K per the KR run (acc 0001104659-26-037723), DG FY2025 10-K
per the DG run (acc 0001104659-26-032325). Fiscal years ending 2026-01-31 (TGT, WMT, KR)
or 2026-01-30 (DG); COST 2025-08-31.

| | **TGT** | **Walmart U.S.** | **Costco** | **Kroger** | **DG** |
|---|---|---|---|---|---|
| net sales $M | **104,780** | 482,975 | 269,912 | 147,642 | 42,724 |
| GAAP op margin | **4.9% (4.6% adj)** | **5.2%** | 3.85% | 1.28% (3.32% adj FIFO) | 5.16% |
| comps, latest FY | **−2.6%** | **+4.3%** | **+6%** (+8% ex gas/FX) | +2.9% ex-fuel | +3.0% |
| comps, prior two FYs | **+0.1 / −3.7** | +4.8 / +5.5 | +5 / +6-range | +1.5 / +0.9 | +1.4 / +0.2 |
| physical direction | **traffic −2.2%; real comps −5.1%** | *"growth in unit volumes"* | frequency **+5%**, members +6.3% | units NEGATIVE (filed) | traffic +1.6, ticket +1.4 |
| store base | 1,978 → **1,995** | **4,611 (flat 3 yrs, 699M sqft flat)** | 914 (+24) | 2,697 (shrinking) | 20,893 (+299) |
| prepaid member annuity | ~$0 (Circle 360 not quantified) | Walmart+ inside $2.6bn memb.+other | **$5,323M fees, 92.3% renewal** | none | none |
| [E2-43] NTOA return, after-tax | **12.4% (adj)** | ~17–18% consolidated¹ | ~35%+² | 15.8% | 8.6% (lease-incl, DG run) |
| own-brand quantified? | **yes ~30%, wording downgraded** | no (Great Value not quantified) | no (Kirkland not quantified) | yes ">$39bn" ≈29% | no |

¹ WMT does not allocate liabilities by segment, so a Walmart-U.S.-only NTOA cannot be
built from the filing; consolidated: assets 284,668 − cash 10,727 − goodwill 28,735 −
(AP 63,061 + accrued 31,187 + deferred/other 16,549) ≈ $134bn; op income 29,825 × ~0.77
≈ 23.0bn → ~17% — and the U.S. segment (5.2% margin vs 4.2% consolidated, segment assets
$165.6bn) is the *better* half. ² COST: assets 77,099 − cash+STI ~15.3bn − goodwill ~1.0
− (current liabilities ex-debt ~37.0 + other LT ~2.6) ≈ $21bn; op income 10,383 × ~0.75 ≈
7.8bn → ~35%+ (its profit pool is half membership fees on near-zero incremental capital).
- **Peers named: 4 of the ~6 the industry has at scale** (the four the operator ordered;
  Amazon is taken qualitatively below — its GAAP segments do not produce a comparable
  NTOA row for US general merchandise; TJX/BJ's not taken, stated). **No peer unavailable
  — nothing PROVISIONAL.** Aldi/Trader Joe's private, recorded as in the KR run.
- **The row's limit [E3-61]:** position, not conduct; identical structures produce
  opposite outcomes, and comp definitions differ across filers (stated in the DG row).

**What the row establishes:** same fiscal year, same twelve months, same country —
**Walmart U.S. comps beat Target's in each of the last three years (+5.5/+4.8/+4.3
against −3.7/+0.1/−2.6), on growing unit volumes, from a store base flat for three years,
at a higher operating margin (5.2% vs 4.6% adjusted).** Costco compounded frequency +5%
on a 92.3%-renewal prepaid base. Kroger — the run this one was benchmarked against — beat
Target's comps in all three years too (+0.9/+1.5/+2.9 ex-fuel), albeit at a fraction of
the margin and with falling units of its own. **Target lost share of trips to the price
leader above it, the club annuity beside it, and the grocer below it, simultaneously,
for three consecutive years.** The DG run's finding — "the attack is coming through the
delivery van" — replicates: Walmart built nothing and took the traffic.

### The attacker's test **[E2-45]**

With ample capital and skilled personnel, how would I attack Target? **The attack is not
hypothetical; the record is filed.** Walmart attacked the value flank from a flat store
base and won three straight years of comps on positive units. Amazon attacked the
convenience flank — Target's own risk factor now names dependence on *"the capabilities
and search algorithms of those third parties"* as a competitive risk, and Target's
response was to *join* the marketplace model (Target Plus) and to sell same-day delivery
through Shipt. Costco attacked the stock-up trip with a fee wall Target cannot replicate
without destroying its format. **The discretionary middle — design-led apparel and home
at a markup over Walmart — is exactly the slice that shrank: home furnishings & décor
−12% in two years ($17,760M → $15,608M), apparel −4.7% in FY2025.** The attacker does
not need a plan; three of them are already through the gate.

### What has Target stopped publishing? **[E2-49]** — it fires, dated

- **RedCard Penetration** — published annually for years, *"we monitor the percentage of
  purchases that are paid for using RedCards … because … a meaningful portion of
  incremental purchases on our RedCards are also incremental sales"*:
  **24.5% (2017) → 23.8 → 23.3 → 21.5 → 20.5% (2021) — four consecutive declines — then
  the table and the metric were WITHDRAWN in the FY2022 10-K** (zero occurrences of
  "Penetration"; by FY2025 zero RedCard content of any kind, the cards rebranded Target
  Circle Card). The exact HD/DKS pattern the brief predicted: a yardstick discarded while
  yielding unfavorable readings.
- Target Circle membership counts: not disclosed in any 10-K vintage read (the loyalty
  base the bull case cites is not filed at all).
- Sales per square foot: **never published in any vintage read** — so no withdrawal
  (absence-claim rule: sweep of FY2016–FY2025 vintages).
- Fair recording of the other side: the traffic/ticket decomposition — the most damaging
  table in the filing — **is still published every year**, and the credit-card
  profit-sharing decline is disclosed plainly. The candor read at Q3 credits this.

### The moat candidates, tested at full strength — and the H1 FY2026 recovery **[E4-51]**

**This is the strongest counter-case in the retail cohort since COST, and it is stated
before it is answered.**

1. **The traffic series turned positive in the newest half-year — the brief's declared
   trigger for taking the claim seriously.** Q2 FY2026: comps **+3.8%** (traffic **+3.6**,
   ticket +0.2); H1: comps **+4.7%** (traffic **+4.0**); stores-originated comps +2.7/+3.7;
   digital +8.7/+8.8. Underlying operating income **+19% ex-refund in Q2** (+~23% H1
   ex-items); gross margin +~100bp underlying; TTM ROIC back to 15.4% (refund-assisted).
2. **Owned brands at ~30% of $102.7bn is a $31bn own-brand complex** — bigger than
   Kroger's $39bn claim in quality-of-margin terms, the largest *designed* (not
   price-tier) own-brand stable in US retail, with return privileges (one year vs 90
   days) the national brands don't get. Beauty — the category Ulta and Sephora fight
   over — grew straight through the downturn ($12,538M → $13,214M).
3. **Roundel is real and compounding: advertising revenue $522M → $649M → $915M (+41%),
   non-merchandise sales +20.1% in Q2 FY2026** — high-margin, data-driven, the KR
   alternative-profit finding with better growth.
4. The FY2025 traffic decline carries a **named exogenous component**: the 10-K itself
   files *"consumer boycotts organized throughout 2025"* over the DEI rollback, on top of
   the 2023 Pride-assortment boycotts. Part of −2.2% was punishment, not preference — and
   part of H1 FY2026's +4.0% is its lapse.
5. Balance sheet and conduct: $5.4bn cash, A2/A/A, no CP outstanding at any point in two
   years, buybacks executed at $106–115 and **zero at $164** — price discipline the ORLY
   run would envy.

**Why it still fails [E3-03](2).** Every item above is real, and none of it is a consumer
franchise:
- The H1 FY2026 half-year sits against a base its own filing calls boycott-depressed, and
  the two-year traffic stack (+4.0 on −1.8) is ~**+1.1%/yr** — against Walmart U.S.
  compounding +4–5% on positive units for three years. One recovering half against three
  structural years; [E4-17]'s "beliefs change quite gradually" cuts against promoting it,
  exactly as it cut against convicting ANF on two soft quarters.
- The moat candidates are all **riders on store traffic, not owners of it** (the KR
  finding, restated): Roundel sells access to Target's shoppers — *"our advertisers do
  not have long-term commitments with us"* (Item 1A, filed); the card income shrinks as
  the card base shrinks; the own brands are exclusive to a store the customer must first
  choose to enter, and the customer's commitment instrument is **zero** — no fee, no
  membership, no switching cost. Costco's shopper prepays $65–130 for the right to shop;
  Target's shopper re-decides every trip against a phone, and the filer says so.
- The two-characteristic test [E2-44] failed on filed arithmetic — price did NOT hold
  when volume left (three years of falling nominal ticket), and dollar volume did not
  grow on $17bn of capital.
- The slow variables all point one way: own-brand penetration wording down, RedCard
  penetration withdrawn after four declines, credit income −22% in two years, gross
  margin 100bp below pre-pandemic, adjusted operating margin 4.6% vs 6.0% (FY2019),
  ROIC 15.4% → 13.0% underlying. **[E3-30]'s question — aberrational cycle or permanent
  slip? — is answered by seven years of zero adjusted operating-income growth across two
  full cycles, not by the newest two quarters.**
- [E4-23] key-person: LOW — recorded in the business's favor. [E4-04]: the moat basis —
  trend-right assortment — must be **re-earned every season** (*"A large part of our
  business is dependent on our ability to make trend-right decisions"*), and FY2022 filed
  what one season's lapse costs: 4.7 points of gross margin. A basis that a single
  season's misjudgment can breach for $5bn is defended spending, not structure.
- Untapped pricing power [E3-33]/[E5-28]: claiming it would claim near-monopoly; the
  filer concedes decisions are made *"solely on price or convenience."* No.
- Dominance class [E2-53]: no — Target prospers or not according to Walmart's price file,
  the container schedule, and the consumer cycle, as FY2022 demonstrated.

- Class: **[x] NONE at the enterprise level** — with two genuinely narrow assets inside
  it (the owned-brand/design complex; Roundel) that ride on traffic they do not control,
  plus best-in-cohort disclosure candor. Direction: **NARROWING** on the slow variables
  (own-brand share, card penetration/income, margins, ROIC, real productivity), with one
  recovering half-year at the end of the series.
- **VERDICT: [x] OUT.** Fails **[E3-03] criterion 2** on the filer's own competition
  disclosure and the filed behavior of its customers (three years of traffic loss to
  three different attackers at once); fails **both halves of [E2-44]** on filed
  arithmetic; fails **[E4-32]** direction; **[E2-49]** fires, dated. The H1 FY2026
  recovery is recorded at full strength and does not constitute a franchise — a
  franchise is a structure, not a good half. **[E5-13]: most names should end here, and
  that is the system working. The sixteenth Q2 closure in this queue's history.**

---
⛔ **Q3, Q4 and Q5 do not open for entry. Q1 IN · Q2 OUT.** The hard sequence closes the
file for any BUY decision. Everything below is **FOR THE RECORD** because the operator's
brief tasked the earned tests regardless (Stage 0 dividend decomposition is above; pay vs
performance, [E4-52], [E2-60], [E5-11], ASC 842, the (c) direction and the named death
follow). **Everything below operator rule 3's header: COMPUTATION — NOT A CLEARANCE.
Nothing below is entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless — Q3 can
stop a run, never start one.*

### STEP 1 — THE WEIGHT CASE, declared first
- [ ] Daily execution · [ ] Control · [ ] Leverage — **none ticked → Q3 is a qualitative
  OVERLAY.** Leverage is modest (net debt ~$11.1bn against $16.2bn equity and 8.1x EBIT
  interest cover); no control position; merchandising is season-by-season execution, but
  the business absorbed its own worst season (FY2022, −4.7pts of gross margin) with A
  ratings intact — [E5-18]'s capacity-to-stand-it, demonstrated on the record.

**Honesty — the binary [E5-16]:** no integrity disqualifier found in the filings read. The
2013 data breach (operational, disclosed, litigated, resolved) and the 2023/2025
boycott controversies are conduct-of-business matters, not personal misconduct. CEO
transition orderly and internal: Fiddelke (CFO 2019–24, COO 2024–26) CEO from February
2026; Cornell to Executive Chair. *A Q3 pass is the absence of found disqualifiers, not a
finding that the managers are honest [E5-17].*

### STEP 2 — THE FLAGS
- [ ] weak accounting — none found; LIFO retail method; the one estimate worth naming is
  the pension expected long-term return of **7.20%** (a plan of ~$360M sensitivity per
  point; noted as a prompt, small in context).
- [ ] unintelligible footnotes — no; the disclosure is among the cleanest in this cohort.
- [x] **trumpeted projections [E3-48], with the record run:** Target guides annually. The
  filed base-rate check: FY2025 STIP goals (set March 2025) were **Net Sales $108,567M
  (+1.9% over prior actual) and Incentive Operating Income $6,362M (+6.1% over prior
  actual)** — outturn $104,780M and $5,140M, **both missed**. The 10-K's own risk factor
  concedes the forecasting record: *"We have not always been able to accurately forecast
  consumer demand."* Not a promotion flag — goals were set above actuals and missed
  honestly — but the projections exist and the FY2022 collapse is what missing them costs.
- [ ] serial share issuance — **no**: 504.2M → 452.8M shares over five years.
- [ ] **EBITDA [E4-29]: ZERO occurrences in the FY2025 10-K, the Q2 FY2026 10-Q, AND the
  proxy.** The third filer in this project (after ULTA and MCD-proxy) to manage it.
- [ ] filed-figure tells [E4-30]: growth is conspicuously NOT smooth (NI $6,946M → $2,780M
  → $4,138M); cash taxes paid as a share of pretax dipped to ~6–7% in FY2022–23
  (bonus-depreciation timing) and **recovered to 20.1% / 22.9%** in FY2024–25 — acquits.
- [E4-52] restructuring streak: **does not replicate on Target.** One instance — the
  FY2025 "business transformation" at **$250M**, with *"we may incur additional … costs
  and charges in future periods"* filed beside it. A watch item ([E5-33]: the costs are
  real, and they sit inside the OE mean below), not a streak. Contrast PEP's 12
  consecutive years.
- [E2-49] in pay-land: PSU metric switched Merchandise Sales → Net Sales in 2025,
  disclosed with the reason, applied prospectively — the announced-ahead case, not the
  disposition-of-the-yardstick case. The RedCard withdrawal is already charged at Q2.

### STEP 3 — THE PRIMARY TEST [E2-01], and the pay-for-performance record
- Earnings rate on equity: NI/avg equity = **24.4% (FY2025)**, 29.2% (FY2024) — flattered
  by buybacks shrinking the book; the honest denominator [E2-43] gives **12.4% after tax
  on $30.0bn of unleveraged net tangible operating assets**, and the company's own ROIC
  reads **15.4% → 13.8% (13.0% ex one-times)**. Good, not great, and falling.
- **The DG/ULTA pay-rigging pattern does NOT replicate — the anti-pattern, verified:**
  goals set ABOVE prior actuals; STIP paid **44.6% of goal** (financial component 42%,
  scorecard 50%); three-year payouts **93.4% / 83.0% / 44.6%** — variable and tracking
  results down. **And the incentive measure was adjusted SYMMETRICALLY: "For Fiscal 2025,
  we excluded the net gain from interchange fee settlements, as well as business
  transformation costs"** — management excluded a $593M windfall GAIN from its own bonus
  metric. That is the [E2-26] half-owner standard applied to their own pay.
- **The filed Item 402(v) table is the five-year verdict on capital results: $100 invested
  2021-01-30 → $66.89 (FY2025) against the 17-company retail peer group's $176.65.**
  Target trailed its own peer group in three consecutive years and destroyed a third of
  the investment over five. CAP tracked it (CEO: $57.8M in 2021, −$9.6M in 2022, $7.8M in
  2025) — the pay system is honest; the results it measured are poor.
- **[E3-54] retention FAILS the five-year window:** ~$12.1bn retained (FY2021–25 earnings
  less dividends) against a market value that FELL — cap ~$90bn (Jan 2021, ~500.9M sh at
  ~$181) → $74.5bn today even after a +65% 2026 rally. Roughly **$0 of market value per $1
  retained, at best**, on the current quote.

**The institutional imperative [E2-30], scored:** (1) resists change — no: the format
was re-mixed toward digital/same-day fast. (2) projects soak up funds — the FY2022–23
capex peak ($5.5bn, $4.8bn) into a demand cliff fires it mildly. (3) staff studies — the
"business transformation initiative" is the classic shape; not evidenced beyond the
charge. (4) peer imitation — **yes, mildly**: Circle 360 imitates Walmart+/Prime; Target
Plus imitates the marketplace model; both are defensive necessity as much as imitation.

**Buybacks [E5-08]:** (1) ample funds — yes. (2) discount — **the record is the
anti-ORLY pattern in execution but not in stated policy**: repurchases ran $7.4bn at
~$220+ (FY2021, near the top), $2.8bn (FY2022), zero (FY2023), $1.0bn at ~$141 (FY2024),
$403M at ~$106 (FY2025, at/below the conservative zero-growth band computed at Q5), and
**zero in H1 FY2026** — though the H1 stop, with the stock still near its lows in Q1,
reads as cash preservation through the tariff fight rather than price discipline. The
FY2021 tranche at ~$220 against a value band later proven to be less than half that is a
**capital-allocation flag** on the cycle, stated with [E4-13]'s humility clause. Binds
position size; no position exists.

**Candor [E2-26]:** the best in the non-COST cohort — the traffic/ticket table that
convicts the company at Q2 is published every year; the FY2022 markdown catastrophe was
reported plainly with its causes; the incentive metric excluded a windfall gain; there is
no adjusted-earnings promotion (FY2024 10-K had NO non-GAAP adjustments at all). Against
it: the RedCard Penetration withdrawal [E2-49] and the unquantified Circle membership
base. Authorship [E2-72] not assessed (no shareholder letter is filed with the 10-K).

- **VERDICT (for the record): [x] IN as an overlay — no disqualifier found.** Honest
  reporting, honest pay design, poor five-year capital results, one cycle-timing buyback
  flag. **IN never promotes; Q2 OUT stands [E2-37].**

---
## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings [E2-23] — **COMPUTATION — NOT A CLEARANCE**

OCF − SBC − (c), finance-lease ROU additions included in capex (they are purchases of
productive assets financed by lease — the screen's own construction, kept):

| FY | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| OE, (c)=capex+FL | 3,564 | 7,248 | 4,565 | **−1,954** | 3,460 | 3,853 | 2,450 |
| OE, (c)=D&A | 4,366 | 7,840 | 5,755 | 1,098 | 5,569 | 4,082 | 3,147 |

- **3-yr window:** 3,254 (capex+FL) to 4,266 (D&A) · **5-yr:** **2,475** to 3,930 ·
  **7-yr:** 3,312 to **4,551**
- **Combined range $2,475M – $4,551M, width 83.9%.** The [E4-25] question was answered at
  Stage 0(b): **the width is the FY2022 crisis year** (OE −$1,954M at the capex end — an
  inventory glut cleared by markdown, OCF halved, capex peaking simultaneously) sitting
  inside the 5-yr window, plus a capex line that swung 2,891 → 5,528. The distorted year
  is NAMED [E5-11]; the range does not close the file because the verdict is already
  closed at Q2, and every construction prices below the floor anyway (see below).
- **[E4-41] normalization:** the 3-yr window contains the one-time $593M interchange gain
  (cash, inside FY2025 OCF) — stripped, the 3-yr capex+FL mean is ~3,056. The 7-yr
  window contains the FY2020 stimulus year (7,248). Both flatter; both named.
- **Maintenance capex — the disclosed judgment [E2-23, E3-44, E5-20]:** this is NOT the
  [E5-20] exception class (the filing never says depreciation understates renewal), but
  the D&A default is still refused as (c): **capex has exceeded D&A every year since
  FY2018** (5-yr mean 1.45x incl finance leases) and management guides **~$5bn for 2026
  against ~$3.2bn of D&A** — and the excess is overwhelmingly *defensive*: remodels,
  supply chain, technology, i.e. [E2-23]'s "fully maintain its long-term competitive
  position" for a box whose traffic decays without them. True growth capex is only the
  ~18–30 new stores a year (+0.9%/yr of sq ft), allowed at ~$500M. **Target disclosed a
  new-store vs remodel capex dollar split in NO vintage read (FY2016–FY2025 — narrative
  counts only; the FY2025 capex chart is an image); stated per the absence-claim rule.
  The DG measured-split precedent is unavailable; (c) is a guess and is disclosed as
  one: (c) ≈ $3,300–3,800M.** SBC subtracted in full [E5-06] ($281M, reported charge as
  floor).
- **JUDGED OWNER EARNINGS: ~$3,100M** (5-yr capex+FL construction 2,475 as the
  conservative bound; 3-yr ex-gain ~3,050 as the center; the D&A ends kept only as the
  display top). Band carried: **$2,500M – $3,900M**.

### Great, good, or gruesome? [E4-20]
**[x] Good — with a filed gruesome episode.** 12–13% after-tax on tangible capital,
earned also on added capital but at a falling rate ([E4-32]); FY2022 showed what the
gruesome state looks like (capital consumed, OE negative). [E4-43]: good passes Q4.

### Staying power — all three [E5-11]
1. **Large and reliable earnings stream:** large, yes; reliability carries one named
   failure — FY2022 OE was negative at the capex end. Passes with the exception stated.
2. **Massive liquid assets: PASSES** — $5,488M cash (of which $4.6bn in ≤60-day
   instruments), **no commercial paper outstanding at any time during 2025 or 2024**, and
   the two revolvers ($1.0bn 364-day + $3.0bn to 2028) are backstops NOT counted, per
   [E5-39]. The first non-COST retailer in this queue to pass (2) cleanly.
3. **No significant near-term cash requirements: PASSES** — current debt $2,130M against
   $5,488M of cash; dividends ~$2.1bn and guided capex ~$5bn covered by OCF ($6.6bn
   FY2025, $4.5bn in H1 FY2026 alone).
- Leverage, named and quantified [E4-16, E3-29]: total debt $16,456M (including $2,113M
  of finance leases) + $3,834M operating lease liabilities; net of cash ~$11.0bn ≈ 3.5x
  judged OE. Coverage [E2-54]: OCF less capex = $2,835M against $629M of cash interest —
  **4.5x out of current cash flow net of capex**. Comfortable; A2/A/A.
- **[E2-60] restricted earnings:** fired historically, acquits currently. **FY2021–22:
  $10.2bn of buybacks against $2.6bn of two-year owner earnings, debt +$4.5bn** — the
  distribution that exceeded restricted earnings preceded the five-year $100 → $66.89
  TSR. FY2023–25: dividends+buybacks $7.5bn against $9.8bn of capex-end OE, debt flat —
  inside the line.
- **ASC 842, honestly:** finance leases are NOT immaterial in stock — $2,113M liability,
  13.6-yr weighted term at 4.00% — but additions are modest in flow ($104M / $319M /
  $104M = 2.8–11% of cash capex) and are **already included in (c) above**. Operating
  leases $3.7bn ROU / $3.8bn liability, additions $381M. The MCD lesson (lease-financed
  additions outside the capex line) is handled by construction here.

### The specific way this business dies [E2-27, E3-24]
- **Mechanism:** the discretionary middle collapses. Target's 46% discretionary mix is
  the slice Walmart under-prices, Amazon out-conveniences, and Costco out-values; traffic
  compounds away at −2%/yr while the fixed big-box estate (250M sq ft, $34bn of PP&E)
  deleverages; gross margin reverts toward the FY2022 state in every demand shock because
  inventory must be marked down to leave the building.
- **Quantified from filed figures:** the FY2022 year IS the stress test, filed: GM 23.6%,
  op margin 3.5% → on today's sales that is ~$3.7bn of operating income against $629M of
  cash interest — **coverage ~6x even in the crisis state**; maturities staggered, no CP,
  $5.5bn cash. Solvency death requires that state to persist for years while $16bn of
  debt rolls — **a low-level possibility** [E3-24].
- **The realistic death is the DG/KR shape, and its first five years are already filed:**
  seven years of zero adjusted operating-income growth, four years of negative real
  comps, capital retained at ~$0 of market value per $1 [E3-54]. Permanent value
  stagnation, not bankruptcy — **a real possibility**.
- **VERDICT (for the record): [x] IN — it survives.** Q2 OUT stands.

---
## Q5 BLOCK — **COMPUTATION — NOT A CLEARANCE** (operator rule 3; the queue contract
requires a price from every run)

*Q1 IN · Q2 OUT — the hard sequence closes the file. Nothing here is entry language.*

- Sovereign **5.27%** (US Treasury 30-yr par, 2026-09-02, issuing authority) — bare rate,
  no per-name premium [E3-42].
- Market cap **$74,509M** (454,296,736 sh × $164.01, 2026-09-03, aggregator quote
  flagged).
- **The yield:** judged OE $3,100M ÷ $74,509M = **4.16%**; band **3.32%** (5-yr capex+FL
  bottom) **to 6.11%** (7-yr D&A top, a construction the (c) judgment rejects). **Below
  the 5.27% bond on every construction this run accepts.**
- **What the price already assumes:** perpetual growth of **+1.1%** (judged) to **+1.95%**
  (conservative bottom) just to match the bare bond — achievable-looking, against a
  business whose owner earnings have compounded at **roughly zero** over nine years
  (FY2016 capex-end OE ≈ $3.8bn → judged $3.1bn today) and whose adjusted operating
  income is $4,775M against FY2016's $4,864M. **Growth needed for the [E4-28] floor:
  +5.8% (judged) to +6.7% (bottom) perpetual** — the screen's 6.65% reproduced — against
  that same zero-growth record. [E4-35]'s base rate governs the belief.
- **Honest pre-tax expectancy at $164.01: ~4.2% + ~0–2% growth ≈ 4–6%. Below the ~10%
  floor on every construction — quit on, not ranked [E4-28].**
- **THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** (zero-growth at the sovereign):
  - conservative (5-yr bottom): ~$47bn ≈ **$105/sh**
  - judged: ~$59bn ≈ **$130/sh**
  - generous (top of accepted band $3,900M): ~$74bn ≈ **$160–165/sh**
  - at the [E4-28] floor: **~$55–85/sh, judged ~$70/sh**
- **The price sits AT THE TOP of the zero-growth band** — the market is already paying
  for the H1 FY2026 recovery to be structural. After a +65% rally from the fiscal-2025
  close (the filed FY2025 TSR base of $66.89 per $100), the quote needs the traffic
  inflection to hold AND convert to operating-income growth merely to keep pace with the
  bond.
- Windage count: conservatism spent **once** (the judged OE sits below the window means;
  no margin stacked on the rate; no second application).
- Bar: **Screamer test [E4-01]** — price above the judged case and at the top of the whole
  range → **no**. Not close.

## Q6 — FOR THE RECORD: pre-committed monitoring [E1-02]
- **Thesis-confirming metric (for any future re-look):** the filed traffic line. Two more
  positive halves ON A NON-BOYCOTT BASE (i.e., positive against FY2026 comparables),
  converting to adjusted operating income above **$5.5bn** (the FY2023–24 level), would
  make the H1 FY2026 inflection structural rather than aberrational [E3-30].
- **Thesis-breaking (of the OUT, i.e. reopen-test):** owned-brand penetration wording
  recovering to "one-third"; RedCard/Circle-class engagement metric re-published;
  Roundel crossing ~$1.5bn while total op margin holds ≥6%.
- **Re-entry price, pre-committed:** ~**$130/sh at a 5.27% sovereign** (recomputed at the
  rate of the day) — and only via the reopen tests above; Q2 OUT is otherwise permanent.
- Next catalyst: Q3 FY2026 10-Q (~late November 2026); FY2026 10-K (~March 2027) for the
  full-year traffic line and any further IEEPA refunds.

---
## SELF-AUDIT
- [x] Questions answered in order; stop-at-first-non-IN honored (Q2 OUT closes; Q3–Q5
  are FOR THE RECORD under the operator's brief and rule 3 headers)
- [x] No question marked IN carries an unverified/provisional caveat
- [x] No UNRESEARCHED verdicts outstanding; absence claims name their sweeps (sales/sqft
  never published — 8-vintage sweep; capex split never disclosed — same sweep; CPI-2016
  not pulled — FY2016 excluded from the real series rather than estimated)
- [x] Step 0: filing read, accession numbers recorded; OCF $6,562M cross-checked
- [x] Owner earnings multi-year, three windows shown, (c) a disclosed judgment with the
  band; SBC subtracted in full
- [x] Competitor row filled (4 peers, filing-sourced, same-window; limits stated); moat
  class NOT provisional
- [x] Sovereign from the issuing authority, dated; price dated and aggregator-flagged
- [x] Value as round-number range; screamer bar only; windage counted (once)
- [x] Run committed to git after Step 0/Q1, Q2, Q3, and this close
- Tool defects logged this run: (1) `floor_screen.py` crashes on TGT in `chart_events`
  (OSError, date.fromtimestamp) — row reproduced by hand; (2) `run.py` share basis is a
  weighted average, cover count used instead (known defect, still live); (3) run.py D&A
  tag (3,000 vs filed 2,981 for FY2024) — immaterial here, same first-tag class as the
  MCD defect.

## REGISTER
- Verdict: **[x] OUT (about the business)** — at Q2, [E3-03] criterion 2.
- One line: **a well-run, honestly-reported general merchant whose customers re-choose it
  every trip and have chosen it less for three straight years — the discretionary middle
  between Walmart's price and Costco's membership, with the H1 FY2026 traffic recovery
  recorded at full strength and priced past its own zero-growth value.**

---
## OUTPUT CONTRACT (queue requirement)
**PRICE (COMPUTATION — NOT A CLEARANCE):** zero-growth value at the 5.27% sovereign
**~$105–165 per share, judged ~$130**; at the [E4-28] 10% floor **~$55–85, judged ~$70**.
Current price **$164.01** (2026-09-03) sits at the top of the sovereign band; honest
pre-tax expectancy **~4–6%**, below the floor on every construction.
**PASS/FAIL: FAIL — closed at Q2 (franchise test, [E3-03] criterion 2). Q1 IN · Q2 OUT ·
Q3/Q4 recorded for the record (no disqualifier; survives) · Q5 never opened.**


