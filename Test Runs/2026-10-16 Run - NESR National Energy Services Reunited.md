# Company Run — National Energy Services Reunited Corp. (Nasdaq: NESR) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-16, after the run was committed: not held (`PORTFOLIO.md` carries no line for
NESR or National Energy Services).*

**Dispatched run.** Written by a dispatched analyst under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the
two departures the brief states (lines of evidence derived by the analyst from the filings; competitors chosen as a
CONVENTION of the run where the 10-K names none). The lock file in `Screens/_daily/` was present when this run started
(seen in a directory listing, held by the dispatching session; not opened).

**Contamination, declared and not used.** (1) A listing of `Test Runs/`, made only to confirm this run's file name was free,
showed six other run files and research folders dated 2026-10-16 (HMH, NGS, NOV, OIS, SEI, USAC); none was opened. (2) The
session context carried recent commit subjects about the SEI run and its fold, and memory-index lines about the queue's
state. (3) Nothing about NESR from any other file was seen. None of this bears on the judgments below.

**Lines of evidence chosen, and from which items** (the brief's departure (1)): from the FY2025 10-K Item 1 (the two
segments, the customers and their concentration, the competition paragraph, capital spending) and Item 1A (customer
spending and cancellable contracts, concentration in a few NOC customers, larger competitors, equipment capital needs,
the restatement and SEC matters); from Item 7 (segment results and their explanations, cost of services, liquidity) and
Item 9A (the material weakness and its remediation); the same items of the 20-Fs for FY2018 to FY2024, read for the
recurring explanations ("transition between hydraulic fracturing contracts in Saudi Arabia"), the 2020 restatement (FY2022
20-F, Note 4 and Item 16F) and the SEC settlement (FY2024 20-F); the 10-Qs of 2026 for the latest balance sheet and the
payables; the 8-K of 2026-08-10 on the auditor; the DEF 14A for pay and ownership.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $19.11 (close 2026-10-15; aggregator quote via `tools/run.py`, flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: 100,851,754 ordinary shares, one class (10-Q for the period ended
  2026-06-30, filed 2026-08-10, accession `0001493152-26-036720`; `python Screens/cover_shares.py NESR`). Checked: the
  balance sheet of the same 10-Q carries the same count, issued equals outstanding (no treasury shares, BVI no-par shares);
  the DEF 14A gives 100,797,004 at the record date 2026-03-10 and the FY2025 10-K 100,787,173 at 2025-12-31; no 8-K or
  prospectus after the 10-Q issues shares (the 8-Ks of 2026-08-10 are earnings and the auditor; none later on EDGAR's list).
  The warrants were exchanged in July 2025 (FY2025 10-K, Note 15: 34,136,353 warrants tendered for 3,413,645 shares).
- **Market cap:** $1,927M (100.852M × $19.11).
- **Sovereign for the earnings currency:** USD 30-year par yield 5.43% (US Treasury daily par yield curve, 2026-10-15, as
  fetched by `tools/run.py` from `tools/sources.py`). The earnings currency is USD (the XBRL unit and the reporting
  currency; the Gulf currencies are pegged, the filing's market-risk item says its exposure is weighted to the dollar).
- **Filings read** (operator rule 4): FY2025 10-K filed 2026-03-06, accession `0001493152-26-009139` (Items 1, 1A, 7, 8,
  9A); 20-F FY2024 `0001641172-25-001136`; 20-F FY2023 `0001493152-24-017128`; 20-F FY2022 (filed 2023-12-29)
  `0001493152-23-046470` (restatement note, Item 16F); 20-F FY2020 `0001493152-21-006706`; 20-F FY2019
  `0001493152-20-004179`; 20-F FY2018 `0001493152-19-003164`; 10-Q Q1 2026 `0001493152-26-022091`; 10-Q Q2 2026
  `0001493152-26-036720`; DEF 14A filed 2026-03-24 `0001493152-26-012394`; 8-Ks of 2026-02-17 `0001493152-26-006872`,
  2026-05-14 `0001493152-26-022961`, 2026-07-21 `0001493152-26-034075`, 2026-08-10 `0001493152-26-036718` and
  `0001493152-26-036716` (auditor). No 20-F for FY2021 was filed alone: FY2021 is presented in the FY2022 and FY2023
  20-Fs (an NT 20-F of 2022-05-03, `0001493152-22-011873`, is on the list).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $264,242
  thousand on the filed statement of cash flows (10-K page 62) against 264.2 in the tagged series of `tools/run.py`;
  capital expenditures $143,454 thousand against the Item 1 sentence "$143.5 million during the year ended December 31,
  2025" and the tagged 143.5. They agree.
- `python tools/run.py NESR`, arithmetic lines only (its v4 lines, its three-year "owner earnings" mean, yield and points
  over the sovereign are not used, Part VII): OCF 177.0 / 229.3 / 264.2 (2023 to 2025), SBC 6.8 / 6.0 / 8.3, D&A 142.2 /
  142.8 / 141.7, capex 68.2 / 105.1 / 143.5, finance-lease principal 2.4 / 3.2 / 3.9; the ten-year balance-sheet table and
  the debt lines on the face (used at Q4 below, after the stop). The tool does not see the "payments on seller-provided
  financing for capital expenditures" in the financing section (15.3 / 14.4 / 15.6 / 3.8 / 7.4 for 2021 to 2025) nor the
  IPM investments (17.4 in 2022, 16.0 in 2023); both are capital spending and are read from the filed statements below.
  Owner cash after every real cost, by year, is built in the research folder (`compute.py`, from the filed cash-flow
  statements) and shown under the COMPUTATION below.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is "a share is a business": would I be content to own this "if the market closed for
five years" **[M1997-109]**, which here means owning a contractor whose largest customer gives half its revenue under
contracts the filing says "can be cancelled or renegotiated by our customers at any time" (10-K Item 1A). The second is the
analyst's own habit: look for "what’s wrong in things" **[M2025-013]**, and aim the reading "to possibly reject your
original hypothesis" **[M1998-144]**. No macro view of oil enters. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the restatement of 2020 and earlier (FY2022 20-F, Note 4): 2020 net income cut from $50.1M to $16.6M
and equity before 2020 cut by $50.4M, from unrecorded payables in Saudi Arabia and the UAE; (2) a material weakness "related
to tone at the top" for FY2022 to FY2024 (10-K Item 9A); (3) an SEC cease-and-desist order of 2024-08-28 with a $400,000
penalty (FY2024 20-F); (4) Nasdaq delisting effective 2023-04-28 (FY2023 20-F cover); (5) auditor churn: KPMG dismissed
2021, PwC resigned 2023 without issuing an opinion, KPMG resigned its re-audit 2023, Grant Thornton dismissed 2026-08-04
(FY2022 20-F Item 16F; 8-K `0001493152-26-036716`); (6) the same explanation in three years of results, "transition between
hydraulic fracturing contracts in Saudi Arabia" (2021, 2022) and "reduced hydraulic fracturing stages upon contract
transition" (2025); (7) accounts payable up from $305.3M (2024-12-31) to $603.2M (2026-06-30) on flat-to-rising revenue,
which the 10-Q calls "more closely controlling timing of payments on Accounts payable". Each is placed below under the
question it bears on.

## THE STANDING RULE
Nothing in this run finances, sizes or holds a position; a purchase made with the buyer's own money and no borrowing does
not engage the rule, which forbids borrowed money in "the investor's tool kit" **[L2014-005]** and the risk of "what we have
and need for what we don’t have and don’t need" **[M2012-081]**. Not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as stated.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will
  be in 10 years" **[M2000-037]**; the product need not be understood if "the economic dynamics of the industry" are
  **[M2011-014]**.
- **What the business is** (10-K Item 1, `0001493152-26-009139`): an oilfield-services contractor, about 99% of revenue in
  the MENA region; two segments, Production Services (fracturing, coiled tubing, stimulation, cementing, nitrogen and the
  rest; 62% of 2025 revenue) and Drilling and Evaluation Services (rigs, well testing, wireline, directional drilling and
  the rest; 38%). The customers are national oil companies; four customers gave 49%, 9%, 8% and 7% of 2025 revenue (54%,
  9%, 7%, 4% in 2024).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (a) the activity budgets of a handful of NOCs
  (the filing's own two indicators are oil price and rig count, MD&A Executive Overview); (b) whether NESR wins and keeps
  the tendered contracts of the largest customer, and at what price; (c) its cost against the rivals bidding for the same
  work. Variable (a) is the regional budget, which the speakers would not forecast and do not need to: a dependence on a
  commodity price is not by itself a STOP, "We don’t think we can predict commodity prices." **[M2016-025]**, and the business
  is judged "off the figures" **[M2008-069]**. Variables (b) and (c) are the castle and the cost position, which Q2 reads
  from the filer's and the rivals' filings.
- **Do the past statements tell the future ones?** Yes in kind: the service lines, the customers and the cost structure
  have been the same since 2018, and the figures are filed for 2018 to 2025, with the caveat that 2018 and 2019 were never
  restated year by year (the $50.4M correction before 2020 was taken through equity, FY2022 20-F Note 4). That caveat
  belongs to Q4.
- **Fast-moving technology?** No: the services are long-established; the Roya directional-drilling tools are a growth
  effort inside one segment, not the economics of the whole **[M1998-008]**.
- **Abroad** **[M2000-141]**: a BVI company operating through subsidiaries in Saudi Arabia, Oman, Kuwait, the UAE, Iraq,
  Algeria, Egypt and Libya, taxed country by country; the governance is a US-listed domestic filer from 2026. Readable from
  the filings, at the edge rather than well inside.
- **Can I name the winner, not just the industry** **[M2012-067]**? That is the question Q2 answers from the figures; a
  sustainable edge is judged only after this filter **[M1997-148]**.
- **VERDICT: IN.** The economics of a regional oilfield-services contractor can be foreseen in kind from its filings; what
  cannot be assumed is that it will win its tenders at a good price, which is the castle question and goes to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (business of parts, section B; segment operating income from the segment notes of the FY2025 10-K
`0001493152-26-009139` and the FY2023 20-F `0001493152-24-017128`; US$ millions; before unallocated corporate costs of 40 to
72 a year):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share | Decides |
|---|---|---|---|---|---|---|---|---|
| Production Services | -1.9 | 28.7 | 111.1 | 146.9 | 100.3 | 385.1 | 66% | **yes** (more than half) |
| Drilling and Evaluation | -1.2 | 33.5 | 36.5 | 63.1 | 69.1 | 200.9 | 34% | no |

The file closes on Production Services. Both parts sell to the same NOCs on the same terms, so most facts below bear on both.

**The castle tests, each with its filing fact.**
1. **Key factors and their permanence** **[M1995-038]**. The filing names NESR's claimed edge as local: "promoting high local
   content in our operations optimizes our cost structure" (10-K MD&A Executive Overview) and "superior execution,
   reliability, and a commitment to safety" (Item 1, Competition). Neither is shown to be permanent by any figure in the
   filings: no market share, no win rate and no price premium is disclosed in the 10-K or the 20-Fs read.
2. **The customer and the low bid** **[M2017-009]**, **[L2004-003]**. The customers are NOCs; one gave 49% of 2025 revenue
   (54% in 2024). The filing lists the factors of competition in this order: "price, operational performance, product and
   service quality, safety record, responsiveness, technological capability" (Item 1); "Most of our contracts can be
   cancelled or renegotiated by our customers at any time" (Item 1A). The deciding part's revenue has moved three times on
   the re-tender of one customer's fracturing work: 2021, "decreased hydraulic fracturing stages in Saudi Arabia during
   transition between hydraulic fracturing contracts"; 2022, "a reduction in hydraulic fracturing activity in Saudi Arabia
   during a transitory period between hydraulic fracturing contracts" (FY2022 20-F `0001493152-23-046470`, MD&A); 2025,
   "reduced hydraulic fracturing stages upon contract transition coupled with reduced coiled tubing activity in Saudi Arabia"
   (10-K MD&A), with Production Services operating income down from 146.9 to 100.3; and then up again, Q2 2026 Production
   Services revenue $329.7M against $205.1M "primarily due to increased hydraulic fracturing stages in Saudi Arabia" (10-Q
   `0001493152-26-036720`). The work is won and lost by contract, and no filing shows the customer preferring NESR at a
   higher price.
3. **The money test** **[M2011-015]**: could a rival with money take the business? The filing answers it: "Several of our
   primary competitors are diversified multinational companies with substantially larger operating staff and greater
   capital resources"; the industry is "dominated by a few large players that have resources to invest in new technologies"
   (Item 1A). One competitor "is frequently enough to ruin a business" **[M2012-108]**.
4. **Pricing power** **[M2005-020]**: no price increase is described in any year read; the downturn language is the filer's
   own, "downward pressure on the prices that we are able to charge" (Item 1A). Cost increases were not passed through in
   2021: cost of services 99.7% of revenue, from "supplier price inflation mainly on chemicals and consumables" among other
   causes (FY2022 20-F MD&A).
5. **The low-cost position**, which in a field where the customer buys by tender is the castle that would have to be there
   **[M1997-010]**, **[M2001-013]**, measured "more by cost of production" **[M2006-004]**, and "The figures are available."
   **[M2009-059]**. The competitor row below is the measure. NESR's operating margin over 2021 to 2025 was 4.9% against
   12.9% to 15.7% at the three rivals in the same five years; on tangible capital, 11.5% pre-tax against 25.4% to 40.3%.
   A contractor earning about a third of its rivals' margin on the same customers' kind of work in the same up-cycle is not
   the low-cost producer, whatever its local cost advantages; the filer's claim that local content "optimizes our cost
   structure" is not borne out by its margins against the rivals'.
6. **Brand and share of mind**: none is claimed for a contractor whose customers are a few NOCs; the test does not apply.
7. **Widening or narrowing** **[M1999-108]**: margins rose from -4.9% (2021) to 10.6% (2024) and fell to 7.4% (2025) on
   flat revenue, with cost of services up 359 basis points "mainly due to an elevated cost structure expected to support
   higher activity levels going forward" (10-K MD&A). H1 2026 shows the operating margin back at 10.9% on revenue up 47%
   (10-Q). The swings follow contract volume; no evidence of a widening moat.
8. **What could destroy it** **[M2000-014]**: the loss or re-pricing of the largest customer's work, which the filing names:
   "the failure to extend or replace the contracts with a major customer, or the extension or replacement of such contracts
   on less favorable terms, as a result of competition or otherwise" (Item 1A).
9. **Ask the competitors**: none of the rivals' figures used names NESR; no scuttlebutt on the public record was found or
   sought beyond the filings.

**The competitor row** (the brief's departure (2)). **No rival is named** in the 10-K's competition paragraph ("both large
multinational corporations and smaller local service providers") nor in the 20-F for FY2024 ("competitors comprised of both
small and large companies"); a text search of the FY2025 10-K and the 20-Fs for FY2018 to FY2024 for SLB, Schlumberger,
Halliburton, Baker Hughes, Weatherford, Nabors and the regional drillers found the names only in directors' biographies and
as the source of a rig count. **CONVENTION of this run:** the rivals are SLB, Halliburton and Weatherford; rationale: they
are the three SEC-filing multinationals with the largest oilfield-service operations in the Middle East offering the same
service lines (fracturing, coiled tubing, cementing, wireline, well testing, directional drilling), so they bid for the
same NOC work. Flagged, relevant rivals that do not file with the SEC: ADES Holding and Arabian Drilling (Saudi-listed),
ADNOC Drilling (Abu Dhabi-listed), Chinese state service companies (Sinopec Oilfield Service, CNPC units, China Oilfield
Services), and the smaller local providers the 10-K mentions without names. Caveats: the rivals' figures are company-wide,
not MENA-only, since none of the three reports profit by region; they are tagged XBRL from the rivals' own 10-Ks,
transcription, not cross-checked line by line against the filed statements (flagged per operator rule 4).

| Company (latest 10-K accession) | Metric | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2021-25 | 2018-25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NESR (`0001493152-26-009139`; 2018-19 from `0001493152-21-006706`, pre-restatement) | operating margin | 13.6% | 10.9% | 4.2% | -4.9% | -0.1% | 7.0% | 10.6% | 7.4% | 4.9% | n/m |
| NESR | operating income / tangible capital | | | 7.8% | -9.8% | -0.2% | 16.9% | 29.2% | 21.3% | 11.5% | 10.9% (2020-25) |
| Halliburton (`0000045012-26-000015`) | operating margin | 10.3% | -2.0% | -16.9% | 11.8% | 13.3% | 17.7% | 16.7% | 10.2% | 14.1% | 8.7% |
| Halliburton | operating income / tangible capital | 16.4% | -3.4% | -25.8% | 18.0% | 25.2% | 34.2% | 30.3% | 18.1% | 25.4% | 14.9% |
| SLB (`0001193125-26-021017`) | pre-tax income plus interest / revenue | 9.7% | -29.8% | -45.5% | 12.7% | 16.9% | 17.5% | 17.0% | 13.6% | 15.7% | 2.9% |
| SLB | same / tangible capital | 19.7% | -66.3% | -108.1% | 26.5% | 41.9% | 42.0% | 42.2% | 34.5% | 37.8% | 6.8% |
| Weatherford (`0001603923-26-000014`) | operating margin | -36.3% | reorganized | -40.3% | 3.2% | 9.5% | 16.0% | 17.0% | 15.4% | 12.9% | n/m |
| Weatherford | operating income / tangible capital | n/m | | n/m | 8.8% | 29.8% | 62.6% | 56.5% | 40.2% | 40.3% | n/m |

Tangible capital = equity plus borrowings less cash, goodwill and intangibles, at each year-end (research folder:
`peers.py`, `peer_table_hal_wfrd_nesr.txt`, `peer_table_slb.txt`). NESR's 2018 adds the successor and predecessor periods
(operating income 53.4 + 12.8 on revenue 348.6 + 137.0, FY2020 20-F `0001493152-21-006706`); 2018 and 2019 are as first
filed and overstated by an unallocated part of the $50.4M correction before 2020 (FY2022 20-F, Note 4). SLB's GAAP line
includes its 2019 and 2020 impairments; its tagged operating income before charges is 12.1% and 10.2% of revenue in those
years. Weatherford's 2019 is omitted: it was reorganized in 2019, with $4,297M of claims and liabilities discharged on
2019-12-13 (its 10-K `0001603923-20-000017`, reorganization items).

**The field's returns over the last full cycle** (section C), judged in words, not by a figure **[M1999-108]**. The cycle
2018 to 2025 runs from the 2018 level through the 2020 trough to the 2023 and 2024 peak and the 2025 decline. Over it the
field's durable players earned ordinary returns at best: Halliburton 8.7% on revenue, SLB 2.9% on revenue after its
charges, Weatherford a reorganization that discharged $4.3 billion of claims. NESR, inside the field, earned less than
each of them in the up-cycle years 2021 to 2025, and in 2021 and 2022 lost money at the operating line while Halliburton and
SLB earned 11.8% to 16.9%. This is the case the rows name: "you can have only two competitors and they’re still terrible
businesses" **[M2013-052]**; a standing castle protects "excellent returns" **[L2007-004]**, and the returns here are
ordinary for the field and below ordinary for NESR. The improvement of 2023 and 2024 is not a change for the better
credited on a full cycle **[M2017-026]**, **[L1995-022]**: it reversed in 2025 on one contract's transition and returned in
2026 on the next.

**The non-deciding part** (Drilling and Evaluation, 34%): the same customers and the same tendering; its operating income
rose each year 2022 to 2025 (33.5, 36.5, 63.1, 69.1) on "increased rig assignments and sites in Saudi Arabia" and the Roya
directional-drilling tools (10-K MD&A). No castle is shown for it either; it would be carried to Q7 as an ordinary business
at no growth.

**Why OUT and not TOO HARD.** The tenuous-moat row sends a castle to TOO HARD because "We don’t know how to valuate that"
**[M2000-019]**; here the returns are known from the filer's and the rivals' filings over a full cycle, and the cost
position is read from the figures, which the commodity-business paragraph of Q2 says is the test: the high-cost producer in
a field whose customers buy by tender is OUT **[M1997-010]**. The castle is shown open on the evidence: the customer
re-tenders the work, price is named first, the rivals are larger and earn more on the figures, and the field's returns over
the cycle are ordinary; asked whether an attacker with money could take it, the filing itself says yes **[M2011-015]**.

- **VERDICT: OUT** on the deciding part, Production Services: the castle is shown open on the evidence (one customer's
  fracturing work re-tendered three times in five years, price named first among the factors, margins about a third of
  the rivals' in the same five years), and the field's durable players earn only ordinary returns over the full cycle
  2018 to 2025.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read (the template asks for them in Step 0 when the file closes before Q4); the
reading is under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts were found and are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback test has nothing to read: no repurchase and no dividend in the filings read.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked; oilfield services is not among the named businesses).

---
## THE BOX
**OUT at Q2**, on the deciding part (Production Services): a castle shown open on the evidence, one customer's work
re-tendered, price named first, margins about a third of the SEC-filing rivals' over 2021 to 2025, in a field whose durable
players earned ordinary returns over the full cycle 2018 to 2025. **Integrity facts recorded, not judged** (the 2020 and
earlier restatement, the tone-at-the-top material weakness of FY2022 to FY2024, the SEC cease-and-desist order of 2024, the
auditor history; see AFTER THE STOP, Q5). COMPUTATION beneath the stop: value about $6.53 to $12.03 a share all-equity
against $19.11, no case earns the floor at the price; fair price about $4.59 all-equity ($3.52 equity-only).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).

**Bearing on Q3 (capital).**
- Pre-tax operating income on tangible capital 11.5% over 2021 to 2025 (7.8%, -9.8%, -0.2%, 16.9%, 29.2%, 21.3% for 2020 to
  2025); on total capital including the $645M of goodwill paid in the 2018 combination and the 2020 and 2021 acquisitions,
  far lower (operating income averaged $54.5M a year 2021 to 2025 against equity plus net debt of about $1.15 to $1.26
  billion).
- Capital spending "predominantly to purchase equipment to support revenue growth" (10-K Item 1): $107.1M, $122.4M, $68.2M,
  $105.1M, $143.5M for 2021 to 2025, plus seller-financed capex paid $15.3M, $14.4M, $15.6M, $3.8M, $7.4M, IPM investments
  $17.4M (2022) and $16.0M (2023), finance-lease principal $21.4M (2021) then $2.4M to $3.9M; depreciation (D&A less
  amortization of acquired intangibles) $104.1M, $97.0M, $123.5M, $124.0M, $123.0M. Net PP&E $426M (2021) to $465M (2025)
  and $531M (2026-06-30) on revenue up 51% 2021 to 2025. H1 2026 capex $110.1M "to support growth in our operations" (10-Q).

**Bearing on Q4 (the accounts): the balance sheets first.** The reading the template asks for, 2018 to 2025 (`tools/run.py` table, first-filed tagged vintages, read against
the filed balance sheets of the FY2025 10-K and the 20-Fs):
- Equity $831M (2018) to $968M (2025): retained earnings $28M, $68M, $29M (2020 restated), then negative, -$36M, -$75M,
  -$62M (2021 to 2023), then $14M and $65M; the rest of the growth in equity is shares issued (SAPESCO and Action, stock
  pay, the 2025 warrant exchange). Goodwill $571M to $645M (the 2020 and 2021 acquisitions), unchanged since 2021, never
  impaired; intangibles amortizing from $138M to $47M.
- Cash $25M to $125M (2025) and $175M (2026-06-30). Debt on the face $302M (2018), peak $596M (2021), $310M (2025),
  $275M (2026-06-30).
- Receivables $63M (2018) to $178M (2025), with unbilled revenue $121M and retention withholdings $33M beside them
  (2025); the proxy gives DSO of 70 days at 2025 year-end. Inventory $58M to $95M, flat since 2020 against revenue up 59%.
- **Accounts payable and accrued expenses**: $314.6M (2021), $353.5M (2022), $351.2M (2023), $305.3M (2024), $421.1M (2025),
  $603.2M (2026-06-30, 10-Q). The increase was $116.2M of 2025's operating cash of $264.2M and $181.5M of H1 2026's $204.8M,
  which the 10-Q explains as "improved working capital management year-over-year, and in particular more closely
  controlling timing of payments on Accounts payable and accrued expenses in relation to payment terms". Against cost of
  services, payables rose from about 28% (2024) to 36% (2025) and about 38% (H1 2026 annualized). The restatement of 2020
  was "primarily related to the completeness of accounts payable and accrued liabilities in Saudi Arabia and the United
  Arab Emirates" (FY2022 20-F).
- **The restatement** (FY2022 20-F `0001493152-23-046470`, Note 4 and the Note at its front): 2020 net income $50.1M as
  first reported, $16.6M restated (a $34.1M correction of assets and liabilities in 2020, a $45.3M reclassification from
  SG&A to cost of services, and a $0.6M warrant correction); equity before 2020 reduced by a further $50.4M, taken through
  opening balances and not allocated to 2018 or 2019, so the income statements of 2018 and 2019 stand as first filed and
  overstated by an unknown split of that sum. The SEC order (below) describes the restatement as of "previously issued
  financial statements for 2018 through 2020" (FY2024 20-F).
- What the owner cash leaves out if read from tagged data: the seller-financed capital spending and the IPM investments
  sit outside the capex tag (above); `tools/run.py` did not see them.
- The adjusted figure and the targets: the annual bonus pays on adjusted EBITDA and DSO; "The Company’s 2025 adjusted
  EBITDA was $281 million. Adjusted EBITDA includes adjustments for certain Total Charges and Credits [...] of $38
  million", against a target of $273M (DEF 14A `0001493152-26-012394`). The 2021 MD&A calls "Many of the costs" of that
  year's loss "one-off or non-recurring in nature" (FY2022 20-F); charges recur in later years ("Impairments and other
  charges" $7.9M, $5.3M, $9.6M for 2023 to 2025, cash-flow statement).
- Stock pay $9.8M, $9.3M, $6.8M, $6.0M, $8.3M (2021 to 2025), charged in owner cash below.

**Bearing on Q5 (the people): integrity facts, recorded, not judged.**
- The restatement above, caused by unrecorded liabilities found on an ERP change in Saudi Arabia and the UAE.
- A material weakness for FY2022, FY2023 and FY2024: "Our executive officers failed to set an appropriate tone at the top
  sufficient to ensure a culture of compliance with the Company’s accounting, finance and internal control policies"
  (10-K Item 9A); declared remediated in 2025, with ICFR effective at 2025-12-31 and the auditor's opinion on it (10-K).
- SEC: on 2024-08-28 a settled cease-and-desist order under Exchange Act sections 13(a), 13(b)(2)(A) and 13(b)(2)(B),
  without admitting or denying, with a $400,000 civil penalty and a further $1.2M had the weakness not been remediated by
  2025-08-28 (FY2024 20-F `0001641172-25-001136`). The FY2025 10-K reports the weakness remediated; no payment of the
  $1.2M is reported in the filings read.
- Listing: delisted from Nasdaq effective 2023-04-28 for the late filings, traded on the OTC Pink market, later relisted
  (FY2023 20-F `0001493152-24-017128`; Nasdaq Capital Market on the FY2024 20-F cover).
- Auditors (FY2022 20-F Item 16F; 8-K `0001493152-26-036716`): KPMG dismissed 2021-03-31 and PwC appointed; on 2022-03-10
  the company concluded it would restate 2020; KPMG engaged 2022-06-15 to re-audit 2018 to 2020 and resigned that
  engagement 2023-05-15; PwC resigned 2023-06-09 having issued no audit opinion; Grant Thornton (Dubai Branch) engaged
  2023-07-12; on 2026-08-04 the audit committee dismissed Grant Thornton effective after the FY2026 audit and appointed
  PwC for FY2027; the 8-K reports no disagreements and names the tone-at-the-top weakness as the reportable event.
- The chairman is the chief executive, Sherif Foda, "since inception" (10-K Item 10), holding 3.2% (DEF 14A); the CFO
  reports to the non-employee directors on financial reporting "at least until December 31, 2026", and has had "final
  responsibility for the Company’s capital expenditure process" since March 2023 (10-K Items 1 and 9A).
- CEO pay 59 times the median employee's $38,212 for 2025 (DEF 14A); retention bonuses paid to the CFO under a 2023
  agreement.

**Bearing on Q6 (the money and the owners).**
- No dividends and no repurchases in the filings read. Shares outstanding rose from 85.6M (2018-12-31, the 20-F cover) to 100.85M (2026),
  through acquisition issuance, stock pay and the 2025 warrant exchange (3,413,645 shares for 34,136,353 warrants).
- Acquisitions: SAPESCO (2020, $13.2M cash in the cash-flow statement), Action service lines (2021, $51.9M cash); minority
  WDVGE stake (2022); NEDA and technology stakes at cost of $25.2M (2025), $5.1M impaired in 2025 and up to $7.1M more at
  risk in 2026 (10-K Item 1).
- Major holders (DEF 14A): Olayan Financing 17.2%, FMR 7.4%, Encompass 7.1%, SCF-VIII 6.4%, Al Nowais Investments 5.3%;
  Olayan and Al Nowais each have board nomination rights under 2018 relationship agreements.

**Bearing on Q9 (debt and exposures).**
- Net debt $99.6M at 2026-06-30 (current long-term debt $64.5M, short-term borrowings $50.4M, long-term debt $159.7M, less
  cash $175.0M; 10-Q). The secured term loan, $225.8M drawn, is due 2027-11-04; the revolving facility was not extended
  after 2026-02-04; "The Company is currently working with its lenders to refinance and extend the 2021 Secured Facilities
  Agreement" (10-Q). The working-capital facility for guarantees and letters of credit, $283.8M, was $266.3M utilized.
  Covenants: net debt to EBITDA up to 3.5, debt-service coverage at least 1.25, EBITDA interest cover at least 4.0, in
  compliance. Relating the debt to the ability to pay **[M1995-104]** is the Q9 question, not reached.
- Concentration: one customer 49% of revenue; contracts cancellable at the customer's option (10-K Item 1A); operations in
  Iraq, Libya and other countries named in the 10-K's political-risk factor.

## COMPUTATION, NOT A CLEARANCE
*(The file closed at Q2. The figures below are the operator's reporting figures, computed by Q7's construction; they are
not a valuation verdict and carry no entry language, operator rule 3.)*

**Owner cash after every real cost** (US$ millions, from the filed cash-flow statements: FY2025 10-K for 2023 to 2025, FY2023
20-F for 2021 and 2022, FY2022 20-F for 2020 as restated; `compute.py` and `computation_out.txt` in the research folder).
All-spending case = operating cash less stock pay, capital spending, IPM investments, other investing (the strategic stakes),
seller-financed capex paid, finance-lease principal and cash paid for acquisitions, plus disposal proceeds. Maintenance case
= operating cash less stock pay, depreciation as the maintenance guess, and other investing, plus disposal proceeds. Unlevered
(all-equity) = the same plus cash interest paid net of a 20% tax shield.

| | 2021 | 2022 | 2023 | 2024 | 2025 | five-year average |
|---|---|---|---|---|---|---|
| all spending, after interest (equity-only) | -83.2 | -81.0 | 68.8 | 105.2 | 92.4 | 20.4 |
| maintenance only, after interest (equity-only) | 8.4 | -20.6 | 47.5 | 93.3 | 124.2 | 50.5 |
| all spending, before interest (all-equity) | -75.3 | -65.6 | 95.9 | 135.8 | 115.2 | 41.2 |
| maintenance only, before interest (all-equity) | 16.3 | -5.2 | 74.6 | 123.9 | 147.0 | 71.3 |
| memo: increase in payables and accruals | 31.2 | 33.7 | -3.4 | -38.5 | 116.2 | |

**Q7's range convention, item by item.**
- Base: the five-year average, 2021 to 2025. **(a) Cycles:** 2021, the first year, is a trough by the filer's own account
  (an operating loss, costs "one-off or non-recurring in nature", the contract transition); a base over a full cycle of
  owner cash cannot be built, since 2018 and 2019 were not restated year by year and the restated record (2020 to 2025)
  holds no completed peak-to-peak or trough-to-trough of owner cash. The literal window is therefore the base, said so;
  the longest restated span, 2020 to 2025, is shown beside.
- **(b) Decline and sign change:** the all-spending series changes sign; the compound rate between the end years is
  meaningless, and between the halves of the window (2021 and 2022 averaging -70.4 unlevered, 2024 and 2025 averaging
  125.5) it is meaningless too; the maintenance series likewise (5.5 against 135.4). By (b) the range is the no-growth case
  alone, said so. Sales grew 10.9% a year 2021 to 2025, which is not owner-cash growth and is not credited.
- **(c) Acquisitions:** the $51.9M paid for Action in 2021 is deducted in the all-spending case; no growth is credited, so
  no organic pair is needed; net purchases ($51.9M) are less than half of owner cash before purchases over the window, so
  the serial-acquirer rule does not apply; no merger (deal paid in shares) inside the window; no deal signed and unclosed.
- **(d) Working capital** is counted (it is inside operating cash). Beside: 2025 with its $116.2M payables increase
  removed, since the filer ties the build to the timing of its payments, not to the business's needs.
- **(e) Growth spending:** the filing says the capital spending was "predominantly" for growth, and depreciation is the
  maintenance guess the rows allow, "not inappropriate in most companies to use as a proxy for required capital
  expenditures" **[M1998-127]**; so the maintenance-only case is central. With no growth credited, the all-spending case
  charges growth spending and credits nothing for it; it is shown as the bottom, and the inversion (the growth bought worth
  less than its cost) is the finding the rows allow, "growth can destroy value" **[L2000-023]**.
- **(f) The cap:** not engaged; no growth is carried.
- Rate 5.43% (the sovereign); after year ten no growth (here, none at all). Net debt $99.6M at 2026-06-30; operating
  leases left out. Company's own tax: owner cash is after the taxes it paid; the tax note was not read for carryforwards or
  credits, so no shelter is priced (a gap, stated).

**Value range** (all-equity, less net debt, per share on 100.852M shares):
- **Bottom, all spending, no growth:** $41.2M / 5.43% = $759M; less net debt $99.6M = **$6.53 a share** (equity-only
  $3.73).
- **Top, maintenance only, no growth:** $71.3M / 5.43% = $1,313M; less net debt = **$12.03 a share** (equity-only $9.23).
- Against **$19.11**. Width 1.84 to 1 per share, under three to one.
- **The floor, tested first:** at the price (market value $1,927M plus net debt $99.6M = $2,027M), the cases yield 2.0% and
  3.5% at no growth; no case in the range earns about ten percent; the price is above the top of the range. By Q7's
  construction this would close OUT at the floor whatever the width **[M2003-149]**. For scale, not as a case: the
  maintenance base grown at the 10.9% sales rate for ten years and then flat is worth $1,520M at ten percent, still below
  the $2,027M paid.
- Beside, 2025 payables increase removed: $2.29 to $7.79 a share. Beside, the six-year span 2020 to 2025: $5.80 to $10.82.

**Fair price** (Part VII: each end case valued at ten percent, the two averaged, after the company's own tax): bottom
$41.2M / 10% = $412M, top $71.3M / 10% = $713M, average $562M, less net debt $99.6M = **$4.59 a share on the all-equity
basis (the central figure)**; **$3.52 a share equity-only** ($20.4M and $50.5M at ten percent, averaged, per share). No cheap
price is reported.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `1bc2d9c3`); written question by question; committed after Step 0
      to Q1 (`e84a5163`), after Q2 (`3cd0d36f`), and at the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock file was present in `Screens/_daily/`
      (held by the dispatcher, not touched); the fold is the dispatcher's.
- [x] No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened or searched; one listing of
      `Test Runs/` to check this run's file name showed other runs' names, declared under contamination above, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (check script
      `check_cites.py` in the research folder, PASS); every filing fact carries its accession; numbers come from filings
      or carry their convention.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the figures beneath it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from the
      US Treasury par curve; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations paragraph, seven items); the facts for later questions are
      under AFTER THE STOP, and the box line carries the integrity flag.
- [x] No point-in-time anchor applies (a live run); no row dated after the price date.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three-year "owner earnings", yield and v4 lines were not.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Weak points, honestly: the rivals' figures are company-wide tagged data, not MENA segments, and were not cross-checked
  line by line against their filed statements; the 20% tax shield on interest is a CONVENTION of the run; the 2018 and
  2019 NESR margins in the competitor row are known to be overstated; the maintenance guess is depreciation, which the
  filer neither confirms nor contradicts.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Rivals for a field where the filer names none and the real rivals are company-wide.** The brief's convention let me
choose SLB, Halliburton and Weatherford, but none reports profit for the Middle East, so the cost comparison Q2's
commodity-business paragraph asks for ("measured by cost of production") is made at company level, against rivals whose mix
differs; the framework says nothing on how far a company-wide comparison may stand for a regional one. I said so and judged
on the size of the gap (a third of the margin over five years), which no difference of mix seemed able to close; a closer
call would have needed a rule. (2) **Q7 (b) when every growth measure is meaningless and (e) is engaged.** The text sends a
sign-changing series to "the no-growth case alone", while (e) makes the maintenance case central and forbids charging all
spending while capping the growth it bought. With no growth credited at all, it is unclear whether the all-spending
no-growth case is a legitimate bottom (it charges growth spending against nothing) or should be dropped, leaving a
one-point "range" and a fair price that is the maintenance case alone. I kept it as the bottom, as (e)'s inversion clause
reads, and say so; the fair price would be $6.08 on the maintenance case alone. (3) **A cycle base the filer's record
cannot supply.** (a) asks for a full-cycle base where an end year is aberrational; where the only years before the window
are known to be misstated and not restated year by year, the text gives no fallback. I used the literal window and showed
the longest restated span beside. (4) **Payables as a source of owner cash.** (d) counts working capital, and treats a draw
tied to one event as aberrational; it says nothing of a release (here, payables stretched by management's own account,
$298M in eighteen months), which flatters the base. I showed it removed beside. (5) **The template's Q4 balance-sheet
reading in a file closed at Q2** has no home except AFTER THE STOP, and Q4's own row cannot be cited there without
implying the question was reached; I recorded the reading without the citation.
