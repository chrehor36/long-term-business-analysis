# Company Run — Abercrombie & Fitch Co. (ANF) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Queue context:** tier 2 of `Screens/WATCHLIST RUN QUEUE.md`. Screen row (corrected queue,
2026-09-02) — yield 3.78%, growth required 6.22%, spread **90.3%**, level_shift **"STEP UP —
normalize down [E4-41]"** — **REPRODUCED to the decimal** from cached companyfacts before
adjudicating: constructions 5y_capex **$247.8M** (bottom), 5y_D&A $271.2M, 3y_capex $427.9M,
3y_D&A $471.7M (top); 247.8/6,555 = 3.78% on the screen's cap. Two notes on the screen row,
recorded here rather than lost: **(1)** the queue CSV's level_shift ratio is 2.45; the same
function run on ALL eighteen filed years returns **3.94** (same verdict — the ratio depends
on how much history the caller feeds it); **(2)** `best_year_dependence()` reads 0.119 — "no
single-year dependence" — **and is structurally blind here, because the boom is a TWO-year
event** (FY2023 $455.5M, FY2024 $488.8M). Leave-one-out cannot see a two-year boom for the
same reason level_shift could not see a boundary step. The [E4-41] work is done by hand at Q4.

**Apparel-cohort precedents:** AEO (Q2 OUT), NKE (Q2 OUT), COLM (Q2 OUT), LEVI (Q1–Q4 IN,
Q5 UNKNOWABLE), DKS (Q2 OUT), ULTA (Q2 OUT). The attacker metric and the physical-series
tests are imported unchanged from the AEO/NKE runs.

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
  (issuing authority, via `tools/sources.py`)**
- FX: not needed — ANF reports and predominantly earns in USD (US 63.7% of FY2025 net sales,
  per the 10-K geographic note). No ADR.

**Stage 0 by hand:**
- **Share count off the 10-Q cover, hand-read from the primary document** (not dei): **Class A
  Common Stock, $0.01 par, 44,431,710 shares outstanding as of May 29, 2026** — 10-Q filed
  2026-06-05, accession 0001018840-26-000036. **Single class**; only Class A is registered
  (cover, Section 12(b) table). `cover_shares.py ANF` returns the same count — verified, not
  substituted. No warrants or listed senior claims.
- **Price $136.60**, Yahoo Finance quote as of 2026-09-02 16:00 ET — **aggregator, used for
  the live quote only, flagged as such** (operator rule 5). Context: $147.75 on 2026-08-26,
  the day the Q2 FY2026 8-K was filed; −7.5% since.
- **Market cap = 44,431,710 × $136.60 = $6,069M.** (The screen's $6,555M row was struck at
  ~$147.53; the cap moved 7% inside a week. All yields below are on the live cap.)
- **Dividend check: confirmed — ANF pays no dividend.** FY2025 cash-flow statement carries no
  dividend line; the FY2025 10-K Item 5 states no dividends paid in either of the two most
  recent fiscal years. (Last dividend was 2020; suspended, never resumed.)
- **Boom-window artifact check: the window IS the boom.** The screen's own bottom boundary
  (5y capex, FY2021–FY2025) contains FY2023–FY2024, the two best owner-earnings years in the
  filed record. Handled at Q4 under [E4-41].

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **10-K for fiscal 2025 (52 weeks ended 2026-01-31), filed
  2026-03-26, accession 0001018840-26-000012**; 10-Q for the thirteen weeks ended 2026-05-02,
  filed 2026-06-05, accession 0001018840-26-000036; Q2 FY2026 earnings 8-K filed 2026-08-26,
  accession 0001018840-26-000041 (Exhibit 99.1)
- figure cross-checked against the filed statement: **FY2025 net cash provided by operating
  activities $619.1M and capex $240.8M, read off the filed Consolidated Statements of Cash
  Flows, match the XBRL series used in the screen reproduction; FY2025 net sales $5,266.3M
  and operating income $699.1M match the filed Statements of Operations.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language:** ANF designs teen and
  young-adult casual clothing under two brand families (Abercrombie, for 20s–30s;
  Hollister, for teens), has it sewn by 124 third-party vendors in 15 countries (Vietnam
  37% and Cambodia 26% of FY2025 receipts), and sells it at roughly a 61.5% gross margin
  through 829 leased mall stores (5.3M gross sq ft, all leased, 1–10 year terms) and
  digital channels (the majority of Abercrombie-brand sales). Of each sales dollar in
  FY2025: 38.5¢ merchandise cost (including a $90M net tariff hit), 34.4¢ selling
  (occupancy, store payroll, marketing, fulfillment), 13.7¢ G&A, leaving 13.3¢ of
  operating profit (12.5¢ excluding a one-time litigation receipt). No customer owes it
  anything: every sale is re-won at the season's fashion cycle. Inventory turns fast by
  design ("test and chase"); the balance sheet is cash-rich and debt-free.
- **The scarce input this business controls:** honestly — none that is durable. The two
  trademarks are owned, but the record (Q2, below) shows the trademarks alone earned
  1–13% on operating assets for five straight years, then 47–83% under the same
  registrant once merchandising caught the customer again. The operative scarce input is
  **brand heat and merchandise judgment**, which resides in the team, not the company —
  recorded here and carried to Q2 as [E4-23] key-person exposure, not held against
  understanding.
- **Will the fundamentals look broadly the same in ten years?** The model — design,
  outsource, retail at a brand markup through stores plus digital — yes; it is one of the
  oldest models in retail. The *economics* of any single fashion brand are subject to
  constant re-choice by the customer; that instability is the Q2 question, and the cohort
  precedent (AEO, NKE, COLM, LEVI) is that it belongs there, not here.
- **VERDICT: [x] IN.** Simple to describe, filings complete, unit economics computable
  from the filed statements. Understanding is not the hurdle for this name.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The prior most likely to be wrong is the Q2-OUT prior, so the disconfirming case is built
first, at full strength [E4-26, E4-51]. The apparel cohort is 0-for-6 at this gate; ORLY
just showed a streak can end when the counter-case is taken seriously. This one was.**

### THE CASE FOR ANF AS A FRANCHISE — stated as its holders would state it **[E4-51]**

1. **It earns the highest return on unleveraged net tangible operating assets [E2-43] of
   any mall-apparel filer in the row — 66.9% — above Lululemon (61.5%), double Gap and
   Urban Outfitters, 4.4x American Eagle**, on the identical formula both sides, and it has
   held above 60% for three consecutive years (61.4% → 83.1% → 66.9%).
2. **The deflated physical series ACQUITS, decisively.** Real (CPI-U) sales per gross
   square foot rose ~52% over the decade FY2015→FY2025 and ~37% even from the pre-boom
   FY2019 base; real sales per store rose ~24% and ~19% on the same comparisons. This is
   the instrument that convicted DG, Foot Locker and UAL. It does not convict ANF —
   **the fifth acquittal** (AEO, ULTA, DICK'S, ORLY, now ANF).
3. **Two banners, and when one cools the other has carried**: Hollister +13% comps in
   FY2025 while Abercrombie was −7%; Abercrombie +4% comps in Q2 FY2026 while Hollister
   was −3%. Q2 FY2026 was a record quarter for BOTH brands; the company has grown net
   sales fifteen consecutive quarters.
4. **Pricing conduct is live, not theoretical**: AUR GREW low-single-digit in FY2025 and
   again in Q1 FY2026 *"driven by selected changes to tickets"* — ticket increases taken
   under a $90M tariff hit, with unit volume still growing mid-single-digit in FY2025.
5. **The balance sheet is the cleanest in the cohort**: zero funded debt (8.75% notes
   redeemed July 2024), $784.6M of cash and securities, an undrawn $500M ABL, and
   buybacks executed at $83–88 average against a $136.60 quote.
6. **Gross margin is at record levels** — 64.2% (FY2024), 61.5% (FY2025 after absorbing
   170bp of tariffs) — achieved with inventory flat year-over-year against +6% sales.

**Every number above is filing-sourced and none is withdrawn below. What follows disputes
none of it. It disputes that these facts establish a franchise under [E3-03], which is a
narrower claim.**

### [E3-03], the three criteria
- **(1) Needed or desired — [x] YES.** Clothing for teens and young adults, bought
  repeatedly.
- **(2) Thought by its customers to have NO CLOSE SUBSTITUTE — [ ] FAILS.** The filer's
  own Item 1 (FY2025 10-K, verbatim): *"The Company operates in a rapidly evolving and
  highly competitive retail business environment. Competitors include individual and chain
  specialty apparel retailers; local, regional, national and global department stores;
  discount stores, fast fashion, value fashion and off-price retailers; social commerce;
  and digitally-native brands and online-exclusive businesses."* And the same Item 1 names
  the mechanism: *"Operating in a highly competitive industry environment can cause the
  Company to engage in greater than expected promotional activity, which would result in
  pressure on average unit retail and profitability."* One honest difference from AEO is
  recorded: ANF's competitive-basis sentence does **not** end in "price" — it claims
  differentiation on *"product… high quality and newness; brand voice… and experience."*
  But "newness" is the confession in one word: a moat that must be re-earned **every
  season** is [E4-04]'s continuously-rebuilt moat by the company's own description. The
  customer re-chooses at zero cost, every season, exactly as in the six cohort files
  before this one.
- **(3) Not subject to price regulation — [x] YES.**

**One of three, and the one that fails is the criterion.**

### THE DECIDING ARITHMETIC — the same trademarks, across their own cycle **[E2-53, E3-46]**

**[E2-53]'s dominance test — "Once dominant… Good or bad, it will prosper" — asks whether
POSITION, not execution, sets the economics. ANF's own filed record is the direct
refutation, and it is the sharpest single fact in this file:**

| return on unleveraged net tangible operating assets [E2-43] | FY2015 | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| same formula as the peer row | 6.1% | **1.3%** | 6.7% | 13.0% | 7.3% | (2.7)% | 47.1% | **10.3%** | 61.4% | **83.1%** | 66.9% |

The SAME two trademarks, the SAME registrant, the SAME malls: **1.3% in FY2016, 83.1% in
FY2024**. Position carried nothing across those nine years; merchandising execution and a
brand-heat wave carried everything. [E3-46] asks for *"very high returns on capital
employed **over time**"* — this series fails the "over time" half exactly as NIKE's did,
in the opposite direction. Note also FY2022: even INSIDE the current management's tenure,
one bad inventory year (freight, over-buy) took the return from 47.1% to 10.3% and owner
earnings to **negative $196M**. A franchise does not swing to a loss on one season's
inventory misjudgment; a fashion retailer does.

**The company's own longer history supplies the base rate for what follows an ANF boom:**
owner earnings peaked at $291M in FY2012 (the last boom) and were **negative $42M the
following year**; the FY2012 revenue peak ($4.51bn) was not seen again for eleven years.
Of [E4-36]'s four causes of extreme success, this record is **wave-riding [E3-51]** plus
extreme execution — *"the advantage lives in the wave, not the surfer"* — and the surfer
has already wiped out once on this exact beach.

**[E4-23] key-person: the results require the merchant team.** CEO Fran Horowitz (2017–)
executed the turnaround; the strategy documents are execution language throughout
("testing and chase," brand playbooks). Recorded HERE as a moat defect, not at Q3 as a
strength: *"the moat will go when the surgeon goes."*

### THE PRICING TEST **[E2-44, E4-37]** — mixed, and the mix is the answer
- AUR rose low-single-digit in FY2025 and Q1 FY2026 (ticket changes) — a real pass at the
  margin, better than NKE (whose ASP fell) or DKS (promotional retreat).
- **But the margin did not hold**: cost of sales rose 270bp (tariffs 170bp of it) against
  only low-single-digit AUR growth; adjusted operating margin fell **15.0% → 12.5%**, and
  FY2026's underlying guide (ex-refunds) is ~12.3–12.8%. All three segment margins fell in
  FY2025 (Americas 30.1→27.7%, EMEA 14.3→11.2%, APAC to a **(17.5)%** loss). A franchise
  passes a cost shock to the customer [E2-44]; ANF split it with the customer and ate the
  difference in margin. And the "targeted promotions" language plus the Item 1 promotional
  sentence is [E4-37]'s agony, in the filing's own words.
- **Untapped pricing power [E3-33, E5-28]: NOT CLAIMED.** Claiming it would claim
  near-monopoly in teen apparel; nothing in the filings supports it and the tariff
  pass-through record contradicts it.

### THE PHYSICAL SERIES **[E4-55]** — reported as it fell, both halves
**The deflated series acquits (case-FOR item 2), with two confounds stated:** (1) the
denominator shrank 30% — gross sq ft went 7,292k (FY2015) → 4,980k (FY2023) before
regrowing to 5,300k — so a survivor fleet of the best locations lifts the ratio; (2) the
numerator includes digital, which grew to a large share (majority of Abercrombie-brand
sales) without adding square feet. The store-only series ANF used to publish ran **$343–
$381 flat from FY2014–FY2019** and was then discontinued. Even so: nominal sales per sq
ft $483 → $994 and per store $3.78M → $6.35M over the decade clear CPI by wide margins on
every construction, including from the pre-boom FY2019 base. **The DG instrument does not
convict.**

**[E4-55] units — the absence is a finding (the COLM ruling), and here it is confessed:**
the FY2025 10-K's KPI list names *"transactional metrics, such as traffic and conversion…
AUR, average unit cost… average units per transaction"* and then states: *"not all of
these metrics are disclosed publicly by the Company due to the proprietary nature of the
information."* **No unit count, transaction count, or AUR number appears anywhere in the
filings** — only qualitative direction in MD&A ("mid-single-digit unit volume growth,"
FY2025 — recorded as a credit: the direction is at least given, and it is currently
positive). ANF's FY2016 10-K named *"average number of transactions per store"* as a KPI;
that named metric left the list by FY2019 and never returned.

**[E2-49] metric-switching, dated:** *"Net store sales per average gross square foot"* was
published through the FY2019 10-K and not after — the honest caveat is that the SEC
abolished Item 6 selected data in 2021, so the table's death is partly regulatory. But
**"store metrics, such as net sales per gross square foot" remained on the company's own
KPI list through the FY2024 10-K and was deleted from it in the FY2025 10-K** — the year
square footage began growing again and Abercrombie comps went negative. And **EBITDA
entered the same 10-K series in FY2024** (zero occurrences in FY2021–FY2023 10-Ks; a full
EBITDA/adjusted-EBITDA reconciliation with 10 occurrences in the Q2 FY2026 release) — a
flattering metric ADDED at the margin peak. Both fire as prompts; the EBITDA read is at
Q3.

### THE COMPETITOR ROW — required **[E3-28]**

**Peers: 4 SEC registrants on identical formulas (numerator operating income; denominator
net PP&E + inventories + trade receivables − trade payables; all from each filer's own
10-K/companyfacts, FY ending Jan/Feb 2026), plus the brand-layer row imported unchanged
from the NKE run, plus the named unavailables.**

| latest fiscal year | **ANF** | LULU | GPS | URBN | AEO |
|---|---|---|---|---|---|
| Revenue ($M) | 5,266.3 | 11,102.6 | 15,366.0 | 6,165.4 | 5,547.2 |
| Operating margin | **13.3% — 2nd** | **19.9% — 1st** | 7.3% | 9.8% | 4.1% |
| Return on unlev. net tangible op. assets [E2-43] | **66.9% — 1st** | 61.5% | 32.2% | 31.3% | 15.1% |
| Same, operating leases capitalised | 31.6% | **41.0% — 1st** | 14.7% | 19.2% | 7.1% |
| Funded debt | **$0** | $0 | $1,492M | $0 | $0 |

Brand layer (NKE run, 2026-09-02, same formula): **Deckers 166.3%, On 52.4%, NIKE 26.3%.**
ANF sits between Lululemon and On — elite current economics, in a row where the FY2021
leader (NIKE, 51.7%) is now 4th of 7. **The row's own lesson is that leadership in this
metric has not persisted for anyone in this industry.**

- **Peers named: 4 of the industry's real competitor set obtained from primary filings;
  the industry's actual set is far larger and mostly unfilable** — H&M (Stockholm), Inditex/
  Zara (CNMV), Fast Retailing/Uniqlo (Tokyo): exchange-filing rung, not pulled this
  session; **Shein: private — no primary filing exists at any rung (UNKNOWABLE, not
  UNRESEARCHED)**; Walmart/Target/Amazon/TJX do not segment apparel. Under the template
  rule this would hold the moat class **PROVISIONAL — except the class is NONE on the
  subject's own Item 1 and its own return series, regardless of what any unpulled peer
  filed.** The limit is recorded, not papered over; [E3-61] governs: the row shows
  position, never conduct.

**[E2-45] the attacker's test — how would I compete with ample capital and skilled
personnel?** The answer is running: fast-fashion and **social commerce** (Shein's channel,
named by category in ANF's own Item 1) attack the teen customer with zero store capital, a
two-week design cycle against ANF's season, and an algorithmic feed where ANF's customer
already lives. Amazon attacks the basics layer. ANF's Hollister banner sells to the most
Shein-exposed cohort in retail, and its comps went **negative (−3%) in Q2 FY2026**. ANF's
defence — brand heat plus chase speed — is real and currently winning at Abercrombie, but
it is a defence that must be re-won each season [E4-04]; the attacker's cost of entry is
a design team and a TikTok budget. Contrast ORLY, where the attack was tried and died.

### Direction **[E4-32]** — the moat's own trend, axis by axis
| axis | direction | evidence |
|---|---|---|
| Return on operating assets | **NARROWING** | 83.1% (FY2024) → 66.9% (FY2025) |
| Operating margin | **NARROWING** | adj. 15.0% → 12.5% → ~12.3–12.8% underlying guided |
| Comps | **NARROWING** | +17% (FY2024) → +3% (FY2025) → −1% (Q1 FY26) → flat (Q2 FY26) |
| Abercrombie banner | mixed | −7% comps FY2025, +4% Q2 FY2026 |
| Hollister banner | **NARROWING** | +13% FY2025 → −2% Q1 → −3% Q2 FY2026 |
| Physical productivity | **WIDENING** | real sales/sq ft positive every construction |
| Pricing conduct | mixed | AUR up; margin down 250bp; "targeted promotions" |
| Segment breadth | **NARROWING** | EMEA comps 0% then −11%/−4%; APAC at a (17.5)% loss, under strategic review |

- Class: **[x] NONE** · Direction: **NARROWING on the majority of axes, from a very high
  level**
- **VERDICT: [x] OUT.** [E3-03] criterion (2) fails on the filer's own Item 1 and on the
  deciding arithmetic: the same trademarks earned 1.3%–13% for five years, then 47–83%,
  with one negative-$196M year inside the boom — position never set these economics;
  merchandising execution and a wave did [E3-51]. The 66.9% is real, it is 1st in the row,
  and [E2-53] read honestly says it belongs to the ride, not the castle. **This is a
  superbly run fashion cycle, not a franchise — the COLM language holds: management
  "capitalized on" a trend; that is not pricing power.** OUT is about the business class,
  permanent, and price does not repair it [E5-35].

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*
**THE FILE IS CLOSED AT Q2. Q3 is recorded, not a gate, and promotes nothing [E2-37].**

**STEP 1 — WEIGHT CASE:**
- [x] **Daily execution [E3-38]** — fashion merchandising is have-to-be-smart-every-day in
  its purest form; the FY2022 season (one inventory misjudgment → −$196M owner earnings)
  is the demonstration. Q3 would be a **BINARY GATE** here had the run continued.
- [ ] Control — no; liquid NYSE listing. · [ ] Leverage — no; zero funded debt.

**Honesty — binary, permanent, filings-based [E5-16], each matter dated to when public:**
the era of former CEO Michael Jeffries (1992–2014) produced conduct allegations (public
October 2023, BBC investigation) and criminal charges against Jeffries personally (public
October 2024) for conduct during his tenure. **The current team (Horowitz, CEO 2017–) is
two management generations removed and is not implicated in any filing read.** The FY2025
10-K's contingencies note names no quantifiable accrued matter. On the team actually
running the company: **no disqualifier found** — which is the absence of found
disqualifiers, not a finding of honesty [E5-17].

**STEP 2 — THE FLAGS:**
- [ ] weak accounting — not fired. PwC (auditor since 1996), clean ICFR opinion, SBC
  expensed, no pension.
- [ ] unintelligible footnotes — not fired; the statements are plainly written.
- [x] **trumpeted projections** — fires as a practice: quarterly and annual guidance on
  five-plus lines, updated seasonally, a Long-Term "Always Forward Plan" with targets the
  company itself notes it outperformed. [E5-30]'s ratchet is live. The [E3-48] check runs
  the other way, though: the May 2026 outlook (Q2 op margin "around 10%", EPS $1.80–2.00)
  was beaten ex-refunds (12.1%, ~$2.42) — guidance has recently been set low and beaten,
  not missed.
- [ ] serial share issuance [E5-15] — the reverse: count 47.6M → 44.4M inside eighteen
  months.
- [x] **EBITDA promotion [E4-29] — FIRES, dated.** Zero occurrences of "EBITDA" in the
  FY2021–FY2023 10-Ks; an EBITDA/adjusted-EBITDA reconciliation **appears first in the
  FY2024 10-K (the peak-margin year)**, is on the FY2025 KPI list, and runs to 10
  occurrences in the Q2 FY2026 release — justified verbatim by *"excluding the impact of
  differences in… debt service levels and capital investment"* on a company with **no debt
  service** and capex at 1.55x D&A. The one mitigant, recorded: **pay does NOT run on
  EBITDA** — incentives run on Adjusted EBIT, which keeps depreciation in.
- [ ] filed-figure tells [E4-30] — not fired. Cash taxes/pretax: 27.1% (FY2023), 28.3%
  (FY2024), 26.5% (FY2025) against a 28.5% book rate — no falling pattern. Reported
  operating income runs 72.8, 15.2, 72.0, 127.4, 70.1, (20.5), 343.1, 92.6, 484.7, 740.8,
  699.1 ($M, FY2015–FY2025) — nothing smooth about it.
- [x] **metric-switching [E2-49]** — the Q2 findings restated: per-square-foot store
  metrics deleted from the KPI list in FY2025 after eight years; the numeric series ended
  with FY2019 (Item 6 abolition the partial cause); EBITDA added FY2024.

**STEP 3 — THE PRIMARY TEST [E2-01]** — return on average equity, FY2016–FY2025, computed
from the filed equity series: 0.3%, 0.6%, 6.4%, 3.9%, (12.8)%, 30.3%, 0.4%, 34.5%, 43.8%,
**37.3%** *(net income ÷ average stockholders' equity; buybacks have shrunk equity,
flattering the recent years — the [E2-43] denominator at Q2 is the honest one and shows
the same shape)*. Mean of the ten: **14.5%**; mean of the first five: **(0.3)%**. The
series IS the Q2 verdict.

**Half-owner test [E2-26]: passes in the main.** The litigation settlement was quantified
separately at every line it touched (selling expense, G&A legal fees, EBITDA bridge, and
in the proxy's incentive-EBIT — where the committee **excluded the windfall against the
executives' interest**); the tariff impact was given in dollars and basis points; segment
tables are complete with cost detail. The material gap remains the [E4-55] transactional
data, withheld as "proprietary."

**Institutional imperative [E2-30]:** (1) resists change — no; the record is the
opposite (fleet cut 30%, flagships closed, ERP replaced, APAC put under strategic review
rather than defended). (2) projects to soak up funds — no; capex is ~4.6% of revenue and
excess cash goes to buybacks. (3) staff studies — not evidenced. (4) peer imitation —
partial: the EBITDA adoption and guidance culture are industry-standard behavior. Score:
one partial of four.

**Capital allocation — the two buyback conditions [E5-08], and this is the strongest Q3
section in the apparel cohort:**
- (1) ample funds: yes — $785M liquid, no debt, $1.2bn liquidity, after funding capex.
- (2) material discount to conservatively calculated IV: **the record says yes,
  behaviorally.** FY2024: 1.6M shares at ~$144. FY2025: **5.4M shares at ~$83** — the
  pace TRIPLED when the price halved. H1 FY2026: 3.2M at ~$88 (7% of the company in six
  months), guided to ≥$500M for the year. Purchases at $83–88 sit at the conservative end
  of this run's own sovereign-rate value band ($85–145, below) and below the $136.60
  quote. **This is the inverse of the ORLY condition-2 flag: a program run to price, not
  to a dollar budget.** [E4-31]'s third condition (an informed register): comps, brand
  sales, and segment data are published quarterly; the withheld transactional metrics cut
  against it slightly.
- Pay-versus-performance, the DG/ULTA test — **does NOT replicate, and the contrast is
  worth recording**: the FY2025 Adjusted-EBIT targets (Spring $355M + Fall $500M at
  target) were set ~15% ABOVE FY2024's $741M actual; Spring missed threshold and paid
  **zero** on that tranche; the year paid **49% of target** in a year net income fell 10%
  and the stock fell 18%. One flag inside it: the committee added back **$75M of tariff
  expense** to incentive EBIT (execs paid as if the tariffs had not happened) while
  excluding the litigation windfall — one adjustment in each direction, both disclosed
  line-by-line. The FY2023–25 PSAs vested at 200% because the boom blew through scales
  set in March 2023 — boom-cycle pay, but pre-set, long-lived bullseyes [E2-49].

**THE GUARDRAIL:** [x] confirmed — nothing here promotes the name; the key-person
dependence is recorded at Q2 as a moat defect [E4-23], and the manager IS the plan, which
is [E2-36]'s disqualifying branch, not its excisable-cancer branch.

- **VERDICT (recorded, not a gate): IN — no disqualifier found on the current team.**
  Two flags fire (EBITDA adoption, dated; guidance culture) and are read, not scored.
  The capital-allocation record is the best in the six-name apparel cohort. **IN never
  promotes: a remarkable jockey, and Q2 already ruled on the horse [E2-38].**

## Q4 — WILL IT SURVIVE?
**THE FILE IS CLOSED AT Q2. Q4 is recorded, not a gate — it exists to feed the required
price computation and the boom-question record.**

### Owner earnings — the one number **[E2-23]**, built back to FY2016 as instructed

**By year (OCF − SBC − capex, the CONVENTION; $M; ANF fiscal labels, FY2025 = year ended
2026-01-31):**

| | FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|
| capex end | 21.6 | 156.6 | 178.8 | 83.9 | 284.3 | 151.5 | **(195.9)** | 455.5 | 488.8 | 339.3 |
| D&A end | (32.9) | 69.0 | 153.1 | 113.1 | 219.0 | 104.4 | (163.6) | 472.2 | 517.9 | 425.1 |

**The windows [E4-25] — every one published, none defended:**
| window | capex end | D&A end |
|---|---|---|
| 3y FY2023–25 (the boom) | 427.9 | 471.7 |
| 5y FY2021–25 (screen's) | **247.8** | 271.2 |
| 7y FY2019–25 | 229.6 | 241.2 |
| 10y FY2016–25 | 196.4 | 187.7 |
| pre-boom 4y FY2016–19 | 110.2 | 75.6 |

- **Spread: 90.3% on the screen's four constructions; 110.2–471.7 across all published
  windows — the width IS a finding [E4-25], and the distorted years are named**: FY2022
  (freight/inventory bust, OCF −$2.3M), FY2020 (pandemic: capex halved, rent abated), and
  FY2023–24 (the boom: brand-heat surge plus the freight/input-cost collapse tailwind).
- **THE [E4-41] NORMALIZATION — the boom question, worked by hand:**
  - The 3-year window 427.9/471.7 is **REJECTED as a perpetuity base**: it is two boom
    years plus FY2025, sits 2.2x the ten-year mean, and the screen's own STEP UP flag
    fired. The ETD/FLO/ASIX lesson applies as written.
  - Favourable breaks stripped from the current level: the **$38.6M litigation receipt**
    inside FY2025 GAAP (one-time, quantified by the filer) → FY2025 ex-item ≈ **$300M**;
    the **~$100M IEEPA tariff refund** inside FY2026 H1 and ~220bp inside FY2026 guided
    margin (one-time by construction — a refund of prior years' costs).
  - Adverse break NOT credited back (all nine innings count [E2-57]): FY2025 carries a
    $90M net tariff hit; the post-IEEPA regime (10% Section 122 global tariff, subsequent-
    events note) may cost less — noted, not added.
  - `best_year_dependence()` read 0.119 ("no single-year dependence") and is **structurally
    blind here**: the boom is a two-year event; leave-one-out cannot see it. Recorded as a
    tool finding.
  - **Judged owner-earnings band: $250M–$340M, judged central ≈ $300M** — FY2025 ex-item
    at total capex, corroborated by the 5y capex mean ($248M) below it and the FY2026
    ex-refund run-rate (~$300–360M) above it. The 10y mean ($196M) is carried as the
    through-cycle floor: it averages the pre-turnaround company and is arguably a
    different business (fleet −30%, cost base rebuilt) — stated as a judgment, not
    resolved by preference.
- **Maintenance capex (c) — a DISCLOSED JUDGMENT:** capex/D&A 1.55x (FY2025), guided
  ~$250M FY2026 vs ~$155M D&A. Not the [E5-20] exception class — the filing never says
  D&A understates renewal, and the excess buys units (62 new stores FY2025). **But in
  fashion retail the remodel cycle IS competitive maintenance** ("experience" is the
  stated basis of competition; 47 remodels + 11 right-sizes FY2025), so the honest (c)
  sits **between D&A and total capex, nearer capex**; both ends published above, and the
  judged band uses total capex — one place conservatism is spent, counted at Q5.
- Stock compensation subtracted in full, $39.0M FY2025 [E5-06]. Working capital: inside
  OCF by construction (weighted-average cost inventory, not LIFO — the carve-out does not
  apply).

### Great, good, or gruesome? **[E4-20]**
- **Today it computes as great** (66.9% on tangible operating assets, modest capital);
  **across its own cycle it is a GOOD business at best** — the ten-year owner-earnings
  mean ($196M) against the ten-year average operating-asset base (~$900M) is ~22%
  pre-tax, earned with violent interruptions. The gruesome label does not fit: it does
  not eat capital. The [E4-20] savings-account rate is attractive but NOT reliably
  "earned also on deposits that are added" — added capital earns whatever the fashion
  cycle pays that year.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream: **large now, NOT reliable** — OCF was negative $2.3M in
  FY2022 and net income −$114M in FY2020; two zero-or-worse years inside six.
- (2) massive liquid assets: **passes** — $784.6M cash + securities (13% of the market
  cap), $245M of it offshore but repatriable at insignificant tax (filer's statement).
  The $500M ABL is NOT counted [E5-39].
- (3) no significant near-term cash requirements: **passes — the cleanest (3) in the
  cohort.** Zero funded debt (8.75% notes redeemed 2024-07-15), no maturities, leases
  $312M due <1yr (operating, inside the P&L), purchase obligations $406.5M <1yr (ordinary-
  course inventory), buyback fully discretionary. Total <1yr calls $731M vs $785M liquid
  before a dollar of the year's ~$600M OCF.
- Leverage, named and quantified: **funded debt $0; operating lease liabilities $1,168M
  ($1,422M undiscounted); net interest INCOME $21.6M.** [E2-54] coverage: no interest to
  cover. The leases are the leverage, and they are covenant-free and store-matched.
- **The company survives its cycles — that is the filed record (it survived 2016–2019 at
  a ~0% ROE and FY2020 at −$114M without distress). What does not survive the cycle is
  the earnings level.**

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]** — exposure, not experience
- **The mechanism: brand-heat reversion on a fixed occupancy base — the company's own
  2012→2016 sequence.** Owner earnings peaked at $291M in FY2012, went NEGATIVE the next
  year, and the revenue peak took eleven years to re-attain. Fashion demand re-chooses;
  $533M of store occupancy and a rebuilt 829-store fleet do not.
- **Quantified from filed figures:** both banners reverting to modest decline (comps −10%
  cumulative over two years, gross margin −300bp to ~58.5% on promotional defence — HALF
  the 2013–16 severity) on today's cost base: revenue ~$4.7bn, gross profit ~$2.77bn,
  selling+G&A sticky at ~$2.5bn → operating income ~$250M → owner earnings ~$100–150M —
  the pre-boom level. At this run's own floor arithmetic that is a ~$1.5–2.5bn business
  against a $6.1bn quote. Hollister's −3% Q2 comps and Abercrombie's −7% FY2025 comps
  show each banner has already had its first negative season inside the last 18 months.
- Likelihood: **[x] a real possibility** — it is the base rate of this company's own
  fifty-year record, twice realized (post-1999, post-2012).
- Insolvency proper: a **low-level possibility** only — no debt, cash-rich; the equity
  derates, the company does not die.
- **VERDICT (recorded, not a gate): IN on survival of the company; the earnings LEVEL
  carries the [E4-41] discount above, and the wide spread is itself the Q4 finding.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN. Q2 is OUT — Q5 does not open.** What
follows is the queue's required price output, under operator rule 3's heading, and it
carries no entry language.

---
## COMPUTATION — NOT A CLEARANCE

*Inputs: judged owner-earnings band $250–340M (judged $300M) per Q4's [E4-41] work; the
5y-capex screen bottom $247.8M and 10y mean $196.4M as conservative anchors; the 3y boom
window $427.9M shown and REJECTED as a base. Cap $6,069M (44,431,710 × $136.60,
2026-09-02). Sovereign 5.27%, bare rate, no per-name premium [E3-42].*

**1. THE YIELD** — owner earnings ÷ market cap, beside the sovereign:
| construction | OE ($M) | yield | vs 5.27% bond |
|---|---|---|---|
| 10y mean | 196.4 | 3.24% | −2.03 pts |
| 5y capex (screen bottom) | 247.8 | 4.08% | −1.19 pts |
| **judged, [E4-41]-normalized** | **300** | **4.94%** | **−0.33 pts** |
| FY2025 as filed | 339.3 | 5.59% | +0.32 pts |
| 3y boom window — rejected [E4-41] | 427.9 | 7.05% | +1.78 pts |

**Every honest construction sits at or below the bond; only the rejected boom window
clears it, and nothing clears the [E4-28] floor.**

**2. WHAT THE PRICE ALREADY ASSUMES:** to merely match the bond from the judged level the
price needs ~+0.3–1.2% perpetual growth — roughly fair against the bond on boom-adjusted
earnings. To reach the ~10% floor it needs **~+5.1% perpetual** (screen said 6.22% on its
bottom construction — reproduced). What the business has actually done across its own full
cycle: owner earnings FY2012 peak $291M → FY2025 $339M ≈ **+1.2%/yr peak-to-peak**;
revenue +4.7%/yr over ten years; the boom CAGRs are the wave, not the trend.

**3. WHAT YOU ARE PAID:** −0.3 points versus the sovereign at the judged level; honest
pre-tax expectancy **3.2%–5.6%** (7.05% only on the construction [E4-41] forbids). **Below
the ~10% quit figure on every honest construction: quit on, not ranked [E4-28].**

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:**
- **Zero-growth at the bare sovereign: roughly $85–145/share** ($85 at the 10y mean, $105
  at the screen bottom, ~$130 judged, $145 at FY2025 as filed; the rejected boom window
  would say ~$185).
- **At the [E4-28] ~10% floor: roughly $55–75/share.**
- **Current price $136.60** — inside the sovereign-rate range, in its upper half: **Bar
  2's middle outcome — no useful conclusion at the bond; far above the whole floor band.**
- Bar: **Screamer test [E4-01]** (the file is closed; no margin arithmetic is owed). Price
  does not clear the conservative case — not remotely.
- **Windage count: ONE** — (c) judged at total capex inside the judged band. The [E4-41]
  boom rejection is not windage; it is the removal of a favourable break the corpus
  requires before the mean is trusted.

**The price line the queue requires:** at $136.60 the market is paying ~20x the judged
boom-adjusted owner earnings of a no-moat fashion retailer whose margin is already
receding (adjusted 15.0% → 12.5% → ~12.5% guided ex-refunds), i.e. it prices the 2023–25
level as permanent plus a little growth. The corrected screen row (3.78% yield, 6.22%
growth required, STEP UP) said exactly this from orbit; the filings confirm it from the
ground.

## Q6 — DOES NOT OPEN. The file closed at Q2.
For the watchlist's standing monitor (not an entry trigger): the fact that would most
challenge this file's verdict is **five more years of both-banner comps positive and
returns held above 40% on [E2-43] through a full fashion cycle** — that would be evidence
of position, not wave. The re-read band is **$55–75** (floor arithmetic on judged OE),
where the price would pay ~10% on boom-adjusted earnings and the Q2 verdict would still
have to be re-argued on its merits, not waved through.

---
## SELF-AUDIT
- [x] Questions answered in order; Q1 IN, Q2 OUT closed the file; Q3/Q4 recorded as
  non-gates; the price reported under COMPUTATION — NOT A CLEARANCE per the queue contract
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q2's
  peer-row gaps (H&M, Inditex, Fast Retailing, Shein) are recorded with their rungs, and
  the verdict does not rest on them: it rests on the subject's own Item 1 and return series
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: FY2025 10-K read (MD&A, cash-flow detail lines, footnotes), accession
  0001018840-26-000012; OCF/capex/net sales/operating income cross-checked filed-vs-XBRL
- [x] Owner earnings on multi-year means; five windows published; (c) disclosed as a
  judgment with both ends shown
- [x] Competitor row: 4 registrants on identical formulas + brand layer from the NKE run;
  unavailable peers named with rung and obstacle
- [x] Sovereign 5.27% USD, US Treasury daily par curve (issuing authority), 2026-09-01
- [x] Value as round-number ranges ($85–145 sovereign; $55–75 floor)
- [x] One bar (screamer); windage count one, stated
- [x] Price $136.60 dated 2026-09-02, Yahoo aggregator, flagged, live quote only
- [x] Run committed to git after Q2 and at close

**Tool/brief findings recorded for the maintainers:**
1. **`best_year_dependence()` is structurally blind to two-year booms** — it read 0.119
   ("no single-year dependence") on a series whose 5-year window is carried by FY2023+
   FY2024 jointly. A leave-TWO-out (or leave-k-out) variant would catch the ETD/FLO/ASIX/
   ANF shape; today only `level_shift()` catches it, and only when the boom sits at the
   window boundary.
2. The queue CSV's level_shift ratio (2.45) and the same function on all filed years
   (3.94) differ because the caller controls the history — worth pinning the input window
   in `regen_queue.py` so the number is reproducible.
3. The brief's "two distinct banners both comping positive" disconfirming case was STALE
   at run time: Hollister comps were −2% (Q1 FY2026) and −3% (Q2), total comps −1%/flat.
   The strongest real disconfirming case is the return-on-capital row plus the record
   quarters, and it was built at full strength.
4. The brief's [E5-08] framing ("buying back aggressively — at what prices, against what
   value?") implied a flag; the record shows the opposite: pace tripled at ~$83–88 as the
   price halved — purchases at the conservative end of this run's own value band.
   Condition 2 passes behaviorally.
5. BLS free API truncates at 10 years per request — the 2025 annual CPI average needs a
   second call (gotcha for future deflated-series work).
6. ASC 842 finance leases: zero occurrences in the FY2025 10-K — immaterial for a
   SEVENTH consecutive run.

## REGISTER
- Verdict: **[x] OUT (about the business)** — at Q2, [E3-03] criterion (2).
- One line: **The best current economics in mall apparel (66.9% on tangible operating
  assets, 1st of the row) belong to a two-year brand-heat wave ridden superbly, not to a
  position — the same trademarks earned 1.3–13% for five straight pre-boom years, lost
  $196M of owner earnings on one mid-boom inventory season, and the price at $136.60 asks
  the wave to be a perpetuity.**
- **PRICE (required output): $136.60 against roughly $85–145/share zero-growth at the
  bare sovereign (judged ~$130), roughly $55–75/share at the [E4-28] floor. Honest
  pre-tax expectancy 3.2–5.6%: below the bond on every honest construction and below the
  10% floor on all of them.**
- **PASS/FAIL (required output): FAIL — closed at Q2 (OUT). Q1 IN · Q2 OUT · Q3 recorded
  IN-no-disqualifier (not a gate) · Q4 recorded IN-on-survival (not a gate) · Q5 not
  opened · Q6 not opened.**
