# Company Run — Versigent PLC (NYSE: VGNT) — 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no VGNT row).*

**Dispatched run.** Written by a dispatched analyst under `Screens/_daily/_dispatch_brief.md` with the departures the
brief states: the repository path (moved 2026-10-25 to C:\Projects\BRK); the lines of evidence derived by the analyst, not
handed down (listed under Step 0); and the primary documents for a company with no 10-K on file (the Form 10 information
statement and two 10-Qs, with Aptiv PLC's 10-Ks for the segment).

**Contamination, declared.** (1) A directory listing of `Test Runs/`, made to check that no file of this name existed before
the template was copied, showed the file names of fourteen other runs dated 2026-10-26 (ASML, NRG, OGE, PAM, PCG, PEG, PLTR,
PNW, PPL, RWEOY, SNPS, SO, TAC, UTL) and their research folders; none was opened and none concerns Versigent or Aptiv.
(2) The session header showed the subjects of the last five commits (a UTL run and its fold); not used. (3) A memory index
line read at session start names queue state in general terms (wave counts, gate-clearer counts); it names no company bearing
on this run and was not used. No run, holding review or `PORTFOLIO.md` was opened, listed by name for this company, or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $41.40 (close 2026-10-23, the last full session before the run; Yahoo Finance chart endpoint through
  `tools/sources.py`, an aggregator, permitted for the live quote only and flagged per operator rule 5). The intraday quote
  at 14:31 ET on 2026-10-26 was $41.35; not used. Range since the spin, from the same aggregator: $34.22 to $50.22.
- **Shares by class** from the latest filing's cover: 70,835,265 ordinary shares, $0.01 par, as of July 31, 2026 (10-Q for
  the quarter ended June 30, 2026, filed 2026-08-04, accession `0002078008-26-000018`; `python Screens/cover_shares.py VGNT`
  returns the same count). One class; 50,000,000 preferred authorized, none issued. Checked against the balance sheet of
  the same 10-Q: 70,925,978 issued and 70,815,717 outstanding at June 30, 2026 (the difference, 110,261, held in treasury
  or as redeemable shares under the conversion programme). Filings after the 10-Q: Forms 4 and one Form 144 only (EDGAR
  submissions index, read 2026-10-26); no 8-K or prospectus changes the count. Diluted weighted shares in Q2 2026: 71.88
  million (same 10-Q); the cover count is used.
- **Market cap:** $41.40 x 70,835,265 = **$2,932.6M**.
- **Sovereign for the earnings currency:** the company reports in US dollars; **5.33%**, the 30-year par yield of the US
  Treasury daily par yield curve, dated 10/23/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4). Versigent has filed no 10-K and no proxy (EDGAR submissions index, 2026-10-26: no
  10-K, no DEF 14A). The primary documents read are:
  - the **information statement**, Exhibit 99.1 to Form 10-12B/A filed 2026-03-06, accession `0001193125-26-096776`
    (combined audited statements FY2023 to FY2025, Ernst & Young LLP opinion dated February 17, 2026; Business, Risk
    Factors and MD&A standing in for 10-K Items 1, 1A and 7; executive compensation; pro forma statements);
  - the **10-Q for Q1 2026**, filed 2026-05-05, accession `0002078008-26-000008`, and the **10-Q for Q2 2026**, filed
    2026-08-04, accession `0002078008-26-000018`;
  - **8-Ks**: 2026-04-01 (the spin), accession `0001193125-26-138219`; 2026-03-12, accession `0001193125-26-104279`;
    2026-03-24, accession `0000950142-26-000815`; the earnings 8-Ks of 2026-05-05 (`0002078008-26-000007`) and 2026-08-04
    (`0002078008-26-000014`), cover documents only (the press-release exhibits were not fetched);
  - **Aptiv PLC (CIK 1521332) 10-Ks** for the segment: FY2025 (filed 2026-02-06, accession `0001521332-26-000009`), which
    reports Electrical Distribution Systems as a segment for FY2023 to FY2025 after the realignment of the first quarter of
    2025; FY2024 (`0001521332-25-000010`) and FY2021 (`0001521332-22-000010`), which report only the combined Signal and
    Power Solutions segment (harnesses together with connectors); FY2018 (`0001521332-19-000007`) fetched, segment table not
    parsed.
  - **The span that could be read for the business itself: FY2023 to FY2025 and the first half of 2026**, from the
    information statement, the two 10-Qs and Aptiv's FY2025 10-K. No filing separates the harness business before 2023: it
    sat inside Signal and Power Solutions (Aptiv) and Electrical/Electronic Architecture (Delphi) together with the
    connector business. That is three years and a half, not a cycle, and it is said here so that every later question reads
    it.
- **One figure cross-checked against the filed statement:** FY2025 net sales $8,818M in the combined statement of
  operations (information statement, F-5) equals the Electrical Distribution Systems segment net sales of $8,818M in Aptiv's
  FY2025 10-K (accession `0001521332-26-000009`, Net Sales by Segment). FY2024 $8,309M and FY2023 $8,832M also agree.
- `python tools/run.py VGNT`: "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." No arithmetic lines printed; every
  figure in this file is taken from the filed statements.
- **Lines of evidence, chosen by the analyst from the primary documents** (brief departure (1)): (i) the pricing terms in
  Risk Factors and MD&A (contractual step-downs, termination for convenience, the "Pricing" paragraph), because they bear
  directly on the castle; (ii) labour content and footprint (People, Properties, MD&A cost structure), because the product is
  hand-assembled; (iii) customer concentration (Note 2, Risk Factors); (iv) the named competitors (Business, Competition)
  and new entrants; (v) volumes against global production (MD&A), for widening or narrowing; (vi) capital spending,
  depreciation and working capital (cash flow statements), for Q3; (vii) the spin financing and the dividend to the former
  parent (Q2 2026 10-Q, Note 10 and the cash flow statement), for Q6 and Q9. Chosen because each answers a question the
  framework asks of this business, not because each was expected to come out one way.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**; for a spin-off with three and a half years of separate history and a short quoted life, the price history
carries nothing, "It just tells us prices." **[M2006-077]**. No macro forecast enters (vehicle production, the EV pace,
tariffs): "macro conclusions are — just never enter into the discussion." **[M2000-094]**. Who is paid to tell you: the
information statement was written by the seller, Aptiv, for a business it chose to separate and load with $2.1 billion of
new borrowing, and its "Competitive Strengths" and expected "margin expansion" are the seller's description; projections in
it are not used, "You do not want to ask an investment banker what he thinks the earnings are going to be in five years of
something he’s trying to sell." **[M2011-083]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) on the
capital the business needs, operating income was about 36% pre-tax in FY2024 and 42% in FY2025 (computed at Q3), because
suppliers' credit funds most of the working capital and capital spending runs below depreciation; that is a strong figure
for any business and it runs against the castle reading below; (2) EDS's adjusted operating margin (7.6%, 6.9%, 7.6% in
FY2023 to FY2025) sits well above that of the one named rival that files with the SEC (Lear E-Systems, 3.9%, 4.1%, 3.1%
including restructuring), which is some evidence of a lower relative cost; (3) a 125-year incumbent with $52 billion of
gross new awards from 2022 to 2025 (information statement, Business), and the filing says OEMs prefer suppliers with global
scale.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not through the target: the buyer's risk is set by the buyer's financing and
size. The rule bars borrowing to buy it, "We are never going to risk what we have and need for what we don’t have and don’t
need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Bought with the buyer's own
money at any size the rule allows, a total loss of the stake would not ruin the buyer; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic
  dynamics of the industry" **[M2011-014]**; the first step is "trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**.
- **What the business is** (information statement, Business, accession `0001193125-26-096776`): low- and high-voltage wire
  harnesses and cables, customer-specific bundles of cut, crimped and taped wire, sold to light- and commercial-vehicle OEMs
  under requirements contracts for the life of a vehicle programme; one reportable segment; 59 manufacturing sites, 138,000
  people at December 31, 2025, of whom 129,000 hourly and about 38,000 contingent; 43% of sales in the Americas, 33% in Asia
  Pacific, 24% in EMEA; about 10% to commercial-vehicle and adjacent customers; ten largest customers 82% of FY2025 sales,
  the largest three 19%, 15% and 13% (Note 2), five largest 65% (Risk Factors).
- **The key variables and how predictable they are.** (1) Vehicle production: cyclical, not forecast, and not needed in
  level (no macro, above). (2) Harness content per vehicle: the filing says electrified vehicles carry "between 1.5 and 2.0
  times the wire harness content" of combustion vehicles, and also that OEMs "have recently announced delays in or changes
  to their electric vehicle investment strategies"; Lear's FY2025 10-K (accession `0000842162-26-000011`) describes "the
  transition to zone-based vehicle electrical architectures". Content is the least predictable variable, and its direction
  is mixed. (3) The price: set by contract, with step-downs "typically 1% to 3% per year" (Risk Factors). (4) Cost: copper,
  mostly passed through by contract clause; labour, which the business follows to the cheapest countries. Variables (3) and
  (4) are the economics, and they are the most predictable of the four: the filing describes the same terms Aptiv's 10-Ks
  have described for years.
- **Would the insiders write it down?** **[M2000-105]**. The industry's own filings write down what the business will look
  like (a Tier I supplier whose price the OEM steps down every year and whose margin depends on cost savings outrunning the
  step-downs); they do not write down content per vehicle in ten years. The first is the economics; the second moves the
  revenue line within a business whose economics are already described.
- **Change.** The filing calls the customers' industry "subject to rapid technological change"; the harness itself is an
  old product made by a labour-intensive process. "whenever we look at a business and we see lots of change coming, 9 times
  out of 10, we’re going to pass on that" **[M1999-063]**. The change here (electrification, zonal architectures,
  automation of harness assembly) bears on the castle and the content, which Q2 owns by the routing; it does not put the
  ten-year economics of a contract harness maker out of sight, because those economics are set by the customer's leverage,
  which does not depend on which architecture wins.
- **The perimeter.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.
  The doubt, written down: content per vehicle in 2036. The economics are not in doubt: a reader can say with reasonable
  confidence where the earning power and competitive position of a contract harness maker will stand in ten years, and
  the filings say it. The doubt is about the size of the revenue, not the nature of the economics, and Q2 is where it is
  weighed.
- **VERDICT: IN.** The economic dynamics are readable from the filings **[M2011-014]**, **[M2012-065]**; the key variables
  are named and the deciding ones (price terms, labour, copper pass-through) are stated in the filing **[M1998-044]**.
  Rapid change in the architecture is carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**Why it has stood.** The harness business has stood for over a century inside Packard Electric, Delphi and Aptiv. What keeps
it standing, on the filing's own account (information statement, Business, accession `0001193125-26-096776`): global scale
and footprint ("OEMs prefer suppliers that have the capability to manufacture products on a global basis"), programme
incumbency for the life of a vehicle, customer-specific engineering, and a cost position built by moving assembly to the
cheapest labour. The question is whether those protect a return, or only a place in the bidding.

- **1. The castle questions: what keeps it standing, how permanent** **[M1995-038]**. The reason the customer comes is
  delivery, quality and a global footprint at a competitive price; the filing's own list of how OEMs choose suppliers puts
  "product quality, price, reliability and timeliness of delivery" first, and the Risk Factors say "Competition is based
  primarily on price, technology, quality, delivery and overall customer service." Nothing in the filing names a reason a
  customer would pay more for this harness than for a rival's of equal quality.
- **2. Would it stand without the lord?** **[L2007-006]**. It does not depend on one person; the risk is the reverse, that
  results depend on continuous cost work by the whole organization (test 10 and the rebuilt moat, below).
- **3. The money test** **[M2011-015]**. Could a well-funded attacker take share? The filing answers: the industry "has
  attracted, and may continue to attract, new and disruptive entrants from outside the traditional automotive supply industry,
  particularly in countries such as China"; in China, "existing market participants will act aggressively to increase their
  market share. Increased competition may result in price reductions, reduced margins". The attacker needs plants in
  low-wage countries and qualification with an OEM. "there are some industries that are just never going to have barriers to
  entry. And in those industries, you better be running very fast" **[M2012-106]**.
- **4. Pricing power and the agony before a price rise** **[M2005-020]**. The test fails on the filing's own words: "Our
  customer supply agreements generally require step-downs in component pricing over the period of production, typically 1%
  to 3% per year. In addition, our customers often reserve the right to terminate their supply contracts for convenience,
  which enhances their ability to obtain price reductions. OEMs have also possessed significant leverage over their
  suppliers, including us, because the automotive component supply industry is highly competitive, serves a limited number
  of customers, has a high fixed-cost base and historically has had excess capacity." (Risk Factors). Other than copper,
  "our overall success in passing commodity cost increases on to our customers has been limited" (Business, Materials). The
  price moves down by contract and the customer holds the lever; the business does not raise its prices, it asks for
  recoveries. "If you name some business that has incredible pricing power, you’re talking about a business that’s a
  monopoly or a near monopoly." **[M2010-092]**; this is the opposite. The Q2 2026 10-Q repeats it: "contractual step-downs
  in component pricing over program life cycles" (accession `0002078008-26-000018`, MD&A, Pricing).
- **5. Unit volume** **[M1999-054]**. Volumes fell 8% in FY2024 against global vehicle production down 1%, and rose 5% in
  FY2025 against production up 4% (information statement, MD&A). Over the two years volume fell about 3% while production
  rose about 3%. Net sales: $8,832M (FY2023), $8,309M (FY2024), $8,818M (FY2025): flat across the span read.
- **6. The low-cost position** **[L2000-017]**, **[M1997-010]**. The filing claims a "Lean and Flexible Cost Structure" and
  "best cost countries". Against Lear E-Systems, the one named rival that files with the SEC, Versigent's margin is higher in
  each of the three years (below), which is evidence of a lower cost relative to Lear (with the caveat that Lear's segment
  mixes in connectors and electronics it is exiting). Whether it is THE low-cost producer cannot be read: the two largest
  harness makers the filing names, Yazaki Corporation (private) and Sumitomo Electric Industries, and the third, Furukawa
  Electric, do not file with the SEC. And the cost position, where it holds, is one made by moving labour to cheaper
  countries, which every rival also does (Lear's 10-K: production "is generally performed in low-cost labor sites in Mexico,
  Honduras, Brazil, Eastern Europe, Africa, China and the Philippines").
- **7. The brand** **[M2023-073]**. None asked for by name; the product is built to the OEM's drawing and carries no mark the
  vehicle buyer sees. The filing: trademarks are not "individually material to our business".
- **8. Would the customer still choose it over the low bid?** **[M2017-009]**. OEMs "rigorously evaluate suppliers on the
  basis of product quality, price, reliability"; they may re-source a programme and may terminate for convenience to get a
  lower price. The counter-model the speakers name, a parts maker "where people don’t simply just take the low bid in order
  to get this gadget" **[M2016-006]**, is one whose customers "would be totally crazy to hire some other supplier"
  **[M2016-009]**; the harness customer can re-source, and the contracts are written to let it.
- **9. Ask the competitors** **[M1999-130]**. Not available beyond the public record. Lear's FY2025 10-K says Lear is
  "de-emphasizing and exiting certain electronics product lines" inside E-Systems "where we do not see a path to sustainable
  risk-adjusted financial returns" (accession `0000842162-26-000011`, Item 1), a rival's reading of part of the field, not of
  harnesses specifically.
- **10. Widening or narrowing** **[M1999-108]**, **[L2005-010]**. For the business itself the span read is too short to show a
  trend in margin (adjusted operating margin 7.6%, 6.9%, 7.6%; GAAP operating margin 6.6%, 5.5%, 6.1%, FY2023 to FY2025).
  What the filing shows is the treadmill: restructuring charges every year ($48M, $101M, $86M; information statement F-5),
  "the continued rotation of our manufacturing footprint to best cost locations", and profitability that "depends in part on
  our ability to generate sufficient production cost savings in the future to offset price reductions" (MD&A). The margin
  holds only as long as the cost-down outruns the price-down.
- **11. What could destroy, modify or reduce it** **[M2000-014]**. The architecture change ("the transition to zone-based
  vehicle electrical architectures", Lear FY2025 10-K) and the automation of harness assembly change both the content and who
  can make it; the shift of share to domestic Chinese OEMs (Risk Factors) changes who the customers are; one customer, a
  "Global EV OEM", took 13% of FY2025 sales (Note 2).

**The parts table.** Versigent "operates its business as a single reportable segment, which includes LV and HV architectures"
(information statement, Business); no part reports separately, so the whole decides (section B).

**The competitor row** (each filer's own filing; segment margin on net sales):

| Year | Versigent / Aptiv EDS, GAAP operating margin | EDS adjusted operating margin | Lear E-Systems segment earnings margin, incl. restructuring | Source for Lear |
|---|---|---|---|---|
| 2014 | not separately filed | not separately filed | 12.6% | 10-K FY2016, `0000842162-17-000006` |
| 2015 | not separately filed | not separately filed | 13.5% | same |
| 2016 | not separately filed | not separately filed | 14.1% | same |
| 2017 | not separately filed | not separately filed | 14.0% | 10-K FY2019, `0000842162-20-000006` |
| 2018 | not separately filed | not separately filed | 12.3% | same |
| 2019 | not separately filed | not separately filed | 7.8% | same |
| 2020 | not separately filed | not separately filed | 2.3% | 10-K FY2020, `0000842162-21-000010` |
| 2021 | not separately filed | not separately filed | 2.5% | 10-K FY2022, `0000842162-23-000011` |
| 2022 | not separately filed | not separately filed | 1.4% | same |
| 2023 | 6.6% (587 / 8,832) | 7.6% | 3.9% | 10-K FY2024, `0000842162-25-000010` |
| 2024 | 5.5% (457 / 8,309) | 6.9% | 4.1% | same |
| 2025 | 6.1% (534 / 8,818) | 7.6% | 3.1% | 10-K FY2025, `0000842162-26-000011` |

Versigent figures: information statement F-5 and selected data (accession `0001193125-26-096776`); Aptiv's FY2025 10-K
(`0001521332-26-000009`) agrees on net sales and gives EDS adjusted operating income of $674M (FY2025) and $579M (FY2024).
Lear E-Systems FY2025: segment earnings of $228.9M in the segment note (the MD&A's figure including restructuring is $186M), on
segment total assets of $3,962.6M: about 5% to 6% pre-tax on the segment's assets. Not filed with the SEC, flagged: Yazaki
Corporation, Sumitomo Electric Industries, Furukawa Electric (the other three rivals the filing names). For context only,
Aptiv's Signal and Power Solutions segment (harnesses and connectors together) earned segment adjusted operating income of
$1,441M on $12,943M (2022), $1,676M on $14,404M (2023) and $1,652M on $13,983M (2024) (Aptiv FY2024 10-K,
`0001521332-25-000010`, segment note); the connector half (Engineered Components Group, gross margin 26.0% in FY2025 against
EDS's 12.2%, Aptiv FY2025 10-K) carried the larger share of that.

**The field's returns over the last full cycle** (section C). The only durable player whose harness-and-connection segment is on
file across a full cycle is Lear E-Systems: 12% to 14% of sales in 2014 to 2018, then 1.4% to 4.1% in 2020 to 2025, ending at
about 5% to 6% pre-tax on its segment assets, with "selling price reductions" named in nearly every year's explanation.
Versigent's own record is three years and cannot show a cycle; on those three years its margin is thin and flat, and its return
on the operating capital it needs is high (Q3), because suppliers' credit funds the working capital and capital spending runs
below depreciation. A thin margin "only works in terms of return on capital if you turn your equity extraordinarily fast"
**[M2017-096]**; this one does, and that is to its credit at Q3. It does not answer Q2's question, which is what protects the
margin.

**The judgment.** The castle the filing describes protects a seat at the bidding, not a price. The decisive facts are the
filing's own: the customer takes 1% to 3% a year by contract and may terminate for convenience to get more; competition is
"based primarily on price"; the industry "historically has had excess capacity"; new entrants from China are named; and the
product is hand-assembled by 129,000 hourly workers in the cheapest countries the business can find, the case the speakers name
plainly: "we do not want to buy into a business that has a very high labor content and that has a product that can be shipped
in from abroad very easily. Because, sooner or later, that will probably be trouble" **[M2007-116]**. The margin survives by
running ahead of the step-downs year after year, with restructuring every year: "A moat that must be continuously rebuilt will
eventually be no moat at all." **[L2007-005]**; and the one rival whose same business is on file across a cycle shows the
rebuilding failing, from 14% to 3%. The improvements in such a field go to the customer: "the improvement you get one day, your
competitor gets the next day. And it very much tends to work to the benefit of consumers but not to increase overall
profitability." **[M2004-053]**; "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. The
contrary evidence (the higher margin than Lear's, the high return on operating capital, the incumbency, the awards) is real and is
written above; it shows a well-run occupant of an open field, not a castle. "A truly great business must have an enduring "moat"
that protects excellent returns on invested capital." **[L2007-004]**; the filing shows what the customer does to the returns
each year, and no moat that stops it.

This is not a castle whose future cannot be judged (TOO HARD, **[M2000-019]**): the price behaviour, which the rows say tells the
most, "you learn a lot about the durability of the economics of a business by observing the behavior of" **[M2005-020]** (the
row's own dash elided), is written into the contracts and stated in the filing. It is shown open.

- **VERDICT: OUT.** The castle is open on the filing's own evidence: no pricing power (contractual step-downs, termination for
  convenience, competition primarily on price, excess capacity) **[M2005-020]**, **[M2010-092]**; high labour content in a
  product made wherever labour is cheapest **[M2007-116]**; a moat that must be rebuilt every year, which the field's one
  full-cycle record shows failing **[L2007-005]**; the customer, not the business, sets the terms **[M2017-009]**. "If the
  answer had been yes, we wouldn’t have done it." **[M2011-015]**. The box is OUT, not TOO HARD **[M2006-013]**. The file closes
  here; Q3 to Q12 are NOT REACHED as clearances, and what follows is written as facts found or under the heading COMPUTATION,
  NOT A CLEARANCE.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (Q2 closed the file OUT). Facts under AFTER THE STOP.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. Facts under AFTER THE STOP.
## Q5 — WHO RUNS IT. NOT REACHED. Facts under AFTER THE STOP; no integrity fact found.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED. Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? NOT REACHED as a STOP. The owner's reporting figures follow, as COMPUTATION, NOT A CLEARANCE.

### COMPUTATION, NOT A CLEARANCE
Q2 closed the file OUT; nothing below is a clearance, a verdict or entry language (operator rules 2 and 3). It is computed
because the owner's reporting convention asks for the two figures (Part VII, The owner's price), and it is built by Q7's range
convention as far as the filings allow. Script: `Test Runs/_research 2026-10-26 VGNT/q7_computation.py`.

- **Owner cash, all-equity basis** (before interest, after the company's own tax as the combined statements record it; the
  carve-out carried no borrowings, so its operating cash flow is before interest): operating cash flow, less all capital
  spending, less stock pay (added back in operating cash flow, a real cost **[L2021-003]**), less the noncontrolling interests'
  share of net income. Information statement, combined statements of cash flows and operations (`0001193125-26-096776`):

  | Year | Operating cash flow | Capital spending | Stock pay | Minority share | Owner cash | Depreciation variant (D&A in place of capital spending) |
  |---|---|---|---|---|---|---|
  | FY2023 | 180 | 244 | 25 | 29 | **-118** | -79 |
  | FY2024 | 707 | 206 | 28 | 26 | **447** | 451 |
  | FY2025 | 641 | 160 | 33 | 18 | **430** | 363 |

  ($ millions.) Working capital is inside operating cash flow, so specific (d) is met: the changes were -278, +93 and -85
  (sum of the changes in operating assets and liabilities). Acquisitions: none in the window (the FY2023 divestiture line is
  -17), so specific (c) does not arise.
- **The window.** Q7's convention asks for five years; three are on file for this business (Step 0). **CONVENTION of this run:
  the window is the three filed years, said so;** rationale: no filing separates the business before FY2023, and a five-year
  figure built from Aptiv's combined Signal and Power Solutions segment would carry the connector business's economics (26%
  gross margin against 12%) into a harness business.
- **Specific (a), the aberrational year.** FY2023 is the first year of the window and the filer describes it as aberrational:
  the UAW strikes "adversely impacted our financial condition, operating results and cash flows for the year ended
  December 31, 2023" and the semiconductor shortage did the same for "portions of the year ended December 31, 2023" (Risk
  Factors); its current tax charge was $384M (tax expense $144M less a deferred benefit of $240M, F-5 and F-8) against about
  $100M in each later year, and its working-capital draw was $278M. No full cycle is on file to average over, so the range is
  shown both ways: the literal window (average $253.0M) and the window with FY2023 removed (average $438.5M). **CONVENTION of
  this run:** where the cycle base of specific (a) cannot be built because no cycle is filed, the literal window is the bottom
  and the window without the aberrational year is the top; rationale: it shows the width the missing years leave, rather than
  choosing one.
- **Specific (b), growth.** Net sales $8,832M, $8,309M, $8,818M: compound growth of nil (-0.1% a year). The owner-cash series
  changes sign, so no growth rate between end years or halves is meaningful; by specific (b) the range is the no-growth case
  alone, said so. Every case below is the no-growth case: ten years at nil and then nil, which is a perpetuity at the
  sovereign. Specific (e): the filing gives no maintenance figure, so the all-spending case is central and the depreciation
  variant is beside it; with no growth case there is no growth spending to schedule (year one $0, year ten $0). Specific (f):
  no growth carried, so the cap does not bind.
- **The rate:** 5.33% (US Treasury 30-year par yield, 10/23/2026).
- **Net debt** at the latest filed date, June 30, 2026 (Q2 2026 10-Q, `0002078008-26-000018`, Note 10 and balance sheet):
  short-term debt $153M plus long-term debt $2,071M ($800M 6.125% notes due 2031, $800M 6.375% notes due 2034, Term Loan A
  due 2031, finance leases and other) less cash $554M = **$1,670M**. Operating leases left out (lease liabilities $144M long
  term), said so. Pension obligations of $214M left out of net debt by the convention and weighed under Q9 facts below. No
  subsequent event stated in that filing changes net debt (the $0.13 dividend declared August 3, about $9M, is not added).
- **The range, all-equity basis (central):** bottom $253.0M / 5.33% = $4,747M, less net debt $1,670M = $3,077M, **$43.43 a
  share**; top $438.5M / 5.33% = $8,227M, less $1,670M = $6,557M, **$92.57 a share**. Width 2.13 to 1 (under the three-to-one
  line). Depreciation variant beside: $41.32 to $84.22. Literal window shown (it is the bottom).
- **The floor, tested first** **[M2003-149]**. Enterprise value at the price: $2,932.6M + $1,670M = $4,602.6M. With no growth,
  the expected return is the owner-cash yield: 5.50% on the literal window and 9.53% on the window without FY2023. **No case on
  the central basis earns the floor of about ten percent at $41.40**; the better case falls just short of it and the literal
  window far short. By the convention this would close Q7 OUT whatever the width; the price also sits just below the bottom of
  a range narrower than three to one, which is no screamer: "It should scream at you." **[M2009-005]**. Equity-only beside (never decides
  alone): owner cash after interest at the Q2 2026 run-rate ($36M a quarter, $144M a year, $121M after tax at the H1 2026
  effective rate of 16%) is $132.0M and $317.5M, a yield of 4.50% and 10.83% on the market value of $2,932.6M; range $34.97 to
  $84.10 a share.
- **VALUE RANGE (reporting figure, all-equity basis): $43.43 to $92.57 a share, against $41.40.**
- **FAIR PRICE (reporting figure, Part VII):** each end case valued at ten percent instead of the long rate, the two averaged,
  less net debt, per share, after the company's own tax: ($2,530M + $4,385M) / 2 = $3,457.5M, less $1,670M = $1,787.5M,
  **$25.23 a share on the all-equity basis (central)**; **$31.73 a share on the equity-only basis** (beside). Not a regulated
  utility, so the all-equity figure is central. No cheap price is reported.
- **What the computation leaves out, said so:** the carve-out's allocated corporate costs against a stand-alone company's own
  (separation costs ran $48M in H1 2026, Q2 2026 10-Q); the 2023 tax charge's cause (not traced); the H1 2026 owner cash
  ($194M operating cash flow less $117M capital spending, $19M stock pay and $1M minority share = $57M for a seasonally weak
  half, not annualized).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED. Fact under AFTER THE STOP.
## Q9 — COULD IT RUIN US. NOT REACHED. Facts under AFTER THE STOP.
## Q10 — IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED; not asked.

---
## THE BOX
**OUT**, decided at **Q2** (the castle shown open on the filing's own evidence: contractual price step-downs of 1% to 3% a year,
termination for convenience, competition primarily on price, high labour content, a moat rebuilt every year that the field's
one full-cycle record shows failing). COMPUTATION, NOT A CLEARANCE: value range $43.43 to $92.57 a share (all-equity,
no-growth, three filed years) against $41.40; fair price $25.23 (all-equity, central), $31.73 (equity-only). No integrity fact
found.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2), each with its source **[M1997-127]**.)*

**Bearing on Q2 (found after the verdict was written).** The Q2 2026 10-Q's bridge of net sales and Adjusted EBITDA from Q2 2025
to Q2 2026 shows "Pricing" of -$18M on net sales and -$18M on Adjusted EBITDA for the quarter (accession `0002078008-26-000018`,
MD&A): the step-downs at work in the first quarter reported after the spin.

**Bearing on Q3 (capital).** Operating capital the business needs (receivables, inventories, other current assets, property,
other long-term assets, less payables, accrued liabilities and other long-term liabilities; operating leases, deferred taxes,
affiliates and cash left out): $1,267M at December 31, 2024 and $1,278M at December 31, 2025 (information statement, F-7).
GAAP operating income on it: $457M (36% pre-tax) and $534M (42% pre-tax). Payables to suppliers ($1,530M at year-end 2025)
fund nearly all of receivables ($1,567M). Capital spending $244M, $206M, $160M against depreciation of $193M, $200M, $226M;
capital expenditures in accounts payable $87M, $52M, $72M. The filing calls the industry "generally capital intensive". Sales
flat over the three years: no growth to measure the return on added capital against **[M2001-019]**.

**Bearing on Q4 (the accounts).** The eight to ten years of balance sheets **[M2025-032]** do not exist for this business:
two combined year-ends (2024, 2025) and two quarter-ends of 2026 are on file. What moved: total equity from $1,848M (December
31, 2025) to $284M (June 30, 2026), of which Versigent's $85M, because a $1,894M dividend was paid to the former parent out of
$2,063M of new borrowing (Q2 2026 10-Q, cash flow statement and Note 3); deferred tax assets $384M to $443M; pension
obligations from $72M (2024) to $217M (2025) when shared plans were legally split and allocated to Versigent in the fourth
quarter of 2025 (Q2 2026 10-Q, Note 2). The information statement features "Adjusted Operating Income" beside GAAP throughout,
and the 10-Q's MD&A explains results by "Adjusted EBITDA" (EBITDA $387M, Adjusted EBITDA $475M for H1 2026, adding back
restructuring of $46M and separation costs of $48M); restructuring has recurred every year (FY2023 $48M, FY2024 $101M, FY2025
$86M). These would be recorded at Q4 as a weighing against **[M1998-086]**, **[L2016-006]**, and carried to Q5. The 2026
earnings press releases (exhibits to the 8-Ks of 2026-05-05 and 2026-08-04) were not fetched, so whether the company gives
guidance was not checked. The auditor's critical audit matters were uncertain tax positions ($67M) and revenue recognition of
customer price reductions and upfront customer payments ($33M capitalized) (information statement, F-2 to F-4).

**Bearing on Q5 (the people).** Chief executive Joseph T. Liotine, at Aptiv from April 2024 (president, Signal and Power
Solutions; president, EDS from November 2024), previously chief executive of Briggs & Stratton and about twenty years at
Whirlpool (Aptiv FY2025 10-K, executive officers). No integrity fact was found in the documents read; no proxy has been filed,
so the proxy tests were not run.

**Bearing on Q6 (the money).** The spin loaded the business with $2.2 billion of debt to pay its former parent $1,894M (above).
In April 2026 the board authorized repurchases of up to $250M "from time to time", with no stated price **[L2016-002]**; a
quarterly dividend of $0.13 a share was declared on August 3, 2026 (Q2 2026 10-Q, Note 14). The information statement's
strategy is to "selectively pursue M&A". Executive pay under Aptiv's plans: annual incentive 70% financial and 30% strategic
goals; performance shares with a relative total shareholder return modifier of plus or minus 20%; target pay set on "market
data" (information statement, Executive Compensation).

**Bearing on Q8 (alternatives).** The long Treasury yields 5.33%; the better of the two no-growth cases yields 9.53% on
enterprise value at the price.

**Bearing on Q9 (debt and exposures).** Net debt $1,670M at June 30, 2026; interest $36M in Q2 2026. Operating income of
$534M (FY2025) and $457M (FY2024) against about $144M of annual interest is cover of 3.7 and 3.2 times on pre-tax operating
income **[M1995-104]**; the senior notes mature in 2031 and 2034 and the term loan amortizes quarterly to 2031 **[L2010-020]**.
Pension obligations $214M. Five customers 65% of sales; requirements contracts with no minimum volumes, terminable for
convenience; warranty "coterminous with the warranty offered by the OEM" and a possible share of recall costs (information
statement, Business and Risk Factors). The "little or no debt" criterion **[R1997-001]** would not be met by a whole-business
buyer.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `2a0451cd`, before the first EDGAR request); written question by
      question; committed after Step 0 and Q1, after Q2, and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits and states that the dispatching session holds the lock and
      folds the run; the fold is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed for this company or searched; one directory
      listing of `Test Runs/` showed other runs' file names, declared under Contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `Test Runs/_research 2026-10-26 VGNT/check_ids.py`); every
      filing fact carries its accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run OUT; nothing after it is a clearance, and the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost, from operating cash flow less all capital spending, stock pay and the minority share,
      never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (Foundations; Q2's contrary paragraph); facts for later questions
      under AFTER THE STOP. No integrity fact found, so the box line carries no integrity flag.
- [x] Not a point-in-time run; no anchor-date bar applies.
- [x] `tools/run.py` printed no arithmetic lines ("UNRESEARCHED", no annual facts); nothing it printed was used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message of the close).
- **Short of the template, said so:** Q4's eight to ten years of balance sheets could not be read (two year-ends exist); Q7's
  five-year window is three years (CONVENTION of this run, above); the earnings press releases and the Aptiv FY2018 segment table
  were not read; the three non-SEC rivals' costs could not be read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **A spin-off with less than five filed years.** Q7's range convention and specific (a) assume a five-year
window and, where an end year is aberrational, a full cycle to average over; neither exists for a business carved out of a
parent that reported it only inside a larger segment. The framework does not say whether to build the missing years from the
parent's combined segment (which would import another business's economics), to shorten the window, or to close TOO HARD (WORK)
on the window. This run shortened the window and showed the aberrational year both in and out, each a CONVENTION of this run;
a rule is needed. (2) **Q2's "field's returns over the last full cycle" when the filer itself has no cycle on file.** Section C
asks for the filer's and the rivals' filings over the cycle; here only one named rival files with the SEC, and its segment mixes
harnesses with connectors and electronics. The run leaned on the filing's own statements of its price terms (which need no
cycle) and used the rival's cycle as corroboration, not as the decider; the text does not say how much a single rival's cycle
may carry when the other named rivals are not SEC filers. (3) **The floor's "about".** The better no-growth case yields 9.53%
on enterprise value; the convention says "about ten percent" and the floor test closes OUT where "no case" earns it. Whether
9.5% is "about ten" is not stated; it did not matter here (Q2 had closed the file, and the literal window yields 5.5%), but it
will matter in a run where it decides. Also noted: the brief's instruction to commit "after each question" sits awkwardly with
a file that closes at Q2, where Q3 to Q9 become one AFTER THE STOP section; it was committed as one closing step.
