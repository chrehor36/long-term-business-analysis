# Company Run — MSA Safety Incorporated (NYSE: MSA) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *(Template clause: for a
dispatched blind run the dispatching session fills it at the fold; added 2026-10-06.)*

**Dispatch.** Dispatched analyst, brief `Screens/_daily/_dispatch_brief.md` with slots filled by the dispatching session's
message of 2026-10-10. Template copied to this file before any fetch. Working folder `Test Runs/_research 2026-10-10 MSA/`
(raw filings under its `cache/`, gitignored). Quotation convention of this file: words in quotation marks directly before a bold v5 id are that row's own
words; every other quotation is from the filing named beside it (some are set in single quotes to keep them apart from a row).

**Contamination, declared before any reading of the company:** the session context handed to this analyst showed (a) a git
status snapshot naming research folders of other runs (AYI, ARCB, BDC) and recent commit subjects about other companies'
runs (LOW, LOPE, LRCX, LSTR) with their boxes and prices; (b) a memory index line saying wave 7 was paused and that there are
"57 gate-clearers, nothing buyable" and that "five holding reviews" are owed. None names MSA. None was opened or used. The
dispatching message said earlier MSA run files exist; none was opened, listed or searched, and `Test Runs/` was not listed.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $180.71 (close 2026-10-09, printed by `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, no par value, **38,578,289** as of 2026-07-24
  (10-Q for the quarter ended 2026-06-30, filed 2026-07-31, accession `0000066570-26-000027`; `python Screens/cover_shares.py MSA`).
  Check: issued 62,081,391 less treasury 23,477,085 at 2026-06-30 (10-Q, Note 8) = 38,604,306, the balance-sheet count; the
  cover count is lower by shares bought back or netted after the quarter. No 8-K or prospectus after the 10-Q issues shares
  (8-Ks of 2026-07-09, Autronica closing, paid in cash; 2026-07-21, a director; 2026-07-30, results). The 4.5% cumulative
  preferred (71,340 issued, 52,998 in treasury, $50 par) is nonvoting and immaterial (FY2025 10-K, Note 8).
- **Market cap:** $180.71 x 38.578289M = **$6,971.5M**.
- **Net debt (all-equity basis, Q7's convention):** at 2026-06-30, notes payable and current debt $8.1M plus long-term debt
  $591.6M less cash $200.1M = $399.7M (10-Q balance sheet); plus the subsequent event the 10-Q itself states, Autronica Fire
  and Security bought on 2026-07-09 for "approximately $ 555 million in cash, net of cash acquired", funded by cash on hand and
  the credit facility (10-Q, Note 20): **net debt $954.7M**. Operating leases left out ($59.4M present value at 2025-12-31,
  FY2025 10-K Note 18); no finance leases are disclosed. Enterprise value at the price: $7,926.2M.
- **Sovereign for the earnings currency:** USD, **5.60%**, US Treasury daily par yield curve, 30-year, 10/09/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-12, `0000066570-26-000005`); 10-Q Q2 2026 (filed 2026-07-31,
  `0000066570-26-000027`); proxy DEF 14A filed 2026-03-26 (`0001193125-26-125902`); 10-Ks FY2016 to FY2024 for the span
  (`0000066570-17-000011`, `-18-000009`, `-19-000010`, `-20-000005`, `-21-000016`, `-22-000007`, `-23-000008`,
  `-24-000008`, `-25-000007`); 8-Ks of 2023-01-05 (`0000066570-23-000002`) and 2023-01-06 (`0001193125-23-003028`, the
  MSA LLC sale), 2025-04-04 (`0001193125-25-073401`, the credit agreement), 2026-02-26 (`0000066570-26-000007`, the $500M
  buyback), 2026-05-05 (`0001140361-26-019007`, the Autronica agreement), 2026-07-09 (`0000066570-26-000019`, the closing),
  2026-07-21 (`0000066570-26-000022`). **One figure cross-checked against the filed statement:** cash from operating
  activities FY2025, $363,867 thousand on the filed Consolidated Statement of Cash Flows (10-K FY2025, page 42), against
  $363.9M printed by `tools/run.py` from XBRL: agrees.
- `python tools/run.py MSA`, arithmetic lines only (output kept in the research folder's cache): OCF less stock pay less
  capital spending, FY2023 $20.1M, FY2024 $224.0M, FY2025 $280.2M; five-year mean $151.2M on that basis, $140.9M on the D&A
  basis. Stock pay FY2021 to FY2025 $18.9M, $19.6M, $30.0M, $18.2M, $15.2M; capital spending $43.8M, $42.6M, $42.8M, $54.2M,
  $68.4M; D&A $50.3M, $56.3M, $60.8M, $64.3M, $71.6M. FY2023 is depressed by the $341.2M cash contribution on the sale of MSA
  LLC (filed cash-flow statement, "Contribution on divestiture of MSA LLC"). The tool's yield, implied-growth and v4 lines are
  not used (Part VII, the tooling). Owner cash for Q7 is built from the filed statements at Q7.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would own this if the market shut for five years **[M1997-109]**, and for a maker
of mandated safety equipment the answer turns on the business, not the quotation. The market serves and does not instruct
**[M2006-077]**: the share returned less than the S&P 500, the S&P Midcap 400 and its industrial index over the five years to
2025 by the company's own table (10-K FY2025, Item 5: $100 to $113.87, against $196.16, $154.68 and $191.48), and that says
nothing about value. Margin of safety: if it needs pencil and paper "it’s too close to think about" **[M1996-084]**. No macro
enters **[M2000-094]**: fire-service grant timing and the Middle East are named by the filer as causes of the 2025 and 2026
swings and are not forecast here. Who is paid to tell you **[M2020-037]**: the company's tables lead with adjusted operating
income and adjusted EBITDA, and its performance stock units vest partly on an EBITDA margin (Q4, Q6). The analyst's habit:
look for "what’s wrong in things" **[M2025-013]**, and read "to possibly reject your original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]**: (1) PFAS claims against the retained subsidiary Globe grew from 34
lawsuits and about 1,865 claims (Feb. 2023, 10-K FY2022) to about 467 lawsuits and 10,578 claims (10-K FY2023), about 663 and
8,801 (10-K FY2024), about 1,288 and 22,090 (Feb. 2026, 10-K FY2025), and 1,222 and 21,372 (10-Q Q2 2026); defense costs are
expensed as incurred and no reserve is recorded. (2) The cumulative-trauma liabilities (coal dust, asbestos, silica) brought
charges in most years from 2015 to 2022 and cost $341.2M of cash to shed in 2023; the shedding rests on the buyer's indemnity,
the buyer being a joint venture of R&Q Insurance Holdings and Obra Capital, an arrangement the filer itself calls "subject to
commercial risk" (Item 1A). (3) Fire-service sales fell from $712.7M (2024) to $647.5M (2025), and organic growth was 0.7% in
2025. (4) Growth since 2016 has largely been bought: Globe $215M (2017), Sierra Monitor $33M (2019), Bacharach $329M and
Bristol $63M (2021), M&C $189M (2025), Autronica $555M (2026).

## THE STANDING RULE
The buyer's conduct: a part-interest bought with cash, unlevered, and sized so that its loss cannot touch what the buyer has
and needs, puts no one at risk of ruin: "We are never going to risk what we have and need for what we don’t have and don’t
need" **[M2012-081]**; "Never risk permanent loss of capital" **[L2023-005]**. Nothing in this name requires the buyer to borrow,
post collateral or meet a cash call. The target's own liabilities (legacy and PFAS claims, its debt) are the target's and are
weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" **[M2012-065]**; the product need not be understood, "What is important is that I understand the economic
dynamics of the industry" **[M2011-014]**; the first step is "trying to identify the key variables in that particular business,
and evaluating how predictable they were first" **[M1998-044]**.

**What the business is (10-K FY2025, Item 1 and Note 9).** Three product categories, each sold in both geographic segments:
Detection (fixed gas and flame detection, portable gas detectors; $763.4M, 41% of 2025 sales), Fire Service (self-contained
breathing apparatus, the G1 in the Americas and the M1 abroad; Cairns and Gallet helmets; Globe and Bristol turnout gear;
$647.5M, 34%), Industrial PPE and Other (V-Gard hard hats, fall protection, respirators, ballistic helmets; $463.9M, 25%).
The products must meet standards set by NIOSH, NFPA, ANSI and their overseas counterparts; in the filer's words, purchases are
"non-discretionary" and "often mandated by government and industry regulations" (Item 1), and fire-service demand "is, in
large part, driven by available government funding" (Item 1A). Over 1,800 distributor locations; no customer over 10% of
sales. Two reportable segments by geography: Americas $1,261.8M of 2025 sales and $364.8M of adjusted operating income,
International $613.0M and $93.3M. The filer reports no margin by product category (searched: Notes 2 and 9 and the MD&A, FY2021
to FY2025; no instance found).

**The key variables, and whether they can be foreseen.**
1. *Replacement demand in fire service.* Breathing apparatus and turnout gear are bought by fire departments to a written
   standard and replaced on wear-out and on the standard's revision. Foreseeable in direction (fire departments must keep buying
   certified gear); lumpy in timing (2025 Americas fire service fell "partly due to a shift in Assistance to Firefighters Grant
   (AFG) funding as well as the 2025 U.S. federal government shutdown", MD&A FY2025). A ten-year view does not hang on the timing.
2. *Detection demand.* Fixed and portable gas detection for energy, utilities, HVAC-R refrigerant leaks, water and general
   industry, required by workplace rules. Foreseeable in kind; the electronics and software inside change, the need does not.
3. *Industrial PPE volume.* Hard hats and fall protection follow industrial and construction employment: a slow cyclical, not a
   structural shift.
4. *Liability.* Products sold to protect lives draw injury claims. The cumulative-trauma claims ran for decades and were sold off
   in 2023; the PFAS claims against Globe are "at a very early stage" (Note 21). Their outcome cannot be known from here. It is a
   variable of how sure the cash is and of what could ruin the target, and the framework weighs it there (Q7, how sure; Q9, test
   7, product liability). It does not make the ten-year economics of the product lines unforeseeable, so it is carried, not
   closed on here.

**Change.** "We view change as more of a threat" **[M1999-063]**, and a technology that "could hurt the business as it presently
exists" does not pass the filter **[M1998-008]**. The filer says ‘Approximately half of MSA’s R&D engineers are now focused on
software development’ (10-Q Q2 2026, MD&A) and pushes a connected ‘MSA+’ offering; R&D plus capitalized software was $80.2M in
2025, 4.3% of sales (MD&A FY2025). That is change inside the product, not change that removes the need: a certified breathing
apparatus or hard hat is still required by standard, and the software rides on hardware MSA certifies. Whether the forecast
is about customers or technology **[M2017-019]**, **[M2023-030]**: here it is about what fire departments and plant operators
will be required to buy, which is about rules and customers, not a technology race.

**Can I name the winner, not only the industry** **[M2012-067]**? The business has been the same for decades (founded 1914),
with the North American fire breathing apparatus and the V-Gard hard hat as its named lines; the filer says its competitors
"are principally privately held concerns or subsidiaries or divisions of corporations engaged in multiple lines of business"
(Item 5). Whether the position is a castle is Q2's question.

**Parts.** The two geographic segments differ in margin (Americas 28.9%, International 15.2% adjusted, 2025). The Americas
carries about 80% of five-year adjusted segment operating income (Q2's parts table), so it decides, and it is understood on
the variables above.

**Do I doubt it is inside?** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.
The doubt in this file is about the liability, which is a question of how sure and how much, carried to Q7 and Q9; the economics
of the product lines are within reach. "If something’s important but unknowable, forget it" **[M2006-076]** is applied at Q7 to
the cash estimate, where the PFAS claims bear.

- **VERDICT: IN.** The ten-year economics of a maker of standard-mandated safety equipment can be foreseen in kind
  **[M2012-065]**, **[M2011-014]**; the key variables are identified and, except the liability, predictable in direction
  **[M1998-044]**; the technology component changes the product, not the need **[M1998-008]**. The liability is carried to Q7
  and Q9.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**; the moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The returns the castle protects (MSA's own filings, FY2016 to FY2025).** Operating margin with the cumulative-trauma charges
and the 2023 loss on the MSA LLC sale put back (each charge from the filed income statements and cash-flow statements):
2016 14.3% (no charge line in operating income that year), 2017 13.9%, 2018 16.1%, 2019 15.3%, 2020 15.3%, 2021 14.9%, 2022 17.0%, 2023 20.2%, 2024 21.5%, 2025 19.8%.
Gross margin 45.6% (2016) to 44.1% (2022) to 47.7% (2023), 47.6% (2024), 46.5% (2025). Operating tangible capital (receivables,
inventory, net plant and prepaid less payables, accrued pay and other current liabilities, from the filed balance sheets) was
$315.8M (2016), $416.6M (2019), $628.8M (2022), $698.2M (2025); pre-tax operating income on it, charges put back, about 52%
(2016), 52% (2019), 41% (2022) and 53% (2025). These are not ordinary returns. The charges put back are not forgiven: they are a
cost of this business and are counted at Q4 and Q7; they are put back here only to read what the product lines earn.

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and how permanent* **[M1995-038]**. The customer buys a certified life-safety device: breathing
   apparatus approved by NIOSH and built to NFPA standards, gas detectors certified for hazardous locations, hard hats to ANSI
   and EN standards (10-K FY2025, Item 1). A fire department standardizes on one breathing-apparatus platform, trains on it,
   and buys its cylinders, masks, telemetry and service from the same maker through trained distributors ("The in-depth
   customer training and education provided by our sales associates to our customers is critical", Item 1). The approvals,
   the installed base and the trained channel are permanent in the sense that matters: each new standard edition must be met
   again, and the incumbent with engineers inside the standard bodies meets it first (Item 1, Research and Development).
2. *Would it stand without the lord* **[M1996-037]**? Chief executives changed in 2018 and 2024 (8-Ks of 2018-05-18 and the
   FY2025 10-K's officer list), and the margins rose through both changes. The business does not rest on one person.
3. *The attacker with money* **[M2011-015]**. The evidence is what rich competitors did. 3M, with money, did not build: it
   bought Scott Safety, a maker of breathing apparatus and gas and flame detection, "for $2.0 billion of cash, net of cash
   acquired", for a business with "revenues of approximately $570 million in 2016" (3M 10-K FY2018, Note 3,
   `0001558370-19-000470`). Honeywell, with money, held this field inside a segment that earned 12.9% to 16.3% from 2016 to
   2022, wrote its personal protective equipment business down by $219M plus $15M and sold it in 2025 for $1,157M (Honeywell
   10-K FY2025, `0000773840-26-000013`). Lakeland, a small attacker building a fire-services line by acquisition (Eagle, LHD,
   Veridian), went from operating profit to operating losses of $9.3M and $15.5M in its last two fiscal years (Lakeland
   XBRL, 10-K FY2026 `0001193125-26-159176`). Nobody has shown the castle can be taken by spending.
4. *Pricing power, and the agony before a rise* **[M2005-020]**. Through the inflation of 2021 to 2023 the filer took ‘pricing
   actions’ (10-K FY2021 and FY2023 MD&A) and gross margin rose from 44.1% (2022) to 47.7% (2023) while volume grew
   (‘favorable unit growth’, 10-K FY2022; organic sales +9.9% in 2022, constant-currency +16.1% in 2023). Charging more while selling more
   against entrenched rivals is the mark **[M2000-031]**, and a strong position will "manage to pass through increases in raw
   material costs" **[M2005-017]**. 2026 pricing continues ("price realization", 10-Q Q2 2026, gross margin 49.5% in the quarter).
5. *Unit volume and share of mind.* Organic sales by the filer's own measure, 2021 to 2025: -2.3%, +9.9%, +16.1%, +1.5%, +0.7%
   (10-Ks FY2021 to FY2025; 2023 is the filer's constant-currency figure, no acquisition falling in that comparison). Volume grew over the span; 2024 and 2025 were flat, with the filer naming grant timing and a
   government shutdown for fire service and "double digit growth in detection" (MD&A FY2025).
6. *The low-cost position.* Not claimed by the filer and not shown; the castle is not a cost castle.
7. *The brand.* "the iconic V-Gard helmet brand, a bellwether product in MSA's portfolio for over 50 years" and the trademark
   "MSA" as the one piece of intellectual property whose loss would matter (Item 1).
8. *Would the customer still choose it over the low bid* **[M2017-009]**? For a breathing apparatus worn into a burning building
   the rows' own case is the parachute: "I don’t think if you were buying a parachute you’d want to take the — necessarily take
   the low bid" **[M2001-014]**; and Precision Castparts' customers "don’t simply just take the low bid" **[M2016-006]**. Fire
   departments buy by public tender to a specification, so price enters; the evidence that the low bid does not decide is the
   price-and-volume record in test 4.
9. *Ask the competitors.* Honeywell names "Mine Safety Appliances (MSA)" among its competitors (Honeywell 10-K FY2018, Item 1,
   `0000930413-19-000366`); 3M's answer was to buy the number-two breathing-apparatus maker. MSA says its competitors "are
   principally privately held concerns or subsidiaries or divisions of corporations engaged in multiple lines of business"
   (10-K FY2025, Item 5). Draeger, a leading European rival in breathing apparatus and gas detection, is not an SEC filer and
   its own reports were not read: flagged.
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Widening on margin (about 15% to about 20% from 2016-2021 to
    2023-2025) and in detection (from $634.9M in 2023 to $763.4M in 2025, part of it M&C); narrowing signs in fire service
    in 2025 and in industrial PPE, where Honeywell's exit says the general PPE field is not rich.
11. *What could destroy, modify or reduce it* **[M2000-014]**. Three things, from the filings: liability (PFAS claims against
    Globe; the field-wide pattern is in the competitors' own filings, 3M's "respirator mask/asbestos" litigation and Combat Arms
    earplugs, 3M 10-K FY2025, `0000066740-26-000014`; Lakeland named in 41 PFAS suits, Lakeland 10-K FY2026); a standard
    rewritten in a way that resets the installed-base advantage (Item 1A: changes "could reduce the demand for our products or
    require us to re-engineer our products, thereby creating opportunities for our competitors"); and government funding.
    None of these is shown on the evidence to be filling the moat; the first is weighed at Q7 and Q9.

**The competitor row** (operating margin of the segment that holds the competing line, from each filer's own 10-K; the
segments are wider than MSA's lines, so the row compares fields, not products):

| Filer, segment | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| MSA, consolidated, liability charges put back | 14.3% | 13.9% | 16.1% | 15.3% | 15.3% | 14.9% | 17.0% | 20.2% | 21.5% | 19.8% |
| MSA, Americas segment, adjusted (filer's measure) | n/r | n/r | n/r | n/r | n/r | 22.3% | 25.6% | 29.1% | 30.5% | 28.9% |
| 3M, Safety and Graphics (2016-18), Safety and Industrial (2019-25) | 23.6% | 33.1%* | 25.2% | 20.7% | 23.7% | 20.9% | 9.8%** | 21.2% | 22.7% | 24.9% |
| Honeywell, Safety and Productivity Solutions (2016-22), Industrial Automation (2023-25) | 14.7% | 15.1% | 16.3% | 12.9% | 14.0% | 13.2% | 15.6% | 20.5% | 19.5% | 18.5% |
| Teledyne, Instrumentation | n/r | 13.2% | 14.4% | 18.1% | 19.5% | 21.7% | 23.5% | 25.5% | 26.8% | 27.5% |
| Lakeland, consolidated (fiscal years ending January of the next year) | n/r | 8.9% | 3.6% | 5.5% | 27.6% | 13.5% | 4.9% | 4.8% | -5.6% | -8.0% |

Sources: MSA 10-Ks FY2016 to FY2025 (accessions in Step 0); 3M 10-K FY2018 (`0001558370-19-000470`; 2016 $1,403M on $5,948M,
2017 $2,066M on $6,235M, 2018 $1,720M on $6,827M), FY2021 (`0000066740-22-000010`; 2019 $2,373M on $11,490M, 2020 $2,784M on
$11,734M, 2021 $2,692M on $12,880M), FY2024 (`0000066740-25-000006`; 2022 $1,135M on $11,604M), FY2025 (2023 $2,324M on
$10,956M, 2024 $2,491M on $10,961M, 2025 $2,836M on $11,384M); Honeywell 10-K FY2018 (2016 $680M on $4,625M, 2017 $852M on
$5,639M, 2018 $1,032M on $6,337M), FY2021 (`0000773840-22-000018`; 2019 $790M on $6,104M, 2020 $907M on $6,481M, 2021
$1,029M on $7,814M), FY2022 (`0000773840-23-000013`; 2022 $1,080M on $6,907M), FY2025 (2023 $2,209M on $10,756M, 2024
$1,962M on $10,051M, 2025 $1,743M on $9,401M); Teledyne 10-K FY2018 (`0001094285-19-000064`; 2017 $126.0M on $953.9M, 2018
$147.4M on $1,021.2M), FY2021 (`0001094285-22-000049`; 2019 $200.4M on $1,105.1M, 2020 $213.2M on $1,094.5M, 2021 $253.7M on
$1,166.9M), FY2023 (`0001094285-24-000044`; 2022 $295.3M on $1,254.0M, 2023 $338.3M on $1,326.2M), FY2025
(`0001094285-26-000017`; 2024 $370.3M on $1,382.6M, 2025 $400.4M on $1,457.1M); Lakeland XBRL company facts and 10-K FY2026
(`0001193125-26-159176`). *2017 includes a $458M divestiture gain (3M Note 3). **2022 as recast in the FY2024 10-K.
n/r = not read. Honeywell's and 3M's segments include
much besides safety (warehouse automation, abrasives, graphics), Teledyne's gas and flame detection is a small part of its
Environmental Instrumentation; the row shows that the large diversified rivals' safety-bearing segments earn mid-teens to
mid-twenties margins and the small specialist attacker earns little, over the whole span.

**The parts table** (the filer reports two segments with different margins; adjusted segment operating income, the filer's
measure, 2021 to 2025, 10-Ks FY2022 to FY2025):

| Part | Five-year adjusted operating income | Share | Castle | Decides |
|---|---|---|---|---|
| Americas | $202.5M + $267.4M + $359.6M + $380.1M + $364.8M = $1,574.4M | 79.7% | stands (tests above; fire service, detection, V-Gard) | yes, more than half |
| International | $73.3M + $60.9M + $89.7M + $84.6M + $93.3M = $401.8M | 20.3% | a lower-margin version of the same lines (15.2% in 2025), not shown open | no |

The filer reports no product-category margins (searched, as at Q1), so the castle is read by category in words: fire service
(certified platforms, installed base) is the strongest; detection is contested by Honeywell, Draeger and Teledyne but is the
growing line; industrial PPE is the weakest, the field a large rival has just left.

**The field's returns over the last full cycle.** The safety-bearing segments of the filers above earned mid-teens to
mid-twenties margins across 2016 to 2025, and MSA earned about 41% to 53% pre-tax on its operating tangible capital in the years
read. That is not the standing castle that protects only ordinary returns (Q2, What it rules OUT); "you can have only two competitors and they’re still
terrible businesses" **[M2013-052]** does not describe this field on its filed numbers. The step-up of margin after 2022 is a
change for the better and is not credited at Q2 (a full cycle is required, section C); the castle stands on the 2016 to 2021
margins alone.

**Contrary evidence written down** **[M1997-127]**: fire-service sales fell 9.2% in 2025; International organic sales fell 3.0%
in the first half of 2026; the liability history says the products that protect lives also draw the claims; and "one competitor
is frequently enough to ruin a business" **[M2012-108]**, which is why test 3 was read from what the rich competitors actually
did.

- **VERDICT: IN.** The castle is a set of certified, installed, distributor-served life-safety platforms whose customer does not
  buy a parachute on the low bid **[M2001-014]**; rich competitors bought into it rather than built **[M2011-015]**; prices rose
  with volume through the inflation **[M2005-020]**, **[M2000-031]**; and it protects returns well above ordinary over the
  span **[L2007-004]**. The deciding part, the Americas, stands. The liability threat is carried to Q7 and Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The question: "Has it earned high returns on capital?" **[M1995-051]**, judged on "the capital actually needed in the business"
**[M2010-090]**, on tangible assets for the business and with goodwill counted "In terms of evaluating the job we’re doing in
allocating capital" **[M2011-060]**.

**The capital the business needs (filed balance sheets and cash-flow statements).**
- *Capital spending* ran 2.0% to 3.6% of sales from 2016 to 2025 ($25.5M on $1,149.5M in 2016; $68.4M on $1,874.8M in 2025,
  of which $19.6M was a ‘strategic footprint investment’, MD&A FY2025). Depreciation and amortization was $71.6M in 2025, of
  which $20.7M was amortization of acquired intangibles (Note 14) and $12.0M amortization of capitalized software (MD&A); plant
  depreciation plus software amortization was therefore about $50.9M, against capital spending of $48.8M before the footprint
  project. The maintenance guess **[M2000-144]**, **[L1999-024]**: about the depreciation charge, $45M to $55M a year at
  2025 size; the footprint spending and part of the software spending are growth. This is a guess, labelled as one; the filer
  gives no maintenance figure.
- *Working capital*: receivables 18.2% of sales in 2016, 16.3% in 2025; inventory 9.0% of sales in 2016, 22.1% at the 2022
  supply-chain peak, 18.3% in 2025. Inventory needs have doubled relative to sales over the decade (acquired apparel and
  detection lines, and supply-chain stock); the profit does end the year mostly as cash, not "sitting in the yard"
  **[M2008-036]**, but more of it stays in inventory than it did.
- *Operating tangible capital* (Q2's measure): $315.8M in 2016, $698.2M in 2025. Pre-tax operating income on it, the liability
  charges put back, about 52% (2016) and 53% (2025); about 40% after a tax rate near the filer's 23.9%. On tangible capital this
  is the first kind of business, one that needs little to stand still **[M1998-081]**.

**What the added capital earned.** From 2016 to 2025 operating income with the charges put back rose from $164.2M to $371.8M,
+$207.6M. Over the same span the company spent $849.6M on acquisitions net of cash acquired (Senscient $18.4M 2016, Globe
$216.3M 2017, Sierra Monitor $33.2M 2019, Bacharach and Bristol $392.4M 2021 plus $13.4M for minority interests, M&C $189.3M
2025; cash-flow statements) and added $382.4M of operating tangible capital. Counting goodwill and acquired intangibles, as the
allocation test requires **[M2011-060]**: capital employed of $725.8M in 2016 (tangible $315.8M, goodwill $333M, intangibles
$77M) and $1,729.2M in 2025 (tangible $698.2M, goodwill $731.6M, intangibles $299.1M), an increase of $1,003.4M that earned the
$207.6M: about 20.7% pre-tax, about 15.7% after tax, on the increment. That is a "very satisfactory rate" on the second kind of
growth **[M1998-081]**, below the return on the original tangible base; the growth was bought, and "whether that’s good or bad
depends on what we earn on that incremental" money **[M2001-019]**. Against: the latest purchase, M&C, contributed ‘net sales
and net loss of $41.0 million and $4.8 million’ in its first eight months (Note 15, after amortization and $9.2M of deal costs),
and Autronica's $555M has no filed earnings record yet. Not counted above and real: the cumulative-trauma charges (Q4) and the
$341.2M paid to shed them, which belong to the old base, not to the added capital.

**Caps for Q7.** The organic growth shown over 2021 to 2025, compounded from the filer's own yearly figures (-2.3%, +9.9%,
+16.1% constant currency, +1.5%, +0.7%), is about 5.0% a year in sales; it includes price through an inflation and a 2023
backlog release the filer names (‘backlog conversion’, MD&A FY2023). No rate above the 5.60% discount rate is carried past year
ten **[M1997-095]**.

- **WEIGHS FOR.** The business needs little tangible capital and earns very high returns on it **[M1995-051]**, **[M1998-081]**;
  the growth since 2016 was mostly bought, at about 15% to 16% after tax on all capital including goodwill, a satisfactory
  but lower rate **[M2001-019]**, **[M2011-060]**. The "little or no debt" criterion is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]** (year-ends 2016 to 2025, USD millions;
`tools/run.py` transcription of the first-filed XBRL, read against the filed balance sheets of the 10-Ks FY2016, FY2019,
FY2022 and FY2025; accessions in Step 0):

| Year-end | Assets | Equity | Cash | Receivables | Inventory | Goodwill | Intangibles | Debt (current + long) | Retained earnings | Treasury stock |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,354 | 558 | 114 | 210 | 103 | 333 | 77 | 391 | 901 | 289 |
| 2017 | 1,685 | 598 | 134 | 244 | 154 | 422 | 183 | 475 | 869 | 298 |
| 2018 | 1,608 | 634 | 140 | 245 | 157 | 414 | 170 | 361 | 936 | 298 |
| 2019 | 1,740 | 726 | 152 | 255 | 185 | 437 | 171 | 348 | 1,012 | 305 |
| 2020 | 1,872 | 802 | 161 | 252 | 198 | 443 | 161 | 307 | 1,066 | 328 |
| 2021 | 2,396 | 834 | 141 | 254 | 281 | 637 | 307 | 598 | 1,050 | 330 |
| 2022 | 2,377 | 924 | 163 | 297 | 338 | 621 | 282 | 573 | 1,158 | 361 |
| 2023 | 2,170 | 967 | 146 | 295 | 293 | 628 | 266 | 602 | 1,143 | 363 |
| 2024 | 2,206 | 1,143 | 165 | 279 | 297 | 621 | 246 | 508 | 1,350 | 398 |
| 2025 | 2,554 | 1,367 | 165 | 306 | 343 | 732 | 299 | 581 | 1,546 | 485 |

What they say. (1) Equity grew from $558M to $1,367M, but goodwill and intangibles grew from $410M to $1,031M: most of the
added capital is purchase price (Globe 2017, Bacharach and Bristol 2021, M&C 2025), and tangible equity stayed small. (2) Retained
earnings fell in 2017 ($901M to $869M), in 2021 ($1,066M to $1,050M) and in 2023 ($1,158M to $1,143M): the three years of the
large liability charges and the MSA LLC sale; the income statement's ‘one-time’ items show here as dents in what was kept.
(3) Receivables held at 16% to 19% of sales; inventory rose from 9.0% of sales (2016) to 22.1% (2022) and 18.3% (2025), explained
by the acquired apparel and detection lines and by supply-chain stock the filer names (10-K FY2022, OCF paragraph:
‘increased inventory balances at year-end 2022 to support the higher backlog’), and partly released in 2023. (4) Debt has run
between $307M and $602M with no year of distress; it rose to fund acquisitions and the 2023 contribution (the $250M term
loan of 2023-01-05, 8-K `0001193125-23-003028`) and is now about to rise again for Autronica (net debt $954.7M, Step 0).
(5) A prepaid pension asset grew from $62.9M (2016) to $279.4M (2025): an overfunded U.S. plan, a real asset, whose
‘pension income’ ($14.0M in 2025, non-cash) the cash-flow statement takes back out. (6) Until 2022 the balance sheet carried
the cumulative-trauma reserves and the insurance receivables against them; on the sale both left (current and noncurrent
product liability $65.1M and $324.7M; insurance receivables and notes $172.2M; Note 21, FY2025). What the balance sheets
cannot say: what the PFAS claims against Globe will cost; no reserve is recorded and defense costs are expensed as incurred.

**The real costs.**
- *Depreciation* is a real cost **[L2015-004]**; plant depreciation and software amortization (about $50.9M in 2025) are close
  to capital spending before the footprint project (Q3). Amortization of acquired intangibles ($20.7M in 2025) is customer
  lists, distribution agreements and technology; the technology part is real, and owner cash below does not add any of it
  back as earnings because it is built from cash flow, not from earnings.
- *Stock pay* is expensed ($15.2M to $30.0M a year, Note 12) and is deducted from owner cash, as **[L2021-003]** asks: earnings
  "after interest, taxes, depreciation, amortization and all forms of compensation".
- *Restructuring* was charged in every year read: $12.3M (2015), $5.7M, $17.6M, $13.2M, $13.8M, $27.4M, $16.4M, $8.0M, $9.9M,
  $6.4M, $3.9M (2025): about $134.6M over eleven years. *Currency losses* were charged in every year read (2015 to 2025, $0.2M to
  $19.8M). *Cumulative-trauma product liability* was charged in most years ($156.1M in 2015, $126.4M in 2017 as restated, $45.3M
  in 2018, $28.4M in 2019, $39.0M in 2020, $185.3M in 2021, $20.6M in 2022), and the sale cost a $129.2M pre-tax loss and $199.6M
  after the write-off of the related deferred tax asset (Note 21). The filer's ‘adjusted operating income’ and ‘adjusted EBITDA’
  remove all of these (Note 9: adjusted operating income is operating income ‘excluding restructuring charges, currency exchange, product
  liability expense, loss on divestiture of Mine Safety Appliances Company, LLC’ and more). Restructuring every year is not a one-time
  item: telling owners year after year not to count "business adjustments that are necessary, is misleading" **[L2016-007]**,
  and a large chunk of costs "dumped into a single quarter" is the restructuring device **[L1998-031]**. The liability charges were
  the cost of products sold decades ago; they are real, and their stopping is bought, not natural.
- *EBITDA in the filer's own mouth.* The 10-K's MD&A leads its segment tables with ‘Adjusted EBITDA’ and ‘Adjusted EBITDA %’,
  and the performance stock units of 2022 vested ‘at 220 % of the target award based on both cumulative performance against
  EBITDA margin and revenue growth targets and MSA's TSR’ (Note 12). The rows call the figure "utter nonsense" **[M1998-086]**,
  and say the count of purchases where people "are talking about EBITDA, is going to be about zero" **[M2002-026]**.
- *Guidance.* The 10-K gives an outlook: ‘We expect to generate full-year mid-single digit organic sales growth in 2026’, an
  interest-expense range of $28M to $31M, and pension income up $4M to $5M (MD&A FY2025). That is earnings guidance in the
  sense of **[L2019-006]**.

**The tells, read.** Prepaid or deferred accounts building suspiciously, inventories out of line **[M1995-064]**: inventory rose
relative to sales, with the causes named by the filer and partly reversed in 2023; the prepaid pension is actuarial and its
income is taken out of cash flow. Reserves that move: the liability reserves were raised (2017, 2021), not released into
earnings, and then sold with $341.2M of cash, more than the net book liability (the sale booked a $123.6M pre-tax loss before
costs, Note 21): the opposite of a reserve released to flatter a year. The accounts are clear, long and complete; nothing in
them confuses **[M1995-063]**. No suspicion arises from the statements themselves.

**Owner cash, recast for Q7** (all-equity basis: cash from operations less stock pay, capital spending and dividends to
minority partners, with net interest after a 24% tax added back; filed cash-flow statements; computed in
`Test Runs/_research 2026-10-10 MSA/q7_calc.py`, output in `q7_output.txt`), USD millions, 2021 to 2025:

| Case | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year average |
|---|---|---|---|---|---|---|
| A. Before acquisitions, the 2023 contribution put back (central, see Q7) | 135.3 | 107.8 | 390.9 | 245.8 | 300.2 | 236.0 |
| B. Before acquisitions, literal window (contribution counted) | 135.3 | 107.8 | 49.8 | 245.8 | 300.2 | 167.8 |
| C. Acquisitions deducted, contribution put back | -270.5 | 107.8 | 390.9 | 245.8 | 110.9 | 117.0 |
| D. Acquisitions deducted, literal | -270.5 | 107.8 | 49.8 | 245.8 | 110.9 | 48.8 |
| E. As A with maintenance capital spending only (depreciation for capex) | 145.6 | 113.1 | 391.0 | 253.5 | 317.7 | 244.2 |

The 2021 and 2022 figures carry the old liability's net cash cost (payments less insurance collections, $24.1M and $27.2M; MD&A
FY2022); 2024 and 2025 carry none of it but carry the PFAS defense costs, expensed. 2023 carries a working-capital release
(inventory down $51.6M; other current items +$53.5M) and the $341.2M contribution. Never a net-income proxy (operator rule 5).

- **VERDICT on the accounts: no STOP (neither confusion nor suspicion); WEIGHS AGAINST.** The statements are clear **[M1995-063]**,
  but the featured figures wave away restructuring every year, currency every year and, until 2023, the liability every year
  **[L2016-007]**, lead with adjusted EBITDA **[M1998-086]**, pay on an EBITDA margin, and give guidance **[L2019-006]**. These
  are recorded as a weighing against **[M1994-018]** and carried to Q5 as evidence on the people.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
Two yardsticks: "how well they run the business" against "the hand they were dealt", and "how well that they treat their
owners" **[M1994-008]**; trust ranks above brains **[M2015-047]**; and on integrity "If you’ve got doubts, forget it." **[M2013-088]**.
For a marketable stock the reading tests carry the weight (Q5, the tests): the proxy, the reports, the record over time.

**The people (10-K FY2025 officer list; DEF 14A 2026).** Steven C. Blanco, chief executive since May 2024, with MSA since
2017 (president of the Americas segment, then chief operating officer). The finance chair turned over: Lee B. McChesney
resigned as chief financial officer on 2025-03-21, an interim served until Julie A. Beck (formerly CFO of Terex) arrived on
2025-08-18. The board has a non-executive chairman and a lead independent director, both elected annually (DEF 14A, governance
table); two former chief executives (William M. Lambert, Nishan J. Vartanian) sit on it.

**The integrity record, read.**
- *The long liability, how it was reported.* For a decade the 10-Ks carried a full cumulative-trauma note: claims, reserves,
  insurance receivables, coverage litigation. The reserves were raised in bad years ($126.4M in 2017, $185.3M in 2021), not
  released to flatter a year, and the 2023 sale was disclosed in an 8-K with the purchase agreement and pro forma statements
  (`0001193125-23-003028`), at a price above the book liability (a $123.6M pre-tax loss before costs, Note 21). The structure,
  a Pennsylvania division of the subsidiary before its sale, put the legacy claims in a capitalized entity the buyer owns, with
  an uncapped indemnity and a solvency opinion. Whether one admires it or not, it was done in the open and paid for. The
  filer itself names the risk that remains: the indemnity "is subject to commercial risk" and "may be subject to future
  judicial interpretation" (Item 1A).
- *Reports that dance* **[M1995-111]**, or the key figure left out **[M2007-082]**: the key figures here are price, volume,
  margin by segment and the liability; all are given, with organic sales separated from acquired and currency effects every
  year. The PFAS count is updated every quarter, including when it falls (22,090 to 21,372 claims, 10-Q Q2 2026).
- *Mistakes spoken of* **[L2024-003]**: the 10-K reports the M&C loss of its first year, the fire-service decline and its causes,
  and the lagging five-year share return in its own table. No 10-K I read uses the words of error about a decision; the 10-K
  has no chief executive's letter (the separate annual report was not read).
- *Habits carried from Q4*: adjusted figures that exclude recurring restructuring, currency and, until 2023, the liability;
  adjusted EBITDA featured and paid on; guidance given. They are reconciled line by line to GAAP in the 10-K, and the excluded
  items are named and quantified; they are the habit of their peers, which the rows call "a negative" but not "a total
  exclusionary factor" **[M1994-018]**. Read with the rest of the record they do not raise a doubt about honesty; they raise one
  about how the managers wish the earnings to be seen, which is weighed at Q6 in the pay.
- *Sanctions, restatements, investigations*: none found in the 10-Ks FY2016 to FY2025 or the 10-Q Q2 2026 (searched: recall,
  Department of Justice, subpoena, SEC investigation, Foreign Corrupt Practices, whistleblower, consent decree, restatement;
  no instance found outside risk-factor boilerplate). A $5.0M "net cost for product-related legal matter" in 2024 is named but
  not described (10-K FY2024).

**The proxy, how they treat themselves** **[M1994-009]**. 2025 total pay of the chief executive $6.43M (salary $0.94M, stock
awards $4.12M, cash incentive $0.77M at 81% of target, pension change $0.49M; DEF 14A Summary Compensation Table); pay ratio
about 88 to 1. Target pay is set at "the middle (50 th percentile) of the market" of a 20-company peer group with the help of
a consultant, Pay Governance (DEF 14A). The cash incentive weighs 50% net sales, 25% adjusted EBITDA margin, 25% working capital
to sales; the performance units pay on adjusted EBITDA margin and revenue growth, modified by relative share return; no measure
charges for capital or acquisitions (DEF 14A, Performance Measures). Directors and officers as a group own 278,148 shares,
0.7% (DEF 14A, beneficial ownership, 2026-02-13), much of it from grants. Shareholders approved the pay with 97.2% of votes.
These are ordinary, not egregious; what they say about the money is Q6's.

**Ability, against the hand dealt** **[M1994-008]**. For it: margins up from about 15% to about 20% over the span (Q2) with
price taken through the inflation; the old liability ended at a known price; detection grown into the largest line. Against:
organic growth of 1.5% and 0.7% in 2024 and 2025; a share return below the S&P Midcap 400 Industrials over five years
(10-K FY2025, Item 5); growth bought at about 15% to 16% after tax on all capital (Q3); a chief financial officer gone after a
short tenure. Ability enters as "the degree of certainty" of the cash **[M1999-104]**, not as a gate.

- **VERDICT on integrity: IN.** No doubt about honesty arises from the record read: the liabilities were disclosed, reserved
  upward and paid off in the open, the reports give the figures that matter, and no sanction or restatement was found
  **[M2013-088]**, **[M1995-111]**. **Ability WEIGHS FOR, narrowly** **[M1994-008]**: better margins and a clean exit from the old
  liability, against slow recent organic growth and a growth record bought rather than built. The habits carried from Q4 weigh
  against at Q6, in the pay.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**. Over 2021 to 2025 net income was $823.4M (XBRL NetIncomeLoss: $21.3M,
  $179.6M, $58.6M, $285.0M, $278.9M); dividends paid $374.7M and stock purchases $171.8M (filed cash-flow statements), so
  $276.9M was kept. Market value went from about $5,836M (39,067,902 shares at 2020-12-31 times a close of $149.39) to about
  $6,231M (38,912,629 shares at 2025-12-31 times $160.14; closes are aggregator quotes, flagged): +$395M, about $1.43 of market
  value per dollar kept. But net debt also rose, from about $146M (end 2020: debt $307M, cash $161M) to about $416M (end
  2025), so about $547M of owners' and lenders' money went in for $395M of market value; and the market leg alone misleads
  **[R2009-002]**, so it is read against intrinsic value as well: the Q7 range, computed below, puts value per share well under
  the market. The test is passed on the market leg only, and narrowly or not at all once the borrowed money is counted.
- *Buybacks* **[L1999-023]**, **[L2016-002]**. The programs name no price: the 2024 program ‘authorizes up to $200.0 million’,
  the 2026 program ‘up to $500 million’, and ‘The timing, manner, price and amount of any repurchases under the program will be
  determined by the Company in its discretion’ (8-K 2026-02-26). Prices paid under the programs: 166,292 shares for $29.9M in
  2024 (about $180.00); 501,420 shares for $80.0M in 2025 (about $159.53; Note 8, FY2025); 427,855 shares for $76.1M in the first
  half of 2026 (about $177.92; 10-Q Q2 2026, Note 8). The Q6 convention (a program with no stated price weighs against unless the
  prices paid sit at or below the bottom of the Q7 range): the bottom of the central Q7 range is $84.50 a share and its top
  $137.29 (Q7, computation in `q7_calc.py`); every price paid sits above the top. The buying was done with a borrowed
  margin (net debt rising, and Autronica to be added), not only with funds "beyond the near-term needs of the business"
  **[L1999-023]**. Weighs against.
- *Issuance and deals* **[L2014-012]**. No shares were issued (Note 8: ‘No new shares were issued during the years ended
  December 31, 2025, or 2024’); every acquisition was paid in cash (Globe, Sierra Monitor, Bacharach, Bristol, M&C, Autronica).
  The one STOP here, an all-stock deal by an undervalued acquirer **[L2009-019]**, does not arise, and serial issuance does not
  arise. Value given against value got: $849.6M of acquisitions from 2016 to 2025 earned about 15% to 16% after tax on all
  capital including goodwill (Q3); M&C lost $4.8M in its first eight months; Autronica's $555M has no filed earnings record. No
  post-mortem comparing an acquisition with its original projection was found in the 10-Ks read **[L2014-013]** (searched the
  acquisitions notes FY2017, FY2019, FY2021, FY2025).
- *Dividends*: $2.10 a share in 2025 against diluted earnings of $7.09 (income statement); a steady, rising dividend, about 30%
  of earnings, paid alongside acquisitions funded partly with debt.

**Part B, the pay, the board and the owners.**
- *Pay tied to what the person controls, with a charge for capital* **[M2003-019]**, **[L1994-019]**. The chief executive's cash
  incentive weighs net sales at 50%, adjusted EBITDA margin at 25% and working capital to sales at 25%; the performance units pay
  on adjusted EBITDA margin and revenue growth, modified by share return relative to an index (DEF 14A). Nothing charges for
  the capital used, and sales growth is rewarded however it is bought: "a batting average that does not include a cost of
  capital is a phony batting average" **[M1995-010]**, and "you get what you reward for" **[M2016-083]**. The 2022 units vested at
  220% of target (Note 12).
- *Who designs it.* A compensation consultant (Pay Governance) and a 20-company peer group set target pay at the median, the
  process the rows call "ratchet, ratchet, and bingo" **[M2012-095]**; "comp committees have become slaves to comparative data"
  **[L2005-015]**.
- *The board.* A non-executive chairman who is the former chief executive (Nishan J. Vartanian, chief executive until May 2024)
  and a lead independent director. Directors and officers together own 0.7%, much of it granted, not bought; the rows want
  directors with "huge and true ownership interests" **[L2002-033]**.
- *The owners as partners.* Candid on the liability and the segments (Q5); guidance given (Q4); the five-year return shown
  honestly in the company's own table, below its indices.

- **WEIGHS AGAINST.** Part A: cash deals only and no issuance, but buybacks with no stated price at prices above the whole Q7
  range **[L2016-002]**, a retention record that passes only on the market leg **[R2009-002]**, and growth bought with rising debt.
  Part B: pay on sales growth and adjusted EBITDA margin with no capital charge **[M1995-010]**, set by consultant and peer group
  **[M2012-095]**; ordinary in size, ill-aimed in kind. The one STOP of Part A does not arise.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**: how
many birds, how sure, how soon, at "the yield on long-term U.S. bonds" **[L2000-021]**; credit only "for whatever net cash is left
every year" **[M1998-080]**; held as "a range of possibilities" **[L2000-024]**. All arithmetic is in
`Test Runs/_research 2026-10-10 MSA/q7_calc.py`, its output in `q7_output.txt`.

**The inputs.**
- *Cash.* Owner cash after every real cost, all-equity basis, five-year average 2021 to 2025, from Q4's table. The figure is
  after stock pay, all capital spending, dividends to minority partners and the PFAS defense costs (expensed), and before
  net interest after a 24% tax (Q7, On what the floor is earned).
- *The 2023 contribution.* **CONVENTION of this run:** the $341.2M paid in 2023 to shed the cumulative-trauma liabilities is put
  back into 2023's owner cash for the central base, and the literal window that counts it is shown beside. Rationale: it
  settled an obligation that existed before the window and no longer exists, as a repaid loan would; averaging it into the
  base would charge it once as paid and again, in effect, every year forever. The old liability's ordinary net cash cost stays
  in 2021 and 2022 ($24.1M and $27.2M), so the base still carries a liability cost of about the old run-rate in two of five years.
- *The window's end years* **[L2005-003]**. The filer describes 2021 as a year of "ongoing supply chain constraints" with an
  elevated backlog (10-K FY2021) and 2023 as a year of "backlog conversion" (10-K FY2023); no full cycle of owner cash can be
  marked peak to peak or trough to trough in the ten years read, so specific (a)'s cycle base cannot be built; the literal
  five-year window is used, and a four-year window that drops 2021 is shown beside as a sensitivity.
- *Acquisitions, specific (c).* The default pair deducts acquisitions ($405.8M in 2021, $189.3M in 2025) and credits total
  growth. Total growth here is meaningless: the series after acquisitions runs -$270.5M, $107.8M, $390.9M, $245.8M, $110.9M,
  changing sign; between halves it runs from -$81.3M to $178.4M; so by specific (b) the default pair is the no-growth case
  alone, said so. The organic pair leaves acquisitions out and credits only the organic growth the filer reports, compounded
  2021 to 2025 at 4.96% a year (Q3). The organic pair is taken as the central range (**CONVENTION of this run**, rationale: with
  growth unmeasurable, the default pair charges $595.1M of purchases and credits none of what they bought, the double charge
  specific (e) forbids in its own words, "Never charge all spending and also cap the growth that spending bought").
- *Autronica*, closed 2026-07-09 after the window: its $555M is in net debt, and it is credited at nothing, no earnings being filed
  (specific (c)).
- *Rate and term*: 5.60%, ten years at the growth shown, then no growth (zero nominal), the cap respected (4.96% is below 5.60%).

**The range** (per share, after net debt of $954.7M, 38.578M shares; price $180.71):

| Case | Base | Growth | Value range a share | Width |
|---|---|---|---|---|
| **Central: organic pair, contribution put back** | $236.0M | 0% to 4.96% | **$84.50 to $137.29** | 1.48x |
| Organic pair, maintenance-only capital spending (specific (e)) | $244.2M | 0% to 4.96% | $88.29 to $142.92 | 1.48x |
| Organic pair, literal window (contribution counted) | $167.8M | 0% to 4.96% | $52.91 to $90.44 | 1.48x |
| Default pair: acquisitions deducted, no growth (specific (b)) | $117.0M | none | $29.41 | n/a |
| Default pair, literal | $48.8M | none | -$2.18 | n/a |
| Equity-only (owner cash after net interest, less Autronica's after-tax interest at the revolver's 4.56%) | $199.1M | 0% to 4.96% | $92.15 to $136.68 | 1.48x |
| Sensitivity: four-year window 2022-2025 (2021 dropped), organic growth 6.86% | $261.2M | 0% to 6.86% | $96.15 to $183.75 | 1.91x |
| Sensitivity: central with Autronica credited at its cost | | | $98.89 to $151.68 | |

**How sure** **[M1999-104]**. The cash above is surer than most: certified products, an installed base, regulated demand (Q1, Q2).
It is less sure on one count the range does not price: the PFAS claims against Globe (21,372 claims at mid-2026), no reserve, no
estimate, ‘at a very early stage’ (Note 21); and the indemnity on the old liabilities rests on a run-off buyer's capital (Q9).
"If something’s important but unknowable, forget it" **[M2006-076]**: the unknowable item here can only lower the figures, so it
does not change the close below.

**The floor and the close.** At $180.71 the enterprise value is $7,926.2M. The central case returns about 4.5% a year at that price
with the full organic growth, about 3.7% with half of it (`q7_output.txt`): below the long bond's 5.60% and far below the floor of
about ten percent (**CONVENTION**, Q7), where "there’s just a point at which we drop out of the game" **[M2003-149]**. The price
is above the top of the central range ($137.29), above the top of the equity-only range ($136.68), above every case built by the
convention, and inside only the most generous sensitivity (four years, 6.86% growth, top $183.75), which is itself no screamer:
"It should scream at you" **[M2009-005]**. A price above the top of the range closes OUT however wide the range (specific (f)).
The width is 1.48x on the central case, under the three-to-one line, so the close is not TOO HARD.

- **Value range:** $84.50 to $137.29 a share (central) against $180.71. **Closes: OUT.**
- **Fair price (a reporting figure, never a verdict; Part VII):** **$47.70** a share, all-equity basis (the midpoint case, the
  $236.0M base at half the shown growth, 2.48%, for ten years and then flat, discounted at the 10% floor: $2,795M of enterprise
  value less $954.7M of net debt); **$61.11** on the equity-only basis (the $199.1M after-interest base, same construction,
  against the shares alone). After the company's own tax, no conversion (Q7, Whose tax). On the literal window the all-equity
  figure would be $26.76. No cheap price is reported.
- **VERDICT: OUT** at Q7 on price: valued, and the price does not clear the floor **[M2003-149]**; the bottom boundary a buyer would
  pay "a reasonable price in relation to" **[L2013-012]** is $84.50 against $180.71.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (the file closed OUT at Q7). Facts under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** The draft would have the buyer do nothing: inaction is the default when Q7 closes OUT.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts under AFTER THE STOP.

---
## THE BOX
**OUT at Q7, on price.** Value range $84.50 to $137.29 a share (central: organic pair, all-equity, the 2023 contribution put back;
literal window $52.91 to $90.44; equity-only $92.15 to $136.68) against $180.71 (2026-10-09). Fair price $47.70 all-equity,
$61.11 equity-only (reporting figures, not verdicts). Q1 IN, Q2 IN, Q3 weighs FOR, Q4 no STOP and weighs AGAINST, Q5 integrity
IN and ability weighs FOR narrowly, Q6 weighs AGAINST. No integrity facts were left unjudged (Q5 was reached and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2; each with its source **[M1997-127]**.)*

**Bearing on Q8 (the alternatives).** The 30-year Treasury yields 5.60% (Treasury par curve, 2026-10-09). At $180.71 the central
case returns about 4.5% a year with the full organic growth and about 3.7% with half of it (`q7_output.txt`).

**Bearing on Q9 (the target's debt and exposures).**
- *Debt.* Net debt $954.7M after Autronica (Step 0), against 2025 owner cash before interest of $300.2M and the filer's adjusted
  EBITDA of $472.9M (about 2.0 times); interest paid $32.1M in 2025 against operating income of $371.8M. Revolving facility $1.3B,
  $1.0B unused at 2025-12-31, maturing 2030; fixed-rate notes to 2036; maturities $8.2M (2026), $33.2M (2027 and 2028),
  $8.2M (2029), $293.5M (2030) (10-K FY2025, Note 13). Covenants: net leverage not over 3.50 to 1, 4.00 to 1 for four quarters after
  an acquisition; fixed charges coverage at least 1.50 to 1 (Note 13). The criterion "little or no debt" **[R1997-001]** is a
  whole-business criterion; the debt is moderate, not little.
- *Liabilities that grow because the owner is rich* (Q9, test 7). MSA sells helmets: V-Gard, Cairns, Gallet and ballistic helmets
  (Item 1); the row is "the last thing Berkshire should do is own a helmet company" **[M2014-083]**, and "we have passed up some
  businesses, because we were worried about the product liability potential" **[M2001-008]**. The legacy claims sold in 2023
  included asbestos (‘coal dust, asbestos, silica, and other legacy exposures’, 8-K 2023-01-05); the row "So we don’t go near
  asbestos" **[M2001-032]** is carried in the framework as a candidate, not a ruling (Q9). PFAS: Globe named in 1,222 lawsuits
  of 21,372 claims at mid-2026, no reserve, defense costs expensed (10-Q Q2 2026, Note 19); MSA LLC's
  PFAS (foam) claims passed to the buyer. The field: 3M reports "respirator mask/asbestos" litigation as a continuing special item
  and paid for its Combat Arms earplugs ($14,785M of net litigation costs in 2023; 3M 10-K FY2025, segment note); Lakeland is
  named in 41 PFAS suits (Lakeland 10-K FY2026).
- *Whose promise it depends on* **[M2003-084]**. The legacy liabilities rest on the indemnity of MSA LLC and its owner, Sag Main
  Holdings, a joint venture of R&Q Insurance Holdings and Obra Capital, "not subject to any cap or time limitation", with a
  six-year limited guaranty from MSA Worldwide of MSA Jacksonville's own indemnity running the other way (8-K
  `0001193125-23-003028`; Note 21). The present condition of R&Q and Obra was not read in any primary document in this run.
- *Pension.* The U.S. qualified plan is overfunded (prepaid pension cost $279.4M; pensions and other benefits liability $143.8M,
  2025-12-31); no U.S. contribution required "in many years" (MD&A FY2025).

**Bearing on Q12.** The products protect firefighters, miners and plant workers; the newspaper test **[M2008-011]** would read the
mission well and the PFAS claims (fabrics "tested and certified to meet current National Fire Protection Association safety
standards", supplied to Globe and containing PFAS for water and chemical resistance, Note 21) badly. None of the named
businesses (casinos, tobacco, loading schemes) applies.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `3d1ddf00`, before the first EDGAR request); written question by
      question; committed after each (Step 0 to Q1 `774d31ad`, Q2 `14306329`, Q3 `5607fa97`, Q4 `046d88a0`, Q5 `0dba3801`,
      Q6 `9571408e`, Q7 `0c8d6c18`), each with a pathspec of the two paths only. The first commit's `git add` of the research
      folder failed while the folder held only the ignored `cache/`; a small notes file was added so the folder could be committed.
- [ ] If dispatched to an analyst: the brief allowed the per-question commits (yes); the lock is the dispatching session's (not
      checked by the analyst, by the brief); the fold is the dispatcher's. Not mine to tick.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; `Test Runs/` was not listed. What was seen
      by accident is declared at the top (git-status and commit subjects of other runs; a memory line).
- [x] Every v5 id resolves and every quoted fragment beside an id is in its row (`check_quotes.py`, run before each commit);
      every filing fact carries its document and, for the filings, the accession in Step 0 or beside it.
- [x] The order was kept; Q7 was the first STOP to fail; Q8 to Q12 are NOT REACHED and nothing after Q7 is a clearance.
- [x] Owner cash after every real cost (stock pay, all capital spending, minority dividends; the liability and PFAS costs that ran
      through cash), never a net-income proxy (operator rule 5); sovereign from the Treasury; aggregator quotes flagged (the price;
      the year-end closes used in Q6).
- [x] Contrary evidence written down as found (foundations, Q2); facts for later questions under AFTER THE STOP; no integrity
      facts were left unjudged, so no flag in the box line.
- [x] Not a point-in-time run; rows of every date are admissible.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS (run 2026-10-10 before the closing commit; all checks OK), and `check_quotes.py` PASS.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) *Q7 specifics (b), (c) and (e) collide for a serial acquirer.* The default pair deducts acquisitions and credits total growth;
when that growth changes sign, (b) leaves the no-growth case alone, so the default pair charges every purchase and credits nothing
it bought, the double charge (e) forbids in words. For MSA that gives $29.41 a share (or -$2.18 on the literal window) against an
organic pair of $84.50 to $137.29. I took the organic pair as central and confessed it as a CONVENTION of this run; the framework
should say which pair governs when the default pair degenerates. (2) *A one-time settlement inside the window has no rule.* Specific
(a) treats aberrational first and last years only; the $341.2M paid in 2023 to shed a pre-existing liability sits mid-window and
moves the base from $236.0M to $167.8M. I put it back as a settled obligation (CONVENTION of this run) and showed the literal window.
(3) *"The price at which the midpoint of the range earns the floor"* does not say whether the midpoint is the midpoint growth case or
the midpoint value; I used the midpoint growth case discounted at the floor. On that construction the equity-only fair price
($61.11) exceeds the all-equity one ($47.70), because the equity-only route capitalizes the interest cost at ten percent, below what
the debt costs to repay at face; the convention is right to make the all-equity figure central. (4) *Product liability has no place
before price.* For a business whose largest unknown is a mass tort, Q1's "important but unknowable" and Q9's test 7 point at the same
fact; the framework routes it to Q9, a weighing reached only after Q7, so a liability that could dominate value is never weighed if
the price fails first, and would be weighed after the value is set if it passes. Here it did not matter (the price failed on the
range before any liability charge), but the routing should be stated. (5) The template's Q7 line names "the six specifics" while Q7
carries four PG specifics and six more; harmless, but a reader can miss the first four (aggregate growth, all capital spending, zero
nominal growth after year ten, a price above the top closes OUT), all applied here.

**Where the brief was wrong.** (a) The dispatching message calls Honeywell's comparator its "safety products segment"; Honeywell
reports no such segment: safety sat in Safety and Productivity Solutions (2016 to 2022) and then Industrial Automation (2023 to 2025),
and Honeywell sold its personal protective equipment business on 2025-05-21 for $1,157M after a $219M write-down (Honeywell 10-K
FY2025). (b) The message's list of acquisitions omits the largest, Autronica Fire and Security, $555M in cash, agreed 2026-05-05 and
closed 2026-07-09, which adds $555M to net debt and moves every per-share figure by about $14; it also omits Bristol Uniforms ($63M,
2021). (c) The canonical brief's commit recipe (`git add -- "<run file>" "<research folder>"`) fails with "pathspec did not match" when
the research folder holds only the ignored `cache/`, which is exactly the state the brief's own instruction to keep raw filings under
`cache/` produces before any notes are written; the whole add aborts and the run file is not staged either.
