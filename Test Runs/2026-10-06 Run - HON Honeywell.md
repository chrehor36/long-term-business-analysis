# Company Run — Honeywell International Inc., now operating as Honeywell Technologies (NASDAQ: HON) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch (commit `87d4824`). Every
judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes
the run and later questions are marked NOT REACHED. Research folder: `Test Runs/_research 2026-10-06 HON/` (tool outputs,
`fetch.py`, `peers.py` and its output, `owner_cash.py` and its output, `check_ids.py`; raw filings under `cache/`,
gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the queue register, the prepped reading list and `tools/alerts.json` were not opened,
and no attempt was made to learn whether the operator holds or wants this name.

**CONTAMINATION, declared.** (1) For form only, I read one other company's v5 run of 2026-10-05 (ETN Eaton); a grep showed
it does not mention Honeywell. (2) `tools/run.py` and `Screens/cover_shares.py` printed their usual lines; nothing in them
was a verdict on this name. (3) My training memory holds a picture of Honeywell as a diversified aerospace-and-industrial
conglomerate of about 650 million shares; the filings below replace it: the company I am asked to price is a different
business from the one in my memory (STEP 0). No earlier run or research folder for HON was opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING

**What is being bought, first, because it changes every line below.** Honeywell has split itself in three. Advanced
Materials was spun off as Solstice Advanced Materials on 2025-10-30 (10-K FY2025, Note 22). Aerospace was spun off as
Honeywell Aerospace Inc. (HONA) effective 12:01 a.m. on 2026-06-29, one HONA share for every two HON shares, and at 12:02
a.m. the same day HON effected a **one-for-two reverse split** (8-K filed 2026-06-29, accession `0000773840-26-000084`,
Items 1.01, 2.01, 5.03; press release Ex. 99.1: "This reduced the number of issued and outstanding shares [...] from
approximately 634 million as of March 31, 2026 to approximately 317 million"). The company "now operates as Honeywell
Technologies", a "pure-play automation company" of three segments, Building Automation, Process Automation and
Technology, and Industrial Automation (same 8-K). On 2026-06-04 its quantum-computing subsidiary Quantinuum went public
and was deconsolidated; HON keeps a 48% equity-method stake carried at $7,260M (10-Q Q2 2026, Note 2). Two businesses of
Industrial Automation, Productivity Solutions and Services and Warehouse and Workflow Solutions, are held for sale under
agreements expected to close in Q3 2026 (10-Q MD&A). Johnson Matthey's Catalyst Technologies was bought on 2026-07-17 for
$1,750M (10-Q Note 3). **So the company priced at $214 has existed in this shape for fourteen weeks; it has no filed
stand-alone cash-flow statement, and its first quarter reported on this basis (Q3 2026) is not yet filed.**

- **Price:** $214.14 (close 2026-10-05, live quote via `tools/run.py`; aggregator, flagged per operator rule 5, used
  for the quote only). It is a post-reverse-split, post-spin price.
- **Shares:** one class of common stock. 10-Q for the quarter ended 2026-06-30, filed 2026-07-23, accession
  `0000773840-26-000124`, cover: "There were 316,940,010 shares of Common Stock outstanding at June 30, 2026." The same
  figure on the cover of the 10-Q/A filed 2026-07-24 (`0000773840-26-000127`, filed "solely for the purpose of correcting
  typographical errors in the presentation of backlog by business segment"), which is what `python Screens/cover_shares.py
  HON` printed: 316,940,010. The count is after the reverse split.
- **Market cap:** $214.14 × 316.94M = **$67.87B**.
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-17, `0000773840-26-000013` (Item 1, 1A, MD&A, the
  statements, Notes 19, 21, 22); 10-Q Q2 2026, `0000773840-26-000124` (statements, Notes 1-3, 18, MD&A, liquidity) and its
  10-Q/A `0000773840-26-000127`; 8-K 2026-06-29 `0000773840-26-000084` with Ex. 99.1 (press release), Ex. 99.2
  (supplemental segment information recast for Honeywell Technologies, 2024 to Q1 2026, "preliminary") and Ex. 99.3 (pro
  forma condensed statements: balance sheet at 2026-03-31, operations 2023, 2024, 2025, Q1 2026); proxy DEF 14A filed
  2026-04-10, `0000773840-26-000029`; Honeywell Aerospace's Form 10 amendment 2, Ex. 99.1 information statement, filed
  2026-06-08, `0001628280-26-041399` (the audited combined statements of the business that left).
- **One figure cross-checked against the filed statement:** 2025 net cash provided by operating activities, $6,408M in
  `tools/run.py` (XBRL) and $6,408M on the filed Consolidated Statement of Cash Flows (10-K FY2025, p.57). Agrees. The
  same statement shows why the tool's figure cannot be used: it is the total including discontinued operations ($333M),
  and its continuing part ($6,075M) still contains Aerospace.
- **`tools/run.py HON`, arithmetic lines only** (Part VII). Its owner-earnings table (mean 4,573 to 4,888) and its 7.20%
  "yield" are computed on the old three-business Honeywell against the new one-business share count: **a defect for
  this name, recorded, and not used**. Its ten-year balance-sheet table is used at Q4 as the history of the old company.

**Owner cash after every real cost, for the business now being bought** (USD millions; `owner_cash.py`, output in
`owner_cash_output.txt`). No filed statement gives it, so it is reconstructed two ways and both are shown:

*Method A, cash by difference:* HON's continuing operating cash flow (10-K) less Aerospace's audited carve-out operating
cash flow (Form 10), less stock pay, less capital spending, each also by difference.

| year | HT OCF | stock pay | capex | owner cash as filed | legacy one-offs in it | ex one-offs | ex one-offs, interest on post-spin debt |
|---|---|---|---|---|---|---|---|
| 2023 | 1,475 | 124 | 354 | **997** | NARCO buyout −1,325 | 2,322 | 2,454 |
| 2024 | 2,574 | 115 | 383 | **2,076** | none | 2,076 | 2,274 |
| 2025 | 2,370 | 113 | 482 | **1,775** | Resideo +1,590, asbestos −1,428 | 1,613 | 2,052 |
| mean | | | | 1,616 | | 2,004 | **2,260** |

*Method B, owner earnings from the pro forma income account* (Ex. 99.3 net income from continuing operations
attributable, plus depreciation and amortization by difference, less capital spending by difference, plus the non-cash
impairments, less the 2025 Resideo gain after tax, less pension income after tax):

| year | pro forma NI | D&A | capex | impairments | Resideo gain a/t | pension income a/t | owner cash |
|---|---|---|---|---|---|---|---|
| 2023 | 1,236 | 702 | 354 | 0 | 0 | 322 | **1,262** |
| 2024 | 1,302 | 806 | 383 | 267 | 0 | 377 | **1,615** |
| 2025 | 1,368 | 976 | 482 | 1,038 | 784 | 313 | **1,803** |
| mean | | | | | | | **1,560** |

Method B is not a net-income proxy: it is net income with the non-cash charges added back and all capital spending
taken off, and it leaves working capital out. Its weak points are stated: impairments are added back before tax because
the filings do not give their tax effect (generous), and pension income is taken off after tax at the 21% US statutory
rate (CONVENTION: the rate is used only to put a non-cash income line on an after-tax footing; the filings give no
effective rate for it). Method A's weak points: the carve-out allocates corporate costs and taxes "as if" Aerospace stood
alone (the auditor names the carve-out adjustments a critical audit matter), its income-tax line shows $206M paid in 2025
against $627M of tax expense, and the interest column restates HON's continuing interest ($1,344M in 2025) to the pro
forma figure for the debt Honeywell Technologies keeps ($788M), after tax at the same 21%. The two methods bracket the
base at **$1.56B to $2.26B a year**, about 1.45 to 1. Stock pay is a real cost and is out in both. **Only three years exist
for this entity**, not the five the Q7 convention asks for; this is confessed at Q7.

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. First, no macro enters **[M2000-094]**: the press release of 2026-06-29 sells the new
company as positioned "to lead the industrial sector’s transition from automation to autonomy"; that is a forecast of an
industry and is kept out of every question below. Second, who is paid to tell you **[M2020-037]**: the separation was
advised by Goldman Sachs (lead) and Morgan Stanley, with two law firms (same press release), and the recast and pro forma
figures that describe the new company are management's, furnished, "preliminary and could change" (Ex. 99.2, Ex. 99.3).
Third, the market serves and does not instruct **[M2006-077]**: the $214 quote says nothing about what a fourteen-week-old
company earns. **Contrary evidence, written down as found** **[M1997-127]**: (a) Building Automation grew organically 8%
in 2025 and 9% in Q2 2026 with margins rising to 27.1% (10-Q), which is evidence for a castle, not against it; (b) Process
Automation and Technology organic sales fell 3% in 2025 and 1% in Q2 2026, with "a decline in catalyst shipments", and
its organic figures for 2025 exclude an "Other" item of 6% to 14% of sales a quarter that the exhibit does not explain
(Ex. 99.2); (c) Industrial Automation's two hardware businesses were impaired ($724M of goodwill in 2025) and put up for
sale; (d) the new company's GAAP operating margin on the recast was 5.9% in 2025 and 11.3% in 2024 against a segment
margin of 17.6% and 17.3% (Ex. 99.2), so "segment profit" leaves out much; (e) the 2025 pro forma net income of $1,368M
contains an $802M pre-tax gain from selling Resideo's future reimbursements back to it (10-K Note 19).

## THE STANDING RULE
Bought for cash, unlevered, at a size the buyer can hold through a fall of half, a share of Honeywell Technologies puts
the buyer at no risk of ruin; the rule binds the buyer's financing and sizing, and borrowing to buy is ruled out
**[L2014-005]**, **[M2012-081]**. Nothing about the target changes this line; its own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**; the product may stay
opaque if "the economic dynamics of the industry" are understood **[M2011-014]**. Honeywell Technologies is three
segments and a stake, so it is read by its parts (CONVENTION, framework section VI; **[M2023-031]** stays open against it).

**The parts, from the filings** (2025 net sales and segment profit as recast, Ex. 99.2 of `0000773840-26-000084`;
descriptions from 10-Q Q2 2026 Note 4 and the 10-K Item 1):
- **Building Automation** ($7,367M sales, $1,953M segment profit, 26.5%; 37% of segment sales, 44% of the three
  segments' profit): fire detection, building controls and optimization software, energy management, access control,
  video, "complemented by installation, maintenance, and upgrades"; Products sold "primarily through an industry-leading,
  highly capable, channel partner network", and Solutions. It includes Carrier's former access-solutions business bought
  in 2024 (the 13% and 8% "acquisitions" lines of Ex. 99.2 in Q1 and Q2 2025).
- **Process Automation and Technology** ($6,437M, $1,542M, 24.0%; 32% and 35%): plant control systems in "Projects"
  and "Aftermarket", and UOP's "licensed process technology, equipment, engineering catalyst, adsorbents"; Sundyne pumps
  and compressors (bought 2025-06-06 for $2,160M) and, from 2026-07-17, Johnson Matthey's Catalyst Technologies
  ($1,750M).
- **Industrial Automation** ($6,111M, $896M, 14.7%; 31% and 20%): gas detection, sensors, switches, custody-transfer
  metering, smart energy, thermal and burner controls; until their sale in Q3 2026, also Productivity Solutions and
  Services (mobile computers and scanners, $1,132M of 2025 sales under the old segment) and Warehouse and Workflow
  Solutions ($933M) (10-K Item 1). After those sales Industrial Automation is roughly two-thirds of its 2025 size.
- **The 48% stake in Quantinuum** (quantum computing; IPO 2026-06-04; carried at $7,260M; equity loss of $265M in Q2
  2026 alone, 10-Q Note 2).

**Key variables** **[M1998-044]**: (1) for Building Automation and the control-system half of Process Automation, the
retention of an installed base whose replacement, service and upgrade work comes back to the incumbent; (2) price
against cost; (3) for UOP, the licensing and catalyst flow tied to refinery and petrochemical capital spending, which is
cyclical in level but whose technology position is decades old; (4) for the rest of Industrial Automation, share in
certified safety and measurement products against Emerson, MSA, Itron, TE and others named in the 10-K. The level of
demand in any of them is a forecast and is not a variable I am allowed to use **[M2000-094]**.

**Doubts written down.** (a) The company's own risk factors say it must "defend our market share against an
ever-expanding number of competitors, including many new and non-traditional competitors" and "prevent commoditization
of our products", and that "Emerging technology, such as generative and agentic artificial intelligence, is complex and
rapidly evolving" (10-K Item 1A); its stated strategy is a move "from automation to autonomy". Change is "more of a
threat [...] than an opportunity" **[M1999-063]**, and where future technology "could hurt the business as it presently
exists [...] it won’t make it through the filter" **[M1998-008]**. I read the threat as real but slow for fire, life
safety and plant control, whose products are certified, specified and embedded in buildings and plants for decades; the
reading is mine and is the place a second analyst could differ. (b) Quantinuum is a start-up in a fast-moving technology,
outside the circle by the rows ("Start-ups are not our game" **[L2007-015]**; **[M1998-008]**). It does not decide the
whole's earnings: under the equity-method convention (framework Q4) its owner cash is the dividends it pays, which are
none, so it contributes nothing to owner cash and is carried at Q7 as an asset of unknowable worth, zero at the bottom of
the range and its carrying value at the top. By the by-parts convention it therefore does not put the whole outside, but
a doubt about it is recorded **[M2002-092]**. (c) Test 3, "do I understand enough about this business so that the
financial statements will tell me [...] what the future financial statements are going to look like" **[M2008-033]**:
for this entity there are three years of pro forma income statements, two years and a quarter of recast segments called
"preliminary", and no stand-alone cash-flow statement (STEP 0). That is a question about the numbers, and it is answered
at Q4, not here.

**VERDICT: IN.** The parts that make the earnings (Building Automation, plant control and UOP, certified sensing and
measurement) are installed-base and licensed-technology businesses whose ten-year position can be pictured in the sense
of **[M2000-037]**; the industry is not one whose insiders would refuse to write the forecast down **[M2000-105]**. The
fast-technology part (Quantinuum) is a stake that does not produce the earnings and is valued separately. Doubt (a) is
carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**.

**The record, segment by segment** (segment profit margin; segment definitions changed in 2023 and again in 2026, so the
lines are not one series):

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|
| Building Technologies (2020-22) / Building Automation (2023-) | 21.2% | 22.4% | 24.0% | 25.4% | 25.7% | 26.5% | 26.7% |
| Process Automation and Technology (recast) | | | | | 24.7% | 24.0% | 22.9% |
| Industrial Automation (recast, 2026 composition) | | | | | 16.4% | 14.7% | 17.1% |
| Honeywell Technologies, total segment profit after corporate (recast) | | | | | 17.3% | 17.6% | |

Sources: 10-K FY2022 Note 22 (`0000773840-23-000013`) for 2020-2022; 10-K FY2025 Note 22 (`0000773840-26-000013`) for
Building Automation 2023 ($1,529M on $6,031M); Ex. 99.2 of `0000773840-26-000084` for the recast 2024-2025; 10-Q Q2 2026
MD&A for H1 2026. Organic sales growth, recast: Building Automation +8%, +8%, +7%, +8% in the four quarters of 2025, +8% in
Q1 2026 and +9% in Q2 2026; Process Automation and Technology +3%, +6%, −6%, −3% in the quarters of 2025, −6% in Q1
2026 and −1% in Q2 2026;
Industrial Automation −18%, −14%, −9%, −3% through 2024, then about flat; the whole company −3% in 2024 and +2% in 2025
(Ex. 99.2; 10-Q).

**The castle tests, each with its filing fact.**
1. *The castle questions and the lord* **[M1995-038]**. Building Automation: fire detection, controls and access systems
   installed in buildings and serviced for their lives, sold through a channel of installers; the reason the customer
   comes back is the installed base and its certification, not a person. Process Automation: plant control systems and
   UOP's licensed process technology and catalysts, where the 10-K speaks of "a century of domain expertise" and a "vast
   installed base". Neither depends on "the genius of the lord" **[M1995-038]**; Honeywell has had three chief executives
   since 2017 and the segments' margins rose through them.
2. *The attacker with money* **[M2011-015]**. The competitors the 10-K names are the same incumbents, not entrants:
   Johnson Controls, Schneider Electric and Siemens in buildings; Clariant, Flowserve and Topsoe against UOP; Dematic,
   Emerson, Itron, MSA, Rockwell, TE and Zebra in industrial automation (10-K Item 1, Competition). No instance found in
   the filings read of a new entrant at scale. Against this, the same section says: "Our products face considerable price
   competition."
3. *Pricing power and the agony before a rise* **[M2005-020]**. No filing read describes a price increase in the three
   remaining segments in terms (the Q2 2026 MD&A credits Building Automation's growth to "higher demand", not price, and
   names price only for Aerospace, which has left). The test is therefore answered only by the margin: Building
   Automation's margin rose five and a half points over 2020-2026 through the 2021-2023 cost inflation, which reads as
   costs passed through **[M2005-017]**; Process Automation's fell from 24.7% to 22.1% in the latest quarter on "a
   decline in catalyst shipments". **Weighs for in buildings, undecided in process.**
4. *Would the customer still choose it over the low bid?* **[M2017-009]**, **[M2001-014]**. Fire detection and plant
   safety and control are in the safety path of a building or a refinery; the parachute row is the nearest analogy,
   "I don’t think if you were buying a parachute you’d want to take the — necessarily take the low bid" **[M2001-014]**.
   Against it, the 10-K's own words on price competition, and the two hardware businesses (mobile computers and
   scanners; warehouse automation) where the customer plainly did take the other bid: their goodwill was impaired by
   $724M in 2025 and they are being sold (10-K, Impairment of goodwill; 10-Q MD&A).
5. *Ask the competitors* **[M1999-130]**: the row below, from their own filings.
6. *Widening or narrowing* **[M1999-108]**, **[M2000-075]**. Buildings: widening on the margin record, six years in a row,
   with organic growth of 7% to 9% a quarter since 2025. Process: flat to narrowing over the two and a half recast years,
   with aftermarket sales falling ($926M against $946M in Q2; $1,753M against $1,789M in H1) and growth bought (Sundyne,
   Johnson Matthey, and the LNG business bought in 2024). Industrial: narrowed until the losing parts were cut out.
7. *What could destroy or reduce it, five to fifteen years out* **[M2000-014]**: (a) software and "agentic" AI moving
   the value of building and plant control from the hardware maker to whoever owns the data layer, which is the risk the
   10-K names and the strategy the company has chosen to meet; (b) a fall in refining and petrochemical investment, which
   the 10-K names for Process Automation; (c) the channel: Building Automation's products reach the customer through
   independent installers. None of these is shown happening in the filings read; they are named, not evidenced.

**The competitor row** (each company's own 10-K XBRL facts, `peers.py`, output in `peers_output.txt`; operating income
where tagged, otherwise pre-tax income from continuing operations, marked *; fiscal years end in September for EMR, ROK,
JCI):

| company (10-K accession of the latest year) | metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Honeywell Technologies (pro forma, Ex. 99.3; operating income before impairments from Ex. 99.2) | pre-tax margin | 10.5% | 9.8% | 8.5% |
| Honeywell Technologies | operating margin before impairments | n/a | 12.7% | 11.1% |
| Rockwell Automation (`0001024478-25-000116`) | operating margin | 21.3% | 19.3% | 20.4% |
| Emerson Electric (`0000032604-25-000087`) | pre-tax margin* | 19.1% | 11.5% | 16.3% |
| MSA Safety (`0000066570-26-000005`) | operating margin | 12.9% | 21.5% | 19.8% |
| Zebra Technologies (`0001628280-26-007668`) | operating margin | 10.5% | 14.9% | 13.0% |
| Itron (`0000780571-26-000033`) | operating margin | 5.9% | 10.8% | 13.2% |
| Johnson Controls (`0000833444-25-000097`) | pre-tax margin* | 5.0% | 6.6% | 8.3% |

Honeywell Technologies' GAAP margins sit below Rockwell's, MSA's and Emerson's and above Johnson Controls' and Itron's.
Its segment margins (26.5% in buildings, 24.0% in process) are before the corporate costs, amortization, stock pay,
repositioning and pension items that the GAAP line carries; the gap between the two (17.6% total segment margin against
11.1% operating margin in 2025) is itself a finding for Q4. Honeywell Technologies' pre-tax return on its tangible assets
cannot be measured on a like basis: its only balance sheet is the pro forma at 2026-03-31, with tangible assets of about
$18.4B net of cash, of which $2.4B is held for sale and $4.6B is "other assets" (Ex. 99.3); on that, operating income
before impairments of $2,209M (2025) is about 12% pre-tax, against Rockwell's 26% and MSA's 24% on the same measure.

**Verdict.** The castle is shown standing in Building Automation on the evidence (a margin widened every year from 2020 to
2026 and organic growth through 2025-2026), and in Process Automation it stands but shows no widening; the part of
Industrial Automation whose castle was crossed is being sold, which is the record of a moat that failed there, not of the
whole. Nothing read shows the castle of the remaining whole "filling in", which is what would close it OUT
**[M2011-015]**, and the risk named in (a) is a risk, not evidence; nor is the future beyond judging **[M2000-019]**,
since the parts that make the profit are slow-changing. **VERDICT: IN**, with the price-competition sentence of the 10-K,
the falling process aftermarket and the GAAP margins below the better peers carried forward as the strongest contrary
facts.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**. Physical capital is light: capital spending
  by difference was $354M, $383M and $482M in 2023-2025 (1.8% to 2.4% of sales), against depreciation by difference of
  $264M, $247M and $271M (10-K and Form 10 cash-flow statements). On the only balance sheet of this entity (pro forma,
  2026-03-31, Ex. 99.3), tangible assets net of cash and short-term investments are about $18.4B, and operating income
  before impairments of $2,209M (2025) is about 12% pre-tax on them; the figure is diluted by $2.4B held for sale and
  $4.6B of "other assets", so the operating businesses earn more on what they use, but no filing lets me take those out
  reliably. Read with the warning about "a cyclical peak in earnings, a monopolistic position, or leverage"
  **[L1994-009]**: none of the three is visible here.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. My maintenance guess, stated as a guess:
  about depreciation plus the amortization of software, i.e. most of the $350M to $480M spent; the rest of the growth has
  been bought, not built. The 10-K guides "approximately $1.3 billion for capital expenditures in 2026" for the whole
  pre-spin company; Aerospace's own Form 10 guides $647M of it, which leaves roughly $650M for Honeywell Technologies,
  a rise on the $482M of 2025.
- **What the added capital earned** **[M2001-019]**, **[M2023-081]**. The growth capital went into acquisitions: Carrier's
  access-solutions business, $4,913M (2024-06-03, about $725M of annual sales on the sales contributions the 10-K
  reports, so about 6.8 times sales); Air Products' LNG business, $1,843M (2024-09-30); Sundyne, $2,160M (2025-06-06);
  Johnson Matthey's Catalyst Technologies, $1,750M (2026-07-17); together about $10.7B in two years (10-K Note 3; 10-Q
  Note 3). Over the same span the company's net sales went from $19,407M (2023) to $19,945M (2025), and total segment
  profit from $3,327M (2024) to $3,507M (2025), while the PPE business ($1,157M of proceeds) left. The pro forma balance
  sheet carries goodwill and intangibles of $23.1B against Honeywell shareowners' equity of $16.7B. The increment of
  profit on the capital added since 2023 cannot be separated from the filings, and what can be seen is small.
- **The growth arithmetic** **[M2003-120]**, **[M1999-067]**: the business has not grown its sales in the three years of
  its record (1.4% a year, with acquisitions in it); any growth carried into Q7 above that would be a forecast, not a
  record.
- **UNDECIDED**: a business that needs little physical capital, the first kind in **[M1998-081]** on that measure, but
  whose growth has been bought at prices that put the purchased capital above the owners' equity, with no visible return
  on it yet **[M2011-060]** (goodwill counts "because we paid for it" in judging the allocation, which Q6 weighs).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]**. Ten year-ends of the old Honeywell (first-filed XBRL values as printed by
`tools/run.py`, accessions in `run_py_output.txt`; 2024 and 2025 checked against the filed balance sheet of the 10-K
FY2025), then the one balance sheet of the new company. USD millions.

| year-end | assets | equity | goodwill | intangibles | cash | receivables | inventory | debt on the face | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 54,146 | 19,369 | 17,707 | 4,634 | 7,843 | 8,177 | 4,366 | 15,775 | 28,710 |
| 2018 | 57,773 | 18,180 | 15,546 | 4,139 | 9,287 | 7,508 | 4,326 | 16,214 | 33,978 |
| 2020 | 64,586 | 17,549 | 16,058 | 3,560 | 14,275 | 6,827 | 4,489 | 22,384 | 39,905 |
| 2022 | 62,275 | 16,697 | 17,497 | 3,222 | 9,627 | 7,440 | 5,538 | 19,570 | 45,093 |
| 2023 | 61,525 | 15,856 | 18,049 | 3,231 | 7,925 | 7,530 | 6,178 | 20,443 | 47,979 |
| 2024 | 75,196 | 18,619 | 21,825 | 6,656 | 10,567 | 7,819 | 6,442 | 31,099 | 50,835 |
| 2025 | 73,681 | 13,904 | 21,079 | 6,736 | 12,487 | 7,621 | 6,162 | 34,580 | 50,964 |
| **HT pro forma 2026-03-31** | 52,879 | 16,693 | 18,056 | 5,012 | 10,977 | 4,736 | 1,735 | 20,888 | 53,262 |

(2017, 2019 and 2021 are in the research file and change nothing below. "Debt on the face" is short-term borrowings plus
current and long-term debt; the pro forma line is Ex. 99.3: commercial paper $4,630M, current maturities $3,094M,
long-term debt $13,164M.)

**What the figures say.** (1) Retained earnings rose by $22.3B over nine years while shareowners' equity fell by $5.5B:
the earnings went out, and more, through repurchases (treasury stock at cost of $43.9B at 2026-03-31, Ex. 99.3) and the
spin-offs. (2) Debt on the face more than doubled, from $15.8B to $34.6B, almost all of it from 2023, when the
acquisitions (Q3) and the repurchases were financed with borrowing (10-K: "$10,408 million of long-term debt proceeds" in
2024, "primarily to fund our recent acquisitions"). (3) Goodwill and intangibles rose from $22.3B to $27.8B and, for the
new company alone, stand at $23.1B against $16.7B of equity. (4) Receivables were flat for a decade on a sales line that
was roughly flat too; inventory rose, almost all of it Aerospace's (the pro forma removes $4.6B of $6.4B). **What they
cannot say:** what the new company earns in cash. Its balance sheet exists only as a pro forma at one date, built by
management "for illustrative and informational purposes only", and its cash flows exist in no filing (STEP 0).

**The real costs.**
- *Depreciation* is a real cost **[R1996-023]**; capital spending exceeded depreciation in every year (Q3), so owner cash
  deducts all capital spending.
- *Stock pay* is a real cost **[L2015-003]**, deducted in both methods of STEP 0. The company's "segment profit" excludes
  it ($153M for the new company in 2025) and also excludes "pension and other postretirement service costs" ($57M),
  which is pay (Ex. 99.2 reconciliation).
- *Restructuring* recurs: the new company's "Repositioning, Other" was $147M in 2024 and $390M in 2025, and $159M of
  charges in H1 2026 (Ex. 99.2; 10-Q cash-flow statement); the old company paid $280M, $189M and $153M in cash for it in
  2023-2025 (10-K). "to tell owners year after year, "Don't count this," [...] is misleading" **[L2016-007]**,
  **[L1998-031]**. Both owner-cash methods carry it.
- *Amortization of acquired intangibles* ($509M for the new company in 2025): customer relationships, technology and
  trademarks of Access Solutions and the rest, amortized over 10 to 20 years; "Some truly deplete over time while others
  never lose value" **[L2012-003]**. Method B adds all of it back, which flatters; Method A is unaffected.
- *Pension income*: the cash-flow statement takes out $396M of non-cash "Pension and other postretirement income" in
  2025 (10-K). It is income from assumed returns, not cash **[M2001-026]**; both methods leave it out of owner cash.
- *Legacy liabilities*: the NARCO asbestos buyout ($1,325M, 2023), the Bendix asbestos divestiture ($1,428M, 2025) and
  the Resideo termination ($1,590M received, 2025, with an $802M pre-tax gain) are real one-time cash items; they are shown
  and taken out in Method A and the gain is taken out of Method B. The new company no longer receives Resideo's
  reimbursements of 90% of its environmental spending ($105M in 2025, 10-K), so its future environmental costs are its
  own; neither method adjusts for this.

**Adjusted earnings in the filer's own mouth.** The furnished recast leads with "Segment profit" and "Adjusted earnings
per share", excluding amortization, impairments, divestiture costs, debt restructuring and, in segment profit, stock pay
and pension service cost (Ex. 99.2). Adjusted EPS is 40% of the chief executive's annual bonus formula (proxy, ICP
metrics), and "Adjusted ICP EPS" excludes "restructuring charges" and "material unusual, infrequent, and extraordinary
items" (proxy, ICP note 1). This is "a management that regularly attempts to wave away very real costs by highlighting
"adjusted per-share earnings"" **[L2016-006]**. No EBITDA figure was found in the documents read. In the other
direction, the adjusted EPS removes pension income (−$0.10 in Q1 2026, Ex. 99.2), which is the conservative choice.

**The make-the-numbers habit and the two-tell line (CONVENTION).** The proxy records that 2025 adjusted EPS guidance was
raised three times "from $10.30 to $10.65" and that operations "consistently exceeded expectations"; the ICP target of
$10.30 was beaten with $10.89 (proxy, CFO qualitative considerations and ICP table). One year of guidance beaten; I did
not assemble earlier years, so the habit is not established **[L2002-041]**. The adjusted-earnings framing is one tell. A
second was looked for in the list the framework gives (reserves that move, prepaid or deferred accounts building
**[M1995-064]**, profits on both sides of a contract): other current assets rose from $1,182M to $1,779M in H1 2026, in
a half that included the spin, and the filing does not explain it; I record it as unexplained, not as a tell, since
spin-related receivables and taxes are the obvious candidates and I could not test them. One tell is a weighing
**[M1994-018]**.

**Confusion?** "when the accounting confuses you, I would just tend to forget about it" **[M1995-063]**; "people don’t
obfuscate with numbers, usually, without a purpose" **[M2003-029]**. The difficulty here is not obfuscation: the company
furnished recast segments, audited carve-out statements of the business that left, and pro forma statements, and the two
reconstructions of STEP 0 agree to within about 1.45 to 1. It is the difficulty of a company that has changed shape three
times in a year, and it is real: the base for Q7 is a range, not a figure, and rests on three years where the convention
asks for five.

**VERDICT on confusion: IN**, narrowly (the accounts can be read and a bounded recast made); **WEIGHS AGAINST** on the
adjusted-earnings framing tied to pay, the recurring restructuring, and the absence of any filed cash-flow statement for
the business being bought **[L2016-006]**, **[L2016-007]**. The recast owner cash fed to Q7 is the STEP 0 band, $1.56B to
$2.26B a year.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. Vimal Kapur has been "Chief Executive Officer of Honeywell International Inc.
  since June 2023 and Chairman of the Board since June 2024", after a year as president and chief operating officer
  (proxy, director biography). His
  record is the transformation: about $11B of acquisitions ("Deploy $11 billion to accretive acquisitions", proxy), three
  separations, the asbestos and Resideo settlements, and $3.8B of repurchases in 2025. The hand dealt and what was made of
  it, for the business now being bought: organic sales −3% in 2024 and +2% in 2025, Building Automation's margin rising,
  the Industrial Automation hardware businesses impaired and sold (Q2). The proxy itself says that while operating
  performance "was strong, current and three-year total shareowner return (TSR) was substantially lower than the median
  of our compensation peer group and XLI", and the 2023-25 performance units paid 59% of target.
- **How they treat themselves against the owners** **[M1994-009]**. Chief executive's total pay in the summary
  compensation table: $20,381,435 for 2025 (salary $1.6M, stock awards $10.9M, options $3.6M, cash incentive $3.5M). On
  top, February 2025 "one-time equity awards" to five officers, 60% options and 40% restricted units, vesting "50% at the
  completion of the Honeywell Aerospace spin-off and 50% at the one-year anniversary", granted "to incentivize leadership
  for the successful completion of Honeywell’s critical and unique transformational activities" (proxy, Transaction
  Awards): pay for completing transactions, which the rows warn pushes "toward deals" **[M2014-076]**. The bonus pays 40%
  on adjusted EPS and 40% on free cash flow, and the 2025 cash incentive paid 126% of target for the chief executive.
- **Tells of dishonesty** (the framework's Q5 list). None found in the documents read: no restatement, no reserve
  release found, no stock price in the lobby, the goodwill impairment of the failing hardware businesses was taken and
  named plainly (10-K MD&A, "Impairment of goodwill increased due to an impairment charge related to the classification of
  the Productivity Solutions and Services and Warehouse and Workflow Solutions businesses as held for sale"), and the
  August 2026 8-K moves the Building Automation chief, whose segment widened its margin, to run Process Technology, whose
  chief leaves (`0000773840-26-000130`), which reads as acting on a weak unit **[M2010-081]**. The language of the
  documents is the language of the consultant ("from automation to autonomy", "Honeywell Technologies Forge
  intelligence layer"), which the rows call "a big turnoff" when it "looks like it came out of the same consulting firm"
  **[M1998-038]**; I note it and do not make it a tell of dishonesty. Integrity is applied on doubt **[M2013-088]**; I have none from the record,
  read as a marketable-stock reader reads **[M2007-081]**.
- **Love of the business** **[M2000-098]**: not judgeable from documents.
- **The chair.** The chief executive is also chairman, with an independent lead director (proxy); the rows name the cost:
  "how hard it is to replace a mediocre CEO if that person is also Chairman" **[L2014-026]**.
- **VERDICT on integrity: IN**; **ability UNDECIDED**: a record of deal-making and portfolio surgery whose results for the
  remaining business are not yet in the numbers, and a total-return record the proxy itself calls below its peers.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *Retention test* **[R1995-009]**, **[M1998-110]**. The old company kept nothing: over 2023-2025 it paid $8,733M of
  dividends and $9,174M of repurchases against net income of $16,184M (10-K cash-flow statement), and borrowed for the
  acquisitions (Q4). The market leg was not tested: no year-end price was read in the filings, and I did not take one
  from memory. The forward question, "Can you keep using all of the capital you generate, effectively" **[M2010-097]**,
  is answered so far by acquisitions whose return is not visible (Q3).
- *Buybacks* **[L1999-023]**, **[L2016-002]**. The stated policy names no price. It is "to maintain our commitment to
  reduce share count by at least 1% per year" (10-K, letter section) and "to offset the dilutive impact of employee
  stock-based compensation plans [...] and (ii) to reduce share count via share repurchases as and when attractive
  opportunities arise" (10-K Item 5; the same words in the Q2 2026 10-Q). The rows rule out both purposes by name:
  "dilution by itself is a negative and buying back your stock at too high a price is another negative. So it has to be
  related to valuation." **[M2016-049]**; buying to offset options **[M2014-008]**. Prices paid: 19.2M, 8.0M and 18.1M
  pre-split shares for $3,715M, $1,672M and $3,819M in 2023, 2024 and 2025 (about $193, $209 and $211 a share; 10-K
  statement of shareowners' equity), and 2.2M post-split shares for $1,004M in H1 2026 (10-Q). The convention's test
  (prices paid against the bottom of the Q7 range) cannot be run cleanly: every share bought was a share of the old
  company, carrying Aerospace (and, before October 2025, Advanced Materials), whose value this run does not estimate.
  On the stated purpose alone, **weighs against**.
- *Deals* **[L2014-012]**, **[L2017-004]**. All paid in cash or borrowed money, so the all-stock STOP **[L2009-019]** does
  not arise. Value given against value got cannot be read from the filings (Q3: about $10.7B for businesses whose profit
  is not disclosed separately; Access Solutions at about 6.8 times sales). The proxy calls them "accretive acquisitions";
  "even a high-priced deal will usually boost per-share earnings if it is debt-financed" **[L2017-004]**. The board's
  rationale for combining the chair and chief executive roles is "the decision-making speed and agility required to
  drive an ambitious organic and inorganic growth agenda" (proxy): the forces that "push toward deals" **[M2014-076]**.
- **Part A WEIGHS AGAINST**: a buyback with no price and a dilution purpose, and $10.7B of debt-financed acquisitions in
  two years whose returns cannot yet be seen.

**Part B, the pay, the board, the owners.**
- *Pay tied to what the person controls* **[M2003-019]**, **[L1996-018]**. Annual bonus: adjusted EPS 40%, free cash flow
  40%, sales 20% (proxy, ICP); performance units: three-year revenue, three-year average ROI, segment margin and relative
  TSR, 25% each (proxy, 2025-2027 plan). The ROI measure is a charge for capital, which is the right kind of metric, but
  it is "Adjusted at measurement to exclude the impact of corporate transactions during the period" (proxy), so the
  capital spent on acquisitions does not count against the people who spend it. Relative TSR and options pay on the
  share price. The transaction awards pay for completing the spin-offs (Q5).
- *The board* **[M2007-120]**, **[L2014-026]**: chair and chief executive combined, with a lead director; the board's
  stated reason is speed in deal-making (above).
- **Part B WEIGHS AGAINST, mildly**: a capital measure that exempts the acquisitions, adjusted earnings in the bonus,
  and pay for transactions.

## Q7 — WHAT IS IT WORTH? STOP.
**The construction (CONVENTION, framework Q7 and section VI).** Owner cash after every real cost, averaged, carried at the
growth shown and capped by Q3, for ten years, then zero nominal growth, discounted at the sovereign 5.66% **[L2000-021]**,
**[M1996-025]**; the ends are the no-growth and shown-growth cases **[L2000-024]**, **[L1999-027]**. Arithmetic in
`owner_cash.py`, output `owner_cash_output.txt`. Two departures from the convention, confessed: **(1) a three-year
average, not five**, because the entity has three years of figures (STEP 0); **(2) the base is a band, not a figure**:
$1,560M (Method B) to $2,260M (Method A, one-offs out, interest on the post-spin debt), and the two ends of the range are
built on the two ends of the band, so that the range carries the reconstruction's uncertainty as well as the growth.
The 48% Quantinuum stake is counted at zero at the bottom of the range and at its carrying value of $7,260M at the top
(Q1, doubt (b)); the equity-method convention gives it no owner cash.

**The growth shown, and the Q3 cap.** The two methods disagree in sign. Method B rises from $1,262M (2023) to $1,803M
(2025), 19.6% a year; Method A, one-offs out, falls from $2,322M to $1,613M. Method B's rise is the shape of its own
adjustments (no impairments to add back in 2023, $1,038M added back in 2025, before tax), not of the business; and 19.6%
for ten years would carry owner cash to about $9.3B, near half of present sales, which traces to an absurdity
**[M1999-067]**, **[M1997-095]**. A base year "aberrational" in either direction distorts the rate **[L2005-003]**. The
growth the business has actually shown is in its sales, $19,407M (2023) to $19,945M (2025), **1.4% a year**, with
acquisitions inside it. The shown-growth case is capped there; the uncapped case is shown for the reader.

**COMPUTATION** (USD; per share on 316.94M shares):

| case | base | growth yrs 1-10 | value at 5.66% | per share | + Quantinuum at carrying value | value at 10% | per share |
|---|---|---|---|---|---|---|---|
| no growth, low base | $1,560M | 0% | $27.6B | **$87** | $110 | $15.6B | $49 |
| no growth, high base | $2,260M | 0% | $39.9B | $126 | $149 | $22.6B | $71 |
| shown growth (sales, Q3-capped), high base | $2,260M | 1.4% | $44.5B | $140 | **$163** | $24.8B | $78 |
| uncapped Method-B growth, low base | $1,560M | 19.6% | $127.5B | $402 | $425 | $61.2B | $193 |

**Value range: $87 to $163 a share** (bottom: no growth, low base, Quantinuum at zero; top: capped growth, high base,
Quantinuum at carrying value), **against $214.14.** Width 1.9 to 1, inside the three-to-one line. The uncapped case is
shown and not used.

**Expected return at the price** (the discount rate at which each case equals the market value of $67.87B; ex-Quantinuum,
the operations' price of $60.61B): no growth, low base **2.3%** (2.6% ex-Quantinuum); no growth, high base 3.3% (3.7%);
capped growth, high base **3.7%** (4.2%). All are below the 5.66% Treasury. Only the uncapped 19.6% case reaches 9.3%
(10.1% ex-Quantinuum).

**The floor** (CONVENTION, about ten percent pre-tax **[M2003-149]**, **[L2002-020]**, **[M1994-004]**). Owner cash here is
after the company's own income tax; I read the 10% as the buyer's return before the buyer's tax, since the 2002 row's own
parenthesis converts it to an after-corporate-tax figure of six and a half to seven percent, the corporation there being
the holder (the row's fraction is a damaged character), and I discount after-tax owner cash at 10%. On the other reading
the floor would be lower; at 8% the capped high case is worth about $99 a share, $121 with the stake, so the verdict does
not turn on it.

**Reported at the owner's request (CONVENTION of reporting, not a rule; COMPUTATION, NOT A CLEARANCE beyond what Q7
itself decides):**
- **Value range:** $87 to $163 a share (Q3-capped).
- **Fair price** (the central base, $1,910M, the mean of the two methods, at the capped 1.4% growth, discounted at the
  10% floor): **about $66 a share, or about $89 with the Quantinuum stake at its carrying value.**
- **Cheap price** (no-growth owner cash on the low base clears the 10% floor with no growth at all): **about $49 a share**.
- **The price, $214.14,** is above the top of the range, and its expected return in every case the Q3 cap allows (2.3% to
  4.2%) is below both the floor and the Treasury.

**Closes.** The price sits above the top of the narrower range; by the PG specific, "a price above the top of the range
closes OUT through the floor convention". The close does not depend on which method of STEP 0 is right, on the
Quantinuum stake, or on the reading of "pre-tax": the most generous case the cap allows gives 4.2%. It does not even
depend on the cap except through the one case (19.6% for ten years) that the row on absurdities rules out. "If you
need to use a computer or a calculator to make the calculation, you shouldn’t buy it" **[M2009-005]**; "there’s just a
point at which we drop out of the game" **[M2003-149]**. The doubts of Q2 to Q6 enter as "the degree of certainty"
**[M1999-104]** and would only lower the range.

**VERDICT: OUT.** The file closes here.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed OUT). COMPUTATION — NOT A CLEARANCE: the 30-year Treasury at 5.66% exceeds the expected return
at the price in every case Q7 allows (2.3% to 4.2%); "one opportunity cost of buying the stock is to compare it with a
bond" **[M1997-089]**.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED as a clearance.** Recorded because the facts were read: on the pro forma balance sheet at 2026-03-31 the
new company carries debt of $20.9B (commercial paper $4.6B, current maturities $3.1B, long-term $13.2B) against cash and
short-term investments of $11.4B (Ex. 99.3), before the $1,750M Johnson Matthey purchase of July 2026; net debt of
roughly $9.5B to $11B is four to seven years of the owner cash of STEP 0. Relating debt to the ability to pay
**[M1995-104]**, ruin is not in view, but the "little or no debt" description **[R1997-001]** does not fit, and the
commercial paper and current maturities, $7.7B, must be met or rolled **[L2010-020]**. Would weigh AGAINST, mildly.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** Inaction is the default **[M2003-070]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** No business named in the rows (casinos, tobacco, loading schemes) is among Honeywell Technologies'; nothing
in the documents read would trouble the newspaper test **[M2008-011]**.

---
## THE BOX
**OUT at Q7.** Honeywell Technologies (the automation company left after the Aerospace spin and the 1-for-2 reverse split
of 2026-06-29) passes Q1 and Q2 (Building Automation's castle widening, Process Automation standing, the failed hardware
being sold), with Q3 undecided and Q4 to Q6 weighing against; but at **$214.14** against a value range of **$87 to $163 a
share** (owner cash reconstructed at $1.56B to $2.26B a year, growth capped at the 1.4% of sales shown, the Quantinuum
stake at zero to carrying value), the expected return is 2.3% to 4.2%, below the ~10% floor and below the 5.66%
Treasury. Fair price about $66 (about $89 with the stake); cheap price about $49. COMPUTATION figures as labelled.
**Reversal condition:** the first filed statements of the new company (the Q3 2026 10-Q, then the FY2026 10-K) showing
owner cash after every real cost of roughly $6B a year or more, or the price falling to about $90 or below with the
filed cash in the band, would reopen Q7; nothing short of a near-tripling of owner cash, or a price near the fair price,
changes the box.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `87d4824`, before the first EDGAR request); written question by
      question; committed after each (`4db871b` STEP 0 to standing rule, `65271f3` Q1, `d96060d` Q2, `996cc24` Q3,
      `a9cc802` Q4, `bb6fe5e` Q5, `d19e2da` Q6, `50945f5` Q7 to Q12), each with a pathspec, with `git status --short`
      checked before each commit and no raw filing staged (all downloads under `cache/`, gitignored).
- [x] Every v5 id resolves (`check_ids.py` against `principle_ledger_v5.csv`: none missing, no v4 E-id); every filing
      fact has its accession; non-filing figures: the quote only (aggregator, flagged). The 21% statutory rate used in
      STEP 0 is labelled CONVENTION.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED and their figures are
      labelled COMPUTATION or recorded without a verdict.
- [x] Owner cash after every real cost (all capital spending, stock pay), never a net-income proxy: Method B is net
      income with non-cash charges added back and all capital spending deducted, stated as such, and Method A is cash;
      the sovereign from the US Treasury; the quote flagged.
- [x] Contrary evidence written down as found (Foundations line (a) to (e), carried into Q2, Q4, Q6).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` used; its owner-earnings table and "yield" were found to mix the old
      three-business company with the new share count and were not used (defect reported).
- [x] `python tools/check_framework.py` PASS before every commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **A company that has just changed shape has no five years.** The Q7 convention asks for a five-year
average of owner cash; Honeywell Technologies has three years of pro forma figures, two of recast segments and none of
filed cash flows. Nothing in the framework says whether to close TOO HARD (WORK) and wait for the first filed statements,
to reconstruct from the parent's and the spun-off company's statements, or to fall back on the parent's history. I
reconstructed two ways and carried the band into the range, because the close did not depend on it; a rule is needed for
the case where it would (for example: reconstruct, and close TOO HARD (WORK) if the two methods straddle the price). (2)
**Q4's confusion STOP does not distinguish transformation from obfuscation.** The rows read confusion as a sign of purpose
**[M2003-029]**; here the confusion is structural and the company furnished the bridges. I closed IN narrowly; a second
analyst could close it TOO HARD (WORK) on the same facts, which is the kind of split the correction pass meant to remove.
(3) **The buyback convention cannot be run across a spin-off**: every share bought carried businesses since distributed,
and the Q7 range is for what is left. I recorded the test as not runnable and weighed on the stated purpose. The
convention could say: run it only on purchases made in the current shape, and say so otherwise. (4) **The growth shown
on aggregate owner cash can change sign with the method of reconstruction** (19.6% a year against a decline); the PG
specific does not say what to do when the measure itself is unstable. I capped at sales growth, as the ETN run did on
other grounds; the framework should name the cap. A tool defect besides: `tools/run.py` uses total operating cash flow
including discontinued operations and the pre-spin financials against the post-spin, post-reverse-split share count,
which for a company that has just spun off its larger half yields a meaningless "yield" (7.20% here); it should warn
when the latest 8-K reports a completed spin-off or a reverse split.
