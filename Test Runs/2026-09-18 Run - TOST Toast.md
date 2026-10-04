# Company Run — Toast, Inc. (TOST) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stopped at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Asked aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

---
## STEP 0 — THE RATE, THE PRICE, AND THE FILING

### The sovereign — for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **2026-09-17** · **US Treasury daily par yield curve, 30 Yr, from the issuing
  authority** (`home.treasury.gov`, `daily_treasury_yield_curve`, 2026 CSV; the newest row on
  the file at the time of this run is `09/17/2026,...,5.32,5.29`). **FRED DGS30 was not used;
  it is only the fallback.**
- Struck by this run, not inherited from the brief. The rate moved inside two days (09-16
  reads 5.35, 09-17 reads 5.29), which is why the protocol requires each run to strike it.
- **FX / ADR ratio: not applicable.** Toast earns in USD. The FY2025 10-K segment note:
  *"We did not earn material revenue in any country other than the United States during the
  fiscal years ended December 31, 2025, 2024, and 2023."* Item 7A: *"Most of our sales and
  operating expenses are denominated in U.S. dollars."*

### The price — struck by this run, aggregator flagged (operator rule 5)
- **$30.65, the close of 2026-09-17** — the last COMPLETED close. Source: Yahoo Finance
  daily chart series (aggregator, permitted for live quotes only, **flagged**).
- **`tools/sources.price()` was NOT used for the struck price, and the reason is a tooling
  defect recorded at the end of this file.** It returned `(30.275, '2026-09-18', 'USD')` at
  14:17 UTC today with the market open: that is `regularMarketPrice`, an INTRADAY quote,
  stamped with the date of the last trade. Its docstring says *"Latest close."* A run that
  wrote "$30.28 (2026-09-18 close)" would state a falsehood.
- Five prior closes, for the range: 09-11 $32.12 · 09-14 $33.29 · 09-15 $31.84 ·
  09-16 $31.12 · 09-17 $30.65.
- **The aggregator series was cross-checked against a primary filing**, the CL run's method:
  the Form 4 of **2026-09-04**, accession **0001650164-26-000187**, reports open-market sales
  on **2026-09-02** at **$33.542** and **$34.095**. Yahoo's 2026-09-02 bar is low $32.65 /
  high $34.28 / close $34.04. Both filed prices sit inside the filed day's range. The
  aggregator series is corroborated by a primary document.

### The share count — from the cover, with the accession
- **514 million Class A + 64 million Class B = 578 million**, as of **2026-07-30**, from the
  cover of the Q2 2026 10-Q, accession **0001650164-26-000164**, filed 2026-08-05:
  *"The registrant had outstanding 514 million shares of Class A common stock and 64 million
  shares of Class B common stock as of July 30, 2026."*
- **The ERIC trap (issued vs outstanding) was checked on the document: the cover says
  "had outstanding", not "issued".** The 2026-06-30 balance sheet says *"issued and
  outstanding"* for both classes and gives 512 + 65 = 577 million, one month earlier —
  consistent with the cover, not in conflict with it.
- **The SPGI trap (a cover that excludes shares it calls outstanding) was checked: there is
  no exclusion clause on this cover.**
- **Two classes, and they are economically identical.** FY2025 10-K Note 8: *"Each share of
  Class A common stock entitles the holder to one vote per share and each share of Class B
  common stock entitles the holder to ten votes per share on all matters submitted to a vote
  of stockholders. Holders of Class A common stock and Class B common stock are entitled to
  receive dividends, when and if declared by our Board of Directors… Each share of Class B
  common stock is convertible into one share of Class A common stock voluntarily at any time
  by the holder, and will convert automatically into one share of Class A common stock upon
  the earlier of (a) the date the holders of two-thirds of our outstanding Class B common
  stock elect to convert… or (b) September 24, 2028."* Votes differ ten to one; the
  economics do not, and the whole Class B converts by September 2028. **They are summed.**
- **A SOURCE LIMIT, stated rather than hidden.** Toast tags its entire XBRL instance at
  `decimals="-6"`. No exact share count and no exact dollar figure exists anywhere in the
  filing. **The cap cannot be struck to better than about ±0.1%**, and every figure in this
  run carries the filer's own million-dollar rounding.
- `sources.shares_outstanding()` returns **None** for this filer: there is no undimensioned
  `dei` count, because the count is dimensioned by share class. That is why the cover is read.

### The market cap
- $30.65 × 578 million = **$17.7 billion**. Split factor after 2026-07-30 = **1.0** (no split
  in the window); `close` used, never `adjclose`.

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, period ended 2025-12-31, filed **2026-02-18**, accession
  **0001650164-26-000057**, primary document `tost-20251231.htm`. Auditor **Ernst & Young LLP**
  (*"We have served as the Company's auditor since 2019"*), unqualified on the statements and
  unqualified on internal control over financial reporting.
- **Q2 2026 Form 10-Q**, period ended 2026-06-30, filed **2026-08-05**, accession
  **0001650164-26-000164**.
- Also read: 8-K EX-99.1 earnings releases of **2026-08-04** (acc. 0001650164-26-000162),
  **2026-05-07** (0001650164-26-000113) and **2026-02-12** (0001650164-26-000050); the
  **DEF 14A of 2026-04-23** (0001650164-26-000098); and the Form 4 of 2026-09-04.
- **Figures cross-checked against the filed statement** (four, not one): FY2025 operating
  cash flow **$661M**, capital expenditures **$(53)M**, stock-based compensation **$242M**
  and total revenue **$6,153M**, all read off the face of the FY2025 consolidated statements,
  all four matching the XBRL series used at Q4.
- **LIVE-DEAL CHECK, re-queried at the time of this run** (not inherited from the brief):
  EDGAR submissions for CIK 0001650164 fetched live on 2026-09-18 show the newest filing as a
  **Form 4 of 2026-09-04**; the newest periodic filing is the Q2 2026 10-Q of 2026-08-05 and
  the newest 8-K is 2026-08-04. `sources.deal_filings("0001650164")` returns empty lists.
  **No merger, tender or exchange form is live.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language

Toast sells a restaurant a cash register and then takes a cut of everything that goes through
it. That is the whole of it, and the second half is where the money is.

Three lines, FY2025 (10-K Item 7 and the statements of operations):

| line | revenue | cost of revenue | gross profit | margin |
|---|---|---|---|---|
| Subscription services | $936M | $264M | **$672M** | 71.8% |
| Financial technology solutions | $5,037M | $3,891M | **$1,146M** | 22.8% |
| Hardware and professional services | $180M | $400M | **−$220M** | **−122%** |
| Amortization of acquired intangibles | — | $5M | −$5M | |
| **Total** | **$6,153M** | **$4,560M** | **$1,593M** | **25.9%** |

Read as three separate businesses and the model is plain:

1. **The hardware and the onboarding are sold at a deliberate loss.** Toast spent $400M to
   deliver $180M of terminals and installation in FY2025 — a **$220M a year subsidy** paid to
   put its own hardware on a restaurant's counter. The 10-K says so in its own way: *"We also
   offer a number of ways for customers to reduce the upfront cost of our products. With an
   Easy Pay commercial lease, Toast customers can get up and running quickly while minimizing
   their upfront costs, such as hardware and onboarding fees, by making lease payments
   generally through a portion of their daily transactions."* This is customer acquisition
   that happens to run through cost of revenue.
2. **The subscription is the software rent.** $936M at 72% gross margin across ~164,000 live
   locations — roughly $6,300 of software revenue per average location per year, rising about
   9-10% a year, because Toast sells more modules into the same restaurant (payroll,
   marketing, inventory, xtraCHEF, Toast Capital) over time.
3. **The payment take is the engine.** 82% of reported revenue is financial technology
   solutions, reported **gross**: Toast collects the whole merchant discount rate and pays
   interchange, network assessments and processing fees out of it, which is why the margin
   looks thin. The 10-K states the choice and the reason: *"The transaction fees collected are
   recognized as revenue on a gross basis as we are the principal in the delivery of the
   managed payments solutions to the customers."* What Toast keeps is the $1,146M of fintech
   gross profit, which on $195.1 billion of gross payment volume is a **net take rate of
   0.587%** — 59 basis points of everything a Toast restaurant sells.

**So reported revenue is the wrong number at this company and gross profit is the right one.**
$6.15bn of "revenue" is mostly other people's interchange passing through. This is a
$1.6bn gross-profit business that grew that number 33% in FY2025.

**And the net take rate is rising, not falling:** 0.552% (FY2024) → 0.587% (FY2025) → 0.599%
(H1 2026), computed as fintech gross profit ÷ GPV from the filed revenue, cost and GPV lines.
Recorded here as arithmetic about the model; it is not yet a moat claim, which is relative.

### The scarce input this business controls
**The point-of-sale terminal in the restaurant, and therefore the payment flow attached to
it.** Not the software, which is copyable; not the payment rail, which is a commodity. What is
scarce is the *position*: once Toast's Android terminals, kitchen display, handhelds and
payroll records are the restaurant's operating record, the processor is chosen by whoever owns
that record, and Toast owns it. Toast pays $220M a year of hardware subsidy and a large
field sales force to buy that position once, and then earns 59 basis points on every dollar
the restaurant rings up without buying the position again.

Named precisely because the framework asks for it: the scarce input is **not a physical
asset**. Net property and equipment is $105M, and $202M of the $256M gross is capitalised
software. The plant is trivial. What is on the balance sheet is not what makes the money —
which is the fact that sets up the (c) judgment at Q4.

### Two perimeter questions, settled on the document rather than assumed
- **Merchant float is NOT inside operating cash, unlike ABNB.** Customer money is carried
  outside the operating line: *"Cash held on behalf of customers 159 123 87"* and *"Restricted
  cash 71 59 55"* are reconciled separately from *"Cash and cash equivalents 1,353 903 605"*,
  and *"Change in customer funds obligations, net 36 36 27"* sits in **FINANCING**. The
  offsetting *"Customer funds obligation"* of $159M sits inside accrued expenses. **The ABNB
  adjustment is therefore not owed here.** Interest income of $51M is earned on Toast's own
  $1,991M of cash and marketable securities, which Item 7A identifies by name, and it is
  outside owner earnings anyway because the construction starts from operating cash.
- **Toast Capital: Toast DOES bear credit risk on the loans, and the brief's prior was
  wrong.** Settled on Note 2 and Note 4; see Q4 and DEFECTS FOUND. Recorded here because it
  is part of how the money is made: fintech revenue includes loan marketing and servicing
  fees, and the guarantee loss is a real cost of that revenue.

### Will the fundamentals look broadly the same in ten years?
**Broadly yes, at the level Q1 asks about.** Restaurants will still need a till, the till will
still be the natural place to take the payment, and whoever owns the till will still collect a
percentage. The mechanism is stable and statable in four sentences without one word of Toast's
language. Whether Toast in particular keeps 59 basis points of the volume is a **relative**
question, is a claim about competitors, and belongs at Q2.

**The honest limit, stated rather than smoothed:** the filed record is seven years long, the
company earned its first operating profit in FY2024, and the company's own self-description
changed inside eighteen months — *"the all-in-one digital technology platform built for
hospitality"* (press release, 2026-02-12) became *"the global technology platform built for
restaurants and retail businesses"* (2026-05-07 and 2026-08-04). That is a prompt to read, not
a Q1 failure: the mechanism did not change, the addressable-market claim did.

- **VERDICT: [x] IN**
  *The unit economics are writable without management's language, the scarce input is
  nameable, and the mechanism is stable **[E3-31]**. The durability of Toast's SHARE of it is
  a relative claim and is not settled here.*

---
## DATED NOTE, 2026-09-18 ~13:30 EDT: STEP 0 AND Q1 VERIFIED BY THE RESUMING SESSION, AND THREE CORRECTIONS
*The first session was killed by a session limit at about 10:30 EDT after committing Step 0 and
Q1 (`4af8db5`, `ccacfcc`). This session re-checked both rather than inheriting them. Nothing above
is edited (operator rule 6); what follows corrects it.*

**Re-struck and CONFIRMED:**
- **Sovereign 5.29%, 09/17/2026**, re-fetched at 13:10 EDT directly from the US Treasury daily par
  yield curve 2026 CSV (`09/17/2026,3.97,...,5.32,5.29`). 09/17 is still the newest row, so the
  figure stands.
- **Price $30.65, the 2026-09-17 close**, re-fetched from the Yahoo daily chart (aggregator,
  flagged). At 13:09 EDT on 2026-09-18 `regularMarketPrice` read **30.135** with the market open,
  so 09-17 is still the last completed close and the intraday defect recorded above reproduces.
- **The Form 4 cross-check reproduces**: accession `0001650164-26-000187` (reporting person
  Jonathan Vassil) reports sales on 2026-09-02 at **$33.542** and **$34.095**; the Yahoo bar for
  2026-09-02 is low $32.65, high $34.285. Both prices sit inside the range.
- **Share count 578 million** (514 Class A + 64 Class B), 10-Q cover, accession
  `0001650164-26-000164`. Confirmed on the document.
- **EDGAR re-queried at 13:10 EDT**: the newest filing for CIK 0001650164 is still the **Form 4 of
  2026-09-04**; between 2026-08-05 and today there are only Forms 4 and 144. No 8-K, no deal form.
- **Cash and marketable securities $1,991M** (Item 7A: *"We had cash and cash equivalents of $1,353
  million and marketable securities of $638 million as of December 31, 2025"*) and interest income
  $51M: confirmed.
- **The Q1 gross-profit table, the 33% gross-profit growth (1,190 to 1,593 = +33.9%) and the
  take rates** (fintech gross profit / GPV: 686/126.1 = 0.544% FY2023, 878/159.1 = 0.552% FY2024,
  1,146/195.1 = 0.587% FY2025, 671/112.0 = 0.599% H1 2026): all reproduce from the filed lines.

**CORRECTION 1 (Q1, the self-description).** Q1 says the self-description *"changed inside eighteen
months"* and quotes February and May 2026. **The quoted pair is less than three months apart, and
there were two changes, not one.** Every EX-99.1 release from 2025-02-19 to 2025-11-04 reads *"the
all-in-one digital technology platform built for restaurants"*; the 2026-02-12 release reads
*"built for **hospitality**"*; the 2026-05-07 and 2026-08-04 releases read *"the global technology
platform built for restaurants and retail businesses"*. **Two rewrites of the addressable-market
claim inside six months.** Q1's verdict does not depend on it (the mechanism did not change), but
the error ran in the flattering direction and is carried to Q3 as a prompt under [E2-49].

**CORRECTION 2 (Q1, the float).** Q1 calls *"Cash held on behalf of customers"* and *"Restricted
cash"* **customer money** and **merchant float**. The notes say otherwise:
- *"Cash held on behalf of customers represents an asset that is restricted for the purpose of
  satisfying obligations to remit funds to various tax authorities to satisfy customers' **payroll,
  tax** and other obligations."* It is **payroll float**, not card-settlement float.
- *"Restricted cash represents cash held with commercial lending institutions. The restrictions are
  related to cash held as **collateral** pursuant to an agreement with the originating third-party
  bank for the working capital loans serviced by Toast Capital."* It is **Toast's own money posted
  as collateral for the loan guarantee**, not customer money at all.
- Card-settlement money does not appear on the balance sheet as a float asset; what does appear is
  *"Accrued transaction-based costs $368"* (FY2025), a liability to the networks and processors,
  and its movement **is inside operating cash**.
Q1's conclusion survives (the ABNB adjustment is not owed, because neither pool runs through
operating cash as a customer prepayment), but the reason given was wrong on both lines.

**CORRECTION 3 (Q1, Toast Capital).** Q1 says Toast *"DOES bear credit risk on the loans"* and
refers forward to Q4. The direction is right and the scope was missing. From FY2025 Note 2:
*"we are obligated to purchase certain loans originated by our industrial banking partner in cases
where the customer's payments on the loan are missing or delayed for a defined period of time ...
**Our obligation is limited to a specified percentage of the total loans originated, measured on a
quarterly basis.**"* It is a **capped first-loss guarantee**, not full credit risk. **And the
perimeter moved in 2026, which neither Q1 nor the brief knew:** Q2 2026 10-Q Note 4, *"The Company
purchases loans from its bank partner that are not delinquent at acquisition and for which the
Company has the intent and ability to hold for the foreseeable future ... As of June 30, 2026, loans
held for investment, net, were $ 46 million ... compared to $ 0 million ... as of December 31,
2025."* Toast began carrying performing loans on its own balance sheet in H1 2026. Taken up at Q4.

**The Step 0 claim that four figures "all match the XBRL series used at Q4"** was written before
Q4 existed. It is re-checked at Q4 below rather than accepted.

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHAT IS BEING TESTED
Q1 named the scarce input as **the position**: the terminal on the counter and the operating
record behind it, from which Toast takes 59 basis points of everything the restaurant sells. The
franchise claim is therefore a claim that restaurants regard Toast as having **no close
substitute** once installed, and that Toast can price accordingly. [E3-03] states how the claim
shows itself: *"The existence of all three conditions will be demonstrated by a company's ability
to regularly price its product or service aggressively and thereby to earn high rates of return on
capital."* (1991 letter.) That sentence is the test, and it is tested below on Toast's own filings
first, then against the row.

### THE THREE CONDITIONS **[E3-03]**

**(1) Needed or desired: IN.** A restaurant must take card payments and record orders. About
164,000 locations, GPV $195.1bn in FY2025 (+23%), and the take on it rising.

**(3) Not subject to price regulation: IN, with one note.** No regime sets Toast's processing or
subscription fees. The regulated element (interchange, and the Durbin cap on debit) sits in
Toast's cost of revenue and is passed through, because revenue is booked gross and the networks'
fees are cost. [E2-59] is not engaged on the fee Toast keeps.

**(2) No close substitute: NOT SHOWN, and Toast's own filings say the opposite in four places.**

1. **The company's own pricing sentence.** FY2025 10-K, Item 1A (accession
   `0001650164-26-000057`, filed 2026-02-18): *"many of our competitors are well capitalized and
   offer discounted products and services, lower customer processing rates and fees, customer
   discounts and promotions, innovative platforms and offerings, and alternative pay models, any of
   which may be more attractive than those that we offer. Such competitive pressures may lead us to
   maintain or lower our processing rates and fees or maintain or increase our incentives,
   discounts, and promotions in order to remain competitive, particularly in markets where we do not
   have a leading position. **Such efforts have negatively affected, and may continue to negatively
   affect, our financial performance**"*. The last sentence is in the past tense: the concessions
   have already been made. This is the criterion-(2) sentence on the company's own filing, and it
   runs against the claim.
2. **The one broad price test on the record failed, and the company said so in writing.** Form 8-K
   of 2023-07-19, Item 7.01, EX-99.1, a letter to customers signed by the then CEO: *"we have made
   the decision to remove the $0.99 order processing fee from the new version of our digital
   ordering suite by the end of this week."* ... *"We made the wrong decision"*, and in the same
   letter: *"for the last 12 years there have been **no broad-based price increases**, despite
   significant investment in our platform."* That is **[E4-37]**'s measure read at the bad end:
   *"it's not a great business when you have to have a **prayer session** before you raise your
   prices a penny ... you can almost measure the strength of a business over time by **the agony
   they go through** in determining whether a price increase can be sustained"* (2005 meeting).
   Ninety-nine cents on a digital order was withdrawn within weeks, publicly, with an apology, and
   the letter records twelve years without a broad increase. The FY2024 and FY2025 10-Ks carry the
   lesson forward as a risk factor: *"Changes to our pricing and packaging model may also lead to
   reputational damage, competitive harm, regulatory scrutiny, and potential legal liabilities"*.
3. **The position is bought, and the price of buying it is set by rivals who do the same.** Toast
   delivered $180M of hardware and installation for $400M of cost in FY2025 (a hardware and
   professional-services gross margin of **-102.8% / -84.6% / -122.2%** in FY2023-25), and
   capitalised **$147M** of sales commissions against $99M amortised. Lightspeed's FY2026 MD&A
   (fiscal year ended 2026-03-31, filed with its 40-F) describes the same weapon in the same market:
   *"we continue to support our customers with **free hardware and implementation and competitive
   rates**. As a result of this initiative, we generally require our eligible new and existing
   customers to adopt our payments solutions."* A subsidy every competitor offers is the entry fee
   to a contested market, not evidence of an uncontested one.
4. **The company's own share estimate.** FY2025 10-K Item 1: *"we estimate that U.S. restaurant
   locations on our platform account for approximately **20%** of the U.S. restaurant market."* Four
   in five US restaurants run something else. [E2-53]'s dominance class (*"Once dominant ... Good or
   bad, it will prosper"*) is not available at a fifth of the market, and **[E5-28]** says a claim of
   pricing power is a claim of *"a monopoly or a near monopoly"*.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*

Restaurant point-of-sale-plus-payments has an unusual number of filed participants. Taken:
**Block/Square, NCR Voyix (Aloha), PAR Technology, Shift4 (SkyTab), Lightspeed**, with **Fiserv
(Clover), Global Payments (Genius/Heartland), Oracle (Simphony/MICROS)** and **Olo** examined and
recorded as not separable or no longer filing. **NCR Voyix was not in the brief's list** and is the
one filer with a pure restaurant segment; it was fetched for this run (10-K FY2025, accession
`0000070866-26-000006`, filed 2026-02-26; it names *"Toast, Inc."* among its key competitors).

**ROW A: GROWTH OF THE RESTAURANT/POS BUSINESS, FY2023 to FY2025, each from the filer's own
statements** (gross profit where the filer reports it for the relevant business, revenue where it
does not; the basis differs and is stated per row):

| company | measure | FY2023 | FY2024 | FY2025 | growth 23→24 / 24→25 | source |
|---|---|---:|---:|---:|---|---|
| **Toast** (subject) | gross profit, $M | 834 | 1,190 | 1,593 | **+42.7% / +33.9%** | 10-K FY2024 and FY2025, statements of operations |
| Block, Square segment | segment gross profit, $M | 3,128.7 | 3,598.9 | 3,935.0 | +15.0% / +9.3% | XYZ 10-K FY2025, segment note |
| NCR Voyix, Restaurants segment | segment revenue, $M | 886 | 825 | 818 | **-6.9% / -0.8%** | VYX 10-K FY2025, MD&A segment table |
| PAR Technology | subscription service revenue, $M | 122.6 | 207.4 | 291.2 | +69.2% / +40.4% (**acquired**: TASK 2024, Delaget 2025) | PAR 10-K FY2025 |
| Shift4 | gross revenue less network fees, $M (the filer's non-GAAP) | 940.4 | 1,354.4 | 1,981 | +44.0% / +46.3% (**acquired**) | FOUR 10-K FY2024 and FY2025, KPI tables |
| Lightspeed | gross profit, $M, fiscal years to March | | 450.2 (FY25) | 526.9 (FY26) | +17.0% | LSPD MD&A FY2026 |

**ROW B: THE TAKE, gross profit per dollar of payment volume** (same metric, same window, where the
filer reports both halves):

| company | FY2023 | FY2024 | FY2025 | construction |
|---|---:|---:|---:|---|
| **Toast, total gross profit / GPV** | **0.661%** | **0.748%** | **0.817%** | 834/126.1, 1,190/159.1, 1,593/195.1 |
| Toast, fintech gross profit / GPV | 0.544% | 0.552% | 0.587% | the Q1 table |
| Block, Square segment GP / Block GPV | 1.374% | 1.494% | 1.516% | 3,128.7/227,699; 3,598.9/240,812; 3,935.0/259,631 |
| Shift4, GRLNF / end-to-end volume | 0.862% | 0.822% | 0.948% | 940.4/109.0; 1,354.4/164.8; 1,981/209. **Before** other costs of sales, so it overstates against a gross-profit basis |
| Lightspeed, GP / GTV | | 0.493% (FY25) | 0.537% (FY26) | GTV includes volume Lightspeed does not process; a bound, not a comparator |

**ROW C: THE SOFTWARE ALONE, and THE HARDWARE** (the lines PAR and Toast both report):

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| **Toast, subscription services gross margin** | 66.8% | 69.0% | 71.8% (H1 2026: 77.8%) |
| PAR, subscription service gross margin | 48.0% | 53.5% | 54.7% |
| **Toast, hardware and professional services** | -102.8% | -84.6% | -122.2% |
| PAR, hardware | +22.3% | +24.3% | +22.9% |

**Not separable, and why, each tested on the document:**
- **Fiserv / Clover.** Neither the FY2025 10-K nor the Q2 2026 10-Q nor either furnished earnings
  release this run fetched (EX-99.1 of 2026-02-10, `0000798354-26-000006`, and of 2026-08-06,
  `0000798354-26-000028`) carries a Clover revenue, GPV or margin figure; the word appears in the
  boilerplate and in the Clover Capital cash-advance lines only. **Fiserv's investor slides are the
  next rung (company IR site) and were not pulled**, so the Clover cell is **UNRESEARCHED**, and its
  cost to the verdict is stated below.
- **Global Payments** names Toast as a direct competitor (*"Fiserv, Inc. ("Fiserv"), Chase
  Paymentech Solutions, LLC, Elavon, Inc., a subsidiary of U.S. Bancorp, Bank of America Merchant
  Services, Wells Fargo Merchant Services, Toast, Inc., Stripe, Inc. ("Stripe"), Shopify Inc. and
  Block Inc. ("Block")"*, GPN 10-K FY2025) but does not segment its POS software. **Oracle** reports
  no hospitality segment. Both are recorded as not separable.
- **Olo is no longer a filer.** Its submissions show a **Form 15-12G on 2025-09-23**, after the
  merger became effective on 2025-09-16. The brief listed it as a filing rival; it has not filed a
  periodic report since its Q2 2025 10-Q.
- **Private participants (SpotOn, TouchBistro, Revel, Qu and others).** The brief asked whether a
  filing every participant must make resolves the row, as Form NRSRO did at SPGI. **Tested, and it
  does not, with the reason for each route:** (a) **state money-transmitter licensing** does not
  capture card volume at this company: Toast's own 10-K says *"TPS is licensed as a money
  transmitter in most states in connection with certain payroll processing services we provide"*,
  while card processing runs under *"registered as a payment facilitator or certified service
  provider with the Payment Networks"*, a network registration with no public call report;
  (b) the **card networks' registries** of payment facilitators list names, not volumes (reasoned
  from what a registry is; **not fetched**, and stated as such); (c) the **Nilson Report** is a paid
  trade publication, not a filing, and sits off the evidence ladder. **No universal filing was
  found; recorded as "tested, does not resolve".** EDGAR full-text search returns filings naming
  SpotOn and TouchBistro (49 and 30 hits), which is a count of mentions, not a row.

**Peers named: nine examined, five carried with numbers, four recorded as unavailable**, of an
industry whose competitors the 10-K says *"vary in size and in the breadth and scope of the
products and services they offer"*. Buffett says eight; I examined nine and could number five.

### WHAT THE ROW SHOWS, AND WHAT IT DOES NOT
- **Toast is taking share, fast, from the legacy incumbent and from at least one cloud rival.** Its
  gross profit grew 34-43% a year while the one pure restaurant segment on file (NCR Voyix
  Restaurants, the Aloha business) **shrank** and **re-priced for margin** (Adjusted EBITDA margin
  22.2%, 30.4%, 32.6% on falling revenue: a harvest). **Lightspeed left the US restaurant market**:
  LSPD FY2026 MD&A, *"On April 28, 2026, we sold all of the issued and outstanding capital stock of
  Provide Holdings Inc., which includes our Upserve U.S. hospitality product line, to an affiliate of
  Skyview Equity ("Skyview") for $44.0 million in cash and up to $37.0 million in contingent
  consideration."* That is **[E2-45]**'s attacker's test answered by an actual attacker, and it cuts
  **for** Toast: a funded rival tried and sold out for at most $81M.
- **But the row does not show Toast charging more than its rivals.** Square earns **1.52%** of
  gross profit per dollar of volume to Toast's **0.82%**, and Square's take also rose over the same
  three years (1.37% to 1.52%). The rising take is **industry-wide in this window**, so it is not
  Toast-specific evidence of pricing power; and the 10-K attributes fintech growth to *"the increase
  in Locations on the Toast platform"*, not to price. Mix (Toast Capital fees, larger customers,
  module adoption) cannot be separated from rate on anything filed. Block's own 10-K says its Square
  GPV growth was *"driven primarily by strength in Food and Beverage sellers"*: the largest rival is
  growing in Toast's market at the same time.
- **Toast's growth is itself evidence of substitutability.** Every location Toast wins from Aloha,
  MICROS or Upserve is a restaurant that regarded one system as a substitute for another and
  switched. The filings show switching at scale in Toast's favour; **Toast discloses no churn or
  retention rate** (the word appears only in the definition of a live location and in the
  deferred-commission policy), so whether switching away from Toast is rare cannot be shown from any
  document I can name.

### THE OTHER Q2 TESTS
- **[E4-04]: rapid and continuous change is engaged in the company's own words.** *"The markets in
  which we compete are characterized by constant change and innovation, and we expect them to
  continue to evolve rapidly"* and *"The overall market for restaurant management software is
  rapidly evolving and subject to changing technology, shifting customer and guest needs, and
  frequent introductions of new applications"* (FY2025 10-K, Item 1A). [E4-04], 2007 letter: *"Our
  criterion of "enduring" causes us to rule out companies in industries prone to rapid and
  continuous change ... A moat that must be continuously rebuilt will eventually be no moat at
  all."* v4's scope test (does the spending defend the same advantage or buy its replacement?) is
  answered partly each way. The $220M hardware subsidy and $147M of commissions buy **new**
  positions, which is growth. The $374M of R&D and $54M of capitalised software on a **3-year**
  amortisation life buy the product that keeps the installed position from being switched at
  contract end (contracts run 12 to 36 months), which is replacement on a three-year clock.
  **[E5-23]** licenses defending a moat all of the time; it does not turn a product that must be
  rebuilt every three years to win a 12-36 month renewal into an enduring moat.
- **[E4-36] which cause of extreme success? Wave-riding.** The wave is the migration of US
  restaurants from on-premise legacy POS to cloud systems with integrated payments, and the row
  shows it: the legacy segment shrinking, the cloud entrants growing. **[E3-51]**: *"when a surfer
  gets up and catches the wave and just stays there, he can go a long, long time. But if he gets off
  the wave, he becomes mired in shallows."* **A surfing run is not a moat; the advantage lives in the
  wave, not the surfer.** Toast is the best surfer on the filed record. That is a finding about
  execution, not about a franchise.
- **[E2-44] two-characteristic test.** (1) *"an ability to increase prices rather easily (even when
  product demand is flat and capacity is not fully utilized) without fear of significant loss of
  either market share or unit volume"*: **FAILS on the record**; the only broad attempt on file was
  withdrawn in weeks. (2) *"an ability to accommodate large dollar volume increases in business ...
  with only minor additional investment of capital"*: **passes on plant** (net property and
  equipment $105M against $1.6bn of gross profit) and **fails on customer-acquisition capital** the
  balance sheet does not call capital: about $220M a year of hardware loss and $147M a year of
  capitalised commissions to add locations.
- **[E3-33] untapped pricing power: REFUSED** under [E5-28] at a 20% share, and the 2023 letter is
  direct evidence that management went looking for it and did not find it.
- **[E4-32] direction: widening SHARE, not a widening moat.** The share gains against a harvesting
  incumbent and a retreating cloud rival are real and are recorded. [E4-32] asks about the moat's
  width, and a share gain in a market where customers are visibly switching is the wave, not the
  moat.
- **[E4-23] key-person: no defect found.** The CEO changed (Comparato signed the 2023 letter; the
  2026 proxy's CEO is Aman Narang) and location growth continued through the handover.
- **[E3-46] the return on capital.** Operating income was **-$287M, +$16M, +$292M** in FY2023-25.
  The business has earned an operating profit for two years; a high return on a small tangible base
  in FY2025 is recorded, and two years is not a record [E2-42].
- **[E3-61] the row's limit, stated.** The row shows position and trajectory; it cannot show how
  Square, Clover and the private entrants will price the next five years.

### WHAT THE FRANCHISE CASE RESTS ON, AT FULL STRENGTH **[E4-26, E4-51]**
The best case for IN, stated so that its holders would accept it: switching a restaurant's POS is
painful (hardware, menus, staff training, payroll records, integrations), contracts run 12-36
months, the software margin is 17 points above the only software peer on file and rising, the net
take has risen every year, the legacy incumbent is shrinking and a funded cloud rival sold its US
restaurant business for at most $81M. **Each fact is true and each is recorded.** What defeats it
is that criterion (2) is a statement about what customers **think**, and the only direct evidence
of that on the record is the customers' reaction to a 99-cent fee and the company's own sentence
that it has had to lower rates and raise incentives to keep them. **Switching costs that have to be
defended with lower rates and free hardware are a moat the rivals are crossing.**

**What the UNRESEARCHED Clover cell costs the verdict: nothing that could reverse it.** Clover's
numbers could show Clover growing faster or slower than Toast; neither would supply the evidence
criterion (2) lacks, which is Toast's own ability to raise its price.

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** (not shown; contradicted on the filer's
  own words) · not price-regulated **[x]**
- **Class: NONE.** A fast-growing share position on a technology wave, bought with a hardware
  subsidy the competitors also offer, in a market the filer calls rapidly evolving and intensely
  competitive. **Direction: share widening; moat not shown to exist.**
- **The gate does not close on missing evidence.** Clover is UNRESEARCHED and churn is unpublished,
  and neither is what fails the gate: it fails on documents in hand, the 10-K's concession sentence
  and the 2023 8-K.

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
*OUT on the business: [E3-03] criterion (2) is contradicted on the company's own filings (past rate
concessions to competitors; the withdrawn fee and twelve years without a broad increase, [E4-37]);
[E4-04]'s rapid-change exclusion is engaged in the company's own words; the record is a surfing run
[E3-51, E4-36], not a franchise. Not a finding that Toast is a poor business: it may be the best-run
business in its market. **The file closes here.** Q3-Q6 below are RECORDED, NOT GOVERNING, as at
NVDA and the other Q2 closes in wave 5.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the
> queue asks every run for a price and because the evidence was gathered; it decides nothing and
> cannot reopen Q2 [E2-37, E3-39].

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution** **[E3-38]**: ticked. Q2 found a product rebuilt on a three-year clock to
  win 12-36 month renewals, in a market the filer calls intensely competitive, with the position
  bought daily by a field sales force and a hardware subsidy. That is have-to-be-smart-every-day.
- [ ] **Control** **[E1-16]**: not ticked; a minority public holding. **But note the structure**:
  Class B carries ten votes a share until the sunset of **September 24, 2028** (FY2025 10-K Note 8),
  so an outside holder cannot influence the board before then.
- [ ] **Leverage** **[E3-29]**: not ticked. No borrowings (*"there were no borrowings outstanding on
  the 2021 Facility"*); the Toast Capital guarantee is capped at *"a specified percentage of the
  total loans originated, measured on a quarterly basis"*.

**Case declared: a BINARY GATE, on daily execution.** Had the file been open, a weak manager would
not be survivable here and no price would compensate.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became public
- **Litigation and regulatory**: FY2025 10-K Item 3, *"We are not currently a party to any
  litigation or claims that, if determined adversely to us, would have a material adverse effect"*;
  Note 15 records no accrual for material claims. No restatement, no material weakness; Ernst & Young
  unqualified on the statements and on internal control (auditor since 2019).
- **The 2023-07-19 letter is a candor event, not a misconduct event**: management reversed a fee in
  writing and said *"We made the wrong decision."* [E2-26] counts that on the positive side.
- **No disqualifier found.** Per [E5-17] this is the absence of found disqualifiers, not a finding
  that the managers are honest.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **EBITDA / adjusted-earnings promotion [E4-29]: FIRES AT FULL STRENGTH, in four places, and
  the fourth is the one that matters.** (a) Headline: the Q2 2026 release (8-K of 2026-08-04, acc.
  `0001650164-26-000162`) opens *"Net income was $154 million and Adjusted EBITDA was $221 million in
  second quarter"*, and every release from 2025-02-19 to 2026-08-04 carries Adjusted EBITDA in its
  headline bullets. (b) The CEO's own quote, 2025-11-04: *"ARR grew 30% to over $2.0 billion,
  Adjusted EBITDA was $176 million"*. (c) **Guidance is given in it**: FY2026 *"Adjusted EBITDA in
  the range of $805 million to $825 million"*. (d) **Pay is funded on it**: DEF 14A of 2026-04-23
  (acc. `0001650164-26-000098`), the short-term bonus is *"Funded based on Recurring Gross Profit
  (RGP) and Adjusted EBITDA performance"*. Adjusted EBITDA is *"net income (loss), adjusted to
  exclude stock-based compensation expense and related payroll tax expense, depreciation and
  amortization expense"*: FY2025 **$633M against GAAP operating income of $292M**, a gap made
  mostly of $242M of stock compensation. [E4-29]: *"Doing so implies that depreciation is not truly
  an expense ... That's nonsense."* Here the larger deletion is stock pay, which **[E5-06]** calls an
  expense without qualification.
- [x] **The second pay yardstick has a deletion of its own, and no brief named it.** "Recurring gross
  profit" (RGP, $1,887M in FY2025) is subscription plus fintech gross profit with D&A and SBC added
  back. **It excludes the hardware and professional-services line altogether**, which lost **$220M**
  in FY2025. RGP exceeds GAAP gross profit ($1,593M) by $294M. The $220M is the cost of buying the
  position Q1 named as the scarce input, and **the bonus metric does not bear it.** [E4-27] asks
  what pay is funded on; here it is funded on a measure that omits both the stock pay and the
  acquisition subsidy. Recorded as a Q3 finding under [E2-26] (the same item not quantified at the
  line where it matters).
- [x] **Trumpeted projections [E4-22 third flag]: FIRES, with a beaten record.** Quarterly and
  annual guidance on non-GAAP gross profit and Adjusted EBITDA in every release. [E3-48] asks for the
  record: FY2025 Adjusted EBITDA was guided at **$510-530M** (2025-02-19), raised to $540-560M,
  $565-585M and $610-620M, and came in at **$633M**; RGP was guided at **$1,745-1,765M** and came
  in at **$1,887M**. Beaten every time. [E3-48] gives beaten guidance weight; [E5-30] says a
  guidance culture is a ratchet (*"do it once and you probably never stop"*). Both are carried.
- [x] **Serial share issuance [E5-15]: FIRED 2022-2025, then REVERSED in 2026.** Shares outstanding
  **523M (2022-12-31), 543M, 572M, 589M (2025-12-31)**: +12.6% in three years, on $242-277M a year
  of stock pay. H1 2026: *"Repurchased 19 million shares for $486 million"* (release of
  2026-08-04), taking the count to **577M** at 2026-06-30. The reversal is real and is recorded;
  so is the arithmetic that the H1 2026 buyback ($486M) was **4.5x** the H1 2026 stock-pay charge
  ($109M), i.e. cash is now being spent to retire what stock pay issued.
- [ ] **Weak accounting / period-shifting [E4-22 first flag, E4-34 fourth question]: NOT FIRED, but
  TWO PROMPTS recorded.** Revenue is booked gross and the 10-K states why (*"we are the principal in
  the delivery of the managed payments solutions"*); the Toast Capital guarantee is accounted for
  in a note a reader can follow. **Prompt 1:** H1 2026 depreciation and amortization fell to **$22M
  from $35M** (10-Q cash-flow statement) while software capitalisation continued at about $50M a
  year on a three-year life; the 10-Q discloses no change in estimate and reports *"no material
  changes in our significant accounting policies"*. **Prompt 2:** amortisation of deferred contract
  acquisition costs was **$46M in H1 2026 against $48M in H1 2025** on an opening balance that rose
  from $172M to $220M. Both movements flatter operating income by roughly $15M a half-year. **Owner
  earnings below are built on operating cash and are immune to both.** The FY2026 10-K is the
  document that will show whether either was an estimate change.
- [ ] **Unintelligible footnotes**: not fired; the notes are plain.
- [ ] **Filed-figure tells [E4-30]**: not fired. Growth is not unnaturally smooth (net adds by
  quarter 6,000, 8,500, 7,500, 8,000, 7,000, 9,500); cash tax is near zero on net operating losses
  (FY2025 tax expense $4M on $346M pretax), which is explained rather than falling.
- [ ] **Metric-switching [E2-49]: NOT FIRED.** The headline metrics (net adds, ARR, net income,
  Adjusted EBITDA) and the two guided metrics are the same in all seven releases from 2025-02-19 to
  2026-08-04. **What did change is the self-description, twice in six months** (Step 0 correction 1);
  that is a change of addressable-market claim, not of yardstick, and it is carried as a prompt, not
  a fire. **The [E2-49] prior now stands at six fires and six failures.**
- [ ] **Dividends funded by issuance [E2-52]**: none paid. **Stock-price targeting [E3-50]**: no
  instance found.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net income over average equity: **FY2024 1.4%** (19 / avg 1,194 and 1,545), **FY2025 18.6%**
(342 / avg 1,545 and 2,124), **H1 2026 annualised 26.9%** (280 x 2 / avg 2,124 and 2,045). Before
FY2024 the company lost money every year. **$1,991M of the $2,124M of FY2025 equity is cash and
marketable securities**, so the return on operating equity is far higher and is not a meaningful
ratio. The honest statement is that the test has **two years of data**, both rising; [E2-42] asks
for not less than five.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
Mixed. For: the 2023 letter; the gross-versus-net choice explained in the notes; the guarantee
disclosed with its roll-forward. Against: the public narrative and the pay are built on two measures
that remove stock pay, depreciation and the hardware subsidy, and the GAAP line that shows the
subsidy (hardware and professional services gross profit) is not a headline number anywhere.

### RATIONALITY IS CAPITAL ALLOCATION
- **Institutional imperative [E2-30]:** (1) resist change: not seen; (2) projects to soak up funds:
  **a prompt** (retail, international and enterprise pushes, and the addressable-market claim
  rewritten twice); (3) staff studies: no evidence either way; (4) imitation: not seen.
- **Acquisitions:** goodwill $113M unchanged since FY2023; no deal of size. [E3-40] not engaged.
- **The warrant**: a pre-IPO warrant on 5 million Class B shares at a $17.50 strike was repurchased
  on 2024-07-03 for **$61M** (FY2024, not FY2025 as the brief said); about 1 million warrant shares
  remain ($19M liability). The FY2025 10-K does not name the holder; the IPO registration statement
  is the document that would. Immaterial and not pursued.
- **Buybacks, the two conditions [E5-08] and the third [E4-31]:** (1) ample funds: **yes**, $1.99bn
  of cash and securities and no debt at FY2025, $1.71bn after the H1 2026 buyback ($1,015M cash and $698M marketable securities at 2026-06-30). (3) information
  supplied: yes. (2) **a material discount to conservatively calculated intrinsic value: NOT MET on
  this run's arithmetic.** The Q5 computation below puts owner earnings at about $0.33-0.36bn a
  year against a $17.7bn cap at today's price; the H1 2026 buyback was done at about **$25.60 a
  share** (19M shares for $486M), a cap of about $14.8bn, which is a **2.4% owner-earnings yield**
  at the FY2025 figure. That is not a material discount to any value this run can conservatively
  compute. **CAPITAL-ALLOCATION FLAG**, stated with the humility clause: *"it is natural for CEOs to
  be optimistic about their own businesses. They also know a whole lot more about them than I
  do"* **[E4-13]**, and *"infractions, even serious ones, are innocent"* **[E5-08]**. The flag binds
  position size, never the discount rate. (For completeness: the CEO *"expressed a preference for a
  reduced equity award for 2025 in light of the Company's focus on financial discipline and managing
  equity dilution"*, DEF 14A. Recorded as the rare-positive tell it is.)

### THE GUARDRAIL
- [x] Nothing here promotes the name; Q2 is closed and a strong Q3 could not repair it
  [E2-37, E2-38, E3-39].
- [x] Key-person dependence was tested at Q2 [E4-23]: none found.
- [x] No manager is being relied on as the plan [E2-35, E2-36].

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary**  [ ] OUT  [ ] UNRESEARCHED
  [ ] UNKNOWABLE
  *IN = no disqualifier found, not a finding of honesty [E5-17]. Gate case on daily execution.
  Carried: [E4-29] fires at full strength including the pay yardstick; the RGP bonus metric omits
  the $220M hardware subsidy; guidance culture with a beaten record; serial issuance 2022-25
  reversed by a 2026 buyback that fails buyback condition (2) on this run's arithmetic; two
  amortisation prompts for the FY2026 10-K.*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the
> queue asks every run for a price and because the evidence was gathered; it decides nothing and
> cannot reopen Q2 [E2-37, E3-39].

### THE SKIP REASON, TESTED ON THE FILING RATHER THAN INHERITED
The wave 5 label is *"capex unresolved [E5-20]: build (c) by hand from the filing"*. Three things
were checked, in the order the dated notes beside the table ask for.

**1. The current `owner_earnings()` prices the name, and reproduces exactly.** Re-run on the
companyfacts on disk: `{'5y_da': -65.4M, '5y_capex': -68.2M, '3y_da': +80.7M, '3y_capex': +78.3M}`,
the same four numbers the brief printed. So on the current screen the label is the CL/AMZN kind of
**tooling artefact**: `PaymentsToAcquirePropertyPlantAndEquipment` stops after FY2022 and
`PaymentsToAcquireProductiveAssets` takes over.

**2. Early-year facts: no NVDA-style hole, BUT A DEFINITION BREAK the brief's series hides.** The
two tags **overlap for FY2021 and FY2022 with different values**: the old tag reads **$12M and
$16M**, the new one **$19M and $33M**. The difference is capitalised software, which Toast
reported on a separate line (`PaymentsForSoftware` 7 and 17) until its FY2023 10-K folded both into
one *"Capital expenditures"* line and recast the comparatives. `floor_screen.annual(f, CAPX_TAGS)`
takes the first tag and returns the **software-excluded** figures for FY2019-22 (9, 28, 12, 16),
which is the series the brief quoted as *"a complete seven-year series"*; `owner_earnings()` reads
`capital_acquired()` instead and uses the **software-included** figures (15, 36, 19, 33). **The
screen's number was right and the brief's quoted series was a mixed definition**: four years
without software, three years with it. A two-paths split of the kind the 2026-09-12 resume note
lists, found again, and harmless to the screen only because the priced path was the fuller one.

**3. [E5-20] asked separately on the filing, and answered in words: NO.** Toast is not in the
capital-intensive exception class. Net property and equipment is **$105M** on $6,153M of revenue;
capital expenditure has run **0.8-1.1%** of revenue in FY2023-25; over FY2021-25 total capex of
**$201M** against D&A of **$187M** is **1.07x**, the [E2-41] and [E3-44] default case (*"capital
expenditures that over time roughly approximate depreciation"*). [E4-47] is not engaged: the 10-K
says Toast earned no material revenue outside the United States.

**4. WHAT THE D&A IS MADE OF (the third instruction of the SPGI note, and it bites).** FY2025 D&A of
$64M is:

| component | FY2025 | source |
|---|---:|---|
| **amortisation of capitalised internal-use software** | **$49M** | Note 7: *"Amortization expense attributable to capitalized software and website development costs was $ 49 million, $ 30 million, and $ 16 million"* |
| depreciation of other property and equipment | $8M | Note 7: *"Depreciation and amortization expense, which excludes amortization expense related to capitalized software ... was $ 8 million, $ 11 million, and $ 10 million"* |
| amortisation of acquired intangibles | about $6M | Note 5: accumulated amortisation $27M to $33M |

**77% of D&A is software.** And the capex line is its mirror: FY2025 capitalised software additions
were **$54M**, of which **$12M was stock-based compensation** (cash-flow supplemental: *"Stock-based
compensation included in capitalized software $12 $14 $13"*), so about **$42M** of the $53M cash
capex was software and about **$11M** was equipment (computer equipment, tooling, leasehold).
**The brief's prior 1 survives: the capex line is NOT hardware placed with customers.** Terminals
are sold, recognised at shipment, and their cost sits in cost of revenue, so the $220M subsidy is
already inside operating cash. **The brief's prior 3 is confirmed on the document** (capitalised
SBC is real, $12-14M a year), **with one correction:** the brief inferred it from additions of $54M
"exceeding" cash capex of $53M, a $1M gap; the filed non-cash figure is **$12M**, twelve times what
the arithmetic suggested, because cash capex also contains $11M of equipment that the additions
figure excludes.

**Of the six names now run from this row: ABNB had a real presentation gap, AMZN had no gap, NVDA
had a tag gap plus a history gap, CL had a tag gap only, SPGI had a tag gap plus a (c) question the
label misdescribes, and TOST has a tag gap plus a definition break in the overlap years, with a (c)
that is software on a three-year life. The exception class has applied at AMZN alone.**

### OWNER EARNINGS - THE ONE NUMBER **[E2-23]**
Construction (CONVENTION, v4 section VI): operating cash flow, less stock-based compensation, less
(c). Every figure from the filed cash-flow statements (FY2025 10-K `0001650164-26-000057`, FY2024
10-K, Q2 2026 10-Q `0001650164-26-000164`), cross-checked to companyfacts; never a net-income proxy.
**The Step 0 claim that four figures match the XBRL series is now checked: OCF $661M, capex $53M,
SBC $242M and revenue $6,153M all match companyfacts exactly.**

**Stock compensation is subtracted in full [E5-06], and at the capex end it must include the part
that was capitalised**, because the expensed charge excludes it and cash capex excludes it too, so
it would otherwise appear nowhere. At the D&A end it is already inside the software amortisation.
**This is the resume note's "SBC max-rule double-count" limit, and at this company it runs the other
way:** the risk is not counting capitalised SBC twice but counting it zero times.

| $M | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM to 2026-06-30 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| operating cash flow | -126 | -125 | 2 | -156 | 135 | 360 | 661 | 635 |
| SBC expensed | 34 | 86 | 142 | 228 | 277 | 253 | 242 | 231 |
| SBC capitalised into software | n/f | n/f | n/f | n/f | 13 | 14 | 12 | n/f (about 12) |
| capex incl. software | 15 | 36 | 19 | 33 | 42 | 54 | 53 | 59 |
| D&A | 7 | 27 | 21 | 24 | 32 | 46 | 64 | 51 |
| **owner earnings, (c) = capex** | **-175** | **-247** | **-159** | **-417** | **-197** | **39** | **354** | **about 333** |
| owner earnings, (c) = D&A | -167 | -238 | -161 | -408 | -174 | 61 | 355 | 353 |

*n/f = not filed in the documents on disk; FY2019-22 capitalised SBC would lower those years
further. TTM = FY2025 less H1 2025 plus H1 2026.*

**MORE THAN ONE WINDOW [E4-25, E4-38]:**
- **Five-year default [E2-42], FY2021-25: -$76M** at the capex end, -$65M at the D&A end.
- **Three-year, FY2023-25: +$65M** at the capex end, +$81M at the D&A end.
- **FY2025 alone: +$354M / +$355M. TTM: about +$333M / +$353M.**
- **The combined range runs from -$76M to +$355M. It spans zero.** [E4-25]: *"Usually, the range
  must be so wide that no useful conclusion can be reached."* **On the corpus's own default window
  this business has not yet earned owner earnings at all**; the positive figures come from the last
  two years. That is not a distorted year inside the window; it is a trajectory, and the window
  cannot be picked to hide it [E4-38].

**THREE ADJUSTMENTS, each shown both ways and none used to move the answer:**
1. **Interest income is inside operating cash, and Q1 said it was not (correction 4, below).**
   Under US GAAP interest received is an operating cash flow. FY2025 interest income was **$51M**
   (FY2024 $42M, FY2023 $37M), earned on Toast's own $1.99bn of cash and securities. Owner
   earnings from the business alone, FY2025, are **$303M**; the three-year mean is **$22M**. At
   Q5 the cash is carried separately and the interest is removed, not counted twice.
2. **Deferred commissions: growth spending inside operating cash.** Commissions paid exceeded
   commissions amortised by **$45M, $48M and $48M** (FY2023-25) and by **$47M in H1 2026 alone**
   (capitalisation $93M against amortisation $46M). At a steady state the two would be equal, so
   this gap is the cost of adding locations and is not maintenance. Adding it back lifts the
   three-year mean to **$112M**. **Not added back in the central figure**: [E2-23] (c) is a guess
   about maintenance, and the $220M hardware subsidy that sits beside it in operating cash cannot
   be split between new and replacement terminals on anything filed, so one growth add-back
   without the other would be selective.
3. **H1 2026 working capital**: inventories rose **$103M** in six months (*"higher inventory
   purchases"*, 10-Q MD&A), so the TTM operating cash of $635M is depressed against FY2025's $661M.
   `working_capital_flag()` fires on FY2021 accounts payable ($15M when OCF was $2M) and refuses the
   ratio in words; the dollars are trivial and it is not the line that matters here.

**(c): A DISCLOSED JUDGMENT.** Set at **total capital expenditure including capitalised software,
plus the capitalised SBC**. The two ends agree within $1M in FY2025 and within $22M in FY2024, so
the choice does not move the answer. The honest (c) question at this company is not plant: it is
whether a **three-year-life software asset** and **customer-acquisition spending that runs through
cost of revenue and commissions** are maintenance. The software is treated as maintenance (it keeps
the installed base from switching at renewal, Q2); the customer acquisition is left inside
operating cash as filed, which is conservative for a growing business and is disclosed above.

**STOCK COMPENSATION: THE RECORD IN THIS REGISTER.** SBC against operating cash:
- FY2025: **36.6%** (242/661); TTM 36.4%.
- **Over the listed life, FY2021-25: 114%** (1,142/1,002).
- **Over the whole filed record, FY2019-25: 168%** (1,262/751).
**Stock compensation exceeded all the operating cash the company has ever generated, by two-thirds.**
The register's previous marks were ARM at 96.6% and CALX at 98.4%, both closed at Q4. [E3-70]'s
grant-date measure was read by hand, as the resume note asks when SBC/OCF exceeds 50%: FY2025 RSU
grants were **6 million at $36.09** (about $217M) plus 2 million options at a $34.00 strike, so
the grant-date value is of the same order as the $242M charge and the charge is a fair floor. The
value delivered was larger: *"The fair value of RSUs vested during the fiscal years ended December
31, 2025, 2024, and 2023 was $ 405 million, $ 284 million, and $ 208 million"*, and option
exercises carried *"$ 278 million"* of intrinsic value in FY2025.

**Cumulative owner earnings FY2019-25 at the capex end: -$802M.**

### PER SHARE, THE SPGI CONSTRUCTION
Owner earnings per diluted share: FY2024 **$0.07** ($39M / 591M), FY2025 **$0.58** ($354M / 607M).
Every earlier year is negative, so no per-share growth rate can be computed across comparable
periods. Diluted shares rose from 533M (FY2023) to 607M (FY2025), **+13.9% in two years**.

### GREAT, GOOD, OR GRUESOME? **[E4-20, E4-43]**
- [ ] great
- [x] **good, on two years of evidence, after five gruesome ones**
- [ ] gruesome
FY2019-23 is the gruesome account in [E4-20]'s own words: *"grows rapidly, requires significant
capital to engender the growth, and then earns little or no money"*, with the capital supplied in
stock compensation and customer-acquisition losses rather than plant. FY2024-25 turned: owner
earnings went from -$197M to +$354M while gross profit grew 34%. [E4-43] says do not over-read;
[E2-42] says two years is not a test. **Recorded as good, provisionally, on the trajectory.**

### STAYING POWER - score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: PARTIAL.** Large in FY2025; reliable is not yet
  shown (two positive years).
- **(2) Massive liquid assets: YES.** $1,713M of cash and marketable securities at 2026-06-30, no
  debt, and an undrawn $350M revolver (*"our total available borrowing capacity under the 2021
  Facility was $ 347 million"*).
- **(3) No significant near-term cash requirements: YES.** Hardware purchase obligations of $106M
  and cloud commitments of $90M due within twelve months; the Toast Capital guarantee is capped by
  quarterly cohort and its liability was **$53M** (contingent) plus **$21M** (stand-ready) at
  2026-06-30, against $73M of restricted cash already posted as collateral.
- **Score: 2.5 of 3.** Leverage, named and quantified [E4-16, E3-29]: **none**; no interest is paid,
  so [E2-54]'s coverage test is not engaged.

**TOAST CAPITAL AND THE SECTOR METHOD.** The brief asked whether the insurer/lender treatment in
`Framework/SECTOR METHOD - owner earnings for insurers …` is owed. **It is not**, on three facts:
the business is not funded by float (the loans are originated and funded by the bank partner; the
only balance-sheet loans are $46M of performing loans bought in H1 2026 from Toast's own cash); the
guarantee's cash cost already runs through operating cash (loan purchases reduce the accrued
liability, $45M a year in FY2024-25 and $28M in H1 2026, against credit-loss expense of $62M and
$45M); and the exposure is capped. The $80M of H1 2026 loan purchases and $30M of repayments sit in
**investing** cash and are excluded from owner earnings as a new, small lending perimeter, named
here so a later run can size it.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism: take compression.** Toast earns $1,146M of fintech gross profit on $195.1bn of
  GPV. Its own 10-K says rivals offer *"lower customer processing rates and fees"* and that
  matching them *"ha[s] negatively affected"* results. Q2's row shows the largest rival, Square,
  growing in food and beverage at the same time.
- **Quantified from filed figures.** Each **1 basis point** of net take on FY2025 GPV is **$19.5M**
  of gross profit. A compression of **10 basis points** (0.587% to 0.487%, back below the FY2023
  level of 0.544%) removes **$195M**, which is **55% of FY2025 owner earnings** and **64% of the
  business-only figure** ($303M). Add a doubling of Toast Capital credit losses in a restaurant
  recession ($62M to about $124M, still inside the cap) and a GPV decline, and owner earnings return
  to roughly zero. The business does not go broke: it has no debt and $1.7bn of cash. **It dies as
  an investment by returning to the break-even economics it had in FY2023**, with a
  software-rebuild bill and a subsidy bill that do not shrink.
- **Exposure, not experience [E4-40]:** the credit record of the guarantee (2023-25) is a benign
  restaurant economy late in a cycle; the exposure is a quarterly-cohort cap nobody outside can see
  as a number.
- **Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility** for material take
  compression, because the company's own filing says it has already happened; **a low-level
  possibility** for insolvency.

**The Step 0/Q1 correction this section owes (CORRECTION 4).** Q1 says interest income *"is
outside owner earnings anyway because the construction starts from operating cash"*. It is
inside: US GAAP classifies interest received as operating cash. Handled above by showing owner
earnings with and without it, and at Q5 by removing it and carrying the cash separately.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival**  [ ] OUT  [ ] UNRESEARCHED
  [ ] UNKNOWABLE
  *The business survives: no debt, $1.7bn of liquid assets, positive operating cash for three
  years. But the owner-earnings range on the default five-year window spans zero (-$76M to
  +$355M), which on its own would have made Q5's answer "no useful conclusion" [E4-25] on that
  window; stock compensation has consumed 168% of all operating cash ever filed, a new high in the
  register.*

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION - NOT A CLEARANCE
*Q5 does not open: Q2 is OUT. The arithmetic below is recorded because the queue asks every run for
a price, and it carries no entry language. It is not a ranking and it arms nothing.*

**The pair:** price **US$30.65**, the **2026-09-17 close** (Yahoo daily chart, aggregator, flagged;
2026-09-18 had not closed when this was written) x **578 million shares** (514M Class A + 64M Class B,
10-Q cover, accession `0001650164-26-000164`, as of 2026-07-30; the classes are economically
identical and are summed) x split factor **1.0** = **market capitalisation US$17,715.7M**, good to
about +/-0.1% because the filer rounds its count to the million. Less **$1,713M** of cash and
marketable securities at 2026-06-30 (restricted cash and cash held for customers' payroll excluded)
= **US$16,002.7M** for the business. **Sovereign USD 30-year 5.29%**, US Treasury daily par yield
curve, the issuing authority, **09/17/2026**.

**Interest is removed from owner earnings and the cash is carried separately**, so it is counted
once (Q4 correction 4).

| construction | owner earnings | on | yield | multiple | vs 5.29% | growth needed, forever, to reach ~10% |
|---|---:|---|---:|---:|---:|---:|
| five-year default, FY2021-25 | **negative (-$76M)** | | **none** | | | **not computable** |
| three-year mean FY2023-25, ex-interest | $22M | business | 0.14% | 727x | -5.15 pts | 9.86% |
| TTM to 2026-06-30, ex-interest | about $281M | business | 1.76% | 57x | -3.53 pts | 8.24% |
| **FY2025, ex-interest (central)** | **$303M** | business | **1.89%** | **53x** | **-3.40 pts** | **8.11%** |
| FY2025 + the commission growth add-back, ex-interest | $351M | business | 2.19% | 46x | -3.10 pts | 7.81% |
| FY2025 with interest, on the whole cap | $354M | cap | 2.00% | 50x | -3.29 pts | 8.00% |

**1. THE YIELD.** $303M / $16,002.7M = **1.89%**, against a sovereign of **5.29%**.

**2. WHAT THE PRICE ALREADY ASSUMES.** From the best full year ever filed, owner earnings must
compound at **about 8% a year in perpetuity** to reach the ~10% floor, and at **3.4%** merely to
match the bond. **What the business has actually done** cannot be stated as an owner-earnings
growth rate, because every year before FY2024 is negative; gross profit grew 43% and 34% in the
last two years, and the company guides FY2026 recurring gross profit up 23-25%. [E4-35]'s base rate
is the burden: 8% forever from a first-profit year is a claim the corpus says fewer than one in
twenty of the best businesses meet at 15% for twenty years, and this one is not yet five years
profitable. **[E4-44] and [E2-63] are the binding bounds**: value cannot outgrow earnings, and Q2
found no pricing power to carry the growth once the location wave slows.

**3. WHAT YOU ARE PAID.** **Minus 3.4 points against the sovereign** on the central construction;
minus 3.1 at the most generous; nothing at all on the five-year default window.

**Certainty is not priced in the rate [E3-42].** Sovereign used 5.29%, bare. No per-name premium.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
Cap = owner earnings / (0.10 - g), plus the $1,713M of cash, over 578M shares:

| owner earnings | g = 3% | g = 5% | g = 7% | g = 8% |
|---|---:|---:|---:|---:|
| **$303M (central)** | $10 | $13 | $20 | $29 |
| $351M (with the commission add-back) | $12 | $15 | $23 | $33 |

**Value, in round numbers: roughly $10 to $25 a share** on the central figure at 3-7% perpetual
growth. **Current price: $30.65, above the range**, and inside it only if 8% perpetual growth is
granted on the most generous construction. **On the corpus's five-year default window no value can
be computed at all**, because owner earnings are negative: that window's answer is [E4-25]'s *"no
useful conclusion can be reached"*.

**Which bar:** the screamer test [E4-01] only, because the file is closed and no margin is applied.
The conservative end (the three-year mean) is about **$3-4 a share** including the cash; the price
is roughly eight times it. **Above the whole range on every construction but one.**
**Windage count: ONE** ((c) at total capex plus capitalised SBC, worth $1M in FY2025 against the
D&A end); leaving the commission and hardware growth spending inside operating cash is disclosed
and priced both ways, not spent as a second margin.

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a
  1.9% business yield against a 5.29% sovereign and a ~10% floor: below both, **FAIL** on price as
  well, and **no useful conclusion** on the five-year window.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed. These are the conditions on
> which the file would be REOPENED at Q2 [E1-02]; a Q2 OUT is a finding about the business, so a
> price alert would be a category error (the QLYS ruling, 2026-09-07).

**What would reopen Q2 (each observable in a filing):**
1. **A broad-based price increase that holds.** A filed statement of a subscription or processing
   price rise, followed by net location adds that do not fall and a take that rises faster than
   Square's. That is [E3-03]'s *"ability to regularly price its product or service aggressively"*,
   which the 2023 letter shows was absent.
2. **Disclosed retention.** A churn or gross-retention figure in a 10-K or earnings release showing
   that installed restaurants rarely switch away. Nothing filed today shows it.
3. **The concession sentence disappears.** A 10-K whose competition risk factor no longer says rate
   concessions *"have negatively affected"* results.
4. **Dominance, not share.** Toast's own estimate of its share of US restaurant locations moving
   from ~20% toward a level at which [E2-53]'s dominance class could be argued, with the legacy
   segment (NCR Voyix Restaurants) and the cloud rivals shrinking in the filed row.

**Thesis-confirming (for the OUT):** fintech gross profit / GPV falling back toward the FY2023 level
of 0.544%; hardware and professional-services losses widening; rivals' filed volumes growing in food
and beverage.

**Next dated documents:** the Q3 2026 10-Q and earnings release (early November 2026) and the FY2026
10-K (February 2027), which will also answer Q3's two amortisation prompts.

**Position size:** none. **VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at
Q2 and the reopening conditions are recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN (first session, verified and corrected
  by dated note) → **Q2 OUT, the file closed**; Q3-Q6 recorded beneath explicit RECORDED, NOT
  GOVERNING banners, as at NVDA.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN was
  re-verified line by line. The two UNRESEARCHED cells in Q2 (Clover's numbers; churn, which no
  document publishes) are named and are not what closes the gate.
- [x] No UNRESEARCHED verdict was returned; the Clover cell names its artefact (Fiserv investor
  slides, company IR site rung).
- [x] No UNKNOWABLE verdict was returned.
- [x] Step 0: the filing was read with accession numbers; four figures cross-checked to
  companyfacts at Q4, and the Step 0 claim that they matched is now true rather than asserted.
- [x] Owner earnings on multi-year windows (five-year default, three-year, FY2025, TTM); (c)
  disclosed as a judgment and shown at both ends; capitalised SBC subtracted at the capex end.
- [x] Competitor row filled: nine examined, five numbered; Clover UNRESEARCHED; privates tested
  against a universal-filing route and recorded as not resolving.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/17/2026,
  re-fetched by this session.
- [x] Value stated as a round-number range under a COMPUTATION - NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as a close, aggregator flagged, cross-checked against a Form 4.
- [x] Run committed to git after every question, with a pathspec.
- [x] Every ledger id cited was checked to exist in `principle_ledger.csv` (267 rows).
- [x] No em dashes in anything this session wrote (the template's own headings carry them).

### THINGS THE RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q1, the self-description** (first session): two rewrites in six months, not one in eighteen.
2. **Q1, the float** (first session): "cash held on behalf of customers" is payroll float;
   restricted cash is Toast's own collateral; neither is merchant float.
3. **Q1, Toast Capital** (first session): the credit risk is a capped first-loss guarantee, and
   H1 2026 added $46M of loans held on balance sheet.
4. **Q1, interest income** (first session): it is inside operating cash, not outside it. Q4 shows
   owner earnings both ways and Q5 removes it and carries the cash separately.
5. **This session**, before commit: Q3 first said $1.6bn of cash after the H1 2026 buyback; the
   balance sheet says $1,713M. Corrected in the draft.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The warrant repurchase is dated to the wrong year.** The brief puts *"Warrant repurchase
   ( 61 )"* in **FY2025** financing. The cash-flow columns are 2025, 2024, 2023 and the line reads
   *"— ( 61 ) —"*: it is **FY2024** (the repurchase closed 2024-07-03), as is the $14M
   extinguishment gain.
2. **The quoted capex series mixes two definitions.** *"9, 28, 12, 16, 42, 54, 53"* is
   `annual(f, CAPX_TAGS)`, which returns the **software-excluded** figures for FY2019-22; FY2023-25
   include software. The two tags overlap in FY2021-22 with different values (12/16 against 19/33).
   `owner_earnings()` reads `capital_acquired()` and uses the fuller figures, which is why the
   screen's numbers reproduce while the brief's series does not reconcile for FY2019-22. The brief
   also said `PaymentsToAcquireProductiveAssets` carries FY2023-25; companyfacts carries FY2021-25.
3. **The capitalised-SBC inference was right in direction and wrong in size.** Additions of $54M
   exceed cash capex of $53M by $1M; the filed non-cash SBC in software is **$12M** (cash-flow
   supplemental), because cash capex also contains about $11M of equipment.
4. **The float was misnamed.** The brief called the customer cash merchant float; the notes say it
   is money held to remit customers' payroll taxes, and restricted cash is Toast's own collateral.
   The brief was right that interest may sit inside income; it missed that interest income on
   **all** of Toast's cash sits inside operating cash.
5. **The credit-loss figure was attributed wholly to Toast Capital.** Of the $91M FY2025
   *"Credit loss expense"*, **$62M** is the Toast Capital guarantee (Note 4); **$22M** is the
   receivables allowance (Note 7); the rest is other.
6. **The competitor list omitted the one pure restaurant filer and included a non-filer.** NCR
   Voyix (Aloha) reports a Restaurants segment and names Toast as a key competitor; it was not
   listed. Olo was listed as a filing rival; it filed a Form 15-12G on 2025-09-23 after its merger.
7. **The brief did not know the Toast Capital perimeter moved in 2026** ($46M of loans held for
   investment at 2026-06-30), because it read only the 10-K note.
8. **The brief's prior 2 (credit risk sits with the bank) was wrong, as the brief feared; prior 1
   (the capex label is a tooling artefact and the real (c) question is software) was right; prior
   3 (capitalised SBC) was right in direction.** Prior 4 was honoured: the brief named no gate, and
   the gate that closed (Q2) was not one the brief pointed at.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- `tools/sources.price()` returns an intraday `regularMarketPrice` stamped with today's date while
  its docstring says *"Latest close"* (found by the first session, reproduced by this one at 13:09
  EDT). Every run striking a price during market hours must use the chart's last completed close.
- `floor_screen.annual(f, CAPX_TAGS)` and `capital_acquired()` disagree where two capex tags
  overlap with different scopes (TOST FY2021-22). The priced path is the right one; a brief or run
  that quotes `annual()` gets a mixed-definition series.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**The 8-K Item 7.01 customer letter is the [E4-37] document.** The agony metric had been argued
from pricing language in 10-Ks; here a company filed its own prayer session, with a date, a price
(99 cents) and an apology. For any business that sells to small merchants, search the 8-K
exhibits for letters to customers before scoring [E2-44](1).

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** TOST FAILS AT Q2 (OUT, on [E3-03] criterion 2 as Toast's own filings test it and on
  [E4-04] in its own words; a surfing run, not a franchise). Q1 IN; Q3 IN on the binary (recorded,
  gate case on daily execution, [E4-29] fires in the bonus yardstick); Q4 IN on survival (recorded;
  owner earnings -$76M five-year to +$355M FY2025, SBC 168% of all operating cash ever filed);
  price $30.65 x 578M = $17.7bn, headed COMPUTATION - NOT A CLEARANCE: 1.89% business yield
  against a 5.29% sovereign; Q6 arms nothing.
- Work order: none. UNKNOWABLE: none.
