# Company Run: Illinois Tool Works Inc. (NYSE: ITW), 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch** (the
copy and the empty research folder were made before the first EDGAR or price call of this run).

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md`, slots filled by the dispatcher's message of 2026-10-07.
Research folder: `Test Runs/_research 2026-10-07 ITW/` (raw filings under `cache/`, gitignored; `fetch.py`, `check_ids.py`
and `row.py` are this run's own scripts). The lock in `Screens/_daily/` was present when this run started, held by the
dispatching session ("interactive v5 re-runs batch 6", 2026-10-07 12:43).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared before any verdict (the blind rule).** Seen by accident and not used: (1) the session's opening
git status listed other companies' research folders by ticker (among them AYI, ARCB, BDC, CHD) and recent commit subjects
naming other runs and their boxes (ESI, HAS, GFF, GRMN); none is about ITW. (2) The lock file's text says this batch is
"v5 re-runs", which with the brief's own words ("there are earlier ones") tells me ITW has been run before under some
earlier edition; I do not know the box of any earlier run and did not look. (3) The session's memory index carries lines
on the queue and on holding reviews owed in general; it names no ITW position and I learned nothing about whether anyone
holds this name. No `Test Runs/` file other than this one and the template was opened, listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $261.94 (quote of 2026-10-07 from `tools/sources.py price()`, an aggregator, live quote only, flagged per
  operator rule 5; not a filed figure).
- **Shares by class** from the latest filing's cover: one class of common stock, **284.8 million** outstanding at
  June 30, 2026 (10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0000049826-26-000049`;
  `python Screens/cover_shares.py ITW` returns 284,800,000). Cross-checked: the 10-Q balance sheet gives issued 550.0
  million, outstanding 284.8 million, treasury stock carried at $28,004 million. The cover gives the count at the quarter
  end, not at a later date; the company bought 2.9 million shares in the second quarter of 2026 for about $750 million
  (same 10-Q, MD&A), so the count today is probably a little lower. No 8-K or prospectus after the 10-Q states a share
  count (8-Ks read: 2026-08-13 note issue, accession `0001193125-26-349149`; 2026-07-28 results, `0000049826-26-000047`;
  2026-05-22 officer change, `0000049826-26-000033`; 2026-02-23 credit agreement, `0001193125-26-061771`).
- **Market cap:** 284.8M x $261.94 = **$74,601M**.
- **Net debt at the latest filed date (2026-06-30, 10-Q `0000049826-26-000049`):** short-term debt $3,145M plus long-term
  debt $6,549M less cash $839M = **$8,855M**; operating leases ($242M at 2025-12-31, 10-K note 9) left out and said so.
  Subsequent event stated: the $1.5 billion 4.650% notes due 2029 issued 2026-08-13 (8-K `0001193125-26-349149`), whose
  proceeds the filing says repay commercial paper; it changes the mix of the debt, not its sum, so nothing is added.
  Enterprise value at the price: $74,601M + $8,855M = **$83,456M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, dated 10/06/2026
  (`python tools/sources.py`, the issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-13, accession `0000049826-26-000008`; 10-Q for the
  quarter ended 2026-06-30, filed 2026-08-06, accession `0000049826-26-000049`; proxy (DEF 14A) filed 2026-03-27,
  accession `0001193125-26-127599`; the four 8-Ks above; and the earlier 10-Ks named at each question. **One figure
  cross-checked against the filed statement:** net cash provided by operating activities FY2025 $3,126M in the 10-K's
  Statement of Cash Flows (`0000049826-26-000008`) equals the XBRL value `tools/run.py` printed (3,126); capital spending
  $419M and stock-based compensation $69M likewise agree.
- `python tools/run.py ITW` arithmetic lines only (read for its numbers, nothing it prints as a rule): OCF less stock pay
  less capital spending FY2023 $3,015M, FY2024 $2,783M, FY2025 $2,638M; the five-year window FY2021 to FY2025 averages
  $2,503M on the capital-spending basis and $2,617M on the depreciation basis; stock pay is in the cash-flow statement
  each year (FY2025 $69M) and is deducted; no securities, software or other spending lines inside operating cash were
  found by the tool. The full owner-cash recast is at Q4.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is a share is a business: the question is whether I would be content to own ITW "if
the market closed for five years" **[M1997-109]**, which turns the run onto the seven businesses and what they earn, not
onto the quotation. The market serves and does not instruct: "It just tells us prices." **[M2006-077]**; a price of
$261.94 is a fact to set against the value at Q7, not a verdict. Margin of safety is the attitude the value question
must keep: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. The
analyst's habits apply because this is a famous, admired company whose own filings call its model "powerful and highly
differentiated"; that is the seller's description, and "don’t ask the barber whether you need a haircut" **[M2011-083]**.
No macro view enters. **Contrary evidence, written down as found** **[M1997-127]**:
- (1) Organic revenue has been flat to down for three years: the FY2025 10-K gives -0.7% for FY2024 and flat for FY2025,
  while operating margin rose; the earnings growth of these years is margin and buybacks, not volume (10-K
  `0000049826-26-000008`, MD&A).
- (2) Stockholders' equity is $3,226M against retained earnings of $30,150M and treasury stock of $26,875M (FY2025 10-K
  balance sheet); goodwill and intangibles ($5,689M) exceed equity. The high returns on equity are partly made by
  shrinking equity, which Q3 must read with care.
- (3) Total debt rose from $7,829M (2016) to $8,969M (2025) and $9,694M (2026-06-30) while the company paid out more in
  dividends and buybacks ($3,285M in FY2025) than its free cash flow ($2,707M); the gap is borrowed.
- (4) The company features non-GAAP figures (free cash flow, after-tax ROIC with discrete tax items removed, total debt
  to EBITDA) and states long-term performance targets (risk factor, 10-K Item 1A): carried to Q4 and Q5.
- (5) Construction Products organic revenue fell 6.1% (FY2024) and 5.1% (FY2025); Test & Measurement organic revenue
  fell in both years, and the 10-K blames lower demand in the MTS Test & Simulation business for FY2025.

## THE STANDING RULE
The buyer's conduct, not the target's: a part-interest bought in the market with cash, unlevered, puts nothing the buyer
has and needs at risk, "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; bought on margin it would breach the rule, "borrowed money has no place in the investor's tool kit"
**[L2014-005]**. Nothing in this run assumes borrowed money. Passes for an unlevered buyer.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** "can I understand it?" **[M1995-051]**, where understanding is "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" **[M2012-065]**. Knowing the chemistry of an adhesive
or the metallurgy of a weld is not the test; "What is important is that I understand the economic dynamics of the
industry." **[M2011-014]**.

**What the business is, from the filing** (10-K FY2025, `0000049826-26-000008`, Item 1): 88 divisions in 49 countries,
about 43,000 people, seven reported segments, products sold "directly to industrial manufacturers and through independent
distributors"; backlog "generally is not considered a significant factor" because delivery periods are short; no customer
above 5% of revenue; raw materials (steel, resins, chemicals) "available from numerous commercial sources"; about 21,800
granted and pending patents, none individually material; legal proceedings "None". Over half of sales are outside the
United States. The products are fasteners and plastic components for cars, commercial kitchen equipment and its service
(Hobart), materials-testing machines and their consumables (Instron, MTS, Buehler) and electronics-assembly and
clean-room consumables, arc welding machines and wire (Miller, Hobart Brothers), adhesives, lubricants and car-care
fluids (Permatex, Rain-X), nails, anchors and nailers for builders (Paslode), and a miscellany of packaging, marking,
appliance and ground-support products (Hi-Cone).

**The parts, and which decides (Q1's holding-company paragraph, extended to segments, read with Q2's business of
parts).** Share of the five-year (2021 to 2025) total of segment operating income, from the segment notes of the FY2022
10-K (`0000049826-23-000008`) and the FY2025 10-K (`0000049826-26-000008`); computed in `segments.py`:

| Segment | 2021-2025 operating income, $M | Share |
|---|---|---|
| Test & Measurement and Electronics | 3,410 | 16.9% |
| Food Equipment | 3,272 | 16.2% |
| Automotive OEM | 2,923 | 14.5% |
| Welding | 2,896 | 14.4% |
| Construction Products | 2,765 | 13.7% |
| Specialty Products | 2,515 | 12.5% |
| Polymers & Fluids | 2,395 | 11.9% |
| Total segments | 20,176 | 100% |

No part carries half; by the CONVENTION the largest part decides, which is Test & Measurement and Electronics, ahead of
Food Equipment by 0.7 points. Every part is read below, since the margin between the largest and the next is a rounding
difference (see "What in the framework was wrong or unclear").

**The tests.**
1. *Key variables and their predictability* ("trying to identify the key variables in that particular business, and
   evaluating how predictable they were first" **[M1998-044]**). For every segment the variables are the same three:
   unit demand in the end market (auto builds, restaurant and institutional kitchen spending, industrial and laboratory
   capital spending, fabrication and construction activity), the price set against steel, resin and labour costs (the
   filer reports "price/cost" every year in every segment), and the cost structure ITW's own operating method sets. The
   first is cyclical but not mysterious: the 2020 drop (organic revenue -9.8%, FY2020 10-K `0000049826-21-000007`) and
   the recovery (+12.3% in 2021, FY2021 10-K `0000049826-22-000006`; +12.1% in 2022, FY2023 10-K
   `0000049826-24-000008`) are the shape of an industrial cycle, not of a field being remade.
2. *Do the past statements tell the future ones?* ("do I understand enough about this business so that the financial
   statements will tell me the information that’s useful to me" **[M2008-033]**). The same seven segments have been
   reported on the same basis since the FY2014 10-K (`0000049826-15-000016`), fourteen years of revenue and operating
   income per part, with the drivers of each year's margin itemised. That is unusually legible.
3. *Is the deciding question important and knowable?* **[M2006-076]**. Yes: whether the margin and the capital needs of
   these product lines hold is knowable from the record and from the rivals' filings, which Q2 reads.
4. *How far off could I be?* ("some model in our mind of how far off we can be" **[M2011-084]**). Revenue can fall a
   tenth in a bad year; the range of outcomes over ten years is a range of volume and margin, not of survival.
5. *Change.* "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on
   that." **[M1999-063]**; technology that "could hurt the business as it presently exists" "won’t make it through the
   filter" **[M1998-008]**. Two places carry real technology exposure. (a) The deciding part, Test & Measurement and
   Electronics: test machines, software and consumables for materials and structures, plus equipment and consumables
   for electronics assembly and semiconductors (10-K Item 1). Testing a material to a standard is old and slow to change;
   the electronics half rides the semiconductor and electronics capital cycle (FY2024 electronics assembly organic
   revenue -11.1%, FY2025 10-K MD&A) and is the part of ITW where product generations turn fastest. Its own record shows
   the segment margin moving from 14.9% (2012) to between 24.2% and 27.4% in every year 2019 to 2025 (`segments.py`),
   through the 2020 collapse and the 2021 acquisition of MTS Test & Simulation; a business remade by technology does not
   usually hold its margin so steadily. (b) Automotive OEM, through electric vehicles: the 10-K reports content gains with
   Chinese makers and growth "in the electric vehicles market"; the fastener and plastic-component content of a car does
   not vanish with the drivetrain. Neither is the fast-moving field the routing rule sends to TOO HARD.
6. *Do I doubt it is inside?* "if you have doubts about something being into your circle of competence, it isn’t."
   **[M2002-092]**. I can say what each of the seven businesses sells, to whom, against whom, and what moves its profit;
   the doubt I carry is about the castle and the price, which are the next questions, not about understanding.

**Routing.** Not a bank, not a financial institution, not a field changing so fast that its ten-year economics cannot be
foreseen. A holding company of seven operating parts, each understood by the tests above, the deciding part included.

**VERDICT: IN.** The economics of the seven businesses, the deciding Test & Measurement and Electronics part among them,
can be foreseen as a range over ten years: industrial demand, price against materials, and a cost structure the filer
reports in detail every year **[M2012-065]**, **[M2011-014]**, **[M2008-033]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they? How much do they depend on the genius of the lord in
the castle?" **[M1995-038]**. The moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The segment margin record, 2012 to 2025** (segment operating income over segment revenue, after the allocated
corporate overhead; transcribed in `segments.py` from the 10-Ks `0000049826-15-000016`, `0000049826-18-000017`,
`0000049826-21-000007`, `0000049826-23-000008`, `0000049826-26-000008`):

| Segment | 2012 | 2016 | 2019 | 2020 | 2022 | 2025 | avg 2012-14 | avg 2023-25 |
|---|---|---|---|---|---|---|---|---|
| Automotive OEM | 19.4 | 24.1 | 21.5 | 17.8 | 16.8 | 21.1 | 21.1 | 19.3 |
| Food Equipment | 17.1 | 25.5 | 26.4 | 19.7 | 25.3 | 27.9 | 19.0 | 27.4 |
| Test & Measurement and Electronics | 14.9 | 18.8 | 25.6 | 25.8 | 24.2 | 24.6 | 15.0 | 24.6 |
| Welding | 25.4 | 24.9 | 27.7 | 27.2 | 30.8 | 32.9 | 25.5 | 32.3 |
| Polymers & Fluids | 15.9 | 20.3 | 22.8 | 24.8 | 25.1 | 27.9 | 17.0 | 27.4 |
| Construction Products | 11.7 | 22.4 | 23.6 | 25.5 | 25.9 | 30.2 | 14.1 | 29.3 |
| Specialty Products | 19.5 | 25.6 | 25.9 | 26.0 | 26.7 | 31.2 | 20.4 | 29.3 |
| Company (operating margin) | 16.7 | 22.5 | 24.1 | 22.9 | 23.8 | 26.3 | | |

**The parts table** (section B; share from Q1):

| Part | Share of 2021-25 segment profit | Castle, in one line | Decides |
|---|---|---|---|
| Test & Measurement and Electronics | 16.9% | Instron, MTS and Buehler testing machines, software, service and consumables; electronics-assembly and clean-room consumables. Margin 24-27% every year 2019-2025, held through 2020 | **Yes (largest)** |
| Food Equipment | 16.2% | Hobart warewash, cooking, refrigeration, food-processing equipment and a service business that grew in each of 2024 and 2025 | no |
| Automotive OEM | 14.5% | engineered fasteners and plastic components; lowest margin of the seven, below its own 2014-2018 level | no |
| Welding | 14.4% | Miller and Hobart machines and consumables; the highest and steadiest margin | no |
| Construction Products | 13.7% | Paslode and engineered fasteners; margin up from 11.7% to 30.2% while organic revenue fell in 2024 and 2025 | no |
| Specialty Products | 12.5% | Hi-Cone packaging, coding, appliance parts, ground-support equipment | no |
| Polymers & Fluids | 11.9% | Permatex, Rain-X, industrial adhesives and fluids | no |

**The castle tests, on the deciding part first, then the whole.**
1. *Key factors and their permanence* **[M1995-038]**. For Test & Measurement and Electronics the filing's description
   is "a branded and innovative producer" of test equipment, "consumables, and related software"; the segment's own
   margin record is the evidence that the factors last: 14.9% in 2012, 25.6% in 2019, 25.8% in the 2020 trough when
   ITW's revenue fell a tenth, 27.4% in 2021, then 24.2% to 24.9% after the MTS deal diluted it by 350 basis points in
   2022 (FY2022 10-K MD&A). Testing to a published standard ties the customer's results to the machine and its software;
   the installed base buys service and consumables.
2. *The money test* **[M2011-015]**: could a rival with money take Instron's or MTS's place? The record of one who
   tried is in the rivals' filings. Emerson paid for National Instruments (closed 2023-10-11) and its Test & Measurement
   segment earned a GAAP loss of $68M on $1,486M of sales in FY2025 after $425M of acquisition amortization, about 25%
   before that amortization (Emerson 10-K FY2025, `0000032604-25-000087`): money bought a business, not ITW's margin
   at a better price. MTS Systems, the business ITW bought, earned 4.1% (FY2018) and 6.1% (FY2019) on its Test &
   Simulation segment and a loss in FY2020 after impairments, as a stand-alone filer (MTS 10-K FY2020,
   `0000068709-20-000047`); the castle ITW claims for this part is therefore partly its own operating method, applied to
   a business that did not earn this much before.
3. *Pricing through the last inflation* **[M2005-020]**, **[M2005-017]**. ITW reports price against material cost as a
   margin effect every year: company total -150 basis points in 2021 and -90 in 2022 (FY2022 10-K), then +210 in 2023
   (FY2023 10-K), +40 in 2024 and +10 in 2025 (FY2025 10-K). Organic revenue rose 12.3% in 2021 and 12.1% in 2022 with
   volume weak, so price carried it. Costs ran ahead for two years and were then recovered with margin to spare; the
   company margin went from 22.9% (2020) to 26.3% (2025). "over time the businesses with strong competitive positions
   manage to pass through increases in raw material costs [...] But you get these temporary situations where, sometimes,
   the costs are increasing faster." **[M2005-017]**: that is the shape of 2021 to 2023.
4. *Unit volume.* Here the evidence runs against. Organic revenue: +2.6% (2014), +1.2% (2016), +2.9% (2017), -1.9%
   (2019), -9.8% (2020), +12.3% (2021), +12.1% (2022), +2.0% (2023), -0.7% (2024), flat (2025), with product-line
   simplification deliberately taking 0.2 to 0.6 points off each year. Segment revenue was $13,870M in 2012 and $16,062M
   in 2025, about 1.1% a year with prices and the MTS purchase included. The castle shows in margin, not in volume.
5. *The low bid* **[M2017-009]**. The customers are manufacturers, restaurants and laboratories buying a part, a
   machine or a consumable whose cost is small against the cost of its failure; no customer is above 5% of revenue
   (10-K Item 1). The deciding part's testing customers in particular buy to a standard, not on the low bid.
6. *Ask the competitors; the competitor row* (same metric, their own filings; total-company operating margin from each
   filer's XBRL 10-K facts, transcription in `peers.py`; segment figures read in the filed statements):

| Filer (accession of the 10-K read) | Metric | 2012-2014 | 2019 | 2020 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| ITW, company (`0000049826-26-000008`) | GAAP operating margin | 16.7-19.9% | 24.1% | 22.9% | 25.1% | 26.8% | 26.3% |
| Lincoln Electric, company (`0000059527-26-000006`) | GAAP operating margin | 12.7-14.3% | 12.3% | 10.6% | 17.1% | 15.9% | 17.0% |
| Lincoln Electric, Americas Welding | segment adjusted EBIT / external sales | | | | | | 19.6% (534.8 / 2,723.6) |
| ITW Welding | segment operating margin | 25.3-25.9% | 27.7% | 27.2% | 31.8% | 32.3% | 32.9% |
| ESAB, company (`0001877322-26-000007`; Form 10 filed 2022-02-22, first 10-K 2023-03-07 for FY2022) | GAAP operating margin | not a filer | n/a | 10.4% | 14.6% | 16.3% | 14.5% |
| Middleby, Commercial Foodservice (`0000769520-26-000011`) | segment adjusted EBITDA less segment depreciation and amortization / sales | | | | 24.5% | 24.3% | 23.6% |
| ITW Food Equipment | segment operating margin | 17.1-20.8% | 26.4% | 19.7% | 27.2% | 27.2% | 27.9% |
| Emerson, Test & Measurement (`0000032604-25-000087`) | segment earnings / sales (before amortization in brackets) | | | | | -19.8% | -4.6% (about 25%) |
| MTS Systems, Test & Simulation (`0000068709-20-000047`) | segment operating income / revenue | | 6.1% | loss | | | |
| ITW Test & Measurement and Electronics | segment operating margin | 14.8-15.4% | 25.6% | 25.8% | 24.2% | 24.9% | 24.6% |
| Dover, company (`0000029905-26-000009`) | GAAP operating margin | 15.7-16.2% | 13.7% | 14.0% | 15.9% | 15.6% | 17.0% |
| Parker-Hannifin, company (`0000076334-26-000105`; June years) | GAAP operating margin | 13.5-15.2% | 15.6% | 14.4% | 17.9% | 20.4% | 21.9% (FY2026 23.6%) |
| Emerson, company | pre-tax earnings plus interest / sales (no operating-income tag) | 12.8-18.0% | 15.6% | 13.9% | 19.1% | 11.5% | 16.3% |

   Middleby's and Lincoln's segment measures exclude restructuring and other items that ITW's segment figures include,
   which flatters the rivals, and ITW's still lead. Non-filers flagged: ZwickRoell (testing machines, private, Germany),
   Shimadzu (testing machines, Japan, not an SEC filer), Rational and Welbilt-under-Ali (food equipment, not SEC filers),
   Fronius and Kemppi (welding, private): their margins could not be read. No rival in any of ITW's segments shows the
   margin of the matching ITW part in any year read.
7. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Six of seven segments widened their margins between
   2012-14 and 2023-25 by 7 to 15 points; Automotive OEM narrowed by about 2. The change is credited only on a full
   cycle (section C): the margins were set by 2017-2019, fell in 2020 by no more than the volume explains (Welding,
   Polymers, Construction, Specialty and Test & Measurement held or rose in 2020), absorbed the 2021-2022 cost inflation
   and stood higher in 2023-2025 through three years of flat volume. That is a full cycle, trough and inflation both.
8. *Would it stand without the lord?* **[L2007-006]**. Here is the real weakness of the case. The filing names "The ITW
   Business Model" as "the Company's competitive advantage" (10-K Item 1): a management method, 80/20, applied by
   management. The margins before the method was reapplied (2012) were ordinary to good, 12% to 25% by segment; much of
   what Q2 credits is the method. The rows say a business that "requires a superstar" "cannot be deemed great"
   **[L2007-006]**; they also say of Precision Castparts that it "requires a very superior management that’s going to
   stay superior for a long time" and that this "works" **[M2016-005]**, an OPEN tension the framework carries. ITW's
   method is not one person: it has run since the 1980s and through three chief executives, it is taught to the
   division managers, and the 2024 succession (Mr O'Herlihy, Vice Chairman since 2015) changed nothing in the margins.
   Weighed, not decisive: a method embedded in 88 divisions is nearer to Mayo's moat than to the surgeon's.
9. *What could destroy, modify or reduce it* **[M2000-014]**. Electric vehicles for Automotive OEM (not the deciding
   part); a semiconductor and electronics down-cycle for the electronics half of the deciding part; the MTS business,
   whose demand fell in 2025 and which the filing still describes as to be improved; and the risk that the margin is
   pressed so far that volume is given up, which the flat organic revenue does not yet disprove. "A moat that must be
   continuously rebuilt will eventually be no moat at all." **[L2007-005]**: the 80/20 work is continual, but it has
   added to standing positions rather than replaced lost ones; the evidence is that the margins held when the work met a
   recession.

**The field's returns over the last full cycle (section C), judged in words.** The field is not ordinary: the rivals'
own filings show Lincoln, Middleby, Dover and Parker earning mid-teens to low-twenties operating margins, and ITW's
parts earn more than the matching rival in every comparison read, on identifiable assets that are small (ITW Welding
earned $583M on $933M of identifiable assets in 2022, FY2022 10-K segment note; Lincoln's Americas Welding earned an
adjusted $534.8M on $2,464M of segment assets in 2025). A standing castle that protects excellent returns, not ordinary
ones.

**VERDICT: IN.** The deciding part, Test & Measurement and Electronics, has held a 24% to 27% margin through the 2020
trough, the 2021-2022 inflation and a dilutive acquisition, above every testing rival whose figures could be read; the
other six parts tell the same story except Automotive OEM, which does not decide and is carried to Q7 as it is. Price
was passed through the inflation after a two-year lag **[M2005-017]**; the margins widened and were held over a full
cycle **[L2005-010]**; the weakness, that part of the castle is a management method **[L2007-006]**, **[M2016-005]**, and
that volume has not grown, is carried to Q3, Q5 and Q7 rather than closing the file.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"we’re defining it in terms of the capital actually needed in the business" **[M2010-090]**; for the business, "look at
return on tangible assets", and for the capital allocation "you have to include goodwill, because we paid for it"
**[M2011-060]**. Return on equity is not used: ITW's equity ($3,226M at 2025-12-31) has been shrunk by $26,875M of
treasury stock, and "if you keep the equity low enough by buying shares back, why, you could make return on equity
whatever you want" **[M1998-017]**.

**Return on the capital actually needed** (balance sheet lines from the 10-Ks via XBRL, checked against the FY2025
statement `0000049826-26-000008`; tangible operating capital = trade receivables + inventories + net plant less accounts
payable and accrued expenses):

| | 2016 | 2025 |
|---|---|---|
| Receivables + inventories + net plant | 2,357 + 1,076 + 1,652 = 5,085 | 3,227 + 1,659 + 2,230 = 7,116 |
| less payables + accrued expenses | 511 + 1,202 = 1,713 | 522 + 1,636 = 2,158 |
| Tangible operating capital | 3,372 | 4,958 |
| Operating income | 3,064 | 4,216 |
| Pre-tax return on tangible operating capital | 91% | 85% |
| Goodwill + intangibles | 6,021 | 5,689 |
| Pre-tax return including goodwill and intangibles | 33% | 40% |

The company's own after-tax return on average invested capital, a non-GAAP figure defined in its MD&A, is 30.4%, 31.2%
and 29.3% for 2023 to 2025 (10-K `0000049826-26-000008`, MD&A), consistent with the last line after tax at its 23.9%
adjusted rate.

**What the added capital earned.** From 2016 to 2025 operating income rose $1,152M. Tangible operating capital rose
$1,586M, and cash paid for acquisitions over 2016-2025 was $1,427M (cash-flow statements, chiefly MTS $731M in 2021 and
a $453M purchase in 2016): about $3,013M added for $1,152M more pre-tax, roughly 38% pre-tax on the increment with the
acquisitions counted, far more without them. The increment earns less than the base, as the rows expect: "Most of the
great businesses generate lots of money. They do not generate lots of opportunities to earn high returns on incremental
capital" **[M2003-120]**.

**Reinvestment to stand still and to grow.** Capital spending $455M, $437M and $419M (2023-2025) against depreciation
$282M, $301M and $317M (10-K cash-flow statement): about 1.4 times depreciation and 2.6% of revenue. "Every year we spend
amounts equal to our depreciation charge simply to stay in the same economic place" **[L2000-035]**; the filing does not
split maintenance from growth spending **[L1999-024]**, so the excess over depreciation is not shown to be growth, and
Q7 charges all of it. Working capital swings with the cycle: inventories rose from $1,189M (2020) to $2,054M (2022) and
fell to $1,659M (2025), which is why operating cash was $2,348M in 2022 and $3,539M in 2023.

**The growth arithmetic and its cap.** The business has not been growing: organic revenue averaged about 2% a year over
2019-2025 with the 2021-2022 price rises in it, and segment revenue grew about 1.1% a year from 2012 to 2025. So the
high return applies to small increments, and most of the cash cannot be reinvested at it; it has gone to dividends and
buybacks (Q6). This is the first of the three grades in the 1998 answer, "more and more money every year without putting
up anything to get it, or very little" **[M1998-081]**, but with "more and more" only modestly true: owner cash rose
from about $2.3B a year (2016-2020) to $2.5B (2021-2025).

**WEIGHS FOR.** Very high returns on the tangible capital the businesses need and modest reinvestment to keep them **[M2010-090]**,
**[M2011-060]**, **[M1998-081]**, tempered by small growth and a lower return on the acquired increment **[M2003-120]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight to ten years of them, before the income account** **[M2025-032]** (`tools/run.py`
  prints the ten-year table; read the filed statements behind it). Say what moved and why: equity against goodwill and
  intangibles, cash, receivables and inventory against sales, debt, retained earnings; "what the figures are saying and
  what they don’t say and what they can’t say" **[M2025-032]**. *(line added 2026-10-05: the rule was in Q4 of the
  framework from adoption, and no run had been asked to do it.)*
- The real costs (depreciation, stock pay, restructurings, the recurring "one-time"); EBITDA in the filer's own
  mouth; what the accounts say of management's character. The make-the-numbers habit, guidance and a featured
  adjusted figure weigh against here and are carried to Q5 (section A of the gaps case, 2026-10-06).
- **VERDICT on the accounts: IN / OUT on suspicion / TOO HARD (WORK or NATURE) on confusion; WEIGHS FOR / AGAINST**
  otherwise, with ids. The recast earnings feed Q7.

**The balance sheets first, 2016 to 2025** (year-end, $M; `tools/run.py` table of first-filed XBRL values, accessions
`0000049826-17-000022` to `0000049826-26-000008`; FY2025 checked against the filed Statement of Financial Position):

| | 2016 | 2018 | 2020 | 2022 | 2025 | 2026-06-30 |
|---|---|---|---|---|---|---|
| Total assets | 15,201 | 14,870 | 15,612 | 15,422 | 16,148 | 16,494 |
| Cash | 2,472 | 1,504 | 2,564 | 708 | 851 | 839 |
| Receivables | 2,357 | 2,622 | 2,506 | 3,171 | 3,227 | 3,564 |
| Inventories | 1,076 | 1,318 | 1,189 | 2,054 | 1,659 | 1,756 |
| Goodwill + intangibles | 6,021 | 5,717 | 5,471 | 5,632 | 5,689 | 5,632 |
| Total debt | 7,829 | 7,380 | 8,122 | 7,763 | 8,969 | 9,694 |
| Retained earnings | 19,505 | 21,217 | 23,114 | 25,799 | 30,150 | 30,812 |
| Stockholders' equity | 4,259 | 3,258 | 3,182 | 3,089 | 3,226 | 2,895 |
| Revenue (year) | 13,599 | 14,768 | 12,574 | 15,932 | 16,044 | |

What moved and why. (1) Total assets did not grow in nine years while revenue rose 18%: the business needs little new
capital (Q3). (2) Retained earnings rose $10.6B and equity fell $1.0B: every dollar earned and more went out as dividends
and buybacks, and treasury stock reached $28,004M at 2026-06-30; equity is now smaller than goodwill and intangibles, so
book value says nothing here **[M2025-032]**. (3) Cash fell from $2.5B to under $0.9B and debt rose from $7.8B to $9.7B:
the payouts have been partly borrowed (Q6, Q9). (4) Intangibles fell from $1,463M to $591M as old purchase intangibles
amortized; goodwill stayed near $4.5-5.1B; there is no goodwill impairment in 2023-2025 (10-K note 8; cumulative charges
$240M). (5) Receivables rose 37% against revenue up 18%: about 63 days of sales in 2016, 73 days in 2025 and roughly 76
days at 2026-06-30 on the first-half run rate. The filing gives no reason; written down as contrary evidence, a watch item
of the kind **[M1995-064]** names ("inventories look out of line, you know, with sales"), not shown to be a tell: inventory,
the other line it names, rose in the 2021-2022 supply shortage and came back down. (6) Prepaid expenses and other current
assets rose from $312M to $463M in 2025 (10-K working-capital table) and were $441M at 2026-06-30; small against the
whole, unexplained, recorded. What the balance sheets cannot say: the value of the brands and the operating method, which
appear nowhere on them.

**The real costs.**
- *Depreciation* $317M (2025) against capital spending $419M: depreciation understates the cash need, so owner cash
  charges all capital spending, with the depreciation variant beside it.
- *Stock pay* $69M (2025), expensed and in the statement of cash flows each year (10-K note 14); about 0.4% of revenue; it
  is deducted from owner cash **[L2015-003]**, **[L2021-003]**.
- *Amortization* of acquired intangibles $80M (2025), customer lists, trademarks and patents from past purchases (note 8);
  not added back in the central figure because owner cash starts from operating cash flow, where it is already non-cash.
- *Restructuring* is small and kept inside operating income in every segment table (the MD&A gives it as a 10 to 50 basis
  point margin effect), never excluded from the figures the company features.
- *Pensions*: the U.S. plans closed to new entrants in 2007; a 25 basis point fall in the discount rate adds about $21M to
  the U.S. primary plan obligation (10-K critical estimates). Not material to the recast.
- *The one-off items* the company names, and the direction they run: the 2024 LIFO-to-FIFO change ($117M pre-tax
  favourable) and the 2024 Wilsonart gain ($363M pre-tax, $1.26 a share), and the 2022 divestiture gains ($0.61): in each
  case the release shows GAAP EPS first and an "ex-item" figure that removes the **gain**, making the featured growth
  smaller, not larger (8-Ks `0000049826-23-000002`, `0000049826-24-000017`, `0000049826-24-000045`).

**EBITDA in the filer's own mouth.** The 10-K MD&A computes "Total Debt to EBITDA" (1.9 times in 2025) as a debt measure;
EBITDA is not presented as earnings anywhere read. "The one figure we regard as utter nonsense is the so-called EBITDA"
**[M1998-086]**: a weighing against of the mild kind, since it is used to describe leverage and the depreciation it leaves
out is small against the profit.

**Guidance, targets and the adjusted figure, recorded here and carried to Q5.** ITW gives annual GAAP EPS guidance, and
organic-growth and margin guidance, every February and updates it every quarter (EX-99.1 to the 8-Ks read:
`0000049826-23-000002`, `-23-000050`, `-24-000005`, `-24-000017`, `-24-000034`, `-24-000045`, `-25-000004`, `-25-000011`,
`-25-000034`, `-25-000050`, `-26-000003`, `-26-000047`). The trail:

| Year | Organic growth guided (Feb) | Organic growth reported | GAAP EPS guided (Feb) | GAAP EPS reported |
|---|---|---|---|---|
| 2023 | 3 to 5% | 2.0% (missed) | $9.40 to $9.80 | $9.74 |
| 2024 | 1 to 3% | -0.7% (missed) | $10.00 to $10.40 | $11.71, or $10.15 without the LIFO change and the Wilsonart gain |
| 2025 | 0 to 2% | 0.0% (bottom of range) | range raised and narrowed in the year to $10.40 to $10.50 | $10.49, which the release says "exceeded the prior guidance mid-point of $10.45" |
| 2026 | 1 to 3%, raised in July to 3 to 4% | (first half 2.5%) | $11.00 to $11.40, raised in July to a $11.45 midpoint | not yet |

The habit is there: guidance is given, and the February 2026 release headlines that EPS "exceeded the prior guidance
mid-point". But the targets are not consistently reached: organic growth missed its range twice in three years, and EPS
landed inside its range, not always above it **[L2002-041]**, **[L2019-006]**. The featured figure is GAAP EPS; the
adjusted figures (free cash flow, after-tax ROIC with discrete tax items removed, "ex-item" EPS) are shown beside GAAP and
remove gains as well as costs **[L2016-006]**. The 10-K risk factors name "long-term financial performance targets"; the
company states and pursues them.

**What the accounts say of management's character.** Clear and consistent: the same segment table for fourteen years,
the drivers of every margin change itemised in basis points, restructuring left in, gains taken out of the featured
growth. That is the management "that doesn’t care about the accounting but does explain to you in clear terms what’s
going on" **[M1994-018]**, with a guidance habit beside it.

**Owner cash after every real cost** (operating cash flow less stock pay less all capital spending; for the all-equity
basis the company's interest expense is added back after tax at 24% (CONVENTION of this run: the company's own adjusted
rates were 23.2% to 23.9% for 2023-2025 and its 2021-2022 rate is not restated in what I read, so 24% is used for all
years); acquisitions net of businesses sold are deducted by Q7 specific (c); $M):

| Year | OCF | stock pay | capex | equity-only owner cash | after-tax interest | all-equity owner cash | acquisitions net of sales | all-equity, acquisitions deducted | equity-only, acquisitions deducted |
|---|---|---|---|---|---|---|---|---|---|
| 2018 | 2,811 | 40 | 364 | 2,407 | 195 | 2,602 | -1 | 2,603 | 2,408 |
| 2019 | 2,995 | 41 | 326 | 2,628 | 168 | 2,796 | -116 | 2,912 | 2,744 |
| 2020 | 2,807 | 42 | 236 | 2,529 | 157 | 2,686 | -1 | 2,687 | 2,530 |
| 2021 | 2,557 | 53 | 296 | 2,208 | 154 | 2,362 | 731 | 1,631 | 1,477 |
| 2022 | 2,348 | 63 | 412 | 1,873 | 154 | 2,027 | -276 | 2,303 | 2,149 |
| 2023 | 3,539 | 69 | 455 | 3,015 | 202 | 3,217 | -7 | 3,224 | 3,022 |
| 2024 | 3,281 | 61 | 437 | 2,783 | 215 | 2,998 | -280 | 3,278 | 3,063 |
| 2025 | 3,126 | 69 | 419 | 2,638 | 222 | 2,860 | 118 | 2,742 | 2,520 |

Sources: cash-flow statements in the FY2020 (`0000049826-21-000007`), FY2022 (`0000049826-23-000008`) and FY2025
(`0000049826-26-000008`) 10-Ks; interest expense from the income statements of the same filings ($257M, $221M, $206M,
$202M, $203M, $266M, $283M, $292M); acquisitions and proceeds from sales of operations, affiliates and the Wilsonart
interest from the investing section. The five-year (2021-2025) averages: equity-only owner cash $2,503M, all-equity
$2,693M; with acquisitions net of sales deducted, all-equity **$2,636M** and equity-only **$2,446M**. Operating cash flow
swings with working capital (inventories built in 2021-2022 and released in 2023); it is counted, by Q7 specific (d).

**VERDICT on the accounts: WEIGHS FOR**, not a STOP: the accounts are clear, stock pay and restructuring are left in, the
depreciation shortfall is visible and charged **[M1994-018]**, **[L2021-003]**. Against, and carried to Q5: annual GAAP EPS
and organic guidance with a "beat the midpoint" headline **[L2019-006]**, **[L2002-041]**; EBITDA used for leverage
**[M1998-086]**; receivables growing faster than sales, recorded **[M1995-064]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- The two yardsticks; the tells of dishonesty (the proxy, the letters, how they talk about mistakes); love of the
  business; what ability shows in. Integrity applied on doubt alone.
- The habits carried from Q4 (targets made or beaten, guidance, the adjusted figure featured), read with the integrity
  record; doubt closes **[M2013-088]**.
- **VERDICT on integrity: IN / OUT; ability WEIGHS FOR / AGAINST**, with ids.

**Who.** Christopher A. O'Herlihy, President and Chief Executive Officer since 2024, Vice Chairman 2015-2023 (10-K
executive officers table); Michael M. Larsen, CFO since 2013; the former chief executive, E. Scott Santi, signed the 2023
releases as Chairman and CEO. The operating group presidents are career ITW people (the 10-K table shows each rising
through the segments). The chief accounting officer of seventeen years retires in 2027 and is succeeded by the company
controller, a 20-year ITW employee and former Deloitte auditor; the 8-K says the retirement "is not due to any
disagreement" (8-K `0000049826-26-000033`).

**The first yardstick, the record against the hand dealt** **[M1994-008]**. The hand: seven mature industrial businesses
with flat volume. The play: segment margins up 7 to 15 points in six of seven segments over 2012-2025, held through 2020
and the 2021-2022 inflation, above every rival whose filing could be read (Q2). Ability weighs for.

**The second yardstick, the treatment of owners** **[M1994-008]**, **[M1994-009]**, from the proxy (DEF 14A
`0001193125-26-127599`): CEO total compensation in the Summary Compensation Table $6.9M (2023), $10.9M (2024, first year
as CEO) and $15.2M (2025), of which $10.5M in 2025 is stock and options at grant value. Annual incentive on operating
income growth and organic revenue growth; three-year PSUs on operating margin, after-tax ROIC, EPS growth and a
"CBI Yield" (revenue from new products); 2023-2025 PSUs paid 150.4% of target; the committee "made no adjustments" to
the 2025 annual payouts; stock ownership of six times salary for the CEO, with net shares retained; a clawback on
restatement "whether or not based on misconduct"; hedging and pledging prohibited; no dividends on unvested awards.
Nothing in the proxy is the "heads I win, tails you lose" form **[L1994-020]**; the size and the options are weighed at Q6.

**The habits carried from Q4**, read with the integrity record. Annual GAAP EPS and organic guidance, updated quarterly,
with a release headline that EPS "exceeded the prior guidance mid-point" (February 2026). Against: the rows that warn of
CEOs who "consistently reach their declared targets" **[L2002-041]** and of "the scourge of earnings "guidance" and the
desire of CEOs to "hit the number."" **[L2019-006]**. But the record in the releases is not one of always hitting:
organic growth missed its guided range in 2023 and 2024 and the miss was reported in the same releases in the same
words ("organic growth declined 0.7%"); the featured number is GAAP EPS; the "ex-item" figures remove gains, not costs;
the accounts leave restructuring and stock pay in. The language of the releases and the 10-K is corporate and heavy with
house terms ("80/20 Front-to-Back", "Customer-back Innovation", "Win the Recovery"); "a standardized bunch of popular
jargon that looks like it came out of the same consulting firm, I do think it’s a big turnoff" **[M1998-038]**: a turnoff,
weighed against the clarity of the figures behind it. How they speak of mistakes: no release or 10-K passage read calls
anything a mistake; MTS is described as a business to be improved, its 2025 decline named plainly in the MD&A ("lower
demand in the MTS Test & Simulation business"); the taboo of **[L2024-003]** is not shown, but no confession is shown
either.

**The tells of dishonesty, swept.** Reports that dance: none found; the key figure (organic growth) is reported every
quarter, good or bad. Too good to be true: no. Stock price emphasis: the releases do not headline the share price; the
10-K carries the required performance graph. Legal: Item 3 "None" (FY2025 10-K); a text sweep of the FY2014, FY2017,
FY2020, FY2022 and FY2025 10-Ks for "Foreign Corrupt", "deferred prosecution", "consent decree" and "restatement of"
found no instance. Serial issuance: none; the share count fell from 379,447,026 at 2015-01-31 (FY2014 10-K cover, `0000049826-15-000016`)
to 284.8 million at 2026-06-30.

**VERDICT on integrity: IN.** I have no doubt of the kind **[M2013-088]** closes on: the guidance habit is real and is
recorded against, but the record shows misses reported plainly, GAAP featured, gains excluded rather than costs, and
clean accounts over fourteen years. **Ability WEIGHS FOR**, on the record against the hand dealt **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- Part A: the retention test (a dollar kept worth more than a dollar, over time); buybacks (only below value; a buyback
  with no stated price weighs against unless the prices paid sit at or below the bottom of the Q7 range); issuance and
  deals (value given against value got; an all-stock deal at an undervalued price is the one STOP here).
- Part B: pay tied to what the person controls; the board; the owners as partners.
- **WEIGHS FOR / AGAINST / UNDECIDED**, one sentence per part, with ids.

**Part A: the money.**
- *Retention.* ITW retains almost nothing: in 2025 it earned $3,066M and paid $1,785M in dividends and $1,500M in
  buybacks (10-K cash-flow statement), more than net income and more than its free cash flow of $2,707M; the gap was
  borrowed (net debt proceeds $508M). The retention test **[R1995-009]** is therefore a test of the small sums kept, and
  the business that cannot employ its earnings "should be paying out dividends" **[M2004-089]**; it does. Dividends:
  quarterly $1.40 (2023) to $1.50 (2024) to $1.61 (2025), $6.44 a year at the last rate; about 2.5% on the price.
- *Buybacks and the prices paid* (10-K FY2025 MD&A and Item 5, `0000049826-26-000008`; 10-Q `0000049826-26-000049`):

| Period | Shares | Average price | Amount |
|---|---|---|---|
| 2022 | 7.1M | $210.46 | $1,750M (cash flow) |
| 2023 | 6.3M + 38,000 | $235.35; $263.44 | $1,500M |
| 2024 | 5.9M | $254.04 | $1,500M |
| 2025 | 6.0M | $251.20 | $1,500M |
| 2026 first half | 4.3M | about $262 ($1,125M / 4.3M) | $1,125M |

  The programmes (2021, $3.0B; 2023, $5.0B with about $2.0B left at 2025-12-31) name an amount and no price; the risk
  factor says buybacks are "a significant component of the Company's capital allocation strategy" funded "with free cash
  flow and short-term borrowings". A programme with no stated price weighs against **[L2016-002]** unless the prices paid
  sit at or below the bottom of the Q7 range. Recorded back from Q7: the bottom of the central range is $135 a share
  (all-equity) and $152 (equity-only); every purchase since 2022 was made at $210 to $262, well above the top of the range
  ($158 all-equity, $176 equity-only). By the framework's test, these repurchases were made above value, "Continuing
  shareholders are hurt unless shares are purchased below intrinsic value." **[L2011-003]**, and with borrowed money
  beyond free cash flow, which **[L1999-023]**'s "sensible borrowing capacity" allows but its second condition does not.
  Weighs against.
- *Deals.* MTS Test & Simulation, bought from Amphenol on 2021-12-01 for $750M (goodwill $430M, intangibles $259M;
  FY2022 10-K note 3, `0000049826-23-000008`), a business with $422M of revenue in 2022 that earned 4.1% to 6.1% as part
  of MTS Systems (Q2) and diluted the segment margin by 350 basis points in 2022; demand fell in 2025. On ITW's own
  figures the price is about 1.8 times revenue for a business still below the segment's margin four years on: value got
  against value given is not shown to be favourable **[M1995-001]**. Cash paid, no stock issued, so the one STOP of Part A
  (an all-stock deal in undervalued stock) does not arise. Divestitures, the other side of the portfolio work: 51% of
  Decorative Surfaces to CD&R in 2012 for about $1.05B in payments (FY2014 10-K), then a $167M dividend from Wilsonart in
  2016 and the remaining interest sold in 2024 for $398M (FY2025 10-K note 5); Industrial Packaging to Carlyle in 2014 for
  $3.2B, pre-tax gain $1.7B (FY2014 10-K); smaller sales in 2019 ($120M proceeds) and 2022 ($278M). The proceeds largely
  funded buybacks (FY2014 10-K: "A portion of the proceeds was used to fund share repurchases").
- **Part A WEIGHS AGAINST**: the payout policy fits a business that cannot reinvest **[M2004-089]**, but the buybacks
  are made at prices above every value this run can build, on borrowed money beyond free cash flow, with no stated
  price **[L2016-002]**, **[L2011-003]**; MTS is not shown to have earned its price **[M1995-001]**.

**Part B: the pay, the board, the owners.**
- *Pay* (proxy `0001193125-26-127599`): annual incentive on operating-income growth and organic growth, which the segment
  managers control; PSUs on three-year operating margin, after-tax ROIC, EPS growth and CBI yield, the last two moved by
  buybacks and by new-product revenue respectively; half of long-term pay in ten-year stock options at the market price
  on the grant date, with no step-up for retained earnings (the rows ask for "a step-up in price that reflects the fact
  that money is reinvested" **[M1997-043]**), softened here because ITW pays out most of its earnings. CEO pay rose from
  $10.9M to $15.2M in a year when EPS excluding the 2024 items rose 3.3%. Peer-median targeting ("Target total
  compensation is based on the median of our peer group") is the ratchet the rows warn of.
- *The board*: the CEO does not chair; the former CEO (2012-2023) is non-executive Chairman and is listed as not
  independent; there is an independent Lead Director. The executive committee ownership guideline is six times salary.
- *The owners*: no dual class, no poison pill found in what I read, fair-disclosure policy stated in the 10-K, results
  reported in plain GAAP.
- **Part B WEIGHS AGAINST, mildly**: pay is tied to what the managers control and recovered on restatement, but fixed-price
  options, EPS growth helped by buybacks, and peer-median ratchets are the forms the rows criticise **[M1997-043]**.

## Q7 — WHAT IS IT WORTH? STOP.
- How much cash, how sure, how soon, at the long government rate, as a range (the CONVENTION construction: five-year
  average of owner cash after every real cost, carried at the growth shown and capped by Q3, ten years then no real
  growth, at the sovereign; the six specifics: the cycle base where an end year is aberrational, negative growth carried as the bottom, acquisitions deducted with total growth credited and the
  organic pair beside, working capital counted, the maintenance-only case central where the filing allows the guess, the cap;
  a deal closed after the window on its own filed record).
- The floor (CONVENTION): about ten percent pre-tax expected return, as the speakers stated and qualified it; below it
  the name is quit on, not ranked. Applied to owner cash after the company's own income tax, no conversion; a
  carryforward or credit that runs out inside ten years is priced separately (section E).
- **Value range:** $135.29 to $158.06 a share (all-equity, central) against $261.94. **Closes:** TOO HARD if the range is wider than about three
  to one; OUT if the price sits inside or just below a narrower range (not a screamer); IN only if the price is so far
  below that no pencil is needed.
- **Fair price (a reporting figure, never a verdict; Part VII):** $68.04 a share, the price at which the midpoint of the
  range earns the floor, after the company's own tax; the central figure on the all-equity basis (owner cash before interest
  against market value plus net debt at the latest filed date, stated subsequent events added) and the equity-only figure
  $92.33 beside it. No cheap price is reported. *(basis named 2026-10-06, section H.)*
- **VERDICT: OUT** (below).

"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; credit goes for "whatever net cash is left every year" **[M1998-080]**.
Arithmetic in `q7.py` (output kept in `cache/`, rerunnable).

**Inputs.** Owner cash after every real cost from Q4, all-equity basis (before interest, after the company's own tax, no
conversion), acquisitions net of businesses sold deducted (specific (c), the default pair). Rate 5.64% (30-year Treasury,
10/06/2026). Net debt $8,855M (2026-06-30, Step 0); shares 284.8M. The company's tax is at its normal rate (adjusted
23.2% to 23.9%); no carryforward or credit expiring inside ten years was found that lowers it (the 2024 capital-loss use
and the 2025 valuation-allowance release are one-off discrete items, already in the cash taxes of those years).

**The base, specific (a).** The literal window 2021-2025 averages $2,636M. Its first year is aberrational on the filer's
own description: 2021 carries the $731M MTS purchase, a single deal the filer names, and the post-2020 working-capital
build; "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**
(end-to-end the literal window gives 13.9% a year). The cycle base is 2018-2025, peak (2018-2019) through the 2020 trough
and the 2021-2022 inflation to 2023-2025: **$2,672M**. The two bases differ by 1%; the cycle base is central, the literal
window beside.

**The growth shown, specifics (a), (b) and (c).** Measured between the averages of successive five-year periods,
equity-only owner cash with acquisitions deducted: 2016-2020 $2,257M to 2021-2025 $2,446M, **1.62% a year** (aggregate,
not per share). The organic pair, acquisitions left out and the filer's own organic growth credited: the 2019-2025
average of the reported organic rates is 2.0% (Q2, test 4), on a window base of $2,693M. The cap (f): 1.62% and 2.0% are
far below the 5.64% rate; nothing to cut **[M1997-095]**.

**Specifics (d) and (e).** Working capital is in operating cash flow (counted). The filing does not split maintenance
from growth capital spending, so all of it is charged; the depreciation variant (charging $317M instead of $419M in 2025,
about $100-140M a year more owner cash) would lift the range by roughly $8 a share and changes nothing below.

**The range (COMPUTATION in `q7.py`; ten years at the shown growth, then zero nominal growth, at 5.64%):**

| Case | Base, $M | Growth | Enterprise value, $M | Per share (less $8,855M net debt, / 284.8M) |
|---|---|---|---|---|
| Central, no growth | 2,672 | 0% | 47,385 | **$135.29** |
| Central, shown growth | 2,672 | 1.62% | 53,871 | **$158.06** |
| Literal window, beside | 2,636 | 0% / 1.62% | 46,730 / 53,128 | $132.99 / $155.45 |
| Organic pair, beside | 2,693 | 0% / 2.0% | 47,745 / 55,941 | $136.55 / $165.33 |
| Equity-only, beside (owner cash after interest / shares) | 2,489 | 0% / 1.62% | | $154.96 / $176.18 |

**Value range: $135 to $158 a share (all-equity, central) against $261.94.** Width 1.17 to one: narrow, not the
TOO HARD case. The price sits **above the top** of every range built: $104 a share above the central top, $86 above the
equity-only top, $97 above the organic pair's top.

**The floor.** At the price the enterprise costs $83,456M. The expected return on it: 3.20% with no growth, 3.68% with the
shown growth (internal rate of return of the shown-growth stream), against the floor of about ten percent **[M2003-149]**
and even against the 5.64% bond. To earn only the bond rate the price needs owner cash to grow 7.1% a year for ten years,
four times what it has shown. "there’s just a point at which we drop out of the game" **[M2003-149]**: this is well
below it.

**Fair price (a reporting figure, never a verdict; Part VII):** **$68.04 a share** on the all-equity basis, the price at
which the midpoint case (growth 0.81%, halfway between the two ends) earns 10% after the company's own tax, enterprise
value $28,233M less $8,855M net debt; the equity-only figure beside it is **$92.33** (owner cash after interest, same
midpoint growth, at 10%). Central figure: all-equity. No cheap price is reported.

**VERDICT: OUT.** Valued, with a narrow range, and the price is above its top: the expected return at the price is about
a third of the floor, so by the floor convention the name is quit on, not ranked **[M2003-149]**, **[L2013-012]**; no
pencil could make it a screamer **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7.** Q1 IN, Q2 IN, Q3 weighs for, Q4 weighs for, Q5 integrity IN and ability for, Q6 weighs against (A) and
mildly against (B); Q7 OUT: value range **$135.29 to $158.06 a share** (all-equity, cycle base 2018-2025, shown growth
1.62%) against **$261.94** (quote of 2026-10-07); expected return at the price 3.2% to 3.7% against the floor of about ten
percent. Not a TOO HARD, so no research pass is opened. No integrity facts are left unjudged (Q5 was reached and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Bears on Q8.** The price's expected return (3.2% to 3.7%, Q7) is below the 5.64% thirty-year Treasury yield
  (10/06/2026) on which the range was discounted.
- **Bears on Q9.** Total debt $9,694M at 2026-06-30 (short-term $3,145M including $2.1B of commercial paper and the $1.0B
  2.65% notes due 2026-11-15; long-term $6,549M), cash $839M (10-Q `0000049826-26-000049`). Long-term maturities at
  2025-12-31: $999M (2026), $1,467M (2027), $759M (2028), none in 2029, $585M (2030), $3,872M later; all senior unsecured;
  about $5.0B of it in euros, designated as a hedge of the euro operations (10-K note 10). A $3.0B revolving facility to
  2027-10-21 backs the commercial paper and was undrawn; a new credit agreement was signed 2026-02-20 (8-K
  `0001193125-26-061771`, not read beyond its cover); $1.5B of 4.650% notes due 2029 issued 2026-08-13 to repay commercial
  paper. Operating income covered interest about 14 times in 2025 ($4,216M / $292M); the company's own debt-to-EBITDA was
  1.9. Guarantees and letters of credit about $265M. Pensions closed to new entrants since 2007. Over 50% of sales outside
  the United States; four immaterial Russian subsidiaries ($38M net assets). Product-liability, toxic-tort and
  environmental claims are described as ordinary-course and not material (note 12). The commercial-paper reliance is a
  rolling short-term borrowing that funds part of the buybacks.
- **Bears on Q10.** Nothing beyond Q7.
- **Bears on Q12.** Fasteners, kitchen equipment, welding machines, test machines, adhesives, packaging rings; none of
  the businesses the rows name. Hi-Cone's plastic multi-pack rings are the product most exposed to the single-use-plastics
  rules the 10-K risk factors mention.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits `9738f0cf` (Step 0), `75265742` (Q1), `cf074dbc` (Q2), `ac962ac3` (Q3), `fc388971` (Q4), `de72edb1` (Q5),
      `d2b27ce1` (Q6), `c0479976` (Q7), and the close. The run was interrupted by a usage limit between Q1 and Q2 and resumed
      on 2026-10-10 from the file on disk; nothing was refetched that was in `cache/`. The run keeps its 2026-10-07 date
      and its 2026-10-07 price; **the price was not refreshed**, so it is now three days old at the close.
- [x] Dispatched: the brief allowed per-question commits; the lock in `Screens/_daily/` was the dispatcher's. Several
      analysts committed into the same repository at once on 2026-10-10 and the git index was repeatedly locked; three
      stale lock files (index.lock, HEAD.lock, refs/heads/master.lock, all dated 10:02 to 10:05 with no git process alive)
      were removed by me before the Q2 commit, and later commits went through a retry helper (`commit.py`) that waits and
      never removes a lock. Every commit of this run is a pathspec commit of my two paths only; other analysts' staged
      files (a JKHY run file was staged in the shared index at the time) were not committed by me. Folding is the
      dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination, added at the
      resume:** `git log` output during the commit retries showed other runs' commit subjects (KLAC, JKHY, AME), including
      their boxes and figures; none is about ITW and none was used. The coordinator's resume message named nothing about
      ITW's outcome.
- [x] Every v5 id resolves and every quoted fragment beside an id is in its row (`check_ids.py`, last run: 65 ids,
      0 problems); every filing fact carries its accession or names the 10-K it comes from; competitor totals are XBRL
      transcriptions from each filer's 10-K facts, segment figures read in the filed statements.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 are NOT REACHED.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending, acquisitions net of
      sales deducted), never a net-income proxy; the sovereign from the U.S. Treasury; the price is an aggregator quote,
      flagged.
- [x] Contrary evidence was written down as found (foundations list; receivables and prepaid lines at Q4; MTS at Q2 and
      Q6; flat volume at Q2 and Q3).
- [x] No point-in-time anchor; rows of any date allowed.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the closing commit (result in the close commit's message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The business-of-parts threshold decided by a rounding difference.** With seven segments each holding 12% to 17% of
five-year profit, the CONVENTION's "the largest part decides" picked Test & Measurement and Electronics (16.9%) over Food
Equipment (16.2%); a different five-year window (2020-2024) or one year of FX would swap them. The convention was written
for a company with one big part; for an evenly spread conglomerate it should say whether "decides" means the largest, all
parts above some share, or the whole read together. I applied it literally and read every part, which here all pointed
the same way. (2) **"The midpoint of the range" for the fair price** is not defined: the midpoint of the two per-share
values, or the cash stream at the midpoint growth. I used the stream at midpoint growth discounted at 10% (`q7.py`); the
two differ little here because the range is narrow, but they would not on a wide range. (3) **The tax rate for adding
interest back** on the all-equity basis is not stated; I used 24%, the company's adjusted rate rounded, as a CONVENTION
of this run. (4) **Specific (c) "net of businesses sold"** did not say whether the sale of an equity-method stake
(Wilsonart, $395M in 2024) counts as a business sold; I counted it, which raises the 2024 base by $280M and the central
range by about $3 a share. (5) **Specific (a) leaves the length of "the last full cycle" to the analyst**; I took
2018-2025 on the filer's own description of 2020 as the trough and 2021 as the acquisition year. (6) **The template's
Q7 and Q2 instruction bullets** stay in the run file above the answers; a filled run reads oddly with the blank
placeholders, which I filled for Q7. (7) **The brief's commit instruction assumes one writer**: with several dispatched
analysts committing into one repository at once, the shared git index locked repeatedly and left stale lock files, and
`git log` put other runs' subjects and boxes in front of each analyst, which the blind rule cannot prevent. A brief for
parallel analysts should give each a worktree or serialise the commits.

**Where the brief was wrong or short.** The dispatcher's message listed Parker-Hannifin, Dover and Emerson as
competitors "segment by segment where possible", but none of them matches ITW's segments except Emerson's Test &
Measurement (from 2023), and the deciding part's most direct comparator, MTS Systems' own Test & Simulation filings
before 2021, was not on the list; I added it. "ESAB filed from 2022 (check)": ESAB's Form 10 was filed 2022-02-22 and its
first 10-K on 2023-03-07 for FY2022; its XBRL facts carry 2020-2021 as comparatives. The brief's commit procedure, as
above, did not survive parallel dispatch.
