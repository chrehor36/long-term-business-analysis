# Company Run — The Simply Good Foods Company (SMPL) — 2026-09-20
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

WAVE 7, name 3. **NEW PURCHASE question**, so v4 governs and not the holdings framework.

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
## ANSWER FIRST

**Q1 IN. Q2 OUT. The file closes at Q2, on the business, on criterion (2) of [E3-03].**
A brand portfolio in which the company's own filings say one brand is losing shelf space
(Atkins retail takeaway **-23.9%** in the quarter), a second is losing velocity on shelf
space it just gained (OWYN, "poor velocities, including on newly expanded distribution"),
and gross margin fell **470 basis points** in nine months on input costs the company could
not pass through, is not a product its customers think has no close substitute. The
closest listed peer lost **640 basis points** of gross margin in the same window, which is
the category answer and not a company answer: this is the commodity end's equation
**[E2-58]** operating on a set of trademarks.

**Price struck this session: $10.13 (2026-09-18, aggregator, FLAGGED).**
**Shares: 88,460,545, from the COVER of the 10-Q for the quarter ended 2026-05-30,
accession 0001702744-26-000023, filed 2026-07-09.**
**Cap: $896.1M. Sovereign: 5.34% USD 30Y, US Treasury, 09/18/2026.**

**THE CAP FLAG RESOLVED, AND THE BRIEF HAD THE DIRECTION WRONG.** The screen cap of $967M
is approximately right and the SHARE COUNT IS NOT TOO LOW. The float it was measured
against is a dollar figure from a 10-K cover struck on a date at which the stock traded at
**$37.75**. It now trades at **$10.13**. A cap below a stale cover float means the PRICE
moved, and here it moved by roughly three quarters in nineteen months. Full working in
"THE SCREEN ROW" below.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34** % · date **09/18/2026** · source (issuing authority) **US Treasury daily
  par yield curve, 30-year constant maturity**, struck this session by `python tools/sources.py`
- FX: none. SMPL is a US filer reporting in USD; foreign currency transactions were an
  immaterial $0.1M gain over thirty-nine weeks, and the Canadian subsidiary is being wound
  down. No ADR ratio.
- *Note on the brief: it warned me not to inherit 5.34%. I did not; I struck it fresh, and
  the Treasury curve returned 5.34% for 09/18/2026. The number is the same by coincidence,
  not by inheritance. The instruction was right and worth keeping.*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: Form 10-K for the fifty-two weeks ended 2025-08-30, filed 2025-10-28,
  accession 0001702744-25-000046** (`atk-20250830.htm`).
- **Also read in full: Form 10-Q for the thirteen and thirty-nine weeks ended 2026-05-30,
  filed 2026-07-09, accession 0001702744-26-000023** (`atk-20260530.htm`). This is the
  newest periodic filing and it is nine months newer than the annual report; every current
  fact in this run comes from it.
- **Also read: 8-K of 2026-07-09, accession 0001702744-26-000021, EX-99.1 earnings
  release** (`a991_pressreleasexq3x2026.htm`), pulled before any Q3 scoring, per the
  standing CGNX rule and **[E4-29]**.
- **Also read: 8-K of 2025-11-20, event date 2025-11-19, accession 0001104659-25-114309**,
  Items 1.01 / 2.03 / 9.01. This is the `deal_note` 8-K. **It is a credit facility
  amendment, not a merger.** See "LIVENESS CHECK" below.
- **Also read: 8-K of 2026-01-21, accession 0001104659-26-005379**, Item 5.02, the CEO
  transition; and 8-K of 2026-04-21, accession 0001104659-26-045701, Item 5.02.
- **Figure cross-checked against the filed statement, two of them:**
  1. **Term Facility.** Note 5 of the 10-Q states the Term Facility balance at 2026-05-30
     as **$400,000 thousand**, less deferred financing fees of $2,963 thousand, giving
     **$397,037 thousand**, which is the number printed on the face of the consolidated
     balance sheet as "Long-term debt, less current maturities". The two agree to the
     dollar. The XBRL was not used for either.
  2. **Share count.** The balance sheet states **104,050,545 shares issued** and
     **15,609,338 treasury shares** at 2026-05-30, a difference of **88,441,207**. The
     cover of the same document states **88,460,545 shares issued and outstanding as of
     July 2, 2026**. The two reconcile across the thirty-three days between them. This is
     the figure the market cap is struck on, and it is a filed-statement cross-check of the
     one input the screen flagged as impossible.

---
## LIVENESS CHECK — done before anything was priced

The ROKU rule of 2026-09-12 and the LEG fold of this week both say a `deal_note` gets read
before a run is spent. Done, and SMPL is alive:

- `submissions.json` for **CIK 0001702744** returns `entityType: operating`,
  `exchanges: ['Nasdaq']`, `tickers: ['SMPL']`, `category: Large accelerated filer`,
  `fiscalYearEnd: 0826`, no former names.
- The newest filings are a 10-Q filed **2026-07-09** and Forms 4 filed **2026-07-24**. A
  deregistered company does not file those.
- The `deal_note` 8-K is the **2026 Incremental Facility Amendment**: an eighth amendment
  to the 2017 Barclays credit agreement adding **$150.0 million** to the Term Facility and
  extending its maturity from March 2027 to **March 2030**. There is no EX-2.1 because
  there is no merger. **The brief's guess, "most likely a credit facility or offering",
  was correct.**

---
## THE SCREEN ROW — REPRODUCED, THEN ADJUDICATED. IT IS DATA, NOT A VERDICT.

Row as given, from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`:
`SMPL,Simply Good Foods Co,967,128,160,0.249,...`

### 1. `cap_flag` — "CAP BELOW FILED PUBLIC FLOAT". RESOLVED: **the cap is right and the flag is an artefact.**

The flag says cap $967M against a filed float of $3,300M as of **2024-02-23**, a ratio of
3.41x, and instructs a hand re-strike.

**Re-struck by hand:**

| | | |
|---|---|---|
| shares outstanding | **88,460,545** | cover of 10-Q, accession **0001702744-26-000023**, as of 2026-07-02 |
| cross-check | 104,050,545 issued less 15,609,338 treasury = 88,441,207 | face of the balance sheet, same document, 2026-05-30 |
| price | **$10.13**, close of **2026-09-18** | **AGGREGATOR — FLAGGED**, `tools/sources.py` |
| splits after the measurement date | none | no split events in the filing history |
| **cap** | **$10.13 x 88,460,545 = $896.1M** | split-invariant form |

The screen's $967M implies a price of **$10.93** on the same share count, which is a
plausible early-September quote. **The screen's cap was not broken.** The broken half is
the comparison:

- **The float figure is a DOLLAR AMOUNT frozen at a cover-page measurement date.** The
  FY2025 10-K cover, accession 0001702744-25-000046, reads verbatim: *"The aggregate
  market value of the common stock held by non-affiliates of the registrant as of February
  28, 2025, the last trading day of the registrant's most recently completed second fiscal
  quarter was approximately $3.5 billion based on the closing price of **$37.75** for one
  share of common stock, as reported on the Nasdaq Capital Market on that date."*
- **$37.75 then. $10.13 now.** The stock has lost **73%** in nineteen months. A cap
  measured today cannot help but sit below a float measured at four times the price.
- **The screen also used the WRONG cover.** Its float datum is $3,300M as of
  **2024-02-23**, which is the FY2024 10-K's cover, accession 0001702744-24-000089, one
  year older again, while the screen's own `newest_filing` column already pointed at the
  FY2025 annual period. **So the flag compares a cap of September 2026 with a float of
  February 2024: thirty-one months of drift.**

**THE OPERATOR'S PRIOR, REFUTED IN BOTH HALVES.** The brief said (a) re-striking the cap is
"the first real work of the run" and (b) "a cap below a filed float most obviously means
the SHARE COUNT is too low". (a) is wrong on informativeness: the re-strike took four
fetches and produced no business finding. (b) is wrong on direction: the share count is
right to the share, and it is the PRICE that moved. The brief was right about one thing and
asked me to check it rather than assume it: SMPL's annual period does end in August
(`fiscalYearEnd` 0826), and its cover float is therefore measured at the **last trading day
of February**, not June 30. Both covers confirm it, 2024-02-23 and 2025-02-28 being
late-February Fridays. **The premise checked out; the inference drawn from it did not.**

**What this flag class actually is.** `cap_flag` compares a live-priced cap with a
point-in-time dollar float. It will fire on every name whose stock has fallen hard since
its last cover date, and it will never fire on one that has risen. **It is a drawdown
detector wearing a data-integrity label.** That is a useful thing to own; it is not what
the label says, and a run that reads it as "one of the two is wrong" goes looking for a
share-count error that is not there. Recorded as a tooling finding.

### 2. `acq_note` — "NET CASH INFLOW ($282M, 29% of cap)". RESOLVED: **a sign-convention flip between XBRL vintages. There was no inflow.**

`PaymentsToAcquireBusinessesNetOfCashAcquired`, as filed:

| fiscal year | tagged in the FY2024 10-K (0001702744-24-000089) | tagged in the FY2025 10-K (0001702744-25-000046) |
|---|---|---|
| FY2024, ended 2024-08-31 | **+280.4** | **-280.4** |
| FY2025, ended 2025-08-30 | — | **-1.7** |

**The same year, the same company, the same element, opposite signs in two consecutive
annual filings.** The screen reads the newest vintage, summed the two negatives
(-280.4 plus -1.7 = **-282.1**), and reported a $282M net cash INFLOW. There was none.

**What actually happened**, read from the filing text and not from a tag, exactly as
section 5 of the RESUME STATE requires:
- **June 13, 2024: SMPL acquired Only What You Need, Inc. ("OWYN")**, a plant-based RTD
  protein shake brand. The 10-K's intangibles note states the acquired **brand
  indefinite-lived intangible at approximately $223.0 million** and the **customer
  relationship intangible at $20.5 million** at the acquisition date; goodwill rose from
  $543.1M to $591.7M.
- It was financed with cash **and $250.0 million of incremental term debt**, the 2024
  Incremental Facility Amendment of the same date, 8-K accession 0001104659-24-072273.
- The FY2025 investing line of **-$1.7M** is the tail: the 10-Q names it as **$1.7 million
  of cash proceeds received from escrow related to net working capital adjustments**,
  a small inflow, correctly signed.

So the perimeter is **understated by the screen in the opposite direction from the usual
case**: the project's six recorded perimeter understatements came from stock consideration
invisible to the tags; this one came from a sign flip that turned $282M of spending into
$282M of receipts. **That is a new failure mode for the flag and it belongs in the tooling
record.** The truncated note, "so the CONSIDE", was truncated on a sentence that was wrong
anyway.

**And the business fact behind it is the sharpest thing in this run**, because OWYN cost
about $280M in June 2024 and by **2026-05-30** the company had written **$200.0 million**
off the OWYN brand intangible. See Q2.

### 3. `da_note` / `spread_caveat` — "4-construction width only, rebuild it [E4-25]". DONE, and the rebuild LOWERS the bottom by about a quarter.

The screen's published band was **$128M to $160M**. It could not see behind a five-year
window. Rebuilt over every year that exists (`years_filed` said 8; there are eight full
fiscal years plus a 2017 stub), all figures in $M, every one from a 10-K:

| FY | revenue | OCF | SBC | D&A | depreciation only | capex | OE, c=D&A | OE, c=depn | OE, c=capex |
|---|---|---|---|---|---|---|---|---|---|
| 2018 | 431.4 | 61.0 | 4.0 | 7.7 | 1.2 | 1.8 | 49.3 | 55.8 | 55.2 |
| 2019 | 523.4 | 73.0 | 5.5 | 7.6 | 1.1 | 1.0 | 59.9 | 66.4 | 66.5 |
| 2020 | 816.6 | 58.9 | 7.6 | 16.0 | 1.8 | 1.7 | 35.3 | 49.5 | 49.6 |
| 2021 | 1005.6 | 132.1 | 8.3 | 18.2 | 2.3 | 5.9 | 105.6 | 121.5 | 117.9 |
| 2022 | 1168.7 | 110.6 | 11.7 | 19.3 | 3.2 | 5.2 | 79.6 | 95.7 | 93.7 |
| 2023 | 1242.7 | 171.1 | 14.5 | 20.3 | 4.4 | 11.6 | 136.3 | 152.2 | 145.0 |
| 2024 | 1331.3 | 215.7 | 18.4 | 21.0 | 5.8 | 5.7 | 176.3 | 191.5 | 191.6 |
| 2025 | 1450.9 | 178.5 | 15.3 | 21.4 | 6.1 | 20.5 | 141.8 | 157.1 | 142.7 |

**Every window published [E4-38]**, because picking one and defending it is the named
disease:

| window | OE mean, c = D&A | OE mean, c = depreciation only | OE mean, c = total capex |
|---|---|---|---|
| **8 years, FY2018-FY2025** | **98.0** | 111.2 | 107.8 |
| 5 years, FY2021-FY2025 | 127.9 | 143.6 | 138.2 |
| 3 years, FY2023-FY2025 | 151.5 | 166.9 | 159.8 |
| FY2025 alone | 141.8 | 157.1 | 142.7 |
| **TTM to 2026-05-30** | **107.9** | 123.5 | 103.8 |

The screen's $128M bottom is the five-year mean at c = D&A, 127.9. **The eight-year mean is
$98.0M, twenty-three percent lower**, and the window the screen could not see is the one
containing the pre-Quest business. `spread_caveat` was right that the band was construction
width only, and the rebuild widens it downward, which is what **[E4-25]** predicts when a
distorted window is opened up.

TTM to 2026-05-30 is built as FY2025 less the thirty-nine weeks to 2025-05-31 plus the
thirty-nine weeks to 2026-05-30: OCF 178.5 - 133.1 + 102.2 = **147.6**; SBC 15.3 - 12.8 +
13.2 = **15.7**; D&A 21.4 - 15.5 + 18.1 = **24.0**; capex 20.5 - 2.5 + 10.1 = **28.1**;
intangible amortisation 15.1 - 11.2 + 11.7 = **15.6**, so depreciation only = 24.0 - 15.6 =
**8.4**.

### 4. `level_shift` 2.16 and `level_shift_oe` 2.09 — "STEP UP, normalize down [E4-41]". **ADJUDICATED: DO NOT NORMALISE DOWN.**

A ratio is a prompt to read, never a score (operator rule 8). Read, the step is made of two
dated purchases and not of a lucky year:

- **November 7, 2019: Quest Nutrition**, financed with **$460.0 million** of incremental
  term debt, the Incremental Facility Amendment named in the 10-Q's own debt note. FY2020
  revenue went 523.4 to 816.6 on a part-year of Quest; FY2021 to 1,005.6 on a full year.
- **June 13, 2024: OWYN**, financed with **$250.0 million** of incremental term debt.

**[E4-41] is about removing FAVOURABLE EXOGENOUS BREAKS from a mean before trusting it.**
The corpus's worked case is a no-megacat year and a bond tailwind. **A bought business is
neither exogenous nor a break.** Quest is permanently inside the perimeter and is the one
brand still growing; normalising it away would delete the only working part of the company.
**The flag's instruction is refused here, with the reason written down.**

The same reading finds what the ratio was pointing at from the wrong end. **The step up was
bought with debt at the top and part of it is now being written off:**

| | |
|---|---|
| Term Facility, FY2019, pre-Quest | $190.9M |
| after Quest, OWYN and the 2026 amendment, at 2026-05-30 | **$400.0M** |
| brand and goodwill impairments, FY2025 | **$60.9M** (Atkins brand and a licensing agreement) |
| brand and goodwill impairments, 39 weeks to 2026-05-30 | **$331.0M** ($200.0M OWYN brand, $93.0M Atkins brand, $38.0M goodwill) |
| **total, twenty-four months** | **$391.9M** |

**$391.9M of written-off intangibles against $400.0M of borrowed money.** That is not a step
up to normalise down. It is a step up that has begun to reverse, and it belongs at Q2 and in
the Q3 items, not in a mean adjustment.

### 5. The two numbers the screen got right
`years_filed` 8 is right: FY2018 through FY2025 are eight full fiscal years, and FY2017 is a
stub from the July 2017 formation. `growth_required` -0.0323 is directionally right: at the
screen's own cap the name needed negative growth to clear, which is a way of saying it
looked cheap, and the computation below finds the same. **Neither is a verdict.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** SMPL owns three trademarks
  (Quest, Atkins, OWYN) and does not own a factory. It pays contract manufacturers to make
  protein bars, protein chips, cookies, confections and ready-to-drink protein shakes; it
  pays retailers, through trade promotion and slotting, to put them on the nutrition shelf;
  and it pays for advertising and social influencers to make shoppers pick its box rather
  than the one beside it. Revenue is boxes sold times price. About **36 cents of each
  revenue dollar survived cost of goods in FY2025** and about **32 cents in the nine months
  to May 2026**; of that, selling and marketing took about 9 to 10 cents and general and
  administrative about 10 to 11 cents. Capital employed in things is trivial: property and
  equipment is **$42.3M on a $2,062.4M balance sheet**, and capex has run **$1.0M to $20.5M
  a year on revenue of $431M to $1,451M**. Capital employed in trademarks is almost
  everything: intangibles and goodwill were **$1,508.9M, seventy-three percent of total
  assets**, at 2026-05-30.
- **The scarce input this business controls:** **shelf facings in the retailer's nutrition
  aisle, at two retailers.** Walmart was **31%** of consolidated FY2025 sales (24% mass, 7%
  Sam's Club and e-commerce) and Amazon **18%**. The 10-K says the contracts are **"at
  will"** and carry **no recurring or minimum purchase amounts**. The trademark is what the
  company owns; the facing is what it must keep renting, and the renter can stop.
- **Will the fundamentals look broadly the same in ten years?** The mechanism will: people
  will still buy portable protein, contract manufacturers will still make it, and a handful
  of retailers will still decide who is on the shelf. **Which trademark is on the box is the
  part that does not stay the same**, and this company's own filed record is the proof: the
  Atkins brand it was built around is down **22.1%** in retail takeaway year to date. That
  answer belongs at Q2, not here.
- **Circle-of-competence check [E4-46]:** this took under an hour of filings to understand
  and nothing in it is a five-month study. It is a simple business.

- **VERDICT: [x] IN**

*Recorded against [E5-13]: most names should end at Q1 and this one does not, which is the
system working in the other direction. Q1 IN is not a compliment; it is a statement that the
arithmetic of the business is legible.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

The test, verbatim: a franchise is a product or service that **"(1) is needed or desired;
(2) is thought by its customers to have no close substitute and; (3) is not subject to
price regulation."**

- **(1) Needed or desired** — [x] yes. Category demand is real and the company is not
  inventing it.
- **(2) No close substitute** — [ ] **FAILS.** This is where the file closes, and the
  evidence is the company's own, in its own words.
- **(3) Not price-regulated** — [x] yes, not regulated.

### The evidence for the failure of criterion (2), all filed, all dated

**(a) The shelf is being taken away and the consumer is not objecting.** From the EX-99.1
of 2026-07-09, accession 0001702744-26-000021, verbatim: *"Net sales of $357.0 million
decreased 6.3% versus the comparable year ago period, driven by a decline for Atkins of
24.6%"* and *"Total Simply Good Foods retail takeaway decreased about 6.7% ... while Atkins
declined 23.9%, which was largely as expected for the brand due to known distribution
losses."* Retail takeaway is the consumer-level series. It fell **23.9%** alongside the
distribution loss. **A product with no close substitute does not lose a quarter of its
consumer offtake when a retailer reduces its facings; the shopper goes and finds it, or
complains to the retailer.** Here the shopper bought something else.

**(b) Extra shelf space did not produce sales.** Year to date, from the same release:
*"OWYN's net sales decline was the result of **poor velocities, including on newly expanded
distribution**."* This is the inverse experiment and it is the more damning one. Atkins
lost distribution and lost sales; OWYN GAINED distribution and still lost sales. **When a
brand is given more facings and sells less per facing, the facing was the asset and the
brand was not.**

**(c) The company cannot raise price into a cost increase.** Nine months to 2026-05-30:
gross margin **32.2%** against **36.9%**, a **470 basis point** fall, and the MD&A's stated
cause is *"higher input costs and restructuring costs"*. This is **[E2-44]**'s first
characteristic failing on the filed statement: the test is whether the business can raise
prices *"even when product demand is flat and capacity is not fully utilized"*, and demand
here is not flat but falling, and the price did not move. **[E4-37]**'s inverse metric
points the same way: *"you can almost measure the strength of a business over time by the
agony they go through in determining whether a price increase can be sustained."* Nothing
in these filings suggests a price increase was even attempted; the response to margin loss
was **restructuring costs and a planned reduction in Atkins marketing spend**.

**(d) The physical series is the honest one, and it is negative. [E4-55].** The corpus's
rule where units exist is to monitor units, because dollar revenue flattered by pricing is
how a shrinking franchise hides. Here there is no flattering to do. Retail takeaway minus
3.8% year to date; Atkins takeaway minus 22.1%; company net sales guided to **$1.345bn to
$1.355bn for FY2026, a decline of roughly 6% to 7%**.

**(e) The company's own valuers priced the trademarks down by $391.9M in twenty-four
months.** FY2025: **$60.9M** on the Atkins brand and a licensing agreement, triggered, in
the 10-K's words, by *"the declines of future revenue projections during the fourth quarter
of fiscal year 2025"*. Thirty-nine weeks to 2026-05-30: **$200.0M on OWYN, $93.0M on
Atkins, $38.0M on goodwill**. The Atkins impairment is a **critical audit matter** in the
FY2025 10-K.

**I must discount part of (e) and here is why.** The FY2026 impairments were triggered, in
the 10-Q's own words, by *"the sustained decline in the Company's share price and declines
in the Company's market capitalization"*. That is **circular**: the market marks the equity
down, the accounting marks the assets down to follow, and a run that counts the write-down
as independent evidence of a weakening moat is counting the share price twice. **So the
FY2026 $331.0M is not treated here as independent evidence.** What is independent is (a)
through (d), which are unit and margin facts, and the **FY2025 $60.9M**, whose stated
trigger was revenue projections and not the stock. **The verdict below does not need the
FY2026 number and does not rest on it.**

- **Must the moat be continuously rebuilt? Does success depend on a great manager?
  [E4-04]:** The moat here is being rebuilt rather than defended, and the filing says so in
  its own strategy section: growth comes from *"line extensions and through acquisitions"*,
  from *"the continued pursuit of merger and acquisition transactions"*, and the company is
  *"actively seeking to identify and evaluate new acquisition opportunities"*. Under the
  framework's own test, **does a lapse in spending destroy the structure or merely narrow
  it, and does the spending defend the same advantage or buy its replacement?** Quest was
  bought to replace Atkins and OWYN was bought to supplement Quest. **That is buying a
  replacement, which is the excluded class, and not Coca-Cola defending one trademark.**
- **Primary moat metric, filing-sourced, and its trend:** gross margin. FY2021 40.8%,
  FY2022 38.1%, FY2023 36.5%, FY2024 38.4%, FY2025 36.2%, nine months FY2026 **32.2%**.
  **Direction: down, and accelerating.** **[E4-32]** makes direction the primary criterion
  of a great business, and this direction is the wrong one.

### THE COMPETITOR ROW — required [E3-28]

Every figure below computed by me from the named filing, same metric, matched windows.

| Company | net sales, latest matched period | growth vs prior year | gross margin, latest | gross margin, prior | source |
|---|---|---|---|---|---|
| **SMPL (subject)** | **$1,023.2M**, 39wk to 2026-05-30 | **-5.4%** | **32.2%** | 36.9% | 10-Q, accession 0001702744-26-000023 |
| **BellRing Brands (BRBR)** | **$1,706.4M**, 9m to 2026-06-30 | **+2.3%** | **28.5%** | 34.9% | BRBR 10-Q, CIK 0001772016 |
| **Medifast (MED)** | $385.8M, FY2025 | **-36.0%** | 71.3% | 73.8% | MED 10-K, CIK 0000910329 |
| **Herbalife (HLF)** | $5,037.5M, FY2025 | +0.9% | 77.9% | 77.9% | HLF 10-K, CIK 0001180262 |
| **Celsius (CELH)** | $2,515.3M, FY2025 | +85.5% | 50.4% | 50.2% | CELH 10-K, CIK 0001341766 |

And the full-fiscal-year gross margin series, subject against its closest peer:

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | latest 9m |
|---|---|---|---|---|---|---|
| **SMPL** | 40.8% | 38.1% | 36.5% | 38.4% | 36.2% | **32.2%** |
| **BRBR** | 31.0% | 30.8% | 31.8% | 35.4% | 33.3% | **28.5%** |

- **Peers named: 4, of which 1 is a true like-for-like.** The listed competitor set for
  branded nutritional snacking in the US is small: **BellRing Brands is the only pure-play
  public comparable**, with Premier Protein and Dymatize selling the same RTD shakes and
  powders into the same Walmart, club and e-commerce channels. Medifast and Herbalife are
  included because they are the listed weight-management brands and the Atkins question is
  a weight-management question; their direct-selling model makes gross margin
  non-comparable in LEVEL, so only the DIRECTION is read from them. Celsius is the adjacent
  functional-beverage case, included as a control on whether the whole consumer-health
  shelf is shrinking. It is not: Celsius grew 85.5% with its margin flat.
- **Peers unavailable, named with the obstacle:** **private label** is the competitor the
  10-K names first and it files nothing; **Abbott (Ensure)** and **Nestle (Boost,
  Optifast)** do not segment the nutrition brands to a comparable line, and Nestle is a
  foreign issuer outside EDGAR. **The moat class is NOT held PROVISIONAL on this**, because
  the verdict is OUT and not IN: the missing peers could only make the subject look
  relatively better, and criterion (2) already fails on the subject's own filings.
- **What the row shows.** **SMPL is the higher-margin one and it is the shrinking one.** It
  carries 370 basis points more gross margin than BRBR and it is the one losing sales.
  **Both lost roughly 500 to 650 basis points of gross margin in the same twelve months**,
  so the cost shock passed through neither of them. **That is the commodity end's equation
  [E2-58]** — *"persistent over-capacity without administered prices (or costs) equals poor
  profitability"* — applied not to the trademarks but to the layer underneath them: the
  contract-manufacturing and protein-input layer has pricing power over both branded
  buyers, and the branded buyers have none over the retailer. **Neither end of this business
  is where the administered price sits.**
- **The row's limit, stated [E3-61]:** the row shows position and cannot show conduct. It
  cannot tell me whether Quest's 5.1% takeaway growth is a durable share gain or BellRing
  choosing not to contest it, and the corpus says even Munger had no model for predicting
  that: *"I think you'd have to know the people involved."*
- **An absence, worded as the absence-claim rule requires.** A recorded sweep was run on
  2026-09-20 against EDGAR full-text search, 10-K forms, 2024-09-01 to 2026-09-20, for
  `"Simply Good Foods"`, `"Quest Nutrition"`, `"Atkins"`, `"OWYN"` and `"Premier Protein"`.
  **No instance was found of any competitor's 10-K naming this company or its brands.** The
  only non-SMPL hits were unrelated uses of the surname Atkins and a Farmer Brothers
  reference. **Weight it low:** the same sweep shows BellRing's own brand named only in
  BellRing's and Post's filings, so not naming rivals is this industry's convention and the
  absence says little either way. It is recorded because it was looked for.

- **Untapped pricing power [E3-33]?** **No, and the opposite.** Claiming that class is
  claiming near-monopoly **[E5-28]**, and the competitor row supports nothing of the kind.
  The filed record is of a company that met an input-cost increase by cutting marketing and
  taking restructuring charges.
- **The dominance class [E2-53]?** No. *"Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be."* Here the
  marketplace, in the form of a retailer's planogram decision, determined it.
- **The second question about the business is a number [E3-46]:** *"the best businesses, by
  definition, are going to be businesses that earn very high returns on capital employed
  over time."* Return on book equity has never exceeded **10.5%** in eight fiscal years
  (10.5, 5.7, 5.8, 3.4, 7.5, 8.5, 8.1, 5.7). The series and the mandatory **[E2-43]**
  scoping are in the Q3 items below, because the denominator is 73% purchase price.
- **The attacker's test [E2-45]** — how would I compete with it, given ample capital and
  skilled people? **I would buy the facing.** Trade spend and slotting at two retailers, a
  contract manufacturer anyone can hire, and an influencer budget. The barrier is money,
  and money is the one barrier the corpus does not count as a moat.
- **Which of the four causes of extreme success [E4-36] is the record from?** It is
  **wave-riding [E3-51]**. Atkins rode the low-carbohydrate wave; Quest rode the protein
  wave. *"when a surfer gets up and catches the wave and just stays there, he can go a
  long, long time. But if he gets off the wave, he becomes mired in shallows."* **Atkins is
  the filed demonstration of getting off the wave, inside this same registrant.** The
  advantage lives in the wave and not in the surfer, and a surfing run is not a moat.
- **Key-person dependence, recorded here as a moat defect and not at Q3 [E4-23].** On
  **2026-01-19**, 8-K accession 0001104659-26-005379, **Joseph E. Scalzo, 66, returned as
  President and CEO**, succeeding Geoff Tanner, who had held the job two years. Scalzo ran
  this company from July 2017 to January 2024 and ran Atkins Nutritionals before that.
  **The company's answer to a broken brand portfolio was to bring back the man who built
  it.** *"if a business requires a superstar to produce great results, the business itself
  cannot be deemed great ... You can count, though, on the moat of the Mayo Clinic to
  endure, even though you can't name its CEO."* **Recorded as a Q2 moat defect, exactly as
  the framework instructs, so that a warning about the business is not misread as a
  compliment to the person.**

### THE STRONGEST SINGLE FACT AGAINST THIS VERDICT, stated as its holders would state it **[E4-51]**

*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."* The bull case, fairly:

**Quest works.** Quest net sales grew **3.4%** year to date and Quest **retail takeaway grew
5.1%**, in a category where the closest listed peer grew 2.3% and the subject as a whole
shrank. **Quest's brand intangible was put through the same quantitative impairment test as
Atkins and OWYN in the third quarter of FY2026 and passed**: the 10-Q states *"its fair
value exceeded its carrying value, resulting in no impairment."* On that reading SMPL is not
one failing business but one working brand carried inside a holding company alongside two
mistakes, priced as though all three were broken, generating **$147.6M of trailing operating
cash on a $896M market value** with net debt of $276M and no principal due for a year. That
is the case, and it is a real one.

**Why it does not save the gate.** First, **the security is the company and not the brand**,
and the unit of the test is the company **[E4-08]**; I cannot buy Quest. Second, Quest's
growth is **volume-driven at a falling gross margin** — the same 470 basis points apply to
it, and a brand that must sell more units at a worse margin to stand still is demonstrating
the substitute problem rather than escaping it. Third, **Quest is itself a wave**, bought
at the top of the protein wave with $460M of borrowed money, and the registrant's own
history contains the worked example of what the end of a wave looks like. Fourth, **the
Quest impairment test passing is a statement that fair value exceeded carrying value with
no margin disclosed** — it is the absence of a write-down, not a valuation. **The bull case
is a price argument, and Q2 is not a price question [E5-42]**: *"whether it's a good
investment for us depends on how much we pay for that in the end"* comes AFTER the business
is judged.

- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL · Direction: **narrowing**, and
  the narrowing is measured in the filings at 470 basis points of gross margin and 22
  percentage points of Atkins takeaway in twelve months.
- **VERDICT: [x] OUT** — permanent, on criterion (2) of **[E3-03]**, evidenced from the
  company's own 10-Q and its own earnings release. **Not UNKNOWABLE:** I can name the
  documents and I have them, and they answer the question rather than leaving it
  indeterminate, which is the separating test **[E4-19]** run in the OUT direction. **Not
  UNRESEARCHED:** no further artifact would change a unit series that the company itself
  publishes and explains.

**The cost of this verdict, acknowledged [E3-47]:** *"Typically, our most egregious mistakes
fall in the omission, rather than the commission, category ... their invisibility does not
reduce their cost."* This is a business I understand, trading at a trailing owner-earnings
yield of roughly 12% (computed below, not a clearance). If Quest is a franchise and the
market is pricing the whole company as though it were Atkins, this OUT is an omission error
and it will not be visible. **I am writing that down rather than hedging the verdict**, and
Q6 pre-commits the metric that would prove it wrong.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN. The gate closed at Q2. Everything below is
RECORDED, NOT GOVERNING.**

---
## Q3 ITEMS — NO VERDICT IS WRITTEN; THE GATE IS CLOSED AT Q2 **[E2-01, E4-22, E4-29, E2-49, E4-30, E5-08, E2-52, E5-24]**

Recorded because the run read the filings and the findings are owed to the register, and
because **[E4-29]** requires the earnings release to be read before any Q3 scoring. **No
verdict is drawn, and none of this promotes or rescues anything [E2-37, E3-39].**

**The weight case, declared anyway.** Daily execution: **ticked**. This is an
undifferentiated consumer product whose position must be re-won at every planogram reset,
which puts it on **[E3-43]**'s *"a business, unlike a franchise, can be killed by poor
management"* side of the line rather than the franchise side. Control: no. Leverage: no,
about 1.25 times net debt to guided Adjusted EBITDA. **One of three ticked means Q3 would
have been a binary gate had the run reached it.**

**THE FIFTH FLAG FIRES, AND IT FIRES WHERE THE CGNX RULE SAID TO LOOK [E4-29].** The FY2025
10-K puts **"Adjusted EBITDA"** in the MD&A's own "Other financial data" line directly
under net income, at $278.2M and 19.2% of net sales. The EX-99.1 of 2026-07-09 goes
further: **four of the five headline bullets are non-GAAP** (Adjusted Diluted EPS, Adjusted
EBITDA), and **the forward outlook is stated in Adjusted EBITDA**: *"Adjusted EBITDA
expected to range between $220 and $225 million, or -21% to -19% year-over-year."* The
exclusion list is long: *"loss on impairment, stock-based compensation expense, executive
transition costs, business transaction costs, inventory step-up, integration expenses, term
loan transaction fees, and other non-core expenses."* **Stock-based compensation is
excluded**, which the corpus refuses outright **[E5-06]**, and so are the impairments, which
**[E5-33]** says belong in the owner-earnings mean. **This is a depreciation-deleting
measure applied to a business whose depreciation is small and whose AMORTISATION is the
running write-off of the brands it bought** — the reverse-float mechanism **[E5-41]** in its
purest form, because the money for those brands was spent in 2019 and 2024 and the expense
is being recorded now.

**The third flag fires with it [E4-22]:** the company guides, and the FY2026 outlook was
**updated** during the year, which is the projections flag plus **[E5-30]**'s ratchet. **The
action [E3-48] is to set past guidance against outturn**, and the partial record here is
that FY2026 guidance moved to a **6% to 7% net sales DECLINE** against an FY2025 that grew
9.0%. A full guidance-versus-outturn table is the named work order if this name is ever
reopened; the artifact is the EX-99.1 series, accessions 0001702744-26-000004,
0001702744-26-000010 and 0001702744-26-000021.

**[E2-49] metric-switching: CHECKED, NOT FIRED.** The headline metric carries the same
Adjusted EBITDA definition across the FY2024 10-K, the FY2025 10-K and the FY2026 releases,
including through the deterioration. The RESUME STATE records that prior at six fires and
five failures; **this is a sixth failure.** The yardstick was not disposed of when the
readings turned unfavourable.

**[E4-30] filed-figure tells: CHECKED, NOT FIRED.** Cash income taxes paid as a share of
pretax income, by fiscal year: 8.7%, 11.7%, 5.7%, 39.8%, 32.7%, 15.6%, 17.8%, **28.9%**.
The series RISES across the window. The tell is a FALLING cash-tax share, and it is absent.
Reported growth is also not unnaturally smooth: net income went 70.5, 47.5, 65.6, 40.9,
108.6, 133.6, 139.3, 103.6.

**[E2-01] the primary test, run as a series.** Return on book equity, FY2018 to FY2025:
**10.5%, 5.7%, 5.8%, 3.4%, 7.5%, 8.5%, 8.1%, 5.7%. It has never reached 11%.**
**The [E2-43] scoping is mandatory here and it cuts both ways.** This is an acquisitive
filer and the denominator is 73% goodwill and purchased intangibles, so book equity is
mostly **what was paid**, not what the managers have to work with. On unleveraged net
tangible assets the operating business earns enormously, because property and equipment is
$42.3M, and **[E2-73]** is the governing line: *"the managers of the units should be judged
by the returns they achieve on the underlying assets; what we pay for a business does not
affect the amount of capital its manager has to work with."* **So the 5 to 10 percent
series is a statement about the PRICES PAID for Quest and OWYN, not about the operators.**
The goodwill wedge, reported separately as the rule requires: tangible book equity at
2026-05-30 is **$1,418.1M less $1,508.9M of goodwill and intangibles = negative $90.8M.**

**[E5-08], [E2-52] and [E5-24]: the largest capital-allocation item in the file, and it is
live.** In the thirty-nine weeks to 2026-05-30 the company:
- repurchased **$213.2M** of its own stock, **11,651,767 shares**, treasury going from
  3,957,571 to 15,609,338; and
- **drew $150.0M of new term debt on 2025-11-19**; against
- **$102.2M** of cash from operations.

**Buybacks were 2.1 times operating cash flow and the gap was borrowed.** Condition (1) of
**[E5-08]** — *"ample funds to take care of the operational and liquidity needs of its
business"* — is the one to read, and **[E2-52]**'s form is the test: *"Beware of 'dividends'
that can be paid out only if someone promises to replace the capital distributed."* Here
the capital distributed was replaced by a lender.

**The corpus licenses exactly this conduct, and then fails it on the price test.**
**[E4-50]**: the wiser board buys *"very aggressively, using up all cash on hand and also
borrowing funds"*, and the framework's own gloss is that **the discount does the licensing,
never the borrowing**. So the only question is whether the discount was real. The filed
average prices are computable from the equity statement: **second quarter FY2026, 4,606,990
shares for $89.4M = $19.40 a share; third quarter FY2026, 2,061,263 shares for $25.3M =
$12.26 a share.** The stock closed at **$10.13** on 2026-09-18. **In the same nine months
the company wrote $331.0M off the carrying value of the brands.** **[E5-24]**: *"what is
smart at one price is dumb at another."* This is a **CAPITAL ALLOCATION FLAG**, stated with
the humility clause **[E4-13]**: it rests on my range and not theirs, and *"many CEOs never
stop believing their stock is cheap"* **[E5-08]**. **It binds position size and moves no
rate**, per the CONVENTION in section VI. Position size here is zero, so the flag has
nowhere to bind, which is itself worth noting as a limit of that convention on a closed
file.

**[E3-40] loss of focus, and [E2-56] the Pro-Am effect.** The clearest single number in this
run: **OWYN cost about $280M in June 2024, $223.0M of it booked as brand, and $200.0M of
the brand was written off by May 2026** — twenty-three months. Over the same period Atkins
takeaway fell 22.1% and Atkins marketing spend was cut by plan. *"Loss of focus is what most
worries Charlie and me when we contemplate investing in businesses that in general look
outstanding."* **[E2-56]** says to judge retention segment by segment and never on the
blended return; segment by segment, the capital retained and sent to OWYN has produced a
write-off and *"poor velocities."*

**[E2-30] the institutional imperative, scored.** (1) resists change in current direction:
not established; the company cut costs and changed CEO. (2) **projects or acquisitions
materialise to soak up available funds: TICKED** — the stated strategy is continuous
acquisition, in the 10-K's own words, and OWYN is the instance. (3) staff studies produced
to justify the leader's craving: not established from filings. (4) **peer behaviour
mindlessly imitated: arguable** — a plant-based RTD purchase at the top of the plant-based
cycle. **The last clause of [E2-30] governs and is repeated here: institutional dynamics,
not venality or stupidity. This is not a fraud test.**

**[E2-26] the half-owner test. Mostly PASSED, and I want to say so plainly.** Atkins'
decline is quantified brand by brand in both the 10-Q and the release; the distribution
losses are named as distribution losses rather than buried; the OWYN velocity failure is
stated in those words; the impairment triggers are disclosed including the embarrassing one
(*"largely the result of ... declines in stock price"*); the restructuring costs sitting
inside gross margin are given as **$6.2 million and a 180-basis-point headwind**; and the
Atkins impairment is carried as a critical audit matter. **A company hiding this would not
write "poor velocities, including on newly expanded distribution."** That is candid
reporting of a bad result, and **[E2-69]** says to judge deviations by direction.

**[E5-16] the binary: no integrity matter was found in these filings.** Recorded in the
framework's own form: **this is the absence of found disqualifiers, not a finding that the
managers are honest [E5-17].**

---
## Q4 ITEMS — RECORDED **[E5-11, E4-20, E4-43, E2-54, E3-52, E2-23, E3-44, E5-20, E4-25]**

**Owner earnings.** The full rebuild, every window, both (c) ends, is in "THE SCREEN ROW"
section 3 above and is not repeated. **The CONVENTION applied is the framework's own:**
operating cash flow less share-based compensation less the (c) guess. **No net-income proxy
appears anywhere in this file** (operator rule 5, PRIME RULE 3).

**(c) IS A DISCLOSED JUDGMENT AND HERE IS THE JUDGMENT [E2-23, E2-09, E3-44].** *"(c) must
be a guess."*

1. **The D&A default [E3-44, E2-41] runs the wrong way on this filer, and the SPGI question
   is why: ask what the D&A is actually made of.** FY2025 D&A of $21.4M is **$6.1M of
   depreciation and $15.1M of amortisation of purchased intangibles** (customer
   relationships, proprietary recipes, licensing agreements, software and website
   development). The amortisation is the unwinding of the Quest and OWYN purchase prices.
   **It is not a renewal cost of anything.** Charging it as (c) would charge the owner twice
   for acquisitions already paid for in cash and already sitting in the debt balance.
2. **This is not the [E5-20] capital-intensive exception either.** There are no railroads
   here: the company owns no manufacturing plant, capex ran $1.0M to $20.5M on revenue of
   $431M to $1,451M, and property and equipment is $42.3M of a $2,062.4M balance sheet.
3. **So the honest band for (c) runs from depreciation only, about $6M to $8M, to total
   capex, about $20M to $28M**, and all three columns are published above rather than one
   being chosen.
4. **And the guess must be disclosed as UNDERSTATED, because the corpus's words are
   "requires to FULLY MAINTAIN ... its unit volume."** At the current level of spend **unit
   volume is not being maintained**: retail takeaway is down 3.8% year to date and the
   company guides net sales down 6% to 7%. **The true (c) for this business is not a capex
   number at all; it is the advertising and trade spend needed to hold the facing, and the
   filed evidence is that what is being spent is not enough.** FY2025 selling and marketing
   was $134.3M, of which **57% was advertising** by the 10-K's own disclosure, and the line
   was **cut 6.7%** that year. **I cannot name the number that would hold volume. That is
   the guess, disclosed as a guess, and it makes every owner-earnings figure in this file an
   OVERSTATEMENT of what an owner could take out and leave the business standing still.**
   **[E2-60]** is the third dimension and it is failing in the other direction too: the
   payout, here a buyback, was part-funded by raising leverage.

**Great, good, or gruesome? [E4-20]** — **GOOD, tipping.** It is not gruesome: it does not
*"grow rapidly, require significant capital to engender the growth, and then earn little or
no money."* It is capital-light and converts revenue to cash at roughly 10% of sales.
**[E4-43] is the governing scope note: the good class PASSES Q4, and only the gruesome
fails it.** **So Q4 would not have closed this file; Q2 did.** That distinction matters for
the register: **SMPL fails on the franchise, not on survival.**

**Staying power, all three scored [E5-11].**
1. **A large and reliable stream of earnings** — large, yes; **reliable, no.** Adjusted
   EBITDA guided down 19% to 21%, net sales guided down 6% to 7%, gross margin guided down
   375 basis points, and the nine-month GAAP result is a **$186.4M net loss**.
2. **Massive liquid assets** — **$123.9M of cash** at 2026-05-30 and **$73.9M undrawn** on
   the revolver ($75.0M less $1.1M of letters of credit). Adequate; not massive.
3. **No significant near-term cash requirements** — **this one is genuinely clean, and it is
   the one that usually kills.** The 10-Q states: *"The Company is not required to make
   principal payments on the Term Facility over the twelve months following the period ended
   May 30, 2026. The outstanding balance of the Term Facility is due upon its maturity in
   March 2030."* The revolver runs to December 2029. **The November 2025 amendment bought
   three years of runway at the same moment it funded the buyback**, and whatever the second
   half of that decision is worth, the first half removed the near-term cliff. **[E5-39]**
   is satisfied on its own terms: nothing here depends on the kindness of strangers inside
   twelve months.
- **Leverage, named and quantified [E4-16, E3-29], with no ratio ceiling applied because
  the framework has none:** Term Facility **$400.0M** at an effective **5.7%**, floating at
  SOFR plus 200 basis points with a 0% floor; cash $123.9M; **net debt $276.1M**, against
  guided FY2026 Adjusted EBITDA of $220M to $225M, **roughly 1.25 times**. **[E2-54]**'s
  coverage test: interest was $15.9M over thirty-nine weeks against $102.2M of operating
  cash flow with $10.1M of capex taken out first. **Comfortably met out of current cash
  flow net of capital expenditures**, which is the exact form of the test. **[E3-52]**:
  these are covenanted bank borrowings with a named maturity, not covenant-free float, so
  they are read strictly and not discounted.

**Name the specific way THIS business dies [E2-27, E3-24, E4-40].**
**The mechanism: the Atkins path, run again on Quest.** A nutritional-snacking trademark is
a lease on a diet fashion and on a set of shelf facings. When the fashion moves, retail
takeaway falls; when takeaway falls, the retailer cuts facings at the next planogram reset;
when facings are cut, takeaway falls further. **The registrant already contains the worked
example.** Atkins went from the brand the company is named after to **minus 22.1% takeaway
and $153.9M of cumulative brand write-down in two years.** OWYN shows the loop can start
without any fashion shift at all: expanded distribution, poor velocity, $200.0M written off
in twenty-three months.
**Quantified from filed figures.** Quest is now the majority of the company. FY2026 guided
net sales are $1.345bn to $1.355bn. If Quest were to repeat Atkins' trajectory of about
minus 22% a year for three years while Atkins continues at minus 20% and OWYN stays flat,
group net sales would approach **$700M** with gross margin at or below today's 32.2%; gross
profit would fall from roughly $435M to roughly $225M, against FY2025 operating expenses
excluding impairment of about **$308M**. **The company would be loss-making at the operating
line before any restructuring**, with $400.0M of debt due March 2030.
**One UNRESEARCHED item, named:** the Credit Agreement's financial covenant levels are not
quantified in the 10-Q text; the artifact is the Credit Agreement exhibit to the 8-K of
2025-11-20, accession 0001104659-25-114309. **This is a work order, not a gate verdict, and
it does not change the Q2 close.**
**Likelihood: [x] a real possibility.** Not *likely*: Quest takeaway is currently **growing
5.1%**, which is the direct evidence against the mechanism firing now. Not *a low-level
possibility*: the same company has already run this exact sequence to completion on one
brand and is two years into it on a second.
**And the corpus's named failure mode for this very exercise, [E4-40]: model exposure, not
experience.** Quest's benign recent history is the thing most likely to mislead here. The
exposure is that **a single retailer is 31% of sales on an at-will contract with no minimum
purchase amounts**, and that exposure does not shrink because nothing has happened yet.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

**Q1 through Q4 do not all show IN. The file closed at Q2. Nothing below is an entry, a
ranking, a recommendation or a clearance, and no entry language appears in it.** It is
recorded so that the register carries a price and so that the reversal condition at Q6 has
a number attached to it.

- Market cap: **$10.13 x 88,460,545 = $896.1M**. Net debt $276.1M. Enterprise value
  approximately **$1,172M**.
- Sovereign: **5.34%**, the bare rate, no per-name premium added **[E3-42]**.

| owner-earnings window | OE ($M) | yield on $896.1M of equity value |
|---|---|---|
| TTM to 2026-05-30, c = total capex | 103.8 | **11.6%** |
| TTM to 2026-05-30, c = D&A | 107.9 | **12.0%** |
| TTM to 2026-05-30, c = depreciation only | 123.5 | **13.8%** |
| 8-year mean FY2018-FY2025, c = D&A | 98.0 | 10.9% |
| 8-year mean, c = depreciation only | 111.2 | 12.4% |
| 5-year mean FY2021-FY2025, c = D&A | 127.9 | 14.3% |

- **Points over the sovereign**, trailing, at the c = D&A end: 12.0% less 5.34% = **6.7
  points**.
- **What the price already assumes:** at 12.0% trailing the quote requires **no growth at
  all**, and is consistent with a permanent decline of a few percent a year. The screen's
  `growth_required` of **-0.0323** said the same thing from its own band and is confirmed.
- **What the business has actually done:** FY2026 is guided to **minus 6% to minus 7%** net
  sales, minus 375 basis points of gross margin, and minus 19% to minus 21% of Adjusted
  EBITDA. Price and outturn are in roughly the same place, which is why this is not a
  screamer **[E4-01]**: the range sits INSIDE the price rather than below it, and the
  corpus's own middle outcome is *"no useful conclusion, move on."*
- **Windage count: ONE.** Conservatism is spent once **[E4-11, E4-48]**. It is spent in the
  disclosed Q4 statement that **(c) is understated**, because the business is not holding
  unit volume at current spend. No second margin is applied anywhere, no risk premium was
  added to the 5.34% **[E3-42]**, and the yields above are stated BEFORE that single
  conservatism, not after.
- **THE FLOOR VERDICT, recorded rather than applied [E4-28].** The honest pre-tax expectancy
  at this price on trailing owner earnings is **approximately 12%**, which is **above** the
  corpus's ~10% figure-we-quit-on. **THAT DOES NOT PROMOTE THIS NAME.** Q5 cannot open on a
  file closed at Q2, and the corpus states the reason as a law **[E5-35]**: *"You can turn
  any investment into a bad deal by paying too much. What you can't do is turn any
  investment into a good deal by paying little."* **[E2-38]** is the same thing in pictures:
  *"Good jockeys will do well on good horses, but not on broken-down nags."*
- **What bounds the upside, named [E2-63, E4-44]:** the whole of this is a lease on shelf
  facings at two retailers, and value cannot over the long term grow faster than earnings.
  **[E3-17]** is the qualifier that matters most for a name this cheap: over decades the
  business return converges on the owner, so an entry discount does not rescue a declining
  unit series held for ten years.
- **VERDICT: [ ] IN  [ ] NOT IN — QUIT ON  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  **NO BOX IS TICKED. Q5 WAS NOT REACHED AND THE ARITHMETIC ABOVE CASTS NO VOTE.**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

No position is taken, so there is nothing to sell. **[E1-02]** still applies to the
reversal, written before the fact: *"I believe in establishing yardsticks prior to the
act."*

**WHAT WOULD PROVE THE Q2 OUT WRONG — pre-committed, and it is a unit test, not a price test
[E4-55, E4-32, E2-44]:**
1. **Quest retail takeaway holds positive for four consecutive quarters WHILE gross margin
   recovers above 36%.** That combination, and only that combination, would say the company
   can pass cost through, which is the criterion (2) evidence currently absent. Takeaway
   alone does not do it; margin alone does not do it.
2. **A price increase taken and held**, stated in an MD&A as price/mix positive with volume
   not falling to pay for it. **[E2-44]** is the exact test and it is currently failing.
3. **Atkins takeaway decline decelerating to single digits**, which would say the brand has
   a floor rather than an asymptote.
- **Threshold and window: all three, read on the FY2027 10-K and the four EX-99.1 releases
  that precede it.** Next catalyst: the **FY2026 10-K, expected late October 2026**, which
  will carry the fourth-quarter impairment test and the FY2027 outlook.

**WHAT WOULD CONFIRM IT:** Quest takeaway turning negative; or a second consecutive year of
brand impairment; or the loss of a Walmart or Amazon line.

**The monitoring question [E3-30, E4-17]:** *is this erosion part of an aberrational cycle,
or has the business slipped in a way that permanently reduces intrinsic business values?*
**Answered in this run as permanent for Atkins and OWYN and open for Quest.** The corpus is
right that beliefs about moats change gradually; this one has the advantage that the same
company already ran the experiment once and published the result.

**Position size: ZERO.** No alert band is armed and no `PORTFOLIO.md` row is added, per the
QLYS ruling of 2026-09-07: **a name that failed on the BUSINESS gets no price alert, because
a price alert on it is a category error.** The reversal condition is recorded in words
above.

- **VERDICT: [x] OUT** — the file is closed at Q2, on the business. Q6 records the reversal
  condition rather than an exit.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, stop. Q3 and Q4
      recorded without verdicts; Q5 headed COMPUTATION — NOT A CLEARANCE with no box ticked.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests
      on the 10-K and the 10-Q read directly. The competitor row is complete enough that the
      moat class is NONE rather than PROVISIONAL, and the reason is stated in the row.
- [x] Every UNRESEARCHED item names the artifact and where it lives. Two are named: the
      Credit Agreement financial covenant levels (exhibit to 8-K accession
      0001104659-25-114309) and the full guidance-versus-outturn table (EX-99.1 series,
      accessions 0001702744-26-000004, -000010, -000021). **Neither is a gate verdict.**
- [x] No UNKNOWABLE verdict was written.
- [x] Step 0: the filings were read, with accession numbers, and **two figures were
      cross-checked against the filed statements** (Term Facility $400,000k reconciling to
      $397,037k on the balance sheet; 104,050,545 less 15,609,338 reconciling to the cover's
      88,460,545).
- [x] Owner earnings on a multi-year mean and never via a net-income proxy; **four windows
      and three (c) ends published**; (c) disclosed as a judgment and disclosed as
      understated.
- [x] Competitor row filled, five companies, every figure computed by me from filings, with
      the unavailable peers named and their obstacle stated.
- [x] Sovereign is USD for a USD earner, from the US Treasury, dated 09/18/2026, struck this
      session.
- [x] Value stated as a range, not a point estimate, and headed as a computation.
- [x] One bar chosen: neither, because Q5 did not open. Windage count stated: **one**.
- [x] Prices dated; the aggregator was used for the live quote only and is FLAGGED.
- [x] Every judgment carries a ledger id, and every id cited was checked to exist in
      `principle_ledger.csv` before it was written.
- [x] `python tools/check_framework.py` run before the fold commit.
- [x] Run committed to git, with a pathspec, at each stage.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** A three-brand nutritional-snacking company trading at roughly a 12% trailing
  owner-earnings yield, closed at Q2 because its own filings show one brand losing 23.9% of
  retail takeaway to distribution cuts, a second losing velocity on distribution it had just
  gained, and 470 basis points of gross margin lost to input costs it could not pass on,
  which is criterion (2) of **[E3-03]** failing on the company's own evidence.
- **The cap flag resolved:** the cap was right, the price had fallen 73% since the cover
  float was struck, and the screen compared a September 2026 cap with a February 2024 float.
- **The acquisition flag resolved:** there was no net cash inflow. The XBRL sign for
  `PaymentsToAcquireBusinessesNetOfCashAcquired` flipped between the FY2024 and FY2025
  vintages and the screen summed the negatives.

## RUN LOG
- Sovereign struck 2026-09-20 from the US Treasury daily par yield curve: **5.34%, dated
  09/18/2026**.
- Price struck 2026-09-20: **$10.13, close of 2026-09-18**, aggregator, FLAGGED.
- Filings read: 10-K 0001702744-25-000046; 10-Q 0001702744-26-000023; 8-K EX-99.1
  0001702744-26-000021; 8-K 0001104659-25-114309; 8-K 0001104659-26-005379; 8-K
  0001104659-26-045701; 8-K 0001104659-24-072273 (referenced).
- Peer filings read: BRBR (CIK 0001772016), MED (0000910329), HLF (0001180262), CELH
  (0001341766).
- EDGAR full-text sweep run 2026-09-20, 10-K forms, 2024-09-01 to 2026-09-20, five terms.
- Research folder: `Test Runs/_research 2026-09-20 SMPL/`.
