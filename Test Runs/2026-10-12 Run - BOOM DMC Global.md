# Company Run — DMC Global Inc. (Nasdaq: BOOM) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run (operator rule 10). Quotation marks in this file: words in "double quotes" placed before a bold id
are that ledger row's own words; words from the company's filings are set in ‘single quotes’ with the accession beside
them; everything else is my wording. Dollar figures are USD; "M" is millions. Working folder:
`Test Runs/_research 2026-10-12 BOOM/` (`calc.py` and `calc_out.txt` hold every computed figure below; `check_cites.py`
is the citation check).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-12, after the run was committed: `PORTFOLIO.md` read for this one ticker; not held.*

**Contamination, declared:** (1) the first directory listing of `Test Runs/` that I made to check for a clash of file
names returned, by a pattern on "DMC" and "Dynamic", three names: `2026-09-25 Run - DMC Del Monte Corp.md`, its research
folder, and `2026-10-06 Run - GD General Dynamics.md`. They are other companies (Del Monte, General Dynamics); none was
opened, and nothing of them is used. No file about DMC Global, Dynamic Materials or BOOM appeared. (2) `git log` shows the
subjects of the DSGR run and fold of 2026-10-12 (another company); not used. (3) The session's memory index names the
queue's general state; it says nothing of this name. Nothing else from the blind list was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.66 (close 2026-10-09, the last close before this run; `tools/run.py`, an aggregator quote, flagged per
  operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.05 par, **20,540,949** shares as of
  2026-07-22 (10-Q for the quarter to 2026-06-30, filed 2026-07-29, accession `0000034067-26-000048`;
  `python Screens/cover_shares.py BOOM`). Checked against the 10-Q balance sheet of the same filing: 21,559,103 shares
  issued less 1,018,154 shares of treasury stock and stock held for deferred compensation = 20,540,949, exact. The
  company also has ‘Stock Purchase Rights’ registered (the rights plan, see Q6 facts below); no second share class.
  Filings after the 10-Q: an S-8 of 2026-05-13 (plan shares, before the 10-Q), 13G filings of 2026-07-28 and 2026-08-14
  (holders' reports), no 8-K or prospectus after 2026-07-29 (EDGAR submissions list read 2026-10-12). No adjustment.
- **Market cap:** 20.540949M × $5.66 = **$116.3M**.
- **Sovereign for the earnings currency:** USD, **5.60%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-09 (`python tools/sources.py`, issuing authority). Earnings currency: USD (the reporting currency; about 10% of
  2025 sales were in other currencies, mainly the euro, 10-K Item 7A).
- **Filings read** (operator rule 4):
  - 10-K for fiscal 2025, filed 2026-02-23, accession `0000034067-26-000009`: Item 1, Item 1A, Item 7 in full; Item 8
    cash-flow statement, Note 2 (redeemable noncontrolling interest), Note 11 (segments), Legal Proceedings.
  - 10-Q for the quarter to 2026-06-30, filed 2026-07-29, `0000034067-26-000048`: balance sheet, Note 2, debt note,
    segment tables, MD&A on DynaEnergetics, liquidity.
  - Proxy (DEF 14A) filed 2026-03-31, `0000034067-26-000022` (fetched; read only for the facts recorded after the stop).
  - 8-Ks: 2026-03-05 `0000034067-26-000011` (cash awards in lieu of equity), 2026-04-27 `0000034067-26-000028` (Amendment
    No. 2 to the rights agreement), 2026-05-14 `0000034067-26-000038` (annual meeting votes), 2026-07-29
    `0000034067-26-000047` (results release cover). Schedule 13D/A of 2026-02-24 `0000921895-26-000546` (holder's report).
  - For the span: 10-K fiscal 2023 `0000034067-24-000025`, fiscal 2021 `0000034067-22-000023`, fiscal 2020
    `0000034067-21-000015` (segment tables, cash-flow statements, the patent passages).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025,
  $53,534 thousand on the face of the consolidated statement of cash flows (10-K `0000034067-26-000009`), equals the
  tagged figure `tools/run.py` prints ($53.5M). Cash paid for interest in 2025, $4,952 thousand, and 2025 stock-based
  compensation added back in operating cash, $5,542 thousand, read from the same statement.
- `python tools/run.py BOOM` arithmetic lines only (Part VII; its rule and id lines not read): operating cash 2023 to
  2025 $65.9M, $46.6M, $53.5M; capital spending $16.0M, $17.3M, $16.5M; depreciation and amortization $36.5M, $35.0M,
  $34.0M (of which amortization of Arcadia's purchased intangibles $21.2M in 2024 and $19.1M in 2025, 10-K Item 7);
  stock pay $10.3M, $6.9M, $5.8M (the tagged expense; the cash-flow add-back is $5.5M in 2025, used below). The run.py
  "5-yr window" includes 2021, the year of the Arcadia purchase, and is not used; the recast is in Q7's computation.

**The lines of evidence, chosen from the 10-K and why** (the brief's one departure: the lines are mine to derive).
From Item 1: (i) the three businesses and their shares of sales, because a company of parts is read part by part
(Q1, Q2); (ii) the Arcadia operating agreement, put and call, because it is the largest claim ahead of the common.
From Item 1A: (iii) DynaEnergetics' customer concentration and the pricing it has lost to consolidation; (iv) its
competition with ‘the industry’s three largest oil and gas service companies’; (v) Arcadia's own statement that
‘barriers to entry are low in certain product lines’; (vi) the dilution and control risk of the put. From Item 7:
(vii) segment operating income and the cause the filer gives for each change; (viii) net debt and the credit facility;
(ix) the floor value of the redeemable noncontrolling interest. Lines (iii), (iv) and (vii) are the castle tests of the
deciding part; (ii), (vi), (viii) and (ix) are the claims on the cash. I chose them because the filer itself names them
as the reasons its results moved, and because the hunt is for the evidence against.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would own this "if the market closed for five years" **[M1997-109]**,
which turns the run to the three businesses and to who has first call on their cash. No macro enters: "macro
conclusions are — just never enter into the discussion." **[M2000-094]**, so the oil price and the building cycle are
read only as properties of the businesses (how volume and price behave through them), never as forecasts. The margin of
safety is an attitude here; the arithmetic is Q7's. The analyst's habits govern the hunt: look for "what’s wrong in
things" **[M2025-013]** and use the reading "to possibly reject your original hypothesis" **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the price ($5.66) is far below the stated book value
per share and below the cash the businesses have produced in recent years, which tempts the reading "cheap"; against it,
the 10-Q states that a put on 40% of Arcadia, exercisable since 2026-09-06, carries a ‘Floor Value’ of $187,080 thousand
and could pass ‘majority voting control of the Company’ to the minority holder (`0000034067-26-000048`, Note 2). (2) The
deciding business, DynaEnergetics, earned 22% on sales in 2019 and 3.8% in 2025; the filer attributes the 2025 fall to
‘lower pricing as a result of industry consolidation and a highly competitive core North American market’
(`0000034067-26-000009`, Item 7). (3) One DynaEnergetics customer was about 26% of consolidated sales in 2025 (Item 1A).
Each is weighed where its question falls.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if bought with the buyer's own money and sized so that its loss is
bearable: "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own exposures (the put, the
credit facility) are the target's, weighed at Q9, not the buyer's conduct. No ruin to the buyer from the purchase itself.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The parts, and which one decides.** DMC reports three businesses with different economics (10-K
`0000034067-26-000009`, Item 1 and Note 11), so it is read by its parts: "lumping them together, as is done in standard
financial statements, impedes analysis." **[L2008-005]**. Under the framework's holding-company paragraph and Q2's
business-of-parts CONVENTION (a part decides at more than half of five-year operating profit, or else the largest), the
five-year segment operating income, 2021 to 2025, from the segment tables of the 10-Ks for fiscal 2025, 2023 and 2021:

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share |
|---|---|---|---|---|---|---|---|
| DynaEnergetics (perforating systems) | 8.2 | 39.1 | 46.4 | 16.2 | 10.4 | 120.3 | 164% of the reported total; 56% of the total before Arcadia's goodwill charge |
| NobelClad (explosion-welded clad plate) | 9.8 | 8.0 | 19.4 | 20.1 | 9.6 | 66.9 | 91%; 31% |
| Arcadia Products (60% owned) | not owned (bought 2021-12-23; no Arcadia sales recorded in 2021) | 4.0 | 21.4 | -143.6 (after a $141.7M goodwill impairment; -1.9 before it) | 4.2 | -114.0 (27.7 before the charge) | negative; 13% |
| Total of the parts | 18.0 | 51.1 | 87.2 | -107.3 | 24.2 | 73.2 (214.9 before the charge) | |

($M. Shares are of the sum of the parts before unallocated corporate cost.) On either reading DynaEnergetics carries more
than half of five-year operating profit, so **DynaEnergetics decides**. It is also the largest part by 2025 sales
(44.3%).

**The test applied to the deciding part.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**, and the product itself may stay opaque so long
as "I understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?"
**[M2011-014]**. The key variables, named "first" because "that is the first step" **[M1998-044]**, are from the filing:
- **Volume**: the number of perforating stages pumped, which follows ‘the level of expenditures by the oil and gas
  industry’ on North American onshore completions (Item 1A). It moves with a cycle no one can forecast (sales $310.4M in
  2019, $146.4M in 2020, $315.0M in 2023, $270.2M in 2025; 10-Ks `0000034067-21-000015`, `0000034067-24-000025`,
  `0000034067-26-000009`). The level ten years out is unknowable, but a cyclical volume is averaged over the cycle at Q7;
  it does not by itself put the economics out of reach.
- **Price and share**: what a component maker can charge ‘international and U.S. oilfield service companies’ (Item 1),
  among them ‘the industry’s three largest oil and gas service companies, which produce perforating systems for their own
  use and also buy systems [...] from independent suppliers such as DynaEnergetics’ (Item 1), with one customer at about
  26% of consolidated sales in 2025 (Item 1A). This is the variable that decides the earning power, and the filings of
  2019 to 2026 show which way it has run. That is a question about the castle, and it can be read from the record.

The economics are legible: a manufactured consumable (detonators, shaped charges, pre-assembled gun systems) sold per
stage to service companies, priced against self-supplying giants and many smaller makers. What I cannot foresee is the
oil cycle, which Q7's cycle base handles, and not the nature of the business. The filer says its market is ‘characterized
by continual technological developments’ (Item 1A); the products named (factory-assembled guns, the IS3 detonator, now
being upgraded to a ‘next generation IS3 detonator’, Item 1) show a steady product race rather than the fast change that
closes Q1, and the routing sends that question to Q2 in any case. The doubt rule, "if you have doubts about something
being into your circle of competence, it isn’t." **[M2002-092]**, is weighed: my doubt is not whether I understand how
the business earns, but whether it will keep earning, which is Q2's question **[M2012-065]**.

The two non-deciding parts, for the record: NobelClad (custom clad plate for chemical, refining and smelting equipment,
‘cyclical in nature’ with order timing ‘difficult to predict’, Item 1) and Arcadia (aluminum storefronts, curtain wall,
interior partitions and luxury windows for the western US building market, Item 1) are both understandable industrial
businesses; neither decides.

- **VERDICT: IN** (on the deciding part, DynaEnergetics; narrowly, and the economics it makes legible are read at Q2).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**; the moat is what "protects excellent returns on invested capital" and
"competitors will repeatedly assault any business "castle" that is earning high returns" **[L2007-004]**.

**The parts table** (section B; shares from the Q1 table, before Arcadia's goodwill charge):

| Part | Share of five-year operating profit | Castle, in one line from the filings | Decides |
|---|---|---|---|
| DynaEnergetics | 56% (164% after the charge) | Read below: shown filling in | **Yes** |
| NobelClad | 31% | A niche process with few usable sites (‘limited availability of sites suitable for cladding operations’, Item 1A) and a premium position the filer claims, against roll bonding, weld overlay and ‘a growing number of smaller companies with explosion welded clad manufacturing capability in China and India’ (Item 1A); not judged further | No |
| Arcadia Products | 13% (negative after the charge) | The filer: ‘barriers to entry are low in certain product lines’ and a ‘competitive bidding environment’ has kept it from passing through costs (Items 1A, 7); goodwill fully written off in 2024; open on the filer's own words | No (an open non-deciding part is carried to Q7 at no growth) |

**The castle tests on DynaEnergetics, each with its filing fact.**

1. *What keeps it standing, and how permanent?* The advantage the filer names is product: factory-assembled,
   ‘Performance-Assured’ gun systems since 2015 and the IS3 detonator (Item 1). Its permanence: ‘No single patent or
   trademark is considered to be critical’ (Item 1), and by 2021 the filer was suing rivals because ‘many of the
   pre-wired carriers in the market incorporate features that violate DynaEnergetics patents’ (10-K fiscal 2021,
   `0000034067-22-000023`, Item 7), with patent litigation cost in G&A in 2021 and 2022 and lower in 2023
   (`0000034067-24-000025`). The design was copied within a few years of launch. The rows say what that means: "usually
   if something can gain competitive advantage very quickly, you have to worry about them losing it quickly, too."
   **[M2002-050]**.
2. *Would it stand without the lord?* Not reached as a separate finding.
3. *The attacker with money.* The attackers are already in: the rivals are ‘large national and multi-national
   companies, including the oil and natural gas industry’s largest oilfield service providers’ with ‘greater financial,
   technical, and other resources’, and ‘many smaller companies capable of competing effectively on a regional or local
   basis’ (Item 1A). The field is the one the rows describe: "there are some industries that are just never going to
   have barriers to entry. And in those industries, you better be running very fast" **[M2012-106]**.
4. *Pricing power.* The opposite of a price rise: 2025 sales fell 6%, ‘largely attributable to lower pricing resulting
   from industry consolidation and a highly competitive core North American market, which reduced net sales by $16,213’
   (thousands; Item 7); in the second quarter of 2026, ‘a decrease in pricing due to a highly competitive environment’
   (10-Q `0000034067-26-000048`). Gross margin 39.5% in 2019, 26.0% in 2020 (`0000034067-21-000015`), 17.4% in 2024,
   16.3% in 2025, 15.9% in the second quarter of 2026. "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained." **[M2005-020]**; here the price is
   being cut.
5. *Unit volume.* Volume follows completions; the 2025 decline is price, not volume, on the filer's own account (above).
6. *Low cost.* No filing claim of the low-cost position for DynaEnergetics; it ‘must continue to provide innovative
   products at competitive prices’ (Item 1A). Not shown.
7. *The brand.* Customers ‘select perforating products based on their leading performance, system compatibility,
   product pricing’ (Item 1). No evidence of asking by name.
8. *Would the customer still choose it over the low bid?* The customers are few and large: ‘significant customer
   concentration and customer consolidation, resulting in certain customers having substantial negotiating leverage,
   which has negatively impacted our pricing, margins and profitability’, one customer about 26% of consolidated sales in
   2025 (Item 1A; about 59% of DynaEnergetics' $270.2M), 22% in the first half of 2026 (10-Q). Three of the largest
   customers also make the product themselves (Item 1). When the buyer is also the rival, the buyer sets the price, the
   case the rows narrate as "he determined our profit, because we looked at his price every day." **[M2023-079]**.
9. *Ask the competitors.* No interview; the competitor row below stands in for it.
10. *Widening or narrowing.* "the number one question you want to ask yourself is whether the — could the competitive
    advantage have been made stronger and more durable" **[M2000-075]**. The record says narrower: operating margin
    22.2% (2019), 4.2% (2020), 4.7% (2021), 14.8% (2022), 14.7% (2023), 5.6% (2024), 3.8% (2025), 3.8% (first half of
    2026). The two activity peaks, 2019 and 2023, show margins of 22.2% and 14.7%; the 2025 margin is below the 2020
    trough's on sales 85% higher. The rows' test: "how wide the moat is and whether it’s likely to widen further or shrink
    on you." **[M1999-108]**.
11. *What could destroy it.* Named by the filer: customer consolidation, self-supply by the largest service companies,
    product obsolescence (‘if our proprietary technologies, equipment, facilities, or work processes become obsolete, we
    may no longer be competitive’) and legislation on fracturing and greenhouse gases (Item 1A). "what can happen — say
    five, 10, 15 years from now — that will destroy, or modify, or reduce the economic strengths" **[M2000-014]**: the
    reduction is already in the accounts.

**The competitor row** (operating margin, segment operating income over segment revenue, from each filer's own 10-K):

| Year | DynaEnergetics | Core Laboratories, Production Enhancement | Halliburton, Completion and Production |
|---|---|---|---|
| 2021 | 4.7% (8.2 / 175.4) | 9.7% (15.2 / 156.6) | 14.7% (1,238 / 8,410) |
| 2022 | 14.8% (39.1 / 264.3) | 9.0% (16.4 / 182.0) | 17.6% (2,037 / 11,582) |
| 2023 | 14.7% (46.4 / 315.0) | 7.1% (12.5 / 176.4) | 20.7% (2,835 / 13,689) |
| 2024 | 5.6% (16.2 / 287.7) | 3.7% (6.6 / 177.7) | 20.4% (2,709 / 13,251) |
| 2025 | 3.8% (10.4 / 270.2) | 6.7% (12.1 / 178.8) | 16.6% (2,128 / 12,782) |
| Five years | 9.2% | 7.2% | 18.3% |

Sources: Core Laboratories N.V. 10-K fiscal 2022 `0000950170-23-002412` and Core Laboratories Inc. 10-K fiscal 2025
`0001193125-26-118177`; Halliburton 10-Ks fiscal 2022 `0000045012-23-000011`, fiscal 2024 `0000045012-25-000010`, fiscal
2025 `0000045012-26-000015`; DMC as in Q1 (all figures $M). **The 10-K names no rival by
name**: it speaks of ‘the industry’s three largest oil and gas service companies’ and ‘independent manufacturers of
perforating products’ without naming them, so the brief's rule (rivals the 10-K names) yields none, and no named
non-filer can be flagged. The two above are my choice: Core Lab's Production Enhancement segment says it ‘has established
itself as a global leader in the manufacturing and distribution of high-performance perforating products’
(`0001193125-26-118177`, Item 1), the nearest independent maker that files; Halliburton is one of the large service
companies that both buy and make perforating systems (my identification, not the filing's). Limits: Core Lab's segment
includes diagnostic services and Halliburton's includes pressure pumping and much else, so the rows compare the layers of
the field, not the same product. Private independent makers could not be compared.

**The field's returns, judged in words** (section C). Over the span the nearest independent component maker earns thin
margins (3.7% to 9.7%), DynaEnergetics' margin has fallen from above that band to its bottom, and the integrated service
company that is both customer and rival earns 18.3% on its sales over the five years against 9.2% and 7.2%, about twice as much. The money in the chain is kept by
the customer. "you can have only two competitors and they’re still terrible businesses, they beat each other’s brains
out." **[M2013-052]**. I do not close on "ordinary returns" alone: the 2019 to 2023 span holds good years, and the
CONVENTION asks for ordinary returns over a full cycle; the close below rests on the castle shown filling in.

**Contrary evidence, written down as found** **[M1997-127]**: the 2022 and 2023 margins (14.8%, 14.7%) show the business
can earn well near an activity peak; NobelClad and Arcadia are not judged here and could be better or worse; the filer
says DynaEnergetics ‘is continuing a series of initiatives designed to reduce costs and increase market share’ (Item 7),
which, if it worked, would be a change for the better, credited only on a full cycle under section C. None of these
reverses the price record: the 2025 and 2026 price cuts came at activity well above the 2020 trough.

**The close.** The deciding part's castle is shown, on the filer's own evidence, to be filling in: the design was copied,
no patent is critical, prices are being cut to consolidated customers who also make the product, and the margin at each
stage of the cycle is lower than at the same stage before. The money test closes it: "If the answer had been yes, we
wouldn’t have done it." **[M2011-015]**, the yes being that a funded rival can take the business, and here rivals and
customers have. Among the rows' three boxes, "in, out, and too hard" **[M2006-013]**, a castle shown open on the evidence
is OUT, and the business whose price a rival sets is on Q2's list of what it rules OUT ("whatever he charged for gas was
my price." **[M2012-109]**). It is not TOO HARD: the answer is not beyond judgment, it is in the accounts. Price does not
reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT** at Q2, on the deciding part (DynaEnergetics): the castle is shown filling in on the evidence.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The template asks for the eight to ten years of balance sheets even when the file closes
before Q4; that reading is under AFTER THE STOP, Q4, and is not weighed.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts carried from the accounts that bear on the people are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Q6's buyback test needs the bottom of Q7's range; Q7 is not reached either, so nothing is written back
here. Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. No business of the company is of a kind the question names; not asked.

---
## COMPUTATION, NOT A CLEARANCE: the value range and the fair price (the owner's reporting figures)
*Arithmetic beneath a closing STOP (operator rule 3). It carries no entry language, decides nothing, and does not
reopen Q2. Every figure is in `calc.py` / `calc_out.txt`; USD millions unless "a share".*

**Owner cash after every real cost** (operator rule 5; never a net-income proxy): net cash from operations less the
stock pay added back in it, less all capital spending, plus proceeds of equipment sold, from the filed cash-flow
statements (10-K fiscal 2025 `0000034067-26-000009` for 2023 to 2025, fiscal 2023 `0000034067-24-000025` for 2021 and
2022). All-equity basis (Q7, On what the floor is earned): cash interest paid added back after tax at the 21% US rate
(a CONVENTION of this run: the rows give no rate; the US group carries a valuation allowance, so the true shield may be
smaller, which would lower these figures by under $1M a year). The company's own cash tax is in the figure (Q7, Whose
tax); no carryforward shelter is priced, because cash tax paid ($10.5M in 2025 on a pre-tax loss, mostly German) runs
above the statutory rate, not below it.

| Year | Operating cash | Stock pay | Capital spending | Owner cash, equity | Owner cash, all-equity | Paid to Arcadia's 40% holder | All-equity, after the minority's cash | Acquisitions | Sales |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | -12.8 | 6.6 | 8.7 | -27.0 | -27.0 | 0 | -27.0 | 285.9 (Arcadia: $261.0M cash plus the $24.9M note to the seller) | 260.1 |
| 2022 | 44.9 | 10.1 | 18.6 | 16.4 | 21.3 | 12.3 | 9.0 | 2.4 (price adjustment) | 654.1 |
| 2023 | 65.9 | 10.3 | 16.0 | 40.0 | 47.3 | 13.5 | 33.8 | 0 | 719.2 |
| 2024 | 46.6 | 6.9 | 17.3 | 22.5 | 28.4 | 10.9 (incl. a $2.5M deemed dividend) | 17.5 | 0 | 642.9 |
| 2025 | 53.5 | 5.5 | 16.5 | 31.5 | 35.4 | 6.4 | 29.0 | 0 | 609.8 |

Depreciation variant (spending replaced by depreciation alone): 2024 $25.8M, 2025 $33.1M against $22.5M and $31.5M on
the spending basis; capital spending ran 1.1 to 1.2 times depreciation. The filing gives no split of maintenance from
growth spending, so the all-spending case is central (specific (e)). Working capital is inside operating cash
(specific (d)).

**The window.** The literal window is 2021 to 2025. 2021 is the merger year: Arcadia was bought on 2021-12-23 and ‘no
sales were recorded’ for it in 2021 (10-K fiscal 2021 `0000034067-22-000023`, segment note). The specific says a merger
inside the window is valued on the combined companies' own averages; Arcadia's own full-year 2021 cash record was not
read (only the combined company files), so the combined base is the four fully combined years 2022 to 2025 (CONVENTION
of this run: the only combined years on file). The deal's financing (a $150M term loan drawn in 2021 and since repaid or refinanced into the present
credit facility, and about $149M of shares issued in 2021) is in today's net debt and share count.

**The minority.** Arcadia is 60% owned. Two readings of the 40% holder's claim, both shown:
- **A (central, by the framework's own net-debt definition, which names borrowings and finance leases only):** the
  owner cash that reaches DMC's holders is consolidated owner cash less the cash actually paid to the 40% holder, and
  claims are net debt at 2026-06-30: debt $59.1M less cash $28.6M = **$30.5M** (10-Q `0000034067-26-000048`; operating
  leases left out, as the convention says).
- **B (beside):** the put is exercised at its floor: DMC owns 100% of Arcadia's cash and owes $187.08M less the $24.9M
  note = **$162.2M** (‘subject to potential working capital adjustments’), added to net debt (claims $192.7M). The 10-Q
  says the put has been exercisable since 2026-09-06, and that its preferred-stock form could give the holder ‘majority
  voting control of the Company’. No 8-K reporting an exercise had been filed by 2026-10-12.

**Growth.** Specific (b): the series changes level sharply, so growth is measured between the halves of the combined
window (2022 to 2023 against 2024 to 2025). Specific (f): where the shown growth carried ten years needs owner cash above
the highest share of sales the series has earned, growth is cut to the business's own sales growth between the same
halves, **-4.5% a year** (sales $686.6M to $626.3M average). Under A the shown growth (+7.4% default pair; +4.3% with
acquisitions left out) rests on the minority's distributions falling, not on the business; carried ten years it would
need 5.6% to 7.3% of sales against a highest share of 4.8% in the combined years, so it is cut. Under B the shown growth
is already negative (-1.7%). Negative growth is the bottom of the range and no growth the top (specific (b)). Ten years,
then zero nominal growth, discounted at the 5.60% sovereign.

| Case | Base owner cash | Growth carried | Range, a share | Width | Fair price, a share (each end at 10%, averaged) |
|---|---|---|---|---|---|
| **A, default pair (acquisitions deducted, total growth), all-equity: CENTRAL** | 21.7 | -4.5% (cut from +7.4%) | **$11.77 to $17.40** | 1.42 | **$7.72** |
| A, default pair, equity-only (after interest, no net debt) | 16.2 | -4.5% (cut from +14.2%) | $9.90 to $14.10 | 1.42 | **$6.88** |
| A, acquisitions left out (the filer reports no organic growth; the only acquisition in the combined window is the $2.4M price adjustment), all-equity | 22.3 | -4.5% (cut from +4.3%) | $12.14 to $17.92 | 1.42 | $7.98 |
| B, put exercised at its floor, all-equity | 32.5 | -1.7% | $15.24 to $18.88 | 1.15 | $5.57 |
| B, equity-only | 27.0 | +0.1% | $15.58 to $15.70 | 1.01 | $5.28 |
| Literal window 2021 to 2025, default pair (Arcadia's $285.9M deducted) | -45.2 | not meaningful | not positive (the no-growth case is -$40.78 a share) | n/a | not positive |
| Beside: the (f) cap read on every filing read (2019, before Arcadia: 8.4% of sales), A default all-equity uncut | 21.7 | +7.4% | $17.40 to $32.46 | 1.80 | $12.60 |

**Against the price of $5.66:** the central range (A) is $11.77 to $17.40 and the central fair price $7.72 (equity-only
$6.88); with the put exercised at its floor (B) the fair price is $5.57 (equity-only $5.28), below the price. The
literal window, which charges the Arcadia purchase, gives no positive value. Which reading of the 40% holder's claim
governs moves the fair price from above the price to below it; the run states both and decides between neither, since
the file is closed. Book equity was $11.78 a share at 2025-12-31.

---
## THE BOX
**OUT** at **Q2** (why is the castle still standing), on the deciding part, DynaEnergetics (56% of five-year segment
operating profit before Arcadia's goodwill charge): the castle is shown filling in on the filer's own evidence, with
prices cut to consolidated customers who also make the product and operating margin down from 22.2% (2019) to 3.8%
(2025 and the first half of 2026). Integrity facts recorded, not judged. COMPUTATION beneath the stop: central range
$11.77 to $17.40 a share (A, all-equity, combined window 2022 to 2025, growth cut to -4.5%), fair price $7.72 (equity-only
$6.88); with the Arcadia put exercised at its floor, fair $5.57 (equity-only $5.28); literal window not positive; price
$5.66.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).

**Q3 (capital).** Arcadia was bought for $261.0M cash plus $21.7M non-cash consideration and a $24.9M loan to the seller
(10-K fiscal 2023 `0000034067-24-000025`, cash-flow statement), and its operating agreement sets a ‘Floor Value’ of
$467.7M for 100% (10-Q `0000034067-26-000048`, Note 2). Arcadia's segment operating income was $4.0M, $21.4M, -$1.9M
(before the goodwill charge) and $4.2M in 2022 to 2025; its adjusted EBITDA $25.4M (2024) and $28.6M (2025) (10-K
Item 7). Consolidated capital spending $16.0M to $18.6M a year against depreciation of $13.9M to $14.9M (2024, 2025).
NobelClad's backlog $62.6M at 2025 year-end (Item 1A).

**Q4 (the accounts; the ten balance sheets, read as the template requires).** From `tools/run.py`'s ten-year table
(tagged, first-filed values) checked against the filed 2025 and 2024 balance sheet (`0000034067-26-000009`):
- *Equity against goodwill and intangibles.* Equity $112M (2016), $106M (2017, after a $17.6M goodwill write-off),
  $197M (2020), $361M (2021, after about $149M of shares sold to pay for Arcadia), $410M (2023), $251M (2024), $242M
  (2025). Goodwill $141.3M to $141.7M from 2021 to 2023, then nil after the 2024 impairment; Arcadia's purchased
  intangibles $255.6M (2021) amortized to $155.1M (2025). In 2024 a further $64.3M was charged to equity to carry the
  40% holder's interest at its $187.08M floor (equity statement, ‘Adjustment of redeemable noncontrolling interest’),
  and $4.4M more in 2025; retained earnings went from $146.6M (2023) to nil (2024) to a deficit of $13.5M (2025). The
  redeemable interest sits between liabilities and equity at $187,080 thousand at both year-ends.
- *Cash, receivables and inventory against sales.* Receivables 15.3% of sales in 2019 and 15.4% in 2025; inventory
  13.5% of sales in 2019 and 23.7% in 2025 (Arcadia's model carries more stock). The allowance for doubtful accounts
  rose to $9.8M (2025) from $6.9M, $9.4M of it at DynaEnergetics, where $6.1M was provided in 2025 (Note 2).
- *Debt.* Long-term debt nil (2016), $132.4M (2021), $47.2M (2025); total debt $59.1M at 2026-06-30 with net credit
  facility borrowings of $8.2M in the half year ‘to assist in funding increased working capital’ (10-Q).
- *What the figures do not say.* The balance sheet carries the minority's claim at the floor, not at what Arcadia
  earns; the gap is the contract, not the business.
- *The real costs and the featured figures* (recorded for Q4's weighing and carried toward Q5 by the convention, not
  weighed): amortization of Arcadia's customer relationships, accelerated, $21.2M (2024) and $19.1M (2025); stock pay
  $10.3M (2023) to $5.5M (2025); restructuring and impairment charges in each of 2023 to 2025 ($2.5M in 2024, $3.6M in
  2025) and ‘strategic review and related expenses’ of $7.8M (2024) and $2.7M (2025). The filer features ‘Adjusted
  EBITDA’, ‘Adjusted EBITDA attributable to DMC Global Inc.’ and an ‘Adjusted net (loss) income’ computed ‘prior to the
  adjustment of redeemable noncontrolling interest’ (Item 7): for 2025 that table shows $(0.68) a share before the
  adjustment and $(0.35) ‘As adjusted’, against a GAAP loss of $(0.90) a diluted share after it. Performance shares
  vest on ‘cumulative targeted Adjusted EBITDA’ and ‘Adjusted Free Cash Flow’ (Note on stock compensation); the 2026 cash
  awards for the two segment heads pay on the same two measures (8-K `0000034067-26-000011`). The rows that bear on
  these are listed for the later run, not applied: **[L2016-006]**, **[L2021-003]**.

**Q5 (the people; integrity facts recorded, not judged).** The featured adjusted figures above, which leave out the
transfer of value to the 40% holder and recurring restructuring and review costs, are the habits the convention
carries from Q4 to Q5; any later run that reaches Q5 must answer them **[M2013-088]**. Board: six directors elected
2026-05-13 with between 1.89M and 2.88M shares withheld each against 8.79M to 9.79M for (8-K `0000034067-26-000038`).
CEO James O'Leary (8-K `0000034067-26-000011`); the 2025 10-K records ‘CEO transition expenses’ of $520 thousand
(Item 7). The proxy (`0000034067-26-000022`) was fetched and not read for judgment.

**Q6 (the money and the owners).** (1) The Arcadia contract: the call (DMC's, from 2024-12-23, cash only) and the put
(the holder's, from 2026-09-06 after a December 2024 amendment) both price the 40% at the higher of a value based on the
acquisition price and a multiple of Arcadia's EBITDA, with a floor of $187.08M for the 40% (Item 1; 10-Q Note 2). On a
put DMC may pay 20% in cash and 80% in a new ‘Put Preferred’ paying 3%, issued in a number set at the 60-day average price
of the common and each convertible into one common share, capped at 19.9% of the common until holders vote to lift the cap (the put holder may not vote),
redeemable from 2027-06-23 and in full by the third anniversary, subject to Delaware limits on redemptions that would
impair capital (10-Q, Note 2 and Part II Item 1A). The 10-Q: ‘it is likely that if the Put Preferred is issued, a
stockholder vote to remove the voting and conversion cap would result in the minority interest holder acquiring
majority voting control of the Company through the involuntary dilution of the existing stockholders.’ (2) Shares:
about $149M raised by an offering and an at-the-market program in 2021 (`0000034067-24-000025`); treasury purchases of
$1.2M to $2.5M a year (cash-flow statements); dividends none since 2020 except the $2.5M deemed dividend to the 40% holder
in 2024. (3) A stockholder rights plan of 2024-06-05, extended to 2026-06-04 and, by Amendment No. 2 of 2026-04-24, to
2027-06-04 (8-K `0000034067-26-000028`); Steel Partners and affiliates reported 1,194,441 shares, 5.8%, on Schedule
13D/A of 2026-02-24 (`0000921895-26-000546`). (4) A strategic review of DynaEnergetics and NobelClad from January 2024;
‘no longer actively marketing’ them from October 2024 (Item 1). (5) Long-term incentive awards for 2026 paid partly in
cash ‘given the lack of a sufficient number of available shares’ under the 2025 plan (8-K `0000034067-26-000011`); the
plan was amended and restated and approved on 2026-05-13. Rows for the later run, not applied: **[L2009-019]**,
**[M1995-001]**, **[L2014-012]**.

**Q9 (debt and exposures).** Credit facility with a KeyBank-led group: term loan payable $938 thousand a quarter to
March 2028, $1,250 thousand thereafter, balloon at maturity 2029-02-06; secured by receivables, inventory and fixed
assets including Arcadia; leverage ratio 2.19x at 2026-06-30 against a 3.0x maximum (3.5x for two quarters after a put or
call payment); debt-service coverage 3.28x at 2025 year-end against a 1.25x minimum (10-K Item 7; 10-Q). The put claim
of about $162M (net of the note) against a market value of $116.3M; the 10-K: ‘Debt financing could materially impact
the Company’s leverage while equity financing could materially dilute existing stockholders.’ One customer 22% of
first-half 2026 sales. Explosives at two businesses (Item 1A). Rows for the later run, not applied: **[L2014-024]**,
**[R1997-001]**, **[M2013-076]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `061cd131`); written question by question; committed after each
      (Step 0 `e117b49b`, Q1 `5d8d8454`, Q2 `f5c3894a`, the close in the commit that carries this line).
- [x] Dispatched run: the brief allowed per-question pathspec commits; the lock in `Screens/_daily/` was present (held by
      the dispatcher; I did not touch it). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched beyond the one listing declared
      under contamination (other companies' file names, not opened).
- [x] Every v5 id resolves (`check_cites.py`: ids against `principle_ledger_v5.csv`, every quoted fragment before an id
      found in that row); every filing fact carries its accession; no E-id.
- [x] The order was kept; Q2 closed the run; Q3 to Q12 NOT REACHED; every figure after the stop is headed COMPUTATION,
      NOT A CLEARANCE or recorded as a fact, not weighed.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from
      the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations; Q2); facts for later questions under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` used.
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the commit message).

Honest gaps: Arcadia's own 2021 cash record, Arcadia's EBITDA-multiple put price (only the floor is stated), the
proxy's pay tables, Core Lab's and Halliburton's 2019 to 2020 segment years, and private perforating makers were not
read. The interest add-back at 21% is mine. The parts table counts segment operating income before unallocated
corporate cost.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A put-able minority interest is not in the net-debt definition.** Q7's all-equity basis names ‘borrowings and
finance leases less cash and securities’; a redeemable noncontrolling interest with a contractual floor of $162M (net),
exercisable now and payable partly in convertible preferred that could pass control, is not borrowing, yet it is the
largest claim ahead of the common and larger than the market value. Read literally, the central figure leaves it out and
puts the fair price ($7.72) above the price; counted, the fair price ($5.57) is below it. I showed both and called the
literal one central; the convention should say which governs. (2) **No rule for consolidated subsidiaries with a
minority.** I deducted the cash actually paid to the minority, by analogy with the equity-method rule (dividends
received); the framework says nothing either way. (3) **A merger inside the window whose target's pre-merger year is not
on file.** The specific asks for the combined companies' own averages; when only the acquirer files, the combined
years are fewer than five. I used the four combined years and said so. (4) **Specific (f)'s ‘highest share of sales the
business has earned in the filings read’ is ambiguous across a merger:** the pre-merger company (2019: 8.4%) is a
different business from the combined one (highest 4.8% after the minority's cash). I read it on the combined years and
showed the other reading beside. (5) **Section B's ‘five-year operating profit’ does not say whether an impairment
counts**; here a part's sum is negative with the charge and positive without it. Both readings gave the same deciding
part, so nothing turned on it, but a closer case would. (6) **The brief's competitor rule (rivals the 10-K names)
yields nothing when the 10-K names no rival by name**, as here; I chose the nearest filers and said so.
