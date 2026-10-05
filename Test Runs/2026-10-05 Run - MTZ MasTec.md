# Company Run — MasTec, Inc. (NYSE: MTZ) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**
Working folder: `Test Runs/_research 2026-10-05 MTZ/` (filing texts, fetch script, competitor extracts).

**POSITION NOTE, declared before any verdict:** NOT CHECKED, by instruction. This run is blind: `PORTFOLIO.md`, every
holding review, the session-state files, the run queue, the prepped reading list, any other run file on this company and
every other 2026-10-05 run file were left unopened, and no attempt was made to learn whether anyone holds or wants MTZ.
**Contamination declared:** (1) the git status printed at session start lists an untracked file
`Test Runs/2026-10-05 Run - MYRG MYR Group.md` and the recent commit subjects name same-day v5 runs on PWR, EME, IESC,
FIX and UTI with their boxes (PWR TOO HARD (WORK) at Q2; EME, IESC, FIX OUT at Q2). I read those subject lines because
the session printed them; I opened none of the files. Those boxes are for other companies; this run's Q2 rests only on
MasTec's own filings and the competitors' filings fetched fresh below. (2) `tools/run.py` prints v4 material; only its
arithmetic lines were used (Part VII). (3) A file `Test Runs/2026-09-25 Run - MHH Mastech Digital.md` exists; it is a
different company (Mastech Digital), seen only as a file name in a directory listing, not opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $222.21 (2026-10-05 intraday, 16:33 UTC; Yahoo chart via `tools/sources.py`; **aggregator, live quote
  only, flagged** per operator rule 5). The same series shows $433.28 on 2026-05-06, $396.25 on 2026-06-26, $336.79 on
  2026-07-27, $261.22 on 2026-08-03 and $210.23 on 2026-09-29: the price roughly halved from its May high in five months.
  The reason for the fall was not found in the filings read.
- **Shares by class** from the latest filing's cover: one class, common stock $0.10 par, **80,304,948** shares as of
  2026-07-27 (10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession `0000015615-26-000093`;
  `python Screens/cover_shares.py MTZ`). The 10-K cover shows 78,894,830 as of 2026-02-23 (accession
  `0000015615-26-000020`); the difference is mostly the ~1.2 million shares issued for the Superior Group (8-K of
  2026-07-07, accession `0001193125-26-297552`).
- **Market cap:** 80.305M × $222.21 = **$17,845M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 2026-10-02
  (issuing authority; `tools/sources.py` via `tools/run.py`).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-26, accession `0000015615-26-000020`); 10-Q for
  Q2 2026 (filed 2026-07-30, accession `0000015615-26-000093`); proxy DEF 14A (filed 2026-04-09, accession
  `0001140361-26-014022`); 8-Ks of 2026-07-07 (`0001193125-26-297552`, Superior Group agreement, $700M term loan, revolver
  upsized), 2026-07-20 (`0001193125-26-309077`, $700M term loan drawn and $600M revolver drawn for Superior), 2026-07-30
  (`0000015615-26-000095`, Q2 results, Exhibit 99.1), 2026-08-10 (`0001193125-26-342507`, $650M 5.850% notes due 2036),
  2026-08-17 (`0001193125-26-354111`, notes closed). Older 10-Ks for the 2010 to 2024 record and the competitors' filings
  are listed where used.
- **One figure cross-checked against the filed statement:** operating cash flow FY2025, $545,714K in the filed
  cash-flow statement (10-K FY2025, Item 8), equals run.py's 546; capex $259,985K and stock pay $34,002K also agree.
- `python tools/run.py MTZ` arithmetic lines (USD millions, relabelled; see the note under the table):

  | FY | OCF | SBC | D&A | capex (cash) | OCF − SBC − capex | OCF − SBC − D&A |
  |---|---|---|---|---|---|---|
  | 2023 | 687 | 33 | 603 | 193 | 461 | 51 |
  | 2024 | 1,122 | 33 | 507 | 149 | 940 | 582 |
  | 2025 | 546 | 34 | 427 | 260 | 252 | 85 |

  *(run.py's own column labels are swapped against what it computes: its "OE lo" column is OCF − SBC − D&A and its "OE
  hi" is OCF − SBC − cash capex, because cash capex here is far BELOW depreciation. The reason, finance leases and
  equipment bought on credit, is read at Q3 and Q4. The table above is relabelled from the arithmetic.)* Each figure is
  checked against the filing below; run.py's stated defects (stale shares, stock pay, securities in OCF) are tested there.

## THE FOUNDATIONS (not a gate)
A share is a business, and the market "just tells us prices" **[M2006-077]**: the halving of MTZ's quote since May 2026
(Step 0) is information about the price only, and this run neither reads it as a signal against the business nor as a
bargain. The margin of safety is an attitude here: if the case needs pencil and paper "it's too close to think about"
**[M1996-084]**. No macro forecast enters **[M2000-094]**; MasTec's 10-K is built around forecasts of AI data-center
power, IIJA and IRA spending and LNG exports, and what counts instead is "the average profitability of the business over
time and how strong its competitive mode is" (the transcript's word) **[M2015-016]**. Who is paid to tell you: the 10-K's
"Industry Trends" pages quote IBISWorld, Deloitte and S&P forecasts that the filer selected; they are read as the
seller's case, not as evidence. The analyst's habit applied: look for "what's wrong in things" **[M2025-013]**, and aim the
reading at rejecting the hypothesis **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**:
1. (against my early lean toward OUT) The pipeline segment earned EBITDA margins of 20.3% in 2019 and 21.9% in 2021
   (10-K FY2019, accession `0000015615-20-000005`; 10-K FY2022, `0000015615-23-000009`): in large-diameter mainline work
   MasTec has at times earned far more than an ordinary contractor. Carried into Q2.
2. (against) The FY2014 10-K was filed on 2015-07-31, five months late, after an Audit Committee investigation of
   cost-to-complete estimates; three 2014 quarters were restated and a material weakness was reported (accession
   `0000015615-15-000053`). Carried to the not-reached record (Q4, Q5).
3. (against) Contract assets (unbilled revenue) rose from $1,556M (2024) to $2,002M (2025) to $2,484M (2026-06-30),
   faster than revenue; and $172M of receivables sold under non-recourse arrangements were outstanding at 2025 year end
   against $84M a year earlier, cash that flatters operating cash flow (10-K FY2025, Note 5; 10-Q Q2 2026).
4. (for) Quanta's own 10-K says customers "often consider other factors" than price and that "competition may lessen as
   industry resources, such as labor supplies, approach capacity" (PWR 10-K FY2025, `0001050915-26-000006`). Carried
   into Q2 as the strongest case for a castle.
5. (against) The Superior Group was bought in July 2026 for about $1.6 billion: about $1.2 billion in cash, funded mostly
   by $1.3 billion of new borrowing, and 1.22 million shares issued at $336.61 a share (10-Q Q2 2026, Note 3); the price is now $222.21.
6. (against) The Chairman and the CEO, the founding family, have pledged shares and hold prepaid variable forward sale
   contracts on part of their stock (proxy 2026, accession `0001140361-26-014022`, ownership footnotes).

## THE STANDING RULE
Owning MTZ need not put the buyer at risk of ruin if it is bought with the buyer's own money, unlevered and sized so that a
halving (which the quotation has just shown it can do in five months) costs nothing the buyer needs: "never going to risk
what we have and need for what we don't have and don't need" **[M2012-081]**; "borrowed money has no place in the
investor's tool kit" **[L2014-005]**. No margin, no options. The rule is satisfied by the buyer's conduct; the target's own
debt is Q9's question (not reached).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, not knowledge of the product; what matters is "the economic dynamics of the
  industry. Is there [...] are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **What the business is, from the filing.** A labor-based contractor: "This structure is generally focused on broad
  end-user markets for the Company's labor-based construction services" (10-K FY2025, Note 14). It builds and maintains
  wireless and fiber networks, wind, solar and gas generation, transmission and distribution lines, and oil, gas and
  water pipelines, for about 1,800 customers; the top ten gave 34% of 2025 revenue and AT&T alone about 10% (Note 14).
  44% of 2025 revenue came under master service agreements (MSAs), which "do not obligate our customers to undertake any
  infrastructure projects" and "typically provide for termination on short or no advance notice"; the rest is project
  work, much of it fixed price under cost-to-cost accounting (Item 1, "Customers"). 36,000 employees, about 9,000 in
  unions (Item 1).
- **The key variables** **[M1998-044]**: (a) the capital spending of its customers in four unrelated end markets
  (telecom, renewables, utilities, oil and gas midstream); (b) the margin it can win on bid work; (c) its own execution on
  fixed-price jobs (cost-to-complete estimates). Of these, (a) is NOT foreseeable ten years out and the filer itself
  calls it subject to "changes in governmental policies that reduce tax or funding incentives" (Item 1; the One Big
  Beautiful Bill Act's acceleration of the phase-out of clean-energy credits is named there). (b) is foreseeable in kind
  from sixteen years of filings: a single-digit margin that falls hard when volume falls (Q2). (c) is knowable only after
  the fact, project by project.
- **Do the past statements tell me the future ones?** **[M2008-033]** For the margin and the return on capital, yes in
  kind: 2010 to 2025 show the same economics in every segment mix (Q2's table). For the volume and the mix, no: pipeline
  revenue fell 52% in 2022 and rose 70% in 2023 (10-K FY2022, FY2023 MD&A); clean energy went from 3% of revenue in 2017
  to 19% in 2025 (Item 1).
- **Routing.** This is not a fast-changing technology business; the routing to Q1 TOO HARD is for a business "whose
  ten-year economics cannot be foreseen because its industry changes fast" (Q1, The routing, fixed). The ten-year
  question that matters here, whether this contractor can earn a protected return, is about the castle, and it can be
  read from the filings and from four competitors' filings. The volume forecast is important but unknowable
  **[M2006-076]**, and it is NOT needed to answer Q2 if Q2 closes on the economics alone; if Q2 had needed it, this
  would have been TOO HARD here. I have no doubt that the business is inside the circle as an economic proposition (a
  bid contractor), only about its volumes **[M2002-092]**; my model of how far off I could be **[M2011-084]** is narrow on
  margins and wide on revenue.
- **VERDICT: IN**, narrowly, on the economics (a labor contractor bidding for work), with the volume forecast set aside
  as unknowable and not needed for the next STOP **[M2012-065]**, **[M2011-014]**, **[M2006-076]**. The reading that
  would have closed it here instead is recorded in "What in the framework was wrong or unclear".

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what's going to keep it standing" **[M1995-038]**, asked from
the attacker's side **[M2011-015]**.

**The castle tests, each with its filing fact.**
- **Would the customer still choose it over the low bid?** **[M2017-009]**, **[M1997-102]**. The filer answers in its
  own 10-K: "Our industry is highly competitive and highly fragmented [...] While we believe that our customers consider a
  number of factors when selecting a service provider, they award most of their work through a bid process, and price is
  often a principal factor in determining which service provider is selected." (10-K FY2025, Item 1, "Competition",
  accession `0000015615-26-000020`). Even the recurring work is bid: MSAs "are frequently awarded on a competitive bidding
  basis" and "typically provide for termination on short or no advance notice"; 47% of the year-end backlog is MSA work
  under which "our customers are not contractually committed to purchase a minimum amount of services" (Item 1,
  "Customers" and "Backlog"). This is the failing answer the rows give: the customer who does not care from whom he buys
  **[L2004-003]**.
- **The attacker with money** **[M2011-015]**, **[M2012-106]**. The filer names the barriers as "adequate financial
  resources, technical expertise, high safety ratings, established customer relationships and a proven track record",
  and adds "Some of our customers employ their own personnel to perform infrastructure services of the type we provide"
  (Item 1). Each of these can be bought: MasTec itself entered clean energy at scale by purchase (IEA, 2022, total
  consideration $748.5M, of which $530.6M goodwill: 10-K FY2022 Note 3, accession `0000015615-23-000009`) and
  data-center electrical work by purchase (Superior, 2026, about $1.6B: 10-Q Q2 2026 Note 3). What a well-funded entrant
  cannot quickly buy is a trained, partly unionised craft workforce; that is the case for the castle, tested below.
  Against it, Dycom, a competitor, writes in its own 10-K: "Relatively few barriers to entry exist in the markets in
  which we operate, which means that any organization could become a competitor if it has adequate financial resources
  and access to technical expertise" (DY 10-K for the year ended January 2026, accession `0000067215-26-000008`).
- **Pricing power and the agony before a rise** **[M2005-020]**. No instance in the filings read of MasTec raising prices
  on existing work; margins move with volume and execution. The 2023 MD&A attributes the cost-ratio rise to "reduced
  project efficiencies", "certain overhead costs incurred to maintain operating capacity" and "the effects of inflation on
  labor, material and other costs" (10-K FY2023, accession `0000015615-24-000021`): inflation was absorbed, not passed
  on, in the year it came.
- **The low-cost position** **[L2004-007]**, **[L2000-017]**, **[M1997-010]**. Nothing in the filings claims MasTec is
  the low-cost producer, and the competitor row says it is not, at least in power delivery and in the slack years. In
  2025 MasTec's Power Delivery segment earned EBITDA of 8.1% of revenue, BEFORE its 3.4% of depreciation and
  amortization (10-K FY2025, Note 14: EBITDA $338.8M, D&A $142.3M, revenue $4,176.1M), while Quanta's Electric segment
  earned operating income of 10.3% of revenue AFTER depreciation (PWR 10-K FY2025, MD&A segment table, accession
  `0001050915-26-000006`; Quanta's segment figures exclude intangible amortization, so the comparison is approximate,
  but the gap is wider than that difference). In the slack years the gap is plain (table below): MasTec's operating
  margin fell to 1.6% (2022) and 1.3% (2023) while Quanta's held at 5.1% and 5.4%. "the low-cost producer can put you
  out of business" **[M1997-010]**; "the guy with the lower cost comes in and kills you" **[M2001-013]**.
- **Brand and share of mind.** The MasTec® service mark is used to market "integrated" offerings (Item 1); no filing fact
  shows a customer asking for MasTec by name or paying more for it. The buyer is a utility, carrier or developer running
  a bid.
- **Ask the competitors** **[M1999-130]**, **[M2017-091]**. No interview is on the public record; the nearest is what each
  competitor tells its own owners about the same market. MYR Group: "most of their work is awarded through a bid process
  where price is always a principal factor" (MYRG 10-K FY2025, accession `0000700923-26-000007`). Quanta: "price is often
  an important factor in the award of such agreements. Accordingly, we could be underbid by our competitors" (PWR 10-K
  FY2025). Primoris: "some customer contracts are awarded through bidding processes based on price and the acceptance of
  certain risks" (PRIM 10-K FY2025, accession `0001104659-26-018677`). Dycom: "Relatively few barriers to entry" (above).
  Five companies, one answer.
- **Widening or narrowing** **[M1999-108]**, **[M2000-075]**. Operating return on tangible assets (pre-tax income plus
  net interest, over year-end total assets less goodwill and intangibles) ran 13% to 19% in 2010 to 2014, 13% to 17% in
  2016 to 2020, and 2.3% to 9.8% in 2021 to 2025; the operating margin went from 8.0% (2010) to 4.8% (2025) while
  revenue rose six-fold, much of the rise bought (cash paid for acquisitions, net, $3.2 billion over 2010 to 2025, XBRL
  PaymentsToAcquireBusinessesNetOfCashAcquired, first-filed 10-K values, plus shares). The trend is narrowing, not
  widening.
- **What could destroy or reduce it** **[M2000-014]**. Customers' capital budgets and federal policy (Q1); a fixed-price
  project gone wrong (the 2014 restatement concerned cost-to-complete estimates on "two large and complex Electrical
  Transmission segment projects", 10-K FY2014 Note 2, accession `0000015615-15-000053`); customers doing the work
  themselves (Item 1).

**The strongest case for the castle, stated as its holder would state it** **[M2016-055]**.
(1) Scarce skilled labor: Quanta writes that "competition may lessen as industry resources, such as labor supplies,
approach capacity", and that customers "often consider other factors [...] which we expect to benefit larger service
providers such as us" (PWR 10-K FY2025). (2) MasTec's pipeline segment earned EBITDA margins of 20.3% (2019) and 21.9%
(2021): few contractors can build large-diameter mainline pipe, and when it is in demand they are paid for it. (3) A
record 18-month backlog of $21.4 billion at 2026-06-30 (8-K of 2026-07-30, Exhibit 99.1, accession
`0000015615-26-000095`) and an adjusted EBITDA margin guided to 9.8% for Q3 2026.
**Why it does not hold as a castle.** (1) The labor case is stated by Quanta as a condition of the cycle ("as industry
resources [...] approach capacity"), not as a lasting barrier; a margin that exists only when capacity is tight leaves the
rival setting the price the rest of the time **[M2012-109]**, **[M2023-079]**. (2) The pipeline windfall proves it: the
same segment's revenue fell 52% in 2022, "primarily due to a decrease in large diameter project activity", and its
EBITDA margin fell 850 basis points with "reduced productivity" (10-K FY2022 MD&A); in 2015 it was 10.5% (10-K FY2016,
accession `0000015615-17-000007`). Margins set by how many pipelines the customers decide to build belong to the
customers' cycle, not to MasTec. (3) The backlog is 47% MSA work with no minimum commitment, and adjusted EBITDA leaves
out the depreciation and the amortization of the purchases that built the backlog. And the position has been rebuilt by
purchase every few years (fourteen acquisitions in 2021 alone: 10-K FY2022 Note 3): "A moat that must be continuously
rebuilt will eventually be no moat at all" **[L2007-005]**.

**The competitor row.** Operating margin = operating income over revenue, or pre-tax income plus net interest where the
filer reports no operating-income line (MTZ, DY). Return on tangible assets (RoTA) = the same earnings over year-end
total assets less goodwill and intangibles. Source: each company's XBRL company facts, first-filed 10-K values,
transcription only; cross-checked against the filed statements for PWR FY2025 (revenue $28,479,697K, operating income
$1,611,509K, accession `0001050915-26-000006`) and MYRG FY2025 (revenue $3,657,889K, income from operations $166,872K,
accession `0000700923-26-000007`). Dycom's fiscal year ends in January and is labelled by the calendar year it mostly
covers. Script and output: `Test Runs/_research 2026-10-05 MTZ/peers.py`.

| Company (CIK) | Op. margin, mean 2010-25 | worst year | 2022 | 2023 | 2025 | RoTA, mean 2010-25 | RoTA worst | RoTA, mean 2021-25 |
|---|---|---|---|---|---|---|---|---|
| **MasTec (15615)** | 5.3% | -0.5% (2015) | 1.6% | 1.3% | 4.8% | 11.6% | -1.1% (2015) | 6.3% |
| Quanta (1050915) | 5.4% | 3.1% (2015) | 5.1% | 5.4% | 5.7% | 10.3% | 6.9% | 10.5% |
| Primoris (1361538) | 5.0% | 2.9% (2016) | 4.4% | 4.4% | 5.4% | 10.3% | 5.7% | 9.8% |
| MYR Group (700923) | 4.0% | 1.6% (2024) | 3.8% | 3.5% | 4.6% | 9.2% | 3.9% | 9.2% |
| Dycom (67215, FY to Jan, 2011-25) | 6.1% | 2.7% (2021) | 5.8% | 8.3% | 7.8% | 12.3% | 4.9% | 12.0% |

What the row says: the whole trade earns about five cents of operating profit on a dollar of revenue and about ten
percent pre-tax on its tangible assets through the cycle; nobody in it earns a protected high return, which is what a
commodity field looks like **[M2000-072]**, **[M2004-053]**. MasTec's long average is the trade's average; its worst
years are worse than the trade's, and in 2022 and 2023 it was the lowest of the five. Fewness of large rivals does not
change that **[M2013-052]**.

**VERDICT: OUT.** The castle is shown open on the evidence, in the filer's own words and in sixteen years of its figures:
customers "award most of their work through a bid process, and price is often a principal factor" (10-K FY2025); the four
competitors say the same of the same market; the return on tangible assets has narrowed from the high teens to single
digits as the business was enlarged by purchase; and MasTec is not shown to be the low-cost operator, the route the rows
name through a commodity field **[L2004-007]**, **[M1997-010]**. The customer indifferent to whom he buys from
**[L2004-003]**, **[M2017-009]** and the rival who sets the price **[M2012-109]** are the failing answers; "If the answer
had been yes, we wouldn't have done it" **[M2011-015]**. This is OUT, not TOO HARD: the castle's future is not
unjudgeable, it is judged open **[M2006-013]**. Price does not reopen it (Q2, Why it is a STOP).

---
## Q3 to Q10, Q12: NOT REACHED
The file closed OUT at Q2. Nothing below is a clearance. The facts gathered for these questions are recorded after the
box, under COMPUTATION — NOT A CLEARANCE, because the owner asked for the value range, the fair-price band and the cheap
price, and the run instructions ask for the balance-sheet reading.

---
## THE BOX
**OUT**, decided at **Q2**: the castle is shown open (work won by bid with price a principal factor, in the filer's and
four competitors' own words; a narrowing return on tangible assets; not the low-cost operator). Not a TOO HARD; no
research pass is owed. For the record only (COMPUTATION, below, labelled because the file closed before Q7): value range
$66 to $142 a share; fair-price band $66 to $83; cheap price about $33; against a price of $222.21.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section was produced after the file closed OUT at Q2. It carries no entry language and clears
nothing (operator rule 3). It is here because the owner asked for the value range, the fair-price band and the cheap
price, and the run instructions ask for the balance-sheet reading and the filing facts behind the questions not reached.
No verdict is given on Q3 to Q10; the facts are recorded so that a later reader need not fetch them again.*

### The balance sheets first, ten years of them (the Q4 reading, not judged) **[M2025-032]**
USD millions, year end; 2016 to 2025 from `tools/run.py` (first-filed XBRL, accessions listed in
`Test Runs/_research 2026-10-05 MTZ/run_py.txt`), 2010 to 2015 and the debt line from XBRL company facts
(`table.py`), the FY2025 and 2026-06-30 columns read from the filed statements (accessions `0000015615-26-000020`,
`0000015615-26-000093`).

| Year end | Total assets | Equity (MasTec) | Goodwill + intangibles | Tangible equity | Debt incl. finance leases | Cash | AR + contract assets, % of revenue |
|---|---|---|---|---|---|---|---|
| 2010 | 1,656 | 653 | 691 | -38 | 394 | n/a | 24.0% |
| 2013 | 2,920 | 1,016 | 1,065 | -49 | 817 | n/a | 35.1% |
| 2016 | 3,183 | 1,097 | 1,176 | -79 | 1,026 | 39 | n/a (pre-ASC 606 split) |
| 2018 | 4,440 | 1,390 | 1,269 | 121 | 1,407 | 27 | see note |
| 2019 | 4,997 | 1,787 | 1,433 | 354 | 1,432 | 71 | 26.1% |
| 2020 | 5,228 | 2,002 | 1,427 | 575 | 1,303 | 423 | 27.8% |
| 2021 | 7,121 | 2,540 | 2,191 | 349 | 2,014 | 361 | 28.3% |
| 2022 | 9,293 | 2,737 | 2,991 | -254 | 3,224 | 371 | 32.0% |
| 2023 | 9,374 | 2,706 | 2,910 | -204 | 3,065 | 530 | 26.1% |
| 2024 | 8,975 | 2,912 | 2,930 | -18 | 2,224 | 400 | 23.9% |
| 2025 | 9,924 | 3,259 | 2,905 | 354 | 2,331 | 396 | 24.8% |
| 2026-06-30 | 10,925 | 3,477 | 3,090 | 387 | 2,753 (before the July borrowing) | 316 | about 25% of the H1 run rate |

What the figures say. (1) **Tangible equity is near zero or negative in most of the years shown**: the book equity is
largely the price of businesses bought. Retained earnings rose from $510M (2016) to $2,708M (2025), and goodwill plus
intangibles rose by $1,729M over the same years. (2) **Debt grew with the purchases**: $394M (2010), $3,224M (2022, after
IEA), $2,331M (2025), $2,753M at 2026-06-30, and then $1,300M more drawn in July 2026 for Superior ($700M term loan and
$600M revolver, 8-K of 2026-07-20, accession `0001193125-26-309077`), part refinanced by $650M of 5.850% notes due 2036
(8-K of 2026-08-10, accession `0001193125-26-342507`). Pro forma debt is about $4.0 billion before the July cash use is
netted, against equity of about $3.9 billion. (3) **Receivables and unbilled work run at about a quarter of a year's
revenue**; the 2018 figure (AR $1,924M plus costs in excess of billings $1,253M on $6,909M revenue) is not comparable
because the pre-2019 receivable line included unbilled amounts that ASC 606 later moved to contract assets. Contract
assets alone rose from $1,556M (2024) to $2,002M (2025) to $2,484M (2026-06-30), faster than revenue: a "look twice"
item in the rows' sense (Q4 tells), recorded, not judged. (4) **Receivables sold**: $172M of sold receivables were
outstanding at 2025 year end against $84M a year earlier (Note 5), and the discount charges ($23.8M in 2025) sit in
interest expense; operating cash flow in 2024 and 2025 is that much flattered. (5) **What the figures can't say**: the
profit on uncompleted fixed-price work rests on cost-to-complete estimates, the subject of the 2014 restatement and the
material weakness reported then (10-K FY2014, Note 2 and Item 9A, accession `0000015615-15-000053`; the investigation
"arose as a result of concerns communicated to senior management through the Company's internal reporting system").

### Owner cash after every real cost (operator rule 5; not a net-income proxy)
Owner cash = operating cash flow − stock pay − cash capital expenditure − finance-lease principal payments (the
equipment MasTec buys on lease credit: $229M of additions in 2025, cash-flow statement, supplemental non-cash disclosure) + proceeds from equipment sold −
distributions to non-controlling interests. Depreciation variant = operating cash flow − stock pay − depreciation −
distributions to non-controlling interests. USD millions; FY2023 to FY2025 cross-checked to the filed cash-flow statement
(10-K FY2025: operating cash flow $545,714K, capital expenditures $259,985K, finance-lease payments $161,024K, stock
pay $34,002K, all as XBRL); earlier years XBRL first-filed values.

| FY | Revenue | OCF | Stock pay | Capex | Lease principal | Equipment sold | NCI dist. | **Owner cash** | Depreciation | Dep. variant |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 5,135 | 206 | 15 | 117 | 58 | 11 | 0 | 27 | | |
| 2017 | 6,607 | 156 | 16 | 123 | 68 | 20 | 1 | -32 | | |
| 2018 | 6,909 | 530 | 14 | 180 | 72 | 39 | 1 | 303 | | |
| 2019 | 7,183 | 550 | 16 | 126 | 88 | 35 | 1 | 353 | | |
| 2020 | 6,321 | 937 | 22 | 214 | 127 | 37 | 1 | 611 | 259 | |
| 2021 | 7,952 | 793 | 25 | 170 | 159 | 65 | 0 | 505 | 346 | 422 |
| 2022 | 9,778 | 352 | 27 | 263 | 181 | 81 | 1 | -39 | 371 | -47 |
| 2023 | 11,996 | 687 | 33 | 193 | 168 | 84 | 3 | 375 | 434 | 217 |
| 2024 | 12,303 | 1,122 | 33 | 149 | 154 | 66 | 33 | 819 | 367 | 689 |
| 2025 | 14,299 | 546 | 34 | 260 | 161 | 56 | 25 | 122 | 296 | 191 |
| **mean 2021-25** | | | | | | | | **356** | | **294** |
| mean 2016-20 | | | | | | | | 252 | | |

`tools/run.py`'s stated defects checked: the share count is the cover count (no split since 2010; 80,304,948 at
2026-07-27); stock pay is not zero ($34.0M in 2025); operating cash flow holds no securities purchases, but does hold the
receivable sales above. Over 2010 to 2025 owner cash summed to about $3.6 billion, cash paid for acquisitions to about $3.2
billion, and buybacks to about $0.85 billion; debt rose by about $1.9 billion. The cash the business made went to buying
other businesses. Spending on equipment (capex plus lease principal less sales, mean $301M in 2021-25) ran below
depreciation (mean $363M), in part because equipment also arrived inside acquisitions (IEA brought $213M of property and
equipment); the depreciation variant is therefore taken as the conservative end. Depreciation is "almost always true
costs" **[L2015-004]**.

### The value range, the fair-price band, the cheap price (COMPUTATION; the file closed before Q7)
Built by Q7's CONVENTION (five-year average owner cash; carried at the growth shown, measured on aggregate owner cash;
ten years, then zero nominal growth; discounted at the 30-year Treasury, 5.63%; ends = no-growth and shown-growth)
**[L2000-025]**, **[M2009-005]**. Growth shown: mean owner cash 2016-20 $252M to 2021-25 $356M = 7.2% a year. That growth
was bought (cash acquisitions of $1.9 billion in 2021 and 2022 alone, plus 2.7 million shares for IEA); Q3, had it been
reached, would very likely have capped it, so the top end is generous. **The Superior Group (July 2026) is counted at what
was paid for it**: its earnings are not in the five years and its price ($1.2B borrowed plus 1.22M shares) is not in the
share count used, i.e. treated as neither adding nor subtracting value; its own earnings were not found in the filings
read. Shares: 78.90M (99,319,916 issued less 20,422,329 treasury at 2025-12-31, 10-K FY2025 balance sheet).

| Case | Cash input | Equity value | Per share |
|---|---|---|---|
| Low: no growth, depreciation variant | $294M | $5,222M | **$66** |
| No growth, all-capex owner cash | $356M | $6,323M | $80 |
| Shown growth 7.2% for ten years, depreciation variant | $294M | $9,244M | $117 |
| High: shown growth 7.2% for ten years, all-capex owner cash | $356M | $11,193M | **$142** |

- **Value range: $66 to $142 a share** (top to bottom 2.1 to 1, inside Q7's three-to-one CONVENTION) against **$222.21**.
  The price is above the top of the range. The owner cash yield at the price is 2.0% ($356M on a $17,845M market cap)
  against a 5.63% Treasury; the price needs about 13% a year growth in owner cash for ten years, then none, to be worth
  itself at the Treasury rate.
- **Fair-price band (prices inside the range at which the expected pre-tax return is at least about ten percent,
  the floor CONVENTION **[M2003-149]**, **[L2002-020]**, **[M1994-004]**)**: pre-tax owner cash = owner cash plus the mean
  2021-25 income-tax provision ($43.6M). On the shown-growth case ($399M pre-tax) the price that returns 10% is $83, so
  the band is **$66 to $83**. On the no-growth case ($337M pre-tax, depreciation variant) the 10% price is $43, below the
  bottom of the range, so no price inside the range clears the floor on that case. Expected pre-tax return at $222.21:
  about 4.1% (shown-growth case) and about 1.9% (no-growth case).
- **Cheap price (below which the case would need no pencil): about $33**, half the bottom of the range. CONVENTION,
  ours: the rows ask for "a big discount" from present value **[M1997-126]** and illustrate a screamer with a price near a
  third of value **[M2008-068]**; one half of the bottom is our line, confessed. At $33 the no-growth, depreciation-variant
  case returns about 11% after tax. Even there the box would stay OUT: Q2's STOP is not reopened by price.

### Facts read for the questions not reached (recorded, not judged)
- **Q3 (capital).** Return on tangible assets 2.3% to 9.8% in 2021-25 (Q2 table). Equipment spend below depreciation
  (above). Acquisitions 2010-25: about $3.2B cash, plus shares for IEA (2.7M, $173.7M), HMG (about 2.0M in 2021) and
  Superior (1.22M, $410.5M).
- **Q4 (the numbers).** Management features adjusted EBITDA: the proxy calls 2025 "Adjusted EBITDA of $1.2 billion"
  against GAAP pre-tax income of $515M, and the 2026 guidance leads with adjusted diluted EPS of $9.30 against GAAP $6.20
  (8-K 2026-07-30). The rows on that habit: **[M1998-086]**, **[L2000-036]**, **[L2016-006]**. Segment profit is reported
  as EBITDA by the CEO as chief operating decision maker (Note 14). The 2014 restatement and material weakness (above).
  Receivables sold (above).
- **Q5 (the people).** Jorge Mas, Chairman since 1998, employee since 1979; José R. Mas, CEO since 2007 (proxy
  2026). Officers and directors as a group own 21.4%; both brothers have pledged shares and hold prepaid variable forward
  sale contracts on part of their holdings, amended in August 2025 (proxy ownership footnotes). Related parties (10-K
  FY2025 Note 16): MasTec built for the Miami professional soccer franchise the Mas brothers majority-own ($77.6M of
  revenue in 2025, $37.5M receivable at year end); leases an aircraft from an entity owned by Jorge Mas ($5.6M in 2025);
  buys from CCI, chaired by their brother Juan Carlos Mas ($6.4M); subcontracts to an entity partly owned by the brothers
  ($3.5M); and keeps split-dollar life insurance for the brothers' trusts with maximum face amounts of $200M and $75M.
- **Q6 (money and owners).** CEO total pay $11.5M (2025), $10.8M (2024), $9.6M (2023, a year with a GAAP net loss
  attributable of $49.9M); the NEO bonus pool is keyed to adjusted EBITDA (threshold $800M, cap 5% of adjusted EBITDA) and
  the committee "may also consider other factors such as successful acquisition activity" (proxy 2026). Buybacks: $77M
  in 2025 (702,533 shares, about $110 a share; the programs are dollar authorizations with no stated price, used when "management believes that the market price of the Company's stock is undervalued", 10-K FY2025 Item 5), $81M (2022), $120M (2020), $314M (2018).
  Stock issued for IEA in October 2022 at about $64 a share and for Superior in July 2026 at $336.61.
- **Q9 (ruin).** Pro forma debt about $4.0B after Superior; the credit agreements carry a 3.50 leverage covenant (4.00
  for four quarters after a large acquisition) and cross-default to the surety indemnity agreement (8-K 2026-07-07);
  performance and payment bonds outstanding $10.9B at 2025 year end, with $4.6B of cost to complete on bonded projects
  (Note 15). Pre-tax income covered net interest about 4.0 times in 2025 and did not cover it in 2023.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Committed after each*: NOT done; the
      run instructions forbid commits, so the write-early discipline was kept by writing each section to disk as it
      closed, without commits.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its accession
      or names its filing; peer figures name their source and two are cross-checked to the filed statements.
- [x] The order was kept; Q2 failed and closed the run; nothing after it is a clearance; the computation is headed as
      operator rule 3 requires.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the US Treasury; the price is an
      aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (six items, in the Foundations).
- [x] No point-in-time anchor: this is a run as of today; no row was excluded or used for date reasons.
- [x] Only the arithmetic lines of `tools/run.py` were used; its column labels were found swapped and are corrected in Step 0.
- [x] `python tools/check_framework.py` run before reporting (result recorded below). No commit made (instruction).
- [x] Blind rule kept; contamination declared in the position note (commit subjects naming other same-day boxes).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 for a business whose economics are foreseeable in kind but whose volumes are not.** MasTec's margin and return
on capital can be read from sixteen years of filings; its revenue depends on four sets of customers' capital budgets and on
federal policy, which nobody in the industry would write down ten years out **[M2000-105]**. Q1's definition joins
"earning power and competitive position" **[M2012-065]**, and earning power is volume times margin. The routing sentence
sends only fast-changing industries to Q1 TOO HARD. I read Q1 as passed on the economics and let Q2 decide, because Q2
could close on the economics alone; a second analyst could defensibly close this at Q1 TOO HARD (NATURE) on the volume
question. Both routes end the file; they differ in the box, and the framework does not say which governs a cyclical
contractor. A sentence is wanted: whether "earning power" at Q1 means the level or only the kind. (2) **The competitor row
has no stated metric.** The template asks for "the same metric from the competitors' own filings"; I used operating margin
and pre-tax return on tangible assets because Q3 names return on tangible assets **[M2011-060]**, but filers differ (MTZ
and DY have no operating-income line), so the row mixes operating income with pre-tax plus interest. (3) **"Owner cash
after every real cost" and finance leases.** MasTec buys much of its equipment on finance leases ($229M of additions in
2025), so cash capital expenditure alone understates the capital spent; the template and Q7's CONVENTION say "deducts all
capital spending" without saying whether lease-financed equipment counts as spent when acquired or when paid. I deducted
the principal payments, and showed the depreciation variant as the lower end. (4) **The fair-price band when the floor
price sits below the range.** The owner's reporting definition (prices inside the range at which the return clears ten
percent) has no answer on the no-growth case, because the ten-percent price ($43) is below the bottom of the range ($66);
I reported the band from the shown-growth case and said so. (5) **The pre-tax floor against after-tax owner cash.** The
floor is stated pre-tax **[L2002-020]** while owner cash is after tax; I grossed up by the book tax provision, not cash
taxes (cash taxes were far lower in 2022-23 because of deferred taxes), a choice the CONVENTION does not make.

## CHECKS RUN
- `python tools/check_framework.py` (2026-10-05, after the last edit): **PASS** ("every number resolves to a verbatim
  source or a confessed convention, and every ledger row matches the document it cites"; phantom citations 0 in every
  governing document).
- ID and quote check (`Test Runs/_research 2026-10-05 MTZ/idcheck.py`): 68 citations, 54 distinct v5 ids, all present in
  `principle_ledger_v5.csv`; no E-ids; every quoted fragment set beside an id was matched inside that row's
  `quote_verbatim` (apostrophes and dashes normalised; `[...]` splits). The script's 11 flags were all filing quotations
  or section titles that fall inside its text window (10-K, proxy and competitor quotations, each attributed to its
  filing in the text), none a ledger quotation.
