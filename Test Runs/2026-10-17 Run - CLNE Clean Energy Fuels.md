# Company Run — Clean Energy Fuels Corp. (Nasdaq: CLNE) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

Dispatched blind run (operator rule ten). The lock in `Screens/_daily/` is held by the dispatching session; this analyst
did not write or touch it. Working folder: `Test Runs/_research 2026-10-17 CLNE/` (notes, fetch and arithmetic scripts,
their outputs; raw filings sit in its gitignored `cache/` and are re-fetchable from EDGAR by the accessions below).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (1e3d2fb2): `PORTFOLIO.md` read for this one ticker; the operator does not hold CLNE (no line names CLNE or Clean Energy).*

**Contamination, declared and not used.** (1) To check for a lock and for my own paths I listed `Test Runs/` filtered on
today's date; the listing showed the file and folder names of other runs dated 2026-10-17 (none of this company, under any
name or ticker). No such file was opened. (2) The session context showed recent commit subjects, one of them a fold of
another company's run (a gas utility), with its box and range, and a memory index line on the queue and on holdings
reviews owed. None of it concerns this company; none was used. (3) The `Screens/_daily/` listing showed the lock file
exists. Nothing else from any blind-listed file was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.50 (close 2026-10-16; aggregator quote via `tools/run.py`, **flagged per operator rule 5**: a live
  quote from an aggregator, not a primary source).
- **Shares by class** from the latest filing's cover: one class, common stock, $0.0001 par: **220,445,015** shares as of
  2026-07-30 (Form 10-Q for the quarter to 2026-06-30, filed 2026-08-06, accession `0001104659-26-092061`;
  `python Screens/cover_shares.py CLNE`). Checked against the balance sheet of the same 10-Q: 220,358,166 shares
  "issued and outstanding" at 2026-06-30, no treasury shares shown, so issued less treasury equals outstanding. No 8-K or
  prospectus after the 10-Q issues shares (the 8-Ks of 2026-08-06 and 2026-10-06 are results and an officer change;
  the Forms 3 and 4 of 2026-10-07 are a new officer's holdings). Potential shares, all out of the money at $1.50
  (10-Q Note 13): Amazon warrant 58,767,714 at $13.49 (18,806,507 unvested), Stonepeak warrant 20,125,451 at $5.50 and
  $6.50, options 19,099,280, RSUs 6,428,198.
- **Market cap:** 220.445M × $1.50 = **$330.7M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (issuing authority; `tools/run.py`, which calls `tools/sources.py`).
- **Filings read** (operator rule 4):
  - Form 10-K for FY2025, filed 2026-02-24, accession `0001104659-26-019215` (Items 1, 1A, 7, 8: statements and notes).
  - Form 10-Q for Q2 2026, filed 2026-08-06, accession `0001104659-26-092061` (statements, debt, equity, warrant notes).
  - DEF 14A for the 2026 meeting, filed 2026-04-30, accession `0001104659-26-052378` (ownership, pay, board).
  - 8-Ks: 2026-04-23 CEO succession `0001104659-26-047340`; 2026-06-23 COO `0001104659-26-076660`; 2026-10-06 CFO
    succession `0001104659-26-113910`; 2025-11-21 two TotalEnergies directors resign `0001104659-25-115054`; results
    8-Ks 2026-02-24 `0001104659-26-019128` and 2026-08-06 `0001104659-26-092030` (cover pages only read).
  - Earlier 10-Ks for the cycle and the cash-flow history: FY2023 `0001558370-24-002174` (2021 to 2023), FY2020
    `0001558370-21-002638` (2018 to 2020), FY2017 `0001368265-18-000010` (2015 to 2017).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025,
  $85,529 thousand on the filed consolidated statement of cash flows (10-K `0001104659-26-019215`, page 61), equals the
  85.5 that `tools/run.py` transcribed from XBRL. Also checked: total stockholders' equity $565,067 thousand at
  2025-12-31 on the filed balance sheet against run.py's 559 (run.py prints the parent-only figure, $559,421 thousand;
  the difference is the noncontrolling interest, $5,646 thousand).
- **`python tools/run.py CLNE`, arithmetic lines only** (output kept at `Test Runs/_research 2026-10-17 CLNE/runpy_out.txt`).
  Its owner-earnings columns are wrong for this filer in three ways, each checked against the filed cash-flow
  statement: (a) its capex takes only "purchases of and deposits on property and equipment" and misses two filed
  investing lines that are capital spending for this business, "payment and deposits on equipment and manure rights for
  ADG RNG production projects" (2021 to 2025: 5.8, 9.0, 20.3, 15.0, 34.2) and "investments in other entities", the cash put
  into the RNG joint ventures (78.9, 89.7, 73.5, 32.9, 16.5); (b) its stock-pay column takes employee stock pay only and
  misses the "stock-based sales incentive charges", the Amazon warrant, added back inside operating cash (83.6, 24.3,
  60.6, 60.8, 66.1); (c) its 2025 D&A of 98.6 includes $54.4M of accelerated depreciation and retirement charges for
  the Pilot station removal (10-K MD&A, "Fueling Station Equipment Removal"). It did flag the 2025 paid-in-kind interest
  of $15.0M inside operating cash; that is right. My recast is in `owner_cash.py` / `owner_cash_out.txt` in the research
  folder and is used below.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which for this company turns on cash the business itself has not yet shown it can produce (one profitable
year in eleven, below). The market serves and does not instruct: "It just tells us prices" **[M2006-077]**; a share price
that has fallen to $1.50 instructs nothing about value either way. Margin of safety: "if you have to actually do it on —
with pencil and paper, it’s too close to think about" **[M1996-084]**. No macro forecast enters: "macro conclusions are —
just never enter into the discussion" **[M2000-094]**; this bears hard here, because the earnings of this business are,
on the filer's own account, set largely by government programmes whose future is a political forecast, which is exactly
the kind of forecast the foundations keep out of the decision. Who is paid to tell you: the 10-K's market sizing (its
4.1 million Class 8 trucks burning over 40 billion gallons a year) and its growth language come from the seller of the
fuel. The row: "you do not get impartial advice" where the fee depends on the answer **[M2020-037]**; so the seller's
projection is not used **[M2011-083]**. The analyst's habits: look for "what’s wrong in things" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the filer says of its own market that "it is difficult
to accurately predict demand for our vehicle fuels" and that adoption in heavy-duty trucking has been "slower than we
anticipated" (10-K FY2025, MD&A, Key Trends); (2) net loss in ten of the last eleven years, accumulated deficit
$1,234.6M at 2025-12-31; (3) goodwill written off in full, $64.3M, in Q1 2025 because the market value of its single
reporting unit fell below carrying value; (4) the federal alternative fuel tax credit (AFTC), $20.7M to $23.8M of revenue a
year in 2021 to 2024, "expired on December 31, 2024 and has not been renewed"; (5) the anchor station customer for LNG,
Pilot, did not renew (agreement expired 2025-08-01); (6) the JV dairy-RNG programme produced 2.7M GGEs in 2025 against
300.1M GGEs sold, after about $376M of company cash put into the JVs and ADG equipment in 2021 to 2025 (cash-flow statements), and the bpJV lost
$45.0M in 2025 (Note 3); (7) two of the bpJV's dairy partners entered Chapter 11 (East Valley 2024, Ash Grove 2025);
(8) TotalEnergies' two directors resigned from the board on 2025-11-18. Written down as found; weighed where each bears.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not by the business: a part-interest bought for cash, unlevered and
sized within means, cannot ruin the buyer however the target fares, and the rule binds the buyer's conduct: "Never risk
permanent loss of capital" **[L2023-005]**; no "bet the company" decisions **[M2014-039]**; "borrowed money has no place
in the investor's tool kit" **[L2014-005]**. The rule is met if the purchase is unlevered and small; the target's own
debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The lines of evidence chosen** (departure from the canonical brief, stated: derived from the 10-K's Items 1, 1A and 7, as
the brief requires). From Item 1: the revenue lines (fuel sales; RIN and LCFS credits; AFTC; station construction; O&M),
the RNG supply model (third-party offtake plus JV dairy projects), the customer markets (refuse, transit, trucking,
airports), and the competition paragraph. From Item 1A: the dependence on Environmental Credits and tax credits, the
dependence on truck and engine makers, the history of losses, the indebtedness, the three large equity holders. From
Item 7: the sources-of-revenue table, the volume table, the key trends, the AFTC expiry, the Pilot non-renewal, the
dairy-partner bankruptcies, the goodwill impairment, the Stonepeak loan. Those are the lines read below and after the stop.

**What the business is, from the filing.** It buys RNG (from over 150 third-party sources under offtake agreements, and a
little from its JVs) and conventional gas, and sells it as CNG and LNG to fleets through 582 US and 27 Canadian stations
it owns, operates or supplies; it generates RINs and LCFS credits by dispensing RNG into vehicle tanks and sells them,
sharing their value with the RNG producer by negotiation ("we and the supplier negotiate to determine what percentage
share of the value of the Environmental Credit each party will retain"); it builds and maintains stations. Single
reportable segment (10-K Note on segments). Volume flat: 288.2M GGEs (2023), 297.5M (2024), 300.1M (2025).
Revenue flat for a decade: $384.3M (2015), $402.7M (2016), $346.4M (2018), $425.2M (2023), $424.8M (2025).

**The key variables, and how predictable they are** **[M1998-044]**:
1. *The value of the Environmental Credits.* RIN and LCFS revenue was $45.3M of $424.8M revenue in 2025 and the AFTC a
   further $23.8M in 2024; the filer's gross margin before D&A in 2025 was $114.9M (revenue less product and service
   cost of sales), so the government programmes carried roughly 40% of the margin in 2025 and more before the AFTC
   lapsed. Their value is set by regulators year by year: the EPA's renewable volume obligations, CARB's carbon-intensity
   scores and LCFS targets, and Congress for the AFTC and the Section 45Z credit (the OBBBA of 2025-07-04 "modifies,
   accelerates the phase‑out of, or otherwise affects a number of tax incentives"; 45Z runs to 2029). The filer: the
   credit markets "have been volatile and unpredictable" (2025 LCFS from $75.50 to $40.00); dairy projects "are heavily
   dependent on the LCFS credits [...] for commercial viability. If CARB reduces the CI score [...] the number of LCFS
   credits [...] will decline."
2. *Whether the heavy-truck fleet adopts natural-gas engines over diesel, battery and hydrogen.* The filer's "biggest
   competition" is diesel; it is "dependent on the production of vehicles and engines [...] by manufacturers, over which
   we have no control"; California's zero-emission truck rules (ACT, ACF) were partly repealed or tied up in litigation in
   2025, and the filer says the transition "has the potential to create favorable market conditions for RNG but could
   also harm our vehicle fueling business. Future regulatory actions will be required". Its own fleet fund contracted
   zero trucks in 2025.
3. *The share of the credit it keeps* against RNG producers who can sell to rival dispensers, utilities and other users
   ("increased demand for RNG may also result in greater competition for RNG supply").

**The tests applied.**
- Where will it be in ten years **[M2012-065]**: "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years". I cannot get one. Each of the three variables is a decision of a
  regulator, a legislature or a truck buyer facing those regulators, and the history in the filings is of exactly such
  decisions swinging the result: the AFTC lapsed and was revived retroactively more than once (AFTC revenue $26.7M in
  2018, $47.1M in 2019, $19.8M in 2020), and the one profitable year in eleven (2019, net income $13.3M) is the year with
  the largest AFTC.
- Do the past statements tell me the future ones **[M2008-033]**: no. The past statements are a record of programme
  values, not of a business's own earning power; the largest programme item in them has ended, and the 10-K says
  "investors in our securities should not rely on the results of one period as an indicator of performance in any other
  period."
- Is it important and knowable: the credit values and the truck-drivetrain outcome are the most important facts for the
  ten-year cash and are not knowable from any filing; they are set by future politics. "If something’s important but
  unknowable, forget it." **[M2006-076]**.
- Would the insiders write it down **[M2000-105]**: the filer, after 28 years in the industry, writes that the market "is a
  relatively new and developing market. As a result, it is difficult to accurately predict demand for our vehicle fuels"
  and that adoption has "been slower than we anticipated". The insiders decline to write the forecast down; the
  forecast that the first question needs is the one they say they cannot make.
- Can I name the winner, not just the industry **[M2012-067]**, **[L2009-005]**: even granting growth in RNG, the filer's
  own competition paragraph lists diesel, renewable diesel, biodiesel, ethanol, electric and hydrogen vehicles, truck-stop
  owners, utilities and industrial gas companies; which fuel wins heavy trucking in ten years is not something I can see.
- The speakers' own nearest case: of another policy-supported renewable fuel, "in terms of figuring out what an ethanol
  plant is going to be earning on capital five or ten years from now, it’s far easier for us to figure out whether people
  will be drinking Coca-Cola" **[M2006-016]** (a row about an industry, weighed with the tests above, not deciding alone).
- Do I doubt it is inside **[M2002-092]**: yes. "if you have doubts about something being into your circle of competence,
  it isn’t."

**Which cause** (section I, the two causes). The deciding question, the ten-year value of government-created credits and
the drivetrain the heavy-truck fleet will choose under shifting rules, is not a fact a filing not yet read could supply:
it is a forecast of regulators' and legislators' decisions that the filer itself says it cannot make, and studying the
programmes harder would not produce it: "We couldn't solve this problem, moreover, even if we were to spend years
intensely studying those industries." **[L1993-023]**. That is NATURE, not WORK: the insiders would not write it down
**[M2000-105]**. A lower price does not reopen it **[M2000-038]**.

**VERDICT: TOO HARD (NATURE).** The economics ten years out depend on credit values and drivetrain choices set by future
government action, which the filer says it cannot predict (10-K `0001104659-26-019215`, Items 1A and 7) **[M2006-076]**,
**[M2000-105]**, **[M2002-092]**, **[M2006-013]**. The file closes here; Q2 to Q12 are NOT REACHED, and every figure below is
a fact found after the stop or a COMPUTATION, NOT A CLEARANCE.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (Q1 closed the file). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The eight-to-ten years of balance sheets were read in Step 0 (`tools/run.py`'s table, checked against the
filed balance sheets of the FY2025, FY2023, FY2020 and FY2017 10-Ks); what they show is under AFTER THE STOP.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures are computed below, under AFTER THE STOP, headed
COMPUTATION, NOT A CLEARANCE (operator rule 3).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1**: the ten-year economics rest on the value of government-created fuel credits and on
the drivetrain the heavy-truck fleet adopts under shifting federal and California rules, a forecast the filer itself says
it cannot make; no research pass is opened, and a lower price does not reopen the box **[M2000-038]**. Integrity facts
recorded, not judged (Q5, below). For the owner's reference only, COMPUTATION, NOT A CLEARANCE: value range −$6.85 to
−$0.40 a share all-equity (−$6.98 to −$0.53 equity-only) against $1.50; no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).

### Bearing on Q2 (the castle)
- **The filer names no rival by name.** Its competition paragraph lists categories only: diesel first ("The biggest
  competition for RNG use as a vehicle fuel is diesel"), then renewable diesel, biodiesel, ethanol, electric and
  hydrogen vehicles, truck-stop and station owners, utilities, industrial gas companies; and it says "some of our
  competitors have substantially greater financial, marketing, and other resources than we have" (10-K
  `0001104659-26-019215`, Item 1, Competition).
- **CONVENTION of this run (the rivals chosen):** since the 10-K names none, I chose the two SEC-filing companies whose
  business is nearest (RNG supply plus dispensing and credit generation): OPAL Fuels Inc. (CIK 0001842279) and Montauk
  Renewables, Inc. (CIK 0001826600). Rationale: Montauk's own 10-K lists "Clean Energy Fuels Corp" first among
  "competitors in the United States that have a similar business model to our own", with Opal Fuels, U.S. Gain,
  Brightmark, Gevo Inc. and AMP Energy (Montauk 10-K FY2025, filed 2026-03-11, accession `0001193125-26-102364`, Item 1,
  Competition). U.S. Gain, Brightmark and AMP Energy: not SEC filers as far as I found (not read). Gevo files with the
  SEC but is a fuel producer of another kind (not read). bp (owner of Archaea) and TotalEnergies are CLNE's JV partners
  and foreign filers (not read).
- **The competitor row, same metrics, 2021 to 2025 summed** (the filers' XBRL from their 10-Ks, `peers_out.txt`; one
  figure each cross-checked: OPAL total revenues 2025 $348,975 thousand on its filed statement of operations, 10-K filed
  2026-03-16, accession `0001628280-26-017908`; Montauk total operating revenues 2025 $176,382 thousand, accession above;
  CLNE from its own statements):

  | 2021 to 2025, USD M | revenue | operating income | operating margin | OCF − capex − stock pay |
  |---|---|---|---|---|
  | CLNE (capex incl. ADG equipment and JV investments; Amazon charge excluded) | 1,941.7 | −419.4 | −21.6% | −417.5 |
  | OPAL Fuels (PP&E capex only) | 1,306.7 | 54.2 | 4.1% | −430.0 |
  | Montauk Renewables (PP&E capex only) | 880.7 | 88.5 | 10.0% | −89.9 |

  CLNE's operating income was negative in every year 2009 to 2025 except 2018 ($3.9M) and 2019 ($9.9M) (XBRL, as filed).
- **The field's returns over the last cycle, from the filings:** the distributor (CLNE) lost money at the operating line
  over the whole span; the two producers earned thin operating margins and, after capital spending, consumed cash in
  aggregate. This is the evidence Q2's test of a standing castle that protects only ordinary returns would read;
  recorded, not judged.
- **Ask the competitors.** OPAL's 10-K: the California dispensing market "has become increasingly competitive because of
  increasing supply of RNG with these relatively low CI scores. As such, fleet operators using vehicles fueled by natural
  gas have been able to demand RNG marketers like us provide them with greater economic incentives for allowing us to
  dispense the fuel at the Fueling Stations, typically in the form of a greater share of our marketing fee or a greater
  share in the monetary value of the Environmental Attributes" (OPAL 10-K `0001628280-26-017908`, Item 1A). CLNE's own
  MD&A: oil and diesel price conditions "have led us to reduce the prices we charge some customers for our fuels, which
  has reduced our profit margins."
- **The claimed advantage.** The filer's stated edge is access to dispensers: "we calculate that we have access to more
  fueling stations and vehicle fleets than all our competitors combined"; it estimates it generated 31% of US D3 RINs
  and 46% of CA LCFS Bio-CNG and Bio-LNG credits in 2025 (10-K, Item 1). Against it: its largest LNG station customer,
  Pilot, did not renew (agreement expired 2025-08-01; $54.4M of accelerated depreciation and retirement charges); its
  California fleet fund contracted zero trucks in 2025; volume grew from 245.8M GGEs (2021) to 300.1M (2025) while
  operating income stayed negative.

### Bearing on Q3 (capital)
- Capital put in, 2021 to 2025 (cash-flow statements): PP&E $259.2M, ADG equipment and manure rights $84.3M,
  investments in JVs $291.5M; a further $26.8M into JVs and $1.2M of ADG equipment in H1 2026 (10-Q).
- What it has returned: the JVs reported losses (CLNE's equity-method losses $12.5M, $26.6M, $26.7M in 2023 to 2025);
  the bpJV, $446.7M of assets at 2025-12-31, had revenue of $7.2M and a net loss of $45.0M in 2025 (10-K Note 3); JV and
  consolidated dairy production 2.7M GGEs in 2025 against 300.1M GGEs sold. The bpJV sold $29.5M of investment tax
  credits for $27.2M in 2025.
- Return on capital: operating income negative on total assets of $1,056.7M (2025); no year in the window earned a
  positive operating return.

### Bearing on Q4 (the accounts); balance sheets read first **[M2025-032]**
- **Balance sheets, 2018 to 2025** (filed statements; USD M): stockholders' equity 508 (2018), 533, 514, 747 (2021), 720,
  727, 713, 565 (2025, incl. NCI); accumulated deficit −689 (2018) to −1,235 (2025), so $546M lost in seven years;
  goodwill 64 throughout, then 0 after the Q1 2025 impairment; long-term debt 75 (2018), 33, 82, 23, 145, 261 (2023,
  Stonepeak), 265, 227 (carrying; $250M principal); cash plus short-term investments $219.5M (2024), $158.3M (2025),
  $140.2M (2026-06-30); investments in other entities from $0.65M put in during 2020 to $262.3M carried (2025); receivables 69 (2018) to 101 (2025),
  about a quarter of revenue; inventory 35 to 44.
- **What moved and why:** equity was held up by issuance, not earnings: additional paid-in capital rose with the 2018
  TotalEnergies purchase ($83.4M of stock issued that year), the 2021 at-the-market sales ($204.5M gross), the Stonepeak
  warrant ($42.4M), the Amazon warrant charges ($295.4M cumulative 2021 to 2025) and stock pay. The owners funded the
  losses. What the figures cannot say: the future value of the credits that carry the margin, and whether the JV dairy
  assets ($262M carried) will ever earn.
- **The real costs:** employee stock pay $15.0M, $26.5M, $23.3M, $10.8M, $8.9M (2021 to 2025); the Amazon warrant charges
  (non-cash contra-revenue at grant-date fair value; the warrants, at a $13.49 strike, are far out of the money at $1.50,
  so dilution today, calculated as the row calculates it **[M2014-004]**, is nil; but the charge
  records a price concession made in equity); depreciation $44.2M to $54.7M a year against PP&E capex of $23.1M to
  $100.9M; paid-in-kind interest $15.0M in 2025.
- **EBITDA in the filer's mouth:** the proxy pays the annual bonus 30% on "Adjusted EBITDA", a non-GAAP measure, $67.6M
  achieved in 2025, the year of a $222.0M net loss (DEF 14A `0001104659-26-052378`, CD&A). Recorded as the habit the
  framework carries from Q4 to Q5; not weighed.

### Bearing on Q5 (the people): integrity facts recorded, not judged
- **Pay against results:** the CEO's 2025 bonus was 111% of salary ($867,973) in a year with a net loss of $222.0M; for
  2025 the compensation committee "established base, middle, and maximum targets that were somewhat below our actual
  achievement in 2024" (DEF 14A, CD&A). Bonus metrics: Adjusted EBITDA 30%, strategic initiatives 20%, fuel volume 15%,
  RNG volume 15%, and fuel margin per GGE (which excludes the Amazon warrant charges). The rows the framework would read
  here: a featured "adjusted" figure **[L2016-006]**, declared targets reached **[L2002-041]**, and "If you’ve got doubts,
  forget it." **[M2013-088]**. Not judged.
- **Succession and turnover:** founder-CEO Andrew J. Littlefair (CEO since 2001) succeeded on 2026-04-22 by Barclay F.
  Corbus, SVP Strategic Development since 2007 and before that co-CEO of WR Hambrecht + Co, the bank that managed the
  company's IPO; Mr. Littlefair stays as a director and paid consultant (8-K `0001104659-26-047340`). New COO 2026-06-23
  (8-K `0001104659-26-076660`). CFO Robert M. Vreeland departed by agreement; the corporate controller, Jason J.
  Armstrong, became CFO 2026-10-06 (8-K `0001104659-26-113910`). Two TotalEnergies-designated directors resigned
  2025-11-18, "not due to any disagreement" (8-K `0001104659-25-115054`).
- **Candour:** the 10-K's risk factors and MD&A are plain about losses, credit volatility, slow truck adoption and the
  AFTC lapse; I found no tell of dishonesty in the accounts read. The 10-K still calls the market "a relatively new and
  developing market" in the company's 28th year.
- **Ownership:** TotalEnergies 51.0M shares (23.18%, including shares under a voting agreement), Stonepeak 20.1M warrant
  shares (9.10%), BlackRock 6.68%, GMO 6.01%; the largest insider, Mr. Littlefair, 1.48% (DEF 14A).

### Bearing on Q6 (the money and the owners)
- **Buybacks:** 14,301,158 shares bought for $31.3M since the programme began in 2020 (about $2.19 a share); 4,913,818
  shares in 2025 for $7.9M (about $1.62); none in H1 2026; buying beyond $15M needs the lender's consent (10-Q Note 15).
  The programme names no price.
- **Issuance:** the 2018 TotalEnergies placement, the 2021 ATM sales ($204.5M), warrants to a customer (Amazon,
  58.8M shares) and to a lender (Stonepeak, 20.1M shares); the row Q6 would read on serial issuance is **[L2014-015]**;
  not weighed. No all-stock acquisition found.
- **Retention:** no dividend; accumulated deficit −$1,234.6M at 2025-12-31.

### Bearing on Q9 (the target's debt)
- Stonepeak senior secured first-lien term loan: $250.0M principal after a $65.0M voluntary prepayment on 2025-12-03
  (with a $5.3M prepayment penalty; $11.5M loss on extinguishment), 9.50% fixed, interest only, balloon due 2029-12-12;
  covenants on maximum total leverage, minimum interest coverage and minimum liquidity; call premium to an 11.5% lender
  IRR and a 1.40 multiple; secured on substantially all personal property (10-Q `0001104659-26-092061`, Note 12). $15.0M
  of 2025 interest was paid in kind. Operating income has not covered interest in any year since 2019.
- Net debt at 2026-06-30: debt $250.2M principal plus finance leases $3.0M, less cash (including restricted) $59.2M and
  short-term investments $81.0M: **$113.0M**. Operating leases ($90.5M) left out, and said so.
- Sudden demands: take-or-pay gas purchase contracts (Item 1); credit compliance failures can force it to "purchase
  credits in the open market to cover any credits we have contracted to sell" (Item 1A).

### Q7 figures: COMPUTATION, NOT A CLEARANCE
*Headed as operator rule 3 requires. No entry language; reporting figures for the owner only (Part VII, The owner's
price). Built by Q7's range convention as written; nothing here is a verdict.*

- **Owner cash after every real cost** (`owner_cash.py`, `owner_cash_out.txt`; USD M): operating cash as filed, less
  employee stock pay; the equity-only series also less paid-in-kind interest; the all-equity series instead adds back
  cash interest paid less interest income. Maintenance-only (e): depreciation as the maintenance guess, the filing stating
  no maintenance figure; depreciation "is not inappropriate in most companies to use as a proxy for required capital
  expenditures" **[M1998-127]**; the guess is mine, as the rows allow **[M2000-144]**, **[L1999-024]**. All-spending: PP&E
  capex, ADG equipment and JV investments, net of other investing receipts.

  | year | all-equity, maintenance-only | equity-only, maintenance-only | all-equity, all spending | equity-only, all spending |
  |---|---|---|---|---|
  | 2021 | −16.1 | −18.9 | −78.4 | −81.2 |
  | 2022 | −16.0 | −14.5 | −101.4 | −99.9 |
  | 2023 | −19.9 | −25.2 | −164.2 | −169.5 |
  | 2024 | 22.5 | 9.1 | −46.9 | −60.3 |
  | 2025 | 36.0 | 17.4 | 11.8 | −6.8 |
  | **five-year average** | **1.3** | **−6.4** | **−75.8** | **−83.5** |

  The literal window is the base: the filer calls neither 2021 nor 2025 a cyclical peak or trough (a); the 2025 D&A is
  taken without the $54.4M Pilot charge, a removal the filer ties to one contract.
- **The specifics applied.** Growth (b): the maintenance-only series changes sign (first two years average −16.1, last two
  +29.3), so a compound rate is meaningless and no growth is carried. Growth spending (e): about $376M put into JVs and
  ADG equipment in 2021 to 2025 bought 2.7M GGEs a year of production and equity-method losses, so the growth bought is
  worth less than its cost; the maintenance-only no-growth case is the top of the range and the all-spending case the
  bottom: "growth can destroy value" **[L2000-023]**. Acquisitions (c): no business bought for cash in the window; small
  asset sales are counted net in other investing; the JV contributions are capital spending, not acquisitions; the
  serial-acquirer test does not apply. Working capital (d): inside operating cash. Cap (f): no growth carried. Tax: the
  company pays almost no income tax (income taxes paid $41 thousand in 2025) under a valuation allowance; at the statutory
  rate the tax on a $1.3M average would be about $0.3M, immaterial, so no shelter is priced. Basis: all-equity, net debt
  $113.0M at 2026-06-30, operating leases left out **[L2017-004]**.
- **Value range (all-equity, central):** whole business $23.9M (top: $1.3M a year at no growth at 5.43%) to −$1,396M
  (bottom), less net debt $113.0M, over 220.445M shares: **−$6.85 to −$0.40 a share, against $1.50.** Equity-only beside:
  **−$6.98 to −$0.53.**
- **The floor, tested first:** no case earns about ten percent at the price **[M2003-149]**. Market value plus net debt is
  $443.7M; ten percent needs $44.4M of owner cash a year before interest; the most generous case averages $1.3M (0.29%),
  and the best single year of eight (2025, $36.0M) gives 8.1%. The price is above the top of the range, which Q7's
  convention closes OUT however wide the range. Had Q7 been reached, it would have closed OUT on the floor.
- **Fair price (Part VII: each end valued at ten percent, the two averaged; after the company's own tax):** all-equity
  **−$2.20 a share** (top case −$0.45, bottom −$3.95); equity-only **−$2.04** (−$0.29 and −$3.79). No case computed gives
  a positive fair price.
- **Beside the central figures:** (1) the Amazon warrant charge counted as a cost: range −$11.78 to −$5.34, fair −$4.88
  all-equity; (2) the AFTC removed from the base years, since it "expired on December 31, 2024 and has not been renewed":
  range −$8.31 to −$1.87, fair −$3.00 all-equity; (3) the no-growth top case alone, by (b)'s last sentence: fair −$0.45
  all-equity, −$0.29 equity-only (`range_out.txt`).
- **Q6's buyback line, from this computation:** the 2025 purchases at about $1.62 sit above the top of the range
  (−$0.40), so by the framework's test they would weigh against, value being "entirely purchase-price dependent"
  **[L2016-002]**, **[L1999-023]**; recorded, not weighed.

## RESEARCH PASS
Not opened: the box is TOO HARD (NATURE), not WORK; and no case of the COMPUTATION earns the floor at the price, so no
answer to any question could make the name a purchase at $1.50 (Part VII, When a research pass is run).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1 closed, and again for
      the facts after the stop, the computation and this audit.
- [x] Dispatched run: the brief allowed per-question pathspec commits of my two paths; the lock is held by the dispatching
      session (seen present, not touched). The fold into the register is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. Seen by accident and declared above:
      today's run-file names in a dated listing of `Test Runs/`, one fold commit subject, a memory index line.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_ids.py` in the research folder (no E-ids; every id
      present; every quoted fragment beside an id found in its row); every filing fact carries its accession.
- [x] The order was kept; Q1's STOP closed the run; nothing after it is a clearance; every later figure is a fact found or
      a COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; run.py's capex and
      stock-pay columns corrected against the filing; sovereign from the US Treasury; the price flagged as an aggregator's.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor bars any row.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text and ids ignored.
- [x] `python tools/check_framework.py` PASS before the final commit (result in `notes.md`).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a long-losing, policy-dependent business.** The routing sends a business whose ten-year economics
cannot be foreseen "because its industry changes fast" to Q1 TOO HARD, and the commodity paragraph says a dependence on a
commodity price is never by itself a STOP at Q1. Neither says where a business goes whose margin is largely a
government-created credit and whose market depends on emissions rules: is a credit price a commodity price (then Q1
passes, and Q2 would very likely close OUT on the field's returns), or is a regulator's decision a forecast the insiders
will not write down (then Q1 TOO HARD, NATURE)? I chose the second, on the filer's own statement that it cannot predict
demand and with **[M2006-016]** weighed beside the tests, but a second analyst could reach Q2 OUT on the same evidence.
The boxes differ (TOO HARD NATURE closes the file for good; OUT invites a re-look at a price alert), though here no price
could matter, since every case computed is negative. A sentence on government-created revenue would settle it.
(2) **Customer equity incentives.** Q4 names stock pay as a real cost but says nothing of warrants given to a customer and
booked as contra-revenue at grant-date value; when such warrants are far out of the money, the charge and the economic
cost diverge. I left the charge out of the central owner cash and showed it beside. (3) **An expired subsidy in the base
years.** Q7 averages five years but says nothing of a revenue line the filing states has ended (the AFTC); I kept the
literal window central and showed the base without it beside. (4) **A negative fair price.** Computed as Part VII says,
both ends negative give a negative figure, which the alert tooling may not expect; a rule that a non-positive fair price
sets no alert may be wanted. (5) `tools/run.py`'s capex column misses this filer's ADG equipment line and its JV
contributions, and its stock-pay column misses stock-based sales incentives; both were corrected by hand from the filed
statements.
