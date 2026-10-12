# Company Run: EVI Industries, Inc. (NYSE American: EVI), 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch.

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (overnight cycle of 2026-10-12). Research folder:
`Test Runs/_research 2026-10-12 EVI/` (notes, the tool outputs, `calc.py` and its output, the fetch script; raw filings in
`cache/`, ignored by git).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker, 2026-10-12).

**CONTAMINATION, declared.** (1) To check for a same-day file I listed `Test Runs/` filtered by the string "2026-10-12";
the listing showed nine other runs of today and their research folders (ADRZY, BOOM, BOUYF, CLIR, DPMAY, DSGR, EOSE,
EQPT, SUNB) and no EVI file. None was opened. (2) The session context showed recent commit subjects, including the EQPT
fold of today with its box and figures, and the git status listed untracked files from AYI and ARCB research folders.
(3) The project map and a memory index line say that every name run under v4.1 is being re-run under v5, from which I
infer that EVI may have a v4.1 run; I do not know its box and did not look. (4) DSGR appears in the listing; I avoided
using Distribution Solutions Group as a stand-in competitor for that reason. Nothing of these is used below.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $19.20 (2026-10-12, live quote printed by `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: 12,878,532 common shares, $0.025 par, one class (10-K for the year
  ended 2026-06-30, filed 2026-09-08, cover as of 2026-09-03, accession `0001437749-26-029759`;
  `python Screens/cover_shares.py EVI`). Check against the balance sheet: 13,151,783 issued less 276,087 treasury =
  12,875,696 at 2026-06-30; the difference of 2,836 is employee plan issuance after the year end. Preferred: 200,000
  authorized, none issued. **Sudsies:** the 8-K of 2026-07-23 (`0001437749-26-024286`) provided for $600,000 of common
  stock in Transactions C and D; the 8-K of 2026-09-02 (`0001437749-26-029515`) reports amendments of 2026-08-31 making
  both "paid entirely in cash", and the 10-K states the total of $37.4 million was paid in cash. No shares were issued
  in the Sudsies transactions; no prospectus or later 8-K changes the count.
- **Market cap:** 12.879M x $19.20 = **$247.3M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2026 (filed 2026-09-08, `0001437749-26-029759`): Items 1, 1A, 7, the
  statements and Note 1; 10-Ks FY2019 to FY2025 for the supplier, competition and cash-flow passages and the
  statements (`0001174947-19-001060`, `0001174947-20-000945`, `0001174947-21-000839`, `0001174947-22-001008`,
  `0001174947-23-001191`, `0001174947-24-001056`, `0002077096-25-000107`); proxy DEF 14A filed 2025-11-20
  (`0002077096-25-000183`): the compensation table, the CEO compensation section, the controlled-company section and the
  ownership notes; 8-Ks of 2026-07-23, 2026-09-02 and 2026-09-08 (`0001437749-26-029760`) with their press releases
  (Exhibits 99.1). The 10-Q for the quarter to 2026-03-31 (`0001437749-26-016124`) was fetched; the 10-K supersedes it
  and it was not relied on. **One figure cross-checked against the filed statement:** net cash provided by operating
  activities FY2026 $20,606 thousand on the filed Consolidated Statement of Cash Flows equals the XBRL fact and the
  `tools/run.py` line (20.6); revenue FY2026 $446,570 thousand on the filed Statement of Operations equals the 8-K
  press release of 2026-09-08.
- **`python tools/run.py EVI`, arithmetic lines only** (output in the research folder). Its three-year owner-cash
  table skipped FY2024 because the capital-spending tag changed that year; FY2024 capital expenditures of $4,867 thousand
  were read from the filed cash-flow statement in the FY2025 and FY2024 10-Ks and the series below was rebuilt from the
  filed statements (`calc.py`). The tool's alternates: no securities inside operating cash, no other stock-pay line, no
  intangible, software or other spending beside capital expenditures; checked against the FY2026 statement, correct.
  Owner cash (USD thousands; operating cash less stock pay less capital expenditures; then less cash paid for acquisitions):

  | FY (June) | OCF | stock pay | capex | before acquisitions | cash acquisitions | after acquisitions | stock paid for acquisitions |
  |---|---|---|---|---|---|---|---|
  | 2017 | 2,590 | 421 | 237 | 1,932 | 14,708 | -12,776 | 16,053 |
  | 2018 | 11,345 | 1,575 | 829 | 8,941 | 13,352 | -4,411 | 21,376 |
  | 2019 | -8,725 | 1,740 | 2,979 | -13,444 | 12,542 | -25,986 | 17,050 |
  | 2020 | 23,066 | 2,302 | 3,375 | 17,389 | 1,379 | 16,010 | 8,010 |
  | 2021 | 13,694 | 2,437 | 2,824 | 8,433 | 4,818 | 3,615 | 8,877 |
  | 2022 | -1,898 | 2,598 | 3,981 | -8,477 | 11,953 | -20,430 | 4,331 |
  | 2023 | 940 | 3,062 | 3,708 | -5,830 | 2,278 | -8,108 | 503 |
  | 2024 | 32,652 | 4,974 | 4,867 | 22,811 | 1,949 | 20,862 | 229 |
  | 2025 | 21,265 | 4,558 | 4,861 | 11,846 | 46,925 | -35,079 | 0 |
  | 2026 | 20,606 | 5,298 | 7,152 | 8,156 | 7,182 | 974 | 0 |

  Five-year average FY2022 to FY2026: **$5.70M before acquisitions, -$8.36M after cash acquisitions.** Depreciation and
  amortization FY2026 $8,109 thousand (of which intangible amortization about $3.1M); capital expenditures $7,152 thousand.
  Stock pay is resolved and complete (one line, restricted stock; the employee purchase plan is immaterial).

**The balance sheets, FY2016 to FY2026, read here because the file closes before Q4** **[M2025-032]** (USD millions,
filed statements and first-filed XBRL; accessions as above):

| June 30 | assets | equity | goodwill | intangibles | cash | receivables | inventory | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 10.2 | 5.1 | 0 | 0.0 | 3.9 | 1.8 | 2.6 | 0 | 2.8 |
| 2017 | 57.1 | 32.2 | 24.8 | 7.2 | 0.7 | 13.6 | 7.7 | 3.7 | 4.9 |
| 2018 | 95.5 | 57.0 | 37.1 | 15.8 | 1.3 | 16.0 | 15.4 | 8.8 | 7.5 |
| 2019 | 154.5 | 77.3 | 54.5 | 22.4 | 5.0 | 30.6 | 26.4 | 40.6 | 9.6 |
| 2020 | 160.7 | 87.8 | 56.7 | 21.8 | 9.8 | 23.0 | 24.1 | 25.0 | 10.4 |
| 2021 | 177.9 | 106.7 | 63.9 | 23.7 | 6.1 | 28.9 | 25.1 | 11.9 | 18.8 |
| 2022 | 230.8 | 117.7 | 71.0 | 26.2 | 4.0 | 43.0 | 49.4 | 27.8 | 22.9 |
| 2023 | 253.8 | 131.0 | 73.4 | 24.1 | 5.9 | 50.5 | 59.2 | 34.9 | 32.6 |
| 2024 | 230.7 | 136.6 | 75.1 | 22.0 | 4.6 | 43.0 | 47.9 | 12.9 | 34.2 |
| 2025 | 307.0 | 143.5 | 91.7 | 30.9 | 8.9 | 60.5 | 66.1 | 53.0 | 37.1 |
| 2026 | 304.5 | 150.1 | 93.9 | 28.9 | 6.8 | 56.8 | 66.3 | 51.0 | 39.8 |

What the figures say. The company was a $10M distributor in 2016 and is a $304M collection of acquired distributors in
2026. Equity grew $145M, of which retained earnings supplied $37M; the rest is paid-in capital, mostly shares issued to
sellers ($76.4M of stock paid for acquisitions FY2017 to FY2024 by the table above). Goodwill and intangibles ($122.8M)
are 82% of equity, so tangible equity is about $27M. Receivables have stayed near 11% to 16% of sales and inventory
rose from 10% of sales (2018) to 18% (2022) and back to 15% (2026): the filer ties the 2022 build partly to supply-chain
purchases in advance (10-K FY2022, `0001174947-22-001008`), and it was released in FY2024, when operating cash was
$32.7M. Customer deposits ($20.1M) and payables ($47.6M) fund much of the inventory, which is why the tangible capital
is small. Debt has swung with acquisitions: $8.8M, $40.6M, $11.9M, $34.9M, $12.9M, $53.0M, $51.0M; at 2026-06-30 net
debt was $44.2M, and the Sudsies purchase of 2026-09-01 ($37.4M cash) came after it. What they do not say: whether the
acquired goodwill earns its cost, which only the earnings can show; and what they cannot say: whether the supplier
franchises behind the inventory will be renewed.

**Lines of evidence, derived from the FY2026 10-K (the brief's departure on evidence).** Chosen from Item 1, Item 1A
and Item 7 because each bears on whether the castle stands: (1) supplier dependence, four manufacturers 71% of product
purchases, contracts short-term and terminable on short notice, and supplier relationships that "ceased" on certain
acquisitions (Item 1 Sources of Supply; Item 1A); (2) the basis of competition, over 500 distributors, competition on
design, "competitive pricing", product representation and service, and manufacturers that own distribution (Item 1
Competition; Item 1A); (3) growth by acquisition: FY2026 revenue growth "attributable to revenues generated by
businesses acquired" (Item 7); (4) margins and costs: gross margin 31.5%, SG&A 28.0% of revenue (Item 7); (5) the new
consumer garment care division (Sudsies) and its environmental exposure to perchloroethylene (Items 1 and 1A);
(6) the credit facility and its covenants (Item 7); (7) control by management, 52.3% of the vote (Item 1A).

**Competitors.** The 10-K names no rival: it describes "over 500 full-line or partial-line equipment distributors",
"independently owned distributors and certain manufacturers which own distribution businesses". No named rival
therefore exists to be flagged as non-filing. Used instead: **Alliance Laundry Holdings Inc.** (ALH, CIK 1317685, 10-K
FY2025 filed 2026-03-13, `0001317685-26-000011`), the manufacturer that states it is "the number one supplier of
commercial laundry equipment in terms of market share in North America", sells through "company-owned distribution
offices" as well as independent distributors, and bought four distributors in 2024 and 2025 (its Note 4); it was listed
among EVI's major manufacturers in the FY2020 10-K and is absent from the list from the FY2021 10-K onward. It is the
one filing example of the "manufacturers which own distribution businesses" that the 10-K names as competition. And,
as a **stand-in only, not a rival**, **Alta Equipment Group** (ALTG, CIK 1759824; XBRL facts from its 10-Ks, latest
`0001193125-26-076932`, transcription, flagged), a roll-up of franchised equipment dealers in another field, used only
to show what the franchised-dealer model earns.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the share as a business **[M1997-109]**: EVI is bought for what the
distribution business will send out in cash, and the record of that cash (the table above) is weak beside the
company's own featured figures. The analyst's habits apply: look for "what’s wrong in things" **[M2025-013]**, since a
decade of revenue growth and a press release that calls the business durable and predictable invite the opposite habit. **Contrary
evidence, written down as found** **[M1997-127]**: (a) gross margin rose every year from 23.1% (FY2019) to 31.5% (FY2026),
which the filer attributes to mix toward service and parts and to "favorable changes in product and customer mix";
(b) on tangible capital the business earns 14% to 27% pretax on operating income in FY2019 to FY2026, because customer
deposits and payables fund the inventory; (c) the proxy (`0002077096-25-000183`) records "the execution of long-term
distribution agreements with certain of the Company’s key suppliers" in the fiscal 2024 bonus rationale, which cuts
against the supplier-termination risk; (d) 55,000 customers, none above 10%, and about 30,300 service visits in the
fourth quarter of FY2026 (press release, `0001437749-26-029760`).

## THE STANDING RULE
A part-interest bought with the buyer's own money, unlevered, puts the buyer at no risk of ruin; the rule binds the
buyer's conduct, not the target's **[M2012-081]**, and no borrowing is contemplated **[L2014-005]**. The target's own debt
(net debt $44.2M at 2026-06-30, plus the $37.4M Sudsies payment) belongs to Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years", with "some notion of how the industry will develop and
  where the company will stand within the industry" **[M2012-065]**. The product is plain: washers, dryers, ironers,
  boilers and the parts and service for them, sold to laundromats, hotels, hospitals, prisons and industrial
  laundries (10-K FY2026, Item 1). What matters, as the row on a business whose chemistry was never understood puts it, is
  "the economic dynamics of the industry" and "Is there ease of entry?" **[M2011-014]**, and those can be read from the
  filings.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) replacement demand for commercial laundry
  equipment, which the filer describes as recurring and which does not depend on fast technology (research and
  development is "generally immaterial" because the manufacturers do it, Item 1); (2) the terms on which manufacturers
  grant distribution, which the filer says can be "terminated on short notice" (Item 1A); (3) the price of distributors
  bought; (4) local price competition among 500 distributors. Variable (1) is foreseeable in a general way over ten
  years; variables (2) and (4) are the castle question and are sent to Q2; (3) goes to Q6.
- **Routing.** This is not a business whose economics are out of reach because its industry changes fast; laundry
  equipment changes slowly and the manufacturers carry the technology. Nor is it a financial institution or a holding
  company of unrelated parts. The new consumer garment care division (Sudsies, bought 2026-09-01 for $37.4M; trailing
  revenue about $21.7M and operating income about $4.7M by the furnished press release of 2026-07-20) is a separate
  segment from FY2027; it is not in the five-year record and it does not decide (Q2, the parts table). The warning row
  is retail, where "it’s easy to sort of think you understand retail, and then subsequently find out you don’t"
  **[M2014-052]**; a distributor of other makers' machines is near that edge, and the doubt about the position, not about
  the economics, is carried to Q2. Doubt about being inside the circle would put it outside **[M2002-092]**; the doubt
  here is about the castle, which is the next question's business **[M1997-148]**.
- **VERDICT: IN.** The ten-year economics of commercial laundry distribution and service can be pictured from the
  filings (10-K FY2026, `0001437749-26-029759`, Items 1 and 7) **[M2012-065]**, **[M2011-014]**; whether EVI holds a
  protected place in them is Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is the 1995 one: "why is that castle still standing?", "What are the key factors? And how permanent are
they?" **[M1995-038]**. A moat is what "protects excellent returns on invested capital" against competitors who "will
repeatedly assault" it **[L2007-004]**.

**The castle tests, each with its filing fact.**
1. **The key factors and their permanence** **[M1995-038]**. The filer names its strengths as an experienced sales and
   service organization, a comprehensive product line, well-stocked inventories, design and installation, and its
   supplier relationships, which it says provide "exclusivity for certain products in certain areas and, in certain
   cases, favorable pricing" (10-K FY2026, Item 1, Sources of Supply). The permanence of the last is stated by the
   filer itself: "the Company does not have contracts with all of its manufacturers, and certain contracts the Company
   does have are short term agreements and can be terminated on short notice"; four manufacturers supplied 71% of
   product purchases in FY2026 and 72% in FY2025 (Item 1A). Every 10-K from FY2019 to FY2026 carries the sentence that
   "In connection with certain business acquisitions, the business relationship between the acquired business and its
   principal supplier ceased", after which those businesses carried other brands (Item 1). The key factor that
   gives local exclusivity is owned by the manufacturer and is revocable.
2. **The money test** **[M2011-015]**. Could a well-funded attacker take this position? The company's own history
   answers it. In 2015 it was "a single Miami, Florida-based distributor with 31 employees" (press release of
   2026-07-20, Exhibit 99.1 to `0001437749-26-024286`); by spending $117M in cash on acquisitions in FY2017 to FY2026 and
   issuing about $76.4M of stock to sellers (the Step 0 table), it became what it calls "North America's leading commercial
   laundry distribution and service enterprise" in a field where "no single competitor of the Company has a major share
   of the market" (10-K FY2026, Item 1A). About $190M bought the leading position; the same can be done by another buyer.
   And another buyer is doing it: Alliance Laundry, the largest North American manufacturer, acquired four distributors
   in 2024 and 2025, among them Metropolitan Laundry Machinery Sales of the New York area on 2025-08-01 (ALH 10-K FY2025,
   Note 4, `0001317685-26-000011`), the same month EVI bought New York-based ASN Laundry Group (EVI 10-K FY2026, Item 7).
   The test's own words for that answer: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The
   field is one of those "that are just never going to have barriers to entry" in the sense of **[M2012-106]**: a
   distributor is bought or built with money, and "one competitor is frequently enough to ruin a business"
   **[M2012-108]** when that competitor also makes the machines.
3. **Pricing power and the agony before a rise** **[M2005-020]**. The filer lists "competitive pricing" among the bases
   of competition and says "The Company believes its services are competitively priced" (Item 1); on inflation and
   tariffs, "there is no assurance that the Company will be able to effectively increase the price of its products and
   services to offset increased costs" (Item 7). The gross margin rose from 23.1% (FY2019) to 31.5% (FY2026), and the
   filer attributes the FY2026 rise to "favorable changes in product and customer mix" and to solution selling (Item 7),
   not to price; written down as contrary evidence above. No filing fact shows prices raised without agony.
4. **The brand in the customer's mind.** The brands sold are the manufacturers' (Item 1 lists American Dryer, Chicago
   Dryer, Cleaver Brooks, Girbau, Dexter, Milnor, Whirlpool and others); EVI's units trade under their own local names.
   The brand owner in this field states that its machines sell "at a price premium versus competitor offerings while
   securing a high degree of loyalty" (ALH 10-K FY2025, Business). In the speakers' terms the distributor is the
   intermediary, and "the brand is our protection against the intermediaries making all the money" **[M2019-041]**; the
   margins in the competitor row below show where the money is made.
5. **The low-cost position.** No filing fact shows EVI as the low-cost distributor. Its SG&A was 28.0% of revenue in
   FY2026 (26.8% in FY2025), corporate expenses were $13.8M (press release of 2026-09-08), and the filer warns that
   competitors "may have greater financial and other resources" and "less indebtedness" (Item 1A). In a field where
   price is a basis of competition, "the guy with the lower cost comes in and kills you" **[M2001-013]**.
6. **Would the customer still choose it over the low bid?** **[M2017-009]**. The filer's own list of how distributors
   compete puts "competitive pricing" beside facility design, product representation, installation and service (Item 1,
   Competition). Service is the one route the rows name out of the commodity class, where "the people care enormously
   about service" **[M2001-014]**; EVI's 425 service personnel and 30,300 quarterly service visits are that route, and
   they are recorded as contrary evidence. But the service network is the thing EVI bought for about $190M, so it is
   also the thing the next buyer can buy.
7. **Ask the competitors** **[M1999-130]**. The manufacturer's own filing says distributors are "a critical part of the
   commercial laundry market" and that its relationships with them are "difficult-to-replicate", and then that "Our
   direct sales channel complements our distribution network by bringing us closer to end-customers and enhancing
   strategic flexibility" (ALH 10-K FY2025). Alliance appears among EVI's "major manufacturers" in the FY2020 10-K
   (`0001174947-20-000945`) and not in the list from FY2021 (`0001174947-21-000839`) to FY2026. The supplier that owns the
   leading brand chose its own offices and other distributors over EVI.
8. **Widening or narrowing** **[M1999-108]**. After a decade of building, the operating margin is 3.5% (FY2026) against
   5.7% (FY2017) and 4.6% (FY2018); management states "EVI's objective is to achieve double-digit consolidated operating
   margins" (press release of 2026-09-08), a level not reached in any year of the record. The gross-margin gain has been
   spent in SG&A. No filing fact shows the position strengthening at the operating line.
9. **What could destroy or reduce it, five to fifteen years out** **[M2000-014]**. The loss of a principal supplier (which
   the filer has already met on acquisitions), forward integration by the manufacturers that own the brands, and the
   bidding of other roll-up buyers for the same distributors.

**The competitor row** (same metrics from each company's own filings):

| company | role | gross margin | operating margin | span | source |
|---|---|---|---|---|---|
| EVI Industries | the filer, distributor | 29.8%, 30.4%, 31.5% (FY2024 to FY2026); 21.6% to 31.5% over FY2017 to FY2026 | 3.3%, 3.5%, 3.5% (FY2024 to FY2026); 1.2% to 5.7% over FY2017 to FY2026 | FY2017 to FY2026 | 10-Ks listed in Step 0 |
| Alliance Laundry Holdings | largest NA manufacturer; owns distribution offices; buys distributors | 34.7%, 36.5%, 37.6% | 17.3%, 18.8%, 18.6% | CY2023 to CY2025 (three years filed) | 10-K FY2025, `0001317685-26-000011` |
| Alta Equipment Group (stand-in, not a rival) | franchised equipment-dealer roll-up, another field | not used | 2.1%, -0.9%, 1.5%, 2.6%, 2.9%, 1.0%, 1.3% | CY2019 to CY2025 | XBRL facts from its 10-Ks, flagged |

**The parts table.** EVI reported one operating and reportable segment through FY2026 (10-K FY2026, Item 1).

| part | share of five-year operating profit | castle | decides |
|---|---|---|---|
| Commercial laundry distribution and service | 100% (FY2022 to FY2026) | open, by the tests above | yes |
| Consumer garment care (Sudsies, from 2026-09-01) | 0% of the window; about 23% of FY2026 combined operating income if the furnished press-release figure of $4.7M is taken | not judged | no |

The file closes on the deciding part **[L2008-005]**.

**The field's returns over the last full cycle.** The span FY2017 to FY2026 contains the pandemic trough (operating
margin 1.2% in FY2020 and 1.3% in FY2021) and the supply-chain inventory build and release of FY2022 to FY2024. Over it
EVI's operating margin ran 1.2% to 5.7%; its pretax operating income on total capital employed, purchased goodwill
included, ran 2.7% to 10.7%; on tangible capital (goodwill and intangibles excluded) it ran about 11% to 27% in FY2019
to FY2026 (`calc.py`). The stand-in dealer roll-up ran -0.9% to 2.9% operating margin. The brand-owning manufacturer ran
17% to 19%. Judged in words **[M1999-108]**: the tangible-capital returns are not poor, and that is written down
against the verdict; they come from turning a thin margin fast, which "only works in terms of return on capital if you
turn your equity extraordinarily fast" **[M2017-096]**, and they are the returns of the local businesses EVI buys, which
the owner pays for in goodwill. The row on dealerships says it plainly in both directions: "There are not any huge
advantages of scale, at least that I’m aware of, in owning lots of dealerships. But running dealerships well is a very
good business. It’s a local business." **[M2015-011]** (weighed, not a verdict on the industry, by the convention on
rows about one business). The owner of EVI pays for the local businesses at prices that leave 2.7% to 10.7% pretax on
the whole capital, with no scale advantage shown in the margin.

**Why OUT and not TOO HARD.** A castle whose future cannot be judged goes to TOO HARD **[M2000-019]**. This one can be
judged on facts already filed: the attacker test is answered yes by the company's own decade of purchases and by the
leading manufacturer's purchases of distributors in the same markets; the local exclusivity is the supplier's to grant
and has been withdrawn on acquisitions; price is a stated basis of competition among 500 distributors; and the margin
has not widened with scale. The 1995 row gives the base rate, "most moats aren’t worth a damn" **[M1995-038]**, and
the evidence here does not lift EVI out of it. A cheap price does not reopen the question: "What you can’t do is turn
any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The castle is shown open: the money test fails on the company's own record and the brand owner's
  forward integration (10-K FY2026 `0001437749-26-029759`, Items 1, 1A and 7; ALH 10-K FY2025 `0001317685-26-000011`,
  Note 4) **[M2011-015]**, **[M2012-106]**; the protective franchise belongs to the manufacturers and is terminable on short
  notice; price is set in competition **[M2017-009]**; and the profit in the chain sits with the brand **[M2019-041]**.
  Q3 onward are NOT REACHED.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (closed at Q2). The balance sheets were read in Step 0.
## Q5: WHO RUNS IT. NOT REACHED (closed at Q2); integrity facts recorded below, not judged.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (closed at Q2).
## Q7: WHAT IS IT WORTH. NOT REACHED as a question; computed below under COMPUTATION, NOT A CLEARANCE at the owner's request.
## Q8, Q9, Q10, Q12: NOT REACHED (closed at Q2).

---
## THE BOX
**OUT at Q2**: the castle is shown open (the money test answered yes by the company's own decade of purchases and by
the leading manufacturer's purchases of distributors; the local exclusivity is the suppliers' to grant and terminable
on short notice; price a stated basis of competition; margin not widened with scale) **[M2011-015]**. **Integrity facts
recorded, not judged.** COMPUTATION, NOT A CLEARANCE: value range -$4.35 a share (one no-growth case, all-equity; the
organic pair $3.83 beside) against $19.20; fair price -$7.35 (equity-only -$3.31).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Bearing on Q3 (capital).** Pretax operating income on total capital employed, goodwill included: 10.7%, 6.2%, 2.7%,
2.9%, 4.5%, 10.3%, 8.0%, 7.3%, 8.1% (FY2018 to FY2026); on tangible capital about 11% to 27% (FY2019 to FY2026)
(`calc.py`, from the statements in Step 0). Revenue grew from $36.0M (FY2016) to $446.6M (FY2026), the FY2026 increase
"attributable to revenues generated by businesses acquired" (10-K FY2026, Item 7); the filer reports no organic growth
figure. Capital expenditures $7.15M in FY2026 against depreciation of about $5.0M (D&A $8.1M less intangible
amortization of about $3.1M); the filing does not separate maintenance from growth spending.

**Bearing on Q4 (the accounts).** (1) The headline results feature "Adjusted EBITDA" ($29.1M, "a record"), defined as
EBITDA with one further adjustment, stock compensation, excluded because "management believes the exclusion allows
investors to better assess the full earnings potential of the business"; a further figure excludes corporate expenses
($13.8M) to show "adjusted EBITDA was $42.9 million, or 9.6% of revenues" (press release of 2026-09-08, Exhibit 99.1 to
`0001437749-26-029760`). Net income was $7.7M and owner cash after acquisitions was $1.0M in the same year. Stock pay was
$5.3M in FY2026, $4.6M in FY2025, $5.0M in FY2024. (2) FY2021 net income of $8.4M includes $6.96M of loan forgiveness
(XBRL fact from 10-K FY2021, `0001174947-21-000839`); operating income that year was $3.2M. (3) Effective tax rate 34.5% in
FY2026, raised by "nondeductible compensation" (Item 7). (4) Goodwill $93.9M and intangibles $28.9M against equity
$150.1M; the annual impairment test found no impairment (Item 7). (5) The credit agreement measures leverage on EBITDA
(Item 7), a lender's term.

**Bearing on Q5 (the people).** (1) The press release of 2026-07-20 stated Sudsies' five-year EBITDA compound growth as
62%; the 8-K that furnished it says the release "inadvertently overstated" the figure and "The corrected percentage is
31%" (`0001437749-26-024286`, Item 8.01); the exhibit as furnished carries the 62%. (2) The featured adjusted figure in
the Q4 facts above. (3) Control: management and the board, through stockholders agreements over shares issued to
sellers in acquisitions, "may be deemed to control the Company as a result of their collective voting power over shares
representing approximately 52.3%" (10-K FY2026, Item 1A); as a "controlled company" EVI is exempt from the NYSE American
rules requiring a majority of independent directors and an independent compensation committee (Item 1A; proxy
`0002077096-25-000183`, which gives 56.2% including 431,466 shares the board directs). (4) Related-party leases from
current or former principals of subsidiaries, about $0.9M a year in total (10-K FY2026, Item 7). (5) Chief executive
pay: total $5,350,835 in FY2025 and $5,914,510 in FY2024 (salary $650,000, discretionary cash bonus $650,000 and
$750,000, restricted stock $3,999,997 and $4,500,009), against net income of $7.5M and $5.6M in those years (proxy,
Summary Compensation Table); a further $850,000 cash bonus and 173,635 restricted shares were granted in September 2025
(proxy). Half of each recent award cliff-vests on the tenth anniversary, and earlier awards vest when the chief
executive reaches 62, in 2040 (proxy). Bonuses are discretionary, "based upon a subjective evaluation" (proxy).
(6) The FY2024 bonus rationale credits "the execution of long-term distribution agreements with certain of the
Company’s key suppliers" (proxy).

**Bearing on Q6 (the money and the owners).** (1) Buyback authorized 2026-07-28, up to $10.0M, with no price stated:
timing, price and amount "at management’s discretion based on market conditions, the trading price" and other factors
(10-K FY2026, Item 7); repurchases to date are shares withheld for employee taxes ($1.5M in FY2026). (2) Dividends of
$0.33 a share in FY2026 ($4.98M) and $0.31 in FY2025 ($4.59M), paid while owner cash after acquisitions was $1.0M and
-$35.1M. (3) Stock issued to sellers of acquired businesses, $76.4M in FY2017 to FY2024 (the Step 0 table), none in
FY2025 or FY2026; the 10-K states the company "believes the issuance of stock consideration in transactions aligns the
interests of the sellers" (Item 1). (4) Sudsies: $37.4M, all cash after the amendments of 2026-08-31, for a business with
furnished trailing operating income of about $4.7M; it is "the Company’s first dedicated expansion beyond the commercial
laundry distribution and service industry" (Item 1). No all-stock deal is in the record read.

**Bearing on Q9 (debt).** Long-term debt $51.0M at 2026-06-30 under a $150M facility maturing 2030-03-26, "collateralized
by substantially all of the assets", with maximum-leverage and minimum-coverage covenants, in compliance; $52.2M
available; weighted rate 5.24% (Item 7). The $37.4M Sudsies payment followed on 2026-09-01. Operating lease liabilities
$12.1M. Environmental exposure to perchloroethylene in the garment care business, described in Items 1 and 1A.

**Bearing on Q12.** Nothing found.

---
## COMPUTATION, NOT A CLEARANCE
*At the owner's request (the brief's reporting convention, a reporting convention and not a rule). The file closed at
Q2; nothing here is a verdict, a clearance or entry language (operator rule 3).*

**Construction, by Q7's range convention in full.**
- **Cash input:** owner cash after every real cost (operating cash, which counts working capital and the company's own
  cash taxes, less stock pay, less all capital expenditures), averaged over the five-year window FY2022 to FY2026
  **[L2005-003]**; acquisitions: cash paid for businesses deducted and total growth credited (the default pair), the
  organic pair beside **[M1998-080]**, **[M2014-068]**. Stock paid to sellers in the window ($5.1M, FY2022 to FY2024) is
  not deducted; its cost sits in today's share count.
- **Cycle base:** the first window year, FY2022, carries the inventory build the filer ties partly to supply-chain
  purchases in advance, released in FY2024; the window contains both the build and the release. The ten-year average
  FY2017 to FY2026, which also contains the pandemic trough, is shown beside as the full-cycle base; the literal window
  is the central figure. The two agree.
- **Growth:** owner cash after acquisitions averaged -$14.27M in FY2022 and FY2023 and -$17.05M in FY2025 and FY2026; the
  series changes sign year to year and a compound rate between end years is meaningless; between the halves it is
  negative to more negative, which carries no meaningful rate either. By specific (b) the range is **the no-growth case
  alone, said so**. The organic series (before acquisitions) changes sign between the halves (-$7.15M to $10.00M): no
  growth carried there either. Growth on aggregate, not per-share, figures (the PG re-test's first specific).
- **Term:** ten years at the window's level, then from year eleven no nominal growth on owner cash before purchases
  (the acquisition spending stops when growth stops, specific (c)); discounted at the 5.60% Treasury rate
  **[L2000-021]**.
- **Maintenance-only case (specific (e)):** not available; the filing does not separate maintenance from growth spending.
  All spending is deducted.
- **Tax:** the company's own (operating cash is after cash taxes; window effective rate 32.5%); no carryforward found.
- **Basis:** all-equity central **[L2017-004]**: owner cash plus after-tax cash interest (window average $2.42M x
  (1 - 0.325) = $1.63M), against net debt of $81.6M = borrowings $51.0M less cash $6.774M at 2026-06-30 ($44.2M), plus the
  Sudsies payment of $37.4M in cash on 2026-09-01, a subsequent event the 10-K states. Operating leases left out.
  Equity-only beside: owner cash after interest, less the after-tax interest on the Sudsies borrowing at 5.24%.
- **The Sudsies deal (closed after the window, before the price date):** its financing is added to net debt and it is
  credited at nothing, because no earnings of it are filed (the 8-Ks furnish press-release figures and no financial
  statements). Beside: credited at the press release's $4.7M operating income after a 25% tax, at no growth
  (CONVENTION of this run: 21% federal plus the 5.5% Florida rate, rounded down; rationale: the release gives no tax
  figure), it would add $4.89 a share at 5.60% and $2.74 at ten percent.
- **Shares:** 12,878,532 (cover, 2026-09-03).

**Results** (USD a share; `calc.py`, output in `calc_output.txt`):

| case | at 5.60% (value) | at 10% (for the fair price) | equity-only at 5.60% | equity-only at 10% |
|---|---|---|---|---|
| **Central: window FY2022 to FY2026, acquisitions deducted, no growth** | **-4.35** | **-7.35** | -2.12 | -3.31 |
| Beside: ten-year base FY2017 to FY2026, same pair | -4.49 | -7.07 | -1.48 | -2.59 |
| Beside: organic pair (no purchases, no growth), window | 3.83 | -0.64 | 6.07 | 3.40 |
| Beside: organic pair plus Sudsies at its press-release figure | 8.72 | 2.10 | not computed | not computed |

**(a) VALUE RANGE: -$4.35 a share, all-equity, central** (a single no-growth case by specific (b); equity-only -$2.12),
against **$19.20**. The literal window is the central figure; the ten-year base gives -$4.49. The organic pair beside
gives $3.83 (equity-only $6.07). At $19.20 the market value plus net debt is $328.9M, against unlevered owner cash
before purchases of $7.34M a year (2.2%). No case in the table earns the floor of about ten percent at the price
**[M2003-149]**; had the file reached Q7, the price above the top of every case would close it OUT through the floor
convention, before any width test.

**(b) FAIR PRICE: -$7.35 a share, all-equity, central** (the single end case valued at ten percent, so the average of the
ends is that case; equity-only -$3.31). Not positive. The organic pair at ten percent is -$0.64 all-equity and $3.40
equity-only. Tax treatment: owner cash after the company's own tax, no conversion. No other price figure is reported.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      `2a41bc4c` (Step 0 to Q1), `53ce0bcc` (Q2), and the close.
- [x] Dispatched to an analyst: the brief allowed the per-question pathspec commits and states that the dispatching
      session holds the lock; the fold is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` filtered by
      today's date was made, and what it showed is declared under CONTAMINATION; nothing of it is used.
- [x] Every v5 id resolves (check script in the research folder: every M, L or R id in the CSV, every quoted fragment
      beside an id in that row, no E-ids); every filing fact carries its accession; numbers come from filings or
      `calc.py`, and the one invented number (the 25% tax on the Sudsies side figure) is labelled CONVENTION.
- [x] The order was kept; Q2's STOP closed the run; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operating cash less stock pay less all capital spending,
      then acquisitions); the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (the foundations paragraph and Q2's tests 3, 6 and the field's returns);
      the facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No point-in-time anchor applies (a live run); no row is cited for a later date than the run.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its three-year table was rebuilt from the filed
      statements where it had skipped FY2024.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The no-growth case with acquisitions deducted.** Specific (b) sends a sign-changing series to the no-growth case
alone, and specific (c)'s default pair deducts acquisitions and credits total growth, with the purchases stopping when
growth stops after year ten. When the growth credited is zero from year one, the text does not say whether the
purchases are still deducted for ten years (charging spending for growth that is not credited, which specific (e)
forbids in its own case) or stop at once (which makes the central case the organic pair). I deducted them for ten
years, as the words of (c) read, and showed the organic pair beside; both lie far below the price, so the box does not
turn on it, but a run near the price would. (2) **Competitors when the 10-K names none.** The brief allows a substitute
and the framework does not say what kind; I used the brand-owning manufacturer that owns distribution (one of the
competitor classes the 10-K describes) and a dealer roll-up in another field as a stand-in. A manufacturer is not a
like-for-like distributor, and the margin gap partly reflects manufacturing, not only position. (3) **"Ordinary
returns" for a roll-up.** Q2's convention on a castle that protects only ordinary returns does not say whether the
return is measured on tangible capital (the local businesses' own) or on total capital including purchased goodwill
(the buyer's); here the first gives 11% to 27% pretax and the second 2.7% to 10.7%, opposite readings. I did not decide
the box on that convention; the money test decided it. (4) **"Its own filed record" for a deal closed after the
window.** The target's only figures are in a furnished press release, not in filed financial statements; I credited
nothing and showed the press-release figure beside. (5) **Tool.** `tools/run.py` builds its three-year owner-cash
mean from 2023, 2025 and 2026 because the capital-spending tag changed in FY2024; its mean silently skips a year.
