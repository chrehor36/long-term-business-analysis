# Company Run — Comfort Systems USA, Inc. (NYSE: FIX) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. This run is blind by instruction: `PORTFOLIO.md`, the holding
reviews, the session-state files, the run queue, the prepped reading list and any other `Test Runs/` file about this company
were not opened. Whether the operator holds or wants FIX is unknown to the analyst.

**CONTAMINATION, declared:** the session opened with the repository map, the operator protocol and a memory index in
context. Those carried the recent commit subjects (PWR closed TOO HARD (WORK) at Q2 on its slack-years margin history;
LINC OUT at Q2; UTI TOO HARD (NATURE) at Q1; a TBTC integrity note) and a one-line queue summary ("57 gate-clearers,
nothing buyable"). None names FIX. The PWR subject line is a sister contractor's verdict and is the nearest thing to a
prior; it was not opened, and the FIX close below rests on FIX's and its competitors' own filings. The directory listing of
`Test Runs/` (file names only) was read to confirm no FIX file existed; none did.

Research folder: `Test Runs/_research 2026-10-05 FIX/` (filings as fetched, text conversions, `hist.py`, `peer.py`,
`peer2.py`, `value_calc.txt`, the rows read in `rows_a.txt` to `rows_c.txt`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1,720.32 (2026-10-05, as printed by `tools/run.py`; **aggregator, live quote only, flagged** under operator
  rule 5).
- **Shares by class** from the latest filing's cover: 35,194,329 common, $0.01 par, one class (10-Q for the period ended
  2026-06-30, filed 2026-07-23, accession `0001104659-26-086258`; `python Screens/cover_shares.py FIX`). Preferred stock
  authorized, none issued (10-Q balance sheet).
- **Market cap:** $60,546M (35.194M × $1,720.32).
- **Sovereign for the earnings currency:** USD 5.63%, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-19, accession `0001104659-26-017530` (Items 1, 1A, 2, 3, 4A, 5, 7, 8 with notes 3, 4, 5,
    6, 7, 8, 9 and 16).
  - 10-Q Q2 2026, filed 2026-07-23, accession `0001104659-26-086258` (statements, revenue disaggregation, backlog,
    cash flow discussion, the Hunt acquisition, buybacks).
  - Proxy (DEF 14A) for the 2026 meeting, filed 2026-04-09, accession `0001308179-26-000245` (summary compensation table
    and PSU design only; Q5 and Q6 were not reached).
  - 8-Ks: 2026-07-23 (`0001104659-26-086255`, Q2 results and dividend), 2026-06-22 (`0001104659-26-076386`, new COO),
    2025-12-19 (`0001104659-25-123112`, President and COO from 2026-01-01), 2025-09-02 (`0001104659-25-086404`, credit
    facility amendment).
  - The cycle record: 10-K FY2011 (`0001047469-12-001931`), FY2020 (`0001558370-21-001828`), FY2022
    (`0001558370-23-001757`), FY2023 (`0001558370-24-001529`), FY2024 (`0001558370-25-001222`); 10-Q Q1 2025
    (`0001558370-25-005411`, searched for one line item).
  - Competitors: EMCOR 10-K FY2025 (`0000105634-26-000025`, read for operating income and its competition paragraph);
    EME, IESC, LMB and MYRG XBRL company facts (SEC API, first-filed values; accessions per figure in the Q2 row).
- **One figure cross-checked against the filed statement:** FY2025 revenue $9,101,641K and operating cash flow
  $1,186,356K in the filed 10-K statements (`0001104659-26-017530`) agree with the XBRL values ($9,102M; $1,186M) that
  `tools/run.py` and `hist.py` transcribe. For the competitor row, EMCOR's FY2025 operating income of $1,713,418K,
  10.1% of revenue, in its filed 10-K agrees with the XBRL value ($1,713.4M).
- `python tools/run.py FIX` arithmetic lines only (its rules, ids and floor are v4 material and were not used, Part VII):
  OCF less SBC less capex, $M: 2023 532 to 545, 2024 687 to 721, 2025 1,010 to 1,023; five-year window 508 to 536;
  the price implies 23.8% growth at 5.63%; ten balance sheets 2016 to 2025 printed and read (Q4 computation below).
  SBC: $12.9M (2023), $16.6M (2024), $21.8M (2025), $28.6M in the first half of 2026 alone (10-Q).

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. A share is a business: the test is whether I would be content to own it "if the market
closed for five years" **[M1997-109]**. The market serves, it does not instruct: the company bought its own stock at
$309.22 a share in April 2025 and at $1,438.19 in 2026 (10-K Item 5; 10-Q note 10), so the quotation has risen more than
five-fold in eighteen months, and "the fact that a given asset has appreciated in the recent past is never a reason to buy
it" **[L2013-007]**; the price "just tells us prices" **[M2006-077]**. No macro enters: the data-center building cycle that
now supplies 58.7% of revenue is not forecast here; what counts is "the average profitability of the business over time
and how strong its competitive mode is" **[M2015-016]**, **[M2000-094]**. The analyst's habit applied: look for "what’s
wrong in things" **[M2025-013]**, and read to "possibly reject your original hypothesis" **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**:
1. *(against the business, found first)* Management's own words, FY2025 10-K MD&A: "the high degree of competition and low
   barriers to entry in most of our markets"; and "we believe that price for value is the most influential factor for most
   customers in choosing a mechanical or electrical installation and service provider."
2. *(against)* 2010 to 2012 operating margins of 1.8%, minus 4.0% and 1.7%, with "a difficult pricing environment" and job
   write-downs (10-K FY2011).
3. *(against the current figures)* Upward revisions of earlier estimates added 7.9% of revenue in the first half of 2026,
   against "not material" in 2018 to 2022 (10-Q; 10-Ks FY2020 and FY2022).
4. *(for the business)* Positive free cash flow in each of the last 27 calendar years (10-K FY2025 MD&A); operating margins
   above EMCOR's in every year 2015 to 2022.
5. *(for)* Customers have paid ahead: billings in excess of costs and deferred revenue of $3,231M at 2026-06-30, against
   cash of $1,855M (10-Q balance sheet).
6. *(against the newest claimed edge)* Modular jobs in 2023 had "lower margins than any of our other businesses" (10-K FY2023).

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin: nothing in the run assumes borrowed money or a forced sale, and the rule
binds the buyer's financing and sizing, not the target **[M2012-081]**, **[L2014-005]**. No finding.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (10-K FY2025, `0001104659-26-017530`, Item 1 and MD&A): a U.S. mechanical (73.3% of 2025
  revenue) and electrical (26.7%) contractor, 50 operating units and 190 locations, run locally ("Our local management
  teams maintain responsibility for day-to-day operating decisions"). 92.7% of revenue is project work; the average project
  is about $2.9 million and takes six to nine months; 8,427 projects were in process at year end. "Our overall price for the
  project is typically set at a fixed amount in the contract"; "we bear the risk of cost overruns in most of our
  contracts" (Item 1A heading). Customers usually pay ahead or as billed: billings in excess of costs and deferred revenue
  were $2,120M at year end 2025 and $3,231M at 2026-06-30 (10-Q `0001104659-26-086258`). Capital is mostly working
  capital: "Our business does not require significant amounts of investment in long-term fixed assets."
- **The customers:** technology 21.4% of revenue in 2023, 33.2% in 2024, 45.0% in 2025, 58.7% in the second quarter of 2026
  (10-K note 3; 10-Q revenue table); one customer 13.8%, 13.3% and 12.8% of revenue in 2023 to 2025 (10-K note 16).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the bid margin, set by how many contractors
  chase the work; (2) the volume of nonresidential construction, and now of data-center construction in particular;
  (3) labor, "the most impact on our project performance" (MD&A); (4) estimating accuracy on fixed-price work. The first,
  third and fourth are the economics of an old trade and can be read from fifteen years of filings; the statements do tell
  me what future statements will look like in kind **[M2008-033]**. The second, the ten-year volume of data-center
  building, I cannot foresee, and its insiders would not write it down **[M2000-105]**.
- **Why that does not close the file here.** Q1 asks for "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, and understanding is of "the economic dynamics of the
  industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**. Those I can judge: the trade's
  economics (fixed-price bids, labor, retainage, customer advances, local competition) have not changed in the fifteen years
  of filings read, and the company's competitive position is described in its own filings in the same words in 2011 and
  2025 (Q2). The demand level is the kind of factor the rows keep out of the decision **[M2015-016]**, and the framework's
  own routing to Q1 TOO HARD (its Q1 text, not a row) is for "a business whose ten-year economics cannot be foreseen because
  its industry changes fast"; the
  mechanical and electrical trades do not, and no technology in the filings threatens the trade itself **[M1998-008]**.
  How far off could I be **[M2011-084]**: far off on the volume, near on the kind of business. The doubt rule
  **[M2002-092]** was put to the economics, not to the volume, and the economics are not in doubt.
- **The contrary reading, written down:** a reader could close here TOO HARD (NATURE) on the ground that 58.7% of revenue
  now depends on a technology customer base whose ten-year spending nobody can forecast **[M2000-105]**, **[L2009-005]**.
  I do not, because the question that decides this file (is there a castle) is answerable from the record without that
  forecast; if the castle were shown durable, the forecast would then matter at Q7 and would be met there.
- **VERDICT: IN.** The economics of a fixed-price mechanical and electrical contractor are inside the perimeter
  **[M1995-051]**, **[M2012-065]**, **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**. The company's own answer, in its 10-K: "We believe that the relative size and
strength of our Balance Sheet and surety relationships, as compared to most companies in our industry, represent
competitive advantages for us" (FY2025 MD&A); design-and-build relationships; "unmatched capability in mechanical off-site
or modular construction" (Item 1); scale and multi-location coverage "over smaller competitors" (Item 1). Each test below
is run against that answer.

**1. The attacker with money** **[M2011-015]**, **[M1997-103]**. The company names its attackers: "there are divisions of
larger contracting companies, utilities and MEP equipment manufacturers that provide MEP services in some of the same
service lines and geographic areas we serve. Some of these competitors and potential competitors have greater financial
resources than we do" (10-K FY2025 Item 1). Its largest public competitor states the door is open to any of them:
"relatively few barriers exist to prevent entry into most of the industries in which we operate. As a result, any
organization that has adequate financial resources, and access to technical expertise, may become a competitor" (EMCOR
10-K FY2025, `0000105634-26-000025`). FIX's own MD&A: "the high degree of competition and low barriers to entry in most of
our markets." This is the industry the rows describe as industries that "are just never going to have barriers to entry"
**[M2012-106]**; and "a dozen people want to go into it" **[M2000-077]** is the observed state, "thousands of local and
regional companies" (Item 1). **Fails.**

**2. Would the customer still choose it over the low bid** **[M2017-009]**. "Typically, customers will seek pricing from
competitors for a given project. [...] we believe that price for value is the most influential factor for most customers"
(MD&A). "a large portion of our work is awarded through a bid process. Consequently, price is often the principal factor in
determining which contractor is selected, especially on smaller, less complex projects. Smaller competitors are sometimes
able to win bids for these projects based on price alone due to their lower cost and financial return requirements"
(Item 1A). The failing answer in the rows is the customer who does not care "from whom they buy" **[L2004-003]**. **Fails**,
in the company's words, for most customers; the large design-and-build data-center jobs are the possible exception
(contrary evidence 5) and are tested under 5 and 6 below.

**3. Pricing power** **[M2005-020]**. No filing read claims it. The 2011 10-K: gross margin fell from 20.0% (2009) to
17.0% (2010) to 14.6% (2011), "primarily from a difficult pricing environment", and management expected "price competition
to continue to be strong, as local and regional competitors respond cautiously to changing conditions". The 2025 10-K:
"we expect price competition to continue as local and regional industry participants compete for customers" and, of
costs, "we may not be able to offset such higher costs through price increases" (Item 1A). Inflation and cost risk are
handled by "escalation and escape provisions in bids and contracts" (Item 1), a contract term, not a price set by the
seller. **Fails.**

**4. The low-cost position, the one exception in a commodity field** **[L2004-007]**, **[L2000-017]**, **[M1997-010]**.
FIX says smaller rivals win on "their lower cost and financial return requirements"; EMCOR says the same of its rivals
("Certain of our competitors have lower overhead cost structures"). On the record, FIX earned less on its tangible
operating assets than EMCOR in every slack year read (operating income over total assets less goodwill, intangibles and
cash, from XBRL; row below): 2011 FIX minus 13% against EMCOR 13%; 2012 6% against 16%; 2013 12% against 13%; 2014 9% against
18%. The rows' measure is cost against the competitor, "on parity or less" **[M2001-013]**; the slack years do not show FIX
there. **Fails** as a castle; not shown to be the low-cost operator.

**5. Did it take adversity and still do well?** **[M2000-032]**. The last downturn is in the filings (XBRL first-filed
values, 10-K FY2011 `0001047469-12-001931` and later):

| | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 |
|---|---|---|---|---|---|---|---|
| Revenue $M | 1,129 | 1,108 | 1,240 | 1,331 | 1,357 | 1,411 | 1,581 |
| Operating income $M | 57 | 20 | -49 | 22 | 46 | 42 | 90 |
| Operating margin | 5.0% | 1.8% | -4.0% | 1.7% | 3.4% | 3.0% | 5.7% |

The 2011 loss includes a $57.3M goodwill impairment and a $1.6M intangible impairment, at four reporting units in Virginia,
Maryland and North Carolina including ColonialWebb, bought in 2010 (10-K FY2011, note on goodwill); before them the 2011 margin was under 1%. In those years the 10-K made the same
claim it makes now: "We believe that the relative size and strength of our balance sheet and surety support as compared to
most companies in our industry represent competitive advantages for us" (FY2011 MD&A). The claimed advantage was present
and the margin was not. The business took adversity and did not do well. **Fails.**

**6. Widening or narrowing, and what the current returns are** **[M1999-108]**, **[L2005-010]**. Operating margin rose from
6.1% (2022) to 8.0% (2023), 10.7% (2024), 14.4% (2025) and 17.0% in the first half of 2026 (10-Q). Three facts say this is
the industry's tide, not a castle: (a) the competitors rose in the same years (row below: EMCOR 5.1% to 10.1%, IES 2.6% to
11.4%, Limbach 2.4% to 7.6%), so "the industry factors will, in my view, just overwhelm any specific strategy"
**[M2000-069]**; (b) the 10-K calls 2025 "an unprecedented overall demand environment"; (c) the newest claimed edge,
modular construction, was in 2023 the business with "lower margins than any of our other businesses" (10-K FY2023
`0001558370-24-001529`) and two years later the source of "improvements in project execution at our Texas modular
operation ($124.3 million)" (10-K FY2025). The row on speed applies: "usually if something can gain competitive advantage
very quickly, you have to worry about them losing it quickly, too" **[M2002-050]**; and leadership alone "provides no
certainties" **[L1996-031]**.

**7. Ask the competitors** **[M2017-091]**, **[M1999-130]**. On the public record, the largest one answers for the
industry: few barriers, competitors with lower overhead, work "frequently awarded through a competitive bidding process",
"downward pressure on our contract prices and profit margins" (EMCOR 10-K FY2025). No competitor filing read names FIX as
the one it fears.

**8. What could destroy or reduce it, five to fifteen years out** **[M2000-014]**. A fall in data-center building, which is
58.7% of revenue, would return the company to the conditions of 2010 to 2012, with fixed-price backlog bid in a
seller's market and estimates revised the other way (Q4 computation, the estimate revisions). One customer is 12.8% of
revenue; "one competitor is frequently enough to ruin a business" **[M2012-108]**, and one buyer with that share can set
the terms.

**The competitor row** (same metrics, from the competitors' own filings via XBRL first-filed values; `peer.py`,
`peer2.py`; EMCOR's FY2025 figure cross-checked to its filed 10-K):

| Operating margin | 2010 | 2011 | 2012 | 2013 | 2014 | 2017 | 2019 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FIX | 1.8% | -4.0% | 1.7% | 3.4% | 3.0% | 5.6% | 6.3% | 6.1% | 6.1% | 8.0% | 10.7% | 14.4% |
| EME (EMCOR) | -0.6% | 3.8% | 3.9% | 3.3% | 4.5% | 4.3% | 5.0% | 5.4% | 5.1% | 7.0% | 9.2% | 10.1% |
| IESC (IES Holdings, FY to Sept.) | -6.3% | -7.3% | -0.1% | n/a | 1.5% | 2.5% | 3.9% | 5.6% | 2.6% | 6.7% | 10.4% | 11.4% |
| LMB (Limbach) | | | | | | 1.2% | 1.5% | 2.9% | 2.4% | 5.7% | 7.4% | 7.6% |
| MYRG (MYR Group) | 4.4% | 3.8% | 5.6% | 6.2% | 6.2% | 2.1% | 2.8% | 4.7% | 3.8% | 3.5% | 1.6% | 4.6% |

| Operating income ÷ (assets less goodwill, intangibles, cash) | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2017 | 2019 | 2021 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FIX | 5% | -13% | 6% | 12% | 9% | 20% | 17% | 17% | 15% | 19% | 26% | 33% |
| EME | -2% | 13% | 16% | 13% | 18% | 16% | 16% | 16% | 17% | 20% | 29% | 30% |
| IESC | -17% | -25% | 0% | 0% | 6% | 12% | 6% | 12% | 15% | 21% | 30% | 29% |
| MYRG | 10% | 9% | 14% | 14% | 15% | 11% | 5% | 7% | 13% | 10% | 4% | 13% |

Accessions for the anchor figures: FIX 2011 `0001047469-12-001931`, 2013 `0001047469-14-001513`, 2020
`0001558370-21-001828`, 2025 `0001104659-26-017530`; EME 2011 `0001193125-12-079814`, 2013 `0000105634-14-000042`, 2020
`0000105634-21-000044`, 2025 `0000105634-26-000025`; IESC 2011 `0001193125-11-346104`, 2020 `0001048268-20-000033`, 2025
`0001048268-25-000174`; LMB 2020 `0001628280-21-005652`, 2025 `0001628280-26-013285`; MYRG 2011 `0001047469-12-002223`, 2013
`0001047469-14-001830`, 2020 `0000700923-21-000007`, 2025 `0000700923-26-000007`. The IESC 2013 value is a tagging gap in the
XBRL and is shown n/a; EMCOR's 2020 figure carries its goodwill impairment of that year. What the row shows: FIX beat
EMCOR on margin in the middle years 2015 to 2022 (contrary evidence 4), trailed it on return in the slack years 2011 to
2014, and moved with the whole group from 2023.

**The contrary case at its strongest, stated before deciding** **[M2025-013]**: FIX may have built something since 2015
that 2011 did not test: large design-and-build data-center jobs, a modular factory network, a labor force of 22,700, and
customers who prepay $3.2B to secure capacity. If those customers would not take the low bid for a data hall, the castle
is new. Against it: the prepayments are the mark of a seller's market in a shortage of skilled labor, which the 10-K calls
"unprecedented"; the competitors' margins rose with FIX's; the modular unit was the lowest-margin business two years ago;
and the company itself, in the year of its best margin, still describes low barriers and price-driven customers. A castle
that exists only while demand exceeds the trade's capacity is the castle "whose moats proved illusory" **[L2007-004]**.

- **VERDICT: OUT.** The castle is shown open on the evidence, by the single fact the filings themselves supply: in the last
  slack market (2010 to 2012), with the same claimed advantages of size, balance sheet and surety, operating margins fell to
  1.8%, minus 4.0% and 1.7% in "a difficult pricing environment", and the company still describes its markets in 2025 as
  having "low barriers to entry" with price the most influential factor for most customers. That is the industry with no
  barriers **[M2012-106]**, whose customers buy on the bid **[L2004-003]**, **[M2017-009]**, and which did not hold up under
  adversity **[M2000-032]**. It is a business an attacker with money could enter, and of that case the row says: "If the
  answer had been yes, we wouldn’t have done it." **[M2011-015]**. The current returns are a demand peak shared by the competitors **[M2000-069]**, and "we would
  not want to buy things on the basis that these returns would be sustained" **[M1998-016]**. In the rows' boxes this is
  OUT, not TOO HARD: the moat is not unknown, it is shown absent **[M2006-013]**. Price does not reopen it **[M2019-015]**,
  **[M2003-040]**.

**The file closes here.** Everything below Q2 is either NOT REACHED or COMPUTATION — NOT A CLEARANCE, kept for the
owner's request and for the record. Nothing below carries entry language.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (closed at Q2). COMPUTATION — NOT A CLEARANCE, recorded because it bears on Q7's arithmetic:
- Capital actually needed **[M2010-090]**, read on tangible assets **[M2011-060]**: tangible equity was $186M (2016),
  about zero (2020), minus $91M (2021), $938M (2025); the business runs on customer money. Billed receivables were 22.0% of
  revenue in 2018 and 28.3% in 2025 (retention $506.5M at 2025 year end, note 3), while contract liabilities rose from 5.9%
  of revenue (2017) to 23.3% (2025) and $3,231M at 2026-06-30. Net of the advances the operating working capital is small,
  which makes return on tangible capital very high (33% on the table's measure in 2025) and makes it a property of the
  demand cycle: the FY2024 10-K says the advances "will reverse when project costs are incurred, except to the extent that
  additional advance payments are received." The return is read for "a cyclical peak in earnings" **[L1994-009]**.
- Reinvestment: depreciation $62.4M against capex $154.9M (2025); first half of 2026 capex $288.8M, including "$188.9
  million of building purchases [...] to support growth in our modular business" (10-Q), against depreciation of $38.6M.
  The two kinds of need are maintenance and growth **[L1999-024]**, and the owner is owed a best guess of the first
  **[M2000-144]**. My guess, stated as one: maintenance is about depreciation, the rest growth spending. The basis is the
  10-K's own sentence, "Our business does not require significant amounts of investment in long-term fixed assets."
- Acquisitions are a standing use of cash: $280M (2025), $235M (2024), $227M (2021), $196M (2019) net of cash acquired,
  plus earn-outs ($88.1M expensed in 2024, $33.5M in 2025) and notes to sellers. Goodwill and intangibles rose from $191M
  (2016) to $1,511M (2025) and $1,636M (June 2026). Accumulated goodwill impairments: $116.6M, all mechanical (note 6).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED** (closed at Q2). COMPUTATION — NOT A CLEARANCE, the balance sheets read first as the row asks: "balance
sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]** (`tools/run.py` table, XBRL
first-filed vintage, read against the FY2025, FY2024, FY2022 and FY2020 filed statements):

| Year-end $M | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 709 | 881 | 1,063 | 1,505 | 1,757 | 2,209 | 2,597 | 3,306 | 4,711 | 6,441 | 8,488 |
| Equity | 377 | 418 | 498 | 585 | 696 | 806 | 1,000 | 1,278 | 1,705 | 2,449 | 3,217 |
| Goodwill + intangibles | 191 | 277 | 330 | 492 | 696 | 897 | 886 | 947 | 1,310 | 1,511 | 1,636 |
| Cash | 32 | 37 | 46 | 51 | 55 | 59 | 57 | 205 | 550 | 982 | 1,855 |
| Contract liabilities (billings in excess, deferred revenue) | n/a | 106 | 131 | 167 | 226 | 307 | 462 | 910 | 1,149 | 2,120 | 3,231 |
| Long-term debt | 2 | 60 | 74 | 205 | 236 | 385 | 247 | 39 | 62 | 139 | 54 |
| Retained earnings | 124 | 168 | 269 | 369 | 503 | 629 | 855 | 1,148 | 1,627 | 2,581 | 3,340 |
| Treasury stock at cost | 57 | 64 | 88 | 104 | 129 | 151 | 187 | 210 | 274 | 496 | 517 |

What the figures say: equity grew mainly by retained earnings; goodwill and intangibles grew faster than equity until 2021
(tangible equity reached minus $91M), with acquisitions funded partly by debt that peaked in 2021 and was repaid by 2023.
Cash has never exceeded the customers' advances, so the cash pile is the customers' money, not surplus. Receivables rose
faster than revenue. What they do not say: how much of the 2025 to 2026 margin rests on estimate revisions (below). What
they cannot say: what the advances do when the data-center cycle turns.
- **The estimate revisions.** "net revenue recognized from our performance obligations partially satisfied in the previous
  period positively impacted revenue by 3.9%, 2.3% and 1.3%" for 2025, 2024 and 2023 (10-K FY2025 note 3), and by 7.9% in
  the first half of 2026 (10-Q). The FY2020 and FY2022 10-Ks called the comparable item "not material", and the FY2023 10-K
  called 2023 "not material" before the FY2025 10-K quantified it at 1.3%. In dollars: about $355M of 2025 revenue (27% of
  operating income) and about $484M in the first half of 2026 (46% of operating income), on cost-to-cost accounting where
  a revision of estimated cost moves revenue and profit together. The rows name "construction in progress or progress
  payment-type things" as a place "you can cheat in accounting" **[M2013-086]** and warn of the "subsequent release back into
  earnings" **[M1999-048]**. No sign of a make-the-numbers habit was looked for (Q4 not reached); this is recorded as a
  weighing against the durability of the reported margin, not as a tell, and the job write-downs of 2010 and 2011 show the
  same mechanism running the other way.
- **One unexplained line:** "Repayments to customers" of $250.0M sat in other current liabilities at 2024 year end and zero
  at 2025 year end (10-K FY2025 note 8). No explanation found in a text search of the FY2024 10-K, the FY2025 10-K and the
  Q1 2025 10-Q for "repay", "refund", "overpay" and "returned to". It is a liability, conservative in direction; recorded,
  not weighed.
- **Real costs:** the company reports free cash flow as OCF less capex, and does not feature EBITDA; EBITDA appears only as
  the credit-facility covenant term and in the proxy's peer-group criteria. Stock pay $21.8M (2025) is expensed. Accrued job
  losses doubled, $21.6M to $44.0M (note 8). Earn-out remeasurements are expensed and kept in owner cash as a cost of the
  acquisitions **[L2021-003]**.

## Q5 — WHO RUNS IT. STOP on integrity.
**NOT REACHED.** Record only: chief executive Brian Lane since December 2011, chief financial officer William George since
2005 (founding team, 1997); total 2025 pay of the CEO $10.62M (proxy, `0001308179-26-000245`); performance shares on EPS and
relative TSR. No judgment is made.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Record only: buybacks under a share-count authorization with no stated price, 445,172 shares in 2025 at an
average $489.40 and under 0.1 million shares in the first half of 2026 for about $8.2M at an average $1,438.19 (10-K Item 5; 10-Q); cumulative 10.9 million shares at an average
$50.88. Against the computed range below, the 2026 purchases sat far above its top and the 2025 purchases above it. No
judgment is made.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED** (closed at Q2). **COMPUTATION — NOT A CLEARANCE**, at the owner's request. The construction is the
framework's CONVENTION (Part VI): owner cash after every real cost **[L2021-003]**, **[L2015-004]**, **[M2012-034]**, five-year
average **[L2005-003]**, carried at the growth shown and capped by Q3 **[M1997-095]**, **[M1999-067]**, ten years then no
growth, at the long government rate **[L2000-021]**, **[M1996-025]**, the ends being the no-growth and shown-growth cases
**[L2000-024]**.
- **Owner cash**, $M = net income (after stock pay, earn-outs and tax) + depreciation + amortization of acquired intangibles
  − all capital spending. Working-capital swings are left out on purpose: OCF in 2023 to 2025 carried roughly $1.3B of
  customer-advance build that the company says will reverse (Q3), which is why `tools/run.py`'s OCF-based window (508 to
  536) runs above this one. Amortization is added back as the framework's Q4 allows; the variant without the add-back is shown.

| | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr average |
|---|---|---|---|---|---|---|
| Net income | 143.3 | 245.9 | 323.4 | 522.4 | 1,022.6 | |
| + Depreciation | 28.4 | 33.6 | 38.2 | 48.2 | 62.4 | |
| + Amortization | 40.5 | 47.8 | 43.4 | 97.3 | 79.6 | |
| − Capex (all) | 22.3 | 48.4 | 94.8 | 111.1 | 154.9 | |
| **Owner cash (main)** | **190.0** | **278.9** | **310.1** | **556.8** | **1,009.6** | **469.1** |
| Depreciation variant (capex = depreciation) | 183.9 | 293.7 | 366.8 | 619.7 | 1,102.1 | 513.2 |
| No amortization add-back | 149.5 | 231.1 | 266.7 | 459.6 | 930.0 | 407.4 |

- **Growth shown:** 51.8% a year on aggregate owner cash, 2021 to 2025. Carried for ten years it multiplies the base
  sixty-five-fold; trace out that arithmetic and "you bump into absurdities" **[M1999-067]** and is capped at the discount rate **[M1997-095]**.
  Returns at this level are not assumed to last **[M1998-016]**, and the five-year window contains no slack year.
- **Value range** (main base $469.1M, 35.194M shares, 5.63%): no-growth end $8,332M, **$237 a share**; shown-growth end
  capped at 5.63%, $13,023M, **$370 a share**. Width 1.56 to one, inside the three-to-one convention. Depreciation variant
  $259 to $405; no-add-back variant $206 to $321. No cash is added: cash ($1,855M) is less than the customers' advances
  ($3,231M) at 2026-06-30.
- **Against the price of $1,720.32:** the price is 4.6 times the top of the range. The expected return at the price, on
  the shown-growth stream, is 1.31% a year after tax (0.77% on the no-growth stream), below the 5.63% bond. Even the
  trailing twelve months to 2026-06-30 as the base (owner cash $1,199.6M; depreciation variant $1,517.7M), carried at the
  cap, gives a top of $946 (or $1,197) a share and an expected return of 3.2% (4.0%). The price implies 23.8% growth a
  year for ten years (`tools/run.py` arithmetic line).
- **The floor** (CONVENTION, about ten percent pre-tax) **[M2003-149]**, **[L2002-020]**, **[M1994-004]**, qualified by
  **[M2003-151]**: owner cash is after corporate tax, so ten percent pre-tax is taken as 7.9% after tax at the 20.9%
  effective rate the FY2025 10-K reports (MD&A, provision for income taxes). This conversion is mine.
- **(a) FAIR-PRICE BAND, COMPUTATION:** prices inside the value range at which the expected return is at or above the
  floor. On the shown-growth stream the floor is met at or below **$255**; on the no-growth stream at or below $169, which
  is under the range. The band is therefore **$237 to $255 a share**, and only if the growth case is granted.
- **(b) CHEAP PRICE, COMPUTATION:** the price at which even the no-growth case clears the floor with no growth assumed:
  **$169 a share or below** (no-growth stream, 7.9% after tax). Applying ten percent to the after-tax cash instead gives
  $133. The rows ask that a decision "scream at you" **[M2009-005]**, **[M1996-084]**, and a cyclical contractor whose base
  holds no slack year would need a margin below either figure; this is my reading, not a row.
- What the computation would have closed, had the file reached it: OUT, the price above the top of a narrow range and
  the expected return below the floor **[M2003-149]**. It did not reach it.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.** (COMPUTATION only: the expected return at the price, 0.8% to 1.3% after tax on the five-year base, is
below the 5.63% Treasury **[M1997-089]**.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Record only: long-term debt $53.8M at 2026-06-30; revolver $1.1B to October 2030; surety bonds on 10% to
20% of the business; self-insured to $500,000 a claim with $250M aggregate excess cover (10-K note 13). Not weighed.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** The draft would have the buyer do nothing **[M2008-085]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT ASKED.** No named business is involved.

---
## THE BOX
**OUT, at Q2.** The castle is shown open: the filings record low barriers to entry and price-driven customers in the
company's own words in 2025, and the last slack market (2010 to 2012) took operating margins to 1.8%, minus 4.0% and 1.7%
with the same claimed advantages in place; the 2023 to 2026 margins rose with the whole competitor group. Q7 not reached;
as COMPUTATION — NOT A CLEARANCE the range is $237 to $370 a share against $1,720.32, fair-price band $237 to $255, cheap
price $169 or below. No research pass is owed: the box is OUT, not TOO HARD (WORK).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied and the research folder made before the first
      EDGAR call). [ ] Written question by question and committed after each: **not done**. The file was written in one
      pass after the reading, and nothing was committed, by the instruction for this run (no commits). Write-early was not
      kept; a session killed mid-run would have left the template only.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`; no v4 id is used); every filing fact has
      its accession; numbers come from filings or carry the convention they rest on.
- [x] The order was kept; Q2 closed the run; Q3, Q4 and Q7 text is headed COMPUTATION — NOT A CLEARANCE and carries no
      entry language; Q5, Q6, Q8, Q9 and Q10 hold record lines only.
- [x] Owner cash after every real cost, never a net-income proxy: net income plus non-cash charges less all capital
      spending, with stock pay and earn-outs inside it and the depreciation variant beside it (operator rule 5); the
      sovereign from the US Treasury, dated; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, in both directions (Foundations, items 1 to 6).
- [x] No row dated after the anchor is cited (the run is dated today; not a point-in-time test).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` run before handing back (result recorded in the reply to the operator).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 has no rule for a customer base that changes fast inside a trade that does not.** The routing sends "a business
   whose ten-year economics cannot be foreseen because its industry changes fast" to Q1 TOO HARD. FIX's trade is old; its
   customers (58.7% technology) are in the fastest-changing field there is. Whether that is Q1 TOO HARD (NATURE) or a demand
   level that Q1 sets aside (as macro, **[M2015-016]**) is not said. I passed Q1 and wrote the contrary reading down; a
   second analyst could close at Q1 with equal citation, and the box would differ (TOO HARD instead of OUT).
2. **Q2's OUT and TOO HARD turn on the age of the evidence.** The decisive slack-year record is fifteen years old and the
   business has since changed its mix. The framework says a castle "shown open on the evidence" is OUT and one whose future
   "cannot be judged" is TOO HARD, but not how old the showing may be, nor whether a new line of business (modular, data
   halls) must be shown open separately. I treated the company's own present-tense description of low barriers as carrying
   the old record forward; a rule would help.
3. **Q7's growth cap is unstated as a number.** The CONVENTION caps shown growth by "no rate that runs past the discount
   rate"; with 51.8% shown, I capped at the discount rate itself, which makes the top end the no-growth value plus ten years
   of flat present value. Another analyst could cap lower or higher. The five-year average also spans a five-fold change in
   size and no slack year, and the convention has no cycle rule beyond **[L2005-003]** and **[L1994-009]**.
4. **The floor is pre-tax; owner cash is after tax.** The convention says "about ten percent pre-tax" and the construction
   uses after-tax owner cash; the conversion is not stated. I used the filing's effective rate (20.9%) to get 7.9% after
   tax, and showed the stricter ten-percent-after-tax figures beside it.
5. **Customer advances.** The convention does not say whether cash funded by customer prepayments counts toward value, nor
   how to treat operating cash flow swollen by advances that will reverse. I excluded both and said why; `tools/run.py`'s
   OCF-based owner earnings include them.
6. **Q4's tells do not name cost-to-cost estimate revisions.** **[M2013-086]** names construction-in-progress accounting as
   a place to cheat, but the tells list gives no test for a rising share of profit from revised estimates (7.9% of revenue,
   46% of operating income in the first half of 2026). I recorded it as a weighing; with Q4 not reached it decided nothing.
