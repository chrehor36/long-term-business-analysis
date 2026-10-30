# Company Run — CSW Industrials, Inc. (NYSE: CSW, formerly Nasdaq: CSWI) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred to this run by its blind rule, so
the analyst does not know whether the operator holds CSW. The run is written as a purchase run for a buyer who may or
may not own it.

**CONTAMINATION DECLARED.** The session's opening context showed git commit subjects naming other runs' boxes from
2026-10-05 (GENC OUT at Q2, AROC OUT at Q2, MBUU kept OUT) and a directory listing that showed the file names, not the
contents, of other 2026-10-05 runs and research passes. None was opened. No file about CSW other than this one was
opened. The barred files (`PORTFOLIO.md`, the holding reviews, `Screens/RESUME STATE*`, the run queue, the prepped
reading list, the unadopted 2026-10-05 gaps case) were not opened. Working folder: `Test Runs/_research 2026-10-05 CSW/`.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $305.83 (2026-10-05, the quote printed by `python tools/run.py CSW`, which labels it "aggregator, live quote
  only"; flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, par $0.01: **16,293,487** (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-30, accession `0001624794-26-000046`; `python Screens/cover_shares.py CSW`).
  The 8-K of 2026-08-31 (`0001624794-26-000051`) gives 16,296,266 shares entitled to vote at the 2026-07-08 record date;
  the two agree within 0.02%. No other class (10-K FY2026 balance sheet: preferred authorized, none issued).
- **Market cap:** 16.293M x $305.83 = **$4,983M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority). Revenue is 95% Americas (10-K FY2026, MD&A).
- **Filings read** (operator rule 4):
  - 10-K FY2026 (year to 2026-03-31), filed 2026-05-26, accession `0001624794-26-000027`: Items 1, 1A, 5, 7, 8 (balance
    sheet, operations, equity, cash flows, Note 2 acquisitions with the pro forma table).
  - 10-Q Q1 FY2027 (quarter to 2026-06-30), filed 2026-07-30, `0001624794-26-000046`.
  - DEF 14A filed 2026-07-16, `0001193125-26-306099` (CD&A, summary compensation, pay versus performance, ownership).
  - 8-Ks: 2025-03-18 Aspen agreement and press release (`0001193125-25-056730`); 2025-05-01 Aspen close
    (`0001193125-25-109980`); 2025-05-05 credit agreement (`0001193125-25-112791`); 2025-10-01 MARS agreement, press
    release and amendment of the CEO succession award (`0001193125-25-226016`); 2025-11-04 MARS close, Term Loan A,
    press release (`0001193125-25-264609`); 2026-08-31 annual meeting votes (`0001624794-26-000051`).
  - 424B5 of 2024-09-06 for the follow-on offering (`0001193125-24-214539`).
  - 10-Ks FY2017 to FY2025 for organic growth and segment history: `0001624794-17-000014`, `-18-000009`, `-19-000021`,
    `-20-000051`, `-21-000031`, `-22-000040`, `-23-000039`, `-24-000032`, `-25-000056`.
  - **The ticker change:** the 10-K FY2026, Item 1: listing moved from Nasdaq (CSWI) to the NYSE, trading as "CSW" from
    June 9, 2025.
  - **The 2015 spin-off:** the 10-K FY2026, Item 1: incorporated 2014 "in anticipation of CSW's separation from Capital
    Southwest Corporation"; separation executed September 30, 2015 by pro-rata distribution.
- **One figure cross-checked against the filed statement:** XBRL total assets FY2026 $2,317M against the filed balance
  sheet $2,316,684 thousand; XBRL operating cash flow FY2026 $149.7M against the filed cash-flow statement $149,653
  thousand. Both agree.
- `python tools/run.py CSW`, arithmetic lines only. **Two repairs found and made by hand:**
  (1) run.py printed stock pay as **0** for every year; the filed cash-flow line "Share-based and other executive
  compensation" is $11.537M (FY2024), $13.587M (FY2025), $14.930M (FY2026). run.py's owner-earnings lines are therefore
  overstated and are not used. (2) run.py's balance-sheet table leaves equity blank for FY2024 to FY2026; the filed
  figures are $615.7M, $1,072.2M, $1,050.4M (statements of equity, 10-K FY2026). run.py's share count is the cover count
  above and is correct after the 2024 offering. Current debt: run.py prints only long-term debt; the filed current
  portion is $29.458M at 2026-03-31 and at 2026-06-30.
- **Owner cash after every real cost** (operating cash flow less stock pay less capital spending; $M; filed cash-flow
  lines, FY2017 to FY2026; the depreciation variant beside it; computation in `_research 2026-10-05 CSW/_q7_arith.py`):

| FY (Mar) | OCF | stock pay | capex | depreciation | owner cash | (dep. variant) | interest paid | owner cash before interest, after 25% tax | per diluted share |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 39.0 | 4.6 | 9.4 | 7.9 | 25.0 | 26.5 | 2.6 | 26.9 | 1.58 |
| 2018 | 43.2 | 4.2 | 5.5 | 7.7 | 33.5 | 31.3 | 2.1 | 35.1 | 2.13 |
| 2019 | 59.7 | 3.9 | 7.5 | 7.4 | 48.3 | 48.4 | 1.3 | 49.3 | 3.12 |
| 2020 | 69.9 | 5.1 | 11.4 | 7.9 | 53.4 | 56.9 | 1.2 | 54.3 | 3.51 |
| 2021 | 66.3 | 5.1 | 8.8 | 9.2 | 52.4 | 52.0 | 1.9 | 53.8 | 3.47 |
| 2022 | 69.1 | 8.4 | 15.7 | 11.6 | 45.0 | 49.1 | 5.0 | 48.8 | 2.85 |
| 2023 | 121.5 | 9.8 | 14.0 | 12.8 | 97.7 | 98.9 | 12.5 | 107.1 | 6.30 |
| 2024 | 164.3 | 11.5 | 16.6 | 14.0 | 136.2 | 138.8 | 12.3 | 145.4 | 8.73 |
| 2025 | 168.4 | 13.6 | 16.3 | 14.2 | 138.5 | 140.6 | 4.8 | 142.1 | 8.50 |
| 2026 | 149.7 | 14.9 | 17.3 | 15.9 | 117.5 | 118.9 | 20.9 | 133.2 | 7.04 |

  Five-year average (FY2022 to FY2026): owner cash $107.0M; before interest $115.3M. The 25% is the "blended statutory
  income tax rate of 25.0%" the filer itself uses in its pro forma note (10-K FY2026, Note 2). FY2018 and FY2019 operating
  cash includes discontinued coatings operations (continuing-operations OCF $57.4M and $68.2M). Capital spending ran at
  0.7x (FY2018) to 1.4x depreciation, 1.1x to 1.2x in the last three years; the maintenance share is not disclosed (the 10-K names "continuous improvement
  and automation, safety enhancements, capacity expansion, enterprise resource planning systems and new product
  introductions"), so all of it is deducted.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would own CSW content "if the market closed for five years"
**[M1997-109]**; the answer turns on the contractor-products franchise, not on the quotation. The market serves and
"It just tells us prices." **[M2006-077]**: $100 in the stock on 2021-03-31 was worth $193.60 five years later (proxy,
pay versus performance), and the quote is now $305.83; neither figure carries an instruction about value. Margin of safety: if the case
needs a pencil, "it’s too close to think about" **[M1996-084]**. Who is paid to tell you: every acquisition release and
the proxy speak in adjusted EBITDA, the measure on which management is paid (Q4, Q6). **Contrary evidence, written down
as found** **[M1997-127]**, "write it down in the first 30 minutes": (1) run.py's zero stock pay made owner earnings
look larger than they are; (2) organic sales fell 2.1% in FY2026 and 3.6% in Contractor Solutions; (3) the filer prices
its deals in EBITDA multiples (12.4x for MARS, about 11x for Aspen); (4) MARS earned $3.9M pre-tax on $60.1M of revenue
in its first five months against a $658.1M price; (5) the filer's own risk factor: distributors "play a significant role
in determining which of our products are available"; (6) Engineered Building Solutions cut prices "in response to
competitive pressures" and impaired Greco; (7) the CEO pay plan excludes the financing cost of acquisitions from its cash
metric (+$55.2M) and gained a new lower payout threshold in FY2026; (8) buybacks of $127.5M in FY2026 at about $253 a
share were funded in a year of $871.5M of net borrowing.

## THE STANDING RULE
The buyer's conduct only: a purchase would be paid in cash from the buyer's own funds, never on margin, because
"borrowed money has no place in the investor's tool kit" **[L2014-005]**, and "We are never going to risk what we have
and need for what we don’t have and don’t need." **[M2012-081]**. No conflict found. The target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (10-K FY2026, Item 1 and MD&A; `0001624794-26-000027`): three segments. Contractor
  Solutions, $810.3M of FY2026 revenue (75%): HVAC/R and plumbing installation and service products (RectorSeal No. 5
  thread sealant, condensate pumps, switches and pans, line-set covers, TRUaire grilles, registers and diffusers made in
  Vietnam), and since 2025 Aspen evaporator coils and air handlers and MARS motors, capacitors and repair parts. Sold
  mostly through HVAC/R and plumbing wholesalers; HVAC/R was 59% of FY2026 revenue. Specialized Reliability Solutions,
  $160.1M: Whitmore lubricants, anti-seize, desiccant breathers for mining, rail, energy, industrial. Engineered Building
  Solutions, $119.9M: smoke and fire curtains, expansion joints, railings, Greco (now held for sale and exit).
- **The test as stated:** understanding is "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**; the
  chemistry or the motor can stay opaque, "What is important is that I understand the economic dynamics of the
  industry." **[M2011-014]**.
- **The key variables** "trying to identify the key variables in that particular business, and evaluating how
  predictable they were first" **[M1998-044]**: (1) the volume of HVAC/R repair and replacement work in North America,
  driven by an installed base, its age and the weather (10-K FY2026, Our Markets); foreseeable in direction over ten
  years, cyclical year to year (FY2026 organic -2.1%, Q1 FY2027 organic +5.3%, `0001624794-26-000046`); (2) CSW's price
  and position at the wholesaler's counter, which is Q2's question; (3) what management buys next, which is Q6's.
- **Change:** "We view change as more of a threat into the investment process than an opportunity." **[M1999-063]**.
  The changes in view are slow and regulatory (refrigerant rules, tariffs, ductless systems, for which CSW sells
  accessories); no fast technology decides the economics. A chemical sealant and a condensate pump in 2036 look like
  those of 2026.
- **Do the past statements tell me the future ones?** "the financial statements will tell me the information that’s
  useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**.
  Partly. The filed history describes a business that has been rebuilt by purchase every few years (TRUaire 2020,
  Aspen and MARS 2025); FY2026 pro forma revenue is $1,232.7M against $878.3M reported a year earlier (Note 2). The
  acquired pieces sell into the same channel and end market, so the past still reads forward, but less well than for a
  business whose composition is stable. Recorded as contrary evidence.
- **Doubt test:** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.
  The doubt found is about the castle and the price of growth, not about whether the economics can be followed. A
  contractor-consumables maker selling through distribution is inside the perimeter.
- **VERDICT: IN.** The ten-year economics turn on slow-moving repair demand and on position in a distribution channel,
  both readable from filings **[M2012-065]**, **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**; a moat "that protects excellent returns on invested capital"
**[L2007-004]**.

- **The record the castle must explain.** Segment operating margins after amortization of acquired intangibles, from
  the filer's segment tables (10-Ks `0001624794-20-000051`, `-23-000039`, `-25-000056`, `-26-000027`):

| FY | Industrial Products / Contractor Solutions | Specialized Reliability | Engineered Building |
|---|---|---|---|
| 2018 | 23.7% (Industrial Products) | 12.7% (Specialty Chemicals) | (in Industrial Products) |
| 2019 | 23.7% | 16.6% | |
| 2020 | 23.7% | 16.4% | |
| 2021 | 24.0% (Contractor Solutions) | 0.7% | 14.7% |
| 2022 | 23.1% | 7.8% | 11.4% |
| 2023 | 24.6% | 13.7% | 12.4% |
| 2024 | 26.5% | 14.9% | 16.3% |
| 2025 | 26.9% | 15.4% | 15.8% |
| 2026 | 21.7% (acquisitions, amortization, integration, inventory write-down) | 13.8% | -1.0% (Greco impairment $15.6M) |
| Q1 FY27 | 27.2% (with MARS and Aspen in) | 16.7% | 15.8% |

  On tangible operating capital (receivables + inventory + prepaid + plant less payables and accruals, filed balance
  sheets) the FY2025 business earned $181.2M of operating income on $313.2M, 58% pre-tax after amortization; FY2026
  $168.5M on $461.1M, 37% (51% before $51.2M amortization and $15.6M impairment).
- **Pricing power and the agony before a rise.** "you can almost measure the strength of a business over time by the
  agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. In the 2021 to 2023
  inflation, organic revenue rose 24.8% (FY2022) and 15.3% (FY2023, "due to pricing initiatives"; 10-K FY2023
  `0001624794-23-000039`) while Contractor Solutions' margin went from 24.0% to 24.6% and then 26.5%: costs were passed
  through and more, which is what "over time the businesses with strong competitive positions manage to pass through
  increases in raw material costs" **[M2005-017]** describes. Against it: in FY2026 tariffs were met by price "to
  partially offset the impact" (10-K FY2026, Item 1), and gross margin fell from 44.8% to 41.9% (mostly acquisition mix).
- **Unit volume.** Organic growth by year (10-K MD&A, each year's own figure): FY2017 +5.8% (restated basis), FY2018
  +7.8%, FY2019 +7.3%, FY2020 +5.9%, FY2021 -0.1%, FY2022 +24.8%, FY2023 +15.3%, FY2024 +3.1%, FY2025 +4.8%, FY2026
  -2.1%; compounded about 7% a year over ten years, of which the FY2022 to FY2023 pricing is a large part. FY2026
  Contractor Solutions organic -3.6% "due to lower unit volumes partially offset by pricing actions". The channel shrank
  in the same span: Watsco's calendar-2025 revenue fell to $7,239M from $7,618M (-5.0%; Watsco 10-K `0001193125-26-082486`,
  XBRL). CSW's volume fell less than its largest channel's sales: no evidence of lost share, no evidence of gained share.
- **The brand in the customer's mind, and the intermediary.** The filer: "HVAC/R contractors ask for our products by
  name" and No. 5 "is widely regarded as an industry standard for thread sealants" (10-K FY2026, Item 1). The row: "you’re
  probably going to get better gross of margins if they ask for you by name" **[M2023-073]**. The intermediary test: "the
  brand is our protection against the intermediaries making all the money" **[M2019-041]**; if the trade trusts the
  distributor as much as the brand, "then the value of having the brand moves over to the retailer from the product
  itself" **[M2001-090]**. The evidence across the span is that the value has not moved: CSW's gross margin averaged 43.9%
  FY2016 to FY2026 (proxy, adjusted; GAAP 44.2% to 44.8% FY2024 to FY2025), and its contractor segment earned 23% to
  27% operating margins while the channel earned far less (competitor row below). Against it, the filer's own risk factor:
  distributors "play a significant role in determining which of our products are available for purchase", and "Many of
  the distributors [...] also offer competitors’ products" (10-K FY2026, Item 1A). No customer was 10% or more of revenue
  in any year FY2017 to FY2026 (each 10-K, Item 1).
- **The attacker with money; the low bid.** "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The
  filer names DiversiTech, DuraVent, Intermatic, Little Giant, Nu-Calgon and RGF in HVAC/R, and BrassCraft, IPS, J.R.
  Smith, Mainline and Oatey in plumbing, and says "we compete in this space by leveraging the breadth of our product
  lines, customer service and pricing" (10-K FY2026, Item 1). The products are copyable: a condensate pump or a pad is
  not a secret, and "anything you do, your competitors can copy" **[M1996-017]**. What has not been copied in ten years
  is the economics: a funded competitor of similar scope (DiversiTech) has existed throughout, and CSW's contractor
  margins rose. The shape is the one the rows name for small specialist markets: "very small markets that aren’t really
  too attractive to anybody with any sense to enter, and fanaticism in service" **[M2011-017]**. The customer, a
  contractor buying a small item whose failure means a callback, is not choosing on "the low bid" **[M2017-009]**; that
  is inferred from the margins and the pricing record, not from a customer survey.
- **Ask the competitors.** "which one would it be and why?" **[M1999-130]**. Not possible from the record: the named
  competitors are private (DiversiTech, Nu-Calgon, Oatey, RGF) or segments of larger filers (Little Giant in Franklin
  Electric). Recorded as a gap.
- **Widening or narrowing.** "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Contractor
  Solutions: widening on the margin evidence FY2021 to FY2025, held through the FY2026 volume fall once acquisitions are
  separated out (Q1 FY2027 27.2%). Engineered Building Solutions: narrowing, on the filer's own words "strategic pricing
  in response to competitive pressures" and the Greco impairment and exit (10-K FY2026, MD&A); about 11% of revenue.
  Specialized Reliability: 14% to 15% margins against ExxonMobil, Shell, Fuchs and Kluber; no castle shown, none shown
  open.
- **What could destroy, modify or reduce it.** "destroy, or modify, or reduce the economic strengths that we perceive
  currently exist in a business" **[M2000-014]**: wholesaler consolidation and private label (the risk factor above);
  the funded private competitor; one competitor "is frequently enough to ruin a business" **[M2012-108]**; and the
  buyer's own acquisitions diluting a high-return core with lower-return pieces (Aspen's adjusted EBITDA margin about
  23% on 2024 revenue of $122.4M, per the filer's release `0001193125-25-056730`; MARS a parts distributor).
- **The competitor row** (operating margin, from each filer's own 10-K XBRL; calendar years; the channel and the
  consumables-distribution model, not direct product competitors, which are private):

| | 2015 | 2017 | 2019 | 2021 | 2023 | 2025 | accession of latest |
|---|---|---|---|---|---|---|---|
| CSW, consolidated (FY to March, following year) | n/a | 15.5% (FY18) | 17.1% (FY20) | 15.5% (FY22) | 20.1% (FY24) | 15.6% (FY26) | `0001624794-26-000027` |
| CSW Contractor / Industrial Products segment | n/a | 23.7% | 23.7% | 23.1% | 26.5% | 21.7% | as above |
| Watsco (WSO), HVAC/R distributor, CSW's channel | 8.2% | 8.2% | 7.7% | 10.0% | 10.9% | 10.0% | `0001193125-26-082486` |
| Pool (POOL), consumables distributor | 9.1% | 10.2% | 10.7% | 15.7% | 13.5% | 11.0% | `0001193125-26-074833` |
| Fastenal (FAST), consumables distributor | 21.4% | 20.1% | 19.8% | 20.3% | 20.8% | 20.2% | `0000815556-26-000009` |

  Gross margins over the same span: Watsco 24.2% to 28.0%; Pool 28.6% to 31.3%; Fastenal 45.0% to 50.4%; CSW 41.9% to
  44.8% (FY2024 to FY2026, GAAP). Watsco's 2015 to 2017 XBRL margins print identically to one decimal and are flagged as a
  transcription to verify; the comparison does not turn on a tenth. The reading: over the whole span the maker earns two
  to three times its channel's operating margin on sales and holds it; the channel has not taken the margin. The
  comparison is on sales, not capital; the distributors' capital figures were not pulled.
- **VERDICT: IN**, for the contractor-products core that is three-quarters of revenue and nearly all of segment profit:
  a decade of 23% to 27% segment margins on a small tangible base, a pricing record through the 2021 to 2023 inflation,
  and a channel that has not taken the margin, in a field a funded rival has occupied throughout **[M2005-017]**,
  **[M2011-017]**, **[M2019-041]**. Carried forward as doubt, not settled: the competitors could not be asked
  **[M1999-130]**, the distributor decides the shelf **[M2001-090]**, Engineered Building's castle is shown narrowing,
  and the newest third of the business (MARS, Aspen) has no record under CSW. The moat is not "tenuous in any way"
  **[M2000-019]** in the core on the evidence; it is unproven in the acquired pieces, which enters Q7's certainty
  **[M1999-104]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"Has it earned high returns on capital?" **[M1995-051]**; measured on "the capital actually needed in the business"
**[M2010-090]**, and for the capital allocation, "you have to include goodwill, because we paid for it." **[M2011-060]**.
- **The business's own capital.** 58% pre-tax on tangible operating capital in FY2025, 37% (51% before amortization and
  impairment) in FY2026 (Q2). Capital spending $14M to $17M a year on about $0.8 to $1.1 billion of revenue (1.6% of
  FY2026 revenue). Working capital is the real reinvestment: inventory used $35.7M of cash in FY2025 and $36.8M in FY2026
  (cash-flow statement). This is the "best business" shape of **[M1998-081]** in the core: much money, little capital.
- **The capital actually put in.** Over FY2016 to FY2026 the filer paid $1,667M in cash for acquisitions
  (`PaymentsToAcquireBusinessesGross`, XBRL, each 10-K) plus 849,852 treasury shares (valued $97.7M at close) for
  TRUaire, and raised $347.4M of equity in September 2024. Goodwill and intangibles rose from $171.5M (FY2017) to
  $1,532.7M (FY2026). On total capital including goodwill (equity $1,050.4M + redeemable NCI $19.0M + debt $869.3M -
  cash $33.8M = $1,904.9M at 2026-03-31) FY2026 operating income was $168.5M, 8.8% pre-tax; before amortization and
  impairment $235.3M, 12.4%; with the missing months of MARS and Aspen added on the filer's own adjusted EBITDA, about
  14%.
- **What the added capital earned.** FY2021 to FY2026: capital added about $1,137M (earnings retained $448.5M + equity
  raised $347.4M - buybacks $234.1M + net debt added $575M); owner cash before interest rose $79.3M, about $104M with
  full-year MARS and Aspen. About 9% after tax, 12% pre-tax at the filer's 25% rate. Decent, near the floor, nowhere
  near the core's own return: "Most of the great businesses generate lots of money. They do not generate lots of
  opportunities to earn high returns on incremental capital." **[M2003-120]**. The two largest purchases were priced at
  12.4x (MARS) and about 11x (Aspen) adjusted EBITDA (filer's releases), about 8% to 9% pre-tax before synergies; whether
  that is good "depends on what we earn on that incremental $130 million over time" **[M2001-019]**, and neither is a
  year old. "nothing shabby about earning $82 million pre-tax on $400 million of net tangible assets" **[L2007-008]**
  marks the kind: second-best, "as the second-best choice, still a good choice" **[M2018-055]**.
- **Growth arithmetic.** Owner cash before interest grew 28.6% a year FY2022 to FY2026 on the aggregate; that growth was
  bought. Organic revenue growth compounded about 7% a year over ten years (with the inflation pricing) and 1.9% a year
  over the last three. Earnings rising because capital was added is not a rising return: "we’re not earning a higher
  rate of return on capital than we were when we started" **[M2023-081]** is the pattern to test, and here the
  per-dollar return on total capital has fallen as goodwill has risen.
- **WEIGHS FOR** on the business's own capital (very high return on tangible capital, little capital to stand still)
  **[M1998-081]**, **[M2010-090]**; **UNDECIDED** on the added capital, whose return sits near 9% after tax and whose
  largest pieces are untested **[M2001-019]**, **[M2003-120]**, **[M2011-060]**. Net: WEIGHS FOR, with the caveat that
  the growth Q7 may carry is the organic rate, not the bought rate.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** "balance sheets over an 8 or 10 year period before I even look at the income
  account" **[M2025-032]** ($M; `tools/run.py` table of first-filed XBRL, checked against the filed FY2025 and FY2026
  statements; equity FY2024 to FY2026 from the filed statements of equity):

| Mar | assets | equity | cash | receivables | inventory | goodwill | intangibles | debt | retained | inventory / sales |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 398 | 272 | 23 | 64 | 50 | 81 | 91 | 73 | 245 | 17.4% |
| 2018 | 341 | 266 | 12 | 63 | 43 | 82 | 53 | 24 | 234 | 13.2% |
| 2019 | 353 | 264 | 27 | 66 | 51 | 86 | 50 | 32 | 278 | 14.7% |
| 2020 | 369 | 277 | 18 | 75 | 54 | 92 | 46 | 11 | 315 | 13.9% |
| 2021 | 875 | 412 | 10 | 97 | 98 | 219 | 283 | 243 | 347 | 23.4% |
| 2022 | 995 | 469 | 17 | 123 | 150 | 225 | 301 | 253 | 408 | 24.0% |
| 2023 | 1,043 | 526 | 18 | 123 | 162 | 243 | 319 | 253 | 493 | 21.3% |
| 2024 | 1,043 | 616 | 22 | 143 | 151 | 247 | 319 | 166 | 583 | 19.0% |
| 2025 | 1,379 | 1,072 | 226 | 156 | 195 | 264 | 358 | 0 | 705 | 22.2% |
| 2026 | 2,317 | 1,050 | 34 | 210 | 310 | 633 | 900 | 869 | 799 | 28.6% (25.1% on pro forma sales) |

  **What the figures say.** (1) The company has been bought into twice: goodwill and intangibles were 43% of assets in
  FY2017 and 66% in FY2026; tangible equity went from about +$101M (FY2017) to -$482M (FY2026). (2) Debt has cycled:
  near zero by FY2020, $243M after TRUaire (FY2021), paid to zero with the September 2024 offering (FY2025, when cash was
  $226M), then $869M after MARS and Aspen (FY2026; $855M at 2026-06-30). The FY2025 balance sheet was a pause between two
  borrowings, not a resting state. (3) Receivables held between 16% and 23% of sales throughout, 19% in FY2026: no sign of
  revenue pulled forward. (4) Inventory to sales rose from 13% to 15% (FY2018 to FY2020) to 21% to 24% after TRUaire (imported grilles)
  and to 25% on pro forma FY2026 sales after MARS (a parts distributor) and Aspen. "inventories look out of line, you
  know, with sales" **[M1995-064]**: the rise tracks the acquired mix and is explained in the MD&A line by line; recorded
  as a watch item, not a tell. Prepaid and other current assets 1.9% of sales (FY2025) to 2.5% (FY2026). (5) Retained
  earnings rose every year but FY2018 (discontinued coatings). **What they cannot say** "what the figures are saying and
  what they don’t say and what they can’t say" **[M2025-032]**: whether $766.6M of finite-lived customer lists from MARS
  and Aspen will hold their worth (the purchase-price allocations are still preliminary, Note 2), and what the acquired
  businesses earned before CSW owned them (no audited target statements were found filed).
- **The real costs.** Depreciation is real, "almost always true costs" **[L2015-004]**; capex ran 1.0x to 1.5x
  depreciation, deducted in full. Stock pay ($14.9M, 1.4% of revenue) is real, "the most egregious example"
  **[L2015-003]** of a cost owners are told to ignore, and is deducted (run.py's zero was a tool error, not the filer's).
  Amortization of acquired customer lists ($47.3M in FY2026) arises "through purchase-accounting rules and are clearly
  not real expenses" **[L2012-003]**, and owner cash adds it back; the customer lists bought at 15-year lives may deplete
  faster than that, and the run does not credit them as permanent. The recurring "one-time": transaction and integration
  costs in FY2024, FY2025 and FY2026, contingent-consideration remeasurement ($2.1M FY2025), trademark impairments
  (FY2024, FY2026), the Greco impairment and exit, a "discrete" inventory write-down (FY2026). To call these one-off
  "when management is simply making business adjustments that are necessary, is misleading" **[L2016-007]**; owner cash
  is computed from operating cash flow and leaves every one of them in.
- **EBITDA in the filer's own mouth.** The MARS release prices the deal at "10.4x pro-forma trailing twelve-month [...]
  EBITDA adjusted for identified synergies" and 12.4x "estimated adjusted TTM EBITDA" (`0001193125-25-264609`); the Aspen
  release at "11x [...] estimated 2024 adjusted EBITDA" (`0001193125-25-056730`); the proxy's headline performance lines
  are "Total adjusted EBITDA CAGR of 16.7% from FY16 through FY26" and "$270M FY26 adjusted EBITDA"; EBITDA is the
  company-selected measure in pay versus performance and the main annual bonus metric (47 uses of the word in the proxy,
  2 in the 10-K). The rows: "we do not think so-called EBITDA (earnings before interest, taxes, depreciation and
  amortization) is a meaningful measure of performance" **[R1996-023]**; "I’ll look at that figure when you tell me
  you’ll make all the capital expenditures." **[M2003-108]**; and "the number of times we’re going to buy into a company,
  whether it’s through stocks or through the entire company, where people are talking about EBITDA, is going to be about
  zero" **[M2002-026]**. Against suspicion: the 10-K itself reports GAAP segment operating income after amortization,
  deducts stock pay, discloses the pro forma adjustments in full, and states organic growth including the bad year. This
  is "a management that regularly attempts to wave away very real costs by highlighting" **[L2016-006]** in its releases
  and proxy, not in its accounts.
- **The two-tell line** (framework Q4, CONVENTION): EBITDA featured is one tell. A second was hunted: reserves that move
  (an uncertain-tax-position release of $6.4M in FY2026 on statute lapses, disclosed with its components; not a tell);
  prepaid or deferred accounts building (prepaid up from 1.9% to 2.5% of sales; small); inventory against sales (above;
  explained by mix); profits on both sides of a contract (none found). "There is seldom just one cockroach in the
  kitchen." **[L2002-039]**; no second one found. "we can’t afford to use it as a total exclusionary factor"
  **[M1994-018]** governs a management preoccupied with presentation whose accounts are clear.
- **VERDICT on confusion: IN** (the accounts are clear and reconcile; no second tell). **WEIGHS AGAINST** on EBITDA
  featured in releases, proxy and pay **[L2016-006]**, **[M2002-026]**, **[R1996-023]**. The recast earnings for Q7 are
  owner cash after stock pay and all capital spending **[L2021-003]**, before acquisition spending, with interest handled
  by subtracting the debt (Q7). *Robustness: a reader who takes **[M2002-026]** as a STOP by itself closes the file OUT
  here instead of at Q7; the box is the same.*

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. How well they run it, read from "what they’ve accomplished and what their
  competitors have accomplished, and seeing how they have allocated capital over time" **[M1994-008]**: Joseph B. Armes
  has been CEO and Chairman since the September 2015 spin (President since 2018; proxy `0001193125-26-306099`). GAAP
  operating income $47.5M (FY2016) to $168.5M (FY2026); owner cash per diluted share $1.58 (FY2017) to $7.04 (FY2026),
  $8.73 at its FY2024 peak. The coatings unit was sold (FY2018 loss from discontinued operations), Greco bought (FY2018)
  and now written down and put up for sale and exit. The hand dealt was RectorSeal, Whitmore and Smoke Guard; the
  contractor margin rose under him (Q2). How they treat owners: the proxy, "see how they treat themselves versus how they
  treat the shareholders" **[M1994-009]**, in Q6 Part B.
- **Integrity, the STOP.** "if they don’t have the last, the first two will kill you" **[M2005-003]**; on doubt alone,
  "If you’ve got doubts, forget it." **[M2013-088]**. Hunted: restatements (none in the ten 10-Ks FY2017 to FY2026; every "restated" is an amended agreement),
  material weaknesses (none; each 10-K carries an effective internal-control opinion), adverse auditor opinions (none;
  Grant Thornton in FY2026, unqualified, with the acquired-intangibles valuation as the critical audit matter), related-party dealings (policy disclosed, none material found), the stock price fixation tell (the
  proxy features relative TSR and adjusted EBITDA growth; promotional, not dishonest). The 10-K's self-description
  "We have a successful record of making attractive and synergistic acquisitions" sits beside a Greco write-down that is
  not called a mistake: the word "mistake" appears zero times in the FY2026 10-K, the FY2025 10-K and the 2026 proxy.
  "That taboo, implying managerial perfection, always made me nervous" **[L2024-003]**: a weight, not a doubt about
  honesty, since the facts of the failure (impairment, exit costs, segment loss) are disclosed plainly.
- **Love of the business.** "do they love the business or do they love the money?" **[M2000-098]**. Armes holds 72,409
  shares (proxy, as of 2026-07-08), about $22M at the price, roughly three years of his reported pay ($7.27M FY2026,
  $6.33M FY2025, $5.96M FY2024, $17.04M FY2022 with a special retention and succession grant). The October 2025 board
  action extended the vesting deadline of that succession award to April 26, 2032 because he "has expressed to the Board
  his willingness and intention to continue serving" (8-K `0001193125-25-226016`). Evidence of staying, and of an award
  kept alive that would otherwise have lapsed.
- **Ability** enters as a weight on certainty, "the degree of certainty that we attribute to the stream of income"
  **[M1999-104]**; "we still look to the underlying business, though" **[M1996-037]**. The core would survive ordinary
  management; the acquisition programme would not survive a careless one.
- **VERDICT on integrity: IN** (no tell of dishonesty found; the reports dance in their releases, not in their figures).
  **Ability WEIGHS FOR** on the operating record **[M1994-008]**, tempered by the unadmitted Greco error **[L2024-003]**
  and the combined Chairman and CEO **[L2014-026]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **Retention.** "delivers shareholders at least $1 of market value for each $1 retained" **[R1995-009]**, checked over
  three to five years since "almost any management that wants to retain money is going to rationalize it" **[M1998-110]**.
  Market leg: $100 invested on 2021-03-31 was worth $193.60 on 2026-03-31 (proxy, pay versus performance; peer group
  $166.08); market value rose by roughly $2 billion (inferred from that return, the share counts and the March 2026
  repurchase prices; no 2021 closing price was fetched) against about $562M of equity kept or raised net of buybacks
  (earnings retained $448.5M + offering $347.4M - buybacks $234.1M, FY2022 to FY2026). Intrinsic leg: the added capital,
  debt included, earns about 9% after tax (Q3). Passes on both legs, the second narrowly.
- **Buybacks.** Only "below its intrinsic value, conservatively-calculated" **[L1999-023]**; the question is "entirely
  purchase-price dependent" **[L2016-002]**. The programme ($250M, expiring 2026-12-31) names no price; it bought 503,076
  shares for $127.5M in FY2026 (about $253) and 87,970 for $23.5M in Q1 FY2027 (about $267) (10-K Item 5 and Note 13;
  10-Q Note 12). Under the framework's CONVENTION for a buyback with no stated price, the prices paid are read against
  the bottom of the Q7 range ($74): they sit far above its top ($145). And they were made in the year the company
  borrowed $871.5M net, with interest expense rising "due to increased borrowing under our Revolving Credit Facility and
  TLA to fund the acquisitions [...] and share repurchasing activities" (10-K FY2026, MD&A): the case of a business that
  "needs all its available money to protect or expand its own operations and is also uncomfortable adding further debt"
  **[L2016-003]** reversed, debt added to buy stock. **WEIGHS AGAINST.**
- **Issuance.** Two issues in ten years: 849,852 treasury shares to TRUaire's sellers at about $115 (December 2020),
  and about 1.27 million shares in September 2024 for $347.4M net, about $275 a share (424B5; equity statement). Issuing
  "beneath that figure" harms owners **[M1996-013]**; the 2024 issue was well above this run's value, so it took money
  from new owners on terms good for the old. Neither was an all-stock purchase, so the one STOP, "it's impossible for that
  buyer to make a sensible deal in an all-stock deal" **[L2009-019]**, does not arise. Not "hell-bent on issuing shares"
  **[L2014-015]**.
- **Deals: value given against value got.** "the acquirer typically gives up more intrinsic value than it receives"
  **[L1994-015]**. MARS: $658.1M for a business the filer put at $52.3M of adjusted EBITDA, with a target of a 30%
  margin within twelve months from synergies; its first five months earned $3.9M pre-tax on $60.1M of revenue after
  integration and amortization (Note 2). Aspen: $327.6M for $28.5M of adjusted 2024 EBITDA; $17.3M pre-tax on $131.7M of
  revenue in eleven months. Both were announced as "immediately accretive" to EPS, which a debt-financed deal nearly
  always is: "even a high-priced deal will usually boost per-share earnings if it is debt-financed" **[L2017-004]**.
  Greco (bought FY2018) is now being sold and exited after a $15.6M impairment; no post-mortem against the original case
  was found, and "Post mortems of acquisitions, in which reality is honestly compared to the original projections, are
  rare in American boardrooms." **[L2014-013]**. Ten years of deals did lift owner cash per share fourfold; the last two
  were bought at prices whose pre-synergy return is below the floor.
- **Part A: UNDECIDED**, leaning against: retention passes **[R1995-009]**; buybacks above value on borrowed money weigh
  against **[L2016-002]**, **[L2016-003]**; deal prices below the floor before synergies weigh against **[L1994-015]**,
  **[L2017-004]**.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls, with a charge for capital.** "a batting average that does not include a cost
  of capital is a phony batting average" **[M1995-010]**; Berkshire "both charge managers a high rate for incremental
  capital they employ" **[L1994-019]**. The annual plan pays on EBITDA and operating cash flow; acquisitions made after
  targets are set are excluded, which is good, but so is their financing: for FY2026 "the net OCF adjustments increased
  the AIP’s measured OCF by $55.2 million compared to reported operating cash flow, which was primarily driven by the
  exclusion of the MARS Parts acquisition" (proxy, CD&A). No charge for the $1 billion put into deals reaches the bonus.
  Long-term pay: performance shares on TSR relative to the Russell 2000, which removes part of the market's "that kind
  of a ride" **[M2000-062]** but measures the quotation, not the business.
- **The bar moved down, by peer comparison.** For FY2026 the committee added a "lower threshold" paying 30% at 70% of the
  EBITDA target and 60% of the OCF target "to better align the AIP’s payout matrix with practices among our Compensation
  Peer Group", and set targets twice a year (proxy, CD&A). "comp committees have become slaves to comparative data"
  **[L2005-015]**; "ratchet, ratchet, and bingo" **[M2012-095]**. A compensation consultant (WTW) is used: "But we do not
  bring in compensation consultants." **[M2004-016]**.
- **The board.** Chairman and CEO combined, with a lead independent director: "I've seen how hard it is to replace a
  mediocre CEO if that person is also Chairman." **[L2014-026]**. Directors' own holdings are small (from 495 shares for
  the newest to 22,113; proxy, which does not separate shares bought from shares granted), and the rows prefer directors "purchasing shares with their savings,
  rather than simply having been the recipients of grants" **[L2019-008]**. Say-on-pay passed with 96.76% (8-K
  `0001624794-26-000051`).
- **Part B: WEIGHS AGAINST** **[M1995-010]**, **[L2005-015]**, **[L2014-026]**.

## Q7 — WHAT IS IT WORTH? STOP.
"It is the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at the long government rate, "What is the risk-free interest rate (which we consider to be the yield on long-term U.S.
bonds)?" **[L2000-021]**, held as a range, "working with a range of possibilities is the better approach"
**[L2000-024]**; and the real question, "are you going to have to put more cash into after you buy it?" **[M2014-068]**.

- **The construction (framework CONVENTION, Part VI):** five-year average of owner cash after every real cost, carried
  ten years at the growth shown and capped by Q3, then zero nominal growth, at the sovereign, 5.63%; the ends are the
  no-growth and the shown-growth cases.
- **Base.** Five-year average owner cash before interest, after tax at the filer's 25%: **$115.3M** (FY2022 to FY2026,
  table in Step 0). **CONVENTION of this run, confessed:** the base is taken before interest and the claims ahead of
  the common are subtracted afterwards, because the debt that bought today's earning power ($855.5M at 2026-06-30) was
  almost all taken on in the last of the five averaged years; averaging after-interest cash from years with little or no
  debt would count earnings bought with debt and charge almost none of the debt. Claims ahead of the common: debt
  $855.5M - cash $47.5M (10-Q, 2026-06-30) + redeemable noncontrolling interest $19.0M + contingent consideration $16.7M
  (10-K FY2026) = **$843.6M**. (The levered alternative, $107.0M with no debt subtracted, gives $117 to $182 a share;
  shown so that the choice can be checked; it does not change the close.)
- **Growth shown, and the cap.** On the aggregate owner cash before interest, growth FY2022 to FY2026 was 28.6% a year;
  it was bought with about $1.2 billion of acquisitions in the same span and $347M of new equity, so Q3 caps it at the
  growth the business earns without new capital. Organic revenue growth was about 7% a year over ten years with the
  inflation pricing and 1.9% a year over the last three. The cap the framework names, "when the compound rate becomes
  higher than the discount rate, you get into infinite numbers" **[M1997-095]**, "if you trace out the mathematics of it,
  you bump into absurdities, then you better change expectations somewhat" **[M1999-067]**, holds the shown-growth case
  at the discount rate, 5.63%, which is below the ten-year organic rate and above the three-year one.
- **COMPUTATION** (`_research 2026-10-05 CSW/_q7_arith.py`):
  - No-growth end: $115.3M / 5.63% = $2,048M enterprise; less $843.6M = $1,204M; **$73.9 a share**.
  - Shown-growth end (5.63% for ten years, then none): $3,201M enterprise; **$144.7 a share**.
  - Width: 1.96 to one, inside the three-to-one line, so the range is usable.
  - Beside it, not the convention: on a pro forma base ($158.2M: FY2026 before interest plus the missing months of MARS
    and Aspen on the filer's own adjusted EBITDA, taxed at 25%), the same two ends are $120.6 and $217.7.
- **Value range: $74 to $145 a share against $305.83.** The price is 2.1 times the top of the convention range and 1.4
  times the top of the pro forma variant. At the price, owner cash before interest yields 2.0% on the enterprise (2.7%
  on the pro forma base); a 10% return at the price needs owner cash to grow 18.6% a year for ten years from the pro
  forma base (23.1% from the five-year base), which is the bought rate, not the earned one.
- **The floor (CONVENTION):** about ten percent pre-tax, "we don’t want to buy equities where our real expectancy is
  below 10 percent" **[M2003-149]**; "a very high probability of at least 10% pre-tax returns" **[L2002-020]**, a figure
  the speakers called their guess at opportunity cost, "we are guessing at our future opportunity cost"
  **[M2003-151]**. At $305.83 the expected return on any case this run can support is below it.
- **VERDICT: OUT.** The price sits above the top of a narrow range, which the framework closes through the floor: "there’s
  just a point at which we drop out of the game" **[M2003-149]**. Not a screamer in any variant; "It should scream at
  you." **[M2009-005]**.

**Reporting at the owner's request (COMPUTATION, not a rule change, not a clearance):**
- **VALUE RANGE:** $74 to $145 a share (framework convention); $121 to $218 on the pro forma base.
- **FAIR PRICE: about $85 a share.** Rule: the price at which the central case returns 10% a year pre-tax to the holder
  (the floor), using the convention's shape. Central case: the pro forma base $158.2M, growing 5% a year for ten years
  (between the three-year organic 1.9% and the ten-year 7%), then zero nominal growth, discounted at 10%, less the
  $843.6M of claims. Sensitivity: 3% growth gives $67, 7% gives $106; a perpetual 5% growth instead of zero after year
  ten gives about $142. The return counted is owner cash after the company's taxes, which is pre-tax to the holder;
  after a 21% corporate tax on the holder, 10% is about 7.9% (the row's own translation, printed with a damaged fraction
  character, is six-and-a-fraction to seven percent after corporate tax **[L2002-020]**).
- **CHEAP PRICE: about $45 a share.** Rule: the price at which the central (pro forma) base clears the 10% floor with no
  growth at all, so that no growth assumption and no pencil is needed: $158.2M / 10% = $1,582M, less $843.6M, over
  16.29M shares. On the five-year base the same rule gives $19.
- Against the price of $305.83: 3.6 times the fair price, 6.8 times the cheap price.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED** (Q7 closed OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED** (Q7 closed OUT). Recorded for the file, not as a clearance: debt $855.5M at 2026-06-30, secured, under
a revolver and Term Loan A maturing November 4, 2030, with $29.5M due within a year; FY2026 operating income covered
cash interest about eight times, on a year that carried the new debt for five months; the filer's pro forma adds $20.8M
of interest for a full year, which brings the cover to about four times ("you can’t talk about debt levels without relating it to the ability to pay debt"
**[M1995-104]**). For a whole business, "Businesses earning good returns on equity while employing little or no debt"
**[R1997-001]** would not describe FY2026's CSW.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED** (Q7 closed OUT).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** No named business of the rows (casinos, tobacco, loading schemes) is involved.

---
## THE BOX
**OUT at Q7** (the value question): range **$74 to $145** a share against **$305.83**; fair price about $85, cheap
price about $45 (COMPUTATION). Q1 IN, Q2 IN (the contractor core), Q3 WEIGHS FOR (with the added capital undecided),
Q4 IN on confusion and WEIGHS AGAINST on EBITDA featured, Q5 IN, Q6 Part A UNDECIDED and Part B AGAINST. The box is a
price verdict on a business the run finds good in its core, "We’ve got three boxes at the company: in, out, and too
hard." **[M2006-013]**; it is not TOO HARD, so no research pass is opened.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied, and the research folder made, before the
      first EDGAR request).
- [ ] Written question by question and committed after each (write-early). **Not done:** the operator's instruction for
      this session forbade commits, and the questions were drafted from notes and written in one pass at the end. Stated,
      not hidden.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id was checked by script
      against that row's text; every filing fact has its document and accession; no v4 id is used.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED; the Q9 record is
      marked as not a clearance; the reporting prices are labelled COMPUTATION.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less stock pay less
      all capital spending; run.py's zero stock pay was found and replaced with the filed figures. Sovereign from the
      issuing authority (US Treasury, 2026-10-02). The price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations list, and in Q1, Q2, Q4, Q6).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; N/A.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its stock pay and equity columns were wrong and
      were replaced from the filings.
- [x] `python tools/check_framework.py` PASS before finishing (no commit made, at the operator's instruction).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **EBITDA talk: STOP or weight?** Q4's "Why confusion is a STOP" paragraph quotes **[M2002-026]** ("about zero")
as the stop "stated as a count", while the heading and the template make Q4 a STOP only on confusion or suspicion, and
the two-tell CONVENTION treats "adjusted earnings featured" as one tell. A filer whose accounts are clear but whose
releases, proxy and bonus all speak adjusted EBITDA falls between the two readings. This run applied the two-tell line
(weight against) and recorded that the box is the same either way; the framework should say whether EBITDA featured
outside the accounts is a STOP by itself. (2) **The serial acquirer and the Q7 convention.** The convention averages
five years of owner cash and carries "the growth shown" on the aggregate figure. For a company whose earning power
doubled by debt-financed purchase in the last averaged year, the literal construction either averages after-interest
cash from debt-free years (overstating value) or must subtract today's debt from an average that does not yet contain
the earnings the debt bought (understating it). The run confessed its choice (before-interest base, claims subtracted)
and showed the alternatives; the framework names no rule for it, nor for whether acquisition spending is "capital
spending" to be deducted from owner cash (the run did not deduct it, and instead refused to carry bought growth, via
Q3's cap). (3) **"Capped by Q3" has no number.** The convention caps the shown growth by Q3's growth arithmetic and by
the discount rate; when the organic rate (about 7% over ten years) exceeds the 5.63% sovereign, the run used the
sovereign as the cap, reading **[M1997-095]** as binding over a ten-year span, which the row states for an indefinite
one. (4) **The template's write-early rule** conflicts with an instruction not to commit; the self-audit records the
gap. (5) **run.py** printed zero stock pay for a filer that tags it under `EmployeeBenefitsAndShareBasedCompensation`
and left equity blank after FY2023; the tool needs that tag added.
