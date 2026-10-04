# Company Run — Archer-Daniels-Midland Co (ADM) — 2026-09-21
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
- rate **5.34%** · date **2026-09-18** (the most recent published print; 09-21 is a Sunday)
  · source **US Treasury daily par yield curve, 30-year par yield**, struck for this run from
  the issuing authority (`home.treasury.gov` daily-treasury-rates CSV, via `tools/sources.py`).
  **FRED DGS30 was not used.** The rate is NOT inherited from the brief — the brief withheld it.
- FX / ADR: none. ADM reports and earns predominantly in USD; the quote currency and the
  earnings currency agree. (Foreign-currency translation moved equity $450M in 2025 — a real
  exposure, recorded at Q4, not an earnings-currency problem.)

**Price and share count, re-struck by this run — the screen's cap is not taken on trust:**
- price **$85.18**, close of **2026-09-18**, Yahoo Finance chart endpoint — *aggregator, used
  for the live quote only and flagged as such* (operator rule 5). Raw response saved to
  `Test Runs/_research 2026-09-21 ADM/price_yahoo_raw.json`.
- shares **481,959,583**, **Common Stock, no par value — a SINGLE class**, read off the cover
  of the **10-Q for the period ended 2026-06-30, filed 2026-08-04, accession
  0000007084-26-000042**, as-of date 2026-07-30 (`Screens/cover_shares.py ADM`). No split in
  the period; no second class; no convertible preferred on the balance sheet.
- **market cap, hand-struck = 481,959,583 × $85.18 = $41,053M.**
- **Against the screen's $39,328M: +$1,725M, +4.4%.** The difference is a price-date
  difference, not a count error — the screen's cap was struck on an earlier quote against the
  same single-class cover count. **The screen's cap survives the re-strike here.** It is the
  screen's OWNER-EARNINGS column that does not survive (Q4).

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **primary: FY2025 Form 10-K, period 2025-12-31, filed 2026-02-17, accession
  0000007084-26-000011** (`adm-20251231.htm`).
- **secondary: Form 10-Q, period 2026-06-30, filed 2026-08-04, accession 0000007084-26-000042**
  — the newest periodic filing.
- also read, and each one changes the reading: **FY2024 10-K** (0000007084-25-000011),
  **FY2023 10-K** (0000007084-24-000009), **FY2023 10-K/A** (0000007084-24-000051),
  **FY2022 10-K** (0000007084-23-000010), **FY2021 10-K** (0000007084-22-000008),
  **FY2020 10-K** (0000007084-21-000008), **FY2018 10-K** (0000007084-19-000012),
  **FY2016 10-K** (0000007084-17-000008), **FY2014 10-K** (0000007084-15-000005);
  **NT 10-K filed 2024-03-01** (0001193125-24-054362); **8-K Item 5.02 filed 2024-01-22**
  (0001193125-24-011608); **8-K Item 4.02 filed 2024-11-05** (0000007084-24-000034);
  **8-K EX-99.1 earnings release filed 2026-08-04** (0000007084-26-000040).
- **figure cross-checked against the filed statement:** FY2025 net cash provided by operating
  activities. XBRL `NetCashProvidedByUsedInOperatingActivities` = **$5,452M**; the Consolidated
  Statements of Cash Flows in the FY2025 10-K reads *"Net cash provided by operating activities
  | 5,452 | 2,790 | 4,460"*. **Agrees.**
- **second cross-check, computed rather than read:** total assets $52,389M less total current
  liabilities $19,534M, total long-term liabilities $9,828M and temporary equity $287M =
  **$22,740M**, which is the filed Total Shareholders' Equity to the dollar.
- **A THIRD CROSS-CHECK THAT DID NOT AGREE, AND IT IS THE FINDING OF THIS RUN.** The FY2016
  10-K reports **"Total Operating Activities | 1,475"** for FY2016. The FY2018 10-K reports
  **"Total Operating Activities | (6,508)"** for the same FY2016. Both are ADM's own filed
  statements. The reconciling line is **"Deferred consideration in securitized receivables |
  (7,838) | (8,177) | (8,063)"** for 2018/2017/2016, which the FY2018 10-K added to operating
  activities on adoption of the securitization-classification guidance, with an exactly equal
  and opposite amount in **investing**. ADM says so in its own MD&A: *"Deferred consideration in
  securitized receivables of $4.6 billion and $7.7 billion in 2020 and 2019, respectively, was
  offset by the same amounts of net consideration received for beneficial interest obtained for
  selling trade receivables."* (FY2020 10-K.) **Every "negative operating cash flow" year in
  ADM's tagged history — 2016 through 2020 — is a classification artifact, not a business fact.**
  See the rebuilt series at Q4 and the tooling note at the end.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** ADM buys crops from farmers,
moves them, stores them, and turns some of them into things worth more than the crop. Three
segments, and they make money three different ways.

**Ag Services and Oilseeds (FY2025 revenue $61,571M, 77% of the total; segment operating
profit $1,614M).** Two distinct activities under one name. *Origination and merchandising* is
a spread business: buy grain at a country elevator, pay to move it by truck, rail, barge and
ship, sell it at a port or to a processor, and keep the difference between the delivered price
and the acquired price less the freight. The inventory is hedged on the futures market, so the
flat price is not the earnings driver — the **basis** and the **freight spread** are. *Crushing*
is a conversion business: buy a soybean, crush it, sell the meal and the oil. The margin is the
difference between what the beans cost and what the meal plus oil fetch — the **crush spread**
— which is set on exchanges ADM does not control and which ADM's own MD&A says was
*"compressed"* in 2025.

**Carbohydrate Solutions ($10,737M revenue; $1,211M profit).** Wet and dry corn milling. Buy
corn, separate it into starch, sweetener, oil and protein, or ferment it into ethanol. Ethanol
is sold into a fuel market whose demand is set by a blending mandate. Same shape as crushing:
a conversion spread between an input priced on an exchange and outputs priced on exchanges.

**Nutrition ($7,512M revenue; $417M profit).** Flavours, colours, plant proteins, probiotics,
premix feed, pet treats. This is the only leg that is sold on specification rather than on
price, and it is the smallest — **9.4% of revenue and 12.9% of segment operating profit** in
FY2025 — with a **5.6% operating margin** against Ag Services and Oilseeds' 2.6% and
Carbohydrate Solutions' 11.3%.

**And a fourth thing, which is not a segment and is not small.** ADM Investor Services is a
registered futures commission merchant. It sits in "Other Business" and it parks **$8,432M of
segregated cash and investments** on ADM's balance sheet against **$8,919M of payables to
brokerage customers** — customer money, on both sides. Other Business earned $298M pre-tax in
FY2025 and Corporate cost $2,049M. **16% of ADM's total assets are its brokerage customers'
money**, which matters at Q4 and which makes every balance-sheet ratio read wrong if you skip it.

**So the money comes from three spreads and a float.** None of the three spreads is set by
ADM. What ADM sells is the ability to be physically present at both ends of one — to own the
elevator on the river, the barge, the port terminal, the crush plant and the working capital
to carry the crop between them.

**The scarce input this business controls.** Not the crop, which ADM buys *"from thousands of
growers, grain elevators, and wholesale merchants"* under *"short-term (less than one year)
agreements or on a spot basis"*, and for which the filing says *"The Company is not dependent
upon any particular grower, elevator, or merchant."* Not a brand: the whole company's
trademarks, brands, recipes and other intellectual property carry a **net book value of $579
million** at 2025-12-31 against $52,389M of assets, and *"More than 95% of these intangibles
are in the Nutrition segment which is not materially dependent upon any individual trademark,
brand, recipe or other intellectual property."* The scarce input is the **irreplaceable
physical network** — river elevators, port terminals, rail fleets, barges and crush plants
sited where the crop is — plus the **balance sheet that carries $10,369M of inventory** through
a harvest. Both are ownable. Neither is exclusive: Bunge, Cargill, Louis Dreyfus and CHS own
the same kind of network on the same rivers.

**Will the fundamentals look broadly the same in ten years?** Yes, and this is the honest
answer in ADM's favour. People eat; livestock eat meal; soybeans are crushed; corn is milled.
The physical series says the volumes are already flat: **oilseeds processed 36,324 thousand
metric tons in 2025 against 36,308 in 2018**, and **corn processed 18,525 against 22,343** over
the same seven years. A business whose throughput has not moved in a decade is stable in
character even where it is not growing, which is what **[E3-31]** asks — *"relatively simple
and stable in character"*.

**The [E4-46] test, asked honestly.** Is this a named filing inside an understood business, or
a business that would take months of study? I can state the three spreads, name the network,
read the cash and find the brokerage float on the face of the balance sheet. It took reading
nine 10-Ks to find the securitization artifact at Step 0, but that was a **document retrieval**
problem, not a comprehension problem — which is precisely the line [E4-46] draws.

**Q1 is IN, and it is IN on the ground that the business is legible, not that it is good.** The
legibility finding carries two things forward that are NOT used to close this gate: the spreads
are set outside the company (Q2), and the reported operating-cash line has been restated by a
classification change and is dominated by working capital (Q4).

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### FIRST, THE CASE AT FULL STRENGTH — built to be worth attacking

**The scale-and-network case, and it is a real one.** ADM is one of four companies on earth
that can originate a crop in Brazil, finance it, barge it down a river, load it onto a
Panamax, crush it in Europe and sell the meal to a feed mill, all on its own balance sheet.
The network is a century old and is sited where the crops are: 41,496 employees, subsidiaries
in 75 countries, $11,179M of net property, plant and equipment, $10,369M of inventory carried
through a harvest, and $12.3 billion of committed credit lines to finance the carry. Nobody
builds a second one. A new entrant cannot buy the elevator that already sits on that bend of
the Illinois River. **And the scale is real in the physical series**: 36,324 thousand metric
tons of oilseeds and 18,525 of corn processed in 2025.

**Plus the option on the regime.** Ethanol demand is set by a blending mandate; biodiesel
carried the Blenders' Tax Credit through 2024 (**$316 million of benefit recorded in FY2024**,
the 10-K says so as a number) and the Clean Fuel Production Credit from 2025. A policy that
guarantees a buyer for a corn product is worth money.

### THEN THE THREE CRITERIA [E3-03], AND THE FILING ANSWERS TWO OF THEM AGAINST THE COMPANY

- **(1) Needed or desired — YES.** [x] People eat. Livestock eat meal. This is not in doubt.
- **(2) Thought by its customers to have NO CLOSE SUBSTITUTE — NO.** [ ] **ADM's own Risk
  Factors say the opposite, in the company's own words:** *"Many of the products bought and
  sold by the Company are global commodities or are derived from global commodities that are
  **highly price competitive and, in many cases, subject to substitution**"* (FY2025 10-K,
  Item 1A). A soybean meal buyer does not care whose meal it is. The MD&A says the same thing
  about price: *"changes in selling prices move in relationship to changes in prices of the
  commodity-based agricultural raw materials."* ADM does not set a price; it passes one
  through.
- **(3) Not subject to price regulation — YES, but it cuts the wrong way.** [x] Prices are not
  regulated. They are set on the CBOT and on the crush and ethanol boards, which is worse for
  the owner than regulation: **[E2-59]** is explicit that administered pricing *floors* a
  commodity business, and the one thing ADM's earnings actually do lean on — biofuel policy —
  is exactly that borrowed floor. The FY2025 MD&A names the withdrawal as the cause of the bad
  year: *"the deferral of U.S. biofuel policy … negatively impacted sales volumes and margins."*
  **The moat belongs to the regime, and "That day is gone" is how [E2-59] says it ends.**

**Criterion (2) fails on the filer's own sentence. [E3-03] is a conjunctive test. It is failed.**

### THE COMMODITY DOCTRINE, WHICH IS THE GOVERNING TEXT HERE **[E2-58]**

> *"persistent over-capacity without administered prices (or costs) equals poor profitability"*
> … long-term profitability is set by *"the ratio of supply-tight to supply-ample years"* … the
> one exception is *"a cost advantage that is both **wide and sustainable** … By definition
> such exceptions are few."*

**ADM's Risk Factors describe [E2-58]'s over-capacity equation as a live mechanism, unprompted:**
*"Pricing of the Company's products is partly dependent upon **industry processing capacity**,
which is impacted by competitor actions to **bring idled capacity on-line, build new production
capacity** or execute aggressive consolidation."* That is the glut mechanism, written by the
company, in the risk factor it files every year.

**The supply-tight / supply-ample ratio is visible in ADM's own decade.** Return on average
equity capital employed **[E2-01]**, computed from the filed statements:

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| net earnings $M | 1,279 | 1,595 | 1,810 | 1,379 | 1,772 | 2,709 | 4,340 | 3,483 | 1,800 | **1,078** |
| avg equity $M | 17,548 | 17,752 | 18,659 | 19,111 | 19,624 | 21,265 | 23,412 | 24,231 | 23,162 | 22,459 |
| **ROE** | 7.3% | 9.0% | 9.7% | 7.2% | 9.0% | 12.7% | **18.5%** | 14.4% | 7.8% | **4.8%** |

Ten-year mean **10.0%**; five-year mean **11.6%**. **[E2-42]**'s red light — *"Red lights
should start flashing if the five-year average annual gain falls much below the return on
equity earned over the period by American industry in aggregate"* — is not flashing on the
five-year window, because 2021-23 was a supply-tight run (Ukraine, drought, a biofuel bid). It
is flashing on the ten-year one, and on the two most recent years. **[E3-46]** asks the second
question about the business as a number — *"the best businesses, by definition, are going to
be businesses that earn very high returns on capital employed over time"* — and 10% over a
decade, from the largest balance sheet in the industry, is not that number.

### THE COMPETITOR ROW — REQUIRED [E3-28], and it is what settles this gate

Same metric (**net earnings ÷ average shareholders' equity, [E2-01]**), same window
(**FY2021-FY2025, the five-year default [E2-42]**), **filing-sourced, every cell**. Revenue and
margin added because a merchandiser's margin is the shape of the business.

| Company | FY2025 revenue | FY2025 net margin | **ROE 2021** | **2022** | **2023** | **2024** | **2025** | **5-yr mean ROE** | source |
|---|---|---|---|---|---|---|---|---|---|
| **ADM (subject)** | **$80,269M** | **1.34%** | 12.7% | 18.5% | 14.4% | 7.8% | **4.8%** | **11.6%** | FY2025 10-K, acc 0000007084-26-000011 |
| **BG Bunge Global** | $70,329M *(perimeter note below)* | 1.16% | 29.6% | 18.9% | 22.3% | 11.0% | **6.3%** | **17.6%** | FY2025 10-K, acc 0001628280-26-009842 |
| **CHS Inc** (co-op, FY to 31 Aug) | $35,463M | 1.69% | 6.2% | 18.2% | 19.1% | 10.4% | **5.5%** | **11.9%** | FY2025 10-K, CIK 0000823277 |
| **ANDE The Andersons** | $11,009M | 0.87% | 10.2% | 11.5% | 8.2% | 8.6% | **7.3%** | **9.2%** | FY2025 10-K, CIK 0000821026 |
| **INGR Ingredion** | $7,219M | 10.10% | 3.9% | 15.8% | 19.2% | 17.6% | **18.0%** | **14.9%** | FY2025 10-K, acc 0001628280-26-008603 |
| **DAR Darling Ingredients** | $6,136M | 1.03% | 21.1% | 20.8% | 15.4% | 6.2% | **1.4%** | **13.0%** | FY2025 10-K, CIK 0000916540 |
| **Tate & Lyle plc** (UK, FY to 31 Mar 2026) | **£2,006m** *(sterling, unconverted)* | 4.89% | — | — | — | — | **6.2%** | *one year, restructured perimeter* | FY26 results statement, 2026-05, company IR |
| **Cargill Inc.** | **UNRESEARCHED — UNOBTAINABLE** | | | | | | | | **private; files nothing with the SEC** |
| **Louis Dreyfus Company B.V.** | **UNRESEARCHED — UNOBTAINABLE** | | | | | | | | **private; files nothing with the SEC** |

**Peers named: 7 obtained, 2 named and unobtainable, of an industry with 6 to 8 real global
participants.** Buffett says eight **[E3-28]**; I took seven and disclosed the two I could not.

**The three disclosed limits in that row, stated rather than smoothed:**

1. **Bunge's perimeter is not ADM's.** Bunge completed its combination with Viterra on
   **2 July 2025**, so FY2025 carries six months of it. The 10-K quantifies both halves: *"Net
   sales includ e $ 15.3 billion attributable to Viterra for the year ended December 31, 2025"*
   *(the space inside "include" is an artifact of the filer's inline-XBRL tagging and is
   transcribed here rather than smoothed — PRIME RULE 1)*, and the pro-forma full-year net
   sales are **$89,507M (2025) and $93,932M (2024)**. **On a full-year basis the combined
   Bunge-Viterra is LARGER than ADM.** Bunge's equity also nearly doubled mid-year
   ($9,913M → $15,904M) on stock issued for Viterra, which is why its FY2025 ROE is struck on
   average equity and why 6.3% is the honest comparable rather than a like-for-like operating
   read. *(The resume state records that stock consideration in an acquisition perimeter does
   not resolve undimensioned in companyfacts — a source limit already tested, not re-tested
   here. It did not bite: Bunge states the perimeter in words and in numbers in its own 10-K.)*
2. **Tate & Lyle is no longer in ADM's business, and that is itself the finding.** It **sold
   Primient**, its US corn wet-milling arm, in June 2024, and combined with CP Kelco in
   November 2024. The one peer with the option to leave the commodity end **left it**, and its
   reported operating margin is now 9.0% on £2,006m. One year only, on a restructured
   perimeter: I do not average it with the others and I do not convert the sterling.
3. **Cargill and Louis Dreyfus file nothing.** With Bunge and ADM they are the traditional
   "ABCD" of global grain. **Two of the four cannot be measured.** That is a disclosed limit of
   the row, not a silent omission, and it caps how strong any relative-position claim from this
   row can be. *(It does not cap the claim actually made below, which is a NEGATIVE one and
   needs no missing cell to stand.)*

### WHAT THE ROW SAYS, AND IT IS THE VERDICT

**The returns move together, and they move with the crop cycle, not with the company.** In
FY2022-23 every merchandiser in the row earned 15-22%. In FY2025 ADM earned 4.8%, Bunge 6.3%,
CHS 5.5%, Andersons 7.3% and Darling 1.4%. That is **[E2-58]**'s *"ratio of supply-tight to
supply-ample years"* rendered as five independent income statements. It is not five moats
narrowing simultaneously; it is one cycle.

**And the decisive cell: the largest player does not earn the best return.** ADM's five-year
mean ROE of **11.6%** sits *below* Bunge's 17.6%, Ingredion's 14.9% and Darling's 13.0%, and
barely above CHS's 11.9%. **If scale in this industry were the "cost advantage that is both
wide and sustainable" that [E2-58] names as the one exception, the biggest balance sheet would
earn the highest return. It earns a middling one.** The exception is claimed and refuted on
filed figures, which is exactly what the competitor row exists to do — a moat is a claim about
*relative* position **[E3-28]** and cannot be evidenced from one company's numbers.

**The one name in the row that does not track the cycle is the one that is not a
merchandiser.** Ingredion earned **18.0% in FY2025 on a 10.1% net margin** while every
merchandiser in the row was at or under 7.3% on margins of 0.9-1.7%. ADM's own equivalent leg,
Nutrition, is **9.4% of revenue and 12.9% of segment operating profit**. The good business is
visible inside ADM and it is one-eighth of the company.

### THE OTHER Q2 TESTS, EACH ANSWERED

- **The two-characteristic test [E2-44].** Can ADM raise prices *"even when product demand is
  flat and capacity is not fully utilized"*? **No** — the MD&A says selling prices *"move in
  relationship to changes in prices of the commodity-based agricultural raw materials."* Can it
  grow dollar volume *"with only minor additional investment of capital"*? **No** — gross
  profit is $5.0bn on $80.3bn of revenue (**6.2%**) and net earnings are $1,078M (**1.34%**),
  so every extra dollar of throughput must be financed at full commodity cost through inventory
  and receivables. **Both characteristics fail.**
- **The agony metric [E4-37].** *"you can almost measure the strength of a business over time
  by the agony they go through in determining whether a price increase can be sustained."*
  ADM does not hold a pricing meeting for soybean meal at all. There is no price to raise. The
  metric returns its worst possible reading: the question is not even askable.
- **Untapped pricing power [E3-33], scoped by [E5-28].** Claiming this class is claiming
  *"a monopoly or a near monopoly"*. The row has at least six other global participants, two of
  them unmeasurable and one of them now larger. **Not claimed.**
- **The dominance class [E2-53]** — *"Once dominant … Good or bad, it will prosper."* ADM is
  large and is not dominant: it is the biggest of four peers who set each other's prices.
  **Not in the class.**
- **The attacker's test [E2-45].** *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* I would not build a second river network — and I would not
  need to. I would buy Viterra and be bigger by Tuesday, which is precisely what Bunge did on
  2 July 2025 for stock and cash. **A moat a competitor can out-scale with one cheque is not a
  moat.**
- **Direction outranks existence [E4-32]** — is the moat *widening every year*? **No.** ROE has
  fallen three consecutive years (14.4% → 7.8% → 4.8%) while the scale-leadership position was
  lost to the Bunge-Viterra combination.
- **Where units exist, monitor units [E4-55].** They exist here and they are the honest series:

  | thousand metric tons | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | **Oilseeds processed** | 33,817 | 33,788 | 34,733 | **36,308** | 36,271 | 36,565 | 35,125 | 32,952 | 34,899 | 35,719 | **36,324** |
  | **Corn processed** | 23,126 | 22,273 | 22,700 | **22,343** | 22,079 | 17,885 | 19,126 | 18,558 | 18,067 | 18,541 | **18,525** |

  **Oilseed throughput in 2025 is 16 thousand tons above 2018 — seven years, 0.04%. Corn
  throughput is 17% BELOW 2018 and has not recovered from the 2020 step down.** This is
  [E4-55]'s shape — *"a serious reverse, not likely to disappear in some 'bounce back'
  effect"* — and the physical series is the honest one. **The counter-reading, stated fairly:**
  part of the corn decline is a deliberate retreat from low-margin grind, and ADM says it runs
  *"at or near capacity, adjusting facilities individually … to react to the current margin
  environment."* Both readings are carried. Neither produces growth.
- **The four causes of extreme success [E4-36].** ADM's good years came from **wave-riding** —
  a war, a drought and a biofuel bid, all exogenous. **[E3-51]**: *"when a surfer gets up and
  catches the wave and just stays there, he can go a long, long time. But if he gets off the
  wave, he becomes mired in shallows."* The 18.5% ROE of 2022 and the 4.8% of 2025 are the same
  company with the same assets. **A surfing run is not a moat; the advantage lives in the wave.**
- **[E3-61]'s limit on the row, stated.** *"In some businesses, the participants behave like a
  demented Kellogg. In other businesses, they don't … I think you'd have to know the people
  involved."* The row shows position; it cannot show conduct. ADM's own risk factor expects the
  demented behaviour (*"bring idled capacity on-line, build new production capacity"*) and I
  cannot predict it. **This limit does not rescue the gate**: it would matter if the verdict
  rested on forecasting competitor conduct, and it does not. It rests on [E3-03] criterion (2)
  failing in ADM's own sentence.
- **Key-person dependence [E4-23]:** none found. This is not a business that requires a
  superstar, and recording that is not a compliment — it is the absence of one more defect.

### THE VERDICT FORM [E4-04] TAKES — checked, and it is NOT the perimeter close

The ruling of 2026-09-20 says a name that **passes [E3-03]** and whose durability cannot be
judged from the filings closes **UNKNOWABLE at Q2**, without prejudice. **That branch does not
apply here, and it was checked before OUT was written.** ADM does not pass [E3-03]: criterion
(2) fails on the company's own filed sentence about substitution. This is not a business I
cannot judge — it is a business the filings let me judge, and the judgment is that there is no
franchise. There is a large, old, competently-run commodity network earning about 10% on
equity across a decade in an industry whose own risk factors recite [E2-58]'s over-capacity
equation. Nor is the [E4-04] *rebuilt-from-zero* test the ground: ADM's network is maintained,
not replaced. **The gate fails at [E3-03] itself, not at durability.**

- Needed or desired [x] · no close substitute [ ] · not price-regulated [x]
- Primary moat metric, filing-sourced, and its trend: **return on average equity capital
  employed [E2-01] — 14.4% (2023) → 7.8% (2024) → 4.8% (2025); ten-year mean 10.0%. FALLING.**
- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL · **Direction: NARROWING**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *OUT on the business, permanent. The evidence is here and the business fails [E3-03]. Not a
  diligence failure and not indeterminacy: the resolving document was read and it is ADM's own
  Form 10-K.*

  **Asked aloud, as the framework requires: "Can I name the document that would resolve this?"**
  **It is already read** — FY2025 10-K Item 1A (substitution), Item 7 MD&A (price pass-through,
  processed volumes), and six peers' FY2025 annual filings. Nothing further would move it.

---
# THE FILE IS CLOSED AT Q2.

**Everything below this line is RECORDED, NOT SCORED.** Operator rule 2: no verdict box is
ticked at Q3, Q4, Q5 or Q6, and no Q5 output is reported as a clearance. The findings are
written because a closed file that discards its evidence has to be re-run, and because two of
them are tooling defects that bear on other names in the queue.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT SCORED**

*The file closed at Q2. No verdict box below is ticked. This section exists because the
brief pointed at a restatement and a material weakness, and because a closed file that throws
away what it found has to be re-run.*

**STEP 1 — THE WEIGHT CASE, declared even though nothing turns on it here.**
- [x] **Daily execution [E3-38].** This is a have-to-be-smart-every-day business: $6,222M of
  **market inventories** marked to market daily against a derivative book, plus a licensed
  futures commission merchant holding $8,919M of customer money. The 1977 root **[E2-70]**
  applies — an undifferentiated product magnifies the manager.
- [ ] **Control [E1-16]** — a minority public stake, exitable.
- [ ] **Leverage [E3-29]** — short-term debt $798M + current maturities $1,006M + long-term
  $6,606M = **$8,410M against $22,740M of equity**. Real, laddered, not a magnifier.
- **Case declared: ONE determinant high, so Q3 WOULD have been a BINARY GATE** and no price
  would have compensated. Recorded for the register; it decides nothing, because Q2 already
  closed the file on the business.

### HONESTY — the record, each matter dated to when it became PUBLIC [E5-16]

| date public | document | what it says |
|---|---|---|
| **2024-01-22** (event 01-19) | 8-K Item 5.02, acc 0001193125-24-011608 | *"the decision of the Board on January 19, 2024 to place Vikram Luthar, the Company's Chief Financial Officer and Senior Vice President, on administrative leave, effective immediately … pending an ongoing investigation being conducted by outside counsel for the Company and the Board's Audit Committee regarding certain accounting practices and procedures with respect to the Company's Nutrition reporting segment, including as related to certain intersegment transactions. The investigation was initiated in response to the Company's receipt of a voluntary document request by the Securities and Exchange Commission"* |
| **2024-03-01** | NT 10-K, acc 0001193125-24-054362 | *"Due to the investigation, the preparation of the Company's financial statements to be included in the Annual Report as well as finalization of the assessment of internal control over financial reporting, require additional time to complete."* And it pre-announces the finding: the Company *"anticipates correcting certain intersegment sales … that were not recorded at amounts approximating market"* and *"a material weakness in the Company's internal control over financial reporting related to its accounting practices and procedures for intersegment sales."* |
| **2024-03-12** | FY2023 10-K, acc 0000007084-24-000009 | filed late but inside the Rule 12b-25 window. Material weakness disclosed; E&Y's ICFR opinion adverse. |
| **2024-04-22** (event 04-19) | 8-K Item 5.02, acc 0001193125-24-104863 | *"Mr. Luthar will resign effective September 30, 2024"* under a Transition Agreement, staying on as a non-executive employee. **He received his 2023 annual cash performance incentive of $743,419 and the shares earned for his 2021 performance share unit award, *"in each case consistent with the determinations of the Company performance metrics that applied to other executive officers."*** |
| **2024-11-05** (event 11-04) | **8-K ITEM 4.02, acc 0000007084-24-000034** | **The second cockroach, and it is the one that matters.** *"In the course of **testing new controls implemented as part of the Company's material weakness remediation plan** in the third quarter of 2024, the Company identified **additional misclassified intersegment transactions**."* The FY2023 10-K and the Q1 and Q2 2024 10-Qs *"should no longer be relied upon because of errors identified in such financial statements."* |
| **2024-11-18** | 10-K/A (0000007084-24-000051) and two 10-Q/As | the restatements filed. |
| **FY2024 10-K, 2025-02-20** | Item 9A | *"the Company's Chief Executive Officer and Chief Financial Officer concluded that the Company's disclosure controls and procedures **were not effective** as of December 31, 2024"*; management concluded ICFR *"was not effective"*; **E&Y's separate ICFR opinion is adverse** — *"because of the effect of the material weakness described below … the Company … **has not maintained effective internal control over financial reporting** as of December 31, 2024."* |
| **FY2025 10-K, 2026-02-17** | Item 9A | *"Based on evidence validating the operational effectiveness of the Company's newly implemented controls, as previously disclosed, the Company concluded that the previously disclosed material weakness was **fully remediated as of June 30, 2025**. The operational effectiveness of these implemented controls has been tested effectively through the end of the fiscal year."* Disclosure controls effective; E&Y unqualified on ICFR. |
| **2026-01-28** (event 01-27) | **8-K Item 8.01, acc 0001193125-26-025560** | *"the Company has reached a settlement with the SEC, resolving its investigation in its entirety. Under the terms of the settlement, the Company, without admitting or denying any wrongdoing, has agreed to pay a civil penalty of $40 million … In addition, the DOJ has notified the Company that it is no longer a subject of its investigation. These outcomes end the investigations of the Company by the SEC and DOJ."* The press release adds ADM's own framing: *"The transactions addressed in the SEC resolution affected segment-level reporting and had **no impact on the Company's reported consolidated balance sheet, earnings or cash flows** for the periods presented in the restated filings."* |

**The earlier filings show the criminal leg the settlement closed.** The FY2023 10-K: *"Department
of Justice (the DOJ) focused primarily on the same subject matter, and the DOJ **directed grand
jury subpoenas to certain current and former Company employees**."*

**Still live at the FY2025 10-K (Note 20):** the securities-fraud class action filed 2024-01-24
in the Northern District of Illinois, on which *"On March 12, 2025, the court **denied**
Defendants' motions to dismiss"*; consolidated derivative actions in Delaware and Illinois; a
books-and-records action filed 2025-07-03; and, separately and much older, the ethanol
benchmark-manipulation class actions where plaintiffs *"allege that members of the putative
class collectively suffered damages calculated to be between approximately $500 million to over
$2.0 billion."*

**The honest read, and I am writing it the way [E5-17] requires — as the absence or presence of
found disqualifiers, not as a character finding.**
- **What is NOT here.** No admission of wrongdoing. No restatement of earnings, cash flow or the
  balance sheet — the errors were **inside** the segment note. The DOJ closed with no action.
  The company self-reported after an SEC document request and had outside counsel run the
  investigation under the Audit Committee. On **[E5-22]**'s test — *penalty size is not
  seriousness, in either direction* — the $40M is not the measure; **the measure is whether
  they acted when they learned**, and on the filed record they did: leave, investigation,
  disclosure, correction, remediation, all inside fourteen months.
- **What IS here, and it is not small.** **[E4-22]**'s first flag — *"beware of companies
  displaying weak accounting … **There is seldom just one cockroach in the kitchen**"* — fires
  on the specific fact that **the second set of errors was found while testing the remediation
  of the first**. A control environment that produces new errors during its own repair has told
  you the depth of the problem. The company was without a permanent CFO for roughly a year. And
  the departing CFO, placed on leave in connection with the matter, was paid his 2023 bonus and
  his 2021 performance shares in full — which is a fact about how the board priced the conduct,
  recorded without a verdict on it.
- **[E4-34]**'s fourth auditor's-eye question — is there any action with *"the purpose and
  effect of moving revenues or expenses from one reporting period to another"*? **On the filed
  record, no.** The errors moved amounts **between segments**, not between periods. That is a
  materially milder species than the one [E4-34] hunts, and saying so is part of stating the
  record honestly.

### STEP 2 — THE FLAGS. Each is a prompt to read, never a verdict [E4-22, E5-15].

- [x] **weak accounting** — the material weakness, and the second finding during remediation.
  Quoted above. **Now formally cured**: remediated 2025-06-30, unqualified ICFR opinion for
  FY2025.
- [ ] **unintelligible footnotes** — no. The segment note, the inventory note and the cash-flow
  detail lines are legible and the securitization line was findable by reading three 10-Ks.
- [x] **trumpeted earnings projections / growth targets [E4-22, E3-48, E5-30]** — **fires, and
  it is the live one.** The latest earnings release (8-K EX-99.1, filed **2026-08-04**, acc
  0000007084-26-000040) is headlined ***"Raises full-year 2026 adjusted EPS guidance on strong
  commercial and operational execution"***, and the guided number is **non-GAAP**: *"ADM now
  expects 2026 adjusted EPS of approximately **$5.15 to $5.60**, up from the prior adjusted EPS
  guidance range of **$4.15 to $4.70**."* Management guides a metric it defines, and it
  **expressly declines to guide the GAAP one**: *"ADM is not presenting forecasted GAAP earnings
  per diluted share or a quantitative reconciliation … in reliance on the unreasonable efforts
  exemption."* **[E5-30]**: *"once you start it, it's all over. You can't quit … And forecasting
  earnings, I can't imagine anything more destructive."* This is a ratchet, not this year's fact.
- [ ] **serial share issuance [E5-15]** — no, the opposite. $2,673M repurchased in 2023 and
  $2,327M in 2024. See the allocation flag below.
- [x] **EBITDA / adjusted-earnings promotion [E4-29]** — **fires.** The FY2025 10-K says in
  terms: *"The Company uses **adjusted net earnings, adjusted diluted EPS, EBITDA, adjusted
  EBITDA, and total segment operating profit**, non-GAAP financial measures as defined by the
  SEC, to evaluate the Company's financial performance."* The Q2 2026 release carries a full
  EBITDA and Adjusted EBITDA reconciliation. **[E4-29]**: *"Trumpeting EBITDA … is a
  particularly pernicious practice … That's nonsense."* And **[E5-41]**'s mechanism bites
  exactly here — ADM's depreciation is **reverse float**, money spent on river terminals and
  crush plants years ago and only now recorded; D&A was $1,181M in FY2025, against $1,255M of
  earnings before income taxes. **EBITDA deletes an expense roughly the size of the company's
  entire pre-tax profit.**
- [x] **the adjusted-earnings gap, sized [E5-33, E3-53]** — FY2025 GAAP net earnings **$1,078M
  / $2.23**; adjusted net earnings **$1,660M / $3.43**. The bridge is $582M, of which **$776M is
  "Impairment, exit, restructuring charges, and settlement contingencies"**. FY2024: $1,800M
  GAAP to $2,339M adjusted, with $512M of the same line. **Two consecutive years in which
  restructuring and impairment are excluded from the headline number.** **[E5-33]**: *"to tell
  owners year after year, 'Don't count this' … is misleading."* **[E3-53]**: *"a large chunk of
  costs that should properly be attributed to a number of years is dumped into a single
  quarter."* **These charges are in the owner-earnings mean below, at full weight.**
- [ ] **filed-figure tells [E4-30] — CHECKED AND DID NOT FIRE.** Cash income taxes as a share of
  reported pre-tax income, from the filed statements: **2021 16.7% · 2022 13.5% · 2023 17.3% ·
  2024 29.2% · 2025 31.0%.** The ratio is **rising**, not falling; the tell points the other
  way. And reported growth is anything but *"unnaturally smooth"* — ROE ran 12.7 → 18.5 → 14.4
  → 7.8 → 4.8. **A flag checked and cleared is worth recording as much as one that fires.**
- [ ] **metric-switching [E2-49] — CHECKED, DID NOT FIRE.** The brief said [E2-49] stands at six
  fires and five failures and told me to assume nothing. **It does not fire.** ADM's headline
  non-GAAP measures — adjusted EPS, total segment operating profit, adjusted EBITDA — are the
  **same four measures, defined in the same words**, in the FY2023, FY2024 and FY2025 10-Ks and
  in the Q2 2026 release, across a period in which segment operating profit fell from $6.4bn
  (2022) to $3.2bn (2025). **[E2-49]** predicts *"disposition of the yardstick rather than
  disposition of the manager"* when results deteriorate. **ADM kept the yardstick through a 50%
  deterioration.** That is the candour case, and it is recorded in ADM's favour. **The prior now
  stands at six fires and SIX failures.**
- [ ] **dividends funded by issuance [E2-52] — CHECKED, DID NOT FIRE.** Cash dividends $977M /
  $985M / $987M in 2023-25 against **zero** proceeds from share issuance in any year and $5.0bn
  of net repurchase. There is no Peter-to-Paul here.

### STEP 3 — THE PRIMARY TEST [E2-01]

The ten-year ROE series is at Q2 and is not repeated. **Mean 10.0%, five-year 11.6%, last three
years 14.4% → 7.8% → 4.8%.** **[E2-43]**'s denominator adjustment for an acquisitive filer:
goodwill and intangibles are **$6,745M of $22,740M of equity (30%)**, so return on average net
tangible equity runs materially higher — 6.9% in FY2025, 25.7% at the 2022 peak. Reported
separately, as [E2-43] requires, and it does not change the shape: the series still tracks the
crop cycle.

**The half-owner test [E2-26]** — *does this reporting tell me what I would want to know if the
positions were reversed?* **Mixed, and the split is clean.** ADM discloses the things that hurt
it in words and in numbers: the deferred-consideration offset, the processed-volume decline, the
material weakness, the non-reliance, the grand-jury subpoenas, the $500M-to-$2.0bn class-action
damages claim, the $316M BTC benefit, and the segregated customer money on both sides of the
balance sheet. Against that, the **headline** number management steers to is one it defines and
will not reconcile forward. [E2-26]'s standard is *"a one-time item quantified separately at
every line passes; the same item buried in an adjusted figure does not."* **ADM quantifies the
items line by line AND buries them in the headline.** It passes the disclosure half and fails
the emphasis half.

**[E2-72]**'s authorship tell: the 10-K carries no shareholder letter at all, so there is
nothing to score either way.

### THE INSTITUTIONAL IMPERATIVE — score all four [E2-30]. *Not a fraud test.*
- [x] **resists any change in current direction** — ADM has been the same three-segment
  commodity processor throughout, while Tate & Lyle sold its corn wet-milling arm and Bunge
  doubled by combining with Viterra. Doing nothing is a decision.
- [ ] **projects/acquisitions materialise to soak up available funds** — **no.** Acquisitions
  were $23M (2023), $927M (2024) and $108M (2025). The screen's `acq_note` of *"$2,644M, 7% of
  cap, inside the window"* is the five-year total and is dominated by earlier years. This is a
  restrained acquirer, and the resume state's acquisition-perimeter understatement limit is
  stated, not re-tested.
- [ ] **staff studies produced to justify the leader's craving** — nothing found in the filings.
- [x] **peer behaviour mindlessly imitated** — the risk factor ADM files itself describes the
  industry doing exactly this: *"competitor actions to bring idled capacity on-line, build new
  production capacity or execute aggressive consolidation."* That is [E2-27]'s *"viewed
  collectively, the decisions neutralized each other"* written as a risk factor.

### CAPITAL ALLOCATION — the buyback conditions [E5-08], and the flag
- **(1) ample funds for operations and liquidity?** Yes at the FY2025 date: $10.4bn of total
  available liquidity, $9.4bn of it undrawn lines.
- **(2) repurchases at a material discount to conservatively calculated IV?** **FAILS, and the
  pattern is the wrong way round.** ADM repurchased **$2,673M in 2023 and $2,327M in 2024 —
  $5.0bn — and $0 in 2025**, while the FY2025 10-K's own Issuer Purchases table shows the stock
  changing hands at **$67.63 in October 2025 and $57.31 in November 2025** and the quote today
  is **$85.18**. **114,764,049 shares remained authorised**, so nothing stopped it. The company
  bought heavily into the 2022-23 earnings peak and stopped buying at the lowest prices of the
  cycle. **[E5-24]**: *"what is smart at one price is dumb at another."* **[E4-50]**: at a true
  discount the rational course is aggressive. **[E2-51]**: *"A manager who consistently turns his
  back on repurchases, when these clearly are in the interests of owners, reveals more than he
  knows of his motivations."*
- **The humility clause, as required [E4-13]:** *"it is natural for CEOs to be optimistic about
  their own businesses. They also know a whole lot more about them than I do."* ADM had a $40M
  SEC settlement to fund, a trough year and a dividend to defend; a board may reasonably have
  chosen the balance sheet over the buyback in 2025. **CAPITAL ALLOCATION FLAG recorded. It
  binds position size and nothing else** — never the discount rate **[E3-42, E4-21]** — and here
  it binds a position size of zero, because Q2 closed the file.
- **[E2-60] — restricted earnings.** Cash dividends of **$987M against $1,078M of net earnings**
  is a **92% payout in a trough year**, funded out of a working-capital release. The filing
  guides to **$1.0 billion of dividends and ~$1.4 billion of capex in 2026**. One trough year is
  not *"consistently distributes restricted earnings"*, and the balance sheet absorbed it. It is
  the direction to watch, and it is Q6's monitoring item below.

### THE GUARDRAIL [E2-37, E2-38, E3-39] — checked before writing anything above
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** It could not be —
  the file closed at Q2, and Q3 cannot repair Q2 by construction.
- [x] Not a great-manager business: **[E4-23]** was answered at Q2 and no key-person dependence
  was found.
- [x] **The [E2-37] test, stated plainly:** ADM's managers may be allocating capital competently
  inside their industry. *"a textile company that allocates capital brilliantly within its
  industry is a remarkable textile company — but not a remarkable business."*

- **VERDICT: NOT SCORED. The file closed at Q2.** *For the record only: Q3 found no integrity
  disqualifier — the errors were segment-level, no earnings or cash flow was restated, the DOJ
  closed with no action, and the metric-withdrawal prior failed. It found four live flags: the
  first-flag accounting history, non-GAAP guidance, EBITDA promotion, and the backwards buyback.
  **This is the absence of found disqualifiers, not a finding that the managers are honest —
  "sincerity and empathy can easily be faked" [E5-17].***

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT SCORED**

### Owner earnings — REBUILT FROM THE FILINGS, because the tagged series is unusable

**The screen's `spread_caveat` said its four constructions "CANNOT see variation older than the
5-year window; rebuild it [E4-25]", and its `level_note_oe` said the pre-window years run down
to $-7,081.0M. Rebuilt. Here is what the five-year window hid, and it is not what the screen
thought.**

**The pre-window negatives are not a business fact.** ADM's operating-cash line carried
**"Deferred consideration in securitized receivables"** from 2016 to 2020 — receivables sold
whose deferred purchase price was collected back in the **investing** section, dollar for
dollar. The FY2020 MD&A states the offset: *"Deferred consideration in securitized receivables
of $4.6 billion and $7.7 billion in 2020 and 2019, respectively, was offset by the same amounts
of net consideration received for beneficial interest obtained for selling trade receivables."*
The arithmetic is exact in every year: FY2018 −$7,838M in operating against −$6,957M + $14,795M
= +$7,838M in investing. **Adding the line back is a DISCLOSED JUDGMENT of this run**, made
because it restores comparability with the pre-2016 and post-2020 presentations; the alternative
is a ten-year mean of roughly minus $5.9bn a year, which is not a number about ADM.

| $M | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| operating cash **as tagged** | (6,508) | (5,966) | (4,784) | (5,452) | (2,386) | 6,595 | 3,478 | 4,460 | 2,790 | 5,452 |
| deferred consideration add-back | 8,063 | 8,177 | 7,838 | 7,681 | 4,603 | — | — | — | — | — |
| **operating cash, rebuilt** | **1,555** | **2,211** | **3,054** | **2,229** | **2,217** | **6,595** | **3,478** | **4,460** | **2,790** | **5,452** |
| less SBC, in full **[E5-06]** | (74) | (66) | (109) | (89) | (151) | (161) | (147) | (112) | (74) | (83) |
| less total capex — **the valid (c) end** | (882) | (1,049) | (842) | (828) | (823) | (1,169) | (1,319) | (1,494) | (1,563) | (1,248) |
| **OWNER EARNINGS (capex end)** | **599** | **1,096** | **2,103** | **1,312** | **1,243** | **5,265** | **2,012** | **2,854** | **1,153** | **4,121** |
| *memo: at the D&A end of (c)* | *581* | *1,221* | *2,004* | *1,147* | *1,090* | *5,438* | *2,303* | *3,289* | *1,575* | *4,188* |
| memo: net earnings | 1,279 | 1,595 | 1,810 | 1,379 | 1,772 | 2,709 | 4,340 | 3,483 | 1,800 | 1,078 |

- **Short-window mean (5 yrs, FY2021-25): $3,081M to $3,359M.** *(This reproduces the screen's
  $3,081M-$3,358M to the rounding. The screen's five-year arithmetic is correct.)*
- **Long-window mean (10 yrs, FY2016-25): $2,176M to $2,284M.**
- **Spread, conservative end: the ten-year mean is 29.4% BELOW the five-year mean.**
- **What the five-year window hid: the 2016-2020 half, which averaged $1,271M a year of owner
  earnings against the 2021-2025 half's $3,081M.** The five-year default **[E2-42]** happens to
  sit exactly on the supply-tight half of the crop cycle. **[E4-38]** names this disease —
  *"growth-rate presentations can be significantly distorted by a calculated selection of either
  initial or terminal dates"* — and its remedy is to publish every window. Both are published.
  **The spread is not an inconvenience; it IS the range [E4-25].**
- **Is that range too wide to reach a conclusion?** No, and that is worth saying, because the
  range is wide and the conclusion survives it anyway: **every point in it is far below the
  ~10% floor** at this price. See the computation below.
- **The distorted years, named [E5-11]:** 2021-22 (the Ukraine invasion, a South American
  drought, a biofuel bid) on the high side; 2016-17 (a global grain glut) on the low side.
  **[E4-41]** requires the mean be normalized DOWN for luck, and the favourable break here is
  named: 2021's $5,265M is the single largest owner-earnings year in the decade and sits in the
  short window. **[E3-55]**'s scope is checked and does not rescue it: See's losing money eight
  months a year is volatility around a *certain* mechanism. ADM's volatility is about the LEVEL
  — the crush spread itself moves — which is exactly the case [E5-11] says bears on whether
  earnings are reliable.

**MAINTENANCE CAPEX — a DISCLOSED JUDGMENT with a corpus default [E2-23, E3-44, E2-41, E5-20].**
D&A is the corpus default for (c). **This business is in the exception class and the D&A end is
therefore shown only as a memo line, never as an equally legitimate answer.** The ground, from
the filing: ADM calls itself *"a capital intensive agricultural commodity-based business"* in
its own liquidity section; **capex has exceeded D&A in four of the last five years** ($1,494M vs
$1,059M in 2023, $1,563M vs $1,141M in 2024); and the company guides 2026 capex of *"approximately
$1.4 billion"* against FY2025 D&A of $1,181M. A river terminal, a barge fleet and a crush plant
are renewed in current dollars against depreciation charged in old ones — **[E4-47]**'s
inflation condition, which widens the exception class for exactly this kind of asset. **(c) is
therefore judged at total capex, and the honest figure is the capex end.**

**THE WORKING-CAPITAL INCREMENT — [E2-23] constraint 3, and the LIFO carve-out DOES NOT APPLY.**
The parenthetical exempts *"businesses following the LIFO inventory method"*. **ADM is not one.**
The inventory note says: *"Certain merchandisable agricultural commodity inventories, which
include inventories acquired under deferred pricing contracts, are **stated at market value**. In
addition, the Company values certain inventories using the **first-in, first-out (FIFO)** method
at the lower of cost or net realizable value."* **Market inventories are $6,222M of $10,369M.**
Under market-value and FIFO accounting, a rise in commodity prices requires more working capital
at the same unit volume, so the increment is real and must be in (c). The operating-cash
construction already nets it — but **the direction has to be stated, because FY2025 is the whole
question:**

| $M, working-capital lines from the filed cash-flow statement | 2023 | 2024 | 2025 |
|---|---|---|---|
| segregated investments | (194) | (693) | (43) |
| trade receivables | 737 | 447 | 855 |
| **inventories** | **2,889** | **162** | **1,511** |
| other current assets | 694 | 665 | 672 |
| trade payables | (1,544) | (719) | (473) |
| payables to brokerage customers | (2,059) | (78) | 1,064 |
| accrued expenses and other payables | (790) | (276) | (823) |
| **net working-capital contribution to operating cash** | **(267)** | **(492)** | **+2,763** |
| **as a share of that year's operating cash** | (6.0)% | (17.6)% | **+50.7%** |

**More than half of FY2025's operating cash is a working-capital release, and ADM says why:**
*"Changes in inventories resulted in cash inflow of $1.5 billion in the current year **reflecting
lower commodity pricing** and reductions driven by working capital reduction initiatives"*, and
the brokerage inflow *"is driven by increased trading activity in the Company's futures
commission and brokerage business"* — that last $1,064M is **customers' money**, not ADM's.
**Inventory has fallen from $14,771M (2022) to $10,369M (2025): a $4.4bn release that reverses
if grain prices normalise upward.** FY2025's $4,121M of owner earnings is therefore the
**high-water mark of a de-stocking year**, not a run rate.

**The honest cross-check on all of it.** Over the ten years, cumulative rebuilt owner earnings
(capex end) are **$21,758M** against cumulative reported net earnings of **$21,245M** — within
**2.4%**. Working capital swings violently and nets to roughly nothing across a cycle with flat
unit volume, which is the LIFO carve-out's *logic* arriving at the same place by a different
route. **The defensible long-run owner-earnings figure for ADM is about $2.2 billion a year.**

**EQUITY-METHOD INCOME IS NOT CASH TO THE OWNER, and it is a fifth of the story.** ADM holds
**22.5% of Wilmar International**, plus Stratas, Olenex, Edible Oils, Hungrana, Red Star and
others. **Equity in earnings of unconsolidated affiliates was $648M in FY2025 — 60% of the
$1,078M of net earnings.** The cash-flow statement separates them on its own face: *"Equity in
earnings of unconsolidated affiliates, net of dividends | (224) | (180) | (143)"*, so **cash
dividends actually received were $424M (2025), $441M (2024) and $408M (2023)** and only that
cash is inside the operating line and inside the owner-earnings table above. **Handled
explicitly: the undistributed $224M is OUT.** The framework's [E3-04] look-through convention
would add it back for a *valuation* of the stake; it is deliberately not added here, because the
one-book rule is being applied to a closed file and adding it would only make a failing yield
look better. **Conservatism is spent once and this is not the place [E4-11].** The FY2025 Wilmar
result also carries two specified items on its own — *"a one time remeasurement gain of $254
million and a $163 million penalty charge"* — which is a reminder that the look-through would
import someone else's volatility, not remove any.

**SBC, verified rather than assumed.** The brief said ADM was not among the 21 names where SBC
resolves for no year, and to verify. **Verified: `ShareBasedCompensation` resolves for every one
of the ten years** ($74M to $161M) and reconciles to the *"Stock compensation expense"* line on
the face of the filed cash-flow statement ($83M / $74M / $112M for 2025/2024/2023). **No partial
resolution. Subtracted in full [E5-06].** SBC runs 1.5-2.4% of operating cash, so **[E3-70]**'s
market-value measure — the grant-date total rather than the charge — would move owner earnings
by well under 1% and cannot change any reading here. Recorded, not pursued. *(The resume state's
SBC max-rule double-count limit is noted and does not bite: ADM capitalises no SBC into software
that I can find, and the charge and the add-back are the same number.)*

### Great, good, or gruesome? **[E4-20]**
- [ ] great — [ ] good — [x] **GRUESOME-ADJACENT, and the honest label is "good at the top of
  the cycle, gruesome at the bottom."** Read it as [E4-20] frames it, as a savings account.
  Ten-year owner earnings of ~$2.2bn on average equity that rose from $17.5bn to $22.5bn: the
  account pays roughly **10%** and **requires you to keep adding money** — $10.3bn of cumulative
  capex over the decade against $10.2bn of cumulative D&A, for **oilseed throughput that is
  0.04% higher than 2018 and corn throughput 17% lower**. **[E4-43]** forbids over-reading:
  the *good* class passes, and *"nothing shabby about earning $82 million pre-tax on $400
  million of net tangible assets"* is a 20.5% return. ADM's ten-year 10.0% is half of that and
  is below **[E5-40]**'s ~12% *"quite satisfactory"* return-on-retention benchmark. **It is not
  gruesome — the capital does earn a return — but it is at best the low end of good, and it is
  good only when averaged across a cycle whose bottom is 4.8%.**

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — LARGE, NOT RELIABLE.** $2.2bn of owner
  earnings on a ten-year mean, with a range from $599M to $5,265M. The stream is real; its
  *level* is not predictable, which is the distinction [E5-11] draws.
- **(2) massive liquid assets — NO, and this is the weak one.** **Cash and cash equivalents were
  $1,015M at 2025-12-31** against $52,389M of assets. The $8,432M of "segregated cash and
  investments" is **customers' money**, matched by $8,919M of payables to brokerage customers,
  and cannot be counted. ADM's own stated liquidity of **$10.4bn is $1.0bn of cash plus $9.4bn
  of unused credit lines**, and **[E5-39]** refuses to count the lines: *"We will never be
  dependent on the kindness of strangers … we don't count on bank lines. You know, we don't
  count on — we don't count on anything."* **The filing states the
  dependency itself:** *"The Company **depends on access to credit markets**, which can be
  impacted by its credit rating and factors outside of the Company's control, to fund its
  working capital needs and capital expenditures."* There was **$715 million of commercial paper
  outstanding at 2025-12-31** against $5.1bn of supporting lines. This is a business financed by
  the wholesale funding market by design.
- **(3) no significant near-term cash requirements — ADEQUATE, and the filing quantifies it.**
  *"the Company's other material cash requirements within the next 12 months include current
  maturities of long-term debt of $1.0 billion, interest payments of $527 million, operating
  lease payments of $357 million, and pension, other postretirement, and defined contribution
  plan contributions of $119 million"*, plus guided capex of ~$1.4bn and dividends of ~$1.0bn —
  **about $4.4bn**. The debt ladder is genuinely long: **2026 $1,006M · 2027 $266M · 2028 nil ·
  2029 $145M · 2030 $1,006M · thereafter $5,442M.** Pension contributions of $119M are trivial
  against a $52bn balance sheet; the brief's pension prior is **refuted as a material item**.
  **[E2-54]**'s coverage test passes with room: FY2025 cash interest $629M against $5,452M of
  operating cash net of $1,248M of capex.
- **Leverage, named and quantified [E4-16, E3-29]:** short-term debt $798M + current maturities
  $1,006M + long-term debt $6,606M = **$8,410M against $22,740M of equity and $11,179M of net
  PP&E**. **[E3-52]**'s terms test: this is covenanted, dated, wholesale debt, not
  customer-prepaid float — with one exception, the **$8,919M of payables to brokerage
  customers**, which is customer money that is not ADM's to use and is matched asset for asset.
  **There is no leverage ratio in this framework and the corpus supplies none.** The number is
  stated and judged: **moderate, well-laddered, and not the way this business dies.**

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**

**Model exposure, not experience [E4-40].** ADM has not had a solvency event in a century, and
that history is *"not only useless, but actually dangerous"* as a guide. The exposure is in the
filing.

**The mechanism.** ADM does not die of debt. It dies of **[E2-27]**'s collective-capex trap:
*"Viewed individually, each company's capital investment decision appeared cost-effective and
rational; viewed collectively, the decisions neutralized each other and were irrational."* The
industry adds crush and mill capacity into a good crush spread — ADM's own risk factor names the
behaviour — the spread compresses, and every participant is left with more capital in the game
at anemic returns. ADM does not fail; **it grinds**, spending $1.3-1.5bn a year to hold flat
volumes at a single-digit return on equity. That is exactly what the last decade shows.

**And the faster mechanism, which the filing makes quantifiable:** a **funding event**. ADM
finances $10.4bn of inventory and receivables with $715M of commercial paper and $12.3bn of
lines, and says in terms that it depends on credit-market access. A credit-rating downgrade in a
year when grain prices spike would demand *more* working capital at the moment funding costs
most — **[E2-64]** in reverse.

**Quantified from the filed figures.** Take **[E3-24]**'s form. ADM's FY2025 gross profit was
**$5.0 billion on $80.3 billion of revenue: a 6.2% gross margin**, and net earnings were
**$1,078M, a 1.34% net margin**. **A 1.4-percentage-point compression of the gross margin — from
6.2% to 4.8%, about $1.1 billion — wipes out the entire net income of the company.** That is
roughly the distance between the FY2024 and FY2025 segment operating profit outcomes ($4,209M to
$3,242M), so it is not a tail scenario; it is the amplitude the cycle already delivers. Two such
years in a row, with the dividend held at $1.0bn and capex at $1.4bn, and ADM is funding its
distribution from the balance sheet — which is **[E2-60]**'s *"consistently distributes
restricted earnings"* and the beginning of the grind.

**Likelihood:** [ ] likely · [x] **a real possibility** — for the margin-compression grind, which
is the observed behaviour of the last decade, not a forecast · [ ] a low-level possibility — for
a funding event, which requires a rating action and a price spike together.

**And the argument against my own position, as [E4-51] demands** — *"I'm not entitled to have an
opinion unless I can state the arguments against my position better than the people who are in
opposition."* **The best case against everything above:** ADM's assets are irreplaceable and
sited where the crops are; global protein demand compounds; the 2026 year to date is running far
ahead of 2025 (**YTD EBT $1,472M, +133%; adjusted EPS guidance raised twice to $5.15-5.60**); the
crush and ethanol spreads that destroyed 2025 have already turned on the finalised 2026-27
renewable volume obligations; the material weakness is remediated and the government
investigations are closed with no admission and no DOJ action; the balance sheet is
conservatively laddered; and the stock is bought at a point in the cycle where reported earnings
understate normal. **A buyer who believes the cycle mean-reverts to the 2021-23 level is buying
$3.1-3.4bn of owner earnings for $41bn — 7.5-8.2%.** I think that is the strongest honest form
of the bull case, and I record that it still does not clear the floor.

- **VERDICT: NOT SCORED. The file closed at Q2.** *For the record: Q4 would have turned on the
  ten-year mean of ~$2.2bn and the finding that FY2025's $4.1bn is half a de-stocking release,
  not a run rate.*

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**

**⛔ Q5 DID NOT OPEN. Q2 returned OUT.** The arithmetic below is recorded because the screen
ranked this name on an owner-earnings figure that needed rebuilding, and the rebuilt figure is
the thing a future reader needs. **No entry language appears here and none is implied. This is
not a valuation of ADM and it is not a price at which ADM would be bought; the business gate
failed and no price repairs it [E5-35].**

- market cap, hand-struck: **$41,053M** (481,959,583 shares × $85.18, 2026-09-18)
- sovereign: **5.34%**, US Treasury 30-year par yield, 2026-09-18, the bare rate with **no
  per-name premium added [E3-42]**

| | owner earnings | ÷ cap | vs sovereign 5.34% | vs the ~10% floor [E4-28] |
|---|---|---|---|---|
| **ten-year rebuilt mean (2016-25)** | **$2,176M - $2,284M** | **5.30% - 5.56%** | **−0.04 to +0.22 points** | **far below** |
| five-year mean (2021-25) | $3,081M - $3,359M | 7.50% - 8.18% | +2.16 to +2.84 points | below |
| FY2025 alone (a de-stocking year) | $4,121M - $4,188M | 10.04% - 10.20% | +4.70 to +4.86 points | *only the single distorted year touches it* |

**Read the table the way [E4-28] instructs — the floor first, and it does not move with the
sovereign:** *"basically that's the figure we quit on … that's true whether short rates are 6
percent or whether short rates are 1 percent."* **On the honest long-window number ADM yields
about what the 30-year Treasury yields.** Only the single most distorted year in the decade —
the one whose cash is 50.7% working-capital release — reaches 10%, and a floor cleared by one
cherry-picked year is **[E4-38]**'s terminal-date distortion, which is the error, not the answer.

**What the price already assumes.** To turn the ten-year mean of $2,176M into a 10% expectancy
on $41,053M requires owner earnings to **grow 89%**, to about $4.1bn, and stay there. ADM has
reached $4.1bn once in ten years. **[E4-35]**'s base rate applies to any case that needs it:
*"fewer than 10 of the 200 most profitable companies in 2000 will attain 15% annual growth in
earnings-per-share over the next 20 years."* **And [E4-44]**'s second bound: the value cannot
grow faster than the earnings, and the earnings are throughput times a spread ADM does not set,
on throughput that has not moved in seven years.

**One book [E3-34].** No DCF was run. It would have been an engine at most, and it casts no vote.
**Windage count: ONE.** Conservatism is spent once **[E4-11]** — in the choice of the capex end
of (c) over the D&A end, which is not windage at all but the [E5-20] exception class applied. No
margin of safety is applied on top, because nothing here is a purchase case.

- **VERDICT: NOT SCORED, and no box is ticked. Q5 did not open [operator rule 2].**

## Q6 — WHAT WOULD PROVE ME WRONG? — **RECORDED, NOT SCORED**

There is no entry, so there is no exit to pre-commit and no position to size. **[E1-02]** —
*"I believe in establishing yardsticks prior to the act"* — is still worth honouring for the
reversal condition, because a Q2 OUT is permanent **about the evidence as it stands** and the
honest thing is to say what evidence would be new rather than to pretend none could be.

**The reversal condition, in words, and deliberately NOT as a price alert.** A price band on a
name that failed on the *business* is a category error (the QLYS ruling), and no price
compensates for a Q2 failure **[E5-35]**: *"You can turn any investment into a bad deal by paying
too much. What you can't do is turn any investment into a good deal by paying little."*
**ADM gets no band in `tools/alerts.json` and no `PORTFOLIO.md` row.**

**What would reopen the file — all three are business facts, none is a price:**
1. **Nutrition becomes the company rather than one-eighth of it.** If the Nutrition segment
   reached a third of segment operating profit at Ingredion-like returns sustained across a full
   crop cycle, the [E3-03] criterion-(2) failure would have to be re-argued against a different
   revenue mix. Today it is 12.9% of segment operating profit on a 5.6% margin.
2. **A structural cost advantage appearing in the competitor row.** If ADM's return on equity
   capital employed ran materially *above* Bunge's, Ingredion's and CHS's through a full cycle
   rather than below them, [E2-58]'s *"wide and sustainable"* exception would have evidence it
   presently lacks. The test is relative and it is annual.
3. **The physical series turning.** Oilseed and corn throughput growing for three consecutive
   years would refute the [E4-55] reading directly.

**What would NOT reopen it:** a good crush year, a raised adjusted-EPS guide, a favourable
renewable volume obligation, or a lower share price. Those are the wave **[E3-51]**, not the
surfer.

- **VERDICT: NOT SCORED. The file closed at Q2.**

---
## SELF-AUDIT — ticked honestly, and two boxes are qualified rather than ticked

- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT, stop. Q3-Q6 recorded
      beneath the close with no boxes ticked, per operator rule 2.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** One question is
      marked IN — Q1 — and it rests on the FY2025 10-K read in full.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** No gate returned
      UNRESEARCHED. **Two competitor-row CELLS are UNRESEARCHED and are named: Cargill Inc. and
      Louis Dreyfus Company B.V., both private, neither an SEC filer, no audited English
      statements publicly filed. The ladder rung that fails is "competitor filings" and the
      obstacle is that they do not exist.** The moat class is **NONE**, not PROVISIONAL, and the
      reason is stated at Q2: the claim the row is used to support is a NEGATIVE one — that ADM
      has no wide and sustainable cost advantage — and the two missing cells cannot supply one.
      *A reader who disagrees with that reasoning should read the class as PROVISIONAL; the
      [E3-03] criterion-(2) failure closes the gate either way, on ADM's own sentence.*
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** No gate returned
      UNKNOWABLE. The [E4-04] perimeter-close branch was checked at Q2 and explicitly rejected,
      with the reason written down.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** Nine
      ADM 10-Ks, one 10-K/A, one 10-Q, one NT 10-K and four 8-Ks, each with its accession number.
      Three cross-checks: FY2025 operating cash $5,452M (agrees); shareholders' equity recomputed
      from A−L = $22,740M (agrees); FY2016 operating cash **$1,475M vs $(6,508)M across two
      filings (does NOT agree, and is the finding)**.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Two windows published with the spread (29.4%); (c) judged at total capex under [E5-20] with
      the D&A end shown as a memo and named INVALID for this class; the working-capital increment
      addressed with the LIFO carve-out tested and found **not** to apply.
- [x] **Competitor row filled.** Seven peers obtained and cross-checked, two named as
      unobtainable. Bunge's Viterra perimeter established from Bunge's own 10-K.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      2026-09-18, US Treasury daily par yield curve. FRED not used. Not inherited from the brief.
- [x] **Value stated as a round-number range, not a point estimate.** No value was stated at all,
      because Q5 did not open. The yields at Q5 are headed COMPUTATION — NOT A CLEARANCE.
- [x] **One bar chosen, not both; windage count stated.** Neither bar was applied, because no
      valuation was performed. **Windage count: ONE**, stated at Q5.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $85.18, close
      2026-09-18, Yahoo Finance, flagged, raw JSON saved to the research folder.
- [x] **Run committed to git** — with a pathspec, after Q1 and after Q2, and again at the fold.

**Two things this audit will not tick clean, stated rather than buried:**
1. **The securitization add-back is my judgment, not ADM's presentation.** ADM never published a
   ten-year comparable operating-cash series. I built one by adding back a line the company
   quantified and whose exact offset the company states in words. **If a reader rejects the
   add-back, the ten-year window has no honest number at all and only the five-year window
   stands — which yields 7.50-8.18% and still fails the floor.** The conclusion does not depend
   on the judgment; the disclosure does.
2. **[E3-04]'s look-through on the Wilmar stake was deliberately not applied.** Adding the $224M
   of undistributed equity earnings would raise the yield by roughly half a point. It is left
   out and the reason is written at Q4: this is a closed file, and spending the arithmetic in
   the favourable direction on a name that already failed is the incentive **[E4-27]** warns
   about.

## REGISTER

- Verdict: [ ] IN · [x] **OUT (about the business)** · [ ] UNRESEARCHED · [ ] UNKNOWABLE
- **One line: ADM fails Q2 on [E3-03] criterion (2) in its own filed words — its products are
  "highly price competitive and, in many cases, subject to substitution" — and the seven-peer
  competitor row refutes [E2-58]'s one exception, because the industry's largest balance sheet
  earns a middling five-year return (ADM 11.6% against Bunge 17.6%, Ingredion 14.9%, Darling
  13.0%, CHS 11.9%).**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable to any gate. The two unobtainable
  competitor cells are Cargill and Louis Dreyfus; both are private, file nothing with the SEC,
  and the obstacle is structural rather than procedural.
- **If UNKNOWABLE:** not applicable. Checked against the [E4-04] perimeter-close branch and
  rejected with reasons at Q2.
- **Reversal condition (in place of a price band, per the QLYS ruling):** Nutrition reaching a
  third of segment operating profit at sustained Ingredion-like returns; ADM's return on equity
  capital employed running above Bunge's, Ingredion's and CHS's through a full cycle; or three
  consecutive years of growth in oilseed and corn throughput. **No price alert. No portfolio
  row.**

---
## TOOLING DEFECTS FOUND BY THIS RUN — three, each measured before being recorded

**1. `working_capital_flag()` tests SINGLE LINES and missed a 50.7% aggregate.** ADM's
`wc_note` is **blank** on the master queue row. The flag fires when one working-capital line
moves by more than 30% of a year's operating cash. ADM's FY2025 lines, against $5,452M of
operating cash: inventories **+$1,511M = 27.7%**, payables to brokerage customers **+$1,064M =
19.5%**, trade receivables **+$855M = 15.7%**, accrued expenses **−$823M = 15.1%**. **Every line
is under the threshold. The AGGREGATE working-capital contribution is +$2,763M = 50.7% of
operating cash.** The flag is silent on the single largest distortion in the name's
owner-earnings series. **This is not the same defect as the annual-facts limit already recorded
in the resume state** (that one is about periodicity; this one is about aggregation), and it
will under-fire on every merchandiser, where the working-capital story is the sum of many
correlated lines rather than one big one. **Suggested fix, offered and not applied:** fire on
the *net sum* of the working-capital detail lines as well as on any single line. It adds no
step and no number the filing does not already carry.

**2. The queue's owner-earnings series for ADM is built on a classification artifact, and
`level_note_oe`'s "$-7,081.0M" is not a fact about the business.** Any name that ran an accounts
receivable securitization with a deferred-purchase-price structure between roughly 2016 and 2021
carries five years of structurally negative tagged operating cash with an exactly offsetting
investing inflow. The screen's own `spread_caveat` told this run to rebuild the long window, and
rebuilding it turned an apparent $-7.1bn into $+1.6bn to $+3.1bn a year. **The five-year window
is unaffected and reproduces exactly ($3,081M-$3,358M), so no queue ranking changes** — but any
long-window statement about ADM from the tagged series is meaningless, and the same shape will
appear on other merchandisers and consumer names of that vintage. **Recorded as a data-shape
hazard for a reader, not proposed as a tool: only a reader can tell a classification change from
a business change.**

**3. `RevenueFromContractWithCustomerExcludingAssessedTax` returns 31% of ADM's revenue.** The
tag gives **$24,956M** for FY2025 against a filed **$80,269M** (`Revenues`). The reason is real
and not a filer error: most of ADM's sales are commodity contracts accounted for under
derivative rather than ASC 606 rules, so they are not revenue-from-contracts-with-customers at
all. **No owner-earnings number in the queue depends on revenue, so nothing is wrong today** —
but any screen column keyed on the preferred revenue tag would read ADM, and every commodity
merchandiser, 69% low. **Measured, not assumed:** Bunge shows the same shape ($16,944M tagged
against $70,329M filed) and The Andersons the same ($1,531M against $11,009M). **Three of three
merchandisers tested.**

## PRIORS THIS RUN REFUTED — including the brief's own

- **The brief's summary of the segment matter was materially right and one clause was wrong.**
  The CFO leave, the delayed 10-K, the SEC investigation, the DOJ involvement, the segment
  revision and the material weakness are all confirmed from the filings. **What the brief did
  not know, and what the filings show, is that the matter is CLOSED**: the SEC settled on
  2026-01-27 for a **$40 million civil penalty with no admission**, the **DOJ closed with no
  further action**, and the material weakness was **remediated as of 2025-06-30** with an
  unqualified ICFR opinion for FY2025. The brief also said *"segment results were subsequently
  revised"*, which is right, and implied the revision might bear on the owner-earnings number —
  **it does not**: ADM's own words are that the transactions *"affected segment-level reporting
  and had no impact on the Company's reported consolidated balance sheet, earnings or cash
  flows."* I checked that claim against the FY2023 10-K/A rather than taking it, and the
  consolidated statements are unchanged.
- **[E2-49], the metric-withdrawal prior, FAILED to fire** — sixth failure against six fires.
  ADM kept the same four non-GAAP yardsticks through a 50% fall in segment operating profit.
- **[E4-30]'s cash-tax tell FAILED to fire** — the ratio rose from 13.5% to 31.0%.
- **The brief's pension prior is refuted as a material item.** Pension, other postretirement and
  defined-contribution contributions are **$119 million** in the next twelve months, against
  $52bn of assets. It is not a survival item and it is not close to one.
- **The screen's cap SURVIVED the hand-strike** — $41,053M against $39,328M, a 4.4% price-date
  difference. **Two runs on 2026-09-21 found machine caps wrong by 6.29x (BELFB) and 18% (FC);
  this one did not.** The prior that machine caps are unreliable is a prior about *multi-class
  and stale-cover* filers, and ADM is neither: one class, cover dated 2026-07-30.
- **The screen's five-year owner-earnings arithmetic reproduced exactly.** Where the screen was
  wrong was not the arithmetic but the *input series*, and its own `spread_caveat` said so.
