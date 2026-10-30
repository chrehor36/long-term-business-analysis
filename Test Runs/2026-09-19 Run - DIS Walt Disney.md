# Company Run — The Walt Disney Company (DIS) — 2026-09-19
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

**Entity, confirmed by me, not taken from the brief.** `tools/sources.py:cik_for('DIS')` returns
**`('0001744489', 'Walt Disney Co')`**. The submissions file for that CIK carries
`formerNames: [{'name': 'TWDC Holdco 613 Corp', 'from': 2018-06-25, 'to': 2018-06-28}]` — the
shell incorporated to become the new parent at the TFCF (Twenty-First Century Fox) closing on
2019-03-20. The old registrant, CIK 0001001039, is now **TWDC Enterprises 18 Corp ("Legacy
Disney")** and survives only as a co-obligor on pre-2019 notes (FY2026 Q3 10-Q, guarantor note:
*"On March 20, 2019 as part of the acquisition of TFCF, The Walt Disney Company ('TWDC') became
the ultimate parent of TWDC Enterprises 18 Corp (formerly known as The Walt Disney Company)"*).
**The brief's CIK is right and it is the right one to use: every 10-K since FY2019 is filed under
0001744489.** SIC 7990, fiscal year ends the Saturday nearest 30 September (`fiscalYearEnd 1003`).

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a
forecast **[E4-15, E3-32]**:
- rate **5.34** % · date **2026-09-18** · source (issuing authority) **US Treasury daily par yield
  curve, 30 Yr column** (`home.treasury.gov` .../daily-treasury-rates.csv/2026/all), struck fresh
  for this run on 2026-09-19. **Not FRED**, which is the labelled fallback only.
- FX: **none needed.** USD is both the quote currency and the reporting currency. Roughly a
  quarter of revenue is earned abroad (Linear international $1,055M, ESPN international $1,548M,
  international Parks & Experiences $6,520M, plus international DTC, of $94,425M), but the filer
  reports in USD and the earnings currency is USD.

**Price and count — the aggregator is flagged, the count is off the cover.**
- price **$102.67**, close **2026-09-18**, source Yahoo chart via `tools/sources.py:price` —
  **AGGREGATOR, live quote only, flagged as operator rule 5 requires.**
- shares **1,726,686,902**, from the cover of the **FY2026 Q3 10-Q**: *"There were 1,726,686,902
  shares of common stock outstanding as of July 29, 2026."* (accession **0001744489-26-000057**,
  filed 2026-08-05, period 2026-06-27).
- `split_factor_after('DIS','2026-07-29')` = **1.0** — no split between the count date and the
  price date, so the cap is the plain product.
- **market cap = $177.3bn** (1,726,686,902 × $102.67 = $177,278,944,228).
- *The count has fallen hard: the FY2025 10-K cover said 1,785,288,846 as of 2025-11-05.
  **58.6M shares, 3.3% of the company, retired in three quarters** — $7,245M of repurchases in
  the nine months to 2026-06-27 against $2,496M in the comparable prior period. That is a Q3
  fact and is read there.*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **FY2025 10-K**, period ended **2025-09-27**, filed **2025-11-13**, accession
    **0001744489-25-000155** (primary document `dis-20250927.htm`). The governing document.
  - **FY2026 Q3 10-Q**, period ended **2026-06-27**, filed **2026-08-05**, accession
    **0001744489-26-000057**.
  - **FY2023 10-K** (accession 0001744489-23-000216) and **FY2021 10-K** (accession
    0001744489-21-000220) for the FY2019–FY2022 windows.
  - Text of all four is on disk in `Test Runs/_research 2026-09-19 DIS/`.
- **figure cross-checked against the filed statement:** the cash-flow line *"Depreciation and
  amortization | 5,326"* (FY2025, Consolidated Statements of Cash Flows) reconciles exactly to
  the MD&A's two component tables — total depreciation expense **$3,859M** (Entertainment 773 +
  Sports 48 + Experiences 2,715 + Corporate 323) plus amortization of intangible assets
  **$1,467M** (Entertainment 52 + Experiences 108 + TFCF and Hulu 1,307) = **$5,326M**. The XBRL
  value for `DepreciationDepletionAndAmortization` FY2025 is the same 5,326, so the tagged data
  and the face agree. **And the cross-check found the thing that matters most at Q4: this D&A
  line EXCLUDES content amortization of $23,286M**, which the filer runs through *"Net change in
  produced and licensed content costs and advances"* — i.e. content spending is already inside
  operating cash flow, and (c) must not double-count it.
- Also checked: OCF **18,101**, capex **8,024**, equity-based compensation **1,363** — all three
  read identically off the face of the FY2025 cash-flow statement and out of companyfacts.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Answered per reported segment, on the SONY (2026-09-13) and GHC (2026-09-02) precedent: the
understanding verdict is about the money-making, not its durability, which is Q2 and Q4.** The
segments are the ones the filings now report — **Entertainment, Sports, Experiences** — restated
in FY2024 and carried in the FY2025 10-K segment note (Note 17) and MD&A.

### The filed frame — FY2023 to FY2025, segment note, $ millions

| | revenue FY23 · 24 · 25 | segment OI FY23 · 24 · 25 | FY25 OI margin | FY25 share of segment OI |
|---|---|---|---|---|
| **Entertainment** | 40,635 · 41,186 · 42,466 | 1,444 · 3,923 · **4,674** | 11.0% | 26.6% |
| — Linear Networks | 9,364 (FY25) | 3,452 (FY24) → **2,955** | 31.6% | 16.8% |
| — Direct-to-Consumer | 24,614 (FY25) | 143 (FY24) → **1,327** | **5.4%** | 7.6% |
| — Content Sales/Licensing | 8,488 (FY25) | 328 (FY24) → **392** | 4.6% | 2.2% |
| **Sports** | 17,111 · 17,619 · 17,672 | 2,465 · 2,406 · **2,882** | 16.3% | 16.4% |
| — ESPN domestic | 16,085 (FY25) | 3,056 (FY24) → **2,801** | 17.4% | 16.0% |
| **Experiences** | 32,549 · 34,151 · 36,156 | 8,954 · 9,272 · **9,995** | 27.6% | **56.9%** |
| — Parks & Experiences domestic | 25,191 (FY25) | 5,878 → **6,375** | 25.3% | 36.3% |
| — Parks & Experiences int'l | 6,520 (FY25) | 1,354 → **1,442** | 22.1% | 8.2% |
| — Consumer Products | 4,445 (FY25) | 2,040 → **2,178** | **49.0%** | 12.4% |
| Eliminations | (1,397) · (1,595) · (1,869) | | | |
| **Total** | 88,898 · 91,361 · **94,425** | 12,863 · 15,601 · **17,551** | 18.6% | 100% |

Below that line, and it is large: corporate and unallocated shared expenses **(1,646)**,
restructuring and impairment **(819)**, equity in the loss of the India joint venture **(202)**,
interest expense net **(1,305)**, TFCF and Hulu acquisition amortization **(1,576)** — leaving
income before income taxes **$12,003M** on $17,551M of segment operating income. **Roughly 32%
of segment operating income never reaches pre-tax income.**

### Unit economics, in my own words, no management language

Disney is **four different collection mechanisms bolted to one library of characters**, and they
are not equally good:

1. **Sell admission to a place built around the characters (Experiences, 57% of segment profit
   on 38% of revenue).** Disney owns land, buildings, ships and hotels at six resorts and sells a
   day's entry, a room, a meal and a souvenir. The customer pays for proximity to characters he
   already loves; the plant is the only way to deliver it, and there are six of them on earth.
   **Per-capita spending is the lever, not attendance:** FY2025 theme-park admission revenue rose
   5%, *"due to an increase of 4% from higher average per capita ticket revenue"* — while
   **domestic attendance fell 1%** and international rose 1% (key-metrics table). Hotel occupancy
   87% domestic on 10,236 thousand available room-nights, up 43 thousand on the year: physical
   capacity barely moved.
2. **Charge a royalty for someone else manufacturing character goods (Consumer Products, inside
   Experiences).** $4,445M of revenue at a **49% operating margin** — the best margin in the
   company and the least capital in it. This is the purest expression of what Disney owns.
3. **Charge a monthly fee for a library (DTC, $24,614M).** Disney spends cash making and buying
   content, puts it behind a paywall, and collects $7.81 a month per Disney+ subscriber and
   $12.36 per Hulu SVOD-only subscriber. In FY2025 this earned **$1,327M on $24,614M — 5.4%** —
   after $143M in FY2024 and losses before that. **Programming and production cost $14,257M of
   the $18,263M of operating expense**, so the margin is the thin residue of a very large
   content bill.
4. **Charge a per-subscriber fee to a distributor whose subscriber count is falling (Linear
   Networks $9,364M; ESPN affiliate and subscription fees $11,944M).** The pay-TV bundle pays
   Disney a fee per home. This is the most profitable revenue in the filing — Linear Networks
   earned **31.6%** — and its unit count is disappearing in public: domestic Linear affiliate
   revenue *"a decline of 9% from fewer subscribers, partially offset by an increase of 7% from
   higher effective rates"*; domestic ESPN *"an increase of 7% from higher effective rates was
   offset by a decrease of 7% from fewer subscribers."* **Price is being raised exactly fast
   enough to stand still, which is the [E4-55] shape: a shrinking unit series hidden by
   pricing.** Disney has two sources of this money and both sit on that curve.
5. **Sell the content itself to third parties and to cinemas (Content Sales/Licensing, $8,488M
   at 4.6%).** The theatrical slate is a per-title gamble; the filing lists FY2025's titles by
   name and the swing in operating income is driven by *"lower film cost impairments."*

### The scarce input this business controls
**The characters and the trademarks**, plus the six pieces of built land they are installed on.
Mickey, Marvel, Star Wars, Pixar, the Disney Princesses — legal monopolies of long but finite
life, and their value shows up where the least capital touches them (Consumer Products at 49%,
Experiences at 27.6%). **What Disney does NOT control is the third and fourth mechanisms' inputs.**
Streaming distribution is available to anyone. ESPN's input — live sports rights — is **rented,
not owned**: Sports programming and production cost $12,492M against $17,672M of revenue, 71% of
it, on contracts that expire and are re-auctioned; the FY2025 increase is *"expanded college
football programming rights and contractual rate increases."* And the pay-TV distributor's
customer relationship is not Disney's either.

### Will the fundamentals look broadly the same in ten years?
**Split, and I will state the split rather than average it:**
- **Experiences (57% of segment profit): yes.** Admission to a themed resort and a royalty on
  character merchandise have worked the same way since 1955 and the 1930s respectively.
- **Linear Networks and ESPN's affiliate fee (about 30% of segment profit between them): no, and
  the filing says so in units.** The subscriber base that pays these fees shrinks 7–9% a year
  and price rises are offsetting it almost exactly. ESPN launched its own DTC service in August
  2025 — the filer's own answer to the same fact.
- **DTC: the mechanism yes, the economics unproven.** A subscription to a library is a
  comprehensible business. Whether Disney's version earns a return on the $22.7bn a year it
  spends on content is a Q2/Q4 question, and FY2025's 5.4% margin is its first serious answer.

### Disconfirming evidence, hunted before the verdict **[E4-26]**
[E3-31] asks for businesses *"relatively simple and stable in character"* and warns off anything
*"subject to constant change"*; **[E4-46]** puts outside the circle a business that would need
months of study. The honest case against Q1 IN: Disney's video half has had its distribution
rebuilt twice in fifteen years; $82.6bn of its $197.5bn balance sheet is goodwill and acquired
intangibles from purchases whose returns are no longer separately reported; and 32% of segment
operating income vanishes before pre-tax income into corporate, restructuring, interest and
acquisition amortization. **The answer that survives it:** every one of those figures came off
the face of one filing in an afternoon, each collection mechanism is one paragraph, and the filer
publishes revenue drivers, operating income and physical unit metrics per line. **Q1 tests whether
I can say who pays, for what, and how much. I can.** Stability is not assumed here; it is named
above, unaveraged, so Q2 and Q4 must answer it.

- **VERDICT: [x] IN** — the money-making is understandable line by line from the FY2025 10-K.
  Durability, relative position and the capital each leg consumes are judged at Q2 and Q4.
  *(No "unverified" or "provisional" caveat carried.)*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Answered leg by leg, and then decided by where the profit and the capital actually are** — the HAS
precedent (2026-09-03: Q2 IN because the profit was *overwhelmingly* the franchise leg and the rest
*"neither grows nor eats material capital"*), the GHC precedent (2026-09-02: the verdict must hold for
what the shareholder actually buys) and the SONY precedent (2026-09-13: Q2 OUT where the legs had to
re-win their positions). **The metric set is chosen by business type first [E5-37].** Peer rows are on
disk with every figure's accession: `_research 2026-09-19 DIS/peers_video.md` and
`_research 2026-09-19 DIS/peers_parks_sports.md`.

### First: where is the profit, and where is the capital?

Disney does not disclose segment assets — *"We do not present a measure of total assets for our
reportable segments as this information is not used by the CODM to allocate resources and assess
performance"* (FY2025 10-K, Note 17). So capital is assembled from the items the filing **does** attribute
by segment, and every allocation is labelled. Goodwill by segment is **filed** (Note 4). Net PP&E is
allocated by each segment's **filed** depreciation share — which is conservative *against* Experiences,
because attraction assets are longer-lived than broadcast and technology plant, so Experiences' true PP&E
share is higher than its depreciation share and its computed return below is if anything overstated.
Content assets are split 70/30 Entertainment/Sports, a judgment, stated. Computation:
`_research 2026-09-19 DIS/segcap.py`.

| FY2025, $M | goodwill (filed) | content (allocated) | net PP&E (allocated) | capital | segment OI (filed) | **pre-tax return** |
|---|---|---|---|---|---|---|
| **Entertainment** | 51,258 | 21,929 | 8,264 | 81,451 | 4,674 | **5.7%** |
| **Sports** | 16,486 | 9,398 | 513 | 26,397 | 2,882 | **10.9%** |
| **Experiences** | 5,550 | 0 | 29,025 | 34,575 | 9,995 | **28.9%** |
| Total | 73,294 | 31,327 | 37,802 | 142,423 | 17,551 | 12.3% |

**Entertainment and Sports together: 43.1% of segment operating income on 75.7% of the capital, earning
7.0% pre-tax. Experiences: 56.9% of segment operating income on 24.3% of the capital, earning 28.9%
pre-tax.** This is **[E3-46]**'s question — *"the best businesses, by definition, are going to be
businesses that earn very high returns on capital employed over time"* — asked about the business before
the manager, and answered two different ways inside one security. It is also **[E2-56]**'s Pro-Am effect
set out in numbers: *"Their marvelous core businesses … camouflage repeated failures in capital allocation
elsewhere."* The blended 12.3% is the camouflage; judge the retention segment by segment.

And the direction of the spending is the opposite of the direction of the returns: **Experiences took 80.1%
of FY2025 capex** ($6,429M of $8,024M) — which is the right direction — while the $82.6bn of goodwill and
acquired intangibles that already sit on the balance sheet are 92% in the two legs earning 7.0%.

### The three [E3-03] criteria, leg by leg

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its customers to
> have **no close substitute** and; (3) is not subject to price regulation." — **[E3-03]**

**1. EXPERIENCES — Parks, Cruise Line, Consumer Products (56.9% of segment OI). PASSES all three.**
- (1) desired: yes. (2) **no close substitute: yes, and the competitor row proves it rather than asserts
  it.** (3) not price-regulated: yes.
- **[E2-44]'s two-characteristic test, which is the one that discriminates here.** Characteristic 1 — can
  it raise prices *"even when product demand is flat and capacity is not fully utilized"*? FY2025:
  **domestic attendance −1%, domestic per-capita guest spending +5%**, hotel occupancy 87% on available
  room-nights up 43 thousand of 10,236 thousand (FY2025 10-K key-metrics table). Volume flat to down,
  price up, and the segment's operating margin *held* at 27.6%. That is the test passed in the exact
  configuration [E2-44] specifies. Characteristic 2 — grow dollar volume *"with only minor additional
  investment of capital"*? **FAILS for the parks** ($6,429M of capex against $9,995M of segment operating
  income) and **passes outright for Consumer Products**, which earned **$2,178M on $4,445M of revenue —
  a 49.0% operating margin** — and is the leg where the least capital touches the trademark.
- **[E4-55], the physical series, read honestly.** Attendance −1% domestic while dollar revenue rose is
  precisely the Precision Steel shape the corpus warns about — *"Dollar revenue flattered by pricing is
  how a shrinking franchise hides."* **The reason it is not that here is the peer row**: every peer's
  physical series fell *further* in the same year while its price per guest fell too, which is what
  distinguishes a franchise raising price into flat demand from a business losing customers.
- **[E4-37]'s inverse metric** — *"the agony they go through in determining whether a price increase can be
  sustained."* Three consecutive years of per-capita increases (+3% FY2024, +5% FY2025, +3% rate in 9M
  FY2026 against 6% volume), disclosed as a matter of routine in a key-metrics table, with no hedging
  language anywhere in the MD&A. **This is yawn-pricing, not prayer-session pricing.**
- **[E4-32] direction: WIDENING.** Experiences segment operating income $8,954M → $9,272M → $9,995M
  (FY2023–25), and **+10% to $8,941M in the nine months to 2026-06-27** while every listed peer's
  operating income fell.

**THE COMPETITOR ROW — THEME PARKS. [E3-28].** Four operators; the industry's listed universe in North
America is essentially these four, and the two largest non-US comparables (Oriental Land, which licenses
Tokyo Disney Resort, and Merlin) are not SEC registrants — recorded as an evidence-ladder gap, rung
"exchange filings (TDnet)", not pulled. **The label break is stated: Disney and United Parks file segment
OPERATING INCOME; Comcast and Six Flags file ADJUSTED EBITDA, which is not operating income and which the
[E4-29] doctrine refuses as a profit measure. So the row is given BOTH ways.**

| latest FY | revenue | profit, as the filer measures it | margin | attendance | per-capita | source |
|---|---|---|---|---|---|---|
| **DIS Experiences** FY2025 | **36,156** | **OI 9,995** · EBITDA 12,818 | **27.6%** · 35.5% | **−1% dom, +1% int'l** | **+5% dom, +2% int'l** | 10-K 0001744489-25-000155 |
| CMCSA Theme Parks FY2025 | 9,836 | Adj EBITDA 3,080 | — · 31.3% | not disclosed | not disclosed | 10-K 0001628280-26-004994 |
| CMCSA Theme Parks FY2023 | 8,947 | Adj EBITDA 3,345 | — · 37.4% | not disclosed | not disclosed | same |
| FUN Six Flags FY2025 | 3,100 | **OI (1,375)** · Adj EBITDA 792 | **(44.4)%** · 25.5% | 47.4M (−2.1M like-for-like) | $61.90 (+1.0%) | 10-K 0001999001-26-000048 |
| PRKS United Parks FY2025 | 1,663 | **OI 365** | **22.0%** | 21.17M (−1.8%) | $78.54 (−1.9%); admission per cap **−4.3%** | 10-K 0001193125-26-088288 |

*Disney's EBITDA figure is my arithmetic (segment OI $9,995M + segment depreciation and amortization
$2,823M), added only so the Comcast and Six Flags measures have something of the same construction to sit
beside; it is labelled and it casts no vote.*

**What the row shows, and it is not close.**
- **Comcast opened Epic Universe in Orlando in May 2025 — a whole new theme park aimed directly at Walt
  Disney World — and its Theme Parks Adjusted EBITDA is still $265M BELOW its FY2023 figure** ($3,080M vs
  $3,345M), with margin down 6.1 points to 31.3% on revenue up 10%. Disney's Experiences operating income
  rose 12% over the same two years with its margin unchanged. **[E2-45]'s attacker's test — *"how I would
  like, assuming I had ample capital and skilled personnel, to compete with it"* — has been run as a live
  experiment by a $124bn-revenue competitor with ample capital, and the filed answer is that the attacker's
  own segment economics deteriorated.** Comcast discloses no cost figure for Epic Universe and no
  attendance at all (searched; recorded as not disclosed).
- **Six Flags wrote off $1,518M of goodwill and trade names in the third quarter of FY2025**, on eight
  reporting units, because *"revenue and earnings not meeting expectations"* — and its like-for-like
  attendance fell 2.1 million visits.
- **United Parks' admission per capita fell 4.3%** and attendance 1.8%; its operating income fell 21%.
- So in the same twelve months: Disney raised price 5% with volume flat and held its margin; the three
  listed competitors all saw price or volume or both fall, and two of the three took impairments or a
  margin collapse. **[E2-53]'s dominance class is the right reading — *"Once dominant, the newspaper
  itself, not the marketplace, determines just how good or how bad the paper will be"*.**
- **Untapped pricing power [E3-33]:** *not* claimed. [E5-28] scopes the class to *"a monopoly or a near
  monopoly"*, and Disney is visibly *using* its pricing power rather than sitting on it — three straight
  years of per-capita increases. The one place a claim could be made is Consumer Products at a 49% margin,
  and no filed evidence supports an untapped increment there.
- **Maintenance capex, and this row is the only place a filed anchor for Disney's (c) exists** — carried
  forward to Q4. United Parks files the split: *"(a) Reflects capital expenditures for park rides,
  attractions and maintenance activities"* **$182.4M** against *"(b) … park expansion, new properties, or
  other revenue and/or expense return on investment"* $35.1M, with depreciation of $168.0M — so a
  theme-park operator that discloses the split runs **maintenance capex at about 1.1× depreciation**
  (three-year means: core capex $195.4M ÷ depreciation $159.3M = **1.23×**). Six Flags states a hard
  floor: *"an expected required minimum annual maintenance and infrastructure capital expenditure of
  approximately $125 million to $150 million"* against 2026 total capex guidance of $400–425M and FY2025
  depreciation of $486M. **Neither peer's maintenance capex is a large multiple of depreciation.**

**EXPERIENCES VERDICT: WIDE franchise, direction WIDENING.** This leg would carry a Q2 IN on its own.

**2. SPORTS — ESPN (16.4% of segment OI, and falling). FAILS criterion 2, and fails [E4-04] outright.**
- (1) desired: yes — live sport is the last appointment viewing. (3) not price-regulated: **under attack
  rather than regulated** — three private antitrust actions consolidated in the Northern District of
  California allege Disney *"uses certain pricing and packaging provisions in its carriage agreements with
  vMVPDs to increase prices for and reduce output"*, and the Unger plaintiffs *"seek damages and injunctive
  relief, including an injunction requiring the Company to segregate or divest any interest in Fubo and
  Hulu, or in the alternative, business assets relating to Fubo and Hulu + Live TV"* (FY2025 10-K, Note 14).
- (2) **no close substitute: the filings say the opposite, twice, in public, with dates.** *"On October 30,
  2025, the Company's channels were removed from YouTube TV following the expiration of the parties'
  distribution contract without agreement on renewal terms, and the Company cannot predict how long this
  service blackout will last or reasonably estimate the adverse impact on our results of operations"*
  (FY2025 10-K risk factors). And in the latest quarter: *"in the third quarter of fiscal 2026, the NFL
  Network and NFL RedZone were removed from Comcast Xfinity and **service has not been reinstated**"*
  (FY2026 Q3 10-Q). The largest virtual distributor in the United States and the largest cable operator in
  the United States each took Disney's channels off rather than pay the asked rate. **A product with no
  close substitute does not get switched off by its distributor.** The earnings release names the cost:
  Sports operating income fell 17% in the quarter, *"modestly steeper than our prior guidance of
  approximately 14%"*, and among the causes was *"the impact of a network carriage dispute."*
- **[E4-04] is decisive, and this is the excluded class, not a defence-of-the-same-advantage case.** The
  framework's test: *"does a lapse in spending destroy the structure, or merely narrow it — and does the
  spending defend the same advantage, or buy its replacement?"* ESPN owns no sport. Its entire advantage
  **is** a portfolio of expiring licences — *"Rights include the National Football League (NFL), college
  football … the National Basketball Association (NBA), mixed martial arts (**through the end of calendar
  2025**), Major League Baseball, the National Hockey League, soccer, US Open Tennis, Formula 1 (**through
  the end of calendar 2025**), the Wimbledon Championships, the Masters … the WNBA and the PGA
  Championship"* (FY2025 10-K, Item 1). Two of those expired inside the filing's own sentence. Every
  renewal **buys the advantage again at auction**; that is Mitsui's Rhodes Ridge, not Coca-Cola's
  trademark. Programming and production cost **$12,492M against $17,672M of segment revenue — 71 cents of
  every revenue dollar paid to the owners of the thing customers actually want.**
- **The scale of the re-purchase is signed and filed: $84,076M of sports-programming rights commitments**
  (Note 14), $9,894M due in FY2026 and roughly $9.1–9.8bn a year through FY2030, $36,610M thereafter.
  **That is 29.2× the Sports segment's FY2025 operating income and 4.8× the whole company's segment
  operating income**, and the filer adds that *"Certain sports programming rights have payments that are
  variable based primarily on revenues and are not included in the table above."*
- **[E3-51], the surfing run, names what the record actually was.** ESPN's thirty-year record came from
  riding the pay-TV bundle: a fee collected from every home whether it watched or not. The wave is
  measurably over, in units, in Disney's own filing — domestic ESPN affiliate and subscription fees were
  flat because *"an increase of 7% from higher effective rates was offset by a decrease of 7% from fewer
  subscribers"* — and in the distributors' filings: **Comcast's domestic video customers fell 1.3 million
  to 11.3 million in FY2025 alone** (10-K 0001628280-26-004994), and WBD reports *"an 8% decline in
  domestic linear subscribers … Declines in linear subscribers are expected to continue"* (10-K
  0001437107-25-000031). *"When a surfer gets up and catches the wave … he can go a long, long time. But
  if he gets off the wave, he becomes mired in shallows."* **The advantage lived in the wave.**
- **And Disney has now sold 10% of ESPN to its largest rights counterparty.** *"On January 31, 2026, ESPN
  acquired NFL Network and certain other media assets owned and controlled by NFL Enterprises LLC,
  including the NFL RedZone channel's pay TV distribution and NFL Fantasy … in exchange for a 10%
  noncontrolling interest in ESPN (the NFL Transaction). Following the NFL Transaction, the Company has an
  effective 72% interest in ESPN and Hearst Corporation has an 18% interest"* (FY2026 Q3 8-K EX-99.1,
  accession 0001744489-26-000056). The counterparty that sets the price of ESPN's single largest input is
  now a shareholder in ESPN. That is read again at Q3 under **[E5-44]**.
- **[E4-32] direction: NARROWING, sharply.** Sports segment operating income $2,465M (FY2023) → $2,406M
  (FY2024) → $2,882M (FY2025, and the rise is *"due to the Star India Transaction"*, i.e. the removal of a
  loss-making business, not growth) → **−14% to $1,701M in the nine months to 2026-06-27**. Domestic ESPN
  operating income fell $3,056M → $2,801M in FY2025 while its revenue rose 5%.

**SPORTS VERDICT: NOT A FRANCHISE. Excluded by [E4-04]; criterion 2 refuted by two filed blackouts.**

**3. ENTERTAINMENT — Linear Networks, Direct-to-Consumer, Content Sales/Licensing (26.6% of segment OI).
FAILS criterion 2 in every sub-leg, for three different reasons.**

- **Linear Networks ($2,955M of OI, the highest-margin revenue in the company at 31.6%): a melting
  franchise, and the melt is the unit count.** Domestic affiliate revenue *"a decline of 9% from fewer
  subscribers, partially offset by an increase of 7% from higher effective rates"*; domestic advertising
  *"a decline of 8% from fewer impressions attributable to lower average viewership."* Goodwill of $1.3bn
  (FY2024) and $0.7bn (FY2023) has already been written off **on this reporting unit by name** — *"we
  recorded goodwill impairment charges of $1.3 billion and $0.7 billion … related to the entertainment
  linear networks reporting unit"* (FY2025 10-K, Note 18 cross-reference). A franchise whose auditor-tested
  fair value has fallen below carrying value twice in two years is not a franchise; it is a run-off.
- **Direct-to-Consumer ($1,327M of OI on $24,614M, a 5.4% margin in its first properly profitable year):
  [E3-03] criterion 2 is answered by the brief's own question — when the same household holds three
  services, none of them is the one with no close substitute.** The peer row settles it:

**THE COMPETITOR ROW — STREAMING AND STUDIOS. [E3-28].** Seven names; the industry's real competitor set
for a general-entertainment subscription service. **The label break is stated in every row.**

| latest FY | streaming/DTC revenue | profit, as the filer measures it | margin | subscribers | ARPU | content cash spend | source |
|---|---|---|---|---|---|---|---|
| **DIS DTC** FY2025 | **24,614** | **segment OI 1,327** | **5.4%** | Disney+ 131.6M · Hulu 64.1M (43.7M held in both) | Disney+ **$7.81, +11%** | company-wide **22,709** | 0001744489-25-000155 |
| **NFLX** FY2025 | 45,183 | **operating income 13,327** | **29.5%** | **no longer disclosed** | **no longer disclosed** | additions to content assets **17,097** | 0001065280-26-000034 |
| **WBD Streaming** FY2025 | 10,876 | **GAAP operating loss (264)** · Adj EBITDA 1,370 | **(2.4)%** · 12.6% | 131.6M, +13% | **$6.92, −11%** | content payments 11,401 | 0001437107-26-000020 |
| **CMCSA Peacock** FY2025 | 5,400 | **not filed**; revenue less costs **(1,100)** | **(20.4)%** | 44M (incl. unactivated bundles) | not disclosed | not separable | 0001628280-26-004994 |
| **SONY Pictures** FY3/26 | ¥1,499bn | OI margin **7.0%** | 7.0% | Crunchyroll 21M | n/a | film-cost additions ¥475.6bn | run file 2026-09-13, 20-F 0001193125-26-274893 |
| **AAPL** | Apple TV+ **not broken out** | not filed | — | not disclosed | — | not disclosed | 10-K 0000320193-25-000079 |
| **AMZN** | Prime Video **not broken out** | not filed | — | not disclosed | — | not disclosed | 10-K 0001018724-26-000004 |

- **Peers named: 7 of the industry's ~7 real competitors in general-entertainment video** (Netflix,
  Comcast/NBCUniversal, Warner Bros. Discovery, Paramount Skydance, Sony, Amazon, Apple). Buffett says
  eight; the eighth in video is YouTube, whose owner discloses no comparable segment. **Two of the seven
  (Apple, Amazon) do not file streaming-segment profitability at all.** Under the template's own rule that
  makes the **video moat class PROVISIONAL** — *and that is not a problem for this verdict, because the
  finding against the DTC leg does not rest on Apple's or Amazon's margins.* It rests on Disney's own
  filed 5.4%, on Netflix's filed 29.5%, and on what the filings say about substitution. The absence is
  recorded as required and its direction noted: a competitor who can fund a video service out of another
  business's profit and never has to show its margin is *worse* for the substitute question, not better.
- **[E2-44] characteristic 1 at Disney+ — and Disney passes it where its peers do not.** Domestic Disney+
  ARPU $6.34 (FY2022) → $6.97 (FY2023) → $7.89 (FY2024) → **$8.06 (FY2025)**, +27% over three years, with
  domestic subscribers 46.4M → 59.3M over the same span; total Disney+ ARPU +11% in FY2025 *"reflecting
  increases in pricing"* with subscribers +5%. **WBD did the opposite: subscribers +13%, global ARPU −11%,
  *"primarily attributable to broader wholesale distribution of HBO Max Basic with Ads"*.** Hulu SVOD-only
  ARPU, meanwhile, went $12.72 → $12.17 → $12.36 across FY2022–25: **flat in nominal terms for three
  years, and down in real terms.** So the price-raising power exists at Disney+ and does not exist at Hulu,
  which is the larger content bill of the two ($9,018M vs $5,239M of programming and production cost).
- **The subscriber count is not a unit series that can be trusted across the row.** Disney's own footnote:
  the Disney+ 131.6M and the Hulu 64.1M *"Includes 43.7 million and 27.1 million subscribers to bundles
  that have both Disney+ and Hulu"* — the same person counted twice, and the double-count grew 61% in one
  year. Comcast counts Peacock subscribers delivered through third-party bundles *"regardless of whether
  it is activated."* Netflix has **removed the series altogether**: *"During the year ended December 31,
  2025, we discontinued the reporting of membership numbers … focusing instead on revenue and operating
  margin."* **[E4-55] asks for the physical series; in streaming the industry has stopped filing an honest
  one.** That is a finding about the disclosure, and it is the reason the margin is the only comparable.
- **The structural answer to criterion 2 is that the field is consolidating around someone else.**
  Netflix agreed on 2025-12-04 to buy WBD's streaming and studios businesses for ~$72.0bn equity value;
  WBD's board then found a *"Company Superior Proposal"*, terminated the Netflix agreement on 2026-02-27,
  **paid Netflix a $2.8 billion termination fee, and agreed to be acquired whole by Paramount Skydance at
  $31.00 cash a share, with Larry J. Ellison personally guaranteeing $45.72 billion of the
  consideration** (WBD 10-K FY2025, accession 0001437107-26-000020). Comcast **completed** the separation
  of its cable networks into Versant on 2026-01-02. **Within fifteen months the two nearest rivals in
  general-entertainment video have been recapitalised or dismembered, one competitor has been outbid $72bn
  and paid $2.8bn to walk away, and the winner of the auction is a studio backed by a balance sheet larger
  than Disney's own.** A business whose product had no close substitute would not be in an industry where
  the assets change hands at these prices.
- **Content Sales/Licensing ($392M of OI on $8,488M — 4.6%): key-person and key-title dependent, which is
  a Q2 moat defect under [E4-23], not a Q3 note.** *"if a business requires a superstar to produce great
  results, the business itself cannot be deemed great."* The filer's own language: operating income moved
  on *"lower film cost impairments"*; the latest quarter reports *"While audience scores for both Star
  Wars: The Mandalorian and Grogu and fiscal Q4's live action Moana have been strong, **both films
  underperformed our box office expectations**"* and guides Entertainment down for *"the impact of Moana's
  box office performance coming in below our prior expectations"* (FY2026 Q3 EX-99.1). A leg whose
  quarterly result turns on two release outcomes is a slate, not a franchise. **It is a channel for the
  franchise — which is a different thing, and is the strongest counter-argument to this verdict; it is
  stated in full below.**

### [E3-61] — the row's limit, stated
*"In some businesses, the participants behave like a demented Kellogg. In other businesses, they don't …
**I think you'd have to know the people involved.**"* The parks row shows Disney's position; it cannot show
that Comcast will keep building at the Orlando margin it just earned, or that Paramount Skydance will price
HBO Max rationally once it owns it. The row is position, not conduct.

### [E4-36] — which cause of extreme success is this?
Experiences and Consumer Products are the **nonlinear combination**: a century of character investment,
installed in physical plant that cannot be copied, monetised simultaneously as admission, room, meal,
souvenir and third-party royalty — each of which raises the value of the others. That is ownable. Sports
was **wave-riding** on the pay-TV bundle. DTC is an **extreme-performance-over-many-factors** attempt in a
market with five equally-funded attempts. Only the first is ownable.

### THE HONEST CASE AGAINST THIS VERDICT — **[E4-51]**, stated better than the opposition would
*"I'm not entitled to have an opinion unless I can state the arguments against my position better than the
people who are in opposition."* The bull case is not that ESPN is a franchise. It is this:

> **Disney owns exactly one moat — the characters — and rents it out through four channels. Two of those
> channels (pay television, theatrical) are in secular decline and one (streaming) is in a price war, but
> the moat is not in the channels, it is in the IP, and the IP is demonstrably intact.** Toy Story 5 passed
> $1bn of global box office in FY2026 and took the franchise past $4bn lifetime; it *"further lifted the
> franchise on Disney+, which has over two billion hours streamed, while Toy Story merchandise helped
> deliver our strongest quarter of year-over-year growth in Consumer Products revenue in 20 quarters"*, and
> *"Toy Story has a presence at every park and on every cruise ship we operate."* **One film release moved
> four revenue lines at once. No competitor in the peer row can do that with any property it owns.** On
> that reading, the right answer is HAS (2026-09-03): the profit is overwhelmingly the franchise leg, and
> the non-franchise legs are the declining rent on an asset whose owner is now collecting it elsewhere.

**Why that argument does not carry Q2, and the reason is a number, not a preference.**
1. **The HAS test has two halves and this fails the second.** HAS passed because the non-franchise legs
   *"neither grow nor eat material capital."* Here they eat **75.7% of the capital** ($107.8bn of $142.4bn)
   and carry **$84.1bn of signed, non-cancellable forward commitments** — 4.8× the whole company's annual
   segment operating income, and 59% of the entire market capitalisation in commitments alone.
2. **ESPN is not a channel for the characters.** Mickey does not appear on Monday Night Football. Sports
   holds $16.5bn of goodwill and $84.1bn of commitments and has no connection to the IP at all; it is a
   separate, contract-dependent, capital-heavy business that happens to be inside the same registrant. The
   "one moat, four channels" reading requires ignoring the leg that carries the largest single obligation
   in the filing.
3. **The 2019 purchase is the other half of the answer.** The TFCF acquisition added roughly **$49.0bn of
   goodwill and $16.4bn of intangibles** (goodwill $31,269M → $80,293M and intangibles $6,812M → $23,215M
   between FY2018 and FY2019, companyfacts, cross-checked to the FY2025 balance sheet) and raised the
   weighted diluted share count from 1,507M to 1,831M at its peak. **$51.3bn of that goodwill sits in
   Entertainment, which earned 5.7% pre-tax on its capital in FY2025**, and $2.6bn of it has already been
   written off. The shareholder did not buy one moat and four channels; he bought one moat **plus** a
   $65bn library-and-networks purchase whose reporting unit has failed its impairment test twice.
4. **[E4-04] admits no averaging.** The criterion is about the moat's *basis*, and two of the three
   segments must periodically replace theirs. A franchise verdict for the whole security would be a
   franchise verdict for $84bn of expiring contracts.

### CLASS AND DIRECTION
- **Experiences / Consumer Products: WIDE, WIDENING.** Would pass Q2 alone.
- **Sports (ESPN): NONE.** [E4-04] excluded; criterion 2 refuted by two filed blackouts; NARROWING (−14%).
- **Entertainment — Linear: NONE, in run-off** (two goodwill impairments on the reporting unit).
  **DTC: NARROW at best and PROVISIONAL on the peer row** (two of seven peers file no segment
  profitability), at a 5.4% margin against Netflix's 29.5%. **Content Sales: NONE** — [E4-23] defect.
- **Class for the security the shareholder actually buys: NOT A FRANCHISE.** 43.1% of the profit and
  75.7% of the capital sit in businesses that fail [E3-03] criterion 2 and are excluded by [E4-04].

- **VERDICT: [x] OUT**
  *The evidence is here and the business, at this perimeter, fails the franchise test. This is a finding
  about the security, not about the parks: Disney's Experiences segment is the clearest single franchise
  found in any run on disk, and it is attached to $107.8bn of capital earning 7.0% and $84.1bn of signed
  sports-rights obligations. The reversal condition, in words and not as a price alert: **a filed
  separation, sale or spin of ESPN and the linear networks** — which is exactly what Comcast did on
  2026-01-02 and what WBD tried twice — **would leave a security that this framework would have to look
  at again from Q1.** No document resolves the question as it stands, so this is OUT, not UNRESEARCHED.*

### ADDENDUM TO Q2, added later the same day (2026-09-19) when the streaming peer row finished
*Left beside the row above rather than editing it, per operator rule 6. **Nothing below changes the Q2
verdict**; two items sharpen it and one runs against it, and the one that runs against it is stated first.*

1. **AGAINST this verdict — Paramount is the one filer in the set that dates a price rise and reports the
   subscriber response, and the response was good.** It raised domestic Paramount+ pricing in **June 2023**
   and thereafter reported **+10.0 million subscribers (+15%) and +12% subscription revenue**, with no
   offsetting cancellation figure disclosed. Taken with Disney's own Disney+ ARPU +27% over three years on a
   growing domestic base, **the honest reading is that general-entertainment streaming subscribers are less
   price-sensitive than the [E2-44] test's failure mode assumes.** That weakens the "no pricing power"
   version of the argument. **It does not weaken the argument actually made**, which is not about pricing
   power but about **[E3-03] criterion 2 — the absence of a close substitute — and about the 5.4% margin
   that the pricing power has so far produced.**
2. **The comparability finding, which is worse than the row above stated.** Only **ONE** peer files a
   streaming profit measure on the same basis as Disney's DTC segment operating income: **WBD Streaming, a
   GAAP operating LOSS of $(264)M on $10,876M**. Peacock has **no filed profit measure at all**; Paramount's
   is Adjusted OIBDA on a third exclusion list; **and no GAAP full year 2025 exists for Paramount at all** —
   pushdown accounting from the August 2025 Skydance transaction splits the year at 6/7 August and the filer
   supplies a pro forma for **revenue only**. Apple and Amazon file nothing. **So the correct count is that
   four of the seven peers file no comparable streaming profit figure, not two.** Under the template's rule
   the **video moat class is PROVISIONAL** and that is recorded; it is not load-bearing, because the finding
   rests on Disney's own filed 5.4% against Netflix's own filed 29.5%, both GAAP operating margins.
3. **Content spend is four incompatible constructions** and must never be summed across the row: Netflix
   *"additions to content assets"* $17,097M (cash); Disney produced-and-licensed content spend $22,709M
   (cash, **company-wide, not DTC**); WBD $11,401M (cash, **net of production payables**); Amazon ~$22.4bn
   (an **expense**, and it **includes music**). Recorded so no later reader treats the Q2 table's rightmost
   column as a like-for-like series.
4. **A registrant trap worth recording for the tooling**: `PARA` in the SEC's own `company_tickers.json`
   now resolves to **Banzai International, Inc. (CIK 0001826011)**, an unrelated filer. Paramount is the
   chain **Paramount Global CIK 0000813828 → Paramount Skydance Corp CIK 0002041610**. Any screen that
   resolves a peer by ticker will price the wrong company. Comcast's FY2025 10-K also filed under a filer
   agent's accession prefix (0001628280) rather than its own.

### SECOND ADDENDUM, added later the same day (2026-09-19) when the sports-rights peer row finished
*Again left beside the row rather than editing it (operator rule 6). **It contains one CORRECTION to Q3
below, which must be read there**, two facts that run against the Q2 verdict, and the distributor unit
series that Q4's death arithmetic rests on. Source file: `_research 2026-09-19 DIS/peers_parks_sports.md`,
Part B. **Nothing below changes the Q2 verdict.***

**CORRECTION TO Q3 — the NFL Transaction IS valued in a filing, and Q3 below says it is not.**
Q3's [E5-44] bullet states *"No valuation of either side is filed."* **That is wrong**, and is corrected
here rather than by editing it. The **FY2026 Q3 10-Q (accession 0001744489-26-000057)** discloses the
transaction at a fair value of approximately **$3 billion**, with amortisation of the acquired intangibles
beginning in **2033**, the NFL Network and RedZone **rights licensed to ESPN through 2033 with no amount
disclosed**, and an **Exchange Right exercisable after July 2034 at 70% of fair market value.** So:
**Disney gave a 10% interest in ESPN valued at about $3bn**, which implies ESPN at roughly **$30bn — about
10.4× its FY2025 segment operating income of $2,882M** — for three assets in the declining channel, one of
which (NFL Network) was removed from Comcast Xfinity in the same quarter and *"has not been reinstated."*
**The [E5-44] test can now be run rather than merely flagged: what was given is measurable, what was
received is not, because the rights licence back to ESPN through 2033 carries no disclosed price.** The
flag stands and is now quantified on one side only. *(The 70%-of-fair-market-value exchange right is
itself worth noting: the counterparty can put its stake back at a 30% discount to value, which is a
shareholder-favourable term.)*

**1. AGAINST this verdict — ESPN's affiliate rate increases are the best in the industry, by a wide
margin.** The like-for-like comparison, both from FY2025 filings: **ESPN domestic, +7% rate against −7%
subscribers**; **WBD Global Linear Networks, +3% domestic affiliate rates against a −9% domestic subscriber
decline**, producing distribution revenue **−8%**. ESPN holds its dollar line where WBD cannot.
**That is real evidence of relative bargaining power inside a dying channel**, and it is the strongest
single fact against the [E3-03] criterion-2 finding on the Sports leg. It does not overturn it: the two
blackouts happened *to Disney*, not to WBD, precisely because Disney asks for more.

**2. AGAINST this verdict — not all linear networks are shrinking, and the one that is growing is a
competitor's.** **Fox Corporation's Cable Network Programming segment grew: revenue $5,955M → $6,930M →
$7,348M and Segment EBITDA $2,693M → $3,030M → $3,099M across FY2024–26** (peer file, Part B). So the
linear decline is not a law of the medium; Disney's linear portfolio is declining and Fox's is not. Recorded
in full, because it means the Linear Networks finding above is about **Disney's channels**, not about cable.

**3. FOR this verdict — the whole industry is contracted, at Disney's scale or larger, which is what makes
[E4-04]'s exclusion a class judgment rather than a company judgment.** Disney's sports programming
commitments **$84,076M** of a $104,088M total; **Comcast's programming obligation $93.8bn**, the
*"substantial majority"* sports, unsplit; **Fox's licensed-programming commitment $24,365M**. Comcast's NBA
rights run *"from the 2025-26 season to 2035-36"*, six Conference Finals series, price not disclosed.
**Nobody in this industry owns the sport; everybody has signed for a decade of it.**

**4. FOR this verdict — a filed instance of a sports-rights contract losing money outright.** WBD recorded
**$73M in 2025** under its loss-cap where NCAA rights plus production costs exceeded advertising and
sponsorship revenue. That is [E4-04]'s excluded class producing its characteristic outcome in a competitor's
audited statements.

**5. FOR this verdict — the unit series Q4's death arithmetic needs, from three distributors' own
filings.** Pay-TV subscribers, in millions: **Comcast domestic video 18.176 (2021) → 11.270 (2025), −38.0%**;
**Charter 14.122 → 12.892 → 12.605**; **EchoStar Pay-TV 8.526 → 7.778 → 6.998.** The three-distributor sum
fell 36.754 → 30.873 (my arithmetic, and explicitly **not** a market total; YouTube TV is not disclosed by
Alphabet). **And EchoStar's own FY2025 10-K names Disney's new service as a cause of its subscriber loss:**
*"in August 2025, ESPN Unlimited and FOX One sports packages were launched."* **Disney's DTC service is
taking subscribers from the distributors that pay Disney's affiliate fee** — which is the mechanism, in a
counterparty's audited filing, and it is the sharpest corroboration of shape #10 in the file.

**6. A perimeter fact recorded for any future run: Fubo has no calendar-2025 10-K.** It changed its fiscal
year end to 30 September on the Disney closing; **Disney holds 70% economic and 70% voting and appoints a
board majority**, so Fubo's subscriber count is not an independent count of the market — it is Disney's own.

**7. The international parks note, for completeness of the Q2 parks row.** Disney files an International
Theme Parks note: revenues **$6,111M**, costs **$(4,963)M**, Asia parks' net PP&E **$6,060M**, and
**royalty and management fees of $323M eliminated in consolidation.** **Oriental Land Co (the Tokyo Disney
Resort licensee) is recorded as an UNRESEARCHED evidence-ladder gap**, rung named: EDINET Annual Securities
Report / TDnet Kessan Tanshin, TSE code 4661; no 20-F exists and none was pulled. It is a licensee, not a
competitor, so it does not gate the moat class. The dollar Tokyo Disney royalty is not separately filed.

**8. The peer search method is on disk so it can be re-run**: EDGAR full-text search, nine phrase queries,
forms=10-K, 2025-01-01 → 2026-09-19. Besides DIS, CMCSA, FUN and PRKS the only other US-listed gated-park
operator disclosing attendance is **Parks! America (PRKA)**, revenue $10.47M, percentage change only.
**TEA/AECOM was deliberately not used** — it is an aggregator and United Parks' own 10-K says *"attendance
rankings … are not independently validated by the Company."*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> ⚠️ **RECORDED, NOT GOVERNING. Q2 is OUT and the file is closed there.** Everything below was done
> because the brief asked for the whole surface and because the findings are worth having on disk for
> any future look at this name; **none of it promotes anything, and under the guardrail it could not
> even if it were glowing [E2-37, E2-38, E3-39].** Every ledger id below was checked against
> `principle_ledger.csv` before citing (176 ids checked, 0 missing — see the defect note at the end).

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
- [x] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38, E3-43]**
- [ ] **Control** — whole business, no exit **[E1-16]** *(a minority public stake; exit is a market order)*
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]** *(borrowings $42,026M against total
      equity $114,612M = 0.37×; net borrowings $36,331M = 2.07× segment operating income; segment
      operating income covers net interest 13.4×. Not the twenty-to-one case.)*

**Case declared: Q3 is a BINARY GATE, not an overlay, and the reason is segment-specific.** The parks are
a have-to-be-smart-once business — **[E2-53]**'s dominance class, where *"the newspaper itself, not the
marketplace, determines just how good or how bad the paper will be"*. But the legs that hold 75.7% of the
capital are not: a film slate must be re-created every year, $84.1bn of sports rights must be re-bought at
auction, and carriage must be re-negotiated with counterparties who have twice this year switched the
channels off. **[E3-43]**'s distinction is exactly this: *"franchises can tolerate mis-management … a
business, unlike a franchise, can be killed by poor management."* Disney is both, and the part that is
"a business" carries the capital. So the gate applies, and **no price compensates [E1-16, E3-29, E5-35]**.

### Honesty — binary, permanent, filings-based **[E5-16]**
*"We are understanding about business mistakes; our tolerance for personal misconduct is zero."* Each
matter dated to when it became **public**, so the test stays point-in-time honest.

- **2023-05-12 — a securities class action about the Disney+ accounting itself**, in the Central District
  of California against the Company, former CEO Robert Chapek, former CFO Christine McCarthy and former
  DMED chairman Kareem Daniel; **Robert Iger added by the consolidated complaint of 2023-11-06.**
  *"Plaintiffs … allege purported misstatements and omissions concerning, and a scheme to conceal, accurate
  costs and subscriber growth of the Disney+ platform."* Motion to dismiss **granted in part and otherwise
  denied 2025-02-19**; judgment on the pleadings **denied 2025-05-21**; a writ of mandamus to the Ninth
  Circuit **denied 2025-07-18**; **trial set for 2027-08-17**, discovery in progress. (FY2025 10-K, Note 14,
  accession 0001744489-25-000155.)
- **Six shareholder derivative complaints** on the same facts (2023-08-04 Gervat, 2023-08-23 Stourbridge,
  2023-12-15 McAdams, 2025-06-27 Payne, 2025-11-05 Siegel, 2026-11-07 received), naming Iger, Chapek,
  McCarthy, Daniel and ten current and former directors, pleading *"breach of fiduciary duty, unjust
  enrichment, abuse of control, gross mismanagement, waste, and insider selling."*
- **Three consolidated private antitrust actions** (Biddle 2022-11-18, Fendelander 2022-11-30, Unger
  2025-01-14) on ESPN's carriage bundling; preliminary settlement approval of the YouTube TV and DirecTV
  Stream classes **2026-03-31**, *"for an amount that is not material"*; the Fubo class continues and seeks
  divestiture of Fubo and Hulu + Live TV.
- **Reading, with [E5-22] and [E5-17] both applied.** [E5-22]: penalty size is not seriousness in either
  direction — the *"not material"* settlement amount proves nothing about the conduct. What counts is
  whether *"they didn't act when they learned"*, and **the allegation here is precisely that the Disney+
  cost and subscriber disclosure was engineered** — i.e. it goes to the same accounting the flags below
  read. It is **unresolved litigation, and litigation is a source to read, not the primary checklist.**
  No finding of misconduct exists. **Therefore no [E5-16] disqualifier is found — and that is all it is.**
  *"Sincerity and empathy can easily be faked"* **[E5-17]**; a Q3 pass is the absence of found
  disqualifiers, never a finding that the managers are honest. **Point-in-time note for any later run: if
  the August 2027 trial produces a finding on the Disney+ disclosure, this row changes character.**

### STEP 2 — THE FLAGS **[E4-22, E5-15]**. *Accounting and disclosure, not litigation. Each a prompt to READ.*

- [ ] **weak accounting** — not found. PwC ratified 1,389.4M for / 99.4M against (2026-03-20 8-K, Item 5.07).
      No pension-assumption or comp-expensing tell.
- [ ] **unintelligible footnotes** — the opposite, and it is the strongest **[E2-26]** pass in the file:
      the 10-K files domestic *and* international attendance change, per-capita guest spending change,
      hotel occupancy, available room-nights, per-room guest spending, ARPU by service, and programming and
      production cost **split between Hulu ($9,018M) and Disney+ ($5,239M)**. A reader who wanted to know
      which streaming service is losing the money is told. *That reporting "tells you what you would want
      to know if your positions were reversed"* — it is what made this run's Q2 possible.
- [x] **trumpeted earnings projections / growth targets — FIRES, at full strength, in the 8-K.** From the
      FY2026 Q3 EX-99.1 (accession 0001744489-26-000056), in one page:
      *"We continue to expect fiscal 2026 adjusted EPS growth of approximately 12%, excluding the impact of
      the 53rd week"* · *"approximately 16%, including the impact of the 53rd week"* · *"We expect Q4 total
      segment operating income of approximately $4.9 billion"* · *"We are now targeting at least $9 billion
      in share repurchases in fiscal 2026"* · **"Fiscal 2027 outlook: We continue to expect double-digit
      growth in adjusted EPS in fiscal 2027"** · *"We continue to expect double-digit Entertainment SVOD
      operating margin for full-year fiscal 2026"* · *"We expect our future capital projects, over their
      lifetimes, to deliver double-digit returns."* **A two-year-forward adjusted-EPS growth target and a
      forward return-on-capital promise, neither reconciled to GAAP** — the filer says so itself: *"The
      Company is not providing the forward-looking measure for diluted EPS, income before income taxes …
      or reconciliations."* **[E5-30]** is the reason this matters more than the numbers do: *"once you
      start it, it's all over. You can't quit … forecasting earnings, I can't imagine anything more
      destructive."* **[E4-35]** names the cost: lofty targets *"corrode CEO behavior"*.
      **THE [E3-48] ACTION, PERFORMED — and it is the mitigant, so it goes in beside the flag.** Guidance
      against outturn, from the same document: *"Total segment operating income modestly exceeded our prior
      guidance"* · *"Our Sports segment operating income decline of 17% versus the prior-year quarter was
      **modestly steeper than our prior guidance of approximately 14%**"* · *"our Q4 Entertainment segment
      results will reflect the impact of **Moana's box office performance coming in below our prior
      expectations**"* · *"both films underperformed our box office expectations."* **They publish their own
      misses, by segment and by title, in the same release as the guidance.** Buffett's base rate is that
      *"about nine cases out of ten"* projections exist to justify a decided course, and his remedy is to
      demand *"the record of the people who made the projections."* **The record here is mixed and
      disclosed, which is better than most.** The flag still fires: the practice is the problem, not the
      accuracy.
- [x] **serial share issuance [E5-15] — fires on the history, and is now reversing.** Weighted diluted
      shares: **1,507M (FY2018) → 1,666M (FY2019, TFCF paid substantially in stock) → 1,828M (FY2021) →
      1,831M (FY2024)**, a rise of **21.5%** across a stretch in which **buybacks were zero every year
      FY2019 through FY2023** and the count still crept up on equity compensation. FY2025 1,811M; the
      FY2026 Q3 cover count is **1,726.7M**. This is acquisition consideration plus SBC, not the
      promotion-minded issuance [E5-15] describes, and it is recorded as such — but the dilution is real
      and it is the denominator of every per-share figure below.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — CLEAN on EBITDA, and verified by count.**
      `grep -c -i ebitda` returns **0 in the FY2025 10-K and 0 in the FY2026 Q3 earnings release.** The
      word appears in the filings **only** as the bank-covenant definition (*"interest coverage of three
      times earnings before interest, taxes, depreciation and amortization, including both intangible
      amortization and amortization of our film and television production and programming costs"*), which
      is a lender's term, not a promoted measure. **The CGNX companion rule of 2026-09-07 — pull the 8-K
      EX-99.1 before scoring [E4-29] — was followed, and this is the first run on disk where it clears the
      8-K as well as the 10-K.** Recorded so the rule is known to cut both ways.
      **BUT the adjusted-earnings half of the same flag fires, and this is the sharpest finding in Q3.**
      The promoted headline is **"adjusted EPS"**, which excludes restructuring and impairment charges and
      acquisition amortization. Restructuring and impairment charges, by fiscal year, off the income
      statements of the FY2021, FY2023 and FY2025 10-Ks and the FY2026 Q3 10-Q:

| FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 9M FY2026 | **total** |
|---|---|---|---|---|---|---|---|
| 5,735 | 654 | 237 | 3,892 | 3,595 | 819 | 1,139 | **16,071** |

      **Seven consecutive fiscal years. $16.1bn. Excluded from the headline every time.** **[E5-33]** is
      exact: the charges are real costs and belong in the owner-earnings mean — *"to tell owners year after
      year, 'Don't count this' … is misleading"*. **[E3-53]** names the mechanism, *"a large chunk of costs
      that should properly be attributed to a number of years is dumped into a single quarter"*, and
      **[E2-57]** the doctrine: *"'except for' should be excised from the lexicon … you must count the runs
      scored against you in all nine innings … the real mistake is not the act, but the actor."* Inside the
      total: $5.0bn of International Channels goodwill and intangibles (FY2020), $1.3bn of entertainment
      linear networks goodwill (FY2024) and $0.7bn of the same unit (FY2023), $1.3bn of Star India goodwill
      (FY2024), $812M on the A+E investment and $88M of severance in Q3 FY2026 alone. **Q4 below therefore
      does not use adjusted EPS for anything; owner earnings are built from operating cash flow, in which
      the cash portion of these charges already sits.**
- [ ] **filed-figure tells [E4-30] — DO NOT fire, and the arithmetic is shown because the FY2025 number
      looks alarming until it is read.** Cash taxes paid as a share of pre-tax income: FY2017 27.6% ·
      FY2018 17.0% · FY2019 66.5% · FY2020 n/a (pre-tax loss) · FY2021 64.0% · FY2022 20.8% · FY2023 25.0%
      · FY2024 52.4% · **FY2025 10.2%**. The FY2025 collapse is explained, dated and named in the MD&A:
      *"payments for fiscal 2025 U.S. federal and California state income tax liabilities were deferred
      until October 2025 pursuant to relief related to the 2025 wildfires in California"*, and FY2024's
      52.4% is the mirror image — *"Tax payments in the prior year reflected the payment of fiscal 2023
      U.S. federal and California state income taxes that had been deferred pursuant to relief related to
      2023 winter storms in California."* **A named, dated, natural-disaster deferral is not the [E4-30]
      tell.** Nor is there an unnatural-smoothness tell: diluted EPS from continuing operations ran
      **−1.57 · 1.11 · 1.71 · 1.29 · 2.72 · 6.85** across FY2020–25. Nothing is smooth here.
- [x] **SIXTH — metric-switching [E2-49]. FIRES, twice, and this is the second-sharpest finding.**
      *"Yardsticks seldom are discarded while yielding favorable readings. But when results deteriorate,
      most managers favor **disposition of the yardstick rather than disposition of the manager**"* — the
      demand is for *"pre-set, long-lived and small bullseyes"*. All quotes from DEF 14A filed 2026-01-22,
      accession 0001744489-26-000013.
      **(a) The TSR comparator was replaced after three consecutive total forfeitures.** *"For annual awards
      vested in fiscal 2023, 2024 and 2025, as well as Mr. Iger's new hire award vested in fiscal 2025,
      **NEOs forfeited 100% of PBUs that were subject to cumulative TSR performance measurement**"*, and
      *"our executives have received below-target payouts of annual PBUs in each of the last five years."*
      Then: *"Starting in fiscal 2025, TSR performance measured against the S&P 500 Media & Entertainment
      Index, **a more focused comparator group with similar industry dynamics as the Company and a more
      appropriate representation of our relative performance** than a more broad-based index."* **The
      yardstick that produced three zeros was exchanged for one whose constituents share the decline.**
      *The candor half, and it is real: the proxy states the change, the reason, the forfeitures and the
      years, in the same document, and flags it as previewed a year ahead. [E2-49]'s own candor case is
      "one announced ahead with reasons". Both halves are true; the flag fires and is mitigated, not
      extinguished.*
      **(b) The free-cash-flow bar was moved down while the metric deteriorated, and paid 160%.** For two
      of three bonus metrics the Committee *"increased targets year-over-year for adjusted total segment
      operating income and adjusted revenue by 12.9% and 1.2%"* and *"narrowed the performance ranges …
      which raises the bar required for a minimum bonus payout."* For the third: *"Due to significant
      planned capital expenditures at our Experiences segment … **the Compensation Committee set adjusted
      after-tax free cash flow below both fiscal 2024 target and actual results.**"* The filed outcome:
      threshold $3,464M · target $6,464M · maximum $9,464M · **actual $8,273M, which is 4% BELOW the prior
      year — and paid at 160% of target.** **The bar was cut by roughly a quarter and then beaten by 28%
      on a result that fell.** Weighted financial performance for FY2025: **146% of target** (FY2024: 129%).
      *Also disclosed, and also candid: the Committee adjusted measured performance DOWN by $1,804M net on
      free cash flow and by $79M and $226M on segment operating income and revenue to strip India — i.e.
      the discretion ran against the executives as well as for them. Recorded.*
- [x] **What pay actually vests on — [E4-27], and this is where the flags converge.** *"Never, ever, think
      about something else when you should be thinking about the power of incentives."* Annual bonus: **70%
      financial** (adjusted total segment operating income 50% · adjusted revenue 25% · adjusted after-tax
      free cash flow 25%) **/ 30% "Other Performance Factors"**. PBUs: **50% three-year average Adjusted EPS
      Growth · 25% relative TSR vs the S&P 500 Media & Entertainment Index · 25% ROIC.** So **the two
      largest single weights in the whole pay structure are adjusted total segment operating income and
      adjusted EPS growth — the two measures that exclude the $16.1bn of charges taken in seven consecutive
      years.** And the ROIC bullseye is withheld: *"for competitive reasons **we do not publicly disclose
      long-term goals for the ROIC portion** of our PBUs for ongoing performance periods"* — against
      [E2-49]'s demand for pre-set bullseyes, the target exists and the register may not see it. *The ROIC
      definition itself is disclosed and is honest about including the purchase price: invested capital is
      **total assets less cash, deferred tax assets and non-interest-bearing liabilities** — goodwill is NOT
      excluded, so the $82.6bn TFCF wedge is in the denominator management is measured on. That is the
      harder construction, and it is to their credit.*
- **[E4-52] — CONVERGING FLAGS ARE A DIFFERENT EVENT.** *"extreme consequences from **confluences** of
  psychological tendencies acting in favor of a particular outcome … it dominates life."* Count what points
  one way: (i) a two-year-forward adjusted-EPS growth target, publicly repeated; (ii) a headline measure
  that excludes seven consecutive years of charges; (iii) pay vesting 50% of PBUs on that same adjusted EPS
  growth and 50% of the bonus on adjusted segment operating income; (iv) a TSR yardstick replaced after
  three consecutive zeros; (v) a free-cash-flow bar lowered to accommodate the capex programme and then
  beaten at 160%; (vi) a buyback announced as **a dollar target** — *"at least $9 billion"* — which reduces
  the share count and so raises the per-share number the other five measure. **Six mechanisms all
  reinforcing one output: a rising reported adjusted EPS.** This is not six prompts to add up; it is one
  system, and [E4-52] says to read it as one. **[E5-38] scopes it and the scope is kept:** people Buffett
  would trust with his wallet *"would play games with any number that came to them"* — the flags read the
  accounting; the binary [E5-16] judges the person on conduct; the two tests stay distinct, and no conduct
  finding is made here.
- **The auditor's-eye test [E4-34]**, fourth question — *"any action with the purpose and effect of moving
  revenues or expenses from one reporting period to another"*. Two candidates, both disclosed: the
  California tax deferrals above (statutory, not elective) and the **53rd week**, which the filer quantifies
  itself — *"the 53rd week contributing approximately $600 million"* to Q4 segment operating income, *"a
  fairly proportionate impact on total revenues, with roughly a 1.5-2% lift"*, and *"we will lap this impact
  across the P&L in fiscal 2027."* **Guiding to growth of "approximately 12% excluding" and "approximately
  16% including" the same extra week, and naming the lap, is the disclosure [E4-34] asks for.** Recorded as
  a pass on this one test.

### STEP 3 — THE PRIMARY TEST **[E2-01]**
*"The primary test of managerial economic performance is the achievement of a high earnings rate on equity
capital employed (without undue leverage, accounting gimmickry, etc.) and not the achievement of consistent
gains in earnings per share."* Balance sheet before income statement. Computation:
`_research 2026-09-19 DIS/roc.py`; equity is attributable to Disney, from companyfacts cross-checked to the
FY2025 balance sheet ($109,869M).

| | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| net income attributable to Disney | (2,864) | 1,995 | 3,145 | 2,354 | 4,972 | 12,404 |
| average equity | 86,230 | 86,068 | 91,781 | 97,143 | 99,987 | 105,283 |
| **return on equity** | **(3.3)%** | **2.3%** | **3.4%** | **2.4%** | **5.0%** | **11.8%** |
| segment OI less corporate ÷ unleveraged net tangible assets **[E2-43]** | — | — | — | 19.4% | 21.1% | **21.5%** |
| the goodwill-and-intangibles wedge, reported separately **[E2-43]** | 96.9bn | 95.2bn | 92.7bn | 90.1bn | 84.1bn | **82.6bn** |

**Five-year mean ROE FY2021–25: 5.0%. Seven-year FY2019–25: 5.4%.** **[E2-42]**: *"Red lights should start
flashing if the five-year average annual gain falls much below the return on equity earned over the period
by American industry in aggregate."* **The red light is on.** And the second row is why, and is the honest
other half **[E2-43, E2-73]**: on *unleveraged net tangible assets*, with the purchase-price wedge held out
separately, the operating businesses earn **21.5% pre-tax** — *"the best guide to the economic
attractiveness of the operation"*. **The gap between 5.0% and 21.5% is $82.6bn of goodwill and acquired
intangibles, and that is the 2019 purchase price sitting in the shareholder's denominator.** [E2-73]:
*"what we pay for a business does not affect the amount of capital its manager has to work with"* — so the
operators are judged on the 21.5%, and the owner is judged on the 5.0%, and both figures are true.
**[E3-59]'s two yardsticks:** they run the business well against the hand dealt (21.5%, and the segment
table at Q2 shows where); the second yardstick — *"how well that they treat their owners"* — is the buyback
question below.

**The half-owner test [E2-26]:** **passes, and unusually well.** See the footnotes bullet above. The one
place it does not pass: the NFL Transaction, in which 10% of ESPN changed hands and **no valuation of
either side is filed** — only *"non-cash tax charges resulting from the Fubo and NFL Transactions"*. An
owner would want to know what a tenth of ESPN was worth.

### The institutional imperative — score all four **[E2-30]**
*Not a fraud test: "institutional dynamics, not venality or stupidity."*
- [ ] **resists any change in current direction** — no. Star India sold into the Viacom18 joint venture,
      the linear networks written down twice, ESPN DTC launched August 2025, Fubo acquired, the CEO
      succeeded on schedule. This management changes direction.
- [x] **projects/acquisitions materialise to soak up available funds** — capex $3,578M (FY2021) → $4,943M
      → $4,969M → $5,412M → **$8,024M (FY2025)** → *"approximately $9 billion"* guided FY2026; plus
      $8,610M for the Hulu minority (FY2024) and a further $439M on final appraisal (FY2025), $1,506M for
      Epic Games (FY2024), and Fubo. **$104.1bn of forward commitments.** The direction of the *recent*
      spend is the right one (80.1% of FY2025 capex into the franchise leg), which is the mitigant.
- [x] **staff studies produced to justify the leader's craving** — the pay design is the filed instance,
      and it is **[E3-58]**'s delegation prompt: *"Management recommends financial and other performance
      measures, weightings and ranges"*, and the Committee then *"reviews proposed performance measures and
      ranges with input from its consultant and approves"* them. Management proposes the bar it is paid
      against; a consultant validates it.
- [x] **peer behaviour mindlessly imitated** — **the clearest instance in the file, and it is now filed
      history.** Every major studio launched a general-entertainment subscription service within thirty
      months of each other and spent a decade of profits on it. Of the four: Comcast **completed** the
      separation of its cable networks into Versant on 2026-01-02; Warner Bros. Discovery announced a
      two-company split, was bid for by Netflix at ~$72bn, terminated that agreement, paid Netflix
      **$2.8bn**, and agreed to be bought whole by Paramount Skydance at $31.00 cash; Paramount was itself
      taken over in August 2025. **Disney did the same thing at the same time as everyone else, and the
      industry is now being taken apart.** [E2-30]'s last clause governs: this is institutional dynamics,
      not venality.

### Capital allocation — the buyback conditions **[E5-08, E4-31]**
- **(1) ample funds for operations and liquidity?** Yes. $12,250M of committed bank facilities, **capacity
  used $0**; Moody's A2/P-1, S&P A/A-1 (Fitch withdrew for commercial reasons 2025-09-29). Cash $5,695M.
- **(2) repurchases at a material discount to conservatively calculated IV?** **NO, on our own range — and
  the failure is structural, not a matter of our estimate being right.** $2,992M repurchased in FY2024,
  $3,500M in FY2025, **$7,245M in the nine months to 2026-06-27** against $2,496M in the comparable prior
  period, and the target is announced as a **dollar amount**: *"We are now targeting at least $9 billion in
  share repurchases in fiscal 2026."* **[E5-24]** is the first law of capital allocation — *"what is smart
  at one price is dumb at another"* — and **a pre-committed dollar amount is price-indifferent by
  construction.** **[E5-25]** shows what real compliance looks like: Berkshire published **both conditions
  as numbers in advance** (the 110%-of-book limit, the $20bn liquidity floor). Disney publishes the spend
  and not the price. **[E4-31]**'s third condition — *"Shareholders should have been supplied all the
  information they need for estimating that value"* — is the closest thing to a pass, because the
  disclosure genuinely is good (see [E2-26] above); but no intrinsic-value condition is stated at all.
  → **CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**: *"it is natural for CEOs to
  be optimistic about their own businesses. **They also know a whole lot more about them than I do.**"*
  This rests on our own owner-earnings range (Q4 below: a 2.1–3.5% yield on the five-year window at
  $102.67), and *"many CEOs never stop believing their stock is cheap"* **[E5-08]** — infractions here are
  innocent. **It binds position size, never the discount rate — and position size is nil, because Q2 is
  OUT.** **[E2-51]**'s inverse reading does not apply either way: the FY2019–FY2023 refusal to repurchase
  was forced by the TFCF leverage and the pandemic, not chosen.
- **[E2-52] — dividends funded by issuance? NO.** Dividend $1,366M (FY2024) → $1,803M (FY2025), raised 50%
  to $1.50 a share, against net share *retirement*. The [E2-52] test is passed.
- **[E5-44] — stock deals run the same law in shares, and one was done in January.** *"The intrinsic value
  of the shares you give in an acquisition must not be greater than the intrinsic value of the business you
  receive."* On 2026-01-31 Disney gave **a 10% noncontrolling interest in ESPN** for NFL Network, NFL
  RedZone's pay-TV distribution and NFL Fantasy. What was received is three pay-TV assets in the declining
  channel the rest of this run measures; what was given is a tenth of a business that earned $2,882M of
  segment operating income. **No valuation of either side is filed.** And within the same quarter the NFL
  Network was removed from Comcast Xfinity and *"service has not been reinstated."* Flag, unquantifiable
  from the filings, recorded.
- **[E3-54] retention, and [E4-39]'s rare positive.** The 2019 purchase added roughly **$49.0bn of goodwill
  and $16.4bn of intangibles** and 300-odd million shares; $2.6bn of that goodwill has since been written
  off by reporting unit, and **Entertainment earns 5.7% pre-tax on the capital it carries**. **No candid
  acquisition post-mortem against the announcement case was found in any filing searched** (the FY2021,
  FY2023, FY2025 10-Ks, the FY2026 Q3 10-Q, the 2026 proxy and the FY2026 Q3 earnings release) — worded as
  "no instance found", per the absence-claim rule. [E4-39]: such a post-mortem is *"almost never
  witnessed"*, so its absence is the base case, not an accusation; but the credit [E4-39] awards is not
  earned.

### Loss of focus — **[E3-40]**, and it is the right diagnosis of the decade, not of today
*"A far more serious problem occurs when the management of a great company **gets sidetracked and neglects
its wonderful base business while purchasing other businesses that are so-so or worse** … Loss of focus is
what most worries Charlie and me."* In filed numbers: between FY2019 and FY2023 Disney spent roughly $65bn
of purchase price on a library-and-networks acquisition, $8.6bn on the Hulu minority, and $22–24bn a year
on content — while **Experiences capex fell to $3,578M in FY2021** and the base business's plant went
under-fed through the very period its competitor was building Epic Universe. **[E5-45]**'s ABCs are the
slower version of the same read and are a Q6 monitoring item.
**The turn is filed and it is real: 80.1% of FY2025 capex went to Experiences, capex is guided to ~$9bn,
and the new CEO is the man who ran that segment.** A future run should score this flag as *fired in the
past decade and reversing*, not as live.

### THE GUARDRAIL — check before writing the verdict
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** It cannot be — Q2 is OUT, and
      *"a textile company that allocates capital brilliantly within its industry is a remarkable textile
      company — but not a remarkable business"* **[E2-37]**; *"good jockeys will do well on good horses,
      but not on broken-down nags"* **[E2-38]**; *"averaged out, betting on the quality of a business is
      better than betting on the quality of management"* **[E3-39]**.
- [x] **Key-person dependence is recorded at Q2 as a moat defect [E4-23]**, in the Content
      Sales/Licensing leg, where the quarter turns on two release outcomes. **At the company level the
      opposite is now filed:** on 2026-02-02 the Board appointed **Josh D'Amaro**, Chairman of Disney
      Experiences since 2020 — the head of the single leg that *is* a franchise — as Chief Executive
      Officer effective **2026-03-18**, with Iger moving to Senior Advisor *"reporting exclusively to the
      Board"* through **2026-12-31**; Dana Walden became President and Chief Creative Officer; D'Amaro
      joined the Board on 2026-03-18 (8-Ks 0001744489-26-000022 and 0001628280-26-020172). **An internal
      promotion from the best-performing segment, announced with a date and executed on it, is the most
      favourable single fact in this Q3** — and it is *"the knight … who throws the crocodiles into the
      moat"* **[E4-33]**, which sets the moat's direction and never its existence. Say-on-pay passed
      1,091.7M for / 181.8M against (**85.7%**); Lagomasino drew the most against votes (87.4M).
      *Pay scale, recorded without comment beyond the filing's own: D'Amaro base $2.5M, bonus target 250%,
      annual LTI target $26.25M plus a one-time $9.705M; Iger's FY2025 total $45,851,157 against a median
      employee total of $56,932 — the filer's own ratio, **805:1**.*
- [x] If a great manager were the reason to act **[E2-35, E2-36]**: **the franchise is intact and the
      damage is not excisable by a surgeon** — it is $84.1bn of signed rights contracts and $82.6bn of
      purchase price. The excisable-cancer exception does not open here; the required act is a corporate
      separation, not a skilled operator, and **[E4-24]** governs what to do about a good business whose
      capital wanders: *"you'll probably do better to get out"*, with Munger's rating of the engagement
      alternative — *"Worse than poor."*

- **VERDICT: [x] IN — meaning ONLY that no [E5-16] disqualifier was found.** *Not a finding that the
  managers are honest — "sincerity and empathy can easily be faked" **[E5-17]**; and the filed statement
  itself is not bedrock **[E5-32]**. **IN never promotes, and here it cannot: the file closed at Q2.**
  Live flags carried forward: the projections flag at full strength **[E4-22, E5-30]**; the
  adjusted-earnings half of **[E4-29]** across seven consecutive years of charges; **[E2-49]** twice; a
  **CAPITAL ALLOCATION FLAG** on a dollar-target buyback **[E5-08, E5-24, E5-25]**; an unvalued stock deal
  **[E5-44]**; and the six of them converging on one output, which **[E4-52]** says to read as one system.
  An unresolved securities class action about the Disney+ disclosure goes to trial on 2027-08-17 and would
  change this row's character if it produces a finding.*

## Q4 — WILL IT SURVIVE?

> ⚠️ **RECORDED, NOT GOVERNING.** Q2 is OUT. Q4 is done in full because the (c) construction for a filer
> whose content spend runs through operating cash flow is worth having on disk, and because the brief asked
> for it. Computations: `_research 2026-09-19 DIS/oe2.py` and `death.py`.

### Owner earnings — the one number **[E2-23]**

**FIRST, THE THING THAT GOVERNS (c) FOR THIS FILER, AND IT IS NOT THE CAPEX LINE.**
Disney runs **film, episodic, sports and programming cash spend through OPERATING cash flow**, not through
investing. The FY2025 cash-flow statement shows *"Net change in produced and licensed content costs and
advances | 577"* as an **add-back**, which is the amount by which content **amortization of $23,286M
exceeded cash content spend of $22,709M**. So:

- **Cash content spend is already deducted inside OCF.** Adding it to (c) would double-count $22.7bn a year.
- **The cash-flow "Depreciation and amortization" line of $5,326M is NOT the right (c) proxy either.** It
  is depreciation $3,859M **plus** amortization of intangible assets $1,467M, of which **$1,307M is TFCF
  and Hulu purchase-price amortization** — the amortization of a 2019 cheque, which requires **no
  replacement spending whatever**. Using $5,326M as (c) charges the shareholder for the acquisition a
  second time. **The correct D&A proxy for (c) at this filer is DEPRECIATION ALONE: $3,859M (FY2025),
  five-year mean $3,434M.** *(Tooling note for the operator: any construction that reads a
  `DepreciationDepletionAndAmortization` tag as the (c) default overstates (c) by about $1.5bn a year for
  DIS. Recorded in the defect list at the end.)*
- **Is the content library being maintained? Not quite, and it flatters recent OCF.** Cash spend was
  **below** amortization in both filed years (−$577M FY2025, −$1,046M FY2024) and production and
  programming assets fell from $36,593M (opening FY2024) to **$33,390M**. That is a 2.4%-a-year run-down on
  an operating basis, and the filer guides FY2026 content spend **up**, to *"approximately $24 billion
  including sports rights"* from $22.7bn. **Judgment, disclosed: content requires no (c) addition because
  it is inside OCF, but FY2024–25 operating cash flow is flattered by roughly $0.6–1.0bn a year of
  under-spending the library, which is a reason not to trust the top of the range below.**

**SECOND, THE [E5-20] QUESTION, ASKED ON THE FILING AND ANSWERED.**
*"in the case of all railroads, merely spending their depreciation expense will not keep them in the same
place."* Does Disney fall in that exception class, which would make the D&A end **INVALID** rather than
merely optimistic?
- **For it:** gross attractions, buildings and equipment $82,041M against accumulated depreciation
  $48,889M — **59.6% depreciated** on stated lives of *"20 – 40 years"* for attractions, buildings and
  improvements, so the book cost of a 1971-vintage Magic Kingdom asset bears no relation to what replacing
  it costs today. **[E4-47]** applies directly: *"inflation destroys value … very unequally"*, and
  replacement capex in current dollars outruns depreciation charged in old dollars for asset-heavy filers.
  Experiences depreciation is itself rising fast — $2,470M → $2,715M → $2,368M in nine months (≈$3,157M
  annualised) — which is the signal that today's spending is entering service at a much higher cost basis.
- **Against, and this is the decisive half, because it is filed by peers rather than reasoned:**
  (i) Disney is **not capital-intensive by the measure the framework's own prior runs used.** Gross PP&E
  including land and projects in progress is $90,144M against revenue of $94,425M — **0.95×**, against the
  **5.1×** recorded for EQIX and DLR in the queue notes of 2026-09-18. Depreciation is 4.1% of revenue.
  (ii) **The two listed theme-park operators that actually file a maintenance/growth capex split put
  maintenance at roughly depreciation, not a multiple of it.** United Parks files *"capital expenditures for
  park rides, attractions and maintenance activities"* of **$182.4M against depreciation of $168.0M** (a
  three-year mean of $195.4M against $159.3M = **1.23×**); Six Flags states a floor of *"approximately $125
  million to $150 million"* of *"required minimum annual maintenance and infrastructure capital
  expenditure"* against FY2025 depreciation of $486M. **No peer's disclosed maintenance capex is a large
  multiple of its depreciation.**
- **ANSWER: the [E5-20] exception class does NOT apply. The depreciation end of (c) is the OPTIMISTIC BOUND
  of a legitimate band, not an invalid figure** — which is a different answer from AMZN, EQIX and DLR, the
  three names in this queue where the class did apply. The peer anchor is used instead to set the middle.

**THIRD, (c) ITSELF — A DISCLOSED JUDGMENT, BUILT THREE WAYS. "(c) must be a guess."**

| construction | basis | 5-yr mean FY2021–25 | FY2025 | authority |
|---|---|---|---|---|
| **low / optimistic** | depreciation only | **3,434** | 3,859 | the corpus default **[E3-44, E2-41]** |
| **central** | depreciation × 1.20 | **4,121** | 4,631 | the United Parks filed maintenance-to-depreciation ratio, 1.23× on three-year means |
| **high** | total capital expenditure | **5,385** | 8,024 | the [E5-20] treatment, used as the pessimistic bound |
| *(for reference)* | FY2026 guided capex | — | **~9,000** | *"approximately $9 billion"*, MD&A |

**Why total capex is the pessimistic bound and not the central case, in the filer's own words.** The FY2025
spend is described as *"principally for theme park and resort expansion, new attractions, cruise ships,
capital improvements and systems infrastructure"* — **expansion named first** — and the FY2026 increase is
*"primarily due to higher spending at Experiences, attributable to theme park and resort expansion and new
attractions."* Management's own claim about it: *"We expect our future capital projects, over their
lifetimes, to deliver **double-digit returns**."* **If that claim is true, most of $8–9bn a year is growth
capital and does not belong in (c) at all. If it is false, owner earnings are grossly overstated. The
filing gives NO maintenance/growth split, and that absence is the single largest uncertainty in this
section.** It is disclosed as the guess [E2-23] says it must be.

*The working-capital increment [E2-23] constraint 3 is inside OCF by the framework's own CONVENTION — the
FY2025 changes in operating assets and liabilities net to −$430M, and the filer holds $2,063M of content
advances and $6,248M of deferred revenue, so the increment is immaterial to the band.*

**FOURTH, STOCK COMPENSATION — SUBTRACTED IN FULL, AND IT RESOLVES AND IS COMPLETE.**
`ShareBasedCompensation` is published for **every** fiscal year FY2017–FY2025 and is non-zero in all nine;
there is no SBC hole and no zero substitution. The charge reconciles to the filed footnote
(FY2025: options $70M + RSUs $1,293M = $1,363M).
**[E3-70]** requires the market value of the grant, not the accounting charge: *"an amount equal to what the
company could have realized by publicly selling options of like quantity and structure"* — the reported
charge is **the floor of the subtraction, not the measure.** Grant-date fair value of each year's grants
(RSU units × weighted-average grant-date fair value, plus ~2M options × their WAGDFV, all from the filed
equity footnotes and the XBRL grant tags; unit counts are rounded to whole millions in the filings, so
these are approximate and labelled):

| $M | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|---|
| charge, net of capitalised | 711 | 525 | 600 | 977 | 1,143 | 1,366 | 1,363 |
| capitalised (footnote: excluded from the charge) | — | — | — | — | 145 | 201 | 194 |
| **[E3-70] grant-date value** | 508 | 929 | 1,191 | 1,866 | 1,680 | 1,754 | **1,812** |
| grant ÷ charge | 0.71× | 1.77× | 1.99× | 1.91× | 1.47× | 1.28× | **1.33×** |

**Grant value exceeds the charge in six of the seven years, by 28% to 99%.** Five-year means FY2021–25:
charge **$1,090M**, grant value **$1,661M** — a gap of $571M a year. Both are carried through the
owner-earnings table below, which is what [E3-70] requires. **SBC is 7.5% of FY2025 operating cash flow at
the charge and 10.0% at the grant measure — material, but nowhere near the [ARM/PATH] class.**

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE **[E4-25]**
*"Using precise numbers is, in fact, foolish; working with a range of possibilities is the better
approach."* **[E4-38]**'s remedy applied: **every** window is published, not a chosen one, and the pandemic
years are shown **both in and out, never silently dropped.** Owner earnings = OCF − SBC − (c).

| window | mean OCF | SBC chg | SBC grant | dep | capex | **OE at dep + chg** | OE at dep + grant | OE at capex + chg | **OE at capex + grant** |
|---|---|---|---|---|---|---|---|---|---|
| **FY2021–25 — the corpus default [E2-42]** | 10,701 | 1,090 | 1,661 | 3,434 | 5,385 | **6,177** | 5,607 | 4,226 | **3,655** |
| FY2019–23 — the earlier five | 7,007 | 791 | 1,235 | 3,172 | 4,478 | 3,043 | 2,600 | 1,738 | **1,294** |
| FY2019–25 — every year at this perimeter | 9,587 | 955 | 1,391 | 3,308 | 5,118 | 5,324 | 4,887 | 3,514 | 3,077 |
| **FY2022–25 — pandemic years EXCLUDED** | 11,985 | 1,212 | 1,778 | 3,526 | 5,837 | **7,247** | 6,682 | 4,936 | **4,370** |
| FY2023–25 — the current shape | 13,979 | 1,291 | 1,749 | 3,640 | 6,135 | **9,049** | 8,591 | 6,554 | 6,096 |
| FY2017–19 — pre-TFCF, pre-streaming | 10,874 | 400 | 400 | 2,729 | 4,321 | 7,745 | — | 6,153 | — |

At the **central** (c) of 1.20× depreciation the default window gives **$5,491M** (charge) and **$4,920M**
(grant value). **TTM to 2026-06-27**: OCF $16,989M − SBC $1,519M − capex $8,696M = **$6,774M**; at
depreciation of ~$4,100M, **$11,370M**. On the company's own FY2026 guidance (OCF ≥$19,000M, capex
~$9,000M): **$8,481M**; at depreciation, $13,381M.

- **Spread, conservative end:** $1,294M (FY2019–23, capex + grant value) to $4,370M (FY2022–25, same
  construction) — **a 3.4× spread on the conservative end alone.**
- **Combined range (window spread × capex band × SBC measure): $1,294M to $9,049M — a 7.0× range.**
- **Is that range too wide to reach a conclusion [E4-25]?** For the *level*, yes. **For the decision, no,
  and that is why the file does not close here:** every corner of the range, at every window and both (c)
  ends, is **below** the 30-year sovereign and **far** below the ~10% floor at the current price (Q5).
  **[E4-25]**'s "too wide" rule closes a file when the width straddles the answer. It does not here.
- **The wide spread is itself a Q4 finding [E5-11], and the distorted years are named, not dropped:**
  **FY2020 and FY2021 are a pandemic trough** — parks closed, cruises suspended, OCF $7,616M and $5,566M
  against $14,295M in FY2018 — and **FY2019 is a part-year perimeter** (TFCF consolidated from
  2019-03-20), which is why FY2019 OCF of $5,984M sits below FY2018's $14,295M despite revenue rising
  $10bn. Both effects are shown by giving the FY2022–25 window beside the FY2021–25 one. **[E3-55]** scopes
  it correctly: this width is **not** the See's-Candies kind of noise around a certain mechanism; it is
  genuine uncertainty about the level, produced by a pandemic, a perimeter change and a (c) the filer
  refuses to split.
- **[E4-41] — normalize DOWN for luck, and there is one to remove.** FY2025 operating cash flow of
  $18,101M is flattered by a **named, dated tax deferral**: *"payments for fiscal 2025 U.S. federal and
  California state income tax liabilities were deferred until October 2025 pursuant to relief related to
  the 2025 wildfires in California."* Cash taxes were $1,221M on $12,003M of pre-tax income (10.2%) against
  a nine-year median nearer 26%. **Normalising FY2025 cash taxes to 25% of pre-tax income would remove
  roughly $1.8bn from FY2025 OCF**, taking the FY2023–25 window's top figure from $9,049M to about
  $8,450M. Removed before the mean is trusted, as [E4-41] requires.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — [x] **good** — [ ] gruesome
**Evidence, and it is two different answers inside one security.** *"The great one pays an extraordinarily
high interest rate that will rise as the years pass. The good one pays an attractive rate of interest that
will be earned also on deposits that are added."*
- **Experiences is GREAT on the filed numbers**: 28.9% pre-tax on its computed capital, 27.6% operating
  margin, price raised 5% with volume flat, and 80.1% of FY2025 capex going into it at a management-claimed
  double-digit return.
- **Entertainment and Sports are at best GOOD and arguably below it**: **7.0% pre-tax** on $107.8bn of
  computed capital, ≈5.3% after tax at 25%, against **[E5-40]**'s stated benchmark that ~12% on retained
  capital is *"quite satisfactory"*. They do not fit *gruesome* either — **[E4-43]** is explicit that only
  the gruesome fails Q4, and gruesome means *"grows rapidly, requires significant capital to engender the
  growth, and then earns little or no money."* Entertainment does not grow rapidly; it declines slowly on a
  purchase price. **It is a poor return on capital, not a bottomless pit.**
- **Blended: GOOD.** Q4 does not fail on this test. **[E4-43]**: *"good ranks below great at Q5, and that
  is all."* — except that here Q5 never opens.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — PASSES, and comfortably.** $94,425M of revenue, $17,551M
  of segment operating income, $18,101M of operating cash flow, across four independent collection
  mechanisms in twelve countries; Experiences alone earns $9,995M. Moody's **A2/P-1**, S&P **A/A-1**, both
  Stable (Fitch withdrew its A−/F2 for commercial reasons on 2025-09-29 — recorded, because a withdrawn
  rating is a disclosure event).
- **(2) massive liquid assets — FAILS on the corpus's standard, and the filing shows why.** Cash and
  equivalents **$5,695M**, which is **2.9% of total assets** and **less than the $6,751M of borrowings
  maturing in FY2026**. Disney's own liquidity statement counts *"access to debt and equity capital markets
  and **borrowing capacity under current bank facilities**"* — $12,250M committed, **$0 drawn** — and it
  uses the commercial-paper market actively (net CP repayment $943M in FY2025; net CP **borrowing** $2,268M
  in the nine months to 2026-06-27). **[E5-39]** is the standard and it is not met: *"We will never be
  dependent on **the kindness of strangers** … cash is a lot like oxygen: you don't notice it 99.9 percent
  of the time. But if it's absent, it's the only thing you notice."* **[E2-64]**'s offensive half also
  fails: this balance sheet is not built to buy in a storm.
  *The candour half is real and goes in: the filer lists the levers by name — if liquidity tightens it
  would consider *"raising additional financing, reducing or not declaring future dividends; reducing or
  stopping share repurchases; reducing capital spending; reducing film and episodic content investments; or
  implementing further cost-saving initiatives."* That is what [E2-26] asks for, and it is also the
  **[E2-60]** warning in the filer's own hand: the payout is the first thing that goes.*
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAILS, and this is the one [E5-11] says usually
  kills.** FY2026, from the filed tables and the company's own guidance:

| FY2026 | $M |
|---|---|
| borrowings maturing (Note 8) | 6,751 |
| interest on borrowings (Note 8) | 1,559 |
| programming and other contractual commitments (Note 14, FY2026 column) | 17,007 |
| capital expenditure, guided *"approximately $9 billion"* | 9,000 |
| dividends (approx., $1.50 × ~1.73bn shares) | 2,400 |
| buyback target, *"at least $9 billion"* | 9,000 |
| **total intended and contracted outflow** | **45,717** |
| **guided operating cash flow, *"at least $19 billion"*** | **19,000** |

  Most of the $17,007M of commitments is the operating cost base and already sits inside operating cash
  flow, so the fair statement is: **non-cancellable, non-operating outflow of $17,310M** (debt service plus
  capex) **against $19,000M of guided operating cash flow, with $11,400M of dividends and buybacks
  announced on top of it.** The buyback is therefore being funded from the balance sheet, and the nine
  months to 2026-06-27 show exactly that — $7,245M of repurchases against $2,268M of net new commercial
  paper and $5,046M of new borrowings.
  **And the number that makes strength 3 a structural failure rather than a timing one: $104,088M of signed
  contractual commitments, $84,076M of it sports rights — 59% of the entire market capitalisation, 4.8× the
  company's annual segment operating income — running at $9.1–9.9bn a year through FY2030 with $36,610M
  thereafter.**
- **[E2-54]'s coverage test — PASSES, and it is the strongest survival fact in the file.** *"whenever
  someone creates a capital structure that does not allow all interest, both payable and accrued, to be
  comfortably met out of current cash flow net of ample capital expenditures — zip up your wallet."*
  FY2025: ($18,101M − $8,024M) ÷ $2,050M of interest paid = **4.9×**. FY2024: **4.0×**. FY2026 guided:
  **4.9×**. Comfortable by any reading.
- **Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this framework and the
  corpus supplies none*: total borrowings **$42,026M** ($6,711M current, $35,315M non-current) against total
  equity of $114,612M (0.37×) and net of cash **$36,331M = 2.07× segment operating income**. Interest
  expense net $1,305M is covered 13.4× by segment operating income; total interest paid $2,050M with
  $322M of it capitalised into parks and film production.
- **[E3-52] — read the terms, not just the quantity, and they cut both ways.** The good half: **one**
  financial covenant across $12.25bn of facilities — *"interest coverage of three times earnings before
  interest, taxes, depreciation and amortization, including both intangible amortization and amortization
  of our film and television production and programming costs"*, met *"by a significant margin"* — with
  Asia Theme Parks and Fubo carved out of all representations and events of default, and maturities long
  ($25,872M of $41,251M falls after FY2030). The bad half: **the $84.1bn of rights commitments are the
  inverse of float.** Float is *"where we get the money first and we have the expense later"*
  **[E5-41]**; here the expense is contracted first and the revenue may or may not arrive — and the filer
  says so: *"There can be no assurance that revenues from programming based on these rights will exceed the
  cost of the rights plus the other costs of producing and distributing the programming."*
- **Jurisdiction [E3-66]:** a US registrant; shareholders stand first in the queue. No adjustment.
- **[E5-29] and [E2-55]:** risk here is impairment, not price movement, and the worst case is scored, not
  the expected one — which is what the next section does.

### Name the specific way THIS business dies **[E2-27, E3-24]**
**Named against `Screens/SURVIVAL SHAPES - index.md`: shape #10, THE CAMOUFLAGE** (first named by SONY,
2026-09-13) — *"cash from the strong legs is recycled into legs that must re-win a race each cycle; the
company lives, the owner's return does not"* — **with shape #1, CONTRACTED NOT TO STOP, as a feature**
(*"commitments already signed oblige spending the business may not recover"*). **No new shape is proposed.**
Disney is the cleanest instance of #10 on disk: the strong leg is visible and separately reported (28.9% on
its capital), the recycling is visible ($22.7bn a year of content, $9.9bn a year of contracted sports
rights), and the race re-run each cycle is visible in two forms — a rights auction and a carriage
renegotiation.

- **THE MECHANISM.** ESPN's cost base is contracted years forward and cannot be reduced. Its revenue is a
  per-home fee collected through distributors, from a base that is shrinking at a measured rate in three
  independent filers' disclosures, offset so far by rate rises that those distributors have now twice
  refused. The moment the rate rise stops clearing, the contracted cost stays and the fee does not. The
  same arithmetic runs in the Linear Networks leg one step further along, where the goodwill has already
  failed its impairment test twice.
- **QUANTIFIED FROM FILED FIGURES.** ESPN domestic revenue $16,085M, operating income $2,801M, costs
  therefore $13,284M, of which **contracted programming and production is $12,492M**. Affiliate and
  subscription fees $11,944M.

| fall in ESPN affiliate and subscription fees | $M lost | ESPN domestic operating income | change |
|---|---|---|---|
| 5% | 597 | 2,204 | −21% |
| 10% | 1,194 | 1,607 | −43% |
| 15% | 1,792 | 1,009 | −64% |
| **23.5%** | **2,807** | **−6** | **−100%** |

  **The wipe-out point is a 23.5% fall in the fee line.** At the rate of unit loss Disney itself files —
  *"a decrease of 7% from fewer subscribers"* — with the offsetting 7% rate rises no longer clearing, 23.5%
  arrives in **3.7 years**. The units are corroborated outside Disney: **Comcast's domestic video customers
  fell 1.3 million to 11.3 million in FY2025** (10-K 0001628280-26-004994) and WBD reports *"an 8% decline
  in domestic linear subscribers … Declines in linear subscribers are expected to continue"* (10-K
  0001437107-25-000031). **Combined exposure: ESPN domestic $2,801M plus Linear Networks $2,955M = $5,756M,
  32.8% of segment operating income, resting on rate rises that YouTube TV refused on 2025-10-30 and that
  Comcast Xfinity is still refusing for NFL Network at the date of the Q3 10-Q** — against $84,076M of
  signed rights that do not fall with it.
- **MODEL EXPOSURE, NOT EXPERIENCE [E4-40].** *"all of us in the industry made a fundamental underwriting
  mistake by focusing on experience, rather than exposure."* The **experience** is twenty years of rate
  rises that worked and two decades of ESPN as the single most profitable cable network in America. The
  **exposure** is the table above plus $84.1bn of signed contracts, and the experience is *"not only
  useless, but actually dangerous"* as a guide to it.
- **LIKELIHOOD: [ ] likely · [x] a real possibility · [ ] a low-level possibility.** Not *likely* within
  five years, for reasons that must be stated because **[E4-51]** requires the bear case to be one its
  holders would accept as fairly stated — and so must the bull case here:
  **the company is building the replacement channel and the sport itself is not declining.** ESPN's own DTC
  service launched in August 2025; the latest release reports *"a growing number of subscribers"* and
  *"relationships with the NFL, MLB, FOX One, and — launched just yesterday — the CW Network"*; **domestic
  ESPN advertising revenue rose 14% in FY2025 on 13% higher rates** with expanded College Football Playoff
  games. That is the opposite signal from the affiliate line. **The death is a race between the DTC ramp
  and the affiliate melt, run against a cost base that is already signed.** Nothing in the filings settles
  which wins, and Disney has $94bn of revenue and A2/A ratings while it runs. Hence *a real possibility*,
  and hence the company survives the mechanism even where the owner's return does not — which is precisely
  what shape #10 says.

- **VERDICT: [x] IN** — **RECORDED, NOT GOVERNING.** *It survives: $94bn of revenue, 4.9× interest
  coverage after ample capex [E2-54], one covenant met by a significant margin, long maturities, A2/A.
  Recorded against it: **two of the three [E5-11] strengths fail** — liquid assets are 2.9% of assets and
  the liquidity statement leans on undrawn bank lines and commercial paper, which **[E5-39]** refuses; and
  near-term cash requirements are large and contracted, $104.1bn of commitments against a $177.3bn market
  capitalisation. The owner-earnings range is **$1,294M to $9,049M**, a 7.0× spread, and it is wide because
  a pandemic, a perimeter change and an undisclosed maintenance/growth capex split all sit inside it.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

# ⛔ COMPUTATION — NOT A CLEARANCE

**Q2 is OUT. Q5 has NOT opened. Nothing below is an entry finding, a target, a valuation opinion or a
ranking, and none of it may be quoted as one.** Operator rule 3: *"Any valuation math produced before
Q1-Q4 close must be headed 'COMPUTATION — NOT A CLEARANCE' and may carry no entry language."* It is
computed because the brief asked for the price and the pass/fail in words, and because a name that failed
on the business should be shown not to have been a near miss on price either. Arithmetic:
`_research 2026-09-19 DIS/q5calc.py`.

**The price, and what the buyer is paying for, in words.**
At **$102.67** (close 2026-09-18, aggregator, flagged) on **1,726,686,902** shares from the FY2026 Q3
cover, the market capitalisation is **$177,279M**. Against the **US Treasury 30-year par yield of 5.34%**
(2026-09-18, issuing authority), **the buyer at this price is paying $177bn for a business whose owner
earnings over the corpus's default five-year window are $3.7bn to $6.2bn — a yield of 2.1% to 3.5% — and,
on the most generous construction anywhere in this file (the company's own FY2026 guidance of at least $19bn
of operating cash flow, with (c) at depreciation and stock pay taken at the charge rather than the grant),
$13.4bn, or 7.55%.** Nothing in the range reaches the ~10% floor. **In plainer words still: the buyer is
paying roughly 14 times the optimistic end of a normalised owner-earnings figure and about 29 times the
five-year conservative one, for a company whose owner earnings PER SHARE have not grown in seven years,
and he is simultaneously buying $104bn of signed forward commitments worth 59% of what he is paying.**

**THE FLOOR, BEFORE THE RANKING [E4-28, E3-13].** *"that's the figure we quit on … that's true whether
short rates are 6 percent or whether short rates are 1 percent."*
**Honest pre-tax expectancy at this price, no growth assumed: 2.1% to 3.5% on the default window; 4.8% to
7.6% on the company's own forward guidance. Every construction is below roughly 10%. The name is QUIT ON,
and the ranking lines are not filled in.** *(It would have been quit on at Q5 even had Q2 passed. Two
independent reasons to stop is not two half-reasons.)*

**1. THE YIELD** — owner earnings ÷ market cap, beside the sovereign of **5.34%**

| window and (c) construction | owner earnings | **yield** | vs the bond |
|---|---|---|---|
| **FY2021–25, the corpus default [E2-42]** | $3,655M – $6,177M | **2.06% – 3.48%** | below at both ends |
| FY2021–25 at the **central** (c) of 1.20× depreciation | $4,920M – $5,491M | **2.78% – 3.10%** | below at both ends |
| FY2019–23, the earlier five | $1,294M – $3,043M | 0.73% – 1.72% | below at both ends |
| FY2019–25, every year at this perimeter | $3,077M – $5,324M | 1.74% – 3.00% | below at both ends |
| FY2022–25, **pandemic years excluded** | $4,370M – $7,247M | 2.47% – 4.09% | below at both ends |
| FY2023–25, the current shape | $6,096M – $9,049M | 3.44% – 5.10% | below at both ends |
| TTM to 2026-06-27 | $6,774M – $11,370M | 3.82% – 6.41% | clears the bond at the top end only |
| **FY2026 on the company's own guidance** | $8,481M – $13,381M | **4.78% – 7.55%** | clears the bond at the top end only |

**2. WHAT THE PRICE ALREADY ASSUMES.** Perpetual growth required to justify $177,279M:

| | at the ~10% floor | at the sovereign 5.34% |
|---|---|---|
| on the default window, conservative (c) | **+7.94% for ever** | +3.28% for ever |
| on the default window, D&A (c) | +6.52% for ever | +1.86% for ever |
| on the central (c) | +7.22% to +6.90% | +2.56% to +2.24% |
| on the company's own FY2026 guidance | +5.22% to +2.45% | +0.56% to −2.21% |

**WHAT THE BUSINESS HAS ACTUALLY DONE**, off the filed statements:

| | | |
|---|---|---|
| revenue FY2018 → FY2025 | $59,434M → $94,425M | **+6.84% a year** *(of which the 2019 purchase is most of it)* |
| revenue FY2019 → FY2025, post-TFCF | $69,607M → $94,425M | +5.21% a year |
| operating cash flow FY2018 → FY2025 | $14,295M → $18,101M | +3.43% a year |
| net income attributable FY2018 → FY2025 | $12,598M → $12,404M | **−0.22% a year** |
| **owner earnings PER SHARE, D&A end of (c)** | **FY2018 $7.39 → FY2025 $7.11** | **−0.56% a year over seven years** |
| **owner earnings PER SHARE, capex end of (c)** | **FY2018 $6.26 → FY2025 $4.81** | **−3.70% a year** |
| segment operating income FY2023 → FY2025 | $12,863M → $17,551M | +16.81% a year *(off a trough)* |

**The price needs roughly 7–8% perpetual growth to clear the floor. The per-share owner-earnings series has
gone backwards for seven years.** **[E4-44]** bounds the gap: *"the value of an asset, whatever its
character, **cannot over the long term grow faster than its earnings do**"* — and *"The Tinker Bell approach
— clap if you believe — just won't cut it."* **[E4-35]** gives the base rate a 7–8% case would have to beat
on its way to justifying the quote: *"fewer than 10 of the 200 most profitable companies in 2000 will attain
15% annual growth in earnings-per-share over the next 20 years"* — 7–8% is not 15%, so the wager is not
absurd, but it must be carried **on a company that has delivered −0.56% per share for seven years**, and
that burden is not discharged by anything in the filings. **[E2-63] — state the ceiling too:** the upside
is bounded by the fact that **80.1% of the capital expenditure feeds the leg holding 24.3% of the capital
and 56.9% of the profit**, so growth in the good leg requires continuous reinvestment (the *good* savings
account, **[E4-20]**), while the two legs holding 75.7% of the capital would have to improve from 7.0% —
which is a re-rating of a purchase price, not earnings growth.

**3. WHAT YOU ARE PAID** — the return at this price, in points over the sovereign:
**−3.28 to −1.86 points on the default window; −2.56 to −2.24 at the central (c); −0.56 to +2.21 on the
company's own forward guidance.** On the framework's default window, **the buyer is paid less than the
30-year Treasury, with equity risk, for the privilege.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- sovereign used **5.34%** — **the bare rate, no per-name premium added.** *"If you say I'm going to stick
  an extra 6 percent in on the interest rate to allow for the fact — I tend to think that's kind of
  nonsense … It may look mathematical. But it's **mathematical gibberish**."*
- Certainty was handled **twice and neither place is the rate**: at the understanding gate (Q1, which
  passed) and, notionally, in the end margin — which is **not applied here, because no bar is armed below a
  closed gate.** **Windage count: 1** — conservatism is spent once, at the conservative end of the
  owner-earnings range **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — *"Using precise numbers is, in fact, foolish."*

| | capitalised value | per share | price |
|---|---|---|---|
| **at the ~10% floor [E4-28]** — the buying standard | $36,550M – $133,810M | **roughly $20 to $80** | **$102.67** |
| at the sovereign 5.34% — the yardstick at a base [E4-21] | $68,446M – $250,581M | roughly $40 to $145 | $102.67 |

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- **floor verdict: honest pre-tax expectancy 2.1% – 7.6% against ~10% → BELOW → quit on, and the lines
  below are NOT filled in.**
- points over sovereign, this name: *not filled in — the floor was not cleared.*
- against the rest of the opportunity set: *not filled in.* **[E2-74]**: between opportunities the money is
  parked, liquid and waiting, because *"Mr. Market will offer us opportunities — you can be sure of that."*

**WHICH BAR — stated for the record, armed for nothing.**
- [ ] **Normal method [E4-11]** — not used. No margin is applied below a closed gate.
- [x] **Screamer test [E4-01]**, run as an observation only. *"Occasionally … even very conservative
      estimates reveal that the price quoted is startlingly low in relation to value."* At the buying
      standard (~10%) **the price is ABOVE THE WHOLE RANGE** — outcome three of three, *"no"*. At the
      sovereign the price sits **INSIDE** the range, which is outcome two, *"no useful conclusion — move
      on"*. **Neither outcome is the rare case, and the governing one is the floor.**
      **[E3-65]** is the calibration: a real screamer was the Washington Post at *"about 20 percent of the
      value to a private owner … and a management with a lot of integrity and intelligence. That one was a
      real dream."* This is a price above the conservative range of a business whose owner earnings per share
      have fallen for seven years. **[E3-17]** adds the long-horizon half and it points the same way: *"If
      the business earns 6 percent on capital over 40 years … you're not going to make much different than a
      6 percent return, even if you originally buy it at a huge discount"* — and three quarters of this
      company's capital earns 7.0% pre-tax.

- **VERDICT: Q5 DID NOT OPEN.** *No Q5 verdict is recorded and no ranking position is assigned.
  The computation above is a below-gate computation and nothing else.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> ⚠️ **RECORDED, NOT GOVERNING — and there is nothing to sell.** Q6's function is to pre-commit an exit
> metric *before entry* **[E1-02]**; there is no entry. What follows is the **monitoring specification for a
> name that failed on the business**, written so that a future session can tell in one reading whether the
> ground has moved. **No band is armed in `tools/alerts.json` and no `PORTFOLIO.md` row is added** — a name
> that failed at Q2 failed on the BUSINESS, and a price alert on it would be a category error (the QLYS
> ruling, 2026-09-07).

**Pre-committed, before any entry [E1-02]:**
- **Thesis-confirming metric** *(would confirm the OUT)*: Sports segment operating income, and ESPN
  domestic affiliate and subscription fees. The FY2026 nine-month reading is **Sports OI −14% to $1,701M**;
  a second consecutive full year of decline, with the rate-rise offset no longer holding the fee line flat,
  confirms it.
- **THESIS-BREAKING METRIC AND ITS THRESHOLD — the one that would force a re-run from Q1:** **a filed
  separation, sale or spin of ESPN and/or the linear networks.** The threshold is a *document*, not a
  number: an 8-K, S-1 or Form 10 announcing it. Comcast did exactly this on 2026-01-02 (Versant), WBD tried
  it twice, and Disney has the same option. **If it is filed, the remaining security is Experiences plus
  Consumer Products plus a studio — 56.9% of today's segment operating income on 24.3% of today's capital,
  earning 28.9% pre-tax — and this framework would have to look at it again from Q1, because Q2 would very
  likely be IN.** *That is the single most important sentence in this file for any future session.*
  Secondary threshold: if Entertainment plus Sports return on their computed capital rises through 12%
  **[E5-40]** on three consecutive years without a separation, the Q2 reasoning weakens on its own terms.
- **Next catalyst dates:** FY2026 Q4 and full-year results, expected **early November 2026** (the FY2025
  10-K was filed 2025-11-13 and its earnings 8-K on 2025-11-13); the **2027 annual meeting** proxy in
  January 2027; **Iger's Transition Date, 2026-12-31**, after which D'Amaro is alone; the **securities
  class action trial, 2027-08-17**; and the **PSKY/WBD outside date of 2027-03-04 (extendable to
  2027-06-04)**, which settles what the largest competitor looks like.

**The sell rule [E2-28]** — recorded for completeness, applicable to nothing:
- SELL if the market judges it more valuable than the facts indicate — *at $102.67 the market judges it
  above the whole range at the buying standard; that is why it was not bought.*
- SELL if funds are needed for something more undervalued or better understood — *n/a.*
- HOLD while: return on equity capital satisfactory — **5.0% five-year mean, not satisfactory [E2-42]**;
  management competent and honest — **no disqualifier found, flags live**; market does not overvalue —
  **it does, at the floor.**
- *Price appreciation and holding period are explicitly rejected as reasons to sell. Not engaged here.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question — *"is
this erosion just part of an aberrational cycle … or has the business slipped in a way that permanently
reduces intrinsic business values?"* **Answered, for the two legs that closed the file: permanent, not
cyclical.** The pay-TV subscriber base is not coming back — Comcast domestic video fell from 18.176M to
11.270M between 2021 and 2025, a 38.0% fall, and WBD says *"Declines in linear subscribers are expected to
continue."* **For the Experiences leg the answer is the opposite: no erosion at all is visible**, and the
FY2026 nine-month reading (+10% operating income, *"roughly 6% volume and 3% rate"*) is the strongest in
the file. **[E5-45]**'s ABCs — arrogance, bureaucracy, complacency — are the slow third damage vector and
are a standing monitoring item; **[E3-40]**'s loss of focus fired across FY2019–23 and is now reversing
(80.1% of FY2025 capex into the base business, and the man who ran that business is now the CEO).

**Position size — a judgment, stated: NIL.** Q2 is OUT. **Do not trim winners [E5-14]** does not engage;
nothing is held. **[E3-45]**'s direction — capital to rank #1 — points elsewhere.

- **VERDICT: [x] OUT** *(recorded as the consequence of Q2, not as an independent finding)*

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → the file closed there.** Q3, Q4
      and Q6 are marked **RECORDED, NOT GOVERNING** in their own headers; **Q5 did not open** and its
      arithmetic carries the mandatory heading with no entry language (operator rule 3).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN is unqualified.
      Q4 IN is unqualified as to survival. **The word PROVISIONAL appears only inside Q2, attached to the
      *video* moat sub-class, and Q2's verdict is OUT — so no IN verdict rests on it.** *(This is the
      distinction the template's rule turns on and it is stated explicitly so no later reader has to
      reconstruct it.)*
- [x] Every UNRESEARCHED verdict names the artifact and where it lives — **there is no UNRESEARCHED gate
      verdict in this file.** One evidence-ladder gap is recorded inside Q2 (Oriental Land Co, TSE 4661;
      rung: EDINET Annual Securities Report / TDnet; not pulled; a licensee, not a competitor, so it gates
      nothing).
- [x] Every UNKNOWABLE verdict states what specifically cannot be known — **there is no UNKNOWABLE verdict
      in this file.** The two things that genuinely cannot be known are named where they bite: the
      maintenance/growth split of $8–9bn of annual capital expenditure (Q4), and whether ESPN's DTC ramp
      outruns the affiliate melt (Q4's likelihood judgment). Neither was needed to reach the verdict.
- [x] Step 0: the filing was read, with accession numbers (four filings plus the proxy and four 8-Ks), and
      a figure was cross-checked — cash-flow D&A $5,326M reconciled to depreciation $3,859M plus intangible
      amortisation $1,467M off the MD&A component tables, and separately to the XBRL tag.
- [x] Owner earnings on a multi-year mean; **six windows** stated, pandemic years shown both in and out and
      never silently dropped **[E4-25, E4-38]**; capex band disclosed as a judgment with the [E5-20]
      question asked on the filing and answered NO, with the peer-filed maintenance-to-depreciation ratio
      used to set the middle.
- [x] Competitor row filled — **eleven filings, ten peers across two rows** (parks: Comcast, Six Flags,
      United Parks; video: Netflix, Comcast/Peacock, WBD, Paramount Skydance, Sony, Amazon, Apple; sports
      rights: Fox, Comcast, WBD; distributors: Comcast, Charter, EchoStar). The video sub-class is marked
      PROVISIONAL because four of seven peers file no comparable streaming profit measure, and the reason
      it is not load-bearing is stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury daily par yield
      curve, 30 Yr), dated 2026-09-18, struck fresh for this run. **Not FRED.**
- [x] Value stated as a round-number range ($20–$80 at the floor; $40–$145 at the sovereign), not a point
      estimate.
- [x] One bar chosen, not both — the screamer test, run as an observation only below a closed gate.
      **Windage count: 1.**
- [x] Prices dated (close 2026-09-18); the aggregator is used for the live quote only and is flagged in
      Step 0 and again at Q5.
- [x] Run committed to git — five commits, each with a pathspec.
- [x] **Every ledger id cited was checked against `principle_ledger.csv` before use.** 176 ids checked,
      **0 missing**. [E4-27] is the incentives row and [E4-52] the lollapalooza row — the confusion the
      SONY run found on 2026-09-13 was not repeated.
- [x] **The two later addenda are dated and placed beside the sections they amend, not inside them**
      (operator rule 6), and the second one **corrects a statement in Q3** rather than editing it.

## REGISTER
- Verdict: [ ] IN · **[x] OUT (about the business)** · [ ] UNRESEARCHED · [ ] UNKNOWABLE
- **One line: Q1 IN / Q2 OUT — the clearest theme-park franchise on disk is bolted to $107.8bn of capital
  earning 7.0% and $84.1bn of signed sports rights; 43.1% of the profit and 75.7% of the capital fail
  [E3-03] criterion 2 and are excluded by [E4-04], and two distributors proved criterion 2 false in public
  in eleven months.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
- **The reversal condition, in words and not as a price band:** a filed separation, sale or spin of ESPN
  and/or the linear networks. What would remain is 56.9% of today's segment operating income on 24.3% of
  today's capital at a 28.9% pre-tax return, and **this framework would have to run it again from Q1.**

