# Company Run: Mayville Engineering Company, Inc. (NYSE: MEC), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit c8089f90). Research folder:
`Test Runs/_research 2026-10-17 MEC/` (filings as fetched, the text conversions, `run_py_output.txt`,
`cover_shares_output.txt`, the rivals' XBRL facts in `peers/`, the arithmetic scripts and their outputs).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (df63a4b2): not held; `PORTFOLIO.md` has no line for MEC or Mayville.*

**Dispatch.** A dispatched purchase run under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the one departure
the brief states (the lines of evidence derived by the analyst from the 10-K, below).

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` taken to check that this run's paths did
not exist showed the file names of other runs dated 2026-10-17 (ALFVY, AMTM, ARCAY, BCKIY, CDNL, FER, FLR, LGN, MPTI, MTRX,
TTEK) and their research folders; none was opened. (2) The session context at start carried the git status and the last
five commit subjects, which are about the MTRX run (its box and Q7 figures) and name research folders of AYI and ARCB;
nothing about MEC. (3) The session context carried the project map and a memory index line about the queue in general
terms ("gate-clearers, nothing buyable"); nothing about MEC. No `Test Runs/` file about MEC under any name was seen. None of
this is used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $13.90, close 2026-10-16, from `tools/run.py` (aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: common stock, no par, one class, **25,500,331** shares as of
  2026-07-31 (10-Q for the quarter ended 2026-06-30, filed 2026-08-05, accession `0001104659-26-091110`;
  `python Screens/cover_shares.py MEC`). Check against the balance sheet of the same 10-Q: 27,684,120 issued less 2,187,334
  treasury = 25,496,786 at 2026-06-30; the 3,545 difference to the cover is consistent with restricted-unit vesting in July.
  The May 2026 offering (8-K of 2026-05-21, accession `0001104659-26-064802`; final prospectus supplement 424B5 filed
  2026-05-20, accession `0001104659-26-064616`): 4,348,000 shares at $20.00 plus the fully exercised 652,000-share option,
  5,000,000 in all, net proceeds $93,884 thousand in the 10-Q's cash-flow statement ("Proceeds from stock offering"). These
  shares are inside the 2026-06-30 count (issued rose from 22,505,704 at 2025-12-31). The only 8-K after the 10-Q is the
  results release of 2026-08-04 (accession `0001104659-26-090424`, items 2.02 and 9.01); no issuance after it was found.
- **Market cap:** 25.500331M x $13.90 = **$354.5M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-03-04, accession `0001104659-26-023496`): Items 1, 1A, 2, 5,
  7, 8 and the notes on acquisitions, debt, leases, taxes, ESOP and deferred compensation; 10-Q for Q2 2026 (filed
  2026-08-05, `0001104659-26-091110`); proxy DEF 14A of 2026-03-10 (`0001104659-26-025849`); 8-Ks of 2026-08-04 with
  exhibit 99.1, 2026-05-21, 2026-02-26 (`0001104659-26-020541`, the credit agreement amendment), 2025-07-01
  (`0001558370-25-009027`, Accu-Fab closing) and the 8-K/A of 2025-09-15 (`0001104659-25-089961`); the 10-Ks for FY2019 to
  FY2024 (accessions `0001564590-20-008206`, `0001564590-21-011139`, `0001564590-22-008290`, `0001558370-23-002542`,
  `0001558370-24-002598`, `0001558370-25-002369`) for the statements of the cycle; the IPO prospectus 424B4 of 2019-05-10
  (`0001193125-19-144347`) for the 2017 balance sheet. **One figure cross-checked against the filed statement:** operating
  cash flow FY2025, $38.6M in `tools/run.py`, is $38,562 thousand on the face of the FY2025 consolidated statement of cash
  flows (10-K, page 48). Match.
- **`tools/run.py MEC`, arithmetic lines only** (output in the research folder). Operating cash flow, stock pay, capital
  spending and depreciation for FY2023 to FY2025 as filed: OCF 40.4 / 89.8 / 38.6; SBC 4.5 / 5.2 / 3.3; capex 16.6 / 12.1 /
  11.6; D&A 35.1 / 37.6 / 41.3 ($M). The tool's three-year mean of OCF less SBC less capex is 38.5 and on the D&A basis 13.9;
  its five-year means are 15.1 (capex basis) and 7.8 (D&A basis); it flags the 97% divergence between windows. Finance-lease
  principal (0.4 / 0.6 / 1.0) is an alternate the tool does not choose; this run deducts it. SBC is resolved from the
  cash-flow statement in every year; no other stock-pay line was found. Nothing the tool prints as a rule, a floor or an id
  is used (Part VII, The tooling).

### Owner cash after every real cost, by year (USD millions; from the filed cash-flow statements; arithmetic in `owner_cash.txt`)
Owner cash = OCF less stock pay less capital spending (net of PP&E sale proceeds) less finance-lease principal. Acquisitions
are listed separately. Interest paid is shown so the all-equity figure (before interest, after the company's own tax) can be
built at Q7. Years before 2019 are pre-IPO: an S corporation owned by its ESOP that paid no income tax and bought back ESOP
shares in cash, so 2017 and 2018 are shown for the balance sheet and the cycle, not used in the owner-cash base.

| FY | OCF | SBC | capex | PP&E sold | fin. lease | **owner cash** | acquisitions | interest paid |
|---|---|---|---|---|---|---|---|---|
| 2019 | 33.4 | 3.5 | 25.8 | 0.1 | 0.5 | **3.7** | 2.4 | 6.6 |
| 2020 | 36.5 | 4.7 | 7.8 | 2.0 | 0.6 | **25.4** | 0 | 3.0 |
| 2021 | 14.5 | 5.0 | 39.3 | 5.3 | 0.5 | **-25.0** | 0 | 2.1 |
| 2022 | 52.4 | 3.8 | 58.6 | 7.9 | 0.3 | **-2.3** | 0 | 3.7 |
| 2023 | 40.4 | 4.5 | 16.6 | 1.1 | 0.4 | **19.9** | 88.6 (MSA) | 10.7 |
| 2024 | 89.8 | 5.2 | 12.1 | 0.4 | 0.6 | **72.3** | 0 | 10.3 |
| 2025 | 38.6 | 3.3 | 11.6 | 0.1 | 1.0 | **22.7** | 140.0 (Accu-Fab) | 9.7 |
| H1 2026 | -1.3 | 2.3 | 12.3 | 0.0 | 1.2 | **-17.1** | 0 | 7.0 |

The year notes the filer gives: 2021 carries the cancelled contract of a former fitness customer (an impairment and loss on
contracts of $16,151 thousand in the FY2022 10-K income statement, and an inventory build of $27.9M in OCF); 2023 carries an
$18.5M distribution from the legacy deferred-compensation plan (10-K FY2025, Note on deferred compensation: distributions of
"$253, $286 and $18,520" for 2025, 2024, 2023); 2024 carries the $25.5M gross payment from that fitness customer settling the
lawsuit, which the filer calls a gain on lawsuit settlement; 2025 the filer describes as "reduced customer demand across nearly
all end markets and customer de-stocking channel inventory" (10-K FY2025, Item 7). Five-year mean 2021 to 2025: **$17.5M**;
cycle mean 2020 to 2025: **$18.8M**.

### The lines of evidence this name needs, derived from the FY2025 10-K (the brief's one departure)
1. **Item 1, Customers and Competitive Strengths:** "embedded relationships", "high customer switching costs", "We have not
   historically experienced customer attrition"; top customer 13.6% and top ten 62.3% of 2025 sales (PACCAR 13.6%, John Deere
   10.0%). Tested at Q2 against the margins the relationships earn.
2. **Item 1, Cost Structure and Strategy:** contracts "pass through changes in commodity prices"; MBX "Commercial Excellence"
   includes "the implementation of a value-based pricing model". Tested at Q2 as pricing power.
3. **Item 1A:** competitors "be better positioned to compete on price [...] or willingness to make sales at lower margins than
   us"; customers may "insource the production of components that has traditionally been outsourced to us"; "Most of our
   customers do not commit to long-term production schedules". Q1 and Q2.
4. **Item 1A:** "Because our industry is capital intensive and we have significant fixed and semi-fixed costs, our
   profitability is sensitive to changes in volume." Q3 and Q4.
5. **Item 1A and Item 7:** the acquisition strategy (Mid-States Aluminum 2023, Accu-Fab 2025) and the new dependence on data
   center and critical power demand. Q3, Q6, Q7.
6. **Item 7, Liquidity:** consolidated total leverage 3.68 to 1 at 2025-12-31 against a 4.00 covenant; $17,730 thousand of
   availability; the 2026-02-25 amendment cutting the facility to $275,000 thousand and raising the leverage ceiling to 5.25.
   The standing rule and Q9.
7. **Item 7:** EBITDA, Adjusted EBITDA and free cash flow presented as "key performance indicators", and guidance in the
   releases. Q4 and Q5.
8. **Item 7 and the notes:** the 2021 contract loss and the 2024 lawsuit gain, the two aberrational years. Q7 (a).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the fabrication business will earn, "Would I be happy buying this stock if the
market closed for five years?" **[M1997-109]**, not what the price did after a $20.00 offering in May and a $13.90 close in
October; the market "just tells us prices" **[M2006-077]**. Margin of safety: if the decision needs a pencil, "it’s too close to
think about" **[M1996-084]**. No macro enters: the heavy-truck cycle and the data-center build-out are read only as the
business's own record, "macro conclusions are — just never enter into the discussion." **[M2000-094]**. Who is paid to tell you:
the company sold 5,000,000 new shares in May 2026 through underwriters, and its releases feature Adjusted EBITDA and guidance;
the seller's projection is not consulted **[M2011-083]**. The analyst's habits: look for "what’s wrong" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (i) against the bear case: owner cash was positive in five of
the seven taxed years, the company has been ranked the largest U.S. fabricator by The Fabricator for fifteen years, and the
2026 order book shows data-center awards of about $40M in Q2 alone (8-K 2026-08-04, ex. 99.1); (ii) against the bull case:
operating margin below every chosen rival over the span (Q2), negative tangible equity at 2025-12-31 (Step 0 balance
sheets, below), a covenant amendment followed by an equity raise, and negative owner cash in H1 2026.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin, provided it is bought with the buyer's own money and sized so that a
large fall forces nothing: "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**;
no borrowed money for it **[L2014-005]**. The target's own debt is a separate matter, weighed at Q9.

### The balance sheets first (read in Step 0 because the file closes before Q4; **[M2025-032]**)
USD millions, from the filed balance sheets (2017 from the IPO prospectus; 2018 to 2025 from the 10-Ks; 2026-06-30 from the
10-Q). Tangible equity = equity less goodwill and intangibles.

| year-end | sales | total assets | equity | goodwill + intangibles | tangible equity | receivables | inventory | revolver + term debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 313.3 | 214.3 | (temporary equity, ESOP-owned) | n/a | n/a | n/a | n/a | 67.9 incl. other LT liabilities | 17.7 |
| 2018 | 354.5 | 391.7 | (temporary equity 103.0) | 152.3 | n/a | 52.3 | 53.4 | 179.9 | 26.8 |
| 2019 | 519.7 | 363.6 | 200.9 | 143.7 | 57.2 | 40.2 | 45.7 | 72.6 | 22.1 |
| 2020 | 357.6 | 338.5 | 200.9 | 133.0 | 67.9 | 42.1 | 41.4 | 45.3 | 15.0 |
| 2021 | 454.8 | 379.5 | 198.3 | 122.3 | 76.0 | 55.4 | 70.2 | 67.6 | 7.5 |
| 2022 | 539.4 | 440.6 | 217.9 | 115.3 | 102.6 | 58.0 | 71.7 | 72.2 | 26.3 |
| 2023 | 588.4 | 496.7 | 230.0 | 151.3 | 78.7 | 57.4 | 67.8 | 147.5 | 34.1 |
| 2024 | 581.6 | 445.6 | 251.8 | 144.4 | 107.4 | 49.8 | 54.8 | 79.7 | 60.1 |
| 2025 | 546.5 | 563.6 | 240.7 | 251.5 | **-10.8** | 57.6 | 59.4 | 203.9 | 52.0 |
| 2026-06-30 | (H1 307.8) | 588.6 | 325.5 | 245.5 | 80.0 | 77.2 | 69.3 | 127.1 | 41.7 |

What the figures say **[M2025-032]**. (1) The asset base grew by purchase, not by retention: goodwill and intangibles went
from $115M (2022) to $252M (2025) through two cash acquisitions paid with the revolver, while retained earnings moved from
$22M at the IPO year-end to $52M at 2025 and back to $42M at 2026-06-30, about $20M kept in six and a half years. (2) At
2025-12-31 tangible equity was negative and the revolver stood at $202.5M against $17.7M of availability; the 2026 equity
issue, not earnings, restored it. (3) Working capital is moving the wrong way for cash: receivables were 7.7% of sales in
2019, 10.5% in 2025 and $77.2M at 2026-06-30 on a second-quarter run-rate of about $652M a year (11.8%); inventory rose $10.8M
in H1 2026. (4) Cash is never held; the revolver is the cash account (cash $0.0M to $3.1M at every year-end). What they do not
say: the margin each end market earns (one segment, no profit by end market) and the price terms of the customer contracts.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product need not be understood if "I understand the economic dynamics of the
  industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**. The product here is plain:
  laser-cut, bent, stamped, welded and coated steel and aluminum parts and assemblies made to OEM drawings (10-K Item 1,
  Our Capabilities).
- **The key variables and whether they are foreseeable** ("trying to identify the key variables in that particular business,
  and evaluating how predictable they were first" **[M1998-044]**): (a) the build rates of the customers' end markets
  (class 8 trucks, construction and access, powersports, agriculture, data center enclosures): cyclical, not foreseeable year
  by year, but their averages over a cycle are visible in nine years of filings; (b) the spread MEC earns over its pass-through
  material cost, which its statements show year by year; (c) the capital it must put in to hold and win platforms (the 2021
  and 2022 capex of $39M and $59M, the two acquisitions). None is a technology forecast. The data-center line is newer and
  faster-moving, but the thing sold into it is the same fabricated metal; what is not foreseeable is that market's volume,
  not MEC's economics per unit of it.
- **Do the past statements tell me the future ones?** **[M2008-033]**: largely yes for the kind of business; the nine years
  show a fabricator whose earnings swing with customer volume around a thin margin. The ten-year picture that can be written
  down is of the same job-shop economics at larger size, not a different business.
- **Contrary evidence.** Customers can change the volume by design changes, insourcing, or cancellation (Item 1A; the 2021
  fitness-customer cancellation is the instance), and "Most of our customers do not commit to long-term production
  schedules" (Item 1A). That limits how sure the volume can be, which is Q7's "how sure", not a bar to understanding the
  economics. A doubt would put it outside **[M2002-092]**; my doubt is about how good the economics are, not about what they are.
- **Routing.** Not a fast-changing industry in the sense of **[M1998-008]**; not a financial institution; one operating segment.
- **VERDICT: IN, narrowly.** The economics of a contract metal fabricator can be foreseen from its filings **[M2012-065]**,
  **[M2011-014]**; whether they are good is Q2's question.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**; and what the castle must
protect, "excellent returns on invested capital" **[L2007-004]**.

**The castle the filer claims** (10-K FY2025, Item 1): embedded relationships with "high customer switching costs"; scale
("largest fabricator in the United States for the past 15 years in a row" per The Fabricator magazine); breadth ("no single
manufacturer directly competes with us across our full offering"); a "highly fragmented" field of "small local players"; and
"We have not historically experienced customer attrition".

**The castle tests, each with its filing fact.**
1. *Key factors and their permanence* **[M1995-038]**. The relationships are real (John Deere for "more than 40" years,
   over 65 platforms) but they are relationships with buyers who re-award the work at every redevelopment cycle ("generally
   every three to five years for our customers", Item 1) through "the request for proposal processes" (Item 1, Sales and
   Marketing). A relationship that is re-bid every three to five years is held by price and execution each time, not owned.
2. *Would it stand without the lord?* The MBX programme dates from 2022 under the present chief executive, with COO
   restructuring costs in 2023 and CFO transition costs in 2025 (Adjusted EBITDA reconciliation, Item 7). No fact found that
   the business earns well whoever runs it; the record below says it has earned poorly throughout.
3. *The money test* **[M2011-015]**. Could a well-funded attacker build or buy this position? The filer itself shows that
   it can be bought: it entered data-center enclosures by paying $140,500 thousand for Accu-Fab, LLC from Tide Rock YieldCo,
   LLC (10-K FY2025, Note 2), and it bought Mid-States Aluminum for $95,945 thousand in 2023 (10-K FY2023, Note 2). The
   field is "highly fragmented" with many local players (Item 1). Fabrication capacity (lasers, press brakes, robotic welding,
   coating lines) is bought equipment (Item 1, Technology-Enabled Infrastructure). Here the answer to the See's question is
   yes, the answer on which "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**; and "there are some
   industries that are just never going to have barriers to entry" **[M2012-106]**.
4. *Pricing power and the agony before a rise* **[M2005-020]**. The filer's contracts pass material cost through ("pass
   through changes in commodity prices", Item 1); that protects the margin from steel and aluminum, it is not power over
   the margin itself. Its strategy names "the implementation of a value-based pricing model" as an aim (Item 1, MBX
   Commercial Excellence), which says the prices were not set on value before. Item 1A lists competitors able to "compete on
   price [...] or willingness to make sales at lower margins than us" and customers whose loss of share may lead them "to
   reduce prices, thereby exerting pricing pressure on us". In 2025, with sales down 6.0%, the manufacturing margin fell from
   12.2% to 9.9% of sales (Item 7): the margin follows the volume.
5. *Unit volume.* Net sales were $519.7M in 2019 and $546.5M in 2025, but 2025 includes Mid-States Aluminum (bought 2023;
   $25.7M of sales in its first half-year, 10-K FY2023 Note 2) and Accu-Fab ($40.7M from 2025-07-01, 10-K FY2025 Note 2). On the
   filer's own pro forma (10-K FY2025, Note 2), sales with Accu-Fab for both full years fell from $643.1M (2024) to $580.5M
   (2025), down 9.7%. Organic volume over the span is flat to lower; the growth in the line is bought.
6. *The low-cost position* **[L2000-017]**, **[M1997-010]**. Where "The guy who could sell it cheaper than we could made it
   risky for us." **[M1997-010]**, the evidence for a low-cost position would be margins above the rivals' over the cycle. The
   competitor row below shows MEC's below every rival chosen, over the whole span.
7. *The brand.* None; the product carries the customer's brand.
8. *Would the customer still choose it over the low bid?* **[M2017-009]**. The work is won in request-for-proposal rounds,
   most customers "do not commit to long-term production schedules", and a customer may decide "to insource the production of
   components that has traditionally been outsourced to us" (Item 1A). The 2021 cancellation by the fitness customer, settled
   for $25.5M in 2024, is the instance of a customer walking away. No fact found of MEC holding work against a lower bid.
9. *Ask the competitors.* Not available on the public record for this field; the one rival 10-K read in full (CMT FY2025,
   "MAJOR COMPETITORS") names only molders, not MEC.
10. *Widening or narrowing* **[M1999-108]**. Operating margin 3.0% (2017), 6.3% (2018), then -0.4%, -1.8%, -1.6%, 4.8%,
    3.4%, 7.7% (about 3.3% without the $25.5M lawsuit gain), -0.7% (2025), and -2.4% for H1 2026 (10-Q). No widening is
    visible in nine years.
11. *What could destroy or reduce it* **[M2000-014]**. Insourcing by a large customer (PACCAR 13.6%, Deere 10.0%, top ten
    62.3%); a customer's own loss of share; and, in the new line, the data-center capital cycle the filer names as a risk
    ("reduced capital spending by Data Center & Critical Power customers or delays or cancellations of project launches",
    Item 1A).

**The competitor row.** The 10-K names no rival: "we believe that no single manufacturer directly competes with us across our
full offering" (Item 1), and Item 1A speaks of "competitors" without names. The comparison set is therefore a **CONVENTION of
this run**: three SEC filers that, like MEC, make engineered metal or structural components to order for heavy-truck,
construction, powersports and industrial OEMs: Commercial Vehicle Group (CVGI), Core Molding Technologies (CMT) and Park-Ohio
Holdings (PKOH). Rationale: they sell into the same OEM build cycles on the same award terms, while the proxy's compensation
peer group (Ampco-Pittsburgh, The Eastern Company, Miller Industries, AZZ, Gorman-Rupp, Myers Industries, Blue Bird, Hurco) is
chosen by size, not by business. Named rivals that do not file: none named. Metric: operating income over net sales, and
operating income over total assets, from each filer's 10-K XBRL facts (transcription; CMT's FY2025 operating income of $14,218
thousand cross-checked against the face of its 10-K, accession `0001026655-26-000009`).

| filer | span | mean operating margin | range | mean operating income / total assets | last 10-K accession |
|---|---|---|---|---|---|
| **MEC** | 2017 to 2025 | **2.3%** (2018 to 2025: 2.2%) | -1.8% to 7.7% | **2.6%** (2018 to 2025) | `0001104659-26-023496` |
| CVGI | 2016 to 2025 | 2.9% | -3.2% to 7.4% | 5.9% | `0001628280-26-016520` |
| CMT | 2016 to 2025 | 3.7% | -4.1% to 7.4% | 5.4% | `0001026655-26-000009` |
| PKOH | 2016 to 2025 | 4.0% | -0.8% to 6.4% | 4.9% | `0000076282-26-000007` |

(Arithmetic in `peer.py` and `peer2.py`, output in `peers_out.txt`. MEC's 2024 includes the $25.5M lawsuit gain; without it
MEC's span is lower still.)

**The parts table.** One operating segment and one reporting unit (10-K FY2025, Item 7 and the goodwill note); no profit is
reported by end market. The parts paragraph does not apply; the end markets are read as one business.

**The field's returns over the last full cycle, judged in words** (the CONVENTION on "ordinary" carries no figure). The span is
2019 to 2025 for MEC as a taxed public company and 2016 to 2025 for the rivals; it holds the 2020 trough, the 2022 to 2023 peak
and the 2024 to 2025 downturn. The field earns thin margins on every filer's record, low single digits on sales and mid single
digits pre-tax on total assets: ordinary at best and, against a long government bond at 5.43%, poor. MEC earns the least of the
four: pre-tax operating income averaging 2.6% of total assets, below the government bond before tax in an average year. That
is not a castle protecting even ordinary returns. It is the business the rows describe in the price-taker, "whatever he charged
for gas was my price" **[M2012-109]**, and in the field where "the improvement you get one day, your competitor gets the next
day" **[M2004-053]**.

**Contrary evidence, written down** **[M1997-127]**. (a) The 2026 data-center ramp: Q2 2026 data center and critical power
sales of $29.0M against $5.0M a year earlier, organic growth in that line of 172.8% (8-K 2026-08-04, ex. 99.1), and Accu-Fab's
$7,335 thousand of operating income on $40,697 thousand of sales in its first half-year (18.0%), well above MEC's own margin.
(b) Q2 2026 manufacturing margin of 10.9% against 10.3%. Read against the rule that a change for the better is credited only on
a full cycle in which the price behaviour held **[M2005-020]**, **[L1995-022]**: no filed year shows MEC's margin or return
improved and held; H1 2026 operating income is negative (-$7.3M on $307.8M of sales), and the improvement is in the release's
guidance, not in the statements. The 18% margin is what was paid for: $140.5M for about $14.7M of annualized pre-tax operating
income, about 10% pre-tax on the price, which buys a return and does not show a castle.

**Why OUT and not TOO HARD.** The castle's future is not unknowable; it is shown on nine years of the filer's statements and ten
of three rivals', and the rows send a known, poor return to OUT: the moat is what "protects excellent returns" **[L2007-004]**;
"you can have only two competitors and they’re still terrible businesses" **[M2013-052]**; and the tenuous-moat row, "We don’t
know how to valuate that" **[M2000-019]**, does not apply where the returns are known. The money test fails **[M2011-015]**, the
pricing test fails **[M2005-020]**, and the low-cost test fails against the rivals **[M1997-010]**. Price does not reopen it:
"What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The castle is open on the evidence: a contract fabricator without pricing power, entered by purchase, earning
  the lowest returns of a low-return field over the whole span **[M2011-015]**, **[M2005-020]**, **[L2007-004]**, **[M2013-052]**.
  The file closes here. Q3 to Q12 are NOT REACHED as clearances; what follows is facts found and computation only.

## Q3 to Q6, Q8 to Q10, Q12: NOT REACHED (the file closed OUT at Q2; operator rule 2)

## Q7: COMPUTATION, NOT A CLEARANCE
*(The file closed at Q2. These figures are the two reporting figures the brief asks for, built by Q7's range convention, and
carry no entry language. Arithmetic in `owner_cash.py`, output `owner_cash.txt`.)*

- **The cash input** (Q4's recast; **[L2021-003]**): owner cash after every real cost, from the table in Step 0. The all-equity
  figure adds back interest paid at an after-tax rate of 25% (**CONVENTION of this run**: 21% federal plus state; rationale:
  Q7's basis needs owner cash before interest and after the company's own tax, the filing's own effective rate swings with
  losses and discrete items, and 25% sits between the 2024 effective rate of 22.6% and the statutory federal rate plus state).
- **(a) Cycle base.** Both end years of the literal window 2021 to 2025 are aberrational on the filer's own description: 2021
  carries the cancelled fitness-customer contract and its $27.9M inventory build; 2025 is "reduced customer demand across
  nearly all end markets and customer de-stocking". The base is the last full cycle, trough to trough, 2020 (the pandemic
  trough) to 2025, both troughs included: **$23.76M a year** before interest. The literal window beside it: $22.98M.
- **(b) Decline and sign.** The series changes sign (2021 and 2022 negative). Halves: 2020 to 2022 mean $1.6M, 2023 to 2025
  mean $46.0M; a compound rate between them is meaningless (the second half carries the $25.5M lawsuit receipt of 2024 and the
  first the loss it settled). **The range is the no-growth case alone**, said so.
- **(c) Acquisitions.** Net purchases 2021 to 2025: $228.5M (Mid-States Aluminum $88.6M, Accu-Fab $140.0M), against owner
  cash before purchases of $87.6M. More than half: **the serial acquirer**; the central figure is the organic pair, purchases
  left out, organic growth as the filer reports it. The 10-K reports no organic growth figure; the releases report it only
  quarter by quarter; the filer's pro forma shows 2025 down 9.7% on 2024 with Accu-Fab in both years. Organic growth credited:
  none. The default pair beside it (purchases deducted, total growth credited): base **-$14.3M** a year over the cycle, a
  negative value; the purchases have cost more than the whole business has produced. Accu-Fab closed inside the window and is
  in the base for its half-year; no deal is signed and unclosed.
- **(d) Working capital** is inside operating cash flow every year. The H1 2026 draw ($19.8M receivables, $10.8M inventory) is
  outside the window and is not in the base.
- **(e) Maintenance.** The filing does not state a maintenance figure. Capital spending ran $11.6M to $16.6M in 2023 to 2025
  against depreciation of $27.3M to $31.6M, after $97.9M in 2021 and 2022; over 2019 to 2025 capital spending was $171.8M and
  depreciation $176.8M. The filing does not allow the maintenance guess, so the all-spending case is central; the depreciation
  variant (depreciation in place of capital spending) is shown beside: base $19.57M.
- **(f) The cap.** No growth is carried; nothing to cut.
- **Net debt at 2026-06-30** (10-Q): revolver $125,718 thousand + Fond du Lac term note $1,375 thousand + finance-lease
  liabilities about $9,827 thousand (estimate: $2,904 thousand at 2025-12-31 per the 10-K lease note, plus $8,150 thousand of
  new finance-lease assets and less $1,227 thousand of principal paid in H1 2026 per the 10-Q; the 10-Q gives the undiscounted
  payments as $10,803 thousand) less cash $2,203 thousand = **$134.7M**. Operating leases (about $29.0M) left out, said so. No
  subsequent event is stated in the 10-Q. Market value $354.5M; market value plus net debt **$489.2M**.

**The floor first** **[M2003-149]**. The one case, no growth on $23.76M, earns 4.86% on $489.2M at the price; the literal window
4.70%; the depreciation variant 4.00%; equity-only, $18.83M on $354.5M, 5.31%. **No case earns the floor of about ten percent
at the price**, so Q7, had it been reached, closes OUT whatever the width.

**Value range (COMPUTATION, all-equity, at the 5.43% sovereign, less net debt):** no-growth case alone, **$11.88 a share**
(literal window $11.31; depreciation variant $8.85) against a price of **$13.90**. The price sits above the only case.

**Fair price (a reporting figure, never a verdict; Part VII):** the single case valued at ten percent: $23.76M / 0.10 =
$237.6M, less $134.7M of net debt, over 25.500331M shares = **$4.04 a share, all-equity basis (central)**, after the company's
own tax. Equity-only beside it: $18.83M / 0.10 / 25.500331M = **$7.39 a share** (higher than the central figure because the
cycle's interest was paid on smaller borrowings than the $134.7M owed now). Literal-window fair price $3.73; depreciation
variant $2.39. No cheap price is reported.

## THE BOX
**OUT at Q2** (the castle open: no pricing power, entered by purchase, the lowest returns of a low-return field over the whole
span). Integrity facts recorded, not judged. Q7 as COMPUTATION: no-growth value $11.88 a share (all-equity) against $13.90; fair
price $4.04 (all-equity), $7.39 equity-only; no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed, each with its source **[M1997-127]**; the box unchanged, operator rule 2.)*

**Q3 (capital).** Capital employed (equity plus revolver and term debt) was about $273M at 2019 and $444M at 2025; operating
income summed over 2019 to 2025 was $70.9M (10-K income statements), $45.4M without the 2024 lawsuit gain. The two acquisitions
cost $236M (purchase prices $95.9M and $140.5M) for about $14.7M of annualized Accu-Fab operating income (Note 2, FY2025) and
an MSA contribution the filings give only for its first half-year ($3,027 thousand of operating income on $25,687 thousand of
sales, 10-K FY2023 Note 2). 2026 capital spending is planned at $25M to $35M, plus an "incremental $50 million in organic growth
initiatives across 2026 and 2027" (8-K 2026-08-04, ex. 99.1).

**Q4 (accounts).** The 10-K presents EBITDA, Adjusted EBITDA and free cash flow as "key performance indicators" (Item 7);
the releases feature Adjusted EBITDA, Adjusted Net Income and Adjusted Diluted EPS and give quarterly and annual guidance
(8-K 2026-08-04, ex. 99.1: Q3 2026 net sales $160M to $170M, Adjusted EBITDA $15.5M to $18.5M; FY2026 net sales $620M to $650M,
Adjusted EBITDA $52M to $60M, free cash flow $7M to $15M). The Adjusted EBITDA reconciliation adds back stock pay every year and
a different list of one-time items each year (2023: field replacement claim, legal costs, COO restructuring, acquisition
costs, inventory step-up; 2024: legal costs, restructuring, less the lawsuit gain; 2025: CFO transition, tornado clean-up,
acquisition costs, restructuring, inventory step-up). An impairment of $1,544 thousand in Q1 2026 (10-Q). Receivables rose to
$77.2M at 2026-06-30. No accounting confusion found in the statements read; the auditor excluded Accu-Fab's internal control
from the 2025 assessment as permitted for an acquisition (10-K FY2025, auditor's report and Item 9A).

**Q5 (people; integrity facts recorded, not judged).** The guidance habit and the featured adjusted figures above, which the
framework carries from Q4 to Q5 (Q4, The make-the-numbers habit). The proxy (DEF 14A 2026): CEO Jag Reddy's 2025 total
compensation $3,183,288 in the Summary Compensation Table; no annual bonus earned for 2025 (Adjusted EBITDA and free cash flow
goals missed); one-time cash "transaction awards" approved 2026-03-02 for completing Accu-Fab ($370,000 to the CEO, $960,000
in all to five officers), described as for "a strategically significant, immediately accretive transaction"; directors and
officers as a group own 5.6%; the ESOP 9.4% and the 401(k) plan 10.7% (record date 2026-02-20). The proxy's performance
stock units measure ROIC and Adjusted EBITDA.

**Q6 (money and owners).** Buybacks: $4,607 thousand in 2025 for 304,136 shares (treasury count 1,883,198 to 2,187,334), an
average of about $15.15 a share, and $5,896 thousand in 2024; none in H1 2026. The 10-K states no price limit: repurchases
"will depend on business conditions, free cash flow generation, other cash requirements and stock price" (Item 7). The
COMPUTATION's only case is $11.88 a share (all-equity) and $8.85 on the depreciation variant, so the 2025 prices paid sat above
the bottom of the computed range (the Q6 test written back from Q7, here as a fact only). Issuance: 5,000,000 new shares at
$20.00 in May 2026, net $93.9M, used to repay the revolver and to fund the $50M growth plan (ex. 99.1). Both acquisitions were
paid in cash from the revolver; neither was paid in stock, so Q6's one STOP does not arise. No dividend.

**Q9 (debt and exposures).** At 2025-12-31 consolidated total leverage was 3.68 to 1 against a 4.00 covenant (raised from 3.50
for four quarters after the Accu-Fab deal), with $17,730 thousand available (10-K FY2025, Item 7). The 2026-02-25 amendment
cut the facility to $275,000 thousand, raised the leverage ceiling to 5.25 for Q1 and Q2 2026, 5.00 for Q3, 4.00 for Q4 and
3.50 from 2027, and lowered the interest-coverage minimum to 2.75 (8-K 2026-02-26). At 2026-06-30, after the offering:
leverage 2.91 to 1, interest coverage 3.27 to 1 against 2.75, availability $108,505 thousand, rate 6.65%; everything matures
2028-06-28 (10-Q). Customer concentration: PACCAR 13.6%, Deere 10.0%, top ten 62.3% (10-K FY2025, Item 1).

**Q12.** None of the businesses the framework names; no newspaper-test fact found.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit c8089f90); written question by question; committed after Step 0 and
      Q1 (beb79294), after Q2 (c2dbfceb), and after this close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not checked by
      the analyst); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the one directory listing of
      `Test Runs/` (taken to check this run's paths) and the session-start context are declared under contamination and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_ids.py` in the research folder; every filing fact has
      its accession or its document and date; the rivals' figures are XBRL transcription of their 10-Ks, one cross-checked.
- [x] The order was kept; Q1 IN, Q2 OUT closed the file; nothing after it is a clearance; Q7 headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capital spending, finance-lease principal), never a net-income proxy;
      the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations, Q1, Q2); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message of the close).

**Weak points, honestly.** (1) The comparison set is mine (CONVENTION), because the 10-K names no rival; a different set of
contract fabricators could show different margins, though all three chosen run above MEC. (2) The finance-lease balance at
2026-06-30 is my estimate from the 10-K and 10-Q flows; an error of a few million moves the per-share figures by cents. (3) The
after-tax rate on interest (25%) is a CONVENTION of this run. (4) The cycle is drawn trough to trough with both troughs in; drawn
2021 to 2025 the base is $22.98M and nothing changes.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A change for the better that is only projected.** Q2 credits a change for the better only on a full cycle and, until
then, sends the file to TOO HARD (NATURE) with a re-look condition. The text does not say whether that route opens when the
claimed change exists only in the company's guidance and in a newly bought end market, with no filed year showing the margin or
return improved. Read literally, any guided improvement could turn a known poor record from OUT into TOO HARD. I read the rule as
applying only where the filings show the change; here they do not, so the box is OUT. A line saying so would settle it.
(2) **The serial acquirer's "organic growth, as the filer reports it".** This filer reports no organic growth in its 10-K, only
quarter by quarter in its releases. The convention does not say what to credit then; I credited none and said why. (3) **The
cycle base.** "Trough to trough" does not say whether both trough years are counted; I counted both and showed the literal
window beside it. (4) **After-tax interest.** The all-equity basis needs interest after the company's tax, and Q7 does not fix
the rate where the effective rate is distorted by losses; I confessed 25%. (5) **No named rivals.** The brief's rule (a chosen
set is a CONVENTION) works, but neither the brief nor Q2 says whether the proxy's compensation peer group should be preferred
when the 10-K is silent; I rejected it as chosen by size and said so.
