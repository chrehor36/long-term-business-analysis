# Company Run — Bloomin' Brands, Inc. (BLMN) — 2026-09-21
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

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
- rate **5.34 %** · date **09/18/2026** (Friday, the last curve date published; struck fresh
  on **Monday 2026-09-21**, before that day's curve is posted) · source (issuing authority)
  **US Treasury daily par yield curve, 30 Yr**, fetched directly from
  `home.treasury.gov/.../daily-treasury-rates.csv/2026/all` on 2026-09-21. **Not FRED**;
  FRED is the fallback under operator rule 5. Raw line as fetched:
  `09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34`.
- FX: none. BLMN's continuing operations earn in USD. *(Brazil, the one material
  non-USD earner, was deconsolidated 2024-12-30 and is now a 33% equity-method stake;
  see the perimeter note below.)*
- Currency of the quote: USD. No ADR ratio.

**Price** — aggregator, flagged as such, live quote only:
- **US$8.07**, close of **2026-09-18**, Yahoo Finance chart endpoint (`query1.finance.yahoo.com`),
  fetched 2026-09-21. Last eight closes as fetched: 9.04 (09-09), 8.67, 8.69, 8.91, 8.01,
  8.04, 8.05, **8.07**.

**Share count — hand-read off the newest cover page**, not a weighted average and not
run.py's basis:
- **85,620,917 shares of common stock**, verbatim from the cover of the **10-Q for the
  quarterly period ended June 28, 2026**: *"As of August 3, 2026, 85,620,917 shares of
  common stock of the registrant were outstanding."*
- document · date · **accession no. `0001546417-26-000032`**, filed **2026-08-06**,
  primary document `blmn-20260628.htm`.
- One class of common stock. **No splits**: the Yahoo split-event series over a twenty-year
  window returns none, and `floor_screen.share_count_shift()` did not fire, so the cover count is
  the count and no split factor applies.

**CAP, STRUCK BY HAND: 85,620,917 × $8.07 = $690.9M.**

### Does the screen's cap reproduce? **NO.**
The screen row carries **`cap_m` 903**. 903 ÷ 85.62M = **$10.55 a share** — a price BLMN
has not traded at recently; it closed at $8.07 on 2026-09-18 and at $9.04 as recently as
2026-09-09. The share count is not the error: 85.62M is the filed cover count and the screen
implies the same order. **The screen's cap is a stale price, ~23.5% above the quote**, and
because `cap_m` is the denominator of `yield_bottom`, `vs_sovereign` and `growth_required`,
**every price-side field in the row is understated.** Corrected on the screen's own bottom
number, 74 ÷ 690.9 = 10.7%, not 8.21%.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Anchor filing: 10-K for the fiscal year ended December 28, 2025, accession
  `0001546417-26-000009`, filed 2026-02-25**, primary document `blmn-20251228.htm`.
  Secondary: the 10-Q above (`0001546417-26-000032`), and the 8-K EX-99.1 earnings
  releases named at Q3.
- **Figure cross-checked by hand against the filed statement:** the FY2025 consolidated
  statement of cash flows line *"Net cash provided by operating activities"* reads
  **$276,694** thousand in the filed document, against the XBRL
  `NetCashProvidedByUsedInOperatingActivities` fact of 276,694,000 for the period
  2024-12-30 → 2025-12-28 in accession `0001546417-26-000009`. It ties. The same statement
  carries *"Net cash provided by operating activities of continuing operations"* at
  **$275,946**, i.e. **$748** of the year's operating cash came from discontinued
  operations — the distinction that breaks both tools below.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language.** Bloomin' Brands leases a box,
  fits it out, and sells cooked food and drink to people who walk in. At the end of FY2025 it
  operated **957 company-owned restaurants in the United States** and collected royalties from
  **493 franchised** ones, almost all of them abroad (10-K FY2025, Item 1, accession
  `0001546417-26-000009`). Four brands, one model: Outback Steakhouse (548 company boxes),
  Carrabba's (187), Bonefish (156), Fleming's (66).
  The arithmetic of a year, all of it from the filed FY2025 income statement:
  **$3,884.2M of restaurant sales** across ~957 boxes — call it **$4.06M a box**, and the
  filed per-brand averages are Outback **$4,008**, Carrabba's **$3,716**, Bonefish **$3,145**,
  Fleming's **$6,071** thousand. Out of every dollar of that restaurant sale the filing takes
  **30.3c of food and beverage, 31.9c of labour, and 26.1c of other restaurant operating cost**
  (which contains $93.1M of advertising), leaving **11.7c** — the number the company calls
  restaurant-level operating margin. Then, against **total** revenues of $3,956.0M, **4.5%
  depreciation, 6.0% general and administrative, 1.1% impairment and closing provisions and
  0.7% goodwill impairment**, leaving **operating income of $37.2M — 0.9% of revenue.**
  Interest took $45.4M, and the company reported a **pre-tax loss of $8.2M** and net income of
  $13.8M from continuing operations only because of a $26.7M tax benefit.
  The second, much smaller business is the royalty: **$71.8M of franchise and other revenues**,
  of which the International Franchise segment alone produced **$31.3M of revenue against
  $0.9M of segment expense — $30.4M of segment operating income.** That is 82% of the whole
  company's operating income earned on 0.8% of its revenue, from 355 restaurants it does not
  own. I can understand both halves. The 957-box half is where all the capital is.
- **The scarce input this business controls:** I cannot name one that the company controls.
  Sites are leased and reproducible (the filing's own "Joey" prototype is ~5,000 sq ft, 190
  seats, explicitly designed to cut the cost of a box); restaurant labour is a spot market the
  filing says is inflating (*"1.3% from higher hourly and field management labor costs,
  primarily due to wage rate inflation"*); beef, seafood and produce are commodities bought at
  market. What is left is the four **brand names and the trade dress** — the Bloomin' Onion,
  the Outback decor, the Fleming's wine list. That is the only candidate, and whether it is
  scarce is precisely Q2's question, not Q1's.
- **Will the fundamentals look broadly the same in ten years?** Yes. Americans will still buy
  a steak cooked by somebody else; the cost structure of a casual-dining box has been three
  roughly-equal thirds for decades and is in the filing that way now. This is a business that
  is *"relatively simple and stable in character"* **[E3-31]** in the sense the corpus means:
  I do not have to forecast a technology to know how the money arrives. What will change — and
  what I cannot settle here — is how many guests come and what they pay.

- **VERDICT: [x] IN**
  *Understanding is not approval. The 0.9% operating margin, the 11.7% restaurant-level margin
  falling from 13.3%, and the fact that the international royalty stream is most of the
  operating income are Q2 and Q4 findings, recorded here and carried forward.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### THE BULL CASE, BUILT AT FULL STRENGTH FIRST, FROM THE FILINGS
Operator rule 9 and **[E4-26]** — *"intensively consider any evidence tending to disconfirm any
hypothesis of his, more so if he thought his hypothesis was a particularly good one"* — cut both
ways here, and the hypothesis I am most at risk of protecting is the cheap one. So the case for
Bloomin' Brands is stated at its best before it is tested, all of it from `0001546417-26-000009`
and `0001546417-26-000032`:

1. **The brands are not small and they are not uniformly sick.** Outback averages **$4,008
   thousand** a box; Fleming's **$6,071 thousand**, up from $4,422 in FY2019. In FY2025
   Carrabba's comped **+2.8%** and Fleming's **+2.5%**, both positive.
2. **The turn shows in the newest filed numbers.** H1 FY2026 combined U.S. comparable sales
   **+1.6%**, Q2 **+2.3%** — the first positive prints in two years. **Bonefish**, the worst brand
   in the group, comped **+7.0%** in H1 FY2026 with **traffic +3.7%**.
3. **There is a genuinely capital-free, high-return stream inside the company.** The International
   Franchise segment earned **$30,412 thousand of segment operating income on $31,297 thousand of
   revenue against $885 thousand of segment expense** — 82% of the whole company's operating income
   on 0.8% of its revenue, from 355 restaurants it does not own and does not have to build.
4. **The balance sheet was mended, deliberately, inside the window.** The Brazil Sale Transaction
   closed 2024-12-30 and brought **$103.9M and then $123.5M** to the revolver across 2025; the
   2025 convertible notes were fully settled May 2025; there is **nothing due before 2029**.
5. **Management has stopped spending on growth to spend on the base.** New-unit development slowed
   to about six planned openings in 2026 from 15 in 2025; the dividend was suspended in October
   2025; free cash flow is directed at debt paydown; *"we plan to remodel nearly all of our Outback
   Steakhouse restaurants by the end of 2028."*

That is the strongest honest version. Now the franchise test.

### [E3-03] — the three conditions
- **Needed or desired** — [x] **YES.** People buy restaurant meals and will keep doing so.
- **Thought by its customers to have NO CLOSE SUBSTITUTE** — [ ] **NO, and the company says so in
  its own Item 1.** Verbatim, FY2025 10-K: *"At an aggregate level, all major casual dining
  restaurants in markets in which we operate would be considered competitors of our concepts. We
  also face growing competition from the supermarket industry which offers expanded selections of
  prepared meals. Further, improving product offerings and convenience options from quick-service
  and fast-casual restaurants, and the expansion of home delivery services, together with negative
  economic conditions, could cause consumers to choose less expensive alternatives than our
  restaurants."* And Item 1A: *"our ability to increase our market share within the
  hyper-competitive casual dining segment."* A filer describing its own segment as
  hyper-competitive, naming supermarkets, quick-service, fast-casual and delivery as substitutes,
  and defining its competitive set as *all* major casual dining restaurants, is describing the
  absence of criterion 2, not its presence.
- **Not subject to price regulation** — [x] **YES**, menu prices are unregulated.

**[E3-03] fails on criterion 2.** And the same passage gives the observable proof of all three:
*"The existence of all three conditions will be demonstrated by a company's ability to regularly
price its product or service aggressively and thereby to earn high rates of return on capital"*
**[E3-43]**. BLMN did price aggressively — average check **+19.9%** compounded FY2022-FY2025 — and
earned **0.94%** of revenue in operating income and **5.8%** on net tangible operating assets,
last of the eight filers in the row below. Aggressive pricing plus low returns on capital is the
filed signature of the condition being absent.

### The physical series — the honest one **[E4-55]**
Munger, 2006 Wesco letter, **reproduced with its OCR artifacts per PRIME RULE 1 — the doubled
opening quotation marks, the two apostrophes closing *bounce back*, and the replacement character
standing where the `ff` ligature of *effect* was**:
> *"This decline in physical volume is a serious reverse, not likely to disappear in some
> ""bounce back'' e&#65533;ect. Nor do we expect another sharp rise in prices like the approximately
> 40% rise that recently occurred, holding dollar volume roughly level despite a precipitous drop
> in physical volume."*

He wrote that of Precision Steel's pounds falling 69 million to 46 million while price rises held
dollars level. BLMN's units are guests, and its own MD&A files them, re-struck here from four of
its 10-Ks plus the H1 10-Q:

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 FY2026 |
|---|---|---|---|---|---|---|
| Combined U.S. **traffic** | +20.7% | **(5.3)%** | **(3.1)%** | **(4.4)%** | **(1.4)%** | **(1.8)%** |
| Combined U.S. average check | +9.8% | +9.3% | +4.5% | +3.3% | +1.6% | +3.4% |
| Outback **traffic** | +18.1% | **(6.3)%** | **(4.3)%** | **(4.2)%** | **(1.2)%** | **(2.6)%** |

Compounded FY2022-FY2025: **traffic (13.5)% against average check +19.9%** combined U.S.;
Outback **(15.1)% against +19.3%**. Five consecutive negative traffic periods, and the newest of
them is the two quarters *after* the November 2025 turnaround whose first stated platform is to
*"drive in-restaurant traffic growth."* FY2021's +20.7% is not evidence of a moat: it is the
dining rooms reopening, and **[E3-51]**'s surfing distinction applies — *"when a surfer gets up
and catches the wave and just stays there, he can go a long, long time. But if he gets off the
wave, he becomes mired in shallows."* The wave was the reopening; the shallows are FY2022 onward.

### The inverse metric **[E4-37]** and the untapped-pricing-power class **[E3-33, E5-28]**
*"it's not a great business when you have to have a prayer session before you raise your prices a
penny."* BLMN raised check 19.9% over four years and lost 13.5% of its guests doing it; in FY2025
it took only +0.7% at Outback and traffic still fell. That is the agony end of **[E4-37]**, not the
yawn end. The untapped-pricing-power class **[E3-33]** is explicitly **not available** here:
**[E5-28]** scopes it — *"If you name some business that has incredible pricing power, you're
talking about a business that's a monopoly or a near monopoly"* — and the competitor row shows
seven filers competing for the same guest.

### **[E2-44]**'s two-characteristic test
*"(1) an ability to increase prices rather easily (even when product demand is flat and capacity is
not fully utilized) without fear of significant loss of either market share or unit volume"* —
**fails on the filed traffic series.** *"(2) an ability to accommodate large dollar volume
increases in business … with only minor additional investment of capital"* — **fails**: total
revenues rose 0.1% in FY2025 on $179.9M of capital expenditure and $177.7M of depreciation.

### **[E2-45]** the attacker's test
*"how I would like, assuming I had ample capital and skilled personnel, to compete with it."* With
capital and people I could open a steakhouse across the street; the filings show competitors doing
exactly that and winning — Chili's took **+3.6%** traffic in the year BLMN lost **(1.4)%**. The
answer to the grizzly question is that I would take this fight gladly, which is the wrong answer.

### **[E4-32]** direction, and **[E2-53]** dominance
*"we want the moat widened every year."* The direction here is **narrowing**, on four independent
filed series: traffic negative five periods running; restaurant-level margin **13.3% → 11.7%**;
company-owned U.S. units **970 → 957** in FY2025 alone on the 10-K's own system-wide rollforward
(19 company-owned U.S. openings against 32 company-owned U.S. closures; 19 against 40 counting
franchised units, which closed eight more and opened none), with the MD&A attributing $67.0M of lost sales to *"the closure
of 86 restaurants since December 31, 2023"*; and a **$28,188 thousand goodwill impairment at
Bonefish** in FY2025
plus **$45,137 thousand** of impairment and closing provisions. **[E2-53]**'s dominance class —
*"Once dominant, the newspaper itself, not the marketplace, determines just how good or how bad the
paper will be. Good or bad, it will prosper"* — is the opposite of a filer whose own Item 1A says
its results depend on *"our ability to increase our market share."*

### **[E4-04]**, applied as the framework's 2026-09-20 ruling requires
The ruling says [E4-04] is *"applied as a competence limit, never as a fourth franchise criterion"*,
and that a name which **passes** [E3-03] but whose durability cannot be judged closes UNKNOWABLE.
**That branch is not reached, because [E3-03] itself fails on the filings.** For completeness: the
remodel programme (*"nearly all of our Outback Steakhouse restaurants by the end of 2028"*) is
spending that **defends** the same brand rather than buying its replacement, so it is [E5-23]'s
maintenance obligation and not [E4-04]'s continuously-rebuilt moat. The verdict does not rest on it.

### **[E4-36]** — which of the four causes of extreme success is this?
None of them is operating. There is no extreme maximisation of one variable (Outback's AUV is good,
not extreme); no non-linear combination (four separate brands sharing a back office); no extreme
performance over many factors (the company is 7th of 8 on operating margin and 8th of 8 on return
on net tangible operating assets); and the one wave it caught — the 2021 reopening — it has been
off since 2022.

### **[E4-23]** — key-person and turnaround dependence, recorded HERE as a moat defect
*"if a business requires a superstar to produce great results, the business itself cannot be deemed
great."* The company's own stated path to acceptable results is a **"comprehensive turnaround
strategy"** announced November 2025, supported by *"Strong Management Team: we have the right team
in place to lead our brands through our turnaround initiatives."* **[E2-36]** asks whether the
moat is intact with a *"localized excisable cancer"* or whether **the manager is the plan**. Here
the plan *is* the plan: four platforms, a remodel of nearly the entire Outback estate, and a
dividend suspended to pay for it. That is the *"corporate Pygmalion"* side of [E2-36], and it is
recorded at Q2 as a moat defect exactly as the framework directs, not at Q3 as a strength.

### THE COMPETITOR ROW — required **[E3-28]**
Full workpaper with every accession: `Test Runs/_research 2026-09-21 BLMN/COMPETITOR ROW.md`.
Every figure struck 2026-09-21 from the filer's own most recent 10-K.

| Company | comparable traffic, latest FY | operating margin, latest FY | restaurant-level margin | OI / NTOA* | source (10-K accession) |
|---|---|---|---|---|---|
| **BLMN** (FY2025) | **(1.4)%** U.S. combined; **(1.8)%** H1 FY2026 | **0.94%** | **11.7%** (from 13.3%) | **5.8%** | `0001546417-26-000009` |
| DRI Darden (FY2026) | not disclosed (+4.5% blended comp) | 12.0% | n/d in this form | 34.9% | `0000940944-26-000025` |
| EAT Brinker (FY2026) | **+2.5%** co-owned; Chili's **+3.6%** | 10.7% | 17.8% | 101% | `0000703351-26-000029` |
| TXRH Texas Roadhouse (FY2025) | **+2.8%** | 8.1% | 15.5% (from 17.1%) | 34.7% | `0001104659-26-021292` |
| CAKE Cheesecake Factory (FY2025) | (2.3)% | 5.0% | n/d comparable | 32.8% | `0001104659-26-018643` |
| BJRI BJ's (FY2025) | **+2.8%** | 3.3% | n/d comparable | 9.5% | `0001193125-26-083331` |
| CBRL Cracker Barrel (FY2025) | (3.0)% | 1.6% | n/d comparable | 8.3% | `0001104659-25-093663` |
| RRGB Red Robin (FY2025) | (3.8)% guest count | 0.23% | n/d comparable | 7.0% (unreliable) | `0001628280-26-011733` |

\* NTOA = total assets − cash − goodwill − intangibles ex-goodwill − operating-lease ROU asset −
total current liabilities. **One construction, mine, applied identically to all eight**; it treats
all current liabilities as non-interest-bearing and so flatters every filer equally. BLMN on the
more careful construction (stripping current debt and current lease liabilities first) is **4.53%**.

- **Peers named: 7 of the 9 SEC-registered US casual-dining operators of scale.** Buffett says
  eight **[E3-28]**; with the subject the row holds eight filers. The two left out are named with
  reasons: **DIN** (Dine Brands is almost wholly franchised, so its comparable-traffic series
  measures restaurants that are not in its P&L) and **DENN** (newest 10-K on EDGAR is FY2024, a
  year stale). Nothing was dropped silently.
- **Any peer unavailable?** No. All seven filed and were read. Two disclosure limits, stated:
  **DRI publishes no traffic/check decomposition at all**, so its cell in row 1 is empty on the
  filing and not on my effort; and CAKE, CBRL, BJRI and RRGB publish no restaurant-level margin on
  BLMN's definition, so row 3 carries three filers, not eight. Neither limit changes the reading,
  because BLMN is bottom-two on the metric every filer does publish.
- **Untapped pricing power [E3-33]?** **No.** The opposite: pricing has been taken and guests left.
  Claiming the class would be claiming near-monopoly **[E5-28]**, which the row refutes.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: NARROWING**

### THE ROW'S LIMIT, STATED **[E3-61]**
*"In some businesses, the participants behave like a demented Kellogg. In other businesses, they
don't … I think you'd have to know the people involved …"* The row establishes relative position. It
cannot tell me whether Chili's traffic gain is a permanent share shift or a discount cycle that
reverses. That uncertainty would matter if the verdict rested on the peers' *conduct*. It does not:
the verdict rests on BLMN's own filed traffic series, its own Item 1 substitution language, and its
own returns on capital, each of which fails without reference to what the peers do next.

### WHY THIS IS OUT AND NOT UNKNOWABLE
The separating test **[E4-19]**: *can I name the document that would resolve this?* There is no
missing document. Everything the test needs — the substitution language, the ten-year traffic and
check decomposition, the unit rollforward, the impairments, the returns on capital, and seven
competitors' identical disclosures — is filed and was read. The evidence is here and the business
fails criterion 2 of **[E3-03]**. That is the definition of OUT.

**The cheapness is not permitted to vote here.** The screen's 8.21% bottom-end yield — really about
10.7% once the stale cap is corrected — is a Q5 input, and Q5 does not open. **[E5-42]** keeps the
two judgments apart: business quality is *"the capital actually needed in the business"*, and
*"whether it's a good investment for us depends on how much we pay for that in the end."* Q2 is the
first half. **[E5-35]** is the standing answer to the temptation: *"You can turn any investment into
a bad deal by paying too much. What you can't do is turn any investment into a good deal by paying
little …"*

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  **OUT on the business, at [E3-03] criterion 2 — no close substitute — on the company's own Item 1
  language, its own five-period traffic decline against a 19.9% price rise, and a competitor row in
  which it is 7th of 8 on operating margin and 8th of 8 on return on net tangible operating assets.**

---
⛔ **The file closes here.** Q1 IN, Q2 OUT. Under the hard sequence (operator rule 2) Q3, Q4, Q5 and
Q6 are **not opened**; no valuation is reported. The arithmetic that exists is recorded below the
close, headed as a computation and not a clearance, because the run was dispatched to test the
screen's row and that obligation survives the verdict.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
**NOT OPENED.** Q2 returned OUT. Operator rule 2: *"No Q5 output may be reported unless Q1-Q4 each
show IN"*, and the framework's own instruction is to **stop at the first verdict that is not IN**.
No weight case is declared, no flag is scored, and nothing here may be read as a finding about
Bloomin' Brands' managers in either direction. **VERDICT: not reached.**

*One procedural note, because the queue's standing rule for this gate exists and the run should
record that it was not skipped for convenience: the standing instruction is to pull the latest 8-K
EX-99.1 before scoring [E4-29] and [E4-22]'s third flag. That pull was **not made**, because the
gate was not opened. If this file is ever reopened — see the reversal condition below — the 8-K
exhibits to `0001546417-26-000030` (2026-08-05) and `0001546417-26-000023` (2026-05-06) are the
first documents to read, and the FY2025 10-K's own non-GAAP section (Adjusted restaurant-level
operating margin, Adjusted income from operations, Adjusted net income, Adjusted diluted EPS) is
the place [E4-29] would be tested.*

## Q4 — WILL IT SURVIVE?
**NOT OPENED.** Q2 returned OUT. **VERDICT: not reached.**

---
⛔ **Q5 does not open.** Q2 is OUT. UNRESEARCHED and UNKNOWABLE both close the file; OUT closes it
permanently.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**NOT OPENED, AND NO VALUATION IS REPORTED.** Operator rule 3 governs everything in the next
section. **VERDICT: not reached.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**NOT OPENED** — there is no position and none is contemplated. **VERDICT: not reached.**
The reversal condition, in words, is recorded in the fold section below in place of a price alert;
a price band on a name that failed on the business would be a category error (the QLYS ruling,
2026-09-07).

---

# COMPUTATION — NOT A CLEARANCE
**Operator rule 3.** *Any valuation math produced before Q1-Q4 close must be headed*
**"COMPUTATION — NOT A CLEARANCE"** *and may carry no entry language.* Q1-Q4 did **not** close; Q2
is OUT. Nothing below is a valuation, a ranking, a yield to act on, or a statement that this
security is cheap. It exists for one reason: the run was dispatched to **reproduce the screen row's
arithmetic and say whether it reproduces**, and that obligation to the screen survives the verdict
on the business.

## 1. THE SCREEN ROW, FIELD BY FIELD — IT DOES NOT REPRODUCE
The row as dispatched:
`BLMN,"Bloomin' Brands, Inc.",903,74,159,1.141,$74M to $159M,…,0.0821,0.0286,0.0179,…`

| field | screen | rebuilt 2026-09-21 | reproduces? |
|---|---|---|---|
| `cap_m` | 903 | **690.9** ($8.07 × 85,620,917 cover shares) | **NO — 30.7% high** |
| `oe_bottom_m` | 74 | **60.0** (`3y_capex`) | **NO — 19% high** |
| `oe_top_m` | 159 | **150.3** (`5y_da`) | **NO — 5.5% high** |
| `spread` | 1.141 | **1.505** | **NO** |
| `yield_bottom` | 0.0821 | **0.0868** (60.0 ÷ 690.9) | no, and the two errors partly cancel |
| `vs_sovereign` | 0.0286 | 0.0868 − 0.0534 = **0.0334** | no |
| `growth_required` | 0.0179 | 0.10 − 0.0868 = **0.0132** | no |
| `years_filed` | 16 | **16** (FY2010 … FY2025) | yes |
| `newest_filing` | 2025-12-28 | 2025-12-28 | yes |
| `newest_periodic` | 2026-06-28 | 2026-06-28 | yes |

The rebuild ran `Screens/floor_screen.py`'s own `owner_earnings()` against companyfacts pulled fresh
on 2026-09-21, and returned exactly four constructions:
**`3y_capex` 60.0 · `3y_da` 124.8 · `5y_capex` 108.4 · `5y_da` 150.3 ($M).**
So the published 74/159 was computed on an earlier cut of the same tagged data. The **cap** error is
independent and larger: it is a stale price, ~$10.55 a share against a 2026-09-18 close of $8.07.

## 2. THE ROW'S TWO IMPERATIVES, TESTED RATHER THAN INHERITED
Per the TAIL-TRIAGE CORRECTION of 2026-09-12, both were read as unlabelled and tested.

**(a) `level_note_oe` — "STEP DOWN - the series has changed level".** **CONFIRMED, and the screen
understates it: the series changes level TWICE, and both are disclosed events.**
- **2020:** dining rooms closed. FY2020 operating cash fell to $138.8M from $317.6M.
- **2024-12-30:** the **Brazil Sale Transaction**. Brazil is reported as **discontinued operations
  for all periods** in the FY2024 and FY2025 10-Ks. The filed cash-flow statement
  (`0001546417-26-000009`) separates them: operating cash of **discontinued** operations was
  **$78,255 / $12,132 / $748** thousand in FY2023 / FY2024 / FY2025, and **capital expenditures were
  restated** from $324,255 to $282,229 (FY2023) and from $219,691 to $192,791 (FY2022).
  **A mean drawn across FY2021-FY2025 is therefore measuring two different companies.**

**(b) `spread_caveat` — "4-construction width only (3y/5y × two capex ends): CANNOT see variation
older than the 5-year window; rebuild it [E4-25]".** **CONFIRMED. Rebuilt three ways below.**

## 3. THE REBUILD [E4-25]
*"Working with a range of possibilities is the better approach … Usually, the range must be so wide
that no useful conclusion can be reached."*

**(i) Ten windows on the mixed-perimeter tagged series** (`tools/run.py`'s own construction, 3 to
16 years, both capex ends), $M:

| window | 3y | 4y | 5y | 6y | 7y | 8y | 10y | 12y | 14y | 16y |
|---|---|---|---|---|---|---|---|---|---|---|
| capex end | 109.1 | 127.3 | 144.8 | 111.3 | 109.1 | 102.0 | 99.6 | 104.4 | 106.3 | 105.1 |
| D&A end | 162.6 | 178.1 | 193.5 | 167.3 | 162.1 | 149.3 | 150.0 | 151.0 | 152.1 | 154.2 |

Full width **99.6 to 193.5**, a spread of **94%** — which is **narrower** than the published 114%.
**So on the screen's own mixed-perimeter series, adding eleven more windows does NOT widen the
range, and the caveat's stated direction does not bite.** It bites on construction (ii) below, where
the perimeter is fixed: **the caveat is right, but for a reason it does not name.** This is exactly
what the TAIL-TRIAGE CORRECTION requires a run to check rather than inherit.

**(ii) The perimeter-consistent series — continuing operations only, which is the only version that
divides the same company by the same company.** All six inputs per year taken from the filed
cash-flow statements in `0001546417-25-000034` and `0001546417-26-000009`, $ thousands:

| FY | OCF continuing | SBC | capex | D&A | (OCF−SBC)−capex | (OCF−SBC)−D&A |
|---|---|---|---|---|---|---|
| 2022 | 348,332 | 16,282 | 192,791 | 149,900 | **139,259** | **182,150** |
| 2023 | 454,166 | 11,690 | 282,229 | 169,266 | **160,247** | **273,210** |
| 2024 | 216,000 | 7,484 | 220,737 | 175,580 | **(12,221)** | **32,936** |
| 2025 | 275,946 | 7,780 | 179,924 | 177,680 | **88,242** | **90,486** |

means: **4y 93.9 / 144.7 · 3y 78.8 / 132.2 · 2y 38.0 / 61.7 · FY2025 alone 88.2 / 90.5** ($M).
**Range on the only internally consistent perimeter: $38M to $145M — a spread of 281%, against the
published 114% and the ten-window mixed-perimeter 94%.** The screen's rebuild imperative is
therefore **upheld**, and the thing hiding the width was not the length of the window at all: it is
that inside the published series the operating-cash line and the capital-expenditure line describe
two different companies on either side of 2024-12-30.

**(iii) The lease question the brief asked.** BLMN leases nearly all its boxes. The lease note
discloses *"Leased assets obtained in exchange for new operating lease liabilities"* of
**$57,211 / $91,305 / $74,539** thousand in FY2025 / FY2024 / FY2023, plus finance-lease additions
of **$3,386 / $4,038 / $6,480**. Neither tool counts either. Treating both as capital committed,
the FY2023-FY2025 mean owner earnings is **−$0.2M** — i.e. **zero**. That construction is not
asserted as the right one; it is shown because **[E4-25]** says the width of the range is the
finding, and this is the width.

**(iv) Two constructions the brief warned about, TESTED AND REFUTED for BLMN.**
- **Capitalised software missing from capex** (the DRI defect). **Does not apply.** BLMN's filed
  consolidated statement of cash flows carries **one** investing line for fixed assets,
  *"Capital expenditures"*, and no separate capitalised-software line in any of FY2023-FY2025.
- **Working capital omitted.** **Does not apply.** BLMN's working-capital movements sit inside
  operating cash flow as seven separate change-in-assets-and-liabilities lines; the OCF-based
  construction already nets them, which is why the framework's CONVENTION uses OCF. FY2025 they net
  to **+$5,476** thousand — 2% of operating cash, not a swing factor. `floor_screen`'s
  `working_capital_flag` returned **None** for BLMN, and opening the lines confirms it.

## 4. THE FLOOR, AND WHY IT IS NOT A VERDICT
On the widest construction the arithmetic sits above **[E4-28]**'s ~10% honest expectancy and above
the **5.34%** sovereign; on the narrowest (lease-inclusive) it sits at zero. **This decides nothing.**
Q5 never opens, and the reason is the corpus's own ordering **[E5-42]**: business quality first,
price second. Recording the yield here and calling it an opportunity would be exactly the error
operator rule 9 exists to prevent — *"the analyst holding a position has an incentive to clear it."*

## 5. TOOLING DEFECTS FOUND
1. **`tools/run.py` mixes accounting perimeters on any filer with discontinued operations, in the
   flattering direction.** `floor_screen.py` has carried `ocf_continuing()` since the AMD run of
   2026-09-07 — it removes separately-tagged discontinued-operations cash from OCF. **`run.py` has
   no such function**; its `OCF` tag list lets the *total* tag win, while its capex and D&A lists
   resolve to the *restated continuing-operations* figures from the newest 10-K. For BLMN FY2023
   that pairs **$532.4M of operating cash (which includes $78.3M Brazil earned)** with **$282.2M of
   capex that excludes Brazil**, overstating that year's conservative end by **$78.3M, or 49%.**
   This is the "fix applied to one path and not its twin" hazard that `floor_screen.py`'s own
   comments say has been found three times in two days — found a fourth time here, in the other
   direction. **No tool was changed by this run; the defect is reported, not patched.**
2. **`Screens/floor_screen.py` mixes the perimeter the other way, conservatively.** Its
   `ocf_continuing()` correctly returns continuing-operations OCF, but `da_annual()` and
   `capital_acquired()` take the **largest resolving value per year**, which for BLMN FY2022 and
   FY2023 returns the **pre-restatement, Brazil-inclusive** capex ($330.7M vs $282.2M for FY2023)
   and D&A ($191.2M vs $169.3M). The max rule is right for the MCD subcomponent case and wrong
   here. The direction is conservative, so it does not flatter — but it is still not one company,
   and it is part of why the published 74/159 cannot be reproduced.
3. **The published row's `cap_m` was ~24% stale in price.** Not a code defect; a refresh-date one.
   It is worth recording because `cap_m` is the denominator of four downstream fields, and a stale
   cap on a falling stock makes a name look **less** cheap than it is, which is the direction that
   causes a name to be *skipped*, not bought.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, file closed. Q3-Q6 recorded
      as **not opened** with the reason, which is the hard sequence, not an omission.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on
      the filed FY2025 income statement and Item 1 alone.
- [x] Every UNRESEARCHED verdict names the artifact — **there are none.**
- [x] Every UNKNOWABLE verdict states what cannot be known — **there are none.** The Q2 verdict is
      OUT, and [E4-19]'s separating test was asked aloud: no document is missing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked by hand
      (FY2025 operating cash flow $276,694 against the filed statement, plus the continuing /
      discontinued split of $275,946 / $748 that neither tool reads correctly).
- [x] Owner earnings on a multi-year mean; windows stated (ten of them, plus a perimeter-consistent
      four-year rebuild); capex band disclosed as a judgment — **and reported ONLY under the
      COMPUTATION — NOT A CLEARANCE heading**, because Q4 never opened.
- [x] Competitor row filled — eight filers, each from its own most recent 10-K with the accession
      recorded; two peers excluded with named reasons; two disclosure limits stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury daily
      par yield curve), dated 09/18/2026, struck 2026-09-21.
- [x] Value stated as a round-number range, not a point estimate — **not applicable; no value is
      stated**, because Q5 did not open.
- [x] One bar chosen, not both — **not applicable; neither bar was used.** Windage count: **zero.**
      No conservatism was applied anywhere, because no valuation was made.
- [x] Prices dated; aggregator used for the live quote only and flagged (Yahoo, close of
      2026-09-18).
- [x] Run committed to git — after Step 0, after Q1, after Q2, and at the fold.

## REGISTER
- Verdict: [ ] IN  [x] **OUT (about the business)**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
- **One line:** Bloomin' Brands fails **[E3-03] criterion 2** on its own Item 1 — *"At an aggregate
  level, all major casual dining restaurants in markets in which we operate would be considered
  competitors of our concepts"* — with combined U.S. traffic down in five consecutive filed periods
  and **(13.5)% compounded FY2022-FY2025** against average check **+19.9%**, a restaurant-level
  margin falling 13.3% → 11.7%, and a position of **7th of 8 on operating margin and 8th of 8 on
  return on net tangible operating assets** in a competitor row struck from eight filers' own 10-Ks.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
- **REVERSAL CONDITION, recorded in words in place of a price alert** (gate-clearers only get
  alerts; the QLYS ruling of 2026-09-07). This file reopens only on a change in the **business**,
  never on a change in the price. The named test: **four consecutive quarters of positive Combined
  U.S. comparable-restaurant traffic, with average check growth no greater than traffic growth**,
  reported in BLMN's own 10-Q MD&A traffic table — i.e. guests returning rather than prices rising —
  **accompanied by a restaurant-level operating margin back above 13.3% and a GAAP operating margin
  that moves BLMN out of the bottom two of the competitor row.** Anything short of that is the
  turnaround working on the P&L without changing the answer to [E3-03] criterion 2, which is what
  the file turned on. Price is not a reopening condition at any level **[E5-35]**.
