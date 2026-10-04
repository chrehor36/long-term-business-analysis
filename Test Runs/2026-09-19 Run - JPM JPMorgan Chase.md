# Company Run — JPMorgan Chase & Co. (JPM) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**THE FOURTH BANK THIS PROJECT HAS RUN, AND THE LARGEST COMPANY IT HAS EVER RUN.** CIK
**0000019617**, found this session by `tools/sources.py:cik_for('JPM')`, which returns
`('0000019617', 'JPMORGAN CHASE & CO')`. WAVE 6, under the operator ruling of 2026-09-19 that
the five banks are run.

*A correction to the brief, made here rather than silently: the brief says JPM is **the third**
bank. It is the **fourth**. `Test Runs/2026-09-19 Run - CCB Coastal Financial.md` was the first,
`Test Runs/2026-09-19 Run - ACNB ACNB Corporation.md` the second, and
`Test Runs/2026-09-19 Run - SOFI SoFi Technologies.md` the third — SOFI closed at Q2 the same day
and is already in the survival-shapes index as **#26 THE MARKED BOOK**. Nothing in the run turns
on the count; it is corrected because the deliverable asks whether the banks now run have settled
the Q2 question, and the answer depends on how many there are and where each closed.*

**HOW A BANK IS RUN HERE — four corpus rules, declared before any number, and they are the same
four CCB and ACNB declared:**

1. **Q3 is the deciding gate, not an overlay** — **[E3-29]**: *"Because leverage of 20:1
   magnifies the effects of managerial strengths and weaknesses, we have no interest in
   purchasing shares of a poorly-managed bank at a 'cheap' price. Instead, our only interest is
   in buying into well-managed banks at fair prices."* The one place in the framework where
   cheapness is ruled out as a remedy.
2. **The named failure mode is conformity** — **[E3-02]**, *"the tendency of executives to
   mindlessly imitate the behavior of their peers, no matter how foolish it may be to do so."*
   For this bank the test has a date and a filed answer: **March–May 2023**.
3. **Reserves are where dishonesty hides** — **[E2-50]**, *"where 'earnings' can be created by the
   stroke of a pen, the dishonest will gather"* — so the allowance and provisioning record is
   judged against subsequent charge-offs, and the candor benchmark **[E2-67]** is looked for.
4. **Survival is a quantified stress, not a ratio** — **[E3-24]**, the corpus's own worked bank
   example, run at Q4 against this bank's own loan book **and set beside the bank's own published
   regulatory stress result**. **No leverage ceiling**: the 10:1 rule was deleted
   (`Framework/INVENTIONS - deleted and why.md`), the corpus says twenty to one and calls it
   common, and its conclusion is about management.

**And owner earnings by the ordinary construction does not work for a bank.** This run states how
it measures return on equity capital employed **[E2-01]** and confesses the construction as a
**CONVENTION** under PRIME RULE 3, at Q3 STEP 3.

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
- rate **5.34 %** · date **09/18/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck fresh this session by `tools/sources.py:sovereign('USD')`, which
  returned `(5.34, '09/18/2026', 'US Treasury daily par yield curve')`. **FRED DGS30 is the
  fallback and was not used** (CLAUDE.md, corrected 2026-09-02).
- FX: **none needed for the quote.** JPMorganChase reports in USD and is a Delaware financial
  holding company. **But the earnings are not wholly USD-earned and that is recorded rather than
  waved at:** the FY2025 10-K states 60% of employees are in the U.S., the Firm operates in
  "65 countries" (FY2023 wording) with principal non-US operating subsidiaries J.P. Morgan
  Securities plc (U.K.) and J.P. Morgan SE (Germany). The **reporting** currency is the earnings
  currency for this run's purposes and the USD sovereign is the right one; the multi-currency
  point raised by the AIG replication of the same day is noted at the self-audit.
- **Price: US$349.67, close of 2026-09-18**, from `tools/sources.py:price('JPM')` — **AGGREGATOR,
  FLAGGED, live quote only**, per operator rule 5. **Corroborated against a primary document:**
  the Q2 2026 10-Q reports **market capitalization of $870,104 million at 2026-06-30 on
  2,658.2 million shares**, i.e. a filed period-end price of **$327.33**; today's quote is 6.8%
  above it, which is consistent and not a stale or broken input.

**Share count — the issued-versus-outstanding check, and it matters more here than anywhere this
project has run.**
- **Shares outstanding: 2,658,186,195**, from the **cover of the Form 10-Q for the quarter ended
  2026-06-30, accession `0001628280-26-054343`, filed 2026-08-06**, verbatim: *"Number of shares
  of common stock outstanding as of June 30, 2026: 2,658,186,195."*
- **The check, run because the AIG defect of 2026-09-19 showed an issued figure would have
  overstated a cap 3.6-fold.** The filed Q2 2026 balance sheet states **"Common stock ($1 par
  value; authorized 9,000,000,000 shares; issued 4,104,933,895 shares)"** and **"Treasury stock,
  at cost (1,446,747,700 … shares) … (178,433)"**. **4,104,933,895 − 1,446,747,700 =
  2,658,186,195**, to the share. **Using the issued figure would have overstated the market
  capitalisation by 1.544× — $1.44 trillion instead of $0.93 trillion.** JPMorganChase has **one
  class** of common stock, so the HBB per-class cover layer does not arise; `dei` is tagged once,
  undimensioned. Preferred stock is separate and is **not** in the common count: 2,105,375
  preferred shares at $21,040 million carrying value, excluded.
- **Post-cover issuance check, and the direction is stated because it is the conservative one.**
  No 8-K, S-3 takedown or prospectus supplement between 2026-08-06 and 2026-09-19 reports a
  common-equity issuance. **The live action in the other direction is a repurchase programme, and
  it is large:** the count has fallen **2,749.7M → 2,722.2M → 2,696.2M → 2,679.5M → 2,658.2M**
  over the five quarters to 2026-06-30, about **21–27 million shares a quarter**. **So the true
  count on 2026-09-19 is almost certainly BELOW 2,658,186,195**, which means the cap used here is
  **overstated** and every yield computed from it is **understated**. That is the conservative
  direction and the count is left as filed rather than estimated forward.
  `tools/sources.py:deal_filings('0000019617')` returns `([], [], '2026-02-13')` — **no live deal
  form**, so the quote is not a merger spread (the ROKU defect of 2026-09-12).
- **Split factor after the measurement date: 1.0**, from
  `tools/sources.py:split_factor_after('JPM','2026-06-30')`. The house rule
  `cap = close(anchor) × shares(measurement) × splits AFTER measurement` therefore needs no
  adjustment.
- **MARKET CAPITALISATION: 2,658,186,195 × $349.67 = US$929,488 million (US$929.5 billion).**
- **`formerNames` is NOT empty and it was checked rather than assumed** (the BLK trap of
  2026-09-19): the CIK carries **JPMORGAN CHASE & CO** (2009→), **J P MORGAN CHASE & CO**
  (2001→2011), **CHASE MANHATTAN CORP /DE/** (1996→2000) and **CHEMICAL BANKING CORP**
  (1994→1996). The same CIK spans the whole window used in this run and further back; there is no
  broken history.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Documents read this session, with dates and accession numbers:**

| document | period | filed | accession |
|---|---|---|---|
| **10-K** | FY2025 | 2026-02-13 | `0001628280-26-008131` |
| **10-K** | FY2024 | 2025-02-14 | `0000019617-25-000270` |
| **10-K** | FY2023 | 2024-02-16 | `0000019617-24-000225` |
| **10-K** | FY2022 | 2023-02-21 | `0000019617-23-000231` |
| **10-K** | FY2021 | 2022-02-22 | `0000019617-22-000272` |
| **10-Q** | Q2 2026 | 2026-08-06 | `0001628280-26-054343` |
| **DEF 14A** proxy | 2026 meeting | 2026-04-06 | `0000019617-26-000096` |
| **8-K EX-99.1** earnings release | Q2 2026 | 2026-07-14 | `0001628280-26-048078` |

  *The earnings release was pulled deliberately under the CGNX companion rule of 2026-09-07: a
  run that reads only the annual report will score clean a company that has built its public
  narrative on a non-GAAP metric. For this filer the metric in question is **ROTCE**, and it is
  scored at Q3.*

- **Figure cross-checked against the filed statement — TWO, and the first is the [E5-32] one**
  (*"the floating plug"* — audited does not mean true; equity recomputed from A − L):
  1. Q2 2026 filed balance sheet: **total assets $5,015,069M − total liabilities $4,640,471M =
     $374,598M**, identical to the filed **total stockholders' equity of $374,598M**. Common
     equity is that less **$21,040M of preferred = $353,558M**, and $353,558M ÷ 2,658.186M shares
     = **$133.01 book value per share**, identical to the filer's own reported $133.01.
  2. FY2025 net income reconciled to the **sum of the segment columns** in the Segment & Corporate
     Results table: **$18,245M (CCB) + $27,761M (CIB) + $6,522M (AWM) + $4,520M (Corporate) =
     $57,048M**, identical to the filed consolidated net income of $57,048M.
- *If the filing could not be obtained → **UNRESEARCHED**.* **No rung failed.** One tooling note,
  confirmed for the third time in a day: `tools/sources.py:_get()` defaults to `WEB_UA` and
  `www.sec.gov/Archives` answers that with HTTP 403, so **every primary fetch in this run passed
  `headers=SEC_UA`**.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Unit economics in my own words, no management language

JPMorganChase is **four businesses on one balance sheet, and the balance sheet is the fourth
one.**

**One — the American consumer bank (CCB).** Branches in 48 states plus Washington D.C., credit
cards, car loans, mortgages and a retail brokerage. It takes deposits from households and small
businesses, lends a part of them out and invests the rest, and charges fees for cards and
accounts. FY2025: total net revenue **$76,029M**, net income **$18,245M**, on **$56.0 billion of
allocated equity** — a **32% return on the capital assigned to it.** The credit-card book is the
engine and it is also the loss: Card Services drives essentially all of the firm's net
charge-offs, and the FY2025 provision in CCB was **$11,493M** against $35,762M of pre-provision
profit.

**Two — the corporate and investment bank (CIB).** Advising companies on deals, underwriting
their stock and bonds, making markets in everything, moving their money around the world, and
holding their securities in custody. FY2025: revenue **$78,454M**, net income **$27,761M**, on
**$149.5 billion of allocated equity** — an **18% return.** This is the largest single consumer of
the firm's capital: 43.7% of common equity earns 18%. Investment banking fees were $9,615M;
principal transactions (market-making) $27,212M; lending- and deposit-related fees $9,093M.

**Three — asset and wealth management (AWM).** Managing $7.1 trillion of client assets for a fee.
FY2025: revenue **$24,073M**, net income **$6,522M**, on **$16.0 billion of allocated equity** —
a **40% return**, the highest in the firm, on 4.7% of the capital. This is the one leg that is not
really a bank at all: it needs almost no balance sheet, and the fee is charged on someone else's
money.

**Four — Corporate, which is where the balance sheet itself lives.** Treasury and the chief
investment office run the securities portfolio, the funding and the interest-rate position, and
Corporate holds all the capital the firm has accumulated in excess of its current regulatory
requirement. FY2025: revenue **$7,025M**, net income **$4,520M**, on **$120.9 billion of allocated
equity** — **35.3% of the firm's common equity earning about 3.7%.** The filer says so in as many
words: *"Any capital that the Firm has accumulated in excess of these current requirements … has
been retained in Corporate in addition to its allocated balance."*

**The one sentence that is the whole business:** *JPMorganChase gathers $2.7 trillion of other
people's money at a price well below what money is worth, lends and invests it, sells the same
customers advice and execution and custody and asset management at a fee, and holds a third of its
equity idle against a regulatory requirement — so its return is the spread on the money, plus the
fees on the relationship, diluted by the capital it must keep and cannot use.*

### The arithmetic of the whole thing, from the filed statements, FY2025

| | $M | note |
|---|---|---|
| Net interest income | **95,443** | 52.3% of total net revenue |
| Noninterest revenue | 87,004 | of which asset management fees $20,327, principal transactions $27,212, investment banking fees $9,615, card income $4,720 |
| **Total net revenue** | **182,447** | |
| Total noninterest expense | (95,640) | overhead ratio **52%** |
| **Pre-provision profit** | **86,807** | |
| Provision for credit losses | (14,212) | includes **$2.2bn** for lending-related commitments on the Apple Card transaction |
| **Income before tax** | **72,595** | |
| Income tax | (15,547) | 21.4% effective |
| **Net income** | **57,048** | ROE **17%**, ROTCE **20%**, ROA **1.29%** |

**The single most important structural number in the file:** net interest income is **52.3%** of
revenue, and the balance sheet that produces it is **$4,424,900M of assets at 2025-12-31 against
$342,393M of common equity — 12.9 to 1** (and $5,015,069M against $353,558M at 2026-06-30, **14.2
to 1**). **[E3-29]**'s mechanism therefore applies at full strength even though the ratio is well
below the twenty to one the corpus calls common: *"mistakes that involve only a small portion of
assets can destroy a major portion of equity."* A 1% loss on assets is 14% of the common equity.

### The scarce input this business controls

**Two, and they are different in kind.**

**(a) The deposit base, and specifically its price.** $2,713,700M of deposits at 2026-06-30. This
is the input, the scarce thing, and the whole question of whether JPMorgan is a franchise is the
question of whether it gets this input cheaper than its rivals and why. That is Q2 and it is not
decided here.

**(b) The permission to be this size.** JPMorganChase is a global systemically important bank with
a **4.5% GSIB surcharge under Method 2** and a Standardized CET1 requirement of **11.5%**
including buffers. Its scale is legally conditioned: the filer's own Risk Factors run to 22 pages
on regulation, and its capital, its distributions and its ability to grow by acquisition are all
subject to Federal Reserve approval. **This is a permission, not a property** — the same class of
scarce input the CCB run identified in a very different bank — and **[E2-59]** is the rule that
governs what a regime-based advantage is worth. It is taken up at Q2.

### Will the fundamentals look broadly the same in ten years?

**Yes, and this is the clearest yes of any bank on this track.** Taking deposits, lending against
buildings and businesses, running a payment system, underwriting securities and charging a fee on
managed assets are activities this company has performed continuously under predecessor names
since 1799 (The Manhattan Company) and under this CIK since it filed as **CHEMICAL BANKING CORP**
in 1994. The 10-K's description of what CCB, CIB and AWM do would have been recognisable in 1995.
**[E3-31]** asks for *"relatively simple and stable in character"*, and the *character* is stable
even though the company is enormous.

**What is NOT simple, and it has to be written down rather than smoothed:** the FY2025 10-K runs
to **12.9 megabytes** of HTML and about **1.43 million characters** of text; it carries **32
reportable-segment notes and 34 notes in the FY2023 edition**; trading assets are $1,062,072M at
2026-06-30 with $1,074,506M of liabilities measured at fair value on a recurring basis, of which
**$76,139M is Level 3**; and Note 22–24 commitments and contingencies plus the legal-proceedings
note are the longest in this project's experience. **A reader cannot verify this balance sheet.
What a reader can do is understand the four mechanisms above, which is what Q1 asks, and then
price the unverifiability — which [E3-42] says happens at the understanding gate and in the end
margin, and nowhere else.**

### The verdict, and why it is IN and not UNKNOWABLE

**[E4-46]** scopes this exactly: *"if we can't make a decision in five minutes, we can't make it
in five months"* — a business that would take months of study is outside the circle and the verdict
is Q1 OUT, with no fetch that repairs it. **The honest answer is that the four mechanisms are
legible in an afternoon and the trading book is not legible at all.** The run resolves that the way
the framework does rather than by preference: **the mechanisms that produce 96% of the earnings —
consumer banking, banking and payments, asset management, and the spread on the securities
portfolio — are simple, and the part that is not legible is carried explicitly into Q4 as the named
way this business dies, where it is quantified.** Level 3 assets of $76,139M are 21.5% of common
equity, and that is a Q4 number, not a Q1 excuse.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

*Written as a finding and not as a compliment: I can state how this makes money and I have. I
cannot audit the trading book, and that is priced at Q4 and in the end margin, never in the rate
**[E3-42]**.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three criteria, one at a time, and criterion 2 is where the whole file lives.**

- **Needed or desired [x]** — a place to keep money, a loan, a payment system, a market-maker and
  a fee-paid asset manager. Demand is not in question.
- **No close substitute — [x], and ONLY on the one narrow ground the corpus names, and NOT on the
  ground the previous bank used.** A deposit is a commodity and this run proves that against
  JPMorgan itself below. The argument is **[E2-58]**'s single exception and it is worked in full.
- **Not price-regulated [x] on its own terms — deposit and loan rates are not administered — but
  [E2-59] is recorded against this tick and it BITES, harder here than at any bank on this track.**
  See the First Republic finding below.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**

**No to the first; and the second is a real finding, not a formality.**

On **[E4-04]**'s scope test — *"does a lapse in spending destroy the structure, or merely narrow
it — and does the spending defend the same advantage, or buy its replacement?"* — the branch
network, the payment rails, the custody platform and the Chase brand must be **defended** (and the
filer is spending heavily: technology, communications and equipment expense $6,128M in H1 2026, up
16%; marketing $3,274M, up 27%). A lapse narrows. **It does not replace the basis of the
advantage**, which is the deposit base and the installed operational position. This is Coca-Cola's
advertising, not Mitsui's Rhodes Ridge.

**On the manager, the filer's own competition section is the evidence and it is [E3-38]'s list
almost verbatim:** *"The Firm's businesses generally compete on the basis of the quality and
variety of the Firm's products and services, **transaction execution, innovation, reputation and
price**."* Transaction execution and innovation are have-to-be-smart-**every-day**. **Under
[E4-23] that is recorded HERE, at Q2, as a moat defect** — *"if a business requires a superstar to
produce great results, the business itself cannot be deemed great"* — and it is the reason the
class below is NARROW rather than WIDE. **It also sets the Q3 weight case**, and it is why Q3 is a
gate.

*One thing that cuts the other way and is written because it is true: under **[E2-53]**'s dominance
test and **[E5-18]**'s stand-a-little-mismanagement test, a bank with 11.67% of all United States
domestic insured deposits and the #1 position in global investment banking fees holds a position
that would survive a mediocre chief executive for years. The filings cannot show that; the
arithmetic of a $2.7 trillion deposit base suggests it. It is recorded as a judgment, not as
evidence.*

### Primary moat metric, filing-sourced, and its trend — AND THE FIRST ONE FAILS

**The metric ACNB's franchise rested on was the cost of the money, and it is the right first test
for any bank. JPMorgan FAILS it, and that is the most important single fact in this Q2.**

| JPMorganChase, cost of **total** deposits (interest expense on deposits / average total deposits including noninterest-bearing), from the filer's OWN daily-average tables in five successive 10-Ks | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| **cost of total deposits** | **0.023%** | **0.409%** | **1.696%** | **2.077%** | **1.800%** |
| noninterest-bearing share of average deposits | 27.8% | 29.1% | 28.0% | 26.8% | **24.1%** |
| average total deposits, $M | 2,347,154 | 2,467,915 | 2,359,067 | 2,386,642 | 2,506,565 |

*Source rows, per year, so this is reproducible: FY2021 10-K `0000019617-22-000272` interest-bearing
deposits average $1,694,865M / interest $531M / noninterest-bearing $652,289M; FY2022
`0000019617-23-000231` $1,748,666M / $10,082M / $719,249M; FY2023 `0000019617-24-000225`
$1,698,529M / $40,016M / $660,538M; FY2024 `0000019617-25-000270` $1,748,050M / $49,559M /
$638,592M; FY2025 `0001628280-26-008131` $1,902,382M / $45,112M / $604,183M.*

**Direction: the noninterest-bearing share has fallen every year since 2022, 29.1% to 24.1%.**
**[E4-32]** — direction outranks existence — reads that as the funding franchise **narrowing**, on
the filer's own numbers, and **[E4-55]**'s units test confirms it: the *physical* series (the share
of deposits paying nothing at all) is the honest one, and it is down 5.0 points in three years.

### THE COMPETITOR ROW — required **[E3-28]**. TWO ROWS, because one alone cannot settle it.

*Specification, stated once so the row is reproducible. **ROTCE** is each filer's own published
figure, read in its own 10-K text, because every one of the six publishes it and it is the
**[E2-43]** denominator the framework requires for an acquisitive filer (*"unleveraged net tangible
assets … the best guide to the economic attractiveness of the operation"*) with the goodwill wedge
outside it. **Efficiency / overhead** is each filer's own published ratio, unadjusted, so merger
costs and one-time items are left in for everybody. **Cost of total deposits** is computed by this
session on ONE uniform specification for all six — interest expense on deposits divided by the
simple average of opening and closing total deposits — from each filer's own annual tagged data,
because the six do not all publish the same deposit-cost measure. **The uniform figure is
cross-checked against the filed daily-average table for the subject: 1.817% for JPM in 2025 on the
uniform basis against 1.800% on the filer's own daily averages, a 1.7-basis-point difference, which
is the period-end-versus-daily-average artefact and is disclosed rather than smoothed.***

#### ROW A — the five named peers, holding-company level, five years, from their own 10-Ks

| holding company | **ROTCE 2025** | 2024 | 2023 | 2022 | 2021 | **5-yr mean ROTCE** | **efficiency 2025** | **5-yr mean efficiency** | **cost of total deposits, 5-yr mean** | source |
|---|---|---|---|---|---|---|---|---|---|---|
| **JPMorgan Chase — the subject** | **20** | **22** | **21** | **18** | **23** | **20.80%** | **52** | **55.40%** | **1.202%** | 10-K `0001628280-26-008131` + four prior |
| Morgan Stanley | 21.6 | 18.8 | 12.8 | 15.3 | 19.8 | **17.66%** | 68 | 4-yr 72.3 | 1.699% | 10-K `0000895421-26-000086`; FY2022 `0000895421-23-000284` |
| Goldman Sachs (ROTE) | 16.0 | 13.5 | 8.1 | 11.0 | 24.3 | **14.58%** | not published as one ratio | — | **2.958%** | 10-K `0000886982-26-000091`; FY2022 `0000886982-23-000003` |
| Bank of America | 14.22 | 12.94 | 13.46 | 15.15 | 17.02 | **14.56%** | 61.65 | **64.66%** | **1.066%** | 10-K `0000070858-26-000157`; FY2023 `0000070858-24-000122`; FY2022 `0000070858-23-000092` |
| Wells Fargo | 14.6 | 13.4 | 13.1 | 8.95 | 14.29 | **12.87%** | 66 | **69.20%** | **0.927%** | 10-K `0000072971-26-000133`; FY2022 `0000072971-23-000071` |
| Citigroup | 7.7 | 7.0 | 4.9 | 8.9 | 13.4 | **8.38%** | 64.7 | **67.52%** | 1.902% | 10-K `0000831001-26-000011` |

- **Peers named: 5 of 5 the brief asked for, and they are the right five** — the other US universal
  banks and the other two US GSIB broker-dealers. **Buffett says eight [E3-28]**; the category of
  "banks JPMorgan competes with across all of its businesses" has **five** members and all five are
  here. Row B below takes the whole insured industry.
- *Goldman Sachs does not publish a single efficiency ratio in the FY2025 10-K text; its bank-level
  figure is in Row B. That cell is left empty rather than constructed on a different definition.
  Morgan Stanley's FY2021 expense efficiency ratio was not located in the two filings read, so its
  mean is a four-year mean and is labelled as such.*

**WHAT ROW A SAYS, AND IT SAYS TWO OPPOSITE THINGS THAT BOTH HAVE TO BE WRITTEN DOWN.**

**FOR the franchise, and it is decisive on the one number the corpus asks about the business
[E3-46]** (*"the best businesses, by definition, are going to be businesses that earn very high
returns on capital employed over time"*):
1. **JPMorgan is FIRST of six on return on tangible common equity in four of the five years and on
   the five-year mean, by 3.14 points over Morgan Stanley and about 6.2 points over Bank of America
   and Goldman Sachs.** Its worst year (18%, 2022) beats Bank of America's best year (17.02%),
   Wells Fargo's best (14.6%) and Citigroup's best (13.4%).
2. **And it is first on the cost line — the operating one.** Overhead ratio **52%** against Bank of
   America's 61.65%, Citigroup's 64.7% and Wells Fargo's 66%. Five-year means: **JPMorgan 55.40%,
   Bank of America 64.66%, Citigroup 67.52%, Wells Fargo 69.20%.** **The gap against the next-best
   universal bank is 9.65 points of a $182,447M revenue base, which is about $17.6 billion of
   pre-tax income a year.** And it is **widening**: JPMorgan went 59, 59, 55, 52, 52 while Bank of
   America went 67.03, 64.71, 66.79, 63.12, 61.65. **This is the [E2-58] exception, met on filed
   figures: *"a cost advantage that is both wide and sustainable … By definition such exceptions
   are few."***

**AGAINST the franchise, and this is the part a bull case omits:**
3. **JPMorgan is NOT the cheapest funder. It is THIRD of six, in every one of the five years.**
   Five-year mean cost of total deposits: **Wells Fargo 0.927%, Bank of America 1.066%, JPMorgan
   1.202%**, Morgan Stanley 1.699%, Citigroup 1.902%, Goldman Sachs 2.958%. **The single metric on
   which the previous bank in this queue passed criterion 2 — ACNB, first of eleven and sixth of
   fifty-six on cost of funds — JPMorgan LOSES, to two of its five peers, every year.** On
   $2,506,565M of average deposits, Bank of America's 13.6-basis-point five-year advantage is worth
   about **$3.4 billion a year pre-tax** and Wells Fargo's 27.5 basis points about **$6.9 billion**.
   **A deposit is a commodity, and JPMorgan's deposits are not the cheap ones.**
4. **The deposit share is FLAT over five years, including the year it absorbed a failed bank.**
   See Row B.
5. **The investment-banking share is FALLING while the rank holds.** The filer's own Dealogic table:
   global investment-banking fee wallet share **8.6% (2023), 9.1% (2024), 8.4% (2025)**; and the
   loan-syndication rank slipped from **#1 to #2 globally and #1 to #2 in the U.S.** in 2025 (global
   share 12.0%, 10.2%, 10.1%; U.S. 15.1%, 11.7%, 11.3%). **[E4-32]** reads a #1 rank with a
   three-year decline in share as a narrowing, not a widening.

#### ROW B — the whole insured industry, from the issuing authority, not from the SEC

Row A is six listed holding companies. **The FDIC collects a quarterly Call Report from every
insured institution in the United States and publishes the ratios directly**, which is the only
instrument that can see the mutuals, the foreign branches and the private banks an SEC row cannot —
the rung the CCB run said was missing from the evidence ladder, and the rung the ACNB run used to
close its moat class. This session pulled **all 4,411 insured institutions' 2025-12-31 Call
Reports** (and 4,904 / 4,773 / 4,658 / 4,560 / 4,313 filers at the five other dates), plus the seven
relevant bank subsidiaries at six dates. **JPMorgan Chase Bank, N.A. is CERT 628.**

**(i) DEPOSIT SHARE — the evidence the brief asked for, and the answer is FLAT.**

| domestic deposits, share of ALL FDIC-insured institutions | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06-30 |
|---|---|---|---|---|---|---|
| **JPMorgan Chase Bank NA** | **11.77%** | **11.30%** | **11.68%** | **11.44%** | **11.67%** | **11.65%** |
| Bank of America NA | 11.08% | 10.82% | 10.94% | 10.79% | 10.56% | 10.37% |
| Wells Fargo Bank NA | 8.23% | 7.85% | 7.98% | 7.94% | 7.95% | 8.13% |
| Citibank NA | 4.02% | 4.36% | 4.28% | 4.24% | 4.48% | 4.69% |
| *industry domestic deposits, $bn* | *18,287* | *17,830* | *17,451* | *17,856* | *18,573* | *19,119* |
| *institutions filing* | *4,904* | *4,773* | *4,658* | *4,560* | *4,411* | *4,313* |

**JPMorganChase is the largest deposit-taker in the United States at 11.67% of all domestic insured
deposits, $2,167.8 billion at 2025-12-31 — and its share in mid-2026 is 12 basis points BELOW where
it stood at the end of 2021, after absorbing First Republic.** Bank of America's share fell 71 basis
points over the same window and Wells Fargo's fell 10; Citigroup's rose 67. **So JPMorgan held
share while its largest rival lost it, which is a relative win — but the franchise did not widen on
the measure that matters most to it, and a $92 billion acquired deposit base bought 38 basis points
of share that had drifted away within two years.**

**(ii) THE BANK-LEVEL ROW — six dates, seven institutions, one uniform Call Report definition**

| FDIC Call Report | metric | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06-30 | **5-yr mean** |
|---|---|---|---|---|---|---|---|---|
| **JPMorgan Chase Bank NA** | cost of funding earning assets | 0.073 | 0.528 | 1.971 | 2.392 | **2.082** | 1.913 | **1.409%** |
| Bank of America NA | same | 0.039 | 0.286 | 1.625 | 2.195 | **1.868** | 1.596 | **1.203%** |
| Wells Fargo Bank NA | same | 0.064 | 0.329 | 1.510 | 1.963 | **1.660** | 1.578 | **1.105%** |
| Citibank NA | same | 0.252 | 0.975 | 3.006 | 3.373 | 2.846 | 2.580 | 2.090% |
| Goldman Sachs Bank USA | same | 0.465 | 1.746 | 4.648 | 4.811 | 3.954 | 3.590 | 3.125% |
| Morgan Stanley Bank NA | same | 0.207 | 0.589 | 2.431 | 2.992 | 2.834 | 3.218 | 1.811% |
| Morgan Stanley Private Bank NA | same | 0.157 | 0.438 | 2.277 | 2.858 | 2.562 | 2.505 | 1.658% |
| **JPMorgan Chase Bank NA** | net interest margin | 1.81 | 2.32 | 3.15 | 3.04 | **2.96** | 2.88 | **2.66%** |
| Bank of America NA | same | 1.99 | 2.43 | 2.71 | 2.50 | 2.50 | 2.53 | 2.43% |
| Wells Fargo Bank NA | same | 2.22 | 2.89 | 3.58 | 3.37 | **3.29** | 3.13 | **3.07%** |
| Citibank NA | same | 2.56 | 2.90 | 3.05 | 3.00 | 3.08 | 3.02 | 2.92% |
| **JPMorgan Chase Bank NA** | efficiency ratio | 61.65 | 56.98 | 52.23 | 53.64 | **52.37** | 54.38 | **55.37%** |
| Bank of America NA | same | 61.74 | 56.23 | 56.54 | 56.52 | 52.27 | 53.91 | 56.66% |
| Wells Fargo Bank NA | same | 69.98 | 67.79 | 58.91 | 56.93 | 55.41 | 54.77 | 61.80% |
| Citibank NA | same | 62.09 | 56.94 | 61.94 | 57.85 | 55.60 | 51.39 | 58.88% |
| Goldman Sachs Bank USA | same | 48.51 | 44.87 | 41.44 | 34.07 | 39.21 | 38.49 | 41.62% |
| **JPMorgan Chase Bank NA** | noninterest-bearing share of deposits | 29.2 | 27.7 | 26.8 | 24.8 | **23.2** | 23.8 | — |
| Bank of America NA | same | 41.6 | 35.9 | 30.2 | 28.2 | **27.5** | 28.7 | — |
| Wells Fargo Bank NA | same | 37.4 | 35.0 | 28.5 | 29.3 | **27.3** | 26.7 | — |
| Citibank NA | same | 17.7 | 13.8 | 13.2 | 14.0 | 12.7 | 11.7 | — |

**Row B confirms Row A independently and it sharpens the adverse finding.** On the one input that
IS the business — the price of the money — **JPMorgan Chase Bank, N.A. is third of the four
universal banks at every one of six dates**, 21 basis points behind Bank of America and 42 behind
Wells Fargo at 2025-12-31, and the gap on the *free* money is larger still: **23.2% of JPMorgan's
deposits pay nothing against 27.5% at Bank of America and 27.3% at Wells Fargo.** JPMorgan does
**not** have the cheapest or the stickiest deposit base in the United States. What it has is the
**largest**, and — on the efficiency ratio and on holding-company ROTCE — the **best-run**.

- **Peers named: 5 SEC-registrant holding companies (Row A) plus every FDIC-insured institution in
  the United States at six dates (Row B, 4,313 to 4,904 filers).** Buffett says eight **[E3-28]**;
  this row took five where five is the whole category, then took the entire insured industry.
- **Any peer unavailable? ONE class, named with its artifact rather than waved at: the non-bank
  competitors the filer itself names** — *"e-commerce and other internet-based companies, digital
  asset and other financial technology companies"*, money-market funds, and the credit unions
  (NCUA Form 5300, public, not pulled). **That rung is UNRESEARCHED and the direction of the
  missing evidence is stated so a reader can price it: money-market funds and fintech deposit
  sweeps are structurally CHEAPER substitutes for a deposit, so the missing rung can only push the
  measured funding position further DOWN, never up.** **The uncertainty is spent in the CLASS —
  NARROW, not WIDE — and not left as an open question**, because the advantage that survives the
  row is the operating-cost one, measured against five named filers over five years, and the
  funding advantage has already been found absent.
- **Untapped pricing power — could a manager raise the return simply by raising prices? [E3-33]**
  **NO, and [E5-28] is respected: claiming this class means claiming near-monopoly, and 11.67% of
  deposits is not one.** **[E4-37]**'s inverse metric is the useful test and the filed record
  answers it in the *wrong* direction for the franchise: the price JPMorgan pays for its money went
  from 0.023% to 2.077% in three years, and its free-deposit share fell every year. **This is a
  business that had to raise the price it pays, not one that could raise the price it charges.** On
  the asset side its own Risk Factors say the opposite of pricing power: *"Actions by competitors
  could put pressure on the pricing for JPMorganChase's products and services or could cause it to
  lose market share, particularly with respect to investment products and traditional banking
  products."*
- **[E2-58]'s commodity doctrine, which IS the criterion-2 test for any bank, and where the pass
  comes from.** The equation: persistent over-capacity without administered prices equals poor
  profitability, with **one** exception — *"a cost advantage that is both **wide and sustainable** …
  By definition such exceptions are few."* **JPMorgan's cost advantage is real, wide and measured,
  and it is on the EXPENSE line, not the funding line.** 52% overhead against 61.65% / 64.7% / 66%;
  a five-year mean 9.3 to 13.8 points better than the three other universal banks; about
  **$17.6 billion a year pre-tax at the 2025 revenue base**; and **widening rather than closing**.
  **This is the second way a bank has met [E3-03] criterion 2 in this project, and it is a
  different way from the first:** ACNB met it on **cost of funds** (a low deposit beta, a property
  of the depositor base); **JPMorgan fails on cost of funds and meets it on cost of operations**
  (scale spread over a fixed platform). *A brief correction: the brief says "two banks have already
  met it differently"; the record is that **one** has. CCB's Q2 was OUT and SOFI's Q2 was OUT.
  JPMorgan is the second.*
- **[E3-62]'s second step, mandatory in a commodity business: how much of the cost advantage stays
  home and how much flows to the customer?** **It stays home, and the arithmetic says so:**
  JPMorgan runs a 2.96% net interest margin on 2.08% money while Bank of America runs 2.50% on
  1.87% and Wells Fargo 3.29% on 1.66%. JPMorgan is **not** buying its deposit share by paying up
  for deposits **or** by undercutting on loans — its margin is second of four and its funding cost
  third of four, which is the profile of a firm competing on service and scale rather than on price.
  **The 9.65-point overhead gap is retained as pre-tax income, not competed away.**
- **[E4-36] — which of the four causes of extreme success is this?** **Extreme performance over
  many factors**, not the max/min of one variable and not wave-riding. JPMorgan is **not** first on
  cost of funds (third), **not** first on net interest margin (second of four), **not** first on
  bank-level efficiency (Goldman Sachs Bank USA is, at 39.21%, on a different business), and
  **not** gaining deposit share. It is first on the **composite** — return on tangible equity — in
  four of five years, by being top-quartile on many lines at once and bottom on none. **[E3-51]**'s
  surfing test is failed in the right direction: the 2021 to 2025 rate cycle *was* a wave and all
  six banks sat in it, so the *relative* position is not the wave.
- **[E2-45]'s attacker's test — with ample capital and skilled people, how would I compete with
  this?** **Not on price, and not on scale.** I would do exactly what the filer's Risk Factors
  describe being done to it: attack the profitable edges without the balance sheet or the
  regulation — *"both financial institutions and their non-banking competitors face the risk of
  disruption to payments processing and other products and services from the use of new
  technologies that may not require intermediation, such as tokenized securities"*, and *"advocacy
  by non-banking competitors for exemptions from regulatory requirements could significantly
  disadvantage traditional financial institutions."* **That attack is already fully deployed** —
  money-market funds above 4%, fintech sweep accounts, private credit taking the leveraged-loan
  book — **and JPMorgan's answer, visible in the filed numbers, is that its free-deposit share fell
  5.0 points in four years while its deposit share held.** The attack is working on the *price* of
  the deposits and not yet on the *quantity*.
- **[E3-61]'s limit is recorded because the corpus insists on it:** the row shows position, not
  conduct — *"In some businesses, the participants behave like a demented Kellogg. In other
  businesses, they don't … I think you'd have to know the people involved."* Six banks with almost
  identical charters produced five-year mean ROTCE from 8.38% to 20.80%. The row cannot say which
  will imitate the next lax underwriting cycle. **That is Q3's question, and for a bank Q3 is a
  gate [E3-29].**

### [E2-59] — AND THIS IS WHERE IT BITES, BECAUSE THE 2023 GAIN WAS GRANTED BY THE REGIME

**[E2-59]** is exact: administered pricing or regulatory protection can floor a commodity
business's profits, but *"the moat belongs to the **regime**,"* and *"That day is gone"* is how it
ends. The brief asks whether any advantage rests on being systemically important rather than on
winning customers. **On one specific, dated, quantified event, it does — and it is the largest
single acquisition gain in the window.**

- **JPMorgan Chase Bank, N.A. held 11.30% of all United States domestic insured deposits at
  2022-12-31**, on the FDIC's own numbers — a share it has held above eleven per cent throughout.
  **So the ordinary route to buying a $200 billion bank was closed by the nationwide deposit
  concentration limit**, and the filer's own Supervision and Regulation section states the parallel
  cap it lives under: *"acquisitions by financial companies are generally prohibited if, as a result
  of the acquisition, the total liabilities of the financial company would exceed 10% of the total
  liabilities of all financial companies, as determined under Federal Reserve regulations."*
- **What opened instead was an FDIC receivership auction.** From Note 34 of the FY2023 10-K
  (accession `0000019617-24-000225`): *"On May 1, 2023, JPMorgan Chase acquired certain assets and
  assumed certain liabilities of First Republic Bank (the 'First Republic acquisition') from the
  Federal Deposit Insurance Corporation ('FDIC'), as receiver."*
- **The advantage was granted, not won.** Only a handful of institutions could absorb $192,231
  million of assets overnight, and the receiver's least-cost mandate selected the largest bidder.
  **That is [E2-59]'s regime exactly: the profit is floored by an arrangement rather than by a
  customer's preference.** It is scored here as a **regime advantage, not as moat evidence** — and
  the $2,775 million after-tax gain is handled at Q4 under the CNR rule.

### Class and direction

- Class: **[ ] WIDE  [x] NARROW  [ ] NONE  [ ] PROVISIONAL.** NARROW, and the reason is specific
  rather than a hedge: **the franchise is ONE line of the income statement — the expense line — plus
  a position.** It is not the deposit price (third of six), not the margin (second of four), not
  deposit-share growth (flat), not investment-banking share (falling); and the business
  **requires** daily competence by the filer's own account of what it competes on, which
  **[E4-23]** makes a moat defect. **[E2-53]**'s dominance class — *"Good or bad, it will
  prosper"* — is the strongest available reading and it is **not** claimed, because the filings show
  a company that has to earn its 52% overhead ratio every year against five rivals trying to close
  it.
- Direction: **MIXED, and the two limbs point opposite ways on purpose, exactly as ACNB's did.**
  **Widening:** the overhead ratio (59 to 52 while Bank of America went 67.03 to 61.65), and ROTCE
  first of six in four of five years. **Narrowing:** the noninterest-bearing deposit share (29.1%
  to 24.1%), the investment-banking fee wallet (9.1% to 8.4%), the loan-syndication rank (#1 to
  #2), and a deposit share 12 basis points below 2021 after buying a bank. **[E4-32] is claimed for
  the composite and explicitly NOT claimed for the funding franchise.**

- **VERDICT: [x] IN — class NARROW, direction MIXED  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

*Why this is IN and not UNRESEARCHED, stated so a reader can disagree with the trade that was made.
The gate asks whether this is a franchise. Five named peers over five years from their own filings,
plus every insured institution in the United States at six dates from the regulator that collects
the data, say that JPMorganChase earns a return on tangible common equity 3.1 to 12.4 points above
every one of its five real competitors, for five consecutive years, on a 9.3-to-13.8-point
operating-cost advantage that is widening — which is **[E2-58]**'s one named exception, met on filed
figures. **The class is NARROW because that is one line and because the business requires daily
competence; the direction is MIXED and written as MIXED; the non-bank substitute rung is named as a
work order with its direction stated.** No "unverified", "general knowledge" or "provisional" caveat
is carried into the verdict — what is carried is a class and a direction, both of which are
findings.*

*And the structural question CCB left for the operator is answered the same way ACNB answered it and
is NOT resolved here: **[E3-43]** classes a bank as *"a business, unlike a franchise"*, which read
literally makes Q2 OUT automatic for every bank. **This run did not use that reasoning and did not
need to refuse it** — it ran **[E3-03]**'s three criteria and **[E2-58]**'s exception on filed
numbers, which is what ACNB did. The general question remains the operator's call under PRIME
RULE 5, and the note at the foot of this file records what the fourth bank contributes to it.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*

- [x] **Daily execution** — **[E3-38]**, its 1991 original **[E3-43]**, the 1977 root **[E2-70]**.
  The filer's own statement of what it competes on is the evidence: *"transaction execution,
  innovation, reputation and price."* Add a **$1,062,072 million trading book** at 2026-06-30, a
  **$1,673,579 million wholesale credit portfolio**, 320,560 employees and operations in dozens of
  countries. This is have-to-be-smart-**every-day** by construction.
- [ ] **Control** — no; this would be a minority listed position **[E1-16]**.
- [x] **Leverage** — **[E3-29]**. **Total assets $4,424,900M over common equity $342,393M at
  2025-12-31 is 12.9 : 1; $5,015,069M over $353,558M at 2026-06-30 is 14.2 : 1.** That is below the
  twenty to one the corpus calls *"a common ratio in this industry"* and **there is no leverage
  ceiling in this framework** — the 10:1 rule was deleted and does not return. **But the
  mechanism [E3-29] describes is fully present and does not need 20:1:** *"mistakes that involve
  only a small portion of assets can destroy a major portion of equity."* **A loss of one per cent
  of assets is 14.2 per cent of the common equity.** For scale, the 2012 trading loss in one
  portfolio was about 0.17% of assets and cost $275 million in Federal Reserve penalties alone.

**Case declared: TWO of three determinants are high, so Q3 is a BINARY GATE and NO PRICE
COMPENSATES [E3-29, E1-16, E5-35]** — *"You can turn any investment into a bad deal by paying too
much. What you can't do is turn any investment into a good deal by paying little."* This is the one
place in the framework where cheapness is ruled out as a remedy, and for this company it is the
question the file turns on.

### Honesty — binary, permanent, filings-based **[E5-16]**, each matter dated to when it became PUBLIC

**THE CLOSEST PRECEDENT ON DISK IS AGAINST THIS COMPANY AND IT HAS TO BE FACED FIRST.**
`Framework/v4/VERIFICATION - the two cases that decide the deletions.md` rejects **Citigroup at
mid-2007 at Q3**, on the company's own Legal Proceedings section — Enron ($2.01 billion), Adelphia
($250 million), WorldCom, Parmalat, the research-analyst matters and twelve named securities
actions — and concludes: *"v4 rejects Citigroup at Q3. The run stops there and never reaches the
balance sheet."* **A run on the largest bank in the United States that does not test itself against
that precedent has not done Q3.** So the record is set out in full, dated, and then compared with
Citigroup's on one instrument.

**THE FILED RECORD, dated to when each matter became public.** From the 10-Ks read:

| date public | matter, from the filings | disposition as at 2025-12-31 |
|---|---|---|
| **2015-05** | **The Firm pleaded GUILTY to a single violation of federal antitrust law** (foreign exchange). *"in May 2015, the Firm pleaded guilty to a single violation of federal antitrust law."* A DOL exemption permits continued reliance on the ERISA Qualified Professional Asset Manager exemption **through the ten-year disqualification period, which began in January 2017** | one South Africa Competition Tribunal matter remains; the accompanying Federal Reserve Cease and Desist Order was **terminated 2021-08-03** |
| **2016-12, re-imposed 2023-12** | European Commission finding of *"an infringement of European antitrust rules relating to EURIBOR"*; the European General Court annulled the fine and **re-imposed it in an identical amount** | appeal heard by the Court of Justice of the European Union January 2026, judgment reserved |
| **2020-09-29** | **Deferred Prosecution Agreement with the Department of Justice** relating to the *"precious metals and U.S. Treasuries markets investigations"*, plus a CFTC cooperation obligation. Disclosed as an *"Ongoing obligation"* in the FY2021, FY2022 and FY2023 10-Ks | **the DPA is GONE from the FY2024 and FY2025 10-Ks** — served and lapsed. A shareholder derivative action over the same conduct is pending in the E.D.N.Y. against the Firm, its Board and certain current and former officers; defendants have moved to dismiss |
| **2021-08** | India's Enforcement Directorate fined J.P. Morgan India **approximately $31.5 million**, following a July 2019 Supreme Court of India order making *"preliminary findings that Amrapali and other parties, including unspecified JPMorganChase entities, violated certain criminal currency control and money laundering provisions"* | under appeal |
| **2023-06 / 2023-11** | **Epstein.** *"alleging that JPMorgan Chase Bank, N.A. knowingly facilitated Jeffrey Epstein's sex trafficking and other unlawful conduct by providing banking services to Epstein until 2013."* **$290 million paid to a fund for Epstein survivors**; final approval November 2023, over the objections of certain state Attorneys General | settled and paid |
| **2024-03 / 2024-05** | **NEW consent orders with the OCC and the Board of Governors of the Federal Reserve System, and a May 2024 CFTC resolution, relating to *"the Firm's processes to inventory trading venues and confirm the completeness of certain data fed to trade surveillance platforms"*** | the Federal Reserve order was **terminated 2025-12-04**; the CFTC matter is discharged; **the March 2024 OCC consent order remains in force and is the only ongoing obligation disclosed at 2025-12-31** |
| **2026-01** | *"a civil lawsuit filed in January 2026 in Florida state court by President Donald J. Trump, in his personal capacity, and several affiliated corporate entities, against JPMorgan Chase Bank, N.A. and its CEO"*, under the August 2025 Executive Order *"Guaranteeing Fair Banking for All Americans"* | pending; JPMorganChase *"is responding to requests from government authorities"* |
| ongoing | **Legal expense: $1.4 billion (2023), $740 million (2024), $361 million (2025)** | falling 74% in two years |
| ongoing | **Estimated aggregate range of reasonably possible losses in excess of reserves: $0 to approximately $1.2 billion** at 2025-12-31 | **0.13% of the market capitalisation** |

**THE DECISIVE ARTIFACT, PULLED FROM THE ISSUING AUTHORITY RATHER THAN RECALLED.** The 10-K
discloses the *existence* of the 2024 orders in one sentence and not their number, their history or
their status; and **"no other order is disclosed" is an absence claim**, which the framework's
absence-claim rule forbids unless a recorded sweep looked for it. So the sweep was performed on the
register that actually holds the answer: **the Board of Governors of the Federal Reserve System's
own enforcement-actions file, `https://www.federalreserve.gov/supervisionreg/files/enforcementactions.csv`,
downloaded 2026-09-19 — 2,889 actions, saved to
`Test Runs/_research 2026-09-19 JPM/frb_enforcement_actions.csv`.** *This is the rung the CCB run of
the same day said was missing from the six-rung evidence ladder. It is not missing. It is one HTTP
request from the issuing authority, and it settles a gate.*

**JPMorgan Chase & Co.'s complete Federal Reserve entity record, all thirteen actions:**

| effective | terminated | action |
|---|---|---|
| 2003-07-28 | 2006-10-26 | Written Agreement |
| 2011-04-13 | 2018-01-12 | Cease and Desist Order (with EMC Mortgage) |
| 2011-07-06 | 2017-06-16 | Written Agreement |
| 2012-02-09 | n/a | **Civil Money Penalty, $275,000,000** |
| 2013-01-14 | 2019-06-06 | Cease and Desist Order |
| 2013-01-14 | 2019-12-05 | Cease and Desist Order |
| 2013-02-28 | 2018-01-12 | Amendment to the 2011 Order to Cease and Desist |
| 2013-09-18 | n/a | **Civil Money Penalty, $200,000,000** |
| 2015-05-20 | n/a | **Civil Money Penalty, $342,000,000** |
| 2015-05-20 | 2021-08-03 | Cease and Desist Order |
| 2016-11-17 | 2020-02-11 | Cease and Desist Order |
| 2016-11-17 | n/a | **Civil Money Penalty, $61,932,500** |
| 2024-03-08 | **2025-12-04** | Cease and Desist Order, Civil Money Penalty |

**And the same register, run across the competitor row, because a conduct record is a relative
claim exactly as a moat is [E3-28]:**

| group (all name variants) | entity actions | of which ORDERS | **orders STILL OPEN** | civil money penalties | **$ penalties** | actions since 2020 | individuals actioned |
|---|---|---|---|---|---|---|---|
| **JPMorgan Chase** | **13** | **9** | **0** | 5 | **$878,932,500** | **1** | 4 |
| Citigroup | 12 | 7 | **1** | 5 | $442,600,000 | 2 | 1 |
| Goldman Sachs | 10 | 5 | 0 | 5 | $50,390,054 | 2 | 7 |
| Wells Fargo | 8 | 5 | **1** | 3 | $172,000,000 | 2 | **17** |
| Bank of America | 7 | 5 | 0 | 2 | $380,500,000 | 0 | 1 |
| Morgan Stanley | 3 | 2 | 0 | 1 | $8,000,000 | 0 | 3 |

**What this says, and both halves are written down.**

**AGAINST JPMorgan:** it has the **most** Federal Reserve entity actions of the six (tied with
Citigroup at thirteen and twelve) and **by far the largest total of civil money penalties —
$878.9 million, twice Citigroup's and more than double Bank of America's.** Two of the five
penalties are the events where its own traders did the damage: **$200,000,000 on 2013-09-18** (the
2012 trading loss) and **$342,000,000 on 2015-05-20** (foreign exchange, alongside the criminal
guilty plea). Four individuals affiliated with the Firm have been the subject of Federal Reserve
actions, including prohibitions from banking. **This is not a clean record and no part of this file
will call it one.**

**FOR JPMorgan, and it is the test the corpus actually supplies.** **[E5-22]** is exact: *penalty
size is not seriousness, in either direction* — the Wells Fargo error was reading a $185 million
fine as small, and *"the failure that counts is **they didn't act when they learned**."*
- **Every terminable Federal Reserve order against JPMorgan Chase & Co. has been terminated.
  ZERO are open.** The most recent, dated 2024-03-08, was **released on 2025-12-04 — twenty-one
  months.** A supervisor terminates an order only when remediation has been examined and accepted.
- **Citigroup and Wells Fargo each still have an open order on the same register at the same
  date.** So the Citigroup comparison, run on one instrument from one authority, comes out the
  other way in 2026 from the way it came out in 2007: **the reason v4 rejected Citigroup was a
  record of live, unresolved matters, and JPMorgan's comparable record is closed while
  Citigroup's — nineteen years later — still is not.**
- Only **one** Federal Reserve action since 2020, against two at Citigroup, two at Wells Fargo and
  two at Goldman Sachs.
- The **Deferred Prosecution Agreement was served and lapsed**, which is the filed evidence that
  the Department of Justice's conditions were met: the FY2021, FY2022 and FY2023 10-Ks disclose it
  as an ongoing obligation and the FY2024 and FY2025 10-Ks do not.
- Legal expense **$1.4 billion → $740 million → $361 million**, and the reasonably-possible-loss
  range above reserves is **$0 to about $1.2 billion**, 0.13% of the market capitalisation.

**No [E5-16] disqualifier is found, and the finding is written in the form the corpus requires —
[E5-17]: *"People are not that easy to read. Sincerity and empathy can easily be faked."*
A Q3 pass is the ABSENCE OF FOUND DISQUALIFIERS, not a finding that the managers are honest.**
The conduct in each matter was by identified employees or by the institution's controls, the
individuals were prosecuted or prohibited, and **[E2-31]**'s *"never succeeded in making a good deal
with a bad person"* is a test about a person and is not met by any named officer on this record.
**The reader who concludes from the same table that $879 million of central-bank penalties and a
criminal antitrust plea IS a disqualifier has a defensible reading, and this run says so rather
than hiding it.** What decides it here is that the corpus's own operative test — did they act when
they learned — is answered by the regulator's own termination dates, and it is answered yes,
thirteen times out of thirteen.

### STEP 2 — THE FLAGS **[E4-22, E5-15, E4-29, E4-30]**. Each is a prompt to READ, never a verdict.

- [x] **WEAK ACCOUNTING — the cockroach rule FIRES, and it is the sharpest Q3 finding in the file.**
  *"There is seldom just one cockroach in the kitchen."* **The 2020 Deferred Prosecution Agreement
  was about traders manipulating the precious-metals and U.S. Treasuries markets. The 2024 consent
  orders are about the Firm's *"processes to inventory trading venues and confirm the completeness
  of certain data fed to trade surveillance platforms"* — that is, the controls whose job is to
  CATCH exactly that conduct, and they were found deficient three and a half years after the DPA
  that the same conduct produced.** The failure class is identical both times, and it is the same
  shape the CCB run found at Coastal Financial the same day: **the controls were remediated; the
  exposure was not.** Three mitigating facts, stated because they are true: the Federal Reserve half
  of the 2024 order was terminated within twenty-one months; the 2024 matter is a **surveillance
  data-completeness** failure and not a finding of trading misconduct; and **the Firm's internal
  control over financial reporting has never been reported as ineffective in any of the five 10-Ks
  read, and no restatement appears in any of them.** That is the opposite of Coastal's material
  weaknesses and it is the distinction that keeps this a fired flag rather than a disqualifier.
- [ ] **UNINTELLIGIBLE FOOTNOTES — does not fire on intelligibility, and the honest verdict is
  "voluminous but not obscure."** The FY2025 10-K runs to about 1.43 million characters and 32
  notes. But every number this run needed was findable and internally reconcilable: the segment
  columns sum to consolidated net income to the dollar; equity recomputes from A − L to the dollar;
  the allowance is disaggregated by loan class; the deposit cost is derivable from the filer's own
  daily-average table; the buyback is published with **quarterly average prices paid per share**;
  the Level 3 hierarchy is published on both sides of the balance sheet. **Length is not the flag
  [E4-22] names.** *What cannot be verified is the mark on $33,732 million of Level 3 assets and
  $76,139 million of Level 3 liabilities, and that is carried into Q4 as exposure, not scored here
  as obscurity.*
- [x] **TRUMPETED EARNINGS PROJECTIONS / GROWTH TARGETS — FIRES, and [E3-48] then answers it in the
  Firm's favour.** JPMorganChase publishes an annual numeric Outlook in the 10-K itself. For 2026:
  *"Management expects net interest income to be approximately $103 billion and net interest income
  excluding Markets to be approximately $95 billion, market dependent… adjusted expense to be
  approximately $105 billion… the net charge-off rate in Card Services to be approximately 3.4%."*
  **Two of the three are non-GAAP measures and the filer says so.** **[E5-30]** is the reason this
  matters beyond one year: *"once you start it, it's all over. You can't quit… forecasting
  earnings, I can't imagine anything more destructive."* A guidance culture is a ratchet, and this
  one is twenty years old.
  **[E3-48]'s prescribed action — pull the past guidance and set it against the outturn — was
  performed, and the record is the candor case:**

  | 2025 guidance, given January 2025 and printed in the FY2024 10-K (`0000019617-25-000270`) | outturn, FY2025 10-K | |
  |---|---|---|
  | net interest income **approximately $94.0 billion** | **$95,443 million** | **beat by $1.4bn** |
  | NII excluding Markets **approximately $90.0 billion** | **$92,591 million** | **beat by $2.6bn (+2.9%)** |
  | adjusted expense **approximately $95.0 billion** | noninterest expense **$95,640 million** (GAAP) | on the number |
  | Card Services net charge-off rate **approximately 3.60%** | **3.31%** | **29 basis points better** |

  **Guided conservatively and beaten on three of three measurable items, in the same direction.**
  Buffett's stated remedy is to *"demand the record of the people who made the projections"*
  **[E3-48]**; the record was demanded and it is good. **The flag stays fired on the practice and is
  answered on the outturn.**
- [ ] **SERIAL SHARE ISSUANCE [E5-15] — DOES NOT FIRE, and the arithmetic is emphatic.**
  *"one of the surest indicators of a promotion-minded management, weak accounting, a stock that is
  overpriced and — all too often — outright dishonesty."* **The issued common share count is
  4,104,933,895 in the FY2021, FY2022, FY2023, FY2024 and FY2025 10-Ks and in the Q2 2026 10-Q — the
  same number, to the share, in all six filings.** **NOT ONE COMMON SHARE HAS BEEN ISSUED IN FIVE
  YEARS.** Every movement in the outstanding count is treasury: shares outstanding fell
  **3,049.4M (2020) → 2,944.1M → 2,934.2M → 2,876.6M → 2,797.6M → 2,696.2M → 2,658.2M (2026-06-30)**,
  a **12.8% reduction**. **The $192 billion First Republic acquisition was paid for in cash and a
  note, not in paper** ($13,524M to the FDIC net of cash acquired, a $48,848M Purchase Money Note at
  fair value, and $5,447M of settled deposits and financings) — so **[E5-44]**'s stock-deal law does
  not engage, and **[E2-52]**'s dividends-funded-by-issuance flag cannot fire: every dollar of the
  $65 billion of common dividends and the $82 billion of buybacks over five years came out of
  $251,081 million of net income.
- [ ] **EBITDA / ADJUSTED-EARNINGS PROMOTION [E4-29] — DOES NOT FIRE on EBITDA, and the check was
  made the way the CGNX ruling of 2026-09-07 requires** (the furnished earnings release, not only
  the annual report). **The word EBITDA appears nowhere in the FY2025 10-K.** The non-GAAP measures
  the Firm does promote are **ROTCE, tangible book value per share, pre-provision profit,
  "NII excluding Markets" and "adjusted expense"**, each reconciled in a dedicated section
  (pages 59–61). **The direction test [E2-69] cuts both ways here and is reported both ways:**
  ROTCE and TBVPS make the reported figures look **BETTER** (ROTCE 20% against an ROE of 17%,
  because the denominator excludes $64.3 billion of goodwill and intangibles the shareholder paid
  for) — that is the *flattering* direction; but **[E2-43]** is the corpus's own instruction that
  for an acquisitive filer *tangible* net assets are *"the best guide to the economic attractiveness
  of the operation"*, **so ROTCE is the measure this framework would have demanded anyway**, and
  the Firm publishes the goodwill wedge separately on the balance sheet rather than hiding it.
  **"Adjusted expense" and "NII excluding Markets", by contrast, are guidance metrics whose
  definitions the Firm controls, and those are the ones to watch — which is precisely the
  metric-switching test below.**
- [x] **FILED-FIGURE TELLS [E4-30] — one of the two is present and is explained, the other is
  refuted.**
  **Reported growth is NOT unnaturally smooth** — net income $48,334M → $37,676M → $49,552M →
  $58,471M → $57,048M, a 22% drop and a 32% recovery inside five years, and ROE 19 → 14 → 17 → 18
  → 17. Nothing is being ironed flat; the 2022 fall is fully visible.
  **The cash-tax tell:** the effective book tax rate ran **18.9% (2021), 18.4% (2022), 19.6%
  (2023), 22.1% (2024), 21.4% (2025)** — **rising, not falling**, which is the benign direction, and
  the rise is explained in the filings by the January 2024 change in accounting for tax-credit
  investments, which moved amortisation of alternative-energy investments out of other income and
  **into income tax expense**. **[E4-30]**'s tell is *falling* cash tax as a share of pretax income;
  the series here goes the other way and the flag is recorded as **tested and not fired**.
- [x] **METRIC-SWITCHING [E2-49] — FIRES, on a real and dated switch, and the switch was announced
  with reasons rather than following deterioration.** *"Yardsticks seldom are discarded while
  yielding favorable readings… demand pre-set, long-lived and small bullseyes."* **JPMorganChase
  reorganised from FOUR reportable segments to THREE with effect from 2024.** The FY2023 10-K
  reports *"four major reportable business segments… Consumer & Community Banking, the Corporate &
  Investment Bank (CIB), Commercial Banking (CB), and Asset & Wealth Management"*; the FY2025 10-K
  reports *"three reportable business segments – Consumer & Community Banking, Commercial &
  Investment Bank and Asset & Wealth Management."* **Commercial Banking, which the brief asked
  about as a separate segment with its own filed return on equity, no longer exists as a reporting
  unit — it was merged into the CIB in January 2024, and its former chief executive became
  co-CEO of the merged segment.** The effect on the reader is real: **the segment that held the
  commercial-real-estate book and reported a 15–19% return on equity on its own is now inside a
  $149.5 billion CIB reporting a blended 18%**, and the separate series is not restated forward.
  **[E2-56]** is the rule that bites — *"Their marvelous core businesses camouflage repeated
  failures in capital allocation elsewhere… judge retention segment-by-segment, never on the
  blended return"* — **and this reorganisation removed one of the four segments a reader had to
  judge with.** *What keeps this a fired flag rather than a disqualifier is that the switch was
  announced in advance, came with restated prior-year comparatives in the FY2024 10-K, was
  accompanied by a named management change, and did NOT follow deterioration: the former CB segment
  was profitable and growing when it was folded in. It is the announced-ahead-with-reasons case that
  [E2-49] calls the candor case, with the reader's loss recorded anyway.*
- [ ] **THE EXCEPT-FOR FLAG [E2-57] — does not fire.** The Firm quantifies its one-time items
  separately at every line and leaves them **in** the reported figures: the **$7.9 billion net Visa
  gain and the $1.0 billion Visa contribution** are footnoted to the 2024 revenue and expense lines
  rather than excluded; the **$2.9 billion FDIC special assessment** is in 2023 expense; the
  **$2.2 billion Apple Card lending-commitment provision** is in the 2025 provision with its
  25-basis-point capital effect stated. **[E3-53]**'s restructuring-charge test finds nothing: no
  restructuring charge appears in any of the five years, and **[E5-33]**'s rule that such costs
  belong in the owner-earnings mean is satisfied because they were never taken out.
- [ ] **DIVIDENDS FUNDED BY ISSUANCE [E2-52] — cannot fire.** Zero net issuance in five years.
- [ ] **STOCK-PRICE TARGETING [E3-50] — does not fire in the form the corpus names.** The Firm
  states the opposite of a price target: *"The common share repurchase program approved by the
  Board of Directors does not establish specific price targets or timetables."* **That sentence is
  read twice in this file — once here, where it acquits the Firm of price-targeting, and once
  below, where it is the exact failure of [E5-25]'s standard.**
- [x] **THE AUDITOR'S-EYE TEST [E4-34], fourth question — period-shifting.** The one place where
  reported earnings move between periods by management judgment at scale is the **allowance for
  credit losses**, and that is [E2-50]'s territory. It is tested next, as its own section, because
  for a bank it carries the Q3 weight.

### RESERVES — where dishonesty hides **[E2-50]**, tested against subsequent charge-offs

> *"Where 'earnings' can be created by the stroke of a pen, the dishonest will gather."*

| year | allowance for credit losses, year-end $M | net charge-offs, $M | provision, $M | **provision less charge-offs** | **allowance ÷ NEXT year's charge-offs** |
|---|---|---|---|---|---|
| 2019 | 14,314 | 5,629 | 5,585 | −44 | **2.72×** |
| 2020 | **30,815** | 5,259 | **17,480** | **+12,221** | **10.76×** |
| 2021 | 18,689 | 2,865 | **−9,256** | **−12,121** | **6.55×** |
| 2022 | 22,204 | 2,853 | 6,389 | +3,536 | **3.58×** |
| 2023 | 24,765 | 6,209 | 9,320 | +3,111 | **2.87×** |
| 2024 | 26,866 | 8,638 | 10,678 | +2,040 | **2.73×** |
| 2025 | **31,230** | 9,849 | **14,212** | **+4,363** | **3.34×** (H1 2026 annualised) |
| H1 2026 | 31,531 | 4,682 | 5,022 | +340 | — |

**THE RECORD IS CONSERVATIVE AND IT IS CONSERVATIVE BY A LARGE MARGIN.** Over the seven years
2019–2025 the cumulative provision was **$54,408 million against cumulative net charge-offs of
$41,302 million** — **$13,106 million, 31.7%, MORE reserved than lost** — and the allowance grew
from $14,314M to $31,230M while the loan book grew from about $1.0 trillion to $1.49 trillion.
**The allowance covered the following year's charge-offs at least 2.72 times in every single year
of the window, and 10.76 times in 2020.** Loss reserves have not been used to manufacture earnings;
they have been used to store them.

**AND THE ONE HONEST CRITICISM, WHICH IS THE CB RUN'S #23 THE CUSHION APPLIED HERE.** The
$17,480M pandemic build of 2020 and the **−$9,256M release of 2021** are the same money, and the
release landed in the year JPMorganChase reported its **best ROE and ROTCE of the window (19% and
23%)**. On the filer's own numbers, 2021 pre-tax income of $59,562M contains a $9,256M reserve
release: **15.5% of the best year's pre-tax income was a reversal of a provision taken the year
before.** That is not dishonesty — CECL requires it, the direction was disclosed, and the
subsequent charge-offs (2.865% and 2.853% of nothing like the modelled scenario) proved the release
right. **But a reader who reads 2021's 23% ROTCE as earning power is reading a release.** It is
recorded as a Q4 window distortion and as a Q6 monitoring item, not as a conduct finding.

**THE CANDOR BENCHMARK [E2-67] — and the answer is a qualified NO, stated precisely.** Berkshire
published a table of *its own reserving errors* *"so you can … judge whether we may have some
systemic bias"*, naming the direction. **JPMorganChase publishes no equivalent.** What it does
publish is the input rather than the error: the **weighted-average macroeconomic scenarios**
underlying the allowance, the allowance rollforward, the allowance allocated by loan class, and —
in the Q2 2026 10-Q, verbatim — *"Recognizing that forecasts of macroeconomic conditions are
inherently uncertain, the Firm believes that its process to consider the available information and
associated risks and uncertainties is appropriately governed and that its estimates of expected
credit losses were reasonable and appropriate for the period."* **That is a statement of confidence,
not a back-test.** A filer that published, each year, its prior year's allowance against the losses
that actually arrived would meet **[E2-67]** in form; JPMorganChase meets it only in substance, and
only because **a reader can construct the back-test from the published series — which is what the
table above is.** *Recorded as the one disclosure this reader wanted and did not get, and as the
Q6 monitoring metric.*

**ONE FORWARD-LOOKING ITEM THAT IS THE RIGHT DIRECTION AND IS WORTH NAMING.** The FY2025 provision
of $14,212M includes **$2.2 billion for lending-related commitments on the Apple Card transaction —
a portfolio the Firm does not acquire until approximately December 2027.** JPMorganChase took the
reserve, and about **25 basis points of Standardized CET1 (90 basis points Advanced)**, more than
two years before the exposure arrives. Reserving ahead of an event that has not happened is the
opposite of the [E2-50] failure mode.

### [E3-02] — THE NAMED FAILURE MODE IS CONFORMITY, AND FOR THIS BANK THE TEST HAS A DATE

> *"the tendency of executives to mindlessly imitate the behavior of their peers, no matter how
> foolish it may be to do so."*

**March to May 2023 is the only moment in the last two decades when this test could be run on a
large American bank against a control group that actually failed.** Three banks failed — Silicon
Valley Bank (2023-03-10), Signature Bank (2023-03-12), First Republic Bank (2023-05-01) — and the
mechanism in every case was the same: a held-to-maturity securities book bought at 2020–21 yields,
marked nowhere, funded by uninsured deposits that could leave in a day.

**The test is therefore: what did JPMorganChase's balance sheet look like at 2022-12-31, BEFORE any
of it was public?** From the FDIC Call Reports of all four institutions at that date, from the
issuing authority, one uniform definition:

| at **2022-12-31**, FDIC Call Report | assets $bn | equity $bn | **assets ÷ equity** | HTM securities $bn | **HTM ÷ equity** | AFS $bn | uninsured deposits % | noninterest-bearing deposits % |
|---|---|---|---|---|---|---|---|---|
| **JPMorgan Chase Bank NA** | **3,201.9** | **303.6** | **10.5** | 425.4 | **1.40×** | 205.8 | **44.2%** | 27.7% |
| Citibank NA | 1,764.1 | 164.3 | 10.7 | 262.9 | 1.60× | 222.5 | 45.4% | 13.8% |
| Wells Fargo Bank NA | 1,717.5 | 161.4 | 10.6 | 297.1 | 1.84× | 104.5 | 50.8% | 35.0% |
| Bank of America NA | 2,418.5 | 225.4 | 10.7 | **632.8** | **2.81×** | 192.1 | 40.4% | 35.9% |
| *Signature Bank* — **failed 2023-03-12** | 110.4 | 8.0 | 13.8 | 7.8 | 0.97× | 18.4 | **89.7%** | 35.7% |
| *First Republic Bank* — **failed 2023-05-01** | 212.6 | 17.4 | 12.2 | 28.4 | 1.63× | 3.3 | **67.7%** | 35.5% |
| *Silicon Valley Bank* — **failed 2023-03-10** | 209.0 | 15.5 | 13.5 | **91.3** | **5.91×** | 26.0 | **86.4%** | 47.3% |

**JPMorgan Chase Bank, N.A. carried the LOWEST held-to-maturity book relative to equity of all
seven institutions — 1.40 times, against Silicon Valley Bank's 5.91 and Bank of America's 2.81 —
and the lowest assets-to-equity ratio, 10.5. It also had the lowest uninsured-deposit share of the
four survivors bar Bank of America.** **[E3-02] is answered with a number and the answer is that it
did not imitate.** And the peer it most conspicuously did not imitate is the one closest to it in
size: **Bank of America held $632.8 billion of held-to-maturity securities at 2.81 times its bank
equity, exactly double JPMorgan's ratio** — and it is Bank of America whose ROTCE has since run
6.2 points below JPMorgan's on a five-year mean.

**JPMorgan's own filings carry the confirming mark.** At 2022-12-31 its HTM portfolio had an
amortized cost of **$425,305 million** against a fair value of **$388,648 million** — **$36,762
million of gross unrealized loss, which is 13.9% of the $264,928 million of common equity at the
same date.** Marked in full it would have cost a seventh of the equity. **The same mark at Silicon
Valley Bank was of the order of its entire equity.** That is the whole of the 2023 story in one
ratio, and the only thing JPMorganChase had to do to survive it was **not** reach for yield in 2021,
which the filings show it did not: it bought **$111.8 billion** of HTM securities in 2021 and only
**$33.7 billion** in 2022, on a balance sheet nine times Silicon Valley Bank's.

**Two further filed facts, both of which belong here and point in opposite directions.**
- **What it did with the position.** *"The Firm had placed a $5 billion deposit with First Republic
  Bank on March 16, 2023, as part of $30 billion of deposits provided by a consortium of large U.S.
  banks. The Firm's $5 billion deposit was effectively settled as part of the acquisition and the
  associated allowance for credit losses was released upon closing. The Firm subsequently repaid
  the remaining $25 billion of deposits to the consortium of banks."* JPMorganChase put $5 billion
  of its own money into a bank it then bought from the receiver six weeks later, and recovered it in
  the settlement. **[E2-64]** is the right lens — *"the most attractive opportunities may present
  themselves at a time when credit is extremely expensive — or even unavailable"* — and this is a
  balance sheet built for the storm being used to buy in it.
- **What the regime charged it for surviving.** The FY2023 10-K records a **$2.9 billion FDIC
  special assessment** in noninterest expense — a levy on the surviving large banks to fund the
  uninsured depositors of the three that failed. **The regime that granted the First Republic
  opportunity also sent the bill**, and both belong in the [E2-59] ledger at Q2.

### STEP 3 — THE PRIMARY TEST **[E2-01]**

> **"The primary test of managerial economic performance is the achievement of a high earnings rate
> on equity capital employed (without undue leverage, accounting gimmickry, etc.) and not the
> achievement of consistent gains in earnings per share."**

### HOW THIS RUN MEASURES RETURN ON EQUITY CAPITAL FOR A BANK — LABELLED CONVENTION, PRIME RULE 3

> **CONVENTION (JPM, 2026-09-19).** *The same construction the CCB run wrote on 2026-09-19 and the
> ACNB run adopted the same day, **adopted here because JPMorganChase's filings do not make it
> wrong**, with **the CNR modification ACNB added** and **one further modification this filer
> forces, disclosed below.** Owner earnings by the ordinary construction — operating cash flow less
> share-based compensation less a maintenance-capex guess — does not work for a bank, and
> JPMorganChase's own statements show why in three lines. **(i) Operating cash flow is not a
> return** for a company whose operating section contains the movement of a $1.06 trillion trading
> book and $432.9 billion of resale agreements. **(ii) There is no maintenance capex that matters:**
> premises and equipment stood at **$37,701 million against $5,015,069 million of assets — 0.75%** —
> and a loan book does not wear out. **(iii) Deposit and loan flows are financing and investing**,
> so the cash statement of a bank measures the direction of its balance sheet, not its earnings.*
>
> ***The metric set is therefore selected by business type first, as [E5-37] requires*** (*"different
> numbers are of different importance … depending on the kind of business"; "there is not
> one-size-fits-all"*) ***and the metric is the one the corpus itself names — [E2-01]'s "high
> earnings rate on equity capital employed". Four measures, all from filed statements:***
> 1. ***return on average common equity***, as the filer reports it;
> 2. ***return on average TANGIBLE common equity***, because **[E2-43]** says that for an acquisitive
>    filer the denominator is unleveraged net tangible assets — *"the best guide to the economic
>    attractiveness of the operation"* — **with the goodwill wedge reported separately and never
>    hidden inside book equity.** JPMorganChase has made five decades of acquisitions, so this is
>    the **governing** denominator, and the wedge is **$64,304 million of goodwill, MSRs and other
>    intangibles at 2026-06-30, 18.2% of common equity** — reported here, on its own line, exactly
>    as the filer reports it;
> 3. ***return on average assets***, the one bank ratio immune to the leverage choice and therefore
>    to **[E2-47]**'s carve-out for unusual debt-equity ratios;
> 4. ***the (c) EQUIVALENT, which is the part that is ours.*** *For a bank, the expenditure the
>    business "requires to fully maintain its long-term competitive position and its unit volume"
>    **[E2-23]** is not plant. It is **the equity that must be retained to hold the regulatory
>    capital ratio constant while the balance sheet grows** — a bank that grows assets and does not
>    retain the matching capital must stop growing or sell shares. So **(c) = Δassets × the Firm's
>    Tier 1 leverage ratio**, and **"owner earnings" for a bank = net income − (c)**. Its corpus
>    anchor is **[E2-60]**'s third dimension of maintenance, which is explicitly **"its financial
>    strength"**.*
>
> ***MODIFICATION 1 — THE CNR RULE, inherited from ACNB: Δassets is SPLIT into organic and
> acquired.*** *JPMorganChase's 2023 asset increase of $209,650 million contains **$192,231 million
> of assets that arrived on 2023-05-01 from the FDIC as receiver of First Republic Bank**. Charging
> the acquired perimeter's capital requirement against that year's earnings would be arithmetic
> about an acquisition dressed up as arithmetic about earning power. **So (c) is computed on the
> ORGANIC perimeter and the acquisition's capital cost is stated separately, in full, on its own
> line.*** ***But the CNR rule applies DIFFERENTLY here from ACNB and the difference is stated:
> ACNB paid for its acquisition with newly issued stock, so the acquired capital arrived with the
> assets; JPMorganChase paid $67,834 million in cash, a note and settled deposits, and issued no
> shares — so the capital behind the acquired perimeter DID come out of retained earnings, and the
> $13,264 million charge is real. Both figures are below and neither is hidden.***
>
> ***MODIFICATION 2 — THIS FILER FORCES A SECOND ONE, AND IT IS NEW TO THE CONVENTION. For a bank
> with a $1.06 trillion trading book, total assets are the wrong base and the run says so rather
> than using them silently.*** *Roughly half of JPMorganChase's 2025–26 asset growth is Markets
> balance sheet — trading assets rose $259 billion and resale agreements and securities borrowed
> rose $262 billion in the six months to 2026-06-30 — which is client-driven, low-risk-weight, and
> **seasonally larger at mid-year than at year-end** (the filer says so: *"as well as when compared
> with seasonally lower levels at year-end"*). **So the convention is run twice, once on total
> assets at the Tier 1 leverage ratio and once on RISK-WEIGHTED assets at the Firm's own 11.5% CET1
> requirement, and the two are reported side by side. They agree to within 12% in 2025
> ($29,124M against $25,787M), which is the robustness check that licenses using either; and the
> half-year figure is NOT annualised, because the balance sheet it is struck on is the seasonal
> peak.***
>
> *Share-based compensation is already an expense in every figure above and is **not** added back
> **[E5-06]**; the Firm does not disclose a separate consolidated SBC charge in the filings read,
> and it is immaterial against $95,640 million of noninterest expense. **[E3-70]**'s grant-value
> measure is not constructed and cannot change a verdict at this scale — and the count test settles
> it independently: **zero net shares issued in five years.***

**THE SERIES. Balance sheet before income statement, as [E2-01] requires.**

| | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 ann. |
|---|---|---|---|---|---|---|
| net income, $M | 48,334 | 37,676 | 49,552 | 58,471 | 57,048 | **75,298** |
| **ROE, as filed** | **19%** | **14%** | **17%** | **18%** | **17%** | **22%** |
| **ROTCE — the [E2-43] denominator** | **23%** | **18%** | **21%** | **22%** | **20%** | **26%** |
| ROA | 1.30% | 0.98% | 1.30% | 1.43% | 1.29% | 1.56% |
| book value per share | $88.07 | $90.29 | $104.45 | $116.07 | $126.99 | **$133.01** |
| **tangible book value per share** | **$71.53** | **$73.12** | **$86.08** | **$97.30** | **$107.56** | **$113.35** |
| diluted EPS | $15.36 | $12.09 | $16.23 | $19.75 | $20.02 | **$27.26** |
| effective book tax rate | 18.9% | 18.4% | 19.6% | 22.1% | 21.4% | — |
| common shares outstanding, M | 2,944.1 | 2,934.2 | 2,876.6 | 2,797.6 | 2,696.2 | **2,658.2** |

**WHAT THE SERIES SAYS, AND IT SAYS ONE THING CLEARLY AND ONE THING THAT NEEDS UNPICKING.**

**Clearly: this is the best large-bank return record in the United States and it is not close.**
Five-year mean ROTCE **20.80%**, first of six in four of the five years, minimum 18% — and the
filer's own relative claim, which Row A at Q2 corroborates: *"In the past 10 years, achieving
reported ROTCE of ≥18% has been rare amongst our PSU peers. JPMorganChase achieved it 6 times, and
our 10 PSU peers combined have only achieved it 8 times."* **[E2-01]** is defined *in opposition to*
EPS growth, and here both point the same way: **tangible book value per share compounded from
$66.11 at 2020-12-31 to $113.35 at 2026-06-30, +71.5% in five and a half years, 10.3% a year,
while the share count fell 12.8% and $65 billion of dividends were paid.** That is the arithmetic
of a business earning well above its cost of capital and returning the surplus.

**Needing unpicking: a third of the equity is not earning that return, and the reported figure is
the blend.** **[E2-56]** is explicit — *"Their marvelous core businesses camouflage repeated
failures in capital allocation elsewhere… judge retention segment-by-segment, incrementally, never
on the blended return."* Applied:

| FY2025, on the filer's own capital allocation | allocated equity $bn | % of common equity | net income $M | **return on allocated equity** |
|---|---|---|---|---|
| **Asset & Wealth Management** | **16.0** | 4.7% | 6,522 | **40%** |
| **Consumer & Community Banking** | **56.0** | 16.4% | 18,245 | **32%** |
| **Commercial & Investment Bank** | **149.5** | **43.7%** | 27,761 | **18%** |
| **Corporate** | **120.9** | **35.3%** | 4,520 | **≈3.7%** (the filer reports "NM") |
| **Total** | **342.4** | 100% | **57,048** | **17%** |

**ALL THREE OPERATING SEGMENTS EARN FAR ABOVE ANY PLAUSIBLE COST OF THE CAPITAL ALLOCATED TO THEM,
AND THE FOURTH — WHICH HOLDS MORE THAN A THIRD OF THE COMMON EQUITY — EARNS ABOUT A GOVERNMENT-BOND
RETURN.** The filer says exactly why, and the sentence is the most important disclosure in this Q3:
*"Any capital that the Firm has accumulated in excess of these current requirements, including the
capital required to meet the potential increased requirements of the U.S. Basel III proposal, has
been retained in Corporate in addition to its allocated balance."* **Corporate is the regulatory
buffer.** At 2025-12-31 CET1 capital was **$288,469 million against a Standardized requirement of
11.5% on $1,981,692 million of risk-weighted assets, i.e. $227,895 million — an excess of
$60,574 million**, and the Firm has since begun releasing it: **Corporate's allocated equity falls
from $120.9 billion to $98.4 billion on 2026-01-01, with $5.5 billion going to CCB and
$17.0 billion to the CIB.**

**So the honest reading of [E2-01] for JPMorganChase is: the operating businesses earn 18% to 40%,
the 17% blended ROE is diluted by a 35% allocation earning 3.7%, and the amount of the dilution is
set by the Federal Reserve rather than by management.** That is the single largest structural fact
about this company's return, it is disclosed, and it goes straight into Q5 — because a buyer at
today's price is buying the blend.

**THE (c) RECORD, and it is the opposite of Coastal Financial's:**

| year | Δ assets $M | less assets acquired | **organic Δ assets** | Tier 1 leverage, as filed | **(c) leverage basis** | *(c) RWA basis, at 11.5% CET1 req* | net income $M | **net income − (c)** |
|---|---|---|---|---|---|---|---|---|
| 2021 | +358,810 | — | +358,810 | 7.2% | **25,834** | — | 48,334 | **+22,500** |
| 2022 | −77,824 | — | −77,824 | 7.2% | **0** | — | 37,676 | **+37,676** |
| 2023 | +209,650 | **192,231** (First Republic, 2023-05-01, from the FDIC as receiver) | **+17,419** | 6.9% | **1,202** | — | 49,552 | **+48,350** |
| 2024 | +127,421 | — | +127,421 | 7.2% | **9,174** | *4,449* | 58,471 | **+49,297** |
| 2025 | +422,086 | — | +422,086 | 6.9% | **29,124** | *25,787* | 57,048 | **+27,924** |
| *H1 2026 — **NOT annualised**, seasonal peak* | *+590,169* | — | *+590,169* | *6.6%* | *38,951* | — | *37,649* | *−1,302* |

- **The acquired perimeter's capital cost, stated separately in full: $192,231 million × 6.9% =
  $13,264 million**, and unlike ACNB's case **it was funded out of retained earnings rather than by
  issuing stock**, so a reader who wishes to charge it to 2023 may: the five-year mean then falls
  from $37,149 million to **$34,497 million**. Both figures are carried at Q4.
- **Five-year organic (c): $65,334 million; with the acquisition, $78,598 million — against
  cumulative net income of $251,081 million. A surplus of $172,483 million.** **The same CONVENTION
  applied to Coastal Financial on 2026-09-19 produced a $111.6 million SHORTFALL and applied to
  ACNB a $143.8 million surplus; applied to JPMorganChase it produces a $172.5 BILLION surplus.
  The construction is not tuned to a result.**
- **And the balance sheet confirms it independently, which is the point of building it this way.**
  Common equity rose **$93,102 million** from 2020-12-31 ($249,291M) to 2025-12-31 ($342,393M) while
  cumulative net income was **$251,081 million**, common dividends about **$65 billion** and
  buybacks **$81,949 million**. **No common share was issued.** So retained earnings alone funded
  the dividend, the buyback, the $192 billion acquisition and the entire organic balance sheet.
  **[E2-60] passes on its own terms:** these are not restricted earnings — the payout did not cost
  the business its financial strength, and the CET1 ratio at 2026-06-30 (14.2%) is still 2.7 points
  above the 11.5% requirement.

**THE HALF-OWNER TEST [E2-26]** — *does this reporting tell me what I would want to know if the
positions were reversed?* **Mostly yes, and unusually so for a company this size, with two
identifiable gaps.**
- **What is disclosed and separately quantified:** allocated equity and return by segment; the
  capital allocation methodology and the fact that excess capital sits in Corporate; quarterly
  average prices paid per share for buybacks; the allowance by loan class; the daily-average balance
  sheet with rates on every line; the criticized-exposure total by industry; Level 3 on both sides;
  the numeric forward outlook; the reasonably-possible-loss range; and the goodwill wedge on its own
  balance-sheet line.
- **Gap 1, and it is the one the reader most wanted: no reserving back-test [E2-67].** Covered above.
- **Gap 2: the segment that was removed.** Commercial Banking's separate return series ended with
  2023. **[E2-56]** wanted it and it is gone.

**THE INSTITUTIONAL IMPERATIVE — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] **resists any change in current direction — DOES NOT FIRE, and the 2023–24 record is why.**
  The Firm merged two of its four segments, changed the chief executives of both consumer and
  wholesale banking in January 2024 (Marianne Lake sole CEO of CCB; Piepszak to Chief Operating
  Officer; Rohrbaugh and Petno co-CEOs of the merged CIB), bought a failed bank from a receiver in
  six weeks, and took on the Apple Card portfolio in 2026. Whatever else this is, it is not
  institutional inertia.
- [x] **projects or acquisitions materialise to soak up available funds — FIRES, and it is the
  live one.** **[E2-30]**'s second behaviour is available funds finding a use. The Firm has
  $60.6 billion of CET1 above its requirement; in 2025 it (i) committed to the **Apple Card
  portfolio**, taking a $2.2 billion provision and ~90 basis points of Advanced CET1 for an asset
  that arrives in about December 2027, (ii) grew assets **$422 billion**, and (iii) spent
  **$31.6 billion** on its own shares at 2.57 times tangible book. **The buffer is being deployed,
  and the question of whether it is being deployed well is the capital-allocation test below.**
- [ ] staff studies produced to justify the leader's craving — not observable from filings.
- [ ] **peer behaviour mindlessly imitated [E3-02] — DOES NOT FIRE, and it is this company's best
  mark.** The 2022-12-31 table above is the evidence: the lowest HTM-to-equity ratio of seven
  institutions, half Bank of America's, a quarter of Silicon Valley Bank's. **Tested against a
  control group that actually died, and found in JPMorganChase's favour.**

### THE INCENTIVE READ **[E4-27]** — *"Never, ever, think about something else when you should be thinking about the power of incentives."*

From the DEF 14A of 2026-04-06 (`0000019617-26-000096`):
- **Mr Dimon's 2025 total compensation was $40,644,723.** Cash award **$5 million**, capped at 25%
  of total compensation and deliberately set below the cap; **100% of his equity is in at-risk
  Performance Share Units**, about 88% of variable pay — *"a higher proportion than any of our peer
  firms' CEOs"*, and total cash *"consistently among the lowest"* against a ~$12 million peer median.
- **The PSU pays on absolute and relative ROTCE over three years.** *"For the 2025 PSU award, the
  CMDC set the absolute ROTCE thresholds as follows: (1) maximum payout at 18% or greater; and (2)
  zero payout at less than 6%,"* with payout 0% to 150%.

**Two readings, and both are written down.**

**FOR:** **the metric the chief executive is paid on is the metric this framework's primary test
demands.** **[E2-01]** asks for the earnings rate on equity capital employed and **[E2-43]** says
the denominator for an acquisitive filer is tangible net assets. **That is ROTCE.** It is a
pre-set, long-lived, small bullseye of exactly the kind **[E2-49]** demands, it has not been
switched, and it is the opposite of the ACNB and CCB defect where the incentive metric excluded the
risk that mattered. **Almost no large company pays its chief executive on the number this framework
would have chosen.**

**AGAINST, and it is the sharpest finding in this Q3 after the cockroach rule: the denominator is
something management can shrink, and it has been shrinking it hard.** ROTCE is earnings ÷ average
tangible common equity. **Buying back stock at 2.57 times tangible book removes cash from the
numerator's base and tangible equity from the denominator, and the denominator effect dominates.**
The arithmetic, from filed figures:
- Cumulative buybacks 2021–2025: **$81,949 million, 418.4 million shares, average $195.86.**
- Tangible common equity at 2025-12-31: **$290,003 million** ($107.56 × 2,696.2M).
- **Had none of the $81,949 million been spent, 2025 ROTCE on the same earnings would have been
  approximately 16.1% rather than the reported 19.9%.** The five-year buyback programme accounts
  for roughly **3.8 points of the reported 20%** — **and the maximum PSU payout threshold is 18%.**
- The 2025 buyback alone accounts for about **1.1 points**.

**[E5-38] governs the conclusion: a fired flag is not a venality finding** — the flag reads the
incentive, and the binary **[E5-16]** judges the person on conduct. **Nothing here suggests the
buyback was done to hit a PSU threshold**, and the simplest explanation is the one the filer gives:
excess capital with nowhere better to go. **But a chief executive whose entire equity award pays at
maximum above 18% ROTCE, and who can add nearly four points to ROTCE by retiring equity, is looking
at an incentive the framework is required to notice, and it is noticed here.**

### CAPITAL ALLOCATION — the two buyback conditions **[E5-08]**, plus the third **[E4-31]**

| year | shares repurchased, M | $M | **average price paid** | book value/share | **price ÷ book** | tangible book/share | **price ÷ TANGIBLE book** |
|---|---|---|---|---|---|---|---|
| 2021 | 119.7 | 18,448 | $154.12 | $88.07 | 1.75× | $71.53 | **2.15×** |
| 2022 | 23.1 | 3,122 | $135.15 | $90.29 | 1.50× | $73.12 | **1.85×** |
| 2023 | 69.5 | 9,898 | $142.42 | $104.45 | 1.36× | $86.08 | **1.65×** |
| 2024 | 91.7 | 18,841 | $205.46 | $116.07 | 1.77× | $97.30 | **2.11×** |
| **2025** | **114.4** | **31,640** | **$276.55** | $126.99 | **2.18×** | $107.56 | **2.57×** |
| **today, 2026-09-18** | — | — | **$349.67** | **$133.01** | **2.63×** | **$113.35** | **3.08×** |
| *2021–2025 total* | *418.4* | *81,949* | *$195.86* | | | | |

- **(1) ample funds for operations and liquidity? YES, and emphatically.** CET1 14.2% against an
  11.5% requirement; Firm liquidity coverage ratio 110% and the Bank's 118%; $60.6 billion of CET1
  above requirement at 2025-12-31.
- **(2) repurchases at a MATERIAL DISCOUNT to intrinsic business value, conservatively calculated?
  THIS FAILS, and it is a CAPITAL-ALLOCATION FLAG.** **[E5-24]** is the first law: *"whether the
  money is slated for acquisitions or share repurchases … **what is smart at one price is dumb at
  another**."* **JPMorganChase spent $9.9 billion on its own shares at 1.65 times tangible book in
  2023 and $31.6 billion at 2.57 times tangible book in 2025 — THREE TIMES THE DOLLARS AT 1.6 TIMES
  THE PRICE.** That is the first law inverted, on the filer's own quarterly table, and the 2025
  quarterly series shows it getting worse within the year: $252.50 in the first quarter and $317.28
  in December. **A conservative calculation of intrinsic value cannot show a *material discount* at
  3.08 times tangible book, which is where the stock is today.**
- **(3) the third condition [E4-31] — *"Shareholders should have been supplied all the information
  they need for estimating that value"* — PASSES**, and by a wide margin. This is the most
  comprehensively disclosed company this project has run.
- **[E5-25] IS THE STANDARD AND JPMORGANCHASE EXPLICITLY DECLINES IT.** Berkshire published *both*
  conditions as numbers in advance — the 110%-of-book limit and the $20 billion liquidity floor —
  because *"financial strength that is unquestionable takes precedence over all else."*
  JPMorganChase states the opposite in terms: *"The common share repurchase program approved by the
  Board of Directors **does not establish specific price targets or timetables**."* **A programme
  with no published price discipline, executed at a rising multiple in rising size, is the
  behaviour [E5-24] warns against, whatever the intent.**
- **THE COUNTER-ARGUMENT, STATED AS WELL AS ITS HOLDERS WOULD STATE IT [E4-51], BECAUSE IT IS
  STRONG.** *The alternative use of the money is not 20% ROTCE. It is Corporate, which earns about
  3.7% on $120.9 billion. A share bought at 2.57 times tangible book in a business earning 20% on
  tangible book returns roughly 20/2.57 ≈ 7.8% on the cash spent, forever, and growing — which is
  materially better than 3.7%, better than the 5.34% thirty-year Treasury, and it reduces the
  regulatory capital the Firm is forced to hold idle. On that comparison the 2025 buyback is the
  best available use of trapped capital, and the rising multiple is a consequence of the business
  working, not a failure of discipline.* **I think that argument is right about the comparison and
  wrong about the standard.** **[E5-08]** does not ask whether a buyback beats the next-best use; it
  asks for a **material discount to conservatively calculated intrinsic value**, and 7.8% on cash
  spent is not a material discount — it is a fair price. **[E5-31]** is the tie-breaker and it sides
  with the flag: the order is business needs first, then acquisitions versus repurchases **by
  per-share value added at the price** — and value added at 3.08 times tangible book is thin.
- **[E2-51] does NOT fire** — a manager who *refuses* repurchases *"reveals more than he knows of
  his motivations."* JPMorganChase does the opposite. **[E4-50]**'s aggressive-at-a-discount
  licence is being used without the discount that licenses it.

**THE FLAG, STATED WITH THE HUMILITY CLAUSE [E4-13] AS THE FRAMEWORK REQUIRES.**
> **CAPITAL-ALLOCATION FLAG — LIVE.** Repurchases at 2.18× book and 2.57× tangible book in 2025,
> rising within the year, three times the 2023 dollar amount at 1.6 times the 2023 price, under a
> programme that states it sets no price targets. **This rests on our own intrinsic-value range and
> [E4-13] applies: *"it is natural for CEOs to be optimistic about their own businesses. They also
> know a whole lot more about them than I do"*, and *"infractions, even serious ones, are innocent;
> many CEOs never stop believing their stock is cheap"* [E5-08]. The flag binds POSITION SIZE.
> It does not touch the discount rate.**

### THE GUARDRAIL — checked before writing the verdict

- [x] **Confirmed: nothing in this Q3 is being used to PROMOTE the name.** **[E2-37, E2-38, E3-39]**
  — *"a textile company that allocates capital brilliantly within its industry is a remarkable
  textile company — but not a remarkable business"*; *"Good jockeys will do well on good horses, but
  not on broken-down nags."* The 2022 held-to-maturity discipline and the 20.8% five-year mean ROTCE
  are the best facts in this file and **neither promotes the name**. Q2 passed on a measured
  operating-cost advantage, not on management, and Q5 will judge the price.
- [x] **The business REQUIRES daily competence, and that is recorded at Q2 as a moat defect
  [E4-23]**, which it was — *"if a business requires a superstar to produce great results, the
  business itself cannot be deemed great."* **It is written there and not here as a strength.**
  And **[E4-33]**'s knight sets the moat's *direction*, never its *existence*: the widening
  overhead-ratio advantage is the filed evidence of a knight, and it changes the class not at all.
- [x] **Is a great manager the reason to act? NO, and the question is asked precisely because a
  reader would want to make it the reason.** **[E2-35, E2-36]** — is the franchise intact and the
  damage excisable, or **is the manager the plan**? The franchise is intact and there is no
  *"localized excisable cancer"* to excise, so the exception class does not arise. **And the one
  fact that makes this question live is not in the filings as a risk factor and is stated as a
  judgment: Mr Dimon has run this company since 2005 and is 70.** **[E4-23]** locates key-person
  dependence at Q2, where it is already recorded; **[E2-48]**'s superstar tell — *"these champs have
  made very few deals in recent years, and often have found repurchase of their own shares to be the
  most sensible employment of corporate capital"* — is half met (few deals, heavy repurchase) and
  half contradicted (the repurchase is at 2.57× tangible book, not at a discount). **The corpus
  names its superstars rather than denying them [E2-48, E3-63]; this run names the tell as HALF met
  and declines to claim the class**, because the second half of the tell is the price, and the price
  is where this name is about to fail.

- **VERDICT: [x] IN — at GATE weight  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**IN means no disqualifier was found. It is NOT a finding that the managers are honest —
*"sincerity and empathy can easily be faked"* [E5-17] — and it never promotes.** It is carried with:
- a **live CAPITAL-ALLOCATION FLAG** which binds position size and not the discount rate;
- the **cockroach finding** on trade-surveillance controls, fired twice in the same failure class
  four years apart;
- the **metric-switching** finding on the loss of Commercial Banking as a reportable segment; and
- the **[E2-67] gap**: no reserving back-test is published, and the one in this file was built by
  the reader.

*Why this is IN and not UNRESEARCHED, stated so a reader can disagree. Q3 is a GATE here, and at
gate weight the framework forbids an IN that carries "unverified" or "provisional". **The decisive
artifact was named and then obtained**, from the issuing authority rather than from a filing's
one-sentence summary: the Federal Reserve's own enforcement register, all 2,889 actions, which
shows thirteen entity actions against JPMorgan Chase & Co. since 2003, **zero orders open**, the
most recent terminated within twenty-one months, and open orders still standing against Citigroup
and Wells Fargo. **That is [E5-22]'s test — did they act when they learned — answered by the
supervisor's own termination dates, and it is the reason this run does not reach the conclusion the
Citigroup 2007 case reached on a record of LIVE matters.** The residual work order that remains is
named at the self-audit and it is not decision-changing: the **text** of the March 2024 OCC consent
order, which lives on the OCC's enforcement-action register, a rung this run did not reach.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — and for a bank the construction is the CONVENTION declared at Q3

The CONVENTION is stated in full at Q3 STEP 3 and is not restated. Its operative parts: **"owner
earnings" for a bank = net income − (c)**, and **(c) = the equity that must be retained to hold the
regulatory capital ratio constant while the balance sheet grows**, computed on the **organic**
perimeter (the CNR rule), run on **both** total assets at the Tier 1 leverage ratio **and**
risk-weighted assets at the 11.5% CET1 requirement, and **never annualised from a half-year struck
on the seasonal balance-sheet peak.**

**A CORRECTION MADE IN THE RUN, recorded rather than edited out, per operator rule 6.** The Q1
section above says *"Level 3 assets of $76,139M are 21.5% of common equity."* **That figure is the
Level 3 LIABILITIES total, not assets.** From the Q2 2026 10-Q's own fair-value table:
**Level 3 ASSETS are $33,732 million — 1% of total Firm assets and 9.5% of common equity** — and
**Level 3 LIABILITIES are $76,139 million, 21.5% of common equity.** The Q1 sentence conflated the
two. The corrected figures are the ones used below; the error is left visible above and logged in
the self-audit.

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE **[E4-25, E4-38]**

*"Using precise numbers is, in fact, foolish; working with a range of possibilities is the better
approach."* And **[E4-38]**'s remedy for date-selection distortion is to publish **every** window.
**Six are published, and the (c) band is published on top of them, because the two together are the
range.**

**THE (c) BAND — a DISCLOSED JUDGMENT, and for a bank it is not capex at all.** The corpus default
(D&A as the proxy for (c), **[E3-44, E2-41]**) is **inapplicable and is not used**: premises and
equipment stood at $37,701 million against $5,015,069 million of assets, and nothing in
JPMorganChase's filings says depreciation understates renewal, so **[E5-20]**'s exception class is
silent too. **The judgment inside (c) is the growth rate charged as maintenance, and the band is
disclosed:**
- **(c) LOW = $7,633 million** — 2.5% nominal asset growth (roughly inflation, so real unit volume
  is held) at the 6.9% Tier 1 leverage ratio. **[E2-23]**'s words are *"requires to fully
  **maintain** … its unit volume"*, and growth beyond inflation is discretionary expansion.
- **(c) MID = $13,067 million** — the actual five-year mean of the organic (c) computed at Q3.
- **(c) HIGH = $29,124 million** — the 2025 figure, i.e. treating all the growth actually pursued
  as required.

| window | net income, $M | **less (c) LOW** | **less (c) MID** | **less (c) HIGH** | yield on the $929,488M cap, at (c) MID |
|---|---|---|---|---|---|
| **FY2025** | 57,048 | **49,415** | **43,981** | **27,924** | **4.73%** |
| **five-year mean, 2021–2025** | 50,216 | **42,583** | **37,149** | 21,092 | **4.00%** |
| five-year mean, charging First Republic's $13,264M to 2023 | 47,563 | 39,930 | **34,497** | 18,439 | 3.71% |
| three-year mean, 2023–2025 | 55,024 | 47,391 | 41,957 | 25,900 | 4.51% |
| FY2024 (the peak year) | 58,471 | 50,838 | 45,404 | 29,347 | 4.89% |
| *H1 2026 annualised — **NOT USED**: contains a $4.6bn Visa gain and $1.0bn of equity gains, and its (c) is struck on the seasonal peak* | *75,298* | *—* | *—* | *—* | *—* |

- **Short-window mean** (FY2025, at (c) MID): **$43,981 million**
- **Long-window mean** (2021–2025, at (c) MID): **$37,149 million**
- **Spread, conservative end:** the long window is **15.5% below** the short one.
- **COMBINED RANGE (window spread × (c) band), and this is the number that goes to Q5:
  $27,924 million to $49,415 million — a yield of 3.00% to 5.32% on the market capitalisation, and
  a PRE-TAX yield of 3.82% to 6.76% grossed up at the Firm's own 21.4% effective rate.**
- **Is that range too wide to reach a conclusion? NO — and the reason is specific, so this is a
  judgment and not a convenience.** The width is almost entirely the **(c) band**, not the earnings:
  net income across the five years runs $37,676M to $58,471M, a spread of 55%, but four of the five
  years sit between $48bn and $59bn and the outlier (2022) is explained in the filings by a $6,389M
  provision and no Visa gain. **The (c) band is wide because 2025's asset growth of $422 billion was
  roughly half Markets balance sheet, which the filer itself calls seasonal, and Markets balance
  sheet is not "unit volume" in [E2-23]'s sense.** So the run takes the range and carries it, and
  says which end it believes: **the (c) MID end, $37,149M to $43,981M, 4.00% to 4.73% of the cap.**
  **[E4-25]**'s *"too wide"* verdict is **NOT** invoked, and the reason is written here so a reader
  can disagree.
- **A distorted year sits in the window and it is NAMED [E5-11, E4-41].** **Three, in fact, and all
  three are removed or flagged before the mean is trusted, because [E4-41] requires favourable
  exogenous breaks to be named and removed:**
  1. **2021 contains a −$9,256 million provision, i.e. a $9.3 billion reserve RELEASE** — 15.5% of
     that year's pre-tax income and the reason 2021 shows the window's best ROTCE of 23%.
  2. **2024 contains a $7.9 billion net Visa gain** in revenue (partly offset by a $1.0 billion
     Visa contribution in expense) — 13.5% of that year's pre-tax income, and the reason 2024 is
     the peak.
  3. **2023 contains the $2,775 million First Republic bargain purchase gain** and, against it, the
     **$2.9 billion FDIC special assessment**; the two roughly cancel, which is worth stating
     because a run that removed only the gain would understate the year.
  **Stripping all three, the five-year mean net income falls from $50,216M to roughly $46,300M and
  the (c)-MID owner-earnings mean from $37,149M to about $33,200M — a 3.57% yield.** That figure is
  carried to Q5 as the conservative boundary **[E5-34]** requires.
- **Stock compensation [E5-06]:** already an expense in every figure, not added back; not separately
  disclosed at the consolidated level in the filings read, and immaterial against $95,640 million of
  noninterest expense. **[E3-70]**'s grant-value question cannot change a verdict here, and the
  count test settles it independently: **zero net common shares issued in five years.**
- **[E3-04]'s look-through addition is NOT made and the reason is stated:** JPMorganChase has no
  material equity-method stake whose undistributed earnings are excluded from net income; its
  principal investments ($54.1 billion) are carried at fair value with the changes in income.
- *If the (c) band changes the verdict → UNKNOWABLE.* **It does not.** At (c) LOW the pre-tax yield
  is 6.76% and at (c) HIGH it is 3.82%; **at every point in the band the Q5 answer is the same one**
  — below the ~10% floor. **The band moves the number and not the answer, which is the only
  condition under which a band is allowed to stand.**

### Great, good, or gruesome? **[E4-20]**

- [ ] great — high return, rising, little capital needed
- [x] **good** — attractive return, earned also on capital that is added
- [ ] gruesome — grows, eats capital, earns little

**Evidence, and the boundary call is argued rather than asserted.**

**Not gruesome, and not close.** The gruesome test is *"grows rapidly, requires significant capital
to engender the growth, and then earns little or no money."* JPMorganChase earns **20.8% on
tangible common equity on a five-year mean** and needed **$65,334 million of organic retained
capital over five years against $251,081 million of net income** — a $172 billion surplus, from
which it paid $65 billion of dividends and bought $82 billion of its own stock without issuing a
share. **[E4-43]** is applied so as not to over-read the class: the *good* class **passes** —
*"nothing shabby about earning $82 million pre-tax on $400 million of net tangible assets"* — and
**[E5-40]**'s ~12% on retained capital is *"quite satisfactory"*. JPMorganChase earns roughly 20%.

**Not great, and the reason is the whole of this run's Q5.** The *great* class *"pays an
extraordinarily high interest rate that will rise as the years pass"* and needs **little capital**.
JPMorganChase needs an enormous amount of capital and **is not free to choose how much**: at
2025-12-31, **$120.9 billion — 35.3% of the common equity — sat in Corporate earning about 3.7%**,
because the Federal Reserve requires 11.5% of $1,981,692 million of risk-weighted assets and the
Firm held $288,469 million, an excess of **$60,574 million**. **The business earns 18% to 40% on the
capital it is permitted to use, and a bond return on the rest.** A savings account whose custodian
decides what fraction of the deposit earns the high rate is a *good* account, not a great one —
and that is the honest reading of **[E4-20]** for a globally systemically important bank.

### Staying power — score all three **[E5-11]**, and the metric set is selected by business type first **[E5-37]**

- **(1) A LARGE AND RELIABLE STREAM OF EARNINGS — YES, and it is the strongest such stream this
  project has measured.** Net income above $37 billion in every one of the five years and above
  $48 billion in four of five; net interest income $95,443 million in 2025 on 2.5 million basis
  points of spread across $3,834,359 million of average interest-earning assets; **pre-provision
  profit $86,807 million in 2025** — that is the annual shock absorber, and it is 24.6% of common
  equity. Four segments, three of them earning 18% or better, in businesses whose fundamentals have
  not changed in decades. *The one qualification, already recorded: 2021's figure contains a
  $9.3 billion reserve release and 2024's a $7.9 billion Visa gain.*
- **(2) MASSIVE LIQUID ASSETS — YES, and the figures are the largest on this track by an order of
  magnitude.** At 2026-06-30: *"eligible end-of-period High Quality Liquid Assets ('HQLA') of
  approximately **$956 billion** and unencumbered marketable securities with a fair value of
  approximately **$541 billion**, resulting in approximately **$1.5 trillion of liquidity
  sources**."* Average HQLA for the quarter **$975,412 million** against average net cash outflows
  of **$885,521 million — a liquidity coverage ratio of 110%** for the Firm and **118%** for the
  Bank, both against a 100% minimum, with **net excess eligible HQLA of $89,891 million** at the
  Firm and **$164,579 million** at the Bank. **[E5-39]**: *"cash is a lot like oxygen"* — and
  **[E2-64]**, strength as an offensive asset, has a dated instance: *"The Firm had placed a $5
  billion deposit with First Republic Bank on March 16, 2023, as part of $30 billion of deposits
  provided by a consortium of large U.S. banks"*, and six weeks later bought the bank from the
  receiver.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — and this is where the score is a QUALIFIED YES
  rather than a yes, because the deposits ARE the near-term requirement and the number is worse than
  a bank that failed.** *"Ignoring that last necessity is what usually leads companies to experience
  unexpected problems."*
  - **Firmwide estimated uninsured deposits were $1,743.9 billion at 2026-06-30 on $2,713.7 billion
    of deposits — 64.3%**, up from $1,558.6 billion and 60.9% at 2025-12-31. **First Republic Bank
    failed with 67.7% of its deposits uninsured.** That comparison has to be made and it is made
    here rather than avoided.
  - **Four filed facts that make the same number mean something different, and they are the reason
    the score is a qualified yes rather than a fail.**
    (i) **The composition:** the filer states the uninsured deposits are *"primarily reflecting
    wholesale operating deposits"* — payroll, custody, clearing and cash-management balances that
    exist because the client's own operations run through them, which is the stickiest deposit
    there is and the reason the LCR rule treats them at a low outflow rate.
    (ii) **The coverage:** $1.5 trillion of liquidity sources against $1,743.9 billion of uninsured
    deposits is **87% coverage**, and the LCR of 110% is struck on a 30-day stress the regulator
    designs.
    (iii) **The 2023 evidence, which is the only real-world test available:** when three banks
    failed on exactly this exposure, **JPMorgan's domestic deposit share ROSE from 11.30% to 11.68%**
    on the FDIC's own numbers. **It was the destination of the run, not its victim.**
    (iv) **The measurement difference is disclosed rather than smoothed:** the FDIC Call Report puts
    JPMorgan Chase Bank, N.A.'s uninsured deposits at **49.4% of its deposits** at the same date,
    against the Firm's own 64.3% — the difference being non-U.S. deposits, which the Firm deems
    uninsured in full.
  - **Score: 3 of 3, with strength (3) carried as QUALIFIED and the qualification quantified.**
- **Leverage, named and quantified [E4-16, E3-29] — there is no ratio ceiling in this framework and
  the corpus supplies none.** Assets ÷ common equity **12.9 : 1** at 2025-12-31 and **14.2 : 1** at
  2026-06-30. Regulatory: **CET1 14.6% → 14.2%** against an **11.5% requirement**; Tier 1 15.5% →
  15.1%; total capital 17.4% → 17.0%; **Tier 1 leverage 6.9% → 6.6%**; supplementary leverage
  5.8% → 5.5%. **[E2-54]**'s coverage test — *"all interest, both payable and accrued, comfortably
  met out of current cash flow net of ample capital expenditures"* — passes without strain: total
  interest expense was $97,898 million in 2025 against $193,341 million of gross interest income and
  $86,807 million of pre-provision profit. **[E3-52]** is the right lens on the terms and it is
  favourable: $2.7 trillion of the funding is **deposits — covenant-free, largely
  customer-prepaid, and in the case of $970 billion of it, federally insured** — against
  $460,523 million of long-term debt.
- **Jurisdiction [E3-66]:** a Delaware financial holding company; shareholders stand where US law
  puts them, which the corpus calls *"especially favorable to shareholder interests."* No
  adjustment. *The one live jurisdiction exposure is named in Note 30 and quantified: Russian courts
  have entered judgment against the Firm including **one claim for $439 million**, and the total of
  the judgments **"exceeds the total amount of available assets that the Firm holds in Russia"** —
  the Firm states its remaining Russian exposure is *"not material."**

### Name the specific way THIS business dies **[E2-27, E3-24]** — modelled from EXPOSURE, not experience **[E4-40]**

> **[E4-40]** is the governing instruction: *"all of us in the industry made a fundamental
> underwriting mistake by focusing on **experience, rather than exposure**"* — a benign loss history
> late in a good cycle is *"not only useless, but actually dangerous."*

**FIRST, THE CORPUS'S OWN BANK ARITHMETIC, BECAUSE IT IS THE BENCHMARK THE FRAMEWORK SUPPLIES
[E3-24].** *"If 10% of all $48 billion of the bank's loans … produced losses averaging 30% of
principal, the company would roughly break even."*
- **On JPMorganChase at 2026-06-30: 10% of $1,542,462 million of loans losing 30% of principal is
  $46,274 million** — against **$86,807 million of FY2025 pre-provision profit** and an
  **allowance of $31,531 million**, i.e. **$118,338 million of absorption. It is covered nearly
  three times over, with $72,064 million to spare, and the equity is untouched.**
- **The corpus's test does not bite at this scale, so it is pushed until it does:**
  - to consume **one year's pre-provision profit** the whole loan book must lose **5.63%** of
    principal in one year — **7.6 times the worst net charge-off rate in the ten filed years read
    (0.74%, 2025)**;
  - to consume **pre-provision profit plus the entire allowance**, **7.67%**;
  - to erase **all of that plus the $301,305 million of tangible common equity**, **27.21% of the
    loan book.**
- **CONCLUSION: THIS BANK DOES NOT DIE OF LOANS, and saying so is the beginning of the answer, not
  the end of it.** The loan book is 30.8% of a $5.0 trillion balance sheet.

**SECOND, THE BANK'S OWN PUBLISHED REGULATORY STRESS RESULT, AND HOW MY SCENARIO DIFFERS — which
the brief requires and which is the right discipline.**
- **What the filings say, verbatim:** *"The Firm's current SCB requirement is **2.5%** and will
  remain in effect through September 30, 2027, based on the current rules. The Firm's Standardized
  CET1 capital ratio requirement, including regulatory buffers, was **11.5%** as of December 31,
  2025."* The Stress Capital Buffer is derived from the peak-to-trough CET1 decline in the Federal
  Reserve's own severely adverse supervisory scenario, **and it is FLOORED at 2.5%** — the filing
  states the floor: *"a variable SCB requirement, **floored at 2.5%**, for Standardized regulatory
  capital requirements."*
- **So the filed fact is this: on the Federal Reserve's own severely adverse scenario, run on the
  Federal Reserve's own models, JPMorganChase's modelled CET1 depletion is AT OR BELOW the 2.5%
  regulatory floor** — because a larger modelled decline would produce an SCB above 2.5%, and it
  does not. Against an actual CET1 ratio of **14.2%** and a requirement of **11.5%**, the
  supervisor's worst case **uses the buffer and does not breach the minimum.** The Firm also
  carries an 11.5% requirement that includes a **4.5% GSIB surcharge under Method 2**, the largest
  in the United States.
- **HOW MY SCENARIO DIFFERS, stated in three ways.** (1) **It is harsher on the loan book than the
  supervisor's, and that turns out not to matter** — see above. (2) **It attacks a different
  exposure: the part of the balance sheet the supervisor models and I cannot verify.** (3)
  **Most importantly, it asks a different question.** The supervisory scenario asks whether the
  Firm stays above its minimum. **The corpus asks what ends the OWNER's return, and those are not
  the same question** — which is exactly the finding the SOFI run of the same day recorded as
  #26 THE MARKED BOOK.
- *The numeric Dodd-Frank Act stress-test table lives in the Firm's own DFAST disclosure on its
  investor-relations site and in the Federal Reserve's DFAST publication. **Ladder rung: outside the
  six-rung evidence ladder. Named and not pulled.** The Federal Reserve's ENFORCEMENT register WAS
  pulled and did decide Q3, which shows the rung is reachable; the DFAST table is not
  decision-changing here because the filed SCB already bounds the supervisor's answer.*

**THIRD, THE MECHANISMS, QUANTIFIED FROM FILED FIGURES, WITH A STATED LIKELIHOOD EACH.**

**MECHANISM 1 — a severe credit cycle. A real possibility; a poor year, not an impairment.**
At a **3.0% net charge-off rate** on $1,542,462 million of loans — four times the worst filed year —
charge-offs are $46,274 million, the allowance absorbs $31,531 million and must then be rebuilt to
match a worse outlook, so the provision is roughly **$70 billion**. Against $86,807 million of
pre-provision profit **the Firm still earns money.** Exposure, from the Q2 2026 allowance
allocation: **credit card is 17% of retained loans and carries $15,561 million of the
$26,152 million loan allowance — 59.5% of the reserve against 17% of the book**, which is where a
consumer recession lands first; wholesale *"secured by real estate"* is 11% and commercial and
industrial 13%, with **criticized wholesale exposure of $50.3 billion, 3.3% of the wholesale
portfolio, of which $45.1 billion is still performing.**

**MECHANISM 2 — a funding run. A low-level possibility, and the 2023 record is the evidence.**
$1,743.9 billion of uninsured deposits against $1.5 trillion of liquidity sources, an LCR of 110%,
and the historical fact that in the one month this was tested JPMorgan's deposit share rose. **The
corpus's own scoping applies [E2-61]: *"you can be broke but flush"* is the insurer's trap; a bank's
trap is the reverse — flush and then suddenly not.** The exposure is real and the coverage is 87%.

**MECHANISM 3 — the trading and Level 3 book, AND THIS IS THE ONE NO DOCUMENT BOUNDS.**
$1,062,072 million of trading assets; **$33,732 million of Level 3 assets (9.5% of common equity)
and $76,139 million of Level 3 liabilities (21.5%)**; $67,767 million of derivative receivables
after netting, of which **$13,048 million is Level 3 before netting**; $9,156 million of mortgage
servicing rights, every dollar of it Level 3. **Risk Management VaR at 95% averaged $39 million a
day for CIB trading in the June 2026 quarter, with a maximum of $70 million. That is a measure of
the ordinary and it says nothing whatever about the tail** — and **[E4-40]** is explicit that
experience is the wrong input.
- **The filed precedent for what a control failure costs here is on this company's own record:**
  the 2013-09-18 Federal Reserve civil money penalty of **$200,000,000** and the 2013-01-14 Cease
  and Desist Order, arising from a loss in one portfolio in 2012. **A loss of that order is about
  1.8% of today's common equity — survivable and invisible in a year's results.**
- **The governing rule is [E5-32] and it is unusually apt: Salomon's books carried a daily invented
  number *"just put in there to make assets equal liabilities"*, signed by the largest audit firm in
  the country for twelve years. Audited does not mean true.** Two cross-checks were performed and
  both passed (equity recomputed from A − L; net income reconciled to the segment columns), and
  **neither of them can test a mark.**
- **And the Q3 cockroach finding is the live exposure here, not a historical one:** the March 2024
  consent orders found the Firm's *"processes to inventory trading venues and confirm the
  completeness of certain data fed to trade surveillance platforms"* deficient — i.e. **in 2024 the
  Firm could not be certain it was watching everything it traded on.** The Federal Reserve
  terminated its half in December 2025; the OCC order is still in force.
- **Likelihood of a $6 billion event: a real possibility, and the filed record contains one.
  Likelihood of a $60 billion event (17% of common equity): a low-level possibility. Likelihood of
  an event that impairs the firm: I cannot bound it from any document, and the honest statement is
  that this is the exposure a reader is asked to take on trust.**

**MECHANISM 4 — THE ONE THAT ACTUALLY ENDS THE OWNER'S RETURN, AND IT IS NOT INSOLVENCY.**

Putting the arithmetic together: to take CET1 from **14.2% to the 11.5% requirement** costs
**$53,506 million of after-tax capital, about $68 billion pre-tax**; to take it to the **7.0%** level
at which distributions stop entirely costs **$142,682 million after tax, about $181 billion
pre-tax** — more than two years of pre-provision profit. **JPMorganChase is very hard to kill and
the filings say so from every direction.**

**What is not hard is for the owner's return to stop compounding, and the mechanism is disclosed in
one sentence of the FY2025 10-K:** *"Any capital that the Firm has accumulated in excess of these
current requirements, **including the capital required to meet the potential increased requirements
of the U.S. Basel III proposal**, has been retained in Corporate in addition to its allocated
balance."*
- The operating businesses earn **18%, 32% and 40%** on the capital allocated to them. **Corporate
  holds $120.9 billion — 35.3% of the common equity — and earns about 3.7%.** The blended 17% ROE
  and 20% ROTCE are the average of a franchise and a Treasury bill.
- **The mix is not management's decision.** The 11.5% requirement is 4.5% minimum + 4.5% GSIB
  surcharge + 2.5% SCB, every term of it set by the Federal Reserve. The filer discloses the pending
  **U.S. Basel III proposal** which would *"replace the Advanced approach with an expanded
  risk-based approach"* and extend the SCB to both approaches — and states that at 2025-12-31
  *"the Advanced risk-based ratios became more binding on the Firm than the Standardized
  risk-based ratios."*
- **The arithmetic of the mechanism, from filed figures: each additional point of required CET1 on
  $1,981,692 million of risk-weighted assets moves $19,817 million of equity from the 18–40%
  businesses into the 3.7% one — about $2.9 billion a year of pre-tax income, 4.0% of 2025's
  pre-tax, per point.** A three-point increase, which is within the range the Basel III proposal was
  originally scoped at, costs roughly **$8.7 billion a year and about 1.7 points of ROTCE**, with no
  change whatever in the underlying business.
- **And it runs both ways, which is why this is a mechanism and not a bear case.** In February 2026
  the Federal Reserve froze SCB requirements *"at current levels through September 30, 2027"*, and
  **Corporate's allocated equity falls from $120.9 billion to $98.4 billion on 2026-01-01**, with
  $5.5 billion released to CCB and $17.0 billion to the CIB. **The single largest driver of this
  company's return on equity over the next five years is a regulatory decision, and the owner has no
  vote in it.**
- **Likelihood: [x] LIKELY** — not as a catastrophe but as the thing that happens. The requirement
  has moved in both directions in the last five years and will move again.

**[E4-51] — CAN I STATE THE ARGUMENT AGAINST MY OWN CONCLUSION BETTER THAN ITS HOLDERS?** The bull
case, stated as well as I can state it: *JPMorganChase earns 20.8% on tangible common equity on a
five-year mean, first of six in four of five years, minimum 18% — a record no other large American
bank has come close to. It carried the lowest held-to-maturity book relative to equity of any large
bank into 2023, which is why it bought a failed competitor instead of becoming one. It has reserved
31.7% more than it has lost over seven years. It has issued not one common share in five years while
retiring 12.8% of the count and compounding tangible book per share at 10.3% a year. It has no open
Federal Reserve order while two of its five peers do. Its operating cost advantage is 9.65 points
over the next-best universal bank and widening. Its overhead ratio has fallen from 59 to 52. Every
one of its three operating segments earns above 18% on allocated capital. And the $120.9 billion of
idle capital in Corporate is not a defect but an option: it is already being released, $22.5 billion
of it on 1 January 2026, and every dollar released moves from 3.7% to 18–40%. At 3.08 times tangible
book you are paying a fair price for the best-run large bank in the world with a regulatory tailwind
in front of it.* **I think that case is right about the business on every count and I have written
each of those facts into this file.** Where I part from it is at the last sentence: **a fair price
is not a discount**, and Q5 measures the price. And on the one point of substance where I part from
it on the business: **the release of Corporate's capital is a one-time event of about $60 billion,
not a growth engine — once the buffer is at the requirement there is no more to release, and what
remains is a company earning 17% blended on equity it is required to hold.**

**THE SURVIVAL SHAPE.** Checked against all of `Screens/SURVIVAL SHAPES - index.md` as it stood when
this file was written: **twenty-seven rows and a maximum number of 26** (the index's own numbering
note records that CCB and ACNB both took 25 and SOFI was numbered 26). **So this one is 27.**
Nearest existing, and why each is not it:
- **#14 THE PATRON** *(GFS)* — *"the government that funds the plant sets the terms and can change
  them."* **Inverted:** no government funds JPMorganChase; one **withholds permission to deploy its
  own capital.**
- **#17 THE PERMIT** *(ABNB)* — governments permit, cap or withdraw the **product**, market by
  market. Here the product is not at risk; **the capital is.**
- **#26 THE MARKED BOOK** *(SOFI)* — shares the distinguishing feature (*the company does not fail;
  the per-share compounding stops*) but not the mechanism: SoFi's is an unrealised fair-value
  write-up on retained loans, and JPMorganChase's earnings are collected in cash.
- **#10 THE CAMOUFLAGE** *(SONY)* — a strong leg's cash recycled into legs that must re-win a race.
  **Corporate is not a weak business burning the strong one's cash; it is the same capital, not
  deployed.**

**PROPOSED, #27 — THE LICENCE** *(pending the operator)*: **the business earns a very high return on
the capital it is permitted to use, and a regulator — not the owner and not the manager — decides
what fraction of the equity that is; the surplus is held at a bond return inside the same company,
so the reported return is a blend the owner cannot set, it is re-priced periodically by a supervisory
decision with no change whatever in the business, and the better the franchise the more the idle
capital costs. It does not kill the company; it caps the owner's compounding, and the cap moves.**
**Its tells, checkable on any filer:** a Corporate or Other segment holding a large share of equity
at a return the filer itself marks *"NM"*; a capital requirement printed in the filing beside a
higher actual ratio; a blended return on equity materially below **every** operating segment's; and
the filer's own sentence explaining that excess capital is *"retained in Corporate."*

- **VERDICT: [x] IN — GOOD, not great  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

*The three strengths score 3 of 3 with strength (3) qualified and the qualification quantified; the
loan book fails the corpus's own stress test by a factor of nearly three in the Firm's favour; the
named death is a regulatory re-pricing of the owner's return rather than an insolvency, and it is
likely rather than remote. **The one exposure no document bounds is the mark on $33,732 million of
Level 3 assets and $76,139 million of Level 3 liabilities inside a $1.06 trillion trading book, and
[E5-32] is the reason that is a permanent open item rather than a work order: there is no filing
that would close it.** That is priced once, at the end margin, and nowhere else **[E3-42]**.*

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Q1, Q2, Q3 and Q4 each show IN, so Q5 opens. This is the SECOND bank in this queue to reach Q5
and the largest company this project has ever priced.**

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*

**Honest pre-tax expectancy at this price: 7.5% at the bottom boundary, 11.1% at the top, centred
about 9.6%.**

Construction, so it can be checked:

| | pre-tax owner earnings, $M | **pre-tax yield on the $929,488M cap** | + sustainable growth in owner earnings per share | **= honest pre-tax expectancy** |
|---|---|---|---|---|
| **conservative** — five-year mean net income with the three distorted years removed **[E4-41]**, less (c) MID | **42,239** | **4.54%** | **3.0%** | **7.54%** |
| centre — FY2025 net income less (c) MID | 55,955 | 6.02% | 3.6% | **9.62%** |
| **optimistic** — FY2025 net income less (c) LOW | **62,869** | **6.76%** | **4.3%** | **11.06%** |

*Owner earnings are grossed up to pre-tax at the Firm's own 21.4% FY2025 effective book rate. The
growth term is built from the retention arithmetic rather than from a trend line: FY2025 paid out
$16,107 million of common dividends and $31,640 million of buybacks against $57,048 million of net
income — an 83.7% total payout — so the retained 16.3%, $9,301 million, compounds at the ~20% return
on tangible equity the business earns, which is **3.3 points of growth**; to that the optimistic end
adds about **1 point** for the release of Corporate's excess capital from a 3.7% return into the
18–40% businesses, which is already under way ($22.5 billion on 2026-01-01). The conservative end
takes 3.0% and no release credit.*

**BELOW ROUGHLY 10%, THE NAME IS NOT RANKED — IT IS QUIT ON, whatever the sovereign is [E4-28].**
**[E5-34]** settles which end governs: *"we will buy the stock (or business) if it sells at a
reasonable price in relation to **the bottom boundary of our estimate**."* **The bottom boundary is
7.54% and the centre is 9.62%. JPMorganChase is QUIT ON at the floor.**

**And the floor's own basis is respected [E4-28]:** the 10% is *"true whether short rates are 6
percent or whether short rates are 1 percent"*, because its basis is guessed future opportunity cost
rather than today's rate. **So the fact that 7.54% beats the 5.34% sovereign by 2.20 points does not
save it.** This is the configuration CLAUDE.md names in the Berkshire case, and the fifth name on
this track to land in it after KO, CB, GFF and ACNB: **above the bond, below the floor.**

**THE GROWTH BELIEF IS TESTED AGAINST THE CORPUS'S BASE RATE [E4-35] AND BOUNDED [E4-44, E2-63],
AND THIS IS WHERE THE PRICE CASE ACTUALLY BREAKS.**
- **[E4-35]** is **not** engaged: nothing here needs 15% growth and none is claimed. The case rests
  on 3.0% to 4.3%.
- **[E4-44]** IS engaged and it is decisive: *"the value of an asset, whatever its character, cannot
  over the long term grow faster than its earnings do"* and *"The Tinker Bell approach — clap if you
  believe — just won't cut it."* **The delivered record LOOKS like it supports a much higher growth
  rate than the case needs: diluted EPS compounded 6.85% a year from 2021 to 2025 and tangible book
  value per share 10.30% a year from 2020 to mid-2026. On those numbers the price clears the floor
  comfortably.** **It does not, and the reason is one number: net interest income went from
  $52,311 million in 2021 to $95,443 million in 2025 — plus 82.5% — while noninterest revenue rose
  25.5%.** Net interest income is **52.3% of 2025 revenue**, and its near-doubling is the federal
  funds rate going from nothing to about five per cent. **[E4-41]** is mandatory here: *the only
  pro-forma in the corpus that ever disclosed earnings too HIGH is Berkshire's own*, and favourable
  exogenous breaks are *named and removed before the mean is trusted.* **The break is named: the
  rate cycle. It is not a growth rate and it will not repeat from here, because it cannot happen
  twice from the same starting point.** **[E3-51]** is the right classification — *"when a surfer
  gets up and catches the wave and just stays there, he can go a long, long time. But if he gets off
  the wave, he becomes mired in shallows"* — and the wave in the 2021–2025 earnings record is the
  rate cycle, which every one of the six banks in Row A rode.
- **[E2-63] — state the ceiling, not just the yield.** The upside is bounded three ways and all three
  are filed: **(i)** deposit share is flat at 11.65% and the nationwide concentration limit means it
  cannot grow much by acquisition; **(ii)** the return on the equity the Firm may actually use is
  already 18% to 40%, near the top of what any large bank has ever sustained, and the filer's own
  proxy says ROTCE at or above 18% has been achieved **six times in ten years by JPMorganChase and
  eight times in total by its ten peers combined** — i.e. this is already the ceiling of the
  observable distribution; and **(iii)** the one genuine step-change available — releasing the
  $60,574 million of CET1 above requirement — **is a one-time event of finite size, not an engine**,
  and the Basel III proposal could take it back.

**One book. Owner earnings against the bond. A DCF may run as an engine; it casts no vote [E3-34].**
**No DCF was run.** The figures below are a yield, a multiple and a required-return capitalisation —
the corpus's own practice **[E3-24, E4-21]**.

**1. THE YIELD**
- owner earnings **$33,200M to $49,415M** ÷ market cap **$929,488M** = **3.57% to 5.32%** ·
  sovereign **5.34%**
- **pre-tax**, grossed up at the Firm's 21.4% rate: **4.54% to 6.76%**
- *(and for the reader who rejects the CONVENTION's (c) altogether: FY2025 net income of $57,048M is
  **6.14%** of the cap and FY2025 pre-tax income of $72,595M is **7.81%**. **Even on that reading —
  charging nothing at all for the capital the balance sheet must retain — the pre-tax yield is
  7.81% and still below the floor before any growth is added; with 3% growth it is 10.8% and
  clears.** That is the single most important sensitivity in this section and it is stated in full
  rather than buried: **a reader who does not accept this run's bank CONVENTION reaches a different
  Q5 verdict.** The CONVENTION is confessed as ours at Q3 under PRIME RULE 3, and this is exactly
  where it bites.)*

**2. WHAT THE PRICE ALREADY ASSUMES**
- **growth needed for a 10% pre-tax expectancy at $349.67: 5.46% a year FOR EVER at the conservative
  end, 3.98% at the centre, 3.24% at the optimistic end.**
- **what the business has actually done: diluted EPS +6.85% a year (2021–2025), tangible book value
  per share +10.30% a year (2020 to mid-2026), net income +8.75% a year from a 2021 base cleaned of
  its $9,256 million reserve release.** **On the raw record the price clears the floor at every end
  of the range.**
- **So the entire Q5 verdict rests on whether the 2021–2025 growth is repeatable, and the filings
  say it is not: 82.5% growth in net interest income off a zero policy rate is not a business
  result that can be extended, and it is 52.3% of the revenue.** That is a judgment, it is the
  judgment this section turns on, and it is written where a reader can refuse it.

**3. WHAT YOU ARE PAID**
- return at the current price = **plus 2.20 points over the sovereign** at the conservative end,
  **plus 4.28** at the centre, **plus 5.72** at the optimistic end.
- **The owner of JPMorganChase at $349.67 is paid, on the bottom boundary this run can honestly
  build, about two and a quarter points over a thirty-year Treasury to own 14.2 times leverage
  against the American economy, a $1.06 trillion trading book whose Level 3 marks no reader can
  test, and a return on equity whose mix is set by the Federal Reserve.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- sovereign used **5.34%** — **the bare rate, no per-name premium added.** *"It may look
  mathematical. But it's **mathematical gibberish** in my view."*
- **Certainty is handled TWICE and neither place is the rate [E3-42, E4-11, E4-48]:** at the
  understanding gate (Q1 passed on four legible mechanisms and explicitly carried the trading book
  forward to Q4 rather than into the rate), and in the discount to value demanded at the end. It is
  priced **once** and is not stacked. **[E3-60]** grades that margin by understanding, and this is
  **not** a creek-crossing: an unauditable $1.06 trillion trading book and 14.2 times leverage sit
  nearer the Grand Canyon end than the creek. **The margin is not the binding constraint here,
  because the floor already fails without one.**

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this method
cannot support:
- **conservative ≈ $200 a share** · **optimistic ≈ $340 a share** · **current price $349.67**
  *(construction: pre-tax owner earnings of $42,239M–$62,869M required to return the **[E4-28]**
  floor of 10% with no growth gives $422,392M–$628,690M of value, or **$159–$237 a share**;
  allowing 3% perpetual growth and therefore a 7% required return gives $603,417M–$898,128M, or
  **$227–$338 a share**. Rounded to $200 and $340. In tangible-book terms the range is **1.8× to
  3.0×** against today's **3.08×**.)*
- **THE CROSS-CHECK THAT THIS RUN DID NOT SET THE RANGE TO SUIT ITSELF, and it runs partly against
  me and is reported that way:** management bought its own stock at an average of **$142.42 in 2023**
  — inside the conservative half of this band — at **$205.46 in 2024**, at **$276.55 in 2025** and at
  **$317.28 in December 2025**, which is **inside the top quarter of my optimistic case and above
  its midpoint.** **So the Firm's own revealed valuation in late 2025 was broadly where my
  optimistic end is, and only today's $349.67 is above it.** That is a fair reading of the
  disagreement: the gap between this run and the board is **one year of multiple expansion**, not an
  order of magnitude, and it is the same gap that produced the capital-allocation flag at Q3.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- **floor verdict first: honest pre-tax expectancy 7.54% at the bottom boundary [E5-34], 9.62% at
  the centre, against ~10% [E4-28] — BELOW, so the name is QUIT ON and the ranking lines below are
  not filled in.**
- points over sovereign, this name: *(not filled in — the floor was not cleared)*
- against the rest of the opportunity set: *(not filled in — the floor was not cleared)*
- *Take the best available, or nothing.* **[E2-74]**'s parking place is the answer for the money —
  *"our major parking place for money is medium-term tax-exempt bonds"* — liquid and waiting,
  because *"Mr. Market will offer us opportunities."* **The box exists so cash pressure never bends
  the standard, and a shortfall of 2.5 points at the bottom boundary is precisely the size of gap
  that cash pressure bends.** **[E4-45]** makes the same point from the other side: *"8 1/2 wouldn't
  tempt you"* — a small margin is not a margin.

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — **not used.** No end margin is applied, because the floor failed
  before a margin was reached and applying one would be windage on a number that is already out.
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      **No. $349.67 is 75% above the conservative case of ~$200 and 2.8% above the top of the
      optimistic case of ~$340.** Three outcomes: below the conservative case → act · inside the
      range → no useful conclusion, move on · **above the whole range → no.** **This is the third
      outcome, narrowly.** No margin is added on top; *"startlingly low"* is what you observe, and
      **[E3-65]** is the calibration that settles it: the Washington Post was bought at *"about 20
      percent of the value to a private owner."* **JPMorganChase is available at 103% to 175% of this
      run's own value range.**
- **WINDAGE COUNT: ONE.** Applied once, at Q4, in taking the **[E4-41]**-adjusted five-year mean net
  income at the **(c) MID** end as the bottom boundary of earning power — one act of conservatism on
  one number, earning power. **No margin is added at Q5, no premium is added to the rate, and no
  haircut is taken to the growth rate.** **[E4-48]** satisfied: realistic inputs, errors on the
  conservative side, conservatism spent once.
- **[E3-17]'s long-horizon qualifier, recorded because it is the best argument for the other
  verdict:** *"If the business earns 6 percent on capital over 40 years … you're not going to make
  much different than a 6 percent return, even if you originally buy it at a huge discount"* — and
  the inverse is that **a business earning 20.8% on tangible capital delivers most of that to a
  patient owner over decades almost regardless of a 40% entry premium.** JPMorganChase is the
  strongest instance of that inverse this project has measured. **The entry discount dominates short
  horizons and business quality dominates long ones; both tests bind and neither excuses the other.
  This run applies the entry test because Q5 is the entry question and the floor is the entry
  standard.**

- **VERDICT: [ ] IN — [x] OUT ON PRICE. Quit on at the ~10% floor [E4-28]. Ranking position: not
  ranked.**

*This is a failure on the PRICE, not on the business. All four business gates cleared. The QLYS
ruling of 2026-09-07 is the precedent for which way that cuts: a Q2 failure is a failure on the
business and a price alert would be a category error, but **a Q5 failure is exactly the case where a
price band IS the right artifact** — and it is armed at the fold.*

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]** — *"I believe in establishing yardsticks prior to the act."*
Nothing is held, so **[E2-28]**'s sell rule has nothing to act on; what follows is the entry
yardstick and the monitoring set, written now so it cannot be fitted to a later quote.

**THESIS-CONFIRMING METRICS (would confirm the Q5 OUT — i.e. that the price was the problem and the
business was not):**
1. **Overhead ratio staying at or below 52% while Bank of America's, Citigroup's and Wells Fargo's
   stay above 61%.** This is the measured franchise and it is the one thing that must hold.
2. **Return on tangible common equity at or above 18% in every year.** The floor of the five-year
   record, and the level the filer's own proxy says ten peers have reached eight times combined in a
   decade.
3. **Zero net common shares issued.** Five years running; the cleanest single signal in the file.
4. **No open Federal Reserve enforcement order** — checkable quarterly, for free, at
   `federalreserve.gov/supervisionreg/files/enforcementactions.csv`.

**THESIS-BREAKING METRICS AND THEIR THRESHOLDS (would force the business verdicts to be revisited):**
1. **Q2, the cost advantage — the only thing the franchise rests on.** **Threshold: the overhead
   ratio above 56% for two consecutive years, or the gap to Bank of America's efficiency ratio
   narrowing below 5 points.** Bank of America closed to within 0.6 points at the *bank* level in
   2025 (52.27% against 52.37% on the FDIC Call Report) while remaining 9.65 points behind at the
   holding company — **that convergence is the single metric to watch and it has already begun on
   one of the two measures.**
2. **Q2, the funding franchise — already narrowing.** **Threshold: the noninterest-bearing share of
   average deposits below 22%** (it has gone 29.1% → 24.1% in three years), **or the cost of total
   deposits above Citigroup's.**
3. **Q3, the cockroach.** **Threshold: a THIRD enforcement action in the market-conduct or
   trade-surveillance class, or any new Federal Reserve order that is not terminated within two
   years.** The 2020 DPA and the 2024 consent orders are two in the same class four years apart;
   a third would change the Q3 verdict from IN to OUT, because **[E5-22]**'s *"they didn't act when
   they learned"* would then be answered the other way.
4. **Q3, the reserve.** **Threshold: the allowance covering the following year's net charge-offs
   below 2.0× (the seven-year minimum is 2.72×), or a year in which the provision is below
   charge-offs while the loan book grows.** The [E2-67] back-test in this file is the instrument and
   it must be re-run each year, because **JPMorganChase does not publish it.**
5. **Q4, the named death.** **Threshold: the Standardized CET1 requirement rising above 13%**, which
   on 2025 risk-weighted assets moves a further $29.7 billion of equity from the 18–40% businesses
   into the 3.7% one, about $4.4 billion a year of pre-tax income. **This is the metric with no
   company-specific driver at all — it is a Federal Reserve decision — which is why it is the
   proposed shape.**
6. **Q4, the exposure no document bounds.** **Threshold: any single trading or valuation loss above
   $10 billion, or Level 3 assets above 15% of common equity** (9.5% at 2026-06-30).

**NEXT CATALYST DATES, from the filing pattern:**
- **Q3 2026 10-Q, early November 2026** (2025-11-04 in the prior year) — the first statement after
  the seasonal balance-sheet peak, and the first read on whether the H1 asset growth persists.
- **FY2026 10-K, mid-February 2027** (2026-02-13 this year) — the annual outlook against outturn
  **[E3-48]**, the full-year reserve back-test, and the first year of the three-segment reporting
  with two full comparatives.
- **2026 CCAR submission was filed 2026-04-06**; the Firm's final SCB requirement *"will become
  effective on October 1, 2026"* — but the Federal Reserve announced in February 2026 that
  **SCB requirements "will remain at current levels through September 30, 2027"**, so the live date
  for Mechanism 4 is **the 2027 test on revised models**, which the filing flags explicitly.
- **The Apple Card portfolio closes approximately December 2027** — $110 billion of Advanced
  risk-weighted assets and a $2.2 billion provision already taken.

**[E4-17]/[E3-30] MONITORING QUESTION — aberrational cycle or permanent slippage?** *"is this
erosion just part of an aberrational cycle … or has the business slipped in a way that permanently
reduces intrinsic business values?"* **On today's evidence: aberrational on the funding side and not
slippage.** The noninterest-bearing deposit share fell at every large bank as rates rose, and
JPMorgan's fell less than Bank of America's (14.1 points) and Wells Fargo's (10.1 points) — it fell
6.0. **What would make it slippage is the third bullet above: the overhead gap closing.** The
franchise is a cost advantage; if the cost advantage goes, there is nothing else.

**THE SELL RULE [E2-28], recorded for the counterfactual, because nothing is held:**
- SELL if the market judges it more valuable than the facts indicate — **that is the present state
  of affairs and it is why nothing is bought.**
- SELL if funds are needed for something more undervalued or better understood — not applicable.
- HOLD while: return on equity capital satisfactory (20.8% five-year mean ROTCE — yes) · management
  competent and honest (no disqualifier found, with a live capital-allocation flag) · market does not
  overvalue (**it does, on this run's range**).
- *Price appreciation and holding period are explicitly rejected as reasons to sell.*

**Do not trim winners [E5-14]. POSITION SIZE: ZERO** — not a judgment about sizing; the business
cleared and the price did not. **And the sizing judgment is recorded in advance for the case where a
band is hit: sized DOWN, because the CAPITAL-ALLOCATION FLAG at Q3 is live, and [E4-13] says the
flag binds position size and never the discount rate.** **[E3-45]**'s direction governs the rest:
capital goes to rank #1, and this name is not ranked.

**TWO PRICE BANDS ARE ARMED AT THE FOLD, because a Q5 failure is a price failure (the QLYS ruling,
2026-09-07, read the ACNB way):**
- **$230** — where the **bottom boundary** of the owner-earnings range returns the ~10% floor with
  3% growth, i.e. $227 rounded. **2.03× the 2026-06-30 tangible book value per share of $113.35.**
- **$190** — a deeper band at **1.68× tangible book**, below anything the Firm itself has paid for
  its own stock since 2023.
- ***Both bands must be re-struck annually, and the reason is stated so a future session does not
  read a stale number: tangible book value per share is compounding at about 10% a year
  ($66.11 at 2020-12-31 to $113.35 at 2026-06-30), so a fixed dollar band tightens in real terms
  every quarter. At the 2027 mid-year tangible book these bands correspond to roughly 1.8× and 1.5×.***

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** *(the falsifiers are pre-committed,
  each is a filed series or a free public register, and the thresholds are numeric)*

---
## WHAT THE FOURTH BANK ADDS TO THE FRAMEWORK'S BANK PROBLEM

*The CCB run of 2026-09-19 left four structural gaps for the operator. Three of them now have more
evidence and one of them is CLOSED. None is fixed here: PRIME RULE 5 requires a written case and the
operator's approval for a structural change, and PRIME RULE 6 requires the ledger row before the
rule.*

1. **GAP 1 — CAN ANY BANK PASS Q2? The four banks now run have SHARPENED this question rather than
   settled it, and the sharpening is a real result.** **[E3-43]** classes a bank as *"a business,
   unlike a franchise"*, which read literally makes Q2 OUT automatic. **The record of four runs is
   that no bank has been closed on that ground, and two of the four have passed Q2 on filed facts by
   two DIFFERENT routes:**
   - **CCB — Q2 OUT**, on the counterparties' own 10-Ks: the customers dual-source by design.
   - **SOFI — Q2 OUT**, on the largest technology client replacing Galileo with its own ledger.
   - **ACNB — Q2 IN**, on **[E2-58]**'s wide-and-sustainable cost advantage measured on the
     **COST OF FUNDS** (a low deposit beta: 64 basis points below the median of its own 56-bank
     market over five years).
   - **JPM — Q2 IN**, on **[E2-58]**'s same exception measured on the **COST OF OPERATIONS** (a
     9.65-point overhead advantage over the next-best universal bank, widening) — **and JPMorgan
     FAILS ACNB's test, being third of six on the cost of deposits in every one of five years.**
   **So the finding after four banks is this: [E3-03] criterion 2 is passable for a bank, it is
   passable ONLY through [E2-58]'s single exception, and the exception has at least two independent
   forms — the price of the liability and the cost of the platform. Neither is "no close substitute"
   in the ordinary sense, and a bank that has neither is OUT.** That is a usable rule and it is
   offered to the operator as one. **What it does NOT settle is whether [E2-58]'s exception is the
   right doorway at all**, or whether **[E3-29]**'s buying of a bank at 20:1 leverage means the
   corpus intended an explicit exception class in which Q2 returns NARROW by construction and the
   decision moves wholly to Q3 and Q5. **The four runs are consistent with either reading.**
2. **GAP 2 — THE EVIDENCE LADDER STOPS TOO SOON FOR A REGULATED FILER. THIS IS NOW CLOSED, AND IT
   COST ONE HTTP REQUEST.** CCB named two missing rungs: the FFIEC/FDIC Call Report and the bank
   supervisors' enforcement registers. **Both have now been used and both decided a gate.** ACNB
   used the FDIC Call Report to close its moat class over 56 institutions; this run used it over
   **4,411 institutions at six dates** for the deposit-share and conformity tests, and used **the
   Federal Reserve's own enforcement-actions file (2,889 actions) to decide Q3** — the gate the
   Citigroup precedent says decides a bank. **RECOMMENDATION, for the operator: add one rung to the
   evidence ladder between "SEC EDGAR primary documents" and "company IR site" — *the prudential
   regulator's own published data for the sector*, with the two instruments named
   (`api.fdic.gov/banks/financials` for the Call Report, and
   `federalreserve.gov/supervisionreg/files/enforcementactions.csv` for conduct).** It is not a new
   threshold and it adds no step; it removes friction from one, which is the test CLAUDE.md sets for
   tooling. **The rung that is still genuinely absent is the OCC's enforcement register** (an
   `apps.occ.gov` endpoint returned 404 to two attempts this session) and the **NCUA Form 5300**
   data for credit unions, which ACNB also named.
3. **GAP 3 — OWNER EARNINGS NEEDS A DECLARED FORM FOR BALANCE-SHEET BUSINESSES. The CONVENTION has
   now been tested on four banks spanning a factor of 1,300 in size and it has NOT broken, and this
   run adds a second modification to it.** Its record: a **$111.6 million shortfall** at Coastal
   Financial ($0.7bn cap), a **$143.8 million surplus** at ACNB ($0.66bn cap), and a **$172.5
   billion surplus** at JPMorganChase ($929bn cap) — the same construction, three opposite
   magnitudes, none of them tuned. **Its two modifications, both forced by filings rather than
   chosen:** ACNB's **CNR split** of Δassets into organic and acquired; and this run's **dual base**
   — total assets at the Tier 1 leverage ratio **and** risk-weighted assets at the CET1 requirement,
   because for a bank with a $1.06 trillion trading book total assets are a seasonal number and not
   unit volume. **They agreed to within 12% in 2025, which is the evidence that either base is
   usable.** **It is ours, it is confessed as ours in every run that uses it, and after four banks it
   should either be adopted with a ledger row or refused.** Its strongest corpus anchor remains
   **[E2-60]**'s third dimension of maintenance, *"its financial strength."*
   *And this run records the one place the CONVENTION changes a verdict, which is what a confessed
   convention is for: **without it, JPMorganChase's pre-tax yield is 7.81% and with 3% growth it
   clears the ~10% floor. With it, the bottom boundary is 7.54% and it does not.** The CONVENTION
   is the difference between a pass and a fail on this name, and that is stated at Q5 rather than
   hidden.*
4. **GAP 4 — MAY "COMPUTATION — NOT A CLEARANCE" CARRY A PRICE VERDICT?** Not engaged here: all four
   business gates cleared, so Q5 opened properly and the price verdict is a real verdict, not a
   below-gate computation. **The question stands for the next bank that closes early.**
5. **A FIFTH, NEW WITH THIS RUN, AND IT IS A TOOLING MATTER THE OPERATOR SHOULD KNOW ABOUT.**
   `tools/sources.py:_get()` still defaults to `WEB_UA` and `www.sec.gov/Archives` answers that with
   HTTP 403 — **the third confirmation in one day** (BLK, ACNB, JPM). It is a one-line fix
   (`headers=SEC_UA` as the default for any `sec.gov` host) and every run is paying for it. **And a
   second: `tools/sources.py` has no helper for the FDIC or Federal Reserve endpoints this run and
   the ACNB run both had to hand-roll.** Two functions — `call_report(cert, dates)` and
   `enforcement_actions(name)` — would get the same numbers sooner without adding a step, which is
   the test CLAUDE.md sets.

---
## SUMMARY — the verdict line

| | |
|---|---|
| **Q1 understand** | **IN** — four businesses on one balance sheet; the trading book is not auditable and is carried to Q4 rather than into the rate |
| **Q2 franchise** | **IN — class NARROW, direction MIXED.** [E2-58]'s single exception, met on the **cost of operations** and NOT on the cost of funds |
| **Q3 honest and rational** | **IN at GATE weight.** No disqualifier found; **a live CAPITAL-ALLOCATION FLAG**, the cockroach rule fired twice in one failure class, and no reserving back-test published |
| **Q4 survive** | **IN — GOOD, not great [E4-20, E4-43].** Named death: **#27 THE LICENCE**, proposed |
| **Q5 price** | **OUT ON PRICE — quit on at the ~10% floor [E4-28].** Honest pre-tax expectancy 7.54% at the bottom boundary, 9.62% centred, against a 5.34% sovereign |
| **Q6 falsifiers** | **IN** — pre-committed, numeric; **two price bands armed, $230 and $190** |

**Price US$349.67** (2026-09-18 close, `tools/sources.py price()`, **aggregator FLAGGED**,
corroborated against the Q2 10-Q's own filed market capitalisation) **× 2,658,186,195 shares**
(cover of the 10-Q for the quarter ended 2026-06-30, accession `0001628280-26-054343`; issued
4,104,933,895 less treasury 1,446,747,700 reconciles to the share, and the issued figure would have
overstated the cap **1.544-fold**) **= market capitalisation US$929,488 million.** **Sovereign
5.34%**, USD, **US Treasury daily par yield curve, 30-year, 09/18/2026**, struck fresh this session
from the issuing authority, **not FRED**.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 IN → Q3 IN → Q4 IN → **Q5 OUT
      ON PRICE** → Q6 IN. Q5 opened properly because all four business gates showed IN, so no
      `COMPUTATION — NOT A CLEARANCE` heading is required and none is used.
- [x] **No question marked IN carries an "unverified", "general knowledge" or "provisional" caveat.**
      Q2 carries a **class and a direction**, both of which are findings; Q3 was tested at gate weight
      and the decisive artifact was **obtained** rather than assumed; Q4's unbounded item is named as
      a permanent open item under **[E5-32]** rather than as a provisional pass.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** None was written. **Three
      named work orders are recorded inside passing gates and none is decision-changing:**
      (i) the **text** of the March 2024 OCC consent order — OCC enforcement register, an
      `apps.occ.gov` endpoint that returned HTTP 404 to two attempts this session; (ii) the
      **NCUA Form 5300** data for credit unions as non-bank deposit substitutes; (iii) the numeric
      **Dodd-Frank stress-test table**, which the filed 2.5% SCB already bounds.
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known** — none was written. The
      one thing that cannot be known is stated at Q4 as an exposure rather than as a verdict: **no
      filing bounds the tail on $33,732 million of Level 3 assets and $76,139 million of Level 3
      liabilities inside a $1.06 trillion trading book, and [E5-32] says no filing would.**
- [x] **Step 0: the filing was read, with accession numbers, and TWO figures were cross-checked.**
      Five 10-Ks (FY2021 `0000019617-22-000272`, FY2022 `0000019617-23-000231`, FY2023
      `0000019617-24-000225`, FY2024 `0000019617-25-000270`, FY2025 `0001628280-26-008131`), the Q2
      2026 10-Q `0001628280-26-054343`, the 2026 proxy `0000019617-26-000096`, and the Q2 2026 8-K
      earnings release `0001628280-26-048078`; plus **ten peer filings** (BAC FY2025
      `0000070858-26-000157`, FY2023 `0000070858-24-000122`, FY2022 `0000070858-23-000092`; C FY2025
      `0000831001-26-000011`, FY2022 `0000831001-23-000037`; WFC FY2025 `0000072971-26-000133`,
      FY2022 `0000072971-23-000071`; GS FY2025 `0000886982-26-000091`, FY2022 `0000886982-23-000003`;
      MS FY2025 `0000895421-26-000086`, FY2022 `0000895421-23-000284`). **Cross-check 1, the [E5-32]
      one:** $5,015,069M − $4,640,471M = $374,598M, identical to filed total stockholders' equity,
      and less $21,040M of preferred gives $353,558M, which ÷ 2,658.186M shares = $133.01, identical
      to the filer's own book value per share. **Cross-check 2:** FY2025 net income reconciled to the
      sum of the four segment columns, $18,245 + $27,761 + $6,522 + $4,520 = $57,048M.
- [x] **Owner earnings on a multi-year mean; window stated; (c) band disclosed as a judgment.** Six
      windows published, four used; (c) band LOW/MID/HIGH with the reason for sitting at MID stated;
      the D&A default **[E3-44, E2-41]** and the **[E5-20]** exception class both declared
      inapplicable **with reasons** rather than forced; the half-year explicitly **not annualised**.
      **The ordinary construction was refused with three reasons and the CONVENTION was declared and
      labelled at Q3 STEP 3 (PRIME RULE 3), with its two modifications and the one place it changes
      the verdict.**
- [x] **Competitor row filled.** **Row A: five named holding companies over five years from their own
      10-Ks. Row B: every FDIC-insured institution in the United States at six dates — 4,313 to
      4,904 filers — from the issuing authority.** Peers named: 5 of 5 where five is the whole
      category, then the whole industry. **[E3-28]** wants eight; the category has five. The moat is
      **NARROW, not PROVISIONAL**, and the one unavailable class (non-bank deposit substitutes) is
      named with its artifact and the **direction** of the missing evidence stated.
- [x] **Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 09/18/2026, struck fresh.** The multi-currency point raised by the AIG replication of the
      same day is recorded at Step 0: 40% of employees are outside the U.S. and the principal non-US
      subsidiaries are UK- and German-domiciled, but the **reporting** currency is USD and no FX leg
      enters the quote. *This run does NOT resolve the general multi-currency question and does not
      claim to.*
- [x] **Value stated as a round-number range, not a point estimate:** conservative ≈ $200,
      optimistic ≈ $340, price $349.67. Cross-checked against management's own repurchase prices,
      **including the one that runs against this run's range** ($317.28 in December 2025).
- [x] **One bar chosen, not both; windage count stated.** Screamer test **[E4-01]** only; windage
      count **ONE**, applied at Q4 on earning power.
- [x] **Prices dated; aggregator used for live quotes only and flagged**, and corroborated against a
      primary document (the filed period-end market capitalisation of $870,104M at 2026-06-30).
- [x] **`python tools/check_framework.py` PASSES** — run before each commit, not after.
- [x] **Run committed to git with a pathspec, per the six-step fold**, in five commits (Q1, Q2, Q3,
      Q4, Q5/Q6+audit).
- [x] **ONE ERROR OF MY OWN FOUND AND CORRECTED IN AN ADDENDUM RATHER THAN BY EDITING HISTORY
      (operator rule 6).** Q1 states *"Level 3 assets of $76,139M are 21.5% of common equity."*
      **$76,139M is the Level 3 LIABILITIES figure; Level 3 ASSETS are $33,732M, 9.5% of common
      equity.** The Q1 sentence is left visible, the correction is at the head of Q4, and the
      corrected figures are the ones used in every subsequent calculation.
- [x] **THE ANALYST IS A SUBJECT OF THE PSYCHOLOGY (operator rule 9, [E4-27], [E4-26], [E3-41]).**
      Two specific places where this run hunted disconfirming evidence hardest against its own
      developing view, recorded so the check is auditable rather than asserted:
      (i) **at Q2**, the run's first instinct was that the largest bank in America must have the
      cheapest deposits, and the uniform five-year row built to confirm it **refuted it** — JPMorgan
      is third of six, every year — and the refutation is printed as the most important fact in Q2
      rather than footnoted; (ii) **at Q3**, the precedent on disk (Citigroup 2007) pointed to OUT,
      and rather than reasoning around a $879 million penalty record the run went and got the
      supervisor's own register, which could have confirmed the OUT and instead showed zero open
      orders. **And the place where the incentive ran the other way is named too: a name that
      clears all four business gates is a more interesting run than one that closes at Q2, and Q5's
      verdict turns on a single judgment — that 82.5% growth in net interest income off a zero
      policy rate is not repeatable — which is stated at Q5 in the open, where a reader can refuse
      it, precisely because it is the judgment that produces the tidier answer.**

## REGISTER
- Verdict: [ ] IN  [ ] OUT (about the business)  [ ] UNRESEARCHED  [ ] UNKNOWABLE ·
  **[x] FAIL AT Q5 ON PRICE** — all four business gates IN.
- **One line: JPM (JPMorgan Chase & Co.), 2026-09-19 — ALL FOUR BUSINESS GATES IN; FAIL at Q5 on
  PRICE, quit on at the ~10% [E4-28] floor with an honest pre-tax expectancy of 7.54% at the bottom
  boundary and 9.62% centred, above the 5.34% sovereign by 2.2 to 4.3 points on every construction.
  The FOURTH bank this project has run and the SECOND to clear the business gates. Q2 passes on
  [E2-58]'s single exception measured on the COST OF OPERATIONS — a 9.65-point overhead advantage
  over the next-best universal bank, widening, worth about $17.6bn a year pre-tax — and explicitly
  FAILS the test ACNB passed on, being THIRD of six on the cost of total deposits in every one of
  five years (5-yr means WFC 0.927%, BAC 1.066%, JPM 1.202%). Five-year mean ROTCE 20.80%, first of
  six in four of five years. Q3 IN at GATE weight, decided by the Federal Reserve's own
  enforcement register (2,889 actions, pulled from the issuing authority): thirteen entity actions
  since 2003, ZERO orders open, $878.9M of civil money penalties — the largest of the six — and the
  2024-03-08 order terminated 2025-12-04, while Citigroup and Wells Fargo each still have an open
  order. [E3-02] conformity tested at 2022-12-31 from the FDIC Call Reports: HTM securities at 1.40x
  equity, the LOWEST of seven institutions against Silicon Valley Bank's 5.91x and Bank of America's
  2.81x. Reserving record 31.7% more provisioned than charged off over seven years, with no
  published back-test ([E2-67] met in substance, not in form). Zero net common shares issued in five
  years. LIVE CAPITAL-ALLOCATION FLAG: $31.6bn of buybacks in 2025 at 2.57x tangible book against
  $9.9bn at 1.65x in 2023. Named death #27 THE LICENCE (proposed): $120.9bn — 35.3% of common
  equity — earns about 3.7% in Corporate as the regulatory buffer while the three operating segments
  earn 18%, 32% and 40%, and the mix is a Federal Reserve decision. Price US$349.67 (2026-09-18,
  aggregator, flagged), 2,658,186,195 shares from the Q2 2026 10-Q cover of 2026-06-30 (accession
  `0001628280-26-054343`), cap US$929,488M, sovereign 5.34% (US Treasury 30-year, 09/18/2026).
  Value range ~$200 to ~$340 a share against a $349.67 quote; 3.08x tangible book. Bands $230 and
  $190, to be re-struck annually because tangible book compounds at about 10% a year.**
- **If UNRESEARCHED — THE WORK ORDER:** not the governing verdict. Three named work orders sit
  inside passing gates and none is decision-changing: the **text of the March 2024 OCC consent
  order** (OCC enforcement register; an `apps.occ.gov` endpoint returned HTTP 404 twice this
  session — **the one rung still genuinely missing**); the **NCUA Form 5300** data for credit
  unions; and the numeric **DFAST table** (bounded already by the filed 2.5% SCB).
- **If UNKNOWABLE:** not applicable as a verdict. The one permanently unknowable item is recorded at
  Q4: **no filing bounds the tail on $33,732M of Level 3 assets and $76,139M of Level 3 liabilities
  in a $1.06 trillion trading book, and [E5-32] is the reason no filing would.**
- **THE STRONGEST SINGLE FACT AGAINST THIS CONCLUSION, stated because [E4-51] requires it and
  because it nearly reverses the verdict:** **on the record the business has actually delivered, the
  price clears the floor.** Diluted earnings per share compounded **6.85% a year** from 2021 to 2025
  and tangible book value per share **10.30% a year** from 2020 to mid-2026, against the **3.24% to
  5.46%** of perpetual growth the quote requires for a 10% pre-tax expectancy. **The entire Q5
  failure rests on one judgment — that the 82.5% rise in net interest income from $52,311 million
  (2021) to $95,443 million (2025), on 52.3% of the revenue, was the federal funds rate and not the
  business, and cannot happen again from here.** If that judgment is wrong, JPMorganChase clears the
  floor at $349.67 and this file's verdict is wrong with it. **A second fact in the same direction:
  the Firm's own board bought 8.9 million shares at $317.28 in December 2025, inside the top quarter
  of this run's optimistic case — the disagreement between this run and the people who know the
  business best is one year of multiple expansion, not an order of magnitude.**
