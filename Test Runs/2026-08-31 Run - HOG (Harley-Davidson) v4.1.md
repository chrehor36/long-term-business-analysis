# Company Run: Harley-Davidson, Inc. (NYSE: HOG), 2026-08-31
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`.

**Position context: NONE HELD. Fresh entry run.** Surfaced by the 2026-08-31 prepped
reading list as the **highest statute yield with a real brand (11.6%)**. ~$2,750 of
TAXABLE capital is earmarked for the first name that graduates.

**BIAS DECLARED, operator rule 9.** An 11.6% statute yield on the most famous industrial
brand in America is exactly the shape that has failed five times in this project. ETD,
FLO, OXM, WEYS, COLM. The analyst's incentive is to clear it; the antidote is the
corpus's own, hunt disconfirming evidence hardest for the favourite hypothesis
**[E4-26]**, *"you must not fool yourself, and you're the easiest person to fool"*
**[E3-41]**. The **iron prescription [E4-51]** is applied at Q4: the bull case is stated
as its best advocate would state it, from the company's own raised guidance and its new
strategic plan, before it is answered. **A "no" is a fully successful run.**

**Evidence committed alongside this file:**
- `Test Runs/_research 2026-08-26/HOG dividend decomposition 2019-2026.md`
- `Test Runs/_research 2026-08-26/HOG unit, share and dealer series 2014-2026.md`
- `Test Runs/_research 2026-08-26/HOG two-business separation and owner earnings.md`
- `Test Runs/_research 2026-08-26/HOG competitor row (PII-DOO).md`

---
# STAGE 0: THE FIVE-MINUTE ARTIFACT CHECK
*Reported first, per the run-order protocol. Three questions: is the cap real, is the
dividend real, is the yield a boom-window artifact?*

## (a) THE CAP, clean

| | |
|---|---|
| Share class structure | **ONE class.** Common stock, $0.01 par. Preferred authorised 2,000,000, **none issued** (FY2025 10-K Note 4). No dual class, no tracking stock. |
| Total economic shares | **104,072,507** |
| Share-count date | **2026-07-31**, filed cover of the Q2 2026 10-Q, acc. 0000793952-26-000061, filed 2026-08-05. **One month old. Current.** |
| Cross-check | FY2025 10-K cover: 111,850,563 at 2026-01-30. The 7.0% decline in six months reconciles to the ASR settlement (3,147,971 shares delivered 2026-02-13) plus $100.4M of open-market repurchases in H1 2026, 7.9M shares total, per the Q2 2026 press release. **Reconciles.** |
| Price | **$27.52**, 2026-08-31 (Yahoo Finance, **aggregator, live quote only, flagged**) |
| **Market capitalisation** | **$2,864M** |

**One contingent-dilution item, recorded and not netted:** KKR and PIMCO hold a 9.8%
non-controlling interest in HDFS exchangeable into HOG common stock **from Q4 2032** (or
on a change of control) at 1.75x HDFS's equity carrying value, **capped at 4.9% of HOG's
outstanding shares** (Q2 2026 10-Q, EPS note). Not dilutive today, capped, and six years
away. **The cap is not an artifact. LEVI-class failure does not apply here.**

## (b) THE DIVIDEND: AN ARTIFACT, CONFIRMED AND QUANTIFIED

The operator's prior integrity pass is **confirmed in full from the filings**:

| FY | cash dividends per share (face of the income statement) | implied quarterly | % of the 2019 rate |
|---|---:|---:|---:|
| **2019** | **$1.50** | **$0.375** | 100% |
| 2020 | $0.44 | $0.375 Q1, then **$0.02** | **5.3% run-rate** |
| 2021 | $0.60 | $0.15 | 40% |
| 2022 | $0.63 | ~$0.1575 | 42% |
| 2023 | $0.66 | $0.165 | 44% |
| 2024 | $0.69 | $0.1725 | 46% |
| 2025 | $0.72 | $0.18 | 48% |
| **2026 (H1, filed)** | $0.375 for six months | **$0.1875** | **exactly 50.0%** |

Arithmetic proof of the cut: $0.375 + (3 x $0.02) = $0.435, filed as $0.44. **A 94.7%
reduction in the quarterly rate, taken in Q2 2020.**

**Where the screen's "+17% five-year growth" comes from.** `Screens/prep_lists.py`
line 245 computes `(TTM dividends now / TTM dividends 5 years ago) ^ 0.2 - 1`:
- TTM now: $0.18 + $0.18 + $0.1875 + $0.1875 = **$0.735**
- TTM five years ago (Aug 2020 - Aug 2021): **$0.02 + $0.02** + $0.15 + $0.15 = **$0.34**
- (0.735 / 0.34) ^ 0.2 - 1 = **+16.7%**, printed as **+17%**

**The base window contains two quarters at the emergency $0.02 rate.** The entire growth
figure is the climb out of the cut. The same window construction is why the screen's own
`div_cut_5y` flag reads False, the lookback starts *after* the cut.

**Cash, not per-share, is the sharper fact:** dollars distributed fell from **$237.2M
(2019) to $86.4M (2025)**, a 64% decline, on a share count down 27%. Buybacks have
absorbed **4.3x** the dividend cash since 2023 ($1,177M vs $274M).

> **RECORDED: HOG FAILS THE OPERATOR'S DIVIDEND-COMPOUNDER MANDATE OUTRIGHT.** It cut
> 94.7% in 2020, it has not restored half the 2019 rate in six years, the growth number
> that put it on the list is the cut measured backwards, and dividends rank **second**
> behind strategic initiatives in the company's own stated capital-allocation priorities
> (FY2025 10-K, Item 5). **From here the name is run as a VALUE / CYCLICAL read on its
> own merits, with zero credit taken for dividend growth.**

## (c) THE BOOM-WINDOW ARTIFACT CHECK **[E4-41]**: TWO booms in the window, not one

*"normalize the mean DOWN for luck … Favourable exogenous breaks in the window are named
and removed before the mean is trusted."*

**Boom 1, the 2021-2023 powersports demand and pricing boom.** HDMC segment operating
income: $476.8M (2021), **$677.1M (2022), $661.2M (2023)**, $277.8M (2024), **-$28.7M
(2025)**, guided **+$10M to +$50M (2026)**. Revenue per retail unit rose from $20,949
(2019) to **$29,763 (2023)** and is back to $26,999. **Any five-year window ending in
2025 contains the two highest HDMC profit years in the company's modern history and the
demand regime that produced them has ended.**

**Boom 2, and this one is bigger and is inside the screen's own numerator.** The
statute yield of 11.6% is worst-five-year net income ($338.7M, 2025) over the cap. **That
$338.7M contains a net $135.3M pre-tax one-time credit from the Q4 2025 HDFS
Transaction**, a $191.4M release of the allowance for credit losses on receivables sold,
plus a $27.9M gain on securitisation residuals, less an $11.4M loss on sale and a $72.6M
loss on debt extinguishment. At the 2025 effective rate that is roughly **+$97M after
tax**. Clean 2025 net income was closer to **$240M**, and the statute yield closer to
**8.4%**, not 11.6%.

**And the deeper artifact: the motorcycle company lost money in 2025.** HDMC segment
operating income was **-$28.7M**. Every dollar of 2025 reported profit came from the
finance company, and $191.4M of the finance company's profit was an accounting release.

> **STAGE 0 VERDICT: the cap survives; the dividend and the yield do not.** The name is
> not closed at Stage 0. The manufacturing business is legible and the balance sheet is
> real, but it enters the framework stripped of both reasons it was on the list.

---
## STEP 0: THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · observed 2026-08-27 · FRED `DGS30`**, pulled directly from
  `fredgraph.csv` (Treasury constant maturity, the project's standing USD source). FRED's
  known 1-2 day publication lag is immaterial and noted. Taken as **the currently observed
  rate, never a forecast [E3-32]**.
- FX: none material to the yardstick. Quote currency = reporting currency = USD. 67% of
  HDMC revenue is US; the largest non-USD exposures are EUR (a EUR 610.0M medium-term
  note at HDFS) and EMEA/Japan sales.
- Price: **$27.52, 2026-08-31** (Yahoo, aggregator, live quote only, flagged).

**The filing was read, not tagged data [E3-27, E4-14]:**
1. **FY2025 Form 10-K**, year ended 2025-12-31, **filed 2026-02-26, accession
   0000793952-26-000011**. Auditor **Ernst & Young LLP** (auditor since 1982),
   unqualified opinion on the statements and on internal control.
   [x] MD&A (Overview, Key Factors, Guidance, Results, Liquidity)
   [x] cash-flow statement **including its detail lines and Note 5 supplemental**
   [x] footnotes. Note 4 capital stock, Note 6 finance receivables, Note 10 debt,
       Note 11 VIEs, Note 15 commitments and contingencies, Note 16 share-based awards,
       Note 18 reportable segments, **Note 19 supplemental consolidating data**,
       plus the E&Y **critical audit matter** on the transfer of financial assets.
2. **Q2 2026 Form 10-Q**, period ended 2026-06-30, **filed 2026-08-05, accession
   0000793952-26-000061** (cover share count; H1 consolidating data; segment results;
   HDFS credit metrics; "Back to the Bricks").
3. **DEF 14A filed 2026-04-09, accession 0000793952-26-000022** (meeting 2026-05-21;
   CEO transition, board refreshment, compensation, beneficial ownership).
4. Supporting: **FY2024 10-K** acc. 0000793952-25-000063; **FY2023 10-K** acc.
   0000793952-24-000076; **FY2021 10-K** acc. 0000793952-22-000014; **FY2019 10-K** acc.
   0000793952-20-000008; **FY2015 10-K** acc. 0000793952-16-000047 (the long unit and
   share series); **8-K 2026-07-23** acc. 0000793952-26-000058 (Q2 2026 release and
   raised guidance); **8-K 2026-06-26** acc. 0000793952-26-000050 (officer change);
   **8-K 2025-04-10** acc. 0000793952-25-000085 (Dourdeville resignation and the
   company's point-by-point response); **8-K 2025-05-19** acc. 0001104659-25-050474
   (2025 annual-meeting vote); **DEF 14A 2025-04-03** acc. 0000793952-25-000076.

**Figure cross-checked against the filed statement (operator rule 4):** FY2025 net cash
provided by operating activities. The filed Consolidated Statements of Cash Flows reads
**$568,922** thousand; **Note 5** (supplemental cash-flow detail) reconciles to the same
**$568,922**; the MD&A "Cash Flow Activity" table carries **$568,922**. **Three-way match
inside the document.** Second check, and the one that matters for method: **Note 19's
Non-Financial Services column reconciles to the cent**, non-FS net income $976,716 less
the $1,000,000 intercompany dividend from HDFS, bridged through D&A, SBC, the non-cash
pension credit and the working-capital change, gives **$283,515**, exactly non-FS OCF
$1,283,515 less $1,000,000. The reconciliation is set out in the committed evidence file.

---
# THE METHOD PROBLEM, HANDLED FIRST: HOG IS TWO BUSINESSES

**Treatment adopted, stated explicitly:**

1. **The manufacturing business is valued on owner earnings.** Its perimeter is Note 19's
   **Non-Financial Services Entities** (HDMC + LiveWire + the parent). Owner earnings are
   computed the framework way, a multi-year mean of (operating cash flow less SBC) less
   the (c) guess, with **one mandatory correction**: non-FS operating cash flow contains
   the **intercompany dividend HDFS pays up to the parent** ($239.9M in 2021, ~$200M in
   2022-2024, **$1,000.0M in 2025**, $100.0M in H1 2026). That is not an operating cash
   flow of the motorcycle company and it is removed. Removing it is not a judgment: it
   equals the consolidating adjustment to net income each year, and the 2025 bridge
   reconciles exactly.
2. **The finance business is valued separately**, at its filed book equity attributable
   to HOG, cross-checked against a **market-tested price**: KKR and PIMCO each paid
   $23.3M for 4.9% of HDFS in Q4 2025, **9.8% for $46.6M, implying $476M for 100%**,
   which the company states was "approximately 1.75x HDFS's post-transaction equity
   carrying value." HDFS book equity at 2026-06-30 is **$377.0M**; HOG's 90.2% share is
   **$340M at book, $429M at the KKR/PIMCO price**.
3. **NO blended consolidated owner-earnings yield is reported anywhere in this run as a
   valuation input**, and here is the demonstration of why: consolidated operating cash
   flow was **+$568.9M in FY2025 and NEGATIVE $59.7M in H1 2026**, same company, opposite
   sign, entirely because of where finance receivables sit relative to the held-for-sale
   line. Consolidated debt likewise fell from $6,960M to $2,967M in one year without a
   dollar of the motorcycle company's obligations changing. **A consolidated yield on
   this filer is an artifact of the finance book's funding, and the screen's 11.6% is
   exactly that artifact.**

**What the separation shows on the balance sheet (Note 19, at 2026-06-30):**

| $M | manufacturing (non-FS) | finance (HDFS) |
|---|---:|---:|
| Cash | **1,283.3** | 612.5 |
| Finance receivables | n/a | 2,645.2 |
| Total assets | 4,308.8 | 3,446.3 |
| Short-term debt + current LTD | **, ** | 1,111.6 |
| Long-term debt | **297.3** | 833.5 |
| Deposits | n/a | 516.5 |
| Equity | 2,864.5 | **377.0** |

**The manufacturing entity carries exactly one debt instrument: $300M of 4.625% senior
notes issued July 2015, due 2045.** **Terms read [E3-52]:** nineteen years to maturity,
fixed coupon, and the filing states plainly that **"No financial covenants are required
under the medium-term or senior notes."** Interest ~$13.9M/year. Manufacturing **net cash
of +$986.0M**. This is a covenant-free, long-dated, trivially small obligation, the
benign end of [E3-52]'s spectrum, and nothing like the covenanted bank debt the LOW/RPM
leverage discipline was built for.

**All the leverage is at HDFS**: $1,945M of debt plus $516M of deposits on $377M of
equity, roughly 6.5x, with a credit-facility covenant permitting up to **10.0x**. Ratings
at 2025-12-31: Moody's **Baa3** stable, S&P **BBB- CreditWatch Negative**, Fitch BBB+
stable, **one notch above non-investment grade at two of three agencies.**

**Coverage test [E2-54] on the MANUFACTURING business's obligations**, *"all interest,
both payable and accrued, comfortably met out of current cash flow net of ample capital
expenditures"*:

| | 2024 | 2025 | 2026 (on guidance) |
|---|---:|---:|---:|
| manufacturing interest expense | $30.7M | $33.4M | ~$14M |
| manufacturing OCF less capex | $336.3M | $131.0M | **negative** |
| coverage | 11.0x | 3.9x | **fails on flow** |

The 2026 failure has no solvency consequence, $1.28bn of gross cash against $14M of
interest and a 2045 maturity, but it is the honest reading and it is recorded: **the
obligations are trivial; the cash flow that is supposed to cover them is guided to be
more trivial still.**

---
## Q1: CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics, in my own words, without management's language.** Harley-Davidson
  builds heavy motorcycles, mostly touring and cruiser models over 600cc, in a handful
  of US plants plus Thailand, and sells them **wholesale** to about **1,174 independent
  dealership points** in ~100 countries. The dealer takes the inventory risk (financed by
  Harley's own floorplan lender) and sells to a retail buyer. Harley books revenue on
  shipment, not on retail sale, so **wholesale shipments and retail sales are two
  different series and they diverge for years at a time**, the single most important
  thing to understand about reading this company. A second, higher-margin stream comes
  from parts, accessories, apparel and trademark licensing on the installed base
  (~$256M of P&A + apparel/licensing revenue in Q2 2026 alone, 22% of HDMC revenue).
  A third stream is **HDFS**, which lends to the dealer (floorplan) and to the retail
  buyer (installment), and since Q4 2025 sells up to two-thirds of new retail
  originations to KKR and PIMCO while keeping the servicing fee.
- **The scarce input the business controls: the trademark and the sound.** Not the
  factory, not the engineering, not distribution. The Bar and Shield has been in use
  since 1910; the V-twin's identity is the product. Everything else in the model,
  plants, dealers, the finance book, is replaceable and has been partially replaced.
  **This is a brand-and-installed-base business wearing a manufacturer's balance sheet.**
- **Will the fundamentals look broadly the same in ten years?** The *mechanism* will:
  people who want a large American cruiser will buy one from a dealer and finance it. The
  *scale* will not, and that is Q2's question, not Q1's. One genuine intelligibility
  caveat is recorded and answered: the two-business structure would make consolidated
  numbers unreadable, but **the company publishes separate consolidating statements in
  Note 19**, so the ambiguity is removable from the filings and was removed above.
- **VERDICT: [x] IN.** The business is legible; a competent reader can state the unit
  economics and name the scarce input in a paragraph. The cyclical level lands at Q4/Q5
  as range width; the secular direction is Q2's question.

## Q2: IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by
> its customers to have **no close substitute** and; (3) is not subject to price
> regulation." **[E3-03]**

- Needed or desired **[x]**, demonstrably, for 123 years.
- Not price-regulated **[x]**, no price regulation. (Tariffs are a cost, not a price cap;
  see the [E2-59] note below.)
- **No close substitute [ ]. FAILS, and the filed evidence is the strongest this project
  has yet assembled on a Q2.**

### The physical series, which is the honest one **[E4-55]**

*"Precision Steel's pounds fell 69M -> 46M while price rises held dollar revenue level,
'a serious reverse, not likely to disappear in some bounce back effect.'"*

| | 2015 | 2019 | 2023 | **2025** | change |
|---|---:|---:|---:|---:|---:|
| Worldwide retail units | 264,627 | 218,273 | 162,771 | **132,535** | **-50.1% since 2015** |
| U.S. retail units | 168,240 | 125,960 | 98,468 | **82,698** | **-50.8% since 2015** |
| Dealership points | 1,435 | 1,569 | 1,277 | **1,174** | **-25.2% since 2019** |
| **U.S. 601+cc market share** | n/a | 49.1% | 37.9% | **34.5%** | **-16.2 pts since 2017 (50.7%)** |
| Europe 601+cc market share | n/a | 9.1% | 4.8% | **3.4%** | **-5.7 pts since 2019** |

**And the dollars-versus-units test resolves cleanly.** HDMC revenue per retail unit:
$20,949 (2019) -> **$29,763 (2023)** -> $26,999 (2025). From 2019 to 2023 **units fell 25%
while dollars per unit rose 42%**, so dollar revenue *rose* 6%, the classic disguise.
From 2023 to 2025 **the price lever stopped working**: units -19%, dollars per unit -9%,
revenue -26%, and **HDMC segment operating income went from $661.2M to -$28.7M.**

In 2025 the U.S. 601+cc industry fell 6.1% and Harley fell **12.9%**, it declined at
roughly twice the industry rate. **Macro explains about half. The other half is
substitution.**

### [E2-44], the two-characteristic test: **0 of 2 today, 1 of 2 historically**

1. *Raise prices when demand is flat and capacity is not fully utilised?* It **could**,
   1919-2023, that is what the +42% per-unit figure is. It **cannot now**: the FY2023
   10-K describes "the elimination of the pricing surcharge in 2023 and a fine-tuned
   pricing strategy in 2024"; the Q2 2026 press release lists **"net pricing"** among the
   items that *hurt* gross margin, which fell 108bp to 27.5%. **Fails today.**
2. *Grow dollar volume with only minor additional capital?* HDMC revenue $4,845M (2023)
   -> $3,578M (2025) on capex of $189M and $149M. **Fails.**

### [E4-37], the agony test, and it has flipped in real time

*"you can almost measure the strength of a business over time by the agony they go
through in determining whether a price increase can be sustained … it's not a great
business when you have to have a prayer session before you raise your prices a penny."*

The 2021-2023 filings are yawn-class: price rose, mix improved, margin expanded. The
2025-2026 filings are agony-class: pricing is a negative in the margin bridge, tariffs of
**$67M (2025) rising to $75-105M (2026 estimate)** are being absorbed rather than passed
on, and the strategic plan's answer to demand is a **cheaper** motorcycle (the "Sprint"
small-displacement model) and the return of the Sportster. **[E4-37] detects a moat
downgrade in real time; it has detected one.**

### [E2-45], the attacker's test, answered empirically rather than hypothetically

The question is how one would attack this business with ample capital and skilled
personnel. **The attack already happened and it won.** Between 2017 and 2025 Harley gave
up **16.2 points of U.S. 601+cc share** and **61% of its European registrations**. The
competitor row (committed separately) names who took it. And the most damaging attacker
is one Harley manufactures itself:

> "when the supply of used motorcycles increases or the prices for used Harley-Davidson
> motorcycles decline, there can be reduced demand among retail purchasers for new
> Harley-Davidson motorcycles **at or near manufacturer's suggested retail prices**"
> Source: FY2025 10-K, Item 1A

A durable good sold to an installed base that is not being replaced generates its own
substitute supply. Every Harley ever built is still a Harley. **That is the structural
reason the pricing lever exhausted.**

### THE COMPETITOR ROW, required **[E3-28]**

Built and committed as `Test Runs/_research 2026-08-26/HOG competitor row (PII-DOO).md`,
with every accession and the fiscal-calendar differences stated there. **Peers taken:
Polaris Inc. (NYSE: PII), which owned Indian Motorcycle, and BRP Inc. (TSX/Nasdaq: DOO),
reached through SEC EDGAR as a 40-F filer, no fallback route needed, no aggregator used.**

**THE ROW RETURNED A MARKET-CLEARING PRICE, AND IT IS THE STRONGEST SINGLE FACT IN THIS
FILE.**

> **Polaris, the disclosed number two in North American 900cc+ motorcycles, sold Indian
> Motorcycle to Carolwood LP for "a nominal sales price," took $342.5M of charges, wrote
> On Road segment goodwill to zero, and recorded a NET CASH OUTFLOW of $79.3M to complete
> the disposal.** Announced 2025-10-10, closed **2026-02-02**.
> Source: Polaris FY2025 10-K, acc. 0001628280-26-008033, Note 4; 8-K acc. 0001628280-25-044839;
> Q2 2026 10-Q, acc. 0001628280-26-050104

**[E2-45]'s attacker's test is normally hypothetical. Here the incumbent attacker answered
it by leaving, and paid to leave.** A rational, well-capitalised operator, at arm's length,
ten months ago, valued a heavyweight motorcycle franchise with ~$478M of revenue at
approximately nothing, and the buyer was private equity, not a strategic. Polaris told
its own shareholders the separation would be **accretive by ~$50M of adjusted EBITDA and
~$1.00 of adjusted EPS.** The claim *"we held the number two position in North America
market share for the 900cc+ category"*, present in the FY2023 and FY2024 10-Ks, **is absent
from the FY2025 10-K**, along with the industry table, the INDIAN trademark and any
motorcycle retail metric in the Q2 2026 MD&A.

| | **HOG** (Dec FYE) | **Polaris** (Dec FYE) | **BRP** (Jan FYE, CAD) |
|---|---|---|---|
| Latest full-year revenue | $4,473.2M (2025) | $7,152.0M (2025) | C$8,442.7M (FY2026) |
| Operating margin, latest FY | 8.6% consolidated / **-0.8% HDMC** | **(4.9)%** | **4.7%** |
| Operating margin, 2 yrs earlier | 13.3% / **13.6% HDMC** | 7.8% | 14.1% |
| Motorcycle position | **34.5% US 601+cc, from 50.7% (2017)** | **#2 in NA 900cc+. EXITED 2026-02-02** | 3WV leader; **#3 global e-moto** |
| Captive finance | **CONSOLIDATED (HDFS)** | equity-method JV, **off balance sheet** ($131.5M carrying value) | **none, third-party floor plan only** |
| Dividend record | **cut 94.7% in 2020; still half the 2019 rate** | **31 consecutive years of increases**, $150.3M paid into a $465.5M loss year | n/a |

- Peers named: **2 of roughly 6 real competitors** (Polaris/Indian, BRP, BMW Motorrad,
  Honda, Yamaha, Kawasaki/Suzuki). BMW and the three Japanese majors report motorcycles
  inside conglomerate segments and are **not retrievable at a comparable metric**, the
  shortfall is named and carried as a work order. The row is therefore supplemented by the
  industry registration series, which captures all of them at once in the only metric that
  matters here: **units, and share of units.**
- **Row limit stated [E3-61]:** the row shows position; it cannot show conduct.

**What the row establishes that the subject's own numbers cannot:**

1. **The category is shrinking on four independently constructed measures, not one.**
   Polaris's internal NA 900cc+ estimate fell from 190,000 units (2020) to roughly 156,000
   (2025). BRP's global three-wheel market, where Can-Am competes directly with Harley's
   Trikes, fell from ~38,000 (2023) to ~32,000 (2024) to **~27,000 units (2025), -29% in
   two years.** BRP's global electric motorcycle market is **~6,000 units and -18%**, which
   is the best primary-source read available on **LiveWire's addressable market, and Harley
   has spent $525-535M since 2021 to compete in it.** Harley's own MIC-sourced US 601+cc
   series is down 7.4% in two years. **Four estimates, four sources, one direction.**
2. **The distress is specific to heavyweight two-wheel, not to discretionary powersports.**
   Polaris posted a Q2 2026 operating margin of 7.4% on a 23.7% gross margin; BRP posted
   Q1 FY2027 revenue +29.5% on a 23.5% gross margin; both cut network inventories ~17% and
   report retail stabilising. **The peers' non-motorcycle powersports businesses are
   recovering while motorcycles are not.** That materially weakens any "it is only the
   cycle" framing for Harley, and it is the one thing a competitor row shows best:
   whether the trouble is the industry or the company.
3. **Neither peer is a franchise in motorcycles either.** Polaris has left. BRP's overlap is
   a shrinking 3WV niche plus a sub-scale EV line it has just impaired by **C$229.8M**,
   while disclosing a decision to *"limit further EV investments"*, the same conclusion
   Harley reached about LiveWire in the same year, from the other side of the market.
4. **The financing structures differ fundamentally**, which is the independent
   justification for this run's two-business separation: Harley **consolidates** HDFS;
   Polaris carries Polaris Acceptance as an **equity-method JV** with $1,781.4M of finance
   receivables and $1,470.8M of notes payable **off** its balance sheet; BRP has **no
   captive at all.** Comparing Harley's consolidated operating margin to either peer's
   without separating HDFS would be comparing three different animals.
5. **A caution, recorded rather than buried.** Neither Polaris nor BRP cites the Motorcycle
   Industry Council or any 601+cc series; both state their industry figures are internal
   management estimates. **The 601+cc series that anchors the market-share finding above is
   single-sourced from Harley's own filings** and is not independently corroborated at the
   same definition. Polaris's independently constructed series shows the same *direction* on
   a different definition and geography. The run reports both and treats neither as the
   other.
6. **And the registration series still gives what no company row can:** the US 601+cc market
   shrank 6.1% in 2025 and Harley shrank 12.9%; the European 601+cc market **grew 9.0% in
   2024** while Harley's European share went 4.8% -> 5.0% -> 3.4%. **Harley is losing share
   into both a shrinking market and a growing one.** That is not a cycle.

### The remaining Q2 tests, run and recorded

- **[E2-53] the dominance class.** Harley **was** the textbook case, *"Once dominant …
  Good or bad, it will prosper"*, at **50.7% of U.S. 601+cc registrations in 2017**. At
  34.5% it is a large share-holder in a shrinking category, not a dominant one. The
  franchise this test describes existed and has been leaving for a decade.
- **[E3-46] the second question about the business is a number.** Manufacturing return on
  manufacturing equity (Note 19): **27.1% (2021), 27.7% (2022), 24.1% (2023), 11.4%
  (2024), -0.9% (2025).** A high-return business four years ago; not one now.
- **[E3-33] / [E5-28] untapped pricing power: none.** The lever has been used to
  exhaustion and its exhaustion is what 2025 was. The near-monopoly claim [E5-28] requires
  cannot be made about a company that has lost 16 points of share.
- **[E2-58] the commodity doctrine** does not apply: this is a differentiated premium
  product, and the failure is substitution and demographics, not over-capacity pricing.
  **[E2-59]**, however, is live and is recorded as a *negative* here: tariffs are a
  regime, the regime is currently costing $67-105M a year, the Supreme Court struck the
  IEEPA tariffs on 2026-02-20, and **a regime that can give can take**, the 2018-2021 EU
  rebalancing tariffs took Harley's landed EU duty to **31%** and are a live template.
  Credited as nothing in either direction.
- **[E4-23] the Mayo test, passes, and it is the one real positive.** Harley's moat does
  not require a superstar; the brand outlived Zeitz, Levatich, Wandell and Bleustein. The
  moat defect is not key-person dependence. **It is that the moat is shrinking on its own.**
- **[E4-04] / [E5-23] does the moat need rebuilding or defending?** Defending, advertising
  and product refresh, not replacement of the asset. That test passes. It does not save
  the verdict, because [E4-32] outranks it.

### [E4-32]: DIRECTION, *"the primary criterion of a great business"*

**NARROWING, on every physical series, for a decade, in every region.** Units -50%,
dealer points -25%, U.S. share -16.2 points, European share -5.7 points, revenue per unit
now falling too.

### The bull case, stated at full strength **[E4-51]** before it is answered

*A fair statement of what a holder would say, from the filings:* Q2 2026 was the first
positive retail quarter in years. **North America +2.8%, worldwide +0.5%, U.S. +3.3%**;
global dealer inventory is down 17% year-on-year and healthy; HDMC operating income rose
18% to $72M on 9% higher shipments; a new CEO from outside the industry announced a
strategy in Q2 2026, **"Back to the Bricks"**, targeting **$150M of cost reduction plus
$75M of profitability improvement ($225M total)**, a **mid-single-digit CAGR in worldwide
retail sales over three to five years**, HDMC gross margin of **25-30%**, and HDMC
operating expense below 20% of revenue; the company **raised** full-year guidance on
2026-07-23 (retail and shipments to 133,500-138,500 units, HDMC operating income from a
$40M loss to a $10-50M profit); the balance sheet is transformed, with **$986M of net
cash at the manufacturing entity**, consolidated debt down from $6.96bn to $2.97bn, and a
finance company de-risked into a fee-earning servicer with KKR and PIMCO as partners; the
brand is one of a handful of genuinely global American icons and licensing alone is a
perpetuity; and one-third of the market cap is cash.

**The answer, and it is the direction test.** Every element of that case is about the
*level*, a cyclical trough, a cost programme, a balance-sheet event. **Not one element
is evidence that the substitution has stopped.** One quarter of +3.3% U.S. retail against
eleven years at -6.7% a year is a datum, not a reversal; the company's own raised
guidance still puts 2026 units at **133,500-138,500 against 218,273 in 2019**; the
"market share gains" claimed in the Q2 press release are a quarter's move inside an
eight-year, 16-point loss; and the strategic plan's own growth target, mid-single-digit
retail CAGR, is precisely the kind of belief **[E4-35]** says must carry the burden of
proof in writing against the base rate, offered here by a CEO eleven months into the job
with no full year on the record, in a business whose last two guidance years missed by
half (Q3 below). **[E4-32] is not satisfied by a cheaper price or a better plan. It asks
whether the moat widened, and it did not.**

- Class: **[x] NARROW**, real over an installed base and a licensing stream; not wide.
  Direction: **NARROWING.**
- **VERDICT: [x] OUT.** Under **[E3-03]** a franchise is one whose customers think it has
  **no close substitute**; the marginal buyer's substitution is a filed, eight-year,
  16-point, two-continent fact. **[E2-44]** scores 0 of 2 today. **[E4-37]**'s agony
  metric has flipped inside the filings. **[E2-45]**'s attack was run in the real world
  and won. **[E4-55]**'s physical series is down 50% in eleven years and the dollars have
  now broken too. **[E4-32]**'s direction, *"the primary criterion of a great business"*,
  reads narrowing everywhere. What remains is a genuine, valuable, historically great
  **business in secular unit decline**, and the corpus has a word for that class:
  *"a business, unlike a franchise, **can be killed by poor management**"* **[E3-43]**.
  **The entry run stops here. [E5-13]: most names should end here, and that is the
  system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · **Q2 OUT**. The hard sequence closes
the file for any BUY decision. No position exists, so no [E2-28] hold read is required.
Everything below is **FOR THE RECORD**: the operator tasked this run with the two-business
separation, the Q3 conduct record, the deaths, the floor arithmetic and Q6 bands, and Q6
is written regardless. **Every valuation figure below carries operator rule 3's header.
Nothing below is entry language.**

---
## Q3: FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless
**Q3 can stop a run; it can never start one** [E2-37, E2-38, E3-39].*

### STEP 1: THE WEIGHT CASE, declared first

- **[x] Daily execution. HIGH.** A discretionary premium consumer durable sold through
  independent dealers, requiring annual model refreshes, pricing decisions, dealer
  network health, inventory discipline and tariff mitigation. Nearer [E3-38]'s retailer
  than its network TV station: *"For a retailer, hiring that nephew would be an express
  ticket to bankruptcy."* Q2 has already ruled this a business, not a franchise, and
  **[E3-43]** attaches the gate to exactly that class.
- **[x] Leverage. HIGH at the group, LOW at the manufacturer.** HDFS runs ~6.5x debt and
  deposits on equity with a covenant permitting 10.0x, and HOG's equity is the residual of
  the whole. **[E3-29]** governs: *"Because leverage of 20:1 magnifies the effects of
  managerial strengths and weaknesses, we have no interest in purchasing shares of a
  poorly-managed bank at a 'cheap' price."* The 2025 transaction cut this materially
  (consolidated debt $6.96bn -> $2.97bn) but did not remove it.
- [ ] Control, no; marketable minority, exit exists.

**Two determinants high → Q3 would be a BINARY GATE for entry, and no price compensates
[E3-29, E1-16, E5-35]:** *"You can turn any investment into a bad deal by paying too much.
What you can't do is turn any investment into a good deal by paying little."*

### The honesty binary **[E5-16]**, no disqualifier found

*"We are understanding about business mistakes; our tolerance for personal misconduct is
zero."* **The sweep, named**, so the absence claim is bounded: FY2025 10-K **Item 3 Legal
Proceedings** and **Note 15**; the **E&Y** opinion and ICFR attestation (unqualified;
auditor since 1982) and its **critical audit matter**; the 2026 and 2025 DEF 14A
related-party and governance sections; the full 8-K stream 2025-01 to 2026-08. **No
restatement, no SEC enforcement matter, no self-dealing finding appears in the documents
read.** Worded per the absence-claim rule: **no instance found in the documents read**,
not "none exists."

**One live matter, dated and characterised.** The **Japan Fair Trade Commission**
initiated an investigation of Harley-Davidson Japan KK on or about **2024-07-30** for
"alleged improper activity, **including setting excessive sales quotas for H-D Japan's
motorcycle dealers**." The company says it does not expect material costs and is not
aware of similar activity outside Japan. Under the **TJX 2022 calibration** this is a
channel-conduct matter, not financial dishonesty toward owners, and it is **not a Q3
failure**. It is, however, a prompt to read, and it reads onto one thing that matters
elsewhere in this file: **the retail-sales series is compiled from dealer-supplied
warranty and registration data that "the Company does not regularly verify"** (the
footnote appears under every retail table). A regulator alleging quota pressure on
dealers, in a market whose retail data the dealers supply, is worth carrying as a
data-quality note. **[E5-22]: penalty size is not seriousness in either direction; the
failure that counts is not acting when you learn.** No evidence of failure to act found.

### STEP 2: THE FLAGS **[E4-22, E4-29, E5-15, E4-30, E2-49, E2-52, E3-50, E2-57, E3-53]**

- [ ] **Weak accounting. NOT FIRED.** Share-based compensation is expensed in full
  ($31.7M in 2025). Pension assumptions are **conservative, not fanciful**: discount rate
  5.55%, **expected return on plan assets 6.40%**, compensation increase 4.00%; the plan
  is **overfunded** ($546.3M asset against $53.1M of liabilities). Nothing here resembles
  [E4-22]'s cockroach.
- [ ] **Unintelligible footnotes. NOT FIRED, and the reverse fires as a candor
  positive.** **Note 19's Supplemental Consolidating Data** publishes separate income
  statements, balance sheets *and cash-flow statements* for the manufacturing and finance
  entities. It is not required by GAAP segment rules. It is precisely what a half-owner
  would want to know **[E2-26]** and it is the reason this run could do its job. Credited.
- [x] **TRUMPETED PROJECTIONS. FIRED, and it is the file's largest Q3 finding.** HOG
  guides **every segment, every year, in numbers**, and layers multi-year targets on top:
  a "$400 million of incremental cost" productivity target set in 2022 for 2025 and then
  **extended to 2026**; **"HDFS operating income … approximately three times 2026 expected
  … in or around 2029"**; and "Back to the Bricks" targeting a **mid-single-digit retail
  CAGR over three to five years** and **HDMC gross margin of 25-30%**. This is the
  behaviour **[E5-30]** calls a ratchet: *"once you start it, it's all over … And
  forecasting earnings, I can't imagine anything more destructive."*

  **[E3-48] action taken, the record of the people who made the projections, pulled and
  set against outturn:**

  | guidance, as given | date given | **outturn** |
  |---|---|---|
  | HDMC operating **margin 12.6% - 13.6%** for 2024 | 2024-02-08 | **6.7%** ($277.8M on $4,121.9M) |
  | Worldwide retail units **flat to +9%** for 2024 | 2024-02-08 | **-7.1%** |
  | HDMC operating **margin 7.0% - 8.0%** for 2025 | 2025-02-05 | **-0.8%** (a **$28.7M operating LOSS**) |
  | HDMC revenue **flat to -5%** for 2025 | 2025-02-05 | **-13.2%** |
  | Worldwide retail units **flat** for 2025 | 2025-02-05 | **-12.4%** |
  | LiveWire operating loss $70-80M for 2025 | 2025-02-05 | $75.0M, **met** |

  **Two consecutive years in which the central margin guidance was missed by roughly
  half, and the unit guidance was missed by twelve points.** Buffett's stated base rate is
  that *"about nine cases out of ten"* projections exist to justify a decided course; the
  remedy is to demand the record. **The record is here, and it is poor.** One
  qualification, made in fairness: **both misses belong to the prior management** (Zeitz,
  who left 2025-10-01). The 2026 guidance is the new CEO's, and its only data point so
  far is a **raise** on 2026-07-23 after a beat. **One raise is not a record.**
- [ ] **Serial share issuance [E5-15]. NOT FIRED; the opposite.** Diluted shares 155.0M
  (2021) -> 145.1M (2023) -> 132.3M (2024) -> 121.3M (2025) -> **104.07M outstanding at
  2026-07-31**: a **33% reduction in five years**, funded from cash and asset proceeds,
  not from issuance. **[E2-52]** does not fire either, dividends are paid from cash while
  the share count falls.
- [x] **EBITDA / ADJUSTED-EARNINGS PROMOTION [E4-29]. FIRED.** The Q2 2026 press release
  headlines **"HDMC Adjusted EBITDA margin of 10.4%, up from 9.3%"** as a bullet, directly
  above a GAAP operating margin of 6.6%, and repeats Adjusted EBITDA in the HDMC results
  table. In a business carrying **$170M of annual D&A against $10-50M of guided segment
  operating income**, EBITDA deletes an expense several times larger than the profit.
  **[E5-41]:** *"Depreciation is where you spend the money first … and record the expense
  later. And it's **reverse float**."* The measure is reconciled and the GAAP figure is
  given beside it, which is the mild form, but it is promoted, and the flag fires.
- [~] **Filed-figure tells [E4-30], one fires, and the filing explains it.** Cash taxes
  as a share of pre-tax income: **27.4% (2023), 21.5% (2024), 8.6% (2025)**, a falling
  series, which is the tell. **Prompt followed into the text:** the 2025 gap is accounted
  for by an **$84.1M deferred-tax swing** arising from the HDFS Transaction and by the
  ASU 2023-09 change in how cash taxes are presented (2025 is stated net of refunds; prior
  years are not). The book effective rate went **up** in 2025, to 28.2% from 13.9%. **No
  fraud finding.** The second tell, unnaturally smooth reported growth, is absent:
  earnings are violently lumpy.
- [x] **METRIC-SWITCHING [E2-49]. FIRED, with an innocent reading available.** HDMC
  guidance was given as an **operating margin** in 2024 ("12.6% to 13.6%") and 2025
  ("7.0% to 8.0%"), and switched to an **absolute operating income range** for 2026 ("$40
  million loss to $10 million income") **after** the margin collapsed to negative.
  *"Yardsticks seldom are discarded while yielding favorable readings."* The innocent
  reading is real, a margin percentage is meaningless near zero, but **[E2-49]** asks
  for *"pre-set, long-lived and small bullseyes"*, and this bullseye moved after a bad
  year rather than ahead of one with reasons.
- [x] **RESTRUCTURING [E3-53, E5-33], recorded, not condemned.** Harley runs a named
  restructuring roughly every four years: **The Rewire (2020, $130.0M of restructuring
  expense)**, The Hardwire (2021-25), **Back to the Bricks (2026-27, $150M of cost
  reduction plus $75M of "other benefit")**. The charges are real costs and they are in
  the owner-earnings means below, per **[E5-33]**: *"to tell owners year after year,
  'Don't count this' … is misleading."*
- [~] **"EXCEPT FOR" [E2-57], soft fire.** The MD&A attributes the decline overwhelmingly
  to "a challenging macroeconomic environment, including high interest rates and depressed
  consumer sentiment." In 2025 that environment cost the U.S. 601+cc industry 6.1% and
  cost Harley 12.9%. **The filing does not anywhere state that it lost share, in those
  words, in the MD&A discussion of the decline**, the share number is disclosed
  accurately in the registration table two paragraphs later, so this is not concealment;
  it is emphasis. *"the real mistake is not the act, but the actor."*
- [ ] **Stock-price targeting [E3-50], not fired.** No language found premising management
  on the highest possible stock price.

### STEP 3: THE PRIMARY TEST **[E2-01]**, balance sheet first **[E5-27]**

**[E2-43] applies and is used:** for a filer with a captive finance arm, book equity is
the wrong denominator and the corpus says so. The run reports **both**.

Consolidated ROE (net income attributable ÷ average total HOG equity):
**30.4% (2021) · 27.2% (2022) · 23.0% (2023) · 14.2% (2024) · 10.7% (2025)**

Manufacturing return on manufacturing equity (Note 19 non-FS, net income less the
intercompany dividend ÷ average non-FS equity):
**27.1% (2021) · 27.7% (2022) · 24.1% (2023) · 11.4% (2024) · -0.9% (2025)**

HDFS return on HDFS equity: **31.5% (2021) · 23.2% (2022) · 17.2% (2023) · 17.6% (2024) ·
47.8% (2025, on the allowance release)**; post-transaction the company's own 2026 guidance
implies **11-13%**.

**Balance sheet across eight years [E5-27]:** total HOG equity $1,722.8M (2020) ->
$2,553.2M (2021) -> $2,903.5M (2022) -> $3,252.8M (2023) -> $3,166.0M (2024) -> $3,140.7M
(2025) -> $3,099.2M (6/30/26). Goodwill is immaterial and static ($63.9M). Treasury stock
grew from $935.1M (2022) to $2,275.4M (6/30/26), real cash returned. **No accounting
gimmickry found; no goodwill wedge to strip.** The primary test therefore reads cleanly,
and what it says is that **the manufacturing business's return on capital collapsed from
27% to zero in four years.** That is a Q2 finding restated as a number, which is where
**[E3-46]** puts it, *asked about the business, before the manager.*

### The half-owner test **[E2-26]**, passes, notably

Does the reporting tell me what I would want to know if the positions were reversed? On
the whole **yes, and better than most**: retail units by region every quarter; dealer
counts by region every year; **industry registrations and its own market share, published
even as the share falls**; the separate consolidating statements; segment operating income
with the expense build-out; a **tariff table by country with 2025 actual and 2026
estimate**; managed-basis credit losses and delinquencies; and the LiveWire concession
that *"indicators point to a much later EV adoption than the Company originally
anticipated."* **A company hiding a melt does not publish its own market-share series.**
This is the file's strongest Q3 positive and it is why the melt could be measured at all.

### The institutional imperative, scored **[E2-30]**

*"Institutional dynamics, not venality or stupidity."*

1. **[x] Resists any change in current direction. FIRED historically, now reversing.**
   Five years of "The Rewire" and "The Hardwire" under the same CEO produced a 39% unit
   decline; the board searched for a successor from Q4 2024, evaluated three candidates in
   March 2025 and **offered the job to none of them**; the change came only after a
   near-50% withhold vote (below).
2. **[x] Projects/acquisitions materialise to soak up available funds. FIRED, and it has
   a name: LiveWire.** Cumulative operating losses of roughly **$525-535M (2021-2026e)
   against $173M of cumulative revenue**, with 2025 revenue ($25.7M) *below* 2021's
   ($35.8M). Taken public via SPAC in 2022 at the peak of the EV-SPAC wave, which is
   **[E2-30] behaviour (4), peer behaviour mindlessly imitated**, as cleanly as the corpus
   describes it. **Credit where due, and it is the single best capital-allocation act in
   the file:** the FY2025 10-K states flatly that **"The Company does not plan to make
   additional investments in LiveWire beyond the amount outstanding under the Term Loan"**
   (a $75M secured loan at SOFR+4.00% due 2027) and concedes the adoption thesis was
   wrong. **That is the rare-positive tell [E4-39]: a management revisiting its own case
   against the announcement.** It arrived after half a billion dollars.
3. **[ ] Staff studies to justify the leader's craving**, not observable from filings.
4. **[x] Peer behaviour mindlessly imitated. FIRED.** The LiveWire SPAC (2022 EV wave);
   and arguably the KKR/PIMCO forward-flow structure (the 2024-26 captive-finance
   partial-sale wave), though that one is defensible on its economics.

### Capital allocation, the buyback conditions **[E5-08, E4-31, E5-24, E2-51]**

- **Condition (1), ample funds for operations and liquidity: MET, comfortably.** $986M of
  net cash at the manufacturing entity, $1.9bn consolidated, $4.3bn of total liquidity
  including facilities at 2025-12-31.
- **Condition (2), a material discount to conservatively calculated intrinsic value:
  UNPROVEN AT THE PRICES PAID, and this is the capital-allocation flag.** **[E5-24]:**
  *"what is smart at one price is dumb at another."* The record:

  | period | discretionary repurchases | approximate average price | HDMC operating income that year |
  |---|---:|---:|---:|
  | 2023 | $364.0M | ~$32 | $661.2M |
  | 2024 | $459.8M | ~$35 | $277.8M |
  | 2025 | $353.3M | ~$25 (ASR at ~$25 in Nov) | **-$28.7M** |
  | H1 2026 | $158M / 7.9M shares | **~$20** | (guided $10-50M) |

  **$1.18bn was spent in three years, roughly $824M of it above $30, into a business whose
  segment operating income fell from $661M to negative over the same window.** The shares
  are now $27.52. The buybacks were not wrong in *kind*, retiring a third of the equity
  of a cash-rich company is defensible, but they were made at prices that the company's
  own subsequent guidance did not support, and **[E4-31]**'s third condition (an
  adequately informed register) sits awkwardly beside guidance that missed by half in the
  same years. **Stated with [E4-13]'s humility clause: this rests on our own value range,
  and management knows the business better than we do.** Note the honest offset, per
  [E4-26]: management **paused** discretionary repurchases at 2025 year-end pending the
  new strategy, which is the discipline [E5-31] asks for, and then resumed at ~$20.
  **The flag binds position size, never the discount rate, and position size is moot,
  because Q2 is OUT.**

### The CEO transition and the activist campaign, the facts, dated

| date | event | source |
|---|---|---|
| 2022-2025 | **H Partners** holds a large stake; **Jared Dourdeville** sits on the board (3+ years) | DEF 14A 2026-04-09 |
| Q4 2024 | Board initiates a CEO search after Zeitz expresses interest in retiring in 2025 | DEF 14A 2026-04-09 |
| 2025-03-26/28 | Board meets three CEO candidates and **decides to offer the role to none** | 8-K 2025-04-10, acc. 0000793952-25-000085 |
| 2025-04-01 | Dourdeville demands the immediate resignation of three directors | same 8-K |
| **2025-04-05** | **Dourdeville resigns from the board**, citing succession planning, board and governance, working culture and commercial execution | same 8-K (resignation letter furnished as Ex. 17.1) |
| 2025-04 to 05 | H Partners runs a **withhold campaign** (DFAN14A stream, filer 0000921895); company responds with ~25 DEFA14As | EDGAR |
| **2025-05-14** | **Annual meeting.** All directors re-elected, but: **Zeitz 50,808,847 for / 48,747,552 withheld (49.0% withheld)**; Linebarger 40,493,878 withheld (40.7%); Levinson 42,076,657 withheld (42.3%). Say-on-pay 68.5M for / 19.8M against / **11.3M abstentions** | 8-K 2025-05-19, acc. 0001104659-25-050474 |
| 2025-09-15 | **Levinson and Linebarger retire** from the board; Nova and Reintjes appointed | DEF 14A 2026-04-09 |
| **2025-10-01** | **Artie Starrs becomes President and CEO** (previously CEO of Topgolf). **Zeitz steps down as Chairman, President and CEO**, to a senior advisory role into early 2026. **Troy Alstead becomes independent non-executive Chairman**, the combined Chairman/CEO structure is ended | DEF 14A 2026-04-09 |
| Q4 2025 | HDFS Transaction with **KKR and PIMCO**; new COO, CCO/CFO and CMTO appointed | FY2025 10-K |
| Q2 2026 | **"Back to the Bricks"** strategic plan announced | Q2 2026 10-Q |
| 2026-06-29 | Chief Legal Officer replaced | 8-K 2026-06-26, acc. 0000793952-26-000050 |
| 2026 proxy | **H Partners no longer appears among >5% holders** (Vanguard 12.55%, BlackRock 10.24%, Donald Smith 8.16%, Dimensional 6.27%, Beutel Goodman 5.09%). Farley (Ford) not standing for re-election; board shrinks 9 -> 8 | DEF 14A 2026-04-09 |

**Read: the activist won and left.** Every substantive thing H Partners demanded, the CEO
out, the chairman/CEO split, the two long-tenured directors gone, board refreshment,
happened within six months of the vote, and the campaigner is no longer a 5% holder. That
is a governance improvement, and it is recorded as one. It is also **[E4-49]** in
miniature and pointing the other way: the corpus rates persuading managements as *"worse
than poor"* and prescribes exiting instead; here engagement worked, at the cost of a
board seat and a year.

**The manager the run would actually be buying: Artie Starrs, eleven months in.**
Compensation 2025 (three months): $304,000 salary, a **$2,000,000 signing bonus**,
$6,125,019 of stock awards, total **$8,591,990**. Owns **15,000 shares** outright against
400,016 restricted stock units (DEF 14A, as of 2026-03-12). **All directors and executive
officers as a group own 1,060,225 shares, under 1% of the company.** *"Who ever washes a
rental car?"* is the corpus's phrase; the answer here is that the alignment is
grant-based, not purchase-based, which is ordinary for a US large-cap and is recorded, not
condemned. **[E5-38]** governs: a fired flag is not a venality finding. **What cannot be
done is the thing the standard forbids, ranking a manager in advance of a record.**
*"we cheat. We buy businesses with good managers."* **Track record, or no verdict.**

### THE GUARDRAIL, checked before the verdict

- [x] Confirmed: **nothing in this Q3 is used to promote the name.** Q2 is OUT and stays
  OUT; a strong manager cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
  *"a textile company that allocates capital brilliantly within its industry is a
  remarkable textile company, but not a remarkable business."*
- [x] Key-person dependence was tested at **Q2** per **[E4-23]** and **does not fire**,
  the brand outlives its CEOs. Recorded there, not here as a compliment.
- [x] **Is the franchise intact and the damage excisable, or is the manager the plan?**
  **[E2-35, E2-36]** This is the question the whole file turns on. GEICO's franchise was
  *"still intact within the company, although submerged in a sea of financial and
  operating troubles."* **Harley's is not submerged; it is smaller.** Sixteen points of
  U.S. share did not go into a sea, they went to competitors and to the used market. The
  new CEO's plan, cost cuts, a cheaper model, the Sportster's return, a mid-single-digit
  retail CAGR, **is a corporate Pygmalion, not a surgeon's excision.** That is the
  unbuyable configuration the corpus names.

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found in the documents read; the gate
  would NOT clear today, and the reason is a record that does not yet exist.** The
  disclosure is unusually candid (Note 19, the published share series, the LiveWire
  concession, the tariff table); the governance has genuinely improved; the balance sheet
  has been de-risked. Against that: a **fired projections flag with a two-year record of
  missing by half**, a **fired EBITDA-promotion flag**, a **fired metric-switch**, a
  **capital-allocation flag on $824M of buybacks above $30**, half a billion dollars into
  LiveWire, and a chief executive with **eleven months and one raised guidance** in a
  business the weight rule makes a binary gate. **UNRESEARCHED, and the documents are
  named and dated:** the FY2026 10-K (EDGAR, ~late February 2027, the first full year
  under Starrs, and the first test of "Back to the Bricks" against its own targets); the
  Q3 2026 10-Q (EDGAR, ~early November 2026, the seasonally loss-making half, against
  guidance that implies HDMC at -$81M to -$41M in H2); the 2027 DEF 14A (EDGAR, ~April
  2027. Starrs's first full compensation cycle and any open-market purchases).
  *A pass here would be the absence of found disqualifiers, never a clearance
  **[E5-17]**, and IN never promotes; Q2 OUT stands regardless.*

## Q4: FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings: **COMPUTATION, NOT A CLEARANCE** **[E2-23]**

Convention applied to the **manufacturing business only**, per the method declared above:
multi-year mean of (operating cash flow - SBC) - (c), with OCF from Note 19's
Non-Financial Services column and the intercompany HDFS dividend removed. **The finance
business is valued separately and is never blended into this yield.**

| $M | mfg OCF (ex-dividend) | SBC | D&A | capex | **OE (c=D&A)** | **OE (c=capex)** |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | 403.1 | 38.9 | 156.0 | 116.0 | **208.2** | **248.2** |
| 2022 | 226.1 | 51.0 | 143.3 | 147.3 | **31.9** | **27.9** |
| 2023 | 569.5 | 79.3 | 149.2 | 202.3 | **341.0** | **287.8** |
| 2024 | 531.0 | 47.0 | 151.3 | 194.7 | **332.7** | **289.3** |
| 2025 | 283.7 | 29.6 | 163.0 | 152.7 | **91.1** | **101.5** |

**MORE THAN ONE WINDOW; THE SPREAD IS PART OF THE RANGE [E4-25].**
- **Long window (5-yr, 2021-25, the corpus default [E2-42]): $191M - $201M**
- **Short window (3-yr, 2023-25): $226M - $255M**
- **Two-year (2024-25): $195M - $212M**
- **Spread, conservative end: the 3-yr mean sits 18% ABOVE the 5-yr mean**, an inversion,
  because the distorted year is 2022 (a $271M working-capital *build* as inventories were
  rebuilt post-COVID), not a pandemic trough. **Naming the distortion is a Q4 finding
  [E5-11]:** every window ending in 2025 contains 2022-2023, when HDMC operating income
  was **$677M and $661M**, the peak of the powersports demand and pricing boom. **[E4-41]
  governs: normalize DOWN for luck.** The mean is not the number.

**Stock compensation subtracted in full [E5-06]** ($29.6M-$79.3M/yr). The [E3-70]
market-value uplift is not separately estimated; at this scale relative to the numbers
below it does not change any verdict.

**Maintenance capex, a DISCLOSED JUDGMENT with the corpus default applied [E3-44,
E2-41, E5-20].** D&A is taken as the operative (c). The [E5-20] exception is **NOT**
invoked: this is not a railroad, no filing statement says depreciation understates
renewal, and the historic capex-to-D&A relationship straddles 1.0x (2021 0.74x, 2022
1.03x, 2023 1.36x, 2024 1.29x, 2025 0.94x). **The band is displayed and it changes
nothing**. D&A and capex give answers within 10% of each other in four of five years.
The 2026 guidance ($175-200M of capital investments against ~$170M of D&A) sits at the
capex end and is used in the bottom-boundary build below.

**No look-through increment [E3-04]:** no material equity-method investees; the only
minority interests run the other way (KKR/PIMCO in HDFS, public holders of LiveWire).

### THE FINDING THAT GOVERNS THIS GATE, 2025's owner earnings are a liquidation

The $161.0M working-capital movement inside 2025's manufacturing OCF is a **release**:
inventories -$47.6M, receivables -$30.6M, other current assets -$60.8M. **Strip it and
2025 manufacturing owner earnings were -$69.9M.** The release continued and accelerated:
non-FS inventories fell a further **$221.8M in H1 2026** (balance-sheet inventories
$730.9M -> $500.9M, **-31% in six months**).

**[E2-23] constraint 3** requires the working-capital *increment* to be included in (c)
where the business requires it to maintain unit volume. **A shrinking business generates
the mirror image, a release, and the release is not earnings.** It cannot repeat: the
inventory is nearly a third gone. **This is the [E4-41] normalization the gate requires,
and it turns 2025 from $91M of owner earnings into negative $70M.**

H1 2026, same method: mfg OCF $62.6M (after removing the $100M intercompany dividend)
less SBC $17.2M less D&A $85.3M = **-$39.9M**, *including* the $221.8M inventory release
and *excluding* the seasonally loss-making second half.

### THE BOTTOM BOUNDARY **[E5-34]**, built from the company's own RAISED guidance

*"we will buy the stock … if it sells at a reasonable price in relation to **the bottom
boundary of our estimate**."*

| item | $M |
|---|---:|
| HDMC operating income, **raised** guidance, 2026-07-23 | +10 to +50 |
| LiveWire operating loss, guidance | (70) to (80) |
| **manufacturing operating result** | **(70) to (20)** |
| investment income on ~$1.2bn of cash at ~4% | +45 |
| interest on the 2045 notes | (14) |
| add back D&A | +170 |
| less capital investments (company guidance) | (187) |
| less stock compensation (run-rate) | (35) |
| less cash tax | (10) |
| **MANUFACTURING OWNER EARNINGS, before working capital** | **(101) to (51)** |

**The bottom boundary of manufacturing owner earnings in 2026 is NEGATIVE**, on
management's own *improved* numbers. The seasonality check confirms the shape: H1 2025
HDMC was +$177.6M against a full-year **-$28.7M**, i.e. **H2 2025 HDMC was -$206.3M**; H1
2026 HDMC was +$91.3M and the raised full-year guidance of $10-50M implies **H2 2026 HDMC
of -$81M to -$41M.**

### Great, good, or gruesome? **[E4-20]**

- [ ] great, [x] **at the HDMC segment through 2023**, and the record should say so:
  24-28% returns on manufacturing capital, capex under $200M, a brand needing defence not
  replacement.
- [x] **GOOD, deteriorating to GRUESOME at the consolidated level, and the split is the
  point.** Take the three savings accounts one at a time:
  - **HDMC alone** was the *great* account and is now paying nothing: return on
    manufacturing capital 27% -> **-0.9%**.
  - **LiveWire** is the **gruesome** account exactly as defined: *"grows rapidly, requires
    significant capital to engender the growth, and then earns little or no money"*, except
    it did not even grow. **$525-535M consumed for revenue that fell.** *"attracted by
    growth when they should have been repelled by it."*
  - **HDFS post-transaction** is the **good** account **[E4-43]**: ~11-13% on equity, and
    *"nothing shabby"* about that, it passes, it just ranks below great.
  **The blend is why the consolidated number misleads in both directions.**

### Staying power, score all three **[E5-11]**

1. **A large and reliable stream of earnings. LARGE, NOT RELIABLE. FAILS on reliability.**
   Consolidated operating income: $9.7M (2020), $823.4M (2021), $909.3M (2022), $779.1M
   (2023), $386.6M (2024), **guided $0-40M (2026)**. That is a hundred-fold range in six
   years. **[E3-55] is the right scope test and it does not rescue this**: volatility with
   a *certain* endgame is not a defect, but here the mechanism itself is uncertain, the
   bounce is not See's losing money eight months a year, it is a unit base halving.
2. **Massive liquid assets. PASSES, and this is the leg that carries the file.**
   $1,895.8M consolidated cash at 2026-06-30, of which **$1,283.3M sits at the
   manufacturing entity** against $297.3M of manufacturing debt. **Net cash $986.0M, 34%
   of the market capitalisation.** Add an overfunded pension (net asset ~$493M, largely
   trapped and **valued at nothing in this run**).
3. **No significant near-term cash requirements. PASSES at the manufacturer, QUALIFIED at
   the group.** *← the one that usually kills.* The manufacturer has **no maturity before
   2045**, no pension deficit, no covenant. The group does: HDFS faces $500M due 2027 and
   ~$861M in 2029-2030, and it funds a re-growing receivable book with commercial paper
   ($613.1M outstanding) and brokered deposits ($516.5M), **the kindness of strangers
   [E5-39] in exactly the form the corpus warns about**, mitigated by the forward-flow
   agreement, which the company itself says "will reduce its funding risk in the
   near-term." **[E2-55]: score the worst case, not the expected one**, in a funding
   freeze HDFS shrinks its book and starves the dealers of floorplan, which starves
   shipments. That transmission is the group's real near-term cash risk and it is not on
   the manufacturer's balance sheet.

**Leverage, named and quantified [E4-16, E3-29], there is no ratio ceiling in this
framework and the corpus supplies none.** Manufacturer: $297.3M of covenant-free 4.625%
notes due 2045 against $1,283.3M of cash, **negative leverage**. Finance company: ~6.5x
debt-and-deposits to equity against a 10.0x covenant, at BBB-/Baa3 with S&P on
CreditWatch Negative. **Consolidated debt fell from $6,960M to $2,967M in 2025.** The
single largest thing the current management did was take the leverage out.

### Name the specific ways THIS business dies **[E2-27, E3-24, E4-40]**
*Model **exposure**, not experience **[E4-40]**. The bear case stated as its best advocate
would state it, per the iron prescription **[E4-51]**.*

**1. THE DEMOGRAPHIC MELT, the slow death, and it is the named one.**
*Mechanism:* Harley sells a discretionary durable to a cohort that is aging out and is not
being replaced at the same rate, in a category whose own registrations are flat to
falling, while producing its own substitute supply (used bikes) with every unit ever sold.
*Quantified from filed figures:* worldwide retail units **264,627 (2015) -> 132,535
(2025)**, -6.7%/yr for eleven years; U.S. 601+cc share **50.7% (2017) -> 34.5% (2025)**;
dealer points **1,569 (2019) -> 1,174 (2025)**. HDMC's fixed-cost base cannot follow: the
FY2025 MD&A names "unfavorable manufacturing leverage related to higher fixed costs per
unit on lower production and shipment volumes" as a primary cause of the segment's first
operating loss. At another -6%/yr, units reach ~99,000 by 2030 and the plant footprint
deleverages faster than $225M of announced cost saving can offset, **the shrink-to-margin
lever, which held the dollar line up from 2019 to 2023, has already been spent, and 2025
is what its exhaustion looks like.**
*Exposure, not experience [E4-40], and the row supplies the exposure evidence:* the
category itself is shrinking on four independently constructed measures (Polaris's NA
900cc+ estimate 190,000 -> ~156,000 units 2020-2025; BRP's global three-wheel market
-29% in two years; BRP's global electric motorcycle market ~6,000 units and -18%;
Harley's own MIC-sourced US 601+cc -7.4% in two years). **And the terminal value of a
heavyweight motorcycle franchise was market-tested ten months ago: Polaris accepted a
nominal price, absorbed $342.5M of charges and paid $79.3M of net cash to hand the North
American number two to private equity.** That is what this death looks like when it
finishes, priced by a competitor rather than modelled by an analyst.
*Likelihood:* **[x] LIKELY.** It is the filed eleven-year trend, not a scenario. *This is
the named death.*

**2. TARIFFS AND THE TRADE REGIME, the fast wound, and it is larger than the profit.**
*Mechanism/exposure:* Harley manufactures in the US and Thailand and sells 33% of HDMC
revenue outside the US, so it is exposed both ways, input tariffs on steel, aluminium and
components, and retaliatory tariffs on exported motorcycles.
*Quantified from the company's own table:* **$67M of cost in 2025, estimated $75-105M in
2026** (steel and aluminium alone $31M in 2025). Against guided HDMC operating income of
**$10-50M**, the tariff bill is **1.5x to 10x the entire segment profit.** The precedent is
filed: the 2018 EU rebalancing tariffs took Harley's landed EU duty to **31%** from April
2021. The Supreme Court struck the IEEPA tariffs on 2026-02-20, which cuts the other way
and produced a "tariff recovery" in Q2 2026 gross profit, **which is exactly [E2-59]'s
point: the moat belongs to the regime, and "That day is gone" is how it ends, in either
direction.**
*Likelihood:* **[x] a real possibility** that the 2026 estimate is exceeded; the base case
is already in the guidance.

**3. THE HDFS CREDIT CYCLE, reduced, not removed, and the reduction is new.**
*Mechanism/exposure:* HOG retains one-third of new retail originations plus all dealer
floorplan; receivables have already rebuilt from **$1,965M (2025-12-31) to $2,645M
(2026-06-30)** and the company intends to keep growing them ("approximately three times
2026 expected HDFS operating income in or around 2029").
*Quantified [E3-24]-style:* on the $2,645M book at 2026-06-30, a recession doubling
managed retail losses from 3.0% to 6.0% for two years costs roughly **$160M pre-tax**
against HDFS equity of $377M, survivable, and nothing like the pre-2025 exposure, where
the same shock on a $7,288M book would have cost ~$440M. **The transaction genuinely cut
this death in half.** The residual is transmission: **wholesale credit losses rose $4.8M
in 2025 "driven by the charge-off of finance receivables at several troubled dealers"**,
and a dealer network shrinking 25% is a floorplan book with rising idiosyncratic risk.
*Likelihood:* **[x] a low-level possibility** of a solvency-relevant credit event; a real
possibility of a further earnings drag. **[E4-40] warning honoured:** managed losses of
3.0-3.4% are a benign *experience* late in a long cycle, and the corpus calls that
*"not only useless, but actually dangerous"* as a guide.

**4. LIVEWIRE, quantified, and now capped by management's own words.**
*Exposure:* $525-535M consumed 2021-2026e; 2026 guided loss $70-80M, which is **larger
than guided HDMC operating income**. *The cap:* "The Company does not plan to make
additional investments in LiveWire beyond the amount outstanding under the Term Loan"
($75M, secured, due 2027-12-15). *Likelihood:* the 2026 loss is **certain (guided)**;
further parent funding beyond the term loan is **a low-level possibility** given the
written statement; a **write-off of the $118M of LiveWire assets is a real possibility**
and would be immaterial to solvency.

**5. THE TRANSITION ITSELF.** A new CEO from outside powersports, a new COO, CFO/CCO, CMO
and General Counsel, a refreshed board, and a strategy announced eleven months in, all
executing simultaneously in a **daily-execution business** (the Q3 weight case). *Not
quantifiable from filed figures.* *Likelihood of execution stumbles inside the window:*
**a real possibility**; of a solvency consequence: **negligible**, because of leg 2.

- **Q4 FOR-THE-RECORD READ: SURVIVAL IS NOT IN DOUBT.** $986M of manufacturing net cash,
  one covenant-free bond due 2045, an overfunded pension, and a finance book cut by
  two-thirds mean **the company will be here in ten years**. What is in doubt is the
  earning power: **the manufacturing business's owner earnings on the bottom boundary are
  negative, and its return on capital has gone from 27% to zero in four years.** Were this
  gate live it would read **IN on survival**, with the melt (death 1) carried as the
  central valuation fact, which is Q2's finding restated. **The business survives; the
  franchise is going.**

---
## Q5: FOR THE RECORD, **COMPUTATION, NOT A CLEARANCE**
*(Q1-Q4 did not close IN; operator rule 3's header governs everything below; no entry
language appears anywhere in this section.)*

### THE FLOOR, BEFORE THE RANKING **[E4-28]**, *"that's the figure we quit on"*

**What the price actually pays for.** At $27.52 and 104,072,507 shares:

| | $M |
|---|---:|
| Market capitalisation | **2,864** |
| less manufacturing net cash (Note 19, 2026-06-30) | (986) |
| less HOG's 90.2% of HDFS, at book $377.0M / at the KKR-PIMCO price $475.5M | (340) to (429) |
| **= implied value of the motorcycle company (HDMC + LiveWire + the brand)** | **1,449 - 1,538** |

**Roughly $1.5 billion, or about $14 a share, for Harley-Davidson Motor Company.**

### 1. THE YIELD, manufacturing owner earnings ÷ implied manufacturing value

| owner-earnings basis | yield | vs sovereign 5.19% |
|---|---:|---:|
| **2026 bottom boundary, on raised guidance: -$51M to -$101M [E5-34]** | **negative** | **-10 pts** |
| 2025 ex working-capital release: -$70M | negative | -10 pts |
| 2025 as filed (WC-flattered): $91-101M | 6.2% - 6.6% | +1.1 to +1.4 pts |
| 2-yr mean (2024-25): $195-212M | 13.2% - 14.0% | +8.0 to +8.8 pts |
| **5-yr mean (2021-25), the corpus default window: $191-201M** | **12.7% - 13.5%** | **+7.6 to +8.3 pts** |
| 3-yr mean (2023-25): $226-255M | 15.6% - 16.6% | +10.4 to +11.4 pts |

**The spread between the top and bottom rows is the entire finding [E4-25].** It is not a
width to be resolved by preference; it is the unresolved question of whether 2021-2023 or
2025-2026 is the normal year, and **[E4-41] instructs the run which way to lean**: the
boom-inclusive means are flattered by a demand regime that has ended, and the honest
weight sits at the bottom boundary, which is negative.

**For contrast, and to show what the screen saw:** consolidated owner earnings on the
whole company (FY2025 OCF $568.9M less SBC $31.7M less D&A $172.4M = $364.8M) over the
$2,864M cap gives **12.7%**, a number that looks identical to the 5-year manufacturing
mean and is arrived at by a completely different and invalid route: it blends a finance
company's debt-funded cash flow with a manufacturer's inventory liquidation. **The same
computation on H1 2026 gives a negative number.** That is why the two-business treatment
was declared before any arithmetic.

### 2. WHAT THE PRICE ALREADY ASSUMES

At $1.5bn for the motorcycle company, and taking the sovereign as the no-growth
capitalisation rate, the price assumes **sustainable manufacturing owner earnings of about
$75-80M**. That is below the 5-year mean ($191-201M) and far below 2023-2024
($333-341M), **so the market is not extrapolating the boom.** It is above 2025 stripped of
the working-capital release (-$70M) and above the 2026 bottom boundary (-$51M to -$101M),
**so the market IS assuming the trough is a trough and that "Back to the Bricks" restores
something.** *What the business has actually done:* units -6.7%/yr for eleven years, U.S.
share -2.0 points a year for eight, HDMC operating income from $661M to -$29M in two.
**The price is a bet on the level, made against the direction.**

### 3. WHAT YOU ARE PAID

**Nothing, on the bottom boundary**, a negative yield, roughly 10 points *below* the
sovereign. **+7.6 to +8.3 points over the sovereign** on the corpus's default five-year
window, which is the number a bull would quote and which **[E4-41]** forbids this run
from trusting. **The answer depends entirely on which owner-earnings figure is real, and
that IS the finding [E4-25].**

### THE FLOOR VERDICT, stated plainly **[E4-28]**

The floor is 10% pre-tax expectancy, *"whether short rates are 6 percent or whether short
rates are 1 percent."* Clearing it at $27.52 requires manufacturing owner earnings of
**$145-154M**. The company's own raised guidance for 2026 implies **negative**. **The
floor clears only on a mean that contains 2022 and 2023, the two best HDMC years ever
recorded, in a demand regime the filings say has ended.** That is the same failure mode
that closed ETD nine days ago, and it is refused for the same reason.

**Note what bounds the upside too [E2-63, E4-44]:** *"the value of an asset … cannot over
the long term grow faster than its earnings do."* The bull path requires HDMC operating
income to travel from -$28.7M to something like $400M, which needs the $225M cost
programme delivered **in full** and unit growth at mid-single digits for five years,
against an eleven-year record of -6.7%/yr. **[E4-35]** puts the burden of proof on that
belief, in writing, and the writing is not here.

**And the downside has a market-tested marker, which is rarer and worth more than a
model.** The implied ~$1.5bn for Harley Motor Company is not a floor supported by asset
value: on 2026-02-02 Polaris transferred Indian Motorcycle, the disclosed North American
number two in 900cc+, ~$478M of revenue, for **a nominal price, plus $79.3M of Polaris
cash going out with it**, after writing the segment's goodwill to zero. Harley is a far
bigger and far better brand than Indian and the two are not equivalent. But the
transaction says something no discounted cash flow can: **in 2026 the private market
price of a heavyweight motorcycle franchise, set by the informed seller who owned it, was
approximately zero.** That is the [E3-24] discipline applied to the downside, a
mechanism, quantified from filed figures, with a stated likelihood.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**

*Motorcycle company at the stated owner-earnings level, plus $986M manufacturing net cash,
plus HDFS at $340-429M:*

| case | manufacturing OE | valued at | total value | per share |
|---|---:|---|---:|---:|
| **bottom boundary (2026 guidance)** | ~$0 | n/a | **~$1,330-1,420M** | **~$13 - $14** |
| trough-normal | $75M | the 10% floor | ~$2,080-2,170M | ~$20 - $21 |
| 2025-as-filed normal | $100M | the 10% floor | ~$2,330-2,420M | ~$22 - $23 |
| 5-yr mean, boom-inclusive | $196M | the 10% floor | ~$3,330-3,420M | ~$32 - $33 |
| 5-yr mean at the bare sovereign | $196M | 5.19% | ~$5,100-5,190M | ~$49 - $50 |

- **conservative ~$13-14 · optimistic ~$49-50 · current price $27.52**

**The range is too wide to reach a useful conclusion, and that IS the conclusion
[E4-25].** *"Usually, the range must be so wide that no useful conclusion can be reached."*
The width is not sloppiness; it is the honest measure of an unresolved
cyclical-versus-secular question on a business whose segment profit moved $690M in two
years.

**WHICH BAR:** **[x] Screamer test [E4-01]** only. The price sits **inside** the range,
the middle box, *"no useful conclusion, move on."* **No margin is stacked on top; none is
subtracted.** For the record, a screamer here would need the whole motorcycle company for
free, i.e. a price at or below net cash plus HDFS, about **$13 a share**, which is what
"startlingly low" would look like on this balance sheet and is nowhere near $27.52.

**WINDAGE COUNT: ONE.** The single place conservatism is spent is the choice to weight the
**bottom boundary over the boom-inclusive mean**, and it is justified in writing by
(i) the 2025 working-capital-release arithmetic, (ii) the company's own 2026 guidance, and
(iii) **[E4-41]**'s explicit instruction. The removal of the $135.3M of HDFS one-time
items, the removal of the intercompany dividend, and the use of [E5-34]'s bottom boundary
are **required corpus moves, not additional windage**. **No risk premium is placed in the
discount rate [E3-42]**, the sovereign is used bare, and certainty is priced at Q1's
understanding gate and, had this reached a decision, once at the end.

---
## Q6: WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists. These are pre-committed yardsticks for the WATCH LIST, set prior to
any act **[E1-02]**: "I believe in establishing yardsticks prior to the act." **Alert
thresholds are LISTED HERE ONLY, `tools/alerts.json` was not edited.**)*

### Q2 REOPEN CONDITIONS, the only route back to an entry run: **BOTH required.**

**1. EVIDENCE, not price, the direction test [E4-32] must actually turn:**
- **Two consecutive full years of rising worldwide retail units** (FY2027 and FY2028
  10-Ks). One quarter, one year, or a guidance range does not count. The 2026 guidance
  (133,500-138,500) would satisfy year one at the top of the range; year two must follow.
- **U.S. 601+cc market share stable or rising for two consecutive years** (the FY2027 and
  FY2028 10-K registration tables). This is the load-bearing series: the melt is a share
  story as much as an industry story, and share is the half Harley controls.
- **Dealership points stable or rising** (FY2027 10-K). 1,174 today.
- **HDMC operating margin back above 7% with the tariff bill absorbed**, the level the
  2025 guidance promised and missed, achieved rather than promised.
- **And "Back to the Bricks" delivered against its own numbers**, not restated: $150M of
  cost reduction realised by end-2027, plus the $75M profitability benefit, plus the
  mid-single-digit retail CAGR showing up in units.

**2. PRICE [E4-28], the bottom boundary must pay the floor with zero growth credited:**
manufacturing OE of $75-100M (the trough-normal band, itself generous against a guided
negative) capitalised at 10%, plus $986M of manufacturing net cash, plus HDFS at
$340-429M = **$2,080M - $2,420M, i.e. roughly $20 to $23 a share.**
**At $27.52 the quote sits 20% to 38% above that band.**

### Thesis-confirming and thesis-breaking metrics, with thresholds

| metric | source and cadence | confirms | **breaks** |
|---|---|---|---|
| **Worldwide retail units** | quarterly 10-Q / press release | two consecutive years up | any full year below **125,000** |
| **U.S. 601+cc market share** | annual 10-K registration table | stable or rising two years | below **32%** |
| **Dealership points** | annual 10-K | stable or rising | below **1,100** |
| **HDMC operating margin** | quarterly segment note | above 7% full-year | a second consecutive full-year operating loss |
| **HDFS 30-day managed delinquency** | quarterly 10-Q | below 5.5% at year-end | above **6.5%** at any year-end (5.77% at 2025-12-31) |
| **HDFS managed annualised retail credit losses** | quarterly 10-Q | below 3.0% | above **4.0%** |
| **Manufacturing net cash (Note 19)** | quarterly consolidating data | above $750M | below **$500M** |
| **Non-FS inventories** | quarterly balance sheet | stable | a further release below **$400M** (the liquidation running out) |
| **Guidance vs outturn** | annual | 2026 met or beaten | a third consecutive year of missing HDMC guidance by >25% |
| **LiveWire** | quarterly | losses below $50M/yr or exit | any parent funding beyond the $75M term loan |
| **Credit rating** | 10-K / agency actions | S&P off CreditWatch Negative | **any downgrade to non-investment grade** |
| **Tariff bill** | annual 10-K table | below $50M | above **$120M** |

### Catalysts and dates

- **Q3 2026 10-Q, ~early November 2026**, the seasonally loss-making half, against
  guidance implying **HDMC of -$81M to -$41M in H2**. The single most informative filing
  on the calendar.
- **FY2026 10-K, ~late February 2027**, first full year under Starrs; FY2026 units,
  dealer points, U.S. and European share; the first "Back to the Bricks" scorecard; 2027
  guidance.
- **2027 DEF 14A, ~April 2027**: Starrs's first full compensation cycle; open-market
  purchases, if any.
- **Trade policy**, post-2026-02-20 Supreme Court disposition of the struck IEEPA
  tariffs, refunds, and any successor measures. Context, never a trigger **[E3-32]**.
- **Q4 2028**: HOG's first right to buy back the KKR/PIMCO HDFS stake, one-third a year.
- **Q4 2032**, the KKR/PIMCO exchange right into HOG stock, capped at 4.9%.
- **Indian Motorcycle under Carolwood LP**, no longer a public filer after 2026-02-02, so
  its retail performance disappears from the record. Its new CEO, Mike Kennedy, spent 26
  years at Harley-Davidson. Watch instead for Harley's own U.S. 601+cc share in the FY2026
  and FY2027 10-Ks: **if Indian shrinks under private ownership and Harley's share still
  does not recover, the melt is demographic rather than competitive**, which is the worse
  of the two readings and the one this file leans toward.

### The sell rule, for the record **[E2-28]**, no position exists

- SELL if the market judges it more valuable than the facts indicate, **n/a**.
- SELL if funds are needed for something more undervalued or better understood, **the
  $2,750 stays in SGOV [E2-74]**: *"our major parking place for money"*, liquid, waiting,
  so that cash pressure never bends the standard.
- HOLD conditions (return on equity capital satisfactory; management competent and honest;
  market does not overvalue), the first fails today at **-0.9%** manufacturing return on
  manufacturing equity.

### The monitoring question **[E4-17, E3-30]**

*Is this erosion an aberrational cycle, or has the business slipped in a way that
permanently reduces intrinsic business values?* **On eleven years of units, eight years of
share and six years of dealer counts, this run reads it as permanent slippage, not a
cycle.** **[E4-17]** is honoured, *"those beliefs change quite gradually"*, and the belief
formed here took eleven years of filed data to form. **The counter-trigger [E2-40] is
armed too:** if the two reopen conditions are both met, the view crystallizes the other
way and delay would be the graver error.

### Position sizing, a judgment, stated **[E3-45, E2-62]**

**Zero.** Not because the price is uninteresting but because Q2 is OUT. Had it graduated,
**[E2-62]** would bind the sizing anyway: concentration *"makes sense only because"* the
concentrating owner has exceptional financial strength, and $2,750 is the whole
discretionary allocation. **Capital goes to rank #1 [E3-45], and this name is not on the
list.**

### The taxable never-switch test, as tasked

The earmarked account is **TAXABLE**, and **[E2-46]** / **[E3-64]** make it prefer a
compounder taxed once at the end: annual realisation versus a single compounder over
twenty years came to **$25,250 versus $692,000** after tax; Munger's per-annum form is
*"over 3.5 percent"* a year given up by trading. **HOG is the opposite shape on its own
bull case.** The thesis, cyclical trough plus a turnaround plan plus a re-rating, is a
**trade with a sell discipline**, not a hold-forever position; the dividend leg pays 2.7%
of ordinary income annually at half its 2019 rate; and the exit would be a taxable event
inside a few years by construction. **HOG does not qualify as a taxable-account
never-switch name even if it were to graduate on price.** The full switching bar
**[E4-45]**, tax, plus friction of up to 3%/yr **[E3-67]**, plus a *material* gap, is not
close to being cleared here.

- **VERDICT: [x] IN**, the question is answered with pre-committed, dated,
  document-named conditions on both sides, and with a price band that would have to be
  reached before the evidence conditions are even worth re-testing.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (**Q2 OUT**); Q3-Q5 written
      **for the record only**, headed **COMPUTATION, NOT A CLEARANCE** per operator rule 3
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's
      two-business complexity is resolved from Note 19, not carried as a caveat
- [x] Every UNRESEARCHED item names the artifact and where it lives, see the register
- [x] Every UNKNOWABLE item states what specifically cannot be known, median owner age,
      resolvable only by a paid third-party survey, not a filing
- [x] Step 0: the filing was read with accession numbers; **FY2025 OCF $568,922K
      cross-checked three ways inside the document**, and Note 19's manufacturing bridge
      reconciled to the cent
- [x] Owner earnings on multi-year means; **both windows shown** with the spread named and
      the distorted years identified (2022's working-capital build; 2022-23's boom);
      **capex band displayed and disclosed as a judgment** with the [E5-20] exception
      explicitly declined and the reason given; SBC subtracted in full
- [x] **The two-business method was declared before any arithmetic**, the finance business
      was valued separately, and **no blended owner-earnings yield is used as a valuation
      input anywhere**, with the demonstration of why (consolidated OCF +$568.9M FY2025
      vs -$59.7M H1 2026)
- [x] Competitor row built and committed as a separate file, **2 of ~6 real competitors,
      both reached through primary filings (Polaris 10-K/10-Q; BRP 40-F via EDGAR, no
      fallback needed, no aggregator used)**; the peer shortfall is named (BMW and the
      three Japanese majors do not report motorcycles at a comparable metric) and carried
      as a work order; the moat class was decided on the subject's own filed physical
      series, the industry registration series **and the row's market-clearing price
      observation**, which agree
- [x] The row's own limits are recorded, not buried: peer industry figures are internal
      management estimates, and Harley's 601+cc series is **single-sourced from Harley's
      filings** and corroborated only as to direction
- [x] Sovereign for the earnings currency (USD) from the issuing-authority source
      (FRED DGS30), dated **2026-08-27**, taken as observed and never forecast
- [x] Value stated as a **round-number range**; the too-wide range identified as itself
      the conclusion **[E4-25]**
- [x] **One bar chosen** (screamer), not both; **windage count: one**, justified in writing
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Stage 0 reported first, including the dividend trajectory and the
      dividend-compounder failure
- [x] The market-beating claim is not made anywhere; every judgment carries a ledger id or
      is labelled a judgment or an estimate
- [x] Q6 alert thresholds **LISTED ONLY**; `tools/alerts.json` not edited
- [x] No shared file edited; only this run file and the four research files created
- [x] Run committed to git: commit **61ac9d4**, 2026-08-31, together with the four
      research files. **Disclosed:** that commit also swept in 55 files belonging to a
      concurrent UNH session which staged them between this run's `git add` and its
      `git commit`. Nothing was lost or overwritten and no history was rewritten; the
      sweep is recorded here rather than corrected by rebase, per operator rule 6.

## REGISTER
- **Verdict: [x] OUT (about the business, at Q2, for entry).** No position held; no hold
  read required. Q3 for the record: **UNRESEARCHED** (the record of the new management
  does not yet exist; documents named and dated). Q4 for the record: **survivable, and
  melting**. Q5 computation: **the floor fails on the bottom boundary and clears only on a
  boom-inclusive mean [E4-41] forbids trusting; the range is too wide to conclude on.**
- **One line:** *a real brand, an honest and unusually candid set of filings, a
  transformed balance sheet with $986M of net cash at the manufacturer and a finance arm
  de-risked with KKR and PIMCO, attached to a motorcycle company that has lost half its
  units in eleven years and sixteen points of U.S. share in eight, whose segment
  operating income went from $661M to negative in two, whose 2025 owner earnings were a
  working-capital liquidation, whose 2026 owner earnings are guided negative, whose
  dividend is still exactly half the 2019 rate, and whose closest listed competitor paid
  $79.3M of its own cash to give the number-two franchise in the category away for
  nothing; the price is not stupid, and neither is it a screamer.*
- **Stage 0 artifacts found and recorded:** (1) the "+17% five-year dividend growth" is
  the 2020 cut measured backwards through a window containing two $0.02 quarters;
  (2) the "11.6% statute yield" rests on a 2025 net income containing $135.3M pre-tax of
  HDFS-transaction one-timers, and on a consolidated blend that mixes a manufacturer's
  inventory liquidation with a finance company's debt-funded cash flow;
  (3) the boom-window check finds the two best HDMC years in company history inside the
  corpus's default five-year window.
- **The row's decisive fact, recorded here so it is not lost in a research file:** on
  **2026-02-02 Polaris completed the sale of Indian Motorcycle to Carolwood LP for "a
  nominal sales price,"** having taken **$342.5M** of charges, written On Road segment
  goodwill to **zero**, and paid out **$79.3M of net cash** to complete the disposal
  (Polaris FY2025 10-K, acc. 0001628280-26-008033, Note 4). The *"number two position in
  North America … for the 900cc+ category"* claim, present in the FY2023 and FY2024 10-Ks,
  is **absent** from the FY2025 10-K.
- **Work orders (UNRESEARCHED):**
  1. **Q3 2026 10-Q**: EDGAR, ~early November 2026. The seasonally negative half against
     guidance implying HDMC -$81M to -$41M in H2 2026.
  2. **FY2026 10-K**: EDGAR, ~late February 2027. FY2026 units, dealer points, U.S. and
     European 601+cc share, the first full-year "Back to the Bricks" scorecard, and
     audited FY2026 Note 19 consolidating data to re-run this file's owner-earnings table.
  3. **2027 DEF 14A**: EDGAR, ~April 2027. Starrs's first full compensation cycle;
     insider open-market purchases.
  4. **BMW Motorrad, Honda, Yamaha, Kawasaki motorcycle-segment data**, annual reports
     (bmwgroup.com, global.honda, global.yamaha-motor.com, khi.co.jp), retrievable in
     English but **not at a comparable segment metric**; the gap is named in the
     competitor row file.
  5. **Median Harley owner age**: Motorcycle Industry Council owner-demographics study or
     S&P Global Mobility / Polk registration demographics. **Not a filing, and paid.**
     Closed as UNKNOWABLE from filings; the filed proxy is the used-motorcycle
     substitution risk factor, which the company states in its own words.
- **The single biggest concern:** **the price is being asked to bet on the level of a
  business whose direction has been measured, by the company itself, for eleven years.**
  Every bull item in the file, the trough, the cost programme, the new CEO, the net cash,
  the de-risked finance arm, is an argument about how much Harley earns in a normal year.
  None of them is evidence that the eleven-year, -6.7%-a-year unit decline and the
  sixteen-point share loss have stopped. **[E4-32]** says direction is *"the primary
  criterion of a great business"*, and at $27.52 an investor pays roughly $1.5bn for a
  motorcycle company whose own raised guidance says it will earn nothing in 2026, on the
  hope that a management with eleven months of tenure reverses a decade in five years.
  **The sharpest form of the concern is not in Harley's filings at all: seven months ago
  the only other listed company that owned a heavyweight American motorcycle brand
  concluded that the right price for one was nothing, and wrote a cheque to be rid of it.**

---
*This file is a judgment by the AI running the framework. The underlying facts are the
FY2025 10-K (acc. 0000793952-26-000011), the Q2 2026 10-Q (acc. 0000793952-26-000061),
the 2026 DEF 14A (acc. 0000793952-26-000022), the FY2024/FY2023/FY2021/FY2019/FY2015
10-Ks (accessions in Step 0), the 8-Ks named in Q3, the competitor filings cited in the
committed row file, FRED DGS30 dated 2026-08-27, and one flagged live quote. Where a
number is a judgment or an estimate, the (c) choice, the 2026 bottom-boundary build, the
investment-income and cash-tax assumptions inside it, the HDFS valuation basis, the
trough-normal owner-earnings band, and the entry band, it is labelled as one.*
