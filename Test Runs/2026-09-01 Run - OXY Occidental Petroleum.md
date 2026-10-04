# Company Run — Occidental Petroleum Corporation (NYSE: OXY) — 2026-09-01
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file and
that document disagree, that document governs.

**Position context: NONE HELD. Fresh entry run**, surfaced from `Screens/WATCHLIST RUN QUEUE.md`
TIER 1 wave 1 (the tier that needs ≤6% perpetual growth to clear the [E4-28] floor).

**Screen input, reproduced as received and headed as what it is — a COMPUTATION:** cap
≈$58,989M · owner-earnings bottom boundary ≈$3,944M · bottom yield 6.69% against a 5.18%
sovereign · 3.31% perpetual growth required for the [E4-28] floor · spread 64% · nine-year
owner earnings (OCF − SBC − capital acquired), $M: **1,247 · 2,514 · 812 · 1,218 · 7,277 ·
11,970 · 5,595 · 3,998 · 3,476** · capex/D&A 0.77×.

**Every one of those inputs is superseded below, and the run says why.** Three of them are
wrong on the filed record, and the errors do not point the same way.

**The operator's tasking is answered in full**, and where the tasking's own priors turned out
to be wrong on the filings, the run says so rather than confirming what it was sent to
confirm — operator rule 9 and **[E4-26]**.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED. NO → UNKNOWABLE. **[E4-19]**

---
# STAGE 0 — THE FIVE-MINUTE ARTIFACT CHECK
*Reported first, per operator tasking, before any gate opens.*

## (a) THE CAP — and the two claims sitting in front of the common

| | |
|---|---|
| **Filed cover share count** | **999,637,371** shares outstanding **as of July 31, 2026** — Q2 2026 Form 10-Q cover page, accession **0001628280-26-053388** |
| Currency of that count | **Verified current**, 32 days old at the run date. It reconciles to Note 9 of the same 10-Q: **999,708,551** outstanding at 2026-06-30, the 71,180-share difference being ordinary plan and warrant activity in July. |
| Price | **$60.95, NYSE close 2026-09-01** *(Yahoo chart API — aggregator, live quote only, flagged; `regularMarketTime` equals the session close, so the bar is complete)*. 52-week range **$38.80–$67.45**. |
| **Market cap, filed cover shares** | **999,637,371 × $60.95 = $60,928M** |
| **Warrant overhang — large and NOT theoretical** | **17.9M Common Stock Warrants at a $22.00 strike** (expiring 2027-08-03, deep in the money) and **83.9M Berkshire Warrants at a $59.59 strike** (10-Q Note 9, as of 2026-06-30). |
| **Cap on total economic shares** | **1,101,437,371 × $60.95 = $67,133M — 10.2% above the headline.** |
| **Preferred stock, ahead of the common** | **84,897 shares, $100,000 face each = $8,490M face**, carried at **$8,287M**, liquidation preference **$105,000/share = $8,914M**, mandatory-redemption cost **110% of face = $9,339M**. |
| Debt | **$13,743M** total debt and finance leases at 2026-06-30 (10-Q Note 6); **$11.8bn of principal** per the Q2 release. Cash **$4,188M**. |
| **Enterprise value including the preferred** | **60,928 + 13,743 − 4,188 + 8,490 = $78,973M** |

**THE SCREEN'S CAP IS NOT WRONG BY MUCH; IT IS BLIND BY A LOT.** $58,989M against $60,928M is
a price difference of no consequence. But the screen prices **only the common**, and behind
that common sit **$8.5bn of face-value preferred stock paying an 8% coupon** and **101.8M of
warrants**, one tranche of which is struck at $59.59 against a $60.95 quote. The operator's
instruction to quantify this is correct and the arithmetic is below at Q4.

## (b) THE BERKSHIRE WARRANTS ARE AT THE MONEY TODAY — a live, dated fact

Q2 2026 10-Q, Note 9, verbatim: *"Anti-dilutive securities excluded from diluted shares
(millions) 83.9"*. They were excluded from the Q2 diluted count because the strike of
**$59.59** sat above the average price for the quarter. **At the 2026-09-01 close of $60.95 they
are in the money.** Every valuation below is therefore reported on **both** share counts, and the
fully-diluted count is the one used for the price band.

## (c) THE DIVIDEND — the operator's COLM test, run, and the operator's own figure corrected

**The operator's brief says the 2020 cut ran "from $0.79 to $0.11." The filed record says it
ran from $0.79 to $0.01.** The ex-dividend series (Yahoo chart events, cross-checked against
the FY2020 10-K's dividends-per-share disclosure) is:

| year | declared/paid per share | note |
|---|---|---|
| 2016 | $3.02 | |
| 2017 | $3.06 | |
| 2018 | $3.10 | |
| 2019 | **$3.14** | the pre-cut peak; $0.79/qtr |
| **2020** | **$0.82** | $0.79 in Q1, then **$0.01** for the remaining three quarters |
| **2021** | **$0.04** | $0.01 all four quarters — the floor |
| 2022 | $0.52 | $0.13/qtr |
| 2023 | $0.72 | $0.18/qtr |
| 2024 | $0.88 | $0.22/qtr |
| 2025 | $0.96 | $0.24/qtr |
| 2026 | $1.04 paid; **$1.12 declared run-rate** | $0.26/qtr, raised to **$0.28** payable 2026-10-15 (Q2 release) |

**THE MANUFACTURED-GROWTH ARITHMETIC, AND ITS CORRECTION.**

- **Raw five-year lookback, 2021 → 2026: `(1.04/0.04)^(1/5) − 1 = +91.9% a year.`** That is the
  COLM error in its purest form: the denominator is a **penny**, deliberately set there to
  survive. Any dividend-growth screen anchored on 2021 returns a number that describes a
  near-death experience, not a compounding business.
- **The corrected test, from the pre-cut rate: `(1.04/3.14)^(1/7) − 1 = −14.6% a year.`**
- **Level check: the current declared rate of $1.12 is 64% BELOW the 2019 rate of $3.14, seven
  years later.** The dividend has not been restored; it has been rebuilt from zero to about
  a third of what it was.
- Current yield at $60.95: **$1.12 ÷ $60.95 = 1.84%.**

> **RECORDED: OXY IS NOT A DIVIDEND COMPOUNDER AND ANY FIVE-YEAR DIVIDEND-GROWTH FIGURE FOR IT
> IS AN ARTIFACT OF THE 2020 CUT.** This is the WEYS/COLM lesson in its third shape. The name
> is run from here as a commodity-cyclical read.

## (d) THE BOOM-WINDOW ARTIFACT **[E4-41, E4-38]** — TESTED, AND THE PREDICTION IS CONFIRMED, TWICE OVER

The operator's instruction was to look at the **shape** of the nine-year series and test
whether the mean is meaningful at all. It is not, and there are **two** independent reasons,
not one.

### The series, reproduced exactly, and located

The screen's construction is **OCF (total, as filed each year) − capital expenditures − SBC**,
and it reproduces to the dollar from SEC XBRL:

| FY | OCF | capex | SBC subtracted | = screen OE |
|---|---|---|---|---|
| 2017 | 4,861 | 3,599 | 15 | **1,247** |
| 2018 | 7,669 | 4,975 | 180 | **2,514** |
| 2019 | 7,375 | 6,367 | 196 | **812** |
| 2020 | 3,955 | 2,535 | 202 | **1,218** |
| 2021 | 10,434 | 2,870 | 287 | **7,277** |
| 2022 | 16,810 | 4,497 | 343 | **11,970** |
| 2023 | 12,308 | 6,270 | 443 | **5,595** |
| 2024 | 11,439 | 7,018 | 423 | **3,998** |
| 2025 | 10,532 | 6,427 | 629 | **3,476** |

*(FIRST CORRECTION TO THE SCREEN: the SBC column is wrong. The FY2025 10-K's stock-based
incentive note states the expense as **$234M, $213M and $203M** for 2025, 2024 and 2023 —
not $629M, $423M and $443M. The screen is subtracting something else under that label and it
makes the recent years look ~$200–400M worse than the filing does. The error is in the
company's favour once corrected, and the run corrects it.)*

### Shape test 1 — the distribution

- nine-year mean **$4,234M** · median **$3,476M** · min **$812M** (2019) · max **$11,970M** (2022)
- **max ÷ min = 14.7×**
- **FY2021 + FY2022 = $19,247M = 50.5% of the entire nine-year total, out of 2 of 9 years
  (22% of the window).**
- **Excluding the two spike years, the seven-year mean is $2,694M — 36.4% below the
  nine-year mean.**

Half the "earnings" being averaged came from a fifth of the window. **A mean built that way is
not a central tendency; it is a boom with seven quiet years attached.** The operator's read is
correct and the screen's "steady" flag is an artifact of the window's width.

### Shape test 2 — THE FILER'S OWN SENSITIVITY MAKES THE MEAN SMALLER THAN ITS OWN ERROR BAR

This is the decisive arithmetic and it comes from OXY's own Item 7A, FY2025 10-K, verbatim:

> *"Price changes at global prices and levels of production affect the Company's budgeted 2026
> pre-tax cash by approximately **$240 million for a $1 per barrel change in WTI price** and
> approximately $25 million for a $1 per barrel change in Brent price. If domestic natural gas
> prices varied by $0.50 per Mcf, it would have an estimated annual effect on the Company's
> budgeted 2026 pre-tax cash of approximately $120 million."*

- Annual average WTI across the window ran from **$39.16 (2020)** to **$94.53 (2022)** — a
  spread of **$55.37**.
- **$55.37 × $240M = $13.29bn of pre-tax cash swing** attributable to price alone.
- The mean it is being averaged into is **$4.23bn**.
- **The price swing inside the window is 3.1× the mean the window produces.**

**That is the answer to "test whether the mean is meaningful at all." It is not.** A nine-year
mean is a legitimate estimator when the year-to-year variation is noise around a level. Here
the variation is not noise around a level — it *is* the level, set by an exogenous price the
company states in its own filing it does not control. Averaging it produces a number with no
referent: no year resembles it, and the next year's deviation from it is determined by
something the filer says is *"difficult to reliably forecast."*

**[E3-55] is the test that could rescue this and it fails.** The corpus does permit
volatility: *"If we have a business about which we're extremely confident as to the business
result, **we would prefer that it have high volatility** than low volatility."* The condition is
confidence in **the business result**. See's losing money eight months a year is a seasonal
pattern with a certain annual endgame. **OXY's variation is not a pattern with a certain
endgame; it is the unhedged output of a price nobody can forecast.** The distinction is exactly
the one [E3-55] draws, and OXY sits on the wrong side of it.

### Shape test 3 — THE SCALE ARTIFACT, which the operator did not name and which cuts the OTHER way

| | 2017 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2Q26 |
|---|---|---|---|---|---|---|---|---|---|
| **Production, Mboe/d** | 601 | 720 | 1,364 | 1,166 | 1,175 | 1,223 | 1,327 | **1,434** | **1,433** |

**The window spans a company that grew 2.39× in physical volume**, through Anadarko (closed
2019-08-08) and CrownRock (closed 2024-08). A nine-year mean of a company that more than
doubled **understates** the current business — the same [E4-38] date-selection warning the
MTDR run found running backwards, and the prior established there is carried here without
re-derivation. **So the nine-year mean is wrong in two directions at once**: too high for the
price mix, too low for the scale. That is not a number to be adjusted. It is a number to be
abandoned, and the run abandons it.

### Shape test 4 — AND THE BUSINESS BEING AVERAGED NO LONGER EXISTS

**OxyChem — the chemical segment — was sold to Berkshire Hathaway for $9.7 billion cash. The
sale closed on January 2, 2026.** FY2025 10-K, Note 4, verbatim:

> *"In October 2025, the Company announced entry into a purchase and sale agreement with
> Berkshire Hathaway (the Purchase Agreement) to sell all of the issued and outstanding equity
> interests in OxyChem in an all-cash transaction for $9.7 billion, subject to customary
> purchase price adjustments. **The OxyChem Transaction closed on January 2, 2026.** An Occidental
> subsidiary will retain environmental liabilities relating to legacy sites."*

Every year in the screen's nine-year series **includes OxyChem's cash flow**. OxyChem
contributed **$926M, $920M and $2,073M of operating cash flow in 2025, 2024 and 2023**
(FY2025 10-K cash-flow statement, discontinued-operations line). **Roughly a tenth of the
recent series, and more in the earlier years, came from a business Occidental no longer owns.**

> **STAGE 0 VERDICT ON THE SCREEN INPUT: the nine-year owner-earnings series is not a
> measurement of the business that exists on 2026-09-01. It mixes a company 2.4× smaller, a
> 2021–22 price spike worth half the total, a divested chemical division, an SBC line that
> does not match the filing, and a (c) that is total capex rather than maintenance capex. The
> run rebuilds it from the filings below and does not use the screen's numbers for any
> verdict.**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.25% · observation date 2026-08-31 · FRED DGS30**, Treasury constant-maturity,
  fetched direct from `fredgraph.csv?id=DGS30` on 2026-09-01. Local copy
  `Test Runs/_research 2026-09-01 OXY/DGS30_2026-09-01.csv`. The 1–2 day publication lag is
  standing and immaterial. *(The screen used 5.18%, the 2026-08-26 observation. The run uses
  the latest observation and notes the 7bp difference moves nothing.)*
- **FX: none.** Quote currency = earnings currency = USD. International operations (Oman, UAE,
  Algeria) sell into dollar-denominated markets and the filing reports in USD throughout.

**The filing was read — not tagged data [E3-27, E4-14]:**

1. **FY2025 Form 10-K** (year ended 2025-12-31), filed **2026-02-18, accession
   0001628280-26-009059** — [x] MD&A incl. Outlook, Cash Flow Analysis, Liquidity, Contractual
   Obligations  [x] consolidated statements of cash flows **including the detail lines**
   [x] footnotes (Note 1 accounting policies and discontinued-operations basis of presentation;
   Note 4 Acquisitions, Divestitures and Other Transactions; Note 5 Long-Term Debt; Note 7
   equity-method investments; Note 8 fair value and impairments; Note 9 income taxes incl. the
   cash-taxes-paid table; Note 11 Environmental Liabilities; Note 13 Stockholders' Equity — the
   **preferred stock and warrant terms**; Note 14 stock-based compensation; **Note 15 Industry
   Segments**)  [x] **Supplemental Oil and Gas Information (Unaudited)** — reserve
   rollforwards, **Costs Incurred**, Results of Operations, capitalized costs  [x] Item 1A risk
   factors  [x] Item 7A market risk **including the price sensitivities used above**.
2. **Q2 2026 Form 10-Q** (period 2026-06-30), filed **2026-08-05, accession
   0001628280-26-053388** — balance sheet, cash-flow statement, Note 6 debt incl. the
   **debt-extinguishment table**, Note 9 stockholders' equity incl. **warrants and preferred**,
   Note 10 segments, MD&A production and realized-price tables.
3. **8-K + Ex-99.1, Q2 2026 results**, filed **2026-08-05, accession 0001628280-26-053377** —
   the quarterly production, realization, capex and free-cash-flow schedules used for the
   normalization, and the dividend increase.
4. **DEF 14A**, filed **2026-03-19, accession 0001628280-26-019816** — incentive metrics and the
   **metric switch**, related-party disclosure of the Berkshire transaction, 5% beneficial
   owners.
5. **8-K, Item 5.02**, filed **2026-05-04, accession 0000950157-26-000569** — **the CEO
   change**.
6. **8-K**, filed **2026-03-09, accession 0000950157-26-000265** — the tender offers and the
   **Fifth Supplemental Indenture eliminating covenants** on the 6.125% 2031 notes.
7. SEC XBRL `companyfacts` for CIK 0000797468 — used **only** to build the FY2017–FY2022 series
   and to locate the screen's construction. No verdict rests on it.

**Figures cross-checked against the filed statement (operator protocol 4):**
- **Check 1 — cash flow.** The FY2025 Consolidated Statements of Cash Flows read, on the
  operating section: **"Operating cash flow from continuing operations 9,606 · 10,519 ·
  10,235"**, **"Operating cash flow from discontinued operations 926 · 920 · 2,073"**, **"Net
  cash provided by operating activities 10,532 · 11,439 · 12,308"** ($M, FY2025 · FY2024 ·
  FY2023). SEC XBRL carries the identical values under the identical accession. **Ties.**
- **Check 2 — EPS.** Q2 2026 net income attributable to common $2,807M ÷ 997.1M basic weighted
  shares = **$2.815 → the filed basic EPS of $2.80** (the small residual is the $20M allocated
  to participating securities, which the filing shows separately). **Ties.**
- **Check 3 — the preferred.** 84,897 preferred shares × $100,000 face × 8% = **$679.2M**,
  against the filed **"Occidental paid $679 million in preferred stock dividends in 2025"**
  (Note 13) and the filed **"Less: Preferred stock dividends and redemption premiums (679)"**
  in the Note 15 segment reconciliation. **Ties on three independent lines.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Occidental drills wells — mostly
horizontal wells in the Permian Basin of West Texas and New Mexico, plus the Rockies, the Gulf
of America, Oman, the UAE and Algeria — and sells what comes out of them at whatever the
posted market price is that day. In 2025 it sold **1,434 thousand barrels of oil equivalent per
day**: 62% oil and NGL, 38% natural gas by energy content. It received **$64.60 a barrel for oil
worldwide, $20.60 a barrel for NGLs, and $1.58 per thousand cubic feet for domestic natural
gas**. Against that it spent **$8.94 per barrel of oil equivalent on lease operating expense**,
plus transportation, production taxes and overhead, and charged **$13.60 per Boe of depletion**.
Everything above those costs is margin. It spent **$6,427M of capital in 2025** to keep the
wells coming, because **each well's output falls steeply from the day it is drilled** and
production stops unless new wells replace the decline.

There are two other pieces. **Midstream and marketing** owns pipeline capacity, gas processing
and a 40.9% interest in Western Midstream (WES), and earns spreads on moving and processing
its own and third-party volumes; it produced **$252M of pre-tax segment income in 2025**
against $563M in 2024 and a **loss of $35M in 2023**. Inside it sits **Oxy Low Carbon Ventures**,
which is building **STRATOS**, a direct-air-capture plant in Ector County, Texas. **The chemical
business, which used to be the third leg, was sold to Berkshire Hathaway on 2026-01-02.**

**The scarce input this business controls: none.** This is the finding, and it is stated at Q1
because it determines everything after it. Occidental controls its **costs** and its **capital
allocation**. It does not control **one dollar** of its selling price. The 10-K says so in its own
words, and the arithmetic is in Item 7A: **$240M of pre-tax cash per $1 of WTI.** The acreage is
not scarce either — it is bought at auction and in bolt-ons at prices set by other bidders.

**Will the fundamentals look broadly the same in ten years?** The *mechanics* will: rock,
decline curves, a screen price. The *level* will not, and no one can say which way. That is the
honest answer, and it is the reason [E3-31]'s *"relatively simple and stable in character"*
splits: this business is **simple** and it is **not stable in character**.

**But Q1 asks whether I can understand how it makes money — not whether I like the answer.** I
can. The unit economics are transparent, the filings are complete, the physical series is
disclosed, and I can compute the whole thing from the supplemental oil and gas tables. **A
business I understand and dislike is a Q2 problem, not a Q1 problem.** Marking Q1 OUT here would
be smuggling the moat verdict into the understanding gate.

- **VERDICT: [x] IN.** The business is understood. The instability is recorded and carried to
  Q2, where the corpus files it.

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**THIS IS THE CENTRAL QUESTION OF THE RUN, PER THE OPERATOR'S TASKING, AND THE COMMODITY
DOCTRINE IS WORKED THROUGH BLOCK BY BLOCK BELOW RATHER THAN SUMMARIZED.**

### The three criteria **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."*

- **(1) Needed or desired — [x] YES.** Unambiguously. The 10-K's own Outlook: *"various industry
  forecasts indicate a growing demand for hydrocarbons for the next decade."*
- **(2) No close substitute — [ ] FAILS, and it fails at the deepest possible level.** A barrel
  of Occidental's oil is not thought by its customers to have no close substitute; it is
  thought by its customers to have a **perfect** substitute, which is any other barrel of the
  same gravity delivered to the same point. The filing prices its own output as *"Worldwide oil
  as a percentage of average WTI: 104%"* — the product is defined by reference to somebody
  else's index. **When your own MD&A expresses your selling price as a percentage of a
  benchmark, criterion 2 has already been answered.**
- **(3) Not subject to price regulation — [x] technically YES**, no rate base, no tariff. But
  see **[E2-59]** below: the absence of regulation here is not a franchise property, it is the
  absence of the only thing that ever floored this class.

**0 of 3 on the criterion that matters. [E3-03] is failed.**

### THE COMMODITY DOCTRINE **[E2-58]**, applied line by line

> *"persistent over-capacity without administered prices (or costs) equals poor profitability"*;
> long-term profitability set by *"the ratio of supply-tight to supply-ample years"*; and
> prosperity breeds the next glut — *"nothing fails like success."*

**The ratio of supply-tight to supply-ample years, read off Occidental's own realizations:**

| | 2021 | 2022 | 2023 | 2024 | 2025 | 1Q26 | **2Q26** |
|---|---|---|---|---|---|---|---|
| Worldwide oil, $/Bbl | — | — | 76.85 | 75.05 | 64.60 | 69.91 | **96.78** |
| Worldwide NGL, $/Bbl | — | — | 21.32 | 21.38 | 20.60 | 18.99 | **24.64** |
| **Domestic natural gas, $/Mcf** | — | — | **2.04** | **0.94** | **1.58** | **1.01** | **(1.48)** |
| Domestic gas as % of NYMEX | — | — | — | — | 52%¹ | 26% | **(51)%** |

*¹ H1 2025. All figures from the FY2025 10-K MD&A "Average Realized Prices" table and the Q2
2026 10-Q MD&A table.*

**In the most recent filed quarter, Occidental received NEGATIVE $1.48 per thousand cubic feet
for its domestic natural gas.** It paid buyers to take 38% of its volume. That is [E2-58]'s
over-capacity condition observed directly, and the mechanism is [E2-27]'s exactly: associated
gas arrives from oil-directed drilling whether or not anyone wants it, every operator's
individually rational decision to drill for oil is collectively irrational for the gas price,
and Permian takeaway fills up. **This is the same finding the MTDR run recorded at Matador in
the same quarter** (realised gas $(0.79)/Mcf) — two independent Permian filers, same quarter,
same sign. The prior established there is confirmed here, not re-derived.

**"Nothing fails like success" is observable in the same filing.** The 2Q26 oil realization of
$96.78 is what breeds the next glut, and the 10-K names the machinery: *"the actions of OPEC,
other significant producers and governments."*

**The one exception [E2-58] permits — "a cost advantage that is both wide and sustainable …
By definition such exceptions are few."** Occidental's per-unit cost record is **good and
improving**, and the run states that at full strength before testing it:

| $/Boe | 2023 | 2024 | 2025 |
|---|---|---|---|
| Lease operating expense | 10.48 | 9.75 | **8.94** |
| Depletion, depreciation and amortization (O&G segment) | 13.69 | 13.50 | 13.60 |

LOE per Boe has fallen **15% in two years**, and the 10-K attributes it to *"operational
efficiencies in the Permian Basin and lower energy costs in Oman"* — real operating
improvement, not a denominator effect. **That is a genuine achievement and it is recorded as
one.** Whether it is *wide and sustainable* relative to peers is a relative claim and is
settled by the competitor row below, not by this table.

### THE SECOND STEP **[E3-62]** — asked, and unanswerable in Occidental's favour

> vendor projections show the savings; none ever asks *"how much is going to stay home and how
> much is just going to flow through to the customer"* — in a commodity business the gains flow
> to buyers; in the one-paper town they stick.

For Occidental the answer is structural and it is **half good**. A **cost** saving stays home
entirely: there is no customer to pass it to, because there is no price to negotiate. That is
the favourable half and it is why the LOE improvement above is real money. **But the second
step's other half is fatal: a cost saving is the ONLY gain that can stay home, because the
price side of the equation is not Occidental's to move.** The textile-loom lesson applies with a
twist — Occidental keeps its own efficiency gains, but it also keeps none of the price, and
across the industry the same efficiency gains lower the marginal cost of supply and therefore
the clearing price. **The gains stay home at the company; they flow through to the customer at
the industry.** [E2-27]'s exact structure: *"viewed individually, each company's capital
investment decision appeared cost-effective and rational; viewed collectively, the decisions
neutralized each other."*

### THE RESCUE THAT ISN'T **[E2-59]** — the regime check

> administered pricing can floor a commodity business's profits, but the moat belongs to the
> **regime**, and *"That day is gone"* is how it ends.

**No administered price. No cartel membership. No rate base. No regulated tariff.** Occidental
is a **price-taker to OPEC's administered supply, not a member of it** — the 10-K lists *"the
actions of OPEC"* among the factors affecting its price, which is the definition of standing on
the wrong side of an administered regime. The one contractual structure running Occidental's
way is its **international production-sharing contracts** (Oman, UAE, Algeria), which have
cost-recovery mechanics that partially cushion low prices — and the 10-K says so: *"These
price-change sensitivities include the impact of PSC and similar contract volume changes on
income."* **That is a contract term, bought at a bid round, in someone else's sovereign
jurisdiction. It floors a slice of the earnings; it does not create a class.** [E2-59]'s own
scoping sentence governs: *"Regulation caps a franchise and floors a commodity business;
neither creates the class."*

### **[E4-04]** — MUST THE MOAT BE CONTINUOUSLY REBUILT? Worked from the filed reserve tables

The corpus scopes [E4-04] precisely: what "enduring" excludes is the moat whose basis must be
**periodically replaced** — *"rapid-change industries, **depleting assets**."* The test: *"does a
lapse in spending destroy the structure, or merely narrow it — and does the spending defend the
same advantage, or **buy its replacement**?"*

**THE ANSWER IS IN THE SUPPLEMENTAL OIL AND GAS TABLES AND IT IS WORSE THAN MATADOR'S.**

All figures from the FY2025 10-K Supplemental Oil and Gas Information (Unaudited) — the reserve
rollforwards and the Costs Incurred table — converted at 6 Mcf = 1 Boe, MMBoe:

| | FY2023 | FY2024 | FY2025 | **3-yr total** |
|---|---|---|---|---|
| **Production** | 446.3 | 486.2 | 523.2 | **1,455.7** |
| Extensions and discoveries | 152.5 | 325.5 | 339.5 | 817.5 |
| Improved recovery | 23.0 | 47.3 | 60.3 | 130.6 |
| **Organic additions (drill bit)** | **175.5** | **372.8** | **399.8** | **948.2** |
| **ORGANIC RESERVE REPLACEMENT** | **39.3%** | **76.7%** | **76.4%** | **65.1%** |
| Revisions of previous estimates | +406.2 | +169.5 | +161.3 | +737.0 |
| Purchases of reserves in place | 31.3 | **623.3** | 10.2 | 664.8 |
| Sales of reserves in place | (2.3) | (49.7) | (56.8) | (108.8) |
| Replacement incl. revisions | 130.3% | 111.5% | 107.2% | **115.8%** |
| Replacement incl. revisions **and purchases** | 137.3% | 239.7% | 109.2% | **161.4%** |

**OCCIDENTAL REPLACES ROUGHLY TWO-THIRDS OF ITS PRODUCTION WITH THE DRILL BIT. The rest comes
from revisions and from buying other people's reserves.** Over three years the drill bit
replaced **65.1%** of what was produced. The gap was closed by **+737 MMBoe of revisions** —
which are estimate changes driven by price decks, infill results and development-plan updates,
and which reverse when prices fall (the FY2025 note discloses **negative price revisions of 57
MMbbl of oil**, offset by positive economic-condition revisions of 73 MMbbl) — and by **623
MMBoe purchased in 2024, which is CrownRock.**

**That is [E4-04]'s excluded class demonstrated from the filer's own tables, and it is the
Rhodes Ridge case the corpus already decided.** The spending does not defend the same
advantage; **it buys the replacement**, and in 2024 it bought it for **$12.1bn of property
acquisition cost**.

**The physical series [E4-55], which is the honest one:**

| | YE2023 | YE2024 | YE2025 |
|---|---|---|---|
| Proved developed reserves, MMBoe | 2,750 | 3,190 | 3,294 |
| **Proved developed reserve life, years** | **6.16** | **6.56** | **6.30** |
| Total proved reserves, MMBoe | 3,982 | 4,612 | 4,603 |
| **Total proved reserve life, years** | **8.92** | **9.49** | **8.80** |
| Proved undeveloped, MMBoe | 2,961 | 3,326 | **1,309**¹ |

*¹ YE2025 PUD = 625 MMbbl oil + 333 MMbbl NGL + 2,108 Bcf gas ÷ 6 = **1,309 MMBoe = 2.50 years
of production of drilling inventory booked as proved.***

**Total proved reserve life fell from 9.49 to 8.80 years in the year CrownRock was fully
consolidated.** The reserve base did not grow in 2025 (4,612 → 4,603 MMBoe) while production
grew 7.6%. **A lapse in spending here does not narrow the structure. It starts a clock, and the
filed clock reads 6.3 years developed and 8.8 years proved.**

### The pricing tests — every one of them, and none of them can be run in Occidental's favour

- **Untapped pricing power [E3-33] / [E5-28]: none, structurally.** [E5-28] scopes the class:
  *"If you name some business that has incredible pricing power, you're talking about a
  business that's **a monopoly or a near monopoly**."* Occidental produces roughly 1.2 million
  Boe/d in a United States producing over 13 million barrels a day of crude. Not a monopoly by
  three orders of magnitude of market share.
- **The inverse metric [E4-37]: CANNOT BE RUN AT ALL.** *"you can almost measure the strength of
  a business over time by **the agony they go through in determining whether a price increase
  can be sustained**."* There is no price decision at Occidental. There is no agony because
  there is no deliberation because there is no discretion. **The metric's total inapplicability
  is the sharpest possible negative reading**, and it is the same reading the MTDR run recorded.
- **Two-characteristic test [E2-44]: 0 of 2.** (1) Raise prices with demand flat and capacity
  under-utilised — **no**, and in 2Q26 the price went below zero on 38% of the volume. (2) Grow
  dollar volume with only minor additional capital — **no**: the 2026 capital plan is
  **$5.5–5.9bn against a $60.9bn market cap, 9–10% of the capitalisation annually, to hold
  production FLAT.**
- **Dominance class [E2-53]: unavailable.** *"Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be."* At Occidental the
  marketplace determines it and the 10-K says so.
- **The attacker's test [E2-45]** — *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* An attacker with ample capital does not need to compete with
  Occidental at all; it bids against Occidental at the next lease sale, or it buys a private
  operator, as Occidental itself did with CrownRock. **The barrier to entry is capital, and
  capital is the one thing the attacker was assumed to have.**
- **Direction [E4-32] — "the moat widened every year" is "the primary criterion of a great
  business."** Occidental's ownable metrics: total proved reserve life **9.49 → 8.80 years**;
  proved developed life **6.56 → 6.30**; organic replacement **76.7% → 76.4%** on a three-year
  mean of 65.1%; domestic realised gas **$2.04 → $0.94 → $1.58 → $(1.48)**. Against that, LOE
  per Boe **$10.48 → $8.94** and G&A discipline, which are real and are the only things moving
  the right way. **Direction: mixed on costs, negative on everything that is a claim about
  position.**

### **[E4-36]** — which of the four causes of extreme success?

Not the extreme max/min of one variable; not a non-linear combination. It is either **extreme
performance over many factors** (a large, competent operator that has cut LOE 15% in two years,
integrated two mega-acquisitions and holds premier Permian acreage) or **wave-riding
[E3-51]** — *"when a surfer gets up and catches the wave and just stays there, he can go a long,
long time. But if he gets off the wave, he becomes mired in shallows."* **The filed evidence
says both are present and only one is ownable.** The 2021–22 result was the wave: **half the
nine-year owner-earnings total from 22% of the window**, on a price Occidental did not set. The
cost record is the ownable part, and [E2-37]'s sentence governs what it can be worth:
*"a textile company that allocates capital brilliantly within its industry is a remarkable
textile company — **but not a remarkable business**."*

### KEY-PERSON DEPENDENCE — recorded HERE as a moat defect **[E4-23]**, and it just changed hands

**Vicki Hollub, CEO since 2016 and the architect of both the Anadarko and CrownRock
acquisitions, retired effective June 1, 2026.** 8-K filed 2026-05-04, accession
0000950157-26-000569, verbatim:

> *"On April 30, 2026, Vicki Hollub, President and Chief Executive Officer ('CEO') of Occidental
> Petroleum Corporation ('Occidental'), informed the Board of Directors of Occidental (the
> 'Board') of her decision to retire, effective as of June 1, 2026 (the 'Transition Date')."*
> … *"the Board unanimously approved the appointment of **Richard A. Jackson, 50**, as
> Occidental's President and CEO and as a member of the Board."*

Per **[E4-23]** this is recorded at Q2 as a **moat defect, not at Q3 as a compliment**: *"if a
business requires a superstar to produce great results, the business itself cannot be deemed
great … The partnership's moat will go when the surgeon goes."* Whatever view one takes of
Hollub's record — and it is a mixed one, worked at Q3 — **a business whose ten-year trajectory
was set by one person's two acquisition decisions is a business where the person mattered more
than the position**, which is precisely what [E2-53]'s dominance class excludes.

### THE COMPETITOR ROW — required **[E3-28]**

> *"**I can't be an intelligent owner of a business unless I know what all the other businesses
> in that industry are doing.**"* — **[E3-28]**

**Peers taken: four, plus the subject — Diamondback (FANG), Devon (DVN), EOG Resources (EOG)
and ConocoPhillips (COP).** Every figure below is computed from **each filer's own FY2025 Form
10-K Supplemental Oil and Gas Disclosures** — the reserve rollforwards and the Costs Incurred
tables — on the same basis, same window, 6 Mcf = 1 Boe. Local extracts:
`Test Runs/_research 2026-09-01 OXY/{OXY,FANG,DVN,EOG,COP}.txt`. Chevron was pulled and is
**excluded with a reason**: as an integrated with large equity affiliates it does not present a
comparable consolidated E&P cost-and-reserve pair, and forcing it into the row would be a
worse error than leaving it out. **Four of the industry's roughly eight real large-cap US
comparables were taken.**

| FY2025 unless stated | **OXY** | FANG | DVN | EOG | COP |
|---|---|---|---|---|---|
| Production, MMBoe | **523.2** | 336.2 | 307.0 | 452.0 | 796.0 |
| Organic replacement, **drill bit only**, FY2025 | **76.4%** | 172.2% | 144.3% | 74.3% | 23.7% |
| Organic replacement, **drill bit only**, 3-yr | **65.1%** | 168.9% | 135.3% | 126.5% | 32.6% |
| Replacement, **all organic sources incl. revisions**, 3-yr | **115.8%** | 101.0% | 144.6% | 145.7% | 105.1% |
| **F&D, drill-bit basis, 3-yr, $/Boe** | **$18.28** | $8.03 | $9.84 | $11.29 | $51.23 |
| **F&D, all-organic-sources, 3-yr, $/Boe** | **$10.29** | $13.42 | $9.21 | $9.80 | $15.91 |
| Proved developed reserve life, YE2025, yrs | **6.30** | 7.50 | 6.01 | 7.40 | 5.33 |
| Total proved reserve life, YE2025, yrs | **8.80** | 10.76 | 7.91 | 12.20 | 8.17 |
| DD&A on producing activities, $/Boe | **$13.60** | $14.70 | n/d | n/d | n/d |

### WHAT THE ROW ACTUALLY SAYS — and it is NOT what a single-metric reading would have said

**This is the run's strongest disconfirming finding against its own prior, and [E4-26] requires
it be stated first and in full.**

On the **drill-bit-only** metric — extensions and discoveries plus improved recovery, divided by
production — Occidental replaces **65.1%** of what it produces over three years and its finding
cost is **$18.28/Boe, the worst of the four comparable filers**. Taken alone that reads as a
company liquidating its base at a premium price, and that is where the run's first pass landed.

**The competitor row refutes it.** Look at ConocoPhillips: **32.6%** drill-bit replacement and a
computed drill-bit F&D of **$51.23/Boe**. ConocoPhillips is not liquidating. The number is an
artifact of **booking convention**: COP books almost all of its additions through *revisions*
(*"Upward revisions of 554 MMBOE were predominately driven by progression of development plans
of 635 MMBOE in the Lower 48 unconventional plays"* — FY2025 10-K, verbatim), while Diamondback
books them through *extensions and discoveries* and then takes them back through **negative**
revisions of 304 MMBoe in 2025 alone. **The drill-bit ratio is not comparable across filers and
therefore cannot support a moat claim in either direction.**

**On the metric that IS robust to booking convention — all organic sources, three years —
the row is flat:**

**DVN 144.6% · EOG 145.7% · OXY 115.8% · COP 105.1% · FANG 101.0%**
**F&D: DVN $9.21 · EOG $9.80 · OXY $10.29 · FANG $13.42 · COP $15.91**

**Occidental sits in the middle of a tightly bunched field on both.** It is not cheap and it is
not expensive; it replaces more than it produces and so does everyone else; its reserve life is
mid-pack and its DD&A per barrel is a dollar below Diamondback's.

> **AND THAT IS THE Q2 FINDING, NOT A REPRIEVE FROM IT.** **[E2-58]**'s one exception is *"a cost
> advantage that is both **wide and sustainable** … By definition such exceptions are few."*
> The competitor row does not show Occidental with a narrow cost advantage. **It shows
> Occidental with no measurable cost advantage at all**, in either direction, against four
> filers whose only common property is that they drill the same rock. A moat is a claim about
> **relative** position; the row is the instrument for testing it; and the instrument returns
> **no difference**. Five companies, same window, same disclosures, indistinguishable
> replacement economics — which is what a commodity industry looks like when you measure it.

**And [E3-61]'s limit on the row is recorded**: *"In some businesses, the participants behave
like a demented Kellogg. In other businesses, they don't … **I think you'd have to know the
people involved.**"* The row shows position. It cannot show conduct, and the 2Q26 negative Waha
gas price is what this industry's conduct looks like when every participant is individually
rational.

### THE COUNTER-CASE, STATED AT ITS FULL STRENGTH BEFORE THE VERDICT **[E4-51, E4-26]**

*[E4-51]: "I'm not entitled to have an opinion unless I can state the arguments against my
position better than the people who are in opposition." What follows is the bull case as its
holders would state it.*

*Occidental is not a generic price-taker. It holds roughly 2.8 million net acres in the Permian
Basin, the lowest-cost large oil resource in the world, and it has cut lease operating expense
15% in two years while integrating a $12bn acquisition. It owns something no other independent
has: **fifty years of CO₂ enhanced-oil-recovery expertise**, which is simultaneously a
low-decline production business and the technical foundation of a carbon-sequestration
franchise that a carbon-priced world would pay for. It has just executed the single best
balance-sheet transaction in its history — selling a cyclical chemicals division at the bottom
of the chemicals cycle for **37× its 2025 net income** to the most price-disciplined buyer in
American finance, and using every dollar to cut debt from $22.4bn to $13.7bn in six months.
Its international PSC barrels in Oman and the UAE are long-life, low-decline and partly
insulated from price. And it is 27% owned by the one investor whose entire method this
framework is built from.*

**And the answers, each from the filing:**

1. **The acreage is bought, not held.** Occidental's own three-year record shows **65% organic
   replacement**; the balance came from **$12.1bn of property acquisition in 2024**. The
   "irreplaceable" input is replaced annually, at auction, in cash.
2. **The CO₂ expertise is real and it has not yet been a business.** OLCV is inside the
   midstream segment, and that segment earned **$252M of pre-tax income in 2025** — after a
   **$487M of impairments**, including Occidental's **$401M share of NET Power's impairment
   losses, "bringing book value of its investment to zero"** (Note 7, verbatim). STRATOS is
   pre-revenue: the 10-K says the Company *"expects to begin sequestering CO₂ captured at
   STRATOS … in 2026"* — future tense, in a filing dated February 2026, for a plant that has
   consumed the majority of **$720M of 2025 midstream capital**. Worked in full at Q4.
3. **The OxyChem sale removed the only earnings stream not indexed to a screen price.** Its
   cash contribution ($926M of FY2025 OCF) is roughly offset by the interest saved (FY2025
   interest and debt expense $1,079M; **the filed Q2 2026 figure is $108M, an annualised
   $432M**, a saving of ~$647M/yr). **On cash flow it is close to a wash — and the business is
   now MORE concentrated in the commodity, not less.** The good news is the balance sheet; the
   structural news is that diversification was the price.
4. **The PSC barrels are 16% of production and they come with a sovereign counterparty.**
   International is 232 of 1,434 Mboe/d.
5. **Berkshire's ownership is a fact about the share register and is addressed at Q3, where
   the run states in writing why it may not be used as evidence here.**

### CLASS AND DIRECTION

- **Class: [x] NONE.** Not narrow — **none**. There is no product for which any customer believes
  there is no close substitute, because there is no product; there is a commodity quoted as a
  percentage of somebody else's index, and in the latest filed quarter that quote went **below
  zero** on 38% of the volume.
- **Direction [E4-32]: negative on every metric that is a claim about position**; positive on
  unit costs, which is an execution claim and which [E2-37] explicitly declines to promote.

- **VERDICT: [x] OUT.** Three independent, filed grounds, **any one of them sufficient**:
  1. **[E3-03] criterion 2 fails on the filer's own presentation.** A selling price expressed in
     the MD&A as *"104% of average WTI"* is the negation of "no close substitute."
  2. **[E2-58]'s equation, observed directly.** Persistent over-capacity without administered
     prices: **domestic realised natural gas of NEGATIVE $1.48/Mcf in the most recent filed
     quarter**, on 38% of volume, with no cost advantage that is *wide and sustainable* — and
     the competitor row below is what makes that a relative claim rather than an assertion.
  3. **[E4-04]'s excluded class, quantified.** The basis must be periodically replaced, and the
     filed three-year organic replacement rate is **65.1%** — Occidental does not even replace
     it, it buys the difference.

  **The MTDR/SD/MITSY precedent applies: Q2 OUT on the subject's own disclosure — entry is
  closed at any price [E5-35]:** *"You can turn any investment into a bad deal by paying too
  much. **What you can't do is turn any investment into a good deal by paying little.**"*
  **[E5-13]: most names should end here, and that is the system working.**

---
⛔ **Q3, Q4 and Q5 DO NOT OPEN FOR ENTRY.** Q1 IN · **Q2 OUT** — the hard sequence closes the
file for any BUY decision. No position exists, so no [E2-28] hold read is required.
**Everything below is FOR THE RECORD, per operator tasking (the (c) judgment; the preferred and
the Anadarko debt; CrownRock and leverage; OxyChem and the DAC ventures; the Berkshire-stake
bias statement; the named death; the price). Everything below sits under operator rule 3's
header and NOTHING below is entry language.**

---

## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. **Q2 OUT stands regardless —
Q3 can stop a run, it can never start one.***

### ⚠ THE BIAS DECLARATION THE OPERATOR REQUIRED, MADE IN WRITING BEFORE ANY EVIDENCE IS READ

**Berkshire Hathaway is Occidental's largest common holder, its sole preferred holder, the
holder of an 83.9M-share warrant, and — since 2026-01-02 — the buyer of its chemical division.
NONE OF THAT IS EVIDENCE ABOUT THIS BUSINESS, AND THIS RUN DOES NOT USE IT AS ANY.**

From the DEF 14A filed 2026-03-19, accession 0001628280-26-019816, verbatim:

> *"Warren E. Buffett and affiliated entities … **348,853,373 … 32.43%** … Warren E. Buffett and
> affiliated entities have shared voting power and shared investment power with regard to
> 348,853,373.38 securities (**264,941,431.00 common shares** and **83,911,942.38 shares
> underlying the Berkshire Warrants**)"*

and, from the same document's related-party section, verbatim:

> *"Occidental entered into a purchase and sale agreement with Berkshire Hathaway Inc.
> (Berkshire), **a greater than 5% beneficial owner of Occidental's common stock**, pursuant to
> which Berkshire agreed to acquire all of the issued and outstanding equity interests in
> OxyChem in an all‑cash transaction valued at approximately $9.7 billion"*

**Why this must be said out loud here.** Operator rule 9: *"the builder of a framework has an
incentive to validate it."* **This framework is constructed entirely out of Berkshire's own
corpus.** Every rule in it is a Buffett or Munger quotation with a ledger id. The temptation to
read "Buffett owns 27% of the common" as a clearance is therefore not a small bias in this run —
**it is the largest one available**, because the framework and the shareholder are the same
source. **[E4-26]** requires that disconfirming evidence be hunted hardest for the favourite
hypothesis, and **[E3-41]** states the reason: *"you must not fool yourself, and you're the
easiest person to fool."*

**The corpus itself forbids the inference, twice over:**
1. **[E5-36]:** *"We don't know how to buy stocks just by looking at financial figures … anything
   a computer could be functioned to do, in terms of screening — **I know I never do it.**"* A
   register entry is a datum on a screen, not an analysis.
2. **[E2-37]:** *"a good managerial record (measured by economic returns) is **far more a function
   of what business boat you get into** than it is of how effectively you row."* If the boat is
   the question, the identity of a passenger is not the answer.

And the corpus supplies the calibration in its own voice — **[E5-26]**: *"it's generally a
mistake to assume that rationality is going to be perfect, **even in very able people** … I
think hubris contributes to it."*

**And the decisive point is structural, not deferential.** Berkshire's Occidental position is
not a verdict it has published; it is a position taken **at prices and on terms available to
nobody else**: a $10bn preferred at an **8% coupon** with a **110%-of-face mandatory-redemption
premium**, plus an **83.9 million share warrant struck at $59.59**. **A common shareholder
buying at $60.95 is not buying what Berkshire bought.** That fact is quantified at Q4 as a claim
ahead of the equity, and it appears nowhere in this run as evidence of quality.

> **RECORDED: Berkshire's stake is used in this run as a FACT ABOUT THE REGISTER and as a
> CAPITAL-STRUCTURE CLAIM AHEAD OF THE COMMON. It is used nowhere as evidence of quality.**

### STEP 1 — THE WEIGHT CASE. *How much damage can this manager do before I can react?*

- [x] **Daily execution — HIGH [E3-38, E3-43, E2-70].** In a price-taker the only decisions that
  exist are where to drill, what to pay for acreage, how much debt to carry, and when to buy a
  competitor. There is no franchise absorbing the error. The 1991 original governs: *"franchises
  can tolerate mis-management … **a business, unlike a franchise, can be killed by poor
  management**."* Occidental is "a business" in that sentence's sense, and 2020 is the proof.
- [ ] Control — no. This would be a minority public-market position.
- [x] **Leverage — HIGH [E3-29].** Total debt and finance leases of **$13,743M** plus **$8,490M
  of face-value preferred** at 2026-06-30, against total equity of **$42,381M** of which
  **$8,287M is the preferred itself**. **Common equity $34,094M against $22,233M of debt and
  preferred claims ranking ahead of it.**

**Two of three ticked → Q3 IS A BINARY GATE AND NO PRICE COMPENSATES [E1-16, E3-29, E5-35].**
*Declared before the evidence, per the template.* This does not change the Q2 OUT; it records
that had Q2 passed, Q3 would have carried gate weight, not overlay weight.

### HONESTY — binary, permanent, filings-based **[E5-16]**

**No disqualifier found in the filings read.** Each matter dated to when it became **public**:
- **No restatement** in the FY2023–FY2025 filings read. The 2025 change in basis of presentation
  is an ASC 205 discontinued-operations reclassification, announced in advance, applied
  retrospectively, with the reason stated in Note 1 — a required accounting change, not a
  restatement.
- **Related-party conduct:** the $9.7bn OxyChem sale to a >5% holder **was disclosed as a
  related-party transaction in the proxy** and run through the related-party policy.
  **Disclosing the conflict is the behaviour [E2-26] asks for**, and it is recorded as such
  rather than as a flag.
- **Environmental and legal:** 152 remediation sites, **$1,870M accrued**, of which **$1,674M
  relates to the retained OxyChem legacy** — Occidental **sold the business and kept the
  liability**, and said so in Note 4 and Note 11 with the accrual quantified. That is disclosure
  working, and it is a Q4 obligation.

**Per [E5-17], written the way the corpus requires: this is the ABSENCE OF FOUND DISQUALIFIERS,
not a finding that the managers are honest.** *"Sincerity and empathy can easily be faked."*

### STEP 2 — THE FLAGS. *Each is a prompt to READ, never a verdict [E4-22, E5-36, E5-38].*

- [ ] **Weak accounting — NOT FIRED.** Stock compensation is expensed — **$234M, $213M and $203M**
  in 2025, 2024 and 2023 (Note 14). Depletion is charged at **$13.60/Boe against a three-year
  replacement-cost range of $10.29–$18.28/Boe**, i.e. **inside the range and within 5% of its
  $14.29 midpoint**. On the SandRidge test (depletion charged at half of replacement cost) this
  **passes**, and it is recorded in Occidental's favour.
- [ ] **Unintelligible footnotes — NOT FIRED.** The preferred terms, both warrant strikes and
  counts, the reserve rollforwards by product and geography, the costs-incurred table, the price
  sensitivities and the environmental accrual are all stated plainly and are computable. **Every
  number in this run was built from those footnotes; that is the test passing.**
- [x] **EBITDA / adjusted-earnings promotion — FIRED, AND IT IS THE LOUDEST ITEM AT Q3
  [E4-29].** The Q2 2026 earnings release (accession 0001628280-26-053377) leads with **five**
  non-GAAP measures and names them itself: *"adjusted income - continuing operations, operating
  cash flow before working capital - continuing operations, capital expenditures, net of
  noncontrolling interest - continuing operations, **free cash flow before working capital -
  continuing operations** and adjusted general and administrative (G&A), other operating and
  non-operating expenses."*
  **The construction that matters is "free cash flow BEFORE WORKING CAPITAL."**
  **[E2-23] constraint 3 requires the working-capital increment to be INCLUDED in (c)**; this
  measure deletes it by definition. The deletion is not trivial: **FY2025 operating cash flow
  before working capital was $10,673M against $9,606M as reported — a $1,067M difference, 11% of
  the real number** — driven by a **$964M decrease in accounts payable and accrued liabilities**
  and a **$305M swing in current income taxes**. The mechanism is [E5-41]'s *"reverse float"* in
  a different costume: cash already gone, deleted from the headline.
  **AND IT IS PAID ON.** DEF 14A, verbatim: *"the Compensation Committee approved metrics related
  to the company's total spend per barrel and **free cash flow before working capital**"* — 40%
  of the 2025 annual cash incentive, *"Result as of 12/31/2025 **$4.28B**"* against a target band
  of *"$3.8B to $4.1B"*, contributing to a payout at **125% of target**. **The executives were
  paid on a cash-flow measure that excludes a billion dollars of cash that actually left the
  company.**
- [x] **Metric-switching — FIRED [E2-49].** *"Yardsticks seldom are discarded while yielding
  favorable readings. But when results deteriorate, most managers favor **disposition of the
  yardstick rather than disposition of the manager**."* DEF 14A, verbatim: *"**Determined to use
  free cash flow before working capital as a performance metric for the 2025 ACI award in place
  of CROCE**."* CROCE is **cash return on capital employed** — a return-on-capital metric, which
  is [E3-46]'s own second question about a business. It was replaced, for the annual cash bonus,
  by a cash-flow metric, in a period when the return on the CrownRock capital was falling
  (unleveraged pre-tax return on capital employed **~10.4% → ~8.0% → ~6.5%**, computed below).
  **The candor reading is stated at its full strength**: the proxy attributes the change to
  shareholder feedback (*"Evaluate use of CROCE as a metric for both the ACI and LTI awards"*),
  the concern was double-counting one metric across two plans, **CROCE was retained in the
  long-term PSUs**, and the committee simultaneously began *disclosing threshold and maximum
  goals* — a move toward candor, not away from it. **Both readings are on the record and the run
  does not resolve it.** What is not in doubt is the direction of the swap: away from a
  return-on-capital yardstick, at a company whose return on capital was falling.
- [ ] **Trumpeted earnings projections — NOT FIRED, and the guidance record is GOOD [E3-48].**
  Occidental publishes quarterly operational guidance and beats it on the record read: Q2 2026
  production of **1,433 Mboed *"exceeding the high end of guidance"*** and midstream results that
  ***"exceeded the high end of guidance"*** — the filer's own words, checkable against the prior
  quarter's published range. The 2025 ACI *"Total Spend per Barrel"* outturn was **$28.21 against
  a $29.00 target**. **[E3-48] says beaten guidance earns weight, and it is recorded in
  Occidental's favour.** No long-run EPS-growth target is published.
- [x] **Serial share issuance — FIRED, and the arithmetic is large [E5-15].** Shares outstanding:
  **938,457,983 (2024-12-31) → 986,026,416 (2025-12-31) → 999,708,551 (2026-06-30)** — **+6.5% in
  eighteen months.** Cash proceeds **$966M in 2025** and **$295M in H1 2026** (cash-flow
  statements). Most is contractual warrant exercise — **but the March 2025 event was solicited,
  and the 10-Q says so verbatim**:
  > *"On March 3, 2025, Occidental announced an offer to holders of its Common Stock Warrants to
  > exercise their warrants, each exercisable at $22.00, **at a temporarily reduced price of
  > $21.30 per share** with an expiration date of March 31, 2025. In April 2025, Occidental
  > issued **41.9 million shares** of stock in return for proceeds of approximately **$890
  > million**. The incremental fair value associated with the Common Stock Warrants related to
  > the change in exercise price was recognized as an equity issuance cost."*

  **Occidental paid holders 70 cents a share to pull forward the issuance of 41.9 million shares
  at $21.30**, and the disclosed use of proceeds was *"to repay near-term debt maturities."*
  [E5-15] calls serial issuance *"one of the surest indicators of a promotion-minded management,
  weak accounting, a stock that is overpriced and — all too often — outright dishonesty."*
  **The flag fires and is then read down, hard, per [E5-38]:** the warrants expire in August 2027
  and were going to be exercised, the inducement cost 3.2% of the strike, and the money went to
  debt. **It is not a venality finding. It is a company choosing dilution over leverage,
  disclosed in the filing, and it is recorded as exactly that.**
- [ ] **Filed-figure fraud tells — NOT FIRED [E4-30].** Reported results are the opposite of
  *"unnaturally smooth"*: continuing-operations pre-tax income **$4,662M → $4,024M → $3,128M**,
  and quarterly net income to common in 2025 of **$766M · $288M · $661M · $(68)M**. **Cash taxes
  are not falling as a share of pretax income**: total current tax expense **$1,276M · $1,423M ·
  $894M** against continuing pre-tax income of **$4,662M · $4,024M · $3,128M** = **27.4% · 35.4%
  · 28.6%**. The tell looks for a falling series; this one does not fall.
- [ ] **Dividends funded by issuance — NOT FIRED as stated, but recorded [E2-52].** In 2025
  Occidental paid **$1,594M of common and preferred dividends** and received **$966M from share
  issuance**. Dividends are covered several times over by $9,606M of operating cash flow, so the
  literal test does not fire. **The coincidence is on the record and is stated.**
- [x] **[E2-60]'s third dimension — RECORDED, and RECORDED AS CORRECTED.** *Restricted earnings*
  are those whose payout costs the business *"its ability to maintain … **its financial
  strength**."* From 2019 to 2023 Occidental distributed while carrying the largest debt load in
  its history, and the 2020 cut is what the correction looked like. **In 2026 the direction is
  emphatically the opposite**: $8.6bn of debt retired in six months. The flag is recorded as
  **historically fired and currently corrected**, not as absent.

### STEP 3 — THE PRIMARY TEST **[E2-01]**, scoped as its sources scope it **[E2-47, E2-43, E2-73]**

> *"The primary test of managerial economic performance is the achievement of a **high earnings
> rate on equity capital employed** (without undue leverage, accounting gimmickry, etc.) **and
> not the achievement of consistent gains in earnings per share.**"*

**[E2-47] carves out unusual debt-equity ratios; [E2-43] requires unleveraged net tangible
assets for acquisitive filers. Occidental is both**, so the series is run on the denominator
[E2-43] names, with leverage stated beside it rather than hidden inside it.

| $M unless stated | 2023 | 2024 | 2025 |
|---|---|---|---|
| Income from continuing operations before income taxes | 4,662 | 4,024 | **3,128** |
| add back: interest and debt expense, net | 957 | 1,169 | 1,079 |
| **Unleveraged pre-tax return, continuing operations** | **5,619** | **5,193** | **4,207** |
| Approximate capital employed (total equity + total debt) | ~54,000 | ~65,000 | ~65,000 |
| **UNLEVERAGED PRE-TAX RETURN ON CAPITAL EMPLOYED** | **~10.4%** | **~8.0%** | **~6.5%** |
| Net income attributable to **common** stockholders | 3,773 | 2,377 | **1,647** |
| *of which taken by the preferred before the common sees it* | *923* | *679* | ***679*** |

**THE SERIES FALLS BY ROUGHLY A THIRD IN TWO YEARS, ACROSS EXACTLY THE PERIOD IN WHICH $12.1bn
OF CROWNROCK CAPITAL WAS ADDED.** [E2-73] is the right lens — *"the managers of the units should
be judged by the returns they achieve on the underlying assets; **what we pay for a business does
not affect the amount of capital its manager has to work with**"* — and it points the same way:
production rose 17% between 2023 and 2025 while unleveraged pre-tax return on capital employed
fell from ~10.4% to ~6.5%.

**And [E3-59]'s "hand they were dealt" must be adjusted for, and it is most of the fall.**
Realised oil went from $76.85 to $64.60/Bbl over the same window; on the filer's own
$240M-per-dollar sensitivity that is roughly **$2.9bn a year of pre-tax cash, none of it
management's doing.** **Adjusted for the hand, the OPERATING record is respectable and the
CAPITAL-ALLOCATION record is the open question.** That is the honest split, and it is stated
before the imperative scoring below rather than after it.

### THE HALF-OWNER TEST **[E2-26]**

*Does this reporting tell me what I would want to know if the positions were reversed?*
**Substantially yes, and better than most filers in this sector.** It gave me the reserve
rollforward by product and geography for three years; the costs-incurred table; the price
sensitivities in dollars; the preferred terms **including the redemption trigger**; both warrant
strikes and counts; the retained environmental liability quantified; the OxyChem gain and the
related-party disclosure; and a segment reconciliation that shows **the preferred dividend on
its own line**. **The one place it fails is the headline**, where the first number handed to the
reader — *free cash flow before working capital* — is the one that deletes a billion dollars of
real cash outflow. **Nobody in the reversed position wants the number that ignores the
payables.**

### THE INSTITUTIONAL IMPERATIVE — score all four **[E2-30]**

*Not a fraud test: "institutional dynamics, not venality or stupidity."*

- [ ] **Resists any change in current direction — NOT SCORED.** The opposite. Occidental sold its
  chemical division, changed CEO, and cut debt 39% in six months.
- [x] **Projects/acquisitions materialise to soak up available funds — SCORED, and it is the
  central fact of the last seven years.** **Anadarko in 2019 and CrownRock in 2024**, executed
  near two different cycle peaks, funded with an 8% preferred, the bond market, and — in 2019 —
  a bidding contest against Chevron.
- [ ] **Staff studies produced to justify the leader's craving — NOT OBSERVABLE from the filings
  read.** Recorded as unobservable rather than as absent, per the **absence-claim rule**.
- [x] **Peer behaviour mindlessly imitated — SCORED, with a date and a number.** The 2023–24 US
  shale consolidation wave is visible in the peers' own costs-incurred tables built for the
  competitor row above: **costs incurred in 2024 of $40,029M (FANG), $35,984M (COP) and $17,957M
  (OXY)**, against $5,745M, $12,364M and $5,936M in the years either side. **Five large filers
  bought at once, at the same point in the cycle.** That is [E2-27]'s collective irrationality
  and [E2-30]'s fourth behaviour observable in one table.

### CAPITAL ALLOCATION — the buyback conditions **[E5-08, E4-31, E5-24, E5-31]**

- **(1) Ample funds for operations and liquidity? — YES, now.** $4,188M of cash, an undrawn
  $4,150M revolver to 2028-06-30, and near-term maturities after the OxyChem repayments of
  **$24M in 2026, $48M in 2027, $14M in 2028** (10-K, verbatim).
- **(2) Repurchases at a material discount to conservatively calculated IV? — CANNOT BE SCORED
  AS COMPLIANT, and the reason is structural rather than motivational.** FY2025 10-K, verbatim:
  *"The value remaining in the Company's share repurchase program as of December 31, 2025 was
  $1.2 billion. **There were no share repurchases under the Company's share repurchase program
  in 2025.**"* H1 2026 shows **$117M** of treasury purchases. **Occidental bought back
  essentially nothing in 2025 while issuing 47.6 million shares.**
  **[E2-51]** — *"A manager who consistently turns his back on repurchases, when these clearly
  are in the interests of owners, **reveals more than he knows of his motivations**"* — **is
  quoted and then set aside, because the constraint is disclosed and it is contractual.** The
  preferred's mandatory-redemption trigger makes buying stock expensive: every dollar returned
  to common **above $4.00 per share on a trailing twelve months** forces a preferred redemption
  at **110% of face**. At the current $1.12 distribution the headroom is **$2.88 per share, about
  $2,879M a year** of combined buybacks and extra dividends; beyond that a dollar returned to
  common costs **$2.10**. **This is a capital-allocation constraint imposed by a 2019 financing
  decision, and it is a Q4 fact, not a Q3 character finding.**
- **THE HUMILITY CLAUSE, applied [E4-13]:** *"it is natural for CEOs to be optimistic about their
  own businesses. **They also know a whole lot more about them than I do.**"* This scoring rests
  on this run's own value range, which is wide. It **binds position size, never the discount
  rate** — and no position exists.
- **[E5-31]'s real test — per-share value added at the price — and it is genuinely mixed.**
  *Against:* two acquisitions at cycle tops; a share count up 6.5% in eighteen months; and
  **[E5-44]**'s rule — *"The intrinsic value of the shares you give in an acquisition must not be
  greater than the intrinsic value of the business you receive"* — applied to the Occidental
  shares issued for Anadarko in 2019, which the 2020 collapse then repriced.
  *For:* **the OxyChem sale, which is the strongest single allocation decision in the filed
  record** — a cyclical chemicals division sold for **$9.7bn cash against $5,324M of net book
  assets and $262M of FY2025 net income**, with **every dollar applied to debt**. The run states
  the honest caveat on its own favourable point: $9.7bn is 37× the 2025 earnings **and 7.1× the
  2023 earnings of $1,364M**, so the flattering multiple is partly a cyclical trough in
  chemicals — but the price was cash, it was certain, and it removed $8.6bn of debt.
- **The company's own five-year total-return table, FY2025 10-K, reproduced because it is the
  filer's own scoreboard and it is not flattering:** Occidental **$252** against its stated peer
  group **$268** and the S&P 500 **$196**, on $100 invested at 2020-12-31. **Measured from the
  bottom of its own collapse, Occidental has trailed its own chosen peer group over five years.**

### THE GUARDRAIL — checked before the verdict is written

- [x] **Confirmed: nothing in this Q3 is used to PROMOTE the name.** The genuinely good items —
  beaten guidance, LOE per barrel down 15% in two years, a well-priced divestiture, a transformed
  balance sheet — are **operating and allocation quality inside a business the corpus classifies
  as a non-franchise**, and [E2-37] fixes what they can be worth: *"a textile company that
  allocates capital brilliantly within its industry is a remarkable textile company — **but not a
  remarkable business**."*
- [x] **Key-person dependence is recorded at Q2 as a moat defect [E4-23]**, not here as a
  compliment. The 2026-06-01 CEO transition is filed there.
- [x] **Is the franchise intact and the damage excisable, or is the manager the plan
  [E2-35, E2-36]? NEITHER.** There is no franchise for the excisable-cancer exception to attach
  to. Richard Jackson may prove an excellent operator; the corpus's answer to that is
  **[E3-39]**: *"averaged out, **betting on the quality of a business is better than betting on
  the quality of management**."*

- **VERDICT: [x] IN — meaning NO DISQUALIFIER FOUND, which is all this verdict has ever meant
  [E5-17]. It promotes nothing, and Q2's OUT stands.**
  *Three flags fired and are recorded: the adjusted-cash-flow measure that deletes working
  capital and is paid on; the metric switch away from return on capital; and the solicited
  warrant exercise. None is an integrity finding under [E5-16]. Per [E5-38] the flag reads the
  accounting; the binary judges the person; and the two stay distinct.*
  *[E4-52] checked: do the fired flags CONVERGE into a lollapalooza? **No.** They point in
  different directions — one deletes a cash outflow from a bonus metric, one swaps a yardstick,
  one issues stock to cut debt. A reinforcing system aimed at one outcome is not what this looks
  like.*

---

## Q4 — FOR THE RECORD: WILL IT SURVIVE?
### **COMPUTATION — NOT A CLEARANCE** (operator rule 3)
*Q2 returned OUT. Nothing in this section is entry language.*

### Owner earnings — the one number **[E2-23]**

> *"(a) reported earnings plus (b) depreciation, depletion, amortization … less **(c) the average
> annual amount of capitalized expenditures for plant and equipment, etc. that the business
> requires to fully maintain its long-term competitive position and its unit volume.** (If the
> business requires additional working capital to maintain its competitive position and unit
> volume, **the increment also should be included in (c)**.)" … "**(c) must be a guess.**"*

**THE BASE. Continuing operations only — because OxyChem is gone.** The FY2025 10-K restates all
three years for the discontinued operation, so the series below is like-for-like with the
business that exists today:

| $M | 2023 | 2024 | 2025 | 3-yr mean |
|---|---|---|---|---|
| Operating cash flow, **continuing operations** | 10,235 | 10,519 | **9,606** | **10,120** |
| less stock-based compensation, **as filed** (Note 14) | 203 | 213 | 234 | 217 |
| **= base, before (c)** | 10,032 | 10,306 | **9,372** | **9,903** |
| *memo: operating cash flow from discontinued ops (OxyChem), excluded* | *2,073* | *920* | *926* | *— * |

**Working capital is netted through operating cash flow from one audited line**, per the
framework's CONVENTION and [E2-23] constraint 3. **It matters here and the run keeps it in**:
FY2025 operating cash flow before working capital was **$10,673M** against **$9,606M** reported —
a **$1,067M** drag, of which **$964M** was the decrease in accounts payable and accrued
liabilities. **That $1,067M is exactly what the company's headline measure deletes**, and the
run refuses the deletion.

**Equity-method look-through [E3-04] — checked and NOT added.** Occidental holds 40.9% of WES and
40.3% of NET Power. Note 7 discloses **dividends received from equity investments of $705M,
$682M and $571M**, against a **$619M add-back for undistributed LOSSES** in the FY2025 cash-flow
statement and a **$401M share of NET Power's impairment "bringing book value of its investment
to zero."* **Distributions exceeded the investees' earnings, so [E3-04]'s adjustment is negative
and is not taken. Nothing is added.**

### **(c) — THE DISCLOSED JUDGMENT. This is the hard part, and the operator's prior is TESTED, not assumed.**

**The operator's brief: "capex/D&A of 0.77× is suspicious for a depleting asset … If (c) is set
below the level that holds production flat, the owner earnings are partly liquidation
proceeds."** Both halves are tested below. **The first is corrected on the filed record; the
second survives, but through a different channel than the one named.**

**FIRST CORRECTION: the ratio is not 0.77×.** FY2025 capital expenditures as spent were
**$6,427M** (consolidated statement of cash flows) against consolidated D&A of **$7,533M** and
oil-and-gas-segment DD&A of **$7,115M**. **6,427 ÷ 7,533 = 0.85×; 6,427 ÷ 7,115 = 0.90×.** The
screen's 0.77× is not reproducible from the filed statements.

**THE ANCHORS, ASCENDING. Every one of them is filing-sourced.**

| $M/yr at FY2025 volume (523.2 MMBoe · 1,434 Mboe/d) | what it is | source |
|---|---|---|
| **5,500 – 5,900** | **the company's own 2026 capital plan** | FY2025 10-K MD&A, verbatim: *"The Company's planned 2026 capital expenditures are between $5.5 billion and $5.9 billion."* |
| **6,286** | H1-2026 capex annualised ($3,143M × 2) | Q2 2026 10-Q cash-flow statement |
| **6,427** | FY2025 capex as spent | FY2025 10-K cash-flow statement |
| **7,474** | **replace 100% of production at the MIDPOINT of the 3-yr F&D range ($14.29/Boe)** | costs-incurred + reserve rollforward, computed in the competitor row |
| **7,533** | **consolidated D&A — the corpus DEFAULT [E3-44, E2-41]** | FY2025 income statement; $14.40/Boe |
| **8,026** | replace 100% of production at the 2025 **drill-bit-only** F&D of $15.34/Boe | same tables |
| **9,565 – 9,884** | replace 100% at the 3-yr **drill-bit-only** ($18.28/Boe) or **all-in excluding revisions** ($18.89/Boe) | same tables |

**THE VOLUME TEST, AND IT IS DECISIVE ON THE FIRST HALF OF THE OPERATOR'S PRIOR.**
Maintenance capex is *"what the business requires to fully maintain … its unit volume."* The
filed answer is unusually clean here, because 2026 is a flat-production year and half of it has
been reported:

| | FY2025 | 1Q26 | **2Q26** | H1-2026 |
|---|---|---|---|---|
| Worldwide production, Mboe/d | **1,434** | 1,426 | **1,433** | **1,429** |
| Capital expenditures, $M | 6,427 | ~1,554 | ~1,589 | **3,143** |

**Production is flat — 1,429 Mboe/d in H1 2026 against 1,434 in FY2025 — on an annualised spend
of $6,286M, and the company's own plan for the year is $5.5–5.9bn.** So **the level that holds
unit volume flat is roughly $5.7–6.3bn, and it sits BELOW D&A of $7,533M, not above it.**

> **THE OPERATOR'S "SUSPICIOUS FOR A DEPLETING ASSET" PRIOR IS NOT SUPPORTED ON THE VOLUME
> TEST, AND THE RUN SAYS SO RATHER THAN CONFIRMING WHAT IT WAS SENT TO CONFIRM.** capex below
> D&A at Occidental is **not** evidence of volume liquidation. It is evidence that the depletion
> charge, computed on a reserve base bought partly at 2019 and 2024 acquisition prices, exceeds
> the marginal cash cost of holding today's production. **This is the same direction the MTDR
> run found at Matador, and the opposite of the SandRidge finding.** [E5-20]'s railroad exception
> — *"merely spending their depreciation expense will not keep them in the same place"* — **does
> NOT bite at Occidental on unit volume.**

**THE RESERVE TEST, AND IT IS WHERE THE OPERATOR'S SECOND HALF SURVIVES.**
[E2-23] requires (c) to maintain *"its long-term competitive position"* **as well as** unit
volume. Holding this year's barrels is not the same as holding the resource that produces next
decade's:

- **Three-year organic (drill-bit) reserve replacement: 65.1%.** Occidental replaces
  approximately two-thirds of its production with the drill bit and closes the rest with
  revisions and with purchases — **$12.1bn of property acquisition cost in 2024 alone.**
- **Total proved reserve life fell 9.49 → 8.80 years in 2025**, the first full year of CrownRock.
- **The booked drilling inventory is 2.50 years deep**: proved undeveloped reserves of 1,309
  MMBoe against 523.2 MMBoe of annual production.
- **And the honest counter, stated because [E4-26] requires it:** on the metric that is robust
  to booking convention — all organic sources including revisions — Occidental replaced
  **115.8%** of production over three years at **$10.29/Boe**, which is **mid-pack against DVN
  ($9.21), EOG ($9.80), FANG ($13.42) and COP ($15.91)** and is **BELOW its own depletion charge
  of $13.60/Boe.** On that construction the accounting is conservative, not aggressive.

**RECONCILING THE TWO. The true replacement cost sits between the two constructions, and the
filing lets us say why.** The drill-bit-only number ($18.28/Boe) **overstates**, because
development spending includes PUD conversion, which consumes capital and adds no new reserves.
The all-sources number ($10.29/Boe) **understates**, because a material share of the revisions is
free — the FY2025 note attributes **+73 MMbbl of oil revisions to *"changes in economic
conditions"* and +61 MMbbl to *"the Oman contract extension"***, against only **+53 MMbbl** from
*"infill development projects"* that were actually drilled. **Midpoint: $14.29/Boe, which at
523.2 MMBoe is $7,474M a year — within $59M of the consolidated D&A charge of $7,533M.**

> **THE JUDGMENT, DISCLOSED AS A GUESS PER [E2-23] CONSTRAINT 4: (c) = $7,500M.**
>
> It is the corpus's own default **[E3-44, E2-41]** — *"the depreciation charge is not
> inappropriate in most companies to use as a proxy for required capital expenditures"* — and at
> Occidental the default is not merely permitted, it is **independently corroborated**: the
> midpoint replacement cost computed from the supplemental tables lands within 1% of it. It sits
> **above** the $5.7–6.3bn that holds unit volume and **below** the $8.0–9.9bn that would hold the
> reserve base by the drill bit alone. **Band displayed: $5,700M to $8,026M** — as a display of
> the guess, per [E5-20], **never as equally legitimate answers.**

> **AND THE OPERATOR'S DEMANDED STATEMENT, MADE PLAINLY: AT ANY (c) BELOW ROUGHLY $8.0bn, PART
> OF WHAT THIS RUN CALLS OWNER EARNINGS IS INVENTORY DRAWDOWN, NOT INCOME.** Occidental holds
> its barrels flat while replacing 65% of them by the drill bit. The gap is closed by revisions
> that can reverse and by acquisitions that must be paid for. **At (c) = $7,500M the drawdown is
> small; at (c) = $5,700M — the number the company's own capital plan implies and the number a
> free-cash-flow screen would use — roughly $2.3bn a year of the reported "free cash flow" is
> the sale of a wasting asset, and the filed evidence for it is a total proved reserve life that
> went from 9.49 years to 8.80 in a single year.**

### THE WINDOWS, AND THE SPREAD IS PART OF THE RANGE **[E4-25, E4-38, E2-42]**

The corpus default is five years **[E2-42]**. **A five-year window cannot be run honestly on this
filer** and the reason is stated rather than worked around: FY2021 and FY2022 belong to a company
with a chemical division, a different production base, and a WTI price 46% above the FY2025
level. **[E4-38]**'s remedy is to publish every window; the two that describe the business that
exists are below.

| owner earnings TO THE COMMON, $M (after (c) and after $679M of preferred dividends) | (c)=5,700 | (c)=6,427 | **(c)=7,500** | (c)=8,026 |
|---|---|---|---|---|
| **Window A — 3-yr mean, continuing ops (base $9,903M)** | 3,524 | 2,797 | **1,724** | 1,198 |
| *yield on the $60,928M cap* | *5.78%* | *4.59%* | ***2.83%*** | *1.97%* |
| **Window B — FY2025 alone, continuing ops (base $9,372M)** | 2,993 | 2,266 | **1,193** | 667 |
| *yield on the $60,928M cap* | *4.91%* | *3.72%* | ***1.96%*** | *1.09%* |

- **Combined range (window spread × capex band), to the common: $667M to $3,524M — a yield of
  1.09% to 5.78% on the $60,928M cap.** The conservative end is **40%** of the optimistic end.
- **Is that range too wide to reach a conclusion [E4-25]?** **No — and that is itself the
  finding.** *Every single cell in the grid is below the 5.25% sovereign except one, and every
  cell is far below the [E4-28] 10% floor.* The width does not straddle the answer; it lies
  entirely on one side of it. **[E4-25]'s "no useful conclusion" outcome does not apply when the
  whole range agrees.**
- **A wide spread is also a Q4 finding in its own right [E5-11].** The distorted years are named:
  **2021–22 (price spike), 2019 (Anadarko close), 2024 (CrownRock close), 2025–26 (OxyChem
  disposal).** Four structural distortions in nine years is what this business looks like.

### **[E4-41] — NORMALISE THE MEAN DOWN FOR LUCK.** *Stated as a sensitivity, so windage is spent once.*

The corpus's only pro-forma that ever disclosed earnings *too high* is Berkshire's own. Applied
here: **the FY2023–25 window's mean WTI was $72.72 against a nine-year mean of $65.84 — the
window sits $6.88 a barrel ABOVE the long-run average.** On the filer's own sensitivity that is
**$1,650M a year of pre-tax cash, or about $1,205M after tax at the FY2025 cash-tax rate.**

**Applied to the (c)=$7,500M line it would move owner earnings to the common from $1,724M
(2.83%) to $520M (0.85%).** **THIS IS A SENSITIVITY, NOT A SUBTRACTION** — it is not carried into
the reported band, because conservatism is spent once **[E4-11, E4-48]** and this run spends it
at the (c) judgment. But it is real, it is directional, and no honest reading of the file omits
it.

### THE PREFERRED — the operator's tasking, quantified **[E2-23], [E5-11] strength 3**

**This is the capital-structure claim the screen's market cap does not see.** FY2025 10-K Note 13,
verbatim:

> *"In 2019, Occidental issued 100,000 shares of Occidental series A preferred stock, with a face
> value of $100,000 per share and a liquidation preference of $105,000 per share plus unpaid
> accrued dividends to Berkshire Hathaway. Prior to August 2029, **a mandatory redemption
> provision obligates Occidental to redeem preferred stock at a 10% premium to face value on a
> dollar-for-dollar basis for every dollar distributed to common shareholders (either via common
> stock dividends or share repurchases) above $4.00 per share, on a trailing 12-month basis.**
> … **Occidental cannot voluntarily redeem preferred stock before August 2029.** After August
> 2029, Occidental can voluntarily redeem preferred stock at a 5% premium to face value.
> **Dividends on the preferred stock accrue on the face value at a rate per annum of 8%**, but
> will be paid only when, as and if declared by the Company's Board of Directors. At any time,
> when such dividends have not been paid in full, the unpaid amounts will accrue dividends,
> **compounded quarterly, at a rate per annum of 9%.** Following the payment in full of any
> accrued but unpaid dividends, the dividend rate will remain at 9% per annum. **If preferred
> dividends are not paid in full, Occidental is prohibited from paying dividends on common
> stock.** Occidental paid **$679 million** in preferred stock dividends in 2025. … As of the date
> of this filing, approximately **$8.5 billion face value of the preferred stock remains
> outstanding.**"*

**WHAT IT COSTS THE COMMON, IN NUMBERS:**

| | |
|---|---|
| Preferred outstanding, 2026-06-30 | **84,897 shares × $100,000 = $8,490M face**; carried at **$8,287M** |
| **Annual coupon ahead of the common** | **8% × $8,490M = $679M** — cross-checks to the filed $679M paid in 2025 and to the $170M/quarter in the Q2 release |
| Liquidation preference | $105,000/share = **$8,914M** |
| **Cost to retire it before Aug-2029** | **110% of face = $9,339M**, and only via the distribution trigger |
| **Share of the run's owner earnings taken by it** | at (c)=$7,500M and the 3-yr window: **$679M of $2,403M = 28.3%** |
| **Effect on the common's yield** | **2.83% instead of 3.94%** — the preferred takes **111 basis points** off the yield on the quoted cap |
| Rate if ever unpaid | **9% per annum, compounded quarterly**, and **common dividends are blocked** until cured |

**AND THE SECOND, LESS VISIBLE COST: IT CAPS THE CAPITAL RETURN.** Every dollar returned to
common above **$4.00 per share trailing-twelve-months** forces a preferred redemption at **110%
of face**, so beyond that threshold **a dollar to the common costs $2.10**. At the current $1.12
declared rate the headroom is **$2.88 per share ≈ $2,879M a year**. **This is why there were no
open-market buybacks in 2025 despite $1.2bn of authorisation remaining**, and it is a contractual
constraint, not a management preference.

**AND THE WARRANT.** Note 13, verbatim: *"As of December 31, 2025, the Berkshire Warrant would
result in the issuance of **83.9 million shares** of Occidental common stock, if exercised in full
for its current strike price of **$59.59 per share**."* Plus **17.9 million Common Stock Warrants
at $22.00** at 2026-06-30. **101.8 million shares, 10.2% of the count, and the larger tranche is
in the money at the 2026-09-01 close of $60.95.** Every value below is therefore reported on the
**fully diluted 1,101,437,371 shares.**

> **THE OPERATOR'S POINT IS CORRECT AND HERE IS ITS SIZE: between the operating business and the
> common holder sit $8,490M of face-value preferred taking $679M a year, a $9,339M redemption
> obligation that cannot be voluntarily discharged before August 2029, a contractual cap on
> capital returns above $4.00 per share, and 101.8 million warrant shares. The screen priced
> 999.6 million common shares at $60.95 and saw none of it.**

### THE ANADARKO DEBT AND THE CROWNROCK DEBT — the operator's tasking, from the filings

**ANADARKO, closed 2019-08-08.** FY2019 10-K, accession 0000797468-20-000004, Note 3, verbatim
consideration table and allocation:

| $M | |
|---|---|
| Cash to Anadarko stockholders ($59.00 × 491.6M shares) | **29,002** |
| Occidental stock issued (**144 million shares at $46.31**) | 6,679 |
| Anadarko stock-based awards | 23 |
| **TOTAL ACQUISITION CONSIDERATION** | **35,704** |
| **PLUS: Anadarko long-term debt assumed** | **13,240** |
| **PLUS: WES long-term debt assumed** | **7,407** |

Funded, in Occidental's own words (FY2019 10-K, Note 3, verbatim):

> *"In connection with the Acquisition, Occidental issued **$13.0 billion of new senior unsecured
> notes, $8.8 billion of term loans** (the Term Loans) and **100,000 shares of series A preferred
> stock** (the Preferred Stock) **with a warrant to purchase 80 million shares of Occidental
> common stock at an exercise price of $62.50** (the Warrant) **for $10 billion.**"*

**WHAT IT DID TO THE BALANCE SHEET, from the filed balance sheets:**

| | total debt, $M |
|---|---|
| **2018-12-31** (before) | **10,317** |
| **2019-09-30** (first quarter-end after the close) | **47,614** consolidated · **39,977** excluding WES's own separate capital structure |
| 2019-12-31 | 38,588 |
| 2020-12-31 | 36,185 |
| 2021-12-31 | 29,617 |
| **2026-06-30** (today) | **13,743** including finance leases |

**Total debt went from $10.3bn to about $40bn — excluding WES's own $7.6bn — inside eight
weeks, and it took seven years to work off.** Goodwill of **$5.8bn** was recorded and **all of
it was gone within eight months**: $4.6bn derecognised on the 2019-12-31 WES deconsolidation and
*"the remaining $1.2 billion in goodwill was fully impaired in the first quarter of 2020"*
(FY2020 10-K, verbatim).

**CROWNROCK, closed August 2024.** From the FY2025 10-K's own tables rather than from the deal
announcement: FY2024 **property acquisition costs of $8,971M proved plus $3,178M unproved =
$12,149M**, against **$9,117M** of *"Purchases of assets, businesses and equity investments,
net"* in the FY2024 investing cash flow, buying **623.3 MMBoe of reserves in place** — 128% of
that year's entire production. **Two acquisitions, five years apart, each near a cycle peak,
each of which the company then spent years deleveraging out of.** That is [E2-30] behaviour (2)
and it is the central fact of Q3's allocation record.

### THE 2026 DELEVERAGING — stated at full strength, because it is real

Q2 2026 10-Q, Note 6, verbatim: *"In the six months ended June 30, 2026, the Company utilized
after-tax proceeds from the OxyChem Transaction and excess free cash flow to **repay debt of
$8.6 billion**, which resulted in a loss on extinguishment of $190 million."* Borrowings at face
value fell **$20,427M → $11,818M** in six months, across **28 separate note and debenture
series**. The Q2 release: *"Reduced principal debt by $1.9 billion to $11.8 billion, advancing
toward the **$10.0 billion milestone**."*

**Near-term maturities after those repayments (FY2025 10-K, verbatim): "$24 million is due in
2026, $48 million in 2027, $14 million in 2028, $367 million in 2029 and $14.6 billion due in
2030 and thereafter."** **That is the single most favourable fact in this file** and it is
recorded before anything is said against it.

**And the term on which some of it was bought is recorded too [E3-52].** 8-K filed 2026-03-09,
accession 0000950157-26-000265, verbatim: the Fifth Supplemental Indenture *"among other things,
**eliminates certain of the covenants** contained in the 2019 Indenture with respect to the
6.125% 2031 Notes."* Occidental paid tendering holders for consent to strip covenants from the
notes it did not retire. Legal, disclosed, ordinary in a liability-management exercise — and
recorded, because [E3-52] says read the terms and not just the quantity.

### OXYCHEM AND THE LOW-CARBON VENTURES — the operator's tasking, from the filings

**OXYCHEM: SOLD. This is the single most important structural fact about Occidental in 2026 and
the screen's nine-year series does not know it happened.**

| OxyChem, $M | 2023 | 2024 | 2025 |
|---|---|---|---|
| Net sales | 5,101 | 4,706 | **4,368** |
| Income before income taxes | 1,767 | 285 | **495** |
| **Income from discontinued operations, net of tax** | **1,364** | **212** | **262** |
| Operating cash flow (from the consolidated cash-flow statement) | 2,073 | 920 | **926** |

Sold to Berkshire Hathaway for **$9.7bn cash**, closed **2026-01-02**, against **$6,520M of
assets and $1,196M of liabilities held for sale ($5,324M net book)**, producing *"an estimated
gain of $3.2 billion, net of taxes"*.

**THE READ, both ways.** *For:* $9.7bn of certain cash for a business that earned $262M last
year, every dollar applied to debt, executed with a buyer who does not overpay. *Against, and
the run states its own caveat on its own favourable point:* 2025 was a **trough** year for
chlor-alkali — the same division earned **$1,364M in 2023** — so the flattering 37× multiple is
partly a cyclical artifact and the true multiple against mid-cycle earnings is closer to **7×**.
**And the cash arithmetic is close to neutral:** OxyChem contributed **$926M of FY2025 operating
cash flow**; the interest saved is FY2025's **$1,079M** against the filed Q2 2026 figure of
**$108M, an annualised $432M** — a saving of about **$647M**. **Net, before any credit for the
price of the asset, the sale costs roughly $280M a year of cash flow.**

**THE STRUCTURAL CONSEQUENCE IS THE POINT, AND IT RUNS AGAINST THE COMMON HOLDER.** OxyChem was
the one segment whose earnings were not a function of a screen price for a barrel. **It is gone,
and Occidental in 2026 is a purer commodity price-taker than Occidental in 2025 was.** That
belongs at Q2, and it is filed there.

**AND THE LIABILITY DID NOT GO WITH IT.** FY2025 10-K, Note 4, verbatim: *"An Occidental
subsidiary will retain environmental liabilities relating to legacy sites … there are
post-closing indemnification obligations for (i) legacy environmental liabilities and (ii)
pre-closing liabilities of OxyChem … **Occidental also entered into a guaranty in favor of
Berkshire Hathaway**, pursuant to which Occidental guarantees the indemnification obligations of
its subsidiaries under the Purchase Agreement."* Note 11 quantifies it: **152 remediation sites,
$1,870M accrued, of which $1,674M relates to the retained chemical legacy.**

**THE LOW-CARBON VENTURES AND STRATOS: A SUBSIDISED OPTION, NOT A BUSINESS — and the filing is
what says so, not this run.**

- **Pre-revenue at the filing date.** FY2025 10-K, verbatim: *"The Company **expects to begin**
  sequestering CO₂ captured at STRATOS, the first commercial-scale direct air capture facility
  in Ector County, Texas, **in 2026**."* Future tense, in a document filed 2026-02-18. **No
  STRATOS revenue is disclosed in any period.**
- **The spend is disclosed and it is not small.** FY2025 10-K, verbatim: *"In 2025, capital
  expenditures related to the midstream and marketing segment totaled **$720 million**, before
  contributions from noncontrolling interests, **the majority of which were related to the
  construction of STRATOS**."*
- **The economics are conditioned on subsidy, in the filer's own sentence.** Verbatim: *"The
  profitability of sequestration projects is dependent upon the costs of developing, building and
  operating sequestration infrastructure, demand for sequestration services from emitters and
  **the availability of certain tax attributes and credits generated from the capture and
  storage of CO₂**."* **A business whose own 10-K names tax credits as a condition of
  profitability is an option on a policy regime.** [E2-59] is the corpus's ruling on exactly
  that shape: *"the moat belongs to the **regime**"*, and *"That day is gone"* is how it ends.
- **The nearest public comparable in the same portfolio has already been written to zero.**
  Note 7, verbatim: *"In 2025, the Company recorded its share of NET Power's impairment losses of
  **$401 million, bringing book value of its investment to zero**."* Occidental owns **40.3% of
  NET Power** and carries it at **$0**.
- **And the segment it sits in earned almost nothing.** Midstream and marketing pre-tax segment
  income: **$(35)M (2023) · $563M (2024) · $252M (2025)** — the 2025 figure struck after **$487M
  of asset impairments** and *including* a **$301M** gain from a pro-rata ownership reduction in
  WES. Strip the one-off gain and the segment is negative.

> **VERDICT ON THE DAC QUESTION, ANSWERED AS ASKED: on the filed record STRATOS is a
> capital-consuming option on a tax-credit regime, not a business. It has no disclosed revenue,
> it consumed the majority of $720M in 2025, its profitability is explicitly conditioned on
> credits, and the adjacent 40.3%-owned public vehicle is carried at zero. It may become
> something. Nothing in the filings supports valuing it as anything today, and this run values
> it at zero — which is also what the balance sheet does with its closest analogue.**

### GREAT, GOOD, OR GRUESOME? **[E4-20]**, scoped by **[E4-43]** and **[E5-40]**

- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [x] **GRUESOME — on [E4-20]'s own definition, both limbs met.**

> *"the gruesome account **both pays an inadequate interest rate and requires you to keep adding
> money at those disappointing returns**."*

**Limb 1 — the interest rate is inadequate.** At the (c) judgment and the three-year window,
owner earnings to the common are **$1,724M on a $60,928M cap = 2.83%**, against a **5.25%**
sovereign — and that is measured over a window whose mean WTI ($72.72) sat **$6.88 above** the
nine-year average.

**Limb 2 — it requires you to keep adding money.** The 2026 capital plan is **$5.5–5.9bn, 9–10%
of the entire market capitalisation, every year, to hold production FLAT** — plus $12.1bn of
acquisition in 2024 and $35.7bn in 2019 to hold the resource position.

**And the return on the added capital is falling: unleveraged pre-tax return on capital employed
~10.4% → ~8.0% → ~6.5%.** **[E4-43]** is the scoping rule and it is applied honestly rather than
ignored: the *good* class passes, and its illustration is *"nothing shabby about earning $82
million pre-tax on $400 million of net tangible assets"* — **20.5% pre-tax. Occidental earns
6.5%.** **[E5-40]**'s retention benchmark is ~12% as *"quite satisfactory"*; Occidental is at
roughly half of it. **The gruesome escape clause — *"unless the cash they consume gets to earn a
reasonable return"* — is the test, and on the filed series the answer is no.**

**THE HONEST QUALIFIER, AND IT IS THE WHOLE PROBLEM: this classification is a function of an
exogenous price.** At the 2Q26 realisation of $96.78/Bbl the same business is comfortably
*good*. At the 2020 average of $39.16 it is a solvency question. **A business whose [E4-20] class
changes with a price it does not set has not earned a place in either of the first two boxes**;
[E3-51] is the corpus's name for what it has instead — *"the advantage lives in the wave, not the
surfer."*

### STAYING POWER — score all three **[E5-11]**

> *"Financial staying power requires a company to maintain three strengths under all
> circumstances: (1) a large and reliable stream of earnings; (2) massive liquid assets and
> (3) no significant near-term cash requirements."*

**(1) A large and reliable stream of earnings — LARGE, NOT RELIABLE. HALF A PASS.**
$9,606M of continuing-operations operating cash flow is large. **Reliable it is not, and the
filer quantifies the unreliability itself: $240M of pre-tax cash per $1 of WTI, and $120M per
$0.50 of domestic gas.** In the nine-year window WTI ranged $39.16 to $94.53. **[E5-29] is
checked and does not rescue it:** *"Volatility is far from synonymous with risk"* — true, and a
volatile stream with certain coverage passes. **Occidental's stream is not volatile around a
certain level; its level is the variable.**

**(2) Massive liquid assets — ADEQUATE, NOT MASSIVE.** Cash and equivalents **$4,150M** at
2026-06-30 (**$4,188M including restricted**), plus an undrawn **$4,150M** revolver to
2028-06-30. **[E5-39] governs how the revolver is counted: *"We will never be dependent on the
kindness of strangers … cash is a lot like oxygen."* No bank line is counted.** On the corpus's
own standard the liquid assets are **$4.2bn against a $60.9bn capitalisation and a $5.7bn annual
maintenance requirement — under nine months of maintenance capital.**

**(3) No significant near-term cash requirements — THE KILLER, AND FOR THE FIRST TIME IN SEVEN
YEARS IT LARGELY PASSES.**
- **Debt maturities: $24M in 2026, $48M in 2027, $14M in 2028, $367M in 2029.** Genuinely
  trivial. This is the transformation the OxyChem proceeds bought and it is real.
- **But three near-term requirements remain and they are not small:** the **$679M/yr preferred
  coupon**, which is contractual and which blocks the common dividend if unpaid; the
  **$5.5–5.9bn/yr of maintenance capital**, which is not optional if volume is to hold; and
  **$3,038M of purchase obligations due in 2026** (10-K contractual-obligations table, of
  $12,617M total).
- Longer-dated but real: **asset retirement obligations $3,656M** and **environmental
  remediation $1,870M**.

**LEVERAGE, NAMED AND QUANTIFIED — no ratio ceiling is applied, because the framework has none
and the corpus supplies none.**

| at 2026-06-30, $M | |
|---|---|
| Total debt and finance leases | **13,743** |
| less cash and equivalents | (4,150) |
| **Net debt** | **9,593** |
| **plus preferred at face** | **8,490** |
| **Total claims ranking ahead of the common** | **18,083** |
| Total equity | 42,381 |
| less preferred carrying value | (8,287) |
| **Common equity** | **34,094** |
| Net debt ÷ FY2025 continuing operating cash flow | **≈1.0×** |

**[E2-54]'s COVERAGE TEST, run as the corpus specifies — *"all interest, both payable and
accrued, to be comfortably met out of current cash flow net of ample capital expenditures."***
Operating cash flow is stated after cash interest, so interest is added back:

| (c) used | (OCF $9,606M + interest $1,079M) − (c) | ÷ FY2025 interest $1,079M | ÷ current run-rate interest $432M |
|---|---|---|---|
| 5,700 | 4,985 | **4.62×** | 11.54× |
| **7,500 (the judgment)** | **3,185** | **2.95×** | **7.37×** |
| 8,026 | 2,659 | 2.46× | 6.16× |

**Coverage passes comfortably at today's price and today's debt. It passed nothing in 2020, on
the same assets.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]** — and the corpus's bar **[E4-51, E4-40]**

**[E4-40] is the governing instruction and it is why the first death below is modelled from
exposure rather than from the recent record:** *"all of us in the industry made a fundamental
underwriting mistake by **focusing on experience, rather than exposure**."* Occidental's recent
experience is a $96.78 quarter. Its **exposure** is $240M per dollar of WTI.

**AND OCCIDENTAL HAS THE RARE ADVANTAGE OF HAVING ALREADY WRITTEN ITS OWN DEATH SCENE. THE
2020 RECORD IS NOT A HYPOTHETICAL; IT IS A FILED PRECEDENT ON THESE ASSETS.**

**DEATH 1 — THE PRICE FALLS AND THE DEPLETION TREADMILL DOES NOT STOP. Likelihood: A REAL
POSSIBILITY.**

*Mechanism.* Maintenance capital of **$5.5–5.9bn a year is not discretionary if volume is to
hold**, because the wells decline. Revenue is set by a price Occidental does not influence.
Below a WTI in the mid-$50s the maintenance requirement exceeds the cash generated, and the gap
is funded by cutting capital (which liquidates volume), selling assets, or issuing securities.

*Quantified from filed figures*, using the 10-K's own Item 7A sensitivity of **$240M of pre-tax
cash per $1/Bbl of WTI**, from the FY2025 base of $9,606M of continuing operating cash flow at a
$64.81 average WTI:

| WTI | change vs $64.81 | pre-tax cash effect | approx. operating cash flow | less (c) $5,700M (bare volume maintenance) | less $679M preferred |
|---|---|---|---|---|---|
| $80 | +$15.19 | +$3,646M | ~13,252 | +7,552 | **+6,873** |
| **$64.81 (FY2025 actual)** | — | — | **9,606** | **+3,906** | **+3,227** |
| $55 | −$9.81 | −$2,354M | ~7,252 | +1,552 | **+873** |
| **$50** | **−$14.81** | **−$3,554M** | **~6,052** | **+352** | **−327** |
| **$45** | −$19.81 | −$4,754M | ~4,852 | −848 | **−1,527** |
| **$39.16 (the 2020 average)** | −$25.65 | −$6,156M | **~3,450** | **−2,250** | **−2,929** |

*(pre-tax basis; the after-tax effect is smaller in the near term and the direction is the same.
Domestic gas adds to it: at the 2Q26 realisation of **negative $1.48/Mcf** the gas leg is already
subtracting.)*

**Below roughly $50 WTI, Occidental cannot hold its production flat and pay its preferred out of
its own cash flow.** That is the sentence, and the filed precedent for it is 2020.

**DEATH 2 — THE RESERVE TREADMILL FORCES ANOTHER ACQUISITION AT A CYCLE TOP. Likelihood:
LIKELY over a decade.**
*Mechanism.* Drill-bit replacement of **65.1%** over three years; **2.50 years** of booked
undeveloped inventory; total proved reserve life down **9.49 → 8.80 years**. The company has
twice solved this by buying — **$35.7bn in 2019 and $12.1bn in 2024** — and both times the
market let it buy only when prices, and therefore asset prices, were high. **[E2-27] is exactly
this: *"viewed individually, each company's capital investment decision appeared cost-effective
and rational; viewed collectively, the decisions neutralized each other and were irrational … After
each round of investment, all the players had more money in the game and returns remained
anemic."*** The competitor row shows the collective round: **$40.0bn (FANG), $36.0bn (COP) and
$18.0bn (OXY) of costs incurred in 2024 alone.**

**DEATH 3 — THE PREFERRED COMPOUNDS AND THE COMMON IS DILUTED AT THE BOTTOM. Likelihood: A
LOW-LEVEL POSSIBILITY at today's price; A REAL POSSIBILITY below $50 WTI — AND IT HAS ALREADY
HAPPENED ONCE.**
*Mechanism, from the instrument's own terms:* if the preferred dividend is not paid in cash the
rate goes to **9% per annum compounded quarterly** and **common dividends are prohibited until
cured**. The alternative is to pay it in stock. **Occidental did exactly that in 2020.** FY2020
10-K, Note 14, verbatim:

> *"**In March and June 2020, the Board of Directors elected to declare its quarterly dividend on
> the Preferred Stock in shares of common stock.** In accordance with the Certificate of
> Designations, the number of shares issued was calculated based on **90 percent of the average
> of the volume weighted average price** over each of the 10 consecutive trading days following
> the dividend declaration date. **In April and July 2020, Occidental issued approximately 17.3
> million and 11.6 million shares, respectively, of common stock to the holders of the Preferred
> Stock.**"*

**Approximately 28.9 million common shares were issued to the preferred holder, at a 10%
discount to a ten-day VWAP struck after the declaration date, to preserve $400 million of cash —
at the bottom of the worst year in the company's history.** *Quantified today:* $8,490M at 9%
compounding accrues **$764M a year**, and the same stock-settlement mechanic on today's count
would issue roughly **12.4 million shares a year** at a 10% discount.

**DEATH 4 — RECORDED, NOT MODELLED: the retained chemical liability.** Occidental sold OxyChem
and **kept $1,674M of accrued legacy environmental liability across 152 sites, plus an
indemnification guaranty in favour of Berkshire.** [E4-40] applies: the accrual is an estimate;
the exposure is a statutory regime (*"CERCLA and similar laws, **may apply retroactively and
regardless of fault**"* — Note 11, verbatim).

### **[E4-51]: THE BEAR CASE ITS HOLDERS WOULD ACCEPT — AND ITS ANSWER, THE 2020 PRECEDENT**

*A holder would say: none of Death 1 matters, because the balance sheet is transformed. Debt is
$11.8bn against $36bn in 2020. Maturities are $24M this year. Coverage is 7×. Occidental in 2026
is not Occidental in 2020.*

**That is true, it is the strongest thing in the file, and it is stated first. Here is the
answer.** In 2019 Occidental had just bought Anadarko and its filings said the plan was working.
Within twelve months, on **the same assets**:

| the 2020 record, all from the FY2020 10-K, accession 0000797468-21-000009 | |
|---|---|
| Net loss attributable to common stockholders | **$(15,675)M**, or **$(17.06) per share** |
| — of which Q2 2020 alone | $(8,353)M |
| Asset impairments and other charges, continuing operations | **$11,083M** (plus $2.2bn on Ghana in discontinued operations) |
| Total equity | **$34,232M → $18,573M**; retained earnings $20,180M → $2,996M |
| The dividend | **$0.79 → $0.01**, a 98.7% cut in one step |
| Capital expenditure | **$6,367M → $2,535M**, a 60% cut |
| Credit ratings at 2025-12-31 of that year | **BB (Fitch) · Ba2 (Moody's) · BB− (S&P)** — *all three below investment grade* |
| Asset sales to survive | *"Since the Acquisition, Occidental completed the sale of significant non-core assets for net proceeds of approximately **$8.2 billion**"* |
| Shares issued to the preferred holder in lieu of cash | **~28.9 million**, April and July 2020 |
| Warrants distributed to common holders, 2020-08-03 | **~116 million at a $22.00 strike**, expiring 2027-08-03 |

**And two sentences from that filing that no amount of 2026 balance-sheet strength can unwrite.**
FY2020 10-K, Liquidity and Capital Resources, verbatim:

> *"Occidental currently expects its cash on hand to be sufficient to meet its debt maturities,
> operating expenditures and other obligations for the next 12 months from the date of this
> filing. **However, given the inherent uncertainty associated with the duration and severity of
> the COVID-19 pandemic and its resulting impact on oil demand, Occidental may need to raise
> capital to fund its operations and refinance debt maturities.**"*

and, on the covenant, verbatim:

> *"On March 23, 2020, Occidental **amended the sole financial covenant in its RCF** by revising
> the definition of 'Total Capitalization' **to exclude any non-cash write-downs, impairments and
> related charges occurring after September 30, 2019.**"*

**Occidental amended its covenant's denominator ten days after announcing the first dividend cut
and three months before taking an $8.6 billion impairment.** *No going-concern qualification was
issued and none is claimed here.* But **[E2-55]** is the standard — *"we do not wish it to be
only likely that we can meet our obligations; **we wish that to be certain** … acceptable
long-term results under **extraordinarily adverse conditions**"* — and **the corpus's own bar is
whether the worst case is survivable without the kindness of strangers. In 2020 Occidental
survived it by cutting the dividend 98.7%, cutting capital 60%, selling $8.2 billion of assets,
paying its preferred holder in discounted stock, and amending a covenant.** Every one of those is
a filed fact. **The business that did that is the business being priced today, at a higher price,
with the same preferred still outstanding.**

**A CORRECTION TO THE OPERATOR'S BRIEF, MADE ON THE FILED RECORD.** The tasking says the 2020 cut
ran *"from $0.79 to $0.11."* **A $0.11 dividend was announced as an intention and was never
paid.** Q1 2020 10-Q, verbatim: *"Announced the Board of Directors' **intention** on March 10,
2020 to reduce the quarterly common stock dividend to **$0.11** per share from $0.79 per share,
**effective July 2020, subject to Board approval**."* It was overtaken. Q2 2020 10-Q and the
FY2020 10-K both describe the action, verbatim, as: *"**Reduced the quarterly common stock
dividend to $0.01 per share from $0.79 per share**, effective July 2020."* And the filed
quarterly series is *"Dividends per common share $0.79 $0.01 $0.01 $0.01"*. **The cut was 98.7%
in a single step, not 86%. The correction makes the point harder, not softer, and the
manufactured-growth arithmetic at Stage 0 uses the filed $0.01.**

- **VERDICT: [x] OUT.** Not merely UNRESEARCHED and not UNKNOWABLE — the evidence is in and it
  is filed. **A business that (i) is classified GRUESOME on [E4-20]'s own two-limb definition at
  an above-average price window, (ii) cannot cover its own maintenance capital and its preferred
  coupon below roughly $50 WTI on its own disclosed sensitivity, and (iii) has already
  demonstrated, once, on these exact assets, that its response to that condition is a 98.7%
  dividend cut, a 60% capital cut, $8.2bn of forced asset sales and stock issued to its preferred
  holder at a discount — fails Q4.** The 2026 balance sheet makes the *next* episode survivable;
  it does not make the business one whose survival is *certain* under [E2-55]'s
  *"extraordinarily adverse conditions."*
  *Recorded honestly: had the run been forced to choose between OUT and IN on the balance sheet
  alone, it would have said IN. The OUT rests on the earnings stream and the [E4-20] class, not
  on solvency at today's price.*

- **ONE UNRESEARCHED ITEM IS NAMED RATHER THAN GLOSSED, per the four-verdict rule.** The numeric
  level of the RCF's sole financial covenant (maximum Total Debt to Total Capitalization) and
  Occidental's actual ratio against it **are not stated in any 10-K, 10-Q or 8-K read for this
  run**. **The artifact that would resolve it: the Credit Agreement and its March 2020 amendment,
  filed as exhibits to Occidental's 8-K/10-Q filings on EDGAR.** It does not change any verdict
  above — the file is already closed at Q2 — and it is recorded so the gap is visible rather than
  silently filled.

---

### A DISCLOSURE NOTE ON THE PREFERRED, from a recorded sweep

The **$4.00-per-share mandatory-redemption trigger quoted above is from the FY2025 10-K, Note 13
(accession 0001628280-26-009059)**, where it is stated in full. **A recorded keyword sweep of the
FY2019, FY2020 and FY2021 Form 10-Ks and the Q1 and Q2 2020 Form 10-Qs held locally — searching
"$4.00", "trailing twelve", "trailing 12", "mandatorily redeem" and "redemption obligation" —
found no instance of that trigger.** Those filings describe only the optional redemption:
*"The Preferred Stock is redeemable at Occidental's option after the 10th anniversary of
issuance."* The governing instrument is the **Certificate of Designations, Exhibit 3.1 to the
Form 8-K filed 2019-08-08, File No. 1-9210**, which was not fetched for this run. **Two readings
are possible — a disclosure that improved over time, or a material term under-described for
several years — and this run does not choose between them on the evidence it has.** The current
disclosure is complete and is what the run relies on.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

⛔ **Q2 returned OUT and Q4 returned OUT. Q5 IS NOT OPEN AS A GATE.** What follows exists solely
to satisfy the queue's output contract, which requires a price either way. **It carries no entry
language, it is not a valuation clearance, and no part of it may be read as a recommendation.**

**Sovereign, for the earnings currency: USD 30-year 5.25%, observation date 2026-08-31, FRED
DGS30, from the issuing authority's published constant-maturity series.**

### 1. THE YIELD — owner earnings ÷ market cap, beside the sovereign

| | (c)=5,700 *volume-flat* | (c)=6,427 *as spent* | **(c)=7,500 THE JUDGMENT** | (c)=8,026 *drill-bit replacement* |
|---|---|---|---|---|
| **Window A — 3-yr mean, to the common** | 5.78% | 4.59% | **2.83%** | 1.97% |
| **Window B — FY2025, to the common** | 4.91% | 3.72% | **1.96%** | 1.09% |
| **vs the 5.25% sovereign (Window A)** | +0.53 pts | −0.66 pts | **−2.42 pts** | −3.28 pts |

*(All after the $679M preferred coupon. On the $60,928M cap; on the fully diluted $67,133M cap
each figure is ~9% lower — e.g. the judgment line becomes 2.57% and 1.78%.)*

**Seven of the eight cells sit BELOW the risk-free rate.** The single cell that clears it
(+0.53 points) requires simultaneously the more favourable window and a (c) that, on this run's
own reserve arithmetic, funds volume while the resource base shrinks.

### 2. WHAT THE PRICE ALREADY ASSUMES

**At $60.95 the market is paying, on the three-year window and the judgment (c), 35× owner
earnings to the common.** To reach the **[E4-28]** floor of a 10% pre-tax expectancy the business
must add **+7.17 percentage points** of perpetual growth. Even at the most generous
construction — volume-flat (c), three-year window — the requirement is **+4.22 points of
perpetual growth**.

**What the business has actually done, measured on the physical and the return series rather
than on price-driven earnings:**
- Production **1,434 → 1,433 Mboe/d** (FY2025 → 2Q26): **flat.**
- Total proved reserve life **9.49 → 8.80 years**: **shrinking.**
- Unleveraged pre-tax return on capital employed **~10.4% → ~8.0% → ~6.5%**: **falling.**
- Organic drill-bit replacement, three-year: **65.1%.**

**[E4-35] is the base rate that a growth case must clear**: *"I would wager you a very
significant sum that **fewer than 10 of the 200 most profitable companies** in 2000 will attain
15% annual growth in earnings-per-share over the next 20 years."* **The growth required here is
perpetual, not for twenty years, and it must come from a company whose unit volume is flat and
whose selling price it does not set.** **[E4-44]** bounds it further: *"the value of an asset,
whatever its character, **cannot over the long term grow faster than its earnings do**."*

**And [E2-63] requires the ceiling be named as well as the yield.** Occidental's upside is
bounded by **the oil price** and by **the reserve base**: 8.80 years of total proved reserves,
2.50 years of booked undeveloped inventory, and a resource position that has twice needed a
multi-billion-dollar acquisition to extend.

### 3. WHAT YOU ARE PAID — points over the sovereign

**At the (c) judgment: −2.42 points (three-year window) to −3.29 points (FY2025 window).**
**You are paid less than the government bond, before any allowance for the fact that the
government bond's coupon does not depend on OPEC.**

### 4. **THE PRICE — reported as a round-number range [E4-01], on FULLY DILUTED shares**

*"Using precise numbers is, in fact, foolish; working with a range of possibilities is the
better approach."*

| construction | value per share, capitalised at the 5.25% sovereign | value per share, at the [E4-28] 10% floor |
|---|---|---|
| (c)=5,700 · 3-yr window | $60.95 | $32.00 |
| (c)=5,700 · FY2025 | $51.76 | $27.17 |
| (c)=6,427 · 3-yr window | $48.38 | $25.40 |
| (c)=6,427 · FY2025 | $39.19 | $20.57 |
| **(c)=7,500 · 3-yr window — THE JUDGMENT** | **$29.82** | **$15.66** |
| **(c)=7,500 · FY2025 — THE JUDGMENT** | **$20.63** | **$10.83** |
| (c)=8,026 · 3-yr window | $20.72 | $10.88 |
| (c)=8,026 · FY2025 | $11.53 | $6.06 |

> # **THE PRICE — COMPUTATION, NOT A CLEARANCE**
>
> **At the disclosed (c) judgment of $7,500M, capitalised against the 5.25% sovereign, on
> 1,101,437,371 fully diluted shares: roughly $20 to $30 per share.**
>
> **Against the [E4-28] 10% floor rather than the bond: roughly $11 to $16 per share.**
>
> **Widest defensible band across every (c) construction and both windows, at the sovereign:
> roughly $12 to $61 per share.**
>
> **Current price: $60.95, NYSE close 2026-09-01** *(aggregator quote, flagged)*.
>
> **The quoted price sits at or above the top of every band computed above.**

**A DIAGNOSTIC WORTH STATING PLAINLY.** The one cell that reproduces the market price exactly —
**$60.95** — is (c) = $5,700M on the three-year window, capitalised at the 30-year Treasury yield
with **zero growth and zero risk premium**. **That is what the quote assumes: that maintenance
capital is only the amount that holds this year's barrels, that the recent above-average price
window is the normal one, and that a business whose cash flow moves $240M per dollar of WTI
should be discounted at the rate of the United States government.**

### 5. THE FLOOR, THEN THE RANKING **[E4-28, E3-45]**

**Honest pre-tax expectancy at this price: 2.83% at the judgment (c) on the three-year window;
1.96% on FY2025.** *"That's the figure we quit on … we don't want to buy equities where our real
expectancy is below 10 percent. Now, **that's true whether short rates are 6 percent or whether
short rates are 1 percent.**"* **[E4-28]**

> **BELOW THE FLOOR. THE NAME IS NOT RANKED — IT IS QUIT ON**, which is the corpus's own
> vocabulary and is the correct disposition for a file already closed at Q2 and Q4.

### 6. WHICH BAR, AND THE WINDAGE COUNT

- [x] **Bar 2 — the screamer test [E4-01].** Take the conservative end of the range and ask
  whether the price already clears it. **The conservative end is $11.53 per share. The price is
  $60.95.** Outcome: **above the whole range → no.** No margin is added on top; *"startlingly
  low" is what you observe, not what you subtract.*
- [ ] Bar 1 not used. The two are never applied to the same number.
- **WINDAGE COUNT: ONE.** Conservatism is spent once **[E4-11, E4-48]**, at the **(c) judgment**,
  where $7,500M was taken over the $5,700M the filer's own capital plan would support. **Two
  further conservative adjustments were computed and then DELIBERATELY NOT APPLIED**, and are
  reported as sensitivities so the reader can see them and the arithmetic stays honest:
  1. **[E4-41]'s price normalisation** — the FY2023–25 window's mean WTI of $72.72 sits $6.88
     above the nine-year mean; applying it would cut owner earnings to the common by ~$1,205M
     after tax and take the judgment yield from 2.83% to **0.85%**.
  2. **The fully-diluted share count**, which is used for the per-share band but not
     double-counted in the yield table.
- **[E3-42] checked: no per-name risk premium is anywhere in the discount rate.** The sovereign
  is used as observed. Certainty is priced at Q1's understanding gate and, where a margin would
  apply, once at the end — never in the rate.

- **VERDICT: [ ] IN · [x] NOT OPENED AS A GATE — Q2 OUT and Q4 OUT close the file before Q5.
  Ranking position: NOT RANKED, per [E4-28]'s floor. This section is a computation.**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No position exists and none is contemplated.** Under **[E2-28]** the three hold conditions do
not arise; there is nothing to hold. Q6 is completed as the corpus intends it — a **pre-committed
statement of what would refute this run** — and it is written **before** any such evidence
appears, per **[E1-02]**: *"I believe in establishing yardsticks **prior to the act**."*

### What would prove this run wrong — and, critically, WHAT WOULD NOT

**[E5-35] governs the shape of the answer: a Q2 OUT is not repaired by price.** *"You can turn
any investment into a bad deal by paying too much. **What you can't do is turn any investment
into a good deal by paying little.**"* **Therefore no price reopens this file. Not $40, not $25.**
That is stated explicitly so that a later fall in the quote is not mistaken for a thesis
confirmation or an entry signal.

**What WOULD reopen it is a change in the CLASS, and [E4-17] says such changes are slow:**
*"we sell — really when we … **reevaluat[e] the economic characteristics of the business** … And
those beliefs change quite gradually."* Four pre-committed, filing-checkable reopeners:

1. **A cost advantage that becomes wide and sustainable [E2-58].** Occidental's all-organic-sources
   three-year F&D falling **decisively below the peer field** — say below **$7.50/Boe while
   Diamondback, Devon, EOG and ConocoPhillips remain above $9.00** — for **three consecutive
   annual filings**. Today it is $10.29 against a field of $9.21–$15.91: **indistinguishable.**
2. **Organic replacement above 100% by the drill bit alone, for three consecutive years, with no
   acquisition of reserves in place.** Today: **65.1% over three years.** This is the [E4-04] test
   and it is the one that matters most.
3. **STRATOS producing disclosed segment revenue at a positive margin without tax credits.**
   That would be a genuinely different business with different economics, and it would have to be
   visible as a revenue line, not as a capital line. Today it is pre-revenue and the 10-K
   conditions its profitability on *"the availability of certain tax attributes and credits."*
4. **The preferred retired.** Not redeemable at Occidental's option before **August 2029**, and
   then only at 105% of face. Retirement would remove $679M a year and the $4.00 distribution
   cap — a real change to what accrues to the common, and a dated one.

**And the honest statement of what would prove the run wrong in the OTHER direction — [E4-26]
applied to this run's own conclusion:** the single most likely way this file is wrong is that
**oil stays above $85 for a decade**, in which case Occidental is a *good* business bought at a
fair price and the framework's commodity doctrine will have cost the operator a large gain.
**The run accepts that risk explicitly**, on **[E5-13]**'s ground — *"about a dozen truly good
decisions — that would be about one every five years"* — and on **[E3-47]**'s
counterweight, which is recorded rather than suppressed: *"Typically, our most egregious mistakes
fall in the omission, rather than the commission, category… **their invisibility does not reduce
their cost.**"* **This may be an omission error. It is made deliberately, with the cost
acknowledged in writing.**

### The monitoring metrics, pre-committed **[E4-32, E4-55, E3-30]**

- **The physical series, which is the honest one [E4-55]:** total proved reserve life
  (**8.80 years**), proved developed life (**6.30 years**), booked PUD inventory
  (**2.50 years**), production (**1,433 Mboe/d**).
- **The return series [E3-46]:** unleveraged pre-tax return on capital employed (**~6.5%**).
- **The capital-structure series:** principal debt (**$11.8bn**, milestone $10.0bn), preferred
  face (**$8,490M**), share count (**999,637,371** plus **101.8M** warrant shares).
- **[E3-30]'s question, asked of any change: *"is this erosion just part of an aberrational
  cycle … or … has the business slipped in a way that permanently reduces intrinsic business
  values"*?** For Occidental the honest answer is that the *cycle* is the business, which is why
  the reopeners above are all structural and none of them is a price.

### Position size **[E3-45, E2-62]**

**ZERO. Not held; not to be held on this analysis.** [E2-62]'s licence condition does not arise.

- **VERDICT: [x] OUT** — consistent with Q2 and Q4. The file is closed on the business, not on
  the diligence and not on the evidence.

---
## SELF-AUDIT (operator rule 6 — the run is incomplete until this is checked)

- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 OUT → (Q3, Q4, Q5, Q6
      completed FOR THE RECORD under operator rule 3's header, per the queue's output contract).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on
      the filed unit economics; Q3's IN is written as the corpus requires — *the absence of found
      disqualifiers*, not a finding of honesty **[E5-17]**.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** One item is recorded
      UNRESEARCHED and it changes no verdict: the numeric level of the RCF's Total Debt to Total
      Capitalization covenant. **Artifact: the Credit Agreement and its 2020-03-23 amendment,
      filed as exhibits on EDGAR under CIK 0000797468.** A second, similar item: the Certificate
      of Designations (**Exhibit 3.1 to the Form 8-K filed 2019-08-08, File No. 1-9210**), not
      needed because the FY2025 10-K states the preferred terms in full.
- [x] **No UNKNOWABLE verdict was issued**, and the run says why: every question here was
      resolvable from filed documents.
- [x] **Step 0: the filing was read, with accession numbers; three figures were cross-checked**
      against the filed statements (cash flow, EPS, and the preferred coupon on three independent
      lines).
- [x] **Owner earnings on a multi-year mean; both windows stated; the capex band disclosed as a
      judgment.** (c) = **$7,500M**, band **$5,700M–$8,026M**, built from the reserve-replacement
      ratio and organic F&D cost in the supplemental oil and gas disclosures as tasked.
- [x] **Competitor row filled** — four peers plus the subject, same metric, same window, each
      from the peer's own FY2025 10-K supplemental disclosures. Chevron excluded **with the
      reason stated**, not silently.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.**
- [x] **Value stated as a round-number range, not a point estimate.**
- [x] **One bar chosen, not both** (Bar 2, the screamer test). **Windage count: ONE**, stated,
      with the two unapplied adjustments disclosed as sensitivities.
- [x] **Prices dated; the aggregator used for the live quote only and flagged.**
- [x] **Operator rule 9 discharged in writing at Q3** — the Berkshire-stake bias declaration was
      made **before** the evidence was read, and Berkshire's ownership is used nowhere as
      evidence of quality.
- [x] **[E4-26] discharged: the run refused its own tasking's priors in three places** — the
      capex/D&A ratio (0.85×, not 0.77×), the volume-liquidation hypothesis (**not supported**),
      and the dividend cut ($0.79 → $0.01, not $0.11). It also **refuted its own first-pass
      finding** on reserve replacement when the competitor row showed the drill-bit metric to be
      non-comparable across filers.
- [x] **Run committed to git.**

### CORRECTIONS MADE TO THE INPUTS THIS RUN WAS GIVEN — recorded, not buried

| the input as received | what the filings say |
|---|---|
| capex/D&A **0.77×** | **0.85×** ($6,427M ÷ $7,533M) on the FY2025 filed statements; 0.90× against oil-and-gas segment DD&A |
| 2020 dividend cut **$0.79 → $0.11** | **$0.79 → $0.01.** The $0.11 was an announced *intention* (2020-03-10) never paid; a 98.7% cut in one step |
| nine-year SBC of 443 / 423 / 629 (2023/24/25) | **$203M / $213M / $234M** per Note 14 of the FY2025 10-K |
| nine-year owner-earnings series as a measure of the business | includes **OxyChem, sold 2026-01-02**, a company **2.39× smaller** at the start, and a price spike worth **50.5% of the total from 22% of the window** |
| bottom yield **6.69%** vs a 5.18% sovereign | **1.09%–2.83%** to the common at the disclosed (c), against a **5.25%** sovereign |
| the operator's prior that capex below D&A means liquidation of volume | **not supported.** Production is flat on the 2026 plan. What IS being drawn down is the **reserve base and the undeveloped inventory** — a different channel, and it is quantified |

---
## REGISTER

- **Verdict: [x] OUT — about the business.** Not UNRESEARCHED (the diligence was done), not
  UNKNOWABLE (the evidence is filed and it is sufficient).
- **One line:** *Occidental is a large, competently run, honestly accounted, newly de-levered oil
  and gas producer with no measurable cost advantage over its peers, which replaces 65% of its
  production by the drill bit and buys the rest, whose selling price went below zero on 38% of its
  volume in the most recent filed quarter, which has just divested the one segment not indexed to
  a screen price, and which carries $8.5 billion of 8% preferred stock ahead of the common — and
  at $60.95 it yields between 1.1% and 2.8% against a 5.25% government bond.*
- **THE PASS/FAIL LINE:** **FAIL — the file was closed at Q2 (IS IT A FRANCHISE?), on the
  commodity doctrine [E2-58] and the depleting-asset exclusion [E4-04], and it failed again
  independently at Q4 (WILL IT SURVIVE?) on the [E4-20] gruesome classification and the named
  death. Q1 returned IN; Q3 returned IN in the narrow sense that no disqualifier was found. Q5
  and Q6 were completed for the record only. Not all six returned IN.**
- **THE STRONGEST DISCONFIRMING FACT AGAINST THIS RUN'S OWN CONCLUSION** *(recorded per [E4-26],
  because a run that reports only its supporting evidence has not been audited)*: **on the
  reserve-replacement metric that is robust to booking convention, Occidental is INDISTINGUISHABLE
  FROM ITS PEERS AND ITS ACCOUNTING IS CONSERVATIVE** — three-year all-sources replacement of
  **115.8%** at **$10.29/Boe**, against Devon $9.21, EOG $9.80, Diamondback $13.42 and
  ConocoPhillips $15.91, with a depletion charge of **$13.60/Boe that EXCEEDS that replacement
  cost.** The run's first pass, using drill-bit replacement alone (65.1%, $18.28/Boe, worst of
  five), read as a company liquidating at a premium cost. **The competitor row refuted that
  reading**, and the OUT that survives is therefore not *"Occidental is worse"* but the harder and
  more durable *"Occidental is the same"* — which is what [E2-58] says a commodity industry looks
  like, and which is why *"a cost advantage that is both wide and sustainable"* cannot be claimed
  here in either direction.
- **The second-strongest disconfirming fact:** the 2026 balance sheet. **$8.6bn of debt retired
  in six months; maturities of $24M, $48M and $14M in 2026, 2027 and 2028; interest down from
  $1,079M a year to a filed quarterly run-rate of $108M.** On solvency alone this run would have
  returned IN at Q4. **The OUT rests on the earnings stream and the [E4-20] class, not on the
  balance sheet, and the file says so.**
