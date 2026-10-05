# Company Run — KLX Energy Services Holdings, Inc. (Nasdaq: KLXE) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The assignment's blind rule bars opening `PORTFOLIO.md`, so
this run does not know whether the operator holds KLXE. It is written as a purchase run for a name not held.

**CONTAMINATION, declared.** (1) The assignment told me the screen found three-year owner earnings negative before I
computed anything; I recomputed it from the filings and it holds, but the anchor was there. (2) The session's git status
and recent commit subjects name other 2026-10-05 runs and their boxes (RYZ, MBUU "OUT at Q2"; untracked CSW, HOS, SHOE
run files). I opened none of them. (3) `tools/run.py` printed only arithmetic lines this time (no v4 ids); its market
cap and share basis are stale (see Step 0). No other `Test Runs/` file about KLXE was opened; none was looked for.

Working folder: `Test Runs/_research 2026-10-05 KLXE/` (filings as text, `run_py_output.txt`, `peers/peer_table.txt`,
`peers.py`, `rows.txt`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.39 (intraday 2026-10-05, Yahoo Finance chart API; **aggregator, flagged** per operator rule 5). Last
  full close $1.38 on 2026-10-02 (same source). `tools/run.py` printed $1.42 (also an aggregator). The rights-offering
  subscription price was $1.49 (8-K 2026-08-10, accession 0001193125-26-342539).
- **Shares by class:** one class, common stock $0.01 par. Cover of the latest periodic filing: **21,273,059** as of
  2026-07-31 (10-Q for 2026-06-30, filed 2026-08-11, accession 0001738827-26-000032; `python Screens/cover_shares.py
  KLXE`). **That count is stale.** The rights offering closed 2026-09-29: 24,975,001 shares sold for $37.2M cash and
  59,273,445 shares issued to the noteholders in the Backstop Exchange; "the Company expects to have 105,677,168 shares
  of Common Stock issued and outstanding" (8-K filed 2026-09-30, accession 0001738827-26-000058). **This run uses
  105,677,168.** Penny warrants were also issued to noteholders in March 2025 (up to 2,373,187 shares) and March 2026
  (up to 803,712 shares), part exercised (10-Q 0001738827-26-000032); not added, a small count beside 105.7M.
  **Reverse split:** 1-for-5, effective 2020-07-28, the day the all-stock QES merger closed (10-K FY2025, accession
  0001738827-26-000013). No reverse split since. The rights (KLXER) were struck from Nasdaq by Form 25-NSE filed
  2026-09-24 (accession 0001354457-26-000904, file `klxerform25.txt`): that Form 25 is the rights expiring, not the
  common leaving Nasdaq; the common remains on the Nasdaq Global Select Market per every 8-K cover through 2026-09-30.
- **Market cap:** 105,677,168 × $1.39 = **$146.9M**. (`tools/run.py` printed $0.03B on the pre-offering count; wrong
  by a factor of about five after 2026-09-29.)
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve, dated
  10/02/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-03-12 (0001738827-26-000013): business, risk factors,
  MD&A, the four statements; 10-Q for 2026-06-30 filed 2026-08-11 (0001738827-26-000032): statements, liquidity, risk
  factor on the rights offering, subsequent events; earlier 10-Ks for the history: FY ending 2020-01-31
  (0001558370-20-003078), FY ending 2021-01-31 (0001738827-21-000007), FY2022 (0001738827-23-000014), FY2023
  (0001738827-24-000038); 8-Ks of 2026-06-02 (Wolf Pack acquisition and debt-for-equity exchanges,
  0001738827-26-000023), 2026-08-10 (backstop agreement, rights offering, amended indenture terms,
  0001193125-26-342539), 2026-08-24 (rights offering commenced, 0001193125-26-361735), 2026-09-23 (stockholder
  protection rights plan, 0001738827-26-000051), 2026-09-25 (Q3 guidance and preliminary rights results,
  0001193125-26-402987), 2026-09-30 (rights offering closed, backstop exchange, amended and restated indenture,
  0001738827-26-000058); Schedule 13D of Steel Partners filed 2026-09-03 (0000921895-26-002473). The proxy (DEF 14A
  2026-03-26, 0001193125-26-126207) was **not read**: the file closes at Q2, before Q5 and Q6, which are the questions
  that need it.
- **One figure cross-checked against the filed statement:** FY2025 operating cash flow $7.5M, purchases of property and
  equipment $49.1M, depreciation and amortization $95.2M, as printed by `tools/run.py`, agree with the Consolidated
  Statement of Cash Flows in the 10-K FY2025 (0001738827-26-000013, page 73). Total assets $340.3M and stockholders'
  deficit $(74.2)M agree with the balance sheet (page 70).
- **`tools/run.py KLXE` arithmetic lines, checked and corrected.** The tool's owner earnings (OCF − SBC − capex, and
  OCF − SBC − D&A, three years) are right as transcriptions but **leave out two real costs this company carries**:
  finance-lease principal payments (equipment taken on finance leases, $19.9M in 2025, $21.6M in 2024) and
  paid-in-kind interest added back inside operating cash flow as "Non-cash interest expense" ($16.6M in 2025, accruing
  to note principal). It also leaves out proceeds from equipment sales, which this business receives every year. The
  recast below includes all three. CONVENTION (this run): finance-lease principal is counted as capital spending,
  because the asset is fleet equipment acquired on credit and the payment is how it is paid for; PIK interest is
  counted as a cost, because it is interest owed and added to debt; equipment-sale proceeds are credited, because they
  recur and the filing shows them every year. Rationale: Q4's "after every real cost" names no rule for either form.

**Owner cash after every real cost, by fiscal period (USD millions; transcribed from the XBRL facts of each 10-K and
checked against the filed 2025 and H1 2026 statements).** Owner cash = OCF − stock pay − capex + equipment-sale proceeds
− finance-lease principal − PIK interest.

| period | accession | OCF | stock pay | capex | sale proceeds | fin. lease principal | PIK | **owner cash** | D&A |
|---|---|---|---|---|---|---|---|---|---|
| FY to 2019-01-31 | 0001558370-19-002349 | 62.0 | 23.5 | 84.0 | 9.9 | 0.0 | 0.0 | **−35.6** | 41.5 |
| FY to 2020-01-31 | 0001558370-20-003078 | 58.1 | 18.5 | 70.8 | 0.7 | 0.0 | 0.0 | **−30.5** | 64.1 |
| FY to 2021-01-31 | 0001738827-21-000007 | −64.9 | 17.8 | 12.2 | 4.3 | 1.1 | 0.0 | **−91.7** | 61.7 |
| 11 months to 2021-12-31 | 0001738827-23-000014 | −55.6 | 3.2 | 11.0 | 15.5 | 0.5 | 0.0 | **−54.8** | 53.8 |
| 2022 | 0001738827-23-000014 | 15.7 | 3.0 | 35.6 | 16.9 | 9.7 | 0.0 | **−15.7** | 56.8 |
| 2023 | 0001738827-24-000038 | 115.6 | 3.0 | 57.1 | 16.3 | 14.6 | 0.0 | **+57.2** | 72.8 |
| 2024 | 0001738827-25-000041 | 54.2 | 3.9 | 65.1 | 14.0 | 21.6 | 0.0 | **−22.4** | 94.0 |
| 2025 | 0001738827-26-000013 | 7.5 | 2.6 | 49.1 | 16.2 | 19.9 | 16.6 | **−64.5** | 95.2 |
| H1 2026 | 0001738827-26-000032 | 10.8 | 0.9 | 17.3 | 5.6 | 11.0 | 15.0 | **−27.8** | 42.7 |

- **Five-year average (the five fiscal periods to 2025-12-31, the first of them eleven months): −$20.0M a year.** The
  depreciation variant (OCF − stock pay − D&A − PIK): −112.6, −44.1, +39.8, −43.7, −106.9; average **−$53.5M**.
- Eight periods, February 2018 to December 2025: owner cash summed **−$258.0M**. One positive year in eight (2023).
- H1 2026 excludes the $13.5M cash paid for Wolf Pack (an acquisition, not maintenance).
- `tools/run.py`'s three-year means (−$1.2M capex basis, −$31.4M D&A basis) are reproduced by the same inputs; they are
  less negative than the recast only because they omit finance leases and PIK.

### The balance sheets first, eight to ten years of them, read before the income account (**[M2025-032]**)
Done here because the file closes before Q4. Fiscal year-ends from the `tools/run.py` table (first-filed XBRL,
USD thousands converted to millions), read against the filed statements named above.

| year-end | assets | equity | cash | receivables | goodwill | intangibles | long-term debt | accumulated deficit |
|---|---|---|---|---|---|---|---|---|
| 2019-01-31 | 672.8 | 340.7 | 163.8 | 119.6 | 43.2 | 30.3 | 242.2 | −4.5 |
| 2020-01-31 | 623.4 | 312.2 | 123.5 | 79.2 | 28.3 | 45.8 | 243.0 | −100.9 |
| 2021-01-31 | 362.7 | 32.1 | 47.1 | 67.0 | 0 | 2.5 | 243.9 | −433.1 |
| 2021-12-31 | 387.7 | −51.4 | 28.0 | 103.2 | 0 | 2.2 | 274.8 | −525.3 |
| 2022-12-31 | 465.9 | −15.8 | 57.4 | 154.3 | 0 | 2.1 | 283.4 | −528.6 |
| 2023-12-31 | 539.8 | 38.8 | 112.5 | 127.0 | n/a | 1.8 | 284.3 | −509.4 |
| 2024-12-31 | 456.3 | −10.5 | 91.6 | 96.9 | n/a | 1.5 | 285.1 | −562.4 |
| 2025-12-31 | 340.3 | −74.2 | 5.7 | 102.7 | n/a | 1.1 | 253.9 | −639.5 |
| 2026-06-30 (10-Q) | 371.9 | −102.4 | 7.9 | 121.9 | n/a | 0.9 | 284.3 (+4.6 current) | −671.9 |

What the figures say. **Equity has been consumed and replaced, not earned.** From the spin (equity $340.7M at
2019-01-31, accumulated deficit −$4.5M) to mid-2026 the accumulated deficit grew by about $667M, against a peak year's
revenue of $888M. Equity went negative in 2021, briefly positive in 2023 (after the all-stock Greene's acquisition and
the one good year), and has been negative since 2024. **The goodwill and intangibles of the acquisitions are gone**:
goodwill $43.2M and intangibles $30.3M at the spin were written off in the FY to 2020-01-31 (goodwill impairment
$47.0M) and the FY to 2021-01-31 (impairments $213.9M, of which long-lived assets $141.2M and goodwill $28.3M;
0001738827-21-000007). **Debt never came down from operations:** long-term debt sat at $242M to $285M from 2019 to 2025,
refinanced in March 2025 (11.5% senior secured notes due 2025 replaced by floating-rate Cash/PIK senior secured notes
due 2030, with penny warrants, and a new ABL maturing 2028-03-07; 10-K FY2025, 0001738827-26-000013); it fell only when
shareholders and noteholders converted it to equity (2026: $2.19M exchanged for 627,521 shares in May and June; $94.0M
retired in the September rights offering and backstop exchange). **Cash fell from $163.8M to $5.7M.** Receivables
track revenue (about 59 days of 2025 revenue; 52 days in 2023): nothing out of line there. What the balance sheet
cannot say: what the fleet is worth (PP&E net $161.1M at 2025 year-end against $95.2M a year of D&A, so the book is
under two years of depreciation), and what the September recapitalization leaves: by my arithmetic, not a filed figure,
debt on the face about $194.9M after the $94.0M reduction, finance leases $31.3M (10-Q), cash about $38.9M ($7.9M plus
the $31.0M kept for general purposes), so net debt with leases about **$187.3M** and equity roughly positive $20M before
fees and Q3 results.

**Shares, split-adjusted.** About 4.0M at the spin (20.1M weighted average in the FY to 2019-01-31, accession
0001558370-19-002349, divided by the 1-for-5 reverse split of 2020); 6.5M in the FY to 2021-01-31 after the QES
all-stock merger; 18.7M weighted in 2025; **105.7M after 2026-09-29**. The per-share claim has been diluted about
twenty-six times in eight years, through an all-stock merger, an all-stock acquisition, an at-the-market program of up
to $57.8M, penny warrants to lenders, debt-for-equity exchanges and the rights offering.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the fleet and its people will earn for an owner over years, not where
$1.39 goes next. The market serves, it does not instruct: "It just tells us prices." **[M2006-077]**. The
$1.49 subscription price and a 13D filer's view that the shares were "undervalued" (Steel Partners, 0000921895-26-002473)
are prices and opinions, not facts about the business. No macro enters: "macro conclusions are — just never enter into
the discussion." **[M2000-094]**; this run does not forecast oil, gas or the rig count, which is exactly why it asks
whether the business has a position that does not depend on them. The analyst's habits: "I’m looking for what’s wrong in
things because that’s part of investing" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]** (evidence against my reading that this is a poor business,
since that is the hypothesis I formed first):
1. 2026 is improving: Q2 2026 operating income +$2.1M against −$8.7M a year earlier (though $6.5M of it is a bargain
   purchase gain on Wolf Pack); Q3 2026 revenue guided to $180M to $185M, "a 9% sequential Revenue improvement", with an
   "Adjusted EBITDA Margin range of 13% to 14%" (8-K 2026-09-25, 0001193125-26-402987).
2. The September recapitalization removed $94.0M of secured debt and the near-term covenant squeeze (leverage covenant
   reset to 4.50 from the quarter ending 2026-09-30; 8-K 0001738827-26-000058).
3. The company claims a technical niche: 39 patents and 6 pending applications, in-house R&D, services "modest in cost to
   the customer relative to other well construction expenditures but have a high cost of failure", and maintenance capex
   "lower than other oilfield service providers due to the generally asset-light nature of our services" (10-K FY2025).
4. In the good years KLXE's operating margin beat Ranger's (2022: 4.2% against 3.2%; 2023: 6.4% against 5.8%) and was
   far better than Nine's.
5. A disciplined outside holder (Steel Partners, 8.9%) bought in August 2026 at about $1.53 a share.

Contrary evidence against the business, found along the way and written down at once: the 10-Q's own sentence, "If the
Rights Offering is not completed, we may not have sufficient liquidity to meet our obligations as they become due or to
comply with the covenants in our debt instruments" (0001738827-26-000032); the 10-K's warning that failure to refinance
the ABL "could result in our auditors issuing a “going concern” or like qualification" for FY2026; the 10-K's own
statement "Historically, we believe our services generated margins superior to our competitors", which the competitor
row below contradicts in every year against RPC.

## THE STANDING RULE
A purchase for cash, unlevered, sized as a small position, puts the buyer at no risk of ruin even if the common goes to
zero in a restructuring; the rule binds the buyer's financing and size, not the target **[M2012-081]**, **[M2004-065]**.
The target's own debt is Q9's, not reached. The rule would bite only if the position were sized so that its loss
mattered: "Never risk permanent loss of capital." **[L2023-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, and the product can stay opaque if one understands "the economic dynamics
  of the industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **The business, from the filing.** KLXE rents tools and runs crews for onshore US oil and gas wells: drilling
  (directional drilling, motors), completion (coiled tubing, wireline, frac support, flowback; the largest line, $356.5M
  of $636.6M in 2025), production and intervention, from over 60 facilities in three regions, to more than 550 E&P
  customers, top five about 31% of 2025 revenue, none over 10% (10-K FY2025, 0001738827-26-000013). Revenue moves with
  customer spending, which moves with commodity prices and rig and frac activity (10-K: "Activity levels are driven
  primarily by drilling rig counts ... well completions, workover activity").
- **Key variables and whether they are foreseeable** **[M1998-044]**. Two: (a) the level of US onshore activity, and (b)
  KLXE's price and cost against its competitors at any level of activity. (a) is not foreseeable by me or by anyone in
  the filing (the 10-K calls demand "cyclical and subject to sudden and significant volatility"): it is "important but
  unknowable" **[M2006-076]**. (b) is foreseeable from the filings and the competitors' filings, and it is the variable
  that decides the castle: the economic dynamics (bid-based contracts, mobile equipment, consolidating customers, rivals
  with scale) are written in the company's own risk factors and have held through two full cycles since 2018.
- **Routing.** This is not the fast-changing-technology case the Q1 routing sends to TOO HARD; the services are decades
  old. The unforeseeable variable (a) does not need to be foreseen to answer Q2 if (b) shows on the evidence that the
  castle is open; a business whose dynamics are understood and are bad is inside the circle as a business I understand
  well enough to refuse. I judge the competitive position knowable, so Q1 passes and Q2 decides. (The other reading, that
  the earning power cannot be fixed because activity cannot be forecast, would close here TOO HARD (NATURE); see "What in
  the framework was wrong or unclear".)
- **VERDICT: IN.** The economic dynamics of the industry and KLXE's place in it can be read from the filings
  **[M2011-014]**, **[M2012-065]**; the level of the cycle cannot, and Q2 is asked on what can.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The castle tests, each with its filing fact (10-K FY2025, 0001738827-26-000013, unless noted):

- **Is it a commodity?** The filing describes one. "Price competition, equipment availability, location and suitability
  ... are all factors used by customers in awarding contracts. Our competitors are numerous ... Contracts are
  traditionally awarded on the basis of competitive bids or direct negotiations with customers." "The fact that certain
  oilfield services equipment is mobile and can be moved from one market to another ... heightens the competition."
  "Significant increases in overall market capacity have also caused active price competition and led to lower pricing
  and utilization levels." This is the rows' commodity: "the product is available from many suppliers [...] Moreover,
  most insureds don't care from whom they buy." **[L2004-003]**; "anything you do, your competitors can copy"
  **[M1996-017]**.
- **Pricing power, and the agony before a rise** **[M2005-020]**. Price follows the industry's capacity, not KLXE's
  choice. 2023 revenue rose 13.7% while activity "fell and then stabilized", the increase "driven entirely by an increase
  in weighted average price" (10-K FY2023, 0001738827-24-000038); in 2025 revenue fell 10.2%, about 16% of the fall from
  price, and in the two largest regions about 23% (10-K FY2025). The risk factor reads: "We may be unable to maintain
  existing prices or implement price increases on our services", and in high demand "our labor costs could increase at a
  greater rate than our ability to raise prices". Customers "are using their size and purchasing power to achieve
  economies of scale and pricing concessions". The rival sets the price: "he determined our profit, because we looked at
  his price every day." **[M2023-079]**; **[M2012-109]**.
- **Would the customer still choose it over the low bid?** **[M2017-009]**. The filing says contracts go by competitive
  bid. The company's best argument is the "high cost of failure" of downhole tools, the parachute argument ("if you were
  buying a parachute you’d want to take the — necessarily take the low bid" **[M2001-014]**). The record does not show
  it: if customers paid for the low failure rate, the price would hold through a downturn. It did not: lower price was
  about 15% of the 2024 revenue fall (10-K FY2024, 0001738827-25-000041) and about 16% of the 2025 fall, and going into
  2020 the company itself expected "a significant decrease in demand and prices for our services" (10-K for the FY to
  2020-01-31, 0001558370-20-003078).
- **The money test: could a well-funded attacker take it?** **[M2011-015]**. Yes, and the attackers already exist: the
  10-K names Schlumberger, Halliburton, Baker Hughes, Patterson-UTI, Liberty, RPC, ProPetro, Phoenix, STEP, Ranger, Nine,
  Scientific Drilling "and other private" companies, and says "The larger size of many of our competitors provides them
  with cost advantages as a result of their economies of scale". Coiled-tubing units, wireline trucks and rental tools
  can be bought; the rows' failing answer is the airline that "you can create" **[M2013-054]**, in an industry that is
  "just never going to have barriers to entry" **[M2012-106]**.
- **The low-cost position, the one way through a commodity field** **[L2004-007]**, **[L2000-017]**, **[M1997-010]**.
  KLXE is not the low-cost operator by its own filing (the sentence on competitors' economies of scale above) or by the
  record: its operating margin was below RPC's in every one of the eight years (competitor row). Against the
  competitor, not in absolute terms **[M2001-013]**: "It’s like comparing a copper producer whose costs are $2.50 a pound
  with a copper producer whose costs are $1 a pound." **[M2009-059]**. RPC earned a positive cumulative margin and $628.8M
  of owner cash over the span; KLXE lost money and burned cash.
- **Unit volume and share of mind.** Revenue $888.4M (2023) to $709.3M (2024) to $636.6M (2025); drilling revenue down
  29.0% in 2025; 2025's decrease about 84% volume. US rig count, as the filings state it: 779 at 2022-12-31 (10-K
  FY2022), 622 at 2023-12-31 (10-K FY2023), land rigs 527 at 2025-12-31 (10-K FY2025). KLXE's revenue rose and fell with
  the count; nothing in the filings shows share gained in a falling market.
- **The brand.** No customer asks for KLXE by name in anything I can find; the company lists "better brand name
  recognition" among its competitors' advantages.
- **Ask the competitors.** Not done in person. Their filings answer for them: the same-metric row below.
- **Widening or narrowing** **[M1999-108]** **[L2005-010]**. Narrowing on every measure the filings give: falling
  revenue, negative operating income in 2024 and 2025, equity negative, the 2025 cost of sales up to 78.8% of revenue from
  77.5% "as a result of fixed costs leverage due to lower activity", and customer consolidation ("Some of our largest
  customers have consolidated in recent years").
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: customer consolidation and
  in-sourcing (named in the 10-K), new capacity ("new well service rigs, wireline units and coiled tubing units"), and
  efficiency gains that need fewer rigs (the 10-K: oil rigs "declined through 2023 and 2024 as operators focused on
  capital discipline and efficiency gains"). Every improvement goes to the customer: "the improvement you get one day,
  your competitor gets the next day." **[M2004-053]**; "everybody in the crowd is up on tiptoes and they’re not seeing
  any better" **[M2004-054]**.

**The competitor row** (same metric, each company's own 10-K XBRL facts; KLXE's fiscal years end January 31 until 2021,
then an eleven-month period to 2021-12-31, then calendar years, so its span is February 2018 to December 2025, about
95 months against the peers' 96; owner cash here is OCF − stock pay − capex + equipment-sale proceeds for every company
alike, without the finance-lease and PIK deductions of Step 0, so KLXE is shown on the peers' basis; operating income
includes impairments for every company; source table `_research 2026-10-05 KLXE/peers/peer_table.txt`):

| company | latest 10-K accession | revenue 2018–2025 | operating income 2018–2025 | cumulative operating margin | owner cash 2018–2025 | years with operating margin above KLXE's |
|---|---|---|---|---|---|---|
| **KLXE** | 0001738827-26-000013 | $4,768.1M | −$375.2M (−$113.4M before $261.8M of impairments) | **−7.9%** (−2.4% before impairments) | **−$174.0M** | n/a |
| RPC (RES) | 0001104659-26-021480 | $10,667.4M | +$477.6M | **+4.5%** | **+$628.8M** | 8 of 8 |
| Ranger (RNGR) | 0001628280-26-015248 | $3,484.0M | +$53.2M | **+1.5%** | **+$151.6M** | 5 of 8 |
| Nine (NINE) | 0001532286-26-000005 | $4,639.3M | −$571.8M | **−12.3%** | **−$38.7M** | 2 of 8 |
| Patterson-UTI (PTEN), drilling and pressure pumping | 0000889900-26-000013 | $25,277.6M | −$2,721.3M | **−10.8%** | **+$1,780.4M** | 3 of 8 |

KLXE operating margin by year against RPC (KLXE first): 2018 4.5% / 12.2%; 2019 −13.9% / −9.3%; 2020 −108.8% / −51.8%;
2021 −14.7% / 1.9%; 2022 4.2% / 18.0%; 2023 6.4% / 15.1%; 2024 −2.2% / 6.9%; 2025 −4.8% / 2.8%. The whole industry
earns little across a cycle ("Average is going be terrible [...] average is not going to go away, either." in the row's
words of insurance **[M2000-072]**; "they beat each other’s brains out" **[M2013-052]**); within it, KLXE is below the
average of the four peers on cumulative owner cash and below the two survivors without heavy debt (RPC, Ranger) on
margin in most years. Even Patterson-UTI, with negative cumulative operating income after impairments, turned
$1.78B of owner cash; KLXE turned none.

**The strongest case for the castle, stated as well as I can** (**[M1997-127]**): niche downhole tools with patents, a
high cost of failure, a broad basin footprint, and a 13% to 14% adjusted EBITDA margin guided for Q3 2026. Against it:
the patents have not produced a price that holds in a downturn, and the company itself says it does not "regard any
single patent, license or strategic relationship as critical or essential to our business as a whole"; and adjusted
EBITDA is before $95M a year of depreciation on a fleet that must be replaced, $20M a year of finance-lease equipment and
interest, which is why eight years of positive adjusted EBITDA produced −$258.0M of owner cash.

- **VERDICT: OUT.** The castle is shown open on the evidence, not merely unjudgeable: a commodity service sold on bid
  **[L2004-003]**, priced by rivals **[M2023-079]**, open to any attacker with equipment money **[M2012-106]**, and not
  the low-cost operator, which is the way through a commodity field the rows name **[L2004-007]**, **[M1997-010]**, by
  the company's own sentence and by eight years of margins below RPC's **[M2009-059]**. A castle shown open is OUT
  **[M2011-015]**; the rows say why price cannot reopen it: "What you can’t do is turn any investment into a good deal by
  paying little" **[M2019-015]**; "marginal businesses purchased at cheap prices may be attractive as short-term
  investments, they are the wrong foundation" **[L2014-009]**. The cause is the business, not my ignorance, so the box is
  OUT and not TOO HARD **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed OUT). Facts recorded in Step 0 only: capex plus finance-lease principal exceeded operating cash
after stock pay in seven of eight periods; D&A of $95.2M against revenue of $636.6M in 2025.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 as the template asks for a file that closes before Q4. Recorded
without a verdict: the company reports "Adjusted EBITDA" as its headline (8-K 2026-09-25) and defines it to exclude
stock pay, impairments, restructuring and transaction costs; the same release says Adjusted EBITDA "is used to calculate
the Company’s leverage ratio".

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Facts recorded, not judged: interim CFO since at least August 2026 (8-K signatures, Geoffrey C. Stanford,
"Interim Chief Financial Officer"); CEO Chris Baker; the 10-K's claim of historically superior margins is contradicted by
the competitor row.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts recorded, not judged: a stockholder protection rights plan with a 10% trigger was adopted on
2026-09-23 (8-K 0001738827-26-000051), three weeks after Steel Partners filed a 13D at 8.9% (0000921895-26-002473); the
backstop parties may each own up to 30% and get board designation rights (8-K 0001193125-26-342539); the noteholders hold
a right of first offer on any debtor-in-possession financing under the amended indenture (8-K 0001738827-26-000058).

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. **COMPUTATION — NOT A CLEARANCE** (reported at the owner's request; carries no entry
language):

- **(a) VALUE RANGE per the Q7 convention: none can be built.** The convention's input is the five-year average of owner
  cash after every real cost; it is **−$20.0M a year** (depreciation variant −$53.5M). A negative base carried at any
  growth and discounted at 5.63% gives a negative value; the convention has no range for it. The rows' own words for the
  case: "if we don’t have the faintest idea what the future stream is going to look like, we don’t have the faintest idea
  what it’s worth, now." **[M1994-077]** is the cannot-value case; this is the other one, a stream that has been negative,
  and a business gets credit only "for whatever net cash is left every year" **[M1998-080]**.
- **(b) FAIR PRICE** (the price at which the central case clears about ten percent pre-tax, the CONVENTION floor of Q7):
  **none above zero.** On the five-year record no positive price earns any return at all for the owner.
- **(c) CHEAP PRICE** (below which no pencil is needed): **none.** With no positive value there is no price far enough
  below it.
- **A check at the level of the whole enterprise** (CONVENTION, this run: added because the September recapitalization
  cut the interest the five-year figure carries, and an owner may ask whether the business is worth something before
  its debt; rationale: the equity's value is what the enterprise is worth less what it owes). Adding back interest paid
  in cash and in kind (30.5, 33.7, 35.0, 37.1, 44.4; average $36.1M) gives unlevered owner cash of about **+$16.1M a
  year**. At the price, the enterprise costs about $334.2M ($146.9M equity plus about $187.3M net debt with leases, Step
  0, my arithmetic). $16.1M on $334.2M is **4.8%**, below the 5.63% bond and about half the ten-percent floor. Valued at
  ten percent, the enterprise is worth about $161M, less than its net debt: **the equity's value at the floor is below
  zero, about −$26M, or about −$0.25 a share.** The best single year (2023, owner cash +$57.2M, unlevered about +$92M) is
  a cyclical peak and is not used as a base.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED. (On the computation above, the 30-year Treasury at 5.63% beats the enterprise's unlevered yield at the
price.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts recorded: after September 2026, about $195M of secured debt on the face (my arithmetic), floating-rate
Cash/PIK notes due 2030 with mandatory quarterly redemptions of 2% a year, an ABL due 2028-03-07, a leverage covenant of
4.50 stepping to 3.00 by mid-2029, and the 10-K's own going-concern warning tied to the ABL refinancing.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked (closed at Q2).

---
## THE BOX
**OUT at Q2.** A commodity oilfield service sold on bid, priced by its rivals, not the low-cost operator by its own
filing and by eight years of margins below RPC's; owner cash after every real cost −$20.0M a year over five years and
−$258.0M over eight periods; no value range can be built at $1.39 (COMPUTATION: the equity is worth less than zero at the
ten-percent floor even before its debt costs are counted in the cash). Not TOO HARD: the deciding question was knowable
and answered from the filings.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (template copied, then `tools/run.py` and EDGAR). **Not** written and
      committed question by question: the file was filled in one pass after the reading, and **nothing was committed**,
      because this assignment forbids commits. The write-early rule was not met.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact carries its
      accession; numbers without a filing are labelled "my arithmetic" or CONVENTION.
- [x] The order was kept; Q2 closed the run OUT; Q3 to Q10 are NOT REACHED; the Q7 figures are headed COMPUTATION — NOT A
      CLEARANCE and carry no entry language.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5), and stricter than the tool's (finance
      leases and PIK deducted, confessed as a CONVENTION of this run); the sovereign from the US Treasury; aggregator
      quotes flagged.
- [x] Contrary evidence written down as it was found **[M1997-127]**, both for and against the business.
- [x] Not a point-in-time run; no anchor date issue.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two of them (share basis, market cap) were found stale
      and replaced.
- [x] `python tools/check_framework.py` PASS before finishing (no commit made; see the reply).
- Proxy not read (Q5/Q6 not reached). The 2018 spin-off 10-K and the QES merger documents were not read beyond the XBRL
  figures and the later 10-Ks' narrative.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a cyclical commodity.** The routing paragraph sends a business to Q1 TOO HARD when its industry
changes fast; it is silent on a business whose dominant variable (the oil and gas activity level) is "important but
unknowable" **[M2006-076]** while its competitive position is plainly knowable. Read strictly, test 4 could close KLXE at
Q1 TOO HARD (NATURE); I passed Q1 on **[M2011-014]** ("the economic dynamics of the industry") and closed at Q2 OUT on the
evidence. Two analysts could split OUT against TOO HARD (NATURE) on the same facts; the action is the same, the box is
not. A sentence saying that an unforecastable cycle does not by itself close Q1 when the castle question can be answered
without it would settle it. (2) **"After every real cost" does not say how to treat finance-lease principal and
paid-in-kind interest**, both material here ($19.9M and $16.6M in 2025 against $7.5M of operating cash flow), and
`tools/run.py` omits both, so the tool's owner earnings flatter this company by about $36M in 2025. I deducted both and
confessed it. (3) **The share count after a capital event between the last periodic filing and the run date.** The
template asks for the filed cover count; the 8-K of 2026-09-30 gives a count five times larger. I used the 8-K count; the
template and `Screens/cover_shares.py` should say that a later 8-K or prospectus count governs. (4) **The owner's three
reporting figures (range, fair, cheap) have no defined form when owner cash is negative**; I reported "none" and added an
enterprise-level check as a CONVENTION of this run, which another analyst might not add. (5) **"Another way" in
[L2004-007]**: the row names NICO's "ebb-and-flow business model" as a route through a commodity field other than low
cost, and the framework carries it as OPEN without saying what it is; a cyclical service business could be argued into
it. I found no evidence KLXE follows any such model (it kept its debt and fleet through every trough), but the framework
gives no test to apply.
