# Company Run — PENN Entertainment, Inc. (NASDAQ: PENN) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template before any fetch, 2026-10-05; working folder `Test Runs/_research 2026-10-05 PENN/`.)*

**POSITION NOTE, declared before any verdict:** NOT CHECKED. This run is blind: the dispatch forbids opening
`PORTFOLIO.md`, any holding review and the session-state files, so whether the operator holds PENN is unknown to the analyst.

**CONTAMINATION DECLARED.** Seen before the run: the five most recent commit subjects in the session context (LCII, ANDE,
SLVM, LKQ, SCSC purchase runs, all closed OUT at Q2), and the git status listing of three other 2026-10-05 run files (ENR,
ROCK, YELP) by name only; none opened, none about PENN. No other PENN file in `Test Runs/` was opened (`ls` returned none).
The analyst's own background knowledge of PENN (the 2013 GLPI spin, the Barstool and theScore purchases) is declared and
every such fact below is re-sourced to a filing.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $15.10 (quote 2026-10-05 printed by `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: common 134,066,591 (10-Q for the period ended 2026-06-30, filed
  2026-08-06, accession `0000921738-26-000022`, cover as of 2026-07-29; `python Screens/cover_shares.py PENN`). A second
  class, the exchangeable shares issued in the theScore purchase, stood at 98,920 outstanding on 2026-06-30 (same 10-Q,
  balance sheet); immaterial, carried for completeness. Total 134.17M.
- **Market cap:** $15.10 x 134.17M = **$2,026M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-02 (`tools/run.py`, which reads the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-26, accession `0000921738-26-000008` (Items 1, 5, 7, 7A,
  8: balance sheet, operations, cash flows, notes 8, 10, 11, 15, 17); 10-Q Q2 2026, filed 2026-08-06, `0000921738-26-000022`;
  proxy DEF 14A filed 2026-04-27, `0001140361-26-016846`; 8-Ks `0000921738-25-000040` (ESPN termination, 2025-11-06),
  `0001104659-26-018332` (HG Vora cooperation agreement, 2026-02-23), `0001140361-26-000833` (an executive's separation,
  2026-01-09), `0001104659-26-028502` (6.75% notes, 2026-03-16), `0001104659-26-044358` and `0001104659-26-067476` (credit
  agreement amendments). History: the 10-Ks for FY2012 (`0001047469-13-001483`), FY2014 (`0001047469-15-001405`), FY2016
  (`0001558370-17-001016`), FY2018 (`0000921738-19-000011`), FY2020 (`0000921738-21-000009`), FY2021
  (`0000921738-22-000011`), FY2022 (`0000921738-23-000010`), FY2023 (`0000921738-24-000012`), FY2024
  (`0000921738-25-000008`). All saved as text in the working folder.
- **One figure cross-checked against the filed statement:** total PENN stockholders' equity at 2025-12-31, `tools/run.py`
  1,834 against the filed balance sheet $1,834.0M (10-K FY2025, `0000921738-26-000008`); also cash 687 against $686.6M and
  long-term debt 2,849 against $2,848.9M. They agree.
- `python tools/run.py PENN` arithmetic lines only (Part VII): its owner-earnings window stops at 2022 because capex and D&A
  are not tagged for later years under the elements it reads, and **its OCF is before the rent that the filings put in the
  financing section** (principal on finance leases and financing obligations). Its owner-earnings figures are therefore
  not used; owner cash after rent is rebuilt from the filed cash-flow statements at Q4 below. Its ten-year balance-sheet
  table is used, checked against the filed statements.

## STEP 0 (continued) — THE BALANCE SHEETS, TEN YEAR-ENDS, READ BEFORE THE INCOME ACCOUNT
Read because the dispatch asks for them in Step 0 when the file closes before Q4, and because the framework asks for
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. The table is
`tools/run.py`'s first-filed XBRL transcription for equity, goodwill, intangibles and debt, with the lease and
financing-obligation lines taken from the filed balance sheets (10-Ks FY2016, FY2018, FY2020 to FY2025; 10-Q Q2 2026).
USD millions, year-ends.

| Year-end | Equity (PENN) | Goodwill + intangibles | Debt (book) | Financing obligations | Operating lease liab. | Finance lease liab. | Debt + all lease-type liab. | Cash | Accumulated deficit |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | -543 | 1,425 | 1,416 | 3,514 | n/a (pre-ASC 842) | n/a | 4,930 | n/r | n/r |
| 2018 | 731 | 3,085 | 2,453 | 7,148 | n/a (pre-ASC 842) | n/a | 9,602 | 480 | -968 |
| 2019 | 1,853 | 3,297 | 2,419 | 4,143 | 4,575 | 226 | 11,363 | 437 | 162 |
| 2020 | 2,656 | 2,671 | 2,432 | 4,132 | 4,493 | 219 | 11,276 | 1,854 | -507 |
| 2021 | 4,098 | 4,695 | 2,841 | 4,097 | 4,454 | 317 | 11,709 | 1,864 | -86 |
| 2022 | 3,598 | 4,428 | 2,818 | 4,034 | 1,047 | 5,050 | 12,949 | 1,624 | 154 |
| 2023 | 3,202 | 4,313 | 2,798 | 2,427 | 4,246 | 2,103 | 11,574 | 1,072 | -336 |
| 2024 | 2,863 | 4,093 | 2,797 | 2,387 | 3,976 | 2,116 | 11,276 | 707 | -647 |
| 2025 | 1,834 | 3,191 | 2,904 | 2,344 | 3,978 | 2,063 | 11,289 | 687 | -1,490 |
| 2026-06-30 | n/r | n/r | 2,800 (principal, MD&A) | 2,321 | 3,904 | 2,063 | about 11,090 | 887 | n/r |

(n/r = not read for this run. The 2017 year-end was not read. The 2019 "retained earnings" of 162 is the first-filed XBRL
value printed by `tools/run.py`; the 2018 and 2025 figures were checked against the filed balance sheets.)

What the figures are saying, and what they are not:
- **The claim ahead of the owners has not shrunk in seven years.** Debt plus every lease-type liability has sat between
  $11.3B and $12.9B at every year-end since 2019; the accounting has moved the same rent between three lines (financing
  obligation, finance lease, operating lease) as the leases were amended in 2022 and 2023, which is why any single line
  jumps. Against a market value of about $2.0B the owners hold a thin slice on top of a long, escalating claim.
- **Equity rose only when shares were sold, and fell back.** $1,288.8M of common stock was sold in 2020 and theScore was
  paid for partly in 12.3 million shares in 2021 (10-Ks FY2020, FY2021), taking equity to $4.1B; by 2025 it was $1.8B,
  below 2019, after $1.1B of buybacks (2022 at $34.23, 2023 at about $27.55, 2025 at $17.64 average) and the losses and
  impairments of 2023 to 2025.
- **Tangible equity is negative**: goodwill and intangibles of $3,191M exceed equity of $1,834M at 2025-12-31. Of gross
  goodwill of $4,181.1M, $2,394.5M has been written off as accumulated impairment (XBRL, 10-K FY2025).
- **Cash fell** from $1,864M (2021) to $687M (2025) while debt rose, the revolver was drawn ($570.0M at year-end 2025),
  and buybacks and Interactive took the difference; it recovered to $887M by June 2026 after the term-loan and 6.75%-note
  refinancing (10-Q Q2 2026).
- **Receivables and inventories** do not carry the story: receivables $254.2M against revenue $6,961.0M (2025), much of it
  gaming tax reimbursable by online partners; a cash business, as the filer says.
- **What the balance sheet cannot say**: the value of the licences that are not on it at cost, and whether the operating
  lease liability (discounted only to 2033 or 2034, because the filer judges renewals not reasonably certain) understates a
  rent that the operator must in practice keep paying to keep its casinos.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own PENN "if the market closed for five years"
**[M1997-109]**, so this run reads the casinos, the leases and the online arm, not the chart. The chart is loud: the
10-K's own performance graph puts $100 of PENN at the end of 2020 at $17.08 at the end of 2025 against $196.16 for the
S&P 500 (10-K FY2025, Item 5, `0000921738-26-000008`); the market "just tells us prices" **[M2006-077]** and the fall is
neither a reason to buy nor a finding. Margin of safety: if the case needs "pencil and paper, it's too close to think
about" **[M1996-084]**. No macro view of regional consumer spending enters **[M2000-094]**. Who is paid to tell you: the
filer's headline measures are "Segment Adjusted EBITDAR" and "Consolidated Adjusted EBITDA", and the second deducts only
the rent on leases classed as operating, $631.7M of the $967.8M paid to the REIT landlords in 2025; the rest of the rent
sits below EBITDA, in interest and in the financing section of the cash-flow statement (10-K FY2025, Note 11). A reader who
takes the headline figure takes about a third of the rent out of the cost of the business. An activist (HG Vora) won board
seats in February 2026 (8-K `0001104659-26-018332`); the advice that reaches an investor comes from parties paid by one
answer more than another **[M2020-037]**, and neither the filer's adjusted measures nor any outside view is used here. The
analyst's habits: write contrary evidence down at once **[M1997-127]**, read to "possibly reject your original hypothesis"
**[M1998-144]**, and ask "What do I not know that I need to know?" **[M1999-129]**.

**Contrary evidence, written down as found** **[M1997-127]** (in the order found):
1. Rent is the largest cost after gaming taxes and payroll: $967.8M paid to GLPI and VICI in 2025, $950.4M in 2024, $937.8M
   in 2023; minimum rent of $986.3M a year, $970.0M of it under the triple-net leases, with escalators of up to 2% and
   percentage-rent resets (10-K FY2025, MD&A "Triple Net Leases", Note 11).
2. Net loss in each of 2023, 2024 and 2025 ($491.4M, $313.3M, $845.3M); accumulated deficit $1,490.1M at 2025-12-31. Net
   income summed over 2011 to 2025 is a loss of about $1.5B (XBRL first-filed values, checked against the 2023 to 2025
   statement of operations).
3. Interactive lost $402.5M, $499.5M and $267.5M of segment Adjusted EBITDA in 2023 to 2025, after losses of $35.4M and
   $74.9M in 2021 and 2022 (10-Ks FY2022 `0000921738-23-000010` and FY2025).
4. Barstool: 36% bought in 2020, the rest bought in February 2023 for $315.3M cash and 2,442,809 shares, the whole sold to
   its founder in August 2023 "in exchange for nominal cash consideration"; loss on disposal $923.2M (10-K FY2025, Item 1
   and statement of operations).
5. ESPN: "$150.0 million per year in cash" for an initial ten-year term plus warrants on "approximately 31.8 million shares",
   signed August 2023 (10-K FY2023, `0000921738-24-000012`); ended by agreement effective 2025-12-01 after $155.6M paid in
   2025, settled with $38.1M plus $5M (8-K `0000921738-25-000040`); Interactive goodwill impaired $825.0M in Q3 2025.
6. theScore bought "for a purchase price of approximately $ 2.1 billion" in October 2021 (10-K FY2021, `0000921738-22-000011`).
7. Gaming licences, the asset that is the castle wall, impaired again and again with the filer naming competition as the
   cause: Argosy Sioux City 2013, "a new gaming license being awarded for the development of a new casino in Sioux City,
   Iowa to another applicant" ($71.8M); Southern Plains and Midwest 2014, "continued challenging regional gaming
   conditions" ($315.1M, of which $155.3M in Q4); a property in 2018, "impacted by nearby competition"; PENN National
   Race Course 2022 and 2023, "expansion of gaming legislation in the market and increased supply, particularly from our recent openings";
   East Chicago 2023, "increased supply in the region"; 2024, "Increased competition in our South and Midwest
   segments" and "Increased supply" in the Northeast and South; retail 2025, $120.3M, "a former expansion of legislation in the
   market, increased supply, and economic challenges". Sources: 10-Ks FY2014 `0001047469-15-001405`, FY2016
   `0001558370-17-001016`, FY2018, FY2021, FY2022, FY2023, FY2024 `0000921738-25-000008`, FY2025. (Plainridge and
   Dayton, 2015, $40.0M, the filer puts down to "a reduction in the long term earnings forecast", without naming a
   competitor.) The 2016 10-K: "all of our reporting units with goodwill and
   other intangible assets are at risk to have impairment charges in future periods".
8. The filer's own sentence: "Most of our properties operate in mature, competitive markets." (10-K FY2025, MD&A).
9. The landlord's share of property earnings has not moved in ten years: lease payments $442.3M against Adjusted EBITDAR
   $837.1M in 2016 (52.8%), $537.4M against $1,043.2M in 2018 (51.5%) (10-K FY2018 `0000921738-19-000011`); REIT payments
   $967.8M against retail segment EBITDAR $1,868.8M in 2025 (51.8%) (10-K FY2025).
10. Pinnacle Master Lease escalator not earned for the lease year to 2025-04-30 (the 1.8:1 Adjusted Revenue to Rent test):
    "We did not incur an annual escalator" (10-K FY2025, Note 11).
11. Caesars, the other large regional tenant of the same two REITs, impaired $182M of regional assets in 2025 "primarily
    due to localized competition" (Caesars 10-K FY2025, `0001590895-26-000011`); Boyd recorded $128.4M of impairments in
    2025 (Boyd 10-K FY2025, `0001437749-26-004908`).
12. Against the case against: H1 2026 retail segment EBITDAR $988.6M against $946.6M a year earlier, Interactive -$20.4M
    against -$151.0M, "record revenues at nine of our retail properties" (10-Q Q2 2026, `0000921738-26-000022`).

## THE STANDING RULE
The buyer's conduct only: a purchase, if one were ever reached, would be bought with no borrowed money and sized so that a
total loss of it could not touch what the buyer has and needs: "never going to risk what we have and need for what we
don't have and don't need" **[M2012-081]**; leverage is "the one thing that ends — or can prevent you from playing out your
hand" **[M2004-065]**. Owning PENN shares outright does not by itself put the buyer at risk of ruin. PENN's own leverage,
debt plus lease liabilities of about $11 billion against a $2.0 billion market value, is the target's and belongs to Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The question: "a reasonable fix on about what the earning power and competitive position will look like in five or 10
years", which includes "where the company will stand within the industry" **[M2012-065]**; understanding is "a reasonable
probability of being able to asses where the business will be in 10 years" **[M2000-037]** ("asses" is the transcript's
spelling). PENN is two businesses, so it is read by its parts (the framework's holding-company CONVENTION at Q1: a part
that cannot be understood, and that matters, keeps the whole outside the circle).

**Part 1, the retail casinos** (2025 retail segment revenue $5,660.9M of $6,961.0M; all of the segment profit).
- *Key variables* (the "important and knowable" **[M2006-076]**): visits and spend per visit at 42 licensed regional
  properties in 19 states, slot machines about 86% of gaming revenue; state gaming tax rates; rent, which is contractual
  (fixed base, escalators of up to 2% tied to a 1.8:1 revenue-to-rent test, percentage rent reset every two or five years
  on 4% of the change in net revenue); new supply, licensed by state legislatures; substitutes the filer names (VGTs in
  bars and truck stops, sweepstakes, skill games, iCasino, "emerging prediction markets") (10-K FY2025, Items 1 and 7,
  Note 11).
- *Do the past statements tell me the future ones?* **[M2008-033]** For this part, broadly yes. The record is long and
  plain: retail segment revenue $5,255.8M in 2019 and $5,660.9M in 2025 with new builds and acquisitions in between;
  retail segment EBITDAR margin between 32% and 39% in every year but 2020; the same economic shape in every filing back
  to the 2013 spin. What the next ten years hold is, on the filer's own description, mature markets under steady
  competitive pressure, and the forces that would change that are named in the filing. That is "a reasonable fix"
  **[M2012-065]**; whether the fix is good news is Q2's question.
- *Would the insiders write it down?* **[M2000-105]** They have: GLPI and VICI hold leases on these properties running to
  2033, 2034 and, for the Pinnacle lease, a 32.5-year term as the filer accounts for it, at fixed base rents; the lenders
  extended the term loan to May 2033 (10-Q Q2 2026). That is the opposite of "That's too hard."

**Part 2, Interactive** (2025 revenue $1,302.6M, of which $588.3M is gaming tax reimbursed by third-party online
operators for market access, a pass-through; segment Adjusted EBITDA -$267.5M in 2025, -$20.4M in H1 2026).
- The industry's ten-year economics are not foreseeable by me: state-by-state legalisation of iCasino, tax increases,
  and prediction markets under federal oversight (DraftKings launched DraftKings Predictions on 2025-12-19 and FanDuel
  launched FanDuel Predicts in December 2025, per their FY2025 10-Ks, `0001883685-26-000013` and `0001635327-26-000005`).
- But the speakers' Q1 failure is not knowing "who the winners will be" **[M2012-067]**, and here the winners are on the
  public record. FanDuel: "approximately 41% share of the online sports betting market in the states where FanDuel
  sportsbook was live and an approximately 27% share of the iGaming market" (Flutter 10-K FY2025); FanDuel US revenue
  $6,767M and segment Adjusted EBITDA $922M in 2025. DraftKings: revenue $6,054.5M, Adjusted EBITDA $620.0M. PENN: online
  gaming revenue $564.1M, at a loss. PENN is a small, loss-making participant that has spent about $2.1B (theScore), about
  $0.5B (Barstool, sold for nominal consideration) and two years of a $150M-a-year contract (ESPN, ended) without reaching
  scale. That position can be named; what cannot be named is the size of the industry it trails in. The position is
  weighed at Q2 as a castle and at Q6 as a use of the owners' money.

**The doubt, written down** **[M2002-092]**: "if you have doubts about something being into your circle of competence, it
isn't." My doubt is real, but it is about the castle (how fast iCasino, prediction markets and new licences wear down the
regional properties), not about whether the economics can be read; the framework's routing gives that question to Q2.
The counter-reading, that the Interactive part alone keeps the whole outside the circle, is recorded; it would close the
file TOO HARD (NATURE) here. It is not taken, because the part's competitive position can be named from the competitors'
own filings and its losses in H1 2026 ran at about one-seventh of the year before.

**VERDICT: IN.** The retail economics can be given a reasonable fix ten years out **[M2012-065]**, **[M2000-037]**; the
Interactive part's position can be named against named winners **[M2012-067]**. Passes to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what's going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**Why it is still standing, in one line.** The regional casinos stand on state gaming licences: a state admits a fixed
number of casinos, and a local customer ("our in-person customers are predominately local, so we compete for more
day-to-day discretionary spending", 10-K FY2025, Item 1A) goes to the licensed casino nearest him. PENN does not own the
land and buildings of most of these castles; GLPI and VICI do, and are paid first. The question is how permanent the
licence wall is, and the filings answer it.

**The castle tests, each with its filing fact.**
1. *The castle questions: key factors and how permanent* **[M1995-038]**. The key factor is the number of licences, set by
   legislatures and not by PENN. Its permanence, on PENN's own record: in 2013 Iowa awarded "a new gaming license ... for
   the development of a new casino in Sioux City, Iowa to another applicant" and PENN wrote off $71.8M at Argosy Sioux City
   (10-K FY2014); PENN National Race Course was impaired in 2022 and 2023 for "expansion of gaming legislation in the market
   and increased supply", much of it supply PENN itself opened at York and Morgantown, its "two Category 4 development
   projects" (10-Ks FY2021, FY2022, FY2023); East Chicago in 2023 for "increased supply in the region"; $120.3M of retail licences and
   trademarks in 2025 for "a former expansion of legislation in the market, increased supply, and economic challenges"
   (10-K FY2025). The wall moves whenever a legislature moves it.
2. *Would it stand without the lord?* **[L2007-006]**, **[M1996-037]**. Yes, in the narrow sense: a licensed slot floor
   runs on ordinary management. This test does not help PENN, because the same is true of the competitor across the river.
3. *The money test* **[M2011-015]**. For a land casino the attacker needs a licence before money, which is the castle's one
   real strength. But the filer reports the attack happening in the ways money can still go: "We and our competitors have
   invested in expanding existing facilities, developing new facilities, and acquiring established facilities in existing
   markets", and VGTs in bars and truck stops, sweepstakes, skill games, historical horse racing, iCasino and prediction
   markets reach the same local customer without a casino licence (10-K FY2025, Item 1A). On the online side the test has
   been run, by PENN as the attacker, and lost: about $2.1B for theScore, about $0.5B for Barstool (sold for nominal
   consideration, $923.2M loss), $150M a year to ESPN for two years (ended, $825.0M goodwill impairment), and PENN's online
   gaming revenue in 2025 was $564.1M against FanDuel's $6,767M US revenue. "If the answer had been yes, we wouldn't have
   done it." **[M2011-015]**; "one competitor is frequently enough to ruin a business" **[M2012-108]**, and online there are
   two.
4. *Pricing power* **[M2005-020]**. No instance in the filings of a price PENN set and held: the "price" of a slot floor is
   its hold, which the filer describes as stable within a typical 5% to 11% range, and margin is managed through
   promotions and marketing (10-K FY2025, MD&A, Key Performance Indicators). The Pinnacle Master Lease escalator not being
   earned in 2025 says the properties under it did not meet that lease's 1.8:1 revenue-to-rent test.
5. *Unit volume and share of mind* **[M1999-054]**. Retail segment revenue $5,255.8M (2019) and $5,660.9M (2025), up 7.7%
   in six years with York, Morgantown, Perryville, the new Joliet and the M Resort tower added and Tropicana Las Vegas sold
   in between (10-Ks FY2021, FY2025): no organic volume growth is visible in the totals. The South segment fell from
   $1,322.2M to $1,167.1M (2021 to 2025) as "new supply continues to impact visitation" (10-K FY2025; 10-Q Q2 2026).
6. *The low-cost position* **[L2000-017]**, **[M1997-010]**. PENN is not the low-cost operator; it is the operator that pays
   the most rent. The landlords took 51.8% of PENN's 2025 retail segment EBITDAR ($967.8M of $1,868.8M) and about the same
   share in 2016 and 2018 (52.8%, 51.5%). Boyd, which owns most of its properties, paid master-lease rent of $113.8M in 2025
   against $1,278.7M of property EBITDAR, about 9% (Boyd 10-K FY2025). Caesars, the other large REIT tenant, carries $1.4B
   of 2026 rent against $3,517M of 2025 Las Vegas and Regional EBITDA, about 40% (Caesars 10-K FY2025). "The guy who could
   sell it cheaper than we could made it risky for us." **[M1997-010]**
7. *The brand in the customer's mind* **[M2008-075]**. PENN Play has "over 33 million members" (10-K FY2025, Item 1); the
   filer's own impairments of trademarks (Ameristar Council Bluffs, $15.0M, on a rebrand; $10.0M in South and West, 2025)
   show the names are not the draw. No instance found in the filings of a customer asking for PENN by name over the nearer
   casino.
8. *Would the customer still choose it over the low bid?* **[M2017-009]**. The regional customer chooses on convenience
   and on promotions; online the filer says competitors with scale may "adopt aggressive pricing or promotional policies"
   (10-K FY2025, Item 1A), and PENN's Interactive margin improved in 2025 chiefly by "a decrease in marketing expense"
   while online sports revenue fell in H1 2026 on "lower handle" (10-Q Q2 2026). The customer who leaves when the
   promotion stops is buying the low bid **[L2004-003]**.
9. *Ask the competitors* **[M1999-130]**. From their filings rather than their mouths: Caesars wrote down $182M of regional
   assets in 2025 for "localized competition"; Boyd recorded $128.4M of impairments in 2025; Flutter says it holds 41% of
   online sports betting and 27% of iGaming where it is live. The competitors' filings describe the same narrowing.
10. *Widening or narrowing?* **[M1999-108]**, **[L2005-010]**. Narrowing, on the filer's own valuations: licence
    or goodwill impairments in 2013, 2014, 2018, 2021, 2022, 2023, 2024 and 2025 with competition, new supply or new
    legislation named as the cause; the filer's 2016 10-K
    already said "all of our reporting units with goodwill and other intangible assets are at risk". The margin record is
    mixed and is stated fully in the competitor row below: against 2019 the retail margin is flat (32.2% to 33.0%); against
    the 2021 peak it is down 5.7 points, as it is at Caesars Regional and Boyd. The filer's description of what holding
    position takes: competition "may require us to undertake additional substantial capital expenditures to maintain and
    enhance the competitive positioning of our properties" (10-K FY2025, Item 1A). "A moat that must be continuously rebuilt
    will eventually be no moat at all." **[L2007-005]**
11. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. The filer names it: iCasino
    (which PENN itself promotes, "iCasino forward"), "growing competition from new forms of gaming such as prediction
    markets", VGTs, sweepstakes, skill games (10-K FY2025, Item 1A). The newspaper question **[L2006-008]**: if iCasino and
    prediction markets had come first, would a business of renting a building from a REIT at half its property earnings to
    sell slot play to local customers be started? No instance found in the filings of PENN starting one without a REIT
    paying for the building.

**The competitor row** (same metric from each filer's own 10-K: segment Adjusted EBITDAR or Adjusted EBITDA of the
regional casino segments, divided by that segment's revenue; rent is below this line for every company, so the row
compares the castles before the landlord; the rent burden is the last column).

| Company, segment (source, accession) | 2018 | 2019 | 2021 | 2022 | 2023 | 2024 | 2025 | Rent / property EBITDAR 2025 |
|---|---|---|---|---|---|---|---|---|
| PENN, four retail segments (10-Ks FY2018 `0000921738-19-000011`, FY2021, FY2022, FY2025) | 29.1% (consolidated, all segments) | 32.2% | 38.7% | 36.7% | 35.8% | 33.9% | 33.0% | 51.8% |
| PENN, South segment (same) | n/a | 33.0% | 44.4% | 41.7% | 40.6% | 37.1% | 34.4% | |
| Boyd, three land segments (FY2018 `0000906553-19-000009`, FY2021 `0001437749-22-004655`, FY2025 `0001437749-26-004908`) | 29.1% | n/a | 43.1% | n/a | n/a | 40.1% | 39.5% | 8.9% |
| Boyd, Midwest & South (same) | 28.7% | n/a | 39.8% | n/a | n/a | 37.1% | 36.7% | |
| Caesars, Regional (FY2022 `0001590895-23-000070`, FY2025 `0001590895-26-000011`) | n/a | n/a | 35.7% | 34.8% | 34.0% | 32.7% | 31.1% | about 40% (company-wide, 2026 rent) |
| Churchill Downs, Gaming (FY2025 `0000020212-26-000025`) | n/a | n/a | n/a | n/a | 50.1% | 48.5% | 46.0% | owns |
| Red Rock, Las Vegas operations (FY2025 `0001653653-26-000004`) | n/a | n/a | n/a | n/a | n/a | 45.7% | 46.2% | owns |

Online, same three years (revenue; segment Adjusted EBITDA): FanDuel US (Flutter 10-K FY2025) $4,391M / $232M, $5,729M /
$507M, $6,767M / $922M; DraftKings (10-K FY2025) $3,665.4M / -$151.0M, $4,767.7M / $181.3M, $6,054.5M / $620.0M; PENN
Interactive gaming revenue $81.1M, $390.2M, $564.1M, segment Adjusted EBITDA -$402.5M, -$499.5M, -$267.5M (2023, 2024,
2025). The two leaders crossed into profit as they scaled; PENN lost more as it spent.

*How to read the row.* The 2018 PENN figure is the consolidated margin of all segments under the segment structure of
that year, and segment boundaries and acquisitions differ across filers and years, so the long run is read for
direction, not decimals. Read that way: every regional row that
spans 2021 to 2025 is lower in 2025, the operators that own their buildings (Churchill, Red Rock, Boyd) run at 37% to 46%
before rent, PENN and Caesars run at 31% to 33% before rent, and PENN then hands about half of what is left to its
landlords (Caesars about 40%, Boyd about 9%). Against 2019 PENN's retail margin is flat; that is the strongest single fact for the castle and it is recorded.

**What the castle is, on the evidence.** It stands because legislatures have not yet licensed the next casino or legalised
the next substitute in most of PENN's markets; that is a reason that depends on others and has failed, on PENN's own
valuations, in Sioux City, Grantville, East Chicago, the South segment and the 2025 licence write-downs. The castle's own
walls (licence, real estate) belong in part to the state and in part to the landlord; the operator holds the slot floor
between them and must keep spending to "maintain and enhance the competitive positioning" of it. Online, PENN has no
castle; it attacked one and lost.

**VERDICT: OUT.** A castle shown on the evidence to be filling in closes OUT (the framework's Q2 routing): the filer's own
licence impairments, year after year, name new supply and new legislation as the cause **[M1999-108]**, **[L2005-010]**;
holding position requires capital the filer itself says is needed to maintain it, a moat "continuously rebuilt"
**[L2007-005]**; PENN is the
high-rent operator among its peers, not the low-cost one **[M1997-010]**, **[M2001-013]**; and the online money test was
run and failed **[M2011-015]**, **[M2012-108]**. The price does not reopen it: "What you can't do is turn any investment
into a good deal by paying little" **[M2019-015]**; "If you really think a business is declining, most of the time you
should avoid it." **[M2012-062]**. *Counter-reading recorded:* the retail margin is flat against 2019 and H1 2026 is up; a
reader who weights those above the impairment record would call the retail castle not shown filling in but impossible to
judge against iCasino, prediction markets and legislatures, which is TOO HARD (NATURE) **[M2000-019]**, **[M2000-014]**:
the insiders of the regional casino trade have not written down, in any filing read, where the licence wall will be in ten
years. Both readings close the file at Q2; neither is TOO HARD (WORK), so no research pass is opened.

The file closes here. Everything below Q2 is **NOT REACHED** as a clearance; the reporting the owner asked for follows
after THE BOX, headed **COMPUTATION — NOT A CLEARANCE** (operator rule 3).

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (file closed OUT at Q2). The capital arithmetic is in the computation section below, as computation only.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED** as a verdict. The balance sheets of eight to ten years were read, as the dispatch asks when a file closes
before Q4, and are set out under STEP 0 (continued) above. No confusion verdict is given.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** The capital-allocation record (buybacks at $17.64 average in 2025, the Interactive purchases) is set out
as fact in the computation section; no weighing is made.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** Value range, fair price and cheap price: see COMPUTATION — NOT A CLEARANCE below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** The debt and lease obligations are set out in the balance-sheet reading below, as fact only.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** What the framework would have the buyer do: nothing (the framework's Q10 text: inaction is the default).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED** (the run order asks Q12 after Q10). Recorded for the operator, not weighed: casinos are one of the
businesses the framework names, "the gambling casinos use clever psychological tricks to cause people to hurt themselves
[...] It's a dirty business" **[M2007-018]**. By the framework's text this is a STOP for buying and running the whole and a
WEIGHING for a marketable stake; for a share purchase it would have weighed against.

## THE BOX
**OUT at Q2** (the castle shown on the filings to be filling in: competition-driven impairments in eight of the
last thirteen years, the South segment's margin from 44.4% to 34.4%, continual capital "to maintain" position, the highest
rent burden among its peers, and an online attack that was paid for and lost). Counter-reading recorded: TOO HARD
(NATURE) on the retail castle's ten-year future against legislatures, iCasino and prediction markets. Not TOO HARD (WORK);
no research pass is opened. Price $15.10. The arithmetic below is reported at the owner's request and is not a clearance.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section is arithmetic made after a closing STOP (operator rule 3). It carries no entry language and
reopens nothing: "What you can't do is turn any investment into a good deal by paying little" **[M2019-015]**.*

**Owner cash after rent, rebuilt from the filed cash-flow statements** (USD millions). Rent is treated consistently: the
operating-lease rent ($632.4M cash in 2025) and the interest parts of the finance-lease and financing-obligation rent
($109.5M and $147.9M in 2025) are already inside operating cash flow; the principal parts, which the filings put in the
financing section, are deducted here. The sum of the pieces, about $987M in 2025, agrees with the $967.8M paid to the REIT
landlords plus the non-REIT operating leases (10-K FY2025, Note 11). Stock pay and the ESPN warrant expense (warrants
issued for services, a non-cash add-back in operating cash flow) are deducted as the framework's Q4 asks, earnings "after
interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**. Sources: 10-Ks FY2019 vintage
(2019), FY2021 (2021), FY2023 (2022), FY2025 (2023 to 2025); 10-Q Q2 2026.

| Year | OCF | - stock pay | - ESPN warrants | - finance-lease principal | - financing-obligation principal | = before capex | Capex (net of GLPI development sale-leaseback proceeds) | Owner cash, all capex | Maintenance capex | Owner cash, maintenance |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 703.9 | 14.9 | 0 | 6.2 | 51.6 | 631.2 | 190.6 | 440.6 | 165.5 | 465.7 |
| 2021 | 896.1 | 35.1 | 0 | 8.5 | 36.0 | 816.5 | 244.1 | 572.4 | 229.7 (imputed) | 586.8 |
| 2022 | 878.2 | 58.1 | 0 | 110.5 | 63.2 | 646.4 | 263.4 | 383.0 | 220.3 | 426.1 |
| 2023 | 455.9 | 85.9 | 12.5 | 47.1 | 39.2 | 271.2 | 360.0 | -88.8 | 229.7 (imputed) | 41.5 |
| 2024 | 359.3 | 52.9 | 67.9 | 50.3 | 40.8 | 147.4 | 482.7 | -335.3 | 229.4 | -82.0 |
| 2025 | 508.2 | 60.9 | 57.1 | 53.4 | 43.5 | 293.3 | 367.7 (647.7 less 280.0) | -74.4 | 239.3 | 54.0 |
| H1 2026 | 363.1 | 31.5 | 0 | 27.6 | 22.6 | 281.4 | -24.3 (192.0 less 216.3) | 305.7 | 69.1 | 212.3 |

Notes on the inputs. Maintenance capex is the filer's own split where it gives one (2022 derived as $263.4M less $17.1M of
York and Morgantown project spend and $26.0M of insurance-funded hurricane rebuild; 2024 $229.4M; 2025 $239.3M; 2019 the
maintenance line of the cash-flow statement as then filed, $165.5M). The filer gives no split for 2021 and 2023; those two
years carry the mean of the three known years, $229.7M (**CONVENTION of this run**: a disclosed guess, not a substitute
figure, because the input is unobtainable from the filings read). Netting the GLPI sale-leaseback proceeds against
development capex is also a **CONVENTION of this run**: the proceeds bought back the buildings in exchange for added rent
($10.1M for Joliet, $11.7M for the M Resort tower, $17.4M for Aurora), and that rent appears in later years' owner cash, so
counting the gross capex as well would charge the same buildings twice; the gross-capex basis is shown below for
comparison. Cash taxes were $4.7M paid in 2025 and a $3.8M net refund in 2024 ($73.9M paid in 2023), so for the latest two
years owner cash after PENN's taxes is in substance pre-tax. Twelve months to June 2026 (H2 2025 plus H1 2026): $463.0M
before capex; less the filer's 2026 maintenance guidance of about $220.0M, **$243.0M**. H1 2026 operating cash flow
includes favourable working-capital timing of deposits, which the filer names and does not size.

**Five-year average and per-share figures** (134.17M shares; $15.10; market value $2,026M):

| Basis | Annual owner cash | Yield at $15.10 | No-growth value at 5.63% (per share) | Value at a 10% yield (per share) |
|---|---|---|---|---|
| Five-year 2021-25, all capex net of sale-leaseback proceeds (the Q7 CONVENTION's input) | $91.4M | 4.5% | $12.10 | $6.81 |
| Five-year 2021-25, gross capex (no netting) | $35.4M | 1.7% | $4.68 | $2.64 |
| Five-year 2021-25, maintenance capex | $205.3M | 10.1% | $27.18 | $15.30 |
| Whole-cycle 2019 and 2021-25 (2020 excluded), maintenance capex | $248.7M | 12.3% | $32.92 | $18.54 |
| Run-rate, twelve months to June 2026, maintenance guidance | $243.0M | 12.0% | $32.17 | $18.11 |
| Depreciation variant, 2023-25 only (D&A less finance-lease right-of-use amortization, which is rent already deducted) | -$111.8M | negative | none | none |

The depreciation variant is shown for 2023 to 2025 only: before 2023 the buildings under the PENN Master Lease were still
on PENN's books and depreciated while their rent was also paid, so earlier D&A double-counts. Depreciation of $344M to
$356M a year against maintenance capex of $220M to $239M is a gap of about $115M a year that the filer's maintenance
figure does not explain; part is amortization of purchased intangibles (theScore technology among them), part may be
maintenance the filer books as "project" (the filer: competition "may require us to undertake additional substantial
capital expenditures to maintain ... the competitive positioning of our properties"). That gap is the single largest
uncertainty in the arithmetic.

**(a) VALUE RANGE per the Q7 CONVENTION** (five-year average of owner cash after every real cost, all capital spending
deducted; carried ten years at the growth shown on aggregate owner cash, then zero nominal growth; discounted at the
5.63% sovereign). The base is $91.4M. The growth shown cannot be computed as a rate: aggregate owner cash on this basis ran
$572.4M, $383.0M, -$88.8M, -$335.3M, -$74.4M and changes sign. The no-growth end is **$12.10 a share**; the shown-growth
end, carrying any part of the decline forward, is **below zero**. On the maintenance basis the ends are **$27.18** (no
growth) and **$0.45** (the 2021-to-2025 rate of -44.9% a year carried ten years, then flat). Either way the top is far
more than three times the bottom, so had Q7 been reached the CONVENTION would have closed it **TOO HARD**: "the range must
be so wide that no useful conclusion can be reached" **[L2000-025]**. On the CONVENTION's own all-capex input the price,
$15.10, is above the top of the range ($12.10).
*Whole-cycle variant*, because the five-year window holds three abnormal years (2021, the post-closure peak, retail margin
38.7%; 2023 and 2024, the ESPN launch, Interactive at -$402.5M and -$499.5M): adding 2019 and averaging the six normal-
and-abnormal years on the maintenance basis gives $248.7M, a no-growth value of **$32.92** at the sovereign. Range on
that variant, no-growth to the run-rate repeated: $32.17 to $32.92; it rests on the maintenance basis, which the
depreciation gap above calls into question.

**(b) FAIR PRICE**: the price at or below which the central case clears the ~10% pre-tax floor (the framework's Q7
CONVENTION, from the speakers' figure, "we quit on buying ... where our real expectancy is below 10 percent"
**[M2003-149]**). Central case (**CONVENTION of this run**): the five-year maintenance-basis owner cash, $205.3M, at no
growth, because a no-growth case should not be charged growth capital and the five years hold both the abnormal high and
the abnormal lows. Tax treatment: owner cash is after PENN's own cash taxes (small, $4.7M in 2025) and before the buyer's
taxes; it is compared with the pre-tax floor as it stands, which is the stricter reading if PENN's cash taxes rise.
**Fair price: about $15.30 a share** ($205.3M / 10% / 134.17M). On the CONVENTION's all-capex input it would be **$6.81**;
on the whole-cycle variant **$18.54**; on the run-rate **$18.11**. The price, $15.10, sits on the central fair price.
A price at the fair line is exactly the case the framework calls "too close to think about" **[M1996-084]**.

**(c) CHEAP PRICE**: below which no pencil is needed. Rule (**CONVENTION of this run**): the lower of (i) the price at
which the harshest basis the filings support, five-year owner cash with all capital spending, clears the 10% floor at no
growth, and (ii) half the central fair price. (i) $6.81; (ii) $7.65. **Cheap price: about $6.80 a share**, 55% below
$15.10. Rationale: at that price even the basis that charges every dollar of capex, and gives no credit for the new
buildings, clears the floor, so the conclusion would not depend on which capex basis is right; that is the condition
under which a case "should scream at you" **[M2009-005]**. The closing STOP at Q2 is not reopened by any price.

**Facts for Q6 and Q9, recorded and not weighed.** Buybacks: 17.56M shares at $34.23 (2022), about 5.44M at $27.55
(2023), 20.09M at $17.64 (2025), $1.1B in all, every average above today's price and above the central fair price
computed here; the programmes name no price ("There is no minimum number of shares ... and the repurchase program may be
suspended", 8-K `0000921738-25-000040`). Shares sold: $1,288.8M of common stock in 2020; 12.3M shares and 768,441
exchangeable shares for theScore in 2021; 2,442,809 shares for Barstool in 2023. Stock pay $14.9M (2019) to $60.9M (2025).
Leverage: debt plus lease-type liabilities about $11.1B at June 2026 against $887M of cash; the AR PENN and 2023 Master
Leases are "cross-defaulted, cross-collateralized, and coterminous, and subject to a parent guarantee", and the debt
agreements cross-default to the Master Leases (10-K FY2025, Note 11 and MD&A); no material debt maturity before 2027
after the 2026 refinancings (10-Q Q2 2026). The proxy (DEF 14A, `0001140361-26-016846`) was fetched; only its record-date
share count (133,705,284) was read, because Q5 and Q6 were not reached.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed after each: the dispatch
      forbids commits; the file was written section by section to disk instead.*
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession;
      no number without a filing or a CONVENTION label. Competitor figures carry the competitor's accession.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance, and the
      reporting is headed COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); rent deducted in full and
      consistently across the three lease classifications; the sovereign from the US Treasury curve, dated 2026-10-02;
      the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (twelve items under THE FOUNDATIONS).
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used, and its owner-earnings lines were rejected because they
      stop at 2022 and omit the rent in the financing section (Part VII).
- [ ] `python tools/check_framework.py` PASS before the commit: run, result recorded in the reply; no commit made (dispatch).
- Honest gaps: maintenance capex for 2021 and 2023 is imputed; PENN's same-store revenue cannot be separated from
  acquisitions and openings with the filings read; Charles Town's long history (the largest property before Maryland's
  casinos opened) was not read property by property, because PENN stopped reporting property revenue; the proxy was not
  read beyond the share count; competitor margins are segment measures each filer defines its own way.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Rent is not named anywhere in Q4 or Q7.** The framework's owner cash is "after every real cost", and
Q4 lists depreciation, stock pay, restructurings, catastrophe losses, pensions and taxes, but not rent, and not the case
where one lease is split by the accounting into operating rent (inside OCF), interest (inside OCF) and principal (in the
financing section). `tools/run.py` follows the cash-flow statement and so silently drops the principal half of the rent
($96.9M in 2025, $173.7M in 2022). This run deducted it as a real cost on the reasoning of Q4's GM-and-Ford pension row
("believe me, it's real" **[M2005-057]**); the framework should say so in Q4. (2) **The Q7 CONVENTION has no rule when
the five-year owner cash changes sign.** "Carried forward at the growth the business has actually shown" cannot be
computed for $572M falling to -$74M; this run reported the no-growth end and stated that the shown-growth end is below
zero. A sentence is needed: when the series changes sign, the shown-growth end is taken as zero (or the file closes TOO
HARD at Q7). (3) **"All capital spending" meets the sale-leaseback.** When the landlord buys the new building back for
cash and raises the rent, deducting gross capex charges the building twice; this run netted the proceeds and confessed it,
but the CONVENTION is silent. (4) **Q1's holding-company CONVENTION and Q2's routing overlap for a company with a core
business and a loss-making venture.** The doubt rule **[M2002-092]** at Q1 could close the file on the venture alone,
while the venture's fate is really a Q2 castle question and a Q6 capital question; two analysts could close PENN at Q1
TOO HARD (NATURE) or at Q2 OUT on the same facts. The framework should say whether a part that "matters" is judged by its
share of profit, its share of capital spent, or its share of the ten-year forecast.
