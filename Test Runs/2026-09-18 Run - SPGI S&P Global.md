# Company Run — S&P Global Inc. (SPGI) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

CIK **0000064040** · SIC **7320** (Services—Consumer Credit Reporting) · NYSE · one class of
common stock. **WAVE 5, the fifth of the eight "capex unresolved [E5-20]" names** in
`Screens/WATCHLIST RUN QUEUE.md` (ABNB, AMZN, NVDA and CL are run; TOST, EQIX and DLR follow).

*A pre-v4 run of this name exists — `Test Runs/2026-07-15 Run - SPGI (S&P Global).md`. It is
read for leads only. **No conclusion and no number is inherited from it**; it predates the hard
sequence, the SBC fix, the split-invariant cap and the issuing-authority sovereign.*

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

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a
forecast **[E4-15, E3-32]**:
- rate **5.29 %** · date **09/17/2026** · source **US Treasury daily par yield curve, 30 Yr —
  the ISSUING AUTHORITY**, not FRED (`tools/sources.py:sovereign('USD')`; the cache was deleted
  and the curve re-fetched at 09:20 on 2026-09-18, so this is struck fresh and not inherited).
  The 09/18 curve is not yet published; 09/17 is the latest observed. The curve's own adjacent
  rows: 09/16 5.35, 09/15 5.32. **The brief's 5.29% was NOT inherited — it was re-struck and
  happens to agree.**
- FX: **none needed.** S&P Global reports in USD; the sovereign and the quote are the same
  currency as the earnings.

**Price — the aggregator, flagged, and dated:**
- **US$404.11**, close of **2026-09-17** (`tools/sources.py:price('SPGI')`, aggregator quote,
  flagged as such per operator rule 5). 2026-09-18 has not closed.
- **EDGAR re-queried 2026-09-18 09:15.** `submissions.json` re-downloaded from
  `data.sec.gov` this morning: **the newest filing of any kind is a Form 4 of 2026-08-04**
  (accession `0002142367-26-000004`). **There is nothing filed after 2026-09-13, and no Form 4
  in the window**, so unlike the CL run the quote cannot be cross-checked against a primary
  filing. Recorded as a limit, not worked around.

**Share count — the dei element is stale and the cover is NOT the whole story.**
- The newest `EntityCommonStockSharesOutstanding` in companyfacts is **296,000,000 at
  2026-04-24** (10-Q `0000064040-26-000024`), and SPGI's dei values are rounded to the
  hundred-thousand (298,800,000 · 305,300,000 · 302,800,000 …).
- **The 10-Q filed 2026-07-28 is newer and its cover is not in dei. Read by hand, verbatim,**
  10-Q for the quarter ended 2026-06-30, accession **`0000064040-26-000045`**:
  > *"As of July 24, 2026 (latest practicable date), **294.8 million shares** of the issuer's
  > classes of common stock (par value $1.00 per share) were outstanding **excluding 7.2 million
  > outstanding common shares held by the Markit Group Holdings Limited Employee Benefit
  > Trust**."*
- **THE ERIC TRAP, CHECKED AND PRESENT.** The cover count is **outstanding**, not issued. The
  same 10-Q's balance sheet reads *"Common stock, $1 par value: authorized - 600 million shares;
  **issued - 2026 and 2025 415 million shares**"* against treasury of **$38,307M**. Issued 415M
  against outstanding ~295M is a **120M-share gap**; a run that took the issued count would have
  over-stated the cap by roughly **41%**. Outstanding is used.
- **A SECOND, SMALLER TRAP THE BRIEF DID NOT NAME — and it runs the other way.** The cover
  figure **excludes 7.2 million shares that the cover itself calls OUTSTANDING**, held by a
  Markit employee benefit trust inherited in the 2022 merger. The trust is named nowhere else in
  the 10-K or the 10-Q — not in the equity note, not in the EPS note — so the filing gives no
  basis for treating those shares as anything but company-held, treasury-equivalent stock, which
  is why the registrant excludes them from its own denominator. **The headline count is the
  registrant's 294.8M.** The 7.2M is quantified separately rather than blended, per **[E2-26]**:
  at $404.11 it is **+$2,910M of cap, +1.0%**, and it moves the Q5 yield by about 0.03 points.
  It changes no verdict and is recorded, not spent as windage.
- **Splits after the measurement date: none.** S&P Global's last split was 2-for-1 in 2005;
  `sources.split_factor_after('SPGI', '2026-07-24')` returns **1.0**. `cap = close(2026-09-17) ×
  shares(2026-07-24) × 1.0`, using `close`, never `adjclose`.
- **Pre- or post-spin?** **Read after the event, and unaffected by it.** The Mobility separation
  was a *distribution of Mobility Global shares to S&P Global holders*, one MBGL share for each
  SPGI share; SPGI's own count was not changed by it. The 2026-07-24 cover date is 23 days after
  the 2026-07-01 distribution, so the count is post-spin either way. The decline from 305.3M
  (2025-07-25) to 294.8M is **buybacks**: $5,001M in FY2025 and $1,500M in H1 2026, off the
  filed cash-flow statements.

**MARKET CAP: US$404.11 × 294,800,000 × 1.0 = US$119,131.6M (~$119.1bn).**
*Sensitivity, recorded and not blended: including the 7.2M EBT shares gives $122,041.6M.*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: Form 10-K for FY2025, filed 2026-02-11, accession `0000064040-26-000013`** (auditor
  Ernst & Young LLP, unqualified, report dated 2026-02-10; one critical audit matter — the
  valuation of the redeemable noncontrolling interest in S&P Dow Jones Indices LLC).
- Also read: 10-K FY2017 through FY2024 (nine annual reports in all); the 10-Q for 2026-06-30
  (`0000064040-26-000045`) and 2026-03-31 (`0000064040-26-000024`) and the three 2025 10-Qs;
  DEF 14A of 2026-03-31 (`0001104659-26-037380`), 2025 and 2024; the 8-K of 2026-07-28
  (`0000064040-26-000040`, items 2.02/7.01/9.01) **with its EX-99.1 earnings release**; the
  separation 8-K of 2026-07-02 (`0001104659-26-080005`, items 1.01/2.01/8.01/9.01) with the
  Separation and Distribution Agreement; **the 8-K/A of 2026-07-06 (`0001104659-26-080571`)
  with its EX-99.2 pro forma and EX-99.1 recast** (see the perimeter section — this is the
  document the run turns on); the five May 2026 8-Ks; and the S-4 of 2026-07-09.
- **Figure cross-checked against the filed statement:** XBRL
  `NetCashProvidedByUsedInOperatingActivities` FY2025 = **$5,651M**; the filed FY2025
  Consolidated Statement of Cash Flows reads *"Cash provided by operating activities | 5,651 |
  5,689 | 3,710"*. Second cross-check: XBRL `PaymentsToAcquireProductiveAssets` FY2025 =
  **$195M**; the filed statement reads *"Capital expenditures | ( 195 ) | ( 124 ) | ( 143 )"*.
  Both agree to the dollar.

---
## LIVE-DEAL CHECK — done, and cleared

**The S-4 of 2026-07-09, accession `0001104659-26-082258`** (registrant S&P Global Inc.,
additional registrant Standard and Poor's Financial Services LLC), read on the document rather
than taken from the brief. Its cover:
> *"We are offering to exchange up to $600,000,000 of our new registered 4.250% Senior Notes due
> 2031 … for up to $600,000,000 of our existing unregistered 4.250% Senior Notes due 2031 … and
> up to $400,000,000 of our new registered 4.800% Senior Notes due 2035 … **We will not receive
> any proceeds from the exchange offer.**"*

A search of the whole document for "merger agreement" returns **zero hits**. This is the **AVGO
shape** — a registered notes exchange offer, read and cleared. It went effective 2026-07-17
(`EFFECT`, `9999999995-26-002351`) with the 424B3 filed the same day. **The quote is not a
deal spread.**

**The other 2026 8-Ks, all read:** 2026-05-07 (7.01 — Mobility Global's Form 10 filed),
2026-05-12 (7.01 — Mobility investor day deck), 2026-05-18 and 2026-05-20 (8.01 — Rule 135c
notices of Mobility Global's $2.0bn private note offering, priced 2026-05-19 as $650M 5.050%
due 2029, $650M 5.450% due 2031, $700M 6.050% due 2036), 2026-05-21 (8.01 — the board's
approval of the separation and the 2026-06-15 record date), 2026-07-06 (5.02 — the Chief Legal
Officer's retirement). **None of the five May filings is the segment recast the brief asked me
to look for.** The recast is in a filing the brief classed as merely unread; see the next
section.

---
## THE PERIMETER — TWO EVENTS, AND THE SECOND IS ALREADY SOLVED ON EDGAR

### A. The IHS Markit merger — dated from the filing
Note 2 of the FY2022 10-K: the IHS Markit merger **closed on 28 February 2022**, an all-stock
transaction. Its fingerprint is on the face of the cash-flow statement — **amortization of
intangibles steps from $96M (FY2021) to $905M (FY2022) to $1,069M (FY2025)**, while
*Depreciation* alone runs $82-110M across the same years. That is purchase accounting, and it
is the whole of the D&A discontinuity the tooling flags.

### B. The Mobility spin-off — completed 2026-07-01, and **the subtraction is FILED**
8-K of 2026-07-02, accession `0001104659-26-080005`, items 1.01/2.01/8.01/9.01:
> *"On July 1, 2026 … the previously-announced separation … of Mobility Global Inc. … became
> effective … through S&P Global's distribution of 100% of the shares of Mobility Global common
> stock to holders of S&P Global common stock … one share of Mobility Global common stock for
> every share of S&P Global common stock … **S&P Global retains no ownership interest in
> Mobility Global.**"*

**The 10-Q filed 2026-07-28 does NOT present Mobility as discontinued operations**, and says so
in terms — the spin fell one day after the quarter end:
> *"The results of Mobility are included through June 30, 2026. **Beginning with the third
> quarter of 2026**, the historical financial results of Mobility through June 30, 2026 will be
> reflected in our consolidated financial statements as discontinued operations in accordance
> with U.S. GAAP for all periods."*

**So every filed financial statement of S&P Global describes a company that no longer exists.**
The registrant being priced today is smaller than the whole filed history — the HHH shape in
reverse.

**A DEFECT IN MY BRIEF, AND THE FIND IT HID.** The brief sent me to the May 8.01 filings to
look for a segment recast and told me the MBGL Form 10-12B/A was the source for the
subtraction. Neither is where the answer is. **The 8-K/A of 2026-07-06, accession
`0001104659-26-080571`, filed under items 7.01/9.01, carries as EX-99.2 an Article 11
UNAUDITED PRO FORMA CONDENSED CONSOLIDATED INCOME STATEMENT FOR FY2023, FY2024, FY2025 AND
Q1 2026, AND A PRO FORMA BALANCE SHEET AT 2026-03-31, all on the S&P-Global-without-Mobility
perimeter**, and as EX-99.1 the four-quarter 2025 and Q1-2026 recast. The brief listed that
accession only as "unread". It is the document that settles the whole perimeter question, and
it beats the Form 10 for this purpose, because the Form 10's *combined* Mobility statements are
charged allocated overhead that **stays with S&P Global**, while the pro forma's
discontinued-operations column is scoped to what actually leaves.

The pro forma says so itself, in note (a):
> *"Certain liabilities and general corporate overhead expenses that were not specifically
> related to Mobility were **excluded**, as they did not meet the discontinued operations
> criteria including: i. **General corporate overhead costs which were historically allocated to
> Mobility** that included labor and non-labor expenses related to the Company's corporate
> support functions (e.g. finance, accounting, treasury, information technology, legal, among
> others) that historically provided support to Mobility."*

**Filed pro forma, S&P Global continuing operations, $M** (EX-99.2, 8-K/A `0001104659-26-080571`):

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Revenue, as filed (consolidated) | 12,497 | 14,208 | 15,336 |
| less Mobility, discontinued-ops column | 1,484 | 1,609 | 1,747 |
| **Revenue, continuing** | **11,013** | **12,599** | **13,589** |
| Depreciation, continuing | 92 | 83 | 96 |
| Amortization of intangibles, continuing | 740 | 775 | 766 |
| **Operating profit, continuing (subtotal)** | **3,703** | **5,206** | **6,105** |
| Net income from continuing ops attributable to SPGI | 2,371 | 3,569 | 4,166 |
| after transaction accounting adjustments | 2,371 | 3,569 | **4,192** |

**Mobility is 11.4% of FY2025 revenue and 5.8% of FY2025 operating profit** — a smaller share
of profit than of revenue, because the corporate overhead that supported it does not leave.

**And the separation moved cash and debt**, note (b) and the H1 2026 statements:
- *"Reflects the **net cash distribution to the Company received from Mobility Global of $1.974
  billion** in connection with the Separation."* The $2.0bn of Mobility notes issued 2026-05-19
  sat on S&P Global's 2026-06-30 balance sheet and *"became the sole responsibility of Mobility
  Global after the Separation."* On 2026-07-01 the parent kept the cash and shed the debt.
- Pro forma balance sheet at 2026-03-31: cash **$3,663M**, short-term debt $2,697M, long-term
  debt **$10,621M** (against $12,598M consolidated at 2026-06-30, which still included the
  Mobility notes).
- Notes (c) and (d): $50M of additional separation tax liabilities and $106M of one-off
  separation costs, both quantified on the face.

**THE RULING, justified from the corpus rather than from convenience.** I do **not** blend and
I do **not** refuse the crossing windows outright. **[E4-25]** requires the spread to be carried
rather than resolved by preference, and **[E4-38]** requires every window to be published rather
than one selected. So Q4 reports **three perimeters, each named, never mixed inside one mean**:
1. **FY2023-FY2025, continuing operations ex-Mobility** — the perimeter that is being priced:
   post-IHS-Markit and post-spin, covered end to end by the filed Article 11 pro forma. Three
   years, short of **[E2-42]**'s five, and that shortfall is itself a Q4 finding.
2. **FY2021-FY2025 as filed** — the [E2-42] default five-year window, on the consolidated
   perimeter. It crosses the IHS Markit close of 2022-02-28 **and** contains a business that has
   since been distributed away. Reported, and labelled as measuring a company that no longer
   exists.
3. **FY2017-FY2021 as filed** — old S&P Global standalone, before the merger: a clean five-year
   window on one perimeter. Reported as the pre-merger reference, and as the base against which
   the merger's effect is read.

This is the **SONY splice measured**, not the CNR rebuild. The rebuild is unnecessary here
because the registrant has already filed the pro forma, which is up the evidence ladder from
anything I could construct by hand.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** S&P Global sells four
different things and they are not one business:

1. **Ratings ($4,724M of FY2025 revenue including $175M charged to a sister segment; $3,013M of
   segment operating profit; 63.8% margin).** When a company or a government borrows money, the
   people lending it want a short, comparable statement of how likely they are to be repaid.
   S&P sells the borrower that statement — a letter — and charges twice: once when the bond is
   issued, at a fee scaled to the size of the issue (**transaction revenue, $2,470M**), and every
   year thereafter for keeping the letter current (**non-transaction revenue, $2,254M**). The
   cost of producing one more rating is an analyst's time; the fee scales with the size of the
   borrowing, not with the work. **Ratings' entire balance sheet is $1,137M of total assets** and
   it earned **$3,013M** on it in 2025.
2. **Indices ($1,850M revenue, $1,271M operating profit, 68.7% margin).** The S&P 500 and the Dow
   Jones averages are *lists*. The company charges a fee on the money that tracks each list
   (**asset-linked fees, $1,206M**), a royalty on futures and options written against it
   (**sales usage-based royalties, $324M**) and a subscription for the data (**$320M**). The
   cost of maintaining a list is a committee and a calculation engine: **segment capex was $4M
   in 2025 on $3,378M of total assets**. It is a partnership — CME Group and CME Group Index
   Services hold the minority, carried as a **redeemable** noncontrolling interest of **$4,914M**.
3. **Energy ($2,299M revenue, $943M operating profit, 41.0% margin).** Platts prints a daily
   assessed price for physical cargoes of oil, gas, chemicals, metals and agricultural goods.
   Counterparties write *"Platts Dated Brent"* into their own supply contracts, and exchanges pay
   a royalty to settle derivatives against the number. Mostly subscription ($2,016M).
4. **Market Intelligence ($4,916M revenue, $991M operating profit, 20.2% margin).** Desktops,
   data feeds and workflow software sold to banks, asset managers and corporates — Capital IQ,
   RatingsXpress, Enterprise Data Manager. **Total assets $31,234M**, almost all of it goodwill
   and intangibles from the IHS Markit merger, earning **$991M**.

**Mobility is gone** (see the perimeter section): $1,747M of revenue and $378M of segment
operating profit left the company on 2026-07-01.

**THE SCARCE INPUT THE BUSINESS CONTROLS, and it is the same one in three of the four legs.**
It is not data, and it is not people. **It is a reference that third parties have written into
their own binding documents.** An investment mandate says *"rated BBB– or better by S&P"*; a
fund prospectus and a listed futures contract say *"the S&P 500 Index"*; an oil cargo contract
says *"Platts Dated Brent"*. The customer who would have to switch is not the payer — it is
every counterparty to every document that already names the reference. The payer has no unilateral
way out. That is the asset. Market Intelligence has **no such asset**; it sells data that other
people also sell, which is why the same company earns 63.8% and 68.7% in two segments and 20.2%
in a third.

**Will the fundamentals look broadly the same in ten years?** For Ratings, Indices and Energy:
**yes, and the record is long** — Ratings has been doing this for over 150 years; the S&P 500
dates from 1957; the Platts assessments are older than the futures markets that settle against
them. For Market Intelligence: **no**, and the 10-K says so in its own risk factors — *"the
effect of competitive products (including those incorporating artificial intelligence ('AI'))"*,
*"our ability to develop new products or technologies, to integrate our products with new
technologies (e.g., AI), or to compete with new products or technologies offered by new or
existing competitors"*, *"the introduction of competing products (including those developed by
AI) or technologies by other companies"*. That is recorded here and carried into Q2 as a
question about **which leg** is being called a franchise.

**Where it earns: 61% United States**, 23% Europe, 11% Asia, 5% rest of world (Note 12), and *"We
do not have operations in any foreign country that represent more than 7% of our consolidated
revenue."* **The USD sovereign is the right one** — no FX question arises.

**Two marks against [E3-31]'s "relatively simple and stable in character", both recorded rather
than waved through.** The *perimeter* has moved four times in five years — the IHS Markit merger
(2022-02-28), the Engineering Solutions sale (2023-05-02), the OSTTRA sale (2025-10-10) and the
Mobility spin (2026-07-01) — and a reader cannot compare any five-year series without doing the
arithmetic by hand. And the reported structure changed again on 2026-07-01: *"Effective July 1,
2026, we have four reportable segments"*, with 451 Research and Maritime & Trade moving from
Market Intelligence to Energy and Credit Analytics products moving from Market Intelligence to
Ratings. **The businesses themselves are legible; the reporting entity is restless.** 79% of
FY2025 revenue is recognised over time ($12,192M of $15,336M), which is what makes the underlying
streams predictable even while the box around them moves.

**VERDICT: [x] IN**
*I can state, without management's vocabulary, what each of the four legs sells, who pays, what
the incremental cost is, and what would have to happen for the payer to stop. The perimeter
churn is a real cost to the reader and it is recorded; it does not make the cash flows
unpredictable, which is what [E3-31] asks.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### WHICH LEG IS BEING TESTED, AND WHAT FRACTION OF PROFIT IT IS

On the perimeter being priced (FY2025, continuing operations, Mobility removed), reportable
segment operating profit is **$6,218M** and it divides like this:

| segment | FY2025 segment operating profit | share of continuing | net of the Indices minority | share |
|---|---|---|---|---|
| **Ratings** | **$3,013M** | **48.5%** | $3,013M | **51.1%** |
| Indices | $1,271M | 20.4% | **$949M** *(the filing's own "net operating profit" line, after $322M to the noncontrolling partners)* | 16.1% |
| Market Intelligence | $991M | 15.9% | $991M | 16.8% |
| Energy | $943M | 15.2% | $943M | 16.0% |
| **total** | **$6,218M** | 100% | **$5,896M** | 100% |

**The claim being made, and it is deliberately narrow: RATINGS is the franchise, and it is about
half the profit of the company being priced.** Indices is tested and comes out narrower than its
margin suggests. Energy is tested and held **PROVISIONAL**. Market Intelligence — $31.2bn of the
$44.3bn of continuing segment assets — **fails criterion (2) on its own filing** and is not
claimed. The verdict below rests on Ratings and on nothing else.

### THE THREE CONDITIONS, ON RATINGS **[E3-03]**

**(1) Needed or desired — IN, and the evidence is that people pay for it after they have already
got it.** $2,254M of FY2025 Ratings revenue is **non-transaction** — surveillance and
relationship fees on debt that has already been issued and sold. Nobody is compelled to keep a
rating current on a bond already in the market; **1,077,798 outstanding S&P credit ratings** say
they do (Form NRSRO Item 7A, accession `0001650548-26-000001`, as of 2025-12-31).

**(2) No close substitute — IN, and this is the condition the run spent its evidence on.**
See the competitor row below. Three separate tests, all filing-sourced, point the same way:
- **Concentration.** S&P Global Ratings holds **49.4%** of all credit ratings outstanding across
  the nine registered NRSROs that report a count; the top three hold **92.9%**.
- **The two largest earn the same extraordinary margin at the same time, and both are rising.**
  If the products were close substitutes, one of them would be undercutting the other.
- **The 2015 stress test, and it is the sharpest evidence in the file.** In FY2014 S&P accrued
  the DOJ and state settlements and **Ratings' segment operating margin fell to 6%, from 34%**
  (FY2014 10-K, accession `0000064040-15-000004`): *"the Company agreed to pay $687.5 million to
  the United States as a civil monetary penalty … and $687.5 million in aggregate to the States"*,
  plus $125M to CalPERS, plus *"a total of $58 million"* to the SEC under a censure and $19M to
  New York and Massachusetts. Eleven years later the same segment earns **63.8%** and has more
  ratings outstanding than anyone. **That is [E2-53]'s dominance class demonstrated on filed
  numbers** — *"Once dominant … Good or bad, it will prosper."* The customers did not leave after
  the single worst reputational event available to this industry.

**(3) Not subject to price regulation — IN TODAY, and explicitly contingent, which is recorded
rather than smoothed.** No regime sets S&P's rating fees. But the FY2025 10-K names the proposal
in its own words: laws *"are likely to continue to be considered in the future, including, for
example, provisions seeking to **reduce regulatory and investor reliance on credit ratings** or to
increase competition among credit rating agencies, **provisions regarding remuneration and
rotation of credit rating agencies** … which could increase the costs and legal risks relating to
Ratings' activities, or **adversely affect our ability to compete and/or our remuneration**."*
And **[E2-59] applies in both directions and must be said plainly**: the NRSRO designation is a
**regulatory licence** — *"The SEC first began informally designating NRSROs in 1975 for use of
their credit ratings in the determination of capital charges for registered brokers and
dealers"* — so part of the demand belongs to the regime, and the same filing records that
*"governments may from time to time establish official rating agencies or credit ratings
criteria."* **A regime that created a floor can withdraw it.** This is carried to Q6 as the first
falsifier and is the reason the class below is NARROW rather than WIDE.

### THE COMPETITOR ROW — required **[E3-28]**. *A moat is a claim about relative position.*

**ROW A — UNITS, and it is COMPLETE.** *(the physical series **[E4-55]** asks for, and the best
kind of evidence available anywhere in this register: every competitor, including the private
ones, files a primary SEC document carrying its own count of ratings outstanding.)* Form NRSRO
Item 7A, "approximate number outstanding as of the most recent calendar year end", each taken
from that filer's own annual certification on EDGAR:

| NRSRO | ratings outstanding | share | filing |
|---|---:|---:|---|
| **S&P Global Ratings** (subject) | **1,077,798** | **49.4%** | `0001650548-26-000001`, 2026-03-26, as of 2025-12-31 |
| Moody's Investors Service | 684,055 | 31.3% | `0001193125-26-133970`, 2026-03-31, as of 2025-12-31 |
| Fitch Ratings, Inc. | 266,519 | 12.2% | `0001104659-25-028114`, 2025-03-26, **as of 2024-12-31** |
| DBRS, Inc. (Morningstar) | 73,491 | 3.4% | `0001104659-26-037622`, 2026-03-31 |
| Kroll Bond Rating Agency | 52,055 | 2.4% | `0001214659-26-004046`, 2026-03-30 |
| Egan-Jones Ratings Co | 14,348 | 0.7% | `0001651331-26-000004`, 2026-03-30 |
| A.M. Best Rating Services | 8,385 | 0.4% | `0001631580-26-000001`, 2026-03-27 |
| Japan Credit Rating Agency | 5,361 | 0.2% | `0000873292-26-000001`, 2026-03-26 |
| Demotech, Inc. | 451 | 0.0% | `0001962109-26-000001`, 2026-03-27 |
| HR Ratings LLC | *not extracted* | — | `0001628352-26-000004`, 2026-03-26 |
| **total of the nine that report** | **2,182,463** | | |

- **Peers named: 9 of the industry's 10 real competitors**, and the count of ten is not my
  estimate — it is **every registrant that filed a Form NRSRO annual certification in 2026**,
  enumerated from EDGAR full-text search over form type NRSRO-CE. *(Buffett says eight; the
  industry has ten and I took nine.)*
- **THE TWO THINGS THIS ROW DOES NOT SHOW, stated rather than glossed.** First, **S&P's count is
  85% government and municipal securities** (916,817 of 1,077,798), a class that carries small
  fees, while Moody's mix is more corporate and structured — so S&P is 49.4% of the *units* but
  earns only about 52% of the *revenue* of the S&P/Moody's pair, and the units overstate the
  lead. Second, **Fitch's figure is a year stale**: Fitch left Item 7A blank in its 2026
  certification (accession `0001104659-26-036549`, checked page by page, and there are no
  form-field values in it either), so its number is as of 2024-12-31 and its share is understated
  by a year's growth.
- **Because the row is complete in units, the Ratings moat class is NOT held PROVISIONAL** —
  which is the only reason this gate can be marked IN at all.

**ROW B — SEGMENT OPERATING MARGIN, same metric, same window, from each filer's own statements:**

| | FY2023 | FY2024 | FY2025 | source and construction |
|---|---:|---:|---:|---|
| **S&P Global Ratings** | **55.9%** | **61.9%** | **63.8%** | 10-K MD&A segment table: $1,864M / $2,707M / $3,013M on $3,332M / $4,370M / $4,724M |
| Moody's Investors Service | 51.1% | 57.7% | 60.9% | MCO 10-K segment note: Adjusted Operating Income **less that segment's own D&A and restructuring**, so the basis matches — $1,557M / $2,299M / $2,628M on $3,046M / $3,986M / $4,317M |
| Morningstar (DBRS is inside it, unsegmented) | 11.3% | 21.3% | 21.5% | MORN 10-K; **whole company**, so it is a bound, not a comparator |
| Fitch Ratings | **UNKNOWABLE** | | | Hearst subsidiary. Form NRSRO Exhibit 11 *is* audited financial statements, but **Rule 17g-1(i) exempts it from public disclosure** and Fitch has taken the exemption. No document I can name would resolve it. |
| Kroll · Egan-Jones · A.M. Best · JCR · Demotech · HR | **UNKNOWABLE** | | | all privately held; the same exemption |

**What the UNKNOWABLE cells cost the claim, said plainly:** I cannot show that Fitch is not
profitably undercutting the pair, and Fitch is 12% of the field. What survives that gap is that
**the two filers who do report both raised margin by 5 to 10 points over the same three years**,
which is not what happens when a third player is taking share on price. The class below is held
at NARROW partly for this reason.

**ROW C — THE INDICES LEG, tested and NOT claimed as the franchise.** MSCI's own 10-K
(accession `0001408198-26-000011`) names the field:
> *"Among our Index competitors are **S&P Dow Jones Indices LLC (a joint venture of S&P Global
> Inc. and CME Group Inc.); FTSE Russell, a subsidiary of the London Stock Exchange Group plc;
> Nasdaq Inc; Bloomberg Finance L.P. … and Solactive AG**."* … *"Some asset managers also manage
> funds, including ETFs, based on their proprietary indexes … This is often referred to as
> **self-indexing**."*

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| S&P Dow Jones Indices, EBITDA margin *(segment operating profit + segment D&A) ÷ revenue* | 68.9% | 70.3% | **71.0%** |
| MSCI Index segment, Adjusted EBITDA margin | 76.2% | 76.6% | **76.4%** |

**S&P DJI is the larger index business and the LESS profitable one**, against the one index peer
that reports a comparable segment. Five named competitors plus self-indexing is not *"no close
substitute"*. **FTSE Russell (inside LSEG plc), Bloomberg Finance L.P. and Solactive AG are not
SEC registrants; Bloomberg and Solactive are private and their economics are UNKNOWABLE. LSEG
publishes an annual report and is therefore UNRESEARCHED rather than unknowable — and I did not
pull it, because the Indices leg is not carrying this verdict.** The Indices leg is recorded as
**NARROW and PROVISIONAL** and is explicitly excluded from the gate, exactly as the CL run
excluded Pet Nutrition.

**ROW D — MARKET INTELLIGENCE: criterion (2) is NOT shown, on the subject's own words and on a
rival's.** S&P's 10-K: *"The market for data, analytical capabilities, research services and
software services is **intensely competitive, ranging from established firms to fast evolving
market disruptors**."* Morningstar's 10-K names *"FactSet, MSCI, Preqin (a division of
BlackRock), Refinitiv, **S&P Global Market Intelligence**, and smaller or specialized data
providers"* in one list. The numbers agree with the words: FactSet 32.2% operating margin
(FY2025), Morningstar 21.5%, Market Intelligence **20.2%** — this segment earns *peer* margins,
which is what a non-franchise looks like.

**ROW E — ENERGY: PROVISIONAL, and named as such.** Platts price assessments plausibly meet all
three conditions (41.0% margin, 88% subscription revenue, $11M of segment capex), but **the
nearest competitor, Argus Media, is privately held in the United Kingdom and files nothing**, and
OPIS was sold out of this company in 2022. **PROVISIONAL, therefore not claimed** — and it is
15.2% of continuing profit, so it does not need to be.

### THE OTHER Q2 TESTS, ON RATINGS

- **[E4-04] — must the moat be continuously REBUILT?** No. What is being defended — a
  hundred-year default archive, the NRSRO registration, and the letter's presence in other
  people's mandates — is the same asset each year, not its replacement. The spending defends it
  ([E5-23], [E3-49]); it does not buy a substitute for it. Segment capex **$24M / $29M / $64M**
  in 2023-2025 against segment operating profit of $1,864M / $2,707M / $3,013M. **[E4-04] is not
  engaged.**
- **[E4-23] key-person — no defect found.** The segment has had three heads in five years
  (Berisford to 2021, Cheung, then Cheung's successor when she became CEO in November 2024) and
  its margin rose through every handover. You cannot name the president of S&P Global Ratings,
  and the ratings are still bought — which is the Mayo Clinic test passed.
- **[E3-46] the second question about the business is a number.** Ratings earned **$3,013M on
  $1,137M of total segment assets** in FY2025 — total assets, not net tangible assets, so the
  honest denominator is smaller still. Indices earned $1,271M on $3,378M. Market Intelligence
  earned $991M on **$31,234M**. **The same company contains one of the best returns on capital
  obtainable and one of the largest low-return deployments in this register, reported side by
  side in Note 12.** That is **[E2-56]**'s Pro-Am effect on the face of the filing, and it binds
  Q3.
- **[E2-44] two-characteristic test — one passes, one FAILS, and the failure is recorded.**
  (b) *grow dollar volume with only minor additional investment of capital*: **passes
  overwhelmingly**, on the assets and capex above. (a) *raise prices even when demand is flat and
  capacity is not fully utilised*: **NOT demonstrated.** Ratings revenue fell from **$4,097M
  (2021) to $3,050M (2022) — down 25.6% — and segment margin from 64.2% to 54.8%** when bond
  issuance stopped. The franchise did not hold the annual number; it held the position, and the
  number came back higher. **[E3-55]** is the corpus's own scope for exactly this: where the
  business result is certain and only the yearly figure bounces, the bounce is noise rather than
  width. It is still a Q4 and Q5 fact and it is carried to both.
- **[E4-37] the agony metric — the yawn end, with a caveat.** The FY2024 and FY2025 10-Ks both
  say, without hedging, that revenue *"benefited from **improved contract terms across product
  categories**"*. No prayer session. **The caveat is that the realised rate is flat:** transaction
  revenue ÷ total billed issuance ran **5.61 bp (2023), 5.95 bp (2024), 5.71 bp (2025)**, so the
  price rises land in surveillance and relationship fees rather than in the issuance take, and
  the 2025 fall is mix — low-fee government and structured issuance grew fastest.
- **[E4-32] direction — WIDENING on margin, NARROWING against the direct rival.** Ratings margin
  **57.4% (2019) → 63.8% (2025)**, through a merger, a bond bust and a recovery. But the gap over
  Moody's MIS is **+4.8, +4.2, +2.9 points** across 2023-25. Both facts are carried; the second
  is not rounded away.
- **[E3-33] untapped pricing power — REFUSED OUTRIGHT, under [E5-28].** Claiming that class is
  claiming *"a monopoly or a near monopoly"*. A 49.4% unit share in a field where a direct rival
  earns 60.9% margins on 31.3% of the units is a duopoly, not a near-monopoly.
- **[E4-36] which of the four causes of extreme success?** Not wave-riding: the position predates
  every bond market it now rates, and it survived the destruction of its own reputation. It is
  **an extreme maximum on one variable — third-party adoption of the reference** — which is the
  ownable kind.
- **[E3-61] the row's limit, stated.** The row shows position. It cannot show conduct: two firms
  at 60%-plus margins could behave like a demented Kellogg tomorrow, and the corpus says even
  Munger had no model for predicting which way that goes.

### CLASS AND VERDICT

- Needed or desired **[x]** · no close substitute **[x]** (Ratings) · not price-regulated **[x]**
  (today, contingently)
- **Class: NARROW** — not WIDE, for three stated reasons: a live regulatory contingency on
  remuneration and on regulatory reliance **[E2-59]**; a direct rival at 60.9% margins whose gap
  to the subject is narrowing; and the fact that the franchise is **48.5% of the continuing
  profit** of the company being bought, with the remaining 51.5% split between a narrower index
  business, a provisional energy business, and a data business that earns peer margins.
- **Direction: widening on its own margin, narrowing on its lead over the direct rival.**
- **No leg is marked IN on provisional evidence.** Indices and Energy are PROVISIONAL and are
  excluded from the verdict; Market Intelligence fails criterion (2) and is excluded. The verdict
  is carried by Ratings, whose competitor row is complete in units and — for the only rival that
  publishes them — complete in margins.

**VERDICT: [x] IN** — class **NARROW**, carried by Ratings alone.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**A CORRECTION TO MY OWN STEP 0, made here rather than by editing it (operator rule 6).**
Step 0 said the filing gives "no basis for treating [the 7.2 million Markit EBT shares] as
anything but company-held, treasury-equivalent stock." **That is wrong, and the FY2025 balance
sheet says so:** *"Less: common stock in treasury - at cost: 2025 - **109 million shares**"*
against 415 million issued, which leaves **306.0 million legally outstanding** — and
415 − 109 − 7.2 = **298.8 million**, the exact figure on the FY2025 cover. **The EBT shares are
NOT inside treasury stock; they are outstanding shares that the registrant excludes from its
reported count and from its EPS denominator.** The origin is now sourced too: FY2022 10-K
Note 2, *"Excludes 25,219,470 IHS Markit shares held by the Markit Group Holdings Limited
Employee Benefit Trust … converted in the merger into S&P Global shares at the exchange ratio
of 0.2838 and will continue to be held by the trustee in the EBT"* — 25,219,470 × 0.2838 =
7.16 million. **The headline count stays at the registrant's 294.8M**, because that is the
denominator of its own EPS and the trust is a consolidated company vehicle; **the $2,910M
sensitivity stated in Step 0 stands and is now better grounded, not weaker.**

### STEP 1 — THE WEIGHT CASE. *How much damage can this manager do before I can react?*

- [ ] **Daily execution [E3-38, E2-70]** — **NOT ticked, and the reasoning is on the record
      rather than assumed.** A credit rating is close to *"their only products are promises"*,
      which is the condition that magnifies a manager. But this company ran the experiment:
      **the promises failed catastrophically in 2004-2007, the segment's operating margin fell
      to 6% in FY2014 on the settlements, and the franchise did not move.** That is **[E5-18]**'s
      *"capacity to stand it, if we stumble into it"* demonstrated on filed numbers, which is
      the opposite of a have-to-be-smart-every-day business.
- [ ] **Control [E1-16]** — not ticked. A minority public holding with daily liquidity.
- [ ] **Leverage [E3-29]** — not ticked, and quantified rather than waved: **total debt $13,088M**
      at 2025-12-31 ($718M short-term, $12,370M long-term) against free cash flow of $5,135M —
      **2.5x** — and the only financial covenant is *"a requirement that our indebtedness to cash
      flow ratio … is not greater than 4 to 1, and this ratio has never been exceeded."*

**None ticked → Q3 IS A QUALITATIVE OVERLAY.** Findings are recorded; manager quality alone does
not stop the run, and **[E2-37, E2-38, E3-39] mean it cannot start one either.**

### THE BINARY — honesty **[E5-16]**, each matter dated to when it became PUBLIC

| dated | matter | disposition |
|---|---|---|
| **2015-01-21** | SEC administrative settlements on three CMBS and RMBS matters. **The SEC found violations** of Securities Act §17(a)(1), Exchange Act §15E(c)(3) and Rules 17g-2(a)(2)(iii) and 17g-2(a)(6), **ordered S&P Ratings censured**, and ordered payment of *"a total of $58 million"*, plus $19M to New York and Massachusetts. | *"S&P Ratings neither admitted nor denied the violations found by the SEC and the state attorneys general."* Corporate, not personal. |
| **2015-02-03** | DOJ and nineteen states and the District of Columbia: *"the Company agreed to pay **$687.5 million to the United States as a civil monetary penalty** … and **$687.5 million in aggregate to the States**"*, plus **$125 million to CalPERS**. | *"The settlement agreement contains **no findings of violations of law** by the Company, S&P LLC or S&P Ratings."* |
| **2014-10-28** | Criminal indictments in Trani, Italy against *"several current and former S&P Global Ratings managers and ratings analysts"* and against Standard & Poor's Credit Market Services Europe. **The only individual-conduct matter in the file.** | **ACQUITTED.** *"On March 30, 2017, following trial, the court in Trani issued an oral verdict acquitting each of the individual defendants and Standard & Poor's Credit Market Services Europe of all charges … The prosecutor did not appeal, and the verdict is now final."* |
| **2020-08-07** | Australian class action on pre-crisis CDO ratings. Live; no amount accrued. | open |
| FY2025 10-K | *"S&P Global Ratings is in ongoing communication with the staff of the SEC regarding compliance with its extensive obligations"* — routine NRSRO supervision, no proceeding named. | open, unquantified |
| FY2025 10-K risk factors | *"**We have experienced insider trading incidents involving employees in the past**, and it is not always possible to deter misconduct by employees or third-party vendors."* | disclosed by the company against itself; no individual named; recorded |

**No matter in the file names a current officer or director.** The one matter that reached
individuals ended in acquittal, final, with no appeal. **The 2015 SEC censure is a CORPORATE
finding of violation with no individual accountability identified — the exact question the UMC
run of 2026-09-13 put to the operator and which is still unanswered.** I do not decide it here.
I record that (a) it is eleven years old, (b) it predates every current executive officer, and
(c) **it did not govern this verdict, which closes at Q5 on price for reasons that have nothing
to do with it.**

### STEP 2 — THE FLAGS. *Each is a prompt to READ, never a verdict.*

- [ ] **weak accounting** — not found. Ernst & Young LLP, unqualified opinion on the statements
      and on internal control, one critical audit matter (the redeemable NCI valuation), and
      Item 9 *"Changes in and Disagreements with Accountants … **None**."* **Recorded and not
      scored as a flag: E&Y have served since 1969 — fifty-seven years**, which is a long enough
      tenure to be worth naming under **[E4-34]**'s auditor's-eye test even though nothing in the
      filing turns on it.
- [ ] **unintelligible footnotes** — not found; the opposite. See the candor paragraph.
- [x] **TRUMPETED EARNINGS PROJECTIONS — FIRES.** A full annual guidance table, GAAP and
      adjusted, with a **diluted-EPS range**, restated and re-cut every quarter. FY2026:
      *"Diluted EPS | $16.35 to $16.60 | $17.50 to $17.75"*. Plus *"The Company **now expects to
      repurchase more than $7 billion in shares** in total in 2026."* **[E5-30]** is the reason
      this matters: *"once you start it, it's all over … forecasting earnings, I can't imagine
      anything more destructive."* **Fifty-three consecutive years of dividend increases** is
      named in the release as an achievement, which is the same ratchet in another form.
- [ ] **serial share issuance [E5-15]** — does **not** fire on the promotion test. The count has
      gone the other way since 2022. **But one issuance dwarfs everything else in this file and
      it is judged below under [E5-44], not here.**
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, and the CGNX instruction is what
      found it.** The literal word is absent: **"EBITDA" appears ZERO times in the FY2025 10-K
      and ZERO times in the 2026-07-28 earnings release**, so a run that grepped for the word
      would score this clean. One level down, it fires at full strength:
      - **The pay yardstick is "non-GAAP ICP Adjusted EBITA Margin"** — earnings before interest,
        taxes and **amortization** — one of the two financial metrics funding the annual bonus
        for the CEO, CFO, Chief Accounting Officer and Chief Legal Officer (DEF 14A of
        2026-03-31).
      - **The headline number in every release is adjusted diluted EPS**, and *"The largest
        non-core adjustment to earnings in the second quarter of 2026 was for **deal-related
        amortization**."* Guidance quantifies it: **"Deal-related Amortization | ~$785 million"**
        for FY2026 continuing operations, against pro forma continuing GAAP EPS of $16.35-$16.60
        and adjusted EPS of $17.50-$17.75 — a **7% wedge that is almost entirely amortization of
        intangibles the company issued $43.5bn of stock to acquire.**
      - **[E4-29]'s own mechanism is what makes this the paradigm case**, not a technicality:
        *"Depreciation is where you spend the money first … and record the expense later. And
        it's **reverse float**."* Purchased intangibles are money already spent — in shares, in
        2022 — and the adjusted measure deletes the record of it. **[E2-57]** applies in its own
        words: a standing *"except for"* run every quarter for four years over the single largest
        cost of the single largest decision.
      - **This is carried to Q4 as the (c) question**, not left as a complaint.
- [ ] **filed-figure tells [E4-30]** — **no tell.** Cash taxes paid ÷ pre-tax income:
      **34.8% (2023) · 21.8% (2024) · 24.1% (2025)**, against a reported provision of
      21.2% / 21.5% / 22.6%. Cash taxes are not falling as a share of reported pre-tax income.
      Nor is reported growth unnaturally smooth: revenue fell in no year but **operating profit
      fell 4.8% in 2023 and Ratings' revenue fell 25.6% in 2022**, which is the honest shape of a
      cyclical business rather than a managed line.
- [x] **[E2-49] METRIC-SWITCHING — FIRES, with the mitigation stated.** For 2026 the
      Compensation Committee *"approved an increase to the weighting of non-GAAP ICP Adjusted
      Revenue from 50% to 70% for the financial metrics for both enterprise and divisional bonus
      plans … The weighting of non-GAAP ICP Adjusted EBITA Margin was accordingly adjusted from
      50% to 30%."* **The weight on the margin metric was cut by 40% of itself in the year that
      guided margin expansion fell from ~100 bps (FY2024 guidance) to 35-60 bps (FY2026
      guidance).** That is the classic direction. **The mitigation, which [E2-49] itself names as
      the candor case:** it was announced *ahead* of the period, with a stated reason
      (*"incentivizing profitable growth"*), in the proxy, alongside a second change that cuts
      against self-interest (raising the weight of *enterprise* results in division presidents'
      pay). **Fired, and carried; not scored as venality.**
- [ ] **[E2-52] dividends funded by issuance** — does not fire; there is no net issuance. **The
      adjacent fact is recorded because it is the same arithmetic in a different place:** the
      FY2025 release states the company *"returned $6.2 billion to shareholders in 2025 …
      **This represents 113% of adjusted free cash flow for the year**."* The 13-point excess was
      funded by **$1,549M of disposal proceeds** and **$1,708M of new borrowing** ($715M
      commercial paper plus $993M of notes issued 2025-12-04). Distribution above cash generation,
      sourced from asset sales and debt, against a **stated target of "85% or more"**.
- [ ] **[E3-50] stock-price targeting** — no statement found that the job is to encourage the
      highest price. Not fired.
- [x] **[E5-33] restructuring charges — FIRES on recurrence, not on size.** *"Our 2025 and 2024
      restructuring plans consisted of company-wide workforce reductions of approximately 1,300
      and 1,230 positions"*, charges of **$157M and $125M**, under the heading *"We
      **continuously** evaluate our cost structure."* An annual event is an operating cost.
      **Action taken: they stay inside the owner-earnings mean** at Q4 — which they do
      automatically, because they are cash costs already inside operating cash flow, and **no
      restructuring add-back is made.**

### STEP 3 — THE PRIMARY TEST **[E2-01]**, scoped by **[E2-43]**

**The reported series first.** Net income attributable to S&P Global ÷ year-end controlling
equity:

| | FY2021 *(pre-merger)* | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|
| net income attributable to SPGI | $3,024M | $2,626M | $3,852M | $4,471M |
| controlling equity, year end | **$2,032M** | $34,200M | $33,159M | $31,127M |
| **return on equity** | **≈149%** | **7.7%** | **11.6%** | **14.4%** |

**That table is the whole of Q3 in four columns, and [E2-43] is what makes it readable.** The
corpus says that for an acquisitive filer the denominator is **unleveraged net tangible assets**,
with the goodwill wedge reported separately and never hidden inside book equity. Do it:

- **Goodwill $36,475M + other intangibles $16,271M = $52,746M — which is 169% of the $31,127M of
  book equity.** Book equity is not the capital in the business; it is the price paid for
  acquisitions, less the buybacks since.
- **Net tangible OPERATING assets are NEGATIVE, at about −$2.2bn.** Operating assets excluding
  cash, goodwill and intangibles (receivables $3,441M, prepaid $858M, PP&E net $278M, right-of-use
  $413M, equity investments $603M, other non-current $610M and the pension asset $254M) come to
  about **$6,457M**; non-debt operating liabilities (payables $610M, accrued compensation $988M,
  income taxes payable $180M, **unearned revenue $4,088M**, other current $1,010M, non-current
  lease $494M, pension $178M, other non-current $1,107M) come to about **$8,655M**.
- **So the operating business requires no net tangible capital at all — its customers fund it,
  through $4,088M of unearned revenue — and the return on operating capital is not a finite
  number.** Total property and equipment, gross, for a $15.3bn-revenue company, is **$1,139M**.

**The consequence, and it is the finding that organises the rest of Q3: the [E2-01] question
answers itself as "infinite on the operations, and 14.4% on the price paid for acquisitions."
The 14.4% is a verdict on the capital allocation, not on the business.** Pre-merger the same
operations earned about 149% on book. This is exactly what **[E2-73]** separates: what the
managers of the units earn on the underlying assets, against what was paid for the business.

### RATIONALITY IS CAPITAL ALLOCATION — and here it is nearly the whole question

**1. THE IHS MARKIT MERGER — $43.5 BILLION OF STOCK, closed 2022-02-28.** FY2022 10-K Note 2:
*"The estimated fair value of the consideration transferred for IHS Markit was approximately
**$43.5 billion** as of the merger date"*, at an exchange ratio of 0.2838, **entirely in shares**.
Shares outstanding went **241.0 million (2021-12-31) → 321.9 million (2022-12-31), +33.6%**, and
total assets **$15,026M → $61,784M**. It is larger than the whole company that made it.

**[E5-44] governs and is quoted in full because it is the test:** *"The intrinsic value of the
shares you give in an acquisition **must not be greater than the intrinsic value of the business
you receive** … measure the acquirer's paper at IV, not at quote."*

**What was received, traced through to today, from the filings:**

| what happened to the acquired perimeter | evidence |
|---|---|
| regulator-mandated divestitures during 2022 (CUSIP Global Services, OPIS, Base Chemicals, Leveraged Commentary & Data) | FY2022 cash-flow statement: *"Proceeds from dispositions | 3,509"*, with a **$1,898M** gain |
| Engineering Solutions sold **2023-05-02** | FY2023 10-K; inside that year's $1,014M of disposal proceeds |
| **Mobility spun off 2026-07-01** | S&P kept *"the net cash distribution … of **$1.974 billion**"*; shareholders received MBGL shares, worth about **$5.9bn** at MBGL's **$19.925** quote on 2026-09-18 (aggregator, flagged) on roughly 296M shares |
| retained | the IHS Markit portions of Market Intelligence and Energy |

**What the retained part earns, on the same segment definitions before and after:**

| | FY2021 revenue | FY2021 operating profit | FY2025 revenue | FY2025 operating profit | change in operating profit |
|---|---:|---:|---:|---:|---:|
| Market Intelligence | $2,185M | $676M | $4,916M | $991M | **+$315M** |
| Energy *(Platts in 2021)* | $1,012M | $544M | $2,299M | $943M | **+$399M** |
| Mobility *(wholly acquired)* | — | — | $1,747M | $378M | +$378M, **now distributed** |

**About $714M of additional pre-tax segment profit is retained from a $43.5bn payment in
shares**, alongside roughly $3.5bn of 2022 divestiture proceeds, the Engineering Solutions
proceeds, $1.974bn of cash from Mobility, and MBGL stock now worth about $5.9bn.

**THE HUMILITY CLAUSE, APPLIED PROPERLY [E4-13], AND THE LIMIT OF THIS TEST.** I am **not**
computing a destruction figure and I do not claim one. Part of the Market Intelligence and Energy
increase is organic and would have happened without the deal; part of the deal's value was cost
synergy realised inside those segments; and **the counterfactual — what the legacy company would
have earned alone — is unknowable.** What is *observable* and what I do record is this: **the
largest capital allocation in the company's history bought the two segments that earn the lowest
returns on the largest assets, and within four years a quarter of what it bought had been sold or
distributed away.** Market Intelligence carries **$31,234M of total assets and earns $991M**;
Ratings carries **$1,137M and earns $3,013M.**

**2. [E2-56] THE PRO-AM EFFECT, and this is the sharpest Q3 finding in the file.** *"Their
marvelous core businesses … camouflage repeated failures in capital allocation elsewhere."* The
consolidated 42.2% operating margin and 14.4% ROE are the **average** of a business earning 265%
on its segment assets and a business earning 3.2% on its segment assets, reported side by side in
one table of one note. **Judge the retention segment by segment, incrementally, never on the
blend** — which is what the row above does.

**3. [E4-39] THE RARE-POSITIVE TELL — SEARCHED FOR AND NOT FOUND.** *"A candid acquisition
post-mortem is almost never witnessed."* No filing on this company's docket revisits the IHS
Markit merger against its announcement case — not the 10-Ks, not the releases, not the proxies.
**What the company did instead was spin off a quarter of what it bought**, which is a verdict
delivered by action without one delivered in words. The same absence the CL run recorded.

**4. BUYBACKS — THE TWO CONDITIONS [E5-08], AND THE THIRD [E4-31].**
- **(1) ample funds for operations and liquidity — YES.** $5,135M of free cash flow in 2025,
  $1,745M of cash, a $2.0bn undrawn facility, debt maturities of $3M in 2026 and $1.7bn in 2027,
  and a 4:1 covenant *"never exceeded"*.
- **(3) shareholders supplied the information needed to estimate value [E4-31] — YES, to an
  unusually high standard.** The segment note gives revenue, operating profit, D&A, capex **and
  total assets** by segment; the billed-issuance table gives the physical driver of half the
  profit; the Indices table gives operating profit **and** net operating profit after the
  minority; and the Article 11 pro forma of the post-spin company was filed **five days** after
  the spin.
- **(2) a MATERIAL DISCOUNT to conservatively calculated intrinsic value — FAILS ON THE PRICE
  RECORD. CAPITAL-ALLOCATION FLAG.** Item 5 of the FY2025 10-K:
  **Q4 2025 repurchases averaged $514.16 a share** (October $513.68, November $497.02, December
  $521.73), $5,001M for the full year, with *"more than $7 billion"* planned for 2026 against a
  market capitalisation of $119.1bn. **Today's quote is $404.11.** Adding back the whole MBGL
  distribution at $19.93 gives a spin-adjusted **$424.04 — still 17.5% below the average Q4 2025
  repurchase price.** Buying 10% of the company in two years at prices the market has since
  marked down by a sixth is not, on its face, buying at a material discount.
- **THE HUMILITY CLAUSE IS MANDATORY HERE AND IS NOT A FORMALITY [E4-13, E5-08].** This rests on
  **our own** valuation range, which Q5 has not yet produced, and on a quote rather than on value;
  *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole lot
  more about them than I do"*, and *"many CEOs never stop believing their stock is cheap."*
  **The flag binds POSITION SIZE and nothing else. It does not enter the discount rate.**

**5. [E2-30] THE INSTITUTIONAL IMPERATIVE — all four, scored.**
- [ ] **resists any change in current direction** — **NOT fired, and the opposite is arguably
      true.** Four perimeter changes in five years. If there is a fault here it is restlessness.
- [x] **projects or acquisitions materialise to soak up available funds** — **FIRED, and it is
      the largest item in the file.** $43.5bn in 2022; then With Intelligence (November 2025),
      Visible Alpha (May 2024), World Hydrogen Leaders (May 2024), Market Scan (February 2023);
      **$2,023M of acquisitions in FY2025 alone**, against $195M of capital expenditure.
- [ ] **staff studies produced to justify the leader's craving** — **not scoreable from
      filings.** Recorded as unobservable rather than scored clean.
- [x] **peer behaviour mindlessly imitated** — **FIRED as a prompt, not as a verdict.** The
      merger landed inside the same three-year window as LSEG/Refinitiv and ICE/Ellie Mae; the
      financial-data roll-up was the whole industry's strategy at once. **[E2-30]**'s own last
      clause governs: *"Institutional dynamics, not venality or stupidity."*

**6. INCENTIVES — [E4-27], and read the plan, not the slogan** (DEF 14A filed 2026-03-31,
accession `0001104659-26-037380`):
- Short-term incentive **funded at 108.68% of target** for 2025; the **2023-2025 PSU award vested
  at 182.23% of target** — the ULTA shape, and worth stating because the same plan caps at 200%.
- Bonus financial metrics: **non-GAAP ICP Adjusted Revenue** and **non-GAAP ICP Adjusted EBITA
  Margin**, equally weighted in 2025, re-weighted 70/30 for 2026.
- **PSUs are 70% of the long-term award and vest on a three-year cumulative non-GAAP ICP
  Adjusted EPS goal.**
- **NOTHING IN THE PAY PLAN IS A RETURN ON CAPITAL** — which is the number **[E2-01]** and
  **[E3-46]** make the test, in a company whose two largest segments earn **265%** and **3.2%** on
  their own assets. The same finding the CL run made, in a place where it matters more.
- **And the EPS metric is mechanically moved by the buyback the same executives size.** Diluted
  shares fell 3% year on year in Q2 2026 and *"more than $7 billion"* of repurchase is planned for
  2026. A material share of the pay metric is **purchased rather than earned**, and the
  amortization the metric excludes is the cost of the acquisitions that the revenue metric
  rewards. **Read together, the plan pays for buying revenue with stock and for buying the share
  count back with cash, and is silent on the return earned on either.**
- CEO **Martina Cheung**, 2025 total compensation **$12,831,062**, against a median employee at
  **$40,158** — **320 to 1**. The median is low because 26,200 of 44,500 employees are in Asia;
  the ratio is reported as the company reports it and is not interpreted further.

### CANDOR — THE HALF-OWNER TEST **[E2-26]**

**Passes, on an unusually high standard, with one clean exception.**
*Passes:* the segment note reports revenue, operating profit, D&A, capital expenditure **and
total assets** for every segment, which is what let this run take the business apart; the
**billed-issuance table** publishes the physical driver of the Ratings cycle and the company has
just begun publishing it **monthly**; the Indices table shows operating profit **and** the net
figure after the noncontrolling partners, so a reader is not left to find the $322M himself; the
FY2014 10-K set out the settlement amounts payee by payee; the Article 11 pro forma arrived five
days after the spin; and *"revenue also benefited from improved contract terms"* is a company
telling you it raised prices.
*The exception, and it is [E2-57] exactly:* a standing **"except for"** of roughly **$1.1bn a
year** of deal amortization, run every quarter since 2022, carried into guidance, and built into
the pay plan — over the single largest cost of the single largest decision this management has
made.

### THE GUARDRAIL — checked before the verdict

- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** Every finding above is
      either neutral or negative. **[E2-37, E2-38, E3-39]**.
- [x] **This business does not require a great manager**, and that was recorded at Q2 as a moat
      *strength* under **[E4-23]**, not here as a compliment to anyone.
- [x] No great manager is the reason to act. **[E2-35, E2-36]** is not engaged: there is no
      excisable cancer and no Pygmalion on offer.

**VERDICT: [x] IN** — *as the absence of found disqualifiers, not a finding that the managers are
honest; "sincerity and empathy can easily be faked" **[E5-17]**, and "Charlie and I would not have
spotted it."* **IN never promotes.**

**Four findings carried forward, and two of them bind later sections:**
1. **[E4-29] fires on substance** — ~$785M a year of deal amortization deleted from the headline
   measure and from the pay metric. **This binds Q4: it is the (c) question, and Q4 must answer
   it rather than inherit management's answer.**
2. **[E5-08](2) fails on the price record** — $5.0bn repurchased in 2025 at an average of about
   $514 against a spin-adjusted $424 today. **This binds POSITION SIZE at Q6, never the rate.**
3. **[E2-56]/[E2-73]**: 149% on book before the merger, 14.4% after; 265% on Ratings' segment
   assets against 3.2% on Market Intelligence's. The blend is not the number.
4. **[E2-49] fired with its mitigation**, and **[E4-39]** found nothing — no acquisition
   post-mortem exists on this docket.

---
## Q4 — WILL IT SURVIVE?

### THE SKIP REASON, TESTED ON THE FILING RATHER THAN INHERITED

**The queue's wave-5 label for SPGI is "capex unresolved [E5-20]: build (c) by hand from the
filing."** Both halves were tested.

**(a) The label is a TOOLING ARTEFACT — the AMZN and CL kind, not the NVDA kind.** The XBRL tag
changed: `PaymentsToAcquirePropertyPlantAndEquipment` carries 10-K years **FY2007-FY2009 only**
(229.6 / 106.0 / 68.5) and stops; `PaymentsToAcquireProductiveAssets` carries **FY2008-FY2025**
unbroken. A reader following only the first tag sees S&P Global's capital spending end in 2009,
which is what `floor_screen.py` at `a8bc84f` did. **The union fix reaches every window — there is
NO early-year hole of the NVDA kind**, and the two tags overlap in FY2008-FY2009 rather than
leaving a gap.
**I ran it through the CURRENT `owner_earnings()` as the queue's dated notes instruct.** It
prices: `{'5y_da': 3115.0, '5y_capex': 3935.0, '3y_da': 3633.7, '3y_capex': 4644.7}` ($M). The
capex end is the *higher* one here, because capex is a small fraction of D&A — the reverse of the
usual shape, and the reason is purchase amortization.
**And the capex line never left the face of the statement:** *"Capital expenditures | ( 195 ) |
( 124 ) | ( 143 )"*, FY2025 10-K. **`da_annual()`'s defect found by the NVDA run does not bite
here**, because S&P Global reports *Depreciation* and *Amortization of intangibles* as two
separate lines and no combined total exists on the face to be replaced: 110 + 1,069 = 1,179, and
the tool returns 1,179.

**(b) THE D&A DISCONTINUITY IS THE MERGER, confirmed on the filing.** `da_discontinuity_flag()`
fires at 2022-12-31 (5.7x, $178M to $1,013M) and names three possible causes. **It is the first
one.** The filed statements show *Amortization of intangibles* at $96M (FY2021), **$905M
(FY2022)**, $1,042M, $1,077M, $1,069M, while *Depreciation* alone runs $82M / $108M / $101M /
$96M / $110M. The IHS Markit merger closed 2022-02-28 for $43.5bn, of which the FY2022 critical
audit matter identifies *"identified intangible assets of $18.6 billion"*. **Purchase accounting,
not a change of estimate and not a tag artefact.**

**(c) [E5-20] ASKED SEPARATELY, ON THE FILING, AND ANSWERED: NO.** S&P Global is not in the
capital-intensive exception class, and it is about as far from a railroad as a filer gets:
- **Total property and equipment, gross, is $1,139M** on $15,336M of revenue; **net $278M**.
  All long-lived assets *"including right of use assets, property and equipment, net and
  capitalized technology costs, net"* are **$873M**.
- **Capital expenditure has run 0.5% to 1.3% of revenue** for nine years.
- **Capex against depreciation, 2020-2025: $662M against $580M — 1.14x.** That is precisely
  **[E2-41]**'s *"capital expenditures that over time roughly approximate depreciation"* and
  **[E3-44]**'s default case. On continuing operations 2023-25 the ratio is higher, **$394M
  against $271M = 1.45x**, and both numbers are trivial.
- **[E4-47]'s inflation condition is NOT engaged** the way it was at Colgate: 61% of revenue is
  United States and *"We do not have operations in any foreign country that represent more than
  7% of our consolidated revenue"*, so there is no old-dollars depreciation problem.

**So the real (c) question here is not plant at all, and the label pointed at the wrong thing.**
The whole of the D&A band is **amortization of purchased intangibles**, and the question is
whether **buying companies** is what this business requires to fully maintain its position.
**Of the four names now run from this row: ABNB had a real presentation gap, AMZN had no gap,
NVDA had a tag gap plus a history gap, CL had a tag gap only — and SPGI has a tag gap only, with
a second question underneath it that the label does not describe.**

### OWNER EARNINGS — THE ONE NUMBER **[E2-23]**

**Built by hand from the filed cash-flow statements (`_research 2026-09-18 SPGI/oe.py`); never a
net-income proxy.** Construction, and every departure from the standing CONVENTION is disclosed:

> **owner earnings = cash provided by operating activities − stock-based compensation − (c)
> − distributions to noncontrolling interest holders**

- **The working-capital increment [E2-23] constraint 3 is inside operating cash flow**, from one
  audited line, as the CONVENTION provides.
- **THE ONE ADDITION TO THE CONVENTION, and it is correctness rather than conservatism: the
  distributions to noncontrolling interest holders are deducted** — $280M / $287M / $321M in
  2023-25, off the face of the financing section. **CME Group holds 27% of S&P Dow Jones
  Indices** and took **$322M of FY2025's $1,271M of Indices operating profit**; that cash is
  inside consolidated operating cash flow and never reaches an S&P Global shareholder. **[E3-04]**
  requires the look-through *addition* of undistributed investee earnings so the yield is not
  understated; the mirror case — a consolidated subsidiary with an outside owner — requires the
  *subtraction*, or the yield is overstated. The company's own free-cash-flow definition deducts
  the same line. **The figures without this deduction are shown too** (section D below), so the
  reader can see exactly what it costs: about $296M a year, or 7.8% of the mean.

**A. THE PERIMETER BEING PRICED — continuing operations, ex-Mobility, FY2023-FY2025 ($M)**

| year | continuing OCF | SBC | continuing capex | continuing D&A | NCI distributions | **OE, (c)=capex** | OE, (c)=D&A | OE, wc movement stripped |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2023 | 3,145 | 171 | 121 | 832 | 280 | **2,573** | 1,862 | 3,033 |
| 2024 | 5,092 | 247 | 106 | 858 | 287 | **4,452** | 3,700 | 4,217 |
| 2025 | 5,030 | 236 | 167 | 862 | 321 | **4,306** | 3,611 | 4,738 |
| **3-yr mean** | | | | | | **$3,777M** | **$3,058M** | $3,996M |

*Mobility is removed using the FILED Article 11 pro forma's discontinued-operations column
(operating profit $317M / $374M / $373M, plus its own D&A of $311M / $315M / $317M, less its own
tax of $63M / $92M / $69M) and its segment capital expenditure of $22M / $18M / $28M from Note 12.
**Two disclosed approximations, stated because they matter:** (i) Mobility's own working-capital
movement is not separately given, so the split of the consolidated working-capital line is
approximate; (ii) Mobility's SBC is left inside continuing, which overstates continuing operating
cash flow by roughly $26M while the full consolidated SBC deduction over-deducts by the same
amount — **the two cancel to within a rounding error** and neither is a judgment.*

**The CL instruction applied: reported with and without the working-capital movement.** Here it
runs the opposite way to Colgate's. Stripping the movement **raises** the mean from $3,777M to
$3,996M, because working capital was a **use** of cash in two of three years (−$460M in 2023,
+$235M in 2024, −$432M in 2025). **The as-filed figure is therefore the conservative one and it is
the one used.** The component worth naming: unearned revenue rose $352M / $222M / $327M — real
customer prepayment — while **receivables absorbed $291M / $79M / $600M, and days sales
outstanding rose from 74 to 82 in 2025.** That eight-day move is a Q6 monitoring item.
**`working_capital_flag()` returns `None`** — no single line moved more than 30% of a year's
operating cash — and I checked its stated annual-facts limitation against the 10-Qs rather than
trusting the null: H1 2026 operating cash was $2,476M against $2,398M a year earlier, with no
single line above $403M.

**B. THE [E2-42] FIVE-YEAR DEFAULT, FY2021-FY2025, consolidated AS FILED ($M)** — *published
because [E4-38] requires every window, and labelled because it measures a company that no longer
exists: it crosses the 2022-02-28 merger and it contains Mobility throughout.*

| 2021 | 2022 | 2023 | 2024 | 2025 | **5-yr mean** |
|---:|---:|---:|---:|---:|---:|
| 3,214 | 2,030 | 3,116 | 5,031 | 4,899 | **$3,658M**, (c) = capex |
| 3,071 | 1,106 | 2,116 | 3,982 | 3,915 | **$2,838M**, (c) = D&A |

**C. THE PRE-MERGER REFERENCE, FY2017-FY2021, legacy S&P Global on ONE perimeter ($M)**

| 2017 | 2018 | 2019 | 2020 | 2021 | **5-yr mean** |
|---:|---:|---:|---:|---:|---:|
| 1,683 | 1,703 | 2,440 | 3,207 | 3,214 | **$2,449M**, (c) = capex |

**D. WITHOUT the NCI deduction** (the bare CONVENTION), continuing 2023-25: 2,853 / 4,739 / 4,627,
mean **$4,073M**. The deduction costs $296M a year.

**E. TRAILING TWELVE MONTHS to 2026-06-30, continuing** (10-Q `0000064040-26-000045`):
consolidated OCF $5,729M, capex $156M, SBC $239M, NCI distributions $315M; Mobility removed at
$610M and $28M. **OE = $4,437M.** *A single twelve months, not a mean; it is an upper reference,
never the number.*

### (c) — THE DISCLOSED JUDGMENT, because Buffett says it must be a guess

**(c) is set at TOTAL CAPITAL EXPENDITURE.** Three grounds, all from the filing:
1. **Capex here is not just plant.** The MD&A's own definition: *"Capital expenditures include
   purchases of property and equipment **and additions to technology projects**."* The capitalised
   product development is already inside the number, which is what **[E2-23]**'s *"plant and
   equipment, **etc.**"* reaches for in a business like this one.
2. **Capex exceeds depreciation** (1.14x over 2020-25 consolidated, 1.45x over 2023-25
   continuing), so taking capex rather than depreciation is the conservative end on the plant.
3. **The D&A end is invalid in the opposite direction from the usual one.** Continuing D&A of
   $862M is $96M of depreciation and **$766M of amortization of intangibles bought in 2022**.
   Deducting it as (c) asserts that the whole purchased intangible base must be repurchased
   every eleven years to stand still. That is an assertion about acquisitions, not about plant,
   and it deserves to be tested rather than assumed.

**SO THE REAL QUESTION IS TESTED SEPARATELY: IS BUYING COMPANIES A MAINTENANCE REQUIREMENT?**

*Evidence that it is NOT (and this is where I land):*
- **The company's own organic disclosure.** FY2026 guidance: *"Organic, Constant Currency Revenue
  growth | 6.0% to 8.0%"* against reported revenue growth of *"5.9% to 7.9%"*. **Organic growth is
  guided at or above reported growth** — the position is not being held by purchase.
- **84% of continuing profit is earned by segments that buy essentially nothing.** FY2025
  amortization of intangibles from acquisitions by segment: **Ratings $6M, Indices $37M, Energy
  $130M** — $173M of the $766M. The remaining ~$593M sits in Market Intelligence.
- **The reference assets are not purchased and do not amortize.** The letter, the index and the
  assessment were built, not bought, and carry no intangible balance.

*Evidence that it IS, for the Market Intelligence leg, and it is real:*
- **$2,023M of acquisitions in FY2025** against $195M of capital expenditure, and Market
  Intelligence's revenue growth is repeatedly attributed to purchases — *"favorably impacted by
  the acquisition of Visible Alpha in May of 2024 and With Intelligence in November of 2025"*.

**THE RANGE, WHICH IS WHAT [E4-25] ASKS FOR RATHER THAN A RESOLUTION.** If the Market
Intelligence acquisition programme is maintenance rather than growth, (c) rises by the
acquisition run-rate and owner earnings fall:

| construction of (c) | 3-yr mean owner earnings |
|---|---:|
| total capital expenditure **(the judgment used)** | **$3,777M** |
| capex + the 2023-24 acquisition rate (~$300M/yr) | $3,477M |
| capex + the 3-yr mean acquisition spend (296 + 305 + 2,023)/3 = $875M/yr | **$2,902M** |
| continuing D&A (the mechanical D&A end) | **$3,058M** |

**Two independent routes to the low end land within $156M of each other — $2,902M and $3,058M —
which is the useful fact.** The combined range carried to Q5 is therefore **roughly $3,050M to
$3,800M**, with the trailing twelve months at $4,437M as an upper reference and the five-year
as-filed window at $3,658M sitting inside it on a different perimeter.

**Is that range too wide to reach a conclusion [E4-25]?** **No** — and it is worth saying why,
because the honest answer could have been yes. Top to bottom the range is 24%, and **every point
in it produces the same Q5 answer** (see Q5: the widest and narrowest constructions are 2.6% and
3.7% against a 5.29% sovereign). The range would only matter if it straddled the verdict, and it
does not.

**Stock compensation subtracted in full [E5-06]**: $171M / $247M / $236M, from the filed non-cash
block. **THE BA SBC CHECKLIST, RUN LINE BY LINE ON THE FILED BLOCK** — *"Depreciation",
"Amortization of intangibles", "Provision for losses on accounts receivable", "Deferred income
taxes", "Stock-based compensation", "(Gain) loss on dispositions, net", "Restructuring, lease
impairment charges and other"* — **there is no second equity-settled line.** The 401(k) and
retirement contributions are inside *"Accrued compensation and contributions to retirement
plans"* on the balance sheet and are cash; the pension is a $254M **asset**, overfunded, with
$178M of other post-retirement liability. **[E3-70]'s market-value measure is not applied and the
reason is stated:** SBC is **4.2% to 4.6% of operating cash flow** across 2023-25, so the gap between the charge and a grant-date market value cannot move any verdict here; the
reported charge is used as the floor it is. *(SBC ÷ consolidated operating cash flow: 4.6% in
2023, 4.3% in 2024, 4.2% in 2025.)*

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

**[x] GREAT — at the segment level, and the corporate-level qualification is stated rather than
buried.**

*Why great:* net tangible **operating** assets are **negative** (about −$2.2bn; see Q3), so growth
requires no incremental capital in the operations at all. FY2025 continuing owner earnings of
$4,306M were produced on $167M of capital expenditure and gross plant of $1,139M. It is
**[E2-44](b)** — *"grow dollar volume with only minor additional investment of capital"* — in its
purest available form, and **[E5-41]**'s inversion runs the right way: customers prepay $4,088M
of unearned revenue, so this is float rather than reverse float.

*The qualification, and it is [E2-56] again:* at the **corporate** level the growth was bought.
Owner earnings per diluted share, on comparable perimeters:

| | FY2017 | FY2019 | FY2021 *(legacy, no Mobility, no IHS Markit)* | FY2023 | FY2024 | FY2025 *(continuing, no Mobility)* |
|---|---:|---:|---:|---:|---:|---:|
| owner earnings, $M | 1,683 | 2,440 | **3,214** | 2,573 | 4,452 | **4,306** |
| diluted shares, M | 258.9 | 246.9 | **241.8** | 318.9 | 311.9 | **305.1** |
| **OE per diluted share** | $6.50 | $9.88 | **$13.29** | $8.07 | $14.27 | **$14.11** |

**Read the two bold columns together.** Both are the company without Mobility. **Four years and
$43.5 billion of stock after the merger, owner earnings per share is $14.11 against $13.29 — a
total gain of 6.2%, or about 1.5% a year.** Dollars of owner earnings rose 34%; the share count
rose 26%.
**The fair caveats, stated because the comparison is doing a lot of work:** FY2021 capital
expenditure was abnormally low at $35M (normalising it to $100M gives $13.02 a share, which does
not change the conclusion); and FY2021 was a strong issuance year while FY2023 was a weak one.
**The cleaner rate, mid-cycle to boom, is FY2019 to FY2025 continuing: $9.88 to $14.11, +6.1% a
year** — and because it runs from a mid-cycle year *to* a boom year, the underlying rate is
**below** 6.1%. That is the growth number Q5 uses, and it is used at face value rather than
shaded, so that the windage stays spent once.

### STAYING POWER — score all three **[E5-11]**

**(1) A large and reliable stream of earnings — PASS, comfortably.** Operating cash flow has not
been below **$2,016M** in nine filed years and never negative; **79% of FY2025 revenue was
recognised over time** ($12,192M of $15,336M); unearned revenue of $4,088M is next year's revenue
already collected. Even in FY2022, the worst year in the window — merger costs, divestiture taxes
and a bond-market shutdown together — operating cash flow was $2,603M.

**(2) MASSIVE LIQUID ASSETS — FAIL, and it is recorded rather than argued around.** Cash was
**$1,745M at 2025-12-31** against **$13,088M of total debt**; the pro forma post-spin balance
sheet shows **$3,663M** at 2026-03-31 after the $1.974bn Mobility distribution, and the company
has announced it will spend *"more than $7 billion"* on repurchases in 2026. The filing points at
a facility rather than at cash: *"We have the ability to borrow a total of $2.0 billion through
our commercial paper program, **which is supported by our $2.0 billion five-year credit
agreement**"*, with **$825 million of commercial paper outstanding at 2026-06-30**. Commercial
paper is exactly **[E5-39]**'s *kindness of strangers* — it is the funding that disappears in the
week you need it. **Scored FAIL, on the same reading the CL run gave Colgate.**

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASS, with one named exception the filing
itself declines to schedule.** Debt matures **$3M in 2026, $1.7bn in 2027, $784M in 2028, $2.7bn
in 2029, $596M in 2030 and $6.5bn thereafter**, against $5.1bn of annual free cash flow; the fair
value of the debt is **$11.3bn against $13.1bn of book**, so the fixed coupons are worth less than
par at today's rates. The AWS commitment is *"a purchase obligation of $1.0 billion … over a
five-year period"*. **The exception:**
> *"after December 31, 2017, **CME Group and CME Group Index Services LLC ('CGIS') has the right
> at any time to sell, and we are obligated to buy, at least 20% of their share in S&P Dow Jones
> Indices LLC**. **We have excluded this amount from our contractual obligations table** because
> we are uncertain as to the timing and the ultimate amount of the potential payment we may be
> required to make."*

**A $4,914M put, exercisable at the counterparty's option at any time, deliberately left out of
the obligations table.** That is [E5-11]'s third strength in its literal form — *"Ignoring that
last necessity is what usually leads companies to experience unexpected problems"* — and the
filing says, in terms, that it is ignoring it. It is **affordable** (one year's free cash flow,
and the minimum tranche is nearer $1.0bn), which is why this is a pass rather than a fail; but it
is exercisable in exactly the market where S&P's own cash flow would be weakest, and **[E2-55]**
says score the worst case.

**[E5-11] SCORES 2 OF 3.**

**[E2-54] the coverage test:** interest paid in FY2025 was **$390M** against operating cash flow
of $5,651M **net of ample capital expenditure** ($195M) — **14.0x**. Accrued interest is not
material beyond the paid figure. **Leverage, named and quantified [E4-16, E3-29]:** total debt
$13,088M, 2.5x free cash flow; net debt post-spin about $9.7bn; the single financial covenant is
*"indebtedness to cash flow … not greater than 4 to 1, and this ratio has never been exceeded."*
**[E3-52]'s question — read the terms, not the quantity:** $4,088M of unearned revenue is
covenant-free, due-date-free, customer-prepaid funding; $13.1bn of senior notes are long-dated
and unsecured with no maintenance covenants named beyond the facility's.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**Not insolvency. The mechanism is the withdrawal of the requirement to hold the letter.**

**The bear case, stated as well as its holders would state it [E4-51].** S&P Global Ratings does
not sell information; information about credit is free and getting freer. It sells **admission**.
An issuer buys the letter because other people's documents demand it — a pension fund's mandate,
a bank's capital calculation, an insurer's reserve rules, an index's eligibility screen. **None of
those documents is written by S&P Global, and the largest author of them is the state.** The
FY2025 10-K concedes the exposure in its own words: legislators continue to consider *"provisions
seeking to **reduce regulatory and investor reliance on credit ratings**"*, *"provisions regarding
**remuneration** and rotation of credit rating agencies"*, and governments *"may from time to time
establish **official rating agencies**"*. **[E2-59]** is exact about what class that puts the
business in: a regime can floor a business's profits, *"but that day is gone"* is how such
arrangements end, and the moat belongs to the regime rather than to the firm. Meanwhile the
borrowing itself is migrating: the fastest-growing part of corporate credit is private and
bilateral, where the lender does its own work and buys no letter at all — the 10-K lists *"private
market opportunities"* as a Ratings *growth* initiative, which is the company conceding that the
public-issuance base is not where the growth is.

**Quantified from filed figures.** Ratings is **$3,013M of $6,218M** of continuing segment
operating profit, on **$4,724M of revenue** of which **$2,470M is transaction** (tied to new
issuance) and **$2,254M non-transaction** (tied to the stock of ratings outstanding). The
incremental margin on rating fees is close to 100% — the segment's assets are $1,137M and its
capital expenditure is $64M — so revenue lost is profit lost almost dollar for dollar.
- **Scenario 1, fee compression from mandated remuneration rules or a third rating becoming
  standard: −20% of Ratings revenue = −$945M of operating profit, −15.2% of continuing segment
  profit.** Owner earnings fall from about $3,777M to about $3,050M, and the yield at today's
  price from 3.17% to 2.56%.
- **Scenario 2, the deeper one — a 30% reduction in the *stock* of rated debt over a decade as
  reliance is withdrawn and private credit takes share: −30% of both revenue legs = −$1,417M**,
  **−22.8% of continuing segment profit**; owner earnings fall to about **$2,690M** and the yield
  to **2.26%**.
- **Scenario 3, the one the balance sheet feels: Market Intelligence's data products are
  commoditised by general-purpose AI.** That segment carries **$31,234M of total assets** earning
  **$991M**. A write-down to the value of its cash earnings would be a non-cash charge in the
  order of **$20-26bn — 17% to 22% of today's market capitalisation** — alongside the loss of 16%
  of continuing profit. The 10-K names this exposure five separate times in its own risk factors.

**LIKELIHOOD: [x] a real possibility** for Scenario 1 within five years (it is already drafted
legislation in the European Union and the United Kingdom), **[ ] a low-level possibility** for
Scenario 2 within a decade, **[x] a real possibility** for Scenario 3 within a decade. **None of
them is insolvency**, and that is the point: this business does not die of a balance sheet. It
dies, if it dies, of somebody else deleting a sentence from a document.

**[E4-40] — exposure, not experience.** The temptation here is to read the 2015 stress test as
proof of immortality: the franchise took a $1.5bn hit for the worst ratings failure imaginable and
came back stronger. **That is experience.** The *exposure* is different in kind — 2015 was a
reputational failure in a regime that still required the letter. None of the three scenarios above
is a reputational failure; all three are the removal of the requirement. **A benign history of
surviving reputational disasters is "not only useless, but actually dangerous" as a guide to
surviving a regulatory one.**

**VERDICT: [x] IN** — the business survives. It has nine years of never-negative operating cash
flow, negative operating capital requirements, 14x interest coverage and no maturity wall. What
it does not have is massive liquid assets, and what it carries is a $4.9bn put it has excluded
from its own obligations table.

---
⛔ **Q5 opens because Q1, Q2, Q3 and Q4 each returned IN.** The hard sequence (operator rule 2)
is satisfied and this section is **REPORTABLE, not a computation.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**The pair, struck today and used for every figure below:** price **US$404.11**, the
**2026-09-17** close (`tools/sources.py:price('SPGI')`, aggregator, flagged) × **294,800,000
shares** (10-Q cover for the quarter ended 2026-06-30, accession `0000064040-26-000045`, as of
2026-07-24) × split factor **1.0** = **market capitalisation US$119,131.6M**. Sovereign **USD
30-year 5.29%**, US Treasury daily par yield curve, the issuing authority, **09/17/2026**.

### THE FLOOR, BEFORE THE RANKING **[E4-28, E3-13]**

**Honest pre-tax expectancy at this price, on every construction Q4 produced:**

| window | owner earnings | yield | multiple | vs the 5.29% sovereign | **expectancy, + 6.1% growth** |
|---|---:|---:|---:|---:|---:|
| **3-yr continuing mean, (c) = capex — the central construction** | **$3,777M** | **3.17%** | **31.5x** | **−2.12 pts** | **9.27%** |
| 3-yr continuing mean, (c) = capex + the 2023-24 acquisition rate | $3,477M | 2.92% | 34.3x | −2.37 | 9.02% |
| 3-yr continuing mean, (c) = continuing D&A | $3,058M | 2.57% | 39.0x | −2.72 | 8.67% |
| 3-yr continuing mean, (c) = capex + the 3-yr acquisition rate | $2,902M | 2.44% | 41.1x | −2.85 | 8.54% |
| 5-yr 2021-25 as filed *(a different company)* | $3,658M | 3.07% | 32.6x | −2.22 | 9.17% |
| FY2025 continuing alone | $4,306M | 3.61% | 27.7x | −1.68 | 9.71% |
| **TTM to 2026-06-30, continuing — a single year, the upper reference** | **$4,437M** | **3.72%** | **26.8x** | **−1.57** | **9.82%** |

**FLOOR VERDICT: FAIL. Honest pre-tax expectancy is 8.5% to 9.8% against the ~10% floor — below
it on EVERY construction, including the single best twelve months this company has ever filed.**
On the central construction it is **9.27%, short of the floor by 0.73 points.** *"that's the
figure we quit on"* **[E4-28]** — *"true whether short rates are 6 percent or whether short rates
are 1 percent."* **The name is not ranked. It is quit on.**

**And it fails the second test too, which the floor makes redundant but which [E4-15] asks for
anyway: on the bare yield the business pays 2.44% to 3.72% against a government bond at 5.29% —
between 1.6 and 2.9 points BELOW the sovereign on every window.**

*One comparability caveat, stated once and not used to move anything: owner earnings are after
corporate tax and the Treasury yield is before the holder's tax. The same construction was used
at CL, BRK-B and every other gate-clearer in this register, so the comparison is consistent
within the file even though it is not exact.*

### THE THREE THINGS THE FRAMEWORK ASKS FOR

**1. THE YIELD.** Owner earnings **$3,777M** ÷ market cap **$119,131.6M** = **3.17%**, against a
sovereign of **5.29%**.

**2. WHAT THE PRICE ALREADY ASSUMES.** To reach the ~10% floor from a 3.17% yield the business
must compound owner earnings at **6.83% a year in perpetuity**; on the trailing twelve months,
**6.28%**. Merely to match the government bond it must compound at **2.12%**.
**What the business has actually done: +6.1% a year in owner earnings per diluted share, FY2019
to FY2025 on the continuing perimeter** ($9.88 to $14.11) — **and that rate runs from a mid-cycle
issuance year TO a boom year**, so the underlying rate is below it. On the comparable ex-Mobility
perimeters four years apart, FY2021 to FY2025, it is **1.5% a year**.
**So the price requires slightly more than the best measured rate, forever, and appreciably more
than the four-year rate across the merger.**
**[E4-35] is NOT the binding constraint and is not misapplied here** — 6.83% is not a 15% claim
and the twenty-year base rate is not what fails this. **[E4-44] and [E2-63] are the binding ones,
and the ceiling is nameable:** the operations already run on **negative net tangible capital**, so
the return on operating capital cannot usefully rise; all of the required growth must come from
price and volume in four businesses of which one is a duopoly in a regulated activity, one is
losing a margin race to MSCI, one is provisional, and one earns peer margins.

**3. WHAT YOU ARE PAID.** **Minus 2.12 points against the sovereign** on the central construction
(minus 1.57 at the very best, minus 2.85 at the worst). There is no positive spread at this price
on any window built from any perimeter.

### WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE **[E3-42]**

- Sovereign used **5.29%** — **the bare rate. No per-name premium is added**, and none of the
  Q2/Q3/Q4 findings has been allowed near it.
- Certainty is handled twice and neither place is the rate: at the understanding gate (Q1 IN) and
  in the discount to value demanded at the end. It is priced **once** and is not stacked
  **[E4-11, E4-48]**.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**

Solving for the price at which expectancy equals the ~10% floor, cap = OE ÷ (0.10 − g):

| owner earnings | g = 3.0% | g = 4.0% | g = 5.0% | g = 6.1% *(the full realised rate, granted)* |
|---|---:|---:|---:|---:|
| $3,058M (D&A end) | $148 | $173 | $207 | $266 |
| **$3,777M (central)** | **$183** | **$214** | **$256** | **$329** |
| $4,437M (TTM, a single year) | $215 | $251 | $301 | **$386** |

**Value, in round numbers: roughly $185 to $330 a share** on the central construction, **widening
to roughly $150 to $385 only if the D&A end and the trailing twelve months are taken as the two
ends of one range and the full 6.1% growth is granted at the top.**
**Current price: $404.11. The price is ABOVE THE WHOLE RANGE on every construction.**
*(For reference against the bond alone, ignoring the floor: the price at which the owner-earnings
yield equals 5.29% is $196 on the D&A end, $242 on the central construction and $285 on the
trailing twelve months.)*

**A cross-check that does not depend on my construction at all.** The company's own FY2026
guidance for continuing operations is **GAAP diluted EPS of $16.35 to $16.60**. At $404.11 that is
**24.5x this year's guided GAAP earnings**, on a business the same guidance says will grow revenue
5.9% to 7.9%. My owner-earnings figure per share ($12.81 on the three-year mean, $14.84 on the
trailing twelve months) sits below guided GAAP EPS mainly because of the $296M-a-year
noncontrolling-interest deduction and because the mean includes 2023. **The two routes disagree
about the level and agree about the answer.**

### WHICH BAR — and the windage count

- [ ] **Normal method [E4-11]** — **NOT USED.** An end margin is not applied, and the reason is
      that it would be meaningless: the price is already above the undiscounted range. Applying a
      margin to a failed floor would be theatre.
- [x] **Screamer test [E4-01]** — the conservative end of the range is **$150-$185** and the price
      is **$404.11**. Of the three outcomes, this is the third: **price above the whole range →
      NO.** Not *"inside the range, no useful conclusion"* — above it.
- **WINDAGE COUNT: ONE, and it is small.** The single conservative choice is **(c) at total
  capital expenditure rather than depreciation**, worth about $41M a year on the continuing
  perimeter. Everything else is a realistic input: the noncontrolling-interest deduction is
  correctness (that cash does not reach the holder), the as-filed working-capital figure is the
  filed number rather than a shaded one, **and the 6.1% growth rate is granted at face value even
  though it runs from a mid-cycle year to a boom year.** **[E4-41]'s normalisation for luck is
  satisfied by the WINDOW rather than by a second deduction** — the three-year mean already
  contains the 2023 issuance bust alongside the 2024-25 boom (billed issuance $2,539bn, $3,911bn,
  $4,327bn), so deducting a cycle allowance on top would be spending conservatism twice. *(For the
  record, the size of that allowance if anyone wants it: at the three-year mean level of issuance
  and the three-year mean realised rate, FY2025 transaction revenue would have been $2,068M rather
  than $2,470M — about $310M of owner earnings after tax.)*

**VERDICT: [x] FAIL — below the ~10% floor [E4-28]. Not ranked; quit on. Watch-list only.**
*This is the ASML, PNR and CL shape — a finding about the PRICE, not about the business. All four
business gates returned IN.*

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*Recorded and pre-committed **[E1-02]**, "prior to the act". Nothing is owned; these are the terms
on which the file would be reopened.*

**Thesis-confirming metric:** S&P Global Ratings' **share of credit ratings outstanding** across
the nine reporting NRSROs (Form NRSRO Item 7A, filed every March), currently **49.4%**, together
with the **Ratings segment operating margin** (63.8%) and its gap over Moody's MIS (+2.9 points
and narrowing).

**Thesis-breaking metrics and their thresholds — five on the business [E4-17], three on
management, two on survival:**

*Q2 (the franchise):*
1. **Any enacted law or rule in the United States, the European Union or the United Kingdom that
   regulates credit-rating REMUNERATION, mandates rotation, or removes a regulatory reference to
   ratings.** The 10-K names all three as under consideration. **This is the [E2-59] trigger and
   it voids the Q2 verdict outright**, because it is the condition on which criterion (3) was
   passed.
2. **Ratings-outstanding share below 45%** (from 49.4%), or Moody's MIS passing S&P on the
   absolute count — read each March off the two Form NRSRO certifications.
3. **Ratings segment operating margin below Moody's MIS's for two consecutive years.** The gap
   has run +4.8, +4.2, **+2.9** across 2023-25.
4. **Transaction revenue ÷ total billed issuance below 5.0 bp for two consecutive years** (5.61,
   5.95, **5.71** bp). This is **[E4-37]**'s agony metric in numbers, and it has just become
   monthly: *"Beginning with January 2026 data, the Company expects to release its monthly billed
   issuance data … on the 15th of each month."*
5. **Indices: S&P DJI's EBITDA margin falling more than 8 points behind MSCI's Index segment**
   (5.4 points in 2025), **or ETF assets tracking S&P indices falling in two consecutive years**
   (ending ETF AUM $4.389tn in 2024, **$5.480tn in 2025**).

*Q3 (management):*
6. **Any single acquisition above $5bn**, or acquisition spending above $2bn in two consecutive
   years. FY2025 was $2,023M.
7. **Repurchases continuing above $330 a share** — the top of the value range — through a second
   full year. The 2026 programme is *"more than $7 billion"*.
8. **The 2028 proxy still containing no return-on-capital metric**, or the adjusted-EPS PSU
   weighting rising above 70%.

*Q4 (survival):*
9. **CME exercising the S&P Dow Jones Indices put** (an 8-K under item 1.01 or 2.01). $4,914M,
   excluded from the contractual-obligations table.
10. **Cash below $1.5bn at a quarter end with more than $1.5bn of commercial paper outstanding.**
    At 2026-06-30: $4,141M and $825M.

**Next catalyst dates, in order:**
- **Q3 2026 results, late October 2026** — **the first filing that presents Mobility as
  discontinued operations and reallocates the stranded corporate costs.** It is the first clean
  read of the company being priced, and it will test the pro forma this run relied on.
- **The FY2026 10-K, February 2027** — re-derive every band from it.
- **Form NRSRO annual certifications, March 2027** — the units row, including Fitch's, which was
  left blank this year.

**The sell rule [E2-28]** — not engaged; nothing is owned. **No PERMANENT designation is made**
and none could be: **[E2-39]** requires it in writing in advance of ownership.

**The monitoring question [E4-17, E3-30]:** the erosion to watch is not cyclical. Ratings revenue
falling with issuance is an **aberrational cycle** and 2022 proved it — down 25.6%, back to a new
high in three years. The thing that would **permanently reduce intrinsic value** is item 1 above,
and it arrives as a statute rather than as a bad quarter.

**POSITION SIZE: ZERO.** The file fails at Q5 on price. **And the sizing is pre-committed for the
case where it ever clears: SIZED DOWN, because the [E5-08](2) capital-allocation flag is live** —
$5.0bn repurchased in 2025 at an average of about $514 against a spin-adjusted $424 today, with
more than $7bn planned for 2026. **[E4-13]**'s humility clause governs that judgment and the flag
binds size, never the rate.

**VERDICT: [x] IN** *(recorded; the file is closed at Q5 and this section governs only the
conditions for reopening it.)*

---
## THE OUTPUT CONTRACT

**PRICE: US$404.11** (2026-09-17 close; 294,800,000 shares; market capitalisation
**US$119,131.6M**).

**FAIL — the file is closed at Q5, ON PRICE.** Q1 IN · Q2 IN (NARROW, carried by Ratings alone) ·
Q3 IN (qualitative overlay) · Q4 IN · **Q5 FAIL: honest pre-tax expectancy of 8.5% to 9.8%
against the ~10% floor [E4-28], and an owner-earnings yield 1.6 to 2.9 points BELOW the 5.29%
sovereign on every window.** Q6 recorded, and it governs only the conditions for reopening.

**All four business gates cleared. This is a finding about the price, not about the business** —
the ASML, PNR and CL shape.

---
## SELF-AUDIT

- [x] **Questions answered in order; no verdict skipped.** Q5 opened only after Q1-Q4 each showed
      IN, and the file says so at the gate.
- [x] **NO HARD-SEQUENCE VIOLATION, and I audited for one rather than assuming it.** The file was
      searched before folding for valuation language appearing before line 1174 (where Q5 starts).
      Four hits, all inspected: two are the **verbatim text of [E5-44]**, quoted because it is the
      Q3 test for a stock-funded acquisition; one is the **heading of [E5-08]'s second
      condition**, which the template requires at Q3; one is the **humility clause of [E5-08]**
      itself (*"many CEOs never stop believing their stock is cheap"*). **None is an output about
      SPGI's value.** The Q3 buyback paragraph states in terms that it *"rests on our own
      valuation range, which Q5 has not yet produced"*, and compares the repurchase price to
      today's quote — a price-to-price comparison, not a valuation. **No value range, no yield and
      no multiple for this company appears anywhere before Q5.** *(The CL run found two violations
      in a killed session's draft; this session was not killed and none was imported.)*
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2 is IN on
      Ratings, whose competitor row is **complete in units** (nine of ten NRSROs, each from its
      own primary SEC filing). The **PROVISIONAL** legs — Indices and Energy — are named as such
      and are **explicitly excluded from the verdict**, exactly as CL excluded Pet Nutrition.
- [x] **Every UNKNOWABLE names what specifically cannot be known.** Fitch Ratings' income
      statement (Form NRSRO Exhibit 11 is audited financials but Rule 17g-1(i) exempts it from
      publication, and Fitch has taken the exemption); the economics of Kroll, Egan-Jones, A.M.
      Best, JCR, Demotech and HR Ratings (same exemption); Bloomberg Finance L.P. and Solactive AG
      (private, no filing exists); **Argus Media** (private, United Kingdom), which is why Energy
      is PROVISIONAL.
- [x] **Every UNRESEARCHED names the artifact and where it lives.** One only: **LSEG plc's annual
      report**, for FTSE Russell's economics. It is a nameable document on LSEG's investor site
      and it was **not pulled**, because the Indices leg does not carry the verdict. Recorded as
      UNRESEARCHED rather than dressed up as unknowable.
- [x] **Step 0: the filing was read, with accession numbers, and figures were cross-checked.**
      FY2025 10-K `0000064040-26-000013`; OCF $5,651M and capex $195M both matched to the dollar
      against the filed Consolidated Statement of Cash Flows.
- [x] **Owner earnings on a multi-year mean, windows stated, capex band disclosed as a judgment.**
      Three perimeters, never blended; four constructions of (c), two of which land within $156M
      of each other.
- [x] **Competitor row filled.** Nine of ten NRSROs in units; S&P and Moody's in margins on the
      same basis and the same window; MSCI's Index segment for the Indices leg; FactSet and
      Morningstar for Market Intelligence.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated** — USD 5.29%,
      US Treasury daily par yield curve, 09/17/2026, cache deleted and re-fetched this morning.
- [x] **Value stated as a round-number range**, not a point estimate.
- [x] **One bar chosen, not both** (Bar 2, the screamer test; Bar 1's end margin deliberately not
      applied and the reason given). **Windage count: ONE**, stated.
- [x] **Prices dated; the aggregator flagged and used for live quotes only.** SPGI $404.11 at the
      2026-09-17 close; MBGL $19.925 at 2026-09-18, both flagged.
- [x] **Run committed to git**, section by section, with a pathspec on every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record

1. **My own Step 0 error, corrected in a dated note at the head of Q3 rather than by editing**
   (operator rule 6): I wrote that the filing gave "no basis" for treating the 7.2M Markit EBT
   shares as other than treasury-equivalent. The FY2025 balance sheet disproves it — 415M issued
   less **109M of treasury** less 7.2M is exactly the 298.8M on the cover, so the EBT shares are
   **outstanding shares the registrant excludes from its own denominator**, not treasury. The
   headline count and the $2,910M sensitivity both stand; the reasoning behind them is now right.
2. **Fitch Ratings left Item 7A blank in its 2026 Form NRSRO certification** (`0001104659-26-036549`).
   I checked page by page with two different extractors and for form-field values before falling
   back to the 2025 certification, so Fitch's count in the competitor row is **as of 2024-12-31**
   and its share is understated by a year. Said in the row rather than hidden.
3. **HR Ratings LLC's Item 7A did not extract** from its 2026 certification and I did not chase
   it. It is the smallest of the ten and cannot move a 49.4% share. Recorded as incomplete.
4. **The SEC's Annual Report on NRSROs returned HTTP 403** on three plausible paths from this
   harness. Not needed — the per-filer Form NRSRO certifications are the primary source and are
   better.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN

1. **The brief sent me to the wrong documents for the perimeter, and named the right one as
   merely "unread".** It pointed at the May 2026 8.01 filings for a segment recast and at the
   MBGL Form 10-12B/A for the subtraction. **The answer is the 8-K/A of 2026-07-06, accession
   `0001104659-26-080571`**, which carries an **Article 11 unaudited pro forma income statement
   for FY2023, FY2024, FY2025 and Q1 2026, and a pro forma balance sheet** — S&P Global without
   Mobility, filed, five days after the spin. It is also a **better** source than the Form 10,
   because the Form 10's combined statements charge Mobility with allocated corporate overhead
   that stays with S&P Global, while the pro forma's discontinued-operations column is scoped to
   what actually leaves and says so in note (a).
2. **The brief's share-count instruction stopped one step short.** It correctly warned about the
   ERIC trap (issued vs outstanding — present here, and worth 120M shares) and told me to read
   the 10-Q cover. The cover contains a **second** trap running the other way that the brief did
   not name: it excludes **7.2 million shares it itself calls outstanding**, held by an employee
   benefit trust inherited from Markit. Worth $2,910M of market capitalisation.
3. **The brief's framing of the skip reason pointed at the wrong quantity.** "capex unresolved
   [E5-20]: build (c) by hand" is true as far as it goes, and the tag-change hypothesis was right.
   But **plant is not the (c) question at this company** — gross property and equipment is
   $1,139M on $15.3bn of revenue and capex is 1.14x depreciation. The (c) question is whether
   **acquisition** is maintenance, which the [E5-20] label does not describe and which needed a
   different test.
4. **A small factual slip: the brief said `PaymentsToAcquirePropertyPlantAndEquipment` runs
   "FY2007, 2008, 2009 only … then stops" and `PaymentsToAcquireProductiveAssets` runs "FY2008
   through FY2025".** Both true — but the brief then framed this as a possible hole. **The two
   tags OVERLAP in FY2008-FY2009**, so there is no hole anywhere in the nineteen-year series, and
   the union fix reaches every window. Worth stating because the NVDA run's failure mode was
   exactly a hole.
5. **The brief's expectation that Forms 4 would be available to cross-check the quote did not
   hold.** EDGAR, re-queried this morning, shows **nothing filed after 2026-08-04**. The CL
   trick could not be repeated and the limit is recorded instead of worked around.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN

**Form NRSRO is a complete competitor row for an industry with private participants.** Every
nationally recognised statistical rating organisation — including Fitch, which is inside Hearst,
and Kroll, and A.M. Best — files an annual certification on EDGAR carrying **its own count of
credit ratings outstanding by class**. An EDGAR full-text search over form type **NRSRO-CE**
enumerates the whole industry: **exactly ten registrants in 2026.** This is the first name in the
register whose competitor row is complete in units *including the private competitors*, and the
pattern generalises to any SEC-registered-intermediary industry (broker-dealers, transfer agents,
municipal advisors, security-based swap dealers) where registration carries a disclosure exhibit.

---
## REGISTER

- Verdict: **[x] FAIL AT Q5 — about the PRICE.** Not OUT (the business cleared all four gates),
  not UNRESEARCHED, not UNKNOWABLE.
- **One line:** *S&P Global's ratings franchise is real and measurable — 49.4% of every credit
  rating outstanding in the United States regulatory system, a 63.8% segment margin against
  Moody's 60.9%, and a balance sheet that needs no capital because customers prepay — but the
  price asks 31.5 times a three-year mean of owner earnings for a business that has added 1.5% a
  year per share since it issued $43.5 billion of stock, and the expectancy is 9.27% against a
  10% floor and 3.17% against a 5.29% bond.*
- **Not UNRESEARCHED and not UNKNOWABLE:** every number that decides this file is on a filed
  statement, and the one document not pulled (LSEG's annual report) bears on a leg that does not
  carry any verdict.
