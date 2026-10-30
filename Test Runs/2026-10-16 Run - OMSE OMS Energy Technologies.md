# Company Run: OMS Energy Technologies Inc. (Nasdaq Capital Market: OMSE), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run, written under the brief of 2026-10-16 (the canonical brief `Screens/_daily/_dispatch_brief.md` with
three stated departures: lines of evidence derived by the analyst from the 20-F; competitors taken from the 20-F's own list;
the 20-F standing where the template says 10-K). Working folder: `Test Runs/_research 2026-10-16 OMSE/`.*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: not held (`PORTFOLIO.md` carries no line for OMSE or OMS Energy Technologies).

**Contamination, declared and not used.** (1) The session context listed the five most recent commit subjects of the
repository: an INVX (Innovex) v5 re-run of 2026-10-16, with its Q2 box and figures for Weatherford, NOV, Halliburton and the
Dril-Quip half of Innovex. Nothing in them is used here; NOV's figures below are taken from NOV's own XBRL facts, and Dril-Quip
is left out of the rival set partly for this reason. (2) The same context listed untracked file names in two other companies'
research folders (AYI 2026-09-26, ARCB 2026-09-27); names only, not opened. (3) The memory index loaded with the session
carries general queue lines ("57 gate-clearers, nothing buyable"); none names this company. (4) At the start of the session,
before fetching anything, one directory listing of `Test Runs/` filtered by the string "OMS" was run to check the run file
name; it returned no file. It is declared because the blind rule forbids listing; nothing was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $3.91 (close 2026-10-15; Yahoo Finance chart API through `tools/sources.py price()`, an aggregator, used for the
  live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 42,448,704 Ordinary Shares, par $0.0001, one class (20-F for the fiscal
  year ended 2026-03-31, filed 2026-06-25, accession `0001193125-26-282941`; `python Screens/cover_shares.py OMSE` returns the
  same count). Checked: Item 4.A and Item 6.E state 42,448,704 issued and outstanding "as of the date of this annual report";
  no treasury shares are stated; Item 16E reads "Not applicable" (no repurchases); the statement of changes in equity runs
  36,900 thousand (2024-03-31) + 1,845 thousand (notes converted 2024-09-30) + 3,704 thousand (IPO, 2025-05-14) = 42,449 thousand.
  No 6-K after the 20-F exists on EDGAR (the submissions list ends at the 6-K of 2026-06-25); the six Forms 3 of 2026-03-18 to
  2026-04-02 show the chief executive's 26,226,060 shares, unchanged from the Schedule 13D of 2025-06-02
  (`0001213900-25-050288`, 61.78%).
- **Market cap:** $166.0M (42,448,704 x $3.91).
- **Sovereign for the earnings currency:** 5.43%, the US Treasury daily par yield curve, 30-year, 10/15/2026
  (`tools/sources.py sovereign('USD')`, issuing authority, not the FRED fallback). **Why USD:** the reporting currency is the US
  dollar; 59% of FY2026 revenue (Saudi Arabia, $91.8M of $155.9M) is sold to Saudi Aramco on purchase orders whose "price [...]
  is paid in USD" (20-F Item 4.B, Our Customers), and the Saudi riyal is pegged to the dollar; the rest is earned in Singapore,
  Malaysia, Indonesia, Thailand and Brunei, where the filer names OMS (Indonesia) as the one entity with a significant foreign
  currency exposure, "primarily denominated are the United States Dollar (USD) and Indonesian Rupiah (IDR)" (Note 23). The
  business therefore earns mainly in dollars or dollar-pegged riyals.
- **Filings read** (operator rule 4), all from EDGAR, CIK 2012219:
  - 20-F FY2026 (year ended 2026-03-31), filed 2026-06-25, `0001193125-26-282941`: Items 3.D, 4, 5, 6, 7, 10.E, 14, 15, 16C,
    16E, 16G, the audited statements and Notes 1 to 4 and 22.
  - 20-F FY2025, filed 2025-07-25, `0000950170-25-098559`: checked for restatement of FY2025 figures (none found; the FY2025
    revenue of $203,607K and the FY2024 periods agree with the FY2026 20-F).
  - 424B4 prospectus, 2025-05-14, `0001213900-25-042797`: the predecessor year ended 2023-03-31 (income statement, cash-flow
    statement, balance sheet at 2023-03-31), the predecessor equity at 2022-04-01, and revenue by product and market for the year
    ended 2022-03-31 (the earliest figure filed).
  - 6-K of 2026-06-25, `0001193125-26-283046`, Exhibit 99.1 (FY2026 earnings release); 6-K of 2025-11-21,
    `0001193125-25-290488` (half-year report, cover and exhibit fetched); 6-K of 2026-02-02, `0001213900-26-010531` (ZATCA
    assessment); 6-K of 2025-07-24, `0000950170-25-098129` (cover).
  - Schedule 13D, 2025-06-02, `0001213900-25-050288`; Forms 3 of 2026-03-18 (`0001213900-26-030758`, `0001213900-26-030760`),
    2026-03-19 (`0001213900-26-031869`), 2026-03-24 (`0001213900-26-033703`), 2026-03-30 (`0001213900-26-036344`), 2026-04-02
    (`0001213900-26-039432`).
  - As a foreign private issuer the company files no proxy; management, pay, control and related-party dealings are taken from
    Items 6 and 7 of the FY2026 20-F, as the brief directs.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for FY2026, $54,118K:
  the consolidated statement of cash flows (F-8) prints 54,118, and the inline XBRL tag
  `ifrs-full:CashFlowsFromUsedInOperatingActivities` in the same filing carries 54,118 (scale 3). Revenue $155,910K likewise
  agrees between the income statement (F-5), Item 5.A and the tag `ifrs-full:Revenue`.
- `python tools/run.py OMSE`: **refused**, "OMSE: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (an IFRS filer with
  three years of 20-F facts). Every figure below is taken by hand from the filed statements named above; the arithmetic is in
  `Test Runs/_research 2026-10-16 OMSE/_owner_cash.py` and its output `owner_cash.txt`.
- **How many years are filed.** Audited statements exist for the predecessor year ended 2023-03-31, the predecessor stub
  2023-04-01 to 2023-06-15, the successor period 2023-06-16 to 2024-03-31, and the successor years ended 2025-03-31 and
  2026-03-31: four fiscal years of cash flows (FY2023 to FY2026, FY2024 being two stubs on different bases joined by me), four
  balance sheets (2023-03-31 to 2026-03-31), the predecessor equity at 2022-04-01, and FY2022 revenue only. The template's eight
  to ten years of balance sheets **[M2025-032]** do not exist on the public record; this is recorded, not cured.

### The balance sheets (read here, since the file may close before Q4) **[M2025-032]**
US$ thousands, from the filed statements of financial position (2023-03-31: 424B4; 2024-03-31: 424B4 and FY2025 20-F;
2025 and 2026: FY2026 20-F).

| | 2022-04-01 | 2023-03-31 (Predecessor) | 2024-03-31 | 2025-03-31 | 2026-03-31 |
|---|---|---|---|---|---|
| Cash and equivalents | n/f | 29,527 | 43,470 | 72,950 | 151,985 |
| Due from related parties (Sumitomo cash pool; later the CEO's vehicle) | n/f | 20,981 | 1,585 | 1,584 | 1,984 |
| Trade receivables | n/f | 10,190 | 31,948 | 13,467 | 18,955 |
| Inventories | n/f | 9,460 | 30,689 | 32,546 | 17,155 |
| Property, plant and equipment | n/f | 13,483 | 32,040 | 32,055 | 28,535 |
| Goodwill and intangibles | n/f | 99 | 126 | 42 | 494 |
| Trade and other payables | n/f | 24,278 | 47,535 | 15,070 | 27,355 |
| Due to related parties (Sumitomo) | n/f | 28,038 | 0 | 0 | 0 |
| Loans and borrowings | n/f | 0 | 6,504 | 0 | 0 |
| Lease liabilities | n/f | 4,834 | 2,584 | 7,283 | 6,441 |
| Share capital and premium | 90,000 | 103,551 | 67,652 | 72,652 | 101,003 |
| Retained earnings (accumulated deficit) | (80,576) | (68,929) | 13,818 | 58,634 | 90,842 |
| Total equity | 8,182 | 34,143 | 80,354 | 134,587 | 197,391 |

*n/f: not filed (the 2022-04-01 column is from the predecessor statement of changes in equity in the 424B4).*

What the figures say: (1) by 2022-04-01 the business had lost $80.6M of the $90.0M its owner had put in; it was standing on
$8.2M of equity after fifty years of trading, and its owner (Sumitomo Corporation) injected $13.6M more in FY2023 before agreeing
to sell the whole of it for "a total cash consideration of $2 million" (Note 1). (2) The step from 2023 to 2024 is accounting,
not business: the management buyout of 2023-06-16 restated property from $13.5M to a fair value of $33.4M and booked a
"bargain purchase gain" of $49.4M (Note 3), which sits inside the 2024 retained earnings of $13.8M and inside FY2024's reported
net profit of $82.1M. (3) Equity rose from $80.4M to $197.4M in two years: $28.4M from the IPO net of costs, $5.0M from
converted notes, the rest retained profit; the retained profit sits almost wholly as cash ($152.0M against no borrowings).
(4) Receivables swung from 18% of revenue (2024) to 7% (2025) to 12% (2026), inventories from 17% to 16% to 11%; the swings
follow the Saudi call-off orders, which the filer ties to "exceptionally high call-off orders" in FY2025. (5) No goodwill, no
debt, small leases. (6) A related-party receivable from the chief executive's own company has stood on the balance sheet since
2024 ($1.6M, then $2.0M), described below under AFTER THE STOP.
What they cannot say: anything about the years 2015 to 2021 except their sum, the deficit; how the business earned through the
last downturn, year by year, is not on the public record.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years" **[M1997-109]**.
For OMSE that test turns on facts outside the business itself: a holder of the 38% float owns part of a company 61.78%
controlled by its chief executive, whose filing says "we do not expect to pay any cash dividends in the foreseeable future" (Item 3.D), which
holds $152.0M of cash against a market value of $166.0M, and has not bought in a share. The market serves and does not
instruct **[M2006-077]**: the quotation at about the cash per share says nothing by itself about value, and I do not read it as
a verdict either way. Margin of safety and the analyst's habits govern the reading: look for "what’s wrong in things" and "what
you’re missing" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the accumulated deficit of $80.6M at 2022-04-01 on $90.0M of
capital, the prior cycle's whole result; (b) 57% of FY2026 revenue from one customer (Saudi Aramco) under a ten-year agreement
with "no minimum purchase obligations" and termination "for convenience with a 30-day written notice" (Item 4.B); (c) backlog
down from $102.0M to $60.7M in the year to 2026-03-31 (Item 5.A); (d) a material weakness in internal control at 2026-03-31
(Item 15); (e) a loan from the company to its chief executive's private company (Note 22); (f) boilerplate in the 20-F that
describes a different company ("manufacturing facilities in key oil and gas hubs across North America, Europe and Asia", Item
4.B, Competition, against eleven facilities in six Asian and Middle Eastern jurisdictions; "new well service rigs, wireline
units and coiled tubing units", Item 3.D, which the company does not operate); (g) the earnings release gives FY2025
non-Saudi connector revenue as $2.0M where the 20-F gives $2.5M.

## THE STANDING RULE
The rule binds the buyer **[M2012-081]**: a purchase for cash, unlevered, in a size whose total loss the buyer can bear, puts the
buyer at no risk of ruin; borrowed money to own it is ruled out **[L2014-005]**. Nothing in this target changes that; the
target's own exposures (one customer, one country) are weighed at Q9 if reached.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** A Singapore-headquartered group of seven operating subsidiaries in six
  jurisdictions that (i) machines and welds large-diameter specialty connectors onto conductor pipe bought from pipe mills, almost
  all of it in its Dammam plant for Saudi Aramco (FY2026 $96.1M, 62% of revenue); (ii) designs and makes API 6A surface
  wellheads and Christmas trees, mostly for Pertamina Hulu Rokan in western Indonesia ($10.9M); (iii) cuts premium threads on
  tubulars under country-limited licences from VAM, Tenaris, JFE and NOV ($33.4M); (iv) inspection, repair and machining
  ($15.5M) (20-F Item 4.B; Item 5.A tables). Revenue is won "on the basis of competitive bids or direct negotiations" (Item 3.D).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the volume of Aramco's call-off orders for conductor
  connectors, which moved Saudi revenue from $13.7M (FY2022) to $46.6M, $115.6M, $141.1M and $91.8M (424B4; 20-F Item 4.B), set
  by Aramco's drilling programme and by Aramco's choice of supplier, with no minimum; (2) rig activity among a handful of
  national and international operators in South-East Asia (top ten customers 88% of FY2026 revenue, Item 3.D); (3) the price of
  steel conductor pipe, bought on purchase orders with no long-term contracts (Item 4.B, Suppliers); (4) the renewal of the
  threading licences, held from companies that are also competitors. The economics of each are plain: a fabrication and
  machining job-shop that bids for work from national oil companies, with local-content rules (Aramco's IKTVA, Indonesia's
  TKDN) favouring a supplier with a local plant. "What is important is that I understand the economic dynamics of the industry.
  Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**: these questions can be put to this business
  from its filings, and they are put at Q2.
- **The commodity routing.** The business's volume follows its customers' drilling, which follows the oil price; a dependence
  on a commodity price is never by itself a STOP at Q1 **[M2016-025]**, and the question is whether the business can be read
  "off the figures" **[M2008-069]**. It can be read as to its kind; what the figures cannot do is show the last downturn year by
  year, because they are not filed (Step 0). Whether "the financial statements will tell me the information that’s useful to me
  in making a judgment about what the future financial statements are going to look like" **[M2008-033]** is the hard part: four
  years, all inside one upswing.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. My doubt is not
  about what the business does or how it makes money, which is simple, but about the volume over ten years, which nobody outside
  Aramco can forecast; the framework places that forecast at Q2 (the low-cost question and the castle) and Q7 (the cycle base),
  not here **[M2016-025]**. Abroad, the governance and tax are readable from the filing: a Cayman holding company, Nasdaq home-
  country exemptions taken (Item 16G), Singapore 17%, Saudi 20%, Malaysia 24% and Thailand 20% tax (Item 5.A) **[M2000-141]**.
  The industry does not change fast; no technology question routes it to TOO HARD.
- **VERDICT: IN.** The economics are those of a cyclical, bid-won supplier of fabricated steel and machining services to a few
  national oil companies, and they can be judged from the filings **[M2011-014]**, **[M2008-069]**; the unforecastable volume
  is carried to Q2 and Q7 as the framework routes a commodity-linked business **[M2016-025]**. The short filed record is
  carried as a weakness of the evidence, not resolved here **[M2008-033]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (the business of parts, a CONVENTION of the framework). The filer reports gross profit by product line, not
operating profit; gross profit is used as the measure of a part's share, a CONVENTION of this run (rationale: it is the only
profit the filer allocates to its parts, and SG&A is not allocated). Gross profit over the three filed years with product
detail (FY2024 joined from its two stubs; FY2025; FY2026), US$ thousands, from 20-F `0001193125-26-282941` Item 5.A:

| Part | Gross profit FY2024 / FY2025 / FY2026 | Share of three-year gross profit | Castle | Decides |
|---|---|---|---|---|
| Specialty connectors and pipes (99% then 95% of it made in Saudi Arabia for Aramco) | 28,750 / 45,413 / 28,463 | 60.4% | read below | **yes, more than half** |
| Premium threading (licensed) | 14,187 / 14,337 / 9,455 | 22.4% | licensed from rivals, country-limited | no |
| Other ancillary services | 6,089 / 7,073 / 6,233 | 11.3% | inspection and repair | no |
| Surface wellheads and Christmas trees | 4,743 / 2,164 / 3,079 | 5.9% | one Indonesian contract | no |

The file closes on the connectors part.

**The castle tests, each with its filing fact.**
1. *Key factors, and how permanent* **[M1995-038]**. What keeps OMS Saudi on Aramco's supplier list is a local plant (Dammam,
   a 20-year lease from 2018), API certifications and Aramco's IKTVA local-content programme (Item 4.B, Growth Strategies). None
   of these binds the customer: the ten-year Corporate Purchase Agreement of January 2024 carries "no minimum purchase
   obligations" and Aramco "can terminate the LTA for convenience with a 30-day written notice" (Item 4.B). Orders come as spot
   purchase orders and call-offs. The castle's key factor is the customer's continued choice, renewed order by order.
2. *The money test* **[M2011-015]**: could a well-funded rival take the work? The filer names its rivals as SLB, TechnipFMC,
   Baker Hughes, Oil States, NOV and Dril-Quip, says "some of our competitors may be better funded or better connected", and
   says "The larger size of many of our competitors provides them with cost advantages as a result of their economies of scale
   and their ability to obtain volume discounts and purchase raw materials at lower prices" (Items 4.B and 3.D). The rival with
   money is already in the field and, on the filer's own account, holds the lower cost. The local-content rule raises the entry
   cost to a plant in the Kingdom; it does not close the door to rivals that already operate there at scale.
3. *Pricing power and the agony before a rise* **[M2005-020]**: in the filer's words, "we operate in a very competitive industry
   and as a result, we are not always successful in raising, or maintaining, our existing prices", and "Competitive pressures
   could reduce our market share or require us to reduce the price of our services and products, particularly during industry
   downturns" (Item 3.D). Customers "are using their size and purchasing power to seek economies of scale and pricing
   concessions" (Item 3.D). This is the prayer session in the filer's own voice.
4. *Unit volume*: Saudi revenue $13.7M, $46.6M, $115.6M, $141.1M and $91.8M over FY2022 to FY2026 (424B4; 20-F), and backlog
   from $102.0M to $60.7M in FY2026 (Item 5.A). A tenfold rise and a 35% fall in five years is the customer's drilling
   programme, not a place in the customer's mind.
5. *The low-cost position* **[M2006-004]**, **[M2009-059]**: the filing states no unit cost and no cost comparison; it says the
   larger rivals hold the cost advantage (test 2). Saudi gross margin was 30.0% (FY2024), 31.6% (FY2025) and 30.2% (FY2026)
   (Item 5.A, revenue and cost by market), all in the upswing; no downturn margin is filed. There is no evidence that OMS is the
   low-cost producer, and the filer's own words point the other way.
6. *Would the customer choose it over the low bid* **[M2017-009]**: "Contracts are traditionally awarded on the basis of
   competitive bids or direct negotiations with customers via fixed-price, turnkey contracts and transactional agreements", and
   "Price competition" heads the factors "used by customers in awarding contracts" (Item 3.D). The products are made to API
   standards so that they are "safe, reliable and interchangeable" (Item 4.B). This is the customer who buys on the bid
   **[L2004-003]**.
7. *Ask the competitors, and the field's returns*: the competitor row and the field's returns below.
8. *Widening or narrowing* **[M1999-108]**: the diversification moves (connectors to the UAE, Pakistan and Indonesia, $4.6M;
   first wellheads in Pakistan and Angola; packers) are small against a $91.8M Saudi line whose volume fell 35% in a year, and the
   threading line's cost rose on "higher variable licensing cost rates" (Item 5.A). No evidence of a widening moat.
9. *What could destroy it* **[M2000-014]**: Aramco cutting call-offs, moving the work to another local supplier, or in-sourcing;
   the filer lists "in-sourcing, shifting business to a competitor" among the ways a major customer is lost (Item 3.D). "one
   competitor is frequently enough to ruin a business" **[M2012-108]**; here one customer's decision is enough.

**The competitor row.** The 20-F names its rivals (Item 4.B, Competition): Schlumberger (SLB), TechnipFMC, Baker Hughes, Oil
States Industries (part of Oil States International), National Oilwell Varco (NOV) and Dril-Quip; all six file 10-Ks (Dril-Quip
merged into Innovex in 2024); none is a non-filer. Three are taken, chosen for product overlap: Oil States (connector products),
NOV (wellbore and tubular products) and TechnipFMC (surface wellheads in its Surface Technologies segment). Dril-Quip is left out
because its standalone filings stop in 2024 and because of the contamination declared above; SLB and Baker Hughes are far broader
businesses. Metric: operating income over revenue, and net income, whole company, as first reported in each year's 10-K (SEC XBRL
company facts, pulled by `_peers.py`; the accession of each 10-K is listed in `Test Runs/_research 2026-10-16 OMSE/peers_xbrl.txt`).
Whole-company figures, not segment figures: a CONVENTION of this run (rationale: the segment series are not tagged consistently
across the span, and the whole company is what a holder of the rival owned).

| Year | Oil States opm | NOV opm | TechnipFMC opm |
|---|---|---|---|
| 2014 | 17.1% | 16.9% | n/p |
| 2015 | 5.0% | -2.6% | n/p |
| 2016 | -10.0% | -33.3% | n/p |
| 2017 | -11.0% | -3.8% | 9.0% |
| 2018 | -0.5% | 2.5% | -4.2% |
| 2019 | -22.4% | -74.1% | -8.5% |
| 2020 | -83.7% | -39.8% | -19.6% |
| 2021 | -11.3% | -2.4% | 2.9% |
| 2022 | 0.4% | 3.6% | 5.6% |
| 2023 | 3.0% | 7.6% | 8.4% |
| 2024 | -0.2% | 9.9% | 12.7% |
| 2025 | -14.6% | 5.6% | 14.5% |
| **Net income summed** | **-$1,002M (2015 to 2025)** | **-$10,408M (2015 to 2025)** | **-$5,743M (2017 to 2025)** |

*n/p: not pulled (TechnipFMC was formed in January 2017; the FMC Technologies years before it were not read). Latest
accessions: Oil States 10-K FY2025 `0001121484-26-000007`; NOV 10-K FY2025 `0001193125-26-048350`; TechnipFMC 10-K FY2025
`0001681459-26-000010`; earlier years as listed in the research file. The large negative years carry impairments, which are real
losses of capital put in.*

**The filer's own return over the last full cycle.** OMSE's operating margin in the upswing was 20.4% (FY2023), 23.9% (FY2024,
joined stubs), 29.4% (FY2025) and 22.4% (FY2026) (424B4; 20-F). Of the cycle before it the only filed figure is the sum: an
accumulated deficit of $80,576K at 2022-04-01 against $90,000K of share capital (424B4, predecessor statement of changes in
equity), for a business trading since 1972 (Item 4.C). The owner then sold the whole of it for $2.0M, and the filer's own
explanation of the bargain is that the price was fixed "back in 2022 during which the oil and gas industry is still recovering
from a major downturn" and that "market conditions have improved materially since the downturn" (Note 3). The filer itself
attributes the change to the cycle, not to a new castle.

**The field's returns over the last full cycle, judged in words** ("ordinary" carries no figure, a CONVENTION of the framework).
Across the downturn of 2015 to 2021 and the recovery to 2025, the three named rivals lost money in aggregate; the filer lost
almost all of its owner's capital before the upswing; the upswing margins at OMSE (20% to 29%) and at the rivals (TechnipFMC's best
14.5%, in 2025) are the top of the cycle, not its average. A durable field of bidders whose full-cycle return is at or below zero
is the standing castle that protects only ordinary returns, and worse than ordinary: "you can have only two competitors and
they’re still terrible businesses, they beat each other’s brains out" **[M2013-052]**. The castle stands (fifty years, local
plants, API and licence certificates); what it protects over a cycle is not an excellent return **[L2007-004]**.

**Is this a change for the better, to be credited only on a full cycle?** The framework sends an unproven change for the better to
TOO HARD (NATURE). I read that clause as not engaged here: the filer attributes the improvement to "market conditions" (Note 3);
the rivals' margins rose over the same years; and no structural change in the castle is shown (the 2024 Aramco agreement binds
Aramco to nothing, and Saudi volume fell 35% in its second year). The returns of the last full cycle are known from the filings,
which is the case the OUT item names; the tenuous-moat reason for TOO HARD, "We don’t know how to valuate that" **[M2000-019]**,
does not apply when the returns are known. The alternative reading is recorded in the gaps section.

- **VERDICT: OUT.** On the deciding part (specialty connectors for Aramco, 60% of three-year gross profit): a standing castle that
  protects only ordinary returns, shown by the filer's own words (bids, price competition, rivals with the cost advantage, a
  customer bound to nothing and seeking concessions) and by the full-cycle returns in the filer's and three named rivals' own
  filings **[L2007-004]**, **[M2013-052]**, **[L2004-003]**, **[M2005-020]**. The commodity-business routing gives the same answer
  from the other side: no evidence that the company is the low-cost producer, and the filer says its larger rivals are
  **[M1997-010]**, **[M2006-004]**.

Q3 to Q12: **NOT REACHED** (operator rule 2). Facts already found are written under AFTER THE STOP below, not weighed.

---
## THE BOX
**OUT**, decided at **Q2**: a standing castle that protects only ordinary returns over the last full cycle, on the filer's own words
and the full-cycle results in its own and three named rivals' filings **[L2007-004]**, **[M2013-052]**. **Integrity facts recorded,
not judged** (under Q5 below). COMPUTATION, NOT A CLEARANCE, beneath the stop: value (no-growth case alone, all-equity) about
$16.07 a share against $3.91; fair price about $10.36 all-equity ($7.03 equity-only); the literal window's range $16.07 to $62.96,
fair $20.50 all-equity ($17.55 equity-only); the cycle base the framework asks for is not on the public record.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found, each with its source **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).*

**Bearing on Q3 (capital needed).** Property, plant and equipment of $28.5M and right-of-use assets of $7.1M carried $155.9M of
FY2026 revenue; capital spending was $1.1M, $3.2M (successor stub), $2.9M and $1.1M plus $0.5M of intangibles over FY2023 to
FY2026, below depreciation of property in three of the four years (424B4; 20-F cash-flow statements); the filer says "We expect
our production facilities will require minimal capital expenditures for maintenance on an annual basis" (Item 4.B). Working
capital moves with the Saudi orders: an inventory build of $20.8M in the FY2024 successor period and a release of $16.2M in
FY2026 (cash-flow statements). Operating return on tangible capital in the upswing was high; over the prior cycle the capital
put in was almost all lost (Q2).

**Bearing on Q4 (the accounts).** (1) FY2024's reported net profit of $82.1M includes a $49.4M bargain purchase gain on a $2.0M
purchase, and the earnings per share of $2.19 for that period carry it (20-F, F-5; Note 3). (2) Depreciation rose after the buyout
because property was written up from $13.5M to $33.4M (Item 5.A; Note 3). (3) The FY2026 tax charge of $4.5M (11.8% of pre-tax
profit) includes the $2.3M recovery of the 2017 Saudi assessment (Item 5.A); the 2019 assessment of $0.6M went against the
company (Item 4, Legal Proceedings). (4) "Adjusted EBITDA" and "Adjusted free cash flow" are featured among the six headline
bullets of the FY2026 earnings release (6-K `0001193125-26-283046`, Exhibit 99.1) and as "Key Non-IFRS Financial Measures" in
Item 5.A; adjusted free cash flow omits the $1.5M of lease payments. A featured adjusted figure is recorded at Q4 as a weighing
against and carried to Q5 **[L2016-006]**, **[M1998-086]**. (5) Two figures disagree between documents: FY2025 connector revenue
outside Saudi Arabia is $2.5M in the 20-F (Item 5.A) and $2.0M in the earnings release; intangible purchases in the half-year to
2024-09-30 are $283K in the half-year report (6-K `0001193125-25-290488`) against nil for the whole of FY2025 in the annual
cash-flow statement. Neither is reconciled in the filings read. (6) Material weakness at 2026-03-31: the company "did not
maintain a sufficient complement of personnel with an appropriate level of knowledge, experience, and training in International
Financial Reporting Standards ('IFRS') and SEC reporting requirements" (Item 15); disclosure controls ineffective; no auditor
attestation (emerging growth company). Auditor Marcum Asia CPAs LLP, PCAOB ID 5395, since 2023; audit fees $437K, $488K, $355K
(Item 16C). (7) The balance sheets are four, not eight to ten (Step 0) **[M2025-032]**.

**Bearing on Q5 (who runs it), integrity facts recorded, not judged.**
- *Control and the buyout.* Mr. How Meng Hock was appointed chief executive of OMS by Sumitomo Corporation in April 2014 and ran it
  through the years in which the accumulated deficit reached $80.6M (Item 6.A; 424B4). On 2023-01-04, while chief executive, his
  newly formed company OMSET PL agreed to buy the whole business from Sumitomo for "a total cash consideration of $2 million"
  (Note 1); the net assets acquired were later valued at $51.4M, including $29.9M of cash (Note 3). He owns 61.78% (Item 6.E;
  Schedule 13D `0001213900-25-050288`); the IPO of 2025-05-14 at $9.00 sold only new shares, and his 26,226,060 shares are unchanged
  in his Form 3 of 2026-03-18 (`0001213900-26-030760`). This is the hand dealt and how he played it **[M1994-009]**.
- *A loan from the company to the controlling shareholder's company.* The listed company carries a "Loan due from a related
  party" of $1,984K (2026-03-31; $1,584K a year earlier) owed by OMS Energy Technologies Pte. Ltd., "Controlled by ultimate
  controlling individual, Mr. How, the CEO of the Successor"; it arose in FY2024 from "costs incurred as part of our initial
  public offering", was non-interest-bearing until a loan agreement in FY2026, now "is unsecured, bears interest at 1.7% per annum
  payable in arrears, and is fully repayable on March 31, 2027", and rose by $400K in FY2026 (Item 7.B; Note 22; Item 5.B; the
  cash-flow statement). Note 1 describes the same OMSET PL as having "became a shell company". In the same Item 7.B the filer
  states: "the Successor had no related party transactions" for FY2024 to FY2026, and two tables later reports $93K of finance
  income from that related party in FY2026.
- *Pre-IPO issuance to a director's circle.* In February 2024 the successor issued $5.0M of convertible notes at 10% to "RFWM VCC —
  RF Dynamic Fund and Vielink Asia Pte Ltd", converted on 2024-09-30 into 1,845,000 shares, about $2.71 a share against the IPO
  price of $9.00 eight months later (statement of changes in equity, note (2)). Director Ng Tse Meng, appointed May 2024, is
  "Chairman of Ruifeng Wealth Management Pte. Ltd." and holds 922,500 shares, half of the 1,845,000 (Item 6.A, 6.E). The filing
  does not say whether he controls the fund; the facts are written down as found.
- *Disclosure written for another company.* The competition paragraph claims "manufacturing facilities in key oil and gas hubs
  across North America, Europe and Asia" and technologies "such as subsea production systems and well completion tools" (Item
  4.B), against the filer's own list of facilities in six Asian and Middle Eastern jurisdictions; a risk factor speaks of "new well
  service rigs, wireline units and coiled tubing units" (Item 3.D); the 6-K of 2026-02-02 (`0001213900-26-010531`), reporting the
  ZATCA decision, carries forward-looking boilerplate about "the expected completion of the Private Placement, the potential full
  exercise of the Purchaser Warrants", though no private placement is described. Whether the reports tell an owner "about the
  things that we would want to know about" is a Q5 test; these facts bear on it.
- *Pay and board.* Aggregate cash paid to directors and executive officers $605K in FY2026; "no options are issued or outstanding"
  (Item 6.B, 6.E); independent directors paid $15,000 a year each; the chief executive is also chairman; Nasdaq home-country
  exemptions taken, including from shareholder approval of equity compensation plans (Item 16G).
- *Habits carried from Q4:* the featured adjusted figures, and the two unreconciled figures, above.
- Any later run that reaches Q5 must answer these on the integrity record; doubt closes the file **[M2013-088]**.

**Bearing on Q6 (the money and the owners).** Cash rose from $73.0M to $152.0M in FY2026, $28.9M of it IPO proceeds, of which
"we have used $4.4 million" (Item 14); no dividend and none expected (Item 3.D); no repurchase (Item 16E: "Not applicable"). With
the market value of $166.0M near the cash, and funds "beyond the near-term needs of the business", the one combination for a
buyback that **[L1999-023]** names would be met if the price is below value; none was made. The retention test asks whether a
dollar kept will become more than a dollar **[M2008-104]**; the stated uses are "organic growth initiatives" and "selectively
evaluate strategic expansion opportunities" (earnings release). **Buyback test against the bottom of the Q7 range:** no shares
were bought, so there are no prices paid to set against the bottom of the COMPUTATION range ($16.07 a share); the test has nothing
to read.

**Bearing on Q9 (could it ruin us).** No borrowings at 2026-03-31; lease liabilities $6.4M; trade payables $27.4M; restricted cash
of $2.3M pledged for bank guarantees (Note 5). Exposures: one customer at 57% of revenue (67% in FY2025) on terms it can end on 30
days; "fixed-price contracts" under which "we are typically responsible for all cost overruns"; contracts carrying "termination for
convenience" clauses (Item 3.D); Saudi and Middle East geopolitical risk named by the filer. The "little or no debt" criterion
**[R1997-001]** would be met.

**Bearing on Q12.** Nothing found.

### COMPUTATION, NOT A CLEARANCE (Q7 as it would be built; the file is closed at Q2)
*Every figure in this sub-section is arithmetic beneath a closed STOP. It carries no entry language and is not a clearance
(operator rule 3).*

**Owner cash after every real cost, all-equity basis, US$ thousands** (`_owner_cash.py`, `owner_cash.txt`): operating cash flow as
filed, less interest received (the cash that earns it is counted in net cash), less the one-off FY2026 tax refund of $2,398K, less
all capital spending net of disposals, less lease principal and lease interest (rent; the leases are therefore left out of net
debt, and said so), less the profit attributable to minority interests (a CONVENTION of this run: the minority holders of the
Malaysian subsidiaries own that share of the cash; rationale: the framework names no treatment, and the minority's profit share
is the nearest filed measure of its claim).

| | FY2023 (Predecessor year) | FY2024 (two stubs joined) | FY2025 | FY2026 |
|---|---|---|---|---|
| Operating cash flow as filed | 29,030 | 21,155 | 40,502 | 54,118 |
| Owner cash (all spending deducted) | 24,988 | 13,585 | 33,584 | 42,950 |
| Depreciation variant (property depreciation in place of capital spending) | 25,195 | 13,285 | 33,736 | 39,906 |
| Owner cash as a share of revenue | 25.6% | 7.5% | 16.5% | 27.5% |

- **Window.** Four fiscal years, not five, because only four are filed; FY2024 joins a predecessor stub and a successor period
  prepared on different bases (a CONVENTION of this run; rationale: the framework's five-year average needs five filed years, and
  the public record has four). Average **$28,777K**. Taxes are taken as paid; over the four years tax paid ($33.3M) and tax charged
  ($35.2M) are close.
- **Specific (a), cycles.** The window is aberrational at both ends on the filer's own description: FY2023 is the year in which,
  the filer says, the industry "is still recovering from a major downturn" (Note 3); FY2025 was "exceptionally high call-off orders"
  (Item 5.A) and "an unusually high prior-year base" (earnings release); FY2026's owner cash carries a $16.2M inventory release the
  filer ties to "lower customer demand and reduced pre-orders" (Item 5.B) **[L2005-003]**. The base should therefore be the average
  over the last full cycle. That cycle is not on the public record: of FY2015 to FY2022 only the sum survives, an accumulated
  deficit of $80.6M on $90.0M of capital. **The cycle base cannot be computed from the filings read**; the literal window is shown
  in its place and overstates it, on the only evidence there is.
- **Specific (b), growth.** Between the end years the aggregate owner cash grew 19.8% a year; between the halves of the window,
  40.9% a year. Both measure a recovery from a trough to a peak, not growth, and are meaningless by **[L2005-003]**; by (b) the range
  is therefore **the no-growth case alone, said so**. The literal growth case is shown beside it.
- **Specifics (c) to (f).** (c) no acquisitions in the window (the $2.0M buyout is the owner's purchase of the business, not the
  business's purchase); (d) working capital is inside operating cash flow; (e) the filing allows no separate maintenance guess
  beyond the filer's "minimal capital expenditures for maintenance"; all spending is deducted and the depreciation variant is beside
  it; (f) the cap: carried ten years at 19.8% against sales growth of 17.0% over the same window, owner cash would reach about 23% of
  sales, below the highest share filed (27.5%, FY2026), so the cap does not bind by its letter.
- **Net cash** at 2026-03-31: cash and equivalents $151,985K; no borrowings; restricted cash ($2,317K, pledged), the related-party loan
  ($1,984K) and the leases are left out. No subsequent event is stated in the 20-F (Item 8.B).
- **Rate:** 5.43%, the 30-year Treasury, 10/15/2026. Ten years, then zero nominal growth.

| Case | Value of the business (all-equity) | Per share, plus net cash | Per share at 10% (for the fair price) |
|---|---|---|---|
| No growth (the range, by (b)) | $529,959K | **$16.07** | $10.36 |
| Literal window, shown growth 19.8% (beside) | $2,520,381K | $62.96 | $30.64 |

- **The floor, tested first.** At $3.91 the market value is $166.0M and, less net cash, the business is priced at about $14.0M; the
  no-growth owner cash of $28.8M is about twice that each year. Every case earns the floor at the price.
- **The width.** The no-growth case alone has no width; the literal window runs $16.07 to $62.96, about 3.9 to one, wider than three
  to one.
- **What Q7 would have closed.** Not IN on these numbers. The floor's close does not apply, since every case clears it at the
  price; the close that would apply is the first of Q7's three (the framework's heading: cannot be valued), because the cash stream over a cycle cannot be
  estimated from the filed record: "if we don’t have the faintest idea what the future stream is going to look like, we don’t have
  the faintest idea what it’s worth, now" **[M1994-077]**. That is TOO HARD, with WORK as its cause if the Sumitomo-era accounts of
  OMS Holdings Pte. Ltd. can be had from the Singapore registry (not tried) and NATURE if not. Recorded, not decided; the box is OUT
  at Q2.
- **The reporting figures** (a reporting convention; neither is a verdict or entry language):
  - **VALUE RANGE:** about **$16.07 a share** (the no-growth case alone, all-equity, after the company's own tax), against $3.91;
    beside it the literal window, $16.07 to $62.96.
  - **FAIR PRICE:** about **$10.36 a share on the all-equity basis** (the no-growth case valued at ten percent, $287,767K, plus net
    cash; with one end case only, the average of the two ends is that case), and **$7.03 a share equity-only** (owner cash after
    interest, $29,851K, at ten percent, against the market value alone). Beside it, on the literal window's two ends averaged:
    $20.50 all-equity, $17.55 equity-only. After the company's own tax, no conversion.
  - **What these figures do not see, written down:** the cycle base (above); one customer's call-offs as the deciding part's volume;
    a $152.0M cash balance controlled by a 61.78% holder who pays no dividend and to whose company the business has lent money
    ("off-shore cash is simply not worth as much as cash held at home" **[L2016-009]** names the principle that limited cash is worth
    less; the framework gives no rule to price it, and it is added at face here); the backlog down 40% and the second-half FY2026
    revenue of $73.1M against $82.8M in the first half (6-K `0001193125-25-290488`; 20-F).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): Step 0 to Q1
      `b637a8f5`, Q2 `51fde3f9`, the close in the last commit.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not written or
      touched here); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched; one filtered listing of `Test Runs/` (string
      "OMS", no result) and the session-context items are declared under contamination and were not used.
- [x] Every v5 id cited resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row
      (`_check_citations.py`, PASS); no E-ids. Every filing fact carries its document and accession.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; nothing after it is a clearance; the Q7 arithmetic is headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price quote from an aggregator, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS) **[M1997-127]**; the facts for later questions are under AFTER THE
      STOP; the integrity flag is in the box line.
- [x] Not a point-in-time run; no anchor rule engaged.
- [x] `tools/run.py` refused this filer; nothing it prints was used. `Screens/cover_shares.py` was used for the share count only.
- [x] `python tools/check_framework.py` PASS before the last commit.
- Not done: the Singapore registry accounts of the predecessor (the cycle base); the FMC Technologies years before 2017; segment
  margins of the rivals; the Dril-Quip filings (left out, see contamination).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Change for the better against the standing castle.** Q2 holds two rules that touch this name differently: a field whose
durable players earn ordinary returns over a full cycle is OUT, and a change for the better is credited only on a full cycle,
until then TOO HARD (NATURE) with a re-look at the first year volume falls. OMSE's upswing returns are high, the prior cycle's are
known to be poor, and the text does not say which rule governs when a business claims a change that coincides with the cycle. I
chose OUT because the filer itself attributes the change to "market conditions" and the rivals moved the same way; another analyst
could read TOO HARD (NATURE). Under that reading the re-look year may already have come: in FY2026 the Saudi volume fell 35% and
the Saudi gross margin held at 30.2% against 31.6%, which is evidence for price behaviour in a fall, but the fall was one
customer's call-off timing in a year when the field's margins rose, not a field downturn; the text does not say whether a
customer-specific fall counts. (2) **The cycle base that is not filed.** Specific (a) sends an aberrational window to the last full
cycle's average and assumes the filings contain it; for a company listed after a buyout, only the sum of the last cycle (a
deficit) is public. There is no instruction for this case beyond Q7's "cannot be valued", and no rule for whether a foreign
registry's filings count as "a filing not yet read" (WORK) or not. (3) **Four years, two bases.** The five-year average presumes
five filed years; I averaged four, one of them joined from two stubs prepared on different bases, and confessed it. (4) **Cash
under control.** The all-equity basis adds net cash at face; where a 61.78% holder controls a cash pile equal to the market value
and pays nothing out, the rows say limited cash is worth less **[L2016-009]**, but no rule prices it, so the reporting figures are
likely too high for a minority holder. Minority interests in subsidiaries are likewise untreated; I deducted their profit share
and confessed it. (5) **The parts threshold on gross profit.** The parts rule is written on five-year operating profit; the filer
allocates only gross profit, over three years; I used that and said so. (6) **Tooling.** `tools/run.py` refuses an IFRS 20-F filer;
every figure was taken by hand. (7) **The brief.** Its line on the 6-K of 2026-02-02 says the ZATCA assessment is "under appeal";
the 6-K itself reports the appeal committee's decision in the company's favour on 2025-12-23, and the 20-F reports the refund on
2026-03-12. (8) The template's own headings contain dashes of the kind the operator's style rule forbids in prose; they were kept as
form text.
