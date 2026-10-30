# Company Run — EMCOR Group, Inc. (NYSE: EME) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Working folder:
`Test Runs/_research 2026-10-05 EME/` (filings as text, the XBRL extraction script, the peer table, the owner-cash and
range arithmetic). Every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that
returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** NOT CHECKED. This is a blind run: `PORTFOLIO.md`, the holding reviews,
the session-state files, the queue register and the prepped reading list were not opened, and no other run file about
this company was opened. Whether the operator holds this name is unknown to the analyst.

**CONTAMINATION, declared.** (1) The session context showed the last five commit subjects of the repository, which
include other v5 runs of the same day (UTI TOO HARD (NATURE) at Q1, PWR TOO HARD (WORK) at Q2, LINC OUT at Q2) and a
commit named "the electrical-trades run list (16 names, top down)". So the analyst knew that a peer in this run (PWR)
closed TOO HARD (WORK) at Q2 under v5 the same day, and that EME is probably on a list of electrical-trades names. Nothing
in that context says whether anyone holds or wants EME. The PWR verdict was not used as evidence; PWR enters this file
only through its own filings, as a competitor. (2) The project memory index, loaded with the session, carries general
lines about the queue ("57 gate-clearers, nothing buyable") and nothing about EME. (3) A directory listing of
`Test Runs/` grepped for "EME" returned only unrelated names (Chemed, Element Solutions, Brookfield Asset Management, an
addendum); none was opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $785.57 (2026-10-05, from `tools/run.py`'s live quote; **aggregator, live quote only**, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock, **44,109,901** shares (10-Q for the
  period ended 2026-06-30, filed 2026-07-30, accession `0000105634-26-000110`; cover as-of 2026-07-24;
  `python Screens/cover_shares.py EME`). The charter has preferred stock authorised, none issued (FY2025 10-K balance
  sheet).
- **Market cap:** 44.110M x $785.57 = **$34,651M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 10/02/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-26, accession `0000105634-26-000025` (Items 1, 1A, 5, 7, 7A, the four statements,
    Notes 3, 4, 12, 13, 14 (multiemployer section), 15); text in the working folder as `10K_FY2025.txt`.
  - 10-K for FY2024, filed 2025-02-26, accession `0000105634-25-000015` (fetched; used only for the series).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession `0000105634-26-000110` (MD&A, RPO, cash flow,
    buybacks).
  - Proxy (DEF 14A) filed 2026-04-21, accession `0001140361-26-015809` (fetched; pay design skimmed only, Q5 and Q6 not
    reached).
  - 8-Ks: 2025-02-03 (`0000105634-25-000006`, Item 2.01, Miller Electric bought for $865 million cash from an ESOP trust
    and family trusts); 2026-07-31 (`0000105634-26-000115`, Item 1.04, an MSHA imminent-danger order at a mine site
    worked by a subsidiary, no injuries); 2026-07-30 (`0000105634-26-000112`, Q2 results).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
  **$1,302,063 thousand** in the filed Consolidated Statement of Cash Flows (10-K `0000105634-26-000025`), against
  **1,302** (millions) in `tools/run.py`'s XBRL line. They agree. Capital spending $112,750 thousand against run.py's
  113: agree.
- `python tools/run.py EME` **arithmetic lines only** (Part VII): it printed SBC as **0** for every year. That is a tool
  gap, not a fact: the filed cash-flow statement shows "Non-cash share-based compensation expense" of $20,595 thousand
  (2025), $19,978 thousand (2024), $13,739 thousand (2023). SBC is resolved from the filing and the XBRL equity-statement
  tag below. Its D&A line (186 for 2025) adds depreciation $67.4M and amortization of acquired intangibles $119.1M.
  Nothing it printed as a rule, a floor or an id was read.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own EMCOR "if the market closed for five years"
**[M1997-109]**, which turns the run on what the contracting business will earn, not on the quotation's three-year
rise. The market serves and does not instruct: "It just tells us prices." **[M2006-077]**; the record price and the
record backlog are facts about the market's mood and the order book, not about the castle. No macro forecast enters
**[M2016-053]**: the data-centre build-out is not forecast here; it enters only as a fact in the filings (revenue by
market sector) and as a question for the castle (is the margin the company's or the cycle's). Who is paid to tell you
**[M2020-037]**: the 10-K's competitive self-description is written by the seller of the stock; I give most weight to
the passages that cut against its interest. The analyst's habits: hunt "what’s wrong" **[M2025-013]**, write contrary
evidence down at once **[M1997-127]**, and put the last reading to "possibly reject your original hypothesis"
**[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. (Against OUT, found in Item 1.) An invitation to bid "is often conditioned upon prior experience, technical
   capability, and financial strength"; surety bonding is "often a condition to bidding for and winning" the largest
   projects; customers "frequently review the safety records of contractors during the bidding process", and EMCOR's
   recordable incident rate has been under half the industry average for seventeen consecutive years. That is a
   prequalification wall the small firm may not clear, and it is the kind of customer the rows describe as not taking
   the low bid **[M2001-014]**, **[M2016-006]**.
2. (Against OUT, found in the balance sheets.) Customers prepay: contract liabilities of $2,327M against contract assets
   of $338M at 2025-12-31; the business runs on its customers' money and its return on tangible assets was 12.7% to
   15.4% pre-tax even in the ordinary years 2015 to 2019 (peer table below). That is not the "terrible" average of a
   commodity field **[M2000-072]**.
3. (Against OUT, found in the 10-Q.) Remaining performance obligations reached a record $17.14 billion at 2026-06-30,
   up from $11.91 billion a year earlier, with the second-quarter operating margin at 10.6%.
4. (For OUT, found in Item 1 and 1A.) "relatively few barriers exist to prevent entry"; "Certain of our competitors have
   lower overhead cost structures"; "A majority of our revenues are derived from projects requiring competitive bids";
   building-services contracts lost "upon rebid". Recorded at Q2.
5. (For OUT, found in the peer table.) Every building-trades peer's margin rose with EMCOR's in 2023 to 2025 (Comfort
   Systems 6.1% to 14.4%, IES 2.6% to 11.4%, Limbach 2.4% to 7.6%), and before the rise EMCOR's margin sat below
   Comfort Systems' in every year 2015 to 2022.
6. (For OUT, found in the XBRL series.) 2009 to 2010: revenue fell from $6,785M (2008) to $5,121M (2010), and 2010
   closed with an operating loss of $29M after $246M of goodwill and intangible write-downs.

## THE STANDING RULE
Buying a share of a debt-free contractor for cash puts no buyer at risk of ruin, provided it is bought with the buyer's
own money and sized so that a fall of half does not force a sale: "never going to risk what we have and need for what
we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**.
No issue for the buyer's conduct; the question did not have to be applied since the file closes before sizing.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** About 100 operating subsidiaries that design, install and maintain the
  electrical, mechanical, plumbing, fire-protection and control systems inside buildings and plants; 2025 revenue
  $16.99 billion, 97% in the United States, 72% construction, 21% building services, 7% refinery and petrochemical
  industrial services (10-K FY2025, Item 1). The product is skilled labour plus purchased equipment, sold on contract.
  About 62% of the 44,000 employees are union members under about 450 local collective bargaining agreements, and the
  company contributes to about 200 multiemployer pension plans ($725.7M of contributions in 2025) (Item 1, Note 15,
  MD&A). The UK operations were sold on 2025-12-01 (the $144.9M gain sits in 2025 operating income).
- **The key variables and whether they are foreseeable** **[M1998-044]**. Two variables decide the earnings: (1) the
  volume of non-residential building, plant and data-centre construction and renovation in the US, and (2) the gross
  margin EMCOR can win and hold on fixed-price and guaranteed-maximum-price work. The first is cyclical but its shape is
  visible in the filings (revenue fell about a quarter from 2008 to 2010 and recovered over five years). The second is
  the castle question, which Q2 asks. "I never would understand the chemistry of it [...] What is important is that I
  understand the economic dynamics of the industry." **[M2011-014]**: the dynamics here (bid, execute, bill ahead,
  collect retainage, carry labour through the cycle) are plain from Item 1, Note 3 and the cash-flow statement.
- **Do the past statements tell me the future ones** **[M2008-033]**? Partly. The filings since 2008 show a
  business that never lost its revenue base and earned 3% to 5.5% operating margins before 2023 and 7% to 10% since;
  the statements say what kind of business it is, and Q2 asks which of the two margin regimes is its own.
- **Fast change?** No. The technology in the product (switchgear, chillers, controls, prefabrication, BIM) changes, but
  the work is installed by hand, on site, in the US, and the routing to Q1 TOO HARD for an industry whose ten-year
  economics are out of reach through rapid change **[M1998-008]** does not apply. The industry's insiders would write
  down, to a reasonable band, where a large specialty contractor's economics will sit in ten years (they publish
  multi-year margin and backlog commentary; the forecast is cyclical, not unknowable) **[M2000-105]**.
- **Doubt test** **[M2002-092]**: I do not doubt that I understand how this business makes and loses money; the doubt
  is about the durability of its margin, which is Q2's question, not Q1's (the framework's order: "can I understand
  it?" **[M1995-051]**, then the castle).
- **VERDICT: IN.** The economics and the position can be described ten years out to the precision the rows ask, "a
  reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**, with the margin question passed to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? [...] And how permanent are they?" **[M1995-038]**, asked from the
attacker's side, because competitors "will repeatedly assault" any castle earning high returns **[L2007-004]**.

**The castle tests, each with its filing fact.**

1. **The attacker with money** **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on
   See’s Candy, could I do it? [...] If the answer had been yes, we wouldn’t have done it." The filer answers the
   question itself, in Item 1 (Competition): "relatively few barriers exist to prevent entry into the electrical and
   mechanical construction services industry", and of building services, "there are relatively few barriers to entry";
   in Item 1A: "any organization that has adequate financial resources, and access to technical expertise, may become a
   competitor" (10-K `0000105634-26-000025`). The record shows the attack succeeding: Comfort Systems grew revenue from
   $1,581M (2015) to $9,102M (2025) and IES from $574M (FY2015) to $3,371M (FY2025), each partly by buying local
   contractors, in EMCOR's own markets (peer XBRL, accessions below). The money test is answered yes by the filer and
   by the peers' growth. "Normally, if you’ve got a profitable business, you know, a dozen people want to go into it."
   **[M2000-077]**; here they do, and the filer names nine larger ones and "thousands of small companies".
2. **Pricing power and the agony before a rise** **[M2005-020]**: Item 1A: "Competition can place downward pressure on
   our contract prices and profit margins, which may make it difficult to win the project or force us to accept
   contractual terms and conditions that are less favorable to us"; of materials, "there can be no assurance that
   price increases of commodities, if they were to occur, would be recoverable". A business that must win each price
   in a sealed bid has no list price to raise; the test is not met.
3. **Unit volume and share of mind.** Not applicable in the consumer sense; the nearest measure is the order book,
   which is at a record ($17.14B at 2026-06-30). Volume is strong; the test is whether the money comes with it, and
   that is test 6 and the peer row.
4. **The low-cost position** **[L2004-007]**, **[M1997-010]**: "commodity businesses have risk unless you’re the
   low-cost producer". The filer says it is not: "Certain of our competitors have lower overhead cost structures and,
   therefore, are able to provide their services at lower rates than we are currently able to provide." (Item 1A).
   Through 2015 to 2022 its operating margin sat below Comfort Systems' in every year (peer row). The commodity
   exception the rows name is not available to it on its own evidence.
5. **The brand in the customer's mind.** The customer is a general contractor, developer or owner choosing among
   prequalified bidders; "A majority of our revenues are derived from projects requiring competitive bids" (Item 1).
   The EMCOR name is not asked for by the end user; most work is done under about 100 subsidiary names.
6. **Would the customer still choose it over the low bid** **[M2017-009]**? The filer: "Our project and service work is
   frequently awarded through a competitive bidding process, which is standard in our industry. We are constantly
   competing for contracts based on pricing, schedule, and technical expertise." (Item 1A). The contrary evidence
   (Foundations, item 1) is real: prequalification, bonding and safety records narrow the bid list, and on the data
   centres schedule and reliability matter to the owner, as "the people care enormously about service and the
   assurance of safety" **[M2001-014]**. But inside the narrowed list the work is re-bid job by job, and the filer
   reports losing building-services contracts "upon rebid" (Item 1A; MD&A, commercial and government site-based
   divisions). The customer does not buy "for the low bid" alone, and does buy on the bid; that is the industry's
   standing, not EMCOR's castle, since every prequalified rival clears the same wall.
7. **Ask the competitors** **[M2017-091]**: "everybody loves talking about their competitors". Their own 10-Ks:
   - Comfort Systems USA (FY2025 10-K, `0001104659-26-017530`): "the high degree of competition and low barriers to
     entry in most of our markets".
   - IES Holdings (FY2025 10-K, `0001048268-25-000174`): "We enter into contracts principally on the basis of
     competitive bids."; "There are few barriers to entry for electrical contracting services in the residential
     markets."
   - Limbach Holdings (FY2025 10-K, `0001628280-26-013285`), of plan-and-spec bidding: "The Company believes price is
     the predominant selection criteria in this process."
   - Quanta Services (FY2025 10-K, `0001050915-26-000006`): "Relatively few barriers prevent entry into some areas of
     our business".
   - MYR Group (FY2025 10-K, `0000700923-26-000007`), the one dissent, for utility transmission and distribution, not
     building trades: "There are a number of barriers to entry into the T&D markets, including the cost of equipment
     and tooling [...]"; and still "We enter into contracts principally through a competitive bid process."
   Four of five peers describe the field as EMCOR does. None names a rival it could not displace.
8. **Widening or narrowing** **[M1999-108]**? Margins widened from 5.1% (2022) to 9.2% (2025, excluding the UK gain)
   and 10.6% (Q2 2026). The question is whose widening. The competitor row below shows the same widening at Comfort
   Systems, IES and Limbach in the same years, and none at the utility-line contractors (MYR, Quanta). A rise that
   every building-trades contractor enjoyed at once is the tide of a market short of skilled labour and long of
   data-centre work, not a moat EMCOR dug. The rows require that such a return be read for "a cyclical peak in
   earnings" before it is credited **[L1994-009]**, and that the improvement one firm gets "your competitor gets the
   next day" **[M2004-053]**. The data-centre share is concentrated and new: network and communications revenue was
   $1,345M in 2023 and $4,132M in 2025 (48% of US electrical and 23% of US mechanical construction revenue in 2025,
   Note 3); the filer: "If such spending were to decrease, demand for our services could decline" (Item 1A).
9. **What could destroy, modify or reduce it** **[M2000-014]**? A turn in non-residential and data-centre spending,
   which the filer has lived through: revenue fell from $6,785M (2008) to $5,121M (2010), and 2010 ended with an
   operating loss of $29M after goodwill and intangible write-downs of $246M; further write-downs of $58M (2017) and
   $233M (2020) (XBRL `GoodwillAndIntangibleAssetImpairment` and `AssetImpairmentCharges`, EME 10-Ks for those years). "During
   economic downturns, there have typically been fewer small discretionary projects from the private sector and our
   competitors have aggressively bid larger long-term infrastructure and public sector contracts." (MD&A, Liquidity).

**The competitor row** (same metric from each company's own XBRL as first filed in its 10-K; operating income over
revenue, and pre-tax operating income over tangible assets, total assets less goodwill and intangibles; tagged data is
transcription and screening, operator rule 4; the EME figures for 2023 to 2025 were checked to the filed statements).

| Year | EME margin | EME OI/TA | FIX margin | FIX OI/TA | IESC margin (FY Sep) | IESC OI/TA | MYRG margin | LMB margin | PWR margin |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | 4.3% | 12.9% | 5.7% | 17.8% | 3.2% | 9.0% | n/a (tag) | n/a | n/a (tag) |
| 2016 | 4.1% | 12.7% | 6.2% | 19.6% | 3.6% | 7.7% | 3.4% | n/a | 4.2% |
| 2017 | 4.3% (5.1% before write-downs) | 13.2% | 5.6% | 16.4% | 2.5% | 5.9% | 2.1% | 1.2% | 4.0% |
| 2018 | 5.0% | 15.4% | 6.9% | 20.5% | 3.0% | 7.6% | 3.3% | 0.2% | 4.8% |
| 2019 | 5.0% | 14.6% | 6.3% | 16.2% | 3.9% | 11.4% | 2.8% | 1.5% | 4.6% |
| 2020 | 2.9% (5.6% before write-downs) | 7.1% | 6.7% | 18.0% | 4.2% | 10.7% | 3.9% | 3.0% | 5.5% |
| 2021 | 5.4% | 13.4% | 6.1% | 14.4% | 5.6% | 14.5% | 4.7% | 2.9% | 5.1% |
| 2022 | 5.1% | 14.1% | 6.1% | 14.8% | 2.6% | 7.3% | 3.8% | 2.4% | 5.1% |
| 2023 | 7.0% | 17.3% | 8.0% | 17.7% | 6.7% | 19.2% | 3.5% | 5.7% | 5.4% |
| 2024 | 9.2% | 22.2% | 10.7% | 22.0% | 10.4% | 27.2% | 1.6% | 7.4% | 5.7% |
| 2025 | 10.1% (9.2% before the UK gain) | 25.3% | 14.4% | 26.7% | 11.4% | 26.5% | 4.6% | 7.6% | 5.7% |

Accessions (FY2016 / FY2019 / FY2022 / FY2025 10-Ks): EME `0000105634-17-000043`, `0000105634-20-000043`,
`0000105634-23-000005`, `0000105634-26-000025`; FIX `0001558370-17-000882`, `0001558370-20-001491`,
`0001558370-23-001757`, `0001104659-26-017530`; IESC `0001193125-16-789187`, `0001048268-19-000007`,
`0001048268-22-000099`, `0001048268-25-000174`; MYRG `0001144204-17-013721`, `0001104659-20-029253`,
`0000700923-23-000012`, `0000700923-26-000007`; LMB `0001144204-17-020753`, `0001628280-20-007572`,
`0001628280-23-007012`, `0001628280-26-013285`; PWR `0001193125-17-064821`, `0001050915-20-000020`,
`0001050915-23-000010`, `0001050915-26-000006`. Full table with tangible capital employed: `peer_table.txt` in the
working folder. Return on tangible capital employed (equity plus debt less cash, goodwill and intangibles) is not
usable for EME: the figure is near zero or negative in most years (2016: -$270M; 2025: $41M) because customer
prepayments and payables finance the whole working capital; that is why the table uses tangible assets **[M2011-060]**.

**Reading the row.** Through the full cycle EMCOR is a middle-of-the-pack building-trades contractor: below Comfort
Systems on margin and return on tangible assets in every year 2015 to 2022, above IES, MYR and Limbach. Its pre-tax
return on tangible assets of 13% to 15% in ordinary years is decent, made by fast turnover of a thin margin on capital
its customers supply, and the peers who run the same model earn the same or more. In 2023 to 2025 the whole group rose
together. Nothing in the row separates EMCOR from the field; the row shows a field.

**Weighing it, with the contrary evidence.** The case for a castle is the prequalification wall (experience, bonding,
safety, balance sheet) and the scale to take $200M projects **[M2001-014]**. Against it: the filer's own statements that
entry barriers are few, that lower-overhead rivals can underprice it, and that most work is won by bid; four of five
peers saying the same of the field; the peer row showing no persistent EMCOR edge; the record margins shared by every
building-trades rival; and a history of slack years in which revenue fell a quarter and acquired goodwill was written
down three times (2010, 2017, 2020). The wall is real but common to every prequalified bidder: it decides who may bid,
not who wins or at what margin. In the rows' words this is a field that is "just never going to have barriers to
entry. And in those industries, you better be running very fast" **[M2012-106]**, where "anything you do, your
competitors can copy" **[M1996-017]**, where "the guy with the lower cost comes in and kills you" **[M2001-013]**, and
where the customer, like the insured, largely does not "care from whom they buy" inside the bid list
**[L2004-003]**. One test that does not apply, written down so that it is not borrowed: the rows' warning about "a very
high labor content and that has a product that can be shipped in from abroad very easily" **[M2007-116]** is half true
here; the labour content is high but the work cannot be shipped in, so foreign competition is not the threat.

**Open or unjudgeable?** The framework sends a castle shown open on the evidence to OUT and a castle whose future
cannot be judged to TOO HARD **[M2000-019]**, **[M2006-013]**. This is not a case of a moat "tenuous in any way" **[M2000-019]** whose
value cannot be judged; the filer, its competitors and the margin record since 2008 all say the same thing, that
there is no moat to judge: the money test is answered yes **[M2011-015]**, and the castle stands because the market is
strong, not because entry is barred. A future price cannot reopen it: "What you can’t do is turn any investment into a
good deal by paying little" **[M2019-015]**.

**Disconfirmation, the last pass** **[M1998-144]**. What would have closed this IN: a filed statement or record that
EMCOR wins work its rivals bid for at higher prices (a negotiated share above the industry's, or margins above
Comfort Systems' through the slack years). The 10-K gives the opposite on the first ("A majority of our revenues are
derived from projects requiring competitive bids") and the peer row the opposite on the second. The FY2025 10-K does
not state the negotiated share as a number; that is recorded under what could not be got.

- **VERDICT: OUT.** The castle is shown open on the filed evidence: few barriers to entry by the filer's own statement,
  work won mostly by competitive bid, not the low-cost operator by its own statement, no persistent margin or return
  edge over its peers through 2015 to 2022, and a margin rise since 2023 shared by every building-trades rival.
  **[M2011-015]**, **[M2012-106]**, **[M1997-010]**, **[L1994-009]**.

**The file closes here.** Q3 to Q12 are NOT REACHED. What follows them is recorded at the owner's request and is
**COMPUTATION — NOT A CLEARANCE**; it carries no entry language and does not reopen Q2.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING. **NOT REACHED.**
**COMPUTATION — NOT A CLEARANCE.** Recorded for the owner, not weighed. Capital spending ran $35M to $113M a year
(2015 to 2025) against depreciation of $36M to $67M; the business needs little fixed capital, and its working capital is
negative (net contract liabilities $1,990M at 2025-12-31). Pre-tax operating income over tangible assets was 12.7% to
15.4% in 2015 to 2019 and 2021 to 2022, 22% to 25% in 2024 to 2025 **[M2011-060]**. The growth has been bought as well as
earned: acquisitions of $1,022M in 2025 (Miller Electric $876.8M), $228M in 2024; 2025 acquired revenue $1.27B.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? **NOT REACHED.**
**COMPUTATION — NOT A CLEARANCE.** The balance sheets, read 2016 to 2025 before the income account **[M2025-032]**
(`tools/run.py` table; FY2025 statements read in the filing):
- **Equity against goodwill and intangibles.** Equity $1,537M (2016) to $3,674M (2025); goodwill plus intangibles
  $1,467M to $2,521M. Tangible equity was about $70M in 2016 and $1,153M in 2025. Most of the equity a buyer of 2016
  owned was purchased goodwill, written down in 2017 and 2020.
- **Retained earnings against equity.** Retained earnings rose $1,596M to $6,006M while treasury stock rose to $2,432M:
  about $2.97B spent on buybacks since 2011 (Note 12), so book equity grew by less than half of what was earned.
- **Receivables against sales.** Receivables $1,495M on $7,552M revenue (19.8%) in 2016; $4,241M on $16,986M (25.0%) in
  2025, including retainage of $944.5M and claims of $116.1M in receivables (up from $6.9M in 2024) (Note 3). Rising
  claims are a figure to watch.
- **Customer money.** Contract liabilities $489M (6.5% of revenue) in 2016, $2,327M (13.7%) in 2025. The boom brought
  the customers' prepayments; operating cash flow of $3,610M in 2023 to 2025 exceeded net income of $2,913M partly for
  that reason, and the 2025 MD&A already records the unwind: OCF fell "as we worked through these upfront payments". In
  a downturn this float returns to the customers, as the 2010 OCF of $69M shows.
- **Cash and debt.** Cash $465M to $1,112M; no funded debt at 2025-12-31 or 2026-06-30 (Note 9; 10-Q); the revolver was
  drawn $525M and repaid in 2025 for Miller Electric.
- **Off the balance sheet.** Surety exposure about $3.03B (23% of RPO); open purchase obligations $3.07B; about 200
  multiemployer pension plans with withdrawal liability the company cannot estimate (Note 14); self-insured liabilities
  $291.0M net.
- **Income account.** Real costs counted: depreciation, amortization of acquired intangibles (customer relationships and
  backlog deplete as the work is done), stock pay of $20.6M (2025). Project write-downs over $1M each: $85.9M (2025),
  $66.3M (2024), $29.1M (2023), rising with size (Note 3). No EBITDA in the filer's own mouth was found in the 10-K;
  the proxy pays on "adjusted" EPS and an "adjusted" cash-to-income ratio (not weighed; Q6 not reached).

## Q5 — WHO RUNS IT? **NOT REACHED.**
Noted, not weighed: Anthony Guzzi, president since 2004, chief executive since 2011, chairman since 2018 (10-K,
executive officers); 2025 total pay $14,380,630 (proxy `0001140361-26-015809`).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? **NOT REACHED.**
**COMPUTATION — NOT A CLEARANCE**, recorded for the owner: buybacks of $586M (2025) at prices up to $669.69 a share in
the fourth quarter (Item 5); the program names no price above which it stops (Note 12). Against the computation range
below ($322 to $503 a share on the base case), the 2025 fourth-quarter prices ($607.79 to $669.69) sit above the top.
The proxy states that the chief executive "together with certain other named executive officers, developed proposed
2025 financial metrics" for his own annual bonus; this is the pattern "the beneficiary is the one that also really does
all the design" **[M1997-041]**. Neither is weighed; the file closed at Q2.

## Q7 — WHAT IS IT WORTH? **NOT REACHED.**
**COMPUTATION — NOT A CLEARANCE.** Built by the v5 CONVENTION (Part VI) so the owner can see the arithmetic; it carries
no entry language. Value is "the discounted value of the cash that can be taken out of a business during its remaining
life" **[R1996-018]**, at the long government rate **[L2000-021]**.

- **Owner cash after every real cost** (operating cash flow, less stock pay added back in it, less all capital
  spending), USD millions; filed figures for 2023 to 2025, XBRL as first filed for earlier years:

| Year | OCF | SBC | Capex | Owner cash | Depreciation variant | Net acquisitions | After acquisitions |
|---|---|---|---|---|---|---|---|
| 2021 | 319 | 11.1 | 36 | 272 | 259 | 118 | 153 |
| 2022 | 498 | 12.1 | 49 | 437 | 439 | 99 | 338 |
| 2023 | 900 | 13.7 | 78 | 808 | 834 | 96 | 711 |
| 2024 | 1,408 | 20.0 | 75 | 1,313 | 1,331 | 228 | 1,085 |
| 2025 | 1,302 | 20.6 | 113 | 1,169 | 1,214 | 765 (1,022 less UK proceeds 257) | 403 |

  Five-year average **$799M** (depreciation variant $815M; after net acquisitions $538M). The ten-year average 2016 to
  2025 is $579M. The five-year window starts at a low base and ends at the top of the boom; the rows warn of the base
  year **[L2005-003]**, and the window includes $1.8B of customer prepayments that will return.
- **Growth shown** on aggregate owner cash, 2021 to 2025: 44% a year. Capped at the discount rate, 5.63%, by the Q3
  arithmetic **[M1997-095]**; the uncapped figure is the absurdity the rows forbid.
- **Range** (ten years, then zero nominal growth, at 5.63%): no-growth end **$14,200M = $322 a share**; shown-growth end
  (capped) **$22,194M = $503 a share**. Width 1.56 to 1, under the three-to-one line, so not TOO HARD by width.
  Sensitivities: after acquisitions $217 to $339; ten-year average $233 to $365; three-year average (the boom alone)
  $441 to $690.
- **Against the price** of $785.57: above the top of every variant, including the boom-only three-year case. At the
  price the after-tax owner-cash yield is 2.31% (3.12% pre-tax equivalent at the 26.1% tax rate of 2025); expected
  pre-tax return 3.1% with no growth, 8.75% with growth at the cap. Both are below the floor of about ten percent
  pre-tax (CONVENTION, from "a very high probability of at least 10% pre-tax returns" **[L2002-020]** and **[M2003-149]**).
  Had Q2 passed, Q7 would close **OUT** through the floor convention.
- **Fair-price band (the owner's request, COMPUTATION):** prices inside the value range at which the expected pre-tax
  return reaches about 10%. With growth at the cap, every price in the range clears it (the 10% price on that case is
  $561, above the range top of $503), so the band would be **$322 to $503**; with no growth, no price inside the range
  clears it (the 10% price is **$245**, below the range bottom). Read against the bottom of the range, as the rows
  read it **[L2013-012]**, the band is empty on the conservative case.
- **Cheap price (COMPUTATION, the analyst's reading, not a rule):** about **$245 a share**, where the no-growth case
  alone returns 10% pre-tax and the price sits about a quarter below the range bottom; at that price the decision would
  not need the growth case, which is the nearest the arithmetic comes to "It should scream at you." **[M2009-005]**. It
  does not reopen Q2.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? **NOT REACHED.**
**COMPUTATION — NOT A CLEARANCE:** at 3.1% to 8.75% expected pre-tax against a 5.63% long Treasury, the stock does not
beat the bond on the conservative case.

## Q9 — COULD IT RUIN US? **NOT REACHED.**
Noted, not weighed: no funded debt; sudden-demand exposures are surety indemnities ($3.03B exposure, no losses known),
insurance collateral ($105.5M surety, $72.8M letters of credit), multiemployer withdrawal liability (unquantified), and
the PEMEX Deer Park release of 2024-10-10 (two deaths; subsidiaries named; the company expects insurance to cover "much
or all") (Note 15).

## Q10 — IS IT THE FAT PITCH? **NOT REACHED.**

## Q12 (optional) — **NOT REACHED.**

---
## THE BOX
**OUT at Q2.** The castle is shown open on the filed evidence: the filer says entry barriers are few and that
lower-overhead rivals underprice it, most work is won by competitive bid, four of five competitors describe the field
the same way, and the peer row shows no persistent EMCOR edge through 2015 to 2022 and a margin rise since 2023 shared
by every building-trades rival. Not TOO HARD: the deciding question was answered by the evidence, not left open. Range
(COMPUTATION, not reached as a clearance) $322 to $503 a share against $785.57.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not committed after each question**: the instruction for this run
      was not to commit; written top to bottom in one session.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, below); every filing fact has its
      accession; numbers carry a filing or are labelled COMPUTATION or CONVENTION.
- [x] The order was kept; Q2 closed the run; everything after it is headed COMPUTATION — NOT A CLEARANCE and carries
      no entry language.
- [x] Owner cash after every real cost from operating cash flow, stock pay and all capital spending; never a
      net-income proxy. Sovereign from the US Treasury, dated 10/02/2026. The price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, items 1 to 6).
- [x] Not a point-in-time run; rows of every date are admissible.
- [x] Only the arithmetic lines of `tools/run.py` were used; its SBC line (0) was a tool gap and was replaced from the
      filing.
- [x] `python tools/check_framework.py`: **PASS** (2026-10-05, after the last edit). A separate script
      (`check_ids.py`, `check_ids2.py` in the working folder) found no E-ids, no missing ids (52 distinct v5 ids), and no
      quoted fragment beside an id that is absent from that row (26 adjacent fragments checked).
- Honest limits: the peer series are XBRL as first filed, transcription not reading (operator rule 4); only the EME
  figures and the five peers' competition paragraphs were read in the filed documents. MYR and Quanta 2015 revenue and
  Limbach 2015 to 2016 are missing from the tags and left blank.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Open against unjudgeable at Q2 has no test for a field rather than a firm.** The framework sends a
castle "shown to be open" to OUT and one "whose future cannot be judged" to TOO HARD, but most of its failing-answer
rows are about a business losing a castle it had (the notch, the Roman candle). EMCOR never had one by its own account;
the evidence is a field with low barriers whose returns are decent because the field is prepaid and capital-light.
I read "the money test answered yes, by the filer and by the peers' growth" as "shown open"; a second analyst could read
the same-day PWR close (TOO HARD (WORK) at Q2) as precedent for TOO HARD here. A sentence saying that a filer's own
statement of low entry barriers, confirmed by the peer row, is evidence of an open castle (or is not) would settle it.
(2) **A decent return in a commodity-like field is not placed.** The commodity rows say "average is going be terrible";
this field's average pre-tax return on tangible assets is 13% to 15% because customers finance it. Q3 grades returns,
Q2 asks for a moat, and nothing says whether a field-wide, moat-less, decent return is OUT at Q2 or a WEIGHING at Q3.
I closed at Q2 on the moat, which is the STOP. (3) **Q7's convention breaks on a boom window and on bought growth.** The
five-year window here starts at a trough base and ends at a peak, and the "growth shown" (44% a year) is part acquired;
the convention measures growth on aggregate owner cash without deducting the acquisitions that bought it, and does not
say to. I showed the after-acquisitions variant beside the base case. Smaller: `tools/run.py` still prints SBC as 0
when a filer tags stock pay only on the equity statement; the template's write-early commit step conflicts with a run
instructed not to commit.
