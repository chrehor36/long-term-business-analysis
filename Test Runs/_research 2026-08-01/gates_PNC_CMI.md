# GATE RUN — PNC Financial Services Group (PNC) and Cummins Inc. (CMI)

**Analysis date: 2026-08-01 (LIVE analysis, not a backtest)**
**Framework: Buffett/Munger long-term business analysis — Gates 1, 2, 3, 5 as scoped by the operator**

---

## STATUS BANNER — READ FIRST

Per OPERATOR PROTOCOL §1 and §2:

- This run covers **Gates 1, 2, 3, 5 only**. Gates 4, 6, 7, 8 were not run and are not reported.
- Every price and valuation figure below is labeled **COMPUTATION — NOT A CLEARANCE**. No entry permission, starter size, buy price, or watchlist status is granted for either company by this document.
- **PNC**: Gates 1–3 PASS (Gate 3 with one unresolved sub-item), **Gate 5 FAIL**.
- **CMI**: Gates 1–2 PASS, **Gate 3 FAIL on integrity (binary, permanent)**. Gate 5 recorded but MOOT.

### Data-integrity notes for this run

| Item | Status |
|---|---|
| SEC EDGAR direct fetch (sec.gov `/Archives/`) | Returned **HTTP 403** on every attempt. PNC FY2025 10-K and CMI FY2025 10-K could not be read directly. Figures below come from company press releases, the equisolve-hosted 8-K financial highlights, earnings-call transcripts, and dated secondary sources. |
| PDF proxies (PNC 2026 DEF 14A, CMI 2026 DEF 14A) | Would not parse. Compensation metric weightings and beneficial-ownership tables are **UNVERIFIED** for PNC; partially corroborated across filing years for CMI. |
| PNC AOCI / HTM securities unrealized losses | **NOT ESTABLISHED.** Flagged as a material open item in Gate 5. |
| CMI Q2 2026 earnings | **Not yet reported** — scheduled 2026-08-04, three days after this analysis date. Latest CMI quarter is Q1 2026 (reported 2026-05-05). |
| Live price quotes | Multiple sources disagreed within the same week for CMI (see Gate 2 note). Flagged inline. |

---
---

# PART I — PNC FINANCIAL SERVICES GROUP (PNC)

**Market context (COMPUTATION — NOT A CLEARANCE), as of 2026-07-31:**
Price $249.87 · market cap ~$99.8B · trailing P/E 13.74 · dividend yield 3.22% · 52-week range $176.88–$256.49 · tangible book value per share $111.09 (at 2026-06-30) → **P/TBV ≈ 2.25x**.
Quarterly dividend raised 18% to $2.00/share, announced 2026-07-06.

---

## GATE 1 — CIRCLE OF COMPETENCE

### Unit economics in plain words (not management language)

PNC rents money from depositors and lends it out at a higher rate. That is the whole business, plus a fee layer bolted onto it.

**Where the spread actually comes from — three sources, only one of which is a franchise:**

1. **Free money.** Roughly 23% of PNC's deposits pay zero interest (noninterest-bearing were 23% of total in Q2 2026, 22% in Q1 2026, Q4 2025 and Q1 2025). On an average deposit base of $457.0B (Q2 2026), that is roughly $105B of funding on which PNC pays nothing and earns whatever short-term rates happen to be. This is the closest thing to a real economic advantage in the business, and it comes from being the operating bank for households and companies — payroll, checking, treasury management — not from being clever.

2. **The repricing roll-forward — and this is the honest driver right now.** PNC bought securities and wrote fixed-rate loans in 2020–2021 at very low yields. Those assets are maturing and being replaced at 2025–2026 yields. PNC says this explicitly and repeatedly: Q4 2025 NIM expansion "reflect[ed] the benefit of fixed rate asset repricing." On the Q2 2026 call (2026-07-22), CFO Robert Reilly said the repricing benefit extends into 2027 and that NIM should "exceed 3% by end of year." **This is a mechanical, dated, self-terminating tailwind, not pricing power.** Flagged again in Gate 2(d) and Gate 5(a).

3. **Falling deposit costs.** As the Fed cut, PNC repriced deposits down faster than its assets repriced down. Rate paid on interest-bearing deposits: 2.24% (Q2 2025) → 2.32% (Q3 2025) → ~1.96% (Q1 2026) → **1.91% (Q2 2026, down 5 bp)**. Q1 2026 NIM rose 11 bp specifically because the rate paid on interest-bearing deposits fell 18 bp. **This source is now exhausted** — Reilly, Q2 2026 call: "We do have rate paid drifting back up to first quarter levels."

**The funding base:** average deposits $457.0B (Q2 2026), up from $428.8B FY2025 average and $420.6B (Q1 2025). The step-up is largely acquired, not organic — the FirstBank Holding Company acquisition closed 2026-01-05 and brought $26B of assets, $16B of loans and $23B of deposits.

**Revenue mix, FY2025:** net interest income $14,410M; noninterest income $8,689M; record total revenue $23.1B. So ~62% spread / ~38% fee. NIM 2.83% FY2025.

### Reportable segments — three, each independently evaluable

| Segment | Q2 2026 earnings | What it actually is |
|---|---|---|
| Retail Banking | $1,747M | Branches, consumer deposits, cards, mortgage. The funding engine. |
| Corporate & Institutional Banking | $1,588M | C&I lending, treasury management, capital markets. The asset engine. |
| Asset Management Group | $135M | Private bank and institutional asset management. Small. |

(Q4 2025 comparatives: Retail $1,241M, C&IB $1,514M, AMG $121M.)

Three segments, cleanly reported, each with its own P&L and its own drivers. No conglomerate opacity.

### VERDICT — GATE 1: **PASS**

Not opaque, not heterogeneous. A bank's balance sheet is inherently a black box in the sense that you cannot inspect the loans one by one — but PNC discloses portfolio composition, criticized/nonperforming detail by sector (see Gate 5(d)), and three legible segments. The spread mechanics reduce to arithmetic a non-banker can follow. **Pass.**

---

## GATE 2 — MOAT (franchise test)

### (a) Is the product needed or desired? — **YES, with a caveat that matters**

Deposit accounts, payments, and credit are needed. But *needed* is not the test in isolation — the franchise test asks whether **this supplier** is needed. A household needs a checking account; it does not need PNC's checking account. Score this as a pass on the letter and a warning on the substance.

### (b) Is there no close substitute? — **FAIL**

This is the check PNC loses. Money is the purest commodity there is. Substitutes for a PNC deposit: JPMorgan, Bank of America, Wells Fargo, U.S. Bancorp, Truist, several hundred community banks, Treasury Direct, money-market funds, and brokerage cash sweeps. Substitutes for a PNC commercial loan: every other bank plus the entire private-credit market.

Switching costs on a primary operating account are real — direct deposits, autopay, treasury-management integrations — but they are friction, not a moat. The 2023 regional-bank stress proved how fast deposits move when depositors get scared, and 2022–2024 proved how fast they move when depositors get greedy for yield.

**Check (b) fails.**

### (c) Is it relatively unregulated? — **HARD FAIL. Stated plainly, not glossed.**

PNC is one of the most heavily regulated businesses in the American economy. The Federal Reserve, OCC and FDIC set its capital, its leverage, its liquidity and its stress-test buffer. The CFPB governs its consumer pricing. The CRA governs where it must lend. Basel and CCAR govern how much capital it must hold before it may return a dollar to owners.

**How this constrains pricing power specifically — this is a real constraint, not a formality:**

- **PNC cannot set the price of its own funding.** Deposit rates are set by the fed funds rate and by what the competitor across the street is paying. PNC is a price-taker on the liability side.
- **PNC cannot set the price of its own capital return.** CET1 was 9.9% at 2026-06-30 against an operating target of roughly 10%. The buyback ($610M in Q2 2026) and the dividend exist inside a regulator-defined envelope. If the stress-capital buffer moves, the capital plan moves — regardless of what management or owners want.
- **PNC cannot expand freely.** Both the BBVA USA and FirstBank acquisitions required regulatory approval. Growth by acquisition is growth at a regulator's pleasure.
- **Consumer fee income is a political variable.** Overdraft economics, late-fee rules and Reg E interchange have all been rewritten by regulators within the last decade, in both directions depending on the administration. Fee revenue that a regulator can legislate away is not franchise revenue.

The framework permits a heavily regulated business to pass Gate 2 when the other three checks are strong. **They are not.** Check (b) fails alongside (c).

### (d) Proven by pricing power AND returns on capital? — **RETURNS YES, PRICING POWER NO**

#### Primary moat metric, 8-quarter trend (from earnings releases and 8-K financial highlights)

**Net interest margin:**

| Quarter | NIM | Note |
|---|---|---|
| Q3 2024 | 2.64% | derived (Q4 2024 stated "+11 bps") |
| Q4 2024 | 2.75% | |
| Q1 2025 | 2.78% | |
| Q2 2025 | 2.80% | |
| Q3 2025 | 2.79% | −1 bp, "driven by 5% avg. commercial deposit growth" |
| Q4 2025 | 2.84% | +5 bp QoQ, +9 bp YoY, "benefit of fixed rate asset repricing" |
| Q1 2026 | 2.95% | +11 bp QoQ, driven by an 18 bp fall in rate paid on IB deposits |
| Q2 2026 | 2.96% | +1 bp QoQ |

**+32 bp over eight quarters.**

**Rate paid on interest-bearing deposits (deposit cost / beta proxy):**
Q2 2025 2.24% → Q3 2025 2.32% → Q1 2026 ~1.96% → Q2 2026 **1.91%** (−5 bp).
Down-beta has been favorable. Management says it is over ("rate paid drifting back up," Reilly, 2026-07-22).

**Efficiency ratio:**
Q1 2025 62% → Q2 2025 60% → Q3 2025 59% → Q4 2025 59% → FY2025 60% → Q1 2026 61% (60% ex-integration costs) → Q2 2026 60%.
**Flat at 59–61%.** This is the metric that has *not* improved. A genuine banking franchise runs in the low 50s. PNC exceeded its $350M 2025 continuous-improvement cost target and the efficiency ratio still did not move — because revenue and expense grew together.

**ROTCE:**
Q2 2025 15.6% → Q3 2025 16.8% → Q1 2026 15.7% → **Q2 2026 17.88%**. (Q3 2024 and Q4 2024 not located; gap acknowledged.)
Management target: "18% annualized exit rate fourth quarter '26" (Q2 2026 call); Q2 2026 at 17.9%, "in the vicinity."
Full-year ROE: 12.04% (2022), 11.65% (2023), 11.27% (2024), **12.16% (2025)**; PNC's own reported FY2025 return on average common shareholders' equity 12.90%.

#### Reading the trend honestly

The NIM and ROTCE improvement is real and large. **But name its cause.** It is (i) the fixed-rate asset repricing roll-forward, which management dates as running into 2027 and which then stops; (ii) a favorable deposit down-beta which management says is now finished; and (iii) FirstBank scale added by purchase on 2026-01-05. **None of those three is pricing power.** Pricing power would mean PNC charging borrowers more, or paying depositors less, than peers, sustainably, because customers have nowhere else to go. There is no evidence of that in the disclosures.

What PNC *does* have is a **funding advantage**, which is a different and lesser thing: 23% noninterest-bearing deposits, a coast-to-coast branch network, and growing DDA households. Demchak, Q2 2026 call, attributed retail deposit resilience to PNC's scale versus smaller competitors lacking a retail presence — and noted retail deposits kept growing even as rates fell. That is a genuine, durable structural advantage. It is scale and distribution, not franchise.

**Returns on capital:** ROTCE ~16–18% against a cost of equity of roughly 10% is genuine excess return, and it is the correct metric for a bank. But ROE has sat at 11–12% for four straight years and the excess is currently at a rate-cycle high.

### Direction and class

- **Direction: WIDENING — but cyclically, not structurally.** Every basis point of the widening is attributable to a dated, self-terminating mechanical cause. The structural metric (efficiency ratio) is flat.
- **Class: NARROW.** Checks (b) and (c) both fail. The moat is a low-cost, sticky, scaled deposit base — worth something, and worth less than it looks at the top of a rate cycle.

### VERDICT — GATE 2: **PASS (NARROW)**

Not NONE — the 23%-noninterest-bearing deposit franchise and the 17.9% ROTCE are real. Not WIDE — no substitute-blocker, heavy regulation as a live pricing constraint, no demonstrated pricing power, and a flat efficiency ratio. **Pass as NARROW.**

---

## GATE 3 — MANAGEMENT

### INTEGRITY (binary; permanent if failed)

Searched for: fraud, accounting manipulation, cartel/price-fixing, bribery/FCPA, systematic deception of customers or regulators, regulator findings of misconduct.

**Findings:**

| Matter | Date | Assessment |
|---|---|---|
| **Overdraft re-sequencing class action, $90M settlement** — PNC's system posted debit/ATM transactions highest-to-lowest rather than in actual order, maximizing overdraft fees; several hundred thousand customers, transactions 2004–2010 | Settled 2012 | **Blemish, not a Gate-3 failure.** A private class action, not a regulator finding. Industry-wide practice at the time (Wells, BofA and others settled the same claim). Conduct is 16–22 years old, predates Demchak's 2013 appointment, and no admission or regulatory finding of deception attached. Recorded, not disqualifying. |
| **CFPB v. Early Warning Services / Zelle** — banks sued for failing to protect consumers from Zelle fraud | Filed Dec 2024; voluntarily dismissed **with prejudice 2025-03-05** | **PNC WAS NOT A DEFENDANT.** Named parties were JPMorgan Chase, Bank of America, Wells Fargo and Early Warning Services. PNC is clear. |
| **OCC Order of Prohibition, Gerald E. Milligan II** — former teller at a Royal Palm, FL branch, false attestations on a PPP loan application | 2024 | **Individual employee misconduct, not institutional.** The OCC barred the individual; no action against PNC Bank, N.A. Not attributable to management. |
| Redlining / fair-lending enforcement | Searched 2020–2025 | **No PNC action found.** DOJ redlining consent orders in the period ran against First National Bank of Pennsylvania, Park National Bank and others — not PNC. |
| Accounting restatement, FCPA, cartel | Searched | **None found.** |

**INTEGRITY VERDICT: PASS.** No dated institutional finding of deception of customers or regulators. The 2012 overdraft settlement is recorded as a consumer-practices blemish from a prior era and prior management.

### COMPETENCE

**Bill Demchak — CEO since 2013, Chairman. Thirteen years in the seat.**

**The 2023 regional-banking stress is the single best competence datapoint available, and PNC passed it:**

- Deposits at 2023-12-31 were **$421.4B, down only $2.2B (1%)** from year-end 2022 — and that decline was commercial deposits at year end, not a run. Average deposits fell $11.0B versus Q4 2022, attributed to Fed quantitative tightening and customer spending, not flight.
- PNC took **no emergency capital, no FDIC assistance, no discount-window rescue**, and stayed profitable through the year: FY2023 net income $5.6B, diluted EPS $12.79 ($14.10 as adjusted).
- The cost was margin, not solvency: Q4 2023 NIM 2.66%, down 26 bp year-over-year.

While First Republic, Silicon Valley and Signature failed and Western Alliance and PacWest were nearly killed by deposit flight, PNC's deposit base did not move. **That is the franchise proving itself under the only test that matters.**

**Operating record, FY2025 (reported 2026-01-16):** net income $6,997M; diluted EPS $16.59; record revenue $23.1B; ROE 12.90%; efficiency 60%; CET1 10.6%; TBVPS $112.51; net charge-offs $744M; provision $779M; ACL/loans 1.58%; NPL/loans 0.67%. Management's own framing: "the best financial performance in its history."

**Returns on capital / retained-earnings test — this is where competence is weakest:**

ROE by year: 12.04% (2022) → 11.65% (2023) → 11.27% (2024) → 12.16% (2025). **Four years, essentially flat.** PNC retained roughly 60% of earnings each year (2025 payout ratio 39.8%) and returns on owner capital did not rise. Retained earnings grew the book; they did not grow the *return on* the book.

Over the last twelve months the retained-earnings test *does* pass — TBVPS $103.96 (2025-06-30) → $111.09 (2026-06-30), +6.9%, plus a ~3% dividend, against a stock that ran from a 52-week low of $176.88 to $249.87. But that is a rate-cycle re-rating, and it followed a 2021–2024 stretch in which flat ROE produced a sideways-to-down stock.

**Capital allocation:**
- **FirstBank Holding Company, closed 2026-01-05** — $26B assets, $16B loans, $23B deposits. Integration cost guided at $325M, of which $98M was booked through Q1 2026. Execution has been clean: 780,000 customers, 1,620 employees and 95 branches across Colorado and Arizona converted by 2026-06-22.
- **UNVERIFIED CONTEXT — do not rely on without confirmation:** PNC's 2021 acquisition of BBVA USA, funded by the 2020 sale of its BlackRock stake, is widely regarded as a value-destructive swap. **I did not verify the dates, prices or the counterfactual in this session.** It is recorded as an open question for Gate 3 competence, not as an established fact.

**COMPETENCE VERDICT: PASS.** The 2023 stress performance and the operating consistency carry it. Flat ROE across four years is a real reservation, recorded.

### ALIGNMENT

- **2026 proxy filed 2026-03-11.** Demchak's incentive compensation awarded for 2025 performance totaled **$33.7 million**, mixed 73% long-term equity / 27% annual cash. Reported total compensation rose **32%, from $22.4M (2024) to $29.5M (2025)**.
- Board committees are fully independent except that Demchak sits on the Risk Committee.
- **$33.7M against $7.0B of net income is 0.48%** — not looting. But a 32% raise in a year when ROE improved by 89 basis points (11.27% → 12.16%) means **pay is compounding faster than returns on owner capital.** That is the wrong slope.
- **UNRESOLVED:** The 2026 DEF 14A PDF would not parse. **The incentive metric names and weightings, the stock-ownership-guideline multiples, and the beneficial-ownership table (directors and executive officers as a group, and Demchak's personal holdings) were NOT verified.** Whether pay is tied to ROTCE, EPS, revenue, relative TSR or risk goals — and whether management owns a meaningful stake — is unknown from this run.

### VERDICT — GATE 3: **PASS, with one UNRESOLVED sub-item**

Integrity passes cleanly. Competence passes on the 2023 stress record. **Alignment cannot be closed** — the comp structure and insider ownership were not verified.

> **PROTOCOL NOTE:** Under OPERATOR PROTOCOL §1, "a gate marked CONDITIONAL, TODO, or [U]-unresolved is NOT a pass." Strictly applied, **Gate 3 is CONDITIONAL** pending the proxy read, and downstream gates are blocked until it closes. Gate 5 is worked below because the operator scoped it, but this reservation stands on the record.

---

## GATE 5 — INVERSION

### Bull-case assumptions, stated explicitly

1. NIM keeps climbing past 3.00% by end-2026 as fixed-rate assets reprice (Reilly, 2026-07-22).
2. Net interest income rises **15% to 15.5%** in 2026 versus 2025 (management guidance).
3. ROTCE reaches ~18% annualized exit rate in Q4 2026 and **holds there**.
4. Deposit costs stay near 1.91% and the noninterest-bearing mix holds at ~23%.
5. Credit stays benign: NCOs 0.25% annualized, NPLs 0.55%, ACL/loans 1.48% (all Q2 2026).
6. Office CRE is contained and already reserved.
7. FirstBank integrates cleanly and PNC keeps acquiring accretively.
8. Regulators keep permitting ~10% CET1 operation and capital return ($610M buyback in Q2 2026, dividend +18% to $2.00).

### Inversion — what would make this a mistake

#### (a) MOAT DESTRUCTION — **UNRESOLVED**

The entire earnings thesis is a **self-terminating mechanical tailwind**. NIM went 2.64% → 2.96% over eight quarters because a securities and loan book written at 2020–21 yields is rolling into 2026 yields. Management dates the runway as extending into 2027. **After that, it stops.** There is no second act disclosed.

Meanwhile the deposit-cost tailwind is *already* over — Reilly said so on 2026-07-22: "rate paid drifting back up to first quarter levels." So the favorable half of the scissors has closed while the asset half has roughly 4–6 quarters left.

And the structural metric never moved: **efficiency ratio flat at 59–61% for eight quarters**, despite exceeding a $350M cost-savings target in 2025. If the moat were widening, that number would fall. It hasn't.

If the Fed cuts further from here, asset yields fall while deposit costs are already near their floor — NIM compresses from both sides. **Unresolved.**

#### (b) MANAGEMENT FAILURE — **UNRESOLVED**

Demchak's crisis record (2023) is genuinely good, and that partially resolves this. What does not resolve is **acquisition risk**. PNC bought BBVA USA in 2021 and FirstBank in 2026, and management has signaled appetite for more. Bank M&A is the single most reliable mechanism by which super-regionals destroy owner capital — every deal is a fresh opportunity to overpay in stock or cash for a deposit base you could have grown. The FirstBank conversion executed cleanly, which is evidence about *integration* skill, not about *price paid*. **Unresolved.**

Secondary: alignment is unverified (see Gate 3). A management team whose pay metrics you cannot see is a management team you cannot underwrite.

#### (c) BALANCE-SHEET RISK — **UNRESOLVED, and this is the most serious finding in the PNC run**

**Two problems.**

**First — leverage sits directly on the framework's own automatic-fail line.**

| Date | Total assets | Equity denominator | Assets / equity |
|---|---|---|---|
| 2025-12-31 | $573,572M | **Common** shareholders' equity $54,828M | **10.46x** |
| 2025-12-31 | $573,572M | Total equity $60,585M | 9.47x |
| 2026-03-31 | $603,028M | Total equity $63,627M | 9.48x |

The framework's Ruling 2 (ratified 2026-07-15) sets a **hard mechanical ceiling of 10:1 assets/equity for financial businesses — automatic FAIL, no exception.** PNC lands on either side of that line depending on whether preferred stock and noncontrolling interests are counted as equity. On **common** equity — the equity that actually belongs to the shareholder being asked to buy — **PNC exceeds 10:1**.

This is not a rounding question. It must be resolved explicitly in Gate 4 with a stated denominator convention before any downstream work proceeds. It is flagged here because inversion cannot be honest while it is open.

**Second — the securities book was never examined.**

**PNC's AOCI position and its held-to-maturity unrealized losses are NOT ESTABLISHED in this run.** The FY2025 10-K returned HTTP 403 on every attempt.

This is the single number that killed Silicon Valley Bank. In a regime where a bank's asset yields are rising because old low-coupon bonds are rolling off, the mirror image of that story is that the bonds still on the books are underwater. You cannot underwrite a bank's balance sheet without knowing the size of the mark. **Unresolved, and materially so.**

#### (d) OFFICE COMMERCIAL REAL ESTATE — **MOSTLY RESOLVED**

At 2025-12-31: office loans **$5.1 billion, 1.5% of total loans**, plus $0.1B unfunded commitments. Within that book: **criticized 34.0%, nonperforming 11.1%, reserved at 11.0%.**

Sizing the damage: 34.0% criticized on $5.1B is $1.73B of stressed exposure. A punitive 30% loss severity on the *entire* criticized bucket is roughly $520M — against $5.2B of total allowance for credit losses and $7.0B of annual net income. **PNC survives its office book comfortably.** Total NCOs were $226M (0.25% annualized) in Q2 2026 and NPLs fell to 0.55%. On the Q2 2026 call Reilly described CRE pipelines "forming in a very constructive way, across all the categories," with CRE balances growing $690M in the quarter into retail and industrial.

Honest counterweight: **34% criticized is not a healthy portfolio.** It is a portfolio being reserved through. And PNC's own CFO said of office losses, "we're probably about a third of the way through the game." Resolved on *survivability*, not on *finished*.

#### (e) THE EXPOSURE NOBODY IS PRICING — **UNRESOLVED**

**Multifamily is $14,655 million — 50% of PNC's $29,565M commercial real estate book, and roughly 2.9x the office book.**

Multifamily has been the asset class everyone treated as safe while staring at office. The 2021-vintage multifamily loans written at 3% against aggressive rent-growth assumptions now refinance at 2026 rates into softening rents in exactly the Sunbelt markets PNC bought into via BBVA USA. **This is the larger exposure and it received the least attention in every disclosure reviewed.** Unresolved.

### THESIS-BREAKING METRIC AND NUMERIC EXIT THRESHOLD

**Primary: quarterly net interest margin.**
> **EXIT if NIM prints below 2.80% for two consecutive quarters.**

Rationale: 2.80% was the Q2 2025 level. A return there gives back the entire post-2024 repricing gain and means the mechanical tailwind is spent and deposit competition has won. NIM is the correct trip-wire because *the entire bull case is NIM*.

**Secondary hard trips (any one, exit regardless of NIM):**
> - **Criticized office exceeds 45% of the office book** (from 34.0% at 2025-12-31), or
> - **Total net charge-off rate exceeds 0.50% annualized for two consecutive quarters** (from 0.25% in Q2 2026 — a doubling), or
> - **CET1 falls below 9.0%** (from 9.9% at 2026-06-30, against a ~10% operating target).

### VERDICT — GATE 5: **FAIL**

Two of the four inversion tests are **UNRESOLVED** — moat destruction and balance-sheet risk — and one of them is unresolved for the worst possible reason: **the securities book was never measured.** A bank whose AOCI and HTM unrealized-loss position you have not established is a bank you have not analyzed, in a rate regime where that number is the difference between a franchise and a failure.

Compounding it, the assets-to-common-equity ratio of **10.46x at 2025-12-31 sits above the framework's own 10:1 automatic-fail ceiling for financials**, and the core earnings thesis rests on a tailwind management itself dates as expiring in 2027 with nothing disclosed to replace it.

**Gate 5 FAILS. The PNC analysis stops here.** No Gate 6/7/8 output. No valuation. No entry language.

### PNC — GATE SUMMARY

| Gate | Verdict |
|---|---|
| 1 — Circle of competence | **PASS** |
| 2 — Moat | **PASS (NARROW, cyclically widening)** |
| 3 — Management | **PASS** — integrity clean, competence good, **alignment UNRESOLVED** (strictly CONDITIONAL per §1) |
| 5 — Inversion | **FAIL** |

---
---

# PART II — CUMMINS INC. (CMI)

**Market context (COMPUTATION — NOT A CLEARANCE), as of 2026-07-31:**
Price **$634.20** · market cap $87,513M · trailing P/E 32.94 · 52-week range **$354.68–$737.76**.
On FY2025 diluted EPS of $20.50 that is **30.9x trailing** — though FY2025 EPS was depressed by $3.28/share of electrolyzer charges.

> **Price-source conflict, flagged:** three sources within the same week gave $634.20 (2026-07-31), $664.65 (2026-07-26) and $679.71 (undated). The $634.20 figure is used because it is the most recent and most precisely dated. **A 52-week range spanning 2.1x tells you most of what you need to know about the cyclicality and the current sentiment in this name.**

> **TIMING WARNING:** CMI **Q2 2026 earnings are scheduled for 2026-08-04** — three days after this analysis date. Latest available quarter is Q1 2026 (reported 2026-05-05). Any conclusion here is three days from being repriced.

---

## GATE 1 — CIRCLE OF COMPETENCE

### Unit economics in plain words (not management language)

**Sell the iron once. Sell the parts for twenty years.**

Cummins sells a diesel or natural-gas engine, or a complete power system, into a truck, a generator, a mine or a boat. That first sale is competitive, cyclical, and earns a mid-teens margin at best. Then the asset runs for 10–25 years, and every filter, injector, turbo, aftertreatment module and overhaul kit it consumes comes back to Cummins — at a much better margin, on a schedule set by hours of operation rather than by the customer's capex mood.

The value capture is structural: an engine is a *certified* assembly. Its emissions compliance is granted against a specific parts configuration. A fleet cannot substitute a generic injector into a certified aftertreatment system without breaking the certification and the warranty. **Cummins is effectively sole-source for the service life of every engine it ever shipped.**

**Verifiable anchors for the annuity:**
- **Distribution segment parts sales: $4,083M in FY2025 vs $3,980M in FY2024 — up 2.6% in a year when total company revenue fell 1%.** The annuity grew while the cycle shrank. That is the whole thesis in one line.
- That $4.083B is **12.1% of consolidated FY2025 revenue of $33.7B** — and that figure captures only the Distribution segment. Parts and service revenue inside Components and Power Systems is not separately disclosed, so the true aftermarket share is higher but **not quantifiable from disclosure.**
- Management-sourced (via secondary reporting, not verified in filings): ~2.2 million active on-highway Cummins engines in North America; parts intensity peaks around years 7–11 of engine life; roughly $250M of parts sold in 2025 for engines built **before the year 2000.**

> **REJECTED DATA POINT:** One secondary source claimed "aftermarket revenue represents more than 80% of net sales." **This is not credible and is not used anywhere in this analysis.** It cannot be reconciled with the segment disclosures. Flagged so it does not propagate.

### Reportable segments — five, each independently evaluable

**FY2025 vs FY2024** (reported 2026-02-05):

| Segment | FY2025 sales | FY2024 sales | FY2025 EBITDA | FY2025 % | FY2024 EBITDA | FY2024 % |
|---|---|---|---|---|---|---|
| Engine | $10.875B | $11.712B | $1.382B | 12.7% | $1.653B | 14.1% |
| Components | $10.149B | $11.679B | $1.398B | 13.8% | $1.591B | 13.6% |
| Distribution | $12.405B | $11.384B | $1.808B | 14.6% | $1.378B | 12.1% |
| Power Systems | $7.463B | $6.408B | $1.694B | 22.7% | $1.180B | 18.4% |
| Accelera | $0.460B | $0.414B | $(0.896)B | n/m | $(0.764)B | n/m |

(Segment sales exceed consolidated revenue due to intersegment eliminations — normal for this structure.)

**Consolidated FY2025:** revenue $33.7B (−1%); EBITDA $5.4B (16.0% of sales) vs $6.3B (18.6%); net income $2.8B (8.4%); diluted EPS **$20.50** vs $28.37; operating cash flow **$3.621B** vs $1.487B. Includes **$458M ($3.28/share) of electrolyzer charges**, of which $415M non-cash.

**Q4 2025:** revenue $8.5B (+1%); EBITDA $1.2B (13.5%) vs 12.1%; net income $593M; EPS $4.27.

**Q1 2026** (reported 2026-05-05): revenue $8.4B (+3%); EBITDA $1.290B (15.4%), or $1.489B (17.7%) excluding fuel-cell charges; net income $654M / EPS $4.71, versus $824M / $5.96 in Q1 2025; operating cash flow $309M. Includes **$199M ($1.44/share) of charges on the low-pressure fuel cell business sale.**

### VERDICT — GATE 1: **PASS**

Five segments, each with disclosed sales and EBITDA in dollars and percent, quarterly. The business reduces to a sentence an owner can hold in their head. **Pass.**

---

## GATE 2 — MOAT (franchise test)

### (a) Needed or desired? — **YES, strongly**

Class 8 trucks, mining haul trucks, locomotives, marine vessels, standby gensets and — the new one — AI data centers all need prime and backup power that only large reciprocating engines currently supply at scale. Demand evidence: **Power Systems FY2025 EBITDA margin of 22.7% on record sales**, rising to **29.5% in Q1 2026**, driven by "increased demand for power generation products, particularly for data center applications."

### (b) No close substitute? — **PASS, with one real weakness**

**The strength:** Cummins is the last independent engine supplier at scale. Every other major heavy-duty engine in North America is captive to its truck OEM — Detroit Diesel to Daimler, MX to Paccar, and so on. A fleet that specs Cummins gets one engine platform across multiple truck makes, one parts inventory, one training program, and a nationwide service network. **That multi-OEM commonality is the substitute-blocker, and no captive can offer it.**

And once installed, there is genuinely no substitute for a Cummins part in a Cummins engine for the fifteen years it runs.

**The weakness, stated honestly:** at the *point of sale*, captive engines are precisely the substitute, and OEM vertical integration has been taking share from Cummins in on-highway for two decades. **Engine segment EBITDA margin has gone 14.1% (FY2024) → 12.7% (FY2025) → 10.4% (Q1 2026, vs 16.5% in Q1 2025).** The engine franchise is being squeezed in real time.

### (c) Relatively unregulated? — **NO — but here regulation is a moat-BUILDER, unlike at PNC**

Emissions regulation is the dominant force on this business: EPA 2027 at 0.035 g/hp-hr NOx, plus CARB.

But the direction of the effect is opposite to PNC's. Each tightening raises the R&D and certification cost of playing at all, and shifts share toward whoever can afford to certify. That favors scale — which favors Cummins. Crucially, **the regulator does not set Cummins' prices.** Cummins prices its own product.

Evidence of the regulation-as-tailwind dynamic right now: **June 2026 Class 8 orders rose 231% to 31,400 units**, with ACT Research noting rising freight rates and "a race to beat EPA 2027 emissions rules" rapidly filling remaining 2026 build slots.

**Score: PARTIAL PASS** — heavily regulated, but the regulation raises rivals' costs rather than capping Cummins' prices. (See Gate 5(a) for why the *same* fact is also the biggest risk in the thesis.)

### (d) Pricing power AND returns on capital? — **RETURNS: STRONG. PRICING POWER: NOT PROVEN.**

#### Returns on invested capital

| FY | ROIC | ROE |
|---|---|---|
| 2021 | 21.65% | 23.53% |
| 2022 | 17.53% | 22.25% |
| 2023 | **6.20%** | 8.35% |
| 2024 | 20.77% | 38.36% |
| 2025 | **17.95%** | 23.93% |

2023's collapse is the ~$2.04B emissions charge, not operations. **Ex-2023, a 17–22% ROIC band across a full cycle.** That is genuine, durable excess return on capital and it is the strongest single fact about this business.

#### Pricing power — and the answer is no, on management's own words

This is where the franchise story does not survive contact with the disclosures. From Q4 2025 / 2026 guidance commentary:

- Cummins is **"price cost neutral in EBITDA dollars"** in 2026 — no incremental pricing benefit.
- 2026 guidance assumes **"almost no incremental net pricing benefit outside of tariff recovery."**
- The tariff mechanism is **"a tariff surcharge, essentially getting 0% margin revenue that is diluted to the overall margin"** — carrying **50 basis points of guidance dilution.**
- Tariffs cost **$22 million in Q2 2025** before recovery caught up.

**A business with real pricing power passes a cost shock through *at* its margin, and keeps the spread. Cummins passes it through at zero margin and eats the dilution.** That is cost recovery, not pricing power. It is what a supplier does when the customer — a small number of very large truck OEMs — holds the whip.

The pricing power that plausibly *does* exist sits in the parts book, where a captive installed base has no alternative. **But Cummins does not disclose parts pricing or parts margin separately.** That belief is inference, not evidence. Recorded as such.

### Primary moat metrics — trend

**Segment EBITDA margin: FY2024 → FY2025 → Q1 2026 (vs Q1 2025)**

| Segment | FY2024 | FY2025 | Q1 2026 | Q1 2025 | Direction |
|---|---|---|---|---|---|
| Engine | 14.1% | 12.7% | **10.4%** | 16.5% | **NARROWING hard** |
| Components | 13.6% | 13.8% | 13.3% | 14.3% | Flat / slightly narrowing |
| Distribution | 12.1% | 14.6% | 14.2% | 12.9% | **WIDENING** |
| Power Systems | 18.4% | 22.7% | **29.5%** | 23.6% | **WIDENING sharply** |
| Accelera | loss $764M | loss $896M | loss $277M | loss $86M | **Deteriorating** |
| **Consolidated** | **18.6%** | **16.0%** | 15.4% (17.7% ex-charge) | 17.9% | Down, guided to recover |

**Aftermarket/parts mix:** Distribution parts $4,083M FY2025 vs $3,980M FY2024, **+2.6% while total revenue fell 1%.**

**FY2026 guidance (raised 2026-05-05):** revenue **+8% to +11%** (from +3% to +8%); EBITDA **17.75% to 18.50%** of sales (from 17.0–18.0%). Segment raises: Distribution +9–14%, Power Systems +14–19%, Engine +7–12%, Components +5–10%.

*(8-quarter segment granularity was not obtainable from the sources reachable this session — sec.gov returned 403. The FY/quarterly comparison above is what the press releases support. Gap acknowledged.)*

### Direction and class

**Direction: MIXED — and the mix is the whole story.** Consolidated margin *fell* in 2025 (18.6% → 16.0%). Underneath that average, the legacy franchise is narrowing (Engine 14.1% → 10.4%) while the new profit engine is widening violently (Power Systems 18.4% → 29.5%). The FY2026 guided recovery to 17.75–18.50% is **not a truck recovery — it is a data-center genset recovery.**

**Class: WIDE**, on the installed-base parts annuity plus the last-independent-supplier position — both of which are structural and neither of which depends on the cycle. Note that the *location* of the width is migrating from trucks to power generation, and that the Engine segment standing alone would be NARROW.

### VERDICT — GATE 2: **PASS (WIDE)**

Passes (a), (b) and (d)-on-returns; (c) is a partial pass where regulation helps rather than constrains. **Pricing power is explicitly not proven** — the returns are earned on installed base, mix and volume, not on price. Wide moat, honestly qualified.

---

## GATE 3 — MANAGEMENT

> **This is the decisive gate for CMI.**

### INTEGRITY (binary; permanent if failed)

#### The emissions matter — precise timeline

| Date | Event |
|---|---|
| **2019-04-29** | Cummins files an 8-K and issues a press release: it is conducting **a formal review of its emissions certification process and compliance with emissions standards for pickup truck applications**, "following conversations with the United States Environmental Protection Agency and the California Air Resources Board regarding certification for the company's engines in the model year 2019 RAM 2500 and 3500 trucks." Review conducted with external advisers. **Cummins voluntarily disclosed the review to its regulators** and committed to cooperate. |
| **2023-12-22** | Cummins announces an agreement in principle. Company's own language: it **"does not admit wrongdoing"**; **"The company has seen no evidence that anyone acted in bad faith"**; it "has cooperated fully with the relevant regulators" and "worked collaboratively with the regulators for more than four years." Charge of **~$2.04 billion** in Q4 2023, of which **~$1.93B payable in H1 2024.** |
| **2023-12-22** | DOJ, EPA and the State of California announce Cummins will pay a **$1.675 billion civil penalty — the largest civil penalty ever secured under the Clean Air Act**, and per DOJ the second-largest environmental penalty ever. Plus **>$325M to remedy the violations** and **$175M to a California environmental mitigation fund.** |
| **2024-01-10** | Settlement reached; **two consent decrees** filed in federal court, District of Columbia. |
| 2024–2026 | Follow-on private litigation (below). |

#### What the regulators actually found

Per EPA's own account of the settlement:

- Cummins **configured emissions software as defeat devices** that **"reduce or deactivate the vehicle engines emission controls"** during normal driving, **while activating full controls only during testing.**
- Cummins **failed to disclose auxiliary emission control devices (AECDs) to regulators "as part of the engine certification process."**
- **Scope: 630,000 model-year 2013–2019 RAM 2500/3500 engines with illegal defeat devices**, plus **~330,000 model-year 2019–2023 vehicles with undisclosed AECDs** — **nearly one million vehicles**, which EPA described as **"more than any other major defeat devices settlement."** The conduct spans **model years 2013 through 2023 — eleven years.**
- **Remedy:** recall and repair at least **85% of affected vehicles within three years**, replace the software with compliant software, and offer an extended warranty on repaired vehicles.

#### Follow-on litigation

- **Securities class action** (S.D. Indiana), class period **2019-02-11 to 2023-12-21**: settled for **$1,600,000** — stipulation dated **2025-12-08**, approval process running into 2026. Roughly **$0.22 per damaged share** (~$0.14 net of fees). **A nominal amount** — the plaintiffs got essentially nothing.
- **Consolidated shareholder derivative litigation** alleging that Cummins' top executives breached fiduciary duties by overseeing an emissions-cheating scheme: **DISMISSED** by an Indiana federal judge.

#### The assessment

**The exculpatory framing — "does not admit wrongdoing," "no evidence anyone acted in bad faith," self-disclosed, cooperated for four years, derivative suit dismissed, securities case worth $1.6M — is the framing Cummins wrote. It is not the framing of the record.**

What the record establishes:

1. **The mechanism is deception by construction.** Software that deactivates emissions controls on the road and reactivates them on the test bench has exactly one function: to cause the certification test to report something other than real-world behavior. A regulator is *the audience* of that test. Whether any named individual "acted in bad faith" is not the question the framework asks; the framework asks whether there was systematic deception of regulators. Software written to behave differently when it detects it is being watched **is** that.

2. **The AECD non-disclosure is separate and additional.** Failing to disclose auxiliary emission control devices during certification across **~960,000 vehicles over model years 2013–2023** is not a lapse in a quarter. It is a **practice sustained for eleven years across two distinct engine generations.**

3. **The penalty is the largest in the history of the Clean Air Act.** Regulators do not assign record-setting civil penalties for good-faith paperwork disagreements. The magnitude is itself a finding.

4. **The framework's rule is directly on point.** Gate 3 integrity fails on "systematic deception of customers or regulators, or a regulator finding of misconduct." The carve-out is for "pure competition-law matters without deception." **This is the exact inverse of the carve-out** — it is a deception-of-regulator matter with no competition-law dimension at all.

**The genuine mitigation, stated fairly:**

- Cummins **self-disclosed in April 2019**, apparently before EPA compelled it, and cooperated for four-plus years.
- It took the full charge, funded the recall and mitigation, and did not litigate.
- **The conduct predates CEO Jennifer Rumsey** (Chair & CEO since **August 2022**) and largely predates the current executive team.
- **The derivative suit was dismissed** — no court found the current directors culpable.
- The securities settlement of **$1.6 million** implies the plaintiffs' bar concluded the *securities-fraud* claims were nearly worthless.

**Why the mitigation does not cure it:**

Absence of an admission is a **negotiated settlement term**, not a finding of innocence — no defendant admits, ever. The framework's integrity test is stated as **binary and permanent** and contains **no prior-management exception**. It is a test about the conduct of the *business* toward its regulators, and Buffett's own articulation of the standard — that the firm can afford to lose money but cannot afford to lose "even a shred of reputation" — is a statement about an institution, not about an incumbent's tenure.

> ### **INTEGRITY VERDICT: FAIL.**
>
> A record-setting Clean Air Act penalty resting on defeat-device software plus eleven years of undisclosed AECDs across ~960,000 vehicles is a **regulator finding of systematic deception**. Binary. Permanent.

> **JUDGMENT FLAG — the operator should overrule if they disagree.** Per the framework's working style ("when uncertain whether a passage supports a principle, present the passage and ask"), the strongest case *against* this verdict is laid out above in full: voluntary self-disclosure in 2019, four years of documented cooperation, no admission, derivative suit dismissed, a $1.6M securities settlement implying no meaningful investor-deception claim, and a CEO who took the chair in August 2022 — after the conduct. **A reasonable analyst could grade this as a PASS on the "prior management, self-corrected" reading.** This run grades it FAIL because the rule as written is binary, is about the institution, and the conduct spanned eleven years and one million vehicles. **The operator's call governs.**

### COMPETENCE *(recorded, though the gate has already failed)*

**Strong:**
- **ROIC 17.95% (FY2025), 20.77% (FY2024)** — see Gate 2(d). Genuinely good capital productivity.
- Operating cash flow **$3.621B in FY2025** versus $1.487B in FY2024 (2024 was depressed by the emissions payments).
- **15th consecutive dividend increase.** The Atmus divestiture reduced shares outstanding by ~5.6 million, or 4%. Q1 2026 returned **$519M** to shareholders ($276M dividends, $243M buybacks) against a stated goal of returning **50% of operating cash flow.**
- **2030 targets raised 2026-05-21:** revenue **$45–50 billion** by 2030 (6–9% CAGR), **EBITDA above 20%**. A **$450 million** investment to expand high-horsepower genset capacity by **20 GW** (to 55 GW nameplate by 2030), targeting **$9 billion of data-center revenue by 2030** versus ~$5 billion expected in 2026. Power Systems plus Distribution to contribute at least half of earnings. CFO Mark Smith's bridge: data center +2–3% CAGR; content plus on-highway recovery +2–3%; aftermarket, mining and other industrial +2–3%.

**Weak — and it is a pattern, not an incident:**

Accelera has consumed roughly **$2.4 billion** in ~27 months:
- FY2024 segment EBITDA loss **$(764)M**
- FY2025 segment EBITDA loss **$(896)M**, including **$458M of electrolyzer charges** ($415M non-cash)
- Q1 2026 segment EBITDA loss **$(277)M** alone, including **$199M of charges on the low-pressure fuel cell sale**

Management is now **unwinding the bet** — an electrolyzer "strategic review initiated in response to shifts in hydrogen adoption expectations," and the fuel-cell divestiture. **Credit for correcting it; debit for making it.**

Note the shape of the strategy: the company that spent 2021–2025 losing $2B+ betting on the hydrogen and electrification transition is now committing $450M+ to betting on very large diesel and gas engines for AI data centers. **Both are consensus-transition bets.** The second at least has visible, contracted demand behind it. The first also looked that way in 2021.

### ALIGNMENT *(recorded)*

- **Long-term incentive structure is genuinely good:** performance shares **70%** / performance cash **30%**; both measured on **Return on Invested Capital weighted 80%** and **EBITDA weighted 20%**, over a **three-year term**. Cummins' stated rationale: ROIC and EBITDA growth "reinforce the importance of delivering profitable growth and high returns of capital, the two most important drivers of shareholder return." **An 80%-ROIC-weighted LTI is rare and is close to what an owner would actually choose.** This is a real point in management's favor.
- **Jennifer Rumsey**, Chair & CEO since August 2022. Reported total compensation ~**$21.86M** (approximately 6.9% salary, 93.1% bonus/equity). Direct ownership ~**0.03%** of shares outstanding (~$24.5M). **Low insider ownership in percentage terms** — normal for a large-cap industrial, but not owner-like.
- **CAVEAT:** the 2026 DEF 14A (filed **2026-04-02**) could not be opened this session. The ROIC/EBITDA weightings are corroborated across multiple Cummins proxy years, but the **exact current-cycle weightings and the beneficial-ownership table are UNVERIFIED.**

### VERDICT — GATE 3: **FAIL**

**Failed on INTEGRITY.** Competence is strong and the alignment structure is better than most. **Neither cures a binary integrity failure.**

> **Per OPERATOR PROTOCOL §1: Gates 4, 6, 7 and 8 are MOOT and are not run for CMI. No valuation, no clearance, no entry language, no watchlist.**

---

## GATE 5 — INVERSION *(MOOT — Gate 3 failed. Recorded for completeness only.)*

### Bull-case assumptions, stated explicitly

1. Data-center genset demand is **durable, not an AI capex bubble** — $9B of data-center revenue by 2030 versus ~$5B in 2026.
2. The truck cycle recovers through 2026–27 on EPA-2027 pre-buy (June 2026 Class 8 orders **+231% to 31,400 units**; 2026 build slots filling).
3. The parts annuity keeps compounding on ~2.2 million North American engines.
4. Accelera losses shrink toward zero as the electrolyzer and fuel-cell exits complete.
5. FY2026 guidance holds: revenue **+8–11%**, EBITDA **17.75–18.50%** (raised 2026-05-05).
6. ROIC returns to ~20%.

### Inversion — what would make this a mistake

#### (a) MOAT DESTRUCTION — **UNRESOLVED**

**Two vectors, and the second is the one nobody in the bull case addresses.**

**(i) OEM vertical integration in on-highway is happening now.** Engine segment EBITDA margin: 16.5% (Q1 2025) → **10.4% (Q1 2026)**. FY: 14.1% → 12.7%. This is the legacy franchise being squeezed in real time by captive engines.

**(ii) The EPA-2027 pre-buy is a demand *pull-forward*, and it creates a dated air pocket.** Every truck bought in 2026 to beat the rule is a truck **not bought in 2028**. ACT Research says it plainly: 2027 demand will be driven by "replacement cycles, regulatory timing and measured prebuy activity rather than broad fleet expansion," and orders are already "spilling into the first half of 2027." Cummins' 2026 guidance raise, the Class 8 order surge, and the stock's run to a $737.76 52-week high are all being fed by demand that is **borrowed from 2028**. **The 2028 hole is a known, dated, structural feature of this thesis and nothing in the bull case accounts for it.**

Offsetting, honestly: the parts annuity is indifferent to when a truck was bought — it cares about how many are running. Distribution parts grew 2.6% in a down year. That is the part of the moat that survives the air pocket. But it is 12.1% of disclosed revenue, not the whole company.

**Unresolved.**

#### (b) MANAGEMENT FAILURE — **UNRESOLVED, and already realized once**

Approximately **$2.4 billion of Accelera value destruction (FY2024–Q1 2026)** is not a risk; it is a completed event. The same management is now committing **$450M+ of capacity** on the strength of an AI data-center demand signal that is, at minimum, as consensus-driven as the hydrogen signal was in 2021.

**The pattern is chase-the-consensus-transition.** That is precisely the institutional imperative — the thing Buffett warned produces "mindless imitation" of peer behavior. Cummins built hydrogen electrolyzers because everyone was building hydrogen electrolyzers; it is now building high-horsepower gensets because everyone is building data centers. The second call may well be right. **The decision process is the same one that was wrong the first time.**

**Unresolved.**

#### (c) BALANCE-SHEET RISK — **RESOLVED**

At 2025-12-31: total debt ~**$7.6B**; long-term debt $6,792M; commercial paper $353M; cash and equivalents **$2,845M**; total equity **$13.4B**; total assets **$33.99B**. **Debt/equity 0.56** (down from 0.71 in 2022). FY2025 operating cash flow **$3.621B**. Ratings: **S&P 'A' with stable outlook** (affirmed 2025-03-11); **Moody's A2**.

Against the framework's survival-track Fortress Test (Ruling 2): a 50% owner-earnings decline sustained for two consecutive years is **comfortably serviceable** at this leverage, with investment-grade access, a termed-out maturity profile and $2.8B of cash. Note also that Cummins **absorbed a $2.04 billion charge in a single quarter (Q4 2023) without impairing its investment-grade standing** — which is about as direct a real-world stress test as one could ask for.

**Resolved.**

#### (d) A THESIS-BREAKING METRIC EXISTS — **YES**

### THESIS-BREAKING METRIC AND NUMERIC EXIT THRESHOLD

**Primary: Power Systems segment EBITDA margin.**
> **EXIT if Power Systems EBITDA margin prints below 20.0% for two consecutive quarters.**

Rationale: this line went 18.4% (FY2024) → 22.7% (FY2025) → **29.5% (Q1 2026)**, and **the entire re-rating rides on it** — a 52-week range of $354.68 to $737.76 and a 30.9x trailing multiple are not being paid for a truck-engine company. A fall back below 20% means data-center genset pricing has normalized toward historical levels and the multiple has nothing holding it up.

**Secondary — the one that actually breaks the *moat*, not just the multiple:**
> **EXIT if Distribution parts sales decline year-over-year for two consecutive quarters** (against the $4,083M FY2025 base).

The parts annuity is the moat. It grew 2.6% in a year when revenue fell 1%. If it stops doing that, the installed-base premise is broken and nothing else in the thesis matters.

**Tertiary / valuation trip:**
> **EXIT if consolidated EBITDA margin prints below 15.0% for two consecutive quarters** (below the FY2025 trough of 16.0% and far below the 17.75–18.50% guide).

### VERDICT — GATE 5: **FAIL** *(moot — Gate 3 already failed)*

Two of the four inversion tests are **UNRESOLVED**, and the specific unresolved items are not curable by patience: the **EPA-2027 pre-buy air pocket in 2028** is a dated structural feature of the demand curve, and a management team with a demonstrated **$2.4 billion pattern of capitalizing consensus transitions** does not become a different team by holding the stock longer. Balance-sheet risk is genuinely resolved and the parts annuity is genuinely durable — that is not enough.

### CMI — GATE SUMMARY

| Gate | Verdict |
|---|---|
| 1 — Circle of competence | **PASS** |
| 2 — Moat | **PASS (WIDE — but pricing power NOT proven; width migrating from trucks to power gen)** |
| 3 — Management | **FAIL — INTEGRITY (binary, permanent).** Competence strong, alignment structure good; neither cures it. |
| 5 — Inversion | **FAIL (moot)** |
| 4, 6, 7, 8 | **MOOT — NOT RUN** |

---
---

# OPEN ITEMS FOR A FOLLOW-UP RUN

| # | Item | Company | Why it matters |
|---|---|---|---|
| 1 | **AOCI and held-to-maturity securities unrealized losses** | PNC | The single most important unexamined number for any bank in this rate regime. sec.gov returned 403; the FY2025 10-K was never read. **Blocks any honest Gate 4.** |
| 2 | **Assets/equity denominator convention** | PNC | 10.46x on common equity vs 9.47x on total equity at 2025-12-31 — straddles the framework's own 10:1 automatic-fail ceiling for financials (Ruling 2). Must be settled explicitly. |
| 3 | **2026 DEF 14A: incentive metric weightings, ownership guidelines, beneficial ownership table** | PNC | Gate 3 alignment cannot close without it. PDF would not parse. |
| 4 | **Multifamily CRE book — $14,655M, 50% of CRE, ~2.9x the office book** | PNC | Received the least disclosure attention and is the larger exposure. 2021-vintage refinancing risk in Sunbelt markets. |
| 5 | **Uninsured deposit percentage** | PNC | Not established. Directly relevant to the deposit-franchise quality question. |
| 6 | **Q2 2026 earnings, 2026-08-04** | CMI | Three days after this analysis date. Will reprice everything, particularly Power Systems margin — the named thesis-breaking metric. |
| 7 | **2026 DEF 14A current-cycle LTI weightings and beneficial ownership** | CMI | Structure corroborated across years but current-cycle figures unverified. |
| 8 | **Parts/aftermarket revenue outside the Distribution segment** | CMI | Not disclosed. The true size of the annuity — the actual moat — is therefore unquantifiable from filings. |
| 9 | **Operator ruling on the CMI integrity call** | CMI | The judgment flag in Gate 3 is a genuine coin-edge under the framework's binary rule. The operator's decision governs and should be recorded as a ruling. |

---

# SOURCES

**PNC**
- [PNC Reports Full Year 2025 Net Income of $7.0 Billion, $16.59 Diluted EPS (2026-01-16)](https://www.prnewswire.com/news-releases/pnc-reports-full-year-2025-net-income-of-7-0-billion-16-59-diluted-eps-302663341.html)
- [PNC Reports Third Quarter 2025 Results](https://investor.pnc.com/news-events/financial-press-releases/detail/668/pnc-reports-third-quarter-2025-net-income-of-1-8-billion-4-35-diluted-eps)
- [PNC Reports First Quarter 2026 Results (2026-04-15)](https://www.prnewswire.com/news-releases/pnc-reports-first-quarter-2026-net-income-of-1-8-billion-4-13-diluted-eps-or-4-32-as-adjusted-302743057.html)
- [PNC Q1 2026 Financial Highlights (8-K)](https://content.equisolve.net/pnc/sec/0000713676-26-000026/for_pdf/q12026financialhighlightsa.htm)
- [PNC Reports Second Quarter 2026 Results (2026-07-15)](https://investor.pnc.com/news-events/financial-press-releases/detail/694/pnc-reports-second-quarter-2026-net-income-of-2-1-billion-4-81-diluted-eps-or-4-85-as-adjusted)
- [PNC Q2 2026 Earnings Call Transcript (2026-07-22)](https://www.fool.com/earnings/call-transcripts/2026/07/22/pnc-pnc-q2-2026-earnings-call-transcript/)
- [PNC Reports Full Year 2023 Results (2024-01-16)](https://www.prnewswire.com/news-releases/pnc-reports-full-year-2023-net-income-of-5-6-billion-12-79-diluted-eps-or-14-10-as-adjusted-302035659.html)
- [PNC FY2025 Form 10-K (EDGAR — returned 403; office/multifamily CRE figures via search index)](https://www.sec.gov/Archives/edgar/data/713676/000071367626000020/pnc-20251231.htm)
- [PNC 2026 DEF 14A (2026-03-11)](https://investor.pnc.com/sec-filings/all-sec-filings/content/0001193125-26-102189/d62941ddef14a.htm)
- [PNC ratios and price data — stockanalysis.com (2026-07-31)](https://stockanalysis.com/stocks/pnc/financials/ratios/)
- [CFPB drops Zelle lawsuit (2025-03-04/05)](https://www.cnbc.com/2025/03/04/cfpb-drops-jpmorgan-bank-of-america-wells-fargo-lawsuit.html)
- [PNC $90M overdraft settlement (2012)](https://www.americanbanker.com/news/pnc-settles-overdraft-litigation-for-90-million)

**CMI**
- [Cummins Reports Q4 and Full-Year 2025 Results (2026-02-05)](https://investor.cummins.com/news/detail/689/cummins-reports-strong-fourth-quarter-and-full-year-2025)
- [Cummins Q1 2026 Results; Raises Full-Year Outlook (2026-05-05)](https://investor.cummins.com/news/detail/694/cummins-delivered-strong-operating-results-and-returned)
- [Cummins Raises 2030 Financial Targets (2026-05-21)](https://investor.cummins.com/news/detail/696/cummins-raises-2030-financial-targets-announces)
- [Cummins Reviewing Emissions Certification and Compliance Process (2019-04-29)](https://investor.cummins.com/news/detail/420/cummins-reviewing-emissions-certification-and-compliance)
- [Cummins Reaches Agreement in Principle to Settle Regulatory Proceedings (2023-12-22)](https://investor.cummins.com/news/detail/633/cummins-reaches-agreement-in-principle-to-settle-regulatory)
- [DOJ: Cummins Agrees to Pay Record $1.675 Billion Civil Penalty (2023-12-22)](https://www.justice.gov/archives/opa/pr/united-states-and-california-announce-diesel-engine-manufacturer-cummins-inc-agrees-pay)
- [EPA: 2024 Cummins Inc. Vehicle Emission Control Violations Settlement](https://epa.gov/enforcement/2024-cummins-inc-vehicle-emission-control-violations-settlement)
- [Cummins securities class action settlement notice (stipulation 2025-12-08)](https://www.globenewswire.com/news-release/2026/01/15/3219580/0/en/the-rosen-law-firm-p-a-announces-proposed-class-action-settlement-on-behalf-of-purchasers-of-cummins-inc-publicly-traded-common-stock-cmi.html)
- [Cummins beats emissions derivative suits (Law360)](https://www.law360.com/classaction/articles/2482557)
- [Cummins FY2025 Form 10-K (EDGAR — returned 403)](https://www.sec.gov/Archives/edgar/data/26172/000002617226000009/cmi-20251231.htm)
- [Cummins 2026 DEF 14A (2026-04-02)](https://www.sec.gov/Archives/edgar/data/26172/000110465926039158/tm261336-2_def14a.htm)
- [Cummins ratios, ROIC and price data — stockanalysis.com (2026-07-31)](https://stockanalysis.com/stocks/cmi/financials/ratios/)
- [ACT Research: Class 8 truck sales forecast 2026](https://www.actresearch.net/resources/blog/class-8-truck-sales-forecast-2026)
- [Class 8 Truck Orders Surge in June 2026 (CCJ)](https://www.ccjdigital.com/economic-trends/freight-demand/article/15829366/class-8-truck-orders-surge-in-june-as-2026-build-slots-near-capacity)
- [Cummins Q4 2025 Earnings Call Transcript (pricing/tariff commentary)](https://www.theglobeandmail.com/investing/markets/stocks/CMI/pressreleases/50368/cummins-cmi-q4-2025-earnings-call-transcript/)
