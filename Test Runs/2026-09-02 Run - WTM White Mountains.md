# Company Run — WHITE MOUNTAINS INSURANCE GROUP, LTD. (WTM) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**SECTOR METHOD UNDER TEST.** This run is the **first application to any filer** of
`Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`
(written 2026-09-02, derived entirely from Berkshire's letters). **The run has two jobs and
the second outranks the first:** (1) run WTM through the six questions; (2) **report every
place the method does not fit.** Method findings are logged inline as **[METHOD FINDING n]**
and collected in `## JOB 2 — WHERE THE SECTOR METHOD BREAKS` at the foot of this file.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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
- rate **5.27%** · date **2026-09-01** · source **US Treasury daily par yield curve, 30-year
  (issuing authority)**, via `tools/sources.py`. FRED DGS30 not used; it is the fallback.
- FX: **none applied.** WTM reports in USD. *But see [METHOD FINDING 8] — Ark writes at
  Lloyd's and in Bermuda, and a material part of the earnings is GBP- and EUR-denominated
  before translation. The framework's "sovereign for the earnings currency" rule has no
  procedure for a filer whose reporting currency and earnings currencies differ inside one
  consolidated statement. USD is used because the filer reports and the shares trade in USD.*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **10-K, FY2025, filed 2026-02-27, accession 0001628280-26-012603** (`wtm-20251231.htm`)
- **10-Q, Q2 2026, filed 2026-08-06, accession 0001628280-26-053932** (`wtm-20260630.htm`)
- **DEF 14A, filed 2026-04-01, accession 0001104659-26-038487**
- **8-K, 2026-08-27, accession 0001628280-26-059191**
- figure cross-checked against the filed statement: **Ark's gross ending loss and LAE reserve
  balance of $2,481.0M in the MD&A "Loss and LAE Reserve Summary" rollforward ties to the
  consolidated balance sheet line "Loss and loss adjustment expense reserves $2,481.0" at
  2025-12-31, and to the same line in the Q2 2026 10-Q comparative column.** Second
  cross-check: total investments summed by segment off the Q2 balance sheet = $8,134.4M.

### STAGE 0(a) — SHARE COUNT READ BY HAND OFF THE 10-Q COVER
> *"As of August 3, 2026, **2,386,721 common shares** with a par value of $1.00 per share were
> outstanding (which includes 31,665 restricted common shares that were not vested at such
> date)."* — 10-Q cover, accession 0001628280-26-053932

- **Single class.** No A/B structure. No ADR. The BRK-A/B failure mode does not arise here.
- Shares **2,386,721** · price **$2,105.51** (Yahoo Finance, **aggregator, live quote only,
  flagged**, 2026-09-02; prior closes 2026-09-01 $2,098.96, 2026-08-29 n/a, 2026-08-27
  $2,127.57) · **market cap $5,025M**.
- Reconciliation: the 10-K reports 2,479,677 shares at 2025-12-31. The count fell **3.7% in
  seven months** on buybacks. A cached FY2025 count would have overstated the cap by $196M.
  **The hand-read mattered, at the 3.7% level rather than the LEVI/PINS level.**
- Book value per share at 2026-06-30: $5,388.3M ÷ 2,386,721 = **$2,257**. **Price/book 0.93.**

### STAGE 0(b) — IS WTM ACTUALLY A FLOAT-BEARING COMPANY? **THE ANSWER IS: BARELY.**

**This is the first substantive test of the sector method and the method does not survive it
intact.** WTM's FY2025 10-K contains the word **"float" fifteen times, and all fifteen refer
to floating-rate debt** (`Ark 2021 Subordinated Notes ... floating rate`, `HG Global Senior
Notes ... floating rate`, and so on). **WTM never uses the word in the [E5-46] sense and
publishes no float figure.** → **[METHOD FINDING 1]** and **[METHOD FINDING 2]**.

Float therefore had to be *constructed*. Constructed here as policyholder liabilities less
the assets that offset them, at 2025-12-31, from the segment columns of the filed balance
sheet:

| | Ark/WM Outrigger | HG Global | total |
|---|---:|---:|---:|
| Loss and LAE reserves | 2,481.0 | — | 2,481.0 |
| Unearned insurance premiums | 1,026.1 | 327.9 | 1,354.0 |
| *less* reinsurance recoverables | (836.1) | — | (836.1) |
| *less* insurance premiums receivable | (848.4) | (11.4) | (859.8) |
| *less* deferred acquisition costs | (211.1) | (96.9) | (308.0) |
| **constructed float** | **1,611.5** | **219.6** | **1,831.1** |

**Total investments at 2025-12-31, all six columns: $8,323.9M.**
**Float funds 22.0% of the portfolio.** Berkshire in [E5-46] at the same test: $66bn of float
against $158bn of investments = **41.8%**. WTM's float ratio is **roughly half Berkshire's**,
and float is **34% of shareholders' equity** ($1,831M against $5,425M) — $738 per share
against a $2,188 book value per share.

**VERDICT ON STAGE 0(b): WTM is a holding company that owns a float-bearing business, not a
float-bearing company.** The brief's premise — "the smallest and cleanest float-bearing name"
— is **only half right**: it is the smallest, and it is *not* clean. Ark is one of five legs.
**Float is a minority of the story and the sector method must be applied knowing that.**
→ **[METHOD FINDING 3]**.

**What this does to the method:** Q5 steps 1 and 3 (investments at market; other pre-tax
earnings) carry essentially the whole valuation. Step 2 (cost of float) prices a $1.8bn
funding advantage inside a $5.0bn market cap — real, but it is a **rounding item beside the
portfolio**, not the engine. The method is still runnable; its **centre of gravity moves from
step 2 to step 3**, and the method document does not say what to do when it does.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** White Mountains is a **permanent-
capital buyout vehicle for insurance-adjacent businesses.** It raises no outside fund. It buys
control of a business with the parent's own equity, consolidates it, runs it for some years,
and sells it when someone pays more than it thinks the business is worth. Between purchases
the money sits in a securities portfolio. Three earnings streams, all readable off the filed
segment columns:

1. **Underwriting spread.** Ark writes specialty P&C and reinsurance at Lloyd's and in
   Bermuda; HG Global reinsures BAM's municipal-bond guarantees on a first-loss basis. Premium
   comes in, losses go out later, the difference is profit and the timing gap is float.
2. **Fee and distribution income.** Kudu buys minority *revenue* interests in asset and wealth
   managers and collects a distribution yield ($1.2bn deployed into 30 firms, ~$153bn of
   client AUM). Distinguished is an MGA earning commission on premium it places but does not
   bear. WTM Partners is an industrial roll-up (Enterprise Solutions, specialty electrical
   contracting) with no insurance in it at all.
3. **Realised gains on the businesses themselves.** This is not incidental — it is the
   business. FY2025's **book value per share rose 25% and $320 of that $442 per-share gain
   was the Bamboo sale**, on the filer's own arithmetic.

The company states the model itself, in the first paragraph of Item 1:

> *"White Mountains is engaged in the business of **making opportunistic and value-oriented
> acquisitions of businesses and assets in the insurance, financial services and related
> sectors, operating these businesses and assets** through its subsidiaries and, **if and when
> attractive exit valuations become available, disposing of these businesses and assets.**"*
> — 10-K FY2025, Item 1, GENERAL

**The scarce input this business controls: its own permanent capital and the deal judgment of
a very small team.** Not a product, not a brand, not a location. Roughly $1.0bn of
"undeployed capital" at 2025-12-31 on the filer's own number, against a $5.0bn cap.

**Will the fundamentals look broadly the same in ten years?** **The engine will; the contents
will not, and the filer says so.** The record: OneBeacon sold 2017, Sirius sold 2016, Esurance
2011, NSM 2022, BAM deconsolidated 2024-07-01, **Bamboo sold 2025-12-05**, Distinguished
bought 2025-09-02, Enterprise Solutions bought 2025-04-01. **Four of the five segment columns
in the Q2-2026 balance sheet did not exist in that form five years ago.** A ten-year cash-flow
statement about WTM is a statement about businesses not yet bought.

**The honest tension, stated rather than smoothed.** [E3-31] asks for a business "relatively
simple and stable in character" and warns against one "subject to constant change." WTM's
stated business model *is* constant change in its constituents. Against that: the corpus's own
worked float-bearing holding company is **Wesco [E3-71]** — an insurer plus a savings-and-loan
plus a steel service centre — valued as liquidating value plus the float advantage, and the
corpus treats that structure as understandable rather than too hard. **The change is in the
portfolio, not in the mechanism**, and the mechanism is legible from the filing.

**Operator rule 9, declared before the verdict.** I have an incentive to pass Q1, because
Q1 OUT would end the run and the run's *second* job is to test the sector method at Q5. That
incentive is named here so the reader can discount it. The case for OUT is real and is
this: **the ten-year cash flows of White Mountains are the cash flows of businesses that do
not yet exist**, and no amount of filing-reading resolves that. I am passing Q1 anyway
because the *question asked* is whether I can understand how this makes money, and I can —
three streams, each measurable — while the composition problem is properly a **Q4/Q5
question about durability and about [E5-50]'s third element**, where it is carried forward
and where it does real work.

- **VERDICT: [x] IN**
  *Carried forward: the composition problem returns at Q4 (there is no stable owner-earnings
  series to build) and at Q5 (the third element is not a modifier here — it is most of the
  value).*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**FIRST, THE UNIT OF ANALYSIS — and the method does not tell me what it is.**
WTM is five businesses. The sector method's CONVENTION 3 says a part-insurer/part-operating
filer is **valued** in two pieces, but it says nothing about how to run **Q2** on one. Asking
"is WTM a franchise?" is not one question. → **[METHOD FINDING 9]**. I therefore run [E3-03]
twice, on the two units that could plausibly carry a moat, and report both.

### READING (a) — ARK, the underwriting business (68% of FY2025 revenue ex-disposal gain)

| [E3-03] criterion | verdict | the filed words |
|---|---|---|
| (1) needed or desired | **PASS** | specialty P&C and marine/energy cover is contractually and statutorily required in most of these lines |
| (2) **no close substitute** | **FAIL** | see below |
| (3) not price-regulated | **PASS** | Lloyd's and Bermuda are solvency-regulated, not rate-regulated; [E2-59]'s administered-price rescue is absent, which is the honest reading — no regime floors these prices |

**Criterion 2 fails on the company's own Competition section**, which names **eighteen**
competitors in two lists and puts price first among the competitive factors:

> *"Specialized lines of insurance and reinsurance are **highly competitive**. Ark competes
> with other Lloyd's syndicates, London market participants and major U.S., Bermuda, European
> and other international insurance and reinsurance companies. The significant competitive
> factors for most products are **price**, terms and conditions, broker relationships,
> underwriting service, financial strength rating and claims service. Ark competes with
> insurance and reinsurance companies who operate in the Bermuda and Lloyd's markets such as:
> • **Bermuda**: American International Group, Arch Capital, Ascot, Aspen, Chubb, Everest Re,
> Markel, RenaissanceRe, Sompo, SiriusPoint **and others**; • **Lloyd's**: AXIS Capital,
> Beazley, Canopius, Convex, Hiscox, Lancashire, QBE **and other syndicates.**"*
> — 10-K FY2025, Item 1, Ark, "Competition"

This is **[E2-70]** verbatim in a 2026 filing: *"Insurance companies offer standardized
policies which can be copied by anyone. Their only products are promises. It is not difficult
to be licensed, and **rates are an open book.**"*

### THE PRICE SERIES — WTM publishes it, and it is the decisive instrument **[E4-55, E4-37]**

WTM publishes **no policies in force, no policy count, no retention rate and no renewal rate**
— the [E4-55] physical series is absent and **that absence is itself the finding**. But it
publishes something better: **its own risk-adjusted rate change**, which is the [E4-37] agony
metric in numerical form.

| year | **Ark risk-adjusted rate change** | Outrigger Re global property RI | Ark gross written premiums |
|---|---:|---:|---:|
| 2022 | **+9%** | — | $1,452M |
| 2023 | **+15%** | **+33%** | $1,898M |
| 2024 | **flat (0%)** | **(3)%** | $2,207M |
| 2025 | **(4)%** | **(5)%** | $2,557M |

*Sources: FY2022 10-K (acc. 0000776867-23-000004) for 2022; FY2023 10-K (acc.
0000776867-24-000005) for 2023; FY2025 10-K (acc. 0001628280-26-012603) for 2024 and 2025.*

> *"Gross written premiums increased 16% to $2,557 million in 2025 compared to $2,207 million
> in 2024, **with risk adjusted rate change of -4%**."* — FY2025 10-K MD&A

**Gross written premiums grew 76% in three years while the price series went +15% → 0% → −4%.**
That is not a franchise raising price; it is a price-taker taking volume as the market softens.
It is **[E2-58]** as written — *"persistent over-capacity without administered prices (or
costs) equals poor profitability"*, and *"nothing fails like success"*: the 2023 hard market
drew the capacity that is now cutting the rate. And it runs **[E4-37]** backwards — the moat
downgrade is legible in real time, in the filer's own number.

**Ark's combined ratio held flat while price fell**, which is the [E2-53] refutation:

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| **Ark GAAP combined ratio** | **87%** | **82%** | **82%** | **83%** | **83%** |
| Ark/WM Outrigger segment CR | — | — | — | **82%** | **81%** |
| prior-year development | 3 pts fav | 6 pts fav | 2 pts **UNfav** | 4 pts fav | 7 pts fav |
| catastrophe load | 10 pts | 13 pts | 2 pts | 13 pts | 8 pts |

An 81–83% combined ratio is genuinely good. But **three of the last four years were carried by
favourable prior-year development** (4, then 7 points), which is reserve release, not current
pricing — and **[E4-40]** is explicit that a benign loss run late in a good cycle is *"not only
useless, but actually dangerous"* as a guide. Model exposure, not experience.

### READING (b) — THE HOLDING COMPANY, i.e. the capital-allocation engine

| [E3-03] criterion | verdict | why |
|---|---|---|
| (1) needed or desired | **PASS** | sellers of insurance-adjacent businesses want permanent capital |
| (2) **no close substitute** | **FAIL, and harder than reading (a)** | see below |
| (3) not price-regulated | **PASS** | — |

**The product here is capital, and capital is the most fungible input that exists.** The
filings show WTM buying and selling *alongside and against* the substitutes:
- **Bamboo was sold to CVC Capital Partners** — a private-equity buyer (10-K FY2025, Note:
  Bamboo Sale Transaction, 2025-12-05).
- **BroadStreet was bought through an SPV "alongside co-lead investors Ethos Capital LP and
  British Columbia Investment Management Corporation"** — WTM co-invests with its own
  competitors for deals.
- Distinguished was bought from, and Ark before it, in auctioned processes.

**The attacker's test [E2-45] — "how I would like, assuming I had ample capital and skilled
personnel, to compete with it" — fails outright and instantly: I would raise a fund.** That is
literally what CVC, Ethos and BCI did inside WTM's own FY2025 transactions. There is no
scarce input to defend. → this is also **[E4-23]**: *"if a business requires a superstar to
produce great results, the business itself cannot be deemed great"* — recorded here **at Q2
as a moat defect**, which is where the framework requires it, not at Q3 as a compliment.

### THE STRONGEST SINGLE FACT AGAINST A FRANCHISE — and it is arithmetic

Comprehensive income attributable to common shareholders, five years, from the filed
statements of operations and comprehensive income:

| | 2021 | 2022 | 2023 | 2024 | 2025 | **total** |
|---|---:|---:|---:|---:|---:|---:|
| comprehensive income to common | $(273)M | $788M | $511M | $230M | $1,109M | **$2,365M** |
| of which, gain on ONE disposal | — | **$876M** (NSM) | — | — | **$816M** (Bamboo) | **$1,692M** |

**71.5% of five years of comprehensive income came from two sales of businesses.** Strip them
and the remaining $673M over five years is $135M a year against a $5.0bn market cap. **The
record is a deal-making record.** Under **[E4-36]**'s four causes of extreme success this is
not an ownable max/min of a variable and not a nonlinear combination — it is closest to
**wave-riding**: a decade of cheap capital and rich private-market multiples for
insurance distribution assets. **[E3-51]**: *"the advantage lives in the wave, not the surfer."*

### UNTAPPED PRICING POWER **[E3-33]** — tested, and it points the wrong way

Ark's rate change is **negative**: it is *cutting* price, not declining to raise it. The one
place the test half-fires is **HG Global**, where total gross pricing rose **177bp → 194bp**
(2024 → 2025) and BAM/Assured is a genuine **two-player** market — the closest thing in this
filing to **[E5-28]**'s *"monopoly or near monopoly."* But HG Global is **$45M of pre-tax
income out of $1,329M**, HG Re is contractually capped at 15%-of-par first loss, and WTM
**does not control BAM** (deconsolidated 2024-07-01). **A near-monopoly in 3% of the earnings
does not make the holding company a franchise.**

### THE ATTACKER METRIC — IT DOES NOT ADAPT TO THIS FILER, AND HERE IS WHY

The brief asked for return on unleveraged net tangible operating assets, honestly adapted or
honestly refused. **It is refused, on two grounds:**
1. **"Unleveraged" deletes the business.** An insurer's leverage *is* its float, and
   **[E3-52]** treats float as a *liability without covenants or due dates* — a different
   animal from the bank debt the metric was built to strip out. Removing it does not reveal
   the operating return; it removes the operation.
2. **"Net tangible operating assets" collapses into a securities portfolio.** WTM's operating
   asset is $8.3bn of investments. Return on it is an investment return — a market outcome,
   not evidence of a business advantage. The denominator carries no information about position.

**The honest substitutes, both reported above:** the combined ratio series (which the peer row
below prices relatively) and the risk-adjusted rate change series (which prices it in time).
→ **[METHOD FINDING 10]**.

### THE COMPETITOR ROW — required **[E3-28]**

**The peer set is not mine. It is the one WTM's own 10-K names in Ark's Competition section.**
All figures below are from the peers' own 10-K primary documents on EDGAR; full accession
index and source quotes in `Test Runs/_research 2026-09-02 WTM/competitor_row.md`.

**METRIC 1 — GAAP combined ratio, consolidated, same five years.**

| Company | 2021 | 2022 | 2023 | 2024 | 2025 | **5-yr mean** | rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Arch Capital (ACGL)** | 85.2 | 81.6 | 79.3 | 82.5 | 82.8 | **82.3** | **1** |
| **WTM — Ark** | 87 | 82 | 82 | 83 | 83 | **83.4** | **2** |
| RenaissanceRe (RNR) | 102.1 | 97.7 | 77.9 | 83.9 | 87.2 | 89.8 | 3 |
| SiriusPoint (SPNT) | 109.1 | 96.4 | 84.5 | 88.3 | 88.3 | 93.3 | 4 |
| Everest Group (EG) | 97.8 | 96.0 | 90.9 | 102.3 | 98.6 | 97.1 | 5 |

*Accessions: ACGL 0000947484-26-000017 / 0000947484-23-000015; RNR 0000913144-26-000012;
SPNT 0001576018-26-000032 / 0001576018-23-000016; EG 0001095073-26-000006 /
0001095073-23-000007. WTM 0001628280-26-012603 and the FY2022/FY2023 10-Ks named above.*

**Ark is 2nd of 5 and has never been 1st.** It is a good underwriter in a field of good
underwriters — which is [E3-03] criterion 2 restated as a number. *(Arch's consolidated ratio
is flattered by its Mortgage segment at 14.6%; on the P&C-only cut Arch Insurance is 95.2% and
Arch Reinsurance 80.8% in 2025, so Ark's relative position is better than the table shows.
**Stated because it cuts against my verdict.**)*

**METRIC 2 — book value per share, 2020-12-31 → 2025-12-31, the subject's OWN headline metric.**

| Company | BVPS 2020 | BVPS 2025 | **5-yr CAGR** | rank |
|---|---:|---:|---:|---:|
| **Arch Capital (ACGL)** | $30.31 | $65.11 | **16.5%** | **1** |
| RenaissanceRe (RNR) | $138.46 | $247.00 | **12.3%** | 2 |
| **WHITE MOUNTAINS (WTM)** | **$1,259** | **$2,188** | **11.7%** | **3** |
| Markel (MKL) | *not published* | *not published* | *~10.8% derived* | 4 |
| Everest Group (EG) | $243.25 | $379.83 | **9.3%** | 5 |
| SiriusPoint (SPNT) | $16.88 | $19.40 | 2.8% | *(entity discontinuity — Third Point Re → SiriusPoint 2021; not comparable)* |

### **WTM is 3rd of 5 on its own scorecard, and it trails the S&P 500 total return (14.4%).**

That is the row's decisive contribution. **The "mini Berkshire" premise is that this structure
compounds book value better than a plain insurer. Over the last five years two plain specialty
insurers did it better, and the index did it better than all of them.**

**METRIC 3 — the candor test, calibrated. Who else publishes a reserve RANGE with a position
statement? [E2-67]**

| Company | low / recorded / high range published? | position of the booked number stated? |
|---|---|---|
| **WTM** | **YES** — $1,510.2 / $1,943.2 / $2,023.8 net | **YES** — *"in the upper portion of the actuarial range"* |
| Markel | **YES** — $13.6bn / $16.7bn / $17.8bn net | **YES** — *"more likely to be redundant rather than deficient… generally results in loss reserves that exceed the calculated actuarial point estimate"* |
| Everest | **YES** — $31.7bn / $34.3bn / $36.9bn gross (symmetric ±7.5%) | **YES** — *"management's best estimate… is based upon the point estimate derived by our actuaries"* |
| Arch | **PARTIAL** — Monte Carlo 10th/recorded/90th percentile | **NO** verbal statement; zero hits for "range of reasonable" |
| RenaissanceRe | **NO — expressly refused**: *"**We do not calculate a range of estimates**"*, and its sensitivity analysis *"should not be considered an actuarial reserve range"* | n/a |
| SiriusPoint | **NO** — zero hits for the phrase | n/a |

**This is a genuine WTM strength and the row prices it honestly: 3 of 6 filers do it, so it is
strong practice but not distinguishing.** → **[METHOD FINDING 17]**: the sector method's Q4
substitution 2 calls the reserve-development disclosure *"the strongest candor evidence in the
corpus"*, which invites a run to read a peer-standard disclosure as a Berkshire-like act. **A
candor test with no peer row is a compliment, not a measurement.** The row is what turns it
into one, and it is not currently required by the method's substitution 2.

- **Peers named: 5 sourced, of the 18 WTM itself names.** The other 13 are **not
  SEC registrants** — Ascot, Canopius and Convex are private; Beazley, Hiscox, Lancashire and
  QBE file in London and Sydney; Sompo files in Tokyo; and Chubb and AIG, while filers, are
  $60–200bn conglomerates that do not compete with a $2.5bn-premium Lloyd's book on any
  like-for-like basis. **5 of 18 named, 5 of the ~8 that are both SEC-filing and
  size-comparable.** *(Alleghany (Y) is gone — acquired by Berkshire 2022 and no longer files.)*
- **The row does NOT hold the moat PROVISIONAL**, because it is not being used to establish a
  moat. It is corroborating a criterion-2 failure the filer already stated in Item 1.
- **[E3-61]'s limit on the row, honoured:** the row shows Ark's *position* (2nd of 5) and
  cannot show *conduct*. Whether these eighteen behave like a demented Kellogg in the next
  soft market is not in any of these filings.

- **Must the moat be continuously rebuilt? [E4-04]** — **Yes, and worse: it must be
  re-acquired.** WTM's moat is not defended, it is *replaced* every few years by buying a new
  business. On the [E4-04] scope test set out in the framework (*does the spending defend the
  same advantage, or buy its replacement?*) WTM is the **Mitsui/Rhodes Ridge case, not the
  Coca-Cola case** — $225M for Distinguished, $58M for Enterprise Solutions and $150M into
  BroadStreet in 2025 alone bought *replacement* earnings for the Bamboo earnings that were
  sold. This is the excluded class.
- **Does success depend on a great manager?** **Yes** — recorded at Q2 as a moat defect
  **[E4-23]**, per the framework's explicit instruction.
- **Primary moat metric and its trend: Ark risk-adjusted rate change, +15% → 0% → (4)%.
  Direction: NEGATIVE, three consecutive years.**
- **Class: [x] NONE** *(reading (b), the holding company)* / **NARROW and NARROWING**
  *(reading (a), Ark)* · **Direction: deteriorating on the filer's own published price series**
- **VERDICT: [x] OUT**

**WHY OUT AND NOT UNRESEARCHED.** The competitor row strengthens this finding but is not what
carries it: **[E3-03] criterion 2 fails on White Mountains's own filed words** — eighteen
named competitors, price named first, and a published rate series that has gone negative. The
row is required to *establish* a moat; it is not required to *refute* one that the filer has
already refuted in Item 1. Under the four-verdict test, I can name the document that would
resolve a franchise claim, and I have read it: it is the 10-K, and it says no.

**AND THE COUNTER-CASE, STATED AS [E4-51] REQUIRES.** The best argument that WTM clears Q2 is
this: book value per share compounded at **13.5% a year over six years** (2019 $1,024 →
2025 $2,188), the buyback has been executed at **~92% of book** twice in the record, and HG
Global sits in a two-player market. A holder would say the franchise is *the process* — a
25-year record of buying insurance assets cheap and selling them dear, which no competitor
replicates because most capital is impatient and WTM's is permanent. **I take that seriously
and it is the reason this file does not close at Q1.** It fails anyway, on the framework's
own terms, because **[E4-23]** says a process that lives in the people is not a moat, and
because **71.5% of the record is two disposals** — a series of good decisions, not a
structural position. **[E3-39]/[E2-37]** forbid promoting on it.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**
Case declared, and why: ____

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC, so the test stays point-in-time honest: ____

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — comp not expensed, fanciful pension assumptions → *"seldom just one cockroach in the kitchen"*
- [ ] unintelligible footnotes
- [ ] trumpeted earnings projections / growth targets
- [ ] serial share issuance
- [ ] EBITDA / adjusted-earnings promotion **[E4-29]** *(the fifth flag; 12+ corpus statements)*
- [ ] filed-figure tells: unnaturally smooth reported growth; cash-tax % of pretax falling **[E4-30]**
- For every box ticked, what the filing actually says: ____

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.
- Years used, and the series: ____

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed? *(a one-time item quantified separately at every line passes; the
same item buried in an adjusted figure does not)* ____

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] resists any change in current direction
- [ ] projects/acquisitions materialise to soak up available funds
- [ ] staff studies produced to justify the leader's craving
- [ ] peer behaviour mindlessly imitated

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? ____
- (2) repurchases at a **material discount** to conservatively calculated IV? ____
  *(unquantified because the corpus leaves it unquantified)*
- If (2) fails → **CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**:
  this rests on our own IV range, and management knows the business better than we do.
  **Binds position size, never the discount rate.**
**THE GUARDRAIL — check before writing the verdict.**
- [ ] Confirmed: nothing in this Q3 is being used to **promote** the name. A strong manager
      cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [ ] If this business **requires** a great manager, that is recorded at **Q2 as a moat
      defect [E4-23]** — *"the moat will go when the surgeon goes"* — not here as a strength.
- [ ] If a great manager is the reason to act: is the franchise **already intact** and the
      damage **excisable**, or is the manager the plan? **[E2-35, E2-36]** ____

- **VERDICT: [ ] IN  [ ] OUT (integrity failure is permanent)  [ ] UNRESEARCHED → ____
  [ ] UNKNOWABLE → ____**
  *IN = no disqualifier found. NOT a finding that the managers are honest — "sincerity and
  empathy can easily be faked" **[E5-17]**. IN never promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
- **Short-window mean** (window: ____ ): ____
- **Long-window mean** (window: ____ ): ____
- **Spread, conservative end:** ____ %
- **Combined range** (window spread × capex band): ____ to ____
- *Is that range too wide to reach a conclusion? If yes, **that is the verdict** **[E4-25]** —
  close the file, do not resolve it by preference:* ____
- *A wide spread is also a Q4 finding: a distorted year sits in the window (a pandemic year, an
  acquisition, a disposal), which bears on earnings reliability **[E5-11]**. Name it: ____*
- Owner earnings by year: ____
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** D&A is the default proxy
  **[E3-44, E2-41]**; for capital-intensive businesses the D&A end is INVALID and (c) is judged
  up from total capex **[E5-20]**. Which case is this, and why: ____
- Band used ____ ; where in
  the band it sits and the reason cited from the filing: ____
- Stock compensation subtracted in full **[E5-06]**: ____
- *If the capex band changes the verdict → **UNKNOWABLE**.*

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- Evidence: ____

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings ____
- (2) massive liquid assets ____
- (3) **no significant near-term cash requirements** ____  ← *the one that usually kills*
- Leverage, named and quantified **[E4-16, E3-29]** — *there is no ratio ceiling in this
  framework and the corpus supplies none*: ____

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: ____
- Quantified from filed figures, and the resulting outcome: ____
- Likelihood: [ ] likely [ ] a real possibility [ ] a low-level possibility
- *If no mechanism can be named at all → consider **UNKNOWABLE**.*
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

---
⛔ **Q5 DOES NOT OPEN. Q2 returned OUT and the file is closed.**
**Q3, Q4 and Q6 are NOT ANSWERED and carry no verdict.** Material gathered on them before the
close is reported below under JOB 2 as *method tests*, never as verdicts about the company.

---
# COMPUTATION — NOT A CLEARANCE

*Operator rule 3. The queue's output contract requires a price whether or not the file closes.
**This section carries no entry language and is not a valuation opinion.** It exists for two
reasons: the contract, and because **running the sector method's five steps IS JOB 2** — the
method cannot be tested by describing it.*

**Price $2,105.51** (2026-09-02, Yahoo Finance — aggregator, live quote only, flagged) ·
**shares 2,386,721** (hand-read, 10-Q cover) · **market cap $5,025M** ·
**sovereign 5.27%** (US Treasury 30-yr par, 2026-09-01, issuing authority).

## STEP 1 — INVESTMENTS AT MARKET, NET OF MINORITY INTERESTS **[E5-46]**

At 2026-06-30 (10-Q, acc. 0001628280-26-053932), summed from the six segment columns:

| | $M |
|---|---:|
| Total investments, all segments, at fair value | 8,134.4 |
| Cash (all segments) | 127.5 |
| BAM Surplus Notes, at fair value | 352.8 |
| **gross component 1** | **8,614.7** |
| *less* total debt (six segment columns) | **(932.5)** ← **no rule in the method; see [MF 11]** |
| *less* noncontrolling interests (redeemable 131.5 + nonredeemable 732.2) | **(863.7)** |
| **net component 1** | **6,818.5** = **$2,857/share** |

**[METHOD FINDING 11] — step 1 has no rule for debt, and debt is 18.6% of this market cap.**
[E5-46] takes Berkshire's investments at market and stops; Berkshire's borrowings sat in a
finance subsidiary and were matched, so the omission cost nothing. The sector method inherited
the silence and added only *"excluding any held in a finance operation offset by borrowings."*
WTM carries **$932.5M of debt across five separate segment columns**, none of it in a finance
operation, all of it a prior claim on the same investments. **Not subtracting it overstates
component 1 by $391 per share.** I subtracted it and disclose that the method did not tell
me to.

**[METHOD FINDING 12] — "net of minority interests" is in step 1 without a source.**
[E5-46] does not mention minority interests. The phrase is imported from **[E5-48]**, which
deducts them from the **earnings** factor, not the investments factor. For Berkshire in 2010
the difference was immaterial. For WTM the NCI is **$863.7M against $8.6bn — 10% of component
1**, and whether it belongs in step 1 or step 3 changes the answer by $362 a share. The method
should say which, and cite something.

## STEP 2 — THE COST OF FLOAT **[E3-69]**

**CONVENTION 2 window stated: four years, 2022–2025** — the longest span over which WTM's
segment balance sheet is presented on a comparable basis (Ark was acquired 2021-01-01; the
FY2023 10-K gives 2022, the FY2025 10-K gives 2024–25).

Float constructed each year by the recipe in Stage 0(b) — **no filer-published figure exists:**

| $M, at 31 Dec | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|
| Ark/WM Outrigger constructed float | 653.1 | 1,149.2 | 1,458.0 | 1,611.5 |
| HG Global constructed float | 255.7 | 280.2 | 206.3 | 219.6 |
| **total** | **908.8** | **1,429.4** | **1,664.3** | **1,831.1** |
| Ark net earned premiums | 1,043.4 | 1,409.7 | 1,587.8 | 1,697.4 |
| combined ratio (filer-stated) | 82% | 82% | 82% | 81% |
| **underwriting profit** | **+187.8** | **+253.7** | **+285.8** | **+322.5** |

Four-year mean underwriting profit **+$262.5M**; four-year mean Ark float **$1,218.0M**.

### **COST OF FLOAT = −21.6%.** The float is not merely free; WTM is paid 21.6% a year to hold it.

**[METHOD FINDING 13] — and this is the finding I trust least about my own company verdict,
because [E3-69] read naively says Ark is a superb business.** It is a structural artefact.
**Ark's float-to-premium ratio is 0.95x.** Berkshire's has run 2–3x, because retroactive
reinsurance and long-tail casualty generate years of float per dollar of premium; Ark writes
**property, marine and energy — short-tail business that pays claims in months.**

Hold the combined ratio constant at 81% and vary only claim duration:

| float/premium | underwriting margin | **implied "cost of float"** |
|---|---:|---:|
| 0.95x (Ark, short-tail) | 19% | **−20%** |
| 3.0x (long-tail casualty) | 19% | **−6.3%** |

**Same business quality; the ratio differs by a factor of three.** [E3-69] says *"a low cost of
funds signifies a good business."* As a measure of **the cost of the funds** it is exactly
right and Buffett used it for exactly that. **As a cross-filer measure of business quality it
is not comparable unless claim duration is held constant, and the sector method uses it the
second way.** The fix is not a new number: it is to report **float/premium alongside the
ratio**, so the reader can see whether a spectacular cost of float is underwriting skill or
short tails. Ark's is mostly short tails.

**The honest dollar statement, which the ratio obscures:** the float is $1.8bn. Its funding
benefit against borrowing at ~6% is roughly **$110M a year** — real, and about 2% of the market
cap. The $322M of underwriting profit is not a float benefit at all; it is operating profit
that would exist if the losses paid the same day.

## STEP 3 — PRE-TAX EARNINGS OF EVERYTHING ELSE, DIVIDENDS AND INTEREST REMOVED **[E5-48]**

**This step breaks. It is the most important result of the run.**

| $M | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Consolidated pre-tax income (filed) | 565.4 | 316.7 | 1,328.7 |
| *less* net investment income, all segments | (194.2) | (225.2) | (244.4) |
| *less* interest income, BAM Surplus Notes | — | (15.8) | (29.8) |
| *less* net realized and unrealized investment gains (incl. MediaAlpha) | (434.2) | (184.9) | (361.5) |
| *less* net gain on sale of the Bamboo Group | — | — | (849.3) |
| *add back* unrealized loss on deconsolidation of BAM | — | 114.5 | — |
| *add back / less* change in fair value of BAM Surplus Notes | — | (0.5) | 37.5 |
| **= STEP 3, "earnings from everything else", pre-tax** | **(63.0)** | **4.8** | **(118.8)** |

### **Three-year mean: −$59.0M. Component 2 is NEGATIVE in two of three years.**

**[METHOD FINDING 14] — [E5-48]'S ANTI-DOUBLE-COUNTING RULE DESTROYS ANY BUSINESS WHOSE
OPERATING MODEL IS HOLDING INVESTMENTS, AND THE METHOD GIVES NO RULE FOR TELLING THE TWO
APART.** The rule cannot distinguish:
- **investment income earned on the float-and-surplus portfolio** — which must be removed,
  because step 1 already counted the portfolio; from
- **investment income that IS an operating segment's revenue** — which must not be.

**Kudu is the counter-example and it is not marginal.** Kudu's entire business is buying
minority *revenue* interests in asset managers. GAAP reports its returns as `net investment
income` ($78.7M in 2025) and `net realized and unrealized investment gains` ($103.5M). Kudu
has essentially **no other revenue line** — $1.2M of "other revenues" in 2025. Apply [E5-48]
literally and Kudu's revenue vanishes while its costs (G&A $17.9M, interest $25.9M) remain:
**Kudu contributes −$43.8M to step 3.** A business the filer reports at **+$139.6M of segment
pre-tax income** enters the method at **minus forty-four million.**

**Run it the other way and the answer moves 27%:**

| construction | component 1 | component 2 (3-yr mean) | capitalised at 5.27% | **total** | **per share** |
|---|---:|---:|---:|---:|---:|
| **A — [E5-48] applied literally** | 6,818.5 | **(59.0)** | (1,119.5) | **5,699** | **~$2,390** |
| **B — Kudu treated as an operating business** *(its investments removed from component 1, its investment income kept in component 2)* | 5,359.5 | **+100.1** | +1,899.4 | **7,259** | **~$3,040** |

**The two constructions differ by $650 a share — 27% — and the method contains nothing that
decides between them.** Both are faithful readings of [E5-48]. This is not a WTM problem; it
is waiting for **MKL (Markel Ventures), L (Loews' Boardwalk and Altium), and BRK-B itself**.

**[METHOD FINDING 15] — [E5-48] IS PRE-ASU-2016-01 AND THE METHOD DID NOT NOTICE.** The row is
dated **2015**. ASU 2016-01, effective 2018, forced **unrealized gains on equity securities
through the income statement**. Berkshire in 2015 did not run them through net income; every
filer does now. So [E5-48]'s instruction to remove *"the dividends and interest"* names only
two of the three ways a portfolio now enters pre-tax income, and **omits the largest**: for
WTM in FY2023, realized and unrealized gains were **$434.2M against $194.2M of dividends and
interest — 2.2x larger than the item the rule names.** A run that removed only dividends and
interest, as the row literally says, would count the portfolio twice to the tune of $434M.
I removed them; **the method must be amended to say so, for every name in the queue.**

**[METHOD FINDING 16] — disposal gains are unhandled, and at WTM they are the business.**
[E5-48] is silent on gains from selling whole subsidiaries. At WTM these are not noise:
**$849.3M in FY2025 and $876M in FY2022 — 71.5% of five years of comprehensive income.**
Removing them (as I did — they are realisations of asset value already inside component 1)
makes component 2 negative. Keeping them makes component 2 dominated by lumpy, unrepeatable
items and violates **[E5-49]**'s multi-year discipline in spirit. **The method needs an
explicit ruling. I ruled: remove, and disclose.**

## STEP 4 — RANK AGAINST THE SOVEREIGN

**Not performed as a ranking. The file closed at Q2 and a closed name has no ranking
position.** The arithmetic, for the record only:

- Component 2 yield on market cap, construction A: **−59.0 / 5,025 = −1.2%** · sovereign 5.27%
- Component 2 yield, construction B: **+100.1 / 5,025 = +2.0%** · sovereign 5.27%
- Total two-component value **~$2,390 to ~$3,040 per share** against a price of **$2,105.51**
- Honest pre-tax expectancy is **not computable to the [E4-28] floor's precision**, because
  under construction A the operating earnings are negative and the whole return would have to
  come from the portfolio compounding. The filer's own total portfolio return on invested
  assets was **9.1% (2025)** and **6.9% (2024)**; book value per share compounded at
  **11.7% a year over five years.** Read against the 10% floor that is a **straddle, not a
  clearance**, and the next step explains why the 11.7% should not be extrapolated.

## STEP 5 — THE THIRD ELEMENT **[E5-50]**, MEASURED BY **[E3-54]**. **IT POINTS DOWN.**

[E3-54] as the corpus itself restated it in 2009 has two legs. **White Mountains fails both.**

**Leg (1) — did the book-value gain exceed the S&P over the five years?**
- WTM book value per share **$1,259 (2020-12-31) → $2,188 (2025-12-31) = 11.7% a year.**
  *(Both figures filer-stated: FY2020 10-K acc. 0000776867-21-000004; FY2025 10-K acc.
  0001628280-26-012603.)*
- S&P 500 **total return** index 7,759.4 → 15,220.5 over the same five years = **14.4% a year.**
  *(Yahoo ^SP500TR — aggregator, flagged; no filed source exists for an index.)*
- **WTM trailed by 2.7 points a year. LEG (1) FAILS.**

**Leg (2) — did the stock consistently sell at a premium to book?**
- **No. It has persistently sold at a DISCOUNT, and the filer says so in its own buyback
  disclosures:**
  > FY2022: repurchased 461,256 shares at $1,335.11, *"**or 92% of White Mountains's book
  > value per share** and 89% of White Mountains's adjusted book value per share"*
  > FY2025: repurchased 100,581 shares at $2,013.67, *"**or 92% of White Mountains's December
  > 31, 2025 book value per share**"*
- Today: **$2,105.51 against $2,257 of book = 93%.** **LEG (2) FAILS.**

### **THE THIRD ELEMENT IS APPLIED AS A STATED DOWNWARD JUDGMENT.**
Both legs of the corpus's own retention test fail. Per **[E5-50]** — *"if the CEO's talents or
motives are suspect, today's value must be discounted"* — the judgment here is **not** that
motives are suspect; it is the narrower, measured finding that **$1 retained has not become $1
of market value on either leg of the test the corpus specifies.** The two-component figures
above are stated **before** this discount and are not adjusted downward by a second number,
because **conservatism is spent once [E4-11] and the windage count for this section is ONE**
(the [E5-48] removals in step 3, which I have justified in writing).

**The honest counterweight, which a holder would put first:** WTM's 92%-of-book buybacks mean
management is **buying at the discount rather than complaining about it**, which is
[E5-08] condition (2) satisfied and [E2-51] passed. A persistent discount that management
exploits is a very different fact from one it ignores. **It does not rescue [E3-54], which is
a test of what the market did, not of what management intended.**

---
## Q5 — NOT OPENED. The section below is left as template on purpose.

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: ____ %. Below roughly 10%, the name is not ranked — it is
quit on, whatever the sovereign is. Above it, rank, and capital goes to rank #1 [E3-45].
**No risk premium in the discount rate [E3-42]** — certainty lives at Q1 and in Bar 1's
end discount, never in the rate.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings ____ ÷ market cap ____ = **____ %** · sovereign **____ %**

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote: **____ %**
- what the business has actually done: ____ %

**3. WHAT YOU ARE PAID**
- return at the current price = **____ points over the sovereign**

**THE CERTAINTY SPREAD [E3-13].** The corpus gives a floor of +3% over the long bond for a
business you are certain about, and a direction for less certain ones — no ladder.
- spread used ____ % and the reason: ____
- *Certainty is priced **once**, here. It may not also be priced in the margin of safety.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support:
- conservative ____ · optimistic ____ · **current price** ____

**THERE IS NO HURDLE. THERE IS A RANKING [E4-21].**
- points over sovereign, this name: ____
- against the rest of the opportunity set: ____
- *Take the best available, or nothing.*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — realistic inputs, one margin at the end.
      Margin used ____ %, and which corpus illustration it sits nearest:
      bridge ~35% **[E3-25]** · Grand Canyon 60%, the stated ceiling **[E3-26]** ·
      "closer to a dollar on the dollar" for a business you understand **[E4-12]** ·
      "dollar bills for 80 cents" **[E5-09]**
- [ ] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      No margin is added on top. Three outcomes: below the conservative case → act ·
      **inside the range → no useful conclusion, move on** · above the whole range → no.
- **Windage count** — conservatism applied at how many places? ____ *(more than one must be
  justified in writing)* **[E4-11]**

- **VERDICT: [ ] IN  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____ · ranking position ____**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]:**
- Thesis-confirming metric: ____
- **Thesis-breaking metric and its threshold:** ____
- Next catalyst date: ____

**The sell rule [E2-28]** — two triggers, three hold conditions:
- SELL if the market judges it more valuable than the facts indicate ____
- SELL if funds are needed for something more undervalued or better understood ____
- HOLD while: return on equity capital satisfactory ____ · management competent and honest
  ____ · market does not overvalue ____
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question: is this erosion an aberrational cycle, or has the business slipped in a way that
permanently reduces intrinsic value? ____

**Do not trim winners [E5-14].** **Position size** — a judgment, stated: ____
*(sized DOWN if a capital-allocation flag is live)*

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

---
# JOB 2 — WHERE THE SECTOR METHOD BREAKS

*The brief: **"Every place the method does not fit, is ambiguous, or produces an answer you
cannot defend is a finding I want more than the verdict on the company."** Findings 1, 2, 3
and 8 were folded into the method document by the operator between sessions. Findings 9–20
are new.*

## PART A — THE THREE Q4 SUBSTITUTIONS, RUN AS METHOD TESTS
*Q4 was never opened. Nothing here is a verdict about White Mountains.*

### SUBSTITUTION 1 — liquidity as reserve adequacy and net worth, never cash **[E2-61]**
**The method predicted the error. The error arrived with the sign reversed.**

| test | result |
|---|---|
| **[E5-11] strength (2) run NAIVELY, as on a non-insurer** | cash on hand **$127.5M** against **$932.5M** of debt — 14% coverage. **Reads as a FAIL.** |
| **[E2-61] reading — reserve adequacy and net worth** | net worth **$5,388.3M**; Ark's net reserves **$1,943.2M** booked in the *upper* portion of an actuarial range topping out at **$2,023.8M** — **$80.6M of headroom to the actuarial high against $5.4bn of equity**; A.M. Best FSR "A/stable", issuer credit upgraded to "a+/stable" Nov 2025. **Reads as ample.** |

**[METHOD FINDING 18].** The method warns that the unmodified [E5-11] test *"will return a
FALSE PASS"* on an insurer — cash inflow mistaken for health, the walking-dead symptom. **At
WTM it returns a FALSE FAIL instead.** A holding company that pushes cash down into
subsidiaries and keeps a thin parent balance sheet looks distressed on a cash test and is not.
**The substitution is necessary in both directions and the method states only one.**

### SUBSTITUTION 2 — reserve development as the candor test **[E2-67]**. WTM passes it, and the same table contains the run's second-strongest fact against the company.

**What WTM publishes:** the full ASU 2015-09 ten-year incurred and paid triangles **for five
separate reserving lines** (property & A&H, marine & energy, specialty, casualty-active,
casualty-runoff), plus the low/recorded/high range, plus the position statement, plus the
direction of the error **named in words each year**.

**Direction of the error: FAVOURABLE in four of the last five years.** Note this is the
*opposite* sign to Berkshire's own confession in [E2-67] (*"always presented a better
underwriting picture than was truly the case"*). WTM has been **over**-reserving — reporting
worse than truth.

**And the candor act that counts:** FY2025 was **7 points net favourable**, and the filer
discloses inside it that the figure *"includes **$91 million of unfavourable development
related to aviation losses from the conflict in Ukraine and Russia** resulting from the 2025
U.K. High Court rulings."* **A filer managing the impression omits that sentence.** This is
[E2-26]'s half-owner test performed, not claimed.

**Now the fact it exposes, which cuts hard against the company:**

| Ark | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| **reported combined ratio** | 87 | 82 | **82** | **83** | **83** |
| prior-year development (fav +) | +3 | +6 | **−2** | **+4** | **+7** |
| **accident-year CR, before releases** | 90 | 88 | **80** | **87** | **90** |
| catastrophe load | 10 | 13 | 2 | 13 | 8 |
| accident-year CR ex-catastrophe | 80 | 75 | 78 | 74 | **82** |

### **The reported ratio is flat at 82–83%. The accident-year ratio went 80 → 87 → 90. The gap was filled by reserve releases that grew each year (−2 → +4 → +7 points).**
On the ex-catastrophe cut, **2025 is the worst of the five years.** Both cuts agree: the
underlying deteriorated in 2025 while the headline held — which is exactly what the
risk-adjusted rate change series (+15% → 0% → −4%) said would happen. **[E4-40]** applies:
model exposure, not experience.

**[METHOD FINDING 19] — the reserve triangle is a candor instrument AND an earnings-quality
instrument, and the method only uses the first.** Substitution 2 says *read the triangle,
state the direction, say whether the filer names it.* All three done, and WTM passes all
three. But the same disclosure decomposes the combined ratio into current-year underwriting
and prior-year release, and **that decomposition is where the business news was.** The
substitution should require the accident-year cut, not just the direction.

### SUBSTITUTION 3 — concentration licensed by loss-absorption **[E2-62]**
**Moot in the direction the method guards, live in a direction it does not name.**
WTM does not concentrate its *securities*: $8.1bn of investments spread across fixed maturity,
equity, short-term and other long-term, the largest named equity holding being **MediaAlpha at
$224.5M — 2.7% of investments, 4.2% of equity**, with the filer publishing its own sensitivity
(*"each $1.00 per share increase or decrease in the stock price of MediaAlpha will result in
an approximate $7.00 per share increase or decrease in White Mountains's book value per
share"*).

**[METHOD FINDING 20] — WTM concentrates in whole businesses, not in securities, and [E2-62]
addresses securities.** Distinguished is $744.8M of segment assets bought in one 2025
transaction; Bamboo was $585.7M held for sale at end-2024; Ark carries **$370.0M of contingent
consideration** owed to its own managers. A single failed acquisition is a larger, less
liquid and less reversible concentration than any position in the securities book. **The
method transfers the caution to the wrong asset class for an acquisitive holding company.**

## PART B — PAY VERSUS PERFORMANCE, recorded, no Q3 verdict

**The metric is `CVPS`, and half of it is unobservable to a shareholder** (DEF 14A filed
2026-04-01, acc. 0001104659-26-038487):

> *"For calendar years 2025 and forward, CVPS is the average of growth in **book value per
> share (BVPS)** and growth in **intrinsic value per share, which is the BVPS including
> franchise value adjustments to reflect a conservative estimate of the fair value of certain
> subsidiaries/affiliates carried at book value.** For calendar years through 2024, CVPS is
> the average of growth in **adjusted book value per share (ABVPS)** and growth in intrinsic
> value per share."*

**On [E2-49]** — *"disposition of the yardstick rather than disposition of the manager"* — the
ABVPS→BVPS switch is **the candor case, not the flag**: it was announced ahead, the reason
given (the BAM deconsolidation removed what ABVPS adjusted for), the transition rule published
per performance cycle, and **Annex A reconciles the two.** That is [E2-49]'s own described
exception. **The live item is not the switch; it is that 50% of the weight sits on a
company-defined "franchise value adjustment" whose level is never printed.** *(Markel has made
the same migration — it no longer publishes book value per share at all and leads on
"intrinsic value per share" growth, printing only the growth rate. Two of the queue's Mini
Berks have moved their scorecard to an unpublished self-estimate.)*

**The Item 402(v) table, verbatim from the proxy — and it is the run's strongest single
adverse fact:**

| year | CAP to PEO | **WTM TSR ($100 at end-2020)** | **peer-group TSR** | net income $M | CVPS growth |
|---|---:|---:|---:|---:|---:|
| 2021 | $4,639,595 | **91.08** | **127.58** | (275.4) | (1.2)% |
| 2022 | $23,147,640 | **127.17** | **151.65** | 792.8 | 23.9% |
| 2023 | $11,680,222 | **135.42** | **168.05** | 509.2 | 14.5% |
| 2024 | $14,100,992 | **175.12** | **227.67** | 230.4 | 8.3% |
| 2025 | $16,330,438 | **208.42** | **234.32** | 1,106.4 | 22.8% |

### **White Mountains has trailed its OWN chosen peer group in all five years, in its own proxy, while Compensation Actually Paid to the CEO went from $4.6M to $16.3M.**

Set beside the [E3-54] failure (11.7% book compounding against 14.4% for the S&P) and the
competitor row (3rd of 5 on BVPS CAGR), **three independent measures agree**: over five years
this structure underperformed both its peers and the index. *(The honest offset: 2021's
$(275)M loss year anchors the TSR series at its worst point, and the gap narrowed sharply in
2025, from 52 points to 26.)*

## PART C — THE METHOD FINDINGS, COLLECTED

| # | finding | severity |
|---|---|---|
| **1** | WTM uses the word "float" **15 times and all 15 mean floating-rate debt**; the [E5-46] sense never appears | *folded into method doc* |
| **2** | No ledger row supplies a **construction rule for float from a balance sheet**; Berkshire publishes the number, WTM does not | *folded in as CONVENTION 4* |
| **3** | **Float funds 22.0% of the portfolio** vs Berkshire's 41.8% — a holding company that owns a float-bearing business | *folded in as Stage 0(b)* |
| **8** | Multi-currency: Ark earns in GBP/EUR inside a USD filer; no rule for the sovereign | *folded in as an open question* |
| **9** | **Q2's unit of analysis is undefined for a conglomerate.** CONVENTION 3 splits the *valuation*; nothing splits the *franchise question* | **high** |
| **10** | The **attacker metric does not adapt to an insurer** — "unleveraged" deletes float, and "net tangible operating assets" collapses to a securities portfolio | medium |
| **11** | **Step 1 has no rule for debt.** $932.5M = 18.6% of this market cap, $391/share | **high** |
| **12** | **"Net of minority interests" sits in step 1 with no source** — [E5-48] deducts them from *earnings*. $863.7M, $362/share, unresolved | **high** |
| **13** | **Cost of float is not comparable across claim durations.** Same 81% CR gives −20% at 0.95x float/premium and −6.3% at 3.0x. Report float/premium beside it | **high** |
| **14** | **[E5-48] destroys any business whose operating model IS holding investments.** Kudu enters at −$43.8M against a filed +$139.6M. **The two defensible constructions differ by 27% ($2,390 vs $3,040/share) and the method decides neither** | **critical** |
| **15** | **[E5-48] is a 2015 row and pre-dates ASU 2016-01.** It names only "dividends and interest"; post-2018 the largest portfolio item in pre-tax income is **unrealized gains** — $434.2M vs $194.2M at WTM in FY2023 | **critical — affects every name in the queue** |
| **16** | **Disposal gains are unhandled**, and at WTM they are 71.5% of five years of comprehensive income | **high** |
| **17** | The **candor test has no peer row**, so a peer-standard disclosure reads as exceptional candor. 3 of 6 filers publish the reserve range | medium |
| **18** | Substitution 1 warns of a **false pass**; WTM produces a **false fail**. The warning needs both signs | medium |
| **19** | Substitution 2 uses the triangle only for candor; the **accident-year decomposition** is where the business news was (80 → 87 → 90) | **high** |
| **20** | Substitution 3 guards **securities** concentration; an acquisitive holding company concentrates in **whole businesses** | medium |

## PART D — TOOL DEFECTS FOUND, and they block the next three runs in this track

`tools/sources.py` worked correctly: 5.27%, US Treasury daily par curve, issuing authority,
dated. No defect. `tools/run.py` has three, found by running it on all four Mini Berk names:

**DEFECT 1 — `run.py` has NO insurer detection, and it will mislead MKL and L.**
The whole reason `SECTOR METHOD` exists is that owner earnings is not the right number for a
float-bearing filer. The tool computes one anyway, and prints it beside the sovereign with
"points over the sovereign" attached:

| | tool's owner-earnings yield | tool's "points over the sovereign" |
|---|---|---|
| **MKL** | **10.44% – 10.77%** | **+8.13 to +8.48** |
| **L** | **11.90% – 12.23%** | **+9.65 to +10.00** |

**Both are overstated in a knowable direction.** OCF for an insurer is inflated by float
growth — premiums arrive before losses are paid — which is failure mode 1 named in the sector
method's own opening, and which the UNH run of 2026-08-31 already had to correct by hand.
**MKL and L are the next two names in this track's read order and the tool will hand
whoever runs them a confident, wrong number first.** Fix: `run.py` should refuse, or label,
any filer whose SIC is 63xx.

**DEFECT 2 — `run.py` fails safe on WTM, but by accident.**
It returned `WTM: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED.` That is the right
answer for the wrong reason: WTM does not tag capex in the standard element, not because the
tool knows it is a holding company. MKL and L both tag capex through their non-insurance
subsidiaries (Markel Ventures; Boardwalk Pipelines and Loews Hotels), so **the accidental
safety net does not extend to them** — which is exactly what the table above shows.

**DEFECT 3 — the BRK-B share-class bug is STILL LIVE, unchanged, today.**
The queue recorded it on 2026-09-01 as "a $473M cap and a 4,683% yield." Run today:
> `shares 1.6M   market cap 0.83B USD` … `1. THE YIELD 2668.17% .. 3491.17%`
> `3. POINTS OVER THE SOVEREIGN +94.73 .. +94.73`
The tool is taking an A-share count against the B-share price. **It has not been fixed, and
BRK-B is in this track.** The Stage 0(a) hand-read is the mitigation, and it worked here — but
a mitigation that depends on the analyst remembering is not a fix.

### THE ONE-LINE VERDICT ON THE METHOD
**It runs, and it is better than having nothing — Stage 0(b), step 2 and step 5 all did real
work and step 5 produced a clean two-legged failure. But steps 1 and 3 are under-specified to
the point where two honest analysts would differ by 27% on the answer, and finding 15 means
every Mini Berk run done under the current text would double-count unrealized gains.
Findings 14 and 15 should be fixed before MKL is run, not after.**

---
## SELF-AUDIT
- [x] Questions answered in order; **stopped at Q2 OUT.** Q3, Q4, Q5, Q6 not answered and carry no verdict
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN is unqualified; the composition problem it names is carried forward, not used to hedge the verdict
- [x] No UNRESEARCHED verdict issued — nothing to work-order
- [x] No UNKNOWABLE verdict issued
- [x] Step 0: filing read (10-K FY2025 acc. 0001628280-26-012603; 10-Q Q2-2026 acc. 0001628280-26-053932; DEF 14A acc. 0001104659-26-038487; plus FY2020/FY2022/FY2023 10-Ks for the historical series); **cross-check performed** — Ark's $2,481.0M gross reserve rollforward ties to the balance-sheet line and to the 10-Q comparative
- [x] **Owner earnings NOT built — correctly.** The sector method replaces it for this filer class; the substitute (two components plus a judgment) is computed under COMPUTATION — NOT A CLEARANCE, with the float window stated per CONVENTION 2 (four years, 2022–2025)
- [x] Competitor row filled — 5 peers, all from the set WTM's own 10-K names, all filing-sourced with accessions; coverage stated (5 of 18 named, 5 of ~8 SEC-filing and size-comparable)
- [x] Sovereign 5.27%, USD, US Treasury daily par curve (issuing authority), 2026-09-01 — with the multi-currency gap disclosed as unresolved, not papered over
- [x] Value stated as a round-number range (**~$2,390 to ~$3,040/share**), not a point estimate
- [x] **Neither bar applied** — Bar 1 and Bar 2 both price an entry decision, and the file is closed. **Windage count: ONE** (the [E5-48] removals in step 3, justified in writing)
- [x] Prices dated; **aggregator (Yahoo) used for the live quote and the S&P total-return index only, both flagged**; every company figure is filing-sourced
- [x] Run committed to git after Step 0/Q1, after Q2, after the computation, and after the competitor row

## REGISTER
- **Verdict: [x] OUT (about the business), at Q2.**
- **One line:** White Mountains is a well-run buy-operate-and-sell holding company whose own
  10-K names eighteen competitors, whose own published price series has gone **+15% → 0% →
  (4)%** while it grew premium 76%, and **71.5% of whose last five years of comprehensive
  income came from two disposals** — a deal-making record, not a franchise.
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.

---
# OUTPUT CONTRACT

## THE PRICE
**$2,105.51 per share** (2026-09-02; Yahoo Finance, aggregator, live quote only, flagged).
Market cap **$5,025M** on **2,386,721** shares hand-read off the 10-Q cover.
Two-component sector-method value, **COMPUTATION — NOT A CLEARANCE**:
**~$2,390 to ~$3,040 per share**, the width being the unresolved [E5-48] question at
[METHOD FINDING 14], **before** the [E5-50] third element, which is a **stated downward**
judgment because both legs of [E3-54] fail.

## PASS / FAIL
# **FAIL — the file closed at Q2 (OUT).**
**[E3-03] criterion 2 fails**: eighteen named competitors in the filer's own Competition
section, price listed first among competitive factors, and a published risk-adjusted rate
change of **−4%**. The attacker's test **[E2-45]** fails outright — the answer to *"how would
I compete with this"* is *"raise a fund"*, which is what CVC, Ethos Capital and BCI did inside
WTM's own 2025 transactions. **This is the fourteenth consecutive watchlist name to close at
Q2 — but on a differently-selected population, which was the point of running it.**
