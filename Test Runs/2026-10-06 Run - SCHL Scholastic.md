# Company Run — Scholastic Corporation (NASDAQ: SCHL) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. This run is blind: its instructions forbid opening
`PORTFOLIO.md`, any holding review, the resume-state files, the run queue and the prepped reading list. Whether the
operator holds SCHL is unknown to the analyst.

**CONTAMINATION, declared.** The session context showed: the file names (not the contents) of the other runs dated
2026-10-06 in `Test Runs/` (ADT, ASO, BCC, BTU, COLL, CVSA, EMN, GPOR, HRMY, INSW, LRN, MD, MHK, MHO, MTCH, NSIT, NWL, NX,
PATK, PTEN, REYN, TPC, UPWK, WKC, WWW) and an addendum's file name; the commit subjects of the UPWK, WWW, LRN and INSW runs
(their boxes and prices); and a memory-index line saying the register held 57 gate-clearers and nothing buyable. None of
these concerns Scholastic. No file about SCHL exists in `Test Runs/` (directory listing checked before the copy). Nothing
else was opened outside the framework, the template, the ledger, the protocol and the filings.

**Working folder:** `Test Runs/_research 2026-10-06 SCHL/` (filings as text, `fetch.py`, `ledger.py`, `compute.py` and its
output `compute_output.txt`, `run_py_output.txt`, `cover_shares_output.txt`, competitor filings in `peers/`).

**A premise corrected at the outset.** The brief says Scholastic "owns its New York headquarters". It no longer does. On
2025-12-17 it sold 555-557 Broadway for $386.0M and its Jefferson City, Missouri distribution centre for $95.0M and leased
both back (15-year and 20-year terms) (8-K 2025-12-05, accession 0001193125-25-309611; 8-K 2025-12-18, 0001193125-25-324788;
10-K FY2026 Note 4, 0000866729-26-000018). So no real estate is left to read as a separate part. What is left is the leases,
and owner cash has to carry their cost.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $37.41 (close 2026-10-05, from `tools/run.py`; an aggregator quote, live only, flagged per operator rule 5).
  The tender offer of April 2026 paid $40.00, and the estate bought back on 2026-08-26 at $39.7603 (below).
- **Shares by class** from the latest filing's cover: Common 17,581,344, Class A 828,100 (10-Q for the quarter to
  2026-08-31, filed 2026-09-25, accession `0000866729-26-000025`; `python Screens/cover_shares.py SCHL`). **Charter note
  read:** "Class A Stock ... is convertible, at any time, into Common Stock on a share-for-share basis" (10-K FY2026,
  Item 5). The dividend is paid "per Class A and Common share" (same item), and earnings per share are reported "of Class A
  and Common Stock" together. So the two classes are economically equal and differ only in voting. **Shares used:
  18,409,444.** *(`tools/run.py` used the common count alone, 17.6M. That is corrected here.)*
- **Market cap:** 18,409,444 × $37.41 = **$688.7M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - **10-K FY2026** (year to 2026-05-31), filed 2026-07-24, `0000866729-26-000018`: Items 1, 1A, 2, 5 and 7; the financial
    statements; Notes 3 (segments), 4 (sale and leaseback), 5, 6 (debt), 11 (leases), 12 (9 Story) and 16.
  - **10-Q** for the quarter to 2026-08-31, `0000866729-26-000025`.
  - **DEF 14A** 2026-08-07, `0001193125-26-340209`: ownership, Class A, the summary compensation table, incentive metrics,
    special bonuses.
  - **8-Ks:** the sale-leasebacks (above); the tender announcement `0000866729-26-000005`; the tender's final results
    `0001193125-26-173633` (Ex. 99(a)(9)); the estate repurchase `0001193125-26-371245`; FY2026 results
    `0000866729-26-000015` (Ex. 99.1); Q1 FY2027 results `0000866729-26-000022` (Ex. 99.1).
  - **Older 10-Ks for the span:** FY2008 `0000930413-08-004578`, FY2011 `0000930413-11-004927`, FY2014
    `0000866729-14-000008`, FY2017 `0000866729-17-000009`, FY2018 `0000866729-18-000008`, FY2019 `0000866729-19-000009`,
    FY2020 `0000866729-20-000010`, FY2023 `0000866729-23-000019`, FY2025 `0000866729-25-000020`.
  - XBRL company facts for revenue, operating income, operating cash flow, capex, stock pay, taxes paid, buybacks and
    dividends, FY2009 to FY2026 (first-filed values; the FY2009 to FY2014 values include the educational-technology
    business sold in 2015).
- **One figure cross-checked against the filed statement:** operating cash flow for FY2026 is $50.9M in `tools/run.py`
  and $50.9M in the filed Consolidated Statement of Cash Flows (10-K FY2026). PP&E additions match too, $48.4M in both.
  Equity at 2026-05-31 is $750.8M in both the run.py table and the filed balance sheet.
- **`tools/run.py` arithmetic lines only.** Its capex column is PP&E alone. **It leaves out prepublication expenditures**,
  a separate investing line: $17.9M, $24.5M and $22.8M in FY2026, FY2025 and FY2024. That spending is capital and is
  deducted below. Royalty advances and film and television spending sit inside operating cash flow, so they are already
  deducted. Stock pay was $8.5M, $9.3M and $11.0M. run.py's own owner-earnings means, its yields and its "growth the price
  assumes" line are not used. They also predate the sale-leaseback recast.

**Owner cash after every real cost, by year** (operating cash flow less stock pay, PP&E capex, prepublication spending
and finance-lease principal; USD M; filed cash-flow statements of the 10-Ks named above):

| FY (May) | OCF | stock pay | PP&E capex | prepub | fin. lease | **owner cash** | what moved it |
|---|---|---|---|---|---|---|---|
| 2017 | 142.2 | 10.1 | 65.7 | 26.9 | 2.0 | **37.5** | Harry Potter and the Cursed Child year |
| 2018 | 141.5 | 10.7 | 121.5 | 36.1 | 2.0 | **−28.8** | headquarters rebuild capex |
| 2019 | 116.4 | 8.3 | 95.0 | 38.1 | 2.0 | **−27.0** | headquarters rebuild capex |
| 2020 | 2.1 | 3.8 | 62.7 | 28.5 | 2.0 | **−94.9** | schools closed (COVID) |
| 2021 | 71.0 | 6.6 | 47.2 | 20.7 | 2.3 | **−5.8** | fairs at a third of normal |
| 2022 | 226.0 | 7.8 | 42.0 | 17.2 | 2.3 | **156.7** | includes a net tax *refund* of $48.8M |
| 2023 | 148.9 | 10.5 | 62.0 | 26.9 | 2.3 | **47.2** | |
| 2024 | 154.6 | 11.0 | 58.4 | 22.8 | 2.3 | **60.1** | inventory release of $50.9M |
| 2025 | 124.2 | 9.3 | 52.2 | 24.5 | 1.7 | **36.5** | |
| 2026 | 50.9 | 8.5 | 48.4 | 17.9 | 2.1 | **−26.0** | tax on the real-estate gain, about $41.4M |

Five-year mean (FY2022 to FY2026), as filed: **$54.9M**. Ten-year mean (FY2017 to FY2026), as filed: **$15.6M**. All of
it was earned while the company owned its headquarters and its main warehouse and collected rent from the retail tenants
at 557 Broadway ($9.7M, $11.2M and $7.2M of rental income in FY2024 to FY2026; 10-K FY2026 Note 11). From FY2027 it pays
rent instead. The company's own comparable figures put the full-year cost at about $30M pre-tax: FY2025 Adjusted EBITDA
was $145.4M as reported and $115.3M "on a comparable basis" (8-K 2026-07-23, Ex. 99.1). The two new leases cost "approximately $23.7
annually" (in millions, Note 4), and the lost rental income comes on top of that. The recast is carried to the
COMPUTATION section.

**The balance sheets, nine year-ends, read before the income account**, "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]** (run.py ten-year table, first-filed
XBRL, checked against the FY2026 and FY2025 filed balance sheets; USD M):

| May 31 | assets | equity | cash | receivables | inventory | goodwill | intangibles | LT debt | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2018 | 1,825 | 1,321 | 392 | 205 | 295 | 119 | 12 | 0 | 1,065 |
| 2019 | 1,878 | 1,272 | 334 | 250 | 324 | 125 | 14 | 0 | 1,013 |
| 2020 | 2,034 | 1,179 | 394 | 240 | 271 | 125 | 13 | 211 | 948 |
| 2021 | 2,008 | 1,181 | 366 | 256 | 270 | 126 | 10 | 7 | 916 |
| 2022 | 1,941 | 1,217 | 317 | 299 | 281 | 125 | 8 | 0 | 976 |
| 2023 | 1,867 | 1,163 | 224 | 278 | 334 | 133 | 10 | 0 | 1,036 |
| 2024 | 1,671 | 1,018 | 114 | 235 | 264 | 133 | 10 | 0 | 1,024 |
| 2025 | 1,950 | 946 | 124 | 273 | 250 | 199 | 88 | 250 | 1,000 |
| 2026 | 1,728 | 751 | 135 | 236 | 265 | 199 | 78 | 75 | 1,038 |

What the figures say:
- **Retained earnings did not grow in eight years.** They were $1,065M in 2018 and $1,038M in 2026. Over the whole
  span, net income just about covered the dividends ($0.80 a share a year). The 2026 figure is held up by the $99.7M
  real-estate gain.
- **Equity fell from $1,321M to $751M through buybacks.** Treasury stock reached $853.8M. Cash went from $392M to $135M.
  The company had no debt in 2018. It borrowed $250M in 2025 to buy 9 Story, which added $64.2M of goodwill and $85.3M of
  identified intangibles. Most of that loan was repaid in 2026 from the real-estate proceeds.
- **Receivables and inventory held steady against flat sales.** Revenue was $1,628M in FY2018 and $1,582M in FY2026.
  Neither balance shows a build-up that would be a tell. Deferred revenue of $179.2M is mostly book-fair incentive
  credits owed to schools. That is a real obligation, and it also funds the company.
- **PP&E fell from $516M to $202M in 2026** with the sale. Operating lease right-of-use assets rose from $104M to $291M,
  and lease liabilities from $118M to $307M. Building ownership has turned into a lease obligation discounted at 10.4%
  (Note 4).

What they do not say: the worth of the school relationships and of the publishing rights. They also do not show that the
royalty advance book is mostly reserved: the reserve was $92.7M against a net balance of $64.6M at 2026-05-31 (10-K
Note 1), so most advances paid are never earned back.

## THE FOUNDATIONS (not a gate)
A share is a business. The test is whether I would own Scholastic happily if the market closed, because "then you’re
buying a business" **[M1997-109]**. The market price of $37.41 instructs nothing. The company's own Adjusted EBITDA
headline and its guidance are projections and the company's own advocacy. They are read as filing facts and are never
used to value the business, since "we’ve never looked at a projection in connection with either a security we’ve bought
or a business we’ve bought" **[M1995-050]**. The habit that governs this run is to hunt what is wrong: "I’m looking for
what’s wrong in things because that’s part of investing" **[M2025-013]**. Contrary evidence is to be written down at once,
"write it down in the first 30 minutes" **[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. *(Against the castle.)* The FY2018 10-K says competitors "include regional and local school-based book fair operators,
   as well as the recent entry of a competitor operating on a national level". The FY2019 10-K reports lower book-fair
   revenue "primarily driven by lower fair count as a result of a more competitive marketplace". The 10-Ks for FY2008,
   FY2011, FY2014 and FY2017 name no national competitor.
2. *(Against the castle.)* Book clubs revenue was $340.9M in FY2009 (10-K FY2011), $224.3M in FY2018 (10-K FY2020) and
   $57.1M in FY2026 (10-K FY2026 Note 2), "primarily due to lower sponsor participation".
3. *(For the castle, found while hunting against it.)* US book fairs revenue reached a record $576.0M in FY2026, up from
   $541.6M in FY2024, "driven by higher fair count as well as higher revenue per fair". The national entrant has not
   displaced Scholastic in eight years. The filer still calls itself "the leading operator of school-based book club and
   book fair proprietary channels".
4. *(Against.)* Consolidated operating income was $14.5M, $15.8M and $15.2M in FY2024 to FY2026, on $1.6bn of revenue a
   year.
5. *(For.)* The Children's Book Publishing and Distribution segment earned $142.9M in FY2026, a 14.8% margin, its best
   level of the decade.
6. *(Against.)* The company's own risk factor says generative AI poses "a broader and more fundamental set of risks to
   the Company's core business model". The filer writes this; I do not.

## THE STANDING RULE
Owning this would not put the buyer at risk of ruin, provided it is bought with the buyer's own money and sized so that a
total loss is survivable. "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**. Borrowing to buy it is ruled out by the same
rule: "the only way smart people can get clobbered, really, is through leverage" **[M2004-065]**. No question below
depends on how the purchase would be financed.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The test is "a reasonable fix on about what the earning power and competitive position will look like in five or 10
years" **[M2012-065]**. The method is to identify "the key variables in that particular business, and evaluating how
predictable they were first" **[M1998-044]**.

The key variables, from the filings:
- **(a) School book fairs:** fair count and revenue per fair. These are US schools, teachers and parent groups, so the
  question is consumer and institutional behaviour, not technology. The filer has run fairs since 1981 and clubs since 1948.
- **(b) The trade backlist and new hits.** Harry Potter, The Hunger Games, Dog Man, Wings of Fire and The Baby-Sitters
  Club. The top five US trade customers take about 74% of US trade sales (10-K FY2026 Item 1A).
- **(c) Education spending by schools and districts.** The filer says this depends on federal, state and local funding,
  which is "subject to significant uncertainty".
- **(d) Corporate overhead:** $113.9M in FY2026 and $108.1M in FY2025.
- **(e) Entertainment (9 Story),** a small part: revenue $65.7M in FY2026, an operating loss of $16.1M.

What I can foresee. The school channel, the backlist and the overhead are knowable from twenty years of filings, and they
are about the behaviour of children, parents and teachers. That is the kind of forecast the rows accept: "we know what we
think we can project out in terms of consumer behavior and threats to a business" **[M2023-030]**. I can write the
ten-year picture down. Scholastic remains the leading US school book-fair operator, against at least one national rival.
Clubs are smaller or gone. Trade swings around a durable backlist. Education is small and depends on budgets. Group
operating margins are low and volatile, as they have been for eighteen years (averaging 3.0% from FY2009 to FY2026; see
Q2). That is a reasonable fix on earning power and position. It is a fix on a mediocre economics, which is still
understanding.

What I cannot foresee:
- New hits. In children's trade, "Charlie and I can't determine whether we are dealing with a 'pet rock' or a 'Barbie.'"
  **[L1993-023]** *(inner quotation marks rendered as single quotes; the row has double)*. The record bounds this
  variable: trade has swung around its backlist in hit years (FY2012, FY2017, FY2025) and returned each time.
- Education funding and AI-based teaching tools. These are a minority part, now earning about nothing (segment results of
  $15.8M, $6.3M and −$4.1M in FY2024 to FY2026).

On "how far off we can be" **[M2011-084]**: narrow on the school channel and the overhead, wide on trade hits and
Education. The doubt rule, "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**, was weighed. My doubt attaches to the parts in (b) and (c) that cannot be forecast, not to the
economics of the whole. The whole is a school-channel distributor and publisher whose earning power has been low for
eighteen years. That I can state with confidence.

Routing: this is not a fast-changing technology business, so Q1 does not route it to TOO HARD. The generative-AI risk is
the filer's own disclosure. It is written down as contrary evidence 6 and carried to Q2, test 11.

- **VERDICT: IN.** The ten-year economics of the parts that carry the earnings, the school channel and the backlist, can
  be foreseen well enough to judge. The parts that cannot (new hits, Education funding) are bounded by the record and are
  not where the earnings sit.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, asked of a castle the speakers define by what it
protects: "A truly great business must have an enduring 'moat' that protects excellent returns on invested capital."
**[L2007-004]** *(inner quotation marks rendered as single)*. Scholastic's claimed castle is a distribution system, the
school channel ("the strength of their distribution systems" **[L1993-021]**), plus a brand trusted by teachers and a
children's backlist. The tests, each with its filing fact:

1. **The castle questions: what keeps it standing, and how permanent is it?** What keeps it standing: about 40 book-fair
   warehouses, a delivery fleet, the schools' fundraising incentive (credits redeemable for books, $127.2M of them
   outstanding at 2026-05-31), and a curated selection under a name teachers trust. How permanent: the fairs have run
   since 1981. The clubs, which ran on the same school relationships since 1948, have not held (test 5).
2. **Would it stand without the lord?** Yes. The controlling founder-chairman Richard Robinson died in June 2021 and the
   business carried on under a hired chief executive (DEF 14A 2026, pay-versus-performance notes). It does not depend on a
   genius.
3. **The money test.** "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. Here the answer has been
   partly yes, and the filer records it. A national entrant arrived around FY2018 (FY2018 10-K, quoted above) and is still
   there eight years later ("one other competitor operating on a national level", 10-Ks FY2020 to FY2026). It took fairs
   from Scholastic: "lower fair count as a result of a more competitive marketplace" (10-K FY2019). The entrant is private
   and files nothing, so its size is unknown. The rows warn that "one competitor is frequently enough to ruin a business"
   **[M2012-108]**. It has not ruined this one, but it got in.
4. **Pricing power.** Revenue per fair rose about 7% in FY2017 and about 2% in FY2018 (both 10-K FY2018), about 5% in
   FY2023 (10-K FY2023) and again in FY2026. It was "slightly lower" in FY2025 (10-K FY2025). There is some pricing, but over seventeen years it did not carry the fair
   channel ahead of inflation. Fair revenue grew from $415.8M in FY2009 to $576.0M in FY2026, about 2% a year in nominal
   dollars (10-K FY2011; 10-K FY2026 Note 2).
5. **Unit volume and share of mind.** Fair count fell 9% in FY2017, "reflecting in part the fiscal 2017 strategy to reduce the
   number of lower margin fairs" (10-K FY2018), and fell again in FY2019 to competition. COVID followed. Fair count was "approximately 85% of pre-pandemic levels" in FY2023, and the
   FY2023 10-K expected about 90% in FY2024. It has risen since, but no filing read says it regained the FY2017 level.
   Clubs: $340.9M (FY2009), $298.2M (FY2011), $224.3M (FY2018), $126.4M (FY2022), $62.7M (FY2024), $57.1M (FY2026). That
   is down 83% in seventeen years, on "lower sponsor participation". The rows' failing answer: "Fixed costs are high in
   the newspaper business, and that's bad news when unit volume heads south." **[L2006-009]**. The whole school channel,
   fairs plus clubs, brought in $756.7M in FY2009 and $633.1M in FY2026, 16% less in nominal dollars.
6. **The low-cost position.** Scholastic is the scale operator in school fairs, but no filing gives unit costs for it or
   for the entrant. At group level it is not the low-cost publisher: its operating margin trails both public trade
   publishers by a wide gap every year (the competitor row).
7. **The brand in the customer's mind.** It is trusted by teachers and parents (the filer's Item 1A on reputation). In
   trade, the five largest retailers take 74% of US trade sales. There "the value of having the brand moves over to the
   retailer from the product itself" **[M2001-090]**. My reading, not a filing fact: a child asks for Dog Man by its author
   and character, not by its publisher's name.
8. **Would the customer still choose it over the low bid?** For a fair, the school's "bid" is the share of proceeds or
   credits it receives. Scholastic's own response in FY2017 was to "reduce the number of lower margin fairs" (10-K FY2018),
   and its lost fairs in FY2019 went to "a more competitive marketplace" (10-K FY2019). The customer does weigh the bid.
9. **Ask the competitors.** The fair entrant is private and unreachable from the public record. The public trade
   publishers are in the competitor row below. The question cannot be put to anyone by this run, which is recorded as
   such.
10. **Widening or narrowing?** "how wide the moat is and whether it’s likely to widen further or shrink on you"
    **[M1999-108]**. On the filer's own words it has narrowed. A national entrant appeared in a channel where the 10-Ks for
    FY2008, FY2011, FY2014 and FY2017 named none. The clubs wall has mostly fallen. Education revenue fell from $351.2M to
    $267.6M in two years. Group revenue was $1,635.8M in FY2015 (continuing operations, 10-K FY2017) and $1,581.9M in
    FY2026, even after buying 9 Story ($65.7M of FY2026 revenue). That is a decline in nominal dollars over eleven years
    and a larger one in real terms. The rows name this pattern: "if we treat customers with indifference or tolerate
    bloat, our businesses will wither" **[L2005-010]**. Corporate overhead not charged to any segment was $106.5M,
    $108.1M and $113.9M in FY2024 to FY2026, about 7% of revenue (Note 3).
11. **What could destroy, modify or reduce it?** The filer names generative AI, school access, the funding of
    Education, and the "one other competitor". The slow forms are the dangerous ones: "slow change can be much harder to
    perceive" **[M2014-038]**.

**The competitor row.** Operating margin is the same metric for all three. For Scholastic it is consolidated operating
income over revenue. For HarperCollins it is News Corp's Book Publishing Segment EBITDA less the segment's depreciation
and amortization, over segment revenue. For Simon & Schuster it is the Publishing segment's operating income over
revenue. Every figure is from the company's own 10-K.

| fiscal year | Scholastic (consolidated) | Scholastic, Children's Book Publishing & Distribution segment (before overhead) | HarperCollins (News Corp) | Simon & Schuster (CBS / ViacomCBS) |
|---|---|---|---|---|
| 2009 | 3.3% | | | 5.4% |
| 2010 | 6.7% | $117.9M op. income | | 7.7% |
| 2011 | 5.3% | $78.1M | | 10.5% |
| 2012 | 8.7% (Hunger Games) | $152.2M | 5.0% | 10.1% |
| 2013 | 3.8% | $24.5M | 7.9% | 13.1% |
| 2014 | 3.5% | $22.8M | 11.2% | 12.9% |
| 2015 | 2.0% | $94.6M | 10.1% | ≈13.8% |
| 2016 | 4.0% | $120.6M | 7.9% | ≈14.7% |
| 2017 | 5.1% | $143.1M | 9.0% | ≈15.2% |
| 2018 | 3.4% | | 10.6% | 17.2% |
| 2019 | 1.5% | $82.9M | 12.0% | 15.6% |
| 2020 | −6.0% | $23.6M | 10.9% | 15.6% |
| 2021 | −1.7% | | 13.5% | (sold; not public after 2020) |
| 2022 | 5.9% | $115.3M | 11.7% | |
| 2023 | 6.2% | $143.4M | 6.0% | |
| 2024 | 0.9% | $123.3M | 10.3% | |
| 2025 | 1.0% | $130.7M | 11.3% | |
| 2026 | 1.0% | $142.9M (14.8%) | 9.9% | |
| **mean** | **3.0% (FY2009-26)**; 2.6% (FY2012-26) | | **9.8% (FY2012-26)** | **12.7% (2009-20)** |

Sources and caveats:
- **Scholastic:** XBRL operating income and revenue as first filed. FY2009 to FY2014 include the educational-technology
  business sold in 2015. Segment figures are from the MD&A of the 10-Ks for FY2011, FY2014, FY2017, FY2020, FY2023 and
  FY2026. The overhead allocations changed between eras, so the segment column is comparable within an era only.
- **HarperCollins:** News Corp 10-Ks FY2014 `0001193125-14-309269`, FY2017 `0001193125-17-257248`, FY2020
  `0001564708-20-000022`, FY2023 `0001564708-23-000368`, FY2025 `0001564708-25-000419` and FY2026
  `0001564708-26-000175`. Segment EBITDA excludes News Corp's corporate costs.
- **Simon & Schuster:** CBS 10-Ks for 2011 `0001047469-12-001373`, 2014 `0000813828-15-000009` and 2017
  `0000813828-18-000018`, and the ViacomCBS 10-K for 2020 `0000813828-21-000005` (discontinued-operations table). The
  2015 to 2017 figures are OIBDA less D&A and are marked ≈.
- **Not obtained:** Penguin Random House (Bertelsmann) and Hachette (Lagardère) do not file with the SEC. The national
  book-fair entrant and Usborne are private. All four are flagged and left out, not estimated.

What the row says. Scholastic's own children's-books segment, before overhead, earns trade-publisher margins in good
years (14.8% in FY2026; $143.1M on $1,052.1M of segment revenue in FY2017). The company as a whole has earned a third or
less of the competitors' margin, every year, for eighteen years. The castle, whatever it is, has not protected "excellent
returns on invested capital" **[L2007-004]**. It has not done what the rows ask of a great business, to "earn a high
return on capital employed for a very long period of time" **[M2007-023]**. The fair channel has a scale operator's
advantage. That advantage has been met by a national entrant. It sits inside a group whose clubs and Education walls are
falling and whose overhead eats most of what the fairs and the backlist earn.

**Why OUT and not TOO HARD.** The rows send a castle whose future cannot be judged to TOO HARD: "it’s just too risky. We
don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**. This verdict does not rest on a
forecast. It rests on the record: the attack happened and is reported by the filer, the clubs volume fell by five-sixths,
and the group's real revenue and returns declined over the whole span. That is a castle shown narrowing on the evidence,
which the rows put in the "out" box of "three boxes at the company: in, out, and too hard" **[M2006-013]**. The rows also
close the door a lower price might open: "What you can’t do is turn any investment into a good deal by paying little"
**[M2019-015]**; "If you really think a business is declining, most of the time you should avoid it." **[M2012-062]**.
"Leadership alone provides no certainties" **[L1996-031]**. Scholastic leads its channel and has still lost ground in it.

The strongest case for IN was put first and fairly. Fairs are at record revenue, fair count has risen three years
running, the segment margin is the decade's best, and in eight years the entrant has not displaced the leader. If the
fairs were the whole company, this would be a closer question. They are not. The castle that reaches the owner is the
group, and the group's record over the whole span is the evidence.

- **VERDICT: OUT.** The castle is shown on the filings to be narrowing (a national entrant since FY2018 taking fair count;
  clubs down 83% since FY2009; Education down 24% in two years). For eighteen years it has protected a group operating
  margin averaging 3.0%, against 9.8% and 12.7% at the two public trade publishers. The run closes here.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed OUT at Q2). The facts that bear on it are in the COMPUTATION section and carry no verdict.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template requires when the file closes before Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's three figures are in the COMPUTATION section below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. The operator did not ask, and the file is closed. For the record, children's books in schools raise nothing
on the newspaper test.

---
## COMPUTATION — NOT A CLEARANCE
*Written after the closing STOP at Q2, at the owner's request (a reporting request, not a rule change). Nothing here
clears anything, and none of it is entry language. It applies the Q7 conventions as written, so the numbers can be
compared with other runs.*

**1. Owner cash, recast for the leases.** The five-year mean as filed is $54.9M (Step 0 table). Three filing facts recast
it:
- **The real-estate tax.** FY2026 carries higher net tax payments of $41.4M "largely attributable to the gain" (10-K MD&A).
  That tax belongs to the property sale, so $8.3M is added back to the mean.
- **The tax refund.** FY2022 carries a net tax refund of $48.8M (XBRL IncomeTaxesPaidNet), a carry-back of the COVID-year
  losses. It belongs to those years, so $9.8M is taken off the mean.
- **The rent.** The sale-leaseback's full-year cost is about $30.1M pre-tax (FY2025 Adjusted EBITDA $145.4M against
  $115.3M "on a comparable basis", 8-K 2026-07-23). FY2026 had already borne about $11.0M of it. At a 25% tax rate, $20.9M
  comes off the mean.
- *(CONVENTION of this run: a 25% tax rate, the US federal 21% plus state. Rationale: FY2024's effective rate was 25.3%,
  4.1/16.2. FY2026's 33.4% is distorted by the gain.)*

| case | adjustments to the $54.9M mean | owner cash after tax |
|---|---|---|
| bottom | refund out, rent in, gain tax not added back | **$24.2M** |
| central | refund out, gain tax back, rent in | **$32.5M** |
| top | gain tax back, rent in, refund left in | **$42.3M** |

Cross-check only, not an input: the company's own FY2027 free-cash-flow outlook of $35M to $40M is before stock pay of
about $8.5M. That puts it at roughly $27M to $32M on this run's definition, inside the band.

**2. Growth shown.** Revenue from continuing operations went from $1,653.9M (FY2019) to $1,581.9M (FY2026), −0.6% a year.
FY2021 is not used as a base because it was the COVID trough: "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. The owner-cash series itself is too erratic
to fit a rate. So the "shown-growth" end is −0.6% a year, and the no-growth end is 0%. After year ten, zero nominal growth;
discount rate 5.66% throughout (the Q7 CONVENTION).

**3. Equity bridge.**
- Cash $134.9M less debt $80.5M at 2026-05-31 is +$54.4M.
- Less about $23.0M of repurchases between June and August 2026: 590,895 shares in the fiscal year to date, 289,624 of them
  from the Robinson estate at $39.7603 (8-K 2026-08-27).
- That leaves **+$31.4M net cash** at the annual measurement point.
- Film obligations of $17.1M are set against the $19.3M tax-credit receivable that secures them, and both are left out.
- The operating leases are inside owner cash (the rent is deducted), so they are not added as debt.

**4. The range** (`compute.py` in the working folder; per share on 18,409,444 shares):

| owner-cash case | no growth | shown growth (−0.6%/yr) |
|---|---|---|
| bottom $24.2M | $24.95 | $23.87 |
| **central $32.5M** | **$32.89** | **$31.45** |
| top $42.3M | $42.26 | $40.38 |

- **(a) VALUE RANGE: about $24 to $42 a share. The central case is about $31 to $33. The price is $37.41.** The top is
  1.8 times the bottom, inside the three-to-one width of the Q7 CONVENTION, and the price sits inside the range, above its
  centre. Had Q7 been reached, the convention's close would be OUT: "it’s too close to think about" **[M1996-084]**. At
  the price, the central case's pre-tax owner cash ($43.3M) is 6.6% of the enterprise value ($657M). The bottom case gives
  4.9%, the top 8.6%. All three are below the ten-percent floor CONVENTION, the speakers' "we don’t want to buy equities
  where our real expectancy is below 10 percent" **[M2003-149]**. No separable real estate is left, so no read by parts
  is needed. The 236,000 owned square feet abroad (UK, Australia) and the 22.7 acres returned in Jefferson City are
  immaterial.
- **(b) FAIR PRICE: about $25 a share ($25.24).** This is the price at or below which the central case clears the ~10%
  pre-tax floor. The tax treatment: central owner cash after tax, $32.5M, grossed up at 25% to $43.3M pre-tax. **The floor
  is applied to equity plus net debt, the enterprise value.** That gives $433M of enterprise value; adding $31.4M of net
  cash gives $465M of equity. No growth is credited, because the shown growth is negative.
- **(c) CHEAP PRICE: about $13 a share ($13.4).** *CONVENTION of this run:* the cheap price is the price at which the
  **bottom** case, pre-tax ($32.3M), earns 15% on enterprise value. At that price the floor is cleared by half again even
  if the worst of the three readings is the truth. Rationale: the rows' screamer is a case that needs no pencil, "It should scream at you." **[M2009-005]**, and a case that clears the floor only on the central reading needs one. With net cash added, $13.4 a
  share.
- The price of $37.41 is above the fair price and nearly three times the cheap price.

**5. Facts for the questions not reached, recorded without a verdict.**
- **Capital (Q3).** Consolidated operating income totalled $307.5M over FY2017 to FY2026, about $31M a year, on equity of
  $751M to $1,321M. Capital spending (PP&E plus prepublication) ran $66M to $158M a year against D&A of $47M to $66M; the
  FY2018 and FY2019 peaks were the headquarters rebuild.
- **The numbers (Q4).** The results release headlines "Adjusted EBITDA of $151.5 Million". "One-time" charges were $31.9M
  in FY2026 and $20.0M in FY2025 (8-K 2026-07-23). Severance recurs in FY2025 and FY2026 (the FY2026 MD&A reports "higher severance expense" than in FY2025). The PSUs vest
  on "annual adjusted EBITDA and Net Revenue growth goals" (DEF 14A 2026). These would have been read at Q4 against "The one figure we regard as utter nonsense is the so-called EBITDA" **[M1998-086]**, "highlighting 'adjusted per-share earnings' makes us nervous" **[L2016-006]** and "where people are talking about EBITDA, is going to be about zero" **[M2002-026]**.
- **Buybacks (Q6).** FY2025: 3,482,280 shares at an average $20.10, below the range above. FY2026: 4,502,948 shares at
  $35.96 in the open market and 2,834,018 at $40.00 in the tender, inside and above the central case. The estate sale of
  August 2026 was at $39.76. No program states a price limit. Q6's convention would read these prices against the range
  bottom of about $24.
- **Control (Q6, Part B).** The voting Class A stock (828,100 shares) elects four-fifths of the board. The Estate of
  Richard Robinson holds a majority of it, and its Class A votes are controlled by Iole Lucchese, who is Chair, an
  executive vice-president and President of Scholastic Entertainment (10-K FY2026 Item 1A; DEF 14A 2026). Common holders
  elect one-fifth of the board. The estate is selling shares "to meet certain obligations of the Estate" (8-K 2026-08-27).
- **Pay (Q6, Part B).** The chief executive's total for FY2026 was $3,742,972, a ratio of 85:1. A $1.5M special bonus pool
  rewarded the sale-leaseback; two named officers got $400,000 each (DEF 14A 2026).
- **Debt (Q9).** $80.5M at 2026-05-31 and $184.8M at the seasonal low on 2026-08-31 (10-Q). A $400M revolver matures in
  November 2029. Operating lease liabilities are $307.0M.

---
## THE BOX
**OUT, at Q2** (the castle is shown narrowing on the filings, and over eighteen years it has protected no return near its
competitors'). Q3 to Q12 were NOT REACHED. COMPUTATION only: value range about $24 to $42 (central about $31 to $33)
against $37.41; fair price about $25; cheap price about $13.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written question by question. *Not committed:* this run's instructions
      forbid commits, so the write-early commit after each question was not made, and the operator commits.
- [x] Every v5 id resolves. Checked by script against `principle_ledger_v5.csv`; every quoted fragment beside an id was
      matched in that row, with quotation-mark style normalised (two rows' inner double quotes are rendered single and
      marked). Every filing fact has its accession. No number is used without a row or a filing, except the CONVENTIONs
      of this run, which are labelled.
- [x] The order was kept. Q1 IN; Q2 OUT closed the run. Everything after it is NOT REACHED or sits under the computation heading that
      operator rule 3 prescribes.
- [x] Owner cash is after every real cost: stock pay, PP&E, prepublication and finance-lease principal. Royalty advances
      and film spending are inside OCF. No net-income proxy (operator rule 5). The sovereign is from the US Treasury. The
      aggregator price is flagged.
- [x] Contrary evidence was written down as found, "write it down in the first 30 minutes" **[M1997-127]**, six items, three of them for the business.
- [x] No row dated after the anchor is cited. This is not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used. Its capex (prepublication omitted) and its share count (one
      class) were corrected, and its v4 yield lines were ignored.
- [x] `python tools/check_framework.py` PASS (run after this file was written; result in the reply to the operator).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Two tests the brief pointed to are not in v5.** The brief referred to "Q2's tests of a distribution franchise" and
   "Q6 on controlled companies". A search of `Framework/THE FRAMEWORK v5.md` for "distribution" finds only **[L1993-021]**
   and two passing uses. A search for controlling-shareholder, dual-class and family-control language in Q6 finds none.
   So the castle tests were applied as written. The dual-class control by an estate, whose executor is also the chair and
   an executive, has no v5 test of its own. The nearest row says the cure for governance is "the very large
   shareholders" **[M2006-011]**, and here the very large shareholder is the control.
2. **No rule for a castle that is strong in one part and failing in others.** The by-parts reading is a CONVENTION written
   for holding companies at Q1. Scholastic is one operating company with a defended tower (fairs), a fallen wall (clubs),
   a weakening wall (Education) and no wall (trade hits). I judged the castle by what reaches the owner, the group's
   returns against its competitors over the whole span. That is my reading, not a rule. A second analyst could close Q2
   TOO HARD on the fairs alone, since the entrant is private and unmeasurable. I chose OUT because the verdict rests on
   the record, not on a forecast.
3. **The Q7 convention has no rule for a structural break inside the five-year window.** Here the company stopped owning
   its buildings in month seven of year five. To recast, I used the company's own "comparable basis" figure. That is a
   management-prepared adjustment, close to the projection the rows refuse, "we’ve never looked at a projection" **[M1995-050]**. I used it only for the size of
   a contracted rent, which Note 4 corroborates ($23.7M a year for the two leases, before lost rental income).
4. **The tooling.** `tools/run.py` leaves prepublication spending out of capex. For a publisher that is $18M to $38M a year
   of capital, between a third and two-thirds of PP&E spending. It also counts one share class of two. Part VII tells a v5
   run to use only run.py's arithmetic lines, but here the arithmetic lines were themselves incomplete. Every publisher run
   should be told to add the prepublication line.
5. **The template's write-early commit conflicts with this run's instruction not to commit.** I followed the instruction
   and recorded the conflict in the self-audit.
