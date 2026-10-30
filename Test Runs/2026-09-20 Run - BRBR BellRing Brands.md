# Company Run — BELLRING BRANDS, INC. (BRBR) — 2026-09-20
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
## STEP 0 — THE RATE, THE FILING, AND THE THREE LIVE FLAGS

**Sovereign, for the currency the business EARNS in** -- the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **09/18/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck in this run with `python tools/sources.py` at 21:49 EDT on
  2026-09-20. FRED is the fallback and was not used.
- FX: none needed. **88.1% of FY2025 net sales were U.S.** (FY2025 10-K, Item 1, "Our
  Customers"); the filer reports in USD and the quote is USD on the NYSE.

**The filing was read** -- not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the fiscal year ended 2025-09-30, filed
  2025-11-18, accession 0001772016-25-000153** (the newest annual report actually FILED; the
  FY2026 year does not end until 2026-09-30). Superseded in part by the **Form 10-Q for the
  quarter ended 2026-06-30, filed 2026-08-04, accession 0001772016-26-000022**, which is
  where the current share count and the nine-month FY2026 income statement come from. Also
  read: the FY2022 10-K (accession 0001772016-22-000061, filed 2022-11-17) for the
  perimeter and the FY2022 cash-flow statement, and four consecutive 8-K EX-99.1 earnings
  releases (2025-11-18, 2026-02-03, 2026-05-05, 2026-08-04).
- figure cross-checked against the filed statement: **FY2022 net cash provided by operating
  activities of $21.0 million.** XBRL `NetCashProvidedByUsedInOperatingActivities` for the
  period ended 2022-09-30 reports 21,000,000; the filed Consolidated Statements of Cash
  Flows in the FY2022 10-K reads "Net Cash Provided by Operating Activities 21.0". They
  agree. A second cross-check: XBRL `GrossProfit` FY2025 770,400,000 against the filed
  Consolidated Statements of Operations, which reads $770.4. They agree.

### FLAG (i) — `cap_flag`. RESOLVED AGAINST THE SCREEN'S INFERENCE. The cap is right, the float is right, and the gap is an 88% price collapse.

The screen said: *"CAP BELOW FILED PUBLIC FLOAT - cap $1,243M against a filed float of
$9,368M (7.54x) as of 2025-03-31. A cannot be smaller than a subset of itself. One of the
two is wrong - RE-STRIKE THE CAP BY HAND."* Both halves of the screen's arithmetic are
correct and neither number is wrong. **They are seventeen months apart.**

- **The float figure is real and I have read it on the cover.** FY2025 10-K cover,
  accession 0001772016-25-000153: *"The aggregate market value of the registrant's Common
  Stock held by non-affiliates of the registrant as of March 31, 2025 , the last business
  day of the registrant's most recently completed second fiscal quarter, was
  $ 9,367,938,437 ."* That is a **point-in-time** figure fixed by Item 12b-2 at the last
  business day of the second fiscal quarter, and BRBR closed at **$74.46 on 2025-03-31**.
- **How many classes are registered, read from the cover as instructed.** FY2025 10-K:
  *"Securities registered pursuant to Section 12(b) of the Act: Title of each class Trading
  Symbol(s) Name of each exchange on which registered Common Stock, $0.01 par value BRBR
  New York Stock Exchange"* and, on the next line, *"Securities registered pursuant to
  Section 12(g) of the Act: None"*. **Exactly ONE registered class. There is no second
  class to add.** The dual-class structure that existed under Old BellRing was eliminated
  at the Spin-off (see flag (iv)); the FY2025 10-K says so: *"As a result of the Spin-off,
  the dual class voting structure of Old BellRing was eliminated."*
- **THE CAP, RE-STRUCK BY HAND.** `cap = close(anchor) x shares(measurement) x splits AFTER
  measurement`.
  - shares(measurement): **116,278,194**, from the **cover of the newest periodic filing**,
    the 10-Q for the quarter ended 2026-06-30, accession 0001772016-26-000022: *"Common
    Stock, $0.01 par value per share – 116,278,194 shares as of July 28, 2026"*.
  - splits after 2026-07-28: **none.** The chart endpoint returns `events: None` over a
    ten-year range and BellRing has never split; raw response saved to
    `quote_BRBR_splits.json`.
  - close(anchor): **$8.98 on 2026-09-18**, the last regular session before this run.
    **AGGREGATOR, FLAGGED** -- Yahoo Finance chart API, live quote only, raw response saved
    to `Test Runs/_research 2026-09-20 BRBR/quote_BRBR_raw.json`. Used `close`, never
    `adjclose`.
  - **cap = 116,278,194 x $8.98 = $1,044,178,182, i.e. $1,044M.**
- **The screen's $1,243M is the same number a few weeks stale** (it implies $10.69 on
  116.28M shares; BRBR closed at $10.77 at the end of August 2026). It is not a units error
  and this is **not** the MCFT branch of this flag, where the extractor was wrong by 1000x.
  It is the CALM/EMBC branch: the cap is broadly right and the comparison was not
  like-for-like.
- **What the flag actually found is the single most important fact on this page.** Monthly
  closes: **$77.14 (2025-04), $57.93 (2025-06), $36.35 (2025-09), $24.87 (2026-01), $16.09
  (2026-03), $8.36 (2026-05), $8.98 (2026-09-18).** From the float measurement date to today
  the equity has lost **88%** of its value. A screen row whose cap and float disagree by
  7.5x is, here, a screen row reporting a catastrophe. **No yield is reported anywhere in
  this file before Q1-Q4 close; the yields the screen carried (`yield_bottom` 0.1115,
  `vs_sovereign` 0.058, `growth_required` -0.0115) were computed on $1,243M and all move
  with the cap.**

### FLAG (ii) — `wc_note`. THE ARITHMETIC IS EXACT, THE SIGN IS RIGHT, AND THE LINE IS THE THIRD-LARGEST, NOT THE LARGEST. The implication is inverted.

The screen said: *"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 49% of
2022 OCF."* From the filed Consolidated Statements of Cash Flows in the **FY2022 10-K,
accession 0001772016-22-000061**, fiscal year ended 2022-09-30, OCF **$21.0M**, every
working-capital line as a fraction of that year's operating cash:

| line, verbatim from the filed statement | FY2022, $M | as % of FY2022 OCF | direction |
|---|---|---|---|
| "(Increase) decrease in inventories" | **(83.9)** | **399.5%** | **CONSUMED cash -- LARGEST** |
| "Increase in receivables" | **(70.7)** | **336.7%** | **CONSUMED cash -- second** |
| "Increase (decrease) in accounts payable and other current liabilities" | **10.3** | **49.0%** | provided cash -- **third** |
| "Decrease in other assets" | 2.3 | 11.0% | provided cash |
| "Decrease (increase) in prepaid expenses and other current assets" | 1.1 | 5.2% | provided cash |
| "(Decrease) increase in non-current liabilities" | (0.2) | 1.0% | consumed cash |

- **Reproduced to the decimal: 10.3 / 21.0 = 49.05%.** The screen's 49% is exactly right and
  the sign is right; payables did provide cash.
- **But the flag names the third-largest line, and its premise is inverted here.** The two
  largest lines are five and seven times bigger than the one the flag named, and **both
  consumed cash**. A $154.6M working-capital build is why FY2022 OCF is $21.0M. **FY2022
  operating cash is DEPRESSED by working capital, not flattered by it.** The instruction
  "operating cash is not owner earnings when one balance-sheet line produced it" does not
  bite in the direction the flag intends; if anything the caution runs the other way, and
  FY2022 is the year a multi-year mean should be checked for **under**statement.
- **What caused it, from the liquidity discussion in the same 10-K** (MD&A, "Fiscal 2022
  compared to 2021"), verbatim: *"The decrease was primarily driven by unfavorable changes
  related to an increase in inventory and fluctuations in the timing of sales and
  collections of trade receivables and purchases and payments of trade payables. Inventory
  increases were driven by input cost inflation, increased powder finished goods due to
  rebuilding inventory from supply-constrained levels at prior fiscal year end and
  increased raw material levels. Additionally, tax payments (net of refunds) increased by
  $22.6 million and interest payments increased by $9.3 million."*
- **Tooling defect, recorded for the fold.** This is now the **third** run in which this
  flag named a line that is not the largest working-capital mover (EMBC, MCFT, BRBR). The
  defect is in which line the extractor selects, not in its arithmetic, which is exact in
  all three cases.

### FLAG (iii) — `spread_caveat`, the [E4-25] rebuild. THE RECORD IS 8 YEARS AND I USE ALL OF IT, WITH THE PERIMETER CUT MARKED.

`years_filed` 8 is right. **Seven consecutive 10-Ks exist under CIK 0001772016** -- FY2019
(0001772016-19-000038) through FY2025 (0001772016-25-000153) -- and because each carries
three comparative years, the FY2020 10-K reaches back to **fiscal 2018**. The continuous
operating-cash series is therefore FY2018 through FY2025, **eight fiscal years**, and I
rebuild the window over all eight rather than the screen's 4-construction (3-year and
5-year means crossed with two capex ends). The record is shorter than the business because
the business did not file separately before Post's October 2019 IPO of Old BellRing; the
brands sat inside Post from 2013-2015. **Where the eight-year and five-year windows
disagree, both are reported at Q4 and the disagreement is itself the finding [E4-25,
E4-38].**

### FLAG (iv) — THE PERIMETER. `name_change_note` AND `deal_note` ARE BOTH EMPTY AND BOTH CLAIMS ARE FALSE. There is a registrant substitution in the middle of the series.

Established from the filings, with dates and accession numbers. Source: **FY2022 10-K Note 1
-- BACKGROUND, accession 0001772016-22-000061**, and **FY2025 10-K Item 1, accession
0001772016-25-000153**.

- **The predecessor registrant** is **BellRing Intermediate Holdings, Inc., formerly known
  as BellRing Brands, Inc. ("Old BellRing")**, which *"closed its initial public offering
  … of 39.4 million shares of its Class A common stock"* on **2019-10-21** and first traded
  on the NYSE on **2019-10-17**. Old BellRing was an Up-C holding company: it *"had no
  material assets other than its ownership of BellRing LLC units"*, Post held *"71.5 % of
  the economic interest in BellRing LLC"* and one Class B share carrying *"67 % of the
  combined voting power"*.
- **The separation completed 2022-03-10.** Post contributed its Class B share, all its
  BellRing LLC units and *"$ 550.4 of cash"* on **2022-03-09** in exchange for *"$ 840.0 in
  aggregate principal amount of BellRing's 7.00% Senior Notes"*; on **2022-03-10**
  *"BellRing converted into a Delaware corporation and changed its name to 'BellRing Brands,
  Inc.'"* and Post distributed *"78.1 million, or 80.1 %, of its shares"*. Merger Sub merged
  into Old BellRing and each Old BellRing Class A share became one new share **plus $2.97 in
  cash, $115.5 million in total**.
- **Is the CIK that files today the same one that filed the earliest annual report in the
  series? YES, and the filing itself says why:** *"BellRing became the new public parent
  company of, and successor issuer to, Old BellRing, and shares of BellRing Common Stock
  were deemed to be registered under Section 12(b) of the Securities Exchange Act of 1934,
  as amended, pursuant to Rule 12g-3(a) promulgated thereunder."* CIK 0001772016 and
  Exchange Act file number 001-39093 carry across the substitution. `formerNames` in EDGAR's
  submissions JSON is empty, which is why the screen's `name_change_note` came up blank:
  **EDGAR recorded a successor issuer, not a name change, and the screen's name-change
  detector cannot see a Rule 12g-3(a) substitution.** That is a tooling defect and it is
  recorded for the fold.
- **Are the historical statements carve-out/combined or standalone?** Neither label is
  clean and the honest answer is a third one. The **operating perimeter is continuous**:
  the FY2025 10-K defines "BellRing" as *"(1) Old BellRing and its consolidated subsidiaries
  during the periods prior to the … Spin-off, including BellRing LLC, Premier Nutrition …
  Dymatize …, Supreme Protein …, the PowerBar brand and Active Nutrition International"*
  and *"(2) us and our consolidated subsidiaries during the periods subsequent"*. The same
  brands, the same LLC, throughout. The FY2022 statements are audited consolidated
  statements of Old BellRing and then of BellRing, not carve-outs. **What breaks is the
  CLAIM ON THE CASH, not the cash.** Before 2022-03-10, Post owned 71.5% of the economics of
  BellRing LLC: the FY2022 filed cash-flow statement begins at *"Net earnings including
  redeemable noncontrolling interest $ 116.0"* while *"Net earnings available to common
  stockholders"* for the same year was **$82.3**, and FY2021's were $114.4 and $27.6.
  **Consolidated operating cash flow is comparable across the break because it is the same
  operating business; per-share and bottom-line figures before FY2022 are not, because up to
  71.5% of them belonged to Post.**
- **THE CUT I MAKE, AND WHY.** Owner earnings here is built on **consolidated operating cash
  flow less SBC less the (c) guess**, which is the whole business's cash, so the
  **eight-year OCF series is a series and I carry it whole**. Any *per-share* or
  *net-earnings-based* reading of FY2018-FY2021 is **cut at 2022-03-10** and not used. A
  multi-year owner-earnings mean built across a perimeter break is not a series; here the
  break is in the ownership of the earnings, not in the earnings, and that is the
  distinction the cut records rather than smooths. Capital structure across the break is a
  fact about the Spin-off and not about the business: **$840.0M of 7.00% Senior Notes were
  issued to Post as consideration, not to fund anything the business needed**, which is read
  at Q4.
- **Subsequent perimeter moves:** the FY2025 post-Spin definition of the company adds
  **Premier Nutrition Canada, Inc.** and **drops the PowerBar brand** from the pre-Spin
  list. Both are immaterial against $2,316.6M of FY2025 net sales; no acquisition or
  disposition in the window is large enough to break the OCF comparison, and the screen's
  empty `acq_note` is correct on that narrow point even though its empty `deal_note` is not.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language.** BellRing owns two trademarks
  and almost nothing else. It buys milk-based and whey-based protein and it buys plastic
  bottles, hands both to third parties who fill, sterilise and pack them, and pays those
  third parties **a per-unit tolling charge**. The finished cases go from the packer's dock
  to third-party warehouses and then to three retailers. FY2025 net sales $2,316.6M, cost
  of goods sold $1,546.2M, gross profit $770.4M (33.3%). **Capital expenditure guided at $10
  million on $2.3 billion of sales**, i.e. four tenths of one percent, because the plants
  belong to somebody else. The margin is the gap between what Walmart, Costco and Amazon
  will pay for a branded 11-ounce shake and what the protein, the bottle and the tolling
  charge cost. There is no third source of income. From the FY2025 10-K, Item 1,
  "Manufacturing": *"We primarily engage third-party contract manufacturers in North America
  and the European Union … to produce our products. We receive products from our third-party
  contract manufacturers for an agreed-upon tolling charge for each item produced."* The one
  plant it owns is in **Voerde, Germany** and makes bars and gels for Europe.
- **Product mix, from the filed disaggregation note in the 10-Q for the quarter ended
  2026-06-30 (accession 0001772016-26-000022):** nine months to 2026-06-30, Shakes
  **$1,374.4M (80.5%)**, Powders $284.9M (16.7%), Other $47.1M (2.8%). **This is a
  ready-to-drink shake company with a powder business attached.**
- **The scarce input this business controls.** The honest answer is **the Premier Protein
  trademark and the shelf and club-floor position it has bought with it, and that is all.**
  Everything physically scarce in the chain is controlled by somebody else, and the 10-K
  says so in one paragraph: *"one supplier for the majority of our milk-based protein"*;
  *"approximately 46.3% of our Premier Protein RTD shake supply came from our largest
  third-party contract manufacturer, with approximately 28.0% of our Premier Protein RTD
  shake supply manufactured at a single facility"*; and for the flagship 11-ounce pack,
  *"packaging that we currently are sourcing from only one supplier, and equipment that our
  third-party contract manufacturers are currently sourcing from the same supplier."* One
  protein supplier, one bottle supplier, one contract manufacturer at 46.3% -- and on the
  other side, *"Our largest customers, Walmart (which includes its affiliates, including
  Sam's Club), Costco and Amazon, accounted for approximately 74.0% of our net sales in our
  year ended September 30, 2025."*
- **Will the fundamentals look broadly the same in ten years?** Yes, and that is what makes
  this gate pass rather than fail. People will still drink protein shakes; shakes will still
  be filled by somebody, sold by somebody, and bought in a club store. The business is
  *"relatively simple and stable in character"* **[E3-31]** -- a brand, a co-packer, a
  retailer. There is no technology to forecast and no regulated tariff to guess. **What I
  cannot forecast is the SPLIT of the margin among the three parties, and that is a Q2
  question about position, not a Q1 question about comprehension.** Under **[E4-46]** the
  distinction matters: this is not a business that would take five months to learn.
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** · no close substitute **[ ] -- FAILS** · not price-regulated **[x]**
- **Must the moat be continuously rebuilt? Does success depend on a great manager?
  [E4-04]** -- **No on both, and this is NOT where the file closes.** Advertising spend on a
  trademark **defends the same advantage** rather than buying its replacement, which is the
  scope test the framework sets out: Coca-Cola's advertising, not Mitsui's Rhodes Ridge. A
  lapse would narrow the position, not destroy it. And the durability of a protein brand is
  judgeable from filings, so this is not the perimeter close either. **[E4-04] is applied as
  a competence limit and it does not bite here. The failure below is [E3-03] criterion (2),
  on the subject's own filed numbers.**
- **Primary moat metric, filing-sourced, and its trend: gross margin, at the company's own
  definition, from its own filed statements of operations.**
  FY2018 33.6% · FY2019 36.5% · FY2020 34.2% · FY2021 31.0% · FY2022 30.8% · FY2023 31.8% ·
  FY2024 35.4% · FY2025 33.3% · **nine months to 2026-06-30 28.5%**, against 34.9% in the
  matched prior-year nine months. **Direction: down 647 basis points in twelve months, and
  the quarterly path inside FY2026 is 29.9%, 27.0%, 28.6% -- the lowest three quarters in the
  eight-year record.** **[E4-32]** makes direction *"the primary criterion of a great
  business"*, and this direction is the wrong one.

### THE COMPETITOR ROW — required [E3-28]

Every figure computed by me from the named filing, at each filer's own gross-margin
definition, **matched at the calendar quarter ended 2026-06-30** because that is the window
in which the subject broke. SMPL's fiscal quarter ends a month earlier and is used at its
closest available dates, stated. Abbott is taken at its **Nutritional Products segment**,
which is the only place in the row where a direct Ensure-versus-Premier-Protein comparison
is filed.

| Company | quarter | gross margin | prior-year quarter | change | source |
|---|---|---|---|---|---|
| **BRBR (subject)** | 3m to 2026-06-30 | **28.6%** | **35.4%** | **-680 bp** | 10-Q, accession 0001772016-26-000022 |
| **Simply Good Foods (SMPL)** | 13wk to 2026-05-30 | 32.5% | 36.4% *(13wk to 2025-05-31)* | **-390 bp** | 10-Q, accession 0001702744-26-000023 |
| **Celsius (CELH)** | 3m to 2026-06-30 | 48.1% | 51.5% | **-340 bp** | 10-Q, accession 0001341766-26-000050 |
| **Medifast (MED)** | 3m to 2026-06-30 | 69.9% | 72.6% | **-270 bp** | 10-Q, accession 0001628280-26-051928 |
| **Abbott -- Nutritional Products segment (ABT)** | 3m to 2026-06-30 | **46.5%** | 47.8% | **-130 bp** | 10-Q, accession 0001628280-26-050134, Note 15 Segment Information |
| **Post Holdings (POST)** | 3m to 2026-06-30 | **29.1%** | 30.1% | **-100 bp** | 10-Q, accession 0001530950-26-000077 |
| **Herbalife (HLF)** | 3m to 2026-06-30 | 77.7% | 78.0% | **-30 bp** | 10-Q, accession 0001193125-26-335172 |

And the nine-month view, where the subject's fiscal calendar and Post's are **identical**
(both fiscal years end 30 September), so this pair is an exact like-for-like:

| | 9m to 2026-06-30 | 9m to 2025-06-30 | change |
|---|---|---|---|
| **BRBR** | **28.5%** ($485.8M on $1,706.4M) | 34.9% ($583.0M on $1,668.4M) | **-647 bp** |
| **POST** | **29.6%** ($1,822.4M on $6,165.5M) | 29.4% ($1,737.3M on $5,911.1M) | **+17 bp** |

- **Cross-checked against the filed statements, not the XBRL.** BRBR: the Condensed
  Consolidated Statements of Operations in the 10-Q read *"Net Sales $ 570.4 … $ 1,706.4 …
  Cost of goods sold 407.1 … 1,220.6 … Gross Profit 163.3 … 485.8"*. POST: *"Net Sales
  $ 1,948.0 $ 1,984.3 $ 6,165.5 $ 5,911.1 Cost of goods sold 1,381.7 1,388.1 4,343.1
  4,173.8 Gross Profit 566.3 596.2 1,822.4 1,737.3"*. Both agree with the computed figures.
- **Peers named: 6, of the industry's roughly 11 real competitors.** Buffett says eight
  **[E3-28]**; six are computable and five are not, and I name each obstacle rather than
  leave the row short in silence.
- **Peers I could NOT compute, with the named obstacle for each.**
  **(1) Private label and store brands** -- the first competitor the FY2025 10-K names
  (*"We compete with other brands, including private label and store brand products"*) and
  it files nothing. **(2) Fairlife / Core Power** -- wholly owned by The Coca-Cola Company
  and not disclosed as a segment or a line item; ladder rung "SEC EDGAR primary documents"
  reached, figure not present. **(3) Nestlé Health Science (Boost, Optifast)** -- Swiss, not
  an EDGAR filer, and Nestlé's own reporting does not segment to a comparable line; rung
  "exchange filings" reached, no comparable metric published. **(4) Optimum Nutrition /
  Glanbia** -- Irish, listed in Dublin and London, not an EDGAR filer; and it is the more
  important absence because Glanbia is simultaneously a **competitor in powders and a
  supplier of whey protein**, so it sits on both sides of the subject's income statement.
  **(5) The contract manufacturers themselves, which is the absence that matters most** --
  the FY2025 10-K never names the manufacturer that makes 46.3% of Premier Protein RTD
  shakes, nor the *"one supplier"* of milk-based protein, nor the sole 11-ounce bottle
  supplier. They are private. **Their tolling charge is a line I cannot see and cannot
  compute, and it is the line that decides this company's margin.**
- **The moat class is NOT held PROVISIONAL on those five absences**, because the verdict is
  OUT and not IN: every missing peer could only make the subject look relatively better, and
  criterion (2) already fails on the subject's own filings before any peer is consulted. The
  row is here to test a relative claim that the subject's own numbers have already refused.
- **WHAT THE ROW SHOWS, AND IT IS NOT WHAT THE SMPL RUN WROTE DOWN.** See the section below.
- **The row's limit, stated [E3-61]:** *"In some businesses, the participants behave like a
  demented Kellogg. In other businesses, they don't … I think you'd have to know the people
  involved."* The row shows position. It cannot tell me whether Premier Protein's 4.7%
  nine-month price/mix give-back was forced by the retailer or chosen by the manager to buy
  distribution, and the corpus says even Munger had no model for predicting that.
- **An absence, worded as the absence-claim rule requires.** A recorded sweep was run on
  2026-09-20 against EDGAR full-text search, form 10-K, 2024-09-01 to 2026-09-20, for the
  phrase `"Premier Protein"`. **Four hits, and no instance was found of any competitor's
  10-K naming the brand:** two are BellRing's own FY2024 and FY2025 10-Ks, and two are Post
  Holdings' FY2024 and FY2025 10-Ks, which name it because Post is the former parent and a
  co-packing counterparty. Raw response saved to `fts_premier_protein.json`. **Weight it
  low** -- the SMPL run's mirror-image sweep found the same convention running the other way,
  so not naming rivals is how this industry files and the absence says little either way. It
  is recorded because it was looked for.

### THE SMPL PRIOR, REPRODUCED AND THEN NARROWED. A FINDING THE SMPL FOLD IS OWED.

The SMPL run (register entry 135) recorded, from outside this company: *"The closest listed
peer, BellRing (BRBR), lost 640bp of gross margin in the same window on +2.3% sales against
SMPL's -5.4%, so the pass-through failure is a category fact and [E2-58]'s equation is
operating on the layer beneath the trademarks."*

- **The arithmetic reproduces exactly, from BellRing's own filings and at BellRing's own
  definition of gross margin, over the window I state.** Nine months to 2026-06-30: gross
  margin **28.47%** against **34.94%** in the matched prior-year nine months, a fall of
  **647 basis points**, on net sales of $1,706.4M against $1,668.4M, **+2.28%**. SMPL's
  "640bp on +2.3%" is right to the rounding. **The prior is confirmed on its numbers.**
- **But the inference is too wide, and the disconfirming evidence is in the row above.**
  **[E4-26]** says to hunt disconfirming evidence hardest for the hypothesis one finds most
  attractive, and under operator rule 9 the attractive hypothesis here is the one already
  written down. So I looked for a filer that ought to have suffered the same thing and did
  not. **There are two, and neither was in the SMPL row.**
  - **Post Holdings has the identical fiscal calendar, the same nine-month window, the same
    US retail customers, the same commodity-input environment, and it is BellRing's own
    former parent. Its gross margin went UP 17 basis points.**
  - **Abbott's Nutritional Products segment sells Ensure, the direct RTD nutrition
    substitute, into the same aisle. It lost 130 basis points and held 46.5%.**
  Both of them **own their plants.** BellRing and Simply Good Foods own essentially none,
  and they are the two worst figures in the row by a factor of two to six.
- **The narrower finding, and the one I record.** The pass-through failure is **not a
  category fact.** It is a fact about **who owns the conversion step.** Where the brand owner
  also owns the plant, the input shock landed on a cost base it could manage and the margin
  moved by tens of basis points; where the brand owner buys finished goods from a private
  contract manufacturer at *"an agreed-upon tolling charge"*, the shock arrived as a price it
  had to accept, and the margin moved by hundreds. **[E2-58]'s equation is operating exactly
  where the SMPL run said -- beneath the trademarks -- but the layer is narrower than
  "the category": it is the protein input and the tolling charge.** And **[E2-59]** names
  precisely this half of the mechanism, listing administered *costs* beside administered
  prices. The asset-light brand owner faces an **administered cost** it does not set and an
  **administered price** it does not set. It has neither door.
- **A second narrowing, from inside the subject.** The failure is not even uniform across
  BellRing's own brands. Nine months to 2026-06-30, from the 8-K EX-99.1 of 2026-08-04:
  **Premier Protein RTD shake** net sales *"increased 0.5%, driven by 5.2% increase in volume
  and 4.7% decrease in price/mix"* -- volume up five points, price down nearly five. **Dymatize**
  net sales *"increased 13.7%, driven by 9.0% increase in volume and 4.7% increase in
  price/mix"*, and in the June quarter alone *"increased 26.7%, driven by 6.0% increase in
  volume and 20.7% increase in price/mix."* **One company, one input shock, one management,
  two opposite pricing outcomes.** The brand that could not price is the one sold into the
  three customers who take 74% of sales; the brand that took twenty points of price is the
  specialty and international powder brand. **The pass-through failure tracks CHANNEL
  CONCENTRATION, not category and not brand.** That is the correction the SMPL run is owed,
  and it strengthens rather than weakens SMPL's Q2 OUT: the mechanism is sharper than the
  one it named.

### THE [E3-03] CRITERIA, RUN EXPLICITLY

1. **"needed or desired" -- PASSES.** Dollar consumption of Premier Protein RTD shakes
   *"increased 6.0%"* in the 13 weeks to 2026-06-28 (8-K EX-99.1, 2026-08-04). The product is
   wanted, and wanted more than last year.
2. **"is thought by its customers to have no close substitute" -- FAILS, on the subject's own
   filed numbers.** A product with no close substitute does not surrender **4.7% of price/mix
   on its flagship while volume rises 5.2%** in the middle of the worst input-cost year in
   its record. The company's own FY2025 10-K says what it is in: *"The convenient nutrition
   category in which we operate is highly competitive and **highly sensitive to both pricing
   and promotion.** We compete with other brands, including private label and store brand
   products … Some of our competitors have substantially more financial, marketing and other
   resources than us."* Its own list of the grounds of competition ends *"shelf space, price,
   promotional activities"*. **And its FY2025 growth was bought the same way** (MD&A): Premier
   Protein sales *"up $286.3 million, or 17%, driven by 15% higher volumes primarily due to
   distribution gains and **incremental promotional activity**."* **The substitute is one
   shelf over and it is sometimes the retailer's own label.**
3. **"is not subject to price regulation" -- PASSES.** Nothing in the filings suggests a
   regulated price. But note what **[E2-59]** does with that: regulation *caps* a franchise
   and *floors* a commodity business; the absence of regulation creates neither class, and
   here it means only that there is no floor under the margin.

**Two of three is not a franchise. Criterion (2) is the one that carries the definition, and
it fails.**

### THE REST OF THE Q2 BATTERY

- **The two-characteristic test [E2-44]** -- *can it raise prices "even when product demand is
  flat and capacity is not fully utilized"*, and *grow dollar volume "with only minor
  additional investment of capital"?* **Split, and the failure is the decisive half.** The
  second characteristic passes outright and is this business's one genuinely attractive
  feature: capex is guided at **$10 million** against $2.3 billion of sales. The first fails
  in the **strongest possible form** -- demand was **not** flat (volume +4.7% for the nine
  months) and it **still could not hold price** (price/mix -2.4%). The test asks whether
  price survives weak demand; here price did not survive **strong** demand.
- **The inverse metric [E4-37]** -- *"you can almost measure the strength of a business over
  time by the agony they go through in determining whether a price increase can be
  sustained … it's not a great business when you have to have a prayer session before you
  raise your prices a penny."* The agony is in the release, in management's own words
  (2026-08-04): *"we are taking **decisive actions through pricing**, productivity
  initiatives and disciplined cost management to improve profitability."* A company that had
  the price would have taken it four quarters ago instead of announcing that it will try.
- **Untapped pricing power [E3-33]? No, and claiming it would be claiming near-monopoly
  [E5-28].** The row above supports nothing of the kind. The filed record is of a company
  that met an input-cost increase by **cutting** realised price on 80% of its revenue.
- **The dominance class [E2-53]? NO, and this is the cleanest disproof in the file.** *"Once
  dominant, the newspaper itself, not the marketplace, determines just how good or how bad
  the paper will be. Good or bad, it will prosper."* Premier Protein is described by its own
  new CEO as *"the clear leader in ready-to-drink shakes"* (8-K EX-99.1, 2026-08-04). **The
  clear leader lost 680 basis points of gross margin in a quarter in which its own consumption
  grew 6.0%.** The marketplace, not the company, is setting how good this business will be.
  Dominance of the shelf is not dominance of the economics.
- **Where units exist, monitor units [E4-55].** They exist and they are growing: volume +4.7%
  for the nine months, +1.7% in the June quarter, consumption +6.0%. **This is the Precision
  Steel case run backwards.** There, pounds fell while pricing held dollars level and the
  dollar series flattered a shrinking franchise. Here the physical series is **healthy** and
  the dollar margin is collapsing, which says the same thing about the same layer: the
  franchise's problem is not demand, it is that the volume is worth less per unit to its
  owner every quarter. The honest series is still the physical one, and it is telling me the
  category is fine and the position in it is not.
- **The attacker's test [E2-45]** -- *"how I would like, assuming I had ample capital and
  skilled personnel, to compete with it."* **I would like it very much, and the filing tells
  me how.** I would go to the same contract manufacturers, who will fill anybody's bottle for
  a tolling charge; buy the same whey from the same suppliers; and sell to the same three
  buyers, who are already selling their own private label in the same aisle. The only thing I
  would have to build is awareness, which is purchasable, and shelf space, which the retailer
  grants. **A moat you can cross by renting the incumbent's own factory is not a moat.**
- **Which of the four causes of extreme success [E4-36] is this record?** Net sales went from
  $854.4M (FY2019) to $2,316.6M (FY2025), +171% in six years. That is not an extreme max/min
  of one variable, it is not a nonlinear combination, and it is not extreme performance across
  many factors. **It is wave-riding, and the filings let me prove it rather than assert it.**
  **[E3-51]**: *"when a surfer gets up and catches the wave and just stays there, he can go a
  long, long time. But if he gets off the wave, he becomes mired in shallows."* The decisive
  fact is that **the wave has not stopped** -- Premier Protein RTD consumption is still +6.0%,
  the category is still growing -- **and the economics collapsed anyway.** When the wave is
  still running and the surfer is drowning, the advantage was never the surfer's.
  **[E4-36]**'s question is which causes are ownable; wave-riding is the one that is not.
- **Key-person dependence [E4-23]?** Recorded here as instructed rather than at Q3, but it is
  **not** the defect that closes this file. The CEO of six years, Darcy H. Davenport,
  *"will resign as a member of the Board, retire as President and Chief Executive Officer,
  and transition to the role of advisor"* effective 2026-07-29 (8-K, 2026-07-08), succeeded
  by an external hire *"following a comprehensive external search process."* The moat did not
  go when she went; it was already gone, and she left after it went.
- **Class: [x] NONE · Direction: DOWN.**

**VERDICT: [x] OUT**

**Why OUT and not UNKNOWABLE.** The separating test, asked aloud: *"Can I name the document
that would resolve this?"* There is no document to fetch. The documents are all here and they
answer the question against the company: the subject's own nine-month price/mix, its own
gross-margin series, its own statement that it competes on *"shelf space, price, promotional
activities"*, its own 74%-of-sales customer concentration, its own single-supplier and
single-co-manufacturer disclosures, and six peers' filed statements showing that the filers
who own their plants did not suffer this. **This is not the [E4-04] perimeter close either**,
which is reserved for durability that cannot be judged from filings; durability here was
judged, and the answer came back. **The evidence is in and the business fails criterion (2).
That is OUT, permanent** -- a finding about the business, not about my diligence and not about
my evidence.

---
## BENEATH THE CLOSE **[E4-29]** — Q3 THROUGH Q6

**The file closed at Q2.** What follows is the standing CGNX instruction: record what was seen
below the closing gate, marked **SEEN AND NOT SCORED**, with the unopened gates named as
**NOT OPENED**. None of it is a verdict and none of it may be read as one. It is here because
the work was done before Q2 closed, because the brief's standing rule required the 8-K
EX-99.1 earnings releases to be pulled before any Q3 scoring, and because **operator rule 6**
says a run records what it found rather than discarding it.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?

⛔ **NOT OPENED. Q2 returned OUT and the hard sequence stops at the first verdict that is not
IN. No Q3 verdict box is ticked below and no weight case is declared, because declaring one
would be scoring the gate.**

### SEEN AND NOT SCORED

**The [E4-29] fifth flag fires, and it fires in all three places -- the release, the guidance,
and the pay.** *"Trumpeting EBITDA … is a particularly pernicious practice. Doing so implies
that depreciation is not truly an expense, given that it is a 'non-cash' charge. That's
nonsense."*

- Every one of the four FY2026 8-K EX-99.1 releases headlines **Adjusted EBITDA**, and each
  states in terms that *"BellRing provides Adjusted EBITDA guidance only on a non-GAAP basis
  and does not provide a reconciliation of its forward-looking Adjusted EBITDA … to the most
  directly comparable GAAP measure."*
- The release says out loud what the measure is for: *"Management uses certain of these
  non-GAAP measures, including Adjusted EBITDA …, as key metrics in the evaluation of
  underlying company performance, in making financial, operating and planning decisions and,
  **in part, in the determination of bonuses for its executive officers and employees.**
  Additionally, BellRing is required to comply with certain covenants and limitations that
  are based on **variations of EBITDA** in its financing documents."*
- The **DEF 14A filed 2025-12-16 (accession 0001193125-25-320827)** confirms it from the pay
  side: the annual bonus uses *"Adjusted EBITDA (75%) and Net Revenue (25%) as the
  performance metrics"*, and the CD&A's own opening scorecard is stated in the measure --
  *"Adjusted EBITDA to $482 million, with respective growth over 2024 of 16% and 9%"* and
  *"Since our 2019 initial public offering, we have delivered an 18% revenue CAGR"* and an
  *"Adjusted EBITDA CAGR, outperforming the long-term expectations we shared at the time of
  the initial public offering."* Long-term awards are 80% PRSUs on **three-year relative TSR
  against the Russell 3000 Food Products companies**, 20% RSUs.
- Note **[E5-41]**'s mechanism is not the usual one here, and the honest reading has to say
  so: depreciation of property is about **$1.7 million a year** in a business whose entire
  D&A is dominated by amortisation of acquired brands. The reverse-float objection to EBITDA
  bites less hard in an asset-light filer than in a railroad. **What the measure deletes here
  is not depreciation, it is interest** -- $1,140.0 million of debt at 7.00% and SOFR plus a
  margin -- and the charges the company itself calls adjustments.

**The [E4-22] third flag, and [E3-48]'s prescribed action performed in full.** The rule is to
pull the company's own past guidance and set it against outturn. **FY2026, from the company's
own four 8-K EX-99.1 releases, all within nine months:**

| date | accession | FY2026 net sales guided | FY2026 Adjusted EBITDA guided | as % of sales |
|---|---|---|---|---|
| 2025-11-18 | 0001628280-25-052773 | $2.41-$2.49bn, +4% to 8% | **$425-$455M** | ~18% |
| 2026-02-03 | 0001628280-26-004789 | $2.41-$2.46bn, +4% to 6% | **$425-$440M** | ~18% |
| 2026-05-05 | 0001628280-26-030115 | $2.325-$2.365bn, 0% to 2% | **$315-$335M** | ~14% |
| 2026-08-04 | 0001628280-26-052137 | $2.335-$2.375bn, +1% to 3% | **$275-$295M** | ~12% |

**The midpoint went $440M, $432.5M, $325M, $285M. A 35% cut in nine months, with no quarter
in between in which the company told the market it might happen.** Alongside it, on
2025-11-18, the company *"updated its long-term financial algorithm"* to *"Net sales growth
target of 7% to 9%"* and *"Adjusted EBITDA as a percentage of Net Sales target of 18% to
20%"* -- a multi-year target published in the same document as the first of the four numbers
above, and already three points below its own floor two quarters later. **[E5-30]** is the
passage this belongs under: *"once you start it, it's all over. You can't quit … And
forecasting earnings, I can't imagine anything more destructive."* **[E2-49]**'s demand is
for *"pre-set, long-lived and small bullseyes"*, and this is the opposite.

**Capital allocation, against [E5-08]'s two conditions and [E5-24]'s first law -- and this is
the largest single observation in the section.** *"what is smart at one price is dumb at
another."* From the filings:

| window | shares bought | cash | average price paid | source |
|---|---|---|---|---|
| FY2025 | ~9.0m (*"7% of common shares outstanding"*) | **$472.5M** | **$52.62** | 8-K EX-99.1, 2025-11-18 |
| 2025-10-01 to 2025-11-17 | 1.2m | **$40.0M** | **$34.01** | same |
| 9m to 2026-06-30 | 4.9m | **$133.1M** | **$27.41** | 8-K EX-99.1, 2026-08-04 |
| **price on 2026-09-18** | | | **$8.98** | Yahoo, flagged |

Roughly **$645 million** spent buying stock at average prices between $27 and $53, against a
market capitalisation today of **$1,044 million**. And the funding is on the filed cash-flow
statement: in the nine months to 2026-06-30 the company drew *"Proceeds from issuance of
long-term debt 325.0"* against *"Repayments of long-term debt ( 275.0 )"* while paying
*"Purchases of treasury stock ( 137.2 )"* out of **$65.0 million** of operating cash. The
revolver balance went from $250.0M at 2025-09-30 to $300.0M at 2026-06-30. **[E4-50]** does
license borrowing to repurchase -- but it is the *discount* that licenses it, never the
borrowing, and condition (2) is a **material discount to conservatively calculated intrinsic
value**. **$506.9 million of authorisation remains.** Stated with the humility clause
**[E4-13]** as the framework requires: this rests on my own reading and *"they also know a
whole lot more about them than I do"*, and **[E5-08]** says the infraction is usually
innocent -- *"many CEOs never stop believing their stock is cheap."*

**[E2-01], the primary test, is NOT COMPUTABLE in its plain form here, and why matters.**
*"the achievement of a high earnings rate on equity capital employed (without undue leverage,
accounting gimmickry, etc.)"*. **Total Stockholders' Deficit at 2026-06-30 is $(467.2)
million** on total assets of $1,052.1 million; the denominator is negative and has been for
most of the company's life, because the repurchases above and the Spin-off consideration ran
book equity through zero. **[E2-43]** is the scoping rule -- for acquisitive or leveraged
filers the denominator is **unleveraged net tangible assets** with the goodwill wedge
reported separately. That computation was not performed, because performing it would be
scoring an unopened gate.

**Other observations, recorded flat.** The CEO of the company since its IPO, **Darcy H.
Davenport**, *"will resign as a member of the Board, retire as President and Chief Executive
Officer, and transition to the role of advisor"* effective 2026-07-29 (8-K, 2026-07-08,
accession 0001628280-26-047674), succeeded by an external hire. The Chief Growth Officer
stepped down on 2026-06-24 in a workforce realignment expected to yield *"annualized run-rate
operating expense savings of approximately $10 to $12 million"* against *"one-time workforce
realignment charges of approximately $6 million"*. **The Joint Juice litigation settled for
$90.0 million** (8-K, 2025-10-23, accession 0001628280-25-046124: a $19.2M California federal
fund and a $70.8M multistate fund, each *"does not constitute an admission of liability or
wrongdoing"*), with a **$68.1 million provision for legal matters** taken in the June 2025
quarter. **None of this is scored.** Under **[E5-38]** a fired flag is not a venality
finding, and under **[E5-17]** a Q3 pass would in any case be the absence of found
disqualifiers rather than a finding that anyone is honest.

- **NO BOX TICKED. Q3 WAS NOT OPENED** because Q2 returned OUT.

## Q4 — WILL IT SURVIVE?

⛔ **NOT OPENED. Q2 returned OUT.** The arithmetic below was produced in the course of
resolving flags (ii) and (iii) and is reported because it was computed, under **operator
rule 3**:

# COMPUTATION — NOT A CLEARANCE

**No entry language appears anywhere in this block and no verdict is drawn from it.**

**The eight-year filed series, every figure from the filed Consolidated Statements of Cash
Flows** (FY2020 10-K accession 0001772016-20-000070 for FY2018-2020; FY2022 10-K
0001772016-22-000061 for FY2021-2022; FY2025 10-K 0001772016-25-000153 for FY2023-2025):

| fiscal year | OCF $M | "Additions to property" $M | D&A $M | SBC $M |
|---|---|---|---|---|
| 2018 | 141.2 | 5.0 | 25.9 | 0.0 |
| 2019 | 98.3 | 3.2 | 25.3 | 0.0 |
| 2020 | 97.2 | 2.1 | 25.3 | 2.5 |
| 2021 | 226.1 | 1.6 | 53.7 | 4.6 |
| 2022 | **21.0** | 1.8 | 21.3 | 9.8 |
| 2023 | 215.6 | 1.8 | 28.3 | 14.2 |
| 2024 | 199.6 | 1.8 | 36.5 | 21.0 |
| 2025 | 260.6 | 4.7 | 18.6 | 22.1 |
| *9m to 2026-06-30* | *65.0* | *8.1* | *15.0* | *17.6* |

**Owner earnings on the framework's convention** -- OCF less SBC less the (c) guess, the
working-capital increment already netted inside OCF from one audited line per **[E2-23]**
constraint 3. **Never a net-income proxy** (operator rule 5).

| fiscal year | (c) = total capex | (c) = D&A **[E3-44, E2-41]** |
|---|---|---|
| 2018 | 136.2 | 115.3 |
| 2019 | 95.1 | 73.0 |
| 2020 | 92.6 | 69.4 |
| 2021 | 219.9 | 167.8 |
| 2022 | 9.4 | **(10.1)** |
| 2023 | 199.6 | 173.1 |
| 2024 | 176.8 | 142.1 |
| 2025 | 233.8 | 219.9 |
| **8-year mean** | **$145.4M** | **$118.8M** |
| **5-year mean (FY2021-25) [E2-42]** | **$167.9M** | **$138.6M** |
| **3-year mean (FY2023-25)** | **$203.4M** | **$178.4M** |

- **The (c) guess, disclosed as a judgment because *"(c) must be a guess"* [E2-09].** This is
  **not** the capital-intensive exception class of **[E5-20]**: the company owns one bar
  plant in Germany and buys everything else from third parties, and its own MD&A says
  *"Our asset-light business model requires modest capital expenditures, with annual capital
  expenditures over the last three fiscal years averaging less than 1% of net sales. No
  significant capital expenditures are planned for fiscal 2026."* So the D&A default
  **[E3-44]** is not invalid here, but it is **conservative for the wrong reason**:
  depreciation of property is only about $1.7 million a year, and nearly all of the D&A line
  is amortisation of the brands Post bought in 2013-2015, which is a charge against a
  purchase price rather than a renewal cost. **The honest band is the two columns above, and
  I report both rather than resolve them.**
- **THE SCREEN'S SPREAD REPRODUCES.** The screen carried `oe_bottom_m 139` and
  `oe_top_m 203`. My 5-year D&A end is **$138.6M** and my 3-year capex end is **$203.4M**.
  The screen's bracket is right and its `spread_caveat` was right to say it could not see
  older variation: **the eight-year window pulls the bottom of the range down to $118.8M**,
  which the 4-construction could not reach.
- **The windows disagree, and the disagreement is the finding [E4-25, E4-38].** Three-year
  $178-203M against eight-year $119-145M. The combined range is **roughly $119M to $203M**,
  a 71% spread on the same company from the same filings. **A wide spread is a Q4 finding in
  its own right [E5-11]**, and the distorted year is named: **FY2022**, the Spin-off year, in
  which a $154.6M working-capital build (flag (ii)) cut OCF to $21.0M and took the D&A-end
  figure negative. **[E3-55]** says volatility with a certain endgame is not a defect, but
  the endgame here is not certain.
- **[E4-41] -- normalize the mean DOWN, and the screen said so.** `level_shift 1.93`,
  `level_note "STEP UP - normalize down"`. It is right, and it is worse than it looks,
  because the step-up years are the ones the trailing mean is weighted toward and the
  business is no longer running at that level: **nine months of FY2026 produced $65.0M of
  operating cash against $91.5M in the matched prior period, and $39.3M of owner earnings at
  the capex end after $17.6M of SBC and $8.1M of capex.** Management's own guidance puts
  FY2026 Adjusted EBITDA at **$275-295M against $481.6M in FY2025**. **Any mean built on
  FY2018-FY2025 is measuring a business that stopped existing at that level in the current
  year, and applying it to today's price would be the calculated-terminal-date error
  [E4-38] warns against.**
- **Stock compensation subtracted in full [E5-06]**, and the measure is understated: the
  reported charge is *"the floor of the subtraction, not the measure"* **[E3-70]** where SBC
  is material, and $22.1M on $260.6M of operating cash is material.
- **Great, good or gruesome [E4-20] -- not scored, but the evidence is unusual and worth
  recording.** This is not the airline shape. Capex is under 1% of sales, so the business
  does **not** *"require significant capital to engender the growth"*. What it does instead
  is convert a growing physical volume into a shrinking gross margin, which **[E4-20]**'s
  three savings accounts have no box for: the interest rate on the account is falling while
  no new deposit is required. That is a **Q2** finding about position, and Q2 already took
  it.
- **Staying power, the three strengths [E5-11]**, observed and not scored:
  (1) *a large and reliable stream of earnings* -- large, and the reliability is exactly what
  the four guidance tables above put in question; (2) *massive liquid assets* -- **$51.0
  million of cash at 2026-06-30**, down from $89.1M, against $1,140.0M of debt, with
  *"available borrowing capacity under the Revolving Credit Facility"* of **$197.6 million**
  and the drawn portion costing **5.62%**; (3) ***no significant near-term cash
  requirements*, the one that usually kills** -- the **$840.0 million of 7.00% senior notes
  mature in March 2030** and the revolver matures 2030-08-22, *"provided that if on
  December 14, 2029, the Company's 7.00 % Senior Notes have not been redeemed in full in cash
  or refinanced"* the revolver springs earlier. Nothing is due inside three years. **[E3-52]**
  says read the terms and not just the quantity, and the terms are long-dated. **[E5-39]**'s
  standard is that nothing be *dependent on the kindness of strangers*; $300.0M drawn on a
  bank line to fund buybacks is a dependence, whatever the maturity.
- **The capital structure is a fact about the Spin-off, as the brief said.** The $840.0M of
  notes were issued to Post **as consideration** in the Contribution, not to fund anything
  the business asked for. **[E2-54]**'s coverage test, computed and not scored: interest
  expense net was **$60.0M for nine months** against **$65.0M of operating cash before
  capex**, i.e. cash flow net of capex covers accrued and payable interest **less than once**
  in the current nine months, against roughly four times on the FY2025 figures.
- **The named way this business dies, modelled and not scored [E2-27, E3-24].** The mechanism
  is not a covenant and not a maturity. It is the squeeze itself, compounding: the brand
  cannot price to three customers who are 74% of its sales, the tolling charge and the
  protein price are set by suppliers it discloses as single-source, and the only lever left
  is the one management has already pulled twice, promotion, which lowers realised price
  further. Quantified from filed figures: **every 100 basis points of gross margin is $23
  million of pre-tax income on FY2025 sales**; the 647 basis points already lost over nine
  months annualise to roughly **$150 million**, against $60M-$80M of annual interest and a
  FY2025 owner-earnings figure of $220-234M. **A further 300 basis points would take owner
  earnings through the interest bill.** Likelihood, in the corpus's vocabulary: **a real
  possibility**, and the argument against it is stated as **[E4-51]** requires -- whey and
  milk-protein prices are cyclical, tariffs are policy and reversible, the $21.3M of
  inventory charges and the $10.0M bottle charge are non-recurring by their own terms, the
  new CEO inherits a $10-12M cost programme, and Dymatize has already demonstrated that this
  management can take twenty points of price where the channel allows it. **That case is
  real and it is why Q2, not Q4, is the gate that closed this file: the question is not
  whether the cycle turns, it is who gets the margin back when it does.**

- **NO BOX TICKED. Q4 WAS NOT OPENED** because Q2 returned OUT. The block above is headed
  COMPUTATION and carries no entry language.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 returned OUT.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

⛔ **NOT OPENED. Q1 through Q4 do not all show IN: Q2 returned OUT.** No valuation verdict is
recorded, no floor test is run, no ranking position is assigned, and no bar is chosen. The
sovereign was struck in this run (USD 5.34%, 09/18/2026, US Treasury daily par yield curve)
because **Step 0 requires it**, not because a yield was wanted.

**The one thing recorded here, and it is recorded as a warning rather than a computation:**
the screen's `yield_bottom` of 11.15%, its `vs_sovereign` of 5.8 points and its
`growth_required` of -1.15% were all computed on the $1,243M cap and on the $139M-$203M
owner-earnings bracket. **On the re-struck cap of $1,044M they would all look better still,
and they would all be wrong in the same way**: they price a trailing mean of a business whose
own guidance says it is currently earning a little over half of it. **[E4-38]**'s
calculated-terminal-date error and **[E4-41]**'s normalize-down rule both point the same way,
and **[E4-28]**'s floor is not a rescue for a business that failed at Q2 -- the floor sorts
prices, and this file did not reach a price question. **Cheapness is not a remedy for a
franchise finding**; that is what **[E5-35]** says: *"You can turn any investment into a bad
deal by paying too much. What you can't do is turn any investment into a good deal by paying
little."*

- **NO BOX TICKED. Q5 WAS NOT OPENED.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

⛔ **NOT OPENED. There is no position and no entry, so there is nothing to pre-commit
against [E1-02].**

**The reversal condition, written in words and not as a price alert (the QLYS ruling).** No
band is armed in `tools/alerts.json` and no `PORTFOLIO.md` row is created, because this name
failed on the business and not on the price. **This file re-opens only if BellRing's own
filings show the pricing relationship change, and the test is stated in the terms the run
used to close it:** four consecutive quarters in which **Premier Protein RTD price/mix is
positive** while gross margin recovers above roughly 33%, **and** a fall in the share of net
sales taken by Walmart, Costco and Amazon materially below 74%, **and** evidence in the
filings that the conversion step has moved inside the company or onto contracted terms it
sets. Margin recovery alone on falling whey prices is **not** the trigger, because that would
be the cycle and not the position, and **[E3-30]** is the question that governs: *"whether
this erosion is just part of an aberrational cycle … or whether the business has slipped in a
way that permanently reduces intrinsic business values."* **[E4-17]** adds that such beliefs
*"change quite gradually"*, so the re-open is deliberately slow and deliberately not a quote.

- **NO BOX TICKED. Q6 WAS NOT OPENED.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, **Q2 OUT**, and Q3, Q4, Q5, Q6
      are each headed **NOT OPENED** with no verdict box ticked.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the
      only IN in the file. The competitor row is complete for six peers and **the moat class
      is not held PROVISIONAL**, because the verdict is OUT and the five uncomputable peers
      could only make the subject look relatively better.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives -- **there are none.**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known -- **there are none.**
- [x] Step 0: the filing was read, with accession number; two figures were cross-checked
      against the filed statements (FY2022 OCF $21.0M; FY2025 gross profit $770.4M), plus the
      9m FY2026 gross profit on both the subject's and Post's filed statements of operations.
- [x] Owner earnings on a multi-year mean; three windows stated (8-year, 5-year, 3-year);
      capex band disclosed as a judgment with the D&A default **[E3-44]** and the reason the
      capital-intensive exception **[E5-20]** does not apply. **Never a net-income proxy**
      (operator rule 5). The block is headed **COMPUTATION -- NOT A CLEARANCE** (operator
      rule 3) and carries no entry language.
- [x] Competitor row filled: six peers computed from filings at the same metric and matched
      windows, five named with their obstacles.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated: **USD 5.34%,
      09/18/2026, US Treasury daily par yield curve**, struck in this run.
- [x] Value stated as a round-number range -- **not applicable; Q5 was not opened and no value
      is stated anywhere in this file.**
- [x] One bar chosen, not both; windage count stated -- **not applicable; no bar was used.**
      **Windage count: conservatism was spent ZERO times**, because no valuation was run.
- [x] Prices dated; aggregator used for live quotes only and flagged, with the raw responses
      saved to `Test Runs/_research 2026-09-20 BRBR/quote_BRBR_raw.json`,
      `quote_BRBR_3y.json` and `quote_BRBR_splits.json`.
- [x] Run committed to git, with a pathspec, at Step 0, at Q2 and at the close.

## REGISTER
- Verdict: [ ] IN · **[x] OUT (about the business)** · [ ] UNRESEARCHED · [ ] UNKNOWABLE
- **One line:** BellRing owns two trademarks and no factories, sells 74% of its output to
  three retailers, buys the majority of its protein from one supplier and its flagship bottle
  from one supplier, and in the nine months to 2026-06-30 it gave back 4.7% of price/mix on
  the brand that is 80% of its revenue while its volume rose 5.2% and its gross margin fell
  647 basis points -- **so it fails [E3-03] criterion (2), and the competitor row shows the
  two filers in the same aisle that own their own plants lost 130 and minus 17 basis points
  in the same window.**
- **If UNRESEARCHED -- THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
