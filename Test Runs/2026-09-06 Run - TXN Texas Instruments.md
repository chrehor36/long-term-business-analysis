# Company Run — TEXAS INSTRUMENTS INCORPORATED (TXN) — 2026-09-06
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

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year,
  struck fresh from the issuing authority** (`tools/sources.py`, 2026-09-06). FRED is the
  fallback and was not used.
- FX: none. TXN reports in USD and earns in USD. (Geographic revenue is 38% United States,
  21% China, 11% rest of Asia, remainder EMEA/Japan — but the reporting and functional
  currency for all non-U.S. subsidiaries is the U.S. dollar, stated in the accounting-policy
  note: *"The functional currency for our non-U.S. subsidiaries is the U.S. dollar."*)

**STAGE 0(a) — THE SHARE COUNT, READ OFF THE COVER BY HAND.**
> "913,247,686 … Number of shares of Registrant's common stock outstanding as of July 15, 2026"
— **Q2 FY2026 10-Q cover page, accession 0000097476-26-000152.**

**Single class.** Balance sheet, 2026-06-30 and 2025-12-31: *"Common stock, $1 par value.
Shares authorized – 2,400; shares issued – 1,741"*, treasury 834M at 2025-12-31, and
*"Preferred stock, $25 par value. Shares authorized – 10; **none issued**"*. No A/B classes,
no preferred, no convertible. Issued-less-treasury at 2025-12-31 = 1,741 − 834 = **907M**,
consistent with the 913.2M cover count seven months later (the difference is stock
compensation issuance net of a small buyback). The screen's weighted-diluted 913.0M happens
to agree with the cover count to 0.03%; **the cover count is the one used.**

- price **$258.44** · **2026-09-04** · Yahoo aggregator, **flagged — live quote only,
  operator rule 5**
- **market cap = 913,247,686 × $258.44 = $236,020M**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines and supplemental lines  [x] footnotes
- **FY2025 10-K, filed 2026, period ended 2025-12-31, accession `0000097476-26-000059`,
  primary document `txn-20251231.htm`** — downloaded and flattened to
  `Test Runs/_research 2026-09-06 TXN/txn-FY2025-10K-flat.txt`.
- **Q2 FY2026 10-Q, period ended 2026-06-30, accession `0000097476-26-000152`, primary
  document `txn-20260630.htm`** — downloaded and flattened to the same folder.
- Also read: Q1 FY2026 10-Q `0000097476-26-000101`, Q3 FY2025 10-Q `0000097476-25-000060`.

**FIGURE CROSS-CHECKED AGAINST THE FILED STATEMENT — and it reconciles to the dollar.**
The FY2025 cash-flow statement as filed reads *"Cash flows from operating activities 7,153"*,
*"Capital expenditures (4,550)"*, *"Proceeds from U.S. CHIPS and Science Act (CHIPS Act)
incentives 335"*, *"Stock compensation 419"*. TXN's own non-GAAP table states
*"Free cash flow (non-GAAP) $2,938"*. Check: 7,153 − 4,550 + 335 = **2,938** ✓, and my
owner-earnings capex-end figure for FY2025, 7,153 − 419 − 4,550 = **2,184**, is exactly
TXN's own free cash flow less stock compensation less the CHIPS proceeds
(2,938 − 419 − 335 = 2,184) ✓. **The whole owner-earnings construction reconciles to the
company's own published metric by two identified adjustments, both of which the framework
requires: stock compensation is an expense [E5-06], and a government capital subsidy is
not owner earnings.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Texas Instruments prints very
small, very simple electronic circuits onto silicon wafers in factories it owns, cuts them
up, puts them in plastic, and sells them by the catalogue. The parts are cheap — the
average part in an $17.7bn revenue line against *"more than 80,000 products"* sold to
*"over 100,000 customers"* is worth a fraction of a dollar — and almost none of them is
individually important to anybody. What TXN sells is not a chip; it is **the certainty that
the part will be there, in volume, at a knowable price, for the fifteen or twenty years an
industrial or automotive design stays in production.** The money is made on the difference
between what a wafer costs to run through a fully-loaded, fully-depreciated fab and what
several thousand small parts fetch when a customer needs them. In 2025 that difference was
57.0% of revenue at the gross line and 34.1% at the operating line.

**The scarce input this business controls: owned, depreciated, large-diameter wafer
capacity — and the filing quantifies it.**
> "We have focused on creating a competitive manufacturing structural cost advantage by
> investing in our 300mm capacity, as **an unpackaged chip built on a 300mm wafer costs
> about 40% less than an unpackaged chip built on a 200mm wafer.**" — FY2025 10-K, Item 1

Second scarce input, and it is the one that does not depreciate: **the catalogue itself.**
80,000 parts, designed over sixty years, already specified into customers' board designs.
An analog part that is in a design stays in that design until the design dies. TXN states
the tell in its own words for Embedded: *"our customers often invest their own R&D to
develop software that operates on our products. This investment tends to increase the length
of our customer relationships."*

**Will the fundamentals look broadly the same in ten years?** Yes, and this is the strongest
thing about the name. Analog circuits obey physics that has not changed; TXN's oldest
products still sell; the customer base is *"over 100,000"* with *"about half of our revenue
derived from customers outside of our largest 50"*, so no single loss matters; and the
end markets it emphasises — industrial, automotive, data centre — are growing electronic
content per unit. This is emphatically **not** the [E4-46] class that would take months of
study. It is a simple business with one hard question, and the hard question is at Q4.

**Twelve-decisions test [E5-13]:** the business is understandable. That does not make it a
decision; it makes it eligible for one.

- **VERDICT: [x] IN**


## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Needed or desired [x]** — 80,000 catalogue parts in *"almost every type of electronic
equipment"*, 100,000 customers.
**No close substitute [~] — PARTIAL, and the subject is the witness against itself.** For a
part already designed into a board the substitute costs a redesign and a requalification,
which for an automotive or industrial customer is years. For a *new* socket there are dozens:
> "Despite consolidation, the analog and embedded processing markets **remain highly
> fragmented.** As a result, we face significant global competition from **dozens of large
> and small companies**, including both broad-based suppliers and niche suppliers. Our
> competitors also include emerging companies, particularly in Asia."

**Not price-regulated [x].**

**[E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT? HALF OF IT MUST, AND THAT IS THE HALF TXN
JUST SPENT $19.7 BILLION ON.** TXN names four advantages; they split cleanly on this test.
- **The catalogue and the channel do NOT need rebuilding.** An analog part designed in 1995
  still ships; the design win was won once and is not re-competed. This is the durable half
  and it is where the 34.1% operating margin comes from.
- **The 300mm cost advantage MUST be rebuilt, permanently — and the competitor row shows
  rivals renting the identical advantage off other balance sheets.** NXP is obtaining 300mm
  capacity for **3.2% of revenue in capex** by taking 10% of TSMC's Dresden fab (ESMC) and
  40% of Vanguard's Singapore fab (VSMC); STM is getting **up to ~EUR 2.9bn from the State of
  France** for Crolles; TXN's own $1.6bn CHIPS award and 35% ITC are the same instrument
  pointed at itself. **A cost advantage every competitor can rent from a state or a foundry
  is not *"both wide and sustainable"* in [E2-58]'s sense** — it is the ordinary condition of
  a subsidised industry.

**[E3-62] — THE SECOND STEP, AND IT IS THE SHARPEST TEST IN THE FILE.** *"how much is going
to stay home and how much is just going to flow through to the customer."* TXN files the
saving: *"an unpackaged chip built on a 300mm wafer costs about **40% less** than an
unpackaged chip built on a 200mm wafer."* Where did the 40% go? **On the filed record to
date, none of it stayed home.** Gross margin 68.8% (FY2022) to **57.0% (FY2025)**; operating
profit $10,140M to **$6,023M**, below FY2019's $5,723M; revenue **11.7% under the FY2022
peak** after **$19,700M** of capital expenditure in FY2021-25. *(TXN's own "about $24 billion"
is a TEN-year figure, FY2016-25 = $23.55bn; the six-year build is $19.7bn. Stated because the
two are easy to confuse and the brief used the larger one.)* **The qualifier [E4-26] requires
goes here, not in a footnote: the fabs are not loaded.** TXN's own words — *"Our LFAB
facility … was purchased as an operating fab and is in the early stages of ramping, so we
expect factory loadings to increase over time."* **The flow-through question is NOT YET
SETTLED, and it is the single most important open item in this file.**

### THE COMPETITOR ROW — required **[E3-28]**
**Same metric, same window, filing-sourced. Eight peers obtained. TXN names none of them.**

| Company | operating margin | gross margin | capex % rev | capex/depr | ROE (avg) | revenue | fabs | rung |
|---|---|---|---|---|---|---|---|---|
| **TXN** | **34.1%** | 57.0% | **25.7%** | **2.37x** | **30.1%** | $17,682M | owns; most integrated | SEC 10-K `0000097476-26-000059` |
| **ADI** — the direct comp | 26.6% | **61.5%** | 4.8% | 1.31x | 6.6% | $11,020M | fab-lite, **">half"** outsourced | SEC 10-K |
| **NXPI** | 24.8% | 54.7% | 3.2% | **0.71x** | 21.0% | $12,269M | fab-lite ("hybrid model") | SEC 10-K `0001413447-26-000008` |
| **Renesas** | 15.2% | 57.1% | 6.7% | 1.89x | −2.1% | JPY 1,321,212M | owns fabs | **IR rung, IFRS, JPY** |
| **MCHP** | 10.4% | 57.7% | 1.9% | 0.59x | 3.4% | $4,713M | **35% internal** | SEC 10-K |
| **Infineon** | 10.3% | 39.2% | 12.3% | 0.94x | 5.9% | EUR 14,662M | owns fabs | **IR rung, IFRS, EUR** |
| **STM** | 1.5% *(4.7% ex-$376M charge)* | 33.9% | 17.9% | 1.20x | 0.9% | $11,800M | owns all fabs | **SEC 20-F, US GAAP, USD** |
| **ON** | 1.4% *(12.5% ex-$667M charges)* | 33.1% | 5.7% | 0.62x | 1.5% | $5,995M | owns fabs | SEC 10-K |
| *QCOM (run 2026-09-02)* | *27.9% (QTL 72.4 / QCT 30.4)* | — | — | — | — | *$44,284M* | *fabless* | *completed run* |
| *AVGO (run 2026-09-06)* | *39.9% (semi 57.6 / sw 76.8)* | — | — | — | — | *$63,887M* | *fab-lite* | *completed run* |

**Peers: 8 obtained out of the ~8 the industry has, plus 2 from completed runs on identical
formulas. Six sit on the SEC rung; Infineon and Renesas sit on the IR rung and are labelled
as such — IFRS in EUR and JPY, NOT currency- or GAAP-converted, so they inform direction and
rank, not the arithmetic.** **The brief's assumption that STM is an IR-rung name is WRONG and
is corrected here: STM files a 20-F with the SEC in US GAAP and US dollars.**

**WHAT THE ROW SHOWS. THE FIRST TWO POINTS CUT OPPOSITE WAYS AND BOTH ARE TRUE.**

1. **TXN IS THE BEST ANALOG BUSINESS IN THE ROW AND IT IS NOT CLOSE. It led on operating
   margin in every single year 2021-2025** — 48.8 / 50.6 / 41.8 / 34.9 / 34.1 — and **its
   worst year beats every peer's best year in the window.** ROE 30.1% average against NXPI
   21.0%, ADI 6.6%, Infineon 5.9%, MCHP 3.4%, Renesas −2.1%, ON 1.5%, STM 0.9%. **At the
   bottom of the worst analog downcycle in twenty years, with three peers at or under 2%
   operating margins and two taking nine-figure impairments (ON $667.0M, STM $376M), TXN
   earned 34.1% and took a $117M restructuring charge.** That is [E5-18]'s capacity to stand
   a shock, observed rather than asserted.
2. **AND THE MOAT NARROWED ON EVERY FILED MEASURE.** Gross margin fell **11.8 points**
   (68.8 to 57.0) peak-to-trough — **sixth-worst of eight**, better only than STM (−13.4) and
   ON (−15.9), against Renesas +0.2, NXPI −2.2, Infineon −3.9, ADI −6.9, MCHP −11.4.
   **THE GROSS-MARGIN GAP OVER ADI INVERTED: +6.1 points in FY2022 (68.8 vs 62.7), −4.5
   points in FY2025 (57.0 vs 61.5).** The operating-margin lead over NXPI fell from 21.8
   points to 9.3. ROE halved, 62.7% to 30.1%.
   *(Defect caught in my own source and recorded rather than silently fixed: the sub-agent's
   summary quoted ADI's gross-margin change as −1.2 points, which is its FY2022-to-FY2025
   change, not its peak-to-trough. Its own detailed section gives −6.9 peak-to-trough, and
   that is the figure used above.)*
3. **THE ACLS TEST — "did the filed price range and gross margin hold through a revenue
   collapse?" — TXN FAILS THE GROSS-MARGIN HALF, AND THE PRICE HALF CANNOT BE ANSWERED
   BECAUSE NO PRICE IS FILED.** Revenue $20,028M to $15,641M (−21.9%) and gross margin gave
   up 11.8 points on the way down. The mechanism is filed and it is **fixed cost, not
   demand**: cost of revenue **ROSE from $6,257M (FY2022) to $7,599M (FY2025), +21%, while
   revenue fell 11.7%**, and depreciation rose **107%**, $925M to $1,918M. TXN's own policy
   note names it: *"Cost associated with **underutilization of capacity is expensed as
   incurred**."* Axcelis held its filed price range and RAISED gross margin through its
   collapse. TXN did not hold gross margin and files no price range at all.
4. **THE ROW'S DECISIVE STRUCTURAL FACT, AND IT CUTS BOTH WAYS: TXN IS THE ONLY COMPANY IN
   THE ROW STILL SPENDING ABOVE 2x DEPRECIATION.** ADI 1.31x, STM 1.20x, Infineon 0.94x,
   NXPI 0.71x, ON 0.62x, MCHP 0.59x; Renesas at 1.89x is the nearest. **Every peer cut capex
   to or below replacement; TXN raised capex intensity from 14.0% to 25.7% of revenue while
   revenue fell.** The bull reading: TXN bought capacity at the bottom while everyone starved
   theirs, and depreciated capacity earns for twenty years. The bear reading is **NXP's own
   words, which name TXN's exact mechanism**: *"In less favorable industry environments… we
   are generally faced with a decline in the utilization rates of our manufacturing
   facilities… **the fixed costs associated with the full capacity continue to be incurred,
   resulting in lower gross profit.**"* **The three most integrated names (TXN, STM, ON) took
   three of the four largest gross-margin hits; the two most fab-lite (ADI, NXPI) took two of
   the three smallest.** In THIS cycle vertical integration was a liability. Whether it
   becomes an asset in the next one is Q4's question and no filing answers it.

**[E2-44] — BOTH HALVES, AND THEY SPLIT.**
- **Half 1 (raise prices when demand is flat and capacity is not fully utilized): UNKNOWABLE
  from the filing shelf.** TXN files no price series in any vintage. The one thing it files
  about price points the other way: *"Rapid technological change … could contribute to
  shortened product life cycles and **a decline in average selling prices of our products.**"*
  The separating test asked aloud — *can I name the document that would resolve this?* — and
  the answer is **no**: no TXN 10-K, 10-Q, 8-K or proxy in any vintage discloses an ASP or a
  unit series, and no peer's filing contains TXN's prices. **UNKNOWABLE about that
  sub-question, not UNRESEARCHED.**
- **Half 2 (grow dollar volume with only minor additional investment of capital): FAILS on
  the recorded window; unresolved on the forward one.** $19,700M of capex FY2021-25 against
  operating profit of $6,023M (FY2025) versus $5,894M (FY2020): **+$129M on $19.7bn, a 0.65%
  incremental pre-tax return.** On the latest twelve months the same arithmetic gives
  **+$1,360M, 6.90%** — still below [E5-40]'s ~12% "quite satisfactory", still climbing as
  the fabs load. **This is not the [E2-44] shape; on the filed record it is nearer the
  [E4-20] "good" class than the "great" one.**

**[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. THE RECORDED SWEEP: THE PHYSICAL SERIES DOES
NOT EXIST, AND THE TWO PHYSICAL NUMBERS THAT DO EXIST HAVE NOT MOVED IN SIX AND THIRTEEN
YEARS.** FY2025 10-K, word-boundary counts: *unit volume* **0** · *units shipped* **0** ·
*wafer starts* **0** · *SKU* **0** · *part numbers* **0** · *catalog* **0** · *average
selling price* **1**, and it is the risk factor above saying prices fall. All eight *"units"*
hits are restricted stock units. The two stock figures, diffed across **fifteen 10-K
vintages**:
- *"over 100,000 customers"* — **identical in every 10-K from FY2012 (filed 2013-02-22)
  through FY2025.** It was *"90,000"* in the FY2011 10-K. **Thirteen consecutive filings,
  one number, never re-measured in public.**
- *"more than 80,000 products"* — **identical in every 10-K from FY2020 through FY2025.**

**A franchise claim resting on breadth is resting on two constants.** The one
physical-adjacent series that DOES move runs in TXN's favour and is real: distributor revenue
**30% → 25% → 20% → under 20%** FY2022-25 while direct went **70% → 75% → 80%**. That is TXN
taking the distributor's margin — and it is a one-time transition, not a perpetual term
**[E4-44]**.

**AND FIVE CHECKABLE DISCLOSURES WERE DELETED IN THE FY2025 VINTAGE, ALL IN THE YEAR THE
STORY CHANGED:** the **named-fab list** (SM1, SM2, RFAB2, LFAB1, LFAB2 — all now zero hits;
SM3 and SM4 never appeared in any 10-K), the **construction pipeline**, the **"10 to 15
years" horizon**, the **internal-sourcing percentages** (*"about 80% of wafers, 65% of
assembly/test"* in the FY2023 10-K became *"the majority"*), and the **"$7.5 to $9.5 billion
through 2034" CHIPS expectation**. No reason is filed for any of the five. They are recorded
here because they are precisely the disclosures an outsider would use to check the capacity
story, and they are the ones that went.

**[E3-33] / [E5-28] untapped pricing power: NOT CLAIMABLE.** Claiming that class is claiming
*"a monopoly or a near monopoly"*; TXN's own filing says *"highly fragmented … dozens of
large and small companies."* **[E4-37] the agony metric:** TXN files that its own ASPs
decline. Not the yawn end. **[E2-53] the dominance class: NO.**

**[E2-45] THE ATTACKER'S TEST — THE SUBJECT NAMES ITS OWN ATTACKER AND NAMES NO COMPANY.**
Recorded sweep of the FY2025 10-K: *Analog Devices* **0** · *Microchip* **0** · *NXP* **0** ·
*STMicroelectronics* **0** · *Infineon* **0** · *onsemi* **0** · *Renesas* **0** · *Broadcom*
**0** · *Qualcomm* **0** · *Silergy* **0** · *SG Micro* **0** · *3Peak* **0** · *Chinese*
**0**. **TXN NAMES ZERO COMPETITORS BY COMPANY NAME, and the entire Competition section is
168 words.** Three names in one week — AVGO, GOOGL, TXN — with the identical finding. What
TXN does name is the mechanism, in one sentence:
> "we may face increased competition as a result of **China actively promoting and reshaping
> its domestic semiconductor industry through policy changes and investment, which could
> prevent us from competing effectively.** Certain competitors possess sufficient financial,
> technical and management resources and **utilize available incentives offered by various
> countries and government entities** to develop and market products that may compete
> favorably against our products."

Exposure, same document: *"Revenue from end customers headquartered in China represented
about **20%** of our revenue in 2025, while **revenue from products shipped into China
represented about 50% of our revenue in 2025.**"* **Fifty percent, not twenty, is the number
the risk runs on**, and it is the one easy to miss. Peers corroborate the attacker from
independent filings: **MCHP mentions China-near-competition 19 times** (*"competition in
China is intense … changes in the Chinese market adversely impacted our sales volumes in
China"*; *"companies that we believe have **copied, cloned, pirated or reverse engineered**
our proprietary product lines in such countries as China and Taiwan"*); **STM names the
policy instruments** (*"its 5-year plans, the China Standards 2035 campaign and related large
scale national and local public funding schemes"*) and is building a **$3.2bn SiC joint
venture inside China** to answer it; **Infineon's is the sharpest** — *"the risk that an
increased volume of previously imported semiconductors will be manufactured in China."*
**NXPI and Renesas say nothing at all.**

**AND THE PRICING RECORD CANNOT SETTLE IT, BECAUSE NOBODY FILES PRICES.** What the record
does show is that TXN's margin compression is timed to **its own depreciation**, not to a
Chinese price event: of the 11.8-point gross-margin fall, the $993M depreciation increase
alone accounts for **5.6 points of FY2025 revenue**, roughly half, and the balance is
underutilisation and mix. **The Chinese-entrant thesis is neither confirmed nor refuted here.
It is carried to Q6 as the named monitoring item.**

**Class: [ ] WIDE  [x] NARROW  [ ] NONE  [ ] PROVISIONAL · Direction: NARROWING**

**VERDICT: [x] IN (NARROW, narrowing).** Stated so it can be attacked: the durable half of
the moat — 80,000 catalogue parts inside 100,000 customers' designs, half of revenue outside
the top 50, no design win decisive — is real, is the source of the 34.1%, and does **not**
need rebuilding. The half TXN spent $19.7bn on **does** need rebuilding, is being rented by
competitors from foundries and states for a fraction of the money, and **has produced no
owner return yet**. **A moat that is measurably the best in its row and measurably narrower
than it was three years ago is NARROW — not WIDE, and not OUT.** OUT means the evidence is in
and the business fails; a company earning 34.1% and 30% ROE at the bottom of its cycle, while
three of eight peers earn under 2%, has not failed.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?

**STEP 1 — THE WEIGHT CASE. Declared first; nothing below counts until it is.**
- [ ] **Daily execution [E3-38]** — **ARGUED AND REFUSED, on a natural experiment inside the
  window.** TXN made one large operating misjudgment — buying the Lehi fab in October 2021
  for $893M and loading it into Embedded Processing — and **Embedded Processing operating
  profit fell from $1,253M (FY2022) to $304M (FY2025), a 76% destruction of an entire
  segment, margin 38.5% to 11.3%** — while the company still earned 34.1% overall and
  **Analog's margin ROSE** in FY2025 (37.9% to 38.6%). That is [E5-18]'s *"capacity to stand
  it, if we stumble into it"* observed, not assumed. Not a have-to-be-smart-every-day business.
- [ ] **Control [E1-16]** — no. Public minority position.
- [ ] **Leverage [E3-29]** — **ARGUED AND REFUSED.** $14,048M of debt against $34,585M of
  assets and $16,273M of equity: **assets/equity 2.13x**, debt/OCF 1.96x, **[E2-54] coverage
  = (OCF $7,153M − capex $4,550M) ÷ interest $543M = 4.8x on the worst construction, 9.5x on
  the TTM at the guided capex rate**; $9,150M of $14,150M principal falls in "thereafter",
  maturities running to 2063; revolver undrawn, no commercial paper. [E3-29]'s test is
  whether small asset errors destroy equity. At 2.1x they do not.

**None ticked → Q3 IS A QUALITATIVE OVERLAY.** Findings are recorded; none can stop this run,
and under the guardrail none can start it either.

**HONESTY — binary, permanent, filings-based [E5-16]. NO DISQUALIFIER FOUND.** No integrity
matter, no restatement, no enforcement action in the window. **Three 10-K amendments in the
company's entire EDGAR history, all before 2001; 26 consecutive unamended annual reports,
FY2000-FY2025.** ICFR opinion unqualified, `IcfrAuditorAttestationFlag` true. **Both
Dodd-Frank cover boxes UNCHECKED** (visual and XBRL agree). One CAM, *"Uncertain tax
positions"*. Ernst & Young **since 1952** — 74 years, with a stated five-year lead-partner
rotation; non-audit fees **14.6%** of total, 9.1% excluding audit-related. Written per
[E5-17]: **this is the absence of found disqualifiers, not a finding that the managers are
honest.**
*(One historical item recorded rather than buried, because it is exactly this framework's
subject matter: the FY1998 10-K405/A was SEC-comment-driven and the SEC forced TI to reorder
its MD&A to put GAAP ahead of results excluding special charges — the original led with 10.9%
margins ex-charges and $1.79 EPS, burying GAAP's 4.7% and $1.02. That is 28 years old, sits
outside every window used here, and the record since 2000 is clean.)*

**STEP 2 — THE FLAGS. Recorded counts, FY2025 10-K.**
- [ ] weak accounting — **does not fire.** SBC expensed in full; no pension exotica.
- [ ] unintelligible footnotes — **does not fire.** The 10-K is short and unusually plain.
- [x] **trumpeted projections — FIRES ONCE, and it is a large one.** FY2022 10-K: *"Going
  forward, we expect **increased capital expenditures to be the largest driver of free cash
  flow growth over the next 10 to 15 years.**"* **[E3-48] action taken — set against
  outturn:** three years on, free cash flow per share **ex the government money** is **$5.39
  (TTM) against $6.40 (FY2022) and $6.72 (FY2021)**. Not falsified — it is a 10-to-15-year
  claim — and not met so far. **And the sentence carrying that horizon was itself deleted in
  the FY2025 vintage.** **[E5-30]'s ratchet is NOT engaged in the filings**: *guidance*
  returns **0 hits** and *outlook* **1**, and no earnings projection appears in any filed
  document. *(Limit stated: TXN does give quarterly revenue and EPS ranges in furnished press
  releases; those were not tested in this run.)*
- [ ] serial share issuance **[E5-15]** — **does not fire** on its face: 1,278M shares (2008)
  to 907M (2025), −29%. **But see [E5-08] below — the shrinking has stopped.**
- [ ] EBITDA promotion **[E4-29]** — **does not fire. "EBITDA" returns ZERO hits.** So do
  *pro forma* (0) and *except for* (0). *Consecutive* returns 1 and it is a pension formula.
- [x] **filed-figure tells [E4-30] — THE CASH-TAX TELL FIRES MECHANICALLY AND READS CLEAN.**
  Cash taxes paid as a share of reported pre-tax income: **18.2% (2023) → 8.3% (2024) →
  5.2% (2025).** Precisely the pattern [E4-30] names. **And TXN volunteers the answer in a
  supplemental table** — *"Total cash taxes paid 556 / ITC proceeds from CHIPS Act incentives
  (260) / Total cash taxes paid, net of refunds $296"* and separately *"**Total cash taxes
  paid without CHIPS Act incentives $891**."* Giving the reader the number both ways is
  [E2-26]'s half-owner standard met. **Reported growth is the opposite of smooth**: operating
  profit 10,140 → 7,331 → 5,465 → 6,023.
- [x] **A SIXTH THAT THE TEMPLATE DOES NOT LIST BUT THE GOOGL RUN'S METHOD FINDS: USEFUL
  LIVES WERE LENGTHENED TWICE DURING THE BUILD, BOTH UNLABELLED.** Machinery and equipment
  went from **"2 to 10 years" to "5 to 10 years" in the FY2023 vintage**; buildings and
  improvements went from **"5 to 40 years" to "Up to 40 years" in the FY2024 vintage**.
  **Neither carries a change-in-accounting-estimate heading, a rationale, or a dollar
  effect.** Same shape as Alphabet's five movements, at smaller scale: both run in the
  direction that suppresses depreciation, and both land inside the window in which
  depreciation is the whole argument.

**[E2-49] — METRIC-SWITCHING. THIS IS THE Q3 HEADLINE AND IT FIRES FOUR TIMES. Each removed
or redefined a number in the vintage that number stopped flattering. NOT ONE was announced
ahead with a reason, which is the candor case [E2-49] contrasts them against.**

1. **THE PROMISE.** *"Our strategy is to return **all** free cash flow to shareholders"* — in
   the FY2017, FY2018 and FY2019 10-Ks. **Deleted from the FY2020 10-K, filed 2021-02-05.**
   Never restored. Capex was $649M in FY2020 and $2,462M in FY2021: **the sentence came out
   BEFORE the capex line moved — when management knew and the reader did not.** It survives,
   strengthened, in the September dividend 8-Ks with a hedge attached: *"over time."*
2. **THE COVERAGE RATIO.** *"Our dividends represented **X%** of free cash flow, underscoring
   their sustainability"* — filed every year FY2016-FY2021 (**40 / 45 / 42 / 52 / 62 / 62%**).
   **Dropped in the FY2022 10-K; absent since.** Computed for the silent years: **FY2022 73%
   · FY2023 338% · FY2024 320% · FY2025 192%.** The disclosure stopped in the first year it
   would have exceeded roughly two-thirds and stayed stopped through three years in which the
   dividend alone exceeded free cash flow.
3. **THE CONCENTRATION YARDSTICK.** *"more than 40% of our revenue derived from customers
   outside our **largest 100**"* (FY2021-FY2023) became *"about half of our revenue derived
   from customers outside of our **largest 50**"* in the FY2024 10-K — the vintage after
   revenue fell 22%. The old basis was not restated; the two cannot be compared.
4. **AND THE SHARPEST: THE PRIMARY METRIC ITSELF WAS REDEFINED, IN THE YEAR IT WAS WORST.**
   TXN's stated *"best metric for owners"* is free cash flow. In the FY2025 10-K it is
   defined as *"cash flows from operating activities less capital expenditures, **plus
   proceeds from CHIPS Act incentives**"* — a definition that did not previously exist. It
   raises FY2025 free cash flow from **$2,603M to $2,938M, +12.9%**. **And the CHIPS money is
   counted TWICE inside the same metric**: $335M sits inside operating cash flow as a
   reduction of taxes payable, and $335M is added back again as an investing proceed. On the
   pre-2025 definition, TTM free cash flow is **$5,355M, not $6,534M**.

**THE COMPANION FINDING, AND IT IS ITS OWN [E2-26] FAILURE: "free cash flow per share" is
used ten times in the FY2025 10-K, is called *"the ultimate measure to generate value"* —
AND THE FIGURE IS NEVER COMPUTED OR RECONCILED ANYWHERE IN THE DOCUMENT.** The reader is
handed the yardstick and refused the reading.

**STEP 3 — THE PRIMARY TEST [E2-01], AS A SERIES.** Net income ÷ ending equity:
**62.0% (2018) · 56.3% (2019) · 60.9% (2020) · 58.3% (2021) · 60.0% (2022) · 38.5% (2023) ·
28.4% (2024) · 30.7% (2025)**, and 30.1% on average equity. **The primary test has halved.**
Denominator re-scoped per [E2-47]/[E2-43], because TXN now carries $14.0bn of debt and $4.3bn
of goodwill: on **unleveraged net tangible operating assets** — total assets $34,585M less
cash and short-term investments $4,881M less goodwill $4,330M less non-interest-bearing
current liabilities $2,659M = **$22,715M** — FY2025 operating profit of $6,023M is **26.5%
pre-tax**, and that denominator contains several billion dollars of fab earning nothing yet.
**The business earns extraordinary returns on the capital that is working. What halved the
reported ROE is capital that has been added and not yet loaded.**

**[E2-56] THE PRO-AM SPLIT — and TXN's consolidated series is camouflaging the same way.**
Segment operating profit, FY2022 → FY2025: **Analog $8,359M → $5,412M** (margin 54.4% →
38.6%) and **Embedded Processing $1,253M → $304M** (38.5% → 11.3%). The blended 34.1% conceals
that **one segment is carrying the whole company and the other has been reduced to a
rounding error by a fab decision** — and TXN names the cause itself: *"Our LFAB facility,
which primarily supports our Embedded Processing business, was purchased as an operating fab
and is in the early stages of ramping … Until LFAB ramps, we expect Embedded to carry
manufacturing costs that disproportionately affect Embedded Processing operating profit as
compared to Analog."* **The attribution cannot be closed and that is a finding, not a gap in
my work: TXN files NO segment capex, NO segment assets and NO segment depreciation** —
*"depreciation expense is not an independently identifiable component within the segments'
results"*; *"With the exception of goodwill, we do not identify or allocate assets by
operating segment."* **UNKNOWABLE, not UNRESEARCHED.** The candor half is a pass: TXN
publishes the ugly Embedded line every year rather than burying it.

**[E2-30] THE INSTITUTIONAL IMPERATIVE — SCORE ALL FOUR.** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [x] **(1) resists change in current direction** — mildly. Say-on-pay has run 83-87% for
  five years and the committee's response is verbatim identical every year: *"determined that
  it was not necessary at this time to make any material changes."*
- [x] **(2) projects or acquisitions materialise to soak up available funds — FIRES, and the
  timing is the textbook shape.** On **2026-02-04**, in the same document that announces the
  capex cycle is ending and $2-3bn of annual cash is about to be freed, TXN agreed to acquire
  **Silicon Labs at $231.00 per share, ~$7.5 billion enterprise value, all cash** — its first
  acquisition since National Semiconductor in 2011, **8.4x the Lehi purchase and 46% of total
  stockholders' equity** — funded *"with a combination of cash on hand and debt financing"*,
  with a **$5 billion 364-day delayed-draw term loan** entered in June 2026 on top of $14.0bn
  of existing debt, and **landing in the 11.3%-margin segment, not the 38.6% one.** **THE
  ABSOLUTE-SIZE ACQUISITION GATE (new, 2026-09-06) CATCHES THIS AND `acquisition_flag()`
  WOULD NOT: $7.5bn against a $236,020M cap is 3.2%, under the 15% threshold — the same tool
  defect the AVGO run recorded, now confirmed at a fifth of the size.** The deal closes in
  H1 2027 and sits outside every owner-earnings window in this file; it is recorded here as
  an allocation event and at Q6 as a window-resetting catalyst.
- [ ] (3) staff studies produced to justify a craving — not observable; no evidence either way.
- [ ] **(4) peer behaviour mindlessly imitated — DOES NOT FIRE, AND THE OPPOSITE IS TRUE.**
  Every peer in the row cut capex to or below depreciation; TXN raised it to 2.37x. Whether
  that was right is Q4's question, but it was **not imitation**. Credit recorded.

**CAPITAL ALLOCATION — [E5-08]'s TWO CONDITIONS PLUS [E4-31]'s THIRD.**
- **(1) ample funds for operations and liquidity? PASS today — and the [E2-60] limb FIRES.**
  *"restricted earnings are those whose payout costs the business … **its financial
  strength**."* FY2023-25, TXN returned **$17,050M** against **$5,450M** of cash generated
  after capex, and issued **$7,179M of new long-term debt** over the same three years.
  Long-term debt went from **zero in FY2008-09 to $14,048M**. **Retained earnings actually
  FELL in FY2025**, $52,262M → $52,236M, because $4,999M of dividends consumed the entire
  $5,001M of net income before a dollar of buyback. *"A company that consistently distributes
  restricted earnings is destined for oblivion"* is a strong sentence and TXN is nowhere near
  it — but the mechanism [E2-60] names is live, and its stated consequence is followed:
  **(c) was understated during the payout years, and this run therefore does not rest on the
  D&A end.**
- **(2) repurchases at a material discount to conservatively calculated IV? FAILS against my
  own range — and the record is markedly better than the average failure.** Average
  repurchase price: **$36.98 (2013) · $60.09 (2016) · $103.07 (2018) · $108.96 (2020) ·
  $181.72 (2021) · $162.84 (2022) · $162.78 (2023) · $197.66 (2024) · $173.76 (2025)**;
  blended **$107.25 over ten years and 206.5M shares**. Every year from 2021 is above this
  run's value range (Q5). **But [E4-26] requires the disconfirming half first, and it is
  substantial: TXN cut repurchases to $527M (2021) and $293M (2023) — 10% and 6% of the 2018
  level — exactly when the price was highest and the capital was most needed elsewhere. That
  is the INVERSE of the AVGO finding, where the largest buyback in company history was made
  at the highest price ever paid.** No 10-K in 22 years states a price limit or a valuation
  test; the only filed rationale is *"the accretive capture of future free cash flow for
  long-term investors"*, which asserts the outcome and names no test that could fail. **AND
  THE DENOMINATOR HAS STOPPED WORKING: shares outstanding went 919M (2020) to 913M
  (2026-06-30), with issuance exceeding repurchases in 2021, 2023, 2024 and H1 2026** — for a
  company whose sole stated objective is free cash flow **per share**, the per-share lever has
  been idle for five years. **CAPITAL-ALLOCATION FLAG, with the humility clause [E4-13]: it
  rests on my range, and management knows the business better than I do. It binds position
  size, never the discount rate.**
- **(3) [E4-31] — were shareholders supplied all the information they need to estimate value?
  NO, AND THIS IS THE CONDITION THAT ACTUALLY FAILS.** No unit series, no price series, no
  segment capex, no segment assets, no segment depreciation, the dividend coverage ratio
  withdrawn, the fab-level construction detail deleted, and the primary metric named ten times
  and never computed.
- **[E2-52] dividends funded by issuance: does NOT fire on its own terms** — TXN issued no
  stock and is a net repurchaser. The debt-funded variant is captured at [E2-60] above.

**[E4-52] — DO THE FLAGS CONVERGE? YES, AND THEY CONVERGE ON ONE LINE OF THE CASH-FLOW
STATEMENT.** Four withdrawals or redefinitions, two unlabelled useful-life extensions, the
pay program and the payout policy all sit on **opposite sides of the capex line**. The two
numbers withdrawn — the return-all-FCF promise and the dividend coverage ratio — are *below*
capex. The redefinition flatters a metric *below* capex. The useful-life extensions suppress
a charge *driven by* capex. And **the Company-Selected Measure in the Item 402(v) pay table
is "Operating Profit" — which sits *above* capex — while the metric TXN tells owners is
primary, free cash flow per share, is not a pay metric at all, does not appear in the 402(v)
tabular list (revenue growth · operating profit · operating profit margin · TSR), and is
never computed in the 10-K.** **Management is measured on the line a $19.7bn capital
programme does not touch, and stopped publishing the lines it does.** [E4-52] says to read
that as one reinforcing system rather than a sum of prompts, and this run does.

**THE PAY FINDING. The disconfirming half goes first [E4-26].**
**FOR TXN, and it is genuinely unusual: there are no performance conditions in the pay
program at all.** No PSUs, no performance shares, no TSR modifier, no EPS or ROIC gate; RSUs
are four-year cliff time-vesting and options vest 25% a year. The committee states four
separate times that it *"does not rely on formulas or performance targets or thresholds"*,
with a filed rationale (*"thresholds established at the beginning of a year could prove
irrelevant by year-end"*). **A pay program with no metrics structurally cannot dispose of a
yardstick and cannot be gamed the way the AVGO AI-revenue PSU can.** No pledging (*"No
director or executive officer has pledged shares"*); hedging prohibited.
**AGAINST, and the 402(v) table is the worst this queue has recorded: TI Total TSR on a $100
base is $121.78; the S&P Information Technology index over the identical five-year period is
$258.38. TXN returned 22% while its own chosen comparator returned 158% — a 136-point
shortfall — and it lost to the index in four of five years with the gap widening in each of
the last three.** Compensation actually paid to the PEO in 2025 was **$17,392,255** in a year
TSR fell from $127.47 to $121.78. In 2025 TSR was −4.5% and three-year revenue CAGR −4.1%,
both below the peer median, **and bonuses were raised 10%**. Pay ratio **272:1**. Officers
and directors as a group own **0.60%, and 0.23% net of options**; the CEO owns about **46,000
real shares**. Say-on-pay **83.0% (2026)**, down four points to a five-year low, with roughly
one share in six voted against in each of five consecutive years. Chairman and CEO were
**recombined on 2026-01-01**. The pay-benchmark group's median revenue is **1.75x** TXN's.

**THE GUARDRAIL — checked before the verdict is written.**
- [x] Nothing in this Q3 is used to promote the name. The [E2-49] findings are recorded and
      do not demote it either — the Q5 verdict below is reached without any of them.
- [x] This business does not require a great manager. Recorded at Q2 as the *opposite* of a
      key-person defect: [E5-18]'s capacity to stand a stumble was demonstrated on Embedded.
- [x] No great manager is the reason to act, so [E2-35]/[E2-36] does not arise.

- **VERDICT: [x] IN — as an OVERLAY, meaning no disqualifier was found.** [E2-49] fires four
  times, [E2-30](1) and (2) fire, two unlabelled useful-life extensions are recorded,
  [E5-08] condition 2 fails and [E4-31] condition 3 fails, and the [E4-52] convergence is
  stated. **None of these is an integrity finding [E5-38]** — they read the accounting, and
  the conduct record over 26 unamended annual reports is clean. **IN never promotes.**

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**

**OWNER EARNINGS BY YEAR, BY HAND (OCF − SBC − (c)), $M.** Both ends shown; capex end left,
depreciation end right. All figures from the filed cash-flow statements.

| FY | OCF | SBC | capex | depr | **OE, capex end** | **OE, D&A end** | capex/depr | capex % rev |
|---|---|---|---|---|---|---|---|---|
| 2016 | 4,614 | 252 | 531 | 605 | **3,831** | 3,757 | 0.88x | 4.0% |
| 2017 | 5,363 | 242 | 695 | 539 | **4,426** | 4,582 | 1.29x | 4.6% |
| 2018 | 7,189 | 232 | 1,131 | 590 | **5,826** | 6,367 | 1.92x | 7.2% |
| 2019 | 6,649 | 217 | 847 | 708 | **5,585** | 5,724 | 1.20x | 5.9% |
| 2020 | 6,139 | 224 | 649 | 733 | **5,266** | 5,182 | 0.89x | 4.5% |
| 2021 | 8,756 | 230 | 2,462 | 755 | **6,064** | 7,771 | 3.26x | 13.4% |
| 2022 | 8,720 | 289 | 2,797 | 925 | **5,634** | 7,506 | 3.02x | 14.0% |
| 2023 | 6,420 | 362 | 5,071 | 1,175 | **987** | 4,883 | **4.32x** | 28.9% |
| 2024 | 6,318 | 387 | 4,820 | 1,508 | **1,111** | 4,423 | 3.20x | **30.8%** |
| 2025 | 7,153 | 419 | 4,550 | 1,918 | **2,184** | 4,816 | 2.37x | 25.7% |
| **TTM to 2026-06-30** | **8,667** | **410** | **3,312** | **2,122** | **4,945** | **6,135** | **1.56x** | **17.0%** |

### THE WINDOWS — MORE THAN ONE, AND THE SPREAD IS PART OF THE RANGE **[E4-25]**

| window | OE, capex end | yield | OE, D&A end | yield |
|---|---|---|---|---|
| **3-yr (FY2023-25)** | **1,427** | 0.60% | 4,707 | 1.99% |
| **5-yr (FY2021-25) — the corpus default [E2-42]** | **3,196** | 1.35% | 5,880 | **2.49%** |
| **8-yr (FY2018-25)** | 4,082 | 1.73% | 5,834 | 2.47% |
| **10-yr (FY2016-25)** | 4,091 | 1.73% | 5,501 | 2.33% |
| **pre-build 5-yr (FY2016-20) — the maintenance anchor** | **4,987** | 2.11% | 5,122 | 2.17% |
| **TTM to 2026-06-30 (all filed)** | **4,945** | 2.10% | **6,135** | **2.60%** |

### THE SCREEN ROW REPRODUCES TO THE DOLLAR — AND THE FOURTH SPREAD DEFECT FIRES IN REVERSE

`tools/run.py TXN` returns oe_lo **1,427** / oe_hi **4,707** on the 3-year window and
**3,196 .. 5,880** on the 5-year, with a stated conservative-end divergence of **+123.9%**.
**Every one of those four numbers reproduces exactly from my own hand-built series** —
1,427.3 / 4,707.3 / 3,196.0 / 5,879.8 — so the screen is arithmetically clean and the
reconciliation to TXN's own filed free cash flow (Step 0) closes it a second way.

**BUT THE FOURTH SPREAD DEFECT — three confirmations in three days at AAPL, GOOGL and AVGO —
FIRES HERE IN THE OPPOSITE DIRECTION, AND THAT IS THE FINDING.** At those three names the
four-construction spread could not see variation older than five years and read **flatteringly
narrow**. At TXN it reads **UNFLATTERINGLY narrow at the bottom.** Rebuilt over my own six
windows **[E4-25]**:
- The screen's conservative end of **1,427** is the single most pessimistic of the ten
  constructions above. It sits **65% below the 10-year conservative end (4,091)** and **71%
  below the pre-build maintenance anchor (4,987)**.
- The screen cannot see FY2016-2020 at all — **and those are precisely the years that tell you
  what maintenance capex actually costs this business.**
- Full width across my own windows: **1,427 to 6,135, a 330% span**, against the screen's
  1,427-5,880 (312%). Similar magnitude; **opposite bias.**

**THE DEFECT IS THEREFORE NOT "THE SCREEN READS TOO NARROW." IT IS "A FOUR-CONSTRUCTION
SPREAD PINNED TO THE LAST FIVE YEARS INHERITS WHATEVER THOSE FIVE YEARS HAPPEN TO BE."** At
three AI-capex names it inherited a boom and flattered; at a name mid-way through a capital
cycle it inherits the trough and condemns. **The remedy is the same either way and it is
[E4-25]'s: rebuild the width over your own windows.** Fourth confirmation in four days,
first one in this direction.

### THE (c) JUDGMENT — THE WHOLE FILE, AND IT IS A DISCLOSED GUESS **[E2-23]**

*"(c) must be a guess — and one sometimes very difficult to make."* Here is the guess and
every piece of evidence behind it, for and against.

**THE CASE THAT THE CAPEX IS GROWTH AND THE D&A END IS THEREFORE VALID:**
1. **TXN says so, in the filing, in dollars.** *"We are nearing the end of our **six-year
   elevated capital expenditures cycle**, and consistent with our capital management strategy,
   we are **expecting to spend about $2 billion to $3 billion in 2026**."* And: *"we allocated
   about $24 billion to capital expenditures **to support future revenue growth**."*
2. **It is already happening in filed numbers.** H1 2026 capex **$1,190M against $2,428M** in
   H1 2025 — **down 51%**, annualising to ~$2.4bn, inside the guided range.
3. **THE PRE-BUILD RATIO IS THE EMPIRICAL ANCHOR AND IT IS SQUARELY THE [E3-44]/[E2-41]
   DEFAULT CLASS.** FY2016-2020, when TXN was simply maintaining a working analog business:
   **capex averaged $771M against depreciation of $635M — a ratio of 1.21x — and capex ran
   5.3% of revenue.** [E5-20]'s railroad exception requires the true maintenance number to be
   *"higher than 60 percent"* of total capex and depreciation to be structurally inadequate;
   at TXN, over five ordinary years, depreciation was 82% of capex.
4. **Capex/depreciation is CONVERGING, not diverging.** 4.32x (2023) → 3.20x → 2.37x →
   **1.56x TTM.** Compare the three names this brief calls TXN's inverse: **GOOGL 5.25x and
   widening, MSFT 3.38x, ORCL 7.30x.** TXN is walking back toward 1.0x while they walk away
   from it.
5. **The asset base is young and will keep generating depreciation without new cash.**
   Accumulated depreciation is **$5,362M against gross PP&E of $17,682M — only 30.3%.**

**THE CASE THAT THE CAPEX END IS THE HONEST ONE AND (c) MUST BE JUDGED UP:**
1. **REPORTED DEPRECIATION IS ARTIFICIALLY SUPPRESSED, AND THE FILING SAYS BY HOW MUCH.**
   *"The CHIPS Act incentives have **reduced the carrying amounts of manufacturing assets by
   $4.51 billion** … Cost of revenue benefited by **$353 million, $159 million and $45
   million** from the CHIPS Act incentives, **recognized as a reduction of depreciation
   expense** in 2025, 2024 and 2023."* **Grossed up, FY2025 depreciation is ~$2.27bn, not
   $1.92bn — 18% higher.** A subsidy is not a reason the plant lasts longer.
2. **TWO UNLABELLED USEFUL-LIFE EXTENSIONS INSIDE THE BUILD** (Q3): machinery 2-10 → 5-10
   years (FY2023) and buildings 5-40 → "Up to 40" (FY2024), both suppressing the charge,
   neither with a stated dollar effect.
3. **[E2-60] fires: leverage rose to fund the payout**, so (c) was understated during those
   years by construction, and the framework says the D&A end may not be leaned on.
4. **The build is not finished, and TXN says the tap can reopen**: *"Beyond 2026, capital
   expenditures will be **dependent on revenue and growth expectations**."* Sherman is
   designed for four fabs; SM1 is ramping and SM3/SM4 have never appeared in any 10-K.
5. **[E4-47]**: replacement plant in current dollars outruns depreciation charged in old
   dollars, and a 300mm fab is the asset-heavy class that rule is written for.

**THE JUDGMENT, AND IT DOES NOT DEFAULT TO EITHER END: (c) = $2,600M PER YEAR.** It is placed
where three independent filed anchors meet — **TXN's own guided post-build capex of $2-3bn**,
**CHIPS-grossed-up depreciation of ~$2.3-2.5bn**, and **the pre-build 1.21x capex-to-depreciation
ratio applied to that depreciation** — then nudged up $100M for the two unlabelled life
extensions. It is roughly **3.4x** the pre-build maintenance rate of $771M, because the plant
being maintained is roughly three times larger and newer.

**SO: THIS IS THE [E3-44]/[E2-41] DEFAULT CLASS, NOT THE [E5-20] EXCEPTION — AND THE ANSWER
IS DECIDED FROM THE FILINGS RATHER THAN DEFAULTED, AS THE BRIEF REQUIRED. THE BRIEF'S PRIOR
THAT "[E5-20] CUTS BOTH WAYS" IS RIGHT ON THE ARGUMENT AND WRONG ON THE OUTCOME: TXN'S OWN
FILED PRE-BUILD RECORD SHOWS DEPRECIATION AT 82% OF CAPEX OVER FIVE ORDINARY YEARS, WHICH IS
NOT THE RAILROAD.** But it changes almost nothing, and that is the second half of the answer:

**AND HERE IS WHY THE (c) JUDGMENT, WHICH THE BRIEF EXPECTED TO DECIDE THE MAGNITUDE, DOES
NOT DECIDE ANYTHING. Every construction available:**

| construction | OE | yield |
|---|---|---|
| TTM, ITC stripped from OCF, **gross** capex (strictest defensible) | **4,512** | 1.91% |
| TTM, ITC stripped, **judged (c) = 2,600** | **5,224** | 2.21% |
| TTM, ITC stripped, (c) = reported depreciation 2,122 | 5,702 | 2.42% |
| TTM, ITC stripped, capex **net of all CHIPS receipts** | 5,691 | 2.41% |
| **TXN's own redefined TTM free cash flow, $6,534M, less SBC** (most generous constructible) | **6,124** | **2.59%** |
| FY2021, the single best year in the company's history, D&A end | 7,771 | 3.29% |

**THE ENTIRE (c) DEBATE MOVES THE YIELD FROM 1.91% TO 2.59% — SIXTY-EIGHT BASIS POINTS — AND
EVERY POINT OF IT SITS BETWEEN 2.65 AND 3.33 POINTS BELOW A 5.24% GOVERNMENT BOND. THERE IS
NO CONSTRUCTION, ON ANY WINDOW, AT EITHER END OF THE CAPEX BAND, INCLUDING THE BEST YEAR THE
COMPANY HAS EVER HAD, THAT PAYS WHAT THE SOVEREIGN PAYS.**

**THE CHIPS ACT, TREATED HONESTLY.** It is real, filed and large: **$3.35bn of receivables at
2025-12-31** ($1.71bn current, $1.64bn long-term), **cumulative $4.51bn of reduction to the
carrying amount of manufacturing assets**, direct funding of **up to $1.6bn**, and an ITC
raised from **25% to 35%** by the OBBBA for assets placed in service after 2025-12-31. Cash
received: $588M (2024), $670M (2025), **$1,405M in H1 2026 alone**. **It is NOT owner
earnings — it is a reduction of the capital bill, and it is treated that way here:** the ITC
benefit sitting inside operating cash flow (**$433M TTM**) is stripped out of every judged
number above, and the receipts are shown as an alternative reduction of (c) rather than as
income. **TXN does the opposite**: its redefined free cash flow counts the same money twice,
once inside OCF as a tax reduction and once again as an added-back investing proceed.

**Stock compensation subtracted in full [E5-06]: $410M TTM, 2.1% of revenue** — the lowest in
the competitor row and a fraction of AVGO's 11.8%. **[E3-70] recorded and not stacked**: the
market-value measure would be higher than the accounting charge, but at 2.1% of revenue the
difference cannot move a verdict that is three points from the bond.

**ASC 842 — IMMATERIAL, and the vocabulary is absent entirely.** Total lease expense **$162M
(0.92% of revenue)**; total lease liabilities **$731M against $14,048M of debt**; **finance
leases: ZERO** — *"finance lease"*, *"capital lease"*, *"right-of-use"*, *"ASC 842"* and
*"sale-leaseback"* all return **0 hits**; TXN carries the ROU asset inside *"Other long-term
assets"*. New lease originations collapsed **$285M (2023) → $241M (2024) → $26M (2025)**.
**SOFTWARE-CAPEX LINE — IT EXISTS AND IT IS TINY.** *"Capitalized software licenses $238M"* on
the balance sheet and *"Amortization of capitalized software $81M"* in the cash-flow statement
— 0.45% of revenue, amortised above the OCF line, so already inside owner earnings. No
distortion. **CONTINGENT-LIABILITY PERSISTENCE — DOES NOT FIRE: there is nothing to persist.**
No contingency accrual is disclosed; legal proceedings appear only as risk-factor language.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — [x] **GOOD, and travelling** — [ ] gruesome

**Evidence, both directions.** On the capital that is *working*, TXN earns **26.5% pre-tax on
unleveraged net tangible operating assets** — far above [E5-40]'s ~12% "quite satisfactory",
and the best in an eight-name row. **On the capital that was *added*, it earns 0.65% over the
recorded window (FY2020 → FY2025 operating profit, +$129M on $19,700M) and 6.90% on the latest
twelve months (+$1,360M).** That is [E4-20]'s *good* account exactly: *"an attractive rate of
interest that will be earned **also on deposits that are added**"* — except the deposits are
so far earning about a quarter of what the existing balance earns. **[E4-43] governs and it is
carried honestly: the good class PASSES.** It is not gruesome — gruesome requires growing
rapidly and earning little, and TXN grows at 4% and earns 34.1%. It is not great — great
requires little capital, and TXN just spent 25.7% of revenue for two years.

### Staying power — score all three **[E5-11]**
1. **(1) large and reliable stream of earnings — PASS.** Operating profit never fell below
   $5,465M in ten years, including the worst analog downcycle in twenty; 34.1% operating
   margin at the trough; 100,000 customers with half of revenue outside the top 50; **no 10%
   customer is disclosed in any vintage.**
2. **(2) massive liquid assets — PASS, but not "massive."** $3,660M cash + $3,340M short-term
   investments = **$7,000M at 2026-06-30**, plus $3.35bn of CHIPS receivables, against
   $14,048M of debt. Adequate, not fortress.
3. **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASS ON THE CONTRACTUAL TEST, AND THIS
   IS WHERE THE QUALIFICATION LIVES.** Twelve-month contractual claims: current debt **$1,149M**
   + operating lease payments **$122M** + purchase commitments **$440M** = **$1,711M against
   $7,000M of liquid assets = 4.1x**, and **[E5-39] observed: no revolver drawn and no
   commercial paper outstanding are counted, and TXN states both are unused.** **BUT the
   dividend is $5.2bn a year, is not contractual, and carries a 22-year unbroken streak that
   TXN has never once treated as optional.** Add it and the twelve-month call is **$6,911M
   against $7,000M of liquid assets — 1.01x**, covered by the **$8,667M** of TTM operating
   cash flow and not by the balance sheet. **And the $7.5bn Silicon Labs purchase is funded by
   a $5bn delayed-draw term loan — which is precisely [E5-39]'s "kindness of strangers."**
   The third strength passes and it passes on the income statement, which is the position
   [E5-11] says most often surprises people.

**Leverage, named and quantified [E4-16, E3-29]** — no ratio ceiling exists in this framework
and none is invented: **$14,048M of principal, $9,150M of it "thereafter" with maturities to
2063; assets/equity 2.13x; debt/OCF 1.96x; [E2-54] coverage 4.8x on the worst construction and
9.5x on the TTM at the guided capex rate; no financial covenant disclosed; revolver undrawn.**

### Name the specific way THIS business dies **[E2-27, E3-24]**
**[E4-40] applied first: model EXPOSURE, not experience.** TXN's benign loss history is
useless here; what the filing shows it is exposed to is a fixed-cost base built for a revenue
level it has not reached, sold half into one country that has declared its intention to
replace it.

1. **CHINESE DOMESTIC ANALOG TAKES THE COMMODITY END. A REAL POSSIBILITY.** Mechanism named
   by TXN itself and corroborated by MCHP, STM and Infineon from independent filings.
   Quantified: **$3,781M (21%) of revenue is from China-headquartered end customers and ~50%
   of revenue ships into China.** Halve the China-headquartered leg and, because underused
   capacity cost *"is expensed as incurred"*, essentially all of the lost gross profit falls
   to operating profit: **−$1,890M of revenue and roughly −$1,890M of operating profit, 31%
   of FY2025's $6,023M.** Owner earnings would fall to roughly $3.3bn and the yield to ~1.4%.
2. **THE FABS NEVER LOAD. A REAL POSSIBILITY, AND THERE IS ALREADY A WORKED EXAMPLE INSIDE
   THE COMPANY.** Lehi was bought in October 2021 and is still described as *"in the early
   stages of ramping"* **five years later**, and the segment carrying it earns **11.3%
   against Analog's 38.6%**. Quantified: depreciation is going from $1,918M toward $2.5-3.0bn
   as the remaining fabs are placed in service; **every $500M of unabsorbed depreciation is
   2.6 points of gross margin and 8.3% of FY2025 operating profit.** If revenue stalls near
   $19-20bn, the full ramp costs roughly **$1.0bn of operating profit, 17%.**
3. **THE DIVIDEND FORCES THE BALANCE SHEET. A LOW-LEVEL POSSIBILITY.** $5.2bn of dividends
   against judged owner earnings of $5.2bn leaves nothing for the buyback, the acquisition or
   a downturn. Debt has gone **$0 (FY2008-09) to $14,048M** plus a $5bn facility. At $19bn of
   debt and a 5% coupon, interest is **~$950M, 16% of FY2025 operating profit**, against
   $543M today. Low-level because coverage is 4.8-9.5x and the maturities are long.
4. **SILICON LABS IS A $7.5BN WRITE-OFF. A LOW-LEVEL POSSIBILITY** — and the honest statement
   is that **I have not read Silicon Labs' filings**, so this is an exposure, not an
   assessment. It is 46% of TXN's equity, lands in the 11.3%-margin segment, and closes in
   H1 2027, outside every window in this file.
5. **Solvency: essentially unnameable.** [E2-55]'s extraordinarily-adverse-conditions test —
   revenue back to the FY2024 trough of $15.6bn with capex at the guided $2.5bn — still leaves
   roughly $6.3bn of operating cash flow against $1.7bn of contractual claims and $543M of
   interest. The business does not die of leverage. It dies, if it dies, of margin.

**[E4-51] — the bear case its holders would accept as fairly stated:** *TXN owns the best
analog franchise in the world, is the low-cost producer by 40% per chip, has just finished
building the capacity that will carry it for twenty years while every competitor starved
theirs, is about to drop capex from $4.55bn to $2.5bn, and will collect a 35% federal tax
credit on everything it places in service from here. The last three years' numbers are the
cost of that, not the result of it.* **That case is not refuted by anything in this file.
What this file says is that it is already in the price twice over.**

- **VERDICT: [x] IN** — GOOD, not great, and travelling. Owner earnings judged **$5,200M**;
  band **$4,512M to $6,124M** on the TTM, and **$1,427M to $6,135M** across all six windows.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, BEFORE THE RANKING [E4-28, E3-13].** *"that's the figure we quit on."*

**1. THE YIELD**
- owner earnings **$5,200M** ÷ market cap **$236,020M** = **2.20%** · sovereign **5.24%**
- band: **1.91% (strictest) to 2.59% (most generous constructible)**; across all six windows
  **0.60% to 2.60%**

**2. WHAT THE PRICE ALREADY ASSUMES**
- To be worth the price **at the bare bond**: **3.04% perpetual growth** (band 2.65-3.33%).
- To clear the **[E4-28] 10% floor**: **7.80% perpetual growth** (band 7.41-8.09%).
- **What the business has actually done, FY2016 to the TTM, 9.5 years:** revenue **+4.03%/yr**
  · operating profit **+4.32%/yr** · net income **+5.64%/yr** · **owner earnings at the capex
  end +2.72%/yr** · EPS ~+6.9%/yr, and **the EPS leg was buyback-driven and the buyback has
  stopped** (shares 919M in 2020, 913M today, with issuance exceeding repurchases in four of
  the last six periods).

**THE PRICE ASSUMES ROUGHLY 3% FOREVER JUST TO MATCH A TREASURY BOND, AND TXN HAS DELIVERED
2.7% ON OWNER EARNINGS OVER NINE AND A HALF YEARS. THE FLOOR NEEDS 7.8% FOREVER, WHICH TXN
HAS NOT ACHIEVED ON ANY MEASURE EXCEPT THE ONE IT NO LONGER HAS A LEVER FOR.** [E4-35]'s base
rate is the burden of proof here and it is not met in writing.

**3. WHAT YOU ARE PAID**
- **−3.04 points over the sovereign** at the judged number; **−3.33 to −2.65 points** across
  the band. **Negative on every construction.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** Sovereign used **5.24%,
the bare rate, no per-name premium.** Certainty is handled at the understanding gate (Q1 IN)
and in the end discount, once **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a DCF is run only as an engine and casts no
vote **[E3-34]**:

| construction | value | per share |
|---|---|---|
| zero growth at the **[E4-28] floor**, judged OE | $52,000M | **~$57** |
| zero growth at the floor, band | $45,120-61,240M | **$49-67** |
| zero growth at the **sovereign**, judged OE | $99,237M | **~$109** |
| engine: 4%/10yr then 2.5%, discounted at the floor | $79,252M | **~$87** |
| engine: 7%/10yr then 3%, discounted at the floor | $102,835M | **~$113** |
| engine: **10%/10yr then 3%**, discounted at the floor, on the **most generous OE** | $151,350M | **~$166** |
| *(memo)* engine: 4%/10yr then 2.5%, discounted at the **sovereign** | $221,530M | *$243* |

- **conservative ~$57 · optimistic ~$166 · centre ~$110 · current price $258.44**
- **Price is 2.3x the centre and 1.56x the single most generous engine output.** To reach
  today's price the engine has to be discounted at the **bond** rather than at the floor,
  which is the one thing [E4-28] forbids: *"that's true whether short rates are 6 percent or
  whether short rates are 1 percent."*
- Cross-checks: **P/E 47.4x on FY2025, 39.0x on the TTM; price/book 14.5x; price/tangible
  book 19.8x; dividend yield 2.13%** — the last of which is, notably, **below the yield on
  the owner earnings themselves and 3.1 points below the bond.**

**HONEST PRE-TAX EXPECTANCY AT THIS PRICE: ~6.5% (range 5.5% to 8.0%)** — a 2.20% starting
yield plus the 4.0-4.5% the business has actually compounded at, with the upper end allowing
the fabs to load faster than the record suggests. **[E2-63] — state what bounds the upside:
the ceiling here is that owner earnings cannot exceed operating cash flow, TXN's guided capex
floor of ~$2.5bn is already assumed, the CHIPS receipts run out with the build, and the
per-share lever is idle.**

**WHICH BAR** — [x] **Screamer test [E4-01]**, and no margin is added on top.
**Outcome three: the price is above the whole range.** **Windage count: 1** — conservatism
is spent once, at the (c) judgment, and it was spent **AGAINST** the conclusion (I judged (c)
at $2,600M rather than at the $3,312M TTM capex, which *raises* owner earnings by $712M and
*helps* the name). No second windage anywhere.

**THE FLOOR VERDICT, FIRST [E4-28]:** honest pre-tax expectancy **~6.5% against ~10%.**
**BELOW THE FLOOR — SO TXN IS NOT RANKED. IT IS QUIT ON.** The lines about points over the
sovereign and position in the opportunity set are therefore not filled in, per the template.

- **VERDICT: FAIL AT Q5, ON PRICE. Ranking position: not ranked — quit on at the [E4-28]
  floor.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]. No position is taken, so these are re-look triggers.**

- **Thesis-CONFIRMING metric, pre-registered so it cannot be rationalised away later:**
  **capex holding at or below $3bn for two consecutive years WHILE gross margin returns above
  62%.** That is the flow-through [E3-62] question answered in TXN's favour, and it would mean
  the 40% cost advantage is finally sticking to the owners' ribs. **Second confirmer:** the
  incremental pre-tax return on the FY2021-25 build rising through **12%** [E5-40] — i.e.
  operating profit above roughly **$8.3bn** on the current asset base.
- **Thesis-BREAKING metrics and thresholds:** capex guided back above **$4bn** for any year
  ("dependent on revenue and growth expectations" is the filed escape hatch, and it resets
  every window) · gross margin below **56%** for two consecutive quarters · Analog segment
  operating margin below **35%** · Embedded Processing still under **20%** at the end of 2027,
  six years after Lehi · China-headquartered revenue falling two years running · any
  suspension or non-increase of the dividend, which would confirm the [E2-60] reading · a
  further **[E2-49]** withdrawal, and **if the Analog/Embedded segment split itself were
  consolidated, this file reopens at Q2, not at Q5.**
- **The sell rule [E2-28]** — not applicable, no position. Recorded for completeness: the
  first trigger (market judging the business more valuable than the facts indicate) is the
  reason this file closes; the three hold conditions are Q2 (satisfactory, narrowing), Q3
  (competent, no disqualifier) and Q5 (overvalued — fails).
- **[E4-17]/[E3-30] the monitoring question:** is the margin erosion an aberrational cycle or
  a permanent slip? **The honest answer from the filings is that it is BOTH and they cannot
  be separated yet** — roughly half the 11.8-point gross-margin fall is depreciation TXN
  chose to incur and will absorb if revenue grows, and the other half is underutilisation and
  mix whose price component is unobservable because no price is filed **[E4-55]**.
- **PRE-COMMITTED RE-LOOK PRICE: ~$110/share judged at a 5.24% sovereign, recomputed at the
  rate of the day. RE-OPEN BELOW ~$130 (a ~50% decline).** The file is, however, far likelier
  to reopen on earnings than on price: **a full ramp at $2.5bn of capex on $25bn of revenue at
  60% gross margin would put owner earnings near $8bn and the yield near 3.4%** — still short
  of the floor at today's price, which is why the price trigger is where it is.
- **Next catalyst dates:** Q3 2026 results (~late October 2026) testing whether capex stays
  inside the $2-3bn guide · the FY2026 10-K (~early February 2027), the first vintage in which
  the post-build capex rate can be checked against the guide · the **Silicon Labs close in
  H1 2027**, which resets every owner-earnings window · the **September 2026 dividend
  announcement**, the 23rd-year test · and the first full year of the **35% ITC** on assets
  placed in service after 2025-12-31.
- **Position size:** zero. Not ranked, so nothing to size.

- **VERDICT: [x] IN** — the metrics are pre-committed and the re-look conditions are written
  before, not after, the price is known.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN · Q2 IN · Q3 IN · Q4 IN · Q5 FAIL.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Where evidence
      was missing it is marked UNKNOWABLE inside the question and named as such (the ASP /
      unit series at Q2; the segment capital attribution at Q3).
- [x] Every UNKNOWABLE states what specifically cannot be known: TXN's average selling prices
      and unit volumes (no filed document anywhere discloses them); the segment split of
      capital, assets and depreciation (TXN states it does not identify them).
- [x] Step 0: the filing was read — FY2025 10-K accession `0000097476-26-000059` and Q2 FY2026
      10-Q accession `0000097476-26-000152`, both downloaded and flattened; MD&A, cash-flow
      statement including its supplemental lines, and footnotes. **The figure cross-check
      reconciles TXN's own filed free cash flow of $2,938M to my owner-earnings construction
      by two identified adjustments.**
- [x] Owner earnings on a multi-year mean; six windows stated; the capex band disclosed as a
      judgment with the evidence on both sides and the decision made rather than defaulted.
- [x] Competitor row filled — eight peers, six on the SEC rung, two labelled IR rung.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 2026-09-04.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (screamer test), not both; windage count 1, stated, and spent against
      the conclusion.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git after every question.

## REGISTER
- **Verdict: [x] IN through Q4; Q5 FAIL ON PRICE at the [E4-28] floor.**
- **One line:** the best analog business in an eight-name row, mid-way through a $19.7bn
  capacity build whose returns are not yet visible, priced at 47x earnings and 14.5x book for
  a 2.20% owner-earnings yield against a 5.24% bond.
- **PRICE: $258.44 (2026-09-04). VALUE: ~$57 to ~$166, centre ~$110.**
- **PASS/FAIL: FAIL. The file closed at Q5, on price. Q1-Q4 all returned IN.**
