# Company Run — General Dynamics Corporation (NYSE: GD) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, holding
reviews, the session-state files, the register, the prepped reading list and `tools/alerts.json` were not opened, and
no earlier run file or research folder for GD was opened.

**CONTAMINATION, declared.** (1) A directory listing of `Test Runs/` showed the names of the 2026-10-05 run files (names
only); one industrial run of that date (HUBB) was opened for FORM only, and it says nothing about GD. (2) `tools/run.py`
prints a v4 owner-earnings line and a "growth the price assumes" line; only its arithmetic is used (Part VII). (3) The
v5 ledger holds one row about this very company, **[M1994-063]**, found by a text search for "defense" while checking
ids; it is evidence on the shelf, not a prior run, and it is used below and declared here. (4) The analyst knows General
Dynamics in general terms from training (Gulfstream, Electric Boat, the Abrams tank, the 2018 CSRA purchase); that is a
prior to be replaced by the filings, and every fact below is from the documents cited.

Working folder: `Test Runs/_research 2026-10-06 GD/` (`fetch.py`, `h2t.py`, `list_filings.py`, `series.py`, `peers.py`,
`value.py` and their saved outputs; raw filings and company facts under `cache/`, gitignored).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $331.72 (close 2026-10-05; Yahoo chart via `tools/run.py`, an aggregator, live quote only, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $1 par, **270,557,195** outstanding on
  July 5, 2026 (Form 10-Q for the quarter to 2026-07-05, filed 2026-07-29, accession `0000040533-26-000032`;
  `python Screens/cover_shares.py GD` agrees). No second class: 481,880,634 issued, the rest held in treasury (10-K
  FY2025, Note N).
- **Market cap:** 270.557M x $331.72 = **$89,749M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, dated
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-01-30, `0000040533-26-000006`): Item 1, Item 1A, Item 5,
  Item 7 in full, the statements, Notes on leases, shares and segments; 10-Q Q2 2026 (filed 2026-07-29,
  `0000040533-26-000032`): cover, balance sheet, cash flow, share repurchases; proxy DEF 14A (filed 2026-03-27,
  `0001308179-26-000168`): pay design, the summary compensation table, ownership, board leadership; 8-K of 2026-07-29
  with Exhibit 99.1, the Q2 2026 release (`0000040533-26-000029`): its non-GAAP measures; 10-K FY2022 (filed 2023-02-07,
  `0000040533-23-000014`): segment margins of 2021 and 2022. Competitors: Textron 10-K FY2025 (filed 2026-02-11,
  `0000217346-26-000006`), Textron Aviation segment table; the others from their own 10-K facts (Q2).
- **One figure cross-checked against the filed statement:** operating cash flow FY2025 **$5,120M**, capital
  expenditures **$1,161M** and equity-based compensation **$196M** in the filed Consolidated Statement of Cash Flows (10-K
  FY2025, `0000040533-26-000006`) against `tools/run.py`'s 5,120, 1,161 and 196: they agree. FY2023 (4,710 / 904 / 181)
  agrees as well.
- **`python tools/run.py GD`, arithmetic lines only** (saved as `run_py_output.txt`). The share count it uses (270.430M,
  cover of 2026-04-05) is superseded by the July cover above. It flags "other capital payments" in the financing
  section: finance-lease principal of 55, 64 and **556** in 2023 to 2025; the 10-K's lease note says the 2025 figure
  "included approximately $ 490 for the exercise of options to purchase the underlying assets" (`0000040533-26-000006`).
  That is a purchase of assets, a real capital cost, and is carried as the alternate below. Nothing the tool prints as a
  rule, id, floor or verdict is used (Part VII).

**Owner cash after every real cost** = operating cash flow less stock pay less all capital expenditures (USD millions;
stock pay is added back inside operating cash flow, so it is deducted again here as the real cost it is; interest,
taxes and pension contributions are already paid inside operating cash flow). Filed figures; 2021 and 2022 from the
company's 10-K facts (first-filed vintage, `series.py`, accessions `0000040533-22-000007`, `0000040533-23-000014`):

| FY | OCF | stock pay | capex | owner cash | alternate, less finance-lease principal | D&A (run.py) |
|---|---|---|---|---|---|---|
| 2021 | 4,271 | 126 | 887 | **3,258** | 3,258 (not tagged) | n/a |
| 2022 | 4,579 | 165 | 1,114 | **3,300** | 3,300 (not tagged) | n/a |
| 2023 | 4,710 | 181 | 904 | **3,625** | 3,570 | 863 |
| 2024 | 4,112 | 183 | 916 | **3,013** | 2,949 | 886 |
| 2025 | 5,120 | 196 | 1,161 | **3,763** | 3,207 | 924 |
| **5-yr mean** | | | | **3,391.8** | 3,256.8 | |

The long record (10-K facts, first-filed; owner cash on the same definition): 2,529 (2008), 2,353 (2009), 2,498 (2010),
2,652 (2011), 2,123 (2012), 2,546 (2013), 3,079 (2014), 1,820 (2015), 1,706 (2016), 3,325 (2017), 2,318 (2018),
1,861 (2019), 2,763 (2020). Owner-cash yield at the price: 3,391.8 / 89,749 = **3.78%** after corporate tax (alternate
3.63%), against the sovereign at 5.66%. In H1 2026 operating cash flow was 4,035 against 1,450 a year earlier, of which
1,168 was a rise in customer advances (10-Q, `0000040533-26-000032`): timing, not a new level, and it is not added to
the base.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own General Dynamics "if the market closed for five
years" **[M1997-109]**, so the run asks what Electric Boat, Gulfstream, Land Systems and GDIT will earn, not where the
quotation goes. No macro forecast enters: "macro conclusions are — just never enter into the discussion"
**[M2000-094]**. The margin of safety bears hardest: a decision that needs pencil and paper is "too close to
think about" **[M1996-084]**. Who is paid to tell you: the company's own measures are free cash flow before stock pay and
a return on invested capital that adds back amortization (10-K FY2025 MD&A); both are read at Q4. The analyst's habit
kept: look for "what you’re missing" **[M2025-013]**. Defense budgets, wars and the administration's spending moves that
the 10-K's Business Environment section leads with are read only as evidence about GD's own cash, not as a forecast.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The v5 ledger holds Buffett on this company in 1994: "We think the management of General Dynamics has done an
   absolutely sensational job. Obviously, also it isn’t the kind of business, basically, that we have a 20-year view
   on, or something of the sort." **[M1994-063]**. The company of 1994 is not the company of 2025 (Gulfstream was bought
   "more than 25 years ago", Item 1, FY2025), but the speaker's own view of the defense business is on the record.
2. About 68% of 2025 revenue came from the U.S. government; "U.S. government contracts generally permit the government
   to terminate a contract, in whole or in part, for convenience" (Item 1A, `0000040533-26-000006`).
3. In 2025 "federal government staff reductions, contract modifications and terminations, and award delays" hit the IT
   services business, and the M10 Booker vehicle program was terminated (MD&A, same filing).
4. Marine Systems' operating margin fell from 8.3% (2021) to 6.5% (2024) and 7.0% (2025) on "supplier cost growth"
   (10-K FY2022 `0000040533-23-000014`; 10-K FY2025); the consolidated operating margin fell from 13.7% (2016) to 10.0% to
   10.2% (2023 to 2025) (10-K facts, `peers_output.txt`).
5. Technologies carries goodwill of 14,416 (end 2024) of the company's 20,556, earns 1,277 of operating earnings on
   19,252 of identifiable assets, and its fair value "exceeded its carrying value by approximately 25%" at the last
   quantitative test in 2022 (10-K FY2025, Notes and critical accounting policies).
6. Owner cash grew from 2,529 (2008) to 3,763 (2025), about 2.4% a year in aggregate, while 9.7B went into the CSRA
   purchase in 2018 (PaymentsToAcquireBusinesses 10,099 in 2018, 10-K facts `0000040533-19-000010`).
7. The company's stated buyback policy is "opportunistic share repurchases primarily to address dilution" (MD&A FY2025);
   2026's purchases cost $319M for 0.9M shares, about $354 a share (10-Q Q2 2026).
8. Operating earnings of 833 and a net loss of 332 in 2012 (10-K facts, `0000040533-13-000005`): a large write-down in
   that year.

## THE STANDING RULE
A marketable stake bought for cash and held unlevered, with no instrument that can demand cash of the buyer, does not
risk "what we have and need for what we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place in the
investor's tool kit" **[L2014-005]**, so none is assumed. Nothing in the target can call on the buyer. Satisfied.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (Item 1 and segment note, 10-K FY2025, `0000040533-26-000006`). Ten business units in four
  segments; 2025 revenue 52,550 and segment operating earnings 5,531 (corporate costs 175 below them):
  | Segment | 2025 revenue | share | 2025 operating earnings | share | what it is |
  |---|---|---|---|---|---|
  | Marine Systems | 16,723 | 32% | 1,177 | 21% | Electric Boat ("prime contractor and lead shipyard on all Navy nuclear-powered submarine programs"), Bath Iron Works (DDG-51 destroyers, "one of two companies"), NASSCO (auxiliary ships, repair) |
  | Aerospace | 13,110 | 25% | 1,746 | 32% | Gulfstream business jets (aircraft manufacturing 9,413) and aircraft services 3,697 (Gulfstream service, Jet Aviation FBOs and completions) |
  | Combat Systems | 9,246 | 17% | 1,331 | 24% | Land Systems ("sole-source producer" of the Abrams tank and Stryker), European Land Systems (Piranha, ASCOD), Ordnance and Tactical Systems (tank and medium-caliber ammunition, propellants, rocket-motor parts) |
  | Technologies | 13,471 | 26% | 1,277 | 23% | GDIT (IT services 9,057: cloud, cyber, network modernization for defense, intelligence and civilian agencies) and Mission Systems (C5ISR 4,414: encryption, radios, submarine fire control) |
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**; the technology itself need not be known if "I understand the economic
  dynamics of the industry" **[M2011-014]**. The key variables **[M1998-044]**, part by part:
  (a) **Marine:** Navy submarine and destroyer procurement, and the yard's ability to execute fixed-price and
  cost-reimbursement work. The program of record is written down by the customer: Columbia-class, "a 12-boat program"
  whose "Construction is scheduled to span two decades", program value "in excess of $125 billion"; 14 Virginia-class
  boats in backlog "scheduled for delivery through 2034"; 11 DDG-51 destroyers "through 2032"; Marine backlog 52,340
  (Item 1 and MD&A FY2025). Where Electric Boat will be in ten years, building submarines for one customer at margins the
  customer allows, is about as foreseeable as an industrial business gets.
  (b) **Aerospace:** the demand of the rich, of companies and of governments for large-cabin jets, Gulfstream's place
  among "several competitors for each of its Gulfstream products" (Item 1), and the services tail of "more than 3,000
  Gulfstream aircraft in service". The volume is cyclical (owner cash 2,529 in 2008 to 2,353 in 2009, and the segment's
  own record moves with deliveries), but the economics, a product sold by brand and range with a growing installed base
  to service, are foreseeable in kind.
  (c) **Combat:** sole-source vehicle franchises and munitions; "The vehicle programs are generally long-term franchise
  programs, while the weapon systems and munitions programs tend to be shorter-term in nature" (MD&A). Foreseeable in
  kind; volume swings with programs (the M10 Booker terminated in 2025).
  (d) **Technologies:** federal IT services and defense electronics. This is the part the doubt rule bears on.
- **The technology part.** Technologies is a quarter of revenue and 23% of segment earnings, and the 10-K itself says
  "With technology evolving at an unprecedented pace" (Item 1). Change is "more of a threat into the investment process
  than an opportunity" **[M1999-063]**, and "if you have doubts about something being into your circle of competence, it
  isn’t" **[M2002-092]**. What I can and cannot foresee: the *economics* of a government IT contractor have been stable
  for fourteen years through cloud, mobile and the rest, because the work is billed to the government as labor and
  fee under cost-reimbursement and time-and-materials terms (44% and 5% of GD's U.S. government revenue, Item 1): the
  listed IT-services rivals' operating margins sat at 6.8% to 9.6% (CACI) and 4.8% to 11.4% (Booz Allen) in every year
  2012 to their latest 10-K (competitor row, Q2), and GD's own segment at 9.3% to 10.2% (2021 to 2025). Which firms win
  the volume, and how much of the labor AI removes from the government's bill, I cannot foresee; the insiders do bid
  multi-year indefinite-delivery contracts, "approximately 85% of the segment’s orders were from additional work on IDIQ
  contracts or the exercise of options" (MD&A), so they write down at least the next several years **[M2000-105]**. Read
  by its parts, the doubt is about the volume of a minority part whose margin structure is foreseeable, not about where
  the whole will be. I record it as the weakest part of Q1 and carry it to Q2 and Q7, and I note that **[M2002-092]**
  read strictly would send a quarter of the company outside the circle.
- **The speaker on this company.** **[M1994-063]**: not "the kind of business, basically, that we have a 20-year view
  on". That was said of the GD of 1993, then shrinking after the Cold War; it is a holding-period judgment, not a
  statement that its economics could not be foreseen, and the row's own reading in the ledger is that "the business's
  own durability sets the holding view". It is carried to Q2, where durability is asked.
- Would the insiders write the forecast down **[M2000-105]**? For submarines the customer has written it down for two
  decades; for Gulfstream the backlog is 21,828 with "orders for all models" (MD&A); for vehicles the backlog is 27,218.
- **VERDICT: IN.** About three-quarters of the earnings come from submarines, destroyers, combat vehicles, munitions and
  business jets whose ten-year economics can be foreseen in kind **[M2012-065]**, **[M2011-014]**; the remaining part,
  Technologies, has economics whose structure is foreseeable and a volume that is not, and is carried as the doubt
  **[M2002-092]**. The holding company is read by its parts (CONVENTION, Q1 of the framework).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**, starting from the attacker, since "all moats are subject to attack".

**The record the castle must explain** (operating margin %, 10-K facts first-filed, `peers_output.txt`; segment margins
from the segment tables of 10-K FY2022 `0000040533-23-000014` and 10-K FY2025 `0000040533-26-000006`; operating
earnings over total assets less goodwill and intangibles from the balance sheets in `run_py_output.txt`, my arithmetic):

| | 2012 | 2014 | 2016 | 2017 | 2019 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| GD operating margin | 2.6 | 12.6 | 13.7 | 13.5 | 11.8 | 10.8 | 10.7 | 10.0 | 10.1 | 10.2 |
| Aerospace | | | | | | 12.7 | 13.2 | 13.7 | 13.0 | 13.3 |
| Marine Systems | | | | | | 8.3 | 8.1 | 7.0 | 6.5 | 7.0 |
| Combat Systems | | | | | | 14.5 | 14.7 | 13.9 | 14.2 | 14.4 |
| Technologies | | | | | | 10.2 | 9.8 | 9.3 | 9.6 | 9.5 |
| GD op. earnings / tangible assets | | | | 18.6 | 17.3 | 14.9 | | 13.0 | | 15.4 |

**The competitor row** (each competitor's own filings; operating income over revenue from its 10-K facts, first-filed
vintage, unless stated):

| Company (latest 10-K accession) | Competes with | Operating margin through the record |
|---|---|---|
| Huntington Ingalls HII (`0001501585-26-000006`) | Marine: the "one primary competitor", partner on Virginia, subcontractor on Columbia (Item 1, GD) | 5.3 (2012), 11.0 to 12.1 (2015 to 2018), 8.3 to 8.5 (2019 to 2020), 4.6 to 6.8 (2021 to 2025) |
| Textron Aviation segment, Textron TXT (10-K FY2025 `0000217346-26-000006`, segment table) | Aerospace: business jets and aftermarket | segment profit margin 12.1 (2023), 10.7 (2024), 11.7 (2025), against GD Aerospace 13.7, 13.0, 13.3 |
| Lockheed Martin LMT (`0001628280-26-004195`) | defense primes generally | 9.4 (2012) to 14.3 (2019), 9.9 to 10.3 (2024 to 2025) |
| Northrop Grumman NOC (`0001133421-26-000003`) | defense primes, mission systems | 11.0 to 13.3 (2012 to 2020), 6.5 to 10.8 (2022 to 2025) |
| CACI (`0001628280-26-054195`) | Technologies: federal IT | 6.8 to 9.6 in every fiscal year to the latest |
| Booz Allen BAH (`0001628280-26-037521`) | Technologies: federal IT | 4.8 to 11.4 in every fiscal year to the latest |
| Leidos LDOS (`0001336920-26-000030`) | Technologies: federal IT | minus 4.2 to 12.3; 2019 and 2024 not tagged in the series |

(Fiscal-year labels for CACI, BAH and LDOS follow their period ends; the series is a transcription, the GD and Textron
figures were read in the filed tables.) No Combat Systems competitor files with the SEC on a comparable segment; the
rows of the primes stand in for it.

**The castle tests, each with its filing fact.**
1. **The key factors and how permanent** **[M1995-038]**. Marine: the customer needs nuclear submarines and only two
   U.S. yards build them, one of them GD's partner; Electric Boat "leads the construction of both Columbia-class
   ballistic-missile submarines and Virginia-class attack submarines" on programs scheduled two decades out (Item 1).
   Combat: "sole-source producer" of the Abrams and Stryker with "a large installed base" (Item 1). Aerospace: a brand and
   an installed base ("more than 3,000 Gulfstream aircraft in service") with a service network that grows with it. These
   are permanent in kind. Technologies: none named beyond scale and cleared people; it "competes with many companies,
   from large government contracting and commercial technology companies to small niche competitors" (Item 1).
2. **Would it stand without the lord?** The castle in Marine and Combat is the customer's need and the cost of entry,
   not a person. But profit there depends on execution: "Earnings and margin depend on our ability to perform on our
   contracts" (Item 1A), and the 2024 Marine margin fell on "supplier cost growth". The business "that doesn’t require
   good management" **[M1996-037]** is not this one on margin; it is on tenure.
3. **The money test** **[M2011-015]**, **[M1997-103]**. Could a hundred billion dollars build a rival nuclear-submarine
   yard? The filing names one primary competitor in the segment, and that competitor is GD's partner on the same boats
   (Item 1). No attacker with money has appeared in the record read. In business jets the attackers exist and are named
   ("several competitors for each of its Gulfstream products"), and Textron Aviation, the listed one, earned a lower
   margin than GD Aerospace in each of the three years read. In federal IT anyone with cleared people can bid, and
   "anything you do, your competitors can copy" **[M1996-017]** is the fair description: GD's segment margin is inside
   the rivals' band, not above it.
4. **Pricing power and the agony before a rise** **[M2005-020]**. Against: in defense the customer sets the terms. U.S.
   government revenue is 51% fixed-price, 44% cost-reimbursement, 5% time-and-materials, under the FAR and the Cost
   Accounting Standards, which govern "the allowability of our costs" (Item 1); the government can terminate "for
   convenience" (Item 1A). Marine's margin of 6.5% to 8.3% and HII's fall from about 12% to about 5% are the price of
   having one customer who writes the rules. This is the shape **[M2007-112]** gives a regulated business: a pricing
   power tempered by the regulator, "It will never be a sensational business", but "if they earn a decent return on
   capital, it can be a good business over time". In Aerospace, tariffs "did reduce the Aerospace operating margins by 30
   basis points in 2025" (MD&A), i.e. the cost was not fully passed on that year; no statement of Gulfstream price
   increases was found in the 10-K read.
5. **Unit volume and share of mind** **[M1999-054]**. Gulfstream deliveries 136 (2024) to 158 (2025) with a 1.2-to-1
   book-to-bill as revenue grew 16.5%; city-pair speed records ("more than 350") are the brand's own share-of-mind claim
   (Item 1, MD&A). Defense backlog 70.9B (2024) to 96.2B (2025), total backlog 136.5B at Q2 2026 (Exhibit 99.1,
   `0000040533-26-000029`).
6. **The low-cost position** **[M2018-043]**. The company says it strives "to be the low-cost, high-quality provider in
   each of our markets" (Item 1). That is a statement of aim; no filing figure read proves it. The DDG-51 award was
   "competitively awarded" (Item 1), so Bath Iron Works lives on the low bid against one rival.
7. **The brand in the customer's mind** **[M2015-038]**: Gulfstream only. Elsewhere the customer is a procurement office.
8. **Would the customer still choose it over the low bid** **[M2017-009]**? For submarines the Navy has no third
   bidder, and for the Abrams it has the sole source. That is a choice forced by capacity and security, not by
   preference, and it is paid for at the customer's margin.
9. **Ask the competitors** **[M1999-130]**: the public record of the one shipbuilding competitor shows it partnering with
   GD on the same boats (Item 1); no other answer was found on the record. Not answered further.
10. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Widening in tenure: backlog up 30% in 2025 and capacity
    being built for "one Columbia-class submarine plus up to two Virginia-class submarines per year" (Item 1). Narrowing
    in margin: consolidated 13.7% (2016) to 10.2%; Marine 8.3% to 7.0%; return on tangible assets 18.6% (2017) to 13.0%
    to 15.4%. Part of the consolidated fall is mix (Technologies added by the 2018 purchase, Marine grown fastest), not a
    rival crossing the moat.
11. **What could destroy, modify or reduce it** **[M2000-014]**. A change in what the customer buys (unmanned systems in
    place of crewed ships and vehicles; the Army "reviewing its funding priorities", MD&A); budget and termination for
    convenience; for Technologies, the 2025 contract terminations and the labor AI may remove; for Gulfstream, a
    business-jet recession. None of these is shown under way against the submarines, whose program runs two decades.

**The judgment.** The castle is standing, and the reason is plain: nobody else can build what the Navy and Army buy
from GD, and the programs are written down for two decades. What the castle protects is tenure and volume, not a high
return: the customer takes the surplus, and the margins in shipbuilding have narrowed. That is not a castle shown open
**[M2011-015]**: no attacker has crossed it. Nor is its future out of reach: the customer's own procurement plan runs
past the horizon. Technologies has no castle beyond incumbency and earns what its rivals earn; it is a quarter of the
company and the part least protected. The speaker's 1994 holding-period remark **[M1994-063]** is weighed here and
answered in part by the change in the company since, not refuted.
- **VERDICT: IN**, with the weights carried forward: a moat that protects a decent return rather than an excellent one
  **[L2007-004]**, **[M2007-112]**, and a quarter of the earnings in a field where competitors can copy **[M1996-017]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**. The customer funds much of the working
  capital: customer advances and deposits 9,824 at end 2025 against inventories 9,232 and unbilled receivables 8,380
  (balance sheet, 10-K FY2025). My arithmetic from the filed balance sheet: tangible assets 34,865 (57,249 less goodwill
  21,009 and intangibles 1,375), less cash 2,333, less accounts payable 2,678, customer advances 9,824 and other current
  liabilities 3,288, leaves **16,742** of net operating tangible capital; operating earnings of 5,356 on it is about
  **32% pre-tax**. On all tangible assets it is 15.4%; on all assets including the purchased goodwill, 9.4%. Goodwill is
  read separately: forgotten when judging the business, counted when judging the capital allocation "because we paid
  for it" **[M2011-060]**. The high figure is the business; the low one is what its owners paid for Technologies.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capex ran above depreciation of plant
  in every year read: 904 against 608 (2023), 916 against 644 (2024), 1,161 against 680 (2025) (cash flow statements,
  10-K FY2025). The company names the excess as growth: "capital investments in Marine Systems to support significant
  growth in U.S. Navy ship and submarine construction over the next two decades" (Item 1); Marine's 2025 capex was 517
  against its D&A of 270 (segment note). Depreciation as the maintenance proxy is "not inappropriate in most companies"
  **[M1998-127]**, and I take it so here, as a guess the filing allows but does not state: owner cash with depreciation
  of plant in place of capex is 3,921 (2023), 3,285 (2024), 4,244 (2025). The all-capex figure is kept as the Q7 base
  (Part VI's PG specifics); the depreciation variant is shown beside it in Q7.
- **The growth arithmetic** **[M2001-019]**, **[M2023-081]**. From 2017 to 2025 operating earnings rose 1,179 (4,177 to
  5,356) while tangible assets rose 12,435 (22,430 to 34,865): about 9.5% pre-tax on the added tangible capital, and
  about 5.3% on the 22,203 rise in total assets, which includes the 2018 purchase (balance sheets, `run_py_output.txt`;
  operating earnings, 10-K facts). Aggregate owner cash rose about 2.4% a year from 2008 to 2025. Rising earnings do not
  by themselves show a high return on the added money: "We just put way more capital into the business" **[M2023-081]**.
  The ship programs require the capacity: a business where "you have to spend money like crazy if it’s attractive to
  spend money" **[M1998-128]** describes the Navy's yards in part, though the customer contributes to the facilities
  ("Along with strong contributions from the states of Connecticut and Rhode Island", Item 1) and the advances fund the
  work in progress.
- **WEIGHS: UNDECIDED.** The business itself earns a high pre-tax return on the operating capital it needs because its
  customers prepay **[M1995-047]**; the money added since 2017, most of it a purchase of an IT-services business, has
  earned a fair return at best **[L2009-012]**, **[M2018-055]**. The capital-heavy second best, "good enough"
  **[M2018-056]**, not the best business. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, nine year-ends of them, before the income account** **[M2025-032]** (USD millions; 10-K
  facts first-filed, transcribed by `tools/run.py`; 2024 and 2025 read in the filed balance sheet of 10-K FY2025;
  revenue from the filed income statements via the 10-K facts):

  | year-end | assets | equity | goodwill + intangibles | cash | receivables | inventory | debt | retained | revenue |
  |---|---|---|---|---|---|---|---|---|---|
  | 2017 | 35,046 | 11,435 | 12,616 | 2,983 | 3,617 | 5,303 | 3,982 | 26,444 | 30,973 |
  | 2018 | 45,408 | 11,732 | 22,179 | 963 | 3,759 | 5,977 | 12,417 | 29,326 | 36,193 |
  | 2019 | 48,841 | 13,577 | 21,992 | 902 | 3,544 | 6,306 | 11,930 | 31,633 | 39,350 |
  | 2020 | 51,308 | 15,661 | 22,170 | 2,824 | 3,161 | 5,745 | 12,998 | 33,498 | 37,925 |
  | 2021 | 50,073 | 17,641 | 22,076 | 1,603 | 3,041 | 5,340 | 11,495 | 35,420 | 38,469 |
  | 2022 | 51,585 | 18,568 | 22,158 | 1,242 | 3,008 | 6,322 | 10,496 | 37,403 | 39,407 |
  | 2023 | 54,810 | 21,299 | 22,242 | 1,913 | 3,004 | 8,578 | 9,261 | 39,270 | 42,272 |
  | 2024 | 55,880 | 22,063 | 22,076 | 1,697 | 2,977 | 9,724 | 8,762 | 41,487 | 47,716 |
  | 2025 | 57,249 | 25,622 | 22,384 | 2,333 | 2,406 | 9,232 | 8,013 | 44,080 | 52,550 |

  What moved and why. **Goodwill and debt** jumped together in 2018: goodwill and intangibles 12,616 to 22,179 and debt
  3,982 to 12,417, the year of 10,099 of business purchases (10-K facts, `0000040533-19-000010`); the debt has been paid
  down every year since 2020 to 8,013, and equity more than doubled, so tangible equity went from about minus 10,447
  (2018) to about plus 3,238 (2025). **Receivables** fell from 3,617 to 2,406 while revenue rose 70%: billed receivables
  are not where the growth went. **Inventory** rose from 5,303 to 9,232, most of it in 2023 and 2024 (8,578 and 9,724)
  as Gulfstream built G700s and G800s ahead of certification and delivery; the 10-K says 2024 cash flow was "affected
  negatively by growth in operating working capital", and 2025 "positively as operating working capital balances in
  our Aerospace and Combat Systems segments began to unwind" (MD&A FY2025), and the inventory line did fall 492 in 2025.
  That is the rhythm of a new-model ramp, read in the filing, not a build-up the filing does not explain
  **[M1995-064]**. Unbilled receivables (8,380) are matched by customer advances (9,824). **Retained earnings** rose
  every year, 26,444 to 44,080, beside treasury stock of 22,860 (2025). What the figures cannot say
  **[M2025-032]**: how much of the contract margin rests on estimates at completion. "Typically, revenue is recognized
  over time using costs incurred to date relative to total estimated costs at completion" (MD&A), and the margin moves
  when those estimates move; the 2024 Marine "supplier cost growth" was such a move.
- **The real costs.** Depreciation is a real cost here **[L2015-004]**; capex exceeded it every year read (Q3), and the
  Q7 base deducts all capex. Stock pay (196 in 2025) is deducted. Amortization of purchased intangibles (244 with
  finance-lease right-of-use amortization, 2025) is added back in the company's own return on invested capital; most of
  it is the purchased contract and customer relationships of Technologies, which "Some truly deplete over time"
  **[L2012-003]**, and the Q7 base, built from cash, neither adds nor subtracts it. A large write-down sits in the
  record: goodwill impairment of **1,994** in 2012 (10-K facts, `0000040533-13-000005`), the year of the net loss; one
  such charge in fourteen years is not the recurring "one-time" **[L2016-007]**. Pension cost on the government plans is
  deferred: "We have elected to defer recognition of the benefit costs until such costs can be allocated to contracts"
  (MD&A FY2025); the cash contributions are inside operating cash flow, which the Q7 base uses.
- **EBITDA in the filer's own mouth** **[M1998-086]**, **[L2016-006]**: no instance found in the 10-K FY2025 MD&A, the
  Q2 2026 release or the proxy by a text search for "EBITDA" and "adjusted". The company's non-GAAP measures are two:
  free cash flow, "net cash from operating activities less capital expenditures", which does not deduct stock pay; and
  ROIC, which adds back after-tax amortization (MD&A FY2025; Exhibit 99.1 Q2 2026). Both are stated with their
  reconciliations and both are mild. Speech is clear and segment by segment, the kind **[M1994-018]** counts as a plus.
- **The make-the-numbers habit** **[L2002-041]**. The company publishes a yearly outlook by segment ("2026 Outlook" in
  MD&A FY2025), and the proxy pays the annual bonus on "diluted EPS (25%), FCF (25%) and operating margin" against
  targets, the EPS target "set 6.4% higher than 2024’s actual performance" (DEF 14A, `0001308179-26-000168`). Guidance and
  pay on hitting it weigh against **[M2022-054]**. No second tell was found (no reserves that move, no adjusted earnings
  featured, no prepaid or deferred accounts building unexplained), so under the two-tell CONVENTION it is a weighing,
  not suspicion.
- **Cross-check of the base.** Owner cash recomputed from the filed cash-flow statement agrees with the tool (Step 0).
- **VERDICT on confusion: IN.** The accounts can be read and say what they mean **[M1994-079]**; nothing that confused
  was found **[M1995-063]**. **WEIGHS FOR**, modestly: no EBITDA, clear reports, a balance sheet whose movements the
  filing explains; against it the guidance and the EPS-target bonus **[L2002-041]**. The recast earnings fed to Q7 are
  owner cash after all capex and stock pay, five-year mean 3,391.8 (alternate 3,256.8 after the 2025 lease buy-out).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Phebe N. Novakovic, Chairman and Chief Executive Officer; "service as a senior officer of General Dynamics
  since 2002", including as head of Marine Systems (DEF 14A, `0001308179-26-000168`). The roles are combined, with an
  independent Lead Director (Laura J. Schumacher, "Lead Director (2023 to Present)") who chairs executive sessions without
  management (same).
- **The two yardsticks** **[M1994-008]**. How well they run it, against the hand dealt: through 2021 to 2025 the
  segment margins held inside narrow bands (Q2 table) while revenue rose from 38,469 to 52,550, debt fell from 11,495
  to 8,013, and the new Gulfstream line was certified and delivered; against that, Marine's margin fell on supplier cost
  growth, as HII's did more (Q2 row), and the 2018 purchase earns 6.6% pre-tax on the assets now carried for it
  (Technologies 1,277 on 19,252, segment note FY2025). How well they treat the owners: read in the proxy **[M1994-009]**
  below and in the capital record at Q6.
- **The proxy, how they treat themselves** **[M1994-009]**. CEO total pay 2025 **$25,924,082** (salary 1,737,500,
  stock awards 12,539,634, options 5,220,445, annual incentive 5,729,000); 2024 $23,794,702 (summary compensation table,
  DEF 14A). Against it, she owns **802,357 shares** outright plus 573,565 exercisable options (ownership table as of
  March 11, 2026), about $266M of stock at the run's price, and the guideline is "at least 15 times base salary";
  hedging and pledging are prohibited and there is a clawback (DEF 14A). Rich with the shareholders, not off them, is
  the test **[M2003-055]**; a holding of that size bought or kept rather than sold points that way, though the proxy
  read does not separate shares bought with savings from shares received as pay.
- **The letters and reports** **[M1998-036]**, **[M2007-083]**. The proxy letter is short and factual: record revenue,
  earnings and backlog, "$2.2 billion in dividends and share repurchases to cover the dilution". The 10-K reports by
  segment with the outlook and the causes of margin changes, including the unfavorable ones ("supplier cost growth",
  tariffs costing "30 basis points", the IT business hit by terminations). It is plain, not consultant jargon.
- **How they talk about mistakes** **[L2024-003]**: a text search of the 10-K FY2025 and the proxy for "mistake" found
  no instance. The bad news is reported as facts (above) rather than owned as errors; the 2018 purchase, whose
  reporting unit's fair value exceeded carrying value by "approximately 25%" at the last test, is not discussed as a
  judgment. Neutral to slightly against.
- **The tells of dishonesty.** Too good to be true, dancing reports, a stock price posted in the lobby, serial issuance
  **[L2014-015]**: none found. Share count fell from 398.7M diluted (2008) to 272.4M (2025) (10-K facts); the company
  issues no stock for deals in the record read.
- **VERDICT on integrity: IN.** No doubt found on the record read **[M2013-088]**, **[M2015-047]**. **Ability WEIGHS
  FOR**: a long insider record of steady execution in businesses where execution sets the margin **[M1994-008]**, with
  the 2018 purchase as the one large capital judgment that has earned little (Q6). This is a reading of a marketable
  stake: "In terms of sizing up managements — obviously if we’re going to buy the whole business, that’s a different
  question." **[M2007-081]**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**. What was kept: retained earnings rose 26,444 to 44,080 from
  end 2017 to end 2025 (balance sheets, Q4), 17,636 kept after dividends, beside 8,216 spent on buybacks (2018 to 2025,
  10-K facts) and 10,099 into purchases in 2018. What it became, per share: owner cash per diluted share rose from a
  2015 to 2017 mean of **$7.28** to a 2023 to 2025 mean of **$12.60**, about **7.1% a year**; in aggregate, 5.4% a year
  (`value_output.txt`). The market-value leg cannot be read from the filings read (the performance graph is an image);
  the intrinsic-value leg is: per-share owner cash compounding at about 7% while the company also paid a dividend that
  rose every year ("the 28th consecutive annual increase", MD&A FY2025). Against it: the 2018 purchase. Technologies
  carries goodwill of 14,416 and earns 1,277 pre-tax on 19,252 of identifiable assets (segment note), about 6.6%, below
  the 10% floor the run applies at Q7 and close to the long bond. That dollar did not become more than a dollar on the
  evidence read **[M1994-061]**. The forward question, "Can you keep using all of the capital you generate, effectively,
  for a very long time?" **[M2010-097]**: the shipyard capacity the Navy wants will take capital for two decades at
  Marine's margin; the rest is paid out.
- **Buybacks** **[L1999-023]**, **[L2011-003]**. The stated policy is "opportunistic share repurchases primarily to
  address dilution" (MD&A FY2025), and the 2025 and 2026 purchases were made "to cover dilution" (Note N; 10-Q Q2 2026).
  Buying to cover options is ruled out by name **[M2014-008]**, and "dilution by itself is a negative and buying back
  your stock at too high a price is another negative. So it has to be related to valuation." **[M2016-049]**. No price
  above which purchases stop is stated **[L2016-002]**. Under the CONVENTION the prices paid are read against the
  bottom of the Q7 range, **$221** (run at Q7, recorded back here): 2023 about **$217** a share (at the bottom), 2024
  about **$278**, 2025 about **$255** (inside the range, above its bottom), H1 2026 about **$354** (above its top)
  (cash paid over shares bought, 10-K FY2025 Note N and 10-Q Q2 2026). Weighs against.
- **Issuance and deals** **[L2014-012]**. The 2018 purchase was paid in cash and debt (debt 3,982 to 12,417), not stock;
  the STOP for an all-stock deal by an undervalued acquirer **[L2009-019]** does not arise. No serial issuance
  **[L2014-015]**. What was given (about 10.1B plus the debt's cost) against what was got (a segment earning about 6.6%
  pre-tax on its assets): value given exceeded value got on the evidence read, though the company does not say so.
- **Dividends** **[M2004-089]**, **[L2012-015]**. Paid out what Marine and the rest did not need: dividends 1,593 in
  2025; the policy is stated as "a predictable dividend" and has been consistent. Clear, consistent, rational.
- **Part A WEIGHS: UNDECIDED.** Per-share owner cash compounded at about 7% with a rising dividend **[R1995-009]**, set
  against the one large purchase that earns about the bond rate and buybacks made to cover dilution at prices not tied
  to value **[M2016-049]**, **[L2016-002]**.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**. The annual bonus is "formulaic and based on three financial
  metrics of EPS (25%), FCF (25%) and operating margin", plus strategic goals; the long-term grant is "50% PSUs, 30% stock
  options and 20% restricted stock", the PSUs "tied to three-year ROIC with an rTSR modifier" (DEF 14A). Operating margin
  and cash are within management's control; ROIC carries a capital charge of sorts. Against: options are 30% of the
  grant with an exercise price at "the average of the high and low quoted price" on the grant date and no step-up for
  retained earnings, "a royalty on money that you left with me" **[M1997-043]**, **[L1994-021]**; no instance found of
  the dividend conflict named in the proxy **[L2005-014]** (text search for "dividend" near the option plan not made in
  full; recorded as not checked). Relative TSR rides the market **[M2000-062]**.
- **Who designs it** **[M2004-016]**, **[M2012-095]**: "Aon provided survey data for the peer group used to benchmark
  executive compensation", and the 2025 grant increase "is generally aligned with changes in market pay opportunity
  levels observed among our peer group" (DEF 14A): the peer ratchet, in the company's own words.
- **The board** **[M2007-120]**, **[L2014-026]**. Chairman and CEO combined, with a Lead Director; the CEO is not
  mediocre on the record read, which is the condition L2014-026 attaches to the combined role.
- **The owners as partners** **[L1994-023]**. Plain reporting by segment; but yearly guidance by segment **[M2022-054]**.
  A large holder of record is Longview Asset Management, "deemed to beneficially own 27,060,944 shares" for its clients
  (DEF 14A), about 10% of the company: a large owner in the room **[M2006-011]**.
- **Part B WEIGHS: AGAINST, mildly.** The person outranks the plan **[M2007-006]**, and the person reads well; the plan
  itself is a peer-benchmarked, option-bearing, EPS-target design of the kind the rows weigh against **[M1997-043]**,
  **[M2004-016]**.

## Q7 — WHAT IS IT WORTH? STOP.
The three questions: how certain the birds, when and how many, and "the yield on long-term U.S. bonds" **[L2000-021]**;
"use the government bond rate" **[M1996-025]**; no risk premium in the rate, the margin taken as "a big discount" from
the present value **[M1997-126]**; held as a range **[L2000-024]**, **[L1999-027]**. All arithmetic in `value.py`, output
in `value_output.txt`.

**COMPUTATION — the range, under the CONVENTION of Q7 (Part VI):**
- **Base:** five-year mean of owner cash after every real cost, **3,391.8** (Step 0; all capex and stock pay deducted).
  Alternate **3,256.8** with the finance-lease principal deducted where tagged (the 2025 lease buy-out). Depreciation
  variant (Q3's maintenance guess, depreciation of plant in place of capex, 2023 to 2025 only) **3,816.7**.
- **Growth shown,** on aggregate owner cash (PG specific): 2021 to 2025 endpoints **3.67%** a year; a log-linear fit
  through the five years **1.99%**; the long record 2008 to 2025 **2.37%**. The endpoint figure is the highest of the
  three and is used as the shown-growth case, so the range's top is the generous one. Cap of Q3: below the discount rate
  **[M1997-095]**, and no absurdity **[M1999-067]**; the backlog (136.5B at Q2 2026) supports volume, while the margin is
  the customer's (Q2).
- **Term:** ten years at the growth shown, then zero nominal growth (PG specific), discounted at **5.66%**.
- **The range:** no-growth **$59,926M = $221 a share**; shown growth (3.67%) **$80,134M = $296 a share**. With the
  fitted growth the top would be $259; on the alternate base $213 to $284; on the depreciation variant $249 to $333.
  **Width 296 / 221 = 1.34**, well inside three to one: the range is narrow enough to conclude from **[L2000-025]**.
- **Against the price of $331.72:** the price is **above the top** of the range on the all-capex base, and equal to the
  top ($333) only on the most generous variant (depreciation for capex and the highest growth reading together).
- **The floor (CONVENTION, about ten percent pre-tax** **[M1994-004]**, **[L2002-020]**, **[M2003-149]**): expected
  return at the price = owner-cash yield 3.78% plus growth shown 3.67% = **7.45% after tax**; grossed up at the 2025
  effective tax rate of 17.5% (MD&A; the gross-up is ours, CONVENTION: owner cash is after corporate tax and the floor is
  stated pre-tax) about **9.0% pre-tax**. On the fitted growth, 7.0% pre-tax. On the depreciation variant with the
  highest growth, 9.6%. Every reading is below the floor; at the price, this is "a point at which we drop out of the
  game" **[M2003-149]**.
- **The two prices, for the record** (same CONVENTION gross-up): the price at which the central case (all-capex base,
  3.67% growth) earns ten percent pre-tax, **"fair" about $274**; the price at which no-growth owner cash alone earns it,
  **"cheap" about $152**. Neither is entry language; they are what the floor implies.

**The judgment.** How sure: the submarine program is as certain as a defense cash stream gets, and the moat and the
people enter as "the degree of certainty" **[M1999-104]**; the Technologies quarter and the customer's hold on margin
are why the range is not drawn wider at the top. The range is narrow; the price sits above it. A price inside or above
a narrow range is not a screamer: "if you really need a calculator to figure out" it, "forget about the whole exercise"
**[M2009-005]**; "If you have to carry it out to three decimal places, it’s not a good idea." **[M2008-068]**. Here no
pencil is needed in the other direction: on every base and growth reading the expected return at the price is below the
floor.
- **Value range: $221 to $296 a share against $331.72.** Closes OUT: the price is above the top of a narrow range, and
  the expected return at the price, about 9.0% pre-tax on the generous reading, is below the CONVENTION floor.
- **VERDICT: OUT** **[M2003-149]**, **[M2009-005]**, **[L2013-012]**.
- **Q6 recorded back:** the bottom of the range, $221, is the line the buyback test of Q6 used.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed OUT). For the record only, not a clearance: the owner-cash yield of 3.78% sits below the
30-year Treasury at 5.66% before any growth is credited **[M1997-089]**.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Noted for a future run, not weighed: debt 7,516 and cash 4,333 at 2026-07-05 (10-Q Q2 2026); a
$5 billion committed bank facility; notes refinanced at maturity (MD&A FY2025); foreign-exchange forwards of 8.5B
notional (Item 7A).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** The default is inaction **[M1996-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED** (optional; not asked by the operator for this run).

---
## THE BOX
**OUT — decided at Q7.** Value range **$221 to $296 a share** (five-year owner cash 3,391.8 after all capex and stock
pay; no growth to 3.67% shown growth for ten years; 30-year Treasury 5.66%) against **$331.72**: the price is above the
top of a narrow range, and the expected return at the price, about 9.0% pre-tax on the generous reading, is below the
CONVENTION floor of about ten percent **[M2003-149]**. Q1 IN (by parts, Technologies the doubt), Q2 IN (a castle that
protects tenure, not price), Q3 UNDECIDED, Q4 IN and weighs for, Q5 IN and ability weighs for, Q6 Part A UNDECIDED and
Part B against mildly. **What would reverse it:** a price at or below about $274 (the central case clearing the floor)
with the business unchanged; at about $221 the price would only reach the bottom of the range, and a screamer would
need to be well below it **[M1996-084]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `6087d36`); written question by question; committed after each
      (Step 0, Q1, Q2, Q3, Q4, Q5, Q6, Q7 each its own commit).
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before use; the acceptance test's phantom check
      passes); every filing fact has its accession; numbers not from a filing are my arithmetic from filed figures,
      shown in `value.py`, or labelled CONVENTION (the floor, the range construction, the tax gross-up).
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 are NOT REACHED and nothing
      after Q7 is a clearance.
- [x] Owner cash after every real cost (operating cash flow less stock pay less all capex), never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury par curve, dated 2026-10-05; the price an aggregator quote,
      flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (eight items under the foundations, more in
      the questions).
- [x] No point-in-time anchor: the run is dated today; the one row about this company, **[M1994-063]**, is dated 1994
      and is declared under contamination.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before every commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The floor is pre-tax and owner cash is after tax**, and neither the Q7 CONVENTION nor the PG
specifics say how the two are put on one footing; I grossed the after-tax expected return up at the company's own 2025
effective rate (17.5%) and labelled that CONVENTION. A different gross-up (the statutory 21%) would move "fair" but not
the box. (2) **"The growth the business has actually shown"** does not say how it is measured: endpoints over the five
years gave 3.67%, a log-linear fit 1.99%, the seventeen-year record 2.37%. I used the highest, so the top of the range
is generous, and showed the others; the convention should name one. (3) **The holding company read by its parts** (Q1)
gives no threshold for "a part that matters": Technologies is 23% of segment earnings, and **[M2002-092]** read
strictly would have closed Q1 TOO HARD on a quarter of the company. I read the part's economics as foreseeable in
structure and unforeseeable in volume and passed it, recording the doubt; a second analyst could fairly close Q1 there.
(4) **A castle that protects tenure but not price** (a monopsony customer, sole-source programs, margins the customer
sets) fits none of Q2's two closes cleanly: it is not open, its future can be judged, yet **[L2007-004]** defines the
moat by the "excellent returns" it protects. I passed it IN and carried the low return to Q3 and Q7, where the price
decided it; the framework might say whether "decent returns" protected for decades pass Q2 or belong in Q3 only. Tool
note: `tools/run.py` used the April cover count (270.430M) rather than the July 10-Q cover (270.557M) that
`Screens/cover_shares.py` reads; immaterial here, but the two tools disagree on which filing is latest.
