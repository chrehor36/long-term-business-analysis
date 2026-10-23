# Company Run — Centuri Holdings, Inc. (NYSE: CTRI) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run, unattended overnight cycle of 2026-10-18. The template was copied to this name and committed
(914be484) before any fetch. Working folder: `Test Runs/_research 2026-10-18 CTRI/` (notes, scripts, the arithmetic
outputs; raw filings in its gitignored `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (03955ebd):** not held; Centuri Holdings (CTRI) does not appear in `PORTFOLIO.md`.

**Contamination declared.** No other run file, holding review, `PORTFOLIO.md`, resume-state file, register or reading list
was opened, listed or searched. Seen by accident and not used: the session's opening git status and recent commit subjects,
which name another company's v5 re-run and its fold (not this company); the memory index lines loaded with the session
(queue and wave counts, no mention of this company); a count of the files in `Test Runs/` (a number, no names, run to
confirm the dated path was free). Nothing about whether anyone holds or wants CTRI was seen.

**Lines of evidence chosen (the brief's departure: derived by the analyst, not listed by the dispatcher).** From the 10-K's
Item 1 (four segments, all utility labor under MSAs and bids; customers supply the materials; the 10-K names five national
rivals), Item 1A (the risk factors that bear on the castle: competitive bidding and few barriers, MSAs cancellable on 30 days'
notice and rebid, customer concentration, fixed and unit-price overruns, goodwill impairment, activist holders, NOL limits)
and Item 7 (thin gross margins by segment, storm work as the swing, interest nearly equal to operating income, the
securitization of receivables, sale-leasebacks, the Connect purchase): (1) the margin and cash record over ten years, because
a contractor's castle shows in what it keeps of revenue; (2) the field's returns from the named rivals' own filings; (3) the
balance sheets, because acquisitions, impairments, a receivables sale and a fleet shift to leases all live there; (4) the
debt and its cover. The S-1 era is read through the 424B4 of April 2024 (FY2021 to FY2023) and, for FY2016 to FY2020, the
former parent's own 10-K annual-report exhibits, where Centuri was the "utility infrastructure services" segment.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $19.73 (close 2026-10-16; aggregator quote via `tools/run.py`, flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: common stock, $0.01 par, **100,963,053** (10-Q for the quarter ended
  2026-06-28, filed 2026-08-04, accession `0001981599-26-000089`, cover as of 2026-07-31; `python Screens/cover_shares.py CTRI`).
  One class, no treasury: the balance sheet shows 100,956,691 issued and outstanding at 2026-06-28. Filings after the 10-Q: an
  S-8 of 2026-07-10 (plan registration, no issuance) and Forms 3 and 4 (grants); no offering after the November 2025 one.
- **Market cap:** $1,992.0M (100.963M x $19.73).
- **Sovereign for the earnings currency:** USD, **5.43%**, the 30-year par yield, US Treasury daily par yield curve, 2026-10-16
  (as fetched by `tools/run.py`). Canada is about 8% of revenue; the earnings currency of the filing is USD.
- **Filings read** (operator rule 4): 10-K FY2025 (fiscal year ended 2025-12-28), filed 2026-02-26, `0001981599-26-000020`
  (Items 1, 1A, 7, 8); 10-K FY2024, filed 2025-02-26, `0001981599-25-000008` (segment tables for FY2022 to FY2024); 10-Q Q2
  2026, filed 2026-08-04, `0001981599-26-000089`; proxy DEF 14A filed 2026-04-06, `0001981599-26-000046`; 424B4 IPO prospectus
  filed 2024-04-18, `0001193125-24-100835` (audited FY2021 to FY2023); the S-1 of 2024-03-22 (`0001193125-24-075215`) was
  not read separately, its final form being the 424B4; Southwest Gas Holdings 10-K FY2020 annual-report exhibit,
  `0001692115-21-000008`, and 10-K FY2018 Exhibit 13, `0001692115-19-000013` (Centuri segment FY2016 to FY2020); 8-Ks
  `0001981599-26-000088` with Ex. 99.1 (Q2 2026 results, 2026-08-04), `0001981599-26-000108` (officer changes, 2026-08-12),
  `0001981599-25-000069` (Icahn agreement, 2025-11-10), `0001981599-26-000035` (director Nielsen, 2026-03-20).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $78.1M in
  `tools/run.py`, is $78,121 thousand on the filed Consolidated Statements of Cash Flows (10-K FY2025); capital expenditures
  $86.3M against $86,325 thousand. Both agree.
- `python tools/run.py CTRI` arithmetic lines only (output kept at `Test Runs/_research 2026-10-18 CTRI/run_py_output.txt`):
  OCF less SBC less capex FY2023 to FY2025 $58.9M, $56.7M, -$16.3M (mean $33.1M); the D&A basis negative. **Read against the
  filing, the tool's FY2024 figure is wrong as owner cash:** FY2024 OCF of $158.2M contains a one-time $125.0M from the first
  sale of receivables into the securitization facility (10-K FY2025, MD&A, Operating Activities), and FY2025 proceeds from
  equipment sales include $37.8M of sale-leaseback (same, Liquidity). The recast is under Q4 and in
  `compute_output.txt`. SBC is resolved from the cash-flow statement each year (FY2021 $1.7M to FY2025 $8.1M). Finance-lease
  principal ($3.5M to $12.1M a year) is a capital payment outside capex and is deducted. No v4 material printed by the tool was
  used.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: what the owner gets is the cash the business itself produces
**[M1997-109]**, and here the business has turned rising revenue into very little cash for the owner over the window read.
The second is who is paid to tell you: the company's releases lead with "Adjusted EBITDA", "Adjusted Net Income" and "Base"
figures and a $16 billion "opportunity pipeline"; "don’t ask the barber whether you need a haircut" **[M2011-083]**, and the
numbers used below are the filed statements. No macro view enters: the AI and data-centre demand story in Item 1 is not
credited as a forecast **[M2000-094]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the business is
plainly simple and its customers, investment-grade utilities, are among the most durable buyers there are (10-K Item 1:
"top 20 customers are almost exclusively investment-grade utilities"); (2) about 78% of FY2025 revenue came under MSAs and the
backlog was $5.9B at 2025-12-28 and $6.4B at 2026-06-28 (Ex. 99.1, `0001981599-26-000088`); (3) revenue rose from $1,139M in
FY2016 to $2,983M in FY2025 and grew 32% in the first half of 2026; (4) Quanta, the largest rival, has widened its margin and
cash over the decade, which shows that this field can reward scale. Each is weighed where it bears.

## THE STANDING RULE
A part-interest bought for cash, without borrowed money, puts the buyer at no risk of ruin from this purchase; the rule
forbids only the buyer's own leverage and calls on him **[M2012-081]**, **[L2014-005]**. The target's own debt is weighed at
Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the framework states it:** "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
- **What the business is, from the filing.** Centuri sells crews and equipment to North American utilities: it replaces,
  maintains and installs gas distribution pipe and electric distribution and urban transmission lines, "between the substation
  and end-user meter" (10-K FY2025 Item 1, `0001981599-26-000020`). The customer supplies the materials ("materials used in our
  infrastructure service activities are specified, purchased and supplied by our customers", Item 1, Suppliers), so what is sold
  is labor and fleet time. 78% of FY2025 revenue came under MSAs, 22% from bid contracts; 56% of revenue was unit-priced, 23%
  time and materials, 21% fixed price. Four segments: U.S. Gas ($1,328M FY2025 revenue), Union Electric ($808M), Non-Union
  Electric ($599M), Canadian Operations ($247M). About 9,687 employees, 57% union.
- **The key variables and how predictable they are** **[M1998-044]**: (1) the utilities' spending on distribution
  replacement and upkeep, which the 10-K calls "highly predictable, non-discretionary, regulatory-driven investment" (Item 1,
  Our Industry); the direction is foreseeable, the timing is the customer's; (2) the price Centuri gets each time an MSA or bid
  is rebid, which the 10-K says "our customers generally require competitive bidding" (Item 1A); foreseeable in kind, a bidder's
  price; (3) crew cost and productivity under 332 collective agreements; (4) storm-restoration work, which swings a year's
  margin and is unforeseeable by its nature (the company itself strips it out as "Base" figures); (5) the long-run role of gas
  distribution, a slow policy question, not a fast technical one.
- **Do the past statements tell me the future ones?** **[M2008-033]** Yes, in the way that matters: ten years of filed
  figures (FY2016 to FY2020 as the former parent's segment, FY2021 to FY2025 as Centuri) show the same economics through two
  large acquisitions, a pandemic and two goodwill write-downs: operating margins of about 3% to 6% of revenue and little cash
  left after capital spending. A business whose figures repeat this steadily is a business whose ten-year economics can be
  pictured; what they picture is Q2's question.
- **Would the insiders write it down?** **[M2000-105]** The industry writes its forecasts down every year (backlog, guidance,
  pipeline in Ex. 99.1, `0001981599-26-000088`); none of the rivals' filings read calls the next decade unknowable. This is not
  a field of fast technical change; Item 1A's "Technological advancements" risk is a general paragraph, not a stated threat to
  the work.
- **Routing.** Not a business whose ten-year economics cannot be foreseen because its industry changes fast **[M1998-008]**;
  not a financial institution. The parts all sell the same thing (utility labor) and each can be read the same way, so the
  parts paragraph does not keep the whole outside the circle.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The doubts
  found are about whether the business is any good, which is the castle question, not about whether its economics can be
  seen. The economics can be seen; that is what makes Q2 answerable on evidence.
- **VERDICT: IN.** The business is simple, its key variables are named in its own filings, and ten years of statements show
  its economics plainly **[M2012-065]**, **[M1998-044]**, **[M2008-033]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**. The moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The castle tests, each with its filing fact.**
- **The attacker with money** **[M2011-015]**, **[M2012-106]**. The filer answers the question itself: "Relatively few
  barriers prevent entry into some areas of our business, and as a result, any organization that has adequate financial
  resources and access to technical expertise may become one of our competitors." It adds: "Certain of our competitors may also
  have lower overhead cost structures, and therefore may be able to provide services at lower pricing than us", and the
  customers themselves compete: "We also face competition from the in-house service organizations of our existing or
  prospective customers" (10-K FY2025, Item 1A, `0001981599-26-000020`). The field is "highly competitive and highly
  fragmented" with "many regional and local providers" (Item 1, Competition). Centuri itself entered the union electric market
  by buying Riggs Distler in August 2021 for $822.2M in cash (424B4, `0001193125-24-100835`, acquisitions note) and wrote down
  $177.1M of that goodwill in 2022 and $214.0M in 2023 (same, MD&A): the price of a position in this field was not supported by
  what the position earned. A field that any organization with "adequate financial resources" can enter gives the failing
  answer of the test: "there are some industries that are just never going to have barriers to entry" **[M2012-106]**.
- **Would the customer still choose it over the low bid?** **[M2017-009]**, **[L2004-003]**. The filing: "our customers
  generally require competitive bidding of these contracts. As a result, we could be underbid by our competitors or be required
  to lower the prices charged under a contract being rebid"; the MSAs "do not require our customers to commit to a minimum
  amount of services" and "may be cancelled by our customers for convenience upon minimal notice (typically 30 days)"; the
  business "is largely dependent on the competitive bidding process" (Item 1A). The customer buys on the bid, which is the
  failing answer: "most insureds don't care from whom they buy" **[L2004-003]**.
- **Pricing power and the agony before a rise** **[M2005-020]**. Escalation clauses exist but "the annual adjustment provided
  by certain contracts is typically subject to a cap and there can be an extended period of time between the impact of inflation
  on our costs and when billing rates are adjusted. Our actual costs at times can exceed the contractual caps" (Item 7,
  Inflation); and "we have recently experienced, and may in the future experience, more competitive pricing for smaller scale
  projects" (Item 1A). In Q2 2026 higher fuel cost alone took about 75 basis points off U.S. Gas gross margin and about 140 off
  Non-Union Electric (10-Q, `0001981599-26-000089`, MD&A): the cost was not passed through.
- **The low-cost position** **[L2000-017]**, **[M1997-010]**, **[M2001-013]**. No filing claims it, and the rivals' own figures
  do not show it: over FY2021 to FY2025 Centuri's operating margin (3.6% of revenue in aggregate) sat below Quanta's (5.5%) and
  Primoris's (4.9%) and level with MYR Group's (3.6%) (competitor row below). The filer itself says rivals may have "lower
  overhead cost structures". The textile row states the consequence: "The guy who could sell it cheaper than we could made it
  risky for us." **[M1997-010]**
- **Unit volume, brand, share of mind** **[M1999-054]**, **[M2008-075]**. Volume has grown (revenue $1,139M FY2016 to $2,983M
  FY2025, with acquisitions), but the volume is crew time sold on bids; the "brand" the 10-K claims (Item 1) is a reputation for
  safety and capability, which earns the right to bid, not a price above the low bid. No filing fact shows a customer paying
  more for Centuri by name.
- **Ask the competitors** **[M2025-043]**. Not done (no interviews in a filing-only run); the filer names Quanta, MYR Group,
  MasTec, Primoris and Everus as its national competitors (Item 1), and three of their filings are read below instead.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Narrowing on the evidence. Centuri's operating margin was 5.2% of
  revenue over FY2016 to FY2020 (the former parent's segment table) and 3.6% over FY2021 to FY2025 (goodwill impairments added
  back), while all three rivals read widened theirs between the same halves (Quanta 4.7% to 5.5%, MYR 3.1% to 3.6%, Primoris
  4.3% to 4.9%). The largest segment's gross margin went 6.4% (FY2022), 9.1%, 5.5%, 5.4% (FY2025), and 4.2% in Q2 2026 (5.9%
  before the $9.0M City of Chicago revenue reversal) on 45% more revenue (10-Q). Revenue from the former parent, once its
  captive customer, fell from $158.7M in 2019 (SWX 10-K FY2020 exhibit, `0001692115-21-000008`) to $97.6M in FY2025.
- **What could destroy, modify or reduce it** **[M2000-014]**. Rebids at lower prices; customers taking work in-house (Item
  1A names the pressure "to self-perform"); a slow policy turn against gas distribution, U.S. Gas being the largest part; the
  loss of a top customer (the top ten were 48% of FY2025 revenue). None needs to happen for the returns to stay thin; they are
  thin now.

**The competitor row** (same metrics, each from the company's own 10-K XBRL facts, first-filed values; the comparison is over
the whole span read, never one year; output at `Test Runs/_research 2026-10-18 CTRI/peer_table_output.txt`). The 10-K names
five rivals, all SEC filers; the three chosen are the closest in work to Centuri's distribution crews (Quanta's electric and
underground utility work, MYR Group's transmission and distribution segment, Primoris's utilities segment); MasTec and Everus
are named and not read (MasTec is weighted to communications, clean energy and pipelines; Everus files separately only from
its 2024 spin-off).

| company (accession of FY2025 10-K) | operating margin FY2016-20 | FY2021-25 | owner cash after all spending (OCF less SBC less capex), % of revenue over the span | pre-tax operating income / tangible assets, FY2025 |
|---|---|---|---|---|
| Centuri (`0001981599-26-000020`; FY2016-20 from SWX `0001692115-19-000013`, `0001692115-21-000008`) | 5.2% | 3.6% (impairments added back) | 0.4% FY2021-25 as filed; -0.5% with the FY2024 receivables sale taken out | 5.6% |
| Quanta Services (`0001050915-26-000006`) | 4.7% | 5.5% | 3.8% FY2017-25 | 11.0% |
| MYR Group (`0000700923-26-000007`) | 3.1% | 3.6% | 2.0% FY2016-25 | 11.5% |
| Primoris Services (`0001104659-26-018677`) | 4.3% | 4.9% | 2.6% FY2016-25 | 12.2% |

**The parts table** (the filer reports four segments with different margins; its segment measure is gross profit, with SG&A
and amortization not allocated, so gross profit is the measure; the four-segment basis is filed for FY2022 to FY2025 only, in the
10-K FY2025 and FY2024 segment tables, so the span is four years, said so):

| part | gross profit FY2022-25, $M | share | gross margin FY2022 / 23 / 24 / 25 | castle | decides |
|---|---|---|---|---|---|
| U.S. Gas | 351.0 | 36.8% | 6.4% / 9.1% / 5.5% / 5.4% | bid and MSA labor for gas utilities; no barrier claimed; margin narrowing | **yes, the largest part** (no part above half) |
| Non-Union Electric | 228.0 | 23.9% | 10.8% / 12.3% / 12.7% / 9.8% | MSA labor; its best years carry storm work | no |
| Union Electric | 224.2 | 23.5% | 5.9% / 6.9% / 8.4% / 8.8% | the Riggs Distler business whose goodwill was written down by $391.1M | no |
| Canadian Operations | 151.2 | 15.8% | 12.8% / 14.1% / 15.8% / 18.6% | the best margins, about 8% of revenue | no |

The file closes on the deciding part, U.S. Gas, whose margin is the thinnest of the four. No part, read alone, shows a castle on
the filing's own words: the barrier, bidding and in-house paragraphs of Item 1A speak of the whole business.

**The field's returns over the span read, judged in words** (the framework's CONVENTION: "ordinary" carries no figure). The
durable players of this field, Quanta the largest, keep three to six cents of each revenue dollar as operating profit and two to
four cents as cash after all spending, and earn on their tangible assets, before tax, about what a long government bond plus a
modest margin earns. That is an ordinary return, earned by labor sold on bids, and the best of the field earns it through size
and acquisitions, not through a price the customer cannot refuse **[L2007-004]**, **[M2013-052]**. Centuri earns less than the
field's ordinary return and keeps almost none of it as cash. The ten years read include the 2020 slowdown and Centuri's FY2024
revenue fall (9%); no change for the better is claimed for Centuri, whose margin fell.

**What the evidence decides.** The castle is not tenuous in a way that cannot be judged **[M2000-019]**; it is judged, and it is
open: the filer says entry is easy and rivals may be cheaper, the customer buys on the bid and can cancel on thirty days, the
business is not the low-cost operator by the rivals' own figures, and its margin narrowed while theirs widened **[M2011-015]**,
**[M2012-106]**, **[L2004-003]**, **[M1997-010]**, **[M1999-108]**. And the field around it protects only ordinary returns,
which the framework closes OUT, not TOO HARD (Q2, What it rules OUT) **[L2007-004]**, **[M2013-052]**. Price does not reopen
it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The castle is shown open on the evidence of the filer's own risk factors and the rivals' filings, and the
  field protects only ordinary returns **[M2011-015]**, **[M2012-106]**, **[L2004-003]**, **[M1997-010]**, **[L2007-004]**.
  Q3 to Q12 are NOT REACHED; what was found for them is written below, not weighed.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0's sense before the close and are written under AFTER THE STOP, Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback line: no repurchase was found in the filings read (none in FY2023 to FY2025 cash-flow statements or the
Q2 2026 10-Q), so the test against the bottom of the Q7 range has nothing to read; that bottom, as computed below, is negative
on the central basis.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The two reporting figures the owner asks for are computed below under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
*(Operator rule 3: this arithmetic was done after Q2 closed the file. It carries no entry language and changes no box. The
script and its output are `Test Runs/_research 2026-10-18 CTRI/scripts/compute.py` and `compute_output.txt`.)*

**Owner cash by year, $M** (from the filed cash-flow statements: 424B4 `0001193125-24-100835` for FY2021 to FY2023, 10-K FY2025
`0001981599-26-000020` for FY2023 to FY2025). "All spending" is operating cash flow, less stock pay, less capital expenditures,
plus routine proceeds from equipment sales, less finance-lease principal; the FY2024 operating cash flow is taken without the
one-time $125.0M from the first sale of receivables into the securitization facility, and the FY2025 proceeds without the
$37.8M sale-leaseback (both as the 10-K's MD&A describes them). "Maintenance only" is the same before the change in working
capital (net income plus the filed non-cash items, less operating-lease payments). "All-equity" adds back cash interest after
tax.

| FY | revenue | all spending, equity-only | maintenance only, equity-only | cash interest after tax | all spending, all-equity | maintenance only, all-equity | net purchases of businesses and minority interests |
|---|---|---|---|---|---|---|---|
| 2021 | 2,158.7 | 9.8 | 75.4 | 13.7 | 23.5 | 89.1 | 822.2 (Riggs Distler) |
| 2022 | 2,760.3 | -36.1 | 27.5 | 42.4 | 6.3 | 69.9 | 39.6 (Linetec minority) |
| 2023 | 2,899.3 | 58.7 | 55.5 | 73.8 | 132.4 | 129.3 | 39.9 (Linetec minority) |
| 2024 | 2,637.2 | -69.7 | 21.2 | 58.7 | -11.0 | 79.9 | 92.9 (Linetec minority) |
| 2025 | 2,982.8 | -19.5 | 51.2 | 50.3 | 30.7 | 101.5 | 45.8 (Connect) |
| **5-yr average** | | **-11.4** | **46.2** | 47.8 | **36.4** | **94.0** | 208.1 a year |

**Owner cash, central:** **$94.0M a year on the all-equity basis, maintenance only** (its five-year average); $36.4M a year
after all spending including working capital; equity-only beside, $46.2M and -$11.4M. Net debt at the latest filed date: debt
$731.7M (current and long-term debt, line of credit, finance leases, 10-Q at 2026-06-28, `0001981599-26-000089`) less cash
$40.5M, plus the JJ White purchase of about $62.0M in cash that the same 10-Q states as a subsequent event (closed 2026-07-20):
**$753.3M**. Left out and said so: operating-lease liabilities of $197.5M at 2026-06-28, and receivables sold to the
securitization facility, $165.0M at 2026-06-28 (off the balance sheet; with them counted as debt the top of the range below
falls from $9.68 to $8.04 a share). Market value $1,992.0M; market value plus net debt $2,745.3M.

**Q7's range convention, specific by specific.**
- *Five-year average, ten years then zero nominal growth, at the long government rate 5.43%:* applied.
- *(a) Cycle base.* FY2021 holds Riggs Distler for about five months (acquired August 2021) and FY2024 holds the one-time
  receivables sale; the sale is taken out as an event, and the growth is measured on the full post-acquisition years (below).
  The literal window, all spending as filed with nothing taken out, averages $12.0M a year equity-only ($59.8M all-equity), shown
  beside: $3.45 a share at no growth on the all-equity basis.
- *(b) Decline.* The all-spending series changes sign, and its halves (FY2021-22 against FY2024-25: $14.9M to $9.9M all-equity)
  are dominated by working-capital swings, so its rate is meaningless and that case is taken at no growth alone, said so. The
  maintenance-only series falls between the full post-acquisition halves (FY2022-23 $99.6M to FY2024-25 $90.7M): -4.57% a year,
  carried as negative; shown beside, $4.47 a share.
- *(c) Acquisitions.* Net purchases over the window, $1,040.5M, exceed half of owner cash before purchases ($91.0M): the serial
  acquirer. The central figure is the organic pair (purchases left out, growth organic); the filer reports no organic growth, so
  the organic growth is measured on the full post-acquisition years, a CONVENTION of this run (below). The default pair beside:
  with acquisitions deducted the all-equity average is -$171.7M a year, and no positive value results. No signed, unclosed deal
  at the price date. JJ White closed after the window: no earnings of its own are filed, so it is credited at nothing and its
  price is added to net debt.
- *(d) Working capital.* Counted in the all-spending case. Receivables and contract assets rose from 19.7% of revenue (FY2024,
  after the $125.0M sale) to 23.8% (FY2025); the filer ties the FY2025 draw to many projects and approvals, not to one event, so
  no year is set aside for it.
- *(e) Maintenance central.* The filing allows a guess only this far: net capital spending ran below depreciation in FY2024 and
  FY2025 ($99.3M and $86.3M against $108.7M and $111.5M) while the fleet moved to operating leases whose payments are already
  inside operating cash, and net property fell from $548.9M (FY2022) to $466.8M (FY2025); so all net capital spending is taken
  as maintenance and the growth spending is the working capital. The growth bought by that working capital is worth less than its
  cost (revenue up, owner cash down), so the maintenance-only no-growth case is the top of the range and the all-spending case
  the bottom: "growth can destroy value" **[L2000-023]**.
- *(f) The cap.* No growth is carried, so nothing is cut.
- *The basis.* Centuri is not a regulated utility ("We are not directly regulated by the state utilities commissions or by the
  Federal Energy Regulatory Commission", 10-K Item 1), so the all-equity basis is central and the utility exception does not apply.
- *Whose tax.* Owner cash is after the taxes actually paid ($13.6M, $9.4M, $3.6M in FY2023 to FY2025). Federal NOLs of $301.1M,
  "some of which begin to expire in fiscal 2029" (10-K Note on income taxes), shelter part of the window's tax; computing at the
  statutory rate with the shelter's present value added would lower every figure below by a few million dollars a year; it was
  not computed, since it can only move the figures down, and no figure below is near the price.

**The floor, tested first.** The expected return at today's market value plus net debt: 3.42% on the top case (maintenance
only, no growth), 1.33% on the bottom case, 2.25% on the decline case, and 4.93% even on the window-halves growth of +4.49% a year
that counts Riggs Distler's part-year as growth. No case earns about ten percent at the price; at Q7 the file would close OUT
whatever the width.

**VALUE RANGE (reporting figure 1): -$0.82 to $9.68 a share against $19.73**, all-equity basis, central. Top: maintenance-only
owner cash of $94.0M at no growth, $1,730.2M less net debt $753.3M. Bottom: all-spending owner cash of $36.4M at no growth,
$670.0M less net debt. Beside it: the maintenance case at the post-acquisition decline, $4.47; the literal window, $3.45;
equity-only, -$2.07 to $8.43. The price is above the top of the range.

**FAIR PRICE (reporting figure 2): not positive on the all-equity basis, -$1.01 a share** (each end valued at ten percent:
top $940.0M less net debt, $1.84; bottom $364.0M less net debt, -$3.86; averaged). **Equity-only, beside it: $1.72 a share**
(top $4.58, bottom -$1.13, averaged). Company's own tax as paid, no conversion. The all-equity figure is the central one (Q7, On
what the floor is earned); the equity-only figure never decides alone. Neither figure is a verdict or entry language.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. No named business of the rows is involved (utility construction and maintenance labor).

---
## THE BOX
**OUT at Q2**: the castle is shown open on the filer's own words (few barriers to entry, customers require competitive bidding,
rivals may be cheaper, MSAs cancellable on thirty days) and the rivals' filings (Centuri's margin fell from 5.2% to 3.6% of
revenue between FY2016-20 and FY2021-25 while Quanta's, MYR Group's and Primoris's rose), in a field that protects only ordinary
returns. COMPUTATION beside it, not a clearance: value range -$0.82 to $9.68 a share against $19.73; fair price -$1.01
all-equity, $1.72 equity-only. Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; no verdict; the box unchanged.)*

**Q3, capital and returns.**
- Pre-tax operating income (impairments added back) on tangible assets (total assets less goodwill and intangibles): FY2022 5.1%,
  FY2023 9.4%, FY2024 6.4%, FY2025 5.6% (424B4 and 10-K balance sheets and income statements). On the former parent's segment
  assets, which include goodwill, operating income was 10.2% of assets in 2016 and 8.3% in 2020 (SWX exhibits).
- Revenue rose from $2,158.7M (FY2021) to $2,982.8M (FY2025) and maintenance-only owner cash did not rise with it (table above);
  receivables and contract assets rose faster than revenue in FY2025.
- Riggs Distler, bought for $822.2M in 2021 with borrowed money, had $391.1M of goodwill written off in 2022 and 2023 (424B4).

**Q4, the accounts (the balance sheets first** **[M2025-032]**). Full balance sheets are filed for four year-ends (FY2022 and
FY2023 in the 424B4, FY2024 and FY2025 in the 10-K) and the 2026-06-28 quarter; for FY2016 to FY2020 only the former parent's
segment total assets are filed ($579M, $752M, $1,216M, $1,365M, $1,475M); equity at the FY2020 and FY2021 year-ends is in the
424B4's equity statement. What moved:
- *Equity against goodwill:* equity $484.8M (start of FY2021), $479.6M, $386.8M (FY2022), $226.0M (FY2023), $555.6M (FY2024),
  $873.0M (FY2025), $868.9M (2026-06-28). Retained earnings went from $205.6M (start of FY2021) to -$128.4M (FY2025): the
  business has lost more than it kept since 2021, and the equity rose only from the IPO ($327.7M), the November 2025 offering
  ($250.9M) and $55.4M of tax attributes contributed at the separation. Goodwill $587.7M (FY2022) to $375.9M after the
  impairments, $395.7M (FY2025); intangibles $395.2M to $343.2M.
- *Receivables and contract assets against sales:* $632.1M (22.9% of revenue, FY2022), $617.3M (21.3%), $519.6M (19.7%, after
  $125.0M sold), $709.8M (23.8%, FY2025), $771.5M at 2026-06-28 with $165.0M sold. Contract assets alone rose from $235.5M to
  $394.5M in FY2025 (+67%) on revenue up 13%; the 10-K ties it to milestone billing and customer approvals.
- *Debt:* about $1,243M (FY2022, including finance leases), $1,187M (FY2023), $898M (FY2024), $754M (FY2025), $732M
  (2026-06-28), reduced with offering money, while off-balance financing grew (receivables sold $125M then $165M; operating-lease
  liabilities $124.6M at FY2023 to $197.5M).
- *The real costs:* depreciation $111.5M against capital spending of $86.3M in FY2025, with the fleet moved to leases (sale-
  leaseback $37.8M; operating-lease right-of-use assets up $72.3M in FY2025). Amortization of acquired intangibles $27.3M a year.
  Stock pay rose from $1.7M (FY2021) to $8.1M (FY2025) and $6.3M in the first half of 2026.
- *The "non-recurring" items recur:* strategic review costs (FY2023, FY2024), severance (FY2023 $4.0M, FY2024 $8.0M), CEO
  transition (FY2024), separation costs (FY2025), "One Centuri" implementation and acquisition costs (Q2 2026), each added back
  in the adjusted figures (10-K FY2025 MD&A, Non-GAAP; 10-Q MD&A). The row: "to tell owners year after year, "Don't count this,"
  [...] is misleading" **[L2016-007]**.
- *EBITDA in the filer's own mouth:* EBITDA, Adjusted EBITDA, Adjusted Net Income, Adjusted EPS, Base Revenue and Base Gross
  Profit are presented in the 10-K and featured first in the releases; Q2 2026 Adjusted Net Income $24.4M against GAAP net income
  $6.1M (Ex. 99.1, `0001981599-26-000088`) **[M1998-086]**, **[M2002-026]**, **[L2016-006]**.
- *A receivable that went:* revenue for City of Chicago work completed before 2020 was carried as receivables and contract
  assets through the administrative agency's denial of the claim on 2024-07-18, and reversed ($9.0M) in Q2 2026 after a court
  order of 2026-04-20 (10-Q Note 14 and MD&A) **[M2008-064]**.
- *Interest against earnings:* pre-tax earnings over interest 1.19x in FY2025 and 0.96x in FY2024 **[L2012-002]**.

**Q5, integrity and ability (recorded, not judged; any later run that reaches Q5 must answer them** **[M2013-088]**).
- Earnings guidance on adjusted figures: full-year 2026 guidance for Base Revenue, Base Gross Profit, Revenue, Adjusted EBITDA
  ($285M to $310M) and Adjusted Net Income ($60M to $75M), raised on 2026-08-04 (Ex. 99.1) **[L2019-006]**, **[L2002-041]**.
- The adjusted figure featured in place of GAAP, and the recurring "non-recurring" items above **[L2016-006]**, **[L2016-007]**.
- The Chicago receivable carried for years after the work and through an adverse administrative decision, then reversed.
- Turnover at the top: four chief executives served in 2024 (Daily, retired January 2024; Fehrman, January to July; Caudill,
  interim, July to December; Brown from December 2024) (DEF 14A `0001981599-26-000046`, pay-versus-performance notes); the
  chief financial officer and the chief legal officer were replaced on 2026-08-12, each leaving with severance (8-K
  `0001981599-26-000108`).

**Q6, the money and the owners.**
- Issuance: 16,851,929 shares at the IPO (April 2024, $327.7M net) and 12,046,511 in the November 2025 offering and private
  placement at $21.50 (7,441,860 + 3,488,372 to the Icahn Group + 1,116,279 option; $250.9M net); shares outstanding 71.7M at
  the separation, 88.5M (FY2024), 100.7M (FY2025), 100.96M (2026-06-28) **[L2014-015]**. The November 2025 price of $21.50 sits
  above every figure of the computation above.
- Deals: Riggs Distler $822.2M (2021, debt-financed; $391.1M of goodwill written off); the Linetec minority bought out for
  $39.6M, $39.9M and $92.9M (FY2022 to FY2024); Connect about $58.0M (November 2025); JJ White about $62.0M (July 2026). No
  buybacks; dividends of $31.0M (2021) and $15.0M (2022) were paid to the former parent, none since the IPO.
- Pay: 60% of the annual bonus on Adjusted EBITDA; long-term awards set "generally at the median of the peer group"; one-third
  of 2025 performance units on return on net assets and free cash flow (DEF 14A) **[M2012-095]**.
- Board: an independent chair from 2025-09-15; an Icahn designee under the Director Appointment and Nomination Agreement of
  2025-11-10, with CEO and CFO appointments and material deals reserved to the full board or committees on which he sits (8-K
  `0001981599-25-000069`); a new director from 2026-03-20, Steven E. Nielsen, formerly chief executive of Dycom (8-K
  `0001981599-26-000035`).

**Q9, debt and exposures.**
- Term loan $616.0M maturing 2032-07-09 (no principal due before), revolver to 2030-07-09 ($85.9M drawn at 2026-06-28),
  equipment loans; secured by substantially all assets. Covenants: leverage 4.50x until September 2026, then 4.00x; interest
  cover at least 2.50x, with a cushion of $24.8M at FY2025 (10-K MD&A) **[L2010-020]**, **[M1995-104]**.
- Performance and payment bonds outstanding about $822.8M; self-insured retentions; multiemployer pension plans whose future
  obligations "cannot be determined" (10-K) **[R1997-001]** (the whole-business criterion, "little or no debt", noted, not applied).

**Q12.** Nothing found that bears on it.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (914be484); written question by question; committed after each (Step 0
      9e40af46, Q1 2470e8fe, Q2 8a86c984, the rest in one commit after the close, since Q3 to Q12 were not reached).
- [x] Dispatched: the brief allowed the per-question commits and the dispatching session holds the lock; the fold is the
      dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is declared
      under Contamination at the top and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (the check script
      `scripts/check_cites.py`, output in `check_cites_output.txt`); every filing fact carries its accession; numbers come from
      filings or from the run's scripts.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the Q7 arithmetic is headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury daily par
      yield curve; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations paragraph); the facts for later questions are under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] No point-in-time anchor; rows of every year may be cited.
- [x] Only the arithmetic lines of `tools/run.py` were used; its FY2024 owner-cash line was corrected against the filing.
- [x] `python tools/check_framework.py` PASS before the final commit (run 2026-10-18 after the file was complete); the run's
      own check, `scripts/check_cites.py`: 48 distinct ids, all in the ledger, no E-id, 12 quoted fragments beside ids, 0 problems.

**CONVENTIONS of this run, confessed (each ours):**
1. Owner cash takes out the one-time $125.0M initial sale of receivables (FY2024) and the $37.8M sale-leaseback (FY2025), and
   counts routine equipment-sale proceeds against capital spending. Rationale: the first is a financing of receivables and the
   second a one-time sale of the fleet replaced by leases; the routine proceeds recur every year at a fleet business.
2. For the all-equity basis, cash interest is added back after tax at 25%, the company's own blended statutory rate in its
   non-GAAP note; interest paid is used for FY2023 to FY2025, and interest expense less debt-cost amortization for FY2021 and
   FY2022. Rationale: the framework names the basis and not the rate at which to add interest back.
3. Organic growth for the serial acquirer's organic pair is measured between the halves of the full post-acquisition years
   FY2022 to FY2025, because the filer reports no organic growth and FY2021 holds Riggs Distler for five months. Rationale: the
   window's own halves would count an acquisition's part-year as growth; the window-halves result is shown beside.
4. The competitor metrics (operating margin, operating cash less stock pay less capital spending as a share of revenue, pre-tax
   operating income on tangible assets) and the reading of first-filed XBRL values. Rationale: the template asks for "the same
   metric" and names none.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) Q4 asks for "eight to ten years" of balance sheets, but a company carved out of a parent in 2024 files full
balance sheets for only four year-ends; the former parent's segment table gives total assets and nothing else. The framework
does not say whether a carve-out's history may be read from the parent's segment notes or how short a record still counts;
this run read both and said what each holds. (2) Q7 (d) counts the increase in working capital as capital spending, and the
inventory-secured trade finance convention treats one kind of secured working-capital finance, but nothing covers a sale of
receivables to a securitization facility: it releases working capital in the cash-flow statement while it is, in substance,
a financing. This run took the initial sale out of owner cash and showed the sold balance beside net debt; the opposite reading
(count it in net debt as well) lowers every figure further. (3) Q7 (e)'s maintenance guess assumes capital spending is the only
way the fleet is kept up; here the fleet is being moved to operating leases, so capital spending falls below depreciation while
the lease payments move into operating cash. The framework does not say how to read the maintenance guess during such a shift.
(4) The serial-acquirer rule asks for "organic growth as the filer reports it"; this filer reports none, and the rule is
silent on what to do then (CONVENTION 3 above). (5) The all-equity basis adds owner cash "before interest", but the framework
gives no rate at which to add interest back after tax for a company paying little tax under NOLs, and the Whose-tax convention's
trigger ("carryforwards ... that run out inside ten years") does not say what to do when only "some" of them do (CONVENTION 2,
and the tax note under the COMPUTATION).
