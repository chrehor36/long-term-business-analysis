# Company Run — Tetra Tech, Inc. (Nasdaq: TTEK) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure: the lines of
evidence were derived by the analyst from the 10-K's Item 1, Item 1A and Item 7 (listed in Step 0), and the competitors
were taken from the 10-K's own list. Working folder: `Test Runs/_research 2026-10-17 TTEK/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (9a3e7cdc): not held; `PORTFOLIO.md` has no line for TTEK.*

**CONTAMINATION, declared as found (not used):** (1) the session opened with a git status and five recent commit subjects
in its context; they name another company's v5 run (CDNL), closed OUT at Q2 on its filer's own words about ease of entry.
Seen, not opened, not used; the Q2 reasoning below rests on this filer's words and these rivals' filings only. (2) Before
the first fetch the analyst ran a file-name listing of `Test Runs/` filtered for "ttek" and "tetra" to check for an earlier
run of this name; it returned nothing, and no file was opened. This is a listing the blind rule forbids, and it is declared
here as a breach. (3) The session's memory index (loaded automatically) carries queue counts and no line about this name.
(4) The analyst recalls press reports, outside the filings, of criminal pleas by former employees of the subsidiary named at
Q5's facts below; no filing read in this run states them (a search of the FY2019, FY2021 and FY2023 10-Ks for "plead" and
"guilty" found none), and they are not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $34.72 (close 2026-10-16; aggregator quote through `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: common stock, $0.01 par, 256,044,428 shares outstanding as of
  2026-07-20 (10-Q for the quarter ended 2026-06-28, filed 2026-07-31, accession `0000831641-26-000017`;
  `python Screens/cover_shares.py TTEK`). One class. Checked against the balance sheet of the same 10-Q: "issued and
  outstanding, 256,044 and 261,418 shares" (thousands) at 2026-06-28 and 2025-09-28; no treasury line (repurchased shares
  are retired through common stock and retained earnings in the equity statement). Filings after the 10-Q: the 8-K of
  2026-09-10 (`0001104659-26-106564`) announces a $500 million increase to the repurchase authorization and issues no
  shares; no prospectus or share-issuing 8-K is on the filing index after 2026-07-31. Fourth-quarter repurchases, if any,
  are not yet filed, so the count may slightly overstate the shares outstanding today.
- **Market cap:** 256.044M x $34.72 = **$8,889.8M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, 30-year par yield, US Treasury daily par yield curve, 2026-10-16
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for FY2025 (year ended 2025-09-28), filed 2025-11-20, `0000831641-25-000032`: Items 1, 1A, 5, 7, the statements,
    Notes 5, 6, 9, 18 and 19 (segments).
  - 10-Q for Q3 FY2026 (quarter ended 2026-06-28), filed 2026-07-31, `0000831641-26-000017`: MD&A, balance sheet, cash flow,
    acquisitions, debt, earn-out and subsequent-event notes.
  - Proxy (DEF 14A) filed 2026-01-09, `0001104659-26-002458`: compensation discussion, AIP table, PSU terms, summary
    compensation table, ownership table.
  - 8-Ks: 2026-09-10 `0001104659-26-106564`; 2026-07-29 `0001104659-26-088213` (exhibit 99.1, Q3 release); 2025-11-12
    `0001104659-25-110537` (exhibit 99.1, FY2025 release); 2025-12-22 `0001104659-25-123764`; 2026-01-06
    `0001104659-26-001352` (CEO succession); 2026-02-20 `0001104659-26-018205`; 2026-03-26 `0001104659-26-035179`.
  - The cycle: 10-Ks for FY2019 `0000831641-19-000193`, FY2020 `0000831641-20-000154`, FY2021 `0000831641-21-000110`,
    FY2022 `0000831641-22-000123`, FY2023 `0000831641-23-000082`, FY2024 `0000831641-24-000063` (MD&A growth statements,
    segment tables, legal note); the 10-K/A of 2023-08-15 `0001104659-23-091716` (an administrative amendment of the
    auditor's report to reference Schedule II; no change to the statements).
  - **One figure cross-checked against the filed statement:** FY2025 net cash from operating activities, $457,685 thousand
    in the filed Consolidated Statements of Cash Flows, equals the XBRL figure `tools/run.py` printed (457.7). Also: FY2025
    capital expenditures $18,633 thousand (statement) against 18.6 (tool).
- **`python tools/run.py TTEK`, arithmetic lines only** (output kept at `_research 2026-10-17 TTEK/run_py_output.txt`):
  owner cash (OCF less stock pay less capital spending) FY2023 313.0, FY2024 309.4, FY2025 405.1; the tool found finance-lease
  principal (5.6, 6.5, 7.8) outside capex and shows it as an alternate; this run deducts it. No securities lines, no PIK, no
  other stock-pay lines found. D&A FY2025 58.3 of which amortization of acquired intangibles 37.1 (10-K XBRL), so
  depreciation about 21.2 against capital spending 18.6. Stock pay resolved: $33.9M FY2025 (cash-flow statement). The
  tool's yield, growth and "points over the sovereign" lines are not used (Part VII).

**Owner cash after every real cost, by year** (USD millions; OCF less stock pay less capital spending less finance-lease
principal; from the filed cash-flow statements as tagged; working capital is inside OCF; script and output in
`_research 2026-10-17 TTEK/q7_computation.txt`):

| FY | OCF | stock pay | capex | fin. lease | **owner cash** | share of revenue | net purchases of businesses (incl. earn-outs paid in financing) |
|---|---|---|---|---|---|---|---|
| 2016 | 142.0 | 13.0 | 11.9 | 0 | **117.1** | 4.5% | 84.3 |
| 2017 | 138.0 | 13.4 | 9.7 | 0 | **114.9** | 4.2% | 9.0 |
| 2018 | 176.9 | 19.6 | 9.7 | 0 | **147.6** | 5.0% | 69.3 |
| 2019 | 208.5 | 17.6 | 16.2 | 0 | **174.7** | 5.6% | 96.2 |
| 2020 | 262.5 | 19.4 | 12.2 | 1.3 | **229.6** | 7.7% | 91.5 |
| 2021 | 304.4 | 23.1 | 8.6 | 2.7 | **270.0** | 8.4% | 104.9 |
| 2022 | 336.2 | 26.2 | 10.6 | 4.3 | **295.1** | 8.4% | 69.1 |
| 2023 | 368.5 | 28.6 | 26.9 | 5.6 | **307.4** | 6.8% | 766.3 (RPS, net of the $109.3M FX-forward settlement) |
| 2024 | 358.7 | 31.2 | 18.1 | 6.5 | **302.9** | 5.8% | 139.8 |
| 2025 | 457.7 | 33.9 | 18.6 | 7.8 | **397.4** | 7.3% | 106.1 |

Five-year average FY2021-2025: **$314.6M**. FY2025 OCF is described by the filer as raised by "timely cash collections for
work on the aforementioned disaster response in fiscal 2025 and cash collections on terminated USAID programs" and lowered
by "payments of $97 million for the aforementioned legal contingency" (10-K FY2025, Item 7). Earn-out payments classified
in operating cash (FY2024 7.9, FY2025 11.2) are left inside owner cash (conservative).

**The lines of evidence, derived from the 10-K for FY2025** (the brief's departure; each with the item it came from):
1. Item 1, Clients: the client mix and the dependence on U.S. federal agencies; USAID "accounted for 10.6%, 13.0% and 12.2%
   of our revenue in fiscal 2025, 2024 and 2023"; DoD 11.6%.
2. Item 1, Contracts: fixed-price share rising, 36.3% (FY2023) to 43.5% (FY2025); most agreements terminable by clients
   "without cause"; federal contracts terminable "at any time, with or without cause".
3. Item 1, Acquisitions: acquisitions "a key component in the execution of our growth strategy"; RPS bought for $784M in
   cash, debt-funded; CAW, SAGE (FY2025), LST, CCE (FY2024), Amyx (FY2023).
4. Item 1, Competition: "The market for our services is generally competitive"; seventeen named principal competitors.
5. Item 1A, competition risk: "the technical and professional aspects of some of our services generally do not require
   large upfront capital expenditures and provide limited barriers against new competitors"; "This competitive environment
   could force us to make price concessions or otherwise reduce prices for our services."
6. Item 1A, government funding: 46.1% of FY2025 revenue from U.S. federal, state and local agencies, much of it
   "appropriated on an annual basis".
7. Item 7, USAID: "virtually all of our contracts with USAID were terminated for convenience with immediate effect";
   USAID revenue $576.4M in FY2025 against $677.2M in FY2024; "We currently expect no significant USAID revenue in fiscal
   2026."
8. Item 7, the adjusted results: a $115.0M legal contingency charge and a $92.4M goodwill impairment excluded from
   "Adjusted income from operations" ($603.6M against GAAP $408.4M) and from adjusted EPS ($1.56 against $0.93).
9. Item 7 with Note 18: the Hunters Point False Claims Act and CERCLA matter at subsidiary Tetra Tech EC, settled for $97M,
   plus $18M estimated for ancillary claims.
10. Item 7, segments: GSG and CIG operating margins on revenue net of subcontractor costs (16.0% and 14.3% in FY2025).
11. Item 7, capital: $250.0M of repurchases at an average $34.22 in FY2025; $575M of 2.25% convertible notes due August
    2028; a secured credit agreement to 2030.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, and the quotation itself "just tells us prices" **[M2006-077]**. The foundation that bears hardest on this
name is who is paid to tell you: the filer's releases lead with "Record" figures, "EBITDA" and adjusted earnings, and the
filer's own description of its competitive position is the advocate's, so the castle is read from the rivals' filings as
well as its own; one does not get "impartial advice" where the fees run one way **[M2020-037]**. The analyst's habit is to
look for "what’s wrong in things" **[M2025-013]** and to use the rivals' record "to possibly reject your original
hypothesis" **[M1998-144]**. No macro view enters. **Contrary evidence, written down as found** **[M1997-127]**: (a) the
filer's own Item 1A says its services "provide limited barriers against new competitors"; (b) its largest client group
cancelled about an eighth of revenue in weeks (USAID); (c) the two largest named rivals now report margins and returns on
capital at or above the filer's (Q2 below); (d) the executives' FY2025 bonus was computed on an operating income that
excludes the $115M legal settlement (proxy, Q5 facts below); (e) in the filer's favour: ten years of returns on capital
above all three rivals and operating income nearly held in FY2026 through the USAID loss.

## THE STANDING RULE
A part-interest bought for cash in the market, unlevered, at a size the buyer can hold through a fall of half: nothing in
the purchase itself risks "what we have and need" **[M2012-081]** or a "permanent loss of capital" through the buyer's own
conduct **[L2023-005]**. The rule binds the buyer's financing and sizing, which this run does not set; no breach in the
purchase as described.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
- **The key variables** **[M1998-044]**: (1) the volume of paid engineering and consulting hours that water, environment
  and infrastructure clients buy; (2) the spread between billing rates and labour cost, which the filer says turns on
  "billable headcount and cost control" for time-and-materials work and on estimates for the rising fixed-price share
  (Item 1, Contracts); (3) the client mix, above all U.S. federal agencies whose funding is "appropriated on an annual
  basis" (Item 1A); (4) the price paid for acquisitions, which supplied most of the decade's growth (Item 1, Acquisitions).
- **Are they foreseeable?** Variables (1), (2) and (4) are the economics of a professional-services firm and can be read in
  the filings: net revenue, segment margins, cash conversion, the purchases and what they earned. The business has no fast
  technology cycle of its own; it sells hours of qualified people. Variable (3) is not foreseeable as to any one agency (the
  USAID termination took about an eighth of revenue in FY2025-26), but it is a question about how lasting the client
  relationships are, which is Q2's question, not a question whether the economics can be pictured at all. The past
  statements do tell what the future statements will look like in kind **[M2008-033]**: a labour business whose cash follows
  its operating income, with almost no capital spending.
- **Insiders would write it down?** **[M2000-105]** An engineering consultancy's ten-year plan is written down in this
  industry as a matter of course (backlog, recompetes, utilization); the forecast is not one the insiders would call "too
  hard".
- **Change.** The filer describes AI-enabled tools as part of its service ("AI-enabled solutions for asset management",
  Item 1). Whether software compresses the billable hours of studies and design over ten years is a real question; it is a
  threat to the castle, owned by Q2 **[M1999-063]**, and not a change so fast that the economics cannot be pictured. The
  forecast is about customers (water utilities, agencies, industrial owners) more than about technology **[M2017-019]**.
- **Doubt.** The analyst's doubt is about how long the castle stands, not about what the business is or how it earns; "if
  you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]** is applied, and the doubt
  found is Q2's, not Q1's.
- **VERDICT: IN, narrowly.** The economics of a labour-based engineering consultancy can be pictured ten years out from its
  filings (10-K FY2025 `0000831641-25-000032`, Items 1 and 7); what cannot be pictured as easily is whether its edge over
  rivals lasts, which is the next question **[M2012-065]**, **[M2006-076]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A moat is what "protects
excellent returns on invested capital" against competitors who "will repeatedly assault" it **[L2007-004]**.

**The parts table** (segment operating income as filed: FY2021-FY2022 from the FY2022 10-K `0000831641-22-000123`, Note on
reportable segments; FY2023-FY2025 from the FY2025 10-K `0000831641-25-000032`, Note 19; USD millions; segment operating
income is before acquisition amortization and corporate costs):

| part | FY21 | FY22 | FY23 | FY24 | FY25 | five-year total | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| CIG (U.S. commercial and international) | 152.3 | 194.1 | 243.8 | 328.5 | 356.9 | 1,275.6 | **51.0%** | open (below) | **yes (more than half)** |
| GSG (U.S. government and development agencies) | 174.8 | 198.4 | 231.8 | 281.0 | 340.6 | 1,226.6 | 49.0% | open (below) | no |

The file closes on CIG (the business-of-parts CONVENTION of Q2, section B). The parts are near-equal; GSG is read as well,
because the filer's company-wide statements (Item 1A) cover both and because the verdict would not change on GSG's
evidence (GSG carried the USAID loss). Beginning in FY2026 the filer moved units between the segments (10-Q Q3 FY2026);
the as-filed table governs.

**The castle tests, each with its filing fact.**
1. **The key factors and how permanent** **[M1995-038]**. The filer names its own: "a long track record of successful
   performance that results in repeat business and limits competition"; "Institutional knowledge is often a significant
   factor in winning competitive proposals"; "Our people are our number one asset"; and a toolset, "Tetra Tech Delta"
   (10-K FY2025, Item 1). Each is real and none is permanent in the rows' sense: relationships and knowledge are held by
   some 25,000 staff whom rivals can hire, and the toolset is software of a kind rivals also build. The MD&A explains the
   margin gains as "improved project execution including higher labor utilization" (GSG) and "our continued focus on
   high-end consulting services and improved project execution" (CIG): execution, which must be won again each year.
2. **Would it stand without the lord?** It does not depend on one person: the chief executive of twenty years handed over to
   a thirty-year insider on 2026-02-19 (8-K `0001104659-26-001352`). Passed.
3. **The money test** **[M2011-015]**, **[M2012-106]**. The filer answers it in its own risk factors: "We are engaged in a
   highly competitive business. The markets that we serve are highly fragmented and we compete with many regional, national
   and international companies. Certain of these competitors have greater financial and other resources than we do", and
   "the technical and professional aspects of some of our services generally do not require large upfront capital
   expenditures and provide limited barriers against new competitors" (Item 1A). Its own history shows how money buys
   position in this field: RPS was bought for $784 million in cash and became most of CIG's growth (Item 1). The rows'
   failing answer is this one: "there are some industries that are just never going to have barriers to entry. And in those
   industries, you better be running very fast" **[M2012-106]**. Failed.
4. **Pricing power and the agony before a rise** **[M2005-020]**. "This competitive environment could force us to make
   price concessions or otherwise reduce prices for our services" (Item 1A). On federal work the customer sets what is
   recoverable: "only those costs that are reasonable, allocable and allowable are recoverable", audited by the DCAA
   (Item 1). The filer's inflation statement rests on "our ability to negotiate prices as contracts end and new contracts
   begin" (Item 7), the ordinary repricing of a labour contract. No evidence of power to raise price. Failed.
5. **Unit volume and share of mind.** Backlog $4.1 billion at FY2025 year-end, $4.49 billion at 2026-06-28 (10-K Item 1;
   8-K exhibit 99.1 of 2026-07-29). The filer cites ENR ("#1 in Water Treatment and Desalination for 12 years in a row"); its
   largest rival's FY2025 10-K (`0000868857-25-000013`, Item 1) says AECOM is "the number one ranked water, transportation
   design, facilities design, environmental engineering, environmental consulting and environmental science firm in the
   world". A ranking two rivals both claim is not a place in the customer's mind that a rival cannot take.
6. **The low-cost position.** No filing fact shows the filer as the low-cost producer; its costs are engineers' salaries
   paid at the market, and it gives none of its costs against rivals'. Not shown.
7. **The brand in the customer's mind.** Clients "make competitive determinations based upon qualifications, experience,
   performance, reputation, technology, customer relationships and ability to provide the relevant services in a timely,
   safe and cost-efficient manner" (Item 1A). Reputation counts, among six other grounds, bid by bid.
8. **Would the customer still choose it over the low bid?** **[M2017-009]** In part: clients weigh "the quality, innovation
   and timeliness of the firm's service versus its cost to determine which firm offers the best value" (Item 1). This is not
   the pure low bid **[L2004-003]**; nor is it a customer who asks for the firm by name, since "Our failure to win new
   contracts and renew existing contracts" is a stated risk and "re-competes of government contracts" a stated factor
   (Item 1A).
9. **Ask the competitors.** No scuttlebutt in a blind run; their filings speak for them in the row below.
10. **Widening or narrowing?** **[M1999-108]**, **[L2005-010]**, **[M2000-075]**. Against itself, widening: operating
    income over revenue rose from 5.3% (FY2016) to 9.6% (FY2024), 7.5% in FY2025 after the two charges. Against the rivals,
    narrowing: the two largest named rivals reorganised into the same professional-services mix (AECOM sold its Management
    Services segment and its "self-perform at-risk civil infrastructure and power construction" businesses, its 10-K Item 1;
    Jacobs separated its Critical Mission Solutions and Cyber and Intelligence businesses on 2024-09-27, its 10-K
    `0001628280-25-053316`, Item 1), and by FY2024-FY2025 they report pre-tax returns on capital at or above the filer's
    (row below). The decade's lead was matched within two years by rivals who adopted the same mix.
11. **What could destroy, modify or reduce it** **[M2000-014]**. Shown in FY2025, not hypothesised: the U.S. government
    terminated "virtually all of our contracts with USAID" "for convenience with immediate effect" (Item 7); USAID was 13.0%
    of FY2024 revenue, and federal revenue fell 32.5% in the first nine months of FY2026 (10-Q `0000831641-26-000017`). Any
    client may leave: "Most of our agreements permit our clients to terminate the agreements without cause upon payment of
    fees and expenses through the date of the termination" (Item 1). Also open: whether software compresses the billable
    hours of studies and design.

**The competitor row** (same metrics from the rivals' own filings; XBRL figures as first filed for each year; operating
income over revenue, and pre-tax operating income over equity plus net debt, which includes the goodwill each firm paid for
its acquisitions; inputs and arithmetic in `_research 2026-10-17 TTEK/field2.py` and `field_returns.txt`). Rivals named by
the 10-K (Item 1, Competition) that file with the SEC and are closest to the deciding part (engineering, water and
environment, commercial and international): **AECOM**, **Jacobs Solutions**, **Stantec** (Form 40-F, IFRS, Canadian dollars,
December year-ends; operating income taken as profit before tax plus net interest expense). The other SEC filers named
(Booz Allen Hamilton, Exponent, ICF International, Leidos, SAIC) compete with parts of GSG's government IT and advisory
work and were not taken (the brief's limit of three). **Named rivals that do not file with the SEC, flagged:** Arcadis NV,
AtkinsRéalis, Black & Veatch, Brown & Caldwell, CDM Smith, GHD, TRC Companies, Weston Solutions, WSP Global (none appears
in the SEC's company ticker list, `www.sec.gov/files/company_tickers.json`, fetched 2026-10-17).

| firm (filing) | OI / revenue, FY2016-2025 | pre-tax OI / (equity + net debt), 10 yrs | first five | last five | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Tetra Tech (10-Ks FY2016-FY2025; latest `0000831641-25-000032`) | 7.8% | 18.9% | 17.0% | 20.0% | 20.8% | 17.2% |
| AECOM (10-Ks; latest `0000868857-25-000013`) | 3.3% | 10.8% | 6.0% | 19.3% | 25.0% | 26.9% |
| Jacobs (10-Ks; latest `0001628280-25-053316`) | 5.0% | 10.4% | 8.3% | 12.1% | 12.3% | 18.6% |
| Stantec (40-Fs; latest `0001131383-26-000007`) | 6.9% | 12.3% | 10.7% | 13.4% | 13.9% | 15.7% |

Read with care: revenue bases differ (all four book pass-through subcontract costs in revenue, in different shares, so the
margin column compares mix as much as skill); the capital measure includes goodwill paid, the measure the rows use for
judging capital allocation; on tangible capital alone all four firms run near zero or below (`field_returns.txt`), so the
return on tangible assets **[M2011-060]** is very high for every one of them and does not separate them. That is itself a
finding: the field's economics are those of labour businesses that need little capital, which is why entry is cheap.

**The field's returns over the last full cycle, judged in words.** Over FY2016-FY2025, a span that holds the 2016
commodity downturn, the 2020 pandemic year and the 2025 federal cuts, the filer earned clearly better returns than each
rival, and the rivals earned ordinary returns on what they had paid for their businesses until they shed their construction
and government units. The field is not shown to be one of ordinary returns throughout, so the "ordinary returns" OUT does
not decide this file, and the filer's decade-long lead is real. The question the rows put is what protects it, and the
filer's own answer is execution in a fragmented field with "limited barriers against new competitors".

**Why the box is OUT and not TOO HARD.** The rows send a castle shown to be open to OUT **[M2011-015]** and a castle
whose future cannot be judged to TOO HARD **[M2000-019]**, **[M2006-013]**. The evidence here is not silence about the
future; it is three filed facts that show the walls down: the filer states its own barriers are limited and that
competition can force price concessions (tests 3 and 4); its largest client group removed an eighth of its revenue at will
(test 11); and the rivals' filings show the decade's return lead matched within two years once they adopted the same mix
(test 10). The advantage is real and it is the advantage of running fast: "a lot of other people that are going to be
running and looking at what you’re doing" **[M2012-106]**; "A moat that must be continuously rebuilt will eventually be no
moat at all" **[L2007-005]**; "for every Inevitable, there are dozens of Impostors, companies now riding high but vulnerable
to competitive attacks" **[L1996-031]**. In fairness, the rows also say "The service businesses are generally the better
businesses. They require less capital" **[M2009-047]**: that is the Q3 virtue this business has in full (facts below), and
it is the reason entry is cheap, not a wall. A second analyst could weigh the decade's lead more heavily and close TOO HARD
on whether an execution edge lasts; the text does not draw that line (see the last section).

Price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The deciding part (CIG, 51.0% of five-year segment operating income) and the company as a whole sell
  qualified hours in a field the filer calls highly fragmented with "limited barriers against new competitors" (10-K FY2025
  `0000831641-25-000032`, Item 1A), where competition can force price concessions and the largest rivals have matched its
  returns once they adopted its mix (AECOM `0000868857-25-000013`, Jacobs `0001628280-25-053316`) **[M2012-106]**,
  **[M1995-038]**, **[L2007-004]**, **[M2011-015]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten balance sheets were read in Step 0 and Q2's work (as the template asks when the file closes before
Q4); what they show is under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found before the stop are recorded under AFTER THE STOP and flagged in the box line.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP, including the buyback prices against the bottom of the COMPUTATION range.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE (operator
rule 3; Part VII, The owner's price).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. One fact under AFTER THE STOP.

---
## COMPUTATION, NOT A CLEARANCE: the value range and the fair price (reporting figures at the owner's request)
*Arithmetic after a closing STOP. Not a clearance, not a verdict, no entry language (operator rules 2 and 3). The
construction is Q7's range convention as the text states it; script and full output in
`_research 2026-10-17 TTEK/val2.py` and `q7_computation.txt`.*

**Inputs.**
- **Owner cash after every real cost**, five-year average FY2021-FY2025: **$314.6M** (the Step 0 table: OCF less stock pay,
  capital spending and finance-lease principal; after the company's own cash taxes; working capital inside OCF, specific
  (d)). The $97M of Hunters Point settlement payments in FY2025 OCF is left in, as a real cost.
- **All-equity basis** (Q7, On what the floor is earned): owner cash before interest, adding back cash interest paid after
  tax at the FY2025 effective rate the filer gives excluding items, 27.4% (10-K Item 7): average interest paid FY2021-2025
  $28.6M, after tax **$20.8M**; unlevered base **$335.3M**.
- **Net debt** at the latest filed balance sheet (10-Q, 2026-06-28): credit facilities $235.0M plus convertible notes
  $575.0M at face (carried at $801.1M net of $8.9M of issuance costs) less cash $230.8M, plus the subsequent event the
  filing states (a dividend of $0.072 a share declared 2026-07-27, $18.4M) = **$597.6M**. Finance leases are "immaterial"
  (10-Q lease note) and left out; operating leases left out, said so; contingent earn-out liabilities of $113.8M (10-Q)
  are left out of net debt and stated here beside it.
- **Rate:** 5.43%, the 30-year Treasury par yield of 2026-10-16. **Shares:** 256.044M. **Price:** $34.72.

**The specifics applied.**
- **The serial acquirer (specific (c), 2026-10-12).** Net purchases of businesses FY2021-FY2025, including earn-outs paid in
  financing and net of the $109.3M FX-forward settlement on RPS and of divestiture receipts: **$1,186.2M**, against half of
  owner cash before purchases, $786.4M. Purchases exceed half, so **the central figure is the organic pair**: purchases left
  out, organic growth as the filer reports it. The default pair is shown beside.
- **Organic growth as the filer reports it:** revenue excluding acquisitions grew 4.1% (FY2022, 10-K FY2023 Item 7), 12.0%
  excluding RPS (FY2023, 10-K FY2023), 7.6% (FY2024, 10-K FY2024), 3.2% (FY2025, 10-K FY2025): compound **6.67%** a year
  over the four steps of the window. The filer states no organic figure for FY2021.
- **(a) An aberrational end year.** FY2025 is aberrational on the filer's own description (disaster-response peak,
  collections on terminated USAID programs, the $97M settlement paid). No full cycle can be found in owner cash: the series
  rises in seven of the nine year-to-year steps of FY2016-FY2025, with two small dips (FY2017, FY2024) and no trough-to-trough shape (Step 0 table), so no peak-to-peak or trough-to-trough
  base exists to substitute; the five-year average is used, and the four-year average without FY2025 is shown beside.
- **(b) Decline.** None inside the window. After it: revenue fell 9.1% in the first nine months of FY2026 with about $180M
  from acquisitions inside it, an organic fall of about 13% by the analyst's arithmetic (10-Q Item 2), almost all of it the
  USAID loss. A variant carrying that fall through the growth rate is shown beside (2.30% a year over FY2022 to the FY2026
  nine-month figure).
- **(c) Deals after the window.** Halvik and Providence (FY2026, about $232M of purchase price including $39M of earn-out
  fair value, 10-Q acquisitions note) closed before the price date: their cash is already out of the June 2026 balance sheet and so
  inside net debt, and no earnings of theirs are filed, so they are credited at nothing.
- **(e) Maintenance.** The filing does not separate maintenance from growth spending; capital spending ($18.6M FY2025) is
  below depreciation (about $21.2M), so the all-spending case and a maintenance case coincide in substance; all spending is
  deducted.
- **(f) The cap.** At 6.67% for ten years, owner cash would be 6.2% of revenue grown at the same rate, below the highest
  share the filings show (8.4%, FY2021-FY2022): no cut. The total-growth rate of the default pair (10.15%) is below the
  revenue growth of the window (14.08%): no cut.
- **No real growth after year ten** is taken as zero nominal growth; the floor tested first.

**The range (central: organic pair, all-equity basis, per share):**

| case | base | growth, years 1-10 | value a share | expected return at $34.72 |
|---|---|---|---|---|
| no growth (bottom) | $335.3M | 0% | **$21.78** | 3.53% |
| organic growth as reported (top) | $335.3M | 6.67% | **$38.75** | 5.96% |

**Value range $21.78 to $38.75 a share against $34.72.** Width 1.78 to 1. **The floor, tested first:** no case in the range
earns about ten percent at the price; the best case returns 5.96% a year. Had Q7 been reached, the file would close OUT by
the floor (the floor convention, "there’s just a point at which we drop out of the game" **[M2003-149]**).

Shown beside, none deciding: equity-only (owner cash after interest against the market value) $22.63 to $38.54; organic
variant with the FY2026 decline carried, $26.65 at the top; the four-year base without FY2025, $20.29 at no growth; the
default pair (purchases deducted, total owner-cash growth of 10.15% credited, purchases stopping after year ten as specific
(c) says) $14.78 to $39.93, and with purchases continuing after year ten $4.72 to $13.50.

**FAIR PRICE (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent instead of the long
rate, the two averaged: no-growth end $10.76, organic-growth end $18.40, **fair price $14.58 a share on the all-equity
basis** (after the company's own tax; net debt $597.6M deducted), with **$15.87 on the equity-only basis** beside it. On the
default pair with purchases stopping after year ten the figure would be $9.94. No cheap price is reported.

---
## THE BOX
**OUT at Q2** (the castle is open on the filer's own words, "limited barriers against new competitors" in a "highly
fragmented" field where competition "could force us to make price concessions", and on the rivals' filings, AECOM and
Jacobs matching its returns once they adopted its mix); **integrity facts recorded, not judged**. COMPUTATION, NOT A
CLEARANCE: value range $21.78 to $38.75 a share (all-equity, organic pair) against $34.72; no case earns the floor (best
5.96%); fair price $14.58 all-equity ($15.87 equity-only). Q11 belongs to a holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on later questions, each with its source; written down, not weighed; no verdict; the box
unchanged (operator rule 2) **[M1997-127]**.*

**Bearing on Q3 (capital).**
- Capital spending $18.6M in FY2025 on $5,442.6M of revenue; depreciation about $21.2M (D&A $58.3M less amortization of
  acquired intangibles $37.1M), 10-K FY2025 cash-flow statement and XBRL.
- Tangible capital employed (equity plus net debt less goodwill and intangibles) about $205M at FY2025 year-end against
  segment operating income of $697.4M (`field_returns.txt`; 10-K Note 19). The business needs almost no tangible capital;
  customer prepayments ("Contract liabilities" $420.3M) finance much of its working capital (10-K balance sheet).
- Growth was bought: goodwill $1,108.6M (FY2021) to $2,216.3M (2026-06-28) (10-Ks; 10-Q). Over FY2021-FY2025 owner cash
  rose $127.4M a year (from $270.0M to $397.4M) while $1,186.2M was spent on businesses net, before crediting any organic
  growth to the existing business (Step 0 table; analyst's arithmetic).

**Bearing on Q4 (the accounts), the balance sheets FY2016-FY2025 read first** (run.py transcription, checked against the
filed FY2025 and FY2022 balance sheets):
- Equity $869M to $1,780M; goodwill $718M to $2,050M, above equity since FY2023, so tangible equity is below zero
  (FY2025: $1,780M less goodwill $2,050M less intangibles $121M).
- Receivables $714M to $1,159M against revenue $2,584M to $5,443M: 27.6% of revenue to 21.3%, falling; the Q3 FY2026
  release states DSO of 56 days. Contract assets $143M (FY2018) to $138M (FY2025), flat while revenue nearly doubled. No
  prepaid or deferred account building (prepaid and other current assets $98.8M at FY2025, $120.4M at 2026-06-28).
- Debt $332M (FY2016) to $880M (FY2023, after RPS) to $763M (FY2025); cash $121M to $233M through the decade.
- Retained earnings $736M to $1,873M while $1,001.7M of stock was repurchased over FY2016-FY2025 (XBRL repurchase series).
- What the figures cannot say: the worth of the staff who are the business, and how much of the goodwill paid buys
  anything a rival could not hire away.
- Recurring "non-recurring" items: goodwill impairments in FY2015 ($58.1M), FY2019 ($7.8M), FY2020 ($15.8M), FY2025
  ($92.4M); contingent-consideration fair-value adjustments every year; a right-of-use lease impairment ($16.4M, FY2023);
  the $115.0M legal charge (FY2025). (XBRL; 10-K FY2025 statements.)
- In the filer's own mouth: the Q3 FY2026 release's headline bullets read "Operating Income $158 million; EBITDA $173
  million" and "YTD performance drives increased FY26 guidance"; the FY2025 release leads with "Record Adjusted Annual EPS
  $1.56" against GAAP EPS of $0.93 (8-Ks `0001104659-26-088213` and `0001104659-25-110537`, exhibit 99.1). Fiscal 2026
  adjusted EPS guidance was raised to $1.56-$1.59.
- The accounts themselves were not found confusing: segment, acquisition, debt and legal notes reconcile to the statements.

**Bearing on Q5 (integrity): the integrity facts, recorded, not judged.**
- **Hunters Point.** In 2019 the U.S. Attorney's Office intervened in three qui tam actions against subsidiary Tetra Tech EC
  alleging False Claims Act violations in "contracts to perform environmental remediation services at the former Hunters
  Point Naval Shipyard"; CERCLA claims were added in 2024. From the FY2019 to the FY2023 10-K the filer wrote "TtEC disputes
  the claims and will defend this matter vigorously". On 2025-01-17 TtEC settled for $57M (FCA) and $40M (CERCLA), "no
  admission of liability"; $18M more was reserved for ancillary private claims, still pending; TtEC is suing its insurer to
  recover part (10-K FY2025 Note 18; 10-K FY2019 `0000831641-19-000193`).
- **The settlement waved away in the featured figures.** The $115.0M charge was called "non-recurring" and excluded from
  adjusted operating income and adjusted EPS (10-K FY2025 Item 7).
- **The same adjusted figures pay the executives.** The proxy's AIP table shows Corporate operating income "Actual" of
  $603,607 thousand, which equals the adjusted operating income that excludes the legal charge and the impairment, and
  Corporate cash flow "Actual" of $554,685 thousand, which equals reported OCF of $457,685 thousand plus $97,000 thousand
  (the analyst's arithmetic: the settlement payments added back). The table's footnote lists the Corporate exclusions as
  "acquisition related charges, non-core disposition related charges, and one-time, non-recurring tax adjustments"; it does
  not name the legal charge (DEF 14A `0001104659-26-002458`, AIP Award Program Financial Metrics). PSUs vest 50% on adjusted
  EPS growth, whose stated adjustments include goodwill impairment.
- **A discretionary bonus that year.** "a special one-time incentive payment of $50,000 to several senior executives,
  including the NEOs (but excluding the CEO)", for "the level of additional work required to achieve record results"
  (DEF 14A).
- **Pay against ownership.** CEO total compensation $11.62M (FY2025), $12.56M (FY2024), $11.89M (FY2023); CEO beneficial
  ownership 332,630 shares at 2025-12-23, about $11.5M at $34.72; directors and executive officers as a group 1,271,572
  shares, under 1% (DEF 14A).
- **Guidance given and raised;** EBITDA in the headline (Q4 facts above).
- Carried by the template's own rule to any later run that reaches Q5: these must be answered there **[M2013-088]**.

**Bearing on Q6 (the money and the owners).**
- Repurchases: $250.0M at an average $34.22 in FY2025; $200.0M at an average $31.29 in the first nine months of FY2026;
  none in FY2023-FY2024; a further $500M authorized 2026-09-10 (10-K Item 7; 10-Q Note 7; 8-K `0001104659-26-106564`). No
  price above which buying stops is stated in the filings read. Against the COMPUTATION range: every average price paid
  ($34.22, $31.29) sits above its bottom ($21.78 all-equity, organic pair).
- Dividends: $65.0M in FY2025; the release counts a "45th consecutive double-digit increase" (8-K of 2026-07-29).
- Acquisitions with earn-outs: $113.8M of contingent liabilities at 2026-06-28, maximum potential $215.4M (10-Q).
- $575M of 2.25% convertible notes due 2028-08-15, conversion price about $39.31, with capped calls bought for $51.8M at
  issue (10-Q Note 13).
- Succession: Roger R. Argus succeeded Dan L. Batrack as CEO on 2026-02-19; Mr. Batrack continues as Executive Chairman,
  "expected" to serve "for a minimum of two years" (8-K `0001104659-26-001352`). Three directors added December 2025 to
  March 2026, two of them former water-utility chief executives (8-Ks of 2025-12-22 and 2026-03-26).

**Bearing on Q9 (debt and exposures).**
- Borrowings $810M at face against cash $230.8M at 2026-06-28; the credit agreement is "senior secured" by liens on
  receivables and subsidiary equity, matures May 2030; covenant leverage 1.13x and interest coverage 17.31x at FY2025 as the
  agreement defines them (EBITDA-based); pre-tax income over interest expense FY2025, $377.6M over $40.6M, 9.3 times
  (10-K Item 7, Note 19). The $575M convertible notes mature in August 2028 and must then be paid in cash up to principal.
- Every client may terminate without cause; federal funding is appropriated yearly; 43.5% of FY2025 revenue was fixed-price
  (10-K Item 1). Professional liability claims "seeking damages that exceed our insurance coverage" exist (Note 18).

**Bearing on Q12.** The Hunters Point matter concerns the remediation of a contaminated naval shipyard; recorded under Q5.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      template copy `5903fa05`, Step 0 to Q1 `8c4f6875`, Q2 `a1b14934`, the rest in the closing commit.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session; the run is folded into the register before the dispatcher moves on (operator rule ten). A run not in the
      register binds nothing. (Lock and fold are the dispatcher's; not checked by the analyst.)
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule): **breach
      declared** at the top: one name-filtered listing of `Test Runs/` before the first fetch (no match, nothing opened);
      commit subjects of another run seen in the session's opening context (not used).
- [x] Every v5 id resolves (`_research 2026-10-17 TTEK/check_ids.py`, run before the closing commit); every filing fact has
      its accession; no number without a row or a filing. Figures marked "the analyst's arithmetic" are sums of filed
      figures.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance; the valuation is
      headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (US Treasury); the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations line, written before Q2 closed);
      the facts found for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; all rows cited
      are dated 2025 or earlier.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the closing commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2, OUT against TOO HARD for an execution edge.** The filer's returns led all three rivals for ten years while its own
risk factors admit "limited barriers against new competitors". The text sends a castle "shown to be open" to OUT and a
castle "whose future cannot be judged" to TOO HARD, and puts the continuously rebuilt moat on the OUT list only "where the
evidence shows the rebuilding failing". Here the rebuilding was succeeding until the rivals caught up in FY2024-FY2025.
The run closed OUT on the filer's own words plus the rivals' convergence; a second analyst weighting the decade's lead
could close TOO HARD (WORK, on whether the lead held through FY2006-FY2015) and the text does not say which reading
governs. (2) **Q2's measure for a labour business.** The rows' measure, "return on tangible assets" **[M2011-060]**, is unbounded for every firm
in this field (tangible capital near zero or negative), so it cannot separate them; the run used pre-tax return on equity
plus net debt, which includes goodwill paid, and said so. The text gives no measure for a business whose capital is its
people. (3) **Q7 specific (a) with no cycle.** The last window year is aberrational on the filer's own words, but owner
cash shows no cycle in ten years, so the cycle base cannot be built; the text does not say what replaces it. The run kept
the five-year average and showed the four-year average beside. (4) **A known decline after the window.** The filer's FY2026
organic fall (about 13%, the USAID loss) is after the window; specific (b) speaks only of decline shown inside it. The run
kept the window's organic rate central and showed the post-window variant beside. (5) **"Organic growth as the filer
reports it"** is reported in revenue, not owner cash, and for four of the five years only; the run applied the revenue rate
to owner cash. (6) **Net debt and contingent consideration.** The definition (borrowings and finance leases less cash) is
silent on earn-out liabilities ($113.8M here, payable in cash on operating-income targets) and on convertible notes'
conversion; the run left earn-outs out and said so. (7) **The default pair's buy-stop at no growth** produces a no-growth
case that spends ten years of purchase money for no growth; the text's mechanics were followed and the oddity is reported.
(8) **EBITDA in the release headline.** Q4's list of what it rules OUT names EBITDA talk, on the row "where people are talking about EBITDA, is going to be about zero" **[M2002-026]**, while
the 2026-10-06 convention limits Q4's STOP to the accounts and carries press-release habits to Q5; where EBITDA in a
headline lands is not stated. Recorded after the stop.
