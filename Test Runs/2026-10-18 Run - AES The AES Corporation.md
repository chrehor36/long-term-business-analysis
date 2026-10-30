# Company Run — The AES Corporation (NYSE: AES) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 9080a701). Dispatched blind run,
written question by question, committed after each with a pathspec of this file and `Test Runs/_research 2026-10-18 AES/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-18, after the run was committed: `PORTFOLIO.md` read for AES only; not held.*

**CONTAMINATION, declared.** (1) To check that no run file of this name and date existed, I listed `Test Runs/` filtered
on "2026-10-18". The listing showed the file and research-folder names of nine other runs of this date (HOKCY, MDU, NJR,
NWN, OGS, SR, SWX, UGI, XNGSY). None was opened. (2) The session opened with `git log` subjects in context, which state the
result and figures of the UGI run of today. (3) The session context carried a one-line memory index about the queue and a
`git status` snapshot naming other research folders (AYI, ARCB). (4) A failed
`git commit` near the end printed the repository's `git status`, which listed untracked files in other runs' research
folders by name (among them AYI, BDC, CHD, FUL, GPC, HII, LOVE, LYTS, MEDP, NDSN, NGVC); file names only, after the box was
written. Nothing about AES under any name or ticker was seen in any of these. None of it was used. No other run file, holding review, `PORTFOLIO.md`, `Screens/RESUME STATE*`, the queue or the
prepped reading list was opened, listed beyond (1), or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $14.95 (close 2026-10-16, from `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
  **A fact of the run, recorded here and weighed only where the text says:** on 2026-03-01 AES signed an Agreement and Plan of
  Merger with Horizon Parent, L.P. (jointly controlled by vehicles of Global Infrastructure Management, LLC and the EQT
  Infrastructure VI fund) under which each share "shall be automatically converted into the right to receive $15.00 in cash"
  (8-K filed 2026-03-02, accession 0001193125-26-084157). Stockholders approved it on 2026-06-26 (8-K, 0001140361-26-026562);
  CFIUS approval 2026-08-27 (8-K, 0001140361-26-034714); PUCO approval 2026-09-17 (8-K, 0001140361-26-036994). Still required
  per the merger 8-K: approvals of the New York PSC, FERC, Hart-Scott-Rodino and "certain foreign countries", "without the
  imposition of a Burdensome Condition"; the merger 8-K expected closing "in late 2026 or early 2027". The End Date is
  **June 1, 2027**, extendable twice by three months where only regulatory approvals remain (DEFM14A). Termination fees: Parent pays $100 million or about $588 million depending
  on the circumstances; AES pays about $321 million in others (8-K of 2026-03-02). The price sits $0.05 below the cash
  consideration.
- **Shares by class:** 713,438,630 common, single class, par $0.01, from the cover of the 10-Q for the quarter ended
  2026-06-30, filed 2026-08-04, accession `0000874761-26-000144`, count as of 2026-07-31 (`python Screens/cover_shares.py
  AES`). Cross-check: the 10-Q balance sheet shows 859,837,679 issued and 713,157,713 outstanding at 2026-06-30 (treasury
  146,679,966); the 10-K shows 859,836,539 issued and 712,201,777 outstanding at 2025-12-31. No 8-K or prospectus after the
  10-Q issued common stock (8-Ks of 2026-08-05 credit-agreement amendments, 2026-08-27, 2026-09-16 officer departure,
  2026-09-17). Charter note: one class; the $838 million of 2021 Corporate Units converted into 40.5 million common shares
  in 2024 (10-K FY2025, statement of changes in equity); no parent preferred outstanding.
- **Market cap:** $14.95 x 713.44M = **$10,666M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 10/16/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-03-02, accession `0000874761-26-000063`: Item 1 (strategy, the four SBUs, every facility table,
    Energy Infrastructure country by country), Item 1A (renewables policy, indebtedness, defaults), Item 7 (results, non-GAAP
    definitions, capital expenditures, cash flows, Parent Company liquidity), Item 8 (statements, Note 19 segments), Item 9A.
  - 10-K FY2024 (`0000874761-25-000013`, filed 2025-03-11 after an NT 10-K), 10-K FY2023 (`0000874761-24-000011`),
    10-K FY2021 (`0000874761-22-000022`), 10-K FY2019 (`0000874761-20-000012`), 10-K FY2017 (`0000874761-18-000014`):
    balance sheets, cash-flow statements and segment tables for the span.
  - 10-Q Q2 2026, filed 2026-08-04, `0000874761-26-000144`: balance sheet, operations, cash flows, tax-credit transfers.
  - DEFM14A filed 2026-05-15, `0001140361-26-021662`: Background of the Merger, the Board's reasons, Forward-Looking
    Financial Information (the Standalone and Acquisition Cases), J.P. Morgan's selected companies.
  - DEF 14A filed 2026-03-20, `0000874761-26-000070` (pay, read for the facts after the stop).
  - 8-Ks: 2025-03-11 Item 4.02 (`0000950103-25-003226`); 2026-01-16 Item 2.06 (`0000874761-26-000006`); 2026-03-02
    merger (`0001193125-26-084157`); 2026-06-16 notes (`0001193125-26-272726`); 2026-06-26 vote; 2026-07-27 Item 4.01
    (`0000874761-26-000138`); 2026-08-05 (`0000950103-26-011951`); 2026-08-27; 2026-09-16 (`0000874761-26-000153`);
    2026-09-17; earnings-release exhibits of `0000874761-25-000006` (FY2024) and `0000874761-25-000086` (Q3 2025).
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, **$4,306M**,
    on the filed Consolidated Statements of Cash Flows (10-K FY2025, p. 125), equals the XBRL figure `tools/run.py` printed;
    capital expenditures $5,929M likewise.
- **`python tools/run.py AES`, arithmetic lines only** (saved in the research folder): owner cash on the capex basis
  (OCF less stock pay less capital spending) 2023 -$4,692M, 2024 -$4,652M, 2025 -$1,637M; on the D&A basis $4,179M,
  $4,004M, $5,749M; the five-year window -$2,614M (capex) and $3,706M (D&A). Stock pay $2M, $12M, $14M. Finance-lease
  principal $5M, $7M, $21M. The tool's OCF is as filed; it does not deduct purchases of emissions allowances (an operating
  cost the filer classifies in investing: $265M, $488M, $268M, $206M, $309M for 2021 to 2025) or distributions to minority
  partners ($284M, $265M, $323M, $430M, $912M). Both are taken up in the computation below. Nothing the tool prints as a
  rule, an id or a verdict is used (Part VII).

**The balance sheets, ten year-ends, read first:** "balance sheets over an 8 or 10 year period before I even look at the
income account" **[M2025-032]** (filed statements of the 10-Ks
named above and the 10-Q; $M; debt = recourse plus non-recourse, current plus noncurrent, finance leases included in the
non-recourse lines):

| year-end | total assets | AES equity | NCI + redeemable stock of subs | debt | cash | receivables | retained earnings | goodwill | intangibles |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 36,124 | 2,794 | 3,688 | 19,454 | 1,244 | 1,421 | (1,146) | 1,157 | 287 |
| 2017 | 33,112 | 2,465 | 3,217 | 19,965 | 949 | 1,463 | (2,276) | 1,059 | 366 |
| 2018 | 32,521 | 3,208 | 3,275 | 19,295 | 1,166 | 1,595 | (1,005) | 1,059 | 436 |
| 2019 | 33,648 | 2,996 | 3,121 | 20,173 | 1,029 | 1,479 | (692) | 1,059 | 469 |
| 2020 | 34,603 | 2,634 | 2,958 | 19,881 | 1,089 | 1,300 | (680) | 1,061 | 827 |
| 2021 | 32,963 | 2,798 | 3,026 | 18,699 | 943 | 1,418 | (1,089) | 1,177 | 1,450 |
| 2022 | 38,363 | 2,437 | 3,388 | 23,498 | 1,374 | 1,799 | (1,635) | 362 | 1,841 |
| 2023 | 44,799 | 2,488 | 4,961 | 26,878 | 1,426 | 1,420 | (1,386) | 348 | 2,243 |
| 2024 | 47,406 | 3,644 | 4,998 | 29,018 | 1,524 | 1,646 | 293 | 345 | 1,947 |
| 2025 | 51,768 | 4,063 | 7,866 | 29,897 | 1,382 | 1,683 | 641 | 342 | 2,040 |
| 2026-06-30 | 54,238 | 4,942 | 7,882 | 32,117 | 1,800 | 1,934 | 1,429 | 342 | 2,033 |

What the figures say. Total assets were flat at $33B to $36B from 2016 to 2021 and then rose by $21B in four and a half
years, the renewables build. The common equity was lower at the end of 2023 ($2,488M) than at the end of 2016 ($2,794M);
its rise since rests on the 2024 conversion of $838M of Corporate Units into common shares and on income attributed to
the common holders under the hypothetical-liquidation (HLBV) method of the tax-equity partnerships: in 2024 consolidated
net income was $802M while net income attributable to AES was $1,679M, because $877M of loss was allocated to minority and
tax-equity holders (10-K FY2025, statement of operations). Debt rose from $19.5B to $32.1B and stands at about 6.5 times the
common equity; the claims of minority and tax-equity partners ($7.9B) now exceed the common equity by about 1.6 times.
Retained earnings were a deficit in every year-end from 2016 to 2023. Over 2016 to 2025 net income attributable to AES
summed to $1,144M (XBRL, the 10-K figures) while cash dividends paid on the common summed to $3,945M. Receivables held at
about 11% to 14% of revenue throughout and inventory moved with fuel prices (peak $1,055M in 2022); no sign that "inventories look out of line" **[M1995-064]**
was found. Goodwill fell from $1,177M to $362M in 2022 (impairment); intangibles rose sevenfold with
the development pipeline and contracts. What they cannot say: what the common holder owns of the cash, since the
partnership agreements allocate cash, tax attributes and earnings to the partners by formulas that "vary over the life of
the projects" (10-K FY2025, Item 1, facility-table note 3), and whether the debt can be serviced from the parts that will
still be contracted in five years.

## THE FOUNDATIONS (not a gate)
The first foundation bears hardest. "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**:
at $14.95 against a signed $15.00 cash offer, a buyer today owns two things that are not a business: a claim to $15.00 if
the merger closes by its End Date, and, if it fails, a standalone AES whose own Board said it faced "a need of
approximately $2 billion from 2026 to 2030" or cuts to the dividend (DEFM14A, Reasons for the Merger). The run is of the
business, as the brief directs; the deal is recorded as a fact and weighed only where the text speaks. Who is paid to tell
you: the forecasts in the merger proxy were prepared by management for a sale, and the fairness opinions are paid by the
seller; "you do not get impartial advice from Wall Street" **[M2020-037]**; "You do not want to ask an investment banker
what he thinks the earnings are going to be in five years of something he’s trying to sell." **[M2011-083]**. The
forecasts are read below only for what they assume, never as an input: "we’ve never looked at a projection in connection
with either a security we’ve bought or a business we’ve bought" **[M1995-050]**. No macro view enters. **Contrary evidence,
written down as found**, "write it down in the first 30 minutes" **[M1997-127]**: against the business, the restated quarters of 2024 and the adverse internal-control
opinion; four years of owner cash below zero; the withdrawal of three of the bidders who had the data room. Against my own
Q1 verdict below, written as found: the insiders did write forecasts, to 2030 and for some segments to 2035; the 10-K lists
every plant's contract expiry; the two US utilities are ordinary regulated businesses whose economics are as foreseeable
as any utility's; and two long contracts in the deciding part (Southland Energy to 2040, Mong Duong 2 to 2040) are
readable to their ends.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if bought without borrowed money and sized so that a failed merger and a
fall well below $15.00 could be borne; borrowed money to hold it is ruled out: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; it
"can prevent you from playing out your hand" **[M2004-065]**. "We are never going to risk what we have and need for what we
don’t have and don’t need." **[M2012-081]**. The target's own debt is Q9's, not this rule's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The question.** "the first question is, can I understand it?" **[M1995-051]**, where understanding is "a reasonable fix on
about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**.

**The parts.** AES reports four segments with different economics (Renewables; Utilities; Energy Infrastructure; New Energy
Technologies), so Q1 reads the part that decides, by Q2's business-of-parts paragraph, which defines "matters" for Q1. Note 19
reports only one segment profit measure, Adjusted EBITDA. **CONVENTION of this run:** the parts test uses segment Adjusted
EBITDA as its share of five-year operating profit, because it is the only segment profit figure the filer reports; it is
used for nothing else in this run. Five years, as each year was last reported ($M):

| year | Renewables | Utilities | Energy Infrastructure | New Energy Tech. | source |
|---|---|---|---|---|---|
| 2021 | 545 | 633 | 1,494 | (77) | 10-K FY2023, `0000874761-24-000011` |
| 2022 | 613 | 612 | 1,846 | (116) | 10-K FY2024 Note 19, `0000874761-25-000013` |
| 2023 | 697 | 678 | 1,495 | (62) | 10-K FY2025 Note 19, recast |
| 2024 | 612 | 792 | 1,306 | (38) | 10-K FY2025 Note 19 |
| 2025 | 932 | 863 | 1,130 | (35) | 10-K FY2025 Note 19 |
| sum | 3,399 | 3,578 | 7,271 | (328) | |

Energy Infrastructure carries 51% of the three earning parts' five-year sum. The vintages differ: from 2025 the filer moved
its Chile businesses other than two coal plants out of Energy Infrastructure into Renewables and recast 2023 and 2024
(10-K FY2025, Note 19); 2021 and 2022 are on the older boundary. On any boundary Energy Infrastructure is the largest part
(on the recast years alone, 3,931 against Utilities 2,333 and Renewables 2,241), so it **decides** under the paragraph's
"else the largest" whether or not it passes half. The file is read on Energy Infrastructure, with the others noted.

**The deciding part.** Energy Infrastructure is 12,705 gross MW of gas, LNG, coal, pet-coke, diesel and oil plants in nine
countries: Vietnam, the United States, Argentina, Chile, Bulgaria, Mexico, Jordan, Panama and the Dominican Republic (10-K
FY2025, Item 1). From the filed facility table, by gross MW: plants whose contract expires in 2028 or earlier, 5,406 MW
(Southland OTC Alamitos 1,200 and Huntington Beach 236 to 2026 with California DWR, and AES Southland's plan is to retire
the OTC units under the state's cooling-water policy; Maritza 690, PPA expired May 2026; TermoAndes 643, 2025; Merida 505,
moved off its CFE PPA in December 2025 onto a one-year market permit "subject to negotiations with authorities for a
possible extension"; AES Puerto Rico 524, PREPA to 2027; Los Mina 358 and Andres 319 to 2027; TEG 275 and TEP 275 to 2027;
Colon 381 to 2028); plants with no contract date listed, 2,728 MW (Argentina's Paraná-GT 870, San Nicolás 691, Sarmiento 33,
where "approximately 86% of the energy was sold in the wholesale electricity market where prices are largely regulated";
Guillermo Brown 576, operated with no equity; Angamos 558, coal with "publicly announced phase-out plans"); plants
contracted past 2028, 4,571 MW (Mong Duong 2 1,242 to 2040; Southland Energy 1,387 to 2040; Cochrane 550, 2030 to 2037;
Gatun 670 at 24%; Amman East 472 and IPP4 250 at 10%). Sixty-four percent of the part's gross capacity is uncontracted or
contracted only to 2028 or earlier. Gross MW are not earnings; the filer reports no earnings by plant.

**The tests, applied.**
- **Key variables and how predictable**, "trying to identify the key variables in that particular business, and
  evaluating how predictable they were first" **[M1998-044]**: for this part they are the terms on which state buyers and
  regulators in nine countries recontract, extend or retire these plants (the California DWR and the state's cooling-water
  policy; NEK and the European Commission's state-aid review of the Maritza PPA; PREPA; CFE and Mexico's 2025 electricity law;
  the Dominican and Panamanian distribution companies; Argentina's regulated wholesale prices and its FONINVEMEM
  receivables; Chile's 2040 coal retirement decree). Each is a government's future decision, not a market price or a
  customer's choice. "If something is not very predictable, forget it." **[M1998-044]**.
- **Do the past statements tell the future ones**, "so that the financial statements will tell me the information that’s
  useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**: no. The part's Adjusted EBITDA fell from $1,846M (2022)
  to $1,130M (2025) as contracts ended or were sold (the Warrior Run PPA monetized in 2024; Ventanas 1 to 4 and Norgener
  disconnected or sold 2022 to 2025); the segment boundary itself was redrawn in 2025; and the company's quarterly
  statements for Q2 and Q3 2024 were restated (8-K Item 4.02, 2025-03-11) with a material weakness reported. "in many
  cases, the answer would be no" **[M2008-033]**.
- **Would the insiders write it down**: "they would not want to put down on paper their predictions" **[M2000-105]**. The
  company's own words, in the merger proxy, are that it "does not
  as a matter of course disclose public forward-looking financial information as to future revenues, EBITDA, parent free
  cash flow, earnings, or other results due to, among other reasons, the uncertainty, unpredictability and subjectivity of
  the underlying assumptions and estimates" (DEFM14A, Forward-Looking Financial Information). The private forecasts it did
  prepare for the sale assume the deciding variables away: "No significant changes to regulatory or legislative
  environments" and "Continued long-term contracting of power purchase agreements over the forecast periods" (same
  section). Inside the five-year window the legislative environment changed in the United States twice (the 2022 IRA, then
  the 2025 Act that "curtailed" it, 10-K Item 1A) and in Mexico, and Chile accelerated its coal retirements by decree.
- **The buyers who had the data room.** Of the parties who signed confidentiality agreements and read the data room, Party A
  declined to bid citing "its inability to reach confidence on a proper valuation given the Company’s operational
  complexities, business mix and regulatory considerations"; Party B withdrew "due to reservations regarding portfolio
  complexity and strategic fit"; Party C "was unable to support a value meaningfully above the Company’s prior day’s closing
  price of $11.48 per share"; EQT withdrew once before rejoining (DEFM14A, Background of the Merger). J.P. Morgan valued the
  other international segments by intrinsic value "given the lack of public peer trading companies". The Board's own
  reasons name "a portfolio mix that lacks direct comparables in the market, including due to having significant assets in
  international emerging markets". These are not the speakers' tests; they are evidence on test 5 from the people with the
  most information.
- **Abroad: the governance and the tax**: "where we think we understand the nuances of the corporate governance system and
  taxation"; "We don’t understand all 200 countries, by a long shot." **[M2000-141]**. Nine
  countries in the deciding part, several with a state-owned single buyer (EVN, NEK, PREPA, CFE until 2025), and Argentina,
  where the part's receivables depend on government instalments. I do not understand the nuances of the governance and
  taxation of most of them.
- **The whole against the transactions**: "I don’t regard the whole enterprise, or the operation of it, necessarily as
  being within my circle of competence" **[M2002-094]**. Each contract in the facility table can be read; whether the whole
  can be funded "independent from" outside capital cannot. The parent's cash is the distributions of subsidiaries whose debt
  is non-recourse, and the company's own Board said the plan needed about $2 billion of new equity or dividend cuts from 2026
  to 2030.
- **How far off could I be**: "we also have some model in our mind of how far off we can be" **[M2011-084]**. On the contracted 4,571 MW, a narrow range; on the 8,134 MW that are uncontracted
  or contracted only to 2028 or earlier, whose terms are set largely by governments and state buyers, no range I could
  defend.
- **Do I doubt it is inside**: "if you have doubts about something being into your circle of competence, it
  isn’t." **[M2002-092]**. I do. The perimeter is drawn narrow on purpose: "a little smaller than it really is" **[M2005-101]**;
  "knowing where the perimeter is" **[M2010-083]**.

**The other parts, noted.** The Utilities part (AES Indiana, AES Ohio, El Salvador) is a regulated business of the kind Q1
can read; the Renewables part rests on contracted output and on United States tax credits whose law changed in 2025 and
whose guidance is "not yet" all issued (10-K Item 1A). Neither decides; neither would rescue the deciding part, since a part
that cannot be understood and that matters keeps the whole outside, by the doubt row quoted above.

**The cause.** NATURE, not WORK. The deciding question is not a fact in a filing not yet read; it is what nine governments
and their state buyers will do with contracts that end between 2025 and 2028 and with coal they have said they will retire.
The insiders publish no forecast, among other reasons for that one, and their private forecasts assume it away; the best-informed outside
buyers said they could not value it. "in other cases the nature of the industry would be the roadblock" **[L1993-023]**;
more reading would not supply what no filing states: "we’re not going to learn enough in the followings five months to
make up for the fact that we went in deficient in the first place" **[M2008-086]** ("followings" is the transcript's). The WORK reading was weighed and set aside: a
plant-by-plant read of the contracts would tell what is contracted, which the facility table already does; it cannot tell
what the uncontracted or short-contracted two thirds of its capacity will earn.

**VERDICT: TOO HARD (NATURE).** "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of
its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**; the third of "in, out, and too hard" **[M2006-013]**. The file
closes here. Q2 to Q12 are NOT REACHED; what was already found is recorded below, not weighed.

## Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12: NOT REACHED
The file closed at Q1. The Q7 figures below are a computation, not a clearance.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the deciding part, Energy Infrastructure, is a thermal fleet in nine countries
whose ten-year earnings turn on government recontracting and retirement decisions the insiders do not forecast; integrity
facts recorded, not judged. A lower price does not reopen it (section I, the two causes).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source, "write it down in the first 30 minutes" **[M1997-127]**; written down, not weighed; the box
is unchanged (operator rule 2).

**Bearing on Q2 (the castle, the field's returns, the competitors).**
- The 10-K names no rival: "numerous strong and capable competitors" (Item 1A). **CONVENTION of this run:** the competitor
  row uses three SEC filers from the companies J.P. Morgan selected as comparable to AES's segments in the merger proxy:
  NRG Energy and Vistra (selected for Southland, US thermal) and Clearway Energy (selected for AES Clean Energy). Rationale:
  the brief asks for rivals from their own filings and the 10-K names none; the banker's list is the filer's own record of
  who resembles each part. Not SEC filers, flagged: Colbún, Eneva, Auren Energia and ENGIE Brasil Energia (selected for AES
  Andes, Latam LNG and Panama); Central Puerto files with the SEC as a foreign private issuer and was not read.
- Same metric over the whole span, from each company's XBRL 10-K facts (transcription; AES's figures were checked against
  its filed statements, the rivals' were not): cash from operations less capital spending, summed, acquisitions excluded for
  all four ($M).

| company | span | OCF | capital spending | OCF less capital spending | as % of revenue | net income attributable | years OCF below capital spending |
|---|---|---|---|---|---|---|---|
| AES | 2016-2025 | 27,674 | 38,660 | (10,986) | (9.8%) | 1,144 | 2021, 2022, 2023, 2024, 2025 |
| NRG (CIK 1013871) | 2016-2025 | 12,996 | 4,497 | 8,499 | 4.4% | 7,484 | 2022, 2023 |
| Vistra (CIK 1692819) | 2017-2025 | 23,295 | 11,456 | 11,839 | 10.4% | 3,851 | 2021, 2022 |
| Clearway (CIK 1567683) | 2016-2025 | 6,262 | 1,726 | 4,536 | 38.1% | 1,015 | none |

  The rivals bought businesses outside these columns (NRG: Direct Energy 2021, Vivint 2023; Vistra: Dynegy 2018, Energy
  Harbor 2024; Clearway: drop-down acquisitions), so their columns overstate what was left to owners; AES's own acquisitions
  were small (net $916M over 2021 to 2025).
- AES's returns over the span: net income attributable $1,144M over 2016 to 2025 against common equity that averaged about
  $2.9B (Step 0 table). The proxy's pay-versus-performance table: $100 invested at the end of 2020 was worth $73 at the end
  of 2025 for AES and $159 for its peer group (DEF 14A 2026). J.P. Morgan told the Board in April 2025 that AES's "recent
  stock price remained at a similar level to seven years prior" (DEFM14A, Background).
- The deciding part's direction: Energy Infrastructure segment Adjusted EBITDA 1,494, 1,846, 1,495, 1,306, 1,130 (2021 to
  2025, the Q1 table); management's own Standalone Case shows Southland falling from $251M (2026) to $117M (2030) and
  "Other Businesses" from $618M to $543M (DEFM14A). Read for direction only; projections are not inputs.
- The utilities: rate base $5,221M at 2025 and $5,881M projected for 2026 (DEFM14A); a regulated return.

**Bearing on Q3 (capital).** Property, plant and equipment rose from $19,906M (2021) to $37,818M (2025) and $40,657M
(2026-06-30); total segment Adjusted EBITDA moved from $2,580M (2021, as then reported) to $2,890M (2025). The Board's words:
"capital intensity with back-ended cash returns for certain U.S. renewable projects" and "a substantial need for growth
capital in excess of available capital from parent free cash flow" (DEFM14A, Background). The Standalone Case shows AES
Clean Energy's levered free cash flow negative in 2026 to 2029 and in 2031 (DEFM14A).

**Bearing on Q4 (the accounts).**
- **Restatement and control weakness.** 8-K Item 4.02 of 2025-03-11: the statements of operations for Q2 and Q3 2024
  "should no longer" be relied on; impairment on the AES Brasil sale was overstated by about $192M and $5M, "primarily due to
  the use of incomplete data". A material weakness was reported; EY's report on internal control at 2024-12-31 "contained an
  adverse opinion" (8-K Item 4.01, 2026-07-27). The FY2024 10-K followed an NT 10-K (filed 2025-03-03); a 10-K/A was filed
  2025-04-11 (not read). Item 9A of the FY2025 10-K reports the weakness remediated and controls effective at 2025-12-31.
- **Auditor change.** EY dismissed 2026-07-21 because it would not be independent after the merger closes; KPMG engaged,
  after disclosing that KPMG member firms had provided "Impermissible Services" to AES subsidiaries in 2026, completed or
  terminated before the appointment; no disagreements (8-K 2026-07-27).
- **EBITDA in the filer's own mouth.** Adjusted EBITDA is the segment measure and the chief operating decision maker's
  measure (Note 19); a second figure, "Adjusted EBITDA with Tax Attributes", adds back the tax credits and depreciation
  deductions allocated to tax-equity investors ($4,411M in 2025, 10-K Item 7). The definitions of Adjusted EBITDA, PTC and
  EPS were changed in Q1 2024 and again in Q1 2025 (the second to exclude restructuring costs). The speakers' row on the
  figure: "The one figure we regard as utter nonsense is the so-called EBITDA." **[M1998-086]**.
- **The recurring "one-time".** Impairment expense in the cash-flow add-backs: $1,575M (2021), $1,715M (2022), $1,079M
  (2023), $374M (2024), $337M (2025); loss on commencement of sales-type leases $231M (2025); restructuring costs $89M
  (2025) excluded from the adjusted figures.
- **Emissions allowances.** The cost is added back in operating cash flow and the purchases sit in investing ($309M in
  2025), so operating cash flow as filed overstates cash earnings by the purchases.
- **Tax credits in operating cash.** Cash from transferring tax credits, "inclusive of the portion allocated to
  noncontrolling interest holders, is treated as an operating cash inflow" (10-Q Q2 2026, Note 1); the partners' portion
  leaves in financing as distributions ($912M in 2025, up from $430M).
- **HLBV.** Earnings attributed to the common holders rest on a hypothetical-liquidation allocation: net losses of $748M,
  $877M and $431M were allocated to minority and redeemable holders in 2025, 2024 and 2023 while consolidated net income was
  $162M, $802M and -$182M (10-K FY2025).

**Bearing on Q5 (integrity facts recorded, not judged).**
- The restatement and the adverse internal-control opinion above.
- Guidance and targets: annual guidance and multi-year growth targets for Adjusted EBITDA (5% to 7% a year through 2027) and
  Adjusted EPS (7% to 9% through 2025 and through 2027) (FY2024 earnings release, 8-K `0000874761-25-000006`). FY2024
  Adjusted EPS $2.14 against guidance of $1.87 to $1.97; Adjusted EBITDA $2,639M against $2,600M to $2,900M (same).
- The 2025 annual incentive paid on non-GAAP figures: Adjusted EPS $2.34 against a $2.18 target, Adjusted EBITDA $2,871M
  against $2,750M, Parent FCF $1,219M against $1,200M; payout 138%; "No alterations or increases were applied" (DEF 14A 2026).
- CEO pay: Summary Compensation Table $9.15M (2025), $13.36M (2024), $12.72M (2023); the CEO's long-term award cut 30% in
  2025 and again in 2026 "in response to trends observed in the Company’s share price"; no salary increase since 2021
  (DEF 14A 2026). Merger-related "golden parachute" compensation for the CEO estimated at $46,621,736 (DEFM14A).
- The sale process was led by the CEO from early 2024; three of four round-one parties did not bid; GIP cut its price from
  $15.00 to $14.25 "in part due to changes in certain tax assumptions and renewables operating performance" before the final
  $15.00 (DEFM14A, Background).

**Bearing on Q6 (the money and the owners).** Cash dividends on the common, $3,945M over 2016 to 2025 and $251M in the first
half of 2026, while owner cash after all capital spending was below zero in each of 2021 to 2025 (computation below) and net
income attributable summed to $1,144M. Share repurchases: $79M in 2016, none found in the XBRL facts after, so Q6's test of
prices paid against the bottom of the Q7 range has nothing to read. Issuance: $1,014M of equity units in 2021, converted
into 40.5M common shares in 2024. Capital raised by selling stakes to partners and issuing preferred shares in subsidiaries,
net of buying stakes back: $574M, $433M, $2,334M, $1,469M, $3,370M (2021 to 2025, financing section). The Board's statement
that without the merger AES "would be required to reduce and/or eliminate the payment of quarterly cash dividends and/or
issue significant new equity to fund a need of approximately $2 billion from 2026 to 2030" (DEFM14A, Reasons).

**Bearing on Q9 (debt and exposures).** Debt $32,117M at 2026-06-30 (recourse $6,100M, non-recourse $26,017M, finance leases
inside the non-recourse lines); supplier financing $826M. Coverage measured as the row measures it, "pre-tax
earnings/interest, not EBITDA/interest" **[L2012-002]**: income from continuing operations before taxes plus interest expense,
over interest expense, 1.08x (2023), 1.60x (2024), 1.05x (2025). Non-recourse debt in technical default $20M (AES Ilumina);
recourse debt maturing within twelve months $879M at 2025 year-end; Parent Company liquidity $1,381M (2025) against $2,047M
(2024) (10-K Item 7). Change-of-control put at 101% on the June 2026 notes. Litigation: a December 2025 complaint by Sinolam
seeking "about $4 billion" of alleged lost profits (Panama LNG); Dominican Republic suits over coal combustion residuals from
AES Puerto Rico delivered in 2003 and 2004, demanding $476M and "over $600 million" (10-K Item 3).

**Bearing on Q12.** Coal is 15% of AES's generating capacity (10-K Item 1); the coal-residue suits above allege personal
injuries and deaths. None of the businesses the text names as a STOP (casinos, tobacco, loading schemes) is among AES's.

**Bearing on Q8 and Q10.** The price is $0.05 below the $15.00 cash consideration; the merger 8-K expected closing in late
2026 or early 2027. The text has no question addressed to a spread on a pending cash merger (see the last section).

## COMPUTATION, NOT A CLEARANCE: Q7's range and the two reporting figures
*(Q7 was not reached; the file closed at Q1. These figures are arithmetic for the operator's reporting convention and carry
no entry language, operator rule 3. Script and output: `Test Runs/_research 2026-10-18 AES/compute.py` and
`compute_output.txt`.)*

**Owner cash, 2021 to 2025, $M**, from the filed cash-flow statements (10-K FY2023 for 2021 and 2022, 10-K FY2025 for 2023 to
2025): operating cash flow, less stock pay, capital expenditures, payments for financed capital expenditures, purchases of
emissions allowances, acquisitions net of businesses sold, contributions to equity affiliates net of their returns,
distributions to minority partners, and finance-lease principal. The all-equity basis adds back cash interest paid after a
21% tax. **CONVENTIONS of this run:** (1) interest is added back after the US statutory 21%, because the company's own
effective rate swings between benefit and charge and the basis asks for owner cash after the company's tax; (2)
distributions to minority and tax-equity partners are a cost to the common holder on both bases, because the common holder
receives none of that cash and the consolidated debt is already counted in full; (3) capital raised from partners (stake
sales, tax equity, subsidiary preferred) is not credited in the central case, because the filer books it as financing and it
buys a share of future cash that the distributions line then pays out; the case crediting it is shown beside.

| case | 2021 | 2022 | 2023 | 2024 | 2025 | five-year average |
|---|---|---|---|---|---|---|
| all-equity, all spending (central) | (827) | (2,237) | (4,719) | (4,346) | (1,995) | **(2,825)** |
| equity-only, all spending | (1,471) | (2,970) | (5,759) | (5,348) | (2,951) | (3,700) |
| all-equity, depreciation in place of capital spending | 927 | 1,619 | 2,329 | 1,835 | 2,549 | 1,852 |
| equity-only, depreciation in place of capital spending | 283 | 886 | 1,289 | 833 | 1,593 | 977 |
| all-equity, all spending, partner capital credited | (253) | (1,804) | (2,385) | (2,877) | 1,375 | (1,189) |

**The specifics, applied.** Growth on the aggregate, not per share. (a) The filer describes no end year of the window as
aberrational in owner cash; the literal window is the base. (b) The central series is below zero in every year, so a growth
rate between its end years is meaningless, and so is the halves' rate; the range is the no-growth case alone, said so. (c)
Acquisitions net of sales are deducted ($916M over the window); the merger is AES being bought, not a deal AES signed as
buyer, so the signed-deal clause does not apply; not a serial acquirer (owner cash before purchases is below zero, and net
purchases are small beside capital spending). (d) Working capital is inside operating cash flow as filed. (e) The filing does
not allow the maintenance guess: the 10-Ks of FY2021, FY2023, FY2024 and FY2025 chart the year-on-year change in growth,
maintenance and environmental spending, never the levels (FY2025: maintenance down $186M); so the central case deducts all
spending and the depreciation variant stands beside. (f) The depreciation variant's shown growth, 28.8% a year on the
all-equity series, carried ten years would need $23.2B of owner cash against revenue of $12.2B (its highest share of sales
in the window 20.8%); it is cut to revenue growth over the same years, 2.37% a year. Tax: the company's own tax is inside
operating cash flow; so is the cash from transferring tax credits whose law was curtailed in 2025. Section E's treatment
(statutory rate, shelter priced separately) was not applied, because the central case is below zero before it and applying
it would lower every case further. Rate 5.43%; zero nominal growth after year ten.

**Net debt (all-equity basis):** debt $32,117M less cash $1,800M and short-term investments $53M = **$30,264M** at
2026-06-30 (10-Q); with restricted cash of $530M also subtracted, $29,734M (not used). Operating leases left out. No subsequent
event stated in the 10-Q changes net debt; the buyers' financing is not AES's. Market value $10,666M; market value plus net
debt $40,930M.

**The floor, tested first** (about ten percent; "we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**): the central case's expected return at the price is -6.9% on
$40,930M; equity-only, -34.7% on $10,666M. **No case of the range earns the floor at $14.95**; in a run that reached Q7 this
would close OUT before the width test. Beside it, the depreciation variant: all-equity 4.5% (no growth) to 5.5% (capped
growth); equity-only 9.2% to 10.7%.

**THE TWO REPORTING FIGURES (COMPUTATION, NOT A CLEARANCE; a reporting convention, not a verdict):**
- **(a) VALUE RANGE: -$115.34 a share**, the no-growth case alone, all-equity basis (central), against **$14.95**.
  Equity-only beside: -$95.50. (Depreciation variant beside, not the range: all-equity $5.38 to $15.32; equity-only $25.21
  to $30.46.)
- **(b) FAIR PRICE: -$82.01 a share**, all-equity basis (central; the no-growth end valued at ten percent, the only end; not
  positive), after the company's own tax. Equity-only beside: **-$51.86**. (Depreciation variant beside: all-equity -$14.20,
  equity-only $14.89.)

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 9080a701); written question by question; committed after the
      question that closed the file (7d807e10) and after this section.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's; the fold is the
      dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched; the one filtered listing of `Test Runs/`
      and the session context are declared under CONTAMINATION and were not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (`check_ids.py`
      in the research folder); every filing fact carries its document and accession; no E-id.
- [x] The order was kept: Q1 closed the file; nothing after it is a clearance; the figures are headed COMPUTATION.
- [x] Owner cash after every real cost, never a net-income proxy; emissions-allowance purchases and partner distributions
      deducted; the sovereign from the Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written as found, including against my own Q1 verdict (Foundations); facts for later questions are
      under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor date.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the final commit.
- Defects found in my own work: a garbled End Date sentence in Step 0 was rewritten before the Q1 commit. The rivals' XBRL
  columns were not cross-checked against their filed statements; they are transcription.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A target under a signed cash merger.** The price sits $0.05 under the cash consideration, so what a buyer gets is mostly
the deal's closing. The text judges the business (Q1 to Q7) and the alternatives (Q8) and says nothing of a spread on a
pending cash merger; I ran the business, as the brief directed, and recorded the deal as a fact. (2) **The parts test asks
for operating profit**; Note 19 reports only Adjusted EBITDA by segment, and the filer moved its segment boundary inside the
window (Chile, 2025), so the five-year share mixes vintages. I used Adjusted EBITDA as a confessed CONVENTION and showed that
the deciding part is the largest on any boundary; the text could say which figure to use when the filer gives no other. (3)
**Minority and tax-equity partners.** Q7's all-equity basis defines net debt but is silent on $7.9B of noncontrolling and
redeemable interests and on capital raised by selling stakes to partners, which here averaged $1.6B a year against an owner-cash
deficit of $2.8B; I deducted the partners' distributions and showed the partner capital beside. A business financed this way needs a
rule. (4) **Tax credits sold for cash.** Section E prices carryforwards and credits that lower the company's tax; here the
credits are sold, the cash runs through operating cash flow and part of it out to partners. Whether section E reaches them
is unclear; I did not apply it and said why. (5) **WORK or NATURE when the deciding variable is a government's decision.**
The text's examples of NATURE are technology; mine is recontracting and retirement by nine governments. I decided NATURE on
test 5 with the company's own statement of why it publishes no forecast; another analyst could call it WORK, and the text
does not settle it. (6) **"Where the filing allows the maintenance guess"**: this filer charts the yearly change in
maintenance spending but never its level. I read that as not allowing the guess; the text could say whether a disclosed
change without a level counts.
