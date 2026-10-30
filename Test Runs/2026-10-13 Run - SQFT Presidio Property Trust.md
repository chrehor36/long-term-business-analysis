# Company Run — Presidio Property Trust, Inc. (Nasdaq: SQFT) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (SQFT; also searched for Presidio and NetREIT); not held.*

**Dispatched run.** Written by a dispatched analyst under the brief of 2026-10-13, which departs from
`Screens/_daily/_dispatch_brief.md` in one stated place: the lines of evidence were derived by the analyst from the FY2025
10-K's Item 1, Item 1A and Item 7 (below, Step 0), not supplied by hand. Working folder:
`Test Runs/_research 2026-10-13 SQFT/` (notes, fetch and check scripts, tool outputs; raw filings in its gitignored cache).

**Contamination, declared.** Seen by accident and not used: the session's opening git status and recent commit subjects
(a fold and run commits for another company, MSM, and the names of other research folders, AYI and ARCB); the memory index
line on the queue state (counts of earlier gate-clearers, no names). Nothing seen concerns this company under any name
(SQFT, Presidio, NetREIT). No `Test Runs/` file other than the template and this file was opened, listed by name for this
company, or searched; `PORTFOLIO.md`, holding reviews, the register, the resume-state file and the prepped reading list were
not opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.859 a common share (close 2026-10-12; Yahoo chart endpoint through `tools/sources.py`, an aggregator,
  permitted for the live quote only and flagged per operator rule 5). The common closed $1.18 on 2026-10-02, the day the
  exchange offer expired, and fell to $0.94 on 2026-10-06, the settlement date, and to $0.84 on 2026-10-07 (same source).
  The price is below Nasdaq's $1.00 minimum bid; the exchange prospectus carries the delisting risk (424B3 of 2026-09-02,
  `0001493152-26-041167`). The 9.375% Series D preferred closed $6.15 (same source, same date), against a $25.00
  liquidation preference.
- **Shares by class.** `python Screens/cover_shares.py SQFT`: 1,434,432 Series A common, single class, from the 10-Q for
  2026-06-30 filed 2026-08-13 (`0001437749-26-027591`), cover as of 2026-08-13. Checked three ways:
  (1) the 10-Q balance sheet shows 1,316,939 issued and outstanding at 2026-06-30; the prospectus explains the gap: the
  1,434,432 "includes 117,493 shares of unvested stock" (424B3, `0001493152-26-041167`), so the cover count is the full
  count; (2) **split**: one split only in the price history, a 1-for-10 reverse split effective 2025-05-19 (8-K of
  2025-05-16, items 3.03 and 5.03, `0001641172-25-011284`); the 10-K says all share figures are restated for it
  (`0001437749-26-010114`), and the 10-Q count is post-split, so no factor applies; (3) **issuance after the 10-Q**: the
  exchange offer expired 2026-10-02 with 149,773 of 973,736 Series D shares tendered (about 15.4%), for "an aggregate of
  823,753 shares of Common Stock", settlement "on or about October 6, 2026" (Schedule TO-I/A No. 3, 2026-10-05,
  `0001493152-26-045707`; 8-K of 2026-10-05, `0001493152-26-045704`). An at-the-market sales agreement for up to
  $1,419,265 of common was signed 2025-10-14 (8-K `0001493152-25-018016`); no ATM sale after 2026-08-13 is stated in a
  filing read. **Count used: 1,434,432 + 823,753 = 2,258,185 common shares.** Series D preferred remaining:
  973,736 - 149,773 = 823,963 shares. Series A warrants (exercise $7.00 pre-split terms, SQFTW) are out of the money and
  are left out, said so.
- **Market cap:** $0.859 x 2,258,185 = **$1.94M** (common only).
- **Sovereign for the earnings currency (USD):** **5.60%**, the 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-09 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025 filed 2026-03-27 (`0001437749-26-010114`): Items 1, 1A, 2, 7, the
  statements and notes 4, 7, 13 (segments); 10-Q for 2026-06-30 filed 2026-08-13 (`0001437749-26-027591`): statements,
  mortgage note, subsequent events; DEF 14A filed 2026-04-21 (`0001493152-26-018340`): pay-versus-performance table,
  related parties, auditor changes; 8-Ks of 2025-05-16, 2025-10-14, 2026-01-23 (`0001493152-26-003424`, default notice),
  2026-01-28 (`0001493152-26-004044`, preferred dividend suspended), 2026-02-18 (`0001493152-26-007357`, receiver),
  2026-09-02 (`0001493152-26-041173`), 2026-10-05; the exchange prospectus (424B3 of 2026-09-02); the 10-Ks for FY2017
  (`0001564590-18-006319`), FY2019 (`0001080657-20-000013`), FY2021 (`0001437749-22-007590`) and FY2023
  (`0001437749-24-012113`) for the balance sheets, cash flows and occupancy of the span.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $417,870 in
  the filed cash flow statement of the FY2025 10-K, equal to the XBRL fact (same accession). A second check found a
  difference: FY2023 operating cash is $1,489,839 in the FY2023 10-K as filed and $1,448,573 in the XBRL of the next
  10-K (a reclassification in the comparative year, not explained in the text read); the run uses the as-filed figure.
- `python tools/run.py SQFT` printed one line: "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." No arithmetic
  line was produced; every figure below was taken from the filed statements by the analyst (scripts in the research folder,
  `xbrl_flows.txt`, `q7_computation.py`).

**The lines of evidence this name needs, derived from the FY2025 10-K and why.** Item 1 describes two businesses (nine
office and industrial buildings plus one retail centre in Colorado, North Dakota, California, Maryland and Texas; 80 model
homes bought from builders and leased back triple-net, "approximately 69% of our model homes are leased to one
homebuilder"), a capital structure of property mortgages and a 9.375% preferred, and a dividend suspended. Item 1A names
as risks office demand ("Work from home, flexible work schedules [...] could, over time, erode the overall demand for office
space"), competition for tenants that sets rents, refinancing and default, the preferred, and Nasdaq listing. Item 7 shows
revenue falling with sales and a loss of about $4.0M of revenue expected from "the sale of Dakota Center and the loss of
Shea Center II". The lines chosen: (1) occupancy and rent of the office and industrial part over the span, since it carries
most of the net operating income in every year read; (2) what competitors' pricing does to rent, from the filer's own Item
1 and 1A and two office REITs' filings; (3) the properties lost to lenders and the impairments, as the direct evidence of the
castle; (4) the model-home part's economics and concentration; (5) the debt, the maturities and the preferred, for Q9 and
the standing rule; (6) the uses of money (the SPAC, buybacks, tender, exchange) for Q6, written under AFTER THE STOP if a
STOP closes earlier.

**The balance sheets, read in Step 0 in case the file closes before Q4** **[M2025-032]** (filed statements, accessions above;
dollars in millions; equity is stockholders' equity before noncontrolling interest):

| Dec 31 | Total assets | Real estate, net | Cash incl. restricted | Mortgage notes, net | Other notes | Series B pref (liability) | Equity | Accumulated "dividends and losses" |
|---|---|---|---|---|---|---|---|---|
| 2016 | 258.0 | 240.5 | 7.4 | 158.9 | 0 | 32.1 | 43.1 | -106.6 |
| 2017 | 254.5 | 234.5 | 8.3 | 160.3 | 0 | 30.6 | 37.6 | -113.7 |
| 2018 | 233.1 | 211.1 | 9.8 | 149.7 | 0 | 16.8 | 40.4 | -111.3 |
| 2019 | 220.8 | 200.2 | 10.4 | 142.4 | 12.2 | 0 | 39.2 | -113.0 |
| 2020 | 185.6 | 166.3 | 11.5 | 120.0 | 7.5 | 0 | 34.9 | -121.7 |
| 2021 | 161.2 | 138.1 | 14.7 | 88.9 | 0 | 0 | 55.7 | -130.9 |
| 2022 | 291.4 (incl. SPAC trust 136.9) | 130.5 | 16.5 | 96.9 | 0 | 0 | 43.8 | -138.3 |
| 2023 | 176.0 (incl. Conduit stock 18.3) | 144.2 | 6.5 | 107.7 | 0 | 0 | 50.9 | -131.5 |
| 2024 | 142.6 | 127.6 | 8.0 | 102.1 | 0 | 0 | 26.5 | -159.4 |
| 2025 | 122.1 | 108.6 | 7.4 | 92.1 | 0 | 0 | 16.8 | -169.9 |
| 2026-06-30 (10-Q) | 106.7 | 95.0 | 5.9 | 80.1 | 0 | 0 | 13.9 | -173.3 |

What moved, and what the figures say. The asset base has shrunk by more than half (real estate $240.5M to $95.0M) by sales
and, from 2024, by surrender to lenders; the debt has fallen with it but not faster (mortgages 62% of total assets in 2016,
75% at 2026-06-30). Equity before minority interests is $13.9M at 2026-06-30 against $20.6M of preferred liquidation
preference still outstanding after the exchange, so the common's book equity, after the preferred, is below zero. The
accumulated deficit grew from $106.6M to $173.3M: the dividends paid were not earned. Equity rose only when capital was
raised (2021: common and $20.5M of preferred, `0001437749-22-007590`). Goodwill is small ($2.4M to $1.3M, written down
2023 to 2025). The 2022 and 2023 columns carry a special-purpose acquisition company the company sponsored (trust of
$136.9M, consolidated, then deconsolidated in 2023 into Conduit Pharmaceuticals stock carried at $18.3M; that stock was
carried at $3,900 at 2025 year-end against a cost basis of about $7.5M, 10-K Item 7). Cash at the parent is thin:
"Cash, cash equivalents and restricted cash" in corporate and other was $173,621 at 2025 year-end (note 13), and the
receiver's lender holds about $2.4M of the restricted cash (10-Q note 7). What the figures cannot say: the market value of
the buildings; the impairments say the book has been above it at Dakota Center and Shea Center II.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what these buildings and leases will pay their owners, not what the
next buyer pays for a $0.86 share. The market serves, it does not instruct **[M2006-077]**: a fall from $1.18 to $0.86 in
the week the exchange settled tells nothing about value by itself. No macro forecast enters **[M2000-094]**: Item 7 of the
10-K opens with brokers' 2026 outlooks (Morgan Stanley, Colliers, JP Morgan, Nareit, CBRE) and an expectation of rate
cuts; none of it is used. Who is paid to tell you **[M2020-037]**: the exchange offer's terms were set by the issuer, which
benefits from retiring a 9.375% cumulative claim with stock. Margin of safety **[M1996-084]**: if this needs a pencil, it is
too close. **Contrary evidence, written down as found** **[M1997-127]**: (1) the office part has been sold down and two
buildings lost to lenders, which could be read as cleansing the weak assets, leaving a smaller, better-occupied core
(Arapahoe 100%, Baltimore 100%, West Fargo Industrial 96.5%, Genesis 100% at 2025, 10-K Item 2); (2) model homes are
leased triple-net to builders with gains on resale each year ($3.4M in 2024, $1.0M in 2025), a business with a cash yield
that is not office; (3) the exchange retired about 15% of a cumulative 9.375% claim. Each is weighed where it bears.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if it is bought with the buyer's own money and sized so that a total
loss can be borne: "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"Never risk permanent loss of capital." **[L2023-005]**. The target's own leverage and the junior place of the common are
weighed at Q9, not here. Borrowing to buy it would breach the rule outright **[M2004-065]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**. The product is plain: space in mid-size office
  and industrial buildings let on three-to-five-year leases with annual increases, and model homes bought from builders and
  leased back for two to three years, then sold as houses (10-K Item 7). The economics are rent less property costs,
  corporate cost and interest, plus or minus what the buildings fetch when sold. "What is important is that I understand
  the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**:
  for this industry those dynamics can be read from the filings (below, Q2).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) occupancy and market rent in the office
  buildings in suburban Denver, Colorado Springs, Fargo, Bismarck, San Diego and Baltimore; (2) the cost and availability of
  mortgage refinancing at each maturity; (3) builders' demand for model-home leasebacks and the resale price of the homes.
  None depends on a technology the filer cannot describe. The first is the forecast that matters; the filer itself states
  its direction (office demand may "erode", 10-K Item 1A) and quantifies the next year ("a decrease of revenue of
  approximately $4.0 million", Item 7).
- **Do the past statements tell me the future ones?** **[M2008-033]** In direction, yes: the ten years read show the same
  pattern repeated (sales, losses, impairments, refinancing at higher coupons: Grand Pacific 6.35%, West Fargo 7.14%,
  Arapahoe 6.75%, One Park 6.83%, against 4.92% on the Shea loan of 2015; 10-Q note 8). In level, the portfolio changes
  every year, which makes the numbers fragile but not opaque.
- **Is it important and knowable?** **[M2006-076]** The deciding question, whether the office buildings hold their tenants
  at rents that cover their costs, is important and is answered by the filer's and its rivals' filings.
- **Routing.** This is not a business whose ten-year economics are out of reach because its industry changes fast; the
  shift in office demand is a change in the customer's need for the product, and the filings show its effect year by year.
  It is not a bank or a holding company; it is a business of parts (office and industrial, model homes, retail), read by
  parts at Q2.
- **Doubt** **[M2002-092]**: I do not doubt that I understand what this business does and how its money is made; the doubt
  is about whether it is a good business, which is Q2's question, not Q1's.
- **VERDICT: IN.** The economics are simple and foreseeable in kind **[M2012-065]**, **[M2011-014]**; the filer's statements
  tell the future statements in direction **[M2008-033]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**.

**The parts table** (business of parts, section B; "lumping them together, as is done in standard financial statements,
impedes analysis" **[L2008-005]**). The filer reports three segments with different economics (note 13). The filer's own
risk factor gives the office share of net operating income every year of the five-year window: "approximately 59%" (2021,
FY2021 10-K `0001437749-22-007590`), "approximately 63%" (2022) and "54%" (2023) (FY2023 10-K `0001437749-24-012113`),
"approximately 65%" (2024) and "58%" (2025) (FY2025 10-K `0001437749-26-010114`). Net operating income is before
corporate cost, depreciation and interest; it is the only segment profit the filer reports, and it is used as the
operating-profit measure, said so.

| Part | Share of five-year segment NOI | Castle (below) | Decides |
|---|---|---|---|
| Office and industrial (nine buildings at 2025; seven after Dakota Center and Shea Center II) | more than half in each of 2021 to 2025 (54% to 65%) | open | **yes**, more than half |
| Model homes (80 at 2025, 71 at 2026-06-30) | the larger part of the rest (2025 NOI $3.7M of $10.0M segment NOI) | not shown to stand; carried | no |
| Retail (one centre after 2025) | small ($0.4M of NOI in 2025) | not read | no |

**The castle tests, applied to the deciding part.**
- **The attacker with money** **[M2011-015]**. The filer answers it: "Many of these competitors have substantially greater
  financial resources than we do and may be able to accept more risk than we can prudently manage [...] many of these
  competitors have capital structures that allow them to make investments at higher prices than what we can prudently
  offer" (10-K Item 1, Competition). Anyone with capital can build or buy a suburban office building in Denver or Fargo;
  "there are some industries that are just never going to have barriers to entry" **[M2012-106]**. Fails.
- **Pricing power, and who sets the price.** The filer, again: "If our competitors offer space at rental rates below
  current market rates, or below the rental rates we currently charge our tenants, we may lose potential tenants and we may
  be pressured to reduce our rental rates below those we currently charge or to offer more substantial rent abatements,
  tenant improvements, early termination rights or below-market renewal options" (Item 1; the same in Item 1A). That is
  the business whose price a competitor sets: "whatever he charged for gas was my price." **[M2012-109]**; **[M2023-079]**.
  Fails.
- **Would the customer still choose it over the low bid** **[M2017-009]**. A tenant choosing among buildings in the same
  submarket buys on location, rent and concessions (Item 1A lists "the attractiveness of our properties as compared to our
  competitors’ properties based on considerations such as location, rental rates, amenities and safety record"); nothing in
  the filings shows a tenant paying more to be in these buildings. This is the commodity mark, the customer who does not
  care from whom he buys **[L2004-003]**. Fails.
- **Unit volume and share of mind.** Occupancy of the office and industrial part as filed (Item 2, each year's 10-K):
  88.1% (2017), 83.3% (2019), 82.8% (2021), 81.0% (2023), 82.1% (2025). The portfolio was sold down from 1,463,390 square
  feet (2017) to 758,175 (2025) while occupancy fell, so the buildings kept were not the better-let ones on the whole.
- **The low-cost position.** None claimed or shown. Corporate general and administrative cost was $5.7M in 2025 and $7.5M
  in 2024 against total NOI of $10.7M and $12.7M (note 13): more than half of what the buildings earn is spent at head
  office before depreciation and interest. Fails.
- **Widening or narrowing** **[M1999-108]**: "how wide the moat is and whether it’s likely to widen further or shrink on
  you". Narrowing, on the filings. Shea Center II (Highlands Ranch, Colorado, bought 2015 for $25.3M to $26.0M as the
  10-Ks state it): 92.8% occupied (2017), 90.9% (2019), 71.5% (2025); low occupancy "triggered a cash management event"
  under the loan; default notice 2026-01-21 (8-K `0001493152-26-003424`); receiver 2026-02-13 (8-K `0001493152-26-007357`);
  foreclosed 2026-07-01 to the lender's nominee on "a minimum credit bid valued at $12.0 million, and no cash consideration
  was exchanged" (10-Q `0001437749-26-027591`, note 16). Dakota Center (Fargo, bought 2011 for $9.6M): 46.1% occupied,
  loan matured 2024 unpaid, sold 2026-01-14 for $5.125M with the lender taking the proceeds "in full satisfaction" (10-Q,
  note 4). Impairments of real estate in 2020, 2021 and 2023 to 2026 (2025: $6.4M; first half 2026: $3.5M). Two of the nine
  office and industrial buildings held at 2025 were surrendered to lenders within seven months.
- **What could destroy it, five to fifteen years out** **[M2000-014]**: the filer names it, office demand eroded by work from
  home and shared space (Item 1A), with "approximately 58% of our net operating income" from office in 2025.
- **Ask the competitors.** No competitor named by the filer (below); not possible from the record.

**The competitor row.** The 10-K names no rival by name: it says "other REITs, pension funds, insurance companies,
investment funds and companies, partnerships and developers" (Item 1). Comparison chosen by the analyst, and how: two
SEC-filing office REITs that own office buildings in the Denver market, where Shea Center II, One Park Centre and Arapahoe
Center sit (the Colorado buildings carried 41.3% of the 2025 base rent, Item 2): Franklin Street Properties (FSP; "Denver,
Colorado — 44.5%" of its square footage, FY2025 10-K `0001104659-26-025284`) and City Office REIT (CIO; office in "Dallas,
Denver, Orlando, Phoenix, Portland, Raleigh, San Diego, Seattle and Tampa", FY2024 10-K `0000950170-25-023714`). Neither is a
named rival; the North Dakota, Maryland and model-home markets have no comparison here. Figures from each company's
filed XBRL facts (research folder `competitors_xbrl.txt`), the leased rates from the 10-K text.

| Metric | SQFT | FSP | CIO |
|---|---|---|---|
| Revenue, first year read to last | $33.4M (2017) to $16.8M (2025) | $272.6M (2017) to $107.2M (2025) | $106.5M (2017) to $171.1M (2024), grown by purchase |
| Leased or occupied, office | 88.1% (2017) to 82.1% (2025) | 89.7% (2017) to 68.9% (2025) | 85.4% (2024); earlier years not read |
| Net income, the span | loss in 10 of 12 years 2014 to 2025; the two profits (2018, 2023) came from sales gains ($12.2M) and a SPAC deconsolidation gain ($40.3M) | +$8.4M (2016) to -$45.0M (2025); losses 2023 to 2025 ($48.1M, $52.7M, $45.0M) | small profits 2017 to 2020; 2021 +$484.4M; losses 2023, 2024 |
| Operating cash | $5.6M (2017) to $0.4M (2025) | $95.9M (2017) to $3.8M (2025) | $36.6M (2017) to $58.9M (2024) |
| Real estate impairments | 2020, 2021, 2023 to 2026 | not tagged in XBRL | $13.4M (2022), $8.5M (2024) |
| End of the span | buildings surrendered to lenders, preferred dividend suspended | shrinking by sales | agreed to be taken private (DEFM14A 2025-09-08), delisted (Form 25, 2026-01-09) |

**The field's returns over the last full cycle**, judged in words (section C; no figure). The span 2016 to 2025 runs through
the 2020 shock and the office downturn after it. Across it the filer and the larger rival lost money in most of the later
years, saw occupancy and operating cash fall, and sold or surrendered buildings to meet their debts; the other rival grew
by purchase, booked its one large profit in a single year (2021) and left the public market. These are not durable castles
protecting excellent returns; the moat is what "protects excellent returns on invested capital" **[L2007-004]**, and this is
a field in which "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. Where this
business stands inside its field: below it, on head-office cost and on the two buildings lost.

**The model-home part, carried and not deciding.** Sale-leasebacks to builders, "approximately 69% of our model homes are
leased to one homebuilder" (Item 1); Item 1A: "There are a limited number of model homes and competition to buy these
properties may be significant"; resale prices below expectation, "the builder changing their model style after we
purchased the homes" (10-Q note 4). No castle is shown for it; under section B it would be carried to Q7 as an ordinary
business at no growth, and it does not decide.

- A castle shown open on the evidence closes OUT **[M2011-015]**: the attacker with money, the price set by the competitor,
  the customer on the low bid, and the moat narrowing, each answered against the deciding part from the filer's own words
  and filings. The castle's future is not unknowable; the filings show it. A lower price does not reopen it: "What you can’t
  do is turn any investment into a good deal by paying little" **[M2019-015]**; "If you really think a business is
  declining, most of the time you should avoid it." **[M2012-062]**.
- **VERDICT: OUT.** The deciding part's castle is shown open on the evidence **[M2011-015]**, **[M2012-109]**,
  **[M1999-108]**, and the field protects only ordinary returns or worse over the full cycle **[L2007-004]**, **[M2013-052]**;
  the box is OUT among "in, out, and too hard" **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed OUT at Q2). Facts for it are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 **[M2025-032]**; facts for Q4 are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts, with the buyback prices set against the computed range, are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures are computed beneath the stop (COMPUTATION, NOT A CLEARANCE,
below).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Nothing found that resembles the businesses Q12 names.

---
## THE BOX
**OUT at Q2** (the castle): the deciding part, the office and industrial buildings, is a business whose rents its competitors
set, open to any attacker with capital, narrowing on the filings (two of nine buildings surrendered to lenders in 2026), in a
field whose returns over the full cycle were ordinary or worse. **Integrity facts recorded, not judged.** Beneath the stop,
COMPUTATION, NOT A CLEARANCE: no case of the range values the common above zero after the debt, against a price of $0.859.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**. Facts that bear on integrity are
flagged, so that any later run that reaches Q5 answers them **[M2013-088]**.

**Q3, capital in and what it earns.** Segment NOI was $10.7M (2025) on real estate carried at $108.6M; after corporate cost
($5.7M) and depreciation ($4.9M) the result before interest and impairments is about nil (note 13, statements). Building
additions and tenant improvements ran $1.6M to $6.7M a year 2021 to 2025, against depreciation of $4.9M to $5.5M (cash flow
statements). Model homes are bought with about 70% mortgage debt (2025: $9.4M bought, $6.6M of it in notes, Item 1).
Refinancing has moved coupons from 4.67% and 4.92% to 6.35%, 6.75%, 6.83% and 7.14% (10-Q note 8).

**Q4, the accounts.** Operating cash $2.4M (2021), $0.9M (2022), $1.5M (2023), -$0.7M (2024), $0.4M (2025), against
preferred dividends of about $2.1M to $2.3M a year paid until January 2026, and common dividends paid until 2023 (cash flow
statements). The proxy's pay-versus-performance table names "Core FFO" (-$2.70M in 2025, -$1.42M in 2024, -$0.90M in 2023)
as "the most important financial performance measure" linking pay to performance (DEF 14A `0001493152-26-018340`): an
adjusted figure, here negative. Material weaknesses in internal control were disclosed for the Conduit stock received in the
de-SPAC and for the income tax provision; the auditor was dismissed in August 2024 (Baker Tilly, replaced by Moss Adams), and
an 8-K with item 4.01 (change of auditor) was filed again on 2025-06-05 (`0001641172-25-013845`, item list only, not read).
The FY2023 operating cash differs between the FY2023 10-K as filed ($1,489,839) and the comparative in the next 10-K's XBRL
($1,448,573), unexplained in the text read.

**Q5, integrity facts (recorded, not judged).** (1) The company sponsored a special-purpose acquisition company (Murphy Canyon
Acquisition Corp.; trust of $136.9M consolidated at 2022 year-end; deconsolidated in 2023 into Conduit Pharmaceuticals
stock): the stock was carried at $18.3M at 2023 year-end, lost $17.9M in 2024, and was carried at $3,900 at 2025 year-end
against a cost basis of about $7.5M (statements; Item 7). (2) The company leases part of its headquarters to Puppy Toes,
Inc., "a company owned by the Chief Executive Officer and his wife", and to Centurion Counsel, Inc., which Puppy Toes owns,
and is reimbursed at cost for employee services to them; it paid a former director and president of its advisors, the
father-in-law of a sitting director, consulting fees of $191,250 (2024) and $50,000 (2025) (DEF 14A, related parties).
(3) The chief executive is also chairman and president (10-K Item 1). (4) The 10-K justified buybacks by "significant embedded
value in our assets that is yet to be realized by the market" (Item 1) in the years the buildings were impaired and
surrendered. (5) Chief executive pay as reported $613,497 (2025), $747,031 (2024), $698,221 (2023), while the proxy's value of
a $100 initial investment fell to $41.89 (DEF 14A).

**Q6, the money and the owners.** Buybacks in 2025: 16,080 common at an average $4.79, a fixed-price tender for 214,412 common
at $6.80 (about $1.46M), and 23,346 preferred at an average $14.76 (Item 1). The programme named no price above which it
would stop; against the computed range below, where no case values a common share above zero, every price paid sits above
the bottom of the range, which is the test the convention sets **[L2016-002]**. Issuance: $1.67M of common sold in 2025
(cash flow statement; ATM agreement of 2025-10-14); 109,054 preferred sold in 2024 at $16.00 against a $25.00 preference
(Item 1); 86,232 common issued in 2024 for a minority interest in Genesis Plaza (Item 2); the exchange of 2026 issued 823,753
common (57% of the 1,434,432 then outstanding) for 149,773 preferred, 5.5 common for each $25.00 preferred, whose tendering
holders gave up their share of "$1,331,263 accumulated and unpaid dividends" on the class at 2026-07-31 (424B3). Common
dividends 2014 to 2023 exceeded earnings (the accumulated deficit, Step 0). A 1-for-10 reverse split in 2025 (Step 0).

**Q9, debt and exposures.** Mortgage principal $80.9M at 2026-06-30 (10-Q note 8), of which the Shea Center II loan of $16.4M
was extinguished by the foreclosure of 2026-07-01; model-home notes $22.5M maturing 2026 to 2030, one lender's notes carrying
a fixed-charge cover of 1.10 times and a $200,000 liquidity covenant; "$22.6 million of our total debt contained recourse to
the Company" at 2025 year-end (Item 1). Two non-recourse loans went unpaid at maturity (Dakota Center 2024, Shea Center II
2026). Preferred dividends suspended from the January 2026 payment and accruing (8-K `0001493152-26-004044`); eighteen
missed monthly dividends give the preferred holders two board seats (Item 1). The common trades below Nasdaq's $1.00 minimum
bid (Step 0). The filer says it will turn to "real estate sales, from sales of equity or debt securities" if operating cash
falls short (Item 1). Against the acquisition criteria's "little or no debt" **[R1997-001]**, this is the opposite case.

### COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures; Q7's construction; a reporting convention)
Script and output: `Test Runs/_research 2026-10-13 SQFT/q7_computation.py` and `q7_computation_output.txt`.

- **Owner cash** (operating cash less building additions, tenant improvements and leasing costs, from the filed cash flow
  statements; the REIT pays almost no company tax, income taxes paid $78,848 in 2025, so the company's tax is already inside
  the figure): equity-only, after interest, 2021 $0.66M, 2022 -$1.25M, 2023 -$5.17M, 2024 -$3.00M, 2025 -$2.29M,
  **five-year average -$2.21M**; all-equity, interest paid added back, $5.08M, $2.86M, -$0.20M, $2.37M, $3.62M,
  **five-year average $2.75M**. Distributions to minority partners ($1.3M to $7.6M a year) are not deducted in either;
  deducting them makes every year negative on the equity-only basis. The window is the literal one and is generous: it
  includes buildings sold in 2025 and lost in 2026, which the filer expects to take about $4.0M of revenue with them (Item 7).
  Specific (a) is not applied, since the change is a shrinking portfolio, not a cycle; said so.
- **Growth.** The all-equity series changes sign (2023), so by specific (b) growth is measured between the halves: the average
  of 2021 and 2022, $3.97M, to the average of 2024 and 2025, $3.00M: **-9.0% a year**, carried as the bottom; no growth is the
  top. Specific (c): model-home purchases are financed mostly by their own mortgages and recycled through sales; they are
  left out of owner cash, with the model-home gains, and said so. Specific (e): no maintenance split is possible from the
  filing; all building spending is charged.
- **Range, all-equity, at the 5.60% Treasury, ten years, then zero nominal growth:** enterprise value $24.4M (decline) to
  $49.0M (no growth). Net debt $61.0M: mortgage principal $80.86M less cash $5.90M at 2026-06-30, less the Shea Center II loan
  of $16.35M extinguished on 2026-07-01, plus the about $2.4M of restricted cash the lender kept (the subsequent event the 10-Q
  states). **Value range: -$16.23 to -$5.29 a common share** on 2,258,185 shares, **against $0.859.** The price is above the
  top of the range; no case earns the floor, which is tested first and closes OUT whatever the width **[M2003-149]**.
- **CONVENTION, ours, of this run:** the preferred's liquidation preference ($20.60M on 823,963 shares), its arrears (about
  $1.45M by 2026-09-30) and the noncontrolling interest at book ($7.57M) rank ahead of the common and are deducted in a figure
  shown beside the central one; rationale: Q7's text deducts net debt only, and a common share behind a senior perpetual
  preferred ten times the common's market value is not worth the enterprise less the debt. With them: -$29.34 to -$18.41 a
  common share.
- **Equity-only basis:** average owner cash after interest is negative, so every case values the common below zero.
- **Fair price** (each end case valued at ten percent, the two averaged; Part VII): enterprise $27.5M (no growth) and $15.3M
  (decline), average $21.4M, less net debt $61.0M: **below zero (-$17.54 a common share) on the all-equity basis; below zero
  on the equity-only basis.** No positive price earns the floor, against $0.859.
- What would change it: only a sale of the buildings at prices well above the 2026 outcomes (the two buildings that left in
  2026 went for about half what was paid for them); that is a bet on liquidation values, which Q7 does not value.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Commits: the template copy; Step 0 to Q1; Q2; the close.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session; the run is folded into the register before the dispatcher moves on (operator rule ten). A run not in the
      register binds nothing. (The lock and the fold are the dispatcher's; not checked by the analyst.)
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); anything of
      them seen by accident is declared under contamination, not used. Declared as well: before the copy, one listing of
      `Test Runs/` filtered for this company's names (sqft, presidio, netreit) was run, to avoid overwriting an existing file;
      it returned nothing.
- [x] Every v5 id resolves (checked by script, `idcheck.py` in the research folder); every filing fact has its accession; no
      number without a row or a filing.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**; the facts found for later questions are under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII). Not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); it produced none ("UNRESEARCHED", no overlapping
      facts), and every figure was taken from the filed statements.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q7's construction deducts net debt only and says nothing of a perpetual cumulative preferred or of minority interests in
consolidated partnerships. Here the preferred's preference is about ten times the common's market value and ranks ahead of
it; a literal reading would value the common as if it did not exist. I confessed a CONVENTION of this run (both deducted,
shown beside the central figure); a rule is needed. (2) The business-of-parts threshold speaks of "five-year operating
profit"; a REIT reports segment NOI before corporate cost and depreciation, and this filer's corporate cost is more than half
of its segment NOI, so operating profit by part is not in the filing. I used the filer's NOI shares; the deciding part is the
same on any measure here, but in a closer case the measure would decide. (3) The window has no specific for a business that is
selling itself down: the five-year average includes buildings sold or surrendered, so the base overstates what is now owned.
Specific (a) speaks of cycles; I showed the literal window and said it is generous. (4) Q1 against Q2: a slow shift in office
demand from remote work could be read as the "change" that routes a file to Q1 TOO HARD; the routing text speaks of
"fast-moving technology". I read it as a change in the customer's need whose effect the filings already show, so Q2 answers
it on the evidence. (5) `tools/run.py` produced nothing for a REIT whose filings tag tenant improvements, not capital
expenditure; the template assumes its table exists.
