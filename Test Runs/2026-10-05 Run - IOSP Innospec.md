# Company Run — Innospec Inc. (NASDAQ: IOSP) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (the
template copy and the research folder were made before the first EDGAR call).

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched blind: `PORTFOLIO.md`, holding
reviews, the resume-state file, the queue register and the prepped reading list were not opened, and no attempt was made to
learn whether anyone holds or wants this name.

**CONTAMINATION, declared.** (1) The session's opening context listed recent commit subjects naming the boxes of other
v5 runs (CTS, MOV, DBD, RES); none concerns Innospec, and they were not used. (2) `tools/run.py` printed v4 material and a
stale owner-earnings table (FY2013 to FY2015); only its price, share count and balance-sheet arithmetic were read, and every
balance-sheet figure used below was checked against the filed statements. (3) The auto-memory index loaded at start-up
carries a general line about the queue ("nothing buyable"); it names no company and was not used. (4) No other `Test Runs/`
file about Innospec exists (a directory listing found none), and none of today's other run files was opened.

Working folder: `Test Runs/_research 2026-10-05 IOSP/` (filings as text, `arith.py` with every input and sum,
`ledger_rows.txt` with the full text of every row cited).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $98.17 (2026-10-05; live quote through `tools/run.py`, an aggregator, **flagged** under operator rule 5).
  Context, from the filing: the company itself bought 86,826 shares in April 2026 at an average $73.8 (10-Q, 2026-08-05,
  accession 0001193125-26-334178, Part II Item 2).
- **Shares:** 24,631,047 common, one class, cover of the 10-Q for the period ended 2026-06-30, filed 2026-08-05, accession
  0001193125-26-334178 (`python Screens/cover_shares.py IOSP`; the dei cover tag reads the same figure as of 2026-07-31).
- **Market cap:** 24.631M x $98.17 = **$2,418.0M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-18, accession 0001193125-26-056502: Items 1, 1A, 3, 5, 7,
  7A, the statements, Notes 2, 6, 9); 10-Q Q2 2026 (filed 2026-08-05, accession 0001193125-26-334178: statements, segment
  MD&A, Part II Item 2); DEF 14A 2026 (filed 2026-03-26, accession 0001174947-26-000427: ownership, CD&A, Summary
  Compensation Table, pay-versus-performance); 8-K 2026-08-04 (accession 0001193125-26-333724, Item 2.02 cover only; the
  Ex. 99.1 release was not read) and 8-K 2026-06-02 (accession 0001193125-26-257531, a new director). For the ten-year record,
  the segment tables and cash-flow statements of the 10-Ks for FY2011 (0001193125-12-067402), FY2013 (0001193125-14-050831),
  FY2015 (0001193125-16-466575), FY2016 (0001193125-17-045109), FY2017 (0001193125-18-047390), FY2018
  (0001193125-19-044946), FY2019 (0001193125-20-041516), FY2020 (0001193125-21-046094), FY2021 (0001193125-22-044144),
  FY2022 (0001193125-23-044405) and FY2023 (0000950170-24-014960).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$138.3M** in
  the filed Consolidated Statement of Cash Flows (10-K FY2025, p. 53) equals the XBRL fact (138.3). A tag defect found in the
  other direction: the XBRL `Goodwill` fact for FY2025 reads 2.0 and `tools/run.py` prints it for 2025-07-31; the filed
  balance sheet says **$399.0M**. The filed figure is used.
- **Capital spending is untagged in XBRL after FY2015**, so every capex and software figure below was read from the filed
  cash-flow statement of the 10-K that first reported it.
- `tools/run.py IOSP`: arithmetic lines only (price, shares, cap, the balance-sheet table). Its owner-earnings table uses
  FY2013 to FY2015 and is not used (Part VII, the tooling).

### Owner cash, ten years, from the filed cash-flow statements ($M)
Owner cash = operating cash flow, less capital expenditures, less internally developed software (the new ERP system,
capitalised), plus disposal proceeds, less stock compensation (added back in operating cash, but a real cost:
"all forms of compensation" **[L2021-003]**; "the most egregious example" **[L2015-003]**). Acquisitions are shown apart.

| FY | OCF | Capex | Software (+intangible bought) | SBC | D&A | **Owner cash** | OCF − SBC − D&A (depreciation variant) | (Capex+software) / D&A | Acquisitions |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 104.5 | 16.5 | 0.0 | 3.3 | 38.1 | **84.7** | 63.1 | 0.43 | 197.4 |
| 2017 | 82.7 | 23.3 | 4.7 + 4.2 | 4.1 | 50.4 | **46.4** | 28.2 | 0.64 | (2.6) |
| 2018 | 104.9 | 28.9 | 1.2 | 4.9 | 49.6 | **69.9** | 50.4 | 0.61 | 5.4 |
| 2019 | 161.6 | 29.9 | 1.1 | 6.6 | 47.6 | **124.0** | 107.4 | 0.65 | 0 |
| 2020 | 145.9 | 29.7 | 0.0 | 5.8 | 46.0 | **110.4** | 94.1 | 0.65 | 0 |
| 2021 | 93.2 | 39.1 | 0.0 | 4.4 | 42.7 | **52.6** (incl. 2.9 proceeds) | 46.1 | 0.92 | 0 |
| 2022 | 81.7 | 39.6 | 2.7 | 6.7 | 40.1 | **32.9** | 34.9 | 1.05 | 0 |
| 2023 | 207.3 | 62.1 | 15.1 | 8.0 | 39.3 | **122.2** | 160.0 | 1.96 | 34.7 (QGP) |
| 2024 | 184.5 | 41.4 | 20.9 | 8.5 | 43.5 | **114.2** | 132.5 | 1.43 | 0.2 |
| 2025 | 138.3 | 50.3 | 25.2 | 8.1 | 43.6 | **55.8** | 86.6 | 1.73 | 0.7 |

- **Five-year average FY2021–FY2025: $75.5M** (capital-spending basis); **$92.0M** on the depreciation variant. The
  previous five years averaged **$87.1M**. Net of the after-tax interest earned on the cash pile (average $2.8M, counted
  separately as cash): **$72.8M** and **$89.3M**.
- The company's own line agrees with the 2025 cash figure before stock pay: "cash from operations after capital expenditures
  remained strong at $63.9 million" (10-K FY2025, Executive Overview), which is 138.3 − 50.3 − 25.2 + 1.1.
- Against the earnings-based figure the company features, adjusted pre-tax income $177.5M (FY2025) and $204.1M (FY2024)
  "adjusted for stock compensation" among other items (10-K FY2025, MD&A, income taxes), owner cash runs at about half.
  The gap is working capital and capital spending above depreciation, read at Q3/Q4 below.

### The balance sheets first, ten year-ends (filed statements; $M) **[M2025-032]**
*(Q4 is not reached, since the run closes at Q2; the template asks that the balance sheets be read in Step 0 in that case.)*

| Year-end | Total assets | Equity (Innospec) | Goodwill | Other intangibles | Cash | Debt | Receivables | Inventory | Net PP&E | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,181 | 654 | 375 | 144 | 102 | 269 | n/r | n/r | 157 | n/r |
| 2017 | 1,410 | 794 | 362 | 163 | 90 | 218 | 244 | 210 | 196 | 605 |
| 2018 | 1,473 | 825 | 365 | 136 | 123 | 208 | 280 | 248 | 196 | 668 |
| 2019 | 1,469 | 918 | 363 | 114 | 76 | 59 | 292 | 245 | 199 | 756 |
| 2020 | 1,397 | 944 | 371 | 75 | 105 | 0 | 221 | 220 | 211 | 759 |
| 2021 | 1,571 | 1,032 | 364 | 58 | 142 | 0 | 284 | 278 | 214 | 823 |
| 2022 | 1,604 | 1,038 | 359 | 45 | 147 | 0 | 335 | 373 | 221 | 924 |
| 2023 | 1,707 | 1,147 | 399 | 57 | 204 | 0 | 360 | 300 | 268 | 1,028 |
| 2024 | 1,735 | 1,211 | 383 | 65 | 289 | 0 | 342 | 301 | 270 | 1,025 |
| 2025 | 1,832 | 1,326 | 399 | 68 | 292 | 0 | 342 | 329 | 286 | 1,099 |
| 2026-06-30 | 1,846 | 1,343 | 398 | 65 | 250 | 0 | 409 | 337 | 293 | 1,138 |

(n/r: not read for 2016. 2017 to 2025 from `tools/run.py`'s first-filed XBRL vintage, each spot-checked against the filed
balance sheets of the 10-Ks listed above; June 2026 from the 10-Q.)

**What the figures say.** (1) **Debt went to zero and stayed there.** The $269M borrowed for the 2016 Huntsman surfactants
purchase was repaid by 2020; since then the revolver ($250M, to May 2028) has been undrawn (10-K FY2025, Liquidity). (2)
**Goodwill is the largest asset after working capital and has not been written down**, $375M in 2016 to $399M in 2025;
acquired intangibles amortised from $163M (2017) to $45M (2022) and rose again with QGP in December 2023. Tangible equity
2025: 1,326 − 399 − 68 = **$859M**, of which $292M cash. (3) **Working capital rose with sales and stayed up.** Sales
$1,306.8M (2017) to $1,778.0M (2025), +36%; receivables +40%, inventory +57%. Inventory days in Fuel Specialties rose from
113 to 133 (FY2025) and to 144 (June 2026), the company saying it holds stock "to manage the risk of potential supply chain
disruption" (10-Q, Liquidity). That is the "inventories look out of line ... with sales" pattern of **[M1995-064]** in a mild
form, with a stated reason; no prepaid or deferred account is building (prepaid expenses fell from $21.0M to $13.3M). (4)
**Equity doubled ($654M to $1,326M) while owner cash did not rise** (table above): the retained dollars went into working
capital, plant (net PP&E $157M to $293M), an ERP system ($63.9M capitalised 2022 to 2025 and "now complete", 10-Q Note on
software) and acquisitions ($235.8M, 2016 to 2025). (5) **The legacy of the lead business is on the balance sheet:** plant
closure provisions $65.1M "primarily connected to the production of tetra ethyl lead" at Ellesmere Port, the auditor's one
critical audit matter (10-K FY2025, pp. 30 and 48). (6) **The UK defined-benefit pension was bought out in 2024**, a
$155.6M settlement charge, largely non-cash; pension liabilities now $12.7M. (7) **What the figures cannot say:** how much of
Fuel Specialties' profit comes from AvGas tetra-ethyl lead, a product the company calls the world's only source of and whose
use regulators intend to end (below). No segment balance sheet is shown in the parts read.

---
## THE FOUNDATIONS (not a gate)
A share is a business; the market here serves and does not instruct: the price moved from the company's own April buying at
$73.8 to $98.17 in six months, and "it doesn’t tell us anything. It just tells us prices." **[M2006-077]**. The margin of
safety bears at Q7: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**.
The analyst's habits govern the method: look "for what’s wrong in things" **[M2025-013]**, and treat the competitors' own
filings as the scuttlebutt aimed "to possibly reject your original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The company's history: as Octel it made tetra-ethyl lead; in 2010 it settled US and UK investigations into "legacy
   transactions" under the UN Oil for Food Program, the FCPA, the Cuban Assets Control Regulations and UK anti-bribery law,
   $40.2M of fines, penalties and disgorgements plus a compliance monitor to 2013; in 2011 it paid NewMarket/Afton, a direct
   competitor, about $45.0M to settle two civil actions (10-K FY2011, accession 0001193125-12-067402, Notes). Recorded here
   because Q5 is not reached.
2. Owner cash has not grown in ten years (five-year averages $87.1M then $75.5M) while equity doubled and sales rose 36%.
3. Performance Chemicals gross margin fell 4.8 points in 2025 "primarily due to pricing erosion" (10-K FY2025, MD&A).
4. Oilfield Services lost its largest customer's business: one customer was 13.6% of group sales in 2023 ($265.2M); in 2025
   "the absence of production chemical activity in Mexico", and $22.9M of plant and $19.1M of intangibles impaired in Q3 2025
   (10-K FY2025, Item 1, MD&A, Notes 6 and 9).
5. The December 2023 QGP acquisition (Brazil, Performance Chemicals) had its intangibles impaired within two years, and its
   earn-out liability has been written down twice ($15.9M credit in 2025, $4.6M in H1 2026), which means the business is
   earning less than the price assumed.
6. AvGas: the world's only TEL for aviation fuel sits inside Fuel Specialties, and the US government-industry programme aims
   "to eliminate lead emissions from general aviation in the U.S. by the end of 2030"; EU users are authorised to April 2032
   (10-K FY2025, Item 1A). Its size is not disclosed.
7. A competitor, in its own filing, calls the fuel additives submarket "characterized by more competitors" than lubricant
   additives and names Innospec among six or more rivals in each part of it (NewMarket 10-K FY2025, accession
   0001282637-26-000005, Item 1, Competition).
8. A $23.9M FY2025 buyback and a new $75M authorisation (May 2026) state no price above which purchases stop.
9. Corporate costs rose in H1 2026 partly on "higher legal and compliance expenses" (10-Q, Other Income Statement Captions);
   the cause is not stated.

## THE STANDING RULE
Owning a marketable share of a debt-free company, bought with cash and without borrowing, puts the buyer at no risk of ruin
from this name: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; the buyer's financing and sizing are
the buyer's own and are not set here **[M2012-081]**. Clear.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test:** "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
**[M2012-065]**; the key variables and "how predictable they were first" **[M1998-044]**; the chemistry need not be understood,
"What is important is that I understand the economic dynamics of the industry" **[M2011-014]**, said of petroleum additives.

Three businesses, read by their parts (10-K FY2025, Note 3 and MD&A; five-year average segment operating income FY2021–FY2025
in brackets):
- **Fuel Specialties** (sales $701.5M, operating income $144.8M in 2025; [$122.1M, 52%]). Additives for diesel, jet, marine
  and heating fuels sold to refiners, fuel marketers and terminals; plus AvGas TEL. Key variables: fuel volumes, emission and
  fuel-quality rules, renewable-diesel compatibility, raw-material pass-through, and the end date of leaded aviation fuel.
  These are slow-moving and written down by the industry itself (NewMarket names "total vehicle miles driven, fuel economy,
  the introduction of new engine designs, regulations on emissions" as the drivers). The direction of each is foreseeable;
  the size of the AvGas piece is not disclosed.
- **Performance Chemicals** (sales $681.4M, operating income $61.0M; [$72.9M, 31%]). Surfactants, emollients and other
  ingredients for personal and home care, agriculture, mining, construction; markets the company calls "highly fragmented"
  with "substantial competition". Key variables: oleochemical costs and what large customers will pay. Predictable in kind:
  a competitive ingredients business.
- **Oilfield Services** (sales $395.1M, operating income $23.3M; [$38.6M, 17%]). Drilling, completion and production
  chemicals and drag-reducing agents. Key variables: oil-company activity, and one Mexican production-chemicals customer
  whose business came and went. Not predictable year to year; its size in the whole is bounded and can be valued low.

No part turns on fast-moving technology; the insiders do write their drivers down (test 5, **[M2000-105]**). The ten-year
economics of each part can be described; what cannot yet be stated is how much of the protected part is a product with a
regulatory end date, which is a question about the castle (Q2), not about whether the business can be understood. The doubt
rule was applied **[M2002-092]**: the doubt found is about durability and size, not about how the money is made.

**VERDICT: IN.** The economics of all three parts are understood at the level **[M2011-014]** asks; the open question passes
to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now. What are the key factors? And how permanent are they?" **[M1995-038]**. Read part by part, because the parts
answer differently.

**Segment operating margins, from the filed 10-K segment tables** (accessions in Step 0; operating income / sales):

| FY | Fuel Specialties | Performance Chemicals | Oilfield Services | Octane Additives (auto TEL, run-off) |
|---|---|---|---|---|
| 2011 | 15.7% | 12.8% | n/a | loss |
| 2013 | 16.3% | 12.3% | n/a | 36.4% |
| 2015 | 19.2% | 10.5% | 3.4% | 41.5% |
| 2016 | 21.7% | 11.5% | loss | 52.3% |
| 2017 | 20.6% | 7.8% | 3.1% | 45.2% |
| 2018 | 20.2% | 9.5% | 5.5% | 29.4% |
| 2019 | 20.0% | 11.4% | 8.3% | loss |
| 2020 | 16.5% | 12.9% | loss | ended |
| 2021 | 16.9% | 13.5% | 3.1% | |
| 2022 | 16.7% | 14.9% | 7.0% | |
| 2023 | 15.8% | 9.7% | 11.4% | |
| 2024 | 18.5% | 12.7% | 7.9% | |
| 2025 | 20.6% | 9.0% | 5.9% | |
| H1 2026 | 20.2% | 7.5% | 6.6% | |

**The competitor row** (same metric, each competitor's own filing):

| Competitor | Metric | Figures | Source |
|---|---|---|---|
| NewMarket (Afton), petroleum additives | segment operating margin | 13.6% (2018), 16.5% (2019), 16.7% (2020), 19.1% (2023), 22.5% (2024), 20.5% (2025) | 10-K FY2020, 0001282637-21-000004; 10-K FY2025, 0001282637-26-000005 |
| NewMarket (Afton), fuel additives sales | net sales | $410.0M (2018), $397.4M (2019), $314.9M (2020), $394.3M (2023), $389.9M (2024), $377.6M (2025) | same |
| ChampionX, Production Chemical Technologies | segment operating margin | 10.2% (2022), 14.6% (2023), 15.9% (2024) | 10-K FY2024, 0001723089-25-000025 (acquired by SLB, July 2025; no later filing) |
| Lubrizol (Berkshire) | not broken out | 2025 revenue $6.2B, pre-tax earnings down 20.6%; dollar earnings not disclosed | Berkshire 10-K FY2025, 0001193125-26-083899 |
| Croda, Consumer Care | adjusted operating margin | 17.4% (2024), 17.5% (2025) | **non-SEC, flagged**: Croda results release of 24 Feb 2026, read through a web search summary, not from the filed accounts |

**Fuel Specialties, the castle tests.**
- *Return held through the cost cycle.* Gross margin 35.0% (2019), 31.2% (2021), 30.4% (2022), 30.9% (2023), 34.2% (2024),
  36.0% (2025): the raw-material surge of 2021–2022 was passed through and the margin regained, which is what "over time the
  businesses with strong competitive positions manage to pass through increases in raw material costs" describes
  **[M2005-017]**. Prices also fell with costs (2024 Americas price and mix −11%, the 10-K saying "resulting from lower raw
  material costs"). So the record shows pass-through both ways; it shows no price raised ahead of cost, the test of "the
  agony they go through in determining whether a price increase can be sustained" **[M2005-020]**.
- *Ask the competitors* **[M1999-130]**. NewMarket's filing places Innospec among the named rivals in gasoline detergents
  and in diesel and refinery additives and says the fuel submarket "is characterized by more competitors" than lubricant
  additives, where it names only Lubrizol, Infineum and Oronite. Innospec's own filing: "a small number of competitors, none
  of which hold a dominant position" (10-K FY2025, Item 1). Afton's fuel-additive sales fell 8% from 2018 to 2025 while
  Innospec's Fuel Specialties sales rose 22% ($574.5M to $701.5M): on this one metric Innospec held its place better than the
  competitor who reports it.
- *The money test and the Lubrizol rows.* The speakers found Lubrizol's moat in "the relatively low cost of what Lubrizol
  brings to the party", "a connection with customers" and work with customers "when new engines come along" **[M2011-016]**,
  in "very small markets that aren’t really too attractive to anybody with any sense to enter" **[M2011-017]**; and Buffett judged entry "could I
  do it?" **[M2011-015]**. Those rows were said of lubricant additives, where engines are co-developed with OEMs. Fuel
  additives are sold mainly to refiners and fuel marketers to meet "customer, industry, OEM, and government specifications"
  (NewMarket, Item 1): the low cost to the customer and the service tie carry over; the OEM engine lock-in is not shown in
  any filing read. Innospec names its edge as "technical development capacity, independence from major oil companies and
  strong long-term customer relationships".
- *What could destroy, modify or reduce it* **[M2000-014]**. (a) AvGas: the only TEL maker for aviation fuel, with a US aim to
  end leaded avgas by end-2030 and EU authorisation to April 2032; the company says only that, if a replacement is approved,
  "future operating income and cash flows ... would be adversely impacted". Its MD&A has named "the higher margin contribution
  from AvTel" as a driver of segment margin (10-K FY2016 and FY2017). How much of the 20.6% margin is AvGas is not disclosed
  anywhere read. (b) Road-fuel volumes under electrification, slow, inside the horizon. (c) Widening or narrowing
  **[M1999-108]**: margins and share above say holding or widening; the AvGas end date says a piece of it ends inside ten
  years.

**Performance Chemicals: the castle shown open on the evidence.** "pricing erosion and higher demand for our lower margin
products" cut gross margin from 22.7% to 17.9% (2025); 2024 price and mix −8% "driven by lower raw material costs, together
with the greater demand from consumers for lower priced products"; gross margin swung between 17.9% and 31.3% across the
decade; operating margin 7.8% to 14.9%, against Croda's Consumer Care at 17.5% (flagged). The company's own word for the
markets is "highly fragmented". The customer here buys on price and the price follows the raw material, which is the
commodity mark of **[L2004-003]**; Innospec is not shown to be the low-cost producer that alone prospers in such a field
**[L2000-017]**, **[M1997-010]**.

**Oilfield Services: the castle shown open on the evidence.** Margins 3% to 11% with losses in 2016 and 2020, about half of
ChampionX's production-chemicals margin in the same years (7.0%/11.4%/7.9% against 10.2%/14.6%/15.9%); a fragmented market
with "a small number of very large competitors" (Item 1), one of them a Berkshire company in drag-reducing agents
(LiquidPower, Berkshire 10-K FY2025, Item 7); the loss of one customer took segment sales from $691.3M to $395.1M in two years
and forced impairments. "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; the scale leader
earns about twice the margin, and "you do not want to have something whose competitive position is going to erode over time"
**[M2007-117]**.

**How the parts add up.** About half of the five-year segment income (Performance Chemicals and Oilfield Services, 48%)
comes from parts whose castles are open on the evidence; they can be valued as ordinary businesses at an ordinary price, but
they do not carry a moat. Whether the whole has a castle therefore turns on Fuel Specialties alone, and that turns on one
knowable fact the filings withhold: how much of Fuel Specialties' operating income is AvGas TEL, a sole-source product with a
stated end date inside the ten-year horizon, and whether the rest of the segment holds its margin and share against the field
NewMarket describes. If AvGas is small, Fuel Specialties is the kind of castle **[M2011-016]** describes, narrower; if large,
the castle "must be continuously rebuilt" **[L2007-005]** around a dated monopoly. "when we see a moat that’s tenuous in any
way ... We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**. The castle is not shown open
(that would be OUT, **[M2011-015]**), and its future cannot yet be judged.

**Cause of the box.** The deciding question is knowable and important **[M2006-076]**: the company knows its AvGas profit;
management may have spoken to it; the regulatory record and the competitor's filings are public. The work is not done: "I
haven’t done the work and I’m not sure if I did the work I would understand them." **[M1994-026]**. This is the reader's
cause, not the industry's **[L1993-023]**; the insiders would write the forecast down (**[M2000-105]**, test 5 of Q1).

**VERDICT: TOO HARD (WORK)** **[M2006-013]**. The run closes here. Research-pass steps 1 and 2 are written at the end; the
pass itself is not run in this file.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED. (Facts gathered for the research pass, no weighing: capital plus software spending ran 0.43 to 0.65 times D&A
in 2016–2020 and 0.92 to 1.96 times in 2021–2025; owner cash averaged $87.1M then $75.5M while equity rose from $654M to
$1,326M; "there’s your profit sitting in the yard" **[M2008-036]** is the pattern the research pass must test.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0. (Facts recorded, no verdict: the company features "adjusted" pre-tax
income and an "adjusted effective tax rate" that add back stock compensation; it reports the non-GAAP measures with
reconciliations; one tell, adjusted earnings featured, and no second tell was found in the parts read.)

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED (operator rule 2: no Q5 output while Q2 is not IN). Facts recorded for whoever reaches it: CEO Patrick S.
Williams since April 2009, previously head of Fuel Specialties, appointed as the 2010 FCPA/Oil-for-Food settlement was being
reached (DEF 14A 2026; 10-K FY2011); he owns 172,730 shares directly (DEF 14A 2026, ownership table); a separate,
independent chairman; CEO total pay $7.30M (2023), $13.22M (2024), $8.25M (2025) (Summary Compensation Table).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (Facts recorded: dividends $15.9M (2016) to $42.4M (2025), raised every year; buybacks small until $23.9M in
2025 and $13.5M in H1 2026 at about $74, under programmes that name an amount and a period but no price; acquisitions
$235.8M over ten years, the largest the 2016 Huntsman surfactants purchase ($197.4M); long-term incentives pay on relative
TSR (40%), revenue growth (20%) and EPS growth (40%), with 25% vesting at EPS growth of −10% against 2024 (DEF 14A 2026,
CD&A): a scale that pays on a decline, the shape **[M1999-018]** names, for whoever weighs it.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. Reported at the owner's request, all three figures:

### COMPUTATION — NOT A CLEARANCE
*Made after the closing STOP; it carries no entry language and clears nothing.*

Built by the Q7 CONVENTION (five-year average owner cash after every real cost, carried at the growth shown and capped by
Q3, ten years then zero nominal growth, discounted at the long government rate; the ends are the no-growth and shown-growth
cases) **[L2000-021]**, **[L2000-024]**. Inputs: sovereign 5.63%; balance-sheet adjustment at 2026-06-30 = cash $250.2M,
no debt, less plant closure provisions $64.7M and pension liabilities $12.7M = **+$172.8M**; 24.631M shares.

- **Growth shown.** On the aggregate owner cash, none: the 2021–2025 average ($75.5M) is below the 2016–2020 average
  ($87.1M). On segment operating income, about 3.3% a year (FY2017 $176.5M, four segments, to FY2025 $229.1M). The top end
  uses the 3.3%, the most the record shows on any measure, on the depreciation variant; it ignores the AvGas end date, so it
  is generous.

| Case | Cash input | Growth, yrs 1–10 | Operating value | Per share |
|---|---|---|---|---|
| **Bottom**: capital-spending basis, no growth | $72.8M | 0% | $1,293M | **$59.49** |
| depreciation basis, no growth | $89.3M | 0% | $1,585M | $71.38 |
| capital-spending basis, 3.3% | $72.8M | 3.3% | $1,679M | $75.19 |
| **Top**: depreciation basis, 3.3% | $89.3M | 3.3% | $2,059M | **$90.63** |

- **(a) VALUE RANGE: $59.49 to $90.63 a share, against $98.17.** Width about 1.5 to 1, inside the three-to-one line, so by
  the convention this range would not close TOO HARD; the price sits **above the top of the range**, which closes OUT through
  the floor convention if the question were open.
- **(b) FAIR PRICE: about $61 a share.** Rule: the price at which the expected return on the central case equals the floor of
  about ten percent pre-tax (CONVENTION, Q7; **[M2003-149]**, **[L2002-020]**, **[M1994-004]**). After-tax equivalent used:
  **7.6%** = 10% x (1 − 0.241), the company's FY2025 adjusted effective tax rate, since owner cash is after the company's tax;
  the 2002 row itself translates 10% pre-tax to "6�-7% after corporate tax" at the higher tax rate of its day **[L2002-020]**.
  Central case: cash $81.0M (midway between the two bases) growing 1.5% a year (half the operating-income growth, discounted
  for the AvGas end date; my judgment, labelled as such). Operating value = 81.0 / (0.076 − 0.015) = $1,328M; plus $172.8M;
  / 24.631M = **$60.93**. The fair price falls just above the bottom of the range.
- **(c) CHEAP PRICE: about $40 a share.** Rule (CONVENTION, mine, for this report): two-thirds of the bottom of the range,
  $59.49 x 2/3 = **$39.66**, so that the buyer stands "at a big discount from that present value calculated using the
  risk-free interest rate" **[M1997-126]** and the price is "startlingly low in relation to value" **[L2000-025]** on the
  most conservative case; at $40 the no-growth capital-spending case yields about 9.0% after the company's tax, which needs no
  pencil **[M2009-005]**. The one-third is my figure, not a row's.
- **At $98.17** the market value is $2,418M; owner cash ($75.5M) is a 3.1% yield against a 5.63% bond. Even the
  company's adjusted earnings basis (about $135M after tax at its 24% rate, stock pay deducted) would yield about 5.6%, level
  with the bond.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED. (Computation only: at $98.17 the owner-cash yield of 3.1% is below the 30-year Treasury's 5.63%.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. (Facts recorded: no debt; cash $250.2M of which $131.4M held outside the US; covenants on an undrawn revolver;
legacy lead-site obligations $64.7M; ethylene for one German operation is effectively single-source by pipeline, about 4% of
sales.)

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT ASKED. (For the record only: the company still sells tetra-ethyl lead for aviation fuel, a legal product with no current
replacement, which the newspaper test of Q12 would have to weigh.)

---
## THE BOX
**TOO HARD (WORK), at Q2.** Two of the three businesses (about half the profit) show open castles on the evidence; the
third, Fuel Specialties, shows a held margin and held share against its reporting competitor, but how much of it is a
sole-source lead product with a stated end date inside ten years is undisclosed and knowable. COMPUTATION only: value range
$59.49 to $90.63, fair price about $61, cheap price about $40, against $98.17. The research file opens next (Part VII);
steps 1 and 2 follow.

---
## RESEARCH PASS: STEPS 1 AND 2 (written before any reading; the pass is not run here)
*CONVENTION in form (section VI; Part VII). Each OUT answer is one fact; each knowable question carries its span and source;
an unanswerable question is recorded and set aside **[M2008-086]**. No holding facts are known to this analyst.*

**Step 1. "What do I not know that I need to know?" [M1999-129]**

| # | Question | Knowable? |
|---|---|---|
| 1 | What share of Fuel Specialties operating income (or, failing that, sales) is AvGas TEL? | Knowable to the company; whether it is on the public record is to be found **[M2006-076]** |
| 2 | Has Fuel Specialties, excluding AvGas, held its volume over the last decade? | Knowable: the 10-K sales bridges report volume by region with AvGas apart |
| 3 | What does Fuel Specialties earn on the capital it employs, against its reporting competitor? | Knowable if segment assets are disclosed in the 10-K segment note |
| 4 | Is the AvGas end date firm, or receding? | Knowable: FAA/EPA rulings, the EAGLE record, EU REACH authorisation |
| 5 | Does Innospec win and keep fuel-additive business on specification and service, or on price? | Partly knowable: competitor filings, customer statements, trade record **[M1998-144]** |

If question 1 proves unanswerable from primary documents, it is recorded with the search that failed and the close is made on
questions 2 to 5 (form (c)). If on the record the AvGas end date cannot be judged at all, the file closes TOO HARD (NATURE).

**Step 2. For each question: the evidence, where it is, and the answer that would close the file OUT [M1998-144]**

1. **AvGas share.** Span FY2016–FY2025. Source: 10-K MD&A and segment notes; 8-K Ex. 99.1 earnings releases; earnings-call
   transcripts (aggregator, flagged). **OUT if:** any statement of record puts AvGas at one-third or more of Fuel Specialties
   operating income in any year FY2021–FY2025.
2. **Volume excluding AvGas.** Span FY2016–FY2025. Source: the "Volume" row of the Fuel Specialties sales bridge for the
   Americas, EMEA and ASPAC in each 10-K. **OUT if:** the cumulative regional volume change over FY2016–FY2025, compounded from
   the bridges, is negative.
3. **Capital test.** Span FY2021–FY2025. Source: 10-K segment note (identifiable or total assets by segment) for Innospec;
   NewMarket 10-K segment note for petroleum additives. Measure: segment operating income after depreciation set against
   segment assets (earnings after depreciation against capital employed, never cash against capital or the reverse). **OUT
   if:** Fuel Specialties' five-year average is below NewMarket petroleum additives' five-year average on the same measure.
4. **The AvGas date.** Span 2022–2026. Source: FAA and EPA public dockets on unleaded avgas approval and the endangerment
   finding; the EAGLE programme record; ECHA REACH authorisation decisions. **OUT if:** a final federal rule or FAA action of
   record requires the end of leaded avgas sales in the US on or before 31 December 2030.
5. **Specification or price.** Span FY2016–FY2025. Source: Innospec 10-K MD&A price-and-mix lines for Fuel Specialties;
   NewMarket and other competitors' 10-K competition sections. **OUT if:** in any two of the five years FY2021–FY2025 the
   Fuel Specialties MD&A attributes a gross-margin decline to competitive pricing (as distinct from raw-material pass-through).

If the pass closes IN, the run resumes at Q2 and continues to Q3, with the COMPUTATION above to be re-made as Q7 proper.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not done**.
      The file was copied first, but the questions were written in one pass after the reading, and no commit was made (the
      dispatch forbade commits). Declared, not hidden.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; full rows in `ledger_rows.txt`); every filing fact
      has its accession; numbers carry a filing, a row or a CONVENTION/judgment label.
- [x] The order was kept; Q2 closed the run; Q3 to Q10 are NOT REACHED and their recorded facts carry no verdict; the value
      figures are headed COMPUTATION — NOT A CLEARANCE (operator rule 3).
- [x] Owner cash after every real cost, stock pay deducted, never a net-income proxy (operator rule 5); sovereign from the
      Treasury; the price quote flagged as an aggregator's; Croda flagged as non-SEC.
- [x] Contrary evidence written down as found **[M1997-127]** (nine items, Foundations).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used, and a tag defect in them (goodwill 2.0) was caught against the
      filing.
- [x] `python tools/check_framework.py` PASS (run 2026-10-05 after the file was complete); a separate script confirmed no
      E-ids, every M/L/R id present in `principle_ledger_v5.csv`, and every quoted fragment beside an id found in that row
      (it caught one misquote of M2011-017 and one filing phrase sitting beside M2005-020; both corrected before the PASS).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**Q2 has no rule for a business made of parts whose castles differ.** Q1 has one (a holding company is understood by its
parts, and a part that matters and cannot be understood keeps the whole outside, CONVENTION), but Q2's two closes, OUT for a
castle "shown open" and TOO HARD for one "whose future cannot be judged", are written for a single castle. Here two parts with
about half the profit are open on the evidence and one part with the other half is standing but of unjudged durability. Read
literally, "a castle shown open closes OUT" could close the whole company OUT on two segments, which would refuse a business
whose largest part may be a sound castle; read loosely, the open parts could be ignored, which would let a moat on half the
profit clear the whole. What was done: the open parts were treated as ordinary businesses to be valued low, not as a close,
and the close was decided by the part that would carry a moat (Fuel Specialties), which is TOO HARD (WORK). A by-parts rule for
Q2 matching Q1's would settle it. Two smaller points: (i) the Q7 convention's "growth shown" gives no ruling when the aggregate
owner cash shows none while operating income grew; the range here used none at the bottom and the operating-income rate at
the top, and said so; (ii) the floor convention states "about ten percent pre-tax" while the cash input is after the
company's tax; the run used the company's adjusted tax rate for the after-tax equivalent and showed the 2002 row's own
translation beside it, but the convention does not say which tax rate converts the floor.
