# Company Run: Distribution Solutions Group, Inc. (Nasdaq: DSGR), 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
44b0daad). Dispatched blind analyst; working folder `Test Runs/_research 2026-10-12 DSGR/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-12, after the run was committed: not held (`PORTFOLIO.md` does not name DSGR, Distribution Solutions Group, Lawson, TestEquity or Gexpro).*

**Contamination, declared.** Nothing about this company from any other run, review or list was seen. Seen by accident
in the session's opening context, not opened and not used: the repository map and the operator protocol (which the brief
requires); the git status listing, which names other companies' research folders (AYI, ARCB) and university folders; the
last five commit subjects, about another company's run and fold; and a one-line memory index entry describing the queue
in general terms (counts of runs, no company named that bears on this one). None names DSGR, Lawson Products,
TestEquity or Gexpro Services.

**Lines of evidence chosen for this name** (the brief's departure: derived from the 10-K's Items 1, 1A and 7, not from a
list). (1) The parts: four reportable segments with different economics (Item 1; Note 14), read under Q2's business of
parts. (2) The 2022 combination: a reverse acquisition in which the controller's two companies were merged into Lawson
for stock (Item 1; FY2022 10-K Note 1). (3) The acquisition programme: the strategy names acquisitions as a growth engine
(Item 1, "Acquisition Strategy"; Item 1A, integration risk; Note 3). (4) Customer concentration at Gexpro Services (Item
1: top 20 customers 83% of segment revenue). (5) Debt: $704.4 million, all floating, covenants (Item 1A, Item 7A, Note
9), and the $800 million 10.000% notes for the going-private merger. (6) The controller: LKCM and J. Bryan King at about
79%, a "controlled company" (Item 1A), related-party dealings (Note 16), the pending take-private (8-K of 2026-07-16).
(7) Margins against the field (Item 1A: competitors that "price some merchandise more competitively"; Item 7,
segment results). (8) Controls: Item 1A says acquisitions "has in the past resulted in" material weaknesses.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $35.03 (close 2026-10-09; `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
  The merger consideration is $35.00 a share in cash (8-K of 2026-07-16, accession 0001193125-26-306263). The stock
  closed at $19.31 on 2026-03-13, the day before the controller's first proposal (PREM14A of 2026-09-01, accession
  0001193125-26-377452, Background of the Merger) and at $29.90 on 2026-02-27 (FY2025 10-K, Item 5).
- **Shares by class:** one class, common stock $1.00 par: **46,255,422** as of 2026-07-31 (10-Q for 2026-06-30, cover;
  accession 0000703604-26-000041; `python Screens/cover_shares.py DSGR`). Check: issued 47,924,087 less treasury
  1,685,772 = 46,238,315 at 2026-06-30 (same 10-Q, balance sheet), consistent with the cover. The 8-Ks filed after the
  10-Q (2026-09-10 accession 0001193125-26-387187; 2026-10-05 0001193125-26-413150; 2026-10-08 0001193125-26-417257)
  report no issuance by the company; the notes are issued by the merger sub into escrow.
- **Market cap:** $1,620.3M (46,255,422 x $35.03).
- **Sovereign for the earnings currency:** 5.60% (USD; US Treasury daily par yield curve, 30-year, 10/09/2026;
  `python tools/sources.py`). Earnings currency USD (most revenue in the US; Canada, Europe and Latin America the rest,
  FY2025 10-K Note 4).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-03-05, accession 0000703604-26-000008), Items 1, 1A, 5, 7,
  7A, 8 (statements and Notes 1 to 16), 9A; 10-K FY2024 (0000703604-25-000012), FY2023 (0000703604-24-000021), FY2022
  (0000703604-23-000033), Lawson Products 10-K FY2021 (0000703604-22-000019), for the segment, customer and cash-flow
  history; Lawson 10-Q for 2022-03-31 (0000703604-22-000027); 10-Q for 2026-06-30 (0000703604-26-000041); DEF 14A of
  2026-04-01 (0001628280-26-022845), pay tables; PREM14A of 2026-09-01 (0001193125-26-377452), Background of the
  Merger; DEFM14A of 2022-02-10 (0001193125-22-034688), the Gexpro Services and TestEquity sections; 8-Ks of 2026-07-16
  (merger agreement), 2026-10-05 and 2026-10-08 (the notes), 2025-12-22 (0001193125-25-328786, the credit agreement)
  and 2025-04-02 (0001193125-25-070858, the restricted-payments amendment).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $83,849
  thousand on the filed cash-flow statement (FY2025 10-K), against 83.8 in `tools/run.py`; depreciation and
  amortization $80,879 thousand against 80.9; purchases of property, plant and equipment $21,015 thousand against 21.0.
  All agree.
- **`python tools/run.py DSGR`, arithmetic lines only:** OCF 102.3 / 56.5 / 83.8 (FY2023 to FY2025, USD M), stock pay
  7.9 / 5.2 / 6.7, D&A 63.6 / 74.4 / 80.9, capital spending 15.3 / 13.7 / 21.0, rental-fleet purchases 9.3 / 9.5 / 19.5
  (an alternate the tool does not choose; included here, net of rental-fleet sales, Note 5), finance-lease principal 0.5 /
  0.7 / 0.6. The tool's D&A includes amortization of purchased intangibles ($46.5M in FY2025, Note 6), so its "OE D&A"
  column is not used; depreciation proper (PP&E 18.6, capitalized software 4.2, rental fleet 11.6, FY2025, Note 5) is
  read from the filing. Its yield, growth-implied and "points over" lines are not used (Part VII).
- **The balance sheets, eight to ten years, read here because the file closes before Q4** (`tools/run.py` table; filed
  statements behind it). Two entities are in the table and must not be read as one: FY2016 to FY2021 are Lawson Products
  alone (the accounting acquiree of 2022); FY2022 onward are the combined company, whose history before April 1, 2022
  is TestEquity and Gexpro Services (FY2022 10-K, Note 1: "TestEquity and Gexpro Services were treated as a combined
  entity as the accounting acquirer"). What moved, and why:
  - *Lawson alone, 2016 to 2021:* equity 61 to 133, retained earnings 42 to 111, goodwill 6 to 35, no long-term debt
    until 2021 (93, the year of the Partsmaster purchase and the inventory build). A small, nearly unlevered
    distributor.
  - *The combined company, 2022 to 2026-06-30:* equity 563, 662, 641, 649, 655; goodwill 348, 400, 463, 468, 474;
    intangibles 228, 254, 270, 226, 206. **Tangible equity is negative or near zero in every year** (-13, +8, -92, -45,
    -25 at 2026-06-30). Debt on the face 412, 568, 734, 700, 730 (principal 733.8 at 2026-06-30). Retained earnings
    negative throughout (-26 to -25): net income from 2023 to mid-2026 sums to about $1M. Equity grew by
    issuance: the 2022 stock mergers, 3.4 million earnout shares and the $100 million rights offering of 2023 (FY2025 10-K,
    statement of equity).
  - *Working capital against sales:* receivables 13.6%, 13.9%, 13.7% of revenue (FY2023 to FY2025), then 331.6 at
    2026-06-30 against first-half revenue of 1,053.7, about 15.7% annualized, a $60.3M rise in six months; the allowance
    for credit losses rose from 2.4 to 6.5 to 8.0 and bad-debt expense from 0.9 (FY2024) to 4.4 (FY2025). Inventory 20.1%,
    19.3%, 17.8% of revenue, then 378.7 at 2026-06-30. Operating cash flow for the first half of 2026 was $1.6M against
    $28.5M a year earlier (10-Q, cash-flow statement).
  - *What the figures do not say*, "what they don’t say and what they can’t say" **[M2025-032]**: the goodwill and intangibles are mostly the price of deals between
    parties under one control (the 2022 reverse acquisition stepped Lawson's assets up to the $351.5M fair value of the
    stock exchanged, FY2022 10-K cash-flow supplement), so the book equity measures what the controller's companies were
    priced at when combined, not capital put in by outside owners.

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. For a
minority buyer today the answer is not about the business at all: a merger agreement signed by the controller cancels
every share not held by the affiliated stockholders for "$35.00 per share" in cash (8-K, 0001193125-26-306263), with an
outside date of 2026-12-31. A purchase at $35.03 buys either that cash claim, or, if the deal fails, the business at a
price the market set at $19.31 before the bid. The buyer would be focusing on what the next fellow (here the controller)
pays, which is "not our game" **[M1997-052]**. Who is paid to tell you: the $35.00 is called fair by an adviser paid
by the company (PREM14A, William Blair opinion), and the controller's own adviser argued that $31.00 reflected the
company's long-term value (PREM14A, Background); neither opinion is used, since advice is not impartial "when there’s
(an) enormous amount of fees possible from one action, and no fees applicable from another action" **[M2020-037]**. The
proxy's projections are not consulted: "we’ve never looked at a projection in connection with either a security we’ve
bought or a business we’ve bought" **[M1995-050]**. **Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**): (1) tangible equity negative in
every combined year and retained earnings never positive (Step 0); (2) Gexpro Services' top 20 customers rose from 63% of
its revenue (2020, 2022) to 75%, 82% and 83% (2023 to 2025) (FY2022 to FY2025 10-Ks, Item 1; DEFM14A 2022); (3) the
company's operating margin (2.2% to 4.0%, FY2021 to FY2025) is a fraction of every rival the 10-K names that files (Q2);
(4) receivables jumped $60M in the first half of 2026 while operating cash fell to $1.6M (10-Q); (5) a material weakness
at TestEquity as of 2022-12-31 (FY2022 10-K, Item 9A); (6) the pending take-private by the controller at a price set
against a pre-bid quote of $19.31.

## THE STANDING RULE
Owning this does not put the buyer at risk of ruin if it is bought with the buyer's own money and sized as the questions
allow: the rule binds the buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t
need" **[M2012-081]**, and "you never want to use borrowed money" **[M2020-003]**. Nothing in this name requires
borrowing to own it. The target's own debt is weighed at Q9 (not reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**. The product can stay opaque if "I understand
  the economic dynamics of the industry" **[M2011-014]**.
- **A holding company, read by its parts** (Q1's holding-company paragraph, with the threshold of Q2's business of
  parts: a part "matters" when it carries more than half of five-year operating profit, or else is the largest). Segment
  operating income, FY2021 to FY2025 (USD M, as filed; FY2022 and FY2025 10-Ks, Note 14 / segment note; FY2023 10-K):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year |
|---|---|---|---|---|---|---|
| Gexpro Services | 11.1 | 21.3 | 27.0 | 36.5 | 48.8 | **144.7** |
| Lawson (from 2022-04-01 as filed) | (12.0 pre-merger) | 6.5 (+12.1 Q1 pre-merger) | 32.5 | 14.6 | 18.8 | 72.4 as filed; 96.5 combined |
| TestEquity | 0.3 | 11.4 | -16.5 | 4.0 | 14.4 | 13.6 |
| Canada Branch Division (Bolt in "All Other" 2022) | (in Lawson) | 2.6 | 5.7 | 6.0 | 7.7 | 22.0 |

  Lawson's pre-merger figures are Lawson Products' own (FY2021 10-K, 0000703604-22-000019: operating income $11,987
  thousand; Q1 2022 10-Q, 0000703604-22-000027: $12,076 thousand, both including Bolt and before the purchase-accounting
  amortization the merger added). Gexpro Services carries **52.3%** of the parts' five-year operating profit on the
  combined basis (144.7 of 276.8) and 57.3% as filed (144.7 of 252.7): **Gexpro Services is the part that decides**, and
  narrowly. (On adjusted EBITDA, which the filer features and this run does not use, the 2025 parts are closer: Lawson
  51.6, TestEquity 51.0, Gexpro 63.7, Canada 15.6; FY2025 10-K, Item 7. The threshold is read on operating income, the
  convention's measure.)
- **Gexpro Services, the key variables.** A distributor and VMI provider of "high volume, low value Class C parts" to
  OEMs (FY2025 10-K, Item 1): hardware 45%, electrical 24%, fabrications 16%, mechanical 15%; renewable energy 33%,
  industrial power 18%, transportation 17%, aerospace and defense 13%; about 70% of revenue under long-term agreements;
  largest customer about 18%, top 20 about 83%. The variables are the OEMs' production schedules in six end markets, the
  renewal and pricing of a few large agreements, and the margin on a product line that does not change. "trying to
  identify the key variables [...] and evaluating how predictable they were first" **[M1998-044]**: the product and the
  service are plain and slow-changing; the customers' choices are the uncertain part, and that is the castle question
  (Q2), not a failure to understand what the business does or how it earns.
- **The other parts, briefly.** Lawson: MRO C-parts through about 920 field representatives under a VMI model; TestEquity:
  electronic production supplies (60%) and test and measurement (26%) distribution, rentals; Canada: branch MRO. None
  "must deal with fast-moving technology" **[L1993-023]** in the sense that puts the ten-year economics out of reach;
  TestEquity's test equipment line is the nearest, and it is not a deciding part.
- **Do the past statements tell me the future ones**, "the financial statements will tell me the information that’s
  useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**? For the combined company only partly: the history
  is four years of a reverse acquisition and six acquisitions (Note 3), so the statements are a moving perimeter; for
  Gexpro Services the segment record runs from its 2020 carve-out from Rexel (DEFM14A 2022, "Overview"), six years.
  That short record is carried to Q2 as the castle's problem; it does not make the economics unreadable.
- **VERDICT: IN.** The deciding part's economics (a C-parts distributor's gross margin, operating costs, working capital
  and customer contracts) can be understood, and "where the business will be in 10 years" can be pictured in
  kind **[M2000-037]**; whether its position will hold is put to Q2, which the rows place after this filter: "if it passes through that, it’s whether a company can have a
  sustainable edge" **[M1997-148]**.
  The doubt rule, "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**, was applied to the parts: the doubt found is about durability, which is Q2's, not
  about what the business is.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A moat "protects excellent
returns on invested capital" **[L2007-004]**. The parts are read separately, since "lumping them together [...] impedes
analysis" **[L2008-005]**, and the file closes on the deciding part.

**The parts table** (five-year segment operating income, combined basis, from Q1):

| part | share of five-year operating profit | castle, in one line | decides |
|---|---|---|---|
| Gexpro Services | 52.3% (57.3% as filed) | VMI and kitting programmes under long-term agreements with OEMs; margins rising 4.0% to 9.8% (2020 to 2025) while the top 20 customers rose to 83% of revenue | **yes** (more than half) |
| Lawson | 34.9% | field-representative VMI model; operating margin 2.0% to 6.9% since the merger, 3.9% in 2025, against Fastenal's 20% in every year | no |
| TestEquity | 4.9% | multi-brand electronics supplies and test-equipment distribution; operating margin -2.6% to 2.9% | no |
| Canada Branch Division | 7.9% | branch MRO in Canada, mostly bought (Source Atlantic, 2024; Eastern Valve, 2026) | no |

Parts that do not decide and look open (Lawson and TestEquity on these margins) would be carried to Q7 at no growth; the
file is not closed on them.

**The tests, applied to Gexpro Services, each with its filing fact.**
1. *Key factors*, "What are the key factors? And how permanent are they?" **[M1995-038]**: VMI bins installed at customers (155,000 in 2025, from over 75,000 in
   2020, partly by acquisition; FY2025 10-K Item 1; DEFM14A 2022); long-term agreements covering 74% of revenue (2020),
   65% (2022), 67% (2023), 64% (2024), 70% (2025) (the 10-Ks, Item 1). Their terms and lengths are not filed.
2. *Would it stand without the lord?* No superstar is named; the segment has had one chief executive since 2019, and
   LKCM Headwater Operations staff have provided "interim executive management" to the company (Note 16). No finding.
3. *The money test*, "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I
   do it?" **[M2011-015]**: the 10-K says Gexpro's competitors "include large global distributors as well as
   national, regional and local distributors" in "a large, fragmented market with many competitors" (Item 1). The
   business itself was sold by a large distributor, Rexel, in a 2020 carve-out to the controller (DEFM14A 2022,
   "Overview"). Whether a funded rival could take the twenty customers that are 83% of revenue cannot be read from any
   filing; "one competitor is frequently enough to ruin a business" **[M2012-108]**, and here one customer is 18%.
4. *Pricing power*, "the agony they go through in determining whether a price increase can be sustained"
   **[M2005-020]**: in 2020 its agreements "generally allowed these costs to
   be recovered in substantial part through price increases" (DEFM14A 2022); gross margin 29.5% (2020 successor period),
   32.1% (nine months 2021), 31.4% (2024), 31.2% (2025), the 2025 dip from "tariff costs not recovered through price
   increases to customers" (FY2025 10-K, Item 7). Price behaviour held through the cost inflation of 2021 to 2025; it has
   not been seen through a fall in the segment's own volume since 2020.
5. *Unit volume*: segment revenue about 250 (2020, predecessor plus successor), 256, 385, 406, 441, 497 (2021 to 2025,
   USD M; the 2022 step includes acquisitions), average daily sales +13.1% in 2025, led by renewable energy (+$25.3M).
6. *The low-cost position*, "if your costs are on parity or less [...] than your other major competitors, that is
   much more important to you than the absolute level" **[M2001-013]**: not shown. Gexpro's operating margin (after amortization) was 4.0% in its
   2020 downturn and 9.8% at its best year, against Fastenal's 19.8% to 21.4% in every year of the span (competitor row,
   below). No filing shows Gexpro's costs at parity with the low-cost operator.
7. *Brand*: not a factor in an OEM C-parts programme; no finding.
8. *The low bid*, "it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**: no filing says how the agreements are won or
   renewed. The customer base has narrowed: largest customer 23%, 19%, 21%, 23%, 18% and top 20 customers 63%, 63%, 75%,
   82%, 83% (2020, 2022 to 2025; DEFM14A 2022 and the 10-Ks, Item 1). The margin gains of 2023 to 2025 came in the same
   years as the concentration rose.
9. *Ask the competitors*: not on the public record; the 10-K names none of Gexpro's rivals.
10. *Widening or narrowing*, "how wide the moat is and whether it’s likely to widen further or shrink on you"
    **[M1999-108]**: the margin has widened five years running (4.0%, 4.3%, 5.5%, 6.7%, 8.3%,
    9.8%); the customer base has narrowed; renewable energy rose from 23% to 33% of revenue (2020 to 2025). Both
    directions are on the record.
11. *What could* "destroy, or modify, or reduce the economic strengths" **[M2000-014]**: the loss or re-pricing of one or two of the largest
    agreements, or a turn in renewable-energy and power-generation build (together about half of segment revenue in 2025:
    33% plus 18%).

**The competitor row** (same metric, operating income over revenue, from the rivals' own filings; XBRL companyfacts
transcription of the 10-Ks, `peers.py` in the research folder; the rivals are the 10-K's own named peer group, Item 5,
"W.W. Grainger, Inc., Fastenal Company, MSC Industrial Direct Co., Inc., Applied Industrial Technologies, Inc., DXP
Enterprises, Inc. and Global Industrial Company"; the three nearest in kind taken; MSC's fiscal year ends in August):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Fastenal (FAST) | 20.1% | 20.1% | 20.1% | 19.8% | 20.2% | 20.3% | 20.8% | 20.8% | 20.0% | 20.2% |
| MSC Industrial (MSM) | 13.1% | 13.1% | 13.1% | 11.9% | 11.0% | 9.3% | 12.7% | 12.1% | 10.2% | 8.0% |
| W.W. Grainger (GWW) | 11.0% | 9.9% | 10.3% | 11.0% | 8.6% | 11.9% | 14.5% | 15.6% | 15.4% | 13.9% |
| DSG consolidated (as filed) | | | | | | 2.2% | 3.6% | 2.7% | 3.1% | 4.0% |
| Gexpro Services segment | | | | | 4.0% | 4.3% | 5.5% | 6.7% | 8.3% | 9.8% |
| Lawson (pre-merger, then segment) | | | | | 5.8% | 2.9% | 2.0% (9 mo) | 6.9% | 3.1% | 3.9% |
| TestEquity segment | | | | | | 0.1% | 2.9% | -2.6% | 0.5% | 1.8% |

Accessions: FAST 10-Ks 0000815556-19-000015 to 0000815556-26-000009; MSM 0001003078-18-000281 to 0001003078-25-000123;
GWW 0000277135-19-000010 to 0000277135-26-000011 (the accession of the latest 10-K carrying each year is printed by
`peers.py`). Named rivals that do not file: none; the 10-K names no rival as a competitor at all, and the OEM
supply-chain providers Gexpro actually meets are not named in any filing read (no instance found in the FY2025 10-K by a
search for "competitor"). Gexpro Services' own pre-tax return on segment assets (operating income over total segment
assets, Note 14 and the FY2024 10-K): 8.2% (2023), 11.0% (2024), 13.9% (2025).

**The field's returns over the last full cycle, judged in words.** The field's durable players earn excellent returns
through the cycle: Fastenal's margin never left 19.8% to 21.4% from 2015 to 2025, Grainger's never fell below 8.6%
(2020) and MSC's below 8.0%; so this is not a field whose durable players earn only ordinary returns, and the "standing
castle that protects only ordinary returns" clause does not close it OUT. The deciding part, however, is not shown to be
one of those durable players: in the only fall in its own volume on its record (2020) it earned a 4.0% margin, a fifth of
Fastenal's in the same year and below MSC's and Grainger's; its improvement since has come every year with its own
volume rising.

**Change for the better, and why the box is TOO HARD (NATURE).** "the railroads were a terrible business for decades
and decades and decades and then they got good" **[M2017-026]**: Gexpro's five-year widening is that kind of change. The framework credits it only on a full cycle; the rows behind that rule are "you learn a lot about the durability of the
economics of a business" **[M2005-020]** and "a cyclical problem, not a secular one"
**[L1995-022]**. The
manufacturing field was soft in 2023 to 2025 by the filer's own indicator (average monthly PMI 47.1, 48.3, 48.9; FY2025
10-K, Item 7) and Gexpro's margin rose through it, which is evidence for the castle; but its own volume rose in every one
of those years on renewable energy and aerospace, so its price behaviour has not met a fall in its own business, and the
same years carried the rise in customer concentration to 83%. Whether the 9.8% margin holds when one of the twenty large
customers cuts schedules or re-bids is a forecast only that downturn answers: "We couldn't solve this problem, moreover,
even if we were to spend years intensely studying those industries." **[L1993-023]**. The moat is not shown open on the
evidence (OUT needs a castle shown open, the case of "If the answer had been yes, we wouldn’t have done it."
**[M2011-015]**); it is a moat whose future cannot be judged: "We don’t know
how to valuate that, and therefore we leave it alone." **[M2000-019]**.

- **VERDICT: TOO HARD (NATURE)**, the "too hard" pile **[M2006-013]**, decided by Gexpro Services. **Re-look condition
  (dated, from the filings):** the first fiscal year after FY2025 in which Gexpro Services' segment revenue falls; the
  question is then put again on that year's segment margin and customer concentration. If the going-private merger closes
  (outside date 2026-12-31), the company stops filing and the condition cannot be read.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4. Facts found
are under AFTER THE STOP.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged; the box line carries the flag.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found (including the buyback prices against the computed range) are under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? COMPUTATION, NOT A CLEARANCE
The file closed at Q2; everything in this section is arithmetic for the operator's two reporting figures and carries no
verdict or entry language (operator rule 3). Script and output: `q7_computation.py`, `q7_output.txt` in the research
folder. USD millions unless a share figure.

**Owner cash after every real cost, by year** (operating cash flow, which is after the company's own cash taxes and after
working capital; less stock pay; less property and rental-fleet spending net of disposals; acquisitions shown apart).
Combined companies, by the merger rule of Q7's specifics (a merger inside the window, the 2022 combination, valued on
the combined companies' own figures): FY2021 and FY2022 add Lawson Products' own filed figures (FY2021 10-K; Q1 2022
10-Q) to the reported TestEquity and Gexpro Services figures (FY2022 10-K); FY2023 to FY2025 as reported (FY2025 and
FY2024 10-Ks).

| | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| net capital spending (PP&E + rental fleet - disposals) | 15.6 | 13.4 | 18.7 | 14.4 | 26.8 | |
| owner cash, equity-only (after interest), before acquisitions | -4.7 | -27.1 | 75.2 | 36.8 | 50.4 | **26.1** |
| owner cash, all-equity (interest added back after tax), before acquisitions | 7.6 | -10.4 | 105.7 | 78.7 | 91.4 | **54.6** |
| acquisitions (cash, incl. seller-note, earnout and asset purchases) | 66.9 | 125.1 | 260.8 | 215.3 | 2.2 | 134.1 |
| owner cash, all-equity, after acquisitions | -59.4 | -135.5 | -155.1 | -136.6 | 89.2 | **-79.5** |
| owner cash, equity-only, after acquisitions | -71.6 | -152.2 | -185.6 | -178.5 | 48.2 | -107.9 |

The literal window (2021 and 2022 as reported, without Lawson) is shown beside: all-equity before acquisitions 14.4,
-8.2, 105.7, 78.7, 91.4, average 56.4; after acquisitions average -71.1. Stock pay is the filed expense (7.9, 5.2, 6.7 in
2023 to 2025, plus 0.4 of employee-share-purchase expense in 2023). Two CONVENTIONS of this run: **(1)** interest is added
back after a 25% shield (21% federal plus state, the rate reconciliation's state line, Note 13); rationale: a dollar of
deductible interest saves about that rate, and the section 163(j) limit (a $21.3M carryforward under a valuation
allowance, Note 13) only defers part of it, so the full add-back would overstate the after-tax cash; **(2)** Lawson's Q1
2022 stock pay was a benefit of $8.6M (liability awards re-measured, Q1 2022 10-Q) and is not credited; rationale: a
re-measurement gain on a liability is not cash the business produced. The Hisco retention bonuses ($34.6M in 2024, inside
operating cash) are part of a purchase price; they are left in operating cash in the table, and the figure with them added
back is shown in the output as a sensitivity.

**The range, by Q7's range convention, specific by specific.**
- *Aggregate growth*: measured on aggregate owner cash, not per share. The series changes sign inside the window on every
  basis (negative in 2021 and 2022, positive after; after acquisitions negative in four of five years). By specific (b)
  the growth is then measured between the halves of the window; the first half is negative, so the rate is meaningless,
  and **the range is the no-growth case alone, said so**.
- *All spending deducted*: property, software and rental fleet, net of disposals. Depreciation variant beside: depreciation
  proper in 2025 was 34.4 (PP&E 18.6, software 4.2, rental 11.6; Note 5) against net spending of 26.8; the filer guides
  "$25 million to $30 million for net capital expenditures during 2026 to support ongoing operations" (Item 7), which is
  the maintenance guess, so the maintenance-only case of specific (e) and the all-spending case are the same here.
- *Zero growth after year ten*, nominal.
- *A price above the top closes OUT* (were Q7 reached).
- (a) *Cycles*: neither end year is described by the filer as aberrational (FY2022 10-K MD&A describes 2021's operating
  cash as "decreased accounts receivable and increased accrued expenses partially offset by increased inventories"; 2025
  as "net income including non-cash items, partially offset by investments in trade working capital"). The literal window
  stands; a sensitivity on the three post-integration years (2023 to 2025) is shown beside it and is not a convention case.
- (b) *Decline and sign changes*: applied, above.
- (c) *Acquisitions*: the default pair deducts them with total growth credited; the organic pair beside leaves them out and
  credits only organic growth as the filer reports it (2024 organic revenue "decline in organic revenue of $34.5 million",
  FY2024 10-K; 2025 "an increase in organic revenue of $54.4 million", FY2025 10-K; compound 0.38% a year; FY2023 organic
  growth not reported). After year ten the purchases stop: the default case's tail is owner cash before purchases at no
  growth. The Eastern Valve purchase (March 2026, $16.5M, 10-Q) closed after the window: its financing is in the net debt
  at 2026-06-30, and it is credited at nothing (no earnings filed). The going-private merger is not a purchase by the
  company; if it closes, the $800 million of 10.000% notes (8-K 0001193125-26-417257) move onto the company and the public
  shares are cancelled for $35.00; it is not in the central figure.
- (d) *Working capital*: inside operating cash, counted; no single-event year named by the filer.
- (e) *Growth spending*: see all spending, above.
- (f) *The cap*: no growth is carried, so the cap does not bind.
- *Whose tax*: the company's own cash taxes, inside operating cash. Federal NOLs of $21.4M do not expire; state NOLs of
  $85.2M expire 2026 to 2037 (Note 13); their tax value at a state rate of a few percent is a few million dollars,
  immaterial to the range, and not priced separately.
- *On what the floor is earned*: all-equity central, owner cash before interest against market value plus net debt; net
  debt at 2026-06-30 = borrowings 733.8 + finance leases 1.4 - cash 66.9 = **668.2** (10-Q; operating leases of 114.6 left
  out; restricted cash of 8.5 left out as collateral and escrow). Equity-only beside.
- *The rate*: 5.60%, the 30-year Treasury, 2026-10-09.

**Results** (a share figure is the whole-business value less net debt, over 46,255,422 shares):

| case | at 5.60% | at 10% (fair-price leg) | expected return at $35.03 |
|---|---|---|---|
| default pair, all-equity, combined: acquisitions deducted, no-growth alone, purchases stop after year 10 | **-$15.12** | -$20.46 | 1.5% |
| default pair, all-equity, literal window | -$13.35 | -$19.19 | 1.6% |
| default pair, equity-only | -$11.65 | -$12.16 | 0.9% |
| organic pair, all-equity, no growth | $6.62 | -$2.65 | 2.4% |
| organic pair, all-equity, organic growth 0.38% | $7.26 | -$2.34 | 2.5% |
| organic pair, equity-only, no growth / 0.38% | $10.09 / $10.39 | $5.65 / $5.80 | 1.6% / 1.7% |
| sensitivity only: all-equity, 2023 to 2025 average of 91.9, no growth | $21.04 | $5.42 | 4.0% |
| sensitivity only: the same with the Hisco retention bonuses added back | $25.49 | $7.92 | 4.5% |

- **Value range (reporting figure, COMPUTATION):** central, the default pair on the all-equity basis: **the no-growth case
  alone, -$15.12 a share** (literal window beside: -$13.35); the organic pair beside: **$6.62 to $7.26 a share**
  all-equity, $10.09 to $10.39 equity-only; against **$35.03**.
- **Fair price (reporting figure, COMPUTATION; Part VII):** the default pair's is **not positive** (-$20.46 all-equity);
  by the rule for that case the alert figure is the organic pair, labelled so: **-$2.49 a share all-equity, also not
  positive; $5.72 a share equity-only** (the average of its two ends valued at 10%). The all-equity figure is the central
  one; the equity-only figure is shown beside and never decides alone.
- What the arithmetic says, without a verdict: no case, including the two generous sensitivities, has an expected return
  at $35.03 near the speakers' line, "we don’t want to buy equities where our real expectancy is below 10 percent"
**[M2003-149]**; the highest is 4.5%.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing: the file is in the "too hard" pile.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. No business the rows name (casinos, tobacco, loading schemes) is involved; recorded as a fact only.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q2** on the castle of Gexpro Services, the part with more than half of five-year
segment operating profit: a margin rise from 4.0% to 9.8% not yet tested by a fall in its own volume, earned while its top
20 customers rose to 83% of revenue. Re-look: the first fiscal year after FY2025 in which Gexpro Services' segment revenue
falls (unreadable if the going-private merger closes). **Integrity facts recorded, not judged** (AFTER THE STOP, Q5).
COMPUTATION beside it, not a verdict: value range -$15.12 a share (default pair, no-growth alone), organic pair $6.62 to
$7.26, against $35.03.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(The file closed at Q2. Facts already found that bear on later questions, each with its source, written down "in the first 30 minutes" **[M1997-127]**; no
verdict; the box unchanged, operator rule 2.)*

**Q3 (capital).** Five-year acquisition cash on the combined basis 670.3 (2021 to 2025), plus the 2022 all-stock
combination and the $100M rights offering of 2023 (FY2025 10-K, statement of equity). Operating income on the combined
basis rose from 23.4 (2021: 11.4 reported plus Lawson's 12.0) to 78.3 (2025), +54.9, about 8% pre-tax on the acquisition
cash alone, before the stock issued. Operating income over equity plus net debt at 2025-12-31: 78.3 over about 1,293,
about 6% pre-tax; operating income before amortization of purchased intangibles (78.3 + 46.5) over tangible capital (net
debt 644 plus tangible equity -45), about 21% pre-tax. Net capital spending 26.8 against depreciation proper 34.4 (2025).
"whether that’s good or bad depends on what we earn on that incremental $130 million over time" **[M2001-019]** is the
test these facts await.

**Q4 (the accounts).** The filer features "Adjusted EBITDA" in its MD&A and segment reconciliation (FY2025 10-K, Item 7;
"The one figure we regard as utter nonsense is the so-called EBITDA" **[M1998-086]**), and its annual incentive plan pays
on adjusted EBITDA (DEF 14A 2026). The adjustments recur: severance and acquisition-related retention 23.2 (2024) and 5.5
(2025), acquisition costs 10.1 and 0.2, "other non-recurring" 3.4 and 3.8 (Item 7). A material weakness at TestEquity as
of 2022-12-31 (FY2022 10-K, Item 9A); controls effective at 2025-12-31 with an unqualified auditor's opinion (Grant
Thornton, auditor since 2023; FY2025 10-K, Items 8 and 9A). Effective tax rate 57.0% in 2025 on interest-deduction limits
(Note 13). Receivables up $60.3M and first-half operating cash $1.6M in 2026 (10-Q); allowance for credit losses 2.4,
6.5, 8.0 (2024, 2025, 2026-06-30). No earnings guidance found in the filings read.

**Q5 (integrity facts, recorded, not judged).** (1) J. Bryan King is chairman, president and chief executive and the
managing partner of LKCM Headwater, whose group owns about 79% (8-K 2026-07-16); the company pays him nothing (DEF 14A
2026, Summary Compensation Table). (2) LKCM Headwater Operations staff were paid $1.1M, $1.2M and $0.6M (2025, 2024, 2023)
for consulting including "interim executive management"; the company uses LKCM-leased headquarters space rent-free (Note
16). (3) The 2022 combination merged two companies owned by LKCM affiliates into Lawson for stock, after which LKCM owned
about 75%; earnout shares (3.4 million) were issued in 2023; LKCM bought about 3.6 million of the 4.44 million shares of
the 2023 rights offering at $22.50 (PREM14A Background; Note 16). (4) The controller proposed to buy the minority at $29.50
on 2026-03-14, the stock having closed at $19.31 the day before and at $29.90 on 2026-02-27; the special committee asked
$39.50, then $36.50, $35.50 and a "best and final" $35.00; the controller's adviser conveyed that "LKCM was considering
engaging with the Company's stockholders directly" (PREM14A, Background). The deal requires a majority of the votes cast
by disinterested stockholders (8-K 2026-07-16). (5) The projections the committee's adviser used were based on lender
forecasts "LKCM was involved with the preparation of" (PREM14A, Background). (6) Discretionary cash bonuses were paid to
the CFO ($60,000) and the Lawson chief executive ($50,000) for 2025 in a year in which their formula awards paid $27,587
and $96,313 against targets of $420,000 and $600,000 (DEF 14A 2026). (7) "Senior executives leading the other operating
companies prior to the merger date are entitled to equity-based incentives that are separate and apart from the equity
awards described herein and these incentives will not be borne by the Company" (DEF 14A 2026): pay from outside the
company for operating-company heads. Any later run that reaches Q5 must answer these: "If you’ve got doubts, forget
it." **[M2013-088]**.

**Q6 (the money and the owners).** Retention: the combined company's retained earnings were negative at every year-end
(-25.7 at 2023-01-01 to -24.8 at 2026-06-30), so earnings kept since 2023 sum to about $1M; equity grew by
issuance. Buybacks: 138,725 shares at $26.09 (2023),
85,644 at $30.13 (2024), 776,924 at $30.26 (2025), $23.5M in 2025, under a programme that "does not have an expiration
date" and names no price (FY2025 10-K, Item 5 and Note 11); **the Q6 line Q7 owes:** the prices paid ($26.09 to $30.26)
sit above the whole computed range ($6.62 to $7.26 at most, organic pair; the central figure negative), so by Q6's convention the programme would weigh against, value being "entirely purchase-price dependent"
**[L2016-002]**; recorded here and not weighed. The restricted-payments
limit was raised from $10M to $25M a year in 2025 (8-K 0001193125-25-070858). Issuance and deals: the 2022 all-stock
combination is the kind of deal Q6's STOP reads, where "it's impossible for that buyer to make a sensible deal in an all-stock
deal" **[L2009-019]**, and whether Lawson's stock then sat below its value was
not examined. Pay: options granted at premium strikes ($27.50 to $70.00 tranches; DEF 14A 2026), annual plans on adjusted
EBITDA, adjusted sales, working capital and "Equity Value"; a "controlled company" that may use the Nasdaq exemptions
(FY2025 10-K, Item 1A). No dividends 2023 to 2025.

**Q7.** Above, as COMPUTATION.

**Q8 (alternatives).** The 30-year Treasury yields 5.60%; the highest expected return at the price in any case computed is
4.5% (a sensitivity). A buyer at $35.03 who holds to a closing receives $35.00.

**Q9 (debt and exposures).** Borrowings $733.8M at 2026-06-30, 100% floating at 2025-12-31, with a $7.0M annual interest
change per 100 basis points (Item 7A); term loan amortizing $35M a year and $563.9M due December 2030; financial covenants
on interest coverage and net leverage (Note 9). Pre-tax earnings over interest in 2025: 19.4 / 55.4 = 0.35x by the letter's "pre-tax earnings/interest, not EBITDA/interest" **[L2012-002]** (earnings before interest and tax over interest 1.35x). Purchase commitments of about
$240M over twelve months (Item 7). Gexpro's largest customer about 18% of segment revenue. If the merger closes, the
company carries the $800M of 10.000% senior notes due 2032, used to pay the minority, repay part of the credit facility and
"finance future acquisitions" (8-Ks of 2026-10-05 and 2026-10-08), about $80M a year of coupon against 2025 operating
income of $78.3M; "debt piled on them by their private-equity buyers" **[L2008-007]** is the narrated case, recorded and
not weighed (the public holder would by then be cashed out).

**Q12.** No named business; facts only.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (44b0daad); written question by question; committed after Step 0, Q1, Q2
      and the close (write-early). The heavy reading of filings was done before Q1 was written; each section was written
      when its question closed.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's (not checked by
      this analyst); the fold is the dispatcher's. Only the two paths of this run were added and committed.
- [x] No other run file, holding review, `PORTFOLIO.md`, `Screens/RESUME STATE*`, the run queue or the prepped reading
      list was opened, listed or searched; what was seen by accident is declared under Contamination.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_run.py`, and every quoted fragment beside an id
      checked against that row; no E-ids. Every filing fact carries its document and accession.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; Q7 is headed COMPUTATION, NOT A CLEARANCE and
      carries no entry language.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury;
      the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor-date issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; its D&A (which includes intangible amortization) was replaced
      by the filed depreciation lines.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the commit message).
- Honest gaps: the peers' figures are XBRL transcriptions of their 10-Ks, not read from the filed statements (they are a
  comparison, not a clearance); Gexpro Services' customers and contract terms are not in any filing; the William Blair
  analyses and the management projections in the PREM14A were deliberately not used ("we’ve never looked at a projection" **[M1995-050]**); the 13D/A and the
  SC 13E-3 were not read beyond what the PREM14A states.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The re-look condition for a change for the better** says "the first fiscal year in which the business's volume or
its field's volume falls". Here the field was soft for three years by the filer's own indicator (PMI below 50, 2023 to
2025) and one named peer's sales fell, while the deciding part's own volume rose each year; read literally, the condition
may already have been met without the castle ever being tested by a fall in its own business. This run took the
business's own volume as the condition and says so; the text could say which governs when they diverge, and what the
"field" is for a part (OEM C-parts programmes) whose rivals no filing names. (2) **The business-of-parts threshold sits on
the line**: Gexpro is 52.3% on the combined basis and 57.3% as filed, and on operating income before the purchase-accounting
amortization the 2022 reverse acquisition loaded onto Lawson and TestEquity it would likely fall below half (the largest
part would then decide, probably still Gexpro, not computed). The convention names "operating profit" without saying
whether purchase amortization from a deal between commonly controlled parties counts. (3) **A signed cash take-private by
the controller** has no rule: the price is the deal price, not a market price, so the floor test and the reporting
figures compare value against a number the controller set; the foundations' "market closed for five years" test fails
for a reason that has nothing to do with the business. A line on how to run a name with a pending cash-out (run the
business, report the deal beside) would make such runs comparable. (4) **The merger rule for a reverse acquisition** ("a
merger inside the window is valued on the combined companies' own averages") does not say which side's history the filed
statements carry; here the legal acquirer is the accounting acquiree, and `tools/run.py`'s ten-year balance-sheet table
splices Lawson alone (to 2021) onto the combined company (from 2022) with no marker. (5) The tooling prints D&A that
includes purchased-intangible amortization and an "OE D&A" built on it, which for an acquirer makes the depreciation
variant meaningless; the run replaced it with the filed depreciation lines.
