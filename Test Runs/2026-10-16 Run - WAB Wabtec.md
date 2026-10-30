# Company Run — Westinghouse Air Brake Technologies Corporation, d/b/a Wabtec (NYSE: WAB) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md` with the one departure the brief states: the lines of
evidence are derived by the analyst from the 10-K's Items 1, 1A and 7 (listed in Step 0), and the competitors are the
ones the 10-K names. Research folder: `Test Runs/_research 2026-10-16 WAB/` (raw filings in its ignored `cache/`;
`fetch.py`, `h2t.py`, `xb.py` and the arithmetic script `q7.py` are tracked there).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only; not held.*

**Contamination declared.** Seen by accident and not used: the session's opening git status and recent-commit subjects,
which name another company's run (ticker R) and its fold, and a memory index line about queue state; the `Test Runs`
listing was filtered for this ticker only, and no file about this company was found or opened. No `PORTFOLIO.md`,
holding review, register, reading list, resume-state file or other company's run file was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $287.32 (quote of 2026-10-16 printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator
  rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $.01 par, **168,910,851** shares
  (10-Q for the quarter to 2026-06-30, filed 2026-07-22, cover as of 2026-07-17, accession `0001628280-26-049139`;
  `python Screens/cover_shares.py WAB`). Check against issued less treasury: 171.9M issued less 2.8M treasury = 169.1M
  at 2026-06-30 (same 10-Q, balance sheet); the further fall to 168.9M by the cover date fits the buyback running in the
  quarter (817,959 shares bought April to June, same 10-Q, Part II Item 2). No 8-K or prospectus after the 10-Q issues
  shares: the only later 8-K, 2026-10-01 (accession `0000943452-26-000013`), establishes a commercial paper programme of
  up to $2.0 billion, "As of the date of this Current Report on Form 8-K, the Company has not issued any Notes."
- **Market cap:** 168.911M x $287.32 = **$48,532M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-15
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for 2025, filed 2026-02-13, accession `0001628280-26-008067` (Items 1, 1A, 2, 3, 5, 7, 7A, 8 in full: statements,
    Notes 2, 3, 18, 19 and the stock-pay note).
  - 10-Q for the quarter to 2026-06-30, filed 2026-07-22, accession `0001628280-26-049139` (balance sheet, cash flow,
    equity, Dellner note, Note 14 legal, liquidity, Part II Items 2 and 5).
  - Proxy (DEF 14A) filed 2026-03-31, accession `0001628280-26-022197` (governance, CD&A, incentive metrics).
  - 8-K 2026-07-22, accession `0001628280-26-049105`, Exhibit 99.1 (second-quarter release and guidance).
  - 8-K 2026-10-01, accession `0000943452-26-000013` (commercial paper programme).
  - Earlier 10-Ks for the cycle: FY2024 `0001628280-25-005100`, FY2023 `0001628280-24-004774`, FY2022
    `0001628280-23-003675`, FY2021 `0001628280-22-002997`, FY2020 `0001628280-21-002557`, FY2018
    `0001628280-19-002095` (cash flow statements, segment notes, organic sales bridges, legal notes).
  - Competitor: Caterpillar Inc. 10-Ks FY2025 `0000018230-26-000008`, FY2022 `0000018230-23-000011`, FY2019
    `0000018230-20-000056` (segment profit of the segment that holds Progress Rail).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025, $1,759M, in
  the filed Consolidated Statement of Cash Flows of the FY2025 10-K equals the XBRL figure `tools/run.py` printed
  ($1,759M). A second: 2023 OCF $1,201M, filed statement and XBRL agree.
- **`python tools/run.py WAB`, arithmetic lines only** (its v4 material ignored, Part VII): OCF 2023 to 2025
  $1,201M / $1,834M / $1,759M; capex $186M / $207M / $260M; D&A $531M / $503M / $501M. **Stock pay resolved:** the
  tool deducts the stock-pay note's total ($59M / $85M / $94M, AllocatedShareBasedCompensationExpense); the cash-flow
  statement adds back $47M / $66M / $80M. This run deducts the cash-flow add-back, because operating cash already bears
  any part of the expense that was not added back (the stock-pay note, FY2025 10-K: "$46 million of expense related to
  incentive stock units, $32 million ... non-vested restricted stock, $14 million ... restricted stock units, and $2
  million related to units issued for Directors' fees"). The tool's "no securities, other stock pay, intangible,
  software or mine payments beside capex" line was checked against the filed cash flow statements and holds.

### The lines of evidence this name needs (derived by the analyst from the FY2025 10-K)
| # | Line of evidence | Where it came from | Question |
|---|---|---|---|
| 1 | Segments, their sales and operating income over the cycle (2018 to 2025) | Item 1 "Business Segments and Products"; Item 7 segment tables; Note 19 | Q1, Q2 (parts), Q3 |
| 2 | The installed base (nearly 24,600 locomotives) and the aftermarket share (about 60% of sales; 58% of Freight) | Item 1 segments, "Competitive Strengths", "Expand high-margin recurring revenue streams" | Q1, Q2 |
| 3 | Customer concentration and negotiating power (top five about 30% of sales) | Item 1 "Customers"; Item 1A "We are dependent upon key customers" | Q2, Q9 |
| 4 | The named competitors (Knorr-Bremse with New York Air Brake, Amsted Rail, Progress Rail of Caterpillar, CRRC, in-house shops) | Item 1 "Competition" | Q2 |
| 5 | Pricing through the last inflation: "Price competition is strong ... has historically limited our ability to increase prices"; gross margin 2020 to 2025 | Item 1A "highly competitive industry", "raw material shortages ... inflationary pressure"; Item 7 Business Update (tariffs, "price escalations and surcharges") | Q2 |
| 6 | Acquisitions and their goodwill (GE Transportation 2019; Inspection Technologies, Frauscher 2025; Dellner 2026) | Item 1 history; Item 7 "Acquisitions"; Item 1A acquisition risks; Note 3 | Q3, Q6, Q7 |
| 7 | Debt, maturities, receivables programme, supply-chain financing, commercial paper | Item 1A "Our indebtedness"; Item 7 Liquidity and Contractual Obligations; 8-K 2026-10-01 | Q9, Q4 |
| 8 | Buybacks and the prices paid | Item 5; financing cash flows; 10-Q Part II Item 2 | Q6 |
| 9 | Restructuring every year (Integration 2.0, 3.0, Portfolio Optimization) | Item 7 Business Update | Q4 |
| 10 | Litigation and investigations (Progress Rail antitrust and false-advertising suit; asbestos; Denver) | Item 3, Note 18; 10-Q Note 14 | Q5, Q9 |
| 11 | Technology change in rail ("rapid changes in technology ... artificial intelligence") | Item 1A | Q1, Q2 |
| 12 | Emerging-market and conflict exposure (Kazakhstan/CIS, Russia, Guinea, India) | Item 1A international risks; Note 19 geography | Q1, Q9 |
| 13 | Backlog ($27.4 billion at 2025 year-end) and its cancellation terms | Item 1 "Backlog" | Q1 |
| 14 | Stock pay, adjusted figures, guidance and the incentive metrics | Note on stock pay; proxy CD&A; 8-K earnings release | Q4, Q5, Q6 |

---
## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the one that reads the price: the stock is bought for what the business will
pay out, "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**, and the quotation
"just tells us prices" **[M2006-077]**; the decision must "scream at you" with a "huge margin of safety" **[M1996-084]**.
No macro view enters: rail volumes, tariffs and rates are read only as properties of the business **[M2000-094]**. Who
is paid to tell me: the company's own releases lead with adjusted figures and raised guidance (line 14), which is the
seller's projection of what it sells, read and not relied on. The analyst's habits govern the record below: "write it
down in the first 30 minutes" **[M1997-127]**; look for "what’s wrong in things" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Item 1A, 10-K FY2025: "Price competition is strong and, coupled with the existence of a number of cost-conscious
   customers with significant negotiating power, has historically limited our ability to increase prices." (against Q2's
   pricing test; written at the first reading of Item 1A).
2. Item 1A: "the global transportation landscape has been characterized by rapid changes in technology"; "The
   advancement of artificial intelligence technologies may significantly accelerate the pace" (against Q1).
3. Item 1A: top customers "could choose to reduce or terminate their relationships"; "the average service life of certain
   products in our end markets has increased ... allowed end users to replace parts less often" (against the aftermarket).
4. Growth bought, not grown: acquisitions of $2,520M in 2025 and $1,062M in the first half of 2026 against owner cash
   of about $1.4 to 1.7 billion a year; goodwill $10,603M and intangibles $4,122M against equity $11,214M at 2026-06-30.
5. 2018 consent decree with the US Department of Justice on a no-poach agreement with Knorr-Bremse, the principal rival
   (FY2018 and FY2020 10-Ks, legal notes). Carried to Q5.
6. Pay: the 2025 bonus was raised from 178.1% to 192.8% of target by a committee adjustment for tariffs (proxy), and the
   long-term plan's return measure is built on "Adjusted EBITDA after tax". Carried to Q4 to Q6.
7. Price: $287.32 against owner cash of about $1.3 to 1.6 billion a year on an enterprise value near $54 billion, a cash
   yield under 3% against a 5.43% long bond (Step 0 arithmetic; to Q7).

## THE STANDING RULE
The run commits no money and no borrowing; any purchase would be made from cash, never on margin, sized so that a fall of
half or more in the quotation cannot force a sale **[M2012-081]**, **[L2023-005]**, **[M2004-065]**. The target's own debt
is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**; the
product need not be understood if "the economic dynamics of the industry" are **[M2011-014]**.

**What the business is (FY2025 10-K, Item 1).** Two segments. Freight (72% of 2025 sales, $8,036M): new and modernized
diesel-electric locomotives, aftermarket parts and services for an installed base of "nearly 24,600 locomotives", freight
car components and brakes, train control and signalling, and since 2025 non-destructive inspection instruments; "approximately
58% of the Freight Segment’s net sales in the aftermarket". Transit (28%, $3,131M): brakes, doors, HVAC, couplers,
pantographs for passenger rail and buses; about 56% aftermarket. Customers are Class I railroads, lessors, car builders,
transit agencies; no customer 10% or more; top five about 30%.

**The parts (Q1's holding-company paragraph, applied through Q2's business-of-parts threshold).** Five-year segment income
from operations 2021 to 2025 (Note 19 of the FY2025 and FY2022 10-Ks): Freight $717M, $864M, $1,065M, $1,422M,
$1,567M = **$5,635M**; Transit $238M, $231M, $295M, $338M, $422M = **$1,524M**. Freight is 78.7% of the segments' total and
**decides**; Transit does not.

**The key variables** **[M1998-044]**, and how predictable each is:
1. The size and use of the North American and world locomotive fleets, which drive parts, overhauls and modernizations
   (about 60% of sales). Locomotives are long-lived and the base is counted in the filing; this moves slowly and is
   foreseeable in direction.
2. Wabtec's place in that base: one of two makers of long-haul freight locomotives in North America (Item 1 names Progress
   Rail as "Our primary competition for locomotives"). Foreseeable: the base it services is already built.
3. New-locomotive and modernization orders, North American and international (the $4.2 billion Kazakhstan agreement, the
   Simandou locomotives for Guinea): lumpy and cyclical; foreseeable as a cycle, not as a year.
4. Freight-car builds (Components) and transit funding (Transit): cyclical, government-driven; foreseeable in range.

**Do the past statements tell me the future ones?** **[M2008-033]** For the deciding part, yes within a range: Freight
segment income rose every year from 2020 ($584M) to 2025 ($1,567M); over 2018 to 2025 the consolidated business never
lost money and its operating margin before amortization of purchased intangibles ran 11.0% (2019, the merger year) to
18.7% (2025). How far off could I be **[M2011-084]**: on the cycle, a good deal (equipment orders, freight-car builds);
on the base and the aftermarket, a narrow range.

**Would the insiders write it down?** **[M2000-105]** They do: the filing cites UNIFE's published forecast of the world
rail market (a 3% compound rate through 2027), and the backlog of $27.4 billion runs years ahead (30% expected in the
next 12 months, Note 2). This is not an industry whose ten-year shape its own people refuse to forecast.

**Technology and change.** The filing's own risk factor (contrary evidence 2) names "rapid changes in technology". Against
it, the product is the diesel-electric locomotive and the air brake, whose customers keep them for decades and whose
base is serviced by the maker; change toward lower-emission and digital products is being offered by Wabtec itself to the
same customers. I read it as slow change, which "can lull you to sleep easier" **[M2014-038]**, not as the fast-moving
technology that puts the economics out of reach **[L1993-023]**, **[M1998-008]**. The customer forecast here is about
railroads and transit agencies keeping and maintaining fleets, which is a forecast about customers more than about
technology **[M2017-019]**, **[M2023-030]**. The Digital Intelligence product line (signalling, software, inspection
instruments) is the part closest to fast change; it sits inside Freight and is not reported as a part with its own
profit, so it is read inside the deciding segment.

**Do I doubt it is inside?** **[M2002-092]** The doubt I find is about the size of the cycle and the international
contracts, not about where the business stands: in ten years Wabtec will in all likelihood still build, rebuild and supply
parts for most of the locomotives of North America and much of the world's freight and transit brakes. The industry is
seen and the company in it is named, not only the industry **[M2012-067]**. "If something’s important but unknowable,
forget it." **[M2006-076]**: the important things here (base, aftermarket, two-maker locomotive market) are knowable from
the filings.

**VERDICT: IN.** The ten-year economics of the deciding part, Freight, can be foreseen in a range from its installed
base, its aftermarket and its place as one of two North American locomotive makers (FY2025 10-K, Item 1 and Note 19,
`0001628280-26-008067`) **[M2012-065]**, **[M2000-037]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

**The parts table** (Q2, a business of parts; Note 19, FY2025 and FY2022 10-Ks):

| Part | Income from operations 2021-2025 | Share of the segments' five-year total | Castle | Decides |
|---|---|---|---|---|
| Freight | $5,635M | 78.7% | standing (below) | **yes** (more than half) |
| Transit | $1,524M | 21.3% | standing but lower-return (margins 9.2% to 13.5% after amortization, 2021-2025); not shown open | no |

The file closes on Freight.

**The castle tests, each with its filing fact (Freight unless said).**
1. *The castle questions, what keeps it standing and how permanent* **[M1995-038]**. The installed base: "nearly 24,600
   locomotives", and "these customers often look to purchase safety- and performance-related replacement parts and
   technology upgrades from the original equipment components supplier" (Item 1, Competitive Strengths); 58% of Freight
   sales are aftermarket. The base is the result of decades of deliveries (GE Transportation's and Wabtec's) and cannot be
   rebuilt quickly by an entrant; it lasts as long as the locomotives, which railroads overhaul and modernize rather than
   scrap (Services product line: "modernizing, rebuilding and overhauling, remanufacturing").
2. *Would it stand without the lord?* The base and the certifications are not a person's; the CEO changed in 2019 (GE
   Transportation's chief became Wabtec's) and the segment's margins rose afterwards. Passes.
3. *The money test* **[M2011-015]**, **[M1997-103]**, **[M2000-077]**. The attacker with money exists: Progress Rail, owned
   by Caterpillar (2025 sales of machinery, power and energy $63,980M; CAT FY2025 10-K `0000018230-26-000008`), has
   competed in North American locomotives for decades and remains "Our primary competition for locomotives" (Item 1). It
   has not displaced Wabtec: its own 2023 suit claimed that Wabtec "has unlawfully monopolized the markets for long-haul
   freight locomotives, Tier IV long-haul freight locomotives and energy management systems" (Note 18, FY2025 10-K; the
   court dismissed the antitrust claims in June 2025 "saying that no harmful effects on competition resulting from the
   merger had been shown"; all claims were settled in February 2026 "without admission of liability", 10-Q Note 14). The
   filing adds a regulatory barrier: certification and testing "that we believe are difficult for new entrants to meet
   cost-effectively" (Item 1). The one-competitor warning applies **[M2012-108]**: one well-funded rival is present, and a
   field of two makers can still be a terrible business **[M2013-052]**; the margins below show it has not been one here.
4. *Pricing power and the agony before a rise* **[M2005-020]**. **Against:** the filer's own words, "Price competition is
   strong ... has historically limited our ability to increase prices" (Item 1A). **For:** through the inflation of 2021 to
   2023 (Item 1A names steel, aluminum, copper, energy, logistics and labor) the gross margin did not fall: 28.3% (2020),
   30.3% (2021), 30.4% (2022), 30.4% (2023), 32.4% (2024), 34.1% (2025) (income statements, FY2022 and FY2025 10-Ks);
   2025 tariffs were met with "price escalations and surcharges" without "a material impact to our results of operations"
   (Item 7). That is the pass-through the rows credit to strong positions **[M2005-017]**. The filing's sentence describes
   a prayer session; the record is of prices that held. Weighed, the record governs, and the sentence is carried as the
   strongest contrary fact.
5. *Would the customer still choose it over the low bid?* Brakes, couplers, train control and locomotives are
   safety-critical, certified and bought on long contracts, the class the rows describe as one "where quality is
   enormously important, where the customers depend very heavily on them, when there’s contracts that extend over many
   years" **[M2016-006]**. The customers are few and strong (top five about 30%), which cuts the other way; the margin
   record says they have not taken the low bid often enough to stop the rise.
6. *Low-cost position.* Not the castle here, and not shown either way from the filings; Wabtec moves work to "best-cost
   locations" (Item 1). Not relied on.
7. *Ask the competitors.* Progress Rail's complaint is the competitor's answer on the public record: it aims at Wabtec's
   locomotive position, which it calls a monopoly (an allegation only; settled without admission).
8. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Widening on the evidence of 2020 to 2025: Freight income from
   operations $584M to $1,567M, segment margin 11.5% to 19.5%; backlog $22.3 billion to $27.4 billion in 2025 and $30.93
   billion at 2026-06-30 (8-K 2026-07-22 release). A change for the better is credited only over a full cycle; the window
   includes the 2020 downturn, in which Freight income fell from $642.9M (2019) to $583.9M (2020), about 9%, with the
   margin at 11.5% against 11.8%.
9. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: (a) a propulsion change (battery,
   hydrogen) won by a newcomer; the filer is itself the developer of these for the same customers; (b) longer service lives
   and fewer active locomotives (Item 1A: end users "replace parts less often"); (c) CRRC and local suppliers abroad
   (Item 1); (d) railroads doing the work in-house (Item 1). None is shown happening in the filings read; (b) is the most
   live and is a reduction, not a breach.

**The competitor row.** The 10-K names Knorr-Bremse with New York Air Brake, Amsted Rail, Progress Rail of Caterpillar and
CRRC; only Caterpillar files with the SEC. **Not SEC filers, flagged: Knorr-Bremse AG (and its subsidiary New York Air
Brake), Amsted Industries/Amsted Rail (private), CRRC Corporation Limited.** Same metric, segment operating profit as a
percent of sales, over the whole span the filings give:

| Year | Wabtec Freight segment (Note 19) | Wabtec consolidated, before amortization of purchased intangibles | Caterpillar segment holding Progress Rail ("Energy & Transportation"; "Power & Energy" from 2025) |
|---|---|---|---|
| 2017 | n/a | 11.8% | 14.7% (`0000018230-20-000056`) |
| 2018 | 18.9% (pre-GE Wabtec) | 11.8% | 17.3% (same) |
| 2019 | 11.8% (GE merged in) | 11.0% | 17.7% (same) |
| 2020 | 11.5% | 13.6% | 13.8% (`0000018230-21-000063`) |
| 2021 | 13.7% | 14.9% | 13.8% (`0000018230-23-000011`) |
| 2022 | 14.4% | 15.6% | 13.9% (same) |
| 2023 | 15.4% | 16.4% | 17.6% (`0000018230-24-000009`) |
| 2024 | 19.0% | 18.4% | 19.9% (`0000018230-26-000008`) |
| 2025 | 19.5% | 18.7% | 19.9% (same) |

Wabtec segment figures are after about $250M to $300M a year of amortization of purchased intangibles from 2019; the
Caterpillar segment is wider than rail (oil and gas, power generation, marine) and reports no rail profit. With those
caveats, the two locomotive makers' businesses earned mid-to-high-teens operating margins across 2017 to 2025, the 2020
trough included. Caterpillar's "Transportation" application sales (marine and rail together) were $4,306M (2021) to
$5,295M (2025) (CAT FY2022 and FY2025 10-Ks), about two-thirds of Wabtec Freight's sales.

**The field's returns over the last full cycle, judged in words.** On the capital the business actually needs
**[M2010-090]**, with goodwill set aside when judging the business **[M2011-060]**, Wabtec earns very high returns: income
from operations before amortization of purchased intangibles against net tangible capital (equity plus debt less cash,
goodwill and intangibles; run.py's ten-year table checked against the filed balance sheets) was about 68% (2019), 73%
(2020), 78% (2021), 79% (2022), 81% (2023), 112% (2024), 114% (2025), pre-tax. On operating tangible capital alone
(receivables, inventory and other current assets less payables, customer deposits and accruals, plus net plant) 2025
gives about 80%. These are not ordinary returns. The returns on what Wabtec *paid* for its businesses are another matter
(about 13% pre-tax in 2025 on capital including goodwill; Q3 and Q6).

**What the field is not.** Not a business whose price a rival sets: the rival's own complaint says the opposite. Not a
business that needs a superstar. Not one where the customer is indifferent: certification and installed-base parts tie
the customer to the maker.

**VERDICT: IN.** The deciding part's castle stands: an installed base of nearly 24,600 locomotives serviced by its maker,
one of two North American locomotive makers, certification barriers, and margins that held through the 2020 downturn and
the 2021-2023 inflation and widened since, against a Caterpillar-backed rival that has not displaced it (FY2025 10-K Item 1,
Item 1A, Note 18, Note 19; CAT 10-Ks as cited) **[M1995-038]**, **[L2007-004]**, **[M2011-015]**, **[M2005-017]**. The
filer's statement that price competition has limited its price rises **[M2005-020]** is the strongest fact against and is
carried to Q7 as uncertainty in the cash, not as a breach.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it has earned on the capital it needs** **[M1998-005]**, **[M2010-090]**: little tangible capital. Net plant
  $1,616M against sales of $11,167M (2025); capital spending $130M to $260M a year (2021-2025) against depreciation of
  $188M to $210M (D&A less amortization of purchased intangibles, cash flow and income statements); working capital
  largely funded by customer deposits ($1,015M at 2025 year-end). Pre-tax returns on net tangible capital of 68% to 114%
  over 2019-2025 (Q2). Read with care **[L1994-009]**: not "a cyclical peak in earnings" (near 70% already in the 2019
  merger year and the 2020 downturn), not "leverage" (the return is computed before interest, on capital including
  debt); the "monopolistic position" in that row is here a two-maker locomotive market, which is the castle of Q2 and is
  read there.
- **To stand still and to grow** **[L1999-024]**, **[M2000-144]**: capital spending ran below depreciation in 2021 and 2022
  and above it in 2024 ($207M against $200M) and 2025 ($260M against $201M). **The maintenance guess, stated:** about the
  depreciation charge, $200M a year **[M1998-127]**, **[L2000-035]**; the excess is growth spending ($59M in 2025). Inventory
  rose $368M in 2022 "ahead of expected growth, in response to supply chain challenges" (FY2022 10-K Item 7) and is the
  main working-capital draw.
- **The growth arithmetic** **[M2003-120]**, **[M1999-067]**: organic sales grew about 8.8% a year from 2021 to 2025 (the
  filer's organic bridges, Item 7 of each 10-K: -0.1% in 2021, +9.7% 2022, +14.4% 2023, +6.8% 2024, +4.5% 2025); net
  tangible capital grew from about $1.3 billion (2019) to $1.8 billion (2025). The business grows without much capital,
  "more and more money every year without putting up anything to get it, or very little" **[M1998-081]**.
- **What the bought growth earned** (goodwill counted, "because we paid for it" **[M2011-060]**): income from operations
  before amortization against total capital including goodwill and intangibles was about 6.5% (2019), 8.4% (2021) and
  13.2% (2025), pre-tax. Acquisitions 2021-2025 cost $3,520M (cash flow statements, net of cash acquired), plus $354M of
  contingent consideration paid to GE for the 2019 deal (2021-2024), and $1,062M more in the first half of 2026
  (Dellner, 10-Q). Inspection Technologies ($1.788 billion) and Frauscher ($792 million) were bought for goodwill and
  intangibles of $1,659M and $761M (Note 3); their earnings are not disclosed ("The pro forma impact ... was not
  significant"). Whether these purchases earn their price is not shown in the filings.
- **WEIGHS FOR** on the business: little capital in, very high returns on it, growth that needs little more
  **[M1998-081]**, **[L2009-012]**. **AGAINST** on the money put into purchases, whose return on their price is ordinary on
  the record so far; carried to Q6.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, 2016 to 2025** **[M2025-032]** (run.py's first-filed table, read against the
filed balance sheets of the FY2025, FY2022, FY2020 and FY2018 10-Ks; $M):

| Year-end | Assets | Equity | Cash | Receivables | Inventory | Goodwill | Intangibles | Debt | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 6,581 | 2,206 | 398 | 668 | 659 | 2,079 | 1,054 | n/t | 2,553 |
| 2017 | 6,580 | 2,809 | 233 | 801 | 743 | 2,460 | 1,204 | n/t | 2,773 |
| 2018 | 8,649 | 2,865 | 2,342 incl. restricted | 801 | 845 | 2,397 | 1,130 | 3,857 | 3,022 |
| 2019 | 18,944 | 9,956 | 604 | 1,150 | 1,773 | 8,361 | 4,104 | 4,429 | 3,267 |
| 2020 | 18,454 | 10,122 | 599 | 969 | 1,642 | 8,485 | 3,869 | 4,239 | 3,589 |
| 2021 | 18,454 | 10,201 | 473 | 1,085 | 1,689 | 8,587 | 3,705 | 4,058 | 4,055 |
| 2022 | 18,516 | 10,102 | 541 | 975 | 2,034 | 8,508 | 3,402 | 4,002 | 4,577 |
| 2023 | 18,988 | 10,487 | 620 | 1,160 | 2,284 | 8,780 | 3,205 | 4,069 | 5,269 |
| 2024 | 18,702 | 10,091 | 715 | 1,152 | 2,314 | 8,710 | 2,934 | 3,980 | 6,185 |
| 2025 | 22,069 | 11,142 | 789 | 1,410 | 2,745 | 10,216 | 3,838 | 5,541 | 3,878 |

(n/t: debt not tagged in the first-filed XBRL for 2016-2017 and not needed for the reading. 2018 cash is the filed
cash, cash equivalents and restricted cash, $2,342.3M, raised ahead of the GE deal; FY2020 10-K cash flow statement.)

**What moved and why.** (1) 2016-2017: Faiveley Transport bought (goodwill $2.1 billion to $2.5 billion). (2) 2018: notes
issued and cash held for the GE Transportation deal. (3) 2019: the GE merger more than doubled assets; goodwill rose to
$8.4 billion and intangibles to $4.1 billion; equity rose from $2.9 billion to $10.0 billion because most of the price
was paid in shares (65.8 million common shares plus convertible preferred to GE and its holders, about 49.2% of the
fully diluted company, and $2.885 billion in cash; FY2020 10-K Note 3). (4) 2020-2024: assets flat near $18.5 billion to
$19.0 billion; intangibles amortized down from $4.1 billion to $2.9 billion; debt flat near $4.0 billion; retained
earnings up $2.9 billion while treasury stock grew by buybacks. (5) 2025: Inspection Technologies and Frauscher added
$1.5 billion of goodwill and $1.1 billion of acquired intangibles (Note 3), financed by debt ($4.0 billion to $5.5 billion); retained
earnings fell $2.3 billion because 55 million treasury shares were retired against it ("any excess over par as a
deduction from retained earnings", Note 2; equity statement $3,304M), an accounting entry with no cash. (6) Inventory
against sales: 21.6% (2019), 21.7% (2020), 21.6% (2021), 24.3% (2022), 23.6% (2023), 22.3% (2024), 24.6% (2025); the two
rises are explained by the filer (2022 build "ahead of expected growth", 2025 acquired inventory of $192M and tariffs),
and customer deposits rose with them ($693M to $1,015M in 2025). Billed receivables 11% to 14% of sales throughout. No
prepaid or deferred account building **[M1995-064]**: other current assets $263M (2.4% of sales); deferred pre-production
costs fell from $52M to $42M (Note 2).

**What the figures don't say.** (a) Before 2025, receivables sold under the revolving programme were in operating cash;
outstanding sold balances were small ($20M at 2021, $80M at 2022, $20M at 2023, nil at 2024; net remittances of $60M and
$20M in 2023 and 2024, FY2022 and FY2025 10-Ks, Note 2), so operating cash was not flattered by more than tens of
millions in any year. From 2025 the programme is a borrowing. (b) Supply-chain financing covers $285M of payables on
terms of "net 30 and net 180 days" (Note 2); payables are flat against sales, so no stretch is shown. (c) "Below market
intangible amortization" ($88M in 2020 falling to $44M in 2025) is non-cash income from contracts acquired below market
in the GE deal; operating cash excludes it, and so does owner cash below.

**The real costs.** Depreciation is charged and capital spending runs about at it **[L2015-004]**. Stock pay is counted at
the cash-flow add-back (Step 0) **[L2021-003]**, **[L2015-003]**. Amortization of purchased intangibles ($300M in 2025)
arises from purchase accounting on customer relationships, technology and backlog, the kind the rows add back
**[M1997-015]**, **[L2012-003]**; owner cash below is built from operating cash, which never deducted it. Restructuring is
recurring, $65M (2024) and $75M (2025), under Integration 2.0, Integration 3.0 and Portfolio Optimization, with $125M to
$155M more planned for Integration 3.0 (Item 7); it is a real and repeated cost **[L2016-007]** and owner cash bears it.

**EBITDA and the adjusted figures in the filer's own mouth.** The second-quarter release (8-K 2026-07-22) leads with
adjusted EPS beside GAAP EPS, "Announces Increase to Full-Year Revenue & Adjusted EPS Guidance", and reconciles "EBITDA"
and "Adjusted EBITDA"; the proxy's long-term incentive measures return on "Adjusted EBITDA after tax", and the annual
bonus pays on adjusted EPS, which removes "non-cash amortization expense and certain restructuring costs" (proxy, EBIT
margin definition). These weigh against **[L2016-006]**, **[L2019-006]**, **[M1998-086]**: they are things done "in
public in relation to their investors and the promises they make" **[M2004-067]**, and under the framework's Q4 convention
they are recorded here as a WEIGHING and carried to Q5 (judged there) and Q6 (pay). They are not suspicion raised by the
statements themselves: the 10-K's statements are GAAP throughout and the adjusted figures are reconciled in the release.

**Confusion?** None found. Revenue over time on long contracts uses the input method with loss provisions (Note 2), which
is a known judgment area **[M1995-065]**; nothing in the balance-sheet series, the reserves (warranty $248M to $266M) or
the notes reads as games. The accounts can be understood **[M1995-063]**, **[M2003-029]**.

**VERDICT on the accounts: IN** (no confusion, no suspicion raised by the statements); **WEIGHS AGAINST** on the featured
adjusted EPS, the EBITDA reconciliations and the guidance habit, carried to Q5 **[M1994-018]**, **[L2016-006]**. The recast
owner cash feeds Q7: operating cash less the stock-pay add-back less maintenance (depreciation) or all capital spending,
plus interest after the company's tax for the all-equity basis.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**Who.** Rafael Santana, President and CEO since July 2019 (before that CEO of GE Transportation from November 2017; at GE
from 2000), and Chairman as well from the 2026 annual meeting (10-Q Part II Item 5 calls him "Chairman and Chief
Executive Officer"; the proxy letter is the outgoing chairman's "final meeting as Chairman"). Most of the operating
officers came from GE Transportation (FY2025 10-K, executive officers). CFO John Olin since 2021 (from Harley-Davidson).
Albert Neupaver, "Chairman or Executive Chairman of the Board of Wabtec since May 2014", retires from the board at the
2026 meeting (proxy).

**First yardstick, the record against the hand dealt** **[M1994-008]**: dealt a newly merged GE Transportation in 2019
and a 2020 downturn, the present management took the margin before amortization from 11.0% (2019) to 18.7% (2025) and
Freight income from $642.9M to $1,567M, against a Caterpillar segment that went from 17.7% to 19.9% in the same years
(Q2 table); organic growth in four of five years; backlog to a record. The capital half of the record is Q6's.

**Second yardstick, how they treat the owners** **[M1994-009]**: the proxy (Q6, Part B): CEO pay of $26.2M (2025),
$21.0M (2024), $15.5M (2023); a bonus raised by committee adjustment; directors' holdings largely granted. Weighed at Q6.

**The integrity record, as found in the filings read** (operator rule 2: facts first):
1. **The 2018 no-poach consent decree.** "On April 3, 2018, the Company and Knorr-Bremse AG entered into a consent decree
   with the United States Department of Justice resolving allegations that the Company and Knorr-Bremse AG had maintained
   unlawful agreements not to compete for each other’s employees. The allegations also related to Faiveley Transport ...
   No monetary fines or penalties were imposed on the Company. The Company elected to settle this matter with the
   Department of Justice to avoid the cost and distraction of litigation." Class actions by employees followed (FY2020
   10-K legal note, `0001628280-21-002557`; FY2018 10-K `0001628280-19-002095`). This is conduct with the principal rival
   that a front-page story would not flatter **[M2016-033]**. It predates the present CEO (the decree was entered ten
   months before the GE merger closed); the chairman of that era chaired the board until 2026.
2. **Antitrust claims by rivals.** Siemens counterclaimed in 2018 "alleging violations of federal antitrust and state trade
   practices laws related to Wabtec’s PTC sales" (FY2018 10-K); no later filing read reports a finding. Progress Rail's 2023
   suit (antitrust, breach of contract, unfair competition, defamation, false advertising): antitrust claims dismissed
   June 2025; all claims settled February 2026 "without admission of liability by the Company" (10-Q Note 14).
3. **Carried from Q4:** adjusted EPS featured and guided, raised mid-year in 2026; EBITDA reconciled in releases.
   The record read does not show a habit of always hitting declared targets **[L2002-041]**: one release and one proxy
   year were read (2025 adjusted EPS $9.16 against a bonus target of $8.55 and a maximum of $9.83).
4. **No restatement, no material weakness, no SEC enforcement action** reported in the legal notes of the FY2018, FY2020,
   FY2022 and FY2025 10-Ks or the latest 10-Q; the 2022 cyber incident was disclosed in the 10-K (FY2022 Item 1A).
5. **Insider conduct:** the CEO's 10b5-1 plan covers "up to 13,053 shares" (10-Q Part II Item 5) against 120,547 shares
   beneficially owned (proxy); small.

**Reading it.** Integrity is applied on doubt alone: "If you’ve got doubts, forget it." **[M2013-088]**; "we wouldn’t hire
anybody, no matter how able, if we didn’t trust them" **[M2015-047]**. The doubt the record raises attaches to the
pre-2019 leadership and its culture (fact 1): an agreement with the main rival not to hire each other's people is the
kind of conduct the front-page test condemns **[M2016-033]**, and "everybody mouths the integrity, even when it’s lacking"
**[M2010-069]**. Against reading it into the present management: the people who run the business now are, by the 10-K's
list, mostly not those people; the chairman of that era leaves the board in 2026; the rows ask for "evidence of behavior
in front of us" **[M1998-166]** and say "people leave track records" **[M1998-168]**, and the track record of the present
CEO in the filings read (2019-2026) carries no enforcement, restatement or finding. The habits carried from Q4 are the
ordinary corporate ones, adjusted figures reconciled to GAAP and annual guidance; they weigh against **[L2016-006]**,
**[L2019-006]**, and read with the rest they do not amount to doubt about honesty. My judgment: no doubt about the honesty
of the present managers on this record; the decree is the strongest integrity fact found and is written down for any
later reader.

**Ability.** The record against the hand dealt weighs FOR **[M1994-008]**: margins up, organic growth, an integration that
worked on the evidence of the segment figures. The business does not need a genius **[M1996-037]** (Q2 test 2).

**VERDICT on integrity: IN** (no doubt about the present managers on the filings read; the 2018 no-poach decree of the
earlier leadership recorded as the strongest fact against) **[M2013-088]**, **[M1998-168]**. **Ability WEIGHS FOR**
**[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**, **[R2009-002]**. 2021-2025: net income attributable $4,232M
  ($558M, $633M, $815M, $1,056M, $1,170M), dividends $639M, so $3,593M kept; buybacks returned $2,502M of it. The market
  leg: the 10-K's total-return graph runs from $100 at 2020-12-31 to $299.81 at 2025-12-31 (Item 5), while the share
  count fell; market value per dollar kept passes by a wide margin. The value leg: owner cash before interest
  (maintenance basis) rose from $959M (2021) to $1,645M (2025) (Q7 script), with about $3.8 billion of purchases funded on
  the way. **Weighs FOR** on the retention test as the rows state it.
- **Buybacks** **[L1999-023]**, **[L2016-002]**, **[L2011-003]**, **[M1996-013]**. The programme names no price: "No time limit
  was set ... The Company may repurchase shares in the future at any time, depending upon market conditions" (Item 5).
  Under the framework's convention it weighs against unless the prices paid sit at or below the bottom of the Q7 range,
  **$104.21 a share** (all-equity, central; Q7 below). Average prices paid (equity statements and Item 5): 2020 $66.8
  ($207M / 3.1M shares), 2021 $90.9, 2022 $94.6, 2023 $105.6, 2024 $160.4 ($1,107M / 6.9M), 2025 $203.6, first half of
  2026 about $256 ($461M / 1.8M; second quarter $263.08 filed). The purchases of 2020 to 2023 sat at or below today's
  bottom (whose earlier equivalents were lower, the business then being smaller); the $1.79 billion spent from 2024 to
  mid-2026 was paid at 54% to about 150% above it. **Weighs AGAINST.**
- **Issuance and deals** **[L2014-012]**, **[M2007-123]**, **[L2009-019]**. The 2019 GE Transportation deal was paid
  chiefly in shares (65.8M common shares to GE and its holders plus convertible preferred, "approximately 49.2% of the
  outstanding shares", and $2.885 billion cash; FY2020 10-K Note 3), so by the framework's usage it is a merger, before the
  window. It was not "an all-stock deal", so Q6's one STOP does not apply; whether the shares given were worth less than
  the business received cannot be settled from the filings read and is left UNDECIDED. Since then the share count has
  fallen; the company is not "hell-bent on issuing shares" **[L2014-015]**. The cash deals: $3.6 billion for Inspection
  Technologies, Frauscher and Dellner in eight months (2025-2026), mostly goodwill and intangibles, with no disclosed
  earnings, and a stated strategy "to continue to pursue strategic acquisitions" (Item 1) with synergies counted in
  advance (Item 1A) against "we never count on synergies" **[L2016-008]**; the forces that "push toward deals" **[M2014-076]**
  are visible. **Weighs AGAINST.**
- **Dividends**: $1.00 a share in 2025, rising each year; "currently at a rate of approximately $212 million annually"
  (Item 5), about 18% of 2025 net income. Clear and consistent **[L2012-015]**. Neutral.

### Part B: the pay, the board and the owners
- **The pay** (proxy, `0001628280-26-022197`): CEO total $26.2M (2025), $21.0M (2024), $15.5M (2023). The bonus pays on
  adjusted EPS (amortization and restructuring removed) and cash conversion; for 2025 "the Compensation and Talent
  Management Committee determined that a partial impact of tariff-related headwinds should be considered in calculating
  financial performance", which "increased annual incentive payouts for the named executive officers from 178.1% to
  192.8%": an adjustment in the managers' favour after the year, the shape of plans that "payoff no matter what happens"
  **[M1999-018]** and of "heads I win, tails you lose" **[L1994-020]**. The long-term plan pays on three-year ROIC defined as
  "Adjusted EBITDA after tax, divided by ... net debt plus stockholders’ equity" and on operating cash, with a relative
  shareholder-return modifier of plus or minus 20%: the denominator charges the managers for goodwill, which is to their
  credit **[M2011-060]**, but the numerator is a figure before depreciation **[M1998-086]**, and the modifier ties pay to the
  stock price, which the managers do not control **[L1996-018]**, **[L1997-022]**. Restricted stock vests by time over
  three years. **Weighs AGAINST.**
- **The board.** Nine members; from 2026 the CEO is also Chairman, with a Lead Independent Director **[L2014-026]**.
  Directors' holdings are small and largely granted (953 restricted shares a year each; holdings of 1,246 to 24,841 shares
  for the non-employee directors other than the retiring chairman's 605,402) **[L2019-008]**, **[M2017-053]**. **Weighs
  AGAINST.**
- **The owners as partners.** Candour: the 10-K is plain and complete on segments, organic growth, acquisitions and
  litigation **[M1998-036]**; the releases lead with adjusted figures and guidance **[L2019-006]**. Mixed.
- **WEIGHS:** Part A **AGAINST** on balance (retention passes on the market leg; buybacks at prices well above the bottom
  of the range and goodwill-heavy purchases weigh against); Part B **AGAINST** (pay adjusted upward, an EBITDA-based return
  measure, a stock-price modifier, a combined chair).

## Q7 — WHAT IS IT WORTH? STOP.
The definition: "the discounted value of the cash that can be taken out of a business during its remaining life"
**[R1996-018]**, credited only with "whatever net cash is left every year" **[M1998-080]**, at the long government rate
**[L2000-021]**, **[M1996-025]**, held as a range **[L2000-024]**. Arithmetic: `Test Runs/_research 2026-10-16 WAB/q7.py`,
output in `q7_output.txt` beside it.

**Owner cash, recast (Q4), $M** (cash flow statements; interest after the company's own effective tax, 23.3% to 25.7%):

| | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year average |
|---|---|---|---|---|---|---|
| Operating cash | 1,073 | 1,038 | 1,201 | 1,834 | 1,759 | |
| less stock pay (cash-flow add-back) | 46 | 41 | 47 | 66 | 80 | |
| less maintenance = depreciation (D&A less amortization) | 204 | 188 | 210 | 200 | 201 | |
| plus interest after tax (all-equity basis) | 135.7 | 139.6 | 164.7 | 152.1 | 167.2 | 151.9 |
| **Owner cash before interest, maintenance basis (central)** | **958.7** | **948.6** | **1,108.7** | **1,720.1** | **1,645.2** | **1,276.3** |
| Same, all capital spending deducted (beside) | 1,032.7 | 987.6 | 1,132.7 | 1,713.1 | 1,586.2 | 1,290.5 |
| Net purchases of businesses (acquisitions net of cash, less dispositions and the 2025 FX settlement, plus contingent consideration to GE) | 534 | 190 | 420 | 191 | 2,492 | 765.4 |

**The specifics, in order.**
- **(a) Cycles.** No end year of the window is described by the filer as aberrational for cash; 2021 and 2022 owner cash
  are alike ($959M, $949M) and 2025 is below 2024. The literal window is the base, and is the figure shown.
- **(b) Decline.** Not applicable; growth is positive.
- **(c) Acquisitions.** Net purchases over the window, $3,827M, exceed half of owner cash before purchases ($6,452M on the
  all-equity basis; $5,693M after interest): **the serial acquirer**, so the central figure is the **organic pair**
  (purchases left out, organic growth as the filer reports it, 8.78% a year 2021 to 2025, compounded from the filer's
  organic sales bridges), with the default pair beside. Inspection Technologies and Frauscher, bought inside the window,
  are in the base for six months and one month; Dellner, closed 2026-02-10 after the window, is credited at nothing (no
  earnings filed: "The pro forma impact ... was not significant", 10-Q) and its financing is in the net debt below. All
  three prices are therefore in net debt while little of their earnings is in the base; that biases the range down, and it
  is the convention's treatment, stated.
- **(d) Working capital** is inside operating cash.
- **(e) Growth spending.** The maintenance guess is the depreciation charge (Q3) **[M2000-144]**, **[M1998-127]**; the
  maintenance case is central and the all-spending case beside. They differ little, because capital spending ran close to
  depreciation over the window.
- **(f) The cap.** 8.78% carried ten years leaves owner cash at 13.5% of sales (sales at the same organic rate) against the
  highest share the filings show, 16.6% (2024): no cut. After year ten, zero growth **[M1997-095]**. In the default pair the
  total growth of owner cash, 14.45% a year, would carry owner cash to 21.3% of sales: cut to the business's own sales
  growth, 9.31% a year **[M1999-067]**.

**Net debt and shares.** Debt at 2026-06-30, $1,656M current plus $4,915M long-term, less cash, equivalents and restricted
cash of $670M: **$5,901M** (10-Q balance sheet; no finance leases are reported; operating leases, present value $392M at
2025 year-end, left out and said so; the 2026-10-01 commercial paper programme had issued nothing). Shares 168.911M
(Step 0). Market value $48,532M; enterprise value $54,433M. Non-controlling interest $30M, not deducted (immaterial).

**COMPUTATION, the range at the long rate (5.43%), all-equity, per share:**

| Case | No growth (bottom) | Growth carried ten years, then none (top) | Expected return at the price |
|---|---|---|---|
| **Organic pair, maintenance case (central)** | **$104.21** | **$245.51** | 2.34% / 4.80% |
| Organic pair, all spending (beside) | $105.76 | $248.63 | 2.37% / 4.84% |
| Default pair (purchases deducted, growth cut to 9.31%; purchases stop after year ten) | $104.21 | $201.86 | 2.34% / 4.28% |
| Equity-only (owner cash after interest $1,124.4M, against market value) | $122.59 | $247.07 | 2.32% / 4.74% |

The literal five-year window is the central base; no cycle base differs from it. Width of the central range 2.36 to 1.

**The floor, tested first** **[M2003-149]**: about ten percent, applied to owner cash after the company's own tax (Q7, Whose
tax), on the all-equity basis **[L2017-004]**. At $287.32 the expected return is 2.34% on the no-growth case and 4.80% on
the growth case: **no case in the range earns the floor**, and none comes within half of it. For ten percent at today's
enterprise value, owner cash would have to start near $2,965M and grow at the organic rate for ten years, against the
five-year average of $1,276M (q7.py). Even crediting Inspection Technologies, Frauscher and Dellner, bought for about
$3.6 billion, with a full year each, they would have to add some $1.7 billion of owner cash a year, about half their
combined price, for the floor to be reached. The price is also above the top of every range ($245.51 central), which
closes OUT through the floor convention. "there’s just a point at which we drop out of the game" **[M2003-149]**; a bond
at 5.43% beats every case **[M2007-095]**.

**Q6's buyback line**, written back: the bottom of the central range is $104.21 a share; the prices paid since 2024 sat
well above it (Q6, Part A).

- **Value range (COMPUTATION, NOT A CLEARANCE):** **$104.21 to $245.51** a share (all-equity, organic pair, maintenance
  case, 5.43%) against **$287.32**.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$72.20** a share, all-equity central (each end case
  valued at ten percent, $12,763M and $23,431M, averaged, less net debt of $5,901M, over 168.911M shares), owner cash after
  the company's own tax, no conversion. **Equity-only figure beside: $94.39.** (All-spending case beside: $73.40; default
  pair beside: $52.92.) No cheap price is reported.
- **VERDICT: OUT.** No case of the range earns the floor of about ten percent at $287.32 (expected return 2.3% to 4.8%),
  and the price sits above the top of the range; the floor is tested before the width **[M2003-149]**, **[M2009-005]**,
  **[L2013-012]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not chosen by the operator; and the file closed at Q7).

---
## THE BOX
**OUT at Q7.** The castle stands (Q1 IN, Q2 IN on the Freight segment's installed base and two-maker locomotive market;
Q4 IN; Q5 integrity IN), but at $287.32 no case of the range earns the floor of about ten percent: COMPUTATION range
**$104.21 to $245.51** a share (all-equity, organic pair, maintenance case, 5.43%) against **$287.32**; expected return
2.3% to 4.8%; fair price $72.20 all-equity ($94.39 equity-only). Re-look under an alert like any OUT (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged, operator rule 2.)* **[M1997-127]**
- **Q9, debt and sudden demands.** Debt $6,571M gross at 2026-06-30 ($1,656M current) against cash of $670M (10-Q).
  Scheduled principal at 2025 year-end: $1,250M in 2026, $1,840M in 2027-28, $1,227M in 2029-30, $1,250M later (FY2025
  10-K, contractual obligations). Covenants: interest coverage at least 3.0 and net leverage at most 3.5 on a defined
  earnings metric (Item 1A). Income from operations $1,793M against net interest $225M in 2025, about 8 times. Liquidity
  $3,207M at 2025 year-end ($2.0 billion revolver, $443M receivables programme, cash). A commercial paper programme of
  up to $2.0 billion with maturities "up to 397 days" was established 2026-10-01, nothing issued (8-K
  `0000943452-26-000013`): short-term maturities of size if used. Bank guarantees and letters of credit of $1,141M
  supporting customer contracts (Item 7). Ratings BBB / Baa2 / BBB, stable.
- **Q9, exposures.** Asbestos claims, mostly insured or indemnified, "cannot be estimated" (Note 18); warranty reserve
  $266M current; sales in Kazakhstan/CIS $431M (2025) with Russia-related sanctions and nationalization risk named
  (Item 1A, Note 19); the $4.2 billion Kazakhstan locomotive agreement (Item 7); about half of sales outside the US.
- **Q8 and Q10.** The 30-year Treasury at 5.43% exceeds every expected return computed at the price (2.3% to 4.8%).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `310039c4`); written question by question; committed after each
      (Q1 `697d60b7`, Q2 `ddb6f7e8`, Q3-Q4 `7c47fef1`, Q5 `3a8a35e9`, Q6-Q7 `aee534f1`). Q3 and Q4 were committed together,
      a lapse from one commit per question, said here.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatcher's and was not touched;
      the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under Contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
      (`check_ids.py` in the research folder, PASS); every filing fact carries its accession or names the filing whose
      accession is in Step 0; no number without a filing or a CONVENTION.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8, Q9, Q10 and Q12 are NOT REACHED and nothing
      after Q7 is a clearance. Q6's buyback line uses the bottom of Q7's range and was committed with Q7.
- [x] Owner cash is operating cash less stock pay less capital spending (or the depreciation maintenance guess), never a
      net-income proxy (operator rule 5); the sovereign is the Treasury's own curve; the price is an aggregator quote,
      flagged.
- [x] Contrary evidence written down as found (Foundations, items 1 to 7); the facts found for unreached questions are
      under AFTER THE STOP; Q5 was reached, so no integrity flag is needed in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its stock-pay line was replaced by the cash-flow add-back and
      said so (Step 0).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded at the foot of this file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **EBITDA talk: STOP or weighing?** Q4's "Why confusion is a STOP" states the EBITDA count as a stop ("the number of
times we’re going to buy into a company [...] where people are talking about EBITDA, is going to be about zero"
**[M2002-026]**) and Q4's OUT list names "EBITDA as earnings and managements that talk it", while the 2026-10-06 convention
puts Q4's STOP on the accounts and sends an adjusted figure featured in place of GAAP to Q5 as a weighing. Wabtec
reconciles EBITDA in its releases and pays its managers on an EBITDA-based return, but does not present EBITDA as
earnings in its filed statements. I treated it as a weighing carried to Q5 and Q6; the text should say which applies when a
company reports EBITDA in releases and pay plans but not in its accounts. (2) **The serial-acquirer test's "owner cash
before purchases"** does not say whether it is before or after interest; the test was met on both, so nothing turned on
it. (3) **The organic pair and purchases made late in the window.** When the window's largest purchases close in its last
six months (and one more just after it), the organic pair puts their whole price into net debt and almost none of their
earnings into the base. The convention credits them "at nothing where no earnings are filed", which here is because the
filer calls their pro forma effect "not significant"; the text could say whether a disclosed purchase price with no
disclosed earnings should be treated the same way as a deal with no filed record at all. The floor failed by so wide a
margin that nothing turned on it. (4) **The bottom of the range for past buybacks** is computed on today's figures; the
buyback convention does not say whether prices paid years ago are read against today's bottom or the bottom as it would
have stood then. I read them against today's and noted that earlier bottoms would have been lower.


---
**Checks, 2026-10-16:** `python tools/check_framework.py` PASS (v5 ledger 4,280 rows verbatim; test runs phantom in 0 files; pointers 0 missing; v5 scope OK). `python -I "Test Runs/_research 2026-10-16 WAB/check_ids.py"` PASS (no E-ids; every M/L/R id in the v5 ledger; 28 quoted fragments placed before an id each found in that row).
