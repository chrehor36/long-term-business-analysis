# Company Run: Starbucks Corporation (Nasdaq: SBUX), 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold (overnight cycle, 2026-10-11), after the run was committed: **not held**; `PORTFOLIO.md` carries SBUX only as a row of the ranked opportunity set from the v4.1 run of 2026-09-04, in no account.*

**Dispatched run.** Brief: `Screens/_daily/_dispatch_brief.md`, slots filled by the dispatching session's message of
2026-10-10. Working folder `Test Runs/_research 2026-10-10 SBUX/` (notes in `notes.md`; arithmetic in `q7.py`; raw filings
in `cache/`, ignored). Template copied and committed (commit aa564f4a) before any fetch.

**Contamination, declared and not used.** The session's opening git status listed other run files of 2026-10-10 by name
(OTIS, PNR) and research folders of other names (AYI, ARCB), and the recent commit subjects named runs of MA, MSA, NDSN and
ORLY with their boxes; the project's memory index, loaded at session start, carries lines on the queue state, the count of
gate-clearers and owed holding reviews. None names Starbucks; none was opened; nothing of them is used. No file about
Starbucks other than this one was opened, listed or searched. A text search was run on `principle_ledger_v5.csv` for
"Starbucks", "coffee" and "McDonald" (the ledger is a governing source, not a run file): no row names Starbucks.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $90.75 (close 2026-10-09, as printed by `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.001 par, **1,140.0M** as of 2026-07-23
  (10-Q for the quarter ended 2026-06-28, filed 2026-07-29, accession `0000829224-26-000130`;
  `python Screens/cover_shares.py SBUX` printed 1,140,000,000). Checked against the balance sheet of the same 10-Q:
  issued and outstanding 1,139.8M at 2026-06-28; the company retires repurchased shares (no treasury line). No
  repurchases in fiscal 2025 or in the first three quarters of fiscal 2026 (10-K FY2025 Item 5; 10-Q Q3 FY2026, equity
  note: "we made no share repurchases"). No 8-K after the 10-Q reports an issuance (8-K of 2026-09-24,
  `0000829224-26-000145`, is a restructuring and store-count notice).
- **Market cap:** 1,140.0M x $90.75 = **$103,455M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025 (52 weeks to 2025-09-28), filed 2025-11-14, `0000829224-25-000114`: Item 1, Item 1A (labour and union
    risk), Item 5, MD&A in full, balance sheet, cash flow statement, equity statement, Note 17 segments, Note 2.
  - 10-Qs FY2026: Q1 `0000829224-26-000011`, Q2 `0000829224-26-000080`, Q3 `0000829224-26-000130` (Note 2 divestiture,
    debt note, MD&A, statements).
  - Proxies: DEF 14A filed 2026-01-26 `0001213900-26-007780` (FY2025 pay); DEF 14A filed 2025-01-24
    `0001213900-25-006516` (FY2024 pay, the CEO change of 2024).
  - 8-Ks: 2025-11-03 `0000829224-25-000079` (China joint venture announced); 2026-04-02 `0000829224-26-000064` (China
    closing); 2026-05-15 `0000829224-26-000088` (restructuring, Item 2.05); 2026-06-12 `0000829224-26-000106`
    (principal accounting officer); 2026-07-29 `0000829224-26-000129` with EX-99.1 (Q3 FY2026 results and guidance);
    2026-09-24 `0000829224-26-000145` (closures, Item 2.05); 2025-03-14 `0000829224-25-000024` and 2026-03-30
    `0000829224-26-000058` (annual meeting votes).
  - Earlier 10-Ks for the cycle: FY2009 `0000950123-09-064772`, FY2010 `0001193125-10-266333` (segments FY2008 to FY2010,
    comparable sales FY2006 to FY2010), FY2015 `0000829224-15-000038`, FY2019 `0000829224-19-000051`, FY2020
    `0000829224-20-000078`, FY2022 `0000829224-22-000058`, FY2023 `0000829224-23-000058`, FY2024
    `0000829224-24-000057`.
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
    $4,747.5M on the filed cash flow statement of the FY2025 10-K, against the 4,748 printed by `tools/run.py` from XBRL.
    Also FY2025 capital spending $2,305.5M (statement) against 2,306 (tool). They agree.
- `python tools/run.py SBUX`, arithmetic lines only: owner cash (operating cash less stock pay less capital spending)
  FY2023 3,372, FY2024 3,010, FY2025 2,124; three-year mean 2,835 (capital spending basis) and 3,703 (D&A basis); the
  five-year means 2,998 and 3,570. Stock pay resolved to one tag every year (ShareBasedCompensation: 302.7, 308.3, 318.3).
  The tool deducts no acquisitions (FY2025: $177.1M paid for 23.5 Degrees Topco Limited) and credits no divestiture
  proceeds; Q7 builds its own series from the statements (`q7.py`). Nothing the tool prints as a rule, id or floor is used
  (Part VII).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is that a share is a business: the test is whether one would be content to own this
"if the market closed for five years" **[M1997-109]**, which turns the question away from the quotation and onto the
coffeehouses, whose traffic has just fallen for two years and risen for three quarters. The market "just tells us prices"
**[M2006-077]**, and the price of $90.75 is read for what it implies, not as evidence of value. Margin of safety: "if you
have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. The analyst's habit
that governs this file is the hunt for "what’s wrong in things" **[M2025-013]**, with the outside reading used "to possibly
reject your original hypothesis" **[M1998-144]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) owner cash after every real cost was about $3.0B in FY2016 and about $2.1B in FY2025 while revenue rose from $21.3B
to $37.2B (cash flow statements; `q7.py`); (2) the home segment's operating margin fell from 24.2% (Americas, FY2015
10-K) to about 20.7% (FY2019, FY2023) to 11.5% (North America, FY2025) and 11.8% for the first three quarters of FY2026;
(3) North America comparable transactions fell 5% in FY2024 and 4% in FY2025 while average ticket rose 4% and 2%, after
pricing of roughly 400 and 300 basis points of margin in FY2022 and FY2023 (10-Ks FY2022 to FY2025); (4) in China the
company's revenue went from $3,674.8M (FY2021) to $3,160.8M (FY2025) while Luckin Coffee went to 30,888 China stores and
RMB49.3B of revenue in 2025 (Luckin 20-F, `0001104659-26-035712`), and the company sold 60% of its China retail business
on 2026-03-30; (5) shareholders' equity went from +$5.45B (FY2017) to -$8.1B (FY2025) after $30.8B of buybacks in FY2015 to
FY2024, financed in part by debt that rose from $3.9B to $16.1B; (6) restructuring has recurred: $892.0M in FY2025, a
further plan of about $400M approved 2026-05-13 and one of about $300M approved 2026-09-22; (7) three chief executives
between April 2022 and September 2024; (8) dividends paid in FY2025, $2,771.4M, exceeded net earnings of $1,856.4M. On
the other side, also written as found: North America comparable sales rose 6.2% in the first three quarters of FY2026,
with comparable transactions up 3.9% (10-Q Q3 FY2026).

## THE STANDING RULE
A part-interest bought with the buyer's own cash, unlevered, puts the buyer at no risk of ruin; the rule binds how the
purchase would be financed and sized: "We are never going to risk what we have and need for what we don’t have and don’t
need" **[M2012-081]**, and no practice "that can result in sudden demands for large sums" **[L2014-024]**. Nothing in this
name requires the buyer to borrow or to give a counterparty a call on him. The standing rule is met on the buyer's side.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
  The key variables and their predictability are the first step **[M1998-044]**. For Starbucks the filings name them: the
  number of coffeehouses, comparable transactions and ticket in the company-operated North America stores (74% of FY2025
  revenue in North America, 10-K FY2025 Item 1), the store labour cost against the ticket, the royalty and product
  streams from licensees and from the Global Coffee Alliance with Nestle (Channel Development, 5% of revenue), and, since
  2026-03-30, a 40% equity stake and a licence in China in place of a company-operated China business (10-Q Q3 FY2026,
  Note 2).
- **Are they foreseeable?** The product and the format have been the same for decades: the FY2010 10-K and the FY2025 10-K
  describe the same business (company-operated and licensed coffeehouses, packaged coffee through partners). The forecast
  asked is about customers, not technology: whether people will keep buying a handcrafted coffee drink from this chain at
  its price. The rows place that kind of forecast inside the reach of the analysis, "laying out what their prospective
  customers will do in the future" **[M2017-019]**, and "what we think we can project out in terms of consumer behavior
  and threats to a business" **[M2023-030]**. No technological component of significance decides the economics; mobile
  ordering and the rewards programme are distribution, not invention.
- **Do the past statements tell me the future ones?** **[M2008-033]**. In kind, yes: the statements of FY2009, FY2020 and
  FY2025 each show the same mechanism, a fall in transactions against a high fixed cost of labour and occupancy, margin
  falling by half and recovering when traffic returned (US segment 7.5% in FY2009 and 17.1% in FY2010, 10-K FY2010
  segment note; Americas 11.1% in FY2020 and North America 20.8% in FY2021, 10-Ks FY2020 and FY2022). In level, less:
  the FY2024 to FY2026 statements show the North America margin moving from 19.8% to 11.5% within one year and not yet
  back. That is a question of how far off the forecast of earning power can be **[M2011-084]**, which Q7's range must
  carry; it is not a business whose economics cannot be pictured.
- **The warnings the rows give for this kind of business.** Retail is the narrated case of misplaced confidence:
  "it’s easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**, and "In
  retailing, to coast is to fail" **[L1995-008]**. These were weighed. The doubt rule, "if you have doubts about something
  being into your circle of competence, it isn’t" **[M2002-092]**, is applied to the economics, not to the level of the
  next year's margin: I can state the ten-year picture (a large North American coffeehouse chain, fewer company-operated
  stores abroad, more royalty income, earnings driven by traffic against labour cost) and I cannot state its margin to
  within a few points, which is the ordinary condition the range exists for.
- **Routing.** Not a fast-changing industry (no TOO HARD at Q1 on change); not a bank; not a holding company. The parts
  are read at Q2.
- **VERDICT: IN.** The economics can be foreseen in kind ten years out from the filings **[M2012-065]**, **[M2017-019]**;
  the retail warning **[M2014-052]** is carried to Q2 (would it stand without the lord) and to Q7 (the width of the range).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**.

**The parts table** (segment operating income from the segment notes of the FY2022, FY2023 and FY2025 10-Ks; FY2021 to
FY2025; USD millions; unallocated corporate cost of -8,737.9 left out of the shares, which are of the segment total
32,444.0):

| part | 5-yr operating income | share | castle | decides |
|---|---|---|---|---|
| North America (company-operated and licensed coffeehouses, US and Canada) | 22,753.5 (4,259.3; 4,486.5; 5,495.7; 5,355.3; 3,156.7) | 70.1% | standing, narrowed (below) | **yes**, more than half |
| International (incl. China until 2026-03-30) | 5,305.5 (1,245.7; 833.2; 1,230.9; 1,045.7; 950.0) | 16.4% | China: filled in by a rival on the evidence (below); the licensed markets not read separately | no |
| Channel Development (Nestle licence and products; ready-to-drink joint ventures) | 4,385.0 (789.1; 817.3; 967.6; 925.9; 885.1) | 13.5% | a perpetual royalty licence to Nestle since FY2019; margins 44.3% to 52.3% | no |

The file closes on North America, by the business-of-parts convention (section B of the gaps case), which follows
"lumping them together [...] impedes analysis" **[L2008-005]**. The International part, open in China on the evidence below,
does not decide; it is carried to Q7 as an ordinary business at no growth.

**The castle tests on the deciding part (North America).**
1. *Key factors and their permanence* **[M1995-038]**. What keeps customers is habit and the brand in the mind, a daily
   purchase asked for by name: "It’s share of mind. It’s not share of market." **[M1997-099]**. Store density is the
   other factor: 18,371 North America stores at 2026-06-28 (EX-99.1 to 8-K `0000829224-26-000129`), against Dutch Bros'
   1,136 shops in 25 states at 2025-12-31 (Dutch Bros 10-K FY2025, `0001866581-26-000006`).
2. *Would it stand without the lord?* The record weighs against. The founder came back as chief executive in 2008 and
   again, as interim, in 2022; the board paid $95.8M in FY2024 (summary compensation table, DEF 14A
   `0001213900-25-006516`, as reported again in DEF 14A `0001213900-26-007780`) to bring in a third chief executive in
   September 2024 to stop a two-year fall in traffic. The rows say "if it can’t stand a little mismanagement, it’s no
   business" **[M2018-059]**, and of retailers that "Buying a retailer without good management is like buying the Eiffel
   Tower without an elevator" **[L1995-006]**. Starbucks did stand the mismanagement, in the sense that matters for the
   castle: in each of the three troughs (FY2009, FY2020, FY2025) the business shrank in margin, not in customers' loyalty
   beyond recovery, and traffic came back (below). The dependence on the lord is real and is weighed, not taken as an
   open castle.
3. *The attacker with money* **[M2011-015]**. In North America no attacker with money has taken share at scale on the
   filed record: Dutch Bros, the fastest-growing filer, had $1,638.2M of revenue in 2025 against North America's
   $27,373.1M (FY2025). In China the test failed: Luckin Coffee, a rival that "one competitor is frequently enough to
   ruin a business" **[M2012-108]** describes, reached 30,888 China stores and RMB49,288M of revenue in 2025 (from
   RMB24,903M in 2023; Luckin 20-F `0001104659-26-035712`), while the company's China revenue went from $3,674.8M
   (FY2021) to $3,160.8M (FY2025) on 8,009 stores (10-K FY2025 Note 17 and store table) and the company sold 60% of the
   business. Luckin's own filing says "our products are not proprietary" (20-F, risk factors).
4. *Pricing power and the agony* **[M2005-020]**. Through the inflation the company priced: North America average ticket
   +7% in FY2022 ("strategic pricing", about 400 basis points of margin) and +6% in FY2023 (about 300 basis points), then
   +4% in FY2024 with comparable transactions -5%, and +2% in FY2025 with transactions -4% (10-Ks FY2022 to FY2025). The
   row for that pattern is "they maybe just pushed their pricing too far to the point that they lost market share without
   getting — without having — the moat that they thought they had" **[M2001-087]**. Against it: in the first three
   quarters of FY2026 North America comparable transactions rose 3.9% with ticket +2.3%, and +4.5% with ticket +3.5% in
   the third quarter (10-Q Q3 FY2026; EX-99.1), so the customers came back without the price being taken back.
5. *Would the customer still choose it over the low bid?* "it wouldn’t be a question of people buying candy for the low
   bid" **[M2017-009]**. In North America, after two years of losses, the answer on the FY2026 filings is yes; in China it
   was no. The food business in general does not give "the total certainty of dominance" of Coca-Cola, since "People move
   around in the food business" **[M1997-001]**, a row about a category, weighed and not a verdict (the one-company
   convention of 2026-10-07 applied by analogy).
6. *The low-cost position.* Starbucks is not the low-cost operator; it sells at a premium. Its labour cost is what moved:
   store operating expenses rose to 56.4% of North America company-operated revenue in FY2025 from 51.4% in FY2024 (10-K
   FY2025). The rows judge labour cost against the competitor, not in absolute terms: "if your costs are on parity or less
   — labor costs — than your other major competitors, that is much more important to you than the absolute level"
   **[M2001-013]**. The competitor's filing shows the same pressure: McDonald's US company-operated restaurant margin was
   16.0% (2017), 15.6% (2019), 15.2% (2023) and 11.6% (2025) of sales (McDonald's 10-Ks FY2019 `0000063908-20-000022`
   and FY2025 `0000063908-26-000035`), so part of the fall is the field's labour cost, not a castle crossed.
7. *Widening or narrowing* **[M1999-108]**. Narrowing, a notch: the home segment's margin was 24.2% (FY2015), 20.7%
   (FY2019 and FY2023), 19.8% (FY2024), 11.5% (FY2025) and 11.8% in the first three quarters of FY2026; the earlier
   troughs were 6.1% and 7.5% (US segment FY2008 and FY2009, with closure charges) and 11.1% (FY2020). The row for the
   reading is the newspaper industry that "retains its excellent economics, but has lost still another notch"
   **[L1995-023]**. Whether FY2025 is "a cyclical problem, not a secular one" **[L1995-022]** is not settled by three
   quarters; a change for the better is credited only on a full cycle (section C of the gaps case), so none is credited.
8. *What could destroy, modify or reduce it* **[M2000-014]**: a rival with a cheaper, app-ordered, dense format (shown in
   China); labour cost and unionisation (unions represent partners in about 6% of US company-operated stores, 10-K FY2025
   Item 1A); and the company's own pricing past what the customer will pay (shown in FY2024 and FY2025).

**The competitor row** (operating margin, or the closest store-level figure each filer reports, latest year and span):

| filer | metric | figures | source |
|---|---|---|---|
| Starbucks North America | segment operating margin | 24.2% FY2015; 20.7% FY2019; 11.1% FY2020; 20.8% FY2021; 19.2% FY2022; 20.7% FY2023; 19.8% FY2024; 11.5% FY2025 | 10-Ks FY2015, FY2020, FY2022, FY2023, FY2025 |
| McDonald's | consolidated operating margin (90% franchised margin dollars); US company-operated restaurant margin | 46.1% (2025), 45.2% (2024); US company-operated 16.0% (2017) to 11.6% (2025) | 10-Ks FY2019, FY2025 |
| Restaurant Brands, Tim Hortons segment | segment income / segment revenue (franchisor with supply chain) | 1,122 / 3,344 = 33.6% (2019); 1,077 / 4,247 = 25.4% (2025) | 10-Ks FY2019 `0001618756-20-000004`, FY2025 `0001618756-26-000017` |
| Dutch Bros | operating margin; company-operated shop contribution | 161.2 / 1,638.2 = 9.8% (2025); contribution 28.2% (2023), 29.7% (2024), 28.9% (2025) | 10-K FY2025 `0001866581-26-000006` |
| Luckin Coffee (20-F filer, flagged: foreign private issuer, RMB) | operating margin | RMB3,570.1M / 34,474.8M = 10.4% (2024); RMB5,072.9M / 49,288.1M = 10.3% (2025) | 20-F FY2025 `0001104659-26-035712` |
| Costa (Coca-Cola) | not reported separately | flagged: no filed segment figure | none |
| private chains (Dunkin' under Inspire Brands, Tim Hortons' private rivals, independents) | not SEC filers | flagged | none |

**The field's returns over the last full cycle, judged in words.** The established leaders earn well above ordinary
returns on the capital the business needs: Starbucks' operating income against net property, plant and equipment was
about 76% (FY2021) to 62% (FY2024) and 35% in the restructuring year FY2025, and about 33% to 17% with the operating-lease
right-of-use assets added (balance sheets, 10-Ks FY2021 to FY2025); McDonald's and Tim Hortons earn franchisor margins.
The new entrants earn about 10% operating margins while growing fast (Dutch Bros, Luckin). This is not a field of
ordinary returns for the incumbent with the castle; the castle that protects only ordinary returns does not describe
North America on this record. "you can almost measure the strength of a business over time by the agony they go through
in determining whether a price increase can be sustained" **[M2005-020]**: the agony is visible in FY2024 and FY2025 and is
weighed above as the narrowing.

- **VERDICT: IN.** The deciding part's castle is standing on the evidence: customers returned in FY2026 at a higher ticket
  **[M2017-009]**, no attacker with money has taken North America at scale **[M2011-015]**, and its returns on the capital
  needed remain well above ordinary. It is not shown open, and its future can be judged in kind; it has lost a notch
  **[L1995-023]** through pricing past the customer **[M2001-087]** and through labour cost shared with the field
  **[M2001-013]**, and it depends more than a great business should on who runs it **[M2018-059]**. The narrowing is carried
  to Q7 as the growth input and to the width of the range. The China part, filled in by one rival **[M2012-108]**, does
  not decide and is carried to Q7 as an ordinary business at no growth (after the sale of 60%, as an equity stake and a
  licence).

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed.** The capital is "the capital actually needed in the business" **[M2010-090]**,
  not book equity, which is negative here and meaningless as a base: "if you keep the equity low enough by buying shares
  back, why, you could make return on equity whatever you want" **[M1998-017]**. Operating income (pre-tax, after
  depreciation and rent) against net property, plant and equipment: FY2021 4,872.1 / 6,369.5 = 76%; FY2022 4,617.8 /
  6,560.5 = 70%; FY2023 5,870.8 / 7,387.1 = 79%; FY2024 5,408.8 / 8,665.5 = 62%; FY2025 2,936.6 / 8,493.5 = 35%. With the
  operating-lease right-of-use assets added as capital (8,236.0 at FY2021, 9,315.7 at FY2025), 33% falling to 17%
  (balance sheets and income statements, 10-Ks FY2022 to FY2025). Working capital is negative (stored-value card
  liability and current deferred revenue $1,840.6M, payables $1,852.8M, against receivables $1,277.5M and inventory
  $2,185.6M at FY2025), so customers fund part of the stores. On the average, the stores are of the kind that "earn very high returns on
  capital employed" **[M1995-047]**.
- **What the added capital earned.** The test is "what we earn on that incremental $130 million over time"
  **[M2001-019]**. From FY2016 to FY2025 the company spent $18,954.2M on property and equipment against $14,223.3M of
  depreciation and amortization (cash flow statements; XBRL series checked to the FY2022 and FY2025 statements), paid
  $1,311.3M for the East China joint venture (FY2018) and $177.1M for 23.5 Degrees (FY2025), and grew net PP&E from
  $4,533.8M to $8,493.5M. Revenue rose from $21,315.9M to $37,184.4M. Operating income went from $4,171.9M (FY2016) to
  $5,408.8M (FY2024) and $2,936.6M (FY2025); owner cash after all capital spending and stock pay went from about $3,040M
  (FY2016) to $3,010M (FY2024) and $1,947M (FY2025, after the acquisition). The FY2016 to FY2024 increment, about $1.2B of
  pre-tax operating income on about $4.1B of added net PP&E plus a larger lease book, is a fair return; carried to
  FY2025 it is negative. What grew was per-share, not total, and it grew through buybacks financed with debt (Q4, Q6). The
  row that fits: "we’re not earning a higher rate of return on capital than we were when we started. We just put way more
  capital into the business" **[M2023-081]**.
- **Reinvestment to stand still.** The filer states no maintenance figure; the owner is entitled to "my best guess"
  **[M2000-144]**, and none is given. FY2026 capital spending is guided "moderately lower than fiscal 2025" (10-K FY2025
  MD&A) and was $887.8M in three quarters (10-Q Q3 FY2026), with the China stores' spending gone after the sale. Store
  renovation ("coffeehouse uplifts") and store labour are now named as what keeps the customer, so part of the outlay is
  compulsory to stand still.
- **The growth arithmetic and its cap.** A capital-using business is a second best when it earns "decent returns on the
  incremental sums they invest" **[L2009-012]**; here the average return passes and the decade's incremental return does
  not show in the owner's cash.
- **WEIGHS AGAINST**: high returns on the capital the stores need **[M1995-047]**, but a decade of added capital bought no
  growth in owner cash **[M2001-019]**, **[M2023-081]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, nine year-ends and the latest quarter, before the income account** **[M2025-032]**
  (`tools/run.py` table from first-filed XBRL, read against the filed balance sheets of the FY2025 10-K and the Q3 FY2026
  10-Q; USD millions):

  | year-end | assets | equity | cash | receivables | inventory | goodwill | long-term debt (non-current) | retained earnings |
  |---|---|---|---|---|---|---|---|---|
  | FY2017 | 14,366 | 5,450 | 2,462 | 870 | 1,364 | 1,539 | 3,933 | 5,563 |
  | FY2018 | 24,156 | 1,170 | 8,756 | 693 | 1,400 | 3,542 | 9,090 | 1,457 |
  | FY2019 | 19,220 | -6,232 | 2,687 | 879 | 1,529 | 3,491 | 11,167 | -5,771 |
  | FY2020 | 29,374 | -7,805 | 4,351 | 883 | 1,551 | 3,597 | 14,660 | -7,816 |
  | FY2021 | 31,393 | -5,321 | 6,456 | 940 | 1,604 | 3,677 | 13,617 | -6,316 |
  | FY2022 | 27,978 | -8,707 | 2,818 | 1,176 | 2,177 | 3,284 | 13,120 | -8,450 |
  | FY2023 | 29,446 | -7,995 | 3,552 | 1,184 | 1,806 | 3,218 | 13,548 | -7,256 |
  | FY2024 | 31,339 | -7,449 | 3,286 | 1,214 | 1,777 | 3,316 | 14,320 | -7,344 |
  | FY2025 | 32,020 | -8,097 | 3,220 | 1,278 | 2,186 | 3,369 | 14,576 | -8,272 |
  | Q3 FY2026 | 28,295 | -7,674 | 3,450 | 1,304 | 2,209 | 1,239 | 11,780 (+1,498 current) | -8,543 |

  What the figures are saying. (a) Equity went from +$5.45B to -$8.1B in two years, FY2018 and FY2019, and stayed
  negative: Nestle paid "an upfront payment of approximately $7 billion primarily of prepaid royalties" (10-K FY2018,
  `0000829224-18-000052`, Note 2), $5.0B of it went into an accelerated repurchase on 2018-10-02 (same 10-K, Note 18), and
  the FY2019 10-K says cash fell from $9.2B to $3.0B "driven by the usage of the up-front prepaid royalty associated with
  the Global Coffee Alliance primarily for share repurchases". The deficit is buybacks above book, not losses; but the
  prepaid royalty sits as a liability (deferred revenue $5,772.6M long-term at FY2025) that is recognised as revenue for
  decades without cash, so a slice of reported Channel Development revenue each year is non-cash. (b) Long-term debt rose
  from $3.9B to $14.6B; total debt was $16.1B at FY2025 and $13.3B at 2026-06-28 after $2.8B of repayments, $1.3B of it by
  tender with the China proceeds (10-Q Q3 FY2026, debt note). (c) Goodwill doubled in FY2018 with the East China purchase
  and fell to $1,238.8M in FY2026 when China was deconsolidated. (d) Receivables track sales (3.9% of revenue in FY2017,
  3.4% in FY2025); inventory rose in FY2022 (supply chain) and FY2025, which the filer ties to green coffee prices (10-K
  FY2025 MD&A, cash flows). Nothing builds that the filer does not explain; prepaid expenses are small ($452.2M).
  (e) What they do not say: the operating leases ($12.4B of undiscounted obligations, 10-K FY2025 material cash
  requirements) are the larger fixed claim and sit outside debt. What they cannot say: the value of the brand.
- **The real costs.** Depreciation is charged and is "an economic cost every bit as real as wages, materials, or taxes"
  **[R1996-023]**; capital spending ran above it in every year FY2016 to FY2025 (Q3). Stock pay is expensed ($318.3M in
  FY2025) and is not removed in the company's non-GAAP figures (EX-99.1 reconciliation: restructuring, transaction and
  transformation costs, the China gain and their tax only). No EBITDA appears in the 10-K or the earnings release (text
  search: none). Restructuring recurs: $135.8M (FY2019), $278.7M (FY2020), $892.0M (FY2025), $415.8M in the first three
  quarters of FY2026 with two further plans approved (8-Ks `0000829224-26-000088`, about $400M, and
  `0000829224-26-000145`, about $300M). The row: "to tell owners year after year, "Don't count this," when management is
  simply making business adjustments that are necessary, is misleading" **[L2016-007]**; the costs are counted here as real
  and recurring and are inside the operating cash Q7 uses.
- **The habits carried to Q5.** The earnings release leads with GAAP EPS and puts the non-GAAP figure beside it ("Q3 GAAP
  EPS $0.91, Non-GAAP EPS $0.85"), and the company gives guidance in non-GAAP terms: "Non-GAAP earnings per share in the
  range of $2.55 to $2.65" and a non-GAAP operating margin "greater than 11.0%" for FY2026 (EX-99.1,
  `0000829224-26-000129`). Guidance is "the scourge of earnings "guidance"" in the rows **[L2019-006]**, and an adjusted
  figure featured weighs against **[L2016-006]**; both are recorded as a WEIGHING against and carried to Q5.
- **VERDICT on the accounts: WEIGHS AGAINST** (no confusion, no suspicion: the statements are clear, the GAAP figure
  leads, stock pay is in, and every large movement on the balance sheet is explained by the filer). The weight against is
  the recurring restructuring presented as excludable **[L2016-007]**, the guidance **[L2019-006]** and the adjusted figure
  **[L2016-006]**, carried to Q5; a management "preoccupied with accounting considerations" is "a negative" but not "a
  total exclusionary factor" **[M1994-018]**. The recast earnings for Q7 are owner cash after every real cost, from the
  cash flow statements: operating cash less stock pay less all capital spending less acquisitions (Q7).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
*(Resumed 2026-10-11 by a dispatched analyst after the run was killed at the session limit; Q5 onward written in that
session from the research folder's cache, no file refetched. The resume's reading of the file above it changed nothing
in it.)*

The question: "do we really want to be in partnership with this person" **[M2015-005]**, answered for a marketable stock by
reading, not meeting **[M2007-081]**. The people are the chairman and chief executive since September 2024, Brian Niccol,
the chief financial officer since 2025, Cathy Smith, and the board that chose them.

- **The first yardstick: the record against "the hand they were dealt"** **[M1994-008]**. The hand in September 2024:
  North America comparable transactions -5% in FY2024 after pricing past the customer (Q2, test 4), a segment margin of
  19.8% falling, China losing to Luckin. The record since: comparable transactions fell a further 4% in FY2025, then rose
  3.9% in the first three quarters of FY2026 and 4.5% in the third quarter, with ticket up rather than given back (10-Q Q3
  FY2026; EX-99.1 to `0000829224-26-000129`); 627 stores closed in the fourth quarter of FY2025 (10-K FY2025 store table
  note) and about 250 more announced on 2026-09-24 (`0000829224-26-000145`); China sold down to 40% at a filed gain of
  $536.3M (10-Q Q3 FY2026, Note 2 and income statement); debt cut from $16.1B to $13.3B (Q4). Against it: the margin has
  not come back (11.5% FY2025, 11.8% for three quarters of FY2026), and two years is short: the rows buy a record where
  "we’ve actually seen they batted .350" **[M2005-039]**. His record before Starbucks is in another company's filings,
  which were not read for this run, and is not used.
- **The second yardstick: "see how they treat themselves versus how they treat the shareholders"** **[M1994-009]** (DEF 14A
  `0001213900-26-007780`, summary compensation table and its notes; DEF 14A `0001213900-25-006516`).
  - FY2024: $95,801,676, of which $90,291,772 in stock awards, the "make whole" replacement grants of a target value of
    $80,000,000 for equity forfeited at his former employer, and a $5,000,000 signing bonus.
  - FY2025: $30,992,773: salary $1,599,998; bonus $5,000,000 (the second signing instalment); stock awards $19,881,585;
    annual cash incentive $1,971,000, which is 54.8% of the $3,600,000 target, the financial part paying 39.7% of target;
    all other $2,540,190. The formula part of the pay fell with the results.
  - Perquisites: the offer letter provided "a remote office in his city of primary residence", which the company opened in
    FY2025; commuting between that city and Seattle on company aircraft; personal use of the aircraft limited to $250,000 a
    year until September 2025, when the independent directors replaced the limit with a quarterly review by two directors,
    on a security study's recommendation; aircraft cost $997,392 and security $1,142,700 in FY2025; "In fiscal year 2025,
    Mr. Niccol paid Starbucks $0 pursuant to his time-sharing agreement." All of it is disclosed, itemised and explained.
    It is a fact about how a chief executive treats himself, weighed at Q6, Part B; it is not concealment.
- **The reports** **[M1998-036]**, read against "accounting can offer you a lot of insight into the character of
  management" **[M1995-064]**. The 10-K tells an owner what he would want to know: comparable transactions and ticket
  separately for each segment, stores opened and closed by market, each restructuring plan with its charges by kind, the
  Nestle prepayment and how it is used. The industry's key figure, traffic, is given every quarter, including in the two
  years it fell; it is not "touched on [...] in a dishonest manner" **[M2007-082]**. Bad news is told: the closures of
  September 2025 are explained in the filer's own words as stores that "did not demonstrate a viable path to profitability"
  (10-K FY2025 MD&A), and the risk factors say "We have in the past failed, and may in the future fail, to meet announced
  guidance or market expectations" (10-K FY2025 Item 1A). That is the conduct the rows ask for, "tell us the bad news
  immediately" **[M1998-039]**, and the opposite of the taboo that "always made me nervous" **[L2024-003]**.
- **The habits carried from Q4, read with the rest** **[M2004-067]**. Guidance in non-GAAP terms, the non-GAAP EPS printed
  beside the GAAP figure, and restructuring that has recurred since FY2019 presented as excludable. Against a finding of
  doubt: the GAAP figure leads the release; the reconciliation is short and names every item (restructuring and
  transformation costs, transaction costs, the China gain and their tax); stock pay is not excluded; no EBITDA appears;
  the company itself warns that its guidance has been missed. No target is shown to have been made by accounting: the
  FY2025 bonus paid at 54.8% of target and the 10-K reports the misses. Under the rows' wording these habits are "a
  negative" **[M1994-018]**, carried into Q6, Part B (guidance and the adjusted metric in the share awards).
- **The integrity record in the filings read.** No restatement, no SEC enforcement action, no auditor dismissal (Deloitte
  ratified in 2025 and 2026, 8-Ks `0000829224-25-000024` and `0000829224-26-000058`), no related-party dealings with the
  principal accounting officer (8-K `0000829224-26-000106`). Legal proceedings are "litigation matters associated with labor
  union organizing efforts and certain employment litigation" said not to be material (10-K FY2025 Note 16, Commitments and Contingencies, on legal
  proceedings), and the risk factors concede that the company's "position with respect to unions" could "expose us to
  legal risk". The rows' front-page test reaches conduct toward employees as well as owners **[M2016-033]**. The decisions of
  the labour board are not SEC filings and were not read: **a gap, recorded, not filled by impression.** On what was read,
  the dealings with owners show no tell the rows name: nothing too good to be true **[M2002-028]**, no stock price in the
  lobby **[M2004-067]**, no figure obscured.
- **Love of the business.** Not readable from filings for a hired chief executive beyond conduct: he took the job and its
  replacement grants; the 2025 "Back to Starbucks" share awards ($6M target) pay only if operating expense falls and the
  service, store-uplift, menu and rewards programmes are delivered (DEF 14A 2026). The rows say there is "no checklist in
  the world" for the after-the-cheque question **[M2016-066]**; for a stock, the yardsticks carry the weight **[M2007-081]**.
- **Ability.** The rows weigh it heavily for a retailer: "Buying a retailer without good management is like buying the
  Eiffel Tower without an elevator." **[L1995-006]**; and it enters value as "the degree of certainty" **[M1999-104]**. The
  turnaround has restored traffic in three quarters and has not yet restored margin; the finance chair has changed twice
  in 2025 (the former chief financial officer terminated without cause in March 2025, an interim, then Ms Smith; DEF 14A
  2026), and the principal accounting officer role moved in June 2026.
- **VERDICT on integrity: IN.** On the filings read there is no doubt about honesty with owners **[M2013-088]**: the
  reports tell the bad news and the key figure **[M1998-036]**, **[M1998-039]**, and the Q4 habits are disclosed and
  reconciled, a negative and not a tell **[M1994-018]**. The labour-board record is an unread gap, named under SELF-AUDIT.
  **Ability WEIGHS FOR, thinly**: traffic restored against a bad hand **[M1994-008]**, but two years is not a long record
  **[M2005-039]**, and for a retailer the weight on the manager is heavy **[L1995-006]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.** (Cash flow statements and equity notes, 10-Ks FY2018, FY2020, FY2022 to FY2025; `q7.py`,
`q7_cycle.py`.)
- **The retention test** **[R1995-009]**, **[M1998-110]**. Nothing was retained to be tested. From FY2016 to FY2025 net
  earnings were $31,971M; the company paid $20,227M in dividends and $29,357M for its own shares, $49,584M in all, about
  155% of what it earned. The difference came from the Nestle prepayment of about $7B (FY2018) and from borrowing (long-term
  debt $3.9B at FY2017, $14.6B at FY2025). The rows' test asks whether a dollar retained becomes worth more than a dollar; here the
  question is the reverse, whether the dollars borrowed and paid out were paid out at sense **[M2000-050]**, and that is the
  buyback test below.
- **Buybacks.** The programme names share counts, never a price: "The timing, manner, price, and amount of repurchases will
  be determined at our discretion" (10-K FY2025 Item 5), the case of "repurchase announcements almost never refer to a price
  above which repurchases will be eschewed" **[L2016-002]**. Prices actually paid, as the filings state them (shares and
  cost; average my division): FY2016 37.5M for $2.1B (about $56); FY2017 34.9M for about $2.0B (about $58); FY2018 131.5M for
  $7.2B (about $55); FY2019 139.6M for $10.1B (about $72); FY2020 20.3M for $1.7B (about $84); FY2022 36.3M for $4.0B (about
  $110); FY2023 10.0M for $1.0B (about $100); FY2024 12.8M for $1.3B (about $99) (10-Ks FY2018, FY2019, FY2020, FY2022,
  FY2023, FY2024, equity notes). Bought with "cash plus sensible borrowing capacity" **[L1999-023]**? Partly with borrowing
  that has since been reduced with the China proceeds. Bought while the stores needed the money? The FY2022 to FY2024
  purchases, $6.3B at about $99 to $110, came in the years when traffic fell and the turnaround then had to buy back staffing
  and store uplifts; the rows put "the internal need for funds" first **[L2016-003]**. **Written back from Q7 (committed with Q7):** the bottom of the central Q7 range is $45.46 a share on the all-equity
  basis ($50.71 equity-only), "the bottom boundary of our estimate" **[L2013-012]**. Every price paid, about $55 to $110,
  sits above it, and the FY2022 purchases at about $110 sit above the top ($99.49). The purchases are therefore not
  cleared by what they did, and the programme with no stated price weighs against **[L2016-002]**: "If you’re
  repurchasing shares above a rationally calculated intrinsic value, you are harming your shareholders" **[M1996-013]**.
- **Issuance and deals.** No stock issued for a deal; the share count fell from 1,460.5M (2016-10-02, XBRL from the FY2016 10-K) to 1,140.0M, so the
  serial-issuer sign **[L2014-015]** is absent and the all-stock STOP **[L2009-019]** does not arise. Deals for cash: the East
  China joint venture bought for $1,311.3M (FY2018), and China retail sold down to 40% at a $4B enterprise value in 2026 with a
  filed gain of $536.3M (10-Q Q3 FY2026); the row asks whether "we receive less in value than we give" **[M1995-001]**, and on the filed
  record the China round trip did not lose book value, though the 60% was sold after the business lost its position to Luckin
  (Q2).
- **Dividends.** $0.62 a quarter (EX-99.1, `0000829224-26-000129`), about $2.83B a year on 1,140M shares, against owner cash
  after interest of $1,947M in FY2025 and a five-year average of $3,231M (`q7.py`). FY2025 dividends of $2,771.4M exceeded
  net earnings of $1,856.4M and owner cash. The release presents "65 consecutive quarters of dividend payouts with CAGR of
  17%" as a commitment. The rows want "dividend policy should always be clear, consistent and rational." **[L2012-015]**: it
  is clear and consistent; whether paying more than the business throws off, with debt still above its FY2024 level less the
  China repayments, is rational is doubtful, and it is weighed against.

**Part B: the pay, the board and the owners.** (DEF 14A `0001213900-26-007780` and `0001213900-25-006516`; 8-Ks of the
annual meetings.)
- **Pay tied to what the person controls** **[M2003-019]**. The annual bonus pays on financial results (75%) and an individual
  factor (25%); FY2025 paid 54.8% of target. The annual share awards pay 50% on three-year average adjusted EPS and 50% on
  three-year comparable store sales, with a relative-return modifier; the 2025 "Back to Starbucks" awards pay on operating
  expense reduction and four programmes. Comparable sales and expense are under the managers' control; adjusted EPS is a
  figure the managers define, and the rows say "I hate, with a passion, rewarding anything that can be easily faked"
  **[M1996-089]**. The 2023 and 2024 awards were amended in March 2025 to fix three non-financial modifiers at 0.9, below
  threshold, which lowered rather than raised them.
- **Both directions** **[L1994-020]**. The bonus fell to 54.8% when results fell; the replacement grants of FY2024 ($80M
  target) made the new chief executive whole for what he left, which is a purchase price for the man, not pay for
  results here. The signing bonus of $10M was paid in two instalments regardless of results.
- **The board.** The board's first job "is to have the right CEO" **[M2007-120]**: it has chosen three chief executives
  since April 2022 (the founder as interim, Mr Narasimhan from 2023 to August 2024 with severance under his offer letter and
  the severance plan, DEF 14A 2025, and Mr Niccol), and that record weighs against the board. The chief executive is also
  chairman; an independent-chair proposal failed in 2025 (124.5M for, 684.4M against) and 2026 (107.8M for, 763.8M
  against). The row is "I've seen how hard it is to replace a mediocre CEO if that person is also Chairman."
  **[L2014-026]**; nothing here shows the present one mediocre, so it is a structural weight only. Directors' holdings are
  mostly deferred stock units received as fees: of the ten non-executive nominees, four hold shares beyond units (whether
  bought or vested is not stated), the largest 33,587 shares, about $3.0M at the price (DEF 14A 2026, beneficial ownership
  table at 2026-01-16; Mr Niccol holds 69,382); the rows prefer directors "purchasing
  shares with their savings, rather than simply having been the recipients of grants" **[L2019-008]**. The supermajority
  proposal passed in 2026 with the board making no recommendation (8-K `0000829224-26-000058`).
- **Owners as partners.** Earnings guidance is given every quarter in adjusted terms (Q4); by inversion of Berkshire's rule,
  "I can’t imagine anything more destructive" **[M2022-054]**. The perquisites of Q5 (unlimited personal use of the aircraft
  under review, $0 reimbursed in FY2025, a remote office) are how the chief executive treats himself **[M1994-009]**, at a
  cost small against the company and large against the rows' picture of a partner. Say-on-pay passed with about 86% in 2025
  and about 88% in 2026 of votes cast (8-Ks `0000829224-25-000024`, `0000829224-26-000058`). The rows also say
  "There are more problems with having the wrong manager than with having the wrong compensation system."
  **[M2007-006]**, so Part B is weighed below the man.
- **WEIGHS AGAINST.** Part A: a decade of distributions above earnings, financed in part with debt, by a programme that
  names no price **[L2016-002]**, at prices tested against Q7 below **[L1999-023]**, and a dividend above owner cash
  **[L2012-015]**. Part B: share awards half on an adjusted figure **[M1996-089]**, guidance **[M2022-054]**, a combined
  chair, three chief executives in three years **[M2007-120]**, and directors who mostly hold what they were given
  **[L2019-008]**; against these, the bonus fell with results **[L1994-020]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at the long government rate **[L2000-021]**, held as a range **[L2000-024]**. All figures below are from `q7.py` and
`q7_cycle.py` in the research folder, inputs from the filed cash flow statements named there; USD millions unless a per-share
figure. **Price and rate not refreshed:** the price ($90.75, close 2026-10-09) and the sovereign (5.60%, 2026-10-09) of
Step 0 are used unchanged; the result is not near enough to either to need a refresh.

- **The cash input** (Q4's recast): operating cash less stock pay less all capital spending less cash paid for businesses
  plus cash received for businesses sold, specific (c), the default pair: acquisitions deducted, the total growth credited
  (the filer reports no organic owner-cash figure, so the organic pair is not shown). On the all-equity basis **[L2017-004]**
  the after-tax net interest is added back (interest paid less interest income where filed, times one less the year's
  effective rate). Working capital is inside operating cash, specific (d). Unlevered owner cash, FY2016 to FY2025: 3,036;
  2,629; 2,115 (the Nestle prepayment removed, below); 3,858; 181; 5,697; 2,637; 3,821; 3,349; 2,298.
- **Growth spending, specific (e).** The filer gives no maintenance figure (Q3), so the filing does not allow the maintenance
  guess; the central case charges all capital spending, with depreciation in place of capital spending shown beside.
- **The window and the cycle, specific (a).** Both end years of the literal window FY2021 to FY2025 are aberrational on the
  filer's own description: FY2021 carries the recovery from the pandemic and $1,175.0M of cash from the divestiture of the
  South Korea joint venture (10-K FY2022, which describes the conversion of Korea to a fully licensed market); FY2025 is the
  year of the "Back to Starbucks" restructuring, $892.0M of charges and 627 store closures (10-K FY2025). "If either year
  was aberrational, any calculation of growth will be distorted." **[L2005-003]**. **CONVENTION of this run:** the cycles
  are FY2016 to FY2020 and FY2021 to FY2025, each running from a normal year to a year the filer describes as disrupted (the
  pandemic; the restructuring); rationale: the filings name no other cycle and these are the two complete ones in the ten
  years read. **CONVENTION of this run:** the Nestle up-front payment of "approximately $7 billion primarily of prepaid
  royalties" (10-K FY2018) is removed from FY2018 operating cash; rationale: it is decades of royalties received at once, and
  every later year's operating cash already lacks the royalties it prepaid. The variant that keeps it is shown.
- **The base and the growth.** Cycle averages: FY2016 to FY2020, 2,364; FY2021 to FY2025, 3,560 (the same as the literal
  window's average). Growth between the cycle averages: 8.5% a year (7.9% on owner cash after interest). The base is the
  last cycle's average, 3,560.
- **The cap, specific (f).** 3,560 carried ten years at 8.5% is 8,050 in year ten; sales carried at the business's own
  growth between the same cycles (averages 23,690 and 34,129, 7.6% a year) would be about 70,900, so the year-ten owner cash
  is 11.4% of sales, under the highest share earned in a year of the ten read without a business sale (14.6%, FY2019). The
  cap does not cut. Nothing is carried after year ten (zero nominal growth) **[M1997-095]**.
- **The China sale, closed after the window and before the price date, specific (c).** On its own filed record: 60% sold at
  a $4B enterprise value, $3.1B of consideration, $2.5B of net proceeds in the cash flow discussion (10-Q Q3 FY2026). The
  proceeds are inside net debt at 2026-06-28. The five-year base still holds 100% of the China business's cash, which is not
  filed separately. **CONVENTION of this run:** the value given is taken as 60% of the filed enterprise value, $2.4B,
  deducted from the whole-business value; rationale: it is the only filed measure of the part sold; the retained 40% and the
  licence stay in the base. It moves every figure by about $2.1 a share.
- **Net debt** at 2026-06-28 (10-Q Q3 FY2026): borrowings $13,278.6M (current $1,498.4M, long-term $11,780.2M) less cash,
  short-term and long-term investments $3,923.5M = **$9,355.1M**. Operating leases (about $12.4B undiscounted at FY2025) are
  left out, as the convention says, and belong to Q9. Shares 1,140.0M.

**The range (all-equity central, equity-only beside), per share:**

| case | base | growth, years 1 to 10 | all-equity | equity-only |
|---|---|---|---|---|
| **central, cycle (a), Nestle removed: no growth (bottom)** | 3,560 | 0% | **$45.46** | $50.71 |
| **central, cycle (a), Nestle removed: shown growth (top)** | 3,560 | 8.5% (7.9% after interest) | **$99.49** | $94.95 |
| cycle, Nestle prepayment kept as proceeds of a business sold | 3,560 | -1.1% | $40.79 to $45.46 | $42.69 to $50.71 |
| literal window FY2021 to FY2025, decline carried as the bottom (b) | 3,560 | -12.2% (halves) | $11.52 to $45.46 | $17.77 to $50.71 |
| literal window, depreciation in place of capital spending | 4,133 | -5.0% (halves) | $33.37 to $54.42 | $37.98 to $59.67 |
| literal window, in-window divestiture proceeds left out | 3,292 | -7.3% (halves) | $18.71 to $41.25 | $23.88 to $46.50 |

(The literal window's growth is measured between its halves, as `q7.py` does; measured between its end years it would be
-20.3% a year and its bottom lower still. Its end years are what specific (a) replaces.)

- **Value range (central): $45.46 to $99.49 a share** against **$90.75**; width 2.19 to one.
- **The floor first** (Q7, adopted 2026-10-10). At $90.75 the expected return on the central growth case is about 6.0% a
  year and on the no-growth case about 3.1% (the rates that discount each case to the price); the floor is about ten
  percent. On the central base, ten years of growth at 16.8% a year would be needed for the price to earn the floor. No case
  in the table earns it. The most generous reading I could construct (the best five-year average, 3,560, carried at the
  business's own revenue growth of FY2016 to FY2025, 6.4% a year) is worth $82.23 a share at the sovereign and $38.13 at ten
  percent. "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **The price against the range.** The price sits inside the central range, in its upper half; only the shown-growth end
  stands above it, by about 10%. That is the opposite of "It should scream at you." **[M2009-005]**; "if you have to
  actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$33.48 a share** on the all-equity basis (each end of the
  central range valued at ten percent: $20.92 and $45.90 after net debt and the China deduction, averaged), after the
  company's own tax, no conversion; **$38.74** on the equity-only basis beside it. On the literal window the fair price is
  $12.49 (equity-only $20.21). No cheap price is reported.
- **No tax shelter** to price separately: the effective rates of FY2021 to FY2025 run from 21.6% to 25.9% (income tax over
  pre-tax income, 10-Ks), near the statutory rate.
- **VERDICT: OUT.** The business can be valued, and its value does not reach the price at the floor on any case the filings
  support **[M2003-149]**: the price sits inside the range, not below it **[M2009-005]**, and the growth case that lifts the
  top above the price rests on a cycle comparison whose first cycle holds the pandemic year, the kind of base the rows warn
  can "produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. The width (2.19 to one) is under three, so
  the close is OUT and not TOO HARD; under the floor-first order it would be OUT whatever the width.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Q7 closed the file OUT. Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7** (the floor: no case in the range earns about ten percent at the price; the price sits inside the range).
Central value range **$45.46 to $99.49 a share** (all-equity; equity-only $50.71 to $94.95) against **$90.75** (close
2026-10-09); fair price $33.48 all-equity, $38.74 equity-only (reporting figures, not verdicts). Q1 IN, Q2 IN, Q3 weighs
against, Q4 weighs against, Q5 integrity IN and ability weighs for thinly, Q6 weighs against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on a later question, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).
- **Q8 (the bond).** The 30-year Treasury par yield was 5.60% on 2026-10-09 (Step 0). The central base of 3,560 of
  unlevered owner cash is 3.16% of the market value plus net debt at the price ($103,455M + $9,355.1M) (`q7.py`).
- **Q9 (debt and exposures).** Borrowings $13,278.6M at 2026-06-28 after $2.8B of repayments in FY2026, $1.3B of them by
  tender with the China proceeds (10-Q Q3 FY2026, debt note); a commercial paper programme backstopped by the 2025 credit
  facility (same note); operating lease obligations of about $12.4B undiscounted at FY2025 (10-K FY2025, material cash
  requirements); shareholders' equity -$7,674M at 2026-06-28; interest paid $588.3M in FY2025 against operating income of
  $2,936.6M; dividends of about $2.83B a year at the current rate against FY2025 owner cash after interest of $1,947M; the
  stored-value card liability and deferred revenue (customers' prepaid money, $1,840.6M current at FY2025) and the Nestle
  deferred revenue ($5,772.6M long-term at FY2025) are liabilities that are not debt (Q4).
- **Q12 (how the money is made).** A coffeehouse chain; none of the businesses the rows name. Unions represent partners
  in about 6% of US company-operated stores; litigation "associated with labor union organizing efforts" is disclosed as
  not material (10-K FY2025 Item 1A and Note 16). The labour board's decisions were not read (a gap, SELF-AUDIT).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (aa564f4a); written question by question; committed after each (the first
      session to Q4, last 14213758; this resume: Q5 315ba74b, Q6 d05ab82a, Q7 39c5e19f, and the close).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock and the fold are the dispatching session's
      (operator rule ten) and were not checked by me. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination in the resume
      session, declared and not used:** the session's opening git status listed research folders of AYI and ARCB and other
      dated daily digests, and the recent commit subjects named the RPM and PNR folds with RPM's box and figures; the
      memory index loaded at start carries lines on the queue state, the count of gate-clearers and owed holding reviews.
      None names Starbucks; none was opened.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check_quotes.py`: 0 problems); every
      filing fact carries its accession or names its filing in Step 0's list.
- [x] The order was kept: Q5 (a STOP) was answered before Q7; Q3, Q4 and Q6 are weighings carried; Q7 failed and closed
      the file; nothing after it is answered.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price is an aggregator quote, flagged in Step 0.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations, Q2 to Q7); facts for later questions are
      under AFTER THE STOP. Q5 was reached and judged, so the box line carries no integrity flag.
- [x] Not a point-in-time run; no row dated after the run date is cited.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before the closing commit.
- **What I could not get, or chose not to:** (1) the labour board's decisions on the organising campaign, which are not SEC
  filings; Q5's integrity verdict rests on the filings read; (2) China's owner cash, which is not filed separately, so 60%
  of the deal's enterprise value stands in for it (a confessed convention); (3) a maintenance figure, which the filer does
  not give; (4) the chief executive's record at his former employer, in filings not read; (5) for FY2016 to FY2020 interest
  income was not netted in the unlevered add-back (the figures used were filed only from FY2021 in my series), which raises
  the first cycle a little and lowers the shown growth a little; (6) the price and the sovereign were not refreshed on
  2026-10-11, since the result is not close to either.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things, all in Q7's specifics. (1) Specific (a) says a year is aberrational "on the filer's own description" and then
asks for the last full cycle "peak to peak or trough to trough", but this filer describes disrupted years (the pandemic, the
restructuring) and never a peak; I took two five-year blocks each ending in a disrupted year and confessed it. (2) The cycle
average of the first block holds the pandemic year (unlevered owner cash of 181), so the growth between cycles (8.5% a year)
is lifted by exactly the "base year in which earnings were poor" that **[L2005-003]** warns of; specific (a) guards the end
years of the window but not a poor year inside a cycle average, and the 8.5% contradicts Q3's finding that the decade's
capital bought no growth in owner cash. The range convention says the growth is "capped by the growth arithmetic of Q3", but
Q3 is a weighing with no number, so the cap could not be applied as a number; I carried 8.5% as the top and said why it is
weak. It did not decide the box: the price fails the floor on that case too. (3) Specific (f)'s share-of-sales cap does not
say which sales the year-ten owner cash is set against; read against sales carried at their own growth it does not cut,
read against today's sales it would cut the rate to the 7.6% sales growth and lower the top a little; I used the first and
say so here. (4) Specific (c) values a deal closed after the window "on its own filed record, its financing added to today's
net debt", written for a purchase; for a sale of part of a business whose cash is inside the base and is not filed
separately there is no rule, and I confessed 60% of the filed enterprise value as the value given. (5) A prepaid royalty
received in operating cash (Nestle's $7B in FY2018) is neither an acquisition, a divestiture nor working capital in the
specifics' terms; I removed it from the cycle base as a convention of this run and showed the variant that keeps it. Also
noted, outside Q7: Q5's integrity test reaches conduct toward employees through the front-page row **[M2016-033]**, but the
run brief's evidence list (proxy and Item 5.02 8-Ks) does not reach the labour board's record, which is where that conduct
would show for this company.
