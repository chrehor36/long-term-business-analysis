# Company Run: AMERICAN BATTERY MATERIALS, INC. (OTC Pink: BLTH), 2026-10-11
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit e6f1bcd9). Dispatched blind run under
`Screens/_daily/_dispatch_brief.md` with the brief's one stated departure (the analyst derives the lines of evidence and the
competitors from the 10-K). Working folder: `Test Runs/_research 2026-10-11 BLTH/` (raw filings in its gitignored `cache/`).
CIK 1487718. Former names on EDGAR: Internet Media Services, Inc. (2010-04-09 to 2014-05-20), U-Vend, Inc. (2014-05-21 to
2018-03-01), BoxScore Brands, Inc. (2018-04-02 to 2023-04-21).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-11, after the run was committed: `PORTFOLIO.md` does not name BLTH or American Battery Materials; not held.*

**CONTAMINATION, declared.** Seen by accident before any reading, not used: (1) the session's starting context listed the five
latest commit subjects of the repository, which are another company's run (AMBQ, closed "TOO HARD (NATURE) at Q1"); (2) the
same context listed untracked research folders of two other companies (AYI, ARCB) by file name; (3) the memory index loaded
into the session carries summary lines about the queue and the operator's gate-clearers ("57 gate-clearers, nothing buyable",
five holding reviews owed), naming no company. Nothing of BLTH under any name or ticker was seen. No run file, holding
review, `PORTFOLIO.md`, register, reading list or resume-state file was opened, listed or searched. The AMBQ box was not
consulted in choosing this run's box; that this run's Q1 close differs in box (OUT here) is set down so that the fold can see it.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $4.00 (close 2026-10-09, the last trading day before the run; aggregator quote through `tools/run.py`, flagged
  per operator rule 5: live quote only). The 10-K's last reported sale was $3.75 on 2026-03-18 (10-K, Item 5).
- **Shares by class** (one class, common; 0 preferred issued): **3,789,585** on the cover of the 10-Q for the quarter to
  2026-06-30, filed 2026-08-10, accession `0001493152-26-036860` (`python Screens/cover_shares.py BLTH`); the same figure
  is the balance-sheet count issued and outstanding at 2026-06-30 (no treasury shares) and the S-1/A of 2026-08-11
  (accession `0001493152-26-037118`) gives 3,789,585 "as of August 11, 2026". **Subsequent events the filings state:** the
  8-K of 2026-08-25 (accession `0001493152-26-039978`) says that if the company "shall not have consummated an uplist of its
  common stock to NYSE American on or prior to September 30, 2026", then "the Company shall arrange for the issuance of six
  hundred twelve thousand four hundred seventy-six (612,476) shares of Common Stock to the noteholders", automatically.
  **Whether the uplist happened:** no filing shows it. The EDGAR submissions record for CIK 1487718, read 2026-10-11, lists
  no filing after the 8-K of 2026-09-01; no notice of effectiveness and no 424B prospectus for the S-1 of 2024-02-12 or any
  of its amendments; no Form 8-A since the 8-A12B of 2023-01-12 (filed under the BoxScore name during the abandoned SPAC
  deal); and the record's exchange field still reads OTC. The S-1/A itself says "A NYSE American listing for our common
  stock is a condition to completing this offering." I read the filed record as: the uplist was not consummated by
  2026-09-30, so the 612,476 shares and the 15% principal increase took effect by the 8-K's own terms. Share count used for
  the reporting figures: **4,402,061** (3,789,585 + 612,476), with 3,789,585 shown beside. Not counted: 3,045,572 shares the
  S-1/A says would issue on automatic conversion of all convertible notes at its assumed $5.50 offering price; 533,987
  options; 400,000 RSUs (S-1/A, capitalization and offering summary). Reverse splits on the record: 1-for-300 effective
  2023-12-08 and 1-for-5 effective 2025-01-24 (10-K Item 5; S-1/A). *The brief described the DEF 14C of 2025-10-28
  (accession `0001493152-25-019877`) as concerning a further reverse split; read in full, its one action is an amendment
  making the 2024 Incentive Compensation Plan "at all times be equal to 17.5% of the issued and outstanding shares of the
  Company on a fully diluted basis", approved by written consent of holders of 1,590,644 shares, 54.37%; "reverse stock
  split" appears once, in the dissenters'-rights boilerplate.*
- **Market cap:** $17.6M at 4,402,061 shares ($15.2M at 3,789,585).
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 10/09/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-03-19, accession `0001493152-26-011615` (Items 1, 1A, 5,
  7, 8 and notes, 13); 10-Q for Q2 2026, filed 2026-08-10, `0001493152-26-036860` (statements, subsequent events, MD&A);
  10-Q for Q1 2026, `0001493152-26-023799` (fetched, cover only); 10-K for FY2024, `0001641172-25-000535` (fetched for the
  prior column); 10-K for FY2022 under the BoxScore name, `0001213900-23-031453` (debt-conversion notes); DEF 14C,
  `0001493152-25-019877`; 8-Ks of 2025-10-15 (`0001493152-25-018180`, investor-presentation furnishing), 2026-08-25
  (`0001493152-26-039978`) and 2026-09-01 (`0001493152-26-041012`); S-1/A of 2026-08-11 (`0001493152-26-037118`: offering
  summary, capitalization, related-party transactions); XBRL company facts for the 2019 to 2025 annual cash-flow lines.
  **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $396,365 on the filed balance sheet
  (10-K, p. 31) against 396 (thousands) in `tools/run.py`'s ten-year table: agree. Operating cash flow 2025, $(499,416) in
  the filed cash-flow discussion (Item 7) against the XBRL value -499,416: agree.
- `python tools/run.py BLTH`, arithmetic lines only: the tool's owner-earnings window stopped at FY2018 because capital
  spending is not tagged under the elements it reads after 2018, and it warned so; it refused a yield on a non-positive
  base. The figures below are taken from the filings instead. **Owner cash after every real cost, by year** (operating cash
  flow less stock pay less capital spending, the capital spending being the mineral-claim outlays in investing activities;
  USD): 2021 (498,741); 2022 (972,789); 2023 (2,659,671); 2024 (817,897); 2025 (1,337,774). **Five-year average
  (1,257,374).** Negative in every filed year; no revenue in any year of the lithium business (10-K Item 7: "For the year
  ended December 31, 2025, and 2024, our company had no revenue"). Capex and D&A: no depreciable assets; the one non-current
  asset is mineral claims carried at $206,000. Stock pay resolved: 2025 $838,358; 2024 $67,586 (10-K Item 7). Six months to
  2026-06-30: operating cash flow (322,046), stock pay 468,219 (10-Q). Arithmetic in `Test Runs/_research 2026-10-11 BLTH/calc.py`,
  output beside it.

## THE FOUNDATIONS (not a gate)
**A share is a business** bears hardest. The test is "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**. This company cannot survive five years of a closed market on its own filings: its cash was $3,480 at
2025-12-31 and $5,704 at 2026-06-30, every dollar of operating spending since 2021 has come from new notes, and the S-1/A makes
a NYSE American listing "a condition to completing this offering". Its value to a buyer today rests on the next financing, which
is to say on "what somebody else will pay you for it later on, irrespective of what the asset produces, and I call that
speculation" **[M2002-078]**. **Who is paid to tell you** bears second: the 10-K's market case is built from third-party
forecasts (Fastmarkets, BloombergNEF, Benchmark Minerals, Canaccord Genuity), and the rows say "we’ve never looked at a
projection" **[M1995-050]** and "don’t ask the barber whether you need a haircut" **[M2011-083]**. Neither admits or rejects the
business (section II). **Contrary evidence, written down as found** **[M1997-127]**: (1) the claims are real and kept in good
standing (8-K of 2026-09-01: 743 claims renewed with the BLM through 2027); (2) the exploration permit "has been obtained from
both the Federal BLM and the State UDOGM" (10-K Item 1); (3) the historical Superior well recorded "340 ppm" lithium and
"74,400 ppm" magnesium (10-K Item 1), and there is federal support for domestic lithium and magnesium (critical-minerals list,
Section 45X credit) the filing describes; (4) cash burn before financing costs is small, about $0.5M to $1.3M a year, so the
business is a cheap option if it survives; (5) on 2026-08-25 the company says it "is not in default under any of its notes".

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase for cash, unlevered, sized so that the loss of all of it cannot touch what the
buyer has and needs, does not breach "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; borrowing to buy it would, since "it would be almost impossible to go broke without borrowed money being in the
equation" **[M1999-005]**. Written down for the record and not weighed here: on the filings the whole of this equity can go to
nothing (going-concern doubt, liabilities 41 times assets at 2026-06-30), which the rule "Never risk permanent loss of
capital." **[L2023-005]** names as the thing never to do.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**Lines of evidence chosen, and from which item.** Item 1 (Business): exploration-stage status, no reserves, no drilling, no
DLE testing, no customers, no intellectual property, three employees, the named rivals, the claims and the permit. Item 1A
(Risk Factors): going concern, history of losses, the DLE technology's open questions, substitution by non-lithium batteries,
price volatility, dilution, material weaknesses, penny-stock status. Item 7 (MD&A): no revenue, the make-up of the net loss
(stock and principal step-ups paid to noteholders), the working-capital deficit, funding wholly by notes, the warning that the
company may "cease filing the required reports". Item 5 and the S-1/A: the issuance record (note extensions with principal
increases and shares, quarter after quarter) and the reverse splits. Item 13 and the S-1/A: related parties (directors and the
chief executive as noteholders). The history under the former names, from the FY2022 10-K and the XBRL facts.

**The test as the framework states it, applied.** Understanding is "a reasonable probability of being able to asses where the
business will be in 10 years" **[M2000-037]**, which starts with "trying to identify the key variables in that particular
business, and evaluating how predictable they were first" **[M1998-044]**. The key variables here are four, and the filing
itself says none is yet known:
1. **Is there an economic resource at all?** "We have no mineral reserves as defined by Regulation S-K 1300 and have had no
   mining revenue to date." "There has been no exploration or drilling conducted on the property by ABM." "We have not
   calculated mineral and resource estimation." "The only way to determine if the lithium enriched brines exist and can be
   economically produced from the target zones is to drill exploration wells", and the drilling is "subject to obtaining
   financing" (10-K Item 1). The historical well data "cannot be relied upon as an indication that such sites will have
   commercially feasible lithium and magnesium reserves" (Item 1A).
2. **Will the extraction process work on this brine?** "To date, we have not done any testing for the possibility of using DLE
   and will not be able to do any testing until samples of brine are acquired from the target formations" (Item 1); "the
   technology for DLE remains subject to many questions" (Item 1A).
3. **At what cost against rivals, and at what price?** No cost estimate exists ("Cost estimates and authority for expenditures
   for both well tests and the 3D Survey are currently in process", Item 1); the product would be a commodity whose price "may
   fluctuate widely", and the filing itself cites "current oversupply and low prices in battery raw material markets" (Items 1A
   and 1); demand may be cut by "battery technologies that use no, or significantly less, lithium" (Item 1A).
4. **Will the company survive to find out?** The auditor "expressed substantial doubt about our ability to continue as a going
   concern"; working-capital deficit $10,502,348 at 2025-12-31; "If we are unable to obtain sufficient amounts of additional
   capital, we may have to cease filing the required reports and cease operations completely" (Items 1A and 7).

None of the four is predictable, and "If something is not very predictable, forget it." **[M1998-044]**. Not one of them could
be answered by reading more: the first two are answered only by a drill bit the company cannot yet pay for, so this is not a
reading not yet done but a fact that does not yet exist; "If something’s important but unknowable, forget it." **[M2006-076]**.

**Routing.** Q1's list of what it rules OUT names start-ups, on two rows: "Start-ups are not our game." **[L2007-015]** and
"We don’t do startups." **[M2008-088]**. On the filings this is a start-up in every sense the rows use: a business whose operations have
not begun, entered in November 2021 ("We entered the lithium industry in November 2021", Item 1A), with no product, no
customer ("We have no customers and have no off-take agreements", Item 1), no revenue and no resource. The 10-K places itself
among the start-ups by name: it is one of "only three major domestic efforts underway to restart primary production: alongside
startups like Magrathea Metals [...] and Tidal Metals" (Item 1). The shell it grew from was a failed vending business (U-Vend
and BoxScore revenue $1.43M in 2016 and $1.28M in 2018, $80,233 in 2019, none after; XBRL facts from the 10-Ks
`0001213900-18-012036`, `0001213900-19-012471`, `0001213900-21-025789`), so the lithium business has no operating record to
read at all. The speakers' reason for the start-up filter is not a finding of ignorance about a particular business but a
blanket exclusion: "if you blot out startups, there’s a whole layer of complexity that goes out of your life" **[M2008-088]**.
The alternative reading, TOO HARD (NATURE), was weighed: the ten-year economics cannot be foreseen, insiders "would not want to
put down on paper their predictions" **[M2000-105]** about an untested brine and process, and the letter row on new businesses
says "In cases of this sort, any capital commitment must be labeled speculative." **[L2000-026]**. I take the specific item
over the general one: Q1's own list names start-ups as OUT, it was left there when the 2026-10-10 case moved the
continued-invention item to TOO HARD, and a TOO HARD here would hold open a door the filing gives no reason to hold open. Both
readings close the file at Q1, and neither is reopened by a lower price or by research. The disagreement is set down under
WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR.

**Doubt test.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. There is
no doubt to resolve: there is not yet a business whose economics could be inside or outside a circle.

**VERDICT: OUT** at Q1 (a start-up, ruled out by name, **[L2007-015]**, **[M2008-088]**), on the filing facts above, chiefly the
10-K's "We have no mineral reserves [...] and have had no mining revenue to date" and "we have not done any testing for the
possibility of using DLE" (accession `0001493152-26-011615`).

## Q2: WHY IS THE CASTLE STILL STANDING? NOT REACHED (closed at Q1).
## Q3: HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0 and are set down below).
## Q5: WHO RUNS IT? NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7: WHAT IS IT WORTH? NOT REACHED (the reporting figures are computed below, headed COMPUTATION, NOT A CLEARANCE).
## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9: COULD IT RUIN US? NOT REACHED.
## Q10: IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT, at Q1** (a start-up: no reserves, no drilling, no test of the extraction process, no customer, no revenue; ruled out by
name, **[L2007-015]**, **[M2008-088]**). Integrity facts recorded, not judged (see AFTER THE STOP, Q5). The alternative reading,
TOO HARD (NATURE) at Q1, is set down under WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR; either way no research pass is opened and
no lower price reopens the file.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.

**Bearing on Q2 (the castle and the rivals).**
- The rivals the 10-K names: Magrathea Metals and Tidal Metals, as "startups" in primary magnesium (Item 1), and the idled
  US Magnesium LLC plant at Rowley, Utah (Item 1). None files with the SEC: Magrathea Metals Inc. (CIK 1918019) has filed only
  a Form D (2022-03-18) and a D/A (2022-04-14), no periodic report; an EDGAR company search found no registrant named Tidal
  Metals or US Magnesium (searched 2026-10-11). Item 1 otherwise names no competitor ("We are one of many participants in these
  sectors"). **No competitor row could be built from rivals' own filings**, because no named rival files them.
- The filing on its own competitive position: "Many of our competitors possess greater financial resources and technical
  facilities than we do"; "We do not own or license any intellectual property which we consider to be material"; "We
  currently do not have the commercial capabilities required to market and distribute lithium and magnesium" (Item 1). The
  product would be a commodity sold through "intermediaries" (Item 1).
- The field's returns over a cycle: not computable from the record; the company has no operating year in the field.

**Bearing on Q3 (capital).** Everything is ahead: two appraisal wells, a 3D seismic survey, then a pilot and plant, none
costed (Item 1: cost estimates "currently in process"). The S-1/A's estimated net proceeds of $16,251,501 (at an assumed $5.50)
are to fund "pre-production drilling, permitting and geological work". Royalty of 2% of net revenue on the original 102 claims
(Item 1).

**Bearing on Q4 (the accounts). The balance sheets, read first** **[M2025-032]** (`tools/run.py` table from the first-filed
XBRL, checked against the filed 2025 and 2026 statements; USD thousands):

| year-end | total assets | liabilities | equity | cash | debt on the face | accumulated deficit |
|---|---|---|---|---|---|---|
| 2016 | 1,738 | 5,036 | (3,298) | 62 | 696 (partial) | (8,435) |
| 2017 | 910 | 7,197 | (6,287) | 88 | 358 (partial) | (11,618) |
| 2018 | 941 | 7,519 | (6,578) | 63 | 3,484 (partial) | (12,302) |
| 2019 | 101 | 8,066 | (7,965) | not tagged | 4,388 (partial) | (14,198) |
| 2020 | 95 | 11,868 | (11,773) | 24 | 5,175 (partial) | (18,130) |
| 2021 | 110 | 9,153 | (9,043) | 8 | 5,138 (partial) | (16,368) |
| 2022 | 205 | 1,506 | (1,300) | 43 | 714 (partial) | (17,855) |
| 2023 | 357 | 3,373 | (3,017) | 7 | 2,472 | (20,240) |
| 2024 | 323 | 7,130 | (6,807) | 13 | 5,550 | (24,547) |
| 2025 | 396 | 10,693 | (10,296) | 3 | 8,313 | (30,957) |
| 2026-06-30 (10-Q) | 312 | 12,704 | (12,392) | 6 | 9,628 | (36,148) |

What the figures say: shareholders' equity has been negative at every year-end for ten years; assets have never exceeded $1.74M
and are now $311,704, of which $206,000 is the mineral claims and $100,000 prepaid expenses; cash has never exceeded $88,000 at a
year-end. Liabilities fell once, from $9.15M (2021) to $1.51M (2022), and the FY2022 10-K (accession `0001213900-23-031453`)
says how: note principal and interest "converted into" common stock in a series of conversions (for example 76,627,004 and
85,502,658 pre-split shares in single conversions), followed by the 1-for-300 split in 2023 and the 1-for-5 split in 2025. Since
2022 the liabilities have rebuilt to $12.7M, all current. What they cannot say: whether any lithium is there. The income account
in 2025: operating expense $1,863,256 against "Fair value of stock issued for note modification" $2,082,423, loss on
extinguishment $1,744,906 and interest $719,979 (10-K p. 32); in the first half of 2026 those financing items were $2,572,517
and $1,045,346 against $270,000 of new note proceeds and $54,270 of option proceeds (10-Q cash-flow statement). The auditor's one
critical audit matter is the accounting for the convertible notes' embedded features; management reports material weaknesses
("an insufficient complement of qualified accounting personnel", Item 1A). One unreconciled figure: the S-1/A puts the
convertible notes "including accrued interest, totaling approximately $16,750,554 as of August 11, 2026", against $7,890,591 of
convertible notes (including related party) and $1,483,617 of accrued interest on the 2026-06-30 balance sheet, and against the
8-K of 2026-08-25's "total principal of the notes to $11,187,330" after the 15% step-up.

**Bearing on Q5 (integrity facts, recorded, not judged).**
- The chief executive and directors are lenders to the company on the same notes whose maturities they extend: "David E.
  Graber, our Chairman and Chief Executive Officer, and Justin Vorwerk and Jared Levinthal, directors of our company, have made
  loans to us pursuant to convertible promissory notes" (S-1/A, related-party transactions); related-party notes at 2026-06-30
  were $946,531 promissory and $1,507,008 convertible (10-Q). On 2025-10-23 a related party received a $200,000 convertible note
  "for Accrued Payroll" and a $34,200 note "for Accrued Expenses", which then received the 10% principal increase and shares of
  the extension by a most-favored-nation clause (10-K Item 5).
- Each extension pays the noteholders in principal and shares: 2025-08 (to 2025-10-31: 10% principal, $646,498, and 171,715
  shares); 2025-10-31 (to 2026-01-31: 10%, $731,377, and 196,557 shares); 2026-03-16 (to 2026-06-30: 12.5%, $1,045,346, and
  542,066 shares) (all 10-K Item 5); 2026-07-01 (to 2026-08-15; terms not stated in the 10-Q's subsequent-events note);
  2026-08-25 (to 2026-09-30; 15%, $1,459,217, and 612,476 shares if no uplist) (8-K).
- The DEF 14C of 2025-10-28: an evergreen plan reserve of 17.5% of fully diluted shares that may only rise ("in no instance
  shall the number of shares then subject to the 2024 Incentive Compensation Plan be decreased"), approved by written consent;
  "Our executive officers and directors have the power to pass the proposed corporate actions without the concurrence of any of
  the Company's other stockholders."
- Justin Vorwerk resigned from the board on 2026-08-28 "solely due to time constraints" (8-K of 2026-09-01); the S-1/A had named
  him one of four independent directors and the one the board "has determined" would meet the audit-committee financial-expert
  requirements. He is also among the director noteholders.
- The 2023 SPAC merger with Seaport Global Acquisition II was terminated by the SPAC on 2023-11-20 (10-K Item 7).
- An investor presentation was furnished on 2025-10-15 (8-K); not read.

**Bearing on Q6 (issuance).** Shares outstanding: 2,586,982 at 2024-12-31 (restated for the 1-for-5 split), 3,142,371 at
2025-12-31, 3,789,585 at 2026-06-30, 4,402,061 after the automatic issue of 2026-09-30 on the filed terms: up 70% in twenty-one
months. The S-1/A offering would take the count to 10,162,430 before warrants (3,327,273 offered shares with an equal number of
warrants at $6.88, plus 3,045,572 conversion shares). No dividends or buybacks. The rows' view of the serial issuer, "we have
never invested in companies that are hell-bent on issuing shares" **[L2014-015]**, is recorded, not applied.

**Bearing on Q7 (value): COMPUTATION, NOT A CLEARANCE.** Built by Q7's range convention, the reporting figures the brief asks
for; no verdict, no entry language.
- Literal window FY2021 to FY2025, owner cash after every real cost (operating cash flow less stock pay less claim spending),
  USD: (498,741); (972,789); (2,659,671); (817,897); (1,337,774); average (1,257,374). **All-equity basis** (before interest:
  cash interest paid, $60,976 in 2022 and none recorded otherwise, added back): average (1,245,179). **Equity-only basis**
  (after the interest expense as reported, accrued and settled in principal and shares, not cash): average (1,790,245).
- Growth: the series is negative in every year, so a compound rate between end years is meaningless, and so is the rate
  between the first and second halves; by specific (b) the range is **the no-growth case alone**, said so. The four PG
  specifics: growth on aggregate owner cash (none credited); all spending deducted (the claim outlays; there is no
  depreciation to show beside); zero growth after year ten (the no-growth case is zero growth throughout); a price above the
  top closes OUT (it is above). The six more: (a) cycle base: no year is a cyclical peak or trough on the filer's description;
  FY2021 straddles the end of the vending shell and the claim purchase of November 2021, and the FY2022 to FY2025 base,
  average (1,431,789) all-equity, is shown beside; (b) as above; (c) no acquisitions of businesses (the claims are capital
  spending, counted); no merger in the window (the 2023 SPAC deal was terminated); (d) working capital: the operating cash flow
  already carries it, and the growth in accrued expenses and accounts payable flatters it; (e) maintenance-only case: not
  separable, there is no plant; (f) the cap: no growth carried.
- Net debt (all-equity basis), latest filed balance sheet plus the subsequent events the filings state: note principal
  $11,187,330 after the 2026-09-30 step-up (8-K of 2026-08-25) plus accrued interest $1,483,617 less cash $5,704 (10-Q, 2026-06-30)
  = **$12,665,243**; operating leases none. Beside it, on the S-1/A's figure for the convertible notes with interest
  ($16,750,554) plus the promissory notes at 2026-06-30: $18,482,372.
- **(a) VALUE RANGE** (no-growth case alone, at the 5.60% sovereign): whole business (1,245,179) / 0.056 = $(22.2)M; less net
  debt $12.67M = $(34.9)M; **$(7.93) a share** on 4,402,061 shares, all-equity basis (central). Equity-only beside it:
  (1,790,245) / 0.056 = $(32.0)M, **$(7.26) a share**. On 3,789,585 shares: $(9.21) all-equity, $(8.44) equity-only. On the
  FY2022 to FY2025 base: $(8.69). On the S-1/A net debt: $(9.25).
- **(b) FAIR PRICE** (each end case valued at ten percent and the two averaged; here one case): (1,245,179) / 0.10 =
  $(12.5)M less net debt $12.67M = $(25.1)M, **$(5.71) a share, all-equity basis (central)**; equity-only **$(4.07) a share**.
  Tax: the company pays no income tax and has losses; no shelter is priced, since there is no positive owner cash for it to
  shelter. Against the price of **$4.00**.
- Had Q7 been reached it would have closed OUT by the floor tested first: no case earns the floor at any positive price, "we
  don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**; and beneath it, "if we don’t have
  the faintest idea what the future stream is going to look like, we don’t have the faintest idea what it’s worth, now"
  **[M1994-077]**: the past five years of cash say what the company has cost, not what a resource that has not yet been drilled
  would earn. Recorded, not weighed.

**Bearing on Q9 (the target's debt).** Every liability is current. The notes' maturity was 2026-09-30 by the last filed
amendment; no filing after 2026-09-01 reports a further extension, a default or a conversion. Working-capital deficit
$10,502,348 at 2025-12-31 (10-K Item 7) and $12,598,384 at 2026-06-30 (current liabilities less current assets, 10-Q). The 10-K:
"Should additional financing not be available, we will have to negotiate with its lenders to extend the repayment dates of its
indebtedness."

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit e6f1bcd9, before the first EDGAR or tool call); written question by
      question; committed after each section that closed (Q1 at c7a54a63; the remainder in the next commit).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's and was not touched;
      the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (commit
      subjects naming AMBQ's box, two research-folder names, the memory index's queue lines) is declared at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (check script
      `Test Runs/_research 2026-10-11 BLTH/check_cites.py`, output beside it); no E-ids. Every filing fact carries its document
      and accession.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance; the value arithmetic is headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the operating cash flow, stock pay and capital spending, never net income
      (operator rule 5); the sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used (its ten-year balance-sheet table and share counts; its
      owner-earnings window ended at FY2018 and was not used).
- [x] `python tools/check_framework.py` PASS before the commit (recorded in the commit message).
- Not fully done, said plainly: the investor presentation of 2025-10-15 was not read; the terms of the 2026-07-01 extension
  were not found; the gap between the S-1/A's $16.75M and the balance sheet's notes was not reconciled (Q4 not reached).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Q1 gives two boxes for the same company and does not say which governs. Section I says TOO HARD is the box for "a business
whose economics cannot be foreseen (Q1)" and lists Q1 nowhere among the OUT closes, while Q1's own "What it rules OUT" list
names start-ups as OUT on two rows; an exploration-stage issuer with no reserves is both. The 2026-10-10 case moved the
continued-invention item from that list to TOO HARD because its rows' reason was ignorance, and left start-ups in OUT; I read the
leaving as deliberate and took OUT, because the start-up rows give a blanket filter rather than ignorance as the reason, but a
second analyst could take TOO HARD (NATURE) on the same text and the register would then show one kind of name in two boxes. A
sentence in Q1 saying which wins when a start-up is also a business whose economics cannot be foreseen would settle it. Second,
the reporting convention for the fair price assumes a range with two ends; where specific (b) leaves the no-growth case alone,
"the two averaged" is one case, and the run says so; and where owner cash is negative the fair price is a negative number, which
the operator's alert cannot use (no price lies below it). Third, the template's Step 0 asks for `tools/run.py`'s owner cash,
which here stopped at FY2018 because the tool reads capital spending only under the property-plant element and this company's
only capital spending is tagged as mining assets; the figures were taken from the filings instead. Fourth, the equity-only basis
is stated as "owner cash after interest", which for a company whose interest is accrued and settled in principal increases and
shares, not cash, can be read as cash interest (near nil) or interest expense; I used the expense, and said so.
