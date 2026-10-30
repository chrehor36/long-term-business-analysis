# Company Run — KB HOME (KBH) — 2026-09-21
**Wave 7, name 14. Register entry 146** (145 entries counted in the slice from the
`## COMPLETED FROM THE QUEUE` heading line to `## THE WRITE-EARLY PROTOCOL`; the heading
string itself occurs 21 times in that file, which is the USAR fold trap, so the slice was
taken by index and the entries counted with a line-start `^- \*\*` regex).
**Unattended overnight cycle. No operator available; every judgment made here and recorded.**
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
- rate **5.34 %** · date **2026-09-18** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year constant maturity**, file
  `daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve`, downloaded
  2026-09-21 and saved to `Test Runs/_research 2026-09-21 KBH/treasury_daily_par_yield_2026.csv`.
  **Struck fresh, not inherited from the brief.** 2026-09-18 is the newest row in the file (a
  Friday; the 2026-09-21 curve had not posted when this run fetched it). Neighbouring rows, so
  the reader can see how much the rate moves: 09/17 5.29, 09/16 5.35, 09/15 5.36, 09/14 5.34.
  **FRED DGS30 was not used and was not needed.**
- FX if the quote and the earnings differ in currency: **n/a — KB Home builds and sells homes
  in nine US states and reports in USD.** No foreign operations, so **[E3-66]**'s
  where-do-shareholders-stand-in-the-queue test is not engaged.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K, FY ended 2025-11-30, filed 2026-01-23, accession 0000795266-26-000017**
    (`kbh-20251130.htm`) — the primary document.
  - **10-Q, quarter ended 2026-05-31, filed 2026-07-09, accession 0000795266-26-000063**
    (`kbh-20260531.htm`) — the newest periodic.
  - **8-K / EX-99.1 earnings release, 2026-06-23, accession 0000795266-26-000060**
    (`exh991kbh-earningsrelease0.htm`) — pulled BEFORE Q3 was scored, per the CGNX standing
    instruction.
  - **DEF 14A, filed 2026-03-13, accession 0001308179-26-000068.**
  - **10-K, FY ended 2019-11-30, filed 2020-01-24, accession 0000795266-20-000007** — pulled
    to resolve the `da_note`, and it did resolve it. See Q4.
- figure cross-checked against the filed statement: **net cash provided by operating
  activities, FY2025.** The XBRL tag `NetCashProvidedByUsedInOperatingActivities` returns
  $335.7M; the filed CONSOLIDATED STATEMENTS OF CASH FLOWS reads **`335,682`** (in
  thousands). Match. Two more checked in passing: D&A **`37,303`** and stock-based
  compensation **`46,238`**, both agreeing with the tagged series.

### THE NEWEST-FILING COLUMN IS A REPORT DATE — the APOG tooling defect, confirmed again
The screen row says `newest_filing: 2025-11-30`. That is the **report date of the FY2025
10-K**, not a filing date. From `submissions.json` the true newest filing is a **Form 4 of
2026-08-07**, and the newest *periodic* is the **10-Q of 2026-07-09**. **No Q3 filing (quarter
ended 2026-08-31) exists as of 2026-09-21** — checked on EDGAR rather than assumed either way:
the recent-filings array ends at 2026-08-07. So the newest public operating read is the
2026-06-23 EX-99.1, and **the Q3 print is imminent and is not in this file.** Any reader
returning to this run after late September 2026 has a document I did not have.

### THE CAP, STRUCK BY HAND — and what the cap_flag actually showed
**Operator rule 4. The flag was not inherited; it was tested.**

| input | value | source |
|---|---|---|
| close | **$47.12** | 2026-09-18, Yahoo Finance chart API — **AGGREGATOR, FLAGGED**, live quote only; raw JSON saved to `price_KBH_yahoo_raw.json` |
| shares outstanding | **61,309,728** | **cover page of the 10-Q for the quarter ended 2026-05-31**, accession **0000795266-26-000063**: "There were 61,309,728 shares of the registrant's common stock, par value $1.00 per share, outstanding on May 31, 2026." |
| splits after the measurement date | **none** — the split-events query returns null and KBH has not split since before 2017 | |
| **cap = close x shares** | **$2,888.9M, call it $2,890M** | |

**The flag said: "A cap cannot be smaller than a subset of itself. One of the two is wrong."
It is wrong, and this run can show it by exact arithmetic rather than by argument.**

- The filed float is **$3,510,028,491** as of **2025-05-31** (10-K cover, accession
  0000795266-26-000017).
- Shares outstanding on **2025-05-31** were **68,050,184** (cover of the 10-Q for that
  quarter, accession 0000795266-25-000081).
- KBH's close on **2025-05-30**, the last trading day before that date, was **$51.58**.
- **68,050,184 x $51.58 = $3,510,028,491.** To the dollar.

So the "float" KB Home files is simply **every outstanding share priced at the May 2025
close** — the registrant reports no meaningful affiliate holding. The filed float is not a
subset of any later cap; it is **the whole market capitalisation on a date fifteen months
earlier**. The screen's $3,217M and the filing's $3,510M are both correct and are eleven
months apart, and the hand-struck $2,890M is correct on a third date. **Nothing is wrong.
This is the sixth consecutive firing of the flag and the sixth consecutive time its stated
conclusion has been false.** Its real content, once decoded, is a fact about the price and
the buyback: KB Home's market value is down **17.7%** from its May-2025 level, of which
**9.9 percentage points** is price ($51.58 to $47.12) and the remainder is the **6.74 million
shares retired** in between.

**RECOMMENDATION FOR THE TOOLING, recorded and not acted on** (operator rule 8 — a tool may
not conclude): the check should compare the filed float **against a cap struck on the float's
own as-of date**. It currently compares two different dates and reports the difference as an
error. Three of the four inputs it needs — cover float, cover share count, cover as-of date —
are already in the document it parses.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** KB Home buys parcels of land in
  49 major markets across nine states, pays to get water, sewer, roads and grading into them,
  puts a house on each lot using subcontracted trades, and sells the house to a retail buyer.
  In FY2025 it sold **12,902** houses at an average of **$481,400**, took **$6.21 billion** of
  housing revenue, and kept **18.6%** of that as gross profit after land and construction.
  Selling and overhead took **10.4%** of revenue, leaving an **8.2%** homebuilding operating
  margin. A second, small segment collects title and insurance commissions and an equity share
  of a mortgage joint venture (KBHS) that financed **85%** of its buyers; in FY2025 financial
  services contributed **$47.1M** of pretax income against **$507.1M** from homebuilding.
  *(FY2025 10-K MD&A, accession 0000795266-26-000017.)*
  **In one line: it is a land-inventory business with a construction service attached.** The
  money is the spread between what a finished house sells for and what the dirt plus the
  sticks cost, and the capital is not plant — it is **$5.67 billion of land and half-built
  houses** on the balance sheet, **85% of total assets** ($5,670.8M of $6,680.3M at
  2025-11-30). That single fact governs everything at Q4: for this business, **inventory is
  the capital account**, and it runs through operating cash flow.
- **The scarce input this business controls:** **entitled, developed lots in specific
  submarkets** — and the filing says plainly that it does *not* control them, it competes for
  them: *"We compete for homebuyers, construction resources and desirable land against
  numerous homebuilders"* (FY2025 10-K, Item 1, Competition). KB Home owns or has under
  contract **59,106 lots** (10-Q, 2026-05-31), of which about **62% owned, 38% under
  contract**. It controls nothing else in the chain: the trades are subcontracted, the
  materials are in its own words *"standardized materials that are commercially available on
  competitive terms from a variety of outside sources"* (FY2025 10-K), and the buyer's
  mortgage comes from a joint venture it does not consolidate.
- **Will the fundamentals look broadly the same in ten years?** **Yes.** Americans will still
  buy detached houses in Phoenix, Dallas and Jacksonville; the sequence land, entitlement,
  development, construction, sale has not changed in seventy years, and KB Home says it has
  *"built over 700,000 quality homes in our nearly 70-year history"* (EX-99.1, 2026-06-23).
  This is **[E3-31]**'s *"relatively simple and stable in character"*. What is **not** stable
  is the *level* of activity and price — but that is a cyclicality finding for Q4 and Q5, not
  an understanding failure. **[E5-29]** is explicit that *"Volatility is far from synonymous
  with risk"*, and **[E3-55]** that a business whose mechanism is certain may have a very
  bouncy annual figure without that being a defect in the analysis.
- **[E4-46] check — is this a five-minute business or a five-month one?** Five minutes. There
  is no technology to forecast, no reserve estimate to take on trust, no regulated rate base.
  The one genuinely hard judgment, land-value impairment, is disclosed on its own line
  (*"Inventory impairments and land option contract abandonments"*, $32.1M in FY2025) and is
  therefore visible rather than buried.
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**This is the question that closes the file.** The evidence is the filer's own 10-K and nine
builders' filed ten-year records. Nothing here rests on general reasoning about housing.

### The three criteria, run one at a time

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."
> — **[E3-03]**, 1991 letter

- **(1) Needed or desired — [x] YES.** Shelter is the archetype of a desired product, and
  KB Home has delivered *"over 700,000 quality homes in our nearly 70-year history"*
  (EX-99.1, 2026-06-23). No argument here.
- **(2) No close substitute — [ ] NO, and the filer says so itself.** FY2025 10-K, Item 1,
  "Competition" (accession 0000795266-26-000017):

  > *"We **also compete for homebuyers against housing alternatives to new homes, including
  > resale homes, apartments, single-family rentals and other rental housing.**"*

  That is a list of four substitute categories, written by the company. And it is not a
  boilerplate concession it ignores in practice — **the whole of its 2025 selling strategy is
  built on pricing against one of them**:

  > *"we have implemented a simplified sales strategy focused on providing a straightforward,
  > transparent base price, with limited, if any, concessions or incentives, that is intended
  > to offer to our customers **a compelling value competitive with area resale home
  > prices**."* — FY2025 10-K, Item 1

  A business whose stated method of selling is to price competitively against the second-hand
  version of its own product does not meet *"thought by its customers to have no close
  substitute."* The same paragraph also settles what KB Home competes on:

  > *"As to homebuyers, we **primarily compete with other homebuilders on the basis of selling
  > price**, community location and amenities, availability of financing options, home designs,
  > reputation, build time, and the design choices and options that can be included in a home."*

  **Selling price is named first, by the filer, among the factors that decide the sale.**
- **(3) Not subject to price regulation — [x] TRUE.** Home prices are not administered.
  But **[E2-59]** is what governs here, and it is about *costs and prices being administered*,
  not about the absence of regulation being a virtue: profit troubles *"may be escaped, true,
  if prices or costs are administered in some manner and thereby insulated at least partially
  from normal market forces."* Nothing administers a house price. Passing (3) is not evidence
  of a moat; it removes a disqualifier. *(The line "regulation caps a franchise and floors a
  commodity business; neither creates the class" is **THE FRAMEWORK v4's own commentary**, not
  a corpus quotation, and is not quoted here as one — PRIME RULE 1.)* **Criterion 2 has already failed, and
  [E3-03] requires all three.**

### The commodity doctrine, and the one exception it allows

> *"persistent over-capacity without administered prices (or costs) equals poor
> profitability"* … long-run profitability set by *"the ratio of supply-tight to supply-ample
> years"* … the one exception is *"a cost advantage that is both **wide and sustainable** … By
> definition such exceptions are few."* — **[E2-58]**, 1982 letter

Homebuilding is the textbook of the class: an undifferentiated physical product, thousands of
producers (KB Home's own text runs *"from regional and national firms … to small local
enterprises"*), no administered prices, and a supply-tight/supply-ample cycle whose two ends
are visible in this very company's filed record (FY2008 net loss of $976.1M; FY2022 net income
of $816.7M). **So the whole Q2 case for KB Home reduces to the single exception [E2-58]
allows: does KB Home have a cost advantage that is wide and sustainable?** That is a
*relative* claim, and it is exactly what the competitor row is for.

### THE COMPETITOR ROW — required **[E3-28]**

**Metric chosen, and why.** **[E3-46]** is explicit about which number answers the
second question about a business: *"the best businesses, by definition, are going to be
businesses that earn **very high returns on capital employed over time**."* For nine builders
running the same product through the same cycle, **return on equity** is the comparable
figure, and because leverage differs across the group I ran the leverage-neutral **return on
assets** beside it rather than leaving the obvious objection unanswered. Ten fiscal years,
2016 through 2025, every figure from the filer's own 10-K XBRL company-facts, fiscal
year-ends mapped to the calendar year in which the year predominantly falls.

**Peers taken: eight.** D.R. Horton, Lennar, PulteGroup, NVR, Toll Brothers, Meritage,
M/I Homes, Century Communities. *(Buffett says eight **[E3-28]**; the industry has more, and
the eight were chosen to span the shape of it — the two giants, the land-light outlier, three
mid-caps, one luxury builder and one small entry-level builder — so the row cannot be accused
of picking flattering or unflattering company. Fiscal calendars: KBH and LEN end 30 Nov,
DHI 30 Sep, TOL 31 Oct, the rest 31 Dec. All map cleanly to a calendar year and the row says
which.)*

**RETURN ON EQUITY — net income / average stockholders' equity, %**

| Company | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **10y mean** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **KB HOME (subject)** | 6.2 | 9.9 | 8.5 | 12.0 | 11.7 | 19.9 | 24.5 | 15.8 | 16.6 | 10.8 | **13.6** |
| NVR | 33.4 | 36.9 | 46.7 | 42.3 | 33.1 | 40.5 | 53.0 | 40.4 | 39.2 | 33.2 | **39.9** |
| PulteGroup | 12.8 | 10.1 | 22.8 | 19.8 | 23.4 | 27.7 | 31.9 | 27.0 | 27.4 | 17.7 | **22.1** |
| D.R. Horton | 14.0 | 14.3 | 17.5 | 17.0 | 21.7 | 31.2 | 34.2 | 22.5 | 19.8 | 14.5 | **20.7** |
| M/I Homes | 9.1 | 10.3 | 13.4 | 13.7 | 21.2 | 27.5 | 26.6 | 20.3 | 20.7 | 13.2 | **17.6** |
| Meritage | 11.2 | 9.6 | 13.8 | 13.5 | 19.6 | 27.4 | 28.4 | 17.3 | 16.1 | 8.8 | **16.5** |
| Toll Brothers | 9.0 | 12.2 | 16.1 | 12.0 | 9.0 | 16.4 | 22.8 | 21.4 | 21.7 | 16.9 | **15.8** |
| Century Communities | 11.2 | 8.3 | 12.1 | 11.8 | 17.6 | 32.7 | 26.8 | 11.4 | 13.3 | 5.7 | **15.1** |
| Lennar | 14.4 | 10.9 | 15.1 | 12.1 | 14.5 | 22.8 | 20.5 | 15.5 | 14.4 | 8.3 | **14.9** |

**KB Home is LAST of nine on the ten-year mean.**

**THE DISCONFIRMING TEST, run before the verdict was written [E4-26].** The obvious defence
is that KB Home simply carries less leverage, so a lower ROE would mean nothing. **It fails
twice.** First, on the leverage-neutral measure:

**RETURN ON ASSETS — net income / average total assets, %**

| Company | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **10y mean** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **KB HOME (subject)** | 2.1 | 3.6 | 3.4 | 5.3 | 5.7 | 10.1 | 13.1 | 8.9 | 9.6 | 6.3 | **6.8** |
| NVR | 16.5 | 19.1 | 25.9 | 25.2 | 18.8 | 21.3 | 30.0 | 26.0 | 25.9 | 21.9 | **23.1** |
| D.R. Horton | 7.8 | 8.7 | 11.1 | 10.9 | 13.8 | 19.5 | 21.5 | 15.1 | 13.8 | 10.0 | **13.2** |
| PulteGroup | 6.2 | 4.5 | 10.3 | 9.7 | 12.3 | 15.2 | 18.6 | 16.9 | 18.4 | 12.5 | **12.5** |
| Meritage | 5.4 | 4.7 | 6.9 | 7.4 | 11.7 | 17.0 | 18.8 | 12.2 | 11.6 | 6.1 | **10.2** |
| M/I Homes | 3.8 | 4.2 | 5.5 | 6.2 | 10.1 | 13.5 | 14.1 | 12.0 | 13.2 | 8.6 | **9.1** |
| Lennar | 6.1 | 4.8 | 7.2 | 6.4 | 8.3 | 14.0 | 13.0 | 10.2 | 9.8 | 5.5 | **8.5** |
| Toll Brothers | 4.0 | 5.6 | 7.6 | 5.6 | 4.1 | 7.4 | 10.8 | 11.1 | 12.1 | 9.7 | **7.8** |
| Century Communities | 5.1 | 3.7 | 4.8 | 4.8 | 7.7 | 15.7 | 14.4 | 6.6 | 7.7 | 3.3 | **7.4** |

**KB Home is last of nine on the ten-year mean and last or joint-last in EVERY ONE of the ten
individual years.** Not a cycle artifact, not a single bad year, not a window choice: ten of
ten. Second, the direction of the leverage objection is backwards. KB Home's *"financial
leverage, as measured by the ratio of debt to capital, was **30.3%** at November 30, 2025"*
(FY2025 10-K), rising to **34.1%** at 2026-05-31 (10-Q). That is **more** debt than D.R.
Horton (19.8%), Lennar (21.1%) or Toll Brothers (17.4%) carried at their FY2025 ends, and
PulteGroup carries almost none. **KB Home earns the lowest return in the group on the most
leveraged balance sheet in the upper half of it.** The objection, tested, makes the finding
worse.

**The decomposition, so the reader can see where it goes wrong.** Ten-year means:

| | KBH | DHI | PHM | NVR | MHO | TOL | LEN | CCS |
|---|---|---|---|---|---|---|---|---|
| net margin (NI / total revenue), % | **7.1** | 11.4 | 12.3 | 12.7 | 8.0 | 10.7 | 10.1 | 6.6 |
| inventory turns (revenue / avg real-estate inventory), x | **1.23** | 1.70 | 1.41 | *see note* | 1.51 | 1.04 | 1.63 | 1.42 |

*Two cells in this secondary table are not comparably tagged and I say so rather than
estimate: Meritage stopped tagging a standard total-revenue element after 2017, and NVR does
not tag a single homebuilding-inventory total. **Neither gap touches the required row** — the
primary metric (ROE) and the disconfirming metric (ROA) are complete for all nine names in
all ten years — **so the moat class is not held PROVISIONAL on these two cells.** For NVR
specifically I went to the filing and added the components by hand: sold inventory $1,422.2M
plus unsold lots and housing units $253.5M plus land under development $39.3M = about
$1,715M at 2025-12-31 against $10,324M of revenue, i.e. **roughly 6.0x turns against KB
Home's 1.11x**.*

**And the filings say WHY NVR turns its inventory five times faster, which is the cost
advantage [E2-58] asks about, found in a competitor and not in the subject:**

> *"We expect, however, to continue to acquire **substantially all of our finished lot
> inventory using LPAs with forfeitable deposits**."* — NVR 10-K, FY ended 2025-12-31,
> accession 0000906163-26-000018

Against KB Home's own model: *"We focus on investments that provide a **one- to three-year
supply of land or lots** per product line, per community"* (FY2025 10-K), **59,106 lots owned
or under contract, about 62% of them owned** (10-Q, 2026-05-31), and **$2.61 billion of land
and land development investment in FY2025 alone** against $6.21bn of revenue. One builder
rents its land position with a capped downside; the other buys it. That is a structural cost
advantage, and **KB Home is on the wrong side of it.**

- **Peers named: 8 of an industry that has at least 14 listed US builders** (the eight above
  plus LGI Homes, Green Brick, Dream Finders, Tri Pointe, Taylor Morrison, Hovnanian, Beazer).
  Eight is Buffett's number **[E3-28]**; the excluded six are smaller or narrower and none of
  them would move a ranking in which the subject is last of nine.
- **Any peer unavailable? No.** All eight resolve on the required metric for all ten years.
  **The moat class is therefore NOT held PROVISIONAL** and this is not an UNRESEARCHED
  verdict; the evidence is in hand.
- **The row's limit, stated as [E3-61] requires:** this row shows *position*, not *conduct* —
  *"In some businesses, the participants behave like a demented Kellogg. In other businesses,
  they don't … I think you'd have to know the people involved."* It cannot tell me whether
  the eight will price rationally in the next downturn. It can tell me that over ten years,
  through one of the strongest housing markets in American history, **the subject earned less
  on its assets than every one of them.**

### The rest of the Q2 battery, each answered

- **Untapped pricing power [E3-33], scoped by [E5-28].** Claiming this class is claiming
  *"a monopoly or a near monopoly"* **[E5-28]**, and the row refuses it. Worse, the
  **inverse metric [E4-37]** — *"you can almost measure the strength of a business over time
  by the agony they go through in determining whether a price increase can be sustained"* —
  reads at the far end. KB Home did not agonise over a price *increase*; in February 2025 it
  cut: *"we both **reduced selling prices** relative to applicable market conditions and
  lowered or eliminated other homebuyer concessions"* (FY2025 10-K MD&A). **Not
  agony-pricing. Price-cutting, disclosed, as the strategy.**
- **Where units exist, monitor units [E4-55].** All three series point the same way, and the
  physical one is the honest one:

  | | FY2023 | FY2024 | FY2025 | FY2026 (company guidance, EX-99.1 2026-06-23) |
  |---|---|---|---|---|
  | homes delivered | 13,236 | 14,169 | **12,902** | **10,500–11,000** |
  | average selling price | $481,300 | $486,900 | **$481,400** | $457,000 (six months to 2026-05-31, actual) |
  | housing gross profit margin | 21.2% | 21.0% | **18.6%** | **16.1%–16.5%** |

  Units down about 17% on the guidance midpoint against FY2025 and about 24% against FY2024;
  price down; margin down 460–510bp in two years. **[E4-55]**'s Precision Steel case was
  dollar revenue held level by price rises while pounds fell: *"This decline in physical volume
  is a serious reverse, not likely to disappear in some ""bounce back'' e'ect."* **The ledger
  row carries an OCR artifact — doubled quote marks and "e'ect" for "effect" — and PRIME RULE 1
  says to flag it, never to smooth it, so it is reproduced as the ledger holds it.** KB Home
  does not even have that consolation:
  **units, price and margin are falling together.**
- **The two-characteristic test [E2-44].** (1) Can it raise prices *"even when product demand
  is flat and capacity is not fully utilized"*? **No — it cut them, in writing, and guides
  margin lower.** (2) Can it grow dollar volume *"with only minor additional investment of
  capital"*? **No — $2.61bn of land investment in FY2025, against $6.21bn of revenue and
  $428.8M of net income.** Fails both halves.
- **The attacker's test [E2-45]** — *"how I would like, assuming I had ample capital and
  skilled personnel, to compete with it."* I would like it very much. The trades are
  subcontracted and available to anyone; the materials are, in KB Home's own words,
  *"standardized materials that are commercially available on competitive terms from a variety
  of outside sources"*; the design is copyable; and the one thing that is genuinely scarce —
  entitled lots — is bought at auction against *"numerous homebuilders"*, some *"of which can
  bid more for land"* (FY2025 10-K, Item 1A). The barrier is capital, and capital is the one
  input a competitor can always raise.
- **Which of the four causes of extreme success [E4-36]?** There is no extreme success here to
  attribute. To the extent KB Home earned 24.5% on equity in 2022 and 19.9% in 2021, the row
  shows all nine builders did the same thing in the same two years. In **[E4-36]**'s own list
  the fourth cause is *"Catching and riding some sort of big wave"*, and **[E3-51]** is the
  mechanism: *"when a surfer gets up and catches the wave and just stays there, he can go a
  long, long time. But if he gets off the wave, he becomes mired in shallows."* 2025 shows the
  wave receding for all nine at once, which is what tells you the advantage was in the wave.
  *(The framework's gloss "a surfing run is not a moat; the advantage lives in the wave, not
  the surfer" is v4's own sentence and is deliberately not rendered here as a quotation.)*
- **Direction [E4-32]** — *"the moat widened every year"* is the primary criterion of a great
  business. KB Home's direction on every metric in this section is **narrowing**.
- **Key-person dependence [E4-23]?** Not found, and that is worth saying plainly because the
  absence is a point in the company's favour: the CEO transition from Jeffrey Mezger to Robert
  McGibney happened without the filings suggesting the business depends on either man. **But
  [E4-23] cuts the other way too** — *"if a business requires a superstar to produce great
  results, the business itself cannot be deemed great"* — and no superstar is available to
  rescue this one either. **[E2-37]** is the governing line: *"a textile company that
  allocates capital brilliantly within its industry is a remarkable textile company - but not
  a remarkable business."* *(the hyphen is the ledger's own punctuation)*

### Management's own moat claim, tested rather than dismissed **[E4-26]**

The company states one, and it deserves the strongest reading before it is set aside:

> *"We believe this highly interactive, 'customer-first' experience that puts our homebuyers
> firmly in control of designing the home they want based on what they value and how they want
> to live, at a price they can afford, **gives us a meaningful and distinct competitive
> advantage over other homebuilders and resale and rental homes**."* — FY2025 10-K, Item 1,
> "Business Strategy"

Supporting it: KB Home is *"the #1 customer-ranked national homebuilder based on third-party
buyer surveys"*, has *"delivered more ENERGY STAR certified homes than any other builder"*
(EX-99.1, 2026-06-23), and its Built to Order model is real, disclosed and unusual — 73% of
Q2 FY2026 net orders. **The claim is not empty and I do not find it dishonest.**

**It is refuted by the row, not by argument.** If Built to Order were *"a meaningful and
distinct competitive advantage"*, ten years is long enough for it to appear somewhere in the
returns. It appears nowhere: **last of nine on ROE, last of nine on ROA, last of nine in every
one of the ten individual years on ROA, second-lowest on net margin, lowest turns of the six
that resolve.** **[E3-46]** asks the question about the business before the manager, and the
business's answer is that the advantage KB Home describes is a product feature its customers
appear to like and its shareholders have never been paid for. **[E4-32]** is the sharper
form: a real moat shows up as *direction*, and this one has none.

### VERDICT

- Needed or desired [x] · no close substitute [ ] **FAILS** · not price-regulated [x]
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** —
  **not reached, and deliberately so.** Under the ruling of 2026-09-20, **[E4-04]** is applied
  as a *competence limit*, and the perimeter close (UNKNOWABLE at Q2) is reserved for a name
  that **passes [E3-03]** and whose durability cannot be judged from filings. **KB Home does
  not pass [E3-03]** — criterion 2 fails on the filer's own four-substitute sentence — so the
  TSM route is not available and must not be borrowed to soften this. The finding is about
  the business, it is made on filed evidence, and it is therefore **OUT**.
- Primary moat metric, filing-sourced, and its trend: **ten-year return on assets, 6.8% mean,
  last of nine peers in all ten years; trend falling (13.1% in 2022 to 6.3% in 2025).**
- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL · Direction: **NARROWING**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**Could I name the document that would resolve this?** The question does not arise: this is
an OUT, not a non-IN awaiting evidence. The documents that would have resolved it in KB
Home's favour — a filing showing a wide and sustainable cost advantage **[E2-58]**, or a peer
row in which the subject led — were sought and say the opposite.

### THE v3.0 PRIOR — what survived, and what must not be inherited

`Test Runs/2026-07-16 Run - Homebuilders 6-pack (KBH MHO TMHC MTH DFH CCS).md` gave KBH four
lines under **Framework v3.0**. It closes nothing and clears nothing, and its verdict is not
adopted here. Two separate findings about it:

1. **Its quote survives.** The prior rendered KBH's filing as *"compete... against numerous
   homebuilders... some of which are larger and have greater financial resources than us."*
   Opened against the FY2025 10-K, the sentence reads: *"We compete for homebuyers,
   construction resources and desirable land against numerous homebuilders, ranging from
   regional and national firms, some of which are larger and have greater financial resources
   than us, to small local enterprises."* **Every word the prior quoted is in the current
   filing, in that order, and the two ellipses cover exactly what they should.** This project
   has struck a prior brief's recollection as larger, smaller or absent more than once; this
   time the prior was accurate, and that is worth recording as plainly as an error would be.
2. **Its method must not be inherited.** The prior's stated rule was that *"a homebuilder
   passes Gate 2 only on a disclosed structural claim … generic competition text eliminates."*
   **That rule is not in v4 and is not in the corpus.** Eliminating a name because its
   competition paragraph reads generic is a verdict on prose, not on the business, and it
   would have produced the same OUT here for the wrong reason. This run reaches OUT through
   **[E3-03]** criterion 2 on the filer's own substitute list, and through a ten-year
   nine-name row on **[E3-46]**'s metric. **Same answer, different and far stronger evidence
   — and the difference matters, because the v3.0 rule would also have cleared a builder
   whose 10-K merely wrote a good paragraph.** *(The same file also shows two practices v4
   later banned outright: it marked DFH's Gate 3 a *"PASS (provisional)"* on *"general
   knowledge, unverified"*, which v4 makes a protocol violation, and it computed DFH's owner
   earnings as *"OE ≈ NI"*, the net-income proxy operator rule 5 forbids and the ADDENDUM of
   2026-09-20 works through. Nothing in that file is carried forward.)*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?

**NOT OPENED. The file closed at Q2 (OUT, on the business).** Operator rule 2: the sequence is
a hard block, and **[E4-19]**'s box is closed once the evidence is in and the business fails.

**What was nevertheless found and is deliberately NOT scored**, recorded so a future run does
not have to re-fetch it, and so that no reader mistakes an unscored prompt for a clean gate:

- The **8-K EX-99.1 of 2026-06-23** was pulled before this decision, per the CGNX standing
  instruction. It carries a **full quarterly and full-year guidance table** (deliveries,
  housing revenue, gross margin, SG&A ratio, tax rate, community count) and the Executive
  Chairman's line *"We produced solid second-quarter results that **met or exceeded the
  mid-point of our key guidance ranges**."* That is squarely the territory of **[E4-22]**'s
  third flag and of **[E5-30]** — *"once you start it, it's all over … forecasting earnings,
  I can't imagine anything more destructive"*. **It is a prompt to read, never a verdict
  [E5-36]**, it is not scored here, and it would have been the first thing scored had Q2
  passed.
- A **non-GAAP measure** exists: *"Adjusted housing gross profit margin"*, which adds back
  *"inventory impairment and land option contract abandonment charges"* — 19.1% against a
  GAAP 18.6% in FY2025. The gap is small, the reconciliation is published in full, and the
  measure is not EBITDA; but **[E5-33]** is the relevant line (*"to tell owners year after
  year, 'Don't count this' … is misleading"*) and it is left unscored, not scored clean.
- **The word "EBITDA" does not appear in the FY2025 10-K or in the 2026-06-23 EX-99.1.**
  Recorded as an observation about two documents that were read, **not** as an absence claim
  about the company's disclosure generally.
- The **DEF 14A of 2026-03-13 was downloaded** and is in the research folder. It was **not**
  read for the compensation metric, because Q2 had already closed. That is a named,
  deliberate gap, not an oversight.
- **VERDICT: NOT OPENED** *(not IN, not a pass, and not UNRESEARCHED — there is no work
  order, because the file is closed on the business at Q2)*

## Q4 — WILL IT SURVIVE?

**NOT OPENED.** See the computation block below, which is headed as operator rule 3 requires
and carries no entry language and no verdict.

- **VERDICT: NOT OPENED**

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**NOT OPENED, and it may not be.** Operator rule 2: *"No Q5 output may be reported unless
Q1-Q4 each show IN."* Q2 is OUT.

- **VERDICT: NOT OPENED**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**NOT OPENED as a gate** — there is no position and no entry, so **[E1-02]**'s
yardstick-before-the-act has nothing to attach to. **The reversal condition is recorded in
words** under the fold, per the QLYS ruling of 2026-09-07: a name that failed on the business
gets no price alert, because a price alert on it would be a category error.

- **VERDICT: NOT OPENED**

---

# COMPUTATION — NOT A CLEARANCE
**Operator rule 3.** Everything below was produced after Q2 closed the file. **It carries no
entry language, it is not a Q4 or Q5 output, and nothing in it can promote this name.** It
exists because the brief set three specific reading assignments — the `wc_note`, the
`da_note` and **[E4-25]**'s wider window — and because the screen's owner-earnings band is
used by the queue on other names and its construction turns out to be reproducible and worth
recording. Script: `Test Runs/_research 2026-09-21 KBH/rebuild_18yr.py`.

## 1. THE EIGHTEEN-YEAR REBUILD — what the five-year window could not see

`years_filed` is 18 and the `spread_caveat` says the band *"CANNOT see variation older than
the 5-year window; rebuild it [E4-25]"*. Rebuilt. **All 18 filed fiscal years, $M:**

| FY end | operating cash flow | SBC | D&A | PP&E capex | inventory | change in inventory |
|---|---|---|---|---|---|---|
| 2008-11-30 | 341.3 | 5.0 | 9.3 | — | — | — |
| 2009-11-30 | 349.9 | 4.0 | 5.2 | — | 1,501.4 | — |
| 2010-11-30 | **−134.0** | 8.1 | 3.3 | — | 1,696.7 | +195.3 |
| 2011-11-30 | **−347.5** | 8.1 | 2.0 | — | 1,731.6 | +34.9 |
| 2012-11-30 | 34.6 | 6.7 | 1.6 | — | 1,706.6 | −25.1 |
| 2013-11-30 | **−443.5** | 5.7 | 1.9 | — | 2,298.6 | +592.0 |
| 2014-11-30 | **−630.7** | 9.1 | 2.4 | — | 3,218.4 | +919.8 |
| 2015-11-30 | 181.2 | 17.1 | 3.4 | — | 3,313.7 | +95.4 |
| 2016-11-30 | 188.7 | 16.9 | 3.6 | — | 3,403.2 | +89.5 |
| 2017-11-30 | 513.2 | 14.6 | 2.8 | — | 3,263.4 | −139.8 |
| 2018-11-30 | 221.5 | 15.9 | 2.5 | 7.4 | 3,582.8 | +319.5 |
| 2019-11-30 | 251.0 | 18.3 | **27.2** | **40.5** | 3,704.6 | +121.8 |
| 2020-11-30 | 310.7 | 21.5 | 28.4 | 28.8 | 3,897.5 | +192.9 |
| 2021-11-30 | **−37.3** | 28.9 | 28.6 | 39.4 | 4,802.8 | +905.3 |
| 2022-11-30 | 183.4 | 29.5 | 32.3 | 45.2 | 5,543.2 | +740.3 |
| 2023-11-30 | **1,082.7** | 34.6 | 36.4 | 35.5 | 5,133.6 | **−409.5** |
| 2024-11-30 | 362.7 | 34.5 | 37.3 | 39.3 | 5,528.0 | +394.4 |
| 2025-11-30 | 335.7 | 46.2 | 37.3 | 48.4 | 5,670.8 | +142.8 |

**Operating cash flow was NEGATIVE in five of the eighteen filed years** — 2010, 2011, 2013,
2014 and 2021 — and the five-year window contains exactly one of them.

| window | mean OCF | − SBC | − (c) = D&A | **owner earnings, D&A end** |
|---|---|---|---|---|
| **three years, 2023–2025** | 593.7 | 38.4 | 37.0 | **518.3** |
| **five years, 2021–2025** (the screen's) | 385.4 | 34.7 | 34.4 | 316.3 · **309.1** at the total-capex end |
| **eighteen years, 2008–2025** | **153.5** | 18.0 | 14.8 | **120.7** |
| the decade the screen cannot see, 2011–2020 | 27.9 | 13.4 | 7.6 | **6.9** |

**The screen's band is reproduced exactly, and now its construction is known.** `oe_top_m`
**518** is the **three-year** OCF mean less SBC less D&A (593.7 − 38.4 − 37.0 = 518.3).
`oe_bottom_m` **309** is the **five-year** OCF mean less SBC less **total** PP&E capex
(385.4 − 34.7 − 41.6 = 309.1). That is the `spread_caveat`'s *"4-construction width only
(3y/5y x two capex ends)"*, confirmed to the dollar.

**And the spread it reports — 0.676, or "tight" — is arithmetic, not knowledge.** The
eighteen-year figure is **$120.7M, 61% below the band's own bottom end and 77% below its
top**. The decade 2011–2020 produces **$6.9M**, which rounds to nothing. **[E4-25]** is the
governing line — *"Usually, the range must be so wide that no useful conclusion can be
reached"* — and **[E4-38]** names the disease precisely: *"growth-rate presentations can be
significantly distorted by a calculated selection of either initial or terminal dates."* The
five-year window is not a calculated selection by anyone; it is the screen's default. But the
effect is the same, and **[E4-38]**'s remedy, publishing every window, is what the table above
does.

*(A disclosure about the eighteen-year capex end: `PaymentsToAcquirePropertyPlantAndEquipment`
is only tagged from FY2018. For FY2008–FY2017 the model-home and sales-office spend sat inside
**inventories** — see section 3 — and so is already netted inside OCF; the untagged residual
PP&E buying implied by those years' D&A of $1.6M–$3.6M is a rounding item against an
eighteen-year mean. The D&A end and the capex end of the eighteen-year figure differ by about
$1M, which is why only one number is quoted.)*

## 2. THE wc_note — resolved, and it is wrong in both of its two claims

The note reads: *"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 487% of
2021 OCF. Operating cash is not owner earnings when one balance-sheet line produced it (DELL,
INOD). Read the 2021 cash-flow statement and liquidity note."* Read it.

**Claim 1, "ONE LINE MADE THE CASH": false. There was no cash.** FY2021 operating activities
**consumed $37.3 million**. The 487% is arithmetically correct — |+181.6| ÷ |−37.3| = 487% —
and meaningless, because it divides by a denominator that is near zero **and negative**. A
ratio to a negative OCF cannot be read as a share of it, and the word "MADE" inverts the
direction of the year. **Tooling defect, class: a ratio published without a guard on the sign
or the magnitude of its denominator.**

**Claim 2, that accounts payable is the line to watch: false, and it names the wrong line.**
In FY2021 itself the **inventories** line of the same cash-flow statement moved **−$897.8M**,
**4.9 times** the accounts-payable move, and it is the inventories line that governs this
company's operating cash flow across the whole filed record. Over all eighteen years the
correlation between operating cash flow and the inventories line is **−0.58**, and the
mechanism is not statistical, it is definitional:

> *"(If the business requires additional working capital to maintain its competitive position
> and unit volume, **the increment also should be included in (c)**.)"* — **[E2-23]**, 1986

**For a homebuilder, land and homes under construction ARE the working capital, and they run
through operating activities.** Operating cash goes negative when the builder buys land
(FY2014: inventory +$919.8M, OCF −$630.7M; FY2021: +$905.3M, OCF −$37.3M) and positive when it
liquidates (FY2023: inventory **−$409.5M**, OCF **+$1,082.7M**). **The single largest
operating-cash year in KB Home's filed record is the year it shrank its land position.**

**So: is the multi-year mean measuring the cycle or the business?** The brief asked for an
answer with the filed series in front of me, and the answer is **both, and the window decides
which**. A three-year or five-year mean anchored on FY2023 is measuring **the liquidation
phase of a land cycle** and reports it as earnings. An eighteen-year mean spans one full
collapse (2008–2011) and one full boom (2020–2022) and is the only window in the filed record
that contains both ends of **[E2-58]**'s *"ratio of supply-tight to supply-ample years"*.
**That is the window [E2-42]'s five-year default was never designed to override and that
[E4-25] requires be carried alongside it.**

**And the maintenance question, which is the one that matters and which no window answers by
itself:** [E2-23] puts inside (c) only the working capital required *"to fully maintain … its
unit volume."* The two most recent filed years say that the increment KB Home is spending is
**not** buying unit volume:

| | FY2024 | FY2025 | FY2026 (company guidance) |
|---|---|---|---|
| inventory, year end | $5,528.0M | $5,670.8M | $5,730M at 2026-05-31 |
| homes delivered | 14,169 | 12,902 | 10,500–11,000 |
| inventory per home delivered | $390k | $440k | — |

**Inventory up 2.6% over two years; deliveries down about 24% on the FY2026 guidance
midpoint.** Under **[E2-23]** that is not growth capital, and it is not obviously maintenance
capital either — it is capital going in while unit volume goes out. **This is recorded as an
open question, not as a finding**, because the honest reading needs a completed FY2026 and the
Q3 10-Q does not exist yet (see Step 0).

## 3. THE da_note — resolved, and the brief's candidate explanation is REFUTED

The note reads: *"D&A steps 10.7x at 2019-11-30 — READ Note 1 and the cash-flow statement
before using either end of (c) [CERT 2026-09-07]"*, and the brief offered **ASC 842 (leases)**
as *"a candidate explanation and a candidate only"*. **Read, and it is not ASC 842. It is
ASC 606.**

The **FY2019 10-K (accession 0000795266-20-000007)** disposes of the lease candidate in its
own Note 1, under *Recent Accounting Pronouncements **Not Yet Adopted***:

> *"**We will adopt ASU 2016-02 and its related amendments (collectively, "ASC 842") beginning
> December 1, 2019** using the modified retrospective method. … Upon adoption, we expect to
> record lease right-of-use assets and lease liabilities of **approximately $31.0 million** …
> **We do not expect the adoption of ASC 842 to have a material impact on our consolidated
> statements of operations or cash flows.**"*

ASC 842 was adopted **the year after** the step, and was sized at $31.0M of gross right-of-use
assets — which could not produce a $24.7M one-year increase in depreciation in any case. **The
actual cause is in Note 10, Property and Equipment:**

> *"The balance at November 30, 2019 reflects **a change in the classification of certain
> community sales office and other marketing- and model home-related costs and related
> accumulated amortization from inventories to property and equipment, net** due to **our
> adoption of ASC 606** effective December 1, 2018."*

The filed table shows it directly: the line **"Model furnishings and sales office
improvements"** is **$0** at 2018-11-30 and **$82,117 thousand** at 2019-11-30. Note 1 of the
same filing states the consequence: *"Depreciation expense totaled **$27.2 million in 2019**,
**$2.5 million in 2018** and **$2.8 million in 2017**."* PP&E purchases step with it, from
$7.4M (FY2018) to $40.5M (FY2019).

**Why this matters to (c), and it matters more than the step itself.** The step is **not new
economic cost**. It is roughly $30–45M a year of model-home and sales-office spending that
**used to sit inside inventories — and therefore inside operating cash flow — and after
1 December 2018 sits in investing activities instead.** Three consequences, all of which bear
on how this screen's numbers should be read on **any** homebuilder:

1. **The pre-2019 and post-2019 OCF series are not like-for-like.** Post-2019 OCF is flattered
   by roughly the amount of this reclassification relative to the earlier years.
2. **D&A as the corpus default for (c) [E3-44, E2-41] is valid here for the post-2019 years
   and is nonsense for the pre-2019 years**, where it runs $1.6M–$3.6M on a business with
   $1.7bn–$3.6bn of inventory. In the eighteen-year table above this is why the D&A end and
   the capex end nearly coincide: the same money is in the series either way, just in a
   different statement.
3. **Neither end of (c) is the real maintenance question for this business anyway.** KB Home's
   renewal requirement is land, not plant. **[E5-20]**'s capital-intensity exception (*"merely
   spending their depreciation expense will not keep them in the same place"*) is about
   depreciable assets; for a builder the analogous understatement lives in the working-capital
   parenthetical of **[E2-23]**, which is section 2 above.

## 4. THE YIELD ARITHMETIC — shown once, so the register can carry a number, and **it is not a Q5 output**

Against the hand-struck cap of **$2,888.9M** (2026-09-18) and the **5.34%** US Treasury
30-year of the same date:

| owner-earnings construction | figure | yield on cap | vs sovereign |
|---|---|---|---|
| three-year (2023–25), D&A end — the screen's top | $518.3M | 17.9% | +12.6 pts |
| five-year (2021–25), total-capex end — the screen's bottom | $309.1M | 10.7% | +5.4 pts |
| **eighteen-year (2008–25), D&A end** | **$120.7M** | **4.2%** | **−1.2 pts** |
| the decade 2011–2020 | $6.9M | 0.2% | −5.1 pts |

**This is a computation and not a clearance.** The file is closed at Q2 on the business, so
the ~10% floor **[E4-28]** is not applied, no ranking position is assigned, and no bar
(**[E4-11]** or **[E4-01]**) is chosen. The table is here for one reason: to show that the
same company, on the same filings, at the same price, yields **17.9% or 4.2%** depending on
which three years you stand in — which is **[E4-25]**'s *"the range must be so wide that no
useful conclusion can be reached"* demonstrated on a live name, and the reason **[E4-38]**
says to publish every window. **Windage: none spent. No margin applied, because no value was
struck.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 **OUT**, Q3–Q6 marked
      **NOT OPENED** with the reason, per the hard sequence
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 is the
      only IN and it rests on the FY2025 10-K and the 2026-06-23 EX-99.1; the Q2 moat class is
      **NONE**, explicitly not PROVISIONAL, and the row that earns that is complete for all
      nine names across all ten years
- [x] Every UNRESEARCHED verdict names the artifact and where it lives — **there are none.**
      The unread DEF 14A is recorded at Q3 as a deliberate, named gap behind a closed gate,
      not as a work order
- [x] Every UNKNOWABLE verdict states what specifically cannot be known — **there are none**,
      and the Q2 block says explicitly why the **[E4-04]** perimeter close was **not** taken
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked —
      FY2025 operating cash flow, XBRL $335.7M against the filed statement's `335,682`, plus
      D&A `37,303` and SBC `46,238`. One **peer** figure cross-checked too: D.R. Horton's
      FY2025 net income, XBRL $3,585M against its filed statement's `3,585.2`
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment —
      done in the **COMPUTATION** block across four windows, under the operator-rule-3 heading,
      and **no net-income proxy was used anywhere** (operator rule 5; the ADDENDUM of
      2026-09-20 is the worked case)
- [x] Competitor row filled — eight peers, ten fiscal years, calendars aligned and stated,
      every figure filing-sourced; the two untagged cells in the **secondary** table are named
      and one of them (NVR inventory) was filled by hand from the filing
- [x] Sovereign is for the earnings currency, from the issuing authority, dated — USD, US
      Treasury daily par yield curve, 5.34% at 2026-09-18, fetched during this run
- [x] Value stated as a round-number range, not a point estimate — **n/a, no value was
      struck**; Q5 did not open
- [x] One bar chosen, not both; windage count stated — **n/a, no bar applies**; windage zero
- [x] Prices dated; aggregator used for live quotes only and flagged — $47.12 at 2026-09-18,
      Yahoo, flagged, raw JSON saved
- [x] **Every ledger id cited was checked directly against `principle_ledger.csv`: 46 distinct
      ids in the run file, 10 in the register entry, PHANTOM COUNT 0 in both.** Twenty-seven
      rows were then opened and read against the file's own text, not from memory
- [x] **THE VERBATIM AUDIT FOUND FOUR OF MY OWN ERRORS AND THEY WERE CORRECTED IN PLACE BEFORE
      THE FINAL COMMIT, and are named here so nothing is concealed** (PRIME RULE 1; the prior
      text stands in git at commit `2625053`):
      **(a)** I had rendered *"the advantage lives in the wave, not the surfer"* as a quotation
      under **[E3-51]**. It is **THE FRAMEWORK v4.md's own gloss**, not corpus. Replaced with
      [E3-51]'s actual words (*"when a surfer gets up and catches the wave …"*) and with
      **[E4-36]**'s own fourth cause, *"Catching and riding some sort of big wave."*
      **(b)** I had rendered *"neither creates the class"* as a quotation under **[E2-59]**.
      Same defect, same document: it is v4's commentary. Replaced with [E2-59]'s own sentence
      about administered prices and costs.
      **(c)** I had smoothed **[E4-55]**'s OCR artifacts, writing *"bounce back" effect* where
      the ledger holds `""bounce back'' e'ect`. PRIME RULE 1 says flag them, never smooth them;
      the artifact is now reproduced and flagged.
      **(d)** I had set an em dash inside **[E2-37]**'s quotation where the ledger holds a
      hyphen. Corrected to the ledger's punctuation.
      *(The (a) error is the same one the APOG fold of 2026-09-21 corrected on [E4-36] the day
      before — quoting the framework's summary of a row instead of the row. Two runs in two
      days. The cause is reading the corpus through `THE FRAMEWORK v4.md` rather than through
      `principle_ledger.csv`, and the fix is the one already in CLAUDE.md: "do not call a row
      verbatim without opening the document.")*
- [x] Run committed to git — five commits, each with a pathspec

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **KB Home fails [E3-03] criterion 2 on its own filing — it names four substitute
  categories and prices its homes "competitive with area resale home prices" — and the
  eight-peer, ten-year competitor row puts it LAST of nine on return on equity and LAST of
  nine on the leverage-neutral return on assets in every one of the ten years, which refutes
  the only exception [E2-58] allows a commodity business: a cost advantage that is wide and
  sustainable.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a. The **[E4-04]** perimeter close was available and was deliberately
  **not** used: under the ruling of 2026-09-20 it is reserved for names that pass [E3-03], and
  this one does not.

### THE REVERSAL CONDITION, IN WORDS — no price alert, per the QLYS ruling (2026-09-07)
A name that failed on the business gets no band in `tools/alerts.json` and no `PORTFOLIO.md`
row; a price alert would be a category error. **What would reopen this file is a change in the
business, and it is nameable:** KB Home would have to move to a **land-light structure** — the
thing its own competitor NVR discloses and KB Home does not have — such that owned lots fall
materially below the current ~62% of 59,106 and inventory turns rise toward the peer top
quartile, **and** the return-on-assets ranking in the row above changes for reasons other than
the cycle. **[E4-17]** governs the timing of any such belief: *"those beliefs change quite
gradually."* Short of that, the eighteen-year record and the nine-name row say the same thing
and this is a permanent OUT **[E4-19]**.

### FINDINGS OWED TO THE PROJECT, not to this name
1. **`cap_flag` defect** — it compares a filed float to a cap struck on a different date and
   reports the difference as an error. Sixth consecutive false firing. Fix stated in Step 0.
2. **`wc_note` defect** — the "% of OCF" ratio has no guard on the sign or magnitude of its
   denominator, so a year in which operating activities *consumed* cash is reported as a year
   in which one line *"MADE THE CASH"*. It also names the wrong line for this filer class.
3. **`newest_filing` is a report date, not a filing date** — the APOG finding, confirmed.
4. **The screen's owner-earnings band construction is now reproducible to the dollar**
   (3y/D&A for the top, 5y/total-capex for the bottom) and, on this name, sits **4.3x above
   the eighteen-year figure**. That is not an error in the tool — the `spread_caveat` says so
   itself — but it is a measured size for the caveat, which the caveat has never carried.
5. **`principle_ledger.csv` carries 311 unique ids, not 267.** Counted this run with
   `csv.DictReader`: 311 records, 311 non-empty ids, 311 distinct, no duplicates, no empty
   quote cells, 312 raw lines including the header; era split E1 18, E2 78, E3 79, E4 74,
   E5 62. `CLAUDE.md`'s KEY FILES pointer says **267** (itself a correction made 2026-09-19
   from 117). **Recorded for the operator and not acted on** — this run does not edit
   `CLAUDE.md`. It is exactly the failure mode that file warns about in its own words:
   *"Count the file, never the pointer."*
