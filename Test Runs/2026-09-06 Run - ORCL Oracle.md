# Company Run — ORACLE CORPORATION (ORCL) — 2026-09-06
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
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year,
  struck fresh from the issuing authority** (not FRED; CLAUDE.md's corrected ladder).
- FX: none. Oracle reports in USD and 62% of revenue is Americas. No ADR ratio.

**PRICE AND THE SHARE COUNT — STAGE 0 BY HAND.**
- **Price $158.78, 2026-09-04** (Yahoo aggregator, **FLAGGED** — aggregators for live quotes
  only, operator rule 5). 52-week range **$114.99 – $328.33**. *The stock is 51.6% below its
  own 52-week high; this is not a name the market is currently in love with, and the run
  says so before it computes anything.*
- **Shares 2,880,471,000**, hand-read off the FY2026 10-K cover: *"Number of shares of common
  stock outstanding as of June 12, 2026: 2,880,471,000."* **ONE class of common stock** (no
  A/B artifact — the BRK-B / GOOGL problem does not arise). Cross-checked against the XBRL
  `dei:EntityCommonStockSharesOutstanding` for the same accession: identical.
- **NO SPLIT in the window** (last Oracle split was 2000). `close`, never `adjclose`.
- **Common market cap = 2,880,471,000 × $158.78 = $457,341M.**
- **PLUS $5,000M of 6.50% Series D Mandatory Convertible Preferred** issued 2026-02-05
  (50,000 shares × $100,000 liquidation preference), mandatorily converting 2029-01-15 into
  between 499.8126 and 624.7657 common shares each — i.e. **between 25.0M and 31.2M further
  common shares, already contracted.** Enterprise claim on owner earnings therefore
  **$462,341M**, and that is the figure used at Q5. *(The GOOGL run's $19bn preferred is the
  precedent for adding it rather than ignoring it.)*
- **THE SCREEN'S CAP IS WRONG BY 5.3%**: the 2026-09-04 FLOOR SCREEN carries $434,433M, which
  is $158.78 × 2,736M shares — a share count 144.5M short of the filed cover. Every screen
  yield for ORCL is therefore ~5% too generous. Recorded, not used.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2026 Form 10-K, fiscal year ended 2026-05-31, filed 2026-06-22, accession
  `0001193125-26-277521`** (`orcl-20260531.htm`).
- **Eight 10-K vintages read and diffed: FY2019 through FY2026** (accessions
  0001564590-19-023119 · 0001564590-20-030125 · 0001564590-21-033616 · 0001564590-22-023675 ·
  0000950170-23-028914 · 0000950170-24-075605 · 0000950170-25-087926 · 0001193125-26-277521).
- **Figures cross-checked against the filed statement, not the XBRL:** PP&E gross
  **$122,651M** and accumulated depreciation **$(22,694)M** read off Note 4 and reconciled to
  net **$99,957M**; total senior notes and other borrowings **$130,105M** read off Note 6;
  capital expenditures **$55.7 billion** read off the MD&A Liquidity section in words
  (*"Cash used for capital expenditures increased from $21.2 billion in fiscal 2025 to $55.7
  billion in fiscal 2026 primarily due to the expansion of our data centers"*) and matched to
  the tagged `PaymentsToAcquirePropertyPlantAndEquipment` of $55,663M.
- **No Q1 FY2027 10-Q exists at run time** (period 2026-08-31, due ~2026-09-10). The FY2026
  10-K is 3 months and 6 days old and is the whole of the evidence. **This run has no stub
  problem and no furnished-8-K problem — the AVGO defect does not repeat here.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Oracle is two businesses bolted
together, and the filing lets you see both **[E5-37]**:

1. **A rent on a thirty-year-old installed base.** Oracle sold database and application
   licences to essentially every large enterprise and government on earth over four decades.
   Those customers pay **software support** every year — $19,804M in FY2026 — to keep getting
   patches, security fixes and the legal right to run the thing. The marginal cost of
   supplying that is a support organisation that does not scale with the fee. It is a
   toll booth on software already installed and too expensive to remove: ripping Oracle out
   of a bank's core ledger means re-writing the ledger.
2. **A landlord for compute.** Oracle builds data centres, fills them with GPUs and servers,
   and rents the capacity — **cloud infrastructure $18,101M in FY2026, +77%.** The economics
   here are not software economics at all. They are **real-estate-plus-depreciating-hardware
   economics**: you buy a six-year asset with borrowed money, sign a long contract, and hope
   the spread between the contract and (interest + depreciation + power) is positive.

**The scarce input each controls.** Business 1 controls **switching cost** — the customer's
own accumulated data, schema, stored procedures and audit history, which Oracle did not
create but does hold hostage. Business 2 controls **nothing scarce that it did not buy**:
the GPUs come from NVIDIA at NVIDIA's price, the power comes from utilities under take-or-pay
contracts ($13,309M of them filed), the land and shells come increasingly from landlords
(**$260 billion of lease commitments not yet commenced**). *A business whose scarce input is
purchased from a monopolist supplier and resold to three monopsonist customers does not
control a scarce input; it is a spread.*

**Will the fundamentals look broadly the same in ten years?** **For business 1, yes** — the
support line has moved $19,365M → $19,804M across five fiscal years, which is the most stable
series in this filing and behaves exactly like a bond. **For business 2, no, and Oracle's own
filing says so**: capex went $2,135M (FY2021) → $55,663M (FY2026), a **26-fold rise in five
years**, and the MD&A states *"We expect this upward trend to continue during fiscal 2027 and
in the following fiscal years."* A business whose capital base is compounding at 90% a year
is not "relatively simple and stable in character" **[E3-31]**.

**So why is this not an immediate Q1 OUT?** Because [E3-31]'s test is whether *I* can
understand the unit economics and define what I do not know — not whether the business is
placid. **I can state both engines in plain words, I can find both revenue lines and both
cost bases in the filed statements, and the arithmetic that matters (cash in, capital out) is
four lines of a cash-flow statement.** The instability is a Q2/Q4 finding, and it is recorded
there, loudly. **[E4-46]** also binds the other way: this is not a business that would take
five months to learn; it took an afternoon, and the hard part is a judgment, not a fact.

**Recorded against myself [E4-26]:** the honest counter-argument for Q1 OUT is that Oracle's
FY2026 filing describes a company whose largest capital commitments (**$260bn of leases, $19bn
of post-year-end purchase commitments, $638bn of RPO**) are all *forward*, all *contracted*,
and none of them are in the historical series I would use to value it. That is a real
objection, and the answer is that it makes the *number* uncertain, not the *mechanism*
unintelligible. **The uncertainty is priced at Q4/Q5, not hidden here.**

- **VERDICT: [x] IN** — two comprehensible engines, both filed, both measurable. The
  instability of the second is carried forward as evidence, not as a pass.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**THE BRIEF'S HYPOTHESIS WAS THAT Q2 WOULD SPLIT. IT DOES — AND THE PROFIT-MIX TEST GIVES A
DECISIVE ANSWER THE BRIEF DID NOT ANTICIPATE: MEASURED BY CAPITAL, THE COMMODITY TAIL IS NOW
THE WHOLE DOG.**

### [E3-03], applied twice, because there are two businesses **[E5-37]**

| criterion | the software annuity | Oracle Cloud Infrastructure |
|---|---|---|
| (1) needed or desired | **YES** — the database runs the ledger | **YES** — compute is demanded |
| (2) **no close substitute** | **YES** — the substitute exists technically and is refused economically; migration means re-writing the application | **NO** — and Oracle's own Item 1 says so: *"due to the **low barriers to entry in many of our market segments**, new technologies and new and growing competitors frequently emerge to challenge our offerings"* |
| (3) not price-regulated | **YES** | **YES** |

**[E4-04] — must the moat be continuously rebuilt?** This is the whole question and the two
halves answer it in opposite directions. The annuity's moat is the customer's own accumulated
schema and data; a lapse in spending **narrows** it, it does not destroy it — [E5-23]'s
defence case, the Coca-Cola shape. **OCI's moat must be BOUGHT AGAIN EVERY GENERATION**:
Oracle's own Note 4 puts the useful life of *"servers and networking equipment"* at **six
years**, and $59,634M of the $122,651M gross book plus most of the $39,973M of construction
in progress is exactly that. **A six-year asset bought from a supplier at the supplier's price
and resold into a market with four larger participants is [E4-04]'s excluded class**, and it
is [E3-51]'s surfing run — *"the advantage lives in the wave, not the surfer."* The wave is
AI capital spending, and Oracle does not own it.

**[E4-36] — which of the four causes of extreme success?** The annuity is cause (1), an
extreme max on one variable (switching cost). OCI is cause (4), wave-riding. **Only the first
is ownable.**

### THE PROFIT-MIX TEST — the HAS/EFX precedent, run on capital rather than revenue

The brief asked which tail wags. **On revenue it is genuinely close; on capital it is not
close at all, and capital is the question this business poses.**

| measure, FY2026 filed | the software annuity | OCI + cloud |
|---|---|---|
| revenue | software $24,541M (36.4%) | cloud $33,989M (50.5%) |
| revenue growth contribution FY2026 | software **−$183M** | cloud **+$9,483M** |
| capital expenditure | ~nil | **essentially all of $55,663M** |
| PP&E + operating-lease ROU on the balance sheet | ~nil | **$129,647M — 49.5% of total assets** |
| contracted forward capital | ~nil | **$260,000M of leases not yet commenced + $13,309M purchase obligations + $19,000M post-year-end** |

**Five years ago net PP&E was $7,049M. It is $99,957M. The company that existed in FY2021 is
a rounding error on the balance sheet of the company that exists now.**

### THE ANNUITY'S OWN SERIES — filed, and it is the finding

**Software support revenue, five consecutive 10-Ks:**

| FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| $19,365M | $19,426M | $19,609M | $19,523M | **$19,804M** |
| — | 0% | +1% | **0%** | **+1% reported, −1% CONSTANT CURRENCY** |

**+2.3% cumulative in four years — 0.56% a year — and negative in constant currency in the
most recent year.** And the line that FEEDS it is shrinking: **software licence $5,878M →
$5,779M → $5,081M → $5,201M → $4,737M, down 19.4% in four years.** The mechanism is filed:
*"Software support contracts are generally: **priced as a percentage of the net fees paid by
the customer to purchase a software license**."* **Support revenue is arithmetically a
function of the cumulative licence base. A licence line down a fifth in four years is a
leading indicator on the annuity, and the annuity has already stopped growing.**

**[E2-44] — the two-characteristic test, and this is the [E2-44] evidence the brief asked
for.** (1) *Can it raise prices when demand is flat and capacity is not fully utilised?* **The
filed answer for FY2026 is NO: constant-currency software support revenue FELL 1%.** Oracle
does raise annual support uplifts; the filing shows the uplift did not outrun attrition.
(2) *Can it grow dollar volume with only minor additional investment of capital?* **The
annuity, yes. The company, emphatically no — $55,663M of capex against $9,958M of revenue
growth.**

**[E4-37] — agony or yawn?** Oracle's own risk factors are the agony end: *"the increasing
prevalence of various cloud offering models by us and our competitors **may unfavorably impact
the pricing of our cloud and software offerings**"*, and on the infrastructure side *"the
terms, renewal options and **pricing adjustments in our long-term data center leases typically
do not align with the duration and pricing of customer contracts**."* **A business that has
contracted its costs on a fifteen-to-nineteen-year term and its revenues on a one-to-five-year
term has written down, in its own 10-K, that it does not control its price.**

**[E3-33] untapped pricing power — NOT CLAIMABLE, and the reason is [E5-28]:** claiming the
class is claiming near-monopoly. Oracle's own Item 1 names **fourteen** competitors and cites
low barriers to entry. The claim is refused.

**[E4-32] direction — narrowing on every filed metric the framework asks for:**

| metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| cloud + software **segment margin %** | 68% | 67% | 64% | 64% | 63% | **59%** |
| capex ÷ depreciation | 1.39x | 2.29x | 3.44x | 2.19x | 5.49x | **7.30x** |
| depreciation as % of capex **[E5-20]** | 72.0% | 43.7% | 29.1% | 45.6% | 18.2% | **13.7%** |

*(The segment margin is Oracle's own presentation and it already **excludes** stock-based
compensation, amortisation of intangibles and certain allocations — so the true decline is
steeper than the nine points shown.)*

### **[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. RECORDED SWEEP: NO UNIT SERIES EXISTS.**

FY2026 10-K, word-boundary counts: **`ARR` 0 · `annual recurring revenue` 0 · `megawatt` 0 ·
`gigawatt` 0 · `MW` 0 · net retention 0 · a numbered renewal rate 0 · a count of data centres
0 · a count of cloud regions 0 · a customer count 0.** The words *"renewal rates"* appear once
and *"installed base"* once, both in prose, neither with a number — and the identical prose
appears in the FY2019 10-K. **Nothing was withdrawn; nothing was ever filed.** Under the
four-verdict test the physical series is **UNKNOWABLE, not UNRESEARCHED — no document exists
on the filing rung that would supply it.** *(Absence is a finding, and it is the same finding
the AVGO run recorded three days ago at a second AI-infrastructure name.)*

### THE CONCENTRATION DISCLOSURE IS TRUE AND ECONOMICALLY EMPTY

FY2026 10-K, verbatim: *"**No single customer accounted for 10% or more of our total revenues
in fiscal 2026, 2025 or 2024.**"* **The test is on revenue, and the risk is not in revenue —
it is in the $638 billion of remaining performance obligations, of which Oracle's own MD&A
says the increase was *"primarily attributable to **certain significant cloud contracts** that
were entered into during the period."*** The very next sentences of the same footnote say what
the 10% test does not: *"We enter into **certain large, long-term customer cloud arrangements**
that require us to make significant infrastructure investments… **The economic returns on
these investments are dependent on customer demand and the ability of our key customers to
meet their contractual obligations.**"* **"Certain" and "key customers" are the only
quantification filed. No RPO concentration figure exists in any vintage.**

### **OCI'S MARGIN CANNOT BE READ, AND THAT IS STRUCTURAL, NOT AN OVERSIGHT**

Note 15: *"We have **three businesses**—cloud and software…, hardware and services—each of
which is comprised of a **single operating segment**."* **OCI is not a segment. Cloud
applications and cloud infrastructure are disclosed at the REVENUE line only** (new in
FY2026 — $15,888M and $18,101M, a genuine increase in disclosure). **No cost, no margin, no
capex and no assets are filed for OCI separately.** Oracle files no segment capex, no segment
assets and no segment depreciation for any of its three businesses. **So the single most
important economic question about this company — what does OCI earn on the $129.6bn of
capital it has consumed — is UNKNOWABLE from the filings, and the run says so rather than
estimating it.** *(This is the GOOGL finding replicated: Alphabet also files no segment capex
after FY2019 and no segment assets ever.)*

**THE COMPETITOR ROW — required [E3-28].** *Filled from primary filings; see
`Test Runs/_research 2026-09-06 ORCL/competitor_row.md`.*

**SIX PEERS, ALL FROM PRIMARY FILINGS, LATEST COMPLETED FISCAL YEAR EACH.** Oracle's own Item 1
names fourteen competitors; I took the six that compete for the same dollar at scale. SAP is
reported in **EUR, unconverted** — no FX rate was applied, and the ratios are currency-neutral
so the comparison holds.

| | **ORCL FY26** | MSFT FY26 | GOOGL FY25 | AMZN FY25 | SAP FY25 (EUR) | IBM FY25 | CRM FY26 |
|---|---|---|---|---|---|---|---|
| Revenue ($M) | **67,357** | 331,839 | 402,836 | 716,924 | 36,800 | 67,535 | 41,525 |
| Operating margin | **30.59%** | 46.78% | 32.03% | 11.16% | 26.13% | *not presented* | 20.06% |
| Capex ($M) | **55,663** | 115,948 | 91,447 | 131,819 | 739 | 1,091 | 594 |
| **capex ÷ depreciation** | **7.30x** | 3.38x | 4.33x | 3.15x | 0.56x | 0.48x | 0.50x |
| **capex ÷ revenue** | **82.64%** | 34.94% | 22.70% | 18.39% | 2.01% | 1.62% | 1.43% |
| Operating cash flow ($M) | **31,977** | 182,935 | 164,713 | 139,514 | 9,156 | 13,193 | 14,996 |
| **Total debt ($M)** | **129,541** | 40,294 | 48,543 | 68,396 | 6,150 | 61,260 | 14,439 |
| **debt ÷ operating cash flow** | **4.05x** | 0.22x | 0.29x | 0.49x | 0.67x | 4.64x | 0.96x |
| Cloud segment operating margin | **NOT DISCLOSED** | IC **41.35%** | GCP **23.69%** | AWS **35.43%** | n/a | n/a | n/a |
| Leases **not yet commenced** | **$260bn** | **$329.1bn** | $58.5bn | $96.4bn | — | — | — |
| …as a multiple of own revenue | **3.86x** | 0.99x | 0.15x | 0.13x | — | — | — |

*Accessions: MSFT `0001193125-26-323660` FYE 2026-06-30 · GOOGL `0001652044-26-000018` FYE
2025-12-31 · AMZN `0001018724-26-000004` FYE 2025-12-31 · SAP **20-F** `0001104659-26-020058`
FYE 2025-12-31 · IBM `0000051143-26-000010` FYE 2025-12-31 · CRM `0001108524-26-000060` FYE
2026-01-31 · ORCL `0001193125-26-277521` FYE 2026-05-31.*

- **Peers named: 6** of the 14 Oracle itself names. Buffett says eight; I took the six that are
  actually competing for the same enterprise dollar at scale and say so.
- **Peer limits stated, not papered over:** IBM's income statement **does not present operating
  income at all** (gross profit → total expense and other income, with interest inside the
  block); `OperatingIncomeLoss` is untagged and any figure would be my arithmetic, so the cell
  is left empty rather than filled. SAP discloses no PP&E-only cash capex (the line combines
  intangibles), so SAP's capex ratios are an upper bound. AMZN's depreciation denominator is a
  different concept from Oracle's. **None of these limits touches the row's decisive facts.**

**THE ROW'S THREE DECISIVE FACTS, AND ALL THREE CUT AGAINST THE SUBJECT:**

1. **ORACLE IS THE MOST CAPITAL-INTENSIVE COMPANY IN THE ROW BY A FACTOR OF 2.4, AND IT IS THE
   SMALLEST OF THE FOUR CLOUDS.** capex ÷ revenue of **82.64%** against Microsoft's 34.94% and
   Amazon's 18.39%. Oracle is spending **eighty-three cents of capital for every dollar of
   revenue it books**. No other company in the row is above 35%.
2. **ORACLE CARRIES MORE DEBT THAN MICROSOFT AND ALPHABET COMBINED, ON ONE-FIFTH OF
   MICROSOFT'S REVENUE.** $129,541M against $88,837M. Debt ÷ operating cash flow is **4.05x
   against Microsoft's 0.22x, Alphabet's 0.29x and Amazon's 0.49x** — Oracle is 8 to 18 times
   more levered against its own cash generation than the three clouds it competes with.
   *(IBM at 4.64x is the only company in the row that is more levered, and IBM is not building
   data centres.)*
3. **THE ONE NUMBER THAT WOULD SETTLE THE MOAT QUESTION IS THE ONE ORACLE DOES NOT FILE.** All
   three rivals disclose a cloud segment margin — **41.35% / 35.43% / 23.69%.** Oracle
   discloses none. **A company competing on price against three disclosed margins, while
   refusing to disclose its own, is a Q2 fact and not a neutral one.**

**AND ONE FACT FOR THE SUBJECT, RECORDED FIRST BECAUSE [E4-26] REQUIRES IT: Microsoft's
uncommenced lease commitment is LARGER in dollars ($329.1bn vs $260bn).** The framework's own
MSFT run recorded it and passed Q4. **The difference is the denominator: Microsoft's is 0.99x
its revenue and 1.80x its operating cash flow; Oracle's is 3.86x its revenue and 8.13x its
operating cash flow.** Same instrument, four to eight times the relative weight.

**[E3-61] — the row's stated limit.** *"identical structures produce opposite outcomes … I
think you'd have to know the people involved."* The row shows position. It cannot show whether
Oracle's counterparties honour their contracts, and that is the question the whole file turns
on. The row is not asked to answer it.

- **Untapped pricing power [E3-33]:** **refused** — see above; [E5-28] requires near-monopoly
  and Oracle's own Item 1 refutes it.
- **[E2-45] the attacker's test — and here Oracle earns a mark the other two AI names in this
  queue did not.** *"How would I like, assuming I had ample capital and skilled personnel, to
  compete with it?"* Against the annuity: **badly** — I would have to persuade a bank to
  re-write its ledger. Against OCI: **easily, and four people already are**, with more capital
  than Oracle and, in three cases, without borrowing to do it. **Recorded sweep, and it cuts
  FOR Oracle on disclosure: Oracle NAMES ITS COMPETITORS** — Adobe, Alphabet, Amazon.com,
  Cisco, Intel, IBM, Microsoft, Salesforce, SAP SE, Hewlett-Packard Enterprise, Workday, plus
  Allscripts, Arcadia, athenahealth, Epic Systems and InterSystems for Cerner. **Broadcom
  names zero and Alphabet names zero, both established by recorded sweep in this same week.
  Oracle names fourteen-plus in every vintage FY2019–FY2026.**
- **Class: [x] NARROW** · **Direction: NARROWING, and the narrowing is measured, not asserted**
  — segment margin 68%→59%, constant-currency support revenue negative, licence revenue −19.4%,
  capital intensity 7.30x.

- **VERDICT: [x] IN (NARROW)** — the software annuity satisfies all three [E3-03] criteria and
  is a real franchise; OCI satisfies criterion (1) only and sits squarely in [E4-04]'s excluded
  class. **Q2 is IN because a narrow moat is still a moat, not because the composite is
  attractive.** The capital consumption is not priced here — it is a Q4 finding and it is
  where this file will be decided.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day **[E3-38]** — **argued and REFUSED.** The
  annuity is [E3-43]'s franchise half and tolerates mismanagement; OCI is the other half, but
  the corpus's test is *"their only products are promises"* [E2-70], and Oracle's product is a
  database that runs whether the executive suite is competent or not.
- [ ] **Control** — whole business, no exit **[E1-16]** — **NO.** Marketable security, daily
  liquidity, single share class.
- [x] **LEVERAGE — TICKED [E3-29].** *"small asset errors destroy equity."*

**CASE DECLARED: Q3 IS A BINARY GATE, AND NO PRICE COMPENSATES.** The justification, from the
filed balance sheet: **assets ÷ equity is 6.2x** ($261,759M ÷ $42,508M) against Broadcom's 2.1x,
which the AVGO run examined three days ago and *refused*. **Tangible equity is NEGATIVE
$22,982M** ($42,508M − goodwill $62,261M − intangibles $3,229M) — book equity exists only
because of the goodwill. Net PP&E of **$99,957M is 2.35x book equity**, so a 43% impairment of
the data-centre fleet eliminates the entire equity account, and **Oracle's own footnote names
that exact mechanism**: *"Changes in customer demand or the ability of our key customers to
meet their contractual obligations may adversely affect operating margins, cash flows and
**could require evaluation of the recoverability of related long-lived assets.**"* Add $260bn
of uncommenced lease commitments — **6.1x book equity, off the balance sheet.**

**The counter-case, recorded because [E4-26] demands it and because I ticked the box:** the
debt's *terms* are good **[E3-52]** — of $130,105M, only **$7,210M matures in fiscal 2027** and
$90,250M is "thereafter"; the notes are unsecured with no financial covenants; the only
financial covenant anywhere is on the undrawn revolver (Consolidated EBITDA ÷ Consolidated Net
Interest Expense **not less than 3.0:1.0**, comfortably met at roughly 6.5x). **The quantity is
extreme and the terms are benign. I tick the box on the quantity and say so.**

**Honesty — binary, permanent, filings-based [E5-16].** *Each matter dated to when it became
PUBLIC.* **NO DISQUALIFIER FOUND.**
- **No 10-K/A has ever been filed** — recorded sweep of the full EDGAR submissions index:
  amendment forms present are 4/A, 8-K/A, SC 13D/A, SC 13G/A, SC TO-T/A and SCHEDULE 13G/A.
  **Zero 10-K/A, zero 10-Q/A.**
- **Both FY2026 cover boxes are UNCHECKED** — no correction of an error to previously issued
  financial statements, and no restatement requiring a clawback recovery analysis.
- **Ernst & Young LLP, auditor since 2002**; unqualified opinion on the financial statements
  and on internal control; management concluded ICFR effective; *"There were no changes in our
  internal control over financial reporting"* — and **"material weakness" appears exactly once,
  in E&Y's boilerplate description of its own procedure.**
- **ONE Critical Audit Matter, and it is Uncertain Tax Positions** — not revenue recognition,
  not useful lives, not the $260bn of lease commitments. **Recorded as a finding in both
  directions: the auditor did not select the items this run finds hardest.**
- **Contingent-liability persistence — TESTED AND DOES NOT FIRE.** "Contingencies" word count
  fell 25 (FY2022) → 21 (FY2024) → 8 (FY2026), which looks like a withdrawal until you read
  it: the Hewlett-Packard Itanium litigation and the derivative suits were **resolved**, and
  what remains is a single named Netherlands GDPR class action described at length. **Matters
  closed, not quietly dropped.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30]. Recorded sweep of the FY2026 10-K.**

| flag | count / finding | fires? |
|---|---|---|
| weak accounting | SBC **expensed in full**, $4,811M through the income statement; **software development costs *"were not material"*** under both ASC 985-20 and ASC 350-40, so nothing is hidden in a capitalised-software line; no pension assumptions of consequence | **no** |
| unintelligible footnotes | Note 4 gives gross PP&E **by class with the life of each**, names servers at **six years**, and separately discloses **$39,973M of construction in progress**. *(Microsoft files no CIP figure in eleven vintages; Alphabet rebuilt its PP&E taxonomy mid-window. Oracle's PP&E note is the clearest of the three.)* | **no** |
| trumpeted projections / growth targets | *"guidance"* ×8, all risk-factor or tax prose; **no earnings guidance appears in any 10-K.** Oracle guides on quarterly calls, which are not filings and were not used | **no, on the filing rung** |
| **serial share issuance [E5-15]** | **$5,000M of 6.50% mandatory convertible preferred issued 2026-02-05, plus a $20 BILLION AT-THE-MARKET COMMON EQUITY PROGRAM entered 2026-02-02** | **FIRES** |
| **EBITDA / adjusted-earnings promotion [E4-29]** | *"EBITDA"* ×**1**, and it is a **lender's covenant**, not a promoted measure. *"non-GAAP"* ×2, *"free cash flow"* ×6 — and **Oracle's non-GAAP measure is FREE CASH FLOW, which it publishes at NEGATIVE $23,686M** | **does not fire — and see the candour finding below** |
| **filed-figure tells [E4-30]** | reported growth is **not** smooth (net income 13,746 → 6,717 → 8,503 → 10,467 → 12,443 → 17,087); **cash taxes paid ÷ pre-tax income fell 28.4% → 18.9%** in FY2026 | **the cash-tax tell FIRES numerically; read and answered below** |

**THE CASH-TAX TELL, READ RATHER THAN SCORED (operator rule 8).** Cash income taxes paid ÷
pre-tax income: FY2019 23.6% · FY2020 26.7% · FY2021 24.5% · FY2022 33.6% · FY2023 33.0% ·
FY2024 30.3% · FY2025 28.4% · **FY2026 18.9%**. A 9.5-point fall in one year is exactly
[E4-30]'s shape. **The filing explains it and the explanation is mechanical, not evasive:**
the MD&A states the FY2026 GAAP effective rate of 12.6% would be **19.9%** but for *"the U.S.
One, Big, Beautiful Bill Act related to the remeasurement of a deferred tax liability"*, and
$55,663M of capital expenditure generates accelerated tax depreciation on a scale nothing else
in the series does. **The tell fires, the cause is disclosed, and the cause is the same capex
this run is questioning — so it is evidence about the capital programme, not about honesty.**

**THE CANDOUR FINDING, AND IT IS THE STRONGEST SINGLE MARK IN ORACLE'S FAVOUR IN THIS FILE
[E2-26].** *"Does this reporting tell me what I would want to know if the positions were
reversed?"* **Oracle's chosen supplementary measure is free cash flow, and it publishes it at
NEGATIVE $23,686M, beside a line reading "Free cash flow as percent of net income −139%."** It
did not invent an adjusted metric to bridge the gap; it printed the hole. Against that:
Microsoft, Alphabet and Broadcom all pass this test by publishing no non-GAAP measure at all,
which is easier. **Oracle publishes one and lets it read minus twenty-three point seven
billion dollars.** That is the [E2-69] shape — a deviation *toward* candour.

**AND THE SAME TEST FAILS IN ONE PLACE:** the segment presentation. Oracle's cloud-and-software
"Total Margin" of **59%** excludes stock-based compensation, amortisation of intangibles and
"certain expense allocations" — so the number a reader takes from the MD&A is not a margin any
owner receives, and the reconciliation to the 30.59% consolidated operating margin is left to
the reader.

**STEP 3 — THE PRIMARY TEST [E2-01], AND THE ROE DENOMINATOR IS REFUSED UNDER [E2-47]/[E2-43].**

Reported ROE: **50.9% (FY2019) · 83.9% · 262.4% (FY2021) · NOT COMPUTABLE, EQUITY NEGATIVE
$6,220M (FY2022) · 792.5% (FY2023) · 120.3% · 60.8% · 40.2% (FY2026).** **Every one of these is
an artifact.** [E2-47] carves out *"unusual debt-equity ratios"* and Oracle spent FY2013–FY2022
converting equity into debt: **$150,028M of buybacks and $45,289M of dividends — $195,317M
returned — against a debt book that went to $130,105M and an equity account that went
negative.** A 792% ROE is a statement about the denominator, not the business.

**On [E2-43]'s denominator — unleveraged net tangible operating assets — FY2026:**
tangible assets $196,269M (= $261,759M − goodwill $62,261M − intangibles $3,229M) less
non-interest-bearing operating liabilities $51,271M = **$144,998M**, or **$113,104M excluding
the $31,894M of cash and securities.** Operating income $20,606M gives **14.2% pre-tax, or
18.2% ex-cash.** *(Broadcom, measured the same way three days ago: 99.3% and 269%.)* **This is
a fair business return, not a great one, and it is falling as the capital base compounds.**

**[E2-73] — judge the operator on the underlying assets, the buyer on what was paid.** Cerner
closed inside the window: **$27,721M paid in fiscal 2023**, the absolute-size acquisition gate,
the DKS/VMware shape. **Goodwill rose $18,450M in that year and has not moved since; no
impairment has ever been taken; and Oracle files goodwill by segment but has never published a
post-mortem against the announcement case [E4-39].** Healthcare is not separately reported, so
**what Oracle earns on the $27.7bn is UNKNOWABLE from any filed document.**

**[E2-56] — THE PRO-AM TEST, AND IT IS THE Q3 FINDING THAT MATTERS MOST.**
*"Their marvelous core businesses camouflage repeated failures in capital allocation
elsewhere."* Judge retention **incrementally**, never on the blended return:

| | |
|---|---|
| Operating income, FY2021 | $15,213M |
| Operating income, FY2026 | $20,606M |
| **Gain** | **+$5,393M** |
| Capital expenditure FY2022–26 | $96,950M |
| Acquisitions FY2022–26 (Cerner) | $27,932M |
| Operating-lease liabilities added | ~$27,700M |
| Finance-lease liabilities added | $7,701M |
| **Total capital deployed** | **~$160,283M** |
| **Incremental pre-tax return on capital deployed** | **3.4%** |
| …on capex alone | 5.6% |
| …on capex + acquisitions | 4.3% |

**Against [E5-40]'s ~12% "quite satisfactory" benchmark for retained capital, and against
Oracle's own FY2026 interest expense of $4,599M. Oracle has deployed roughly $160 billion of
new capital in five years to add $5.4 billion of operating income.**

**The honest objection, stated as the corpus requires [E4-51]:** $39,973M of that capital is
**construction in progress and has not earned a dollar yet**, and much of the FY2026 spend was
placed in service part-way through the year. **Excluding all FY2026 capex and measuring to
FY2025 makes it worse, not better — $69,219M deployed for +$2,465M of operating income, 3.6%.**
Removing the CIP from the denominator gives 4.5%. **Every construction lands between 3% and 7%.
The finding survives its own best counter-argument.**

**THE INSTITUTIONAL IMPERATIVE — score all four [E2-30].** *Not a fraud test.*
- [x] **resists any change in current direction** — the MD&A commits in advance: *"We expect
  this upward trend to continue during fiscal 2027 and in the following fiscal years."* And the
  $260bn of leases with **fifteen-to-nineteen-year terms** removes the option to stop.
- [x] **projects/acquisitions materialise to soak up available funds** — and beyond them:
  capex rose from $2,135M to $55,663M in five years while operating cash flow rose from
  $15,887M to $31,977M. **The funds available did not soak up the projects; the projects
  outran the funds by $23.7bn and the difference was borrowed.**
- [ ] staff studies produced to justify the leader's craving — **not observable from filings.**
  Recorded as not found, not as absent.
- [x] **peer behaviour mindlessly imitated** — this is [E2-27]'s capital-investment passage
  almost verbatim. Five companies are building the same asset at the same time: capex ÷
  revenue of 82.6% (ORCL), 34.9% (MSFT), 22.7% (GOOGL), 18.4% (AMZN). **"Viewed individually,
  each company's capital investment decision appeared cost-effective and rational; viewed
  collectively, the decisions neutralized each other."** Oracle is the smallest participant
  spending the largest share of its own revenue.

**THREE OF FOUR FIRE. [E4-52] — do they converge into a lollapalooza?** They do converge, but
on **one** outcome (build regardless), and **[E2-30]'s own final clause governs: "Institutional
dynamics, not venality or stupidity, set businesses on these courses."** This is a
capital-allocation finding, not a conduct finding, and it is carried to Q4 and Q5 rather than
being scored here.

**CAPITAL ALLOCATION — THE BUYBACK CONDITIONS [E5-08], AND THE ANSWER SURPRISED ME.**

**Filed repurchase record, share counts and dollars both from the 10-Ks:**

| fiscal year | shares repurchased | dollars | **implied average price** |
|---|---|---|---|
| 2018 | 238.0M | $11,500M | **$48.32** |
| 2019 | 733.8M | $36,000M | **$49.06** |
| 2020 | 361.0M | $19,200M | **$53.19** |
| 2021 | 329.2M | $21,000M | **$63.79** |
| 2022 | 185.8M | $16,200M | **$87.19** |
| 2025 | 3.9M | $600M | $153.85 |
| **2026** | **0.4M** | **$93M** | $232.50 |

**Oracle repurchased 1,847.8 million shares — roughly 39% of the company — between fiscal 2018
and fiscal 2022 at an average of about $56 a share, and the stock is $158.78 today. It then
cut repurchases by 99.4% as the price rose.** On [E5-24]'s first law — *"what is smart at one
price is dumb at another"* — **this is the best record the queue has recorded, and it is the
exact inverse of the AVGO finding three days ago (largest buyback in history at the highest
price ever paid).**

**Two honest qualifications, both against the flattering reading:**
1. **The disclosed reason is not valuation.** The filing says the pace depends on *"our working
   capital needs, **our cash requirements for capital expenditures**, acquisitions and dividend
   payments, our debt repayment obligations."* **Oracle stopped because it ran out of money for
   it, and the right outcome followed from a liquidity constraint rather than from [E5-08]
   condition 2.** $6.3bn of authorisation remains unused.
2. **[E2-60] BITES HARD AND IT IS THE BILL FOR THE GOOD RECORD.** *"where leverage rises to
   fund the payout, (c) was understated"* … *"a company that consistently distributes
   restricted earnings is destined for oblivion."* **The $195bn returned in FY2013–22 is
   precisely why the FY2026 balance sheet cannot fund the FY2026 capital programme from
   equity.** Oracle bought its own stock cheaply with borrowed money and now needs the
   borrowing capacity it spent. The buyback was good; the financing of it is the constraint
   the file now runs into.

**[E5-08] condition (1) — ample funds for operations and liquidity: FAILS TODAY.** Free cash
flow is −$23,686M. The buyback has correctly stopped. **Condition (2) is not reached because
there is no material repurchase to test.** No capital-allocation flag on the buyback.

**[E2-52] — DIVIDENDS FUNDED BY ISSUANCE. THIS ONE FIRES OUTRIGHT.** *"Beware of 'dividends'
that can be paid out only if someone promises to replace the capital distributed."* **FY2026:
$5,787M of dividends paid, against operating cash flow of $31,977M that was $23,686M short of
capital expenditure alone — funded by $46,093M of senior-note proceeds, $5,000M of preferred
stock, $1,900M of short-term financing related to capital expenditures, and a $20bn ATM
programme opened three months before the year end.** The dividend was raised from $4,743M to
$5,787M in the same year. **Every dollar of the FY2026 dividend was borrowed or issued, and
Oracle's own prospectus language says so: the preferred proceeds are for *"general corporate
purposes, which may include capital expenditures, repayment of indebtedness, future
investments or acquisitions and **payment of cash dividends on or repurchases of our common
stock**."*** *(That last clause is the [E2-52] mechanism written into the filing.)*

**[E2-49] — METRIC SWITCHING. TESTED ACROSS SIX VINTAGES; FIRES ONCE, AND IN THE HONEST
DIRECTION.** The *"Cloud Services and License Support Revenues by Ecosystem"* table — the
applications-versus-infrastructure split — was **last filed in the FY2025 10-K (2025-06-18,
acc. 0000950170-25-087926) and first omitted from the FY2026 10-K (2026-06-22, acc.
0001193125-26-277521), a gap of 369 days**, with no reason filed. **But what replaced it
discloses MORE, not less**: for the first time Oracle files cloud applications ($15,888M) and
cloud infrastructure ($18,101M) as separate revenue lines, and re-labels license support as
software support. **The switch REVEALED the deteriorating numbers — software support +1%
reported and −1% constant currency, software licence −9% — rather than concealing them.
[E2-49] asks whether the yardstick was disposed of when results deteriorated. Here the results
deteriorated and the disclosure improved. The flag is recorded and answered against my own
prior.** The one real loss: the applications-versus-database split of the support annuity is no
longer obtainable from any vintage after FY2025.

**PAY VERSUS PERFORMANCE — [E4-27], *"never, ever, think about something else when you should
be thinking about the power of incentives."*** *Source: DEF 14A filed 2025-09-26, accession
`0001193125-25-220801`, read against the 2024 and 2023 proxies. Full extract at
`Test Runs/_research 2026-09-06 ORCL/proxy_pay.md`.*

**DISCONFIRMING FACTS RECORDED FIRST, PER [E4-26] — AND THERE ARE FOUR, ONE OF WHICH IS THE
MOST SHAREHOLDER-FRIENDLY ACT THIS QUEUE HAS RECORDED IN A PROXY:**
1. **THE FY2025 BONUS WAS EARNED AT 104% OF TARGET AND PAID AT ZERO TO EVERY NAMED EXECUTIVE
   OFFICER.** The proxy files it line by line — *"$0 reduced from $5,207,393"* for Ellison and
   for Catz, *"$0 reduced from $520,739"* for Henley — and gives the reason: ***"the funds used
   for bonuses could be better directed to capital expenditures supporting future growth."***
   Management hit its number and took nothing.
2. **Ellison's salary was $1** in fiscal 2023, 2024 and 2025 (raised to $950,000 for fiscal
   2026, and the proxy says so rather than letting it be discovered). **He received no equity
   award in FY2025.** His $5,643,948 total is almost entirely **$5,564,838 of residential
   security**, and he is footnoted as **not an NEO** at all — the disclosure is voluntary.
3. **CEO pay ratio 11 to 1** (Catz $1,113,417 against a median employee of $98,899).
   *(Broadcom's, three days ago: 543 to 1.)*
4. **No employment agreements, no severance, no single-trigger vesting, no tax gross-ups, and
   no option repricing.** Two of the seven PSO tranches were **forfeited outright** — *"become
   the largest enterprise SaaS company"* and *"attain non-GAAP SaaS gross margin of 80%"* were
   missed and not paid.

**AND NOW THE FOUR THAT FIRE:**

**(a) THE PERFORMANCE PERIOD WAS EXTENDED WHEN THE GOALS WERE ABOUT TO LAPSE UNEARNED — [E2-49]
IN THE COMPENSATION COMMITTEE.** The 2017 grant of **17,500,000 performance stock options at a
$51.13 strike** (an identical grant to Ellison and to Catz) had its performance period
**extended by three years in fiscal 2022, from May 2022 to May 2025, at an incremental
accounting charge of $129,275,000 each — $258,550,000 across the two.** *"Yardsticks seldom are
discarded while yielding favorable readings. But when results deteriorate, most managers favor
disposition of the yardstick rather than disposition of the manager."* **Moving the finish line
is the same act as changing the metric, and here it is priced: a quarter of a billion dollars
of charge to keep an award alive that would otherwise have expired.** Five of seven tranches
were subsequently earned; the options expired 2025-07-20.

**(b) SIX OF THE SEVEN HURDLES WERE DISCLOSED ONLY INSIDE A GRAPHIC.** The market-capitalisation
thresholds — increases of **$16.7bn / $33.3bn / $50.0bn / $66.7bn / $83.3bn / $100.0bn** — are
not in the text of the proxy; they exist in an embedded image file (`g72066g00s01.jpg`), which
had to be downloaded and read to obtain them. **A number that a shareholder cannot find by
searching the document is not disclosed in the sense [E2-26] means.**

**(c) THE PLEDGE, AND IT IS TWENTY-ONE TIMES THE ONE THE AVGO RUN FLAGGED THREE DAYS AGO.**
**Larry Ellison owns 1,158,232,353 shares — 40.6% of Oracle — and has pledged 346,000,000 of
them**, which is **29.9% of his own holding and 12.1% of the entire company** *(my arithmetic
from the filed share counts; labelled as mine)*. The trend is the wrong way: **307,000,000
(2023) → 277,000,000 (2024) → 346,000,000 (2025) — up 69 million shares in the latest year.**
He is the **sole carve-out** from Oracle's own pledging policy: *"Mr. Ellison may continue to
pledge Oracle securities as collateral to secure or guarantee indebtedness, but he may not hold
Oracle securities in a margin account."* The board's stated rationale is that *"The pledged
shares secure personal term loans only used to fund outside personal business ventures"* and
that his ownership is *"more than 4,600 times what he is required to hold."* **Lenders,
principal, loan-to-value and maturities are NOT DISCLOSED. No other officer or director
pledges.** *(Recorded, not scored: the stock is down 51.6% from its 52-week high of $328.33
while this pledge grew. The framework has no rule here; the fact belongs on the file.)*

**(d) SELF-DEALING IS SMALL IN DOLLARS AND CONTINUOUS IN KIND [E3-57].** FY2025 related-party
sales to Ellison entities ~$10.8m and purchases ~$10.5m, including **a three-year SailGP
sponsorship with Ellison's own F50 League LLC at ~$10m a year** ($7.5m cash paid in FY2025),
**~$2.5m to Glass Aviation**, bought by his son in 2024, and **~$500,000 to Wing and a Prayer,
Inc., "a company owned by Mr. Ellison."** His half-brother is on the payroll at $301,962.
**Against $67,357M of revenue these are immaterial in amount; they are recorded because
[E3-57] runs self-dealing and folly as one agency cost, and because the mitigant Oracle
discloses puts the burden on Oracle to find a cheaper price and ask for reimbursement.**

**PAY VERSUS PERFORMANCE, ITEM 402(v), AS FILED:** compensation actually paid to the PEO (Catz
in all five years) **$40,389,348 (2021) · $139,242,032 · $304,050,680 · $94,264,234 ·
$461,805,673 (2025)**. Company TSR per $100 invested **48.84 / 37.95 / 106.80 / 132.03 /
231.50** against the **Dow Jones U.S. Technology Total Return Index** at **48.00 / 42.02 /
68.89 / 136.76 / 172.38.** **Oracle beat its comparator in three of five years and trailed in
two.** *(Broadcom beat its comparator in all five; Apple trailed.)*
**A DEFECT IN THE FILED TABLE IS RECORDED RATHER THAN SMOOTHED:** the PVP TSR column implies
+510% from fiscal 2022 to fiscal 2025, while the same proxy's CD&A says *"Oracle's stock was up
130% from the end of fiscal 2022 to the end of fiscal 2025."* **The two numbers in one document
do not reconcile. Reported as filed; not used in any valuation.**

**SAY-ON-PAY — LOW, IMPROVING, AND MORE ADVERSE THAN THE HEADLINE.** Filed as a percentage of
votes cast: **67% (2022 meeting) → 73% (2023) → ~78% (2024).** The 2025 result is **not in this
proxy** and the 2021 figure is referenced but **never stated.** No vote counts are filed.
**CONVENTION — my arithmetic, labelled as mine:** officers and directors hold **40.9%** of the
shares; if that block votes in favour, external support is roughly **(78 − 40.9) ÷ 59.1 = 63%
in 2024 and 44% in 2022.** **A third to a half of the outside register has been voting against
this pay structure for four years.** *(The AVGO parallel: 61.7% and 66.4% in mega-grant years.)*

**THE INCENTIVE READ [E4-27], stated plainly.** The bonus metric is **year-over-year growth in
non-GAAP operating income**, a measure that **adds back the stock compensation this framework
subtracts in full [E5-06]**, and the dollar target and dollar outturn for it are **not
disclosed**. All five of the proxy's "most important measures" are non-GAAP. **But the 2025
outcome is the opposite of what that structure would predict: the bonus was earned and waived
to fund capital expenditure.** And the largest incentive in the company is not in the
compensation tables at all — **it is 1,158,232,353 shares, 40.6% of the equity, held by the
man setting the strategy.** That aligns him with owners on direction and, through a
346-million-share pledge whose terms are undisclosed, with lenders on price.

**Two items absent from the proxy and named as absent:** the co-CEO grants of Magouyrk and
Sicilia (appointed September 2025) are **narrative only — no share counts, no fair values, no
performance metrics filed**; and Ellison's ownership percentage, which appeared in his 2024
director biography, **is removed from the 2025 one.**

**THE GUARDRAIL — checked before the verdict.**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The one strongly favourable
      finding — the buyback discipline — is recorded as a fact about the past and explicitly
      **not** allowed to repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [x] **Does this business require a great manager?** The annuity does not — [E5-18]'s
      stand-a-little-mismanagement test passes on a franchise thirty years old. **OCI does**,
      and that is recorded at **Q2 as a moat defect [E4-23]**, not here as a strength.
- [x] Is a great manager the reason to act? **No. No such case is made.**

- **VERDICT: [x] IN** — **as a BINARY GATE (leverage ticked), with NO DISQUALIFIER FOUND.**
  *IN is the absence of found disqualifiers, not a finding that the managers are honest —
  "sincerity and empathy can easily be faked" **[E5-17]**, and the filed statement itself is
  not bedrock **[E5-32]**. IN never promotes.*

**FOUR FLAGS FIRE AND NONE IS A CONDUCT FINDING [E5-38]:** serial share issuance **[E5-15]**
($5bn preferred plus a $20bn ATM); dividends funded by issuance **[E2-52]**; the yardstick
extended when the goals were about to lapse **[E2-49]**; and three of the four institutional
imperative behaviours **[E2-30]**. **[E4-52] convergence was tested and is REFUSED**: the flags
point at one behaviour — build the data centres, fund them however necessary — which
[E2-30]'s own closing clause calls *"institutional dynamics, not venality or stupidity."*
**They are capital-allocation findings and they are carried to Q4, where the file is decided.**

**AND THE COUNTERWEIGHT IS REAL AND IS NOT ALLOWED TO PROMOTE THE NAME [E2-37, E3-39]:** a
buyback record that is the best in this queue, an earned bonus waived to zero, a CEO pay ratio
of 11:1, no 10-K/A in the company's history, fourteen competitors named in Item 1, and a
self-published free-cash-flow figure of **negative $23,686M**. **On the two yardsticks of
[E3-59] — how well they run the business, and how well they treat their owners — Oracle scores
well on the second. The first is Q4's question and Q4 answers it differently.**

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

### THE SCREEN ROW — reproduced, then rebuilt over my own windows

**BOTH ENDS REPRODUCE, ONE OF THEM TO $0.3 MILLION — AND THE FOURTH SPREAD DEFECT IS HERE
AGAIN IN ITS PUREST FORM.** The 2026-09-04 FLOOR SCREEN carries `oe_bottom −11,193` and
`oe_top 14,464`.

- **`oe_top 14,464` = my three-year mean FY2024-26 with (c) = DEPRECIATION ONLY: 14,464.3.**
  Reproduces to **$0.3M.**
- **`oe_bottom −11,193` = my three-year mean FY2024-26 with (c) = CAPEX PLUS FINANCE-LEASE ROU
  ADDITIONS: −11,199.7.** Reproduces to **$6.7M a year** — the residual is the SBC difference
  between the cash-flow and equity statements, the same $M-scale residual the AVGO run found.
- **BOTH ENDS ARE THE SAME THREE-YEAR WINDOW.** The screen never varied the window; its `spread`
  cell is **empty** because it could not compute one. **The ~$25.7bn "band" the queue's tail
  triage named as "the finding" is a CAPEX-BAND artifact inside one window, not a window
  spread — the same defect that misled on AAPL, GOOGL and AVGO in three days, now at a fourth
  name.**
- **AND HERE IS WHERE ORACLE DIFFERS FROM THE OTHER THREE: the screen's width happens to be
  ROUGHLY RIGHT, for the wrong reason.** Rebuilt over four of my own windows the total span is
  −$11,200M to +$14,464M — essentially the screen's number — because Oracle's two ends move in
  *opposite* directions with recency (the strict end deteriorates, the depreciation end
  improves). **The screen got the width by coincidence and the reasoning by omission.**
- **The screen's CAP is separately wrong: $434,433M against the filed cover's $457,341M**, a
  share count 144.5M short. Every screen yield for ORCL is ~5% too generous.

### OWNER EARNINGS BY YEAR, BY HAND, FROM THE FILED CASH-FLOW STATEMENTS

**OCF − SBC − (c), all four constructions, FY2016–FY2026 ($M):**

| FY | OCF | SBC | capex | fin-lease ROU | depreciation | intang. amort. | **strict (capex+FL)** | **depreciation end** |
|---|---|---|---|---|---|---|---|---|
| 2016 | 13,685 | 1,037 | 1,189 | 0 | 871 | 1,638 | **11,459** | 11,777 |
| 2017 | 14,126 | 1,350 | 2,021 | 0 | 1,000 | 1,451 | **10,755** | 11,776 |
| 2018 | 15,386 | 1,607 | 1,736 | 0 | 1,165 | 1,620 | **12,043** | 12,614 |
| 2019 | 14,551 | 1,653 | 1,660 | 0 | 1,230 | 1,689 | **11,238** | 11,668 |
| 2020 | 13,139 | 1,590 | 1,564 | 0 | 1,382 | 1,586 | **9,985** | 10,167 |
| 2021 | 15,887 | 1,837 | 2,135 | 0 | 1,537 | 1,379 | **11,915** | 12,513 |
| 2022 | 9,539 | 2,613 | 4,511 | 0 | 1,972 | 1,150 | **2,415** | 4,954 |
| 2023 | 17,165 | 3,547 | 8,695 | 0 | 2,526 | 3,582 | **4,923** | 11,092 |
| 2024 | 18,673 | 3,974 | 6,866 | 0 | 3,129 | 3,010 | **7,833** | 11,570 |
| 2025 | 20,821 | 4,674 | 21,215 | 2,921 | 3,867 | 2,307 | **−7,989** | 12,280 |
| **2026** | **31,977** | **4,811** | **55,663** | **4,946** | **7,623** | **1,671** | **−33,443** | **19,543** |

**WINDOWS [E4-25] — more than one, with the spread carried, not resolved:**

| window | strict (capex + finance leases) | depreciation end | D&A end |
|---|---|---|---|
| 3-year FY2024-26 | **−$11,200M** *(= screen oe_bottom)* | **+$14,464M** *(= screen oe_top)* | +$12,135M |
| **5-year FY2022-26 — the corpus default [E2-42]** | **−$5,252M** | +$11,888M | +$9,544M |
| 8-year FY2019-26 | +$860M | +$11,723M | +$9,677M |
| 10-year FY2017-26 | +$2,968M | +$11,818M | +$9,873M |
| FY2026 alone | **−$33,443M** | **+$19,543M** | +$17,872M |

**COMBINED RANGE, CARRIED IN FULL: −$33,443M to +$19,543M on the single year; −$11,200M to
+$14,464M on multi-year means.**

**AND THE MEAN IS REFUSED, ON THE QUEUE'S OWN PRECEDENT.** [E4-25] and the tail triage's
sign-change rule both say the same thing: *"the multi-year mean is averaging two different
businesses… date the inflection and refuse the blended mean."* **The inflection is fiscal
2025**, and it is not subtle: capex went $6,866M → $21,215M → $55,663M in two years, and
finance leases went from **zero to $2,921M to $4,946M of annual ROU additions.** A five-year
mean averages a $42bn-revenue company spending $4.5bn of capital with a $67bn-revenue company
spending $60bn. **That is not a distorted year in a window; every year in the window is a
different company, and saying so is the Q4 finding [E5-11].**

### **MAINTENANCE CAPEX — THE DISCLOSED JUDGMENT. THIS IS THE FILE, AND IT ANSWERS THE BRIEF'S CENTRAL QUESTION IN BOTH DIRECTIONS.**

**FIRST: THE D&A END IS INVALID, AND BY THE WIDEST MARGIN THIS QUEUE HAS RECORDED.**
[E5-20]'s railroad benchmark is that true maintenance capex is *"higher than 60 percent"* of
total capex. **Oracle's depreciation is 13.7% of its capex.**

| | ORCL FY2026 | GOOGL (run of 2026-09-06) | MSFT (run of 2026-09-06) | [E5-20] benchmark |
|---|---|---|---|---|
| depreciation as % of capex | **13.7%** | 19.1% | 33% | **>60%** |
| capex ÷ depreciation | **7.30x** | 5.25x | 3.38x | — |

The ratio ran **1.13x–2.02x for the eight years FY2013–FY2021** — squarely [E3-44]'s default
class where *"the depreciation charge is not inappropriate … as a proxy"* — and then went
2.29 → 3.44 → 2.19 → 5.49 → **7.30x.** **The D&A end is not merely optimistic; the framework
calls it INVALID, and I do not use it except to display the band.**

**THE CVX INVERSION WAS TESTED AND DOES NOT APPLY.** Broadcom's D&A was 14.1x its capex because
its book was bought, not built. Oracle's is the reverse in every particular: the PP&E is
self-constructed data centres, intangible amortisation is *falling* ($3,582M → $1,671M) as the
Cerner intangibles run off, and **capitalised software is filed as *"not material"***, so
nothing is being renewed off the balance sheet.

**SECOND — AND THIS IS THE MEASUREMENT THE BRIEF ASKED FOR: (c) BUILT FORWARD FROM THE FILED
GROSS BOOK AT MANAGEMENT'S OWN FILED LIVES.** Oracle's Note 4 makes this easier than at
Microsoft or Alphabet, because **Oracle files the life of each class AND files construction in
progress separately — neither of which Microsoft does in eleven vintages:**

| class (FY2026 Note 4) | gross | Oracle's own filed life | annual charge |
|---|---|---|---|
| Computer, network, machinery and equipment | $59,634M | 1–6 yr; footnote (1): *"Comprised primarily of servers and networking equipment with estimated useful life of **six years**"* | **$9,939M** |
| Buildings and improvements | $21,263M | 1–40 yr *(25 judged; see sensitivity)* | $851M |
| Furniture, fixtures and other | $452M | 5–15 yr *(10 judged)* | $45M |
| Land | $1,329M | not depreciated | $0 |
| **in-service subtotal** | **$82,678M** | | **$10,835M** |
| **Construction in progress** | **$39,973M** | footnote (2): *"Comprised primarily of **servers, networking equipment** and leasehold improvements to be deployed at our data centers"* → 6 yr | **$6,662M when placed** |
| **TOTAL, on capital ALREADY SPENT** | **$122,651M** | | **≈$17,500M** |

**THE ONE LIFE I HAD TO GUESS BARELY MATTERS, WHICH IS WHY THIS CONSTRUCTION IS TRUSTWORTHY:**
buildings at 20 years gives (c) = $17,710M; at 25 years $17,497M; at 40 years $17,178M — a
**3.1% span**. **82% of the depreciable gross book is six-year server kit on Oracle's own filed
number, so the answer is set by a disclosed life, not by my judgment.**

**THE HEADLINE: ORACLE'S REPORTED FY2026 DEPRECIATION OF $7,623M IS 43.6% OF THE RUN-RATE
IMPLIED BY ITS OWN LIVES ON ITS OWN EXISTING BOOK — AND 70.4% OF THE IN-SERVICE-ONLY
RUN-RATE.** *(The 70.4% is honestly explained by mid-year placements: the in-service book went
$43,044M → $82,678M during the year. The 43.6% is the forward statement and it is not
explained away by anything.)*

**THIRD — AND THE BRIEF'S OTHER DIRECTION IS ALSO RIGHT, WHICH IS WHY (c) IS NEITHER END: THE
FY2026 CAPEX END OVERSTATES MAINTENANCE BY $38 BILLION.** $55,663M of capital spending against
a $17,500M steady-state requirement means **$38,166M of FY2026 capex is GROWTH capital**, and
[E2-23] asks only what the business *"requires to fully maintain"* its position and unit volume.

**AND THE TWO INDEPENDENT CONSTRUCTIONS CONVERGE — the MSFT shape, replicated:** the forward
build of **$17,500M** sits between the 8-year mean capex ($12,789M) and the **5-year mean capex
of $19,390M**, landing within 10% of the latter.

> **THE ANSWER TO THE QUEUE'S TAIL TRIAGE, WHICH NAMED THIS RUN SPECIFICALLY: the ~$25bn band
> is real, both of its ends are wrong, and the filing does decide it. (c) IS APPROXIMATELY
> $17,500M — not $7,623M and not $55,663M — and it is derived from a life Oracle itself
> filed, applied to a gross book Oracle itself disaggregated, with a construction-in-progress
> line Oracle itself broke out.**

- **(c) JUDGED AT $17,500M** — the forward build. **Band carried in full: $7,623M to $55,663M.**
- **Owner earnings at the judged (c):** OCF $31,977M − SBC $4,811M − $17,497M = **$9,669M.**
- **[E4-41] NORMALIZE DOWN FOR LUCK — one item, named and removed:** FY2026 operating cash flow
  contains **$4.6 billion of customer prepayments *"that included a significant financing
  component"***, and the same footnote says ***"No prepayments were received from customers that
  included a significant financing component during fiscal 2025 and 2024"*** and that Oracle
  *"recognize[s] interest expense related"* to them. **That is borrowing from customers sitting
  inside operating cash flow, non-recurring on Oracle's own statement. Removed.**
- **JUDGED OWNER EARNINGS: ≈$5,100M** *(= $9,669M − $4,600M)*, with **$9,700M carried as the
  generous end of the judged construction.**
- **TWO FURTHER CONSERVATIVE ADJUSTMENTS WERE AVAILABLE AND WERE EXPLICITLY DECLINED so that
  conservatism is not stacked [E4-11, E4-48]:** (i) accounts payable rose **$5,864M**
  ($5,113M → $10,977M) in a year of $55.7bn of capex, so an unknown part of that capex is
  unpaid and flattering operating cash flow — *named, quantified, NOT taken*, exactly as the
  MSFT run did with its own $19.8bn version; (ii) **$1,900M of "net cash proceeds from
  short-term financing related to capital expenditures"** sits in FINANCING, meaning capex is
  partly vendor-financed and the true spend exceeds the cash capex line — *named, NOT taken*.
- **Stock compensation subtracted in full, $4,811M [E5-06].** **[E3-70] recorded, not stacked:**
  the market value of options of like quantity and structure exceeds the accounting charge, so
  $4,811M is the floor of the correct subtraction and not the measure. SBC is 7.1% of revenue.
- **[E5-33]/[E3-53]: restructuring is IN the mean, not added back.** FY2026 restructuring and
  other was **$1,838M**, the largest in the eighteen-year series (FY2025: $374M). Oracle charges
  it through GAAP operating income and does not exclude it. *"To tell owners year after year,
  'Don't count this' … is misleading."*
- **[E2-23] constraint 3, the working-capital increment:** it moved *favourably* in FY2026 and
  the favourable part is the $4.6bn prepayment already removed above. Nothing further is due.

### Great, good, or gruesome? **[E4-20]**
- [ ] great  [ ] good  [x] **GRUESOME — on the incremental capital, which is now the whole
  company**

**The evidence, and it is [E2-56]'s incremental test, never the blended one.** *"The worst sort
of business is one that grows rapidly, requires significant capital to engender the growth, and
then earns little or no money… Investors have poured money into a bottomless pit, attracted by
growth when they should have been repelled by it."*

- **Consolidated (the flattering read): 14.2% pre-tax on unleveraged net tangible operating
  assets, 18.2% ex-cash. That is [E4-43]'s GOOD class and it passes.** Recorded first.
- **Incremental (the read [E2-56] requires): $160,283M of capital deployed FY2022–26 for
  +$5,393M of operating income = 3.4% pre-tax.** On capex alone 5.6%; on capex plus Cerner
  4.3%; measured only to FY2025 to strip the un-earning fleet, **3.6%.** **Every construction
  lands between 3% and 7%, against [E5-40]'s ~12% "quite satisfactory" and against Oracle's own
  $4,599M of interest expense.**
- **[E4-43]'s warning is honoured and it does not rescue the verdict.** The *good* class passes
  at *"$82 million pre-tax on $400 million of net tangible assets"* — **20.5%.** Oracle's
  incremental is 3.4%. [E4-20]'s own escape clause is *"unless the cash they consume gets to
  earn a reasonable return"*, and on the filed record it does not.
- **THE BEST COUNTER-ARGUMENT, QUANTIFIED RATHER THAN DISMISSED [E4-51]:** $39,973M of the
  denominator is construction in progress that has earned nothing. **For the FY2022-26 capital
  to reach 12%, operating income must rise $19,234M; it rose $5,393M; so the CIP alone must
  supply $13,841M — a 34.6% pre-tax return on the construction in progress, more than twice
  what the whole company earns on its capital. To reach merely 6%, the CIP must earn 10.6%.**
  **The bull case survives at 6% and dies at 12%, and 6% is below the cost of the debt funding
  it.**

### Staying power — score all three **[E5-11]**

**(1) A large and reliable stream of earnings — PASS, on the income statement.** Operating
income $10,926M → $13,093M → $15,353M → $17,678M → **$20,606M**, up every year since FY2022.
Software support of **$19,804M** is as bond-like a revenue line as exists in this queue.
**But the earnings do not survive the capital, and Oracle publishes that itself: filed free
cash flow −$394M (FY2025) and −$23,686M (FY2026).**

**(2) Massive liquid assets — MARGINAL, AND THE CASH IS BORROWED.** Cash $31,289M + marketable
securities $605M = **$31,894M**, which is 12.2% of total assets and 24.5% of debt. **It was
$10,786M twelve months earlier, and the increase is the $46,093M of senior notes and $5,000M of
preferred issued during the year.** This is not accumulated earnings sitting on the balance
sheet; it is the undeployed remainder of a bond issue.

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAIL, AND IT IS NOT CLOSE. *"Ignoring that
last necessity is what usually leads companies to experience unexpected problems."***

| twelve-month claim | $M |
|---|---|
| debt principal, fiscal 2027 (Note 6) | 7,210 |
| interest (FY2026 actual $4,599M, rising with the book) | ~5,500 |
| operating lease payments, fiscal 2027 (Note 9) | 3,712 |
| finance lease payments, fiscal 2027 (Note 9) | 656 |
| unconditional purchase obligations, fiscal 2027 (Note 9) | 1,841 |
| preferred dividends, 6.50% on $5,000M, **cumulative** | 325 |
| **CONTRACTUAL SUBTOTAL** | **19,244** |
| + common dividend at the FY2026 run rate | 5,787 |
| + capital expenditure, which the MD&A says **will rise above** | 55,663 |
| **TOTAL TWELVE-MONTH REQUIREMENT** | **≈80,694** |

**Against liquid assets of $31,894M plus operating cash flow of $31,977M = $63,871M. A
$16,823M shortfall in year one — and then the $260 BILLION of lease commitments begins to
commence, on Oracle's own filed timetable, *"between the first quarter of fiscal 2027 and
fiscal 2029."***

**[E5-39] — AND ORACLE DEPENDS ON THE KINDNESS OF STRANGERS IN ITS OWN WORDS.** *"We will never
be dependent on the kindness of strangers … cash is a lot like oxygen."* The corpus counts **no
bank lines, no commercial paper, nothing depended on.** Oracle's MD&A: *"we believe that our
current cash, cash equivalents and marketable securities balances, **together with cash
generated from operations and available financing arrangements**, will be sufficient … Thereafter,
we expect that our existing sources of liquidity, **together with potential access to additional
financing**, will continue to be sufficient."* **In March 2026 Oracle replaced a $6.0bn revolver
with a $10.0bn one and raised its commercial paper programme to $10.0bn. Excluding both, as the
corpus requires, the fiscal 2027 plan does not fund.**

**[E2-54] — THE COVERAGE TEST, AND IT FAILS OUTRIGHT.** *"whenever someone creates a capital
structure that does not allow all interest, both payable and accrued, to be comfortably met out
of current cash flow **net of ample capital expenditures** — zip up your wallet."*
**Operating cash flow $31,977M less capital expenditure $55,663M = NEGATIVE $23,686M, against
interest of $4,599M. Coverage is not thin. It is negative.** *(Broadcom's, measured the same way
three days ago: 10.1x.)*

**[E3-52] — read the terms, not just the quantity, and the terms are the one mercy.** Of
$130,105M, only **$7,210M matures in fiscal 2027** and $90,250M is "thereafter"; the notes are
unsecured with no financial covenants; the sole financial covenant is on the undrawn revolver
(Consolidated EBITDA ÷ Consolidated Net Interest Expense ≥ 3.0:1.0, met at roughly 6.5x).
**Long-dated and covenant-light. That is why the death mechanism below is not a near-term
default — it is something slower.**

**Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this framework
and the corpus supplies none:* total debt **$130,105M** plus operating leases $30,190M plus
finance leases $7,701M = **$167,996M of financial obligations**; assets ÷ equity **6.2x**;
tangible equity **NEGATIVE $22,982M**; debt ÷ operating cash flow **4.05x against Microsoft's
0.22x, Alphabet's 0.29x and Amazon's 0.49x.** *"Whenever a bright person … goes broke that has
a lot of money, it's because of leverage"* **[E4-16]**.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**

**[E4-40] governs the method: model EXPOSURE, not experience.** Oracle's loss history is benign
— no impairment has ever been taken on the fleet, no customer has defaulted, revenue has grown
every year. *"A benign loss history late in a good cycle is not only useless, but actually
dangerous."* Every mechanism below comes from what the filing shows Oracle is **exposed** to.

**DEATH 1 — THE DURATION MISMATCH, AND ORACLE WRITES IT DOWN ITSELF. [A REAL POSSIBILITY.]**
FY2026 10-K, verbatim: *"we could be **locked into multi-year commitments for excess data center
space and related capital expenditures, as well as associated financings, without receiving
corresponding revenue**. In addition, the terms, renewal options and **pricing adjustments in our
long-term data center leases typically do not align with the duration and pricing of customer
contracts**, and if customers do not renew their contracts, **we may be unable to re-lease,
repurpose or assign such capacity on acceptable terms, if at all**."*
**Quantified from filed figures: $260,000M of commitments over terms of fifteen to nineteen
years is roughly $15,300M a year of rent that continues whether the racks are full or empty —
74% of FY2026 operating income. A quarter of the fleet standing idle removes ~$3,800M of rent
coverage plus ~$4,400M of depreciation on the owned half: roughly 40% of operating income, from
a 25% occupancy shortfall.** Oracle's customer contracts run *"one to five years"*; its leases
run fifteen to nineteen. **And one guarantee comes due immediately: the disclosure names *"a
lease for which we have guaranteed up to $3.3 billion of the lessor's borrowing, which matures
in September 2026"* — this month.**

**DEATH 2 — [E2-27]'s COLLECTIVE IRRATIONALITY, AND THIS IS THE SHARPEST NUMBER IN THE FILE.
[A REAL POSSIBILITY.]** *"Viewed individually, each company's capital investment decision
appeared cost-effective and rational; viewed collectively, the decisions neutralized each other
and were irrational … After each round of investment, all the players had more money in the
game and returns remained anemic."* Oracle has **$129,647M of cloud capital deployed** (net PP&E
$99,957M + operating-lease ROU $29,690M) against **cloud infrastructure revenue of $18,101M.**
Apply the peers' own **disclosed** cloud margins to it:

| if OCI earned… | operating income | return on the $129,647M already deployed |
|---|---|---|
| Microsoft Intelligent Cloud's **41.35%** — best in the industry | $7,485M | **5.77%** |
| AWS's **35.43%** | $6,413M | **4.95%** |
| Google Cloud's **23.69%** | $4,288M | **3.31%** |

**Not one of them clears the 5.24% sovereign except by rounding, and none clears the 10% floor.
For OCI to earn 12% on the capital ALREADY deployed — before a dollar of the $260bn of leases
commences — its revenue must reach $37,624M, 2.08x today's, AND it must earn the best margin in
the industry. Oracle discloses no margin at all.**

**DEATH 3 — THE ANNUITY RUNS OFF WHILE THE CAPITAL IS BEING SPENT. [LIKELY — THE FILED SERIES
HAS ALREADY TURNED.]** Software licence revenue is **down 19.4% in four years**; support is
contractually *"priced as a percentage of the net fees paid by the customer to purchase a
software license"*; support was **−1% in constant currency in FY2026.** **A 3%-a-year decline
for a decade takes $19,804M to $14,604M — a $5,200M loss of the highest-margin revenue Oracle
has, 25.2% of FY2026 operating income — and it is the leg that funds everything else.**

**DEATH 4 — THE REFINANCING GRIND. [A LOW-LEVEL POSSIBILITY IN ANY ONE YEAR, A CERTAINTY OVER
THE BOOK'S LIFE.]** $130,105M was largely issued between 2016 and 2021 at an average effective
rate near 3.5%. **Repricing the whole book at 6% takes interest from $4,599M to $7,806M —
+$3,207M, 15.6% of FY2026 operating income.** $90,250M matures "thereafter", so this arrives
slowly, which is why it is a grind and not a rupture.

**WHAT DOES *NOT* KILL IT, STATED SO THE BEAR CASE IS NOT OVERSTATED:** a near-term default is
**not** a named death. Only $7,210M matures in fiscal 2027; the notes carry no financial
covenants; and Oracle could stop building tomorrow and harvest a $19.8bn annuity. **The death
here is not insolvency. It is [E4-20]'s bottomless pit: a company that grows, consumes capital
at 3.4% incremental returns, funds the consumption with debt and issued equity, and arrives in
2030 larger, more indebted and no more valuable.**

- Likelihood: [x] **a real possibility** for deaths 1 and 2 · [x] **likely** for death 3 ·
  [x] a low-level possibility for death 4.

- **VERDICT: [x] OUT.**

**THE REASONING, STATED SO IT CAN BE CHECKED RATHER THAN TRUSTED.** Q4 asks four things and
Oracle fails three of them on filed figures, none of which requires a view about AI demand:
1. **[E4-20] GRUESOME** — 3.4% incremental pre-tax return on ~$160bn deployed in five years,
   robust across every construction from 3.4% to 6.8%, against [E5-40]'s ~12%. *"Only the
   gruesome fails Q4."*
2. **[E5-11] strength (3) FAILS** — an ~$80.7bn twelve-month requirement against $63.9bn of
   liquid assets plus operating cash flow, before $260bn of leases begin commencing.
3. **[E2-54] coverage is NEGATIVE** — cash flow net of capital expenditure is −$23,686M against
   $4,599M of interest. The corpus's instruction at this reading is two words.
4. **[E5-39] is failed in Oracle's own MD&A** — the plan depends on *"available financing
   arrangements"* and *"potential access to additional financing."*

**WHY OUT AND NOT UNKNOWABLE [E4-25].** The range *is* enormous — $53bn wide on the single
year. **But width closes a file only when it straddles the decision, and this one straddles
nothing**: the single most generous construction obtainable (FY2026 depreciation-only, the
construction the framework calls INVALID, in the best year the company has ever had) yields
**4.227% against a 5.24% sovereign.** Every construction, on every window, at either end of the
band, pays less than a government bond. **The width is decision-irrelevant — the MSFT
adjudication — and the verdict rests on the incremental return and the near-term cash
requirement, both of which are single-valued facts, not ranges.**

**WHY OUT AND NOT "IN, THEN FAIL AT Q5 ON PRICE", WHICH IS WHAT MSFT, GOOGL AND AVGO DID.**
Those three passed [E5-11] strength (3): Microsoft's uncommenced leases are 1.80x its operating
cash flow, Broadcom's twelve-month fixed claims were covered **5.9x by cash alone with no
revolver counted**. **Oracle's uncommented leases are 8.13x its operating cash flow and its
coverage net of capex is negative.** The distinction is not a matter of degree in the same
direction; it is the difference between a company that could stop and a company that has
contracted not to.

**[E4-18] CHECKED: this verdict did not require fighting for it.** It did not need a narrowed
assumption, a chosen window, or a chosen end of the capex band. **It holds at every window and
at both ends.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — NOT REACHED. **Q4 RETURNED OUT AND THE FILE IS CLOSED.**

⛔ **Operator rule 2: no Q5 output may be reported unless Q1–Q4 each show IN. Q4 is OUT.**
The arithmetic below is published because the queue's output contract requires a price from
every run, and it carries the heading operator rule 3 requires.

---

# COMPUTATION — NOT A CLEARANCE

**This section contains no entry language and confers no clearance. It is arithmetic
published under the queue's output contract, not a Q5 verdict.**

**Sovereign 5.24%** (US Treasury 30-year par yield, 2026-09-04, issuing authority).
**Claim being priced: $462,341M** = 2,880,471,000 common shares × $158.78 (2026-09-04, Yahoo
aggregator, **flagged**) **plus** the $5,000M of 6.50% Series D Mandatory Convertible Preferred.
**Diluted for the mandatory conversion: ~2,908.6M shares.**

### EVERY CONSTRUCTION, EVERY WINDOW, BOTH ENDS OF THE BAND

| construction | owner earnings | yield | vs sovereign | perpetual growth needed for the ~10% floor **[E4-28]** |
|---|---|---|---|---|
| strict, FY2026 alone | −$33,443M | −7.233% | −12.47 pt | 17.23% |
| strict, 3-yr mean *(= screen `oe_bottom`)* | −$11,200M | −2.422% | −7.66 pt | 12.42% |
| **strict, 5-yr mean — the corpus default [E2-42]** | **−$5,252M** | **−1.136%** | **−6.38 pt** | **11.14%** |
| strict, 8-yr mean | +$860M | 0.186% | −5.05 pt | 9.81% |
| strict, 10-yr mean | +$2,968M | 0.642% | −4.60 pt | 9.36% |
| **JUDGED — forward build, ex the one-off prepayment** | **$5,100M** | **1.096%** | **−4.14 pt** | **8.90%** |
| JUDGED — forward build, generous end | $9,700M | 2.091% | −3.15 pt | 7.91% |
| D&A end, 5-yr mean | $9,544M | 2.064% | −3.18 pt | 7.94% |
| D&A end, 3-yr mean | $12,135M | 2.625% | −2.62 pt | 7.38% |
| depreciation end, 5-yr mean **[INVALID, E5-20]** | $11,888M | 2.571% | −2.67 pt | 7.43% |
| depreciation end, 3-yr mean *(= screen `oe_top`)* **[INVALID]** | $14,464M | 3.128% | −2.11 pt | 6.87% |
| **depreciation end, FY2026 alone — the single most generous number constructible [INVALID]** | **$19,543M** | **4.227%** | **−1.01 pt** | **5.77%** |

> **THERE IS NO CONSTRUCTION, ON ANY WINDOW, AT EITHER END OF THE CAPEX BAND — INCLUDING THE
> CONSTRUCTION THE FRAMEWORK CALLS INVALID, IN THE BEST YEAR THE COMPANY HAS EVER HAD — THAT
> PAYS WHAT A GOVERNMENT BOND PAYS. THE GAP RUNS FROM 1.01 TO 12.47 POINTS.**

**WHAT THE PRICE ALREADY ASSUMES, AGAINST WHAT THE BUSINESS HAS DONE.** To clear the [E4-28]
floor from the judged number Oracle must compound owner earnings at **8.90% in perpetuity**;
to be worth the price at the bare bond, **4.14% in perpetuity**. Its actual filed record over
ten years: revenue **+6.2%/yr**, operating income **+5.0%/yr**, owner earnings at the
depreciation end **+5.2%/yr**, and owner earnings at the strict end **from +$11,459M to
−$33,443M**. **The required rate sits at or above everything the business has delivered,
and it must now be delivered with capital intensity up from 1.37x depreciation to 7.30x.**

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01].** *(The DCF runs as an engine only and casts no
vote [E3-34]. Per share on 2,908.6M diluted.)*

| | judged $5,100M | generous $9,700M | INVALID end $19,543M |
|---|---|---|---|
| zero growth at the 10% floor | **~$17** | ~$33 | ~$67 |
| zero growth at the 5.24% sovereign | ~$33 | ~$63 | ~$128 |
| engine: 12%/10yr then 4%, discounted at 10% | ~$55 | ~$106 | ~$214 |
| engine: 15%/10yr then 4% — a rate **[E4-35]** says fewer than 10 of the 200 most profitable companies achieve | ~$70 | ~$133 | ~$268 |

**VALUE ≈ $30 to $130, centre ≈ $60.** *(Round numbers, as [E4-01] requires; the range spans
the judged number at the sovereign to the invalid construction at the sovereign, and
deliberately excludes the engine outputs, which cast no vote.)*

**CURRENT PRICE $158.78 — 2.6x the centre of that range, and above every construction except
the two engine outputs built on the number the framework calls INVALID.**

**Honest pre-tax expectancy at this price: ~1% to ~4%.** Against the ~10% floor **[E4-28]**
and a 5.24% sovereign. **Under a Q5 that had been reached, this would be quit on, not ranked.**

**WINDAGE COUNT: ONE, and it is spent AGAINST the flattering reading, not for it.**
Conservatism is applied at exactly one place — **[E4-41]'s removal of the $4,600M of
non-recurring customer prepayments from operating cash flow**, which Oracle's own footnote
says did not occur in FY2025 or FY2024 and on which it pays interest. **Two further
conservative adjustments were available and were DECLINED so conservatism is not stacked
[E4-11, E4-48]:** the $5,864M rise in accounts payable against $55.7bn of capex, and the
$1,900M of short-term financing of capital expenditure sitting in financing rather than
investing. **And the (c) judgment itself is NOT a windage application — $17,500M is the
MIDDLE of the band, derived from Oracle's own filed six-year server life; taking (c) at total
capex would have produced −$28,497M.**

**NEITHER BAR IS APPLIED, BECAUSE NEITHER IS REACHED.** Bar 2's three outcomes: the price is
**above the whole range** — outcome three. Bar 1's end margin is not computed, because a
margin is subtracted from a value the price must first approach, and it does not.

---

## Q6 — NOT REACHED. Q4 closed the file.

**No position is contemplated, so no exit yardstick is pre-committed [E1-02].** What follows
is a **re-look register**, written now so that a future re-opening is checkable against what
this run actually believed, rather than reconstructed afterwards.

**THE FILE RE-OPENS ON EVIDENCE, NOT ON PRICE — and the evidence is nameable:**

1. **A FILED OCI SEGMENT MARGIN.** Oracle reports three operating segments and OCI is inside
   one of them. **If Oracle begins filing cloud-infrastructure operating income or segment
   assets in a 10-K or 10-Q, the single largest UNKNOWABLE in this file becomes knowable and
   Q2 and Q4 both get re-run.** *(Pre-registered so it cannot be rationalised away later:
   this is the strongest bull trigger, and if the filed margin is at or above Microsoft's
   41.35% on a doubled revenue base, the Q4 verdict was wrong.)*
2. **CAPEX ROLLING OVER.** The MD&A commits to *"this upward trend"* continuing. **Capital
   expenditure falling toward the ~$17,500M steady-state build, with revenue holding, would
   convert this from gruesome to good in two years and is the cleanest possible refutation.**
3. **DEPRECIATION CONVERGING ON THE FORWARD BUILD.** Reported depreciation of $7,623M rising
   toward ~$17,500M is the arithmetic of the fleet switching on. **If revenue and operating
   income rise faster than that charge, the growth capital was real.**
4. **THE ANNUITY RE-ACCELERATING.** Software support has been flat five years and negative in
   constant currency. **Constant-currency support growth above 3%, together with the software
   licence line ceasing to fall, reverses Death 3.**

**THE BREAKERS, equally pre-registered:** RPO falling, or its 12-month conversion rate
dropping below 12%; any impairment charge against the data-centre fleet; the operating lease
liability continuing to compound at the FY2026 rate (13,450 → 30,190); **any drawing on the
$10.0bn revolver or the $10.0bn commercial paper programme**, which would confirm [E5-39];
the ATM programme being used; the common dividend being cut; the Ellison pledge rising above
400 million shares; or a credit-rating downgrade, which Oracle's own risk factors say could
*"affect the terms or availability of certain long-term commitments (including data center
leases)."*

**NEXT CATALYST DATES:** the **Q1 FY2027 10-Q, due approximately 2026-09-10** — four days
after this run, and the first document that will show whether $55.7bn of annual capex is the
new base or the peak; the **$3.3 billion lessor-borrowing guarantee maturing in September
2026**; the FY2027 proxy (~September 2026), which will file the co-CEO grants that the 2025
proxy left as narrative; and the **mandatory conversion of the preferred on 2029-01-15**.

**Position size: ZERO.** Not a judgment about the price — the file did not reach a price
question.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 IN → Q3 IN → **Q4 OUT →
      stop.** Q5 and Q6 are marked NOT REACHED and the arithmetic under them carries operator
      rule 3's heading and no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's moat
      class is NARROW, not PROVISIONAL — the competitor row was pulled, not deferred.
- [x] **Every UNKNOWABLE states what specifically cannot be known.** Three are recorded, all
      inside gates that resolved on other evidence: **(i) OCI's operating margin, assets and
      capex** — Oracle files three segments and OCI is inside one; no document on the filing
      rung supplies it; **(ii) any physical/unit series** — recorded sweep returns zero for
      ARR, annual recurring revenue, megawatts, gigawatts, data-centre count, cloud-region
      count, net retention, a numbered renewal rate and a customer count, in FY2019 as well as
      FY2026, so nothing was withdrawn and nothing was ever filed; **(iii) the return on the
      $27,721M paid for Cerner** — healthcare is not separately reported and no post-mortem
      has ever been published **[E4-39]**.
- [x] **No UNRESEARCHED verdict was written**, so no work order is outstanding.
- [x] **Step 0: the filing was read, with accession numbers; figures cross-checked against the
      filed statements**, not the XBRL — PP&E gross $122,651M and accumulated depreciation
      $(22,694)M reconciled to net $99,957M off Note 4; total borrowings $130,105M off Note 6;
      capex read in words off the MD&A (*"$21.2 billion … to $55.7 billion"*) and matched to
      the tag. Eight 10-K vintages diffed.
- [x] **Owner earnings on multi-year means; four windows shown (3/5/8/10-year) plus the single
      year; the capex band disclosed as a judgment and carried in full.** The blended mean is
      **explicitly refused** with the inflection dated to fiscal 2025 and the reason given.
- [x] **Competitor row filled** — six peers, all primary filings, accessions recorded, and the
      two cells that could not be obtained (IBM's operating income, SAP's PP&E-only capex) are
      **left empty and named**, not estimated.
- [x] **Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04.** FRED not used.
- [x] **Value stated as a round-number range** ($30–$130, centre ~$60), under the
      COMPUTATION heading, not as a point estimate.
- [x] **Neither bar applied, and the reason stated** (the price is above the whole range —
      Bar 2 outcome three; no Bar 1 margin computed, so the two are not stacked).
      **Windage count: ONE**, stated and justified.
- [x] **Prices dated; the aggregator is flagged as an aggregator** and used only for the live
      quote. The share count is hand-read off the cover.
- [x] Run committed to git, in five commits, one per question, under the WRITE-EARLY PROTOCOL.

**DECLARED DEFECTS IN THIS RUN — assume some, and here they are:**
1. **The Q1 FY2027 10-Q did not exist at run time** (due ~2026-09-10). The FY2026 10-K is the
   whole of the evidence and the file is three months and six days stale on the most volatile
   line in it. **This is the single largest limitation and it is four days from being fixed.**
2. **The buildings life in the forward build is MY judgment, not a filed number.** Oracle files
   "1 – 40 years" for the class. I used 25. **The sensitivity is disclosed and is 3.1%**, so it
   does not move the answer — but it is mine, and it is labelled **CONVENTION**.
3. **The split of capex between OCI and everything else is not filed.** I attribute
   substantially all of $55,663M to the cloud fleet on the strength of the MD&A's own words
   (*"primarily due to the expansion of our data centers"*) and Note 4's CIP footnote. **It is
   an inference from two disclosures, not a filed number.**
4. **The accrued-capex question is unresolved, exactly as it was in the MSFT run.** Accounts
   payable rose $5,864M in a $55.7bn capex year and the filing does not permit the
   reconciliation. Carried as a named sensitivity, not taken into the base. **A repeat defect
   in this queue.**
5. **The peer cloud margins used in Death 2 are the peers' own segment disclosures applied to
   Oracle's revenue.** That is a counterfactual, and it is labelled as one.
6. **The proxy's own Pay-Versus-Performance TSR column does not reconcile with the same
   proxy's CD&A** (+510% vs "up 130%"). Reported as filed; **not verified against the 10-K
   performance graph**, which would have settled it.
7. **The external say-on-pay support figures (63% / 44%) are my arithmetic** from the filed
   headline percentage and the filed insider block, labelled CONVENTION. Oracle files no vote
   counts.
8. **`acquisition_flag()` was not run as a tool**; the Cerner test was done by hand from the
   cash-flow statement ($27,721M in fiscal 2023, 6.0% of market cap, inside the window). The
   AVGO run established the guard is defective at this scale anyway.
9. **The applications-versus-database split of the support annuity is unobtainable after
   FY2025** because the ecosystem table was dropped. I could have reconstructed a partial
   series from FY2023–FY2025 and did not.

## REGISTER
- **Verdict: [x] OUT — about the business, at Q4.**
- **One line:** *Oracle is a real software annuity that has stopped growing, bolted to a
  data-centre business that has consumed roughly $160 billion of capital in five years for a
  3.4% incremental pre-tax return, funded with debt that now exceeds Microsoft's and
  Alphabet's combined on one-fifth of Microsoft's revenue — and the twelve-month cash
  requirement exceeds every source of cash the company has.*
- **PRICE (under COMPUTATION — NOT A CLEARANCE): value ≈ $30 to $130, centre ≈ $60, against a
  price of $158.78 on 2026-09-04.**
- **PASS / FAIL: FAIL. The file closed at Q4 (OUT), not at Q5 on price.** Q1 IN · Q2 IN
  (NARROW, narrowing) · Q3 IN (binary gate, no disqualifier found) · **Q4 OUT (GRUESOME;
  [E5-11] strength (3) failed; [E2-54] coverage negative).**
- **Not UNRESEARCHED:** no document was named and not obtained.
- **Not UNKNOWABLE:** the three named UNKNOWABLEs are real but sit inside gates that resolved
  on other evidence, and the owner-earnings width — enormous at $53bn on the single year — is
  **decision-irrelevant because it straddles nothing**: every construction, on every window,
  at either end of the band, yields less than the sovereign.
