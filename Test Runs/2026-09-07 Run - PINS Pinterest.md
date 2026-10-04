# Company Run — Pinterest, Inc. (PINS) — 2026-09-07
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
## STEP 0 — THE RATE, THE COVER, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority, struck this session via `tools/sources.py`; not the FRED fallback)**
- FX: none. Pinterest reports in USD. *(International revenue is a large share and is
  earned in local currencies but is reported and remitted in USD; the reporting currency
  is USD and the 30-yr Treasury is the right sovereign. Recorded, not waved away — the
  currency mix is examined at Q1 under the ARPU-by-geography series.)*

**STAGE 0 — THE COVER COUNT, BY HAND. THIS IS THE NAME THAT EXPOSED THE CAP DEFECT.**

*The addendum of 2026-09-02 found the screen pricing Pinterest on `dei:EntityCommonStock
SharesOutstanding` = 127,371,000 — the pre-IPO balance-sheet count of 2019-03-31, three
weeks before listing. The cap was 4.06x too small and the printed 4.98% yield was really
1.23%. The `cap_m 12017` in the brief is a HAND-READ override, not a computed figure, and
it is now itself five days stale. Both halves are re-struck below.*

**1. The count, re-read from the cover this session.** `python Screens/cover_shares.py PINS`:

    10-Q filed 2026-08-04, period 2026-06-30, accession 0001506293-26-000104
    Class A                        492,198,008
    Class B                         74,115,019
    --- arithmetic sum, NOT a share count ---   566,313,027
    MULTIPLE CLASSES. Whether these are economically equivalent is a JUDGMENT
    from the charter, not arithmetic. READ THE FILING.

**2. The judgment the tool refuses to make, made here from the charter description in the
filing.** The FY2025 10-K, Note 1, verbatim:

> *"We present net income (loss) per share using the two-class method required for multiple
> classes of common stock. **Holders of our Class A and Class B common stock have identical
> rights except with respect to voting, conversion and transfer rights and therefore share
> equally in our net income or losses.**"*

And the mechanism, from Item 1A: *"Our Class B common stock has **twenty votes per share**,
and our Class A common stock has one vote per share… Transfers by holders of Class B common
stock will **generally result in those shares converting to Class A common stock**… all
shares of Class B common stock will automatically convert into shares of Class A common
stock on (i) the **seven-year anniversary of the closing date of our IPO**, except with
respect to shares… held by any holder that continues to beneficially own at least 50% of
the number of shares… that such holder beneficially owned immediately prior to completion
of our IPO."*

**DECISION: the two classes ARE economically equivalent and summing them is correct.** Same
$0.00001 par, identical economic rights on the filing's own words, 1:1 conversion, and the
two-class EPS method returns the same figure for both. The difference is **votes, not
money** — Class B holds 73.2% of the voting power on 12.0% of the shares as of 2025-12-31,
which is a governance finding recorded at Q3, not a share-count adjustment. *(This is the
opposite outcome from CRWD's Stage 0, where the classes had already merged; here both
classes are live and the sum is still the right number.)*

**3. The price is re-struck; the brief's was five days old.**
- **price $20.40 · 2026-09-04 · aggregator, FLAGGED, live quote only** (operator rule 5).
  The brief's $21.22 of 2026-09-02 is 4.0% higher; using it would have understated the
  yield.
- **shares 566,313,027** (10-Q cover, as-of 2026-07-28, both classes, judged equivalent).
- **MARKET CAP = $20.40 × 566,313,027 = $11,553M**, against the brief's $12,017M.

**4. AND A THIRD COVER DATE MATTERS, BECAUSE THIS COMPANY IS RETIRING 17% OF ITSELF IN SIX
MONTHS.** The FY2025 10-K cover (as of **2026-02-06**) reads *"there were **585,458,698**
shares of the registrant's Class A common stock… outstanding, and **79,679,925** shares of
the registrant's Class B common stock outstanding"* — **665,138,623 together**. The
2026-07-28 cover is **566,313,027**. **The count fell 98.8 million shares — 14.9% — in
under six months.** Any cached share count on this name is wrong within a quarter, and the
direction is the reverse of the usual defect: a stale count now **overstates** the cap.
Full treatment at Q3 under **[E5-08]**.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2025 10-K, FYE 2025-12-31, filed 2026-02-12, accession
  `0001506293-26-000021`.**
- Vintages read in full for the disclosure-history and metric tests: FY2024
  `0001506293-25-000022`, FY2023 `0001506293-24-000018`, FY2022 `0001506293-23-000023`,
  FY2021 `0001506293-22-000016`, FY2020 `0001506293-21-000025`.
- **Two 10-Qs read, and they carry the newest and most damaging facts in the file:**
  Q2 2026 `0001506293-26-000104` (filed 2026-08-04) and Q1 2026 `0001506293-26-000068`.
- Two proxies read for Q3: DEF 14A 2026 `0001506293-26-000058`, DEF 14A 2025
  `0001506293-25-000084`.
- Two 8-K earnings releases read for the filed operating-metric tables, which the 10-K
  presents only as chart images: Q4/FY2025 `0001506293-26-000019` exhibit 99.1, and Q2 2026
  `0001506293-26-000102` exhibit 99.1.
- **Figure cross-checked against the filed statement:** XBRL returns FY2025 operating cash
  flow of $1,284,264k. The filed Consolidated Statements of Cash Flows shows **"Net cash
  provided by operating activities 1,284,264"** — agrees to the dollar. **Second
  cross-check, because SBC decides this run:** XBRL `ShareBasedCompensation` FY2025 =
  $880,463k; the filed cash-flow statement's adjustments block shows **"Share-based
  compensation 880,463"** and the Adjusted EBITDA reconciliation in Item 7 shows the same
  880,463 — agrees to the dollar in two independent places in the same document. **Third:**
  the filed investing section shows **"Purchases of property and equipment (32,375)"**
  against the XBRL capex of $32,375k — agrees to the dollar.

---
## THE SCREEN ROW — REPRODUCED EXACTLY, AND THREE OF THE BRIEF'S FOUR FLAGS ARE WRONG AS STATED

**The published row** (`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 199):

    PINS, cap_m 12,017 · oe_bottom_m 147 · oe_top_m 168 · spread 0.139 ·
    yield_bottom 0.0122 · vs_sovereign −0.0402 · growth_required 0.0878 ·
    level_shift 5.26 "STEP UP - normalize down [E4-41]" · best_year_dep 0.446 ·
    newest_filing 2025-12-31

Re-run against today's `companyfacts`, every figure reproduces:
`{'5y_da': 147.1, '5y_capex': 154.8, '3y_da': 166.6, '3y_capex': 167.6}`, level_shift
**5.259**, best_year_dep **0.4463**. **Unlike CRWD, HAS and CERT, the arithmetic here is
sound.** The defects are in what the numbers are being *said to mean*.

**DEFECT 1 IN THE BRIEF — `best_year_dep 0.446` IS NOT "the five-year mean moves 44.6% when
the best year is dropped". IT IS THE LEAVE-*TWO*-OUT ON A NINE-YEAR OPERATING-CASH SERIES.**
Read from `floor_screen.best_year_dependence` and `regen_queue` line 90, the series passed
in is `series = [ocf[y] for y in sorted(ocf)[-9:]]` — **operating cash flow, nine years, not
owner earnings and not five years.** The function returns the **pair** value `d2` whenever
the pair test fires, and it fired here:

| | value |
|---|---|
| 9-year OCF series ($M) | −102.9, −60.4, 0.7, 28.8, 752.9, 469.2, 613.0, 964.6, 1,284.3 |
| **d1 — drop the single best year (2025)** | **0.241** |
| **d2 — drop the best TWO (2025 and 2024)** | **0.446** ← the published figure |
| verdict string | *"TWO YEARS JOINTLY CARRY THE WINDOW"* |

The brief calls 0.446 "the highest on the current reading order and the main event" and
describes it as a single-year drop on a five-year mean. **It is a two-year drop on a
nine-year mean, and the single-year figure is 0.241.** The distinction matters because the
two are opposite diagnoses: a one-year spike says *normalize down*; a two-year step at the
end of a series says *the level may have changed*. **The [E4-41]/[E4-25] question the brief
asked is still the right question — plateau or one exceptional year — and it is answered
below with the half-year data the screen cannot see. But it is answered against a different
number than the brief named.**

**DEFECT 2 IN THE BRIEF, AND IT IS THE BRIEF'S BEST CALL — `level_shift 5.26` IS THE
SIGN-CHANGE CASE, AND THE GUARD ADDED 2026-09-07 DOES NOT CATCH IT.** The brief asked
whether this is the sign-change case. **It is, and the guard misses it for a structural
reason worth recording.** `level_shift` compares the mean of the last 3 years against the
mean of the earlier 6, and refuses a ratio when *the earlier mean* is at or below zero or
negligible against scale. Here:

| | |
|---|---|
| earlier six (2017–2022) | −102.9, −60.4, **0.7**, 28.8, **752.9**, 469.2 → **mean +$181.4M** |
| recent three (2023–2025) | 613.0, 964.6, 1,284.3 → mean $954.0M |
| ratio | **5.26**, printed with a confident verdict string |

**Three of the six "earlier" years are at or below zero and a fourth is $0.7M — a rounding
error on a series that averages $475M — yet the guard waves the row through, because the
single year 2021 ($752.9M) drags the six-year mean to +$181.4M.** The guard tests **the mean
of the early half**, and a mean is exactly the statistic that a sign change inside the early
half destroys. `earlier <= 0` and `0 < earlier < 0.05*scale` are both false, so the
undefined-across-zero condition the docstring exists to catch is present in the data and
absent from the test. **This is the DAL half-fix in a new shape: the guard reads the
aggregate where the defect lives in the components.** A guard that looked at
`min(early_half) < 0 < max(early_half)` would fire here. Recorded as a tooling defect, not
patched in this run *(operator rule 8: the flag is a prompt to read; I read it)*.

**The worded direction is the finding, and it is correct:** *the level HAS changed and the
multi-year mean is averaging two different businesses.* Pinterest before 2021 was a
pre-monetization company that consumed cash; Pinterest after 2021 is a company that
generates it. Any window reaching back past 2021 is not a range — it is two companies.

**DEFECT 3 IN THE BRIEF — THERE IS NO SEPARATELY-TAGGED CAPITALIZED SOFTWARE, AND THE
REASON IS A REAL FINDING ABOUT THE BUSINESS.** Recorded sweep of all six 10-K vintages for
"capitalized software" and "internal-use software": **one instance in six filings**, and it
is a reference to **ASU 2025-06, effective 2028** — a future standard, not a policy. The
filed PP&E note carries exactly three lines — *"Leasehold improvements $95,309 · Furniture
and fixtures 23,752 · Computer and network equipment 33,092 · Total property and equipment
152,153"* — **and no software line at all.** The investing section has exactly one capital
line, *"Purchases of property and equipment (32,375)"*, which the screen resolves correctly.
**The HAS/CRWD defect does not exist on this filer**, and the reason is that Pinterest
capitalizes none of its engineering: every dollar of it runs through R&D expense
($1,427.4M in FY2025, 33.8% of revenue) and every server it uses belongs to Amazon. **Total
gross PP&E of $152.2M against $4,221.8M of revenue** is the whole physical plant.

**DEFECT 4 — THE RAW D&A SERIES, PRINTED AS THE BRIEF REQUIRED, AND IT DOES HAVE A BREAK
THAT `da_discontinuity_flag` RETURNS `None` ON.**

| year | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| **D&A $M** | 16.1 | 20.9 | 27.8 | 37.0 | 27.5 | **46.5** | **21.5** | 21.3 | 25.2 |
| of which depreciation | 20.1 | 20.9 | 26.3 | 36.0 | 26.2 | 21.6 | 14.1 | 13.9 | 19.4 |
| of which intangible amortization | 0.7 | 1.5 | 1.0 | 1.3 | **24.9** | 7.4 | 7.4 | 5.8 | — |

**A 2.16x step down between 2022 and 2023, and the flag does not fire.** The cause is
readable and benign: the 2022 charge carries $24.9M of acquired-intangible amortization
from the 2021–22 acquisitions (Vochi, THE YES) against $1.3M the year before, and
depreciation itself fell as the company exited office space. **It is a real discontinuity
with a real explanation, which is the CERT lesson in its non-alarming form: a broken series
is not an empty one, and this one breaks for a reason the filing states.** It is immaterial
to the verdict here for a reason peculiar to this filer: **(c) is under 1% of operating
cash flow at either end**, so the capex band is 8 basis points of yield wide and cannot
change any answer. That is stated at Q4 rather than used as a licence.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** Pinterest runs a free
website and phone app on which people save pictures of things they want — a sofa, a haircut,
a lasagne, a wedding dress — into folders they label themselves. Nobody pays to use it.
Pinterest sells advertisers the right to slide a picture of their own product into that
stream of saved pictures, and charges when a user clicks it, or per thousand times it is
shown, or per day, or per video view. **Every dollar of the $4,221.8M of FY2025 revenue is
advertising. There is no subscription, no commission, no take rate, and no revenue from
users at all.**

**The money is made in one place, and the concentration is the fact to hold on to.** From
the filed operating-metric table in the Q4 2025 earnings release (8-K
`0001506293-26-000019`, exhibit 99.1):

| FY2025 | MAUs | share of users | revenue | share of revenue | **ARPU** |
|---|---|---|---|---|---|
| **U.S. and Canada** | **105M** | **17.0%** | **$3,173M** | **75.2%** | **$30.84** |
| Europe | 158M | 25.5% | $775M | 18.4% | $5.12 |
| Rest of World | 356M | 57.5% | $274M | 6.5% | $0.83 |
| Global | 619M | 100% | $4,222M | 100% | $7.21 |

**One user in six produces three dollars in four.** A U.S./Canadian user is worth **37
times** a Rest-of-World user. Anyone reading "619 million monthly active users, an all-time
high" as the business is reading the wrong number; the business is 105 million North
Americans and what an advertiser will pay to reach them.

**The cost side is two lines and one of them is not cash.** Cost of revenue was $841.5M
(gross margin **80.1%**) and consists mostly of what Amazon charges: *"Amazon Web Services
('AWS') provides the cloud computing infrastructure we use to host our website, mobile
application and many of the internal tools we use to operate our business. Under our
long-term agreement with AWS, in return for negotiated concessions, we currently are
required to maintain **a substantial majority of our monthly usage** … on AWS."* Pinterest
owns no data centres; **gross property and equipment is $152.2M** — leasehold improvements,
furniture, and laptops — against $4.2bn of revenue. Everything else is people:
**5,265 full-time employees**, against **$880.5M of share-based compensation**, which is
**$167,000 of stock per employee per year** on top of cash salary, and which equals
**68.6% of the entire operating cash flow of the business.**

**The scarce input this business controls.** Not the pictures — the pictures are uploaded by
users and by merchants, and cost nothing. Not the software, and not the AI, both of which
every peer has. **The scarce thing is a body of user-declared purchase intent recorded
before the purchase, attached to a name, in a place where the user is not annoyed to be sold
to.** A person who saves twelve images of grey sectional sofas has told an advertiser more,
and earlier, than any browsing signal can. That artifact — the board — is built by the user
over years and does not transfer. **Its scarcity is real and its measured value is
$30.84 a year in North America and 83 cents everywhere else**, and the whole investment
question is whether that gap is a runway or a verdict. **The honest read on which is at
Q2**, because it is a franchise question and not an understanding question.

**Will the fundamentals look broadly the same in ten years?** The *mechanism* — sell an
advertiser access to a person who has already said what they want to buy — is as old as the
classified page and I expect it to outlive me. **The delivery of it is another matter, and
the company says so itself in its own competition paragraph, which names the threat
explicitly:**

> *"We primarily compete with consumer internet companies that are either tools (search,
> ecommerce) or media (newsfeeds, video, social networks), particularly ones focused on
> advertising. Competitors such as **Amazon, Meta (including Facebook, Instagram, Threads and
> MetaAI), Google (including Gemini, Lens and YouTube), OpenAI (including ChatGPT), Snap,
> Reddit, TikTok and X**, many of which are **larger and have significantly greater financial
> and human resources**, offer users engaging content and commerce opportunities through
> similar…"*

That is the **[E3-31]** *"subject to constant change"* concern in a specific and datable
form: a company whose own filing names a large-language-model chatbot as a competitor for
the *first* time in the FY2025 vintage. **I record it here and adjudicate it at Q2**, which
is where the framework puts the substitution question **[E3-03](2)**.

**Q1 asks whether I can understand how the money is made, and I can — completely.** One
revenue line, one customer type, one geography that matters, one supplier, one cost that
dominates, and no financial engineering anywhere in the statements until January 2026.

- **VERDICT: [x] IN**
  *Recorded and carried forward: the [E3-31] constant-change clause is live and is decided
  at Q2, not waived here.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — by *users*, unambiguously: 640 million monthly, eleven
  consecutive quarters of double-digit growth. By *advertisers*, partially: it delivers a
  signal they want. The distinction between the two carries the whole gate, because the
  customer is the advertiser.
- **No close substitute [ ] — FAILS. The company's own filing lists the substitutes and
  its own balance sheet shows there is nothing holding the customer.**
- Not price-regulated **[x]** — no price regulation. *(Privacy law — GDPR, the DMA and DSA,
  state privacy statutes — constrains the targeting **input**, not the price. Recorded as an
  input risk at Q4, not as a criterion (3) failure.)*

### **[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. THEY EXIST HERE, PINTEREST FILES THEM, AND THE MONEY SEGMENT ONCE FELL 12% IN A YEAR.**

*"Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level — 'a
serious reverse, not likely to disappear in some bounce back effect.' Dollar revenue
flattered by pricing is how a shrinking franchise hides; the physical series is the honest
one."* — **[E4-55]**

**This is the test that could not be run at KLAC or QLYS. Pinterest files the physical
series, by geography, every quarter, and has never withdrawn it. Here it is, from the filed
8-K exhibit 99.1 tables (`0001506293-22-000013`, `-23-000021`, `-24-000017`, `-25-000020`,
`-26-000019`, `-26-000102`):**

**THE MONEY SEGMENT — 17% of users, 75% of revenue:**

| year-end | **MAU** | growth | revenue | growth | **ARPU** | growth | basis |
|---|---|---|---|---|---|---|---|
| 2020 | **98M** | +? | $1,425M | — | $15.34 | +27% | U.S. only |
| **2021** | **86M** | **−12%** | $2,016M | **+41%** | $21.98 | **+43%** | U.S. only |
| 2021 *(restated)* | 95M | — | $2,133M | — | $21.07 | — | U.S. **and Canada** |
| 2022 | 95M | **0%** | $2,309M | +8% | $24.38 | +16% | U.S. and Canada |
| 2023 | 97M | +2% | $2,448M | +6% | $25.52 | +5% | U.S. and Canada |
| 2024 | 101M | +4% | $2,884M | +18% | $29.15 | +14% | U.S. and Canada |
| 2025 | 105M | +4% | $3,173M | +10% | $30.84 | +6% | U.S. and Canada |
| **Q2 2026** | **106M** | **+4%** | $880M (qtr) | +18% | $8.30 (qtr) | +14% | U.S. and Canada |

**In 2021 the U.S. user count fell 12% — 98 million to 86 million — while U.S. revenue rose
41% and U.S. ARPU rose 43%. That is the Precision Steel shape exactly**, and it is the
single most informative year in the file: the moment the lockdowns ended, one North American
user in eight simply stopped coming, and the dollars were held up by price. The corpus's
words for that outcome are *"a serious reverse, not likely to disappear in some 'bounce
back' effect."*

**And on the honest arithmetic it has not fully bounced back, five years later.** The
geographic definition changed to "U.S. and Canada" in Q1 2022, which restated 2021 from 86M
to 95M — a Canadian increment of **9M**. Applying that same increment to the 2020 U.S. figure
of 98M puts **U.S.-and-Canada MAU at roughly 107M at the end of 2020, against the 105M
filed for the end of 2025.** *(Stated as arithmetic across two filed numbers on two bases,
explicitly not a filed figure — the company has never published a restated 2020.)* **The
money segment's physical series has been flat-to-down for five years and the entire dollar
growth in it has come from ARPU.**

**The other two segments, for completeness:**

| | 2021 | 2022 | 2023 | 2024 | 2025 | Q2 2026 |
|---|---|---|---|---|---|---|
| **Europe MAU** | 122M | 124M | 135M | 145M | **158M** | **157M** ← *down sequentially* |
| Europe ARPU | $3.03 | $3.23 | $3.73 | $4.24 | $5.12 (+21%) | $1.35/qtr (**+4%**) |
| Europe revenue growth | — | +4% | +21% | +23% | **+31%** | **+12%** |
| **Rest of World MAU** | 215M | 231M | 266M | 307M | 356M | 377M |
| RoW ARPU | $0.29 | $0.43 | $0.50 | $0.59 | $0.83 | $0.23/qtr |

**Europe was the growth story of 2025 and it decelerated hard in six months**: revenue growth
31% → 12%, ARPU growth 21% → 4%, and the user count went **down** from 158M to 157M. Rest of
World is 57.5% of the users and 6.5% of the revenue at 83 cents a head.

### **[E2-44] — BOTH HALVES, RUN DIRECTLY ON THE FILED SERIES. THIS IS THE TEST THE OPERATOR ASKED FOR.**

*Can it raise prices **"even when product demand is flat and capacity is not fully
utilized"**, and grow dollar volume **"with only minor additional investment of capital"**?*

**HALF TWO PASSES OUTRIGHT, AND IT IS THE BEST FACT IN THE FILE.** Capex was **$32.4M on
$4,221.8M of revenue — 0.77%**, second-lowest in the competitor row behind Reddit's 0.30%,
against Meta's 34.7% and Alphabet's 22.7%. Gross property and equipment is **$152.2M** in
total. D&A is 0.6% of revenue. Pinterest can double its dollar volume without buying
anything, because Amazon owns the machines. **This half is a genuine structural strength and
it is why Q4's staying-power test, had the run reached it, would have been short.**

**HALF ONE IS THE ONE THAT DECIDES, AND IT PASSES ON THE SURFACE AND FAILS ON
DECOMPOSITION.** On the surface: U.S.-and-Canada ARPU went from **$21.07 to $30.84 — +46% in
four years — on a user base up 10.5%.** Dollar revenue rising on a near-flat physical base is
the literal shape [E2-44](1) describes, and I am not going to pretend otherwise. **Three
things take it apart:**

1. **ARPU is not a price. It is revenue ÷ users, which is price × ad load.** A platform can
   raise ARPU 46% purely by showing more advertisements to the same person at the same
   price, and that has a hard ceiling the price does not. **The decomposition cannot be made
   from Pinterest's filings.** Recorded sweep of all six 10-K vintages for "ad impressions",
   "impressions delivered" and "ad load": **no instance found in any vintage.** **Meta files
   exactly this decomposition — "ad impressions delivered" and "average price per ad" as
   separate disclosed series — and Pinterest does not.** The one competitor whose disclosure
   would settle the question files it; the subject does not.
2. **The company says in its own words that the price is wrong**, which is a strange thing
   for a franchise to say seven years after listing. Bill Ready, Q4/FY2025 earnings release,
   2026-02-12: *"we're laser-focused on execution and **transforming our sales and
   go-to-market efforts so monetization better reflects the valuable commercial intent we
   see on Pinterest.** We're confident these important changes will make us a stronger
   company."*
3. **And the [E4-37] inverse metric returns the most extreme reading available.** *"you can
   almost measure the strength of a business over time by **the agony they go through in
   determining whether a price increase can be sustained**… it's not a great business when
   you have to have a prayer session before you raise your prices a penny."* From the Q2
   2026 10-Q: *"In January 2026, we initiated a global restructuring plan… (iii)
   **accelerating the transformation of our sales and go-to-market approach.** As part of
   the Restructuring Plan, we commenced a **workforce reduction of less than 15%** as well
   as office space reductions."* **$61.4M of restructuring charges in the first half of 2026
   and one employee in seven let go, in order to charge more for a product the company
   already sells.** That is not a prayer session. That is a reorganisation.

### **THE FACT THAT SETTLES [E3-03] CRITERION (2), AND IT IS ONE LINE OF THE BALANCE SHEET**

> *"Our total deferred revenue was **$47.5 million** and $23.4 million as of December 31,
> 2025 and 2024, respectively. **We expect materially all of our deferred revenue to be
> recognized in the subsequent quarter.**"* — FY2025 10-K, Note 1

**Deferred revenue is 1.1% of annual revenue and turns over in ninety days. There is no
contract, no minimum commitment, no lock-in, and no forward obligation of any kind on the
customer side.** Every dollar of Pinterest's revenue is re-won on a spot market every
quarter. *(For scale, the CRWD run measured the same line at CrowdStrike: **$4,753M of
deferred revenue against $4,812M of revenue — 99%**. Pinterest has 1.1%. These are not the
same kind of business and the difference is the entire question of whether a customer can
leave costlessly.)*

**And the customer's alternatives are named by Pinterest itself, under securities
liability:** *"Competitors such as Amazon, Meta…, Google…, OpenAI (including ChatGPT), Snap,
Reddit, TikTok and X, **many of which are larger and have significantly greater financial and
human resources**."* An advertiser moves budget from Pinterest to Meta by changing a number
in a dashboard. **[E3-03](2) asks whether the product is "thought by its customers to have no
close substitute." Pinterest's own filing lists eight, and its own balance sheet shows
nothing holds the customer for ninety days.**

### THE COMPETITOR ROW — required **[E3-28]**

*Full working, every accession number, the metric-history sweeps and the denominator
warning: `Test Runs/_research 2026-09-07 PINS/COMPETITOR_ROW.md`.*

**Peers named: 5 of the 8 competitors the company itself names, plus 1 adjacent (The Trade
Desk). THREE OF THE EIGHT ARE UNLISTED — TikTok/ByteDance, OpenAI and X — and cannot be put
in the row at all. Named as a hard limit, not patched.**

| FY2025, filing-sourced | **PINS** | META | GOOGL | SNAP | RDDT | *TTD* |
|---|---|---|---|---|---|---|
| Revenue | **$4,221.8M** | $200,966M | $402,836M | $5,931.4M | $2,202.5M | $2,896.3M |
| Revenue growth | +15.8% | +22.2% | +15.1% | +10.6% | **+69.4%** | +18.5% |
| **GAAP operating margin** | **7.6%** | **41.4%** | **32.0%** | (9.0)% | **20.1%** | 20.3% |
| **SBC ÷ operating cash flow** | **68.6%** | 17.6% | 15.1% | 154.9% | 49.7% | 49.4% |
| **Capex ÷ revenue** | **0.77%** | 34.7% | 22.7% | 3.7% | 0.30% | 6.8% |
| **Owner earnings (OCF−SBC−capex)** | **$371.4M** | $25,682M | $48,313M | $(579.6)M | **$341.0M** | $305.1M |
| Net cash (debt), FY-end | +$2,467.2M | +$22,848M | +$75,762M | $(596.3)M | +$2,476.8M | +$1,303.1M |
| **Names Pinterest in its own 10-K?** | — | **NO** | **NO** | **YES** | **YES** | NO |

**Amazon, the eighth named competitor, is built on its advertising line only: Advertising
services net sales $46,906M → $56,214M → $68,635M (FY2023–25). Amazon's advertising revenue
GREW BY $12.4bn IN 2025 — 2.9x Pinterest's entire business.**

**THE SHARPEST FACT IN THE ROW, AND IT IS REDDIT.** Reddit has been public for two years,
earns **52% of Pinterest's revenue**, and runs the same shape of business — advertising sold
against content its users make for free, near-zero capital, no data centres. **FY2025 owner
earnings: Reddit $341.0M against Pinterest's $371.4M.** Reddit earns **92% of Pinterest's
owner earnings on half the revenue**, at a **20.1% operating margin against 7.6%**, growing
revenue **69% against 16%**. If the commercial-intent asset were a franchise, it would show
up here, and it does not.

**THE [E2-45] ATTACKER'S TEST, RUN IN REVERSE, AND IT IS THE MIRROR IMAGE OF CROWDSTRIKE.**
At CrowdStrike every pure-play peer named CrowdStrike in its competition section under
securities liability and CrowdStrike named nobody — evidence *for* the moat. **Here it is
exactly reversed. Pinterest names eight competitors in its own filing. Meta names only
TikTok, Apple and Google — not Pinterest. Alphabet names Pinterest zero times. The Trade
Desk, zero times. The only two filers that name Pinterest are Snap and Reddit, the two
smaller than it.** Recorded sweeps, all FY2025 10-Ks. **The companies that set the price of
digital advertising do not consider Pinterest worth naming.**

**[E3-46] — "the best businesses, by definition, are going to be businesses that earn very
high returns on capital employed over time." STATED BOTH WAYS, BECAUSE THE TWO DENOMINATORS
DISAGREE AND THE DISAGREEMENT IS THE FINDING.** On **[E2-43]**'s unleveraged net tangible
operating assets, Pinterest earns **59.4%** pre-tax — total assets $5,492.1M less goodwill
and intangibles $106.3M, cash $969.3M, marketable securities $1,497.8M and deferred tax
assets $1,592.2M, less $788.3M of non-interest-bearing operating liabilities, leaves
**$538.2M**, against $319.9M of operating income. **That is a genuinely high number and it is
the strongest arithmetic in Pinterest's favour anywhere in this run.** But it is high because
the denominator is almost nothing, and on the metric that measures whether anything is being
*protected* — operating margin in an 80.1%-gross-margin industry — **Pinterest is fifth of
six at 7.6%.** A business earning 59% on $538M of capital and 7.6% on its revenue is not
being shielded from competition; it is being competed with, on a very small asset base.

### **[E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT? AND [E4-36] — WHICH CAUSE IS THIS?**

*The test: does a lapse in spending destroy the structure, or merely narrow it — and does
the spending defend the same advantage, or buy its replacement?* Pinterest spent
**$1,427.4M on R&D in FY2025 — 33.8% of revenue**, restructured in January 2026 to
*"reallocat[e] resources to AI-focused roles"*, and bought **tvScientific for $450.0M cash**
in December 2025 to enter connected-television advertising. **That is buying a replacement
adjacency, not defending a trademark.** The one thing that would survive a spending lapse is
the accumulated board data, which is real — but it is an asset that decays, because a
five-year-old set of saved sofas is a poor guide to what someone wants today.

**[E4-36]'s four causes: this is wave-riding [E3-51].** The wave is the migration of retail
and consumer-goods advertising budgets onto visual platforms. *"when a surfer gets up and
catches the wave and just stays there, he can go a long, long time. But if he gets off the
wave, he becomes mired in shallows."* **A surfing run is not a moat; the advantage lives in
the wave, not the surfer** — and by Pinterest's own count there are eight surfers on this
wave and it is fifth-largest of the six that can be measured.

### **[E3-33] / [E5-28] — UNTAPPED PRICING POWER? THE CLASS IS CLAIMED AND REFUSED.**

**This is the most attractive reading of Pinterest available and it deserves to be put
properly.** *"There are actually businesses that you will find a few times in a lifetime
where any manager could raise the return enormously just by raising prices, and yet they
haven't done it… That is the ultimate no-brainer."* **[E3-33]** Pinterest looks exactly like
that: the best commercial-intent data on the internet, monetised at $30.84 a year in its
home market, with a CEO saying out loud that monetisation does not reflect the intent.

**[E5-28] scopes the class and disqualifies it:** *"If you name some business that has
incredible pricing power, you're talking about a business that's **a monopoly or a near
monopoly**"* — **and claiming the class for a name is claiming near-monopoly, which the
competitor row must then support.** It does not. Pinterest holds **0.7% of the row's
combined revenue** and 2.1% of it excluding Alphabet's non-advertising businesses; it names
eight larger competitors in its own filing; three of those cannot even be measured. **The
low ARPU is not an untapped price. It is the market's clearing price for a substitutable
inventory**, and the evidence for that is that seven years of trying have not moved it and
the eighth year required firing one employee in seven.

- **Untapped pricing power [E3-33] / [E5-28]?** **No — the class is refused on [E5-28]'s own
  scope, because the competitor row does not support a near-monopoly claim.**
- Class: **NARROW at best, and NOT a franchise on [E3-03].** Direction on the **revenue**
  series is positive and accelerating; direction on the **economics** turned negative in the
  most recent half.
- **VERDICT: [x] OUT — on [E3-03] criterion (2), evidenced by the company's own competition
  paragraph and its own deferred-revenue line.**

### **WHY THIS IS NOT "WIDE", STATED AT FULL STRENGTH FIRST [E4-51, E4-26]**

*"I'm not entitled to have an opinion unless I can **state the arguments against my position
better than the people who are in opposition**."* **[E4-51]** Here is the bull case, put as
well as I can put it:

> Pinterest has **640 million monthly users, an all-time high**, growing double digits for
> **eleven consecutive quarters**. It has raised revenue per user **in every geography in
> every year it has ever filed**, without exception, including through a pandemic reversion,
> an Apple privacy change and an advertising recession. Gross margin is **80.1%**. Capital
> spending is **0.77% of revenue** — it owns no data centres and never will. Revenue growth
> is **accelerating**, from 9% in 2023 to 16% in 2025 to **18% in the latest quarter**. It
> earns **59.4% pre-tax on its unleveraged net tangible operating assets**. It holds a data
> asset that Meta, Google and TikTok structurally cannot synthesise, because their users do
> not sit down and build a labelled catalogue of what they intend to buy — Pinterest's do,
> voluntarily, for free, and have for fifteen years. In North America that user is monetised
> at $30.84 a year; Meta monetises a comparable Western user at several times that on a
> daily-active base. **That gap is the investment case: it is a runway, not a ceiling**, and
> [E3-33] says explicitly that a screen on realised returns *misses this class entirely* —
> *"any manager could raise the return enormously just by raising prices, and yet they
> haven't done it. That is the ultimate no-brainer."* Meanwhile the company is retiring
> **15% of its own shares in six months at $18.17**, below today's quote, and its stock
> compensation ratio has **fallen 37 points in two years**. And on the [E2-49] disclosure
> test it is clean: seven years of filings, **nothing ever withdrawn**, including the year
> it had to publish a 12% decline in its home-market user count.

**That case is real, several of its facts are the best in the whole reading queue, and I am
not discounting them. Here is why it does not carry Q2 anyway.**

**First, [E3-03](2) is not "users come back." It is that the *customer* thinks there is no
close substitute — and the customer is the advertiser, not the user.** Pinterest's own
filing names eight substitutes and calls most of them larger and better resourced. Its
deferred revenue is **1.1% of revenue and turns in ninety days.** There is no contract to
break. Whatever holds the *user* to Pinterest — and something does — **nothing whatever holds
the advertiser**, and the advertiser is who pays.

**Second, [E5-28] disposes of the untapped-pricing-power rescue by its own terms.** Claiming
that class is claiming near-monopoly. Pinterest is 0.7% of the measurable row and names
eight competitors. The class is not available.

**Third, [E4-37] converts the bull case's own best fact into evidence against.** The bull
case says the $30.84 is a runway. The company agrees it should be higher — and it has told
us what raising it costs: a global restructuring, a workforce reduction of one in seven, and
$61.4M of charges in six months, to *"transform the sales and go-to-market approach"* so
that *"monetization better reflects the valuable commercial intent."* **A business that must
rebuild its sales organisation to charge more is a business in agony over price. A franchise
raises the price and sends an invoice.**

**Fourth, [E4-55]'s physical series is the honest one and it fell.** U.S. users **98M → 86M,
−12%, in 2021**, while U.S. dollars rose 41% on price. Five years later the money segment's
user count is **105M against roughly 107M in 2020 on a consistent basis.** The dollars have
grown; the units have not.

**Fifth, the row settles it.** Reddit — half the revenue, two years public, no intent data at
all — earns **92% of Pinterest's owner earnings at 2.6x the operating margin**. Meta and
Alphabet do not name Pinterest in their filings. Amazon's advertising *growth* in one year
was 2.9x Pinterest's whole company.

**What would flip this verdict, named in advance so it is falsifiable:** a filed
decomposition of ARPU into impressions delivered and average price per ad, on Meta's
standard, showing **price per ad rising** over four consecutive quarters; **or** U.S.-and-
Canada ARPU above **$40** with U.S.-and-Canada MAU above **115M** in the same filed year,
which would be the runway converting; **or** a GAAP operating margin above **20%** — Reddit's
current level — sustained for four quarters. Any one of those is a document I can name, so
this verdict is reviewable. **But it is OUT and not UNRESEARCHED, because the documents that
exist have been read and they answer the question.**

**Q2 CLOSES THE FILE. Everything below this line is recorded because the operator's brief
asked for it and because a closed file still owes the register its findings. None of it is a
verdict, and per operator rule 2 none of it can promote the name.**

---

# TESTS RUN BELOW THE CLOSED GATE — RECORDED, NOT VERDICTS

## THE ONE NUMBER, AND THE OPERATOR'S PRIOR ON IT IS REFUTED **[E5-06, E3-70]**

> *"To say 'stock-based compensation' is not an expense is even more cavalier."* — **[E5-06]**

**SBC ÷ operating cash flow, Pinterest, every filed year. Both columns cross-checked to the
dollar against the filed cash-flow statements.**

| year | operating cash flow | stock compensation | **SBC ÷ OCF** |
|---|---|---|---|
| 2017 | $(102.9)M | $28.8M | n/m — OCF negative |
| 2018 | $(60.4)M | $14.9M | n/m — OCF negative |
| **2019** | **$0.7M** | **$1,377.8M** | **n/m — the IPO vesting catch-up** |
| 2020 | $28.8M | $321.0M | 1,113.6% |
| 2021 | $752.9M | $415.4M | 55.2% |
| 2022 | $469.2M | $497.1M | **106.0%** |
| 2023 | $613.0M | $647.9M | **105.7%** |
| 2024 | $964.6M | $765.8M | 79.4% |
| **2025** | **$1,284.3M** | **$880.5M** | **68.6%** |
| **H1 2026** | **$620.9M** | **$556.0M** | **89.5%** |
| TTM to 2026-06-30 | $1,333.8M | $1,021.8M | 76.6% |

**THE CRWD YARDSTICK, MEASURED — AND THE COMPARISON THE CRWD RUN DREW IS BACKWARDS.** The
CRWD run recorded: *"CrowdStrike is at 68.0% — the same place, to within half a point — and
it got there by rising in each of the last three years while **Pinterest's was a LEVEL**."*
**Pinterest's was not a level.** It was **106.0% → 105.7% → 79.4% → 68.6%** — a **37-point
improvement in two years**, the steepest fall of any name in the competitor row except
Reddit's IPO-distorted step. **The two companies arrive at the same ratio from opposite
directions, and on this metric alone Pinterest is the better story, not the matched one.**
*(The exact figure is **68.56%**, which rounds to 68.6%, not the 68.5% carried in the brief
and the CRWD run. Immaterial, corrected for the record.)*

**AND THE HALF-YEAR GIVES IT ALL BACK. H1 2026 SBC of $555,963k against operating cash flow
of $620,908k is 89.5%, against 72.6% in H1 2025.** Stock compensation rose **$141.3M** on
**$333.9M** of incremental revenue: **42 cents of every new revenue dollar went to
incremental stock compensation**, in the same six months in which the company cut *"less
than 15%"* of its workforce. Three years of improvement, reversed in two quarters.

**[E3-70] — the reported charge is the FLOOR of the subtraction, not the measure:** subtract
*"an amount equal to what the company could have realized by **publicly selling options of
like quantity and structure**."* Pinterest's awards are overwhelmingly RSUs, whose grant-date
fair value is the share price, so the charge is close to the market measure here. **But
$880.5M is still a floor for a different reason, and it is a candor point:**

> *"Shares repurchased for tax withholdings on release of restricted stock units and
> restricted stock awards — **(398,982)** / (390,254) / (335,019)"* — the FINANCING section
> of the filed cash-flow statement, FY2025/24/23

**$399.0M of real cash left the building in 2025 to pay employees' tax bills on their stock,
and it sits in FINANCING, below operating cash flow.** Cumulatively **$1,304.8M** across
FY2023–H1 2026. **Pinterest's own "free cash flow" measure — defined in its 10-K as
"net cash provided by operating activities less purchases of property and equipment" and
reported as $1,251.9M for FY2025 — does not deduct a cent of it.** The owner-earnings
construction here is unaffected (subtracting the full $880.5M SBC charge captures the whole
compensation, whichever section its cash half is filed in), but the company's headline cash
measure overstates by 32%.

---
## THE PLATEAU QUESTION — ANSWERED, AND THE ANSWER IS "NEITHER, AND IT IS WORSE THAN BOTH"

**The brief asked: is the recent level a new plateau, or one exceptional year carrying the
mean? [E4-41] and [E4-25].** The screen's `best_year_dep 0.446` said *two years jointly carry
a nine-year operating-cash window.* **The answer is available only from the half-year the
screen cannot see, and it is that the level has ALREADY fallen back.**

| | OCF | SBC | capex | **owner earnings** |
|---|---|---|---|---|
| H1 2025 | $571.4M | $414.7M | $18.3M | **$138.4M** |
| **H1 2026** | **$620.9M** | **$556.0M** | **$39.3M** | **$25.6M** |
| change | +8.7% | **+34.1%** | +115% | **−81.5%** |
| *revenue over the same six months* | | | | **+18.0%** |

**Owner earnings fell 81.5% on 18% revenue growth.** Adding back the entire $61.4M of H1
2026 restructuring charge — which **[E5-33]** says should *not* be added back (*"to tell
owners year after year, 'Don't count this' … is misleading"*), and which is shown here only
so the reader can see it makes no difference — still leaves **$87.0M against $138.4M, −37%.**

**So: FY2025's $371.4M is the single best year in the company's history, and the business has
already fallen below it.** TTM owner earnings through 2026-06-30 are **$258.6M**, down 30.4%
from the FY2025 figure. **[E4-41]'s instruction to normalise the mean DOWN for a favourable
year is correct here** — unlike at CrowdStrike, where the same flag pointed at the wrong end
of the series. **The verdict on the operator's question: it is not a plateau, and it is not
one exceptional year carrying an otherwise-flat mean. It is a rising series that peaked in
FY2025 and turned down in the first half of FY2026.**

---
## OWNER EARNINGS — EVERY WINDOW PUBLISHED **[E4-38]**, AND THE SPREAD CAVEAT IS LIVE FOR THE TENTH TIME

*OE = OCF − SBC − (c). All figures $M, from the filed cash-flow statements.*

| year | OCF | SBC | OCF − SBC | capex | D&A | **OE @ (c)=capex** | OE @ (c)=D&A |
|---|---|---|---|---|---|---|---|
| 2017 | (102.9) | 28.8 | (131.7) | 41.2 | 16.1 | (172.9) | (147.9) |
| 2018 | (60.4) | 14.9 | (75.2) | 22.2 | 20.9 | (97.4) | (96.1) |
| 2019 | 0.7 | 1,377.8 | (1,377.1) | 33.8 | 27.8 | **(1,410.9)** | (1,404.9) |
| 2020 | 28.8 | 321.0 | (292.2) | 17.4 | 37.0 | (309.6) | (329.2) |
| 2021 | 752.9 | 415.4 | 337.5 | 9.0 | 27.5 | 328.5 | 310.0 |
| 2022 | 469.2 | 497.1 | (27.9) | 29.0 | 46.5 | (56.9) | (74.4) |
| 2023 | 613.0 | 647.9 | (34.9) | 8.1 | 21.5 | (43.0) | (56.4) |
| 2024 | 964.6 | 765.8 | 198.8 | 24.6 | 21.3 | 174.2 | 177.5 |
| **2025** | **1,284.3** | **880.5** | **403.8** | 32.4 | 25.2 | **371.4** | **378.7** |
| **TTM 2026-06** | **1,333.8** | **1,021.8** | **312.0** | 53.4 | 33.9 | **258.6** | **278.1** |

**SEVEN WINDOWS, BOTH (c) ENDS — the brief asked for six:**

| window | (c) = capex | (c) = D&A |
|---|---|---|
| 3y (2023–25) | **$167.6M** ← the published `oe_top` | $166.6M |
| 4y (2022–25) | $111.4M | **$106.3M** |
| 5y (2021–25) | $154.8M | **$147.1M** ← the published `oe_bottom` |
| 6y (2020–25) | $77.4M | $67.7M |
| 7y (2019–25) | **$(135.2)M** | **$(142.7)M** |
| 8y (2018–25) | $(130.5)M | $(136.8)M |
| 9y (2017–25) | $(135.2)M | $(138.1)M |

**THE PUBLISHED 13.9% IS FOUR CONSTRUCTIONS OUT OF FOURTEEN, AND THE TRUE RANGE CROSSES
ZERO.** This is the DAL shape, and it is the tenth consecutive run to find the true width
larger than published. Stated three ways, because the honest answer depends on which company
you think you are pricing:

| basis | range | width |
|---|---|---|
| **published** (3y/5y × two ends) | $147.1M – $167.6M | **13.9%** |
| post-monetization only (3y/4y/5y × two ends) | $106.3M – $167.6M | **58%** |
| back to 2020 (3y–6y × two ends) | $67.7M – $167.6M | **148%** |
| **all nine years** | **$(142.7)M – $167.6M** | **CROSSES ZERO — not a ratio** |

**The capex band is the one part of the range that is genuinely narrow, and for a real
reason.** (c) at the D&A end is $25.2M and at the total-capex end $32.4M — a **$7.2M**
difference on a $1,284.3M operating cash flow, **0.6%**. Which case is this under
**[E3-44]/[E2-41]/[E5-20]**? **Neither exception applies.** Pinterest is the opposite of the
railroad: it owns no productive plant, capitalizes no software (recorded sweep, six vintages
— see the screen-row section), and rents its entire computing capacity from Amazon. Capex has
exceeded D&A in two of the last four years and trailed it in two. **The corpus default holds
and the band is 8 basis points of yield wide. Every ounce of the width in this file is
window spread, not capex judgment** — the exact inverse of the CRWD finding, where the
published spread was a window spread wearing a capex band's clothes and the capex end was
understated by an omitted software line.

**And a wide spread is a Q4 finding in its own right [E5-11], scoped by [E3-55].** The
distorting years are named: **2019's $1,377.8M of IPO share-based compensation** (a
once-per-company-lifetime vesting catch-up, not a recurring charge) and **2020's pandemic
demand pull-forward followed by 2021's 12% U.S. user reversal.** This is *not* [E3-55]'s
benign case — *"If we have a business about which we're extremely confident as to the
business result, we would prefer that it have high volatility"* — because the uncertainty
here is about the **level**, not the year-to-year bounce around a known level. See's loses
money eight months a year around a certain annual result; Pinterest's owner earnings went
from $(43.0)M to $371.4M to a $258.6M trailing figure in three years, and nobody including
management can say where the level is.

---
## THE BUYBACK — [E5-08], AND THE OPERATOR'S PRIOR IS REFUTED IN THE OTHER DIRECTION

**The brief asked for the change in DILUTED SHARE COUNT over the full history, not the
dollars, and for a plain statement of which this is: a return of capital, or payroll settled
in cash. Here is the full count, from the filed statements of stockholders' equity.**

| | shares outstanding | repurchased (shares) | repurchased ($) | issued (RSU + options + charity) |
|---|---|---|---|---|
| 2022-12-31 | **683,202k** | — | — | — |
| 2023 | 678,018k | 21,216k | $500.0M | 16,032k |
| 2024 | 675,933k | 19,125k | $600.2M | 17,040k |
| 2025 | 664,546k | 30,108k | $930.3M | 18,721k |
| **H1 2026** | **565,497k** | **111,412k** | **$2,039.8M** | 12,363k |
| **cumulative** | **−117,705k (−17.2%)** | **181,861k** | **$4,070.3M** | **64,156k** |

**THE ANSWER IS UNAMBIGUOUS AND IT IS THE OPPOSITE OF THE CRM RULING. Pinterest repurchased
181.9 million shares against 64.2 million issued — 2.83 times the issuance — and retired
17.2% of the company in three and a half years.** Under **[E5-08]** and the CRM ruling of
2026-09-07, a buyback that only offsets SBC dilution is payroll settled in cash and not a
return of capital. **This one is not that.** It offsets the dilution entirely and then
retires a further 117.7 million shares. **On the count — which is the test the brief
correctly insisted on — this is a genuine return of capital.** *(Contrast CrowdStrike, where
$226.2M of buyback offset 20.6% of a single year's issuance.)*

**But the two conditions are not both met, and the second one fails on my own arithmetic.**

**Condition (1) — ample funds for operations and liquidity [E5-08]. It was met and then it
was spent.** At 2025-12-31 Pinterest held **$969.3M of cash plus $1,497.8M of marketable
securities = $2,467.2M, against zero debt.** At 2026-06-30 it holds **$422.5M plus $852.4M =
$1,274.9M, against $981.1M of convertible notes — net cash of $293.8M, 2.5% of the market
cap.** In six months it spent $2,024.9M on buybacks and $447.0M on an acquisition, and
**borrowed $1bn to do it.** **THIS IS A DEFECT IN THE OPERATOR'S BRIEF AND IT IS THE
MATERIAL ONE:** the instruction to *"credit the large net cash position explicitly in the
valuation as AMAT's run did"* describes a balance sheet that ceased to exist in March 2026.
The credit is $293.8M, not $2.5bn, and it moves the yield by **8 basis points**.

**Condition (2) — repurchases at a material discount to conservatively calculated intrinsic
value. THIS FAILS ON MY OWN RANGE, AND THE FLAG IS RAISED WITH THE HUMILITY CLAUSE.**
Cumulative average price paid: **$4,070.3M ÷ 181,861k = $22.38 per share.** The 2026
repurchases averaged **$18.17** (company's own disclosure, Q2 2026 release: *"Completed over
$2 billion of share repurchases year-to-date at an average price of $18.17"*). Against the
value range computed below — **$4 to $6 per share on the sovereign, $2 to $3.50 on the
[E4-28] floor** — **every share bought back since 2023 was bought above my conservative
value and above my optimistic one.** The cumulative buyback is also **under water against the
market**: $22.38 paid against a $20.40 quote today.

> *"it is natural for CEOs to be optimistic about their own businesses. **They also know a
> whole lot more about them than I do.**"* — **[E4-13]**; *"infractions, even serious ones,
> are innocent; many CEOs never stop believing their stock is cheap"* — **[E5-08]**

**This rests entirely on my own IV range and management knows this business better than I
do. The flag binds position size, never the discount rate — and since the gate is closed
there is no position to bind.** Recorded as a **CAPITAL ALLOCATION FLAG**.

**[E4-50] and the borrowing.** *Munger's wiser board buys "very aggressively, using up all
cash on hand and also borrowing funds" — **the discount does the licensing, never the
borrowing**.* Pinterest did exactly what [E4-50] describes: used the cash and borrowed. **The
licence for it is a true discount, and my range does not find one.** The borrowing itself is
cheap and well-structured — 1.75%, due 2031, conversion price $22.72, with $99.2M of capped
calls bought to push the effective dilution point higher — and I record that it is
competently done. **[E5-24]** governs: *"what is smart at one price is dumb at another."*

**AND THE COUNTERPARTY IS THE STORY [E2-30], and it must be recorded plainly.** From Note 12
of the Q2 2026 10-Q, verbatim:

> *"In March 2026, we entered into the Investment Agreement with **Elliott** and issued
> **$1,000.0 million** in aggregate principal amount of the Notes **to Elliott**. **Marc
> Steinberg is a Partner at Elliott Investment Management L.P. and remains on our board of
> directors pursuant to the Investment Agreement.**"*

**The $1bn of debt that funded the buyback was sold to an activist investor who holds a board
seat contractually secured by the same agreement.** Steinberg has been a director since the
2023 annual meeting. This is a **related-party financing**, disclosed as one, on the face of
the balance sheet with a footnote marker. **It is not a [E5-16] honesty matter — it is
disclosed exactly as it should be, and the candor is a point in management's favour.** But
under **[E2-30]** — *"institutional dynamics, not venality or stupidity"* — the shape is
worth naming: **an activist on the board, a $1bn note from that activist, $2bn of buybacks in
six months at prices above any conservative value, a 15% workforce reduction, and a sales
reorganisation, all inside two quarters.** Behaviour (1) of the imperative — *"an institution
will resist any change in its current direction"* — **does not fire; the reverse fires.**

---
## Q3 ITEMS — NO VERDICT IS WRITTEN, THE GATE IS CLOSED **[E2-01, E4-22, E4-29, E2-49, E4-30]**

**WEIGHT CASE, declared as the template requires.** Daily execution **[ ]** — not ticked. The
product is a consumer website; a bad week does not destroy it, and the 2021 12% user decline
was survived. Control **[ ]** — not ticked, marketable security. Leverage **[ ]** — not
ticked at FY2025 (zero debt); **now marginal**, with $981.1M of converts against $1,274.9M of
liquid assets. **None ticked → Q3 would be a qualitative OVERLAY, not a binary gate**, and
manager quality alone could not have stopped this run. **It did not need to; Q2 stopped it.**

**[E2-01] THE PRIMARY TEST — the multi-year series, run, on both denominators, because they
disagree and the disagreement is the finding.**

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| net income | $316.4M | $(96.0)M | $(35.6)M | **$1,862.1M** | $416.9M |
| average equity | $2,640.6M | $3,160.2M | $3,186.2M | $3,920.9M | $4,748.2M |
| **return on equity** | **12.0%** | **(3.0)%** | **(1.1)%** | **47.5%** | **8.8%** |

**The 2024 figure is not a return; it is a one-time non-cash accounting event.** The FY2025
10-K: *"we released the **valuation allowance** on our U.S. federal and state, excluding
California, deferred tax assets **during the fourth quarter of 2024**."* The line
*"Provision for (benefit from) income taxes"* reads **$(1,574,501)k** for 2024 against pretax
income of $287,605k. **Stripping it, 2024's ROE on a notional tax rate is about 5.8%, and the
five-year series reads 12.0% / (3.0)% / (1.1)% / ~5.8% / 8.8% — a mean of roughly 4.5%.**
**[E2-42]:** *"Red lights should start flashing if the five-year average annual gain falls
much below the return on equity earned over the period by American industry in aggregate."*
It does.

**[E2-43] scopes the denominator and rescues it, and both readings must stand.** Book equity
here is 52% cash, securities and a deferred tax asset. On **unleveraged net tangible
operating assets — $538.2M — the pre-tax return is 59.4%.** *(Working at Q2.)* **The honest
statement is that Pinterest earns a very high return on a very small amount of capital and a
poor return on the capital it actually holds, because most of what it holds is not employed
in the business.**

**[E4-29] — EBITDA PROMOTION. THE FIFTH FLAG FIRES, AND IT FIRES IN THREE PLACES.**
*"Trumpeting EBITDA … is a particularly pernicious practice. Doing so implies that
depreciation is not truly an expense, given that it is a 'non-cash' charge. **That's
nonsense.**"* — **[E4-29]**

1. **In the 10-K itself.** Recorded sweep: **15 occurrences of "Adjusted EBITDA" in the
   FY2025 10-K**, with a full reconciliation in Item 7. Pinterest's definition excludes
   **both** D&A **and** share-based compensation. *(For contrast, the CRWD run's sweep found
   **zero** occurrences of "EBITDA" in three CrowdStrike 10-Ks.)*
2. **In the guidance.** Every quarterly release guides to Adjusted EBITDA and **explicitly
   refuses the GAAP reconciliation**: *"We have not provided the forward-looking GAAP
   equivalent … as a result of the uncertainty regarding, and the potential variability of,
   reconciling items such as **share-based compensation expense** and income taxes."* The
   single largest expense in the business is guided around by naming it as the reason a
   reconciliation is impossible.
3. **In the pay plan, which is where it does damage.** From the 2026 proxy's Item 402(v)
   table: **"Most Important Financial Performance Measures: Revenue · Adjusted EBITDA ·
   Relative TSR."** **Three measures, no GAAP measure, no return-on-capital measure, no
   per-share measure.** [E2-01] asks for *"a high earnings rate on equity capital employed …
   and not the achievement of consistent gains in earnings per share"*; Pinterest's own
   scorecard contains neither, and one of its three is the measure [E4-29] calls nonsense.

**PAY VERSUS PERFORMANCE, from the Item 402(v) table, 2026 proxy, as filed:**

| FY | **PINS TSR ($100)** | **Peer group TSR ($100)** | GAAP net income |
|---|---|---|---|
| 2021 | 55 | 95 | $316,438k |
| 2022 | 37 | 50 | $(96,047)k |
| 2023 | 56 | 80 | $(35,610)k |
| 2024 | 44 | 104 | $1,862,106k |
| **2025** | **39** | **120** | $416,855k |

**$100 invested in Pinterest at the start of 2021 is $39. In the company's own chosen peer
group it is $120. Pinterest underperformed in every one of the five years the table shows,
and the gap is now 3.1x.** *(Recorded as a filed fact about the security, not as a business
finding — [E5-29]: volatility is not risk, and price is not the business. It is here because
it is the company's own scorecard and because **[E3-50]** makes Relative TSR — a named pay
measure — the company's business.)*

**[E2-49] METRIC-SWITCHING — DOES NOT FIRE. THE PREDICTION FAILS FOR THE FOURTH TIME
RUNNING, AND THE COUNTER-EVIDENCE IS STRONGER THAN A SIMPLE ABSENCE.** Recorded sweep of all
six 10-K vintages (full table in `COMPETITOR_ROW.md`): **MAU, ARPU, MAU-by-geography,
ARPU-by-geography and the WAU/MAU ratio appear in every vintage from FY2020 to FY2025.
Nothing has ever been withdrawn.** The only two changes both **added** disclosure — the
geographic split went from two buckets to three in Q1 2022, and free cash flow was
introduced in FY2024. **And the test case is the FY2021 disclosure: the year U.S. MAU fell
12%, Pinterest published the number, on the face of the earnings release, with the decline
in the growth column, and then kept publishing it every quarter for the next five years.**
[E2-49] demands *"pre-set, long-lived and small bullseyes"*; these are the most pre-set and
long-lived in the reading queue. **This is the strongest single point in management's favour
anywhere in the file and it is recorded as one.** *(Control: Snap's FY2020–FY2025 10-Ks were
swept the same way — DAU and ARPU by geography in all six. No withdrawal there either.
Metric withdrawal is an enterprise-software habit, not an advertising-platform one.)*

**[E4-30] — THE CASH-TAX TELL. FIRES ARITHMETICALLY, AND THE EXPLANATION IS DISCLOSED AND
BENIGN — BUT IT IS AN OWNER-EARNINGS PROBLEM, NOT AN HONESTY PROBLEM.**

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| cash paid for income taxes, net | $19,173k | $25,018k | $22,376k |
| pretax income | $(16,440)k | $287,605k | $445,890k |
| **cash tax ÷ pretax** | n/m | **8.7%** | **5.0%** |

*"cash taxes falling as a share of reported pretax income"* **[E4-30]**. The cause is stated
in the filing and is not a manipulation: **federal net operating loss carryforwards of
$2,160.6 million, which "do not expire", plus $554.3M California and $956.4M other state.**
**[E5-38]** governs the reading: a fired flag is not a venality finding. **But the flag has a
second life at Q4 that matters more than its Q3 one: Pinterest's operating cash flow is
currently shielded by a finite asset.** The $1,592.2M deferred tax asset *is* that shield,
measured. When it is exhausted, cash taxes normalise toward the statutory rate and operating
cash flow falls by roughly a fifth of pretax income. **Every owner-earnings figure in this
run is struck at a ~5% cash tax rate and is not repeatable at a 21% one.**

**[E4-22] weak accounting — no live item found.** No restatement, no material weakness, no
auditor change, no immaterial-error correction of the kind CrowdStrike disclosed. **[E2-52]
dividends funded by issuance — does not fire; no dividend.** **[E5-15] serial share issuance
— does not fire; the count is down 17.2%.** **[E2-57] "except for" — does not fire.**
**[E3-53] restructuring charges — one live plan** ($61.4M in H1 2026, plus a November 2024
program), and per **[E5-33]** those charges stay in the owner-earnings mean and are not
annualized away. They are.

**[E5-16] THE HONESTY BINARY — recorded sweep, no disqualifier found.** No SEC or DOJ
inquiry, no securities enforcement matter, no personal-misconduct item in any of the six
10-K vintages or the two proxies read. *(Compare CrowdStrike, where a DOJ and SEC information
request on revenue recognition and ARR sits in the FY2026 10-K.)* Litigation is ordinary-
course intellectual property. **Per [E5-17] this is the absence of found disqualifiers, not a
finding that the managers are honest.**

**THE GUARDRAIL, checked before nothing was written.** Nothing in this Q3 is being used to
promote the name; the gate closed at Q2 and no Q3 finding can reopen it **[E2-37, E2-38,
E3-39]**. **Key-person dependence is recorded at Q2, not here:** the Class B holders control
**73.2% of the voting power on 12.0% of the shares**, and *"Despite no longer being employed
by us, Paul Sciarra and Benjamin Silbermann, two of our co-founders, remain able to exercise
significant voting power."* Two people who do not work at the company can outvote everyone
who owns it. **That is a governance structure, recorded, and under [E4-23] it belongs at Q2
as a moat/ownership defect rather than here as a Q3 strength or weakness.**

---
## Q4 ITEMS — RECORDED **[E5-11, E4-20, E2-54, E3-52, E2-27]**

**GREAT, GOOD, OR GRUESOME? [E4-20]** — **GOOD, and only just, and moving toward gruesome on
the most recent half.** It is not gruesome: gruesome *"grows rapidly, requires significant
capital to engender the growth, and then earns little or no money"*, and Pinterest requires
**no** capital to grow (0.77% of revenue). **[E4-43]** insists the *good* class passes and is
not to be over-read down. But the good class *"pays an attractive rate of interest that will
be earned also on deposits that are added"*, and Pinterest's incremental return on the
capital it retains is the problem: **it retained $4,070.3M and spent it buying its own shares
at $22.38 against a $20.40 quote.** Great is unavailable: **[E4-20]**'s great account *"pays
an extraordinarily high interest rate that will rise as the years pass"*, and owner earnings
fell 81.5% in the latest half.

**STAYING POWER — all three scored [E5-11].**
1. **Large and reliable stream of earnings — PARTIAL.** Large: $1,284.3M of operating cash
   flow. **Reliable: no.** Owner earnings by year: $(43.0)M, $174.2M, $371.4M, and a trailing
   $258.6M. The stream is four years old and has never been stable.
2. **Massive liquid assets — WAS YES, IS NOW MODEST.** $2,467.2M net cash at 2025-12-31;
   **$293.8M net cash at 2026-06-30** after $2.02bn of buybacks, a $447.0M acquisition and a
   $1bn borrowing. **[E5-39]:** *"cash is a lot like oxygen: you don't notice it 99.9 percent
   of the time. But if it's absent, it's the only thing you notice."* Pinterest has just
   converted eight years of accumulated oxygen into retired shares in two quarters.
3. **NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — the one that usually kills, and here it
   PASSES, which is the best structural fact in the file.** The FY2025 10-K's own statement
   of material cash requirements: *"our **$312.3 million** commitment with Amazon Web
   Services, **for which we are not subject to annual purchase commitments**, and our
   **$323.5 million** of operating lease obligations, of which **$50.0 million** is due
   within the next 12 months"*, plus the $450.0M tvScientific payment (since made). **The
   converts are 1.75% and due 2031 — five years out, no covenants disclosed, and
   [E2-54]'s coverage test is passed by an order of magnitude: $17.5M of annual interest
   against $1,333.8M of trailing operating cash flow.** [E3-52] scoping: this is
   long-dated, cheap, uncovenanted paper, not bank debt due next year.

**LEVERAGE, named and quantified [E4-16, E3-29].** $981.1M of convertible notes against
$1,274.9M of liquid assets and $4,759.4M of total assets — **20.6% of assets, net negative.**
There is no ratio ceiling in this framework and the corpus supplies none. The honest
statement: **Pinterest went from a debt-free balance sheet to a modestly levered one in one
quarter, by choice, to buy back stock.**

**NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40] — and model exposure, not
experience.**

**The mechanism: the intent query moves to a chat interface, and Pinterest is a destination
that must be visited.** Pinterest's FY2025 10-K is the first vintage to name **OpenAI
(including ChatGPT)** and **MetaAI** and **Gemini** as competitors. The whole business rests
on a person choosing to open the Pinterest app to browse for a sofa. If that person instead
types "show me grey sectional sofas under $2,000 that fit a small room" into a chat box, the
intent — the scarce input identified at Q1 — is expressed somewhere Pinterest does not own,
and the board that took years to build is not consulted. **Pinterest has no distribution it
controls: no operating system, no browser, no search box, no messaging app, no device.** Its
competitors named in its own filing own all five.

**Quantified from filed figures.** 75.2% of revenue comes from 105 million North American
users whose count has grown 2.5% a year for four years and, on the consistent-basis
arithmetic at Q2, is roughly where it was in 2020. **A repeat of the 2021 experience — a 12%
decline in the money segment's user count — applied to FY2025 would remove about $381M of
revenue.** Against FY2025 operating income of $319.9M and an 80.1% gross margin, roughly
$305M of that is contribution: **a single repeat of an event this business has already
lived through once takes operating income from +$319.9M to roughly +$15M, and the trailing
owner-earnings figure to approximately zero.** **[E4-40]:** model exposure, not experience —
and here the experience is the exposure, because it has already happened once.

**Likelihood: a real possibility.** Not *likely*: the user count is at an all-time high and
growing 11%, revenue growth is accelerating, and the chat-interface substitution is a thesis
rather than a measured fact. Not a *low-level possibility* either: the company itself put
three AI chat products into its competition paragraph this year, and the one segment that
pays has been flat for five years.

**The bear case a holder would accept as fairly stated [E4-51]:** *Pinterest's users are
loyal, its data is unique, and its monetization gap is the largest identified opportunity in
consumer internet. The 2021 decline was a pandemic reversion, not a franchise failure — every
consumer platform gave back lockdown gains that year. The H1 2026 collapse in owner earnings
is a deliberate, disclosed investment: a sales reorganisation and an AI pivot, taken with
revenue accelerating to 18%, funded by a cheap 1.75% convertible and accompanied by the
retirement of 15% of the shares below intrinsic value. Judging a transformation year on its
transformation costs is exactly the [E5-33] error in reverse.* **That case is coherent and I
would not call a holder unreasonable for holding it. It is a bet on execution, and the
framework's answer to a bet on execution is [E4-23] and [E2-37]: a business that requires a
transformation to earn its price is a business whose economics do not currently earn it.**

---
## Q5 — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

⛔ **Q5 did not open. Q2 returned OUT.** Everything in this section is arithmetic produced
below a closed gate, it carries **no entry language of any kind**, and under operator rule 2
it cannot promote the name. It is written because the brief asked for the price, the pass/fail
and the value band.

**THE INPUTS.** Market cap **$11,553M** ($20.40 × 566,313,027, 2026-09-04, aggregator quote
flagged). Sovereign **5.24%**, US Treasury 30-year, 2026-09-04, issuing authority. Net cash
credit **$293.8M** (2026-06-30: $422.5M cash + $852.4M marketable securities − $981.1M
convertible notes) → **enterprise value $11,259M**. *(The $1,616.4M deferred tax asset is
real and is NOT credited: it is not distributable, it is contingent on earning the income it
shelters, and [E3-71]'s treatment of the mirror-image item — a deferred tax **liability** as
an interest-free loan, "never at face, never at zero" — argues for a discount, not a credit
at face. Its effect is already inside the ~5% cash tax rate in the owner-earnings series,
where crediting it again would double-count.)*

**1. THE YIELD, at every construction in the range, beside the bond:**

| construction | owner earnings | **yield** | **vs sovereign** | perpetual growth to reach the 10% floor |
|---|---|---|---|---|
| 6y D&A end (incl. 2020) | $67.7M | 0.59% | **−4.65 pts** | 9.41% |
| **4y D&A end — the bottom boundary [E5-34]** | **$106.3M** | **0.92%** | **−4.32 pts** | **9.08%** |
| 5y D&A end — the published `oe_bottom` | $147.1M | 1.27% | −3.97 pts | 8.73% |
| 3y capex end — the published `oe_top` | $167.6M | 1.45% | −3.79 pts | 8.55% |
| **TTM to 2026-06-30** | **$258.6M** | **2.24%** | **−3.00 pts** | 7.76% |
| **FY2025 alone — the best year ever filed** | **$371.4M** | **3.21%** | **−2.03 pts** | 6.79% |

**THE SINGLE BEST YEAR IN THE COMPANY'S HISTORY YIELDS 3.21% AGAINST A 5.24% GOVERNMENT
BOND. There is no construction of Pinterest's owner earnings, on any window, at either end of
the capex band, that reaches the sovereign.** *(The published row's `yield_bottom 1.22%` and
`vs_sovereign −4.02 pts` were struck on the $12,017M hand-cap; at today's $11,553M the same
construction gives 1.27% and −3.97 pts.)*

**2. WHAT THE PRICE ALREADY ASSUMES.** As a perpetual Gordon rate at the [E4-28] floor:
**9.08% forever** on the bottom boundary, **6.79% forever** even on the best year ever filed.
As a fading rate — a DCF run **as an engine only, casting no vote [E3-34]** — the quote
requires **17.6% a year for ten years then 3% forever, discounted at 10%**, from the trailing
$258.6M; **12.8% a year** from the FY2025 peak; **23.6% a year** from the 3-year mean.

**What the business has actually done:** revenue **+13.1%/yr** over four years, operating cash
flow **+14.3%/yr**, and **owner earnings −81.5% in the latest half-year.** **[E4-35]** is the
bound: *"fewer than 10 of the 200 most profitable companies in 2000 will attain 15% annual
growth in earnings-per-share over the next 20 years."* The quote requires 17.6% for ten years
from a business whose owner earnings have just fallen by four fifths.

**3. WHAT YOU ARE PAID.** **−4.32 points against the sovereign** on the bottom boundary;
**−2.03 points** on the best year Pinterest has ever filed.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — capitalising owner earnings at the **bare
sovereign, no per-name risk premium added [E3-42]**, plus the net cash:

| | conservative | optimistic | *on the best year ever* |
|---|---|---|---|
| at the sovereign 5.24% | **$2.3bn · $4.10/sh** | **$3.5bn · $6.17/sh** | *$7.4bn · $13.03/sh* |
| at the [E4-28] 10% floor | $1.4bn · $2.40/sh | $2.0bn · $3.48/sh | *$4.0bn · $7.08/sh* |
| **current price** | | | **$20.40** |

**Round numbers, as the corpus requires: roughly $4 to $6 a share against the bare bond;
roughly $2.50 to $3.50 against the 10% floor; and roughly $13 a share on the single most
favourable year the company has ever filed, capitalised at the bond with no discount at all.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **0.9% to 2.2%**, against the corpus's ~10%. **Below the
floor by a factor of five. The name is not ranked — it is quit on**, and per the template the
ranking lines are not filled in.

**WHICH BAR? NEITHER, AND THAT IS THE POINT.** The **screamer test [E4-01]** returns the third
outcome, not the middle one: **the price is above the whole range, not inside it.** No margin
of safety is computed, because **[E4-11]**'s margin is applied to a value the price already
exceeds by 3.3x at the optimistic end. **Windage count: ONE.** Conservatism is spent once, on
the bottom-boundary choice of window; the sovereign is bare, no premium is stacked, and the
owner-earnings inputs are the filed figures unadjusted.

**PASS/FAIL: FAIL, on price, by the widest margin in the current reading queue — and the
business gate had already closed at Q2 before the price was ever computed.**

---
## Q6 — WHAT WOULD PROVE ME WRONG?

*Not filled as a verdict — the file closed at Q2 and there is no position to monitor. The
falsifiers are recorded because **[E1-02]** requires yardsticks set in advance and because
this verdict should be reviewable by whoever reads it next.*

**What would reopen Q2** (repeated from above, so it sits in one place): a filed
decomposition of ARPU into **impressions delivered and average price per ad**, on Meta's
standard, showing **price per ad rising for four consecutive quarters**; **or**
U.S.-and-Canada ARPU above **$40** with U.S.-and-Canada MAU above **115M** in the same filed
year; **or** a GAAP operating margin above **20%** sustained for four quarters.

**The thesis-breaking metric for the OUT itself:** **SBC ÷ operating cash flow below 45% for
a full fiscal year.** At that level the labour cost stops consuming the business and the
owner-earnings series becomes something a valuation can be built on. It has never been below
55.2%.

**Next catalyst date:** Q3 2026 results, expected late October 2026 — the first full quarter
after the January restructuring, and the first read on whether H1's 89.5% SBC/OCF was
transformation cost or the new level.

- **VERDICT: not reached.** The run stopped at Q2.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → stop.**
- [x] No question marked IN carries an "unverified" or "provisional" caveat.
- [x] No UNRESEARCHED verdict was written, so none needs an artifact named.
- [x] No UNKNOWABLE verdict was written.
- [x] Step 0: the filing was read, with six 10-K accession numbers, two 10-Qs, two proxies
      and three 8-K exhibits; **three figures cross-checked to the dollar** (OCF $1,284,264k,
      SBC $880,463k in two independent places, capex $32,375k).
- [x] Owner earnings on a multi-year mean; **seven windows published [E4-38]**; capex band
      disclosed as a judgment and shown to be 0.6% of OCF wide.
- [x] Competitor row filled — **5 of the 8 competitors the company names, plus 1 adjacent;
      three are UNLISTED and named as a hard limit, not patched.** The moat class is not
      marked PROVISIONAL because the verdict rests on Pinterest's own filed competition
      paragraph and its own deferred-revenue line, neither of which needs a peer filing.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority, dated
      2026-09-04.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (screamer test, third outcome); **windage count = 1**, stated.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] **All Q3/Q4/Q5 material is headed as recorded-below-a-closed-gate and carries no entry
      language** (operator rules 2 and 3).
- [x] Run committed to git after each gate.

## REGISTER
- **Verdict: [x] OUT** — about the business.
- **One line:** *Pinterest understands its own economics and files the honest physical series,
  but it sells a substitutable advertising inventory to customers who have no contract, at a
  price its own CEO says is wrong, and at $20.40 it costs 3.3x the most generous value this
  method can construct.*
- **Q1 IN · Q2 OUT · Q3 not reached · Q4 not reached · Q5 not reached (computation only) ·
  Q6 not reached.**

---
## RUN LOG
- 2026-09-07: file created; Step 0 and the screen-row rebuild written. Write-early protocol.
- 2026-09-07: Q1 written — IN.
- 2026-09-07: Q2 written — **OUT** on [E3-03] criterion (2). Competitor row built at
  `_research 2026-09-07 PINS/COMPETITOR_ROW.md`. File closes here.
- 2026-09-07: below-the-gate findings, Q5 computation, self-audit and register written.
  Run complete.
