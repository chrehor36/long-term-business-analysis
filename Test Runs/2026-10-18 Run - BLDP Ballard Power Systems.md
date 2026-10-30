# Company Run: Ballard Power Systems Inc. (Nasdaq and TSX: BLDP), 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
941a2ff0).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (3018c93c):** not held; Ballard Power Systems (BLDP) does not appear in `PORTFOLIO.md`.

**Dispatched run.** Written by a dispatched analyst under the brief of 2026-10-18 (operator rule 10). The brief's one stated
departure from `Screens/_daily/_dispatch_brief.md`: the lines of evidence were derived by the analyst from the filing (below).

**Contamination, declared.** (1) The session context showed the repository's recent commit subjects (another company's v5
re-run and fold) and the git status file list (research folders of other companies by ticker). Neither concerns this name;
not used. (2) The session context carried a memory index line on the queue's state (counts of gate-clearers, nothing about
this name); not used. (3) Before creating this file I ran a directory listing of `Test Runs/` filtered for "bldp" or "ballard"
to check that the dated file name was free; it returned no match, so no file about this company was seen, but the listing
was a search of `Test Runs/` that the blind rule forbids, and it is declared here. Nothing else on the blind list was opened,
listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.57, close 2026-10-16 (Nasdaq; Yahoo Finance chart feed via `tools/sources.py`, an AGGREGATOR, flagged per
  operator rule 5; live quote only). For scale only: the GeoPura shares were issued at US$5.02, "based on Ballard's 30-day
  volume-weighted average share price" (6-K 2026-06-23, accession 0001279569-26-000579).
- **Shares by class:** one class, common shares. Cover of the 40-F for FY2025 (filed 2026-03-12, accession
  0001628280-26-017045): 300,784,816 (`python Screens/cover_shares.py BLDP`). Checked against the filed statement of changes in
  equity, balance at 2025-12-31: 300,784,816; no treasury shares are reported. Since: 301,506,494 at 2026-06-30 (interim
  statements, 6-K filed 2026-07-31, accession 0001628280-26-051245); then, at the GeoPura closing on 2026-08-28, "49,584,212
  newly issued Ballard common shares and restricted share units which will be settled in 12 months for an additional
  1,084,540 Ballard common shares" (6-K 2026-08-28, accession 0001279569-26-000834). Count used: 301,506,494 + 49,584,212 +
  1,084,540 = **352,175,246** (the RSUs are deal consideration and are counted; without them 351,090,706). Options and other
  RSUs outstanding are not added (CONVENTION of this run: the count is shares issued plus shares owed as deal consideration;
  rationale: the brief asks for the cover count checked against later filings, and the dilution of the stock plans is small
  beside the result below).
- **Market cap:** 352.18M x $1.57 = **$552.9M**.
- **Sovereign for the earnings currency:** the statements are "Expressed in thousands of U.S. dollars" (40-F FY2025). USD:
  **5.43%**, US Treasury daily par yield curve, 30-year, 10/16/2026 (`tools/sources.py`, issuing authority, not the fallback).
- **Filings read** (operator rule 4): the 40-F for FY2025, filed 2026-03-12, accession 0001628280-26-017045: the Annual
  Information Form (exhibit 99.3, `ballard993123125annualinfo.htm`), the MD&A (exhibit 99.2), the audited statements
  (`bldp-20251231.htm`, KPMG report dated March 11, 2026). The 40-F for FY2023 (filed 2024-03-11, accession
  0001453015-24-000002, statements) and the 40-F for FY2021 (filed 2022-03-14, accession 0001453015-22-000003, statements).
  Interim statements for Q2 2026 (6-K 2026-07-31, accession 0001628280-26-051245, exhibit 99.1, including note 25, subsequent
  event). The management proxy circular for the 2026 meeting (6-K 2026-04-24, accession 0001206774-26-000242, exhibit 99.1).
  Every 6-K news release of 2026 (accessions 0001279569-26-000125, -000207, -000211, -000286, -000292, -000371, -000373,
  -000395, -000453, -000506, -000549, -000579, -000630, -000723, -000834, -000942, -000957). Not read: the Q1 2026 interim
  statements (6-K 0001628280-26-030150; the Q2 statements carry the year to date), the 6-K of 2026-07-07 (accession
  0001206774-26-000351, a 2 MB exhibit 99.2 not opened), the FY2016 to FY2020 40-F texts (their figures are taken from the
  tagged data below).
- **One figure cross-checked against the filed statement:** cash used in operating activities FY2025, $(56,167) thousand in
  the filed cash-flow statement, against $(56.2)M in the tagged data. Further checks: FY2021 cash $1,123,895 thousand and
  operating cash $(80,476) thousand (FY2021 statements) match the tags; FY2022 and FY2023 operating cash $(132,171) and
  $(104,570) thousand and capital additions $33,932 and $41,214 thousand (FY2023 statements) match. One tag differs:
  FY2021 total equity is $1,328,217 thousand in the filed statement against $1,327.0M tagged; the filed figure is used.
- **`python tools/run.py BLDP`:** printed "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." It does not read the
  IFRS taxonomy of a 40-F. Every figure in this file is taken from the filed statements or, for 2016 to 2020 and where marked,
  from the issuer's own tagged IFRS facts in the 40-Fs (SEC companyfacts), and is said so.

**The lines of evidence this name needs, derived from the filing** (the brief's departure): from the AIF's Our Business,
Strategy and Our Markets, Products and Services: what is sold (MEAs, stacks, modules, engineering services) and to whom
(OEMs and system integrators in bus, rail, marine, truck, stationary); from its Competition section: the named rivals and the
substitute technologies; from its Impact of Regulations and Public Policy and its Recent History: the dependence of demand on
subsidy and mandate, the restructurings, the abandoned capacity; from its Risk Factors: the company's own statement of
whether its economics can be forecast; from the MD&A and statements: revenue, gross margin, cash burn and the balance sheet
over ten years; from the 2026 6-Ks: the GeoPura deal and the stated profitability objective.

### The balance sheets first, ten years (read here because the file closes before Q4) [M2025-032]
USD millions at 31 December. 2021, 2023, 2024 and 2025 from the filed statements named above; the other years are the issuer's
tagged IFRS facts in its 40-Fs.

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Cash and equivalents | 72.6 | 60.3 | 192.2 | 147.8 | 763.4 | 1,123.9 | 913.7 | 751.1 | 603.9 | 527.1 |
| Receivables | 14.9 | 23.1 | 38.5 | 49.3 | 56.8 | 46.4 | 48.7 | 58.6 | 32.0 | 24.2 |
| Inventories | 17.2 | 17.3 | 29.3 | 30.1 | 28.5 | 51.5 | 58.0 | 45.9 | 56.4 | 43.8 |
| Goodwill | 40.6 | 40.6 | 40.3 | 40.3 | 40.3 | 64.3 | 64.3 | 40.3 | 0.0 | 0.0 |
| Other intangibles | 18.1 | 17.9 | 8.3 | 5.7 | 3.8 | 20.8 | 5.2 | 1.4 | 1.8 | 0.2 |
| Total assets | 183.4 | 177.7 | 346.1 | 340.3 | 975.6 | 1,440.9 | 1,247.1 | 1,077.5 | 777.3 | 682.4 |
| Lease liabilities | n/a | n/a | n/a | 19.7 | 17.9 | 17.1 | 15.7 | 17.9 | 23.9 | 22.1 |
| Share capital | 977.7 | 986.5 | 1,174.9 | 1,182.7 | 1,884.7 | 2,416.3 | 2,420.4 | 2,425.6 | 2,428.6 | 2,433.2 |
| Accumulated deficit | (1,149.1) | (1,157.4) | (1,184.4) | (1,223.8) | (1,275.5) | (1,387.6) | (1,560.8) | (1,737.5) | (2,060.8) | (2,151.8) |
| Total equity | 121.5 | 119.9 | 282.6 | 250.3 | 900.9 | 1,328.2 | 1,158.9 | 991.2 | 673.0 | 589.9 |
| *Revenue (for the ratios)* | 85.3 | 121.3 | 96.6 | 105.7 | 103.9 | 104.5 | 81.9 | 102.4 | 69.7 | 99.4 |

**What moved and why.** Every dollar of equity on these balance sheets came from shareholders, not from earnings: share
capital rose from $977.7M to $2,433.2M ($1,455.5M in ten years; net proceeds of equity offerings were $694.6M in 2020 and
$527.3M in 2021 per the FY2021 cash-flow statement, $183.7M in 2018 per the tags) while the accumulated deficit deepened from
$1,149.1M to $2,151.8M, a loss of about $1.0B over the decade. The cash pile is the residue of the 2020 and 2021 offerings and
has been drawn down every year since 2021, from $1,123.9M to $527.1M, and to $502.1M at 2026-06-30. Goodwill from the
acquisitions was written off ($40.3M in 2024, "Impairment charges on goodwill", FY2025 statements); $111.0M of property,
plant and equipment was impaired in 2024. There is no borrowing; the only debt-like item is leases. Inventories ran 20% of
sales in 2016 and 44% in 2025 (56.4 against 69.7, or 81%, in 2024); receivables reached 57% of sales in 2023 and a $13.4M
impairment of trade receivables was taken in 2024 (FY2025 cash-flow statement). Revenue was $85.3M in 2016 and $99.4M in
2025, never above $121.3M (2017) in the decade. "what the figures are saying and what they don’t say" **[M2025-032]**: they
say a business that has consumed capital in every year shown, whose sales did not grow over ten years; they cannot say
where the economics will be in ten years, which is the question Q1 asks.

**Owner cash, recast (operator rule 5; a COMPUTATION, not a clearance; feeds the reporting figures only).** Operating cash
less additions to property, plant and equipment, less intangible additions, less stock pay (added back in operating cash and a
real cost), less lease principal. Investment income on the cash is inside operating cash and is removed for the all-equity
basis. USD millions; 2021 to 2025 from the filed statements (2021 capital additions, intangibles, stock pay and lease
principal from the tags).

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Cash used in operating activities | (80.5) | (132.2) | (104.6) | (108.1) | (56.2) |
| Additions to PP&E | 13.2 | 33.9 | 41.2 | 25.8 | 9.8 |
| Intangible additions | 1.5 | 0.6 | 0.2 | 1.8 | 0.3 |
| Stock pay | 9.7 | 9.4 | 11.0 | 7.5 | 6.3 |
| Lease principal | 2.8 | 3.3 | 4.0 | 3.3 | 3.0 |
| **Owner cash, equity-only** | **(107.7)** | **(179.4)** | **(161.0)** | **(146.5)** | **(75.7)** |
| Investment income (interest on the cash) | 4.0 | 19.6 | 43.3 | 36.9 | 24.5 |
| **Owner cash before interest income, all-equity** | **(111.7)** | **(199.0)** | **(204.3)** | **(183.4)** | **(100.3)** |

Five-year averages: **$(134.1)M** equity-only, **$(159.7)M** all-equity. Not deducted, and shown beside: contributions to the
hydrogen infrastructure funds ($51.8M, 17.9, 11.9, 12.0, 8.7) and to the Weichai-Ballard JV ($12.4M in 2021, $9.3M in 2022),
which are investments carried as assets; the JV paid no dividend found and was fully impaired in Q4 2025 (AIF, Recent
History). Income tax paid is negligible (expense $0.1M in 2025); there is no tax to shelter. Depreciation was $4.1M in 2025
against $9.8M of additions, after the 2024 impairments. Half-year 2026: operating cash $(19.2)M and additions $1.4M (Q2
interim statements), the smallest burn in the window, before stock pay, lease principal and the GeoPura business.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, and the business has never produced the cash that would let an owner answer yes without relying on the next
issue of shares (the balance sheets above). The market serves, it does not instruct: the price has run from $2.30 (2026-03-30)
to $6.29 (2026-05-29) and back to $1.57 (aggregator, flagged) without anything in the filings changing at that speed; that is
quotation, not information. Who is paid to tell you: the stated objective of "achieving profitability by the end of 2027" (6-K
2026-07-31) and the GeoPura release's "path to profitability by 2028" and "US$25 million in annual run-rate EBITDA synergies"
(6-K 2026-06-23) are a seller's projections; the speakers "never looked at a projection in connection with either a security"
they bought **[M1995-050]**, and one does not "ask the barber whether you need a haircut" **[M2011-083]**. **Contrary
evidence, written down as found** **[M1997-127]**: (a) four consecutive quarters of positive gross margin to Q2 2026 (20% in
Q2, 6-K 2026-07-31) after three years of negative gross margin; (b) the largest single bus order in the company's history, 500
engines and 50 MW from New Flyer (6-K 2026-03-10), and selection by Solaris and Wrightbus for their next-generation buses (6-Ks
2026-05-05 and 2026-05-06); (c) no debt and about $505M of cash and short-term investments at 2026-06-30 against a market value
of about $553M; (d) a cost base cut about 30% twice (AIF, Recent History). Each is evidence about the next few years; none is
evidence about where the economics will be in ten.

## THE STANDING RULE
A cash purchase of a part-interest, unlevered, sized so that its loss would not touch what the buyer has and needs, carries no
ruin for the buyer: "We are never going to risk what we have and need" **[M2012-081]**; "Never risk permanent loss of
capital." **[L2023-005]**. Nothing in the target puts the buyer at risk of sudden demands **[L2014-024]**; its own ruin risk
is the target's, and belongs to Q9 (not reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10 years"
**[M2000-037]**, "a reasonable fix on about what the earning power and competitive position will look like in five or 10
years", with "some notion of how the industry will develop and where the company will stand within the industry"
**[M2012-065]**. Knowing the product is not enough: it is "the predictability of the economics of the situation 10 years out"
**[M2000-104]**. The product here is plain (a PEM stack turns hydrogen and air into electricity; AIF, Our Business). The
economics are the question.

**The key variables and whether they are foreseeable** **[M1998-044]**. From the filing, the economics of this business in ten
years turn on four things, none of which the filing or anyone in the industry claims to know:
1. **Whether hydrogen fuel cells or batteries win heavy mobility.** The AIF's Competition section: "The recent developments in
   battery-powered powertrain vehicles have created a zero-emission alternative to fuel cell buses in the form of battery
   electric buses and commercial trucks, as well as electrified trains and battery-powered marine vessels", and hydrogen
   combustion engines from Cummins and JCB are emerging beside them. The Risk Factors: "Some of these technologies are as
   capable of fulfilling existing and proposed regulatory requirements as the PEM fuel cell." This is a forecast about
   technology, not about customer habit **[M2017-019]**.
2. **Whether the subsidies and mandates that create the demand survive.** The AIF says its markets "rely on centralized fueling
   depots that simplify the hydrogen infrastructure requirements and are typically government-subsidized, thus enabling the
   purchase of pre-commercial fleets"; the US DOE awards of about $40M were "subsequently terminated in 2025"; the Texas
   Gigafactory was abandoned; CARB's rules face "ongoing legal and political challenges" (AIF, Recent History and Impact of
   Regulations). The truck market "is at a nascent phase typified by demonstration projects".
3. **The price and availability of hydrogen and its fuelling network.** "Adequate investment in hydrogen fueling infrastructure
   and competitive pricing of hydrogen fuel is beyond our control." (Risk Factors.) "We believe there is a multi-year push-out
   of the hydrogen and fuel cell industry" (Risk Factors).
4. **Who the winners among the fuel cell makers will be.** The AIF names thirteen developers for heavy mobility (Sinohytec,
   cellcentric, Cummins, EKPO, Hyundai, Honda, Plug Power, Powercell, Bosch, Re-Fire, Sino-Synergy, Symbio, Toyota) and
   expects "further industry rationalization, failures, restructurings and consolidation"; "Many of our competitors have
   substantial financial resources [...] which give them significant competitive advantages over us."

**The tests.**
- *Where will it be in ten years?* **[M2000-037]** Ten years of the filed record do not narrow it: revenue $85.3M in 2016 and
  $99.4M in 2025, gross margin positive to 2021, negative 2022 to 2024 ($(22.0)M in 2024), positive again in 2025 ($5.5M); a
  net loss in every year of the ten (tagged data; FY2025 statements). The company's own words: "We may never become
  profitable." and "We cannot predict with certainty our future revenues or results from our operations." (Risk Factors.)
- *Do the past statements tell me the future ones?* **[M2008-033]** No: the statements record a pre-commercial market whose
  volume is set by policy and pilot fleets; "the financial statements will tell me the information" **[M2008-033]** only of a
  business whose economics have settled, and these have not.
- *Is it important and knowable?* **[M2006-076]** The deciding question (does hydrogen win enough of heavy mobility and
  stationary power, at a margin, for Ballard to earn a return) is important; it is not "important and knowable"
  **[M2006-076]**.
- *Would the insiders write it down?* **[M2000-105]** The insiders decline in writing: "Consistent with our past practice,
  and in view of the early stage of hydrogen fuel cell market development, specific revenue or net income (loss) guidance for
  2026 is not provided." (6-K 2026-03-12, accession 0001279569-26-000211.) A management that will not write down one year's
  revenue has not written down ten years' economics; they "would not want to put down on paper their predictions" **[M2000-105]**.
  The 2027 or 2028 profitability objective is a stated aim, not a forecast of ten-year economics, and the two releases do not
  agree on its year (6-Ks 2026-06-23 and 2026-07-31).
- *Can I name the winner, not just the industry?* **[M2012-067]** No. Thirteen named rivals, several inside groups far larger
  than Ballard (Toyota, Hyundai, Honda, Bosch, Daimler Truck and Volvo through cellcentric), and the filer expects failures and
  consolidation. "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge
  what its profit margins and returns on capital will be as a host of competitors battle for supremacy." **[L2009-005]**.
- *Is the forecast about customers or about technology?* **[M2017-019]** About technology and policy: the cost, durability and
  power density of stacks against batteries, the price of hydrogen, and subsidy. "a business that must deal with fast-moving
  technology is not going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**; "where we think
  the future technology could hurt the business as it presently exists [...] it won’t make it through the filter"
  **[M1998-008]**. The filer itself: "The market requirements for our products and, by extension, our technology change
  rapidly." (Risk Factors.)
- *Do I doubt it is inside?* **[M2002-092]** Yes, so it is not: "if you have doubts about something being into your circle of
  competence" **[M2002-092]**.

**The routing.** "We view change as more of a threat into the investment process than an opportunity" **[M1999-063]**. A
business whose ten-year economics cannot be foreseen because its industry changes fast closes at Q1 in TOO HARD (the
framework's routing, fixed under What understanding means), never OUT on the business **[M2006-013]**: "It doesn’t mean it isn’t
a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it."
**[M2000-038]**. The start-up item of the OUT list ("Start-ups are not our game." **[L2007-015]**) was weighed and not applied:
the company was founded in 1979 and sells about $100M a year, though the filing calls its markets "pre-commercial" and "early
stage"; the ground of the stop is the fast-changing technology, which the framework sends to TOO HARD.

**The parts.** Since 2026-08-28 the company also owns GeoPura (hydrogen power units, hydrogen production and logistics, an
energy-as-a-service rental model; 6-K 2026-08-28). No filed earnings of GeoPura were found (its expected 2026 revenue of about
£38 million is a seller's figure, 6-K 2026-06-23); no part has operating profit, so the largest part decides (the business of
parts, Q2's CONVENTION, which defines "matters" in Q1): the fuel cell business, about $99M of 2025 revenue. GeoPura's own
economics turn on the same hydrogen variables (2 and 3 above), so the part does not change the answer.

**Which cause: NATURE.** The cause is the industry's, not the reader's: "in other cases the nature of the industry would be the
roadblock" **[L1993-023]**. The test between the causes is whether the insiders would write the forecast down **[M2000-105]**,
and they do not, in the filing itself. No filing not yet read could answer whether batteries or hydrogen win heavy mobility,
whether the subsidies last, or which of fourteen fuel cell makers survives: "Our problem -- which we can't solve by studying
up -- is that we have no insights into which participants in the tech field possess a truly durable competitive advantage."
**[L1999-018]**; more work would not "make up for the fact that we went in deficient in the first place" **[M2008-086]**. So
no research pass is opened, and a lower price does not reopen the box **[M2000-038]**.

**VERDICT: TOO HARD (NATURE).** Filing facts: the company declines revenue and net income guidance "in view of the early
stage of hydrogen fuel cell market development" (6-K 0001279569-26-000211); "We may never become profitable." (AIF, Risk
Factors, 40-F 0001628280-26-017045); battery-electric vehicles named as a competing zero-emission technology in every target
market and thirteen named fuel cell rivals with "further industry rationalization, failures" expected (AIF, Competition and
Strategy). The rows that decide it: **[M2000-037]**, **[M2012-065]**, **[L1993-023]**, **[M1998-008]**, **[M2000-105]**, **[L2009-005]**,
**[M2006-013]**.

---
## Q2 to Q12: NOT REACHED
The STOP at Q1 closed the file (operator rule 2). Nothing below is a clearance.

---
## THE BOX
**TOO HARD (NATURE), at Q1**: the ten-year economics of a PEM fuel cell maker in a subsidy-dependent, technology-contested
market cannot be foreseen, and the company's own management declines to forecast even one year's revenue. Value range by Q7's
convention, a COMPUTATION, not a clearance: **$(7.21) a share all-equity (no positive case) against $1.57**; integrity facts
recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box unchanged.)*

**Bearing on Q2 (the castle).** The competitor row, from the rivals' own filings, the same metrics over the span:

| Company (filing) | Metric | 2021 | 2022 | 2023 | 2024 | 2025 | Earlier years |
|---|---|---|---|---|---|---|---|
| Ballard (40-Fs above) | gross margin, $M | 14.0 | (13.3) | (21.8) | (22.0) | 5.5 | 2016 to 2020: 24.2, 41.6, 29.7, 22.3, 21.0 |
| Ballard | operating cash, $M | (80.5) | (132.2) | (104.6) | (108.1) | (56.2) | negative every year 2016 to 2020 |
| Plug Power (10-Ks; FY2025 accession 0001104659-26-022286, FY2024 0001558370-25-002049, FY2023 0001558370-24-002178; tagged data) | gross profit, $M | (171) | (194) | (508) | (625) | (242) | 2015 to 2020: (10), 4, (28), 3, 28, (469) |
| Plug Power | operating cash, $M | (358) | (829) | (1,107) | (729) | (536) | negative every year 2015 to 2020 |
| Cummins, Accelera segment (10-K FY2025, accession 0000026172-26-000009; FY2023, 0000026172-24-000012) | segment EBITDA (Cummins' own metric; includes electrolyzers and battery powertrains), $M | (218) | (334) | (443) | (764) | (896) | not reported before 2021 |

The field's returns over the whole span read from these filings: no filer among the three shows a profit from fuel cells in any
year found. Cummins in its FY2025 10-K: "due to the continued rapid deterioration in our electrolyzer markets and overall
hydrogen markets, along with significant uncertainty in the alternative power markets resulting from reductions in government
incentives", it impaired the electrolyzer goodwill and intends "to stop new commercial activity in the electrolyzer space".
Named rivals that do not file with the SEC: Beijing Sinohytec, cellcentric (Daimler Truck and Volvo), EKPO (ElringKlinger
and OPmobility), Powercell Sweden, Robert Bosch, Shanghai Re-Fire, Sino-Synergy, Symbio (Michelin, Forvia, Stellantis); Hyundai
does not file; Honda and Toyota file 20-Fs but report no fuel cell segment, so no comparable figure was found for them. The
filer's own words on price: "we see continued pressure on selling prices given weak customer economics, high hydrogen prices
and weak demand-side subsidies" (AIF, Risk Factors). Customers: "We depend on a limited number of customers for the majority of
our revenues" (Risk Factors); the Weichai-Ballard JV was fully impaired and Ballard "does not intend to make additional
significant investments in China" (AIF, Recent History); a truck customer, Quantron, restructured and Ballard "no longer holds
an equity interest" (AIF).

**Bearing on Q3 (capital).** The ten years absorbed $1,455.5M of new share capital and lost about $1.0B of it (balance sheets
above); capital additions of $41.2M in 2023 were followed by $111.0M of impairment of plant in 2024 and the abandonment of the
Texas Gigafactory.

**Bearing on Q4 (the accounts).** Adjusted EBITDA is featured in the results releases ("Adjusted EBITDA1 was (11.6) million",
6-K 2026-03-12) beside the GAAP loss; the GeoPura release features "EBITDA synergies"; "Cash Operating Costs, EBITDA, and
Adjusted EBITDA are non-GAAP measures" (same release). Recorded for Q4 and Q5, not weighed. Restructuring expense $17.0M in
2024 and $23.0M in 2025 (tags), with restructurings in 2023, 2024 and 2025 (AIF).

**Bearing on Q5 (the people; integrity facts recorded, not judged).** CEO Randy MacEwen stepped down and Marty Neese became
CEO on 2025-07-07 (AIF). The 2025 bonus scorecard paid at a 104% multiplier on revenue, order intake, contribution margin and
cash operating cost and capital spend, plus product and "Sign Significant Strategic Agreement" metrics; 2023 PSUs "vested at 89%
of target, with above-target performance in relative TSR offsetting lower cumulative revenue" (circular, 6-K 0001206774-26-000242).
Summary compensation table: Neese C$2,969,858 for part of 2025; MacEwen C$5,567,670 in 2025 including C$2,931,241 of other
compensation (circular). The profitability objective is dated "by the end of 2027" in the Q2 release and "by 2028" in the
GeoPura release (6-Ks 2026-07-31 and 2026-06-23). Weichai sold about 6.9 million shares and its two nominee directors resigned
(6-K 2026-05-14). A new COO from 2026-04-13 (6-K 2026-04-13). No integrity finding is made; a later run that reaches Q5 must
answer these.

**Bearing on Q6 (the money).** GeoPura: upfront £275.0M, of which £82.5M cash and about 50.8 million shares at US$5.02 (the
larger part in shares, so a merger under Q7 specific (c)), up to £27.5M contingent, enterprise value £301.1M (about US$400M)
including GeoPura's net debt; closed 2026-08-28 with 49,584,212 shares plus 1,084,540 shares owed under RSUs; the former
GeoPura holders own about 14.1% (6-Ks 2026-06-23 and 2026-08-28; Q2 interim note 25). Q6's STOP (an all-stock deal in
undervalued stock) is not reached; the fact that the shares were issued at $5.02 and quote at $1.57 is recorded only. No
buyback; no dividend. Commitments to fund HyCap and Clean H2 (Risk Factors). European Innovation Fund grant of up to €113M
tied to a final investment decision "currently planned for the third quarter of 2027" (AIF).

**Bearing on Q9 (debt).** No borrowings; lease liabilities $19.7M at 2026-06-30 (current $3.4M, non-current $16.3M, Q2 interim).
GeoPura's net debt of about £26.1M (the enterprise value less the upfront equity price) assumed at closing.

### COMPUTATION, NOT A CLEARANCE: the two reporting figures (a reporting convention, not a rule; no entry language)
Built by Q7's range convention in full, with the floor tested before the width.
- **Cash input:** five-year average owner cash after every real cost, $(134.1)M equity-only and $(159.7)M all-equity (tables in
  Step 0).
- **Growth (specific (b), decline):** the series is negative in every year; a compound rate between end years of negative
  numbers is meaningless, and so is the rate between the halves of the window. **The range is the no-growth case alone, said
  so.** Specific (a): 2022 and 2023 are the heaviest years of the capacity build that was later impaired, and 2025 the first
  year after the restructuring; the filer calls no year a cyclical peak or trough, so the literal window stands, with 2025
  alone shown beside. Specific (c): GeoPura is a merger closed after the window; no GeoPura earnings are filed, so it is
  credited at nothing, its cash price and assumed net debt are added to net debt and its shares to the count. Specific (d):
  working capital is inside operating cash as filed. Specific (e): the filing does not allow a maintenance guess for a
  business that has never reached a steady state; all spending is charged. Specific (f): no positive growth is carried, so no
  cap binds.
- **Net cash, all-equity basis:** cash $502.1M + short-term investments $3.0M + long-term financial investments $42.0M (fund
  interests at fair value, counted as securities and said so) at 2026-06-30 (Q2 interim), less the GeoPura cash price £82.5M
  (US$109.6M at the deal's own rate of US$400M for £301.1M) and GeoPura's net debt £26.1M (US$34.7M), the subsequent event the
  Q2 filing states (note 25) = **$402.9M**. Leases are left out of net debt because their principal and interest are charged
  inside owner cash (said so). Burn after 2026-06-30 is not filed and not deducted.
- **VALUE RANGE (the no-growth case alone):** all-equity, $(159.7)M / 5.43% = $(2,941)M + $402.9M = $(2,539)M, or
  **$(7.21) a share**; equity-only, $(134.1)M / 5.43% = $(2,469)M, or **$(7.01) a share**; against **$1.57**. Beside it, not
  central: 2025 alone gives $(4.10) a share all-equity and $(3.96) equity-only. The literal window is the window used.
- **The floor, tested first:** no case earns the floor at the price; every case has negative owner cash, so the expected return
  at any positive price is below about ten percent. Under Q7 this would close OUT whatever the width (the floor tested first),
  had Q7 been reached.
- **FAIR PRICE:** each end case valued at ten percent instead of the long rate, averaged (here one case): all-equity
  $(159.7)M / 10% + $402.9M = $(1,195)M, **$(3.39) a share (central figure, all-equity basis)**; equity-only $(134.1)M / 10% =
  $(1,341)M, **$(3.81) a share (beside)**. Tax: the company pays almost none (expense $0.1M in 2025) and owner cash is after the
  company's own tax as filed; no carryforward shelter is priced, since there is no positive income for it to shelter. There is
  no positive fair price: at any price, the central case does not earn the floor.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch (commit 941a2ff0); written question by question. **Committed after each
      question: not fully kept.** The file closed at Q1, and Step 0, Q1, the box, the facts after the stop and the computation
      were written in one pass and went into one commit after the template commit; there was no second question to commit
      separately, but Step 0 and Q1 were not committed apart from the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is held by the dispatching session; the run is
      folded by the dispatcher (operator rule ten). A run not in the register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Not fully kept:** one filtered
      listing of `Test Runs/` for this company's name and ticker, run to check the file name was free, returned no match; it is
      declared under contamination above. Nothing was seen. The other context items (commit subjects, git status, a memory
      line) are declared and not used.
- [x] Every v5 id resolves (checked by `check_cites.py` in the research folder); every filing fact has its accession; every
      number carries a filing or is a sum of filed figures; the share-count rule and the long-term investments as securities
      are confessed.
- [x] The order was kept; the STOP at Q1 closed the run; nothing after it is a clearance; the value figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay and lease principal deducted), never a net-income proxy; the sovereign from
      the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as found (the foundations paragraph); the facts for later questions are under AFTER
      THE STOP, with "integrity facts recorded, not judged" in the box line.
- [x] Not a point-in-time run; no anchor applies.
- [x] `tools/run.py` printed nothing usable for a 40-F; none of it was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Start-up or fast-moving technology.** Q1's OUT list carries "Start-ups" **[L2007-015]** and its TOO HARD paragraph
carries fast-moving technology; a forty-seven-year-old company that its own filing describes as selling into "pre-commercial"
and "early stage" markets and has never earned a profit is arguably both. The two lead to different boxes (OUT against TOO
HARD), and the text gives no test for when a long-lived, never-profitable company is a start-up. This run took the routing
paragraph's ground (fast-changing technology, TOO HARD) because it is the one the filing's own facts state; another analyst
could close OUT. A line saying whether "start-up" is a matter of age, of profit or of market stage would settle it. (2)
**Q7's convention on a business with negative owner cash in every year.** Specific (b) gives "the no-growth case alone" when
the rates are meaningless, which yields a negative value per share far below the cash on the balance sheet; the convention
does not say whether a business that could stop burning (liquidate, or cut to a care-and-maintenance state) should be valued
on its cash instead, the floor the owner could reach by closing it. This run reported the convention's figure and did not
invent the liquidation case. (3) **Lease liabilities under IFRS 16.** The all-equity basis says "borrowings and finance leases
[...] operating leases left out"; IFRS 16 has no operating-lease category for a lessee, so every lease is on the balance sheet.
This run left leases out of net debt because their cash is charged inside owner cash; the text does not say which way an IFRS
filer goes. (4) **The template's commit rhythm** ("committed after each") assumes the run reaches several questions; for a
file closed at Q1 the brief and template are silent on whether Step 0 and Q1 go in one commit.
