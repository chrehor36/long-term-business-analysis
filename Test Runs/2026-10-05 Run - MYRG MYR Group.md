# Company Run — MYR Group Inc. (NASDAQ: MYRG) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched blind: `PORTFOLIO.md`, every holding
review, the resume-state files, the run queue and the prepped reading list were not opened, and no attempt was made to
learn whether anyone holds or wants this name. The analyst does not know the position.

**CONTAMINATION, declared.** (1) The session context opened with the repository's recent commit subjects, which name
four of this run's competitors and their verdicts in other runs of the same day (PWR, EME, IESC, FIX). Those run files
were not opened; every competitor figure below was fetched fresh from the competitors' own filings. (2) A directory
listing of `Test Runs/` showed the file names of the day's other runs and holding reviews (names only; none concerns
MYRG; none was opened). (3) No other MYRG file exists in `Test Runs/` (searched by name before the copy).

Working folder: `Test Runs/_research 2026-10-05 MYRG/` (filings as text, `run_py.txt`, `cover_shares.txt`,
`annual_table.txt`, `competitor_table.txt`, `value.py`, `value_out.txt`, `rows.txt`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $305.16 (2026-10-05, live quote via `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **15,569,250** (Form 10-Q for
  the period ended 2026-06-30, filed 2026-07-29, accession `0000700923-26-000042`; `python Screens/cover_shares.py
  MYRG`). No other class; no preferred issued (10-K balance sheet, 4,000,000 preferred authorized, none issued).
- **Market cap:** about $4,751M (15,569,250 x $305.16).
- **Sovereign for the earnings currency (USD):** 5.63%, the 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-02 (via `tools/run.py`, which reads the Treasury curve first).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-25, accession `0000700923-26-000007` (Items 1, 1A, 5, 7, 7A, 8: the statements and
    notes on revenue recognition, estimates, debt).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-07-29, accession `0000700923-26-000042` (results, backlog, the
    Valley acquisition in Note 12).
  - DEF 14A filed 2026-03-04, accession `0000700923-26-000017` (pay design; read for the record, not used: Q5 and Q6
    NOT REACHED).
  - 8-K filed 2026-09-10, accession `0000700923-26-000047` (new credit agreement, Items 1.01 and 2.03).
  - Earlier 10-Ks for the record: FY2010 (`0001047469-11-001844`), FY2017 (`0001144204-18-013353`), FY2024
    (`0000700923-25-000006`).
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025, $326,567
  thousand in the filed cash-flow statement (10-K `0000700923-26-000007`) against $327M printed by `tools/run.py`:
  agrees. Stock pay FY2025 $14,832 thousand (filed) against $15M (tool): agrees. Shares: tool 15.6M against cover
  15,569,250: agrees (no split since the measurement date).
- `tools/run.py` arithmetic lines (only these used, Part VII): OCF 71 / 87 / 327, stock pay 8 / 9 / 15, D&A 59 / 65 / 67,
  capex 85 / 76 / 94 for FY2023 / 2024 / 2025 ($M). The tool's ten-year balance-sheet table uses first-filed values; its
  2024 total assets ($1,574M) differ from the FY2025 10-K comparative ($1,488.8M) because the company reclassified
  retainage on overbilled contracts from contract assets to contract liabilities in 2025, an "immaterial revision" that
  "did not impact shareholder’s equity, revenue, net income, or net operating cash flows" (10-K FY2025, Note 1). The
  tool's printed "growth the price assumes" (20.8%) and its yields are not used; the owner cash used below is computed
  in `value.py` from the filed series over ten years.

## THE FOUNDATIONS (not a gate)
A share is a business, and the market only "just tells us prices" **[M2006-077]**: the price has risen from the $117
average paid in the company's own 2024-2025 buybacks (10-K FY2025, Item 7) and the $127.04 used for the March 2025
stock grants (DEF 14A 2026) to $305.16, and none of that rise is evidence about the business. No macro forecast enters
**[M2000-094]**: the filer's outlook rests on grid spending, data centres and "the emergence and adoption of artificial
intelligence technologies" (10-K FY2025, Item 7, Outlook), which is a demand forecast for the trade, not a reason the
castle stands; the rows ask instead for "the average profitability of the business over time and how strong its
competitive mode is" **[M2015-016]**. The analyst's habit applied is to look for "what’s wrong in things" **[M2025-013]**
and to write the contrary evidence down at once.

**Contrary evidence, written down as found** **[M1997-127]**:
1. *Against the business (found first):* the filer's own competition section says price decides; anyone with money can
   enter; its MSAs are rebid "and generally attract numerous bidders" and can be ended on 30 to 90 days' notice (Item 1).
2. *Against the business:* gross margin cut by estimate changes three years running: 1.7% (2023, $62.2M of operating
   income), 4.4% (2024, $146.5M), 1.4% (2025, $52.8M) (10-K FY2024 and FY2025, Note 1).
3. *Against the business:* the 2010 10-K said price is "often a principal factor"; every 10-K read from 2017 on says
   "always" (wording change found by search; read as a fact of the filings, not as a measure).
4. *For the business (written down as found, against my own early leaning):* T&D has real entry costs, "the cost of
   equipment and tooling", "availability of qualified labor", bonding (Item 1), which "sometimes reduce the number of
   potential competitors"; the T&D lineage runs to 1891; H1 2026 operating margin 6.4% with T&D at 9.6% (10-Q).
5. *For the business:* return on tangible assets through the cycle is close to Quanta's and Primoris's, not far below.
6. *Against the business:* the 2026 rise is shared by the trade, and the largest competitor names the cause as a
   temporary one: "competition may lessen as industry resources, such as labor supplies, approach capacity" (Quanta
   10-K FY2025, `0001050915-26-000006`).

## THE STANDING RULE
Nothing in owning a common share of this company on unborrowed money can call the buyer's tune; the rule binds the
buyer's financing and sizing, and only a margin purchase would engage it **[M2012-081]**, **[L2014-024]**. No finding.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the filing.** A holding company of electrical contractors in two segments: T&D (54.7% of 2025
  revenue: building and maintaining transmission lines, substations and distribution for utilities, as prime
  contractor, through bids, EPC contracts and one-to-four-year MSAs) and C&I (45.3%: electrical work on data centres,
  hospitals, airports, plants, roadway lighting, mostly as subcontractor to general contractors, 84.5% fixed-price).
  About 9,000 employees, 7,200 craft, about 85% union (mostly IBEW) (10-K FY2025, Item 1). The product is labour and
  equipment sold by the job.
- **The key variables** **[M1998-044]**: (1) the volume of utility and C&I construction spending (cyclical, "vulnerable
  to downturns", Item 1); (2) the margin at which jobs are bid, set by competition; (3) execution on fixed-price jobs
  (estimate changes). The first is a forecast about customers' spending, not about technology; the second and third are
  visible in sixteen years of filed results (operating margin 1.6% to 6.2%, 2010 to 2025, `annual_table.txt`).
- **Can the economics be foreseen?** The test is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, and the economics, not the product, are what must be
  understood: "Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**. Here they can be read:
  a bid contractor whose filed record shows what its earning power is across a boom (2021-2025) and a slack period
  (2015-2019). Do the past statements tell me the future ones **[M2008-033]**? For the margin and the return on capital,
  yes, as a band; for the year-to-year path, no, and the rows do not ask for that. No technology question decides it
  (the work is the same line work since 1891), so the routing of rapid change to TOO HARD does not apply
  **[M1998-008]**, **[M1999-063]**.
- **How far off could I be** **[M2011-084]**? On the volume of work, far (the T&D transmission share swings, large
  awards are "difficult to predict", Item 7). On the margin band, the record gives a narrow range. That narrow range is
  what Q2 must explain.
- **VERDICT: IN.** The economics are simple and on the record; the question the record raises (why the margin stays thin)
  is a castle question, and Q2 owns it **[M1995-051]**, **[M2000-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**.

**The castle tests, each with its filing fact** (10-K FY2025, `0000700923-26-000007`, unless marked):

1. **The attacker with money.** The 2011 test: "if I had a hundred million dollars and I wanted to go in and take on
   See’s Candy, could I do it?" and "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The filer
   answers it in its risk factors: "Any organization that has adequate financial resources and access to technical
   expertise may become one of our competitors." The largest competitor writes the same of the trade: "there are
   relatively few barriers to entry into some of the industries in which we operate" (Quanta 10-K FY2025,
   `0001050915-26-000006`). The answer is yes. The rows' reading of such a field: "there are some industries that are
   just never going to have barriers to entry. And in those industries, you better be running very fast" **[M2012-106]**.
   The T&D entry costs the filer names (equipment, craft labour, bonding) "sometimes reduce the number of potential
   competitors on these projects"; they narrow the bid list on large jobs and do not show up in the returns (test 9 and
   the competitor row).
2. **Pricing power, and the agony before a rise.** "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. Here the price is
   not set by the company at all: work is won job by job, "most of their work is awarded through a bid process where
   price is always a principal factor", and the principal competitive factors begin with "price and flexible contract
   terms". The MSAs carry no volume and no exclusivity in most cases: "A majority of our MSAs do not include
   obligations to assign specific volumes of work to us nor do they grant us exclusivity", and "Many of our contracts,
   including MSAs, are open to bidding at expiration and generally attract numerous bidders." Most contracts "may be
   terminated by our customers on short notice, typically 30 to 90 days". This is the gas station of the rows, where
   "whatever he charged for gas was my price" **[M2012-109]** and the rival "determined our profit, because we looked at
   his price every day" **[M2023-079]**.
3. **Unit volume and share of mind.** Not applicable as a brand test; the customer is a utility procurement desk or a
   general contractor running a bid. Revenue grew from $597M (2010) to $3,658M (2025), partly bought (acquisitions of
   $13.1M in 2015, $12.1M in 2016, $79.7M in 2019, $110.7M in 2022, and Valley at about $328.0M on 2026-07-01, 10-Q Note
   12). Volume grew; margin did not (test 9).
4. **The low-cost position.** In a commodity-like field "being the low-cost producer is all-important" **[L2000-017]**,
   and "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**. The filer does not claim
   the position; it concedes the opposite: "Some of our competitors may have lower labor and overhead cost structures
   and, therefore, may be able to provide their services at lower prices than ours." Its labour is union labour on
   NECA-IBEW terms shared by its union rivals, so its labour cost is at best "on parity" with its union rivals, not below them **[M2001-013]**. Its margin
   is the lowest of the five companies compared (competitor row). No evidence of a cost advantage found.
5. **The brand in the customer's mind.** The filer: "We do not generally register our trade names" and does not
   "consider any single trade name to be of such material importance that its absence would cause a material
   disruption to our business." No brand castle is claimed.
6. **Would the customer still choose it over the low bid?** The 1972 See's question was whether customers would buy
   "in preference to other candies" and not "for the low bid" **[M2017-009]**. The filer's answer is the bid process
   itself (test 2). The C&I segment is mostly subcontract work for general contractors "who typically manage the bid
   process". The rows' description fits: "most insureds don't care from whom they buy" **[L2004-003]**. Safety,
   reputation and relationships are listed among the competitive factors and are real, but they qualify a bidder; they
   do not make the customer pay more than the low qualified bid, on the filer's own words.
7. **Ask the competitors** **[M1999-130]**, **[M2025-043]**. Not done in person; the public record of the competitors'
   own words is used. Quanta: "price is often an important factor in the award of such agreements. Accordingly, we could
   be underbid by our competitors", and "Certain of our competitors may also have lower overhead cost structures"
   (`0001050915-26-000006`). Primoris: contracts "are primarily obtained through competitive bidding or through
   negotiations with customers" from "pre-qualified contractor lists" (`0001104659-26-018677`). Every competitor read
   describes the same open field from the other side.
8. **Widening or narrowing.** The record: operating margin 6.2% in 2013 and 2014, down to 2.1% in 2017 (write-downs on
   two Midwest projects and one Canadian project, 10-K FY2017, `0001144204-18-013353`), 1.6% in 2024 (estimate changes
   cut $146.5M of operating income, 10-K FY2024, `0000700923-25-000006`; "certain T&D clean energy projects and a C&I
   project", 10-K FY2025), 4.6% in 2025, 6.4% in H1 2026. The 2010 10-K said price is "often a principal factor"
   (`0001047469-11-001844`); the 2017, 2024 and 2025 10-Ks say "always". No notch gained in sixteen years; at most the
   wording lost one, in the manner of the newspapers' "lost still another notch" **[L1995-023]**. The H1 2026 rise is
   shared by the trade (competitor row) and is called by the largest competitor a matter of labour capacity; an
   advantage gained that quickly is the kind the rows say can be lost "quickly, too" **[M2002-050]**.
9. **What could destroy, modify or reduce it** **[M2000-014]**: the end of the grid and data-centre spending cycle, which
   the filer cannot forecast ("we cannot predict the impact such factors may have", Item 7); the customers' own crews
   ("competition from in-house service organizations of our existing or prospective customers including electric
   utility companies"); and fixed-price execution. There is no standing advantage for these to reduce.

**The competitor row** (same metric, each company's own 10-K XBRL facts, first-filed values; operating income over
revenue, and operating income over tangible assets, i.e. total assets less goodwill and intangibles, the measure of
**[M2011-060]**; MasTec reports no operating income, so pre-tax income plus interest expense is used for it;
`competitor_table.txt`):

| company (FY2025 10-K accession) | mean operating margin 2010-2025 | low / high | mean pre-tax return on tangible assets 2010-2025 | 2025 margin |
|---|---|---|---|---|
| MYRG (`0000700923-26-000007`) | **4.0%** | 1.6% / 6.2% | **9.2%** | 4.6% |
| Quanta PWR (`0001050915-26-000006`) | 5.4% | 3.1% / 8.1% | 10.3% | 5.7% |
| Primoris PRIM (`0001104659-26-018677`) | 4.9% | 2.9% / 6.8% | 10.3% | 5.4% |
| EMCOR EME (`0000105634-26-000025`) | 4.8% (2010-2019: 3.8%) | -0.6% / 10.1% | 13.3% (2010-2019: 11.3%) | 10.1% |
| MasTec MTZ (`0000015615-26-000020`) | 5.3% | -0.5% / 8.2% | 11.6% | 4.8% |

MYRG has the lowest mean margin and the lowest mean return on tangible assets of the five over sixteen years. A pre-tax
9.2% on tangible assets, before the depreciation-heavy fleet is replaced at rising prices, is the return of an average
participant in a competitive trade: "Average is going be terrible in insurance over time" **[M2000-072]** is said of a
commodity business and fits here. The one competitor whose margin left the band, EMCOR (10.1% in 2025 against 3.8% for
2010-2019), did so in the recent years of the construction boom, which is the trade-wide rise noted in test 8.

**Contrary evidence weighed.** The T&D entry costs and bonding capacity are real; the filer says "The ability to post
bonds provides us with a competitive advantage over smaller or less financially secure competitors." But an advantage
over small firms in a field where Quanta, MasTec and Primoris also bid does not make the customer accept a higher price,
and sixteen years of margins and returns at or below the field say it has not. The castle the rows ask for "protects
excellent returns on invested capital" **[L2007-004]**; the returns here are not excellent and are not protected.

**Box.** A castle shown on the evidence to be open is OUT; "If the answer had been yes, we wouldn’t have done it."
**[M2011-015]**. This is not a castle whose future cannot be judged (that would be TOO HARD **[M2000-019]**,
**[M2006-013]**): the filer, its largest competitor and sixteen years of results all answer the attacker test the same
way. Nor does price reopen it: "What you can’t do is turn any investment into a good deal by paying little"
**[M2019-015]**.

- **VERDICT: OUT.** The castle is shown to be open: entry for any well-funded organization (filer and Quanta, in their
  own words), price-led bidding with rebid MSAs and short termination rights, no cost advantage claimed and a cost
  disadvantage conceded, and the lowest margins and returns of five peers over 2010 to 2025 **[M2011-015]**,
  **[M2012-106]**, **[M2012-109]**, **[M1997-010]**, **[L2004-003]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed OUT at Q2). The figures read for the owner's reporting request are in the COMPUTATION
section below and are not a weighing.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The ten-year balance-sheet reading was done for the computation and is recorded below under
COMPUTATION — NOT A CLEARANCE; it carries no clearance language.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED (operator rule 2: no Q5 output unless Q1 to Q4 each show IN).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (Facts read and set aside: no dividend since the 2008 listing; $75.0M bought back in each of 2024 and 2025
at weighted averages of $116.54 and $117.33 a share; a new $75.0M programme announced 2025-07-30 expired unused on
2026-02-04; Valley bought for about $328.0M cash on 2026-07-01, $235.0M of it borrowed. All from the 10-K FY2025 and the
10-Q.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The value range, fair-price band and cheap price asked for by the owner are reported below,
labelled COMPUTATION.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. (For the record only: surety bonds of about $2.35B face outstanding with about $817.8M of cost to complete
on bonded projects at 2025-12-31; a new $690M revolver and term loans of $150M and C$70M under the credit agreement of
2026-09-08, 8-K `0000700923-26-000047`; covenants of net leverage no more than 3.0 and interest cover no less than 3.0.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked; nothing in the filings read touches the named businesses).

---
## COMPUTATION — NOT A CLEARANCE
*Written at the owner's request (reporting, not a rule change). The file closed OUT at Q2; nothing below reopens it,
and nothing below is entry language. A price does not reopen a castle shown open **[M2019-015]**.*

**The balance sheets first, 2016 to 2025** (run.py's table of first-filed values, read against the filed statements of
FY2025 and FY2024; $M):
- Equity rose from 263 to 660 and retained earnings from 123 to 503, about 380 of retained profit in ten years, while
  about 300 went to buybacks (101.5 in 2016 alone, 75.0 in each of 2024 and 2025, XBRL `PaymentsForRepurchaseOfCommonStock`).
  Equity fell twice, in 2016 and 2024, both times on buybacks, not on losses.
- Goodwill and intangibles rose from 59 to 188, from acquisitions in 2018, 2019 and 2022 (the 2018 payment is not tagged
  in XBRL); Valley adds about 328 of purchase price in 2026, so the bought share of the asset base is rising.
- Receivables rose from 235 to 604 with revenue (20.6% of revenue in 2016, 16.5% in 2025); at 2025 contract assets were
  242 against contract liabilities of 301, so customers' advance billings fund part of the work. The 2025 operating cash
  of 326.6 includes a working-capital inflow of about 140 (filed reconciliation, Item 7), which reverses when billing
  timing turns; the 2023 operating cash of 71.0 shows the other side.
- Cash was small in most years (3 to 82) until 150 at 2025, of which about 93 went into Valley in July 2026.
- Long-term debt stayed small (between 3 and 157 at year-ends, the peak in 2019 after an acquisition) until July 2026 (235 borrowed).
- Property and equipment net rose to 306; capital spending exceeded depreciation of property in every year from 2018 to
  2025 (2025: 94.4 against 61.7). The filer says most capital spending buys specialised equipment "to reduce our
  reliance on lease arrangements and short-term equipment rentals" (Item 7).
- What the figures do not say: how much of the 2025 to 2026 margin is the boom and how much is lasting **[M2025-032]**.
  The filer also leads with EBITDA as a performance and liquidity measure (Item 7); the rows regard it as "utter
  nonsense" **[M1998-086]**, and it is not used here.
- The accounting is not confusing; the one revision (the retainage reclassification) is explained in Note 1. No finding
  on Q4's STOP is made, because Q4 is not reached.

**Owner cash after every real cost** (operating cash flow, less stock pay, less all capital spending; the depreciation
variant beside it, Part VI convention; `value.py`; $M):

| year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| A: all capital spending | 24.4 | -44.4 | 30.9 | 2.7 | 125.1 | 77.3 | 82.5 | -22.1 | 2.7 | 217.4 |
| B: depreciation of property in place of capital spending | 11.6 | -51.7 | 43.5 | 19.8 | 126.6 | 85.8 | 110.4 | 8.4 | 18.3 | 250.1 |

- Five-year average 2021-2025: **A $71.6M; B $94.6M** (net income averaged $81.6M). Owner cash after every real cost,
  "a figure calculated after interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**,
  never a net-income proxy (operator rule 5). The single year 2025 (217.4) is not the base **[L2005-003]**.
- Growth shown, aggregate, five-year average against the prior five-year average: A 20.9% a year, B 25.9%. It is
  measured from a poor base (2016-2020 includes 2017's negative year and the acquisition years) and is partly bought
  (acquisitions of $79.7M in 2019 and $110.7M in 2022). Under the Part VI construction it is capped: no rate that runs
  past the discount rate **[M1997-095]**, so the shown-growth case is carried at 5.63% for ten years, then at zero
  nominal growth.
- Rate: 5.63% **[L2000-021]**, **[M1996-025]**. Net cash at 2026-06-30 of $128.5M (cash 137.9 less debt 9.4, 10-Q)
  added; Valley is treated as bought at what was paid (its $93.0M of cash and $235.0M of borrowing offset by its price).
  Shares 15,569,250.

**Value range (COMPUTATION):** **$90 to $177 a share** (A: $90 no growth to $136 capped growth; B: $116 to $177), a width
of about 2.0 to 1, inside the three-to-one width of the convention. Range, not a point **[L2000-024]**.
- **Against the price of $305.16:** the price sits about 72% above the top of the range. Expected return at the price
  (the internal rate on the same cash streams): 1.6% to 2.6% on A, 2.1% to 3.3% on B; even 20% growth for ten years,
  uncapped, gives only 7.0% (A) and 8.7% (B). All are below the floor of about ten percent, "a point at which we drop out
  of the game" **[M2003-149]** (floor CONVENTION, Part VI, from **[M1994-004]**, **[L2002-020]**, **[M2003-151]**). Had
  Q7 been reached it would close OUT through the floor, as Part VI provides for a price above the range.
- **FAIR-PRICE BAND (COMPUTATION):** prices inside the range at which the expected return is at or above about ten
  percent: **about $90 to $98**, and only on variant B with the capped growth; on variant A no price inside the range
  clears the floor (the ten-percent price is $76, below the range's bottom of $90). With the 2022 acquisition counted as
  capital spending the band is empty (range $65 to $96; ten-percent price $40 to $55).
- **CHEAP PRICE (COMPUTATION):** **about $54 a share**, the price at which the lower owner-cash figure (A, $71.6M) with
  no growth at all returns ten percent; below it the case would need no pencil **[M1996-084]**, **[M2009-005]**. The
  cheap price is ours, a CONVENTION for this report: the worst reading of the record clearing the floor unaided. It does
  not reopen Q2.

---
## THE BOX
**OUT**, decided at **Q2**: the castle is shown open on the filer's own words, its largest competitor's words and sixteen
years of margins and returns at the bottom of five peers **[M2011-015]**, **[M2012-106]**. Not TOO HARD: the deciding
question was answerable from the filings and was answered. COMPUTATION only: value range $90 to $177 against $305.16;
fair-price band about $90 to $98 (variant B only); cheap price about $54.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed: this run was dispatched
      with an instruction not to commit; the dispatcher commits.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its accession;
      no number without a row or a filing, except the cheap-price definition, labelled CONVENTION.
- [x] The order was kept; Q2 closed the file OUT; nothing after it is a clearance; Q3 to Q12 are NOT REACHED; the value
      arithmetic is under COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the US Treasury curve (via
      `tools/run.py`, dated 2026-10-02); the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (six items, three of them for the business).
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its known defects checked: share count (agrees with the
      cover), stock pay (not printed as 0; agrees with the filing), operating cash (no securities purchases in MYRG's
      cash-flow statement; agrees).
- [x] `python tools/check_framework.py` PASS (recorded at the end of the session that wrote this file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) The Q7 range convention says the cash input "deducts all capital spending" (Part VI) but does not say whether
acquisitions are capital spending. For a contractor that grew partly by purchase (and whose growth input is measured
from that purchased growth) the answer moves the range from $90-$177 to $65-$96. I kept acquisitions out of the main
range and showed them as a sensitivity; the convention should say which. (2) The convention measures "the growth the
business has actually shown" (Part VI) without saying how on a series that turns negative (2017, 2023): I used five-year averages
against the prior five-year averages, which avoids a picked base year **[L2005-003]** but is ours. (3) The owner's
"fair-price band" and "cheap price" are reporting requests with no row and no Part VI definition; the floor is stated as
"about ten percent pre-tax" while the owner cash is after corporate tax. I treated the internal rate on after-tax owner
cash as the buyer's pre-tax return (the buyer's own tax not yet paid), which is the stricter reading for a company, and
defined the cheap price as the no-growth, lower-cash case at the floor; both should be written into Part VI if the owner
keeps asking for them. A smaller point: Q2's tests are written for brands and franchises; for a bid contractor the
customer-choice test (test 8 of the framework) is answered by the contract form, and the framework could say that the
filer's description of how work is awarded is the primary evidence for it.
