# Company Run — Fastenal Company (Nasdaq: FAST) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run of record**, under the canonical brief `Screens/_daily/_dispatch_brief.md` with its slots filled. The
brief departs from the canonical one in one place, stated by the dispatcher: the lines of evidence were not written by the
dispatcher; the analyst derived them from the 10-K's Item 1, Item 1A and Item 7 (listed under Step 0 below).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker, 2026-10-12).

**Contamination, declared:** (1) Before copying the template I ran a directory listing of `Test Runs/` filtered for "FAST"
or "Fastenal" to check for a file-name clash; it returned nothing, and nothing was opened. The brief's blind rule counts a
listing of `Test Runs/` as opening it, so the act is declared here. (2) The session context showed the repository's git
status (research folders of other names such as AYI and ARCB) and the subjects of the last commits (two other names'
folds), and the lock file name in `Screens/_daily/`; none concerns this company and none was used. (3) The memory index
loaded with the session names counts of gate-clearers and holdings reviews owed in general terms; it names no company
relevant here and was not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $51.55 (2026-10-12, live quote from the aggregator `tools/run.py` uses; **aggregator, flagged** per operator
  rule 5; not a filed figure).
- **Shares by class** from the latest filing's cover: one class, common stock, par $.01, **1,147,497,573** shares as of
  2026-07-10 (10-Q for the quarter ended 2026-06-30, filed 2026-07-16, accession `0000815556-26-000041`;
  `python Screens/cover_shares.py FAST`). Check: the balance sheet in the same 10-Q gives 1,147,494,415 shares "issued and
  outstanding" at 2026-06-30 (the company holds no treasury stock; repurchased shares are retired, so issued equals
  outstanding). The difference to the cover is 3,158 shares, option exercises after the quarter. No 8-K or prospectus
  filed after the 10-Q changes the count: the filings after it are the 8-K/A of 2026-07-16 (CEO pay, accession
  `0000815556-26-000043`) and an S-8 of 2026-07-16 (`0000815556-26-000039`) registering shares for the new RSU plans, which
  issues nothing by itself. The two-for-one split effective at the close of 2025-05-21 (8-K of 2025-04-25, accession
  `0000815556-25-000087`) is already in every count above; per-share figures from filings before it are halved where used
  below (and an earlier two-for-one split of 2019 is likewise reflected wherever a 2018 price is quoted).
- **Market cap:** $51.55 x 1,147.498M = **$59,153M**.
- **Net debt** (for the all-equity basis of Q7), latest filed balance sheet, 2026-06-30 (10-Q `0000815556-26-000041`):
  current portion of debt $70.0M + long-term debt $50.0M = $120.0M of borrowings (senior unsecured notes under the Master
  Note Agreement; no revolver balance stated), less cash and cash equivalents $204.7M = **net cash $84.7M** (net debt
  -$84.7M). No finance leases are stated; operating leases ($316.9M of lease liabilities at 2025-12-31) are left out, as
  Q7's basis convention says. The subsequent event the 10-Q itself states (the credit agreement and note amendment of
  2026-06-18) changes commitments, not borrowings. All-equity market value: $59,153M - $84.7M = **$59,068M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, the US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`; the issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for 2025, filed 2026-02-05, accession `0000815556-26-000009` (Items 1, 1A, 2, 5, 7, 7A, 8 and the notes read).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-07-16, `0000815556-26-000041` (balance sheet, cash flows, MD&A,
    debt note, share purchases).
  - Proxy (DEF 14A) for the 2026 meeting, filed 2026-02-25, `0000815556-26-000017` (pay, peer group, ownership, related
    persons, the two RSU plans).
  - 8-Ks: 2025-04-10 (`0000815556-25-000077`, interim CFO), 2025-04-25 (`-25-000087`, split), 8-K/A 2025-02-06
    (`-25-000068`, change of auditor KPMG to PwC), 2025-11-03 (`-25-000121`, new CFO), 2025-12-22 (`-25-000123`, CEO
    transition), 2026-04-29 (`-26-000027`, RSU plans approved), 2026-06-12 (`-26-000033`, new director), 2026-06-23
    (`-26-000035`, credit agreement), 8-K/A 2026-07-16 (`-26-000043`, new CEO's pay).
  - Earlier 10-Ks for the cycle and the window: FY2016 (`0000815556-17-000009`), FY2020 (`0000815556-21-000008`), FY2021
    (`0000815556-22-000009`), FY2022 (`0000815556-23-000009`), FY2023 (`0000815556-24-000009`); the FY2024 figures are read
    in the FY2025 10-K's three-year statements. Older years (2007 to 2015) from the XBRL first-filed vintages, flagged as
    transcription.
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities, 2025:
    $1,295.9M on the filed Consolidated Statement of Cash Flows (10-K `0000815556-26-000009`), equal to the XBRL value
    `tools/run.py` used (1,296). Also total assets 2025 $5,052.9M on the filed balance sheet against 5,053 in the tool's
    ten-year table.
- **The lines of evidence, derived by the analyst (the brief's one departure):**
  1. From **Item 1**: the business model (local branches and customer "Sites", Fastenal Managed Inventory: 124,000
     FASTVend devices and 136,638 weighted machine-equivalent units installed, onsite locations), the customer mix (71% to
     76% manufacturing; 74% of sales under contract, 65% national accounts), the product mix (fasteners 30.5%, safety
     22.2%), the sourcing concentration in Asia, the competition paragraph, and the ten-year Sites table.
  2. From **Item 1A**: gross margin pressure from mix ("will likely continue to reduce our gross profit percentage into the
     foreseeable future"), competition from online and "major, non-traditional competitors", industry consolidation, the
     FMI advantage "could be eliminated", trade policy and tariffs, cyclical demand, the CEO transition, and the premium
     multiple risk factor.
  3. From **Item 7**: the drivers of 2025 growth (share gains, tariff pricing of 170 to 200 basis points), the gross and
     operating margins, working capital and inventory, capital spending and its 2026 step-up to $310M to $330M, the
     dividend and the absence of buybacks in 2024 and 2025, and the debt.
- `python tools/run.py FAST` arithmetic lines only (the tool's v4 material, if any, ignored per Part VII): owner earnings
  (OCF - SBC - capex) 2023 1,253, 2024 939, 2025 1,042; the tool's five-year figure 920 (capex basis); D&A 177, 175, 179;
  SBC 7, 8, 8; no securities inside operating cash, no other stock-pay line, no intangible, software or rental-fleet
  spending beside capex. The run's own owner-cash series, recast in Q4 and used in Q7, is in
  `Test Runs/_research 2026-10-12 FAST/q7_calc_output.txt`.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**; for a distributor of consumable industrial supplies whose customers reorder every week, the business
itself can be judged without the quotation. The market serves and does not instruct: "It just tells us prices."
**[M2006-077]**, and the 10-K's own risk factor that investors have "historically" given the income "a higher multiple,
or premium" is a fact about the price, not about the business. Margin of safety: if the decision needs pencil and
paper, "it’s too close to think about" **[M1996-084]**. No macro enters: the filing's account of 2025 (PMI below 50,
tariffs) is read only for what it says about the business's own pricing and share, never as a forecast
**[M2000-094]**. The analyst's habits: look for "what’s wrong" **[M2025-013]**, and write contrary evidence down at once
**[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**:
- Gross margin has fallen from about 50% (2015 and 2016, FY2016 10-K) to 48.3% (2018), 45.5% (2020) and 45.0% (2025),
  and the company says mix "will likely continue to reduce our gross profit percentage into the foreseeable future"
  (10-K 2025, Item 1A). The castle's price is being given up to the larger customer.
- The 10-K names no competitor at all; it describes the industry as "highly competitive" and warns of "major,
  non-traditional competitors" online and of easier "price discovery".
- The FMI advantage, by the company's own risk factor, "could be eliminated" if competitors respond "with highly
  competitive platforms of their own"; one supplier provides most vending equipment.
- Sourcing is "heavily concentrated" in Asia (China and Taiwan); tariffs since February 2025 raised costs.
- Leadership is changing in one year: CFO resigned April 2025, interim CFO, new outside CFO November 2025, CEO steps out
  2026-07-16; the auditor of 38 years (KPMG) was dismissed after FY2024 (no disagreements reported).
- The price: $51.55 against owner cash of about $0.81 a share (five-year average), a cash yield of about 1.6% against a
  5.60% long Treasury.
- The company bought back 1,075,000 shares in the first half of 2026 at $46.33 (10-Q), with no stated price limit.

## THE STANDING RULE
Owning this, bought for cash and sized so that a fall of half or more could be borne, puts the buyer at no risk of ruin:
"Never risk permanent loss of capital." **[L2023-005]**, and "borrowed money has no place in the investor's tool kit"
**[L2014-005]**. The rule binds the buyer's financing and sizing; nothing in the target's own balance sheet (net cash at
2026-06-30) creates a call on the buyer **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** "the first question is, can I understand it?" **[M1995-051]**, where understanding means "a reasonable fix
on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**. The
product can stay plain or opaque; what counts is "the economic dynamics of the industry" **[M2011-014]**.

**What the business is, from the filing.** A distributor: about 96% of 2025 sales were "products manufactured by other
companies" (10-K 2025, Item 1, Manufacturing). It buys fasteners and other industrial and construction supplies, much of
it from Asia, carries them in 15 North American distribution centers and 1,595 branches, and delivers them to customer
sites, increasingly into vending machines and bins it installs in the customer's plant (FMI 44.7% of 2025 sales;
"Digital Footprint" 61.4%). 71% to 76% of customers are manufacturers; the products are mostly consumed in maintaining
facilities and production ("the greater proportion of our sales is derived from products used to maintain facilities",
Item 1). No single customer reaches 5% of sales (Note 2). One reportable segment, the U.S. (Note 10).

**The key variables, and how predictable they are** **[M1998-044]**:
1. The number of customer sites spending $5,000 or more a month, and spend per site. The 10-K's own ten-year table
   (Item 1) gives both: $5k+ sites 11,236 (2016) to 19,066 (2025); their sales $2,627M to $7,311M. Steady through the
   2019 to 2020 slowdown and the 2023 to 2025 manufacturing slump (PMI below 50 in 10 of 12 months of 2025, Item 7).
2. Gross margin, set by product and customer mix: about 50% (2015, 2016) to 45.0% (2025); the company states the
   direction.
3. Operating expense leverage: operating margin 18.3% (2007), 15.3% in the 2009 trough, 20% to 21.5% every year
   2011 to 2025 (XBRL and filed statements; table in Q2).
4. Working capital (inventory about 21% of sales, receivables about 15%), which sets how much of the profit arrives as
   cash.
5. Industrial production, which the speakers would not forecast and Q1 does not need: the cycle moves the year, not the
   ten-year position **[M2000-094]**.

**Do the past statements tell me the future ones?** **[M2008-033]** Largely yes. The business has reported the same
shape for fifteen years: sales compounding, operating margin near 20%, capital spending 2% to 4% of sales, working
capital the swing item. The product (bolts, gloves, cutting tools, janitorial supplies) does not go out of date; what
can change is the channel by which a plant buys them.

**Would the insiders write it down?** **[M2000-105]** The company itself writes the forecast down in its filing: a North
American market "in excess of $140 billion", an industrial vending opportunity of "1.7 million devices", 13,000
potential Onsite locations (Item 1A, labelled its own estimates). Distribution of MRO supplies to manufacturers is not a
field where the insiders would call the ten-year forecast "That’s too hard." **[M2000-105]**.

**Is it fast-moving change?** **[M1999-063]** The threat is the online channel (Item 1A: "the emergence of online
retailers ... could result in easier and quicker price discovery"). That is a change in how a commodity is bought, which
is a castle question (Q2), not a technology whose economics cannot be seen. It does not put the ten-year economics out
of reach at Q1.

**The perimeter.** The speakers warn that "it’s easy to sort of think you understand retail" **[M2014-052]**. This is
not retail: the customer is a plant under a contract (74% of sales), and the 10-K reports the customer-site economics in
more detail than most. Doubt would mean outside **[M2002-092]**; I find none on whether the economics can be foreseen.
Whether they are good enough is Q2's question and the price is Q7's.

**VERDICT: IN.** The ten-year economics of a distributor of consumable industrial supplies to manufacturers can be
foreseen in a general way from fifteen years of filed statements and the filer's own site-level disclosure
**[M2012-065]**, **[M2000-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, where a moat is what "protects excellent returns on
invested capital" **[L2007-004]**.

**The parts table.** None needed: one reportable segment (the U.S.; the other operating segments are each under 10%,
Note 10 of the 10-K), one business model in every country. The castle is read whole **[L2008-005]**.

**What the product is.** The goods are commodities in themselves: standard fasteners, gloves, abrasives, made "by other
companies to industry standards" (Item 1). On the goods alone the customer would buy on "the low bid" **[M2017-009]**,
and the 10-K says so: price is one of the "principal competitive factors", and "The large majority of our customers
utilize multiple channels, from a single distributor or a range of distributors" (Item 1, Competition). So the castle, if
there is one, is not in the product. The filer says it is in the delivery: local stock and people at or in the plant,
"a business model not easily replicated by our competitors", the vending and bin devices "at the point of use", and a
supply chain "that is speedy, efficient, and cost-effective" (Items 1 and 7).

**The castle tests, each with its filing fact.**
- **The attacker with money** **[M2011-015]**. The field has well-funded attackers, and the filer names their kinds:
  "large national distributors", "non-traditional web-based competitors", "online retailers, whether as extensions of
  our traditional competition or in the form of major, non-traditional competitors" (Items 1 and 1A). The evidence on
  whether they have taken it is the competitor row below: the largest filer in the proxy's peer list has twice the sales
  and has not reached Fastenal's operating margin in any year of the span. This test does not pass cleanly: the industry
  is "large, fragmented, and highly competitive" (Item 1A), and "one competitor is frequently enough to ruin a business"
  **[M2012-108]**. What can be said is that fifteen years of attack have not moved the operating margin.
- **Pricing power and the agony before a rise** **[M2005-020]**. Through the 2025 tariffs the company priced 170 to 200
  basis points into sales "while continuing to maintain market price competitiveness and price/cost neutrality" and kept
  gross margin at 45.0% against 45.1% (Item 7); in the second quarter of 2026 pricing added about 290 basis points with
  operating margin unchanged at 21.0% (10-Q). "the businesses with strong competitive positions manage to pass through
  increases in raw material costs" **[M2005-017]**. Against this: gross margin has fallen about five points in ten years,
  and the company expects mix to "continue to reduce" it.
- **The low-cost position**, which the rows prize in "a low-cost producer of something that’s essential to people"
  **[M2004-091]**. The castle the filings describe is a low cost of putting a part where the
  plant uses it: 90% of product moved on the company's own trucks to branches served "two to five times per week", 12
  automated distribution centers handling "approximately 96% of our picking", Local Inventory Fulfillment Terminals for
  dense FMI territories (Item 1). The rows' form of it is the low-cost operator who passes the advantage on: "Our goal,
  however, is not to widen our profit margin but rather to enlarge the price advantage we offer customers."
  **[L1996-016]**. That is exactly the shape of the gross margin falling while the operating margin holds: the large
  customers get lower prices and the cost of serving them falls faster.
- **Would the customer still choose it over the low bid?** **[M2017-009]** The device in the customer's plant, stocked by
  the company's people, is a reason not to re-bid a glove or a drill bit item by item: 44.7% of 2025 sales ran through
  FMI devices and bins, up from 42.5% in 2024 (Item 1); 74% of sales are under contract; customer sites spending $50,000
  or more a month rose from 725 (2016) to 2,653 (2025) (Item 1 table). Service of this kind is named as an escape from the
  commodity class: "the people care enormously about service" **[M2001-014]**; and of small specialised fields, "fanaticism
  in service" **[M2011-017]**.
- **Share of mind, unit volume** **[M1997-099]**. Not a consumer brand; the brand is the service. The volume evidence is
  the site count and the share gains the filer reports in a flat market (2025: "the primary factor contributing to our
  daily sales growth of 9.1% was share gains", Item 7).
- **Ask the competitors**, "which one would it be and why?" **[M1999-130]**. Not on the public record for this run;
  scuttlebutt was not done (stated under what could not be got).
- **Widening or narrowing** **[M1999-108]**. Widening on volume and on the device base (MEUs installed 126,957 to 136,638
  in 2025; Digital Footprint 60.4% to 62.4% of December sales); narrowing on gross margin. The rows ask which matters more:
  "could the competitive advantage have been made stronger and more durable" before the year's P&L **[M2000-075]**. The
  operating margin is the reading I take: it held.
- **What could destroy it, five to fifteen years out** **[M2000-014]**: (i) online price discovery reaching the
  scheduled, contracted plant spend (the filer's own Item 1A); (ii) a rival platform of devices at equal cost (the FMI
  risk factor says the advantage "could be eliminated"); (iii) a durable break in Asian sourcing or a tariff regime that
  rivals with domestic supply escape; (iv) industry consolidation making the offering harder to differentiate (Item 1A).
  None is visible in the margins to date; each is a slow change, which "can be much harder to perceive" **[M2014-038]**.
- **Would it stand without the lord** **[L2007-006]**. The filer describes a decentralised, promote-from-within culture
  with branch-level incentives; the CEO transition of 2026 is to an internal successor of thirty years. The business does
  not appear to need a superstar.

**The competitor row.** The 10-K names no competitor by name (Item 1 and Item 1A were searched for names; none found).
The rivals are therefore taken from the company's own filed peer group in the proxy (DEF 14A 2026, Market Competitiveness
Review: ten companies "similar to our business in terms of the end markets they serve and/or their operating
characteristics"), keeping the three that are industrial distributors of the same supplies: W.W. Grainger (GWW), MSC
Industrial Direct (MSM), Applied Industrial Technologies (AIT). This is the analyst's choice, flagged. The 10-K's unnamed
"smaller regional or local distributors" and "online retailers" cannot be flagged by name because none is named. Metric:
operating income over net sales, and gross margin, from each company's own 10-K figures (XBRL transcription of the filed
statements, first-filed vintage; flagged as transcription).

| Year (fiscal) | FAST OM (GM) | GWW OM (GM) | MSM OM (GM) | AIT OM (GM) |
|---|---|---|---|---|
| 2017 | 20.1% (about 49%) | 10.1% (39.3%) | 13.1% (44.5%) | 6.7% (28.4%) |
| 2018 | 20.1% (48.3%) | 10.3% (38.7%) | 13.1% (43.5%) | 7.3% (28.8%) |
| 2019 | 19.8% (47.2%) | 11.0% (38.3%) | 11.9% (42.6%) | 6.7% (29.0%) |
| 2020 | 20.2% (45.5%) | 8.6% (35.9%) | 11.0% (42.1%) | 2.7% (28.9%) |
| 2021 | 20.3% (46.2%) | 11.9% (36.2%) | 9.3% (41.1%) | 6.3% (28.9%) |
| 2022 | 20.8% (46.1%) | 14.5% (38.4%) | 12.7% (42.2%) | 9.4% (29.0%) |
| 2023 | 20.8% (45.7%) | 15.6% (39.4%) | 12.1% (41.0%) | 10.7% (29.2%) |
| 2024 | 20.0% (45.1%) | 15.4% (39.4%) | 10.2% (41.2%) | 11.1% (29.8%) |
| 2025 | 20.2% (45.0%) | 13.9% (39.1%) | 8.0% (40.8%) | 10.9% (30.3%) |

Accessions of the latest 10-K read for each: FAST `0000815556-26-000009`; GWW `0000277135-26-000011` (FY2025); MSM
`0001003078-25-000123` (FY ended 2025-08-30); AIT `0000109563-26-000033` (FY ended 2026-06-30; its FY2026 OM 11.1%). FAST's
2017 gross margin is read from the FY2016 10-K's quarterly figures (about 49.8% in the fourth quarter of 2016) and the
FY2020 10-K's 48.3% for 2018; it is marked "about".

Read over the whole span: Fastenal's operating margin is the highest of the four in every year, and the only one that did
not fall in 2020 or in the 2023 to 2025 manufacturing slump. MSM, the closest in product (metalworking and MRO), has fallen
from 13.1% to 8.0% across the same years. The wider span the filings allow for Fastenal alone: operating margin 18.3%
(2007), 19.2% (2008), **15.3% (2009, sales down 17.5%)**, 18.9% (2010), then 20.1% to 21.5% every year 2011 to 2025. One
full downturn (2009) cut the margin by four points and did not break it.

**The field's returns over the last full cycle.** Fastenal's pre-tax operating income on the capital employed (equity
plus debt less cash, from the filed balance sheets): 2016 $796M on $2,210M (36%); 2020 $1,142M on $2,892M (39%); 2025
$1,656M on $3,792M (44%). These are excellent returns by any reading of the filings, not ordinary ones; the rivals' margins
are lower but, in words, decent for distributors. The field is not one of the "terrible businesses" that "beat each
other’s brains out" in the rows' sense: its leading filers earn steady margins. The castle that protects only ordinary
returns does not describe this name.

**The verdict reasoning.** The castle is a low-cost, high-service delivery system, built over decades ("In 1993, we began
to aggressively add additional product lines"; vending from 2008, traction from 2011) and lodged in the customer's plant.
It has protected a near-constant operating margin through attack, a downturn, a pandemic, an inflation and a tariff shock.
Its weakness is that the protected figure is the operating margin, not the price: the customer is handed part of the
advantage each year, by the company's choice and by the large customer's leverage. The rows separate the moat that is
maintained from the one that "must be continuously rebuilt" **[L2007-005]**; on fifteen years of filings, this one has been
maintained by daily work, the kind that adds strength "If we are delighting customers, eliminating unnecessary costs"
**[L2005-010]**, and I judge it so, with the gross margin as the line to watch. It is judged, not measured
**[M1999-108]**; "You still know they’re fat" **[M2007-024]**.

**VERDICT: IN.** The castle stands on the evidence of the whole span and against the three filing rivals; it is not shown
open **[M2011-015]**, and its future can be judged to the degree Q2 asks **[M2000-019]**. Contrary evidence carried
forward: the five-point fall in gross margin, the unnamed online attackers, and no scuttlebutt.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"Has it earned high returns on capital?" **[M1995-051]**, measured on "the capital actually needed in the business"
**[M2010-090]**, as "return on tangible assets" **[M2011-060]**.

**Return on the capital needed.** Capital employed (equity plus borrowings less cash, filed balance sheets; goodwill,
intangibles and other assets together only $137.9M at 2025, Note 10, so the figure is nearly all tangible):

| Year-end | Equity | Debt | Cash | Capital employed | Operating income | Pre-tax return |
|---|---|---|---|---|---|---|
| 2016 | 1,933 | 390 | 113 | 2,210 | 796 | 36% |
| 2020 | 2,733 | 405 | 246 | 2,892 | 1,142 | 39% |
| 2025 | 3,944 | 125 | 277 | 3,792 | 1,656 | 44% |

Before crediting a high return the rows rule out "a cyclical peak in earnings, a monopolistic position, or leverage"
**[L1994-009]**: 2025 is not a peak by the filer's account (manufacturing PMI below 50; "Market conditions were sluggish"),
the company has no monopoly (a fragmented market in which "no company has a significant portion"), and it carries almost
no debt. Equity is not shrunk by buybacks (none in 2023 to 2025; small ones in 2018, 2020, 2022 and 2026), so the return
is not manufactured.

**What the added capital earned.** From 2016 to 2025 capital employed rose $1,582M and operating income rose $860M: about
54% pre-tax on the added capital, about 41% after the 24.0% tax rate of 2025. "whether that’s good or bad depends on what
we earn on that incremental $130 million over time" **[M2001-019]**; here the incremental return is higher than the
average.

**Reinvestment to stand still, and to grow.** Two kinds of capital go in.
- **Fixed assets.** Net capital spending 2021 to 2025: $148M, $162M, $161M, $214M, $231M (total $916M) against
  depreciation of $160M, $166M, $167M, $165M, $169M (total $826M): spending ran about 1.1 times depreciation. The filing
  names five categories (FMI hardware, distribution centers and facilities, IT, vehicles, manufacturing equipment, Item 7)
  but does not divide them into maintenance and growth. The rows' stand-in, "Every year we spend amounts equal to our
  depreciation charge simply to stay in the same economic place" **[L2000-035]**, read with "the depreciation charge is
  not inappropriate in most companies to use as a proxy" **[M1998-127]**, puts maintenance near depreciation (about $168M
  in 2025) and growth spending near the excess. That is my guess, as the rows ask a guess to be **[M2000-144]**, not a
  filed figure. The step-up guided for 2026 ($310M to $330M net) includes replacing the Atlanta hub, which is maintenance
  of capacity as much as growth.
- **Working capital.** This is the heavier draw. From 2020 to 2025 receivables rose $476M ($769M to $1,245M) and
  inventory $410M ($1,338M to $1,748M), payables $110M, against sales up $2,553M: about 31 cents of trade working capital
  for each added dollar of sales. The profit does not all end the year as cash; part of it is "your profit sitting in the
  yard" **[M2008-036]**. Owner cash (Q4) averaged $932M over 2021 to 2025 against average net income of $1,115M: about
  84% converts.

**The growth arithmetic.** Each added dollar of sales has needed about 31 cents of working capital and a few cents of
fixed assets, and has carried about 20 cents of operating profit. That is the "second-best business" of the rows, one
that "takes more money, but the rate at which you invest — reinvest — the money to get that growth is a very
satisfactory rate" **[M1998-081]**; it is not the gruesome one. The rate cannot run past its base forever: "if you trace
out the mathematics of it, you bump into absurdities" **[M1999-067]**; Q7 caps the growth carried accordingly. The
company has paid out about 80% of net income as dividends (2025: 79.8%, Item 7), which says it earns more than it can
use at those rates **[M2004-089]**.

**WEIGHS FOR.** High and rising returns on tangible capital without leverage, and a satisfactory return on the
working capital that growth requires **[M1998-081]**, **[M2010-090]**. Against: growth is not free; about a sixth of
earnings is held back in receivables, inventory and plant each year. (The "little or no debt" criterion is applied at
Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first**, ten year-ends, before the income account: "balance sheets over an 8 or 10 year period
before I even look at the income account" **[M2025-032]**. USD millions; XBRL first-filed vintage from `tools/run.py`,
read against the filed statements of the FY2016, FY2020, FY2022, FY2023 and FY2025 10-Ks (accessions in Step 0); sales
added from the filed income statements.

| Year-end | Assets | Equity | Cash | Receivables | Inventory | Debt | Sales | Recv/sales | Inv/sales |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 2,669 | 1,933 | 113 | 500 | 993 | 390 | 3,962 | 12.6% | 25.1% |
| 2017 | 2,910 | 2,097 | 117 | 608 | 1,093 | 415 | 4,391 | 13.8% | 24.9% |
| 2018 | 3,322 | 2,303 | 167 | 714 | 1,279 | 500 | 4,965 | 14.4% | 25.8% |
| 2019 | 3,800 | 2,666 | 175 | 742 | 1,366 | 345 | 5,334 | 13.9% | 25.6% |
| 2020 | 3,965 | 2,733 | 246 | 769 | 1,338 | 405 | 5,647 | 13.6% | 23.7% |
| 2021 | 4,299 | 3,042 | 236 | 900 | 1,524 | 390 | 6,011 | 15.0% | 25.3% |
| 2022 | 4,549 | 3,163 | 230 | 1,013 | 1,708 | 555 | 6,981 | 14.5% | 24.5% |
| 2023 | 4,463 | 3,349 | 221 | 1,088 | 1,523 | 260 | 7,347 | 14.8% | 20.7% |
| 2024 | 4,698 | 3,616 | 256 | 1,109 | 1,645 | 200 | 7,546 | 14.7% | 21.8% |
| 2025 | 5,053 | 3,944 | 277 | 1,245 | 1,748 | 125 | 8,201 | 15.2% | 21.3% |

**What moved and why.** Equity roughly doubled ($1,933M to $3,944M) and is nearly all retained earnings ($3,868M of
$3,944M at 2025; paid-in capital $115.5M): the business was built from its own profits, not from share issues or
acquisitions. Goodwill and intangibles are folded into "Intangibles and other assets" of $137.9M (Note 10): purchased
goodwill is immaterial. Debt peaked at $555M in 2022 (inventory build) and fell to $125M; the company borrows against
the seasonal and working-capital swing and repays it. Inventory against sales improved from about 25% to about 21%
after 2022 (the filer: more stock held centrally in the distribution centers, 46% against 41% the year before, Item 7).
Receivables against sales rose from 12.6% to 15.2% over the ten years, which the filing ties to growth with larger
customers ("growth in sales to our customers", Item 7); the allowance for credit losses is small ($5.3M at 2025) and bad
debt expense was $4.6M. Nothing builds "suspiciously high", and inventory is not "out of line" with sales; it improved
**[M1995-064]**.

**What the figures do not say.** Operating lease liabilities of $316.9M (branches, trucks) sit outside debt; the
branch rents are in occupancy expense and so in the cash figure. Vending devices are capitalised in "Shelving,
industrial vending, and equipment" ($1,524.6M gross, Note 3) and depreciated over 3 to 10 years, so their cost reaches
the income account through depreciation, which is "almost always true costs" **[L2015-004]**.

**The real costs.**
- Depreciation $168.5M and amortization $10.7M (2025): charged; net capital spending exceeded depreciation (Q3).
- Stock pay: options only, $8.4M expensed in 2025; diluted shares 1,150.3M against basic 1,147.6M, so dilution is about
  0.2%. The cost is counted, as "all forms of compensation" must be **[L2021-003]**. New RSU plans were approved in April
  2026 and will add expense from now on (8-K `0000815556-26-000027`).
- Incentive pay is cash and is in SG&A: the 2025 rise in employee costs is stated ("significantly higher bonuses and
  commissions", Item 7).
- No restructuring charges, no special items, no EBITDA and no adjusted earnings in the 10-K, the 10-Q or the 8-Ks read.
  The EBITDA covenant was in fact removed from the credit agreement in June 2026 (8-K `0000815556-26-000035`).
- Tax: 24.0% in 2025, 23.7% in 2024, cash taxes $398.8M against expense $396.6M; no shelter to price.

**What the accounts say of management.** The MD&A explains in plain terms what moved and why, including misses: the
Digital Footprint reached 62.4% of December sales against a goal of 66% to 68%, "attributable to lower volume through our
FMI devices"; capital spending fell below its own range "due to delayed projects". That is the clear speech the rows
count as a plus, a management that "does explain to you in clear terms what’s going on" **[M1994-018]**. The company
publishes operating goals (device signings, Digital Footprint) and a capital spending range, not earnings guidance; it
missed one goal in 2025 and said so. Nothing here is the habit of always reaching "declared targets" **[L2002-041]**. The
auditor changed after 38 years, KPMG to PwC, with no disagreements and no reportable events (8-K/A
`0000815556-25-000068`); PwC's 2025 opinion is clean, with one critical audit matter (revenue recognition, for effort).

**The recast owner cash** (feeds Q7): net cash from operations, less stock pay, less capital spending net of disposal
proceeds, less cash paid for businesses (none in 2021 to 2025; $125M in 2020, $58.7M in 2017), all from the filed cash-flow
statements. USD millions:

| Year | OCF | Stock pay | Net capex | Owner cash | % of sales | Before net interest (after tax) |
|---|---|---|---|---|---|---|
| 2021 | 770.1 | 5.6 | 148.2 | 616.3 | 10.3% | 623.6 |
| 2022 | 941.0 | 7.2 | 162.4 | 771.4 | 11.1% | 781.7 |
| 2023 | 1,432.7 | 7.3 | 160.6 | 1,264.8 | 17.2% | 1,269.9 |
| 2024 | 1,173.3 | 8.0 | 214.1 | 951.2 | 12.6% | 952.6 |
| 2025 | 1,295.9 | 8.4 | 230.5 | 1,057.0 | 12.9% | 1,057.5 |
| **Average** | | | | **932.1** | | **937.1** |

The swing is working capital, as the filer says year by year: 2021 "significant growth in working capital ... significant
product inflation"; 2023 "reduced demand for working capital as a result of an improved supply chain" (FY2021 and FY2023
10-Ks). Variants beside: gross capital spending (proceeds not netted) averages $920.3M; depreciation and amortization in
place of capital spending averages $939.5M. The earlier years, for the cycle (same construction): 2013 $209M, 2014 $303M,
2015 $376M, 2016 $333M, 2017 $409M, 2018 $499M, 2019 $597M, 2020 $814M.

**VERDICT on the accounts: IN** (no confusion, no suspicion **[M1995-063]**); **WEIGHS FOR**: simple accounts, every real
cost charged, no adjusted figure, plain explanation of misses **[M1994-018]**. Carried to Q5: no make-the-numbers habit
found; one change of auditor and one of CFO in 2025, recorded.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet; the two yardsticks are "how well they run the business", read
against "the hand they were dealt" **[M1994-008]**, and how they treat the owners, read in the proxy: "see how they
treat themselves versus how they treat the shareholders" **[M1994-009]**.

**The first yardstick: the record against the hand dealt.** The hand: a commodity product, a fragmented field, a
cyclical manufacturing customer, Asian sourcing, and since 2025 a tariff shock. The record: sales $3,869M (2015) to
$8,201M (2025), operating margin held at 20% to 21% every year while the gross margin fell five points, net cash at mid
2026, and the three filing rivals below it in every year (Q2). The leadership is long-tenured and internal: of the eleven
executive officers, nine joined between 1992 and 2003; the incoming CEO joined in 1996 and ran the Canadian region and
international sales before sales overall (10-K, Executive Officers).

**Integrity: the tells looked for, and what was found.**
- Restatements: none; the proxy states no accounting restatement and no clawback balance (DEF 14A, Executive Incentive
  Recoupment).
- Related-person transactions: "There were no related person transactions during 2025 required to be reported" (DEF
  14A).
- Accounts that confuse or dance: none found (Q4). No adjusted earnings, no EBITDA, no earnings guidance; the misses of
  2025 are told plainly. The rows' worry about a management that hits every declared target does not arise; this one
  missed a stated goal and said why.
- Emphasis on the stock price: the 10-K carries a risk factor on the "premium" multiple, and the company split its stock
  two-for-one in 2019 and again in 2025. A split is not a tell of dishonesty in the rows; it is weighed under Q6 Part B as
  the owners' question it is. No "price of a stock posted in the lobby" **[M2004-067]** kind of fact was found in the
  filings.
- The change of auditor after 38 years: the 8-K/A reports no disagreements and no reportable events, and KPMG's letter
  was filed as Exhibit 16.1. Recorded, not a tell on this evidence.
- The CFO's resignation effective 2025-04-16: the 8-K of 2025-04-10 appoints an interim CFO and gives no reason; the
  departing CFO's 2025 options were forfeited (DEF 14A). No disagreement is stated; no reason is stated either.
  Recorded.
- How they talk about mistakes: the forbidden-word taboo of **[L2024-003]** is not present; the culture statement in the
  10-K names "learn from mistakes" among the expectations of employees, and the MD&A names the shortfalls.

On this record I have no doubt about integrity of the kind that closes the file: "If you’ve got doubts, forget it."
**[M2013-088]**; I have none.

**Love of the business, and after being paid.** For a hired management of a public company the test reads as what the
person does for the company rather than what the company does for the person; the evidence available is tenure (thirty years for the new CEO), a modest
fixed salary ($750,000 for the CEO since at least 2023; $650,000 for the new CEO), and pay that falls when profit falls
(the CEO's cash incentive was $75,250 in 2024, when pre-tax income fell, against $2,569,000 in 2025; DEF 14A Summary
Compensation Table). The outgoing CEO stays as strategic adviser until early 2028 (8-K `0000815556-25-000123`).

**The succession question.** "Who besides you would be the ideal person to run this, and why?" **[M2014-059]**. The board
named the successor seven months before the transition, from inside, and set a handover year; the rows' board duty is
to have the next leader "ready to take over tomorrow" **[L2011-001]**. Met on the evidence.

**Ability: what it shows in.** A long record, not a promise; sense in the reports; focus (no diversifying acquisitions:
"Historically, substantially all of our growth has been organic", Item 1A). The great business needs less of it **[M1996-037]**,
and this one has shown it does not depend on one person.

**VERDICT on integrity: IN** **[M2013-088]**. **Ability WEIGHS FOR** **[M1994-008]**. Recorded for a later reading: the
2025 changes of CFO and auditor, both without a stated cause beyond the filings quoted.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
**The retention test.** "We test the wisdom of retaining earnings by assessing whether retention, over time, delivers
shareholders at least $1 of market value for each $1 retained." **[R1995-009]**, over a span such as "three or four
years" **[M1998-110]**. Over 2021 to 2025: net income $5,575.9M, dividends paid $4,269.3M (filed cash-flow statements),
buybacks $237.9M (2022: 5,000,000 pre-split shares at about $47.58, FY2022 10-K); kept in the business about $1,069M.
Market value: about 1,148.3M shares (574.2M before the 2025 split, FY2020 10-K) at $24.415 at 2020-12-31 = about $28.0B;
1,148.1M shares at $40.13 at 2025-12-31 = about $46.1B (closes from the aggregator chart, split-adjusted, flagged; the
2026-01-02 close of $40.44 in that series matches the 10-K's own stated grant-date close of $40.44). Market value rose
about $18.0B against about $1.1B kept. The market leg passes by a wide margin. The intrinsic leg passes too: the kept
dollars bought working capital and devices that carried owner cash and operating income higher (Q3: about 54% pre-tax on
the added capital). The forward question, "Can you keep using all of the capital you generate, effectively, for a very
long time?" **[M2010-097]**: the company does not try to; it pays out about 80% and keeps what growth needs. That is the
policy the rows ask of a business that earns more than it can use at high rates **[M2004-089]**.

**Dividends.** Regular quarterly dividends raised most years, with specials in 2020 and 2023 ($0.19 a share, 2023, Note
5). The company reports what share of net income it returned ("an average of 73.2%" over five years, 10-Q), but states
no fixed payout ratio; the payout follows what the business does not need. Read as "clear, consistent and rational"
**[L2012-015]**.

**Buybacks.** Small and occasional: 2018, 2020, 2022, and 1,075,000 shares in the first half of 2026 at an average of
$46.33 (10-Q `0000815556-26-000041`), under a 2022 authorization of a number of shares with no stated price. A programme
that names no price weighs against unless the prices paid sit at or below the bottom of the Q7 range, the "intrinsic
value, conservatively-calculated" of **[L1999-023]**; the value of a repurchase is "entirely purchase-price dependent"
**[L2016-002]**. *Written back from Q7 (committed with it):* the bottom of the Q7 range is **$14.66** a share (top $27.75). The purchases
of the first half of 2026, at an average of $46.33, sit above the top of the range, more than three times the bottom; the
2022 purchases, at about $23.79 on today's share basis, sit above the bottom. (The 2018 and 2020 purchases, at about $6.44
and $16.27 on today's basis, are not judged against today's range, which values a larger business.) The buyback with no
stated price **weighs against**: the shares were bought above value, conservatively calculated **[L1999-023]**.

**Issuance and deals.** No stock-paid acquisition in the span; the few acquisitions were small and for cash ($58.7M in
2017, $125.0M in 2020; none 2021 to 2025). Share count 1,142.5M (2023 basic) to 1,147.6M (2025 basic), option exercise
only. The one STOP of Part A, an all-stock deal by an undervalued acquirer, does not arise. The serial-issuer tell
**[L2014-015]** does not arise.

**Part A WEIGHS FOR** on retention and dividends **[R1995-009]**, **[M2004-089]**, with one mark against written back
from Q7: the 2026 buybacks at prices above the top of the value range **[L2016-002]**.

### Part B: the pay, the board and the owners
**Pay tied to what the person controls** **[M2003-019]**. Every executive's cash incentive is a percentage of the amount by
which company-wide quarterly pre-tax income exceeds the same quarter of the year before (the new CEO: 1.75%, 8-K/A
`0000815556-26-000043`; the CFO: 0.50% of pre-tax and 0.35% of net income, 8-K `0000815556-25-000121`), plus a
supplemental quarterly bonus under a "return on asset" plan for improvement in asset management. Branch and field staff
are paid on sales growth, gross or pre-tax profit and "prudent management of working capital" (10-K, Item 1). The capital
element the rows ask of a business that ties up working capital is there in the ROA plan; "you get what you reward for"
**[M2016-083]**. The flaw: a bonus on the increase over last year's quarter pays twice for recovering lost ground. The
CEO's incentive was $75,250 in 2024, when pre-tax income fell, and $2,569,000 in 2025, when it recovered and grew; over
the two years the owners' pre-tax income rose about 8.7% from 2023 to 2025 while the incentive was paid as if on two
separate gains in one of them. It is a partner on the way down in cash **[L1994-020]**, and paid more than evenly on the
way back up.

**Options.** Granted each January to all eligible employees at an exercise price set slightly above the market (January
2026: $41.00 against a $40.44 close, Note 5), no step-up for retained earnings **[L1994-021]**. With about 80% of earnings
paid out, little is retained for the option to ride on; the dividend conflict of options (holders gain from retention,
not from dividends) runs against the option holders here, not the owners. Expense $8.4M, dilution about 0.2%. From 2026,
RSU plans add restricted stock for employees and directors.

**Sizes.** CEO total pay $4,183,328 for 2025 (salary $750,000), 88 times the median employee; the named officers' base
salaries below the peer median by the committee's own account (DEF 14A). Not the overreaching the rows warn of.

**The board.** Twelve directors (from June 2026), nine of the eleven on the 2026 ballot independent; an independent chair
(Scott A. Satterlee, chair since April 2021) separate from the CEO, so the rows' worry about a chief executive who "is also
Chairman" **[L2014-026]** does not arise. Directors' holdings are mostly options; several hold purchased shares in their own
trusts (50,000 for the chair; 40,000 each for three others), "purchasing shares with their savings, rather than simply
having been the recipients of grants" **[L2019-008]** in part. Directors as a group own 3,265,322 shares and options,
under 1%. The succession was planned and disclosed early (Q5).

**The owners.** No earnings guidance, no adjusted figure, the same 10-K for every owner. Two splits (2019, 2025): the rows
state Berkshire's own rule, "we do not consider splitting the stock a pro-shareholder move" **[M1997-019]**, which tests
another company only by inversion; it weighs slightly against, as a choice about which owners to court.

**Part B WEIGHS FOR**, with two marks against: the recovery-paying bonus formula and the splits **[M2003-019]**,
**[L1994-020]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
answered by how much, how sure, how soon, and the rate, "the yield on long-term U.S. bonds" **[L2000-021]**, held as a
range, since "working with a range of possibilities is the better approach" **[L2000-024]**. Arithmetic in
`Test Runs/_research 2026-10-12 FAST/q7_calc.py`, output in `q7_calc_output.txt` beside it.

**The rate.** 5.60%, the 30-year Treasury par yield of 2026-10-09 (Step 0), nominal.

**The cash input (Q4's recast).** Five-year average, 2021 to 2025, of owner cash after every real cost (operating cash
less stock pay less capital spending net of disposals; no acquisitions in the window): **$932.1M** after interest
(equity-only basis), **$937.1M** before net interest after tax (all-equity basis; net interest was $0.7M to $13.6M a
year). Working-capital growth is inside it, as specific (d) requires.

**Is an end year of the window aberrational (specific (a))?** "If either year was aberrational, any calculation of growth
will be distorted." **[L2005-003]**. The owner-cash series as a share of sales: 2015 9.7%, 2016 8.4%, 2017 9.3%, 2018
10.0%, 2019 11.2%, 2020 14.4%, **2021 10.3%**, 2022 11.1%, 2023 17.2%, 2024 12.6%, **2025 12.9%**. The aberrational
years on the filer's own description are 2020 and 2023, when working capital was released ("weaker demand from our
customers resulted in working capital being a net source", FY2021 10-K; "reduced demand for working capital as a result
of an improved supply chain", FY2023 10-K). 2021, the first year, was a year of working-capital growth "as we support
growth in our customers' operations as well as ... significant product inflation" (FY2021 10-K): that is what this
business's growth years look like (2017 to 2019 sat at 9% to 11%), so I do not judge it aberrational, and 2025 is a
middling year in a "sluggish" market. The literal window is therefore the central figure. Beside it, the cycle
construction for anyone who reads 2021 as a trough: owner-cash troughs in 2016, 2021 and 2024; the last full cycle
2021 to 2023 averages $891.7M (all-equity), growth between the 2016-2020 and 2021-2023 averages 13.8% a year.

**The growth shown, and the cap (specific (f)).** Aggregate owner cash grew from $616.3M (2021) to $1,057.0M (2025),
**14.44% a year**. Carried ten years from the $937.1M base it would reach $3,610M, which against sales grown at the
business's own sales rate (8.07% a year, $6,010.9M to $8,200.5M, 2021 to 2025) would be 20.2% of sales; the highest share
of sales owner cash has reached in the filings read is 17.2% (2023, a release year). The shown rate therefore traces to
an absurdity **[M1999-067]** and is cut to the sales growth: **8.07% carried for ten years**, then zero nominal growth, no
rate above the discount rate after year ten **[M1997-095]**. Both rates are written down; the uncut case is shown below.
(The 8.07% includes tariff pricing of 170 to 200 basis points in 2025 and inflation in 2021 and 2022; it is not real
growth, and carrying it ten years is generous.)

**Specifics not engaged:** (b) no decline; (c) no acquisitions in the window and none signed or closed since (the
organic pair equals the total pair); (e) the filing does not divide capital spending into maintenance and growth, so all
spending is charged in the central case; the maintenance-at-depreciation variant is shown beside and barely differs,
since spending ran about 1.1 times depreciation.

**The range** (USD; per share on 1,147.498M shares; the all-equity central figure adds the net cash of $84.7M at
2026-06-30):

| Case | All-equity value | Per share (central) | Equity-only per share |
|---|---|---|---|
| No growth (bottom) | $16,734M | **$14.66** | $14.51 |
| Shown growth cut to 8.07% for ten years, then flat (top) | $31,764M | **$27.75** | $27.54 |
| Width | 1.90 to 1 | | |

Beside it (not deciding): cycle base $13.95 to $26.42; depreciation in place of capital spending $14.69 to $27.83; gross
capital spending $14.40 to $27.26; net income in place of owner cash (working-capital growth not charged) $17.43 to
$33.02; the uncut 14.44% growth for ten years, $45.70 at the top.

**Value range: $14.66 to $27.75 a share against $51.55.**

**The floor tested first** (CONVENTION, Q7, adopted 2026-10-10). The expected return at $51.55 (all-equity market value
$59,068M): the growth case returns **3.18%** a year, the no-growth case 1.59%; the net-income case 3.73%; even the uncut
14.44% growth case returns 5.06%, below the long Treasury itself. To earn the floor of about ten percent, owner cash would
have to grow about 26% a year for ten years and then hold; to earn the long Treasury rate alone, about 16% a year. No case
the analyst could defend earns the floor at the price, so the file closes OUT whatever the width: "there’s just a point
at which we drop out of the game" **[M2003-149]**. The width test (1.90 to 1, under three) would also have sent it to the
price test rather than TOO HARD, and the price sits above the top of the range, which closes OUT by the floor convention
in any case **[M2009-005]**.

The rows that pull the other way were weighed and do not reach this far. Paying up for an outstanding business is the
costliest omission in the speakers' own count, "being reluctant to pay up a little for a business I knew was really
outstanding" **[M1997-083]**, and "a wonderful business at a fair price" **[M2003-040]** is preferred; but the price here
is about twice the top of the range, not a little above it, and "You can turn any investment into a bad deal by paying
too much." **[M2019-015]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent instead of the long
rate (no growth $9,371M; growth $16,369M, all-equity), averaged, plus net cash: **$11.29 a share on the all-equity basis
(central)**; **$11.16 on the equity-only basis** beside it. Owner cash after the company's own income tax (24.0%
effective 2025; no carryforward or credit to price), no conversion. No cheap price is reported.

**VERDICT: OUT.** The price of $51.55 is above the top of the value range ($27.75) and no case earns the floor at it
**[M2003-149]**, **[M2009-005]**. Q8, Q9, Q10 and Q12 are NOT REACHED.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). Fact for the record under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. No named business of the rows (casinos, tobacco, distributor-loading schemes, gambling) is involved; noted
under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**: value range **$14.66 to $27.75** a share (all-equity, central; literal window 2021 to 2025, growth cut to
the 8.07% sales rate by specific (f)) against **$51.55**; the growth case returns 3.18% at the price and no defensible case
earns the floor **[M2003-149]**. Q1 IN, Q2 IN, Q3 weighs for, Q4 IN and weighs for, Q5 integrity IN and ability weighs
for, Q6 weighs for with two marks against (the recovery-paying bonus formula and buybacks above the range). Reporting
figures: value range as above; fair price **$11.29** all-equity (central), $11.16 equity-only. No integrity facts that
call for the flag; the 2025 changes of CFO and auditor are recorded in Q5.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box unchanged **[M1997-127]**.
- **Q8 (the bond):** owner cash of $937.1M against an all-equity market value of $59,068M is a 1.59% cash yield against
  the 5.60% 30-year Treasury (2026-10-09); the growth case returns 3.18% (Q7).
- **Q9 (debt and exposures):** borrowings $120.0M at 2026-06-30 against cash $204.7M; a $835M unsecured revolver
  maturing 2031-06-18 and a note shelf cut from $900M to $600M (8-K `0000815556-26-000035`); covenants of interest cover
  at least 3.00 and total leverage at most 3.00 (3.50 after a qualified acquisition of at least $750M), the latter step-up
  written into the facility in June 2026. Peak quarterly borrowings in 2025 were $365M (Item 7). Operating lease
  liabilities $316.9M. Product liability named as a risk, partly insured (Item 1A); no material litigation (Note 11).
  Supplier concentration: one supplier above 5% of inventory purchases; "primarily one supplier" for vending equipment
  (Item 1). Sourcing concentrated in China and Taiwan.
- **Q10:** nothing beyond Q7.
- **Q12:** the business sells industrial and safety supplies to manufacturers, contractors and governments; none of the
  rows' named businesses.

## CONVENTIONS OF THIS RUN, AND WHAT COULD NOT BE GOT
- **CONVENTION of this run:** when the 10-K names no competitor, the rivals for Q2 are taken from the filer's own peer
  group in its proxy, keeping those in the same line of business (here GWW, MSM, AIT of ten). Rationale: the brief's rule
  assumes the 10-K names rivals; the proxy is the filer's own filed statement of who is comparable, and the choice of three
  is written down so another analyst can check it.
- **CONVENTION of this run:** capital spending is taken net of the proceeds of routine disposals (the filer's own "net
  capital expenditures"), with gross spending shown beside. Rationale: the proceeds are recurring vehicle sales in the
  normal course (Item 7); the difference is about $12M a year and moves no conclusion.
- **CONVENTION of this run:** the all-equity owner cash adds back net interest (expense less income) after tax at 24%.
  Rationale: Q7's basis asks for owner cash before interest while the net cash is credited separately; the adjustment is
  under $11M a year.
- Prices for the retention test's market leg (year-end 2020 and 2025) are aggregator closes, outside operator rule 5's
  "live quotes only"; flagged, and checked against the one filed close available ($40.44 on 2026-01-02, Note 5).
- **Could not get:** scuttlebutt (competitors, customers, former employees) is not on the public record read; the
  competitors' figures are XBRL transcriptions of their filings, not read from their filed statements; the 2009 to 2015
  Fastenal figures are XBRL first-filed vintages, not read from the filed statements; the reason for the CFO's 2025
  resignation is not stated in any filing read.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `60441178`, before the first `tools/run.py` call); written
      question by question; committed after each (Step 0 `a097aad1`, Q1 `19be8c4d`, Q2 `3fae87ba`, Q3 `ebf8ba62`, Q4
      `8d718968`, Q5 `d59da53b`, Q6 `d8c19826`, Q7 with the Q6 write-back `0e3c3b8f`, the rest after).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was present when the
      run began and was not touched by the analyst (the dispatching session holds it). The fold is the dispatcher's.
- [x] Blind rule: no other run file, holding review, `PORTFOLIO.md`, register or reading list was opened or searched. One
      act is declared under contamination: a listing of `Test Runs/` filtered for this company's name before the
      template was copied (it returned nothing). Session-context items seen are declared there and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row
      (`Test Runs/_research 2026-10-12 FAST/idcheck.py`: 0 problems); no E-ids. Every filing fact carries its document and
      accession; numbers are from filings or labelled.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy (the net-income case
      appears only as a labelled variant beside the range, never as the input); the sovereign from the US Treasury; the
      price and the year-end closes flagged as aggregator figures.
- [x] Contrary evidence was written down as found (foundations list; Q2's gross margin; Q6's bonus formula and
      buybacks); facts for later questions are under AFTER THE STOP. No integrity flag is called for on the evidence.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (a) on a working-capital business.** The rule makes owner cash the series that defines the cycle, but this
business's owner cash swings on working capital (released in 2020 and 2023, built in 2021 and 2022), so the "troughs" it
finds (2016, 2021, 2024) are inventory cycles, not business cycles, and the rule does not say whether a growth year with
heavy inventory building is "aberrational". I took the literal window as central (the end years sit inside the range of
normal years as a share of sales) and showed the cycle construction beside; here both lie far below the price. (2)
**Specifics (e) and (f) together.** (e) forbids charging all spending and also capping the growth that spending bought;
(f) then requires cutting an absurd owner-cash growth rate to the sales rate. With working capital charged in full and the
growth cut by (f), the central case does both; the text does not say which yields. Immaterial here (even the uncut case
returns 5.06% at the price), but it would decide a closer name. (3) **The competitor rule** in the brief assumes the 10-K
names rivals; Fastenal's names none, and the run had to confess a convention (the proxy peer group). (4) **Nominal growth
inside the ten years.** The cut to the sales rate carries tariff and inflation pricing as growth for ten years, while
growth after year ten is zero nominal; the framework does not say whether the ten-year rate should be real. (5) **The
retention test's market leg** needs historical prices, which operator rule 5 confines to live quotes from aggregators; the
framework does not say where a filed historical price is to come from when the filing gives none.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(pending)
