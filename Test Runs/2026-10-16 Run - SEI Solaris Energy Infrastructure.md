# Company Run — Solaris Energy Infrastructure, Inc. (NYSE: SEI) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-16, after the run was committed: not held (`PORTFOLIO.md` carries no line for
SEI, SOI or Solaris).*

**CONTAMINATION, declared (the blind rule).** Seen by accident and not used: (1) a directory listing of `Test Runs/`, taken
before the run file was copied, showed five other run files and research folders dated 2026-10-16 (HMH, NGS, NOV, OIS, USAC);
none was opened. (2) The session's opening context showed the last five commit subjects, which describe the NGS run of
2026-10-16 (box and figures); not used. (3) The opening `git status` showed research-folder file names for AYI and ARCB;
not opened. (4) A memory index line in the session context describes the queue state in general terms; it names no SEI or
SOI verdict and was not used. No file about SEI or SOI under any name was opened, listed or searched.

**Dispatch note.** Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure:
the lines of evidence were chosen by the analyst from Items 1, 1A and 7 of the 10-K (listed in Step 0).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $65.16 (close 2026-10-15; `tools/run.py` live quote, **aggregator, flagged** under operator rule 5; used
  for the quote only).
- **Shares by class.** `python Screens/cover_shares.py SEI` reads the cover of the 10-Q filed 2026-08-06 (period
  2026-06-30, accession `0001628280-26-054349`), as of 2026-08-03: Class A 65,831,540; Class B 10,734,852. Charter note
  read (10-Q balance sheet, same accession): Class B "convertible into Class A common stock on a one -for-one basis", each
  Class B share paired with a Solaris LLC ("OpCo") unit; the Class B holders own their share of the business through OpCo
  units, so the two classes are one economic count (the 10-K's Note 14 and the risk factor on Solaris LLC Units read the same
  way). Check against issued shares: the 10-Q balance sheet shows 62,814 thousand Class A and 10,735 thousand Class B issued and
  outstanding at 2026-06-30 (73,549 thousand); the cover's 3.0 million more Class A after the quarter is the GESA acquisition of
  2026-07-01 (2,880,682 Class A shares, 10-Q Note 20 / MD&A) plus vesting. **After the cover:** the Omega Foundation
  Services merger of 2026-09-01 issued 3,599,199 Class A shares (8-K filed 2026-09-08, accession `0001193125-26-385257`).
  **Owners' count used: 80,165,591** (76,566,392 cover + 3,599,199). Not counted: the shares that may issue on conversion of
  the 4.75% 2030 Notes ($155.0 million) and the 0.25% 2031 Notes ($747.5 million, with capped calls); on the all-equity basis
  both are carried as debt at face. The Focus Genco shares of 2026-03-16 (4,182,772 Class A) are inside the 2026-06-30 count.
- **Market cap:** 80,165,591 x $65.16 = **$5,224M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-15 (fetched by `tools/run.py` from the Treasury, the issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-27, accession `0001628280-26-012501` (Items 1, 1A, 3,
  5, 7, 8 with Notes 3, 4, 5, 6, 11, 12, 14, 19, 20, 21); 10-Q for 2026-06-30, filed 2026-08-06, accession
  `0001628280-26-054349` (balance sheet, segment note, MD&A, subsequent events); 10-Q for 2026-03-31, filed 2026-05-01,
  accession `0001628280-26-029046` (fetched, consulted for the Genco closing only); DEF 14A filed 2026-04-01, accession
  `0001140361-26-012799` (ownership, pay table, incentive design); the 10-Ks for FY2018 to FY2024 (accessions
  `0001697500-19-000009`, `0001697500-20-000006`, `0001697500-21-000019`, `0001697500-22-000011`,
  `0001558370-23-003344`, `0001697500-24-000023`, `0001697500-25-000013`) for the cycle and the old segment; 8-Ks of
  2026-03-20 (`0001193125-26-117930`, Genco), 2026-05-01 8-K/A (`0001193125-26-201448`, Genco not significant), 2026-07-06
  (`0001628280-26-047296`), 2026-09-08 (`0001193125-26-385257`, Omega), 2026-09-22 (`0001193125-26-397255`), 2026-09-23
  (`0001193125-26-399432`) and 2026-10-01 (`0001193125-26-410682`, $1.25 billion 7.000% Senior Notes due 2032).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for FY2025,
  $209,104 thousand on the face of the FY2025 consolidated statement of cash flows (accession `0001628280-26-012501`),
  equals `tools/run.py`'s 209.1; FY2023's $89,353 thousand (same statement) equals its 89.4.
- **`python tools/run.py SEI`, arithmetic lines only** (output kept at `Test Runs/_research 2026-10-16 SEI/run_py_output.md`;
  its share line is a stale 2018 weighted average and is not used). Owner cash as filed, OCF less stock pay less all capital
  spending (USD M): 2023 17.2; 2024 -139.7; 2025 -461.1; on depreciation instead of capital spending: 45.4; 1.5; 101.4. Its
  five-year window: -122.3 (capex basis) and 32.8 (D&A basis). Finance-lease principal (2.5; 3.0; 3.2) is printed as an
  alternate and is taken into owner cash below. The tool refuses a growth figure on a non-positive base; so does this run.
- **The lines of evidence this name needs, chosen from Items 1, 1A and 7 (the brief's departure):** (1) the two segments
  and their margins over the last full cycle, and which part decides; (2) customer concentration (one data-center customer
  was 47.3% of FY2025 revenue) and the single leading supplier of generation equipment; (3) competitors, of which the
  10-K names none by name; (4) the capital spending, the debt that funds it and the purchase commitments; (5) the
  acquisitions (MER 2024, HVMVLV 2025, Genco, GESA and Omega 2026) and their goodwill and shares; (6) stock pay and share
  issuance; (7) the short-seller report of 2025-03-17 and the suits that followed; (8) related parties and the Tax
  Receivable Agreement. Pricing through the last inflation is read only for the logistics part (the power part has no
  history through it). Buybacks: none since 2024 ($15.4 million of authority left).

**The balance sheets, read in Step 0 (Q4's eight to ten years, `tools/run.py` table and the filed statements; USD M):**

| year-end | total assets | equity incl. NCI | cash | goodwill | intangibles | debt on the face | note |
|---|---|---|---|---|---|---|---|
| 2018 | 425 | 307 | 25 | 17 | 5 | about 13 (line of credit) | the logistics business at its peak |
| 2019 | 505 | 410 | 67 | 17 | 4 | none tagged | peak year |
| 2020 | 412 | 316 | 60 | 13 | 3 | none tagged | $47.8M impairments (FY2022 10-K cash-flow statement) |
| 2021 | 406 | 298 | 36 | 13 | 2 | none tagged | trough |
| 2022 | 463 | 317 | 9 | 13 | 1 | about 8 | |
| 2023 | 468 | 316 | 6 | 13 | 1 | about 60 | last year of the logistics-only company |
| 2024 | 1,123 | 667 | 114 | 104 | 72 | 316 | MER merger (Sept 2024): goodwill +$90.3M, intangibles +$73.9M; $160.9M share offering |
| 2025 | 2,143 | 827 | 353 | 105 | 60 | 1,084 face (convertibles $902.5M, Stateline term loan $186.0M, finance leases) | equipment held for lease $1,074M |
| 2026-06-30 | 4,212 | 1,161 | 824 (+70.7 restricted) | 105 | 69 | 2,548 face (Senior Notes $1,300M, convertibles $902.5M, Stateline $339.7M, finance leases $5.5M) | deferred revenue $192M (customer prepayments); TRA payable $109M |

What the balance sheets say: for six years (2018 to 2023) this was a small, nearly debt-free logistics company whose assets
did not grow (about $400M to $500M) and whose retained earnings fell from $74M (2019) to $6M (2021), the 2020 trough
taking the cash and an impairment. From 2024 the balance sheet is a different company: assets x9 in thirty months, almost
all of it turbines and equipment held for lease, paid for with $2.5 billion of debt at mid-2026 (another $1.25 billion on
2026-10-01) and with shares issued for MER, HVMVLV, Genco, GESA and Omega and a $160.9M offering. What it cannot say: what
the turbines will earn after their contracts end; the power fleet has no history through a downturn. Receivables rose from
$103M to $210M in six months against power revenue that rose about 30% quarter on quarter, and customer prepayments
($192M of deferred revenue) appeared: both are tied to the new data-center contracts.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years?" **[M1997-109]**; the
question is what the turbine fleet and the silo fleet will earn, not what the next buyer pays for an AI-power story. The
market serves: the price of $65.16 against a stock that was $11.32 at the MER closing (Note 4) "just tells us prices"
**[M2006-077]**. No macro enters **[M2000-094]**: the AI power shortage, the grid build-out and oil prices are not
forecast here. Who is paid to tell you: the 2025 and 2026 debt and convertible offerings (three bond deals and two
convertibles in seventeen months) mean a steady flow of sell-side material whose authors are paid on the deals; "don’t ask
the barber whether you need a haircut" **[M2011-083]**, **[M2020-037]**. Margin of safety: "if you have to actually do it
on — with pencil and paper, it’s too close to think about" **[M1996-084]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) for the business: the power segment earned $189.1M of segment Adjusted EBITDA in FY2025 on
$333.5M of revenue, and contracts of seven to ten years (with extension options) were signed in 2025 and 2026 with three
data-center customers, two of them affiliates of investment-grade technology companies (10-K Item 1 and Note 21; 10-Q
MD&A); (2) against it: one customer was 88% of power revenue in FY2025 and 47.3% of all revenue (Item 1, Note 5); the
filer calls its industry one whose "landscape [...] is evolving rapidly" and its markets "characterized by rapid and
significant technological advancements" (Item 1A); customers "may not continue to outsource" and may use the offering "only
as backup power or bridge power until line power is received" (Item 1A); the Hatchbo contract, as first signed, may be
terminated for convenience on 30 days' notice against a payment of 50% of the remaining rent (Note 21; amended in July
2026 into a final operating agreement whose terms were not read).

## THE STANDING RULE
A part-interest bought for cash, unlevered and sized within means, cannot ruin the buyer; the rule binds the buyer's own financing and sizing, not the target: "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**. The target's $3.8 billion of debt after 2026-10-01
is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The question:** "a reasonable fix on about what the earning power and competitive position will look like in five or 10
years" **[M2012-065]**, "can I understand it?" **[M1995-051]**.

**Which part decides (Q1's holding-company paragraph, extended 2026-10-06 to operating segments; Q2's business-of-parts
CONVENTION).** The filer reports two parts with different economics, and "lumping them together [...] impedes analysis" **[L2008-005]**: Solaris Logistics Solutions (wellsite
proppant storage and handling systems rented to oil and gas completions, since 2014) and Solaris Power Solutions
(gas-turbine and engine generation rented behind the meter, mostly to data centers, since the MER merger of 2024-09-11).
The segments report Adjusted EBITDA, not operating profit (10-K Note 5), so the parts' operating profit is estimated.
**CONVENTION of this run:** segment operating profit = segment Adjusted EBITDA less the depreciation and amortization the
filing ties to the part (leasing depreciation and the MER intangible amortization to power, the rest of non-leasing D&A to
logistics), with corporate costs, stock pay and other items allocated in proportion; before 2024 the company had one part.
Rationale: the convention asks for operating profit and the filer reports none by part. Workings:
`Test Runs/_research 2026-10-16 SEI/scripts/parts.py` and `parts_output.txt`.

| part | FY2021-FY2025 operating profit (est., USD M) | share | trailing five years to 2026-06-30 (est.) | share | castle (Q2) | decides |
|---|---|---|---|---|---|---|
| Logistics | 165.1 (2021 -0.4; 2022 41.8; 2023 49.9; 2024 40.4; 2025 33.4) | **59%** | about 184 | about 48% | read at Q2 | **yes, on the fiscal window** |
| Power | 114.4 (2024 12.4; 2025 102.0) | 41% | about 203 | about 52% | not read (non-deciding) | yes on the trailing window |

Check on the segment figure the filer does report, Adjusted EBITDA FY2021-FY2025: logistics about 396, power 216 (logistics
65%). **CONVENTION of this run: the window is the last five fiscal years**, the window Q7's range convention uses and the
last audited one; rationale: the business-of-parts paragraph does not name its window, and a run may not pick the window
by the answer it gives. The trailing reading is carried beside, with what it would decide, below. **Logistics decides.**
Power does not decide on this window, so under the holding-company paragraph it does not "matter" and does not by itself
keep the whole outside the circle.

**The deciding part, logistics, under the tests.**
- "What’s that chart going to look the next 10 years?" **[M1999-132]** A fleet of about 100 to 110 patented silo systems (11 US patents expiring
  2032 to 2044, Item 1) rented by the day to E&P companies and pressure pumpers, with last-mile trucking passed through.
  Its key variables ("trying to identify the key variables in that particular business" **[M1998-044]**) are US completion activity, which the filer says its system count tracks ("our fully
  utilized systems are highly correlated with US land rig count activity over longer periods", FY2022 10-K, accession
  `0001558370-23-003344`), and the price and share it holds against rivals' systems. Completion activity is a commodity
  dependence, which is never by itself a STOP at Q1: "We don’t think we can predict commodity prices." **[M2016-025]**, and "if you can’t make a decision on something like PetroChina off the figures, forget about going further" **[M2008-069]**.
- "do I understand enough about this business so that the financial statements will tell me the information that’s useful to me" **[M2008-033]**? Yes, for this part: eight years of filed history through a
  full cycle (revenue $242M in 2019, $103M in 2020, $320M in 2022, $289M in 2025; operating profit from +$108M to -$60M and
  back), with one product and one customer type.
- Is it among "things that are important and knowable" **[M2006-076]**, and would its insiders "put down on paper their predictions" **[M2000-105]**? The economics of a
  wellsite equipment rental through the cycle are on the record of every oilfield service filer; this is not a field of
  fast-changing technology. "What is important is that I understand the economic dynamics of the industry. [...] Is there
  ease of entry?" **[M2011-014]**: that question is Q2's.
- Doubt **[M2002-092]**: none on what the part is or how it earns; the doubt is on its castle, which Q2 takes.

**The non-deciding part, power, read and recorded (it does not decide on the fiscal window).** Its ten-year economics turn
on how long behind-the-meter generation is needed before the grid arrives, on what three data-center customers' demand
will be, on turbine supply from "a leading supplier" that sells to others (Item 1), and on how many rivals enter. The filer
itself: "The landscape of the distributed power industry is evolving rapidly [...] increased competition from within the
distributed power industry can likely be expected" (Item 1A); its markets are "characterized by rapid and significant
technological advancements" (Item 1A); customers may use it "only as backup power or bridge power until line power is
received" (Item 1A). "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can
judge what its profit margins and returns on capital will be as a host of competitors battle for supremacy." **[L2009-005]**;
"there’s industries we know that may have a wonderful future, but we don’t have the faintest idea who the winners will be"
**[M2012-067]**; "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on
that" **[M1999-063]**. The insiders' own forecast is limited to contracted megawatts and tenors of two to ten years (10-Q
MD&A), with no figure for the fleet after them; of such a forecast the insiders "would not want to put down on paper their predictions" **[M2000-105]**. Were power the deciding part (as on the trailing window),
this question would close here: **TOO HARD (NATURE)**, since no further reading of a filing could say what a turbine rents for in 2036: "the nature of the industry would be the roadblock" **[L1993-023]**; "It just means that we don’t know how to evaluate it." **[M2000-038]**

- **VERDICT: IN**, on the deciding part (logistics), by the business-of-parts CONVENTION on the fiscal window: "a reasonable fix on about what the earning power and competitive position will look like" **[M2012-065]** is had for that part. The power part is recorded as TOO HARD (NATURE) on its own and does not decide on this window; on the
  trailing window it would decide and the file would close here, TOO HARD (NATURE). No reading of either window makes the
  file IN at the end of Q2 (see Q2).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The question:** "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. Asked of the deciding part, logistics (parts table at Q1).

**The castle tests, on the logistics part, each with its filing fact.**
- **The attacker with money:** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?" **[M2011-015]** The attackers are already inside. FY2025 10-K Item 1A: "We face competition
  from proppant producers, pressure pumping companies and proppant transporters who also offer solutions for unloading,
  storing and delivering proppant at well sites [...] Some of our competitors have greater financial and other resources";
  Item 1: "Some of these companies could be customers of ours on certain jobs while also utilizing their own equipment and
  integrated service offerings on other jobs." A customer that can own the equipment, and rivals that sell sand and
  delivery together, are the "there are some industries that are just never going to have barriers to entry" case
  **[M2012-106]**. The patents (11 US, expiring 2032 to 2044) do not close it: "no single patent or trademark is critical to
  our business" (Item 1), and "competitors or others could independently develop the same or similar technologies" (Item 1A).
- **Pricing power, and the price through the last inflation:** "the agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. Adjusted EBITDA per fully utilized system,
  from the filer's 10-Ks: 2018 about $1.1M (Adjusted EBITDA $123M, about 110 systems); 2019 about $1.0M ($112M, 110);
  2020 about $0.6M ($25M, 45 systems, a 59% fall in systems in one year); 2023 $1.06M (segment $115.1M, 109); 2024 $1.07M
  ($97.6M, 91); 2025 $0.96M ($88.9M, 93); first half 2026 $0.91M annualized ($48.0M, 105). Across 2021 to 2025, years of
  general cost inflation, the profit per system fell; the filer's logistics cost of revenue rose from 64% to 69% of revenue
  in 2025 (10-K MD&A). Competition "is thus based on price, consistency and quality of products" (Item 1A). No sign of the
  power to pass costs through.
- **The low bid:** "it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**; here, on the filer's own words, it is. The customers are E&P companies and pressure
  pumpers buying a service under master service agreements with work orders job by job (Item 1); one customer was 28% of
  the segment in 2025. The rows' failing answer fits: "most insureds don't care from whom they buy" **[L2004-003]**.
- **Unit volume, and the moat** "likely to widen further or shrink on you" **[M1999-108]**. Fully utilized systems: about 110 in 2018 and 2019, 45 in
  2020, 57 in 2021, 95 in 2022, 109 in 2023, 91 in 2024, 93 in 2025, 105 in the first half of 2026. Segment Adjusted EBITDA
  fell three years running ($115.1M, $97.6M, $88.9M) and segment revenue fell 15% in the first half of 2026 (10-Q MD&A).
  The filer: "The market for supply chain management and well site logistic services is becoming increasingly
  competitive" (Item 1A). The moat, if any, is narrowing.
- **The low-cost position:** "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**, measured "more by cost of production" **[M2006-004]**: the filer claims none in its own words; its stated factors
  are "equipment reliability, technical expertise, patent-protected technology [...] and price" (Item 1). No filing read
  shows a cost advantage over the rivals below.
- **Ask the competitors**: the rivals' own filings are the evidence used (row below); no other source read.
- **What could** "destroy, or modify, or reduce the economic strengths" **[M2000-014]**: customer consolidation and "industry efficiency gains"
  (10-K MD&A), and the integrated sand-and-delivery offerings of the sand producers.

**The competitor row.** The 10-K names no competitor by name, only kinds (proppant producers, pressure pumpers, proppant
transporters). **CONVENTION of this run:** the rivals read are SEC filers of each named kind: Smart Sand (SND; proppant
producer with its own wellsite storage systems), U.S. Silica (SLCA; proppant producer with its own container system; filed
10-Ks through FY2023 and then stopped, so its span ends there), ProPetro (PUMP) and Liberty Energy (LBRT) (pressure
pumpers), and Atlas Energy Solutions (AESI; proppant producer and last-mile delivery; public from 2023). Rationale: the brief
asks for named rivals and the filing names kinds only. Metric: pre-tax operating income over total assets less goodwill and
intangibles, summed over the span (each filer's own 10-K XBRL facts; workings in
`Test Runs/_research 2026-10-16 SEI/scripts/peers.py`, `scripts/field.py`, `field_output.txt`):

| filer | span | pre-tax operating income / tangible assets | latest 10-K accession |
|---|---|---|---|
| SEI (then SOI), logistics only | 2017-2023 | **9.3%** (6.4% peak 2019 to peak 2023; -15.1% in 2020, -0.1% in 2021) | `0001697500-24-000023` |
| Smart Sand (SND) | 2017-2025 | 0.2% | `0001529628-26-000006` |
| U.S. Silica (SLCA) | 2017-2023 | 0.0% | `0001524741-24-000007` |
| ProPetro (PUMP) | 2017-2025 | 2.3% | `0001680247-26-000028` |
| Liberty Energy (LBRT) | 2017-2025 | 9.9% | `0001694028-26-000006` |
| Atlas Energy Solutions (AESI) | 2022-2025 (short; falls from 30.9% to -0.6%) | 10.5% | `0001193125-26-067145` |

**The field's returns over the last full cycle, judged in words** (CONVENTION of section C, no figure): the logistics part
earned about 9% before tax on its tangible assets across the cycle 2017 to 2023, about 6% from peak to peak, with two
years of losses and a $47.8M impairment in 2020; it did so in a field whose other durable players earned between nothing and
about 10% before tax over the same years. That is an ordinary return at best, roughly 7% after tax at the company's
effective rate, in a field that is poor. The high returns of 2018 and 2019 (22% to 25%) did not hold through the next
downturn and have not come back. "A truly great business must have an enduring "moat" that protects excellent returns on
invested capital." **[L2007-004]**; "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**.

**The parts table** is at Q1 (logistics decides on the fiscal window, 59% estimated). The power part does not decide on
that window and its castle is not judged here; its facts are under AFTER THE STOP.

**The castle, shown open.** On the evidence: customers who can own the equipment and rivals who bundle it with sand and
delivery; price set by competition, with profit per system falling through the inflation; volume and segment profit
falling; ordinary returns through a full cycle in a poor field. This is not the tenuous moat of which the rows say "We don’t know how to valuate that" **[M2000-019]**: the returns are known, and the section C CONVENTION sends a field "whose durable players earn ordinary
returns over a full cycle, on the evidence of the filer's and the rivals' own filings" to OUT, not TOO HARD. "If the answer
had been yes, we wouldn’t have done it." **[M2011-015]**

- **VERDICT: OUT**, on the deciding part (logistics): a castle open on the evidence and protecting only ordinary returns
  over the full cycle; the rows ask for a moat "that protects excellent returns on invested capital" **[L2007-004]**, and "If the answer had been yes, we wouldn’t have done it." **[M2011-015]** The file closes
  here. Beside it (not deciding the box): on the trailing window the power part decides and the file closes at Q1, TOO HARD
  (NATURE); no window makes the file IN.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The "balance sheets over an 8 or 10 year period" **[M2025-032]** were read in Step 0; other facts under
AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded, not judged, under AFTER THE STOP; a later run that reaches Q5 must answer
them: "If you’ve got doubts, forget it." **[M2013-088]**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (The buyback line Q6 asks of Q7's bottom is written under AFTER THE STOP as a fact, beside the COMPUTATION.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a clearance. The range and the fair price are computed beneath the stop, at the owner's request, under
COMPUTATION, NOT A CLEARANCE below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Debt facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. No named business of Q12 (casinos, tobacco, loading schemes) is involved.

---
## THE BOX
**OUT at Q2** (the deciding part, logistics, on the fiscal five-year window: a castle open on the evidence that protects only
ordinary returns over the full cycle); integrity facts recorded, not judged. Beside it, not deciding: on the trailing
five-year window the power part decides and the file closes at Q1, TOO HARD (NATURE). COMPUTATION beneath the stop: value
range about -$16.4 to -$16.3 a share on the all-equity basis (equity-only $6.0 to $6.1) against $65.16; no case earns the
floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found ("write it down in the first 30 minutes" **[M1997-127]**); no verdict; the box unchanged (operator rule 2).

**Bearing on Q3 (capital in, earnings out).**
- Capital spending: $64.4M (2023), $188.4M (2024), $646.8M (2025), $835.2M in the first half of 2026, "approximately $1
  billion" more expected in the rest of 2026 (10-Q MD&A); purchase commitments of $896.9M due within twelve months and
  $580.3M after, cancellable at penalties of 5% to 90% (10-Q MD&A). Power capacity planned to reach about 3,200 MW by the end
  of 2029, mostly contracted for two to ten years with extension options (10-Q MD&A).
- Growth spending and what it bought, 2021 to 2025: capital spending above depreciation plus cash paid for businesses,
  $926.5M; the rise in maintenance-basis owner cash between the first and last two years, $51.6M a year: about 5.6% after
  tax on the spending (workings `q7_output.txt`). Much of the 2025 spending had not yet reached revenue at year-end.
- Power segment costs include "Equipment rental" of $85.9M in 2025 and $52.4M in the first half of 2026 (10-K Note 5; 10-Q
  segment note): part of the fleet is rented in from others.
- Turbine engine cores are depreciated on units of production (10-K Note 2).

**Bearing on Q4 (the accounts).**
- The filer manages and pays on Adjusted EBITDA: segments are reported on it (Note 5), and the 2025 annual incentive uses
  "EBITDA, free cash flow, customer consistency, fully utilized systems deployed and market share" (DEF 14A).
- Losses on debt extinguishment of $4.1M (2024), $41.5M (2025) and $16.1M (first half 2026): three refinancings in under two
  years. Cash taxes paid $0.8M in 2025 against a $14.7M provision; deferred tax assets $99.1M at 2026-06-30; a Tax
  Receivable Agreement pays 85% of certain realized tax savings to the TRA holders, payable $109.2M at 2026-06-30 (10-Q
  balance sheet; 10-K Note 17).
- Convertible-note accounting was the auditor's critical audit matter (BDO, FY2025 10-K).
- HVMVLV's internal controls were excluded from the FY2025 assessment (Item 9A), as the SEC permits for a new acquisition.

**Bearing on Q5 (integrity facts, recorded, not judged).**
- A short-seller report by Morpheus Research dated 2025-03-17 made allegations the company calls "misleading" (Item 1A); a
  securities class action (Pirello, S.D. Tex., filed 2025-03-28) alleged misleading statements and omissions "relating to
  the MER Acquisition"; the lead plaintiff dismissed all claims voluntarily **without prejudice** on 2026-02-17; two
  shareholder derivative suits (Saint-Phard, Kaszirer) were dismissed voluntarily without prejudice on 2025-12-29 and
  2026-01-05 (10-K Note 19). No finding against the company was found; the allegations themselves were not read.
- Related parties (10-K Note 20; DEF 14A): Solaris Energy Management, owned by the Chairman and Co-CEO, bills office, travel
  and administrative services ($0.7M in 2025); THRC Holdings (10.4% holder until 2024) was affiliated with customers and
  suppliers, including a last-mile logistics supplier; KTR Management, holder of 13.0% of the Class B shares after the MER
  merger, leased property and sold equipment to the company "at cost with no markup"; BlackRock, then a 5% holder, bought
  $55M of the 2030 Notes and $120M of the 2031 Notes with audit-committee approval; the Omega seller's affiliate leases
  property to Omega under a new master lease (8-K 2026-09-08).
- The charter lets the "Designated Parties" (Yorktown, Wells Fargo Central Pacific Holdings, and the non-employee directors,
  the risk factor naming William A. Zartler among those not restricted) compete with the company and keep corporate
  opportunities (Item 1A).
- The largest customer of the power part (88% of its 2025 revenue) is also the 49.9% partner in Stateline, which rents to it
  (10-K Note 3). The new Co-CEO, the new CFO and a 2025 director all came from Aris Water Solutions, where the Chairman was
  executive chairman (Item 1).
- A patent suit by Masaba against the company ended when the PTAB held all claims of Masaba's patent unpatentable, final
  2026-07-14 (10-Q Note 18).

**Bearing on Q6 (the money and the owners).**
- Shares (Class A plus Class B) from about 43.0 million (cover of the FY2023 10-K, early 2024) to 80.2 million (2026-09):
  +86% in about two and a half years, through the $160.9M offering (2024) and stock paid for MER (16,464,778 units),
  HVMVLV (696,028), Genco (4,182,772), GESA (2,880,682) and Omega (3,599,199). The 2030 and 2031 convertibles convert at about
  $26.39 and $57.20 a share (10-K Note 12), both below $65.16: about 18.9 million more shares on conversion, before the
  capped calls. The rows' line on serial issuance is recorded here as the place a later run must read it: "we have never
  invested in companies that are hell-bent on issuing shares" **[L2014-015]** (a candidate second STOP at Q6, OPEN in the
  framework).
- MER merger: $186.4M in units at $11.32 plus $136.7M of cash and capital-spending reimbursement (Note 4), the larger part
  paid in shares, so a merger in the speakers' usage; GESA, Genco and Omega were paid mostly in shares.
- Buybacks: 4,272,127 shares retired for $34.6M ($8.09 average) under a $50M program of 2023 with no stated price; none
  since 2024 (10-Q MD&A). Q6's line against Q7's bottom: the prices paid sit above the bottom of the computed range below
  (about -$16.4 a share), which is negative.
- Dividends: $0.12 a quarter on Class A and the same distribution to OpCo units, paid while capital spending is funded by
  debt (10-K Note 21; cash-flow statement).
- Pay (DEF 14A, accession `0001140361-26-012799`): the Chairman and Co-CEO's total pay was $13,870,354 in 2025 against
  $3,820,166 in 2024, of which $12,574,354 in stock awards; the long-term awards are performance equity on absolute and
  relative total stockholder return; the new Co-CEO received a sign-on stock grant valued at $6,770,000. The Chairman is also
  Co-CEO.

**Bearing on Q9 (debt and exposures).**
- Debt at face, 2026-06-30: 6.375% Senior Notes due 2031 $1,300.0M; convertibles $902.5M (2030 and 2031); Stateline term loan
  $339.7M (non-recourse to the parent, Note 3), $360.7M after a July draw; finance leases $5.5M. Cash $824.1M plus $70.7M
  restricted. On 2026-10-01, $1,250M more of 7.000% Senior Notes due 2032, and the revolver raised to $850M (8-K
  `0001193125-26-410682`). Gross debt after that, about $3.8 billion, against FY2025 operating income of $135.4M.
- The power part depends on one leading supplier of generation equipment (Item 1) and on three data-center customers; the
  Hatchbo contract as first signed could be ended for convenience on 30 days' notice for 50% of the remaining rent (Note
  21); the July 2026 final agreement was not read.
- The logistics part's revenue moves with US completion activity; the 2020 fall in systems was 59% in one year.

## COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price (reporting convention; the owner's request; Part VII)
*Beneath a closed STOP; no entry language; nothing here is a verdict (operator rule 3). Workings:
`Test Runs/_research 2026-10-16 SEI/scripts/q7.py` and `q7_output.txt`.*

- **Owner cash, after every real cost (USD M).** All-spending (OCF less stock pay, capital spending, finance-lease principal
  and cash paid for businesses, plus disposal proceeds; plus net cash interest after tax at 21% for the all-equity basis):
  2021 -8.4; 2022 -21.1; 2023 19.3; 2024 -251.4; 2025 -477.7; **five-year average -147.8** (the literal window).
  Maintenance-only, by specific (e), the depreciation charge taken as the maintenance guess, "not inappropriate in most
  companies to use as a proxy for required capital expenditures" **[M1998-127]** (the filing states logistics capital
  spending of $7.0M in 2025 and calls the power spending growth): 2021 -16.0; 2022 29.9; 2023 45.1; 2024 6.5; 2025 110.6;
  **average 35.2** all-equity, 30.7 after interest (equity-only). Working capital is inside OCF (specific (d)). Tax: cash
  taxes as filed; the deferral and the TRA are not priced separately (this flatters the figure; see the gaps paragraph).
- **Growth shown.** The maintenance series changes sign, so growth is measured between halves (specific (b)): 6.9 (2021-22)
  to 58.5 (2024-25), 103.5% a year. **The cap (f):** carried ten years that would require owner cash of about $43 billion
  against about $3.3 billion at the best share of sales the filings show (17.8%, 2025); cut to the business's own sales
  growth (40.6% a year, 2021 to 2025), never above the discount rate: **5.43%**.
- **Growth spending charged (specific (e)).** The growth was bought at about 5.6% after tax on $926.5M of growth spending
  and purchases; the growth case is charged the spending at that rate. At 5.43% the growth case sits just above the
  no-growth case; at 10% it sits below it (growth that does not earn the floor), so at the fair price the no-growth case is
  the top.
- **Acquisitions (specific (c)).** MER (2024) was paid mostly in units, a merger by the speakers' usage; its own pre-merger
  record (8-K/A of 2024-11-18) was not read, and MER was capital-heavy before the closing ($77.1M of its spending was
  reimbursed). Net purchases over the window exceed half of owner cash before purchases, so the serial-acquirer
  CONVENTION would put the organic pair central; the filer reports no organic growth figure. Genco (2026-03), GESA
  (2026-07) and Omega (2026-09), closed after the window, are credited at nothing (no earnings filed; Genco "not
  significant", 8-K/A `0001193125-26-201448`), their cash added to net debt and their shares to the count. None of this can
  move the result by the amount below.
- **Cycle (a).** The first window year, 2021, is the trough; the 2019-2023 cycle average of maintenance owner cash is 30.9,
  close to the window's 35.2; it changes nothing below.
- **Net debt and claims, all-equity basis.** Face debt at 2026-06-30 $2,547.7M less cash $824.1M (restricted cash left out
  as not free), plus the subsequent events the 10-Q states (GESA cash $52.4M; Stateline draw $21.0M) and the Omega cash
  ($77M): **$1,874.0M**. MZX's 49.9% of Stateline, $86.0M at book, deducted. Operating leases and the $109.2M TRA payable left
  out (said so). The $1,250M notes of 2026-10-01 add cash and debt alike and are not added.
- **VALUE RANGE (all-equity, the central figure): about -$16.4 to -$16.3 a share** (no-growth -$16.36, growth-charged
  -$16.26; 80,165,591 shares) against **$65.16**. Equity-only beside it: $5.98 to $6.07 a share (owner cash after the window's
  interest; the interest now running is far higher: about $83.6M a year on the 2031 Senior Notes alone, 10-Q MD&A). If the
  convertibles were counted as shares instead of debt, the all-equity figure is still below zero.
- **The floor, tested first:** at $65.16 the business is priced at about $7,184M including net debt and the minority; ten
  percent of that is $718M a year of owner cash against a five-year average of $35.2M. **No case earns the floor at the
  price**; the width test does not arise.
- **FAIR PRICE (reporting figure, Part VII): about -$20.8 a share on the all-equity basis** (each end valued at 10%: -$20.06
  no-growth, -$21.49 growth-charged; averaged), after the company's own tax; **equity-only beside it: about $2.1 a share**
  ($2.76 and $1.51 averaged). The all-equity figure is the central one.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `fb099ef8`); written question by question; committed after Step 0,
      Q1, Q2 and the close (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not checked
      or touched here); the fold into the register is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched after the run began; the one
      directory listing of `Test Runs/` before the copy, the commit subjects and the `git status` lines in the opening
      context are declared under CONTAMINATION and were not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (43 distinct ids); every quoted fragment beside an id is in that
      row (`scripts/citecheck.py`: 42 fragments, PASS); no E-ids. Filing facts carry their document; accessions are listed
      in Step 0 and beside the competitor row. Two numbers rest on this run's own estimates, labelled CONVENTION: the
      parts' operating profit and the rivals chosen.
- [x] The order was kept; Q2 closed the run; everything after it is NOT REACHED, AFTER THE STOP, or COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (OCF less stock pay, capital spending, finance-lease principal and purchases; the
      maintenance case on depreciation as the stated guess), never a net-income proxy; the sovereign from the Treasury;
      the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (Foundations; AFTER THE STOP); the integrity flag is in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used (its stale share line rejected).
- [x] `python tools/check_framework.py` PASS (2026-10-16, before the closing commit); `scripts/citecheck.py` PASS.
- Honest notes: (1) the segment operating-profit split is an estimate, and the deciding part turns on the window chosen;
  the box does not (OUT on one window, TOO HARD (NATURE) on the other, never IN). (2) The MER pre-merger statements
  (8-K/A of 2024-11-18), the Morpheus report itself, the July 2026 Hatchbo final agreement and the GESA and Omega target
  financials were not read. (3) 2021 and 2022 interest paid was not read (debt under $10M then; taken as nil). (4) The
  company's 2020 impairment is counted inside 2020 operating income in the logistics returns.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The business-of-parts CONVENTION (Q2, section B, extended to Q1) decides by "more than half of the company's five-year
operating profit" but names neither the window nor the measure when a filer reports segment Adjusted EBITDA and no segment
operating profit. Here both mattered: on the last five fiscal years the shrinking logistics part decides (about 59% of
estimated operating profit, 65% of reported segment Adjusted EBITDA), while on the trailing five years to the last 10-Q the
power part decides (about 52%), and by every forward measure (80% of segment Adjusted EBITDA in 2026, 87% of segment
assets, nearly all capital spending and all of the $3.8 billion of debt) power is the business being bought. A
backward-looking threshold therefore let a part that is now a fifth of the company carry the box, and made the part that
the buyer's money would actually own "not matter" at Q1. I chose the fiscal window as a CONVENTION of this run (the window
Q7's range uses, and audited), estimated segment operating profit by allocating D&A and corporate costs, showed the
trailing reading beside it, and found that the box is closed either way (OUT at Q2, or TOO HARD (NATURE) at Q1). A rule is
needed for a company in transformation: which window, which measure, and whether a part that carries most of the capital
employed and the debt "matters" at Q1 whatever its past profit. Second: the convention says what to do with a non-deciding
part that is open (carry it to Q7 at no growth) but not with a non-deciding part whose future cannot be judged. Third,
at Q7: specific (e) says to charge growth spending "against the growth it buys" but gives no method; I charged it at the
after-tax return the window's growth spending actually earned (about 5.6%), which is a CONVENTION of this run. Fourth:
"Whose tax" prices a carryforward separately but says nothing of a Tax Receivable Agreement that hands 85% of the tax saving
to former owners; the computation leaves both the deferral and the TRA unpriced and says so.
