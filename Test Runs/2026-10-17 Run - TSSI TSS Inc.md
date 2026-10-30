# Company Run — TSS, Inc. (Nasdaq: TSSI) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the brief's two stated departures
(the lines of evidence derived by the analyst from the 10-K's Items 1, 1A and 7; the competitors are those the 10-K names,
or, if it names none, up to three SEC filers chosen as a CONVENTION of this run). SEC CIK 0001320760. Formerly Fortress
International Group, Inc. (until 2013). Research folder: `Test Runs/_research 2026-10-17 TSSI/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (cb3bd014): not held; `PORTFOLIO.md` has no line for TSSI, TSS or Fortress.*

**Contamination, declared and not used.** (1) At the start of the run, before reading the blind rule closely, I ran a
file-name search of the `Test Runs/` listing for "tssi", "tss " and "fortress" (one `ls | grep` command). It printed no
match. That is a search the blind rule forbids; I declare it. Its only content is that no file name in `Test Runs/`
contains those strings; I did not use it. (2) The session context showed recent commit subjects about another company
(MEC) and an untracked research folder of two other companies (AYI, ARCB), and the memory index lines about the queue
(a wave paused at a named ticker, a count of gate-clearers). None concerns this company; none was used. (3) Reading
`.gitignore` to keep raw filings untracked showed comments naming other runs (SNPS, DELL, MGM research folders); not
opened, not used.

**Lines of evidence (the brief's departure 1), chosen from the 10-K's Items 1, 1A and 7 and why.** From Item 1 and Item 7:
(a) the three segments (procurement, systems integration, facilities management) and their revenue and margin over the
span, because the business changed shape in 2024; (b) the long-term AI rack integration agreement with the largest
customer (signed October 2024, amended December 2025), because it carries the fixed fees, the facility and the debt; (c)
the procurement business's gross and net deals and its factoring, because it is 80% of 2025 revenue. From Item 1A: (d)
customer concentration (99%, 99%, 96% of revenue in 2025, 2024, 2023), the first risk factor; (e) "Future power demands of
AI-enabled computer racks is unknown"; (f) rapid technological change in the industry served; (g) the material weakness in
internal control, unremediated at 2025-12-31; (h) the factoring arrangement and vendor credit. Also covered as the brief
requires: debt and leases, share issuance and buybacks with prices, stock pay, the auditor change, litigation. Chosen
because each one bears on whether the ten-year economics can be foreseen (Q1) or on the facts later questions would need.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $7.07 (close 2026-10-16, printed by `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
  For scale only: 3,000,000 shares plus a 450,000-share over-allotment were sold at $17.00 in August 2025 (8-K filed
  2025-08-15, accession 0001654954-25-009676).
- **Shares by class** from the latest filing's cover: 28,219,070 common, one class, as of 2026-08-07 (10-Q/A for the period
  ended 2026-06-30, filed 2026-08-14, accession 0001654954-26-007668; `python Screens/cover_shares.py TSSI`). Check: the
  balance sheet at 2026-06-30 shows 28,200 thousand issued and outstanding and no treasury shares (treasury shares were
  retired in 2025). Other counts filed: 27,773,594 at 2026-03-11 (10-K cover), 28,073,956 at 2026-05-01 (10-Q for Q1,
  accession 0001654954-26-004534). **Not reconciled:** the proxy (DEF 14A filed 2026-04-23, accession
  0001140361-26-016374) states 28,860,368 shares outstanding at the 2026-04-07 record date, about 1.09 million above the
  March count and 0.79 million above the May count; no filing read explains the difference. The cover count is used. No
  8-K or prospectus after the 10-Q changes the count (the only later filing is a Form 4 of 2026-10-06).
- **Market cap:** $199.5M (28.219M x $7.07).
- **Sovereign for the earnings currency (USD):** 5.43%, US Treasury daily par yield curve, 30-year, 10/16/2026
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-03-18, accession 0001654954-26-002342 (Items 1, 1A, 2,
  3, 5, 7, 8 and the notes on revenue, tax, debt, leases, stock pay); 10-Q for the period ended 2026-06-30, filed
  2026-08-13, accession 0001654954-26-007589, and its 10-Q/A filed 2026-08-14, accession 0001654954-26-007668 (the
  amendment's stated sole purpose is to complete inline XBRL tagging; text read from the amendment); 10-Q for Q1 2026,
  accession 0001654954-26-004534 (cover); proxy DEF 14A filed 2026-04-23, accession 0001140361-26-016374; 10-K for FY2024,
  accession 0001654954-25-004295, and FY2023, accession 0001437749-24-009879 (concentration, material weakness); NT 10-K
  filed 2025-03-31, accession 0001654954-25-003688; 8-Ks: 2025-01-07 (Susser Bank term loan, 0001654954-25-000152),
  2025-07-16 (auditor change, 0001654954-25-008149), 2025-08-15 (offering, 0001654954-25-009676), 2025-09-23
  (incremental loan, 0001654954-25-011027), 2025-11-13 (results and a director appointment, 0001654954-25-012990),
  2026-08-13 (Q2 results, exhibit 99.1, 0001654954-26-007587). **One figure cross-checked against the filed statement:**
  net cash from operating activities FY2025, $34,863 thousand on the filed cash-flow statement (10-K, accession
  0001654954-26-002342), equals the tagged figure `tools/run.py` prints (34.9M); cash at 2025-12-31, $85,510 thousand,
  likewise.
- `python tools/run.py TSSI` arithmetic lines only (output kept in the research folder, `run_py_output.txt`): operating
  cash less stock pay less capital spending, by year, $M: 2023 -9.1, 2024 5.6, 2025 -1.8; three-year mean -1.8 on the
  capex basis and 10.5 on the depreciation basis; five-year mean -0.5 (capex) and 6.7 (depreciation). Capex 2024 8.5 and
  2025 32.7 (the Georgetown facility build-out); D&A 2025 3.8; stock pay 2023 0.6, 2024 1.2, 2025 4.0. No securities,
  intangible or software lines inside operating cash. Nothing `tools/run.py` prints as a rule, id or verdict is used.

**The balance sheets, ten year-ends, read before the income account (`tools/run.py` table, first-filed XBRL; 2024 and 2025
read on the filed statements)** **[M2025-032]**. Required here because the file closes before Q4. USD thousands:

| year-end | assets | equity | cash | receivables | inventory | debt | accumulated deficit |
|---|---|---|---|---|---|---|---|
| 2016 | 8,576 | -1,431 | 2,152 | 2,389 | 59 | 1,071 | -68,423 |
| 2017 | 6,727 | -305 | 2,268 | 990 | 134 | 1,656 | -67,657 |
| 2018 | 9,110 | 2,481 | 6,178 | 727 | 108 | 1,838 | -65,220 |
| 2019 | 17,567 | 2,869 | 8,678 | 3,865 | 1,353 | 2,028 | -65,094 |
| 2020 | 23,808 | 3,183 | 19,012 | 915 | 197 | 2,234 | -65,015 |
| 2021 | 19,281 | 2,203 | 7,992 | 1,846 | 847 | 2,023 | -66,312 |
| 2022 | 31,406 | 2,934 | 20,397 | 2,745 | 862 | 0 | -66,385 |
| 2023 | 25,600 | 3,549 | 11,831 | 3,527 | 2,343 | 0 | -66,311 |
| 2024 | 96,568 | 7,138 | 23,222 | 16,203 | 17,673 | 8,200 | -60,335 |
| 2025 | 184,935 | 76,635 | 85,510 | 12,501 | 15,966 | 18,014 | -45,210 |
| 2026-06-30 | 175,321 | 80,296 | 67,679 | 14,320 | 16,962 | 16,080 | -41,502 |

What the figures say: for eight year-ends the company carried equity of less than $3.6M against an accumulated deficit of
$65M to $68M; it earned almost nothing on its books from 2016 to 2023 (cumulative change in the deficit, 2016 to 2023,
about $2.1M). Cash in those years moved with procurement payables, not with earnings (2020 $19.0M, 2021 $8.0M, 2022
$20.4M, 2023 $11.8M). Then three things arrived at once: in 2024 receivables and inventory rose by about $28M against
payables up about $39M (procurement scale), a $24M lease right-of-use asset (the Georgetown lease to 2035) and $8.2M of
bank debt; in 2025 equity rose by $69.5M, of which $55.3M was the stock offering and $7.9M the release of the tax
valuation allowance (a non-cash deferred tax asset); retained earnings from operations supplied the rest. Goodwill is $0.8M
and intangibles nil, so equity is nearly all tangible. What they do not say: whose cash the year-end cash is. At
2025-12-31 accounts payable were $46.4M and deferred revenue $13.9M against cash of $85.5M; six months later deferred
revenue had fallen to $2.8M and cash to $67.7M, with operating cash of -$7.3M for the half year. What they cannot say:
anything about the customer contract's term or renewal, which is not filed (the 10-K exhibit list carries the Susser
Bank agreements and the executive agreements, and no instance of the customer agreement).

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. Here the
honest answer turns on one customer and one contract that the filings do not let me read, so the foundation that bears is
the margin of safety, "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**, and the analyst's habit of writing contrary evidence down. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the AI rack agreement carries fixed monthly fees and staffing fees that the filer says cover the
facility, labor and debt service, and on termination for convenience the customer "would remain obligated to pay us
amounts that we believe would be sufficient to cover the related facility costs and debt service costs" (10-K, Item 1);
(2) the customer relationship is long: 96% of revenue in 2022 and 2023 came from the same OEM (10-K FY2023, accession
0001437749-24-009879), and the December 2025 amendment extended the term by two years with automatic renewals; (3) net
cash of about $51.6M at 2026-06-30 against a market cap of $199.5M; (4) in April 2026 the same customer took the idle Round
Rock building for warehousing through March 2029 (10-Q/A); (5) facilities management earns gross margins near 50% to 60%
and the company has integrated over 500 modular data centers. Each of these makes the next few years more foreseeable; none
reaches ten.

## THE STANDING RULE
A purchase would be made with cash, without borrowed money, and sized so that its loss to zero could not touch what the
buyer has and needs: "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing about this name requires
otherwise. Passes as a matter of the buyer's conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The question: "the first question is, can I understand it?" **[M1995-051]**, where understanding is "a reasonable fix on
about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**, "where the
business will be in 10 years" **[M2000-037]**. I understand what the company does: it assembles and tests customers'
servers in racks under consignment, resells hardware it buys from vendors, and maintains modular data centers. The
product is plain. The question is the economics in ten years, and the rows say the two are different things **[M2012-065]**.

**The tests, applied to the filings.**
1. **Where will it be in ten years? (test 1)** The business of 2026 did not exist in 2023. Revenue was $27.4M in 2021 and
   $245.7M in 2025; 80% of 2025 revenue ($197.5M) was procurement at a 7.7% gross margin; systems integration rose from
   $8.8M (2023) to $40.3M (2025) on AI rack integration that began in June 2024; facilities management was flat at about
   $8M with maintenance revenue falling because "more MDCs are being retired compared to the number of new MDCs being
   deployed" (10-K, accession 0001654954-26-002342, Items 1A and 7). Half-year 2026 revenue fell 37% to $90.5M as
   procurement fell 53% (10-Q/A, accession 0001654954-26-007668). There is no settled shape from which to look out.
2. **The key variables, and how predictable they are (test 2)** **[M1998-044]**: (i) the volume and terms the single OEM
   customer gives the company: 99%, 99% and 96% of revenue in 2025, 2024 and 2023 (10-K, Item 1A), the customer
   agreement not filed, terminable for convenience by either party on 180 days' notice (10-K, Item 1); (ii) the power and
   cooling each new generation of AI racks will need, which the filer itself calls unknown: "Future power demands of
   AI-enabled computer racks is unknown" (10-K, Item 1A), with 15 megawatts contractually committed by the city and no
   guarantee of more; (iii) procurement volume, which the filer says "has been unpredictable and subject to large
   fluctuations" and is tied to federal buying (10-K, Item 7). The rows: "If something is not very predictable, forget
   it." **[M1998-044]**. None of the three is.
3. **Do the past statements tell me the future ones? (test 3)** "do I understand enough about this business so that the
   financial statements will tell me the information that’s useful to me in making a judgment about what the future
   financial statements are going to look like" **[M2008-033]**. No: the ten balance sheets above describe a near-zero-
   earning integrator of the 2010s; the last two describe a different business built on one 2024 contract.
4. **Important and knowable? (test 4)** The customer's choices for the next ten years are the most important fact here and
   are not knowable from outside: "If something’s important but unknowable, forget it." **[M2006-076]**.
5. **Would the insiders write it down? (test 5)** The filer's own management does not: it writes that power demands are
   "unknown", that procurement "we cannot accurately predict", and (Q2 2026) "We do not rely on a predictable flow of
   business" (10-Q/A); its only forward figure is a one-year Adjusted EBITDA outlook (press release, exhibit 99.1 to the
   8-K of 2026-08-13, accession 0001654954-26-007587). "They would say, “That’s too hard.”" **[M2000-105]**.
6. **Can I name the winner? (test 6)** The 10-K says it competes against "channel resellers and divisions of large
   information technology service and equipment providers" with resources "that exceed our own" (Items 1 and 1A). That
   rack integration for AI data centers will grow may be seen; who will do it in 2036, and at what return, cannot: "we don’t
   have the faintest idea who the winners will be" **[M2012-067]**.
7. **Customers or technology? (test 7)** Technology. The company's own description of its growth is each new GPU and
   cooling generation; in August 2026 it began "a ~$17 million investment" "in readiness for the next generation of AI
   data center technology" (exhibit 99.1, accession 0001654954-26-007587), after $48M on the Georgetown facility through
   2026-06-30 (10-Q/A). The 10-K's own risk factor: "The mission-critical information technology industry is characterized
   by rapid technological change". The rows: "where we think the future technology could hurt the business as it
   presently exists [...] it won’t make it through the filter" **[M1998-008]**; "a business that must deal with
   fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**;
   "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on that"
   **[M1999-063]**.
8. **How far off could I be? (test 8)** "we also have some model in our mind of how far off we can be" **[M2011-084]**. Here
   the plausible outcomes run from a business whose one customer brings rack integration in house or moves it to a larger
   integrator, leaving a long lease (Georgetown to May 2035) and bank debt, to one whose revenue keeps doubling. No narrow
   range exists.
9. **Do I doubt it is inside? (test 9)** Yes: "if you have doubts about something being into your circle of competence, it
   isn’t" **[M2002-092]**.

**Routing.** The framework fixes it: a business whose ten-year economics cannot be foreseen because its industry changes
fast closes at Q1 in TOO HARD **[M1998-008]**, **[L1993-023]**; the box is "too hard" **[M2006-013]**, and it is not a
judgment of quality: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth.
It just means that we don’t know how to evaluate it." **[M2000-038]**.

**The cause: NATURE, not WORK.** The deciding question (what this one customer will buy from this company, in what rack
generation, at what power, ten years out) is a forecast the industry's insiders do not write down **[M2000-105]**, and the
filer, the insider nearest to it, calls the central input unknown. No filing not yet read would answer it: the customer
agreement is not filed, and if it were, a contract terminable for convenience on 180 days' notice does not reach ten years.
"We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries."
**[L1993-023]**; "we’re not going to learn enough in the followings five months to make up for the fact that we went in
deficient in the first place" **[M2008-086]**. A lower price does not reopen it **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE).** The ten-year economics depend on one customer (99% of 2025 revenue, 10-K accession
  0001654954-26-002342) and on AI rack power needs the filer calls "unknown", in an industry it calls one of "rapid
  technological change" (10-K, Item 1A). Rows: **[M2012-065]**, **[M1998-044]**, **[M2000-105]**, **[L1993-023]**,
  **[M2002-092]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed the file). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting figures are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1**: the ten-year economics rest on one customer (99% of 2025 revenue) and on AI rack
power and cooling needs the filer calls "unknown", in an industry it calls one of rapid technological change; no filing
or study answers what that customer will buy in ten years. Integrity facts recorded, not judged (see AFTER THE STOP, Q5).
For the owner's report only, COMPUTATION, NOT A CLEARANCE: value range $5.98 to $8.08 a share (all-equity basis,
maintenance case) against $7.07, with the all-spending case beside at $1.22; no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q1 closed the file. Facts already found that bear on later questions, each with its source **[M1997-127]**; written down,
not weighed; no verdict; the box unchanged, operator rule 2.)*

**Bearing on Q2 (the castle).**
- Concentration: one OEM customer, 99% / 99% / 96% of revenue in 2025 / 2024 / 2023 (10-K, accession
  0001654954-26-002342, Item 1A) and 96% in 2022 (10-K FY2023, accession 0001437749-24-009879). The 10-K does not name the
  customer; it describes "a global Fortune 100 information technology company with a significant presence near our
  headquarters". A director appointed 2025-11-11 was then Special Advisor to the Vice Chair and Chief Operating Officer of
  Dell Technologies (8-K, accession 0001654954-25-012990; the proxy says he held that role until April 2026). Recorded as
  found; the filings read do not identify the customer.
- Terms: most components are consigned by the customer, so integration revenue is a service fee; the AI rack agreement is
  terminable for convenience by either party on 180 days' notice; other contracts "are cancelable on short notice"; "we
  continue to experience some price pressure as some companies are willing to take on projects at lower margins" (10-K,
  Item 1A). The company invested about $40M (10-K) and then $48M through 2026-06-30 (10-Q/A) in a leased facility, plus a
  planned ~$17M "in readiness for the next generation of AI data center technology" (exhibit 99.1, 8-K accession
  0001654954-26-007587).
- **The competitor row (the brief's departure 2).** The 10-K names no rival; it names "channel resellers and divisions of
  large information technology service and equipment providers". **CONVENTION of this run:** three SEC filers chosen as
  the nearest public analogues of the two large segments, rack and systems integration (Sanmina, SANM; TD SYNNEX, SNX,
  whose integration arm builds racks for data centers) and IT procurement with services (ePlus, PLUS); rationale: they file
  full statements with the SEC and sell the same two services to the same kind of buyer. No non-filing rival is named in
  the 10-K, so none is flagged. Metric: operating income over revenue, each from its own 10-K XBRL (output
  `peers_output.txt`; accessions as listed there):

  | | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
  |---|---|---|---|---|---|
  | TSSI (calendar year) | -3.0% | 3.0% | -0.4% | 3.9% | 2.6% |
  | Sanmina (FY ends Sept/Oct) | 4.2% | 4.7% | 5.1% | 4.4% | 4.4% |
  | TD SYNNEX (FY ends Nov) | 2.0% | 1.7% | 1.9% | 2.0% | 2.3% |
  | ePlus (FY ends March of the next year) | 8.1% | 8.0% | 7.1% | 6.8% | 6.8% |

  TSSI 2023 to 2025 on the FY2025 10-K's presentation (bank factoring fees inside operating income); 2021 and 2022 as first
  reported, with factoring fees then below operating income, so those two years are flattered against the later three.
  Across the span TSSI earned a lower operating margin than the integration and services peers and about the margin of a
  distributor. Recorded, not judged.

**Bearing on Q3 (capital).** Capital spending 2024 $8.5M and 2025 $32.7M against depreciation of $0.6M and $3.8M; first
half 2026 $4.6M in cash plus $5.6M financed through payables (10-Q/A). Lease liabilities $22.7M at 2026-06-30 (Georgetown
to May 2035; the Round Rock lease to March 2029, now used for the customer's warehousing). Operating income: 2024 $5.8M,
2025 $6.3M (10-K, FY2025 presentation); half-year 2026 pre-tax income $4.5M (exhibit 99.1).

**Bearing on Q4 (the accounts).**
- Material weakness in internal control identified in the FY2024 audit ("ineffective design of certain management review
  controls", with "adjustments that were and could have been material to our 2024 consolidated financial statements") and
  not remediated at 2025-12-31 (10-K, Item 1A and Item 9A). The FY2024 10-K was filed late after an NT 10-K (accession
  0001654954-25-003688).
- Auditor change: Weaver and Tidwell dismissed 2025-07-10 by the audit committee; no disagreements; one reportable event,
  the material weakness; BDO USA engaged 2025-07-15 (8-K, accession 0001654954-25-008149).
- 2025 net income of $15.1M includes a $7.9M non-cash release of the tax valuation allowance; pre-tax income was $7.5M, of
  which $1.7M was interest income on the offering proceeds (10-K).
- 2025 operating cash of $34.9M included a $10.5M rise in deferred revenue and year-end procurement timing the filer itself
  describes; in the first half of 2026 deferred revenue fell $10.9M and operating cash was -$7.3M (10-Q/A). Operating cash
  for the twelve months to 2026-06-30: $34.9M - $37.0M + (-$7.3M) = -$9.4M (arithmetic on the filed figures).
- The company features "Adjusted EBITDA" in its releases, defined before "stock-based compensation" among other items, and
  gives an outlook for it ("We maintain our 2026 outlook for Adjusted EBITDA to be at the upper end of our $20 million to
  $22 million range") and says it uses the measure "as a factor in evaluating the performance of certain management
  personnel when determining incentive compensation" (exhibit 99.1, accession 0001654954-26-007587). The rows the
  framework would weigh it under at Q4 and Q5 (not applied): **[L2016-006]**, **[L2015-003]**, **[L2019-006]**, **[M2002-026]**.

**Bearing on Q5 (the people; integrity facts recorded, not judged).**
- The adjusted-figure, guidance and incentive facts in the Q4 bullet above, which the framework carries to Q5 (Q4, the
  make-the-numbers habit).
- The material weakness, the late FY2024 10-K and the auditor dismissal above.
- The proxy reports that the chief operating officer failed to file two Forms 4 on time (a June 2024 award and a June 2025
  withholding), filed on 2026-04-22, "because of an administrative error" (DEF 14A, accession 0001140361-26-016374).
- The share count the proxy states for its record date (28,860,368 at 2026-04-07) does not reconcile with the 10-K and
  10-Q cover counts on either side (Step 0).
- Insider forms on EDGAR's index, counted, not read: Form 144 notices 10 in 2024, 7 in 2025, 7 in 2026; Forms 4 32, 17 and
  33. Directors and officers as a group own 15.97% (proxy, with options counted as the proxy counts them).
- Pay, 2025 (proxy): chief executive $3,081,505 in total, of which stock awards $2,416,950; finance chief $2,335,233; chief
  operating officer $2,289,657. The chief executive is 74. Company operating income for 2025 was $6.3M.

**Bearing on Q6 (the money and the owners).** Shares sold: 3,450,000 at $17.00 in August 2025 for $55.3M net (8-K,
accession 0001654954-25-009676), while the stock now trades at $7.07. Weighted diluted shares 18.4M (2021) to 27.2M (2025),
XBRL from the 10-Ks. Repurchases: $4.5M (2024) and $4.9M (2025) and $2.2M (half-year 2026), all described as shares taken
from employees to cover tax withholding or exercise prices on vesting, not a programme with a stated price (10-K, Item 5
and Item 7; 10-Q/A); December 2025: 988 shares at $9.46. No dividend. The issuance row the framework carries at Q6 (not
applied): **[L2014-015]**; the buyback row: **[L2016-002]**.

**Bearing on Q9 (debt and exposures).** Susser Bank term loan, $20M plus a $5M incremental loan, SOFR plus 3.0% with a 4.5%
floor, maturing 2030-01-05, secured by "a first priority lien on substantially all of VTC’s and the Company’s assets",
guaranteed by the company (8-Ks, accessions 0001654954-25-000152 and 0001654954-25-011027); $16.1M outstanding at
2026-06-30. Procurement is financed by vendor credit and "a single factoring arrangement" (10-K, Item 1A); factoring fees
$3.7M in 2025. Fixed power charges about $192,000 a month regardless of use (10-K, Item 7). A letter of credit
collateralized by $1.8M of restricted cash (10-Q/A). The rows the framework would apply (not applied): **[M1995-104]**,
**[L2014-023]**.

**Litigation.** "We are not a party to any material litigation in any court, and we are not aware of any contemplated
proceeding by any governmental authority against us." (10-K, Item 3).

### COMPUTATION, NOT A CLEARANCE: the value range and the fair price (the owner's reporting figures)
*(Operator rule 3. The file closed at Q1; nothing here is a verdict, a clearance or entry language. Script and output in
the research folder: `q7_computation.py`, `q7_output.txt`.)*

**Owner cash, USD millions, FY2021 to FY2025 (the five-year window).** Operating cash (which counts working capital, Q7
specific (d)) less stock pay, less capital spending; on the all-equity basis: after-tax interest income on the cash pile
removed and after-tax bank interest added back; bank factoring fees left inside owner cash as an operating cost
(**CONVENTION of this run**, rationale: factoring sells the procurement receivables and its cost is charged where the
business pays it, the same reasoning as Q7's inventory-secured trade finance convention, which does not name factoring);
federal tax at the 21% statutory rate on operating pre-tax income (Q7, Whose tax: the company paid no federal tax in the
window because of its loss carryforwards), the shelter's present value added separately.

| | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| all spending deducted | -10.98 | 13.65 | -9.39 | 3.96 | -4.18 | -1.39 |
| maintenance case (depreciation as the maintenance guess) | -11.46 | 13.80 | -9.45 | 11.84 | 24.80 | 5.91 |
| revenue | 27.4 | 30.6 | 54.4 | 148.1 | 245.7 | |

- **The specifics applied.** (e) The maintenance case is central, because the filing allows the guess: the 2024 to 2026
  spending is described as the build-out of a new facility for one contract and readiness for a new technology
  generation (10-K, Item 7; exhibit 99.1), so depreciation is taken as the maintenance need; the all-spending case is shown
  beside. (b) The series changes sign, so growth is measured between the halves of the window: 1.17 (2021-22) to 18.32
  (2024-25), about 150% a year. (f) Carried ten years that rate requires owner cash far above the highest share of sales
  earned (45% in 2022, a working-capital year), so growth is cut to the business's own sales growth, 73% a year from 2021
  to 2025, and then to the discount rate, 5.43%, the ceiling the specific sets. (a) The last window year is aberrational on
  the filer's own description (year-end procurement timing and a $10.5M deferred-revenue inflow that reversed in the first
  half of 2026); no full cycle exists for this business in its present form (two years old), so no cycle base can be
  built, and the literal window is the base, said so. Without the $10.5M deferred-revenue inflow the maintenance mean
  falls from 5.91 to about 3.8. (c) No acquisitions in the window.
- **Whose tax and the shelter.** Net operating losses of about $54M at 2025-12-31, a portion expiring from 2029 (10-K tax
  note). At the 2025 operating base and the 80% limit on post-2017 losses the shelter is used over about eleven years:
  present value $8.5M at 5.43%, $6.9M at 10%. The framework's convention is written for a shelter that runs out inside ten
  years; this one runs about eleven, so applying it is a **CONVENTION of this run** (rationale: the statutory rate with the
  shelter added is the more conservative reading and the margin over ten years is one year).
- **Net debt** at 2026-06-30 (10-Q/A): borrowings $16.08M less cash $67.68M = net cash $51.60M; restricted cash of $1.81M
  (collateral) left out; operating leases ($22.7M) left out, as the convention says, and said so.

**VALUE RANGE (all-equity basis, maintenance case central):** enterprise $108.8M (no growth) to $167.8M (5.43% for ten
years, then zero nominal growth), width 1.54 to 1; per share, adding net cash and the shelter, **$5.98 to $8.08 against
$7.07**. Beside it: the all-spending case, no-growth only (its mean is negative), enterprise -$25.6M, **$1.22 a share**;
the equity-only range (owner cash after interest, no net cash added), $4.38 to $6.59.

**The floor, tested first.** Enterprise value at the price, less net cash and the shelter: $139.4M. Return on it: maintenance
no-growth 4.2%, maintenance growth case 6.4% (internal rate), all-spending -1.0%. **No case earns the floor of about ten
percent at the price.** Had the file reached Q7, it would have closed OUT here, before the width test, by the CONVENTION in Q7
headed "The floor is tested first"; the row behind it: "there’s just a point at which we drop out of the game" **[M2003-149]**.

**FAIR PRICE (Part VII, each end valued at ten percent, the two averaged, after the company's tax):** **$4.64 a share on the
all-equity basis** (the two ends $4.16 and $5.11, each including net cash of $51.6M and the shelter at 10%); **$2.96 on the
equity-only basis**, beside it, which credits the cash pile only through its interest. Price $7.07. No cheap price is
reported (Part VII).

**Do the figures mean much?** Little, and that is the Q1 finding in numbers: the five-year mean is built from a business
that changed shape in year four, the last year's operating cash reversed in the next half-year, and trailing twelve-month
operating cash is negative.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5f0092bf, before the first EDGAR request); written question by
      question; committed after Step 0 and Q1, and again after this section.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's, not checked by
      me; the fold is the dispatcher's. A run not in the register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Not fully kept:** one file-name
      search of the `Test Runs/` listing for this company's names was run at the start (no match printed); declared under
      Contamination at the head of the file and not used. Nothing else from the blind list was opened.
- [x] Every v5 id resolves (checked by `tssi_check.py` in the research folder, below); every filing fact has its accession;
      the one count not reconciled (the proxy's share count) is stated as such.
- [x] The order was kept; Q1, the first STOP, closed the run; everything after it is AFTER THE STOP or COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (stock pay deducted; depreciation or all capital spending deducted; statutory tax),
      never a net-income proxy; the sovereign from the US Treasury curve; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (Foundations); the facts for later questions are under AFTER THE STOP, with
      "integrity facts recorded, not judged" in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the commit (run 2026-10-17; `checks_output.txt`), and `tssi_check.py` PASS (no E-ids; all ids in the v5 ledger; every quote beside an id found in its row).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Customer concentration has no home.** No question names a business that depends on one customer for 99% of its
revenue. I read it at Q1 as a key variable that is not predictable **[M1998-044]**; it could equally be read at Q2 (would
the customer still choose it over the low bid, **[M2017-009]**) or Q9 (whose promise does it depend on). Two analysts
could close the same file at Q1 TOO HARD (NATURE) or at Q2 OUT on these facts. (2) **Q7 (e) against (f).** (e) says charge
the growth spending "against the growth it buys" and never charge all spending while capping the growth; (f) then cuts a
150% shown rate to the discount rate. How much of the growth spending belongs against a growth that (f) has cut to 5.43%
is not said; I charged none of it in the growth case and showed the all-spending case beside. (3) **(a), the aberrational
last year, assumes a cycle exists.** This business has two years in its present form; no cycle base can be built, and the
text does not say what then. I used the literal window and showed the effect of the reversing item. (4) **Whose tax, the
ten-year edge.** The shelter convention applies to a carryforward that "run[s] out inside ten years"; here it runs about
eleven at the current base, and the text gives no rule for the near miss. (5) **Factoring.** The all-equity basis names
floor-plan debt; it does not name receivables factoring, which is this company's main financing. I kept factoring inside
owner cash, confessed above. (6) **The equity-only fair price** credits $67.7M of cash only through its interest at a 10%
discount, which values the cash at well below its face; the figure is printed as Part VII asks, but it reads as a
penalty for holding cash rather than a measure of the business. (7) **The blind rule and the first command.** The brief
forbids searching `Test Runs/` for this company, and a reflexive first-step search for an existing file is the natural
thing to do before copying a template; a sentence in the template's first step saying "do not look for an earlier file"
would have stopped me.

*check_framework.py and the id check: see the research folder's `checks_output.txt`.*
