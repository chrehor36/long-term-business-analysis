# Company Run: Primoris Services Corporation (NYSE: PRIM), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch.

**POSITION NOTE, declared before any verdict:** NOT CHECKED. The blind rule of this run bars `PORTFOLIO.md`, every holding
review, the session-state file, the register and the prepped reading list. The analyst does not know whether the operator
holds or wants this name and made no attempt to learn it.

**CONTAMINATION, declared.** (1) The session context showed the subjects of the five most recent commits, which name v5 runs
of EME, FIX and IESC (each closed OUT at Q2), PWR (TOO HARD (WORK) at Q2) and UTI (TOO HARD (NATURE) at Q1). PWR is one of
the four competitors this run was told to read; its figures below were fetched fresh from Quanta's own filings, and its
verdict line was not used. No run file of any of those names was opened. (2) The git status in the context lists research
folders of other names (AYI, BDC, CHD, ARCB); none was opened. (3) Nothing seen bears on PRIM, its holding status, or any
earlier PRIM run; a search of the `Test Runs/` file list for "PRIM" returned only this file.

**Working folder:** `Test Runs/_research 2026-10-05 PRIM/` (filing texts, `fetch.py`, `series.py`, `peers.py`, `peers2.py`,
`value.py` and their outputs).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $79.08 (close 2026-10-02; Yahoo chart endpoint through `tools/sources.py`; AGGREGATOR, live quote only, flagged
  per operator rule 5). `tools/run.py` printed $78.94 intraday on 2026-10-05 and a later read printed $79.26; the case does
  not turn on the difference. For scale: the company bought its own shares in May 2026 at $111.29 (10-Q below).
- **Shares by class** from the latest filing's cover: 53,832,327 common, $0.0001 par, one class (10-Q for the quarter to
  2026-06-30, filed 2026-08-05, cover as of 2026-07-31, accession `0001104659-26-090540`; `python Screens/cover_shares.py PRIM`).
- **Market cap:** $4,257M (53.832327M x $79.08).
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 2026-10-02 (`python tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-24, `0001104659-26-018677`: Item 1 (business, customers, competition, contract
    provisions), Item 1A (read for price competition, fixed-price risk, renewables policy, bonding), Item 7 (MD&A, segment
    results 2023 to 2025, estimates, backlog, liquidity), Item 8 (balance sheet, income statement, cash flow statement,
    the AR securitization note).
  - 10-Q for Q2 2026, filed 2026-08-05, `0001104659-26-090540`: statements, Note 4 (PayneCrest), Note 13 (the class action),
    the AR facility, changes in estimates, unapproved contract modifications, segment MD&A, Part II Item 2 (purchases).
  - DEF 14A filed 2026-03-20, `0001104659-26-032237`: leadership history, the Annual Incentive Plan and the LTIP, severance terms.
  - 8-Ks: `0001361538-25-000026` (2025-06-04, auditor change Moss Adams to Baker Tilly, no disagreements);
    `0001361538-25-000035` (2025-10-07, new CEO from 2025-11-10); `0001361538-25-000038` (2025-11-03, Q3 2025);
    `0001361538-26-000007` (2026-02-23, FY2025); `0001361538-26-000011` (2026-03-17, a director retires);
    `0001361538-26-000014` (2026-05-05, Q1 2026); `0001361538-26-000017` (2026-06-22, guidance cut, COO departure,
    May buyback); `0001361538-26-000021` (2026-08-04, Q2 2026); `0001361538-26-000030` (2026-08-31, two directors added).
  - Earlier 10-Ks for the acquisitions: FY2021 `0001558370-22-002400` (FIH), FY2022 `0001558370-23-002191` (PLH).
  - **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $4,407.8M on the filed balance sheet
    of `0001104659-26-018677`, against $4,408M in the XBRL table `tools/run.py` prints. Agrees. Operating cash flow 2025,
    $470.4M filed, against 470 in the same table. Agrees.
- **`python tools/run.py PRIM`, arithmetic lines only** (its yields, its "growth the price assumes" and its window language
  are v4 material and are not used, Part VII). Checked against the filing for the three known defects: the share count is
  current (cover of 2026-07-31; no split since); stock pay is not zero and matches the filed cash flow statement ($11.8M,
  $15.1M, $20.6M for 2023 to 2025); operating cash flow carries no securities purchases, **but it does carry receivables sold
  under the AR securitization facility**, which the filing books in operating cash: $50.0M net in 2025, about $75.0M in 2023
  (derived: $125.0M outstanding at 2025-12-31 less 2025's $50.0M, with 2024's $10.0M sold and $10.0M repaid), and $88.5M
  net in the first half of 2026 ($213.5M outstanding at 2026-06-30). These are taken out of owner cash below. Owner cash is
  computed from the filed cash flow statements, not from `run.py`'s owner-earnings lines.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would own this "if the market closed for five years" (**[M1997-109]**: "Would I
be happy buying this stock if the market closed for five years?"), and the quotation carries no instruction: "It just tells
us prices." **[M2006-077]**. The price fell from $111.29 (the company's own May purchase price) to about $79 after the June
guidance cut; neither number says anything about what the business earns. No macro enters: renewables tax policy, data-centre
demand and interest rates are named in the filings and in the press releases as the reasons for optimism; the question is
"the average profitability of the business over time" **[M2015-016]**, and macro forecasts "just never enter into the
discussion" **[M2000-094]**. Who is paid to tell me: the press releases lead with adjusted EBITDA and record backlog, and the
executives' annual bonus is paid on adjusted EBITDA and on new business booked (proxy, below); "you do not get impartial advice
from Wall Street" **[M2020-037]** applies with equal force to the issuer's own framing. The analyst's habit: hunt the case
against, "to possibly reject your original hypothesis" **[M1998-144]**, and avoid "always your previous conclusion" **[M2016-054]**.

**Contrary evidence, written down as found** **[M1997-127]** ("write it down in the first 30 minutes"), in the order it turned up:
1. 2026-06-22 8-K: full-year 2026 net income guidance cut from $223.0M to $234.0M down to $71.0M to $101.0M; renewables revenue
   now expected about $2.1B against about $3.0B in 2025; cost overruns on six renewables projects, assessed with "a third-party
   industry expert"; the COO departed the same day, treated as a termination without cause.
2. Same 8-K and the 10-Q: the company bought 449,287 shares in May 2026 at $111.29 ($50.0M), in the month after its Q1 release
   called the renewables problems "isolated" and one month before the cut; the price is now about $79.
3. 10-Q Note 13: a putative securities class action filed 2026-07-21 against the company and current and former officers,
   alleging false and misleading disclosures.
4. 10-Q: operating cash flow for the first half of 2026 was minus $131.3M, and that figure already includes $88.5M of
   receivables sold under the securitization facility.
5. 10-Q: $244.0M of unapproved contract modifications in transaction prices at 2026-06-30, of which $205.9M already
   recognised as revenue; tangible equity at the same date was about $180M (computed in the balance-sheet reading below).
6. Proxy and 8-Ks: the CEO separated by mutual agreement on 2025-03-20; the chairman served as interim CEO; an outside CEO
   started 2025-11-10; the COO, under an employment agreement of January 2025, left 2026-06-22.
7. The four competitors' own 10-Ks say price decides most awards (Q2, test 9), and Quanta's says there are "relatively few
   barriers to entry" in some of its industries.
8. 10-K Item 7: cost escalation is capped in certain contracts and "In some cases, our actual cost increases have exceeded
   the contractual caps" (Q2, test 4).

Evidence the other way, written down with the same care: record total backlog of $13.9B at 2026-06-30 ($8.2B of it MSA);
Utilities segment operating margin rose from 3.7% (2023) to 5.7% (2024) and 6.8% (2025); "Historically, substantially all of
the gas and electric distribution and communications customers have renewed their MSAs with us" (10-K Item 1); a lost-time
injury rate of 0.11 against an industry average of 0.90 (10-K Item 1); return on tangible assets near 10% pre-tax through the
cycle, level with the peers.

## THE STANDING RULE
Common stock, bought unlevered and sized so that its total loss could not ruin the buyer, carries no call on the buyer's cash;
the rule binds the buyer's conduct: "We are never going to risk what we have and need" **[M2012-081]**, and "borrowed money has
no place in the investor's tool kit" **[L2014-005]**. Nothing in this name changes that; no purchase is made in any case.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** "the first question is, can I understand it?" **[M1995-051]**, where understanding is
  "what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; the product may stay
  opaque if "I understand the economic dynamics of the industry" **[M2011-014]**, which the same row spells out as "Is there
  ease of entry?" **[M2011-014]**.
- **What the business is (10-K FY2025, `0001104659-26-018677`, Item 1 and Item 7).** A specialty contractor in two segments.
  Utilities (2025 revenue $2,691.7M before eliminations): construction and maintenance of gas and electric distribution and
  transmission and communications networks, "Substantially all" of it under renewable unit-price MSAs. Energy (2025 revenue
  $5,018.6M before eliminations; derived from the segment table: 2024's $4,032.0M plus the stated $986.6M increase):
  engineering, procurement and construction of utility-scale solar, storage, gas generation, industrial, pipeline and highway
  work, mostly project-based. MSA work was 32.0% of 2025 revenue (36.8% in 2024, 36.7% in 2023); work won by competitive bid
  was about 27.6% of 2025 revenue; the top ten customers were 53.1% of 2025 revenue, "a different group of customers" each year.
  Contracts are unit-price, time and material, fixed-price or cost-plus; "any increase in our unit cost over the unit price
  bid, whether due to inflation, inefficiency, faulty estimates or other factors, is borne by us" (Item 1).
- **The key variables and whether they are foreseeable** (**[M1998-044]**: "evaluating how predictable they were first").
  (a) The spread a contractor earns on labour and equipment priced by bid or negotiated unit rates: foreseeable from the
  record, sixteen years of filed margins between 2.9% and 6.8% and four competitors' filings showing the same band (Q2's
  table). (b) Utility capital and maintenance spending on distribution networks: foreseeable in direction, regulated and
  recurring. (c) The volume of renewables EPC work, about 40% of 2025 revenue ($3.0B of $7.57B): a policy forecast that the
  filer itself flags ("Changes to federal support for renewable energy projects may also negatively affect future demand for
  our services", Item 1A); the 2026 drop to about $2.1B shows how fast it moves. (d) Execution on fixed-price and unit-price
  projects: the variable that turned 2026 from a forecast $223.0M to $234.0M of net income into $71.0M to $101.0M.
- **Do the past statements tell me the future ones?** **[M2008-033]** ("what the future financial statements are going to look
  like"). On the economics, yes: the statements from 2010 to mid-2026 show the same thin spread, interrupted by troughs and project losses
  (operating margin 3.5% and 2.9% in 2015 and 2016, from XBRL, the filings of those years not read; the PLH legacy projects and a communications project in 2023; pipeline negative gross margins in 2022 per the
  FY2022 10-K; six renewables projects in 2025 and 2026). On the volume of any one end market, no.
- **Routing.** This is not a business whose economics change fast with technology; it is a labour-and-equipment trade whose
  pricing is set by bid. The volume of renewables work is not foreseeable, but the economics of the firm are: a reasonable fix
  says a price-taking contractor earning a mid-single-digit spread, with periodic losses on fixed-price work. The industry is
  seen and the firm's place in it is seen; whether that place is protected is the castle question, which Q2 owns
  (**[M1997-148]**: Q1 comes first, then "whether a company can have a sustainable edge").
- **Doubt recorded.** "if you have doubts about something being into your circle of competence" **[M2002-092]**, it is not.
  The doubt here is about the volume mix, not about the economic dynamics; the dynamics are stated in the same words by the
  filer and by four competitors. "Just because" growth can be seen "does not mean we can judge what its profit margins and
  returns on capital will be as a host of competitors battle for supremacy" **[L2009-005]**: that row sends the margin question
  to the evidence, and the evidence (sixteen years of it, five filers) answers it.
- **VERDICT: IN.** The economics are understood; what they show is answered at Q2. (Filing facts: 10-K FY2025 Items 1, 1A, 7.)

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, asked on the premise that "all moats are subject to attack
in a capitalistic system" **[M1995-038]**; a moat "protects excellent returns on invested capital" **[L2007-004]**.

**What the filer offers as its castle** (10-K FY2025, `0001104659-26-018677`, Item 1): long MSA relationships ("Historically,
substantially all of the gas and electric distribution and communications customers have renewed their MSAs with us"); places
on customers' pre-qualified contractor lists, won by "prior performance", safety, "financial strength" and "bonding capacity";
a large owned and leased equipment fleet, of which the filer says "The cost of construction equipment, and in some cases the
availability of construction equipment, provides a significant barrier to entry into several of our businesses"; a stable,
cross-trained, partly unionised craft workforce; a safety record well better than the industry's. The tests below ask whether
any of these has kept returns above what the trade earns.

**The tests, each with its filing fact.**
1. **The castle questions: what keeps it standing, and how permanent?** The filer's own answer to why customers choose it
   puts price first: "pricing is a key element for most construction projects and service agreements" (Item 1, Customers);
   "We are engaged in a competitive business in which some customer contracts are awarded through bidding processes based on
   price and the acceptance of certain risks"; "The strong competition in our markets requires maintaining skilled personnel
   and investing in equipment and technology, which can put pressure on profit margins"; "an increase in competition may
   result in a decrease in new awards, a decrease in profit margins, or both" (Item 1A). The reasons it lists for being chosen
   (relationships, prequalification, equipment, safety) are claimed as their own grounds by the three competitors whose
   10-Ks were read below (Quanta: "technical expertise and experience", "safety ratings, financial and operational
   resources"; MasTec: "adequate financial resources, technical expertise, high safety ratings, established customer
   relationships"; MYR Group: "reputation for safety, quality and reliability"), so none is this company's own.
2. **Would it stand without the lord?** Not the deciding test here. The business ran through three chief executives and lost
   its COO between March 2025 and June 2026 (proxy, `0001104659-26-032237`; 8-Ks `0001361538-25-000035`,
   `0001361538-26-000017`); the renewables overruns grew through that span. The record does not show a castle that needs no
   management; it shows a trade in which execution decides the year.
3. **The money test: could a well-funded attacker take it?** "could I do it?" **[M2011-015]**. The answer is in the record of
   the company itself and in its largest rival's filing. Primoris entered utility gas and communications work by buying
   Future Infrastructure for about $604.7M (January 2021, FY2021 10-K `0001558370-22-002400`), power delivery by buying PLH
   for about $438.3M (August 2022, FY2022 10-K `0001558370-23-002191`), and data-centre electrical work by buying PayneCrest
   for about $404.7M (May 2026, 10-Q `0001104659-26-090540`): each position was bought with money. Quanta's 10-K for FY2025
   (`0001050915-26-000006`, Competition and Market Demand) says: "there are relatively few barriers to entry into some of the
   industries in which we operate and, as a result, organizations that have adequate financial resources and access to
   technical expertise may become a competitor." That is the attacker with money, stated by the industry's largest firm.
   The rows: "there are some industries that are just never going to have barriers to entry" **[M2012-106]**; "you can create
   another airline" **[M2013-054]**; "one competitor is frequently enough to ruin a business" **[M2012-108]**.
4. **Pricing power, and the agony before a price rise.** "a prayer session before you raise your prices a penny" **[M2005-020]**;
   strong positions "manage to pass through increases in raw material costs" **[M2005-017]**. The filing (Item 7, Material
   Trends and Uncertainties): "the annual adjustment provided by certain contracts is typically subject to a cap and there can
   be an extended period of time between the impact of inflation on our costs and when billing rates are adjusted. In some
   cases, our actual cost increases have exceeded the contractual caps, and therefore negatively impacted the profitability of
   our operations until the contracts have been renegotiated to reflect these higher costs." Costs pass through late, capped,
   and only by renegotiation. The test fails on the filer's own words.
5. **Unit volume and share of mind.** Not a consumer franchise; nobody asks for the contractor by name. Backlog at a record
   $13.9B (2026-06-30, 8-K `0001361538-26-000021`) measures work booked, not price earned on it; in the same quarter the
   Energy segment booked about $2.0B of awards and ran a gross margin of minus 0.3%.
6. **The low-cost position.** The exception for a commodity field is the low-cost operator: "Another way to prosper in a
   commodity-type business is to be the low-cost operator." **[L2004-007]**. No filing fact shows Primoris to be the low-cost
   operator; its margins sit inside the competitors' band (the table below), not above it, and the six overrun projects of
   2025 to 2026 are the mark of the operator whose costs ran over its bids. "Our textile business was not the low-cost
   producer." **[M1997-010]**; "the guy with the lower cost comes in and kills you" **[M2001-013]**.
7. **The brand in the customer's mind.** No instance in the filings of work won on the name; the top ten customers are a
   different group each year and a large project "may result in significant revenue in one year, with significantly less
   revenue in subsequent years" (Item 1).
8. **Would the customer still choose it over the low bid?** "the low bid" **[M2017-009]** is how much of this work is awarded:
   construction contracts "are primarily obtained through competitive bidding or through negotiations with customers"
   (Item 1). The rows' failing answer: "most insureds don't care from whom they buy" **[L2004-003]**, so that "price competition
   in insurance is usually fierce" **[L2004-003]**. Read for contractors, it is the same sentence.
9. **Ask the competitors** ("which one would it be and why?" **[M1999-130]**; "everybody loves talking about their competitors"
   **[M2017-091]**). Their filings answer the castle question for the whole trade:
   - Quanta (10-K FY2025, `0001050915-26-000006`): "A significant portion of our revenues is currently derived from unit price
     or fixed price agreements, and price is often an important factor in the award of such agreements. Accordingly, we could
     be underbid by our competitors."
   - MasTec (10-K FY2025, `0000015615-26-000020`): customers "award most of their work through a bid process, and price is
     often a principal factor in determining which service provider is selected."
   - MYR Group (10-K FY2025, `0000700923-26-000007`): "Competition in both of our business segments is primarily based on the
     price of the construction services and upon the reputation for safety, quality and reliability of the contractor."
   - Primoris itself names Quanta, Dycom, MYR Group and MasTec as its utility competitors, and Blattner and Mortenson in
     renewables (Item 1). Dycom's 10-K (`0000067215-26-000008`) was not read in text; its figures below are XBRL only.
10. **Widening or narrowing?** "grows either weaker or stronger" **[L2005-010]**. Narrowing in Energy: segment gross margin
    11.4% (2023), 11.0% (2024), 10.1% (2025), then minus 0.3% in Q2 2026, with consolidated revenue negatively adjusted by $87.6M in
    the first half of 2026 for changes in estimates on performance obligations satisfied before 2026 (10-Q). Widening in Utilities over 2023 to
    2025 (operating margin 3.7%, 5.7%, 6.8%), but the 2023 base was depressed by PLH legacy projects (10-K Item 7), and the
    first half of 2026 gave back a point of gross margin (11.9% to 10.9%, 10-Q). "the improvement you get one day, your
    competitor gets the next day" **[M2004-053]**.
11. **What could destroy, modify or reduce it?** **[M2000-014]** ("destroy, or modify, or reduce the economic strengths").
    Nothing needs to: there is no excess return to reduce. The risks the filer lists (renewables policy, bonding availability,
    fixed-price overruns, customer concentration) bear on volume and on losses, not on a protected spread.

**The competitor row** (same metric, each company's own XBRL filings via SEC companyfacts, latest vintage; operating income
over revenue, and operating income over total assets less goodwill and intangibles at year end, pre-tax; transcription from
tags, flagged; Quanta's FY2025 operating income of $1,611.5M checked against the filed text of `0001050915-26-000006` and
agrees; MasTec and Dycom tag no operating-income line, so their figure is pre-tax income plus interest expense (MasTec) and
pre-tax income alone (Dycom, no interest tag found), which understates Dycom):

| 2012 to 2025 (fiscal years) | median margin | lowest year | highest year | median return on tangible assets | lowest | highest |
|---|---|---|---|---|---|---|
| Primoris (`0001104659-26-018677` and prior 10-Ks) | 4.6% | 2.9% (2016) | 6.4% (2013) | 9.9% | 5.7% | 14.1% |
| Quanta (`0001050915-26-000006`) | 5.3% | 3.1% (2015) | 7.9% (2012) | 10.4% | 6.9% | 13.6% |
| MasTec (`0000015615-26-000020`) | 5.4% | minus 0.7% (2023) | 7.1% (2019) | 11.2% | minus 1.3% | 15.9% |
| MYR Group (`0000700923-26-000007`) | 3.9% | 1.6% (2024) | 6.2% (2013, 2014) | 9.6% | 4.2% | 13.6% |
| Dycom, FY2012 to FY2026 (`0000067215-26-000008`) | 5.1% | 1.7% (FY2022) | 8.2% (FY2017) | 9.7% | 3.0% | 18.0% |

Primoris's own series, operating margin by year from XBRL (the 10-K values for 2023 to 2025 read in the filed segment
tables): 2010 6.1%, 2011 6.8%, 2012 6.2%, 2013 6.4%, 2014 5.0%, 2015 3.5%, 2016 2.9%, 2017 4.5%, 2018 4.4%, 2019 4.5%, 2020
4.7%, 2021 4.9%, 2022 4.4%, 2023 4.4%, 2024 5.0%, 2025 5.4%; first half of 2026 about minus 0.1% (operating income $24.4M in
Q1 and minus $26.8M in Q2 on revenue of about $3.2B, 8-Ks `0001361538-26-000014` and `0001361538-26-000021`). The full tables
are in `Test Runs/_research 2026-10-05 PRIM/peers_out.txt`.

What the row shows: five firms in one band, around 4% to 5% on revenue and about 10% pre-tax on tangible assets, each with
bad years near or below zero. None stands above the others for long, Primoris included. A castle would show as a return the
others cannot reach; the trade's returns are level, which is what the filers' sentences on price say they would be.
"average is not going to go away, either" **[M2000-072]**; "anything you do, your competitors can copy" **[M1996-017]**.

**The deciding fact, single.** The filer states that price is "a key element for most construction projects and service
agreements" (10-K FY2025, Item 1), and three of the four named competitors state the same of their own awards in their own
10-Ks. A business whose customer buys on the low bid is on the rules-OUT list of Q2 (**[L2004-003]**, **[M2017-009]**); the
sixteen-year margin record and the competitor row are the evidence that the price competition is real, not a risk-factor
formula.

**Shown open, or future not judgeable?** The framework sends a castle "shown on the evidence to be filling in" to OUT and a
castle whose future cannot be judged to TOO HARD (Q2, What it rules OUT; **[M2000-019]**; the boxes are "in, out, and too
hard" **[M2006-013]**). This is the first case: the future can be judged, and what it shows is a trade without a moat. There
is no castle to keep standing; the question of how long it stands does not arise. The rows' own mistakes point here: "where I
misgauged the competitive position of the business" **[M2012-031]**. A lower price does not reopen it: one cannot "turn any
investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** No castle: price decides the awards by the filer's and the competitors' own statements; costs pass through
  only late, capped and by renegotiation; margins sit inside the competitors' band for sixteen years with recurrent losses on
  fixed-price work. Rows: **[M1995-038]**, **[M2012-106]**, **[M2005-017]**, **[L2004-003]**, **[M2017-009]**, **[L2004-007]**,
  **[M2000-072]**.

## Q3 to Q12: NOT REACHED
The run closed OUT at Q2 (operator rule 2; Part VII: a STOP that fails closes the file). Nothing below is a clearance and
nothing below answers Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 or Q12. At the owner's request, the record beyond the close follows,
every number in it headed as computation.

---
## RECORD BEYOND THE CLOSE (COMPUTATION — NOT A CLEARANCE)
*Operator rule 3. Everything in this section was produced after Q2 closed the file OUT, at the owner's request for the value
figures. It carries no entry language, answers no question, and changes no verdict. Where a later question would have had to
rule on a fact, the fact is recorded and the ruling is left undone.*

### The balance sheets, ten year-ends, read before the income account
Read as the rows ask, "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
Figures in $M from the XBRL table `tools/run.py` prints (first-filed vintage), with 2024, 2025 and 2026-06-30 read in the
filed statements (`0001104659-26-018677`, `0001104659-26-090540`). Equity for 2016 to 2018 is total assets less total
liabilities (the tag is absent). Tangible equity is equity less goodwill and intangibles. Debt is the long-term portion as
tagged, plus the current portion where read in the filing.

| year-end | total assets | equity | goodwill | intangibles | tangible equity | cash | debt | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 1,171 | 499 | 127 | 33 | 339 | 136 | 203 | 335 |
| 2017 | 1,256 | 562 | 153 | 45 | 364 | 170 | 193 | 396 |
| 2018 | 1,594 | 607 | 206 | 81 | 320 | 151 | 306 | 461 |
| 2019 | 1,830 | 630 | 215 | 70 | 345 | 120 | 296 | 531 |
| 2020 | 1,970 | 715 | 215 | 61 | 439 | 327 | 269 | 625 |
| 2021 | 2,543 | 990 | 582 | 171 | 237 | 201 | 594 | 727 |
| 2022 | 3,544 | 1,109 | 872 | 249 | minus 12 | 249 | 1,065 | 848 |
| 2023 | 3,827 | 1,236 | 858 | 228 | 150 | 218 | 885 | 961 |
| 2024 | 4,196 | 1,410 | 857 | 208 | 345 | 456 | 735 | 1,128 |
| 2025 | 4,408 | 1,681 | 857 | 190 | 634 | 536 | 470 | 1,386 |
| 2026-06-30 | 4,639 | 1,606 | 1,052 | 375 | 180 | 218 | 797 | n/r |

What the figures say:
- **Retained earnings went into purchased goodwill.** Retained earnings rose $1,051M from 2016 to 2025; goodwill and
  intangibles rose $887M over the same span, and a further $380M in the first half of 2026 with PayneCrest. With the 2021
  equity issue ($149.3M net at $35 a share, FY2021 10-K) the growth of the balance sheet is bought growth. Tangible equity was
  about $340M in 2016 and about $180M at mid-2026 after nine years of profits; it went below zero at the end of 2022 after PLH.
- **Debt follows the deals.** $203M (2016), $1,065M (2022, after FIH and PLH), paid down to $470M by 2025 from the strong
  2024 and 2025 cash flows, then $797M at mid-2026 (term loan raised by $411.8M on 2026-05-01 and extended to 2031, 10-Q).
- **Working capital is financed by customers and by receivables sales.** At 2025-12-31 receivables of $723.4M and contract
  assets of $936.9M (together 22% of revenue) stood against payables of $744.3M and contract liabilities of $633.6M; contract
  liabilities rose $251.2M in 2024 alone (renewables advances). A further $125.0M of receivables had been sold and taken off
  the balance sheet (2025), $213.5M by mid-2026, under a facility that matures 2027-03-24.
- **What the balance sheet does not show, and the income account relies on.** Unapproved contract modifications in
  transaction prices of $201.2M (2025, $179.5M already in revenue) and $244.0M (mid-2026, $205.9M already in revenue): at
  mid-2026 the revenue booked on change orders the customers have not agreed exceeds tangible equity. Operating lease assets of
  $488.9M (2025) carry part of the equipment fleet off the capital-spending line (new leases of $260.4M, $228.7M and $161.5M
  in 2023 to 2025).
- **"what they don't say and what they can't say"**: the rows name "progress payment-type things" **[M2013-086]** among the
  places accounting can be gamed, and revenue not matched "on something close to cash in the short-term" **[M1995-065]**.
  Prepaid expenses and other current assets rose from $95.6M (2024) to $137.8M (2025) and $168.2M (mid-2026) while revenue
  fell in 2026. These facts are recorded; whether they make the accounts confusing or suspect is Q4's ruling, NOT REACHED.

### Owner cash after every real cost (the Q4 recast, as computation)
From the filed cash flow statements (FY2025 10-K for 2023 to 2025; XBRL for 2021 and 2022): operating cash flow, less
receivables sold under the securitization facility, less stock pay, less all capital spending; the depreciation variant
and the variant net of equipment-sale proceeds beside it. Never a net-income proxy (operator rule 5).

| $M | 2021 | 2022 | 2023 | 2024 | 2025 | five-year average |
|---|---|---|---|---|---|---|
| operating cash flow (filed) | 79.7 | 83.3 | 198.5 | 508.3 | 470.4 | 268.0 |
| less receivables sold (facility) | 0 | 0 | 75.0 | 0 | 50.0 | 25.0 |
| less stock pay | 10.5 | 7.4 | 11.8 | 15.1 | 20.6 | 13.1 |
| less capital spending | 133.8 | 94.7 | 103.0 | 126.5 | 129.9 | 117.6 |
| **owner cash, all capital spending** | **minus 64.6** | **minus 18.8** | **8.7** | **366.7** | **269.9** | **112.4** |
| variant: net of equipment-sale proceeds | minus 15.1 | 22.5 | 72.4 | 466.0 | 302.4 | 169.6 |
| variant: depreciation in place of capital spending | minus 18.0 | minus 2.3 | 26.5 | 417.3 | 325.6 | 149.8 |

The five-year average leans on 2024 and 2025, two years in which customer advances ($251.2M in 2024) and payables ($121.0M in
2025) financed the work; the first half of 2026 then used $131.3M of operating cash, about $219.8M before receivables sales,
which is outside the five fiscal years and not in the average. Depreciation is a real cost **[R1996-023]**; EBITDA, which
every release leads with, is "utter nonsense" **[M1998-086]** as earnings; stock pay is deducted **[L2015-003]**. The
company's own equipment sales booked gains of $48.1M, $44.8M and $21.7M (2023 to 2025), so the fleet is sold above book; the
headline uses all capital spending, as the convention says, and shows the net figure beside it.

### Value range, fair-price band, cheap price (COMPUTATION; the file closed before Q7)
The Q7 CONVENTION construction, carried out as arithmetic only: five-year average owner cash; the no-growth end; the
shown-growth end at the growth of aggregate owner cash between the 2016 to 2020 average ($79.1M) and the 2021 to 2025 average
($112.4M), 7.3% a year, for ten years, then zero nominal growth; discounted at the 30-year Treasury, 5.63% ("the yield on
long-term U.S. bonds" **[L2000-021]**), as a range ("working with a range of possibilities is the better approach"
**[L2000-024]**). The growth figure is bought growth: the FIH and PLH purchases ($1,043M) fall inside the span and are not
deducted from owner cash, so the shown-growth end overstates what the business grew by itself (**[L2005-003]** on base years
applies as well: the 2021 to 2023 years were near zero or negative).

| per share, 53.83M shares | no growth | shown growth | width |
|---|---|---|---|
| **headline: all capital spending ($112.4M)** | **$37.08** | **$66.06** (7.3%) | 1.8 to 1 |
| variant: net of sale proceeds ($169.6M) | $55.97 | $147.52 (12.3%) | 2.6 to 1 |

- **Against the price of $79.08:** above the top of the headline range. The expected return at $79.08 on the headline case is
  2.6% (no growth) to 4.8% (shown growth) on after-tax owner cash, 3.7% to 6.5% grossed up to pre-tax at the 2025 effective
  tax rate of 28.4%: below the floor of about ten percent pre-tax (CONVENTION, Q7; "we have no scientific studies or anything"
  **[M2003-149]**). To earn 10% on after-tax owner cash at $79.08, owner cash would have to grow about 19% a year for ten
  years; to earn the Treasury rate, about 9.6%.
- **FAIR-PRICE BAND** (prices inside the range at which the expected return is at or above about ten percent pre-tax):
  **$37.08 to $48.17**, and only if owner cash keeps growing at the shown 7.3%; on the no-growth case no price inside the range
  reaches the floor (the floor price there is $29.16). On the stricter reading, ten percent on after-tax owner cash, the band
  is empty: the shown-growth floor price is $34.49, below the range bottom.
- **CHEAP PRICE** (below which the case needs no pencil): **$20.88**, the price at which the no-growth case alone earns ten
  percent on after-tax owner cash, with no growth, no tax gross-up and no sale proceeds assumed. CONVENTION, ours: the owner's
  request names no rule, and the rows give the screamer only by example ("if I was buying it at 35 billion" against a worth
  near 100 **[M2008-068]**; "a big discount from that present value" **[M1997-126]**; "It should scream at you." **[M2009-005]**);
  $20.88 is about 56% of the range bottom.
- **What the range leaves out:** the first half of 2026 (cash used, a net loss of $6.7M); PayneCrest ($404.7M paid in May 2026,
  its earnings not yet in any full year, its price added to debt); the company's 2026 guidance (net income $71.0M to $101.0M),
  which is a projection and is not used ("never looked at a projection" **[M1995-050]**). Each of these, if it entered, would
  lower the range, not raise it.

### Facts a Q4, Q5, Q6 or Q9 would have had to weigh (recorded, NOT ANSWERED)
- **The numbers in the issuer's mouth.** Every release from Q3 2025 to Q2 2026 leads with adjusted EBITDA, adjusted net income
  and adjusted EPS; adjusted net income adds back stock pay and amortization; guidance was raised in November 2025 (for 2025) and the 2026
  net income guidance was cut by about three fifths at its midpoint in June 2026. A management that features adjusted earnings "makes us nervous" **[L2016-006]**.
- **Pay** (proxy, `0001104659-26-032237`). The cash bonus is weighted 60% on adjusted EBITDA (before depreciation, stock pay,
  transaction costs, impairments and severance), with components on new business generated, cash management and safety;
  2025's adjusted EBITDA of $531.1M against a $449.7M target paid the maximum 200%. PSUs vest on net income and operating
  margin. No component charges for capital. A bonus on bookings in a trade priced by bid rewards volume won, and "you get what
  you reward for" **[M2016-083]**; pay tied "to what is actually under the reasonable control of the person" **[M2003-019]**.
  CEO severance without cause: 200% of salary plus accelerated vesting; on a change in control, 2.5 times salary and target bonus.
- **The buyback.** 449,287 shares in May 2026 at $111.29 ($50.0M), the same month the term loan was raised by $411.8M for
  PayneCrest and before the operating cash outflow of the half-year was reported; the programme names no price ("The timing of
  share purchases, if any, depends on market conditions, share price and other factors", 10-Q). The rows allow a buyback only
  with funds "beyond the near-term needs of the business" and below "intrinsic value, conservatively-calculated" **[L1999-023]**;
  value is "entirely purchase-price dependent" **[L2016-002]**. The price paid was three times the bottom and 1.7 times the top
  of the computed range.
- **People.** The CEO separated by mutual agreement on 2025-03-20; the chairman was interim CEO until an outside CEO from Jacobs
  started 2025-11-10; the COO left 2026-06-22, "not related to any financial or accounting issue". A putative securities class
  action was filed 2026-07-21. The forward-looking statements of the 10-K, the 10-Q and the June release list "the results of
  the review of prior period accounting on certain projects" and "governmental investigations and/or inquiries" among the risk
  factors; no instance found, in a text search of the 10-K and the 10-Q for "restat", "material weakness", "subpoena",
  "investigation" and "prior period", of a restatement, a material weakness or a named inquiry.
- **Debt and sudden demands.** Debt of $797M at mid-2026 against a half-year operating loss; $213.5M of receivables sold under a
  facility maturing 2027-03-24; performance bonds, which sureties "can decline to issue bonds at any time or require the posting
  of additional collateral" (10-K Item 1A). The rows ask for "no significant near-term cash requirements"
  **[L2014-023]** and warn that "maturities must actually be met by payment" **[L2010-020]**; debt is read against "the ability
  to pay debt" **[M1995-104]**. In 2025, operating income covered net interest of $28.7M about 14 times; in 2026 to date it did not.

---
## THE BOX
**OUT, at Q2.** No castle: price decides the awards in the filer's own words and in its competitors' 10-Ks, costs pass through
only late and capped, and sixteen years of margins sit inside the competitors' band with recurrent losses on fixed-price work.
Not TOO HARD: the castle's future can be judged, and it shows none (**[M2006-013]**, **[L2004-003]**, **[M2012-106]**). No
research pass is opened (that is for TOO HARD (WORK) only). For the record only, COMPUTATION: value $37 to $66 a share
(variant $56 to $148), fair-price band $37 to $48 conditional on growth, cheap price $21, against $79.08.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written in order, Step 0 and Q1 first, then Q2, then the record beyond the
      close. **Not committed after each question**: the dispatching instruction for this run forbade commits; the write-early
      order was kept in the file, not in git.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, with every quoted fragment beside an id
      matched as a substring of that row); no v4 (E) id is cited; every filing fact carries its accession; numbers not from a
      filing are computation, labelled.
- [x] The order was kept; Q2 closed the run OUT; nothing after it is a clearance, and the record beyond the close is headed
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash flow statements, with receivables sales removed; never a net-income
      proxy; the sovereign from the US Treasury, dated; the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations section, items 1 to 8, and the
      evidence the other way beside it).
- [x] Not a point-in-time run; no row was used for its date.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three known defects were checked and a fourth form of the
      operating-cash defect (receivables sales) was found and removed.
- [x] `python tools/check_framework.py` PASS (run after the file was complete; result in the reply to the dispatcher).
- Honest gaps: the 2010 to 2020 filings were not read in text (XBRL only for those years); Dycom's 10-K was not read in text and
  its figure is pre-tax income without interest added back; the 2023 receivables sale of $75.0M is derived, not read in the
  FY2023 10-K; no competitor, customer or employee was spoken to.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The floor and the range are on different tax bases.** The Q7 CONVENTION builds the range from owner cash, which is after
tax, and the floor CONVENTION is "about ten percent pre-tax"; the rows themselves state the figure both ways (after-tax streams
in 1994, pre-tax returns in 2002). For a 28% taxpayer the choice moves the floor price by 40%. This run showed both and took
the after-tax reading for the cheap price. A sentence fixing the basis would settle it. (2) **"Growth shown on aggregate owner
cash" breaks down** when the five-year window opens with negative years (2021 and 2022 here) and when the growth was bought
with acquisitions that owner cash never deducts. This run measured growth between two five-year averages and said the growth
was bought; the convention could say how acquisitions inside the window are charged. (3) **Receivables sold under a
securitization facility sit inside operating cash** under GAAP; nothing in Q4 or the convention names them, and they moved this
name's owner cash by $25M a year on average and by $88.5M in one half-year. They were removed here as financing in substance.
(4) **The owner's three reporting figures for a file closed before Q7** (range, fair-price band, cheap price) have no rule for
the cheap price and none for the band when the floor price falls below the range bottom; both were defined here as
conventions and confessed. (5) **OUT against TOO HARD at Q2** turned on whether the filer's and the competitors' own sentences
on price count as a castle "shown" open. The text supports OUT (the low-bid customer is on the rules-OUT list), but the line
between "shown on the evidence" and "cannot be judged" is drawn by example only; a sentence saying that a filer's own statement
that price decides most awards, corroborated by the record, is sufficient evidence of an open castle would make two analysts
land in the same box.
