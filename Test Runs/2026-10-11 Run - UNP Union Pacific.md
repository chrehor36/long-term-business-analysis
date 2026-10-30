# Company Run — Union Pacific Corporation (NYSE: UNP) — 2026-10-11
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run of 2026-10-11, written question by question by one analyst under the canonical brief
(`Screens/_daily/_dispatch_brief.md`) with the two departures the dispatching brief states: the lines of evidence are
derived here from the 10-K's Items 1, 1A and 7 (listed in Step 0), and the competitors are the rivals the 10-K names.*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-11, after the run was committed: not held (`PORTFOLIO.md` names UNP only in the opportunity set, from a v4.1 run, as watch-list only with no position held).*

**Contamination, declared and not used.** (1) A listing of `Test Runs/` made to check that this run's file name was free
showed the names of four other run files and research folders dated 2026-10-11 (SHOP, SPGI, TECH, TXN); none was
opened. (2) The session's opening context showed the subjects of the latest commits, which are the TXN fold (its box and
figures); not opened, not used. (3) The project's memory index, loaded with the session, carries lines on queue state
and gate-clearer counts; no line names this company. (4) Not a blind-listed file but declared all the same: the v5
ledger itself holds rows in which the speakers name this company, **[M2021-018]** and **[M2021-038]**; under Q2's
convention on a row about one company they are weighed as evidence of a test and of a view at that date, never as a
verdict.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $278.34 (close 2026-10-09, the last close before the run date; printed by `tools/run.py`; **aggregator, live
  quote only, flagged** per operator rule 5). For scale, the 10-K's own figure: $235.10 close on 2026-01-30 (10-K, Item 5).
- **Shares by class** from the latest filing's cover: one class, common stock par $2.50, **594,075,498** as of 2026-07-17
  (10-Q for the quarter ended 2026-06-30, filed 2026-07-23, accession `0000100885-26-000250`;
  `python Screens/cover_shares.py UNP`). Cross-check: the 10-Q balance sheet shows 1,113,359,575 issued and 593,957,035
  outstanding at 2026-06-30 (issued less treasury, 519.4 million treasury shares in the equity statement), which agrees
  within the 0.1 million of option and ESPP issuance between the two dates. No 8-K or prospectus filed after the 10-Q
  (EDGAR submissions list read 2026-10-11: the last filing is the 10-Q and its 8-K of 2026-07-23). The merger would add
  about 225 million shares at closing (10-Q Note 18); not closed, so not counted.
- **Market cap:** 594.075M × $278.34 = **$165.35B**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 10/09/2026, the
  issuing authority (`python tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-06, accession `0000100885-26-000037`: CEO's letter, Items 1, 1A, 1C, 2, 3, 5, 7
    (in full), Notes 18 and 20, the financial statements.
  - 10-Q for the quarter ended 2026-06-30, filed 2026-07-23, accession `0000100885-26-000250`: statements, Notes 14 to 18.
  - DEF 14A filed 2026-03-25, accession `0000100885-26-000098` (Q5, Q6).
  - Merger: 8-K of 2025-07-29 (accession `0001193125-25-168150`, merger agreement); S-4/A of 2025-09-30 (accession
    `0001193125-25-224307`, the deal terms and the reasons); 8-K of 2025-11-17 (accession `0000100885-25-000332`, the
    vote).
  - Other 8-Ks: 2025-12-12 (`0000100885-25-000345`), 2026-05-18 (`0000100885-26-000174`), 2026-07-23
    (`0000100885-26-000249`).
  - Earlier 10-Ks for the cycle, as cited where used; XBRL company facts for the ten-year series (transcription only,
    each year's first-filed 10-K value with its accession, in `_research 2026-10-11 UNP/notes_unp_series.txt`).
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025 **$9,290M**,
  as printed in the 10-K's MD&A cash-flow table and free-cash-flow reconciliation (accession `0000100885-26-000037`),
  equals the `tools/run.py` figure. Also capital investments FY2025 $3,791M (10-K, cash capital investments table) equals
  the tool's capex.
- `python tools/run.py UNP`, arithmetic lines only (full output in the research folder): owner cash (OCF less stock pay
  less capital spending) FY2023 $4,666M, FY2024 $5,776M, FY2025 $5,357M; five-year mean (FY2021 to FY2025) $5,490M on the
  capex basis, $6,644M on the depreciation basis; capex above depreciation in every year (FY2025 $3,791M against $2,465M).
  Finance-lease principal (FY2023 $65M, FY2024 $47M, FY2025 $36M) is shown by the tool as an alternate and is small; it
  is carried in the capital-spending figure at Q7 (all spending deducted). No securities inside operating cash, no
  paid-in-kind interest, no minority dividends. Everything the tool prints as a rule, an id or a verdict was ignored
  (Part VII, the tooling).

**The lines of evidence, chosen from the 10-K's own items** (first departure of the brief):
1. From Item 1 (business): one reportable segment; revenue by commodity group (Bulk 33%, Industrial 37%, Premium 30% of
   freight revenue in 2025); Mexico gateways; 13 unions, about 83% of the workforce. Read: revenue, carloads and average
   revenue per car by group over the cycle; operating ratio over the cycle.
2. From Item 1A (risks): competition from BNSF, trucks and barges (the only railroad named is BNSF); hazardous materials;
   key suppliers of locomotives and rail; regulation by the STB (rates, reciprocal switching, revenue adequacy);
   fuel-price pass-through; reliance on capital markets; the pending Norfolk Southern merger, its conditions, the
   $2.5B termination fee and the new debt. Read: the competitor's filings over the span; the STB process in the 10-Q;
   debt and maturities.
3. From Item 7 (MD&A): pricing ("core pricing gains") against inflation; capital investments by type; the filer's own
   statement that inflation-adjusted depreciation "would be substantially greater than historically reported amounts";
   free cash flow defined after dividends; ROIC "as adjusted" used in executive pay; share repurchases paused for the
   merger. Read: ten years of balance sheets; owner cash after all capital spending; buybacks and their prices; the
   proxy's pay design.
4. From Item 3 (legal): the fuel-surcharge antitrust cases (summary judgment for the railroads 2025-06-24, on appeal);
   environmental sites; personal-injury claims.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this railroad "if the market closed for five
years" **[M1997-109]**, and the answer turns on the cash the network throws off after what it must put back, not on the
quotation, which rose from $235.10 on 2026-01-30 (10-K, Item 5) to $278.34 by 2026-10-09 with no change in the filed
business that this run found; the market "just tells us prices" **[M2006-077]**. No macro forecast enters (tariffs,
coal demand, rates are read only as properties of the business). Who is paid to tell you bears directly: the merger is
a transaction on which, by the speakers' account, "you do not get impartial advice from Wall Street" **[M2020-037]**,
and the S-4's fairness opinions are read as advocacy. **Contrary evidence, written down as found** **[M1997-127]**:
(a) the filer's own MD&A says that at current replacement prices "depreciation charges (on an inflation-adjusted basis)
would be substantially greater than historically reported amounts" (10-K, Other matters, Inflation), so reported
earnings overstate what the owner can take out; (b) total carloads were 8,447 thousand in 2025 against more than 9
million in the middle of the last decade (see Q2), volume the business has not regained; (c) equity fell from $19.9B
(2016) to $12.2B (2022) while debt rose from $15.0B to $33.3B, the gap filled by buybacks, so the 40% return on equity
the 10-K prints is largely made by shrinking equity; (d) the 10-K's own five-year comparison shows UNP's three-year total
return 19.7% against 86.0% for the S&P 500 (Item 5). The analyst's habit applied: look for "what’s wrong in things"
**[M2025-013]**.

## THE STANDING RULE
A part-interest bought for cash, unlevered, sized so that a fall of half or more could be borne, puts the buyer at no
risk of ruin; the rule binds the buyer's conduct, "We are never going to risk what we have and need for what we don’t
have and don’t need" **[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The
target's own debt is weighed at Q9, not here. **Passes for an unlevered buyer.**

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**.
- **What the business is** (10-K, Item 1, accession `0000100885-26-000037`): a single integrated rail network, 32,889
  route miles in 23 western states, one reportable segment; freight revenue $23.2B in 2025 from Bulk (grain, fertilizer,
  food, coal), Industrial (chemicals, plastics, rock, lumber, petroleum) and Premium (automotive and intermodal); the only
  railroad serving all six major Mexico gateways. Its revenue is volume (carloads) times price per car; its costs are
  labour under national agreements, fuel recovered by surcharge with a two-month lag, purchased services, depreciation of
  a long-lived network, and rents.
- **The key variables and whether they are predictable** **[M1998-044]**: (1) volume by commodity, which moves with
  industrial production, harvests, trade and coal burn; the direction of coal is a known secular decline and of the rest
  is broadly the economy's; (2) price per unit of service, which the filings show rising in every year read, with
  volume down or up (Q2); (3) the capital the network must take back each year, which the filer itself says exceeds
  depreciation at today's prices (MD&A, Inflation); (4) regulation, the STB's jurisdiction over rates, switching and
  mergers. None of these turns on a technology the industry's own insiders could not write down; the product, a
  ton-mile on steel wheels, is the same product it was a century ago, and the threats the 10-K names (autonomous or more
  fuel-efficient trucks, size and weight limits, regulation) are slow ones, which Q2 weighs **[M2014-038]**.
- **Do the past statements tell me the future ones?** **[M2008-033]** Yes in shape: ten years of filings show operating
  income between $7.3B and $9.9B, capital spending between $2.9B and $4.7B, and an operating ratio between about 57% and
  63%; the range of outcomes in ten years can be pictured.
- **The pending merger.** If the STB approves, the business becomes a transcontinental railroad with Norfolk Southern
  (10-Q Note 18, accession `0000100885-26-000250`). Norfolk Southern is the same kind of business (a Class I railroad of
  carload, coal, automotive and intermodal freight), so the combined company is inside the same perimeter; what is less
  knowable is the STB's conditions and the integration, which are weighed at Q6, Q7 and Q9, not here.
- **Routing.** Not a fast-changing industry; not a financial institution; one segment, so no parts test is needed.
- **VERDICT: IN.** The economics of a western railroad ten years out can be pictured within a range: the network, its
  product and its cost structure, the commodities it carries and the direction of each, all from the filings. The doubt
  test **[M2002-092]** was asked and does not bite on the understanding of the business; the doubts found are about the
  castle's returns, the capital and the price, which later questions own.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**. Facts below are from UNP's 10-Ks for FY2009 to FY2025 (accessions in
`_research 2026-10-11 UNP/notes_unp_series.txt` and notes.md) and BNSF's 10-Ks.

- **The money test, the attacker with money.** "if I had a hundred million dollars and I wanted to go in and take on
  See’s Candy, could I do it?" **[M2011-015]**. No one can lay a second network of 32,889 route miles into the ports,
  gateways and plants UNP reaches; the rows say it of railroads in general: "You really couldn’t create another
  railroad" **[M2013-054]**, an asset "that couldn’t be duplicated for, you name it, three, four, five, six times, you
  know, what it’s selling for" **[M2012-030]**, which "would be impossible to construct now" **[M2024-058]**. The 10-K's
  own supplier paragraph adds that locomotive and rail suppliers face "high barriers to entry" (Item 1A). No rail
  entrant in the West in the span read: the rail rivals in UNP's territory in 2025 are the same as in 2009 (10-K Item 1A
  names BNSF alone). **Passes.**
- **Ask the competitors** **[M2025-043]**. BNSF's own 10-K for FY2025 (accession `0000934612-26-000004`, Competition):
  "BNSF Railway’s primary rail competitor in the western region of the U.S. is the Union Pacific Railroad Company", and
  of trucks: "The presence of advanced, high service truck lines with expedited delivery, subsidized infrastructure, and
  minimal empty mileage continues to affect the market for non-bulk, time-sensitive freight. The potential expansion of
  longer combination vehicles and deployment of autonomous technology could further encroach upon markets traditionally
  served by railroads." The two western railroads name each other and the truck; neither names a new railroad.
- **Pricing power, the agony before a rise, and the price behaviour through bad years** **[M2005-020]**. "You learn a
  lot about [...] the durability of the economics of a business by observing the behavior of [...] the price behavior"
  **[M2005-020]**. In every year read in which volume fell, the filer reports core pricing gains: 2009 (16% volume
  decline, "core pricing gains" partly offsetting; FY2009 10-K, accession `0001193125-10-023294`), 2015 (carloads down
  6%, "Core pricing gains of 3.7%"; FY2015 10-K, `0000100885-16-000260`), 2016 (carloads down 7%, "our second lowest
  volume levels since 1998", core pricing gains; `0000100885-17-000056`), 2019 (volume down 6%, core pricing gains;
  `0000100885-20-000065`), 2020 (volume down 7% in the pandemic, core pricing gains; `0000100885-21-000068`), 2023
  (volume down 1%, core pricing gains; `0001437749-24-003599`). Through the last inflation, the operating ratio went
  57.2% (2021), 60.1% (2022), 62.3% (2023, "driven by inflation, excess network costs, the ratification charge [...]"),
  then 59.9% (2024) and 59.8% (2025): cost rose faster than price for two years and price caught up within two more,
  the pattern the rows describe, "over time the businesses with strong competitive positions manage to pass through
  increases in raw material costs [...] But you get these temporary situations where, sometimes, the costs are
  increasing faster" **[M2005-017]**. Over the span the operating ratio improved from 67.8% (2012) and 63.5% (2014) to
  about 60%. **Passes**: no prayer session is visible; the price held in every downturn read.
- **Unit volume and share of mind.** Weighs against. Total revenue carloads: 9,048 thousand (2012), 9,625 (2014, the
  peak read), 8,442 (2016), 8,908 (2018), 7,753 (2020), 8,447 (2025). Volume in 2025 is 12% below 2014. The largest cause
  is coal: coal revenue $4,127M of $22,560M freight revenue in 2014 (FY2014 10-K, `0001193125-15-037518`) against coal
  and renewables $1,786M of $23,220M in 2025; the rows call that decline "for sure, [...] secular" **[M2016-021]**. The
  business lost more than half of its coal revenue and still grew freight revenue from $22.6B to $23.2B, on price.
  Volume decline is not a fail by itself, "it will have unit declines over a period of time, but I think we’ll do fine"
  **[M2015-066]**, but a business that grows only on price, with fewer units, is drawing on its castle rather than
  widening it, and that is written down here as the strongest single fact against.
- **The low-cost position.** Against the truck, rail is the low-cost carrier of bulk over distance (the 10-K cites the
  AAR: three to four times more fuel-efficient than trucks; Item 1), but the 10-K concedes that motor carriers "generally
  have an advantage over railroads with respect to transit times and timeliness of service" and use "public
  rights-of-way maintained by public entities" while the railroad must "build or acquire and maintain" its own (Item 1A).
  The low-cost position holds for bulk and long haul and is contested in Premium (intermodal and automotive, 30% of
  freight revenue). Against BNSF, the rival rail network: UNP's operating ratio was lower than BNSF's in every year
  compared (below).
- **Would the customer still choose it over the low bid?** For a shipper of grain, coal, chemicals, rock or soda ash
  on a line served by one railroad, there is no low bid by rail; the 10-K names barge, truck and "product or geographic
  competition" as the substitutes (Item 1A). For intermodal, the customer can and does take the truck.
- **Widening or narrowing** **[M1999-108]**: on margin, widening (operating ratio 67.8% to 59.8%, 2012 to 2025); on
  volume, narrowing (carloads down 12% from the 2014 peak); on service, the 2025 metrics are the filer's "best-ever"
  (10-K MD&A), which this run reads as management's claim, not as evidence of the moat.
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: (1) regulation: the STB
  "continues to explore changes to the methodology for determining railroad revenue adequacy, the possible uses of
  revenue adequacy in regulating railroad rates, and ways to regulate service" and is reviewing reciprocal switching
  (10-K Item 1); the rows record a regulated moat that broke, "I did not anticipate or even consider the adverse
  developments in regulatory returns" **[L2023-011]**, and "railroads, utilities, insurance companies, are all very much
  affected by the political process" **[M2012-074]**; (2) the autonomous or longer truck (both railroads' 10-Ks);
  (3) the continued fall of coal; (4) trade with Mexico and Asia (Item 1A). None of these, on the filings, empties the
  castle within ten years; (1) and (2) could narrow it, and they are carried to Q7 as reasons the range stays modest.
- **Change for the better, credited on a full cycle.** The rows record the railroads' change: "the railroads were a
  terrible business for decades and decades and decades and then they got good" **[M2017-026]**; "We were slow to
  recognize the change" **[L2022-020]**. The framework credits such a change "only on the evidence of a full cycle in
  which the price behaviour held". That evidence is in the filings: volume fell in 2009, 2015 to 2016, 2019 to 2020 and
  2023, and the price behaviour held in each (above). **Credited**; no TOO HARD (NATURE) on this ground.

**The competitor row** (the 10-K names one rail rival, BNSF; Burlington Northern Santa Fe, LLC files a 10-K with the
SEC; trucks, barges, ships and pipelines are named only as classes, so no further named rival exists to compare).
Operating ratio, operating expenses over operating revenues, from each filer's own statements; BNSF's figures carry
Berkshire's purchase accounting (pushed-down step-up in depreciation since 2010), which raises its depreciation and so
flatters UNP in the comparison by an amount not stated in either filing.

| Year | UNP revenue $M | UNP operating ratio | BNSF revenue $M | BNSF operating ratio |
|---|---|---|---|---|
| 2014 | 23,988 | 63.5% | 23,239 | 69.8% |
| 2016 | 19,941 | 63.5% | 19,829 | 66.3% |
| 2018 | 22,832 | 62.7% | 23,855 | 67.3% |
| 2020 | 19,533 | 59.9% | 20,869 | 62.9% |
| 2021 | 21,804 | 57.2% | 23,282 | 62.2% |
| 2022 | 24,875 | 60.1% | 25,888 | 66.8% |
| 2023 | 24,119 | 62.3% | 23,876 | 69.0% |
| 2024 | 24,250 | 59.9% | 23,437 | 68.1% |
| 2025 | 24,510 | 59.8% | 23,421 | 65.6% |

Sources: UNP 10-Ks (operating ratio as printed; 2016 as printed in the FY2016 10-K, 63.7% as restated in the FY2020
10-K); BNSF 10-Ks FY2015 (`0000934612-16-000034`), FY2020 (`0000934612-21-000005`), FY2025 (`0000934612-26-000004`)
and XBRL company facts for the years between, BNSF ratio computed here as one less operating income over revenues.
Volume: UNP carloads fell from 9,625 thousand (2014) to 8,447 (2025); BNSF cars and units from 10,275 thousand (2014)
to 9,622 (2025) (BNSF FY2015 and FY2025 10-Ks). Both western railroads lost units over the span; both held price; UNP
earned the better margin in every year compared. Capital spending against depreciation, 2025: UNP $3,791M against
$2,465M; BNSF $3,797M (capital expenditures excluding equipment $3,272M plus equipment $525M) against $2,737M of
depreciation and amortization. Both spend about one and a half times their depreciation.

**The parts table.** One reportable segment (10-K Item 1: "we treat the financial results of the Railroad as one
segment due to the integrated nature of our rail network"); the commodity groups report revenue, not profit. No parts
test.

**The field's returns over the last full cycle, judged in words.** UNP's operating income against its net property:
$7,272M on $50,389M (2016, 14.4% before tax), $7,834M on $54,161M (2020, 14.5%), $9,846M on $59,645M (2025, 16.5%);
the filer's own after-tax "return on invested capital as adjusted" 15.5% (2023), 15.8% (2024), 16.3% (2025) (10-K MD&A).
BNSF's operating income against its net property of $72,372M (2025) is 11.1% before tax, on a base written up to
Berkshire's 2010 purchase price and with $15.4B of goodwill beside it, so not comparable to UNP's historical cost. On
the capital actually employed, at historical cost, the field's better player earns well above an ordinary return
through the full cycle, troughs included (2016 and 2020 at 14.4% and 14.5% before tax). The other side is stated by the
filer and by the speakers: at replacement cost the return is far lower, "depreciation charges (on an inflation-adjusted
basis) would be substantially greater than historically reported amounts" (10-K, Other matters), and of the rival
"what it earns in its - relation to its replacement value is a pittance" **[M2024-058]** (a row about one company, read
under Q2's convention as the speakers' view of BNSF at that date, not a verdict on UNP). This run reads the castle test
on the capital the business actually has, as the rows define the return, "in terms of the capital actually needed in
the business" **[M2010-090]**, and carries the replacement-cost point to Q3 and Q4, where it governs what must go back
in. Judged in words: not ordinary on the capital employed; modest on the capital it would take to rebuild, which no
one will spend.

- **VERDICT: IN.** The castle stands for a reason that is permanent on any horizon the filings allow, that no one can
  build another western railroad **[M2013-054]**, and the price behaviour held through four volume downturns in sixteen
  years **[M2005-020]**, so the change for the better is credited on a full cycle **[M2017-026]**. Written down against
  it and carried: volume 12% below its 2014 peak, a secular loss of coal **[M2016-021]**, the truck's hold on
  time-sensitive freight, and a regulator that can reprice the castle **[L2023-011]**. The moat is not "tenuous"
  **[M2000-019]** on the evidence; it is a moat around a business whose units are shrinking, which Q3 and Q7 must
  weigh.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The question: "does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**, and of
the added capital, the second-best grade, "It takes more money, but the rate at which you invest — reinvest — the money
to get that growth is a very satisfactory rate" is the test **[M1998-081]**.

**Capital spending against depreciation, every year of the span** (10-Ks; capex = "capital investments" in the cash-flow
statement; $M):

| Year | Capex | Depreciation | Ratio | Net property | Operating income |
|---|---|---|---|---|---|
| 2015 | 4,650 | 2,012 | 2.31 | 48,866 | 8,052 |
| 2016 | 3,505 | 2,038 | 1.72 | 50,389 | 7,272 |
| 2017 | 3,238 | 2,105 | 1.54 | 51,605 | 8,061 |
| 2018 | 3,437 | 2,191 | 1.57 | 52,679 | 8,517 |
| 2019 | 3,453 | 2,216 | 1.56 | 53,916 | 8,554 |
| 2020 | 2,927 | 2,210 | 1.32 | 54,161 | 7,834 |
| 2021 | 2,936 | 2,208 | 1.33 | 54,871 | 9,338 |
| 2022 | 3,620 | 2,246 | 1.61 | 56,038 | 9,917 |
| 2023 | 3,606 | 2,318 | 1.56 | 57,398 | 9,082 |
| 2024 | 3,452 | 2,398 | 1.44 | n/r | 9,713 |
| 2025 | 3,791 | 2,465 | 1.54 | 59,645 | 9,846 |

(Each year's first-filed 10-K value, from the XBRL company facts with accessions in the research folder; 2025 from the
10-K and the 10-Q's comparative balance sheet; 2024 net property not pulled, not needed.)

- **Return on the capital actually needed** **[M2010-090]**, at historical cost and "return on tangible assets"
  **[M2011-060]** (no goodwill on UNP's balance sheet): operating income over net property 16.5% before tax in 2015,
  14.4% at the 2016 trough, 14.5% at the 2020 trough, 16.5% in 2025; the filer's after-tax ROIC 15.5% to 16.3%
  (2023 to 2025). Not cyclical-peak returns: the troughs are within two points of the peaks.
- **What the added capital earned.** From 2015 to 2025 net property rose $10.8B (48,866 to 59,645) and operating income
  $1.8B (8,052 to 9,846): about 17% before tax on the increment, at historical cost. But most of the gain came from price
  and productivity, not from new volume (carloads fell from 9,062 thousand in 2015 to 8,447 in 2025), so the increment
  is better read as the capital needed to keep the network competitive while price rose than as capital that bought
  growth.
- **To stand still, and to grow** **[L1999-024]**, **[M2000-144]**. The filer splits its 2025 spending (10-K, cash
  capital investments table): road infrastructure replacements $1,987M; locomotives and freight cars $810M (including
  $311M of lease buyouts); technology and other $377M; capacity and commercial facilities $617M ("line expansion and
  other capacity projects" $258M, "commercial facilities" $359M). The maintenance guess this run makes from that split,
  stated as a guess: replacements plus equipment plus technology, about $3.2B, against depreciation of $2.47B; growth
  spending about $0.6B. The filer's own inflation note says replacement at current prices would carry depreciation
  "substantially greater than historically reported amounts", so the depreciation charge is not the maintenance figure,
  which is what the rows say of every railroad: "merely spending their depreciation expense will not keep them in the
  same place" **[M2016-092]**, and "BNSF must annually spend more than its depreciation charge to simply maintain its
  present level of business" **[L2023-009]** (a row about one company; read as the same test applied, and the BNSF
  figures above show the same ratio).
- **Compulsory reinvestment.** The spending is not optional: "you have to spend money like crazy if it’s attractive to
  spend money, and you have to spend it the same way if it’s unattractive" **[M1998-128]**; the speakers "have tried to
  avoid places where there was a lot of compulsory reinvestment just in order to stand still" **[M1997-016]**, and say of
  railroads in inflation that "it just keeps eating up more and more money, and your depreciation charges are inadequate"
  **[M2015-049]**.
- **The growth arithmetic and its caps.** Owner cash (Q4, Q7) rose from $3,938M (2016) to $5,357M (2025); freight
  revenue only from $22,560M (2014) to $23,220M (2025). Growth has come from price on a shrinking unit base, financed by
  spending about one and a half times depreciation. A rate of growth that requires price to keep outrunning cost while
  volume falls is the rate Q7 must not carry past the discount rate or past the business's own sales growth.
- **The second best, named.** The rows accept this class: "we are today quite willing to enter businesses that
  regularly require large capital expenditures. We expect only that these businesses have reasonable expectations of
  earning decent returns on the incremental sums they invest" **[L2009-012]**; "as the second-best choice, still a good
  choice, the answer is yes. It’s not as good as the best choice" **[M2018-055]**. On historical cost UNP clears
  "decent"; on replacement cost the speakers' own word for the rival is "a pittance" **[M2024-058]**.
- **WEIGHS AGAINST**, as the rows' second-best grade, not as a bar: decent returns on the capital at historical cost and
  on the increment, but a compulsory reinvestment above depreciation every year to stand still **[M1997-016]**,
  **[M2016-092]**, with the growth in owner cash bought by price on falling volume. (The "little or no debt" criterion of
  **[R1997-001]** is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (`tools/run.py`, each year's
first-filed XBRL value, accessions in the research folder; June 2026 from the 10-Q; $M):

| Year-end | Assets | Liabilities | Equity | Cash | Receivables | Debt | Retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 55,718 | 35,786 | 19,932 | 1,277 | 1,258 | 15,007 | 32,587 |
| 2017 | 57,806 | 32,950 | 24,856 | 1,275 | 1,493 | 16,944 | 41,317 |
| 2018 | 59,147 | 38,724 | 20,423 | 1,273 | 1,755 | 22,391 | 45,284 |
| 2019 | 61,673 | 43,545 | 18,128 | 831 | 1,595 | 25,200 | 48,605 |
| 2020 | 62,398 | 45,440 | 16,958 | 1,799 | 1,505 | 26,729 | 51,326 |
| 2021 | 63,525 | 49,364 | 14,161 | 960 | 1,722 | 29,729 | 55,049 |
| 2022 | 65,449 | 53,286 | 12,163 | 973 | 1,891 | 33,326 | 58,887 |
| 2023 | 67,132 | 52,344 | 14,788 | 1,055 | 2,073 | 32,579 | 62,093 |
| 2024 | 67,715 | 50,825 | 16,890 | 1,016 | 1,894 | 31,192 | 65,628 |
| 2025 | 69,698 | 51,231 | 18,467 | 1,266 | 1,860 | 31,814 | 69,529 |
| Jun 2026 | 71,211 | 50,538 | 20,673 | 1,614 (+500 short-term investments) | 2,130 | 30,327 | 71,584 |

**What the figures say.** (1) **No goodwill or acquired intangibles**: the assets are the network (net property
$59.6B of $69.7B at 2025) and the $2.0B TTX car-pool interest. (2) **Retained earnings more than doubled ($32.6B to
$69.5B) while equity fell** from $19.9B to a low of $12.2B in 2022: the difference is treasury stock, $58.8B at
2025-12-31 (10-K balance sheet), the buybacks of the decade (Q6). (3) **Debt more than doubled**, $15.0B to $33.3B
(2022), then eased to $30.3B (June 2026) after the buybacks paused: the buybacks were funded largely by borrowing. (4)
The 2017 jump in equity is the Tax Act's remeasurement of deferred taxes (2017 net income $10,712M against $5,966M in
2018; income tax a credit of $3,080M in 2017; XBRL `0000100885-18-000048`), a book gain with no cash in it. (5)
Receivables against revenue moved from 6.3% (2016) to 7.6% (2025), and materials and supplies from $787M to $919M in
the first half of 2026 with revenue up 7%: no building of receivables, inventories or prepaid accounts out of line with
sales **[M1995-064]**. (6) Deferred income taxes of $13.4B sit as a liability that grows with the network; not read as
equity. (7) The debt's fair value, $24.7B against $30.3B carried (10-Q, Note 13, fair value of financial instruments), says the debt is long and fixed, at
coupons below today's rates (no variable-rate debt, 10-K Item 7).

**What they don't say and can't say.** They cannot say what it costs to replace the network; the filer itself says
"assuming that we replace all operating assets at current price levels, depreciation charges (on an inflation-adjusted
basis) would be substantially greater than historically reported amounts" (10-K, Other matters, Inflation). They don't
say how much of the spending is maintenance (Q3 makes the guess). And the 40.4% "return on average common
shareholders' equity" the 10-K prints (MD&A) is not a measure of the business: "if you keep the equity low enough by
buying shares back, why, you could make return on equity whatever you want" **[M1998-017]**; "we could make it almost
any number you want if we just used enough leverage" **[M2001-054]**.

**The real costs.**
- **Depreciation** is short of the cost of standing still (above, and Q3): "the depreciation charge we record in our
  railroad business falls far short of the capital outlays needed to merely keep the railroad running properly [...]
  (This overstatement of earnings exists at all railroads.)" **[L2015-004]**. The owner-cash figure carried to Q7 therefore
  deducts all capital spending, not depreciation.
- **Stock pay** $142M in 2025 ($118M 2024, $107M 2023; 10-K cash-flow statement), expensed in the income statement and
  deducted in owner cash.
- **The recurring "one-time"**: crew-staffing agreement ratification charges in 2023, 2024 and 2025 (10-K MD&A: "higher
  crew staffing agreement ratification charges in 2025 as we reached agreements in both years") are excluded from the
  "adjusted" figures of the earnings releases (8-K of 2026-07-23, Exhibit 99.1, accession `0000100885-26-000249`); three
  years running is a cost of doing business **[L2016-007]**. Owner cash carries them, being cash.
- **Non-operating help in the reported growth.** The 10-K's CEO letter leads with "an 8% increase in earnings per share"
  for 2025; operating income rose 1% ($9,713M to $9,846M). The rest came from $250M of industrial-park land sales in
  other income, a $115M deferred-tax benefit from Kansas legislation, purchased tax credits and fewer shares (10-K MD&A,
  Non-operating items). The land sales and the tax items are not the railroad's earning power.
- **Pensions**: funded at 2025 (10-K MD&A), expected return on assets 5.25%, a net periodic benefit of $14M in 2025;
  not fanciful.
- **Taxes**: cash taxes paid are in OCF; H.R.1's bonus depreciation added "$0.3 billion" to 2025 operating cash (10-K
  MD&A), a deferral that recurs while the spending continues; not removed, but noted.

**EBITDA in the filer's own mouth.** Only as "adjusted debt / adjusted EBITDA", presented as the rating agencies' leverage
measure (10-K MD&A; 8-K Exhibit 99.1), never as earnings. The speakers' coverage measure is "pre-tax earnings/interest,
not EBITDA/interest" **[L2012-002]**; on that measure 2025 coverage is $9,166M of pre-tax income plus $1,309M interest,
over $1,309M, about 8.0 times (Q9).

**The habits carried to Q5** (a WEIGHING here, judged there): (a) **guidance**: the 2026-07-23 release (8-K Exhibit 99.1)
says "Reported earnings per share growth increased to high-single digit; consistent with attaining 3-year CAGR target of
high-single to low-double digit through 2027" under the heading "On Track with Investor Day Targets", that is, a
published multi-year earnings target and progress reports against it, "the scourge of earnings "guidance" and the desire
of CEOs to "hit the number."" **[L2019-006]**; (b) **an adjusted figure featured**: the release's first bullet gives
"Diluted earnings per share (EPS) of $3.36 and adjusted diluted EPS* of $3.41", reported first; the adjustments run both
ways (2025's adjusted figure was below GAAP, removing the Kansas tax benefit; 2026's removes acquisition costs), which
is the milder form, but "a management that regularly attempts to wave away very real costs by highlighting "adjusted
per-share earnings" makes us nervous" **[L2016-006]**; (c) **free cash flow** is defined by the filer after dividends
paid (10-K MD&A), an unusual definition that makes no claim to be owner earnings and is not used here.

- **VERDICT on the accounts: WEIGHS AGAINST; no STOP.** The accounts are not confusing and raise no suspicion of the kind
  that closes the file **[M1995-063]**: no goodwill, no reserves moving with a deal, no receivables or inventories out of
  line, and the filer itself states the depreciation shortfall that most hurts its reported figures. They weigh against
  because reported earnings overstate owner cash by the depreciation shortfall **[L2015-004]**, the headline return on
  equity is made by buybacks and debt **[M1998-017]**, and the 2025 per-share growth leaned on land sales and tax items.
  The guidance and the adjusted figure are carried to Q5, where "we find it so frequent that we can’t afford to use it as
  a total exclusionary factor" **[M1994-018]** is read beside the integrity record.
- **Recast earnings for Q7**: owner cash = cash from operations less stock pay less all capital spending (finance-lease
  principal added to spending): FY2021 $5,902M, FY2022 $5,552M, FY2023 $4,601M, FY2024 $5,729M, FY2025 $5,321M;
  before interest, add interest after the company's own effective tax rate (Q7 table).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**Who.** V. James Vena, chief executive since 2023-08-14, age 67, a railroad operator who was UNP's chief operating
officer in 2019 and 2020 (10-K, executive officers); chief financial officer Jennifer Hamann, 34 years at the company
(DEF 14A, accession `0000100885-26-000098`); an independent, non-executive chairman, Michael McCarthy (10-K, directors).
The company has "No Employment Agreements with any of our Executive Officers" (DEF 14A).

**The two yardsticks** **[M1994-008]**. (1) *How well they run it, against the hand dealt and the competitor:* the
operating ratio under the present team went from 62.3% (2023, the year Vena arrived in August) to 59.9% (2024) and
59.8% (2025), against BNSF's 69.0%, 68.1% and 65.6% (Q2 row); workforce productivity, terminal dwell, train length and
fuel rate at the filer's best levels (10-K MD&A; 8-K of 2026-07-23). Volume grew 3% (2024) and 1% (2025) after years of
decline. The hand: the same network, labour agreements and coal decline the predecessors had. (2) *How they treat the
owners:* the proxy is read for "how they treat themselves versus how they treat the shareholders" **[M1994-009]** (Q6,
Part B, below): CEO total compensation $20.3M (2025), $17.6M (2024); pay ratio 151 to 1; Vena owns 98,258 shares
including 92,885 exercisable options, and holds 215,310 unvested stock units (DEF 14A, security ownership).

**The integrity record, read for doubt** **[M2013-088]**.
- No restatement; no material weakness; the auditor's report on internal control is clean (10-K Item 9A); no SEC or DOJ
  investigation of the company or its officers disclosed in the 10-K's Item 3 or Note 17 or in the 10-Q.
- The litigation of record is the fuel-surcharge antitrust case brought in 2007 against four Class I railroads; the
  district court granted all railroads summary judgment on 2025-06-24, now on appeal (10-K Item 3). An industry
  practice under appeal, decided for the railroads so far; not a finding against these people.
- *Candour.* The 10-K's MD&A states unprompted the fact most damaging to its own earnings, that inflation-adjusted
  depreciation "would be substantially greater than historically reported amounts", and the CEO letter of the FY2022
  10-K (the predecessor's) said "we fell short of expectations in 2022" (`0001437749-23-002959`). The present CEO's letter
  (FY2025) is a list of "best-ever" results with no mistake named; the rows were nervous of the taboo on "mistake"
  **[L2024-003]**; one letter is not a taboo, and this is recorded, not weighed as a tell.
- *The habits carried from Q4.* A published three-year earnings-per-share growth target ("high-single to low-double
  digit through 2027") with quarterly progress reports against it, and an adjusted EPS figure printed beside the
  reported one in the release's first line (8-K Exhibit 99.1, `0000100885-26-000249`). Read with the rest of the record:
  the targets are stated as ranges and the adjusted figures move both ways (2025's adjusted EPS was below GAAP); no
  instance found in the documents read of a target met by a reserve release, a change of estimate or a one-off gain
  presented as operating; the 2025 land-sale gain and Kansas tax benefit were disclosed and quantified in the 10-K MD&A,
  not hidden. The habit is the one the rows dislike, "Managers that always promise to "make the numbers" will at some
  point be tempted to make up the numbers" **[L2002-041]**, and it weighs against; it does not, on this record, raise
  a doubt about honesty.
- *The pay design* (DEF 14A): annual bonus 70% on operating income and operating ratio (the ratio adjusted to the
  planned fuel price), 10% safety, 20% a "strategic" scorecard; long-term pay 60% performance units on three-year ROIC
  (two-thirds) and operating-income growth relative to industrial and railroad peers (one-third), 40% stock options.
  ROIC as the filer defines it puts debt in the denominator, so the units cannot be earned by buying back stock with
  borrowed money; that is a point for the design. The options are fixed-price with no step-up for retained earnings
  **[L1994-021]**, and an option holder "benefits not at all from dividends" **[M2003-018]** (Q6 Part B weighs it).
- **VERDICT on integrity: IN.** Doubt was looked for in the proxy, the 10-K's legal and control sections, the earnings
  release and the merger documents; none found that bears on honesty. The rows' test is trust before ability: "we
  wouldn’t hire anybody, no matter how able, if we didn’t trust them" **[M2015-047]**; nothing read gives a reason not
  to.
- **Ability: WEIGHS FOR.** The operating record against the hand and against the rival is the best of the span read
  (operating ratio 59.8% against BNSF's 65.6% in 2025; injury and derailment rates the company's lowest), and it is an
  operator's record, the kind "we still look to the underlying business, though" **[M1996-037]** leaves to the business
  to carry. Against ability, carried to Q6: the same management chose, within two years of arriving, the largest
  acquisition in the industry's history, on synergies stated as EBITDA, and paused the buybacks to pay for it.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **Where the decade's cash went** (10-Ks FY2016 to FY2025; $M): owner cash (OCF less stock pay less capex) summed
  2016 to 2025 about $51,000; dividends paid $26,965; buybacks $43,314; together $70,279, about $19,000 more than the
  owner cash, the gap met by debt that rose from $15,007 to $31,814 (Q4 table). Beyond the capital spending already
  deducted, nothing was retained; more than everything was paid out, on borrowed money.
- **The retention test** **[R1995-009]**. The money that was kept is the capital spending above depreciation, about
  $11.6B over 2016 to 2025 (Q3 table: capex $33,965M against depreciation $22,395M). It went with operating income rising
  from $7,272M (2016) to $9,846M (2025) at historical cost, mostly through price (Q3); judged on that, the dollar kept in
  the network has held its value, which is the most the rows ask of a compulsory reinvestment. Forward: "Can you keep
  using all of the capital you generate, effectively, for a very long time?" **[M2010-097]**: this business cannot; it
  spends about two-fifths of its operating cash on capital (2025: $3,791M of $9,290M) and has paid out more than the rest.
- **Buybacks.** The authorizations are by share count, never by price: "up to 100 million shares of our common stock by
  March 31, 2028" (10-K Note 18), the kind of programme of which the rows say "corporate repurchase announcements almost
  never refer to a price above which repurchases will be eschewed" **[L2016-002]**; much of it was done by accelerated
  repurchase (ASR) contracts with banks, a fixed sum at an average price set later (10-K Note 18). Prices paid, each
  year's 10-K, Item 5: 2018, 57.7M shares at $143.70; 2019, 35.6M at $165.77; 2020, 22.8M at $167.92; 2021, 33.8M at
  $218.36; 2022, 27.4M at $231.51; 2023, 3.7M at $202.67; 2024, 6.5M at $240.51; 2025, 12.0M at $234.15. Funded in large
  part by borrowing, against the rows' first condition, "available funds -- cash plus sensible borrowing capacity --
  beyond the near-term needs of the business" **[L1999-023]**. **Against the bottom of the Q7 range (written back from
  Q7):** the bottom is $120.64 a share on the all-equity basis ($133.15 equity-only); every year's average price,
  $143.70 (2018) to $240.51 (2024), sits above it, and from 2021 on the prices sit above the top ($162.31). The rows read
  such purchases by what they did: "if you buy it for $1.10, you are doing them no favor at all" **[M2014-008]**. (Today's
  range rests on FY2021 to FY2025 cash, at least as high as the earlier years' cash, so the earlier purchases are not
  made to look worse by the comparison.) **Weighs against.**
- **The deal: Norfolk Southern.** Terms (10-K Note 20; 10-Q Note 18; S-4/A `0001193125-25-224307`): one UNP share plus
  $88.82 in cash for each NSC share; about 225 million UNP shares to be issued (38% of the 594 million outstanding) and
  about $20B of cash, "funded through a combination of new debt and cash accumulated through cash provided by operating
  activities"; an implied value of $320.00 per NSC share at signing, "a premium of approximately 25%" to NSC's 30-day
  average (S-4/A); a $2.5B termination fee each way; STB approval pending, the first application rejected as incomplete
  on 2026-01-16, the revised one accepted on 2026-05-28 "while holding the proceedings in abeyance" for supplemental
  information (10-Q Note 18); expected completion 2027. The board's reasons lead with "approximately $2.75 billion of
  annualized synergies (comprising cost savings of $1.0 billion and $1.75 billion in EBITDA growth from market
  opportunities)" (S-4/A, reasons). The banker is paid $52.5M, of which all but $11.5M "is contingent upon the
  completion of the mergers" (S-4/A, opinion of Morgan Stanley).
  - *The one STOP in Part A* **[L2009-019]** does not apply: the deal is not wholly in stock (about $20B is cash), and
    UNP's stock is not below its intrinsic value on this run's range (Q7: price above the top). The rows' defensible case
    for a premium is in fact this one, "its stock is overvalued relative to the acquiree's" **[L1997-031]**; it is the
    cash leg, borrowed, and the price paid for NSC's cash, that the rows test.
  - *Value given against value got* **[M2007-123]**, **[L2014-012]**: on the filed records alone, with no synergy
    counted ("we never count on synergies when we acquire companies" **[L2016-008]**) and the deal valued on an
    all-equity basis **[L2017-004]**, the combined company is worth less per UNP share than UNP alone (Q7, the merger
    valued beside: $80.81 to $115.58 a share combined against $120.64 to $162.31 standalone, all-equity basis). NSC's five
    years of owner cash before interest average $2,468M (its 10-Ks FY2021 to FY2025); UNP pays about $72B of stock and
    cash for the equity at signing ($320.00 a share implied), about $82B at today's UNP price, and takes on $15.5B of NSC's net debt (NSC 10-Q for 2026-06-30, accession
    `0001628280-26-049326`).
  - *The forces toward deals.* The rows describe the setting: "there are all these forces that push toward deals, and
    if you try to push toward deals, you’re going to get a lot of dumb deals" **[M2014-076]**; and of railroad mergers in
    2021, a row that names this company: "people are not going to remember what you paid, but they’re going to remember
    whether you built a larger system. And the investment bankers are cheering you on at every move." **[M2021-038]**
    (weighed under Q2's convention on a row about one company: the speakers' view of rail deal-making at that date, not a
    verdict on this deal).
- **Dividends**: $5.44 a share declared in 2025, raised every year read; the release of 2026-07-23 affirms "Consistent
  annual dividend increases", a payout policy stated in advance of the earnings that must fund it.
- **Part A: WEIGHS AGAINST.** A decade of buybacks at prices with no stated limit, funded partly by debt; and a pending
  acquisition whose price the filed records do not support without the synergies the rows refuse to count
  **[L2016-008]**, financed by about $20B of new borrowing. No STOP **[L2009-019]**.

### Part B: the pay, the board and the owners
- **The proxy** (DEF 14A, `0000100885-26-000098`): CEO total pay $20.3M (2025), $17.6M (2024); salary raised to
  $1.5M and long-term target to about $15M, the committee having "increased Mr. Vena's Total Direct Compensation by 20%
  due to his exceptional performance"; pay set against a peer group with a compensation consultant ("Guidance from
  Compensation Consultant"), the comparative ratchet the rows warn of **[L2005-015]**, **[M2012-095]**. Bonus on operating
  income and operating ratio, measures inside management's control **[M2003-019]**, with the ratio adjusted to the
  planned fuel price (the board removes a cost management does not control; reasonable). Units on three-year ROIC and
  relative operating-income growth (the 2023 to 2025 units vested at 86% of target on a 15.9% average ROIC). Options are
  40% of the long-term award, fixed-price, no step-up **[L1994-021]**.
- **Owners as partners.** Stock ownership guideline seven times salary for the CEO; hedging and pledging barred; no
  employment agreements; an independent chairman separate from the CEO, the arrangement the rows prefer for replacing
  a CEO **[L2014-026]**. Directors: five of the eleven non-management directors hold no shares beneficially, only deferred stock units
  (Edison, Simons, Tien, Will, Williams; DEF 14A, security ownership), so the board as a body has not bought much
  "with their savings" **[L2019-008]**. Say-on-pay 2026: 454.1M for, 24.4M against (8-K of 2026-05-18).
- **Part B: WEIGHS AGAINST, lightly.** For: ROIC in the units (buybacks cannot inflate it), operating measures in the
  bonus, a split chair, a real ownership guideline. Against: a consultant and peer-group process, fixed-price options,
  and a board most of whose members own little stock bought with their own money.

**WEIGHS AGAINST** on both parts; no STOP.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; worked "with a range of possibilities" **[L2000-024]** by Q7's range
convention, at the sovereign of Step 0, 5.60%. Arithmetic in `_research 2026-10-11 UNP/scripts/q7.py`, output in
`q7_output.txt`; every input a filed figure named below.

**The cash input, owner cash after every real cost** **[L2021-003]** (Q4's recast; $M; each year's 10-K; interest after
the company's own effective tax rate, which ran 22.1% to 23.3%):

| FY | OCF | Stock pay | Capex | Finance-lease principal | Owner cash (equity basis) | After-tax interest | Before interest (all-equity basis) | Growth capex (capacity and commercial) | Maintenance-only, before interest |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 9,032 | 88 | 2,936 | 106 | 5,902 | 890 | 6,792 | 527 | 7,319 |
| 2022 | 9,362 | 99 | 3,620 | 91 | 5,552 | 980 | 6,532 | 584 | 7,116 |
| 2023 | 8,379 | 107 | 3,606 | 65 | 4,601 | 1,038 | 5,639 | 664 | 6,303 |
| 2024 | 9,346 | 118 | 3,452 | 47 | 5,729 | 974 | 6,703 | 500 | 7,203 |
| 2025 | 9,290 | 142 | 3,791 | 36 | 5,321 | 1,019 | 6,340 | 617 | 6,957 |
| **Mean** | | | | | **5,421** | | **6,401** | | **6,980** |
| Growth, 2021 to 2025, compound | | | | | **-2.56%** | | **-1.71%** | | -1.26% |

**The window and the specifics.** (a) *Cycles:* the literal five-year window FY2021 to FY2025 is the central figure.
Neither end year is aberrational on the filer's own description: FY2021's capital plan was "approximately $2.9 billion,
essentially flat with 2020" because "Implementation of our new transportation plan has generated capacity" (FY2020 10-K,
`0000100885-21-000068`), a plan, not an event; FY2025 had $0.3B of bonus-depreciation cash (10-K MD&A), kept because it
recurs while the spending does. The year the filer does describe as hit by one-time items is FY2023 ("$454 million of
payments related to the 2022 one-time charge for agreements reached with our labor unions and the ratification charge";
FY2023 10-K, `0001437749-24-003599`), inside the window, so it stays in the average and no cycle base is used. A
sensitivity is shown beside: the five-year averages 2016 to 2020 and 2021 to 2025 (before interest; finance leases not
tagged before 2019 and so left out of both) grew 3.82% a year. (b) *Decline:* the growth shown between the end years is
negative on every series, so it is carried as negative and makes the bottom; the no-growth case is the top. (c)
*Acquisitions:* none inside the window; the Norfolk Southern deal is signed, not closed, and is valued beside the
central figure, not in it. (d) *Working capital:* inside cash from operations; no single-year draw tied to one contract
(FY2023's labour payments are one-time by the filer's description but are cash the owner did not get, and stay). (e)
*Growth spending:* the filing allows the maintenance guess (Q3: "capacity and commercial facilities" is the filer's
growth line). The growth that spending bought, measured on owner cash, is negative, so it was worth less than its cost
and the inversion applies: the top of the range is the maintenance-only case at no growth, the bottom the all-spending
case at the growth shown, since "growth can destroy value" **[L2000-023]**. (f) *The cap:* no positive growth is carried,
so no cap binds; the 3.82% sensitivity, carried ten years, would put owner cash at 28% of sales against a highest share
of 31% in the filings read (FY2021), so it too stands uncut. Zero nominal growth after year ten; nothing above the
discount rate is carried after year ten **[M1997-095]**.

**Whose tax and on what the floor is earned.** Owner cash is after the company's own income tax, no conversion; no
carryforward or credit that runs out inside ten years (purchased tax credits and bonus depreciation are disclosed, not
expiring shelters). Central figure on the **all-equity basis**: owner cash before interest against the market value plus
net debt. Net debt at 2026-06-30 (10-Q): debt due within one year $1,288M plus debt due after one year $29,039M (finance
leases inside these lines) less cash $1,614M and short-term investments $500M = **$28,213M**; operating leases ($609M
non-current) left out, and said so; no subsequent event in the 10-Q changes it. Enterprise value at the price:
$165,355M + $28,213M = **$193,568M**.

**The value range** (all specifics applied; $ a share):

| Case | Base $M | Growth carried | Value at 5.60% $M | Per share, all-equity (less net debt, / 594.075M) | Equity-only per share |
|---|---|---|---|---|---|
| Top: maintenance-only, no growth | 6,980 (equity basis 5,999) | 0% | 124,639 | **$162.31** | $180.33 |
| Middle reference: all spending, no growth | 6,401 (5,421) | 0% | 114,310 | $144.93 | $162.95 |
| Bottom: all spending, growth shown | 6,401 (5,421) | -1.71% (-2.56%) | 99,884 | **$120.64** | $133.15 |
| Sensitivity beside: all spending, cycle-average growth | 6,401 | +3.82% | 154,832 | $213.14 | not computed |

**VALUE RANGE: $120.64 to $162.31 a share (all-equity basis, central); $133.15 to $180.33 equity-only; against $278.34.**
The literal window is the central window here, so it is the figure shown; the cycle-average sensitivity beside it is
$213.14. Width 1.35 to 1.

**The floor, tested first** (CONVENTION, Q7, adopted 2026-10-10): the expected return at $278.34 (the discount rate at
which each case's cash equals the price paid; all-equity against $193,568M, equity-only against $165,355M): top case
3.61% (equity-only 3.63%); no-growth all-spending 3.31% (3.28%); bottom 2.84% (2.61%); the cycle sensitivity 4.53%. **No
case earns the floor of about ten percent, nor half of it**: "we don’t want to buy equities where our real expectancy is
below 10 percent" **[M2003-149]**. Even the most generous case this run could construct, growth of 3.82% a year for ten
years, earns less than the long Treasury's 5.60%.

**The merger, valued beside as if closed** (specific (c), adopted 2026-10-10; the box is decided on the central
figure). NSC's own filed record (10-Ks FY2021 to FY2025, accession `0001628280-26-006268` for FY2025, XBRL with
accessions in `notes_nsc_series.txt`): owner cash before interest 3,232; 2,769; 1,359 (2023, the East Palestine year);
2,267; 2,715; mean **$2,468M**. Combined mean $8,869M; combined growth 2021 to 2025 -2.51%. Net debt as if closed: UNP
$28,213M + NSC $15,547M (NSC 10-Q 2026-06-30: $649M current and $15,967M long-term debt less $1,069M cash) + the $20B
cash consideration = $63,760M; shares 594.075M + 224.6M issued (one for each NSC share outstanding, NSC 10-Q cover) =
818.7M. **As if closed: $80.81 to $115.58 a share (all-equity basis; all-spending cases, since NSC's growth-spending
split was not read), no synergy counted** **[L2016-008]**. Like for like with the standalone all-spending cases ($120.64
at the growth shown, $144.93 at no growth), the value per UNP share falls by a fifth to a third on the deal's filed
terms and the two companies' filed cash; the $2.75B of stated "annualized synergies" would have to be real, and after
tax, to close the gap.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged.
All-equity: top $70.00, bottom $48.59, **fair price $59.30 a share** (central); equity-only: top $100.99, bottom $76.89,
**$88.94 a share** beside it. Tax: the company's own, as above. No cheap price is reported.

- **VERDICT: OUT.** No case in the range earns the floor at the price **[M2003-149]**: the price, $278.34, is 1.7 times the
  top of the range, and the expected return on every case is between 2.6% and 4.5%, below the long government bond.
  Closed OUT by the floor convention, tested before the width; the range itself is narrow (1.35 to 1), so the file is
  not TOO HARD on this question. Q8 to Q10 and Q12 are NOT REACHED.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (closed at Q7). See AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (closed at Q7). See AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (closed at Q7).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed at Q7).

---
## THE BOX
**OUT at Q7, on the floor.** Value range $120.64 to $162.31 a share on the all-equity basis ($133.15 to $180.33
equity-only), literal window FY2021 to FY2025, against $278.34 (close 2026-10-09, aggregator); expected return at the
price 2.6% to 4.5% on every case, below the ten percent floor and below the 5.60% long Treasury. Q1 IN, Q2 IN, Q3 weighs
against, Q4 weighs against (no STOP), Q5 integrity IN and ability weighs for, Q6 weighs against (no STOP). Reporting
figures: fair price $59.30 (all-equity, central), $88.94 (equity-only). The pending Norfolk Southern merger, valued
beside as if closed with no synergy, $80.81 to $115.58 a share. No integrity facts adverse to the people were found.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on the questions the STOP left unasked, each with its source **[M1997-127]**; written
down, not weighed; the box unchanged (operator rule 2).

**Q8 (the alternatives).** The long Treasury yields 5.60% (Step 0); every case of Q7's range earns 2.6% to 4.5% at the
price. The company's own alternative, its stock below value, is not open at this price (Q6: buybacks are paused for the
merger in any case, 10-Q Note 16).

**Q9 (the target's debt and exposures).**
- Debt $30,327M at 2026-06-30, all fixed-rate (10-K Item 7: "we did not have variable-rate debt"); contractual debt
  payments including interest $2,724M in 2026, $2,455M in 2027, $2,402M in 2028, $47,667M after 2030 (10-K, contractual
  obligations table). Fair value $24.7B against $30.3B carried (10-Q).
- Coverage on the speakers' measure, pre-tax earnings over interest **[L2012-002]**: FY2025 ($9,166M + $1,309M) /
  $1,309M = 8.0 times.
- Liquidity at 2026-06-30: $1.6B cash, $0.5B short-term investments, a $2.0B undrawn revolver, $600M undrawn on the
  receivables facility; access to that facility "may be reduced or restricted if our bond ratings fall to certain levels
  below investment grade" (10-K MD&A; 10-Q MD&A).
- The merger would add about $20B of new borrowing and NSC's $15.5B of net debt (combined net debt about $63.8B as if
  closed, Q7); the 10-K's risk factors say "the combined company will likely be required to comply with a leverage
  covenant" and that rating agencies "may take negative actions"; a $2.5B termination fee runs each way.
- Exposures: common-carrier obligation to carry hazardous materials, including toxic-inhalation-hazard chlorine,
  "regardless of risk or potential exposure to loss" (10-K Item 1A); NSC's own record carries the East Palestine
  derailment litigation of 2023 (NSC 10-Q, legal actions note). Personal-injury liability $413M accrued with a
  reasonably possible range to $530M; environmental $259M across 343 sites, 17 on the Superfund list; a putative class
  action under the Illinois Biometric Information Privacy Act, no estimate (10-K Note 17). The fuel-surcharge antitrust
  cases, summary judgment for the railroads 2025-06-24, on appeal (10-K Item 3).
- Pension and retiree plans funded at 2025-12-31 (10-K MD&A).

**Q10, Q12.** Nothing recorded.

**Integrity (Q5) facts.** None adverse found; nothing to flag in the box line.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit eff748e8, before the first EDGAR request); written question by
      question; committed after each question with a pathspec of the run file and the research folder only.
- [x] Dispatched run: the brief allowed per-question commits; the lock is the dispatching session's (not touched here);
      the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` (by name
      pattern for today's date, to check this file's name) showed four other runs' file names; declared under
      contamination, not opened, not used. The session context showed the TXN fold's commit subject; declared, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `_research 2026-10-11 UNP/scripts/check_run.py`, output `check_run_output.txt`); every filing fact carries
      its accession or names its filing; no E-ids.
- [x] The order was kept: Q1 to Q6 answered (no STOP closed among them), Q7 closed OUT, Q8 to Q12 NOT REACHED; nothing
      after Q7 is a clearance.
- [x] Owner cash after every real cost (all capital spending, stock pay, finance-lease principal), never a net-income
      proxy; the sovereign from the US Treasury par curve (issuing authority); the price is an aggregator quote and is
      flagged.
- [x] Contrary evidence written down as found (foundations paragraph, Q2's volume and coal lines, Q3, Q4); facts for
      later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor-date issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 material was ignored.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the research folder,
      `check_framework_output.txt`).

**Honest notes on the work.** (1) The prices paid for buybacks are compared with today's range, not with a range built
at each purchase date; stated in Q6. (2) The maintenance split uses the filer's "capacity and commercial facilities"
line as all of the growth spending and treats locomotives, freight cars and technology as maintenance, which lowers the
top of the range; a different split could raise it, but no split brings the expected return near the floor. (3) BNSF's
operating ratio carries Berkshire's purchase accounting; the comparison flatters UNP by an unstated amount. (4) NSC's
growth-spending split was not read, so the as-if-closed figure uses all-spending cases only. (5) The 2016-2020 to
2021-2025 sensitivity leaves finance-lease principal out of both windows because it is not tagged before 2019.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR

(1) **Q2's "ordinary returns" against replacement cost.** The convention judges the field's returns "from the filer's
and the rivals' own filings" in words, and the castle rows define the return on "the capital actually needed in the
business" **[M2010-090]**; but for a railroad the rows themselves say the return on replacement value is "a pittance"
**[M2024-058]** while the return on historical cost is well above ordinary (UNP 14% to 17% before tax on net property).
The framework does not say which base the "ordinary returns" test reads, and the two bases give opposite answers for
every railroad. This run read the castle test on historical cost and carried replacement cost to Q3 and Q4; a reader who
chose replacement cost would close Q2 OUT. A sentence naming the base is needed. (2) **Specific (e) and negative growth.**
The inversion rule ("the maintenance-only no-growth case is the top of the range and the growth case the bottom") is
written for growth spending that buys too little growth; when owner-cash growth is negative on every series, the rule
still applies, but the text does not say whether the "growth case" at the bottom is the all-spending series at its own
(negative) rate or the maintenance-only series at its rate; this run used the all-spending series, the more conservative,
and says so. (3) **Specific (a), what makes an end year "aberrational on the filer's own description".** FY2021's low
capital plan was described by the filer as a plan made possible by freed capacity, not as an unusual year; the rule
gives no test for a filer's neutral description of an unusual number, and an analyst could have read FY2021 either way.
The box did not turn on it here (the cycle sensitivity is shown beside). (4) **The brief's instruction on competitors**
("the rivals the 10-K itself names, up to three that file with the SEC") gave one railroad, BNSF; the 10-K names trucks,
barges, ships and pipelines only as classes. A one-rival comparison was the honest result; the framework's Q2 asks for
"the competitors" in the plural and does not say what to do when the filer names one.
